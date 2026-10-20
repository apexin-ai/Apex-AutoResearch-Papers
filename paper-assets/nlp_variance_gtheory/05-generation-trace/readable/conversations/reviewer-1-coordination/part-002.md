# Reviewer 1 coordination — Part 2 of 2

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../reviewer-1-coordination.md) · [Structured JSON](../../../sessions/43/43d7fe325dc90230775f.json)

## Round 15

### Tool call

_source line 506 · 2026-05-22T15:08:01.123035+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form dimensions/criteria, scoring scales (1-5 etc.), and what each score means. I need the exact official review form fields and scoring rubrics that ARR reviewers must fill out."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form dimensions/criteria, scoring scales (1-5 etc.), and what each score means. I need the exact official review form fields and scoring rubrics that ARR reviewers must fill out."
  }
}
```

</details>

---


### Tool call

_source line 507 · 2026-05-22T15:08:01.524538+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 508 · 2026-05-22T15:08:01.881279+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 509 · 2026-05-22T15:08:02.836151+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1311
}
```

</details>

---


### Tool result

_source line 510 · 2026-05-22T15:08:02.837378+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 511 · 2026-05-22T15:08:02.839034+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 512 · 2026-05-22T15:08:03.039869+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 513 · 2026-05-22T15:08:03.794147+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool result

_source line 514 · 2026-05-22T15:08:03.945868+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool result

_source line 515 · 2026-05-22T15:08:07.409710+00:00_

# ARR Review Form Dimensions and Scoring

Based on the guidelines provided, the document references a review form but **does not explicitly detail the complete scoring scales or all form fields**. However, it does specify:

## Three Primary Scores (as of February 2025)

The guidelines state reviewers must provide:

1. **Soundness** - "must be justified by the text of the review"
2. **Excitement** - a subjective score "orthogonal to the assessment of the soundness"
3. **Overall Recommendation** - "an explicit recommendation for the outcome of this paper"

## What the Scores Reflect

**Soundness** assesses technical validity. Low soundness scores require justification in the review text; scoring low without identifying faults suggests bias or incomplete review.

**Excitement** captures personal interest independent of technical quality, allowing reviewers to distinguish between "sound but unexciting" and subjectively valuable work.

**Overall Assessment** is described as "composite" reflecting soundness, excitement, novelty, and potential impact—with the note that "all papers recommended for Findings and main conferences are expected to be sufficiently sound and reproducible."

## Additional Form Elements

The guidelines mention:
- Confidence score (confidence level in assessment)
- Reproducibility score (must be justified)
- Author identity disclosure field
- Secondary reviewer acknowledgment field

**For the exact numerical scales (1-5 ranges) and complete form structure, you would need to consult the ARR OpenReview platform or the detailed [review form post](https://aclrollingreview.org/reviewform) referenced in the guidelines.**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6286
}
```

</details>

---


### Tool call

_source line 516 · 2026-05-22T15:08:11.935107+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 517 · 2026-05-22T15:08:12.286459+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 518 · 2026-05-22T15:08:13.190063+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1254
}
```

</details>

---


### Tool result

_source line 519 · 2026-05-22T15:08:13.190882+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 520 · 2026-05-22T15:08:13.542444+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 521 · 2026-05-22T15:08:13.743569+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 522 · 2026-05-22T15:08:14.146267+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 523 · 2026-05-22T15:08:15.103117+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1560
}
```

</details>

---


### Tool result

_source line 524 · 2026-05-22T15:08:15.104296+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1360
}
```

</details>

---


### Tool result

_source line 525 · 2026-05-22T15:08:15.209344+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1063
}
```

</details>

---


### Tool call

_source line 526 · 2026-05-22T15:08:15.209799+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 527 · 2026-05-22T15:08:15.765947+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 556
}
```

</details>

---


### Tool call

_source line 528 · 2026-05-22T15:08:15.766365+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 529 · 2026-05-22T15:08:16.371478+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 605
}
```

</details>

---


### Tool call

_source line 530 · 2026-05-22T15:08:16.472268+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 531 · 2026-05-22T15:08:17.375995+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 532 · 2026-05-22T15:08:17.526793+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ARR review form: all fields, all scoring dimensions (soundness, excitement, overall assessment, confidence, reproducibility, etc.), the exact numerical scales (1-5), and what each score level means. I need the full rubric."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete ARR review form: all fields, all scoring dimensions (soundness, excitement, overall assessment, confidence, reproducibility, etc.), the exact numerical scales (1-5), and what each score level means. I need the full rubric."
  }
}
```

</details>

---


### Tool result

_source line 533 · 2026-05-22T15:08:25.861994+00:00_

# ACL Rolling Review Form Structure

## Core Review Sections

**Paper Summary**: Describe the paper's topic and highlight potential misunderstandings.

**Summary of Strengths**: Explain reasons for publication at selective *ACL venues, including methodology, empirical results, or theoretical analysis.

**Summary of Weaknesses**: Number concerns about correctness, impact, clarity, or other publication barriers.

**Comments/Suggestions/Typos**: Additional improvement recommendations beyond addressing weaknesses.

## Scoring Dimensions

### Reviewer Confidence (1-5 scale)
- 5: "Positive that my evaluation is correct"
- 4: Quite sure; unlikely to have missed important details
- 3: Pretty sure; chance of missing details or not checking carefully
- 2: Willing to defend but likely missed details or novelty unclear
- 1: "Not my area, or paper is very hard to understand"

### Soundness (1-5 scale with half-points)
- 5: "Excellent: This study is one of the most thorough I have seen"
- 4: Strong; sufficient support with possible minor gaps
- 3: Acceptable; main claims supported with minor issues
- 2: Poor; main claims lack sufficient support
- 1: "Major Issues: This study is not yet sufficiently thorough"

### Excitement (1-5 scale with half-points)
- 5: "Highly Exciting: I would recommend this paper to others"
- 4: "Exciting: I would mention this paper to others"
- 3: Interesting; might mention or attend if time permits
- 2: "Potentially Interesting: does not resonate with me"
- 1: "Not Exciting: does not resonate with me"

### Overall Assessment (1-5 scale with half-points)
- 5: Consider for Award (top 2.5% papers)
- 4.5: Borderline Award
- 4: Conference acceptance
- 3.5: Borderline Conference
- 3: Findings acceptance
- 2.5: Borderline Findings
- 2: "Resubmit next cycle"
- 1.5: "Resubmit after next cycle"
- 1: Do not resubmit

## Additional Evaluation Dimensions

**Reproducibility** (1-5): Ability to reproduce results or build upon work

**Datasets** (1-5): Value of newly re
…[truncated 382 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8335
}
```

</details>

---


### Tool call

_source line 534 · 2026-05-22T15:08:33.548463+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 535 · 2026-05-22T15:08:33.852277+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 536 · 2026-05-22T15:08:33.957764+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 409
}
```

</details>

---


### Tool result

_source line 537 · 2026-05-22T15:08:34.312029+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 459
}
```

</details>

---


### Tool call

_source line 538 · 2026-05-22T15:12:48.019175+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿意见 — 方法严谨性审查\n\n**论文**: \"Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Analysis\"\n**Venue**: EMNLP 2026 (ACL Rolling Review)\n\n---\n\n## 总体评分\n**Overall Assessment**: 3.5 (Borderline Conference)\n**一句话总结**: 将 G-theory 系统性地应用于 LLM 评估方差分解是有价值的方法论贡献，实验规模可观（~2.3M observations, 7 facets），但 binary scoring 的根本性局限、D-study 不变性假设的验证不足、以及标题与实际范围的错位，使论文在当前形态下处于 Conference 边界。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心方法论合理，robustness analyses 覆盖了主要质疑方向，但 Henderson Method I 在 binary 数据上的验证深度不够（probit simulation 仅验证 ranking, Spearman=0.73 为中等相关），D-study invariance 假设缺乏独立验证 |\n| Excitement | 3.5/5 | G-theory 应用于 LLM 评估属新颖且实用的贡献，D-study budget 和 calculator 有直接实践价值；但范围限于 7-9B binary scoring 降低了 excitement |\n| Reproducibility | 4/5 | 论文承诺释放代码、数据和 D-study calculator（Appendix C），实验设计细节充分（Table 1, Appendix E），prompt 模板完整给出（p14） |\n| Confidence | 4/5 | 本人熟悉 G-theory、IRT、bootstrap 方法及 LLM 评估实践，对核心方法论评估有信心 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Henderson Method I 在 binary 数据上的验证深度不足\n\n- **具体位置**: §3.5 (Binary Data Assumptions, p5), Appendix A (Probit simulation, p11)\n- **问题**: 论文使用 Henderson Method I（本质为 ANOVA-based estimator，假设正态分布残差）处理 binary (0/1) 数据，提供了三项 robustness check：(a) probit simulation (Spearman=0.7312)，(b) GLMM complement（保持 7 个 grouped component orderings），(c) accuracy-range stability (r=−0.016)。然而：\n  - **Probit simulation 仅验证 ranking preservation**，Spearman=0.73 仅为中等相关，意味着约 47% 的 ranking variance 未被保留。论文未报告绝对量级恢复精度（如各方差分量的 RMSE 或 bias），无法判断 D-study 推算所依赖的 point estimates 偏差多大。\n  - **GLMM complement 的验证标准过松**：\"orderings ≥ 1.0\" 仅要求 7 个分组排序一致，未检验各方差分量的比例是否一致。例如，item 占 35% vs. 55% 都可能满足排序不变，但会导致完全不同的 D-study budgets。\n  - **Accuracy-range stability** 是有用的 sanity check 但不直接回应 binary-vs-continuous 问题。\n- **为什么影响接收**: G-theory 方差分量的 point estimates 是全文 D-study projections（§4.5, Table 4, Table 7）的基础。如果 binary scoring 下 Henderson Method I 的 estimates 存在系统性 bias（即使 rankings 大致保留），所有 budget 推荐（如\"3-prompt × 3-seed, 178 items for G≥0.80\"）的数值可靠性无法保证。\n- **建议修改方向**: (1) 在 probit simulation 中增加方差分量 point estimate 的 bias/RMSE 报告；(2) 对 GLMM 输出的方差分量比例与 Henderson Method I 做定量对比（如 mean absolute percentage error），而非仅验证 orderings。\n\n**N2** [critical] D-study 方差分量不变性假设缺乏充分验证\n\n- **具体位置**: §4.5 (Design-Dependent Reproducibility Budgets, p8), Table 4, Table 8 (Forward prediction, p12-13)\n- **问题**: D-study 从 observed variance components 外推到不同 design budgets，核心假设是方差分量在 item pool expansion、model universe expansion 和 temporal drift 下保持不变。论文的验证包括：\n  - **Forward prediction (Table 8)**: 从 4 个 exp-001 models 预测到 8 个 models，MC |ΔG|≤0.029, FF |ΔG|≤0.065。但这 4 个模型是 8 个模型的子集，不是独立样本。这是 in-sample cross-validation 而非 out-of-sample validation。\n  - **LOMO stability (Table 5)**: 删除单个 benchmark 后 G_abs 变化小。但这是 benchmark-level 稳定性，不直接验证 item pool expansion 的不变性。\n  - **Table 6**: Random vs. fixed model 的 G 系数差异很小（mean |ΔG|=0.002）。这支持 quasi-random assumption 但不验证 temporal invariance。\n  - **Temporal drift**: Limitations (§6) 提到 \"temporal correlation may limit exchangeability\" 但没有任何 empirical evidence。\n- **为什么影响接收**: 论文的核心实用价值在于 D-study budget 推荐（如 Table 4 的\"recommended 3-prompt × 3-seed\"），如果方差分量在 model universe 扩展（如从 8 个 7-9B models 到包含 70B 或不同 architecture 的 models）后显著变化，这些推荐便不可用。\n- **建议修改方向**: (1) 使用真正的 held-out models（非 exp-001 子集）做 forward prediction；(2) 至少讨论 temporal invariance 的 plausibility bounds——例如，引用文献中已知的 LLM benchmark saturation / performance ceiling 变化趋势来 bound drift magnitude。\n\n**N3** [critical] 标题 overclaiming：scope 远窄于 \"Open-Weight LLM Evaluation\"\n\n- **具体位置**: Title, Abstract (p1), Limitations §6 (p9)\n- **问题**: 标题 \"Reproducibility Budgets for Open-Weight LLM Evaluation\" 暗示覆盖 open-weight LLM 评估的一般情况。实际范围：\n  - **Models**: 8 个 7-9B instruction-tuned models（Table 10, p14）。不含 base models、>9B models（如 70B）、也不含非 Transformer architectures。\n  - **Scoring**: 仅 binary correctness (1/0)。§4.4 的 partial-credit pilot 显示 scoring granularity 根本性改变方差结构（G_abs 从 0.770→0.523, item difficulty ρ=0.26）。\n  - **Benchmarks**: 5 个 benchmarks（MMLU, ARC, HellaSwag, GSM8K, MATH），均为 closed-ended knowledge/reasoning tasks。不含 open-ended generation、code generation、multi-turn dialogue。\n  - **Format**: §4.3 的 format analysis 基于 n=5 benchmarks，permutation p=0.10（resolution floor）。\n- **为什么影响接收**: Title overclaiming 是 ARR 审稿中常见的扣分点。读者可能基于标题期望广泛适用的 budget 推荐，但实际上这些推荐仅对 7-9B instruction-tuned models + binary scoring + closed-ended benchmarks 有效。\n- **建议修改方向**: 修改标题增加限定，如 \"Reproducibility Budgets for Binary-Scored Open-Weight LLM Evaluation at the 7–9B Scale\" 或类似措辞。至少在 abstract 的第一句话中明确范围限定（目前 abstract 说 \"open-weight 7-9B parameter instruction-tuned models\" 但标题不含此限定）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Partial-credit pilot 的发现未被充分讨论，implications 被低估\n\n- **具体位置**: §4.4 最后一段 (p8), §6 Limitations (p9)\n- **问题**: §4.4 报告了 binary vs. step-level partial credit 的对比：prompt template variance 从 25.5%→1.2%, residual 从 28.2%→46.9%, G_abs 从 0.770→0.523, item difficulty rankings ρ=0.26。这些数字显示方差结构发生了**根本性**改变——不是微调，而是质变。然而论文仅用一段话（~4行）报告此发现，并在 Limitations 中以一句话带过 (\"A pilot partial-credit analysis confirms that scoring granularity fundamentally reshapes variance structure\")。\n- **影响**: 当 ρ=0.26（item difficulty rankings 几乎不相关），这意味着 binary scoring 下观察到的 \"item difficulty dominates variance\" 这一核心结论可能是 binary scoring 的 artifact 而非评估管道的固有属性。这对论文的 generalizability claim 是一个重大 caveat，值得更显著的讨论。\n- **建议**: 在 §5 Conclusion 或 §4.4 中增加一个独立段落讨论此发现的 implications：binary scoring 下的 D-study budgets 是否为 upper bounds 或 lower bounds？partial credit scoring 下是否需要更多还是更少的 items？\n\n**W2** [warning] §4.3 Format-associated patterns 的统计基础薄弱\n\n- **具体位置**: §4.3 (p6-7), Table 3 (p7)\n- **问题**: \n  - n=5 benchmarks 下的 permutation test p=0.10 是该样本量的最小可能 p 值（C(5,3)=10 种 MC/FF 划分中仅有 1 种比观察到的更极端）。论文正确标注了 \"Exploratory\" 但 §5 Conclusion 中仍将 format-associated differences 作为主要 finding 之一陈述（\"We observe suggestive but underpowered format-associated differences in variance concentration\"）。\n  - **MC vs. FF 设计不对称性**: ordering facet 仅对 MC benchmarks 有意义（FF 中 r_order=0 by construction），且 MC 和 FF 的 prompt templates 本质不同（MC: 选择选项; FF: 自由生成）。这意味着 \"format effect\" 与 prompt structure effect 存在混淆——观察到的 MC/FF 方差结构差异可能部分归因于 prompt template 设计差异而非 format 本身。\n- **建议**: (1) 在 §4.3 中明确讨论 format-prompt confound；(2) 在 §5 中降低 format finding 的 claim 强度——将其定位为 \"hypothesis-generating observation\" 而非 finding。\n\n**W3** [warning] 8 个 models 作为 \"quasi-random facet\" 的辩护不够充分\n\n- **具体位置**: §3.2 (Facets 段落, p4), Table 10 (p14)\n- **问题**: 论文引用 Meredith (1993) 和 Patrick & Bernstein (2016) 来辩护将 8 个 purposively selected models 视为 quasi-random facet。但 quasi-random sampling 的适用条件比较苛刻——要求样本能\"代表\" target universe 的 heterogeneity。这 8 个模型全部是 7-9B instruction-tuned models，来自有限的 architecture families（Llama, Mistral, OLMo, Qwen, Gemma）。Table 6 显示 random vs. fixed model 的 G 差异很小，但这只说明在这 8 个模型内部差异有限，不能证明它们代表了 \"open-weight instruction-tuned models\" 的 universe。\n- **影响**: D-study 推算中 \"increasing number of models\" 的外推依赖此假设。如果 universe 中包含 70B models 或不同 training paradigm 的 models，model×item interaction 可能显著不同。\n- **建议**: (1) 在 §3.2 中更明确地定义 target universe（\"7-9B instruction-tuned models from diverse architecture families\"而非笼统的 \"open-weight\"）；(2) 增加讨论 quasi-random assumption 在 model universe expansion 下的 breakdown conditions。\n\n**W4** [warning] Bootstrap CI 的 item-level resampling 可能低估不确定性\n\n- **具体位置**: §3.1 最后一段 (p4), Appendix A (CI method comparison, p11)\n- **问题**: Bootstrap 使用 item-level resampling with replacement (1,000 resamples)。在 fully crossed design 中，observations 嵌套在 items 内且同时嵌套在 models/conditions 内。Item-level resampling 保留了 item 内的条件结构，但忽略了 model-level clustering。Appendix A 报告 stratified bootstrap by subject (10 subjects × 20 items) 产生的 CI 在 simple item-level bootstrap 的 4% 以内——但这是 subject-level stratification，不是 model-level stratification。\n- **影响**: 如果 model-level variance 对 CI 有贡献（考虑到 model 是 fixed/quasi-random 的仅 8 个水平），item-only resampling 可能产生过窄的 CI。\n- **建议**: 补充一个 model-level jackknife 或 leave-one-model-out bootstrap 的 CI 比较，验证 item-level resampling 的 coverage 是否充分。实际上 Table 5 (LOMO) 已有 leave-one-model-out 的 G_abs 变化，但没有转化为 CI 比较。\n\n---\n\n## 小问题（不影响接收）\n\n- §3.2 (p4): \"arbitrarily chosen seed 42\" — 建议替换为 \"pre-specified seed\" 以避免暗示 seed 选择的随意性可能影响结果。\n- Table 1 (p5): \"Total records\" 行显示 480,800 和 2,304,000，但正文 (p1 abstract) 说 \"approximately 2.3 million\"。建议统一表述或解释 exp-001 与 exp-002 的 record 总和。\n- Figure 1 (p2): Y 轴标签 \"Generalizability Coefficient\" 偏小，建议增大字号以提高可读性。\n- §4.1 (p6): \"Variance components are estimated via Henderson Method I with bootstrap confidence intervals (1,000 resamples)\" — \"1,000 resamples\" 较少，考虑增加到 5,000-10,000 以改善 CI tail stability。\n- Appendix E (p14): Prompt templates 的格式化很好，但缺少 temperature 和 seed 的具体取值列表——虽然 Table 1 有列出，但 Appendix 中的完整 factorial 描述会更方便 reproducibility。\n\n---\n\n## 主要优势\n\n1. **方法论新颖性**: 首次将 G-theory 的完整框架（variance decomposition → G/D-study → budget projections）系统性应用于 LLM 评估，填补了现有文献只做单一方差源分析的空白。\n2. **实验规模与设计严谨性**: 7-facet fully crossed design 跨 5 个 benchmarks，总计约 2.3M binary observations，是该领域最大规模的系统性方差分析。实验细节充分（Table 1, Appendix E 的 prompt templates, Table 10 的 model 列表）。\n3. **实用产出**: D-study budget 推荐（Table 4, Table 7）和承诺释放的 G-theory calculator 为 practitioner 提供了直接可操作的工具，有真实的社区价值。\n4. **Robustness 意识**: 论文主动预判了 binary scoring、quasi-random model 等方法论质疑，提供了多项 robustness check（probit simulation, GLMM, accuracy-range stability, LOMO, forward prediction），尽管验证深度仍有改进空间。\n5. **Partial-credit pilot 的诚实性**: §4.4 如实报告了 binary vs. partial-credit 的巨大差异（ρ=0.26），没有回避这一不利发现。\n6. **Cross-benchmark 比较**: exp-002 的 reduced crossing 设计允许跨 benchmark 的方差结构比较，揭示了 item-dominated (MC) vs. model×item-dominated (FF) 的格式分化模式，即使统计功效有限，仍是有价值的探索性发现。\n\n---\n\n## Questions for Authors\n\nQ1: 在 probit simulation (Appendix A) 中，Spearman=0.7312 意味着 binary Henderson Method I 的方差分量 rankings 与 continuous-scale 的 rankings 有约 27% 的不一致。能否报告各方差分量 point estimate 的 bias（如 mean relative error）？这对 D-study budget 推荐的数值可靠性至关重要。\n\nQ2: Forward prediction (Table 8) 使用的 4 个 models 是 8 个 models 的子集。是否考虑过使用完全不同的 held-out models（如不在 exp-001 和 exp-002 中的 models）做 out-of-sample validation？如果没有，是否有实际困难（如计算资源）阻止了此验证？\n\nQ3: Partial-credit pilot 显示 item difficulty rankings 在 binary vs. partial credit 下几乎不相关（ρ=0.26）。这是否意味着 binary scoring 下观察到的 \"item difficulty dominates variance\" 可能主要是 binary threshold 的 artifact（即难题和易题在 binary 下产生极端 0/1 分布，人为放大 item variance share）？\n\nQ4: §4.3 的 format analysis 中，MC 和 FF benchmarks 使用不同的 prompt templates（MC 含选项选择指令，FF 含自由生成指令）。ordering facet 也仅对 MC 有意义。如何排除观察到的 MC/FF 方差结构差异来自 prompt design 差异而非 format 本身？\n\nQ5: 论文的 target model universe 定义为 \"open-weight 7-9B instruction-tuned models\"（§3.2）。D-study budget 推荐（Table 4, Table 7）是否仅适用于此范围？如果 practitioner 的 evaluation universe 包含 70B models 或 base models，这些 budgets 的 transferability 如何？\n\n---\n\n## Missing References\n\n- Jiang & Skorupski (2018) 在 Appendix A 中被引用来支持 GLMM complement，但正文 §3.5 中未引用。建议在 §3.5 讨论 binary data 时引用此方法论依据。\n- 关于 G-theory 在 binary/dichotomous data 上的适用性，Brennan (2001, Ch. 12) 在正文中被引用，但缺少 Cardinet, Johnson & Pini (2010) 的 \"Applying Generalizability Theory using EduG\" 中关于 dichotomous data 的专门讨论，这是 G-theory 社区的标准参考。\n- 关于 LLM benchmark saturation 和 temporal drift，Kiela et al. (2021) \"Dynabench: Rethinking Benchmarking in NLP\" 讨论了 benchmark 随时间退化的问题，可加强 §6 Limitations 中 temporal invariance 的讨论。",
  "reviewer_id": "1",
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿意见 — 方法严谨性审查\n\n**论文**: \"Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Analysis\"\n**Venue**: EMNLP 2026 (ACL Rolling Review)\n\n---\n\n## 总体评分\n**Overall Assessment**: 3.5 (Borderline Conference)\n**一句话总结**: 将 G-theory 系统性地应用于 LLM 评估方差分解是有价值的方法论贡献，实验规模可观（~2.3M observations, 7 facets），但 binary scoring 的根本性局限、D-study 不变性假设的验证不足、以及标题与实际范围的错位，使论文在当前形态下处于 Conference 边界。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心方法论合理，robustness analyses 覆盖了主要质疑方向，但 Henderson Method I 在 binary 数据上的验证深度不够（probit simulation 仅验证 ranking, Spearman=0.73 为中等相关），D-study invariance 假设缺乏独立验证 |\n| Excitement | 3.5/5 | G-theory 应用于 LLM 评估属新颖且实用的贡献，D-study budget 和 calculator 有直接实践价值；但范围限于 7-9B binary scoring 降低了 excitement |\n| Reproducibility | 4/5 | 论文承诺释放代码、数据和 D-study calculator（Appendix C），实验设计细节充分（Table 1, Appendix E），prompt 模板完整给出（p14） |\n| Confidence | 4/5 | 本人熟悉 G-theory、IRT、bootstrap 方法及 LLM 评估实践，对核心方法论评估有信心 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Henderson Method I 在 binary 数据上的验证深度不足\n\n- **具体位置**: §3.5 (Binary Data Assumptions, p5), Appendix A (Probit simulation, p11)\n- **问题**: 论文使用 Henderson Method I（本质为 ANOVA-based estimator，假设正态分布残差）处理 binary (0/1) 数据，提供了三项 robustness check：(a) probit simulation (Spearman=0.7312)，(b) GLMM complement（保持 7 个 grouped component orderings），(c) accuracy-range stability (r=−0.016)。然而：\n  - **Probit simulation 仅验证 ranking preservation**，Spearman=0.73 仅为中等相关，意味着约 47% 的 ranking variance 未被保留。论文未报告绝对量级恢复精度（如各方差分量的 RMSE 或 bias），无法判断 D-study 推算所依赖的 point estimates 偏差多大。\n  - **GLMM complement 的验证标准过松**：\"orderings ≥ 1.0\" 仅要求 7 个分组排序一致，未检验各方差分量的比例是否一致。例如，item 占 35% vs. 55% 都可能满足排序不变，但会导致完全不同的 D-study budgets。\n  - **Accuracy-range stability** 是有用的 sanity check 但不直接回应 binary-vs-continuous 问题。\n- **为什么影响接收**: G-theory 方差分量的 point estimates 是全文 D-study projections（§4.5, Table 4, Table 7）的基础。如果 binary scoring 下 Henderson Method I 的 estimates 存在系统性 bias（即使 rankings 大致保留），所有 budget 推荐（如\"3-prompt × 3-seed, 178 items for G≥0.80\"）的数值可靠性无法保证。\n- **建议修改方向**: (1) 在 probit simulation 中增加方差分量 point estimate 的 bias/RMSE 报告；(2) 对 GLMM 输出的方差分量比例与 Henderson Method I 做定量对比（如 mean absolute percentage error），而非仅验证 orderings。\n\n**N2** [critical] D-study 方差分量不变性假设缺乏充分验证\n\n- **具体位置**: §4.5 (Design-Dependent Reproducibility Budgets, p8), Table 4, Table 8 (Forward prediction, p12-13)\n- **问题**: D-study 从 observed variance components 外推到不同 design budgets，核心假设是方差分量在 item pool expansion、model universe expansion 和 temporal drift 下保持不变。论文的验证包括：\n  - **Forward prediction (Table 8)**: 从 4 个 exp-001 models 预测到 8 个 models，MC |ΔG|≤0.029, FF |ΔG|≤0.065。但这 4 个模型是 8 个模型的子集，不是独立样本。这是 in-sample cross-validation 而非 out-of-sample validation。\n  - **LOMO stability (Table 5)**: 删除单个 benchmark 后 G_abs 变化小。但这是 benchmark-level 稳定性，不直接验证 item pool expansion 的不变性。\n  - **Table 6**: Random vs. fixed model 的 G 系数差异很小（mean |ΔG|=0.002）。这支持 quasi-random assumption 但不验证 temporal invariance。\n  - **Temporal drift**: Limitations (§6) 提到 \"temporal correlation may limit exchangeability\" 但没有任何 empirical evidence。\n- **为什么影响接收**: 论文的核心实用价值在于 D-study budget 推荐（如 Table 4 的\"recommended 3-prompt × 3-seed\"），如果方差分量在 model universe 扩展（如从 8 个 7-9B models 到包含 70B 或不同 architecture 的 models）后显著变化，这些推荐便不可用。\n- **建议修改方向**: (1) 使用真正的 held-out models（非 exp-001 子集）做 forward prediction；(2) 至少讨论 temporal invariance 的 plausibility bounds——例如，引用文献中已知的 LLM benchmark saturation / performance ceiling 变化趋势来 bound drift magnitude。\n\n**N3** [critical] 标题 overclaiming：scope 远窄于 \"Open-Weight LLM Evaluation\"\n\n- **具体位置**: Title, Abstract (p1), Limitations §6 (p9)\n- **问题**: 标题 \"Reproducibility Budgets for Open-Weight LLM Evaluation\" 暗示覆盖 open-weight LLM 评估的一般情况。实际范围：\n  - **Models**: 8 个 7-9B instruction-tuned models（Table 10, p14）。不含 base models、>9B models（如 70B）、也不含非 Transformer architectures。\n  - **Scoring**: 仅 binary correctness (1/0)。§4.4 的 partial-credit pilot 显示 scoring granularity 根本性改变方差结构（G_abs 从 0.770→0.523, item difficulty ρ=0.26）。\n  - **Benchmarks**: 5 个 benchmarks（MMLU, ARC, HellaSwag, GSM8K, MATH），均为 closed-ended knowledge/reasoning tasks。不含 open-ended generation、code generation、multi-turn dialogue。\n  - **Format**: §4.3 的 format analysis 基于 n=5 benchmarks，permutation p=0.10（resolution floor）。\n- **为什么影响接收**: Title overclaiming 是 ARR 审稿中常见的扣分点。读者可能基于标题期望广泛适用的 budget 推荐，但实际上这些推荐仅对 7-9B instruction-tuned models + binary scoring + closed-ended benchmarks 有效。\n- **建议修改方向**: 修改标题增加限定，如 \"Reproducibility Budgets for Binary-Scored Open-Weight LLM Evaluation at the 7–9B Scale\" 或类似措辞。至少在 abstract 的第一句话中明确范围限定（目前 abstract 说 \"open-weight 7-9B parameter instruction-tuned models\" 但标题不含此限定）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Partial-credit pilot 的发现未被充分讨论，implications 被低估\n\n- **具体位置**: §4.4 最后一段 (p8), §6 Limitations (p9)\n- **问题**: §4.4 报告了 binary vs. step-level partial credit 的对比：prompt template variance 从 25.5%→1.2%, residual 从 28.2%→46.9%, G_abs 从 0.770→0.523, item difficulty rankings ρ=0.26。这些数字显示方差结构发生了**根本性**改变——不是微调，而是质变。然而论文仅用一段话（~4行）报告此发现，并在 Limitations 中以一句话带过 (\"A pilot partial-credit analysis confirms that scoring granularity fundamentally reshapes variance structure\")。\n- **影响**: 当 ρ=0.26（item difficulty rankings 几乎不相关），这意味着 binary scoring 下观察到的 \"item difficulty dominates variance\" 这一核心结论可能是 binary scoring 的 artifact 而非评估管道的固有属性。这对论文的 generalizability claim 是一个重大 caveat，值得更显著的讨论。\n- **建议**: 在 §5 Conclusion 或 §4.4 中增加一个独立段落讨论此发现的 implications：binary scoring 下的 D-study budgets 是否为 upper bounds 或 lower bounds？partial credit scoring 下是否需要更多还是更少的 items？\n\n**W2** [warning] §4.3 Format-associated patterns 的统计基础薄弱\n\n- **具体位置**: §4.3 (p6-7), Table 3 (p7)\n- **问题**: \n  - n=5 benchmarks 下的 permutation test p=0.10 是该样本量的最小可能 p 值（C(5,3)=10 种 MC/FF 划分中仅有 1 种比观察到的更极端）。论文正确标注了 \"Exploratory\" 但 §5 Conclusion 中仍将 format-associated differences 作为主要 finding 之一陈述（\"We observe suggestive but underpowered format-associated differences in variance concentration\"）。\n  - **MC vs. FF 设计不对称性**: ordering facet 仅对 MC benchmarks 有意义（FF 中 r_order=0 by construction），且 MC 和 FF 的 prompt templates 本质不同（MC: 选择选项; FF: 自由生成）。这意味着 \"format effect\" 与 prompt structure effect 存在混淆——观察到的 MC/FF 方差结构差异可能部分归因于 prompt template 设计差异而非 format 本身。\n- **建议**: (1) 在 §4.3 中明确讨论 format-prompt confound；(2) 在 §5 中降低 format finding 的 claim 强度——将其定位为 \"hypothesis-generating observation\" 而非 finding。\n\n**W3** [warning] 8 个 models 作为 \"quasi-random facet\" 的辩护不够充分\n\n- **具体位置**: §3.2 (Facets 段落, p4), Table 10 (p14)\n- **问题**: 论文引用 Meredith (1993) 和 Patrick & Bernstein (2016) 来辩护将 8 个 purposively selected models 视为 quasi-random facet。但 quasi-random sampling 的适用条件比较苛刻——要求样本能\"代表\" target universe 的 heterogeneity。这 8 个模型全部是 7-9B instruction-tuned models，来自有限的 architecture families（Llama, Mistral, OLMo, Qwen, Gemma）。Table 6 显示 random vs. fixed model 的 G 差异很小，但这只说明在这 8 个模型内部差异有限，不能证明它们代表了 \"open-weight instruction-tuned models\" 的 universe。\n- **影响**: D-study 推算中 \"increasing number of models\" 的外推依赖此假设。如果 universe 中包含 70B models 或不同 training paradigm 的 models，model×item interaction 可能显著不同。\n- **建议**: (1) 在 §3.2 中更明确地定义 target universe（\"7-9B instruction-tuned models from diverse architecture families\"而非笼统的 \"open-weight\"）；(2) 增加讨论 quasi-random assumption 在 model universe expansion 下的 breakdown conditions。\n\n**W4** [warning] Bootstrap CI 的 item-level resampling 可能低估不确定性\n\n- **具体位置**: §3.1 最后一段 (p4), Appendix A (CI method comparison, p11)\n- **问题**: Bootstrap 使用 item-level resampling with replacement (1,000 resamples)。在 fully crossed design 中，observations 嵌套在 items 内且同时嵌套在 models/conditions 内。Item-level resampling 保留了 item 内的条件结构，但忽略了 model-level clustering。Appendix A 报告 stratified bootstrap by subject (10 subjects × 20 items) 产生的 CI 在 simple item-level bootstrap 的 4% 以内——但这是 subject-level stratification，不是 model-level stratification。\n- **影响**: 如果 model-level variance 对 CI 有贡献（考虑到 model 是 fixed/quasi-random 的仅 8 个水平），item-only resampling 可能产生过窄的 CI。\n- **建议**: 补充一个 model-level jackknife 或 leave-one-model-out bootstrap 的 CI 比较，验证 item-level resampling 的 coverage 是否充分。实际上 Table 5 (LOMO) 已有 leave-one-model-out 的 G_abs 变化，但没有转化为 CI 比较。\n\n---\n\n## 小问题（不影响接收）\n\n- §3.2 (p4): \"arbitrarily chosen seed 42\" — 建议替换为 \"pre-specified seed\" 以避免暗示 seed 选择的随意性可能影响结果。\n- Table 1 (p5): \"Total records\" 行显示 480,800 和 2,304,000，但正文 (p1 abstract) 说 \"approximately 2.3 million\"。建议统一表述或解释 exp-001 与 exp-002 的 record 总和。\n- Figure 1 (p2): Y 轴标签 \"Generalizability Coefficient\" 偏小，建议增大字号以提高可读性。\n- §4.1 (p6): \"Variance components are estimated via Henderson Method I with bootstrap confidence intervals (1,000 resamples)\" — \"1,000 resamples\" 较少，考虑增加到 5,000-10,000 以改善 CI tail stability。\n- Appendix E (p14): Prompt templates 的格式化很好，但缺少 temperature 和 seed 的具体取值列表——虽然 Table 1 有列出，但 Appendix 中的完整 factorial 描述会更方便 reproducibility。\n\n---\n\n## 主要优势\n\n1. **方法论新颖性**: 首次将 G-theory 的完整框架（variance decomposition → G/D-study → budget projections）系统性应用于 LLM 评估，填补了现有文献只做单一方差源分析的空白。\n2. **实验规模与设计严谨性**: 7-facet fully crossed design 跨 5 个 benchmarks，总计约 2.3M binary observations，是该领域最大规模的系统性方差分析。实验细节充分（Table 1, Appendix E 的 prompt templates, Table 10 的 model 列表）。\n3. **实用产出**: D-study budget 推荐（Table 4, Table 7）和承诺释放的 G-theory calculator 为 practitioner 提供了直接可操作的工具，有真实的社区价值。\n4. **Robustness 意识**: 论文主动预判了 binary scoring、quasi-random model 等方法论质疑，提供了多项 robustness check（probit simulation, GLMM, accuracy-range stability, LOMO, forward prediction），尽管验证深度仍有改进空间。\n5. **Partial-credit pilot 的诚实性**: §4.4 如实报告了 binary vs. partial-credit 的巨大差异（ρ=0.26），没有回避这一不利发现。\n6. **Cross-benchmark 比较**: exp-002 的 reduced crossing 设计允许跨 benchmark 的方差结构比较，揭示了 item-dominated (MC) vs. model×item-dominated (FF) 的格式分化模式，即使统计功效有限，仍是有价值的探索性发现。\n\n---\n\n## Questions for Authors\n\nQ1: 在 probit simulation (Appendix A) 中，Spearman=0.7312 意味着 binary Henderson Method I 的方差分量 rankings 与 continuous-scale 的 rankings 有约 27% 的不一致。能否报告各方差分量 point estimate 的 bias（如 mean relative error）？这对 D-study budget 推荐的数值可靠性至关重要。\n\nQ2: Forward prediction (Table 8) 使用的 4 个 models 是 8 个 models 的子集。是否考虑过使用完全不同的 held-out models（如不在 exp-001 和 exp-002 中的 models）做 out-of-sample validation？如果没有，是否有实际困难（如计算资源）阻止了此验证？\n\nQ3: Partial-credit pilot 显示 item difficulty rankings 在 binary vs. partial credit 下几乎不相关（ρ=0.26）。这是否意味着 binary scoring 下观察到的 \"item difficulty dominates variance\" 可能主要是 binary threshold 的 artifact（即难题和易题在 binary 下产生极端 0/1 分布，人为放大 item variance share）？\n\nQ4: §4.3 的 format analysis 中，MC 和 FF benchmarks 使用不同的 prompt templates（MC 含选项选择指令，FF 含自由生成指令）。ordering facet 也仅对 MC 有意义。如何排除观察到的 MC/FF 方差结构差异来自 prompt design 差异而非 format 本身？\n\nQ5: 论文的 target model universe 定义为 \"open-weight 7-9B instruction-tuned models\"（§3.2）。D-study budget 推荐（Table 4, Table 7）是否仅适用于此范围？如果 practitioner 的 evaluation universe 包含 70B models 或 base models，这些 budgets 的 transferability 如何？\n\n---\n\n## Missing References\n\n- Jiang & Skorupski (2018) 在 Appendix A 中被引用来支持 GLMM complement，但正文 §3.5 中未引用。建议在 §3.5 讨论 binary data 时引用此方法论依据。\n- 关于 G-theory 在 binary/dichotomous data 上的适用性，Brennan (2001, Ch. 12) 在正文中被引用，但缺少 Cardinet, Johnson & Pini (2010) 的 \"Applying Generalizability Theory using EduG\" 中关于 dichotomous data 的专门讨论，这是 G-theory 社区的标准参考。\n- 关于 LLM benchmark saturation 和 temporal drift，Kiela et al. (2021) \"Dynabench: Rethinking Benchmarking in NLP\" 讨论了 benchmark 随时间退化的问题，可加强 §6 Limitations 中 temporal invariance 的讨论。",
    "reviewer_id": "1",
    "project": "nlp_variance_gtheory"
  }
}
```

