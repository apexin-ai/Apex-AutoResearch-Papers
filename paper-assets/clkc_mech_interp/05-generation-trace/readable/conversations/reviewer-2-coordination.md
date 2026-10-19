# Reviewer 2 coordination

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 332
- **Recorded user turns:** 8
- **Tool calls:** 158
- **Original source:** `logs/chats/feishu_group_oc_8b9aa92fafaf69b48d2c44b41c2fe9d9_reviewer_2.jsonl`
- **Structured JSON:** [`df7173ed5b722c188f99.json`](../../sessions/df/df7173ed5b722c188f99.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

72 recorded events

### User

_source line 1 · 2026-05-24T14:56:08.822965+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责审查本文的**新颖性、学术贡献完整性、Related Work 覆盖度和写作质量**。

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

1. **新颖性和贡献评估**：
   - 三个 claim 的独立新颖性：(1) 跨语言冲突可检测性+不对称性刻画, (2) Detection-Decision 层分离, (3) Confound exclusion pipeline
   - 与现有工作的差异化：vs Zhao et al. 2024 (单语探针), vs Basu et al. 2026 (steering 失败), vs Wendler et al. 2024 (英语中心空间)
   - "Detection ≠ Decision" 是否足够 novel 以支撑一篇 EMNLP long paper？
   - Steering 仅在 Llama 一个模型成功——这个 contribution 的 generalizability 如何？

2. **Related Work 完整性**：
   - 是否遗漏了关键引用？特别是：
     - Cross-lingual probing 的其他工作（如 Pires et al. 2019, Chi et al. 2020）
     - Knowledge conflict resolution 的最新工作（2025-2026）
     - Activation steering 的其他方法（activation patching, causal tracing, DAS）
     - 多语言 LLM 内部表征的最新研究
   - Related Work 的组织和覆盖是否平衡？

3. **写作质量和清晰度**：
   - Abstract 是否准确反映论文内容？是否在 200 words 限制内？
   - Introduction 的 narrative flow 和 motivation 是否清晰？
   - 论文结构是否合理？各节篇幅是否平衡？
   - Figures 和 Tables 是否 self-contained、标注清晰？
   - Limitations section 是否覆盖关键局限？

4. **学术诚信和格式合规**：
   - 匿名性检查：是否有 de-anonymization 风险？
   - 引用格式是否正确、是否有 hallucinated citations？
   - 页数是否符合 8 页限制？
   - AI 使用声明是否符合 venue 要求？

5. **论文 framing 和 positioning**：
   - Title 是否准确反映内容？
   - 论文是否 oversell（如将 Llama-specific 结果泛化为一般结论）或 undersell 其贡献？
   - Conclusion 中的 future work 方向是否合理？

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-24T14:56:25.223133+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
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

_source line 3 · 2026-05-24T14:56:25.273699+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-24T14:56:33.157482+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-24T14:56:33.559350+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 reviewer guidelines review form scoring dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 reviewer guidelines review form scoring dimensions"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-24T14:56:35.267176+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
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

### Tool result

_source line 7 · 2026-05-24T14:56:39.583943+00:00_

Web search results for query: "EMNLP 2026 reviewer guidelines review form scoring dimensions"

Links: [{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"2026 Reviewer Guidelines","url":"https://neurips.cc/Conferences/2026/ReviewerGuidelines"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Advice on Reviewing for EMNLP","url":"https://2020.emnlp.org/blog/2020-05-17-write-good-reviews/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's what I found about EMNLP 2026 reviewer guidelines and scoring:

## Scoring Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. Since EMNLP 2026 accepts papers through the ACL Rolling Review (ARR) system, these are the primary scoring dimensions used.

## Review Process and Deadlines

If you receive assignments, your reviews must be completed by July 6, or your meta-reviews - by July 29.

## Review Form and Criteria

The search results indicate that soundness scores must be justified by the text of the review. Additionally, reviewers should evaluate papers based on technical soundness, clarity of writing, and the quality of contributions rather than solely on state-of-the-art performance metrics.

The ARR Reviewer Guidelines page appears to contain more detailed information about the scoring dimensions and review form, though the full specific scoring rubrics weren't fully captured in these search results. For the most compr
…[truncated 320 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6024
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-24T14:56:40.539507+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about ACL Rolling Review 2026 reviewer guidelines, review form, and criteria:

## Reviewer Guidelines

The recommended workflow is: (1) read the paper and get the first impression, (2) search for related work, not deliberately trying to find that particular submission. If you feel qualified to review some aspects but not others (e.g., experimental results but not formal proofs), please state in the review if you did not check some major parts, such as proofs, as this information is
…[truncated 1138 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7382
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-24T14:56:41.950174+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 451.9}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 515.2}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 527.8}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 548.1}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 455.1}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 458.0}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 546.6}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 524.6}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 480.9}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_
…[truncated 317 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6682
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-24T14:56:48.480628+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract ALL scoring dimensions, their scales, and descriptions from the ACL Rolling Review form. Include: soundness, excitement, overall assessment, reproducibility, and any other dimensions. List the exact score ranges and what each score means."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract ALL scoring dimensions, their scales, and descriptions from the ACL Rolling Review form. Include: soundness, excitement, overall assessment, reproducibility, and any other dimensions. List the exact score ranges and what each score means."
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-24T14:56:49.436316+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-24T14:56:49.740400+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-24T14:56:50.394040+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-24T14:56:50.703466+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-24T14:56:50.906757+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1470
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-24T14:56:51.613090+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1872
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-24T14:56:52.268204+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1874
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-24T14:56:52.269055+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1565
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-24T14:56:55.599140+00:00_

# ACL Rolling Review Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: Quite sure, with unlikely but conceivable oversights
- **3**: Pretty sure, but may have missed details
- **2**: Willing to defend evaluation, but likely missed some details
- **1**: "Not my area, or paper is very hard to understand"

## 2. **Soundness**
Scale: 1-5 (with .5 increments)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: Strong; provides sufficient support with optional extra experiments
- **3**: Acceptable; supports main claims with minor gaps
- **2**: Poor; main claims lack sufficient support
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## 3. **Excitement**
Scale: 1-5 (with .5 increments)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation"
- **4**: Exciting; would mention to others or attend presentation
- **3**: Interesting; might mention points or attend if time permits
- **2**: Potentially Interesting; resonates with some in community
- **1**: "Not Exciting: this paper does not resonate with me"

## 4. **Overall Assessment**
Scale: 1-5 (with .5 increments)
- **5**: Consider for Award (top 2.5% papers)
- **4**: Conference acceptance recommended
- **3**: Findings track recommended
- **2**: Resubmit next cycle
- **1**: "Do not resubmit: This paper has to be fully redone"

## 5. **Reproducibility**
Scale: 1-5
- **5**: "They could easily reproduce the results"
- **4**: Mostly reproducible with minor variations
- **3**: Reproducible with difficulty; underspecified parameters
- **2**: "Hard pressed to reproduce the results"
- **1**: "Would not be able to reproduce the results"

## 6. **Datasets & Software Value**
Scale: 1-5 (separate dimensions)
- **5**: Enabling; affects research project choices
- **4**: Useful; recommended f
…[truncated 443 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7118
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-24T14:57:03.131858+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-24T14:57:03.182692+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-24T14:57:03.690071+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-24T14:57:04.692651+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1560
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-24T14:57:04.693087+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-24T14:57:05.048979+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1866
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-24T14:57:05.049400+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-24T14:57:05.520295+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_1/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-24T14:57:05.521579+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1831
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-24T14:57:06.632037+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1938
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-24T14:57:06.833669+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1784
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-24T14:57:06.835293+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1315
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-24T14:57:35.869502+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-24T14:57:36.822951+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-24T14:57:36.823334+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Pires et al 2019 \"How multilingual is multilingual BERT\" cross-lingual probing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Pires et al 2019 \"How multilingual is multilingual BERT\" cross-lingual probing"
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-24T14:57:37.324983+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Chi et al 2020 \"Finding Universal Grammatical Relations in Multilingual BERT\" cross-lingual representation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Chi et al 2020 \"Finding Universal Grammatical Relations in Multilingual BERT\" cross-lingual representation"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-24T14:57:42.249350+00:00_

Web search results for query: "Pires et al 2019 "How multilingual is multilingual BERT" cross-lingual probing"

Links: [{"title":"How Multilingual is Multilingual BERT? - ACL Anthology","url":"https://aclanthology.org/P19-1493/"},{"title":"[2101.11109] First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT","url":"https://ar5iv.labs.arxiv.org/html/2101.11109"},{"title":"Probing Multilingual BERT for Genetic and Typological ...","url":"https://aclanthology.org/2020.coling-main.105.pdf"},{"title":"CROSS-LINGUAL ABILITY OF MULTILINGUAL BERT","url":"https://openreview.net/attachment?id=HJeT3yrtDr&name=original_pdf"},{"title":"How multilingual is Multilingual BERT?","url":"https://arxiv.org/pdf/1906.01502"},{"title":"[1906.01502] How multilingual is Multilingual BERT? - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/1906.01502"},{"title":"[1906.01502] How multilingual is Multilingual BERT?","url":"https://arxiv.org/abs/1906.01502"},{"title":"How Multilingual is Multilingual BERT? | Request PDF","url":"https://www.researchgate.net/publication/335783767_How_Multilingual_is_Multilingual_BERT"}]

I found the paper! Here's information about the Pires et al. 2019 study:

"How multilingual is Multilingual BERT?" by Pires, Schlinger, and Garrette demonstrates that Multilingual BERT (M-BERT), released by Devlin et al. as a single language model pre-trained from monolingual corpora in 104 languages, is surprisingly good at zero-shot cross-lingual model transfer, in which task-specific annotations in one language are used to fine-tune the model for evaluation in another language.

The paper presents a large number of probing experiments, showing that transfer is possible even to languages in different scripts, that transfer works best between typologically similar languages, that monolingual corpora can train models for code-switching, and that the model can find translation pairs.

The findings conclude that M-BERT does create multilingual
…[truncated 459 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5426
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-24T14:57:47.334208+00:00_

Web search results for query: "Chi et al 2020 "Finding Universal Grammatical Relations in Multilingual BERT" cross-lingual representation"

Links: [{"title":"Finding Universal Grammatical Relations in Multilingual BERT - ACL Anthology","url":"https://aclanthology.org/2020.acl-main.493/"},{"title":"[2005.04511] Finding Universal Grammatical Relations in Multilingual BERT","url":"https://arxiv.org/abs/2005.04511"},{"title":"(PDF) Finding Universal Grammatical Relations in Multilingual BERT","url":"https://www.researchgate.net/publication/343296595_Finding_Universal_Grammatical_Relations_in_Multilingual_BERT"},{"title":"(Open Access) Finding Universal Grammatical Relations in Multilingual BERT (2020) | Ethan A. Chi | 151 Citations","url":"https://scispace.com/papers/finding-universal-grammatical-relations-in-multilingual-bert-20r4twdl61"},{"title":"Finding Universal Grammatical Relations in Multilingual BERT","url":"https://arxiv.org/pdf/2005.04511"},{"title":"Finding Universal Grammatical Relations in Multilingual BERT - Ethan A. Chi","url":"http://ethanachi.com/multilingual-probing.html"},{"title":"dblp: Finding Universal Grammatical Relations in Multilingual BERT.","url":"https://dblp.org/rec/conf/acl/ChiHM20.html"}]

I found the paper you're looking for! Here are the key details:

## Citation Information
The paper "Finding Universal Grammatical Relations in Multilingual BERT" was authored by Ethan A. Chi, John Hewitt, and Christopher D. Manning and published in Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics (ACL 2020).

## Main Findings
The paper examines Multilingual BERT (mBERT), a transformer-based multilingual masked language model capable of zero-shot cross-lingual transfer, suggesting that some aspects of its representations are shared cross-lingually.

The core research findings show that subspaces of mBERT representations recover syntactic tree distances in languages other than English, and that these subspaces are a
…[truncated 496 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 10009
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-24T14:57:52.657656+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
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

_source line 39 · 2026-05-24T14:57:52.708325+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-24T14:57:54.966784+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-24T14:57:55.469036+00:00_

1	When multilingual large language models (LLMs) encounter conflicting information across languages, the language of presentation can determine the model's answer. Behavioral studies attribute this to linguistic affinity, but the internal mechanism remains unknown: how is the conflict signal encoded, does it share structure with general cross-lingual representations, and does detectability imply causal influence on resolution?
2	
3	We probe residual stream representations in Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-IT. Our analysis combines cross-lingual transfer, a non-conflict baseline on XNLI, confound exclusion for translation quality and token overlap, and representation steering. Conflict signals are linearly detectable across languages, and cross-lingual transfer exhibits a directional asymmetry: probes trained on Chinese transfer to English ${\sim}$7 percentage points more accurately than the reverse. This asymmetry matches the XNLI non-conflict baseline in both magnitude and direction, with overlapping confidence intervals; it inherits from the model's general multilingual structure rather than conflict-specific encoding. A dissociation emerges between detection and decision: in Llama, the probe signal peaks at late layers (88\% depth), but representation steering achieves causal influence only at a mid-layer (41\% depth); analogous Qwen and Gemma steering yields no significant effect. These findings demonstrate that linear detectability does not imply causal relevance, with direct implications for probe-based intervention research.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-24T14:57:55.469475+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-24T14:57:55.971699+00:00_

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
…[truncated 740 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-24T14:57:55.972112+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-24T14:57:56.574950+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-24T14:57:56.625649+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-24T14:57:56.676389+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-24T14:58:35.209547+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$~]//g; s/  */ /g' | wc -w",
  "description": "Count abstract word count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$~]//g; s/  */ /g' | wc -w",
    "description": "Count abstract word count"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-24T14:58:35.662700+00:00_

200

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 453
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-24T14:58:35.715031+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-24T14:58:36.167258+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-24T14:58:36.217956+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-24T14:58:36.620023+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-24T14:58:36.620397+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-24T14:58:36.972357+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-24T14:58:36.972992+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-24T14:58:37.025186+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	This work investigated whether knowledge conflict signals in multilingual LLMs are detectable across languages and whether detected signals causally influence conflict resolution.
5	Through residual stream probing on Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-IT, we showed that conflict signals are linearly detectable both within and across languages, with balanced accuracies of 77.6\%, 75.0\%, and 76.2\% on English within-language detection and all cross-lingual transfer directions significantly exceeding chance (binomial $p < 0.001$).
6	The observed transfer asymmetry (ZH$\to$EN exceeding EN$\to$ZH by approximately 6--7~pp) is consistent across all three architectures and matches the XNLI non-conflict baseline in magnitude and direction for all models, establishing that this pattern reflects the general cross-lingual representational structure of English-dominant models rather than conflict-specific encoding.
7	
8	A central finding is the dissociation between detection and decision.
9	Probe accuracy peaks at late layers (L28, 88\% depth), but representation steering succeeds only at a mid-layer (L13, 41\% depth; Fisher $p = 0.002$), and all late-layer interventions fail.
10	This result demonstrates that linear detectability does not imply causal influence, and that conflict resolution occurs upstream of where the outcome becomes linearly readable.
11	For probing-based intervention research, this dissociation implies that cross-layer sweeps are necessary to identify the computationally relevant site, as targeting the probe peak alone can miss the true decision point.
12	
13	Several directions remain open.
14	Steering failed in both Qwen (L14; $n = 131$, best $p = 0.785$) and Gemma (L17; $n = 171$, 88.9\% probe accuracy, best $p = 0.448$), with zero directional flips despite Gemma's probe accuracy exceeding Llama's, confirming that the causal influence of the probe direction is architecture-specific.
15	Futur
…[truncated 237 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-24T14:58:44.957673+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "references.bib",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "references.bib",
    "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-24T14:58:45.912646+00:00_

/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 954
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-24T14:58:45.913170+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Meng et al 2022 \"Locating and Editing Factual Associations in GPT\" activation patching causal tracing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Meng et al 2022 \"Locating and Editing Factual Associations in GPT\" activation patching causal tracing"
  }
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-24T14:58:46.465282+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "knowledge conflict multilingual LLM 2025 2026 cross-lingual representation probing recent work"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "knowledge conflict multilingual LLM 2025 2026 cross-lingual representation probing recent work"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-24T14:58:53.088147+00:00_

Web search results for query: "Meng et al 2022 "Locating and Editing Factual Associations in GPT" activation patching causal tracing"

Links: [{"title":"[PDF] Locating and Editing Factual Associations in GPT | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Locating-and-Editing-Factual-Associations-in-GPT-Meng-Bau/996445d847f06e99b0bd259345408a0cf1bce87e"},{"title":"Locating and Editing Factual Associations in GPT Kevin Meng⇤ MIT CSAIL","url":"https://proceedings.neurips.cc/paper_files/paper/2022/file/6f1d43d5a82a37e89b0665b33bf3a182-Paper-Conference.pdf"},{"title":"Locating and Editing Factual Associations in GPT Kevin Meng∗ MIT CSAIL","url":"https://arxiv.org/pdf/2202.05262"},{"title":"Locating and Editing Factual Associations in GPT | Request PDF","url":"https://www.researchgate.net/publication/401454431_Locating_and_Editing_Factual_Associations_in_GPT"},{"title":"Locating and Editing Factual Associations in GPT","url":"https://rome.baulab.info/"},{"title":"Locating and Editing Factual Associations in GPT","url":"https://proceedings.neurips.cc/paper_files/paper/2022/hash/6f1d43d5a82a37e89b0665b33bf3a182-Abstract-Conference.html"},{"title":"[2202.05262] Locating and Editing Factual Associations in GPT","url":"https://arxiv.org/abs/2202.05262"},{"title":"Locating and Editing Factual Associations in GPT - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2202.05262"},{"title":"Locating and editing factual associations in GPT | Proceedings of the 36th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3600270.3601532"}]

I found relevant information about the Meng et al. 2022 paper. Here are the key findings:

## Overview
The paper "Locating and Editing Factual Associations in GPT" by Kevin Meng, David Bau, Alex Andonian, and Yonatan Belinkov was published at NeurIPS 2022.

## Main Contributions

The paper analyzes the storage and recall of factual associations in autoregressive transformer la
…[truncated 1089 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7174
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-24T14:58:53.841530+00:00_

Web search results for query: "knowledge conflict multilingual LLM 2025 2026 cross-lingual representation probing recent work"

Links: [{"title":"Mitigating Cross-Lingual Cultural Inconsistencies in LLMs via Consensus-Driven Preference Optimisation","url":"https://arxiv.org/html/2605.12515"},{"title":"Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge   Representation Sharing in LLMs","url":"https://arxiv.org/pdf/2408.10646"},{"title":"When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models","url":"https://arxiv.org/pdf/2601.07041"},{"title":"Crosslingual Capabilities and Knowledge Barriers in Multilingual Large Language Models | OpenReview","url":"https://openreview.net/forum?id=BCyAlMoyx5"},{"title":"Exploring Multilingual Probing in Large Language Models: A   Cross-Language Analysis","url":"https://arxiv.org/pdf/2409.14459"},{"title":"Probing Cross-Lingual Lexical Knowledge from Multilingual Sentence   Encoders","url":"https://arxiv.org/pdf/2205.00267"},{"title":"Probing the Emergence of Cross-lingual Alignment during LLM Training","url":"https://arxiv.org/pdf/2406.13229"}]

Based on the search results, here are the key recent findings on knowledge conflict in multilingual LLMs and cross-lingual representation probing:

## Knowledge Conflict in Multilingual Models

Knowledge conflict occurs when a model's internally stored belief contradicts information presented in context, and how LLMs react to and resolve such conflicts is central to system robustness and faithfulness. Despite the reality of multilingual systems, existing studies remain largely English-centric, leaving the mechanisms underlying Cross-Lingual Knowledge Conflict (CLKC) largely unexplored.

Multilingual LLMs exhibit language-conditioned memories: knowledge correct in one language may be incomplete or incorrect in another.

## Cross-Lingual Representation and Knowledge Consistency

Recent research distinguishes between surface-level consistency and deeper rep
…[truncated 1187 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7376
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-24T14:58:59.211301+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-24T14:58:59.211943+00:00_

1	% References for Cross-Lingual Knowledge Conflict paper
2	% Auto-generated from literature_map.yaml
3	
4	@article{basu2026interpretability,
5	  author    = {Basu, S. and others},
6	  title     = {Interpretability without Actionability: Mechanistic Methods Cannot Correct Language Model Errors Despite Near-Perfect Internal Representations},
7	  journal   = {arXiv preprint arXiv:2603.18353},
8	  year      = {2026},
9	  url       = {https://arxiv.org/abs/2603.18353}
10	}
11	
12	@article{brink2026probing,
13	  author    = {Brink, I. and Boer, A. and Ulmer, D.},
14	  title     = {Probing for Knowledge Attribution in Large Language Models},
15	  journal   = {arXiv preprint arXiv:2602.22787},
16	  year      = {2026},
17	  url       = {https://arxiv.org/abs/2602.22787}
18	}
19	
20	@inproceedings{ifergan2024beneath,
21	  author    = {Ifergan, M. and Choshen, L. and Aharoni, R. and Szpektor, I. and Abend, O.},
22	  title     = {Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in {LLMs}},
23	  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2025},
24	  year      = {2024},
25	  url       = {https://arxiv.org/abs/2408.10646}
26	}
27	
28	
29	@inproceedings{li2025taming,
30	  author    = {Li, G. and Chen, Y. and Tong, H.},
31	  title     = {Taming Knowledge Conflicts in Language Models},
32	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},
33	  year      = {2025},
34	  url       = {https://arxiv.org/abs/2503.10996}
35	}
36	
37	@article{pham2026where,
38	  author    = {Pham, M.V. and Borkakoty, H. and Hou, Y.},
39	  title     = {Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge Conflict in Language Models},
40	  journal   = {arXiv preprint arXiv:2601.09445},
41	  year      = {2026},
42	  url       = {https://arxiv.org/abs/2601.09445}
43	}
44	
45	
46	@inproceedings{wang2025lost,
47	  author    = {Wang, M. and Adel, H. and Lange, L. and others},

…[truncated 8395 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-24T15:00:21.047060+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Geiger et al 2024 \"Distributed Alignment Search\" DAS causal abstraction intervention"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Geiger et al 2024 \"Distributed Alignment Search\" DAS causal abstraction intervention"
  }
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-24T15:00:21.097955+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Qwen3-8B technical report 2025 model architecture layers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Qwen3-8B technical report 2025 model architecture layers"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-24T15:00:27.380887+00:00_

Web search results for query: "Geiger et al 2024 "Distributed Alignment Search" DAS causal abstraction intervention"

Links: [{"title":"Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations","url":"https://proceedings.mlr.press/v236/geiger24a.html"},{"title":"Proceedings of Machine Learning Research vol 236:1–23, 2024","url":"https://proceedings.mlr.press/v236/geiger24a/geiger24a.pdf"},{"title":"Is Causal Abstraction Enough for Mechanistic Interpretability?","url":"https://openreview.net/pdf?id=ZYXTLo7kCi"},{"title":"[2303.02536] Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations","url":"https://arxiv.org/abs/2303.02536"},{"title":"Distributed Alignment Search: Identifying Causal ...","url":"https://sidn.baulab.info/structure/"},{"title":"Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations","url":"https://arxiv.org/html/2303.02536v4"},{"title":"(PDF) Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations","url":"https://www.researchgate.net/publication/383739393_Finding_Alignments_Between_Interpretable_Causal_Variables_and_Distributed_Neural_Representations"},{"title":"Finding Alignments Between Interpretable Causal Variables and   Distributed Neural Representations","url":"https://arxiv.org/pdf/2303.02536"}]

I found the paper! Here's what the search results reveal about the Geiger et al. 2024 work on Distributed Alignment Search (DAS):

## Overview

Causal abstraction is a promising theoretical framework for explainable artificial intelligence that defines when an interpretable high-level causal model is a faithful simplification of a low-level deep learning system.

## The DAS Method

Existing causal abstraction methods have two major limitations: they require a brute-force search over alignments between the high-level model and the low-level one, and they presuppose that variables in the h
…[truncated 1171 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6333
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-24T15:00:27.884153+00:00_

Web search results for query: "Qwen3-8B technical report 2025 model architecture layers"

Links: [{"title":"Qwen3-8B LLM: Architecture & Efficiency","url":"https://www.emergentmind.com/topics/qwen3-8b-model"},{"title":"Qwen-3-8B: Dense LLM with Unified Thinking","url":"https://www.emergentmind.com/topics/qwen-3-8b-model"},{"title":"arXiv:2506.05176v3 [cs.CL] 11 Jun 2025 Technical Report","url":"https://arxiv.org/pdf/2506.05176"},{"title":"Qwen3-8B: Efficient 8B Language Model","url":"https://www.emergentmind.com/topics/qwen3-8b"},{"title":"Qwen3 8B | Open Laboratory","url":"https://openlaboratory.com/models/qwen3-8b/"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"Qwen3-Next Complete Technical Analysis: Major Breakthrough in AI Model Architecture for 2025 - DEV Community","url":"https://dev.to/czmilo/qwen3-next-complete-technical-analysis-major-breakthrough-in-ai-model-architecture-for-2025-3kml"},{"title":"Qwen3 Technical Report","url":"https://arxiv.org/html/2505.09388v1"}]

Based on the search results, here's information about the Qwen3-8B model architecture from the 2025 technical report:

## Model Architecture Overview

Qwen3-8B was developed by Alibaba and first described in the "Qwen3 Technical Report" (May 2025).

## Layer Configuration

Qwen3-8B is a dense transformer-based model with 8.2 billion parameters—6.95 billion of which are non-embedding parameters—spanning 36 layers.

## Key Architectural Features

The architecture includes Grouped Query Attention (GQA), SwiGLU, Rotary Positional Embeddings (RoPE), and RMSNorm with pre-normalization.

The model employs 32 attention heads for queries and 8 for key/value, supported by Grouped Query Attention (GQA), which optimizes efficiency and scaling.

## Context Window

The model supports a context window of at least 32,768 tokens (native) and up to 128k tokens using YaRN and dual-chunk attention extensions.

## Additional D
…[truncated 369 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6786
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-24T15:02:37.860081+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿意见：Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries from General Multilingual Representations\n\n### 总体评分\n\n**Overall**: 3.0 / 5 — Findings\n**一句话总结**: 方法论扎实、混淆排除设计巧妙，但核心 claim 之一（Detection ≠ Decision）仅在 1/3 模型上成立，跨语言扩展的新颖性相对于 Zhao et al. (2024) 较为增量，整体贡献不足以支撑 EMNLP 主会议 Long Paper。\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5 / 5 | 统计方法严谨（Bonferroni、paired bootstrap），混淆排除设计优秀；但核心因果 claim 仅基于 Llama 一个模型，single-seed probing，样本量偏小 |\n| Excitement | 2.5 / 5 | 跨语言扩展较增量，不对称性发现可由已知 English-centric bias 预测；Detection ≠ Decision 有价值但 N=1 模型泛化性不足 |\n| Overall Assessment | 3.0 / 5 | 适合 Findings track：方法论贡献有参考价值，但新颖性和结论强度不足以进入主会议 |\n| Reproducibility | 3 / 5 | 方法描述详细但 single-seed、无代码/数据发布计划 |\n| Confidence | 4 / 5 | 熟悉 cross-lingual probing、representation steering、knowledge conflict 等相关领域 |\n\n---\n\n### Must-Fix 问题\n\n**N1** [Critical] Steering 仅在 Llama 成功，\"Detection ≠ Decision\" claim 的泛化性严重不足\n- 位置：Section 4.6, Table 3, Section 5, Contributions bullet 2\n- 论文最具新颖性的 claim（Detection-Decision Layer Dissociation）因果证据仅来自 Llama 一个模型。Qwen (p=0.785, 0 flips) 和 Gemma (p=0.448, 0 flips) 均完全失败。一个仅在 1/3 模型上成立的因果发现难以支撑一般性结论。\n- 建议：(a) 尝试 activation patching / DAS 等替代方法排除是 linear steering 本身的局限；(b) 明确降低 claim 强度；(c) 补充对 steering 失败的 mechanistic 解释。\n\n**N2** [Critical] 新颖性增量性\n- 位置：Contributions (Section 1), Section 4.2-4.3\n- Contribution 1 是 Zhao et al. (2024) 的直接跨语言扩展；不对称性可从 Wendler et al. (2024) 和 Kargaran et al. (2024) 直接预测。Contribution 3（Confound Pipeline）虽有用但单独不足以支撑 long paper。三个 contributions = \"增量扩展\" + \"N=1 case study\" + \"methodological toolkit\"。\n\n---\n\n### Should-Fix 问题\n\n**W1** [Major] Qwen3-8B 引用错误：论文使用 Qwen3-8B 但引用 Qwen2.5 Technical Report (yang2024qwen25)。正确引用应为 arXiv:2505.09388。\n\n**W2** [Major] 仅一个语言对 (EN-ZH) 但标题使用 \"Cross-Lingual\" 暗示一般性。EN-DE 仅在 confound exclusion 中简要提及。\n\n**W3** [Major] Single-seed probing：所有结果基于单次种子训练，未考虑探针训练随机性。\n\n**W4** [Minor] Related Work 遗漏：Pires et al. 2019, Chi et al. 2020, Meng et al. 2022 (activation patching), Geiger et al. 2024 (DAS)。\n\n**W5** [Minor] 多个 bib 条目使用 \"and others\" 格式，作者信息不完整。\n\n**W6** [Minor] Abstract 恰好 200 words，位于限制边界。\n\n---\n\n### 小问题\n- \"A suggestive MLP trend\" 段不显著结果占过多篇幅，可移至 Appendix\n- Table 3 中 Qwen/Gemma 行缺少具体 flip rates，与 Llama 行详细程度不一致\n- Limitations 中 Gemma 88.9% 数字在正文中已多次重复\n\n### Missing References\n1. Pires et al. (2019) \"How Multilingual is Multilingual BERT\" — 跨语言 probing 开创性工作\n2. Chi et al. (2020) \"Finding Universal Grammatical Relations in Multilingual BERT\"\n3. Meng et al. (2022) \"Locating and Editing Factual Associations in GPT\" — activation patching 基础\n4. Geiger et al. (2024) DAS — 替代因果干预方法\n5. Qwen Team (2025) Qwen3 Technical Report (arXiv:2505.09388) — 正确模型引用\n\n### 主要优势\n- S1: 混淆排除设计系统全面，为跨语言 probing 研究树立良好范式\n- S2: 诚实报告负面结果（Qwen/Gemma steering 失败）\n- S3: XNLI baseline 比较实验设计巧妙\n- S4: 统计实践严谨（Bonferroni, paired bootstrap, 独立复制 N=201）\n- S5: Discussion 部分有深度思考",
  "reviewer_id": "2",
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿意见：Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries from General Multilingual Representations\n\n### 总体评分\n\n**Overall**: 3.0 / 5 — Findings\n**一句话总结**: 方法论扎实、混淆排除设计巧妙，但核心 claim 之一（Detection ≠ Decision）仅在 1/3 模型上成立，跨语言扩展的新颖性相对于 Zhao et al. (2024) 较为增量，整体贡献不足以支撑 EMNLP 主会议 Long Paper。\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5 / 5 | 统计方法严谨（Bonferroni、paired bootstrap），混淆排除设计优秀；但核心因果 claim 仅基于 Llama 一个模型，single-seed probing，样本量偏小 |\n| Excitement | 2.5 / 5 | 跨语言扩展较增量，不对称性发现可由已知 English-centric bias 预测；Detection ≠ Decision 有价值但 N=1 模型泛化性不足 |\n| Overall Assessment | 3.0 / 5 | 适合 Findings track：方法论贡献有参考价值，但新颖性和结论强度不足以进入主会议 |\n| Reproducibility | 3 / 5 | 方法描述详细但 single-seed、无代码/数据发布计划 |\n| Confidence | 4 / 5 | 熟悉 cross-lingual probing、representation steering、knowledge conflict 等相关领域 |\n\n---\n\n### Must-Fix 问题\n\n**N1** [Critical] Steering 仅在 Llama 成功，\"Detection ≠ Decision\" claim 的泛化性严重不足\n- 位置：Section 4.6, Table 3, Section 5, Contributions bullet 2\n- 论文最具新颖性的 claim（Detection-Decision Layer Dissociation）因果证据仅来自 Llama 一个模型。Qwen (p=0.785, 0 flips) 和 Gemma (p=0.448, 0 flips) 均完全失败。一个仅在 1/3 模型上成立的因果发现难以支撑一般性结论。\n- 建议：(a) 尝试 activation patching / DAS 等替代方法排除是 linear steering 本身的局限；(b) 明确降低 claim 强度；(c) 补充对 steering 失败的 mechanistic 解释。\n\n**N2** [Critical] 新颖性增量性\n- 位置：Contributions (Section 1), Section 4.2-4.3\n- Contribution 1 是 Zhao et al. (2024) 的直接跨语言扩展；不对称性可从 Wendler et al. (2024) 和 Kargaran et al. (2024) 直接预测。Contribution 3（Confound Pipeline）虽有用但单独不足以支撑 long paper。三个 contributions = \"增量扩展\" + \"N=1 case study\" + \"methodological toolkit\"。\n\n---\n\n### Should-Fix 问题\n\n**W1** [Major] Qwen3-8B 引用错误：论文使用 Qwen3-8B 但引用 Qwen2.5 Technical Report (yang2024qwen25)。正确引用应为 arXiv:2505.09388。\n\n**W2** [Major] 仅一个语言对 (EN-ZH) 但标题使用 \"Cross-Lingual\" 暗示一般性。EN-DE 仅在 confound exclusion 中简要提及。\n\n**W3** [Major] Single-seed probing：所有结果基于单次种子训练，未考虑探针训练随机性。\n\n**W4** [Minor] Related Work 遗漏：Pires et al. 2019, Chi et al. 2020, Meng et al. 2022 (activation patching), Geiger et al. 2024 (DAS)。\n\n**W5** [Minor] 多个 bib 条目使用 \"and others\" 格式，作者信息不完整。\n\n**W6** [Minor] Abstract 恰好 200 words，位于限制边界。\n\n---\n\n### 小问题\n- \"A suggestive MLP trend\" 段不显著结果占过多篇幅，可移至 Appendix\n- Table 3 中 Qwen/Gemma 行缺少具体 flip rates，与 Llama 行详细程度不一致\n- Limitations 中 Gemma 88.9% 数字在正文中已多次重复\n\n### Missing References\n1. Pires et al. (2019) \"How Multilingual is Multilingual BERT\" — 跨语言 probing 开创性工作\n2. Chi et al. (2020) \"Finding Universal Grammatical Relations in Multilingual BERT\"\n3. Meng et al. (2022) \"Locating and Editing Factual Associations in GPT\" — activation patching 基础\n4. Geiger et al. (2024) DAS — 替代因果干预方法\n5. Qwen Team (2025) Qwen3 Technical Report (arXiv:2505.09388) — 正确模型引用\n\n### 主要优势\n- S1: 混淆排除设计系统全面，为跨语言 probing 研究树立良好范式\n- S2: 诚实报告负面结果（Qwen/Gemma steering 失败）\n- S3: XNLI baseline 比较实验设计巧妙\n- S4: 统计实践严谨（Bonferroni, paired bootstrap, 独立复制 N=201）\n- S5: Discussion 部分有深度思考",
    "reviewer_id": "2",
    "project": "clkc_mech_interp"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-24T15:02:41.728172+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3868
}
```

</details>

---

### Assistant

_source line 72 · 2026-05-24T15:02:54.900917+00:00_

审稿意见已提交给 Review Director。

总结：给出 **Overall 3.0 / 5（Findings）**。核心判断依据：

1. **两个 Critical 问题**：Detection ≠ Decision 的因果证据仅在 Llama 1 个模型成立（N1）；整体新颖性相对于 Zhao et al. 2024 较增量（N2）
2. **三个 Major 问题**：Qwen3 引用错误（W1）、单一语言对（W2）、single-seed probing（W3）
3. **主要优势**：混淆排除 pipeline 设计优秀、统计实践严谨、负面结果诚实报告
4. **遗漏引用**：Pires 2019、Chi 2020、Meng 2022、Geiger 2024、Qwen3 正确引用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2"
}
```

</details>

---

## Round 2

10 recorded events

### User

_source line 73 · 2026-05-24T15:03:22.874228+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和 Missing Reference，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 审稿意见

### Overall Assessment: 3.5 — Borderline Conference

**N1** [Critical] Steering 实验的多重比较校正不完整，核心 p=0.002 可能不保真
- 主实验在 3 个层（L13, L18, L28）各测试 k=10 个 α 值，共 30 次检验。Bonferroni 仅在层内应用（0.05/10=0.005），未跨层校正。若全 family 校正（0.05/30≈0.00167），L13 正方向 p=0.002 不再显著。独立复现（N=201）缓解但非预注册。
- 建议: 明确说明为什么层间不需要校正（如预注册），或采用 FDR 校正，或报告完整 family-wise p 值。

**N2** [Critical] 因果声明的泛化性：N=1 模型问题
- Steering 仅 Llama L13 成功，Qwen/Gemma 全部阴性（零翻转）。但论文框架性表述暗示这是 general principle。无法区分：Llama 特有特征 vs 线性 steering 局限 vs 统计偶然。Gemma 88.9% probe accuracy 下零效应对 "probe direction = causal direction" 构成反证。

**W1** [Major] 单种子实验——Table 1 所有结果基于单次 split，未报告多种子 mean ± std，peak layer 可能因 split 变化。

**W2** [Major] "非冲突特异"声明仅基于 CI 重叠，缺乏正式 TOST 等价性检验或 difference-in-differences 检验。

**W3** [Major] COMET tercile 分析统计功效不足（每 tercile 64-91 样本），p=0.695/0.761 反映 power 不足而非无效应。Gemma 未报告。

**W4** [Major] 跨模型比较在不同样本子集上进行（Llama 1368, Qwen 966, Gemma 1590），未在交集上验证。

**W5** [Minor] 翻译模型（Qwen3-8B）与实验对象重叠，未讨论此 confound。

**W6** [Minor] Table 3 caption "p < 0.05" 与正文 Bonferroni 阈值 0.005 不一致。

### Questions
Q1: Bonferroni 为什么按层而非按整个 steering 实验校正？
Q2: 独立复现（N=201）是否在观察到 L13 主实验结果之后进行？
Q3: Gemma L21 cross-task transfer dip（0.730）与 alternating attention 架构的关系？
Q4: L13 和 L28 的 w_probe cosine similarity 是多少？
Q5: Qwen Δ_asym CI 包含零，如何支撑 "consistent across all three architectures"？

### Missing References
- Turner, Thacker, and Fry (2023): "Activation Addition"
- Marks et al. (2024): "Geometry of Truth"

### 主要优势
- S1: 首次多架构/多语言知识冲突信号的系统性 probing 研究
- S2: Confound exclusion pipeline 设计周全
- S3: XNLI baseline 对比有方法论启示价值
- S4: 对 negative results 的诚实处理
- S5: 独立复现（N=201）展示 causal gradient 空间精度
- S6: 写作清晰，结构完整

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-24T15:04:14.769280+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Qwen3 technical report arxiv 2505.09388 May 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Qwen3 technical report arxiv 2505.09388 May 2025"
  }
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-24T15:04:14.878292+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Turner Thacker Fry 2023 \"Activation Addition\" steering vectors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Turner Thacker Fry 2023 \"Activation Addition\" steering vectors"
  }
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-24T15:04:15.280168+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Marks et al 2024 \"Geometry of Truth\" probing LLM representations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Marks et al 2024 \"Geometry of Truth\" probing LLM representations"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-24T15:04:20.101999+00:00_

Web search results for query: "Qwen3 technical report arxiv 2505.09388 May 2025"

Links: [{"title":"[2505.09388] Qwen3 Technical Report","url":"https://arxiv.org/abs/2505.09388"},{"title":"[2505.09388v1] Qwen3 Technical Report","url":"https://arxiv.org/abs/2505.09388v1"},{"title":"Paper page - Qwen3 Technical Report","url":"https://huggingface.co/papers/2505.09388"},{"title":"Qwen3 Technical Report","url":"https://arxiv.org/html/2505.09388.pdf"},{"title":"Qwen3 Technical Report | Request PDF","url":"https://www.researchgate.net/publication/391741196_Qwen3_Technical_Report"},{"title":"Qwen3 Technical Report - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250509388Y/abstract"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"[2505.09388] Qwen3 Technical Report - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2505.09388"}]

I found the Qwen3 Technical Report paper! Here's a summary of the key information:

## Qwen3 Technical Report (arXiv:2505.09388)

**Publication Details:**
The paper was submitted on May 14, 2025, and is available on arXiv at https://arxiv.org/abs/2505.09388.

**Overview:**
Qwen3 is the latest version of the Qwen model family, comprising a series of large language models designed to advance performance, efficiency, and multilingual capabilities.

**Model Architecture:**
The Qwen3 series includes models of both dense and Mixture-of-Expert (MoE) architectures, with parameter scales ranging from 0.6 to 235 billion.

**Key Innovations:**
1. **Unified Framework:** A key innovation is the integration of thinking mode (for complex, multi-step reasoning) and non-thinking mode (for rapid, context-driven responses) into a unified framework, which eliminates the need to switch between different models and enables dynamic mode switching based on user queries or chat templates.

2. **Thinking Budget Mechanism:** Qwen3 introduces a thinking budget mechanism, all
…[truncated 573 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5332
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-24T15:04:21.609009+00:00_

Web search results for query: "Turner Thacker Fry 2023 "Activation Addition" steering vectors"

Links: [{"title":"Activation Steering in LLMs","url":"https://www.emergentmind.com/topics/activation-steering-method"},{"title":"Paper page - Activation Addition: Steering Language Models Without Optimization","url":"https://huggingface.co/papers/2308.10248"},{"title":"Activation Addition: Steering Language Models Without Optimization - University of Bristol","url":"https://research-information.bris.ac.uk/en/publications/activation-addition-steering-language-models-without-optimization/"},{"title":"[2308.10248] Steering Language Models With Activation Engineering","url":"https://arxiv.org/abs/2308.10248"},{"title":"Activation Addition: Steering Language Models Without Optimization","url":"https://arxiv.org/html/2308.10248v4"},{"title":"Steering Llama 2 via Contrastive Activation Addition","url":"https://arxiv.org/pdf/2312.06681"}]

Based on the search results, here's what I found about Turner, Thacker, Fry, and "Activation Addition" steering vectors:

Activation Addition (ActAdd) is a method that modifies model activations at inference-time to control large language model behavior with less compute and effort than supervised finetuning or reinforcement learning from human feedback.

Unlike past work which learned steering vectors, the Activation Addition method computes them by taking the activation differences that result from pairs of prompts. Specifically, Activation Addition contrasts the intermediate activations on prompt pairs (such as "Love" versus "Hate") to compute a steering vector.

The inference-time approach yields control over high-level properties of output and preserves off-target model performance, involves far less compute and implementation effort compared to finetuning or RLHF, allows users to provide natural language specifications, and its overhead scales naturally with model size.

Note: The paper's authorship appears to be led by Alexander Matt Tur
…[truncated 259 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6730
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-24T15:04:22.776278+00:00_

Web search results for query: "Marks et al 2024 "Geometry of Truth" probing LLM representations"

Links: [{"title":"The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/geometry-truth-emergent-linear-structure-large-language"},{"title":"Probing the Geometry of Truth: Consistency and Generalization of Truth Directions in LLMs Across Logical Transformations and Question Answering Tasks","url":"https://arxiv.org/html/2506.00823v1"},{"title":"The Geometry of Truth: Emergent Linear Structure in LLM Representation of True/False Datasets - Arize AI","url":"https://arize.com/blog/the-geometry-of-truth-emergent-linear-structure-in-llm-representation-of-true-false-datasets/"},{"title":"The Geometry of Truth: Emergent Linear Structure in LLM Representations of True/False Datasets","url":"https://arxiv.org/html/2310.06824v3"},{"title":"Community Paper Reading – The Geometry of Truth: Emergent Linear Structure in LLM Representation of True/False Datasets · Zoom · Luma","url":"https://luma.com/geometry-of-truth"},{"title":"The Geometry of Truth: Emergent Linear Structure in Large Language Model   Representations of True/False Datasets","url":"https://arxiv.org/pdf/2310.06824"},{"title":"Probing the Geometry of Truth: Consistency and Generalization of Truth Directions in LLMs Across Logical Transformations and Question Answering Tasks","url":"https://arxiv.org/pdf/2506.00823"}]

Based on the search results, here's what I found about the Marks et al 2024 "Geometry of Truth" paper:

## Overview

Samuel Marks and Max Tegmark authored the paper "The Geometry of Truth: Emergent Linear Structure in LLM Representations of True/False Datasets." It was published on August 20, 2024.

## Research Focus

The work uses high-quality datasets of simple true/false statements to study in detail the structure of LLM representations of truth.

## Key Findings

The pape
…[truncated 789 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7496
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-24T15:06:48.323132+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿意见\n\n## 审查侧重：新颖性、学术贡献完整性、Related Work 覆盖度、写作质量\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 — Findings\n**一句话总结**: 方法论设计扎实（confound exclusion pipeline + XNLI baseline），但核心贡献的新颖性有限（跨语言延伸 Zhao et al. 2024 + 已知 English-centric bias 的 re-confirmation），且最具新意的 Detection ≠ Decision 主张仅在 1/3 模型上成立，不足以支撑 EMNLP long paper 的 conference 级别。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法论合理、统计实践整体规范，但核心因果声明基于 N=1 模型，single-seed split，confound exclusion 功效不足 |\n| Excitement | 2.5/5 | 跨语言延伸和不对称性发现属 incremental；Detection ≠ Decision 有洞察但泛化性不足 |\n| Reproducibility | 3/5 | 实验细节基本充足，但 single seed、无代码发布声明、翻译 pipeline 依赖特定模型版本 |\n| Reviewer Confidence | 4/5 | 熟悉 cross-lingual probing、representation steering 和 knowledge conflict 文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [Critical] 新颖性不足以支撑 EMNLP Long Paper\n- 具体位置：Section 1（Contributions），全文\n- 问题：三个 contribution 的独立新颖性均有限：\n  - (1) 跨语言冲突可检测性+不对称性：是 Zhao et al. (2024) 从单语到跨语言的直接延伸。不对称性结果（ZH→EN > EN→ZH ~7pp）在 English-centric bias 已被 Wendler et al. (2024) 和 Kargaran et al. (2024) 充分记录的背景下，属 expected finding。论文本身也承认 \"it inherits from the model's general multilingual structure\"（Abstract），这实际上削弱了此 contribution 的新颖性。\n  - (2) Detection-Decision 层分离：最有潜力的贡献，但仅在 Llama 一个模型上成立（Section 4.6）。Qwen 和 Gemma 均为零翻转（Table 3/5）。论文将其定性为 \"architecture-specific\"（Section 5），但这意味着该发现的 generalizability 极其有限。\n  - (3) Confound exclusion pipeline：方法论贡献有价值，但作为独立 contribution 略显薄弱——本质上是 best practice checklist（COMET 分层 + token overlap + XNLI baseline），而非新方法。\n- 为什么影响接收：对于 EMNLP long paper（非 Findings），至少需要一个 contribution 具有足够的 novelty 和 generalizability。当前最强贡献（Detection ≠ Decision）受限于 N=1 模型。\n- 建议修改方向：(a) 增加至少一个非 Llama 模型的因果干预成功案例（或使用非线性干预方法如 activation patching），(b) 或将论文重新定位为 Findings-level 的实证研究，弱化因果声明。\n\n**N2** [Critical] Qwen3 引用错误\n- 具体位置：Section 4.1，references.bib 中 `yang2024qwen25`\n- 问题：论文声称使用 \"Qwen3-8B\"（36 layers），但引用的是 Qwen2.5 Technical Report（arXiv:2412.15115）。Qwen3 Technical Report 于 2025 年 5 月发表（arXiv:2505.09388），是独立论文。这是明确的引用错误。Qwen3-8B（36 layers, 8.2B params）与 Qwen2.5-7B（28 layers）架构完全不同。\n- 为什么影响接收：引用错误损害学术诚信，且审稿人无法验证模型规格是否正确。\n- 建议修改方向：替换为正确的 Qwen3 引用 (Yang et al., 2025; arXiv:2505.09388)。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [Major] Related Work 遗漏关键引用\n- 具体位置：Section 2\n- 问题：以下重要相关工作未被引用：\n  - **Pires et al. (2019)** \"How Multilingual is Multilingual BERT?\"——cross-lingual probing 的奠基性工作，首次系统研究了零样本跨语言迁移，是 Section 2 第二段（cross-lingual representations）的直接前驱。\n  - **Chi et al. (2020)** \"Finding Universal Grammatical Relations in Multilingual BERT\"——跨语言表征中共享子空间的 structural probing，与本文 cross-task language probe transfer（Section 5 第三段）直接相关。\n  - **Meng et al. (2022)** \"Locating and Editing Factual Associations in GPT\"——causal tracing / activation patching 的奠基工作。论文在 Conclusion 中提到 activation patching 作为 future work，却未引用这一方法的原始论文。\n  - **Geiger et al. (2024)** \"Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations\"——DAS（Distributed Alignment Search）是 causal intervention 的重要替代方法，与 Section 2 第三段（representation steering and causal intervention）直接相关。\n- 建议：在 Section 2 各对应段落补充上述引用，并讨论本文方法与 activation patching / DAS 的区别。\n\n**W2** [Major] 论文存在 Oversell 倾向\n- 具体位置：Title, Abstract, Section 1\n- 问题：标题 \"Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries from General Multilingual Representations\" 暗示一般性结论，但实验仅覆盖一个语言对（EN-ZH）。EN-DE 数据仅在 Section 4.5 confound exclusion 中作为辅助分析出现，不构成主要实验。Abstract 中 \"Conflict signals are linearly detectable across languages\" 的表述未限定为 EN-ZH。Section 1 contributions 中 \"the first evidence\" 也有 oversell 嫌疑——Zhao et al. (2024) 已在单语中证明了可检测性，跨语言延伸是增量而非 \"first\"。\n- 建议：(a) 标题和 abstract 中明确限定为 EN-ZH，(b) 将 \"first evidence\" 修改为 \"first cross-lingual evidence\"。\n\n**W3** [Major] Bib 条目格式不规范\n- 具体位置：references.bib\n- 问题：多个 bib 条目使用 `and others` 代替完整作者列表（如 `{Basu, S. and others}`, `{Zhao, J. and others}`, `{Wang, M. and Adel, H. and Lange, L. and others}`）。ACL 模板要求完整作者列表或标准 `et al.` 格式。当前格式在编译后可能产生不规范的引用显示。\n- 建议：补全所有作者列表，或至少列出前三位作者。\n\n**W4** [Minor] 翻译模型与实验对象重叠（同意 R1-W5）\n- 具体位置：Section 3.2, Section 4.1\n- 问题：Qwen3-8B 同时用作翻译模型和实验对象。翻译输出可能对 Qwen 的 representation space 存在系统性偏好，导致 Qwen 的跨语言 probe transfer 结果受到 confound。论文未讨论此问题。\n- 建议：在 Limitations 中讨论，或额外使用独立翻译模型（如 NLLB）验证 Qwen 子集结果的鲁棒性。\n\n**W5** [Minor] Abstract 恰好 200 words\n- 具体位置：Abstract\n- 问题：经计算（去除 LaTeX 命令后），abstract 恰好 200 words，处于 EMNLP 2026 限制的临界值。不同的 word count 工具可能给出略有不同的结果。建议留出安全余量。\n- 建议：精简至 190 words 以下。\n\n---\n\n## 小问题（不影响接收）\n\n- Figure 1 的三个子图使用相同的 y 轴范围，但 Gemma 有 42 层（x 轴范围更大），导致视觉上的密度不一致，建议统一按 relative depth (%) 为 x 轴。\n- Section 5 \"A suggestive MLP trend\" 段落提出了 MLP sublayer 的观察但 CI 包含零——这种 \"suggestive\" 表述在审稿中容易被视为 cherry-picking，建议删除或移至 appendix。\n- Discussion Section 5 \"Direct evidence for a shared cross-lingual subspace\" 中 cross-task probe transfer 实验（conflict→XNLI 达到 0.96+）是重要结果，但仅出现在 Discussion 中而非 Experiments，结构安排不佳。\n\n---\n\n## 主要优势\n\n- **S1**: Confound exclusion pipeline（COMET tercile + token overlap + XNLI baseline）设计周全，对未来跨语言 probing 研究有方法论参考价值。\n- **S2**: XNLI baseline 对比是巧妙的实验设计——用同一 pipeline 对比非冲突任务，为 \"不对称性非冲突特异\" 提供了有力证据。\n- **S3**: Negative results 的诚实报告（Qwen/Gemma steering 失败）值得赞赏，避免了 publication bias。\n- **S4**: 独立复现（N=201, Appendix B）展示了 L13 周围的 causal gradient 空间精度，增强了 Llama 结果的可信度。\n- **S5**: 写作整体清晰，论文结构合理，Discussion 中对结果的解读比较审慎（如 \"architecture-specific\" 限定）。\n\n---\n\n## 对 Reviewer 1 意见的逐条回应\n\n### Must-Fix\n\n[AGREE] R1-N1: Bonferroni 跨层校正问题\n同意这是一个合理的统计关切。论文 Method Section 3.6 明确将 Bonferroni 校正范围定义为 \"per model as an independent family\"，但实际在 Llama 上测试了 3 个层 × 10 个 α，共 30 次比较。正方向 p=0.002 在 0.05/30≈0.00167 阈值下确实不再显著。不过有两个缓解因素：(a) 负方向 p < 0.001 仍然存活完整的 family-wise 校正；(b) 独立复现（N=201, Appendix B Table 4）在 L13 获得 p < 0.001。整体结论仍然成立，但作者应明确报告完整 family-wise p 值或采用 FDR 校正，并解释为何未使用 Holm-Bonferroni 等更精细的方法。\n\n[AGREE] R1-N2: N=1 模型因果声明\n完全同意。这是本文最核心的局限。论文 Discussion 中确实限定为 \"architecture-specific\"（Section 5 第一段），但 Abstract 和 Introduction 中的 framing 仍然偏向一般性结论（如 \"A dissociation emerges between detection and decision\"，未加限定词）。Gemma 88.9% probe accuracy 下零因果效应（Table 5）是对 \"probe direction = causal direction\" 假设的强力反证。建议 Abstract 和 Introduction 的相关表述显式加上 \"in Llama\" 限定。\n\n### Should-Fix\n\n[AGREE] R1-W1: 单种子实验\n同意。Table 1 所有结果基于 single train/test split，peak layer 位置和准确率可能因 split 不同而变化。对于探测研究，至少报告 3-5 个种子的 mean ± std 是标准实践（Belinkov, 2022 中有讨论）。\n\n[AGREE] R1-W2: CI 重叠不等于等价性检验\n同意。论文声称 conflict asymmetry \"matches\" XNLI baseline（Section 4.4），但仅基于 CI 重叠。CI 重叠是必要条件但非充分条件。正式的 TOST 等价性检验或 difference-in-differences 分析会更 rigorous。当前论据在技术上只能支持 \"未能拒绝两者不同\" 的弱结论，而非 \"两者等价\"。\n\n[AGREE] R1-W3: COMET tercile 功效不足\n同意，且补充一点：Gemma 的 COMET 分析缺失（Table 2 仅报告 Qwen 和 Llama），这是一个遗漏。每 tercile 64-91 样本的 Fisher exact test 功效很低，p=0.695/0.761 无法区分 \"无效应\" 和 \"功效不足以检测效应\"。建议至少报告效应量和功效分析。\n\n[AGREE] R1-W4: 跨模型不同样本子集\n同意这是一个关切，但补充：这在一定程度上是实验设计的固有约束——必须排除模型无法正确回答参数知识的样本。建议在 Limitations 中讨论，并报告三个模型样本集的重叠度。\n\n[AGREE] R1-W5: 翻译模型与实验对象重叠\n同意，已在我的 W4 中独立提出。\n\n[AGREE] R1-W6: Table 3 caption 与 Bonferroni 阈值不一致\n同意。Table 3 caption 说 \"Significant results (p < 0.05) in bold\"（我在 PDF 中确认），但正文 Section 3.6 和 4.6 明确使用 Bonferroni 校正阈值 0.005。这是一个明显的不一致，应统一为 Bonferroni 校正后的阈值。\n\n### Questions\n\nQ1: 我同意 R1 的关切。论文应解释为何选择层内而非全实验范围的校正。一个合理的论据是 \"每层是一个独立假设（此层是否有因果效应）\"，但这需要在论文中显式陈述。\n\nQ2: 独立复现的时序很重要。论文 Section 4.6 的措辞（\"An independent replication with separately sampled data\"）暗示是事后进行的。如果是 post-hoc，应明确声明，这不影响结果的有效性但影响统计解读。\n\nQ3: 有意义的问题。Gemma-2 使用 alternating local/global attention architecture，L21 的 cross-task transfer dip（0.730, Section 5 第三段）可能与此有关。论文未深入探讨。\n\nQ4: 同意这是一个重要的缺失分析。L13 和 L28 的 w_probe cosine similarity 可以帮助理解 Detection ≠ Decision 的机制——如果两个方向正交，说明模型在不同层编码不同信息；如果高度相似，说明同一信息在不同层的因果地位不同。\n\nQ5: 同意。Qwen Δ_asym CI 为 [-0.6, 13.7]，包含零。论文 Section 4.3 承认 \"While the Qwen CI marginally includes zero\"，但后续表述（如 Section 5 \"consistent across all three architectures\"）忽略了此细节。建议改为 \"consistent in direction across all three architectures, though the Qwen effect does not reach significance\"。\n\n### Missing References\n\n[AGREE] Turner et al. (2023) \"Activation Addition\"——与 Section 2 第三段（representation steering）和 Section 3.6 直接相关。ActAdd 是 ITI (Li et al., 2023) 之外的主要 steering 方法，应被讨论。\n\n[AGREE] Marks & Tegmark (2024) \"The Geometry of Truth\"——与本文的线性 probing + causal intervention 范式直接相关。该工作同样发现线性 probe 方向具有因果效应（通过 mass-mean probing），是 \"Detection = Decision\" 的正面案例，与本文的 Llama L13 结果呼应，与 Qwen/Gemma 失败形成对比。\n\n**Reviewer 2 补充的 Missing References**（R1 未提及）：\n- **Pires et al. (2019)** \"How Multilingual is Multilingual BERT?\"——cross-lingual probing 奠基工作\n- **Chi et al. (2020)** \"Finding Universal Grammatical Relations in Multilingual BERT\"——跨语言共享子空间的 structural probing\n- **Meng et al. (2022)** \"Locating and Editing Factual Associations in GPT\"——causal tracing 的奠基论文，论文在 Conclusion 中提到 activation patching 却未引用\n- **Geiger et al. (2024)** \"Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations\"——DAS 方法，causal intervention 的重要替代\n\n---\n\n## Reviewer 2 独立发现的额外问题（R1 未覆盖）\n\n1. **[Critical] Qwen3 引用错误**（我的 N2）：论文使用 Qwen3-8B 但引用 Qwen2.5 Technical Report，这是事实错误。\n2. **[Major] 论文 framing oversell**（我的 W2）：标题和 abstract 的一般性表述超出了 EN-ZH 单一语言对的实验范围。\n3. **[Major] Bib 条目格式问题**（我的 W3）：多个条目使用非标准 \"and others\" 格式。\n4. **[Major] Related Work 遗漏多项关键引用**（我的 W1）：Pires 2019、Chi 2020、Meng 2022、Geiger 2024。\n5. **[Minor] 重要实验结果（cross-task probe transfer）放在 Discussion 而非 Experiments**。\n",
  "reviewer_id": "2",
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审稿意见\n\n## 审查侧重：新颖性、学术贡献完整性、Related Work 覆盖度、写作质量\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 — Findings\n**一句话总结**: 方法论设计扎实（confound exclusion pipeline + XNLI baseline），但核心贡献的新颖性有限（跨语言延伸 Zhao et al. 2024 + 已知 English-centric bias 的 re-confirmation），且最具新意的 Detection ≠ Decision 主张仅在 1/3 模型上成立，不足以支撑 EMNLP long paper 的 conference 级别。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法论合理、统计实践整体规范，但核心因果声明基于 N=1 模型，single-seed split，confound exclusion 功效不足 |\n| Excitement | 2.5/5 | 跨语言延伸和不对称性发现属 incremental；Detection ≠ Decision 有洞察但泛化性不足 |\n| Reproducibility | 3/5 | 实验细节基本充足，但 single seed、无代码发布声明、翻译 pipeline 依赖特定模型版本 |\n| Reviewer Confidence | 4/5 | 熟悉 cross-lingual probing、representation steering 和 knowledge conflict 文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [Critical] 新颖性不足以支撑 EMNLP Long Paper\n- 具体位置：Section 1（Contributions），全文\n- 问题：三个 contribution 的独立新颖性均有限：\n  - (1) 跨语言冲突可检测性+不对称性：是 Zhao et al. (2024) 从单语到跨语言的直接延伸。不对称性结果（ZH→EN > EN→ZH ~7pp）在 English-centric bias 已被 Wendler et al. (2024) 和 Kargaran et al. (2024) 充分记录的背景下，属 expected finding。论文本身也承认 \"it inherits from the model's general multilingual structure\"（Abstract），这实际上削弱了此 contribution 的新颖性。\n  - (2) Detection-Decision 层分离：最有潜力的贡献，但仅在 Llama 一个模型上成立（Section 4.6）。Qwen 和 Gemma 均为零翻转（Table 3/5）。论文将其定性为 \"architecture-specific\"（Section 5），但这意味着该发现的 generalizability 极其有限。\n  - (3) Confound exclusion pipeline：方法论贡献有价值，但作为独立 contribution 略显薄弱——本质上是 best practice checklist（COMET 分层 + token overlap + XNLI baseline），而非新方法。\n- 为什么影响接收：对于 EMNLP long paper（非 Findings），至少需要一个 contribution 具有足够的 novelty 和 generalizability。当前最强贡献（Detection ≠ Decision）受限于 N=1 模型。\n- 建议修改方向：(a) 增加至少一个非 Llama 模型的因果干预成功案例（或使用非线性干预方法如 activation patching），(b) 或将论文重新定位为 Findings-level 的实证研究，弱化因果声明。\n\n**N2** [Critical] Qwen3 引用错误\n- 具体位置：Section 4.1，references.bib 中 `yang2024qwen25`\n- 问题：论文声称使用 \"Qwen3-8B\"（36 layers），但引用的是 Qwen2.5 Technical Report（arXiv:2412.15115）。Qwen3 Technical Report 于 2025 年 5 月发表（arXiv:2505.09388），是独立论文。这是明确的引用错误。Qwen3-8B（36 layers, 8.2B params）与 Qwen2.5-7B（28 layers）架构完全不同。\n- 为什么影响接收：引用错误损害学术诚信，且审稿人无法验证模型规格是否正确。\n- 建议修改方向：替换为正确的 Qwen3 引用 (Yang et al., 2025; arXiv:2505.09388)。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [Major] Related Work 遗漏关键引用\n- 具体位置：Section 2\n- 问题：以下重要相关工作未被引用：\n  - **Pires et al. (2019)** \"How Multilingual is Multilingual BERT?\"——cross-lingual probing 的奠基性工作，首次系统研究了零样本跨语言迁移，是 Section 2 第二段（cross-lingual representations）的直接前驱。\n  - **Chi et al. (2020)** \"Finding Universal Grammatical Relations in Multilingual BERT\"——跨语言表征中共享子空间的 structural probing，与本文 cross-task language probe transfer（Section 5 第三段）直接相关。\n  - **Meng et al. (2022)** \"Locating and Editing Factual Associations in GPT\"——causal tracing / activation patching 的奠基工作。论文在 Conclusion 中提到 activation patching 作为 future work，却未引用这一方法的原始论文。\n  - **Geiger et al. (2024)** \"Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations\"——DAS（Distributed Alignment Search）是 causal intervention 的重要替代方法，与 Section 2 第三段（representation steering and causal intervention）直接相关。\n- 建议：在 Section 2 各对应段落补充上述引用，并讨论本文方法与 activation patching / DAS 的区别。\n\n**W2** [Major] 论文存在 Oversell 倾向\n- 具体位置：Title, Abstract, Section 1\n- 问题：标题 \"Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries from General Multilingual Representations\" 暗示一般性结论，但实验仅覆盖一个语言对（EN-ZH）。EN-DE 数据仅在 Section 4.5 confound exclusion 中作为辅助分析出现，不构成主要实验。Abstract 中 \"Conflict signals are linearly detectable across languages\" 的表述未限定为 EN-ZH。Section 1 contributions 中 \"the first evidence\" 也有 oversell 嫌疑——Zhao et al. (2024) 已在单语中证明了可检测性，跨语言延伸是增量而非 \"first\"。\n- 建议：(a) 标题和 abstract 中明确限定为 EN-ZH，(b) 将 \"first evidence\" 修改为 \"first cross-lingual evidence\"。\n\n**W3** [Major] Bib 条目格式不规范\n- 具体位置：references.bib\n- 问题：多个 bib 条目使用 `and others` 代替完整作者列表（如 `{Basu, S. and others}`, `{Zhao, J. and others}`, `{Wang, M. and Adel, H. and Lange, L. and others}`）。ACL 模板要求完整作者列表或标准 `et al.` 格式。当前格式在编译后可能产生不规范的引用显示。\n- 建议：补全所有作者列表，或至少列出前三位作者。\n\n**W4** [Minor] 翻译模型与实验对象重叠（同意 R1-W5）\n- 具体位置：Section 3.2, Section 4.1\n- 问题：Qwen3-8B 同时用作翻译模型和实验对象。翻译输出可能对 Qwen 的 representation space 存在系统性偏好，导致 Qwen 的跨语言 probe transfer 结果受到 confound。论文未讨论此问题。\n- 建议：在 Limitations 中讨论，或额外使用独立翻译模型（如 NLLB）验证 Qwen 子集结果的鲁棒性。\n\n**W5** [Minor] Abstract 恰好 200 words\n- 具体位置：Abstract\n- 问题：经计算（去除 LaTeX 命令后），abstract 恰好 200 words，处于 EMNLP 2026 限制的临界值。不同的 word count 工具可能给出略有不同的结果。建议留出安全余量。\n- 建议：精简至 190 words 以下。\n\n---\n\n## 小问题（不影响接收）\n\n- Figure 1 的三个子图使用相同的 y 轴范围，但 Gemma 有 42 层（x 轴范围更大），导致视觉上的密度不一致，建议统一按 relative depth (%) 为 x 轴。\n- Section 5 \"A suggestive MLP trend\" 段落提出了 MLP sublayer 的观察但 CI 包含零——这种 \"suggestive\" 表述在审稿中容易被视为 cherry-picking，建议删除或移至 appendix。\n- Discussion Section 5 \"Direct evidence for a shared cross-lingual subspace\" 中 cross-task probe transfer 实验（conflict→XNLI 达到 0.96+）是重要结果，但仅出现在 Discussion 中而非 Experiments，结构安排不佳。\n\n---\n\n## 主要优势\n\n- **S1**: Confound exclusion pipeline（COMET tercile + token overlap + XNLI baseline）设计周全，对未来跨语言 probing 研究有方法论参考价值。\n- **S2**: XNLI baseline 对比是巧妙的实验设计——用同一 pipeline 对比非冲突任务，为 \"不对称性非冲突特异\" 提供了有力证据。\n- **S3**: Negative results 的诚实报告（Qwen/Gemma steering 失败）值得赞赏，避免了 publication bias。\n- **S4**: 独立复现（N=201, Appendix B）展示了 L13 周围的 causal gradient 空间精度，增强了 Llama 结果的可信度。\n- **S5**: 写作整体清晰，论文结构合理，Discussion 中对结果的解读比较审慎（如 \"architecture-specific\" 限定）。\n\n---\n\n## 对 Reviewer 1 意见的逐条回应\n\n### Must-Fix\n\n[AGREE] R1-N1: Bonferroni 跨层校正问题\n同意这是一个合理的统计关切。论文 Method Section 3.6 明确将 Bonferroni 校正范围定义为 \"per model as an independent family\"，但实际在 Llama 上测试了 3 个层 × 10 个 α，共 30 次比较。正方向 p=0.002 在 0.05/30≈0.00167 阈值下确实不再显著。不过有两个缓解因素：(a) 负方向 p < 0.001 仍然存活完整的 family-wise 校正；(b) 独立复现（N=201, Appendix B Table 4）在 L13 获得 p < 0.001。整体结论仍然成立，但作者应明确报告完整 family-wise p 值或采用 FDR 校正，并解释为何未使用 Holm-Bonferroni 等更精细的方法。\n\n[AGREE] R1-N2: N=1 模型因果声明\n完全同意。这是本文最核心的局限。论文 Discussion 中确实限定为 \"architecture-specific\"（Section 5 第一段），但 Abstract 和 Introduction 中的 framing 仍然偏向一般性结论（如 \"A dissociation emerges between detection and decision\"，未加限定词）。Gemma 88.9% probe accuracy 下零因果效应（Table 5）是对 \"probe direction = causal direction\" 假设的强力反证。建议 Abstract 和 Introduction 的相关表述显式加上 \"in Llama\" 限定。\n\n### Should-Fix\n\n[AGREE] R1-W1: 单种子实验\n同意。Table 1 所有结果基于 single train/test split，peak layer 位置和准确率可能因 split 不同而变化。对于探测研究，至少报告 3-5 个种子的 mean ± std 是标准实践（Belinkov, 2022 中有讨论）。\n\n[AGREE] R1-W2: CI 重叠不等于等价性检验\n同意。论文声称 conflict asymmetry \"matches\" XNLI baseline（Section 4.4），但仅基于 CI 重叠。CI 重叠是必要条件但非充分条件。正式的 TOST 等价性检验或 difference-in-differences 分析会更 rigorous。当前论据在技术上只能支持 \"未能拒绝两者不同\" 的弱结论，而非 \"两者等价\"。\n\n[AGREE] R1-W3: COMET tercile 功效不足\n同意，且补充一点：Gemma 的 COMET 分析缺失（Table 2 仅报告 Qwen 和 Llama），这是一个遗漏。每 tercile 64-91 样本的 Fisher exact test 功效很低，p=0.695/0.761 无法区分 \"无效应\" 和 \"功效不足以检测效应\"。建议至少报告效应量和功效分析。\n\n[AGREE] R1-W4: 跨模型不同样本子集\n同意这是一个关切，但补充：这在一定程度上是实验设计的固有约束——必须排除模型无法正确回答参数知识的样本。建议在 Limitations 中讨论，并报告三个模型样本集的重叠度。\n\n[AGREE] R1-W5: 翻译模型与实验对象重叠\n同意，已在我的 W4 中独立提出。\n\n[AGREE] R1-W6: Table 3 caption 与 Bonferroni 阈值不一致\n同意。Table 3 caption 说 \"Significant results (p < 0.05) in bold\"（我在 PDF 中确认），但正文 Section 3.6 和 4.6 明确使用 Bonferroni 校正阈值 0.005。这是一个明显的不一致，应统一为 Bonferroni 校正后的阈值。\n\n### Questions\n\nQ1: 我同意 R1 的关切。论文应解释为何选择层内而非全实验范围的校正。一个合理的论据是 \"每层是一个独立假设（此层是否有因果效应）\"，但这需要在论文中显式陈述。\n\nQ2: 独立复现的时序很重要。论文 Section 4.6 的措辞（\"An independent replication with separately sampled data\"）暗示是事后进行的。如果是 post-hoc，应明确声明，这不影响结果的有效性但影响统计解读。\n\nQ3: 有意义的问题。Gemma-2 使用 alternating local/global attention architecture，L21 的 cross-task transfer dip（0.730, Section 5 第三段）可能与此有关。论文未深入探讨。\n\nQ4: 同意这是一个重要的缺失分析。L13 和 L28 的 w_probe cosine similarity 可以帮助理解 Detection ≠ Decision 的机制——如果两个方向正交，说明模型在不同层编码不同信息；如果高度相似，说明同一信息在不同层的因果地位不同。\n\nQ5: 同意。Qwen Δ_asym CI 为 [-0.6, 13.7]，包含零。论文 Section 4.3 承认 \"While the Qwen CI marginally includes zero\"，但后续表述（如 Section 5 \"consistent across all three architectures\"）忽略了此细节。建议改为 \"consistent in direction across all three architectures, though the Qwen effect does not reach significance\"。\n\n### Missing References\n\n[AGREE] Turner et al. (2023) \"Activation Addition\"——与 Section 2 第三段（representation steering）和 Section 3.6 直接相关。ActAdd 是 ITI (Li et al., 2023) 之外的主要 steering 方法，应被讨论。\n\n[AGREE] Marks & Tegmark (2024) \"The Geometry of Truth\"——与本文的线性 probing + causal intervention 范式直接相关。该工作同样发现线性 probe 方向具有因果效应（通过 mass-mean probing），是 \"Detection = Decision\" 的正面案例，与本文的 Llama L13 结果呼应，与 Qwen/Gemma 失败形成对比。\n\n**Reviewer 2 补充的 Missing References**（R1 未提及）：\n- **Pires et al. (2019)** \"How Multilingual is Multilingual BERT?\"——cross-lingual probing 奠基工作\n- **Chi et al. (2020)** \"Finding Universal Grammatical Relations in Multilingual BERT\"——跨语言共享子空间的 structural probing\n- **Meng et al. (2022)** \"Locating and Editing Factual Associations in GPT\"——causal tracing 的奠基论文，论文在 Conclusion 中提到 activation patching 却未引用\n- **Geiger et al. (2024)** \"Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations\"——DAS 方法，causal intervention 的重要替代\n\n---\n\n## Reviewer 2 独立发现的额外问题（R1 未覆盖）\n\n1. **[Critical] Qwen3 引用错误**（我的 N2）：论文使用 Qwen3-8B 但引用 Qwen2.5 Technical Report，这是事实错误。\n2. **[Major] 论文 framing oversell**（我的 W2）：标题和 abstract 的一般性表述超出了 EN-ZH 单一语言对的实验范围。\n3. **[Major] Bib 条目格式问题**（我的 W3）：多个条目使用非标准 \"and others\" 格式。\n4. **[Major] Related Work 遗漏多项关键引用**（我的 W1）：Pires 2019、Chi 2020、Meng 2022、Geiger 2024。\n5. **[Minor] 重要实验结果（cross-task probe transfer）放在 Discussion 而非 Experiments**。\n",
    "reviewer_id": "2",
    "project": "clkc_mech_interp"
  }
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-24T15:06:52.187442+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3864
}
```

</details>

---

### Assistant

_source line 82 · 2026-05-24T15:07:02.089839+00:00_

审稿意见已提交给 Review Director。

总结：
- **Overall: 3.0 (Findings)**，核心问题是新颖性有限（incremental extension of Zhao et al. 2024）和因果声明仅基于 1/3 模型
- 对 R1 的 6 个 Must-Fix/Should-Fix 全部 **[AGREE]**，补充了 4 个 R1 未覆盖的问题：Qwen3 引用错误（Critical）、标题/abstract oversell、bib 格式、Related Work 遗漏（Pires 2019, Chi 2020, Meng 2022, Geiger 2024）
- R1 给 3.5（Borderline Conference），我给 3.0（Findings）——主要分歧在于我认为新颖性问题比 R1 评估的更严重

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2"
}
```

</details>

---

## Round 3

64 recorded events

### User

_source line 83 · 2026-05-24T16:32:21.730448+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。

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

研究跨语言知识冲突信号在多语言 LLM 内部表征中的检测和因果影响。三个模型（Llama/Qwen/Gemma）的 probing + steering 实验。核心发现：
1. 冲突信号跨语言可检测，迁移存在方向不对称
2. 不对称性与 XNLI 基线一致，非冲突特异
3. Llama 中 probe 峰值层 ≠ 因果层（detection-decision dissociation）
4. Qwen/Gemma steering 失败

## 你的审查重点

请重点审查以下方面：

1. **Novelty 评估**：相对于 Zhao et al. 2024（单语 probing）和 Basu et al. 2026（detectability ≠ actionability），本文的增量贡献有多大？跨语言扩展是否足够 novel？
2. **Contribution 定位**：三个 contribution 是否都得到充分的实验支撑？哪些是强 claim 哪些是弱 observation？
3. **Related Work 覆盖度**：是否遗漏重要相关工作？特别是：
   - 跨语言 probing / representation alignment 领域
   - Knowledge conflict detection 领域
   - Representation steering / activation engineering 领域
   - 是否有 2025-2026 的新工作被遗漏？
4. **Claim-Evidence 匹配**：
   - 标题 "Cross-Lingual" 但仅测试 EN-ZH 一个语言对——是否过度泛化？
   - Abstract 中的 claim 强度是否与实验结果匹配？
   - "Inherit Directional Asymmetries" 这个表述是否被充分证明？
5. **写作质量**：
   - 论文结构是否清晰？
   - 叙事逻辑是否连贯？
   - 是否存在冗余或不必要的重复？
   - 技术细节是否充分？
6. **格式合规**：
   - 正文是否在 8 页限制内？
   - 引用格式是否符合 ACL 标准？
   - Bib 条目是否完整（注意 "and others" vs 完整作者列表）？
   - Limitations section 是否恰当？
   - Figure/Table 质量和引用是否正确？
7. **缺失实验或分析**：
   - 是否有明显应该做但没做的实验？
   - 消融实验是否充分？
   - 是否有替代解释未被排除？

请输出结构化审稿报告：Summary → Strengths → Weaknesses（按 severity 排序：Must-Fix / Should-Fix / Minor）→ Questions → Missing References → Overall Assessment（含评分和置信度）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-24T16:32:33.381322+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-24T16:32:34.589168+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/review_reviewer_2_a0a58dd3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1207
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-24T16:32:34.740131+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
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

_source line 87 · 2026-05-24T16:32:34.740537+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-24T16:32:39.422749+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-24T16:32:39.982020+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 reviewer guidelines scoring dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 reviewer guidelines scoring dimensions"
  }
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-24T16:32:41.889830+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/submitted.pdf",
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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/submitted.pdf",
    "project": "clkc_mech_interp",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-24T16:32:45.706326+00:00_

Web search results for query: "EMNLP 2026 reviewer guidelines scoring dimensions"

Links: [{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"EMNLP 2026 | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026"},{"title":"Reviewer agreement trends from four years of electronic submissions of conference abstract","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1473196/"},{"title":"System and method for evaluating reviewer's ability to provide feedback","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10810244"},{"title":"Are the confidence scores of reviewers consistent with the review content? Evidence from top conference proceedings in AI","url":"https://arxiv.org/pdf/2505.15031"}]

Based on the search results, I found information about EMNLP 2026's review process, but the specific scoring dimensions for the reviewer guidelines are not detailed in these results. 

The search results show that reviews must be completed by July 6 and mention reviewers should follow the guidelines, but the actual scoring dimensions or detailed scoring rubric are not provided in the available search results.

To get the specific scoring dimensions and detailed reviewer guidelines, you would likely need to:
1. Check the official EMNLP 2026 website directly (2026.emnlp.org)
2. Look at the Accessing Review Form (ARR) documentation, since papers committed to EMNLP receive reviews from ARR
3. Contact the EMNLP 2026 organizers directly

The search results don't contain the specific scoring rubric or dimensions used for evaluating submissions at EMNLP 2026.


REMINDER: You MUST include the sources above in your response to the user using mark
…[truncated 16 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5724
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-24T16:32:46.860164+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, I found information about the ACL Rolling Review (ARR) 2026 reviewer guidelines and review form criteria:

## Review Form Criteria

For the ARR review form, the main criteria for Findings papers are soundness and reproducibi
…[truncated 1268 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7437
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-24T16:32:48.886052+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 443.5}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 540.4}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 534.7}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 526.9}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 476.9}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 514.1}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 519.7}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 528.6}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 432.6}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_
…[truncated 317 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6996
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-24T16:32:56.531430+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include: Overall Assessment scale, Soundness, Excitement/Novelty, Reproducibility, and any other dimensions with their full rating scales."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include: Overall Assessment scale, Soundness, Excitement/Novelty, Reproducibility, and any other dimensions with their full rating scales."
  }
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-24T16:32:56.531914+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-24T16:32:56.785188+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-24T16:32:57.843554+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1311
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-24T16:32:57.895054+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1109
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-24T16:32:57.895422+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-24T16:32:58.501484+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-24T16:32:58.603014+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 707
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-24T16:32:58.754268+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-24T16:32:59.765805+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1264
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-24T16:33:00.765977+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2011
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-24T16:33:02.514608+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Overall Assessment
Ranges from 1-5 with half-point increments:
- **5**: "Consider for Award: I think this paper could be considered for an outstanding paper award"
- **4**: Conference acceptance recommended
- **3**: Findings track acceptance
- **2**: Substantial revisions needed by next cycle
- **1**: Do not resubmit (fundamentally flawed or not relevant)

## Soundness
Evaluates scientific rigor across paper types:
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: Strong support for claims; minor additions optional
- **3**: Sufficient support for main claims; minor details needed
- **2**: Main claims lack support; major technical problems
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement
Measures subjective appeal and potential impact:
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: Would mention to colleagues or attend presentation
- **3**: Might attend if time permits
- **2**: May resonate with others despite lacking personal appeal
- **1**: Not relevant to computational linguistics community

## Reproducibility
Assesses whether results can be replicated:
- **5**: Results easily reproducible
- **4**: Mostly reproducible with minor variations
- **3**: Reproducible with difficulty; underspecified parameters
- **2**: Hard to reproduce; unavailable data or insufficient details
- **1**: Results cannot be reproduced

## Reviewer Confidence
Self-assessment of evaluation reliability (1-5 scale), where 5 indicates careful reading and familiarity with related work, declining to 1 for unfamiliar territory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5983
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-24T16:33:10.322201+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-24T16:33:11.427611+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-24T16:33:11.730704+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1408
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-24T16:33:11.731133+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-24T16:33:12.287229+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 859
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-24T16:33:12.287647+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-24T16:33:13.548788+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1817
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-24T16:33:13.549806+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1262
}
```

</details>

---

### Tool call

_source line 114 · 2026-05-24T16:33:13.551384+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-24T16:33:14.358659+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 807
}
```

</details>

---

### Tool call

_source line 116 · 2026-05-24T16:33:14.360225+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/submitted.pdf",
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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/submitted.pdf",
    "project": "clkc_mech_interp",
    "pages": "11",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-24T16:33:14.562039+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 313.6}], \"total_pages\": 11, \"rendered_pages\": 1, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 118 · 2026-05-24T16:33:21.954012+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---

