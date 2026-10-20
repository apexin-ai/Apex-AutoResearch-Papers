# Reviewer 2 coordination — Part 2 of 2

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../reviewer-2-coordination.md) · [Structured JSON](../../../sessions/31/31d4f7607fc2692ee090.json)

## Round 16

### Tool call

_source line 474 · 2026-05-25T21:16:40.686596+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 475 · 2026-05-25T21:16:41.191226+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 476 · 2026-05-25T21:16:41.645535+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2831
}
```

</details>

---


### Tool call

_source line 477 · 2026-05-25T21:16:41.645978+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 478 · 2026-05-25T21:16:42.678102+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 479 · 2026-05-25T21:16:43.185161+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 480 · 2026-05-25T21:16:45.600491+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 6283
}
```

</details>

---


### Tool call

_source line 481 · 2026-05-25T21:16:45.651138+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines including: all scoring dimensions (soundness, excitement, overall assessment, confidence, etc.), their scales (1-5 or whatever), and detailed descriptions for each score level. Also extract any specific criteria reviewers should evaluate."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines including: all scoring dimensions (soundness, excitement, overall assessment, confidence, etc.), their scales (1-5 or whatever), and detailed descriptions for each score level. Also extract any specific criteria reviewers should evaluate."
  }
}
```

</details>

---


### Tool result

_source line 482 · 2026-05-25T21:16:45.854398+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 6077
}
```

</details>

---


### Tool result

_source line 483 · 2026-05-25T21:16:46.536867+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5850
}
```

</details>

---


### Tool result

_source line 484 · 2026-05-25T21:16:46.856854+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5665
}
```

</details>

---


### Tool result

_source line 485 · 2026-05-25T21:16:48.785159+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 7139
}
```

</details>

---


### Tool result

_source line 486 · 2026-05-25T21:16:50.500923+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 7822
}
```

</details>

---


### Tool result

_source line 487 · 2026-05-25T21:16:50.553340+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 7368
}
```

</details>

---


### Tool result

_source line 488 · 2026-05-25T21:16:56.039954+00:00_

# ARR Reviewer Scoring Guidelines

Based on the ARR Reviewer Guidelines document, here's what reviewers are asked to provide:

## Three Primary Scores

**1. Soundness**
Reviewers assess whether work is technically correct and methodologically valid. The guidelines emphasize that "soundness scores must be justified by the text of the review." Low soundness ratings require explicit problems identified in the evaluation.

**2. Excitement**
This reflects personal interest separate from technical merit. The document notes this is "orthogonal to the assessment of the soundness of the paper" and that excitement "do not necessarily come with explicit reasons."

**3. Overall Assessment**
Described as "an explicit recommendation for the outcome," this composite score reflects "soundness, excitement, and also other factors like novelty and impact." The guidelines clarify that papers can deserve acceptance despite lower personal excitement if they offer significant contributions to their target communities.

## Additional Scoring Elements

The document mentions a **confidence score**, though specific scale details aren't provided in the excerpt.

## Key Evaluation Criteria

Reviewers should assess:
- Technical soundness and proof validity
- Novelty and contribution significance
- Appropriate scope of claims
- Experimental rigor and statistical validity
- Reproducibility and clarity
- Ethical considerations
- Professional tone and constructive feedback

The guidelines emphasize that scores must align with review justifications, avoiding unconscious biases.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 10388
}
```

</details>

---


### Tool call

_source line 489 · 2026-05-25T21:17:21.000641+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/submitted.pdf",
  "project": "gated_mfrm_judge_bias",
  "pages": "11-18",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/submitted.pdf",
    "project": "gated_mfrm_judge_bias",
    "pages": "11-18",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 490 · 2026-05-25T21:17:23.110458+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 435.2}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 445.6}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 443.2}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 447.9}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.3}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 448.9}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 399.3}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 21.3}], \"total_pages\": 18, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2109
}
```

</details>

---


### Tool call

_source line 491 · 2026-05-25T21:17:23.236081+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ARR review form with all scoring dimensions, their exact scales, and descriptions for each level. Include: Overall Assessment scale (1-5), Soundness scale, Excitement/Novelty scale, Confidence scale, Reproducibility, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete ARR review form with all scoring dimensions, their exact scales, and descriptions for each level. Include: Overall Assessment scale (1-5), Soundness scale, Excitement/Novelty scale, Confidence scale, Reproducibility, and any other dimensions."
  }
}
```

</details>

---


### Tool result

_source line 492 · 2026-05-25T21:17:30.018689+00:00_

# ARR Review Form Scoring Dimensions

## Reviewer Confidence (1-5 scale)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## Soundness (1-5 scale with half-points)
- **5**: "Excellent: This study is one of the most thorough I have seen."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## Excitement/Novelty (1-5 scale with half-points)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

## Overall Assessment (1-5 scale with half-points)
- **5**: "Consider for Award"
- **4**: "Conference: I think this paper could be accepted"
- **3**: "Findings: I think this paper could be accepted to Findings of the ACL"
- **2**: "Resubmit next cycle"
- **1**: "Do not resubmit"

## Reproducibility (1-5 scale)
- **5**: "They could easily reproduce the results."
- **4**: "They could mostly reproduce the results."
- **3**: "They could reproduce the results with some difficulty."
- **2**: "They would be hard pressed to reproduce the results."
…[truncated 339 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6782
}
```

</details>

---


### Tool call

_source line 493 · 2026-05-25T21:17:33.782443+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 494 · 2026-05-25T21:17:34.844406+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1061
}
```

</details>

---


### Tool call

_source line 495 · 2026-05-25T21:17:34.995278+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 496 · 2026-05-25T21:17:35.354719+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 497 · 2026-05-25T21:17:38.571867+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3576
}
```

</details>

---


### Tool result

_source line 498 · 2026-05-25T21:17:38.572760+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3218
}
```

</details>

---


### Tool call

_source line 499 · 2026-05-25T21:17:39.124874+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 500 · 2026-05-25T21:17:39.780207+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 501 · 2026-05-25T21:17:40.045562+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 920
}
```

</details>

---


### Tool call

_source line 502 · 2026-05-25T21:17:40.500573+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool call

_source line 503 · 2026-05-25T21:17:40.500957+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool call

_source line 504 · 2026-05-25T21:17:40.501189+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 505 · 2026-05-25T21:17:40.551927+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 506 · 2026-05-25T21:17:41.761318+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1981
}
```

</details>

---


### Tool result

_source line 507 · 2026-05-25T21:17:41.966262+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1465
}
```

</details>

---


### Tool result

_source line 508 · 2026-05-25T21:17:42.068440+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1567
}
```

</details>

---


### Tool call