</details>

---


### Tool result

_source line 539 · 2026-05-22T15:12:52.047719+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_265de443abfe4594f91451b075b582ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4028
}
```

</details>

---


### Tool call

_source line 540 · 2026-05-22T15:12:56.937006+00:00_

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
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
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

_source line 541 · 2026-05-22T15:12:56.987633+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 542 · 2026-05-22T15:13:02.616748+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 543 · 2026-05-22T15:13:02.767597+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 150
}
```

</details>

---


### Assistant

_source line 544 · 2026-05-22T15:13:12.943297+00:00_

已完成。审稿意见已提交给 Review Director，核心评判：

- **Overall: 3.5 (Borderline Conference)**
- 3 个 Must-Fix：Henderson Method I 在 binary 数据上的验证深度不足、D-study 不变性假设缺独立验证、标题 overclaiming
- 4 个 Should-Fix：partial-credit 发现讨论不充分、format analysis 统计功效不足且存在 confound、quasi-random model 辩护薄弱、bootstrap CI 可能低估不确定性
- 主要优势：G-theory 应用新颖、实验规模大、实用产出（D-study calculator）、robustness 意识好

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1"
}
```

</details>

---


## Round 16

## Round 16

4 recorded events


### User

_source line 545 · 2026-05-22T15:17:13.588574+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2（新颖性/完整性审查）的完整审稿意见。请逐条回应其 Must-Fix 和 Should-Fix 问题：对每条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 完整审稿意见

**Overall**: 3.5 (Borderline Conference)

### Must-Fix 问题

**N1** [critical] "10× fewer items" headline 掩盖总评估成本的 100-200× 增加
- Abstract 以 "55 vs 552 items" 为核心 headline，cross-model projections 声称 "item reductions exceed 10× across all five benchmarks"。但总评估量的对比完全不同：
  - 单模型 full multi-facet: 55 items × 1,296 conditions = 71,280 evaluations vs single-condition 552 × 1 = 552 evaluations → 129× 更多评估量
  - Cross-model (Table 7, MMLU): 93 items × 2,304 conditions = 214,272 evaluations vs 1,216 × 1 = 1,216 evaluations → 176× 更多评估量
  - 推荐的 3×3 设计 (178 items × 9 = 1,602 evals vs 552 evals) 相对合理 (2.9× 更多评估量换取 3.1× 更少 items)，但这个 3.1× 远不如 headline 的 10×
- R2 认为论文的 value proposition 其实是 "同等 reliability 下更少 items（但更多 conditions per item）"——这需要前提条件：items 是瓶颈（如构建新 benchmark），而非 compute 是瓶颈。

**N2** [critical] 相对 Messing (2026) 的增量贡献需要更强的 justification
- Messing (2026) 已将 G-theory 引入 LLM 评测（TEE framework, judge identity 43.8%）。本文三个增量方向：
  - (i) infrastructure facets → 主要发现是 negligible (<1%)，确认零效应有价值但 excitement 有限
  - (ii) cross-benchmark → format comparison p=0.10，达到 resolution floor，标注为 exploratory
  - (iii) D-study budgets → 最强贡献，但 D-study 是 G-theory 标准操作
- R2 认为 "complementary" 定位意味着本文是 Messing 的应用延伸而非独立创新。

**N3** [critical] FF benchmarks 40-44% 残差方差缺乏解释性分析
- Table 3: GSM8K residual 39.9%, MATH 43.9%——最大 component 是残差。
- 论文承认 "likely reflect sources not captured by our facets" 但未做任何分析验证。
- 未分析 item 特征如何预测 model×item interaction 或残差大小。
- 当残差占主导时，D-study budgets 的可靠性存疑。

### Should-Fix 问题

**W1** Data contamination 作为 model×item interaction 的混淆变量未被讨论。model×item 30-36% 可能部分来自 contamination 而非 genuine DIF。
**W2** Contribution 层级权重不均：C2 (precision separability) 本质是 null result，C3 (toolkit) 是软件工程贡献，与 C1 并列 overclaiming。
**W3** ARC model×prompt 异常 (8.0%) 未讨论，远高于其他 MC benchmarks (<1.6%)。
**W4** Conclusion 过于简短（仅一段约 5 句），未充分讨论 practical implications。
**W5** Cross-benchmark 比较受非对称设计限制：MC 和 FF 的 prompt manipulation 质的不同，ordering 仅 MC 有意义。

### Missing References
- Data contamination: Golchin & Surdeanu (2023), Sainz et al. (2023)
- Dynamic benchmarking: Kiela et al. (2021) DynaBench

---

请对以上每条 N1-N3、W1-W5 逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 546 · 2026-05-22T15:18:49.488100+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: \"10× fewer items\" headline 掩盖总评估成本增加**\n\n同意此为 framing 问题。论文 abstract (p1) 确实同时给出了两组数字——\"178 items (1,602 total evaluations per model)\" vs \"552 items under single-condition\"——但 headline effect 仍然是 \"10× fewer items\"（p1 abstract 末尾: \"full multi-facet designs further reduce to 55 items\"；p2 第1段: \"item reductions exceed 10× across all five benchmarks\"）。这两处表述未附带总 evaluation 量对比，容易产生误导。\n\n不过，R2 的 cost 计算需要一个 nuance：**10× item reduction 的应用场景是 benchmark construction**（item 开发成本远高于 compute 成本），而 3.1× 的 3-prompt×3-seed 设计才是面向日常 evaluation 的推荐。论文在 §4.5 (p8) 确实区分了这两个 use case，但 abstract 和 §5 的 framing 未能清晰传达此区别。建议作者在 abstract 中明确 \"10× item reduction requires 1,296 conditions per item\" 的 tradeoff。\n\n---\n\n**[REBUT] R2-N2: 相对 Messing (2026) 增量贡献不足**\n\nR2 对三个增量方向的评估过于消极：\n\n(a) **Infrastructure facets negligible ≠ low value**。Messing (2026) 未交叉 infrastructure facets（precision, seed, temperature），因此 practitioners 在此之前无法知道这些因素是否重要。本文的 null result 直接回答了一个实际问题：是否需要控制 numerical precision 和 random seed？§4.1 (p6) 报告 precision <1%, seed <0.5%, temperature interaction 1.3%——这为 practitioners 提供了可操作的简化依据（如 Table 4 的 budget 推荐不含 precision 作为必控 facet）。Null results 在实验科学中与 positive results 同等重要，尤其当 community 中存在 \"precision matters\" 的 implicit assumption 时。\n\n(b) **Cross-benchmark comparison 虽 underpowered 但提供了 structural insight**。Messing (2026) 仅在单 benchmark 上工作（judge identity 43.8%），无法观察到本文 Table 3 (p7) 揭示的 MC vs. FF 方差结构分化：MC benchmarks 的 item-related variance 集中在 item main effect (MMLU 37.9%, ARC 34.3%)，而 FF benchmarks 将 variance 分散到 model×item interaction (GSM8K 37.9%, MATH 43.9% residual)。p=0.10 确实是 resolution floor，但 structural pattern 本身——MC item-dominated vs. FF interaction-dominated——在 Table 3 的全部 5 个 benchmarks 中一致，不是随机波动。\n\n(c) **D-study 虽是 G-theory 标准操作，但在 LLM 评估中的应用是新的**。R2 称 D-study 是 \"standard operation\" 是对方法论 novelty 和 application novelty 的混淆。G-theory 的 D-study 在教育测量中是标准的，但**从未被应用于 LLM 评估的 multi-facet crossed design**。Table 4 (p8) 和 Table 7 (p12) 的 budget 推荐是该领域第一组有 G-theory 支撑的 evidence-based reproducibility guidelines。\n\n综合看，本文与 Messing (2026) 的关系不是 \"应用延伸\" 而是 **互补但独立的贡献**：Messing 聚焦 judge variation（LLM-as-judge），本文聚焦 evaluation pipeline variation（direct scoring）。两者的 facet universe、design、应用场景均不同。\n\n---\n\n**[AGREE] R2-N3: FF benchmarks 40-44% 残差方差缺乏解释性分析**\n\n同意这是一个显著缺陷。Table 3 (p7) 显示 GSM8K residual 39.9%, MATH residual 43.9%（标注为 \"all others <0.1\"），这意味着**最大的方差来源是未建模的**。论文 §4.3 (p7) 仅以一句话承认 \"likely reflect sources not captured by our facets: chain-of-thought path diversity, generation stochasticity, and answer extraction heuristics\"，但未做任何验证。\n\n我在自己的审稿中未将此列为 Must-Fix，但 R2 的论证说服了我：当残差是最大 component 时，D-study projections 的基础被削弱——因为 D-study 假设所有 systematic variance 已被 facets 捕获，residual 仅为 random error。如果 FF benchmarks 的残差中含有 systematic（但未建模的）variance sources，Table 7 (p12) 的 cross-model budget projections 对 FF benchmarks 可能过于乐观。\n\n建议补充：(1) 分析 item-level features（如 solution length, reasoning steps）与 residual magnitude 的相关性；(2) 至少讨论 residual 中 systematic vs. random 的 plausible 比例。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Data contamination 作为 model×item interaction 的混淆变量**\n\n同意。Model×item interaction 占 30-36% (Table 2-3) 是本文最重要的发现之一，但 data contamination 是一个合理的 alternative explanation：如果某些 models 在训练中见过特定 benchmark items，这些 items 上的表现会系统性偏高，产生 DIF-like patterns，但原因不是 genuine differential functioning 而是 memorization。论文 §2 (p3) 引用了 IRT 文献讨论 DIF，但完全未提及 contamination。即使无法直接测量 contamination，至少应在 §4.2 或 §5 中将其列为 model×item interaction 的 candidate explanation 之一，并引用 Golchin & Surdeanu (2023) 等 contamination detection 文献。\n\n---\n\n**[AGREE] R2-W2: Contribution 层级权重不均**\n\n部分同意。§1 (p1-2) 列出三个 contributions：C1 (design-dependent budgets), C2 (precision separability), C3 (toolkit)。C2 本质上是 \"BF16/FP16/FP32 差异 negligible\" 的 null result，将其与 C1 并列确实 overclaiming。但我认为 R2 对 null result 的价值判断略低——C2 对 practitioners 有直接影响（不需要 FP32 evaluation），只是不应与 C1 并列为同等 contribution。建议作者将 C2 降级为 C1 的 sub-finding，C3 (toolkit) 从 contribution list 移至 practical implications。\n\n---\n\n**[AGREE] R2-W3: ARC model×prompt 异常 (8.0%) 未讨论**\n\n同意。Table 3 (p7) 显示 ARC 的 model×prompt interaction 为 8.0%，远高于其他 MC benchmarks（MMLU model×prompt 在 Table 2 中未单独列出但 all main facet effects <1% except prompt 0.9%）。这一异常值得至少一句话的解释——是否与 ARC 的 prompt template 设计有关（如 ARC 的选项数量/格式与 MMLU 不同）？\n\n---\n\n**[AGREE] R2-W4: Conclusion 过于简短**\n\n同意。§5 Conclusion (p8) 仅约 5 句话，未讨论 practical implications 的细节（如哪些 benchmarks 最需要 multi-facet design？practitioner 应如何选择 prompt 数量？）。考虑到 8 页 limit，空间有限，但 Conclusion 可以适当扩展以加强 takeaway message。\n\n---\n\n**[AGREE] R2-W5: Cross-benchmark 比较受非对称设计限制**\n\n同意，这与我自己的 W2 一致。MC 和 FF 的 prompt manipulation 本质不同（MC: 选项顺序/选择指令; FF: 生成策略），ordering facet 仅 MC 有意义——这使得 Table 3 的 MC vs. FF 比较不是 pure format comparison 而是 format + prompt design + ordering 的 compound comparison。论文 §4.3 (p7) 的 \"Exploratory\" 标注是恰当的，但未充分讨论这些 confounds。\n\n---\n\n### Missing References 回应\n\n- **Data contamination references**: 同意应引用。Golchin & Surdeanu (2023) 和 Sainz et al. (2023) 直接相关。\n- **Kiela et al. (2021) DynaBench**: 同意。我在自己的 Missing References 中也提到了这篇，可加强 §6 temporal drift 讨论。\n\n---\n\n### 总结\n\nR2 的 N1 (cost framing) 和 N3 (residual analysis) 我完全同意，这些是论文需要 fix 的实质问题。N2 (relative to Messing) 我不同意——本文与 Messing 的关系是互补而非增量延伸，R2 低估了 infrastructure null results 和 cross-benchmark structural insights 的价值。W1-W5 我基本同意，这些问题可修复但需要在修订中逐一 address。",
  "reviewer_id": "1",
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: \"10× fewer items\" headline 掩盖总评估成本增加**\n\n同意此为 framing 问题。论文 abstract (p1) 确实同时给出了两组数字——\"178 items (1,602 total evaluations per model)\" vs \"552 items under single-condition\"——但 headline effect 仍然是 \"10× fewer items\"（p1 abstract 末尾: \"full multi-facet designs further reduce to 55 items\"；p2 第1段: \"item reductions exceed 10× across all five benchmarks\"）。这两处表述未附带总 evaluation 量对比，容易产生误导。\n\n不过，R2 的 cost 计算需要一个 nuance：**10× item reduction 的应用场景是 benchmark construction**（item 开发成本远高于 compute 成本），而 3.1× 的 3-prompt×3-seed 设计才是面向日常 evaluation 的推荐。论文在 §4.5 (p8) 确实区分了这两个 use case，但 abstract 和 §5 的 framing 未能清晰传达此区别。建议作者在 abstract 中明确 \"10× item reduction requires 1,296 conditions per item\" 的 tradeoff。\n\n---\n\n**[REBUT] R2-N2: 相对 Messing (2026) 增量贡献不足**\n\nR2 对三个增量方向的评估过于消极：\n\n(a) **Infrastructure facets negligible ≠ low value**。Messing (2026) 未交叉 infrastructure facets（precision, seed, temperature），因此 practitioners 在此之前无法知道这些因素是否重要。本文的 null result 直接回答了一个实际问题：是否需要控制 numerical precision 和 random seed？§4.1 (p6) 报告 precision <1%, seed <0.5%, temperature interaction 1.3%——这为 practitioners 提供了可操作的简化依据（如 Table 4 的 budget 推荐不含 precision 作为必控 facet）。Null results 在实验科学中与 positive results 同等重要，尤其当 community 中存在 \"precision matters\" 的 implicit assumption 时。\n\n(b) **Cross-benchmark comparison 虽 underpowered 但提供了 structural insight**。Messing (2026) 仅在单 benchmark 上工作（judge identity 43.8%），无法观察到本文 Table 3 (p7) 揭示的 MC vs. FF 方差结构分化：MC benchmarks 的 item-related variance 集中在 item main effect (MMLU 37.9%, ARC 34.3%)，而 FF benchmarks 将 variance 分散到 model×item interaction (GSM8K 37.9%, MATH 43.9% residual)。p=0.10 确实是 resolution floor，但 structural pattern 本身——MC item-dominated vs. FF interaction-dominated——在 Table 3 的全部 5 个 benchmarks 中一致，不是随机波动。\n\n(c) **D-study 虽是 G-theory 标准操作，但在 LLM 评估中的应用是新的**。R2 称 D-study 是 \"standard operation\" 是对方法论 novelty 和 application novelty 的混淆。G-theory 的 D-study 在教育测量中是标准的，但**从未被应用于 LLM 评估的 multi-facet crossed design**。Table 4 (p8) 和 Table 7 (p12) 的 budget 推荐是该领域第一组有 G-theory 支撑的 evidence-based reproducibility guidelines。\n\n综合看，本文与 Messing (2026) 的关系不是 \"应用延伸\" 而是 **互补但独立的贡献**：Messing 聚焦 judge variation（LLM-as-judge），本文聚焦 evaluation pipeline variation（direct scoring）。两者的 facet universe、design、应用场景均不同。\n\n---\n\n**[AGREE] R2-N3: FF benchmarks 40-44% 残差方差缺乏解释性分析**\n\n同意这是一个显著缺陷。Table 3 (p7) 显示 GSM8K residual 39.9%, MATH residual 43.9%（标注为 \"all others <0.1\"），这意味着**最大的方差来源是未建模的**。论文 §4.3 (p7) 仅以一句话承认 \"likely reflect sources not captured by our facets: chain-of-thought path diversity, generation stochasticity, and answer extraction heuristics\"，但未做任何验证。\n\n我在自己的审稿中未将此列为 Must-Fix，但 R2 的论证说服了我：当残差是最大 component 时，D-study projections 的基础被削弱——因为 D-study 假设所有 systematic variance 已被 facets 捕获，residual 仅为 random error。如果 FF benchmarks 的残差中含有 systematic（但未建模的）variance sources，Table 7 (p12) 的 cross-model budget projections 对 FF benchmarks 可能过于乐观。\n\n建议补充：(1) 分析 item-level features（如 solution length, reasoning steps）与 residual magnitude 的相关性；(2) 至少讨论 residual 中 systematic vs. random 的 plausible 比例。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Data contamination 作为 model×item interaction 的混淆变量**\n\n同意。Model×item interaction 占 30-36% (Table 2-3) 是本文最重要的发现之一，但 data contamination 是一个合理的 alternative explanation：如果某些 models 在训练中见过特定 benchmark items，这些 items 上的表现会系统性偏高，产生 DIF-like patterns，但原因不是 genuine differential functioning 而是 memorization。论文 §2 (p3) 引用了 IRT 文献讨论 DIF，但完全未提及 contamination。即使无法直接测量 contamination，至少应在 §4.2 或 §5 中将其列为 model×item interaction 的 candidate explanation 之一，并引用 Golchin & Surdeanu (2023) 等 contamination detection 文献。\n\n---\n\n**[AGREE] R2-W2: Contribution 层级权重不均**\n\n部分同意。§1 (p1-2) 列出三个 contributions：C1 (design-dependent budgets), C2 (precision separability), C3 (toolkit)。C2 本质上是 \"BF16/FP16/FP32 差异 negligible\" 的 null result，将其与 C1 并列确实 overclaiming。但我认为 R2 对 null result 的价值判断略低——C2 对 practitioners 有直接影响（不需要 FP32 evaluation），只是不应与 C1 并列为同等 contribution。建议作者将 C2 降级为 C1 的 sub-finding，C3 (toolkit) 从 contribution list 移至 practical implications。\n\n---\n\n**[AGREE] R2-W3: ARC model×prompt 异常 (8.0%) 未讨论**\n\n同意。Table 3 (p7) 显示 ARC 的 model×prompt interaction 为 8.0%，远高于其他 MC benchmarks（MMLU model×prompt 在 Table 2 中未单独列出但 all main facet effects <1% except prompt 0.9%）。这一异常值得至少一句话的解释——是否与 ARC 的 prompt template 设计有关（如 ARC 的选项数量/格式与 MMLU 不同）？\n\n---\n\n**[AGREE] R2-W4: Conclusion 过于简短**\n\n同意。§5 Conclusion (p8) 仅约 5 句话，未讨论 practical implications 的细节（如哪些 benchmarks 最需要 multi-facet design？practitioner 应如何选择 prompt 数量？）。考虑到 8 页 limit，空间有限，但 Conclusion 可以适当扩展以加强 takeaway message。\n\n---\n\n**[AGREE] R2-W5: Cross-benchmark 比较受非对称设计限制**\n\n同意，这与我自己的 W2 一致。MC 和 FF 的 prompt manipulation 本质不同（MC: 选项顺序/选择指令; FF: 生成策略），ordering facet 仅 MC 有意义——这使得 Table 3 的 MC vs. FF 比较不是 pure format comparison 而是 format + prompt design + ordering 的 compound comparison。论文 §4.3 (p7) 的 \"Exploratory\" 标注是恰当的，但未充分讨论这些 confounds。\n\n---\n\n### Missing References 回应\n\n- **Data contamination references**: 同意应引用。Golchin & Surdeanu (2023) 和 Sainz et al. (2023) 直接相关。\n- **Kiela et al. (2021) DynaBench**: 同意。我在自己的 Missing References 中也提到了这篇，可加强 §6 temporal drift 讨论。\n\n---\n\n### 总结\n\nR2 的 N1 (cost framing) 和 N3 (residual analysis) 我完全同意，这些是论文需要 fix 的实质问题。N2 (relative to Messing) 我不同意——本文与 Messing 的关系是互补而非增量延伸，R2 低估了 infrastructure null results 和 cross-benchmark structural insights 的价值。W1-W5 我基本同意，这些问题可修复但需要在修订中逐一 address。",
    "reviewer_id": "1",
    "project": "nlp_variance_gtheory"
  }
}
```

</details>

---


### Tool result

_source line 547 · 2026-05-22T15:18:53.103418+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_265de443abfe4594f91451b075b582ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3615
}
```

</details>

---


### Assistant

_source line 548 · 2026-05-22T15:18:59.118575+00:00_

交叉回应已提交。

对 R2 的 7 条意见：**5 条 AGREE**（N1 cost framing、N3 残差分析、W1 contamination、W3 ARC 异常、W4 结论过短、W5 设计不对称），**1 条 REBUT**（N2 相对 Messing 的增量贡献——我认为本文与 Messing 是互补关系而非增量延伸），W2 部分同意（null result 有价值但不应与主贡献并列）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1"
}
```

</details>

---


## Round 17

## Round 17

46 recorded events


### User

_source line 549 · 2026-05-23T01:02:54.272276+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计**。

## 论文信息
- **标题**: Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models
- **论文路径**: projects/nlp_variance_gtheory/docs/paper/main.tex
- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/submitted.pdf

## 目标 Venue
- **EMNLP 2026**（通过 ARR 统一审稿）
- **截止日期**: 2026-05-25
- **格式**: ACL 模板，正文 ≤8 页，References 不限，Limitations 必需且不计页数
- **匿名**: Double-blind
- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

## 你的审查侧重

### 1. G-theory 方法论适用性
- Henderson Method I 应用于 binary (0/1) 数据的理论合理性——论文声称 robustness（§3.5），但 probit simulation ρ=0.732 仅中等相关，是否有 bias/RMSE 的完整报告？
- 方差分量估计的置信区间方法：bootstrap 仅 item-level resampling，是否充分捕获 model-level uncertainty？
- LOMO 和 Cohen's κ 是否充分支持 quasi-random model facet assumption（8 个 purposively selected models 作为 random facet）？

### 2. D-study Projection 有效性
- Forward prediction（Table 8）：4-model → 8-model，这是否 in-sample cross-validation（4 模型是 8 模型子集）而非真正 out-of-sample？
- Variance component invariance assumption 在 temporal drift 下是否成立？有无 empirical evidence？
- Scale validation（§4.6）仅限 Qwen2.5 单一架构家族，cross-family generalization 的证据？