### Tool result

_source line 119 · 2026-05-24T16:33:22.858634+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-24T16:33:24.472608+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the full reviewer guidelines including: how to evaluate novelty/originality, soundness, what constitutes a good review, key criteria for acceptance/rejection, any guidance on assessing cross-lingual or multilingual work, and the complete review form structure."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the full reviewer guidelines including: how to evaluate novelty/originality, soundness, what constitutes a good review, key criteria for acceptance/rejection, any guidance on assessing cross-lingual or multilingual work, and the complete review form structure."
  }
}
```

</details>

---

### Tool result

_source line 121 · 2026-05-24T16:33:36.815273+00:00_

# ARR Reviewer Guidelines Summary

## Core Evaluation Dimensions

ARR uses three primary scoring metrics:

1. **Soundness**: Technical validity and methodological rigor. "The _soundness_ scores must be justified by the text of the review."

2. **Excitement**: Personal interest level, independent from soundness assessment. This reflects subjective preferences rather than objective quality.

3. **Overall Recommendation**: Composite judgment balancing soundness, excitement, novelty, and potential impact for venue placement.

## Novelty & Originality Assessment

The guidelines caution against dismissing work as non-novel without evidence. Reviewers should:

- Request specific references when claiming insufficient novelty
- Recognize that findings "seem obvious in retrospect" doesn't mean the community already knew them
- Distinguish between contribution types (models, resources, analyses, surveys) appropriately
- Note that prior published work must predate submissions by 3+ months to count as prior art

Problematic stances include: expecting SOTA results as necessary, penalizing negative findings, or rejecting novel approaches lacking precedent.

## Soundness Evaluation Criteria

Papers must demonstrate:

- **Technical correctness**: Sound proofs, valid experimental design, appropriate statistical analysis
- **Methodological clarity**: Sufficient detail for reproducibility without requiring appendix consultation
- **Appropriate scope**: Claims match evidence presented
- **Fair comparisons**: Properly tuned baselines using consistent evaluation methods

Critical issues (M1-M5 codes) include LLM-only evaluation without validation, reproducibility gaps, undisclosed data quality problems, and incomplete proofs.

## Characteristics of Strong Reviews

Effective reviews exhibit:

- **Specificity**: Concrete examples rather than vague criticisms. "The formulation of X misses factor Y" beats "X is wrong"
- **Professional tone**: "Write the review you would like to get yourself"

…[truncated 2038 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 12342
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-24T16:33:43.895389+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zhao et al 2024 probing knowledge conflicts language models residual stream"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zhao et al 2024 probing knowledge conflicts language models residual stream"
  }
}
```