_source line 509 · 2026-05-25T21:19:08.392482+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/main.tex",
  "limit": "120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/main.tex",
    "limit": "120"
  }
}
```

</details>

---


### Tool result

_source line 510 · 2026-05-25T21:19:09.247007+00:00_

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
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{amsthm}
14	\usepackage{booktabs}
15	\usepackage{xcolor}
16	\usepackage{subcaption}
17	
18	\newtheorem{observation}{Observation}
19	\newtheorem{proposition}{Proposition}
20	\newtheorem{theorem}{Theorem}
21	\newtheorem{corollary}{Corollary}
22	
23	\graphicspath{{../../figures/paper/}}
24	
25	\title{Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model\\for Disentangling Judge Bias and Contamination in LLM Evaluation}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	\input{abstract}
33	\input{introduction}
34	\input{related_work}
35	\input{background}
36	\input{method}
37	\input{experiments}
38	\input{conclusion}
39	
40	\section*{Limitations}
41	\input{limitations}
42	
43	\bibliography{references}
44	
45	\appendix
46	\input{appendix}
47	
48	\end{document}
49	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 511 · 2026-05-25T21:19:09.247485+00:00_

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
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
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

_source line 512 · 2026-05-25T21:19:09.298007+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 513 · 2026-05-25T21:19:23.836618+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 514 · 2026-05-25T21:19:24.138055+00:00_

1	\begin{abstract}
2	When an LLM judge scores a model response on a benchmark item, the result conflates genuine ability, the judge's scoring tendency, and any advantage from training data exposure. Current evaluation pipelines correct for judge bias and contamination independently, but we show that separate correction is structurally flawed. We formalize this as an omitted variable bias (OVB) problem: any estimator that models one distortion while omitting the other produces systematically biased ability estimates, regardless of correction order. We propose the Gated Many-Facet Rasch Model (G-MFRM), a Bayesian framework that jointly estimates model ability, judge severity, and contamination susceptibility with formal identifiability guarantees. In synthetic experiments ($N = 50$), G-MFRM reduces ability RMSE by 51\% over sequential pipelines ($p < 0.001$) and recovers contamination susceptibility with Pearson $r = 0.81$. On Arena-Hard, G-MFRM provides interpretable per-model contamination diagnostics (in an 8-model pilot, older models exhibit 4--6$\times$ higher susceptibility), and a controlled coverage ablation demonstrates that over-correction decreases from $\Delta\tau = -0.044$ at 46\% coverage to $\Delta\tau = 0$ at full coverage, quantifying exposure estimation requirements for contamination-aware evaluation. Leave-one-out cross-validation confirms improved predictive fit ($|\Delta\mathrm{ELPD}/\mathrm{SE}| = 5.9$)\footnote{Code and data are available at \url{https://anonymous.4open.science/r/gated_mfrm_judge_bias-43CC/}.}.
3	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 515 · 2026-05-25T21:19:24.138548+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 516 · 2026-05-25T21:19:24.490164+00:00_

1	The evaluation uses a single benchmark (Arena-Hard) with an incomplete observation design (${\sim}$58\% fill rate); generalization to other benchmarks and larger model populations remains to be verified. Posterior credible intervals for contamination susceptibility $c_n$ exhibit systematic overconfidence (71\% coverage at nominal 95\%; Appendix~\ref{app:ci_coverage}), a structural issue from the multiplicative coupling and HalfNormal boundary at $c_n = 0$ that warrants simulation-based recalibration. The rank-1 contamination structure assumes a single $c_n$ per model, whereas contamination may be domain-specific (e.g., coding vs.\ reasoning), motivating higher-rank decompositions in future work. The judge panel comprises six models from four provider families; generalization to more homogeneous panels is untested.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 517 · 2026-05-25T21:19:24.590928+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 518 · 2026-05-25T21:19:24.642363+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced G-MFRM, a Bayesian measurement model that jointly estimates model ability, judge severity, and contamination susceptibility within a single inferential framework. The key theoretical contribution is formalizing the confounding between judge bias and benchmark contamination as omitted variable bias: omitting the contamination facet produces systematic bias in ability estimates, driven primarily by the specification error itself rather than the exposure-severity covariance (Section~\ref{sec:confounding}).
5	
6	On Arena-Hard, G-MFRM provides interpretable per-model contamination diagnostics unavailable from existing methods: older models exhibit 4--6$\times$ higher susceptibility, and MFRM-only estimation inflates ability for the most contaminated models by up to 0.79 logits. A controlled coverage ablation ($\Delta\tau$: $-0.044 \to -0.015 \to 0.000$ as coverage increases to 100\%) demonstrates that over-correction is attributable to incomplete exposure estimation, and complete coverage eliminates the over-correction observed in partial-coverage settings. Ablation confirms joint estimation as the dominant contributor: staged estimation doubles ability RMSE.
7	
8	Two practical implications emerge. First, evaluation frameworks that treat judge bias and contamination as independent incur systematic errors; future LLM evaluation should model these facets jointly. Second, the coverage--degradation finding provides an actionable quality requirement for contamination-aware evaluation. For practitioners operating Arena-style evaluations, G-MFRM can serve as a post-hoc calibration layer: given pairwise judgments and exposure estimates, the model produces contamination-adjusted rankings and flags models warranting training data audits. The exposure estimation pipeline (\S\ref{sec:staged}) is modular, so improved contamination detectors can substitute for reference anchoring without modifying the measurement model
…[truncated 286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 519 · 2026-05-25T21:19:48.755614+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper && cat abstract.tex | sed 's/\\\\begin{abstract}//' | sed 's/\\\\end{abstract}//' | sed 's/\\\\[a-zA-Z]*{[^}]*}//g' | sed 's/\\\\[a-zA-Z]*//g' | sed 's/\\$[^$]*\\$//g' | sed 's/[{}]//g' | sed 's/~/ /g' | sed 's/\\\\%/%/g' | tr -s ' ' '\\n' | grep -v '^$' | wc -l",
  "description": "Count abstract words (stripped of LaTeX commands)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper && cat abstract.tex | sed 's/\\\\begin{abstract}//' | sed 's/\\\\end{abstract}//' | sed 's/\\\\[a-zA-Z]*{[^}]*}//g' | sed 's/\\\\[a-zA-Z]*//g' | sed 's/\\$[^$]*\\$//g' | sed 's/[{}]//g' | sed 's/~/ /g' | sed 's/\\\\%/%/g' | tr -s ' ' '\\n' | grep -v '^$' | wc -l",
    "description": "Count abstract words (stripped of LaTeX commands)"
  }
}
```

</details>

---


### Tool call

_source line 520 · 2026-05-25T21:19:48.806296+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 521 · 2026-05-25T21:19:48.958101+00:00_

171
Shell cwd was reset to /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/review_reviewer_2_800cc3c1

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool result