### 3. 实验设计完整性
- Reduced crossing（exp-002）vs full crossing（exp-001）的 ΔG=0.0008——这个验证是否充分？
- FF benchmarks residual variance 39.9-43.9%——G-theory 模型解释力是否足够？是否分析了 item 特征与残差的关系？
- Binary scoring confound：partial-credit pilot 显示 G 从 0.76→0.55，ρ=0.26——所有发现的 metric-conditionality 是否充分讨论？
- Data contamination 作为 model×item interaction (30-36%) 的混淆变量是否充分讨论？

### 4. 统计检验与 Claims 匹配
- Format-associated pattern（§4.3）：n=5, p=0.10，标注 exploratory 是否充分？confounds（prompt semantics、ordering 非对称性）的讨论是否完整？
- '10× fewer items' 或类似 headline claim 与实际总评估量（items × conditions）的关系——是否有误导性？
- Contribution 层级：C2 (precision separability) 是 null result，与 C1 并列是否 overclaiming？

### 5. 格式合规
- 正文是否严格 ≤8 页？
- 匿名性：是否有 de-anonymizing 线索？
- Limitations section 是否存在且充分？

请按以下结构输出审稿报告：
1. **Summary**（2-3 句）
2. **Strengths**（逐条，标 [S1], [S2]...）
3. **Weaknesses**（逐条，标 [W1], [W2]...，每条标注 severity: Must-Fix / Should-Fix / Minor）
4. **Questions**（需作者澄清）
5. **Missing References**（如有）
6. **Overall Assessment**（评分 + 置信度 + 1 段总评）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 550 · 2026-05-23T01:03:04.071045+00:00_

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
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
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

_source line 551 · 2026-05-23T01:03:04.121726+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 552 · 2026-05-23T01:03:07.439316+00:00_

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
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria dimensions"
  }
}
```

</details>

---


### Tool call

_source line 553 · 2026-05-23T01:03:09.547951+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/submitted.pdf",
  "pages": "1-10",
  "project": "nlp_variance_gtheory",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/submitted.pdf",
    "pages": "1-10",
    "project": "nlp_variance_gtheory",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 554 · 2026-05-23T01:03:17.130666+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria dimensions"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines and review form criteria:

## Review Form Criteria and Dimensions

The main criteria for Findings papers are soundness and reproducibility, while conference recommendations may also consider novelty, impact and other factors.

## Review Scoring Scale

The review form uses the following scoring dimensions:

- 5 = Consider for Award: papers that could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers)
- 2 
…[truncated 823 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 9691
}
```

</details>

---


### Tool result

_source line 555 · 2026-05-23T01:03:18.643413+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 470.6}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 517.5}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 579.4}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 526.4}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 484.1}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 500.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 503.5}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 492.3}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 550.8}, {\"page\":
…[truncated 438 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 9095
}
```

</details>

---


### Tool call

_source line 556 · 2026-05-23T01:03:28.597493+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. I need every field that reviewers fill in, especially: Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, Confidence, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. I need every field that reviewers fill in, especially: Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, Confidence, and any other scored dimensions."
  }
}
```

</details>

---


### Tool call

_source line 557 · 2026-05-23T01:03:29.601935+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/submitted.pdf",
  "pages": "11-16",
  "project": "nlp_variance_gtheory",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/submitted.pdf",
    "pages": "11-16",
    "project": "nlp_variance_gtheory",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 558 · 2026-05-23T01:03:30.579044+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 559 · 2026-05-23T01:03:31.031270+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 560 · 2026-05-23T01:03:31.483719+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 561 · 2026-05-23T01:03:32.136776+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 562 · 2026-05-23T01:03:36.305914+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## Core Scoring Dimensions

**Reviewer Confidence** (1-5 scale)
- 5: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- 4: High confidence with unlikely oversights
- 3: Adequate understanding but possible gaps
- 2: May have missed details or novelty assessment
- 1: "Not my area, or paper is very hard to understand"

**Soundness** (1-5 scale with half-points)
- 5: Exceptionally thorough research
- 4: "This study provides sufficient support for all of its claims"
- 3: Adequate support for main claims with minor gaps
- 2: Main claims lack sufficient support; major technical problems
- 1: "Not yet sufficiently thorough to warrant publication"

**Excitement** (1-5 scale with half-points)
- 5: "Highly Exciting: I would recommend this paper to others"
- 4: Notable contribution meriting mention to colleagues
- 3: Interesting but not compelling
- 2: "Does not resonate with me, but it might with others"
- 1: "Not Exciting: this paper does not resonate with me"

**Overall Assessment** (1-5 scale with half-points)
- 5: "Consider for Award: top 2.5% papers"
- 4: Conference acceptance recommended
- 3: Findings track acceptance
- 2: Needs substantial revisions
- 1: "Do not resubmit: fully redone needed"

## Additional Scoring Dimensions

**Reproducibility** (1-5 scale)
- 5: Results easily reproducible
- 3: Possible but with difficulty; underspecified parameters
- 1: Not reproducible regardless of effort

**Datasets** (1-5 scale)
- 5: Enabling impact on future research
- 4: Useful for ongoing work
- 3: Potentially useful
- 2: Documentary value only
- 1: No usable datasets

**Software** (1-5 scale)
- 5: Enabling impact on future projects
- 4: Recommended for ongoing research
- 1: No usable software

**Author Identity Recognition** (1-5 scale)
- 5: Known from submission violations
- 1: No educated guess possible

## Narrative Sections

- Paper Summary
- Summary of Stre
…[truncated 239 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7708
}
```

</details>

---


### Tool result

_source line 563 · 2026-05-23T01:03:36.959627+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 585.6}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 498.8}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 467.3}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 427.5}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 390.8}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 31.0}], \"total_pages\": 16, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7357
}
```

</details>

---


### Tool result

_source line 564 · 2026-05-23T01:03:39.131808+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 6995
}
```

</details>

---


### Tool result

_source line 565 · 2026-05-23T01:03:39.132900+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 8553
}
```

</details>

---


### Tool result

_source line 566 · 2026-05-23T01:03:39.133928+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 7650
}
```

</details>

---


### Tool result

_source line 567 · 2026-05-23T01:03:39.135102+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 8103
}
```

</details>

---


### Tool call

_source line 568 · 2026-05-23T01:03:45.415549+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 569 · 2026-05-23T01:03:45.969342+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 570 · 2026-05-23T01:03:46.019993+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 571 · 2026-05-23T01:03:46.321305+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 572 · 2026-05-23T01:03:46.726786+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 573 · 2026-05-23T01:03:46.729374+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 709
}
```

</details>

---


### Tool result

_source line 574 · 2026-05-23T01:03:47.335418+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1014
}
```

</details>

---


### Tool result

_source line 575 · 2026-05-23T01:03:47.587464+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 860
}
```

</details>

---


### Tool call

_source line 576 · 2026-05-23T01:03:53.258599+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 577 · 2026-05-23T01:03:53.861602+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 578 · 2026-05-23T01:03:54.768243+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1509
}
```

</details>

---


### Tool call

_source line 579 · 2026-05-23T01:03:54.768676+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 580 · 2026-05-23T01:03:54.921583+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 581 · 2026-05-23T01:03:55.123456+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1261
}
```

</details>

---


### Tool result

_source line 582 · 2026-05-23T01:03:55.779304+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1010
}
```

</details>

---


### Tool result

_source line 583 · 2026-05-23T01:03:55.980840+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1059
}
```

</details>

---


### Tool call

_source line 584 · 2026-05-23T01:04:01.305070+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 585 · 2026-05-23T01:04:01.808284+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 586 · 2026-05-23T01:04:02.212006+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 587 · 2026-05-23T01:04:02.212522+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 588 · 2026-05-23T01:04:02.414839+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 606
}
```

</details>

---


### Tool result

_source line 589 · 2026-05-23T01:04:02.767511+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 554
}
```

</details>

---


### Tool call

_source line 590 · 2026-05-23T01:05:59.957751+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the key reviewer guidelines: what should reviewers focus on, how to assess soundness, what constitutes a good vs weak paper, any specific instructions about evaluating methodology, experiments, claims, and formatting."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the key reviewer guidelines: what should reviewers focus on, how to assess soundness, what constitutes a good vs weak paper, any specific instructions about evaluating methodology, experiments, claims, and formatting."
  }
}
```

</details>

---


### Tool result

_source line 591 · 2026-05-23T01:06:06.888534+00:00_

# ARR Reviewer Guidelines: Key Focus Areas

## Core Reviewing Tasks

Reviewers should complete four primary tasks:
1. Allocate calendar time for reviewing and discussion periods
2. Verify assignment appropriateness (expertise, conflicts of interest)
3. Write substantive reviews with clear justification
4. Update assessments after author responses and peer discussion

## Assessing Soundness

The guidelines emphasize that "soundness scores must be justified by the text of the review." Reviewers should evaluate:
- Technical correctness and validity of arguments
- Clarity of research questions and contributions
- Appropriate scope of claims relative to evidence presented
- Completeness of methodological assumptions and proofs

## Reading Strategy

Reviewers should read papers twice: first, skimming to understand the research question without looking at results (avoiding hindsight bias), then conducting in-depth evaluation of evidence and methodology.

## Common Review Pitfalls to Avoid

The guidelines flag 17 problematic heuristics, including:
- Dismissing work as "unsurprising" when findings haven't been previously empirically tested
- Requiring SOTA results when papers claim other contributions (efficiency, interpretability, fairness)
- Rejecting negative results or simple solutions unnecessarily
- Requesting experiments unrelated to the paper's actual claims

## Writing Quality Standards

Reviews must be "professional and neutral," avoiding sarcasm or dismissiveness. Specificity is essential—vague criticisms like "X is unclear" should instead identify "Y and Z are missing from X's description."

## NLP-Specific Issues

Watch for methodological problems including LLM-only evaluation without validation, reproducibility gaps, undisclosed data quality issues, and overclaimed findings unsupported by limited evaluation scope.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6930
}
```

</details>

---


### Tool call

_source line 592 · 2026-05-23T01:10:42.962638+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿报告（方法严谨性 + 实验设计）\n\n### 1. Summary\n\n本文将 Generalizability Theory (G-theory) 应用于 LLM 评估，通过完全交叉因子设计（8 个 7–9B 指令微调模型 × 5 个 benchmark × 7 个 facets）对约 230 万条二元评分记录进行方差分解，量化 item selection、model×item interaction、prompt template 等方差来源的相对贡献，并通过 D-study 推导出可操作的 reproducibility budgets。核心发现：item selection 主导方差（~38%），推荐的 3-prompt × 3-seed 设计可在 178 items 下达到 G ≥ 0.80。\n\n### 2. Strengths\n\n**[S1]** 首次在 LLM 评估中同时交叉 infrastructure（precision、temperature、ordering）和 methodology（prompt、seed）facets 进行 G-theory 分析，填补了现有文献仅处理单一维度方差的空白（§1, §2）。\n\n**[S2]** 实验规模大且设计严谨：exp-001 完全交叉设计覆盖 460,800 条记录（Table 1），exp-002 扩展至 5 个 benchmark 的 2,304,000 条记录。完整 factorial 设计使方差分量可无混淆地估计。\n\n**[S3]** 实用价值突出：D-study reproducibility budget（Table 4, Figure 1）为 benchmark 设计者和评估实践者提供了可直接使用的 item 数量指南，承诺开源 G-theory pipeline 和 D-study calculator。\n\n**[S4]** Appendix A 的 robustness 分析极为全面：GLMM complement（ρ=1.0 rank preservation）、accuracy-range stability、REML（CV < 3.1%）、null calibration（observed/null = 1.0008）、facet sensitivity、LOMO stability（40 subsets，Table 5）——远超大多数投稿的 sensitivity 分析深度。\n\n**[S5]** Item difficulty heterogeneity 分析（§4.3, Appendix D-F）揭示了 MC vs FF benchmark 的方差结构差异（item-dominated vs distributed），为 benchmark 设计提供了有意义的 typology。\n\n### 3. Weaknesses\n\n**[W1] [Should-Fix] Henderson Method I 在 binary 数据上的适用性论证不充分**\n- 具体位置：§3.5, Appendix A\n- 问题：Henderson Method I 假设连续正态数据。论文的 probit simulation 报告 Spearman ρ = 0.732，仅为中等相关，但论文定性为 \"robustness\"。Bias 报告仅限于特定 difficulty stratum（|bias| = 0.28–0.37 for p ∈ [0.5, 0.8]），缺少对极端 difficulty items 的 bias/RMSE 完整报告。GLMM complement 显示 rank preservation ρ = 1.0，但 rank correlation ≠ magnitude agreement——若 variance components 绝对值存在系统性偏移，D-study budget 的具体数字可能偏离。\n- 建议：补充 probit simulation 的完整 bias/RMSE 分解（按 difficulty quintile），明确 D-study budget 在 GLMM 框架下的对应数值。\n\n**[W2] [Should-Fix] Forward prediction（Table 8）为 in-sample 验证，非 out-of-sample**\n- 具体位置：§4.5, Table 8\n- 问题：4-model subset（DeepSeek, Llama, Mistral, Qwen3）是 8-model 全集的子集。从子集估计方差分量后预测全集 G 系数，本质上是 in-sample cross-validation。Error 范围 0.96–6.88% 看似不大，但 in-sample 设计 inherently 低估 prediction error。LOMO 是 leave-one-model-out（7→8），同样非 truly held-out families。\n- 建议：明确标注为 in-sample consistency check；更理想的做法是用 non-overlapping model pairs 做 split-half cross-validation。\n\n**[W3] [Should-Fix] Scale validation 局限于 Qwen2.5 单一架构家族**\n- 具体位置：§4.6\n- 问题：Within-family validation（Qwen2.5 3B/7B/72B）显示 variance structure 在 scale 上稳定，但同一家族共享 training recipe 和 tokenizer，item difficulty profile 可能高度相关。论文 claim \"preliminary evidence that budgets generalize beyond the 7–9B range\" 缺乏 cross-family 支撑。\n- 建议：明确 \"within-family only\" 限制；如有数据补充 Llama-3.1 8B→70B 验证。\n\n**[W4] [Should-Fix] Partial-credit scoring sensitivity 对发现影响讨论不足**\n- 具体位置：§4.4, §5\n- 问题：Binary → partial-credit 导致 G 从 0.76→0.55，ρ = 0.26。所有 D-study budgets、format-associated patterns 都 conditioned on binary scoring，但 Conclusion 仅一句带过。当前许多重要 benchmark 使用 non-binary scoring（GSM8K 部分评分、LLM-as-judge）。\n- 建议：在 Conclusion/Limitations 中明确所有 budgets 仅对 binary correctness scoring 有效。\n\n**[W5] [Should-Fix] Data contamination 作为 model×item interaction（30–36%）的混淆变量讨论不足**\n- 具体位置：§6\n- 问题：Model×item interaction 是第二大方差来源（up to 36%），但 data contamination 可能 inflate 该分量。论文仅提供间接证据（\"三个独立 MC benchmarks\"），未做 contamination detection。\n- 建议：讨论 contamination 如何影响 variance decomposition；引用相关检测方法并解释为何未采用。\n\n**[W6] [Minor] Format-associated pattern（§4.3）n=5, p=0.10，exploratory 但叙事权重过大**\n- 问题：MC vs FF 对比基于 n=5，permutation p=0.10，但占约大半页篇幅且被提升为 C1 核心组成。混淆变量（prompt semantics、scoring 方式差异）讨论不完整。\n- 建议：缩短 §4.3 或降级为 preliminary observation。\n\n**[W7] [Minor] C2（precision separability）本质为 null result，与 C1 并列有 overclaiming 之嫌**\n- 问题：BF16/FP16 interchangeable（< 0.1% interaction）不令人惊讶，列为 main contribution 权重过高。\n- 建议：降级为 additional finding 或合并入 C1。\n\n**[W8] [Minor] Bootstrap CI 仅 item-level resampling，model-facet uncertainty 可能被低估**\n- 问题：Model facet 仅 8 levels + purposively selected。Item-level bootstrap 不能捕获 \"换一组 models\" 的 uncertainty。\n- 建议：明确 CI 仅反映 item-sampling variability。\n\n**[W9] [Minor] \"3.1× item reduction\" framing 未凸显总评估量从 552 增至 1,602（增加 2.9×）**\n- 建议：在 Abstract 中平衡呈现 item reduction 和 total evaluation increase。\n\n### 4. Questions for Authors\n\n**Q1.** Table 8 的 4 models 是 8 models 子集。是否有能力做 truly held-out 验证——例如用 exp-001 方差分量预测 exp-002 中某个全新 benchmark 的 G 系数？\n\n**Q2.** Probit simulation ρ = 0.732：能否报告 variance components 的 MAPE 而非仅 rank correlation？对 D-study budget，magnitude accuracy 比 rank preservation 更关键。\n\n**Q3.** Partial-credit G = 0.55, ρ = 0.26 是基于 GSM8K 单一 benchmark 吗？是否有其他 benchmark 上的验证？\n\n**Q4.** LOMO Table 5 中 MATH 的 CV = 0.919——请澄清此为何种 quantity 的 coefficient of variation？若 CV 接近 1.0 是否反映 model facet 在该 benchmark 上高度不稳定？\n\n**Q5.** FF benchmarks 残差 39.9–43.9%。是否考虑过 3-parameter IRT 的 guessing parameter 对 MC benchmarks 残差的解释？\n\n### 5. Missing References\n\n- Oren et al. (2024) \"Proving Test Set Contamination in Black Box Language Models\" — 可讨论 contamination 对 item-level variance 的影响\n- Brennan (2001, Ch. 12) 对 dichotomous data 的 G-theory 处理建议更显式地讨论\n\n### 6. Overall Assessment\n\n**Overall: 3.5 — Borderline Conference**\n**Confidence: 4/5**\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心方法论应用得当，但 binary data 适用性论证依赖 ρ=0.732 中等相关；forward prediction 为 in-sample；scale validation 限于单一 family |\n| Excitement | 3.5/5 | G-theory 在 LLM 评估中的首次系统应用，有实际价值；但 scope 限于 7–9B / binary scoring |\n| Reproducibility | 4.0/5 | 实验设计细节充分，承诺开源；prompt template 和 hyperparameters 记录完整 |\n| Datasets | 3.0/5 | 使用现有公开 benchmark，未引入新数据集 |\n\n**总评：** 本文提出了有价值的方法论贡献——将 G-theory 系统引入 LLM 评估。但存在几个 concerns：(1) Henderson Method I 对 binary 数据的适用性需更完整的 bias/RMSE 报告；(2) forward prediction 的 in-sample 性质需明确标注；(3) partial-credit scoring 导致 G 大幅下降意味着 budget 推荐适用范围比 framing 更窄；(4) data contamination 作为 model×item interaction 混淆变量需更深入讨论。这些均非 fatal flaws，但累积起来使核心 claims 需更多 qualification。当前推荐 Borderline Conference / strong Findings。",
  "reviewer_id": "1",
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿报告（方法严谨性 + 实验设计）\n\n### 1. Summary\n\n本文将 Generalizability Theory (G-theory) 应用于 LLM 评估，通过完全交叉因子设计（8 个 7–9B 指令微调模型 × 5 个 benchmark × 7 个 facets）对约 230 万条二元评分记录进行方差分解，量化 item selection、model×item interaction、prompt template 等方差来源的相对贡献，并通过 D-study 推导出可操作的 reproducibility budgets。核心发现：item selection 主导方差（~38%），推荐的 3-prompt × 3-seed 设计可在 178 items 下达到 G ≥ 0.80。\n\n### 2. Strengths\n\n**[S1]** 首次在 LLM 评估中同时交叉 infrastructure（precision、temperature、ordering）和 methodology（prompt、seed）facets 进行 G-theory 分析，填补了现有文献仅处理单一维度方差的空白（§1, §2）。\n\n**[S2]** 实验规模大且设计严谨：exp-001 完全交叉设计覆盖 460,800 条记录（Table 1），exp-002 扩展至 5 个 benchmark 的 2,304,000 条记录。完整 factorial 设计使方差分量可无混淆地估计。\n\n**[S3]** 实用价值突出：D-study reproducibility budget（Table 4, Figure 1）为 benchmark 设计者和评估实践者提供了可直接使用的 item 数量指南，承诺开源 G-theory pipeline 和 D-study calculator。\n\n**[S4]** Appendix A 的 robustness 分析极为全面：GLMM complement（ρ=1.0 rank preservation）、accuracy-range stability、REML（CV < 3.1%）、null calibration（observed/null = 1.0008）、facet sensitivity、LOMO stability（40 subsets，Table 5）——远超大多数投稿的 sensitivity 分析深度。\n\n**[S5]** Item difficulty heterogeneity 分析（§4.3, Appendix D-F）揭示了 MC vs FF benchmark 的方差结构差异（item-dominated vs distributed），为 benchmark 设计提供了有意义的 typology。\n\n### 3. Weaknesses\n\n**[W1] [Should-Fix] Henderson Method I 在 binary 数据上的适用性论证不充分**\n- 具体位置：§3.5, Appendix A\n- 问题：Henderson Method I 假设连续正态数据。论文的 probit simulation 报告 Spearman ρ = 0.732，仅为中等相关，但论文定性为 \"robustness\"。Bias 报告仅限于特定 difficulty stratum（|bias| = 0.28–0.37 for p ∈ [0.5, 0.8]），缺少对极端 difficulty items 的 bias/RMSE 完整报告。GLMM complement 显示 rank preservation ρ = 1.0，但 rank correlation ≠ magnitude agreement——若 variance components 绝对值存在系统性偏移，D-study budget 的具体数字可能偏离。\n- 建议：补充 probit simulation 的完整 bias/RMSE 分解（按 difficulty quintile），明确 D-study budget 在 GLMM 框架下的对应数值。\n\n**[W2] [Should-Fix] Forward prediction（Table 8）为 in-sample 验证，非 out-of-sample**\n- 具体位置：§4.5, Table 8\n- 问题：4-model subset（DeepSeek, Llama, Mistral, Qwen3）是 8-model 全集的子集。从子集估计方差分量后预测全集 G 系数，本质上是 in-sample cross-validation。Error 范围 0.96–6.88% 看似不大，但 in-sample 设计 inherently 低估 prediction error。LOMO 是 leave-one-model-out（7→8），同样非 truly held-out families。\n- 建议：明确标注为 in-sample consistency check；更理想的做法是用 non-overlapping model pairs 做 split-half cross-validation。\n\n**[W3] [Should-Fix] Scale validation 局限于 Qwen2.5 单一架构家族**\n- 具体位置：§4.6\n- 问题：Within-family validation（Qwen2.5 3B/7B/72B）显示 variance structure 在 scale 上稳定，但同一家族共享 training recipe 和 tokenizer，item difficulty profile 可能高度相关。论文 claim \"preliminary evidence that budgets generalize beyond the 7–9B range\" 缺乏 cross-family 支撑。\n- 建议：明确 \"within-family only\" 限制；如有数据补充 Llama-3.1 8B→70B 验证。\n\n**[W4] [Should-Fix] Partial-credit scoring sensitivity 对发现影响讨论不足**\n- 具体位置：§4.4, §5\n- 问题：Binary → partial-credit 导致 G 从 0.76→0.55，ρ = 0.26。所有 D-study budgets、format-associated patterns 都 conditioned on binary scoring，但 Conclusion 仅一句带过。当前许多重要 benchmark 使用 non-binary scoring（GSM8K 部分评分、LLM-as-judge）。\n- 建议：在 Conclusion/Limitations 中明确所有 budgets 仅对 binary correctness scoring 有效。\n\n**[W5] [Should-Fix] Data contamination 作为 model×item interaction（30–36%）的混淆变量讨论不足**\n- 具体位置：§6\n- 问题：Model×item interaction 是第二大方差来源（up to 36%），但 data contamination 可能 inflate 该分量。论文仅提供间接证据（\"三个独立 MC benchmarks\"），未做 contamination detection。\n- 建议：讨论 contamination 如何影响 variance decomposition；引用相关检测方法并解释为何未采用。\n\n**[W6] [Minor] Format-associated pattern（§4.3）n=5, p=0.10，exploratory 但叙事权重过大**\n- 问题：MC vs FF 对比基于 n=5，permutation p=0.10，但占约大半页篇幅且被提升为 C1 核心组成。混淆变量（prompt semantics、scoring 方式差异）讨论不完整。\n- 建议：缩短 §4.3 或降级为 preliminary observation。\n\n**[W7] [Minor] C2（precision separability）本质为 null result，与 C1 并列有 overclaiming 之嫌**\n- 问题：BF16/FP16 interchangeable（< 0.1% interaction）不令人惊讶，列为 main contribution 权重过高。\n- 建议：降级为 additional finding 或合并入 C1。\n\n**[W8] [Minor] Bootstrap CI 仅 item-level resampling，model-facet uncertainty 可能被低估**\n- 问题：Model facet 仅 8 levels + purposively selected。Item-level bootstrap 不能捕获 \"换一组 models\" 的 uncertainty。\n- 建议：明确 CI 仅反映 item-sampling variability。\n\n**[W9] [Minor] \"3.1× item reduction\" framing 未凸显总评估量从 552 增至 1,602（增加 2.9×）**\n- 建议：在 Abstract 中平衡呈现 item reduction 和 total evaluation increase。\n\n### 4. Questions for Authors\n\n**Q1.** Table 8 的 4 models 是 8 models 子集。是否有能力做 truly held-out 验证——例如用 exp-001 方差分量预测 exp-002 中某个全新 benchmark 的 G 系数？\n\n**Q2.** Probit simulation ρ = 0.732：能否报告 variance components 的 MAPE 而非仅 rank correlation？对 D-study budget，magnitude accuracy 比 rank preservation 更关键。\n\n**Q3.** Partial-credit G = 0.55, ρ = 0.26 是基于 GSM8K 单一 benchmark 吗？是否有其他 benchmark 上的验证？\n\n**Q4.** LOMO Table 5 中 MATH 的 CV = 0.919——请澄清此为何种 quantity 的 coefficient of variation？若 CV 接近 1.0 是否反映 model facet 在该 benchmark 上高度不稳定？\n\n**Q5.** FF benchmarks 残差 39.9–43.9%。是否考虑过 3-parameter IRT 的 guessing parameter 对 MC benchmarks 残差的解释？\n\n### 5. Missing References\n\n- Oren et al. (2024) \"Proving Test Set Contamination in Black Box Language Models\" — 可讨论 contamination 对 item-level variance 的影响\n- Brennan (2001, Ch. 12) 对 dichotomous data 的 G-theory 处理建议更显式地讨论\n\n### 6. Overall Assessment\n\n**Overall: 3.5 — Borderline Conference**\n**Confidence: 4/5**\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心方法论应用得当，但 binary data 适用性论证依赖 ρ=0.732 中等相关；forward prediction 为 in-sample；scale validation 限于单一 family |\n| Excitement | 3.5/5 | G-theory 在 LLM 评估中的首次系统应用，有实际价值；但 scope 限于 7–9B / binary scoring |\n| Reproducibility | 4.0/5 | 实验设计细节充分，承诺开源；prompt template 和 hyperparameters 记录完整 |\n| Datasets | 3.0/5 | 使用现有公开 benchmark，未引入新数据集 |\n\n**总评：** 本文提出了有价值的方法论贡献——将 G-theory 系统引入 LLM 评估。但存在几个 concerns：(1) Henderson Method I 对 binary 数据的适用性需更完整的 bias/RMSE 报告；(2) forward prediction 的 in-sample 性质需明确标注；(3) partial-credit scoring 导致 G 大幅下降意味着 budget 推荐适用范围比 framing 更窄；(4) data contamination 作为 model×item interaction 混淆变量需更深入讨论。这些均非 fatal flaws，但累积起来使核心 claims 需更多 qualification。当前推荐 Borderline Conference / strong Findings。",
    "reviewer_id": "1",
    "project": "nlp_variance_gtheory"
  }
}
```

</details>

---


### Tool result

_source line 593 · 2026-05-23T01:10:46.524059+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_265de443abfe4594f91451b075b582ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3561
}
```

</details>

---


### Assistant

_source line 594 · 2026-05-23T01:10:54.104578+00:00_

审稿报告已提交给 Review Director。

**评分摘要：**
- **Overall: 3.5（Borderline Conference）**，Confidence 4/5
- Soundness 3.5, Excitement 3.5, Reproducibility 4.0

**核心判断：** 方法论贡献有价值（G-theory 首次系统应用于 LLM 评估），实验规模大且 robustness 分析全面。但 5 个 Should-Fix 问题（binary data 适用性论证不充分、forward prediction in-sample、scale validation 限于单一家族、partial-credit sensitivity 讨论不足、data contamination 混淆未解决）累积起来使核心 claims 需要更多 qualification。当前推荐 Borderline Conference / strong Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1"
}
```

</details>

---


## Round 18

## Round 18

4 recorded events


### User

_source line 595 · 2026-05-23T01:14:27.997553+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 2 的完整审稿意见

请逐条回应 Reviewer 2 的每个 Weakness 和 Question：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

以下是 Reviewer 2 的完整审稿意见：

### Strengths

**[S1] 严谨的实验设计与验证闭环**
exp-001 的全交叉因子设计（7 facets, 460,800 records）和 exp-002 的系统性 reduced crossing（5 benchmarks, 2,304,000 records）设计合理。关键的是，作者验证了 reduced crossing 保留了方差结构（ΔG = 0.0008, Appendix A），而非简单假设。

**[S2] 示范级的 robustness analyses**
Appendix A 覆盖了几乎所有可预见的方法论质疑：GLMM 补充分析、accuracy-range stability、Henderson Method I vs. REML 对比、probit simulation（259,200 条件下 binary/continuous rankings τ = 0.81）、null calibration（100 replications, observed-to-null ratio = 1.0008）、facet specification sensitivity、reduced crossing validation、以及 LOMO leave-one-model-out stability。

**[S3] D-study 预算的实用价值**
Table 4 和 Table 7 提供了可直接操作的评估设计指南，区分了 item-minimizing（multi-facet）和 evaluation-minimizing（single-condition）两种策略。Figure 1 的 D-study 曲线直观展示了 G coefficient 随 item 数量和条件数的变化。

**[S4] Related work positioning 清晰**
论文准确定位了与 Messing (2026) 的三个差异化方向，并系统覆盖了 IRT、方差分解和 psychometrics 经典文献。

**[S5] Limitations section 诚实且全面**
Section 6 主动覆盖了 temporal correlation、model exchangeability、binary scoring constraint、benchmark sample size (n=5)、few-shot ordering vs. identity、cross-validation 限制（仅 MMLU）、以及 contamination 对预算估计的影响。

### Weaknesses

**[W1] Must-Fix: "3.1× item reduction" 标题 framing 具有误导性**
- 论文以 "3.1× item reduction"（552 → 178 items）作为核心 headline，但推荐的 3-prompt × 3-seed 设计实际需要 178 × 9 = 1,602 次评估/模型，而 baseline 单条件设计仅需 552 次评估。**总计算成本增加了约 2.9×**（1,602/552）。对于一篇关于评估 *budget* 的论文，将 item count 下降包装为 "reduction" 而淡化总评估量上升，存在系统性误导。Section 5 的确承认了这一 tradeoff，但这一关键区分被埋在结论段中，Abstract 和 Introduction 完全未提及。
- 建议：在 Abstract 和 Introduction 中明确呈现 tradeoff。