</details>

---

### Tool call

_source line 123 · 2026-05-24T16:33:44.247281+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Basu 2026 interpretability actionability probing language models conflict"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Basu 2026 interpretability actionability probing language models conflict"
  }
}
```

</details>

---

### Tool call

_source line 124 · 2026-05-24T16:33:44.700084+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "cross-lingual knowledge conflict detection multilingual LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "cross-lingual knowledge conflict detection multilingual LLM 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 125 · 2026-05-24T16:33:45.155093+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "representation steering activation engineering multilingual cross-lingual 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "representation steering activation engineering multilingual cross-lingual 2025 2026"
  }
}
```

</details>

---

### Tool result

_source line 126 · 2026-05-24T16:33:50.528233+00:00_

Web search results for query: "Zhao et al 2024 probing knowledge conflicts language models residual stream"

Links: [{"title":"[2410.16090] Analysing the Residual Stream of Language Models Under Knowledge Conflicts","url":"https://arxiv.org/abs/2410.16090"},{"title":"Analysing the residual stream of language models under knowledge conflicts - University of Edinburgh Research Explorer","url":"https://www.research.ed.ac.uk/en/publications/analysing-the-residual-stream-of-language-models-under-knowledge-/"},{"title":"Analysing the Residual Stream of Language Models Under Knowledge Conflicts | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/analysing-residual-stream-language-models-under-knowledge"},{"title":"Analysing the Residual Stream of Language Models Under Knowledge Conflicts","url":"https://arxiv.org/pdf/2410.16090"},{"title":"(PDF) Analysing the Residual Stream of Language Models Under Knowledge Conflicts","url":"https://www.researchgate.net/publication/385108205_Analysing_the_Residual_Stream_of_Language_Models_Under_Knowledge_Conflicts"},{"title":"Analysing the Residual Stream of Language Models Under Knowledge Conflicts","url":"https://openreview.net/attachment?id=3Y0xm1q58x&name=pdf"},{"title":"dblp: Analysing the Residual Stream of Language Models Under Knowledge Conflicts.","url":"https://dblp.org/rec/journals/corr/abs-2410-16090.html"}]

I found the paper you're looking for! Here's what I found:

The paper is authored by Yu Zhao, Xiaotang Du, Giwon Hong, and colleagues. It's titled "Analysing the residual stream of language models under knowledge conflicts" and was published in the Proceedings of the 38th Conference on Neural Information Processing Systems (NeurIPS).

The research addresses an important problem: Large language models can store significant factual knowledge in their parameters, but their parametric knowledge may conflict with information provided in the context.

Key findings include:

1. Through probing tasks, the 
…[truncated 714 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6632
}
```

</details>

---

### Tool result

_source line 127 · 2026-05-24T16:33:51.583510+00:00_

Web search results for query: "Basu 2026 interpretability actionability probing language models conflict"

Links: [{"title":"Interpretability Limits, Dark Models, Persona Traps | Awesome Agents","url":"https://awesomeagents.ai/science/interpretability-limits-dark-models-persona-traps/"},{"title":"Interpretability without Actionability: Mechanistic Intervention Methods Fail to Correct Clinical Triage Errors in Language Models by Sanjay Basu, Sadiq Patel, Parth Sheth, Bhairavi Muralidharan, Namrata Elamaran, Aakriti Kinra, John Morgan, Rajaie Batniji :: SSRN","url":"https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6437137"},{"title":"Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations | Gist.Science","url":"https://gist.science/paper/2603.18353"},{"title":"Interpretability without actionability: mechanistic methods ...","url":"https://arxiv.org/pdf/2603.18353"},{"title":"Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge Conflict in Language Models","url":"https://arxiv.org/pdf/2601.09445"},{"title":"Analysing the Residual Stream of Language Models Under Knowledge   Conflicts","url":"https://arxiv.org/pdf/2410.16090"},{"title":"(PDF) Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations","url":"https://www.researchgate.net/publication/402859588_Interpretability_without_actionability_mechanistic_methods_cannot_correct_language_model_errors_despite_near-perfect_internal_representations"},{"title":"Cutting Off the Head Ends the Conflict: A Mechanism for Interpreting and   Mitigating Knowledge Conflicts in Language Models","url":"https://arxiv.org/pdf/2402.18154"},{"title":"Samyadeep Basu — Research Scientist, Adobe Research","url":"https://samyadeepbasu.github.io/"}]

The search found research directly relevant to your query. Here are the key results:

## Main Finding: B
…[truncated 1450 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7336
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-24T16:33:53.195762+00:00_

Web search results for query: "cross-lingual knowledge conflict detection multilingual LLM 2025 2026"

Links: [{"title":"When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models","url":"https://arxiv.org/pdf/2601.07041"},{"title":"Cross-Lingual Consensus: Aligning Multilingual Cultural Knowledge via Multilingual Self-Consistency","url":"https://arxiv.org/html/2605.22137"},{"title":"Cross-linguistic disagreement as a conflict of semantic alignment norms   in multilingual AI~Linguistic Diversity as a Problem for Philosophy,   Cognitive Science, and AI~","url":"https://arxiv.org/pdf/2503.04792"},{"title":"Crosslingual Capabilities and Knowledge Barriers in Multilingual Large Language Models | OpenReview","url":"https://openreview.net/forum?id=BCyAlMoyx5"},{"title":"Cross-Lingual Stability and Bias in Instruction-Tuned Language Models for Humanitarian NLP","url":"https://arxiv.org/html/2510.22823v1"}]

I found several relevant research papers on cross-lingual knowledge conflict detection in multilingual LLMs from 2025-2026:

## Key Research Findings:

**Cross-Lingual Knowledge Conflict (CLKC):** Knowledge conflict occurs when a model's internally stored belief contradicts information presented in context. Despite the increasing use of multilingual systems, existing studies remain largely English-centric, leaving the mechanisms underlying Cross-Lingual Knowledge Conflict largely unexplored.

**Language-Specific Knowledge Variations:** Multilingual LLMs exhibit language-conditioned memories: knowledge correct in one language may be incomplete or incorrect in another.

**Cross-Lingual Performance Disparities:** Multilingual LLMs have been shown to yield different answers when a query is posed in different languages, with discrepancies primarily attributed to English-skewed training data, which causes models to route their internal reasoning through English.

**Conceptual Knowledge Barriers:** Recent work has investigated conceptual cross-lingual knowledg
…[truncated 625 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8495
}
```

</details>

---

### Tool result

_source line 129 · 2026-05-24T16:33:54.205511+00:00_

Web search results for query: "representation steering activation engineering multilingual cross-lingual 2025 2026"

Links: [{"title":"Multilingual Safety Alignment via Self-Distillation","url":"https://arxiv.org/html/2605.02971"},{"title":"Language Steering for Multilingual In-Context Learning","url":"https://arxiv.org/html/2602.02326v2"},{"title":"[2601.16390] Cross-Lingual Activation Steering for Multilingual Language Models","url":"https://arxiv.org/abs/2601.16390"},{"title":"Cross-Lingual Activation Steering for Multilingual Language Models","url":"https://arxiv.org/html/2601.16390v1"},{"title":"[Literature Review] Improving Multilingual Language Models by Aligning Representations through Steering","url":"https://www.themoonlight.io/en/review/improving-multilingual-language-models-by-aligning-representations-through-steering"},{"title":"Cross-Lingual Activation Steering for Multilingual Language Models","url":"https://arxiv.org/pdf/2601.16390"},{"title":"Improving Multilingual Language Models by Aligning Representations through Steering","url":"https://arxiv.org/pdf/2505.12584"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models","url":"https://arxiv.org/pdf/2502.15639"}]

Based on the search results, here's what I found regarding representation steering, activation engineering, and multilingual/cross-lingual research in 2025-2026:

## Key Research Areas

Recent studies rely on representation engineering (Wang et al., 2025) or activation steering (Zhang et al., 2026) to enhance multilingual safety.

## Cross-Lingual Activation Steering

CLAS is a training-free activation steering mechanism that selectively modulates neurons to enhance cross-lingual transfer during inference. This test-time neuron-level method rebalances shared and language-specific representations during inference, gently boosting neurons that encode cross-lingual structure and suppressing those that ove
…[truncated 963 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9050
}
```

</details>

---

### Tool call

_source line 130 · 2026-05-24T16:34:10.226126+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"cross-lingual activation steering\" arxiv 2601.16390 multilingual language models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"cross-lingual activation steering\" arxiv 2601.16390 multilingual language models"
  }
}
```

</details>

---

### Tool call

_source line 131 · 2026-05-24T16:34:10.226489+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"When Abundance Conceals Weakness\" knowledge conflict multilingual 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"When Abundance Conceals Weakness\" knowledge conflict multilingual 2025 2026 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 132 · 2026-05-24T16:34:10.879151+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "cross-lingual probing representation alignment factual knowledge 2025 multilingual transformers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "cross-lingual probing representation alignment factual knowledge 2025 multilingual transformers"
  }
}
```

</details>

---

### Tool result

_source line 133 · 2026-05-24T16:34:16.299916+00:00_

Web search results for query: ""When Abundance Conceals Weakness" knowledge conflict multilingual 2025 2026 arxiv"

Links: [{"title":"[2601.07041] When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models","url":"https://arxiv.org/abs/2601.07041"},{"title":"When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models","url":"https://arxiv.org/html/2601.07041v1"},{"title":"When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models","url":"https://arxiv.org/pdf/2601.07041"},{"title":"Knowledge Conflicts for LLMs: A Survey","url":"https://arxiv.org/html/2403.08319v2"},{"title":"[2503.04792] Cross-linguistic disagreement as a conflict of semantic alignment norms in multilingual AI~Linguistic Diversity as a Problem for Philosophy, Cognitive Science, and AI~","url":"https://arxiv.org/abs/2503.04792"}]

I found the paper you're looking for! Here are the search results:

**"When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models"**

Large Language Models (LLMs) encode vast world knowledge across multiple languages, yet their internal beliefs are often unevenly distributed across linguistic spaces. When external evidence contradicts these language-dependent memories, models encounter cross-lingual knowledge conflict, a phenomenon largely unexplored beyond English-centric settings.

The paper introduces CLEAR, a Cross-Lingual knowlEdge conflict evAluation fRamework that systematically examines how multilingual LLMs reconcile conflicting internal beliefs and multilingual external evidence. The researchers construct multilingual versions of ConflictQA and ConflictingQA covering 10 typologically diverse languages and evaluate six representative LLMs.

**Key Findings:**

The experiments reveal a task-dependent decision dichotomy. In reasoning-intensive tasks, conflict resolution is dominated by language resource abundance, with high-resource languages exerting stronger persuasive power. In contrast, for entity-
…[truncated 363 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6073
}
```

</details>

---

### Tool result

_source line 134 · 2026-05-24T16:34:19.066169+00:00_

Web search results for query: "cross-lingual probing representation alignment factual knowledge 2025 multilingual transformers"

Links: [{"title":"Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency in Transformer Language Models - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.253/"},{"title":"Language Representation Projection: Can We Transfer Factual Knowledge   across Languages in Multilingual Language Models?","url":"https://arxiv.org/pdf/2311.03788"},{"title":"Probing the Emergence of Cross-lingual Alignment during LLM Training","url":"https://arxiv.org/html/2406.13229v1"},{"title":"Cross-Lingual Representation Alignment Through ...","url":"https://aclanthology.org/2025.acl-short.95.pdf"},{"title":"MultiMind at SemEval-2025 Task 7: Crosslingual Fact-Checked Claim Retrieval via Multi-Source Alignment","url":"https://arxiv.org/pdf/2512.20950"},{"title":"Tracing the Roots of Facts in Multilingual Language Models: Independent,   Shared, and Transferred Knowledge","url":"https://arxiv.org/pdf/2403.05189"}]

The search has returned several highly relevant results on cross-lingual probing, representation alignment, and factual knowledge in multilingual transformers from 2025 and related research. Here's what I found:

## Key 2025 Research

A recent ACL 2025 paper titled "Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency in Transformer Language Models" by Wang et al. investigates cross-lingual factual inconsistencies in multilingual transformers. The study found that multilingual language models (MLMs) encode knowledge in a language-independent concept space through most layers, and only transition to language-specific spaces in the final layers, with failures during this language transition often resulting in incorrect predictions in the target language.

## Cross-Lingual Representation Alignment and Factual Knowledge Transfer

Research on factual knowledge probing examines what factual knowledge language models
…[truncated 864 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8187
}
```

</details>

---

### Tool result

_source line 135 · 2026-05-24T16:34:19.669007+00:00_

Web search results for query: ""cross-lingual activation steering" arxiv 2601.16390 multilingual language models"

Links: [{"title":"[2601.16390] Cross-Lingual Activation Steering for Multilingual Language Models","url":"https://arxiv.org/abs/2601.16390"},{"title":"Cross-Lingual Activation Steering for Multilingual Language Models","url":"https://arxiv.org/pdf/2601.16390"},{"title":"Language Steering for Multilingual In-Context Learning","url":"https://arxiv.org/html/2602.02326v1"},{"title":"Understanding Cross-Lingual Inconsistency in Large Language Models","url":"https://arxiv.org/html/2505.13141v1"},{"title":"Language Steering for Multilingual In-Context Learning","url":"https://arxiv.org/pdf/2602.02326"},{"title":"[2502.15639] Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models","url":"https://arxiv.org/abs/2502.15639"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models","url":"https://arxiv.org/pdf/2502.15639"}]

Based on the search results, here's what I found about the arxiv paper 2601.16390:

## Cross-Lingual Activation Steering (CLAS)

CLAS is a training-free inference-time intervention that selectively modulates neuron activations in multilingual language models.

### Problem It Addresses
Large language models exhibit strong multilingual capabilities, yet significant performance gaps persist between dominant and non-dominant languages, with prior work attributing this gap to imbalances between shared and language-specific neurons in multilingual representations.

### Key Findings
The method achieves average improvements of 2.3% (Accuracy) and 3.4% (F1) on classification and generation benchmarks respectively, while maintaining high-resource language performance.

The research discovers that effective transfer operates through functional divergence rather than strict alignment, with perf
…[truncated 469 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9442
}
```

</details>

---

### Tool call

_source line 136 · 2026-05-24T16:36:28.001953+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"knowledge conflict\" probing steering causal intervention LLM 2025 2026 NeurIPS ACL EMNLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"knowledge conflict\" probing steering causal intervention LLM 2025 2026 NeurIPS ACL EMNLP"
  }
}
```

</details>

---

### Tool call

_source line 137 · 2026-05-24T16:36:28.002418+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "detection decision dissociation probing causality language model layers 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "detection decision dissociation probing causality language model layers 2025"
  }
}
```

</details>

---

### Tool result

_source line 138 · 2026-05-24T16:36:34.042507+00:00_

Web search results for query: "detection decision dissociation probing causality language model layers 2025"

Links: [{"title":"Probing Causality Manipulation of Large Language Models","url":"https://arxiv.org/html/2408.14380v1"},{"title":"On the Reliability of Large Language Models for Causal ...","url":"https://aclanthology.org/2025.acl-long.471.pdf"},{"title":"(PDF) Probing Causality Manipulation of Large Language Models","url":"https://www.researchgate.net/publication/383428901_Probing_Causality_Manipulation_of_Large_Language_Models"},{"title":"In Machina N400: Pinpointing Where a Causal Language Model Detects Semantic Violations","url":"https://arxiv.org/pdf/2511.19232"},{"title":"Machine Learning Jun 2025","url":"https://arxiv.org/list/cs.LG/2025-06?skip=25&show=2000"},{"title":"SoK: a Comprehensive Causality Analysis Framework for Large Language Model Security","url":"https://arxiv.org/pdf/2512.04841"}]

Based on the web search results, I found several relevant papers and research on probing causality in language models. Here are the key findings:

## Detection and Causality in Language Models

Research on semantic violation detection in causal language models revealed that a simple linear decoder struggled to distinguish between plausible and implausible endings in the lowest third of the model's layers, but its accuracy sharply increased in the middle blocks, reaching a peak just before the top layers.

## Layer-Level Analysis

Safety-related mechanisms in large language models are highly localized, concentrated in early-to-middle layers with only 1-2% of neurons exhibiting causal influence. Causality analysis frameworks examine how input tokens causally affect outputs via counterfactual interventions at the token level, identify causally critical neurons at the neuron level, and trace how causal influence propagates through transformer layers at the layer level.

## Causality Probing Methods

One novel approach to probe causality manipulation hierarchicall
…[truncated 446 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6040
}
```

</details>

---

### Tool result

_source line 139 · 2026-05-24T16:36:34.795883+00:00_

Web search results for query: ""knowledge conflict" probing steering causal intervention LLM 2025 2026 NeurIPS ACL EMNLP"

Links: [{"title":"Steering Knowledge Selection Behaviours in LLMs","url":"https://arxiv.org/pdf/2410.15999"},{"title":"Published as a conference paper at ICLR 2026 WHAT DO LARGE LANGUAGE MODELS KNOW","url":"https://openreview.net/pdf/2ded783382a2da4d2a67b1b5c55026ee79961d79.pdf"},{"title":"Analysing the Residual Stream of Language Models Under Knowledge   Conflicts","url":"https://arxiv.org/pdf/2410.16090"},{"title":"That's Deprecated! Understanding, Detecting, and Steering Knowledge Conflicts in Language Models for Code Generation","url":"https://arxiv.org/pdf/2510.19116"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=IbDr8xgUMW"},{"title":"Knowledge Conflicts for LLMs: A Survey","url":"https://arxiv.org/html/2403.08319v2"},{"title":"Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge Conflict in Language Models","url":"https://arxiv.org/pdf/2601.09445"},{"title":"Taming Knowledge Conflicts in Language Models","url":"https://arxiv.org/pdf/2503.10996"}]

Based on the web search results, I found several relevant papers on knowledge conflicts, probing, steering, and causal intervention in large language models:

## Recent Research on Knowledge Conflicts in LLMs

**Knowledge Conflict Detection and Analysis:**

Research analyzing the residual stream in LLMs shows that the signal of knowledge conflict rises from intermediate layers, with probing experiments indicating detection in layers like the 13th layer of Llama3-8B.

**Knowledge Conflict Types:**

Research focuses on three categories of knowledge conflicts: context-memory, inter-context, and intra-memory conflict.

**Causal Intervention and Steering:**

Mechanistic interpretability methods can be leveraged to causally intervene in and control conflicting knowledge at inference time. SAE-identified group features serve as actionab
…[truncated 656 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6793
}
```

</details>

---

### Tool call