_source line 522 · 2026-05-25T21:19:48.958572+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Judge Bias in LLM Evaluation.}
5	LLM-as-a-judge evaluations exhibit position bias \citep{wang2024positionbias}, self-preference \citep{panickssery2024selffavor}, and other cognitive biases \citep{koo2024cobbler, ye2024justice, bavaresco2025judgebench}; see also \citet{li2024splitmerge} and \citet{fiedler2026bias_uncertainty}. On the correction side, CyclicJudge \citep{cyclicjudge2026} eliminates average bias via round-robin assignment, and UDA \citep{uda2026} learns a neural K-factor reducing inter-judge deviation by 63.4\%. All of these methods model only the judge facet, absorbing contamination effects into ability estimates (Section~\ref{sec:confounding}).
6	
7	\paragraph{Benchmark Contamination Detection and Avoidance.}
8	Detection methods include performance-based tests \citep{constat2024}, unified contamination metrics \citep{dcr2025}, token-level log-probability probes \citep{logprober2024, mink2024}, and guided prompting \citep{golchin2024timetravel, oren2024proving}; see also \citet{deng2024contamination, sainz2023contamination}. \citet{preference_leakage2026} identify judge-side preference leakage, complementary to G-MFRM's examinee-side focus. Avoidance strategies include dynamic benchmarks \citep{livebench2025}, private evaluation \citep{truce2024}, and subset selection \citep{polo2024tinybenchmarks}. G-MFRM instead corrects for residual contamination while simultaneously modeling judge effects.
9	
10	\paragraph{Item Response Theory (IRT) and MFRM for LLM Evaluation.}
11	IRT has been applied to NLP leaderboards for ranking and benchmark analysis \citep{lalor2019irt, rodriguez2021irt, vania2021irt}. The Many-Facet Rasch Model (MFRM) \citep{linacre1989mfrm, linacre1994mfrm} extends IRT to multi-rater settings; \citet{jiao2025mfrm_llm} apply it to LLM judge panels, and \citet{uto2020generalized} and \citet{choi2026irt_judge} propose Bayesian variants; see also \citet{zhou2025psnirt}. The Do
…[truncated 266 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 523 · 2026-05-25T21:20:04.295561+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex"
  }
}
```

</details>

---


### Tool call

_source line 524 · 2026-05-25T21:20:04.296507+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 525 · 2026-05-25T21:20:04.347001+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{fig5_6_combined}
7	\caption{Contamination diagnostics ($N = 8$ pilot, 9 judges). (a)~Contamination susceptibility $\hat{c}_n$ (posterior mean $\pm$ 95\% CI), ordered by magnitude. Older models (GPT-3.5-Turbo, GPT-4-0613) show 4--6$\times$ higher susceptibility than recent models (GPT-4o). (b)~Ability bias absorbed by MFRM-only estimation: $\Delta\theta = \hat{\theta}_{\mathrm{MFRM}} - \hat{\theta}_{\mathrm{G\text{-}MFRM}}$. The monotonic relationship (Spearman $\rho = 1.0$; $N = 8$, interpret with caution) confirms that contamination inflates MFRM ability estimates for high-$c_n$ models, as predicted by the OVB analysis (Section~\ref{sec:confounding}).}
8	\label{fig:contamination_and_bias}
9	\end{figure*}
10	
11	\subsection{Setup}
12	\label{sec:setup}
13	
14	Our main experiment uses $N = 17$ target models evaluated by 6 LLM judges; a smaller $N = 8$ pilot with 9 judges validates sample-size effects. Table~\ref{tab:main_results} reports both configurations as part of the coverage analysis.
15	
16	\paragraph{Data and models.} We evaluate on Arena-Hard \citep{li2024arenahard}, a benchmark of 500 multi-turn conversational items selected for high separability among frontier models. The evaluation uses all 500 items in a connected incomplete design (${\sim}$58\% fill rate of the $N \times I \times J$ tensor). Seventeen target models spanning proprietary and open-source families are evaluated: GPT-4o, GPT-4o-mini, Qwen2.5-72B, LLaMA-3.3-70B, Qwen3-8B, Gemma-2-9B, GPT-4-0613, GPT-3.5-Turbo, Claude-3.5-Sonnet, GPT-4-Turbo, LLaMA-3.1-70B, Gemma-2-27B, Claude-3-Opus, LLaMA-3-70B, Mixtral-8x22B, Claude-3-Haiku, and LLaMA-3-8B. Ground-truth rankings are derived from Chatbot Arena human preference data \citep{zheng2023mtbench}.
17	
18	\paragraph{Judges.} Six LLM judges score responses in position-swapped pairwise mode: Claude Sonnet 4.6, DeepSeek-V4-Pro, Gem
…[truncated 8253 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 526 · 2026-05-25T21:20:04.347397+00:00_

1	\section{Confounding in LLM Evaluation}
2	\label{sec:confounding}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{fig2_ovb_bias}
7	\caption{Sequential estimation bias ($\hat{\theta}_{\mathrm{seq}} - \theta_{\mathrm{true}}$) versus true contamination susceptibility $c_n$. Pearson $r = 0.80$ ($p < 0.001$) confirms systematic overestimation of contaminated models. Synthetic data: $N = 50$, $I = 100$, $J = 8$.}
8	\label{fig:ovb_bias}
9	\end{figure}
10	
11	The Many-Facet Rasch Model (MFRM) extends classical Rasch measurement to settings with multiple rater facets \citep{linacre1989mfrm, linacre1994mfrm}. Originating in educational measurement, the model treats rater variation as a nuisance facet to be estimated and removed rather than a source of noise to be averaged over. In the LLM evaluation context, where $J$ judges score $N$ models across $I$ items, the MFRM specifies
12	%
13	\begin{equation}
14	\label{eq:mfrm}
15	\log \frac{P(Y_{nij} \geq k \mid \theta_n, b_i, d_j, \gamma_k)}{P(Y_{nij} < k \mid \theta_n, b_i, d_j, \gamma_k)} = \theta_n - b_i - d_j - \gamma_k,
16	\end{equation}
17	%
18	where $Y_{nij}$ is the ordinal rating by judge $j$ for model $n$ on item $i$, $\theta_n$ is the ability of model $n$ ($n = 1, \ldots, N$), $b_i$ is the difficulty of item $i$ ($i = 1, \ldots, I$), $d_j$ is the severity of judge $j$ ($j = 1, \ldots, J$), and $\gamma_k$ is the threshold for category $k$. All facets reside on a common logit scale, so model ability is directly comparable after adjustment for item difficulty and judge severity. \citet{jiao2025mfrm_llm} applied this framework to compare ten LLM raters with human experts and showed that MFRM separates genuine ability from systematic judge effects in multi-judge panels.
19	
20	However, standard MFRM assumes that all systematic sources of score variation are captured by the modeled facets. This assumption breaks down when some models have been exposed to benchmark items during training \citep{dcr20
…[truncated 3804 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 527 · 2026-05-25T21:20:09.515856+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 528 · 2026-05-25T21:20:09.516481+00:00_

1	\section{The G-MFRM Framework}
2	\label{sec:method}
3	
4	Section~\ref{sec:confounding} established that omitting contamination from the measurement model produces directional bias in ability estimates (Observation~\ref{obs:ovb}). We now introduce the Gated Many-Facet Rasch Model (G-MFRM), which jointly estimates ability, judge severity, and contamination susceptibility within a single measurement framework. The key design choices, staged estimation with externally fixed exposure and a hierarchical HalfNormal prior for the contamination term, are motivated by the identifiability analysis in \S\ref{sec:identifiability} and the error propagation bounds in \S\ref{sec:error_prop}.
5	
6	\subsection{Model Specification}
7	\label{sec:model_spec}
8	
9	G-MFRM extends the standard MFRM \citep{linacre1989mfrm, linacre1994mfrm} by adding a multiplicative contamination gating term to the linear predictor (Eq.~\ref{eq:mfrm}):
10	%
11	\begin{equation}
12	\label{eq:gmfrm}
13	\log \frac{P(Y_{nij} \geq k)}{P(Y_{nij} < k)} = \theta_n - b_i - d_j - \gamma_k + c_n \cdot e_i,
14	\end{equation}
15	%
16	where all terms carry the definitions from Section~\ref{sec:confounding}. The gating structure $c_n \cdot e_i$ separates model-specific contamination susceptibility ($c_n \geq 0$) from item-specific exposure ($e_i \in [0,1]$). When $c_n = 0$ or $e_i = 0$, the gating term vanishes and Eq.~\ref{eq:gmfrm} reduces to the standard MFRM.
17	
18	We enforce non-negativity and sparsity through a hierarchical HalfNormal prior: $\sigma_c \sim \text{HalfNormal}(1.0)$, $c^{\mathrm{raw}}_n \sim \text{HalfNormal}(1.0)$, $c_n = c^{\mathrm{raw}}_n \cdot \sigma_c$. The hierarchical structure provides adaptive shrinkage: when data support low contamination, $\sigma_c$ contracts toward zero. The remaining priors are $\theta_n \sim \mathcal{N}(0, 1)$, $b_i \sim \mathcal{N}(0, 1)$, $d_j \sim \mathcal{N}(0, 0.5)$, and uniform on $\gamma_k$.
19	
20	G-MFRM extends the Doubly-Gated IRT model of \citet{shu2013dgirt}
…[truncated 5934 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 529 · 2026-05-25T21:22:23.681832+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/review_round_5/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 530 · 2026-05-25T21:22:23.732411+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 531 · 2026-05-25T21:24:18.181364+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — 新颖性与完整性审查\n\n### Paper Summary\n\n本文提出 G-MFRM（Gated Many-Facet Rasch Model），将标准 MFRM 扩展为联合估计模型能力 θ_n、评委严格度 d_j 和 contamination susceptibility c_n 的贝叶斯框架。核心理论论点是：分别校正评委偏差和数据污染会产生遗漏变量偏差（OVB），因此必须联合建模。框架采用三阶段估计（标准 MFRM → 外部 exposure 估计 → Joint MCMC）。合成数据上 RMSE 降低 51%；在 Arena-Hard 上对 17 个模型和 6 个评委提供 per-model contamination 诊断。\n\n---\n\n## 总体评分\n**Overall**: 3.0 / 5（Findings）\n**一句话总结**: 问题定位准确、框架设计规范，但核心实验仅覆盖单一 benchmark 且 contamination 验证缺乏独立证据，主实验排名准确度反而低于所有 baseline，尚不足以支撑主会议接收。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0 / 5 | 方法论整体合理，OVB 形式化和 identifiability 证明自洽；但 c_n 验证存在循环性（仅 model age proxy），e_i 估计缺乏 ground truth 验证，主实验 τ 低于所有 baseline |\n| Excitement | 3.0 / 5 | 联合建模 judge bias 与 contamination 是有价值的方向，但单 benchmark 实验和 ranking 退化削弱了实际影响力 |\n| Reproducibility | 4 / 5 | 匿名代码已提供，MCMC 设置（NUTS, 6000+4000×4 chains, R̂<1.05, ESS>100）描述清晰，合成数据生成可复现 |\n| Confidence | 4 / 5 | 本人熟悉 IRT/MFRM、贝叶斯推断和 LLM 评估领域，仔细阅读了全文含 18 页 appendix |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 单一 benchmark 无法支撑标题和 abstract 中的通用性声明\n- 具体位置：Section 5.1、Title、Abstract\n- 问题：全部真实数据实验仅使用 Arena-Hard（500 条多轮对话 item）。论文标题和 abstract 使用 \"LLM Evaluation\" 这一泛化表述，暗示方法适用于各类评估场景。但不同 benchmark 的 contamination 模式差异巨大：选择题（MMLU）vs. 开放生成（Arena-Hard）vs. 代码（HumanEval）的 exposure 特征完全不同，e_i 估计 pipeline（reference model anchoring + cross-model agreement）在非对话式 benchmark 上的行为未知。\n- 为什么影响接收：Generalizability 是 EMNLP 主会议的核心要求。仅在一个 benchmark 上验证的方法难以支撑 \"for LLM Evaluation\" 的定位。Limitations 虽有提及但不足以弥补证据缺口。\n- 建议修改方向：至少增加 1-2 个不同类型的 benchmark（如 MMLU 或 GSM8K）验证 G-MFRM 的适用性，或将标题/claims 限定为 \"conversational/open-ended evaluation\"。\n\n**N2** [critical] c_n 验证存在循环性，缺乏独立外部验证\n- 具体位置：Section 5.2（Contamination diagnostics 段落）、Figure 5\n- 问题：c_n 的验证逻辑是 \"older models have higher c_n → aligns with expectations → therefore c_n captures contamination\"。这是 face validity，不是 rigorous validation。具体问题：\n  (1) model age 与多种因素共变（架构复杂度、训练数据量、RLHF 质量），无法区分 c_n 是否真正捕获 contamination 还是其他 age-correlated effect；\n  (2) Stage 2 的 exposure 估计使用 gpt-4-0314（本身是老模型）作为 reference anchor，可能引入系统性偏差；\n  (3) N=8 pilot 的 Spearman ρ = 1.0 被论文自身承认 \"not statistically remarkable\"（line 66, experiments.tex），但仍作为叙事支撑。\n  (4) 没有对比独立 contamination indicator（如 membership inference attack、n-gram overlap、memorization probe）来交叉验证 c_n 的含义。\n- 为什么影响接收：如果 c_n 并非 contamination 而是 model age 的 proxy，则 G-MFRM 的核心 value proposition（disentangling contamination）不成立。\n- 建议修改方向：(a) 使用已知被 contaminate 的 item subset（如通过 n-gram match 确认的 item）验证 c_n 是否对这些 item 的 score inflation 更敏感；(b) 在 contamination 已知为 absent 的 benchmark 上验证 c_n ≈ 0；(c) 对比 independent contamination metrics（如 Min-K%）与 c_n 的一致性。\n\n**N3** [critical] 主实验排名准确度低于所有 baseline，解释虽合理但替代假说未被排除\n- 具体位置：Table 1、Section 5.2（Exposure coverage 段落）\n- 问题：N=17 主实验中，G-MFRM 的 Kendall τ = 0.794，Δτ = −0.044，是所有方法中最差的。全部 7 个 baseline 的 τ 均在 raw average（0.838）的 ±0.015 范围内。论文的解释是 \"incomplete exposure coverage (46%) 导致 over-correction\"，并通过 coverage ablation（Δτ: −0.044 → −0.015 → 0.000）支撑。\n  然而，替代假说同样成立：Arena-Hard 上的 contamination 信号太弱以至于不影响排名，G-MFRM 通过不必要的修正引入了噪声。Coverage ablation 的 Δτ → 0 同时兼容两种解释——既可能是修正越来越准确，也可能是限制到高信噪比 item 后噪声被抑制。\n  论文未提供 discriminating evidence 区分这两种假说。\n- 为什么影响接收：如果在 practitioner 最关心的指标上表现更差，且无法排除\"方法引入噪声\"的解释，说服力严重不足。\n- 建议修改方向：(a) 在 coverage ablation 中增加 placebo test：用 random e_i 替代真实 e_i，如果 Δτ 同样改善则支持噪声假说；(b) 展示 G-MFRM 在 synthetic data 上 coverage < 50% 时的行为，确认 real data 退化是否与 synthetic predictions 一致；(c) 报告 individual model ranking changes 而非仅聚合 τ。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] OVB 形式化是教科书应用而非原创贡献\n- 具体位置：Section 3、Observation 1（Eq. 3）\n- 问题：Observation 1 直接将 Angrist & Pischke (2009) 的 OVB 公式应用到 MFRM 的线性预测器上。论文诚实地在脚注中承认 \"The OVB formula is exact for linear models. We apply it to the MFRM linear predictor η, which is an approximation\"（background.tex, line 34 footnote）。虽然 Pearson r = 0.80 支持近似质量，但这是标准计量经济学工具的领域应用，而非方法论创新。Contributions list 中称之为 \"a formal analysis\" 略有过度宣称。\n- 建议：在 contributions list 中将措辞调整为 \"We apply the OVB framework to characterize...\" 而非暗示原创形式化。\n\n**W2** [warning] N=8 pilot 统计效力不足以支撑 contamination diagnostics 的叙事权重\n- 具体位置：Figure 5、Section 5.2 中大量基于 N=8 的分析\n- 问题：N=8 的 posterior 估计 credible interval 很宽（Figure 5a 可见），Spearman ρ = 1.0 在 N=8 下的显著性有限。论文在 pilot 上构建了大量叙事（contamination gradient by model age、ability bias absorption、LOO ELPD），但统计效力不足以使这些发现 robust。N=17 分析的 contamination 结果（GPT-3.5-Turbo: 2.57, GPT-4-0613: 3.78）与 N=8 不一致（5.60, 4.20），论文用 \"shrinkage from larger population\" 解释，但也可能反映估计不稳定。\n- 建议：减少对 N=8 pilot 的叙事依赖，将 N=17 分析作为主要证据；或明确标注 pilot 仅为 exploratory/illustrative。\n\n**W3** [warning] e_i 估计 pipeline 缺乏 ground truth 验证\n- 具体位置：Section 4.2（Stage 2）、Appendix K（weight robustness）\n- 问题：Appendix K 展示不同权重配置下 e_i 的 Spearman ρ ≥ 0.998，但这只说明不同权重产生类似 e_i 排序——不说明 e_i 是否准确度量了真实 exposure。没有对比已知 contaminated items（如通过 memorization probe 确认的 items）来验证 e_i 的准确性。Figure 11（Appendix R）展示 e_i recovery on synthetic data，但 synthetic data 的 e_i 生成过程与真实 exposure 机制差异很大。\n- 建议：如果有已知 contamination 的 item subset，报告 e_i 在这些 items 上的 precision/recall。\n\n**W4** [warning] Ground truth（Chatbot Arena 排名）本身存在偏差\n- 具体位置：Section 5.1（Data and models 段落）\n- 问题：Kendall τ 是 against Chatbot Arena human preference data 计算的，但 Arena 排名本身受 position bias、response length bias、demographic bias 影响。G-MFRM 的排名\"准确度\"实际上衡量的是与另一个 biased ranking system 的一致性，而非与 ground truth ability 的一致性。Limitations 未讨论此点。\n- 建议：增加讨论 ground truth 选择的局限性，或考虑使用多个 reference ranking 的平均。\n\n**W5** [warning] Table 1 caption 中 \"seven baselines\" 的列举不完整\n- 具体位置：Table 1 caption\n- 问题：Caption 括号中只列出 5 个名称（MFRM-only, Sequential, CyclicJudge, DCR Factor, Pref. Leakage），但声称 \"all seven baselines\"。虽然正文（Section 5.2）完整列出了 7 个（加上 Raw Average 和 CyclicJudge+discard），但读者可能只看表格不看正文，造成困惑。更重要的是，Table 1 本身只展示了 G-MFRM 的结果，没有 per-baseline 的 τ 值，读者无法验证 \"within 0.015\" 的声明。\n- 建议：(a) 在 Table 1 中增加至少几个代表性 baseline 的 τ 值；(b) 或在 appendix 提供完整 baseline comparison table。\n\n---\n\n## 小问题（不影响接收）\n\n- Abstract 字数约 185 词，符合 ARR ≤200 要求。\n- 匿名性合规：作者为 \"Anonymous\"，代码使用 anonymous.4open.science。\n- 正文 8 页 + Limitations 在正文内（page 8）→ 格式合规。\n- Limitations 覆盖 3 个点（单 benchmark、CI overconfidence、rank-1 contamination），篇幅适当。\n- Section 6 Conclusion 部分与 abstract 有较多重复内容，可考虑精简 Conclusion 并增加更多 forward-looking insight。\n- Figure 1(b) pipeline 可视化清晰有效，是全文最佳图之一。\n- 两个模型同时作为 judge 和 target（Qwen2.5-72B, LLaMA-3.3-70B），虽然 d_j 吸收了 self-evaluation bias 且有 robustness check（Appendix H），但应在主文 Setup 中更显著地提及这一 concern。\n\n---\n\n## 对作者的提问\n\n1. 能否提供 c_n 与独立 contamination indicator（如 Min-K%、n-gram overlap）的交叉验证？\n2. 在已知无 contamination 的 benchmark 上，G-MFRM 是否正确估计 c_n ≈ 0 for all models？\n3. Coverage ablation 中 Δτ → 0 如何排除\"限制到高信噪比 item 后噪声被抑制\"的替代解释？建议增加 random e_i placebo test。\n4. N=8 与 N=17 的 c_n 估计值差异较大（GPT-3.5-Turbo: 5.60 vs 2.57），除 shrinkage 外是否有其他解释？\n5. 为什么 N=17 使用 6 judges 而 N=8 pilot 使用 9 judges？不同 panel 组成如何影响 c_n 估计？\n\n---\n\n## 可能遗漏的参考文献\n\n- 论文 Related Work 覆盖较完整，主要工作（CyclicJudge, UDA, Preference Leakage, DG-IRT, MFRM 系列）均已引用。\n- 建议检查是否有 2025-2026 年发表的 IRT-for-LLM 新工作遗漏（如 Batsuren et al. 2024 \"Evaluating LLMs with Item Response Theory\" 等）。\n- Stureborg et al. (2024) \"Large Language Models are Inconsistent and Biased Evaluators\" 可能值得引用，与 judge bias 讨论相关。\n\n---\n\n## 主要优势\n\n1. **问题定位精准**：首次将 judge bias 与 contamination 的交互建模为 OVB 问题，为联合建模提供了清晰的理论动机。\n2. **框架设计规范**：三阶段估计、identifiability 分析（Theorem 1）和 error propagation bounds 构成完整的理论体系。\n3. **诚实透明的报告**：论文不隐藏主实验 ranking 退化（Δτ = −0.044），通过 coverage ablation 提供合理解释，Limitations 讨论到位。\n4. **丰富的 appendix**：18 页 appendix 覆盖证明、robustness check、posterior predictive check、judge count sensitivity 等，体现实验严谨性。\n5. **实用性**：G-MFRM 作为 post-hoc calibration layer 的定位清晰，exposure pipeline 模块化设计允许替换不同的 contamination detector。\n\n---\n\n**最终判断**：问题重要、框架合理，但 (1) 单 benchmark 实验 (2) c_n 验证循环性 (3) 主实验 ranking 退化 三个 critical issue 需要在下一轮修改中解决。当前适合 Findings 接收，距 main conference 接收需补充多 benchmark 验证和独立 c_n validation。",
  "reviewer_id": "2",
  "project": "gated_mfrm_judge_bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — 新颖性与完整性审查\n\n### Paper Summary\n\n本文提出 G-MFRM（Gated Many-Facet Rasch Model），将标准 MFRM 扩展为联合估计模型能力 θ_n、评委严格度 d_j 和 contamination susceptibility c_n 的贝叶斯框架。核心理论论点是：分别校正评委偏差和数据污染会产生遗漏变量偏差（OVB），因此必须联合建模。框架采用三阶段估计（标准 MFRM → 外部 exposure 估计 → Joint MCMC）。合成数据上 RMSE 降低 51%；在 Arena-Hard 上对 17 个模型和 6 个评委提供 per-model contamination 诊断。\n\n---\n\n## 总体评分\n**Overall**: 3.0 / 5（Findings）\n**一句话总结**: 问题定位准确、框架设计规范，但核心实验仅覆盖单一 benchmark 且 contamination 验证缺乏独立证据，主实验排名准确度反而低于所有 baseline，尚不足以支撑主会议接收。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0 / 5 | 方法论整体合理，OVB 形式化和 identifiability 证明自洽；但 c_n 验证存在循环性（仅 model age proxy），e_i 估计缺乏 ground truth 验证，主实验 τ 低于所有 baseline |\n| Excitement | 3.0 / 5 | 联合建模 judge bias 与 contamination 是有价值的方向，但单 benchmark 实验和 ranking 退化削弱了实际影响力 |\n| Reproducibility | 4 / 5 | 匿名代码已提供，MCMC 设置（NUTS, 6000+4000×4 chains, R̂<1.05, ESS>100）描述清晰，合成数据生成可复现 |\n| Confidence | 4 / 5 | 本人熟悉 IRT/MFRM、贝叶斯推断和 LLM 评估领域，仔细阅读了全文含 18 页 appendix |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 单一 benchmark 无法支撑标题和 abstract 中的通用性声明\n- 具体位置：Section 5.1、Title、Abstract\n- 问题：全部真实数据实验仅使用 Arena-Hard（500 条多轮对话 item）。论文标题和 abstract 使用 \"LLM Evaluation\" 这一泛化表述，暗示方法适用于各类评估场景。但不同 benchmark 的 contamination 模式差异巨大：选择题（MMLU）vs. 开放生成（Arena-Hard）vs. 代码（HumanEval）的 exposure 特征完全不同，e_i 估计 pipeline（reference model anchoring + cross-model agreement）在非对话式 benchmark 上的行为未知。\n- 为什么影响接收：Generalizability 是 EMNLP 主会议的核心要求。仅在一个 benchmark 上验证的方法难以支撑 \"for LLM Evaluation\" 的定位。Limitations 虽有提及但不足以弥补证据缺口。\n- 建议修改方向：至少增加 1-2 个不同类型的 benchmark（如 MMLU 或 GSM8K）验证 G-MFRM 的适用性，或将标题/claims 限定为 \"conversational/open-ended evaluation\"。\n\n**N2** [critical] c_n 验证存在循环性，缺乏独立外部验证\n- 具体位置：Section 5.2（Contamination diagnostics 段落）、Figure 5\n- 问题：c_n 的验证逻辑是 \"older models have higher c_n → aligns with expectations → therefore c_n captures contamination\"。这是 face validity，不是 rigorous validation。具体问题：\n  (1) model age 与多种因素共变（架构复杂度、训练数据量、RLHF 质量），无法区分 c_n 是否真正捕获 contamination 还是其他 age-correlated effect；\n  (2) Stage 2 的 exposure 估计使用 gpt-4-0314（本身是老模型）作为 reference anchor，可能引入系统性偏差；\n  (3) N=8 pilot 的 Spearman ρ = 1.0 被论文自身承认 \"not statistically remarkable\"（line 66, experiments.tex），但仍作为叙事支撑。\n  (4) 没有对比独立 contamination indicator（如 membership inference attack、n-gram overlap、memorization probe）来交叉验证 c_n 的含义。\n- 为什么影响接收：如果 c_n 并非 contamination 而是 model age 的 proxy，则 G-MFRM 的核心 value proposition（disentangling contamination）不成立。\n- 建议修改方向：(a) 使用已知被 contaminate 的 item subset（如通过 n-gram match 确认的 item）验证 c_n 是否对这些 item 的 score inflation 更敏感；(b) 在 contamination 已知为 absent 的 benchmark 上验证 c_n ≈ 0；(c) 对比 independent contamination metrics（如 Min-K%）与 c_n 的一致性。\n\n**N3** [critical] 主实验排名准确度低于所有 baseline，解释虽合理但替代假说未被排除\n- 具体位置：Table 1、Section 5.2（Exposure coverage 段落）\n- 问题：N=17 主实验中，G-MFRM 的 Kendall τ = 0.794，Δτ = −0.044，是所有方法中最差的。全部 7 个 baseline 的 τ 均在 raw average（0.838）的 ±0.015 范围内。论文的解释是 \"incomplete exposure coverage (46%) 导致 over-correction\"，并通过 coverage ablation（Δτ: −0.044 → −0.015 → 0.000）支撑。\n  然而，替代假说同样成立：Arena-Hard 上的 contamination 信号太弱以至于不影响排名，G-MFRM 通过不必要的修正引入了噪声。Coverage ablation 的 Δτ → 0 同时兼容两种解释——既可能是修正越来越准确，也可能是限制到高信噪比 item 后噪声被抑制。\n  论文未提供 discriminating evidence 区分这两种假说。\n- 为什么影响接收：如果在 practitioner 最关心的指标上表现更差，且无法排除\"方法引入噪声\"的解释，说服力严重不足。\n- 建议修改方向：(a) 在 coverage ablation 中增加 placebo test：用 random e_i 替代真实 e_i，如果 Δτ 同样改善则支持噪声假说；(b) 展示 G-MFRM 在 synthetic data 上 coverage < 50% 时的行为，确认 real data 退化是否与 synthetic predictions 一致；(c) 报告 individual model ranking changes 而非仅聚合 τ。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] OVB 形式化是教科书应用而非原创贡献\n- 具体位置：Section 3、Observation 1（Eq. 3）\n- 问题：Observation 1 直接将 Angrist & Pischke (2009) 的 OVB 公式应用到 MFRM 的线性预测器上。论文诚实地在脚注中承认 \"The OVB formula is exact for linear models. We apply it to the MFRM linear predictor η, which is an approximation\"（background.tex, line 34 footnote）。虽然 Pearson r = 0.80 支持近似质量，但这是标准计量经济学工具的领域应用，而非方法论创新。Contributions list 中称之为 \"a formal analysis\" 略有过度宣称。\n- 建议：在 contributions list 中将措辞调整为 \"We apply the OVB framework to characterize...\" 而非暗示原创形式化。\n\n**W2** [warning] N=8 pilot 统计效力不足以支撑 contamination diagnostics 的叙事权重\n- 具体位置：Figure 5、Section 5.2 中大量基于 N=8 的分析\n- 问题：N=8 的 posterior 估计 credible interval 很宽（Figure 5a 可见），Spearman ρ = 1.0 在 N=8 下的显著性有限。论文在 pilot 上构建了大量叙事（contamination gradient by model age、ability bias absorption、LOO ELPD），但统计效力不足以使这些发现 robust。N=17 分析的 contamination 结果（GPT-3.5-Turbo: 2.57, GPT-4-0613: 3.78）与 N=8 不一致（5.60, 4.20），论文用 \"shrinkage from larger population\" 解释，但也可能反映估计不稳定。\n- 建议：减少对 N=8 pilot 的叙事依赖，将 N=17 分析作为主要证据；或明确标注 pilot 仅为 exploratory/illustrative。\n\n**W3** [warning] e_i 估计 pipeline 缺乏 ground truth 验证\n- 具体位置：Section 4.2（Stage 2）、Appendix K（weight robustness）\n- 问题：Appendix K 展示不同权重配置下 e_i 的 Spearman ρ ≥ 0.998，但这只说明不同权重产生类似 e_i 排序——不说明 e_i 是否准确度量了真实 exposure。没有对比已知 contaminated items（如通过 memorization probe 确认的 items）来验证 e_i 的准确性。Figure 11（Appendix R）展示 e_i recovery on synthetic data，但 synthetic data 的 e_i 生成过程与真实 exposure 机制差异很大。\n- 建议：如果有已知 contamination 的 item subset，报告 e_i 在这些 items 上的 precision/recall。\n\n**W4** [warning] Ground truth（Chatbot Arena 排名）本身存在偏差\n- 具体位置：Section 5.1（Data and models 段落）\n- 问题：Kendall τ 是 against Chatbot Arena human preference data 计算的，但 Arena 排名本身受 position bias、response length bias、demographic bias 影响。G-MFRM 的排名\"准确度\"实际上衡量的是与另一个 biased ranking system 的一致性，而非与 ground truth ability 的一致性。Limitations 未讨论此点。\n- 建议：增加讨论 ground truth 选择的局限性，或考虑使用多个 reference ranking 的平均。\n\n**W5** [warning] Table 1 caption 中 \"seven baselines\" 的列举不完整\n- 具体位置：Table 1 caption\n- 问题：Caption 括号中只列出 5 个名称（MFRM-only, Sequential, CyclicJudge, DCR Factor, Pref. Leakage），但声称 \"all seven baselines\"。虽然正文（Section 5.2）完整列出了 7 个（加上 Raw Average 和 CyclicJudge+discard），但读者可能只看表格不看正文，造成困惑。更重要的是，Table 1 本身只展示了 G-MFRM 的结果，没有 per-baseline 的 τ 值，读者无法验证 \"within 0.015\" 的声明。\n- 建议：(a) 在 Table 1 中增加至少几个代表性 baseline 的 τ 值；(b) 或在 appendix 提供完整 baseline comparison table。\n\n---\n\n## 小问题（不影响接收）\n\n- Abstract 字数约 185 词，符合 ARR ≤200 要求。\n- 匿名性合规：作者为 \"Anonymous\"，代码使用 anonymous.4open.science。\n- 正文 8 页 + Limitations 在正文内（page 8）→ 格式合规。\n- Limitations 覆盖 3 个点（单 benchmark、CI overconfidence、rank-1 contamination），篇幅适当。\n- Section 6 Conclusion 部分与 abstract 有较多重复内容，可考虑精简 Conclusion 并增加更多 forward-looking insight。\n- Figure 1(b) pipeline 可视化清晰有效，是全文最佳图之一。\n- 两个模型同时作为 judge 和 target（Qwen2.5-72B, LLaMA-3.3-70B），虽然 d_j 吸收了 self-evaluation bias 且有 robustness check（Appendix H），但应在主文 Setup 中更显著地提及这一 concern。\n\n---\n\n## 对作者的提问\n\n1. 能否提供 c_n 与独立 contamination indicator（如 Min-K%、n-gram overlap）的交叉验证？\n2. 在已知无 contamination 的 benchmark 上，G-MFRM 是否正确估计 c_n ≈ 0 for all models？\n3. Coverage ablation 中 Δτ → 0 如何排除\"限制到高信噪比 item 后噪声被抑制\"的替代解释？建议增加 random e_i placebo test。\n4. N=8 与 N=17 的 c_n 估计值差异较大（GPT-3.5-Turbo: 5.60 vs 2.57），除 shrinkage 外是否有其他解释？\n5. 为什么 N=17 使用 6 judges 而 N=8 pilot 使用 9 judges？不同 panel 组成如何影响 c_n 估计？\n\n---\n\n## 可能遗漏的参考文献\n\n- 论文 Related Work 覆盖较完整，主要工作（CyclicJudge, UDA, Preference Leakage, DG-IRT, MFRM 系列）均已引用。\n- 建议检查是否有 2025-2026 年发表的 IRT-for-LLM 新工作遗漏（如 Batsuren et al. 2024 \"Evaluating LLMs with Item Response Theory\" 等）。\n- Stureborg et al. (2024) \"Large Language Models are Inconsistent and Biased Evaluators\" 可能值得引用，与 judge bias 讨论相关。\n\n---\n\n## 主要优势\n\n1. **问题定位精准**：首次将 judge bias 与 contamination 的交互建模为 OVB 问题，为联合建模提供了清晰的理论动机。\n2. **框架设计规范**：三阶段估计、identifiability 分析（Theorem 1）和 error propagation bounds 构成完整的理论体系。\n3. **诚实透明的报告**：论文不隐藏主实验 ranking 退化（Δτ = −0.044），通过 coverage ablation 提供合理解释，Limitations 讨论到位。\n4. **丰富的 appendix**：18 页 appendix 覆盖证明、robustness check、posterior predictive check、judge count sensitivity 等，体现实验严谨性。\n5. **实用性**：G-MFRM 作为 post-hoc calibration layer 的定位清晰，exposure pipeline 模块化设计允许替换不同的 contamination detector。\n\n---\n\n**最终判断**：问题重要、框架合理，但 (1) 单 benchmark 实验 (2) c_n 验证循环性 (3) 主实验 ranking 退化 三个 critical issue 需要在下一轮修改中解决。当前适合 Findings 接收，距 main conference 接收需补充多 benchmark 验证和独立 c_n validation。",
    "reviewer_id": "2",
    "project": "gated_mfrm_judge_bias"
  }
}
```