**[W2] Should-Fix: C2（precision separability）作为独立 contribution 过于单薄**
- C2 的核心发现——BF16/FP16 在 binary scoring 下功能上不可区分（<0.1% interaction）——本质上是 binary scoring 信息损失的直接推论。将此包装为独立 contribution 夸大了工作的贡献范围。
- 建议：将 C2 降级为 C1 方差分解结果的一个子发现。

**[W3] Should-Fix: Format-associated variance patterns 统计效力不足且呈现方式过于积极**
- MC vs. FF 方差模式对比基于 n = 5 benchmarks（3 MC, 2 FF），Spearman ρ = 0.82 (p = 0.089, n = 5) 在任何传统阈值下都不显著。论文另报 cross-benchmark Spearman ρ = 0.90 (p = 0.006, n = 10)，但这是 within-MMLU 10 subjects 的结果，不是独立的 cross-benchmark 证据，两者被混淆呈现。
- 建议：明确分离两种证据；承认 n = 5 无统计效力。

**[W4] Should-Fix: 相对于 Messing (2026) 的增量贡献边界性**
- 三个扩展方向逐一审视——(i) facet 替换而非方法论创新；(ii) 跨 benchmark 增加 scope 但核心发现一致；(iii) D-study 是教科书内容非方法论贡献。三者叠加的增量价值是否足够 EMNLP main conference 是核心问题。
- excitement 维度低：属于 competent application 而非 methodological advance。

**[W5] Should-Fix: Abstract 数字密度过高，核心 message 被淹没**
- Abstract 包含至少 20 个具体数值，读者难以提取核心 message。
- 建议：保留 3–4 个最关键数字。

**[W6] Minor: Conclusion (Section 5) 对实用影响讨论不足**
- 未讨论：现有 benchmark 套件是否应据此重组、benchmark 开发者 vs. 使用者应如何分别应用预算、对 leaderboard 运营的具体建议。

**[W7] Minor: Model main effect 仅 2.8%（Table 2）引发 generalizability 疑问**
- 8 个模型的 model main effect 仅 2.8%，意味着模型在整体准确率上几乎不可区分。模型样本可能过于同质。D-study budgets 是否泛化到更多样的模型组合是未解答的关键问题。

**[W8] Minor: Anonymous arXiv 自引可能破坏匿名性**
- "Anonymous. 2025. Variance-aware LLM annotation. arXiv preprint arXiv:2601.02310." — reviewer 可通过 arXiv URL 查找作者身份。

### Questions

**Q1.** Table 4 显示 multi-facet 3×3 设计需 1,602 evaluations，单条件设计仅需 552。能否提供具体的 GPU-hours 或 API 成本对比？

**Q2.** Model main effect 仅 2.8%。D-study budgets 是否泛化到比较更多样模型集合的场景？

**Q3.** 鉴于 partial credit "fundamentally reshapes variance structure"，这些基于 binary scoring 的 budgets 对非 binary 场景的参考价值如何？

**Q4.** MC vs. FF 方差模式是否可能反映 benchmark 构建差异而非格式本身？是否考虑过控制 item difficulty 后的残差分析？

**Q5.** Anonymous arXiv 自引是否为作者自己的工作？

### Missing References

- Saxon et al. (2024) "Benchmarks as Microscopes: A Call for Model Metrology" (COLM 2024)
- Alzahrani et al. (2024) "When Benchmarks are Targets" (ACL 2024)

### Overall Assessment
**Overall: 3.5 — Borderline Conference**, Confidence: 4/5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 596 · 2026-05-23T01:16:38.969106+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n### Weaknesses 逐条回应\n\n**[AGREE] R2-W1: \"3.1× item reduction\" framing 误导性**\n同意核心观点，但对 severity 有分歧。Abstract 实际包含两个数字：\"178 items (1,602 total evaluations per model)\" 和 \"552 items, 552 evaluations\"——信息 present 但 emphasis 不平衡。我列为 Minor（W9），R2 列 Must-Fix，我认为 **Should-Fix** 更合适——framing 需 rebalance 但非 factually misleading。\n\n**[AGREE] R2-W2: C2 独立 contribution 过于单薄**\n完全同意。与我的 W7 一致。BF16/FP16 在 binary scoring 下不可区分是 binary 信息损失的直接推论。\n\n**[AGREE] R2-W3: Format-associated patterns 统计效力不足**\n同意，且 R2 指出了一个我未充分展开的关键问题：cross-benchmark ρ = 0.82 (n=5, p=0.089) 与 within-MMLU ρ = 0.90 (p=0.006, n=10) 被混淆呈现，后者不构成独立的 cross-benchmark 证据。\n\n**[REBUT] R2-W4: 相对于 Messing (2026) 增量贡献边界性**\nR2 将 coherent contribution 拆解为三个 sub-claims 逐一 devalue，过于 reductionist。具体反驳：\n(i) 同时交叉 infrastructure + methodology facets 使二者 interaction 首次可估计（如 precision×temperature = 1.3%），是 design-level 创新非简单替换；\n(ii) 跨 benchmark 结果揭示了 heterogeneity（MC item-dominated vs FF distributed），非 \"核心发现一致\"；\n(iii) D-study 方法是教科书内容，但 D-study 结果（具体 budget 数字、format-conditional patterns）是实证贡献。\n定性为 \"competent application 而非 methodological advance\" 过于苛刻。\n\n**[AGREE] R2-W5: Abstract 数字密度过高**\n同意。20+ 个数值影响可读性。\n\n**[AGREE] R2-W6: Conclusion 实用影响讨论不足**\n同意但 priority 较低，受 8 页限制。\n\n**[REBUT] R2-W7: Model main effect 2.8% 引发 generalizability 疑问**\nR2 误读了 G-theory。Model main effect 小意味着整体准确率相近（7-9B 同量级 expected），不等于模型 \"不可区分\"。Model×item interaction（30-36%）才是 ranking 信息来源。D-study 估计 ranking reliability 而非 absolute differentiation——即使 model main effect = 0%，只要 model×item interaction 足够大，G 仍可很高。正确的泛化性质疑应关注 model×item interaction 在更多样模型下是否稳定，而非 model main effect 大小。\n\n**[AGREE] R2-W8: Anonymous arXiv 自引破坏匿名性**\n同意。arXiv:2601.02310 提供可追溯 URL，违反 double-blind。\n\n### Questions 回应\nQ1-Q5 全部 AGREE，与我的审稿观点一致。\n\n### 综合判断\nR2 的 9 个 Weaknesses 中 AGREE 7 条，REBUT 2 条（W4 增量贡献、W7 model main effect 解读）。两位 reviewer 在 item budget framing、C2 降级、format pattern 效力、binary conditionality、匿名性问题上高度一致。主要分歧在 R2-W4 的增量贡献判断——我认为本文作为 G-theory 在 LLM 评估中的首次系统应用，整体贡献超越三个子 claims 的加法。\n\n维持 **Overall 3.5 (Borderline Conference)** 不变。",
  "reviewer_id": "1",
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n### Weaknesses 逐条回应\n\n**[AGREE] R2-W1: \"3.1× item reduction\" framing 误导性**\n同意核心观点，但对 severity 有分歧。Abstract 实际包含两个数字：\"178 items (1,602 total evaluations per model)\" 和 \"552 items, 552 evaluations\"——信息 present 但 emphasis 不平衡。我列为 Minor（W9），R2 列 Must-Fix，我认为 **Should-Fix** 更合适——framing 需 rebalance 但非 factually misleading。\n\n**[AGREE] R2-W2: C2 独立 contribution 过于单薄**\n完全同意。与我的 W7 一致。BF16/FP16 在 binary scoring 下不可区分是 binary 信息损失的直接推论。\n\n**[AGREE] R2-W3: Format-associated patterns 统计效力不足**\n同意，且 R2 指出了一个我未充分展开的关键问题：cross-benchmark ρ = 0.82 (n=5, p=0.089) 与 within-MMLU ρ = 0.90 (p=0.006, n=10) 被混淆呈现，后者不构成独立的 cross-benchmark 证据。\n\n**[REBUT] R2-W4: 相对于 Messing (2026) 增量贡献边界性**\nR2 将 coherent contribution 拆解为三个 sub-claims 逐一 devalue，过于 reductionist。具体反驳：\n(i) 同时交叉 infrastructure + methodology facets 使二者 interaction 首次可估计（如 precision×temperature = 1.3%），是 design-level 创新非简单替换；\n(ii) 跨 benchmark 结果揭示了 heterogeneity（MC item-dominated vs FF distributed），非 \"核心发现一致\"；\n(iii) D-study 方法是教科书内容，但 D-study 结果（具体 budget 数字、format-conditional patterns）是实证贡献。\n定性为 \"competent application 而非 methodological advance\" 过于苛刻。\n\n**[AGREE] R2-W5: Abstract 数字密度过高**\n同意。20+ 个数值影响可读性。\n\n**[AGREE] R2-W6: Conclusion 实用影响讨论不足**\n同意但 priority 较低，受 8 页限制。\n\n**[REBUT] R2-W7: Model main effect 2.8% 引发 generalizability 疑问**\nR2 误读了 G-theory。Model main effect 小意味着整体准确率相近（7-9B 同量级 expected），不等于模型 \"不可区分\"。Model×item interaction（30-36%）才是 ranking 信息来源。D-study 估计 ranking reliability 而非 absolute differentiation——即使 model main effect = 0%，只要 model×item interaction 足够大，G 仍可很高。正确的泛化性质疑应关注 model×item interaction 在更多样模型下是否稳定，而非 model main effect 大小。\n\n**[AGREE] R2-W8: Anonymous arXiv 自引破坏匿名性**\n同意。arXiv:2601.02310 提供可追溯 URL，违反 double-blind。\n\n### Questions 回应\nQ1-Q5 全部 AGREE，与我的审稿观点一致。\n\n### 综合判断\nR2 的 9 个 Weaknesses 中 AGREE 7 条，REBUT 2 条（W4 增量贡献、W7 model main effect 解读）。两位 reviewer 在 item budget framing、C2 降级、format pattern 效力、binary conditionality、匿名性问题上高度一致。主要分歧在 R2-W4 的增量贡献判断——我认为本文作为 G-theory 在 LLM 评估中的首次系统应用，整体贡献超越三个子 claims 的加法。\n\n维持 **Overall 3.5 (Borderline Conference)** 不变。",
    "reviewer_id": "1",
    "project": "nlp_variance_gtheory"
  }
}
```

</details>

---


### Tool result

_source line 597 · 2026-05-23T01:16:42.483084+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_265de443abfe4594f91451b075b582ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3513
}
```

</details>

---


### Assistant

_source line 598 · 2026-05-23T01:16:46.888636+00:00_

交叉回应已提交给 Review Director。

总结：对 R2 的 9 个 Weaknesses，AGREE 7 条，REBUT 2 条（W4 增量贡献判断和 W7 model main effect 解读）。两位 reviewer 在核心方法论问题上高度一致，主要分歧在于对 Messing (2026) 增量贡献的评价。维持 Overall 3.5 不变。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1"
}
```

</details>

---


## Round 19

## Round 19

64 recorded events


### User

_source line 599 · 2026-05-23T02:29:21.205670+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责 **方法严谨性** 审查。

## 论文信息
- **标题**: Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models
- **Venue**: EMNLP 2026 (via ARR)
- **截止日期**: 2026-05-25
- **格式**: ACL 模板，long paper，正文 8 页限制，参考文献不限，double-blind
- **论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex
- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/submitted.pdf

## 你的审查侧重

重点审查以下方面：

1. **G-theory 方法论正确性**：Henderson Method I 在 binary data 上的适用性；variance component 估计是否准确；G 系数和 D-study projection 的公式和推导是否正确
2. **实验设计**：fully crossed factorial design 的合理性和完整性；facet 选择和 level 设置是否充分；reduced crossing (exp-002) 是否引入 confounding
3. **统计推断**：bootstrap CI 的构建方法；probit simulation 和 GLMM complement 的 validation 充分性；LOMO 和 inter-model agreement 分析
4. **D-study Projection 假设**：variance component invariance 假设是否成立；forward prediction 的 in-sample vs out-of-sample 性质；scale validation 的局限性
5. **Binary scoring 限制**：binary data 对 G-theory 的影响；partial-credit pilot 的 implications；text-exact-match 对比的解释
6. **模型 facet 处理**：8 个 purposively selected 模型作为 quasi-random facet 的合理性；model exchangeability 论证；target universe 定义
7. **格式合规**：8 页限制、匿名性、引用格式

请给出完整的 Strengths、Weaknesses (Must-Fix / Should-Fix / Minor)、Questions，以及 Overall Assessment 评分（按 EMNLP 2026 ARR 标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 600 · 2026-05-23T02:29:30.344554+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 601 · 2026-05-23T02:29:31.799560+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1455
}
```

</details>

---


### Tool call

_source line 602 · 2026-05-23T02:29:31.950643+00:00_

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
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
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

_source line 603 · 2026-05-23T02:29:31.951092+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 604 · 2026-05-23T02:29:36.818705+00:00_

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
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 605 · 2026-05-23T02:29:38.936591+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/submitted.pdf",
  "project": "nlp_variance_gtheory",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/submitted.pdf",
    "project": "nlp_variance_gtheory",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 606 · 2026-05-23T02:29:45.169170+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's what I found about ACL ARR 2026 reviewer guidelines and review form criteria:

## Review Form Criteria

For main papers versus Findings papers, the main criteria for Findings are soundness and reproducibility, while conference recommendations may also consider novelty,
…[truncated 1311 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8350
}
```

</details>

---


### Tool result

_source line 607 · 2026-05-23T02:29:46.525191+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 467.2}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 505.0}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 576.8}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 538.9}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 488.7}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 496.3}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 502.4}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 501.7}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 561.3}, {\"page\":
…[truncated 438 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7588
}
```

</details>

---


### Tool call

_source line 608 · 2026-05-23T02:29:53.454751+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form criteria, all scoring dimensions, their scales, and descriptions. Include: Overall Assessment scale, Soundness, Excitement/Novelty, Reproducibility, and any other dimensions with their full rating scales."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form criteria, all scoring dimensions, their scales, and descriptions. Include: Overall Assessment scale, Soundness, Excitement/Novelty, Reproducibility, and any other dimensions with their full rating scales."
  }
}
```

</details>

---


### Tool call

_source line 609 · 2026-05-23T02:29:55.868580+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines including: what reviewers should evaluate, how to assess soundness, novelty, clarity, significance, reproducibility. Include any specific instructions about scoring, what constitutes a strong vs weak paper, and ethical review guidelines."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines including: what reviewers should evaluate, how to assess soundness, novelty, clarity, significance, reproducibility. Include any specific instructions about scoring, what constitutes a strong vs weak paper, and ethical review guidelines."
  }
}
```

</details>

---


### Tool call

_source line 610 · 2026-05-23T02:29:57.274029+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/submitted.pdf",
  "project": "nlp_variance_gtheory",
  "pages": "11-16",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/submitted.pdf",
    "project": "nlp_variance_gtheory",
    "pages": "11-16",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 611 · 2026-05-23T02:29:57.775909+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 612 · 2026-05-23T02:29:58.780582+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 613 · 2026-05-23T02:29:59.382875+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 614 · 2026-05-23T02:29:59.834912+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 615 · 2026-05-23T02:30:00.186747+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 616 · 2026-05-23T02:30:00.740131+00:00_

# ACL Rolling Review Form - Complete Criteria & Scales

## Overall Assessment
**Scale: 1-5 (with .5 increments)**
- 5: Consider for Award (top 2.5% papers)
- 4.5: Borderline Award
- 4: Conference acceptance
- 3.5: Borderline Conference
- 3: Findings acceptance
- 2.5: Borderline Findings
- 2: Resubmit next cycle
- 1.5: Resubmit after next cycle
- 1: Do not resubmit

## Soundness
**Scale: 1-5 (with .5 increments)**
- 5: "one of the most thorough" studies given its type
- 4: Strong support for claims; extra experiments optional
- 3: Sufficient support for main claims; minor points need detail
- 2: Main claims lack support; major technical problems
- 1: Insufficiently thorough or irrelevant to ACL

## Excitement/Novelty
**Scale: 1-5 (with .5 increments)**
- 5: Highly Exciting; would recommend to others
- 4: Exciting; would mention to colleagues
- 3: Interesting; might attend presentation
- 2: Potentially Interesting; limited personal resonance
- 1: Not Exciting; lacks relevance to NLP community

## Reviewer Confidence
**Scale: 1-5**
- 5: Positive evaluation; very careful review
- 4: Quite sure; unlikely to have missed important points
- 3: Pretty sure; possible gaps in detail checking
- 2: Willing to defend but likely missed details
- 1: Outside expertise area or incomprehensible paper

## Reproducibility
**Scale: 1-5**
- 5: Results easily reproducible
- 4: Mostly reproducible; minor variance possible
- 3: Reproducible with difficulty; underspecified parameters
- 2: Hard to reproduce; unavailable data/insufficient details
- 1: Impossible to reproduce

## Datasets & Software
**Scale: 1-5 (identical for both)**
- 5: Enabling; affects research direction
- 4: Useful for researchers/developers
- 3: Potentially useful
- 2: Documentary value for replication
- 1: None released

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7285
}
```

</details>

---


### Tool result

_source line 617 · 2026-05-23T02:30:05.968192+00:00_

# ARR Reviewer Guidelines Summary

## Core Evaluation Framework

Reviewers assess papers using three primary scores:

- **Soundness**: Technical validity and methodological rigor
- **Excitement**: Personal interest and subjective appeal
- **Overall Recommendation**: Composite judgment for acceptance consideration

## Key Assessment Dimensions

### Soundness Evaluation
"Soundness scores must be justified by the text of the review." Low scores require explicit justification of major faults. Reviewers should verify that methodology is technically correct and appropriately scoped for claims made.

### What Constitutes Strong Papers

Strong submissions demonstrate:
- Clear research questions addressing genuine knowledge gaps
- Appropriate methodology matching the research aim
- Sufficient evidence supporting stated claims
- Technical validity in proofs, experiments, or arguments
- Fair representation of related work
- Reproducible results with sufficient implementation details

### Common Evaluation Pitfalls to Avoid

The guidelines identify 17 heuristics that reflect reviewer bias rather than paper weakness, including dismissing work for being "too simple," lacking SOTA results, or using non-preferred methodologies. Reviewers should reassess when relying on these patterns.

## Assessment of Specific Dimensions

**Novelty**: Requires explicit references to prior work published 3+ months before submission. Negative results and reproductions are valid contributions if properly framed.

**Clarity**: Specificity matters—vague criticisms lack utility. Reviewers should identify exactly which concepts need clarification and where information is missing.

**Reproducibility**: Assess whether sufficient detail exists for reimplementation, including hyperparameters, dataset specifications, and code availability plans. This doesn't require actually running code.

**Significance**: Evaluate impact potential for the target community, not just citation counts or SOTA achievement. Resou
…[truncated 1262 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 10099
}
```

</details>

---


### Tool result

_source line 618 · 2026-05-23T02:30:07.580985+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 580.8}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 546.0}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 469.6}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 423.1}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 418.2}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 118.1}], \"total_pages\": 16, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 10306
}
```

</details>

---


### Tool result

_source line 619 · 2026-05-23T02:30:10.447938+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 10613
}
```

</details>

---


### Tool result

_source line 620 · 2026-05-23T02:30:10.453435+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 10266
}
```

</details>

---


### Tool result

_source line 621 · 2026-05-23T02:30:10.454492+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 11071
}
```

</details>

---


### Tool result

_source line 622 · 2026-05-23T02:30:10.505478+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 11724
}
```

</details>

---


### Tool result

_source line 623 · 2026-05-23T02:30:10.506142+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 12730
}
```

</details>

---


### Tool call

_source line 624 · 2026-05-23T02:30:17.185091+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 625 · 2026-05-23T02:30:17.842545+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 626 · 2026-05-23T02:30:18.496538+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 627 · 2026-05-23T02:30:19.305547+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 628 · 2026-05-23T02:30:19.357570+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 629 · 2026-05-23T02:30:19.358705+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2173
}
```

</details>

---


### Tool result

_source line 630 · 2026-05-23T02:30:20.466253+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2623
}
```

</details>

---


### Tool result

_source line 631 · 2026-05-23T02:30:21.169433+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2672
}
```

</details>

---


### Tool result

_source line 632 · 2026-05-23T02:30:21.522533+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2216
}
```

</details>

---


### Tool result

_source line 633 · 2026-05-23T02:30:21.523251+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2165
}
```

</details>

---


### Tool call

_source line 634 · 2026-05-23T02:30:29.758568+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 635 · 2026-05-23T02:30:29.961565+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 636 · 2026-05-23T02:30:30.620466+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 861
}
```

</details>

---


### Tool call

_source line 637 · 2026-05-23T02:30:30.771404+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 638 · 2026-05-23T02:30:30.873728+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 912
}
```

</details>

---


### Tool call

_source line 639 · 2026-05-23T02:30:31.025566+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 640 · 2026-05-23T02:30:31.780696+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1009
}
```

</details>

---


### Tool call

_source line 641 · 2026-05-23T02:30:31.782778+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 642 · 2026-05-23T02:30:32.084901+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1059
}
```

</details>

---


### Tool call

_source line 643 · 2026-05-23T02:30:32.085228+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 644 · 2026-05-23T02:30:32.187585+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Tool result

_source line 645 · 2026-05-23T02:30:32.439752+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 656
}
```

</details>

---


### Tool call