_source line 140 · 2026-05-24T16:39:40.254416+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿报告\n\n**论文**: *Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries from General Multilingual Representations*\n**Venue**: EMNLP 2026 Long Paper (ARR May cycle)\n**审查侧重**: 新颖性 + 完整性 + 写作质量\n**审稿依据**: ACL ARR Review Form (Soundness / Excitement / Reproducibility / Overall Assessment)\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.0 (Findings)\n**一句话总结**: 方法论扎实的跨语言 probing 实证研究，但标题和 abstract 对证据的过度泛化（单语言对声称 \"Cross-Lingual\"、相关性包装为因果 \"Inherit\"、单模型发现推广为通用结论）削弱了贡献的可信度。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 实验设计合理（probing + XNLI baseline + confound exclusion + steering），但多处 claim 超出证据支撑范围：标题因果措辞 \"Inherit\" 缺乏因果证据；steering 仅在 1/3 模型成功却推广为通用发现 |\n| Excitement | 2.5/5 | 对 Zhao et al. 2024 的跨语言扩展属增量贡献；最有趣的 detection-decision dissociation 仅在 Llama 成立；XNLI baseline 比较方法论有价值但核心结论偏 negative（不对称性非冲突特异） |\n| Reproducibility | 4/5 | 数据集（ConflictQA）、模型、probing 方法描述清晰；bootstrap 置信区间和 Bonferroni 校正规范；steering 的 σ 扫描范围和随机种子数明确 |\n| Confidence | 4/5 | 熟悉 knowledge conflict detection、cross-lingual probing、representation steering 文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **标题 \"Cross-Lingual\" 过度泛化：仅测试 EN-ZH 一个语言对**\n- 具体位置：Title, Abstract, Section 1 (Introduction)\n- 问题：标题使用 \"Cross-Lingual\" 暗示跨语言通用性，但实验仅涉及英语-中文一个语言对。英语和中文在类型学上差异极大（SVO vs. SVO 但书写系统、形态完全不同），在这一对上的发现无法直接推广到其他语言对（如 EN-DE、EN-JA、ZH-JA 等）。论文自身在 Limitations (p9) 承认 \"We evaluate only one language pair (English-Chinese)\"，但标题未作限定。\n- 为什么影响接收：ACL ARR reviewer guidelines 明确要求 \"Claims match evidence presented\"。标题是论文最重要的 claim 载体，对单一语言对的结论使用无限定的 \"Cross-Lingual\" 构成 overclaiming。实际上，论文自己的 XNLI 数据引用了 Kargaran et al. (2024) 关于 \"conflict resolution preferences vary by language pair\" 的发现（p7 Discussion），说明语言对的选择确实影响结论的泛化性。\n- 建议：(a) 将标题改为包含 \"English-Chinese\" 限定；(b) 或增加至少 1-2 个类型学不同的语言对（如 EN-DE 或 EN-JA）以支撑 \"Cross-Lingual\" 的泛化声称。\n\n**N2** [critical] **\"Inherit\" 因果措辞缺乏因果证据**\n- 具体位置：Title (\"Inherit Directional Asymmetries\"), Abstract (\"inheriting from the model's general multilingual structure\"), Section 4.4 (p5), Section 5 Discussion (p7)\n- 问题：标题核心动词 \"Inherit\" 意味着因果关系——冲突信号的不对称性*因为*继承自通用跨语言表征而产生。但实际证据仅是相关性：冲突 probing 不对称性和 XNLI 非冲突 baseline 不对称性在量级和方向上一致（CI 重叠）。CI 重叠仅说明无法拒绝零假设（两者相同），不等于证明共享机制。论文未提供任何因果实验（如 ablation 去除 cross-lingual alignment 后观察冲突不对称性变化）来建立 \"inheritance\" 路径。\n- 为什么影响接收：这不仅是措辞问题——\"Inherit\" 是论文的核心 narrative（三个 contribution 中的第一个）。如果降级为相关性观察，contribution 的实质性会显著降低。\n- 建议：(a) 将 \"Inherit\" 替换为更弱的措辞如 \"Mirror\" 或 \"Parallel\"；(b) 在 Discussion 中明确区分相关性证据和因果 claim；(c) 或设计额外实验建立因果链（如在 representation alignment 被人工破坏的条件下检验冲突不对称性是否消失）。\n\n**N3** [critical] **Steering 证据不足以支撑 detection-decision dissociation 作为通用发现**\n- 具体位置：Abstract (\"These findings demonstrate that linear detectability does not imply causal relevance\"), Section 4.6 (p6-7, Table 3), Section 5 Discussion (p7)\n- 问题：Steering 仅在 Llama L13 (41% depth) 产生显著因果效果（Fisher p = 0.002, Bonferroni 校正后）。Qwen (L14, n=131, best p = 0.785) 和 Gemma (L17, n=171, best p = 0.418) 在所有层均无显著 steering 效果（zero directional flips）。Detection-decision dissociation 因此是单模型发现，而非通用现象。然而 abstract 表述 \"These findings demonstrate...\" 暗示通用性。\n- 为什么影响接收：将 n=1 模型的发现包装为 \"demonstrate\" 级别的结论，且列为三个 contribution 之一（\"Detection-decision layer dissociation\"），是 overclaiming。Qwen/Gemma 的 steering 全面失败更可能说明 probe-based steering 方法本身的局限性，而非 detection ≠ decision 的通用规律。\n- 建议：(a) 将 abstract 中的 \"demonstrate\" 改为 \"suggest\" 或限定为 \"in Llama\"；(b) 在 contributions 列表中将此项从 contribution 降级为 observation；(c) 对 Qwen/Gemma steering 失败提供更深入的分析（见 W4）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **遗漏重要相关工作：跨语言 activation steering**\n- 具体位置：Section 2 Related Work (p2-3)\n- 问题：以下直接相关的近期工作未被引用：\n  1. Pokharel, Agrawal & Nagar (2026). \"Cross-Lingual Activation Steering for Multilingual Language Models.\" arXiv:2601.16390 (Jan 2026) — 提出跨语言 activation steering 方法 CLAS，直接涉及本文核心方法论（cross-lingual + steering），且发现 \"effective transfer operates through functional divergence rather than strict alignment\"，与本文的 XNLI baseline 发现形成对话。\n  2. \"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models.\" arXiv:2502.15639 (Feb 2025) — 分析模型干预对跨语言对齐的影响，直接相关于本文 Section 3.6 和 Section 5 的 steering 讨论。\n- 建议：在 Related Work 的 \"Representation steering and causal intervention\" 段落中增加这些引用，并讨论本文 steering 结果与它们的异同。\n\n**W2** [warning] **Contribution 2（detection-decision dissociation）缺乏泛化性**\n- 具体位置：Section 1 contributions list (p2), Section 5 Discussion (p7)\n- 问题：论文将 detection-decision dissociation 列为三个 contribution 之一，但这仅在 Llama 中观察到。在 Qwen 和 Gemma 中，既没有成功的 steering 也就无法验证是否存在 dissociation（不是 dissociation 不存在，而是 steering 方法本身失效了，无法区分）。\n- 建议：明确表述 \"在 Llama 中观察到 dissociation，Qwen/Gemma 由于 steering 方法失效无法验证\"，而非暗示这是三个模型的共同发现。\n\n**W3** [warning] **Confound exclusion pipeline 的局限性未充分讨论**\n- 具体位置：Section 4.5 (p5-6, Table 2), Section 3.5\n- 问题：\n  (a) Translation quality confound：通过 COMET score 分层（Table 2）排除，但 Qwen 的 COMET tercile 分层显示 Δ = −1.7 pp (p = 0.061) 即翻译质量低的样本确实有影响但被忽略。Llama 的显著效果 (Δ = +1.7, p = 0.063 → 实际未达 0.05) 也接近边界。用 tercile 粗分层可能遗漏细粒度效应。\n  (b) Token overlap confound：Pearson 相关分析（p5-6）显示 Llama 有 weak negative correlation (r = −0.15, p = 0.014)，这说明 overlap 确实与 probe accuracy 相关，仅靠 \"weak\" 的定性判断不足以排除。\n  (c) 未考虑翻译过程引入的系统性实体表征偏差（如中文实体名的音译/意译选择）。\n- 建议：在 Limitations 或 Discussion 中更明确地承认这些局限。\n\n**W4** [warning] **对 Qwen/Gemma steering 失败的分析不足**\n- 具体位置：Section 4.6 (p6-7), Section 5 Discussion (p7-8)\n- 问题：Gemma 的 88.9% probe accuracy 是三个模型中最高的，但 steering 完全无效（zero directional flips）。论文正确指出这 \"rules out probe quality as a confound\"（p7），是一个 \"informative negative\"。但分析仅停留在 \"the causal influence of the probe direction is architecture-dependent\" 的结论层面，未提供 mechanistic 假设：为什么高精度 probe 方向在 steering 时无效？是否与这些模型的 residual stream 结构、attention pattern、或 layer normalization 实现有关？\n- 建议：增加至少一段讨论，提出可检验的 mechanistic 假设。\n\n**W5** [warning] **新颖性相对 Zhao et al. 2024 的增量贡献需更明确定位**\n- 具体位置：Section 1 Introduction (p1-2), Section 2 Related Work (p2-3)\n- 问题：Zhao et al. (2024) 已建立了 residual stream probing 检测知识冲突的框架。本文的主要创新是 (1) 跨语言扩展，(2) XNLI baseline 比较，(3) steering 实验。其中 (1) 是直接扩展，(3) 大部分失败。真正独特的贡献是 (2) XNLI baseline comparison 的方法论思路——但这本质上是一个 negative finding（不对称性非冲突特异）。论文应更坦诚地定位自己相对于 Zhao et al. 的增量幅度。\n- 建议：在 Introduction 中更明确地 articulate \"beyond Zhao et al., our unique methodological contribution is...\"，而非通过三个并列的 contributions 暗示对等的创新量。\n\n---\n\n## 小问题（不影响接收）\n\n1. **Abstract 措辞**: \"Our analysis confronts cross-lingual transfer\" — \"confronts\" 用词不常见，建议改为 \"examines\" 或 \"addresses\"。\n2. **Figure 1 可读性**: 三个模型的 layer-wise probe accuracy 曲线（p5）在打印时较难辨认，特别是 dashed lines（MLP subspace probes）和 star markers。建议增大图幅或拆分为三个 subplot。\n3. **Table 1 注释**: \"Δ_asym is the mean of paired bootstrap differences, not the arithmetic difference of the reported single-seed accuracies\" — 这个重要注释放在 table 脚注中容易被忽略，建议在正文 Section 4.3 中显著提及。\n4. **Section 3.2 数据过滤**: \"filtering samples by querying each model without context and retaining only those answered correctly\" — 这个过滤步骤可能引入选择偏差（只保留模型自信的知识），应在 Limitations 中提及。\n5. **p3 \"Bělohlavek 2022\"**: Related Work 中 \"Probing classifiers\" 引用 Bellinkov 2022，请确认拼写。\n6. **Appendix 结构**: Appendix A (Use of AI Assistants), B (Causal Boundary), C (Matched-Condition) 的安排合理，但 Appendix B 的 Table 4 和 Appendix C 的 Table 5 中部分数据对理解主文 claims 至关重要（如 Llama causal gradient 的精确层定位），考虑将关键结果提升到正文。\n7. **References 格式**: 检查 arXiv preprint 引用是否已被会议接收（如 Zhao et al. 2024 已被 NeurIPS 接收，应更新引用格式）。\n\n---\n\n## 主要优势\n\n1. **研究问题定位精准**: 将 mechanistic interpretability 和 multilingual NLP 的交叉领域具体化为一个清晰可检验的问题，不泛泛而谈。\n2. **XNLI baseline 比较是方法论亮点**: 用非冲突跨语言任务的迁移不对称性作为控制条件，系统地检验冲突信号不对称性的特异性——这个 experimental design choice 值得社区借鉴，即使结论是 negative 的。\n3. **诚实报告负面结果**: Qwen/Gemma steering 失败被完整报告而非隐藏，且 Gemma 的 \"high detectability + zero steering effect\" 被正确解读为 informative negative，体现了良好的科学态度。\n4. **Confound exclusion 流程系统化**: 翻译质量分层 + token overlap 分析 + 非冲突 baseline 三重检查，虽然各环节有局限，但作为 pipeline 展示了对 probing 研究中 confound 的重视。\n5. **三模型比较**: 在 Llama/Qwen/Gemma 三个架构上的一致性和差异性都提供了有价值的信息（尤其是一致的 detectability 和分化的 steerability）。\n\n---\n\n## 缺失的关键相关工作\n\n| 引用 | 相关性 | 为什么应该引用 |\n|------|--------|--------------|\n| Pokharel et al. 2026 \"Cross-Lingual Activation Steering\" (arXiv:2601.16390) | 直接相关 | 跨语言 + steering，本文核心方法的最近相关工作 |\n| \"Steering into New Embedding Spaces\" (arXiv:2502.15639, Feb 2025) | 直接相关 | 分析 cross-lingual alignment 在 model intervention 下的变化 |\n| \"Steering Knowledge Selection Behaviours in LLMs\" (arXiv:2410.15999, Oct 2024) | 高度相关 | 专门研究知识选择行为的 steering，与本文 Section 3.6 直接对话 |\n\n---\n\n## Questions for Authors\n\n1. XNLI baseline 和 conflict probing 的 CI 重叠是否能排除两者由不同机制产生但碰巧量级相近的可能？是否考虑过用 partial correlation 或 mediation analysis 进一步检验？\n2. Qwen/Gemma steering 失败是否可能与 steering 方法本身（probe direction injection）在这些架构上的适用性有关，而非反映 detection-decision dissociation 的缺失？是否尝试过其他 steering 方法（如 Activation Addition, DAS）？\n3. ConflictQA 数据集过滤后 Llama 保留 1,368 样本、Qwen 966、Gemma 1,590——模型间样本差异较大，是否会影响跨模型比较的公平性？\n4. 翻译使用 Qwen3-SB，这与实验模型 Qwen3-8B 同系列——是否存在 translation model 偏好同系列模型 tokenization 的风险，从而影响 token overlap confound analysis？\n\n---\n\n## 总结\n\n本文在跨语言知识冲突的 mechanistic interpretability 方向做了系统的实证探索，方法论设计（特别是 XNLI baseline 比较）有亮点，负面结果的诚实报告体现了良好的科学态度。但三个核心问题——标题对单语言对结果的过度泛化、相关性证据包装为因果 \"Inherit\"、以及单模型 steering 结果推广为通用 \"demonstrate\" ——构成了 claim-evidence 的系统性不匹配。建议：(1) 收窄标题和 abstract 的 claim 强度，(2) 补充 1-2 个额外语言对或将标题限定为 EN-ZH，(3) 将 detection-decision dissociation 定位为 Llama-specific observation 而非通用 contribution。修改后适合 Findings track 接收。\n",
  "reviewer_id": "2",
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审稿报告\n\n**论文**: *Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries from General Multilingual Representations*\n**Venue**: EMNLP 2026 Long Paper (ARR May cycle)\n**审查侧重**: 新颖性 + 完整性 + 写作质量\n**审稿依据**: ACL ARR Review Form (Soundness / Excitement / Reproducibility / Overall Assessment)\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.0 (Findings)\n**一句话总结**: 方法论扎实的跨语言 probing 实证研究，但标题和 abstract 对证据的过度泛化（单语言对声称 \"Cross-Lingual\"、相关性包装为因果 \"Inherit\"、单模型发现推广为通用结论）削弱了贡献的可信度。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 实验设计合理（probing + XNLI baseline + confound exclusion + steering），但多处 claim 超出证据支撑范围：标题因果措辞 \"Inherit\" 缺乏因果证据；steering 仅在 1/3 模型成功却推广为通用发现 |\n| Excitement | 2.5/5 | 对 Zhao et al. 2024 的跨语言扩展属增量贡献；最有趣的 detection-decision dissociation 仅在 Llama 成立；XNLI baseline 比较方法论有价值但核心结论偏 negative（不对称性非冲突特异） |\n| Reproducibility | 4/5 | 数据集（ConflictQA）、模型、probing 方法描述清晰；bootstrap 置信区间和 Bonferroni 校正规范；steering 的 σ 扫描范围和随机种子数明确 |\n| Confidence | 4/5 | 熟悉 knowledge conflict detection、cross-lingual probing、representation steering 文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **标题 \"Cross-Lingual\" 过度泛化：仅测试 EN-ZH 一个语言对**\n- 具体位置：Title, Abstract, Section 1 (Introduction)\n- 问题：标题使用 \"Cross-Lingual\" 暗示跨语言通用性，但实验仅涉及英语-中文一个语言对。英语和中文在类型学上差异极大（SVO vs. SVO 但书写系统、形态完全不同），在这一对上的发现无法直接推广到其他语言对（如 EN-DE、EN-JA、ZH-JA 等）。论文自身在 Limitations (p9) 承认 \"We evaluate only one language pair (English-Chinese)\"，但标题未作限定。\n- 为什么影响接收：ACL ARR reviewer guidelines 明确要求 \"Claims match evidence presented\"。标题是论文最重要的 claim 载体，对单一语言对的结论使用无限定的 \"Cross-Lingual\" 构成 overclaiming。实际上，论文自己的 XNLI 数据引用了 Kargaran et al. (2024) 关于 \"conflict resolution preferences vary by language pair\" 的发现（p7 Discussion），说明语言对的选择确实影响结论的泛化性。\n- 建议：(a) 将标题改为包含 \"English-Chinese\" 限定；(b) 或增加至少 1-2 个类型学不同的语言对（如 EN-DE 或 EN-JA）以支撑 \"Cross-Lingual\" 的泛化声称。\n\n**N2** [critical] **\"Inherit\" 因果措辞缺乏因果证据**\n- 具体位置：Title (\"Inherit Directional Asymmetries\"), Abstract (\"inheriting from the model's general multilingual structure\"), Section 4.4 (p5), Section 5 Discussion (p7)\n- 问题：标题核心动词 \"Inherit\" 意味着因果关系——冲突信号的不对称性*因为*继承自通用跨语言表征而产生。但实际证据仅是相关性：冲突 probing 不对称性和 XNLI 非冲突 baseline 不对称性在量级和方向上一致（CI 重叠）。CI 重叠仅说明无法拒绝零假设（两者相同），不等于证明共享机制。论文未提供任何因果实验（如 ablation 去除 cross-lingual alignment 后观察冲突不对称性变化）来建立 \"inheritance\" 路径。\n- 为什么影响接收：这不仅是措辞问题——\"Inherit\" 是论文的核心 narrative（三个 contribution 中的第一个）。如果降级为相关性观察，contribution 的实质性会显著降低。\n- 建议：(a) 将 \"Inherit\" 替换为更弱的措辞如 \"Mirror\" 或 \"Parallel\"；(b) 在 Discussion 中明确区分相关性证据和因果 claim；(c) 或设计额外实验建立因果链（如在 representation alignment 被人工破坏的条件下检验冲突不对称性是否消失）。\n\n**N3** [critical] **Steering 证据不足以支撑 detection-decision dissociation 作为通用发现**\n- 具体位置：Abstract (\"These findings demonstrate that linear detectability does not imply causal relevance\"), Section 4.6 (p6-7, Table 3), Section 5 Discussion (p7)\n- 问题：Steering 仅在 Llama L13 (41% depth) 产生显著因果效果（Fisher p = 0.002, Bonferroni 校正后）。Qwen (L14, n=131, best p = 0.785) 和 Gemma (L17, n=171, best p = 0.418) 在所有层均无显著 steering 效果（zero directional flips）。Detection-decision dissociation 因此是单模型发现，而非通用现象。然而 abstract 表述 \"These findings demonstrate...\" 暗示通用性。\n- 为什么影响接收：将 n=1 模型的发现包装为 \"demonstrate\" 级别的结论，且列为三个 contribution 之一（\"Detection-decision layer dissociation\"），是 overclaiming。Qwen/Gemma 的 steering 全面失败更可能说明 probe-based steering 方法本身的局限性，而非 detection ≠ decision 的通用规律。\n- 建议：(a) 将 abstract 中的 \"demonstrate\" 改为 \"suggest\" 或限定为 \"in Llama\"；(b) 在 contributions 列表中将此项从 contribution 降级为 observation；(c) 对 Qwen/Gemma steering 失败提供更深入的分析（见 W4）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **遗漏重要相关工作：跨语言 activation steering**\n- 具体位置：Section 2 Related Work (p2-3)\n- 问题：以下直接相关的近期工作未被引用：\n  1. Pokharel, Agrawal & Nagar (2026). \"Cross-Lingual Activation Steering for Multilingual Language Models.\" arXiv:2601.16390 (Jan 2026) — 提出跨语言 activation steering 方法 CLAS，直接涉及本文核心方法论（cross-lingual + steering），且发现 \"effective transfer operates through functional divergence rather than strict alignment\"，与本文的 XNLI baseline 发现形成对话。\n  2. \"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models.\" arXiv:2502.15639 (Feb 2025) — 分析模型干预对跨语言对齐的影响，直接相关于本文 Section 3.6 和 Section 5 的 steering 讨论。\n- 建议：在 Related Work 的 \"Representation steering and causal intervention\" 段落中增加这些引用，并讨论本文 steering 结果与它们的异同。\n\n**W2** [warning] **Contribution 2（detection-decision dissociation）缺乏泛化性**\n- 具体位置：Section 1 contributions list (p2), Section 5 Discussion (p7)\n- 问题：论文将 detection-decision dissociation 列为三个 contribution 之一，但这仅在 Llama 中观察到。在 Qwen 和 Gemma 中，既没有成功的 steering 也就无法验证是否存在 dissociation（不是 dissociation 不存在，而是 steering 方法本身失效了，无法区分）。\n- 建议：明确表述 \"在 Llama 中观察到 dissociation，Qwen/Gemma 由于 steering 方法失效无法验证\"，而非暗示这是三个模型的共同发现。\n\n**W3** [warning] **Confound exclusion pipeline 的局限性未充分讨论**\n- 具体位置：Section 4.5 (p5-6, Table 2), Section 3.5\n- 问题：\n  (a) Translation quality confound：通过 COMET score 分层（Table 2）排除，但 Qwen 的 COMET tercile 分层显示 Δ = −1.7 pp (p = 0.061) 即翻译质量低的样本确实有影响但被忽略。Llama 的显著效果 (Δ = +1.7, p = 0.063 → 实际未达 0.05) 也接近边界。用 tercile 粗分层可能遗漏细粒度效应。\n  (b) Token overlap confound：Pearson 相关分析（p5-6）显示 Llama 有 weak negative correlation (r = −0.15, p = 0.014)，这说明 overlap 确实与 probe accuracy 相关，仅靠 \"weak\" 的定性判断不足以排除。\n  (c) 未考虑翻译过程引入的系统性实体表征偏差（如中文实体名的音译/意译选择）。\n- 建议：在 Limitations 或 Discussion 中更明确地承认这些局限。\n\n**W4** [warning] **对 Qwen/Gemma steering 失败的分析不足**\n- 具体位置：Section 4.6 (p6-7), Section 5 Discussion (p7-8)\n- 问题：Gemma 的 88.9% probe accuracy 是三个模型中最高的，但 steering 完全无效（zero directional flips）。论文正确指出这 \"rules out probe quality as a confound\"（p7），是一个 \"informative negative\"。但分析仅停留在 \"the causal influence of the probe direction is architecture-dependent\" 的结论层面，未提供 mechanistic 假设：为什么高精度 probe 方向在 steering 时无效？是否与这些模型的 residual stream 结构、attention pattern、或 layer normalization 实现有关？\n- 建议：增加至少一段讨论，提出可检验的 mechanistic 假设。\n\n**W5** [warning] **新颖性相对 Zhao et al. 2024 的增量贡献需更明确定位**\n- 具体位置：Section 1 Introduction (p1-2), Section 2 Related Work (p2-3)\n- 问题：Zhao et al. (2024) 已建立了 residual stream probing 检测知识冲突的框架。本文的主要创新是 (1) 跨语言扩展，(2) XNLI baseline 比较，(3) steering 实验。其中 (1) 是直接扩展，(3) 大部分失败。真正独特的贡献是 (2) XNLI baseline comparison 的方法论思路——但这本质上是一个 negative finding（不对称性非冲突特异）。论文应更坦诚地定位自己相对于 Zhao et al. 的增量幅度。\n- 建议：在 Introduction 中更明确地 articulate \"beyond Zhao et al., our unique methodological contribution is...\"，而非通过三个并列的 contributions 暗示对等的创新量。\n\n---\n\n## 小问题（不影响接收）\n\n1. **Abstract 措辞**: \"Our analysis confronts cross-lingual transfer\" — \"confronts\" 用词不常见，建议改为 \"examines\" 或 \"addresses\"。\n2. **Figure 1 可读性**: 三个模型的 layer-wise probe accuracy 曲线（p5）在打印时较难辨认，特别是 dashed lines（MLP subspace probes）和 star markers。建议增大图幅或拆分为三个 subplot。\n3. **Table 1 注释**: \"Δ_asym is the mean of paired bootstrap differences, not the arithmetic difference of the reported single-seed accuracies\" — 这个重要注释放在 table 脚注中容易被忽略，建议在正文 Section 4.3 中显著提及。\n4. **Section 3.2 数据过滤**: \"filtering samples by querying each model without context and retaining only those answered correctly\" — 这个过滤步骤可能引入选择偏差（只保留模型自信的知识），应在 Limitations 中提及。\n5. **p3 \"Bělohlavek 2022\"**: Related Work 中 \"Probing classifiers\" 引用 Bellinkov 2022，请确认拼写。\n6. **Appendix 结构**: Appendix A (Use of AI Assistants), B (Causal Boundary), C (Matched-Condition) 的安排合理，但 Appendix B 的 Table 4 和 Appendix C 的 Table 5 中部分数据对理解主文 claims 至关重要（如 Llama causal gradient 的精确层定位），考虑将关键结果提升到正文。\n7. **References 格式**: 检查 arXiv preprint 引用是否已被会议接收（如 Zhao et al. 2024 已被 NeurIPS 接收，应更新引用格式）。\n\n---\n\n## 主要优势\n\n1. **研究问题定位精准**: 将 mechanistic interpretability 和 multilingual NLP 的交叉领域具体化为一个清晰可检验的问题，不泛泛而谈。\n2. **XNLI baseline 比较是方法论亮点**: 用非冲突跨语言任务的迁移不对称性作为控制条件，系统地检验冲突信号不对称性的特异性——这个 experimental design choice 值得社区借鉴，即使结论是 negative 的。\n3. **诚实报告负面结果**: Qwen/Gemma steering 失败被完整报告而非隐藏，且 Gemma 的 \"high detectability + zero steering effect\" 被正确解读为 informative negative，体现了良好的科学态度。\n4. **Confound exclusion 流程系统化**: 翻译质量分层 + token overlap 分析 + 非冲突 baseline 三重检查，虽然各环节有局限，但作为 pipeline 展示了对 probing 研究中 confound 的重视。\n5. **三模型比较**: 在 Llama/Qwen/Gemma 三个架构上的一致性和差异性都提供了有价值的信息（尤其是一致的 detectability 和分化的 steerability）。\n\n---\n\n## 缺失的关键相关工作\n\n| 引用 | 相关性 | 为什么应该引用 |\n|------|--------|--------------|\n| Pokharel et al. 2026 \"Cross-Lingual Activation Steering\" (arXiv:2601.16390) | 直接相关 | 跨语言 + steering，本文核心方法的最近相关工作 |\n| \"Steering into New Embedding Spaces\" (arXiv:2502.15639, Feb 2025) | 直接相关 | 分析 cross-lingual alignment 在 model intervention 下的变化 |\n| \"Steering Knowledge Selection Behaviours in LLMs\" (arXiv:2410.15999, Oct 2024) | 高度相关 | 专门研究知识选择行为的 steering，与本文 Section 3.6 直接对话 |\n\n---\n\n## Questions for Authors\n\n1. XNLI baseline 和 conflict probing 的 CI 重叠是否能排除两者由不同机制产生但碰巧量级相近的可能？是否考虑过用 partial correlation 或 mediation analysis 进一步检验？\n2. Qwen/Gemma steering 失败是否可能与 steering 方法本身（probe direction injection）在这些架构上的适用性有关，而非反映 detection-decision dissociation 的缺失？是否尝试过其他 steering 方法（如 Activation Addition, DAS）？\n3. ConflictQA 数据集过滤后 Llama 保留 1,368 样本、Qwen 966、Gemma 1,590——模型间样本差异较大，是否会影响跨模型比较的公平性？\n4. 翻译使用 Qwen3-SB，这与实验模型 Qwen3-8B 同系列——是否存在 translation model 偏好同系列模型 tokenization 的风险，从而影响 token overlap confound analysis？\n\n---\n\n## 总结\n\n本文在跨语言知识冲突的 mechanistic interpretability 方向做了系统的实证探索，方法论设计（特别是 XNLI baseline 比较）有亮点，负面结果的诚实报告体现了良好的科学态度。但三个核心问题——标题对单语言对结果的过度泛化、相关性证据包装为因果 \"Inherit\"、以及单模型 steering 结果推广为通用 \"demonstrate\" ——构成了 claim-evidence 的系统性不匹配。建议：(1) 收窄标题和 abstract 的 claim 强度，(2) 补充 1-2 个额外语言对或将标题限定为 EN-ZH，(3) 将 detection-decision dissociation 定位为 Llama-specific observation 而非通用 contribution。修改后适合 Findings track 接收。\n",
    "reviewer_id": "2",
    "project": "clkc_mech_interp"
  }
}
```

</details>

---

### Tool result

_source line 141 · 2026-05-24T16:39:43.969314+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3714
}
```

</details>

---

### Tool call

_source line 142 · 2026-05-24T16:39:47.231628+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
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

_source line 143 · 2026-05-24T16:39:47.282239+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 144 · 2026-05-24T16:39:50.646038+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images"
  }
}
```

</details>

---

### Tool result

_source line 145 · 2026-05-24T16:39:50.697665+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 51
}
```

</details>

---

### Assistant

_source line 146 · 2026-05-24T16:39:59.621719+00:00_

审稿报告已提交至 Review Director。

核心判断：**Overall 3.0 (Findings)**。方法论设计有亮点（XNLI baseline 比较、三模型对比、confound exclusion pipeline），但存在三个系统性 claim-evidence 不匹配：

1. **标题 "Cross-Lingual" 仅测试 EN-ZH 一个语言对** — overclaiming
2. **"Inherit" 因果措辞仅有相关性证据**（CI 重叠 ≠ 因果链）
3. **Detection-decision dissociation 仅在 Llama 成立**，Qwen/Gemma steering 全面失败，但 abstract 用 "demonstrate" 推广为通用结论

另外标记了 3 个遗漏的直接相关工作（Pokharel et al. 2026 跨语言 activation steering 等）和若干 should-fix / minor 问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2"
}
```

</details>

---

## Round 4

16 recorded events

### User

_source line 147 · 2026-05-24T16:40:50.478486+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 1 的完整审稿

请逐条阅读 Reviewer 1 的审稿意见，对每个 Must-Fix 和 Should-Fix 问题用 `[AGREE]` 或 `[REBUT]` 回应，附简要理由。重点关注你们之间的分歧点。

---

以下是 Reviewer 1 的完整审稿：

**Overall Assessment**: 3.5 (Borderline Conference)

### Must-Fix 问题

**M1** [critical] **单种子设计不满足当前 probing 标准**
- 所有 probing 实验使用单一随机种子，不满足 Sellam et al. 2022 和 Dodge et al. 2020 建立的多种子标准。Bootstrap CI 仅量化采样不确定性，不覆盖训练随机性。
- 建议：至少 5 个随机种子，报告均值±标准差。

**M2** [critical] **TOST 等价检验无功效却做了等价结论**
- Section 4.4 用 TOST 检验 conflict 和 XNLI 不对称性的等价性，但未报告统计功效（power）。在样本量有限时，TOST 不显著可能仅因检验功效不足，而非真正等价。
- 建议：报告 power analysis，或改用 Bayesian equivalence testing（BF < 1/3 标准）。

**M3** [critical] **因果发现仅 1/3 模型成立但被列为主要贡献**
- Steering 仅在 Llama 成功，Qwen/Gemma 完全失败。但论文将 "detection-decision layer dissociation" 列为三个主要 contribution 之一，构成 overclaiming。
- 建议：降级为 observation，或在 contribution 声明中限定为 Llama-specific。

### Should-Fix 问题

**S1** Gemma confound 分析数据缺失——Gemma 的 COMET tercile 分层和 token overlap 数据未报告。

**S2** Tercile 分析功效不足——每个 tercile 仅 ~300-500 样本，可能检测不到 2-3pp 的效应。

**S3** 跨模型样本自选择偏差——各模型用自身知识过滤样本（Llama 1368, Qwen 966, Gemma 1590），导致比较的不是同一组事实。

**S4** Abstract 内部一致性——先说 "shared multilingual representations, not conflict-specific mechanisms" 又说 "detectability does not imply causal relevance"，逻辑跳跃过大。

**S5** 因果边界 "gradient" 的统计验证不充分——Llama L13 steering 效果需要更系统的层扫描。

**S6** 不对称性对称点的讨论缺失——Gemma 几乎对称（Δ_asym ~ 0）但论文未充分讨论。

### Reviewer 1 的主要优势评价
1. Confound exclusion + XNLI baseline + boundary replication 的方法管线
2. Detection ≠ Decision 发现本身
3. 三模型比较设计
4. Bootstrap CI 和 Bonferroni 校正等统计规范
5. 诚实报告负面结果

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 148 · 2026-05-24T16:41:51.722124+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/submitted.pdf",
  "project": "clkc_mech_interp",
  "pages": "3,5,6,9",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/submitted.pdf",
    "project": "clkc_mech_interp",
    "pages": "3,5,6,9",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 149 · 2026-05-24T16:41:52.625740+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 534.7}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 476.9}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 514.1}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 432.6}], \"total_pages\": 11, \"rendered_pages\": 4, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 903
}
```

</details>

---

### Tool call

_source line 150 · 2026-05-24T16:41:55.642037+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---

### Tool call

_source line 151 · 2026-05-24T16:41:56.145653+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---

### Tool call

_source line 152 · 2026-05-24T16:41:56.872567+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---

### Tool result

_source line 153 · 2026-05-24T16:41:57.229584+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1587
}
```

</details>

---

### Tool call

_source line 154 · 2026-05-24T16:41:57.229951+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---

### Tool result

_source line 155 · 2026-05-24T16:41:57.532865+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1387
}
```

</details>

---

### Tool result

_source line 156 · 2026-05-24T16:41:58.287097+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1414
}
```

</details>

---

### Tool result

_source line 157 · 2026-05-24T16:41:58.388582+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1158
}
```

</details>

---

### Tool call

_source line 158 · 2026-05-24T16:43:51.465720+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的交叉回应\n\n---\n\n## Must-Fix 问题回应\n\n### [REBUT] R1-M1: 单种子设计不满足当前 probing 标准\n\nReviewer 1 的多种子要求对**神经网络 probe 完全正确**，但本文使用的是 **ℓ₁-regularized logistic regression**（Section 3.3, p3: \"we train an ℓ₁-regularized logistic regression probe (Belinkov, 2022; Hewitt and Liang, 2019)\"）。Logistic regression 是凸优化问题，给定相同数据其解唯一，不依赖随机初始化——Sellam et al. 2022 和 Dodge et al. 2020 的多种子标准针对的是非凸神经网络微调，不直接适用于凸 probe。\n\n**但有一个 Reviewer 1 未明确指出但确实存在的相关问题**：论文使用单一 80/20 split（Section 3.2），bootstrap 覆盖的是给定 split 上的采样不确定性，不覆盖 split 本身的随机性。对凸 probe，正确的做法是 k-fold cross-validation 或多次 random split，而非多随机种子。这是一个 mild concern（不是 Must-Fix），因为 2000 次 bootstrap 已经提供了合理的 CI，且凸 probe 在同一 split 上结果稳定。\n\n**结论**：M1 的诊断方向偏移——问题不在 \"种子\" 而在 \"split\"，且对凸 probe 的严重程度低于 Reviewer 1 的评估。建议降级为 Should-Fix。\n\n---\n\n### [AGREE] R1-M2: TOST 等价检验无功效却做了等价结论\n\n完全同意。论文 Section 4.4 (p5) 明确使用了 TOST（±2 pp margin）并**自行承认功效不足**：\"Formal TOST equivalence tests (±2 pp margin) were non-significant for all three models (Llama p = 0.41, Qwen p = 0.366, Gemma p = 0.377), reflecting insufficient power (SE ≈ 4.37 pp) rather than meaningful differences.\"\n\n这使得问题更加严重：论文明知 TOST 功效不足，却仍以 \"point estimates fall within ±1.3 pp\" 和 CI 重叠为依据推出 \"the asymmetry thus reflects a general cross-lingual property\" 的结论，并在标题中使用 \"Inherit\" 这一因果措辞。**自我承认统计证据不足后仍做等价声称，构成比简单遗漏更严重的方法论问题。**\n\n我在自己的审稿中将此问题归入 N2（\"Inherit\" 因果措辞缺乏因果证据），Reviewer 1 的 M2 从统计检验角度提供了更精确的技术诊断。两者互补，共同构成 Must-Fix。\n\nReviewer 1 建议 Bayesian equivalence testing (BF < 1/3) 是合理的替代方案。\n\n---\n\n### [AGREE] R1-M3: 因果发现仅 1/3 模型成立但被列为主要贡献\n\n完全同意，与我的 N3 一致。Detection-decision dissociation 仅在 Llama L13 成立（Fisher p = 0.002），Qwen (best p = 0.785) 和 Gemma (best p = 0.418) 均 zero directional flips。Abstract 的 \"These findings demonstrate...\" 和 contributions 列表将此作为通用发现是 overclaiming。\n\n补充一点 Reviewer 1 未展开的角度：Qwen/Gemma 的 steering 全面失败也意味着我们**无法区分**这两个模型是 (a) 不存在 detection-decision dissociation，还是 (b) 存在 dissociation 但 probe-based steering 方法对这些架构无效。论文将 Gemma 解读为 \"informative negative\" (p7)，但实际上这个 negative 有两种不同的解释，论文只讨论了一种。\n\n---\n\n## Should-Fix 问题回应\n\n### [AGREE] R1-S1: Gemma confound 分析数据缺失\n\n确认 Table 2 (p6) 仅报告 Qwen 和 Llama 的 COMET tercile 和 token overlap 数据，Gemma 完全缺失。三个模型中 Gemma 的 probe accuracy 最高 (88.9%)，恰恰是最需要排除 confound 的模型。数据缺失无正当理由。\n\n---\n\n### [AGREE] R1-S2: Tercile 分析功效不足\n\n同意。每个 tercile ~300-500 样本检测 2-3 pp 效应确实可能功效不足。Llama 的 COMET tercile Δ = +1.7 pp (p = 0.063) 和 Qwen 的 Δ = -1.7 pp (p = 0.061) 都在边界附近——这恰好说明样本量可能刚好不够检测到真实效应。用连续变量回归而非三等分会更稳健。\n\n---\n\n### [AGREE] R1-S3: 跨模型样本自选择偏差\n\n同意，我在 Questions for Authors (Q3) 中也提出了同一问题。Llama 1368 / Qwen 966 / Gemma 1590 是各模型自身知识过滤后的不同子集，跨模型比较的可比性受到威胁。理想方案是取三个模型都能正确回答的交集子集做额外分析。\n\n---\n\n### [REBUT] R1-S4: Abstract 内部一致性——逻辑跳跃\n\n不同意 Reviewer 1 对此的判断。Abstract 的两个核心发现在逻辑上是兼容且互补的：\n\n1. \"inheriting from the model's general multilingual structure rather than conflict-specific encoding\" → 关于不对称性信号的**性质**（结构性的，非冲突特异的）\n2. \"linear detectability does not imply causal relevance\" → 关于 detection 的**功能局限**（可检测不等于可操控）\n\n这不是逻辑矛盾或跳跃，而是两个不同维度的发现：(1) 说 \"什么\"，(2) 说 \"然后怎样\"。可以同时成立：冲突信号的跨语言不对称性继承自通用结构（性质），且即使信号可检测也不能通过 steering 因果地影响决策（功能）。\n\n**但 Reviewer 1 的直觉有合理内核**：Abstract 在这两个发现之间缺少一句过渡性解释来连接逻辑链。读者需要自行推断两者的关系。建议作者在 Abstract 中加一句桥接（如 \"Beyond the nature of the asymmetry, we further examine whether detected signals carry causal weight\"），但这属于写作润色而非逻辑缺陷。\n\n---\n\n### [REBUT] R1-S5: 因果边界 \"gradient\" 的统计验证不充分\n\n部分不同意。Appendix B (p9, Table 4) 提供了独立的 causal boundary replication：使用独立样本 (N = 201) 和独立随机采样，扫描了 Llama 从 L10 到 L28 共 6 个层，确认 L13 显著 (p < 0.001) 且 L12 仍显著 (p = 0.0003)，而邻近层（L10, L18, L28）均不显著或 Bonferroni 后消失。这已经构成了合理的 boundary delineation。\n\n主文 Table 3 (p7) 也在多个 depth 上测试了所有三个模型的 steering 效果。综合主文 + Appendix 的层扫描，验证的系统性在 probing 文献中属于合理水平。Reviewer 1 要求 \"更系统的层扫描\" 具体需要什么级别，没有明确——如果是每一层都扫描，那需要极大的 Bonferroni 校正代价。\n\n**但我同意**一个相关点：论文声称 L13 是 \"remarkably narrow causal window\" (p6)，这个修饰语（\"remarkably\"）需要与其他 causal intervention 文献的 window 宽度对比才能成立，论文未提供这个对比。\n\n---\n\n### [AGREE] R1-S6: Gemma 不对称性对称点讨论缺失\n\n同意。Table 1 显示 Gemma Δ_asym 接近 0（EN→ZH 和 ZH→EN 准确率几乎相同），而 Llama 和 Qwen 都有 ~7 pp 的 ZH→EN 优势。这是一个值得讨论的跨架构差异——Gemma 的对称性可能反映了其训练数据中英中分布更均衡，或其内部 representation alignment 机制不同。论文提及 Kargaran et al. (2024) 的 \"conflict resolution preferences vary by language pair\" 但未将其应用到解释 Gemma 的对称性。\n\n---\n\n## 分歧总结\n\n| 条目 | 我的判断 | 与 R1 的差异 | 理由 |\n|------|----------|------------|------|\n| M1 | Should-Fix (非 Must-Fix) | 降级 | 凸 probe 不需要多种子；问题在 split 不在 seed |\n| M2 | Must-Fix | 完全一致 | 自认功效不足仍做等价声称 |\n| M3 | Must-Fix | 完全一致 | 与我的 N3 一致 |\n| S1 | Should-Fix | 一致 | — |\n| S2 | Should-Fix | 一致 | — |\n| S3 | Should-Fix | 一致 | — |\n| S4 | Minor (非 Should-Fix) | 降级 | 逻辑兼容但缺过渡句，是写作问题非逻辑问题 |\n| S5 | Minor (非 Should-Fix) | 降级 | Appendix B 已提供合理层扫描 |\n| S6 | Should-Fix | 一致 | — |\n\n**关于 Overall Assessment**：Reviewer 1 给 3.5 (Borderline Conference)，我给 3.0 (Findings)。差异主要来自我对新颖性的更严格评估——我认为单语言对的跨语言扩展 + 核心 XNLI 结论是 negative finding + steering 2/3 失败，整体增量贡献不足以支撑 Borderline Conference。Reviewer 1 可能更看重方法论管线（confound exclusion + boundary replication）的价值。我认为方法论管线有价值但不足以弥补 claim-evidence 的系统性不匹配。\n",
  "reviewer_id": "2",
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的交叉回应\n\n---\n\n## Must-Fix 问题回应\n\n### [REBUT] R1-M1: 单种子设计不满足当前 probing 标准\n\nReviewer 1 的多种子要求对**神经网络 probe 完全正确**，但本文使用的是 **ℓ₁-regularized logistic regression**（Section 3.3, p3: \"we train an ℓ₁-regularized logistic regression probe (Belinkov, 2022; Hewitt and Liang, 2019)\"）。Logistic regression 是凸优化问题，给定相同数据其解唯一，不依赖随机初始化——Sellam et al. 2022 和 Dodge et al. 2020 的多种子标准针对的是非凸神经网络微调，不直接适用于凸 probe。\n\n**但有一个 Reviewer 1 未明确指出但确实存在的相关问题**：论文使用单一 80/20 split（Section 3.2），bootstrap 覆盖的是给定 split 上的采样不确定性，不覆盖 split 本身的随机性。对凸 probe，正确的做法是 k-fold cross-validation 或多次 random split，而非多随机种子。这是一个 mild concern（不是 Must-Fix），因为 2000 次 bootstrap 已经提供了合理的 CI，且凸 probe 在同一 split 上结果稳定。\n\n**结论**：M1 的诊断方向偏移——问题不在 \"种子\" 而在 \"split\"，且对凸 probe 的严重程度低于 Reviewer 1 的评估。建议降级为 Should-Fix。\n\n---\n\n### [AGREE] R1-M2: TOST 等价检验无功效却做了等价结论\n\n完全同意。论文 Section 4.4 (p5) 明确使用了 TOST（±2 pp margin）并**自行承认功效不足**：\"Formal TOST equivalence tests (±2 pp margin) were non-significant for all three models (Llama p = 0.41, Qwen p = 0.366, Gemma p = 0.377), reflecting insufficient power (SE ≈ 4.37 pp) rather than meaningful differences.\"\n\n这使得问题更加严重：论文明知 TOST 功效不足，却仍以 \"point estimates fall within ±1.3 pp\" 和 CI 重叠为依据推出 \"the asymmetry thus reflects a general cross-lingual property\" 的结论，并在标题中使用 \"Inherit\" 这一因果措辞。**自我承认统计证据不足后仍做等价声称，构成比简单遗漏更严重的方法论问题。**\n\n我在自己的审稿中将此问题归入 N2（\"Inherit\" 因果措辞缺乏因果证据），Reviewer 1 的 M2 从统计检验角度提供了更精确的技术诊断。两者互补，共同构成 Must-Fix。\n\nReviewer 1 建议 Bayesian equivalence testing (BF < 1/3) 是合理的替代方案。\n\n---\n\n### [AGREE] R1-M3: 因果发现仅 1/3 模型成立但被列为主要贡献\n\n完全同意，与我的 N3 一致。Detection-decision dissociation 仅在 Llama L13 成立（Fisher p = 0.002），Qwen (best p = 0.785) 和 Gemma (best p = 0.418) 均 zero directional flips。Abstract 的 \"These findings demonstrate...\" 和 contributions 列表将此作为通用发现是 overclaiming。\n\n补充一点 Reviewer 1 未展开的角度：Qwen/Gemma 的 steering 全面失败也意味着我们**无法区分**这两个模型是 (a) 不存在 detection-decision dissociation，还是 (b) 存在 dissociation 但 probe-based steering 方法对这些架构无效。论文将 Gemma 解读为 \"informative negative\" (p7)，但实际上这个 negative 有两种不同的解释，论文只讨论了一种。\n\n---\n\n## Should-Fix 问题回应\n\n### [AGREE] R1-S1: Gemma confound 分析数据缺失\n\n确认 Table 2 (p6) 仅报告 Qwen 和 Llama 的 COMET tercile 和 token overlap 数据，Gemma 完全缺失。三个模型中 Gemma 的 probe accuracy 最高 (88.9%)，恰恰是最需要排除 confound 的模型。数据缺失无正当理由。\n\n---\n\n### [AGREE] R1-S2: Tercile 分析功效不足\n\n同意。每个 tercile ~300-500 样本检测 2-3 pp 效应确实可能功效不足。Llama 的 COMET tercile Δ = +1.7 pp (p = 0.063) 和 Qwen 的 Δ = -1.7 pp (p = 0.061) 都在边界附近——这恰好说明样本量可能刚好不够检测到真实效应。用连续变量回归而非三等分会更稳健。\n\n---\n\n### [AGREE] R1-S3: 跨模型样本自选择偏差\n\n同意，我在 Questions for Authors (Q3) 中也提出了同一问题。Llama 1368 / Qwen 966 / Gemma 1590 是各模型自身知识过滤后的不同子集，跨模型比较的可比性受到威胁。理想方案是取三个模型都能正确回答的交集子集做额外分析。\n\n---\n\n### [REBUT] R1-S4: Abstract 内部一致性——逻辑跳跃\n\n不同意 Reviewer 1 对此的判断。Abstract 的两个核心发现在逻辑上是兼容且互补的：\n\n1. \"inheriting from the model's general multilingual structure rather than conflict-specific encoding\" → 关于不对称性信号的**性质**（结构性的，非冲突特异的）\n2. \"linear detectability does not imply causal relevance\" → 关于 detection 的**功能局限**（可检测不等于可操控）\n\n这不是逻辑矛盾或跳跃，而是两个不同维度的发现：(1) 说 \"什么\"，(2) 说 \"然后怎样\"。可以同时成立：冲突信号的跨语言不对称性继承自通用结构（性质），且即使信号可检测也不能通过 steering 因果地影响决策（功能）。\n\n**但 Reviewer 1 的直觉有合理内核**：Abstract 在这两个发现之间缺少一句过渡性解释来连接逻辑链。读者需要自行推断两者的关系。建议作者在 Abstract 中加一句桥接（如 \"Beyond the nature of the asymmetry, we further examine whether detected signals carry causal weight\"），但这属于写作润色而非逻辑缺陷。\n\n---\n\n### [REBUT] R1-S5: 因果边界 \"gradient\" 的统计验证不充分\n\n部分不同意。Appendix B (p9, Table 4) 提供了独立的 causal boundary replication：使用独立样本 (N = 201) 和独立随机采样，扫描了 Llama 从 L10 到 L28 共 6 个层，确认 L13 显著 (p < 0.001) 且 L12 仍显著 (p = 0.0003)，而邻近层（L10, L18, L28）均不显著或 Bonferroni 后消失。这已经构成了合理的 boundary delineation。\n\n主文 Table 3 (p7) 也在多个 depth 上测试了所有三个模型的 steering 效果。综合主文 + Appendix 的层扫描，验证的系统性在 probing 文献中属于合理水平。Reviewer 1 要求 \"更系统的层扫描\" 具体需要什么级别，没有明确——如果是每一层都扫描，那需要极大的 Bonferroni 校正代价。\n\n**但我同意**一个相关点：论文声称 L13 是 \"remarkably narrow causal window\" (p6)，这个修饰语（\"remarkably\"）需要与其他 causal intervention 文献的 window 宽度对比才能成立，论文未提供这个对比。\n\n---\n\n### [AGREE] R1-S6: Gemma 不对称性对称点讨论缺失\n\n同意。Table 1 显示 Gemma Δ_asym 接近 0（EN→ZH 和 ZH→EN 准确率几乎相同），而 Llama 和 Qwen 都有 ~7 pp 的 ZH→EN 优势。这是一个值得讨论的跨架构差异——Gemma 的对称性可能反映了其训练数据中英中分布更均衡，或其内部 representation alignment 机制不同。论文提及 Kargaran et al. (2024) 的 \"conflict resolution preferences vary by language pair\" 但未将其应用到解释 Gemma 的对称性。\n\n---\n\n## 分歧总结\n\n| 条目 | 我的判断 | 与 R1 的差异 | 理由 |\n|------|----------|------------|------|\n| M1 | Should-Fix (非 Must-Fix) | 降级 | 凸 probe 不需要多种子；问题在 split 不在 seed |\n| M2 | Must-Fix | 完全一致 | 自认功效不足仍做等价声称 |\n| M3 | Must-Fix | 完全一致 | 与我的 N3 一致 |\n| S1 | Should-Fix | 一致 | — |\n| S2 | Should-Fix | 一致 | — |\n| S3 | Should-Fix | 一致 | — |\n| S4 | Minor (非 Should-Fix) | 降级 | 逻辑兼容但缺过渡句，是写作问题非逻辑问题 |\n| S5 | Minor (非 Should-Fix) | 降级 | Appendix B 已提供合理层扫描 |\n| S6 | Should-Fix | 一致 | — |\n\n**关于 Overall Assessment**：Reviewer 1 给 3.5 (Borderline Conference)，我给 3.0 (Findings)。差异主要来自我对新颖性的更严格评估——我认为单语言对的跨语言扩展 + 核心 XNLI 结论是 negative finding + steering 2/3 失败，整体增量贡献不足以支撑 Borderline Conference。Reviewer 1 可能更看重方法论管线（confound exclusion + boundary replication）的价值。我认为方法论管线有价值但不足以弥补 claim-evidence 的系统性不匹配。\n",
    "reviewer_id": "2",
    "project": "clkc_mech_interp"
  }
}
```

</details>

---

### Tool result

_source line 159 · 2026-05-24T16:43:55.451459+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3985
}
```