</details>

---


### Tool result

_source line 532 · 2026-05-25T21:24:22.252766+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4071
}
```

</details>

---


### Assistant

_source line 533 · 2026-05-25T21:24:31.739615+00:00_

审稿报告已提交给 Review Director。

**核心结论**：Overall 3.0/5（Findings），Soundness 3.0，Excitement 3.0，Confidence 4/5。

三个 critical issues：
1. **单 benchmark（Arena-Hard）** 无法支撑标题中 "LLM Evaluation" 的通用性声明
2. **c_n 验证循环性** — 仅用 model age proxy 验证，缺乏独立 contamination indicator 交叉验证
3. **主实验 ranking 退化** — G-MFRM 的 τ = 0.794 低于所有 7 个 baseline（均在 0.838 ± 0.015 内），coverage ablation 的解释虽合理但未排除"引入噪声"的替代假说

主要优势：问题定位精准（OVB 视角）、框架设计规范（identifiability + error propagation）、报告诚实透明。适合 Findings 接收，距 main conference 需补充多 benchmark 验证和独立 c_n validation。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2"
}
```

</details>

---


## Round 17

## Round 17

4 recorded events


### User

_source line 534 · 2026-05-25T21:25:31.265162+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见。请逐条回应，对每个 Must-Fix 和 Should-Fix 问题标注 [AGREE] 或 [REBUT]，并提供理由（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 — 方法严谨性审查