_source line 646 · 2026-05-23T02:33:37.175509+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex",
  "limit": "120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex",
    "limit": "120"
  }
}
```

</details>

---


### Tool result

_source line 647 · 2026-05-23T02:33:37.277541+00:00_

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
11	\usepackage{graphicx}
12	\usepackage{amsmath,amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{xcolor}
16	
17	\graphicspath{{../../figures/paper/}}
18	
19	\title{Reproducibility Budgets for Open-Weight LLM Evaluation:\\A Generalizability Theory Study of 7--9B Instruction-Tuned Models}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\begin{abstract}
27	\input{abstract}
28	\end{abstract}
29	
30	% === INTRODUCTION ===
31	\input{introduction}
32	
33	% === RELATED WORK ===
34	\input{related_work}
35	
36	% === METHOD ===
37	\input{method}
38	
39	% === EXPERIMENTS ===
40	\input{experiments}
41	
42	% === CONCLUSION ===
43	\input{conclusion}
44	
45	% === LIMITATIONS ===
46	\input{limitations}
47	
48	\bibliography{references}
49	
50	% === APPENDIX ===
51	\input{appendix}
52	
53	\end{document}
54	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 648 · 2026-05-23T02:33:40.904779+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 649 · 2026-05-23T02:33:40.955350+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 650 · 2026-05-23T02:33:44.021018+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 651 · 2026-05-23T02:33:44.322294+00:00_

1	\section{Method and Experimental Design}
2	\label{sec:method}
3	
4	\subsection{Generalizability Theory}
5	\label{sec:gtheory}
6	
7	Generalizability theory (G-theory) treats each measurement as one observation from a universe of admissible conditions defined by the crossed facets of an evaluation design \cite{shavelson1991generalizability, brennan2001generalizability}. The \emph{object of measurement} is the entity whose consistency is of interest. In our setting, test items ($p$) serve as the object of measurement, and the goal is to determine how reliably item-level scores generalize across the methodological conditions under which they are collected.
8	
9	A \emph{G-study} decomposes total observed variance into components $\sigma^2_x$ for each facet $x$ and their interactions. Each component quantifies how much variability that source contributes to the overall measurement. Large interaction components (e.g., $\sigma^2_{pM}$ for item-by-model) indicate that facets do not affect items uniformly but instead create differential difficulty profiles. We estimate variance components via Henderson Method~I, an unbiased ANOVA-based estimator for balanced designs \cite[Ch.~3]{brennan2001generalizability}, with 1,000-resample bootstrap confidence intervals \cite{efron1993bootstrap} (item-level resampling with replacement, preserving the fully-crossed structure across all other facets) \cite{li2023bootstrap}.
10	
11	A \emph{D-study} projects the generalizability coefficient under hypothetical designs with different numbers of conditions per facet:
12	\begin{equation}
13	G_\text{item} = \frac{\sigma^2_p}{\sigma^2_p + \sigma^2_\text{rel}}
14	\label{eq:gcoeff}
15	\end{equation}
16	where $\sigma^2_\text{rel}$ aggregates all item-by-facet interaction variances, each divided by the number of conditions for the corresponding facets \cite[Ch.~4]{brennan2001generalizability}. This prospective capability distinguishes G-theory from classical ANOVA: rather than only attributing varia
…[truncated 10670 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 652 · 2026-05-23T02:33:44.322674+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 653 · 2026-05-23T02:33:44.423497+00:00_

1	\section{Experiments}
2	
3	All experiments use open-weight 7--9B parameter models evaluated with vLLM~0.9.2 on a single NVIDIA RTX PRO 6000 GPU (96GB) with binary correctness scoring.
4	
5	\subsection{Single-Model Baseline}
6	
7	We first establish the variance structure within a single model (Llama-3.1-8B-Instruct) on MMLU to isolate methodological facet contributions before introducing cross-model variation.
8	
9	\paragraph{Design.} The G-study crosses six facets: 200 items $\times$ 3 numerical precisions (BF16, FP16, FP32) $\times$ 6 prompt templates $\times$ 6 random seeds $\times$ 3 temperature levels (0.0, 0.3, 0.7) $\times$ 4 answer orderings, yielding 259,200 binary observations. Variance components are estimated via Henderson Method~I with bootstrap confidence intervals (1,000 resamples).
10	
11	\paragraph{Results.} Under binary scoring, item difficulty (\texttt{item\_id}) accounts for 58.4\% of total variance, with the residual term contributing 23.1\%. All main facet effects are negligible ($<$1\% each): precision 0.9\%, prompt template, temperature, seed, and ordering each $<$0.5\%. The interesting structure appears in item-conditional interactions: prompt$\times$item is the largest at 5.5\%, followed by seed$\times$item (4.7\%), precision$\times$item (3.3\%), temperature$\times$item (2.9\%), and ordering$\times$item (0.8\%). This pattern indicates that methodological choices do not shift performance uniformly across items; instead, specific items are differentially sensitive to specific facets---prompt template variation produces the largest item-conditional effect.
12	
13	The resulting generalizability coefficient is $G_\text{item} = 0.936$, indicating that 200 items under multi-facet conditions produce highly reliable rankings. A D-study projection shows $G \geq 0.80$ is achievable with as few as 55 items in this multi-facet design.
14	
15	For text-exact-match scoring (requiring verbatim string matches), the variance structure shifts dramatically: te
…[truncated 11477 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 654 · 2026-05-23T02:33:49.594801+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 655 · 2026-05-23T02:33:49.796434+00:00_

1	\appendix
2	\section{Additional Robustness Analyses}
3	\label{app:robustness}
4	
5	We report nine robustness analyses that verify the stability of the variance decomposition under alternative analytical choices.
6	
7	\paragraph{GLMM complement.} A generalized linear mixed model (GLMM) with marginal logit link produces variance component rankings that perfectly preserve all seven grouped component orderings ($\rho = 1.0$) relative to Henderson Method~I \cite{jiang2018bayesian, tuerlinckx2006glmm}. This confirms that the linear variance decomposition is robust to the binary outcome distribution.
8	
9	\paragraph{Accuracy-range stability.} The \texttt{item\_id} variance share remains stable across subsets with mean accuracy from 0.62 to 0.72 ($r = -0.048$). This rules out distortion from binary floor or ceiling effects at observed accuracy levels.
10	
11	\paragraph{Estimator robustness.} We compare Henderson Method~I with restricted maximum likelihood (REML-EM, 500 iterations, practical convergence $\Delta < 0.003$ percentage points). All variance components differ by $<$0.5 percentage points between estimators. The largest discrepancy occurs on the residual component (0.47pp); all substantive components (item, model$\times$item, model) differ by $<$0.3pp. Henderson Method~I is preferred for our balanced designs because it produces unbiased estimates without distributional assumptions \cite[Ch.~12]{brennan2001generalizability}.
12	
13	\paragraph{Probit simulation.} A probit simulation matched to our 1,296-condition design confirms that Henderson Method~I recovers variance component rankings from dichotomized data (Spearman $\rho = 0.732$ between binary and continuous rankings, excluding residual; \texttt{item\_id} dominant in all 100 replications; top-5 ordering correct in 79\% of replications). Bias analysis by difficulty stratum shows $|\text{bias}| = 0.28$--$0.37$ for items with $p \in [0.5, 0.8]$, where the Bernoulli variance ceiling $p(1{-}p)$ is largest. This an
…[truncated 22080 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 656 · 2026-05-23T02:33:49.897194+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 657 · 2026-05-23T02:33:49.947823+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Our eight models share the 2024--2025 instruction-tuning paradigm; temporal correlation may limit exchangeability, and results do not generalize to API-based or base models. Preliminary within-family 72B validation (\S4.6) suggests stable variance structure across scales, but is limited to a single architecture (Qwen2.5); the Qwen2.5 family shares training recipes and tokenizer, so validating with architecturally distinct families (e.g., Llama-3 70B, Mistral-Large) is necessary before extrapolating budget recommendations to arbitrary model families. The benchmark sample ($n = 5$) limits statistical power for format-associated observations ($p = 0.10$); other formats (code generation, multi-turn dialogue) may differ. All D-study budgets reported in this paper are strictly valid only under binary correctness scoring. Our partial-credit pilot (GSM8K only, single model) shows $G$ drops from 0.76 to 0.55 with $\rho = 0.26$ for item rankings, indicating budgets do not transfer to finer-grained scoring rubrics; the partial-credit analysis is limited to a single benchmark and single model, and its generalizability is unknown. Our design varies few-shot example ordering but not example identity, a known variance source. All eight models may have encountered benchmark items during pre-training; differential contamination across architectures could inflate model$\times$item interaction \citep{golchin2023contamination, oren2024proving}, though consistent variance structures across three independently constructed MC benchmarks provide indirect evidence against contamination as the sole driver. Contamination affects absolute budget estimates but has limited impact on the multi-facet vs.\ single-condition budget \emph{ratio}, since both designs are equally exposed to contaminated items.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 658 · 2026-05-23T02:45:48.212652+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## 总体评分\n**Overall**: 3.5 / 5 — Borderline Conference\n**一句话总结**: 方法论执行扎实、鲁棒性验证异常充分，但 D-study 预算的数学推导不完整、binary scoring 对投影精度的影响未量化，且 G_item 与实际模型比较可靠性之间的概念鸿沟削弱了核心贡献的说服力。\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方差分解本身正确，Henderson Method I 适用性验证充分；但 D-study item budget 公式不完整（Equation 1 不含 n_p），binary 数据对投影精度的系统性偏差未量化 |\n| Excitement | 3.5/5 | G-theory 应用于 LLM 评估是新颖且实用的，format-associated patterns 有洞察价值，但核心方法论是成熟框架的领域迁移，非方法论创新 |\n| Reproducibility | 4/5 | 实验描述详尽，承诺开源代码/数据/计算器；但 D-study 投影公式不完整，外部读者无法独立验证 item budget 数值 |\n| Confidence | 4/5 | 对 G-theory 和 LLM 评估方法论有深入了解，仔细验证了公式和数值 |\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] D-study item budget 计算公式不完整，核心贡献不可独立验证\n\n- 具体位置：Section 3.1 Equation 1；Section 4.5 Table 4；Appendix B Table 7\n- 问题：Equation 1 定义 $G_\\text{item} = \\sigma^2_p / (\\sigma^2_p + \\sigma^2_\\text{rel})$，其中 $\\sigma^2_\\text{rel}$ 仅依赖各 facet 的条件数（$n_M, n_\\delta$ 等），不包含 item 数量 $n_p$。据此公式，multi-facet 下 $G = 58.4/(58.4+3.985) = 0.936$，single-condition 下 $G = 58.4/(58.4+40.3) = 0.592$——这些值与 Table 4 中 G_200 一致，但与 $n_p$ 无关。然而 Table 4 同时报告了 $n_{G\\geq0.80} = 55$（multi-facet）和 $552$（single-condition），Figure 1 的 D-study 曲线也显示 G 随 item 数增加而上升。这意味着实际计算使用了一个包含 $n_p$ 的公式（可能是 Spearman-Brown 或 Brennan 2001 Ch. 4 中 aggregate score 的可靠性公式），但论文从未给出。\n- 我尝试验证的计算：通过 G(200) = 0.592 和 n_{G≥0.80} = 552 反推，得到 single-item 可靠性约 0.0072，与 Spearman-Brown 公式 G(n) = nG₁/(1+(n-1)G₁) 一致（G(552) ≈ 0.80 ✓）。但这与 Equation 1 给出的 G = 0.592 完全不同，说明论文中实际存在两个不同的 G 指标但只明确定义了一个。\n- 为什么影响接收：D-study 预算是论文的核心实用贡献（标题和摘要的主角），但读者无法从论文中独立验证 \"178 items for G ≥ 0.80\" 等关键数字。这是可复现性的根本问题。\n- 建议修改方向：(a) 在 Section 3.1 完整给出 D-study 投影公式，明确 G 如何同时依赖 $n_p$（item 数）和 $n_f$（各 facet 条件数），区分 per-item G 和 aggregate-score G；(b) 提供一个从 variance components 到 Table 4 数值的完整计算示例。\n\n**N2** [critical] Binary scoring 对 D-study 投影精度的系统性影响未量化\n\n- 具体位置：Section 3.5；Appendix A（Probit simulation）\n- 问题：Probit simulation 报告 binary 与 continuous variance components 之间 Spearman $\\rho = 0.732$（excluding residual），top-5 ordering 仅在 79% 的 replications 中正确，中等难度 items 的偏差 |bias| = 0.28–0.37。这些数字说明 binary scoring 引入了中等程度的系统性偏差。然而论文从未评估这种偏差对 D-study 投影（55 items, 178 items, 552 items）的影响——bootstrap CIs 捕捉的是抽样变异性，不是 binary scoring 的系统性偏差。\n- 为什么影响接收：如果 variance components 因 binary scoring 存在系统偏差，D-study 的具体 item 数推荐可能不准确。论文的实用价值取决于这些数字的可信度。ρ = 0.732 意味着约 46% 的组分排名变异性未被恢复——这是否足以改变 \"178 items\" 的推荐？论文没有回答。\n- 建议修改方向：(a) 从 probit simulation 的 continuous variance components 计算 D-study projections，与 binary 版本比较；(b) 报告 D-study budget 在 binary vs. continuous 下的差异（绝对 item 数和百分比），让读者评估推荐的鲁棒性；(c) 如果差异大，修改置信区间以包含系统偏差。\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] G_item 测量的是 item 难度可靠性，非模型比较可靠性——概念鸿沟未讨论\n\n- 具体位置：Section 3.1（object of measurement 定义）；Section 4.5（D-study budgets）；Introduction（\"reproducibility budgets for LLM evaluation\"）\n- 问题：论文明确定义 items 为 object of measurement（Section 3.1），G_item 衡量的是 \"how reliably item-level scores generalize across methodological conditions\"。但论文的动机和实际应用场景是 model evaluation reproducibility——实践者想知道\"我需要多少评测来可靠区分模型\"。这是不同的 G-theory 问题：model ranking reliability 需要将 models 作为 object of measurement。从 Table 2 看，σ²_model 仅 2.8%，model-level G coefficient 在当前设计下可能显著低于 G_item。论文始终使用 G_item 但以 \"reproducibility budget for evaluation\" 的措辞呈现结果，构成 framing mismatch。\n- 建议：(a) 显式计算 G_model（models 为 object，items 为 facet），展示在推荐设计下的值；(b) 正式讨论 G_item ≥ 0.80 蕴含（或不蕴含）model ranking reliability 的条件；(c) 如果两者差距大，调整推荐。\n\n**W2** [warning] 模型可交换性假设的 out-of-sample 验证不足\n\n- 具体位置：Section 3.5；Appendix A（LOMO）；Section 4.6（72B validation）\n- 问题：8 个 purposively selected 模型被处理为 quasi-random facet。LOMO 分析（CV ≤ 1.25%，Table 5）和 four-model subset check（|ΔG| ≤ 0.029/0.065，Table 8）都是 within-sample stability metrics——它们验证了这 8 个模型可互换，但不能证明 target universe 中的其他模型也会产生类似方差结构。72B validation 仅在 Qwen2.5 family 内（共享 tokenizer 和训练方法），不是 cross-family evidence。论文引用的 Meredith (1993) 和 Putnick & Bornstein (2016) 讨论的是 measurement invariance testing，不是将 purposive samples 作为 random 的 G-theory 正当性。\n- 建议：(a) 从其他 family（如 Llama-3 70B 或 Mistral-Large）获取至少一个 cross-family validation point；(b) 更明确地限定 budget 推荐的适用范围（\"for these 8 specific architecture families\" vs. \"for 7-9B instruction-tuned models in general\"）；(c) 讨论 2024-2025 instruction-tuning paradigm 的时间相关性对 exchangeability 的影响。\n\n**W3** [warning] Partial-credit pilot 基于单 benchmark、单 model，但结论陈述过于确定\n\n- 具体位置：Section 3.5；Appendix A（Scoring metric sensitivity）\n- 问题：论文基于 GSM8K + Llama-3.1-8B 的 partial-credit pilot 得出 \"D-study budgets do not transfer to finer-grained scoring rubrics\"（Section 3.5），且在 abstract 中强调 \"a tradeoff that favors multi-condition designs\"。然而这只是单 benchmark、单 model 的实验，partial-credit scoring 的具体方法（step-level credit 如何定义？多少 levels？）未在正文中描述。ρ = 0.26 可能反映特定 scoring rubric 的 artifact 而非 general pattern。Limitations section 承认了这一点但 main text 的措辞仍然是 definitive 的。\n- 建议：(a) 将 main text 中的表述从 \"do not transfer\" 改为 \"preliminary evidence suggests limited transferability\"；(b) 至少在一个 MC benchmark 上重复 partial-credit 分析以检验 generality。\n\n**W4** [warning] Format-associated pattern 的统计支撑不足且设计不对称\n\n- 具体位置：Section 4.3；Table 3\n- 问题：MC vs. FF 方差结构差异基于 n = 5 benchmarks（3 MC + 2 FF），permutation test p = 0.10（论文自己承认），benchmark-level CI 包含 zero（[-1.7, 5.1]）。同时，实验设计不对称：ordering facet 仅对 MC 有效，MC 和 FF 使用不同类型的 prompt templates（option layout vs. CoT elicitation）。这些设计差异可能 confound format comparison。论文在 Section 4.3 末尾承认了这一点（\"potentially confounding format comparisons\"），但 Table 3 和 Figure 3 的呈现方式仍然暗示 format 是 causal driver。\n- 建议：(a) 在 Table 3 标题中注明统计显著性不足；(b) 更明确地将 format patterns 标注为 descriptive/exploratory 而非 confirmatory；(c) 讨论 prompt type confound 的可能影响。\n\n## 小问题（不影响接收）\n\n- **M1**：Table 2 和 Table 3 中 \"all others < 0.1%\" / \"< 1.0%\" 不够精确——建议报告具体数值或提供附录表格，方便读者独立重现 G coefficient 计算。\n- **M2**：Section 3.2 提到 temperature 三个水平为 0.0/0.3/0.7，但许多评测实践使用 temperature = 1.0（default for some APIs）。排除 1.0 可能低估 temperature-related variance。\n- **M3**：所有实验使用单一推理引擎（vLLM 0.9.2）。不同引擎（TGI, transformers, llama.cpp）可能引入额外的 numerical precision variance，这没有被 captured。\n- **M4**：每 benchmark 200 items（stratified from MMLU 57 subjects，deterministic seed 42 for others）。200 items 对 MMLU（14K items）的代表性可能不足——cross-subject generalization \"remains untested\"（Section 3.2）。\n- **M5**：Few-shot example identity 未作为 facet（Limitations 已承认），但这是已知的 significant variance source（Sclar et al., 2024）。\n\n## 主要优势\n\n1. **问题意义重大**：LLM 评估可复现性是领域级别的痛点，G-theory 框架提供了严格的理论工具来量化和优化评估设计。这是将心理测量学引入 NLP 的 timely contribution。\n2. **实验规模充分**：~230 万 binary records，8 模型 × 5 benchmarks × 7 facets，factorial design 的规模在同类工作中罕见。\n3. **鲁棒性验证异常全面**：9 项附录分析（GLMM complement, probit simulation, null calibration, REML comparison, LOMO, inter-model agreement, CI method comparison, facet specification sensitivity, reduced crossing validation）系统性地排除了常见的 methodological threats。这是论文最突出的优势。\n4. **实用输出具体可操作**：D-study budget recommendations（如 \"3-prompt × 3-seed with 178 items for G ≥ 0.80\"）可直接指导 benchmark 设计，承诺开源的 D-study calculator 有实际工程价值。\n5. **Limitations section 坦诚且全面**：binary scoring 限制、model exchangeability、benchmark sample size、contamination 等都有诚实讨论。\n6. **Subject-level 分析有洞察价值**：Table 10 揭示 reasoning-heavy subjects（high_school_math: G = 0.614）与 knowledge-intensive subjects（international_law: G = 0.930）的显著差异，对 benchmark 设计者有直接参考价值。\n",
  "reviewer_id": "1",
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## 总体评分\n**Overall**: 3.5 / 5 — Borderline Conference\n**一句话总结**: 方法论执行扎实、鲁棒性验证异常充分，但 D-study 预算的数学推导不完整、binary scoring 对投影精度的影响未量化，且 G_item 与实际模型比较可靠性之间的概念鸿沟削弱了核心贡献的说服力。\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方差分解本身正确，Henderson Method I 适用性验证充分；但 D-study item budget 公式不完整（Equation 1 不含 n_p），binary 数据对投影精度的系统性偏差未量化 |\n| Excitement | 3.5/5 | G-theory 应用于 LLM 评估是新颖且实用的，format-associated patterns 有洞察价值，但核心方法论是成熟框架的领域迁移，非方法论创新 |\n| Reproducibility | 4/5 | 实验描述详尽，承诺开源代码/数据/计算器；但 D-study 投影公式不完整，外部读者无法独立验证 item budget 数值 |\n| Confidence | 4/5 | 对 G-theory 和 LLM 评估方法论有深入了解，仔细验证了公式和数值 |\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] D-study item budget 计算公式不完整，核心贡献不可独立验证\n\n- 具体位置：Section 3.1 Equation 1；Section 4.5 Table 4；Appendix B Table 7\n- 问题：Equation 1 定义 $G_\\text{item} = \\sigma^2_p / (\\sigma^2_p + \\sigma^2_\\text{rel})$，其中 $\\sigma^2_\\text{rel}$ 仅依赖各 facet 的条件数（$n_M, n_\\delta$ 等），不包含 item 数量 $n_p$。据此公式，multi-facet 下 $G = 58.4/(58.4+3.985) = 0.936$，single-condition 下 $G = 58.4/(58.4+40.3) = 0.592$——这些值与 Table 4 中 G_200 一致，但与 $n_p$ 无关。然而 Table 4 同时报告了 $n_{G\\geq0.80} = 55$（multi-facet）和 $552$（single-condition），Figure 1 的 D-study 曲线也显示 G 随 item 数增加而上升。这意味着实际计算使用了一个包含 $n_p$ 的公式（可能是 Spearman-Brown 或 Brennan 2001 Ch. 4 中 aggregate score 的可靠性公式），但论文从未给出。\n- 我尝试验证的计算：通过 G(200) = 0.592 和 n_{G≥0.80} = 552 反推，得到 single-item 可靠性约 0.0072，与 Spearman-Brown 公式 G(n) = nG₁/(1+(n-1)G₁) 一致（G(552) ≈ 0.80 ✓）。但这与 Equation 1 给出的 G = 0.592 完全不同，说明论文中实际存在两个不同的 G 指标但只明确定义了一个。\n- 为什么影响接收：D-study 预算是论文的核心实用贡献（标题和摘要的主角），但读者无法从论文中独立验证 \"178 items for G ≥ 0.80\" 等关键数字。这是可复现性的根本问题。\n- 建议修改方向：(a) 在 Section 3.1 完整给出 D-study 投影公式，明确 G 如何同时依赖 $n_p$（item 数）和 $n_f$（各 facet 条件数），区分 per-item G 和 aggregate-score G；(b) 提供一个从 variance components 到 Table 4 数值的完整计算示例。\n\n**N2** [critical] Binary scoring 对 D-study 投影精度的系统性影响未量化\n\n- 具体位置：Section 3.5；Appendix A（Probit simulation）\n- 问题：Probit simulation 报告 binary 与 continuous variance components 之间 Spearman $\\rho = 0.732$（excluding residual），top-5 ordering 仅在 79% 的 replications 中正确，中等难度 items 的偏差 |bias| = 0.28–0.37。这些数字说明 binary scoring 引入了中等程度的系统性偏差。然而论文从未评估这种偏差对 D-study 投影（55 items, 178 items, 552 items）的影响——bootstrap CIs 捕捉的是抽样变异性，不是 binary scoring 的系统性偏差。\n- 为什么影响接收：如果 variance components 因 binary scoring 存在系统偏差，D-study 的具体 item 数推荐可能不准确。论文的实用价值取决于这些数字的可信度。ρ = 0.732 意味着约 46% 的组分排名变异性未被恢复——这是否足以改变 \"178 items\" 的推荐？论文没有回答。\n- 建议修改方向：(a) 从 probit simulation 的 continuous variance components 计算 D-study projections，与 binary 版本比较；(b) 报告 D-study budget 在 binary vs. continuous 下的差异（绝对 item 数和百分比），让读者评估推荐的鲁棒性；(c) 如果差异大，修改置信区间以包含系统偏差。\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] G_item 测量的是 item 难度可靠性，非模型比较可靠性——概念鸿沟未讨论\n\n- 具体位置：Section 3.1（object of measurement 定义）；Section 4.5（D-study budgets）；Introduction（\"reproducibility budgets for LLM evaluation\"）\n- 问题：论文明确定义 items 为 object of measurement（Section 3.1），G_item 衡量的是 \"how reliably item-level scores generalize across methodological conditions\"。但论文的动机和实际应用场景是 model evaluation reproducibility——实践者想知道\"我需要多少评测来可靠区分模型\"。这是不同的 G-theory 问题：model ranking reliability 需要将 models 作为 object of measurement。从 Table 2 看，σ²_model 仅 2.8%，model-level G coefficient 在当前设计下可能显著低于 G_item。论文始终使用 G_item 但以 \"reproducibility budget for evaluation\" 的措辞呈现结果，构成 framing mismatch。\n- 建议：(a) 显式计算 G_model（models 为 object，items 为 facet），展示在推荐设计下的值；(b) 正式讨论 G_item ≥ 0.80 蕴含（或不蕴含）model ranking reliability 的条件；(c) 如果两者差距大，调整推荐。\n\n**W2** [warning] 模型可交换性假设的 out-of-sample 验证不足\n\n- 具体位置：Section 3.5；Appendix A（LOMO）；Section 4.6（72B validation）\n- 问题：8 个 purposively selected 模型被处理为 quasi-random facet。LOMO 分析（CV ≤ 1.25%，Table 5）和 four-model subset check（|ΔG| ≤ 0.029/0.065，Table 8）都是 within-sample stability metrics——它们验证了这 8 个模型可互换，但不能证明 target universe 中的其他模型也会产生类似方差结构。72B validation 仅在 Qwen2.5 family 内（共享 tokenizer 和训练方法），不是 cross-family evidence。论文引用的 Meredith (1993) 和 Putnick & Bornstein (2016) 讨论的是 measurement invariance testing，不是将 purposive samples 作为 random 的 G-theory 正当性。\n- 建议：(a) 从其他 family（如 Llama-3 70B 或 Mistral-Large）获取至少一个 cross-family validation point；(b) 更明确地限定 budget 推荐的适用范围（\"for these 8 specific architecture families\" vs. \"for 7-9B instruction-tuned models in general\"）；(c) 讨论 2024-2025 instruction-tuning paradigm 的时间相关性对 exchangeability 的影响。\n\n**W3** [warning] Partial-credit pilot 基于单 benchmark、单 model，但结论陈述过于确定\n\n- 具体位置：Section 3.5；Appendix A（Scoring metric sensitivity）\n- 问题：论文基于 GSM8K + Llama-3.1-8B 的 partial-credit pilot 得出 \"D-study budgets do not transfer to finer-grained scoring rubrics\"（Section 3.5），且在 abstract 中强调 \"a tradeoff that favors multi-condition designs\"。然而这只是单 benchmark、单 model 的实验，partial-credit scoring 的具体方法（step-level credit 如何定义？多少 levels？）未在正文中描述。ρ = 0.26 可能反映特定 scoring rubric 的 artifact 而非 general pattern。Limitations section 承认了这一点但 main text 的措辞仍然是 definitive 的。\n- 建议：(a) 将 main text 中的表述从 \"do not transfer\" 改为 \"preliminary evidence suggests limited transferability\"；(b) 至少在一个 MC benchmark 上重复 partial-credit 分析以检验 generality。\n\n**W4** [warning] Format-associated pattern 的统计支撑不足且设计不对称\n\n- 具体位置：Section 4.3；Table 3\n- 问题：MC vs. FF 方差结构差异基于 n = 5 benchmarks（3 MC + 2 FF），permutation test p = 0.10（论文自己承认），benchmark-level CI 包含 zero（[-1.7, 5.1]）。同时，实验设计不对称：ordering facet 仅对 MC 有效，MC 和 FF 使用不同类型的 prompt templates（option layout vs. CoT elicitation）。这些设计差异可能 confound format comparison。论文在 Section 4.3 末尾承认了这一点（\"potentially confounding format comparisons\"），但 Table 3 和 Figure 3 的呈现方式仍然暗示 format 是 causal driver。\n- 建议：(a) 在 Table 3 标题中注明统计显著性不足；(b) 更明确地将 format patterns 标注为 descriptive/exploratory 而非 confirmatory；(c) 讨论 prompt type confound 的可能影响。\n\n## 小问题（不影响接收）\n\n- **M1**：Table 2 和 Table 3 中 \"all others < 0.1%\" / \"< 1.0%\" 不够精确——建议报告具体数值或提供附录表格，方便读者独立重现 G coefficient 计算。\n- **M2**：Section 3.2 提到 temperature 三个水平为 0.0/0.3/0.7，但许多评测实践使用 temperature = 1.0（default for some APIs）。排除 1.0 可能低估 temperature-related variance。\n- **M3**：所有实验使用单一推理引擎（vLLM 0.9.2）。不同引擎（TGI, transformers, llama.cpp）可能引入额外的 numerical precision variance，这没有被 captured。\n- **M4**：每 benchmark 200 items（stratified from MMLU 57 subjects，deterministic seed 42 for others）。200 items 对 MMLU（14K items）的代表性可能不足——cross-subject generalization \"remains untested\"（Section 3.2）。\n- **M5**：Few-shot example identity 未作为 facet（Limitations 已承认），但这是已知的 significant variance source（Sclar et al., 2024）。\n\n## 主要优势\n\n1. **问题意义重大**：LLM 评估可复现性是领域级别的痛点，G-theory 框架提供了严格的理论工具来量化和优化评估设计。这是将心理测量学引入 NLP 的 timely contribution。\n2. **实验规模充分**：~230 万 binary records，8 模型 × 5 benchmarks × 7 facets，factorial design 的规模在同类工作中罕见。\n3. **鲁棒性验证异常全面**：9 项附录分析（GLMM complement, probit simulation, null calibration, REML comparison, LOMO, inter-model agreement, CI method comparison, facet specification sensitivity, reduced crossing validation）系统性地排除了常见的 methodological threats。这是论文最突出的优势。\n4. **实用输出具体可操作**：D-study budget recommendations（如 \"3-prompt × 3-seed with 178 items for G ≥ 0.80\"）可直接指导 benchmark 设计，承诺开源的 D-study calculator 有实际工程价值。\n5. **Limitations section 坦诚且全面**：binary scoring 限制、model exchangeability、benchmark sample size、contamination 等都有诚实讨论。\n6. **Subject-level 分析有洞察价值**：Table 10 揭示 reasoning-heavy subjects（high_school_math: G = 0.614）与 knowledge-intensive subjects（international_law: G = 0.930）的显著差异，对 benchmark 设计者有直接参考价值。\n",
    "reviewer_id": "1",
    "project": "nlp_variance_gtheory"
  }
}
```

</details>

---


### Tool result

_source line 659 · 2026-05-23T02:45:51.927730+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_265de443abfe4594f91451b075b582ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3715
}
```

</details>

---


### Tool call

_source line 660 · 2026-05-23T02:45:56.861555+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 661 · 2026-05-23T02:45:56.912209+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 662 · 2026-05-23T02:46:09.553941+00:00_

审稿完成，已提交给 Review Director。

**评分总结**：Overall 3.5（Borderline Conference），Soundness 3.5，Excitement 3.5，Reproducibility 4。

**核心发现**：

- **2 个 Must-Fix**：(1) D-study item budget 公式不完整——Equation 1 不含 n_p，但 Table 4 的 budget 明显依赖 item 数量，实际计算公式未给出，核心贡献无法独立验证；(2) Binary scoring 对 D-study 投影的系统性偏差未量化——probit simulation 仅恢复 ρ=0.732 的排名一致性，bootstrap CI 不捕捉此偏差。

- **4 个 Should-Fix**：G_item vs 模型比较可靠性的概念鸿沟；模型可交换性假设缺乏 out-of-sample 验证；partial-credit pilot 过于有限但结论陈述过于确定；format-associated pattern 统计支撑不足（p=0.10, n=5）。

- **主要优势**：实验规模大（230 万 records）、鲁棒性验证异常全面（9 项分析）、实用输出具体可操作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1"
}
```

</details>

---


## Round 20

## Round 20

4 recorded events


### User

_source line 663 · 2026-05-23T02:46:41.725279+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每一条 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 — 新颖性与完整性审查

**Overall**: 3.5 / 5 — Borderline Conference

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 实验设计严谨；主要扣分：quasi-random model facet 假设在 8 个同代模型上的可迁移性有限 |
| Excitement | 3/5 | G-theory 是成熟框架，应用于 LLM 评估的开创性已被 Messing (2026) 占据；三个扩展方向是 solid incremental work 但非 paradigm shift |
| Reproducibility | 4/5 | 模型全部开源，承诺发布 pipeline；扣分：200 items 具体采样过程需发布 item list |
| Overall | 3.5/5 | 高质量实证工作，适合 Findings；Conference 需更强方法论创新 |

## Must-Fix

**N1** [critical] 相对于 Messing (2026) TEE 的增量贡献定位不够清晰——方法论创新 vs. scale-up 界限模糊
- 三个扩展方向：(i) infrastructure facets 替代 judge identity = facet 选择不同≠方法论不同；(ii) 1→5 benchmarks = scale-up；(iii) D-study projection = 教科书操作
- IRT+G-theory 互补性（Table 4, IRT 116 items single-condition G=0.457 vs. multi-facet G=0.895）是最有潜力的独立贡献点但被埋在 §4.5
- 建议：Contributions 中提升 IRT+G-theory 互补性；Positioning 段对三个方向标注方法论层级

**N2** [critical] Binary scoring conditionality 限制 D-study budget 适用范围，但 title/abstract 暗示更广适用性
- Partial-credit pilot: G 0.76→0.55, ρ=0.26；text-exact-match: G 0.936 vs. 0.007
- 核心产出（178 items, 3×3 design）仅对 binary correctness 有效
- 建议：Title 加 "under Binary Scoring" 限定；Abstract 首句声明 scope

## Should-Fix

**W1** "3.1× item reduction" framing 掩盖 total evaluation 增长（552→1,602 evaluations）
**W2** Format-associated pattern (C2) 占约 1 页但 p=0.10, benchmark-level CI 含零——篇幅奢侈
**W3** Conclusion 过于简短，缺 practical implications
**W4** Related Work 缺 evaluation harness 实现层面文献（lm-eval-harness 整合, MMLU-Redux/Pro）
**W5** Model 样本时间同质性可能高估 model×item interaction 稳定性

## Minor
M1: Abstract 数字密度过高
M2: Table 3 "prompt" 行 MC/FF 含义不同
M3: Appendix table 编号验证
M4: §4.4 过短
M5: Figure 1 y 轴字体偏小

## Questions
1. IRT+G-theory 互补性是否意味最优策略是先 IRT 选 item 再 G-theory 优化 protocol？
2. 是否计划扩展到 LLM-as-judge continuous scoring？
3. 是否可对 8 个模型运行 contamination detection？
4. 72B 验证是否计划增加 cross-family 模型？