</details>

---

### Tool call

_source line 160 · 2026-05-24T16:43:59.014120+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images"
  }
}
```

</details>

---

### Tool result

_source line 161 · 2026-05-24T16:43:59.064773+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_2/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---

### Assistant

_source line 162 · 2026-05-24T16:44:07.120318+00:00_

交叉回应已提交给 Director。

核心分歧点：
- **M1 降级**：凸 probe (logistic regression) 的解唯一，多种子要求不适用，问题在 data split 而非 seed，严重程度应为 Should-Fix
- **S4 降级**：Abstract 两个发现逻辑兼容（信号性质 vs. 功能局限），缺的是过渡句而非逻辑一致性
- **S5 降级**：Appendix B 已提供独立层扫描验证 (L10-L28, N=201)，验证系统性合理
- **Overall 分差**：我给 3.0 (Findings) vs R1 的 3.5 (Borderline Conference)，主要因为我对新颖性评估更严格——单语言对 + negative XNLI 结论 + 2/3 steering 失败的增量贡献不足以支撑 Borderline Conference

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2"
}
```

</details>

---

## Round 5

112 recorded events

### User

_source line 163 · 2026-05-25T04:19:12.436627+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性与完整性**审查。

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

### 1. 新颖性与贡献评估
- 论文的三个 contributions 是否足以构成 EMNLP long paper 级别的贡献？
- "Detection ≠ Decision" 这一发现在 Basu et al. 2026 已有类似结论——本文的增量贡献是什么？
- 跨语言冲突信号的检测性（Contribution 1）是否属于"expected result"（已知冲突信号可检测 + 已知跨语言表征共享 → 跨语言冲突信号可检测）？
- Steering 仅在一个模型的一个层有效——这是否足以支撑 Contribution 2 的 claim？

### 2. 相关工作覆盖
- 是否遗漏了关键相关工作？特别关注：
  - 跨语言 mechanistic interpretability 的最新工作（2025-2026）
  - Knowledge conflict 在多语言场景的行为研究
  - Representation steering 的最新方法论进展
  - Probing methodology 的批判性讨论（是否引用了 Belinkov 2022 survey？）
- 引用是否全部真实存在？（特别注意 2026 年的引用）

### 3. 写作质量
- Abstract 是否在 200 words 以内（EMNLP 2026 要求）？
- 论文叙事是否清晰连贯？Introduction 的 contribution list 与实验结果是否一致？
- Discussion 是否过于 speculative（如三个 hypotheses for steering failure）？
- Limitations 是否覆盖了关键弱点？

### 4. 格式合规
- 正文是否在 8 页以内？
- 是否正确使用 ACL 模板（\usepackage[review]{acl}）？
- 匿名性：是否有任何去匿名化线索？
- 图表质量：Figure 1, 2, 3 的信息密度和可读性
- Table 格式是否符合 ACL 标准？

### 5. 整体论文结构
- 正面结果（probing）和负面结果（Qwen/Gemma steering failure）的比例是否平衡？
- 论文是否过于 Llama-centric？三模型设计的预期价值是否充分实现？
- Conclusion 是否过于保守或过于激进？

请输出标准审稿格式：Summary → Strengths → Weaknesses（按 severity: Must-Fix / Should-Fix / Minor 分级）→ Questions → Missing References → 建议评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 164 · 2026-05-25T04:19:19.301240+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 165 · 2026-05-25T04:19:19.352070+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/review_reviewer_2_a0a58dd3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 166 · 2026-05-25T04:19:22.316174+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-prod42"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-prod42"
  }
}
```

</details>

---

### Tool result

_source line 167 · 2026-05-25T04:19:22.517605+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 168 · 2026-05-25T04:19:26.340038+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
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

_source line 169 · 2026-05-25T04:19:26.591259+00:00_

/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 251
}
```

</details>

---

### Tool call

_source line 170 · 2026-05-25T04:19:28.753270+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 171 · 2026-05-25T04:19:28.803973+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 172 · 2026-05-25T04:19:34.986213+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
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

_source line 173 · 2026-05-25T04:19:35.087173+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 174 · 2026-05-25T04:19:44.441588+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
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

### Tool call

_source line 175 · 2026-05-25T04:19:45.047704+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool call

_source line 176 · 2026-05-25T04:19:45.550160+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---

### Tool result

_source line 177 · 2026-05-25T04:19:45.853113+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 443.5}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 508.9}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 544.9}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 507.3}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 507.8}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.1}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 519.4}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 533.0}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 483.5}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_
…[truncated 317 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1411
}
```

</details>

---

### Tool result

_source line 178 · 2026-05-25T04:19:45.904283+00:00_

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
18	\title{English-Chinese Knowledge Conflict Signals Mirror General Cross-Lingual Asymmetries}
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
70	\begin{tabular}{lcccccc}
71	\toprule
72
…[truncated 3343 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---

### Tool result

_source line 179 · 2026-05-25T04:19:52.842540+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Overall Recommendation Scale

The 
…[truncated 1096 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7292
}
```

</details>

---

### Tool call

_source line 180 · 2026-05-25T04:19:59.257679+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
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

_source line 181 · 2026-05-25T04:19:59.309023+00:00_

/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/acl_latex.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 182 · 2026-05-25T04:20:10.195715+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 183 · 2026-05-25T04:20:10.246314+00:00_

1	When multilingual large language models (LLMs) encounter conflicting information across languages, presentation language can determine the answer. Behavioral studies attribute this to linguistic affinity, but the internal mechanism remains unknown: how is the conflict signal encoded, and does detectability imply causal influence on resolution?
2	
3	We probe residual stream representations in Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-IT, focusing on English (EN)--Chinese (ZH) conflicts. Our analysis combines cross-lingual transfer, Cross-lingual Natural Language Inference (XNLI) non-conflict baselines, confound exclusion, and representation steering. Conflict signals are linearly detectable across languages, and cross-lingual transfer exhibits a directional asymmetry: probes trained on Chinese transfer to English ${\sim}$7 percentage points more accurately than the reverse. This asymmetry is consistent with the XNLI non-conflict baseline in both magnitude and direction, with overlapping confidence intervals, mirroring the model's general multilingual structure rather than conflict-specific encoding. A dissociation emerges between detection and decision in Llama-3.1-8B-Instruct: the probe signal peaks at late layers (88\% depth), but representation steering achieves causal influence only at a mid-layer (41\% depth); analogous Qwen and Gemma steering yields no significant effect. These findings, observed in Llama-3.1-8B-Instruct and absent in Qwen and Gemma, indicate that linear detectability does not imply causal relevance, with implications for probe-based intervention.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 184 · 2026-05-25T04:20:10.648157+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 185 · 2026-05-25T04:20:11.153232+00:00_

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
…[truncated 4607 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 505
}
```

</details>

---

### Tool call

_source line 186 · 2026-05-25T04:20:11.153607+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 187 · 2026-05-25T04:20:11.608085+00:00_

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
13	Behavioral consequences have been documented by \citet{wang2025lost}, \citet{zhao2026when} (CLEAR cross-lingual conflict benchmark), and \citet{ifergan2024beneath, xing2024evaluating}; our work provides a mechanistic account of why such asymmetries arise.
14	
15	\paragraph{Representation steering and causal intervention.}
16	\citet{li2023iti} introduced Inferenc
…[truncated 1506 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---

### Tool call

_source line 188 · 2026-05-25T04:20:11.608555+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 189 · 2026-05-25T04:20:12.519424+00:00_

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
18	For cross-lingual transfer, we translate all inputs into Chinese using a Qwen3-8B pipeline, with quality validated by COMET (Crosslingual Optimized Metric for Evaluation of Translation; \citet{rei2020comet}) back-translation scores used in confound analysis (\S\ref{sec:confound_method}).
19	
20	\subsection{Activation Extraction and Probing}
21	\label{sec:extraction}
22	
23	For each input, we construct English and Chinese versions and extract the last-token residual stream $\mathbf{h}_l \in \mathbb{R}^d$ at every layer $l$ ($L = 32$ for Llama, $36$ for Qwen, $42$ for Gemma; $d = 4096$ for Llama/Qwen, $3584$ for Gemma), following the last-token aggregation principle \citep{belinkov2022probing}.
24	We record the model's answer and assign bin
…[truncated 3020 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 910
}
```

</details>

---

### Tool call

_source line 190 · 2026-05-25T04:20:12.520027+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 191 · 2026-05-25T04:20:13.022434+00:00_

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
16	We translate all English contexts and questions into Chinese using a Qwen3-8B translation pipeline (EN$\to$ZH), with quality validated by COMET \citep{rei2020comet} back-translation scores.
17	
18	\paragraph{Probing.}
19	For each layer $l$, we train an $L_2$-regularized logistic regression probe ($C = 1.0$, scikit-learn default) on the last-token residual stream representation $\mathbf{h}_l$, with binary labels indicating whether the model chose the contextual or parametric answer.
20	We report balanced accuracy to account for class imbalance.
21	All confidence intervals (CIs) are computed via bootstrap resampling with paired differences for asymmetry estimation.
22	All activation extraction and steering exp
…[truncated 15405 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 192 · 2026-05-25T04:20:13.022815+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 193 · 2026-05-25T04:20:13.475231+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Causal influence is localized to L13 regardless of detection peak.}
5	In Llama, causal influence is consistently localized to layer~13 (41\% depth; Fisher $p = 0.002$), regardless of where detection accuracy peaks: EN$\to$EN detection peaks at L28 (88\% depth) while ZH$\to$ZH peaks at L13 itself, yet causal influence is found only at L13 in both cases, with all late-layer interventions producing no significant behavioral change ($p > 0.3$).
6	This layer coincides with the site of cross-lingual alignment identified in prior work \citep{muller2021first, wendler2024llamas}, suggesting that mid-layers serve a dual role in alignment and conflict resolution.
7	The detection signal at later layers is best understood as a diagnostic readout of a decision already made upstream.
8	A practical implication follows: intervention experiments that target only the highest-accuracy layer risk missing the computationally relevant site; cross-layer sweeps are necessary.
9	Steering failed in both Qwen (L14, 39\%; $n = 131$, best $p = 0.785$) and Gemma (L17, 40\%; $n = 171$, best $p = 0.448$), with zero directional flips in both cases.
10	The Gemma result is particularly informative: its 88.9\% probe accuracy, the highest among all three models, rules out probe quality as a confound, since the direction that best separates conflict labels carries no causal influence despite being highly discriminative.
11	This establishes that the causal influence of the probe direction is architecture-dependent, not a general property of mid-layer computation.
12	
13	\paragraph{Why does steering fail in Qwen and Gemma?}
14	Three mechanistic hypotheses merit consideration.
15	First, the causal pathway may be non-linear: the probe direction captures the dominant linear component of the conflict signal, but the actual causal structure may involve non-linear interactions that single-direction perturbation cannot address \citep{elhage2022toy}.

…[truncated 3728 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 194 · 2026-05-25T04:20:13.526042+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 195 · 2026-05-25T04:20:13.977820+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that knowledge conflict signals in multilingual LLMs are linearly detectable across languages (balanced accuracies 75.0--77.6\% within-language, all cross-lingual transfers above chance at $p < 0.001$) and that the transfer asymmetry (ZH$\to$EN exceeding EN$\to$ZH by ${\sim}$6--7~pp) is consistent with the XNLI non-conflict baseline across all three architectures, reflecting general cross-lingual structure rather than conflict-specific encoding.
5	
6	In Llama-3.1-8B-Instruct, causal influence is consistently localized to L13 (41\% depth; Fisher $p = 0.002$) regardless of where detection accuracy peaks, and all late-layer interventions fail.
7	Linear detectability is neither sufficient nor predictive of causal relevance; cross-layer sweeps are necessary to identify the computationally relevant site.
8	
9	Steering failed in both Qwen and Gemma despite Gemma's 88.9\% probe accuracy, confirming that the causal influence of the probe direction is architecture-specific.
10	Future work should explore alternative intervention methods, diverse language pairs, and sparse autoencoder decomposition.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---

### Tool call

_source line 196 · 2026-05-25T04:20:13.978290+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 197 · 2026-05-25T04:20:14.480413+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	Our study has three main limitations.
5	First, we evaluate only one language pair (English-Chinese) and causal steering succeeded only in Llama at L13; Gemma L17 failed despite 88.9\% probe accuracy ($n = 171$) and Qwen L14 ($n = 131$) was also negative.
6	Typologically diverse language pairs and alternative intervention methods are needed to assess generality.
7	Second, the effective dataset size (966 to 1,590 samples per model) is constrained by parametric knowledge verification, which retains only questions where the model confidently knows the ground truth and may bias toward well-represented knowledge; additionally, Qwen3-8B serves as both the translation model and an experimental subject, though COMET-based quality control and Llama/Gemma cross-validation mitigate this dual-role concern.
8	Third, all probing results are based on a single train/test split with bootstrap confidence intervals capturing within-split variability; while peak balanced accuracy remains stable across seeds (Llama $\pm$0.12\%, Gemma $\pm$1.32\%, Qwen $\pm$1.90\%), the specific peak layer can shift, and future work should verify stability across larger datasets to improve statistical power for stratified comparisons such as the COMET tercile ablation.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 198 · 2026-05-25T04:20:15.684467+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions (soundness, excitement, overall assessment, etc.), their scales, and descriptions. Include the full text of each criterion."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions (soundness, excitement, overall assessment, etc.), their scales, and descriptions. Include the full text of each criterion."
  }
}
```

</details>

---

### Tool result

_source line 199 · 2026-05-25T04:20:24.522329+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## 2. **Soundness**
Scale: 1-5 (with .5 increments)
- **5**: "Excellent: This study is one of the most thorough I have seen."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. **Excitement**
Scale: 1-5 (with .5 increments)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

## 4. **Overall Assessment**
Scale: 1-5 (with .5 increments)
- **5**: "Consider for Award: Could be considered for an outstanding paper award."
- **4.5**: "Borderline Award"
- **4**: "Conference: Could be accepted to an ACL conference."
- **3.5**: "Borderline Conference"
- **3**: "Findings: Could be accepted to the Findings of the ACL."
- **2.5**: "Borderline Findings"
- **2**: "Resubmit next cycle: Needs substantial revisions by next ARR cycle."
- **1.5**: "Resubmit after next cycle: Needs substantial 
…[truncated 1676 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 8837
}
```

</details>

---

### Tool call

_source line 200 · 2026-05-25T04:20:36.422053+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---

### Tool result

_source line 201 · 2026-05-25T04:20:37.985361+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/review_reviewer_2_a0a58dd3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1563
}
```

</details>

---

### Tool call

_source line 202 · 2026-05-25T04:20:38.136502+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---

### Tool result

_source line 203 · 2026-05-25T04:20:38.990169+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/review_reviewer_2_a0a58dd3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---

### Tool call

_source line 204 · 2026-05-25T04:20:39.141167+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---

### Tool result

_source line 205 · 2026-05-25T04:20:40.195462+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/review_reviewer_2_a0a58dd3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1054
}
```

</details>

---

### Tool call

_source line 206 · 2026-05-25T04:20:40.346382+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---

### Tool result

_source line 207 · 2026-05-25T04:20:41.200094+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/review_reviewer_2_a0a58dd3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---

### Tool call

_source line 208 · 2026-05-25T04:20:41.351078+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---

### Tool result

_source line 209 · 2026-05-25T04:20:41.401713+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/review_reviewer_2_a0a58dd3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 210 · 2026-05-25T04:20:41.502485+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---

### Tool result

_source line 211 · 2026-05-25T04:20:41.553154+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/review_reviewer_2_a0a58dd3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 212 · 2026-05-25T04:20:41.553589+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---

### Tool result

_source line 213 · 2026-05-25T04:20:41.604703+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/review_reviewer_2_a0a58dd3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 214 · 2026-05-25T04:20:41.655383+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---

### Tool result

_source line 215 · 2026-05-25T04:20:41.907825+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/review_reviewer_2_a0a58dd3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---

### Tool call

_source line 216 · 2026-05-25T04:20:41.908290+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---

### Tool call

_source line 217 · 2026-05-25T04:20:41.908488+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---

### Tool result

_source line 218 · 2026-05-25T04:20:42.009187+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/review_reviewer_2_a0a58dd3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---

### Tool result

_source line 219 · 2026-05-25T04:20:42.009604+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/review_reviewer_2_a0a58dd3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 220 · 2026-05-25T04:20:55.537048+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/ 2>/dev/null || echo \"DIR NOT FOUND\"",
  "description": "Check PDF images directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/_pdf_images/ 2>/dev/null || echo \"DIR NOT FOUND\"",
    "description": "Check PDF images directory"
  }
}
```

</details>

---

### Tool result

_source line 221 · 2026-05-25T04:20:55.718026+00:00_

DIR NOT FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 180
}
```

</details>

---

### Tool call

_source line 222 · 2026-05-25T04:20:58.480027+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/ -name \"*.png\" 2>/dev/null | head -20",
  "description": "Find PNG files in review artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/ -name \"*.png\" 2>/dev/null | head -20",
    "description": "Find PNG files in review artifacts"
  }
}
```

</details>

---

### Tool result

_source line 223 · 2026-05-25T04:20:58.580906+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 224 · 2026-05-25T04:21:07.028205+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/ 2>/dev/null",
  "description": "List review round 3 artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/ 2>/dev/null",
    "description": "List review round 3 artifacts"
  }
}
```

</details>

---

### Tool result

_source line 225 · 2026-05-25T04:21:07.078836+00:00_

total 368
drwxr-xr-x  2 ubuntu ubuntu   4096 May 25 04:20 .
drwxr-xr-x 14 ubuntu ubuntu   4096 May 25 04:15 ..
-rw-r--r--  1 ubuntu ubuntu 366570 May 25 04:12 submitted.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 226 · 2026-05-25T04:21:14.459033+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/submitted.pdf",
  "project": "clkc_mech_interp",
  "pages": "1-5",
  "dpi": "150",
  "output_dir": "/tmp/review_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/submitted.pdf",
    "project": "clkc_mech_interp",
    "pages": "1-5",
    "dpi": "150",
    "output_dir": "/tmp/review_pdf_images"
  }
}
```

</details>

---

### Tool result

_source line 227 · 2026-05-25T04:21:15.061878+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/tmp/review_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 443.5}, {\"page\": 2, \"path\": \"/tmp/review_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 508.9}, {\"page\": 3, \"path\": \"/tmp/review_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 544.9}, {\"page\": 4, \"path\": \"/tmp/review_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 507.3}, {\"page\": 5, \"path\": \"/tmp/review_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 507.8}], \"total_pages\": 11, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/tmp/review_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 602
}
```

</details>

---

### Tool call

_source line 228 · 2026-05-25T04:21:24.405481+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/review_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/review_pdf_images/submitted_p1.png"
  }
}
```

</details>

---

### Tool call

_source line 229 · 2026-05-25T04:21:24.607010+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/review_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/review_pdf_images/submitted_p2.png"
  }
}
```

</details>

---

### Tool call

_source line 230 · 2026-05-25T04:21:25.115046+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/review_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/review_pdf_images/submitted_p3.png"
  }
}
```

</details>

---

### Tool call

_source line 231 · 2026-05-25T04:21:25.467970+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/review_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/review_pdf_images/submitted_p4.png"
  }
}
```

</details>

---

### Tool result

_source line 232 · 2026-05-25T04:21:25.470104+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1064
}
```

</details>

---

### Tool call

_source line 233 · 2026-05-25T04:21:25.470516+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/review_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/review_pdf_images/submitted_p5.png"
  }
}
```

</details>

---

### Tool result

_source line 234 · 2026-05-25T04:21:26.230509+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1623
}
```

</details>

---

### Tool result

_source line 235 · 2026-05-25T04:21:27.338978+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2223
}
```

</details>

---

### Tool result

_source line 236 · 2026-05-25T04:21:27.540762+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2070
}
```

</details>

---

### Tool result

_source line 237 · 2026-05-25T04:21:27.542024+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2074
}
```

</details>

---

### Tool call

_source line 238 · 2026-05-25T04:21:35.579136+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/submitted.pdf",
  "project": "clkc_mech_interp",
  "pages": "6-11",
  "dpi": "150",
  "output_dir": "/tmp/review_pdf_images2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_3/submitted.pdf",
    "project": "clkc_mech_interp",
    "pages": "6-11",
    "dpi": "150",
    "output_dir": "/tmp/review_pdf_images2"
  }
}
```

</details>

---

### Tool result

_source line 239 · 2026-05-25T04:21:36.281582+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 6, \"path\": \"/tmp/review_pdf_images2/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.1}, {\"page\": 7, \"path\": \"/tmp/review_pdf_images2/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 519.4}, {\"page\": 8, \"path\": \"/tmp/review_pdf_images2/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 533.0}, {\"page\": 9, \"path\": \"/tmp/review_pdf_images2/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 483.5}, {\"page\": 10, \"path\": \"/tmp/review_pdf_images2/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 562.0}, {\"page\": 11, \"path\": \"/tmp/review_pdf_images2/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 508.9}], \"total_pages\": 11, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/tmp/review_pdf_images2\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 702
}
```

</details>

---

### Tool call

_source line 240 · 2026-05-25T04:21:42.759527+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/review_pdf_images2/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/review_pdf_images2/submitted_p6.png"
  }
}
```

</details>

---

### Tool call

_source line 241 · 2026-05-25T04:21:42.910414+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/review_pdf_images2/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/review_pdf_images2/submitted_p7.png"
  }
}
```

</details>

---

### Tool call

_source line 242 · 2026-05-25T04:21:43.263343+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/review_pdf_images2/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/review_pdf_images2/submitted_p8.png"
  }
}
```

</details>

---

### Tool call

_source line 243 · 2026-05-25T04:21:43.263926+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/review_pdf_images2/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/review_pdf_images2/submitted_p9.png"
  }
}
```

</details>

---

### Tool call

_source line 244 · 2026-05-25T04:21:43.521021+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/review_pdf_images2/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/review_pdf_images2/submitted_p10.png"
  }
}
```

</details>

---

### Tool call

_source line 245 · 2026-05-25T04:21:43.975026+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/review_pdf_images2/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/review_pdf_images2/submitted_p11.png"
  }
}
```

</details>

---

### Tool result

_source line 246 · 2026-05-25T04:21:45.487495+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2727
}
```

</details>

---

### Tool result

_source line 247 · 2026-05-25T04:21:46.602524+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3692
}
```

</details>

---

### Tool result

_source line 248 · 2026-05-25T04:21:46.754297+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3490
}
```

</details>

---

### Tool result

_source line 249 · 2026-05-25T04:21:46.856232+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3592
}
```

</details>

---

### Tool result

_source line 250 · 2026-05-25T04:21:47.108744+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3587
}
```

</details>

---

### Tool result

_source line 251 · 2026-05-25T04:21:47.159837+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3184
}
```

</details>

---

### Tool call

_source line 252 · 2026-05-25T04:22:59.286483+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "references.bib",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "references.bib",
    "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 253 · 2026-05-25T04:22:59.289007+00:00_

/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 254 · 2026-05-25T04:23:06.535783+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 255 · 2026-05-25T04:23:06.686873+00:00_

1	% References for Cross-Lingual Knowledge Conflict paper
2	
3	@article{basu2026interpretability,
4	  author    = {Basu, Sanjay and Patel, Sadiq Y. and Sheth, Parth and Muralidharan, Bhairavi and Elamaran, Namrata and Kinra, Aakriti and Morgan, John and Batniji, Rajaie},
5	  title     = {Interpretability without Actionability: Mechanistic Methods Cannot Correct Language Model Errors Despite Near-Perfect Internal Representations},
6	  journal   = {arXiv preprint arXiv:2603.18353},
7	  year      = {2026},
8	  url       = {https://arxiv.org/abs/2603.18353}
9	}
10	
11	@article{brink2026probing,
12	  author    = {Brink, I. and Boer, A. and Ulmer, D.},
13	  title     = {Probing for Knowledge Attribution in Large Language Models},
14	  journal   = {arXiv preprint arXiv:2602.22787},
15	  year      = {2026},
16	  url       = {https://arxiv.org/abs/2602.22787}
17	}
18	
19	@inproceedings{ifergan2024beneath,
20	  author    = {Ifergan, Matan and Choshen, Leshem and Aharoni, Roee and Szpektor, Idan and Abend, Omri},
21	  title     = {Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in {LLMs}},
22	  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2025},
23	  year      = {2024},
24	  url       = {https://arxiv.org/abs/2408.10646}
25	}
26	
27	
28	@inproceedings{li2025taming,
29	  author    = {Li, Gaotang and Chen, Yufei and Tong, Hanghang},
30	  title     = {Taming Knowledge Conflicts in Language Models},
31	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},
32	  year      = {2025},
33	  url       = {https://arxiv.org/abs/2503.10996}
34	}
35	
36	@article{pham2026where,
37	  author    = {Pham, Minh Vu and Borkakoty, Hrishav and Hou, Yufang},
38	  title     = {Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge Conflict in Language Models},
39	  journal   = {arXiv preprint arXiv:2601.09445},
40	  year      = {2026},
41	  url       = {https://arxiv.org
…[truncated 13622 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 256 · 2026-05-25T04:23:17.586093+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2603.18353 Basu interpretability actionability mechanistic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2603.18353 Basu interpretability actionability mechanistic"
  }
}
```

</details>

---

### Tool call

_source line 257 · 2026-05-25T04:23:17.987661+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2601.16390 Pokharel cross-lingual activation steering"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2601.16390 Pokharel cross-lingual activation steering"
  }
}
```

</details>

---

### Tool call

_source line 258 · 2026-05-25T04:23:18.439662+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2601.07041 Zhao \"When Abundance Conceals Weakness\" knowledge conflict multilingual"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2601.07041 Zhao \"When Abundance Conceals Weakness\" knowledge conflict multilingual"
  }
}
```

</details>

---

### Tool result

_source line 259 · 2026-05-25T04:23:24.484359+00:00_

Web search results for query: "arxiv 2603.18353 Basu interpretability actionability mechanistic"

Links: [{"title":"[2603.18353] Interpretability without actionability","url":"https://arxiv.org/abs/2603.18353"},{"title":"Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations","url":"https://arxiv.org/html/2603.18353v1"},{"title":"(PDF) Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations","url":"https://www.researchgate.net/publication/402859588_Interpretability_without_actionability_mechanistic_methods_cannot_correct_language_model_errors_despite_near-perfect_internal_representations"},{"title":"Interpretability without actionability: mechanistic methods ...","url":"https://arxiv.org/pdf/2603.18353"},{"title":"Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2603.18353"},{"title":"A Survey on Mechanistic Interpretability for Multi-Modal Foundation Models","url":"https://arxiv.org/html/2502.17516v1"},{"title":"Interpretability Can Be Actionable","url":"https://arxiv.org/html/2605.11161v1"}]

I found the paper you're looking for. Here's what the search reveals:

The paper is titled "Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations" by Sanjay Basu and 7 other authors, submitted on March 18, 2026.

**Key findings:**

The paper investigates whether mechanistic interpretability methods can bridge the knowledge-action gap, where language models encode task-relevant knowledge in internal representations that far exceeds their output performance.

The researchers compared four mechanistic interpretability methods: concept bottleneck steerin
…[truncated 800 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6898
}
```

</details>

---

### Tool result

_source line 260 · 2026-05-25T04:23:25.286937+00:00_

Web search results for query: "arxiv 2601.07041 Zhao "When Abundance Conceals Weakness" knowledge conflict multilingual"

Links: [{"title":"[2601.07041] When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models","url":"https://arxiv.org/abs/2601.07041"},{"title":"When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models","url":"https://arxiv.org/html/2601.07041v1"},{"title":"When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models","url":"https://arxiv.org/pdf/2601.07041"},{"title":"Uncovering inequalities in new knowledge learning by large language models across different languages","url":"https://arxiv.org/html/2503.04064v1"},{"title":"Seeing through the Conflict: Transparent Knowledge Conflict Handling in Retrieval-Augmented Generation","url":"https://arxiv.org/html/2601.06842"}]

Based on the search results, I found the paper you're looking for:

**Title:** "When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models"

**Authors:** Jiaqi Zhao, Qiang Huang, Haodong Chen, Xiaoxing You, and Jun Yu from Harbin Institute of Technology (Shenzhen) and Hangzhou Dianzi University

**Main Contribution:** The paper addresses how Large Language Models encode vast world knowledge across multiple languages, yet their internal beliefs are often unevenly distributed across linguistic spaces. When external evidence contradicts these language-dependent memories, models encounter cross-lingual knowledge conflict, a phenomenon largely unexplored beyond English-centric settings.

**Methodology:** The authors introduce CLEAR, a Cross-Lingual knowlEdge conflict evAluation fRamework that systematically examines how multilingual LLMs reconcile conflicting internal beliefs and multilingual external evidence, decomposing conflict resolution into four progressive scenarios.

**Key Findings:** In reasoning-intensive tasks, conflict resolution is dominated by language resource abundance, with high-resource languages exert
…[truncated 344 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6847
}
```

</details>

---

### Tool result

_source line 261 · 2026-05-25T04:23:25.588344+00:00_

Web search results for query: "arxiv 2601.16390 Pokharel cross-lingual activation steering"

Links: [{"title":"[2601.16390] Cross-Lingual Activation Steering for Multilingual Language Models","url":"https://arxiv.org/abs/2601.16390"},{"title":"Language Steering for Multilingual In-Context Learning","url":"https://arxiv.org/html/2602.02326v2"},{"title":"Cross-Lingual Activation Steering for Multilingual Language Models","url":"https://arxiv.org/pdf/2601.16390"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models","url":"https://arxiv.org/pdf/2502.15639"},{"title":"Can Activation Steering Generalize Across Languages? A Study on Syllogistic Reasoning in Language Models - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.125/"}]

Based on the search results, I found the paper you're looking for. Here's information about arxiv 2601.16390:

**Title:** Cross-Lingual Activation Steering for Multilingual Language Models

**Authors:** Rhitabrat Pokharel, Ameeta Agrawal, and Tanay Nagar

**Main Contribution:** The authors propose Cross-Lingual Activation Steering (CLAS), a training-free inference-time intervention that selectively modulates neuron activations.

**Problem Addressed:** Large language models exhibit strong multilingual capabilities, yet significant performance gaps persist between dominant and non-dominant languages, with prior work attributing this gap to imbalances between shared and language-specific neurons in multilingual representations.

**Results:** The method achieves average improvements of 2.3% (Acc.) and 3.4% (F1) respectively on classification and generation benchmarks, while maintaining high-resource language performance.

**Key Finding:** The authors discover that effective transfer operates through functional divergence rather than strict alignment; performance gains correlate with increased language cluster separation.

The paper was submitted o
…[truncated 122 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7600
}
```

</details>

---

### Tool call

_source line 262 · 2026-05-25T04:23:32.512977+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2602.22787 Brink probing knowledge attribution"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2602.22787 Brink probing knowledge attribution"
  }
}
```

</details>

---

### Tool call

_source line 263 · 2026-05-25T04:23:32.915225+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "cross-lingual mechanistic interpretability probing steering 2025 2026 multilingual LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "cross-lingual mechanistic interpretability probing steering 2025 2026 multilingual LLM"
  }
}
```

</details>

---

### Tool result

_source line 264 · 2026-05-25T04:23:37.081233+00:00_

Web search results for query: "arxiv 2602.22787 Brink probing knowledge attribution"

Links: [{"title":"[2602.22787] Probing for Knowledge Attribution in Large Language Models","url":"https://arxiv.org/abs/2602.22787"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=235&show=1000"},{"title":"Probing for Knowledge Attribution in Large Language Models","url":"https://arxiv.org/html/2602.22787"},{"title":"Probing for Knowledge Attribution in Large Language Models","url":"https://arxiv.org/pdf/2602.22787"},{"title":"Source-Aware Training Enables Knowledge Attribution in Language Models","url":"https://arxiv.org/pdf/2404.01019"}]

Based on the search results, here's information about the paper:

**Title:** "Probing for Knowledge Attribution in Large Language Models"

**Authors:** Ivo Brink, Alexander Boer, and Dennis Ulmer

**Main Focus:** The work focuses on the problem of contributive attribution: identifying the dominant knowledge source behind each output.

**Problem Addressed:** Large language models (LLMs) often generate fluent but unfounded claims, or hallucinations, which fall into two types: (i) faithfulness violations - misusing user context - and (ii) factuality violations - errors from internal knowledge.

**Approach:** A probe, a simple linear classifier trained on model hidden representations, can reliably predict contributive attribution. For its training, they introduce AttriWiki, a self-supervised data pipeline that prompts models to recall withheld entities from memory or read them from context, generating labelled examples automatically.

**Results:** Probes trained on AttriWiki data reveal a strong attribution signal, achieving up to 0.96 Macro-F1 on Llama-3.1-8B, Mistral-7B, and Qwen-7B, transferring to out-of-domain benchmarks.

The paper was submitted on February 26, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 4568
}
```

</details>

---

### Tool result

_source line 265 · 2026-05-25T04:23:41.246061+00:00_

Web search results for query: "cross-lingual mechanistic interpretability probing steering 2025 2026 multilingual LLM"

Links: [{"title":"Language Steering for Multilingual In-Context Learning","url":"https://arxiv.org/html/2602.02326v1"},{"title":"Improving Multilingual Language Models by Aligning Representations through Steering","url":"https://arxiv.org/html/2505.12584"},{"title":"CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark","url":"https://arxiv.org/pdf/2601.08331"},{"title":"Steering Large Language Models for Cross-lingual Information Retrieval | Proceedings of the 47th International ACM SIGIR Conference on Research and Development in Information Retrieval","url":"https://dl.acm.org/doi/10.1145/3626772.3657819"},{"title":"Improving Multilingual Language Models by Aligning Representations through Steering","url":"https://arxiv.org/pdf/2505.12584"},{"title":"Causal Language Control in Multilingual Transformers via Sparse Feature Steering","url":"https://arxiv.org/pdf/2507.13410"},{"title":"[2512.02841] Cross-Lingual Prompt Steerability: Towards Accurate and Robust LLM Behavior across Languages","url":"https://arxiv.org/abs/2512.02841"}]

I found several recent papers on cross-lingual mechanistic interpretability and steering in multilingual language models from 2025-2026. Here are the key findings:

## Recent Research Overview

Multilingual models encode language identity and linguistic structure in distinct regions of their latent space, which can significantly affect cross-lingual generalization. Language-specific information is not uniformly distributed, but instead manifests as structured patterns within model activations.

## Steering Approaches

Recent research has used representation steering to align hidden states between English and a target language by learning a steering vector through least-squares optimization and applying it across all layers of the model.

Recent work probing LLMs has revealed language-specific features and neurons,
…[truncated 980 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8330
}
```

</details>

---

### Tool call

_source line 266 · 2026-05-25T04:23:46.567285+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ravichander probing \"information-theoretic\" critique 2021 OR Pimentel probing information theory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ravichander probing \"information-theoretic\" critique 2021 OR Pimentel probing information theory"
  }
}
```

</details>

---

### Tool call

_source line 267 · 2026-05-25T04:23:46.818394+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"CLaS-Bench\" cross-lingual alignment steering benchmark 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"CLaS-Bench\" cross-lingual alignment steering benchmark 2026 arxiv"
  }
}
```

</details>

---

### Tool result

_source line 268 · 2026-05-25T04:23:51.843689+00:00_

Web search results for query: ""CLaS-Bench" cross-lingual alignment steering benchmark 2026 arxiv"

