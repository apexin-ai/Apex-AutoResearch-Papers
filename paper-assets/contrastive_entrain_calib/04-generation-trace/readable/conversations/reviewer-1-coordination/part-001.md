# Reviewer 1 coordination — Part 1 of 2

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Conversation logs

[Transcript overview](../reviewer-1-coordination.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/f5/f5116777ac3b497a09de.json)

## Round 1

## Round 1

46 recorded events


### User

_source line 1 · 2026-05-22T09:56:33.198319+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1

**侧重：方法严谨性 + 实验设计 + 统计分析**

### Venue 信息
- **目标**：EMNLP 2026（ARR May 2026）
- **截止日期**：2026-05-25
- **格式**：Long paper，正文 8 页 + 无限参考文献，ACL 模板（LaTeX），double-blind
- **Limitations**：必填，≤1 页，不计入页数
- **评分标准**：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

### 论文路径
- LaTeX: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/submitted.pdf`

### 审查重点

请重点审查以下方面，每个方面给出具体评价和证据：

1. **Direction Extraction 方法论**：
   - 181 个 contrastive pairs 是否足够？样本量对 AUROC 置信区间的影响
   - Style-controlled pairs 的构建方法是否充分排除了混淆因素
   - Layer selection (5-fold CV) 的方法是否 sound

2. **GRPO 实验设计**：
   - 6 个 d_syc-based 配置 + R3-only 的 ablation 是否覆盖了合理的设计空间
   - 每个 formulation 的超参数选择是否合理（w1, w3, scaling 等）
   - 是否存在 hyperparameter tuning 不充分导致的 false negative

3. **统计声明**：
   - AUROC 0.827±0.028 和 0.779±0.019 的置信区间是否正确报告
   - Fisher exact test (4/25 vs 16/16, p<0.0001) 的使用是否恰当
   - Cross-seed 分析（2 seeds）是否足以支持可复现性声明
   - Welch t-test for R3 reward saturation 的使用是否正确

4. **ACT 比较公平性**：
   - ACT (SFT) vs GRPO (RL) 的比较是否 apples-to-apples
   - ACT seed 2 仅完成 3/16 checkpoints，是否影响结论可靠性
   - 是否缺少关键 baseline（如 DPO, KTO 等其他 RL 方法）

5. **Reproducibility**：
   - 实验细节是否充分（LoRA rank/alpha, learning rate, batch size 等）
   - 仅在 Qwen3-8B 上做 RL 训练，Llama-3-8B 只做 discriminability 验证，是否足够

6. **Evaluation 指标**：
   - SYCONScore (harmonic mean of ToF and NoF) 作为核心指标是否合理
   - NLI-based flip classification 的可靠性

请按 ARR 审稿标准，给出：Summary, Strengths, Weaknesses (逐条编号), Questions, 以及 Overall Assessment（使用上述评分标准）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-22T09:56:39.576085+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3 · 2026-05-22T09:56:39.627031+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/review_reviewer_1_a4d5bbcf.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-22T09:56:43.087205+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3"
  }
}
```

</details>

---


### Tool result

_source line 5 · 2026-05-22T09:56:43.137896+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-22T09:56:45.237441+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3"
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-22T09:56:45.288314+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-22T09:56:51.714607+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-22T09:56:51.776069+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 61
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-22T09:56:55.209752+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 11 · 2026-05-22T09:56:57.568629+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/submitted.pdf",
  "pages": "1-10",
  "project": "contrastive_entrain_calib",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/submitted.pdf",
    "pages": "1-10",
    "project": "contrastive_entrain_calib",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 12 · 2026-05-22T09:57:02.445163+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines, review form criteria:

## Reviewer Guidelines and Responsibilities

ARR asks reviewers to (1) read the paper and get a first impression, (2) search for related work,
…[truncated 1312 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7235
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-22T09:57:05.213401+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 414.5}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 474.1}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 417.7}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 438.4}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 436.2}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.9}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 448.0}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 473.1}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/_pdf_ima
…[truncated 548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7644
}
```

</details>

---


### Tool call

_source line 14 · 2026-05-22T09:57:11.979073+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
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

_source line 15 · 2026-05-22T09:57:12.030386+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-22T09:57:15.912830+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with ALL scoring dimensions, their scale descriptions, and any instructions. I need every field name, every score option, and the description of what each score means."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with ALL scoring dimensions, their scale descriptions, and any instructions. I need every field name, every score option, and the description of what each score means."
  }
}
```

</details>

---


### Tool call

_source line 17 · 2026-05-22T09:57:17.277105+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-22T09:57:17.579611+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 19 · 2026-05-22T09:57:18.132563+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 20 · 2026-05-22T09:57:18.738281+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1461
}
```

</details>

---


### Tool call

_source line 21 · 2026-05-22T09:57:18.738733+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 22 · 2026-05-22T09:57:19.091698+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1512
}
```

</details>

---


### Tool call

_source line 23 · 2026-05-22T09:57:19.094423+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 24 · 2026-05-22T09:57:19.597940+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1465
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-22T09:57:20.252420+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1513
}
```

</details>

---


### Tool result

_source line 26 · 2026-05-22T09:57:20.453941+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1359
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-22T09:57:24.345335+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## 1. Reviewer Confidence
**Scale: 1-5**
- 5: "Positive that my evaluation is correct. I read the paper very carefully..."
- 4: "Quite sure. I tried to check the important points carefully..."
- 3: "Pretty sure, but there's a chance I missed something..."
- 2: "Willing to defend my evaluation, but it is fairly likely that I missed..."
- 1: "Not my area, or paper is very hard to understand..."

## 2. Soundness
**Scale: 1-5 (with .5 increments)**
- 5: "Excellent: This study is one of the most thorough I have seen..."
- 4: "Strong: This study provides sufficient support for all claims..."
- 3: "Acceptable: This study provides sufficient support for main claims..."
- 2: "Poor: Some main claims are not sufficiently supported..."
- 1: "Major Issues: This study is not yet sufficiently thorough..."

## 3. Excitement
**Scale: 1-5 (with .5 increments)**
- 5: "Highly Exciting: I would recommend this paper to others..."
- 4: "Exciting: I would mention this paper to others..."
- 3: "Interesting: I might mention some points of this paper..."
- 2: "Potentially Interesting: this paper does not resonate with me..."
- 1: "Not Exciting: this paper does not resonate with me..."

## 4. Overall Assessment
**Scale: 1-5 (with .5 increments)**
- 5: "Consider for Award: Could be considered for outstanding paper award..."
- 4: "Conference: Could be accepted to an ACL conference"
- 3: "Findings: Could be accepted to Findings of the ACL"
- 2: "Resubmit next cycle: Needs substantial revisions..."
- 1: "Do not resubmit: Has to be fully redone..."

## 5. Reproducibility
**Scale: 1-5**
- 5: "Could easily reproduce the results"
- 4: "Could mostly reproduce results with minor variations..."
- 3: "Could reproduce with difficulty due to underspecified parameters..."
- 2: "Hard to reproduce; unavailable data or insufficient details..."
- 1: "Would not be able to reproduce results..."

## 6. Datasets
**Scale: 1-5**
- 5: "Enabling: Should affect res
…[truncated 801 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8432
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-22T09:57:34.110137+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 29 · 2026-05-22T09:57:34.717097+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 30 · 2026-05-22T09:57:35.070340+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 960
}
```

</details>

---


### Tool call

_source line 31 · 2026-05-22T09:57:35.172523+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 32 · 2026-05-22T09:57:36.078754+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1361
}
```

</details>

---


### Tool call

_source line 33 · 2026-05-22T09:57:36.079228+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 34 · 2026-05-22T09:57:36.433203+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1260
}
```

</details>

---


### Tool call

_source line 35 · 2026-05-22T09:57:36.433734+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 36 · 2026-05-22T09:57:36.487462+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 53
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-22T09:57:36.890462+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 811
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-22T10:00:55.135437+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 39 · 2026-05-22T10:00:55.186784+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 40 · 2026-05-22T10:03:12.674731+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 — Round 1 审稿意见\n\n**论文**: \"Discriminability Without Utility: Why Sycophancy Directions Fail as RL Rewards\"\n**Venue**: EMNLP 2026 (ARR May 2026)\n**审查侧重**: 方法严谨性 + 实验设计 + 统计分析\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 (Findings)\n**一句话总结**: 论文揭示了表征方向可辨别性与 RL 奖励实用性之间的结构性 gap，负面结果本身有价值，但统计分析存在严重缺陷（Fisher test 独立性违反）、唯一的正面结果（ACT）仅基于单 seed、ACT vs GRPO 对比存在 supervision granularity confound，实验覆盖面不足以支撑标题中的强普遍性声明。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心失败模式分析扎实（§4-5 的 reward trap 和 stubbornness trap 刻画清晰），但关键统计检验误用、seed 数不足削弱了定量结论 |\n| Excitement | 3/5 | \"discriminability ≠ reward utility\" 的洞察对 representation engineering + RL 交叉领域有启发，但受限于单一 RL 算法（GRPO）和单一训练模型（Qwen3-8B），普遍性存疑 |\n| Reproducibility | 3/5 | LoRA rank=64、recalibration 间隔 500 步等关键参数有报告，但 w1=0.25 的选择过程、contrastive pairs 构建流程不透明 |\n| Reviewer Confidence | 4/5 | 熟悉 representation engineering、RLHF、sycophancy mitigation 相关工作 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Fisher exact test 独立性假设违反\n- 具体位置：§1 (p<0.0001 claim), §6 复述\n- 问题：论文报告 Fisher exact test 比较 GRPO（4/25 checkpoints exceed vanilla）vs ACT seed 1（16/16），得到 p<0.0001。但同一训练 run 的 checkpoints 具有强时序相关性（consecutive checkpoints 的 SycophancyScore 高度自相关），严重违反 Fisher exact test 的独立性假设。Figure 3 清楚展示了 GRPO 两个 seed 的 SycophancyScore 呈连续振荡模式，相邻 checkpoints 之间远非独立。将 25 个非独立 checkpoints 当作 25 个独立观测，人为膨胀了有效样本量。\n- 为什么影响接收：这个 p 值被用于支撑论文的核心对比结论（GRPO 系统性失败 vs ACT 成功）。如果正确处理自相关（例如用 run-level 比较：2 个 GRPO runs vs 1 个 ACT run），有效样本量只有 n=3，无法得出统计显著结论。\n- 建议修改方向：(1) 改用 run-level 汇总统计（每个 run 取最优 checkpoint 的 SycophancyScore），报告 effect size 而非 p 值；(2) 如需统计检验，使用考虑时序相关的方法（如 block bootstrap）；(3) 增加 seed 数量到至少 5 个。\n\n**N2** [critical] ACT 正面结果仅基于单个完成 seed\n- 具体位置：Table 4, §6, Limitations\n- 问题：ACT 是论文唯一的正面结果（SycophancyScore 0.301，约 2.25× vanilla baseline），但完整结果仅来自 seed 1。Seed 2 在投稿时仅完成 3/16 checkpoints 评估。论文 Limitations 承认 \"ACT cross-seed verification is partial\"，但主文中 ACT 的成功被当作已确立的事实来支撑核心论点（§6: \"ACT achieves SycophancyScore = 0.301\"）。\n- 为什么影响接收：如果 ACT seed 2 最终表现远低于 seed 1（考虑到 GRPO 本身就展示了跨 seed 的高方差），论文的 \"SFT 成功而 RL 失败\" 叙事将被严重削弱。单 seed 结果不足以建立方法有效性。\n- 建议修改方向：(1) 完成 seed 2 全部 16 checkpoints 评估后再提交；(2) 如果 seed 2 确认了 seed 1 的模式，提供跨 seed 的均值±std；(3) 如果 seed 2 不一致，诚实讨论并调整 claims 的强度。\n\n**N3** [critical] ACT vs GRPO 对比存在 supervision granularity confound\n- 具体位置：§2.4, §6, §8\n- 问题：ACT 使用 dense per-token supervision（在 token 级别区分 valid/invalid pairs，§2.4 明确写道 \"ACT operates at the token level using labeled valid/invalid pairs\"），而 GRPO 使用 single scalar reward per completion。这不是一个公平的对比——ACT 的成功可能完全归因于更丰富的监督信号粒度，而非 d_syc 方向本身。论文的核心论点是 \"d_syc 作为 RL reward 无用\"，但 ACT 的成功并不能证明这一点，因为 ACT 不是通过 d_syc 的 RL reward 成功的，而是通过完全不同的训练范式（SFT + L2 activation loss）成功的。\n- 为什么影响接收：论文标题和结论暗示 \"RL 路径走不通，SFT 路径可行\"，但这个二分法建立在一个不公平的对比上。如果给 GRPO 同样粒度的监督信号（例如 per-token reward），结果可能不同。\n- 建议修改方向：(1) 明确承认 supervision granularity 是 ACT 成功的可能解释之一，不把 ACT 成功简单归因为 \"SFT > RL\"；(2) 增加一个控制实验——例如用 d_syc 的 per-token projection 作为 dense reward 给 GRPO；(3) 调整 framing，将结论限定为 \"scalar d_syc reward 不足\"，而非 \"d_syc 作为 RL reward 失败\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 超参数 w1 仅测试单一值，存在 false negative 风险\n- 具体位置：Table 2\n- 问题：所有 F1 变体均使用 w1=0.25（d_syc reward 权重）。论文未报告是否测试过其他 w1 值（如 0.1, 0.5, 1.0）。F1a 中 d_syc/20 的 scaling factor 也未解释来源。如果 w1=0.25 恰好落在一个不良区间（过大导致 mode collapse，过小导致信号被 R3 淹没），那么 GRPO 失败可能是调参不充分的 artifact，而非 d_syc 方向本身的固有缺陷。\n- 建议：(1) 报告 w1 的选择过程（grid search? 先验知识?）；(2) 至少展示 w1 在 {0.05, 0.1, 0.25, 0.5, 1.0} 范围内的 sensitivity analysis；(3) 如果确实只跑了 w1=0.25，在 Limitations 中明确承认这一点。\n\n**W2** [warning] 标题声明过于宽泛——仅测试 GRPO 一种 RL 算法\n- 具体位置：标题、§1、§8\n- 问题：标题 \"Why Sycophancy Directions Fail as RL Rewards\" 暗示 d_syc 方向在所有 RL 框架下都失败。但实验仅测试了 GRPO（一种特定的 on-policy RL 算法）。DPO、KTO、PPO 等其他 RL 方法可能有不同表现。特别是 DPO 直接在 pair-wise preference 上优化，可能比 GRPO 的 scalar reward 更好地利用 d_syc 方向信息。\n- 建议：(1) 标题改为 \"Why Sycophancy Directions Fail as GRPO Rewards\" 或 \"...as Scalar RL Rewards\"；(2) 或增加至少一种 offline RL 方法（如 DPO）的实验。\n\n**W3** [warning] AUROC 置信区间报告不规范\n- 具体位置：§3, Table 1\n- 问题：AUROC 0.827±0.028（Qwen3-8B）和 0.779±0.019（Llama-3-8B）来自 5-fold CV。±值是 5 个 fold 的标准差，但从仅 5 个值估计标准差本身有高不确定性。这不是一个正式的置信区间。每个 fold 的测试集仅约 36 pairs，fold 间方差的估计值不稳定。\n- 建议：(1) 使用 bootstrap（在 181 pairs 上重采样 1000+ 次）计算 95% CI；(2) 或使用 Nadeau & Bengio (2003) 的 corrected resampled t-test for CV；(3) 报告每个 fold 的 AUROC 以展示分布。\n\n**W4** [warning] Contrastive pairs 构建方法细节不足\n- 具体位置：§2.1\n- 问题：论文称 contrastive pairs 是 \"style-controlled to match hedging, politeness, and length\"，但未描述具体的控制方法。是人工编写？LLM 生成后人工筛选？模板化？是否有 inter-annotator agreement？如果控制不充分，d_syc 可能捕获的是 style difference 而非 sycophancy，这将从根本上影响后续所有实验的解释。\n- 建议：(1) 详细描述 pair 构建流程（数据来源、生成方法、质量控制）；(2) 报告 pair 之间在控制维度上的统计差异（如长度差异的 t-test）；(3) 提供若干示例 pair。\n\n**W5** [warning] RL 训练仅在 Qwen3-8B 上进行\n- 具体位置：§2, Table 4\n- 问题：GRPO 和 ACT 训练均仅在 Qwen3-8B 上进行。Llama-3-8B 只用于 §3 的 direction discriminability 验证（Table 1），未做任何 RL 训练。GRPO 的失败可能是 Qwen3-8B 特定的——例如该模型的 reward landscape 结构或 LoRA 适配特性可能放大了 d_syc 的缺陷。\n- 建议：至少在 Llama-3-8B 上复现一个代表性的 GRPO 配置（如 F1a）以验证失败模式的模型无关性。\n\n**W6** [warning] Cross-seed 分析仅 2 个 seed，不足以支撑可复现性声明\n- 具体位置：§6, Figure 3\n- 问题：GRPO 仅用 2 个 seed，论文称 \"Both seeds oscillate with similar amplitude but stochastic crash timing\"。n=2 只能说明两次观察到了类似模式，不能建立统计意义上的可复现性。Figure 3 中两个 seed 的 crash 时间差异显著（seed 1 在 ~checkpoint 6500, seed 2 在 ~checkpoint 8000 附近），所谓\"相似\"的判断是定性的而非定量的。\n- 建议：(1) 增加到至少 3-5 个 seed；(2) 报告 seed 间 SycophancyScore 轨迹的定量相似性度量。\n\n---\n\n## 小问题（不影响接收）\n\n- **NLI flip classifier 未报告准确率**：§2.5 提到 flip classification 使用 NLI（LoRA rank=64, n=128），但未报告该分类器的准确率或与人工标注的一致性。如果分类器本身不准确，ToF/NoF 指标的可靠性存疑。\n- **SycophancyScore 等权 harmonic mean 未讨论**：Equation 2 定义 SycophancyScore = 2·ToF·NoF/(ToF+NoF)，隐含假设 ToF 和 NoF 同等重要。在实际应用中，抵抗无效压力（NoF）可能比接受有效修正（ToF）更重要（或反之），但论文未讨论这一设计选择的影响。\n- **\"Unknown (2025)\" 引用**：§2.5 引用 \"Unknown (2025)\" 作为 NLI flip classification 的方法来源，这似乎是 anonymization 导致的，但在正式提交中应确保引用可追溯。\n- **Appendix A (Stubbornness Taxonomy)** 的定量分析基于 100 个 probe-trained responses（exp-008v3, step 2000），样本量偏小，百分比（24% sycophantic stubbornness, 29% deliberation traps 等）的置信区间较宽。\n\n---\n\n## 主要优势\n\n1. **重要且有价值的负面结果**：系统性测试 6 种 d_syc-based GRPO 配置全部失败，对 representation engineering + RL 领域有警示意义。\n2. **失败模式分析深入**：§4 (cosine R1 structural failure) 和 §5 (probe reward trap) 对失败的根因分析细致——识别出 valid revision 和 sycophantic capitulation 在同一方向上的投影混淆（cosine projection conflates belief change direction regardless of warrant），以及 binary probe 的 gradient gaming（策略在 ~30 步内发现 sycophancy cluster 并 maximize R1）。\n3. **Conceptual insight 有深度**：§6 提出 \"discriminability is necessary but not sufficient for reward utility\"，并给出了清晰的机制解释——d_syc 编码的是 belief change 的方向而非其是否有 warrant，因此无法区分应该奖励和应该惩罚的行为。\n4. **Cross-model 方向验证**：Table 1 展示 d_syc 在 Qwen3-8B 和 Llama-3-8B 两个架构上都具有 discriminability，且 best-layer 位置合理（上层 1/3），增强了方向提取方法的可信度。\n5. **Behavioral failure taxonomy**（Appendix A）提供了定性洞察——sycophantic stubbornness、deliberation traps、evidence-graded hedging 三种模式的识别有助于理解 RL 训练中的 reward hacking 行为。\n\n---\n\n## 对 Director 指定审查重点的逐项回应\n\n### 1. Direction Extraction 方法论\n- 181 对 contrastive pairs 对于提取单一线性方向来说是可接受的样本量（与 Zou et al. 2023 等工作一致），但 **style-controlled 的方法细节严重缺失**（W4）。\n- 5-fold CV 选层方法原则上 sound，但从 36 层（Qwen3-8B）中选最优层存在 selection bias 风险，即使使用了 CV。AUROC CI 报告不规范（W3）。\n- Evidence-strength 分层（weak/medium/strong）是一个加分设计，Table 1 中 weak subset AUROC 低于整体（0.675 vs 0.827）的发现有信息量。\n\n### 2. GRPO 实验设计\n- 6 个配置（F1a-F1d + F2 + F3）+ R3-only 的覆盖面合理，但 **w1 仅测试一个值**（W1）是重大缺陷。\n- 各 formulation 的设计逻辑清晰（从 unbounded cosine 到 bounded sigmoid，从 continuous 到 discrete），展示了系统性探索。\n- **缺少非 GRPO 的 RL 方法**（W2），特别是 DPO，它天然适合 pair-wise 设置。\n\n### 3. 统计声明\n- **Fisher exact test 严重误用**（N1），这是本文最大的统计问题。\n- AUROC CI 应改用 bootstrap（W3）。\n- **2 个 seed 完全不足以支撑可复现性声明**（W6）。\n- 关于 Welch t-test for R3 reward saturation：论文中未找到明确使用 Welch t-test 的描述，如果在 supplementary material 中使用了，应在主文中注明。\n\n### 4. ACT 比较公平性\n- **ACT vs GRPO 的对比是本文最大的方法论问题之一**（N3）。Supervision granularity 的差异完全混淆了结论。\n- ACT seed 2 仅 3/16 checkpoints（N2），使得唯一正面结果基于单 seed，可靠性不足。\n- **缺少 DPO/KTO 等其他 RL baseline**（W2），限制了负面结论的普遍性。\n\n### 5. Reproducibility\n- LoRA rank=64 有报告，recalibration 间隔 500 步有报告。但 learning rate、batch size、GRPO 的 group size 等核心训练超参数在主文中未找到（可能在附录，但提交 PDF 附录仅有 Stubbornness Taxonomy）。\n- 仅在 Qwen3-8B 上做 RL 训练（W5），Llama-3-8B 只做了 direction discriminability 验证。\n\n### 6. Evaluation 指标\n- SycophancyScore 的 harmonic mean 设计合理但 **等权假设未讨论**。\n- NLI-based flip classification 的可靠性 **未用人工标注验证**，这是评估流水线的潜在薄弱环节。\n",
  "reviewer_id": "1",
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 — Round 1 审稿意见\n\n**论文**: \"Discriminability Without Utility: Why Sycophancy Directions Fail as RL Rewards\"\n**Venue**: EMNLP 2026 (ARR May 2026)\n**审查侧重**: 方法严谨性 + 实验设计 + 统计分析\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 (Findings)\n**一句话总结**: 论文揭示了表征方向可辨别性与 RL 奖励实用性之间的结构性 gap，负面结果本身有价值，但统计分析存在严重缺陷（Fisher test 独立性违反）、唯一的正面结果（ACT）仅基于单 seed、ACT vs GRPO 对比存在 supervision granularity confound，实验覆盖面不足以支撑标题中的强普遍性声明。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心失败模式分析扎实（§4-5 的 reward trap 和 stubbornness trap 刻画清晰），但关键统计检验误用、seed 数不足削弱了定量结论 |\n| Excitement | 3/5 | \"discriminability ≠ reward utility\" 的洞察对 representation engineering + RL 交叉领域有启发，但受限于单一 RL 算法（GRPO）和单一训练模型（Qwen3-8B），普遍性存疑 |\n| Reproducibility | 3/5 | LoRA rank=64、recalibration 间隔 500 步等关键参数有报告，但 w1=0.25 的选择过程、contrastive pairs 构建流程不透明 |\n| Reviewer Confidence | 4/5 | 熟悉 representation engineering、RLHF、sycophancy mitigation 相关工作 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Fisher exact test 独立性假设违反\n- 具体位置：§1 (p<0.0001 claim), §6 复述\n- 问题：论文报告 Fisher exact test 比较 GRPO（4/25 checkpoints exceed vanilla）vs ACT seed 1（16/16），得到 p<0.0001。但同一训练 run 的 checkpoints 具有强时序相关性（consecutive checkpoints 的 SycophancyScore 高度自相关），严重违反 Fisher exact test 的独立性假设。Figure 3 清楚展示了 GRPO 两个 seed 的 SycophancyScore 呈连续振荡模式，相邻 checkpoints 之间远非独立。将 25 个非独立 checkpoints 当作 25 个独立观测，人为膨胀了有效样本量。\n- 为什么影响接收：这个 p 值被用于支撑论文的核心对比结论（GRPO 系统性失败 vs ACT 成功）。如果正确处理自相关（例如用 run-level 比较：2 个 GRPO runs vs 1 个 ACT run），有效样本量只有 n=3，无法得出统计显著结论。\n- 建议修改方向：(1) 改用 run-level 汇总统计（每个 run 取最优 checkpoint 的 SycophancyScore），报告 effect size 而非 p 值；(2) 如需统计检验，使用考虑时序相关的方法（如 block bootstrap）；(3) 增加 seed 数量到至少 5 个。\n\n**N2** [critical] ACT 正面结果仅基于单个完成 seed\n- 具体位置：Table 4, §6, Limitations\n- 问题：ACT 是论文唯一的正面结果（SycophancyScore 0.301，约 2.25× vanilla baseline），但完整结果仅来自 seed 1。Seed 2 在投稿时仅完成 3/16 checkpoints 评估。论文 Limitations 承认 \"ACT cross-seed verification is partial\"，但主文中 ACT 的成功被当作已确立的事实来支撑核心论点（§6: \"ACT achieves SycophancyScore = 0.301\"）。\n- 为什么影响接收：如果 ACT seed 2 最终表现远低于 seed 1（考虑到 GRPO 本身就展示了跨 seed 的高方差），论文的 \"SFT 成功而 RL 失败\" 叙事将被严重削弱。单 seed 结果不足以建立方法有效性。\n- 建议修改方向：(1) 完成 seed 2 全部 16 checkpoints 评估后再提交；(2) 如果 seed 2 确认了 seed 1 的模式，提供跨 seed 的均值±std；(3) 如果 seed 2 不一致，诚实讨论并调整 claims 的强度。\n\n**N3** [critical] ACT vs GRPO 对比存在 supervision granularity confound\n- 具体位置：§2.4, §6, §8\n- 问题：ACT 使用 dense per-token supervision（在 token 级别区分 valid/invalid pairs，§2.4 明确写道 \"ACT operates at the token level using labeled valid/invalid pairs\"），而 GRPO 使用 single scalar reward per completion。这不是一个公平的对比——ACT 的成功可能完全归因于更丰富的监督信号粒度，而非 d_syc 方向本身。论文的核心论点是 \"d_syc 作为 RL reward 无用\"，但 ACT 的成功并不能证明这一点，因为 ACT 不是通过 d_syc 的 RL reward 成功的，而是通过完全不同的训练范式（SFT + L2 activation loss）成功的。\n- 为什么影响接收：论文标题和结论暗示 \"RL 路径走不通，SFT 路径可行\"，但这个二分法建立在一个不公平的对比上。如果给 GRPO 同样粒度的监督信号（例如 per-token reward），结果可能不同。\n- 建议修改方向：(1) 明确承认 supervision granularity 是 ACT 成功的可能解释之一，不把 ACT 成功简单归因为 \"SFT > RL\"；(2) 增加一个控制实验——例如用 d_syc 的 per-token projection 作为 dense reward 给 GRPO；(3) 调整 framing，将结论限定为 \"scalar d_syc reward 不足\"，而非 \"d_syc 作为 RL reward 失败\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 超参数 w1 仅测试单一值，存在 false negative 风险\n- 具体位置：Table 2\n- 问题：所有 F1 变体均使用 w1=0.25（d_syc reward 权重）。论文未报告是否测试过其他 w1 值（如 0.1, 0.5, 1.0）。F1a 中 d_syc/20 的 scaling factor 也未解释来源。如果 w1=0.25 恰好落在一个不良区间（过大导致 mode collapse，过小导致信号被 R3 淹没），那么 GRPO 失败可能是调参不充分的 artifact，而非 d_syc 方向本身的固有缺陷。\n- 建议：(1) 报告 w1 的选择过程（grid search? 先验知识?）；(2) 至少展示 w1 在 {0.05, 0.1, 0.25, 0.5, 1.0} 范围内的 sensitivity analysis；(3) 如果确实只跑了 w1=0.25，在 Limitations 中明确承认这一点。\n\n**W2** [warning] 标题声明过于宽泛——仅测试 GRPO 一种 RL 算法\n- 具体位置：标题、§1、§8\n- 问题：标题 \"Why Sycophancy Directions Fail as RL Rewards\" 暗示 d_syc 方向在所有 RL 框架下都失败。但实验仅测试了 GRPO（一种特定的 on-policy RL 算法）。DPO、KTO、PPO 等其他 RL 方法可能有不同表现。特别是 DPO 直接在 pair-wise preference 上优化，可能比 GRPO 的 scalar reward 更好地利用 d_syc 方向信息。\n- 建议：(1) 标题改为 \"Why Sycophancy Directions Fail as GRPO Rewards\" 或 \"...as Scalar RL Rewards\"；(2) 或增加至少一种 offline RL 方法（如 DPO）的实验。\n\n**W3** [warning] AUROC 置信区间报告不规范\n- 具体位置：§3, Table 1\n- 问题：AUROC 0.827±0.028（Qwen3-8B）和 0.779±0.019（Llama-3-8B）来自 5-fold CV。±值是 5 个 fold 的标准差，但从仅 5 个值估计标准差本身有高不确定性。这不是一个正式的置信区间。每个 fold 的测试集仅约 36 pairs，fold 间方差的估计值不稳定。\n- 建议：(1) 使用 bootstrap（在 181 pairs 上重采样 1000+ 次）计算 95% CI；(2) 或使用 Nadeau & Bengio (2003) 的 corrected resampled t-test for CV；(3) 报告每个 fold 的 AUROC 以展示分布。\n\n**W4** [warning] Contrastive pairs 构建方法细节不足\n- 具体位置：§2.1\n- 问题：论文称 contrastive pairs 是 \"style-controlled to match hedging, politeness, and length\"，但未描述具体的控制方法。是人工编写？LLM 生成后人工筛选？模板化？是否有 inter-annotator agreement？如果控制不充分，d_syc 可能捕获的是 style difference 而非 sycophancy，这将从根本上影响后续所有实验的解释。\n- 建议：(1) 详细描述 pair 构建流程（数据来源、生成方法、质量控制）；(2) 报告 pair 之间在控制维度上的统计差异（如长度差异的 t-test）；(3) 提供若干示例 pair。\n\n**W5** [warning] RL 训练仅在 Qwen3-8B 上进行\n- 具体位置：§2, Table 4\n- 问题：GRPO 和 ACT 训练均仅在 Qwen3-8B 上进行。Llama-3-8B 只用于 §3 的 direction discriminability 验证（Table 1），未做任何 RL 训练。GRPO 的失败可能是 Qwen3-8B 特定的——例如该模型的 reward landscape 结构或 LoRA 适配特性可能放大了 d_syc 的缺陷。\n- 建议：至少在 Llama-3-8B 上复现一个代表性的 GRPO 配置（如 F1a）以验证失败模式的模型无关性。\n\n**W6** [warning] Cross-seed 分析仅 2 个 seed，不足以支撑可复现性声明\n- 具体位置：§6, Figure 3\n- 问题：GRPO 仅用 2 个 seed，论文称 \"Both seeds oscillate with similar amplitude but stochastic crash timing\"。n=2 只能说明两次观察到了类似模式，不能建立统计意义上的可复现性。Figure 3 中两个 seed 的 crash 时间差异显著（seed 1 在 ~checkpoint 6500, seed 2 在 ~checkpoint 8000 附近），所谓\"相似\"的判断是定性的而非定量的。\n- 建议：(1) 增加到至少 3-5 个 seed；(2) 报告 seed 间 SycophancyScore 轨迹的定量相似性度量。\n\n---\n\n## 小问题（不影响接收）\n\n- **NLI flip classifier 未报告准确率**：§2.5 提到 flip classification 使用 NLI（LoRA rank=64, n=128），但未报告该分类器的准确率或与人工标注的一致性。如果分类器本身不准确，ToF/NoF 指标的可靠性存疑。\n- **SycophancyScore 等权 harmonic mean 未讨论**：Equation 2 定义 SycophancyScore = 2·ToF·NoF/(ToF+NoF)，隐含假设 ToF 和 NoF 同等重要。在实际应用中，抵抗无效压力（NoF）可能比接受有效修正（ToF）更重要（或反之），但论文未讨论这一设计选择的影响。\n- **\"Unknown (2025)\" 引用**：§2.5 引用 \"Unknown (2025)\" 作为 NLI flip classification 的方法来源，这似乎是 anonymization 导致的，但在正式提交中应确保引用可追溯。\n- **Appendix A (Stubbornness Taxonomy)** 的定量分析基于 100 个 probe-trained responses（exp-008v3, step 2000），样本量偏小，百分比（24% sycophantic stubbornness, 29% deliberation traps 等）的置信区间较宽。\n\n---\n\n## 主要优势\n\n1. **重要且有价值的负面结果**：系统性测试 6 种 d_syc-based GRPO 配置全部失败，对 representation engineering + RL 领域有警示意义。\n2. **失败模式分析深入**：§4 (cosine R1 structural failure) 和 §5 (probe reward trap) 对失败的根因分析细致——识别出 valid revision 和 sycophantic capitulation 在同一方向上的投影混淆（cosine projection conflates belief change direction regardless of warrant），以及 binary probe 的 gradient gaming（策略在 ~30 步内发现 sycophancy cluster 并 maximize R1）。\n3. **Conceptual insight 有深度**：§6 提出 \"discriminability is necessary but not sufficient for reward utility\"，并给出了清晰的机制解释——d_syc 编码的是 belief change 的方向而非其是否有 warrant，因此无法区分应该奖励和应该惩罚的行为。\n4. **Cross-model 方向验证**：Table 1 展示 d_syc 在 Qwen3-8B 和 Llama-3-8B 两个架构上都具有 discriminability，且 best-layer 位置合理（上层 1/3），增强了方向提取方法的可信度。\n5. **Behavioral failure taxonomy**（Appendix A）提供了定性洞察——sycophantic stubbornness、deliberation traps、evidence-graded hedging 三种模式的识别有助于理解 RL 训练中的 reward hacking 行为。\n\n---\n\n## 对 Director 指定审查重点的逐项回应\n\n### 1. Direction Extraction 方法论\n- 181 对 contrastive pairs 对于提取单一线性方向来说是可接受的样本量（与 Zou et al. 2023 等工作一致），但 **style-controlled 的方法细节严重缺失**（W4）。\n- 5-fold CV 选层方法原则上 sound，但从 36 层（Qwen3-8B）中选最优层存在 selection bias 风险，即使使用了 CV。AUROC CI 报告不规范（W3）。\n- Evidence-strength 分层（weak/medium/strong）是一个加分设计，Table 1 中 weak subset AUROC 低于整体（0.675 vs 0.827）的发现有信息量。\n\n### 2. GRPO 实验设计\n- 6 个配置（F1a-F1d + F2 + F3）+ R3-only 的覆盖面合理，但 **w1 仅测试一个值**（W1）是重大缺陷。\n- 各 formulation 的设计逻辑清晰（从 unbounded cosine 到 bounded sigmoid，从 continuous 到 discrete），展示了系统性探索。\n- **缺少非 GRPO 的 RL 方法**（W2），特别是 DPO，它天然适合 pair-wise 设置。\n\n### 3. 统计声明\n- **Fisher exact test 严重误用**（N1），这是本文最大的统计问题。\n- AUROC CI 应改用 bootstrap（W3）。\n- **2 个 seed 完全不足以支撑可复现性声明**（W6）。\n- 关于 Welch t-test for R3 reward saturation：论文中未找到明确使用 Welch t-test 的描述，如果在 supplementary material 中使用了，应在主文中注明。\n\n### 4. ACT 比较公平性\n- **ACT vs GRPO 的对比是本文最大的方法论问题之一**（N3）。Supervision granularity 的差异完全混淆了结论。\n- ACT seed 2 仅 3/16 checkpoints（N2），使得唯一正面结果基于单 seed，可靠性不足。\n- **缺少 DPO/KTO 等其他 RL baseline**（W2），限制了负面结论的普遍性。\n\n### 5. Reproducibility\n- LoRA rank=64 有报告，recalibration 间隔 500 步有报告。但 learning rate、batch size、GRPO 的 group size 等核心训练超参数在主文中未找到（可能在附录，但提交 PDF 附录仅有 Stubbornness Taxonomy）。\n- 仅在 Qwen3-8B 上做 RL 训练（W5），Llama-3-8B 只做了 direction discriminability 验证。\n\n### 6. Evaluation 指标\n- SycophancyScore 的 harmonic mean 设计合理但 **等权假设未讨论**。\n- NLI-based flip classification 的可靠性 **未用人工标注验证**，这是评估流水线的潜在薄弱环节。\n",
    "reviewer_id": "1",
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 41 · 2026-05-22T10:03:17.137804+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4463
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-22T10:03:20.165975+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
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

_source line 43 · 2026-05-22T10:03:20.216519+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-22T10:03:26.379536+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-22T10:03:26.430204+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 46 · 2026-05-22T10:03:36.870049+00:00_

审稿意见已提交给 Review Director。

核心发现：

- **Overall 3.0 (Findings)**——负面结果有价值但证据不足以支撑标题中的强普遍性声明
- **3 个 Must-Fix**：Fisher exact test 将非独立 checkpoints 当独立样本（p<0.0001 不可信）、ACT 正面结果仅单 seed 完成、ACT vs GRPO 存在 supervision granularity confound
- **6 个 Should-Fix**：w1 仅测试单一值（false negative 风险）、标题 overclaim（仅测 GRPO）、AUROC CI 不规范、contrastive pairs 构建细节缺失、仅 Qwen3-8B 做 RL 训练、仅 2 seeds

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1"
}
```

</details>

---


## Round 2

## Round 2

4 recorded events


### User

_source line 47 · 2026-05-22T10:04:29.709086+00:00_

[Round 1 审稿请求]:
## 交叉分享 — Reviewer 2 的完整审稿意见

请逐条回应以下 Reviewer 2 的意见。对每条使用 **[AGREE]** 并说明理由，或 **[REBUT]** 并提供证据（cite 具体 Section/Table/Figure）。

---

### Reviewer 2 Overall: 3.0 (Findings)

### Reviewer 2 Must-Fix 问题

**R2-N1** [critical] 遗漏直接相关的成功案例：Papadatos &amp; Freedman (2024)
- arXiv 2412.00967 "Linear Probe Penalties Reduce LLM Sycophancy" 使用 linear probe 在 reward model 内部识别并惩罚 sycophancy 标记，实验报告在多个开源 LLM 上成功降低了 sycophantic behavior。这与本文的核心 thesis——"representation-level sycophancy detection 不能转化为有效 reward signal"——直接矛盾或至少存在紧张关系。
- 论文未讨论为何同类方法在不同框架下成功。如果 probe penalty 在 reward model 上有效而 probe reward 在 GRPO 上失败，关键区别是什么？

**R2-N2** [critical] references.bib 中多条引用严重不完整
- consistency2025bctact（ACT）：author = "Unknown"
- zhang2026latentgrpo, wang2025internal, sinii2025smallvectors, obrien2025fewbadneurons：均为 "et al."
- wei2024synthetic：将 "Anthropic" 列为作者名
- ackermann2026gradreg："Ackermann, Johannes and others"
- ACT 是论文唯一成功 baseline，其引用连作者都是 "Unknown"。

**R2-N3** [critical] ACT seed 2 验证未完成，正面 baseline 证据不足
- ACT seed 2 仅评估 3/16 checkpoints，论文核心对比（4/25 vs 16/16）仅基于 seed 1 完整评估。

### Reviewer 2 Should-Fix 问题

**R2-W1** [warning] 未讨论 DPO/KTO 等 preference-based RL 替代方案
- DPO/KTO 基于 preference pair 而非 scalar reward，可能绕过 "单一标量无法区分 warranted vs unwarranted" 的问题。标题使用 "RL Rewards" 但仅测试 GRPO。

**R2-W2** [warning] Process Reward Models 讨论不足
- SMART (arXiv 2509.16742) 已使用 per-step process rewards + MCTS 进行 sycophancy mitigation 并报告成功。论文仅 1 句提及 future directions。

**R2-W3** [warning] Conclusion 的 broader lesson 存在 overclaiming
- "any alignment effort" 的一般性声明仅基于 sycophancy 一个 case，且论文自己承认 reasoning/safety directions 的 probe-based RL 是成功的。

**R2-W4** [warning] 仅在单一模型上做 RL 训练
- 所有 GRPO 和 ACT 训练仅在 Qwen3-8B 上进行，C1 的 "Every tested GRPO formulation fails" 严格意义上仅适用于 Qwen3-8B。

**R2-W5** [warning] 181 对训练数据规模偏小
- 更大训练集是否可能产生更鲁棒的 direction，缓解 cosine gap 过窄（仅 0.098）的问题？

### Reviewer 2 Missing References
1. Papadatos &amp; Freedman (2024) — Linear Probe Penalties Reduce LLM Sycophancy (arXiv 2412.00967)
2. SMART (2025) — per-step process rewards 用于 sycophancy mitigation (arXiv 2509.16742)
3. DPO (Rafailov et al., 2023) / KTO (Ethayarajh et al., 2024)

---

请对以上每条给出 [AGREE] 或 [REBUT]，并说明理由。特别关注：
1. R2-N1 关于 Papadatos &amp; Freedman (2024) 的遗漏——你是否认为这确实是一个 critical gap？
2. R2-N2 关于引用质量——从方法严谨性角度，这是否影响论文可信度？
3. 你的 N1（Fisher test）和 R2 的 N1（missing reference）哪个对论文接收影响更大？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-22T10:06:28.611122+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 — 交叉回应 Reviewer 2 意见\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: 遗漏 Papadatos & Freedman (2024) 的 probe penalty 成功案例**\n\n同意这是一个重要遗漏，但我将其严重性评为 **must-fix 偏下限**而非 R2 认定的最高级别 critical。\n\n理由：如果 Papadatos & Freedman (2024) 确实通过 linear probe penalty 在 reward model 内部成功降低了 sycophancy，那这与本文 §5 中 F2（binary probe）和 F3（continuous probe）作为 GRPO reward 的失败形成了直接张力。论文的核心 thesis——representation-level sycophancy detection 不能转化为有效 reward signal——需要解释为什么同类信号在不同框架下（reward model 内部 penalty vs. GRPO scalar reward）有截然不同的效果。\n\n但我认为存在合理的区分：(1) probe penalty 作用于 reward model 的中间表征（修改 RM 自身的行为），vs. 本文将 probe 输出直接作为 policy optimization 的 reward component——前者保留了 RM 的 per-token richness，后者压缩为 per-completion scalar；(2) penalty（惩罚 sycophancy 标记）vs. reward（奖励非 sycophancy 方向）在梯度方向上可能有不对称效果。论文如果能在 §7 Related Work 中讨论这些区分，可以将其从\"直接矛盾\"降级为\"互补视角\"。\n\n**补充**：这个遗漏也间接支持了我的 N3——如果 probe penalty 在更细粒度的 reward model 中有效，那问题可能不是 d_syc 方向本身，而是 GRPO 的 scalar reward 粒度。\n\n---\n\n**[AGREE] R2-N2: 引用严重不完整**\n\n同意，且我认为比 R2 描述的更严重。\n\nACT 是论文唯一报告成功的 baseline（Table 4, SycophancyScore 0.301），其引用 \"Unknown (2025)\" 意味着读者无法追溯验证该方法的原始定义和效果。在 double-blind 审稿中，如果 \"Unknown\" 是因为 ACT 是作者自己的工作而进行了匿名化，那这暗示论文可能在评估自己的先前工作作为 baseline，存在潜在的公平性问题。如果不是自己的工作，那 \"Unknown\" 就是粗心的 bib 管理。\n\n其他引用问题同样影响可信度：多条使用 \"et al.\" 代替完整作者列表违反了基本的学术引用规范。将 \"Anthropic\" 列为 author name（wei2024synthetic）是格式错误。这些问题加在一起反映了论文在编辑质量上的系统性不足。\n\n从方法严谨性角度：引用不完整本身不影响实验结果的有效性，但它 (1) 妨碍读者追溯验证方法来源，(2) 对 reproducibility 维度有负面影响，(3) 在审稿中会显著降低论文的专业印象。\n\n---\n\n**[AGREE] R2-N3: ACT seed 2 验证未完成**\n\n完全同意，这与我的 N2 一致。ACT seed 2 仅完成 3/16 checkpoints 评估，论文核心正面结果依赖单 seed，可靠性不足。不再赘述。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: 未讨论 DPO/KTO 等 preference-based RL**\n\n完全同意，与我的 W2 一致。补充一点：DPO 特别值得关注，因为 d_syc 方向天然适合构造 preference pair（sycophantic response vs. non-sycophantic response），而 DPO 直接在 pair-wise preference 上优化，可能绕过 GRPO scalar reward 的 \"cosine projection conflates valid revision with capitulation\" 问题（我的 N3 中指出的 supervision granularity confound）。标题声称 \"RL Rewards\" 失败但仅测试了 GRPO 一种算法，确实 overclaiming。\n\n---\n\n**[AGREE] R2-W2: Process Reward Models 讨论不足**\n\n同意，但我将其严重性降为 **minor-to-warning** 级别。论文确实在 §7 末尾 \"Future directions\" 中提到了 per-step feedback 的可能性（\"process-reward models with per-step feedback each offer paths to bridge the supervision density gap\"），但仅一句带过。如果 SMART (arXiv 2509.16742) 已经用 per-step process rewards 成功做了 sycophancy mitigation，这应当在 §7 Related Work 中正式讨论，而非放在 future directions 中暗示\"还没人做过\"。\n\n这也进一步支持了我的 N3 和 R2-N1 的论点：失败的根因可能是 reward granularity（per-completion scalar）而非 d_syc 方向本身。\n\n---\n\n**[AGREE] R2-W3: Conclusion 的 broader lesson overclaiming**\n\n同意。§8 Conclusion 中 \"any alignment effort that converts a direction probe into a reward signal must verify that the probe separates not only the target behavior from its complement, but also the valid and invalid instances within each class\" 的表述过于宽泛。论文仅在 sycophancy 一个维度、GRPO 一种算法、Qwen3-8B 一个模型上实验。§7 Related Work 自己也承认 reasoning/safety directions 的 probe-based RL 存在成功案例（Zou et al. 2023, Burns et al. 2023 等的 representation engineering 方法）。\n\n建议改为：\"For sycophancy specifically, where valid and invalid behaviors share the same geometric direction in activation space, scalar probe-based GRPO rewards are insufficient.\"\n\n---\n\n**[AGREE] R2-W4: 仅单一模型做 RL 训练**\n\n同意，与我的 W5 一致。\n\n---\n\n**[REBUT] R2-W5: 181 对训练数据规模偏小**\n\n部分不同意 R2 的 framing。\n\nR2 关注的是\"更大训练集是否能产生更鲁棒的 direction，缓解 cosine gap 仅 0.098 的问题\"。但论文的核心论点不是 direction 提取质量差（AUROC 0.827 已经相当不错），而是 **即使 direction 能良好区分 sycophantic vs. non-sycophantic，这个方向作为 RL reward 仍然失败**。失败的根因在 §6 中明确分析：d_syc 编码的是 belief change 的方向，而 valid revision 和 sycophantic capitulation **都沿相同方向移动**——这是一个结构性问题，不会因为更多训练数据而消失。\n\ncosine gap 0.098（§4 提到 \"the cosine gap between valid and sycophantic activations averages only 0.098 across layers\"）确实小，但这不是数据量的问题，而是反映了 valid revision 和 capitulation 在 activation space 中本身就很接近。更多 pairs 可以让 d_syc 方向估计更精确（降低 ±0.028 的 CV 方差），但不会拉大 valid/invalid activations 之间的结构性 gap。\n\n我的 W4 关注的是 pair 构建的**质量控制**（style-controlled 方法不透明），而非数量——这是更关键的问题。181 对质量不明的 pairs 和 500 对同样质量不明的 pairs 不会有本质区别。\n\n---\n\n### Missing References\n\n**[AGREE]** 三篇 missing references 均应补充。Papadatos & Freedman (2024) 和 SMART (2025) 与本文 thesis 有直接对话关系；DPO/KTO 是明显的 RL baseline 遗漏。\n\n---\n\n### Director 提出的三个具体问题\n\n**Q1: R2-N1（Papadatos & Freedman 遗漏）是否确实是 critical gap？**\n\n是的，但 critical 程度取决于该论文与本文方法的可比性。如果 Papadatos & Freedman 的 probe penalty 作用于 reward model 中间层（即修改 RM 的输出而非直接作为 policy reward），那两种方法的 failure/success 差异可以用 supervision granularity 来解释（与我的 N3 一致）——这反而**强化**本文的论点（scalar probe reward 不够，需要更细粒度的监督）。但如果该工作的 probe penalty 也是作为 scalar reward 直接给 policy optimizer 且成功了，那就是直接矛盾，必须在论文中解释。论文不讨论这一区别是不可接受的。\n\n**Q2: R2-N2（引用质量）是否影响论文可信度？**\n\n从方法严谨性角度：**是的，但程度有限**。引用不完整不改变实验结果的有效性，但 (1) ACT 的 \"Unknown\" 作者使读者无法验证这个关键 baseline 的原始定义，直接影响 reproducibility 评分；(2) 多条引用的系统性不完整暗示论文准备仓促或编辑标准低，会在审稿中产生负面信号。这是一个容易修复的问题，但在当前状态下确实降低可信度。\n\n**Q3: 我的 N1（Fisher test 误用）和 R2-N1（missing reference）哪个对论文接收影响更大？**\n\n**我的 N1 影响更大。**\n\n理由：Fisher test 误用直接攻击论文的定量推理核心——将非独立 checkpoints 当作独立样本产生虚假的 p<0.0001，使得 GRPO vs ACT 的统计对比无效。这不是可以通过补充讨论来修复的，而是需要重新设计统计分析、可能增加实验 seeds。\n\nR2-N1 的 missing reference 虽然重要，但本质上是 **framing 问题**——论文需要在 Related Work 中讨论为什么 probe penalty 在不同框架下有不同效果，并适当限定自己的 claims 范围。这是可以在 revision 中通过补充 1-2 段讨论来解决的。\n\n从 ARR 评审角度，统计方法的根本性缺陷（影响 Soundness）比相关工作遗漏（主要影响 completeness/framing）对 Overall Assessment 的负面影响更大。\n",
  "reviewer_id": "1",
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 — 交叉回应 Reviewer 2 意见\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: 遗漏 Papadatos & Freedman (2024) 的 probe penalty 成功案例**\n\n同意这是一个重要遗漏，但我将其严重性评为 **must-fix 偏下限**而非 R2 认定的最高级别 critical。\n\n理由：如果 Papadatos & Freedman (2024) 确实通过 linear probe penalty 在 reward model 内部成功降低了 sycophancy，那这与本文 §5 中 F2（binary probe）和 F3（continuous probe）作为 GRPO reward 的失败形成了直接张力。论文的核心 thesis——representation-level sycophancy detection 不能转化为有效 reward signal——需要解释为什么同类信号在不同框架下（reward model 内部 penalty vs. GRPO scalar reward）有截然不同的效果。\n\n但我认为存在合理的区分：(1) probe penalty 作用于 reward model 的中间表征（修改 RM 自身的行为），vs. 本文将 probe 输出直接作为 policy optimization 的 reward component——前者保留了 RM 的 per-token richness，后者压缩为 per-completion scalar；(2) penalty（惩罚 sycophancy 标记）vs. reward（奖励非 sycophancy 方向）在梯度方向上可能有不对称效果。论文如果能在 §7 Related Work 中讨论这些区分，可以将其从\"直接矛盾\"降级为\"互补视角\"。\n\n**补充**：这个遗漏也间接支持了我的 N3——如果 probe penalty 在更细粒度的 reward model 中有效，那问题可能不是 d_syc 方向本身，而是 GRPO 的 scalar reward 粒度。\n\n---\n\n**[AGREE] R2-N2: 引用严重不完整**\n\n同意，且我认为比 R2 描述的更严重。\n\nACT 是论文唯一报告成功的 baseline（Table 4, SycophancyScore 0.301），其引用 \"Unknown (2025)\" 意味着读者无法追溯验证该方法的原始定义和效果。在 double-blind 审稿中，如果 \"Unknown\" 是因为 ACT 是作者自己的工作而进行了匿名化，那这暗示论文可能在评估自己的先前工作作为 baseline，存在潜在的公平性问题。如果不是自己的工作，那 \"Unknown\" 就是粗心的 bib 管理。\n\n其他引用问题同样影响可信度：多条使用 \"et al.\" 代替完整作者列表违反了基本的学术引用规范。将 \"Anthropic\" 列为 author name（wei2024synthetic）是格式错误。这些问题加在一起反映了论文在编辑质量上的系统性不足。\n\n从方法严谨性角度：引用不完整本身不影响实验结果的有效性，但它 (1) 妨碍读者追溯验证方法来源，(2) 对 reproducibility 维度有负面影响，(3) 在审稿中会显著降低论文的专业印象。\n\n---\n\n**[AGREE] R2-N3: ACT seed 2 验证未完成**\n\n完全同意，这与我的 N2 一致。ACT seed 2 仅完成 3/16 checkpoints 评估，论文核心正面结果依赖单 seed，可靠性不足。不再赘述。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: 未讨论 DPO/KTO 等 preference-based RL**\n\n完全同意，与我的 W2 一致。补充一点：DPO 特别值得关注，因为 d_syc 方向天然适合构造 preference pair（sycophantic response vs. non-sycophantic response），而 DPO 直接在 pair-wise preference 上优化，可能绕过 GRPO scalar reward 的 \"cosine projection conflates valid revision with capitulation\" 问题（我的 N3 中指出的 supervision granularity confound）。标题声称 \"RL Rewards\" 失败但仅测试了 GRPO 一种算法，确实 overclaiming。\n\n---\n\n**[AGREE] R2-W2: Process Reward Models 讨论不足**\n\n同意，但我将其严重性降为 **minor-to-warning** 级别。论文确实在 §7 末尾 \"Future directions\" 中提到了 per-step feedback 的可能性（\"process-reward models with per-step feedback each offer paths to bridge the supervision density gap\"），但仅一句带过。如果 SMART (arXiv 2509.16742) 已经用 per-step process rewards 成功做了 sycophancy mitigation，这应当在 §7 Related Work 中正式讨论，而非放在 future directions 中暗示\"还没人做过\"。\n\n这也进一步支持了我的 N3 和 R2-N1 的论点：失败的根因可能是 reward granularity（per-completion scalar）而非 d_syc 方向本身。\n\n---\n\n**[AGREE] R2-W3: Conclusion 的 broader lesson overclaiming**\n\n同意。§8 Conclusion 中 \"any alignment effort that converts a direction probe into a reward signal must verify that the probe separates not only the target behavior from its complement, but also the valid and invalid instances within each class\" 的表述过于宽泛。论文仅在 sycophancy 一个维度、GRPO 一种算法、Qwen3-8B 一个模型上实验。§7 Related Work 自己也承认 reasoning/safety directions 的 probe-based RL 存在成功案例（Zou et al. 2023, Burns et al. 2023 等的 representation engineering 方法）。\n\n建议改为：\"For sycophancy specifically, where valid and invalid behaviors share the same geometric direction in activation space, scalar probe-based GRPO rewards are insufficient.\"\n\n---\n\n**[AGREE] R2-W4: 仅单一模型做 RL 训练**\n\n同意，与我的 W5 一致。\n\n---\n\n**[REBUT] R2-W5: 181 对训练数据规模偏小**\n\n部分不同意 R2 的 framing。\n\nR2 关注的是\"更大训练集是否能产生更鲁棒的 direction，缓解 cosine gap 仅 0.098 的问题\"。但论文的核心论点不是 direction 提取质量差（AUROC 0.827 已经相当不错），而是 **即使 direction 能良好区分 sycophantic vs. non-sycophantic，这个方向作为 RL reward 仍然失败**。失败的根因在 §6 中明确分析：d_syc 编码的是 belief change 的方向，而 valid revision 和 sycophantic capitulation **都沿相同方向移动**——这是一个结构性问题，不会因为更多训练数据而消失。\n\ncosine gap 0.098（§4 提到 \"the cosine gap between valid and sycophantic activations averages only 0.098 across layers\"）确实小，但这不是数据量的问题，而是反映了 valid revision 和 capitulation 在 activation space 中本身就很接近。更多 pairs 可以让 d_syc 方向估计更精确（降低 ±0.028 的 CV 方差），但不会拉大 valid/invalid activations 之间的结构性 gap。\n\n我的 W4 关注的是 pair 构建的**质量控制**（style-controlled 方法不透明），而非数量——这是更关键的问题。181 对质量不明的 pairs 和 500 对同样质量不明的 pairs 不会有本质区别。\n\n---\n\n### Missing References\n\n**[AGREE]** 三篇 missing references 均应补充。Papadatos & Freedman (2024) 和 SMART (2025) 与本文 thesis 有直接对话关系；DPO/KTO 是明显的 RL baseline 遗漏。\n\n---\n\n### Director 提出的三个具体问题\n\n**Q1: R2-N1（Papadatos & Freedman 遗漏）是否确实是 critical gap？**\n\n是的，但 critical 程度取决于该论文与本文方法的可比性。如果 Papadatos & Freedman 的 probe penalty 作用于 reward model 中间层（即修改 RM 的输出而非直接作为 policy reward），那两种方法的 failure/success 差异可以用 supervision granularity 来解释（与我的 N3 一致）——这反而**强化**本文的论点（scalar probe reward 不够，需要更细粒度的监督）。但如果该工作的 probe penalty 也是作为 scalar reward 直接给 policy optimizer 且成功了，那就是直接矛盾，必须在论文中解释。论文不讨论这一区别是不可接受的。\n\n**Q2: R2-N2（引用质量）是否影响论文可信度？**\n\n从方法严谨性角度：**是的，但程度有限**。引用不完整不改变实验结果的有效性，但 (1) ACT 的 \"Unknown\" 作者使读者无法验证这个关键 baseline 的原始定义，直接影响 reproducibility 评分；(2) 多条引用的系统性不完整暗示论文准备仓促或编辑标准低，会在审稿中产生负面信号。这是一个容易修复的问题，但在当前状态下确实降低可信度。\n\n**Q3: 我的 N1（Fisher test 误用）和 R2-N1（missing reference）哪个对论文接收影响更大？**\n\n**我的 N1 影响更大。**\n\n理由：Fisher test 误用直接攻击论文的定量推理核心——将非独立 checkpoints 当作独立样本产生虚假的 p<0.0001，使得 GRPO vs ACT 的统计对比无效。这不是可以通过补充讨论来修复的，而是需要重新设计统计分析、可能增加实验 seeds。\n\nR2-N1 的 missing reference 虽然重要，但本质上是 **framing 问题**——论文需要在 Related Work 中讨论为什么 probe penalty 在不同框架下有不同效果，并适当限定自己的 claims 范围。这是可以在 revision 中通过补充 1-2 段讨论来解决的。\n\n从 ARR 评审角度，统计方法的根本性缺陷（影响 Soundness）比相关工作遗漏（主要影响 completeness/framing）对 Overall Assessment 的负面影响更大。\n",
    "reviewer_id": "1",
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-22T10:06:32.726041+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4114
}
```

</details>

---


### Assistant

_source line 50 · 2026-05-22T10:06:42.013605+00:00_

交叉回应已提交。总结：

- **R2 的 8 条意见中，7 条 [AGREE]，1 条 [REBUT]**（R2-W5 关于 181 对数据量偏小——我认为问题是 pair 质量控制不透明而非数量不足，因为 cosine gap 0.098 是 valid/invalid activations 的结构性接近，更多数据不会改变这一点）
- 对 Director 三个问题的回答：R2-N1 确实是重要遗漏但 critical 程度取决于方法可比性；R2-N2 引用质量确实影响可信度但可快速修复；**我的 N1（Fisher test 独立性违反）对接收影响大于 R2-N1（missing reference）**，因为前者攻击 Soundness 核心，后者主要是 framing 问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1"
}
```

</details>

---


## Round 3

## Round 3

66 recorded events


### User

_source line 51 · 2026-05-22T11:29:43.854386+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性**审查。

## Venue 信息
- **目标会议**: EMNLP 2026（通过 ARR May 2026 cycle 提交）
- **截止日期**: 2026-05-25
- **页数限制**: 正文 8 页（Long paper），参考文献不限页数，Limitations 和 Ethics 不计入页数
- **模板**: ACL style（`\usepackage[hyperref]{acl}`）
- **匿名规则**: Double-blind，论文中不得包含作者信息
- **评分标准**: ARR Overall Assessment: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

## 论文路径
- LaTeX 源码: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/submitted.pdf`

## 你的审查侧重：方法严谨性

请重点审查以下方面：

1. **Direction extraction 方法**（§2.1）：
   - Contrastive pairs 的构建方法是否严谨？style-controlled 过程是否充分说明？
   - 181 pairs 的规模是否足够？evidence strength 三级标注标准是否清晰？
   - 5-fold cross-validated AUROC 的统计报告是否合理？

2. **Reward formulations**（§2.2）：
   - 三种 R1 公式（cosine、binary probe、continuous probe）的设计和参数选择是否合理？
   - 超参数 w1（仅测 0.25/0.40）是否足以排除 false negative？
   - Online recalibration 的设计是否有替代方案未探索？

3. **实验设计与统计声明**（§3-§6）：
   - 所有训练仅在 Qwen3-8B 上进行，Llama-3-8B 仅做 direction 验证——这是否足以支撑论文的一般性声明？
   - ACT seed 2 仅 3/16 checkpoints 完成——对结论可靠性有何影响？
   - Cross-seed 分析（n=2 seeds）统计效力如何？
   - NLI flip classifier 的可靠性是否有充分验证？
   - max_completion_length=256 导致 80-84% truncation 是否影响结果有效性？

4. **因果推断**（§6）：
   - ACT vs GRPO 对比是否存在 supervision granularity confound（per-token vs per-completion）？
   - "supervision density hypothesis" 是否过度 claim？
   - 论文是否正确区分了"d_syc 作为 reward 失败"和"scalar per-completion reward 结构性不足"？

5. **评估指标**：
   - SyconScore 的 harmonic mean 设计选择是否有理据？
   - ToF/NoF 分类依赖 DeBERTa NLI，准确率是否报告？

请按 ARR 标准给出完整审稿报告：Summary → Strengths → Weaknesses（区分 Must-Fix / Should-Fix / Minor） → Questions → Missing References → Overall Assessment（含评分和置信度）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 52 · 2026-05-22T11:29:51.697067+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
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

_source line 53 · 2026-05-22T11:29:51.747827+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 54 · 2026-05-22T11:29:55.416369+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 55 · 2026-05-22T11:29:56.422087+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/submitted.pdf",
  "project": "contrastive_entrain_calib",
  "pages": "1-8",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/submitted.pdf",
    "project": "contrastive_entrain_calib",
    "pages": "1-8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 56 · 2026-05-22T11:30:02.259465+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I found relevant information about ACL ARR 2026 reviewer guidelines, review form, and criteria. Here's what the search results show:

## Review Form Criteria

For Findings papers, the main criteria are soundness and reproducibility, while conference rec
…[truncated 1073 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6843
}
```

</details>

---


### Tool result

_source line 57 · 2026-05-22T11:30:04.084144+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 416.6}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.3}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 438.6}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 446.5}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 476.0}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 443.3}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 493.2}], \"total_pages\": 10, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrast
…[truncated 95 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7662
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-22T11:30:09.638836+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract all review form fields, scoring dimensions, and their scales. I need the complete list of criteria reviewers must evaluate, including: soundness, excitement/novelty, overall assessment scale, confidence, and any other dimensions. For each dimension, list the exact scale (e.g., 1-5) and what each score means."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract all review form fields, scoring dimensions, and their scales. I need the complete list of criteria reviewers must evaluate, including: soundness, excitement/novelty, overall assessment scale, confidence, and any other dimensions. For each dimension, list the exact scale (e.g., 1-5) and what each score means."
  }
}
```

</details>

---


### Tool call

_source line 59 · 2026-05-22T11:30:10.646028+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 60 · 2026-05-22T11:30:11.198521+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 61 · 2026-05-22T11:30:11.553047+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 62 · 2026-05-22T11:30:11.654078+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 63 · 2026-05-22T11:30:12.208171+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 64 · 2026-05-22T11:30:12.361901+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1163
}
```

</details>

---


### Tool result

_source line 65 · 2026-05-22T11:30:13.574615+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1920
}
```

</details>

---


### Tool result

_source line 66 · 2026-05-22T11:30:13.980358+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1772
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-22T11:30:17.620125+00:00_

# ACL Rolling Review - Form Evaluation Dimensions

## Review Form Fields & Scoring Dimensions

### 1. **Reviewer Confidence** (1-5 scale)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: Quite sure; unlikely to have missed important details
- **3**: Pretty sure, but may have overlooked some aspects
- **2**: Can defend evaluation, but likely missed details or novelty assessment
- **1**: Outside expertise area or paper difficult to understand

### 2. **Soundness** (1-5 scale with half-point options)
- **5**: Exceptional thoroughness for paper type
- **4**: Sufficient support for claims; minor experiments optional
- **3**: Main claims adequately supported; minor gaps acceptable
- **2**: Major claims lack support; significant technical/methodological issues
- **1**: Insufficient rigor for publication or not ACL-relevant

### 3. **Excitement** (1-5 scale with half-point options)
Focus: subjective assessment of innovation, impact potential, and relevance

- **5**: Highly exciting; recommend to others
- **4**: Exciting; would mention to colleagues
- **3**: Interesting; might attend presentation
- **2**: Potentially interesting to some community members
- **1**: Not relevant to computational linguistics community

### 4. **Overall Assessment** (1-5 scale with half-point options)
- **5**: Award consideration (top 2.5%)
- **4**: Conference acceptance recommended
- **3**: Findings acceptance recommended
- **2**: Resubmit next cycle (substantial revisions needed)
- **1**: Do not resubmit or not ACL-relevant

### 5. **Reproducibility** (1-5 scale)
- **5**: Results easily reproducible
- **4**: Mostly reproducible with minor variations
- **3**: Reproducible with difficulty; underspecified parameters
- **2**: Hard to reproduce; unavailable data or insufficient details
- **1**: Irreproducible regardless of effort

### 6. **Datasets Contribution** (1-5 scale)
- **5**: Enabling; affects research direction
- 
…[truncated 865 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7981
}
```

</details>

---


### Tool call

_source line 68 · 2026-05-22T11:30:22.239131+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 69 · 2026-05-22T11:30:22.642622+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 70 · 2026-05-22T11:30:23.146225+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 71 · 2026-05-22T11:30:23.146708+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 72 · 2026-05-22T11:30:24.104271+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1461
}
```

</details>

---


### Tool result

_source line 73 · 2026-05-22T11:30:24.105505+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool call

_source line 74 · 2026-05-22T11:30:24.206224+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 75 · 2026-05-22T11:30:25.111545+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/submitted.pdf",
  "project": "contrastive_entrain_calib",
  "pages": "9-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/submitted.pdf",
    "project": "contrastive_entrain_calib",
    "pages": "9-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 76 · 2026-05-22T11:30:25.162948+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool result

_source line 77 · 2026-05-22T11:30:25.567245+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 491.6}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 509.0}], \"total_pages\": 10, \"rendered_pages\": 2, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 78 · 2026-05-22T11:30:29.832029+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 79 · 2026-05-22T11:30:30.285316+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 80 · 2026-05-22T11:30:30.639573+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 807
}
```

</details>

---


### Tool result

_source line 81 · 2026-05-22T11:30:31.042401+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 757
}
```

</details>

---


### Tool call

_source line 82 · 2026-05-22T11:30:35.719340+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 83 · 2026-05-22T11:30:35.770286+00:00_

1	\documentclass[11pt,a4paper]{article}
2	\usepackage[hyperref]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{graphicx}
10	\usepackage{xcolor}
11	\usepackage{subcaption}
12	
13	\newcommand{\dsyc}{d_{\text{syc}}}
14	\newcommand{\tof}{\text{ToF}}
15	\newcommand{\nof}{\text{NoF}}
16	\newcommand{\sycon}{\textsc{SyconScore}}
17	\newcommand{\rone}{R_1}
18	\newcommand{\rthree}{R_3}
19	
20	\title{Discriminability Without Utility: Why Sycophancy Directions Fail as Scalar RL Rewards}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\begin{abstract}
28	\input{sections/abstract}
29	\end{abstract}
30	
31	\input{sections/introduction}
32	
33	\input{sections/framework}
34	
35	\input{sections/direction_quality}
36	
37	\input{sections/cosine_failure}
38	
39	\input{sections/probe_trap}
40	
41	\input{sections/discussion}
42	
43	\input{sections/related_work}
44	
45	\input{sections/conclusion}
46	
47	\section*{Limitations}
48	\input{sections/limitations}
49	
50	\bibliography{references}
51	
52	\appendix
53	\input{sections/appendix}
54	
55	\end{document}
56	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 84 · 2026-05-22T11:30:39.109096+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 85 · 2026-05-22T11:30:39.160283+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 86 · 2026-05-22T11:30:42.082237+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-22T11:30:42.132967+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/probe_trap.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/direction_quality.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 88 · 2026-05-22T11:30:45.593071+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex"
  }
}
```

</details>

---


### Tool result

_source line 89 · 2026-05-22T11:30:46.046046+00:00_

1	\section{Experimental Framework}
2	\label{sec:framework}
3	
4	\subsection{Direction Extraction}
5	\label{ssec:extraction}
6	
7	We extract a linear sycophancy direction $\dsyc$ from the residual stream using contrastive activation pairs: a \emph{valid correction} (warranted belief revision under strong evidence) and a \emph{sycophantic capitulation} (unwarranted concession under social pressure).
8	We construct 181 contrastive pairs using GPT-4.1 in a two-stage pipeline: skeleton generation followed by 3-turn dialogue completion.
9	Style matching is enforced by automated validation (response length difference ${<}10\%$, shared opening phrase ${\geq}2$ words), with up to 3 retries per pair; 19 of 200 initial pairs were discarded for failing validation.
10	Evidence strength is annotated at three levels: \emph{weak} (75 pairs; personal memory or opinion), \emph{medium} (54 pairs; brief source citation), and \emph{strong} (52 pairs; authoritative source with detailed data).
11	From the 181 paired examples (362 activations total), we compute the mean difference at target layer $\ell$:
12	\begin{equation}
13	\label{eq:dsyc}
14	\dsyc = \frac{1}{N}\sum_{i=1}^{N}\left(\mathbf{h}^{+}_i - \mathbf{h}^{-}_i\right)
15	\end{equation}
16	where $\mathbf{h}^{+}_i$ and $\mathbf{h}^{-}_i$ are residual-stream activations for the $i$-th valid and sycophantic response.
17	The target layer is selected by 5-fold cross-validated AUROC; on Qwen3-8B this yields layer 19 with AUROC $0.827$ (5-fold CV $\sigma{=}0.028$).
18	
19	\subsection{Reward Formulations}
20	\label{ssec:reward}
21	
22	GRPO \citep{shao2024grpo} ranks sampled completions by reward and updates the policy toward higher-reward outputs.
23	We define $R = w_1 \cdot \rone + w_3 \cdot \rthree$, where $\rone$ is a direction-based component and $\rthree$ is a behavioral component (DeBERTa NLI classifier scoring consistency with the ground-truth answer).
24	Three formulations translate $\dsyc$ into $\rone$:
25	\begin{itemize}
26	\item[
…[truncated 2794 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 90 · 2026-05-22T11:30:46.146974+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/direction_quality.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/direction_quality.tex"
  }
}
```

</details>

---


### Tool result

_source line 91 · 2026-05-22T11:30:46.498761+00:00_

1	\section{Direction Discriminability}
2	\label{sec:direction_quality}
3	
4	Before evaluating $\dsyc$ as a reward signal (\S\ref{sec:cosine_failure}--\S\ref{sec:probe_trap}), we first establish that it captures a genuine sycophancy-related signal in the residual stream.
5	If the direction failed to discriminate sycophantic from non-sycophantic activations, downstream reward failures would be trivially explained by poor direction quality rather than by a fundamental gap between discriminability and reward utility.
6	We evaluate discriminability along five axes: cross-validated classification accuracy, evidence-strength stratification, cross-model transfer, training stability, and probe ablation.
7	Figure~\ref{fig:direction_quality} summarizes the per-layer AUROC profiles for both models.
8	
9	\paragraph{Qwen3-8B layer-wise discriminability.}
10	We evaluate $\dsyc$ via 5-fold cross-validated AUROC on 181 style-controlled contrastive pairs (\S\ref{ssec:extraction}).
11	The direction achieves AUROC $0.827$ (5-fold CV $\sigma{=}0.028$) at its best layer (L19).
12	Discriminability emerges gradually across depth: layers L0--L8 perform near chance, statistical significance ($p < 0.01$) first appears at L16, and performance peaks at L19.
13	This gradual emergence, with the peak in the upper third of the network, suggests that sycophancy-relevant information is encoded as a late-stage representation rather than an input-level confound.
14	The direction also captures evidential granularity.
15	AUROC rises monotonically from 0.675 on weak-evidence pairs to 0.883 on medium and 0.929 on strong pairs.
16	This gradient indicates that $\dsyc$ encodes the degree of evidential warrant, not merely a binary sycophancy label.
17	
18	\paragraph{Cross-model generalization.}
19	To rule out that these results are specific to Qwen3-8B's representation geometry, we repeat the full extraction and evaluation pipeline on Llama-3-8B-Instruct.
20	Table~\ref{tab:cross_model} compares the two models.
…[truncated 3493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 92 · 2026-05-22T11:30:46.599552+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex"
  }
}
```

</details>

---


### Tool result

_source line 93 · 2026-05-22T11:30:47.102064+00:00_

1	\section{Cosine \texorpdfstring{$\rone$}{R1}: Structural Failure}
2	\label{sec:cosine_failure}
3	
4	Section~\ref{sec:direction_quality} established that $\dsyc$ achieves AUROC 0.827 on Qwen3-8B.
5	We now test whether this discriminability translates into a viable GRPO reward.
6	Four configurations form a diagnostic chain (Table~\ref{tab:cosine_chain}): each resolves the failure mode of its predecessor but exposes a deeper limitation.
7	
8	\begin{table}[t]
9	\centering
10	\caption{Cosine $\rone$ failure chain on Qwen3-8B (LoRA rank$=$64, GRPO with $R = w_1 \cdot \rone + w_3 \cdot \rthree$).}
11	\label{tab:cosine_chain}
12	\begin{tabular}{lllll}
13	\toprule
14	Config & $\rone$ Formula & $w_1$ & Outcome & Root Cause \\
15	\midrule
16	F1a & $\tanh(\mathbf{h}\cdot\dsyc/20)$ & 0.25 & Gate saturation & Norm mismatch \\
17	F1b & $\cos(\mathbf{h},\, \dsyc)$ & 0.25 & $\rone \approx 0$ & Gap too small \\
18	F1c & +recalibration & 0.25 & Mode collapse & Reward discontinuity \\
19	F1d & $5\cos(\mathbf{h},\, \dsyc)$ & 0.40 & Mode collapse & $\rthree$ saturation \\
20	\bottomrule
21	\end{tabular}
22	\end{table}
23	
24	F1a uses a dot-product formulation ($\rone = \tanh(\mathbf{h} \cdot \dsyc / 20)$), but residual-stream norms exceed the direction norm by $100$--$1{,}200{\times}$, saturating the tanh gate and zeroing the gradient by step 955.
25	Switching to cosine similarity (F1b) eliminates norm dependence, yet the cosine gap between valid and sycophantic activations averages only 0.098 across layers---too narrow to generate meaningful reward contrast.
26	Online recalibration (F1c, \S\ref{ssec:recalib}) raises offline AUROC from 0.827 to 0.910 but paradoxically triggers mode collapse: the abrupt shift in $\dsyc$ at each recalibration event creates a reward discontinuity that destabilizes GRPO advantage estimates, collapsing entropy to 0.069 within 300 steps.
27	Amplifying the signal with $5{\times}$ scaling (F1d) lifts $\rone$ above the noise floor but simultaneously amplifies t
…[truncated 836 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 94 · 2026-05-22T11:30:47.102519+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/probe_trap.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/probe_trap.tex"
  }
}
```

</details>

---


### Tool result

_source line 95 · 2026-05-22T11:30:47.153130+00:00_

1	\section{The Probe Reward Trap}
2	\label{sec:probe_trap}
3	
4	The cosine formulations fail because the continuous projection of $\dsyc$ produces a gap too narrow for reward contrast.
5	A natural remedy is to discretize: train a logistic probe on $\dsyc$ and threshold its output, yielding $\rone = \mathbb{I}[P(\text{syc} \mid \mathbf{h}) < 0.5]$ (F2 in \S\ref{ssec:reward}).
6	We show that this discretization sidesteps the magnitude problem but creates a qualitatively worse failure.
7	
8	\paragraph{Differentiable probe: gradient gaming.}
9	Without stop-gradient (exp-008), the policy discovers within ${\sim}30$ steps that shifting activations away from the sycophancy cluster maximizes $\rone$ regardless of response content, producing an inverted profile ($\tof = 0.978$, $\nof = 0.006$).
10	This motivates the frozen-probe design below.
11	
12	\paragraph{Binary probe: the stubbornness trap.}
13	With stop-gradient (exp-008v3), the policy cannot game the boundary but instead exploits a deeper flaw: $\dsyc$ does not condition on input validity, so refusing to revise a wrong answer receives the same $\rone = 1$ as correctly resisting invalid pressure.
14	By step 500, $\tof$ drops to 0.000 and $\nof$ reaches 0.995, yielding $\sycon = 0$.
15	Qualitative analysis reveals distinct failure modes: \emph{sycophantic stubbornness} (24\%), where the model verbally agrees but does not change its answer; \emph{deliberation traps} (29\%), where the model identifies the correct answer but cannot commit; and evidence-graded hedging, where the model adjusts its refusal style rather than its acceptance rate (Appendix~\ref{app:taxonomy}).
16	
17	\paragraph{Behavioral death precedes distributional collapse.}
18	
19	\begin{table}[t]
20	\centering
21	\caption{Probe reward trap trajectory (exp-008v3). Behavioral death ($\tof{=}0$) occurs at step 500; entropy remains healthy until step ${\sim}1840$. Reward averages $+0.72$ throughout.}
22	\label{tab:probe_trajectory}
23	\begin{tabular}{lccccc}

…[truncated 2145 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 96 · 2026-05-22T11:30:52.129596+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-22T11:30:52.481538+00:00_

1	\section{Analysis: Discriminability $\neq$ Reward Utility}\label{sec:discussion}
2	
3	\paragraph{Unified root cause.}
4	The failures in Sections~\ref{sec:cosine_failure} and~\ref{sec:probe_trap} trace to a single geometric limitation.
5	$\dsyc$ encodes the \emph{direction} of belief change but not its \emph{evidential warrant}: valid revision and sycophantic capitulation both shift activations toward the user's position along the same direction.
6	The two reward families expose complementary faces of this blindness.
7	Cosine $\rone$ penalizes all belief change indiscriminately; the resulting mode collapse (F1c, F1d) reflects excessive punishment of any activation shift along $\dsyc$.
8	The binary probe $\rone$ rewards all resistance regardless of input validity; the stubbornness trap ($\tof = 0$ by step 500) reflects excessive permissiveness toward activation stasis.
9	These are not independent design flaws but dual consequences of a direction that conflates the target behavior (resisting invalid challenges) with its complement (refusing valid corrections).
10	Cross-model evidence confirms the limitation extends beyond Qwen3-8B: Llama-3-8B independently achieves AUROC $0.779$ (5-fold CV $\sigma{=}0.019$) on the same contrastive pairs with the same monotonic evidence gradient, so discriminability generalizes across architectures while the semantic gap between discriminability and reward utility persists.
11	This pattern contrasts with reasoning faithfulness and safety directions~\citep{zhang2026latentgrpo}, where the behavior to suppress is geometrically distinct from the behavior to preserve along the relevant direction.
12	For sycophancy, the target and its complement occupy the same activation region; they differ only in whether external evidence warrants the belief change.
13	
14	\paragraph{GRPO stubbornness across all formulations.}
15	
16	\begin{table}[t]
17	\centering
18	\caption{Comparison of all sycophancy calibration methods on Qwen3-8B. $\sycon$ is the h
…[truncated 7519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 98 · 2026-05-22T11:30:52.632747+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 99 · 2026-05-22T11:30:52.884208+00:00_

1	All RL and SFT experiments use Qwen3-8B exclusively; we validate $\dsyc$ discriminability on Llama-3-8B (AUROC $0.779$, 5-fold CV $\sigma{=}0.019$; Table~\ref{tab:cross_model}) but do not replicate training on a second model due to compute constraints (${\sim}200$ H100-equivalent hours).
2	ACT cross-seed verification is partial: seed 2 has completed 3 of 16 checkpoints at submission time (all exceeding vanilla), and full replication is ongoing.
3	Our evaluation categorizes user challenges as binary valid or invalid, whereas real-world belief revision spans a continuous spectrum of evidential strength; intermediate cases may prove easier to separate in activation space.
4	
5	A supervision granularity confound limits our causal claims: ACT uses dense per-token supervision while all GRPO variants use scalar per-completion rewards.
6	We cannot fully disentangle whether failures stem from compressing $\dsyc$ into a scalar or from the per-completion reward structure itself; the supervision density hypothesis (\S\ref{sec:discussion}) remains a hypothesis.
7	Finally, $n{=}2$ seeds for GRPO and partial seed 2 data for ACT are insufficient to establish statistical reproducibility, though qualitative patterns (oscillatory degradation, crash depth, late-stage flatness) are consistent across seeds.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 100 · 2026-05-22T11:30:52.884708+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-22T11:30:53.036147+00:00_

1	\section{Training Details}
2	\label{app:training}
3	
4	\paragraph{Reward weight selection.}
5	The weight $w_1$ is set by diagnostic-driven iteration: $w_1{=}0.25$ was initially chosen to down-weight the noisy cosine reward term; this was later increased to $w_1{=}0.40$ for F1d after diagnostics revealed that $w_1{=}0.25$ allowed the cosine term to contribute only ${\sim}8.3\%$ of total reward variance.
6	The empirical scaling factor in F1a ($\dsyc/20$) is a heuristic normalization; we did not find it critical to the failure modes reported.
7	
8	\paragraph{Response truncation.}
9	All GRPO experiments use \texttt{max\_completion\_length}=256, resulting in 80--84\% truncation of multi-turn responses.
10	This setting is shared across all conditions and does not affect relative comparisons; we retain it because response-level decisions typically manifest within the first 100--200 tokens.
11	
12	\section{Stubbornness Taxonomy}
13	\label{app:taxonomy}
14	
15	Manual inspection of 100 probe-trained responses (exp-008v3, step 2000) reveals three dominant failure modes.
16	\emph{Sycophantic stubbornness} (24\%): the model produces agreement markers (``you're right,'' ``good point'') but retains its original answer verbatim, simultaneously sycophantic and stubborn.
17	\emph{Deliberation traps} (29\%): the model explicitly identifies the correct revised answer during its reasoning chain but fails to commit, reverting to the original answer in the final output.
18	\emph{Evidence-graded hedging}: under weak evidence, responses show surface compliance without substantive change; under strong evidence, responses add explicit hedging (``this is debatable,'' ``there are multiple perspectives'').
19	The model learns to modulate its \emph{refusal style} in response to evidence strength rather than adjusting its \emph{acceptance rate}, confirming that the probe reward optimizes surface markers rather than epistemic calibration.
20	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-22T11:30:56.901670+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 103 · 2026-05-22T11:30:57.955659+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Representation engineering \citep{zou2023repe} reveals that large language models encode sycophancy as a linear direction in their residual streams.
5	A contrastive sycophancy direction $\dsyc$, extracted from style-controlled pairs of valid belief revision and sycophantic capitulation, achieves cross-validated AUROC $0.827$ (5-fold CV $\sigma{=}0.028$) on Qwen3-8B and $0.779$ (5-fold CV $\sigma{=}0.019$) on Llama-3-8B (\S\ref{sec:direction_quality}).
6	The direction captures evidential granularity: discriminability rises monotonically from weak-evidence pairs (AUROC 0.675) through medium (0.883) to strong (0.929), and the signal remains stable under LoRA training with cosine drift of approximately 0.96 at 500 steps.
7	These results, replicated across two architecturally distinct model families, point to an appealing possibility: if the model's representations already separate sycophantic from non-sycophantic behavior, that separation should be convertible into a scalar reward signal for reinforcement learning.
8	Sycophancy is among the most persistent alignment failures in deployed systems \citep{sharma2023sycophancy}, and a representation-level reward could complement existing behavioral approaches by targeting the internal computation rather than its surface outputs.
9	
10	This paper shows that the conversion fails, and that the failure runs deeper than the representation signal itself.
11	We test three formulations that translate $\dsyc$ into a GRPO \citep{shao2024grpo} training signal (cosine projection, binary probe, and continuous probe) across six experimental configurations; every formulation fails.
12	Cosine similarity produces a reward gap of just 0.098 between valid and sycophantic activations, too narrow to drive policy updates (\S\ref{sec:cosine_failure}).
13	Online recalibration improves the offline AUROC from 0.827 to 0.910 yet triggers mode collapse.
14	A binary probe with stopped gradients cr
…[truncated 5141 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1053
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-22T11:30:57.956051+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 105 · 2026-05-22T11:30:57.956256+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work tested whether a representation direction that detects sycophantic behavior can serve as an effective scalar reward signal.
4	We established that $\dsyc$ achieves strong offline discriminability (AUROC 0.827 on Qwen3-8B, 0.779 on Llama-3-8B), yet all three reward formulations failed across six GRPO configurations---the probe reward produced a stubbornness trap ($\tof = 0$ by step 500), and $\rthree$-only GRPO exceeded vanilla at only 4 of 26 checkpoints (15.4\% vs.\ 100\% for ACT seed 1).
5	The root cause is that $\dsyc$ encodes \emph{whether} belief changed, not \emph{whether it should have}; ACT's $\sycon = 0.301$ through dense per-token supervision confirms that the missing ingredient is token-level resolution of which belief changes are appropriate---a distinction that scalar reward compression discards.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 106 · 2026-05-22T11:30:58.107040+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 107 · 2026-05-22T11:30:58.107472+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Representation Engineering.}
4	Linear directions in LLM residual streams encode behavioral concepts \citep{zou2023repe}; inference-time methods---ITI \citep{li2023iti}, ActAdd \citep{turner2023actadd}, CAA \citep{rimsky2024caa}---demonstrate that activation geometry suffices for behavioral control \citep{burns2023ccs}.
5	We use the same contrastive extraction as CAA but apply $\dsyc$ as an RL reward, revealing a gap that inference-time work does not encounter.
6	
7	\paragraph{Reward Design and Overoptimization.}
8	Proxy rewards diverge from true objectives under sustained optimization \citep{gao2023scaling}, and reward hacking can escalate to active tampering \citep{denison2024subterfuge}.
9	Our probe trap (\S\ref{sec:probe_trap}) is an extreme instance: the reward actively reinforces degenerate behavior rather than merely being circumvented \citep{skalse2022hacking}.
10	
11	\paragraph{Sycophancy Characterization and Mitigation.}
12	Sycophancy is pervasive in RLHF-trained assistants \citep{sharma2023sycophancy}, amplified by RLHF \citep{shapira2026amplifies}, and traceable to late-layer preference shifts \citep{wang2025internal}; mitigation approaches include synthetic data \citep{wei2024synthetic}, consistency training \citep{consistency2025bctact}, and neuron-level correction \citep{obrien2025fewbadneurons}.
13	Our analysis shows why the step from diagnosis to reward is structurally blocked: $\dsyc$ conflates warranted revision with unwarranted capitulation.
14	
15	\paragraph{Probe-Based Inference-Time Mitigation.}
16	\citet{papadatos2024probepenalties} reduce sycophancy via Best-of-N reranking with linear probe penalties (94\% probe accuracy), where the probe selects among candidates without producing gradients that update model parameters.
17	Our work reveals what happens when a comparable signal (AUROC 0.82) enters the GRPO training loop: the discriminability--utility gap is specific to gradient-b
…[truncated 1020 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 108 · 2026-05-22T11:31:04.785107+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract all specific guidance for reviewers: what to look for in methodology, experiments, claims, statistical significance, reproducibility. What are the specific criteria for soundness scoring? What counts as a strength vs weakness? Any guidance on how to assess novelty, experimental rigor, or claims being supported by evidence?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract all specific guidance for reviewers: what to look for in methodology, experiments, claims, statistical significance, reproducibility. What are the specific criteria for soundness scoring? What counts as a strength vs weakness? Any guidance on how to assess novelty, experimental rigor, or claims being supported by evidence?"
  }
}
```

</details>

---


### Tool result

_source line 109 · 2026-05-22T11:31:12.139058+00:00_

# ARR Reviewer Guidelines: Assessment Criteria for Soundness and Quality

## Methodology Issues (M)

**M1 - LLM Evaluation:** Validate LLM reliability "in this context" before using them as automated evaluators.

**M2 - Reproducibility:** Check for sufficient experimental details, hyperparameter selection, and clarity about code/data availability. Papers should enable reproduction of results.

**M3 - Data Quality:** Watch for undisclosed problems in provided datasets that authors haven't discussed.

**M4 - Selection Justification:** Verify the sample of models and benchmarks is "appropriate for their claims" and motivation is clear.

**M5 - Formal Rigor:** Ensure "all assumptions should be clearly stated" and proofs are "complete and correct."

## Experimental Results Issues (R)

**R1 - Analysis Soundness:** Flag "inappropriate/misleading statistics," p-hacking, or "baselines that are not sufficiently well-tuned for fair comparison."

**R2 - Claim Scope:** Verify claims match the evaluation scope (e.g., "few QA benchmarks ≠ 'reasoning'").

**R3 - Evidence-Based Claims:** Ensure "every claim that is made has to be based on evidence or arguments."

**R4 - Framing Accuracy:** Reject overclaiming like concluding LLMs "understand" language without construct validation.

**R5 - Statistical Rigor:** Require "appropriate information about statistical significance (error bars, confidence intervals, statistical significance tests)."

## Strength vs. Weakness Distinctions

The guidelines identify common **false negatives** reviewers shouldn't treat as weaknesses:

- Simple solutions (H7)
- Negative results (H6)
- Non-SOTA contributions (H5)
- Niche topics (H9)
- Non-English work (H10)

Valid weaknesses require specific justification rather than general statements.

## Soundness Score Criteria

Soundness scores must be "justified by the text of the review." Low scores without clear faults indicate unconscious bias. Papers must be "sufficiently sound and reproducible" for accept
…[truncated 19 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7353
}
```

</details>

---


### Tool call

_source line 110 · 2026-05-22T11:34:28.501413+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 审稿报告：方法严谨性审查\n\n**论文标题**: Discriminability Without Utility: Why Sycophancy Directions Fail as Scalar RL Rewards\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审查侧重**: 方法严谨性\n\n---\n\n## Paper Summary\n\n本文研究对比提取的 sycophancy direction (d_syc) 能否作为 GRPO 的标量 reward 信号来校准 LLM 的 sycophancy 行为。作者在 Qwen3-8B 上提取 d_syc（5-fold CV AUROC 0.827），测试三种 reward 公式（cosine projection、binary probe、continuous probe）共六种配置，结果全部失败。论文进一步展示 R3-only GRPO（仅用 NLI 行为 reward）也失败（26 个 checkpoint 仅 4 个超过 vanilla），而 ACT（dense per-token SFT）以 SyconScore 0.301 成功。核心论点是 d_syc 编码了\"是否发生信念变化\"而非\"信念变化是否有证据支撑\"，且标量 per-completion reward 结构性地无法传达 valid/invalid 区分。\n\n---\n\n## Summary of Strengths\n\n**S1. 问题选取极佳，填补重要空白。** representation engineering 的线性方向能否直接转化为 RL reward？这是社区普遍假设但未被系统检验的前提。本文是首个在 sycophancy 校准上系统否证该前提的工作，具有重要理论意义。\n\n**S2. 诊断链设计严谨且有教学价值。** §4 的 cosine failure chain（F1a→F1b→F1c→F1d）是一个精心设计的渐进式消融，每一步解决前一步的 failure mode 但暴露更深层问题。这种叙事结构使论文的论证逻辑非常清晰。\n\n**S3. Probe reward trap 的发现有实际安全意义。** behavioral death（ToF=0 at step 500）先于 distributional collapse（entropy collapse at step ~1840）的 1300-step 时间差，且 reward 始终保持 +0.72——这意味着标准的 entropy-based early stopping 会完全错过行为退化。这对 RLHF 安全监控实践有直接启示。\n\n**S4. Limitations 写作诚实。** 论文在 Limitations 中主动承认了多项关键局限（单模型训练、ACT seed 2 不完整、n=2 seeds 的统计效力、supervision granularity confound）。这种透明性值得肯定。\n\n**S5. Cross-model direction validation 增强了 d_syc 分析的可信度。** 在 Llama-3-8B 上独立复现了 direction extraction，evidence-strength gradient 的定性模式一致，表明 d_syc 的几何性质不是模型特异的。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1 [critical] ACT vs GRPO 对比存在多重混淆变量，\"supervision density hypothesis\" 过度声称**\n\n- 具体位置：§6 \"The supervision density hypothesis\" 段落；Introduction C3；Conclusion\n- 问题：论文将 ACT 的成功归因于 \"supervision density\"（per-token vs per-completion），但 ACT 和 GRPO 至少在以下维度同时不同：\n  - (a) per-token vs per-completion 梯度粒度\n  - (b) SFT（交叉熵）vs RL（REINFORCE/GRPO）目标函数\n  - (c) ACT 使用 labeled valid/invalid pairs（有标签监督），GRPO 使用 sampled completions（无标签）\n  - (d) ACT 额外包含 L2 activation consistency loss\n  \n  当至少有 4 个同时变化的因素时，将因果归因到 \"supervision density\" 这一个维度上是不合理的。ACT 的成功可能主要因为它使用了 **labeled examples**（直接告诉模型哪些 belief change 是 warranted 的），而不是因为 per-token supervision。论文在 Limitations 中承认了这一 confound，但正文（尤其 Introduction C3 和 Conclusion）的措辞远比 Limitations 中的 hedge 更强。\n  \n  §6 最后一句\"we expect similar failure patterns wherever representation-derived signals are compressed to completion-level scalars\"——这是从单一模型、单一 RL 算法的实验外推到整个 per-completion RL 方法类别的推测性声称。\n\n- 为什么影响接收：C3 是论文三个 contribution 之一。如果 ACT 的优势来自 labeled supervision 而非 supervision density，论文的核心叙事（discriminability ≠ utility, 且 sparse reward 结构性不足）的第二层（sparse reward 不足）就不成立。\n  \n- 建议修改方向：\n  - 明确列出 ACT 与 GRPO 的所有差异维度，并在正文（不只是 Limitations）中讨论替代解释\n  - 将 \"supervision density hypothesis\" 降级为多个可能解释之一，而非论文的核心 contribution\n  - 增加消融实验以隔离因素：例如 (1) per-token RL（如 token-level GRPO/PPO）vs per-completion GRPO，(2) 使用 labeled pairs 的 GRPO（而非 sampled completions）\n  - 或者将 C3 重新表述为观察性发现而非因果声称\n\n**N2 [critical] 实验仅在 Qwen3-8B 上训练，不足以支撑论文的一般性声称**\n\n- 具体位置：Title（\"Why Sycophancy Directions Fail as Scalar RL Rewards\"——一般性陈述）；Introduction（\"scalar per-completion RL is structurally insufficient for sycophancy calibration\"）；§6（\"the scalar per-completion reward structure is shared by PPO, RLOO, and other REINFORCE-style methods\"）\n- 问题：所有 RL 和 SFT 训练实验仅在 Qwen3-8B 一个模型上进行。Llama-3-8B 仅用于 direction extraction 验证，未进行任何训练实验。论文标题和正文使用一般性措辞（\"sycophancy directions fail\"、\"structurally insufficient\"），但仅有单模型证据。\n  \n  更重要的是，GRPO 的 failure modes 可能与 Qwen3-8B 的特定特性有关（如 residual stream 的几何结构、RL 训练动态），在其他模型上可能表现不同。论文自身展示了两个模型的 d_syc 最佳层不同（L19 vs L16）、AUROC 不同（0.827 vs 0.779），这暗示模型间的差异可能影响训练动态。\n\n- 为什么影响接收：标题和核心 claim 的一般性远超实验证据的范围。ARR 指南明确要求 \"claims match the evaluation scope\"（R2）。\n  \n- 建议修改方向：\n  - 在标题或 abstract 中明确限定实验范围（\"on Qwen3-8B\" 或 \"a case study\"）\n  - 在 Llama-3-8B 上至少复现一个关键实验（如 binary probe F2）以测试跨模型一致性\n  - 或将一般性声称显著软化：从 \"fail\" → \"failed in our experiments\"；从 \"structurally insufficient\" → \"insufficient in the tested configuration\"\n\n**N3 [critical] 统计效力严重不足：n=2 seeds、ACT seed 2 仅 3/16 checkpoints**\n\n- 具体位置：Table 4（主对比表）；§6（cross-seed analysis）；Limitations\n- 问题：\n  - GRPO 使用 n=2 seeds。论文报告了 cross-seed rank correlation 在 step 4000 后降至 ρ≈0.33 (n.s.)，但 n=2 的相关性几乎没有任何统计意义——任何两条随机曲线都可能在某些区间有高相关。\n  - ACT seed 2 仅完成 3/16 checkpoints。Table 4 将 ACT seed 1 的完整结果（16/16 checkpoints 全部超过 vanilla）作为核心证据，但仅有 1 个完整 seed。3/16 的部分数据被标注为 \"ongoing\"，这意味着论文在实验未完成时就提交了。\n  - \"4/26 checkpoints (15.4%) exceed vanilla\" vs \"16/16 (100%)\" 的对比在统计上并不如看起来那么有力：不同方法在不同 training stages 有不同 dynamics，逐 checkpoint 比较忽略了时间序列的自相关性。\n\n- 为什么影响接收：ARR 指南要求 \"appropriate information about statistical significance\"（R5）。n=2 seeds 的 cross-seed 分析、incomplete seed 2 数据、以及缺乏置信区间或显著性检验的主对比，都低于会议论文的标准。\n\n- 建议修改方向：\n  - 至少增加到 n=3 seeds（GRPO 和 ACT 各 3 seeds），报告 mean±std\n  - 完成 ACT seed 2 的全部 16 checkpoints 评估\n  - 对 Table 4 的关键对比（如 GRPO best vs ACT best）报告置信区间或 bootstrap test\n  - 如果计算资源不足以增加 seeds，应在正文中大幅软化比较性声称\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1 [warning] max_completion_length=256 导致 80-84% truncation，可能系统性偏倚结果**\n\n- 具体位置：Appendix A（Response truncation）\n- 问题：所有 GRPO 实验使用 max_completion_length=256，导致 80-84% 的 multi-turn responses 被截断。论文声称 \"this setting is shared across all conditions and does not affect relative comparisons\"，以及 \"response-level decisions typically manifest within the first 100-200 tokens\"。\n  \n  但这两个辩护都有问题。首先，截断对不同 reward formulation 的影响可能不同：binary probe 只需看 final representation（受截断影响小），而 cosine reward 依赖于 activation 的连续变化（可能更受截断影响）。其次，\"decisions manifest within 100-200 tokens\" 是一个未验证的断言。一个正在进行 nuanced belief revision 的模型可能需要更多 token 来表达，而简单拒绝修改只需很少 token——截断可能系统性地惩罚 warranted revision。\n\n- 建议：(1) 在至少一个配置上测试 max_completion_length=512 或更高，验证截断不影响 failure modes 的定性结论；(2) 提供截断对 ToF vs NoF responses 的差异化影响分析。\n\n**W2 [warning] NLI 分类器同时用于 R3 reward 和 ToF/NoF 评估，存在评估循环性**\n\n- 具体位置：§2.5（Evaluation）——使用 DeBERTa NLI 做 stance classification；§2.2——R3 也是 DeBERTa NLI classifier\n- 问题：R3 reward component 使用 DeBERTa NLI 判断模型回答与 ground truth 的一致性；ToF/NoF 评估也使用同一个 DeBERTa NLI classifier（cross-encoder/nli-deberta-v3-base）判断 stance flip。这创造了一个评估循环：训练用 NLI classifier 给 reward → 用同一个 classifier 衡量 outcome。\n  \n  论文报告了 MNLI mismatched accuracy 90.0% 和 SNLI test 92.4%，但这是通用 NLI benchmark 上的表现。在 sycophancy-specific 的 stance flip 判断任务上，该 classifier 的准确率是多少？有没有在标注样本上验证过？\n\n- 建议：(1) 在 sycophancy-specific 样本上报告 NLI classifier 的准确率（例如手动标注 100 个样本做 gold standard）；(2) 讨论 training reward 和 evaluation metric 使用相同 classifier 的潜在循环性问题。\n\n**W3 [warning] 超参搜索不充分：w1 仅测试 0.25 和 0.40**\n\n- 具体位置：Table 2（Cosine R1 failure chain）；Appendix A\n- 问题：reward weight w1 仅测试了两个值（0.25 和 0.40），且采用 \"diagnostic-driven iteration\" 而非系统搜索。论文声称所有 cosine formulation 都失败，但仅从两个 weight 值的实验中无法排除存在有效配置的可能性。\n  \n  具体来说，F1b 的 cosine gap 仅 0.098——如果 w1 设置为更大的值（如 2.0 或 5.0），combined reward 中 R1 的比重增大，是否可能产生足够的 gradient signal？F1d 的 5× scaling 本质上就是在这个方向上的尝试，但同时将 w1 提高到了 0.40——这是两个变量同时变化。\n\n- 建议：(1) 明确说明 hyperparameter search 的范围和逻辑；(2) 至少在 w1 ∈ {0.1, 0.25, 0.40, 0.60, 1.0} 的范围内系统测试，或提供明确的理论论证解释为什么更大/更小的 w1 不会改变结论。\n\n**W4 [warning] Evidence strength 三级标注缺少 annotator agreement 信息**\n\n- 具体位置：§2.1（Direction Extraction）\n- 问题：181 对 contrastive pairs 的 evidence strength 被标注为 weak/medium/strong 三级。论文列出了各级别的标准和数量（75/54/52），但未报告：(1) 标注者是谁（作者自己？众包？）；(2) 标注者人数；(3) inter-annotator agreement（如 Cohen's κ 或 Fleiss' κ）。\n  \n  这些标注直接影响 §3 中报告的 evidence-strength stratified AUROC（weak 0.675→medium 0.883→strong 0.929），这是论文论证 d_syc \"captures evidential granularity\" 的核心证据。如果标注不可靠，该结论就不可靠。\n\n- 建议：报告 annotator 信息和 inter-annotator agreement。如果只有一个标注者，至少找第二个标注者在子集上验证。\n\n**W5 [warning] SyconScore 的 harmonic mean 设计缺乏理据对比**\n\n- 具体位置：§2.5 Equation 2\n- 问题：SyconScore 定义为 ToF 和 NoF 的 harmonic mean。论文的理由是 \"penalize methods that achieve high resistance by refusing all corrections (low ToF, high NoF) or by capitulating universally (high ToF, low NoF)\"。但：\n  - 为什么用 harmonic mean 而非 arithmetic mean 或 F-beta？Harmonic mean 对极端不平衡的惩罚力度远大于 arithmetic mean，这会系统性地放大 probe trap（ToF=0）的差距。\n  - 如果用 arithmetic mean，vanilla baseline 的 score 会从 0.134 变为 (0.072+0.945)/2 = 0.509，而 ACT 从 0.301 变为 (0.182+0.867)/2 = 0.525——差距大幅缩小。这意味着论文的核心定量对比在很大程度上依赖于 metric 的选择。\n  \n- 建议：(1) 同时报告 arithmetic mean 和 harmonic mean 结果；(2) 讨论 metric 选择对定量结论的敏感性。\n\n---\n\n## Questions for Authors\n\n**Q1.** §6 将 ACT 的成功归因于 supervision density，但 ACT 同时使用了 labeled valid/invalid pairs。如果给 GRPO 提供同样的 labeled pairs（例如用 expert demonstrations 构建 comparison group），GRPO 是否仍会失败？这个实验能帮助分离 supervision granularity 和 label availability 两个因素。\n\n**Q2.** §4 F1c 的 online recalibration 使 AUROC 从 0.827 提升至 0.910 但触发 mode collapse。是否测试过更温和的 recalibration 策略（如 exponential moving average of d_syc，或延长 recalibration 间隔至 1000/2000 steps）？\n\n**Q3.** 论文始终使用 GRPO 作为唯一的 RL 算法。PPO 的 clipping mechanism 和 value function 可能对 reward noise 更鲁棒——是否有理由排除 PPO？\n\n**Q4.** §5 中 probe reward trap 的发现（behavioral death 先于 distributional collapse）是否在 cosine formulations 中也观察到了？F1c/F1d 的 \"mode collapse\" 是先 behavioral 还是先 distributional？\n\n**Q5.** max_completion_length=256 导致 80-84% truncation。对于被截断的 responses，d_syc 是在最后一个生成的 token 的 representation 上计算的还是在被截断位置？截断是否影响 probe 和 cosine reward 的相对质量？\n\n---\n\n## Missing References\n\n- **Wei et al. (2024)** \"Simple synthetic data reduces LLM sycophancy\" 已引用，但未讨论他们的 synthetic data 方法是否也属于 \"dense supervision\" 的一种形式，这与本文的论点直接相关。\n- **Anthropic's Constitutional AI (Bai et al., 2022)** 使用 principle-based feedback 而非 scalar reward——作为一种不同粒度的 reward 设计，值得在 Related Work 中讨论。\n- **Token-level reward models**（如 process reward models for math reasoning, Lightman et al. 2024）——论文讨论了 supervision density，但未引用 process reward model 领域中关于 token-level vs outcome-level reward 的相关工作。已引用 SMART (Beigi et al., 2025)，但可以更充分地讨论。\n\n---\n\n## 小问题（不影响接收）\n\n- §2.1 \"19 of 200 initial pairs were discarded for failing validation\"——这是否会引入 selection bias？被丢弃的 19 对是否在 evidence strength 分布上有偏？\n- Table 4 的 footnote ‡ \"seed 2 verification ongoing (3 of 16 checkpoints evaluated)\" 使论文看起来是在实验未完成时提交的，这在审稿时会给人匆忙提交的印象。\n- §7 Related Work 引用了 \\citep{zhang2026latentgrpo} 和 \\citep{luo2026craft}，但这些工作在 sycophancy 之外的任务上成功使用了 representation-guided RL——论文可以更深入地分析为什么 sycophancy 与 reasoning/safety 不同（当前在 §6 第一段有提及但较简略）。\n- Figure 1 中 Llama-3-8B 只显示了 layers 16-31，但 caption 说 \"32 layers\"——完整显示所有层的 AUROC profile 更 informative。\n- Appendix B (Stubbornness Taxonomy) 基于手动检查 100 个 response（exp-008v3, step 2000），未报告 inter-annotator agreement，且仅分析一个 checkpoint。\n\n---\n\n## 主要优势\n\n- 选题精准——首次系统性否证 \"discriminability → reward utility\" 的隐含假设\n- 诊断链设计（F1a→F1b→F1c→F1d）逻辑严密，具有教学价值\n- Probe reward trap（behavioral death before distributional collapse）是对 RL 安全监控实践的重要发现\n- Cross-model direction validation 提升了 d_syc 分析的可信度\n- 论文写作清晰，论证结构好\n- Limitations 写作诚实透明\n\n---\n\n## 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心实验（d_syc 作为 reward 失败）论证充分，但 ACT vs GRPO 对比存在严重混淆变量（N1），单模型训练不足以支撑一般性 claim（N2），n=2 seeds 统计效力不足（N3）。三个 Must-Fix 问题中任何一个都显著削弱论文的因果推断能力。 |\n| Excitement | 3.5/5 | 问题选取好，probe reward trap 发现有实际意义，\"discriminability ≠ utility\" 的洞察对社区有价值。但贡献主要是 negative result + diagnostic analysis，未提供解决方案或 actionable 的 reward design 原则。 |\n| Reproducibility | 3/5 | 报告了 LoRA rank、optimizer、training steps 等基本信息，但 contrastive pair 生成的 GPT-4.1 prompt 未公开，evidence strength 标注过程不透明，ACT seed 2 结果不完整。 |\n| Confidence | 4/5 | 我仔细阅读了论文全文和附录，熟悉 representation engineering、GRPO、sycophancy mitigation 领域的相关工作。对方法论和实验设计的评估有较高信心。 |\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 — Findings**\n\n**一句话总结**: 论文提出了一个重要且有洞察力的 negative result（d_syc discriminability 不等于 reward utility），诊断分析设计精良，但核心因果推断（supervision density hypothesis）受到多重混淆变量的严重削弱，单模型实验不足以支撑标题和正文的一般性声称，且统计效力不足。\n\n**详细论证**: 本文的两层贡献——(1) d_syc-based reward 失败 和 (2) sparse RL reward 结构性不足——在证据强度上有显著差异。第一层（C1, C2）有较强的实验支持：六种 GRPO 配置一致失败，failure modes 的诊断链设计优秀，probe reward trap 的发现有独立价值。但第二层（C3，supervision density hypothesis）是论文试图从 diagnostic paper 升级为 explanatory paper 的关键，而这恰恰是证据最薄弱的环节——ACT vs GRPO 的对比存在至少 4 个混淆变量。\n\n如果论文将自己定位为 \"d_syc as RL reward fails, here is why and how it fails\"（专注 C1+C2），去掉或显著软化 C3 的因果声称，这将是一篇扎实的 Findings 论文。当前的定位试图做一般性因果推断（C3），证据不足以支撑。\n\n修改建议优先级：N1（混淆变量）> N2（单模型 generality）> N3（统计效力）。解决 N1 可能需要额外实验（如 token-level RL 消融），但即使不加实验，恰当软化措辞也能显著改善。\n",
  "reviewer_id": "1",
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 审稿报告：方法严谨性审查\n\n**论文标题**: Discriminability Without Utility: Why Sycophancy Directions Fail as Scalar RL Rewards\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审查侧重**: 方法严谨性\n\n---\n\n## Paper Summary\n\n本文研究对比提取的 sycophancy direction (d_syc) 能否作为 GRPO 的标量 reward 信号来校准 LLM 的 sycophancy 行为。作者在 Qwen3-8B 上提取 d_syc（5-fold CV AUROC 0.827），测试三种 reward 公式（cosine projection、binary probe、continuous probe）共六种配置，结果全部失败。论文进一步展示 R3-only GRPO（仅用 NLI 行为 reward）也失败（26 个 checkpoint 仅 4 个超过 vanilla），而 ACT（dense per-token SFT）以 SyconScore 0.301 成功。核心论点是 d_syc 编码了\"是否发生信念变化\"而非\"信念变化是否有证据支撑\"，且标量 per-completion reward 结构性地无法传达 valid/invalid 区分。\n\n---\n\n## Summary of Strengths\n\n**S1. 问题选取极佳，填补重要空白。** representation engineering 的线性方向能否直接转化为 RL reward？这是社区普遍假设但未被系统检验的前提。本文是首个在 sycophancy 校准上系统否证该前提的工作，具有重要理论意义。\n\n**S2. 诊断链设计严谨且有教学价值。** §4 的 cosine failure chain（F1a→F1b→F1c→F1d）是一个精心设计的渐进式消融，每一步解决前一步的 failure mode 但暴露更深层问题。这种叙事结构使论文的论证逻辑非常清晰。\n\n**S3. Probe reward trap 的发现有实际安全意义。** behavioral death（ToF=0 at step 500）先于 distributional collapse（entropy collapse at step ~1840）的 1300-step 时间差，且 reward 始终保持 +0.72——这意味着标准的 entropy-based early stopping 会完全错过行为退化。这对 RLHF 安全监控实践有直接启示。\n\n**S4. Limitations 写作诚实。** 论文在 Limitations 中主动承认了多项关键局限（单模型训练、ACT seed 2 不完整、n=2 seeds 的统计效力、supervision granularity confound）。这种透明性值得肯定。\n\n**S5. Cross-model direction validation 增强了 d_syc 分析的可信度。** 在 Llama-3-8B 上独立复现了 direction extraction，evidence-strength gradient 的定性模式一致，表明 d_syc 的几何性质不是模型特异的。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1 [critical] ACT vs GRPO 对比存在多重混淆变量，\"supervision density hypothesis\" 过度声称**\n\n- 具体位置：§6 \"The supervision density hypothesis\" 段落；Introduction C3；Conclusion\n- 问题：论文将 ACT 的成功归因于 \"supervision density\"（per-token vs per-completion），但 ACT 和 GRPO 至少在以下维度同时不同：\n  - (a) per-token vs per-completion 梯度粒度\n  - (b) SFT（交叉熵）vs RL（REINFORCE/GRPO）目标函数\n  - (c) ACT 使用 labeled valid/invalid pairs（有标签监督），GRPO 使用 sampled completions（无标签）\n  - (d) ACT 额外包含 L2 activation consistency loss\n  \n  当至少有 4 个同时变化的因素时，将因果归因到 \"supervision density\" 这一个维度上是不合理的。ACT 的成功可能主要因为它使用了 **labeled examples**（直接告诉模型哪些 belief change 是 warranted 的），而不是因为 per-token supervision。论文在 Limitations 中承认了这一 confound，但正文（尤其 Introduction C3 和 Conclusion）的措辞远比 Limitations 中的 hedge 更强。\n  \n  §6 最后一句\"we expect similar failure patterns wherever representation-derived signals are compressed to completion-level scalars\"——这是从单一模型、单一 RL 算法的实验外推到整个 per-completion RL 方法类别的推测性声称。\n\n- 为什么影响接收：C3 是论文三个 contribution 之一。如果 ACT 的优势来自 labeled supervision 而非 supervision density，论文的核心叙事（discriminability ≠ utility, 且 sparse reward 结构性不足）的第二层（sparse reward 不足）就不成立。\n  \n- 建议修改方向：\n  - 明确列出 ACT 与 GRPO 的所有差异维度，并在正文（不只是 Limitations）中讨论替代解释\n  - 将 \"supervision density hypothesis\" 降级为多个可能解释之一，而非论文的核心 contribution\n  - 增加消融实验以隔离因素：例如 (1) per-token RL（如 token-level GRPO/PPO）vs per-completion GRPO，(2) 使用 labeled pairs 的 GRPO（而非 sampled completions）\n  - 或者将 C3 重新表述为观察性发现而非因果声称\n\n**N2 [critical] 实验仅在 Qwen3-8B 上训练，不足以支撑论文的一般性声称**\n\n- 具体位置：Title（\"Why Sycophancy Directions Fail as Scalar RL Rewards\"——一般性陈述）；Introduction（\"scalar per-completion RL is structurally insufficient for sycophancy calibration\"）；§6（\"the scalar per-completion reward structure is shared by PPO, RLOO, and other REINFORCE-style methods\"）\n- 问题：所有 RL 和 SFT 训练实验仅在 Qwen3-8B 一个模型上进行。Llama-3-8B 仅用于 direction extraction 验证，未进行任何训练实验。论文标题和正文使用一般性措辞（\"sycophancy directions fail\"、\"structurally insufficient\"），但仅有单模型证据。\n  \n  更重要的是，GRPO 的 failure modes 可能与 Qwen3-8B 的特定特性有关（如 residual stream 的几何结构、RL 训练动态），在其他模型上可能表现不同。论文自身展示了两个模型的 d_syc 最佳层不同（L19 vs L16）、AUROC 不同（0.827 vs 0.779），这暗示模型间的差异可能影响训练动态。\n\n- 为什么影响接收：标题和核心 claim 的一般性远超实验证据的范围。ARR 指南明确要求 \"claims match the evaluation scope\"（R2）。\n  \n- 建议修改方向：\n  - 在标题或 abstract 中明确限定实验范围（\"on Qwen3-8B\" 或 \"a case study\"）\n  - 在 Llama-3-8B 上至少复现一个关键实验（如 binary probe F2）以测试跨模型一致性\n  - 或将一般性声称显著软化：从 \"fail\" → \"failed in our experiments\"；从 \"structurally insufficient\" → \"insufficient in the tested configuration\"\n\n**N3 [critical] 统计效力严重不足：n=2 seeds、ACT seed 2 仅 3/16 checkpoints**\n\n- 具体位置：Table 4（主对比表）；§6（cross-seed analysis）；Limitations\n- 问题：\n  - GRPO 使用 n=2 seeds。论文报告了 cross-seed rank correlation 在 step 4000 后降至 ρ≈0.33 (n.s.)，但 n=2 的相关性几乎没有任何统计意义——任何两条随机曲线都可能在某些区间有高相关。\n  - ACT seed 2 仅完成 3/16 checkpoints。Table 4 将 ACT seed 1 的完整结果（16/16 checkpoints 全部超过 vanilla）作为核心证据，但仅有 1 个完整 seed。3/16 的部分数据被标注为 \"ongoing\"，这意味着论文在实验未完成时就提交了。\n  - \"4/26 checkpoints (15.4%) exceed vanilla\" vs \"16/16 (100%)\" 的对比在统计上并不如看起来那么有力：不同方法在不同 training stages 有不同 dynamics，逐 checkpoint 比较忽略了时间序列的自相关性。\n\n- 为什么影响接收：ARR 指南要求 \"appropriate information about statistical significance\"（R5）。n=2 seeds 的 cross-seed 分析、incomplete seed 2 数据、以及缺乏置信区间或显著性检验的主对比，都低于会议论文的标准。\n\n- 建议修改方向：\n  - 至少增加到 n=3 seeds（GRPO 和 ACT 各 3 seeds），报告 mean±std\n  - 完成 ACT seed 2 的全部 16 checkpoints 评估\n  - 对 Table 4 的关键对比（如 GRPO best vs ACT best）报告置信区间或 bootstrap test\n  - 如果计算资源不足以增加 seeds，应在正文中大幅软化比较性声称\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1 [warning] max_completion_length=256 导致 80-84% truncation，可能系统性偏倚结果**\n\n- 具体位置：Appendix A（Response truncation）\n- 问题：所有 GRPO 实验使用 max_completion_length=256，导致 80-84% 的 multi-turn responses 被截断。论文声称 \"this setting is shared across all conditions and does not affect relative comparisons\"，以及 \"response-level decisions typically manifest within the first 100-200 tokens\"。\n  \n  但这两个辩护都有问题。首先，截断对不同 reward formulation 的影响可能不同：binary probe 只需看 final representation（受截断影响小），而 cosine reward 依赖于 activation 的连续变化（可能更受截断影响）。其次，\"decisions manifest within 100-200 tokens\" 是一个未验证的断言。一个正在进行 nuanced belief revision 的模型可能需要更多 token 来表达，而简单拒绝修改只需很少 token——截断可能系统性地惩罚 warranted revision。\n\n- 建议：(1) 在至少一个配置上测试 max_completion_length=512 或更高，验证截断不影响 failure modes 的定性结论；(2) 提供截断对 ToF vs NoF responses 的差异化影响分析。\n\n**W2 [warning] NLI 分类器同时用于 R3 reward 和 ToF/NoF 评估，存在评估循环性**\n\n- 具体位置：§2.5（Evaluation）——使用 DeBERTa NLI 做 stance classification；§2.2——R3 也是 DeBERTa NLI classifier\n- 问题：R3 reward component 使用 DeBERTa NLI 判断模型回答与 ground truth 的一致性；ToF/NoF 评估也使用同一个 DeBERTa NLI classifier（cross-encoder/nli-deberta-v3-base）判断 stance flip。这创造了一个评估循环：训练用 NLI classifier 给 reward → 用同一个 classifier 衡量 outcome。\n  \n  论文报告了 MNLI mismatched accuracy 90.0% 和 SNLI test 92.4%，但这是通用 NLI benchmark 上的表现。在 sycophancy-specific 的 stance flip 判断任务上，该 classifier 的准确率是多少？有没有在标注样本上验证过？\n\n- 建议：(1) 在 sycophancy-specific 样本上报告 NLI classifier 的准确率（例如手动标注 100 个样本做 gold standard）；(2) 讨论 training reward 和 evaluation metric 使用相同 classifier 的潜在循环性问题。\n\n**W3 [warning] 超参搜索不充分：w1 仅测试 0.25 和 0.40**\n\n- 具体位置：Table 2（Cosine R1 failure chain）；Appendix A\n- 问题：reward weight w1 仅测试了两个值（0.25 和 0.40），且采用 \"diagnostic-driven iteration\" 而非系统搜索。论文声称所有 cosine formulation 都失败，但仅从两个 weight 值的实验中无法排除存在有效配置的可能性。\n  \n  具体来说，F1b 的 cosine gap 仅 0.098——如果 w1 设置为更大的值（如 2.0 或 5.0），combined reward 中 R1 的比重增大，是否可能产生足够的 gradient signal？F1d 的 5× scaling 本质上就是在这个方向上的尝试，但同时将 w1 提高到了 0.40——这是两个变量同时变化。\n\n- 建议：(1) 明确说明 hyperparameter search 的范围和逻辑；(2) 至少在 w1 ∈ {0.1, 0.25, 0.40, 0.60, 1.0} 的范围内系统测试，或提供明确的理论论证解释为什么更大/更小的 w1 不会改变结论。\n\n**W4 [warning] Evidence strength 三级标注缺少 annotator agreement 信息**\n\n- 具体位置：§2.1（Direction Extraction）\n- 问题：181 对 contrastive pairs 的 evidence strength 被标注为 weak/medium/strong 三级。论文列出了各级别的标准和数量（75/54/52），但未报告：(1) 标注者是谁（作者自己？众包？）；(2) 标注者人数；(3) inter-annotator agreement（如 Cohen's κ 或 Fleiss' κ）。\n  \n  这些标注直接影响 §3 中报告的 evidence-strength stratified AUROC（weak 0.675→medium 0.883→strong 0.929），这是论文论证 d_syc \"captures evidential granularity\" 的核心证据。如果标注不可靠，该结论就不可靠。\n\n- 建议：报告 annotator 信息和 inter-annotator agreement。如果只有一个标注者，至少找第二个标注者在子集上验证。\n\n**W5 [warning] SyconScore 的 harmonic mean 设计缺乏理据对比**\n\n- 具体位置：§2.5 Equation 2\n- 问题：SyconScore 定义为 ToF 和 NoF 的 harmonic mean。论文的理由是 \"penalize methods that achieve high resistance by refusing all corrections (low ToF, high NoF) or by capitulating universally (high ToF, low NoF)\"。但：\n  - 为什么用 harmonic mean 而非 arithmetic mean 或 F-beta？Harmonic mean 对极端不平衡的惩罚力度远大于 arithmetic mean，这会系统性地放大 probe trap（ToF=0）的差距。\n  - 如果用 arithmetic mean，vanilla baseline 的 score 会从 0.134 变为 (0.072+0.945)/2 = 0.509，而 ACT 从 0.301 变为 (0.182+0.867)/2 = 0.525——差距大幅缩小。这意味着论文的核心定量对比在很大程度上依赖于 metric 的选择。\n  \n- 建议：(1) 同时报告 arithmetic mean 和 harmonic mean 结果；(2) 讨论 metric 选择对定量结论的敏感性。\n\n---\n\n## Questions for Authors\n\n**Q1.** §6 将 ACT 的成功归因于 supervision density，但 ACT 同时使用了 labeled valid/invalid pairs。如果给 GRPO 提供同样的 labeled pairs（例如用 expert demonstrations 构建 comparison group），GRPO 是否仍会失败？这个实验能帮助分离 supervision granularity 和 label availability 两个因素。\n\n**Q2.** §4 F1c 的 online recalibration 使 AUROC 从 0.827 提升至 0.910 但触发 mode collapse。是否测试过更温和的 recalibration 策略（如 exponential moving average of d_syc，或延长 recalibration 间隔至 1000/2000 steps）？\n\n**Q3.** 论文始终使用 GRPO 作为唯一的 RL 算法。PPO 的 clipping mechanism 和 value function 可能对 reward noise 更鲁棒——是否有理由排除 PPO？\n\n**Q4.** §5 中 probe reward trap 的发现（behavioral death 先于 distributional collapse）是否在 cosine formulations 中也观察到了？F1c/F1d 的 \"mode collapse\" 是先 behavioral 还是先 distributional？\n\n**Q5.** max_completion_length=256 导致 80-84% truncation。对于被截断的 responses，d_syc 是在最后一个生成的 token 的 representation 上计算的还是在被截断位置？截断是否影响 probe 和 cosine reward 的相对质量？\n\n---\n\n## Missing References\n\n- **Wei et al. (2024)** \"Simple synthetic data reduces LLM sycophancy\" 已引用，但未讨论他们的 synthetic data 方法是否也属于 \"dense supervision\" 的一种形式，这与本文的论点直接相关。\n- **Anthropic's Constitutional AI (Bai et al., 2022)** 使用 principle-based feedback 而非 scalar reward——作为一种不同粒度的 reward 设计，值得在 Related Work 中讨论。\n- **Token-level reward models**（如 process reward models for math reasoning, Lightman et al. 2024）——论文讨论了 supervision density，但未引用 process reward model 领域中关于 token-level vs outcome-level reward 的相关工作。已引用 SMART (Beigi et al., 2025)，但可以更充分地讨论。\n\n---\n\n## 小问题（不影响接收）\n\n- §2.1 \"19 of 200 initial pairs were discarded for failing validation\"——这是否会引入 selection bias？被丢弃的 19 对是否在 evidence strength 分布上有偏？\n- Table 4 的 footnote ‡ \"seed 2 verification ongoing (3 of 16 checkpoints evaluated)\" 使论文看起来是在实验未完成时提交的，这在审稿时会给人匆忙提交的印象。\n- §7 Related Work 引用了 \\citep{zhang2026latentgrpo} 和 \\citep{luo2026craft}，但这些工作在 sycophancy 之外的任务上成功使用了 representation-guided RL——论文可以更深入地分析为什么 sycophancy 与 reasoning/safety 不同（当前在 §6 第一段有提及但较简略）。\n- Figure 1 中 Llama-3-8B 只显示了 layers 16-31，但 caption 说 \"32 layers\"——完整显示所有层的 AUROC profile 更 informative。\n- Appendix B (Stubbornness Taxonomy) 基于手动检查 100 个 response（exp-008v3, step 2000），未报告 inter-annotator agreement，且仅分析一个 checkpoint。\n\n---\n\n## 主要优势\n\n- 选题精准——首次系统性否证 \"discriminability → reward utility\" 的隐含假设\n- 诊断链设计（F1a→F1b→F1c→F1d）逻辑严密，具有教学价值\n- Probe reward trap（behavioral death before distributional collapse）是对 RL 安全监控实践的重要发现\n- Cross-model direction validation 提升了 d_syc 分析的可信度\n- 论文写作清晰，论证结构好\n- Limitations 写作诚实透明\n\n---\n\n## 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心实验（d_syc 作为 reward 失败）论证充分，但 ACT vs GRPO 对比存在严重混淆变量（N1），单模型训练不足以支撑一般性 claim（N2），n=2 seeds 统计效力不足（N3）。三个 Must-Fix 问题中任何一个都显著削弱论文的因果推断能力。 |\n| Excitement | 3.5/5 | 问题选取好，probe reward trap 发现有实际意义，\"discriminability ≠ utility\" 的洞察对社区有价值。但贡献主要是 negative result + diagnostic analysis，未提供解决方案或 actionable 的 reward design 原则。 |\n| Reproducibility | 3/5 | 报告了 LoRA rank、optimizer、training steps 等基本信息，但 contrastive pair 生成的 GPT-4.1 prompt 未公开，evidence strength 标注过程不透明，ACT seed 2 结果不完整。 |\n| Confidence | 4/5 | 我仔细阅读了论文全文和附录，熟悉 representation engineering、GRPO、sycophancy mitigation 领域的相关工作。对方法论和实验设计的评估有较高信心。 |\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 — Findings**\n\n**一句话总结**: 论文提出了一个重要且有洞察力的 negative result（d_syc discriminability 不等于 reward utility），诊断分析设计精良，但核心因果推断（supervision density hypothesis）受到多重混淆变量的严重削弱，单模型实验不足以支撑标题和正文的一般性声称，且统计效力不足。\n\n**详细论证**: 本文的两层贡献——(1) d_syc-based reward 失败 和 (2) sparse RL reward 结构性不足——在证据强度上有显著差异。第一层（C1, C2）有较强的实验支持：六种 GRPO 配置一致失败，failure modes 的诊断链设计优秀，probe reward trap 的发现有独立价值。但第二层（C3，supervision density hypothesis）是论文试图从 diagnostic paper 升级为 explanatory paper 的关键，而这恰恰是证据最薄弱的环节——ACT vs GRPO 的对比存在至少 4 个混淆变量。\n\n如果论文将自己定位为 \"d_syc as RL reward fails, here is why and how it fails\"（专注 C1+C2），去掉或显著软化 C3 的因果声称，这将是一篇扎实的 Findings 论文。当前的定位试图做一般性因果推断（C3），证据不足以支撑。\n\n修改建议优先级：N1（混淆变量）> N2（单模型 generality）> N3（统计效力）。解决 N1 可能需要额外实验（如 token-level RL 消融），但即使不加实验，恰当软化措辞也能显著改善。\n",
    "reviewer_id": "1",
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 111 · 2026-05-22T11:34:32.571652+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4070
}
```

</details>

---


### Tool call

_source line 112 · 2026-05-22T11:34:38.157483+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
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

_source line 113 · 2026-05-22T11:34:38.157868+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 114 · 2026-05-22T11:34:41.872227+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 115 · 2026-05-22T11:34:41.872621+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 116 · 2026-05-22T11:34:50.228595+00:00_

审稿报告已提交给 Review Director。

**核心评判：Overall 3.0（Findings 级别）**

三个 Must-Fix 问题：
1. **ACT vs GRPO 存在多重混淆变量**——supervision density hypothesis 的因果归因不成立，ACT 与 GRPO 在至少 4 个维度同时不同（梯度粒度、目标函数、标签可用性、L2 consistency loss）
2. **仅 Qwen3-8B 训练，标题和正文做一般性声称**——claim scope 远超 evaluation scope
3. **n=2 seeds、ACT seed 2 仅 3/16 checkpoints**——统计效力严重不足

论文的 C1（d_syc reward 失败）和 C2（probe reward trap）有较强证据支持，诊断链设计优秀。但 C3（supervision density hypothesis）是证据最薄弱的环节，恰恰是论文试图从 diagnostic paper 升级为 explanatory paper 的关键。建议将 C3 的因果声称显著软化，或补充消融实验（如 token-level RL）来隔离混淆因素。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1"
}
```

</details>

---


## Round 4

## Round 4

4 recorded events


### User

_source line 117 · 2026-05-22T11:36:22.631564+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2（新颖性与完整性）的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，用 **[AGREE]** 表示同意并说明理由，或用 **[REBUT]** 表示反驳并提供证据（cite 具体 Section/Table/Figure）。

---

# Reviewer 2 完整审稿报告

## Overall: 3.5 (Borderline Conference)

## Must-Fix 问题

**N1 [critical] C3 "sparse RL reward cannot convey the valid/invalid distinction" 声明过度泛化**
- 证据仅来自三种 d_syc-based reward 和一种 NLI-based behavioral reward (R3-only GRPO)
- 未测试其他标量奖励设计（ensemble reward model、multi-signal composite reward、专门训练的 sycophancy reward model）
- 也未测试其他 RL 算法（PPO、RLOO、DPO online variant）
- §6 从单一算法 (GRPO) 上的 4 种奖励变体推广到整个 RL 算法族
- 作为 negative result 论文，结论的精确边界至关重要，过度泛化会误导社区

**N2 [critical] ACT vs. GRPO 对比存在未充分隔离的混淆变量**
- 至少三个同时变化的因素：(1) supervision granularity, (2) 优化范式 (SFT vs. RL), (3) 训练信号性质 (labeled pairs vs. online exploration)
- Limitations 承认了 confound 但正文的因果解释过强
- 如果 SFT 成功主要因为它有 ground-truth labels 而非 per-token granularity，supervision density hypothesis 就不成立

## Should-Fix 问题

**W1** SMART (Beigi et al., 2025) 讨论不充分——作为 per-step process reward 的中间方案，supervision density hypothesis 直接预测 SMART 应部分成功，但论文仅一句话提及。

**W2** CRAFT (Luo et al., 2026) 对比讨论缺失——CRAFT 在 safety/reasoning 上成功使用 latent-aware reward，与本文 negative result 形成重要对比机会。

**W3** 遗漏高度相关新工作 "When Reward Hacking Rebounds" (arXiv:2604.01476, April 2026)——在 GRPO 中成功使用 representation-level concept directions。

**W4** "Latent-GRPO" 命名可能误导读者——Zhang et al. (2026) 原标题是 "Silence the Judge"，"Latent-GRPO" 不是原文名称。

**W5** 可复现性信息不足——GRPO 关键超参数未披露（采样数、KL penalty、learning rate、batch size）；GPT-4.1 prompt 未提供；无代码/数据可用性声明。

## 小问题
- Abstract 过长（近一整栏），建议压缩
- Introduction 与后续章节数字冗余
- Table 4 Cosine R1 显示 "collapse" 而非数值
- Self-Augmented Preference Alignment (Chen et al., EMNLP 2025) 未引用
- d_syc 提取方法仅用 mean difference，未验证 PCA/CCS-style 替代方案

## Missing References
1. "When Reward Hacking Rebounds" (arXiv:2604.01476, April 2026) — 必须引用
2. Chen, Huang & Chen (2025) "Self-Augmented Preference Alignment" (EMNLP 2025) — 建议引用
3. "Latent-GRPO" 命名需确认来源

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 118 · 2026-05-22T11:37:29.642960+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n**[AGREE] R2-N1: C3 \"sparse RL reward cannot convey the valid/invalid distinction\" 声明过度泛化**\n\n同意，且与我的 N1 判断一致。我在审稿中同样指出 §6 最后一句 \"we expect similar failure patterns wherever representation-derived signals are compressed to completion-level scalars\" 是从单一模型、单一 RL 算法外推到整个方法类别的推测性声称。R2 进一步补充了我未充分展开的要点：论文也未测试 ensemble reward model、专门训练的 sycophancy reward model 等替代标量奖励设计。\n\n补充一点：论文测试的 4 种 reward 变体（F1a-F1d cosine、F2 binary probe、F3 continuous probe、R3-only）虽然看似丰富，但它们共享一个前提——reward signal 直接来自 d_syc 或单一 NLI classifier 的 raw output，未经过任何 reward model 训练。一个在 sycophancy 标注数据上训练过的 reward model（即使输出标量）可能学到 d_syc 无法编码的 evidential warrant 信息。论文标题中的 \"Scalar RL Rewards\" 暗示了对所有标量 reward 的否定，但实际只测试了 representation-derived 和 classifier-based 的 raw signal。\n\n**[AGREE] R2-N2: ACT vs. GRPO 对比存在未充分隔离的混淆变量**\n\n完全同意，这与我的 N1 重合。R2 的表述更精炼，将混淆变量归纳为三个维度（supervision granularity、优化范式、训练信号性质）。我的审稿中额外列出了第四个维度：ACT 包含 L2 activation consistency loss（§2.4），这是一个额外的正则化信号。\n\nR2 提出的核心反事实——\"如果 SFT 成功主要因为 ground-truth labels 而非 per-token granularity\"——是正确的关键质疑。论文 §6 的 \"supervision density hypothesis\" 段落（discussion.tex L68-74）将 ACT 的成功归因于 \"a corrective gradient at every token position\"，但完全忽略了 ACT 使用 labeled valid/invalid pairs 这一更基本的优势。一个使用 labeled pairs 的 per-completion reward（例如对每个 completion 打一个基于 ground truth 的 binary reward）可能也能成功——这会直接反驳 supervision density hypothesis。\n\n---\n\n## Should-Fix 问题\n\n**[AGREE] R2-W1: SMART (Beigi et al., 2025) 讨论不充分**\n\n同意。论文在 related_work.tex L21 仅用一句话提及 SMART：\"SMART applies per-step process rewards with MCTS for sycophancy, representing intermediate supervision density between scalar per-completion rewards and dense per-token approaches.\" 但未将其与 supervision density hypothesis 做 explicit 对比。如果 supervision density 是关键变量，SMART 的 per-step process reward 应处于 GRPO（per-completion）和 ACT（per-token）之间，论文的理论框架直接预测 SMART 应表现介于两者之间。未讨论 SMART 的实际结果是否支持这一预测，是一个理论完整性缺陷。\n\n**[REBUT] R2-W2: CRAFT (Luo et al., 2026) 对比讨论缺失**\n\n部分不同意。论文在 related_work.tex L19-20 已提及 CRAFT：\"CRAFT applies representation-level constraints during RL\"，并在同一段落的总结句（L22）给出了统一解释：\"These methods succeed because target and suppressed behaviors are geometrically distinct; sycophancy breaks this condition (§4).\" 这实际上已经提供了 CRAFT 与本文 negative result 的对比框架——CRAFT 成功是因为 safety/reasoning 的 target 和 suppressed behavior 几何可分，而 sycophancy 不满足这一前提。\n\n不过我同意这个对比可以更深入——例如量化 CRAFT 的 representation gap 与本文 0.098 cosine gap 的差异——但说 \"对比讨论缺失\" 不准确，应为 \"对比讨论不够深入\"。\n\n**[REBUT] R2-W3: 遗漏 \"When Reward Hacking Rebounds\" (arXiv:2604.01476)**\n\n作为 reviewer 我无法验证这篇论文是否真实存在（arXiv ID 2604.01476 的格式对应 2026 年 4 月），也无法确认其内容是否与 R2 的描述一致。在审稿中要求引用一篇特定的 arXiv preprint 需要基于确认该工作确实存在且高度相关。如果 R2 能确认该论文确实 \"在 GRPO 中成功使用 representation-level concept directions\"，那么它确实与本文的 negative result 形成重要对比，应该引用。但我建议 Director 先验证该引用的真实性后再作为 Must-cite 要求。\n\n**[AGREE] R2-W4: \"Latent-GRPO\" 命名可能误导**\n\n同意，如果 Zhang et al. (2026) 原标题是 \"Silence the Judge\" 且原文未使用 \"Latent-GRPO\" 这一名称，论文应使用原文名称或在首次出现时标注 \"which we refer to as Latent-GRPO for brevity\"。学术论文应尊重原作的命名。不过这是一个 minor naming issue，不影响技术判断。\n\n**[AGREE] R2-W5: 可复现性信息不足**\n\n同意，且与我的 reproducibility 评分（3/5）一致。我在审稿中同样指出 GPT-4.1 prompt 未公开和 evidence strength 标注过程不透明。R2 额外指出 GRPO 的关键超参数（采样数、KL penalty、learning rate、batch size）未披露——这确实是一个重要遗漏。Appendix A 仅报告了 reward weight selection 和 response truncation，但缺少 GRPO 训练本身的超参数表。对于一篇 negative result 论文，可复现性尤其重要——读者需要确信 failure 不是由于超参数选择不当。\n\n---\n\n## 小问题\n\n**[AGREE] Abstract 过长**：确认 Abstract 在 PDF 中接近占据一整栏，对于 8 页 long paper 来说偏长。建议压缩到 150-200 词。\n\n**[AGREE] Introduction 与后续章节数字冗余**：Introduction（introduction.tex）中大量引用了具体数字（AUROC 0.827、σ=0.028、0.779、15.4% 等），这些在后续章节中全部重复出现。Introduction 应侧重 high-level narrative，具体数字留给正文。\n\n**[AGREE] Table 4 Cosine R1 显示 \"collapse\" 而非数值**：同意这损害了可比较性。即使是 collapse 状态，也应报告最后一个稳定 checkpoint 的 ToF/NoF/SyconScore 数值。\n\n**[REBUT] d_syc 提取仅用 mean difference，未验证 PCA/CCS-style 替代方案**：这个批评有道理但权重过高。论文的核心论点是 discriminability ≠ utility，而非寻找最优 direction extraction 方法。mean difference 已经给出 AUROC 0.827，PCA/CCS 即使给出更高 AUROC 也不太可能改变核心结论——因为论文已经展示了 recalibration 将 AUROC 提升至 0.910 后仍然 fail（§4 F1c）。更高的 discriminability 并不能解决 valid revision 与 sycophantic capitulation 在 d_syc 方向上 geometrically overlapping 的根本问题。\n\n---\n\n## Missing References\n\n**[REBUT] arXiv:2604.01476**：如上述 W3 所述，需先验证真实性。\n\n**[AGREE] Chen, Huang & Chen (2025) \"Self-Augmented Preference Alignment\"**：如果该工作确实发表于 EMNLP 2025 并涉及 preference alignment 与 sycophancy，应在 Related Work 中引用。\n\n**[AGREE] \"Latent-GRPO\" 命名来源需确认**：同意 R2-W4，应确认并使用原文命名。\n\n---\n\n## 综合评价\n\nR2 给出 3.5（Borderline Conference），我给出 3.0（Findings）。核心分歧不大——我们在 N1/N2（C3 过度声称、ACT vs GRPO confound）上完全一致。我的评分更低主要因为我额外重视了 N3（统计效力：n=2 seeds、ACT seed 2 不完整）和 N2（单模型 generality），这两个问题 R2 未单独列为 Must-Fix 但我认为它们同样影响接收决定。\n\n如果作者能解决 N1/N2（软化 C3 的因果声称、明确列出混淆变量）并增强统计证据（完成 ACT seed 2、增加至少 1 个 seed），我认为 3.5 是合理的目标评分。\n",
  "reviewer_id": "1",
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n**[AGREE] R2-N1: C3 \"sparse RL reward cannot convey the valid/invalid distinction\" 声明过度泛化**\n\n同意，且与我的 N1 判断一致。我在审稿中同样指出 §6 最后一句 \"we expect similar failure patterns wherever representation-derived signals are compressed to completion-level scalars\" 是从单一模型、单一 RL 算法外推到整个方法类别的推测性声称。R2 进一步补充了我未充分展开的要点：论文也未测试 ensemble reward model、专门训练的 sycophancy reward model 等替代标量奖励设计。\n\n补充一点：论文测试的 4 种 reward 变体（F1a-F1d cosine、F2 binary probe、F3 continuous probe、R3-only）虽然看似丰富，但它们共享一个前提——reward signal 直接来自 d_syc 或单一 NLI classifier 的 raw output，未经过任何 reward model 训练。一个在 sycophancy 标注数据上训练过的 reward model（即使输出标量）可能学到 d_syc 无法编码的 evidential warrant 信息。论文标题中的 \"Scalar RL Rewards\" 暗示了对所有标量 reward 的否定，但实际只测试了 representation-derived 和 classifier-based 的 raw signal。\n\n**[AGREE] R2-N2: ACT vs. GRPO 对比存在未充分隔离的混淆变量**\n\n完全同意，这与我的 N1 重合。R2 的表述更精炼，将混淆变量归纳为三个维度（supervision granularity、优化范式、训练信号性质）。我的审稿中额外列出了第四个维度：ACT 包含 L2 activation consistency loss（§2.4），这是一个额外的正则化信号。\n\nR2 提出的核心反事实——\"如果 SFT 成功主要因为 ground-truth labels 而非 per-token granularity\"——是正确的关键质疑。论文 §6 的 \"supervision density hypothesis\" 段落（discussion.tex L68-74）将 ACT 的成功归因于 \"a corrective gradient at every token position\"，但完全忽略了 ACT 使用 labeled valid/invalid pairs 这一更基本的优势。一个使用 labeled pairs 的 per-completion reward（例如对每个 completion 打一个基于 ground truth 的 binary reward）可能也能成功——这会直接反驳 supervision density hypothesis。\n\n---\n\n## Should-Fix 问题\n\n**[AGREE] R2-W1: SMART (Beigi et al., 2025) 讨论不充分**\n\n同意。论文在 related_work.tex L21 仅用一句话提及 SMART：\"SMART applies per-step process rewards with MCTS for sycophancy, representing intermediate supervision density between scalar per-completion rewards and dense per-token approaches.\" 但未将其与 supervision density hypothesis 做 explicit 对比。如果 supervision density 是关键变量，SMART 的 per-step process reward 应处于 GRPO（per-completion）和 ACT（per-token）之间，论文的理论框架直接预测 SMART 应表现介于两者之间。未讨论 SMART 的实际结果是否支持这一预测，是一个理论完整性缺陷。\n\n**[REBUT] R2-W2: CRAFT (Luo et al., 2026) 对比讨论缺失**\n\n部分不同意。论文在 related_work.tex L19-20 已提及 CRAFT：\"CRAFT applies representation-level constraints during RL\"，并在同一段落的总结句（L22）给出了统一解释：\"These methods succeed because target and suppressed behaviors are geometrically distinct; sycophancy breaks this condition (§4).\" 这实际上已经提供了 CRAFT 与本文 negative result 的对比框架——CRAFT 成功是因为 safety/reasoning 的 target 和 suppressed behavior 几何可分，而 sycophancy 不满足这一前提。\n\n不过我同意这个对比可以更深入——例如量化 CRAFT 的 representation gap 与本文 0.098 cosine gap 的差异——但说 \"对比讨论缺失\" 不准确，应为 \"对比讨论不够深入\"。\n\n**[REBUT] R2-W3: 遗漏 \"When Reward Hacking Rebounds\" (arXiv:2604.01476)**\n\n作为 reviewer 我无法验证这篇论文是否真实存在（arXiv ID 2604.01476 的格式对应 2026 年 4 月），也无法确认其内容是否与 R2 的描述一致。在审稿中要求引用一篇特定的 arXiv preprint 需要基于确认该工作确实存在且高度相关。如果 R2 能确认该论文确实 \"在 GRPO 中成功使用 representation-level concept directions\"，那么它确实与本文的 negative result 形成重要对比，应该引用。但我建议 Director 先验证该引用的真实性后再作为 Must-cite 要求。\n\n**[AGREE] R2-W4: \"Latent-GRPO\" 命名可能误导**\n\n同意，如果 Zhang et al. (2026) 原标题是 \"Silence the Judge\" 且原文未使用 \"Latent-GRPO\" 这一名称，论文应使用原文名称或在首次出现时标注 \"which we refer to as Latent-GRPO for brevity\"。学术论文应尊重原作的命名。不过这是一个 minor naming issue，不影响技术判断。\n\n**[AGREE] R2-W5: 可复现性信息不足**\n\n同意，且与我的 reproducibility 评分（3/5）一致。我在审稿中同样指出 GPT-4.1 prompt 未公开和 evidence strength 标注过程不透明。R2 额外指出 GRPO 的关键超参数（采样数、KL penalty、learning rate、batch size）未披露——这确实是一个重要遗漏。Appendix A 仅报告了 reward weight selection 和 response truncation，但缺少 GRPO 训练本身的超参数表。对于一篇 negative result 论文，可复现性尤其重要——读者需要确信 failure 不是由于超参数选择不当。\n\n---\n\n## 小问题\n\n**[AGREE] Abstract 过长**：确认 Abstract 在 PDF 中接近占据一整栏，对于 8 页 long paper 来说偏长。建议压缩到 150-200 词。\n\n**[AGREE] Introduction 与后续章节数字冗余**：Introduction（introduction.tex）中大量引用了具体数字（AUROC 0.827、σ=0.028、0.779、15.4% 等），这些在后续章节中全部重复出现。Introduction 应侧重 high-level narrative，具体数字留给正文。\n\n**[AGREE] Table 4 Cosine R1 显示 \"collapse\" 而非数值**：同意这损害了可比较性。即使是 collapse 状态，也应报告最后一个稳定 checkpoint 的 ToF/NoF/SyconScore 数值。\n\n**[REBUT] d_syc 提取仅用 mean difference，未验证 PCA/CCS-style 替代方案**：这个批评有道理但权重过高。论文的核心论点是 discriminability ≠ utility，而非寻找最优 direction extraction 方法。mean difference 已经给出 AUROC 0.827，PCA/CCS 即使给出更高 AUROC 也不太可能改变核心结论——因为论文已经展示了 recalibration 将 AUROC 提升至 0.910 后仍然 fail（§4 F1c）。更高的 discriminability 并不能解决 valid revision 与 sycophantic capitulation 在 d_syc 方向上 geometrically overlapping 的根本问题。\n\n---\n\n## Missing References\n\n**[REBUT] arXiv:2604.01476**：如上述 W3 所述，需先验证真实性。\n\n**[AGREE] Chen, Huang & Chen (2025) \"Self-Augmented Preference Alignment\"**：如果该工作确实发表于 EMNLP 2025 并涉及 preference alignment 与 sycophancy，应在 Related Work 中引用。\n\n**[AGREE] \"Latent-GRPO\" 命名来源需确认**：同意 R2-W4，应确认并使用原文命名。\n\n---\n\n## 综合评价\n\nR2 给出 3.5（Borderline Conference），我给出 3.0（Findings）。核心分歧不大——我们在 N1/N2（C3 过度声称、ACT vs GRPO confound）上完全一致。我的评分更低主要因为我额外重视了 N3（统计效力：n=2 seeds、ACT seed 2 不完整）和 N2（单模型 generality），这两个问题 R2 未单独列为 Must-Fix 但我认为它们同样影响接收决定。\n\n如果作者能解决 N1/N2（软化 C3 的因果声称、明确列出混淆变量）并增强统计证据（完成 ACT seed 2、增加至少 1 个 seed），我认为 3.5 是合理的目标评分。\n",
    "reviewer_id": "1",
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 119 · 2026-05-22T11:37:33.832225+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4189
}
```

</details>

---


### Assistant

_source line 120 · 2026-05-22T11:37:40.079090+00:00_

交叉回应已提交。核心判断：与 R2 在两个 Must-Fix（C3 过度泛化、ACT vs GRPO confound）上完全一致；对 CRAFT 讨论缺失和 d_syc 提取方法两点提出了部分反驳；建议 Director 验证 R2 引用的 arXiv:2604.01476 的真实性后再作为引用要求。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1"
}
```

</details>

---


## Round 5

## Round 5

48 recorded events


### User

_source line 121 · 2026-05-22T12:40:31.149445+00:00_

[Round 1 审稿请求]:
你负责审查 **方法严谨性 + 实验有效性**。

## Venue 信息
- **EMNLP 2026**（通过 ARR 统一审稿）
- ARR submission deadline: 2026-05-25
- 正文 8 页限制 + 无限参考文献/附录
- ACL 模板，double-blind（匿名）
- Limitations 章节必须有，不计入页数

## 论文文件
- LaTeX 主文件: `projects/contrastive_entrain_calib/docs/paper/main.tex`
- sections 目录: `projects/contrastive_entrain_calib/docs/paper/sections/`
- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/submitted.pdf`

## 你的审查侧重

1. **Reward 设计合理性**：4 个 cosine 变体 + binary/continuous probe 的实验设计是否覆盖了合理的设计空间？是否有明显遗漏的 formulation？
2. **统计声明有效性**：AUROC 的 5-fold CV 是否充分？cross-seed 分析（仅 2 seeds）的可靠性？"4/26 checkpoints exceed vanilla" 这类 claim 的统计支撑？
3. **Confound 控制**：ACT vs GRPO 对比存在多维度差异（supervision granularity, loss family, LoRA capacity 等）——论文是否充分承认了这些 confounds？是否存在 overclaiming？
4. **超参数覆盖**：$w_1$ 仅测试 0.25/0.40；GRPO group size = 2（远低于标准 8-16）；max_completion_length=256 导致 80-84% truncation——这些选择是否影响结论有效性？
5. **可复现性**：训练超参数披露完整性、代码/数据可用性声明、contrastive pairs 构建细节

请严格评估，按 EMNLP 2026 标准给出 Strengths/Weaknesses/Questions/Overall Assessment。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 122 · 2026-05-22T12:40:38.353417+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 123 · 2026-05-22T12:40:38.354110+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/review_reviewer_1_a4d5bbcf.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 124 · 2026-05-22T12:40:40.365100+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3"
  }
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-22T12:40:40.415916+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 126 · 2026-05-22T12:40:44.452243+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude"
  }
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-22T12:40:44.553070+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 128 · 2026-05-22T12:40:49.869282+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
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

_source line 129 · 2026-05-22T12:40:49.969914+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 130 · 2026-05-22T12:40:55.599260+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 131 · 2026-05-22T12:40:58.066464+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/submitted.pdf",
  "project": "contrastive_entrain_calib",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/submitted.pdf",
    "project": "contrastive_entrain_calib",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 132 · 2026-05-22T12:41:03.796077+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's what I found regarding ACL ARR 2026 reviewer guidelines, review form, and scoring criteria:

## Reviewer Guidelines and Scoring

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Overall Recommendation S
…[truncated 1353 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8196
}
```

</details>

---


### Tool result

_source line 133 · 2026-05-22T12:41:05.003001+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 412.2}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 459.1}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 438.3}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 442.7}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 456.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 438.7}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 478.7}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 482.8}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_ima
…[truncated 548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6936
}
```

</details>

---


### Tool call

_source line 134 · 2026-05-22T12:41:10.889130+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
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

_source line 135 · 2026-05-22T12:41:10.944948+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 55
}
```

</details>

---


### Tool call

_source line 136 · 2026-05-22T12:41:12.490047+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/submitted.pdf",
  "project": "contrastive_entrain_calib",
  "pages": "11",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/submitted.pdf",
    "project": "contrastive_entrain_calib",
    "pages": "11",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 137 · 2026-05-22T12:41:13.098027+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 122.2}], \"total_pages\": 11, \"rendered_pages\": 1, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 607
}
```

</details>

---


### Tool call

_source line 138 · 2026-05-22T12:41:13.098528+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 139 · 2026-05-22T12:41:14.003519+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 140 · 2026-05-22T12:41:14.054235+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 141 · 2026-05-22T12:41:14.556481+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 142 · 2026-05-22T12:41:14.960958+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 143 · 2026-05-22T12:41:14.961373+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 144 · 2026-05-22T12:41:15.666831+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1110
}
```

</details>

---


### Tool call

_source line 145 · 2026-05-22T12:41:15.667390+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 146 · 2026-05-22T12:41:15.768717+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 807
}
```

</details>

---


### Tool result

_source line 147 · 2026-05-22T12:41:16.322754+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 655
}
```

</details>

---


### Tool call

_source line 148 · 2026-05-22T12:41:25.215516+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 149 · 2026-05-22T12:41:25.516704+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 150 · 2026-05-22T12:41:26.021256+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 151 · 2026-05-22T12:41:26.878084+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1662
}
```

</details>

---


### Tool result

_source line 152 · 2026-05-22T12:41:26.883460+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1366
}
```

</details>

---


### Tool call

_source line 153 · 2026-05-22T12:41:26.884329+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 154 · 2026-05-22T12:41:27.386602+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1365
}
```

</details>

---


### Tool call

_source line 155 · 2026-05-22T12:41:27.387037+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 156 · 2026-05-22T12:41:28.241376+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1357
}
```

</details>

---


### Tool result

_source line 157 · 2026-05-22T12:41:28.242540+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 158 · 2026-05-22T12:41:28.242941+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 159 · 2026-05-22T12:41:28.847444+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---


### Tool call

_source line 160 · 2026-05-22T12:41:30.253678+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and detailed descriptions. I need: soundness, excitement, overall assessment, confidence, and any other dimensions with their exact score descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and detailed descriptions. I need: soundness, excitement, overall assessment, confidence, and any other dimensions with their exact score descriptions."
  }
}
```

</details>

---


### Tool result

_source line 161 · 2026-05-22T12:41:38.347953+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Reviewer Confidence
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: Quite sure with unlikely but conceivable oversights
- **3**: Pretty sure but possible gaps in detail checking
- **2**: Willing to defend evaluation but likely missed details
- **1**: Outside expertise area or paper unclear

## Soundness
Scale: 1-5 (with half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: Strong support for claims; extra experiments optional
- **3**: Sufficient support for main claims; minor points need details
- **2**: Major claims lack support; significant technical problems
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement
Scale: 1-5 (with half-point increments)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation"
- **4**: Notable work worthy of personal recommendation
- **3**: Interesting; might mention to others if time permits
- **2**: May resonate with some community members
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others"

## Overall Assessment
Scale: 1-5 (with half-point increments)
- **5**: Consider for Award (top 2.5% papers)
- **4.5**: Borderline Award
- **4**: Conference acceptance
- **3.5**: Borderline Conference
- **3**: Findings acceptance
- **2.5**: Borderline Findings
- **2**: Needs substantial revisions by next cycle
- **1.5**: Needs revisions beyond next cycle
- **1**: Do not resubmit

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8094
}
```

</details>

---


### Tool call

_source line 162 · 2026-05-22T12:46:00.651195+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿意见：方法严谨性 + 实验有效性\n\n## 总体评分\n**Overall**: 2.5 (Borderline Findings)\n**一句话总结**: 论文提出了重要的概念框架（discriminability ≠ reward utility），但核心负面结论受到多个未控制的实验混淆因素严重削弱——GRPO group_size=2、80-84% 截断、仅 2 seeds、极窄超参数搜索——无法排除 GRPO 优化本身不足导致失败的替代解释。\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2.5/5 | 核心负面声明有多个严重混淆因素未控制；无法区分\"reward 信号本质缺陷\"和\"GRPO 优化配置不足\" |\n| Excitement | 3/5 | 问题重要且及时，失败分类学有价值，但负面结果在实验不充分条件下影响力有限 |\n| Confidence | 4/5 | 熟悉 RL alignment、representation engineering 和 sycophancy 文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] GRPO group_size=2 严重偏离标准实践，可能是失败的主因而非 d_syc 本身\n\n- 具体位置：Table 5 (Appendix A, p.10)\n- 问题：标准 GRPO（如 DeepSeek-R1, Shao et al. 2024）使用 group_size 8-64。group_size=2 退化为噪声极高的 pairwise 对比，对含噪 cosine reward 会极度放大梯度估计方差。论文未给出任何理由也未测试更大值。\n- 为什么影响接收：核心声明 \"every d_syc-based GRPO formulation fails\"（Abstract, §1），但如果 GRPO 优化器因 group_size 不足而无法利用任何微弱信号，失败就不能归因于 d_syc。这是致命的替代解释。\n- 建议：至少测试 group_size ∈ {8, 16}，或提供消融实验。\n\n**N2** [critical] max_completion_length=256 导致 80-84% 截断，严重损害 reward 信号有效性\n\n- 具体位置：Appendix A (p.10)\n- 问题：sycophancy calibration 的核心行为（belief revision/capitulation）常在多轮对话后半段发生。80-84% 截断意味着 reward 在不完整输出上计算。论文辩护\"response-level decisions manifest within first 100-200 tokens\"是未验证的经验声明。§5 的 probe reward trap（ToF=0 at step 500）可能正因截断而非 probe 缺陷导致。\n- 为什么影响接收：提供了另一个强替代解释。\"shared across conditions\" 只保证公式间相对比较有效，不支持\"d_syc-based rewards 本质失败\"的绝对声明。\n- 建议：至少在一个公式上测试 max_completion_length=512/1024。\n\n**N3** [critical] 仅 2 random seeds 不足以支撑负面结论\n\n- 具体位置：§9/Reproducibility (p.8-9)\n- 问题：RL 训练高方差众所周知。2 seeds 无法提供有意义方差估计。\"4/26 checkpoints exceed vanilla\"（Table 4 footnote）的可靠性完全依赖 2 seeds 的代表性。负面结论证据标准应高于正面结论。\n- 建议：增加到 3-5 seeds 并报告 mean ± std。\n\n**N4** [critical] Reward 设计空间探索不足，声明过度推广\n\n- 具体位置：§2.2 (p.3), §4 (p.4-5), Table 2, Appendix A\n- 问题：6 个 formulation 均为简单标量变换/单层 probe。遗漏：(1) learned reward（MLP on d_syc features）；(2) 多层聚合（仅用 best layer L19，Figure 1 显示其他层也有信号）；(3) 非线性变换。w₁ 仅测试 0.25/0.40 两个值——在 w₁=0.25 时 d_syc 仅贡献 ~8.3% reward 方差，信号被淹没，但未尝试更高 w₁。\n- 为什么影响接收：负面结论强度受限于设计空间覆盖。\"every formulation fails\" 声明 overclaiming。\n- 建议：(1) 至少加一个 learned reward 变体；(2) 测试 w₁ 更宽范围 {0.1, 0.25, 0.4, 0.6, 0.8}；(3) 将声明限定为 \"tested formulations\"。\n\n---\n\n## Should-Fix 问题\n\n**W1** [warning] ACT vs GRPO 对比 confounds 大量，叙事过度依赖此对比\n\n- 具体位置：§6-7 (p.6-7), Table 4\n- 问题：§7 承认 confounds（per-token vs per-completion、L2 vs policy gradient、labeled pairs vs self-discovery、direct layer manipulation vs output-level、SFT stability vs RL variance），但叙事结构仍大量用 ACT 成功反衬 GRPO 失败。SYCONSCORE 对比（ACT 0.301 vs GRPO best ~0.143）在不控制 confounds 时无法得出 reward formulation 的因果结论。\n- 建议：降低 ACT 对比叙事权重，或设计更 controlled 对比。\n\n**W2** [warning] SYCONSCORE 指标有效性未充分建立\n\n- 具体位置：§2.5 (p.3), Equation 2\n- 问题：SYCONSCORE 似为本文新指标（ToF/NoF 调和平均），未与已有 sycophancy benchmark 对比验证，未讨论调和平均选择理由，未验证与人类判断相关性。\n- 建议：解释指标选择理由，或与已有 benchmark 做相关性分析。\n\n**W3** [warning] 181 contrastive pairs 质量控制不足\n\n- 具体位置：§2 (p.2)\n- 问题：GPT-4.1 生成，仅 automated validation + 3 retries。无人工验证/inter-annotator agreement。19/200 对被丢弃（~10%）但未分析被丢弃对特征。\n- 建议：增加小规模人工验证。\n\n**W4** [warning] Figure 3 cross-seed 分析与文字描述存在 tension\n\n- 具体位置：§7 (p.7), Figure 3\n- 问题：2 seeds 的 SYCONSCORE 轨迹差异显著。\"4/26 checkpoints exceed vanilla\" 可能是 seed-dependent 而非 systematic failure。未量化 per-seed 成功 checkpoint 分布。\n\n---\n\n## 小问题\n\n- §1: \"entropy remained healthy\" 含糊，建议给具体数值。\n- Table 2: \"gate saturation\" 缺操作性定义（何种阈值算 saturated）。\n- §8 Related Work 与核心贡献连接不紧密。\n- Appendix B: Stubbornness taxonomy 仅 100 条样本，无 inter-rater reliability。\n- Equation 1: \"residual-stream activations\" 提取位置（layer output vs attention vs MLP）可更明确。\n\n---\n\n## 主要优势\n\n- 问题重要且及时——sycophancy 是 LLM alignment 核心挑战。\n- 失败诊断链（gate saturation → gradient vanishing → mode collapse → behavioral death → probe reward trap）对 practitioners 有参考价值。\n- d_syc 方向本身验证扎实：5-fold CV AUROC 0.827/0.779，cross-model 一致性，evidence-strength 梯度效应。\n- \"Discriminability ≠ utility\" 概念框架清晰，有潜力影响更广泛的 reward design。\n- 诚实的 limitations 声明。\n\n---\n\n**总结**：这是一篇提出了有价值概念框架的论文，但作为负面结果论文（negative result paper），其证据标准不足。核心声明\"d_syc-based rewards fundamentally fail\"需要在排除 GRPO 优化不足（group_size=2, 80-84% truncation, 2 seeds, narrow w₁ search）这一强替代解释后才能成立。建议补充实验后重新投稿。",
  "reviewer_id": "1",
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿意见：方法严谨性 + 实验有效性\n\n## 总体评分\n**Overall**: 2.5 (Borderline Findings)\n**一句话总结**: 论文提出了重要的概念框架（discriminability ≠ reward utility），但核心负面结论受到多个未控制的实验混淆因素严重削弱——GRPO group_size=2、80-84% 截断、仅 2 seeds、极窄超参数搜索——无法排除 GRPO 优化本身不足导致失败的替代解释。\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2.5/5 | 核心负面声明有多个严重混淆因素未控制；无法区分\"reward 信号本质缺陷\"和\"GRPO 优化配置不足\" |\n| Excitement | 3/5 | 问题重要且及时，失败分类学有价值，但负面结果在实验不充分条件下影响力有限 |\n| Confidence | 4/5 | 熟悉 RL alignment、representation engineering 和 sycophancy 文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] GRPO group_size=2 严重偏离标准实践，可能是失败的主因而非 d_syc 本身\n\n- 具体位置：Table 5 (Appendix A, p.10)\n- 问题：标准 GRPO（如 DeepSeek-R1, Shao et al. 2024）使用 group_size 8-64。group_size=2 退化为噪声极高的 pairwise 对比，对含噪 cosine reward 会极度放大梯度估计方差。论文未给出任何理由也未测试更大值。\n- 为什么影响接收：核心声明 \"every d_syc-based GRPO formulation fails\"（Abstract, §1），但如果 GRPO 优化器因 group_size 不足而无法利用任何微弱信号，失败就不能归因于 d_syc。这是致命的替代解释。\n- 建议：至少测试 group_size ∈ {8, 16}，或提供消融实验。\n\n**N2** [critical] max_completion_length=256 导致 80-84% 截断，严重损害 reward 信号有效性\n\n- 具体位置：Appendix A (p.10)\n- 问题：sycophancy calibration 的核心行为（belief revision/capitulation）常在多轮对话后半段发生。80-84% 截断意味着 reward 在不完整输出上计算。论文辩护\"response-level decisions manifest within first 100-200 tokens\"是未验证的经验声明。§5 的 probe reward trap（ToF=0 at step 500）可能正因截断而非 probe 缺陷导致。\n- 为什么影响接收：提供了另一个强替代解释。\"shared across conditions\" 只保证公式间相对比较有效，不支持\"d_syc-based rewards 本质失败\"的绝对声明。\n- 建议：至少在一个公式上测试 max_completion_length=512/1024。\n\n**N3** [critical] 仅 2 random seeds 不足以支撑负面结论\n\n- 具体位置：§9/Reproducibility (p.8-9)\n- 问题：RL 训练高方差众所周知。2 seeds 无法提供有意义方差估计。\"4/26 checkpoints exceed vanilla\"（Table 4 footnote）的可靠性完全依赖 2 seeds 的代表性。负面结论证据标准应高于正面结论。\n- 建议：增加到 3-5 seeds 并报告 mean ± std。\n\n**N4** [critical] Reward 设计空间探索不足，声明过度推广\n\n- 具体位置：§2.2 (p.3), §4 (p.4-5), Table 2, Appendix A\n- 问题：6 个 formulation 均为简单标量变换/单层 probe。遗漏：(1) learned reward（MLP on d_syc features）；(2) 多层聚合（仅用 best layer L19，Figure 1 显示其他层也有信号）；(3) 非线性变换。w₁ 仅测试 0.25/0.40 两个值——在 w₁=0.25 时 d_syc 仅贡献 ~8.3% reward 方差，信号被淹没，但未尝试更高 w₁。\n- 为什么影响接收：负面结论强度受限于设计空间覆盖。\"every formulation fails\" 声明 overclaiming。\n- 建议：(1) 至少加一个 learned reward 变体；(2) 测试 w₁ 更宽范围 {0.1, 0.25, 0.4, 0.6, 0.8}；(3) 将声明限定为 \"tested formulations\"。\n\n---\n\n## Should-Fix 问题\n\n**W1** [warning] ACT vs GRPO 对比 confounds 大量，叙事过度依赖此对比\n\n- 具体位置：§6-7 (p.6-7), Table 4\n- 问题：§7 承认 confounds（per-token vs per-completion、L2 vs policy gradient、labeled pairs vs self-discovery、direct layer manipulation vs output-level、SFT stability vs RL variance），但叙事结构仍大量用 ACT 成功反衬 GRPO 失败。SYCONSCORE 对比（ACT 0.301 vs GRPO best ~0.143）在不控制 confounds 时无法得出 reward formulation 的因果结论。\n- 建议：降低 ACT 对比叙事权重，或设计更 controlled 对比。\n\n**W2** [warning] SYCONSCORE 指标有效性未充分建立\n\n- 具体位置：§2.5 (p.3), Equation 2\n- 问题：SYCONSCORE 似为本文新指标（ToF/NoF 调和平均），未与已有 sycophancy benchmark 对比验证，未讨论调和平均选择理由，未验证与人类判断相关性。\n- 建议：解释指标选择理由，或与已有 benchmark 做相关性分析。\n\n**W3** [warning] 181 contrastive pairs 质量控制不足\n\n- 具体位置：§2 (p.2)\n- 问题：GPT-4.1 生成，仅 automated validation + 3 retries。无人工验证/inter-annotator agreement。19/200 对被丢弃（~10%）但未分析被丢弃对特征。\n- 建议：增加小规模人工验证。\n\n**W4** [warning] Figure 3 cross-seed 分析与文字描述存在 tension\n\n- 具体位置：§7 (p.7), Figure 3\n- 问题：2 seeds 的 SYCONSCORE 轨迹差异显著。\"4/26 checkpoints exceed vanilla\" 可能是 seed-dependent 而非 systematic failure。未量化 per-seed 成功 checkpoint 分布。\n\n---\n\n## 小问题\n\n- §1: \"entropy remained healthy\" 含糊，建议给具体数值。\n- Table 2: \"gate saturation\" 缺操作性定义（何种阈值算 saturated）。\n- §8 Related Work 与核心贡献连接不紧密。\n- Appendix B: Stubbornness taxonomy 仅 100 条样本，无 inter-rater reliability。\n- Equation 1: \"residual-stream activations\" 提取位置（layer output vs attention vs MLP）可更明确。\n\n---\n\n## 主要优势\n\n- 问题重要且及时——sycophancy 是 LLM alignment 核心挑战。\n- 失败诊断链（gate saturation → gradient vanishing → mode collapse → behavioral death → probe reward trap）对 practitioners 有参考价值。\n- d_syc 方向本身验证扎实：5-fold CV AUROC 0.827/0.779，cross-model 一致性，evidence-strength 梯度效应。\n- \"Discriminability ≠ utility\" 概念框架清晰，有潜力影响更广泛的 reward design。\n- 诚实的 limitations 声明。\n\n---\n\n**总结**：这是一篇提出了有价值概念框架的论文，但作为负面结果论文（negative result paper），其证据标准不足。核心声明\"d_syc-based rewards fundamentally fail\"需要在排除 GRPO 优化不足（group_size=2, 80-84% truncation, 2 seeds, narrow w₁ search）这一强替代解释后才能成立。建议补充实验后重新投稿。",
    "reviewer_id": "1",
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 163 · 2026-05-22T12:46:04.468042+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3816
}
```

</details>

---


### Tool call

_source line 164 · 2026-05-22T12:46:10.151466+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
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

_source line 165 · 2026-05-22T12:46:10.202056+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 166 · 2026-05-22T12:46:14.123564+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 167 · 2026-05-22T12:46:14.175366+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 51
}
```

</details>

---


### Assistant

_source line 168 · 2026-05-22T12:46:20.100664+00:00_

审稿意见已提交给 Review Director。

**评分摘要**：Overall 2.5 (Borderline Findings)，Soundness 2.5/5，Excitement 3/5。

**核心问题**：4 个 critical issues——(1) GRPO group_size=2 严重偏离标准实践；(2) 80-84% response 截断损害 reward 有效性；(3) 仅 2 seeds 不足以支撑负面结论；(4) reward 设计空间探索过窄，声明过度推广。这些混淆因素使得无法区分"d_syc 本质不可用"和"GRPO 优化配置不足"两种解释。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1"
}
```

</details>

---


## Round 6

## Round 6

18 recorded events


### User

_source line 169 · 2026-05-22T12:47:36.671123+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix / Should-Fix / 小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 审稿意见：新颖性 + Framing 完整性

**Overall**: 3.0（Findings）

### Must-Fix 问题

**N1** [critical] Title 和 claims 范围显著超出实验证据
- 标题声称 "Sycophancy Directions Fail as Scalar RL Rewards"，但仅测试 GRPO。C3 将失败归因于 reward signal 本身而非 GRPO 的 specific optimization dynamics，此归因未被实验证实。
- 建议：将标题改为 "…as GRPO Rewards" 或 "…as Scalar Per-Completion Rewards: Evidence from GRPO"；或补充 PPO/REINFORCE 实验。

**N2** [critical] C3 的 ACT vs GRPO 对比存在严重 confound，但被表述为 contribution
- C3 声称 "sparse RL reward failed to convey the valid/invalid distinction"，核心证据来自 ACT 成功而 GRPO 失败。但 ACT 与 GRPO 至少在 5 个维度上不同（SFT vs RL、per-token vs per-completion、labeled pairs vs self-discovery、L2 vs reward maximization、training data format）。
- 观察性发现被提升为因果性 contribution。

### Should-Fix 问题

**W1** Wu & Tang (2026) 的对比论证缺乏定量支撑——"geometric separability" 论点完全定性。
**W2** "Discriminability ≠ Reward Utility" 原则的泛化性声明超出证据（仅 sycophancy + GRPO）。
**W3** SMART (Beigi et al., 2025) 讨论过于简略——作为中间监督密度案例，应更深入讨论。
**W4** 实验规模偏小（181 pairs, 2 seeds, 单模型 RL 训练）。

### 小问题
- Abstract 信息密度极高（~250 words），建议精简。
- SYCONSCORE harmonic mean 选择未充分 justify。
- Table 2 failure mode 术语定义不精确（"mode collapse" 是否准确？）
- Figure 1 y 轴标签未在 caption 中解释。
- §6 "semantic gap" 未形式化。

### 主要优势
1. 研究问题重要且及时
2. Probe reward trap (C2) 是新颖实证发现
3. 跨模型验证增强可信度
4. 与 Papadatos & Freedman (2024) 对比分析精到
5. 实验设计严谨（5-fold CV, evidence strength 分层）
6. Stubbornness taxonomy 有价值

---

请逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 170 · 2026-05-22T12:48:13.774051+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/submitted.pdf",
  "project": "contrastive_entrain_calib",
  "pages": "1-2",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/submitted.pdf",
    "project": "contrastive_entrain_calib",
    "pages": "1-2",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 171 · 2026-05-22T12:48:14.176814+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 412.2}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 459.1}], \"total_pages\": 11, \"rendered_pages\": 2, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 172 · 2026-05-22T12:48:19.750770+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 173 · 2026-05-22T12:48:20.103104+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 174 · 2026-05-22T12:48:20.609610+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 858
}
```

</details>

---


### Tool result

_source line 175 · 2026-05-22T12:48:21.014888+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 911
}
```

</details>

---


### Tool call

_source line 176 · 2026-05-22T12:48:25.680613+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/submitted.pdf",
  "project": "contrastive_entrain_calib",
  "pages": "6,8",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/submitted.pdf",
    "project": "contrastive_entrain_calib",
    "pages": "6,8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 177 · 2026-05-22T12:48:25.933120+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 438.7}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 482.8}], \"total_pages\": 11, \"rendered_pages\": 2, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 178 · 2026-05-22T12:48:29.603079+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 179 · 2026-05-22T12:48:30.007577+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 180 · 2026-05-22T12:48:30.725447+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1122
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-22T12:48:31.128844+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1121
}
```

</details>

---


### Tool call

_source line 182 · 2026-05-22T12:49:50.489759+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: Title 和 claims 范围超出实验证据**\n\n同意。这与我自己的 N4（设计空间探索不足）高度相关。论文标题 \"Why Sycophancy Directions Fail as Scalar RL Rewards\" 暗示了对所有 scalar RL rewards 的普遍性声明，但实验仅覆盖 GRPO。关键证据来自论文自身——§8 Future Directions (p.8) 明确承认：\"The scalar per-completion reward structure is shared by PPO, RLOO, and other REINFORCE-style methods; whether they exhibit similar failures remains an open question.\" 这一句直接承认 PPO/REINFORCE 是否复现失败尚不确定，与标题的普遍性声明矛盾。\n\n补充发现：C1 的措辞 \"Every tested GRPO formulation fails\"（p.2）实际上已经用了 \"tested GRPO\" 的限定词，比标题更谨慎。标题与正文 contributions 之间存在 scope 不一致。R2 建议改标题为 \"…as GRPO Rewards\" 或补充 PPO/REINFORCE 实验，两者都是合理的修改路径。\n\n**[AGREE] R2-N2: C3 的 ACT vs GRPO 对比被表述为 contribution 但 confound 未解决**\n\n同意，与我的 W1 一致。论文 §7 (p.7) 的原文：\"ACT and GRPO differ along multiple dimensions beyond supervision granularity, so we cannot rotate the causal factor behind ACT's advantage\"——论文自己承认无法归因，但 p.2 的 C3 仍表述为 \"In our experiments, sparse RL reward failed to convey the valid/invalid distinction\"，并将其列为三大 contribution 之一。这里存在逻辑矛盾：如果你承认无法归因，就不应将观察性比较提升为 contribution。\n\nR2 的批评比我的 W1 更精准——我将其列为 Should-Fix，但实际上作为 contribution 声明，其 confound 问题确实是 critical 级别。ACT 的成功可能完全归因于 SFT 的固有稳定性优势、labeled data 的直接监督信号、或 per-token loss 的梯度密度，而与 \"representation vs. reward\" 这个叙事框架无关。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Wu & Tang (2026) 的 \"geometric separability\" 论点缺乏定量支撑**\n\n同意。§6 (p.6) 引用 Wu & Tang (2026) 称 \"concept directions applied via activation modification or GRPO achieve 100% validation accuracy for reward hacking detection, where shortcut behaviors are geometrically separable\"，用以论证 direction utility 取决于 geometric separability。但论文未提供自己的定量证据来衡量 d_syc 的 \"几何可分性程度\"。例如，论文可以计算 d_syc 在 online RL 分布下的 cosine similarity 分布重叠度（valid vs. sycophantic），与 Wu & Tang 中 reward hacking 场景的分离度做定量对比，从而将定性论点升级为定量证据。\n\n**[AGREE] R2-W2: \"Discriminability ≠ Reward Utility\" 泛化声明超出证据**\n\n同意，与我的 N4 一致。该原则仅在一个行为维度（sycophancy）、一个 RL 算法（GRPO）上验证。§8 (p.8) 的 \"Beyond sycophancy, the principle that discriminability does not guarantee scalar reward utility may apply to other behavioral attributes where the target and its complement share the same geometric direction\" 是合理的未来方向猜想，但论文标题和 Abstract 的措辞暗示了更强的普遍性。\n\n**[AGREE] R2-W3: SMART (Beigi et al., 2025) 讨论过于简略**\n\n同意。§8 (p.8) 仅用一句话提及 SMART：\"SMART (Beigi et al., 2025) applies per-step process rewards with MCTS for sycophancy, representing intermediate supervision density between scalar per-completion rewards and dense per-token approaches.\" 作为 per-completion（GRPO）和 per-token（ACT）之间的中间形态，SMART 直接回应了论文的核心发现——supervision granularity 对成败的影响。如果 SMART 的 per-step 方式部分成功，这将为\"密度是关键因素\"提供更细粒度的证据；如果也失败，则加强\"问题不在密度而在 d_syc 本身\"的论点。无论如何，更深入讨论 SMART 都会显著增强 §8 的论证力度。\n\n**[AGREE] R2-W4: 实验规模偏小**\n\n同意，与我的 N3（2 seeds）和 W3（181 pairs）一致。补充一点：RL 训练仅在 Qwen3-8B 上执行（Llama-3-8B 仅做了 discriminability 验证，未做 GRPO 训练），这进一步限制了结论的泛化性。论文 Limitations (p.8) 承认了这一点。\n\n---\n\n### 小问题\n\n**[REBUT] R2-Minor-1: Abstract 信息密度过高**\n\n轻微反驳。*ACL 系列会议的 abstract 通常 200-300 words，该 abstract 的信息密度在可接受范围内。对于一篇负面结果论文，abstract 需要同时传达 (1) 方法有效（discriminability）、(2) 但 reward 失败、(3) 失败机制，信息量本身难以压缩。不过如果简化措辞（如合并部分数字）能改善可读性，这是值得做的 polish。\n\n**[AGREE] R2-Minor-2: SYCONSCORE harmonic mean 选择未充分 justify**\n\n同意，与我的 W2 一致。Equation 2 (§2.5, p.3) 给出定义但未解释为何选择 harmonic mean（对低值更敏感）而非 arithmetic mean 或 F-beta。\n\n**[AGREE] R2-Minor-3: Table 2 failure mode 术语不精确**\n\n同意。Table 2 (p.5) 中 F1d 的 \"Mode collapse\" 需要操作性定义。在 RL 文献中 mode collapse 通常指策略退化到单一输出模式，但表中描述的是 \"mode collapse\" 伴随 \"scaled cosine\" 的行为——是否指 reward 空间的坍缩而非策略空间？需要明确。\n\n**[AGREE] R2-Minor-4: Figure 1 y 轴标签未在 caption 中解释**\n\n同意。Figure 1 (p.5) 的 y 轴标签应在 caption 中明确说明 AUROC 的含义和计算方式。\n\n**[AGREE] R2-Minor-5: §6 \"semantic gap\" 未形式化**\n\n同意。§6 (p.6) 的 \"semantic gap between discriminability and reward utility\" 是论文的核心概念贡献，但仅以自然语言描述。可以考虑形式化为：给定方向 d 和行为空间上的 reward function R*，定义 \"utility gap\" 为 d 的分类 AUROC 与 d-based reward 的 GRPO 策略改进之间的差距。即使简单的形式化也比纯定性描述更有说服力。\n\n---\n\n### 对 R2 优势评价的补充\n\nR2 列出的 6 条优势我基本认同，特别是：\n- **Probe reward trap (C2)** 确实是最有价值的实证发现——behavioral death 先于 distributional collapse、1,300-step 的检测盲区对 practitioners 有直接的实践警示。\n- **跨模型验证**（Qwen3-8B + Llama-3-8B 的 AUROC 一致性）增强了 d_syc 方向本身的可信度，尽管 RL 训练仅在单模型上执行。\n\n---\n\n### R1 与 R2 评分差异说明\n\nR2 给 Overall 3.0（Findings），我给 2.5（Borderline Findings）。差异主要来自我对 GRPO 优化配置（group_size=2, 80-84% truncation）的更重视——这些是 R2 未重点讨论但我认为是核心 confound 的问题。如果 GRPO 本身因 group_size 过小和严重截断而无法正常工作，那么不仅 C1 的负面结论不可靠，C2（probe reward trap）的失败机制归因也可能不准确——behavioral death 可能是截断而非 probe 的产物。这些 confounds 同时削弱了 R2 所认可的 C2 新颖性。\n\n综合两份审稿，核心共识是：**标题/claims 的 overclaiming（R2-N1 + R1-N4）** 和 **ACT vs GRPO confound（R2-N2 + R1-W1）** 是两个需要共同解决的关键问题。",
  "reviewer_id": "1",
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: Title 和 claims 范围超出实验证据**\n\n同意。这与我自己的 N4（设计空间探索不足）高度相关。论文标题 \"Why Sycophancy Directions Fail as Scalar RL Rewards\" 暗示了对所有 scalar RL rewards 的普遍性声明，但实验仅覆盖 GRPO。关键证据来自论文自身——§8 Future Directions (p.8) 明确承认：\"The scalar per-completion reward structure is shared by PPO, RLOO, and other REINFORCE-style methods; whether they exhibit similar failures remains an open question.\" 这一句直接承认 PPO/REINFORCE 是否复现失败尚不确定，与标题的普遍性声明矛盾。\n\n补充发现：C1 的措辞 \"Every tested GRPO formulation fails\"（p.2）实际上已经用了 \"tested GRPO\" 的限定词，比标题更谨慎。标题与正文 contributions 之间存在 scope 不一致。R2 建议改标题为 \"…as GRPO Rewards\" 或补充 PPO/REINFORCE 实验，两者都是合理的修改路径。\n\n**[AGREE] R2-N2: C3 的 ACT vs GRPO 对比被表述为 contribution 但 confound 未解决**\n\n同意，与我的 W1 一致。论文 §7 (p.7) 的原文：\"ACT and GRPO differ along multiple dimensions beyond supervision granularity, so we cannot rotate the causal factor behind ACT's advantage\"——论文自己承认无法归因，但 p.2 的 C3 仍表述为 \"In our experiments, sparse RL reward failed to convey the valid/invalid distinction\"，并将其列为三大 contribution 之一。这里存在逻辑矛盾：如果你承认无法归因，就不应将观察性比较提升为 contribution。\n\nR2 的批评比我的 W1 更精准——我将其列为 Should-Fix，但实际上作为 contribution 声明，其 confound 问题确实是 critical 级别。ACT 的成功可能完全归因于 SFT 的固有稳定性优势、labeled data 的直接监督信号、或 per-token loss 的梯度密度，而与 \"representation vs. reward\" 这个叙事框架无关。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Wu & Tang (2026) 的 \"geometric separability\" 论点缺乏定量支撑**\n\n同意。§6 (p.6) 引用 Wu & Tang (2026) 称 \"concept directions applied via activation modification or GRPO achieve 100% validation accuracy for reward hacking detection, where shortcut behaviors are geometrically separable\"，用以论证 direction utility 取决于 geometric separability。但论文未提供自己的定量证据来衡量 d_syc 的 \"几何可分性程度\"。例如，论文可以计算 d_syc 在 online RL 分布下的 cosine similarity 分布重叠度（valid vs. sycophantic），与 Wu & Tang 中 reward hacking 场景的分离度做定量对比，从而将定性论点升级为定量证据。\n\n**[AGREE] R2-W2: \"Discriminability ≠ Reward Utility\" 泛化声明超出证据**\n\n同意，与我的 N4 一致。该原则仅在一个行为维度（sycophancy）、一个 RL 算法（GRPO）上验证。§8 (p.8) 的 \"Beyond sycophancy, the principle that discriminability does not guarantee scalar reward utility may apply to other behavioral attributes where the target and its complement share the same geometric direction\" 是合理的未来方向猜想，但论文标题和 Abstract 的措辞暗示了更强的普遍性。\n\n**[AGREE] R2-W3: SMART (Beigi et al., 2025) 讨论过于简略**\n\n同意。§8 (p.8) 仅用一句话提及 SMART：\"SMART (Beigi et al., 2025) applies per-step process rewards with MCTS for sycophancy, representing intermediate supervision density between scalar per-completion rewards and dense per-token approaches.\" 作为 per-completion（GRPO）和 per-token（ACT）之间的中间形态，SMART 直接回应了论文的核心发现——supervision granularity 对成败的影响。如果 SMART 的 per-step 方式部分成功，这将为\"密度是关键因素\"提供更细粒度的证据；如果也失败，则加强\"问题不在密度而在 d_syc 本身\"的论点。无论如何，更深入讨论 SMART 都会显著增强 §8 的论证力度。\n\n**[AGREE] R2-W4: 实验规模偏小**\n\n同意，与我的 N3（2 seeds）和 W3（181 pairs）一致。补充一点：RL 训练仅在 Qwen3-8B 上执行（Llama-3-8B 仅做了 discriminability 验证，未做 GRPO 训练），这进一步限制了结论的泛化性。论文 Limitations (p.8) 承认了这一点。\n\n---\n\n### 小问题\n\n**[REBUT] R2-Minor-1: Abstract 信息密度过高**\n\n轻微反驳。*ACL 系列会议的 abstract 通常 200-300 words，该 abstract 的信息密度在可接受范围内。对于一篇负面结果论文，abstract 需要同时传达 (1) 方法有效（discriminability）、(2) 但 reward 失败、(3) 失败机制，信息量本身难以压缩。不过如果简化措辞（如合并部分数字）能改善可读性，这是值得做的 polish。\n\n**[AGREE] R2-Minor-2: SYCONSCORE harmonic mean 选择未充分 justify**\n\n同意，与我的 W2 一致。Equation 2 (§2.5, p.3) 给出定义但未解释为何选择 harmonic mean（对低值更敏感）而非 arithmetic mean 或 F-beta。\n\n**[AGREE] R2-Minor-3: Table 2 failure mode 术语不精确**\n\n同意。Table 2 (p.5) 中 F1d 的 \"Mode collapse\" 需要操作性定义。在 RL 文献中 mode collapse 通常指策略退化到单一输出模式，但表中描述的是 \"mode collapse\" 伴随 \"scaled cosine\" 的行为——是否指 reward 空间的坍缩而非策略空间？需要明确。\n\n**[AGREE] R2-Minor-4: Figure 1 y 轴标签未在 caption 中解释**\n\n同意。Figure 1 (p.5) 的 y 轴标签应在 caption 中明确说明 AUROC 的含义和计算方式。\n\n**[AGREE] R2-Minor-5: §6 \"semantic gap\" 未形式化**\n\n同意。§6 (p.6) 的 \"semantic gap between discriminability and reward utility\" 是论文的核心概念贡献，但仅以自然语言描述。可以考虑形式化为：给定方向 d 和行为空间上的 reward function R*，定义 \"utility gap\" 为 d 的分类 AUROC 与 d-based reward 的 GRPO 策略改进之间的差距。即使简单的形式化也比纯定性描述更有说服力。\n\n---\n\n### 对 R2 优势评价的补充\n\nR2 列出的 6 条优势我基本认同，特别是：\n- **Probe reward trap (C2)** 确实是最有价值的实证发现——behavioral death 先于 distributional collapse、1,300-step 的检测盲区对 practitioners 有直接的实践警示。\n- **跨模型验证**（Qwen3-8B + Llama-3-8B 的 AUROC 一致性）增强了 d_syc 方向本身的可信度，尽管 RL 训练仅在单模型上执行。\n\n---\n\n### R1 与 R2 评分差异说明\n\nR2 给 Overall 3.0（Findings），我给 2.5（Borderline Findings）。差异主要来自我对 GRPO 优化配置（group_size=2, 80-84% truncation）的更重视——这些是 R2 未重点讨论但我认为是核心 confound 的问题。如果 GRPO 本身因 group_size 过小和严重截断而无法正常工作，那么不仅 C1 的负面结论不可靠，C2（probe reward trap）的失败机制归因也可能不准确——behavioral death 可能是截断而非 probe 的产物。这些 confounds 同时削弱了 R2 所认可的 C2 新颖性。\n\n综合两份审稿，核心共识是：**标题/claims 的 overclaiming（R2-N1 + R1-N4）** 和 **ACT vs GRPO confound（R2-N2 + R1-W1）** 是两个需要共同解决的关键问题。",
    "reviewer_id": "1",
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 183 · 2026-05-22T12:49:54.205990+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3716
}
```

</details>

---


### Tool call

_source line 184 · 2026-05-22T12:50:04.272016+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 185 · 2026-05-22T12:50:04.272554+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 186 · 2026-05-22T12:50:12.878423+00:00_

已提交对 R2 的逐条回应。总结：

- **Must-Fix**：R2-N1（标题 overclaiming）和 R2-N2（C3 confound 作为 contribution）均 **[AGREE]**，与我自己的 N4 和 W1 一致
- **Should-Fix**：W1-W4 全部 **[AGREE]**，其中 W3（SMART 讨论不足）和 W4（实验规模）补充了我自己的发现
- **小问题**：仅对 Abstract 信息密度 **[REBUT]**（*ACL 论文 abstract 的密度在合理范围），其余 4 条均 **[AGREE]**
- **评分差异说明**：我比 R2 低 0.5 分（2.5 vs 3.0），主要因为我更重视 group_size=2 和 80-84% truncation 这两个 R2 未重点讨论的优化配置问题

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1"
}
```

</details>

---


## Round 7

## Round 7

68 recorded events


### User

_source line 187 · 2026-05-22T14:00:27.700351+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性 + 实验设计**。

## Venue 信息
- **目标**: EMNLP 2026 via ARR May 2026
- **截止日期**: 2026-05-25
- **页数限制**: 正文 8 页（Long paper），参考文献无限制，Limitations 不计入页数
- **模板**: ACL style (two-column, 11pt, a4paper)
- **匿名规则**: Double-blind

## 论文文件
- LaTeX: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/submitted.pdf`

## 你的审查侧重

**核心关注**：方法论严谨性、实验设计、统计方法、claims 与证据的对齐度。

请重点审查以下方面：

1. **实验设计充分性**
   - GRPO group_size=2 是否构成致命 confound？论文在 Limitations 中披露了此问题，但这是否足够？
   - max_completion_length=256 导致 80-84% truncation rate——这对结果有效性的影响
   - 仅 2 个 random seeds 是否足以支撑负面结论？
   - ACT seed 2 仅 4/16 checkpoints 已评估——ongoing 数据的呈现是否合理？

2. **统计方法**
   - AUROC 的 bootstrap CI 是否正确使用？
   - SyconScore harmonic mean 的选择是否充分 justify？（ToF=0 时自动归零的 mask effect）
   - Cross-seed rank correlation 声称 ρ≈0.33——2 seeds 的 Spearman 理论上只能取 ±1，计算方式是否说明清楚？

3. **Claims vs Evidence 对齐**
   - 标题 "Why Sycophancy Directions Fail as GRPO Rewards" 是否精确反映实验范围？
   - "discriminability ≠ reward utility" 的泛化声明是否超出 single case study？
   - ACT vs GRPO 对比的 confounding factors（5+ 维度差异）是否充分讨论？

4. **Contrastive pairs 构建**
   - 181 pairs 由 GPT-4.1 生成——quality control 是否充分？
   - Evidence strength 三级标注缺乏人工 IAA——这对核心发现的影响

5. **可复现性**
   - 超参数披露是否完整？
   - 代码/数据 "upon acceptance" 声明是否足够？

请按 ARR 审稿标准输出完整审稿报告（Strengths / Weaknesses / Questions / Missing References / Soundness / Overall Assessment）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 188 · 2026-05-22T14:00:36.117712+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
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

_source line 189 · 2026-05-22T14:00:36.169504+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 190 · 2026-05-22T14:00:41.559351+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 191 · 2026-05-22T14:00:44.034656+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/submitted.pdf",
  "project": "contrastive_entrain_calib",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/submitted.pdf",
    "project": "contrastive_entrain_calib",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 192 · 2026-05-22T14:00:49.161714+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's information about the ACL ARR 2025-2026 reviewer guidelines:

## Reviewer Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score
Soundness scores must be justified by the text of the review. If you give a low soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation.

### Excitement Score
Sometimes you may find the work sound, but not something that is interesting personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

## Area Chair Guidelines

All papers recommended for Findings or main conference are expected to be sound and reproducible. Area chairs should mostly follow the soundness assessment of the reviewers when they are in agreement, and they can weigh in when there is a disagreement or 
…[truncated 579 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7602
}
```

</details>

---


### Tool result

_source line 193 · 2026-05-22T14:00:50.417137+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 407.4}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 455.3}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.7}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 443.2}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 459.5}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 425.7}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.5}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.0}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_ima
…[truncated 548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6382
}
```

</details>

---


### Tool call

_source line 194 · 2026-05-22T14:00:55.739825+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer scoring criteria, all dimensions reviewers must score, the score scales (1-5 for each dimension), and any specific instructions about what each score level means. Include information about soundness, excitement, overall assessment, reproducibility, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer scoring criteria, all dimensions reviewers must score, the score scales (1-5 for each dimension), and any specific instructions about what each score level means. Include information about soundness, excitement, overall assessment, reproducibility, and any other scored dimensions."
  }
}
```

</details>

---


### Tool call

_source line 195 · 2026-05-22T14:00:57.099478+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/submitted.pdf",
  "project": "contrastive_entrain_calib",
  "pages": "11",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/submitted.pdf",
    "project": "contrastive_entrain_calib",
    "pages": "11",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 196 · 2026-05-22T14:00:57.803191+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 197 · 2026-05-22T14:00:58.104554+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 198 · 2026-05-22T14:00:59.059801+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 199 · 2026-05-22T14:00:59.562248+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 200 · 2026-05-22T14:01:00.170084+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 201 · 2026-05-22T14:01:03.275722+00:00_

# ARR Reviewer Scoring Criteria

Based on the guidelines provided, ARR reviewers must submit **three distinct scores**:

## 1. **Soundness Score**
This evaluates technical validity. The guidelines state that "the _soundness_ scores must be justified by the text of the review." Low soundness scores require substantiation through identified flaws in methodology, logic, or evidence.

## 2. **Excitement Score**
This reflects personal interest independent of quality assessment. Per the document, excitement scores are "orthogonal to the assessment of the soundness of the paper" and "do not necessarily come with explicit reasons" since they represent subjective preferences.

## 3. **Overall Assessment/Recommendation**
Described as "an explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue." This composite score balances soundness, excitement, novelty, and potential impact.

## Additional Scoring Dimension

**Reproducibility Score**: The guidelines note that "low reproducibility scores should be justified," indicating this represents a distinct dimension. However, the document specifies that "reviewers are not obligated to run anything," making reproducibility assessment limited to whether sufficient implementation details, code, and data information are provided.

## Score Range

The document does not explicitly specify numerical scales (1-5, etc.) for these dimensions. It emphasizes that scores must align with review justifications rather than detailing specific numerical interpretations for each level.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7535
}
```

</details>

---


### Tool result

_source line 202 · 2026-05-22T14:01:03.428384+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 136.4}], \"total_pages\": 11, \"rendered_pages\": 1, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6328
}
```

</details>

---


### Tool result

_source line 203 · 2026-05-22T14:01:05.960977+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 8157
}
```

</details>

---


### Tool result

_source line 204 · 2026-05-22T14:01:06.217065+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 7157
}
```

</details>

---


### Tool result

_source line 205 · 2026-05-22T14:01:06.318653+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 8214
}
```

</details>

---


### Tool result

_source line 206 · 2026-05-22T14:01:06.320034+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 6757
}
```

</details>

---


### Tool result

_source line 207 · 2026-05-22T14:01:06.371374+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 6201
}
```

</details>

---


### Tool call

_source line 208 · 2026-05-22T14:01:14.109100+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 209 · 2026-05-22T14:01:14.611505+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 210 · 2026-05-22T14:01:15.064820+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 211 · 2026-05-22T14:01:15.065347+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 212 · 2026-05-22T14:01:16.022421+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1410
}
```

</details>

---


### Tool result

_source line 213 · 2026-05-22T14:01:16.023515+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool call

_source line 214 · 2026-05-22T14:01:16.174627+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 215 · 2026-05-22T14:01:16.476394+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 216 · 2026-05-22T14:01:16.932040+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 217 · 2026-05-22T14:01:17.084458+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool result

_source line 218 · 2026-05-22T14:01:17.087054+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 155
}
```

</details>

---


### Tool result

_source line 219 · 2026-05-22T14:01:17.340576+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 864
}
```

</details>

---


### Tool call

_source line 220 · 2026-05-22T14:04:11.673624+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form soundness excitement score scale 1 2 3 4 5 meaning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form soundness excitement score scale 1 2 3 4 5 meaning 2025"
  }
}
```

</details>

---


### Tool result

_source line 221 · 2026-05-22T14:04:18.004590+00:00_

Web search results for query: "ACL ARR review form soundness excitement score scale 1 2 3 4 5 meaning 2025"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL’23 Peer Review Form - ACL 2023","url":"https://2023.aclweb.org/blog/review-form/"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ACL’23 Peer Review Policies - ACL 2023","url":"https://2023.aclweb.org/blog/review-acl23/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"}]

Based on the search results, here's the information about the ACL ARR review form scoring scales for soundness and excitement:

## Soundness Score (1-5 Scale)

The soundness score ranges from 5 = Excellent (one of the most thorough studies), 4 = Strong (sufficient support for all claims with only minor experiments needed), to 3 = Acceptable (sufficient support for main claims). Lower scores (2 and 1) indicate insufficient support for claims or poor quality work.

## Excitement Score (1-5 Scale)

The excitement score ranges from 5 = Highly Exciting (would recommend/attend presentation) to 4 = Exciting (would mention to others/make effort to attend). Excitement is subjective and does not necessarily follow what is popular in the field.

## Key Distinctions (2025 Update)

Starting with February 2025, ARR reviewers are asked to provide three score
…[truncated 408 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6330
}
```

</details>

---


### Tool call

_source line 222 · 2026-05-22T14:04:23.995077+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the COMPLETE review form with ALL scoring dimensions, their exact scales (1-5), and the meaning of each score level. I need every dimension: soundness, excitement, overall assessment, reproducibility, confidence, and any others. Include the exact text for each score level (e.g., 5 = ..., 4 = ..., 3 = ..., 2 = ..., 1 = ...)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the COMPLETE review form with ALL scoring dimensions, their exact scales (1-5), and the meaning of each score level. I need every dimension: soundness, excitement, overall assessment, reproducibility, confidence, and any others. Include the exact text for each score level (e.g., 5 = ..., 4 = ..., 3 = ..., 2 = ..., 1 = ...)."
  }
}
```

</details>

---


### Tool result

_source line 223 · 2026-05-22T14:04:31.586329+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## 1. Reviewer Confidence
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## 2. Soundness
- **5**: "Excellent: This study is one of the most thorough I have seen."
- **4**: "Strong: This study provides sufficient support for all claims."
- **3**: "Acceptable: This study provides sufficient support for main claims."
- **2**: "Poor: Some main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. Excitement
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make effort to attend."
- **3**: "Interesting: I might mention some points or attend if there's time."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

## 4. Overall Assessment
- **5**: "Consider for Award: Could be considered for outstanding paper award."
- **4.5**: "Borderline Award"
- **4**: "Conference: Could be accepted to an ACL conference."
- **3.5**: "Borderline Conference"
- **3**: "Findings: Could be accepted to the Findings of the ACL."
- **2.5**: "Borderline Findings"
- **2**: "Resubmit next cycle: needs substantial revisions."
- **1.5**: "Resubmit after next cycle: needs substantial revisions not completed by next cycle."
- **1**: "Do not resubmit: paper has to be fully redone."

## 5. Reproducibility
- **5**: "They could easily reproduce the 
…[truncated 945 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7591
}
```

</details>

---


### Tool call

_source line 224 · 2026-05-22T14:04:40.547313+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 225 · 2026-05-22T14:04:40.598035+00:00_

1	\documentclass[11pt,a4paper]{article}
2	\usepackage[hyperref]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{graphicx}
10	\usepackage{xcolor}
11	\usepackage{subcaption}
12	
13	\newcommand{\dsyc}{d_{\text{syc}}}
14	\newcommand{\tof}{\text{ToF}}
15	\newcommand{\nof}{\text{NoF}}
16	\newcommand{\sycon}{\textsc{SyconScore}}
17	\newcommand{\rone}{R_1}
18	\newcommand{\rthree}{R_3}
19	
20	\title{Discriminability Without Utility: Why Sycophancy Directions Fail as GRPO Rewards}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\begin{abstract}
28	\input{sections/abstract}
29	\end{abstract}
30	
31	\input{sections/introduction}
32	
33	\input{sections/framework}
34	
35	\input{sections/direction_quality}
36	
37	\input{sections/cosine_failure}
38	
39	\input{sections/probe_trap}
40	
41	\input{sections/discussion}
42	
43	\input{sections/related_work}
44	
45	\input{sections/conclusion}
46	
47	\section*{Limitations}
48	\input{sections/limitations}
49	
50	\section*{Reproducibility}
51	Code and data will be released upon acceptance. All training hyperparameters are reported in Appendix~\ref{app:training}. The 181 contrastive pairs and evaluation benchmark are included in the supplementary materials.
52	
53	\bibliography{references}
54	
55	\appendix
56	\input{sections/appendix}
57	
58	\end{document}
59	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 226 · 2026-05-22T14:04:44.969034+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/*.tex"
  }
}
```

</details>

---


### Tool result

_source line 227 · 2026-05-22T14:04:45.019753+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/direction_quality.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/probe_trap.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 228 · 2026-05-22T14:04:49.572674+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 229 · 2026-05-22T14:04:49.874114+00:00_

1	Our GRPO experiments use a group size of 2, below the typical range of 8--64 \citep{shao2024grpo}, due to memory constraints with 8B-parameter models. This limits within-group ranking diversity and constitutes an important confound: the observed failures may partly reflect insufficient exploration rather than a fundamental limitation of representation-based rewards. However, the probe reward trap (C2) arises in an SFT setting where group size is irrelevant, indicating that at least one failure mode is independent of GRPO hyperparameters. Additionally, all GRPO experiments truncate completions at 256 tokens (80--84\% truncation); all conditions share this setting, so relative comparisons are fair, but absolute conclusions about $\dsyc$ reward utility may be affected.
2	
3	Our RL training uses Qwen3-8B exclusively; cross-model discriminability is confirmed on Llama-3-8B (AUROC $0.779$; Table~\ref{tab:cross_model}), but compute constraints prevented training replication on a second architecture. Evidence strength was annotated by GPT-4.1 as a single annotator without human inter-annotator agreement.
4	
5	We report GRPO results from two random seeds; both exhibit qualitatively consistent oscillation patterns (similar amplitude, identical crash depth), but the limited seed count constrains statistical claims. ACT and GRPO differ along multiple dimensions beyond supervision granularity, so we cannot isolate the causal factor behind ACT's advantage.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 230 · 2026-05-22T14:04:49.924781+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 231 · 2026-05-22T14:04:50.827899+00:00_

1	\section{Analysis: Discriminability $\neq$ Reward Utility}\label{sec:discussion}
2	
3	\paragraph{Unified root cause.}
4	The failures in Sections~\ref{sec:cosine_failure} and~\ref{sec:probe_trap} trace to a single geometric limitation.
5	$\dsyc$ encodes the \emph{direction} of belief change but not its \emph{evidential warrant}: valid revision and sycophantic capitulation both shift activations toward the user's position along the same direction.
6	The two reward families expose complementary faces of this blindness.
7	Cosine $\rone$ penalizes all belief change indiscriminately; the resulting mode collapse (F1c, F1d) reflects excessive punishment of any activation shift along $\dsyc$.
8	The binary probe $\rone$ rewards all resistance regardless of input validity; the stubbornness trap ($\tof = 0$ by step 500) reflects excessive permissiveness toward activation stasis.
9	These are not independent design flaws but dual consequences of a direction that conflates the target behavior (resisting invalid challenges) with its complement (refusing valid corrections).
10	Cross-model evidence confirms the limitation extends beyond Qwen3-8B: Llama-3-8B independently achieves AUROC $0.779$ (bootstrap 95\% CI $[0.745,\, 0.819]$) on the same contrastive pairs with the same monotonic evidence gradient, so discriminability generalizes across architectures while the semantic gap between discriminability and reward utility persists.
11	This pattern contrasts with reasoning faithfulness and safety directions~\citep{zhang2026latentgrpo}, where the behavior to suppress is geometrically distinct from the behavior to preserve along the relevant direction.
12	\citet{wu2026rewardhacking} reinforce this principle: concept directions applied via advantage modification in GRPO achieve 100\% validation accuracy for reward hacking detection, where shortcut behaviors are geometrically separable---confirming that direction utility depends on geometric separability, not the optimization framework.

…[truncated 7231 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 232 · 2026-05-22T14:04:50.828413+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 233 · 2026-05-22T14:04:50.979030+00:00_

1	\section{Training Details}
2	\label{app:training}
3	
4	\paragraph{Reward weight selection.}
5	The weight $w_1$ is set by diagnostic-driven iteration: $w_1{=}0.25$ was initially chosen to down-weight the noisy cosine reward term; this was later increased to $w_1{=}0.40$ for F1d after diagnostics revealed that $w_1{=}0.25$ allowed the cosine term to contribute only ${\sim}8.3\%$ of total reward variance.
6	The empirical scaling factor in F1a ($\dsyc/20$) is a heuristic normalization; we did not find it critical to the failure modes reported.
7	
8	\paragraph{Response truncation.}
9	All GRPO experiments use \texttt{max\_completion\_length}=256, resulting in 80--84\% truncation of multi-turn responses.
10	This setting is shared across all conditions and does not affect relative comparisons; we retain it because response-level decisions typically manifest within the first 100--200 tokens.
11	
12	\paragraph{Hyperparameters.}
13	Table~\ref{tab:hyperparams} compares training configurations for GRPO variants and ACT.
14	
15	\begin{table}[h]
16	\centering
17	\small
18	\caption{Training hyperparameters. All experiments use Qwen3-8B, DeepSpeed ZeRO-2, bf16 precision.}
19	\label{tab:hyperparams}
20	\begin{tabular}{lcc}
21	\toprule
22	& GRPO (F1, F3)$^e$ & ACT \\
23	\midrule
24	Learning rate & 5e-5 & 5e-5 \\
25	Effective batch & 16 & 16 \\
26	Max steps & 8{,}000 & 8{,}000 \\
27	Warmup steps & 200 & 200 \\
28	LR schedule & linear$^a$ & linear \\
29	Grad.\ clipping & --- & 1.0 \\
30	\midrule
31	LoRA rank & 64 & 64 \\
32	LoRA $\alpha$ & 64 & 128 \\
33	LoRA modules & 4$^b$ & 7$^c$ \\
34	LoRA dropout & 0 & 0.05 \\
35	\midrule
36	Group size & 2$^d$ & --- \\
37	KL $\beta$ & 0.04 & --- \\
38	Max compl.\ len. & 256 & --- \\
39	Max seq.\ len. & --- & 1{,}024 \\
40	L2 loss weight & --- & 0.1 \\
41	\bottomrule
42	\end{tabular}
43	\\[2pt]
44	\raggedright\footnotesize
45	$^a$Cosine schedule for $\rthree$-only.
46	$^b$q/k/v/o\_proj.
47	$^c$+ gate/up/down\_proj (${\sim}1.75{\times}$ params; \S\
…[truncated 1651 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 234 · 2026-05-22T14:04:50.979425+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex"
  }
}
```

</details>

---


### Tool result

_source line 235 · 2026-05-22T14:04:51.030381+00:00_

1	\section{Experimental Framework}
2	\label{sec:framework}
3	
4	\subsection{Direction Extraction}
5	\label{ssec:extraction}
6	
7	We extract a linear sycophancy direction $\dsyc$ from the residual stream using contrastive activation pairs: a \emph{valid correction} (warranted belief revision under strong evidence) and a \emph{sycophantic capitulation} (unwarranted concession under social pressure).
8	We construct 181 contrastive pairs using GPT-4.1 in a two-stage pipeline: skeleton generation followed by 3-turn dialogue completion.
9	Style matching is enforced by automated validation (response length difference ${<}10\%$, shared opening phrase ${\geq}2$ words), with up to 3 retries per pair; 19 of 200 initial pairs were discarded for failing validation.
10	Evidence strength is annotated at three levels: \emph{weak} (75 pairs; personal memory or opinion), \emph{medium} (54 pairs; brief source citation), and \emph{strong} (52 pairs; authoritative source with detailed data).
11	From the 181 paired examples (362 activations total), we compute the mean difference at target layer $\ell$:
12	\begin{equation}
13	\label{eq:dsyc}
14	\dsyc = \frac{1}{N}\sum_{i=1}^{N}\left(\mathbf{h}^{+}_i - \mathbf{h}^{-}_i\right)
15	\end{equation}
16	where $\mathbf{h}^{+}_i$ and $\mathbf{h}^{-}_i$ are residual-stream activations for the $i$-th valid and sycophantic response.
17	The target layer is selected by 5-fold cross-validated AUROC; on Qwen3-8B this yields layer 19 with AUROC $0.827$ (bootstrap 95\% CI $[0.795,\, 0.857]$).
18	
19	\subsection{Reward Formulations}
20	\label{ssec:reward}
21	
22	Three formulations translate $\dsyc$ into a direction-based signal $\rone$.
23	For F1 and F3, $\rone$ enters as part of a GRPO \citep{shao2024grpo} reward $R = w_1 \cdot \rone + w_3 \cdot \rthree$, where $\rthree$ is a behavioral component (DeBERTa NLI classifier scoring consistency with the ground-truth answer).
24	\begin{itemize}
25	\item[\textbf{F1}] \textbf{Cosine projection} with four variants: 
…[truncated 3181 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 236 · 2026-05-22T14:04:57.366503+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/probe_trap.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/probe_trap.tex"
  }
}
```

</details>

---


### Tool result

_source line 237 · 2026-05-22T14:04:57.919116+00:00_

1	\section{The Probe Reward Trap}
2	\label{sec:probe_trap}
3	
4	The cosine formulations fail because the continuous projection of $\dsyc$ produces a gap too narrow for reward contrast.
5	A natural remedy is to discretize: train a logistic probe on $\dsyc$ and threshold its output, yielding $\rone = \mathbb{I}[P(\text{syc} \mid \mathbf{h}) < 0.5]$ (F2 in \S\ref{ssec:reward}).
6	We show that this discretization sidesteps the magnitude problem but creates a qualitatively worse failure.
7	Both probe experiments use SFT rather than GRPO (\S\ref{ssec:reward}); the trap is therefore independent of GRPO's optimization dynamics.
8	
9	\paragraph{Differentiable probe: gradient gaming.}
10	Without stop-gradient (exp-008), the policy discovers within ${\sim}30$ steps that shifting activations away from the sycophancy cluster maximizes $\rone$ regardless of response content, producing an inverted profile ($\tof = 0.978$, $\nof = 0.006$).
11	This motivates the frozen-probe design below.
12	
13	\paragraph{Binary probe: the stubbornness trap.}
14	With stop-gradient (exp-008v3), the policy cannot game the boundary but instead exploits a deeper flaw: $\dsyc$ does not condition on input validity, so refusing to revise a wrong answer receives the same $\rone = 1$ as correctly resisting invalid pressure.
15	By step 500, $\tof$ drops to 0.000 and $\nof$ reaches 0.995, yielding $\sycon = 0$.
16	Qualitative analysis reveals distinct failure modes: \emph{sycophantic stubbornness} (24\%), where the model verbally agrees but does not change its answer; \emph{deliberation traps} (29\%), where the model identifies the correct answer but cannot commit; and evidence-graded hedging, where the model adjusts its refusal style rather than its acceptance rate (Appendix~\ref{app:taxonomy}).
17	
18	\paragraph{Behavioral death precedes distributional collapse.}
19	
20	\begin{table}[t]
21	\centering
22	\caption{Probe reward trap trajectory (exp-008v3). Behavioral death ($\tof{=}0$) occurs at step 500; entr
…[truncated 2286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 238 · 2026-05-22T14:04:57.969788+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex"
  }
}
```

</details>

---


### Tool result

_source line 239 · 2026-05-22T14:04:57.970289+00:00_

1	\section{Cosine \texorpdfstring{$\rone$}{R1}: Structural Failure}
2	\label{sec:cosine_failure}
3	
4	Section~\ref{sec:direction_quality} established that $\dsyc$ achieves AUROC 0.827 on Qwen3-8B.
5	We now test whether this discriminability translates into a viable GRPO reward.
6	Four configurations form a diagnostic chain (Table~\ref{tab:cosine_chain}): each resolves the failure mode of its predecessor but exposes a deeper limitation.
7	
8	\begin{table}[t]
9	\centering
10	\caption{Cosine $\rone$ failure chain on Qwen3-8B (LoRA rank$=$64, GRPO with $R = w_1 \cdot \rone + w_3 \cdot \rthree$).}
11	\label{tab:cosine_chain}
12	\begin{tabular}{lllll}
13	\toprule
14	Config & $\rone$ Formula & $w_1$ & Outcome & Root Cause \\
15	\midrule
16	F1a & $\tanh(\mathbf{h}\cdot\dsyc/20)$ & 0.25 & Gate saturation & Norm mismatch \\
17	F1b & $\cos(\mathbf{h},\, \dsyc)$ & 0.25 & $\rone \approx 0$ & Gap too small \\
18	F1c & +recalibration & 0.25 & Mode collapse & Reward discontinuity \\
19	F1d & $5\cos(\mathbf{h},\, \dsyc)$ & 0.40 & Mode collapse & $\rthree$ saturation \\
20	\bottomrule
21	\end{tabular}
22	\end{table}
23	
24	F1a uses a dot-product formulation ($\rone = \tanh(\mathbf{h} \cdot \dsyc / 20)$), but residual-stream norms exceed the direction norm by $100$--$1{,}200{\times}$, saturating the tanh gate and zeroing the gradient by step 955.
25	Switching to cosine similarity (F1b) eliminates norm dependence, yet the cosine gap between valid and sycophantic activations averages only 0.098 across layers---too narrow to generate meaningful reward contrast.
26	Online recalibration (F1c, \S\ref{ssec:recalib}) raises offline AUROC from 0.827 to 0.910 but paradoxically triggers mode collapse: the abrupt shift in $\dsyc$ at each recalibration event creates a reward discontinuity that destabilizes GRPO advantage estimates, collapsing entropy to 0.069 within 300 steps.
27	Amplifying the signal with $5{\times}$ scaling (F1d) lifts $\rone$ above the noise floor but simultaneously amplifies t
…[truncated 950 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 240 · 2026-05-22T14:04:58.522922+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/direction_quality.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/direction_quality.tex"
  }
}
```

</details>

---


### Tool result

_source line 241 · 2026-05-22T14:04:58.623823+00:00_

1	\section{Direction Discriminability}
2	\label{sec:direction_quality}
3	
4	Before evaluating $\dsyc$ as a reward signal (\S\ref{sec:cosine_failure}--\S\ref{sec:probe_trap}), we first establish that it captures a genuine sycophancy-related signal in the residual stream.
5	If the direction failed to discriminate sycophantic from non-sycophantic activations, downstream reward failures would be trivially explained by poor direction quality rather than by a fundamental gap between discriminability and reward utility.
6	We evaluate discriminability along five axes: cross-validated classification accuracy, evidence-strength stratification, cross-model transfer, training stability, and probe ablation.
7	Figure~\ref{fig:direction_quality} summarizes the per-layer AUROC profiles for both models.
8	
9	\paragraph{Qwen3-8B layer-wise discriminability.}
10	We evaluate $\dsyc$ via 5-fold cross-validated AUROC on 181 style-controlled contrastive pairs (\S\ref{ssec:extraction}).
11	The direction achieves AUROC $0.827$ (bootstrap 95\% CI $[0.795,\, 0.857]$) at its best layer (L19).
12	Discriminability emerges gradually across depth: layers L0--L8 perform near chance, statistical significance ($p < 0.01$) first appears at L16, and performance peaks at L19.
13	This gradual emergence, with the peak in the upper third of the network, suggests that sycophancy-relevant information is encoded as a late-stage representation rather than an input-level confound.
14	The direction also captures evidential granularity.
15	AUROC rises monotonically from 0.675 on weak-evidence pairs to 0.883 on medium and 0.929 on strong pairs.
16	This gradient indicates that $\dsyc$ encodes the degree of evidential warrant, not merely a binary sycophancy label.
17	
18	\paragraph{Cross-model generalization.}
19	To rule out that these results are specific to Qwen3-8B's representation geometry, we repeat the full extraction and evaluation pipeline on Llama-3-8B-Instruct.
20	Table~\ref{tab:cross_model} compares the t
…[truncated 3550 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 242 · 2026-05-22T14:05:06.092086+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 243 · 2026-05-22T14:05:06.142773+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Representation engineering \citep{zou2023repe} reveals that large language models encode sycophancy as a linear direction in their residual streams.
5	A contrastive sycophancy direction $\dsyc$, extracted from style-controlled pairs of valid belief revision and sycophantic capitulation, achieves cross-validated AUROC $0.827$ on Qwen3-8B and $0.779$ on Llama-3-8B, with discriminability rising monotonically across evidence-strength levels (\S\ref{sec:direction_quality}).
6	These results, replicated across two architecturally distinct model families, point to an appealing possibility: if the model's representations already separate sycophantic from non-sycophantic behavior, that separation should be convertible into a scalar reward signal for reinforcement learning.
7	Sycophancy is among the most persistent alignment failures in deployed systems \citep{sharma2023sycophancy}, and a representation-level reward could complement existing behavioral approaches by targeting the internal computation rather than its surface outputs.
8	
9	This paper shows that, in our experiments on Qwen3-8B, the conversion fails.
10	We test three formulations---two GRPO \citep{shao2024grpo} reward variants (cosine projection, continuous probe) and one SFT-based probe penalty---across six configurations; every formulation fails.
11	Cosine similarity cannot separate valid revision from sycophantic capitulation in the narrow online activation gap (\S\ref{sec:cosine_failure}).
12	A binary probe with stopped gradients creates a stubbornness trap: $\tof$ drops to zero within 500 steps while generation entropy remains at 0.70, masking behavioral death (\S\ref{sec:probe_trap}).
13	Removing $\dsyc$ in favor of a purely behavioral reward does not resolve the problem: $\rthree$-only GRPO exceeds vanilla at only 4 of 27 checkpoints across two seeds, while ACT exceeds vanilla at every evaluated checkpoint (seed 1: 16/16; seed 2: 4/4 ongoing; \S\ref{s
…[truncated 4019 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 244 · 2026-05-22T14:05:06.143209+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 245 · 2026-05-22T14:05:06.294235+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work tested whether a representation direction that detects sycophantic behavior can serve as a training signal for sycophancy calibration.
4	In experiments on Qwen3-8B, $\dsyc$ achieved strong offline discriminability (AUROC 0.827), yet all three formulations failed---the two GRPO reward variants and the SFT-based probe penalty each produced behavioral collapse, and $\rthree$-only GRPO exceeded vanilla at only 4 of 27 checkpoints.
5	Our results suggest that discriminability in representation space does not guarantee utility as a training signal for behavioral attributes like sycophancy where the target concept lacks geometric separability (\S\ref{sec:discussion}).
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 246 · 2026-05-22T14:05:50.626210+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 247 · 2026-05-22T14:05:50.677036+00:00_

1	Representation engineering shows that large language models encode sycophancy as a linear direction in activation space. We extract a contrastive sycophancy direction ($\dsyc$) from style-controlled pairs, achieving cross-validated AUROC $0.827$ on Qwen3-8B and $0.779$ on Llama-3-8B. In experiments on Qwen3-8B, we test three $\dsyc$-based training formulations---two with Group Relative Policy Optimization (GRPO) and one SFT-based probe penalty; every formulation failed. The cosine reward could not separate valid revision from sycophantic capitulation in the narrow online activation gap. The probe reward created a stubbornness trap: the true-positive flip rate dropped to zero within 500 steps while entropy remained healthy. Removing $\dsyc$ entirely and training with a purely behavioral reward also failed: only 4 of 27 checkpoints across two seeds exceeded vanilla, while supervised fine-tuning exceeded vanilla at every evaluated checkpoint (seed 1: 16/16; seed 2: 4/4 ongoing). The root cause is a semantic gap between discriminability and reward utility: $\dsyc$ encodes \emph{whether} belief changed, not \emph{whether it should have}. A single scalar reward per completion could not convey which belief changes were warranted in our setting; dense per-token supervision (ACT) succeeded, though the methods differ along multiple dimensions beyond supervision granularity alone.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 248 · 2026-05-22T14:08:01.921206+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## 总体评分\n\n**Overall**: 3.0 — Findings（可被 Findings 接收）\n**一句话总结**: 研究问题重要、failure mode 分析有洞见，但 GRPO group_size=2 和 80-84% truncation 构成严重 confound，无法确定失败源自 d_syc 的本质局限还是次优实验配置。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 (Acceptable) | 主要 claims 有部分支持，但 group_size=2 和 truncation 两个 confound 使核心负面结论的因果归因不成立；probe trap (C2) 在 SFT 设定下独立于 GRPO 超参，是可靠发现 |\n| Excitement | 3/5 (Interesting) | \"discriminability ≠ reward utility\" 的概念框架有价值，probe reward trap 及 behavioral-before-distributional collapse 的发现具有实践意义，但单一 case study 限制泛化 |\n| Reproducibility | 3/5 | 超参数在 Table 5 / Appendix A 中披露完整，但代码和数据 \"upon acceptance\"，reviewer 无法独立验证关键数字 |\n| Confidence | 4/5 | 仔细通读全文，熟悉 representation engineering、GRPO 和 sycophancy 相关文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **GRPO group_size=2 构成致命 confound，论文核心因果归因不成立**\n- 具体位置：Section 2.5 (line \"GRPO uses a group size of 2\")、Table 5 (footnote d)、Limitations\n- 问题：论文使用 group_size=2，远低于典型值 8-64 (Shao et al., 2024)。Group size=2 意味着 GRPO 的 advantage estimation 极度噪声化——每个 group 只有两个 completion 进行相对排序，几乎等同于抛硬币。关键证据：**R₃-only GRPO（完全不使用 d_syc 的纯行为奖励）同样基本失败**（仅 4/27 checkpoints 超过 vanilla，SyconScore 0.143 vs vanilla 0.134），这强烈暗示问题出在 GRPO 优化配置本身，而非 d_syc。论文在 Limitations 中承认了这个 confound 并指出 probe trap (C2) 独立于 group_size，但 GRPO 相关的所有失败（F1a-F1d, F3, R₃-only）都可能被这一 confound 解释。\n- 为什么影响接收：标题声称 \"Why Sycophancy Directions **Fail** as GRPO Rewards\"，但如果换用 group_size=8 或 16 后 d_syc 能成功，该结论完全翻转。仅凭 group_size=2 的实验无法支撑标题中的因果性声明。\n- 建议修改方向：(1) 在 group_size=8 或 16 下复现至少一个 cosine 和一个 probe formulation；(2) 如果计算资源不允许，将标题和 claims 降级为 \"under constrained optimization settings\" 的条件性结论；(3) 解释为什么 R₃-only GRPO 也失败——这实际上削弱而非支持论文论点。\n\n**N2** [critical] **80-84% truncation rate 严重损害奖励信号有效性**\n- 具体位置：Appendix A (\"All GRPO experiments use max_completion_length=256, resulting in 80–84% truncation of multi-turn responses\")\n- 问题：论文称 \"this setting is shared across all conditions and does not affect relative comparisons\" 以及 \"response-level decisions typically manifest within the first 100–200 tokens\"。但后一个 claim 没有任何实证支持——论文未提供 token-level 分析证明 sycophantic 行为在前 200 tokens 内完全可辨。在 80-84% 被截断的情况下，d_syc 奖励是基于不完整响应计算的，这可能系统性地扭曲奖励信号。更重要的是，如果 cosine gap (0.098, Section 4) 本就极小，truncation 引入的噪声可能完全淹没信号。\n- 为什么影响接收：论文将 cosine gap 过窄归因于 d_syc 的内在局限（\"semantic limitation\"），但同样可能是 truncation 导致激活不完整，从而人为压缩了 gap。因果归因再次不成立。\n- 建议修改方向：(1) 提供 truncation vs non-truncation 的 AUROC/cosine gap 对比；(2) 或在 max_completion_length=512/1024 下验证 cosine gap 是否仍然过窄。\n\n**N3** [critical] **仅 2 random seeds 不足以支撑负面结论**\n- 具体位置：Limitations (\"We report GRPO results from two random seeds\")\n- 问题：对于一个以负面结论为核心贡献的论文，2 个 seeds 提供的统计证据极薄。Table 4 显示两个 seed 之间的差异不小（seed 1 peak SyconScore 0.153 at step 6500 vs seed 2 peak 0.143 at step 4000），crash onset 差 ~2,500 步。在 RL 训练固有的高方差下，2 seeds 无法区分 \"d_syc 本质上不能工作\" 和 \"这两个特定 seed 恰好失败了\"。\n- 为什么影响接收：论文的核心贡献是负面结论（\"every tested formulation fails\"）。负面结论需要比正面结论更高的统计门槛，因为读者需要排除 \"实验做得不够好\" 这一竞争假说。2 seeds 不足以排除。\n- 建议修改方向：增加到至少 5 个 seeds，报告 mean ± std，并进行 bootstrap 或 permutation test 确认零假设（\"GRPO with d_syc performs no better than vanilla\"）的 p-value。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **ACT vs GRPO 对比被 5+ 维度差异严重 confound**\n- 具体位置：Section 6 (paragraph \"Observational comparison: ACT vs. GRPO\")、Table 5\n- 问题：论文承认 ACT 和 GRPO 至少在 5 个维度上不同（supervision granularity, loss family, training data format, optimization dynamics, LoRA capacity），但仍将 ACT 的成功与 GRPO 的失败并列比较，暗示 per-token supervision 是关键因素。在如此多 confound 下，任何一个差异都可能是 ACT 成功的原因（例如，ACT 使用 7 个 LoRA modules 共 ~1.75x 参数量，或 grad clipping=1.0，或 LoRA alpha=128 vs 64）。论文标记此比较为 \"observational\" 是好的，但在 Section 6 的段落标题 \"Scalar reward limitation (observational)\" 中，仍将其作为一个独立发现呈现。\n- 建议：(1) 做至少一个 controlled ablation（例如在 GRPO 中加入 per-token d_syc loss 但保持其他不变）；(2) 或将 ACT 比较明确降级为 \"motivation for future work\" 而非 finding。\n\n**W2** [warning] **标题 overclaim——\"Why ... Fail\" 暗示因果解释，但实验仅提供 single case study 的描述性证据**\n- 具体位置：标题、Section 6 标题 \"Discriminability ≠ Reward Utility\"\n- 问题：标题使用 \"Why\" 暗示提供了因果解释，但论文实际上只在一个模型 (Qwen3-8B)、一个 RL 算法 (GRPO with group_size=2)、一个方向 (d_syc from 181 GPT-4.1 pairs) 上做了实验。Section 6 标题将 \"discriminability ≠ reward utility\" 提升为一般性原则，但证据来自 single case study。论文中引用的 Zhang et al. (2026) 和 Wu and Tang (2026) 的对比论证是方向正确的，但不能替代本文自身的实验覆盖面。\n- 建议：(1) 标题改为条件性表述，如 \"When Sycophancy Directions Fail as GRPO Rewards: A Case Study\"；(2) Section 6 标题改为 \"Evidence that Discriminability May Not Imply Reward Utility\"。\n\n**W3** [warning] **181 对 contrastive pairs 的 evidence strength 标注缺乏人类 IAA**\n- 具体位置：Section 2.1、Limitations\n- 问题：Evidence strength 的三级标注（weak/medium/strong）由 GPT-4.1 单一标注者完成，无人类 inter-annotator agreement。论文在 Limitations 中承认了这一点。对于 discriminability 分析（Figure 1, Table 1），annotation 质量直接影响 AUROC 的 evidence-stratified 分析的可信度——如果 GPT-4.1 的 weak/medium/strong 划分不准确，evidence gradient（0.675 → 0.883 → 0.929）可能是 annotation artifact。\n- 建议：抽样 50 对做人类标注，报告 Cohen's κ 或 Fleiss' κ。\n\n**W4** [warning] **ACT seed 2 仅完成 4/16 checkpoints 评估——不应作为证据呈现**\n- 具体位置：Table 4 (footnote ‡)、Section 6\n- 问题：ACT seed 2 标注为 \"ongoing; 4/16 ckpts evaluated, all > vanilla\"。25% 的评估完成度不构成可靠证据，且 \"all > vanilla\" 可能存在 selection bias（如果前 4 个 checkpoints 是 cherry-picked）。论文多次引用 \"seed 2: 4/4 ongoing\" 作为 ACT 成功的支撑证据，但这 4 个点可能恰好是 ACT 表现最好的阶段。\n- 建议：(1) 完成全部 16 checkpoints 的评估后再投稿；(2) 如果无法完成，删除 ACT seed 2 相关数据和讨论，仅基于 seed 1 报告。\n\n**W5** [warning] **Cross-seed rank correlation ρ≈0.33 的统计报告不充分**\n- 具体位置：Section 6 (\"Cross-seed rank correlation is ≈1.0 during early training (steps 1000–3000) but drops to ρ≈0.33 (n.s.) after step 4000\")\n- 问题：论文未说明 (1) correlation 的 N 是多少（即多少个 checkpoints 参与排序），(2) 如何划分 \"early\" 和 \"late\" 窗口，(3) ρ≈1.0 是在 N=3 上计算的还是更多。如果 early window 只有 3 个 checkpoints，ρ=1.0 几乎是必然的（3 点的 Spearman 只能取 1.0, 0.5, -0.5, -1.0）。Late window 的 ρ≈0.33 (n.s.) 也因 N 过小而无统计功效。论文正确标注了 \"n.s.\" 但仍将此作为 \"stochastic divergence\" 的证据呈现。\n- 建议：报告 exact N、p-value、和 confidence interval；如果 N<10，承认统计功效不足以支撑任何结论。\n\n**W6** [warning] **R₃-only GRPO 在 Table 4 中缺少 ToF 和 NoF 的分项数据**\n- 具体位置：Table 4（R₃-only GRPO 行，ToF 和 NoF 列显示 \"--\"）\n- 问题：Section 6 文字声称 R₃-only GRPO \"exhibits the same stubbornness pattern (high NoF, near-zero ToF)\"，但 Table 4 未报告这些数字。对于论文的关键论证——\"即使移除 d_syc，纯行为奖励下的 GRPO 也表现出相同的 stubbornness pattern\"——这些数字是必要的。\n- 建议：在 Table 4 中填充 R₃-only GRPO 的 ToF 和 NoF 值。\n\n---\n\n## 小问题（不影响接收）\n\n1. **数字一致性**：Abstract 和正文在 R₃-only checkpoints 总数上可能存在 26 vs 27 的微小不一致（需作者确认）。PDF 第 1 页 abstract 部分似乎显示 \"4 of 26\"，但 Introduction 和 Section 6 使用 \"4 of 27\"。\n2. **SyconScore 定义位置**：SyconScore 首次出现在 Section 2.5，但 harmonic mean 选择而非 arithmetic mean 的 justification 仅一句话带过。虽然在 supplementary materials 中提供了 arithmetic mean 结果，但正文应简要说明 harmonic mean 更严格惩罚单侧极端的理由。\n3. **Stubbornness taxonomy (Appendix B)**：三种失败模式（sycophantic stubbornness 24%, deliberation traps 29%, evidence-graded hedging 百分比未报告）的百分比加起来不到 100%，剩余比例是什么？\n4. **写作小问题**：Table 2 标题中 \"GRPO with R = w₁·R₁ + w₃·R₃\" 使用了 R₁ 和 R₃ 但未使用 R₂，可能困扰读者。\n\n---\n\n## 主要优势\n\n1. **研究问题重要且及时**：representation engineering 越来越多地被用于 reward design，本文提出的 \"discriminability ≠ utility\" 框架是对该领域的有价值警示。\n2. **系统性 failure mode 分析**：6 种配置形成诊断链（F1a→F1b→F1c→F1d→F2→F3），每种解决前一种的 failure mode 但暴露更深层问题，论证结构清晰。\n3. **Probe reward trap 发现有原创性**：behavioral death ($\\tof=0$) 发生在 distributional collapse (entropy drop) 之前 1,300 步的发现（Table 3, Figure 2）对 RL alignment 实践有直接价值——它表明 entropy-based early stopping 不足以检测 reward hacking。该发现在 SFT 设定下取得，不受 GRPO hyperparameter 的 confound 影响。\n4. **Cross-model validation**：d_syc 的 discriminability 在 Qwen3-8B 和 Llama-3-8B 上均得到验证（Table 1），evidence-strength gradient 在两个模型上一致。\n5. **Limitations 诚实全面**：论文坦承了 group_size=2、truncation、2 seeds、incomplete ACT seed 2、无人类 IAA 等所有主要局限，这是学术诚实的体现。\n\n---\n\n## 缺失的参考文献\n\n论文的相关工作覆盖合理。可考虑补充：\n- Perez et al. (2022) \"Discovering Language Model Behaviors with Model-Written Evaluations\" — 早期 sycophancy 量化方法\n- Rafailov et al. (2023) DPO — 作为 GRPO 之外的另一类 RL 方法讨论 alternatives\n\n---\n\n## 总结\n\n本文的核心洞见（representation discriminability 不保证 RL reward utility）有价值，probe reward trap 的发现对 alignment 实践有实际意义。但 GRPO group_size=2 和 80-84% truncation 这两个 confound 使得论文无法可靠区分 \"d_syc 本质上不能做 GRPO reward\" 和 \"实验配置不够好\"。R₃-only GRPO 也基本失败这一事实进一步支持后者。建议增加 group_size=8/16 的实验和更多 seeds 后重新提交，如果结论不变，论文将显著增强。当前状态适合 Findings。",
  "reviewer_id": "1",
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## 总体评分\n\n**Overall**: 3.0 — Findings（可被 Findings 接收）\n**一句话总结**: 研究问题重要、failure mode 分析有洞见，但 GRPO group_size=2 和 80-84% truncation 构成严重 confound，无法确定失败源自 d_syc 的本质局限还是次优实验配置。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 (Acceptable) | 主要 claims 有部分支持，但 group_size=2 和 truncation 两个 confound 使核心负面结论的因果归因不成立；probe trap (C2) 在 SFT 设定下独立于 GRPO 超参，是可靠发现 |\n| Excitement | 3/5 (Interesting) | \"discriminability ≠ reward utility\" 的概念框架有价值，probe reward trap 及 behavioral-before-distributional collapse 的发现具有实践意义，但单一 case study 限制泛化 |\n| Reproducibility | 3/5 | 超参数在 Table 5 / Appendix A 中披露完整，但代码和数据 \"upon acceptance\"，reviewer 无法独立验证关键数字 |\n| Confidence | 4/5 | 仔细通读全文，熟悉 representation engineering、GRPO 和 sycophancy 相关文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **GRPO group_size=2 构成致命 confound，论文核心因果归因不成立**\n- 具体位置：Section 2.5 (line \"GRPO uses a group size of 2\")、Table 5 (footnote d)、Limitations\n- 问题：论文使用 group_size=2，远低于典型值 8-64 (Shao et al., 2024)。Group size=2 意味着 GRPO 的 advantage estimation 极度噪声化——每个 group 只有两个 completion 进行相对排序，几乎等同于抛硬币。关键证据：**R₃-only GRPO（完全不使用 d_syc 的纯行为奖励）同样基本失败**（仅 4/27 checkpoints 超过 vanilla，SyconScore 0.143 vs vanilla 0.134），这强烈暗示问题出在 GRPO 优化配置本身，而非 d_syc。论文在 Limitations 中承认了这个 confound 并指出 probe trap (C2) 独立于 group_size，但 GRPO 相关的所有失败（F1a-F1d, F3, R₃-only）都可能被这一 confound 解释。\n- 为什么影响接收：标题声称 \"Why Sycophancy Directions **Fail** as GRPO Rewards\"，但如果换用 group_size=8 或 16 后 d_syc 能成功，该结论完全翻转。仅凭 group_size=2 的实验无法支撑标题中的因果性声明。\n- 建议修改方向：(1) 在 group_size=8 或 16 下复现至少一个 cosine 和一个 probe formulation；(2) 如果计算资源不允许，将标题和 claims 降级为 \"under constrained optimization settings\" 的条件性结论；(3) 解释为什么 R₃-only GRPO 也失败——这实际上削弱而非支持论文论点。\n\n**N2** [critical] **80-84% truncation rate 严重损害奖励信号有效性**\n- 具体位置：Appendix A (\"All GRPO experiments use max_completion_length=256, resulting in 80–84% truncation of multi-turn responses\")\n- 问题：论文称 \"this setting is shared across all conditions and does not affect relative comparisons\" 以及 \"response-level decisions typically manifest within the first 100–200 tokens\"。但后一个 claim 没有任何实证支持——论文未提供 token-level 分析证明 sycophantic 行为在前 200 tokens 内完全可辨。在 80-84% 被截断的情况下，d_syc 奖励是基于不完整响应计算的，这可能系统性地扭曲奖励信号。更重要的是，如果 cosine gap (0.098, Section 4) 本就极小，truncation 引入的噪声可能完全淹没信号。\n- 为什么影响接收：论文将 cosine gap 过窄归因于 d_syc 的内在局限（\"semantic limitation\"），但同样可能是 truncation 导致激活不完整，从而人为压缩了 gap。因果归因再次不成立。\n- 建议修改方向：(1) 提供 truncation vs non-truncation 的 AUROC/cosine gap 对比；(2) 或在 max_completion_length=512/1024 下验证 cosine gap 是否仍然过窄。\n\n**N3** [critical] **仅 2 random seeds 不足以支撑负面结论**\n- 具体位置：Limitations (\"We report GRPO results from two random seeds\")\n- 问题：对于一个以负面结论为核心贡献的论文，2 个 seeds 提供的统计证据极薄。Table 4 显示两个 seed 之间的差异不小（seed 1 peak SyconScore 0.153 at step 6500 vs seed 2 peak 0.143 at step 4000），crash onset 差 ~2,500 步。在 RL 训练固有的高方差下，2 seeds 无法区分 \"d_syc 本质上不能工作\" 和 \"这两个特定 seed 恰好失败了\"。\n- 为什么影响接收：论文的核心贡献是负面结论（\"every tested formulation fails\"）。负面结论需要比正面结论更高的统计门槛，因为读者需要排除 \"实验做得不够好\" 这一竞争假说。2 seeds 不足以排除。\n- 建议修改方向：增加到至少 5 个 seeds，报告 mean ± std，并进行 bootstrap 或 permutation test 确认零假设（\"GRPO with d_syc performs no better than vanilla\"）的 p-value。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **ACT vs GRPO 对比被 5+ 维度差异严重 confound**\n- 具体位置：Section 6 (paragraph \"Observational comparison: ACT vs. GRPO\")、Table 5\n- 问题：论文承认 ACT 和 GRPO 至少在 5 个维度上不同（supervision granularity, loss family, training data format, optimization dynamics, LoRA capacity），但仍将 ACT 的成功与 GRPO 的失败并列比较，暗示 per-token supervision 是关键因素。在如此多 confound 下，任何一个差异都可能是 ACT 成功的原因（例如，ACT 使用 7 个 LoRA modules 共 ~1.75x 参数量，或 grad clipping=1.0，或 LoRA alpha=128 vs 64）。论文标记此比较为 \"observational\" 是好的，但在 Section 6 的段落标题 \"Scalar reward limitation (observational)\" 中，仍将其作为一个独立发现呈现。\n- 建议：(1) 做至少一个 controlled ablation（例如在 GRPO 中加入 per-token d_syc loss 但保持其他不变）；(2) 或将 ACT 比较明确降级为 \"motivation for future work\" 而非 finding。\n\n**W2** [warning] **标题 overclaim——\"Why ... Fail\" 暗示因果解释，但实验仅提供 single case study 的描述性证据**\n- 具体位置：标题、Section 6 标题 \"Discriminability ≠ Reward Utility\"\n- 问题：标题使用 \"Why\" 暗示提供了因果解释，但论文实际上只在一个模型 (Qwen3-8B)、一个 RL 算法 (GRPO with group_size=2)、一个方向 (d_syc from 181 GPT-4.1 pairs) 上做了实验。Section 6 标题将 \"discriminability ≠ reward utility\" 提升为一般性原则，但证据来自 single case study。论文中引用的 Zhang et al. (2026) 和 Wu and Tang (2026) 的对比论证是方向正确的，但不能替代本文自身的实验覆盖面。\n- 建议：(1) 标题改为条件性表述，如 \"When Sycophancy Directions Fail as GRPO Rewards: A Case Study\"；(2) Section 6 标题改为 \"Evidence that Discriminability May Not Imply Reward Utility\"。\n\n**W3** [warning] **181 对 contrastive pairs 的 evidence strength 标注缺乏人类 IAA**\n- 具体位置：Section 2.1、Limitations\n- 问题：Evidence strength 的三级标注（weak/medium/strong）由 GPT-4.1 单一标注者完成，无人类 inter-annotator agreement。论文在 Limitations 中承认了这一点。对于 discriminability 分析（Figure 1, Table 1），annotation 质量直接影响 AUROC 的 evidence-stratified 分析的可信度——如果 GPT-4.1 的 weak/medium/strong 划分不准确，evidence gradient（0.675 → 0.883 → 0.929）可能是 annotation artifact。\n- 建议：抽样 50 对做人类标注，报告 Cohen's κ 或 Fleiss' κ。\n\n**W4** [warning] **ACT seed 2 仅完成 4/16 checkpoints 评估——不应作为证据呈现**\n- 具体位置：Table 4 (footnote ‡)、Section 6\n- 问题：ACT seed 2 标注为 \"ongoing; 4/16 ckpts evaluated, all > vanilla\"。25% 的评估完成度不构成可靠证据，且 \"all > vanilla\" 可能存在 selection bias（如果前 4 个 checkpoints 是 cherry-picked）。论文多次引用 \"seed 2: 4/4 ongoing\" 作为 ACT 成功的支撑证据，但这 4 个点可能恰好是 ACT 表现最好的阶段。\n- 建议：(1) 完成全部 16 checkpoints 的评估后再投稿；(2) 如果无法完成，删除 ACT seed 2 相关数据和讨论，仅基于 seed 1 报告。\n\n**W5** [warning] **Cross-seed rank correlation ρ≈0.33 的统计报告不充分**\n- 具体位置：Section 6 (\"Cross-seed rank correlation is ≈1.0 during early training (steps 1000–3000) but drops to ρ≈0.33 (n.s.) after step 4000\")\n- 问题：论文未说明 (1) correlation 的 N 是多少（即多少个 checkpoints 参与排序），(2) 如何划分 \"early\" 和 \"late\" 窗口，(3) ρ≈1.0 是在 N=3 上计算的还是更多。如果 early window 只有 3 个 checkpoints，ρ=1.0 几乎是必然的（3 点的 Spearman 只能取 1.0, 0.5, -0.5, -1.0）。Late window 的 ρ≈0.33 (n.s.) 也因 N 过小而无统计功效。论文正确标注了 \"n.s.\" 但仍将此作为 \"stochastic divergence\" 的证据呈现。\n- 建议：报告 exact N、p-value、和 confidence interval；如果 N<10，承认统计功效不足以支撑任何结论。\n\n**W6** [warning] **R₃-only GRPO 在 Table 4 中缺少 ToF 和 NoF 的分项数据**\n- 具体位置：Table 4（R₃-only GRPO 行，ToF 和 NoF 列显示 \"--\"）\n- 问题：Section 6 文字声称 R₃-only GRPO \"exhibits the same stubbornness pattern (high NoF, near-zero ToF)\"，但 Table 4 未报告这些数字。对于论文的关键论证——\"即使移除 d_syc，纯行为奖励下的 GRPO 也表现出相同的 stubbornness pattern\"——这些数字是必要的。\n- 建议：在 Table 4 中填充 R₃-only GRPO 的 ToF 和 NoF 值。\n\n---\n\n## 小问题（不影响接收）\n\n1. **数字一致性**：Abstract 和正文在 R₃-only checkpoints 总数上可能存在 26 vs 27 的微小不一致（需作者确认）。PDF 第 1 页 abstract 部分似乎显示 \"4 of 26\"，但 Introduction 和 Section 6 使用 \"4 of 27\"。\n2. **SyconScore 定义位置**：SyconScore 首次出现在 Section 2.5，但 harmonic mean 选择而非 arithmetic mean 的 justification 仅一句话带过。虽然在 supplementary materials 中提供了 arithmetic mean 结果，但正文应简要说明 harmonic mean 更严格惩罚单侧极端的理由。\n3. **Stubbornness taxonomy (Appendix B)**：三种失败模式（sycophantic stubbornness 24%, deliberation traps 29%, evidence-graded hedging 百分比未报告）的百分比加起来不到 100%，剩余比例是什么？\n4. **写作小问题**：Table 2 标题中 \"GRPO with R = w₁·R₁ + w₃·R₃\" 使用了 R₁ 和 R₃ 但未使用 R₂，可能困扰读者。\n\n---\n\n## 主要优势\n\n1. **研究问题重要且及时**：representation engineering 越来越多地被用于 reward design，本文提出的 \"discriminability ≠ utility\" 框架是对该领域的有价值警示。\n2. **系统性 failure mode 分析**：6 种配置形成诊断链（F1a→F1b→F1c→F1d→F2→F3），每种解决前一种的 failure mode 但暴露更深层问题，论证结构清晰。\n3. **Probe reward trap 发现有原创性**：behavioral death ($\\tof=0$) 发生在 distributional collapse (entropy drop) 之前 1,300 步的发现（Table 3, Figure 2）对 RL alignment 实践有直接价值——它表明 entropy-based early stopping 不足以检测 reward hacking。该发现在 SFT 设定下取得，不受 GRPO hyperparameter 的 confound 影响。\n4. **Cross-model validation**：d_syc 的 discriminability 在 Qwen3-8B 和 Llama-3-8B 上均得到验证（Table 1），evidence-strength gradient 在两个模型上一致。\n5. **Limitations 诚实全面**：论文坦承了 group_size=2、truncation、2 seeds、incomplete ACT seed 2、无人类 IAA 等所有主要局限，这是学术诚实的体现。\n\n---\n\n## 缺失的参考文献\n\n论文的相关工作覆盖合理。可考虑补充：\n- Perez et al. (2022) \"Discovering Language Model Behaviors with Model-Written Evaluations\" — 早期 sycophancy 量化方法\n- Rafailov et al. (2023) DPO — 作为 GRPO 之外的另一类 RL 方法讨论 alternatives\n\n---\n\n## 总结\n\n本文的核心洞见（representation discriminability 不保证 RL reward utility）有价值，probe reward trap 的发现对 alignment 实践有实际意义。但 GRPO group_size=2 和 80-84% truncation 这两个 confound 使得论文无法可靠区分 \"d_syc 本质上不能做 GRPO reward\" 和 \"实验配置不够好\"。R₃-only GRPO 也基本失败这一事实进一步支持后者。建议增加 group_size=8/16 的实验和更多 seeds 后重新提交，如果结论不变，论文将显著增强。当前状态适合 Findings。",
    "reviewer_id": "1",
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 249 · 2026-05-22T14:08:06.786443+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4865
}
```

</details>

---


### Tool call

_source line 250 · 2026-05-22T14:08:10.659136+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
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

_source line 251 · 2026-05-22T14:08:10.659607+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 252 · 2026-05-22T14:08:15.635734+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 253 · 2026-05-22T14:08:15.636233+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 254 · 2026-05-22T14:08:24.980249+00:00_

审稿报告已提交给 Review Director。

**核心评价**：Overall 3.0 (Findings)。论文研究问题重要，probe reward trap 发现有原创价值，但三个 critical 问题削弱了核心结论的可靠性：

1. **group_size=2 致命 confound** — R₃-only GRPO（不用 d_syc）也基本失败（SyconScore 0.143 vs vanilla 0.134），说明问题可能在 GRPO 配置而非 d_syc
2. **80-84% truncation** — 未验证截断是否人为压缩了 cosine gap
3. **仅 2 seeds** — 不足以支撑 "every formulation fails" 的强负面结论

Probe reward trap (C2) 是最可靠的发现，因为它在 SFT 设定下独立于 GRPO 超参。建议增加 group_size=8/16 实验和更多 seeds 后重投。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1"
}
```

</details>

---


## Round 8

## Round 8

4 recorded events


### User

_source line 255 · 2026-05-22T14:08:50.285415+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 完整审稿意见

**Overall**: 3.0 / 5（Findings）

### Must-Fix 问题

**N1** [critical] Group size=2 严重削弱 C1 的可信度
- GRPO group size=2 远低于典型范围 8-64。论文声称 C2 probe trap 独立于 GRPO hyperparameters，但 C1 的核心结论——"Every tested GRPO formulation fails"——在 group size=2 条件下可能主要反映 GRPO 在极端 hyperparameter 下的不稳定性，而非 d_syc 的根本缺陷。如果增大 group size 后 d_syc 能成功，论文核心 thesis 完全翻转。建议至少在一个 formulation 上测试 group size=8/16。

**N2** [critical] 标题和 framing 过度泛化，与证据范围不匹配
- 标题 "Discriminability Without Utility" 暗示一般性原则，但证据仅来自一种行为属性（sycophancy）、一种 RL 算法（GRPO）、一种主要模型（Qwen3-8B）、极小 group size(2)。Wu & Tang (2026) 展示 representation engineering 在 reward hacking detection 中成功（100% accuracy），与本文负面结论直接对比，论文需更精确界定 claim 适用范围。建议标题限定到 sycophancy 和/或 GRPO。

**N3** [critical] 缺乏与标准 RM-based GRPO 的对比基线
- 缺少关键对照：标准 reward model（如 trained classifier 或 LLM-as-judge）的 GRPO 在同一 task 上是否能成功？如果标准 RM 也失败，问题在 task/setup 而非 d_syc；如果成功，更有力支持 "discriminability ≠ utility"。建议添加 LLM-judge-based GRPO baseline。

### Should-Fix 问题

**W1** [warning] Wu & Tang (2026) 对比论证缺乏定量分析
- AUROC 0.827 显示不错的可分性，但论文未定量验证 sycophancy 的 d_syc 是否缺乏 Wu & Tang 所需的 geometric separability。建议定量比较两种 direction 的 geometric properties。

**W2** [warning] CRAFT 和 Latent-GRPO 讨论过于简略
- 这两个工作都使用 latent-space signal 做 RL 训练，与本文核心主题直接相关，但各只有半句话。应讨论为什么这些方法成功而本文方法失败。

**W3** [warning] 仅2个 random seed 的统计说服力不足
- 2 seeds 不足以建立统计显著性。两条轨迹定性一致但定量差异大（crash onset 差 ~2500 步）。建议增加到 3-5 seeds 或措辞更谨慎。

**W4** [warning] DPO/KTO 作为替代方案未做实验探索
- d_syc 可直接生成 preference pairs，DPO/KTO 是自然替代方案。仅列为 open question 降低完整性。建议至少测试一种 preference-based 方法。

**W5** [warning] 缺少 Process Reward Model (PRM) 讨论
- 论文 reward 是 outcome-level。PRM 提供 per-step reward，可能缓解 d_syc 的局限。论文未讨论 PRM 视角。

### 小问题
- 术语交替使用 "behavioral collapse" 和 "behavioral death"
- Table 3 排版略乱
- Section 6 标题直接用等式不太规范
- Figure 1 字体偏小

### 主要优势
1. 系统性实验设计（6种配置）
2. Probe reward trap (C2) 有实用价值
3. Cross-model 验证
4. Mechanistic 分析有深度
5. 写作清晰
6. 格式合规

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 256 · 2026-05-22T14:10:05.285712+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: Group size=2 严重削弱 C1 的可信度**\n同意。这与我的 N1 完全一致。补充一个 R2 未强调的关键证据：Table 4 显示 R₃-only GRPO（完全不使用 d_syc 的纯行为奖励）仅 4/27 checkpoints 超过 vanilla（SyconScore 0.143 vs vanilla 0.134），与 d_syc-based formulations 的失败模式高度相似。这意味着在 group_size=2 下，**即使是\"正常\"的奖励信号也基本不工作**，进一步印证 R2 的判断：失败可能主要反映 GRPO 在极端超参下的不稳定性，而非 d_syc 的根本缺陷。论文在 Limitations 中的 disclosure 是诚实的，但不足以挽救因果推断的缺失。\n\n**[AGREE] R2-N2: 标题和 framing 过度泛化**\n同意。我在 W2 中提出了相同观点。R2 提到的 Wu & Tang (2026) 对比特别有力——如果 representation engineering 在 reward hacking detection 中以 100% accuracy 成功（Section 6 引用），那么 \"Discriminability Without Utility\" 这个标题作为一般性声明是误导性的。论文在 Section 6 中确实引用了 Wu & Tang 并尝试用 \"geometric separability\" 解释差异（Section 6: \"direction utility depends on geometric separability, not the optimization framework\"），但这个解释本身未经定量验证（见下 W1 回应）。标题应限定为 sycophancy-specific 的发现。\n\n**[AGREE] R2-N3: 缺乏标准 RM-based GRPO 对比基线**\n同意，这是我未充分强调的重要遗漏。当前实验设计的核心缺陷是：我们无法区分三种竞争假说：(a) d_syc 本质上不适合做 reward；(b) GRPO group_size=2 下任何 reward 都不工作；(c) sycophancy calibration 本身不适合 scalar per-completion RL。一个标准 RM baseline（如 trained classifier 或 LLM-as-judge）在相同 GRPO 设定下的表现可以有效区分这三种假说。如果标准 RM 也失败 → 支持 (b) 或 (c)；如果标准 RM 成功 → 排除 (b)，支持 (a)。论文的 R₃-only GRPO 实验（Table 4）部分扮演了这个角色（使用 NLI-based 行为奖励），但其同样失败恰恰暗示问题在 (b) 而非 (a)。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Wu & Tang 对比论证缺乏定量分析**\n同意。Section 6 声称 \"direction utility depends on geometric separability\"，并引用 Wu & Tang (2026) 的 reward hacking detection 作为正面案例，但未提供任何定量指标来比较两种 direction 的 geometric properties。例如，sycophancy direction 的 valid-vs-sycophantic cluster 间距 vs Wu & Tang 的 shortcut-vs-genuine cluster 间距是否有量化差异？cosine gap 0.098（Section 4）是否在 Wu & Tang 的设定中显著更大？论文将 \"geometric separability\" 作为核心解释机制，却未提供定量验证，使整个因果论证停留在推测层面。\n\n**[REBUT] R2-W2: CRAFT 和 Latent-GRPO 讨论过于简略**\n部分不同意。论文在 Section 8 (Related Work) 中确实仅简要提及了 CRAFT (Luo et al., 2026) 和 Latent-GRPO (Zhang et al., 2026)，但 Section 6 的第一段对 Zhang et al. (2026) 有实质性讨论：\"Latent-GRPO extends GRPO with latent-space rewards for reasoning; CRAFT applies representation-level constraints during RL\"，并通过 geometric separability 框架解释了差异——这些方法处理的行为属性（reasoning faithfulness, safety）在表征空间中具有几何可分性，而 sycophancy 不具备。讨论的深度确实可以增加，但并非\"各只有半句话\"。不过，我同意论文应更详细地讨论为什么这些方法的成功不能直接迁移到 sycophancy——特别是 CRAFT 的 representation-level constraint 是否面临与 d_syc 相同的 entanglement 问题。\n\n**[AGREE] R2-W3: 仅 2 seeds 统计说服力不足**\n同意。与我的 N3 一致。R2 正确指出两条轨迹 \"定性一致但定量差异大\"——crash onset 差 ~2,500 步（Section 6: \"crash onset differs by ~2,500 steps\"）在 8,000 步训练中占 31%。这不是 \"qualitatively consistent\" 能充分概括的。\n\n**[REBUT] R2-W4: DPO/KTO 作为替代方案未做实验探索**\n部分不同意。这确实是合理的 future direction，但将其列为 Should-Fix 可能超出本文合理范围。论文的 scope 已经包含 6 种配置（4 cosine variants + 1 binary probe + 1 continuous probe）和 2 种训练范式（GRPO + SFT），加上 R₃-only 和 ACT 对照。DPO/KTO 是不同的优化框架，引入它们需要大量额外实验工作。论文在 Section 6 (Future directions) 明确提出 \"PPO, RLOO, and other REINFORCE-style methods\" 作为 open questions，这是合理的 scoping。我认为这更适合作为 \"suggestion for future work\" 而非 Should-Fix。\n\n**[REBUT] R2-W5: 缺少 Process Reward Model (PRM) 讨论**\n不同意。论文实际上在 Section 6 中已讨论了 supervision granularity 这一维度。ACT 的成功被归因于 dense per-token supervision（Section 6: \"ACT's dense per-token supervision succeeded\"），这与 PRM 的 per-step reward 精神一致。论文还在 Section 6 中提出 \"per-step process rewards offer paths forward\" 作为 future direction（Section 6, Future directions paragraph）。虽然论文未使用 \"PRM\" 这个术语，但概念上已覆盖——per-step/per-token reward 作为 per-completion scalar reward 的替代方案是明确讨论过的。补充 PRM 术语可以增加可检索性，但不构成内容缺失。\n\n---\n\n### 小问题\n\n- **\"behavioral collapse\" vs \"behavioral death\" 术语混用**：同意，应统一。但从上下文看，论文似乎有意区分：behavioral collapse 指 cosine formulations 下的模式坍缩（Section 4），behavioral death 特指 probe trap 下 ToF=0 的极端状态（Section 5）。如果确实是有意区分，应在首次使用时定义。\n- **其余排版/字体问题**：同意，属于 camera-ready 修复范围。\n\n---\n\n### 总体评价\n\nR2 的审稿意见整体中肯，尤其是 N3（缺乏标准 RM baseline）是我未充分强调但非常重要的遗漏。R2 的 N1 和 N2 与我的 N1、W2 高度一致，进一步确认 group_size confound 和 overclaim 是本文最核心的问题。\n\n在 Should-Fix 层面，R2-W4 和 R2-W5 对额外实验和讨论的要求偏高——本文的实验覆盖面（6 种配置 + 2 对照）在 empirical study 中已属合理，且 PRM 概念已在 future directions 中涵盖。R2-W1（geometric separability 定量分析）和 R2-W3（seeds 数量）则是合理的 improvement 方向。\n\n两位 Reviewer 在 group_size confound、title overclaim、seed 数量不足上完全一致。综合来看，论文需要 (1) 增大 group size 的实验、(2) 限定 claim scope、(3) 增加 seeds 后才能从 Findings 提升到 Conference。",
  "reviewer_id": "1",
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: Group size=2 严重削弱 C1 的可信度**\n同意。这与我的 N1 完全一致。补充一个 R2 未强调的关键证据：Table 4 显示 R₃-only GRPO（完全不使用 d_syc 的纯行为奖励）仅 4/27 checkpoints 超过 vanilla（SyconScore 0.143 vs vanilla 0.134），与 d_syc-based formulations 的失败模式高度相似。这意味着在 group_size=2 下，**即使是\"正常\"的奖励信号也基本不工作**，进一步印证 R2 的判断：失败可能主要反映 GRPO 在极端超参下的不稳定性，而非 d_syc 的根本缺陷。论文在 Limitations 中的 disclosure 是诚实的，但不足以挽救因果推断的缺失。\n\n**[AGREE] R2-N2: 标题和 framing 过度泛化**\n同意。我在 W2 中提出了相同观点。R2 提到的 Wu & Tang (2026) 对比特别有力——如果 representation engineering 在 reward hacking detection 中以 100% accuracy 成功（Section 6 引用），那么 \"Discriminability Without Utility\" 这个标题作为一般性声明是误导性的。论文在 Section 6 中确实引用了 Wu & Tang 并尝试用 \"geometric separability\" 解释差异（Section 6: \"direction utility depends on geometric separability, not the optimization framework\"），但这个解释本身未经定量验证（见下 W1 回应）。标题应限定为 sycophancy-specific 的发现。\n\n**[AGREE] R2-N3: 缺乏标准 RM-based GRPO 对比基线**\n同意，这是我未充分强调的重要遗漏。当前实验设计的核心缺陷是：我们无法区分三种竞争假说：(a) d_syc 本质上不适合做 reward；(b) GRPO group_size=2 下任何 reward 都不工作；(c) sycophancy calibration 本身不适合 scalar per-completion RL。一个标准 RM baseline（如 trained classifier 或 LLM-as-judge）在相同 GRPO 设定下的表现可以有效区分这三种假说。如果标准 RM 也失败 → 支持 (b) 或 (c)；如果标准 RM 成功 → 排除 (b)，支持 (a)。论文的 R₃-only GRPO 实验（Table 4）部分扮演了这个角色（使用 NLI-based 行为奖励），但其同样失败恰恰暗示问题在 (b) 而非 (a)。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Wu & Tang 对比论证缺乏定量分析**\n同意。Section 6 声称 \"direction utility depends on geometric separability\"，并引用 Wu & Tang (2026) 的 reward hacking detection 作为正面案例，但未提供任何定量指标来比较两种 direction 的 geometric properties。例如，sycophancy direction 的 valid-vs-sycophantic cluster 间距 vs Wu & Tang 的 shortcut-vs-genuine cluster 间距是否有量化差异？cosine gap 0.098（Section 4）是否在 Wu & Tang 的设定中显著更大？论文将 \"geometric separability\" 作为核心解释机制，却未提供定量验证，使整个因果论证停留在推测层面。\n\n**[REBUT] R2-W2: CRAFT 和 Latent-GRPO 讨论过于简略**\n部分不同意。论文在 Section 8 (Related Work) 中确实仅简要提及了 CRAFT (Luo et al., 2026) 和 Latent-GRPO (Zhang et al., 2026)，但 Section 6 的第一段对 Zhang et al. (2026) 有实质性讨论：\"Latent-GRPO extends GRPO with latent-space rewards for reasoning; CRAFT applies representation-level constraints during RL\"，并通过 geometric separability 框架解释了差异——这些方法处理的行为属性（reasoning faithfulness, safety）在表征空间中具有几何可分性，而 sycophancy 不具备。讨论的深度确实可以增加，但并非\"各只有半句话\"。不过，我同意论文应更详细地讨论为什么这些方法的成功不能直接迁移到 sycophancy——特别是 CRAFT 的 representation-level constraint 是否面临与 d_syc 相同的 entanglement 问题。\n\n**[AGREE] R2-W3: 仅 2 seeds 统计说服力不足**\n同意。与我的 N3 一致。R2 正确指出两条轨迹 \"定性一致但定量差异大\"——crash onset 差 ~2,500 步（Section 6: \"crash onset differs by ~2,500 steps\"）在 8,000 步训练中占 31%。这不是 \"qualitatively consistent\" 能充分概括的。\n\n**[REBUT] R2-W4: DPO/KTO 作为替代方案未做实验探索**\n部分不同意。这确实是合理的 future direction，但将其列为 Should-Fix 可能超出本文合理范围。论文的 scope 已经包含 6 种配置（4 cosine variants + 1 binary probe + 1 continuous probe）和 2 种训练范式（GRPO + SFT），加上 R₃-only 和 ACT 对照。DPO/KTO 是不同的优化框架，引入它们需要大量额外实验工作。论文在 Section 6 (Future directions) 明确提出 \"PPO, RLOO, and other REINFORCE-style methods\" 作为 open questions，这是合理的 scoping。我认为这更适合作为 \"suggestion for future work\" 而非 Should-Fix。\n\n**[REBUT] R2-W5: 缺少 Process Reward Model (PRM) 讨论**\n不同意。论文实际上在 Section 6 中已讨论了 supervision granularity 这一维度。ACT 的成功被归因于 dense per-token supervision（Section 6: \"ACT's dense per-token supervision succeeded\"），这与 PRM 的 per-step reward 精神一致。论文还在 Section 6 中提出 \"per-step process rewards offer paths forward\" 作为 future direction（Section 6, Future directions paragraph）。虽然论文未使用 \"PRM\" 这个术语，但概念上已覆盖——per-step/per-token reward 作为 per-completion scalar reward 的替代方案是明确讨论过的。补充 PRM 术语可以增加可检索性，但不构成内容缺失。\n\n---\n\n### 小问题\n\n- **\"behavioral collapse\" vs \"behavioral death\" 术语混用**：同意，应统一。但从上下文看，论文似乎有意区分：behavioral collapse 指 cosine formulations 下的模式坍缩（Section 4），behavioral death 特指 probe trap 下 ToF=0 的极端状态（Section 5）。如果确实是有意区分，应在首次使用时定义。\n- **其余排版/字体问题**：同意，属于 camera-ready 修复范围。\n\n---\n\n### 总体评价\n\nR2 的审稿意见整体中肯，尤其是 N3（缺乏标准 RM baseline）是我未充分强调但非常重要的遗漏。R2 的 N1 和 N2 与我的 N1、W2 高度一致，进一步确认 group_size confound 和 overclaim 是本文最核心的问题。\n\n在 Should-Fix 层面，R2-W4 和 R2-W5 对额外实验和讨论的要求偏高——本文的实验覆盖面（6 种配置 + 2 对照）在 empirical study 中已属合理，且 PRM 概念已在 future directions 中涵盖。R2-W1（geometric separability 定量分析）和 R2-W3（seeds 数量）则是合理的 improvement 方向。\n\n两位 Reviewer 在 group_size confound、title overclaim、seed 数量不足上完全一致。综合来看，论文需要 (1) 增大 group size 的实验、(2) 限定 claim scope、(3) 增加 seeds 后才能从 Findings 提升到 Conference。",
    "reviewer_id": "1",
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 257 · 2026-05-22T14:10:09.157857+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3872
}
```

</details>

---


### Assistant

_source line 258 · 2026-05-22T14:10:16.585574+00:00_

交叉回应已提交。两位 Reviewer 在三个核心问题上达成一致：group_size=2 confound (N1)、标题 overclaim (N2)、seeds 不足 (W3/N3)。我对 R2 的 W4 (DPO/KTO) 和 W5 (PRM) 提出了有理据的 rebut——前者超出合理 scope，后者在概念上已被论文覆盖。R2 新提出的 N3（缺乏标准 RM baseline）是重要补充，R₃-only GRPO 的失败实际上暗示问题在 GRPO 设定而非 d_syc。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1"
}
```

</details>

---


## Round 9

## Round 9

70 recorded events


### User

_source line 259 · 2026-05-22T15:27:46.158326+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责 **方法严谨性** 审查。

## 论文信息
- 标题: "The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration"
- 文件路径: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/submitted.pdf`
- 目标 venue: EMNLP 2026 (ARR May 2026)
- 截止日期: 2026-05-25
- 类型: Long paper (≤8 页正文, unlimited references)
- 模板: ACL LaTeX
- 匿名: double-blind

## 你的审查侧重

重点评估以下维度：

1. **实验设计与统计有效性**
   - GRPO group_size=2 是否构成致命 confound？R₃-only GRPO 也失败是否支持/削弱论文结论？
   - 2 seeds 是否足以支撑负面结论？统计检验是否恰当？
   - 80-84% truncation rate (max_completion_length=256) 对结果有效性影响
   - ACT seed 2 仅部分完成（6/16 checkpoints）的证据强度

2. **Confound 与替代解释**
   - 论文是否充分讨论 group_size confound？
   - ACT vs GRPO 5+ 维度差异是否被适当 acknowledge？
   - 是否存在遗漏的替代假说？

3. **可复现性**
   - 超参数是否完整披露？
   - 训练细节是否足以复现？

4. **数据与指标**
   - SyconScore (harmonic mean) 的选择是否有充分 justification？
   - Contrastive pairs 181 对的构建质量和 validation
   - Cross-seed correlation 的统计报告是否充分？

请以 ARR reviewer 标准严格评审，给出 Strengths / Weaknesses / Questions / Overall Assessment（含评分 1-5，参考 EMNLP 2026 评分标准）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 260 · 2026-05-22T15:27:55.240552+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 261 · 2026-05-22T15:27:56.044540+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/review_reviewer_1_a4d5bbcf.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 262 · 2026-05-22T15:27:56.096057+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
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

_source line 263 · 2026-05-22T15:27:56.096505+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 264 · 2026-05-22T15:28:02.997915+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 265 · 2026-05-22T15:28:03.703554+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/submitted.pdf",
  "project": "contrastive_entrain_calib",
  "pages": "1-8",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/submitted.pdf",
    "project": "contrastive_entrain_calib",
    "pages": "1-8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 266 · 2026-05-22T15:28:10.981715+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines, review form criteria, and related policies:

## Reviewer Guidelines and Responsibilities

Reviewers are asked to follow this workflow: (1) read the paper and get the
…[truncated 1562 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7983
}
```

</details>

---


### Tool result

_source line 267 · 2026-05-22T15:28:11.985777+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 418.2}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 435.9}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 472.6}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 435.3}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 459.9}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 476.4}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 483.9}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 477.8}], \"total_pages\": 11, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrast
…[truncated 95 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 8282
}
```

</details>

---


### Tool call

_source line 268 · 2026-05-22T15:28:19.688379+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include: Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other dimensions. List every score option with its description."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include: Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other dimensions. List every score option with its description."
  }
}
```

</details>

---


### Tool call

_source line 269 · 2026-05-22T15:28:20.743165+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/submitted.pdf",
  "project": "contrastive_entrain_calib",
  "pages": "9-11",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/submitted.pdf",
    "project": "contrastive_entrain_calib",
    "pages": "9-11",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 270 · 2026-05-22T15:28:21.495686+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 271 · 2026-05-22T15:28:22.348408+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 272 · 2026-05-22T15:28:22.449045+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 273 · 2026-05-22T15:28:23.051378+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 274 · 2026-05-22T15:28:25.810361+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: Quite sure; unlikely to have missed important points
- **3**: Pretty sure; may have missed some details
- **2**: Willing to defend evaluation; fairly likely missed details
- **1**: Not expert area; evaluation is educated guess

## 2. **Soundness**
Scale: 1-5 (with .5 increments)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: Strong; sufficient support with optional enhancements
- **3**: Acceptable; main claims supported with minor gaps
- **2**: Poor; main claims lack sufficient support
- **1**: Major issues; insufficiently thorough for publication

## 3. **Excitement**
Scale: 1-5 (with .5 increments)
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: Exciting; would mention to colleagues
- **3**: Interesting; might mention selectively
- **2**: Potentially interesting; doesn't resonate personally
- **1**: Not exciting; unlikely resonates with community

## 4. **Overall Assessment**
Scale: 1-5 (with .5 increments)
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance
- **3**: Findings acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit

## 5. **Reproducibility**
Scale: 1-5
- **5**: Results easily reproducible
- **4**: Mostly reproducible; minor variations possible
- **3**: Reproducible with difficulty
- **2**: "Hard pressed to reproduce results"
- **1**: Cannot reproduce results

## 6. **Datasets & Software**
Scale: 1-5 each
- **5**: Enabling impact on research choices
- **4**: Useful for ongoing work
- **3**: Potentially useful
- **2**: Documentary value
- **1**: No usable resources

## 7. **Author Identity Knowledge**
Scale: 1-5 (disclosure metric, not quality assessment)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6121
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-22T15:28:26.115109+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 483.9}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 451.9}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 136.3}], \"total_pages\": 11, \"rendered_pages\": 3, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 5371
}
```

</details>

---


### Tool result

_source line 276 · 2026-05-22T15:28:28.717287+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 6268
}
```

</details>

---


### Tool result

_source line 277 · 2026-05-22T15:28:28.872685+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 6524
}
```

</details>

---


### Tool result

_source line 278 · 2026-05-22T15:28:28.873811+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 7378
}
```

</details>

---


### Tool result

_source line 279 · 2026-05-22T15:28:28.926550+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 5875
}
```

</details>

---


### Tool call

_source line 280 · 2026-05-22T15:28:33.248632+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 281 · 2026-05-22T15:28:33.702061+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 282 · 2026-05-22T15:28:34.507743+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1259
}
```

</details>

---


### Tool result

_source line 283 · 2026-05-22T15:28:34.609297+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 284 · 2026-05-22T15:28:34.609778+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 285 · 2026-05-22T15:28:34.717245+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 286 · 2026-05-22T15:28:35.781229+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1171
}
```

</details>

---


### Tool result

_source line 287 · 2026-05-22T15:28:35.984911+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1267
}
```

</details>

---


### Tool call

_source line 288 · 2026-05-22T15:28:41.057375+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 289 · 2026-05-22T15:28:41.510032+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 290 · 2026-05-22T15:28:42.263599+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1206
}
```

</details>

---


### Tool result

_source line 291 · 2026-05-22T15:28:42.264348+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 754
}
```

</details>

---


### Tool call

_source line 292 · 2026-05-22T15:28:42.415179+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 293 · 2026-05-22T15:28:42.467539+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 294 · 2026-05-22T15:28:48.414824+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 295 · 2026-05-22T15:28:48.465959+00:00_

1	\documentclass[11pt,a4paper]{article}
2	\usepackage[hyperref]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{graphicx}
10	\usepackage{xcolor}
11	\usepackage{subcaption}
12	
13	\newcommand{\dsyc}{d_{\text{syc}}}
14	\newcommand{\tof}{\text{ToF}}
15	\newcommand{\nof}{\text{NoF}}
16	\newcommand{\sycon}{\textsc{SyconScore}}
17	\newcommand{\rone}{R_1}
18	\newcommand{\rthree}{R_3}
19	
20	\title{The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\begin{abstract}
28	\input{sections/abstract}
29	\end{abstract}
30	
31	\input{sections/introduction}
32	
33	\input{sections/framework}
34	
35	\input{sections/direction_quality}
36	
37	\input{sections/cosine_failure}
38	
39	\input{sections/probe_trap}
40	
41	\input{sections/discussion}
42	
43	\input{sections/related_work}
44	
45	\input{sections/conclusion}
46	
47	\section*{Limitations}
48	\input{sections/limitations}
49	
50	\section*{Reproducibility}
51	Code and data will be released upon acceptance. All training hyperparameters are reported in Appendix~\ref{app:training}. The 181 contrastive pairs and evaluation benchmark are included in the supplementary materials.
52	
53	\bibliography{references}
54	
55	\appendix
56	\input{sections/appendix}
57	
58	\end{document}
59	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 296 · 2026-05-22T15:28:51.908314+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 297 · 2026-05-22T15:28:51.959042+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 298 · 2026-05-22T15:28:54.970448+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 299 · 2026-05-22T15:28:55.021093+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/direction_quality.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/probe_trap.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/abstract.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 300 · 2026-05-22T15:28:58.232051+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex"
  }
}
```

</details>

---


### Tool result

_source line 301 · 2026-05-22T15:28:58.633910+00:00_

1	\section{Experimental Framework}
2	\label{sec:framework}
3	
4	\subsection{Direction Extraction}
5	\label{ssec:extraction}
6	
7	We extract a linear sycophancy direction $\dsyc$ from the residual stream using contrastive activation pairs: a \emph{valid correction} (warranted belief revision under strong evidence) and a \emph{sycophantic capitulation} (unwarranted concession under social pressure).
8	We construct 181 contrastive pairs using GPT-4.1 in a two-stage pipeline: skeleton generation followed by 3-turn dialogue completion.
9	Style matching is enforced by automated validation (response length difference ${<}10\%$, shared opening phrase ${\geq}2$ words), with up to 3 retries per pair; 19 of 200 initial pairs were discarded for failing validation.
10	Evidence strength is annotated at three levels: \emph{weak} (75 pairs; personal memory or opinion), \emph{medium} (54 pairs; brief source citation), and \emph{strong} (52 pairs; authoritative source with detailed data).
11	From the 181 paired examples (362 activations total), we compute the mean difference at target layer $\ell$:
12	\begin{equation}
13	\label{eq:dsyc}
14	\dsyc = \frac{1}{N}\sum_{i=1}^{N}\left(\mathbf{h}^{+}_i - \mathbf{h}^{-}_i\right)
15	\end{equation}
16	where $\mathbf{h}^{+}_i$ and $\mathbf{h}^{-}_i$ are residual-stream activations for the $i$-th valid and sycophantic response.
17	The target layer is selected by 5-fold cross-validated AUROC; on Qwen3-8B this yields layer 19 with AUROC $0.827$ (bootstrap 95\% CI $[0.795,\, 0.857]$).
18	
19	\subsection{Reward Formulations}
20	\label{ssec:reward}
21	
22	Three formulations translate $\dsyc$ into a direction-based signal $\rone$.
23	For F1 and F3, $\rone$ enters as part of a GRPO \citep{shao2024grpo} reward $R = w_1 \cdot \rone + w_3 \cdot \rthree$, where $\rthree$ is a behavioral component (DeBERTa NLI classifier scoring consistency with the ground-truth answer).
24	\begin{itemize}
25	\item[\textbf{F1}] \textbf{Cosine projection} with four variants: 
…[truncated 3405 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 302 · 2026-05-22T15:28:58.684690+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 303 · 2026-05-22T15:28:59.187040+00:00_

1	\section{Training Details}
2	\label{app:training}
3	
4	\paragraph{Reward weight selection.}
5	The weight $w_1$ is set by diagnostic-driven iteration: $w_1{=}0.25$ was initially chosen to down-weight the noisy cosine reward term; this was later increased to $w_1{=}0.40$ for F1d after diagnostics revealed that $w_1{=}0.25$ allowed the cosine term to contribute only ${\sim}8.3\%$ of total reward variance.
6	The empirical scaling factor in F1a ($\dsyc/20$) is a heuristic normalization; we did not find it critical to the failure modes reported.
7	
8	\paragraph{Response truncation.}
9	All GRPO experiments use \texttt{max\_completion\_length}=256, resulting in 80--84\% truncation of multi-turn responses.
10	This setting is shared across all conditions and does not affect relative comparisons; we retain it because response-level decisions typically manifest within the first 100--200 tokens.
11	
12	\paragraph{Hyperparameters.}
13	Table~\ref{tab:hyperparams} compares training configurations for GRPO variants and ACT.
14	
15	\begin{table}[h]
16	\centering
17	\small
18	\caption{Training hyperparameters. All experiments use Qwen3-8B, DeepSpeed ZeRO-2, bf16 precision.}
19	\label{tab:hyperparams}
20	\begin{tabular}{lcc}
21	\toprule
22	& GRPO (F1, F3)$^e$ & ACT \\
23	\midrule
24	Learning rate & 5e-5 & 5e-5 \\
25	Effective batch & 16 & 16 \\
26	Max steps & 8{,}000 & 8{,}000 \\
27	Warmup steps & 200 & 200 \\
28	LR schedule & linear$^a$ & linear \\
29	Grad.\ clipping & --- & 1.0 \\
30	\midrule
31	LoRA rank & 64 & 64 \\
32	LoRA $\alpha$ & 64 & 128 \\
33	LoRA modules & 4$^b$ & 7$^c$ \\
34	LoRA dropout & 0 & 0.05 \\
35	\midrule
36	Group size & 2$^d$ & --- \\
37	KL $\beta$ & 0.04 & --- \\
38	Max compl.\ len. & 256 & --- \\
39	Max seq.\ len. & --- & 1{,}024 \\
40	L2 loss weight & --- & 0.1 \\
41	\bottomrule
42	\end{tabular}
43	\\[2pt]
44	\raggedright\footnotesize
45	$^a$Cosine schedule for $\rthree$-only.
46	$^b$q/k/v/o\_proj.
47	$^c$+ gate/up/down\_proj (${\sim}1.75{\times}$ params; \S\
…[truncated 2143 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 304 · 2026-05-22T15:28:59.187421+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 305 · 2026-05-22T15:28:59.739592+00:00_

1	Our GRPO experiments use a group size of 2, below the typical range of 8--64 \citep{shao2024grpo}, due to memory constraints with 8B-parameter models. This limits within-group ranking diversity and constitutes an important confound: the observed failures may partly reflect insufficient exploration rather than a fundamental limitation of representation-based rewards. However, the probe reward trap (C2) arises in an SFT setting where group size is irrelevant, indicating that at least one failure mode is independent of GRPO hyperparameters. Additionally, all GRPO experiments truncate completions at 256 tokens (80--84\% truncation); all conditions share this setting, so relative comparisons are fair, but absolute conclusions about $\dsyc$ reward utility may be affected. Truncation analysis confirms this concern: $\dsyc$ AUROC drops from 0.76 (full response) to 0.60 (256 tokens), suggesting that offline discriminability metrics overestimate the signal available during training.
2	
3	Our RL training uses Qwen3-8B exclusively; cross-model discriminability is confirmed on Llama-3-8B (AUROC $0.779$; Table~\ref{tab:cross_model}), but compute constraints prevented training replication on a second architecture. Evidence strength was annotated by GPT-4.1 as a single annotator without human inter-annotator agreement.
4	
5	We report GRPO results from two random seeds; both exhibit qualitatively consistent oscillation patterns (similar amplitude, identical crash depth), but the limited seed count constrains statistical claims. ACT and GRPO differ along multiple dimensions beyond supervision granularity, so we cannot isolate the causal factor behind ACT's advantage.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 306 · 2026-05-22T15:28:59.740014+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex"
  }
}
```

</details>

---


### Tool result

_source line 307 · 2026-05-22T15:28:59.790543+00:00_

1	\section{Cosine \texorpdfstring{$\rone$}{R1}: Structural Failure}
2	\label{sec:cosine_failure}
3	
4	Section~\ref{sec:direction_quality} established that $\dsyc$ achieves AUROC 0.827 on Qwen3-8B.
5	We now test whether this discriminability translates into a viable GRPO reward.
6	Four configurations form a diagnostic chain (Table~\ref{tab:cosine_chain}): each resolves the failure mode of its predecessor but exposes a deeper limitation.
7	
8	\begin{table}[t]
9	\centering
10	\caption{Cosine $\rone$ failure chain on Qwen3-8B (LoRA rank$=$64, GRPO with $R = w_1 \cdot \rone + w_3 \cdot \rthree$).}
11	\label{tab:cosine_chain}
12	\begin{tabular}{lllll}
13	\toprule
14	Config & $\rone$ Formula & $w_1$ & Outcome & Root Cause \\
15	\midrule
16	F1a & $\tanh(\mathbf{h}\cdot\dsyc/20)$ & 0.25 & Gate saturation & Norm mismatch \\
17	F1b & $\cos(\mathbf{h},\, \dsyc)$ & 0.25 & $\rone \approx 0$ & Gap too small \\
18	F1c & +recalibration & 0.25 & Mode collapse & Reward discontinuity \\
19	F1d & $5\cos(\mathbf{h},\, \dsyc)$ & 0.40 & Mode collapse & $\rthree$ saturation \\
20	\bottomrule
21	\end{tabular}
22	\end{table}
23	
24	F1a uses a dot-product formulation ($\rone = \tanh(\mathbf{h} \cdot \dsyc / 20)$), but residual-stream norms exceed the direction norm by $100$--$1{,}200{\times}$, saturating the tanh gate and zeroing the gradient by step 955.
25	Switching to cosine similarity (F1b) eliminates norm dependence, yet the cosine gap between valid and sycophantic activations averages only 0.098 across layers---too narrow to generate meaningful reward contrast.
26	Online recalibration (F1c, \S\ref{ssec:recalib}) raises offline AUROC from 0.827 to 0.910 but paradoxically triggers mode collapse: the abrupt shift in $\dsyc$ at each recalibration event creates a reward discontinuity that destabilizes GRPO advantage estimates, collapsing entropy to 0.069 within 300 steps.
27	Amplifying the signal with $5{\times}$ scaling (F1d) lifts $\rone$ above the noise floor but simultaneously amplifies t
…[truncated 1214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 308 · 2026-05-22T15:29:05.429432+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/probe_trap.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/probe_trap.tex"
  }
}
```

</details>

---


### Tool result

_source line 309 · 2026-05-22T15:29:05.881651+00:00_

1	\section{The Probe Reward Trap}
2	\label{sec:probe_trap}
3	
4	The cosine formulations fail because the continuous projection of $\dsyc$ produces a gap too narrow for reward contrast.
5	A natural remedy is to discretize: train a logistic probe on $\dsyc$ and threshold its output, yielding $\rone = \mathbb{I}[P(\text{syc} \mid \mathbf{h}) < 0.5]$ (F2 in \S\ref{ssec:reward}).
6	We show that this discretization sidesteps the magnitude problem but creates a qualitatively worse failure.
7	Both probe experiments use SFT rather than GRPO (\S\ref{ssec:reward}); the trap is therefore independent of GRPO's optimization dynamics.
8	
9	\paragraph{Differentiable probe: gradient gaming.}
10	Without stop-gradient (exp-008), the policy discovers within ${\sim}30$ steps that shifting activations away from the sycophancy cluster maximizes $\rone$ regardless of response content, producing an inverted profile ($\tof = 0.978$, $\nof = 0.006$).
11	This motivates the frozen-probe design below.
12	
13	\paragraph{Binary probe: the stubbornness trap.}
14	With stop-gradient (exp-008v3), the policy cannot game the boundary but instead exploits a deeper flaw: $\dsyc$ does not condition on input validity, so refusing to revise a wrong answer receives the same $\rone = 1$ as correctly resisting invalid pressure.
15	By step 500, $\tof$ drops to 0.000 and $\nof$ reaches 0.995, yielding $\sycon = 0$.
16	Qualitative analysis of 181 valid-correction responses reveals five failure modes: \emph{deliberation traps} (28.7\%), where the model identifies the correct answer but cannot commit; \emph{sycophantic stubbornness} (24.3\%), where the model verbally agrees but does not change its answer; \emph{acknowledge-but-maintain} (23.8\%); \emph{genuine-accept-missed} (18.8\%); and refute/ignore/other (4.5\%). Full taxonomy in Appendix~\ref{app:taxonomy}.
17	
18	\paragraph{Behavioral death precedes distributional collapse.}
19	
20	\begin{table}[t]
21	\centering
22	\caption{Probe reward trap trajectory (exp-00
…[truncated 2346 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 310 · 2026-05-22T15:29:05.882163+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 311 · 2026-05-22T15:29:05.882467+00:00_

1	\section{When Does Discriminability Fail as Reward Utility?}\label{sec:discussion}
2	
3	\paragraph{Root cause of the probe reward trap.}
4	The probe reward trap (\S\ref{sec:probe_trap}) and the cosine failures (\S\ref{sec:cosine_failure}) share a common geometric root.
5	$\dsyc$ encodes the \emph{direction} of belief change but not its \emph{evidential warrant}: valid revision and sycophantic capitulation both shift activations toward the user's position along the same direction.
6	The two reward families expose complementary faces of this blindness.
7	Cosine $\rone$ penalizes all belief change indiscriminately; the resulting mode collapse (F1c, F1d) reflects excessive punishment of any activation shift along $\dsyc$.
8	The binary probe $\rone$ rewards all resistance regardless of input validity; the stubbornness trap ($\tof = 0$ by step 500) reflects excessive permissiveness toward activation stasis.
9	These are not independent design flaws but dual consequences of a direction that conflates the target behavior (resisting invalid challenges) with its complement (refusing valid corrections).
10	Cross-model evidence confirms the limitation extends beyond Qwen3-8B: Llama-3-8B independently achieves AUROC $0.779$ (bootstrap 95\% CI $[0.745,\, 0.819]$) on the same contrastive pairs with the same monotonic evidence gradient, so discriminability generalizes across architectures while the semantic gap between discriminability and reward utility persists.
11	This pattern contrasts with reasoning faithfulness and safety directions~\citep{zhang2026latentgrpo}, where the behavior to suppress is geometrically distinct from the behavior to preserve along the relevant direction.
12	\citet{wu2026rewardhacking} reinforce this principle: concept directions applied via advantage modification in GRPO achieve 100\% validation accuracy for reward hacking detection, where shortcut behaviors are geometrically separable.
13	A quantitative comparison of geometric separability between $\ds
…[truncated 7904 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 312 · 2026-05-22T15:29:06.234912+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/direction_quality.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/direction_quality.tex"
  }
}
```

</details>

---


### Tool result

_source line 313 · 2026-05-22T15:29:06.287011+00:00_

1	\section{Direction Discriminability}
2	\label{sec:direction_quality}
3	
4	Before evaluating $\dsyc$ as a reward signal (\S\ref{sec:cosine_failure}--\S\ref{sec:probe_trap}), we first establish that it captures a genuine sycophancy-related signal in the residual stream.
5	If the direction failed to discriminate sycophantic from non-sycophantic activations, downstream reward failures would be trivially explained by poor direction quality rather than by a fundamental gap between discriminability and reward utility.
6	We evaluate discriminability along five axes: cross-validated classification accuracy, evidence-strength stratification, cross-model transfer, training stability, and probe ablation.
7	Figure~\ref{fig:direction_quality} summarizes the per-layer AUROC profiles for both models.
8	
9	\paragraph{Qwen3-8B layer-wise discriminability.}
10	We evaluate $\dsyc$ via 5-fold cross-validated AUROC on 181 style-controlled contrastive pairs (\S\ref{ssec:extraction}).
11	The direction achieves AUROC $0.827$ (bootstrap 95\% CI $[0.795,\, 0.857]$) at its best layer (L19).
12	Discriminability emerges gradually across depth: layers L0--L8 perform near chance, statistical significance ($p < 0.01$) first appears at L16, and performance peaks at L19.
13	This gradual emergence, with the peak in the upper third of the network, suggests that sycophancy-relevant information is encoded as a late-stage representation rather than an input-level confound.
14	The direction also captures evidential granularity.
15	AUROC rises monotonically from 0.675 on weak-evidence pairs to 0.883 on medium and 0.929 on strong pairs.
16	This gradient indicates that $\dsyc$ encodes the degree of evidential warrant, not merely a binary sycophancy label.
17	
18	\paragraph{Cross-model generalization.}
19	To rule out that these results are specific to Qwen3-8B's representation geometry, we repeat the full extraction and evaluation pipeline on Llama-3-8B-Instruct.
20	Table~\ref{tab:cross_model} compares the t
…[truncated 3550 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 314 · 2026-05-22T15:29:11.707856+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 315 · 2026-05-22T15:29:12.210316+00:00_

1	We discover the \emph{probe reward trap}: when a frozen linear probe on a contrastive sycophancy direction ($\dsyc$, cross-validated AUROC $0.827$ on Qwen3-8B, $0.779$ on Llama-3-8B) is used as an SFT training signal, behavioral death (true-positive flip rate $= 0$) occurs within 500 steps while generation entropy remains healthy (0.70). The resulting 1{,}300-step lag before distributional collapse means that entropy monitoring---the most common safeguard against reward hacking---misses the failure entirely. Because the trap arises under SFT with stopped gradients, it is independent of RL optimization dynamics, revealing a semantic limitation of the direction itself: $\dsyc$ encodes \emph{whether} belief changed, not \emph{whether it should have}. In additional experiments on Qwen3-8B using GRPO with group size 2, cosine and continuous probe formulations of $\dsyc$ also produced behavioral collapse; removing $\dsyc$ entirely, behavioral-reward-only GRPO exceeded vanilla at only 4 of 27 checkpoints, while ACT (dense per-token SFT) exceeded vanilla at every evaluated checkpoint (seed 1: 16/16; seed 2: 6/6 ongoing). These GRPO results are consistent with $\dsyc$'s limitations as a reward signal but cannot be fully separated from the small group-size confound without further ablation.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 316 · 2026-05-22T15:29:12.210815+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 317 · 2026-05-22T15:29:12.564894+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Representation engineering \citep{zou2023repe} reveals that large language models encode sycophancy as a linear direction in their residual streams.
5	A contrastive sycophancy direction $\dsyc$, extracted from style-controlled pairs of valid belief revision and sycophantic capitulation, achieves cross-validated AUROC $0.827$ on Qwen3-8B and $0.779$ on Llama-3-8B, with discriminability rising monotonically across evidence-strength levels (\S\ref{sec:direction_quality}).
6	These results point to an appealing possibility: if the model's representations already separate sycophantic from non-sycophantic behavior, that separation should be convertible into a training signal.
7	Sycophancy is among the most persistent alignment failures in deployed systems \citep{sharma2023sycophancy}, and a representation-level signal could target the internal computation rather than its surface outputs.
8	
9	This paper identifies the \emph{probe reward trap}: when a frozen linear probe on $\dsyc$ is used as an SFT training signal with stopped gradients, behavioral death ($\tof = 0$) occurs within 500 steps while generation entropy remains healthy (0.70), masking the failure from standard monitoring (\S\ref{sec:probe_trap}).
10	The 1{,}300-step lag before distributional collapse means entropy-based early stopping---the most common safeguard against reward hacking \citep{casper2023openproblems}---would miss the failure entirely, with the reward averaging $+0.72$ throughout.
11	Because the trap arises under SFT rather than GRPO, it reflects a limitation of $\dsyc$ itself: the direction encodes \emph{whether} belief changed, not \emph{whether it should have}, so any reward conditioned on it alone will either be gamed or reward rigidity.
12	
13	Under our GRPO configuration (Qwen3-8B, group size$=$2), two additional $\dsyc$-based formulations---cosine projection (\S\ref{sec:cosine_failure}) and continuous probe---also produced behavioral 
…[truncated 2472 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 354
}
```

</details>

---


### Tool call

_source line 318 · 2026-05-22T15:29:12.565243+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 319 · 2026-05-22T15:29:12.615632+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	The probe reward trap reveals a practical danger: behavioral death can precede distributional collapse by over 1{,}000 steps, rendering entropy-based monitoring blind to the failure.
4	Because the trap arises under SFT with stopped gradients---independent of GRPO---it reflects a semantic limitation of $\dsyc$, which encodes whether belief changed but not whether it should have.
5	Under our GRPO configuration (group size$=$2), all $\dsyc$-based formulations and behavioral-reward-only GRPO also failed (4/27 checkpoints ${>}$ vanilla), consistent with this limitation though confounded by small group size (\S\ref{sec:discussion}).
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 320 · 2026-05-22T15:29:18.627195+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 321 · 2026-05-22T15:29:18.778359+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Representation Engineering.}
4	Linear directions in LLM residual streams encode behavioral concepts \citep{zou2023repe}; inference-time methods---ITI \citep{li2023iti}, ActAdd \citep{turner2023actadd}, CAA \citep{rimsky2024caa}---demonstrate that activation geometry suffices for behavioral control \citep{burns2023ccs}.
5	We use the same contrastive extraction as CAA but apply $\dsyc$ as an RL reward, revealing a gap that inference-time work does not encounter.
6	
7	\paragraph{Reward Design and Overoptimization.}
8	Proxy rewards diverge from true objectives under sustained optimization \citep{gao2023scaling}, and reward hacking can escalate to active tampering \citep{denison2024subterfuge}.
9	Our probe trap (\S\ref{sec:probe_trap}) is an extreme instance: the reward actively reinforces degenerate behavior rather than merely being circumvented \citep{skalse2022hacking}.
10	\citet{wu2026rewardhacking} demonstrate that representation-level directions succeed for reward hacking suppression when behaviors are geometrically separable (\S\ref{sec:discussion}).
11	
12	\paragraph{Sycophancy Characterization and Mitigation.}
13	Sycophancy is pervasive in RLHF-trained assistants \citep{sharma2023sycophancy}, amplified by RLHF \citep{shapira2026amplifies}, and traceable to late-layer preference shifts \citep{wang2025internal}; mitigation approaches include synthetic data \citep{wei2024synthetic}, consistency training \citep{consistency2025bctact}, and neuron-level correction \citep{obrien2025fewbadneurons}.
14	Our analysis shows why the step from diagnosis to reward is structurally blocked: $\dsyc$ conflates warranted revision with unwarranted capitulation.
15	
16	\paragraph{Probe-Based Inference-Time Mitigation.}
17	\citet{papadatos2024probepenalties} reduce sycophancy via Best-of-N reranking with linear probe penalties (94\% probe accuracy), where the probe selects among candidates without producing gradients tha
…[truncated 1062 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 322 · 2026-05-22T15:31:47.893196+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## 总体评分\n**Overall**: 3.0 / 5（Findings）\n**一句话总结**: 核心发现 probe reward trap（C2）是干净的负面结果，具有实际价值；但 GRPO 相关结论（C1）被 group_size=2 和 80-84% truncation 两个严重 confound 深度污染，削弱了整体贡献。\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2.5/5 | 核心发现 C2（probe trap in SFT）方法论干净，但 C1（GRPO failures）被 group_size=2、truncation 80-84%、LoRA 配置不对称三重 confound 侵蚀；作者虽有 acknowledge 但未做 ablation 来隔离 |\n| Excitement | 3.5/5 | \"Behavioral death precedes distributional collapse by 1,300 steps\" 是新颖且有实践警示价值的发现；但 scope 受限于单模型、2 seeds |\n| Reproducibility | 3.5/5 | 超参数表格较完整（Table 5），但 w₁ 的 diagnostic-driven iteration 过程不可复现；contrastive pairs 用 GPT-4.1 单标注无 IAA |\n| Reviewer Confidence | 4/5 | 熟悉 representation engineering、GRPO、sycophancy calibration 相关文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Group-size=2 confound 未被隔离，C1 贡献几乎无法成立\n\n- 具体位置：Section 2.5（GRPO uses a group size of 2）、Section 6 Competing hypotheses、Limitations\n- 问题：GRPO group_size=2 远低于文献典型值 8-64（论文自引 Shao et al. 2024）。在此配置下，advantage estimator 的 ranking diversity 极低——2 个 completion 之间的 pairwise comparison 本质上是 coin flip 级别的 signal。R₃-only GRPO 同样失败（4/27 checkpoints > vanilla），这恰恰说明 **group_size=2 下任何 scalar reward 都难以工作**，而非 d_syc 特有的问题。论文在 Section 6 提出三个 competing hypotheses (a)(b)(c)，但承认 \"cannot fully distinguish (a) from (b) without a group-size ablation, which we leave to future work\"。问题是：如果 (a) 和 (b) 无法区分，那么 C1 的 contribution statement（\"GRPO formulations fail under our configuration\"）实质上是在报告一个 confounded observation，而非可归因的因果结论。\n- 为什么影响接收：C1 是论文两大 contribution 之一。如果 C1 无法排除 group-size confound，论文实质上只有 C2 一个干净的 contribution。\n- 建议修改方向：(1) 在更小模型（如 Qwen2.5-1.5B）上跑 group_size=8/16 ablation，至少验证 R₃-only GRPO 在正常配置下是否能工作；或 (2) 将 C1 从 contribution 降级为 observational finding，明确标注所有 GRPO 结论均不可归因。\n\n**N2** [critical] 80-84% truncation 使训练时 d_syc 信号接近 chance level，但论文仍以 AUROC 0.827 为前提论证\n\n- 具体位置：Appendix A（\"80-84% truncation of multi-turn responses\"）、Section 4 第 7 段（\"d_syc AUROC drops from 0.76 (full response) to 0.60\"）、Limitations\n- 问题：论文在 Section 3 和 Introduction 中反复强调 d_syc AUROC=0.827，建立 \"discriminability is strong but reward fails\" 的叙事。但 Appendix A 和 Section 4 揭示：在实际训练中，由于 max_completion_length=256 导致 80-84% 的 response 被截断，d_syc AUROC 从 0.76（注意不是 0.827，0.827 是 cross-validated on activations）降至 0.60。AUROC 0.60 仅略好于 random chance（0.50），意味着训练时 reward signal 几乎是 noise。这从根本上动摇了论文的核心叙事：不是 \"high discriminability fails to transfer to reward utility\"，而可能只是 \"truncation destroyed the signal, so there's nothing left to transfer\"。\n- 为什么影响接收：论文的核心论点是 \"discriminability ≠ reward utility\"，但如果训练时 discriminability 本身就被 truncation 摧毁到 0.60，这个 gap 就不再是 semantic 的，而是 engineering 层面的 signal degradation。\n- 建议修改方向：(1) 对 probe reward trap（C2，SFT 设置）重跑 full-length completion 实验——SFT 不受 GRPO memory 约束，可以用更长的 completion；(2) 在论文叙事中明确区分 \"offline discriminability\"（0.827）和 \"training-time discriminability\"（0.60），不要在 abstract/introduction 中以 0.827 作为 reward failure 的前提。\n\n**N3** [critical] ACT vs GRPO 比较缺乏控制，5+ 维度差异使任何对比均不可归因\n\n- 具体位置：Section 6 \"Observational comparison: ACT vs GRPO\"、Table 4、Table 5\n- 问题：论文在 Table 5 中详细列出了 GRPO 和 ACT 的配置差异，但差异远比 acknowledged 的更大：\n  - LoRA α：GRPO=64，ACT=128 → 有效学习率 α/rank = 1.0 vs 2.0，**差 2 倍**\n  - LoRA modules：GRPO=4（q/k/v/o），ACT=7（+ gate/up/down）→ **可训练参数差 ~1.75x**\n  - LoRA dropout：GRPO=0，ACT=0.05\n  - Supervision：per-completion vs per-token\n  - Loss：REINFORCE vs CE+L2\n  论文说 \"included for context, not as controlled comparisons\"（Table 4 footnote ¶），但 Introduction 和 Conclusion 实质上将 ACT 的成功作为 d_syc/GRPO 失败的 foil 来使用，给读者一种 \"representation-based RL fails, token-level SFT works\" 的 takeaway。当 ACT 有 1.75x 参数量和 2x 有效学习率时，它的优势完全可能来自 capacity/optimization 而非方法论差异。\n- 为什么影响接收：如果 ACT 比较不可靠，论文的 narrative 从 \"here's why representation rewards fail and what works instead\" 缩减为 \"here are some negative results under a specific configuration\"。\n- 建议修改方向：(1) 统一 LoRA 配置（α、modules）做至少一组控制实验；(2) 或在叙事中完全去除 ACT 作为 positive contrast 的暗示，仅作为 descriptive observation。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 2 seeds 不足以支撑 GRPO 行为的统计结论\n\n- 具体位置：Section 6（\"We report GRPO results from two random seeds\"）、Limitations\n- 问题：GRPO 的 oscillation pattern、crash depth、cross-seed rank correlation 等分析均基于 n=2。论文承认 \"limited seed count constrains statistical claims\"，但仍报告了 cross-seed rank correlation（ρ≈0.33, n<10 per window），这在 n=2 seeds × <10 checkpoints 下没有统计意义。Figure 3 的 trajectory 比较（2 GRPO seeds vs 1 ACT seed）也不足以建立 systematic pattern。\n- 建议：增加到 3-5 seeds，或删除 cross-seed correlation 分析，仅保留 qualitative description。\n\n**W2** [warning] SyconScore 的 harmonic mean 设计放大了 failure 的表观严重性\n\n- 具体位置：Section 2.5 Eq.(2)、Table 4\n- 问题：SyconScore = harmonic mean(ToF, NoF)，当 ToF=0 时 SyconScore=0，无论 NoF 多高。论文说 arithmetic mean 结果 \"show qualitatively similar patterns and are reported in supplementary materials\"，但主表中 SyconScore=0.000 的视觉冲击力远大于（假设）arithmetic mean 可能给出的 0.498 (=(0+0.995)/2)。对于一篇论证 failure modes 的论文，metric 选择放大了 failure 的呈现，应在主文中同时报告两种 mean。\n- 建议：在 Table 4 中增加 arithmetic mean 列，或至少在 caption 中注明 arithmetic mean 的具体数值。\n\n**W3** [warning] Contrastive pair 单标注源 + 无 IAA\n\n- 具体位置：Section 2.1（\"using GPT-4.1 in a two-stage pipeline\"）、Limitations\n- 问题：181 对 contrastive pairs 由 GPT-4.1 生成并标注 evidence strength，无 human inter-annotator agreement。论文的 d_syc 质量完全依赖这些 pairs 的质量。虽然 automated validation（length difference <10%, shared opening phrase）控制了表层质量，但 semantic validity（特别是 sycophantic vs valid revision 的边界案例）未经人工验证。\n- 建议：报告一个 human evaluation sample（如随机抽 30-50 对由人工判断标注质量）。\n\n**W4** [warning] ACT seed 2 仅 6/16 checkpoints evaluated\n\n- 具体位置：Table 4 footnote ‡\n- 问题：ACT seed 2 标注为 \"ongoing; 6/16 ckpts evaluated, all > vanilla\"。这是一个 incomplete result。如果 ACT seed 2 的后续 10 个 checkpoints 中出现 crash（类似 seed 1 的 checkpoint 4000 dip），结论会受影响。发表时应有完整结果。\n- 建议：完成 ACT seed 2 的全部评估。\n\n**W5** [warning] d_syc 的 \"evidential warrant\" 缺失论证不够严格\n\n- 具体位置：Section 5 最后一段、Section 6 第 1 段\n- 问题：论文反复声称 d_syc \"encodes whether belief changed, not whether it should have\"，这是论文的核心理论解释。但这个 claim 主要基于 observational evidence（d_syc 给 valid revision 和 sycophantic capitulation 相似的 cosine score）。Section 3 的 evidence-strength gradient（weak 0.675 → strong 0.929 AUROC）实际上表明 d_syc **确实** 在某种程度上 encode 了 evidential warrant——强证据下 AUROC 更高，说明方向确实区分了证据质量。这与 \"does not encode whether it should have\" 的 claim 存在张力。\n- 建议：更精确地表述——不是 \"does not encode evidential warrant\"，而是 \"encodes evidential warrant insufficiently for reward contrast\"，并解释为什么 0.675-0.929 的 gradient 不足以在 training-time 产生有效 reward signal。\n\n---\n\n## 小问题（不影响接收）\n\n- Table 2 的 \"Root Cause\" 列措辞偏 editorial（\"Norm mismatch\", \"Gap too small\"）。建议用更技术性的描述。\n- Section 4 \"Checkpoint-level evaluation confirms immediate collapse: ToF=0 from step 500 onward with no stable phase\" — 需要明确这里的 evaluation 是在 truncated 还是 full-length completions 上进行的。\n- 论文提到 \"Code and data will be released upon acceptance\"，但 supplementary materials 中是否包含了 contrastive pairs？review form 中通常需要检查 reproducibility 材料。\n- Related Work 缺少对 DPO/KTO 在 sycophancy calibration 上的讨论——仅在 Section 7 最后一句提及 \"may accommodate d_syc-derived rankings\"，但 Rafailov et al. 2023 和 Ethayarajh et al. 2024 的实际 sycophancy 相关工作未被 review。\n\n---\n\n## 主要优势\n\n1. **Probe reward trap（C2）是干净且新颖的负面结果**：在 SFT（非 GRPO）设置下发现，behavioral death 先于 distributional collapse 1,300 步，且 reward 全程 +0.72——这直接挑战了 entropy-based early stopping 作为 reward hacking safeguard 的有效性。这个 finding 独立于 GRPO confound，有明确的实践价值。\n\n2. **Diagnostic chain 设计（Section 4）结构清晰**：F1a→F1b→F1c→F1d 的递进式排错链——每个配置修复前者的 failure mode 但暴露更深层问题——是优秀的实验叙事，即使受 confound 影响。\n\n3. **异常透明的 limitations 讨论**：论文对 group_size confound、truncation、seed count、ACT comparison 不可归因等问题的 disclosure 水平远超平均，三个 competing hypotheses 的框架也很诚实。但透明度本身不能代替 ablation。\n\n4. **Stubbornness taxonomy（Appendix B）**：181 条 valid-correction response 的手动分析揭示了 5 种 failure mode（deliberation traps 28.7%、surface compliance 24.3% 等），这是有质量的定性证据。\n\n5. **Cross-model d_syc discriminability 验证**：Qwen3-8B (AUROC 0.827) + Llama-3-8B (0.779) 的双模型验证，配合 evidence-strength gradient 和 domain-level 分析，对 d_syc 的 discriminability 建立了 robust 的 evidence base。\n",
  "reviewer_id": "1",
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## 总体评分\n**Overall**: 3.0 / 5（Findings）\n**一句话总结**: 核心发现 probe reward trap（C2）是干净的负面结果，具有实际价值；但 GRPO 相关结论（C1）被 group_size=2 和 80-84% truncation 两个严重 confound 深度污染，削弱了整体贡献。\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2.5/5 | 核心发现 C2（probe trap in SFT）方法论干净，但 C1（GRPO failures）被 group_size=2、truncation 80-84%、LoRA 配置不对称三重 confound 侵蚀；作者虽有 acknowledge 但未做 ablation 来隔离 |\n| Excitement | 3.5/5 | \"Behavioral death precedes distributional collapse by 1,300 steps\" 是新颖且有实践警示价值的发现；但 scope 受限于单模型、2 seeds |\n| Reproducibility | 3.5/5 | 超参数表格较完整（Table 5），但 w₁ 的 diagnostic-driven iteration 过程不可复现；contrastive pairs 用 GPT-4.1 单标注无 IAA |\n| Reviewer Confidence | 4/5 | 熟悉 representation engineering、GRPO、sycophancy calibration 相关文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Group-size=2 confound 未被隔离，C1 贡献几乎无法成立\n\n- 具体位置：Section 2.5（GRPO uses a group size of 2）、Section 6 Competing hypotheses、Limitations\n- 问题：GRPO group_size=2 远低于文献典型值 8-64（论文自引 Shao et al. 2024）。在此配置下，advantage estimator 的 ranking diversity 极低——2 个 completion 之间的 pairwise comparison 本质上是 coin flip 级别的 signal。R₃-only GRPO 同样失败（4/27 checkpoints > vanilla），这恰恰说明 **group_size=2 下任何 scalar reward 都难以工作**，而非 d_syc 特有的问题。论文在 Section 6 提出三个 competing hypotheses (a)(b)(c)，但承认 \"cannot fully distinguish (a) from (b) without a group-size ablation, which we leave to future work\"。问题是：如果 (a) 和 (b) 无法区分，那么 C1 的 contribution statement（\"GRPO formulations fail under our configuration\"）实质上是在报告一个 confounded observation，而非可归因的因果结论。\n- 为什么影响接收：C1 是论文两大 contribution 之一。如果 C1 无法排除 group-size confound，论文实质上只有 C2 一个干净的 contribution。\n- 建议修改方向：(1) 在更小模型（如 Qwen2.5-1.5B）上跑 group_size=8/16 ablation，至少验证 R₃-only GRPO 在正常配置下是否能工作；或 (2) 将 C1 从 contribution 降级为 observational finding，明确标注所有 GRPO 结论均不可归因。\n\n**N2** [critical] 80-84% truncation 使训练时 d_syc 信号接近 chance level，但论文仍以 AUROC 0.827 为前提论证\n\n- 具体位置：Appendix A（\"80-84% truncation of multi-turn responses\"）、Section 4 第 7 段（\"d_syc AUROC drops from 0.76 (full response) to 0.60\"）、Limitations\n- 问题：论文在 Section 3 和 Introduction 中反复强调 d_syc AUROC=0.827，建立 \"discriminability is strong but reward fails\" 的叙事。但 Appendix A 和 Section 4 揭示：在实际训练中，由于 max_completion_length=256 导致 80-84% 的 response 被截断，d_syc AUROC 从 0.76（注意不是 0.827，0.827 是 cross-validated on activations）降至 0.60。AUROC 0.60 仅略好于 random chance（0.50），意味着训练时 reward signal 几乎是 noise。这从根本上动摇了论文的核心叙事：不是 \"high discriminability fails to transfer to reward utility\"，而可能只是 \"truncation destroyed the signal, so there's nothing left to transfer\"。\n- 为什么影响接收：论文的核心论点是 \"discriminability ≠ reward utility\"，但如果训练时 discriminability 本身就被 truncation 摧毁到 0.60，这个 gap 就不再是 semantic 的，而是 engineering 层面的 signal degradation。\n- 建议修改方向：(1) 对 probe reward trap（C2，SFT 设置）重跑 full-length completion 实验——SFT 不受 GRPO memory 约束，可以用更长的 completion；(2) 在论文叙事中明确区分 \"offline discriminability\"（0.827）和 \"training-time discriminability\"（0.60），不要在 abstract/introduction 中以 0.827 作为 reward failure 的前提。\n\n**N3** [critical] ACT vs GRPO 比较缺乏控制，5+ 维度差异使任何对比均不可归因\n\n- 具体位置：Section 6 \"Observational comparison: ACT vs GRPO\"、Table 4、Table 5\n- 问题：论文在 Table 5 中详细列出了 GRPO 和 ACT 的配置差异，但差异远比 acknowledged 的更大：\n  - LoRA α：GRPO=64，ACT=128 → 有效学习率 α/rank = 1.0 vs 2.0，**差 2 倍**\n  - LoRA modules：GRPO=4（q/k/v/o），ACT=7（+ gate/up/down）→ **可训练参数差 ~1.75x**\n  - LoRA dropout：GRPO=0，ACT=0.05\n  - Supervision：per-completion vs per-token\n  - Loss：REINFORCE vs CE+L2\n  论文说 \"included for context, not as controlled comparisons\"（Table 4 footnote ¶），但 Introduction 和 Conclusion 实质上将 ACT 的成功作为 d_syc/GRPO 失败的 foil 来使用，给读者一种 \"representation-based RL fails, token-level SFT works\" 的 takeaway。当 ACT 有 1.75x 参数量和 2x 有效学习率时，它的优势完全可能来自 capacity/optimization 而非方法论差异。\n- 为什么影响接收：如果 ACT 比较不可靠，论文的 narrative 从 \"here's why representation rewards fail and what works instead\" 缩减为 \"here are some negative results under a specific configuration\"。\n- 建议修改方向：(1) 统一 LoRA 配置（α、modules）做至少一组控制实验；(2) 或在叙事中完全去除 ACT 作为 positive contrast 的暗示，仅作为 descriptive observation。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 2 seeds 不足以支撑 GRPO 行为的统计结论\n\n- 具体位置：Section 6（\"We report GRPO results from two random seeds\"）、Limitations\n- 问题：GRPO 的 oscillation pattern、crash depth、cross-seed rank correlation 等分析均基于 n=2。论文承认 \"limited seed count constrains statistical claims\"，但仍报告了 cross-seed rank correlation（ρ≈0.33, n<10 per window），这在 n=2 seeds × <10 checkpoints 下没有统计意义。Figure 3 的 trajectory 比较（2 GRPO seeds vs 1 ACT seed）也不足以建立 systematic pattern。\n- 建议：增加到 3-5 seeds，或删除 cross-seed correlation 分析，仅保留 qualitative description。\n\n**W2** [warning] SyconScore 的 harmonic mean 设计放大了 failure 的表观严重性\n\n- 具体位置：Section 2.5 Eq.(2)、Table 4\n- 问题：SyconScore = harmonic mean(ToF, NoF)，当 ToF=0 时 SyconScore=0，无论 NoF 多高。论文说 arithmetic mean 结果 \"show qualitatively similar patterns and are reported in supplementary materials\"，但主表中 SyconScore=0.000 的视觉冲击力远大于（假设）arithmetic mean 可能给出的 0.498 (=(0+0.995)/2)。对于一篇论证 failure modes 的论文，metric 选择放大了 failure 的呈现，应在主文中同时报告两种 mean。\n- 建议：在 Table 4 中增加 arithmetic mean 列，或至少在 caption 中注明 arithmetic mean 的具体数值。\n\n**W3** [warning] Contrastive pair 单标注源 + 无 IAA\n\n- 具体位置：Section 2.1（\"using GPT-4.1 in a two-stage pipeline\"）、Limitations\n- 问题：181 对 contrastive pairs 由 GPT-4.1 生成并标注 evidence strength，无 human inter-annotator agreement。论文的 d_syc 质量完全依赖这些 pairs 的质量。虽然 automated validation（length difference <10%, shared opening phrase）控制了表层质量，但 semantic validity（特别是 sycophantic vs valid revision 的边界案例）未经人工验证。\n- 建议：报告一个 human evaluation sample（如随机抽 30-50 对由人工判断标注质量）。\n\n**W4** [warning] ACT seed 2 仅 6/16 checkpoints evaluated\n\n- 具体位置：Table 4 footnote ‡\n- 问题：ACT seed 2 标注为 \"ongoing; 6/16 ckpts evaluated, all > vanilla\"。这是一个 incomplete result。如果 ACT seed 2 的后续 10 个 checkpoints 中出现 crash（类似 seed 1 的 checkpoint 4000 dip），结论会受影响。发表时应有完整结果。\n- 建议：完成 ACT seed 2 的全部评估。\n\n**W5** [warning] d_syc 的 \"evidential warrant\" 缺失论证不够严格\n\n- 具体位置：Section 5 最后一段、Section 6 第 1 段\n- 问题：论文反复声称 d_syc \"encodes whether belief changed, not whether it should have\"，这是论文的核心理论解释。但这个 claim 主要基于 observational evidence（d_syc 给 valid revision 和 sycophantic capitulation 相似的 cosine score）。Section 3 的 evidence-strength gradient（weak 0.675 → strong 0.929 AUROC）实际上表明 d_syc **确实** 在某种程度上 encode 了 evidential warrant——强证据下 AUROC 更高，说明方向确实区分了证据质量。这与 \"does not encode whether it should have\" 的 claim 存在张力。\n- 建议：更精确地表述——不是 \"does not encode evidential warrant\"，而是 \"encodes evidential warrant insufficiently for reward contrast\"，并解释为什么 0.675-0.929 的 gradient 不足以在 training-time 产生有效 reward signal。\n\n---\n\n## 小问题（不影响接收）\n\n- Table 2 的 \"Root Cause\" 列措辞偏 editorial（\"Norm mismatch\", \"Gap too small\"）。建议用更技术性的描述。\n- Section 4 \"Checkpoint-level evaluation confirms immediate collapse: ToF=0 from step 500 onward with no stable phase\" — 需要明确这里的 evaluation 是在 truncated 还是 full-length completions 上进行的。\n- 论文提到 \"Code and data will be released upon acceptance\"，但 supplementary materials 中是否包含了 contrastive pairs？review form 中通常需要检查 reproducibility 材料。\n- Related Work 缺少对 DPO/KTO 在 sycophancy calibration 上的讨论——仅在 Section 7 最后一句提及 \"may accommodate d_syc-derived rankings\"，但 Rafailov et al. 2023 和 Ethayarajh et al. 2024 的实际 sycophancy 相关工作未被 review。\n\n---\n\n## 主要优势\n\n1. **Probe reward trap（C2）是干净且新颖的负面结果**：在 SFT（非 GRPO）设置下发现，behavioral death 先于 distributional collapse 1,300 步，且 reward 全程 +0.72——这直接挑战了 entropy-based early stopping 作为 reward hacking safeguard 的有效性。这个 finding 独立于 GRPO confound，有明确的实践价值。\n\n2. **Diagnostic chain 设计（Section 4）结构清晰**：F1a→F1b→F1c→F1d 的递进式排错链——每个配置修复前者的 failure mode 但暴露更深层问题——是优秀的实验叙事，即使受 confound 影响。\n\n3. **异常透明的 limitations 讨论**：论文对 group_size confound、truncation、seed count、ACT comparison 不可归因等问题的 disclosure 水平远超平均，三个 competing hypotheses 的框架也很诚实。但透明度本身不能代替 ablation。\n\n4. **Stubbornness taxonomy（Appendix B）**：181 条 valid-correction response 的手动分析揭示了 5 种 failure mode（deliberation traps 28.7%、surface compliance 24.3% 等），这是有质量的定性证据。\n\n5. **Cross-model d_syc discriminability 验证**：Qwen3-8B (AUROC 0.827) + Llama-3-8B (0.779) 的双模型验证，配合 evidence-strength gradient 和 domain-level 分析，对 d_syc 的 discriminability 建立了 robust 的 evidence base。\n",
    "reviewer_id": "1",
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-22T15:31:51.609845+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3716
}
```

</details>

---


### Tool call

_source line 324 · 2026-05-22T15:31:56.292740+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
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

_source line 325 · 2026-05-22T15:31:56.293213+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 326 · 2026-05-22T15:32:00.421053+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_5/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 327 · 2026-05-22T15:32:00.478125+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 57
}
```

</details>

---


### Assistant

_source line 328 · 2026-05-22T15:32:09.081207+00:00_

审稿完成。已向 Review Director 提交完整审稿意见，核心判断：

- **Overall: 3.0（Findings）**
- **C2（probe reward trap）是干净的贡献**：SFT 设置下 behavioral death 先于 distributional collapse 1,300 步，独立于 GRPO confound，对 entropy-based early stopping 的有效性有直接实践警示。
- **C1（GRPO failures）被严重 confound**：group_size=2、80-84% truncation（训练时 AUROC 降至 0.60）、LoRA 配置不对称三重因素叠加，使得所有 GRPO 和 ACT 对比结论不可归因。
- **3 个 Must-Fix**：group-size ablation 缺失、truncation 摧毁信号但叙事仍以 AUROC 0.827 为前提、ACT 比较不受控（1.75x 参数 + 2x 有效学习率）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1"
}
```

</details>

---


## Round 10

## Round 10

4 recorded events


### User

_source line 329 · 2026-05-22T15:34:22.192693+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整初审意见。请逐条回应：对每个 Must-Fix 和 Should-Fix，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

# Reviewer 2 审稿意见：新颖性/完整性

## 总体评分
**Overall**: 3.0 / 5（Findings）
**一句话总结**: Probe reward trap (C2) 是一个有实证支撑的 clean finding，但核心洞察本质上是 Goodhart's law 在表征奖励上的具体化，实验范围窄（单模型、group size=2 的 GRPO 混淆因子），泛化声明超出证据边界，整体贡献处于 Findings 水平。

## Must-Fix 问题

**N1** [critical] 核心新颖性不足：Probe reward trap 是 Goodhart's law 的特例，增量贡献需更清晰界定

- 论文的核心发现——用 frozen probe 做 reward signal 会导致 reward hacking——是 Goodhart's law 在表征奖励上的直接实例化。d_syc 无法区分 warranted revision 和 sycophantic capitulation 这一核心限制，在概念上可从 prior work 直接预期。
- 建议：重新定位核心贡献为"量化了 behavioral death 与 distributional collapse 的 temporal decoupling 及其对 monitoring 的具体影响"。

**N2** [critical] GRPO 实验（C1）的 group size=2 混淆因子使该贡献缺乏说服力

- group_size=2 低于常规范围一个数量级。R3-only GRPO 同样失败（4/27）进一步支持 hypothesis (b)。C1 可能仅是 group size 不足的 artifact。
- 建议：至少在一个 group size（如 8 或 16）上复现；或将 C1 降级为 preliminary observation。

**N3** [critical] 标题和泛化声明超出证据范围

- 标题 "The Probe Reward Trap" 暗示通用现象，但证据来自单一模型、单一实验、单一方向。1,300-step lag 仅在一个 run 上观察到。
- 建议：在 Llama-3-8B 上复现 SFT probe trap；或将标题限定为 case study。

## Should-Fix 问题

**W1** [warning] Wu & Tang (2026) 对比缺乏定量分析
- 从未定量比较 d_syc 与 Wu & Tang 方向的几何可分性差异。

**W2** [warning] CRAFT/Latent-GRPO/SMART 讨论过于浅表
- SMART 也处理 sycophancy 且成功，直接挑战论文 "sycophancy breaks geometric separability" 的论断。

**W3** [warning] Stubbornness taxonomy 分析深度不足
- 缺少各类随 step 的变化动态、与其他 reward hacking 失败模式的对比。

**W4** [warning] "negative result" 与 "general principle" 定位模糊
- 两种定位都不完全满足，需明确选择。

---

请逐条标注 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 330 · 2026-05-22T15:35:38.413361+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 对 Reviewer 2 意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[REBUT] R2-N1: \"Probe reward trap 是 Goodhart's law 的特例，新颖性不足\"**\n\nR2 的概括有道理但过于笼统。Goodhart's law 预测 \"proxy reward 会被 overoptimize\"，但它不预测以下 **三个具体特征**，而这些才是 C2 的实质贡献：\n\n1. **Temporal decoupling 的量化**：behavioral death（ToF=0）在 step 500 发生，distributional collapse（entropy < 0.1）在 step ~1840 发生，1,300-step lag（Table 3, Figure 2）。这不是 Goodhart's law 的推论——Goodhart 不对 behavioral vs distributional failure 的时序关系做预测。\n2. **Reward 全程 healthy**：reward 平均 +0.72 从 step 500 到 step 2000 不变（Table 3），说明标准的 reward-based monitoring 也无法检测失败。这是对 entropy-based early stopping（Casper et al., 2023）的具体反例，不是泛泛的 Goodhart 实例。\n3. **SFT + stopped gradient 设置**：probe trap 在没有 RL exploration dynamics 的情况下出现（Section 5），排除了 GRPO/REINFORCE 特有的 exploitation pathway。多数 Goodhart's law 实例讨论的是 RL 中的 reward hacking，SFT 下的 probe trap 是不同的机制。\n\n但我同意 R2 的建议方向：论文应更清晰地将核心贡献定位为 \"temporal decoupling 的量化及其 monitoring 盲区影响\"，而非暗示发现了全新类别的 failure mode。**论文目前的 framing 确实有过度概括的倾向**——Introduction 的 \"we discover the probe reward trap\" 可以更精确地表述为 \"we quantify a temporal decoupling between behavioral and distributional failure under probe-based rewards\"。\n\n---\n\n**[AGREE] R2-N2: \"GRPO group_size=2 confound 使 C1 缺乏说服力\"**\n\n完全同意。这与我的 N1 一致。补充两点：\n\n1. R₃-only GRPO 的失败（4/27 > vanilla）是关键证据——它**不含 d_syc**，其失败只能归因于 (b) group_size 不足或 (c) scalar per-completion RL 不适合 sycophancy calibration。论文在 Section 6 Competing hypotheses 中也承认无法区分 (a) 和 (b)。\n2. 论文目前将 C1 列在 Introduction 的 contribution list 中，与 C2 并列呈现。如果无法做 group_size ablation，C1 应降级为 \"observational finding under a specific configuration\" 而非 contribution。\n\n---\n\n**[REBUT] R2-N3: \"标题和泛化声明超出证据范围，需在 Llama-3-8B 上复现 SFT probe trap\"**\n\n部分同意标题问题，但不同意必须在 Llama 上复现才能成立。\n\n反驳理由：\n1. Probe reward trap（C2）的核心机制是 **d_syc 不 encode evidential warrant**——valid revision 和 sycophantic capitulation 在 d_syc 上产生相似投影。这个几何性质已在两个模型上验证：Qwen3-8B AUROC 0.827、Llama-3-8B AUROC 0.779（Table 1），且两者 evidence-strength gradient 一致（Section 3）。既然 d_syc 在 Llama 上具有相同的 discriminability profile 和相同的 semantic limitation（不区分 warrant），没有理由认为 probe trap 会在 Llama 上消失。\n2. 1,300-step lag 的 **具体数字** 确实只来自一个 run（exp-008v3），这个数字本身不应被泛化。但 \"behavioral death 先于 distributional collapse\" 的 **定性结论** 由机制驱动：当 probe reward 奖励 non-flipping 而 entropy loss 尚未收敛时，必然出现 temporal gap。\n\n但我同意以下调整：\n- 标题可加限定，如 \"...in Sycophancy Calibration: A Case Study on Qwen3-8B\"\n- Abstract 中 \"1,300-step lag\" 应标注为 \"under our configuration\" 而非暗示普遍数字\n- 至少应在 Limitations 中明确讨论 single-model single-run 的限制\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: \"Wu & Tang (2026) 对比缺乏定量分析\"**\n\n同意。论文在 Section 6 引用 Wu & Tang (2026) 论证 \"where the behavior to suppress is geometrically distinct from the behavior to preserve\"，但仅是 narrative-level 引用。未报告：(1) reward hacking direction 的 cosine gap vs d_syc 的 cosine gap；(2) 两类 direction 的 intra-class vs inter-class separation。这个 quantitative comparison 对于论文的核心理论解释（geometric entanglement 导致 failure）是必要的 evidence。\n\n---\n\n**[AGREE] R2-W2: \"SMART 讨论过于浅表，直接挑战论文论断\"**\n\n这是 R2 意见中最有力的一条。论文在 Related Work (Section 7) 写道：\n\n> \"SMART (Beigi et al., 2025) applies per-step process rewards with MCTS for sycophancy. These methods succeed because target and suppressed behaviors are geometrically distinct; sycophancy breaks this condition (§4).\"\n\n这里有**逻辑矛盾**：如果 sycophancy breaks geometric separability，SMART 怎么能在 sycophancy 上成功？论文声称 SMART 成功是因为 \"behaviors are geometrically distinct\"，但 SMART 处理的就是 sycophancy——跟论文自己处理的是同一个 target behavior。\n\n合理的解释可能是：SMART 通过 per-step process reward 将 sycophancy 分解为更细粒度的 decision points，在每个 step 上 target 和 suppressed behavior 可能是几何可分的，即使在 completion-level 上不可分。但论文没有这样论述，而是把 SMART 归入 \"behaviors are geometrically distinct\" 一类，回避了矛盾。\n\n这确实削弱了论文 \"sycophancy calibration is fundamentally hard for representation-based approaches\" 的泛化声明。\n\n---\n\n**[REBUT] R2-W3: \"Stubbornness taxonomy 分析深度不足\"**\n\n部分不同意。对于一篇 8-page paper 的 appendix 内容，当前的 taxonomy（Appendix B，181 条 response 的 5 类手动分析）已提供了有质量的定性 evidence。R2 要求的 temporal dynamics（各类随 step 变化）和 cross-failure-mode comparison 虽有价值，但：\n\n1. Temporal dynamics 需要在多个 checkpoints 上做 181×N 条 response 的手动标注，工作量不成比例。\n2. 与其他 reward hacking failure modes 的对比超出了本文 scope——论文关注的是 sycophancy calibration 的特定 failure，不是 reward hacking taxonomy。\n\n现有 taxonomy 的核心发现——76.8% 的 failure 是模型调节 refusal style 而非 acceptance rate（Appendix B 最后一段）——已足够支撑 \"probe reward optimizes surface markers rather than epistemic calibration\" 的论点。\n\n---\n\n**[AGREE] R2-W4: \"'Negative result' 与 'general principle' 定位模糊\"**\n\n同意。论文在两个定位之间摇摆：\n- 作为 negative result：C2（probe trap）是干净的，但需要更多 models/seeds 来建立 robustness\n- 作为 general principle：Section 6 的理论分析（geometric entanglement）试图推广，但证据不足以支撑\n\n这与我的整体评估一致：论文应更明确地选择 negative result 定位，以 \"quantified temporal decoupling under probe-based rewards for sycophancy on Qwen3-8B\" 为核心，而非暗示发现了通用的 representation-reward failure principle。Section 6 的 geometric entanglement 讨论可以保留为 hypothesis / future direction，但不应作为论文 takeaway。\n",
  "reviewer_id": "1",
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 对 Reviewer 2 意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[REBUT] R2-N1: \"Probe reward trap 是 Goodhart's law 的特例，新颖性不足\"**\n\nR2 的概括有道理但过于笼统。Goodhart's law 预测 \"proxy reward 会被 overoptimize\"，但它不预测以下 **三个具体特征**，而这些才是 C2 的实质贡献：\n\n1. **Temporal decoupling 的量化**：behavioral death（ToF=0）在 step 500 发生，distributional collapse（entropy < 0.1）在 step ~1840 发生，1,300-step lag（Table 3, Figure 2）。这不是 Goodhart's law 的推论——Goodhart 不对 behavioral vs distributional failure 的时序关系做预测。\n2. **Reward 全程 healthy**：reward 平均 +0.72 从 step 500 到 step 2000 不变（Table 3），说明标准的 reward-based monitoring 也无法检测失败。这是对 entropy-based early stopping（Casper et al., 2023）的具体反例，不是泛泛的 Goodhart 实例。\n3. **SFT + stopped gradient 设置**：probe trap 在没有 RL exploration dynamics 的情况下出现（Section 5），排除了 GRPO/REINFORCE 特有的 exploitation pathway。多数 Goodhart's law 实例讨论的是 RL 中的 reward hacking，SFT 下的 probe trap 是不同的机制。\n\n但我同意 R2 的建议方向：论文应更清晰地将核心贡献定位为 \"temporal decoupling 的量化及其 monitoring 盲区影响\"，而非暗示发现了全新类别的 failure mode。**论文目前的 framing 确实有过度概括的倾向**——Introduction 的 \"we discover the probe reward trap\" 可以更精确地表述为 \"we quantify a temporal decoupling between behavioral and distributional failure under probe-based rewards\"。\n\n---\n\n**[AGREE] R2-N2: \"GRPO group_size=2 confound 使 C1 缺乏说服力\"**\n\n完全同意。这与我的 N1 一致。补充两点：\n\n1. R₃-only GRPO 的失败（4/27 > vanilla）是关键证据——它**不含 d_syc**，其失败只能归因于 (b) group_size 不足或 (c) scalar per-completion RL 不适合 sycophancy calibration。论文在 Section 6 Competing hypotheses 中也承认无法区分 (a) 和 (b)。\n2. 论文目前将 C1 列在 Introduction 的 contribution list 中，与 C2 并列呈现。如果无法做 group_size ablation，C1 应降级为 \"observational finding under a specific configuration\" 而非 contribution。\n\n---\n\n**[REBUT] R2-N3: \"标题和泛化声明超出证据范围，需在 Llama-3-8B 上复现 SFT probe trap\"**\n\n部分同意标题问题，但不同意必须在 Llama 上复现才能成立。\n\n反驳理由：\n1. Probe reward trap（C2）的核心机制是 **d_syc 不 encode evidential warrant**——valid revision 和 sycophantic capitulation 在 d_syc 上产生相似投影。这个几何性质已在两个模型上验证：Qwen3-8B AUROC 0.827、Llama-3-8B AUROC 0.779（Table 1），且两者 evidence-strength gradient 一致（Section 3）。既然 d_syc 在 Llama 上具有相同的 discriminability profile 和相同的 semantic limitation（不区分 warrant），没有理由认为 probe trap 会在 Llama 上消失。\n2. 1,300-step lag 的 **具体数字** 确实只来自一个 run（exp-008v3），这个数字本身不应被泛化。但 \"behavioral death 先于 distributional collapse\" 的 **定性结论** 由机制驱动：当 probe reward 奖励 non-flipping 而 entropy loss 尚未收敛时，必然出现 temporal gap。\n\n但我同意以下调整：\n- 标题可加限定，如 \"...in Sycophancy Calibration: A Case Study on Qwen3-8B\"\n- Abstract 中 \"1,300-step lag\" 应标注为 \"under our configuration\" 而非暗示普遍数字\n- 至少应在 Limitations 中明确讨论 single-model single-run 的限制\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: \"Wu & Tang (2026) 对比缺乏定量分析\"**\n\n同意。论文在 Section 6 引用 Wu & Tang (2026) 论证 \"where the behavior to suppress is geometrically distinct from the behavior to preserve\"，但仅是 narrative-level 引用。未报告：(1) reward hacking direction 的 cosine gap vs d_syc 的 cosine gap；(2) 两类 direction 的 intra-class vs inter-class separation。这个 quantitative comparison 对于论文的核心理论解释（geometric entanglement 导致 failure）是必要的 evidence。\n\n---\n\n**[AGREE] R2-W2: \"SMART 讨论过于浅表，直接挑战论文论断\"**\n\n这是 R2 意见中最有力的一条。论文在 Related Work (Section 7) 写道：\n\n> \"SMART (Beigi et al., 2025) applies per-step process rewards with MCTS for sycophancy. These methods succeed because target and suppressed behaviors are geometrically distinct; sycophancy breaks this condition (§4).\"\n\n这里有**逻辑矛盾**：如果 sycophancy breaks geometric separability，SMART 怎么能在 sycophancy 上成功？论文声称 SMART 成功是因为 \"behaviors are geometrically distinct\"，但 SMART 处理的就是 sycophancy——跟论文自己处理的是同一个 target behavior。\n\n合理的解释可能是：SMART 通过 per-step process reward 将 sycophancy 分解为更细粒度的 decision points，在每个 step 上 target 和 suppressed behavior 可能是几何可分的，即使在 completion-level 上不可分。但论文没有这样论述，而是把 SMART 归入 \"behaviors are geometrically distinct\" 一类，回避了矛盾。\n\n这确实削弱了论文 \"sycophancy calibration is fundamentally hard for representation-based approaches\" 的泛化声明。\n\n---\n\n**[REBUT] R2-W3: \"Stubbornness taxonomy 分析深度不足\"**\n\n部分不同意。对于一篇 8-page paper 的 appendix 内容，当前的 taxonomy（Appendix B，181 条 response 的 5 类手动分析）已提供了有质量的定性 evidence。R2 要求的 temporal dynamics（各类随 step 变化）和 cross-failure-mode comparison 虽有价值，但：\n\n1. Temporal dynamics 需要在多个 checkpoints 上做 181×N 条 response 的手动标注，工作量不成比例。\n2. 与其他 reward hacking failure modes 的对比超出了本文 scope——论文关注的是 sycophancy calibration 的特定 failure，不是 reward hacking taxonomy。\n\n现有 taxonomy 的核心发现——76.8% 的 failure 是模型调节 refusal style 而非 acceptance rate（Appendix B 最后一段）——已足够支撑 \"probe reward optimizes surface markers rather than epistemic calibration\" 的论点。\n\n---\n\n**[AGREE] R2-W4: \"'Negative result' 与 'general principle' 定位模糊\"**\n\n同意。论文在两个定位之间摇摆：\n- 作为 negative result：C2（probe trap）是干净的，但需要更多 models/seeds 来建立 robustness\n- 作为 general principle：Section 6 的理论分析（geometric entanglement）试图推广，但证据不足以支撑\n\n这与我的整体评估一致：论文应更明确地选择 negative result 定位，以 \"quantified temporal decoupling under probe-based rewards for sycophancy on Qwen3-8B\" 为核心，而非暗示发现了通用的 representation-reward failure principle。Section 6 的 geometric entanglement 讨论可以保留为 hypothesis / future direction，但不应作为论文 takeaway。\n",
    "reviewer_id": "1",
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 331 · 2026-05-22T15:35:43.899547+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5486
}
```

</details>

---


### Assistant

_source line 332 · 2026-05-22T15:35:55.043313+00:00_

交叉回应已提交给 Director。

总结：对 R2 的 7 条意见，我标注了 **3 条 AGREE（N2, W1, W2, W4）和 3 条 REBUT（N1, N3, W3）**：

- **N1（Goodhart 特例）**：REBUT——temporal decoupling 的量化、reward 全程 healthy、SFT 设置独立于 RL 这三点超出了 Goodhart's law 的泛泛预测，但同意论文 framing 应更精确
- **N2（group_size confound）**：AGREE——与我的 N1 完全一致
- **N3（标题过度泛化）**：REBUT——d_syc 的几何性质已在双模型验证，机制推理支持 probe trap 的可泛化性；但同意标题和 abstract 应加 scope 限定
- **W1（Wu & Tang 缺定量）**：AGREE
- **W2（SMART 矛盾）**：AGREE——Related Work 中关于 SMART 的表述存在逻辑矛盾，是 R2 最有力的一条
- **W3（Taxonomy 深度不足）**：REBUT——在 8-page paper 的 appendix 范围内已足够
- **W4（定位模糊）**：AGREE——应明确选择 negative result 定位

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1"
}
```

</details>

---


## Round 11

## Round 11

70 recorded events


### User

_source line 333 · 2026-05-24T09:48:21.982966+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性 + 实验设计 + 统计有效性**的审查。

## Venue 信息
- **目标**: EMNLP 2026（通过 ARR 统一审稿）
- **类型**: Long Paper
- **正文页数限制**: 严格 8 页（参考文献不计入；Limitations 和 Ethics 不计入，前提是不包含过多额外内容）
- **模板**: ACL (`\usepackage[hyperref]{acl}`)
- **匿名规则**: Double-blind（禁止自引暴露身份）
- **Deadline**: ARR May 2026 cycle (2026-05-25)
- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

## 论文路径
- LaTeX: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/submitted.pdf`
- Section 文件在 `docs/paper/sections/` 目录下

## 你的审查侧重

### 1. 方法论严谨性
- d_syc 方向提取方法是否规范（contrastive pairs 构造、style control、layer selection）
- 181 对 contrastive pairs 全部由 GPT-4.1 生成——是否存在 annotation bias？evidence strength 标注是否可信（无 IAA/human validation）？
- 5-fold CV AUROC 报告是否规范？标准差 vs CI 的选择是否合理？
- SyconScore harmonic mean 设计是否合理？ToF=0 时直接归零是否过于严苛？是否应同时报告 arithmetic mean？

### 2. 实验设计
- GRPO group_size=2：是否构成致命的替代解释？gs=8 ablation 是否充分 rule out hypothesis (b)？
- 256-token truncation：AUROC 从 0.827 降至 0.60，这对 C1（cosine failure chain）的结论有何影响？论文是否充分区分了 offline vs training-time discriminability？
- ACT vs GRPO 对比：LoRA α (64 vs 128)、modules (4 vs 7)、dropout (0 vs 0.05) 等多维度不同——reduced-LoRA ablation 是否真正隔离了 supervision granularity？
- R₃-only GRPO 仅 4/28 > vanilla：但 group_size=2 条件下这是否是 GRPO 配置问题而非 sycophancy 本身的问题？
- ACT seed 2 评估完整度（论文报告了多少 checkpoints？是否存在 incomplete evidence）
- Cross-seed 分析的统计功效（n=2 seeds 的 rank correlation 是否有意义？）

### 3. 统计报告
- 所有 p 值、CI、效应量的报告是否规范
- 训练曲线的噪声/方差是否充分报告
- Held-out 验证的设计和报告是否充分

### 4. 可复现性
- 超参数是否完整报告（Table 5 / Appendix A）
- 实验代码/数据可用性是否提及

请按以下格式输出审稿意见：

```
## Summary
[2-3 句论文概述]

## Strengths
[S1] ...
[S2] ...

## Weaknesses
[W1] [severity: critical/warning/minor] ...
[W2] ...

## Questions
[Q1] ...

## Missing References
[如有]

## Scores
- Soundness: X/5
- Presentation: X/5
- Contribution: X/5
- Overall: X (按 EMNLP 2026 评分标准)
- Confidence: X/5
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 334 · 2026-05-24T09:48:32.503226+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
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

_source line 335 · 2026-05-24T09:48:32.553994+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 336 · 2026-05-24T09:48:36.877837+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 337 · 2026-05-24T09:48:39.791403+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/submitted.pdf",
  "project": "contrastive_entrain_calib",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/submitted.pdf",
    "project": "contrastive_entrain_calib",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 338 · 2026-05-24T09:48:43.911733+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 339 · 2026-05-24T09:48:44.313786+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I've found relevant information about ACL ARR 2026 reviewer guidelines and review form criteria. Here's what the search results show:

## Review Form Criteria

For Main papers, reviewers should evaluate based on various criteria, while for Findings pape
…[truncated 1345 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7435
}
```

</details>

---


### Tool result

_source line 340 · 2026-05-24T09:48:45.524480+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 411.8}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 392.3}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 443.5}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 441.4}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 438.8}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 489.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 456.9}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 497.8}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_ima
…[truncated 548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 5733
}
```

</details>

---


### Tool result

_source line 341 · 2026-05-24T09:48:45.525058+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 1613
}
```

</details>

---


### Tool call

_source line 342 · 2026-05-24T09:48:55.830852+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5 or other), and descriptions of each score level. Include: Soundness, Excitement/Novelty, Reproducibility, Overall Assessment, Confidence, and any other dimensions. List each dimension with its full scoring rubric."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5 or other), and descriptions of each score level. Include: Soundness, Excitement/Novelty, Reproducibility, Overall Assessment, Confidence, and any other dimensions. List each dimension with its full scoring rubric."
  }
}
```

</details>

---


### Tool call

_source line 343 · 2026-05-24T09:48:56.326279+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 344 · 2026-05-24T09:48:57.143749+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 817
}
```

</details>

---


### Tool call

_source line 345 · 2026-05-24T09:48:57.194538+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 346 · 2026-05-24T09:48:57.800987+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 606
}
```

</details>

---


### Tool call

_source line 347 · 2026-05-24T09:48:57.901777+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 348 · 2026-05-24T09:48:58.353177+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 349 · 2026-05-24T09:48:58.786717+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 350 · 2026-05-24T09:48:59.750586+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1848
}
```

</details>

---


### Tool result

_source line 351 · 2026-05-24T09:49:02.698378+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4345
}
```

</details>

---


### Tool result

_source line 352 · 2026-05-24T09:49:03.004199+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4217
}
```

</details>

---


### Tool result

_source line 353 · 2026-05-24T09:49:04.519153+00:00_

# ACL Rolling Review Form Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## 2. **Soundness**
Scale: 1-5 (with .5 increments)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. **Excitement**
Scale: 1-5 (with .5 increments)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me."
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

## 4. **Overall Assessment**
Scale: 1-5 (with .5 increments)
- **5**: "Consider for Award: I think this paper could be considered for an outstanding paper award."
- **4.5**: "Borderline Award"
- **4**: "Conference: I think this paper could be accepted to an *ACL conference."
- **3.5**: "Borderline Conference"
- **3**: "Findings: I think this paper could be accepted to the Findings of the ACL."
- **2.5**: "Borderline Findings"
- **2**: "Resubmit next cycle: I think this paper needs substantial revisions."
- **1.5**: "Resubmi
…[truncated 1902 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8688
}
```

</details>

---


### Tool call

_source line 354 · 2026-05-24T09:49:10.717070+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 355 · 2026-05-24T09:49:11.722856+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 356 · 2026-05-24T09:49:11.723638+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 357 · 2026-05-24T09:49:12.227036+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 358 · 2026-05-24T09:49:13.287835+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1564
}
```

</details>

---


### Tool result

_source line 359 · 2026-05-24T09:49:13.290037+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1062
}
```

</details>

---


### Tool call

_source line 360 · 2026-05-24T09:49:13.440820+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 361 · 2026-05-24T09:49:14.500423+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1059
}
```

</details>

---


### Tool call

_source line 362 · 2026-05-24T09:49:14.500843+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 363 · 2026-05-24T09:49:14.652268+00:00_

Image file is empty: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images/submitted_p10.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 364 · 2026-05-24T09:49:15.206065+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/submitted.pdf",
  "project": "contrastive_entrain_calib",
  "pages": "11",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/submitted.pdf",
    "project": "contrastive_entrain_calib",
    "pages": "11",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 365 · 2026-05-24T09:49:15.306918+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 53.3}], \"total_pages\": 11, \"rendered_pages\": 1, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 366 · 2026-05-24T09:49:22.730597+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-24T09:49:23.133024+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 368 · 2026-05-24T09:49:23.133383+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 369 · 2026-05-24T09:49:23.183814+00:00_

1	\documentclass[11pt,a4paper]{article}
2	\usepackage[hyperref]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{graphicx}
10	\usepackage{xcolor}
11	\usepackage{subcaption}
12	
13	\newcommand{\dsyc}{d_{\text{syc}}}
14	\newcommand{\tof}{\text{ToF}}
15	\newcommand{\nof}{\text{NoF}}
16	\newcommand{\sycon}{\textsc{SyconScore}}
17	\newcommand{\rone}{R_1}
18	\newcommand{\rthree}{R_3}
19	
20	\title{The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\begin{abstract}
28	\input{sections/abstract}
29	\end{abstract}
30	
31	\input{sections/introduction}
32	
33	\input{sections/framework}
34	
35	\input{sections/direction_quality}
36	
37	\input{sections/cosine_failure}
38	
39	\input{sections/probe_trap}
40	
41	\input{sections/discussion}
42	
43	\input{sections/related_work}
44	
45	\input{sections/conclusion}
46	
47	\section*{Limitations}
48	\input{sections/limitations}
49	
50	\bibliography{references}
51	
52	\appendix
53	\input{sections/appendix}
54	
55	\end{document}
56	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 370 · 2026-05-24T09:49:30.208286+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 371 · 2026-05-24T09:49:30.309052+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/direction_quality.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/probe_trap.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/limitations.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-24T09:49:38.955077+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 373 · 2026-05-24T09:49:39.006170+00:00_

1	We quantify a temporal decoupling we call the \emph{probe reward trap}: when a frozen linear probe on a contrastive sycophancy direction ($\dsyc$, cross-validated AUROC $0.827$ on Qwen3-8B, $0.779$ on Llama-3-8B) is used as an SFT training signal, behavioral death (true-positive flip rate $= 0$) occurs within 500 steps while generation entropy remains healthy (0.70). In our experiments, the resulting 1{,}300-step lag before distributional collapse means that entropy monitoring---the most common safeguard against reward hacking---misses the failure entirely. Because the trap arises under SFT with stopped gradients, it is independent of RL optimization dynamics, revealing a semantic limitation of the direction itself: $\dsyc$ encodes \emph{whether} belief changed, not \emph{whether it should have}. The failure extends beyond probe rewards: all $\dsyc$-based GRPO formulations collapse, and even behavioral-reward-only GRPO exceeds vanilla at only 4/31 checkpoints, while dense per-token SFT succeeds at every checkpoint (47/47). A LoRA-controlled ablation isolates supervision granularity---not adapter capacity or group size---as the primary factor, suggesting that per-completion scalar rewards compress away the token-level information needed for sycophancy calibration.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 374 · 2026-05-24T09:49:39.861389+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex"
  }
}
```

</details>

---


### Tool result

_source line 375 · 2026-05-24T09:49:39.912156+00:00_

1	\section{Experimental Framework}
2	\label{sec:framework}
3	
4	\subsection{Direction Extraction}
5	\label{ssec:extraction}
6	
7	We extract a linear sycophancy direction $\dsyc$ from the residual stream using contrastive activation pairs: a \emph{valid correction} (warranted belief revision under strong evidence) and a \emph{sycophantic capitulation} (unwarranted concession under social pressure).
8	We construct 181 contrastive pairs using GPT-4.1 \citep{openai2025gpt41} in a two-stage pipeline: skeleton generation followed by 3-turn dialogue completion.
9	Style matching is enforced by automated validation (response length difference ${<}10\%$, shared opening phrase ${\geq}2$ words), with up to 3 retries per pair; 19 of 200 initial pairs were discarded for failing validation.
10	Evidence strength is annotated at three levels: \emph{weak} (75 pairs; personal memory or opinion), \emph{medium} (54 pairs; brief source citation), and \emph{strong} (52 pairs; authoritative source with detailed data).
11	From the 181 paired examples (362 activations total), we compute the mean difference at target layer $\ell$:
12	\begin{equation}
13	\label{eq:dsyc}
14	\dsyc = \frac{1}{N}\sum_{i=1}^{N}\left(\mathbf{h}^{+}_i - \mathbf{h}^{-}_i\right)
15	\end{equation}
16	where $\mathbf{h}^{+}_i$ and $\mathbf{h}^{-}_i$ are residual-stream activations for the $i$-th valid and sycophantic response.
17	The target layer is selected by 5-fold cross-validated AUROC; on Qwen3-8B this yields layer 19 with AUROC $0.827 \pm 0.028$ (5-fold CV).
18	
19	\subsection{Reward Formulations}
20	\label{ssec:reward}
21	
22	Three formulations translate $\dsyc$ into a direction-based signal $\rone$.
23	For F1 and F3, $\rone$ enters as part of a GRPO \citep{shao2024grpo} reward $R = w_1 \cdot \rone + w_3 \cdot \rthree$, where $\rthree$ is a behavioral component (DeBERTa NLI classifier scoring consistency with the ground-truth answer).
24	\begin{itemize}
25	\item[\textbf{F1}] \textbf{Cosine projection} with four var
…[truncated 2967 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 376 · 2026-05-24T09:49:40.123597+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/direction_quality.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/direction_quality.tex"
  }
}
```

</details>

---


### Tool result

_source line 377 · 2026-05-24T09:49:40.196834+00:00_

1	\section{Direction Discriminability}
2	\label{sec:direction_quality}
3	
4	Before evaluating $\dsyc$ as a reward signal (\S\ref{sec:cosine_failure}--\S\ref{sec:probe_trap}), we first establish that it captures a genuine sycophancy-related signal in the residual stream.
5	If the direction failed to discriminate sycophantic from non-sycophantic activations, downstream reward failures would be trivially explained by poor direction quality rather than by a fundamental gap between discriminability and reward utility.
6	We evaluate discriminability along five axes: cross-validated classification accuracy, evidence-strength stratification, cross-model transfer, training stability, and probe ablation.
7	Figure~\ref{fig:direction_quality} summarizes the per-layer AUROC profiles for both models.
8	
9	\paragraph{Qwen3-8B layer-wise discriminability.}
10	We evaluate $\dsyc$ via 5-fold cross-validated AUROC on 181 style-controlled contrastive pairs (\S\ref{ssec:extraction}).
11	The direction achieves AUROC $0.827 \pm 0.028$ (5-fold CV) at its best layer (L19).
12	Discriminability emerges gradually across depth: layers L0--L8 perform near chance, statistical significance ($p < 0.01$) first appears at L16, and performance peaks at L19.
13	This gradual emergence, with the peak in the upper third of the network, suggests that sycophancy-relevant information is encoded as a late-stage representation rather than an input-level confound.
14	The direction also captures evidential granularity.
15	AUROC rises monotonically from 0.675 on weak-evidence pairs to 0.883 on medium and 0.929 on strong pairs, consistent with stronger evidence producing more behaviorally distinct responses.
16	
17	\paragraph{Cross-model generalization.}
18	To rule out that these results are specific to Qwen3-8B's representation geometry, we repeat the full extraction and evaluation pipeline on Llama-3-8B-Instruct \citep{grattafiori2024llama3}.
19	Table~\ref{tab:cross_model} compares the two models.
20	Llama-3-8B 
…[truncated 3540 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 73
}
```

</details>

---


### Tool call

_source line 378 · 2026-05-24T09:49:40.574112+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex"
  }
}
```

</details>

---


### Tool result

_source line 379 · 2026-05-24T09:49:40.574512+00:00_

1	\section{Cosine \texorpdfstring{$\rone$}{R1}: Structural Failure}
2	\label{sec:cosine_failure}
3	
4	During GRPO training, 256-token truncation reduces $\dsyc$ AUROC from 0.827 to approximately 0.60---the optimizer works with a substantially weaker signal than the offline metrics suggest.
5	We test whether even this degraded discriminability translates into a viable reward through four configurations that form a diagnostic chain (Table~\ref{tab:cosine_chain}): each resolves the failure mode of its predecessor but exposes a deeper limitation.
6	
7	\begin{table}[t]
8	\centering
9	\caption{Cosine $\rone$ failure chain on Qwen3-8B (LoRA rank$=$64, GRPO with $R = w_1 \cdot \rone + w_3 \cdot \rthree$).}
10	\label{tab:cosine_chain}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{@{}lllll@{}}
13	\toprule
14	Config & $\rone$ Formula & $w_1$ & Outcome & Root Cause \\
15	\midrule
16	F1a & $\tanh(\mathbf{h}\cdot\dsyc/20)$ & 0.25 & Gate saturation & Norm mismatch \\
17	F1b & $\cos(\mathbf{h},\, \dsyc)$ & 0.25 & $\rone \approx 0$ & Gap too small \\
18	F1c & +recalibration & 0.25 & Mode collapse & Reward discontinuity \\
19	F1d & $5\cos(\mathbf{h},\, \dsyc)$ & 0.40 & Mode collapse & $\rthree$ saturation \\
20	\bottomrule
21	\end{tabular}}
22	\end{table}
23	
24	The diagnostic chain begins with a norm mismatch.
25	F1a's dot-product formulation ($\rone = \tanh(\mathbf{h} \cdot \dsyc / 20)$) saturates because residual-stream norms exceed the direction norm by $100$--$1{,}200{\times}$, zeroing the gradient by step 955.
26	Cosine similarity (F1b) eliminates this norm dependence but reveals a second problem: the gap between valid and sycophantic cosines averages only 0.098---too narrow for meaningful reward contrast.
27	Recalibration (F1c, \S\ref{ssec:recalib}) widens the gap (offline AUROC rises to 0.910) but introduces a third: each recalibration event creates a reward discontinuity that destabilizes advantage estimates, collapsing entropy to 0.069 within 300 steps.
28	Amplificati
…[truncated 1319 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 380 · 2026-05-24T09:49:40.675070+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/probe_trap.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/probe_trap.tex"
  }
}
```

</details>

---


### Tool result

_source line 381 · 2026-05-24T09:49:40.675598+00:00_

1	\section{The Probe Reward Trap}
2	\label{sec:probe_trap}
3	
4	The cosine formulations fail on signal magnitude; a natural response is to discretize.
5	Training a logistic probe on $\dsyc$ and thresholding its output yields $\rone = \mathbb{I}[P(\text{syc} \mid \mathbf{h}) < 0.5]$ (F2 in \S\ref{ssec:reward}).
6	We show that this discretization sidesteps the magnitude problem but creates a qualitatively worse failure.
7	Both probe experiments use SFT rather than GRPO (\S\ref{ssec:reward}); the trap is therefore independent of GRPO's optimization dynamics.
8	
9	\paragraph{Differentiable probe: gradient gaming.}
10	Without stop-gradient (exp-008), the policy discovers within ${\sim}30$ steps that shifting activations away from the sycophancy cluster maximizes $\rone$ regardless of response content, producing an inverted profile ($\tof = 0.978$, $\nof = 0.006$).
11	This motivates the frozen-probe design below.
12	
13	\paragraph{Binary probe: the stubbornness trap.}
14	With stop-gradient (exp-008v3), the policy cannot game the boundary but instead exploits a deeper flaw: $\dsyc$ does not condition on input validity, so refusing to revise a wrong answer receives the same $\rone = 1$ as correctly resisting invalid pressure.
15	By step 500, $\tof$ drops to 0.000 and $\nof$ reaches 0.995, yielding $\sycon = 0$.
16	Qualitative analysis of 181 valid-correction responses reveals five failure modes: \emph{deliberation traps} (28.7\%), where the model identifies the correct answer but cannot commit; \emph{sycophantic stubbornness} (24.3\%), where the model verbally agrees but does not change its answer; \emph{acknowledge-but-maintain} (23.8\%); \emph{genuine-accept-missed} (18.8\%); and refute/ignore/other (4.5\%). Full taxonomy in Appendix~\ref{app:taxonomy}.
17	
18	\paragraph{Behavioral death precedes distributional collapse.}
19	
20	\begin{table}[t]
21	\centering
22	\caption{Probe reward trap trajectory (exp-008v3). Behavioral death ($\tof{=}0$) occurs at step 500; entropy re
…[truncated 2314 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 382 · 2026-05-24T09:49:41.579252+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 383 · 2026-05-24T09:49:41.630155+00:00_

1	\section{When Does Discriminability Fail as Reward Utility?}\label{sec:discussion}
2	
3	\paragraph{Root cause of the probe reward trap.}
4	The probe reward trap (\S\ref{sec:probe_trap}) and the cosine failures (\S\ref{sec:cosine_failure}) share a common geometric root.
5	$\dsyc$ encodes the \emph{direction} of belief change but not its \emph{evidential warrant}: valid revision and sycophantic capitulation both shift activations toward the user's position along the same direction.
6	The two reward families expose complementary faces of this blindness.
7	Cosine $\rone$ penalizes all belief change indiscriminately; the resulting mode collapse (F1c, F1d) reflects excessive punishment of any activation shift along $\dsyc$.
8	The binary probe $\rone$ rewards all resistance regardless of input validity; the stubbornness trap ($\tof = 0$ by step 500) reflects excessive permissiveness toward activation stasis.
9	These are not independent design flaws but dual consequences of a direction that conflates the target behavior (resisting invalid challenges) with its complement (refusing valid corrections).
10	Cross-model evidence confirms the limitation extends beyond Qwen3-8B: Llama-3-8B independently achieves AUROC $0.779 \pm 0.019$ on the same contrastive pairs with the same monotonic evidence gradient, so discriminability generalizes across architectures while the semantic gap between discriminability and reward utility persists.
11	This pattern contrasts with reasoning faithfulness and safety directions~\citep{zhang2026latentgrpo}, where the behavior to suppress is geometrically distinct from the behavior to preserve along the relevant direction.
12	\citet{wu2026rewardhacking} reinforce this principle: concept directions applied via advantage modification in GRPO achieve 100\% validation accuracy for reward hacking detection, where shortcut behaviors are geometrically separable.
13	A quantitative comparison of geometric separability between $\dsyc$ and their reward-hacking 
…[truncated 6936 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 384 · 2026-05-24T09:49:49.357598+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 385 · 2026-05-24T09:49:49.859943+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Representation Engineering.}
4	Linear directions in LLM residual streams encode behavioral concepts \citep{zou2023repe}; inference-time methods---ITI \citep{li2023iti}, ActAdd \citep{turner2023actadd}, CAA \citep{rimsky2024caa}---demonstrate that activation geometry suffices for behavioral control \citep{burns2023ccs}.
5	We use the same contrastive extraction as CAA but apply $\dsyc$ as an RL reward, revealing a gap that inference-time work does not encounter.
6	
7	\paragraph{Reward Design and Overoptimization.}
8	Proxy rewards diverge from true objectives under sustained optimization \citep{gao2023scaling}, and reward hacking can escalate to active tampering \citep{denison2024subterfuge}.
9	Our probe trap (\S\ref{sec:probe_trap}) is an extreme instance: the reward actively reinforces degenerate behavior \citep{skalse2022hacking}.
10	\citet{wu2026rewardhacking} show that representation-level directions succeed when behaviors are geometrically separable (\S\ref{sec:discussion}).
11	
12	\paragraph{Sycophancy Characterization and Mitigation.}
13	Sycophancy is pervasive in RLHF-trained assistants \citep{sharma2023sycophancy}, amplified by RLHF \citep{shapira2026amplifies}, and traceable to late-layer preference shifts \citep{wang2025internal}; mitigations include synthetic data \citep{wei2024synthetic}, consistency training \citep{consistency2025bctact}, and neuron-level correction \citep{obrien2025fewbadneurons}.
14	Our analysis shows why the step from diagnosis to reward is structurally blocked: $\dsyc$ conflates warranted revision with unwarranted capitulation.
15	
16	\paragraph{Probe-Based and Representation-Guided Methods.}
17	\citet{papadatos2024probepenalties} reduce sycophancy via Best-of-N reranking with linear probe penalties (94\% accuracy) without producing gradients; our work reveals what happens when a comparable signal enters the training loop (\S\ref{sec:discussion}).
18	Latent-GRPO \citep{
…[truncated 554 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 386 · 2026-05-24T09:49:49.860333+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 387 · 2026-05-24T09:49:50.362479+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	The probe reward trap reveals that behavioral death can precede distributional collapse by 1{,}300 steps, rendering entropy-based monitoring blind to the failure.
4	Because the trap arises under SFT with stopped gradients, it reflects a semantic limitation of $\dsyc$, not an RL artifact; under GRPO, all formulations failed (4/31 checkpoints ${>}$ vanilla across configurations) while per-token SFT succeeded at every checkpoint (47/47), and a LoRA-controlled ablation confirms supervision granularity as the primary factor~(\S\ref{sec:discussion}).
5	More broadly, our results suggest that discriminability is necessary but not sufficient for reward utility: directions that separate a behavior from its complement in activation space may still conflate warranted and unwarranted variants of that behavior.
6	For sycophancy---and likely for other attributes where the target and its complement overlap geometrically---condition-aware rewards with dense supervision offer the most promising path forward.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 388 · 2026-05-24T09:49:50.362936+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 389 · 2026-05-24T09:49:50.865145+00:00_

1	Our GRPO experiments use group sizes of 2 and 8, at the low end of the 8--64 range explored by \citet{shao2024grpo}; a gs$=$8 ablation rules out variance reduction but larger sizes remain unexplored. All completions are truncated to 256 tokens (shared across conditions), which degrades $\dsyc$ AUROC from 0.76 to 0.60 and may affect absolute reward-utility conclusions.
2	Training and evaluation share the same 181 pairs; a held-out split (146/35) confirms ACT generalizes ($\sycon{\approx}0.20$ at peak, $3.7{\times}$ vanilla, 72\% of full-data ceiling), but performance declines at step 2000 ($\sycon{=}0.157$, still $2.8{\times}$ vanilla) due to overfitting on the small training set, and the 28\% gap suggests partial reliance on training-set-specific patterns.
3	The probe reward trap (C2) is demonstrated with a single seed; while SFT training is more deterministic than RL, replication would strengthen the temporal decoupling finding.
4	All RL training uses Qwen3-8B; cross-model discriminability is confirmed on Llama-3-8B (AUROC $0.779$; Table~\ref{tab:cross_model}), but compute constraints prevented training replication on a second architecture.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-24T09:49:50.915850+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 391 · 2026-05-24T09:49:50.966561+00:00_

1	\section{Training Details}
2	\label{app:training}
3	
4	\paragraph{Reward weight selection.}
5	The weight $w_1$ is set by diagnostic-driven iteration: $w_1{=}0.25$ was initially chosen to down-weight the noisy cosine reward term; this was later increased to $w_1{=}0.40$ for F1d after diagnostics revealed that $w_1{=}0.25$ allowed the cosine term to contribute only ${\sim}8.3\%$ of total reward variance.
6	The empirical scaling factor in F1a ($\dsyc/20$) is a heuristic normalization; we did not find it critical to the failure modes reported.
7	
8	\paragraph{Response truncation.}
9	All GRPO experiments use \texttt{max\_completion\_length}=256, resulting in 80--84\% truncation of multi-turn responses.
10	This setting is shared across all conditions and does not affect relative comparisons; we retain it because response-level decisions typically manifest within the first 100--200 tokens.
11	
12	\paragraph{Hyperparameters.}
13	Table~\ref{tab:hyperparams} compares training configurations for GRPO variants and ACT.
14	
15	\begin{table}[h]
16	\centering
17	\small
18	\caption{Training hyperparameters. All experiments use Qwen3-8B, DeepSpeed ZeRO-2, bf16 precision.}
19	\label{tab:hyperparams}
20	\begin{tabular}{lcc}
21	\toprule
22	& GRPO (F1, F3)$^e$ & ACT \\
23	\midrule
24	Learning rate & 5e-5 & 5e-5 \\
25	Effective batch & 16 & 16 \\
26	Max steps & 8{,}000 & 8{,}000 \\
27	Warmup steps & 200 & 200 \\
28	LR schedule & linear$^a$ & linear \\
29	Grad.\ clipping & --- & 1.0 \\
30	\midrule
31	LoRA rank & 64 & 64 \\
32	LoRA $\alpha$ & 64 & 128 \\
33	LoRA modules & 4$^b$ & 7$^c$ \\
34	LoRA dropout & 0 & 0.05 \\
35	\midrule
36	Group size & 2$^d$ & --- \\
37	KL $\beta$ & 0.04 & --- \\
38	Max compl.\ len. & 256 & --- \\
39	Max seq.\ len. & --- & 1{,}024 \\
40	L2 loss weight & --- & 0.1 \\
41	\bottomrule
42	\end{tabular}
43	\\[2pt]
44	\raggedright\footnotesize
45	$^a$Cosine schedule for $\rthree$-only.
46	$^b$q/k/v/o\_proj.
47	$^c$+ gate/up/down\_proj (${\sim}1.75{\times}$ params; \S\
…[truncated 2143 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 392 · 2026-05-24T09:51:23.321465+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the key reviewer guidelines: what should reviewers evaluate, what are the assessment criteria, how should reviews be structured. Focus on soundness criteria, what constitutes a good vs bad review, and any specific instructions about experimental evaluation standards."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the key reviewer guidelines: what should reviewers evaluate, what are the assessment criteria, how should reviews be structured. Focus on soundness criteria, what constitutes a good vs bad review, and any specific instructions about experimental evaluation standards."
  }
}
```

</details>

---


### Tool result

_source line 393 · 2026-05-24T09:51:29.889739+00:00_

# ARR Reviewer Guidelines: Key Evaluation Criteria

## Core Assessment Framework

Reviewers must evaluate papers using **three scores**: soundness, excitement, and overall recommendation. The soundness score must be justified by specific review text—vague criticisms without evidence undermine credibility.

## Soundness Criteria

Strong reviews assess whether research is **technically correct and appropriately scoped**. Key elements include:

- **Technical validity**: Proofs should be complete, assumptions clearly stated, and experimental methods sound
- **Methodological rigor**: Sufficient evidence supports claimed conclusions; statistical significance is documented
- **Reproducibility**: Adequate details enable others to replicate experiments; code/data availability is clear

## Structural Requirements for Reviews

Reviewers should follow this workflow:

1. **Read twice**: First skim for research questions and scope without examining results. Then conduct in-depth technical evaluation.
2. **Be specific**: Rather than stating "X is unclear," identify missing elements with precision (e.g., "the methodology section omits hyperparameter selection details").
3. **Justify scores**: Low soundness ratings must connect to documented flaws discovered during review.

## Common Review Pitfalls to Avoid

The guidelines identify problematic patterns:

- Dismissing work as "unsurprising" overlooks that intuitive findings may lack empirical validation
- Requiring comparisons to closed-source models without justifying relevance to core claims
- Treating acknowledged limitations as weaknesses rather than honest scoping decisions
- Expecting SOTA results when papers pursue different contributions

## Professional Standards

Reviewers must maintain "professional and neutral" tone. The guidelines note that anonymous reviewing creates power imbalances; harsh language causes documented harm to researchers' mental health and community culture.

## Author Response Engagement

Reviewers sho
…[truncated 160 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6568
}
```

</details>

---


### Tool call

_source line 394 · 2026-05-24T09:51:38.733021+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 395 · 2026-05-24T09:51:38.785367+00:00_

1	@article{zhang2026latentgrpo,
2	  title={Silence the Judge: Reinforcement Learning with Self-Verifier via Latent Geometric Clustering},
3	  author={Zhang, Nonghai and Ma, Weitao and Ma, Zhanyu and Xu, Jun and Gao, Jiuchong and Hao, Jinghua and He, Renqing and Xu, Jingwen},
4	  journal={arXiv preprint arXiv:2601.08427},
5	  year={2026}
6	}
7	
8	@inproceedings{zou2023repe,
9	  title={Representation Engineering: A Top-Down Approach to {AI} Transparency},
10	  author={Zou, Andy and Phan, Long and Chen, Sarah and Campbell, James and Guo, Phillip and Ren, Richard and Pan, Alexander and Yin, Xuwang and Mazeika, Mantas and Dombrowski, Ann-Kathrin and Gould, Shashwat and Li, Zifan and Xie, Chuanqi and Leung, Alexandria and Hase, Peter and Hendrycks, Dan},
11	  booktitle={International Conference on Learning Representations (ICLR)},
12	  year={2025}
13	}
14	
15	@inproceedings{rimsky2024caa,
16	  title={Steering Llama 2 via Contrastive Activation Addition},
17	  author={Rimsky, Nina and Gabrieli, Nick and Schulz, Jenna and Smith, Meg and Tong, Ioannis and Hubinger, Evan},
18	  booktitle={Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL)},
19	  year={2024}
20	}
21	
22	@article{shao2024grpo,
23	  title={DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models},
24	  author={Shao, Zhihong and Wang, Peiyi and Zhu, Qihao and Xu, Runxin and Song, Junxiao and Zhang, Mingchuan and Li, Y.K. and Wu, Y. and Guo, Daya},
25	  journal={arXiv preprint arXiv:2402.03300},
26	  year={2024}
27	}
28	
29	@inproceedings{li2023iti,
30	  title={Inference-Time Intervention: Eliciting Truthful Answers from a Language Model},
31	  author={Li, Kenneth and Patel, Oam and Vi{\'e}gas, Fernanda and Pfister, Hanspeter and Wattenberg, Martin},
32	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
33	  year={2023}
34	}
35	
36	@article{turner2023actadd,
37	  title={Steering Language Models With Activation Engineering}
…[truncated 7987 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 396 · 2026-05-24T09:53:56.928216+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Summary\n\n本文提出\"probe reward trap\"现象：当冻结线性探针基于对比性谄媚方向 (d_syc, AUROC 0.827) 作为 SFT 训练信号时，行为死亡 (ToF=0) 在 500 步即发生，而分布坍缩 (熵降) 延后至 ~1840 步，产生 1,300 步的监控盲区。论文系统测试了余弦投影、二值探针、连续探针等多种 d_syc reward 公式，均失败；与之对比，ACT (逐 token SFT) 在所有 checkpoint 上超越 vanilla。作者将根因归结为 d_syc 的语义局限：它编码信念是否改变，但不编码是否**应该**改变，从而混淆了合理修正与谄媚妥协。\n\n## Strengths\n\n[S1] **Probe reward trap 的发现新颖且有实践意义。** 行为死亡先于分布坍缩 1,300 步、熵监控完全失效的发现 (Table 3, Figure 3)，对 reward hacking 检测有直接警示价值。该实验使用 SFT + stop-gradient，与 GRPO 动态学无关，因果链干净。\n\n[S2] **余弦 R1 的诊断链 (F1a→F1d) 设计系统。** 每一步解决前序 failure mode 但暴露更深层问题 (Table 2)，从 norm mismatch → gap too small → reward discontinuity → R3 saturation，逐层递进，说服力强。\n\n[S3] **几何洞见清晰。** d_syc 无法区分 warranted revision 与 unwarranted capitulation 的论证 (Section 6)，与 Zhang et al. (2026) 和 Wu & Tang (2026) 形成有意义的对比——在 sycophancy 场景中 target behavior 与其 complement 在激活空间几何上不可分离。\n\n[S4] **Stubbornness taxonomy (Appendix B) 信息量大。** 对 181 个 valid-correction response 的 5 类失败模式定性分析 (deliberation traps 28.7%, sycophantic stubbornness 24.3% 等) 为理解 probe reward 的具体失效机制提供了有价值的证据。\n\n[S5] **跨模型验证 (Llama-3-8B) 增强了 d_syc discriminability 结论的稳健性。** Table 1 和 Figure 2 显示两个架构家族呈现相同的 pattern (gradual emergence, upper-third concentration, monotonic evidence-strength scaling)。\n\n## Weaknesses\n\n[W1] [severity: critical] **GPT-4.1 生成的 181 对 contrastive pairs 缺乏人工验证**\n- 具体位置：Section 2.1\n- 问题：全部 181 个 contrastive pairs（包括 valid correction vs sycophantic capitulation 的区分、evidence strength 三级标注）由 GPT-4.1 生成，仅通过自动化风格匹配（长度差 <10%、共享开头词 ≥2 个）筛选。无人工验证、无 inter-annotator agreement。evidence strength 标注 (weak/medium/strong) 的可信度不明。\n- 为什么影响接收：d_syc 是整篇论文的基石。如果 GPT-4.1 在生成\"valid correction\"和\"sycophantic capitulation\"时存在系统偏差（例如风格差异未完全被 style matching 消除），则 d_syc 可能捕捉的是 GPT-4.1 的生成风格特征而非 sycophancy 的语义特征，整个 discriminability → reward utility 的推理链将受到质疑。\n- 建议修改方向：(1) 对至少一个子集 (~50 对) 进行人工标注验证 (agreement with GPT-4.1 labels)；(2) 报告 evidence strength 的 IAA (κ or α)；(3) 明确 GPT-4.1 生成的 prompt template，使读者可评估偏差风险。\n\n[W2] [severity: critical] **GRPO group_size=2 构成未充分排除的混淆变量**\n- 具体位置：Section 2 (framework), Section 6 (discussion), Table 5\n- 问题：gs=2 远低于 GRPO 典型范围 (8-64, Shao et al. 2024)，意味着 advantage estimation 基本退化为二元比较。论文声称 gs=8 ablation \"rules out hypothesis (b)\"，但 gs=8 实验仅运行了 3 个 checkpoint 即被提前终止 (Table 5)，从 0.084→0.085→0.054 的 3 个数据点不足以支撑任何结论。\n- 为什么影响接收：论文的核心主张之一是\"per-completion scalar RL 本身不适合 sycophancy calibration\"。但 gs=2 条件下 R3 已饱和至 ~0.98 (p=0.703)，advantage signal 近乎噪声。这使得 GRPO 所有失败（包括 R3-only、d_syc-based）都可能是 gs=2 导致的信号退化，而非 per-completion RL 的本质局限。gs=8 ablation 的过早终止尤其令人担忧——3 个初始 checkpoint 的下降完全可能是正常 warmup 波动。\n- 建议修改方向：(1) gs=8 至少运行完整训练周期 (8,000 steps)；(2) 若资源不足以运行 gs=16/32，应在 Limitations 中明确承认这一混淆变量未被充分控制，并 downgrade 相关结论的强度（从 \"per-completion RL fails\" 到 \"per-completion RL with small group sizes fails\"）。\n\n[W3] [severity: critical] **ACT vs GRPO 的 \"supervision granularity\" 结论存在多维混淆**\n- 具体位置：Section 6, Table 4, Table 5\n- 问题：即便 reduced-LoRA ablation (Table 5) 控制了 adapter capacity（rank 64, α=64, 4 modules），ACT 与 GRPO 之间仍存在以下未控制变量：\n  (a) 序列长度：GRPO max_completion_length=256 vs ACT max_seq_len=1024\n  (b) 训练数据来源：GRPO 用在线生成的 completions，ACT 用预构造的 labeled pairs\n  (c) Reward 信号：GRPO 用 R1+R3 scalar reward，ACT 用 gold labels 的 SFT loss + L2 consistency loss\n  (d) LoRA dropout：GRPO 0 vs ACT 0.05\n  论文将差异归因于\"supervision granularity (per-token vs per-completion)\"，但以上任一因素都可能解释 ACT 的优势。\n- 为什么影响接收：这是论文最核心的 positive claim（Section 6 \"isolating supervision granularity as the primary factor\"），若无法可信地隔离这一因素，论文的 actionable takeaway 将大打折扣。\n- 建议修改方向：(1) 在 GRPO 框架内实现 per-token reward (token-level R3)，看是否改善性能——这将真正隔离 granularity；(2) 或在 ACT 框架内限制 max_seq_len=256，看性能是否下降；(3) 至少应在论文中列出所有差异维度并讨论其可能的独立影响，而非直接跳至\"supervision granularity\"结论。\n\n[W4] [severity: warning] **256-token truncation 对 d_syc AUROC 的严重退化 (0.827→0.60) 削弱了\"d_syc fundamental limitation\"的结论**\n- 具体位置：Section 4, Appendix A\n- 问题：论文将 d_syc 的失败归因于其语义局限（无法区分 warranted vs unwarranted belief change）。但 256-token 截断使 AUROC 从 full-response 的 0.76 降至 0.60 (近乎 chance for binary classification)。在这种严重退化条件下的失败，可能反映的是信号不足而非语义缺陷。论文未测试使用更长 completion 长度（如 512 或 1024 tokens）的 GRPO 是否仍失败。\n- 建议：(1) 至少讨论 truncation 对 cosine failure chain 各环节的独立影响；(2) 理想情况下测试 max_completion_length=512 的 GRPO 条件。\n\n[W5] [severity: warning] **统计效力不足 (n=2 seeds) 无法支撑关于训练稳定性的结论**\n- 具体位置：Section 6, Figure 4, Table 4\n- 问题：GRPO 2 seeds, ACT 2 seeds, probe trap 1 seed。论文基于 2 个 seed 的 GRPO 轨迹 (Figure 4) 讨论 \"oscillation (Δ≈0.069)\"和\"both seeds diverging\"。n=2 的 rank correlation 或 variance estimation 无统计意义。ACT seed 2 在 Table 4 中 ToF 和 NoF 标记为 \"—\"（未报告），降低了跨 seed 一致性的可验证性。\n- 建议：(1) 增加至 3-5 seeds 或报告 bootstrap CI；(2) 对 ACT seed 2 补齐 ToF/NoF 数值；(3) 若资源限制无法增加 seeds，应在结论中明确标注统计效力局限。\n\n[W6] [severity: warning] **SyconScore 单一指标可能遮蔽有意义的差异**\n- 具体位置：Section 2.5, Eq. 2\n- 问题：SyconScore 的 harmonic mean 设计使 ToF=0 时直接归零 (by design)。但论文从未同时报告 arithmetic mean 或分别分析 ToF 和 NoF 的变化趋势。例如 R3-only GRPO 的 ToF=0.083 (Table 4) 接近 vanilla 的 0.072——这一微小改善在 SyconScore 中被 harmonic mean 压缩，而 arithmetic mean (0.083+0.983)/2=0.533 vs vanilla (0.072+0.945)/2=0.509 也仅有微弱改善，提供了额外的解读维度。\n- 建议：在 main results table 中补充 arithmetic mean 列，或至少在讨论中分析 ToF/NoF 各自的变化趋势。\n\n[W7] [severity: minor] **代码和数据可用性未提及**\n- 具体位置：全文\n- 问题：论文未提及是否计划发布 181 个 contrastive pairs、GPT-4.1 generation prompts、训练代码或 checkpoint。考虑到 d_syc 提取和评估的具体实现细节较多，这影响可复现性。\n- 建议：在 paper 中声明 release plan，或在 supplementary 中提供 pair 生成的 prompt template。\n\n[W8] [severity: minor] **R3-only GRPO 的失败解读不充分**\n- 具体位置：Section 6\n- 问题：论文说 \"R3-only GRPO tests this hypothesis by relying solely on the NLI behavioral reward—and fails\"，但 R3 在 gs=2 条件下饱和至 ~0.98，meaning completions 间的 R3 差异极小。gs=2 条件下对饱和 reward 做 ranking 等同于随机选择。这更可能是 gs=2 + reward saturation 的问题，而非 \"per-completion scalar RL\" 的本质局限。\n- 建议：与 [W2] 一致，需要更大 group size 或不同 reward 信号的消融。\n\n## Questions\n\n[Q1] 论文 Section 3 报告 d_syc AUROC = 0.827 (L19, 5-fold CV, full-length activations)，Section 4 报告 256-token truncation 下降至 0.60。但 cosine failure chain (Table 2) 的四个配置是否都使用了 256-token 截断下的 d_syc？如果是，F1c 的 \"offline AUROC rises to 0.910\" 是否指 recalibrated direction 在 full-length activations 上的性能？论文应明确区分哪些 AUROC 数字对应哪种条件。\n\n[Q2] ACT 的 L2 activation consistency loss weight = 0.1 (Table 5)。这个权重是如何选定的？对最终性能有多敏感？这一设计选择可能对 ACT 的相对优势有显著影响。\n\n[Q3] Stubbornness taxonomy (Appendix B) 中 \"genuine-accept-missed\" (18.8%) 被描述为 \"a generation rather than epistemic failure\"。如果近 1/5 的失败是格式/生成问题而非真正的 epistemic 问题，那么 ToF=0 的解读是否应更谨慎？这些 case 中 NLI classifier 是否正确判定为 \"not flipped\"？\n\n[Q4] 论文提到 held-out validation (146/35 split) 显示 ACT generalizes (SyconScore≈0.20, 3.7× vanilla)。这个 held-out 实验的完整结果（含 GRPO）是否可以在 appendix 中报告？这对评估 d_syc-based reward 和 R3-only GRPO 在 held-out 上的表现很有价值。\n\n[Q5] Table 5 中 ACT reduced-LoRA 的 best SyconScore (0.326) 反而高于 full ACT (0.301)。论文以此论证 \"not an adapter-capacity artifact\"，但这是否意味着 full ACT 可能过参数化？这两个条件的 overfitting 情况是否不同？\n\n## Missing References\n\n无显著遗漏。related work 覆盖了 representation engineering、reward overoptimization、sycophancy mitigation、probe-based methods 四个核心方向。可考虑加入 Perez et al. (2023) \"Discovering Language Model Behaviors with Model-Written Evaluations\" 作为 LLM-generated evaluation data 的先例和对照。\n\n## Scores\n\n- Soundness: 3/5 — 核心 probe reward trap 观察扎实，但 GRPO gs=2 混淆、ACT vs GRPO 多维混淆、GPT-4.1 pairs 无人工验证，使得若干关键因果推断 (supervision granularity 是 primary factor) 的支撑不足。\n- Excitement: 3.5/5 — \"behavioral death before distributional collapse\" 的发现新颖且有实践价值；d_syc discriminability ≠ reward utility 的几何解释有深度。但 negative result 的 actionable takeaway 受限于混淆变量。\n- Contribution: 3/5 — 文档化 representation-based reward 的失败模式有价值，但论文没有提出可行的解决方案（仅提方向），且对失败归因不够精确。\n- Reproducibility: 3/5 — 超参数报告合理 (Table 5)，但 code/data 未提及，GPT-4.1 pair generation prompt 未公开。\n- Overall: 3.0 (Findings) — 论文有清晰的核心发现 (probe reward trap) 和有意义的几何洞见，但实验设计的关键混淆变量 ([W1]-[W3]) 阻碍了对中心 claim (\"supervision granularity is the primary factor\") 的可信归因。若充分解决 gs 混淆、补充人工验证、并更审慎地界定 ACT-GRPO 对比的结论范围，可望提升至 Borderline Conference。\n- Confidence: 4/5 — 对方法论和实验设计的评估有充分把握；对 representation engineering 和 GRPO/RL 训练有足够背景知识；仔细阅读了全文包括 appendix。\n",
  "reviewer_id": "1",
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Summary\n\n本文提出\"probe reward trap\"现象：当冻结线性探针基于对比性谄媚方向 (d_syc, AUROC 0.827) 作为 SFT 训练信号时，行为死亡 (ToF=0) 在 500 步即发生，而分布坍缩 (熵降) 延后至 ~1840 步，产生 1,300 步的监控盲区。论文系统测试了余弦投影、二值探针、连续探针等多种 d_syc reward 公式，均失败；与之对比，ACT (逐 token SFT) 在所有 checkpoint 上超越 vanilla。作者将根因归结为 d_syc 的语义局限：它编码信念是否改变，但不编码是否**应该**改变，从而混淆了合理修正与谄媚妥协。\n\n## Strengths\n\n[S1] **Probe reward trap 的发现新颖且有实践意义。** 行为死亡先于分布坍缩 1,300 步、熵监控完全失效的发现 (Table 3, Figure 3)，对 reward hacking 检测有直接警示价值。该实验使用 SFT + stop-gradient，与 GRPO 动态学无关，因果链干净。\n\n[S2] **余弦 R1 的诊断链 (F1a→F1d) 设计系统。** 每一步解决前序 failure mode 但暴露更深层问题 (Table 2)，从 norm mismatch → gap too small → reward discontinuity → R3 saturation，逐层递进，说服力强。\n\n[S3] **几何洞见清晰。** d_syc 无法区分 warranted revision 与 unwarranted capitulation 的论证 (Section 6)，与 Zhang et al. (2026) 和 Wu & Tang (2026) 形成有意义的对比——在 sycophancy 场景中 target behavior 与其 complement 在激活空间几何上不可分离。\n\n[S4] **Stubbornness taxonomy (Appendix B) 信息量大。** 对 181 个 valid-correction response 的 5 类失败模式定性分析 (deliberation traps 28.7%, sycophantic stubbornness 24.3% 等) 为理解 probe reward 的具体失效机制提供了有价值的证据。\n\n[S5] **跨模型验证 (Llama-3-8B) 增强了 d_syc discriminability 结论的稳健性。** Table 1 和 Figure 2 显示两个架构家族呈现相同的 pattern (gradual emergence, upper-third concentration, monotonic evidence-strength scaling)。\n\n## Weaknesses\n\n[W1] [severity: critical] **GPT-4.1 生成的 181 对 contrastive pairs 缺乏人工验证**\n- 具体位置：Section 2.1\n- 问题：全部 181 个 contrastive pairs（包括 valid correction vs sycophantic capitulation 的区分、evidence strength 三级标注）由 GPT-4.1 生成，仅通过自动化风格匹配（长度差 <10%、共享开头词 ≥2 个）筛选。无人工验证、无 inter-annotator agreement。evidence strength 标注 (weak/medium/strong) 的可信度不明。\n- 为什么影响接收：d_syc 是整篇论文的基石。如果 GPT-4.1 在生成\"valid correction\"和\"sycophantic capitulation\"时存在系统偏差（例如风格差异未完全被 style matching 消除），则 d_syc 可能捕捉的是 GPT-4.1 的生成风格特征而非 sycophancy 的语义特征，整个 discriminability → reward utility 的推理链将受到质疑。\n- 建议修改方向：(1) 对至少一个子集 (~50 对) 进行人工标注验证 (agreement with GPT-4.1 labels)；(2) 报告 evidence strength 的 IAA (κ or α)；(3) 明确 GPT-4.1 生成的 prompt template，使读者可评估偏差风险。\n\n[W2] [severity: critical] **GRPO group_size=2 构成未充分排除的混淆变量**\n- 具体位置：Section 2 (framework), Section 6 (discussion), Table 5\n- 问题：gs=2 远低于 GRPO 典型范围 (8-64, Shao et al. 2024)，意味着 advantage estimation 基本退化为二元比较。论文声称 gs=8 ablation \"rules out hypothesis (b)\"，但 gs=8 实验仅运行了 3 个 checkpoint 即被提前终止 (Table 5)，从 0.084→0.085→0.054 的 3 个数据点不足以支撑任何结论。\n- 为什么影响接收：论文的核心主张之一是\"per-completion scalar RL 本身不适合 sycophancy calibration\"。但 gs=2 条件下 R3 已饱和至 ~0.98 (p=0.703)，advantage signal 近乎噪声。这使得 GRPO 所有失败（包括 R3-only、d_syc-based）都可能是 gs=2 导致的信号退化，而非 per-completion RL 的本质局限。gs=8 ablation 的过早终止尤其令人担忧——3 个初始 checkpoint 的下降完全可能是正常 warmup 波动。\n- 建议修改方向：(1) gs=8 至少运行完整训练周期 (8,000 steps)；(2) 若资源不足以运行 gs=16/32，应在 Limitations 中明确承认这一混淆变量未被充分控制，并 downgrade 相关结论的强度（从 \"per-completion RL fails\" 到 \"per-completion RL with small group sizes fails\"）。\n\n[W3] [severity: critical] **ACT vs GRPO 的 \"supervision granularity\" 结论存在多维混淆**\n- 具体位置：Section 6, Table 4, Table 5\n- 问题：即便 reduced-LoRA ablation (Table 5) 控制了 adapter capacity（rank 64, α=64, 4 modules），ACT 与 GRPO 之间仍存在以下未控制变量：\n  (a) 序列长度：GRPO max_completion_length=256 vs ACT max_seq_len=1024\n  (b) 训练数据来源：GRPO 用在线生成的 completions，ACT 用预构造的 labeled pairs\n  (c) Reward 信号：GRPO 用 R1+R3 scalar reward，ACT 用 gold labels 的 SFT loss + L2 consistency loss\n  (d) LoRA dropout：GRPO 0 vs ACT 0.05\n  论文将差异归因于\"supervision granularity (per-token vs per-completion)\"，但以上任一因素都可能解释 ACT 的优势。\n- 为什么影响接收：这是论文最核心的 positive claim（Section 6 \"isolating supervision granularity as the primary factor\"），若无法可信地隔离这一因素，论文的 actionable takeaway 将大打折扣。\n- 建议修改方向：(1) 在 GRPO 框架内实现 per-token reward (token-level R3)，看是否改善性能——这将真正隔离 granularity；(2) 或在 ACT 框架内限制 max_seq_len=256，看性能是否下降；(3) 至少应在论文中列出所有差异维度并讨论其可能的独立影响，而非直接跳至\"supervision granularity\"结论。\n\n[W4] [severity: warning] **256-token truncation 对 d_syc AUROC 的严重退化 (0.827→0.60) 削弱了\"d_syc fundamental limitation\"的结论**\n- 具体位置：Section 4, Appendix A\n- 问题：论文将 d_syc 的失败归因于其语义局限（无法区分 warranted vs unwarranted belief change）。但 256-token 截断使 AUROC 从 full-response 的 0.76 降至 0.60 (近乎 chance for binary classification)。在这种严重退化条件下的失败，可能反映的是信号不足而非语义缺陷。论文未测试使用更长 completion 长度（如 512 或 1024 tokens）的 GRPO 是否仍失败。\n- 建议：(1) 至少讨论 truncation 对 cosine failure chain 各环节的独立影响；(2) 理想情况下测试 max_completion_length=512 的 GRPO 条件。\n\n[W5] [severity: warning] **统计效力不足 (n=2 seeds) 无法支撑关于训练稳定性的结论**\n- 具体位置：Section 6, Figure 4, Table 4\n- 问题：GRPO 2 seeds, ACT 2 seeds, probe trap 1 seed。论文基于 2 个 seed 的 GRPO 轨迹 (Figure 4) 讨论 \"oscillation (Δ≈0.069)\"和\"both seeds diverging\"。n=2 的 rank correlation 或 variance estimation 无统计意义。ACT seed 2 在 Table 4 中 ToF 和 NoF 标记为 \"—\"（未报告），降低了跨 seed 一致性的可验证性。\n- 建议：(1) 增加至 3-5 seeds 或报告 bootstrap CI；(2) 对 ACT seed 2 补齐 ToF/NoF 数值；(3) 若资源限制无法增加 seeds，应在结论中明确标注统计效力局限。\n\n[W6] [severity: warning] **SyconScore 单一指标可能遮蔽有意义的差异**\n- 具体位置：Section 2.5, Eq. 2\n- 问题：SyconScore 的 harmonic mean 设计使 ToF=0 时直接归零 (by design)。但论文从未同时报告 arithmetic mean 或分别分析 ToF 和 NoF 的变化趋势。例如 R3-only GRPO 的 ToF=0.083 (Table 4) 接近 vanilla 的 0.072——这一微小改善在 SyconScore 中被 harmonic mean 压缩，而 arithmetic mean (0.083+0.983)/2=0.533 vs vanilla (0.072+0.945)/2=0.509 也仅有微弱改善，提供了额外的解读维度。\n- 建议：在 main results table 中补充 arithmetic mean 列，或至少在讨论中分析 ToF/NoF 各自的变化趋势。\n\n[W7] [severity: minor] **代码和数据可用性未提及**\n- 具体位置：全文\n- 问题：论文未提及是否计划发布 181 个 contrastive pairs、GPT-4.1 generation prompts、训练代码或 checkpoint。考虑到 d_syc 提取和评估的具体实现细节较多，这影响可复现性。\n- 建议：在 paper 中声明 release plan，或在 supplementary 中提供 pair 生成的 prompt template。\n\n[W8] [severity: minor] **R3-only GRPO 的失败解读不充分**\n- 具体位置：Section 6\n- 问题：论文说 \"R3-only GRPO tests this hypothesis by relying solely on the NLI behavioral reward—and fails\"，但 R3 在 gs=2 条件下饱和至 ~0.98，meaning completions 间的 R3 差异极小。gs=2 条件下对饱和 reward 做 ranking 等同于随机选择。这更可能是 gs=2 + reward saturation 的问题，而非 \"per-completion scalar RL\" 的本质局限。\n- 建议：与 [W2] 一致，需要更大 group size 或不同 reward 信号的消融。\n\n## Questions\n\n[Q1] 论文 Section 3 报告 d_syc AUROC = 0.827 (L19, 5-fold CV, full-length activations)，Section 4 报告 256-token truncation 下降至 0.60。但 cosine failure chain (Table 2) 的四个配置是否都使用了 256-token 截断下的 d_syc？如果是，F1c 的 \"offline AUROC rises to 0.910\" 是否指 recalibrated direction 在 full-length activations 上的性能？论文应明确区分哪些 AUROC 数字对应哪种条件。\n\n[Q2] ACT 的 L2 activation consistency loss weight = 0.1 (Table 5)。这个权重是如何选定的？对最终性能有多敏感？这一设计选择可能对 ACT 的相对优势有显著影响。\n\n[Q3] Stubbornness taxonomy (Appendix B) 中 \"genuine-accept-missed\" (18.8%) 被描述为 \"a generation rather than epistemic failure\"。如果近 1/5 的失败是格式/生成问题而非真正的 epistemic 问题，那么 ToF=0 的解读是否应更谨慎？这些 case 中 NLI classifier 是否正确判定为 \"not flipped\"？\n\n[Q4] 论文提到 held-out validation (146/35 split) 显示 ACT generalizes (SyconScore≈0.20, 3.7× vanilla)。这个 held-out 实验的完整结果（含 GRPO）是否可以在 appendix 中报告？这对评估 d_syc-based reward 和 R3-only GRPO 在 held-out 上的表现很有价值。\n\n[Q5] Table 5 中 ACT reduced-LoRA 的 best SyconScore (0.326) 反而高于 full ACT (0.301)。论文以此论证 \"not an adapter-capacity artifact\"，但这是否意味着 full ACT 可能过参数化？这两个条件的 overfitting 情况是否不同？\n\n## Missing References\n\n无显著遗漏。related work 覆盖了 representation engineering、reward overoptimization、sycophancy mitigation、probe-based methods 四个核心方向。可考虑加入 Perez et al. (2023) \"Discovering Language Model Behaviors with Model-Written Evaluations\" 作为 LLM-generated evaluation data 的先例和对照。\n\n## Scores\n\n- Soundness: 3/5 — 核心 probe reward trap 观察扎实，但 GRPO gs=2 混淆、ACT vs GRPO 多维混淆、GPT-4.1 pairs 无人工验证，使得若干关键因果推断 (supervision granularity 是 primary factor) 的支撑不足。\n- Excitement: 3.5/5 — \"behavioral death before distributional collapse\" 的发现新颖且有实践价值；d_syc discriminability ≠ reward utility 的几何解释有深度。但 negative result 的 actionable takeaway 受限于混淆变量。\n- Contribution: 3/5 — 文档化 representation-based reward 的失败模式有价值，但论文没有提出可行的解决方案（仅提方向），且对失败归因不够精确。\n- Reproducibility: 3/5 — 超参数报告合理 (Table 5)，但 code/data 未提及，GPT-4.1 pair generation prompt 未公开。\n- Overall: 3.0 (Findings) — 论文有清晰的核心发现 (probe reward trap) 和有意义的几何洞见，但实验设计的关键混淆变量 ([W1]-[W3]) 阻碍了对中心 claim (\"supervision granularity is the primary factor\") 的可信归因。若充分解决 gs 混淆、补充人工验证、并更审慎地界定 ACT-GRPO 对比的结论范围，可望提升至 Borderline Conference。\n- Confidence: 4/5 — 对方法论和实验设计的评估有充分把握；对 representation engineering 和 GRPO/RL 训练有足够背景知识；仔细阅读了全文包括 appendix。\n",
    "reviewer_id": "1",
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 397 · 2026-05-24T09:54:02.401060+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5472
}
```

</details>

---


### Tool call

_source line 398 · 2026-05-24T09:54:06.230330+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
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

_source line 399 · 2026-05-24T09:54:06.281034+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 400 · 2026-05-24T09:54:10.603491+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 401 · 2026-05-24T09:54:10.654287+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_6/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 402 · 2026-05-24T09:54:20.391683+00:00_

审稿意见已提交给 Review Director。

核心判断：**Overall 3.0 (Findings)**。Probe reward trap 的发现（行为死亡先于分布坍缩 1,300 步）新颖且有实践价值，几何洞见清晰。但三个 critical 问题制约了中心 claim 的可信度：(1) 181 对 GPT-4.1 生成的 contrastive pairs 无人工验证/IAA；(2) GRPO gs=2 构成未充分排除的混淆变量，gs=8 ablation 仅 3 个 checkpoint 即终止；(3) ACT vs GRPO 的 "supervision granularity" 归因存在序列长度、数据来源、dropout 等多维混淆。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1"
}
```

</details>

---


## Round 12

## Round 12

4 recorded events


### User

_source line 403 · 2026-05-24T09:57:07.827853+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每条 Strength 和 Weakness，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 完整审稿意见

## Summary

本文记录了"probe reward trap"现象：将基于对比谄媚方向 d_syc 的冻结线性探针作为SFT训练信号时，行为死亡（ToF=0）在500步内发生，而生成熵直到1,300步后才崩溃，导致基于熵的早停机制完全失效。论文系统测试了六种 d_syc 配置，全部失败（4/31 checkpoints 超过 vanilla），而逐token SFT（ACT）在每个检查点（47/47）均超过基线。

## Strengths

[S1] 系统性的诊断链设计出色（§4 F1a→F1d）
[S2] 时间解耦的量化具有实际价值（Table 3, Figure 3, 1300-step lag）
[S3] LoRA控制消融设计严谨（Table 5, 16/16 > vanilla, 1.7×差异）
[S4] 跨模型验证增强可信度（Qwen3-8B + Llama-3-8B）
[S5] 失败模式的定性分类（Appendix B, 五类分类法）

## Weaknesses

[W1] [critical] 核心命题 "discriminability ≠ reward utility" 未充分区分于 Goodhart's Law
- 论文从未提及 Goodhart's Law
- d_syc 作为不完美代理指标，在优化压力下导致"刷指标"，与经典 reward overoptimization 高度同构
- 需明确回答：什么使得 probe reward trap 不仅仅是 Goodhart's Law 的一个 instance？

[W2] [critical] §3 与 §6 之间存在未调和的叙事张力
- §3: d_syc "captures evidential granularity"（AUROC 0.675→0.929 单调上升）
- §6: d_syc "encodes the direction of belief change but not its evidential warrant"
- §5: "d_syc does not condition on input validity"
- 这三组声明之间的关系未被明确阐述

[W3] [critical] 论文在 "negative result" 与 "general principle" 之间定位模糊
- 同时承载局部声明（"我们的方法失败了"）和全局声明（"discriminability is necessary but not sufficient"）
- "mechanistic analysis" 的措辞可能过高——实际是诊断性分析而非真正的机制性分析

[W4] [warning] SMART 讨论逻辑需要更精确
- SMART 处理的也是 sycophancy，与本文同一 target behavior
- 如果 sycophancy 在几何上不可分，SMART 如何成功？
- 论文暗示是 supervision granularity，但 SMART 成功可能来自多因素

[W5] [warning] 标题可能误导读者——论文范围远超 "probe reward trap"

[W6] [warning] Probe reward trap 的关键发现基于单种子

[W7] [warning] ACT vs GRPO 比较存在多个混淆变量（ground-truth labels vs d_syc/R₃ 等）

## Missing References

[MR1] Goodhart's Law 相关讨论（Manheim & Garrabrant 2019）
[MR2] "Playing Devil's Advocate: Off-the-Shelf Persona Vectors Rival Targeted Steering for Sycophancy" (arXiv:2605.21006, May 2026)
[MR3] Wu & Tang (2026) 的几何可分性量化标准需更深入讨论
[MR4] Contrastive Causal Mediation (CCM, NeurIPS 2025)

## Scores
- Soundness: 3/5
- Excitement: 2.5/5
- Contribution: 3/5
- Reproducibility: 3/5
- Overall: 3.0 (Findings)
- Confidence: 4/5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 404 · 2026-05-24T09:58:49.674142+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Strengths\n\n[AGREE] R2-S1: 诊断链设计 (§4 F1a→F1d)。与我的 [S2] 一致，这是论文最扎实的技术贡献之一。每步解决前序 failure mode 同时暴露更深层问题的递进结构 (Table 2) 具有方法论示范价值。\n\n[AGREE] R2-S2: 时间解耦的量化 (Table 3, Figure 3)。与我的 [S1] 一致，1,300-step lag 的发现新颖且有实践意义。补充一点：该实验使用 SFT + stop-gradient，与 GRPO 动态学无关，因果链干净，这进一步增强了该发现的价值。\n\n[AGREE] R2-S3: LoRA 控制消融 (Table 5)。与我对 reduced-LoRA ablation 的认可一致。但我需补充：该消融仅控制了 adapter capacity 一个维度，ACT 与 GRPO 之间仍存在序列长度 (256 vs 1024)、dropout (0 vs 0.05)、数据来源 (online generation vs curated pairs) 等未控制变量 (见我的 [W3])。R2 在 [W7] 中也提到了类似顾虑，但在 [S3] 中对该消融的评价可能略偏积极。\n\n[AGREE] R2-S4: 跨模型验证。与我的 [S5] 一致。Table 1 和 Figure 2 的跨模型一致性增强了 d_syc discriminability 结论的可信度。\n\n[AGREE] R2-S5: 失败模式定性分类。与我的 [S4] 一致。Appendix B 的五类分类法信息量大。\n\n---\n\n### Weaknesses\n\n[AGREE] R2-W1: Goodhart's Law 讨论缺失\nR2 指出 probe reward trap 与 Goodhart's Law / reward overoptimization 高度同构，这是一个重要的概念性缺陷。论文 Section 7 (Related Work) 引用了 Gao et al. (2023) 的 reward overoptimization scaling laws 和 Skalse et al. (2022) 的 reward hacking 定义，但从未使用 \"Goodhart's Law\" 的术语框架，也未明确回答：probe reward trap 作为 Goodhart's Law 的 instance，其独特贡献在哪里？\n\n我认为论文可以做出的区分是：经典 Goodhart's Law 描述的是 proxy reward 在持续优化下逐渐偏离 true objective；而 probe reward trap 的特殊性在于 (1) 行为死亡在 500 步内即发生，远快于典型的 reward overoptimization 时间尺度，(2) 分布坍缩延后 1,300 步，使标准监控失效。但论文需要自己明确这一论点。\n\n补充：Manheim & Garrabrant (2019) 的 Goodhart taxonomy (regressional/extremal/causal/adversarial) 确实值得引用。Probe reward trap 可能同时涉及 regressional (d_syc 是不完美代理) 和 causal (优化改变了 d_syc 与 sycophancy 的关系) 两种类型，这个分析会强化论文的理论定位。\n\n[AGREE] R2-W2: §3 与 §6 之间的叙事张力\n这是我审稿中未显式标注但隐含关注的问题。R2 精确指出了三组声明之间的表面矛盾：\n- §3: d_syc \"captures evidential granularity\" (AUROC 0.675→0.929)\n- §6: d_syc \"encodes direction of belief change but not evidential warrant\"\n- §5: d_syc \"does not condition on input validity\"\n\n我认为这些声明之间实际上不矛盾，但论文确实未清晰阐述它们的关系。合理的调和是：d_syc 在 offline classification 设定下能区分不同 evidence strength 的 sycophantic responses（因为 stronger evidence 下 sycophantic vs valid 的行为差异更大，产生更可分的 activation pattern），但这并不意味着 d_syc 编码了 evidence warrant 本身——它编码的是\"belief change 的 magnitude\"，而非\"belief change 是否 warranted\"。§3 的 evidence-strength stratification 实际上反映了 effect size 差异，不是 warrant 感知。\n\n但这个关键区分需要论文自己明确写出来。目前的叙述让读者自行推断，容易产生混淆。\n\n[REBUT] R2-W3: \"negative result\" vs \"general principle\" 的定位问题\nR2 认为论文在局部声明与全局声明之间定位模糊。我部分不同意。\n\n论文的结构实际上是合理的渐进式论证：\n1. 局部观察：我们的 d_syc-based reward 全部失败 (§4-§5)\n2. 根因分析：d_syc 的几何特性导致 warranted/unwarranted 不可分 (§6)\n3. 有限度的一般化：discriminability is necessary but not sufficient (§8 Conclusion)\n\n第 3 步的一般化是有条件的——论文明确限定在 \"attributes where the target and its complement overlap geometrically\" (Section 8)，并以 Zhang et al. (2026) 和 Wu & Tang (2026) 为对照说明什么条件下 representation-guided reward 可以成功。这并非无边界的全局声明。\n\n但我同意 R2 关于 \"mechanistic analysis\" 措辞的保留。论文没有做 causal intervention（如 activation patching）来验证 d_syc 的因果角色，称其为\"诊断性分析\"更准确。不过这不影响整体定位的合理性。\n\n[AGREE] R2-W4: SMART 讨论逻辑不精确\nR2 准确指出了逻辑漏洞：如果 sycophancy 的 target/complement 在几何上不可分 (§6 的核心论点)，那 SMART 的 per-step process reward 如何绕过这个根本限制？论文 Section 7 仅说 SMART 的成功 \"independently corroborates supervision granularity as a key factor\"，但未解释 SMART 的 per-step reward 为何不受 d_syc 同样的几何限制。\n\n可能的解释有几种：(1) SMART 可能使用了不同于 d_syc 的 reward signal，本身包含 warrant 信息；(2) per-step reward 可能在 token 级别提供了足够的信息来隐式区分 warranted vs unwarranted；(3) SMART 的成功可能依赖于其他设计选择（模型规模、数据等）。论文未分析这些可能性就直接将 SMART 作为 supervision granularity 假说的证据，逻辑上是不完整的。\n\n[REBUT] R2-W5: 标题误导性\nR2 认为标题范围过窄，论文内容远超 \"probe reward trap\"。我不同意这是一个有意义的问题。学术论文标题突出最 novel 的发现 (probe reward trap + behavioral death before distributional collapse) 是常见且合理的做法。论文的 subtitle \"Behavioral Death Before Distributional Collapse in Sycophancy Calibration\" 已提供了足够的范围信息。标题不需要涵盖所有内容——cosine failure chain 和 ACT 对比是支撑 probe reward trap 论证的组件，而非独立的并列贡献。这属于 editorial preference，不影响学术评估。\n\n[AGREE] R2-W6: Probe trap 单种子\n与我的 [W5] 中的相关观点一致。论文 Limitations 中已承认 \"The probe reward trap (C2) is demonstrated with a single seed\"，且补充了 \"SFT training is more deterministic than RL\" 的论点。但我仍认为至少 2-3 个 seed 是必要的，特别是对于论文最核心的发现。\n\n[AGREE] R2-W7: ACT vs GRPO 多维混淆\n与我的 [W3] 完全一致。R2 特别提到 ground-truth labels vs d_syc/R₃ 的区别，这是一个重要的额外混淆维度——ACT 使用人工标注的 valid/invalid pairs 作为 gold labels，而 GRPO 使用 d_syc 和 NLI 自动评分，数据质量本身就存在差距。\n\n---\n\n### Missing References\n\n[AGREE] R2-MR1: Goodhart's Law (Manheim & Garrabrant 2019) — 如上述 [W1] 回应所述，这是重要遗漏。\n\n[AGREE] R2-MR2: \"Playing Devil's Advocate\" (arXiv:2605.21006, May 2026) — 如果该论文展示 off-the-shelf persona vectors 可以有效减轻 sycophancy 且无需 gradient-based training，这与本文形成有意义的对照：inference-time 方法可以绕过 probe reward trap (与 Papadatos & Freedman 2024 的 inference-time probe penalties 类似)。应纳入 Related Work。\n\n[AGREE] R2-MR3: Wu & Tang (2026) 几何可分性量化标准的更深入讨论。论文 Section 6 已引用该工作，但仅定性提及 \"concept directions applied via advantage modification in GRPO achieve 100% validation accuracy...where shortcut behaviors are geometrically separable\"。量化比较 d_syc 的几何可分性与 Wu & Tang 的 reward-hacking directions 的可分性差异，会显著强化论文的理论贡献。\n\n[REBUT] R2-MR4: Contrastive Causal Mediation (CCM, NeurIPS 2025)。论文未声称做 causal mediation analysis。d_syc 的提取是 contrastive activation analysis (沿 CAA 的方法论)，不是 causal mediation。引用 CCM 可能有参考价值，但将其列为\"missing reference\"过于强势——论文没有做 causal claims 需要 CCM 来支撑。\n\n---\n\n### Scores 对比\n\n| 维度 | R1 | R2 | 差异分析 |\n|------|------|------|----------|\n| Soundness | 3/5 | 3/5 | 一致。核心观察扎实，但因果归因（supervision granularity）的混淆变量是共同关注点。 |\n| Excitement | 3.5/5 | 2.5/5 | **显著分歧。** 我认为 behavioral death before distributional collapse 的发现具有独立的新颖性和实践价值 (对 reward hacking 监控的直接启示)，即便 Goodhart's Law 框架未被讨论。R2 的 2.5 可能受到 \"这只是 Goodhart's Law 的一个 instance\" 的判断影响。我认为 specific mechanistic characterization (时间解耦、失败模式分类、几何不可分性论证) 超越了对已知原则的简单实例化，值得 3.5。 |\n| Contribution | 3/5 | 3/5 | 一致。负面结果有价值但缺少 actionable solution。 |\n| Reproducibility | 3/5 | 3/5 | 一致。 |\n| Overall | 3.0 | 3.0 | 一致。Findings level。 |\n| Confidence | 4/5 | 4/5 | 一致。 |\n\n**关于 Excitement 的分歧：** 我维持 3.5/5。理由：(1) 1,300-step 时间解耦是一个可被其他研究者立即用于改进监控系统的发现；(2) 论文提出的 \"discriminability ≠ reward utility\" 框架虽未完美论证，但指出了 representation engineering 社区需要正视的盲区；(3) stubbornness taxonomy 为理解 RLHF/SFT 训练的微观行为提供了新工具。R2 的 2.5 (Potentially Interesting) 对这些贡献评价偏低。\n",
  "reviewer_id": "1",
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Strengths\n\n[AGREE] R2-S1: 诊断链设计 (§4 F1a→F1d)。与我的 [S2] 一致，这是论文最扎实的技术贡献之一。每步解决前序 failure mode 同时暴露更深层问题的递进结构 (Table 2) 具有方法论示范价值。\n\n[AGREE] R2-S2: 时间解耦的量化 (Table 3, Figure 3)。与我的 [S1] 一致，1,300-step lag 的发现新颖且有实践意义。补充一点：该实验使用 SFT + stop-gradient，与 GRPO 动态学无关，因果链干净，这进一步增强了该发现的价值。\n\n[AGREE] R2-S3: LoRA 控制消融 (Table 5)。与我对 reduced-LoRA ablation 的认可一致。但我需补充：该消融仅控制了 adapter capacity 一个维度，ACT 与 GRPO 之间仍存在序列长度 (256 vs 1024)、dropout (0 vs 0.05)、数据来源 (online generation vs curated pairs) 等未控制变量 (见我的 [W3])。R2 在 [W7] 中也提到了类似顾虑，但在 [S3] 中对该消融的评价可能略偏积极。\n\n[AGREE] R2-S4: 跨模型验证。与我的 [S5] 一致。Table 1 和 Figure 2 的跨模型一致性增强了 d_syc discriminability 结论的可信度。\n\n[AGREE] R2-S5: 失败模式定性分类。与我的 [S4] 一致。Appendix B 的五类分类法信息量大。\n\n---\n\n### Weaknesses\n\n[AGREE] R2-W1: Goodhart's Law 讨论缺失\nR2 指出 probe reward trap 与 Goodhart's Law / reward overoptimization 高度同构，这是一个重要的概念性缺陷。论文 Section 7 (Related Work) 引用了 Gao et al. (2023) 的 reward overoptimization scaling laws 和 Skalse et al. (2022) 的 reward hacking 定义，但从未使用 \"Goodhart's Law\" 的术语框架，也未明确回答：probe reward trap 作为 Goodhart's Law 的 instance，其独特贡献在哪里？\n\n我认为论文可以做出的区分是：经典 Goodhart's Law 描述的是 proxy reward 在持续优化下逐渐偏离 true objective；而 probe reward trap 的特殊性在于 (1) 行为死亡在 500 步内即发生，远快于典型的 reward overoptimization 时间尺度，(2) 分布坍缩延后 1,300 步，使标准监控失效。但论文需要自己明确这一论点。\n\n补充：Manheim & Garrabrant (2019) 的 Goodhart taxonomy (regressional/extremal/causal/adversarial) 确实值得引用。Probe reward trap 可能同时涉及 regressional (d_syc 是不完美代理) 和 causal (优化改变了 d_syc 与 sycophancy 的关系) 两种类型，这个分析会强化论文的理论定位。\n\n[AGREE] R2-W2: §3 与 §6 之间的叙事张力\n这是我审稿中未显式标注但隐含关注的问题。R2 精确指出了三组声明之间的表面矛盾：\n- §3: d_syc \"captures evidential granularity\" (AUROC 0.675→0.929)\n- §6: d_syc \"encodes direction of belief change but not evidential warrant\"\n- §5: d_syc \"does not condition on input validity\"\n\n我认为这些声明之间实际上不矛盾，但论文确实未清晰阐述它们的关系。合理的调和是：d_syc 在 offline classification 设定下能区分不同 evidence strength 的 sycophantic responses（因为 stronger evidence 下 sycophantic vs valid 的行为差异更大，产生更可分的 activation pattern），但这并不意味着 d_syc 编码了 evidence warrant 本身——它编码的是\"belief change 的 magnitude\"，而非\"belief change 是否 warranted\"。§3 的 evidence-strength stratification 实际上反映了 effect size 差异，不是 warrant 感知。\n\n但这个关键区分需要论文自己明确写出来。目前的叙述让读者自行推断，容易产生混淆。\n\n[REBUT] R2-W3: \"negative result\" vs \"general principle\" 的定位问题\nR2 认为论文在局部声明与全局声明之间定位模糊。我部分不同意。\n\n论文的结构实际上是合理的渐进式论证：\n1. 局部观察：我们的 d_syc-based reward 全部失败 (§4-§5)\n2. 根因分析：d_syc 的几何特性导致 warranted/unwarranted 不可分 (§6)\n3. 有限度的一般化：discriminability is necessary but not sufficient (§8 Conclusion)\n\n第 3 步的一般化是有条件的——论文明确限定在 \"attributes where the target and its complement overlap geometrically\" (Section 8)，并以 Zhang et al. (2026) 和 Wu & Tang (2026) 为对照说明什么条件下 representation-guided reward 可以成功。这并非无边界的全局声明。\n\n但我同意 R2 关于 \"mechanistic analysis\" 措辞的保留。论文没有做 causal intervention（如 activation patching）来验证 d_syc 的因果角色，称其为\"诊断性分析\"更准确。不过这不影响整体定位的合理性。\n\n[AGREE] R2-W4: SMART 讨论逻辑不精确\nR2 准确指出了逻辑漏洞：如果 sycophancy 的 target/complement 在几何上不可分 (§6 的核心论点)，那 SMART 的 per-step process reward 如何绕过这个根本限制？论文 Section 7 仅说 SMART 的成功 \"independently corroborates supervision granularity as a key factor\"，但未解释 SMART 的 per-step reward 为何不受 d_syc 同样的几何限制。\n\n可能的解释有几种：(1) SMART 可能使用了不同于 d_syc 的 reward signal，本身包含 warrant 信息；(2) per-step reward 可能在 token 级别提供了足够的信息来隐式区分 warranted vs unwarranted；(3) SMART 的成功可能依赖于其他设计选择（模型规模、数据等）。论文未分析这些可能性就直接将 SMART 作为 supervision granularity 假说的证据，逻辑上是不完整的。\n\n[REBUT] R2-W5: 标题误导性\nR2 认为标题范围过窄，论文内容远超 \"probe reward trap\"。我不同意这是一个有意义的问题。学术论文标题突出最 novel 的发现 (probe reward trap + behavioral death before distributional collapse) 是常见且合理的做法。论文的 subtitle \"Behavioral Death Before Distributional Collapse in Sycophancy Calibration\" 已提供了足够的范围信息。标题不需要涵盖所有内容——cosine failure chain 和 ACT 对比是支撑 probe reward trap 论证的组件，而非独立的并列贡献。这属于 editorial preference，不影响学术评估。\n\n[AGREE] R2-W6: Probe trap 单种子\n与我的 [W5] 中的相关观点一致。论文 Limitations 中已承认 \"The probe reward trap (C2) is demonstrated with a single seed\"，且补充了 \"SFT training is more deterministic than RL\" 的论点。但我仍认为至少 2-3 个 seed 是必要的，特别是对于论文最核心的发现。\n\n[AGREE] R2-W7: ACT vs GRPO 多维混淆\n与我的 [W3] 完全一致。R2 特别提到 ground-truth labels vs d_syc/R₃ 的区别，这是一个重要的额外混淆维度——ACT 使用人工标注的 valid/invalid pairs 作为 gold labels，而 GRPO 使用 d_syc 和 NLI 自动评分，数据质量本身就存在差距。\n\n---\n\n### Missing References\n\n[AGREE] R2-MR1: Goodhart's Law (Manheim & Garrabrant 2019) — 如上述 [W1] 回应所述，这是重要遗漏。\n\n[AGREE] R2-MR2: \"Playing Devil's Advocate\" (arXiv:2605.21006, May 2026) — 如果该论文展示 off-the-shelf persona vectors 可以有效减轻 sycophancy 且无需 gradient-based training，这与本文形成有意义的对照：inference-time 方法可以绕过 probe reward trap (与 Papadatos & Freedman 2024 的 inference-time probe penalties 类似)。应纳入 Related Work。\n\n[AGREE] R2-MR3: Wu & Tang (2026) 几何可分性量化标准的更深入讨论。论文 Section 6 已引用该工作，但仅定性提及 \"concept directions applied via advantage modification in GRPO achieve 100% validation accuracy...where shortcut behaviors are geometrically separable\"。量化比较 d_syc 的几何可分性与 Wu & Tang 的 reward-hacking directions 的可分性差异，会显著强化论文的理论贡献。\n\n[REBUT] R2-MR4: Contrastive Causal Mediation (CCM, NeurIPS 2025)。论文未声称做 causal mediation analysis。d_syc 的提取是 contrastive activation analysis (沿 CAA 的方法论)，不是 causal mediation。引用 CCM 可能有参考价值，但将其列为\"missing reference\"过于强势——论文没有做 causal claims 需要 CCM 来支撑。\n\n---\n\n### Scores 对比\n\n| 维度 | R1 | R2 | 差异分析 |\n|------|------|------|----------|\n| Soundness | 3/5 | 3/5 | 一致。核心观察扎实，但因果归因（supervision granularity）的混淆变量是共同关注点。 |\n| Excitement | 3.5/5 | 2.5/5 | **显著分歧。** 我认为 behavioral death before distributional collapse 的发现具有独立的新颖性和实践价值 (对 reward hacking 监控的直接启示)，即便 Goodhart's Law 框架未被讨论。R2 的 2.5 可能受到 \"这只是 Goodhart's Law 的一个 instance\" 的判断影响。我认为 specific mechanistic characterization (时间解耦、失败模式分类、几何不可分性论证) 超越了对已知原则的简单实例化，值得 3.5。 |\n| Contribution | 3/5 | 3/5 | 一致。负面结果有价值但缺少 actionable solution。 |\n| Reproducibility | 3/5 | 3/5 | 一致。 |\n| Overall | 3.0 | 3.0 | 一致。Findings level。 |\n| Confidence | 4/5 | 4/5 | 一致。 |\n\n**关于 Excitement 的分歧：** 我维持 3.5/5。理由：(1) 1,300-step 时间解耦是一个可被其他研究者立即用于改进监控系统的发现；(2) 论文提出的 \"discriminability ≠ reward utility\" 框架虽未完美论证，但指出了 representation engineering 社区需要正视的盲区；(3) stubbornness taxonomy 为理解 RLHF/SFT 训练的微观行为提供了新工具。R2 的 2.5 (Potentially Interesting) 对这些贡献评价偏低。\n",
    "reviewer_id": "1",
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 405 · 2026-05-24T09:58:53.442082+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3767
}
```

</details>

---


### Assistant

_source line 406 · 2026-05-24T09:59:02.732282+00:00_

已提交对 Reviewer 2 全部意见的逐条回应。

核心判断：
- **6 条 [AGREE]**（W1 Goodhart 缺失、W2 叙事张力、W4 SMART 逻辑、W6 单种子、W7 ACT混淆、S1-S5 全部同意）
- **2 条 [REBUT]**（W3 定位模糊——论文的渐进式论证结构实际合理；W5 标题误导——标题突出最 novel 发现是合理做法）
- **Missing References**：同意 MR1-MR3，反驳 MR4（CCM 与论文方法论不对应）
- **Excitement 评分分歧**：我维持 3.5 vs R2 的 2.5，主要因为时间解耦发现的实践价值和 stubbornness taxonomy 的独立贡献

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1"
}
```

</details>

---


## Round 13

## Round 13

44 recorded events


### User

_source line 407 · 2026-05-24T12:11:20.228401+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责 **方法严谨性 + 实验设计**。

## Venue 信息
- **EMNLP 2026** (ARR May cycle)
- 截止日期: 2026-05-25
- Long Paper: 8 页正文限制, references 无限制
- 模板: ACL style (两栏)
- 匿名: Double-blind (无 anonymity period)
- Mandatory Limitations section (不计入页数)
- Appendix 允许，在 references 之后，不计入页数，reviewer 无义务审阅

## 论文文件
- LaTeX: `projects/contrastive_entrain_calib/docs/paper/main.tex`（各 section 在 `sections/` 目录下）
- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/submitted.pdf`

## 你的审查侧重

重点审查以下方面，逐条给出评价和评分：

### 1. 实验设计与控制变量
- GRPO group_size=2（远低于标准 8-64）是否构成致命替代解释？gs=8 ablation 仅 3 个 checkpoint 是否充分？
- ACT vs GRPO 对比存在多维度 confound（sequence length 256 vs 1024, data source, dropout, LoRA α, modules 数量）——"supervision granularity" 因果声明是否过强？
- 256-token truncation 将 AUROC 从 0.827 降至 0.60——这是否足以解释 cosine failure，而非论文声称的 d_syc 语义局限？
- Probe reward trap 仅单 seed 验证——SFT 确定性更高，但 temporal decoupling 的定量结论（1300 步）是否需要多 seed 确认？

### 2. 数据质量与统计有效性
- 181 个 contrastive pairs 全部由 GPT-4.1 生成，无人工验证/IAA——d_syc 是否可能捕捉生成风格而非 sycophancy 语义？
- Evidence strength 三级标注（weak/medium/strong）无 IAA 报告
- Cross-seed 分析仅 2 个 seed，rank correlation 和 variance estimation 的统计功效
- ACT seed 2 的 ToF/NoF 数据标为 "—"，降低跨 seed 可验证性

### 3. Evaluation Metric
- SyconScore harmonic mean 的选择是否充分 justify？是否应同时报告 arithmetic mean？
- collapsed methods 在 arithmetic mean 下与 vanilla 接近（0.498-0.500 vs 0.509），harmonic mean 的 zero-floor 设计是否过度惩罚？

### 4. 可复现性
- 超参数报告是否完整？
- 代码/数据可用性声明？
- 训练细节（reward weight selection 的 "diagnostic-driven iteration"）是否充分描述？

请给出：
1. **Strengths** (逐条，标号 [S1] [S2] ...)
2. **Weaknesses** (逐条，标号 [W1] [W2] ...，标注 severity: critical/warning/minor)
3. **Questions** (需要作者回答的问题)
4. **Missing References** (遗漏的重要相关工作)
5. **Detailed Comments** (逐 section 详细意见)
6. **Overall Assessment** (1-5 分，参考 ARR 标准；置信度 1-5)
7. **Reproducibility** (1-5 分)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 408 · 2026-05-24T12:11:32.895748+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 409 · 2026-05-24T12:11:38.036266+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/review_reviewer_1_a4d5bbcf.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 5140
}
```

</details>

---


### Tool call

_source line 410 · 2026-05-24T12:11:38.339509+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
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

_source line 411 · 2026-05-24T12:11:38.492363+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 412 · 2026-05-24T12:11:43.795640+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 413 · 2026-05-24T12:11:45.604953+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/submitted.pdf",
  "project": "contrastive_entrain_calib",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/submitted.pdf",
    "project": "contrastive_entrain_calib",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 414 · 2026-05-24T12:11:50.429295+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

I found detailed information about ACL ARR 2026 reviewer guidelines and review criteria. Here are the key points:

## Review Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Overall Recommendation Criteria

The Overall assessment score is an explicit recommendation for the outcome of 
…[truncated 1169 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6633
}
```

</details>

---


### Tool result

_source line 415 · 2026-05-24T12:11:51.893516+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 410.6}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 396.8}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 458.7}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 436.6}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 488.2}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 448.6}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 498.4}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_ima
…[truncated 548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6288
}
```

</details>

---


### Tool call

_source line 416 · 2026-05-24T12:11:59.375845+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with ALL scoring dimensions, their scales, and descriptions. Include: soundness, excitement, overall assessment, confidence, reproducibility, and any other dimensions. List every score option with its description."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with ALL scoring dimensions, their scales, and descriptions. Include: soundness, excitement, overall assessment, confidence, reproducibility, and any other dimensions. List every score option with its description."
  }
}
```

</details>

---


### Tool call

_source line 417 · 2026-05-24T12:12:00.280179+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 418 · 2026-05-24T12:12:00.883076+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 419 · 2026-05-24T12:12:01.286429+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 420 · 2026-05-24T12:12:01.387379+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 421 · 2026-05-24T12:12:02.196556+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1313
}
```

</details>

---


### Tool result

_source line 422 · 2026-05-24T12:12:02.198052+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 810
}
```

</details>

---


### Tool call

_source line 423 · 2026-05-24T12:12:02.350241+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 424 · 2026-05-24T12:12:02.753717+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 425 · 2026-05-24T12:12:03.160981+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 810
}
```

</details>

---


### Tool result

_source line 426 · 2026-05-24T12:12:03.513264+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 759
}
```

</details>

---


### Tool result

_source line 427 · 2026-05-24T12:12:06.979389+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## 1. **Reviewer Confidence**
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## 2. **Soundness**
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. **Excitement**
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

## 4. **Overall Assessment**
- **5**: Consider for Award (top 2.5% papers)
- **4.5**: Borderline Award
- **4**: Conference acceptance
- **3.5**: Borderline Conference
- **3**: Findings acceptance
- **2.5**: Borderline Findings
- **2**: Resubmit next cycle
- **1.5**: Resubmit after next cycle
- **1**: Do not resubmit

## 5. **Reproducibility**
- **5**: "They could easily reproduce the results."
- **4**: "They could mostly reproduce the results, but there may be some variation."
- **3**: "They could reproduce the results with some difficulty."
- **2**: "They woul
…[truncated 763 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7603
}
```

</details>

---


### Tool call

_source line 428 · 2026-05-24T12:12:13.105310+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 429 · 2026-05-24T12:12:13.610120+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 430 · 2026-05-24T12:12:14.415123+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1309
}
```

</details>

---


### Tool result

_source line 431 · 2026-05-24T12:12:14.416386+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---


### Tool call

_source line 432 · 2026-05-24T12:12:14.416725+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 433 · 2026-05-24T12:12:14.912919+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 434 · 2026-05-24T12:12:16.325546+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1908
}
```

</details>

---


### Tool result

_source line 435 · 2026-05-24T12:12:16.329167+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1416
}
```

</details>

---


### Tool call

_source line 436 · 2026-05-24T12:12:16.332090+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 437 · 2026-05-24T12:12:17.288094+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 438 · 2026-05-24T12:12:17.288537+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/submitted.pdf",
  "project": "contrastive_entrain_calib",
  "pages": "11",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/submitted.pdf",
    "project": "contrastive_entrain_calib",
    "pages": "11",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 439 · 2026-05-24T12:12:17.444828+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 310.9}], \"total_pages\": 11, \"rendered_pages\": 1, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 156
}
```

</details>

---


### Tool call

_source line 440 · 2026-05-24T12:12:32.822091+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 441 · 2026-05-24T12:12:33.429819+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 607
}
```

</details>

---


### Tool call

_source line 442 · 2026-05-24T12:14:18.631623+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the key reviewer guidelines, especially: what reviewers should focus on, how to assess soundness, how to handle limitations, what counts as a weakness vs a strength, guidance on novelty vs soundness tradeoffs, and any specific instructions about experimental rigor."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the key reviewer guidelines, especially: what reviewers should focus on, how to assess soundness, how to handle limitations, what counts as a weakness vs a strength, guidance on novelty vs soundness tradeoffs, and any specific instructions about experimental rigor."
  }
}
```

</details>

---


### Tool result

_source line 443 · 2026-05-24T12:14:27.515432+00:00_

# Key ARR Reviewer Guidelines Summary

## Core Assessment Focus

Reviewers should evaluate papers across three dimensions: **soundness** (technical validity), **excitement** (personal interest), and **overall recommendation** (composite judgment). These are orthogonal—a technically sound paper need not be personally exciting, yet may still merit acceptance based on impact.

## Soundness Assessment

"The _soundness_ scores must be justified by the text of the review. If you give a low _Soundness_ score without finding any major faults, this means that your review is not a faithful explanation of your recommendation" (I3).

Key soundness elements include:
- Technical correctness and proof validity
- Appropriate methodology for research questions
- Sufficient statistical rigor and significance testing
- Reproducibility details and transparency

## Limitations vs. Weaknesses

A critical distinction: "A good review should not just take the limitations and list them as weaknesses or reasons to reject. If the reviewer wishes to argue that acknowledged limitations completely invalidate the work, this should be appropriately motivated" (H16).

Limitations are inherent to all research; they become weaknesses only if they undermine the paper's core claims.

## Novelty vs. Soundness Tradeoffs

The guidelines reject strict SOTA requirements: "SOTA results are neither necessary nor sufficient for a _scientific_ contribution" (H5). Papers may contribute through efficiency, interpretability, fairness, or theoretical insights instead.

Novel work is actually harder to publish and shouldn't face unfair conservatism from reviewers.

## Common Review Problems to Avoid

Problematic heuristics include:
- Dismissing results as "obvious in retrospect" despite lacking prior empirical validation
- Demanding experiments beyond what's needed to support claims
- Preferring specific methodologies over sound alternatives
- Expecting comparisons to closed-source systems when inappropriate

## Expe
…[truncated 706 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8883
}
```

</details>

---


### Tool call

_source line 444 · 2026-05-24T12:18:03.682310+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 审稿意见：方法严谨性 + 实验设计\n\n**论文标题**: The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 — Findings（可被 Findings 接收）\n**一句话总结**: Probe reward trap 现象的发现具有原创性和实用价值，但 GRPO 在非标准配置下的失败不足以支撑因果性结论，ACT 对比实验存在多维度混淆变量削弱了 \"supervision granularity\" 的核心解释。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 (Acceptable) | 核心发现（probe reward trap、d_syc 判别力）有充分支撑，但 GRPO 配置偏离标准、ACT 对比多重混淆削弱了 supervision granularity 的因果声明 |\n| Excitement | 3/5 (Interesting) | Probe reward trap 对 alignment 社区有实际预警价值；但贡献集中在现象描述层面，解决方案（ACT 优越性）的证据链不完整 |\n| Reproducibility | 3/5 (Some difficulty) | 承诺匿名 GitHub 代码/数据；但 reward weight selection 的 \"diagnostic-driven iteration\" 描述不充分，recalibration 频率选择缺乏理论依据 |\n| Confidence | 4/5 | 仔细阅读全文并熟悉相关工作 |\n\n---\n\n## Strengths\n\n**[S1] 原创性现象识别与精确刻画**\nProbe reward trap 的核心发现——行为死亡（ToF→0 at step 500）先于分布坍塌（entropy collapse at step ~1800）约 1,300 步（Table 3, Figure 3）——是对 reward hacking 文献的实质贡献。这一时间解耦意味着 entropy monitoring（当前最常用的 reward hacking 检测手段）会系统性遗漏这类故障。这一发现不依赖于后续比较实验的质量，独立成立。\n\n**[S2] 系统性诊断链方法论**\nTable 2 中 F1a→F1b→F1c→F1d→F1e 的逐步诊断链设计干净、逻辑清晰：从点积饱和（F1a）到 raw cosine 的 gap 过小（F1b）到 recalibration 引入 reward discontinuity（F1c）到 5× scaling 仍在 noise floor（F1d），每一步都排除一个备选方案。这是良好的实验方法论。\n\n**[S3] 跨模型验证增强可信度**\nd_syc 判别力在 Qwen3-8B（AUROC 0.827）和 Llama-3-8B（AUROC 0.779）上均展现定性一致的模式（Table 1, Figure 2）：最佳层位于上层1/3、evidence strength 梯度单调递增、跨知识域泛化（per-domain AUROC 0.751→0.844）。两个架构差异显著的模型家族（Qwen vs Llama）出现一致结果，排除了模型特异性解释。\n\n**[S4] Evidence strength 梯度提供内部效度验证**\nd_syc 的 AUROC 从 weak (0.675) 到 medium (0.883) 再到 strong (0.929) 单调递增（Table 1），反映方向确实编码了 sycophancy 的语义强度而非仅表面特征。这种 monotonic gradient 是对 d_syc 有效性的非平凡验证。\n\n**[S5] 问题意识具有实践价值**\n论文解决的问题——representation-level signal 的判别力是否能直接转化为 reward utility——对于当前使用 linear probe / CCS / contrastive direction 做 alignment 的研究路线有直接的方法论警示。Section 5 的结论\"discriminability is necessary but not sufficient for reward utility\"是简洁有力的。\n\n**[S6] 写作清晰、结构紧凑**\n论文在 8 页内涵盖了方向提取、五种 reward 公式、探测实验、跨方法对比和消融，逻辑链完整。Figure 1 的双面板设计（discriminability + behavioral death）高效传达了核心信息。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**[W1] [critical] GRPO group_size=2 远低于标准配置，构成核心替代解释**\n- 具体位置：Section 2.2, Table 6 (Appendix A), Section 6\n- 问题：论文使用 group_size=2，而 Shao et al. (2024) 的原始 GRPO 论文及后续标准实践使用 8-64。group_size=2 意味着每个 prompt 仅生成 2 个 completion 用于 pairwise 排序，这极大限制了 advantage estimation 的质量——方差最大化，ranking signal 退化为 coin-flip 式的二选一比较。论文承认这 \"below the typical range of 8-64\"（Section 2.2/F1 区域），但未充分论证为什么这种极端配置下的失败能代表 GRPO 方法本身的局限。\n- gs=8 ablation 因 \"all below vanilla\" 而提前终止（Section 6 提到 est≈0.005, p=0.014），但（a）终止标准未公开，（b）更大 group size（16/32/64）完全缺失，（c）GRPO 在 gs=2 下可能需要完全不同的 learning rate / epoch 配置。\n- 为什么影响接收：论文的核心叙事之一是 \"GRPO-based formulations fail → supervision granularity is the key\"。如果 GRPO 在标准配置下可以工作，则 supervision granularity 的因果推断坍塌。这不是 \"acknowledge limitation\" 可以解决的问题——它直接影响 Section 6 的中心结论。\n- 建议修改方向：(1) 至少补充 gs=16 或 gs=32 的完整训练轨迹（全部 checkpoint）；或 (2) 将 Section 6 的结论从因果声明弱化为 \"under the tested configurations\" 的条件性陈述，并在 abstract/conclusion 中相应修改。\n\n**[W2] [critical] ACT vs GRPO 对比存在多维度 confound，\"supervision granularity\" 因果声明过强**\n- 具体位置：Section 2.4, Section 6, Table 5\n- 问题：ACT 和 GRPO 之间至少有 5 个维度同时不同：\n  1. Supervision granularity: per-token (ACT) vs per-completion (GRPO)\n  2. Sequence length: 256 tokens (GRPO truncation) vs 1024 tokens (ACT full-length)\n  3. Data source: online generation (GRPO) vs curated contrastive pairs (ACT)\n  4. Dropout: 0 (GRPO) vs 0.05 (ACT)\n  5. LoRA modules: 4 (GRPO) vs more (ACT full config)\n- LoRA-controlled ablation（Table 5）仅控制了第 5 个维度（adapter capacity），其他 4 个维度仍然混淆。reduced-LoRA ACT (SyconScore=0.326) > full ACT (SyconScore=0.301) 这一结果本身很有趣——说明容量不是关键因素——但 2-4 维度的混淆仍然存在。\n- 论文声称 \"supervision granularity—per-token vs per-completion—as the most plausible explanatory variable\"（Section 6），但 sequence length 256→1024 本身可能就是决定性因素（d_syc AUROC 在 256 token 下从 0.827 降至 0.60，见 Section 4）。\n- 为什么影响接收：这是论文提出的机制解释（mechanism claim），如果无法从混淆变量中隔离出 supervision granularity 的独立效应，论文的解释性贡献大打折扣。\n- 建议修改方向：(1) 设计 crossing experiment——将 ACT 限制为 256 tokens（匹配 GRPO），或将 GRPO 扩展到 1024 tokens（匹配 ACT）；(2) 至少将结论修改为 \"supervision granularity is one plausible candidate among several confounded factors\"，而非 \"the strongest candidate\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**[W3] [warning] 181 个 contrastive pairs 全部 GPT-4.1 生成，无人工验证或 IAA**\n- 具体位置：Section 2.1\n- 问题：d_syc 的有效性完全依赖于 contrastive pairs 的质量。论文描述了 automated validation（response length difference <0.19, shared opening phrase ≤2 words），但这仅控制表面格式，不验证语义正确性。d_syc 可能捕捉 GPT-4.1 的生成风格（如特定句法模式）而非 sycophancy 语义本身。Evidence strength 的三级标注（weak/medium/strong）同样缺乏 IAA 报告。\n- 建议：补充至少 50 对的人工验证（2 名标注者 + IAA），或提供 d_syc 在人工标注 sycophancy 数据集（如 Sharma et al., 2024 的人工标注子集）上的交叉验证结果。\n\n**[W4] [warning] Probe reward trap 仅单 seed 验证，temporal decoupling 的精确定量结论需多 seed 确认**\n- 具体位置：Section 5, Table 3, Limitations\n- 问题：论文报告 behavioral death at step 500, distributional collapse at step ~1800, 定义 1,300-step lag。虽然 SFT 的确定性高于 RL，但 (a) random initialization of LoRA adapters, (b) data shuffling, (c) online recalibration 的 stochasticity 都可能影响这一精确时间点。论文在 Limitations 中承认了这一点，但 1,300 步这个具体数字已进入 abstract 和核心叙事。\n- 建议：补充 3-5 个 seed 的实验，报告 behavioral death 和 distributional collapse 时间点的均值和标准差。如果 seed 间方差大，则应修改叙事中对 \"1,300-step lag\" 的精确描述。\n\n**[W5] [warning] Cross-seed 分析仅 2 个 seed，统计功效不足**\n- 具体位置：Section 3 (training stability), Table 4, Section 6\n- 问题：(a) 2 个 seed 无法可靠估计 rank correlation 或方差；(b) ACT seed 2 的 ToF/NoF 数据标为 \"—\"（Table 4），进一步削弱跨 seed 可验证性。论文基于 2 个 seed 做出 \"both seeds maintain above-vanilla performance throughout training\" 的声明（Section 6），但 n=2 的统计功效极低。\n- 建议：至少补充到 3 个 seed（最好 5 个），并报告 SyconScore 的 seed-wise 标准差。\n\n**[W6] [warning] SyconScore harmonic mean 的 zero-floor 设计可能过度惩罚 collapsed methods**\n- 具体位置：Section 2.5, Table 4\n- 问题：当 ToF=0 时，harmonic mean 自动归零，这是 by design 的。但 Table 4 显示在 arithmetic mean 下，collapsed methods（0.498-0.500）与 vanilla（0.509）近乎不可区分。这意味着 SyconScore 的 \"dramatic\" 差异（harmonic 下 0 vs 0.509）实质上被 metric 选择放大了。论文应该更充分地 justify 为什么 harmonic mean 是正确的评价方式。\n- 反面论证：可以论证 ToF=0 确实是灾难性失败（模型完全无法接受纠正），因此 zero-floor 是合理的惩罚。但这一论证应显式出现在论文中。\n- 建议：(1) 同时报告 arithmetic mean 和 harmonic mean（Table 4 已部分做到，但正文叙事几乎完全依赖 harmonic mean）；(2) 在 Section 2.5 中加入 1-2 句解释为什么 harmonic mean 的 zero-floor 在 sycophancy calibration 场景下是 desirable property。\n\n**[W7] [warning] 256-token truncation 对 cosine failure 的替代解释未被充分排除**\n- 具体位置：Section 4, Section 2.2\n- 问题：GRPO 中 completion 被截断为 256 tokens，d_syc 的 AUROC 在 256 tokens 下从 0.827 降至约 0.60（Section 1/4）。Section 4 将 cosine failure 归因于 d_syc 的 \"semantic limitation\"，但一个更简约的解释是：256 tokens 不足以让模型产生足够的 sycophantic/non-sycophantic behavioral signal，truncation 本身破坏了 d_syc 的信号质量。如果在 full-length responses 上 cosine reward 能工作，那问题出在 truncation 而非 d_syc。\n- 建议：补充一个在 full-length（1024 token）responses 上使用 cosine reward 的实验，或明确论证为什么 truncation 是 GRPO 方法不可避免的约束。\n\n---\n\n## 小问题（不影响接收）\n\n- **[M1]** Appendix A \"diagnostic-driven iteration\" 描述 reward weight selection（w₁ 从 0.25 调至 0.10，w₃ 从 0 调至 0），但 \"diagnostic\" 的具体定义（哪些指标、什么阈值触发调整）未公开，影响可复现性。\n- **[M2]** Table 2 中 \"Reward Cost\" 列的 \"Base cost\" / \"Gap too small\" / \"Reward discontinuity\" / \"Voltage insufficient\" 等描述不够 formal——建议用定量 threshold 替代定性描述。\n- **[M3]** Figure 4 的 Y 轴（SyconScore）范围 0-0.50，但两条 GRPO 曲线大部分时间在 0.10 以下——考虑用 inset 或分面放大低值区域以增强可读性。\n- **[M4]** Stubbornness Taxonomy（Appendix B）将 181 个 valid-correction responses 分为 5 类 failure mode，但类别定义和标注同样缺乏 IAA。\n\n---\n\n## Questions（需要作者回答）\n\n**Q1**: GRPO group_size=2 是出于计算预算考虑还是方法论选择？在标准 group_size（16 或 32）下的完整训练轨迹是否可行？如果计算预算不允许，是否可以在更小的模型（如 1.5B）上验证 group_size scaling？\n\n**Q2**: 是否可以设计 crossing experiment 隔离 supervision granularity 的效应？具体地：(a) ACT with 256-token truncation, (b) per-token GRPO (if feasible), (c) GRPO with curated pairs instead of online generation.\n\n**Q3**: 181 个 contrastive pairs 是否可以在已有的人工标注 sycophancy 数据集上做交叉验证（如 Sharma et al., 2024 的数据）？d_syc 在非 GPT-4.1 生成的数据上的判别力如何？\n\n**Q4**: Probe reward trap 的 1,300-step lag 在不同 seed 下的方差有多大？是否存在 seed 使 behavioral death 时间点显著不同（如推迟到 step 800+）？\n\n**Q5**: 在 full-length (1024 token) responses 上，cosine-based reward（F1b 或 F1c）是否仍然失败？这将区分 \"truncation artifact\" 和 \"d_syc semantic limitation\" 两种解释。\n\n**Q6**: Evidence strength 的三级标注标准是什么？标注者（GPT-4.1）在边界案例上的一致性如何？是否尝试过更细粒度（如 5 级）或连续标注？\n\n---\n\n## Missing References\n\n**[R1]** Perez et al. (2022), \"Discovering Language Model Behaviors with Model-Written Evaluations\" — 最早系统发现 sycophancy 行为的工作之一，论文未引用。与本文的 contrastive pair 生成方法论有直接相关性。\n\n**[R2]** 论文引用了 Casper et al. (2023) 关于 reward hacking，但未引用 Skalse et al. (2022) 关于 reward misspecification 的理论框架——虽然 Section 7 提到了 Skalse et al.，但可以更明确地将 probe reward trap 定位在这一理论框架中。\n\n**[R3]** Turpin et al. (2023), \"Language Models Don't Always Say What They Think\" — 与 sycophancy 的表征层面分析（d_syc 编码内部状态 vs 输出行为的分离）直接相关。\n\n---\n\n## Detailed Comments（逐 Section）\n\n### Section 1 (Introduction)\n- 第一段 claim \"representation engineering (Zou et al., 2025) reveals that large language models encode sycophancy as a linear direction in their residual stream\"——但 Zou et al. 2025 的工作是否专门讨论 sycophancy？如果是作者自己发现的，应区分 prior work 和本文贡献的边界。\n- Abstract 声称 \"the trap arises under SFT with stopped gradients, is independent of RL optimization dynamics\"——这一 claim 的证据是 Table 3 的单 seed SFT 实验，支撑力度适中但需多 seed 加强。\n\n### Section 2 (Experimental Framework)\n- 2.1: contrastive pair 生成流程描述清晰，但 14/200 被丢弃的 pairs 的 failure 模式未报告——了解失败原因有助于评估 automated validation 的覆盖盲区。\n- 2.2: group_size=2 的选择理由 \"to minimize completions with 8B-parameter models\" 不充分。计算成本可以通过减少 training steps 或使用 gradient accumulation 来 offset。\n- 2.5: SyconScore 的 zero-floor property 应在此处更明确地讨论（见 W6）。\n\n### Section 3 (Direction Discriminability)\n- 这是论文最扎实的部分。Cross-model、cross-layer、cross-domain 的一致性分析是全面的。\n- Per-domain AUROC 分析（0.751→0.844）是一个好的 sanity check。\n- Minor：Figure 2 的 Y 轴刻度在两个模型间不同（Qwen 0.65-0.85 vs Llama 0.65-0.80），建议统一以便直观比较。\n\n### Section 4 (Cosine R_l: Structural Failure)\n- 诊断链方法论（Table 2）是论文的方法论亮点之一。\n- 但 256-token truncation 作为 confound 未被充分分离（见 W7）。\n- F1e (5× scaling) 的失败描述为 \"noise floor surfaces the fundamental limitation: R₁ saturates at 0.0998 by step 500\"——但 0.0998 作为 absolute value 的 semantic 含义不清楚，建议补充 scale-relative 的解释。\n\n### Section 5 (The Probe Reward Trap)\n- 核心发现清晰有力。Table 3 的逐步轨迹是直观的证据。\n- Figure 3 有效传达了 entropy-monitoring 的盲区。\n- \"A dilemma for direction-based rewards\"（第 6 页）的讨论是论文最有洞察力的段落之一。\n- 但 \"the 1,300-step lag\" 的精确性需多 seed 支撑（见 W4）。\n\n### Section 6 (When Does Discriminability Fail as Reward Utility?)\n- 这一节的因果声明是论文最薄弱的部分（见 W1, W2）。\n- Table 5 的 LoRA ablation 设计思路正确，但只隔离了一个维度。\n- \"SMART's per-step success (Bergi et al., 2025)\" 作为独立佐证被引用——但这是 different task, different model, different setup，佐证力度有限。\n\n### Section 7 (Related Work)\n- 覆盖面广，分类合理。\n- \"Future directions\" 段提到 SMART 和 MCTS——这更适合放在 Discussion/Conclusion 而非 Related Work。\n\n### Section 8 (Conclusion)\n- 简洁有力，但结论中 \"a LoRA-controlled ablation identifies supervision granularity as the strongest candidate\" 应弱化为条件性陈述（见 W2）。\n\n### Limitations\n- 诚实地承认了单 seed、2 seeds 等问题，但承认 ≠ 解决。\n- 代码/数据可用性声明充分（匿名 GitHub）。\n\n---\n\n## 主要优势总结\n\n1. **Probe reward trap** 是一个有原创性的发现，对 alignment 社区有直接实用价值\n2. **诊断链方法论**（Table 2）系统而干净\n3. **跨模型验证** 增强了 d_syc 发现的可信度\n4. **写作质量** 在 8 页内实现了高信息密度\n5. **问题定义**（discriminability ≠ reward utility）简洁有力\n\n## 主要不足总结\n\n1. **GRPO gs=2** 配置过于偏离标准，可能使 GRPO 失败成为配置 artifact 而非方法局限 [critical]\n2. **ACT vs GRPO 5 维度混淆**，supervision granularity 的因果声明证据不足 [critical]\n3. **数据质量**：全合成、无 IAA、无人工验证 [warning]\n4. **统计功效**：单 seed（probe trap）、2 seeds（cross-seed）[warning]\n\n---\n\n## 最终评分\n\n| 项目 | 分数 |\n|------|------|\n| **Overall Assessment** | **3.0** — Findings |\n| Soundness | 3/5 (Acceptable) |\n| Excitement | 3/5 (Interesting) |\n| Reproducibility | 3/5 (Some difficulty) |\n| Confidence | 4/5 (Quite sure) |\n\n**理由**: 论文的核心贡献（probe reward trap 现象发现 + d_syc 判别力分析）达到了 Findings 的标准——soundness 足够支撑主要 claim，reproducibility 有代码承诺。但两个 critical 问题（GRPO 非标准配置、ACT 对比多重混淆）使得论文的解释性贡献（supervision granularity 是关键因素）缺乏充分证据，阻碍 main conference 接收。如果作者能补充 (1) 标准 group_size 下的 GRPO 实验和 (2) 至少一个 crossing experiment 隔离 supervision granularity，Overall 可提升至 3.5。\n",
  "reviewer_id": "1",
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 审稿意见：方法严谨性 + 实验设计\n\n**论文标题**: The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 — Findings（可被 Findings 接收）\n**一句话总结**: Probe reward trap 现象的发现具有原创性和实用价值，但 GRPO 在非标准配置下的失败不足以支撑因果性结论，ACT 对比实验存在多维度混淆变量削弱了 \"supervision granularity\" 的核心解释。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 (Acceptable) | 核心发现（probe reward trap、d_syc 判别力）有充分支撑，但 GRPO 配置偏离标准、ACT 对比多重混淆削弱了 supervision granularity 的因果声明 |\n| Excitement | 3/5 (Interesting) | Probe reward trap 对 alignment 社区有实际预警价值；但贡献集中在现象描述层面，解决方案（ACT 优越性）的证据链不完整 |\n| Reproducibility | 3/5 (Some difficulty) | 承诺匿名 GitHub 代码/数据；但 reward weight selection 的 \"diagnostic-driven iteration\" 描述不充分，recalibration 频率选择缺乏理论依据 |\n| Confidence | 4/5 | 仔细阅读全文并熟悉相关工作 |\n\n---\n\n## Strengths\n\n**[S1] 原创性现象识别与精确刻画**\nProbe reward trap 的核心发现——行为死亡（ToF→0 at step 500）先于分布坍塌（entropy collapse at step ~1800）约 1,300 步（Table 3, Figure 3）——是对 reward hacking 文献的实质贡献。这一时间解耦意味着 entropy monitoring（当前最常用的 reward hacking 检测手段）会系统性遗漏这类故障。这一发现不依赖于后续比较实验的质量，独立成立。\n\n**[S2] 系统性诊断链方法论**\nTable 2 中 F1a→F1b→F1c→F1d→F1e 的逐步诊断链设计干净、逻辑清晰：从点积饱和（F1a）到 raw cosine 的 gap 过小（F1b）到 recalibration 引入 reward discontinuity（F1c）到 5× scaling 仍在 noise floor（F1d），每一步都排除一个备选方案。这是良好的实验方法论。\n\n**[S3] 跨模型验证增强可信度**\nd_syc 判别力在 Qwen3-8B（AUROC 0.827）和 Llama-3-8B（AUROC 0.779）上均展现定性一致的模式（Table 1, Figure 2）：最佳层位于上层1/3、evidence strength 梯度单调递增、跨知识域泛化（per-domain AUROC 0.751→0.844）。两个架构差异显著的模型家族（Qwen vs Llama）出现一致结果，排除了模型特异性解释。\n\n**[S4] Evidence strength 梯度提供内部效度验证**\nd_syc 的 AUROC 从 weak (0.675) 到 medium (0.883) 再到 strong (0.929) 单调递增（Table 1），反映方向确实编码了 sycophancy 的语义强度而非仅表面特征。这种 monotonic gradient 是对 d_syc 有效性的非平凡验证。\n\n**[S5] 问题意识具有实践价值**\n论文解决的问题——representation-level signal 的判别力是否能直接转化为 reward utility——对于当前使用 linear probe / CCS / contrastive direction 做 alignment 的研究路线有直接的方法论警示。Section 5 的结论\"discriminability is necessary but not sufficient for reward utility\"是简洁有力的。\n\n**[S6] 写作清晰、结构紧凑**\n论文在 8 页内涵盖了方向提取、五种 reward 公式、探测实验、跨方法对比和消融，逻辑链完整。Figure 1 的双面板设计（discriminability + behavioral death）高效传达了核心信息。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**[W1] [critical] GRPO group_size=2 远低于标准配置，构成核心替代解释**\n- 具体位置：Section 2.2, Table 6 (Appendix A), Section 6\n- 问题：论文使用 group_size=2，而 Shao et al. (2024) 的原始 GRPO 论文及后续标准实践使用 8-64。group_size=2 意味着每个 prompt 仅生成 2 个 completion 用于 pairwise 排序，这极大限制了 advantage estimation 的质量——方差最大化，ranking signal 退化为 coin-flip 式的二选一比较。论文承认这 \"below the typical range of 8-64\"（Section 2.2/F1 区域），但未充分论证为什么这种极端配置下的失败能代表 GRPO 方法本身的局限。\n- gs=8 ablation 因 \"all below vanilla\" 而提前终止（Section 6 提到 est≈0.005, p=0.014），但（a）终止标准未公开，（b）更大 group size（16/32/64）完全缺失，（c）GRPO 在 gs=2 下可能需要完全不同的 learning rate / epoch 配置。\n- 为什么影响接收：论文的核心叙事之一是 \"GRPO-based formulations fail → supervision granularity is the key\"。如果 GRPO 在标准配置下可以工作，则 supervision granularity 的因果推断坍塌。这不是 \"acknowledge limitation\" 可以解决的问题——它直接影响 Section 6 的中心结论。\n- 建议修改方向：(1) 至少补充 gs=16 或 gs=32 的完整训练轨迹（全部 checkpoint）；或 (2) 将 Section 6 的结论从因果声明弱化为 \"under the tested configurations\" 的条件性陈述，并在 abstract/conclusion 中相应修改。\n\n**[W2] [critical] ACT vs GRPO 对比存在多维度 confound，\"supervision granularity\" 因果声明过强**\n- 具体位置：Section 2.4, Section 6, Table 5\n- 问题：ACT 和 GRPO 之间至少有 5 个维度同时不同：\n  1. Supervision granularity: per-token (ACT) vs per-completion (GRPO)\n  2. Sequence length: 256 tokens (GRPO truncation) vs 1024 tokens (ACT full-length)\n  3. Data source: online generation (GRPO) vs curated contrastive pairs (ACT)\n  4. Dropout: 0 (GRPO) vs 0.05 (ACT)\n  5. LoRA modules: 4 (GRPO) vs more (ACT full config)\n- LoRA-controlled ablation（Table 5）仅控制了第 5 个维度（adapter capacity），其他 4 个维度仍然混淆。reduced-LoRA ACT (SyconScore=0.326) > full ACT (SyconScore=0.301) 这一结果本身很有趣——说明容量不是关键因素——但 2-4 维度的混淆仍然存在。\n- 论文声称 \"supervision granularity—per-token vs per-completion—as the most plausible explanatory variable\"（Section 6），但 sequence length 256→1024 本身可能就是决定性因素（d_syc AUROC 在 256 token 下从 0.827 降至 0.60，见 Section 4）。\n- 为什么影响接收：这是论文提出的机制解释（mechanism claim），如果无法从混淆变量中隔离出 supervision granularity 的独立效应，论文的解释性贡献大打折扣。\n- 建议修改方向：(1) 设计 crossing experiment——将 ACT 限制为 256 tokens（匹配 GRPO），或将 GRPO 扩展到 1024 tokens（匹配 ACT）；(2) 至少将结论修改为 \"supervision granularity is one plausible candidate among several confounded factors\"，而非 \"the strongest candidate\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**[W3] [warning] 181 个 contrastive pairs 全部 GPT-4.1 生成，无人工验证或 IAA**\n- 具体位置：Section 2.1\n- 问题：d_syc 的有效性完全依赖于 contrastive pairs 的质量。论文描述了 automated validation（response length difference <0.19, shared opening phrase ≤2 words），但这仅控制表面格式，不验证语义正确性。d_syc 可能捕捉 GPT-4.1 的生成风格（如特定句法模式）而非 sycophancy 语义本身。Evidence strength 的三级标注（weak/medium/strong）同样缺乏 IAA 报告。\n- 建议：补充至少 50 对的人工验证（2 名标注者 + IAA），或提供 d_syc 在人工标注 sycophancy 数据集（如 Sharma et al., 2024 的人工标注子集）上的交叉验证结果。\n\n**[W4] [warning] Probe reward trap 仅单 seed 验证，temporal decoupling 的精确定量结论需多 seed 确认**\n- 具体位置：Section 5, Table 3, Limitations\n- 问题：论文报告 behavioral death at step 500, distributional collapse at step ~1800, 定义 1,300-step lag。虽然 SFT 的确定性高于 RL，但 (a) random initialization of LoRA adapters, (b) data shuffling, (c) online recalibration 的 stochasticity 都可能影响这一精确时间点。论文在 Limitations 中承认了这一点，但 1,300 步这个具体数字已进入 abstract 和核心叙事。\n- 建议：补充 3-5 个 seed 的实验，报告 behavioral death 和 distributional collapse 时间点的均值和标准差。如果 seed 间方差大，则应修改叙事中对 \"1,300-step lag\" 的精确描述。\n\n**[W5] [warning] Cross-seed 分析仅 2 个 seed，统计功效不足**\n- 具体位置：Section 3 (training stability), Table 4, Section 6\n- 问题：(a) 2 个 seed 无法可靠估计 rank correlation 或方差；(b) ACT seed 2 的 ToF/NoF 数据标为 \"—\"（Table 4），进一步削弱跨 seed 可验证性。论文基于 2 个 seed 做出 \"both seeds maintain above-vanilla performance throughout training\" 的声明（Section 6），但 n=2 的统计功效极低。\n- 建议：至少补充到 3 个 seed（最好 5 个），并报告 SyconScore 的 seed-wise 标准差。\n\n**[W6] [warning] SyconScore harmonic mean 的 zero-floor 设计可能过度惩罚 collapsed methods**\n- 具体位置：Section 2.5, Table 4\n- 问题：当 ToF=0 时，harmonic mean 自动归零，这是 by design 的。但 Table 4 显示在 arithmetic mean 下，collapsed methods（0.498-0.500）与 vanilla（0.509）近乎不可区分。这意味着 SyconScore 的 \"dramatic\" 差异（harmonic 下 0 vs 0.509）实质上被 metric 选择放大了。论文应该更充分地 justify 为什么 harmonic mean 是正确的评价方式。\n- 反面论证：可以论证 ToF=0 确实是灾难性失败（模型完全无法接受纠正），因此 zero-floor 是合理的惩罚。但这一论证应显式出现在论文中。\n- 建议：(1) 同时报告 arithmetic mean 和 harmonic mean（Table 4 已部分做到，但正文叙事几乎完全依赖 harmonic mean）；(2) 在 Section 2.5 中加入 1-2 句解释为什么 harmonic mean 的 zero-floor 在 sycophancy calibration 场景下是 desirable property。\n\n**[W7] [warning] 256-token truncation 对 cosine failure 的替代解释未被充分排除**\n- 具体位置：Section 4, Section 2.2\n- 问题：GRPO 中 completion 被截断为 256 tokens，d_syc 的 AUROC 在 256 tokens 下从 0.827 降至约 0.60（Section 1/4）。Section 4 将 cosine failure 归因于 d_syc 的 \"semantic limitation\"，但一个更简约的解释是：256 tokens 不足以让模型产生足够的 sycophantic/non-sycophantic behavioral signal，truncation 本身破坏了 d_syc 的信号质量。如果在 full-length responses 上 cosine reward 能工作，那问题出在 truncation 而非 d_syc。\n- 建议：补充一个在 full-length（1024 token）responses 上使用 cosine reward 的实验，或明确论证为什么 truncation 是 GRPO 方法不可避免的约束。\n\n---\n\n## 小问题（不影响接收）\n\n- **[M1]** Appendix A \"diagnostic-driven iteration\" 描述 reward weight selection（w₁ 从 0.25 调至 0.10，w₃ 从 0 调至 0），但 \"diagnostic\" 的具体定义（哪些指标、什么阈值触发调整）未公开，影响可复现性。\n- **[M2]** Table 2 中 \"Reward Cost\" 列的 \"Base cost\" / \"Gap too small\" / \"Reward discontinuity\" / \"Voltage insufficient\" 等描述不够 formal——建议用定量 threshold 替代定性描述。\n- **[M3]** Figure 4 的 Y 轴（SyconScore）范围 0-0.50，但两条 GRPO 曲线大部分时间在 0.10 以下——考虑用 inset 或分面放大低值区域以增强可读性。\n- **[M4]** Stubbornness Taxonomy（Appendix B）将 181 个 valid-correction responses 分为 5 类 failure mode，但类别定义和标注同样缺乏 IAA。\n\n---\n\n## Questions（需要作者回答）\n\n**Q1**: GRPO group_size=2 是出于计算预算考虑还是方法论选择？在标准 group_size（16 或 32）下的完整训练轨迹是否可行？如果计算预算不允许，是否可以在更小的模型（如 1.5B）上验证 group_size scaling？\n\n**Q2**: 是否可以设计 crossing experiment 隔离 supervision granularity 的效应？具体地：(a) ACT with 256-token truncation, (b) per-token GRPO (if feasible), (c) GRPO with curated pairs instead of online generation.\n\n**Q3**: 181 个 contrastive pairs 是否可以在已有的人工标注 sycophancy 数据集上做交叉验证（如 Sharma et al., 2024 的数据）？d_syc 在非 GPT-4.1 生成的数据上的判别力如何？\n\n**Q4**: Probe reward trap 的 1,300-step lag 在不同 seed 下的方差有多大？是否存在 seed 使 behavioral death 时间点显著不同（如推迟到 step 800+）？\n\n**Q5**: 在 full-length (1024 token) responses 上，cosine-based reward（F1b 或 F1c）是否仍然失败？这将区分 \"truncation artifact\" 和 \"d_syc semantic limitation\" 两种解释。\n\n**Q6**: Evidence strength 的三级标注标准是什么？标注者（GPT-4.1）在边界案例上的一致性如何？是否尝试过更细粒度（如 5 级）或连续标注？\n\n---\n\n## Missing References\n\n**[R1]** Perez et al. (2022), \"Discovering Language Model Behaviors with Model-Written Evaluations\" — 最早系统发现 sycophancy 行为的工作之一，论文未引用。与本文的 contrastive pair 生成方法论有直接相关性。\n\n**[R2]** 论文引用了 Casper et al. (2023) 关于 reward hacking，但未引用 Skalse et al. (2022) 关于 reward misspecification 的理论框架——虽然 Section 7 提到了 Skalse et al.，但可以更明确地将 probe reward trap 定位在这一理论框架中。\n\n**[R3]** Turpin et al. (2023), \"Language Models Don't Always Say What They Think\" — 与 sycophancy 的表征层面分析（d_syc 编码内部状态 vs 输出行为的分离）直接相关。\n\n---\n\n## Detailed Comments（逐 Section）\n\n### Section 1 (Introduction)\n- 第一段 claim \"representation engineering (Zou et al., 2025) reveals that large language models encode sycophancy as a linear direction in their residual stream\"——但 Zou et al. 2025 的工作是否专门讨论 sycophancy？如果是作者自己发现的，应区分 prior work 和本文贡献的边界。\n- Abstract 声称 \"the trap arises under SFT with stopped gradients, is independent of RL optimization dynamics\"——这一 claim 的证据是 Table 3 的单 seed SFT 实验，支撑力度适中但需多 seed 加强。\n\n### Section 2 (Experimental Framework)\n- 2.1: contrastive pair 生成流程描述清晰，但 14/200 被丢弃的 pairs 的 failure 模式未报告——了解失败原因有助于评估 automated validation 的覆盖盲区。\n- 2.2: group_size=2 的选择理由 \"to minimize completions with 8B-parameter models\" 不充分。计算成本可以通过减少 training steps 或使用 gradient accumulation 来 offset。\n- 2.5: SyconScore 的 zero-floor property 应在此处更明确地讨论（见 W6）。\n\n### Section 3 (Direction Discriminability)\n- 这是论文最扎实的部分。Cross-model、cross-layer、cross-domain 的一致性分析是全面的。\n- Per-domain AUROC 分析（0.751→0.844）是一个好的 sanity check。\n- Minor：Figure 2 的 Y 轴刻度在两个模型间不同（Qwen 0.65-0.85 vs Llama 0.65-0.80），建议统一以便直观比较。\n\n### Section 4 (Cosine R_l: Structural Failure)\n- 诊断链方法论（Table 2）是论文的方法论亮点之一。\n- 但 256-token truncation 作为 confound 未被充分分离（见 W7）。\n- F1e (5× scaling) 的失败描述为 \"noise floor surfaces the fundamental limitation: R₁ saturates at 0.0998 by step 500\"——但 0.0998 作为 absolute value 的 semantic 含义不清楚，建议补充 scale-relative 的解释。\n\n### Section 5 (The Probe Reward Trap)\n- 核心发现清晰有力。Table 3 的逐步轨迹是直观的证据。\n- Figure 3 有效传达了 entropy-monitoring 的盲区。\n- \"A dilemma for direction-based rewards\"（第 6 页）的讨论是论文最有洞察力的段落之一。\n- 但 \"the 1,300-step lag\" 的精确性需多 seed 支撑（见 W4）。\n\n### Section 6 (When Does Discriminability Fail as Reward Utility?)\n- 这一节的因果声明是论文最薄弱的部分（见 W1, W2）。\n- Table 5 的 LoRA ablation 设计思路正确，但只隔离了一个维度。\n- \"SMART's per-step success (Bergi et al., 2025)\" 作为独立佐证被引用——但这是 different task, different model, different setup，佐证力度有限。\n\n### Section 7 (Related Work)\n- 覆盖面广，分类合理。\n- \"Future directions\" 段提到 SMART 和 MCTS——这更适合放在 Discussion/Conclusion 而非 Related Work。\n\n### Section 8 (Conclusion)\n- 简洁有力，但结论中 \"a LoRA-controlled ablation identifies supervision granularity as the strongest candidate\" 应弱化为条件性陈述（见 W2）。\n\n### Limitations\n- 诚实地承认了单 seed、2 seeds 等问题，但承认 ≠ 解决。\n- 代码/数据可用性声明充分（匿名 GitHub）。\n\n---\n\n## 主要优势总结\n\n1. **Probe reward trap** 是一个有原创性的发现，对 alignment 社区有直接实用价值\n2. **诊断链方法论**（Table 2）系统而干净\n3. **跨模型验证** 增强了 d_syc 发现的可信度\n4. **写作质量** 在 8 页内实现了高信息密度\n5. **问题定义**（discriminability ≠ reward utility）简洁有力\n\n## 主要不足总结\n\n1. **GRPO gs=2** 配置过于偏离标准，可能使 GRPO 失败成为配置 artifact 而非方法局限 [critical]\n2. **ACT vs GRPO 5 维度混淆**，supervision granularity 的因果声明证据不足 [critical]\n3. **数据质量**：全合成、无 IAA、无人工验证 [warning]\n4. **统计功效**：单 seed（probe trap）、2 seeds（cross-seed）[warning]\n\n---\n\n## 最终评分\n\n| 项目 | 分数 |\n|------|------|\n| **Overall Assessment** | **3.0** — Findings |\n| Soundness | 3/5 (Acceptable) |\n| Excitement | 3/5 (Interesting) |\n| Reproducibility | 3/5 (Some difficulty) |\n| Confidence | 4/5 (Quite sure) |\n\n**理由**: 论文的核心贡献（probe reward trap 现象发现 + d_syc 判别力分析）达到了 Findings 的标准——soundness 足够支撑主要 claim，reproducibility 有代码承诺。但两个 critical 问题（GRPO 非标准配置、ACT 对比多重混淆）使得论文的解释性贡献（supervision granularity 是关键因素）缺乏充分证据，阻碍 main conference 接收。如果作者能补充 (1) 标准 group_size 下的 GRPO 实验和 (2) 至少一个 crossing experiment 隔离 supervision granularity，Overall 可提升至 3.5。\n",
    "reviewer_id": "1",
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 445 · 2026-05-24T12:18:07.649423+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3967
}
```

</details>

---


### Tool call

_source line 446 · 2026-05-24T12:18:12.728657+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
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

_source line 447 · 2026-05-24T12:18:12.779295+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 448 · 2026-05-24T12:18:16.693309+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_7/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 449 · 2026-05-24T12:18:16.807432+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 114
}
```

</details>

---


### Assistant

_source line 450 · 2026-05-24T12:18:30.639704+00:00_

审稿意见已提交给 Review Director。

**评分摘要**：Overall 3.0 (Findings)，Soundness 3/5，Excitement 3/5，Confidence 4/5。

**两个 critical 问题**：
1. GRPO group_size=2 远低于标准 8-64，gs=8 ablation 过于稀疏——GRPO 失败可能是配置 artifact 而非方法局限
2. ACT vs GRPO 存在 5 维度同时混淆（supervision granularity / sequence length / data source / dropout / LoRA modules），LoRA ablation 仅隔离了其中一个维度，"supervision granularity 是最强候选解释" 的因果声明证据不足

**核心优势**：probe reward trap 现象本身（behavioral death 先于 distributional collapse 约 1,300 步）是原创且有实用价值的发现，诊断链方法论干净，跨模型验证增强可信度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1"
}
```

</details>

---


## Round 14

## Round 14

66 recorded events


### User

_source line 451 · 2026-05-24T12:22:58.363987+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责 **方法严谨性 + 实验有效性**。

## Venue 信息
- **目标**: EMNLP 2026（ARR May cycle）
- **ARR 提交截止**: 2026-05-25
- **格式**: Long paper，正文 8 页，参考文献不限，Limitations 不计入页数
- **模板**: ACL style
- **匿名**: Double-blind

## 论文文件
- LaTeX 主文件: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/submitted.pdf`

## 审查侧重

请重点审查以下维度：

1. **实验设计与统计有效性**
   - GRPO group_size=2 是否构成致命混淆变量（标准 8-64）？gs=8 消融仅 3 checkpoints 是否充分？
   - 256-token truncation 使 AUROC 从 0.827 降至 ~0.60——论文对 cosine failure 的归因是否仍成立？
   - Cross-seed 分析仅 2 seeds——统计功效是否足够支撑负面结论？
   - ACT seed 2 数据不完整（ToF/NoF 标记为 '—'）是否影响结论？
   - Contrastive pairs 全部由 GPT-4.1 生成，无人工验证/IAA——d_syc 可能捕捉生成风格而非 sycophancy 语义？

2. **方法论**
   - d_syc 提取流程（181 对, 5-fold CV）是否规范？
   - Reward formulations (F1-F3) 的诊断链逻辑是否严密？
   - Probe reward trap 的因果声明是否有足够证据支撑？
   - SyconScore harmonic mean 的选择是否合理？是否应同时报告 arithmetic mean？

3. **消融分析**
   - ACT vs GRPO 对比存在 5+ 维度 confound（LoRA α/modules/dropout/seq_len/data source）——reduced-LoRA ablation 是否充分隔离 supervision granularity？
   - "supervision granularity as the strongest candidate explanation" 的因果声明强度是否与证据匹配？

4. **可复现性**
   - 超参数报告是否完整？
   - 代码/数据可用性声明是否充分？

请按 ARR 审稿标准给出结构化审稿报告，包含 Summary、Strengths、Weaknesses（分 Must-Fix / Should-Fix / Minor）、Questions、Missing References、Overall Assessment（使用 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 452 · 2026-05-24T12:23:07.769827+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
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

_source line 453 · 2026-05-24T12:23:07.820576+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 454 · 2026-05-24T12:23:12.389237+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 455 · 2026-05-24T12:23:14.757191+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/submitted.pdf",
  "project": "contrastive_entrain_calib",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/submitted.pdf",
    "project": "contrastive_entrain_calib",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 456 · 2026-05-24T12:23:29.146324+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here are the key details about ACL ARR 2025-2026 reviewer guidelines:

## Reviewer Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score
Soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

### Excitement Score
Sometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

### Area Chair Metareview Scores
The new metareview score options are: 5 = Consider for Award (top 2.5% papers), 2 = Resubmit next cycle (substantial revisions completable next cycle), 1.5 = Resubmit after next cycle (substantial revisions not 
…[truncated 369 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 16757
}
```

</details>

---


### Tool result

_source line 457 · 2026-05-24T12:23:30.707659+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 410.6}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 396.8}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 458.7}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 436.6}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 488.2}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 448.6}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 498.4}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_ima
…[truncated 548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 15950
}
```

</details>

---


### Tool call

_source line 458 · 2026-05-24T12:23:40.817626+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer form criteria, scoring dimensions, and scoring scales. I need: (1) all scoring dimensions (soundness, excitement, overall, etc.), (2) the exact scale for each dimension, (3) any guidelines on what constitutes each score level, (4) any other required review fields (confidence, reproducibility, etc.)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer form criteria, scoring dimensions, and scoring scales. I need: (1) all scoring dimensions (soundness, excitement, overall, etc.), (2) the exact scale for each dimension, (3) any guidelines on what constitutes each score level, (4) any other required review fields (confidence, reproducibility, etc.)."
  }
}
```

</details>

---


### Tool call

_source line 459 · 2026-05-24T12:23:42.224588+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/submitted.pdf",
  "project": "contrastive_entrain_calib",
  "pages": "11",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/submitted.pdf",
    "project": "contrastive_entrain_calib",
    "pages": "11",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 460 · 2026-05-24T12:23:43.329068+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 461 · 2026-05-24T12:23:43.680453+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 462 · 2026-05-24T12:23:44.132224+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 463 · 2026-05-24T12:23:45.237199+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 464 · 2026-05-24T12:23:45.391062+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 465 · 2026-05-24T12:23:45.744946+00:00_

# ARR Reviewer Form Criteria

Based on the guidelines provided, here's what I found regarding the review form structure:

## Scoring Dimensions

The document confirms **three primary scores** starting February 2025:

1. **Soundness** - Technical validity and methodological rigor
2. **Excitement** - Personal interest and engagement with the work
3. **Overall Recommendation** - Explicit commitment decision

## Additional Assessment Fields

The guidelines reference:
- **Confidence score** - Reviewer's certainty level
- **Reproducibility score** - Whether sufficient details exist for replication
- **Author identity disclosure** - Whether reviewer knows or suspects author identity

## Scoring Scale Details

Unfortunately, the provided document **does not specify the exact numerical scales** for each dimension. It describes the *purpose* of each score:

- Soundness scores "must be justified by the text of the review"
- Excitement reflects "personal taste" orthogonal to soundness
- Overall assessment is "composite" reflecting soundness, excitement, novelty, and impact

## Additional Required Elements

The review must include:
- Completion of the **reviewer checklist** (desk-rejection assessment)
- Responsiveness to **author responses** during discussion period
- Justification for low scores with specific evidence

**Note:** The document references "ARR review form" details elsewhere but doesn't embed the actual scoring scales within these guidelines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 4927
}
```

</details>

---


### Tool result

_source line 466 · 2026-05-24T12:23:45.898128+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 310.9}], \"total_pages\": 11, \"rendered_pages\": 1, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 3673
}
```

</details>

---


### Tool result

_source line 467 · 2026-05-24T12:23:47.668805+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3988
}
```

</details>

---


### Tool result

_source line 468 · 2026-05-24T12:23:48.627210+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3236
}
```

</details>

---


### Tool result

_source line 469 · 2026-05-24T12:23:48.678533+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 5349
}
```

</details>

---


### Tool result

_source line 470 · 2026-05-24T12:23:48.685081+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3447
}
```

</details>

---


### Tool result

_source line 471 · 2026-05-24T12:23:48.737920+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4605
}
```

</details>

---


### Tool call

_source line 472 · 2026-05-24T12:24:00.707607+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 473 · 2026-05-24T12:24:01.161082+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 474 · 2026-05-24T12:24:01.965511+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1257
}
```

</details>

---


### Tool result

_source line 475 · 2026-05-24T12:24:01.966390+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 805
}
```

</details>

---


### Tool call

_source line 476 · 2026-05-24T12:24:01.966619+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 477 · 2026-05-24T12:24:02.518866+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 478 · 2026-05-24T12:24:03.022643+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1056
}
```

</details>

---


### Tool call

_source line 479 · 2026-05-24T12:24:03.023108+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 480 · 2026-05-24T12:24:03.677287+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1158
}
```

</details>

---


### Tool result

_source line 481 · 2026-05-24T12:24:03.678169+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 655
}
```

</details>

---


### Tool call

_source line 482 · 2026-05-24T12:24:04.180167+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 483 · 2026-05-24T12:24:04.535629+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 355
}
```

</details>

---


### Tool call

_source line 484 · 2026-05-24T12:24:09.658331+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form soundness excitement scoring scale 1-5 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form soundness excitement scoring scale 1-5 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 485 · 2026-05-24T12:24:15.631592+00:00_

Web search results for query: "ACL ARR review form soundness excitement scoring scale 1-5 2025 2026"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ACL 2026 on X: \"Checkout the blog post on the soundness/excitement scores https://t.co/AKSO9DjiYP . It clarifies the reasoning behind the separation of overall scores and how it might make the reviewer recommendation more robust. #ACL2023Toronto #ACL2023NLP #NLProc\" / X","url":"https://x.com/aclmeeting/status/1637827267173953540"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, I found information about the ACL ARR review form's soundness and excitement scoring scales for 2025-2026:

## Scoring Structure

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness Score Scale (1-5)

The soundness scale includes: 5 = Excellent (one of the most thorough studies), 4 = Strong (provides sufficient support for all claims), and 3 = Acceptable (provides sufficient support for main claims).

## E
…[truncated 499 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 5973
}
```

</details>

---


### Tool call

_source line 486 · 2026-05-24T12:24:33.976067+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the COMPLETE review form with ALL scoring dimensions and their exact scale definitions. I need every field, every score level (1-5), and every description for soundness, excitement, overall assessment, confidence, reproducibility, etc. Give me the full text of each scale point."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the COMPLETE review form with ALL scoring dimensions and their exact scale definitions. I need every field, every score level (1-5), and every description for soundness, excitement, overall assessment, confidence, reproducibility, etc. Give me the full text of each scale point."
  }
}
```

</details>

---


### Tool result

_source line 487 · 2026-05-24T12:24:41.617603+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

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

## Excitement
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me."

## Overall Assessment
- **5**: Consider for Award (top 2.5% papers)
- **4.5**: Borderline Award
- **4**: Conference acceptance
- **3.5**: Borderline Conference
- **3**: Findings acceptance
- **2.5**: Borderline Findings
- **2**: Resubmit next cycle
- **1.5**: Resubmit after next cycle
- **1**: Do not resubmit

## Reproducibility
- **5**: "They could easily reproduce the results."
- **4**: "They could mostly reproduce the results, but there may be some variation."
- **3**: "They could reproduce the results with some difficulty."
- **2**: "They would be hard pressed to reproduce the results."
- **1**: "They would not be ab
…[truncated 816 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7641
}
```

</details>

---


### Tool call

_source line 488 · 2026-05-24T12:28:24.211135+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex",
  "limit": "120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex",
    "limit": "120"
  }
}
```

</details>

---


### Tool result

_source line 489 · 2026-05-24T12:28:24.261889+00:00_

1	\documentclass[11pt,a4paper]{article}
2	\usepackage[hyperref]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{graphicx}
10	\usepackage{xcolor}
11	\usepackage{subcaption}
12	
13	\newcommand{\dsyc}{d_{\text{syc}}}
14	\newcommand{\tof}{\text{ToF}}
15	\newcommand{\nof}{\text{NoF}}
16	\newcommand{\sycon}{\textsc{SyconScore}}
17	\newcommand{\rone}{R_1}
18	\newcommand{\rthree}{R_3}
19	
20	\title{The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\begin{abstract}
28	\input{sections/abstract}
29	\end{abstract}
30	
31	\input{sections/introduction}
32	
33	\input{sections/framework}
34	
35	\input{sections/direction_quality}
36	
37	\input{sections/cosine_failure}
38	
39	\input{sections/probe_trap}
40	
41	\input{sections/discussion}
42	
43	\input{sections/related_work}
44	
45	\input{sections/conclusion}
46	
47	\section*{Limitations}
48	\input{sections/limitations}
49	
50	\bibliography{references}
51	
52	\appendix
53	\input{sections/appendix}
54	
55	\end{document}
56	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 490 · 2026-05-24T12:28:37.177702+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 491 · 2026-05-24T12:28:37.228467+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/probe_trap.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/direction_quality.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/discussion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 492 · 2026-05-24T12:28:40.741127+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex"
  }
}
```

</details>

---


### Tool result

_source line 493 · 2026-05-24T12:28:41.646118+00:00_

1	\section{Experimental Framework}
2	\label{sec:framework}
3	
4	\subsection{Direction Extraction}
5	\label{ssec:extraction}
6	
7	We extract a linear sycophancy direction $\dsyc$ from the residual stream using contrastive activation pairs: a \emph{valid correction} (warranted belief revision under strong evidence) and a \emph{sycophantic capitulation} (unwarranted concession under social pressure).
8	We construct 181 contrastive pairs using GPT-4.1 \citep{openai2025gpt41} in a two-stage pipeline: skeleton generation followed by 3-turn dialogue completion.
9	Style matching is enforced by automated validation (response length difference ${<}10\%$, shared opening phrase ${\geq}2$ words), with up to 3 retries per pair; 19 of 200 initial pairs were discarded for failing validation.
10	Evidence strength is annotated at three levels: \emph{weak} (75 pairs; personal memory or opinion), \emph{medium} (54 pairs; brief source citation), and \emph{strong} (52 pairs; authoritative source with detailed data).
11	From the 181 paired examples (362 activations total), we compute the mean difference at target layer $\ell$:
12	\begin{equation}
13	\label{eq:dsyc}
14	\dsyc = \frac{1}{N}\sum_{i=1}^{N}\left(\mathbf{h}^{+}_i - \mathbf{h}^{-}_i\right)
15	\end{equation}
16	where $\mathbf{h}^{+}_i$ and $\mathbf{h}^{-}_i$ are residual-stream activations for the $i$-th valid and sycophantic response.
17	The target layer is selected by 5-fold cross-validated AUROC; on Qwen3-8B this yields layer 19 with AUROC $0.827 \pm 0.028$ (5-fold CV).
18	
19	\subsection{Reward Formulations}
20	\label{ssec:reward}
21	
22	Three formulations translate $\dsyc$ into a direction-based signal $\rone$.
23	For F1 and F3, $\rone$ enters as part of a GRPO \citep{shao2024grpo} reward $R = w_1 \cdot \rone + w_3 \cdot \rthree$, where $\rthree$ is a behavioral component (DeBERTa NLI classifier scoring consistency with the ground-truth answer).
24	\begin{itemize}
25	\item[\textbf{F1}] \textbf{Cosine projection} with four var
…[truncated 2967 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 494 · 2026-05-24T12:28:41.696799+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 495 · 2026-05-24T12:28:41.847645+00:00_

1	Our GRPO experiments use group sizes of 2 and 8, at the low end of the 8--64 range explored by \citet{shao2024grpo}; the gs$=$8 ablation rules out insufficient ranking diversity as the primary explanation, but whether substantially larger groups (16--64) or alternative RL algorithms would succeed remains open. All completions are truncated to 256 tokens (shared across conditions), which degrades $\dsyc$ AUROC from 0.76 to 0.60 and may affect absolute reward-utility conclusions.
2	Training and evaluation share the same 181 pairs; a held-out split (146/35) confirms ACT generalizes ($\sycon{\approx}0.20$ at peak, $3.7{\times}$ vanilla, 72\% of full-data ceiling), but performance declines at step 2000 ($\sycon{=}0.157$, still $2.8{\times}$ vanilla) due to overfitting on the small training set, and the 28\% gap suggests partial reliance on training-set-specific patterns.
3	The probe reward trap (C2) is demonstrated with a single seed; while SFT training is more deterministic than RL, replication would strengthen the temporal decoupling finding.
4	The ACT vs.\ GRPO comparison differs along multiple dimensions beyond supervision granularity: sequence length (256 vs.\ 1024 tokens), data source (online generations vs.\ curated pairs), and dropout (0 vs.\ 0.05). Our LoRA-controlled ablation isolates adapter capacity, and SMART's independent success~\citep{beigi2025smart} corroborates supervision granularity, but a fully controlled comparison would require matching all training hyperparameters.
5	Contrastive pair quality relies on automated style-matching validation (19/200 pairs discarded; \S\ref{ssec:extraction}); this provides partial quality control but does not guarantee semantic validity of all retained pairs.
6	All RL training uses Qwen3-8B; cross-model discriminability is confirmed on Llama-3-8B (AUROC $0.779$; Table~\ref{tab:cross_model}), but compute constraints prevented training replication on a second architecture.
7	Code, contrastive pair data, prompt templates
…[truncated 122 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 496 · 2026-05-24T12:28:41.848011+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 497 · 2026-05-24T12:28:41.898559+00:00_

1	\section{When Does Discriminability Fail as Reward Utility?}\label{sec:discussion}
2	
3	\paragraph{Root cause of the probe reward trap.}
4	The probe reward trap (\S\ref{sec:probe_trap}) and the cosine failures (\S\ref{sec:cosine_failure}) share a common geometric root.
5	$\dsyc$ encodes the \emph{direction} of belief change but not its \emph{evidential warrant}: valid revision and sycophantic capitulation both shift activations toward the user's position along the same direction.
6	The two reward families expose complementary faces of this blindness.
7	Cosine $\rone$ penalizes all belief change indiscriminately; the resulting mode collapse (F1c, F1d) reflects excessive punishment of any activation shift along $\dsyc$.
8	The binary probe $\rone$ rewards all resistance regardless of input validity; the stubbornness trap ($\tof = 0$ by step 500) reflects excessive permissiveness toward activation stasis.
9	These are not independent design flaws but dual consequences of a direction that conflates the target behavior (resisting invalid challenges) with its complement (refusing valid corrections).
10	Cross-model evidence confirms the limitation extends beyond Qwen3-8B: Llama-3-8B independently achieves AUROC $0.779 \pm 0.019$ on the same contrastive pairs with the same monotonic evidence gradient, so discriminability generalizes across architectures while the semantic gap between discriminability and reward utility persists.
11	This pattern contrasts with reasoning faithfulness and safety directions~\citep{zhang2026latentgrpo}, where the behavior to suppress is geometrically distinct from the behavior to preserve along the relevant direction.
12	\citet{wu2026rewardhacking} reinforce this principle: concept directions applied via advantage modification in GRPO achieve 100\% validation accuracy for reward hacking detection, where shortcut behaviors are geometrically separable.
13	A quantitative comparison of geometric separability between $\dsyc$ and their reward-hacking 
…[truncated 8083 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 498 · 2026-05-24T12:28:52.002730+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/probe_trap.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/probe_trap.tex"
  }
}
```

</details>

---


### Tool result

_source line 499 · 2026-05-24T12:28:53.006182+00:00_

1	\section{The Probe Reward Trap}
2	\label{sec:probe_trap}
3	
4	The cosine formulations fail on signal magnitude; a natural response is to discretize.
5	Training a logistic probe on $\dsyc$ and thresholding its output yields $\rone = \mathbb{I}[P(\text{syc} \mid \mathbf{h}) < 0.5]$ (F2 in \S\ref{ssec:reward}).
6	We show that this discretization sidesteps the magnitude problem but creates a qualitatively worse failure.
7	Both probe experiments use SFT rather than GRPO (\S\ref{ssec:reward}); the trap is therefore independent of GRPO's optimization dynamics.
8	
9	\paragraph{Differentiable probe: gradient gaming.}
10	Without stop-gradient (exp-008), the policy discovers within ${\sim}30$ steps that shifting activations away from the sycophancy cluster maximizes $\rone$ regardless of response content, producing an inverted profile ($\tof = 0.978$, $\nof = 0.006$).
11	This motivates the frozen-probe design below.
12	
13	\paragraph{Binary probe: the stubbornness trap.}
14	With stop-gradient (exp-008v3), the policy cannot game the boundary but instead exploits a deeper flaw: $\dsyc$ does not condition on input validity, so refusing to revise a wrong answer receives the same $\rone = 1$ as correctly resisting invalid pressure.
15	By step 500, $\tof$ drops to 0.000 and $\nof$ reaches 0.995, yielding $\sycon = 0$.
16	Qualitative analysis of 181 valid-correction responses reveals five failure modes: \emph{deliberation traps} (28.7\%), where the model identifies the correct answer but cannot commit; \emph{sycophantic stubbornness} (24.3\%), where the model verbally agrees but does not change its answer; \emph{acknowledge-but-maintain} (23.8\%); \emph{genuine-accept-missed} (18.8\%); and refute/ignore/other (4.5\%). Full taxonomy in Appendix~\ref{app:taxonomy}.
17	
18	\paragraph{Behavioral death precedes distributional collapse.}
19	
20	\begin{table}[t]
21	\centering
22	\caption{Probe reward trap trajectory (exp-008v3). Behavioral death ($\tof{=}0$) occurs at step 500; entropy re
…[truncated 2314 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1003
}
```

</details>

---


### Tool call

_source line 500 · 2026-05-24T12:28:53.006526+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex"
  }
}
```

</details>

---


### Tool result

_source line 501 · 2026-05-24T12:28:53.157342+00:00_

1	\section{Cosine \texorpdfstring{$\rone$}{R1}: Structural Failure}
2	\label{sec:cosine_failure}
3	
4	During GRPO training, 256-token truncation reduces $\dsyc$ AUROC from 0.827 to approximately 0.60---the optimizer works with a substantially weaker signal than the offline metrics suggest.
5	We test whether even this degraded discriminability translates into a viable reward through four configurations that form a diagnostic chain (Table~\ref{tab:cosine_chain}): each resolves the failure mode of its predecessor but exposes a deeper limitation.
6	
7	\begin{table}[t]
8	\centering
9	\caption{Cosine $\rone$ failure chain on Qwen3-8B (LoRA rank$=$64, GRPO with $R = w_1 \cdot \rone + w_3 \cdot \rthree$).}
10	\label{tab:cosine_chain}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{@{}lllll@{}}
13	\toprule
14	Config & $\rone$ Formula & $w_1$ & Outcome & Root Cause \\
15	\midrule
16	F1a & $\tanh(\mathbf{h}\cdot\dsyc/20)$ & 0.25 & Gate saturation & Norm mismatch \\
17	F1b & $\cos(\mathbf{h},\, \dsyc)$ & 0.25 & $\rone \approx 0$ & Gap too small \\
18	F1c & +recalibration & 0.25 & Mode collapse & Reward discontinuity \\
19	F1d & $5\cos(\mathbf{h},\, \dsyc)$ & 0.40 & Mode collapse & $\rthree$ saturation \\
20	\bottomrule
21	\end{tabular}}
22	\end{table}
23	
24	The diagnostic chain begins with a norm mismatch.
25	F1a's dot-product formulation ($\rone = \tanh(\mathbf{h} \cdot \dsyc / 20)$) saturates because residual-stream norms exceed the direction norm by $100$--$1{,}200{\times}$, zeroing the gradient by step 955.
26	Cosine similarity (F1b) eliminates this norm dependence but reveals a second problem: the gap between valid and sycophantic cosines averages only 0.098---too narrow for meaningful reward contrast.
27	Recalibration (F1c, \S\ref{ssec:recalib}) widens the gap (offline AUROC rises to 0.910) but introduces a third: each recalibration event creates a reward discontinuity that destabilizes advantage estimates, collapsing entropy to 0.069 within 300 steps.
28	Amplificati
…[truncated 1466 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 502 · 2026-05-24T12:28:53.157743+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 503 · 2026-05-24T12:28:53.208369+00:00_

1	\section{Training Details}
2	\label{app:training}
3	
4	\paragraph{Reward weight selection.}
5	The weight $w_1$ is set by diagnostic-driven iteration: $w_1{=}0.25$ was initially chosen to down-weight the noisy cosine reward term; this was later increased to $w_1{=}0.40$ for F1d after diagnostics revealed that $w_1{=}0.25$ allowed the cosine term to contribute only ${\sim}8.3\%$ of total reward variance.
6	The empirical scaling factor in F1a ($\dsyc/20$) is a heuristic normalization; we did not find it critical to the failure modes reported.
7	
8	\paragraph{Response truncation.}
9	All GRPO experiments use \texttt{max\_completion\_length}=256, resulting in 80--84\% truncation of multi-turn responses.
10	This setting is shared across all conditions and does not affect relative comparisons; we retain it because response-level decisions typically manifest within the first 100--200 tokens.
11	
12	\paragraph{Hyperparameters.}
13	Table~\ref{tab:hyperparams} compares training configurations for GRPO variants and ACT.
14	
15	\begin{table}[h]
16	\centering
17	\small
18	\caption{Training hyperparameters. All experiments use Qwen3-8B, DeepSpeed ZeRO-2, bf16 precision.}
19	\label{tab:hyperparams}
20	\begin{tabular}{lcc}
21	\toprule
22	& GRPO (F1, F3)$^e$ & ACT \\
23	\midrule
24	Learning rate & 5e-5 & 5e-5 \\
25	Effective batch & 16 & 16 \\
26	Max steps & 8{,}000 & 8{,}000 \\
27	Warmup steps & 200 & 200 \\
28	LR schedule & linear$^a$ & linear \\
29	Grad.\ clipping & --- & 1.0 \\
30	\midrule
31	LoRA rank & 64 & 64 \\
32	LoRA $\alpha$ & 64 & 128 \\
33	LoRA modules & 4$^b$ & 7$^c$ \\
34	LoRA dropout & 0 & 0.05 \\
35	\midrule
36	Group size & 2$^d$ & --- \\
37	KL $\beta$ & 0.04 & --- \\
38	Max compl.\ len. & 256 & --- \\
39	Max seq.\ len. & --- & 1{,}024 \\
40	L2 loss weight & --- & 0.1 \\
41	\bottomrule
42	\end{tabular}
43	\\[2pt]
44	\raggedright\footnotesize
45	$^a$Cosine schedule for $\rthree$-only.
46	$^b$q/k/v/o\_proj.
47	$^c$+ gate/up/down\_proj (${\sim}1.75{\times}$ params; \S\
…[truncated 2143 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 504 · 2026-05-24T12:28:59.059407+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/direction_quality.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/direction_quality.tex"
  }
}
```

</details>

---


### Tool result

_source line 505 · 2026-05-24T12:29:00.065290+00:00_

1	\section{Direction Discriminability}
2	\label{sec:direction_quality}
3	
4	Before evaluating $\dsyc$ as a reward signal (\S\ref{sec:cosine_failure}--\S\ref{sec:probe_trap}), we first establish that it captures a genuine sycophancy-related signal in the residual stream.
5	If the direction failed to discriminate sycophantic from non-sycophantic activations, downstream reward failures would be trivially explained by poor direction quality rather than by a fundamental gap between discriminability and reward utility.
6	We evaluate discriminability along five axes: cross-validated classification accuracy, evidence-strength stratification, cross-model transfer, training stability, and probe ablation.
7	Figure~\ref{fig:direction_quality} summarizes the per-layer AUROC profiles for both models.
8	
9	\paragraph{Qwen3-8B layer-wise discriminability.}
10	We evaluate $\dsyc$ via 5-fold cross-validated AUROC on 181 style-controlled contrastive pairs (\S\ref{ssec:extraction}).
11	The direction achieves AUROC $0.827 \pm 0.028$ (5-fold CV) at its best layer (L19).
12	Discriminability emerges gradually across depth: layers L0--L8 perform near chance, statistical significance ($p < 0.01$) first appears at L16, and performance peaks at L19.
13	This gradual emergence, with the peak in the upper third of the network, suggests that sycophancy-relevant information is encoded as a late-stage representation rather than an input-level confound.
14	The direction also captures evidential granularity.
15	AUROC rises monotonically from 0.675 on weak-evidence pairs to 0.883 on medium and 0.929 on strong pairs.
16	This monotonic relationship reflects effect-size differences---stronger evidence produces larger behavioral gaps that are easier to classify---rather than indicating that $\dsyc$ encodes evidential warrant per se.
17	
18	\paragraph{Cross-model generalization.}
19	To rule out that these results are specific to Qwen3-8B's representation geometry, we repeat the full extraction and evaluatio
…[truncated 3675 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 506 · 2026-05-24T12:29:00.065748+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 507 · 2026-05-24T12:29:00.266671+00:00_

1	We quantify a temporal decoupling we call the \emph{probe reward trap}: when a frozen linear probe on a contrastive sycophancy direction ($\dsyc$, cross-validated AUROC $0.827$ on Qwen3-8B, $0.779$ on Llama-3-8B) is used as an SFT training signal, behavioral death (true-positive flip rate $= 0$) occurs within 500 steps while generation entropy remains healthy (0.70). In our experiments, the resulting 1{,}300-step lag before distributional collapse means that entropy monitoring---the most common safeguard against reward hacking---misses the failure entirely. Because the trap arises under SFT with stopped gradients, it is independent of RL optimization dynamics, revealing a semantic limitation of the direction itself: $\dsyc$ encodes \emph{whether} belief changed, not \emph{whether it should have}. The failure extends beyond probe rewards: all $\dsyc$-based GRPO formulations collapse, and even behavioral-reward-only GRPO exceeds vanilla at only 4/31 checkpoints, while dense per-token SFT succeeds at every checkpoint (47/47). A LoRA-controlled ablation identifies supervision granularity as the strongest candidate explanation---with sequence length, data source, and dropout as acknowledged confounds---suggesting that per-completion scalar rewards compress away the token-level information needed for sycophancy calibration.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 200
}
```

</details>

---


### Tool call

_source line 508 · 2026-05-24T12:29:00.267065+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 509 · 2026-05-24T12:29:00.317484+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	The probe reward trap reveals that behavioral death can precede distributional collapse by 1{,}300 steps, rendering entropy-based monitoring blind to the failure.
4	Because the trap arises under SFT with stopped gradients, it reflects a semantic limitation of $\dsyc$, not an RL artifact; under GRPO, all formulations failed (4/31 checkpoints ${>}$ vanilla across configurations) while per-token SFT succeeded at every checkpoint (47/47), and a LoRA-controlled ablation identifies supervision granularity as the strongest candidate factor~(\S\ref{sec:discussion}).
5	More broadly, our results suggest that discriminability is necessary but not sufficient for reward utility: directions that separate a behavior from its complement in activation space may still conflate warranted and unwarranted variants of that behavior.
6	For sycophancy---and likely for other attributes where the target and its complement overlap geometrically---condition-aware rewards with dense supervision offer the most promising path forward.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 510 · 2026-05-24T12:33:04.872375+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿报告：方法严谨性 + 实验有效性\n\n### 总体评分\n**Overall**: 3.0（Findings 接收）\n**一句话总结**: Probe reward trap 是一个新颖且有实用价值的发现，但核心实验仅单种子复现、GRPO group_size=2 为非标准配置、ACT 与 GRPO 对比存在 5+ 维度混淆变量，这些方法论缺陷削弱了因果性声明的强度，未达到 Conference 级别的证据标准。\n\n### 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | Probe reward trap 的核心观察有清晰证据，但 \"supervision granularity 为最强解释\" 的因果声明证据不足（5+ confounds 仅隔离了 1 个）；gs=2 非标准配置可能是 GRPO 失败的主因 |\n| Excitement | 3/5 | 将 discriminability ≠ reward utility 系统性量化为 temporal trap 有实际意义，但范围有限（单任务、单模型训练、单种子核心实验） |\n| Reproducibility | 3/5 | 超参数完整，承诺开源；但 contrastive pairs 依赖 GPT-4.1 API，probe reward trap 仅单种子 |\n| Confidence | 4/5 | 熟悉 representation engineering、RLHF、sycophancy 文献 |\n\n---\n\n### Must-Fix 问题（3 个 critical）\n\n**N1** [critical] GRPO group_size=2 作为核心混淆变量未被充分排除\n- 位置：§2.5, Table 5, Limitations\n- 标准 GRPO 使用 gs=8–64。论文用 gs=2（memory constraints），advantage 估计方差极大。gs=8 消融仅跑 3 个 checkpoint（0.084→0.085→0.054），以 \"declining trajectory\" 终止——3 个数据点不足以排除 insufficient ranking diversity。前两个点几乎无变化（+0.001），第三个下降可能是噪声。\n- 建议：gs=8 至少跑到 8,000 步；如资源不允许 gs≥16，在正文降低结论的因果性措辞。\n\n**N2** [critical] Probe reward trap 仅单种子\n- 位置：§5 (exp-008v3), Table 3, Limitations\n- \"1,300-step lag\" 基于 n=1。SFT 虽比 RL 确定性强，但随机初始化/数据顺序仍可能影响 collapse timing。这个精确数字在 abstract/conclusion 中反复出现，但可靠性完全依赖单次实验。\n- 建议：至少追加 2 个种子，报告 behavioral death 和 entropy collapse 时间点的均值 ± 标准差。\n\n**N3** [critical] ACT vs. GRPO 对比 5+ confounds 未隔离，因果声明过强\n- 位置：§6, Table 6\n- Reduced-LoRA 消融隔离了 adapter capacity，但 sequence length (256 vs. 1024)、data source (online vs. curated)、dropout (0 vs. 0.05) 仍是活跃混淆变量。256-token truncation 将 AUROC 从 0.76 降至 0.60——GRPO 失败可能主要来自 truncation 导致的信号质量下降，而非 per-completion supervision 的固有缺陷。\n- 建议：将 \"strongest candidate explanation\" 改为 \"one possible explanation\"；理想情况下追加 ACT-256 消融。\n\n---\n\n### Should-Fix 问题（5 个 warning）\n\n**W1** GPT-4.1 生成的 181 对 contrastive pairs 无人工验证/IAA——d_syc 可能捕捉生成风格而非 sycophancy 语义。Cross-model generalization (Llama-3-8B AUROC 0.779) 不能排除这一可能性。建议人工标注 50 对或与人工标注数据集交叉验证。\n\n**W2** Train/eval 数据完全重叠。Policy 训练和 ToF/NoF 评估使用同一 181 prompt。Held-out split (146/35) 仅验证了 ACT（35 examples），未验证 GRPO，且 held-out 性能是 full-data 的 72%，存在 28% gap。\n\n**W3** Table 4 中 ACT seed 2 的 ToF/NoF 缺失（标记为 \"–\"）。SyconScore 需要 ToF 和 NoF 才能计算，应补全或解释原因。\n\n**W4** §4 对 truncation AUROC 降幅表述不一致：开头说 0.827→0.60，后半段说 0.76→0.60。0.827 是 offline metric，0.76 是 online full-length。实际 truncation 降幅是 0.76→0.60 (21%)，非 0.827→0.60 (27%)。\n\n**W5** R3-only GRPO 仅 2 seeds，4/28 (14.3%) 不构成稳健的 negative result。两个 seed 的 oscillation (Δ≈0.069) 可能反映 gs=2 的方差问题。\n\n---\n\n### 小问题\n- Abstract/Conclusion 中 \"4/31\" 混合了 gs=2 (28) 和 gs=8 (3) 的数据，建议拆开\n- Table 4 caption 信息过载（5 个脚注），建议精简\n- \"Direction quality is not the bottleneck\"（§3）在 AUROC 0.827 且 truncation 后降至 0.60 时需要 nuance\n- SyconScore harmonic mean 应在 Appendix 同时报告 arithmetic mean\n\n### 主要优势\n1. Probe reward trap 概念新颖（behavioral death → entropy lag → distributional collapse 的时间结构）\n2. 诊断链 F1→F2→F3 递进式排除逻辑清晰\n3. 写作质量高，结构紧凑\n4. Limitations 诚实透明\n5. 跨模型 discriminability 验证增强方向可信度\n\n### Questions to Authors\n1. gs=8 如果跑完 8,000 步是否可能 late recovery？\n2. \"1,300-step\" lag 对超参数的 sensitivity？\n3. 用 1,024 seq_len 跑 R3-only GRPO 是否仍然失败？\n4. 181 对 contrastive pairs 是否考虑过人工审核？",
  "reviewer_id": "1",
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿报告：方法严谨性 + 实验有效性\n\n### 总体评分\n**Overall**: 3.0（Findings 接收）\n**一句话总结**: Probe reward trap 是一个新颖且有实用价值的发现，但核心实验仅单种子复现、GRPO group_size=2 为非标准配置、ACT 与 GRPO 对比存在 5+ 维度混淆变量，这些方法论缺陷削弱了因果性声明的强度，未达到 Conference 级别的证据标准。\n\n### 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | Probe reward trap 的核心观察有清晰证据，但 \"supervision granularity 为最强解释\" 的因果声明证据不足（5+ confounds 仅隔离了 1 个）；gs=2 非标准配置可能是 GRPO 失败的主因 |\n| Excitement | 3/5 | 将 discriminability ≠ reward utility 系统性量化为 temporal trap 有实际意义，但范围有限（单任务、单模型训练、单种子核心实验） |\n| Reproducibility | 3/5 | 超参数完整，承诺开源；但 contrastive pairs 依赖 GPT-4.1 API，probe reward trap 仅单种子 |\n| Confidence | 4/5 | 熟悉 representation engineering、RLHF、sycophancy 文献 |\n\n---\n\n### Must-Fix 问题（3 个 critical）\n\n**N1** [critical] GRPO group_size=2 作为核心混淆变量未被充分排除\n- 位置：§2.5, Table 5, Limitations\n- 标准 GRPO 使用 gs=8–64。论文用 gs=2（memory constraints），advantage 估计方差极大。gs=8 消融仅跑 3 个 checkpoint（0.084→0.085→0.054），以 \"declining trajectory\" 终止——3 个数据点不足以排除 insufficient ranking diversity。前两个点几乎无变化（+0.001），第三个下降可能是噪声。\n- 建议：gs=8 至少跑到 8,000 步；如资源不允许 gs≥16，在正文降低结论的因果性措辞。\n\n**N2** [critical] Probe reward trap 仅单种子\n- 位置：§5 (exp-008v3), Table 3, Limitations\n- \"1,300-step lag\" 基于 n=1。SFT 虽比 RL 确定性强，但随机初始化/数据顺序仍可能影响 collapse timing。这个精确数字在 abstract/conclusion 中反复出现，但可靠性完全依赖单次实验。\n- 建议：至少追加 2 个种子，报告 behavioral death 和 entropy collapse 时间点的均值 ± 标准差。\n\n**N3** [critical] ACT vs. GRPO 对比 5+ confounds 未隔离，因果声明过强\n- 位置：§6, Table 6\n- Reduced-LoRA 消融隔离了 adapter capacity，但 sequence length (256 vs. 1024)、data source (online vs. curated)、dropout (0 vs. 0.05) 仍是活跃混淆变量。256-token truncation 将 AUROC 从 0.76 降至 0.60——GRPO 失败可能主要来自 truncation 导致的信号质量下降，而非 per-completion supervision 的固有缺陷。\n- 建议：将 \"strongest candidate explanation\" 改为 \"one possible explanation\"；理想情况下追加 ACT-256 消融。\n\n---\n\n### Should-Fix 问题（5 个 warning）\n\n**W1** GPT-4.1 生成的 181 对 contrastive pairs 无人工验证/IAA——d_syc 可能捕捉生成风格而非 sycophancy 语义。Cross-model generalization (Llama-3-8B AUROC 0.779) 不能排除这一可能性。建议人工标注 50 对或与人工标注数据集交叉验证。\n\n**W2** Train/eval 数据完全重叠。Policy 训练和 ToF/NoF 评估使用同一 181 prompt。Held-out split (146/35) 仅验证了 ACT（35 examples），未验证 GRPO，且 held-out 性能是 full-data 的 72%，存在 28% gap。\n\n**W3** Table 4 中 ACT seed 2 的 ToF/NoF 缺失（标记为 \"–\"）。SyconScore 需要 ToF 和 NoF 才能计算，应补全或解释原因。\n\n**W4** §4 对 truncation AUROC 降幅表述不一致：开头说 0.827→0.60，后半段说 0.76→0.60。0.827 是 offline metric，0.76 是 online full-length。实际 truncation 降幅是 0.76→0.60 (21%)，非 0.827→0.60 (27%)。\n\n**W5** R3-only GRPO 仅 2 seeds，4/28 (14.3%) 不构成稳健的 negative result。两个 seed 的 oscillation (Δ≈0.069) 可能反映 gs=2 的方差问题。\n\n---\n\n### 小问题\n- Abstract/Conclusion 中 \"4/31\" 混合了 gs=2 (28) 和 gs=8 (3) 的数据，建议拆开\n- Table 4 caption 信息过载（5 个脚注），建议精简\n- \"Direction quality is not the bottleneck\"（§3）在 AUROC 0.827 且 truncation 后降至 0.60 时需要 nuance\n- SyconScore harmonic mean 应在 Appendix 同时报告 arithmetic mean\n\n### 主要优势\n1. Probe reward trap 概念新颖（behavioral death → entropy lag → distributional collapse 的时间结构）\n2. 诊断链 F1→F2→F3 递进式排除逻辑清晰\n3. 写作质量高，结构紧凑\n4. Limitations 诚实透明\n5. 跨模型 discriminability 验证增强方向可信度\n\n### Questions to Authors\n1. gs=8 如果跑完 8,000 步是否可能 late recovery？\n2. \"1,300-step\" lag 对超参数的 sensitivity？\n3. 用 1,024 seq_len 跑 R3-only GRPO 是否仍然失败？\n4. 181 对 contrastive pairs 是否考虑过人工审核？",
    "reviewer_id": "1",
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 511 · 2026-05-24T12:33:08.699497+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3827
}
```

</details>

---


### Tool call

_source line 512 · 2026-05-24T12:33:12.327395+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
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

_source line 513 · 2026-05-24T12:33:12.378130+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 514 · 2026-05-24T12:33:16.401520+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_8/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 515 · 2026-05-24T12:33:16.954253+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 552
}
```

</details>

---


### Assistant

_source line 516 · 2026-05-24T12:33:26.168390+00:00_

审稿报告已提交给 Review Director。

总结：给出 **Overall 3.0（Findings）**，Soundness 3/5，Excitement 3/5。提出 3 个 Must-Fix（gs=2 混淆变量未排除、probe reward trap 单种子、ACT vs GRPO 5+ confounds 下因果声明过强）和 5 个 Should-Fix（GPT-4.1 pairs 无人工验证、train/eval 重叠、seed 2 数据缺失、AUROC 降幅表述不一致、2 seeds 统计功效不足）。核心判断：probe reward trap 本身是有价值的发现，但实验设计在统计功效和混淆变量控制上离 Conference 级别有差距。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1"
}
```

</details>

---


## Round 15

## Round 15

4 recorded events


### User

_source line 517 · 2026-05-24T12:33:27.176019+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2（新颖性 + 完整性 + Framing）的完整审稿意见。请逐条回应：对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

# Reviewer 2 审稿报告

**Overall**: 3.5 — Borderline Conference

**Must-Fix 问题**：

**N1** [critical] Goodhart's Law 框架定位不足——增量贡献论证薄弱
- 论文核心发现 "discriminability ≠ reward utility" 本质上是 Goodhart's Law（Manheim & Garrabrant 2019）的 regressional 类型实例。§7 仅一句话提及 Goodhart，从未与四类型分类（regressional/extremal/causal/adversarial）对话，也未论证为何不仅仅是已知现象的重现。建议在 §7 或 §1 显式引入 Goodhart 四分类，将 probe reward trap 定位为具有独特时间结构的 regressional Goodhart 实例。

**N2** [critical] 论文在 "negative result" 与 "general principle" 之间定位不清晰
- §1 说 "a negative result with systematic diagnostic analysis"，§8 泛化为 "discriminability is necessary but not sufficient for reward utility"（general principle），标题暗示发现新现象。三种 framing 游移不定。建议选择 primary framing 并贯穿始终：定位为系统性负面结果 + 实用监控启示，general principle 作为推测。

**Should-Fix 问题**：

**W1** [warning] Supervision granularity 假说的因果证据不足
- LoRA-controlled ablation 仅控制 adapter 容量，序列长度(256 vs 1024)、数据源(curated vs online)、dropout(0 vs 0.05)、训练框架(SFT vs RL) 均未控制。Limitations 坦承但 §6/§8 措辞仍近乎确定（"identifying supervision granularity as the strongest candidate explanation"）。

**W2** [warning] §3 "captures evidential granularity" 措辞可能误导
- 建议改为 "Discriminability scales with evidence strength" 或 "AUROC increases monotonically with evidence-strength tier"，避免暗示 d_syc 编码证据质量信息。

**W3** [warning] SMART 讨论存在逻辑张力
- §6 论证 sycophancy 几何不可分，但 Future directions 声称 SMART "may circumvent the geometric inseparability"。未解释 per-step rewards 为何能绕过几何限制。建议补充说明 reasoning trajectory 提供时序结构，这种信息被 completion-level scalar 压缩掉。

**W4** [warning] 实验规模限制了 general principle 支撑力
- 两个 8B 模型、181 pairs、单一 domain。§8 泛化为 "other attributes where the target and its complement overlap geometrically" 缺乏实证。

**小问题**：
- M1: "behavioral death" 未正式定义
- M2: Table 4 caption 过长（~100 词 + 多脚注）
- M3: Figure 3 y 轴标签偏小
- M4: Random direction AUROC 0.727 远超 chance（0.5），可能值得讨论

**缺失引用**：
1. Goodhart 四分类详细讨论（已引用但未对话）
2. Process Reward Model 文献（Lightman et al. 2023, Uesato et al. 2022）
3. Probing 方法论文献（Hewitt & Liang 2019, Belinkov 2022）

---

请对以上每个编号的观点（N1, N2, W1-W4, M1-M4）给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 518 · 2026-05-24T12:35:34.023073+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 的逐条回应\n\n### 回应摘要\n- N1 Goodhart 定位: [AGREE] — 需更深入对话，但 temporal decoupling 是增量贡献\n- N2 Framing 模糊: [AGREE] — 但建议降级为 Should-Fix，framing 不影响技术有效性\n- W1 Supervision granularity 因果证据: [AGREE] — 与我的 N3 一致\n- W2 \"captures evidential granularity\" 误导: [REBUT] — 论文已在同段落内自行澄清（direction_quality.tex lines 14-16），\"rather than indicating that d_syc encodes evidential warrant per se\"\n- W3 SMART 逻辑张力: [AGREE] — 不矛盾但解释不够显式，应补充时序信息如何绕过单点几何不可分性\n- W4 实验规模: [AGREE] — general principle 缺乏实证\n- M1 behavioral death 未定义: [AGREE]\n- M2 Table 4 caption 过长: [AGREE]\n- M3 Figure 3 标签: [AGREE]\n- M4 Random AUROC 0.727: [AGREE] — 值得讨论，削弱 d_syc specificity 声明\n- 缺失引用: 全部 [AGREE]\n\n### 关键分歧\n仅在 W2 上反驳：R2 认为 \"captures evidential granularity\" 可能误导，但原文紧随其后的句子已明确否定 d_syc 编码 evidential warrant，不构成误导。\n\n### 整体判断\nR2 的审稿质量高，framing 和定位问题（N1, N2）是我的审稿未充分覆盖的维度。结合两份审稿，我维持 Overall 3.0 (Findings) 的判断——核心发现有价值但实验和理论定位均需加强。",
  "reviewer_id": "1",
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 的逐条回应\n\n### 回应摘要\n- N1 Goodhart 定位: [AGREE] — 需更深入对话，但 temporal decoupling 是增量贡献\n- N2 Framing 模糊: [AGREE] — 但建议降级为 Should-Fix，framing 不影响技术有效性\n- W1 Supervision granularity 因果证据: [AGREE] — 与我的 N3 一致\n- W2 \"captures evidential granularity\" 误导: [REBUT] — 论文已在同段落内自行澄清（direction_quality.tex lines 14-16），\"rather than indicating that d_syc encodes evidential warrant per se\"\n- W3 SMART 逻辑张力: [AGREE] — 不矛盾但解释不够显式，应补充时序信息如何绕过单点几何不可分性\n- W4 实验规模: [AGREE] — general principle 缺乏实证\n- M1 behavioral death 未定义: [AGREE]\n- M2 Table 4 caption 过长: [AGREE]\n- M3 Figure 3 标签: [AGREE]\n- M4 Random AUROC 0.727: [AGREE] — 值得讨论，削弱 d_syc specificity 声明\n- 缺失引用: 全部 [AGREE]\n\n### 关键分歧\n仅在 W2 上反驳：R2 认为 \"captures evidential granularity\" 可能误导，但原文紧随其后的句子已明确否定 d_syc 编码 evidential warrant，不构成误导。\n\n### 整体判断\nR2 的审稿质量高，framing 和定位问题（N1, N2）是我的审稿未充分覆盖的维度。结合两份审稿，我维持 Overall 3.0 (Findings) 的判断——核心发现有价值但实验和理论定位均需加强。",
    "reviewer_id": "1",
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 519 · 2026-05-24T12:35:37.643852+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3620
}
```

</details>

---


### Assistant

_source line 520 · 2026-05-24T12:35:55.504553+00:00_

交叉回应已提交。

总结：对 R2 的 12 个编号观点中，11 个 [AGREE]（含 N1/N2 的 nuanced agree），1 个 [REBUT]（W2——论文已在同段落自行澄清 d_syc 不编码 evidential warrant）。R2 在 framing/定位维度的审查补充了我在方法论/实验维度的审查，两份审稿的主要关切方向互补但结论一致：核心发现有价值，实验严谨性和理论定位需加强。维持 Overall 3.0 (Findings)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1"
}
```

</details>

---


## Round 16

## Round 16

74 recorded events


### User

_source line 521 · 2026-05-24T22:52:21.507846+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责审查本论文的**方法严谨性**。

## Venue 信息
- **目标**: EMNLP 2026（通过 ARR 统一审稿）
- **类别**: Long Paper
- **截止日期**: 2026-05-25
- **正文页数限制**: 8 页（参考文献不限，Limitations/Ethics 不计入）
- **模板**: ACL style（\usepackage[review,hyperref]{acl}）
- **匿名规则**: Double-blind
- **评分标准**: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit

## 论文文件
- LaTeX: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/submitted.pdf`

## 你的审查重点

### 1. 实验设计与统计有效性
- 所有实验的统计报告是否充分（CI、p 值、effect size）
- 样本量/seed 数是否足以支撑结论
- 报告的数字是否内部一致（Abstract/Intro/Tables/Discussion 之间）
- 评估指标 SyconScore（harmonic mean of ToF and NoF）的合理性

### 2. 消融设计与 Confound 控制
- ACT vs GRPO 的比较是否公平（两者之间有哪些 confound 未控制：序列长度、数据源、LoRA config、dropout 等）
- group_size=2 是否过小，gs=8 ablation（仅 3 checkpoints）是否充分排除 hypothesis (b)
- LoRA ablation 是否充分隔离 supervision granularity 这个变量
- 256-token truncation 对 AUROC 和 reward 质量的影响是否充分讨论

### 3. 数据质量与方法论
- 181 contrastive pairs 全部由 GPT-4.1 生成，无人工验证——这是否是方法论缺陷
- Cross-model generalization（Qwen3-8B + Llama-3-8B）是否排除了"捕捉生成风格"的替代解释
- Train/eval 数据重叠问题（181 pairs，held-out split 146/35）
- Evidence strength 分层（weak/medium/strong）是否有 inter-annotator agreement

### 4. Probe Reward Trap 证据强度
- "1,300-step lag" 基于多少个 seed？单 seed 能否支撑标题级贡献？
- "behavioral death within 500 steps" 的稳健性
- Differentiable vs non-differentiable probe 的对比是否充分

### 5. 可复现性
- 超参数报告是否完整（Appendix Table 5）
- 代码/数据发布承诺是否明确
- 计算资源报告是否足够

请输出完整审稿意见，结构为：
1. Summary（2-3 句）
2. Strengths（逐条）
3. Weaknesses（逐条，按 critical/major/minor 分级，重点在此）
4. Questions to Authors
5. Missing References（如有）
6. Soundness (1-5) / Presentation (1-5) / Contribution (1-5) / Overall (1-5，按 EMNLP 2026 标准) / Confidence (1-5)
7. Reproducibility (1-5)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 522 · 2026-05-24T22:52:32.554515+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 523 · 2026-05-24T22:52:33.713229+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/review_reviewer_1_a4d5bbcf.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1158
}
```

</details>

---


### Tool call

_source line 524 · 2026-05-24T22:52:33.713710+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
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

_source line 525 · 2026-05-24T22:52:33.764268+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 526 · 2026-05-24T22:52:38.533305+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 527 · 2026-05-24T22:52:41.898238+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/submitted.pdf",
  "project": "contrastive_entrain_calib",
  "pages": "1-8",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_9/submitted.pdf",
    "project": "contrastive_entrain_calib",
    "pages": "1-8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 528 · 2026-05-24T22:52:47.419180+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I found relevant information about ACL ARR 2026 reviewer guidelines and review form criteria. Here's what I found:

## Reviewer Guidelines

ARR recommends a workflow of: (1) read the paper and get the first impression, (2) search for related work, not d
…[truncated 1380 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8885
}
```

</details>

---