## 主要优势
1. 实验规模与设计严谨性（2.3M records, 7 facets, 8 models, 5 benchmarks）
2. 9 项鲁棒性分析极为充分
3. D-study budget calculator 实用价值
4. Binary scoring conditionality 透明处理
5. IRT+G-theory 互补性分析（Table 4）
6. 定位诚实（Positioning paragraph）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 664 · 2026-05-23T02:48:08.362193+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 对 Reviewer 2 意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[REBUT] R2-N1: 相对于 Messing (2026) TEE 的增量贡献定位**\n\nR2 的论点是三个扩展方向都是 incremental：facet 选择不同≠方法论不同、scale-up、教科书操作。我部分不同意。\n\n1. R2 低估了 **fully crossed multi-benchmark factorial design** 的方法论贡献。Messing (2026) 仅在 **单一 benchmark** 上 cross 了 5 个 methodology facets，且排除了 infrastructure facets（Section 2, Related Work: \"excluded infrastructure facets and cross-benchmark comparison\"）。本文 cross 7 facets across 5 benchmarks 不仅是 scale-up，更是第一次将 infrastructure facets（precision, seed）与 methodology facets（prompt, ordering）**同时纳入同一个 factorial design**。这使得 facet 间交互项（如 precision×item = 3.3%, Table 2 单模型分析）首次可被估计，揭示了 infrastructure 与 methodology 的相对贡献——这是 Messing (2026) 结构上无法回答的问题。\n\n2. 但 R2 关于 **IRT+G-theory 互补性被埋没** 的观察我完全赞同。Table 4 中 IRT 116 items 在 single-condition 下 G=0.457、multi-facet 下 G=0.895 的对比，证明了 item selection（IRT）和 protocol optimization（G-theory）是正交的——这是论文最具方法论洞察力的发现，但在 Section 4.5 中只用了约 3 行文字。应当提升至 Contributions。\n\n3. \"D-study projection = 教科书操作\" 的说法过于简化。标准 D-study 假设 continuous data；在 binary data 上进行 D-study 并通过 probit simulation、GLMM complement 和 null calibration 验证其有效性（Appendix A）需要非平凡的 methodological adaptation。\n\n**综合判断**：N1 的严重程度被 R2 高估。论文的贡献不是对 Messing (2026) 的 scale-up，而是在一个结构上更完整的设计中回答了不同的问题（infrastructure + methodology 的联合 variance structure + cross-benchmark generalization + actionable budgets）。但 IRT+G-theory 互补性的呈现确实需要加强。建议从 critical 降为 should-fix。\n\n---\n\n**[AGREE] R2-N2: Binary scoring conditionality 的 scope 限制**\n\n完全同意。这与我的 N2 互补。论文的核心发现高度依赖 binary scoring：\n- Text-exact-match: G 从 0.936 暴跌至 0.007（Section 4.1）\n- Partial-credit: G 从 0.76 降至 0.55，item ranking ρ = 0.26（Appendix A, Scoring metric sensitivity）\n- Section 3.5 明确承认 \"All findings in this paper are conditioned on binary correctness scoring\"\n\n但 title（\"Reproducibility Budgets for Open-Weight LLM Evaluation\"）和 abstract 首句（\"Large Language Model (LLM) evaluation results vary across reproductions\"）均暗示更广的适用性。实际上 D-study budgets **仅对 binary correctness scoring 有效**——这对使用 partial credit、LLM-as-judge、或 continuous metrics 的评测完全不适用。\n\nR2 建议 title 加 \"under Binary Scoring\" 是合理的，至少 abstract 首段应在第一处提及 D-study budget 时立即声明 scope。这确实影响接收决定，因为 framing 的广度与实际适用性之间的 gap 可能误导实践者。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: \"3.1× item reduction\" framing 掩盖 total evaluation 增长**\n\n同意。论文摘要中 \"a 3.1× reduction from 552 single-condition items\" 是 item 数的比较（552→178），但 total evaluations 从 552 增加到 1,602（178 × 9 conditions）——增长了 2.9×。这不是 reduction 而是 resource reallocation。论文 Section 4.5 的讨论（\"trading approximately 3× more evaluations per item for 3× fewer items\"）比摘要更诚实。建议 abstract 采用 Section 4.5 的对称措辞。\n\n**[AGREE] R2-W2: Format-associated pattern 篇幅与统计支撑不匹配**\n\n同意，这与我的 W4 一致。Section 4.3 占约 1 页，但 permutation test p = 0.10（论文自认），benchmark-level CI 含零 [-1.7, 5.1]（Section 4.3）。对 n=5 benchmarks（3 MC + 2 FF）的分析，item-level effect size 虽然强 (d = 1.73)，benchmark-level 的 inferential value 很有限。论文已在 Section 4.3 标注 \"exploratory\" 和 \"descriptive observation\"，但 Table 3 和 Figure 3 的醒目呈现方式仍暗示 confirmatory finding。篇幅应与证据强度匹配。\n\n**[REBUT] R2-W3: Conclusion 过于简短**\n\n不完全同意。当前 Conclusion（约半页）覆盖了主要发现的摘要和 open-source 承诺。对于一篇正文 8 页限制的论文，Conclusion 的简短是正文空间管理的合理选择。更重要的 practical implications 实际上已分散在 Section 4.5（design-dependent budgets with adoption gradient）和 Appendix C（intermediate D-study designs, Table 9）。如果 R2 认为缺少的是 \"practitioners should do X\" 的具体指导，Table 9 的 adoption gradient（从 \"minimal upgrade\" 2p 到 \"standard\" 4p×4s×2t）已经提供了。但我同意 Conclusion 可以增加 1-2 句关于 practical adoption pathway 的总结。\n\n**[AGREE] R2-W4: Related Work 缺 evaluation harness 实现层面文献**\n\n部分同意。论文引用了 Sclar et al. (2024)、Pezeshkpour and Hruschka (2024) 等 formatting/ordering 文献，但未讨论 lm-eval-harness 等实际评测框架的实现选择（如默认 prompt template、scoring method、few-shot sampling）如何映射到本文的 facets。MMLU-Redux (Gema et al., 2025) 和 MMLU-Pro 也值得在 Related Work 中定位。不过这不影响方法论完整性，是 completeness 问题。\n\n**[AGREE] R2-W5: Model 样本时间同质性**\n\n同意，这与我的 W2 互补。8 个模型共享 2024-2025 instruction-tuning paradigm（Limitations section 承认），可能导致 model×item interaction patterns 的时间相关性。如果 2026 年的新一代模型（如 Llama-4, Qwen3.5）有显著不同的能力分布，当前的 variance structure 和 D-study budgets 可能不再适用。72B validation（Section 4.6）是同 family 内的 scale validation，无法排除 generation effect。\n\n---\n\n### Minor\n\n**[AGREE] R2-M1**: Abstract 数字密度确实高（G ≥ 0.80, 178 items, 1,602 evaluations, 3.1×, 552, 3×, etc.），对非专业读者不友好。\n\n**[AGREE] R2-M2**: Table 3 \"prompt\" 行含义不同（MC: prompt×item interaction; FF: prompt main effect）已在 caption 中说明，但行标签应更清晰区分。\n\n**[REBUT] R2-M3**: Appendix table 编号——我检查了 PDF（p.11-15），Tables 5-12 编号连续无跳跃，未发现问题。如果 R2 有具体的编号错误请指出。\n\n**[AGREE] R2-M4**: Section 4.4（Precision Separability）确实过短（约 4 行），但内容完整——BF16/FP16 functionally interchangeable under binary scoring, precision×temperature interaction 1.3% under text-exact-match。作为 negative result（precision 不需要控制），简短处理合理。\n\n**[AGREE] R2-M5**: Figure 1 y 轴字体偏小，PDF 中确实需要放大才能读取刻度值。\n\n---\n\n### Questions 回应\n\n**Q1 (IRT+G-theory workflow)**: 这是 Table 4 暗示的最优策略——先用 IRT 做 item selection（减少 item 数），再用 G-theory 做 protocol optimization（减少 per-item variance）。论文中 IRT 116 items + multi-facet G=0.895 vs. single-condition G=0.457 的对比（Table 4）直接支持这一 workflow。但论文未明确提出这个 two-stage pipeline，这是一个遗漏。\n\n**Q2 (LLM-as-judge extension)**: 论文未讨论。鉴于 binary scoring conditionality 如此显著（N2），LLM-as-judge continuous scoring 下的 variance structure 几乎肯定完全不同。这是一个重要的 future direction 但超出当前论文范围。\n\n**Q3 (Contamination detection)**: 论文在 Limitations 中讨论了 contamination（\"differential contamination across architectures could inflate model×item interaction\"），但未运行 contamination detection。论文提供了间接 evidence：consistent variance structures across three independently constructed MC benchmarks（MMLU, ARC, HellaSwag）。直接运行 contamination detection 将加强论文，但不是必需的。\n\n**Q4 (Cross-family 72B validation)**: 论文承认 72B validation 限于 Qwen2.5 family（Limitations）。这与我的 W2 和 R2 的 W5 一致——cross-family validation 是加强论文的最有效方式之一。\n\n---\n\n### 对 R2 Overall 评分的看法\n\nR2 给 3.5（Borderline Conference），我也给了 3.5。两份审稿的主要分歧在于：\n\n1. **N1 严重程度**：R2 认为 novelty 不足是 critical issue。我认为 R2 低估了 fully crossed multi-benchmark design 的贡献和 binary data adaptation 的非平凡性，建议将 N1 降为 should-fix。论文的定位可以改善但贡献是实质性的。\n\n2. **Soundness vs. Novelty 的权重**：R2 的主要顾虑是 novelty/excitement（Excitement 3/5），我的主要顾虑是 methodological completeness（D-study formula 不完整、binary bias 未量化）。两者指向不同的改进方向：R2 要求更强的方法论创新定位，我要求更严格的数学完整性。\n\n3. **共识区域**：binary scoring scope limitation（R2-N2 ≈ 我的 W3）、format-associated pattern 统计不足（R2-W2 ≈ 我的 W4）、model exchangeability（R2-W5 ≈ 我的 W2）。\n",
  "reviewer_id": "1",
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 对 Reviewer 2 意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[REBUT] R2-N1: 相对于 Messing (2026) TEE 的增量贡献定位**\n\nR2 的论点是三个扩展方向都是 incremental：facet 选择不同≠方法论不同、scale-up、教科书操作。我部分不同意。\n\n1. R2 低估了 **fully crossed multi-benchmark factorial design** 的方法论贡献。Messing (2026) 仅在 **单一 benchmark** 上 cross 了 5 个 methodology facets，且排除了 infrastructure facets（Section 2, Related Work: \"excluded infrastructure facets and cross-benchmark comparison\"）。本文 cross 7 facets across 5 benchmarks 不仅是 scale-up，更是第一次将 infrastructure facets（precision, seed）与 methodology facets（prompt, ordering）**同时纳入同一个 factorial design**。这使得 facet 间交互项（如 precision×item = 3.3%, Table 2 单模型分析）首次可被估计，揭示了 infrastructure 与 methodology 的相对贡献——这是 Messing (2026) 结构上无法回答的问题。\n\n2. 但 R2 关于 **IRT+G-theory 互补性被埋没** 的观察我完全赞同。Table 4 中 IRT 116 items 在 single-condition 下 G=0.457、multi-facet 下 G=0.895 的对比，证明了 item selection（IRT）和 protocol optimization（G-theory）是正交的——这是论文最具方法论洞察力的发现，但在 Section 4.5 中只用了约 3 行文字。应当提升至 Contributions。\n\n3. \"D-study projection = 教科书操作\" 的说法过于简化。标准 D-study 假设 continuous data；在 binary data 上进行 D-study 并通过 probit simulation、GLMM complement 和 null calibration 验证其有效性（Appendix A）需要非平凡的 methodological adaptation。\n\n**综合判断**：N1 的严重程度被 R2 高估。论文的贡献不是对 Messing (2026) 的 scale-up，而是在一个结构上更完整的设计中回答了不同的问题（infrastructure + methodology 的联合 variance structure + cross-benchmark generalization + actionable budgets）。但 IRT+G-theory 互补性的呈现确实需要加强。建议从 critical 降为 should-fix。\n\n---\n\n**[AGREE] R2-N2: Binary scoring conditionality 的 scope 限制**\n\n完全同意。这与我的 N2 互补。论文的核心发现高度依赖 binary scoring：\n- Text-exact-match: G 从 0.936 暴跌至 0.007（Section 4.1）\n- Partial-credit: G 从 0.76 降至 0.55，item ranking ρ = 0.26（Appendix A, Scoring metric sensitivity）\n- Section 3.5 明确承认 \"All findings in this paper are conditioned on binary correctness scoring\"\n\n但 title（\"Reproducibility Budgets for Open-Weight LLM Evaluation\"）和 abstract 首句（\"Large Language Model (LLM) evaluation results vary across reproductions\"）均暗示更广的适用性。实际上 D-study budgets **仅对 binary correctness scoring 有效**——这对使用 partial credit、LLM-as-judge、或 continuous metrics 的评测完全不适用。\n\nR2 建议 title 加 \"under Binary Scoring\" 是合理的，至少 abstract 首段应在第一处提及 D-study budget 时立即声明 scope。这确实影响接收决定，因为 framing 的广度与实际适用性之间的 gap 可能误导实践者。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: \"3.1× item reduction\" framing 掩盖 total evaluation 增长**\n\n同意。论文摘要中 \"a 3.1× reduction from 552 single-condition items\" 是 item 数的比较（552→178），但 total evaluations 从 552 增加到 1,602（178 × 9 conditions）——增长了 2.9×。这不是 reduction 而是 resource reallocation。论文 Section 4.5 的讨论（\"trading approximately 3× more evaluations per item for 3× fewer items\"）比摘要更诚实。建议 abstract 采用 Section 4.5 的对称措辞。\n\n**[AGREE] R2-W2: Format-associated pattern 篇幅与统计支撑不匹配**\n\n同意，这与我的 W4 一致。Section 4.3 占约 1 页，但 permutation test p = 0.10（论文自认），benchmark-level CI 含零 [-1.7, 5.1]（Section 4.3）。对 n=5 benchmarks（3 MC + 2 FF）的分析，item-level effect size 虽然强 (d = 1.73)，benchmark-level 的 inferential value 很有限。论文已在 Section 4.3 标注 \"exploratory\" 和 \"descriptive observation\"，但 Table 3 和 Figure 3 的醒目呈现方式仍暗示 confirmatory finding。篇幅应与证据强度匹配。\n\n**[REBUT] R2-W3: Conclusion 过于简短**\n\n不完全同意。当前 Conclusion（约半页）覆盖了主要发现的摘要和 open-source 承诺。对于一篇正文 8 页限制的论文，Conclusion 的简短是正文空间管理的合理选择。更重要的 practical implications 实际上已分散在 Section 4.5（design-dependent budgets with adoption gradient）和 Appendix C（intermediate D-study designs, Table 9）。如果 R2 认为缺少的是 \"practitioners should do X\" 的具体指导，Table 9 的 adoption gradient（从 \"minimal upgrade\" 2p 到 \"standard\" 4p×4s×2t）已经提供了。但我同意 Conclusion 可以增加 1-2 句关于 practical adoption pathway 的总结。\n\n**[AGREE] R2-W4: Related Work 缺 evaluation harness 实现层面文献**\n\n部分同意。论文引用了 Sclar et al. (2024)、Pezeshkpour and Hruschka (2024) 等 formatting/ordering 文献，但未讨论 lm-eval-harness 等实际评测框架的实现选择（如默认 prompt template、scoring method、few-shot sampling）如何映射到本文的 facets。MMLU-Redux (Gema et al., 2025) 和 MMLU-Pro 也值得在 Related Work 中定位。不过这不影响方法论完整性，是 completeness 问题。\n\n**[AGREE] R2-W5: Model 样本时间同质性**\n\n同意，这与我的 W2 互补。8 个模型共享 2024-2025 instruction-tuning paradigm（Limitations section 承认），可能导致 model×item interaction patterns 的时间相关性。如果 2026 年的新一代模型（如 Llama-4, Qwen3.5）有显著不同的能力分布，当前的 variance structure 和 D-study budgets 可能不再适用。72B validation（Section 4.6）是同 family 内的 scale validation，无法排除 generation effect。\n\n---\n\n### Minor\n\n**[AGREE] R2-M1**: Abstract 数字密度确实高（G ≥ 0.80, 178 items, 1,602 evaluations, 3.1×, 552, 3×, etc.），对非专业读者不友好。\n\n**[AGREE] R2-M2**: Table 3 \"prompt\" 行含义不同（MC: prompt×item interaction; FF: prompt main effect）已在 caption 中说明，但行标签应更清晰区分。\n\n**[REBUT] R2-M3**: Appendix table 编号——我检查了 PDF（p.11-15），Tables 5-12 编号连续无跳跃，未发现问题。如果 R2 有具体的编号错误请指出。\n\n**[AGREE] R2-M4**: Section 4.4（Precision Separability）确实过短（约 4 行），但内容完整——BF16/FP16 functionally interchangeable under binary scoring, precision×temperature interaction 1.3% under text-exact-match。作为 negative result（precision 不需要控制），简短处理合理。\n\n**[AGREE] R2-M5**: Figure 1 y 轴字体偏小，PDF 中确实需要放大才能读取刻度值。\n\n---\n\n### Questions 回应\n\n**Q1 (IRT+G-theory workflow)**: 这是 Table 4 暗示的最优策略——先用 IRT 做 item selection（减少 item 数），再用 G-theory 做 protocol optimization（减少 per-item variance）。论文中 IRT 116 items + multi-facet G=0.895 vs. single-condition G=0.457 的对比（Table 4）直接支持这一 workflow。但论文未明确提出这个 two-stage pipeline，这是一个遗漏。\n\n**Q2 (LLM-as-judge extension)**: 论文未讨论。鉴于 binary scoring conditionality 如此显著（N2），LLM-as-judge continuous scoring 下的 variance structure 几乎肯定完全不同。这是一个重要的 future direction 但超出当前论文范围。\n\n**Q3 (Contamination detection)**: 论文在 Limitations 中讨论了 contamination（\"differential contamination across architectures could inflate model×item interaction\"），但未运行 contamination detection。论文提供了间接 evidence：consistent variance structures across three independently constructed MC benchmarks（MMLU, ARC, HellaSwag）。直接运行 contamination detection 将加强论文，但不是必需的。\n\n**Q4 (Cross-family 72B validation)**: 论文承认 72B validation 限于 Qwen2.5 family（Limitations）。这与我的 W2 和 R2 的 W5 一致——cross-family validation 是加强论文的最有效方式之一。\n\n---\n\n### 对 R2 Overall 评分的看法\n\nR2 给 3.5（Borderline Conference），我也给了 3.5。两份审稿的主要分歧在于：\n\n1. **N1 严重程度**：R2 认为 novelty 不足是 critical issue。我认为 R2 低估了 fully crossed multi-benchmark design 的贡献和 binary data adaptation 的非平凡性，建议将 N1 降为 should-fix。论文的定位可以改善但贡献是实质性的。\n\n2. **Soundness vs. Novelty 的权重**：R2 的主要顾虑是 novelty/excitement（Excitement 3/5），我的主要顾虑是 methodological completeness（D-study formula 不完整、binary bias 未量化）。两者指向不同的改进方向：R2 要求更强的方法论创新定位，我要求更严格的数学完整性。\n\n3. **共识区域**：binary scoring scope limitation（R2-N2 ≈ 我的 W3）、format-associated pattern 统计不足（R2-W2 ≈ 我的 W4）、model exchangeability（R2-W5 ≈ 我的 W2）。\n",
    "reviewer_id": "1",
    "project": "nlp_variance_gtheory"
  }
}
```

</details>

---


### Tool result

_source line 665 · 2026-05-23T02:48:11.976705+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_265de443abfe4594f91451b075b582ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3614
}
```

</details>

---


### Assistant

_source line 666 · 2026-05-23T02:48:19.162711+00:00_

交叉回应已提交。

核心判断：
- R2-N1（novelty 不足）严重程度被高估，建议降为 should-fix——论文的 fully crossed multi-benchmark design 和 binary data adaptation 是实质性贡献，非简单 scale-up
- R2-N2（binary scope）完全同意，与我的审稿意见互补
- 两份审稿的主要共识：binary scoring limitation、format pattern 统计不足、model exchangeability；主要分歧：R2 侧重 novelty concern，我侧重 mathematical completeness（D-study formula、binary bias quantification）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1"
}
```

</details>

---


## Round 21

## Round 21

62 recorded events


### User

_source line 667 · 2026-05-25T21:18:35.813645+00:00_

[Round 11 审稿请求]:
你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 的审查。

## Venue 信息
- **目标会议**: EMNLP 2026（通过 ARR 统一审稿）
- **ARR 投稿截止**: 2026-05-25
- **页数限制**: Long paper, 正文 8 页，参考文献不限，Limitations 不计入页数
- **模板**: ACL (review option)
- **匿名规则**: Double-blind
- **附录**: 允许，不计入页数，但不应过度使用

## 论文路径
- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/submitted.pdf`

## 你的审查侧重

请重点审查以下方面：

1. **G-theory 技术正确性**：Henderson Method I 应用于 binary data 的合理性、方差分量估计的无偏性论证、G-coefficient 和 D-study 公式推导是否完整可验证
2. **Binary data 假设**：所有发现均基于 binary scoring，probit simulation (ρ=0.732) 的验证强度、partial-credit (GSM8K G: 0.86→0.77) 的影响是否充分讨论、text-exact-match (G: 0.936→0.007) 的 implication
3. **D-study projection 假设**：方差分量不变性假设（跨 item pool、跨模型、跨时间）的合理性、forward prediction 验证 (Table 8) 的局限性、budget 推荐的外推适用范围
4. **模型作为 quasi-random facet**：8 个 purposively selected 模型作为 random facet 的辩护是否充分、LOMO 和 four-model subset 作为 within-sample 稳定性检验 vs. out-of-sample 泛化、model×item interaction 的可交换性假设
5. **统计声明**：format-associated pattern (n=5, p=0.10) 的统计功效和叙事权重、bootstrap CI 仅 item-level 未含 model-level uncertainty、所有效应量和置信区间的报告完整性
6. **实验设计**：factorial design 的 reduced crossing (exp-002 仅 BF16, 2 temperatures) 是否引入 confound、ordering 仅 MMLU 的非对称性、200 items stratified sampling 的代表性

## Overall Assessment 评分标准 (EMNLP 2026 ARR)
5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit

请严格按照以下结构输出审稿意见：
- **Summary** (2-3 句)
- **Strengths** (逐条列出，标注 S1, S2, ...)
- **Weaknesses** (逐条列出，标注 W1, W2, ...，分为 Must-Fix / Should-Fix / Minor)
- **Questions** (Q1, Q2, ...)
- **Missing References**
- **Overall Assessment** (评分 + 置信度 + 理由)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 668 · 2026-05-25T21:18:45.812291+00:00_

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
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
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

_source line 669 · 2026-05-25T21:18:45.862989+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 670 · 2026-05-25T21:18:49.784524+00:00_

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
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 671 · 2026-05-25T21:18:50.687844+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/submitted.pdf",
  "pages": "1-8",
  "project": "nlp_variance_gtheory",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/submitted.pdf",
    "pages": "1-8",
    "project": "nlp_variance_gtheory",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 672 · 2026-05-25T21:18:56.258504+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Overall Recommendation Scores

A score of 5 means "Consider for Award" - the reviewer thinks the paper could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers). Other recommendation levels include:

- 2 = Resubmit next cycle: substantial revis
…[truncated 750 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6473
}
```

</details>

---


### Tool result

_source line 673 · 2026-05-25T21:18:57.921715+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 461.1}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 756.3}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.6}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 491.2}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.9}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 436.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 404.0}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.8}], \"total_pages\": 15, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images\"}, \"error\": null, \"met
…[truncated 14 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7233
}
```

</details>

---


### Tool call

_source line 674 · 2026-05-25T21:19:02.294576+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review review form soundness excitement scoring 1-5 scale 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review review form soundness excitement scoring 1-5 scale 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 675 · 2026-05-25T21:19:02.746563+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 676 · 2026-05-25T21:19:03.651775+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 677 · 2026-05-25T21:19:03.702404+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 678 · 2026-05-25T21:19:04.154670+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 679 · 2026-05-25T21:19:04.458358+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 755
}
```

</details>

---


### Tool call

_source line 680 · 2026-05-25T21:19:04.712569+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 681 · 2026-05-25T21:19:04.864217+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 709
}
```

</details>

---


### Tool result

_source line 682 · 2026-05-25T21:19:05.366097+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 653
}
```

</details>

---


### Tool result

_source line 683 · 2026-05-25T21:19:12.647222+00:00_

Web search results for query: "ACL Rolling Review review form soundness excitement scoring 1-5 scale 2025 2026"

Links: [{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"},{"title":"Program Chairs’ Report on Peer Review at ACL 2023 Anna Rogers}","url":"https://aclanthology.org/2023.acl-long.report.pdf"},{"title":"ACL’23 Peer Review Form - ACL 2023","url":"https://2023.aclweb.org/blog/review-form/"},{"title":"ACL’23 Peer Review Policies - ACL 2023","url":"https://2023.aclweb.org/blog/review-acl23/"},{"title":"ACL 2026 on X: \"Checkout the blog post on the soundness/excitement scores https://t.co/AKSO9DjiYP . It clarifies the reasoning behind the separation of overall scores and how it might make the reviewer recommendation more robust. #ACL2023Toronto #ACL2023NLP #NLProc\" / X","url":"https://x.com/aclmeeting/status/1637827267173953540"}]

Based on the search results, here's what I found about the ACL Rolling Review (ARR) review form scoring system:

## Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness Score

The soundness score uses a 1-5 scale and evaluates technical merit. A score of 1 means "Major Issues: This study is not yet sufficiently thorough to warrant publication or is not relevant to ACL." Higher scores indicate stronger technical quality, with 5 repres
…[truncated 914 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 10352
}
```

</details>

---


### Tool call

_source line 684 · 2026-05-25T21:19:17.889010+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 685 · 2026-05-25T21:19:18.463599+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 686 · 2026-05-25T21:19:19.378435+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1489
}
```

</details>

---


### Tool result

_source line 687 · 2026-05-25T21:19:19.381558+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 917
}
```

</details>

---


### Tool call

_source line 688 · 2026-05-25T21:19:19.381969+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 689 · 2026-05-25T21:19:19.584662+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 690 · 2026-05-25T21:19:19.838557+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 456
}
```

</details>

---


### Tool result

_source line 691 · 2026-05-25T21:19:20.343004+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 758
}
```

</details>

---


### Tool call

_source line 692 · 2026-05-25T21:19:26.877536+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/submitted.pdf",
  "pages": "9-15",
  "project": "nlp_variance_gtheory",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/submitted.pdf",
    "pages": "9-15",
    "project": "nlp_variance_gtheory",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 693 · 2026-05-25T21:19:27.630848+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 577.2}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 572.8}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 542.1}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 454.6}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 496.6}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 431.3}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 67.5}], \"total_pages\": 15, \"rendered_pages\": 7, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 694 · 2026-05-25T21:19:30.946921+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 695 · 2026-05-25T21:19:31.856262+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 696 · 2026-05-25T21:19:32.360270+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1413
}
```

</details>

---


### Tool call

_source line 697 · 2026-05-25T21:19:32.360733+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 698 · 2026-05-25T21:19:32.715247+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 699 · 2026-05-25T21:19:32.920764+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1064
}
```

</details>

---


### Tool result

_source line 700 · 2026-05-25T21:19:34.479728+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2118
}
```

</details>

---


### Tool result

_source line 701 · 2026-05-25T21:19:34.634128+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1918
}
```

</details>

---


### Tool call

_source line 702 · 2026-05-25T21:19:41.513401+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 703 · 2026-05-25T21:19:42.468350+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 704 · 2026-05-25T21:19:42.469063+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 705 · 2026-05-25T21:19:42.821821+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 706 · 2026-05-25T21:19:42.923830+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Tool result

_source line 707 · 2026-05-25T21:19:43.025196+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 556
}
```

</details>

---


### Tool call

_source line 708 · 2026-05-25T21:19:58.117553+00:00_

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
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
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

_source line 709 · 2026-05-25T21:19:58.218282+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 710 · 2026-05-25T21:20:03.090228+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include soundness, excitement, overall assessment, confidence, and any other dimensions. List each dimension with its full scale description."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include soundness, excitement, overall assessment, confidence, and any other dimensions. List each dimension with its full scale description."
  }
}
```

</details>

---


### Tool result

_source line 711 · 2026-05-25T21:20:09.064259+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- "5 = Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- 4 = Quite sure with unlikely but conceivable missed items
- 3 = Pretty sure, but chance of missed details
- 2 = Willing to defend evaluation, but likely missed details
- "1 = Not my area, or paper is very hard to understand"

## 2. **Soundness**
Scale: 1-5 (with .5 increments)
- "5 = Excellent: This study is one of the most thorough I have seen"
- 4 = Strong with sufficient claim support
- 3 = Acceptable with main claims supported
- 2 = Poor with insufficiently supported main claims
- "1 = Major Issues: This study is not yet sufficiently thorough to warrant publication"

## 3. **Excitement**
Scale: 1-5 (with .5 increments)
- 5 = Would recommend to others and attend presentation
- 4 = Would mention to others; effort to attend
- 3 = Might mention points; attend if time permits
- 2 = Does not resonate personally but might interest community
- "1 = Not Exciting: this paper does not resonate with me"

## 4. **Overall Assessment**
Scale: 1-5 (with .5 increments)
- 5 = Consider for Award (top 2.5%)
- 4 = Conference acceptance
- 3 = Findings acceptance
- 2 = Resubmit next cycle
- 1 = Do not resubmit

## 5. **Reproducibility**
Scale: 1-5
- 5 = Results easily reproducible
- 4 = Mostly reproducible with minor variation
- 3 = Reproducible with difficulty
- 2 = Hard to reproduce; limited data availability
- 1 = Cannot reproduce

## 6. **Datasets & Software**
Each scales 1-5
- 5 = Enabling impact on research choices
- 4 = Useful for ongoing work
- 3 = Potentially useful
- 2 = Documentary value only
- 1 = None released

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5974
}
```

</details>

---


### Tool call

_source line 712 · 2026-05-25T21:21:12.505543+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 713 · 2026-05-25T21:21:12.606262+00:00_

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
11	
12	\usepackage{graphicx}
13	\usepackage{amsmath,amssymb}
14	\usepackage{booktabs}
15	\usepackage{multirow}
16	
17	\graphicspath{{../../figures/paper/}}
18	
19	\title{Reproducibility Budgets for Open-Weight LLM Evaluation:\\A Generalizability Theory Study of 7--9B Instruction-Tuned Models}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\begin{abstract}
27	\input{abstract}
28	\end{abstract}
29	
30	% === INTRODUCTION ===
31	\input{introduction}
32	
33	% === RELATED WORK ===
34	\input{related_work}
35	
36	% === METHOD ===
37	\input{method}
38	
39	% === EXPERIMENTS ===
40	\input{experiments}
41	
42	% === CONCLUSION ===
43	\enlargethispage{1\baselineskip}
44	\input{conclusion}
45	
46	% === LIMITATIONS ===
47	\input{limitations}
48	
49	\bibliography{references}
50	
51	% === APPENDIX ===
52	\input{appendix}
53	
54	\end{document}
55	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 714 · 2026-05-25T21:21:17.225848+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 715 · 2026-05-25T21:21:17.377549+00:00_

1	\section{Method and Experimental Design}
2	\label{sec:method}
3	
4	\subsection{Generalizability Theory}
5	\label{sec:gtheory}
6	
7	Generalizability theory (G-theory) treats each measurement as one observation from a universe of admissible conditions defined by the crossed facets of an evaluation design \cite{shavelson1991generalizability, brennan2001generalizability}. The \emph{object of measurement} is the entity whose consistency is of interest. In our setting, test items ($p$) serve as the object of measurement, and the goal is to determine how reliably item-level scores generalize across the methodological conditions under which they are collected.
8	
9	A \emph{G-study} decomposes total observed variance into components $\sigma^2_x$ for each facet $x$ and their interactions. Each component quantifies how much variability that source contributes to the overall measurement. Large interaction components (e.g., $\sigma^2_{pM}$ for item-by-model) indicate that facets do not affect items uniformly but instead create differential difficulty profiles. We estimate variance components via Henderson Method~I, an unbiased ANOVA-based estimator for balanced designs \cite[Ch.~3]{brennan2001generalizability}, with 1,000-resample bootstrap confidence intervals \cite{efron1993bootstrap} (item-level resampling with replacement, preserving the fully-crossed structure across all other facets) \cite{li2023bootstrap}.
10	
11	A \emph{D-study} projects the generalizability coefficient under hypothetical designs with different numbers of conditions per facet:
12	\begin{equation}
13	G_\text{item} = \frac{\sigma^2_p}{\sigma^2_p + \sigma^2_\text{rel}}
14	\label{eq:gcoeff}
15	\end{equation}
16	where $\sigma^2_\text{rel} = \sum_i \sigma^2_{p \times f_i} / n_{f_i} + \sigma^2_\text{residual} / \prod_i n_{f_i}$ aggregates all item-by-facet interaction variances, each divided by the number of conditions for the corresponding facets \cite[Ch.~4]{brennan2001generalizability}. A D-study projects 
…[truncated 8181 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 716 · 2026-05-25T21:21:17.428254+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 717 · 2026-05-25T21:21:17.493579+00:00_

1	\section{Experiments}
2	
3	All experiments use open-weight 7--9B parameter models evaluated with vLLM~0.9.2 on a single NVIDIA RTX PRO 6000 GPU (96GB) with binary correctness scoring.
4	
5	\subsection{Single-Model Baseline}
6	\label{sec:single_model}
7	
8	\begin{figure}[t]
9	\centering
10	\includegraphics[width=\columnwidth]{fig_single_model_variance}
11	\caption{Single-model variance decomposition (Llama-3.1-8B, MMLU). Item difficulty dominates (58.4\%); all main facet effects are $<$1\%. Item-conditional interactions total 17.2\%.}
12	\label{fig:single_model_var}
13	\end{figure}
14	
15	\paragraph{Design.} The G-study crosses six facets: 200 items $\times$ 3 numerical precisions (BF16, FP16, FP32) $\times$ 6 prompt templates $\times$ 6 random seeds $\times$ 3 temperature levels (0.0, 0.3, 0.7) $\times$ 4 answer orderings, yielding 259,200 binary observations. Variance components are estimated via Henderson Method~I with bootstrap confidence intervals (1,000 resamples).
16	
17	\paragraph{Results.} Item difficulty dominates at 58.4\%, with residual at 23.1\% (Figure~\ref{fig:single_model_var}). All main facet effects are negligible ($<$1\% each); the interesting structure is in item-conditional interactions (17.2\% total), where prompt$\times$item (5.5\%) is largest. The generalizability coefficient $G_\text{item} = 0.936$ (Eq.~\ref{eq:gcoeff}); D-study projection (Eq.~\ref{eq:dstudy}) gives $G \geq 0.80$ with 55 items.
18	
19	For text-exact-match scoring, temperature dominates at 79.7\% and $G_\text{item}$ collapses to 0.007, motivating our exclusive use of binary correctness.
20	
21	\subsection{Cross-Model Variance}
22	
23	Extending to eight models (BF16 subset, 460,800 records), Table~\ref{tab:cross_model} shows that item difficulty drops from 58.4\% to 37.9\%, while model$\times$item interaction emerges at 30.2\% (up to 36\% in MC benchmarks, 15--17\% in FF; \S\ref{sec:format_conditional}). The model main effect is 3--5\% (MC) and 9--11\% (FF)\footnote{Ranges r
…[truncated 12273 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 65
}
```

</details>

---


### Tool call

_source line 718 · 2026-05-25T21:21:24.292957+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 719 · 2026-05-25T21:21:24.343532+00:00_

1	\section*{Limitations}
2	
3	Our design covers eight 7--9B instruction-tuned models; preliminary 72B validation confirms consistent variance structure, but broader scale and temporal coverage is needed. The benchmark sample ($n = 5$) limits statistical power for format-associated observations ($p = 0.10$). All D-study budgets assume binary scoring; partial-credit analysis on GSM8K shows $G$ drops from 0.86 to 0.77, suggesting limited transferability to finer-grained rubrics. Benchmark contamination in pretraining data may inflate item accuracy and compress variance; our design does not control for this source.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 720 · 2026-05-25T21:21:24.394189+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 721 · 2026-05-25T21:21:24.494910+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	The dominant non-residual variance source in LLM evaluation is the model$\times$item interaction (30--36\% in MC, 15--17\% in FF), revealing that models disagree on which items are difficult rather than differing uniformly in overall ability. Multi-facet evaluation designs absorb this interaction: a 3-prompt $\times$ 3-seed protocol achieves $G \geq 0.80$ with 178 MMLU items versus 552 under single-condition, with cross-benchmark budgets of 93--128 items. The variance structure is format-dependent: MC benchmarks concentrate 68--72\% in item-related components while FF benchmarks disperse to 31--41\%, motivating per-format budget calibration. We recommend three practices: adopt multi-facet designs for published results, report item-level accuracy to expose model$\times$item interaction, and calibrate item budgets per benchmark format.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 722 · 2026-05-25T21:21:24.495343+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 723 · 2026-05-25T21:21:24.596107+00:00_