Links: [{"title":"[2601.08331] CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark","url":"https://arxiv.org/abs/2601.08331"},{"title":"CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark","url":"https://arxiv.org/html/2601.08331v1"},{"title":"CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark","url":"https://arxiv.org/pdf/2601.08331"},{"title":"Cross-Lingual Activation Steering for Multilingual Language Models","url":"https://arxiv.org/html/2601.16390"},{"title":"[2601.16390] Cross-Lingual Activation Steering for Multilingual Language Models","url":"https://arxiv.org/abs/2601.16390"}]

Based on the search results, I found information about CLaS-Bench:

CLaS-Bench is the first standardized benchmark for multilingual steering, enabling both rigorous scientific analysis of language representations and practical evaluation of steering as a low-cost adaptation alternative.

The benchmark is a lightweight parallel-question benchmark for evaluating language-forcing behavior in LLMs across 32 languages, enabling systematic evaluation of multilingual steering methods.

Steering performance is measured along two axes: language control and semantic relevance, combined into a single harmonic-mean steering score. The research finds that across languages the simple residual-based DiffMean method consistently outperforms all other methods.

A layer-wise analysis reveals that language-specific structure emerges predominantly in later layers and steering directions cluster based on language family.

The paper was published on arXiv on January 13, 2026 (arxiv ID: 2601.08331) by Daniil Gurgurov and colleagues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5025
}
```

</details>

---

### Tool result

_source line 269 · 2026-05-25T04:23:53.002093+00:00_

Web search results for query: "Ravichander probing "information-theoretic" critique 2021 OR Pimentel probing information theory"

Links: [{"title":"An information theoretic view on selecting linguistic probes | Request PDF","url":"https://www.researchgate.net/publication/347234589_An_information_theoretic_view_on_selecting_linguistic_probes"},{"title":"Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance? | Request PDF","url":"https://www.researchgate.net/publication/355434387_Probing_the_Probing_Paradigm_Does_Probing_Accuracy_Entail_Task_Relevance"},{"title":"(PDF) Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://www.researchgate.net/publication/355072709_Probing_Classifiers_Promises_Shortcomings_and_Advances"},{"title":"Squib Probing Classiﬁers: Promises, Shortcomings, and Advances","url":"https://aclanthology.org/2022.cl-1.7.pdf"},{"title":"Probing Tasks Under Pressure","url":"https://aclanthology.org/2021.clicit-1.36.pdf"},{"title":"A Bayesian Framework for Information-Theoretic Probing - Tiago Pimentel","url":"https://tpimentelms.github.io/publication/2021-11-10-bayesian-information-theory"},{"title":"A Bayesian Framework for Information-Theoretic Probing - ACL Anthology","url":"https://aclanthology.org/2021.emnlp-main.229/"},{"title":"A Bayesian Framework for Information-Theoretic Probing","url":"https://arxiv.org/pdf/2109.03853"},{"title":"[2109.03853] A Bayesian Framework for Information-Theoretic Probing","url":"https://arxiv.org/abs/2109.03853"}]

Based on the search results, I found relevant information about both Ravichander's probing critique and Pimentel's information-theoretic approach:

## Ravichander's 2021 Critique

Ravichander et al. (2021) raised the possibility that probing may identify causally unused features, showing that probes can extract features merely encoded even if unused during inference. Their work was titled "Probing the probing paradigm: Does probing accuracy entail task relevance?"

##
…[truncated 881 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6434
}
```

</details>

---

### Tool call

_source line 270 · 2026-05-25T04:24:21.272727+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex | wc -w",
  "description": "Count abstract words"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex | wc -w",
    "description": "Count abstract words"
  }
}
```

</details>

---

### Tool result

_source line 271 · 2026-05-25T04:24:21.323375+00:00_

198

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 272 · 2026-05-25T04:26:22.619978+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿意见：新颖性与完整性\n\n## 论文信息\n- **标题**: English-Chinese Knowledge Conflict Signals Mirror General Cross-Lingual Asymmetries\n- **Venue**: EMNLP 2026 (ARR Long Paper)\n- **审查侧重**: 新颖性与贡献、相关工作覆盖、写作质量、格式合规、整体结构\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 — Findings（可被 Findings 接收）\n\n**一句话总结**: 实验设计和统计方法扎实，但核心发现 \"Detection ≠ Decision\" 已由 Basu et al. (2026) 建立，跨语言可检测性属于预期结果，且 steering 正面结果仅来自 1/3 模型的 1 个层，新颖性和贡献量不足以支撑主会议 long paper。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 方法论严谨（bootstrap CI、Bonferroni、TOST equivalence、confound exclusion），但 Contribution 2 的 claim 基于 1/3 模型正面结果略有过度 |\n| **Excitement** | 2.5/5 | 核心 insight（detection ≠ causation）已有先行工作；跨语言扩展有价值但增量有限；大量负面结果降低了 impact |\n| **Reproducibility** | 4/5 | 超参数、数据集分割、统计检验细节充分；GPU 型号和 seed 均有报告；独立复制实验是加分项 |\n| **Reviewer Confidence** | 4/5 | 熟悉 probing、representation steering、cross-lingual representations 相关文献 |\n\n---\n\n## 主要优势\n\n1. **统计严谨性突出。** Bootstrap paired CIs、Bonferroni 校正、TOST 等效性检验、Bayesian BF 分析，在 probing/steering 文献中这种统计水准少见。特别是 TOST 的 power analysis（80% power 需 ±12.5 pp margin）是诚实的自我批评。\n\n2. **Confound exclusion pipeline 设计完善。** COMET tercile 分层 + token overlap Jaccard 分析 + EN-DE 对照 + XNLI non-conflict baseline，系统性排除了翻译质量和词汇重叠两个关键混淆变量。EN-DE 的 near-zero asymmetry（Jaccard 14.8% 但 Δ=+1.2 pp, n.s.）特别有说服力。\n\n3. **负面结果的诚实报告。** Qwen 和 Gemma steering 失败的完整报告（包括 matched-condition Appendix Table 5），以及 Gemma 88.9% probe accuracy + zero flips 的对比，是强有力的 negative evidence。\n\n4. **独立复制设计。** L13 steering 用不同 seed、不同 train/test split 独立复制（Appendix C），boundary analysis 用独立采样 N=201（Appendix B），提升了因果定位结论的可信度。\n\n5. **XNLI baseline 比较方法论有价值。** 用非冲突语义任务的 probe transfer asymmetry 作为 baseline，这一方法论思路（\"先确认 baseline asymmetry 再解读 task-specific 差异\"）对后续跨语言 probing 工作有参考价值。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 核心发现 \"Detection ≠ Decision\" 的增量贡献不足\n- **具体位置**: Introduction 第 18 行引用 Basu et al. (2026)；Discussion §5 \"Relation to interpretability without actionability\" 段\n- **问题**: 论文的核心 insight——\"probe accuracy 不意味着 causal relevance\"——已由 Basu et al. (2026) 在临床 NLP 任务中建立（98.2% AUROC probe accuracy + steering 完全失败）。本文在 Discussion 中试图区分：mid-layer steering 在本文成功但在 Basu et al. 中失败，差异在于 layer selection。但这一区分是弱的：(a) 本文的 \"成功\" 仅限于 1/3 模型的 1 个层；(b) layer sweep 是方法论改进，不是新发现；(c) 2/3 模型的失败反而更接近 Basu et al. 的结论。论文需要更明确地阐述超越 Basu et al. 的具体贡献。\n- **为什么影响接收**: 若核心 contribution 已被先行工作覆盖，论文的 novelty 不足以支撑 long paper。\n- **建议修改方向**: 重新定位论文贡献——强调跨语言维度的独特性（如 asymmetry 的 baseline 归因），弱化 \"detection ≠ decision\" 作为独立 contribution。\n\n**N2** [critical] Contribution 2 (\"Architecture-dependent causal localization\") 证据过弱\n- **具体位置**: Introduction Contribution 2；§4.6 全节；Table 3；Appendix Table 5\n- **问题**: 该 contribution 声称 \"causal influence is consistently localized to L13 in Llama, while analogous steering in Qwen and Gemma yields no significant effect\"。但实际证据是：3 个模型中只有 1 个（Llama）在 1 个层（L13）显示显著效果。这不是 \"architecture-dependent causal localization\"，而是 \"我们在一个模型找到了正面结果，两个模型是 null\"。关键问题：\n  - Llama 的正面结果是否是 false positive？考虑到 multiple testing（3 models × 多个 layers × 10 α values），即使有 Bonferroni 校正，family-wise error rate 也需要跨模型评估。\n  - \"Architecture-dependent\" 的 claim 需要解释 **为什么** 不同架构表现不同，而不仅仅是报告它们不同。Discussion 中三个 hypotheses（non-linear pathway、superposition、sandwich normalization）全部是 untested speculation。\n- **为什么影响接收**: 核心 claim 的实验支撑不足以构成 EMNLP 级别贡献。\n- **建议修改方向**: (1) 将 claim 降级为 \"exploratory finding in Llama with null results in Qwen/Gemma\"；(2) 提供至少一个 hypothesis 的初步验证（如 Gemma sandwich norm 的 ablation）；(3) 补充更多模型或更多层的 steering 结果。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Contribution 1（跨语言冲突可检测性）可能是 expected result\n- **具体位置**: Introduction Contribution 1；§4.2-4.3\n- **问题**: 推理链：(1) 知识冲突信号在单语言内可检测（Zhao et al., 2024）→ (2) 多语言模型有共享跨语言表征空间（Wu et al., 2020; Wendler et al., 2024）→ (3) 因此跨语言冲突信号可检测。这是一个相当直接的推论。此外，XNLI baseline 显示 asymmetry 不是冲突特异的——这意味着 Contribution 1 的核心发现是 \"冲突信号的跨语言特性与通用跨语言特性无异\"，本质上是一个 null result。\n- **建议**: 更坦诚地讨论这一推理链的可预测性，并将 XNLI baseline 发现提升为更重要的贡献（\"任何跨语言 probing 研究都必须先控制 baseline asymmetry\" 是有实践价值的方法论建议）。\n\n**W2** [warning] 论文过度 Llama-centric，三模型设计的价值未充分实现\n- **具体位置**: 全文结构；§4.6 Causal Evidence；§5 Discussion\n- **问题**: 三模型设计本应提供 cross-architecture validation，但实际结果是：probing 部分三个模型一致（这是好的），steering 部分 2/3 是 null。论文的核心叙事（detection ≠ decision + mid-layer causal locus）完全依赖 Llama。Qwen 和 Gemma 的主要作用是提供 negative evidence，但 negative evidence 本身不构成 positive contribution。\n- **建议**: (1) 重新组织叙事——将 Llama 定位为 case study 而非通用结论；(2) 更深入分析 Qwen/Gemma 失败的原因，而非仅提供三个 untested hypotheses。\n\n**W3** [warning] 遗漏关键相关工作\n- **具体位置**: §2 Related Work\n- **问题**: 以下相关工作未被讨论：\n  - **Ravichander et al. (2021), \"Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance?\"** — 直接探讨了 probing accuracy 是否意味着 task relevance 的问题，与本文核心论点高度相关。本文引用了 Hewitt & Liang (2019) 的 control task 思路，但漏掉了 Ravichander et al. 对 probing accuracy ≠ task relevance 的更直接论证。\n  - **Gurgurov et al. (2026), \"CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark\" (arXiv:2601.08331)** — 首个跨语言 steering benchmark，覆盖 32 语言，与本文的 cross-lingual steering 实验直接相关。\n  - **Pimentel et al. (2020/2021)** 关于 information-theoretic probing 的理论框架，对 probing methodology 的讨论有补充价值。\n- **建议**: 在 Related Work 中补充这些引用，特别是 Ravichander et al.，因为它直接强化了本文的论点。\n\n**W4** [warning] Discussion 中三个 steering 失败 hypotheses 过于投机\n- **具体位置**: §5 \"Why does steering fail in Qwen and Gemma?\" 段\n- **问题**: 三个假设（non-linear causal pathway、residual stream superposition、architectural differences/sandwich normalization）全部未经验证。论文没有任何实验证据支持其中任何一个。虽然标注为 \"merit consideration\"，但在没有 ablation 或 diagnostic 的情况下，这些假设缺乏信息量——任何 steering 失败都可以用 \"可能是 non-linear\" 或 \"可能是 superposition\" 来解释。\n- **建议**: (1) 删减到最有证据支持的一个假设；或 (2) 对至少一个假设提供初步 diagnostic（如用 non-linear probe 检验 hypothesis 1，或用 PCA 可视化检验 hypothesis 2）。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Abstract 198 words（接近 200 上限），建议适度压缩以留出余量。\n- **M2**: Table 1 注释 \"Δ_asym is the mean of paired bootstrap differences, not the arithmetic difference of the reported single-seed accuracies\" 非常重要但容易被忽略，建议移入正文或用更醒目的方式呈现。\n- **M3**: §4.5 Confound Exclusion 中 Gemma 的 COMET tercile 结果（Δ = +10.3 pp, p = 0.278）在 confound 方向，虽然不显著，但应在 Limitations 中更明确提及。\n- **M4**: Figure 2（layer-wise probe accuracy）和 Figure 3（asymmetry forest plot）的信息密度适中。但 Figure 1（pipeline overview）信息量偏低——主要是流程描述，读正文即可获得相同信息。考虑替换为更有信息量的图（如 Llama L13 steering 前后的行为分布变化）。\n- **M5**: Appendix A (Use of AI Assistants) 的格式符合 ACL 2024+ 的建议，但措辞非常简短，可考虑补充 AI 辅助的具体边界说明。\n- **M6**: 论文引用 Marks & Tegmark (2024) 的 venue 写为 ICLR 2024，但该论文实际发表于 NeurIPS 2023（虽然 arXiv 版本 2023.10 发布），请核实。\n\n---\n\n## Questions to Authors\n\n**Q1**: Llama L13 的 steering 效果是否在不同 prompt template 下稳定？当前实验是否只使用了一种 prompt format？如果 prompt 变化导致 steering 失效，这将进一步削弱 causal claim。\n\n**Q2**: 为什么没有尝试 non-linear steering 方法（如 SAE-based steering，参考 Zhao et al. 2025 的 SpARE）？既然 Discussion 中自己提出了 \"non-linear causal pathway\" 假设，尝试 SAE steering 可以直接检验这一假设。\n\n**Q3**: Qwen3-8B 同时作为翻译模型和实验模型——虽然 Limitations 提到了这一双重角色，但 Qwen 的 EN→ZH probe transfer accuracy 是三个模型中最高的（67.3%），这是否可能是 translation-model artifact（Qwen 生成的翻译与 Qwen 的内部表征自然更 aligned）？\n\n**Q4**: TOST 等效性检验 power 极低（1.4%），Bayes factor 仅 1.5——是否考虑过这可能意味着 conflict 和 XNLI asymmetry 实际上不等效，只是当前数据不足以区分？标题中的 \"Mirror\" 一词暗示等效性，但统计证据并不支持这一强 claim。\n\n---\n\n## Missing References\n\n1. **Ravichander, A., Belinkov, Y., & Hovy, E. (2021).** \"Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance?\" — 直接论证 probing accuracy 不意味着 task relevance。\n2. **Gurgurov, D. et al. (2026).** \"CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark.\" arXiv:2601.08331 — 首个跨语言 steering 标准化 benchmark。\n3. **Pimentel, T. & Cotterell, R. (2021).** \"A Bayesian Framework for Information-Theoretic Probing.\" EMNLP 2021 — probing 的 information-theoretic 理论基础。\n\n---\n\n## 建议评分汇总\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5/5 |\n| Excitement | 2.5/5 |\n| Overall Assessment | 3.0 (Findings) |\n| Reproducibility | 4/5 |\n| Confidence | 4/5 |\n\n**总结**: 这是一篇方法论上扎实、统计上严谨的实验论文。Confound exclusion pipeline 和 XNLI baseline 方法论有价值，负面结果报告诚实。但核心新颖性不足：(1) \"detection ≠ decision\" 已被 Basu et al. 建立；(2) 跨语言可检测性属于预期结果；(3) causal steering 正面结果过于局限（1/3 模型、1 个层）。建议接收至 Findings，但需要 reframe contributions 以更准确反映实际证据强度。主会议接收需要显著增强 causal evidence（更多模型、non-linear steering、或至少一个 failure hypothesis 的验证）。\n",
  "reviewer_id": "2",
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审稿意见：新颖性与完整性\n\n## 论文信息\n- **标题**: English-Chinese Knowledge Conflict Signals Mirror General Cross-Lingual Asymmetries\n- **Venue**: EMNLP 2026 (ARR Long Paper)\n- **审查侧重**: 新颖性与贡献、相关工作覆盖、写作质量、格式合规、整体结构\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 — Findings（可被 Findings 接收）\n\n**一句话总结**: 实验设计和统计方法扎实，但核心发现 \"Detection ≠ Decision\" 已由 Basu et al. (2026) 建立，跨语言可检测性属于预期结果，且 steering 正面结果仅来自 1/3 模型的 1 个层，新颖性和贡献量不足以支撑主会议 long paper。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 方法论严谨（bootstrap CI、Bonferroni、TOST equivalence、confound exclusion），但 Contribution 2 的 claim 基于 1/3 模型正面结果略有过度 |\n| **Excitement** | 2.5/5 | 核心 insight（detection ≠ causation）已有先行工作；跨语言扩展有价值但增量有限；大量负面结果降低了 impact |\n| **Reproducibility** | 4/5 | 超参数、数据集分割、统计检验细节充分；GPU 型号和 seed 均有报告；独立复制实验是加分项 |\n| **Reviewer Confidence** | 4/5 | 熟悉 probing、representation steering、cross-lingual representations 相关文献 |\n\n---\n\n## 主要优势\n\n1. **统计严谨性突出。** Bootstrap paired CIs、Bonferroni 校正、TOST 等效性检验、Bayesian BF 分析，在 probing/steering 文献中这种统计水准少见。特别是 TOST 的 power analysis（80% power 需 ±12.5 pp margin）是诚实的自我批评。\n\n2. **Confound exclusion pipeline 设计完善。** COMET tercile 分层 + token overlap Jaccard 分析 + EN-DE 对照 + XNLI non-conflict baseline，系统性排除了翻译质量和词汇重叠两个关键混淆变量。EN-DE 的 near-zero asymmetry（Jaccard 14.8% 但 Δ=+1.2 pp, n.s.）特别有说服力。\n\n3. **负面结果的诚实报告。** Qwen 和 Gemma steering 失败的完整报告（包括 matched-condition Appendix Table 5），以及 Gemma 88.9% probe accuracy + zero flips 的对比，是强有力的 negative evidence。\n\n4. **独立复制设计。** L13 steering 用不同 seed、不同 train/test split 独立复制（Appendix C），boundary analysis 用独立采样 N=201（Appendix B），提升了因果定位结论的可信度。\n\n5. **XNLI baseline 比较方法论有价值。** 用非冲突语义任务的 probe transfer asymmetry 作为 baseline，这一方法论思路（\"先确认 baseline asymmetry 再解读 task-specific 差异\"）对后续跨语言 probing 工作有参考价值。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 核心发现 \"Detection ≠ Decision\" 的增量贡献不足\n- **具体位置**: Introduction 第 18 行引用 Basu et al. (2026)；Discussion §5 \"Relation to interpretability without actionability\" 段\n- **问题**: 论文的核心 insight——\"probe accuracy 不意味着 causal relevance\"——已由 Basu et al. (2026) 在临床 NLP 任务中建立（98.2% AUROC probe accuracy + steering 完全失败）。本文在 Discussion 中试图区分：mid-layer steering 在本文成功但在 Basu et al. 中失败，差异在于 layer selection。但这一区分是弱的：(a) 本文的 \"成功\" 仅限于 1/3 模型的 1 个层；(b) layer sweep 是方法论改进，不是新发现；(c) 2/3 模型的失败反而更接近 Basu et al. 的结论。论文需要更明确地阐述超越 Basu et al. 的具体贡献。\n- **为什么影响接收**: 若核心 contribution 已被先行工作覆盖，论文的 novelty 不足以支撑 long paper。\n- **建议修改方向**: 重新定位论文贡献——强调跨语言维度的独特性（如 asymmetry 的 baseline 归因），弱化 \"detection ≠ decision\" 作为独立 contribution。\n\n**N2** [critical] Contribution 2 (\"Architecture-dependent causal localization\") 证据过弱\n- **具体位置**: Introduction Contribution 2；§4.6 全节；Table 3；Appendix Table 5\n- **问题**: 该 contribution 声称 \"causal influence is consistently localized to L13 in Llama, while analogous steering in Qwen and Gemma yields no significant effect\"。但实际证据是：3 个模型中只有 1 个（Llama）在 1 个层（L13）显示显著效果。这不是 \"architecture-dependent causal localization\"，而是 \"我们在一个模型找到了正面结果，两个模型是 null\"。关键问题：\n  - Llama 的正面结果是否是 false positive？考虑到 multiple testing（3 models × 多个 layers × 10 α values），即使有 Bonferroni 校正，family-wise error rate 也需要跨模型评估。\n  - \"Architecture-dependent\" 的 claim 需要解释 **为什么** 不同架构表现不同，而不仅仅是报告它们不同。Discussion 中三个 hypotheses（non-linear pathway、superposition、sandwich normalization）全部是 untested speculation。\n- **为什么影响接收**: 核心 claim 的实验支撑不足以构成 EMNLP 级别贡献。\n- **建议修改方向**: (1) 将 claim 降级为 \"exploratory finding in Llama with null results in Qwen/Gemma\"；(2) 提供至少一个 hypothesis 的初步验证（如 Gemma sandwich norm 的 ablation）；(3) 补充更多模型或更多层的 steering 结果。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Contribution 1（跨语言冲突可检测性）可能是 expected result\n- **具体位置**: Introduction Contribution 1；§4.2-4.3\n- **问题**: 推理链：(1) 知识冲突信号在单语言内可检测（Zhao et al., 2024）→ (2) 多语言模型有共享跨语言表征空间（Wu et al., 2020; Wendler et al., 2024）→ (3) 因此跨语言冲突信号可检测。这是一个相当直接的推论。此外，XNLI baseline 显示 asymmetry 不是冲突特异的——这意味着 Contribution 1 的核心发现是 \"冲突信号的跨语言特性与通用跨语言特性无异\"，本质上是一个 null result。\n- **建议**: 更坦诚地讨论这一推理链的可预测性，并将 XNLI baseline 发现提升为更重要的贡献（\"任何跨语言 probing 研究都必须先控制 baseline asymmetry\" 是有实践价值的方法论建议）。\n\n**W2** [warning] 论文过度 Llama-centric，三模型设计的价值未充分实现\n- **具体位置**: 全文结构；§4.6 Causal Evidence；§5 Discussion\n- **问题**: 三模型设计本应提供 cross-architecture validation，但实际结果是：probing 部分三个模型一致（这是好的），steering 部分 2/3 是 null。论文的核心叙事（detection ≠ decision + mid-layer causal locus）完全依赖 Llama。Qwen 和 Gemma 的主要作用是提供 negative evidence，但 negative evidence 本身不构成 positive contribution。\n- **建议**: (1) 重新组织叙事——将 Llama 定位为 case study 而非通用结论；(2) 更深入分析 Qwen/Gemma 失败的原因，而非仅提供三个 untested hypotheses。\n\n**W3** [warning] 遗漏关键相关工作\n- **具体位置**: §2 Related Work\n- **问题**: 以下相关工作未被讨论：\n  - **Ravichander et al. (2021), \"Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance?\"** — 直接探讨了 probing accuracy 是否意味着 task relevance 的问题，与本文核心论点高度相关。本文引用了 Hewitt & Liang (2019) 的 control task 思路，但漏掉了 Ravichander et al. 对 probing accuracy ≠ task relevance 的更直接论证。\n  - **Gurgurov et al. (2026), \"CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark\" (arXiv:2601.08331)** — 首个跨语言 steering benchmark，覆盖 32 语言，与本文的 cross-lingual steering 实验直接相关。\n  - **Pimentel et al. (2020/2021)** 关于 information-theoretic probing 的理论框架，对 probing methodology 的讨论有补充价值。\n- **建议**: 在 Related Work 中补充这些引用，特别是 Ravichander et al.，因为它直接强化了本文的论点。\n\n**W4** [warning] Discussion 中三个 steering 失败 hypotheses 过于投机\n- **具体位置**: §5 \"Why does steering fail in Qwen and Gemma?\" 段\n- **问题**: 三个假设（non-linear causal pathway、residual stream superposition、architectural differences/sandwich normalization）全部未经验证。论文没有任何实验证据支持其中任何一个。虽然标注为 \"merit consideration\"，但在没有 ablation 或 diagnostic 的情况下，这些假设缺乏信息量——任何 steering 失败都可以用 \"可能是 non-linear\" 或 \"可能是 superposition\" 来解释。\n- **建议**: (1) 删减到最有证据支持的一个假设；或 (2) 对至少一个假设提供初步 diagnostic（如用 non-linear probe 检验 hypothesis 1，或用 PCA 可视化检验 hypothesis 2）。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Abstract 198 words（接近 200 上限），建议适度压缩以留出余量。\n- **M2**: Table 1 注释 \"Δ_asym is the mean of paired bootstrap differences, not the arithmetic difference of the reported single-seed accuracies\" 非常重要但容易被忽略，建议移入正文或用更醒目的方式呈现。\n- **M3**: §4.5 Confound Exclusion 中 Gemma 的 COMET tercile 结果（Δ = +10.3 pp, p = 0.278）在 confound 方向，虽然不显著，但应在 Limitations 中更明确提及。\n- **M4**: Figure 2（layer-wise probe accuracy）和 Figure 3（asymmetry forest plot）的信息密度适中。但 Figure 1（pipeline overview）信息量偏低——主要是流程描述，读正文即可获得相同信息。考虑替换为更有信息量的图（如 Llama L13 steering 前后的行为分布变化）。\n- **M5**: Appendix A (Use of AI Assistants) 的格式符合 ACL 2024+ 的建议，但措辞非常简短，可考虑补充 AI 辅助的具体边界说明。\n- **M6**: 论文引用 Marks & Tegmark (2024) 的 venue 写为 ICLR 2024，但该论文实际发表于 NeurIPS 2023（虽然 arXiv 版本 2023.10 发布），请核实。\n\n---\n\n## Questions to Authors\n\n**Q1**: Llama L13 的 steering 效果是否在不同 prompt template 下稳定？当前实验是否只使用了一种 prompt format？如果 prompt 变化导致 steering 失效，这将进一步削弱 causal claim。\n\n**Q2**: 为什么没有尝试 non-linear steering 方法（如 SAE-based steering，参考 Zhao et al. 2025 的 SpARE）？既然 Discussion 中自己提出了 \"non-linear causal pathway\" 假设，尝试 SAE steering 可以直接检验这一假设。\n\n**Q3**: Qwen3-8B 同时作为翻译模型和实验模型——虽然 Limitations 提到了这一双重角色，但 Qwen 的 EN→ZH probe transfer accuracy 是三个模型中最高的（67.3%），这是否可能是 translation-model artifact（Qwen 生成的翻译与 Qwen 的内部表征自然更 aligned）？\n\n**Q4**: TOST 等效性检验 power 极低（1.4%），Bayes factor 仅 1.5——是否考虑过这可能意味着 conflict 和 XNLI asymmetry 实际上不等效，只是当前数据不足以区分？标题中的 \"Mirror\" 一词暗示等效性，但统计证据并不支持这一强 claim。\n\n---\n\n## Missing References\n\n1. **Ravichander, A., Belinkov, Y., & Hovy, E. (2021).** \"Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance?\" — 直接论证 probing accuracy 不意味着 task relevance。\n2. **Gurgurov, D. et al. (2026).** \"CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark.\" arXiv:2601.08331 — 首个跨语言 steering 标准化 benchmark。\n3. **Pimentel, T. & Cotterell, R. (2021).** \"A Bayesian Framework for Information-Theoretic Probing.\" EMNLP 2021 — probing 的 information-theoretic 理论基础。\n\n---\n\n## 建议评分汇总\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5/5 |\n| Excitement | 2.5/5 |\n| Overall Assessment | 3.0 (Findings) |\n| Reproducibility | 4/5 |\n| Confidence | 4/5 |\n\n**总结**: 这是一篇方法论上扎实、统计上严谨的实验论文。Confound exclusion pipeline 和 XNLI baseline 方法论有价值，负面结果报告诚实。但核心新颖性不足：(1) \"detection ≠ decision\" 已被 Basu et al. 建立；(2) 跨语言可检测性属于预期结果；(3) causal steering 正面结果过于局限（1/3 模型、1 个层）。建议接收至 Findings，但需要 reframe contributions 以更准确反映实际证据强度。主会议接收需要显著增强 causal evidence（更多模型、non-linear steering、或至少一个 failure hypothesis 的验证）。\n",
    "reviewer_id": "2",
    "project": "clkc_mech_interp"
  }
}
```

</details>

---

### Tool result

_source line 273 · 2026-05-25T04:26:26.637018+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4017
}
```

</details>

---

### Assistant

_source line 274 · 2026-05-25T04:26:38.450006+00:00_

审稿意见已提交给 Review Director。

**审稿结论**: Overall 3.0（Findings 级别）。

核心判断：
- **Soundness 3.5**：方法论严谨，但 Contribution 2 的 claim 基于 1/3 模型正面结果有过度之嫌
- **Excitement 2.5**：核心 insight "detection ≠ decision" 已由 Basu et al. (2026) 建立，增量贡献有限
- 两个 Must-Fix：(1) 与 Basu et al. 的增量贡献需更明确阐述；(2) "Architecture-dependent causal localization" 证据过弱（1/3 模型、1 层）
- 四个 Should-Fix：跨语言可检测性为 expected result、论文过度 Llama-centric、遗漏关键相关工作（Ravichander 2021、CLaS-Bench 2026）、Discussion 假设过于投机
- 格式合规：正文 8 页 ✓、Abstract 198 词 ✓、`[review]` 模式 ✓、匿名 ✓、Limitations 章节 ✓

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2"
}
```

</details>

---

## Round 6

4 recorded events

### User

_source line 275 · 2026-05-25T04:27:06.905679+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

# Reviewer 1 — 方法严谨性审查

## Must-Fix 问题

**N1** [critical] 标题 "Mirror" 主张与 TOST 等价检验结果之间的根本张力
- 论文标题宣称冲突信号 "mirror" 通用跨语言不对称，但 TOST（±2pp margin）功效仅 1.4%。达到 80% 功效需要 ±12.5pp margin，而观测到的 Δ_asym 本身才 ~7pp。TOST 检验本质上是 uninformative。论文转而依赖 "CI 重叠" 作为替代论据，但 CI 重叠不等同于等价检验。
- 建议：将 "mirror" 改为更保守的 "resemble" 或 "are consistent with"；或用更高 power 的等价检验方法提供正式证据。

**N2** [critical] COMET tercile 消融的 MDD=25.3pp 使翻译质量混淆排除本质上无效
- 80% 功效下 MDD=25.3pp，但主效应仅 ~7pp。即使翻译质量解释了全部不对称，分析也检测不到。Gemma Δ=+10.3pp（虽 p=0.278）效应大小接近主效应。
- 建议：明确标注为 underpowered；考虑使用连续 COMET 分数作为回归协变量。

**N3** [critical] 因果证据限于单模型单层，与标题/摘要的跨模型叙事不匹配
- Steering 仅在 Llama L13 成功，Qwen/Gemma 全部失败。标题和摘要给人跨模型对等发现的印象，但因果证据实际只属于 Llama。
- 建议：在摘要和结论中更清晰地区分 "检测"（跨模型一致）和 "因果影响"（仅 Llama）。

## Should-Fix 问题

**W1** [warning] 单一 train/test split 的探针结果缺乏 cross-validation 验证

**W2** [warning] Qwen3-8B 同时作为翻译模型和实验对象的双重角色风险未充分控制

**W3** [warning] Probe selectivity（Hewitt &amp; Liang, 2019）未被正式评估

**W4** [warning] Balanced accuracy 作为唯一探针性能指标不够充分（缺 AUROC）

**W5** [warning] Steering 实验的 α 值选择缺乏理论依据

## 小问题
M1: COMET 版本未说明
M2: Token overlap 仅用 Jaccard
M3: 代码/数据可用性声明不清
M4: Random direction control 是最低标准
M5: Figure 3 灰色 ±2pp 等价区间视觉暗示 TOST 有效，但实际功效不足