### Overall: 3.5 (Borderline Conference)

### Must-Fix 问题

**N1** [critical] 主实验（N=17）排名准确度系统性低于 baseline，正向结果仅来自统计不显著的小样本 pilot
- Table 1: N=17 的 Δτ = −0.044 / −0.015 / 0.000。N=8 的 Δτ = +0.071 但 bootstrap CI 包含零。
- 标题声称 "Fair Scores via Joint Calibration" 但主实验表明方法在排名任务中无改进甚至有害。正面叙事建立在非显著 pilot 上，存在选择性报告风险。
- 建议：重新定位为诊断工具；或在 N≥17 规模上用完整 exposure 数据重新验证。

**N2** [critical] c_n 置信区间覆盖率仅 67.9–71%，Murphy-Topel 修正未有效解决
- Appendix R: N=8 时 c_n 覆盖率 67.9%，N=50 时 71.3%。Table M 仍以 "95% CI" 标注。
- 对测量模型论文，不确定性量化可靠性是核心质量指标。
- 建议：实现 SBC；报告实际覆盖率对应区间。

**N3** [critical] OVB 线性近似 r=0.80（r²=0.64），36% 方差未解释
- Observation 1 (Eq. 3) 仅对线性模型精确。Taylor 展开推广到 ordinal logit 后 r=0.80。
- 论文承认 "linear approximation serves only as directional motivation" 但以形式化结果呈现。
- 建议：提供近似误差 formal bound；或明确标注 "approximate"。