1	\appendix
2	
3	\section{Additional Robustness Analyses}
4	\label{app:robustness}
5	
6	We report nine robustness analyses that verify the stability of the variance decomposition under alternative analytical choices.
7	
8	\paragraph{GLMM complement.} A generalized linear mixed model (GLMM) with marginal logit link produces variance component rankings that perfectly preserve all seven grouped component orderings ($\rho = 1.0$) relative to Henderson Method~I \cite{jiang2018bayesian, tuerlinckx2006glmm}. This confirms that the linear variance decomposition is robust to the binary outcome distribution.
9	
10	\paragraph{Accuracy-range stability.} The \texttt{item\_id} variance share remains stable across subsets with mean accuracy from 0.62 to 0.72 ($r = -0.048$). This rules out distortion from binary floor or ceiling effects at observed accuracy levels.
11	
12	\paragraph{Estimator robustness.} We compare Henderson Method~I with restricted maximum likelihood (REML-EM, 500 iterations, practical convergence $\Delta < 0.003$ percentage points). All variance components differ by $<$0.5 percentage points between estimators. The largest discrepancy occurs on the residual component (0.47pp); all substantive components (item, model$\times$item, model) differ by $<$0.3pp. Henderson Method~I is preferred for our balanced designs because it produces unbiased estimates without distributional assumptions \cite[Ch.~12]{brennan2001generalizability}.
13	
14	\paragraph{Probit simulation.} A probit simulation matched to our 1,296-condition design confirms that Henderson Method~I recovers variance component rankings from dichotomized data (Spearman $\rho = 0.732$ between binary and continuous rankings, excluding residual; \texttt{item\_id} dominant in all 100 replications; top-5 ordering correct in 79\% of replications). Bias analysis by difficulty stratum shows $|\text{bias}| = 0.28$--$0.37$ for items with $p \in [0.5, 0.8]$, where the Bernoulli variance ceiling $p(1{-}p)$ is largest. Thi
…[truncated 21784 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 724 · 2026-05-25T21:26:06.823741+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 审稿意见 — 方法严谨性 + 实验设计\n\n## Summary\n\n本文将教育测量领域的概化理论（G-theory）引入LLM评估，通过Henderson Method I对8个7-9B开源模型在5个基准上约230万条二值记录进行方差分量分解，发现model×item交互是主要的非残差方差来源（MC 30-36%, FF 15-17%），并据此通过D-study投影给出可复现性预算建议（3-prompt × 3-seed设计将MMLU所需题目从552降至178）。这是G-theory在NLP评估领域的首次完整应用（含D-study投影），方法论框架扎实，实验规模大，且附有9项稳健性检验。主要关切集中在：格式关联模式的统计功效不足但在结论中被过度声称、Bootstrap CI仅捕获item层不确定性、以及二值评分限定下的实用范围偏窄。\n\n## Strengths\n\n**S1** [方法新颖性] 首次将G-theory的完整工作流（G-study方差分解 + D-study预算投影）系统应用于LLM评估，填补了已有工作（Bouthillier et al., 2021; Messing, 2026）在D-study投影和跨格式比较方面的空白（Table 1, Section 2清晰定位了贡献）。\n\n**S2** [实验规模与设计] 7 facet × 8 model × 5 benchmark的全因子/准全因子设计（exp-001: 460,800 records fully crossed on MMLU; exp-002: 2,304,000 records across 5 benchmarks）是该领域迄今最大规模的多面交叉方差分析。设计矩阵（Table 2）清晰、可复现。\n\n**S3** [稳健性检验充分] Appendix A提供9项独立稳健性分析（GLMM ρ=1.0、REML差异<0.5pp、probit simulation、null calibration ratio=1.0008、LOMO max|ΔG|=0.030、accuracy-range stability r=-0.048、CI方法对比、facet specification sensitivity、reduced crossing validation ΔG=0.0008），系统覆盖了估计方法、数据分布、样本稳定性等多个角度。\n\n**S4** [核心发现的洞察力] model×item交互主导（Section 4.2, Table 5）是一个非直觉但重要的发现：模型主要在\"哪些题目难\"上分歧，而非在整体能力上分歧。MMLU学科粒度分析（Table 12, Appendix E）进一步验证了这一机制在knowledge vs. reasoning维度上的梯度变化（G_item从0.614到0.930）。\n\n**S5** [实用产出] 开源G-theory pipeline和D-study calculator具有直接实用价值；Table 7-9的预算建议为benchmark开发者提供了可操作的参考。IRT与G-theory正交互补的论证（Table 7, Zhou et al. 2026的116题在multi-facet下G从0.457升至0.895）也有启发性。\n\n**S6** [Binary data处理的透明度] Section 3.5明确标注了binary scoring假设，probit simulation量化了binarization的代价（D-study预算+36%），partial-credit对比（GSM8K G: 0.86→0.77）和text-exact-match对比（G: 0.936→0.007）展示了metric conditionality的严重程度。这种透明度值得肯定。\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1** [critical] 格式关联模式在结论中被过度声称\n\n- 具体位置：Section 4.3（标题含\"Exploratory\"）vs. Section 5 Conclusion vs. Abstract\n- 问题：Section 4.3明确将MC/FF方差结构差异标记为\"exploratory\"和\"descriptive observation\"（permutation p=0.10, n=5 benchmarks, benchmark-level CI spans zero），但Section 5 Conclusion写道\"The variance structure is format-dependent: MC benchmarks concentrate 68-72%...motivating per-format budget calibration\"，完全去掉了\"exploratory\"限定词。Abstract虽未直接声称format-dependent，但第2页Contribution 3写\"Format-associated variance patterns (exploratory)\"后，后续Table 9的预算建议已按MC/FF分开给出，实际上将这一探索性发现当作已建立的结论用于实践推荐。\n- 为什么影响接收：在n=5（3 MC + 2 FF）、p=0.10的统计功效下，从descriptive observation升级为prescriptive budget separation，违反了统计推断的基本审慎原则。一位Area Chair可能仅读Conclusion而形成错误印象。\n- 建议修改方向：(1) Conclusion中保留\"exploratory/preliminary\"限定词；(2) Table 9的MC/FF分列可保留但需加注\"based on n=5 benchmarks; format-specific calibration requires replication with a larger benchmark sample\"；(3) 或提供per-benchmark budgets而非per-format budgets，避免跨越归纳推断的边界。\n\n**W2** [critical] Bootstrap CI仅捕获item-level不确定性，D-study预算的置信区间被低估\n\n- 具体位置：Table 9 (95% CI columns), Appendix A CI method comparison\n- 问题：论文明确承认\"Bootstrap CIs capture item-sampling variability conditional on these 8 specific models; model-level stability is assessed separately via LOMO\"（Appendix A）。但Table 9报告的95% CI（如MMLU: [76, 116] items）仅反映item-level resampling。LOMO分析显示max|ΔG|=0.030，对应~23%的预算变化（Figure 9），但这一model-level不确定性从未与item-level CI联合量化。读者看到Table 9的CI会误认为它是总不确定性的度量。\n- 为什么影响接收：D-study预算是本文最核心的实用产出。如果其CI被系统性低估，所有基于Table 9的实践建议（\"93-128 items for G≥0.80\"）的可靠性都受到质疑。\n- 建议修改方向：(1) 在Table 9标题或脚注中明确标注CI仅反映item-level sampling variability；(2) 提供联合item+model uncertainty的估计（如将LOMO的|ΔG|范围叠加到bootstrap CI上）；(3) 或至少在正文中讨论combined uncertainty的量级（item CI ~20% + model uncertainty ~23% → 总不确定性可能在30-35%量级）。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W3** [warning] Model作为quasi-random facet的辩护链不完整\n\n- 具体位置：Section 3.6, Appendix A LOMO analysis\n- 问题：8个purposively selected模型被当作random facet，引用Meredith (1993)和Putnick & Barneeon (2016)，但这两篇文献是关于measurement invariance检验方法论的，并非关于justifying random-facet treatment for purposive samples。LOMO和four-model subset（Table 11: MC |ΔG|≤0.029, FF |ΔG|≤0.065）是within-sample stability checks，不等于out-of-sample generalization evidence。特别是FF的7.3% error（MATH, Table 11）意味着从4个模型预测8个模型的方差结构存在非 trivial的偏差。\n- 论文确实提供了\"treating models as random is more conservative\"的论证（G_random < G_fixed by 0.077-0.113，Table 10），这部分论证是有效的——如果模型实际上是固定的，那么random specification给出的是保守估计。但核心问题不在于random vs. fixed specification，而在于：从这8个特定模型估计的方差分量是否代表更广泛的7-9B模型宇宙？\n- 建议：(1) 更准确地引用G-theory文献中关于facet sampling的讨论（如Brennan, 2001, Ch. 5关于random vs. fixed facets的讨论）；(2) 明确讨论\"exchangeability within the target universe\"假设的可检验条件和局限；(3) 对FF benchmarks的较大预测偏差（7%）进行单独讨论。\n\n**W4** [warning] D-study投影的时间不变性假设未被充分讨论\n\n- 具体位置：Section 4.5最后一段 \"All projections assume the 2024-2025 model generation\"\n- 问题：D-study预算建议的实用性依赖于方差分量在时间上的稳定性。但LLM模型架构、训练数据和能力水平变化极快（2024到2025已经有significant shifts），论文仅以一句话带过这一关键假设。Scale validation（Section 4.6: Qwen2.5-72B, Llama-3.1-70B）提供了size维度的初步证据，但没有temporal维度的证据。\n- 建议：增加一段讨论方差分量temporal stability的分析。如果无法获得2025-2026模型的数据，至少应讨论哪些方差分量最可能随模型代际变化（如model×item interaction是否会随模型同质化而降低？）以及这对预算建议的影响方向。\n\n**W5** [warning] Partial-credit scoring的影响被低估\n\n- 具体位置：Section 3.5, Limitations, Appendix A Scoring metric sensitivity\n- 问题：GSM8K partial-credit G从0.86降至0.77（ΔG=-0.135），这一降幅超过了许多在论文中被详细讨论的其他效应。48.1%的incorrect responses有正确的中间步骤但错误的问题理解（Appendix A），这意味着binary scoring系统性地丢失了大量评估信息。然而，D-study预算建议（Table 9）完全基于binary scoring，而现实中越来越多的LLM评估采用partial-credit或连续评分（如GSM8K的step-level、MT-Bench的1-10评分）。\n- 建议：(1) 在正文（而非仅附录和Limitations）中更prominently讨论partial-credit的影响；(2) 至少对GSM8K给出partial-credit条件下的D-study预算以供对比；(3) 讨论binary→partial-credit transition对model×item interaction dominance结论的影响。\n\n**W6** [warning] Object of measurement的选择及其对实用性的影响未被讨论\n\n- 具体位置：Section 3.1\n- 问题：论文选择items作为object of measurement，G_item衡量的是\"item-level scores在不同条件下的泛化性\"。但LLM评估的主要用户关心的是model-level reliability（\"我的模型排名在不同评估条件下是否稳定？\"）。论文虽然间接地通过model×item interaction暗示了model-level的不可靠性，但从未直接量化model-level generalizability（将model作为object of measurement的G-study）。\n- 建议：至少在Discussion或Limitations中解释为什么选择items而非models作为object of measurement，以及两种选择下的G-coefficient有何关系。如可能，补充一个model作为object的G-study结果作为对照。\n\n### Minor（不影响接收）\n\n**M1** exp-002仅使用BF16精度和2个温度（0.0, 0.7），虽然Appendix A的reduced crossing validation显示ΔG=0.0008（在MMLU上），但这一验证仅基于MMLU——对于其他4个benchmark，precision×benchmark交互效应无法从数据中检验。建议在Appendix中加注这一局限。\n\n**M2** Abstract第一句\"up to 79 percentage points\"引用的是prior literature（Sclar et al., 2024等）的极端案例，非本研究发现。建议clarify这是\"prior work has shown\"而非本文的结果，避免在abstract中引发预期偏差。\n\n**M3** \"quasi-random facet\"不是G-theory标准术语（Brennan, 2001; Shavelson and Webb, 1991均使用\"random\"和\"fixed\"）。建议改用\"treated as random for the purpose of generalizability analysis\"或直接引用Brennan (2001, Ch. 5)关于facet universe definition的讨论。\n\n**M4** Benchmark contamination在Limitations中被提及但机制未讨论：如果部分item被contamination使得所有模型均答对，则这些item的model×item interaction为零，可能系统性地低估了model×item在clean benchmarks上的比例。值得一提。\n\n## Questions\n\n**Q1** Table 9的cross-model budgets假设n_M=8（8个模型同时评估）。如果用户仅评估1个模型，D-study预算应如何调整？请提供single-model cross-benchmark budgets（即将Table 7的方法应用到5个benchmark上）以增强实用性。\n\n**Q2** Probit simulation的ρ=0.732（excluding residual）意味着binary和continuous排名之间有约27%的rank discordance。论文论证\"qualitative ordering is preserved\"（top-5 correct in 79% of replications），但这是否足够精确以支持D-study budget projections中的quantitative claims（如\"178 items for G≥0.80\"）？\n\n**Q3** Scale validation（Section 4.6）仅覆盖Qwen和Llama家族，均已在main study中出现。是否有任何来自MoE架构或其他训练范式模型的证据？\n\n**Q4** Ordering facet在非MMLU benchmarks上σ²=0——这是因为ordering操作被执行但无效果，还是因为ordering操作未被应用到其他benchmark？请在正文中澄清。\n\n## Missing References\n\n- Cronbach, L. J., Gleser, G. C., Nanda, H., & Rajaratnam, N. (1972). *The Dependability of Behavioral Measurements*. Wiley. — G-theory的奠基文献，论文仅引用了Shavelson and Webb (1991)和Brennan (2001)作为G-theory来源，缺少对原始文献的致敬。\n- Webb, N. M., Shavelson, R. J., & Haertel, E. H. (2006). \"Reliability coefficients and generalizability theory.\" *Handbook of Statistics*, 26, 81-124. — 关于G-theory在non-standard data（包括binary）上应用的综述讨论。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | Henderson Method I的技术应用基本正确，robustness checks充分（9项），但format pattern overclaim（W1）和CI underestimation（W2）是实质性方法论问题 |\n| Excitement | 3.5/5 | G-theory→LLM evaluation的框架迁移具有新颖性，model×item interaction发现有洞察力，但binary-only限定和n=5 benchmark的format分析限制了impact |\n| Reproducibility | 4/5 | 开源pipeline、详细的设计矩阵、完整的prompt templates（Appendix G）、模型ID（Appendix G）、统计方法描述充分；缺少的是raw data和具体采样种子 |\n| Overall Assessment | **3.5** (Borderline Conference) |\n| Confidence | 4/5 | 熟悉G-theory和LLM evaluation两个领域，仔细阅读了论文及全部附录 |\n\n## Overall Assessment 理由\n\n本文在方法论框架、实验规模和稳健性检验方面达到了高标准，核心发现（model×item interaction dominance + D-study budgets）具有实用价值和理论启发性。将其评为Borderline Conference (3.5)而非Conference (4.0)的主要原因是两个方法论问题的叠加：(1) format-associated pattern从\"exploratory\"到Conclusion中的\"established\"的不当升级，以及(2) D-study预算的CI系统性低估（仅item-level，未含model-level uncertainty）。这两个问题均可在修改中解决（W1可通过调整措辞和添加注释修复，W2可通过报告联合不确定性修复），但在当前版本中它们共同影响了论文的statistical rigor形象。如果作者在revision中修复W1和W2，并改善W3-W6的讨论深度，本文有潜力达到Conference (4.0)水平。\n",
  "reviewer_id": "1",
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 审稿意见 — 方法严谨性 + 实验设计\n\n## Summary\n\n本文将教育测量领域的概化理论（G-theory）引入LLM评估，通过Henderson Method I对8个7-9B开源模型在5个基准上约230万条二值记录进行方差分量分解，发现model×item交互是主要的非残差方差来源（MC 30-36%, FF 15-17%），并据此通过D-study投影给出可复现性预算建议（3-prompt × 3-seed设计将MMLU所需题目从552降至178）。这是G-theory在NLP评估领域的首次完整应用（含D-study投影），方法论框架扎实，实验规模大，且附有9项稳健性检验。主要关切集中在：格式关联模式的统计功效不足但在结论中被过度声称、Bootstrap CI仅捕获item层不确定性、以及二值评分限定下的实用范围偏窄。\n\n## Strengths\n\n**S1** [方法新颖性] 首次将G-theory的完整工作流（G-study方差分解 + D-study预算投影）系统应用于LLM评估，填补了已有工作（Bouthillier et al., 2021; Messing, 2026）在D-study投影和跨格式比较方面的空白（Table 1, Section 2清晰定位了贡献）。\n\n**S2** [实验规模与设计] 7 facet × 8 model × 5 benchmark的全因子/准全因子设计（exp-001: 460,800 records fully crossed on MMLU; exp-002: 2,304,000 records across 5 benchmarks）是该领域迄今最大规模的多面交叉方差分析。设计矩阵（Table 2）清晰、可复现。\n\n**S3** [稳健性检验充分] Appendix A提供9项独立稳健性分析（GLMM ρ=1.0、REML差异<0.5pp、probit simulation、null calibration ratio=1.0008、LOMO max|ΔG|=0.030、accuracy-range stability r=-0.048、CI方法对比、facet specification sensitivity、reduced crossing validation ΔG=0.0008），系统覆盖了估计方法、数据分布、样本稳定性等多个角度。\n\n**S4** [核心发现的洞察力] model×item交互主导（Section 4.2, Table 5）是一个非直觉但重要的发现：模型主要在\"哪些题目难\"上分歧，而非在整体能力上分歧。MMLU学科粒度分析（Table 12, Appendix E）进一步验证了这一机制在knowledge vs. reasoning维度上的梯度变化（G_item从0.614到0.930）。\n\n**S5** [实用产出] 开源G-theory pipeline和D-study calculator具有直接实用价值；Table 7-9的预算建议为benchmark开发者提供了可操作的参考。IRT与G-theory正交互补的论证（Table 7, Zhou et al. 2026的116题在multi-facet下G从0.457升至0.895）也有启发性。\n\n**S6** [Binary data处理的透明度] Section 3.5明确标注了binary scoring假设，probit simulation量化了binarization的代价（D-study预算+36%），partial-credit对比（GSM8K G: 0.86→0.77）和text-exact-match对比（G: 0.936→0.007）展示了metric conditionality的严重程度。这种透明度值得肯定。\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1** [critical] 格式关联模式在结论中被过度声称\n\n- 具体位置：Section 4.3（标题含\"Exploratory\"）vs. Section 5 Conclusion vs. Abstract\n- 问题：Section 4.3明确将MC/FF方差结构差异标记为\"exploratory\"和\"descriptive observation\"（permutation p=0.10, n=5 benchmarks, benchmark-level CI spans zero），但Section 5 Conclusion写道\"The variance structure is format-dependent: MC benchmarks concentrate 68-72%...motivating per-format budget calibration\"，完全去掉了\"exploratory\"限定词。Abstract虽未直接声称format-dependent，但第2页Contribution 3写\"Format-associated variance patterns (exploratory)\"后，后续Table 9的预算建议已按MC/FF分开给出，实际上将这一探索性发现当作已建立的结论用于实践推荐。\n- 为什么影响接收：在n=5（3 MC + 2 FF）、p=0.10的统计功效下，从descriptive observation升级为prescriptive budget separation，违反了统计推断的基本审慎原则。一位Area Chair可能仅读Conclusion而形成错误印象。\n- 建议修改方向：(1) Conclusion中保留\"exploratory/preliminary\"限定词；(2) Table 9的MC/FF分列可保留但需加注\"based on n=5 benchmarks; format-specific calibration requires replication with a larger benchmark sample\"；(3) 或提供per-benchmark budgets而非per-format budgets，避免跨越归纳推断的边界。\n\n**W2** [critical] Bootstrap CI仅捕获item-level不确定性，D-study预算的置信区间被低估\n\n- 具体位置：Table 9 (95% CI columns), Appendix A CI method comparison\n- 问题：论文明确承认\"Bootstrap CIs capture item-sampling variability conditional on these 8 specific models; model-level stability is assessed separately via LOMO\"（Appendix A）。但Table 9报告的95% CI（如MMLU: [76, 116] items）仅反映item-level resampling。LOMO分析显示max|ΔG|=0.030，对应~23%的预算变化（Figure 9），但这一model-level不确定性从未与item-level CI联合量化。读者看到Table 9的CI会误认为它是总不确定性的度量。\n- 为什么影响接收：D-study预算是本文最核心的实用产出。如果其CI被系统性低估，所有基于Table 9的实践建议（\"93-128 items for G≥0.80\"）的可靠性都受到质疑。\n- 建议修改方向：(1) 在Table 9标题或脚注中明确标注CI仅反映item-level sampling variability；(2) 提供联合item+model uncertainty的估计（如将LOMO的|ΔG|范围叠加到bootstrap CI上）；(3) 或至少在正文中讨论combined uncertainty的量级（item CI ~20% + model uncertainty ~23% → 总不确定性可能在30-35%量级）。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W3** [warning] Model作为quasi-random facet的辩护链不完整\n\n- 具体位置：Section 3.6, Appendix A LOMO analysis\n- 问题：8个purposively selected模型被当作random facet，引用Meredith (1993)和Putnick & Barneeon (2016)，但这两篇文献是关于measurement invariance检验方法论的，并非关于justifying random-facet treatment for purposive samples。LOMO和four-model subset（Table 11: MC |ΔG|≤0.029, FF |ΔG|≤0.065）是within-sample stability checks，不等于out-of-sample generalization evidence。特别是FF的7.3% error（MATH, Table 11）意味着从4个模型预测8个模型的方差结构存在非 trivial的偏差。\n- 论文确实提供了\"treating models as random is more conservative\"的论证（G_random < G_fixed by 0.077-0.113，Table 10），这部分论证是有效的——如果模型实际上是固定的，那么random specification给出的是保守估计。但核心问题不在于random vs. fixed specification，而在于：从这8个特定模型估计的方差分量是否代表更广泛的7-9B模型宇宙？\n- 建议：(1) 更准确地引用G-theory文献中关于facet sampling的讨论（如Brennan, 2001, Ch. 5关于random vs. fixed facets的讨论）；(2) 明确讨论\"exchangeability within the target universe\"假设的可检验条件和局限；(3) 对FF benchmarks的较大预测偏差（7%）进行单独讨论。\n\n**W4** [warning] D-study投影的时间不变性假设未被充分讨论\n\n- 具体位置：Section 4.5最后一段 \"All projections assume the 2024-2025 model generation\"\n- 问题：D-study预算建议的实用性依赖于方差分量在时间上的稳定性。但LLM模型架构、训练数据和能力水平变化极快（2024到2025已经有significant shifts），论文仅以一句话带过这一关键假设。Scale validation（Section 4.6: Qwen2.5-72B, Llama-3.1-70B）提供了size维度的初步证据，但没有temporal维度的证据。\n- 建议：增加一段讨论方差分量temporal stability的分析。如果无法获得2025-2026模型的数据，至少应讨论哪些方差分量最可能随模型代际变化（如model×item interaction是否会随模型同质化而降低？）以及这对预算建议的影响方向。\n\n**W5** [warning] Partial-credit scoring的影响被低估\n\n- 具体位置：Section 3.5, Limitations, Appendix A Scoring metric sensitivity\n- 问题：GSM8K partial-credit G从0.86降至0.77（ΔG=-0.135），这一降幅超过了许多在论文中被详细讨论的其他效应。48.1%的incorrect responses有正确的中间步骤但错误的问题理解（Appendix A），这意味着binary scoring系统性地丢失了大量评估信息。然而，D-study预算建议（Table 9）完全基于binary scoring，而现实中越来越多的LLM评估采用partial-credit或连续评分（如GSM8K的step-level、MT-Bench的1-10评分）。\n- 建议：(1) 在正文（而非仅附录和Limitations）中更prominently讨论partial-credit的影响；(2) 至少对GSM8K给出partial-credit条件下的D-study预算以供对比；(3) 讨论binary→partial-credit transition对model×item interaction dominance结论的影响。\n\n**W6** [warning] Object of measurement的选择及其对实用性的影响未被讨论\n\n- 具体位置：Section 3.1\n- 问题：论文选择items作为object of measurement，G_item衡量的是\"item-level scores在不同条件下的泛化性\"。但LLM评估的主要用户关心的是model-level reliability（\"我的模型排名在不同评估条件下是否稳定？\"）。论文虽然间接地通过model×item interaction暗示了model-level的不可靠性，但从未直接量化model-level generalizability（将model作为object of measurement的G-study）。\n- 建议：至少在Discussion或Limitations中解释为什么选择items而非models作为object of measurement，以及两种选择下的G-coefficient有何关系。如可能，补充一个model作为object的G-study结果作为对照。\n\n### Minor（不影响接收）\n\n**M1** exp-002仅使用BF16精度和2个温度（0.0, 0.7），虽然Appendix A的reduced crossing validation显示ΔG=0.0008（在MMLU上），但这一验证仅基于MMLU——对于其他4个benchmark，precision×benchmark交互效应无法从数据中检验。建议在Appendix中加注这一局限。\n\n**M2** Abstract第一句\"up to 79 percentage points\"引用的是prior literature（Sclar et al., 2024等）的极端案例，非本研究发现。建议clarify这是\"prior work has shown\"而非本文的结果，避免在abstract中引发预期偏差。\n\n**M3** \"quasi-random facet\"不是G-theory标准术语（Brennan, 2001; Shavelson and Webb, 1991均使用\"random\"和\"fixed\"）。建议改用\"treated as random for the purpose of generalizability analysis\"或直接引用Brennan (2001, Ch. 5)关于facet universe definition的讨论。\n\n**M4** Benchmark contamination在Limitations中被提及但机制未讨论：如果部分item被contamination使得所有模型均答对，则这些item的model×item interaction为零，可能系统性地低估了model×item在clean benchmarks上的比例。值得一提。\n\n## Questions\n\n**Q1** Table 9的cross-model budgets假设n_M=8（8个模型同时评估）。如果用户仅评估1个模型，D-study预算应如何调整？请提供single-model cross-benchmark budgets（即将Table 7的方法应用到5个benchmark上）以增强实用性。\n\n**Q2** Probit simulation的ρ=0.732（excluding residual）意味着binary和continuous排名之间有约27%的rank discordance。论文论证\"qualitative ordering is preserved\"（top-5 correct in 79% of replications），但这是否足够精确以支持D-study budget projections中的quantitative claims（如\"178 items for G≥0.80\"）？\n\n**Q3** Scale validation（Section 4.6）仅覆盖Qwen和Llama家族，均已在main study中出现。是否有任何来自MoE架构或其他训练范式模型的证据？\n\n**Q4** Ordering facet在非MMLU benchmarks上σ²=0——这是因为ordering操作被执行但无效果，还是因为ordering操作未被应用到其他benchmark？请在正文中澄清。\n\n## Missing References\n\n- Cronbach, L. J., Gleser, G. C., Nanda, H., & Rajaratnam, N. (1972). *The Dependability of Behavioral Measurements*. Wiley. — G-theory的奠基文献，论文仅引用了Shavelson and Webb (1991)和Brennan (2001)作为G-theory来源，缺少对原始文献的致敬。\n- Webb, N. M., Shavelson, R. J., & Haertel, E. H. (2006). \"Reliability coefficients and generalizability theory.\" *Handbook of Statistics*, 26, 81-124. — 关于G-theory在non-standard data（包括binary）上应用的综述讨论。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | Henderson Method I的技术应用基本正确，robustness checks充分（9项），但format pattern overclaim（W1）和CI underestimation（W2）是实质性方法论问题 |\n| Excitement | 3.5/5 | G-theory→LLM evaluation的框架迁移具有新颖性，model×item interaction发现有洞察力，但binary-only限定和n=5 benchmark的format分析限制了impact |\n| Reproducibility | 4/5 | 开源pipeline、详细的设计矩阵、完整的prompt templates（Appendix G）、模型ID（Appendix G）、统计方法描述充分；缺少的是raw data和具体采样种子 |\n| Overall Assessment | **3.5** (Borderline Conference) |\n| Confidence | 4/5 | 熟悉G-theory和LLM evaluation两个领域，仔细阅读了论文及全部附录 |\n\n## Overall Assessment 理由\n\n本文在方法论框架、实验规模和稳健性检验方面达到了高标准，核心发现（model×item interaction dominance + D-study budgets）具有实用价值和理论启发性。将其评为Borderline Conference (3.5)而非Conference (4.0)的主要原因是两个方法论问题的叠加：(1) format-associated pattern从\"exploratory\"到Conclusion中的\"established\"的不当升级，以及(2) D-study预算的CI系统性低估（仅item-level，未含model-level uncertainty）。这两个问题均可在修改中解决（W1可通过调整措辞和添加注释修复，W2可通过报告联合不确定性修复），但在当前版本中它们共同影响了论文的statistical rigor形象。如果作者在revision中修复W1和W2，并改善W3-W6的讨论深度，本文有潜力达到Conference (4.0)水平。\n",
    "reviewer_id": "1",
    "project": "nlp_variance_gtheory"
  }
}
```

</details>

---


### Tool result

_source line 725 · 2026-05-25T21:26:10.487613+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_265de443abfe4594f91451b075b582ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3663
}
```

</details>

---


### Tool call

_source line 726 · 2026-05-25T21:26:16.264013+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 727 · 2026-05-25T21:26:16.314527+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 728 · 2026-05-25T21:26:28.062245+00:00_

审稿意见已提交给 Review Director。