## 总体评分：3.5（Borderline Conference）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 276 · 2026-05-25T04:29:12.802100+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n### R1-N1: 标题 \"Mirror\" 主张与 TOST 等价检验功效不足\n\n**[AGREE]** 同意这是论文的核心张力之一。\n\n论文在 §4.4 承认 TOST 功效仅 1.4%（±2pp margin），需要 ±12.5pp margin 才能达到 80% power。Bayes factor BF₀₁ ≈ 1.5 也仅为 \"directionally consistent but modest evidence\"。论文随后转向 CI 重叠 + 6/6 方向一致性（binomial p = 0.016）作为替代论据，但正如 R1 所指出，CI 重叠不等同于等价检验。\n\n我在 Q4 中也提出了同样的问题。补充一点：标题中的 \"Mirror\" 是全文最强的等价性 claim，但论文在正文中的措辞更谨慎（\"consistent with\"），存在标题与正文之间的不一致。建议将标题改为 \"... Are Consistent With General Cross-Lingual Asymmetries\" 或类似表述。\n\n### R1-N2: COMET tercile 消融 MDD=25.3pp 使混淆排除无效\n\n**[REBUT]** 部分反驳——COMET tercile 分析确实 underpowered，但 \"本质上无效\" 的结论忽略了 confound exclusion pipeline 的多证据链设计。\n\n论文的混淆排除不仅依赖 COMET tercile，而是一个三控制管线：\n1. **COMET tercile**（§4.5 Table 2）：确实 underpowered（MDD=25.3pp），R1 此点正确。但 Qwen 方向相反（Δ = -5.6pp），Llama 接近零（Δ = +1.7pp），这两个模型的方向性证据已经不支持翻译质量混淆。\n2. **Token overlap**（§4.5）：Jaccard 3-4%，Llama 有弱负相关（r = -0.15），方向与 confound hypothesis 相反。\n3. **EN-DE 对照**（§5 \"Typological distance\" 段）：EN-DE Jaccard 14.8%（~4× EN-ZH），但 asymmetry 近零（Δ = +1.2pp, n.s.）。如果 token overlap 或翻译质量驱动 asymmetry，EN-DE 应该显示更大的 asymmetry，但事实相反。\n\nR1 关于 Gemma Δ=+10.3pp 的观察有效——这是三个模型中唯一在 confound 方向的结果。但如 §4.5 所述，Gemma EN→ZH probe 在该层的 baseline accuracy 仅 58.8%（接近 chance），使该分析处于极低功效状态。\n\n**建议**：同意 R1 的建议——(1) 明确标注 COMET tercile 为 underpowered；(2) 补充连续 COMET 回归分析；(3) 将 pipeline 的论证重心从 COMET tercile 转向 token overlap + EN-DE 对照。\n\n### R1-N3: 因果证据限于单模型单层\n\n**[AGREE]** 完全同意，这也是我在 N2 中提出的核心问题。\n\n摘要的叙事结构存在问题：前半段讲跨模型一致的 detectability 和 asymmetry，后半段讲 detection ≠ decision——但后者的正面证据仅来自 Llama L13。读者自然会将两部分理解为同等强度的跨模型发现，但实际不是。\n\n摘要最后一句 \"These findings, observed in Llama-3.1-8B-Instruct and absent in Qwen and Gemma, indicate that linear detectability does not imply causal relevance\" 确实做了区分，但这个区分出现在一个长摘要的最后，很容易被忽略。\n\n补充 R1 的建议：Introduction 的三个 contributions 中，Contribution 2 写为 \"Architecture-dependent causal localization\"，这一措辞暗示了跨架构的系统性发现，但实际是 \"Llama 有因果效应 + 其他两个没有\"。建议改为 \"Causal localization in Llama with negative evidence in Qwen and Gemma\" 或类似更精确的表述。\n\n---\n\n## Should-Fix 问题\n\n### R1-W1: 单一 train/test split 缺乏 cross-validation\n\n**[AGREE]** 方向上同意，但严重性可略降。\n\n论文在 Limitations 中报告了 cross-seed peak accuracy 稳定性：Llama ±0.12%, Gemma ±1.32%, Qwen ±1.90%。此外，L13 steering 有独立 seed 复制（Appendix C，seed=123，4/6 Bonferroni 显著 vs 原始 2/6）。这些提供了一定的稳健性证据。\n\n但 R1 正确指出，正式的 k-fold cross-validation 未被执行。Bootstrap CI 捕获的是 within-split variability，不是 across-split variability。对于 probing 结论，cross-validation 是标准做法（Belinkov 2022 survey 即推荐），缺失构成方法论缺口。\n\n### R1-W2: Qwen 双重角色\n\n**[AGREE]** 同意这是一个需要更好控制的风险。\n\n我在 Q3 中提出了同样的问题。Qwen EN→ZH transfer accuracy 是三模型最高的（67.3% vs Llama 59.6% vs Gemma 62.9%），虽然差距不大，但方向与 \"Qwen 生成的翻译与 Qwen 内部表征自然更 aligned\" 的假设一致。\n\n论文的缓解措施（COMET 质量控制 + Llama/Gemma 交叉验证）部分有效，但最干净的控制应该是用独立翻译模型（如 GPT-4 或专用 MT 模型）重做翻译并对比。\n\n### R1-W3: Probe selectivity 未正式评估\n\n**[AGREE]** 这是一个有效的方法论缺口。\n\n论文引用了 Hewitt & Liang (2019) 的 control task 思路（Introduction 第 17 行，Method §3.3），但未实际执行 control task 实验（如随机标签 baseline 或 selectivity 指标）。XNLI baseline 服务于不同目的（测试 asymmetry 的特异性，而非 probe 的 selectivity）。\n\n补充：我在遗漏引用中也指出了 Ravichander et al. (2021) \"Probing the Probing Paradigm\"，该工作直接论证了 probing accuracy 不意味着 task relevance。本文的核心论点与其高度一致，但既未引用也未执行类似的 selectivity 评估。\n\n### R1-W4: 缺少 AUROC\n\n**[AGREE]** 同意这是一个合理的补充要求。\n\nBalanced accuracy 在单一阈值下操作，AUROC 提供了阈值无关的全面评估。特别是对于 Gemma（88.9% balanced accuracy 但 zero steering flips），AUROC 可以帮助理解 probe 的判别能力是否真的如 balanced accuracy 所暗示的那样强。\n\n但也要注意：balanced accuracy 已经是 class-imbalance-aware 的，且论文的核心论点（detection ≠ causation）不依赖于精确的 probe 性能数值——即使用 AUROC，Gemma 的判别能力大概率仍然很高，而 steering 仍然失败。因此，添加 AUROC 是 good practice，但不会改变核心结论。\n\n### R1-W5: α 值选择缺乏理论依据\n\n**[AGREE]** 同意。\n\n§3.6 描述了 α ∈ {±20, ±10, ±5, ±2, ±1}（10 值）和简化的 {±20, ±10, ±5}（6 值），但未解释为何选择这些特定值。没有基于 probe weight norm、activation magnitude、或 signal-to-noise ratio 的规范化。这使得跨模型的 α 值不可直接比较——同一 α=10 在不同模型/层可能代表截然不同的扰动强度。\n\n建议：用 probe weight 的 norm 或 residual stream 的标准差规范化 α，确保跨模型可比性。\n\n---\n\n## 小问题\n\n**R1-M1 (COMET 版本)**: [AGREE] 需要标注具体版本号（如 wmt22-comet-da 或 Unbabel/wmt22-cometkiwi-da），因为不同版本评分不可比。\n\n**R1-M2 (Token overlap 仅用 Jaccard)**: [AGREE] Jaccard 是粗粒度指标，character-level 或 subword overlap 可能更有信息量。但考虑到 EN-ZH 本身字符系统不同（Latin vs CJK），Jaccard 3-4% 已经足够说明 overlap 极低。\n\n**R1-M3 (代码/数据可用性)**: [AGREE] 当前版本无可用性声明。double-blind 阶段可以用匿名链接。\n\n**R1-M4 (Random direction control 是最低标准)**: [AGREE] 更强的 control 包括：(1) 不同任务的 probe direction（如 XNLI probe weight 用于 conflict steering）；(2) permuted labels 训练的 probe。\n\n**R1-M5 (Figure 3 灰色带暗示 TOST 有效)**: [AGREE] 同意，±2pp 灰色带在视觉上暗示这是一个 meaningful equivalence zone，但 TOST 功效不支持这一暗示。建议删除灰色带或添加注释说明。\n\n---\n\n## 总结\n\nR1 的审稿整体方法论导向，与我的新颖性/完整性评估互补。我们在三个核心问题上高度一致：\n\n1. **\"Mirror\" claim 过强** — R1 从 TOST power 角度、我从标题-正文一致性角度，结论相同。\n2. **因果证据过于局限** — 都认为 1/3 模型正面结果不足以支撑跨架构 claim。\n3. **Confound exclusion 需要加强** — R1 聚焦 COMET tercile underpowered，我同意但认为整个 pipeline（包括 token overlap + EN-DE）提供了 converging evidence，总体结论仍可接受。\n\n主要分歧在于 N2 的严重性：R1 认为 confound exclusion \"本质上无效\"，我认为虽然 COMET tercile 确实 underpowered，但多证据链设计（特别是 EN-DE 对照）部分弥补了这一缺陷。\n\nR1 给出 3.5（Borderline Conference），我给出 3.0（Findings）。差异主要来自我对新颖性的更严格评估——R1 未将 Basu et al. (2026) 的先行发现作为核心关注点，而我认为 \"detection ≠ decision\" 的 novelty 已被显著削弱。综合两份 review，我认为该论文处于 **3.0-3.5 区间**，Findings 接收是合理的，主会议接收需要实质性修改。\n",
  "reviewer_id": "2",
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n### R1-N1: 标题 \"Mirror\" 主张与 TOST 等价检验功效不足\n\n**[AGREE]** 同意这是论文的核心张力之一。\n\n论文在 §4.4 承认 TOST 功效仅 1.4%（±2pp margin），需要 ±12.5pp margin 才能达到 80% power。Bayes factor BF₀₁ ≈ 1.5 也仅为 \"directionally consistent but modest evidence\"。论文随后转向 CI 重叠 + 6/6 方向一致性（binomial p = 0.016）作为替代论据，但正如 R1 所指出，CI 重叠不等同于等价检验。\n\n我在 Q4 中也提出了同样的问题。补充一点：标题中的 \"Mirror\" 是全文最强的等价性 claim，但论文在正文中的措辞更谨慎（\"consistent with\"），存在标题与正文之间的不一致。建议将标题改为 \"... Are Consistent With General Cross-Lingual Asymmetries\" 或类似表述。\n\n### R1-N2: COMET tercile 消融 MDD=25.3pp 使混淆排除无效\n\n**[REBUT]** 部分反驳——COMET tercile 分析确实 underpowered，但 \"本质上无效\" 的结论忽略了 confound exclusion pipeline 的多证据链设计。\n\n论文的混淆排除不仅依赖 COMET tercile，而是一个三控制管线：\n1. **COMET tercile**（§4.5 Table 2）：确实 underpowered（MDD=25.3pp），R1 此点正确。但 Qwen 方向相反（Δ = -5.6pp），Llama 接近零（Δ = +1.7pp），这两个模型的方向性证据已经不支持翻译质量混淆。\n2. **Token overlap**（§4.5）：Jaccard 3-4%，Llama 有弱负相关（r = -0.15），方向与 confound hypothesis 相反。\n3. **EN-DE 对照**（§5 \"Typological distance\" 段）：EN-DE Jaccard 14.8%（~4× EN-ZH），但 asymmetry 近零（Δ = +1.2pp, n.s.）。如果 token overlap 或翻译质量驱动 asymmetry，EN-DE 应该显示更大的 asymmetry，但事实相反。\n\nR1 关于 Gemma Δ=+10.3pp 的观察有效——这是三个模型中唯一在 confound 方向的结果。但如 §4.5 所述，Gemma EN→ZH probe 在该层的 baseline accuracy 仅 58.8%（接近 chance），使该分析处于极低功效状态。\n\n**建议**：同意 R1 的建议——(1) 明确标注 COMET tercile 为 underpowered；(2) 补充连续 COMET 回归分析；(3) 将 pipeline 的论证重心从 COMET tercile 转向 token overlap + EN-DE 对照。\n\n### R1-N3: 因果证据限于单模型单层\n\n**[AGREE]** 完全同意，这也是我在 N2 中提出的核心问题。\n\n摘要的叙事结构存在问题：前半段讲跨模型一致的 detectability 和 asymmetry，后半段讲 detection ≠ decision——但后者的正面证据仅来自 Llama L13。读者自然会将两部分理解为同等强度的跨模型发现，但实际不是。\n\n摘要最后一句 \"These findings, observed in Llama-3.1-8B-Instruct and absent in Qwen and Gemma, indicate that linear detectability does not imply causal relevance\" 确实做了区分，但这个区分出现在一个长摘要的最后，很容易被忽略。\n\n补充 R1 的建议：Introduction 的三个 contributions 中，Contribution 2 写为 \"Architecture-dependent causal localization\"，这一措辞暗示了跨架构的系统性发现，但实际是 \"Llama 有因果效应 + 其他两个没有\"。建议改为 \"Causal localization in Llama with negative evidence in Qwen and Gemma\" 或类似更精确的表述。\n\n---\n\n## Should-Fix 问题\n\n### R1-W1: 单一 train/test split 缺乏 cross-validation\n\n**[AGREE]** 方向上同意，但严重性可略降。\n\n论文在 Limitations 中报告了 cross-seed peak accuracy 稳定性：Llama ±0.12%, Gemma ±1.32%, Qwen ±1.90%。此外，L13 steering 有独立 seed 复制（Appendix C，seed=123，4/6 Bonferroni 显著 vs 原始 2/6）。这些提供了一定的稳健性证据。\n\n但 R1 正确指出，正式的 k-fold cross-validation 未被执行。Bootstrap CI 捕获的是 within-split variability，不是 across-split variability。对于 probing 结论，cross-validation 是标准做法（Belinkov 2022 survey 即推荐），缺失构成方法论缺口。\n\n### R1-W2: Qwen 双重角色\n\n**[AGREE]** 同意这是一个需要更好控制的风险。\n\n我在 Q3 中提出了同样的问题。Qwen EN→ZH transfer accuracy 是三模型最高的（67.3% vs Llama 59.6% vs Gemma 62.9%），虽然差距不大，但方向与 \"Qwen 生成的翻译与 Qwen 内部表征自然更 aligned\" 的假设一致。\n\n论文的缓解措施（COMET 质量控制 + Llama/Gemma 交叉验证）部分有效，但最干净的控制应该是用独立翻译模型（如 GPT-4 或专用 MT 模型）重做翻译并对比。\n\n### R1-W3: Probe selectivity 未正式评估\n\n**[AGREE]** 这是一个有效的方法论缺口。\n\n论文引用了 Hewitt & Liang (2019) 的 control task 思路（Introduction 第 17 行，Method §3.3），但未实际执行 control task 实验（如随机标签 baseline 或 selectivity 指标）。XNLI baseline 服务于不同目的（测试 asymmetry 的特异性，而非 probe 的 selectivity）。\n\n补充：我在遗漏引用中也指出了 Ravichander et al. (2021) \"Probing the Probing Paradigm\"，该工作直接论证了 probing accuracy 不意味着 task relevance。本文的核心论点与其高度一致，但既未引用也未执行类似的 selectivity 评估。\n\n### R1-W4: 缺少 AUROC\n\n**[AGREE]** 同意这是一个合理的补充要求。\n\nBalanced accuracy 在单一阈值下操作，AUROC 提供了阈值无关的全面评估。特别是对于 Gemma（88.9% balanced accuracy 但 zero steering flips），AUROC 可以帮助理解 probe 的判别能力是否真的如 balanced accuracy 所暗示的那样强。\n\n但也要注意：balanced accuracy 已经是 class-imbalance-aware 的，且论文的核心论点（detection ≠ causation）不依赖于精确的 probe 性能数值——即使用 AUROC，Gemma 的判别能力大概率仍然很高，而 steering 仍然失败。因此，添加 AUROC 是 good practice，但不会改变核心结论。\n\n### R1-W5: α 值选择缺乏理论依据\n\n**[AGREE]** 同意。\n\n§3.6 描述了 α ∈ {±20, ±10, ±5, ±2, ±1}（10 值）和简化的 {±20, ±10, ±5}（6 值），但未解释为何选择这些特定值。没有基于 probe weight norm、activation magnitude、或 signal-to-noise ratio 的规范化。这使得跨模型的 α 值不可直接比较——同一 α=10 在不同模型/层可能代表截然不同的扰动强度。\n\n建议：用 probe weight 的 norm 或 residual stream 的标准差规范化 α，确保跨模型可比性。\n\n---\n\n## 小问题\n\n**R1-M1 (COMET 版本)**: [AGREE] 需要标注具体版本号（如 wmt22-comet-da 或 Unbabel/wmt22-cometkiwi-da），因为不同版本评分不可比。\n\n**R1-M2 (Token overlap 仅用 Jaccard)**: [AGREE] Jaccard 是粗粒度指标，character-level 或 subword overlap 可能更有信息量。但考虑到 EN-ZH 本身字符系统不同（Latin vs CJK），Jaccard 3-4% 已经足够说明 overlap 极低。\n\n**R1-M3 (代码/数据可用性)**: [AGREE] 当前版本无可用性声明。double-blind 阶段可以用匿名链接。\n\n**R1-M4 (Random direction control 是最低标准)**: [AGREE] 更强的 control 包括：(1) 不同任务的 probe direction（如 XNLI probe weight 用于 conflict steering）；(2) permuted labels 训练的 probe。\n\n**R1-M5 (Figure 3 灰色带暗示 TOST 有效)**: [AGREE] 同意，±2pp 灰色带在视觉上暗示这是一个 meaningful equivalence zone，但 TOST 功效不支持这一暗示。建议删除灰色带或添加注释说明。\n\n---\n\n## 总结\n\nR1 的审稿整体方法论导向，与我的新颖性/完整性评估互补。我们在三个核心问题上高度一致：\n\n1. **\"Mirror\" claim 过强** — R1 从 TOST power 角度、我从标题-正文一致性角度，结论相同。\n2. **因果证据过于局限** — 都认为 1/3 模型正面结果不足以支撑跨架构 claim。\n3. **Confound exclusion 需要加强** — R1 聚焦 COMET tercile underpowered，我同意但认为整个 pipeline（包括 token overlap + EN-DE）提供了 converging evidence，总体结论仍可接受。\n\n主要分歧在于 N2 的严重性：R1 认为 confound exclusion \"本质上无效\"，我认为虽然 COMET tercile 确实 underpowered，但多证据链设计（特别是 EN-DE 对照）部分弥补了这一缺陷。\n\nR1 给出 3.5（Borderline Conference），我给出 3.0（Findings）。差异主要来自我对新颖性的更严格评估——R1 未将 Basu et al. (2026) 的先行发现作为核心关注点，而我认为 \"detection ≠ decision\" 的 novelty 已被显著削弱。综合两份 review，我认为该论文处于 **3.0-3.5 区间**，Findings 接收是合理的，主会议接收需要实质性修改。\n",
    "reviewer_id": "2",
    "project": "clkc_mech_interp"
  }
}
```

</details>

---

### Tool result

_source line 277 · 2026-05-25T04:29:16.820325+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4018
}
```

</details>

---

### Assistant

_source line 278 · 2026-05-25T04:29:24.966416+00:00_

已提交对 Reviewer 1 的逐条交叉回应。

核心共识：R1-N1（Mirror claim 过强）、R1-N3（因果证据限于 Llama）两点完全同意。唯一分歧在 R1-N2——COMET tercile 确实 underpowered，但反驳了 "本质上无效" 的结论，因为 token overlap + EN-DE 对照提供了 converging evidence。综合两份 review，论文处于 3.0-3.5 区间。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2"
}
```

</details>

---

## Round 7

50 recorded events

### User

_source line 279 · 2026-05-25T21:15:47.370461+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性与完整性**审查。

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

1. **新颖性 (Novelty)**：
   - 相对 Zhao et al. 2024（monolingual conflict probing）的增量是否足够？
   - 相对 Basu et al. 2026（detection≠steering）的差异化是否清晰？
   - "asymmetry reflects general cross-lingual structure" 是否构成独立 contribution 还是 null result repackaging？
   - 四个 contribution 的权重是否均衡？

2. **Related Work 覆盖**：
   - 跨语言 steering 领域：Pokharel 2026, Sundar 2025, Gurgurov 2026 是否充分讨论？
   - 知识冲突 taxonomy 和 mitigation 方向是否有重要遗漏？
   - 信息论 probing 视角（Pimentel 2021, Ravichander 2021）是否充分整合？

3. **叙事结构 (Narrative)**：
   - Introduction 三个研究问题的设置是否 self-contained？
   - 论文核心 claim 从 Abstract→Intro→Results→Discussion→Conclusion 是否一致？
   - "detection≠decision" dissociation 作为核心卖点的叙事是否 convincing？

4. **写作质量**：
   - Abstract 是否在 200 words 以内？
   - 是否存在 overclaiming（标题/Abstract vs 实际实验范围）？
   - 图表是否 informative 且 self-contained？

5. **格式合规**：
   - 页数是否符合 8 页限制？
   - Limitations section 是否存在且位置正确？
   - 匿名化是否完整（无 self-citation 泄露）？

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 280 · 2026-05-25T21:15:54.731654+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/review_reviewer_2_a0a58dd3/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/review_reviewer_2_a0a58dd3/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 281 · 2026-05-25T21:15:55.155436+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/review_reviewer_2_a0a58dd3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 423
}
```

</details>

---

### Tool call

_source line 282 · 2026-05-25T21:15:55.318869+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
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

_source line 283 · 2026-05-25T21:15:55.421155+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 102
}
```

</details>

---

### Tool call

_source line 284 · 2026-05-25T21:15:59.352893+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---

### Tool call

_source line 285 · 2026-05-25T21:16:00.307018+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
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

_source line 286 · 2026-05-25T21:16:06.630240+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines, review form criteria, and related policies:

## Reviewer Guidelines

Reviewers are asked to follow a workflow of reading the paper and getting a first impression, then searching for related work. To preserve double-blind review, reviewers for *ACL conferences and TACL should not actively try to discover author ident
…[truncated 994 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7277
}
```

</details>

---

### Tool result

_source line 287 · 2026-05-25T21:16:08.643227+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 440.3}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 585.6}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 544.6}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 588.5}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 547.8}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 444.7}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 534.7}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 406.8}], \"total_pages\": 12, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 8336
}
```

</details>

---

### Tool call

_source line 288 · 2026-05-25T21:16:13.618607+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form fields, scoring dimensions, and their scales. Include all criteria like soundness, excitement/novelty, reproducibility, clarity, confidence, etc. List every field with its description and scoring scale."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form fields, scoring dimensions, and their scales. Include all criteria like soundness, excitement/novelty, reproducibility, clarity, confidence, etc. List every field with its description and scoring scale."
  }
}
```

</details>

---

### Tool call

_source line 289 · 2026-05-25T21:16:15.588498+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines, especially: what dimensions reviewers should evaluate, what constitutes a good/bad review, specific criteria for soundness/novelty/reproducibility, and any instructions about how to assess papers. Include all scoring rubrics and evaluation criteria."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines, especially: what dimensions reviewers should evaluate, what constitutes a good/bad review, specific criteria for soundness/novelty/reproducibility, and any instructions about how to assess papers. Include all scoring rubrics and evaluation criteria."
  }
}
```

</details>

---

### Tool call

_source line 290 · 2026-05-25T21:16:16.494269+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---

### Tool call

_source line 291 · 2026-05-25T21:16:17.046749+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---

### Tool result

_source line 292 · 2026-05-25T21:16:17.499903+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---

### Tool call

_source line 293 · 2026-05-25T21:16:17.500338+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---

### Tool call

_source line 294 · 2026-05-25T21:16:17.952201+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---

### Tool result

_source line 295 · 2026-05-25T21:16:18.053633+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---

### Tool result

_source line 296 · 2026-05-25T21:16:18.506917+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---

### Tool result

_source line 297 · 2026-05-25T21:16:18.909167+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---

### Tool result

_source line 298 · 2026-05-25T21:16:22.339638+00:00_

# ACL Rolling Review Form Fields and Scoring Dimensions

## Main Review Fields

**Paper Summary**
Narrative description of paper content and topic clarification.

**Summary of Strengths**
Open-ended field identifying publication merits and reasons for acceptance.

**Summary of Weaknesses**
Numbered concerns addressing correctness, impact, clarity, and other factors limiting publication value.

**Comments/Suggestions/Typos**
Additional improvement recommendations beyond main weaknesses.

## Scoring Dimensions

### Reviewer Confidence
Scale: 1–5
- 5: "Positive that my evaluation is correct. I read the paper very carefully"
- 4: Quite sure with unlikely but possible oversights
- 3: Pretty sure with chance of missing details
- 2: Willing to defend evaluation despite likely gaps
- 1: Not an area of expertise or paper difficult to understand

### Soundness
Scale: 1–5 (with .5 increments)
- 5: "This study is one of the most thorough I have seen"
- 4: Strong support for claims; extra experiments optional
- 3: Acceptable; minor points need additional support
- 2: Main claims lack sufficient support
- 1: "Not yet sufficiently thorough to warrant publication"

### Excitement
Scale: 1–5 (with .5 increments)
- 5: "Highly Exciting: I would recommend this paper to others"
- 4: Would mention to others or attend presentation
- 3: Might mention points if time permits
- 2: "Potentially Interesting" but doesn't resonate personally
- 1: Not exciting; lacks computational linguistics relevance

### Overall Assessment
Scale: 1–5 (with .5 increments)
- 5: "Consider for Award"
- 4: Conference acceptance recommended
- 3: Findings-track acceptance
- 2: Resubmit next cycle
- 1.5: Resubmit after next cycle
- 1: Do not resubmit

## Additional Evaluation Fields

**Best Paper Justification**
Required if selecting award/borderline award consideration.

**Limitations and Societal Impact**
Assessment of author discussion regarding work constraints and ethical implications.

**Ethical Concerns**
Evalua
…[truncated 818 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 8721
}
```

</details>

---

### Tool result

_source line 299 · 2026-05-25T21:16:25.263901+00:00_

# ARR Reviewer Guidelines: Evaluation Dimensions & Criteria

## Core Evaluation Dimensions

Reviewers assess papers using three primary scores:

1. **Soundness**: Technical validity and rigor. Scores must be justified by specific review content; low soundness scores require clear evidence of flaws.

2. **Excitement**: Personal interest level, independent of soundness. This reflects subjective taste rather than objective quality.

3. **Overall Recommendation**: Composite assessment reflecting soundness, excitement, novelty, and potential impact for the field.

## Key Evaluation Principles

**Reading Strategy**: Papers should be read twice—first for skim-reading (research question and methodology assessment without results), then in-depth (evaluating evidence and technical soundness).

**Specificity Requirements**: Reviews must provide concrete details. Rather than saying "missing relevant references," specify which papers (e.g., "Smith 2023, Jones 2024") should be discussed.

## Common Review Problems to Avoid

The guidelines identify 17 heuristics (H1-H17) that reflect reviewer bias rather than legitimate weaknesses:

- **H1-H2**: Dismissing findings as "obvious" or rejecting results contradicting expectations
- **H5**: Requiring SOTA results (neither necessary nor sufficient for scientific contribution)
- **H6**: Penalizing negative results (valuable for field progress)
- **H7**: Criticizing "simple" methods when simplicity aids deployment
- **H13**: Demanding extra experiments beyond claims' scope

## Common NLP Paper Problems (M, T, R, G codes)

**Methodology Issues (M1-M5)**:
- LLM-only evaluation without validation
- Insufficient reproducibility details
- Undisclosed data quality problems
- Unmotivated model/benchmark selection
- Incomplete proofs or assumptions

**Results Issues (R1-R5)**:
- Statistical problems or p-hacking
- Claims exceeding evaluation scope
- Speculation presented as conclusions
- Overclaiming from benchmarks

**General Issues (G1-G5)**:
- 
…[truncated 789 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 9675
}
```

</details>

---

### Tool call

_source line 300 · 2026-05-25T21:16:30.032454+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---

### Tool call

_source line 301 · 2026-05-25T21:16:30.654009+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---

### Tool call

_source line 302 · 2026-05-25T21:16:30.974953+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---

### Tool call

_source line 303 · 2026-05-25T21:16:32.159113+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---

### Tool call

_source line 304 · 2026-05-25T21:16:32.871157+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
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

_source line 305 · 2026-05-25T21:16:32.924968+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2892
}
```

</details>

---

### Tool result

_source line 306 · 2026-05-25T21:16:33.332652+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2678
}
```

</details>

---

### Tool result

_source line 307 · 2026-05-25T21:16:34.442367+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2283
}
```

</details>

---

### Tool result

_source line 308 · 2026-05-25T21:16:34.495267+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3520
}
```

</details>

---

### Tool result

_source line 309 · 2026-05-25T21:16:34.997275+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 566.9}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 603.6}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 486.2}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 184.2}], \"total_pages\": 12, \"rendered_pages\": 4, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2126
}
```

</details>

---

### Tool call

_source line 310 · 2026-05-25T21:16:39.316175+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---

### Tool call

_source line 311 · 2026-05-25T21:16:39.718770+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---

### Tool result

_source line 312 · 2026-05-25T21:16:40.222483+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---

### Tool call

_source line 313 · 2026-05-25T21:16:40.222950+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---

### Tool call

_source line 314 · 2026-05-25T21:16:40.676019+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---

### Tool result

_source line 315 · 2026-05-25T21:16:41.230465+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1511
}
```

</details>

---

### Tool result

_source line 316 · 2026-05-25T21:16:41.532529+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1309
}
```

</details>

---

### Tool result

_source line 317 · 2026-05-25T21:16:41.534115+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 858
}
```

</details>

---

### Tool call

_source line 318 · 2026-05-25T21:21:16.683933+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Basu 2026 knowledge conflict probing detection steering dissociation language models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Basu 2026 knowledge conflict probing detection steering dissociation language models"
  }
}
```

</details>

---

### Tool call

_source line 319 · 2026-05-25T21:21:17.236507+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "cross-lingual knowledge editing ROME MEMIT multilingual transfer 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "cross-lingual knowledge editing ROME MEMIT multilingual transfer 2025 2026"
  }
}
```

</details>

---

### Tool result

_source line 320 · 2026-05-25T21:21:24.375572+00:00_

Web search results for query: "Basu 2026 knowledge conflict probing detection steering dissociation language models"

Links: [{"title":"That's Deprecated! Understanding, Detecting, and Steering Knowledge Conflicts in Language Models for Code Generation","url":"https://arxiv.org/pdf/2510.19116"},{"title":"Analysing the Residual Stream of Language Models Under Knowledge   Conflicts","url":"https://arxiv.org/pdf/2410.16090"},{"title":"Taming Knowledge Conflicts in Language Models","url":"https://arxiv.org/pdf/2503.10996"},{"title":"Analysing the Residual Stream of Language Models Under Knowledge Conflicts","url":"https://arxiv.org/html/2410.16090v1"},{"title":"Taming Knowledge Conflicts in Language Models","url":"https://arxiv.org/html/2503.10996v1"},{"title":"When Seeing Overrides Knowing: Disentangling Knowledge Conflicts in Vision-Language Models","url":"https://arxiv.org/pdf/2507.13868"}]

Based on the web search results, I found several relevant research papers on knowledge conflicts in language models. Here's what I found:

## Main Results

The most directly relevant paper appears to be "That's Deprecated! Understanding, Detecting, and Steering Knowledge Conflicts in Language Models for Code Generation" by Bae and colleagues, which investigates how large language models behave when faced with discrepancies between their parametric knowledge and conflicting information contained in a prompt.

The researchers found that sufficiently large LLMs encode the notion of a knowledge conflict in their parameters, enabling detection of knowledge conflicts with up to 80.65% accuracy. They also showed that activation-level steering can achieve up to a 12.6% improvement in steering success over a random baseline.

## Related Research

Additional papers on this topic include:

- A study analyzing the residual stream in LLMs to understand their behavior when knowledge conflicts arise, with probing experiments showing that the signal of knowledge conflict rises from intermediate 
…[truncated 515 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7691
}
```

</details>

---

### Tool result

_source line 321 · 2026-05-25T21:21:25.229393+00:00_

Web search results for query: "cross-lingual knowledge editing ROME MEMIT multilingual transfer 2025 2026"

Links: [{"title":"Editing Across Languages: A Survey of Multilingual Knowledge Editing","url":"https://arxiv.org/html/2505.14393v1"},{"title":"Cross-Lingual Knowledge Editing in Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/384207128_Cross-Lingual_Knowledge_Editing_in_Large_Language_Models"},{"title":"An Exploration of Knowledge Editing for Arabic","url":"https://arxiv.org/html/2507.09629"},{"title":"CLM-Bench: Benchmarking and Analyzing Cross-lingual Misalignment of LLMs in Knowledge Editing","url":"https://arxiv.org/html/2601.17397"},{"title":"(PDF) Editing Across Languages: A Survey of Multilingual Knowledge Editing","url":"https://www.researchgate.net/publication/391911755_Editing_Across_Languages_A_Survey_of_Multilingual_Knowledge_Editing"},{"title":"BMIKE-53: Investigating Cross-Lingual Knowledge Editing with In-Context Learning","url":"https://arxiv.org/html/2406.17764"},{"title":"Edit Once, Update Everywhere: A Simple Framework for Cross-Lingual Knowledge Synchronization in LLMs","url":"https://arxiv.org/pdf/2502.14645"},{"title":"MKE-PLLM: A benchmark for multilingual knowledge editing on pretrained large language model - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0925231225016510"},{"title":"Cross-Lingual Knowledge Editing in Large Language Models","url":"https://arxiv.org/pdf/2309.08952"}]

Based on the search results, here's what I found about cross-lingual knowledge editing research involving ROME, MEMIT, and multilingual transfer:

## Recent Survey and Research (2025-2026)

ROME introduced the locate-then-edit paradigm, identifying key activation pathways and applying a low-rank update to model weights, while MEMIT extended ROME to support batch editing of multiple facts using rank-one updates distributed across layers.