### Should-Fix 问题

**W1** [warning] MCMC 收敛阈值（R̂<1.05, ESS>100）与引用 Vehtari 2021 标准不一致
- 实际结果满足更严标准（R̂≤1.003, ESS≥1240），但声明阈值偏宽。

**W2** [warning] 42% items underfit（74/176 MNSQ<0.5），未做排除后 sensitivity analysis
- Appendix Q: 176 items 中 92 个 misfitting（52%）。

**W3** [warning] Rank-1 contamination 结构限制性强
- 单一 c_n/model，未按 item category 做残差分析。

**W4** [warning] Murphy-Topel correction 在 N=8 下渐近有效性未验证
- 大样本修正，N=8 下可能失效，未对比有/无 correction 覆盖率。

**W5** [warning] σ_crit ≈ 0.2 阈值推导的 i.i.d. Gaussian 假设
- 实际 exposure 估计误差可能跨 items 相关、非 Gaussian、heteroscedastic。

### Questions
1. N=17 100% coverage 下 G-MFRM 与 raw average τ 相同（0.779），是否意味联合校准对排名无增量价值？
2. Murphy-Topel correction 后 c_n 覆盖率具体是多少？报告的 67.9-71% 是修正前还是修正后？
3. Stage 2 gpt-4-0314 锚点若本身存在 contamination，exposure 估计是否系统性偏倚？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 535 · 2026-05-25T21:27:23.297398+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 对 Reviewer 1 的交叉回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: 主实验排名准确度低于 baseline，正向结果来自非显著 pilot**\n\n同意核心判断。这与我的 N3 一致。补充两点：\n\n(1) 论文确实提供了 LOO-ELPD 证据（|ΔELPD/SE| = 5.9, Section 5.2）表明 G-MFRM 在 observation-level predictive accuracy 上显著优于 MFRM-only，说明 contamination signal 是 real 的。但 LOO-ELPD 衡量的是 individual response 拟合而非 aggregate ranking，两者可以 diverge——论文自己也承认这一点（Section 5.2 \"Reconciling predictive fit and ranking accuracy\" 段落）。\n\n(2) R1 建议\"重新定位为诊断工具\"是合理的。论文的 title \"Fair Scores via Joint Calibration\" 暗示 ranking improvement，但实际最有说服力的贡献是 per-model c_n diagnostics。如果重新定位，N=17 的 coverage ablation 反而成为一个有意义的 negative result：它量化了 exposure estimation 不完整时联合校准的 degradation boundary。\n\n---\n\n**[AGREE] R1-N2: c_n CI 覆盖率仅 67.9–71%，Murphy-Topel 修正未有效解决**\n\n同意。我未在自己的审稿中单独列出此问题，但 R1 的判断合理。具体补充：\n\n- Limitations section 和 Conclusion 均提及 \"71% coverage at nominal 95%\"（Limitations line 1, Conclusion line 10），但 Table 6（Appendix M, page 15）仍以 \"95% CI\" 标注 c_n 区间，未加 caveat。这对读者有误导性。\n- 论文在 Conclusion 中提到 \"simulation-based recalibration (Talts et al., 2018 SBC)\" 作为 future work，但 SBC 是标准实践而非 aspirational target，理应在当前版本实现。\n- 对测量模型论文而言，uncertainty quantification 的可靠性确实是核心质量指标，R1 将其列为 critical 是恰当的。\n\n---\n\n**[REBUT] R1-N3: OVB 线性近似 r=0.80，36% 方差未解释**\n\n部分不同意将此列为 critical。理由：\n\n(1) **论文已明确标注了近似性质**。Background.tex line 42 写道 \"the linear approximation serves only as directional motivation\"；Observation 1 的脚注明确说 \"The OVB formula is exact for linear models. We apply it to the MFRM linear predictor η, which is an approximation\"。论文并未声称 Eq. 3 在非线性 MFRM 下精确成立。\n\n(2) **实际估计不依赖线性近似**。G-MFRM 使用 full nonlinear cumulative logit likelihood（Eq. 4, Section 4.1），OVB 分析仅用于 motivate 为什么联合建模是必要的——即解释 *why* omitting c_n·e_i produces bias，而非用于推导 bias magnitude。r = 0.80 说明线性近似在 direction 上是可靠的（80% of cases bias direction correct），这对 motivation 足够。\n\n(3) **但 R1 关于标注的建议合理**。将 Observation 1 标注为 \"Approximate\" 或在标题中加 \"under linear approximation\" 是低成本改进，可以减少误读。这是 presentation issue 而非 methodological flaw。\n\n**结论：降级为 Should-Fix（presentation fix），而非 Must-Fix。** r=0.80 的近似质量对 directional motivation 足够，但 formal environment（Observation）+ 未加 \"approximate\" 限定词确实可能误导读者。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: MCMC 收敛阈值声明偏宽**\n\n同意，且这是 trivial fix。实际结果（R̂ ≤ 1.003, ESS ≥ 1,240, Section 5.2 line 66）远优于声明阈值（R̂ < 1.05, ESS > 100）。按 Vehtari et al. (2021) 推荐 R̂ < 1.01 更新声明阈值即可。不影响实质结论。\n\n---\n\n**[AGREE] R1-W2: 52% items misfit（92/176），未做排除后 sensitivity analysis**\n\n同意，且这一问题比 R1 评估的 \"warning\" 可能更严重。补充：\n\n- Appendix Q（Table 11, page 16）报告 176 items 中 92 个 flagged（infit MNSQ outside [0.5, 1.5]），其中 74 underfit（MNSQ < 0.5）、18 overfit（MNSQ > 1.5）。52% 的 misfit 率远高于 Rasch 建模的常规可接受范围（通常 <20%）。\n- 大量 underfit（MNSQ < 0.5）意味着这些 items 的 response pattern 比模型预期更 predictable（可能是非常容易或非常难的 items），Rasch 模型可能过度参数化。\n- 关键缺失：没有报告排除 misfitting items 后 θ_n 和 c_n 估计是否稳定。如果排除 52% items 后结果显著变化，则整个分析的 robustness 存疑。\n- 建议将此升级为 critical concern 或至少要求 sensitivity analysis。\n\n---\n\n**[AGREE] R1-W3: Rank-1 contamination 结构限制性强**\n\n同意。论文 Limitations 已提及（\"contamination may be domain-specific (e.g., coding vs. reasoning), motivating higher-rank decompositions\"），但未做任何 empirical investigation。即使不实现 multi-rank 模型，至少可以按 item category 做 residual analysis 检查 rank-1 假设是否合理。Arena-Hard 的 500 items 涵盖多种话题，按 topic cluster 检查 c_n 残差分布是可行的。\n\n---\n\n**[AGREE] R1-W4: Murphy-Topel 在 N=8 下渐近有效性存疑**\n\n同意。Murphy-Topel correction 基于渐近理论（Murphy & Topel, 1985），N=8 model 显然不满足大样本条件。论文在 Appendix D（page 12-13）推导了 correction 公式但未讨论 finite-sample properties。R1 的建议（对比有/无 correction 覆盖率）是验证修正有效性的最低要求。\n\n---\n\n**[AGREE] R1-W5: σ_crit ≈ 0.2 阈值的 i.i.d. Gaussian 假设**\n\n同意。Section 4.4 假设 ε_i ~ N(0, σ²)，但真实 exposure 估计误差可能：(a) 跨 items 相关（同一数据源的 items 误差相关）；(b) 非 Gaussian（exposure 估计可能有 heavy tails）；(c) heteroscedastic（高 exposure items 的估计可能比低 exposure items 更准确）。这些违反使 σ_crit ≈ 0.2 的具体数值不可靠，但 \"error propagation matters\" 的 qualitative message 仍成立。\n\n---\n\n### 对 R1 提问的回应\n\n**Q1: N=17 100% coverage 下 G-MFRM 与 raw average τ 相同（0.779），是否意味联合校准对排名无增量价值？**\n\n好问题。我倾向于认为这确实表明 G-MFRM 在当前 Arena-Hard 设置下对 ranking 的增量价值有限。但有两个 nuance：(a) τ = 0.779 对应的是 exposed-only 231 items subset，这个 subset 的 item 组成不同于 full set，raw average 在这个 subset 上本身就较低（0.779 vs 0.838）；(b) G-MFRM 的价值可能更多体现在 c_n diagnostics 而非 τ improvement。但这强化了 R1-N1 的建议——应重新定位。\n\n**Q2: 67.9–71% 是修正前还是修正后？**\n\n根据我对 Appendix D（Murphy-Topel correction, page 12-13）和 Appendix R（c_n recovery, page 17）的阅读，Appendix R, Figure 12 展示 c_n recovery with \"71% coverage\"。Appendix D 的 Murphy-Topel 修正增大了 variance 估计但具体覆盖率改善幅度未独立报告。R1 要求明确区分修正前/后覆盖率是合理的——如果 71% 已经是修正后，则修正效果很差。\n\n**Q3: gpt-4-0314 anchor 若本身 contaminated，e_i 是否系统偏倚？**\n\n非常好的问题，我的审稿中未涉及。gpt-4-0314 作为 Stage 2 anchor（Section 4.2），其 win-rate residuals 用于估计 item-level exposure。如果 gpt-4-0314 本身对部分 Arena-Hard items exposed，则这些 items 的 e_i 会被系统性低估（anchor 的 high performance 被归因于 ability 而非 contamination），进而导致 c_n 估计偏倚。这是一个比我之前发现的 e_i 验证问题（我的 W3）更根本的 concern。\n\n---\n\n### 总结\n\nR1 的 3 个 Must-Fix 中我同意 2 个（N1, N2），认为 N3 应降级为 Should-Fix（presentation issue）。5 个 Should-Fix 全部同意。R1 的 Q3（anchor contamination）是一个我未发现的重要问题。\n\n综合 R1 和我自己的审稿，核心问题集中在：\n1. **Ranking value**（R1-N1 ≈ R2-N3）：主实验无排名改进\n2. **c_n 验证**（R2-N2 + R1-Q3）：face validity + 潜在 anchor bias\n3. **CI 覆盖率**（R1-N2）：uncertainty quantification 不可靠\n4. **单 benchmark**（R2-N1）：generalizability 不足\n\n这些问题中 (1)(2)(4) 需要新实验数据，(3) 需要实现 SBC。如果 rebuttal 能在 (2) 和 (3) 上提供新证据，并将 framing 调整为 diagnostic tool (1)，论文可升至 3.5 (Borderline Conference)。",
  "reviewer_id": "2",
  "project": "gated_mfrm_judge_bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 对 Reviewer 1 的交叉回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: 主实验排名准确度低于 baseline，正向结果来自非显著 pilot**\n\n同意核心判断。这与我的 N3 一致。补充两点：\n\n(1) 论文确实提供了 LOO-ELPD 证据（|ΔELPD/SE| = 5.9, Section 5.2）表明 G-MFRM 在 observation-level predictive accuracy 上显著优于 MFRM-only，说明 contamination signal 是 real 的。但 LOO-ELPD 衡量的是 individual response 拟合而非 aggregate ranking，两者可以 diverge——论文自己也承认这一点（Section 5.2 \"Reconciling predictive fit and ranking accuracy\" 段落）。\n\n(2) R1 建议\"重新定位为诊断工具\"是合理的。论文的 title \"Fair Scores via Joint Calibration\" 暗示 ranking improvement，但实际最有说服力的贡献是 per-model c_n diagnostics。如果重新定位，N=17 的 coverage ablation 反而成为一个有意义的 negative result：它量化了 exposure estimation 不完整时联合校准的 degradation boundary。\n\n---\n\n**[AGREE] R1-N2: c_n CI 覆盖率仅 67.9–71%，Murphy-Topel 修正未有效解决**\n\n同意。我未在自己的审稿中单独列出此问题，但 R1 的判断合理。具体补充：\n\n- Limitations section 和 Conclusion 均提及 \"71% coverage at nominal 95%\"（Limitations line 1, Conclusion line 10），但 Table 6（Appendix M, page 15）仍以 \"95% CI\" 标注 c_n 区间，未加 caveat。这对读者有误导性。\n- 论文在 Conclusion 中提到 \"simulation-based recalibration (Talts et al., 2018 SBC)\" 作为 future work，但 SBC 是标准实践而非 aspirational target，理应在当前版本实现。\n- 对测量模型论文而言，uncertainty quantification 的可靠性确实是核心质量指标，R1 将其列为 critical 是恰当的。\n\n---\n\n**[REBUT] R1-N3: OVB 线性近似 r=0.80，36% 方差未解释**\n\n部分不同意将此列为 critical。理由：\n\n(1) **论文已明确标注了近似性质**。Background.tex line 42 写道 \"the linear approximation serves only as directional motivation\"；Observation 1 的脚注明确说 \"The OVB formula is exact for linear models. We apply it to the MFRM linear predictor η, which is an approximation\"。论文并未声称 Eq. 3 在非线性 MFRM 下精确成立。\n\n(2) **实际估计不依赖线性近似**。G-MFRM 使用 full nonlinear cumulative logit likelihood（Eq. 4, Section 4.1），OVB 分析仅用于 motivate 为什么联合建模是必要的——即解释 *why* omitting c_n·e_i produces bias，而非用于推导 bias magnitude。r = 0.80 说明线性近似在 direction 上是可靠的（80% of cases bias direction correct），这对 motivation 足够。\n\n(3) **但 R1 关于标注的建议合理**。将 Observation 1 标注为 \"Approximate\" 或在标题中加 \"under linear approximation\" 是低成本改进，可以减少误读。这是 presentation issue 而非 methodological flaw。\n\n**结论：降级为 Should-Fix（presentation fix），而非 Must-Fix。** r=0.80 的近似质量对 directional motivation 足够，但 formal environment（Observation）+ 未加 \"approximate\" 限定词确实可能误导读者。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: MCMC 收敛阈值声明偏宽**\n\n同意，且这是 trivial fix。实际结果（R̂ ≤ 1.003, ESS ≥ 1,240, Section 5.2 line 66）远优于声明阈值（R̂ < 1.05, ESS > 100）。按 Vehtari et al. (2021) 推荐 R̂ < 1.01 更新声明阈值即可。不影响实质结论。\n\n---\n\n**[AGREE] R1-W2: 52% items misfit（92/176），未做排除后 sensitivity analysis**\n\n同意，且这一问题比 R1 评估的 \"warning\" 可能更严重。补充：\n\n- Appendix Q（Table 11, page 16）报告 176 items 中 92 个 flagged（infit MNSQ outside [0.5, 1.5]），其中 74 underfit（MNSQ < 0.5）、18 overfit（MNSQ > 1.5）。52% 的 misfit 率远高于 Rasch 建模的常规可接受范围（通常 <20%）。\n- 大量 underfit（MNSQ < 0.5）意味着这些 items 的 response pattern 比模型预期更 predictable（可能是非常容易或非常难的 items），Rasch 模型可能过度参数化。\n- 关键缺失：没有报告排除 misfitting items 后 θ_n 和 c_n 估计是否稳定。如果排除 52% items 后结果显著变化，则整个分析的 robustness 存疑。\n- 建议将此升级为 critical concern 或至少要求 sensitivity analysis。\n\n---\n\n**[AGREE] R1-W3: Rank-1 contamination 结构限制性强**\n\n同意。论文 Limitations 已提及（\"contamination may be domain-specific (e.g., coding vs. reasoning), motivating higher-rank decompositions\"），但未做任何 empirical investigation。即使不实现 multi-rank 模型，至少可以按 item category 做 residual analysis 检查 rank-1 假设是否合理。Arena-Hard 的 500 items 涵盖多种话题，按 topic cluster 检查 c_n 残差分布是可行的。\n\n---\n\n**[AGREE] R1-W4: Murphy-Topel 在 N=8 下渐近有效性存疑**\n\n同意。Murphy-Topel correction 基于渐近理论（Murphy & Topel, 1985），N=8 model 显然不满足大样本条件。论文在 Appendix D（page 12-13）推导了 correction 公式但未讨论 finite-sample properties。R1 的建议（对比有/无 correction 覆盖率）是验证修正有效性的最低要求。\n\n---\n\n**[AGREE] R1-W5: σ_crit ≈ 0.2 阈值的 i.i.d. Gaussian 假设**\n\n同意。Section 4.4 假设 ε_i ~ N(0, σ²)，但真实 exposure 估计误差可能：(a) 跨 items 相关（同一数据源的 items 误差相关）；(b) 非 Gaussian（exposure 估计可能有 heavy tails）；(c) heteroscedastic（高 exposure items 的估计可能比低 exposure items 更准确）。这些违反使 σ_crit ≈ 0.2 的具体数值不可靠，但 \"error propagation matters\" 的 qualitative message 仍成立。\n\n---\n\n### 对 R1 提问的回应\n\n**Q1: N=17 100% coverage 下 G-MFRM 与 raw average τ 相同（0.779），是否意味联合校准对排名无增量价值？**\n\n好问题。我倾向于认为这确实表明 G-MFRM 在当前 Arena-Hard 设置下对 ranking 的增量价值有限。但有两个 nuance：(a) τ = 0.779 对应的是 exposed-only 231 items subset，这个 subset 的 item 组成不同于 full set，raw average 在这个 subset 上本身就较低（0.779 vs 0.838）；(b) G-MFRM 的价值可能更多体现在 c_n diagnostics 而非 τ improvement。但这强化了 R1-N1 的建议——应重新定位。\n\n**Q2: 67.9–71% 是修正前还是修正后？**\n\n根据我对 Appendix D（Murphy-Topel correction, page 12-13）和 Appendix R（c_n recovery, page 17）的阅读，Appendix R, Figure 12 展示 c_n recovery with \"71% coverage\"。Appendix D 的 Murphy-Topel 修正增大了 variance 估计但具体覆盖率改善幅度未独立报告。R1 要求明确区分修正前/后覆盖率是合理的——如果 71% 已经是修正后，则修正效果很差。\n\n**Q3: gpt-4-0314 anchor 若本身 contaminated，e_i 是否系统偏倚？**\n\n非常好的问题，我的审稿中未涉及。gpt-4-0314 作为 Stage 2 anchor（Section 4.2），其 win-rate residuals 用于估计 item-level exposure。如果 gpt-4-0314 本身对部分 Arena-Hard items exposed，则这些 items 的 e_i 会被系统性低估（anchor 的 high performance 被归因于 ability 而非 contamination），进而导致 c_n 估计偏倚。这是一个比我之前发现的 e_i 验证问题（我的 W3）更根本的 concern。\n\n---\n\n### 总结\n\nR1 的 3 个 Must-Fix 中我同意 2 个（N1, N2），认为 N3 应降级为 Should-Fix（presentation issue）。5 个 Should-Fix 全部同意。R1 的 Q3（anchor contamination）是一个我未发现的重要问题。\n\n综合 R1 和我自己的审稿，核心问题集中在：\n1. **Ranking value**（R1-N1 ≈ R2-N3）：主实验无排名改进\n2. **c_n 验证**（R2-N2 + R1-Q3）：face validity + 潜在 anchor bias\n3. **CI 覆盖率**（R1-N2）：uncertainty quantification 不可靠\n4. **单 benchmark**（R2-N1）：generalizability 不足\n\n这些问题中 (1)(2)(4) 需要新实验数据，(3) 需要实现 SBC。如果 rebuttal 能在 (2) 和 (3) 上提供新证据，并将 framing 调整为 diagnostic tool (1)，论文可升至 3.5 (Borderline Conference)。",
    "reviewer_id": "2",
    "project": "gated_mfrm_judge_bias"
  }
}
```

</details>

---


### Tool result

_source line 536 · 2026-05-25T21:27:27.643598+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4346
}
```

</details>

---


### Assistant

_source line 537 · 2026-05-25T21:27:34.408555+00:00_

交叉回应已提交。

总结：R1 的 3 个 Must-Fix 中同意 N1（ranking 退化）和 N2（CI 覆盖率），将 N3（OVB 近似）降级为 Should-Fix（presentation issue，非方法论缺陷）。5 个 Should-Fix 全部同意，特别指出 W2（52% item misfit）可能比 R1 评估的更严重。R1 的 Q3（anchor model 自身 contamination）是我此前遗漏的重要问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_4ec7f5464e5f8985d29c475e59d2f3f6:reviewer_2"
}
```

</details>

---