总结：我给出 **Overall 3.5 (Borderline Conference)**。两个 Must-Fix 问题：(1) 格式关联模式（n=5, p=0.10）在 Conclusion 中从 "exploratory" 升级为 "established"；(2) Table 9 的 D-study 预算 CI 仅捕获 item-level 不确定性，未含 model-level uncertainty（LOMO 显示 ~23% 额外变动）。四个 Should-Fix：model quasi-random facet 辩护链不完整、时间不变性假设欠讨论、partial-credit 影响被低估、object of measurement 选择对实用性的影响未说明。两个 Must-Fix 均可在修改中解决，修复后有潜力达到 4.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1"
}
```

</details>

---


## Round 22

## Round 22

4 recorded events


### User

_source line 729 · 2026-05-25T21:28:37.684968+00:00_

[Round 11 审稿请求]:
以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Weakness 和 Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

# Reviewer 2 审稿意见 — Round 11 (新颖性 + 完整性 + 写作质量)

## Summary

本文将 Generalizability theory (G-theory) 应用于 LLM 评测方差分解，在 8 个 7–9B 指令微调模型和 5 个 benchmark 上交叉 7 个设计因子（共 2.3M 二值记录），发现 model×item 交互是主导非残差方差源（MC 30–36%，FF 15–17%），多因子设计可将所需 item 数从 500+ 降至 ~100（G ≥ 0.80），MC/FF 格式呈现不同的方差结构。论文提供开源 G-theory 流水线和 D-study 计算器。方法论扎实、鲁棒性验证全面，但在关键 framing 和 scope 声明上存在需要修正的问题。

## Strengths

**S1: 实验规模与系统性**
7 facets × 8 models × 5 benchmarks 的全交叉设计是对 Messing (2026)（5 facets × 1 benchmark）的实质性扩展。2.3M 二值记录为方差分解提供了高置信度估计。

**S2: D-study 预算 — 最具实用价值的贡献**
将方差分解转化为可操作的 item 预算建议（Table 7, 8, 9），特别是推荐的 3-prompt × 3-seed 设计（178 items, §4.5）给出了平衡成本和可靠性的具体方案。IRT+G-theory 正交互补性（Table 7: IRT 116 items 在 single-condition 下 G=0.457，multi-facet 下 G=0.895）是一个新颖且有说服力的结果。

**S3: 鲁棒性分析堪称典范**
Appendix A 覆盖了 GLMM complement (ρ=1.0)、accuracy-range stability、Henderson vs REML (<0.5pp)、probit simulation、LOMO (Table 4, CV ≤ 1.25%)、inter-model κ (0.33–0.46)、scoring metric sensitivity 等 9 项检验。这种系统性验证在 NLP 论文中不多见。

**S4: 方法论透明度**
Henderson Method I 选择的合理性（balanced designs + binary data, §3.5）、notation 清晰（footnote 5）、设计矩阵完整（Table 2）、代码公开。quasi-random facet 处理（§3.6）的 fixed vs. random 对比（G 增加 0.077–0.113）增加了透明度。

**S5: IRT 互补性揭示了一个被忽视的维度**
Table 7 中 IRT baseline 一行（G=0.457 → 0.895）是全文最有说服力的单一结果，说明 item selection 和 protocol optimization 是独立的优化维度。这对 benchmark 开发者有直接的方法论启示。

## Weaknesses

### Must-Fix

**W1 [critical]: "10× fewer items" framing 隐藏了 total evaluations 的剧增**
- Abstract: "reducing item requirements from over 1,000 to roughly 100" — 仅描述 item 维度的缩减
- 实际情况：full multi-facet (1,296 conditions) 下 item 从 552→55（10×），但 total evaluations 从 552→71,280（129× 增长）
- 推荐的 3×3 设计虽然在 §4.5 披露了 "2.9× total-evaluation increase for a 3.1× item reduction"，但 abstract 和 Figure 1 overview 都只呈现了 item 维度
- Title 用 "Reproducibility Budgets" 暗示效率提升，但对多数用户而言总计算量才是关键成本
- 建议: Abstract 中应同时报告 item reduction 和 total evaluation overhead（至少对推荐的 3×3 设计）

**W2 [critical]: Binary scoring scope 未在 title/abstract 中充分限定**
- Title: "Reproducibility Budgets for Open-Weight LLM Evaluation" — 暗示适用于一般 LLM 评测
- 但所有发现严格受限于 binary correctness scoring（§3.5）
- Text-exact-match: G 从 0.936 崩溃到 0.007（§4.1）— 方差结构完全改变
- Partial-credit (GSM8K): G 从 0.86 降至 0.77（§3.5）— 显著退化
- 对于实际评测场景（code generation、open-ended QA、rubric-based evaluation），binary scoring 是例外而非常态
- 建议: Title 添加限定语（如 "under Binary Correctness Scoring"），或 abstract 明确声明 scope

**W3 [critical]: G_item 与 model ranking reliability 之间的概念鸿沟**
- 论文以 items (p) 为 object of measurement（§3.1），计算 G_item 衡量 item-level 跨条件泛化能力
- 但 benchmark 用户关心的是 model ranking reliability
- G_item ≥ 0.80 保证 item scores 在不同 prompt/seed 下一致，但不直接等同于 model ranking 稳定
- 论文提供了间接证据（LOMO Table 4, κ=0.33–0.46），但未直接计算 rank-order stability 或 G_model
- 建议: 增加 model ranking stability 分析（如 Kendall's W 或 bootstrap 排名一致性），或至少讨论 G_item 向 model ranking reliability 的映射条件

### Should-Fix

**W4 [warning]: §4.3 format-associated patterns 占比失衡**
- 探索性发现（n=5, permutation p=0.10, benchmark-level CI spans zero）在 8 页正文中占约 1 页
- 贡献 C3 在 Introduction 中与 C1、C2 并列，但证据强度远不如前两者
- 建议: 压缩 §4.3 为一段描述，将 Figure 7 和 Figure 8 移入 appendix

**W5 [warning]: Table 6 caption 中 MC vs FF 不同量的标注易造成混淆**
- "prompt†" 行对 MC 报告 prompt×item interaction，对 FF 报告 prompt main effect
- 同一行代表不同统计量，读者自然期望同一行表示相同概念

**W6 [warning]: Conclusion (§5) 过于简短，缺乏 practical implications 和 adoption pathway**
- 全文仅 4 句话，缺失 benchmark 开发者建议、leaderboard 影响、future work、IRT pipeline 集成路径

**W7 [warning]: Partial-credit transferability 仅在 GSM8K 单一 benchmark 上验证**
- §3.5 声称 partial-credit 下 G 从 0.86 降至 0.77 (ΔG = −0.135)
- 但仅 GSM8K 一个 benchmark
- 建议: 明确声明 "在 GSM8K 的 step-level partial credit 下初步观察到"

**W8 [warning]: 遗漏重要相关文献**
- MMLU-Redux (Gema et al., 2024), MMLU-Pro (Wang et al., 2024), Contamination 检测文献

### Minor

**W9 [minor]: Abstract 约 201 词，略超 EMNLP 2026 的 200 词限制**
**W10 [minor]: Abstract 数值密度过高（20+ 数值）**
**W11 [minor]: main.tex line 43 使用 `\enlargethispage{1\baselineskip}`**
**W12 [minor]: Table 1 (Positioning) 与 Messing (2026) 的对比需注明 facet 差异**

## Questions

**Q1**: 为什么选择 items 而非 models 作为 object of measurement？G_item ≥ 0.80 在什么条件下能保证 model ranking stability？
**Q2**: 推荐的 3×3 设计在单 GPU 上的实际墙钟时间是多少？
**Q3**: 200 items 通过 stratified sampling 选取。不同的 200-item 样本是否会产生类似的 G_item？
**Q4**: Table 1 中与 Messing (2026) 的对比是否公平？两者评测范式不同。
**Q5**: quasi-random 处理的合理性在什么条件下成立？

## Missing References
1. MMLU-Redux (Gema et al., 2024)
2. MMLU-Pro (Wang et al., 2024)
3. Contamination 检测文献 (Shi et al. 2023, Golchin & Surdeanu 2024)
4. Evaluation harness 标准化集成

## Overall Assessment
**3.5** (Borderline Conference) | Confidence: 4/5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 730 · 2026-05-25T21:30:47.932772+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n## Weaknesses 回应\n\n### Must-Fix\n\n**[AGREE] R2-W1: \"10× fewer items\" framing 隐藏了 total evaluations 的剧增**\n\n同意这是一个 framing 问题。Abstract 写 \"reducing item requirements from over 1,000 to roughly 100\" 仅展示了 item 维度的缩减，而 full multi-facet 设计的 total evaluations 从 552 增长到 71,280（129×）。虽然 §4.5 在正文中披露了推荐的 3×3 设计的 tradeoff（\"2.9× total-evaluation increase for a 3.1× item reduction\"），但 abstract 和 Figure 1 overview 的 framing 确实容易让读者形成 \"免费午餐\" 的印象。\n\n不过，我认为此问题的严重程度介于 critical 和 warning 之间。理由：(1) §4.5 和 Table 8 已经完整展示了从 single-condition 到 full multi-facet 的连续 cost-reliability tradeoff；(2) 推荐方案（3×3, 178 items, 1,602 total evals）的 total evaluation overhead 是 2.9×，这在实际GPU时间上是可接受的；(3) 核心洞察——更少的 unique items + 更多的 conditions per item 比更多 unique items + 单一 condition 更可靠——是 G-theory 的标准结论，不存在误导意图。修改 abstract 加入 total evaluation overhead 即可解决。\n\n---\n\n**[AGREE] R2-W2: Binary scoring scope 未在 title/abstract 中充分限定**\n\n同意。这与我自己的审查发现一致。Title \"Reproducibility Budgets for Open-Weight LLM Evaluation\" 暗示了广泛适用性，但 §3.5 明确展示了 binary scoring 的极端 metric conditionality：text-exact-match G 从 0.936 崩溃到 0.007（§4.1），partial-credit G 从 0.86 降至 0.77（Appendix A）。论文的所有 D-study 预算、方差分解结论、format-associated patterns 均严格受限于 binary correctness scoring。\n\nTitle 添加限定语的建议合理。不过我补充一点：binary correctness scoring 在 MC benchmarks（MMLU、ARC、HellaSwag）中确实是标准做法，所以对 MC benchmarks 的结论不存在 scope 问题。问题主要出在 FF benchmarks（GSM8K、MATH），其中许多实际评测使用 partial credit 或更细粒度的 rubric。因此限定语可以更精确——如 \"under Binary Correctness Scoring\" 或在 abstract 中说明 \"all findings are conditioned on binary correctness scoring\"。\n\n---\n\n**[AGREE] R2-W3: G_item 与 model ranking reliability 之间的概念鸿沟**\n\n强烈同意。这与我在 W6 中提出的问题完全一致。论文以 items 为 object of measurement（§3.1），G_item 衡量的是 item-level scores 在不同条件下的泛化能力。但 benchmark 用户的核心需求是 model ranking reliability——\"我的模型在 benchmark 上的排名是否可复现？\"\n\n论文提供了一些间接证据（LOMO Table 4 显示 max|ΔG|=0.030；inter-model Cohen's κ = 0.33-0.46），但从未直接量化 model ranking stability。R2 建议增加 Kendall's W 或 bootstrap 排名一致性分析，我认为这是 actionable 且必要的——至少应讨论 G_item ≥ 0.80 在什么条件下蕴含 model ranking stability。\n\n---\n\n### Should-Fix\n\n**[REBUT] R2-W4: §4.3 format-associated patterns 占比失衡**\n\n部分不同意。R2 认为应将 §4.3 压缩为一段、Figure 7 和 Figure 8 移入 appendix。但我认为：\n\n1. §4.3 的 format-associated finding 虽然在统计上是 exploratory（n=5, p=0.10），但在 **描述层面** 提供了重要的结构信息：MC benchmarks 集中 68-72% 的 item-related variance，FF benchmarks 仅 31-41%。这一 30+ percentage point 的差异（Table 6）即使在 n=5 下也是 substantive 的描述性发现。\n2. Figure 7（item difficulty heterogeneity scatter, ρ=0.82）提供了 **机制解释**（difficulty dispersion drives variance structure），这不是可有可无的附属信息，而是帮助读者理解 WHY MC and FF differ。\n3. MMLU subject-level analysis（Table 12, Appendix E）在 n=10 subjects、p=0.005 下验证了同一机制，提供了跨粒度的 converging evidence。\n\n我同意的是：Conclusion（§5）中应保留 \"exploratory\" 限定词（这也是我在自己的 W1 中提出的核心问题）。但 §4.3 的篇幅（约1页）和 Figure 7-8 在正文中的存在是合理的，因为它们为 per-benchmark budget calibration（Table 9 按 MC/FF 分列）提供了必要的背景信息。\n\n---\n\n**[AGREE] R2-W5: Table 6 caption 中 MC vs FF 不同量的标注易造成混淆**\n\n同意。Table 6（即 Table 6/cross-benchmark variance decomposition）的 \"prompt†\" 行对 MC 报告 prompt×item interaction、对 FF 报告 prompt main effect，同一行代表不同统计量确实违反了表格设计的一致性原则。虽然 caption 中有 footnote 说明（\"†For MC, reports prompt×item interaction; for FF, reports prompt main effect\"），但读者自然期望同一行表示相同概念。建议拆为两行或使用更清晰的标注方式。\n\n---\n\n**[REBUT] R2-W6: Conclusion (§5) 过于简短**\n\n部分不同意。§5 虽然仅 4 句话，但覆盖了三个核心结论（model×item dominance、D-study budgets、format-associated patterns）和三条实践建议（adopt multi-facet designs、report item-level accuracy、calibrate budgets per format）。在 8 页篇幅限制下，简洁的 conclusion 将更多空间让给了方法和实验，这是合理的优先级选择。\n\n不过 R2 指出的一个具体缺失确实存在价值：**adoption pathway**——benchmark 开发者如何将 G-theory pipeline 集成到现有评测流程中？这可以在 Conclusion 或 Discussion 中用 1-2 句话补充，不需要一个完整的段落。Future work 可以在 camera-ready 中扩展，但不是当前版本的必要条件。\n\n---\n\n**[AGREE] R2-W7: Partial-credit transferability 仅在 GSM8K 单一 benchmark 上验证**\n\n同意。这与我在 W5 中的关切一致。GSM8K 的 step-level partial credit 分析（ΔG = -0.135, Appendix A）是唯一的 partial-credit 证据。论文应明确将这一发现限定为 \"在 GSM8K 的 step-level partial credit 下初步观察到\"，而非暗示对所有 partial-credit 评分方案的适用性。MATH 的 \\boxed{} 格式本身也支持 partial credit（中间推理步骤），但论文未做此分析。\n\n---\n\n**[REBUT] R2-W8: 遗漏重要相关文献**\n\n部分不同意：\n\n- **MMLU-Redux (Gema et al., 2024)** 和 **MMLU-Pro (Wang et al., 2024)**：这两篇关注 benchmark 质量和扩展，与本文的方差分解框架关联度有限。本文使用原版 MMLU 是因为它是最广泛使用的 benchmark，且 200-item stratified sample 已经控制了 item 质量。这些文献在 Related Work 中提及是可选的但非必要的。\n- **Contamination检测文献 (Shi et al. 2023, Golchin & Surdeanu 2024)**：Limitations 已提及 contamination 问题（\"Benchmark contamination in pretraining data may inflate item accuracy and compress variance\"）。引用具体检测方法论的文献确实可以增强这一讨论。同意补充。\n- **Evaluation harness 标准化集成**：论文使用自定义 vLLM pipeline 而非 lm-evaluation-harness 是有意为之的设计选择（控制 CUDA-level nondeterminism, §3.4），不需要引用 harness 集成文献。\n\n---\n\n### Minor\n\n**[AGREE] R2-W9: Abstract 约 201 词，略超 EMNLP 2026 的 200 词限制**\n\n同意。EMNLP 2026 硬性限制 abstract ≤ 200 words，201 词违规。必须修剪。\n\n---\n\n**[REBUT] R2-W10: Abstract 数值密度过高（20+ 数值）**\n\n不同意。本文是一篇 quantitative methods paper，其核心贡献就是具体数值（方差分量百分比、G coefficients、item budgets）。Abstract 中的数值密度反映了论文内容的本质。删除数值会使 abstract 变得空泛、无法传达方法论贡献。Methods papers 的 abstract 惯例允许高数值密度——参见 Bouthillier et al. (2021) 的 abstract 同样包含大量统计数字。\n\n---\n\n**[AGREE] R2-W11: `\\enlargethispage{1\\baselineskip}` 排版 hack**\n\n同意这是一个 minor formatting issue，但在实际投稿中很常见（几乎所有 8 页 camera-ready 都有类似调整）。只要不违反 page limit（正文 8 页），这不会被 reviewer 或 AC 标记。\n\n---\n\n**[AGREE] R2-W12: Table 1 与 Messing (2026) 的对比需注明 facet 差异**\n\n同意。Table 1 的 positioning 对比应注明两者评测范式的差异（Messing: single benchmark, judge-based; 本文: 5 benchmarks, generation-based scoring）。目前的对比格式可能暗示 apple-to-apple comparison，但实际上两者的 facet 定义和交叉结构不同。\n\n---\n\n## Questions 回应\n\n**Q1**: 同意这是一个重要的概念问题（已在 W3 回应和我自己的 W6 中讨论）。G_item ≥ 0.80 保证 item scores 的跨条件一致性，但 item-level reliability 向 model ranking reliability 的映射取决于 model main effect 相对于 model×item interaction 的比值。当 model×item 远大于 model main effect（如 MC: 30-36% vs 3-5%），model ranking stability 会低于 G_item 所暗示的水平。\n\n**Q2**: 论文未报告 wall-clock time。这对实用性讨论有价值但非必需——推荐的 3×3 设计（178 items × 9 conditions = 1,602 evaluations）在单 GPU 上应在分钟量级完成（vLLM 推理速度），不构成实际瓶颈。不过补充这一数据可以增强实践指导性。\n\n**Q3**: §4.5 报告了 3 次 MMLU resamples 的 CV=3.1%（§3.2 实为 CV=3.1%）。这提供了初步证据但样本量偏小（仅 3 次 resample）。更充分的验证需要更多 resamples 或 split-half analysis。这与我审查中的考虑一致。\n\n**Q4**: Table 1 的对比基本公平但需要 caveats（同 W12）。Messing (2026) 使用 judge-based evaluation on single benchmark，本文使用 generation-based scoring across 5 benchmarks——两者的 facet 定义不同但 G-theory 框架层面是可比的（都是多面交叉方差分解）。建议 Table 1 caption 中加注评测范式差异。\n\n**Q5**: Quasi-random 处理的合理性条件：(1) 目标 universe 可定义（本文定义为 \"open-weight, instruction-tuned, 7-9B models\"）；(2) 样本覆盖 universe 的主要维度（8 个模型来自 6+ 不同家族）；(3) exchangeability within sample（LOMO CV ≤ 1.25%）。条件 (3) 是 within-sample 验证，不保证 out-of-sample——这是 G-theory 应用中固有的局限，不特指本文。本文通过 random > fixed (conservative) 的论证（Table 10, ΔG = 0.077-0.113）提供了部分 safeguard。\n\n---\n\n## 总体评价\n\nReviewer 2 的审稿在 framing 和 scope 方面提出了有价值的问题（W1-W3），且与我自己的独立审查高度一致。W1（total evaluation framing）和 W2（binary scoring scope）是 presentation 问题而非 methodological flaws，可在修改中解决。W3（G_item vs model ranking）是更深层的概念问题，需要额外分析或充分讨论。\n\n我与 R2 的主要分歧在 W4（§4.3 篇幅）和 W10（abstract 数值密度）——前者的 format-associated 内容虽统计功效不足但描述性价值显著，后者是 methods paper 的惯例。\n\nR2 给出 3.5（Borderline Conference），与我的评分一致。两位 reviewer 的核心关切（format pattern overclaim、binary scope limitation、G_item vs model ranking gap）高度重叠，说明这些是论文的真实短板而非 reviewer 偏见。\n",
  "reviewer_id": "1",
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n## Weaknesses 回应\n\n### Must-Fix\n\n**[AGREE] R2-W1: \"10× fewer items\" framing 隐藏了 total evaluations 的剧增**\n\n同意这是一个 framing 问题。Abstract 写 \"reducing item requirements from over 1,000 to roughly 100\" 仅展示了 item 维度的缩减，而 full multi-facet 设计的 total evaluations 从 552 增长到 71,280（129×）。虽然 §4.5 在正文中披露了推荐的 3×3 设计的 tradeoff（\"2.9× total-evaluation increase for a 3.1× item reduction\"），但 abstract 和 Figure 1 overview 的 framing 确实容易让读者形成 \"免费午餐\" 的印象。\n\n不过，我认为此问题的严重程度介于 critical 和 warning 之间。理由：(1) §4.5 和 Table 8 已经完整展示了从 single-condition 到 full multi-facet 的连续 cost-reliability tradeoff；(2) 推荐方案（3×3, 178 items, 1,602 total evals）的 total evaluation overhead 是 2.9×，这在实际GPU时间上是可接受的；(3) 核心洞察——更少的 unique items + 更多的 conditions per item 比更多 unique items + 单一 condition 更可靠——是 G-theory 的标准结论，不存在误导意图。修改 abstract 加入 total evaluation overhead 即可解决。\n\n---\n\n**[AGREE] R2-W2: Binary scoring scope 未在 title/abstract 中充分限定**\n\n同意。这与我自己的审查发现一致。Title \"Reproducibility Budgets for Open-Weight LLM Evaluation\" 暗示了广泛适用性，但 §3.5 明确展示了 binary scoring 的极端 metric conditionality：text-exact-match G 从 0.936 崩溃到 0.007（§4.1），partial-credit G 从 0.86 降至 0.77（Appendix A）。论文的所有 D-study 预算、方差分解结论、format-associated patterns 均严格受限于 binary correctness scoring。\n\nTitle 添加限定语的建议合理。不过我补充一点：binary correctness scoring 在 MC benchmarks（MMLU、ARC、HellaSwag）中确实是标准做法，所以对 MC benchmarks 的结论不存在 scope 问题。问题主要出在 FF benchmarks（GSM8K、MATH），其中许多实际评测使用 partial credit 或更细粒度的 rubric。因此限定语可以更精确——如 \"under Binary Correctness Scoring\" 或在 abstract 中说明 \"all findings are conditioned on binary correctness scoring\"。\n\n---\n\n**[AGREE] R2-W3: G_item 与 model ranking reliability 之间的概念鸿沟**\n\n强烈同意。这与我在 W6 中提出的问题完全一致。论文以 items 为 object of measurement（§3.1），G_item 衡量的是 item-level scores 在不同条件下的泛化能力。但 benchmark 用户的核心需求是 model ranking reliability——\"我的模型在 benchmark 上的排名是否可复现？\"\n\n论文提供了一些间接证据（LOMO Table 4 显示 max|ΔG|=0.030；inter-model Cohen's κ = 0.33-0.46），但从未直接量化 model ranking stability。R2 建议增加 Kendall's W 或 bootstrap 排名一致性分析，我认为这是 actionable 且必要的——至少应讨论 G_item ≥ 0.80 在什么条件下蕴含 model ranking stability。\n\n---\n\n### Should-Fix\n\n**[REBUT] R2-W4: §4.3 format-associated patterns 占比失衡**\n\n部分不同意。R2 认为应将 §4.3 压缩为一段、Figure 7 和 Figure 8 移入 appendix。但我认为：\n\n1. §4.3 的 format-associated finding 虽然在统计上是 exploratory（n=5, p=0.10），但在 **描述层面** 提供了重要的结构信息：MC benchmarks 集中 68-72% 的 item-related variance，FF benchmarks 仅 31-41%。这一 30+ percentage point 的差异（Table 6）即使在 n=5 下也是 substantive 的描述性发现。\n2. Figure 7（item difficulty heterogeneity scatter, ρ=0.82）提供了 **机制解释**（difficulty dispersion drives variance structure），这不是可有可无的附属信息，而是帮助读者理解 WHY MC and FF differ。\n3. MMLU subject-level analysis（Table 12, Appendix E）在 n=10 subjects、p=0.005 下验证了同一机制，提供了跨粒度的 converging evidence。\n\n我同意的是：Conclusion（§5）中应保留 \"exploratory\" 限定词（这也是我在自己的 W1 中提出的核心问题）。但 §4.3 的篇幅（约1页）和 Figure 7-8 在正文中的存在是合理的，因为它们为 per-benchmark budget calibration（Table 9 按 MC/FF 分列）提供了必要的背景信息。\n\n---\n\n**[AGREE] R2-W5: Table 6 caption 中 MC vs FF 不同量的标注易造成混淆**\n\n同意。Table 6（即 Table 6/cross-benchmark variance decomposition）的 \"prompt†\" 行对 MC 报告 prompt×item interaction、对 FF 报告 prompt main effect，同一行代表不同统计量确实违反了表格设计的一致性原则。虽然 caption 中有 footnote 说明（\"†For MC, reports prompt×item interaction; for FF, reports prompt main effect\"），但读者自然期望同一行表示相同概念。建议拆为两行或使用更清晰的标注方式。\n\n---\n\n**[REBUT] R2-W6: Conclusion (§5) 过于简短**\n\n部分不同意。§5 虽然仅 4 句话，但覆盖了三个核心结论（model×item dominance、D-study budgets、format-associated patterns）和三条实践建议（adopt multi-facet designs、report item-level accuracy、calibrate budgets per format）。在 8 页篇幅限制下，简洁的 conclusion 将更多空间让给了方法和实验，这是合理的优先级选择。\n\n不过 R2 指出的一个具体缺失确实存在价值：**adoption pathway**——benchmark 开发者如何将 G-theory pipeline 集成到现有评测流程中？这可以在 Conclusion 或 Discussion 中用 1-2 句话补充，不需要一个完整的段落。Future work 可以在 camera-ready 中扩展，但不是当前版本的必要条件。\n\n---\n\n**[AGREE] R2-W7: Partial-credit transferability 仅在 GSM8K 单一 benchmark 上验证**\n\n同意。这与我在 W5 中的关切一致。GSM8K 的 step-level partial credit 分析（ΔG = -0.135, Appendix A）是唯一的 partial-credit 证据。论文应明确将这一发现限定为 \"在 GSM8K 的 step-level partial credit 下初步观察到\"，而非暗示对所有 partial-credit 评分方案的适用性。MATH 的 \\boxed{} 格式本身也支持 partial credit（中间推理步骤），但论文未做此分析。\n\n---\n\n**[REBUT] R2-W8: 遗漏重要相关文献**\n\n部分不同意：\n\n- **MMLU-Redux (Gema et al., 2024)** 和 **MMLU-Pro (Wang et al., 2024)**：这两篇关注 benchmark 质量和扩展，与本文的方差分解框架关联度有限。本文使用原版 MMLU 是因为它是最广泛使用的 benchmark，且 200-item stratified sample 已经控制了 item 质量。这些文献在 Related Work 中提及是可选的但非必要的。\n- **Contamination检测文献 (Shi et al. 2023, Golchin & Surdeanu 2024)**：Limitations 已提及 contamination 问题（\"Benchmark contamination in pretraining data may inflate item accuracy and compress variance\"）。引用具体检测方法论的文献确实可以增强这一讨论。同意补充。\n- **Evaluation harness 标准化集成**：论文使用自定义 vLLM pipeline 而非 lm-evaluation-harness 是有意为之的设计选择（控制 CUDA-level nondeterminism, §3.4），不需要引用 harness 集成文献。\n\n---\n\n### Minor\n\n**[AGREE] R2-W9: Abstract 约 201 词，略超 EMNLP 2026 的 200 词限制**\n\n同意。EMNLP 2026 硬性限制 abstract ≤ 200 words，201 词违规。必须修剪。\n\n---\n\n**[REBUT] R2-W10: Abstract 数值密度过高（20+ 数值）**\n\n不同意。本文是一篇 quantitative methods paper，其核心贡献就是具体数值（方差分量百分比、G coefficients、item budgets）。Abstract 中的数值密度反映了论文内容的本质。删除数值会使 abstract 变得空泛、无法传达方法论贡献。Methods papers 的 abstract 惯例允许高数值密度——参见 Bouthillier et al. (2021) 的 abstract 同样包含大量统计数字。\n\n---\n\n**[AGREE] R2-W11: `\\enlargethispage{1\\baselineskip}` 排版 hack**\n\n同意这是一个 minor formatting issue，但在实际投稿中很常见（几乎所有 8 页 camera-ready 都有类似调整）。只要不违反 page limit（正文 8 页），这不会被 reviewer 或 AC 标记。\n\n---\n\n**[AGREE] R2-W12: Table 1 与 Messing (2026) 的对比需注明 facet 差异**\n\n同意。Table 1 的 positioning 对比应注明两者评测范式的差异（Messing: single benchmark, judge-based; 本文: 5 benchmarks, generation-based scoring）。目前的对比格式可能暗示 apple-to-apple comparison，但实际上两者的 facet 定义和交叉结构不同。\n\n---\n\n## Questions 回应\n\n**Q1**: 同意这是一个重要的概念问题（已在 W3 回应和我自己的 W6 中讨论）。G_item ≥ 0.80 保证 item scores 的跨条件一致性，但 item-level reliability 向 model ranking reliability 的映射取决于 model main effect 相对于 model×item interaction 的比值。当 model×item 远大于 model main effect（如 MC: 30-36% vs 3-5%），model ranking stability 会低于 G_item 所暗示的水平。\n\n**Q2**: 论文未报告 wall-clock time。这对实用性讨论有价值但非必需——推荐的 3×3 设计（178 items × 9 conditions = 1,602 evaluations）在单 GPU 上应在分钟量级完成（vLLM 推理速度），不构成实际瓶颈。不过补充这一数据可以增强实践指导性。\n\n**Q3**: §4.5 报告了 3 次 MMLU resamples 的 CV=3.1%（§3.2 实为 CV=3.1%）。这提供了初步证据但样本量偏小（仅 3 次 resample）。更充分的验证需要更多 resamples 或 split-half analysis。这与我审查中的考虑一致。\n\n**Q4**: Table 1 的对比基本公平但需要 caveats（同 W12）。Messing (2026) 使用 judge-based evaluation on single benchmark，本文使用 generation-based scoring across 5 benchmarks——两者的 facet 定义不同但 G-theory 框架层面是可比的（都是多面交叉方差分解）。建议 Table 1 caption 中加注评测范式差异。\n\n**Q5**: Quasi-random 处理的合理性条件：(1) 目标 universe 可定义（本文定义为 \"open-weight, instruction-tuned, 7-9B models\"）；(2) 样本覆盖 universe 的主要维度（8 个模型来自 6+ 不同家族）；(3) exchangeability within sample（LOMO CV ≤ 1.25%）。条件 (3) 是 within-sample 验证，不保证 out-of-sample——这是 G-theory 应用中固有的局限，不特指本文。本文通过 random > fixed (conservative) 的论证（Table 10, ΔG = 0.077-0.113）提供了部分 safeguard。\n\n---\n\n## 总体评价\n\nReviewer 2 的审稿在 framing 和 scope 方面提出了有价值的问题（W1-W3），且与我自己的独立审查高度一致。W1（total evaluation framing）和 W2（binary scoring scope）是 presentation 问题而非 methodological flaws，可在修改中解决。W3（G_item vs model ranking）是更深层的概念问题，需要额外分析或充分讨论。\n\n我与 R2 的主要分歧在 W4（§4.3 篇幅）和 W10（abstract 数值密度）——前者的 format-associated 内容虽统计功效不足但描述性价值显著，后者是 methods paper 的惯例。\n\nR2 给出 3.5（Borderline Conference），与我的评分一致。两位 reviewer 的核心关切（format pattern overclaim、binary scope limitation、G_item vs model ranking gap）高度重叠，说明这些是论文的真实短板而非 reviewer 偏见。\n",
    "reviewer_id": "1",
    "project": "nlp_variance_gtheory"
  }
}
```

</details>

---


### Tool result

_source line 731 · 2026-05-25T21:30:51.547641+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_265de443abfe4594f91451b075b582ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3614
}
```

</details>

---


### Assistant

_source line 732 · 2026-05-25T21:31:04.745628+00:00_

已提交对 Reviewer 2 的逐条回应。总结：

- **6 条 AGREE**：W1（total eval framing）、W2（binary scope）、W3（G_item vs model ranking）、W5（Table 6 混合量）、W7（partial-credit 单 benchmark）、W9/W11/W12（minor issues）
- **3 条 REBUT**：W4（§4.3 篇幅——描述性价值足够支撑正文存在）、W6（Conclusion 简短但内容完整）、W10（abstract 数值密度是 methods paper 惯例）
- W8 部分同意（contamination 文献应补充，MMLU-Redux/Pro 非必需）

两位 reviewer 的核心关切高度重叠：format pattern overclaim、binary scope limitation、G_item vs model ranking gap。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1"
}
```

</details>

---