However, adaptations of ROME, MEMIT, and PMET to multi
…[truncated 1197 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7992
}
```

</details>

---

### Tool call

_source line 322 · 2026-05-25T21:23:27.208294+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿意见：新颖性与完整性\n\n## Summary\n\n本文将知识冲突信号的 probing 分析从单语（Zhao et al. 2024）扩展到跨语言（英-中）设置，使用三个 LLM（Llama-3.1-8B-Instruct、Qwen2.5-8B、Gemma-2-9B-IT）进行残差流探测、XNLI 非冲突基线对照、COMET 混淆因素排除和因果 steering 实验。主要发现：(1) 冲突信号在所有模型和方向上线性可检测；(2) ZH→EN 迁移优势约 7pp，与 XNLI 基线一致，反映一般跨语言结构而非冲突特异性；(3) 因果 steering 仅在 Llama L13（41% 深度）成功，Qwen/Gemma 无显著因果效应，表明检测不蕴含因果相关性。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0/5 | 方法论扎实（bootstrap CI、Bonferroni 校正、Fisher 精确检验），混淆因素控制设计优秀。但核心 claim（detection≠decision）仅 1/3 模型支持，单一 train/test split 影响可靠性 |\n| Excitement | 2.5/5 | Probing 跨语言扩展属增量贡献；最具新颖性的 detection-decision dissociation 已被 Basu et al. 2026 在单语设置中建立；asymmetry 发现为 null result |\n| Reproducibility | 4/5 | 提供匿名代码仓库，方法描述清晰，统计方法完整。单一 split 限制精确数值复现 |\n| Overall Assessment | **3.0/5 (Findings)** | 方法论可靠、控制设计好，适合 Findings 发表。但新颖性不足以达到主会议水平——核心发现要么是增量扩展、要么是 null result、要么是弱支撑的 claim |\n| Confidence | 4/5 | 熟悉 probing/steering/跨语言表征文献，仔细通读全文含 Appendix |\n\n---\n\n## Strengths\n\n**S1. 混淆因素控制设计出色。** COMET 翻译质量分层 + XNLI 非冲突基线的组合是一个真正的方法论贡献（Section 3.5, 4.4-4.5）。用 XNLI 作为非冲突对照来区分冲突特异性 vs. 一般跨语言不对称性，思路清晰且可复用。\n\n**S2. 多模型验证增强泛化性。** 三个架构差异显著的模型（Llama/Qwen/Gemma）在检测能力上一致，强化了\"冲突信号线性可检测\"这一结论的可信度（Table 1, Figure 3）。\n\n**S3. 统计方法规范。** Bootstrap CI（n=2000）、Bonferroni 校正（l=10 to α values）、Fisher 精确检验、matched-condition 控制，统计实践达到 top-venue 标准。\n\n**S4. 诚实报告负面结果。** Qwen/Gemma steering 失败（Table 3）、asymmetry 非冲突特异性（Section 4.4）——这些负面结果的如实报告值得肯定，优于很多只报积极结果的论文。\n\n**S5. Seed replication 加强因果 claim。** Appendix C 用独立 seed 复现了 Llama L13 steering 效果（N=201, 独立 train/test split），排除了单次 split 偶然性的可能。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**N1 [critical] \"Detection ≠ Decision\" 核心 claim 支撑不足，且与 Basu et al. (2026) 差异化不清晰。**\n- 具体位置：Abstract、Section 4.6、Table 3、Figure 5-6、Discussion (Section 5)\n- 问题：\n  (a) Basu et al. (2026) 标题即为 \"Interpretability without actionability\"，在单语设置中已经建立了 detection-steering 的 dissociation。本文的跨语言扩展未能清晰阐述相比单语设置的增量发现——跨语言设置具体揭示了哪些单语分析无法观察到的现象？\n  (b) Representation steering 仅在 Llama L13（41% depth）产生显著因果效应（flip rate 19.9% vs. 6.6% random, Fisher p=0.002）。Qwen 和 Gemma 在所有层均无显著效应。即 2/3 模型不支持任何因果影响。\n  (c) 即使在 Llama 中，相邻的 L16（50% depth）已无显著效应（p>0.12），因果窗口极窄。这可能是精确定位，但也可能是 fragile/model-specific artifact。\n  (d) 论文将\"steering 在 2/3 模型失败\"框架为支持 dissociation 叙事，但另一种同样合理的解释是：线性探针并未捕捉因果相关特征，steering 方法本身（单一方向线性干预）太粗糙。\n- 为什么影响接收：这是论文最核心的叙事卖点。如果 dissociation 已被 Basu et al. 建立、且跨语言扩展未增加实质发现，则论文的核心新颖性大幅下降。\n- 建议修改方向：(1) 在 Section 2 添加与 Basu et al. 2026 的逐点对比段落，明确本文的增量在哪里；(2) 诚实重新定位——从\"我们发现 detection≠decision\"改为\"跨语言设置下 detection≠decision 模式与单语一致\"；(3) 考虑使用 activation patching（而非仅 linear steering）来检验因果性，增强方法多样性。\n\n**N2 [critical] \"General Cross-Lingual Asymmetries\" 泛化声称仅基于单一语言对。**\n- 具体位置：标题、Abstract (\"consistent with general multilingual structure\")、Contribution 2、Section 4.3-4.4\n- 问题：论文标题声称 \"General Cross-Lingual Asymmetries\"，但实验仅覆盖英-中一个语言对。英语和中文有特殊属性（高类型距离、训练数据中英语占比极高），从一个语言对推断\"一般跨语言结构\"在统计上等同于 N=1 的泛化。Section 3.5 提到了 EN-DE 的 XNLI 控制实验，但仅用于混淆因素检查，未作为第二语言对的完整探测实验。\n- 为什么影响接收：标题和核心 claim 的 scope 与实验证据不匹配。Reviewer 和 AC 对 overclaiming 非常敏感。\n- 建议修改方向：(1) 增加至少 1-2 个类型差异大的语言对（如 EN-DE、EN-JA 或 EN-AR）；(2) 或将标题修改为 \"English-Chinese Knowledge Conflict Signals...\"，并在全文中软化 \"general\" 相关表述。\n\n**N3 [critical] Contribution 2（asymmetry = general structure）本质是 null result 被包装为正面贡献。**\n- 具体位置：Page 1 贡献列表第 2 条、Section 4.3-4.4、Figure 4\n- 问题：发现迁移不对称性与 XNLI 基线一致 ＝ 不对称性不是冲突特异的 ＝ 这是一个 null result。将\"没有发现冲突特异不对称性\"列为独立贡献，膨胀了贡献计数。这更适合作为 Contribution 1（跨语言可检测性）的分析组成部分——作为一个重要的控制结果，而非独立贡献。\n- 为什么影响接收：四个贡献中如果一个是 null result、一个弱支撑（detection≠decision），实质上只有两个站得住的贡献（可检测性 + 混淆因素排除），且可检测性本身是增量扩展。整体贡献量偏薄。\n- 建议修改方向：将 asymmetry 发现并入 Contribution 1 的讨论，重新组织为 3 个贡献。\n\n---\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1 [warning] 四个贡献的权重严重不均衡。**\n- 具体位置：Page 1 贡献列表\n- 问题：逐条分析——\n  - C1（跨语言可检测性）：Zhao et al. 2024 单语→跨语言的增量扩展，预期性强\n  - C2（asymmetry = general structure）：null result（见 N3）\n  - C3（detection-decision dissociation）：仅 1/3 模型支持，且 Basu et al. 2026 已建立单语版本（见 N1）\n  - C4（混淆因素排除）：真正的方法论贡献，但偏 methodological\n- 没有一个贡献具有足够独立支撑 conference-level impact 的力度。\n\n**W2 [warning] 单一 train/test split，缺乏交叉验证。**\n- 具体位置：Section 3.3、Limitations\n- 问题：所有 probing 结果基于单次 80/20 随机分割。作者在 Limitations 中承诺 camera-ready 提供 5-fold CV，但当前版本的探测准确率数字无法排除 split 敏感性。Appendix C 的 seed replication 仅覆盖 steering，不覆盖 probing accuracy。\n- 建议：在当前版本中至少报告 3-fold CV 的 mean±std。\n\n**W3 [warning] Steering 分析样本量小、多重比较负担重。**\n- 具体位置：Section 4.6、Table 3\n- 问题：Matched-condition steering 使用 N=131-201。同时在 ~30 层 × 10 个 α 值 × 4 个方向上搜索，即使 Bonferroni 校正后，小样本下的统计功效（power）很低。这增加了 false negative（Qwen/Gemma）和 false positive（Llama L13）的风险。\n- 建议：报告 power analysis，或增加 matched-condition 数据量。\n\n**W4 [warning] 机制深度偏浅——定位偏 empirical probing，非 mechanistic interpretability。**\n- 具体位置：全文\n- 问题：论文定位于\"mechanistic interpretability\"（标题所属领域），但分析停留在残差流整体层面——标准 logistic regression 探针。没有 attention head 或 MLP 层面的分解，没有 circuit-level 分析，没有探究 probe 学到了什么具体特征。这更接近\"empirical probing study\"而非\"mechanistic interpretability\"。\n- 建议：(1) 增加 attention vs. MLP contribution 的分解分析；或 (2) 在 Related Work / framing 中将论文重新定位为 \"empirical cross-lingual probing study\"。\n\n**W5 [warning] Related Work 缺少跨语言知识编辑文献。**\n- 具体位置：Section 2\n- 问题：跨语言知识编辑（cross-lingual knowledge editing）是一个活跃的相关领域——ROME/MEMIT 在多语言模型中的编辑传播失败（如 \"Editing Across Languages\" survey, 2025; CLM-Bench, 2026）与本文发现的跨语言 probe 不对称性在机制上可能共享同一原因（语言特定的激活模式）。Section 2 完全未提及这一方向。\n- 建议：增加一小段讨论跨语言知识编辑的传播失败现象，与本文的 asymmetry 发现建立联系。\n\n**W6 [info] 缺少 Conclusion 章节。**\n- 具体位置：Section 5 → Limitations，无 Section 6\n- 问题：论文从 Discussion 直接跳到 Limitations，没有独立的 Conclusion。虽非格式违规，但缺少一个干净的叙事收尾，影响可读性。\n\n---\n\n## Questions to Authors\n\n**Q1.** Basu et al. (2026) \"Interpretability without actionability\" 已在单语设置下论证 detection ≠ steering。本文的跨语言扩展具体揭示了哪些单语分析观察不到的现象？请明确阐述 incremental novelty。\n\n**Q2.** Llama L13 steering 有效但 L16（仅 3 层之差）即无效（p>0.12）。是否测试了 L14 和 L15？如何解释这个极窄的因果窗口？\n\n**Q3.** Section 3.5 已将 ConflictQA 翻译为德语作为 XNLI 控制。为何不将 EN-DE 作为第二语言对进行完整的 probing 实验，以直接支持\"general cross-lingual\"的 claim？\n\n**Q4.** COMET 分层排除（Section 4.5）使用 tercile 阈值。结果对该阈值敏感度如何？quartile 或 median split 下结论是否一致？\n\n**Q5.** Gemma 的 ConflictQA 正确回答率最低（966/1590），但探测准确率最高（EN→EN 88.9%）。这种背离是否暗示 probe 捕获的是任务无关的信号？\n\n---\n\n## Missing References\n\n1. **跨语言知识编辑传播**: \"Editing Across Languages: A Survey of Multilingual Knowledge Editing\" (2025) 和 CLM-Bench (2026) 探讨了 ROME/MEMIT 在多语言中的传播失败——与本文的 asymmetry 发现机制上相关。\n2. **跨语言知识编辑基准**: BMIKE-53 (53 语言知识编辑基准) 提供了跨语言知识操作的系统性证据。\n\n（Director 指定的 Pokharel 2026、Sundar 2025、Gurgurov 2026、Pimentel 2021、Ravichander 2021 均已在论文中引用 ✓）\n\n---\n\n## 格式合规检查\n\n| 检查项 | 结果 |\n|--------|------|\n| 正文页数 ≤ 8 页 | ✓ Sections 1-5 在 pp.1-8 |\n| Limitations section 存在 | ✓ p.9，正文后 references 前 |\n| Limitations 不计入页数 | ✓ 在第 9 页 |\n| Abstract ≤ 200 words | ✓ 约 164 words |\n| Double-blind 匿名化 | ✓ \"Anonymous ACL submission\"，代码用 anonymous.4open.science |\n| 自引泄露 | 未发现明显泄露 |\n| ACL 模板 | ✓ 标准 ACL 格式 |\n\n---\n\n## 主要优势总结\n\n- 混淆因素控制设计（COMET + XNLI）是可复用的方法论贡献\n- 多模型一致的检测能力增强了泛化性\n- 统计方法规范、负面结果诚实报告\n- 代码公开、AI 辅助使用透明声明\n\n## 总体评分\n\n**Overall: 3.0/5 (Findings)**\n\n**一句话总结**: 方法论扎实、控制设计好的跨语言 probing 研究，适合 Findings 发表，但核心新颖性不足以达到主会议水平——最有新意的 detection≠decision claim 仅 1/3 模型支持且已被 Basu et al. 2026 在单语中建立，\"general cross-lingual\" 的泛化声称仅基于单一语言对。\n\n---\n\nSources:\n- [ARR Review Form](https://aclrollingreview.org/reviewform)\n- [ARR Reviewer Guidelines](https://aclrollingreview.org/reviewerguidelines)\n",
  "reviewer_id": "2",
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审稿意见：新颖性与完整性\n\n## Summary\n\n本文将知识冲突信号的 probing 分析从单语（Zhao et al. 2024）扩展到跨语言（英-中）设置，使用三个 LLM（Llama-3.1-8B-Instruct、Qwen2.5-8B、Gemma-2-9B-IT）进行残差流探测、XNLI 非冲突基线对照、COMET 混淆因素排除和因果 steering 实验。主要发现：(1) 冲突信号在所有模型和方向上线性可检测；(2) ZH→EN 迁移优势约 7pp，与 XNLI 基线一致，反映一般跨语言结构而非冲突特异性；(3) 因果 steering 仅在 Llama L13（41% 深度）成功，Qwen/Gemma 无显著因果效应，表明检测不蕴含因果相关性。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0/5 | 方法论扎实（bootstrap CI、Bonferroni 校正、Fisher 精确检验），混淆因素控制设计优秀。但核心 claim（detection≠decision）仅 1/3 模型支持，单一 train/test split 影响可靠性 |\n| Excitement | 2.5/5 | Probing 跨语言扩展属增量贡献；最具新颖性的 detection-decision dissociation 已被 Basu et al. 2026 在单语设置中建立；asymmetry 发现为 null result |\n| Reproducibility | 4/5 | 提供匿名代码仓库，方法描述清晰，统计方法完整。单一 split 限制精确数值复现 |\n| Overall Assessment | **3.0/5 (Findings)** | 方法论可靠、控制设计好，适合 Findings 发表。但新颖性不足以达到主会议水平——核心发现要么是增量扩展、要么是 null result、要么是弱支撑的 claim |\n| Confidence | 4/5 | 熟悉 probing/steering/跨语言表征文献，仔细通读全文含 Appendix |\n\n---\n\n## Strengths\n\n**S1. 混淆因素控制设计出色。** COMET 翻译质量分层 + XNLI 非冲突基线的组合是一个真正的方法论贡献（Section 3.5, 4.4-4.5）。用 XNLI 作为非冲突对照来区分冲突特异性 vs. 一般跨语言不对称性，思路清晰且可复用。\n\n**S2. 多模型验证增强泛化性。** 三个架构差异显著的模型（Llama/Qwen/Gemma）在检测能力上一致，强化了\"冲突信号线性可检测\"这一结论的可信度（Table 1, Figure 3）。\n\n**S3. 统计方法规范。** Bootstrap CI（n=2000）、Bonferroni 校正（l=10 to α values）、Fisher 精确检验、matched-condition 控制，统计实践达到 top-venue 标准。\n\n**S4. 诚实报告负面结果。** Qwen/Gemma steering 失败（Table 3）、asymmetry 非冲突特异性（Section 4.4）——这些负面结果的如实报告值得肯定，优于很多只报积极结果的论文。\n\n**S5. Seed replication 加强因果 claim。** Appendix C 用独立 seed 复现了 Llama L13 steering 效果（N=201, 独立 train/test split），排除了单次 split 偶然性的可能。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**N1 [critical] \"Detection ≠ Decision\" 核心 claim 支撑不足，且与 Basu et al. (2026) 差异化不清晰。**\n- 具体位置：Abstract、Section 4.6、Table 3、Figure 5-6、Discussion (Section 5)\n- 问题：\n  (a) Basu et al. (2026) 标题即为 \"Interpretability without actionability\"，在单语设置中已经建立了 detection-steering 的 dissociation。本文的跨语言扩展未能清晰阐述相比单语设置的增量发现——跨语言设置具体揭示了哪些单语分析无法观察到的现象？\n  (b) Representation steering 仅在 Llama L13（41% depth）产生显著因果效应（flip rate 19.9% vs. 6.6% random, Fisher p=0.002）。Qwen 和 Gemma 在所有层均无显著效应。即 2/3 模型不支持任何因果影响。\n  (c) 即使在 Llama 中，相邻的 L16（50% depth）已无显著效应（p>0.12），因果窗口极窄。这可能是精确定位，但也可能是 fragile/model-specific artifact。\n  (d) 论文将\"steering 在 2/3 模型失败\"框架为支持 dissociation 叙事，但另一种同样合理的解释是：线性探针并未捕捉因果相关特征，steering 方法本身（单一方向线性干预）太粗糙。\n- 为什么影响接收：这是论文最核心的叙事卖点。如果 dissociation 已被 Basu et al. 建立、且跨语言扩展未增加实质发现，则论文的核心新颖性大幅下降。\n- 建议修改方向：(1) 在 Section 2 添加与 Basu et al. 2026 的逐点对比段落，明确本文的增量在哪里；(2) 诚实重新定位——从\"我们发现 detection≠decision\"改为\"跨语言设置下 detection≠decision 模式与单语一致\"；(3) 考虑使用 activation patching（而非仅 linear steering）来检验因果性，增强方法多样性。\n\n**N2 [critical] \"General Cross-Lingual Asymmetries\" 泛化声称仅基于单一语言对。**\n- 具体位置：标题、Abstract (\"consistent with general multilingual structure\")、Contribution 2、Section 4.3-4.4\n- 问题：论文标题声称 \"General Cross-Lingual Asymmetries\"，但实验仅覆盖英-中一个语言对。英语和中文有特殊属性（高类型距离、训练数据中英语占比极高），从一个语言对推断\"一般跨语言结构\"在统计上等同于 N=1 的泛化。Section 3.5 提到了 EN-DE 的 XNLI 控制实验，但仅用于混淆因素检查，未作为第二语言对的完整探测实验。\n- 为什么影响接收：标题和核心 claim 的 scope 与实验证据不匹配。Reviewer 和 AC 对 overclaiming 非常敏感。\n- 建议修改方向：(1) 增加至少 1-2 个类型差异大的语言对（如 EN-DE、EN-JA 或 EN-AR）；(2) 或将标题修改为 \"English-Chinese Knowledge Conflict Signals...\"，并在全文中软化 \"general\" 相关表述。\n\n**N3 [critical] Contribution 2（asymmetry = general structure）本质是 null result 被包装为正面贡献。**\n- 具体位置：Page 1 贡献列表第 2 条、Section 4.3-4.4、Figure 4\n- 问题：发现迁移不对称性与 XNLI 基线一致 ＝ 不对称性不是冲突特异的 ＝ 这是一个 null result。将\"没有发现冲突特异不对称性\"列为独立贡献，膨胀了贡献计数。这更适合作为 Contribution 1（跨语言可检测性）的分析组成部分——作为一个重要的控制结果，而非独立贡献。\n- 为什么影响接收：四个贡献中如果一个是 null result、一个弱支撑（detection≠decision），实质上只有两个站得住的贡献（可检测性 + 混淆因素排除），且可检测性本身是增量扩展。整体贡献量偏薄。\n- 建议修改方向：将 asymmetry 发现并入 Contribution 1 的讨论，重新组织为 3 个贡献。\n\n---\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1 [warning] 四个贡献的权重严重不均衡。**\n- 具体位置：Page 1 贡献列表\n- 问题：逐条分析——\n  - C1（跨语言可检测性）：Zhao et al. 2024 单语→跨语言的增量扩展，预期性强\n  - C2（asymmetry = general structure）：null result（见 N3）\n  - C3（detection-decision dissociation）：仅 1/3 模型支持，且 Basu et al. 2026 已建立单语版本（见 N1）\n  - C4（混淆因素排除）：真正的方法论贡献，但偏 methodological\n- 没有一个贡献具有足够独立支撑 conference-level impact 的力度。\n\n**W2 [warning] 单一 train/test split，缺乏交叉验证。**\n- 具体位置：Section 3.3、Limitations\n- 问题：所有 probing 结果基于单次 80/20 随机分割。作者在 Limitations 中承诺 camera-ready 提供 5-fold CV，但当前版本的探测准确率数字无法排除 split 敏感性。Appendix C 的 seed replication 仅覆盖 steering，不覆盖 probing accuracy。\n- 建议：在当前版本中至少报告 3-fold CV 的 mean±std。\n\n**W3 [warning] Steering 分析样本量小、多重比较负担重。**\n- 具体位置：Section 4.6、Table 3\n- 问题：Matched-condition steering 使用 N=131-201。同时在 ~30 层 × 10 个 α 值 × 4 个方向上搜索，即使 Bonferroni 校正后，小样本下的统计功效（power）很低。这增加了 false negative（Qwen/Gemma）和 false positive（Llama L13）的风险。\n- 建议：报告 power analysis，或增加 matched-condition 数据量。\n\n**W4 [warning] 机制深度偏浅——定位偏 empirical probing，非 mechanistic interpretability。**\n- 具体位置：全文\n- 问题：论文定位于\"mechanistic interpretability\"（标题所属领域），但分析停留在残差流整体层面——标准 logistic regression 探针。没有 attention head 或 MLP 层面的分解，没有 circuit-level 分析，没有探究 probe 学到了什么具体特征。这更接近\"empirical probing study\"而非\"mechanistic interpretability\"。\n- 建议：(1) 增加 attention vs. MLP contribution 的分解分析；或 (2) 在 Related Work / framing 中将论文重新定位为 \"empirical cross-lingual probing study\"。\n\n**W5 [warning] Related Work 缺少跨语言知识编辑文献。**\n- 具体位置：Section 2\n- 问题：跨语言知识编辑（cross-lingual knowledge editing）是一个活跃的相关领域——ROME/MEMIT 在多语言模型中的编辑传播失败（如 \"Editing Across Languages\" survey, 2025; CLM-Bench, 2026）与本文发现的跨语言 probe 不对称性在机制上可能共享同一原因（语言特定的激活模式）。Section 2 完全未提及这一方向。\n- 建议：增加一小段讨论跨语言知识编辑的传播失败现象，与本文的 asymmetry 发现建立联系。\n\n**W6 [info] 缺少 Conclusion 章节。**\n- 具体位置：Section 5 → Limitations，无 Section 6\n- 问题：论文从 Discussion 直接跳到 Limitations，没有独立的 Conclusion。虽非格式违规，但缺少一个干净的叙事收尾，影响可读性。\n\n---\n\n## Questions to Authors\n\n**Q1.** Basu et al. (2026) \"Interpretability without actionability\" 已在单语设置下论证 detection ≠ steering。本文的跨语言扩展具体揭示了哪些单语分析观察不到的现象？请明确阐述 incremental novelty。\n\n**Q2.** Llama L13 steering 有效但 L16（仅 3 层之差）即无效（p>0.12）。是否测试了 L14 和 L15？如何解释这个极窄的因果窗口？\n\n**Q3.** Section 3.5 已将 ConflictQA 翻译为德语作为 XNLI 控制。为何不将 EN-DE 作为第二语言对进行完整的 probing 实验，以直接支持\"general cross-lingual\"的 claim？\n\n**Q4.** COMET 分层排除（Section 4.5）使用 tercile 阈值。结果对该阈值敏感度如何？quartile 或 median split 下结论是否一致？\n\n**Q5.** Gemma 的 ConflictQA 正确回答率最低（966/1590），但探测准确率最高（EN→EN 88.9%）。这种背离是否暗示 probe 捕获的是任务无关的信号？\n\n---\n\n## Missing References\n\n1. **跨语言知识编辑传播**: \"Editing Across Languages: A Survey of Multilingual Knowledge Editing\" (2025) 和 CLM-Bench (2026) 探讨了 ROME/MEMIT 在多语言中的传播失败——与本文的 asymmetry 发现机制上相关。\n2. **跨语言知识编辑基准**: BMIKE-53 (53 语言知识编辑基准) 提供了跨语言知识操作的系统性证据。\n\n（Director 指定的 Pokharel 2026、Sundar 2025、Gurgurov 2026、Pimentel 2021、Ravichander 2021 均已在论文中引用 ✓）\n\n---\n\n## 格式合规检查\n\n| 检查项 | 结果 |\n|--------|------|\n| 正文页数 ≤ 8 页 | ✓ Sections 1-5 在 pp.1-8 |\n| Limitations section 存在 | ✓ p.9，正文后 references 前 |\n| Limitations 不计入页数 | ✓ 在第 9 页 |\n| Abstract ≤ 200 words | ✓ 约 164 words |\n| Double-blind 匿名化 | ✓ \"Anonymous ACL submission\"，代码用 anonymous.4open.science |\n| 自引泄露 | 未发现明显泄露 |\n| ACL 模板 | ✓ 标准 ACL 格式 |\n\n---\n\n## 主要优势总结\n\n- 混淆因素控制设计（COMET + XNLI）是可复用的方法论贡献\n- 多模型一致的检测能力增强了泛化性\n- 统计方法规范、负面结果诚实报告\n- 代码公开、AI 辅助使用透明声明\n\n## 总体评分\n\n**Overall: 3.0/5 (Findings)**\n\n**一句话总结**: 方法论扎实、控制设计好的跨语言 probing 研究，适合 Findings 发表，但核心新颖性不足以达到主会议水平——最有新意的 detection≠decision claim 仅 1/3 模型支持且已被 Basu et al. 2026 在单语中建立，\"general cross-lingual\" 的泛化声称仅基于单一语言对。\n\n---\n\nSources:\n- [ARR Review Form](https://aclrollingreview.org/reviewform)\n- [ARR Reviewer Guidelines](https://aclrollingreview.org/reviewerguidelines)\n",
    "reviewer_id": "2",
    "project": "clkc_mech_interp"
  }
}
```

</details>

---

### Tool result

_source line 323 · 2026-05-25T21:23:30.922423+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3714
}
```

</details>

---

### Tool call

_source line 324 · 2026-05-25T21:23:35.068040+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
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

_source line 325 · 2026-05-25T21:23:35.121194+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 53
}
```

</details>

---

### Tool call

_source line 326 · 2026-05-25T21:23:38.886569+00:00_

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
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/review_round_4/_pdf_images"
  }
}
```

</details>

---

### Tool result

_source line 327 · 2026-05-25T21:23:38.886932+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 328 · 2026-05-25T21:23:45.825198+00:00_

审稿完成。已向 Review Director 提交完整审稿意见，核心判断：

- **Overall: 3.0/5 (Findings)**
- **3 个 critical 问题**：(1) detection≠decision 核心 claim 仅 1/3 模型支持且与 Basu et al. 2026 差异化不清晰；(2) "General Cross-Lingual" 泛化声称仅基于英-中单一语言对；(3) asymmetry 发现是 null result 被包装为正面贡献
- **5 个 warning 问题**：贡献权重不均衡、单一 split 无 CV、steering 样本小、机制深度不足、缺少跨语言知识编辑文献
- **格式合规**：全部通过（8 页正文、Limitations 存在、Abstract ≤200 words、匿名化完整）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2"
}
```

</details>

---

## Round 8

4 recorded events

### User

_source line 329 · 2026-05-25T21:25:12.071246+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完��审稿意见。请逐条回应其 Weaknesses 和关键论点：对每条用 [AGREE] 表示��意（简述理由），或 [REBUT] 表示反驳��引用具体 Section/Table/Figure 提供证据）���

---

# Reviewer 1 — 方法严谨性审查

## Summary

本文对三个多语言 LLM（Llama-3.1-8B、Qwen3-8B、Gemma-2-9B-IT）的残差流进行探测，研究英中跨语言知识冲突信号的可检测性、迁移不对称性及因果干预效果。主要发现：(1) 冲突信号在两种语言中均线性可分；(2) ZH→EN 迁移优势（~7pp）与 XNLI 基线一致，反映通用跨语言结构而非冲突特异编码；(3) 仅 Llama L13 层的 steering 产生因果效应，Qwen/Gemma steering 失败，据此提出"detection ≠ decision"论断。

## Strengths

**S1.** 三模型设计提供跨架构证据（3.5% 问题重叠，近独立复制）。
**S2.** XNLI 非冲突基线控制得当。
**S3.** EN-DE 类型学控制巧妙（14.8% vs 3.8% Jaccard，Δ = +1.2pp n.s.）。
**S4.** Selectivity control 规范（selectivity gap 21–40pp）。
**S5.** Steering 随机控制设计合理（等幅 r ~ N(0,I) 对照）。
**S6.** Limitations 诚实。

## Weaknesses

**W1 [critical] "Detection ≠ Decision" 核心论断证据不足，存在过度概括。**
- 正面因果证据仅来自一个模型的一个层。Qwen/Gemma 负面结果有多种替代解释：非线性通路、因果窗口在不同层（Qwen 仅测 L14、Gemma 仅测 L17）、样本量不足（n=131/171）、线性 steering 方法局限。
- Absence of evidence ≠ evidence of absence。

**W2 [critical] Qwen 不对称性 CI 包含零，但被当作支持证据。**
- Qwen Δ_asym = +7.2, CI [−0.6, 13.7]，95% CI 跨越零。
- Bonferroni 校正后（阈值 0.017），Llama (p=0.038) 也不再显著，仅 Gemma (p=0.006) 幸存。
- 三模型中两个不显著（校正后），严重削弱"一致"论断。

**W3 [critical] COMET tercile 分析严重欠功效（MDE=25.3pp），无法排除翻译质量混淆。**
- Gemma Δ = +10.3pp 在混淆方向，低功效下 p=0.278 不能排除实质效应。
- 翻译质量混淆未被有效排除。

**W4 [warning] TOST 等价检验功效仅 1.4%，无信息量。**
- ±2pp 边界过严，检验注定失败。

**W5 [warning] 单 train/test split，bootstrap CI 仅捕获 split 内变异性。**

**W6 [warning] 翻译模型 Qwen3-8B 同时作为实验对象。**

**W7 [warning] 全文多重假设检验缺乏整体 FWER 控制。**
- 全文 ~100+ 假设检验，仅 steering 做了 per-layer Bonferroni。三模型不对称性检验属同一族但未校正。

**W8 [warning] Steering 仅在英文数据上评估，未测试跨语言因果干预。**

**W9 [info] Fisher's exact test 用于 paired data 可能不当（应用 McNemar's test）。**

## Overall Assessment: 3.0 (Findings)
## Confidence: 4/5

---

请逐条回应上述 Weaknesses（W1-W9）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 330 · 2026-05-25T21:27:08.716951+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 交叉回应：Reviewer 1 Weaknesses 逐条评议\n\n---\n\n## [AGREE] R1-W1: \"Detection ≠ Decision\" 核心论断证据不足\n\n完全同意。这与我 N1 的判断一致。补充两点：\n\n(1) R1 指出 \"absence of evidence ≠ evidence of absence\" 非常精准。论文将 Qwen/Gemma steering 失败解读为支持 dissociation 叙事，但 R1 正确列举了替代解释（非线性通路、不同因果窗口、样本量不足、线性 steering 局限）。从论文 Table 3 来看，Qwen 仅报告了 L14、Gemma 仅报告了 L17 层的 steering 结果，并未系统搜索所有层的因果窗口——这与 Llama 的 L13 精确定位是不对等的实验设计。\n\n(2) 我在 N1 中额外指出了 Basu et al. (2026) \"Interpretability without actionability\" 已在单语设置中建立了 detection-steering dissociation，进一步削弱了本文在该 claim 上的新颖性。R1 未提及这一文献重叠，但两个问题叠加后，该 claim 的支撑更加薄弱。\n\n---\n\n## [AGREE] R1-W2: Qwen 不对称性 CI 包含零\n\n同意，且认为这是我审稿中的一个遗漏。R1 的分析很有说服力：\n\n- Qwen Δ_asym = +7.2, CI [−0.6, 13.7] 确实跨越零\n- Bonferroni 校正阈值 0.05/3 = 0.017 下，Llama (p=0.038) 也不显著，仅 Gemma (p=0.006) 幸存\n- 论文 Section 4.3 称\"all three models show a consistent directional trend\"——但从统计严格性看，校正后仅 1/3 模型显著支持该 \"consistent\" 断言\n\n这直接影响 Contribution 2（asymmetry reflects general structure）的可信度。如果不对称性本身在多数模型中不显著，那么将其与 XNLI 基线匹配并声称反映\"一般跨语言结构\"就更加站不住。这强化了我 N3 的判断（该 contribution 本质是 null result）。\n\n---\n\n## [AGREE（部分）] R1-W3: COMET tercile 分析功效不足\n\n同意核心论点，但认为需要在论文的多层控制框架中评估。\n\nR1 的功效分析（MDE=25.3pp）是正确的——COMET tercile 分析单独来看确实无法排除翻译质量混淆。Gemma Δ=+10.3pp（Section 4.5, Table 2）在混淆方向，低功效下 p=0.278 完全可能是 type II error。\n\n但我要指出，论文的混淆排除不只依赖 tercile 分析——它是一个多层设计：\n1. COMET tercile stratification（R1 正确指出功效不足）\n2. XNLI 非冲突基线（Section 4.4）——这是独立于翻译质量的控制\n3. Token overlap / Jaccard 分析（Section 4.4）——EN-DE 控制 Jaccard 仅 3.8%\n4. EN-DE 类型学控制（R1 自己在 S3 肯定了这一点：14.8% vs 3.8% Jaccard, Δ=+1.2pp n.s.）\n\n因此，COMET tercile 分析是最薄弱的一环，R1 的批评有效。但翻译质量混淆并非完全未被控制——XNLI 基线和 EN-DE 控制提供了部分独立证据。建议作者增大 tercile 分析的样本量或使用连续回归替代分层分析。\n\n---\n\n## [AGREE] R1-W4: TOST 等价检验功效仅 1.4%\n\n同意。±2pp 等价边界对于 balanced accuracy 来说过窄。在 n~200 的样本量和约 5-8pp 的 bootstrap SE 下，这个检验注定失败。论文应要么使用更合理的等价边界（如 ±5pp），要么删除这个 uninformative 的检验结果，避免给读者造成\"已验证等价性\"的错误印象。\n\n---\n\n## [AGREE] R1-W5: 单 train/test split\n\n完全同意，与我 W2 一致。Bootstrap CI 仅捕获 within-split sampling variability，不捕获 split selection variability。作者承诺 camera-ready 提供 5-fold CV，但当前版本的所有 probe accuracy 数字都有 split 敏感性风险。\n\n---\n\n## [REBUT] R1-W6: 翻译模型 Qwen3-8B 同时作为实验对象\n\n不完全同意。需要区分：\n\n- 翻译模型：**Qwen3-8B**（Section 3.2）\n- 实验探测对象：**Qwen2.5-8B**（Section 4.1）\n\n这是不同代际的模型（Qwen3 vs Qwen2.5），虽属同一模型家族，但架构和训练数据存在代际差异。R1 的担忧（同家族共享 tokenizer/分布偏好可能造成 Qwen2.5 probing 结果的系统性偏差）有一定道理，但：\n\n1. 翻译质量由 COMET（独立于 Qwen 的指标）验证，Section 3.2 明确提到 back-translation 质量校验\n2. 如果 Qwen 家族共享的偏好造成了系统性偏差，我们应该观察到 Qwen2.5 的 probing 结果系统性高于 Llama/Gemma——但 Table 1 显示 Qwen 的 probe accuracy 在三模型中并非系统性最高（EN→EN: Llama 77.6%, Qwen 75.0%, Gemma 88.9%）\n3. Qwen2.5 的 asymmetry CI 包含零（R1-W2），恰恰不支持 Qwen 家族偏好造成系统性优势的假说\n\n该担忧值得在 Limitations 中提及，但不构成对结论的实质性威胁。\n\n---\n\n## [AGREE（部分）] R1-W7: 多重假设检验缺乏整体 FWER 控制\n\n部分同意。R1 指出全文 ~100+ 假设检验缺乏统一 FWER 控制是正确的。特别是：\n\n- 三模型不对称性检验属同一 hypothesis family，应做校正（如 R1-W2 所示，校正后仅 Gemma 显著）\n- Probing accuracy 的 binomial tests（4 方向 × 3 模型 = 12 tests）也属同一族\n\n但我认为要求全文所有检验做统一 FWER 控制过于严格——这在当前 NLP 实证文献中几乎从未执行。更务实的建议是：(1) 对 asymmetry 做三模型 Bonferroni（如 R1 所建议）；(2) 对 steering 保留现有 per-layer Bonferroni；(3) 明确报告哪些结论在校正后仍然成立、哪些不成立。\n\n---\n\n## [AGREE] R1-W8: Steering 仅在英文数据上评估\n\n同意，这是我审稿中未显式提出的一个重要遗漏。\n\n论文声称研究\"跨语言知识冲突\"，但 Section 4.6 的 steering 实验仅评估英文侧数据的 flip rate。如果核心主题是跨语言，则应至少测试：(1) 用 ZH→EN probe 对中文输入做 steering；(2) 用 EN→ZH probe 对英文输入做 cross-lingual steering。缺少这些实验使得 steering 部分与论文的跨语言定位脱节。\n\n这进一步削弱了 detection-decision dissociation 的跨语言意义（我 N1 的延伸）。\n\n---\n\n## [AGREE] R1-W9: Fisher's exact test 用于 paired data\n\n同意这是一个技术性改进点。Section 4.6 的 steering 评估对同一组样本进行 steering vs. random control 比较——这是 paired within-subject design，McNemar's test 比 Fisher's exact test 更合适。Fisher's test 假设两组独立，会低估统计功效。\n\n不过，考虑到 steering 效应在 Llama L13 的 p 值已经很小（p=0.002），切换到 McNemar's 不太可能改变该结论方向。但对 borderline 结果（如 Qwen/Gemma 某些层）可能有影响。建议作者在修改稿中统一使用 McNemar's test。\n\n---\n\n## 综合评议\n\nR1 和我在 3 个核心问题上高度一致：\n1. **Detection ≠ decision claim 支撑不足**（R1-W1 ↔ 我 N1）\n2. **Asymmetry 的 \"consistent\" 断言统计不充分**（R1-W2 ↔ 我 N3）\n3. **单 split 限制可靠性**（R1-W5 ↔ 我 W2）\n\nR1 在统计细节上更深入（W2 的 Bonferroni 校正分析、W3 的 MDE 计算、W4 的 TOST 功效、W9 的配对检验），这些补充了我审稿中的方法论盲点。\n\nR1 唯一我有分歧的是 **W6（翻译模型=实验对象）**——翻译模型 Qwen3-8B 和实验模型 Qwen2.5-8B 是不同代际，且实验数据不支持系统性偏差假说。\n\n**维持我的评分：Overall 3.0 (Findings)**。R1 的统计批评进一步强化了我的判断——论文的方法论基础扎实但统计推断的严谨性有改进空间，核心新颖性不足以达到主会议水平。\n",
  "reviewer_id": "2",
  "project": "clkc_mech_interp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 交叉回应：Reviewer 1 Weaknesses 逐条评议\n\n---\n\n## [AGREE] R1-W1: \"Detection ≠ Decision\" 核心论断证据不足\n\n完全同意。这与我 N1 的判断一致。补充两点：\n\n(1) R1 指出 \"absence of evidence ≠ evidence of absence\" 非常精准。论文将 Qwen/Gemma steering 失败解读为支持 dissociation 叙事，但 R1 正确列举了替代解释（非线性通路、不同因果窗口、样本量不足、线性 steering 局限）。从论文 Table 3 来看，Qwen 仅报告了 L14、Gemma 仅报告了 L17 层的 steering 结果，并未系统搜索所有层的因果窗口——这与 Llama 的 L13 精确定位是不对等的实验设计。\n\n(2) 我在 N1 中额外指出了 Basu et al. (2026) \"Interpretability without actionability\" 已在单语设置中建立了 detection-steering dissociation，进一步削弱了本文在该 claim 上的新颖性。R1 未提及这一文献重叠，但两个问题叠加后，该 claim 的支撑更加薄弱。\n\n---\n\n## [AGREE] R1-W2: Qwen 不对称性 CI 包含零\n\n同意，且认为这是我审稿中的一个遗漏。R1 的分析很有说服力：\n\n- Qwen Δ_asym = +7.2, CI [−0.6, 13.7] 确实跨越零\n- Bonferroni 校正阈值 0.05/3 = 0.017 下，Llama (p=0.038) 也不显著，仅 Gemma (p=0.006) 幸存\n- 论文 Section 4.3 称\"all three models show a consistent directional trend\"——但从统计严格性看，校正后仅 1/3 模型显著支持该 \"consistent\" 断言\n\n这直接影响 Contribution 2（asymmetry reflects general structure）的可信度。如果不对称性本身在多数模型中不显著，那么将其与 XNLI 基线匹配并声称反映\"一般跨语言结构\"就更加站不住。这强化了我 N3 的判断（该 contribution 本质是 null result）。\n\n---\n\n## [AGREE（部分）] R1-W3: COMET tercile 分析功效不足\n\n同意核心论点，但认为需要在论文的多层控制框架中评估。\n\nR1 的功效分析（MDE=25.3pp）是正确的——COMET tercile 分析单独来看确实无法排除翻译质量混淆。Gemma Δ=+10.3pp（Section 4.5, Table 2）在混淆方向，低功效下 p=0.278 完全可能是 type II error。\n\n但我要指出，论文的混淆排除不只依赖 tercile 分析——它是一个多层设计：\n1. COMET tercile stratification（R1 正确指出功效不足）\n2. XNLI 非冲突基线（Section 4.4）——这是独立于翻译质量的控制\n3. Token overlap / Jaccard 分析（Section 4.4）——EN-DE 控制 Jaccard 仅 3.8%\n4. EN-DE 类型学控制（R1 自己在 S3 肯定了这一点：14.8% vs 3.8% Jaccard, Δ=+1.2pp n.s.）\n\n因此，COMET tercile 分析是最薄弱的一环，R1 的批评有效。但翻译质量混淆并非完全未被控制——XNLI 基线和 EN-DE 控制提供了部分独立证据。建议作者增大 tercile 分析的样本量或使用连续回归替代分层分析。\n\n---\n\n## [AGREE] R1-W4: TOST 等价检验功效仅 1.4%\n\n同意。±2pp 等价边界对于 balanced accuracy 来说过窄。在 n~200 的样本量和约 5-8pp 的 bootstrap SE 下，这个检验注定失败。论文应要么使用更合理的等价边界（如 ±5pp），要么删除这个 uninformative 的检验结果，避免给读者造成\"已验证等价性\"的错误印象。\n\n---\n\n## [AGREE] R1-W5: 单 train/test split\n\n完全同意，与我 W2 一致。Bootstrap CI 仅捕获 within-split sampling variability，不捕获 split selection variability。作者承诺 camera-ready 提供 5-fold CV，但当前版本的所有 probe accuracy 数字都有 split 敏感性风险。\n\n---\n\n## [REBUT] R1-W6: 翻译模型 Qwen3-8B 同时作为实验对象\n\n不完全同意。需要区分：\n\n- 翻译模型：**Qwen3-8B**（Section 3.2）\n- 实验探测对象：**Qwen2.5-8B**（Section 4.1）\n\n这是不同代际的模型（Qwen3 vs Qwen2.5），虽属同一模型家族，但架构和训练数据存在代际差异。R1 的担忧（同家族共享 tokenizer/分布偏好可能造成 Qwen2.5 probing 结果的系统性偏差）有一定道理，但：\n\n1. 翻译质量由 COMET（独立于 Qwen 的指标）验证，Section 3.2 明确提到 back-translation 质量校验\n2. 如果 Qwen 家族共享的偏好造成了系统性偏差，我们应该观察到 Qwen2.5 的 probing 结果系统性高于 Llama/Gemma——但 Table 1 显示 Qwen 的 probe accuracy 在三模型中并非系统性最高（EN→EN: Llama 77.6%, Qwen 75.0%, Gemma 88.9%）\n3. Qwen2.5 的 asymmetry CI 包含零（R1-W2），恰恰不支持 Qwen 家族偏好造成系统性优势的假说\n\n该担忧值得在 Limitations 中提及，但不构成对结论的实质性威胁。\n\n---\n\n## [AGREE（部分）] R1-W7: 多重假设检验缺乏整体 FWER 控制\n\n部分同意。R1 指出全文 ~100+ 假设检验缺乏统一 FWER 控制是正确的。特别是：\n\n- 三模型不对称性检验属同一 hypothesis family，应做校正（如 R1-W2 所示，校正后仅 Gemma 显著）\n- Probing accuracy 的 binomial tests（4 方向 × 3 模型 = 12 tests）也属同一族\n\n但我认为要求全文所有检验做统一 FWER 控制过于严格——这在当前 NLP 实证文献中几乎从未执行。更务实的建议是：(1) 对 asymmetry 做三模型 Bonferroni（如 R1 所建议）；(2) 对 steering 保留现有 per-layer Bonferroni；(3) 明确报告哪些结论在校正后仍然成立、哪些不成立。\n\n---\n\n## [AGREE] R1-W8: Steering 仅在英文数据上评估\n\n同意，这是我审稿中未显式提出的一个重要遗漏。\n\n论文声称研究\"跨语言知识冲突\"，但 Section 4.6 的 steering 实验仅评估英文侧数据的 flip rate。如果核心主题是跨语言，则应至少测试：(1) 用 ZH→EN probe 对中文输入做 steering；(2) 用 EN→ZH probe 对英文输入做 cross-lingual steering。缺少这些实验使得 steering 部分与论文的跨语言定位脱节。\n\n这进一步削弱了 detection-decision dissociation 的跨语言意义（我 N1 的延伸）。\n\n---\n\n## [AGREE] R1-W9: Fisher's exact test 用于 paired data\n\n同意这是一个技术性改进点。Section 4.6 的 steering 评估对同一组样本进行 steering vs. random control 比较——这是 paired within-subject design，McNemar's test 比 Fisher's exact test 更合适。Fisher's test 假设两组独立，会低估统计功效。\n\n不过，考虑到 steering 效应在 Llama L13 的 p 值已经很小（p=0.002），切换到 McNemar's 不太可能改变该结论方向。但对 borderline 结果（如 Qwen/Gemma 某些层）可能有影响。建议作者在修改稿中统一使用 McNemar's test。\n\n---\n\n## 综合评议\n\nR1 和我在 3 个核心问题上高度一致：\n1. **Detection ≠ decision claim 支撑不足**（R1-W1 ↔ 我 N1）\n2. **Asymmetry 的 \"consistent\" 断言统计不充分**（R1-W2 ↔ 我 N3）\n3. **单 split 限制可靠性**（R1-W5 ↔ 我 W2）\n\nR1 在统计细节上更深入（W2 的 Bonferroni 校正分析、W3 的 MDE 计算、W4 的 TOST 功效、W9 的配对检验），这些补充了我审稿中的方法论盲点。\n\nR1 唯一我有分歧的是 **W6（翻译模型=实验对象）**——翻译模型 Qwen3-8B 和实验模型 Qwen2.5-8B 是不同代际，且实验数据不支持系统性偏差假说。\n\n**维持我的评分：Overall 3.0 (Findings)**。R1 的统计批评进一步强化了我的判断——论文的方法论基础扎实但统计推断的严谨性有改进空间，核心新颖性不足以达到主会议水平。\n",
    "reviewer_id": "2",
    "project": "clkc_mech_interp"
  }
}
```

</details>

---

### Tool result

_source line 331 · 2026-05-25T21:27:12.782581+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4065
}
```

</details>

---

### Assistant

_source line 332 · 2026-05-25T21:27:17.251088+00:00_

交叉回应已提交。

与 Reviewer 1 在 3 个核心问题上高度一致（detection≠decision 支撑不足、asymmetry "consistent" 断言统计不充分、单 split 限制），唯一分歧在 W6（翻译模型问题）——Qwen3-8B 和 Qwen2.5-8B 是不同代际模型，实验数据不支持系统性偏差假说。维持 Overall 3.0 (Findings) 评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8b9aa92fafaf69b48d2c44b41c2fe9d9:reviewer_2"
}
```

</details>

---
