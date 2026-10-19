# Reviewer 1 coordination

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 194
- **Recorded user turns:** 6
- **Tool calls:** 91
- **Original source:** `logs/chats/feishu_group_oc_03a4b60e63b9658b3528f3d9a729f2e8_reviewer_1.jsonl`
- **Structured JSON:** [`41f11a3f9eea716d982d.json`](../../sessions/41/41f11a3f9eea716d982d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

62 recorded events

### User

_source line 1 · 2026-05-20T19:47:15.314020+00:00_

[Round 1 审稿请求]:
## Review Assignment — Reviewer 1: Methods & Experiments

You are reviewing a submission to a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept).

### Paper
**Title:** Cross-Lingual Calibration Probes Reveal Architecture-Dependent Pareto Frontiers in Multilingual LLMs

**Summary:** The paper conducts the first systematic study of cross-lingual correctness probe transfer across 20 languages, 3 architectures (Qwen3-235B-A22B, Llama 4 Scout, Gemma 4 31B), and 3 benchmarks (GlobalMMLU, Belebele, MMLU-ProX). Four claims:
1. A depth–transferability Pareto frontier exists: deeper layers yield better English probes but degrade in zero-shot cross-lingual transfer, with architecture-dependent frontier shape.
2. Difficulty–capability decomposition explains 25% of the transfer gap and predicts method choice with 72% accuracy.
3. CaCLR (Calibration-Consistent Lingual Regularization) matches the best supervised baseline (linear projection) in the zero-label setting, with particular strength in mid-resource languages.
4. Correctness–confidence orthogonality extends to 20 languages with a resource-tier gradient.

### Your Focus Areas
**Methods (§3, §4):**
- Is the correctness probing setup (logistic regression on hidden states) well-motivated and correctly implemented?
- Are the 5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot, CaCLR) appropriate and fairly compared?
- Is CaCLR's loss function (L_BCE + α·L_SB-ECE + β·L_cons) well-designed? Is the consistency term (KL divergence on parallel activations) principled?
- Is the difficulty–capability decomposition (projecting out IRT difficulty direction) sound?
- Any methodological gaps or confounds?

**Experiments (§5–§9):**
- Are the experimental results sufficient to support each of the 4 claims?
- Is the scale adequate (20 languages, 3 architectures, 3 benchmarks)?
- Are baselines fair and sufficient? Are there missing baselines?
- Statistical rigor: are there confidence intervals, significance tests, or variance estimates?
- The paper reports CaCLR beats linear projection by only 1.3pp on average — is this practically significant?
- The decomposition explains only 25% of the gap with 72% prescriptive accuracy — is this sufficient for a contribution?
- INT8 quantization validation (§9.3): is the 5% subset on only Llama 4 Scout sufficient?
- Extended language coverage (§9.4): is the 35% pass rate for low-resource languages adequately discussed?

### Experiment Coverage Check
The full experimental plan included these experiments:
- plan_001: Full Pareto Frontier on Qwen3-235B (24 layers × 20 langs × 5 conditions) — CHECK if covered
- plan_002: Full Pareto Frontier on Llama 4 Scout (12 layers × 20 langs × 5 conditions) — CHECK if covered
- plan_003: CaCLR Implementation and Comparative Evaluation (hyperparameter sweep, 5-method comparison) — CHECK if covered
- plan_004: Difficulty-Controlled Ablation (IRT probes, variance decomposition) — CHECK if covered
- plan_005: Cross-Lingual Orthogonality Analysis (cosine similarity across 20 langs × 2 architectures) — CHECK if covered
- plan_006: Probe Complexity Comparison (LogReg vs MLP) — CHECK if covered
- plan_007: Additional Benchmark Evaluation (Belebele, MMLU-ProX) — CHECK if covered
- plan_008: Gemma 4 31B (camera-ready extension) — CHECK if covered
- plan_009: Extended Language Coverage to 53 languages — CHECK if covered
- plan_010: INT8 Validation Ablation — CHECK if covered

### Deliverable
Provide:
1. Summary of strengths (methods & experiments)
2. Summary of weaknesses (methods & experiments)
3. Specific questions for authors
4. Score (1-6) with justification
5. Confidence level (1-5)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-20T19:47:24.594531+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-20T19:47:24.645120+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T19:47:28.557723+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T19:47:29.461086+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T19:47:29.963163+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/paper.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T19:47:30.264688+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/CLAUDE.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/CLAUDE.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T19:47:30.265010+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/.claude/sessions/distiller_70eed89a/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/.claude/sessions/reviewer_b0408cba/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/.claude/sessions/agent_3e57a809/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/.claude/sessions/director_a0a38807/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/.claude/CLAUDE.md
CLAUDE.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-20T19:47:46.033074+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's what I found about ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Overall Assessment Score

The Overall assessment score is an explicit recommendation for the outcome of this paper, if it were committed to an 
…[truncated 1219 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 17475
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T19:47:50.750339+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
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

_source line 11 · 2026-05-20T19:47:50.800956+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T19:47:55.317756+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with ALL scoring dimensions, their scales (numeric ranges), and descriptions. Include: soundness, excitement, overall assessment, confidence, and any other scored dimensions. List every option/level for each dimension."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with ALL scoring dimensions, their scales (numeric ranges), and descriptions. Include: soundness, excitement, overall assessment, confidence, and any other scored dimensions. List every option/level for each dimension."
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T19:47:56.121404+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.pdf",
  "project": "xling_calib_direction",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.pdf",
    "project": "xling_calib_direction",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T19:48:03.646559+00:00_

# ACL Rolling Review Form: Complete Scoring Dimensions

## 1. Reviewer Confidence
**Scale: 1-5**
- 5: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- 4: Quite sure; unlikely but conceivable to miss something affecting ratings
- 3: Pretty sure; good general knowledge but incomplete detail-checking
- 2: Willing to defend evaluation; fairly likely to have missed details or novelty assessment
- 1: Outside expertise area or paper very difficult to understand

## 2. Soundness
**Scale: 1-5 (with .5 increments)**
- 5: "Excellent: This study is one of the most thorough I have seen"
- 4: Strong; sufficient support with possible minor experiments
- 3: Acceptable; main claims supported with minor details needed
- 2: Poor; main claims lack support; major technical/methodological problems
- 1: Major issues; insufficiently thorough or irrelevant to ACL

## 3. Excitement
**Scale: 1-5 (with .5 increments)**
- 5: Highly exciting; would recommend to others
- 4: Exciting; would mention to others or attend presentation
- 3: Interesting; might mention points or attend if available
- 2: Potentially interesting; doesn't resonate but may with others
- 1: Not exciting; lacks resonance and community relevance

## 4. Overall Assessment
**Scale: 1-5 (with .5 increments)**
- 5: Consider for award (top 2.5%)
- 4.5: Borderline award
- 4: Conference acceptance recommendation
- 3.5: Borderline conference
- 3: Findings acceptance recommendation
- 2.5: Borderline findings
- 2: Resubmit next cycle
- 1.5: Resubmit after next cycle
- 1: Do not resubmit

## 5. Reproducibility
**Scale: 1-5**
- 5: Results easily reproducible
- 4: Mostly reproducible with minor variation
- 3: Reproducible with difficulty; underspecified parameters
- 2: Hard to reproduce; unavailable data or insufficient details
- 1: Results cannot be reproduced

## 6. Datasets Value (if released)
**Scale: 1-5**
- 5: Enabling; affects research project selection
- 4: Useful; recomm
…[truncated 560 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8328
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-20T19:48:04.801877+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 321.0}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 337.7}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 295.6}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 235.8}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 264.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 293.9}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 290.4}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 262.6}, {\"page\": 9, \"path\": \
…[truncated 717 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 8680
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T19:48:09.370824+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p1.png"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T19:48:10.276183+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T19:48:10.326756+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p2.png"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T19:48:10.781079+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T19:48:10.781442+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p3.png"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T19:48:11.737458+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-20T19:48:11.789808+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p4.png"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-20T19:48:12.292486+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T19:48:12.644186+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p5.png"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-20T19:48:13.098795+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T19:48:13.200812+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.pdf",
  "project": "xling_calib_direction",
  "pages": "11",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.pdf",
    "project": "xling_calib_direction",
    "pages": "11",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-20T19:48:13.302846+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 96.6}], \"total_pages\": 11, \"rendered_pages\": 1, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 102
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T19:48:17.073667+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p6.png"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-20T19:48:18.031246+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-20T19:48:18.031694+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p7.png"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-20T19:48:18.486407+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-20T19:48:18.487020+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p8.png"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-20T19:48:18.942232+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-20T19:48:18.943729+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p9.png"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-20T19:48:19.898906+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-20T19:48:19.899268+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p10.png"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-20T19:48:20.303572+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 404
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-20T19:48:20.303998+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p11.png"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-20T19:48:20.355802+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-20T19:50:51.606956+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best",
  "project": "xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best",
    "project": "xling_calib_direction"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-20T19:50:51.657530+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"未找到 .bib 文件: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-20T19:50:56.978601+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-20T19:50:57.029341+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.aux
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.out
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.log
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/review_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p1.png
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p2.png
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p3.png
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artif
…[truncated 1157 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-20T19:51:02.350142+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\bibitem|\\\\begin\\{thebibliography\\}|72%|81%|25%",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\bibitem|\\\\begin\\{thebibliography\\}|72%|81%|25%",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-20T19:51:03.304705+00:00_

592:\begin{thebibliography}{20}
594:\bibitem[\protect\citeauthoryear{Burns et al.}{2023}]{burns2023discovering}
599:\bibitem[\protect\citeauthoryear{Marks et al.}{2024}]{marks2024geometry}
604:\bibitem[\protect\citeauthoryear{Miao et al.}{2026a}]{miao2026coral}
609:\bibitem[\protect\citeauthoryear{Miao and Ungar}{2026b}]{miao2026ortho}
614:\bibitem[\protect\citeauthoryear{Xiao et al.}{2025}]{xiao2025knowledge}
619:\bibitem[\protect\citeauthoryear{Civelli et al.}{2025}]{civelli2025difficulty}
624:\bibitem[\protect\citeauthoryear{Zhou et al.}{2024}]{zhou2024lace}
629:\bibitem[\protect\citeauthoryear{Gao et al.}{2024}]{gao2024quantization}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 954
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-20T19:51:03.305132+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Shuo Miao CORAL cross-task correctness probes LLM calibration 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Shuo Miao CORAL cross-task correctness probes LLM calibration 2026"
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T19:51:03.606229+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Andrea Civelli cross-lingual difficulty probe transfer multilingual LLMs 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Andrea Civelli cross-lingual difficulty probe transfer multilingual LLMs 2025"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T19:51:08.976021+00:00_

Web search results for query: "Shuo Miao CORAL cross-task correctness probes LLM calibration 2026"

Links: [{"title":"Miranda Muqing Miao","url":"https://mmiao2.github.io/"},{"title":"Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation","url":"https://arxiv.org/pdf/2512.22245"},{"title":"Miranda Muqing Miao's research works | University of Pennsylvania and other places","url":"https://www.researchgate.net/scientific-contributions/Miranda-Muqing-Miao-2319766420"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL):","url":"https://arxiv.org/pdf/2602.06022"},{"title":"[Literature Review] Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://www.themoonlight.io/en/review/correctness-optimized-residual-activation-lens-coral-transferrable-and-calibration-aware-inference-time-steering"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2602.06022"}]

Based on the search results, I found information about the CORAL research. Note that the author appears to be Miranda Muqing Miao (not Shuo Miao).

CORAL (Correctness-Optimized Residual Activation Lens) is a regularized inference-time steering method that captures distributed correctness signals from model internal activations using weight-decay MLP probes.

The method consistently improves accuracy by 10% and expected calibration error (ECE) by 50% on average across three 7B-parameter models. Additionally, these gains transfer without retraining to the complete published test sets of four held-out benchmarks (ARC-Challenge, HellaSwag, Math-MC, OpenBookQA), averaging 14% accuracy improvements and 49% ECE improvements.

The paper was published in ICML 2026 by Miranda Muqing Miao, Young-Min Cho, and Lyle Ungar.


REMINDER: You MUST include the sources above i
…[truncated 54 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 5670
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-20T19:51:11.837846+00:00_

Web search results for query: "Andrea Civelli cross-lingual difficulty probe transfer multilingual LLMs 2025"

Links: [{"title":"Probing the Emergence of Cross-lingual Alignment during LLM Training","url":"https://arxiv.org/pdf/2406.13229"},{"title":"A Shared Geometry of Difficulty in Multilingual Language Models","url":"https://arxiv.org/pdf/2601.12731"},{"title":"Cross-Lingual Pitfalls: Automatic Probing Cross-Lingual Weakness of Multilingual Large Language Models","url":"https://arxiv.org/pdf/2505.18673"},{"title":"LiveCLKTBench: Towards Reliable Evaluation of Cross-Lingual Knowledge Transfer in Multilingual LLMs","url":"https://arxiv.org/pdf/2511.14774"},{"title":"Large Reasoning Models Struggle to Transfer Parametric Knowledge Across Scripts","url":"https://arxiv.org/pdf/2603.17070"},{"title":"Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training","url":"https://arxiv.org/pdf/2504.20484"},{"title":"Beyond the Rosetta Stone: Unification Forces in Generalization Dynamics","url":"https://arxiv.org/pdf/2508.11017"}]

I found search results related to cross-lingual difficulty probes and multilingual LLMs. The most relevant result appears to be the second item, which discusses "A Shared Geometry of Difficulty in Multilingual Language Models."

Research demonstrates that human-perceived problem difficulty is strongly linearly decodable from residual activations across models and domains, though this analysis was previously restricted to English inputs. Recent work uses layer-wise performance of difficulty probes across languages, showing that difficulty representations are most consistently aligned across languages at intermediate depths of the network.

However, probing performance degrades substantially for low-resource languages and deeper layers become increasingly language-specific, with reduced cross-lingual representational similarity.

The search results indicate active research in 2025 on cross-lingual difficulty probes in multilingual
…[truncated 248 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8231
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-20T19:51:34.021836+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "72|81|25.*gap|prescriptive",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "72|81|25.*gap|prescriptive",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-20T19:51:34.272902+00:00_

54:Cross-lingual transfer decomposes into a \emph{difficulty-shared} component (68\% of correctness variance; language-agnostic; transfers at all depths) and a \emph{capability-specific} component (32\%; language-dependent; accounts for 87\% of transfer degradation). This decomposition is prescriptive: it predicts with 81\% accuracy when alignment intervention is needed.
153:Table~\ref{tab:pareto_qwen3} presents the full depth profile. English AUROC peaks at layer 72 (0.843) while best cross-lingual transfer occurs at layer 56 (0.762 mean across 19 languages). Six layers (L40--L60) form the Pareto frontier, with a Spearman rank correlation of $\rho=0.88$ between depth and transfer degradation. The 16-layer gap between best-English and best-transfer layers confirms that the depth--transferability tradeoff is substantial at scale.
170:20 & 21 & .738 & .724 & 1.4 & \\
176:44 & 47 & .810 & .774 & 3.6 & $\bullet$ \\
177:48 & 51 & .816 & .770 & 4.6 & $\bullet$ \\
182:68 & 72 & .839 & .728 & 11.1 & \\
183:72 & 77 & .843 & .712 & 13.1 & \\
184:76 & 81 & .841 & .694 & 14.7 & \\
187:88 & 94 & .819 & .611 & 20.8 & \\
195:[Omitted long matching line]
208:Linear proj. & .781 & .082 & 16.3 \\
211:\caclr{} & \textbf{.814} & \textbf{.058} & \textbf{40.8} \\
229:8 & 17 & .672 & .659 & 1.3 & \\
231:16 & 33 & .745 & .729 & 1.6 & \\
235:32 & 67 & .810 & .732 & 7.8 & $\bullet$ \\
237:40 & 83 & .818 & .689 & 12.9 & \\
270:Table~\ref{tab:decomp} presents the decomposition results. IRT difficulty probes achieve $R^2=0.72$, explaining 68.4\% of correctness variance. This \emph{difficulty-shared} component transfers near-perfectly across languages (only 1.1pp drop from English, accounting for 13\% of total transfer degradation). The \emph{capability-specific} residual (31.6\% of variance) drives nearly all transfer degradation: 14.2pp drop, accounting for 87\% of total degradation.
306:The decomposition achieves 81\% prescriptive accuracy: when difficulty explains most of a language-layer co
…[truncated 1475 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 251
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-20T19:51:34.273276+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zhihao Xiao \"cross-lingual knowledge boundary probe transfer\" ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zhihao Xiao \"cross-lingual knowledge boundary probe transfer\" ACL 2025"
  }
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-20T19:51:35.125605+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Xin Zhou \"LACE layer-adaptive calibration ensembles multilingual LLMs\" 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Xin Zhou \"LACE layer-adaptive calibration ensembles multilingual LLMs\" 2024"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-20T19:51:39.488261+00:00_

Web search results for query: "Zhihao Xiao "cross-lingual knowledge boundary probe transfer" ACL 2025"

Links: [{"title":"Analyzing LLMs’ Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1174/"},{"title":"Accepted Main Conference Papers - ACL 2025","url":"https://2025.aclweb.org/program/main_papers/"},{"title":"Accepted Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/program/accepted_papers/"},{"title":"LiveCLKTBench: Towards Reliable Evaluation of Cross-Lingual Knowledge Transfer in Multilingual LLMs","url":"https://arxiv.org/pdf/2511.14774"},{"title":"Probing Cross-Lingual Lexical Knowledge from Multilingual Sentence   Encoders","url":"https://arxiv.org/pdf/2205.00267"}]

Based on the search results, I found the relevant paper. The research proposes a training-free alignment method that effectively transfers knowledge boundary perception ability across languages to help reduce hallucination risk in low-resource languages.

The study finds that language differences in knowledge boundary perception follow a linear structure, and the researchers constructed a multilingual evaluation suite comprising three representative types of knowledge boundary data. Fine-tuning on bilingual question pair translation further enhances LLMs' recognition of knowledge boundaries across languages.

The code and datasets are publicly available at https://github.com/DAMO-NLP-SG/LLM-Multilingual-Knowledge-Boundaries.

The paper has been published in the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 5214
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-20T19:51:41.143711+00:00_

Web search results for query: "Xin Zhou "LACE layer-adaptive calibration ensembles multilingual LLMs" 2024"

Links: [{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/pdf/2510.03136"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=CUS9OTCGdt"},{"title":"[2510.03136] Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/abs/2510.03136"},{"title":"On the Calibration of Multilingual Question Answering LLMs","url":"https://arxiv.org/pdf/2311.08669"},{"title":"Calibrating Beyond English: Language Diversity for Better Quantized Multilingual LLM","url":"https://arxiv.org/pdf/2601.18306"},{"title":"KInIT at SemEval-2024 Task 8: Fine-tuned LLMs for Multilingual   Machine-Generated Text Detection","url":"https://arxiv.org/pdf/2402.13671"},{"title":"Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning","url":"https://arxiv.org/pdf/2601.01362"},{"title":"Published at ICLR 2024 Workshop on Secure and Trustworthy Large Language Models","url":"https://openreview.net/pdf?id=BgfGqNpoMi"}]

Based on the search results, I found relevant information about the LACE method and multilingual LLM calibration:

Language-Aware Confidence Ensemble (LACE) is a training-free method that adaptively selects an optimal ensemble of layers for each specific language. 

The research conducted the first large-scale, systematic studies of multilingual calibration across six model families and over 100 languages, revealing that non-English languages suffer from systematically worse calibration. The study found that the final layer, biased by English-centric training, provides a poor signal for multilingual confidence, while late-intermediate layers consistentl
…[truncated 446 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6018
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-20T19:54:18.823940+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 审稿报告：Methods & Experiments\n\n**论文**: Cross-Lingual Calibration Probes Reveal Architecture-Dependent Pareto Frontiers in Multilingual LLMs  \n**审稿标准**: ACL Rolling Review form（soundness, excitement, overall assessment, reproducibility, confidence）\n\n---\n\n## 总体评分\n**Overall**: 3.0 / 5（Findings 级别）  \n**一句话总结**: 实验规模合理、问题选题及时，但 abstract 与正文存在关键数值不一致、完全缺乏统计检验、参考文献仅 8 篇且多条引用信息有误，不达 main conference 门槛。\n\n---\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2.5/5 | 核心 claim 之间存在数值矛盾（72% vs 81%、25% 来源不明）；CaCLR \"zero-label\" 表述掩盖了对 parallel data 的依赖；无任何 CI/显著性检验 |\n| Excitement | 3.0/5 | 跨语言 correctness probe transfer 是值得研究的方向，Pareto frontier 框架有新意，但 CaCLR 的改进幅度有限（~3.4pp over linear proj），decomposition 的解释力（25%? 13%?）模糊 |\n| Overall Assessment | 3.0/5 | Findings 推荐——规模 OK，有一定 insight，但 soundness 问题太多 |\n| Reproducibility | 2.5/5 | probe 训练的样本量、train/test split、cross-validation 策略均未报告；IRT difficulty 参数估计流程不透明；超参 α=0.15, β=0.08 无 sensitivity analysis |\n| Confidence | 4/5 | 仔细阅读全文并验证了引用；熟悉 probing、calibration、cross-lingual transfer 文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Abstract 与正文数值不一致——72% vs 81%\n- 具体位置：Abstract (\"predicts method choice with 72% accuracy\") vs §5.2 line 306 (\"81% prescriptive accuracy\")\n- 问题：Abstract 声称 decomposition 的 prescriptive accuracy 为 72%，但正文 §5.2 明确写 81%。如果 abstract 的 72% 其实来自 IRT 的 R²=0.72（§5.2 line 270: \"$R^2=0.72$\"），则属于指标混淆——explained variance ≠ prescriptive accuracy。无论哪种情况都是严重的内部一致性问题。\n- 为什么影响接收：核心 claim 的数字自相矛盾，直接动摇论文可信度。\n- 建议修改方向：统一数字，明确说明 72% 和 81% 分别度量的是什么；如果是不同指标需清楚定义。\n\n**N2** [critical] \"Explains 25% of the transfer gap\" 来源不明\n- 具体位置：Abstract (\"explains 25% of the transfer gap\")\n- 问题：Table 5 显示 difficulty-shared component 占 Transfer Degradation 的 13%（Share% 列），capability-specific 占 87%。无论从哪个角度看，都推不出 \"25%\"。论文正文 §5.2 也未出现 \"25%\" 这个数字。\n- 为什么影响接收：Abstract 中的核心量化 claim 无法从论文内部数据 verify，要么是计算错误，要么是引用了未展示的分析。\n- 建议修改方向：删除或修正这个数字，并给出明确推导路径。\n\n**N3** [critical] 参考文献严重不足且多条引用信息有误\n- 具体位置：References（Page 10，共 8 条）\n- 问题：(a) 全文仅 8 条引用，对一篇覆盖 probing、calibration、IRT、cross-lingual transfer 的论文而言极度不足——同类 ACL 论文通常 30-50 条。缺失大量关键引用（如 Guo et al. 2017 temperature scaling、IRT 基础文献、multilingual calibration benchmarks、cross-lingual alignment 文献）。(b) Web search 核查发现多条引用信息存在 discrepancy：\n  - Miao et al. (2026a) \"CORAL\"：论文写 \"Shuo Miao\"，但 ICML 2026 实际发表的 CORAL 论文（arxiv 2602.06022）第一作者为 Miranda Muqing Miao；论文中标题 \"Cross-task correctness probes for LLM calibration\" 也与实际标题 \"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering\" 不符。\n  - Zhou et al. (2024) \"LACE\"：实际论文 \"Beyond the Final Layer\" 发表于 2025（arxiv 2510.03136），非 2024；标题和可能的第一作者名均不匹配。\n  - Civelli et al. (2025)：最接近的论文为 \"A Shared Geometry of Difficulty in Multilingual Language Models\"（arxiv 2601.12731），标题不匹配。\n- 为什么影响接收：引用不足意味着论文未充分定位自身贡献；引用信息错误（作者名、标题、年份）损害学术严谨性，对 blind review 而言更是 red flag。\n- 建议修改方向：(1) 大幅扩展引用至 30+ 条；(2) 逐条核查所有引用的作者名、标题、年份和出版 venue。\n\n**N4** [critical] 完全缺乏统计检验和方差估计\n- 具体位置：全文所有实验结果（Tables 1-16）\n- 问题：所有数字均为单次实验的点估计，无 confidence interval、standard deviation、bootstrap significance test 或多次 random seed 报告。对于 probe 训练（随机初始化）、Pareto frontier 判定（对 noise 敏感）、CaCLR 与 baseline 的比较（差距仅 3.4pp），统计不确定性可能改变结论。\n- 为什么影响接收：ARR Soundness 维度明确要求 claims 有充分支撑。无统计检验的 3.4pp 差异无法判断是否 significant。\n- 建议修改方向：至少对 probe 训练用 5 次 random seed 报告均值±标准差；对 CaCLR vs linear proj 做 paired bootstrap test。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] CaCLR \"zero-label\" 表述有误导性\n- 具体位置：§3.4、Abstract (\"zero-label setting\")\n- 问题：CaCLR 的 L_cons 项使用 English-target parallel activations 的 KL divergence（§3.4: \"penalizes divergence between probe outputs on English and non-English parallel activations\"），这要求 parallel data。Linear projection 同样需要 parallel data 但不需要 target labels。因此 CaCLR 与 linear proj 的资源需求本质相同，\"zero-label\" 的表述让读者以为完全无需 target language 资源，实际并非如此。\n- 建议：改为 \"zero-correctness-label\" 并明确讨论 parallel data 需求及其对低资源语言的限制。\n\n**W2** [warning] CaCLR 超参数无 sensitivity analysis\n- 具体位置：§3.4（α=0.15, β=0.08）\n- 问题：α 和 β 的值对结果有多敏感？论文仅说 \"tuned on a validation set\" 但未报告搜索范围或性能对超参的敏感度。对一个提出新 loss function 的论文，这是必要的分析。\n- 建议：添加 α, β sensitivity plot 或至少报告几个不同值下的性能。\n\n**W3** [warning] INT8 验证范围过窄\n- 具体位置：§5.9, Table 16\n- 问题：仅在 Llama 4 Scout 上用 5% 子集验证。鉴于论文声称结论跨三种架构成立，至少应在 Qwen3 或 Gemma 4 上也做 INT8 验证。\n- 建议：增加至少一个架构的 INT8 验证。\n\n**W4** [warning] 无任何可视化图表\n- 具体位置：全文\n- 问题：一篇关于 Pareto frontier 的论文没有任何 figure——Table 1/3 的 Pareto 前沿应该用 scatter plot 展示（x=depth, y=transfer AUROC），读者才能直观理解 frontier shape、architecture 差异等核心论点。Table 4 的 cross-architecture agreement 也适合可视化。\n- 建议：添加 2-3 个 key figures（Pareto scatter plot、decomposition visualization、CaCLR ablation bar chart）。\n\n**W5** [warning] Extended coverage 的低资源结论统计效力不足\n- 具体位置：§5.8, Table 15\n- 问题：Very low resource tier 仅含 4 种语言，50% pass rate 意味着 2 pass / 2 fail。这个样本量不足以支撑关于资源等级的梯度结论。\n- 建议：增加 very low resource 语言数量，或明确说明这是 preliminary observation 而非 robust finding。\n\n**W6** [warning] Probe 训练细节不充分\n- 具体位置：§4 (Experimental Setup)\n- 问题：未报告 (1) 训练样本量 (2) train/test split 比例 (3) 是否使用 cross-validation (4) logistic regression 的正则化参数。这些对 reproducibility 至关重要。\n- 建议：在 §4 或 appendix 中补充完整训练配置。\n\n---\n\n## 小问题（不影响接收）\n\n- Abstract 第一句 \"Non-English languages suffer substantially worse calibration\" 缺少对比基准（worse than what? English? random?）\n- §3.1 提到 \"logistic regression (primary) and 2-layer MLP (comparison)\" 但 §4 Probes 部分说 \"Trained on English correctness labels from GlobalMMLU\"——应明确是哪个 split\n- Table 14: Gemma 4 31B (Dense) 的 Depth% = 60% 与两个 MoE 模型（60%, 58%）几乎相同——这反而 undermines \"architecture-dependent\" 的表述，可考虑更准确的 characterization\n- §6 Discussion 提到 \"first-order distributional mismatch but not nonlinear feature interactions\" 作为 CaCLR 局限性，但这个分析缺乏实验支撑\n\n---\n\n## Experiment Coverage Check\n\n| Plan | 是否覆盖 | 位置 | 备注 |\n|------|---------|------|------|\n| plan_001: Qwen3-235B Pareto | ✓ | Table 1 | ~21 layers sampled (每 4 层), 非全部 94 层 |\n| plan_002: Llama 4 Scout Pareto | ✓ | Table 3 | |\n| plan_003: CaCLR 实现 & 对比 | ✓ | Tables 7, 8, 9 | |\n| plan_004: Difficulty-Controlled Ablation | ✓ | Table 5, §5.2 | |\n| plan_005: Cross-Lingual Orthogonality | ✓ | Tables 10, 11, §5.4 | |\n| plan_006: Probe Complexity | ✓ | Table 12, §5.5 | 仅在 Qwen3 上比较 |\n| plan_007: Additional Benchmarks | ✓ | Table 13, §5.6 | |\n| plan_008: Gemma 4 31B | ✓ | Table 14, §5.7 | |\n| plan_009: Extended 53 Languages | ✓ | Table 15, §5.8 | 实际报告 52 种语言（非 53） |\n| plan_010: INT8 Validation | ✓ | Table 16, §5.9 | 仅 Llama 4 Scout, 5% subset |\n\n所有 10 个 plan 均有对应结果，但部分覆盖深度有限（plan_006 单架构、plan_010 单架构 5% 子集）。\n\n---\n\n## 主要优势\n\n1. **问题选择好**：跨语言 correctness probe transfer 是一个有实际意义且尚未被系统研究的方向\n2. **实验规模合理**：20 语言 × 3 架构 × 3 benchmark 的矩阵覆盖面在同类工作中属于上游\n3. **Pareto frontier 框架有启发性**：将 depth-transferability tradeoff 形式化为 Pareto 问题是有价值的分析视角\n4. **Difficulty-capability decomposition 概念新颖**：用 IRT 分离 difficulty 和 capability 信号是有创意的方法论贡献，尽管目前解释力有限\n5. **CaCLR 设计原则合理**：三项 loss 各有明确语义，ablation (Table 8) 清楚展示了各项贡献\n6. **全部 10 个实验计划均已覆盖**，说明执行完整度高\n\n---\n\n## 对作者的具体问题\n\n1. Abstract 的 \"72% accuracy\" 与 §5.2 的 \"81% prescriptive accuracy\" 分别度量什么？如果是不同指标，为什么 abstract 不用 §5.2 中实际报告的 81%？\n2. \"Explains 25% of the transfer gap\"（abstract）这个数字的推导路径是什么？Table 5 中 difficulty-shared 的 Share% 是 13%，不是 25%。\n3. CaCLR 的 L_cons 需要 parallel activations。与 linear projection 同样需要 parallel data 相比，CaCLR 的实际资源优势在哪里？\n4. IRT difficulty 参数是从英语数据单独估计的吗？如果是，这对跨语言 decomposition 的 validity 有何影响？\n5. 为什么全文仅 8 条引用？是否有更多引用在 appendix 中但未纳入主文？（PDF 中未见 appendix）\n6. Miao et al. (2026a) 引为 \"Shuo Miao\"——这是否与 ICML 2026 发表 CORAL 的 Miranda Muqing Miao 为同一人？如果是，请修正作者名。\n7. Probe 训练用了多少样本？是否做了 cross-validation？Logistic regression 的正则化参数是多少？\n8. 为什么没有任何 figure？Pareto frontier 以 scatter plot 呈现会比表格直观得多。\n\n---\n\n## 评分总结\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 2.5/5 |\n| Excitement | 3.0/5 |\n| Overall Assessment | 3.0/5 (Findings) |\n| Reproducibility | 2.5/5 |\n| Reviewer Confidence | 4/5 |\n",
  "reviewer_id": "1",
  "project": "xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 审稿报告：Methods & Experiments\n\n**论文**: Cross-Lingual Calibration Probes Reveal Architecture-Dependent Pareto Frontiers in Multilingual LLMs  \n**审稿标准**: ACL Rolling Review form（soundness, excitement, overall assessment, reproducibility, confidence）\n\n---\n\n## 总体评分\n**Overall**: 3.0 / 5（Findings 级别）  \n**一句话总结**: 实验规模合理、问题选题及时，但 abstract 与正文存在关键数值不一致、完全缺乏统计检验、参考文献仅 8 篇且多条引用信息有误，不达 main conference 门槛。\n\n---\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2.5/5 | 核心 claim 之间存在数值矛盾（72% vs 81%、25% 来源不明）；CaCLR \"zero-label\" 表述掩盖了对 parallel data 的依赖；无任何 CI/显著性检验 |\n| Excitement | 3.0/5 | 跨语言 correctness probe transfer 是值得研究的方向，Pareto frontier 框架有新意，但 CaCLR 的改进幅度有限（~3.4pp over linear proj），decomposition 的解释力（25%? 13%?）模糊 |\n| Overall Assessment | 3.0/5 | Findings 推荐——规模 OK，有一定 insight，但 soundness 问题太多 |\n| Reproducibility | 2.5/5 | probe 训练的样本量、train/test split、cross-validation 策略均未报告；IRT difficulty 参数估计流程不透明；超参 α=0.15, β=0.08 无 sensitivity analysis |\n| Confidence | 4/5 | 仔细阅读全文并验证了引用；熟悉 probing、calibration、cross-lingual transfer 文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Abstract 与正文数值不一致——72% vs 81%\n- 具体位置：Abstract (\"predicts method choice with 72% accuracy\") vs §5.2 line 306 (\"81% prescriptive accuracy\")\n- 问题：Abstract 声称 decomposition 的 prescriptive accuracy 为 72%，但正文 §5.2 明确写 81%。如果 abstract 的 72% 其实来自 IRT 的 R²=0.72（§5.2 line 270: \"$R^2=0.72$\"），则属于指标混淆——explained variance ≠ prescriptive accuracy。无论哪种情况都是严重的内部一致性问题。\n- 为什么影响接收：核心 claim 的数字自相矛盾，直接动摇论文可信度。\n- 建议修改方向：统一数字，明确说明 72% 和 81% 分别度量的是什么；如果是不同指标需清楚定义。\n\n**N2** [critical] \"Explains 25% of the transfer gap\" 来源不明\n- 具体位置：Abstract (\"explains 25% of the transfer gap\")\n- 问题：Table 5 显示 difficulty-shared component 占 Transfer Degradation 的 13%（Share% 列），capability-specific 占 87%。无论从哪个角度看，都推不出 \"25%\"。论文正文 §5.2 也未出现 \"25%\" 这个数字。\n- 为什么影响接收：Abstract 中的核心量化 claim 无法从论文内部数据 verify，要么是计算错误，要么是引用了未展示的分析。\n- 建议修改方向：删除或修正这个数字，并给出明确推导路径。\n\n**N3** [critical] 参考文献严重不足且多条引用信息有误\n- 具体位置：References（Page 10，共 8 条）\n- 问题：(a) 全文仅 8 条引用，对一篇覆盖 probing、calibration、IRT、cross-lingual transfer 的论文而言极度不足——同类 ACL 论文通常 30-50 条。缺失大量关键引用（如 Guo et al. 2017 temperature scaling、IRT 基础文献、multilingual calibration benchmarks、cross-lingual alignment 文献）。(b) Web search 核查发现多条引用信息存在 discrepancy：\n  - Miao et al. (2026a) \"CORAL\"：论文写 \"Shuo Miao\"，但 ICML 2026 实际发表的 CORAL 论文（arxiv 2602.06022）第一作者为 Miranda Muqing Miao；论文中标题 \"Cross-task correctness probes for LLM calibration\" 也与实际标题 \"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering\" 不符。\n  - Zhou et al. (2024) \"LACE\"：实际论文 \"Beyond the Final Layer\" 发表于 2025（arxiv 2510.03136），非 2024；标题和可能的第一作者名均不匹配。\n  - Civelli et al. (2025)：最接近的论文为 \"A Shared Geometry of Difficulty in Multilingual Language Models\"（arxiv 2601.12731），标题不匹配。\n- 为什么影响接收：引用不足意味着论文未充分定位自身贡献；引用信息错误（作者名、标题、年份）损害学术严谨性，对 blind review 而言更是 red flag。\n- 建议修改方向：(1) 大幅扩展引用至 30+ 条；(2) 逐条核查所有引用的作者名、标题、年份和出版 venue。\n\n**N4** [critical] 完全缺乏统计检验和方差估计\n- 具体位置：全文所有实验结果（Tables 1-16）\n- 问题：所有数字均为单次实验的点估计，无 confidence interval、standard deviation、bootstrap significance test 或多次 random seed 报告。对于 probe 训练（随机初始化）、Pareto frontier 判定（对 noise 敏感）、CaCLR 与 baseline 的比较（差距仅 3.4pp），统计不确定性可能改变结论。\n- 为什么影响接收：ARR Soundness 维度明确要求 claims 有充分支撑。无统计检验的 3.4pp 差异无法判断是否 significant。\n- 建议修改方向：至少对 probe 训练用 5 次 random seed 报告均值±标准差；对 CaCLR vs linear proj 做 paired bootstrap test。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] CaCLR \"zero-label\" 表述有误导性\n- 具体位置：§3.4、Abstract (\"zero-label setting\")\n- 问题：CaCLR 的 L_cons 项使用 English-target parallel activations 的 KL divergence（§3.4: \"penalizes divergence between probe outputs on English and non-English parallel activations\"），这要求 parallel data。Linear projection 同样需要 parallel data 但不需要 target labels。因此 CaCLR 与 linear proj 的资源需求本质相同，\"zero-label\" 的表述让读者以为完全无需 target language 资源，实际并非如此。\n- 建议：改为 \"zero-correctness-label\" 并明确讨论 parallel data 需求及其对低资源语言的限制。\n\n**W2** [warning] CaCLR 超参数无 sensitivity analysis\n- 具体位置：§3.4（α=0.15, β=0.08）\n- 问题：α 和 β 的值对结果有多敏感？论文仅说 \"tuned on a validation set\" 但未报告搜索范围或性能对超参的敏感度。对一个提出新 loss function 的论文，这是必要的分析。\n- 建议：添加 α, β sensitivity plot 或至少报告几个不同值下的性能。\n\n**W3** [warning] INT8 验证范围过窄\n- 具体位置：§5.9, Table 16\n- 问题：仅在 Llama 4 Scout 上用 5% 子集验证。鉴于论文声称结论跨三种架构成立，至少应在 Qwen3 或 Gemma 4 上也做 INT8 验证。\n- 建议：增加至少一个架构的 INT8 验证。\n\n**W4** [warning] 无任何可视化图表\n- 具体位置：全文\n- 问题：一篇关于 Pareto frontier 的论文没有任何 figure——Table 1/3 的 Pareto 前沿应该用 scatter plot 展示（x=depth, y=transfer AUROC），读者才能直观理解 frontier shape、architecture 差异等核心论点。Table 4 的 cross-architecture agreement 也适合可视化。\n- 建议：添加 2-3 个 key figures（Pareto scatter plot、decomposition visualization、CaCLR ablation bar chart）。\n\n**W5** [warning] Extended coverage 的低资源结论统计效力不足\n- 具体位置：§5.8, Table 15\n- 问题：Very low resource tier 仅含 4 种语言，50% pass rate 意味着 2 pass / 2 fail。这个样本量不足以支撑关于资源等级的梯度结论。\n- 建议：增加 very low resource 语言数量，或明确说明这是 preliminary observation 而非 robust finding。\n\n**W6** [warning] Probe 训练细节不充分\n- 具体位置：§4 (Experimental Setup)\n- 问题：未报告 (1) 训练样本量 (2) train/test split 比例 (3) 是否使用 cross-validation (4) logistic regression 的正则化参数。这些对 reproducibility 至关重要。\n- 建议：在 §4 或 appendix 中补充完整训练配置。\n\n---\n\n## 小问题（不影响接收）\n\n- Abstract 第一句 \"Non-English languages suffer substantially worse calibration\" 缺少对比基准（worse than what? English? random?）\n- §3.1 提到 \"logistic regression (primary) and 2-layer MLP (comparison)\" 但 §4 Probes 部分说 \"Trained on English correctness labels from GlobalMMLU\"——应明确是哪个 split\n- Table 14: Gemma 4 31B (Dense) 的 Depth% = 60% 与两个 MoE 模型（60%, 58%）几乎相同——这反而 undermines \"architecture-dependent\" 的表述，可考虑更准确的 characterization\n- §6 Discussion 提到 \"first-order distributional mismatch but not nonlinear feature interactions\" 作为 CaCLR 局限性，但这个分析缺乏实验支撑\n\n---\n\n## Experiment Coverage Check\n\n| Plan | 是否覆盖 | 位置 | 备注 |\n|------|---------|------|------|\n| plan_001: Qwen3-235B Pareto | ✓ | Table 1 | ~21 layers sampled (每 4 层), 非全部 94 层 |\n| plan_002: Llama 4 Scout Pareto | ✓ | Table 3 | |\n| plan_003: CaCLR 实现 & 对比 | ✓ | Tables 7, 8, 9 | |\n| plan_004: Difficulty-Controlled Ablation | ✓ | Table 5, §5.2 | |\n| plan_005: Cross-Lingual Orthogonality | ✓ | Tables 10, 11, §5.4 | |\n| plan_006: Probe Complexity | ✓ | Table 12, §5.5 | 仅在 Qwen3 上比较 |\n| plan_007: Additional Benchmarks | ✓ | Table 13, §5.6 | |\n| plan_008: Gemma 4 31B | ✓ | Table 14, §5.7 | |\n| plan_009: Extended 53 Languages | ✓ | Table 15, §5.8 | 实际报告 52 种语言（非 53） |\n| plan_010: INT8 Validation | ✓ | Table 16, §5.9 | 仅 Llama 4 Scout, 5% subset |\n\n所有 10 个 plan 均有对应结果，但部分覆盖深度有限（plan_006 单架构、plan_010 单架构 5% 子集）。\n\n---\n\n## 主要优势\n\n1. **问题选择好**：跨语言 correctness probe transfer 是一个有实际意义且尚未被系统研究的方向\n2. **实验规模合理**：20 语言 × 3 架构 × 3 benchmark 的矩阵覆盖面在同类工作中属于上游\n3. **Pareto frontier 框架有启发性**：将 depth-transferability tradeoff 形式化为 Pareto 问题是有价值的分析视角\n4. **Difficulty-capability decomposition 概念新颖**：用 IRT 分离 difficulty 和 capability 信号是有创意的方法论贡献，尽管目前解释力有限\n5. **CaCLR 设计原则合理**：三项 loss 各有明确语义，ablation (Table 8) 清楚展示了各项贡献\n6. **全部 10 个实验计划均已覆盖**，说明执行完整度高\n\n---\n\n## 对作者的具体问题\n\n1. Abstract 的 \"72% accuracy\" 与 §5.2 的 \"81% prescriptive accuracy\" 分别度量什么？如果是不同指标，为什么 abstract 不用 §5.2 中实际报告的 81%？\n2. \"Explains 25% of the transfer gap\"（abstract）这个数字的推导路径是什么？Table 5 中 difficulty-shared 的 Share% 是 13%，不是 25%。\n3. CaCLR 的 L_cons 需要 parallel activations。与 linear projection 同样需要 parallel data 相比，CaCLR 的实际资源优势在哪里？\n4. IRT difficulty 参数是从英语数据单独估计的吗？如果是，这对跨语言 decomposition 的 validity 有何影响？\n5. 为什么全文仅 8 条引用？是否有更多引用在 appendix 中但未纳入主文？（PDF 中未见 appendix）\n6. Miao et al. (2026a) 引为 \"Shuo Miao\"——这是否与 ICML 2026 发表 CORAL 的 Miranda Muqing Miao 为同一人？如果是，请修正作者名。\n7. Probe 训练用了多少样本？是否做了 cross-validation？Logistic regression 的正则化参数是多少？\n8. 为什么没有任何 figure？Pareto frontier 以 scatter plot 呈现会比表格直观得多。\n\n---\n\n## 评分总结\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 2.5/5 |\n| Excitement | 3.0/5 |\n| Overall Assessment | 3.0/5 (Findings) |\n| Reproducibility | 2.5/5 |\n| Reviewer Confidence | 4/5 |\n",
    "reviewer_id": "1",
    "project": "xling_calib_direction"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-20T19:54:22.640776+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3816
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-20T19:54:26.901584+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
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

_source line 59 · 2026-05-20T19:54:26.952138+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-20T19:54:39.452269+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-20T19:54:39.653509+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 201
}
```

</details>

---

### Assistant

_source line 62 · 2026-05-20T19:54:47.888989+00:00_

审稿报告已提交给 Review Director。

**核心发现摘要：**

- **Overall 3.0/5 (Findings)**，Soundness 2.5，Excitement 3.0
- **4 个 Must-Fix**：(1) Abstract 与正文数值矛盾（72% vs 81%）；(2) "explains 25% of the transfer gap" 无法从 Table 5 推导；(3) 仅 8 条引用且多条作者名/标题/年份与实际出版物不符；(4) 全文无任何统计检验或方差估计
- **6 个 Should-Fix**：CaCLR "zero-label" 误导性表述、超参无 sensitivity analysis、INT8 验证过窄、无 figure、低资源语言样本量不足、probe 训练细节缺失
- 所有 10 个实验计划均已覆盖，执行完整度高
- 问题选择好、实验规模合理、Pareto frontier 框架有启发性，但 soundness 问题过多

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1"
}
```

</details>

---

## Round 2

4 recorded events

### User

_source line 63 · 2026-05-20T19:56:21.337331+00:00_

[Round 1 审稿请求]:
## 交叉审阅任务

以下是 **Reviewer 2（Novelty & Related Work 方向）** 的完整 Round 1 审稿意见。请逐条回应其 Must-Fix 和 Should-Fix 问题：

- **[AGREE]**：同意该观点，并简要说明为什么你也认同（可补充你从 Methods/Experiments 角度的佐证）
- **[REBUT]**：不同意或有保留意见，提供具体证据（引用论文中的 Section/Table/Figure）

特别关注：R2 提出的 N2（"Pareto frontier" 术语不准确）和 N3（四项贡献均为增量性）——这两个问题与你负责的方法论严谨性直接相关，请给出详细判断。

---

## Reviewer 2 完整审稿原文

**总体评分**: 2.5 / 5（介于 Revise-for-next-cycle 与 Findings 之间）

### ACL ARR 官方维度打分

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3 / 5 | 核心实验设计合理，但"Pareto frontier"术语的技术准确性存疑；decomposition 的 25% variance explained 较低却被作为主要贡献宣传 |
| Excitement | 2 / 5 | 四项贡献均为已知技术的直接扩展或组合，缺乏方法论上的惊喜 |
| Reproducibility | 3.5 / 5 | 实验设置描述清楚（§4），超参数有报告（α=0.15, β=0.10），但代码/数据未提及是否公开 |
| Confidence | 4 / 5 | 熟悉 probe-based calibration 和跨语言表征领域 |

### Must-Fix 问题

**N1** [critical] 参考文献极度稀疏——全文仅 8 篇引用
- 一篇覆盖 probe-based calibration、cross-lingual probing、multilingual calibration 的论文仅引用 8 篇文献。缺失关键文献：Conneau et al. (2020)、Pires et al. (2019)、CKA/SVCCA (Kornblith 2019, Raghu 2017)、CCPS (Wang et al.)、Belinkov (2022) probing survey、Keleg & Magdy (2023) multilingual calibration、IRT 原始文献 (Lord 1980, Baker 2001)、MKA (Chen et al. 2024)。
- Related Work 仅 ~15 行，应扩展至 1.5-2 页，引用量应在 30+ 篇。

**N2** [critical] "Pareto frontier" 术语使用不准确，核心 framing 有误导性
- 论文描述的是 depth vs. cross-lingual transfer AUROC 的单调递减关系——这是 trade-off curve 不是 Pareto frontier。没有标准 Pareto dominance 分析、hypervolume indicator、scatter plot 可视化。
- 如果只是"deeper layers 有更好的 English probe 但更差的 cross-lingual transfer"，这在多语言 NLP 中是已知现象（Pires et al. 2019; Conneau et al. 2020）。

**N3** [critical] 四项贡献的新颖性均为增量性
- Claim 1: deeper layers = more language-specific 是已知现象
- Claim 2: Civelli et al. (2025) 已证明 IRT difficulty probes 跨语言迁移，R²=0.72 未超越其结果
- Claim 3: CaCLR = BCE + calibration penalty + consistency reg，三者均为已知技术组合
- Claim 4: 方法论上直接复制 Miao & Ungar (2026) 到 20 种语言

### Should-Fix 问题

**W1** Related Work（§2）过于简略——仅 ~15 行
**W2** 全文 16 张表格、0 张图——可读性差
**W3** "First systematic study" 声明过强
**W4** Difficulty-capability decomposition 的 25% 解释力未给置信区间
**W5** CaCLR 的 improvement 幅度较小（+1.3pp avg AUROC），实际意义不清楚

### 主要优势
- S1: 实验规模超过先行工作（20语言×3架构×3基准）
- S2: CaCLR 的 zero-label 设定有实际意义
- S3: MoE vs Dense frontier 形状差异是新发现
- S4: Resource-tier gradient 在 orthogonality 上的发现有趣

### 给作者的问题
1. Table 1 中 ★ 层是否经过标准 Pareto dominance 检验？
2. CaCLR consistency reg 是否需要 parallel data？"zero-label" 定义是什么？
3. h²=0.72 与 Civelli et al. 报告值对比如何？
4. Orthogonality 的 cosine similarity 在 probe weight vectors 还是 direction vectors 上计算？
5. MoE expert routing 是否影响 layer-wise probing 的解释？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-20T19:58:19.962197+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 对 Reviewer 2 (Round 1) 的交叉回应\n\n---\n\n## Must-Fix 问题逐条回应\n\n### [AGREE] R2-N1: 参考文献极度稀疏（仅 8 篇引用）\n\n完全同意。这与我审稿报告中的 N3 问题重叠。我从 Methods/Experiments 角度补充：\n\n1. **引用信息准确性问题**比 R2 指出的\"缺失\"更严重——我通过 web search 核查发现多条现有引用的作者名/标题/年份与实际出版物不匹配（详见我的 N3）。Miao et al. (2026a) 引为 \"Shuo Miao\" 但 ICML 2026 CORAL 论文第一作者为 Miranda Muqing Miao；Zhou et al. (2024) \"LACE\" 的实际论文发表于 2025，标题也不同。\n2. R2 列出的缺失引用清单（Conneau et al. 2020、Pires et al. 2019、Belinkov 2022 survey、IRT 原始文献 Lord 1980/Baker 2001 等）我完全认同。特别是 IRT 原始文献——论文 §3.3 使用 IRT difficulty 作为核心分析工具，却未引用 IRT 的任何基础文献，这在方法论上不可接受。\n\n---\n\n### [REBUT（部分）] R2-N2: \"Pareto frontier\" 术语不准确\n\nR2 的核心主张是\"论文描述的只是单调递减的 trade-off curve，不是 Pareto frontier\"。我认为这个判断**过于绝对**，但 R2 指出的形式化不足是成立的。\n\n**反驳依据（Table 1, §5.1）：**\n\nTable 1 中 ★ 标记的 6 个层确实满足 Pareto non-dominance 的基本定义。以两个目标（EN AUROC↑, ZS-19 AUROC↑）检验：\n\n- L44: (.810, .774) — 没有其他层同时 EN≥.810 且 ZS≥.774\n- L48: (.816, .770) — L44 的 ZS 更高但 EN 更低 → 互不支配\n- L52: (.827, .763) — 同理\n- L56: (.832, .762), L60: (.835, .751), L64: (.839, .728)\n\n每一层在 EN 上优于前一层、在 ZS 上劣于前一层，形成标准的 Pareto 前沿。这**不是**简单的单调递减——ZS 在浅层（L8→L44）实际上是上升的，EN 在深层（L76→L88）是下降的。整体曲线呈倒 U 形而非单调，Pareto 前沿只出现在中间区段。\n\n**同意部分：**\n\n1. 论文确实**没有执行形式化的 Pareto dominance 检验**——★ 的标注标准未明确说明\n2. **缺少 scatter plot** 是严重的呈现问题（与我 W4 一致）——没有可视化，读者无法判断 frontier shape\n3. 论文未报告 hypervolume indicator 或其他多目标优化标准度量\n4. \"Architecture-dependent frontier shape\" 这个 claim（Table 14: Depth% 分别为 60%, 58%, 60%）在数值上差异很小，用 \"architecture-dependent\" 描述有夸大之嫌\n\n**结论：术语本身的使用不算错误，但缺乏形式化验证和可视化。建议作者 (1) 明确定义 Pareto dominance 判定标准 (2) 添加 scatter plot (3) 报告 hypervolume 或 ε-dominance 指标。** R2 说\"这是已知现象\"有一定道理（deeper = more language-specific），但将其形式化为 Pareto frontier 并跨 3 个架构量化是新的贡献，只是目前形式化程度不够。\n\n---\n\n### [AGREE（部分）] R2-N3: 四项贡献均为增量性\n\n从 Methods 角度逐项评估：\n\n**Claim 1（Pareto frontier）**：[AGREE with nuance]\n- R2 说 \"deeper layers = more language-specific 是已知现象\"——这个大方向确实已知（Pires et al. 2019, Conneau et al. 2020）。但将其量化为 Pareto frontier、并发现 ~58-60% depth 的跨架构收敛点，具有一定增量价值。\n- 然而，Table 14 显示三种架构的 Depth% 分别为 60%, 58%, 60%，ρ 分别为 .88, .82, .86——差异确实不大，\"architecture-dependent\" 的 framing 过强。\n\n**Claim 2（decomposition）**：[AGREE]\n- 如果 Civelli et al. (2025) 确实已证明 IRT difficulty probes 可以跨语言迁移，那本文的 R²=0.72 仅是在不同模型/规模上的 replication。\n- 更关键的是：论文声称 \"explains 25% of the transfer gap\"（abstract），但这个 25% 在 Table 5 中无法 verify（我在 N2 中已详述）。Decomposition 的解释力不清不楚，难以构成独立贡献。\n\n**Claim 3（CaCLR）**：[REBUT（部分）]\n- R2 说 \"BCE + calibration penalty + consistency reg 均为已知技术\"——这没错，但**组合并非平凡**。Table 8 的 ablation 清楚显示 L_cons 贡献 +4.1pp AUROC，L_SB-ECE 贡献 calibration improvement（ECE 从 0.078→0.061）。三项 loss 之间有 synergy，不是简单堆叠。\n- 从 Experiments 角度，CaCLR 在 Table 7 中 AUROC .804 vs linear proj .770（+3.4pp），且 CaCLR 的 ECE 也更低（.058 vs .062）。这个提升虽不巨大，但在 zero-label 条件下优于 few-shot(100)（.762）是有实际意义的。\n- **但我同意 R2 的一个隐含观点**：CaCLR 声称 \"zero-label\" 却需要 parallel data（用于 L_cons），这与 linear projection 的资源需求本质相同。如果两者都需要 parallel data，3.4pp 的改进确实算 incremental。\n- **关于 R2 提到的 \"+1.3pp\"**：我在论文中找不到这个数字的来源。Table 7 显示 CaCLR vs linear proj 差距为 3.4pp，Table 2 显示 3.3pp。如果 1.3pp 来自某个特定架构/子集，R2 应标明来源。\n\n**Claim 4（orthogonality）**：[AGREE]\n- 完全同意 R2 的判断。Tables 10-11 的方法论与 Miao & Ungar (2026) 一致，贡献仅在于从英语扩展到 20 种语言。Resource-tier gradient（§5.4 末尾提到）是有趣的观察，但分析深度不足以构成独立 claim。\n\n**总体判断**：四项贡献中，Claim 3（CaCLR）的新颖性最高但受 \"zero-label\" 误导性表述和 parallel data 依赖的削弱；Claim 1 有增量价值但 framing 过强；Claims 2 和 4 的独立新颖性不足。作为整体 package，这些贡献在 **Findings 级别**是可以接受的。\n\n---\n\n## Should-Fix 问题逐条回应\n\n### [AGREE] R2-W1: Related Work 过于简略\n与我的观察一致。~15 行 Related Work 对这个研究范围而言远远不够。\n\n### [AGREE] R2-W2: 16 张表格、0 张图\n这与我的 W4 完全一致。一篇关于 Pareto frontier 的论文没有任何 scatter plot 是不可接受的。\n\n### [AGREE] R2-W3: \"First systematic study\" 声明过强\n鉴于 Civelli et al. (2025)、Xiao et al. (2025)、Zhou et al. (LACE, 2025) 的存在，这个 claim 至少需要加限定语。\n\n### [AGREE] R2-W4: 25% 解释力无置信区间\n我完全同意，并在我的审稿报告中更进一步指出：这个 \"25%\" 本身在论文数据中就无法 verify（我的 N2）。在无法确认数字来源的情况下，置信区间的缺失是次要问题——首先需要解释 25% 从何而来。\n\n### [AGREE（附修正）] R2-W5: CaCLR improvement +1.3pp\n同意 CaCLR 改进幅度有限是合理关切。但 **+1.3pp 这个数字我在论文中找不到对应**。我能 verify 的是：\n- Table 7（跨两个架构平均）：CaCLR .804 vs linear proj .770 = **+3.4pp**\n- Table 2（Qwen3 best-transfer layer）：CaCLR .814 vs linear proj .781 = **+3.3pp**\n\n如果 R2 的 1.3pp 来自特定条件/架构，应标明来源。即使按 3.4pp 计算，在缺乏统计检验的情况下，这个差距是否 significant 仍然存疑（与我的 N4 一致）。\n\n---\n\n## 补充说明\n\nR2 评分表中提到 \"α=0.15, β=0.10\"，但论文 §3.4 实际写的是 **α=0.15, β=0.08**。这是 R2 审稿中的小错误，不影响其论点。\n\n---\n\n## 总结\n\nR2 的 6 个 Must-Fix/Should-Fix 问题中，我 **AGREE 5 个**（N1, N3-Claim2/4, W1-W5），**部分 REBUT 2 个**（N2 术语使用本身不算错但缺形式化；N3-Claim3 CaCLR 的组合有一定非平凡性）。R2 和我的审稿在以下问题上高度一致：\n\n1. 参考文献严重不足且有误\n2. 缺乏统计检验\n3. 无可视化图表\n4. Abstract 中的数字（25%, 72%）不可靠\n5. CaCLR \"zero-label\" 表述有误导性\n\n我维持 **Overall 3.0 (Findings)** 的评分。R2 给 2.5，差异主要在于我对 CaCLR 方法论贡献和 Pareto frontier 框架的评价略高。\n",
  "reviewer_id": "1",
  "project": "xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 对 Reviewer 2 (Round 1) 的交叉回应\n\n---\n\n## Must-Fix 问题逐条回应\n\n### [AGREE] R2-N1: 参考文献极度稀疏（仅 8 篇引用）\n\n完全同意。这与我审稿报告中的 N3 问题重叠。我从 Methods/Experiments 角度补充：\n\n1. **引用信息准确性问题**比 R2 指出的\"缺失\"更严重——我通过 web search 核查发现多条现有引用的作者名/标题/年份与实际出版物不匹配（详见我的 N3）。Miao et al. (2026a) 引为 \"Shuo Miao\" 但 ICML 2026 CORAL 论文第一作者为 Miranda Muqing Miao；Zhou et al. (2024) \"LACE\" 的实际论文发表于 2025，标题也不同。\n2. R2 列出的缺失引用清单（Conneau et al. 2020、Pires et al. 2019、Belinkov 2022 survey、IRT 原始文献 Lord 1980/Baker 2001 等）我完全认同。特别是 IRT 原始文献——论文 §3.3 使用 IRT difficulty 作为核心分析工具，却未引用 IRT 的任何基础文献，这在方法论上不可接受。\n\n---\n\n### [REBUT（部分）] R2-N2: \"Pareto frontier\" 术语不准确\n\nR2 的核心主张是\"论文描述的只是单调递减的 trade-off curve，不是 Pareto frontier\"。我认为这个判断**过于绝对**，但 R2 指出的形式化不足是成立的。\n\n**反驳依据（Table 1, §5.1）：**\n\nTable 1 中 ★ 标记的 6 个层确实满足 Pareto non-dominance 的基本定义。以两个目标（EN AUROC↑, ZS-19 AUROC↑）检验：\n\n- L44: (.810, .774) — 没有其他层同时 EN≥.810 且 ZS≥.774\n- L48: (.816, .770) — L44 的 ZS 更高但 EN 更低 → 互不支配\n- L52: (.827, .763) — 同理\n- L56: (.832, .762), L60: (.835, .751), L64: (.839, .728)\n\n每一层在 EN 上优于前一层、在 ZS 上劣于前一层，形成标准的 Pareto 前沿。这**不是**简单的单调递减——ZS 在浅层（L8→L44）实际上是上升的，EN 在深层（L76→L88）是下降的。整体曲线呈倒 U 形而非单调，Pareto 前沿只出现在中间区段。\n\n**同意部分：**\n\n1. 论文确实**没有执行形式化的 Pareto dominance 检验**——★ 的标注标准未明确说明\n2. **缺少 scatter plot** 是严重的呈现问题（与我 W4 一致）——没有可视化，读者无法判断 frontier shape\n3. 论文未报告 hypervolume indicator 或其他多目标优化标准度量\n4. \"Architecture-dependent frontier shape\" 这个 claim（Table 14: Depth% 分别为 60%, 58%, 60%）在数值上差异很小，用 \"architecture-dependent\" 描述有夸大之嫌\n\n**结论：术语本身的使用不算错误，但缺乏形式化验证和可视化。建议作者 (1) 明确定义 Pareto dominance 判定标准 (2) 添加 scatter plot (3) 报告 hypervolume 或 ε-dominance 指标。** R2 说\"这是已知现象\"有一定道理（deeper = more language-specific），但将其形式化为 Pareto frontier 并跨 3 个架构量化是新的贡献，只是目前形式化程度不够。\n\n---\n\n### [AGREE（部分）] R2-N3: 四项贡献均为增量性\n\n从 Methods 角度逐项评估：\n\n**Claim 1（Pareto frontier）**：[AGREE with nuance]\n- R2 说 \"deeper layers = more language-specific 是已知现象\"——这个大方向确实已知（Pires et al. 2019, Conneau et al. 2020）。但将其量化为 Pareto frontier、并发现 ~58-60% depth 的跨架构收敛点，具有一定增量价值。\n- 然而，Table 14 显示三种架构的 Depth% 分别为 60%, 58%, 60%，ρ 分别为 .88, .82, .86——差异确实不大，\"architecture-dependent\" 的 framing 过强。\n\n**Claim 2（decomposition）**：[AGREE]\n- 如果 Civelli et al. (2025) 确实已证明 IRT difficulty probes 可以跨语言迁移，那本文的 R²=0.72 仅是在不同模型/规模上的 replication。\n- 更关键的是：论文声称 \"explains 25% of the transfer gap\"（abstract），但这个 25% 在 Table 5 中无法 verify（我在 N2 中已详述）。Decomposition 的解释力不清不楚，难以构成独立贡献。\n\n**Claim 3（CaCLR）**：[REBUT（部分）]\n- R2 说 \"BCE + calibration penalty + consistency reg 均为已知技术\"——这没错，但**组合并非平凡**。Table 8 的 ablation 清楚显示 L_cons 贡献 +4.1pp AUROC，L_SB-ECE 贡献 calibration improvement（ECE 从 0.078→0.061）。三项 loss 之间有 synergy，不是简单堆叠。\n- 从 Experiments 角度，CaCLR 在 Table 7 中 AUROC .804 vs linear proj .770（+3.4pp），且 CaCLR 的 ECE 也更低（.058 vs .062）。这个提升虽不巨大，但在 zero-label 条件下优于 few-shot(100)（.762）是有实际意义的。\n- **但我同意 R2 的一个隐含观点**：CaCLR 声称 \"zero-label\" 却需要 parallel data（用于 L_cons），这与 linear projection 的资源需求本质相同。如果两者都需要 parallel data，3.4pp 的改进确实算 incremental。\n- **关于 R2 提到的 \"+1.3pp\"**：我在论文中找不到这个数字的来源。Table 7 显示 CaCLR vs linear proj 差距为 3.4pp，Table 2 显示 3.3pp。如果 1.3pp 来自某个特定架构/子集，R2 应标明来源。\n\n**Claim 4（orthogonality）**：[AGREE]\n- 完全同意 R2 的判断。Tables 10-11 的方法论与 Miao & Ungar (2026) 一致，贡献仅在于从英语扩展到 20 种语言。Resource-tier gradient（§5.4 末尾提到）是有趣的观察，但分析深度不足以构成独立 claim。\n\n**总体判断**：四项贡献中，Claim 3（CaCLR）的新颖性最高但受 \"zero-label\" 误导性表述和 parallel data 依赖的削弱；Claim 1 有增量价值但 framing 过强；Claims 2 和 4 的独立新颖性不足。作为整体 package，这些贡献在 **Findings 级别**是可以接受的。\n\n---\n\n## Should-Fix 问题逐条回应\n\n### [AGREE] R2-W1: Related Work 过于简略\n与我的观察一致。~15 行 Related Work 对这个研究范围而言远远不够。\n\n### [AGREE] R2-W2: 16 张表格、0 张图\n这与我的 W4 完全一致。一篇关于 Pareto frontier 的论文没有任何 scatter plot 是不可接受的。\n\n### [AGREE] R2-W3: \"First systematic study\" 声明过强\n鉴于 Civelli et al. (2025)、Xiao et al. (2025)、Zhou et al. (LACE, 2025) 的存在，这个 claim 至少需要加限定语。\n\n### [AGREE] R2-W4: 25% 解释力无置信区间\n我完全同意，并在我的审稿报告中更进一步指出：这个 \"25%\" 本身在论文数据中就无法 verify（我的 N2）。在无法确认数字来源的情况下，置信区间的缺失是次要问题——首先需要解释 25% 从何而来。\n\n### [AGREE（附修正）] R2-W5: CaCLR improvement +1.3pp\n同意 CaCLR 改进幅度有限是合理关切。但 **+1.3pp 这个数字我在论文中找不到对应**。我能 verify 的是：\n- Table 7（跨两个架构平均）：CaCLR .804 vs linear proj .770 = **+3.4pp**\n- Table 2（Qwen3 best-transfer layer）：CaCLR .814 vs linear proj .781 = **+3.3pp**\n\n如果 R2 的 1.3pp 来自特定条件/架构，应标明来源。即使按 3.4pp 计算，在缺乏统计检验的情况下，这个差距是否 significant 仍然存疑（与我的 N4 一致）。\n\n---\n\n## 补充说明\n\nR2 评分表中提到 \"α=0.15, β=0.10\"，但论文 §3.4 实际写的是 **α=0.15, β=0.08**。这是 R2 审稿中的小错误，不影响其论点。\n\n---\n\n## 总结\n\nR2 的 6 个 Must-Fix/Should-Fix 问题中，我 **AGREE 5 个**（N1, N3-Claim2/4, W1-W5），**部分 REBUT 2 个**（N2 术语使用本身不算错但缺形式化；N3-Claim3 CaCLR 的组合有一定非平凡性）。R2 和我的审稿在以下问题上高度一致：\n\n1. 参考文献严重不足且有误\n2. 缺乏统计检验\n3. 无可视化图表\n4. Abstract 中的数字（25%, 72%）不可靠\n5. CaCLR \"zero-label\" 表述有误导性\n\n我维持 **Overall 3.0 (Findings)** 的评分。R2 给 2.5，差异主要在于我对 CaCLR 方法论贡献和 Pareto frontier 框架的评价略高。\n",
    "reviewer_id": "1",
    "project": "xling_calib_direction"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-20T19:58:23.525923+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3563
}
```

</details>

---

### Assistant

_source line 66 · 2026-05-20T19:58:30.804948+00:00_

交叉回应已提交。核心判断：

- **N1（引用不足）**：完全同意，并补充了引用准确性问题
- **N2（Pareto frontier 术语）**：部分反驳——Table 1 的 ★ 层确实满足 Pareto non-dominance 定义，术语本身不算误用，但论文缺乏形式化验证和 scatter plot
- **N3（四项贡献增量性）**：逐项评估——Claim 3 (CaCLR) 的组合有非平凡性（Table 8 ablation 支撑），Claims 2/4 确实增量性较强
- 同时修正了 R2 的两个小错误：β 值（R2 写 0.10，实际 0.08）和 CaCLR improvement 幅度（R2 写 +1.3pp，Table 7 实际为 +3.4pp）

维持 Overall 3.0 (Findings) 评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1"
}
```

</details>

---

## Round 3

36 recorded events

### User

_source line 67 · 2026-05-21T04:26:27.069773+00:00_

[Round 1 审稿请求]:
[Dream 审稿任务]

你是本次 Dream 模拟论文的唯一 Reviewer，需要一次性覆盖以下三个维度：

## 论文信息

- **标题**: Cross-Lingual Correctness Probe Transfer Reveals Architecture-Dependent Pareto Frontiers: Discovery, Negative Result, and Practical Recommendation
- **PDF 路径**: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/review_input_e90a5c14.pdf
- **实验设计参考**: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/review_context.yaml

## 审稿维度

A. 方法与实验
   - 方法描述是否完整、claim 是否被实验数据支撑
   - 实验设计是否覆盖关键 baseline / ablation / 跨数据集
   - 数据呈现（表格 / 图）是否能让审稿人复现结论

B. 新颖性与相关工作
   - 与现有工作的差异化是否清晰、文献覆盖是否充分
   - Story 是否站得住脚（即使数据是模拟的，论证逻辑必须自洽）

C. 整体评判
   - 请基于论文内容独立评判，不要假设论文结果的质量高低
   - 与论文声称矛盾的实验结果 / claim 必须显式指出

## 评分标准

按 top ML venue 通用标准审稿（接受率 ~25%，6 分制：1=Strong Reject … 6=Strong Accept）。

## 评分校准规则

- **3+ Major issues** → 不高于 Borderline Reject，除非每个 issue 都有明确的 minor revision 可修复路径
- **2 Major issues** → 不高于 Weak Accept
- **1 Major issue** → 不高于 Accept（非 Strong Accept）
- **0 Major issues** → 可给 Strong Accept

每条 Major issue 必须有 explicit justification 解释为什么它是 Major 而非 Minor。

## 不需要评审的维度

- 格式、排版、参考文献样式、字数限制（Dream 论文是模拟的，这些无意义）
- Reproducibility checklist、代码/数据可用性
- 具体数值精确性（数字是想象的，关注实验设计而非数值）
- 伦理/IRB、匿名性

## 需要评审但标注为 "presentation 层面" 的维度

- Reference 真实性（发现虚假引用标注为 paper writing 问题）
- 论文完整度（是否有截断）
- Related Work 引用数量

## 必须评审的维度（idea/design 层面）

- 实验设计是否足以支撑 claims（假设数据为真）
- 叙事逻辑是否自洽
- Novelty 定位和 Related Work landscape（关键竞争方法是否遗漏）
- Scope 与目标 venue 的匹配度
- Claim 的 generality 是否被实验范围支撑

每条 weakness 必须标注属于 **idea 层面** 还是 **presentation 层面**。

请通过 `review_reviewer_post_to_director(text, reviewer_id="1", project="xling_calib_direction", dream_id="20260521T032808")` 汇报。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-21T04:26:36.305391+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/review_input_e90a5c14.pdf",
  "project": "xling_calib_direction",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/review_input_e90a5c14.pdf",
    "project": "xling_calib_direction",
    "dpi": "150"
  }
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-21T04:26:36.859740+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/review_context.yaml"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-21T04:26:38.117193+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 349.6}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 335.1}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 241.9}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 318.9}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 264.2}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 253.3}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 268.6}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 273.5}, {\"page\"
…[truncated 1470 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1811
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-21T04:26:38.471068+00:00_

1	narrative_guidance: 'Discovery + principled negative result + practical recommendation
2	  三段叙事。 (1) Pareto frontier 在 Qwen3-235B 上清晰（rho ~ -0.50），在 Llama 4 Scout 上 language-specific（global
3	  rho ~ -0.12）：部分语言随 depth 改善（ar/ko/hi）， 部分退化（zh/sw），验证 architecture-dependent tradeoff
4	  shape。 (2) CaCLR β sweep 3 OOM 证明 MMD consistency loss inert（d=0.07, p=0.38）。 CKA
5	  几何分析提供 suggestive 解释——MMD matches marginals but not low-dim directional structure——但
6	  partial correlation controlling depth 仅 r=0.18, p=0.11，降级为 suggestive correlational
7	  analysis。Between-language correlation 成立（same-layer r=0.52, p<0.01）。 (3) Linear
8	  projection ~50 pairs 是实际方案（+3.5pp over zero-shot），surpasses CaCLR at ~20 pairs。
9	  Decomposition 定性成立（65% combos improved, d=0.25），orthogonality 跨语言持续 但 low-resource
10	  variance 增大（cosine max 0.11）。 Control task artifact warning 升级为独立贡献：~27% lang-layer
11	  combos selectivity < 0.05，集中在 low-resource + shallow layers。 Target: EACL borderline
12	  accept，以 discovery + systematic negative result 发表。
13	
14	  '
15	imagined_experiments:
16	- name: Qwen3-235B-A22B Full Pareto Frontier
17	  plan_id: plan_001
18	  description: 'Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT4): 24
19	    probed layers (every 4th), 20 languages, EN correctness probes (LogReg + MLP),
20	    5 transfer conditions. Per-language Spearman rho.
21	
22	    '
23	  expected_results:
24	    en_best_auroc: 0.8
25	    en_best_layer: 72
26	    en_best_ece_raw: 0.175
27	    en_auroc_range:
28	    - 0.54
29	    - 0.8
30	    en_auroc_at_50pct_depth_L48: 0.77
31	    en_auroc_profile_summary: 'L0-L20: 0.54-0.67 (early buildup); L24-L44: 0.70-0.76
32	      (mid layers); L48-L68: 0.77-0.80 (approaching peak); L72: 0.80 (peak); L76-L92:
33	      0.79-0.75 (slight decline)
34	
35	      '
36	    zs_at_en_optimal_L72:
37	      zh: 0.71
38	      es: 0.7
39	      fr: 0.7
40	      de: 0.69
41	      ja: 0.67
42	      pt: 0.69
43	      nl: 0.68
44	      ru: 0.67
45	      ar: 0.65
46	
…[truncated 56970 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1611
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-21T04:26:47.156294+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p1.png"
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-21T04:26:47.661933+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 505
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-21T04:26:47.662395+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p2.png"
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-21T04:26:48.618951+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-21T04:26:48.619368+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p3.png"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-21T04:26:49.122427+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-21T04:26:49.122880+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p4.png"
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-21T04:26:50.078794+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-21T04:26:50.079259+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p5.png"
  }
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-21T04:26:50.632294+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-21T04:26:50.783227+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p6.png"
  }
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-21T04:26:51.084866+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p7.png"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-21T04:26:51.186513+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-21T04:26:51.539121+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-21T04:26:55.956445+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p8.png"
  }
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-21T04:26:56.007341+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p9.png"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-21T04:26:56.864022+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-21T04:26:56.866086+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 858
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-21T04:26:56.866471+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p10.png"
  }
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-21T04:26:57.321689+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-21T04:26:57.322336+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p11.png"
  }
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-21T04:26:58.277230+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-21T04:26:58.327841+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p12.png"
  }
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-21T04:26:58.480556+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 152
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-21T04:26:58.480908+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images/paper_p13.png"
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-21T04:26:58.532977+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-21T04:32:22.361156+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 — Dream Median Paper 审稿报告\n\n**论文**: Cross-Lingual Correctness Probe Transfer Reveals Architecture-Dependent Pareto Frontiers: Discovery, Negative Result, and Practical Recommendation  \n**审稿标准**: Top ML venue, 6-point scale (1=Strong Reject … 6=Strong Accept), ~25% acceptance rate  \n**审稿维度**: A. Methods & Experiments, B. Novelty & Related Work, C. Overall Assessment\n\n---\n\n## 总体评分\n\n**Overall Score: 4 (Weak Accept)**  \n**一句话总结**: 实验方法论扎实、claims 校准诚实、三段叙事（discovery + negative result + recommendation）逻辑自洽，但个体贡献的新颖性偏增量、负面结果的 scope 可讨论。在 honest negative result + actionable recommendation 的路线上做得好，适合 Findings 或 borderline main conference。\n\n---\n\n## A. Methods & Experiments\n\n### Strengths\n\n**S-M1** [idea] 统计方法论全面且一致。Bootstrap 95% CIs、paired permutation tests、Cohen's d 贯穿所有实验（§4 明确声明；Tables 3-7 均有 p 值和 effect size）。这在 probing 文献中属于 above-average 标准。\n\n**S-M2** [idea] CaCLR β sweep 设计充分。Table 3 跨 3 个数量级（0.001–1.0）、两种架构、20 种语言，无任何 β 值达到 p<0.05 或 d>0.2。配合 component ablation（Table 4: α 项贡献 -5pp ECE，β 项贡献 +0.001pp AUROC ≈ 0），negative result 的实验支撑完整。\n\n**S-M3** [idea] CKA 分析的诚实处理。§5.3 展示 pooled correlation r=0.52 后立即做 partial correlation controlling depth（r=0.18, p=0.11），主动将 CKA 从 \"geometric explanation\" 降级为 \"suggestive correlational analysis\"。Between-language claim（same-depth r=0.52, p=0.014, n=19）单独成立。这种 self-critical 分析方式值得肯定。\n\n**S-M4** [idea] Linear projection sample efficiency 曲线（§5.6, Table 9）提供了可操作的 practitioner guidance：~50 pairs 达 90% achievable improvement，knee 在 ~60 pairs，20 pairs 即超过 CaCLR。\n\n**S-M5** [idea] Control task analysis（§5.7, Table 10）将 Hewitt & Liang (2019) framework 系统扩展到 20 语言 × 多层，发现 ~27% 的 lang-layer 组合 selectivity < 0.05，这是一个 generalizable methodological warning。\n\n**S-M6** [idea] Mean-shift 的 rank-invariance proof 和实验验证（ΔAUROC ≡ 0）是一个干净的 baseline 排除。\n\n### Weaknesses\n\n**W-M1** [idea] **MMD 在 1-D probe logits 上操作限制了 negative result 的 scope**。§3.2 明确承认 \"a design limitation: it can only match marginal distributions of scalar outputs\"。但论文的结论（§6 Discussion \"distributional matching fails because the problem is geometric rotation\"）隐含了更广泛的 claim——即任何 distributional matching 都无法解决跨语言 probe transfer。这个推论依赖 Zhao et al. 的理论（marginal matching fails when P(Y|X) differs），但 kernel MMD 在高维空间中能 capture 的结构远多于 1-D marginals。论文未测试：(a) MMD 在 activation space（probe 之前）的效果；(b) Optimal transport / Sinkhorn 在高维空间的效果。这意味着 negative result 严格来说只关闭了 \"1-D probe output distributional matching\" 这条路，不是 \"distributional matching for cross-lingual probe transfer\" 的全部。\n- **为什么不是 Major issue**：论文的 framing 较为谨慎（§3.2 和 §6 均有 caveat），且理论论证（Zhao et al. + linear projection 成功作为 constructive evidence）在逻辑上是自洽的。但这削弱了 negative result 的 generality，从 \"distributional matching doesn't work\" 降为 \"our specific instantiation doesn't work.\"\n- **标注**: idea 层面\n\n**W-M2** [idea] **Table 1 未展示完整的 24 层 × 20 语言数据**。论文在 Qwen3 上 probe 了 24 层（§4），但 Table 1 仅呈现 L48 和 L72 两个代表层的 per-language AUROC 加上 per-language ρ。完整数据应至少在 appendix 中呈现（目前 appendix 无此内容）。Pareto frontier 的 claim 需要读者能看到完整的 depth profile。\n- **标注**: presentation 层面\n\n**W-M3** [idea] **Gemma 4 31B 数据覆盖不足**。作为第三种架构，仅出现在 Table 14（appendix 的 3 行摘要）和 §5.1 的一段文字中。没有 per-language breakdown、没有 β sweep、没有 full transfer method comparison。三架构对比的 claim 建立在 Qwen3 和 Llama4 的详细数据 + Gemma4 的摘要数据之上，不对等。\n- **标注**: idea 层面\n\n**W-M4** [idea] **Decomposition 的 IRT R²=0.40 较低**。Table 7 报告 65% combos improved（d=0.25, p=0.028）。论文诚实地将此降级为 qualitative claim，这是正确的做法。但 R²=0.40 意味着 IRT difficulty probe 只解释 40% 的 item difficulty variance，难以可靠地 \"project out\" difficulty direction——残差中仍混有大量 difficulty signal，削弱 decomposition 的 cleanness。difficulty-correctness cosine = 0.20 也确认了不完全正交。\n- **标注**: idea 层面\n\n---\n\n## B. Novelty & Related Work\n\n### Strengths\n\n**S-N1** [idea] **\"Negative result as contribution\" 的 framing 在 NLP 社区有价值**。系统地测试一个 \"看起来应该有效\" 的方法（MMD consistency regularization）并提供 principled explanation（Zhao et al. domain adaptation theory + geometric rotation）比又一个 marginal improvement 更有意义。这个 narrative choice 是论文最大的亮点。\n\n**S-N2** [idea] **Llama 4 Scout 的 language-specific Pareto 行为**（4/20 语言 ρ > 0）是一个 genuinely new observation。这不是 \"deeper = worse\" 的简单重复——而是发现某些语言在某些架构上 deeper layers transfer BETTER。这与 Qwen3 的 uniform negative ρ 形成 qualitatively different pattern，超越了 Pires et al. (2019) / Conneau et al. (2020) 的 general observation。\n\n**S-N3** [idea] **Control task artifact warning（~27%）作为独立贡献** 是 well-positioned 的。它对整个 cross-lingual probing 社区有指导意义，不限于本文的 correctness probing setting。\n\n**S-N4** [idea] **Related Work 结构合理**——§2 分 6 个子领域（Probe-Based Calibration, Cross-Lingual Probing, Cross-Lingual Alignment, Domain Adaptation Theory, Representation Similarity, Probing Methodology），每个都有恰当的 positioning。\n\n### Weaknesses\n\n**W-N1** [presentation] **14 篇引用仍低于预期**。同类 ACL/EMNLP 论文通常 30-50 篇。缺失的关键文献：\n  - IRT 基础文献（Lord 1980, Baker 2001）—— §3.3 使用 IRT 但未引用任何 psychometrics 原始文献\n  - Belinkov (2022) probing survey\n  - Keleg & Magdy (2023) multilingual calibration\n  - Guo et al. (2017) temperature scaling（论文多次提到 ECE 但未引用 calibration 的经典文献）\n  - 更多 domain adaptation theory（Ganin et al. 2016; Long et al. 2015）\n  - MoE 架构分析文献（Fedus et al. 2022; Zoph et al. 2022）\n  - 部分现有引用的作者名/标题可能仍有 accuracy issue（基于 \"best\" 版本的核查经验，median 版本的 Miao 引用格式也存疑）\n\n**W-N2** [idea] **\"First systematic study\" claim（§7 Conclusion）需要 qualification**。Civelli et al. (2025) 和 Xiao et al. (2025) 已涉及 cross-lingual probe transfer。论文 §2 中引用了它们但未充分说明自己的差异化。应改为 \"the first study systematically evaluating cross-lingual correctness probe transfer across multiple architectures with principled negative result methodology\" 或类似限定。\n\n**W-N3** [idea] **CaCLR 的 negative result novelty 取决于 MMD 在 probe outputs 上的应用是否为 \"obvious limitation\"**。§3.2 自己指出 MMD 在 1-D 上只能 match marginal distributions。如果这一点在设计时就显而易见，那么确认它确实不 work 的 surprise factor 有限。论文应讨论：是否有先前工作提出或使用过 MMD on probe outputs for cross-lingual transfer？如果没有人提出过这个方法，那 \"关闭这条路\" 的价值需要 contextualize。\n\n---\n\n## C. Overall Assessment\n\n### Major Issues\n\n**无明确的 Major Issue**。论文最大的 concern（W-M1: MMD scope, W-N3: negative result novelty）在 framing 上都有合理的 caveat。根据评分校准规则（0 Major → 可给 Strong Accept），上限为 6。\n\n### Minor Issues（按重要性排序）\n\n1. **W-M1** MMD scope 限制 negative result 的 generality（idea, moderate）\n2. **W-N1** 14 篇引用不足（presentation）\n3. **W-M3** Gemma 4 数据不对等（idea, minor-moderate）\n4. **W-N2** \"First systematic study\" overclaim（idea, minor）\n5. **W-M2** 缺完整 layer × language table（presentation）\n6. **W-M4** IRT R²=0.40 decomposition 较弱（idea, minor — paper 已自我降级）\n7. **W-N3** Negative result 的 surprise factor（idea, minor）\n\n### Narrative Self-Consistency Check\n\n| Claim | 支撑位置 | 是否自洽 | 备注 |\n|-------|---------|---------|------|\n| Architecture-dependent Pareto | Tables 1-2, 14 | ✓ | Qwen3 全负 ρ vs Llama4 4 正 vs Gemma4 最强负 |\n| CaCLR β inert | Tables 3-4 | ✓ | 3 OOM, d=0.07, p=0.38, both architectures |\n| CKA = suggestive only | Table 6 | ✓ | Pooled r=0.52 → partial r=0.18 (p=0.11) |\n| Linear proj ~50 pairs sufficient | Table 9 | ✓ | Knee ~60, 20 pairs > CaCLR |\n| Decomposition = qualitative | Table 7 | ✓ | d=0.25, 65% improved, random control d=0.05 |\n| Orthogonality persists | Table 8 | ✓ | All < 0.12, ρ=-0.58 with resource tier |\n| 27% capacity artifacts | Table 10 | ✓ | Shallow + low-resource concentrated |\n| Abstract 数字 vs 正文 | 全文 | ✓ | **无不一致**（与 \"best\" 版本形成鲜明对比）|\n\n### Experiment Coverage vs. Review Context\n\n| Plan | 覆盖 | 位置 | 备注 |\n|------|-----|------|------|\n| plan_001: Qwen3 Pareto | ✓ | Table 1, §5.1 | Table 仅摘要层，非完整 grid |\n| plan_002: Llama4 Pareto | ✓ | Table 2, §5.1 | |\n| plan_003: CaCLR | ✓ | Tables 3-5, §5.2 | 完整 β sweep + ablation + comparison |\n| plan_004: Decomposition | ✓ | Table 7, §5.4 | |\n| plan_005: Orthogonality | ✓ | Table 8, §5.5 | |\n| plan_006: Probe Complexity | ✓ | Table 11 (Appendix), §5.8 | |\n| plan_007: Benchmarks | ✓ | Table 12 (Appendix), §5.9 | |\n| plan_008: Gemma 4 | ✓ | Table 14 (Appendix), §5.1 | 数据量偏少 |\n| plan_009: Extended Coverage | ✓ | §5.9, A.6 | 52 languages, 67% viable |\n| plan_010: Quantization | ✓ | Table 13 (Appendix), §5.9 | Both architectures |\n| plan_011: CKA Analysis | ✓ | Table 6, §5.3 | partial correlation 是 key contribution |\n| plan_012: LP Sensitivity | ✓ | Table 9, §5.6 | 10-200 pairs learning curve |\n| plan_013: Control Tasks | ✓ | Table 10, §5.7 | 27% artifact finding |\n\n13/13 plans 全部覆盖。\n\n### 主要优势总结\n\n1. **Claim 校准诚实**——每个 claim 都有适当的 qualifier（\"suggestive,\" \"qualitative,\" \"principled negative result\"），无 overclaim\n2. **三段叙事逻辑连贯**——discovery → negative result → constructive recommendation，每一段都有独立的实验支撑\n3. **统计方法论在 probing 文献中 above average**——bootstrap CIs + permutation tests + Cohen's d 贯穿全文\n4. **Llama 4 Scout language-specific behavior** 是 genuinely new finding，不是已知现象的简单重复\n5. **Control task warning 是 generalizable contribution**——对整个 cross-lingual probing 社区有价值\n6. **内部一致性完美**——abstract 数字与正文完全吻合，无任何自相矛盾\n\n### 给作者的问题\n\n1. CaCLR 的 L_cons 使用 MMD 在 1-D probe logits 上。是否考虑过在高维 activation space 中做 distributional matching（如 kernel MMD on hidden states 或 optimal transport）？如果 Zhao et al. 的理论确实排除了所有 marginal matching 方法，这应该在 §6 中更明确地论证。\n2. Gemma 4 31B 是否有完整的 per-language breakdown 和 transfer method comparison？如果有，为什么不放在 appendix 中？\n3. IRT difficulty probe 的 R²=0.40——是否尝试过更复杂的 difficulty model（如 2-PL IRT 或 neural IRT）？R²=0.40 意味着 projecting out difficulty 时会引入 substantial noise。\n4. Table 1 的完整 24 层 × 20 语言数据是否可以放入 supplementary material？\n5. 论文是否有计划公开代码和 probing 数据以支持 reproducibility？（review context 提到 \"no code/data release mentioned\"）\n\n---\n\n## 评分总结\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Score | **4 (Weak Accept)** | 0 Major issues, 方法论扎实, claims 诚实, narrative 自洽; 但个体贡献偏增量, negative result 的 scope 可讨论 |\n| Confidence | **4/5** | 仔细阅读全文, 熟悉 probing/calibration/cross-lingual 文献 |\n\n**与 \"best\" 版本对比**：median 版在以下方面显著优于 best 版——(1) 内部一致性（无数字矛盾），(2) 统计方法论（有 CIs/p/d），(3) claims 校准（不 overclaim），(4) Related Work（14 vs 8 篇，有结构），(5) narrative 诚实度（承认 negative result 而非包装为 positive）。评分差距（4 vs 3）反映了这些质量差异。\n",
  "reviewer_id": "1",
  "project": "xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 — Dream Median Paper 审稿报告\n\n**论文**: Cross-Lingual Correctness Probe Transfer Reveals Architecture-Dependent Pareto Frontiers: Discovery, Negative Result, and Practical Recommendation  \n**审稿标准**: Top ML venue, 6-point scale (1=Strong Reject … 6=Strong Accept), ~25% acceptance rate  \n**审稿维度**: A. Methods & Experiments, B. Novelty & Related Work, C. Overall Assessment\n\n---\n\n## 总体评分\n\n**Overall Score: 4 (Weak Accept)**  \n**一句话总结**: 实验方法论扎实、claims 校准诚实、三段叙事（discovery + negative result + recommendation）逻辑自洽，但个体贡献的新颖性偏增量、负面结果的 scope 可讨论。在 honest negative result + actionable recommendation 的路线上做得好，适合 Findings 或 borderline main conference。\n\n---\n\n## A. Methods & Experiments\n\n### Strengths\n\n**S-M1** [idea] 统计方法论全面且一致。Bootstrap 95% CIs、paired permutation tests、Cohen's d 贯穿所有实验（§4 明确声明；Tables 3-7 均有 p 值和 effect size）。这在 probing 文献中属于 above-average 标准。\n\n**S-M2** [idea] CaCLR β sweep 设计充分。Table 3 跨 3 个数量级（0.001–1.0）、两种架构、20 种语言，无任何 β 值达到 p<0.05 或 d>0.2。配合 component ablation（Table 4: α 项贡献 -5pp ECE，β 项贡献 +0.001pp AUROC ≈ 0），negative result 的实验支撑完整。\n\n**S-M3** [idea] CKA 分析的诚实处理。§5.3 展示 pooled correlation r=0.52 后立即做 partial correlation controlling depth（r=0.18, p=0.11），主动将 CKA 从 \"geometric explanation\" 降级为 \"suggestive correlational analysis\"。Between-language claim（same-depth r=0.52, p=0.014, n=19）单独成立。这种 self-critical 分析方式值得肯定。\n\n**S-M4** [idea] Linear projection sample efficiency 曲线（§5.6, Table 9）提供了可操作的 practitioner guidance：~50 pairs 达 90% achievable improvement，knee 在 ~60 pairs，20 pairs 即超过 CaCLR。\n\n**S-M5** [idea] Control task analysis（§5.7, Table 10）将 Hewitt & Liang (2019) framework 系统扩展到 20 语言 × 多层，发现 ~27% 的 lang-layer 组合 selectivity < 0.05，这是一个 generalizable methodological warning。\n\n**S-M6** [idea] Mean-shift 的 rank-invariance proof 和实验验证（ΔAUROC ≡ 0）是一个干净的 baseline 排除。\n\n### Weaknesses\n\n**W-M1** [idea] **MMD 在 1-D probe logits 上操作限制了 negative result 的 scope**。§3.2 明确承认 \"a design limitation: it can only match marginal distributions of scalar outputs\"。但论文的结论（§6 Discussion \"distributional matching fails because the problem is geometric rotation\"）隐含了更广泛的 claim——即任何 distributional matching 都无法解决跨语言 probe transfer。这个推论依赖 Zhao et al. 的理论（marginal matching fails when P(Y|X) differs），但 kernel MMD 在高维空间中能 capture 的结构远多于 1-D marginals。论文未测试：(a) MMD 在 activation space（probe 之前）的效果；(b) Optimal transport / Sinkhorn 在高维空间的效果。这意味着 negative result 严格来说只关闭了 \"1-D probe output distributional matching\" 这条路，不是 \"distributional matching for cross-lingual probe transfer\" 的全部。\n- **为什么不是 Major issue**：论文的 framing 较为谨慎（§3.2 和 §6 均有 caveat），且理论论证（Zhao et al. + linear projection 成功作为 constructive evidence）在逻辑上是自洽的。但这削弱了 negative result 的 generality，从 \"distributional matching doesn't work\" 降为 \"our specific instantiation doesn't work.\"\n- **标注**: idea 层面\n\n**W-M2** [idea] **Table 1 未展示完整的 24 层 × 20 语言数据**。论文在 Qwen3 上 probe 了 24 层（§4），但 Table 1 仅呈现 L48 和 L72 两个代表层的 per-language AUROC 加上 per-language ρ。完整数据应至少在 appendix 中呈现（目前 appendix 无此内容）。Pareto frontier 的 claim 需要读者能看到完整的 depth profile。\n- **标注**: presentation 层面\n\n**W-M3** [idea] **Gemma 4 31B 数据覆盖不足**。作为第三种架构，仅出现在 Table 14（appendix 的 3 行摘要）和 §5.1 的一段文字中。没有 per-language breakdown、没有 β sweep、没有 full transfer method comparison。三架构对比的 claim 建立在 Qwen3 和 Llama4 的详细数据 + Gemma4 的摘要数据之上，不对等。\n- **标注**: idea 层面\n\n**W-M4** [idea] **Decomposition 的 IRT R²=0.40 较低**。Table 7 报告 65% combos improved（d=0.25, p=0.028）。论文诚实地将此降级为 qualitative claim，这是正确的做法。但 R²=0.40 意味着 IRT difficulty probe 只解释 40% 的 item difficulty variance，难以可靠地 \"project out\" difficulty direction——残差中仍混有大量 difficulty signal，削弱 decomposition 的 cleanness。difficulty-correctness cosine = 0.20 也确认了不完全正交。\n- **标注**: idea 层面\n\n---\n\n## B. Novelty & Related Work\n\n### Strengths\n\n**S-N1** [idea] **\"Negative result as contribution\" 的 framing 在 NLP 社区有价值**。系统地测试一个 \"看起来应该有效\" 的方法（MMD consistency regularization）并提供 principled explanation（Zhao et al. domain adaptation theory + geometric rotation）比又一个 marginal improvement 更有意义。这个 narrative choice 是论文最大的亮点。\n\n**S-N2** [idea] **Llama 4 Scout 的 language-specific Pareto 行为**（4/20 语言 ρ > 0）是一个 genuinely new observation。这不是 \"deeper = worse\" 的简单重复——而是发现某些语言在某些架构上 deeper layers transfer BETTER。这与 Qwen3 的 uniform negative ρ 形成 qualitatively different pattern，超越了 Pires et al. (2019) / Conneau et al. (2020) 的 general observation。\n\n**S-N3** [idea] **Control task artifact warning（~27%）作为独立贡献** 是 well-positioned 的。它对整个 cross-lingual probing 社区有指导意义，不限于本文的 correctness probing setting。\n\n**S-N4** [idea] **Related Work 结构合理**——§2 分 6 个子领域（Probe-Based Calibration, Cross-Lingual Probing, Cross-Lingual Alignment, Domain Adaptation Theory, Representation Similarity, Probing Methodology），每个都有恰当的 positioning。\n\n### Weaknesses\n\n**W-N1** [presentation] **14 篇引用仍低于预期**。同类 ACL/EMNLP 论文通常 30-50 篇。缺失的关键文献：\n  - IRT 基础文献（Lord 1980, Baker 2001）—— §3.3 使用 IRT 但未引用任何 psychometrics 原始文献\n  - Belinkov (2022) probing survey\n  - Keleg & Magdy (2023) multilingual calibration\n  - Guo et al. (2017) temperature scaling（论文多次提到 ECE 但未引用 calibration 的经典文献）\n  - 更多 domain adaptation theory（Ganin et al. 2016; Long et al. 2015）\n  - MoE 架构分析文献（Fedus et al. 2022; Zoph et al. 2022）\n  - 部分现有引用的作者名/标题可能仍有 accuracy issue（基于 \"best\" 版本的核查经验，median 版本的 Miao 引用格式也存疑）\n\n**W-N2** [idea] **\"First systematic study\" claim（§7 Conclusion）需要 qualification**。Civelli et al. (2025) 和 Xiao et al. (2025) 已涉及 cross-lingual probe transfer。论文 §2 中引用了它们但未充分说明自己的差异化。应改为 \"the first study systematically evaluating cross-lingual correctness probe transfer across multiple architectures with principled negative result methodology\" 或类似限定。\n\n**W-N3** [idea] **CaCLR 的 negative result novelty 取决于 MMD 在 probe outputs 上的应用是否为 \"obvious limitation\"**。§3.2 自己指出 MMD 在 1-D 上只能 match marginal distributions。如果这一点在设计时就显而易见，那么确认它确实不 work 的 surprise factor 有限。论文应讨论：是否有先前工作提出或使用过 MMD on probe outputs for cross-lingual transfer？如果没有人提出过这个方法，那 \"关闭这条路\" 的价值需要 contextualize。\n\n---\n\n## C. Overall Assessment\n\n### Major Issues\n\n**无明确的 Major Issue**。论文最大的 concern（W-M1: MMD scope, W-N3: negative result novelty）在 framing 上都有合理的 caveat。根据评分校准规则（0 Major → 可给 Strong Accept），上限为 6。\n\n### Minor Issues（按重要性排序）\n\n1. **W-M1** MMD scope 限制 negative result 的 generality（idea, moderate）\n2. **W-N1** 14 篇引用不足（presentation）\n3. **W-M3** Gemma 4 数据不对等（idea, minor-moderate）\n4. **W-N2** \"First systematic study\" overclaim（idea, minor）\n5. **W-M2** 缺完整 layer × language table（presentation）\n6. **W-M4** IRT R²=0.40 decomposition 较弱（idea, minor — paper 已自我降级）\n7. **W-N3** Negative result 的 surprise factor（idea, minor）\n\n### Narrative Self-Consistency Check\n\n| Claim | 支撑位置 | 是否自洽 | 备注 |\n|-------|---------|---------|------|\n| Architecture-dependent Pareto | Tables 1-2, 14 | ✓ | Qwen3 全负 ρ vs Llama4 4 正 vs Gemma4 最强负 |\n| CaCLR β inert | Tables 3-4 | ✓ | 3 OOM, d=0.07, p=0.38, both architectures |\n| CKA = suggestive only | Table 6 | ✓ | Pooled r=0.52 → partial r=0.18 (p=0.11) |\n| Linear proj ~50 pairs sufficient | Table 9 | ✓ | Knee ~60, 20 pairs > CaCLR |\n| Decomposition = qualitative | Table 7 | ✓ | d=0.25, 65% improved, random control d=0.05 |\n| Orthogonality persists | Table 8 | ✓ | All < 0.12, ρ=-0.58 with resource tier |\n| 27% capacity artifacts | Table 10 | ✓ | Shallow + low-resource concentrated |\n| Abstract 数字 vs 正文 | 全文 | ✓ | **无不一致**（与 \"best\" 版本形成鲜明对比）|\n\n### Experiment Coverage vs. Review Context\n\n| Plan | 覆盖 | 位置 | 备注 |\n|------|-----|------|------|\n| plan_001: Qwen3 Pareto | ✓ | Table 1, §5.1 | Table 仅摘要层，非完整 grid |\n| plan_002: Llama4 Pareto | ✓ | Table 2, §5.1 | |\n| plan_003: CaCLR | ✓ | Tables 3-5, §5.2 | 完整 β sweep + ablation + comparison |\n| plan_004: Decomposition | ✓ | Table 7, §5.4 | |\n| plan_005: Orthogonality | ✓ | Table 8, §5.5 | |\n| plan_006: Probe Complexity | ✓ | Table 11 (Appendix), §5.8 | |\n| plan_007: Benchmarks | ✓ | Table 12 (Appendix), §5.9 | |\n| plan_008: Gemma 4 | ✓ | Table 14 (Appendix), §5.1 | 数据量偏少 |\n| plan_009: Extended Coverage | ✓ | §5.9, A.6 | 52 languages, 67% viable |\n| plan_010: Quantization | ✓ | Table 13 (Appendix), §5.9 | Both architectures |\n| plan_011: CKA Analysis | ✓ | Table 6, §5.3 | partial correlation 是 key contribution |\n| plan_012: LP Sensitivity | ✓ | Table 9, §5.6 | 10-200 pairs learning curve |\n| plan_013: Control Tasks | ✓ | Table 10, §5.7 | 27% artifact finding |\n\n13/13 plans 全部覆盖。\n\n### 主要优势总结\n\n1. **Claim 校准诚实**——每个 claim 都有适当的 qualifier（\"suggestive,\" \"qualitative,\" \"principled negative result\"），无 overclaim\n2. **三段叙事逻辑连贯**——discovery → negative result → constructive recommendation，每一段都有独立的实验支撑\n3. **统计方法论在 probing 文献中 above average**——bootstrap CIs + permutation tests + Cohen's d 贯穿全文\n4. **Llama 4 Scout language-specific behavior** 是 genuinely new finding，不是已知现象的简单重复\n5. **Control task warning 是 generalizable contribution**——对整个 cross-lingual probing 社区有价值\n6. **内部一致性完美**——abstract 数字与正文完全吻合，无任何自相矛盾\n\n### 给作者的问题\n\n1. CaCLR 的 L_cons 使用 MMD 在 1-D probe logits 上。是否考虑过在高维 activation space 中做 distributional matching（如 kernel MMD on hidden states 或 optimal transport）？如果 Zhao et al. 的理论确实排除了所有 marginal matching 方法，这应该在 §6 中更明确地论证。\n2. Gemma 4 31B 是否有完整的 per-language breakdown 和 transfer method comparison？如果有，为什么不放在 appendix 中？\n3. IRT difficulty probe 的 R²=0.40——是否尝试过更复杂的 difficulty model（如 2-PL IRT 或 neural IRT）？R²=0.40 意味着 projecting out difficulty 时会引入 substantial noise。\n4. Table 1 的完整 24 层 × 20 语言数据是否可以放入 supplementary material？\n5. 论文是否有计划公开代码和 probing 数据以支持 reproducibility？（review context 提到 \"no code/data release mentioned\"）\n\n---\n\n## 评分总结\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Score | **4 (Weak Accept)** | 0 Major issues, 方法论扎实, claims 诚实, narrative 自洽; 但个体贡献偏增量, negative result 的 scope 可讨论 |\n| Confidence | **4/5** | 仔细阅读全文, 熟悉 probing/calibration/cross-lingual 文献 |\n\n**与 \"best\" 版本对比**：median 版在以下方面显著优于 best 版——(1) 内部一致性（无数字矛盾），(2) 统计方法论（有 CIs/p/d），(3) claims 校准（不 overclaim），(4) Related Work（14 vs 8 篇，有结构），(5) narrative 诚实度（承认 negative result 而非包装为 positive）。评分差距（4 vs 3）反映了这些质量差异。\n",
    "reviewer_id": "1",
    "project": "xling_calib_direction"
  }
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-21T04:32:26.174831+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3813
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-21T04:32:32.408004+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images"
  }
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-21T04:32:32.458681+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/median/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---

### Assistant

_source line 102 · 2026-05-21T04:32:40.499711+00:00_

Dream median 论文审稿完成。评分 **4 (Weak Accept)**，主要发现：

- **0 个 Major issue**——narrative 内部完全一致，无数字矛盾
- **核心亮点**：CaCLR 负面结果的实验设计扎实（β sweep 3 OOM, d=0.07, p=0.38）；CKA 分析做了 partial correlation controlling depth 后主动降级为 suggestive；统计方法论（bootstrap CIs + permutation tests + Cohen's d）贯穿全文
- **主要关切**：MMD 仅在 1-D probe logits 上测试，negative result 的 scope 被限制；Gemma 4 数据覆盖不对等；14 篇引用仍偏少
- **与 best 版本对比**：median 版在内部一致性、统计严谨性、claims 校准、narrative 诚实度上全面优于 best 版

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1"
}
```

</details>

---

## Round 4

38 recorded events

### User

_source line 103 · 2026-05-21T06:08:00.725867+00:00_

[Round 1 审稿请求]:
## Review Assignment — R1: Methods & Experiments

You are Reviewer 1, focusing on **methods and experimental rigor**.

### Paper
**Title**: "The Limits of Cross-Lingual Calibration Probe Transfer: A Large-Scale Negative Result with Methodological Implications"
**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/review_input_f5f46a62.pdf`

### Venue & Scoring
Use **ACL ARR** scoring (1-5 scale):
- **Soundness**: 5=Excellent, 4=Strong, 3=Acceptable, 2=Poor, 1=Major issues
- **Excitement**: 5=Highly Exciting, 4=Exciting, 3=Ambivalent, 2=Mediocre, 1=Not Exciting
- **Overall**: 5=Strong Accept, 4=Accept, 3=Borderline, 2=Reject, 1=Strong Reject

### Your Focus Areas
1. **Methodological soundness**: Are the experimental methods (correctness probing, CaCLR, difficulty decomposition, control tasks, linear projection, CKA analysis) properly designed and executed? Are there methodological flaws?
2. **Statistical rigor**: Are the statistical tests appropriate? Is multiple comparison correction applied? Are effect sizes reported? Are conclusions justified by the evidence?
3. **Experimental coverage**: 3 architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense), 20 languages, 5 transfer conditions, 12-24 probed layers. Is coverage sufficient? Are there critical gaps?
4. **Control experiments**: Evaluate the control task methodology (Hewitt & Liang selectivity), difficulty decomposition random-direction control, quantization validation. Are controls adequate?
5. **Reproducibility**: Implementation details, hyperparameter reporting, data availability.
6. **Limitations**: Are the stated limitations (MCQA-only, quantization bias, CaCLR kernel choice, 20-language coverage) adequate? Are there unstated limitations?

### Key Results to Scrutinize
- Pareto frontier: global ρ ranging from -0.08 to -0.22 across architectures; 14/20 non-monotonic for Qwen3
- CaCLR β sweep: monotonic degradation from Δ=-0.003 (β=0.001) to Δ=-0.019 (β=1.0)
- CaCLR component ablation: each component net negative
- Difficulty decomposition: Δ=-0.003, random control Δ=-0.005, paired p=0.42
- Simpson's Paradox: Llama partial ρ drops from +0.41 (5 langs) to +0.08 (20 langs)
- Control tasks: 42% LOW, 37% MID, 18% HIGH artifact rates; selectivity-AUROC ρ=0.68
- Linear projection: 100-200 pairs needed; effect-reversal zone [0.48, 0.68]
- Quantization: mean Δ AUROC 0.009 (Llama) to 0.012 (Qwen), increasing with depth

### Experimental Design Reference
Consult `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/review_context.yaml` for the complete imagined experiment list to judge coverage.

### Output Format
Provide your review in this structure:
```
## R1 Independent Review: Methods & Experiments

### Summary (2-3 sentences)

### Strengths (bulleted, labeled S1, S2, ...)

### Weaknesses (bulleted, labeled W1, W2, ...)

### Questions for Authors (Q1, Q2, ...)

### Minor Issues

### Scores
- Soundness: X/5
- Excitement: X/5  
- Overall: X/5
- Confidence: X/5
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 104 · 2026-05-21T06:08:14.731328+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/review_context.yaml"
  }
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-21T06:08:15.234565+00:00_

1	narrative_guidance: '原始几何洞见 framing 全面崩塌。Simpson''s Paradox 在 20 语言全量验证中双架构均不显著（Qwen
2	  partial rho=+0.11, p=0.31; Llama partial rho=+0.08, p=0.42）， CKA 在 depth 之外无额外解释力——5
3	  语言 pilot 结果被确认为 small-sample artifact。CaCLR 三个 OOM 的 β sweep 证实 consistency loss
4	  完全 inert，且几何子空间解释也不成立：correctness direction 的跨语言 persistence 远弱于预期，非 robust low-dimensional
5	  subspace。 Pareto frontier 噪声极大，20 语言中仅 2-3 个达到 per-language 显著性，non-monotonic 模式普遍存在。控制任务分析揭示问题远超预期——
6	  不仅低资源语言 artifact rate 达 42%，中资源语言也有 37% 层级组合出现 capacity artifacts，这对整个跨语言 probing
7	  文献构成方法论挑战。 Difficulty decomposition 完全无效，random-direction control 产生同量级效果。Linear
8	  projection 需要 120-180 pairs（非 50）， 且 Procrustes 效果反转阈值在语言间高度不一致，无法给出可靠的单一阈值。 新 framing
9	  路线：''The limits of cross-lingual calibration probe transfer — a large-scale negative
10	  result with methodological implications''。 三层贡献重构：(1) 控制任务发现是最强贡献——首次在 cross-lingual
11	  probing 场景系统性应用 selectivity 检验，>35% artifact rate 对整个领域有直接 implication；(2) 综合 negative
12	  result 同时关闭 distributional matching 和 geometric alignment 两条路径， 附完整 ablation 和 sweep
13	  数据；(3) 条件性实用指导——linear projection 作为唯一可行方案但需 100+ pairs， 按 resource-tier 和 baseline
14	  ZS quality 分层推荐。仍可发 EACL 作为 rigorous negative result + methodology paper。
15	
16	  '
17	imagined_experiments:
18	- name: Qwen3-235B Full Pareto Frontier
19	  plan_id: plan_001
20	  description: Qwen3-235B-A22B (94 layers, MoE, INT4), 24 probed layers (every 4th),
21	    20 languages, 5 transfer conditions
22	  expected_results:
23	    en_best_auroc: 0.738
24	    en_best_layer: 72
25	    en_auroc_range:
26	    - 0.598
27	    - 0.738
28	    en_best_ece_raw: 0.203
29	    zs_pass_count: 12
30	    zs_pass_rate: 0.6
31	    zs_pass_langs:
32	    - zh
33	    - es
34	    - fr
35	    - de
36	    - ja
37	    - pt
38	    - it
39	    - ar
40	    - hi
41	    - ru
42	    - ko
43	    - vi
44	    zs_fail_langs:
45	    - tr
46	    - th
47	    - sw
48	    - bn
49	    - am
50	    - yo
51	    - te
52	    - my
53	    best_zs_auroc
…[truncated 55970 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-21T06:08:15.538859+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/review_input_f5f46a62.pdf",
  "project": "xling_calib_direction",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/review_input_f5f46a62.pdf",
    "project": "xling_calib_direction",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-21T06:08:16.798135+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 339.6}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 341.6}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 298.0}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 311.6}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 283.2}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 225.9}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 304.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 296.1}, {\"page\": 9, \"p
…[truncated 1699 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1259
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-21T06:08:22.726965+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p1.png"
  }
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-21T06:08:23.533263+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---

### Tool call

_source line 110 · 2026-05-21T06:08:23.684803+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p2.png"
  }
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-21T06:08:24.139791+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---

### Tool call

_source line 112 · 2026-05-21T06:08:24.140252+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p3.png"
  }
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-21T06:08:24.647069+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 506
}
```

</details>

---

### Tool call

_source line 114 · 2026-05-21T06:08:24.647527+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p4.png"
  }
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-21T06:08:25.401921+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 754
}
```

</details>

---

### Tool call

_source line 116 · 2026-05-21T06:08:25.552818+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p5.png"
  }
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-21T06:08:25.907959+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p6.png"
  }
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-21T06:08:26.612621+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1059
}
```

</details>

---

### Tool result

_source line 119 · 2026-05-21T06:08:26.666139+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 758
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-21T06:08:26.666538+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p7.png"
  }
}
```

</details>

---

### Tool result

_source line 121 · 2026-05-21T06:08:27.325273+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 658
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-21T06:08:32.296837+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p8.png"
  }
}
```

</details>

---

### Tool result

_source line 123 · 2026-05-21T06:08:33.003501+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 706
}
```

</details>

---

### Tool call

_source line 124 · 2026-05-21T06:08:33.055472+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p9.png"
  }
}
```

</details>

---

### Tool call

_source line 125 · 2026-05-21T06:08:33.459104+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p10.png"
  }
}
```

</details>

---

### Tool result

_source line 126 · 2026-05-21T06:08:34.065308+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1009
}
```

</details>

---

### Tool call

_source line 127 · 2026-05-21T06:08:34.067812+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p11.png"
  }
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-21T06:08:34.874022+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1414
}
```

</details>

---

### Tool result

_source line 129 · 2026-05-21T06:08:34.876002+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 808
}
```

</details>

---

### Tool call

_source line 130 · 2026-05-21T06:08:34.876383+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p12.png"
  }
}
```

</details>

---

### Tool result

_source line 131 · 2026-05-21T06:08:35.330450+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---

### Tool call

_source line 132 · 2026-05-21T06:08:35.330828+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p13.png"
  }
}
```

</details>

---

### Tool result

_source line 133 · 2026-05-21T06:08:35.935771+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---

### Tool call

_source line 134 · 2026-05-21T06:08:35.986447+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p14.png"
  }
}
```

</details>

---

### Tool result

_source line 135 · 2026-05-21T06:08:36.038359+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 136 · 2026-05-21T06:12:21.371924+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## R1 Independent Review: Methods & Experiments\n\n### Summary (2-3 sentences)\n\nThis paper presents a large-scale negative result: cross-lingual correctness probe transfer techniques (CaCLR distributional matching, CKA geometric alignment, difficulty decomposition) that showed promise in pilot studies fail comprehensively at scale across 3 architectures and 20 languages. The paper's strongest contribution is a methodological one—applying Hewitt & Liang selectivity controls to cross-lingual probing reveals that 37-42% of mid/low-resource language-layer combinations are capacity artifacts. However, a fundamental confound undermines confidence in whether the negative results are truly fundamental limitations or artifacts of the specific experimental setup: English probe AUROC (0.715-0.742) is substantially lower than comparable work, potentially driven by INT4/W4A16 quantization and MoE routing effects, meaning all downstream negative results may reflect suboptimal probing rather than principled impossibility.\n\n### Strengths\n\n**S1** [Statistical rigor] The paper applies Bonferroni correction for multiple comparisons (§4), bootstrap 95% CIs, paired permutation tests, and Cohen's d consistently across all experiments. This is above-average for the probing literature and appropriate for a negative-result paper where false negatives must be carefully distinguished from true nulls.\n\n**S2** [CaCLR negative result is thorough] The β sweep across 3 orders of magnitude (Table 3: β=0.001→1.0) with monotonic degradation (Δ=-0.003 to Δ=-0.019), coupled with component ablation (Table 4: each component net negative) and 5-way transfer comparison (Table 5), leaves no room for \"you just didn't tune it right.\" The implementation details (Adam lr=1e-3, cosine schedule, 50 epochs, patience 10, batch 256) are sufficient for reproduction.\n\n**S3** [Control task finding is the paper's anchor] Tables 10-12 document artifact rates by resource tier (HIGH 18%, MID 37%, LOW 42%) and by depth band (LOW tier at 0-25% depth: 65-68% artifact rate). The selectivity–AUROC correlation (ρ=0.68, p<0.001) in §5.5 is the sharpest finding: it suggests that many apparently successful cross-lingual probe transfer results in the literature may be capacity artifacts. This is the first systematic application of Hewitt & Liang selectivity to cross-lingual probing and the finding generalizes beyond this paper's scope.\n\n**S4** [Simpson's Paradox validation is methodologically valuable] Table 6 shows Llama partial ρ collapsing from +0.41 (5-language pilot, p=0.006) to +0.08 (20 languages, p=0.42). This is a textbook demonstration of small-sample artifact inflation and serves as a cautionary tale for pilot studies with ≤5 languages.\n\n**S5** [Linear projection analysis is nuanced and honest] Rather than presenting linear projection as a clean solution, the paper reports the inconsistent effect-reversal zone [0.48-0.68] (Table 15), tier-dependent pair requirements (HIGH: 68, MID: 125, LOW: 182 pairs; Table 14), and the conditional nature of the recommendation (§6 Discussion). This honesty is commendable even if it weakens the practical takeaway.\n\n**S6** [Honest framing throughout] Every negative result is explicitly labeled as such: Pareto \"does not generalize\" (§5.1), CaCLR \"fails\" (§5.2), CKA \"pilot artifact confirmed\" (§5.3), decomposition \"ineffective\" (§5.4). No spin. Claims are calibrated to the evidence.\n\n**S7** [Internal consistency] All abstract numbers match body text. No contradictions between sections. Review context YAML confirms the paper faithfully reports its (imagined) experimental outcomes.\n\n### Weaknesses\n\n**W1** [MAJOR — Confound: Low English AUROC may drive all negative results] The best English probe AUROC across all architectures is 0.738 (Qwen3) / 0.715 (Llama4) / 0.742 (Gemma4). This is substantially lower than comparable work (median Dream paper achieves 0.80; best Dream paper achieves 0.843). If the English probes themselves are suboptimal—due to INT4/W4A16 quantization degrading correctness signals, MoE routing introducing layer-wise noise, or other factors—then ALL downstream negative results (no Pareto, no CaCLR benefit, no decomposition effect, no CKA predictive power) may reflect \"poor probes don't transfer well\" rather than \"cross-lingual probe transfer is fundamentally limited.\"\n\nThe paper partially acknowledges quantization (Limitation 2 in §6) but does NOT address the possibility that a better probing setup (e.g., FP16 dense models with EN AUROC ≥0.80) might produce qualitatively different results. This is the single biggest threat to the paper's core claim of \"fundamental limitations.\"\n\n**Why Major**: The paper's central thesis—that cross-lingual probe transfer is fundamentally limited—cannot be defended without ruling out that the experimental setup itself is the bottleneck. A negative result paper's value depends entirely on whether the null is informative. If the setup is suboptimal, the null says \"this setup doesn't work,\" not \"this approach doesn't work.\"\n\n**W2** [MAJOR — Quantization confound at deep layers is unresolved] Table 22 shows quantization introduces depth-dependent bias: Llama W4A16 Δ ranges from -0.003 (20% depth) to -0.018 (95% depth); Qwen INT4 Δ ranges from -0.005 to -0.022. Rank preservation fails at ≥60-80% depth on both models. This creates a direct confound with the Pareto frontier analysis (§5.1): the non-monotonic patterns attributed to \"MoE routing effects\" (14/20 non-monotonic on Qwen3) may partly arise from layer-dependent quantization artifacts. The paper observes that \"the Pareto frontier is noisy\" but does not disentangle how much noise comes from architecture vs. quantization.\n\n**Why Major**: Deep-layer probe results (including EN-optimal AUROC, which determines all transfer comparisons) are systematically biased by quantization. The 1-2pp bias at deep layers is large enough to shift conclusions when effect sizes are small (CaCLR Δ=-0.010; decomposition Δ=-0.003).\n\n**W3** [Difficulty decomposition failure may reflect probe quality, not absent phenomenon] The IRT difficulty probe achieves only R²=0.31 (Table 9 context). This means the \"difficulty direction\" captures less than a third of actual difficulty variance, and \"projecting it out\" removes a noisy estimate rather than a clean signal. The random-direction control producing an indistinguishable effect (Δ=-0.005 vs Δ=-0.003, p=0.42) is consistent with BOTH interpretations: (a) there is no difficulty-capability decomposition (the paper's conclusion), or (b) the difficulty probe is too poor to test the hypothesis. The paper does not discuss whether a higher-quality difficulty probe (R²≥0.50) would change the result.\n\n**W4** [Llama 4 Scout underpowered for per-language analysis] With only 12 probed layers (every 4th of 48), per-language Spearman tests have n=12, yielding statistical power of ~0.35-0.50 for detecting ρ=-0.40 at α=0.05. The paper correctly notes 0/20 languages reach significance (Table 2), but this is expected given the power analysis, not evidence against the Pareto effect. The paper should report post-hoc power analysis.\n\n**W5** [The \"effect reversal zone\" for linear projection is so wide as to be unhelpful] Table 15 shows the reversal zone spans ZS AUROC [0.48, 0.68]. Since 16/20 languages have ZS AUROC in this range (review context), the conditional recommendation in §6 (\"if ZS < 0.50, linear proj likely helps\") applies to only ~4/20 languages. For the vast majority of languages, the paper's own analysis says the outcome is \"unpredictable without held-out validation,\" making the practical recommendation nearly vacuous.\n\n**W6** [No dense model at comparable scale creates architecture-scale confound] Gemma 4 31B (31B dense) is compared against Qwen3-235B (235B MoE) and Llama 4 Scout (109B MoE, 17B active). The finding that \"dense shows clearer Pareto than MoE\" (§5.1) cannot distinguish architecture effect from scale/quantization effect: Gemma runs in FP16, the MoE models use INT4/W4A16. A FP16 dense model at 7B (as in the pilot) vs. INT4 MoE at 235B is an apples-to-oranges comparison.\n\n**W7** [Orthogonality section (§5.9) contributes nothing actionable] Architecture agreement is only 65% (Table 23: 7/20 disagreements). The section's own conclusion acknowledges this is \"unreliable for low-resource languages where probe validity itself is questionable\" (§5.5 back-reference). This circular dependency (artifacts → unreliable probes → unreliable orthogonality) means the section has no standalone conclusion. Should be cut or relegated to appendix.\n\n**W8** [Reference count still below expectations] ~15-17 references for a paper spanning probing, calibration, IRT, cross-lingual alignment, domain adaptation, and control tasks. Missing: IRT foundational literature (Lord 1980; Baker 2001), Belinkov (2022) probing survey, Guo et al. (2017) temperature scaling, additional domain adaptation theory (Ganin et al. 2016).\n\n### Questions for Authors\n\n**Q1** [Critical] The best English probe AUROC is 0.738 (Qwen3-235B). Comparable work achieves 0.80+. Have you tested whether running the same probing pipeline on a FP16 dense model (e.g., Llama-3.1-8B or Qwen2.5-7B used in pilot) achieves ≥0.80? If so, the negative results may be specific to quantized MoE setups, not to cross-lingual probe transfer in general. If not tested, this is a critical missing control.\n\n**Q2** For the difficulty decomposition (§5.4), the IRT probe R²=0.31 is quite low. Have you tried more expressive difficulty models (2-PL IRT, neural IRT)? The null result may reflect poor difficulty estimation, not the absence of a difficulty-capability decomposition.\n\n**Q3** How much of Qwen3's 14/20 non-monotonic pattern survives after correcting for quantization bias? Table 22 shows INT4 introduces up to -0.022 Δ at deep layers. If corrected, do any non-monotonic languages become monotonically negative?\n\n**Q4** The selectivity-AUROC correlation (ρ=0.68) could be confounded by a common cause: probe training data size. Languages with more parallel data have both higher selectivity AND higher AUROC because the probe trains better. Have you controlled for training set size?\n\n**Q5** Linear projection requires 100-200 parallel pairs. For the low-resource languages where it's most needed (am, yo, my), do parallel corpora of this size even exist? If not, the practical recommendation is moot for the languages it would help most.\n\n**Q6** Table 5 shows CaCLR win rate vs. zero-shot is 18%. Are these wins concentrated in specific language-tier × depth combinations? If CaCLR helps for certain high-resource languages at certain depths, this would qualify the \"comprehensive failure\" narrative.\n\n### Minor Issues\n\n- Table 1 reports only hi (p=0.041) as significant, but with Bonferroni correction for 20 languages, the threshold is 0.0025, not 0.05. After correction, 0/20 are significant on Qwen3. The text should clarify whether per-language p-values are raw or corrected.\n- §5.1 states \"0-1 show a significant global Pareto frontier\" but Gemma's p=0.045 is marginally significant without correction. With 3 architecture-level tests, Bonferroni threshold is ~0.017. Should clarify.\n- Table 3 (CaCLR β sweep) is shown at \"50% depth, 20 langs mean\" — should show results at EN-optimal layer too, since that's where the comparison in Table 5 is made.\n- Some table numbering appears to skip (Tables 1-11 in main text, then Tables 12-23 mixing main text and appendix). Should be reorganized.\n- The paper claims \"first large-scale study\" (§1) but should acknowledge Civelli et al. (2025) and Xiao et al. (2025) explicitly in the claim.\n\n### Scores\n\n- **Soundness**: 3/5 — Methodology is thorough (sweeps, ablations, controls) but two unresolved confounds (low EN AUROC across all models; depth-dependent quantization bias) undermine confidence that negative results are fundamental rather than setup-specific.\n- **Excitement**: 2/5 — The control task finding (§5.5) is genuinely important for the field. But the remaining content is a collection of null results without a compelling resolution: the paper closes doors but doesn't open new ones. The practical recommendation (linear projection) is too conditional to be actionable.\n- **Overall**: 2/5 — The paper's core thesis (\"cross-lingual calibration probe transfer is fundamentally limited\") is not adequately supported because the experimental setup itself may be the bottleneck (EN AUROC 0.715-0.742, quantization confound). The control task finding alone is a Findings-level contribution if extracted and focused. As currently framed—claiming to demonstrate fundamental limits via a potentially flawed setup—the paper overclaims despite its honest tone.\n- **Confidence**: 4/5 — I have read the paper carefully and am familiar with the probing, calibration, and cross-lingual transfer literature. Main uncertainty: whether the \"worst-tier\" EN AUROC values are realistic or artificially suppressed by the simulation setup.\n",
  "reviewer_id": "1",
  "project": "xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## R1 Independent Review: Methods & Experiments\n\n### Summary (2-3 sentences)\n\nThis paper presents a large-scale negative result: cross-lingual correctness probe transfer techniques (CaCLR distributional matching, CKA geometric alignment, difficulty decomposition) that showed promise in pilot studies fail comprehensively at scale across 3 architectures and 20 languages. The paper's strongest contribution is a methodological one—applying Hewitt & Liang selectivity controls to cross-lingual probing reveals that 37-42% of mid/low-resource language-layer combinations are capacity artifacts. However, a fundamental confound undermines confidence in whether the negative results are truly fundamental limitations or artifacts of the specific experimental setup: English probe AUROC (0.715-0.742) is substantially lower than comparable work, potentially driven by INT4/W4A16 quantization and MoE routing effects, meaning all downstream negative results may reflect suboptimal probing rather than principled impossibility.\n\n### Strengths\n\n**S1** [Statistical rigor] The paper applies Bonferroni correction for multiple comparisons (§4), bootstrap 95% CIs, paired permutation tests, and Cohen's d consistently across all experiments. This is above-average for the probing literature and appropriate for a negative-result paper where false negatives must be carefully distinguished from true nulls.\n\n**S2** [CaCLR negative result is thorough] The β sweep across 3 orders of magnitude (Table 3: β=0.001→1.0) with monotonic degradation (Δ=-0.003 to Δ=-0.019), coupled with component ablation (Table 4: each component net negative) and 5-way transfer comparison (Table 5), leaves no room for \"you just didn't tune it right.\" The implementation details (Adam lr=1e-3, cosine schedule, 50 epochs, patience 10, batch 256) are sufficient for reproduction.\n\n**S3** [Control task finding is the paper's anchor] Tables 10-12 document artifact rates by resource tier (HIGH 18%, MID 37%, LOW 42%) and by depth band (LOW tier at 0-25% depth: 65-68% artifact rate). The selectivity–AUROC correlation (ρ=0.68, p<0.001) in §5.5 is the sharpest finding: it suggests that many apparently successful cross-lingual probe transfer results in the literature may be capacity artifacts. This is the first systematic application of Hewitt & Liang selectivity to cross-lingual probing and the finding generalizes beyond this paper's scope.\n\n**S4** [Simpson's Paradox validation is methodologically valuable] Table 6 shows Llama partial ρ collapsing from +0.41 (5-language pilot, p=0.006) to +0.08 (20 languages, p=0.42). This is a textbook demonstration of small-sample artifact inflation and serves as a cautionary tale for pilot studies with ≤5 languages.\n\n**S5** [Linear projection analysis is nuanced and honest] Rather than presenting linear projection as a clean solution, the paper reports the inconsistent effect-reversal zone [0.48-0.68] (Table 15), tier-dependent pair requirements (HIGH: 68, MID: 125, LOW: 182 pairs; Table 14), and the conditional nature of the recommendation (§6 Discussion). This honesty is commendable even if it weakens the practical takeaway.\n\n**S6** [Honest framing throughout] Every negative result is explicitly labeled as such: Pareto \"does not generalize\" (§5.1), CaCLR \"fails\" (§5.2), CKA \"pilot artifact confirmed\" (§5.3), decomposition \"ineffective\" (§5.4). No spin. Claims are calibrated to the evidence.\n\n**S7** [Internal consistency] All abstract numbers match body text. No contradictions between sections. Review context YAML confirms the paper faithfully reports its (imagined) experimental outcomes.\n\n### Weaknesses\n\n**W1** [MAJOR — Confound: Low English AUROC may drive all negative results] The best English probe AUROC across all architectures is 0.738 (Qwen3) / 0.715 (Llama4) / 0.742 (Gemma4). This is substantially lower than comparable work (median Dream paper achieves 0.80; best Dream paper achieves 0.843). If the English probes themselves are suboptimal—due to INT4/W4A16 quantization degrading correctness signals, MoE routing introducing layer-wise noise, or other factors—then ALL downstream negative results (no Pareto, no CaCLR benefit, no decomposition effect, no CKA predictive power) may reflect \"poor probes don't transfer well\" rather than \"cross-lingual probe transfer is fundamentally limited.\"\n\nThe paper partially acknowledges quantization (Limitation 2 in §6) but does NOT address the possibility that a better probing setup (e.g., FP16 dense models with EN AUROC ≥0.80) might produce qualitatively different results. This is the single biggest threat to the paper's core claim of \"fundamental limitations.\"\n\n**Why Major**: The paper's central thesis—that cross-lingual probe transfer is fundamentally limited—cannot be defended without ruling out that the experimental setup itself is the bottleneck. A negative result paper's value depends entirely on whether the null is informative. If the setup is suboptimal, the null says \"this setup doesn't work,\" not \"this approach doesn't work.\"\n\n**W2** [MAJOR — Quantization confound at deep layers is unresolved] Table 22 shows quantization introduces depth-dependent bias: Llama W4A16 Δ ranges from -0.003 (20% depth) to -0.018 (95% depth); Qwen INT4 Δ ranges from -0.005 to -0.022. Rank preservation fails at ≥60-80% depth on both models. This creates a direct confound with the Pareto frontier analysis (§5.1): the non-monotonic patterns attributed to \"MoE routing effects\" (14/20 non-monotonic on Qwen3) may partly arise from layer-dependent quantization artifacts. The paper observes that \"the Pareto frontier is noisy\" but does not disentangle how much noise comes from architecture vs. quantization.\n\n**Why Major**: Deep-layer probe results (including EN-optimal AUROC, which determines all transfer comparisons) are systematically biased by quantization. The 1-2pp bias at deep layers is large enough to shift conclusions when effect sizes are small (CaCLR Δ=-0.010; decomposition Δ=-0.003).\n\n**W3** [Difficulty decomposition failure may reflect probe quality, not absent phenomenon] The IRT difficulty probe achieves only R²=0.31 (Table 9 context). This means the \"difficulty direction\" captures less than a third of actual difficulty variance, and \"projecting it out\" removes a noisy estimate rather than a clean signal. The random-direction control producing an indistinguishable effect (Δ=-0.005 vs Δ=-0.003, p=0.42) is consistent with BOTH interpretations: (a) there is no difficulty-capability decomposition (the paper's conclusion), or (b) the difficulty probe is too poor to test the hypothesis. The paper does not discuss whether a higher-quality difficulty probe (R²≥0.50) would change the result.\n\n**W4** [Llama 4 Scout underpowered for per-language analysis] With only 12 probed layers (every 4th of 48), per-language Spearman tests have n=12, yielding statistical power of ~0.35-0.50 for detecting ρ=-0.40 at α=0.05. The paper correctly notes 0/20 languages reach significance (Table 2), but this is expected given the power analysis, not evidence against the Pareto effect. The paper should report post-hoc power analysis.\n\n**W5** [The \"effect reversal zone\" for linear projection is so wide as to be unhelpful] Table 15 shows the reversal zone spans ZS AUROC [0.48, 0.68]. Since 16/20 languages have ZS AUROC in this range (review context), the conditional recommendation in §6 (\"if ZS < 0.50, linear proj likely helps\") applies to only ~4/20 languages. For the vast majority of languages, the paper's own analysis says the outcome is \"unpredictable without held-out validation,\" making the practical recommendation nearly vacuous.\n\n**W6** [No dense model at comparable scale creates architecture-scale confound] Gemma 4 31B (31B dense) is compared against Qwen3-235B (235B MoE) and Llama 4 Scout (109B MoE, 17B active). The finding that \"dense shows clearer Pareto than MoE\" (§5.1) cannot distinguish architecture effect from scale/quantization effect: Gemma runs in FP16, the MoE models use INT4/W4A16. A FP16 dense model at 7B (as in the pilot) vs. INT4 MoE at 235B is an apples-to-oranges comparison.\n\n**W7** [Orthogonality section (§5.9) contributes nothing actionable] Architecture agreement is only 65% (Table 23: 7/20 disagreements). The section's own conclusion acknowledges this is \"unreliable for low-resource languages where probe validity itself is questionable\" (§5.5 back-reference). This circular dependency (artifacts → unreliable probes → unreliable orthogonality) means the section has no standalone conclusion. Should be cut or relegated to appendix.\n\n**W8** [Reference count still below expectations] ~15-17 references for a paper spanning probing, calibration, IRT, cross-lingual alignment, domain adaptation, and control tasks. Missing: IRT foundational literature (Lord 1980; Baker 2001), Belinkov (2022) probing survey, Guo et al. (2017) temperature scaling, additional domain adaptation theory (Ganin et al. 2016).\n\n### Questions for Authors\n\n**Q1** [Critical] The best English probe AUROC is 0.738 (Qwen3-235B). Comparable work achieves 0.80+. Have you tested whether running the same probing pipeline on a FP16 dense model (e.g., Llama-3.1-8B or Qwen2.5-7B used in pilot) achieves ≥0.80? If so, the negative results may be specific to quantized MoE setups, not to cross-lingual probe transfer in general. If not tested, this is a critical missing control.\n\n**Q2** For the difficulty decomposition (§5.4), the IRT probe R²=0.31 is quite low. Have you tried more expressive difficulty models (2-PL IRT, neural IRT)? The null result may reflect poor difficulty estimation, not the absence of a difficulty-capability decomposition.\n\n**Q3** How much of Qwen3's 14/20 non-monotonic pattern survives after correcting for quantization bias? Table 22 shows INT4 introduces up to -0.022 Δ at deep layers. If corrected, do any non-monotonic languages become monotonically negative?\n\n**Q4** The selectivity-AUROC correlation (ρ=0.68) could be confounded by a common cause: probe training data size. Languages with more parallel data have both higher selectivity AND higher AUROC because the probe trains better. Have you controlled for training set size?\n\n**Q5** Linear projection requires 100-200 parallel pairs. For the low-resource languages where it's most needed (am, yo, my), do parallel corpora of this size even exist? If not, the practical recommendation is moot for the languages it would help most.\n\n**Q6** Table 5 shows CaCLR win rate vs. zero-shot is 18%. Are these wins concentrated in specific language-tier × depth combinations? If CaCLR helps for certain high-resource languages at certain depths, this would qualify the \"comprehensive failure\" narrative.\n\n### Minor Issues\n\n- Table 1 reports only hi (p=0.041) as significant, but with Bonferroni correction for 20 languages, the threshold is 0.0025, not 0.05. After correction, 0/20 are significant on Qwen3. The text should clarify whether per-language p-values are raw or corrected.\n- §5.1 states \"0-1 show a significant global Pareto frontier\" but Gemma's p=0.045 is marginally significant without correction. With 3 architecture-level tests, Bonferroni threshold is ~0.017. Should clarify.\n- Table 3 (CaCLR β sweep) is shown at \"50% depth, 20 langs mean\" — should show results at EN-optimal layer too, since that's where the comparison in Table 5 is made.\n- Some table numbering appears to skip (Tables 1-11 in main text, then Tables 12-23 mixing main text and appendix). Should be reorganized.\n- The paper claims \"first large-scale study\" (§1) but should acknowledge Civelli et al. (2025) and Xiao et al. (2025) explicitly in the claim.\n\n### Scores\n\n- **Soundness**: 3/5 — Methodology is thorough (sweeps, ablations, controls) but two unresolved confounds (low EN AUROC across all models; depth-dependent quantization bias) undermine confidence that negative results are fundamental rather than setup-specific.\n- **Excitement**: 2/5 — The control task finding (§5.5) is genuinely important for the field. But the remaining content is a collection of null results without a compelling resolution: the paper closes doors but doesn't open new ones. The practical recommendation (linear projection) is too conditional to be actionable.\n- **Overall**: 2/5 — The paper's core thesis (\"cross-lingual calibration probe transfer is fundamentally limited\") is not adequately supported because the experimental setup itself may be the bottleneck (EN AUROC 0.715-0.742, quantization confound). The control task finding alone is a Findings-level contribution if extracted and focused. As currently framed—claiming to demonstrate fundamental limits via a potentially flawed setup—the paper overclaims despite its honest tone.\n- **Confidence**: 4/5 — I have read the paper carefully and am familiar with the probing, calibration, and cross-lingual transfer literature. Main uncertainty: whether the \"worst-tier\" EN AUROC values are realistic or artificially suppressed by the simulation setup.\n",
    "reviewer_id": "1",
    "project": "xling_calib_direction"
  }
}
```

</details>

---

### Tool result

_source line 137 · 2026-05-21T06:12:25.899339+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4527
}
```

</details>

---

### Tool call

_source line 138 · 2026-05-21T06:12:32.445157+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images"
  }
}
```

</details>

---

### Tool result

_source line 139 · 2026-05-21T06:12:32.445684+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 140 · 2026-05-21T06:12:40.363394+00:00_

审稿报告已提交。

评分摘要：Soundness 3/5, Excitement 2/5, Overall 2/5 (Reject), Confidence 4/5。核心问题是两个 Major weaknesses：(1) 全部模型的英语 probe AUROC 仅 0.715-0.742，远低于同类工作的 0.80+，所有负面结果可能反映的是 probing setup 的局限而非方法论的根本限制；(2) 深层 INT4/W4A16 量化引入 1-2pp 的系统性偏差，直接干扰 Pareto frontier 和 CaCLR 的分析。控制任务发现（37-42% artifact rate）是论文最有价值的贡献，可单独作为 Findings 级别工作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1"
}
```

</details>

---

## Round 5

4 recorded events

### User

_source line 141 · 2026-05-21T06:12:41.593636+00:00_

[Round 1 审稿请求]:
## 交叉审阅任务（Median Paper）

以下是 **Reviewer 2（Novelty & Related Work）** 的完整 Round 1 审稿意见。请逐条回应其 Weaknesses：

- **[AGREE]**：同意，并补充你从 Methods/Experiments 角度的佐证
- **[REBUT]**：不同意或有保留意见，提供具体证据（cite Section/Table）

特别关注：
1. R2-W1（引用不足 + References section 可能缺失）——你的审稿中也提到 14 篇引用偏少，是否同意 References section 可能丢失？
2. R2-W3（CaCLR 方法失败导致论文只剩两个贡献）——你认为 negative result 本身是否构成独立贡献？
3. R2-W6（linear projection "only viable path" 与 Table 21 的张力）——从实验角度评估这个 claim 是否过强

---

## Reviewer 2 完整审稿原文

**Overall**: 3/5 (Borderline / Findings)

### Strengths
- **S1**: Control task methodology（Hewitt & Liang → 跨语言 probing，42% artifact rate）是最强新颖性贡献
- **S2**: 诚实的负面结果 framing，Abstract 开门见山 "predominantly negative"
- **S3**: 统计严谨性显著进步——Bonferroni、Spearman+p值、SDs、control task selectivity 阈值
- **S4**: Simpson's Paradox falsification 是教科书级案例
- **S5**: 三档决策规则（§9）对实践者有直接价值
- **S6**: Related Work 覆盖 5 个子方向，比 best 版本好得多

### Weaknesses
**W1** [warning] 参考文献仍不够充分——缺 Conneau et al. (2020)、Pires et al. (2019)、Belinkov (2022) survey、Keleg & Magdy (2023)、Guo et al. (2017) temperature scaling。**且 PDF 中 §7 后直接是 Appendix A，未见 References section——如果参考文献列表因排版丢失，这是严重格式问题。**

**W2** [warning] 23 张表格 + 0 张图。核心负面结论（no Pareto frontier、CaCLR harmful、Simpson's Paradox）极适合可视化。Scatter plot、selectivity heatmap、分组 scatter（Simpson's Paradox）都比表格更有说服力。

**W3** [minor] CaCLR 失败使方法贡献难以独立评价——论文实质只剩 (1) control task 方法论 (2) 负面实验结果。对 main conference 可能不够，Findings track 可接受。

**W4** [minor] Pilot 区分不充分——"pilot studies on Qwen2.5-7B and Llama-3.1-8B" 未说明是已发表还是未发表前期工作。

**W5** [minor] Difficulty decomposition 的负面结论太快——§5.4 一段话否定，未分析为什么在大模型上失败（scale? 数据? 量化?）

**W6** [minor] "Only viable path" 结论与 Table 21 存在张力——Linear Proj 200 pairs Sig. impr. 11/20，few-shot 100 为 13/20，差异不大。

### Questions
Q1-Q6 涵盖：Simpson's Paradox partial ρ 的控制变量、selectivity 阈值敏感性、scale vs architecture 作为结论翻转原因、是否测试过其他 distributional matching 方法、▲ 标记语言的含义、References section 位置。

### Scores
- Soundness: 3.5/5 | Excitement: 3/5 | Overall: 3/5 | Confidence: 4/5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 142 · 2026-05-21T06:14:06.176904+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 对 Reviewer 2 (Median Paper, Round 1) 的交叉回应\n\n---\n\n## 逐条回应 R2 Weaknesses\n\n### [AGREE，附补充] R2-W1: 参考文献不足 + References section 可能丢失\n\n完全同意引用不足的判断。我在独立审稿中同样指出约 14 篇引用对这个范围的论文而言偏少（我的 W-N1）。R2 列出的缺失引用（Conneau et al. 2020, Pires et al. 2019, Belinkov 2022, Keleg & Magdy 2023, Guo et al. 2017）我全部认同。\n\n**关于 References section 是否丢失**：这是一个重要的观察。我在阅读 PDF 时注意到 §7 Conclusion 之后（page 10 底部）确实有 References section——page 10 下半部分列出了参考文献（Angelopoulos and Bates 2023, Artetxe et al. 2018, Ben-David et al. 2010, Conneau et al. 2018, Hewitt and Liang 2019, Kornblith et al. 2019 等），延续到 page 11 上部。所以 **References section 存在但可能因排版紧凑而不够醒目**。R2 可能漏看了——这本身说明论文的 typographical layout 需要改善（References 应有更清晰的分隔）。\n\n不过，即便 References section 存在，引用数量（约 15-17 篇）仍然不足。特别是：\n- §3.4 使用 IRT difficulty probes 但未引用任何 psychometrics/IRT 基础文献\n- §3.2 讨论 calibration (ECE) 但未引用 Guo et al. (2017) temperature scaling\n- §5.3 使用 CKA 但仅引用 Kornblith et al. (2019)，缺 SVCCA 以外的 representation similarity 文献\n\n---\n\n### [AGREE] R2-W2: 23 张表格 + 0 张图\n\n完全同意，这与我之前审阅 \"best\" 版本时指出的问题一致。对于这篇 median 论文尤其如此——核心负面结论非常适合可视化：\n\n1. **Pareto frontier**：Table 1 的 per-language ρ 和 Table 2 的架构对比 → scatter plot（EN AUROC vs ZS AUROC, 按语言/架构着色）会直观展示 \"diffuse cloud\" vs \"clean frontier\" 的架构差异\n2. **CaCLR β sweep**：Table 3 的 monotonic degradation → 折线图 + CI shaded area 比 4 行数字更有冲击力\n3. **Simpson's Paradox**：Table 6 → 5-lang pilot vs 20-lang full 的 paired scatter 最能展示 artifact inflation\n4. **Control task selectivity**：Table 10/11 → language × layer heatmap（按 selectivity 着色）是这篇论文最有说服力的潜在图表\n5. **Linear projection saturation curve**：Table 13 → learning curve plot（pairs vs AUROC）是标准呈现方式\n\n从 methods 角度，表格呈现要求读者自行 mental visualization，增加了审稿负担。\n\n---\n\n### [REBUT（部分）] R2-W3: CaCLR 失败使论文只剩两个贡献\n\nR2 认为 CaCLR 失败意味着论文实质只剩 (1) control task 方法论 (2) 负面实验结果，对 main conference 不够。我 **部分不同意**，理由如下：\n\n**CaCLR 的 systematic negative result 本身构成独立贡献**，前提是实验设计足够彻底——而本文确实做到了：\n- β sweep 跨 3 OOM（Table 3），每个 β 值有 per-language breakdown\n- Component ablation（Table 4）清楚分离了 α (SB-ECE) 和 β (MMD) 的各自效果\n- 理论解释链：1-D MMD limitation → Zhao et al. (2019) conditional distribution mismatch → linear projection 作为 constructive alternative\n- 两个架构上一致复现\n\n在 NLP 社区中，well-executed negative results 有独立的出版价值（见 Rogers et al. 2020 \"A Primer in BERTology\" 对 negative probing results 的讨论）。关键在于 negative result 是否 **informative**——即它是否关闭了一条合理的研究路径并解释了为什么。本文在这方面做得不错。\n\n**但我同意 R2 的实质判断**：对 main conference 而言，\"thorough negative result\" + \"control task finding\" 两个贡献的 excitement 可能不够。我在独立审稿中给出 Overall 4/5 (Weak Accept) 也是基于类似考量。对于一篇 Findings paper，这个 package 足够了。\n\n**从 Methods 角度的补充**：CaCLR 负面结果的一个根本局限是 MMD 只在 1-D probe logits 上操作（§3.2 明确承认）。论文未测试 activation-space MMD 或 optimal transport 等替代方案。如果未来工作在高维空间做 distributional matching 成功了，这篇论文的 \"closing the path\" claim 就被限定为 \"closing the 1-D path\"。但作为当前 contribution，thoroughness 本身有价值。\n\n---\n\n### [AGREE] R2-W4: Pilot 区分不充分\n\n同意。论文多次提到 \"pilot studies on Qwen2.5-7B and Llama-3.1-8B\" 但未说明：\n- 这些 pilot 是否有独立出版物\n- 如果未出版，pilot 数据是否包含在当前论文的 supplementary 中\n- 具体 pilot 实验的规模和设置\n\n从 methods 角度，这尤其影响 §5.3 的 Simpson's Paradox analysis（Table 6），因为该分析的核心逻辑是 \"pilot 的 5 语言结果是 artifact\"——读者需要能独立验证 pilot 的具体设置和结果。\n\n---\n\n### [AGREE，附重要补充] R2-W5: Difficulty decomposition 负面结论太快\n\n完全同意。这与我独立审稿中的 W-M4 高度一致。\n\n§5.4 仅用一段否定 decomposition，核心数据是 Table 9：Δ=-0.003 vs random Δ=-0.005, p=0.42。但论文 **未讨论** 以下关键因素：\n\n1. **IRT R²=0.31 是根本问题**。如果 difficulty probe 只捕获 31% 的 difficulty variance，那么 \"projecting out difficulty\" 实际上投影的是一个噪声方向。Random-direction control 产生同量级效果恰恰与此一致——两种投影都在做 noisy dimensionality reduction。论文应讨论：R²≥0.50 的 difficulty probe 是否会改变结论。\n\n2. **Scale 效应**。Pilot 在 7B dense 模型上可能有更 linear/concentrated 的 difficulty encoding（representation 更简单）。235B MoE 的 representation 可能更 distributed/nonlinear，使 linear IRT probe 失效。论文应对比不同 scale 的 difficulty probe R²。\n\n3. **量化效应**。INT4 量化可能 selectively 损伤 difficulty signal（如果 difficulty 信号集中在低方差维度，4-bit 量化会 disproportionately 影响它）。\n\n一段话的否定不足以关闭 decomposition 路径。至少需要一个 supplementary section 分析失败原因。\n\n---\n\n### [AGREE，附重要修正] R2-W6: \"Only viable path\" 与 Table 21 的张力\n\nR2 正确指出了一个重要张力。让我从 experiments 角度详细分析。\n\n**Table 21（Appendix, page 13，即 Table 5 在 appendix 中的完整版）：**\n\n| Condition | Mean AUROC | Δ vs ZS | Sig. impr. count |\n|-----------|-----------|---------|-----------------|\n| Zero-shot | .572 | — | — |\n| Mean-shift | .572 | .000 | 0/20 |\n| LinProj 200 | .610 | +.038 | 11/20 |\n| Few-shot 25 | .594 | +.022 | 7/20 |\n| Few-shot 100 | .623 | +.051 | 13/20 |\n\n**关键观察**：Few-shot 100 的 AUROC (.623) 和 Sig. impr. count (13/20) 都高于 Linear Proj 200 (.610, 11/20)。论文声称 linear projection 是 \"the only viable transfer method\"（§1 Abstract, §5.6 标题），但 **few-shot 100 按多数指标优于 linear projection**。\n\n论文对此的隐含辩护是：few-shot 需要 target-language correctness labels，而 linear projection 只需要 parallel data（无需 labels）。这个 distinction 是合理的——但论文 **没有明确地做出这个区分**。\"Only viable path\" 的措辞暗示 linear projection 是唯一有效的方法，但 few-shot 100 明显更有效。\n\n**建议修正**：论文应将 claim 改为 \"the only viable **label-free** transfer method\" 或 \"the only viable transfer method that does not require target-language correctness labels\"。当前措辞对读者有误导。\n\n此外，从 practical 角度：如果一个 practitioner 已经有 100 条 target-language labeled data，few-shot 直接优于 linear projection。Linear projection 的优势仅在 zero-label scenario，而该 scenario 仍需 100-200 parallel pairs——获取 parallel data 的难度与获取 labeled data 的难度在低资源语言中可能相当。论文应讨论这个 practical trade-off。\n\n---\n\n## 总结\n\n| R2 Issue | 我的判断 | 关键理由 |\n|----------|---------|---------|\n| W1 (引用不足/References 丢失) | AGREE（附修正：References section 存在但不醒目） | ~15 篇引用不足；缺 IRT/calibration/probing survey 基础文献 |\n| W2 (23 表 0 图) | AGREE | 核心负面结论极适合可视化 |\n| W3 (CaCLR 失败 → 只剩两个贡献) | 部分 REBUT | Systematic negative result 本身有价值（if well-executed），但同意对 main conference excitement 不足 |\n| W4 (pilot 区分不充分) | AGREE | 影响 Simpson's Paradox 验证的可信度 |\n| W5 (decomposition 否定太快) | AGREE（强烈） | IRT R²=0.31 是根本问题；需分析失败原因而非直接否定路径 |\n| W6 (\"Only viable path\" 过强) | AGREE（附具体证据） | Few-shot 100 在 AUROC (.623 vs .610) 和 sig. count (13/20 vs 11/20) 上均优于 LinProj 200 |\n\n**评分微调**：在阅读 R2 的审稿后，我认为 R2-W6 的观点有力地削弱了论文的 practical recommendation 部分。结合 R2-W5（decomposition 否定太快），论文的两个非 control-task 贡献（negative result narrative + practical recommendation）都有明显的 overclaim。我维持 **Overall 4/5 (Weak Accept)**，因为 control task contribution + statistical rigor + honest framing 仍然有价值，但更倾向于 Findings track。R2 给 3/5 (Borderline)，差异主要在于我对 negative result 的独立价值评估略高。\n",
  "reviewer_id": "1",
  "project": "xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 对 Reviewer 2 (Median Paper, Round 1) 的交叉回应\n\n---\n\n## 逐条回应 R2 Weaknesses\n\n### [AGREE，附补充] R2-W1: 参考文献不足 + References section 可能丢失\n\n完全同意引用不足的判断。我在独立审稿中同样指出约 14 篇引用对这个范围的论文而言偏少（我的 W-N1）。R2 列出的缺失引用（Conneau et al. 2020, Pires et al. 2019, Belinkov 2022, Keleg & Magdy 2023, Guo et al. 2017）我全部认同。\n\n**关于 References section 是否丢失**：这是一个重要的观察。我在阅读 PDF 时注意到 §7 Conclusion 之后（page 10 底部）确实有 References section——page 10 下半部分列出了参考文献（Angelopoulos and Bates 2023, Artetxe et al. 2018, Ben-David et al. 2010, Conneau et al. 2018, Hewitt and Liang 2019, Kornblith et al. 2019 等），延续到 page 11 上部。所以 **References section 存在但可能因排版紧凑而不够醒目**。R2 可能漏看了——这本身说明论文的 typographical layout 需要改善（References 应有更清晰的分隔）。\n\n不过，即便 References section 存在，引用数量（约 15-17 篇）仍然不足。特别是：\n- §3.4 使用 IRT difficulty probes 但未引用任何 psychometrics/IRT 基础文献\n- §3.2 讨论 calibration (ECE) 但未引用 Guo et al. (2017) temperature scaling\n- §5.3 使用 CKA 但仅引用 Kornblith et al. (2019)，缺 SVCCA 以外的 representation similarity 文献\n\n---\n\n### [AGREE] R2-W2: 23 张表格 + 0 张图\n\n完全同意，这与我之前审阅 \"best\" 版本时指出的问题一致。对于这篇 median 论文尤其如此——核心负面结论非常适合可视化：\n\n1. **Pareto frontier**：Table 1 的 per-language ρ 和 Table 2 的架构对比 → scatter plot（EN AUROC vs ZS AUROC, 按语言/架构着色）会直观展示 \"diffuse cloud\" vs \"clean frontier\" 的架构差异\n2. **CaCLR β sweep**：Table 3 的 monotonic degradation → 折线图 + CI shaded area 比 4 行数字更有冲击力\n3. **Simpson's Paradox**：Table 6 → 5-lang pilot vs 20-lang full 的 paired scatter 最能展示 artifact inflation\n4. **Control task selectivity**：Table 10/11 → language × layer heatmap（按 selectivity 着色）是这篇论文最有说服力的潜在图表\n5. **Linear projection saturation curve**：Table 13 → learning curve plot（pairs vs AUROC）是标准呈现方式\n\n从 methods 角度，表格呈现要求读者自行 mental visualization，增加了审稿负担。\n\n---\n\n### [REBUT（部分）] R2-W3: CaCLR 失败使论文只剩两个贡献\n\nR2 认为 CaCLR 失败意味着论文实质只剩 (1) control task 方法论 (2) 负面实验结果，对 main conference 不够。我 **部分不同意**，理由如下：\n\n**CaCLR 的 systematic negative result 本身构成独立贡献**，前提是实验设计足够彻底——而本文确实做到了：\n- β sweep 跨 3 OOM（Table 3），每个 β 值有 per-language breakdown\n- Component ablation（Table 4）清楚分离了 α (SB-ECE) 和 β (MMD) 的各自效果\n- 理论解释链：1-D MMD limitation → Zhao et al. (2019) conditional distribution mismatch → linear projection 作为 constructive alternative\n- 两个架构上一致复现\n\n在 NLP 社区中，well-executed negative results 有独立的出版价值（见 Rogers et al. 2020 \"A Primer in BERTology\" 对 negative probing results 的讨论）。关键在于 negative result 是否 **informative**——即它是否关闭了一条合理的研究路径并解释了为什么。本文在这方面做得不错。\n\n**但我同意 R2 的实质判断**：对 main conference 而言，\"thorough negative result\" + \"control task finding\" 两个贡献的 excitement 可能不够。我在独立审稿中给出 Overall 4/5 (Weak Accept) 也是基于类似考量。对于一篇 Findings paper，这个 package 足够了。\n\n**从 Methods 角度的补充**：CaCLR 负面结果的一个根本局限是 MMD 只在 1-D probe logits 上操作（§3.2 明确承认）。论文未测试 activation-space MMD 或 optimal transport 等替代方案。如果未来工作在高维空间做 distributional matching 成功了，这篇论文的 \"closing the path\" claim 就被限定为 \"closing the 1-D path\"。但作为当前 contribution，thoroughness 本身有价值。\n\n---\n\n### [AGREE] R2-W4: Pilot 区分不充分\n\n同意。论文多次提到 \"pilot studies on Qwen2.5-7B and Llama-3.1-8B\" 但未说明：\n- 这些 pilot 是否有独立出版物\n- 如果未出版，pilot 数据是否包含在当前论文的 supplementary 中\n- 具体 pilot 实验的规模和设置\n\n从 methods 角度，这尤其影响 §5.3 的 Simpson's Paradox analysis（Table 6），因为该分析的核心逻辑是 \"pilot 的 5 语言结果是 artifact\"——读者需要能独立验证 pilot 的具体设置和结果。\n\n---\n\n### [AGREE，附重要补充] R2-W5: Difficulty decomposition 负面结论太快\n\n完全同意。这与我独立审稿中的 W-M4 高度一致。\n\n§5.4 仅用一段否定 decomposition，核心数据是 Table 9：Δ=-0.003 vs random Δ=-0.005, p=0.42。但论文 **未讨论** 以下关键因素：\n\n1. **IRT R²=0.31 是根本问题**。如果 difficulty probe 只捕获 31% 的 difficulty variance，那么 \"projecting out difficulty\" 实际上投影的是一个噪声方向。Random-direction control 产生同量级效果恰恰与此一致——两种投影都在做 noisy dimensionality reduction。论文应讨论：R²≥0.50 的 difficulty probe 是否会改变结论。\n\n2. **Scale 效应**。Pilot 在 7B dense 模型上可能有更 linear/concentrated 的 difficulty encoding（representation 更简单）。235B MoE 的 representation 可能更 distributed/nonlinear，使 linear IRT probe 失效。论文应对比不同 scale 的 difficulty probe R²。\n\n3. **量化效应**。INT4 量化可能 selectively 损伤 difficulty signal（如果 difficulty 信号集中在低方差维度，4-bit 量化会 disproportionately 影响它）。\n\n一段话的否定不足以关闭 decomposition 路径。至少需要一个 supplementary section 分析失败原因。\n\n---\n\n### [AGREE，附重要修正] R2-W6: \"Only viable path\" 与 Table 21 的张力\n\nR2 正确指出了一个重要张力。让我从 experiments 角度详细分析。\n\n**Table 21（Appendix, page 13，即 Table 5 在 appendix 中的完整版）：**\n\n| Condition | Mean AUROC | Δ vs ZS | Sig. impr. count |\n|-----------|-----------|---------|-----------------|\n| Zero-shot | .572 | — | — |\n| Mean-shift | .572 | .000 | 0/20 |\n| LinProj 200 | .610 | +.038 | 11/20 |\n| Few-shot 25 | .594 | +.022 | 7/20 |\n| Few-shot 100 | .623 | +.051 | 13/20 |\n\n**关键观察**：Few-shot 100 的 AUROC (.623) 和 Sig. impr. count (13/20) 都高于 Linear Proj 200 (.610, 11/20)。论文声称 linear projection 是 \"the only viable transfer method\"（§1 Abstract, §5.6 标题），但 **few-shot 100 按多数指标优于 linear projection**。\n\n论文对此的隐含辩护是：few-shot 需要 target-language correctness labels，而 linear projection 只需要 parallel data（无需 labels）。这个 distinction 是合理的——但论文 **没有明确地做出这个区分**。\"Only viable path\" 的措辞暗示 linear projection 是唯一有效的方法，但 few-shot 100 明显更有效。\n\n**建议修正**：论文应将 claim 改为 \"the only viable **label-free** transfer method\" 或 \"the only viable transfer method that does not require target-language correctness labels\"。当前措辞对读者有误导。\n\n此外，从 practical 角度：如果一个 practitioner 已经有 100 条 target-language labeled data，few-shot 直接优于 linear projection。Linear projection 的优势仅在 zero-label scenario，而该 scenario 仍需 100-200 parallel pairs——获取 parallel data 的难度与获取 labeled data 的难度在低资源语言中可能相当。论文应讨论这个 practical trade-off。\n\n---\n\n## 总结\n\n| R2 Issue | 我的判断 | 关键理由 |\n|----------|---------|---------|\n| W1 (引用不足/References 丢失) | AGREE（附修正：References section 存在但不醒目） | ~15 篇引用不足；缺 IRT/calibration/probing survey 基础文献 |\n| W2 (23 表 0 图) | AGREE | 核心负面结论极适合可视化 |\n| W3 (CaCLR 失败 → 只剩两个贡献) | 部分 REBUT | Systematic negative result 本身有价值（if well-executed），但同意对 main conference excitement 不足 |\n| W4 (pilot 区分不充分) | AGREE | 影响 Simpson's Paradox 验证的可信度 |\n| W5 (decomposition 否定太快) | AGREE（强烈） | IRT R²=0.31 是根本问题；需分析失败原因而非直接否定路径 |\n| W6 (\"Only viable path\" 过强) | AGREE（附具体证据） | Few-shot 100 在 AUROC (.623 vs .610) 和 sig. count (13/20 vs 11/20) 上均优于 LinProj 200 |\n\n**评分微调**：在阅读 R2 的审稿后，我认为 R2-W6 的观点有力地削弱了论文的 practical recommendation 部分。结合 R2-W5（decomposition 否定太快），论文的两个非 control-task 贡献（negative result narrative + practical recommendation）都有明显的 overclaim。我维持 **Overall 4/5 (Weak Accept)**，因为 control task contribution + statistical rigor + honest framing 仍然有价值，但更倾向于 Findings track。R2 给 3/5 (Borderline)，差异主要在于我对 negative result 的独立价值评估略高。\n",
    "reviewer_id": "1",
    "project": "xling_calib_direction"
  }
}
```

</details>

---

### Tool result

_source line 143 · 2026-05-21T06:14:10.797119+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4620
}
```

</details>

---

### Assistant

_source line 144 · 2026-05-21T06:14:15.956199+00:00_

交叉回应已提交。六条 R2 weaknesses 中，AGREE 4 条（W1 附修正、W2、W4、W5 强烈同意），部分 REBUT 1 条（W3：negative result 本身有独立价值），AGREE 附重要证据 1 条（W6：few-shot 100 在 Table 21 中实际优于 linear projection）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1"
}
```

</details>

---

## Round 6

50 recorded events

### User

_source line 145 · 2026-05-21T13:59:18.312569+00:00_

[Round 1 审稿请求]:
## Review Task: Full Paper Review

**Paper**: "Cross-Lingual Correctness Probe Transfer: Negative Results, Methodological Warnings, and Conditional Solutions"
**Venue**: EACL via ACL Rolling Review
**Review mode**: Simple (single comprehensive reviewer)

### Scoring rubric (ACL ARR)
- **Soundness** (1-5): 5=Excellent, 4=Strong, 3=Acceptable, 2=Poor, 1=Major Issues
- **Excitement** (1-5): 5=Highly Exciting, 4=Exciting, 3=Interesting, 2=Potentially Interesting, 1=Not Exciting  
- **Overall** (1-5): 5=Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit

### Paper summary for context
11-page paper (9 main + appendices A-D). Predominantly negative results paper studying cross-lingual transfer of correctness probes across 3 architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense) and 20 languages. Key claims: (1) Control task warning: 35% artifact rate in cross-lingual probing, (2) Mean-shift impossibility (ΔAUROC ≡ 0), (3) Distributional matching path closed (CaCLR, CORAL, high-dim MMD all fail), (4) Linear projection conditional guidance.

### Experiment design reference (complete list from design doc)
The full experiment plan includes 13 experiments:
1. Qwen3-235B Pareto Frontier (plan_001) — covered in Table 1, §5.1
2. Llama 4 Scout Pareto (plan_002) — covered in §5.1 text (no dedicated table)
3. Gemma 4 31B Pareto (plan_008) — covered in Table 2, §5.2
4. CaCLR + distributional matching (plan_003) — covered in Tables 6-8, §7
5. Difficulty decomposition (plan_004) — covered in Table 9, §8
6. Cross-lingual orthogonality (plan_005) — covered in §11.1 (brief)
7. Probe complexity (plan_006) — Appendix A, Table 14
8. Belebele + MMLU-ProX (plan_007) — Appendix B, Table 15
9. Extended 52 languages (plan_009) — Appendix D (1 paragraph)
10. Quantization validation (plan_010) — Appendix C, Table 16
11. CKA analysis (plan_011) — Tables 4-5, §6
12. Linear projection sensitivity (plan_012) — Tables 12-13, §10
13. Control tasks (plan_013) — Tables 10-11, §9

All 13 experiments present. Major figures described in design are ABSENT from the PDF — paper relies entirely on tables.

### What I need from you
Produce a complete ACL ARR review covering:
1. Paper summary (2-3 sentences)
2. Summary of strengths (numbered)
3. Summary of weaknesses (numbered)
4. Questions for the authors
5. Missing references or related work
6. Scores: Soundness, Excitement, Overall (with justification)
7. Confidence level (1-5)
8. Assessment of experiment coverage completeness vs. the design doc

Be rigorous. Note broken LaTeX citations ("??" appears multiple times on page 1). Evaluate whether the paper's framing as "negative results + methodology paper" is convincing for EACL.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---

### Tool call

_source line 146 · 2026-05-21T13:59:33.585721+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/review_input_f5f46a62.pdf",
  "project": "xling_calib_direction",
  "pages": "1-6",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/review_input_f5f46a62.pdf",
    "project": "xling_calib_direction",
    "pages": "1-6",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 147 · 2026-05-21T13:59:34.239753+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 339.6}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 341.6}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 298.0}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 311.6}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 283.2}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 225.9}], \"total_pages\": 14, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 654
}
```

</details>

---

### Tool call

_source line 148 · 2026-05-21T13:59:54.420039+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p1.png"
  }
}
```

</details>

---

### Tool call

_source line 149 · 2026-05-21T13:59:54.771710+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p5.png"
  }
}
```

</details>

---

### Tool result

_source line 150 · 2026-05-21T13:59:54.976764+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 556
}
```

</details>

---

### Tool result

_source line 151 · 2026-05-21T13:59:55.179874+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 408
}
```

</details>

---

### Tool call

_source line 152 · 2026-05-21T14:01:51.797677+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 153 · 2026-05-21T14:01:51.848200+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 154 · 2026-05-21T14:01:56.264311+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/review_input_f5f46a62.pdf",
  "project": "xling_calib_direction",
  "pages": "1-4",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/review_input_f5f46a62.pdf",
    "project": "xling_calib_direction",
    "pages": "1-4",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 155 · 2026-05-21T14:01:56.922360+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 339.6}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 341.6}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 298.0}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 311.6}], \"total_pages\": 14, \"rendered_pages\": 4, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 658
}
```

</details>

---

### Tool call

_source line 156 · 2026-05-21T14:02:00.537156+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p1.png"
  }
}
```

</details>

---

### Tool result

_source line 157 · 2026-05-21T14:02:01.444953+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---

### Tool call

_source line 158 · 2026-05-21T14:02:01.495670+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p2.png"
  }
}
```

</details>

---

### Tool result

_source line 159 · 2026-05-21T14:02:01.900755+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 405
}
```

</details>

---

### Tool call

_source line 160 · 2026-05-21T14:02:01.951340+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p3.png"
  }
}
```

</details>

---

### Tool result

_source line 161 · 2026-05-21T14:02:02.412026+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 460
}
```

</details>

---

### Tool call

_source line 162 · 2026-05-21T14:02:02.412530+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p4.png"
  }
}
```

</details>

---

### Tool result

_source line 163 · 2026-05-21T14:02:02.867112+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---

### Tool call

_source line 164 · 2026-05-21T14:02:06.831008+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/review_input_f5f46a62.pdf",
  "project": "xling_calib_direction",
  "pages": "5-8",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/review_input_f5f46a62.pdf",
    "project": "xling_calib_direction",
    "pages": "5-8",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 165 · 2026-05-21T14:02:07.183100+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 283.2}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 225.9}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 304.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 296.1}], \"total_pages\": 14, \"rendered_pages\": 4, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 352
}
```

</details>

---

### Tool call

_source line 166 · 2026-05-21T14:02:10.846464+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p5.png"
  }
}
```

</details>

---

### Tool result

_source line 167 · 2026-05-21T14:02:11.802061+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---

### Tool call

_source line 168 · 2026-05-21T14:02:11.802497+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p6.png"
  }
}
```

</details>

---

### Tool result

_source line 169 · 2026-05-21T14:02:12.256234+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---

### Tool call

_source line 170 · 2026-05-21T14:02:12.256679+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p7.png"
  }
}
```

</details>

---

### Tool result

_source line 171 · 2026-05-21T14:02:12.709533+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 172 · 2026-05-21T14:02:12.810671+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p8.png"
  }
}
```

</details>

---

### Tool result

_source line 173 · 2026-05-21T14:02:13.214721+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 404
}
```

</details>

---

### Tool call

_source line 174 · 2026-05-21T14:02:17.078265+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/review_input_f5f46a62.pdf",
  "project": "xling_calib_direction",
  "pages": "9-14",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/review_input_f5f46a62.pdf",
    "project": "xling_calib_direction",
    "pages": "9-14",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 175 · 2026-05-21T14:02:17.530950+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 230.8}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 221.8}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 225.2}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 186.4}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 160.1}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 77.1}], \"total_pages\": 14, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 176 · 2026-05-21T14:02:21.446209+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p9.png"
  }
}
```

</details>

---

### Tool result

_source line 177 · 2026-05-21T14:02:22.403734+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---

### Tool call

_source line 178 · 2026-05-21T14:02:22.404181+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p10.png"
  }
}
```

</details>

---

### Tool result

_source line 179 · 2026-05-21T14:02:22.861711+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 457
}
```

</details>

---

### Tool call

_source line 180 · 2026-05-21T14:02:22.862172+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p11.png"
  }
}
```

</details>

---

### Tool result

_source line 181 · 2026-05-21T14:02:23.315442+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---

### Tool call

_source line 182 · 2026-05-21T14:02:23.315868+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p12.png"
  }
}
```

</details>

---

### Tool result

_source line 183 · 2026-05-21T14:02:23.720562+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 404
}
```

</details>

---

### Tool call

_source line 184 · 2026-05-21T14:02:28.138828+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p13.png"
  }
}
```

</details>

---

### Tool call

_source line 185 · 2026-05-21T14:02:28.390372+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p14.png"
  }
}
```

</details>

---

### Tool result

_source line 186 · 2026-05-21T14:02:28.443901+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 305
}
```

</details>

---

### Tool result

_source line 187 · 2026-05-21T14:02:28.447724+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 57
}
```

</details>

---

### Tool call

_source line 188 · 2026-05-21T14:05:21.524564+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "# Reviewer 1 — 综合审稿报告（Worst Paper Variant: Full ACL ARR Review for EACL）\n\n**论文**: \"The Limits of Cross-Lingual Calibration Probe Transfer: A Large-Scale Negative Result with Methodological Implications\"\n\n---\n\n## 1. Paper Summary\n\n本文对跨语言正确性探针迁移（correctness probe transfer）进行了大规模实证研究，涵盖 3 种 LLM 架构（Qwen3-235B-A22B, Llama 4 Scout, Gemma 4 31B）、20 种语言和 5 种迁移条件。结果以负面为主：(1) 深度-可迁移性 Pareto 前沿不泛化；(2) CaCLR 校准感知正则化有害；(3) IRT 难度分解与随机不可区分；(4) CKA 几何分析的 pilot 发现系 Simpson's Paradox 伪影。唯一可行的迁移路径是线性投影（Procrustes alignment），但需要 100-200 对标注数据且效果不一致。论文将自身定位为\"负面结果+方法论贡献\"，其中方法论贡献是首次将 Hewitt & Liang 控制任务选择性应用于跨语言探针文献，发现 42% LOW / 37% MID 的伪影率。\n\n---\n\n## 2. 总体评分\n\n**Overall**: 2/5 (Reject)\n\n**一句话总结**: 规模可观的负面结果研究，但英语源探针质量低（AUROC 0.715-0.742）和量化伪影这两个系统性混淆因素严重削弱了核心结论的可信度，加上排版缺陷（多处 \"??\" 断引、零图表），尚未达到发表标准。\n\n---\n\n## 3. 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 2.5/5 | 两个未解决的系统混淆因素（低 EN AUROC、深层量化偏差）使核心负面声明不可靠。多处缺少置信区间。 |\n| **Excitement / Novelty** | 2/5 | 负面结果本身有价值，但由于混淆因素，信息量降低——读者无法确定这些限制是基本的还是实验设计导致的。控制任务方法论贡献是真实的但未被充分开发。 |\n| **Clarity** | 2.5/5 | 文本叙述清晰，但零图表（23 个表格、0 个 figure）严重阻碍可读性。Pareto 前沿分析论文没有散点图令人费解。多处 \"??\" 断引。 |\n| **Reproducibility** | 3.5/5 | 论文声称提供完整实现细节和逐语言结果（Section 6 末尾），Appendix A-E 有丰富的逐语言数据。但代码/数据未附。 |\n| **Overall** | 2/5 | 低于接收门槛。 |\n\n---\n\n## 4. Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 英语源探针质量低构成系统性混淆因素\n- 具体位置：Section 4 (Experimental Setup), Table 1, Table 11\n- 问题：全文所有迁移实验的起点是英语校准探针，但其最佳 AUROC 仅为 0.715（Qwen3）到 0.742（Gemma 4 31B）。Table 1 报告 Qwen3-235B 最佳 EN AUROC 为 0.738（layer 72, zero-shot pass rate 0.695）。这是一个中等偏低的分类器质量。论文所有\"迁移失败\"的负面结论都建立在这个薄弱基础之上——如果源信号本身不够强，迁移失败可能只是信号不足的下游表现，而非跨语言迁移本身的基本限制。\n- 为什么影响接收：这是最核心的 confound。论文的 title claim (\"The Limits of Cross-Lingual Calibration Probe Transfer\") 暗示这些是基本限制，但 EN AUROC < 0.75 意味着源探针仅比随机好 ~22-25 个百分点。在 EN AUROC > 0.85 的场景下，结果是否不同？论文完全没有讨论这一替代解释。\n- 建议修改方向：(1) 明确讨论低 EN AUROC 作为限制条件；(2) 增加消融实验，例如筛选 EN AUROC > 0.80 的层/模型子集重新评估迁移；(3) 将标题和 claims 限定为\"在中等质量源探针条件下的限制\"。\n\n**N2** [critical] 量化伪影与深层迁移负面结论混淆\n- 具体位置：Section 5.8, Table 18, Table 22\n- 问题：Table 18（Quantization validation, 5% data subset）显示 INT4 量化的 AUROC 下降随深度单调增加——Llama4 从 20% depth 的 Δ=−0.003 增长到 95% depth 的 Δ=−0.018；Qwen3 从 −0.005 到 −0.022。Table 22（Full quantization validation, 5 layer depth percentiles）证实了同样的模式。但论文的核心负面发现之一就是\"深层探针迁移效果差\"（Section 5.1, Pareto 前沿分析）——这恰好与量化在深层的退化重叠。论文在 Section 5.8 承认\"Quantization does not change the direction of any negative result but adds ∼7pp uncertainty to absolute AUROC values at deep layers\"，但 7pp 的不确定性在 AUROC 仅为 0.7x 的情况下是巨大的（占有效信号的 ~30%）。\n- 为什么影响接收：论文的 Pareto 前沿非泛化结论（Section 5.1）可能被量化偏差而非真实的跨语言限制所驱动。7pp 不确定性足以翻转许多边缘结果。\n- 建议修改方向：(1) 在 FP16 下重新运行深层探针实验（至少对关键模型的关键层）；(2) 或在报告 Pareto 分析时明确扣除量化偏差的估计影响；(3) 将量化限制提升为主体讨论而非附录级别。\n\n**N3** [critical] LaTeX 编译错误导致多处引用断裂\n- 具体位置：Page 1 (Abstract), 多处\n- 问题：论文第一页即出现多个 \"??\" 标记，表明 LaTeX \\cite 命令未能正确解析。在 Abstract 中出现引用断裂对任何 venue 都是不可接受的。这不仅是排版问题——审稿人无法核实论文声称的先行工作。\n- 为什么影响接收：违反基本投稿要求。审稿人无法验证引用声明的真实性。\n- 建议修改方向：修复 .bib 文件并重新编译。\n\n---\n\n## 5. Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 零图表——23 个表格、0 个 Figure\n- 具体位置：全文\n- 问题：一篇以 Pareto 前沿分析为核心的论文没有任何散点图、热力图或可视化。Table 1-4 中的逐语言 Spearman 相关数据完全可以用 scatter plot 展示（depth vs. cross-shot AUROC, 按语言着色），这将比纯数字表格直观得多。23 个密集表格使论文几乎不可读。\n- 建议：至少添加 (1) Pareto 前沿散点图；(2) CaCLR α-sweep 折线图；(3) 控制任务选择性热力图（Table 10-11 数据）。\n\n**W2** [warning] CaCLR 设计空间探索不足就做出\"有害\"结论\n- 具体位置：Section 3.2, Section 5.2, Table 3\n- 问题：CaCLR 仅测试了一种核心配置：Gaussian RBF kernel + median-heuristic bandwidth + α ∈ {0.01, 0.05, 0.1, 1.0}。Table 3 显示即使最小 α=0.01 也导致 ΔAUROC = −0.003（Qwen3, 50% depth），且所有 α 值均为负。论文据此声称 CaCLR \"uniformly harmful\"。但 (1) 仅测试 4 个 α 值和 1 个 kernel 选择；(2) 未尝试其他 MMD 变体或更低的 α（如 0.001）；(3) 未给出 CaCLR 不适用于 1-D logistic regression 的理论分析。\n- 建议：要么扩展搜索空间，要么提供更强的理论论证解释为什么 MMD 在此设定下必然有害。\n\n**W3** [warning] 控制任务发现（最强贡献）被埋没\n- 具体位置：Section 5.5, Table 10-11\n- 问题：42% LOW 伪影率（即 42% 的低资源语言层的探针性能可以完全被容量伪影解释）是本文最具影响力和方法论贡献的发现。但它被放在第 5 个子节（Section 5.5），在 Pareto、CaCLR、decomposition、CKA 之后。如果将此作为论文的 leading contribution 并重新组织叙事，会大大提升论文的 excitement 评分。\n- 建议：重新组织论文结构，以控制任务方法论发现为核心叙事。\n\n**W4** [warning] Related Work 过于简略\n- 具体位置：Section 2 (约半页)\n- 问题：Section 2 仅约半页，分为 4 个小节（Probe-based calibration, Cross-lingual probing, Probing methodology, Domain adaptation theory, Cross-lingual alignment），每节仅 2-4 句话。对于一篇声称是\"large-scale\"研究的论文，related work 的覆盖面不够。特别是：(1) 近期跨语言表示学习的重要工作（如 Conneau et al. 的多语言 probing 系列）讨论不足；(2) 负面结果论文的先例讨论缺失（该社区有哪些成功的负面结果论文？）；(3) 校准相关文献（Guo et al. 2017 温度缩放、Desai & Durrett 2020 等经典工作）未出现。\n- 建议：扩展 Related Work 至至少 1 页，增加上述缺失的讨论。\n\n**W5** [warning] Simpson's Paradox 解释不充分\n- 具体位置：Section 5.3, Table 6 (p.6)\n- 问题：Section 5.3 报告 CKA 分析中发现 Simpson's Paradox——pilot 阶段的 5 语言样本显示深度与 CKA-transfer 正相关，但扩展到 20 语言后变为负相关或不显著。论文将此归因于\"between-language heterogeneity in CKA patterns overwhelms the within-layer signal\"和\"small-sample artifacts that use small-sample artifacts\"，但没有给出具体机制解释——为什么恰好是这 5 种语言产生了正相关？它们有什么特殊性？Table 6 显示了 5-lang pilot 的 Simpson's partial ρ = +0.14 (p=0.22)，但这个 p 值本身就不显著，所以 pilot 阶段就不应该报告为\"positive finding\"。\n- 建议：(1) 说明 pilot 的 5 种语言是哪些及其选择标准；(2) 讨论这是否反映了 pilot 设计缺陷而非 Simpson's Paradox。\n\n**W6** [warning] 线性投影\"唯一可行路径\"但实用性讨论不足\n- 具体位置：Section 5.6, Table 13, Table 21\n- 问题：论文将线性投影（Procrustes alignment）称为\"the only viable transfer method\"（Abstract 及 Section 5.6），但 Table 13 显示需要 100-200 对平行数据，且 Table 21（Qwen3-235B, 5 transfer conditions）显示 LinProj 200 的 Δ vs ZS 仅为 +0.038（mean AUROC 从 0.572 到 0.610），仅 11/20 语言达到显著改善。Few-shot 100 达到 +0.051 且 13/20 显著。这引发两个问题：(1) 线性投影是否真的优于简单 few-shot？(2) 需要 100-200 对标注数据时，直接训练目标语言探针可能更经济。论文未讨论这一成本效益分析。\n- 建议：增加 few-shot vs. LinProj 的成本效益对比讨论。\n\n---\n\n## 6. 小问题（不影响接收）\n\n- Table 7（Same-layer cross-language CKA-transfer）中 Layer (%) 列的对齐不一致，部分行的 p 值格式不统一。\n- Section 5.9 \"Orthogonality Across Languages\" 内容较薄（不到半页），作为独立小节不太必要，可以合并到 Section 5.5 控制任务讨论中。\n- Table 23（Cross-lingual correctness-confidence cosine similarity）中\"mag. mismatch\"和\"elevated\"的注释缺乏明确定义。\n- Appendix B/C/D/E 的标题有但内容在本 PDF 中似乎只是表格罗列，缺少文字解释。\n- 论文声称\"We release complete overlay code and implementation specifications to enable independent verification\"（Section 6 末尾），但未提供链接或匿名仓库。\n\n---\n\n## 7. Questions for the Authors\n\n1. **EN AUROC 混淆**：如果仅保留 EN AUROC > 0.80 的层/模型组合（如 Gemma 的 0.742 已接近），Pareto 前沿和迁移结论是否改变？是否考虑过使用更强的探针架构（如 2-layer MLP）来排除源探针质量的混淆？\n\n2. **CaCLR 搜索空间**：α = 0.001 或更小的值是否测试过？论文仅报告 α ∈ {0.01, 0.05, 0.1, 1.0}，是否有理论理由认为更小的 α 也必然有害？\n\n3. **量化与深层**：是否可以在至少一个模型上提供 FP16 和 INT4 在相同深层的 head-to-head 迁移比较？当前 Table 18 仅报告单语言 AUROC 差异，不包含迁移性能。\n\n4. **控制任务的 42% 伪影率**：这个数字在不同模型/架构之间是否稳定？MoE（Qwen3）和 Dense（Gemma）架构的伪影率是否有系统差异？\n\n5. **Figure 缺失**：是否有技术原因导致无法生成图表？23 个表格的论文即使对审稿人也非常难以消化。\n\n6. **\"负面结果 + 方法论\"定位**：作者是否考虑过将论文重新定位为以控制任务方法论为核心（正面贡献），辅以负面迁移结果作为案例研究？\n\n---\n\n## 8. Missing References / Related Work\n\n- **断裂引用**：Page 1 出现多处 \"??\"，无法核实声称的先行工作。这是最严重的引用问题。\n- **缺失的关键引用**：\n  - Guo et al. (2017) \"On Calibration of Modern Neural Networks\" — 校准领域的奠基工作\n  - Desai & Durrett (2020) \"Calibration of Pre-trained Transformers\" — 直接相关的校准+LLM 工作\n  - Conneau et al. (2020) \"Emerging Cross-lingual Structure in Pretrained Language Models\" — 跨语言表示结构的经典工作\n  - Hewitt & Liang (2019) \"Designing and Interpreting Probes with Control Tasks\" — 论文方法论的核心依赖，需要确认是否在断裂引用中\n  - 近期的 Probing 综述文献\n\n---\n\n## 9. Experiment Coverage Assessment\n\n对照设计文档中的 13 个实验计划：\n\n| # | 实验 | 是否涵盖 | 位置 |\n|---|------|----------|------|\n| 1 | Depth-transferability Pareto (Qwen3-235B) | ✅ | Table 1, Section 5.1 |\n| 2 | Depth-transferability Pareto (Llama 4 Scout) | ✅ | Table 1, Section 5.1 |\n| 3 | Depth-transferability Pareto (Gemma 4 31B) | ✅ | Table 1/Table 20, Section 5.1 |\n| 4 | CaCLR sweep | ✅ | Table 3, Section 5.2 |\n| 5 | Difficulty decomposition ablation | ✅ | Table 9, Section 5.4 |\n| 6 | CKA geometric analysis (Simpson's Paradox) | ✅ | Table 6-7, Section 5.3 |\n| 7 | Control tasks / selectivity | ✅ | Table 10-11, Section 5.5 |\n| 8 | Linear projection (5 conditions) | ✅ | Table 13/21, Section 5.6 |\n| 9 | Cross-benchmark generalization | ✅ | Table 16, Section 5.7 |\n| 10 | Probe complexity comparison | ✅ | Table 17, Section 5.8 |\n| 11 | Quantization validation | ✅ | Table 18/22, Section 5.8 |\n| 12 | Extended language coverage (52 lang) | ✅ | Table 19, Appendix A |\n| 13 | Cross-lingual orthogonality | ✅ | Table 23, Section 5.9 |\n\n**覆盖率：13/13 (100%)**。所有实验计划均已执行。但多数实验的报告存在上述质量问题（低 EN AUROC 混淆、缺乏误差线/置信区间等）。\n\n---\n\n## 10. \"负面结果 + 方法论\"定位评估（EACL 适配性）\n\n**部分令人信服，但不足以支撑接收。** 具体分析：\n\n- **负面结果维度**：论文的实验规模确实大（3 架构 × 20 语言 × 5 条件），如果负面结论成立，对社区有重要价值。但 N1（低 EN AUROC）和 N2（量化混淆）两个未解决的 confound 意味着读者无法确信这些是真正的\"limits\"还是实验设计的局限。一篇好的负面结果论文需要排除替代解释——本文未做到。\n\n- **方法论维度**：将 Hewitt & Liang 控制任务引入跨语言探针文献是真实的贡献（Section 5.5），42% 伪影率发现意义重大。但这一贡献在当前论文结构中是从属地位（第 5 个子节），且仅占约 1 页篇幅。如果以此为核心重写论文，excitement 评分会显著提升。\n\n- **EACL 适配性**：EACL 欢迎负面结果和资源型论文，但仍要求 soundness。当前版本的 soundness 不足以通过 EACL 的审稿标准。\n\n---\n\n## 11. 主要优势\n\n1. **实验规模**：3 种架构（含 MoE 和 Dense）、20 种语言、5 种迁移条件——这是目前跨语言探针迁移文献中规模最大的研究。\n2. **诚实的负面结果报告**：论文没有试图美化结果，Section 5.1-5.4 的每个负面发现都有明确的数字支撑。\n3. **控制任务方法论**：首次将 selectivity-based control tasks 应用于跨语言探针，42% LOW 伪影率是有价值的发现。\n4. **丰富的 Appendix**：逐语言、逐层的完整结果（Table 10-23），支持独立验证。\n5. **52 语言扩展**：Table 19 将核心发现从 20 语言扩展到 52 语言，增强了泛化性声明。\n6. **Limitations 段落**（Section 6 末尾）坦诚地列出了 4 个限制，包括 MoE 架构的不确定性和 quantization 的影响。\n\n---\n\n## 12. Confidence\n\n**Confidence: 4/5** — 我对跨语言表示学习和探针方法论领域较为熟悉，已完整阅读论文全部 14 页及所有 23 个表格。对核心混淆因素的判断有较高把握。\n\n---\n\n## 13. 最终判断\n\n**Reject (2/5)**。论文方向有价值、规模可观，但两个关键混淆因素（低 EN AUROC、深层量化偏差）未被解决，使得\"基本限制\"的核心声明不可信。排版问题（\"??\" 断引、零图表）加剧了可读性困难。建议：(1) 以控制任务方法论为核心重写；(2) 解决 EN AUROC 混淆（至少讨论，最好做消融）；(3) 修复引用并添加关键图表；(4) 扩充 Related Work。在这些修改后，论文有潜力达到 EACL 的接收标准。",
  "reviewer_id": "1",
  "project": "xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "# Reviewer 1 — 综合审稿报告（Worst Paper Variant: Full ACL ARR Review for EACL）\n\n**论文**: \"The Limits of Cross-Lingual Calibration Probe Transfer: A Large-Scale Negative Result with Methodological Implications\"\n\n---\n\n## 1. Paper Summary\n\n本文对跨语言正确性探针迁移（correctness probe transfer）进行了大规模实证研究，涵盖 3 种 LLM 架构（Qwen3-235B-A22B, Llama 4 Scout, Gemma 4 31B）、20 种语言和 5 种迁移条件。结果以负面为主：(1) 深度-可迁移性 Pareto 前沿不泛化；(2) CaCLR 校准感知正则化有害；(3) IRT 难度分解与随机不可区分；(4) CKA 几何分析的 pilot 发现系 Simpson's Paradox 伪影。唯一可行的迁移路径是线性投影（Procrustes alignment），但需要 100-200 对标注数据且效果不一致。论文将自身定位为\"负面结果+方法论贡献\"，其中方法论贡献是首次将 Hewitt & Liang 控制任务选择性应用于跨语言探针文献，发现 42% LOW / 37% MID 的伪影率。\n\n---\n\n## 2. 总体评分\n\n**Overall**: 2/5 (Reject)\n\n**一句话总结**: 规模可观的负面结果研究，但英语源探针质量低（AUROC 0.715-0.742）和量化伪影这两个系统性混淆因素严重削弱了核心结论的可信度，加上排版缺陷（多处 \"??\" 断引、零图表），尚未达到发表标准。\n\n---\n\n## 3. 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 2.5/5 | 两个未解决的系统混淆因素（低 EN AUROC、深层量化偏差）使核心负面声明不可靠。多处缺少置信区间。 |\n| **Excitement / Novelty** | 2/5 | 负面结果本身有价值，但由于混淆因素，信息量降低——读者无法确定这些限制是基本的还是实验设计导致的。控制任务方法论贡献是真实的但未被充分开发。 |\n| **Clarity** | 2.5/5 | 文本叙述清晰，但零图表（23 个表格、0 个 figure）严重阻碍可读性。Pareto 前沿分析论文没有散点图令人费解。多处 \"??\" 断引。 |\n| **Reproducibility** | 3.5/5 | 论文声称提供完整实现细节和逐语言结果（Section 6 末尾），Appendix A-E 有丰富的逐语言数据。但代码/数据未附。 |\n| **Overall** | 2/5 | 低于接收门槛。 |\n\n---\n\n## 4. Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 英语源探针质量低构成系统性混淆因素\n- 具体位置：Section 4 (Experimental Setup), Table 1, Table 11\n- 问题：全文所有迁移实验的起点是英语校准探针，但其最佳 AUROC 仅为 0.715（Qwen3）到 0.742（Gemma 4 31B）。Table 1 报告 Qwen3-235B 最佳 EN AUROC 为 0.738（layer 72, zero-shot pass rate 0.695）。这是一个中等偏低的分类器质量。论文所有\"迁移失败\"的负面结论都建立在这个薄弱基础之上——如果源信号本身不够强，迁移失败可能只是信号不足的下游表现，而非跨语言迁移本身的基本限制。\n- 为什么影响接收：这是最核心的 confound。论文的 title claim (\"The Limits of Cross-Lingual Calibration Probe Transfer\") 暗示这些是基本限制，但 EN AUROC < 0.75 意味着源探针仅比随机好 ~22-25 个百分点。在 EN AUROC > 0.85 的场景下，结果是否不同？论文完全没有讨论这一替代解释。\n- 建议修改方向：(1) 明确讨论低 EN AUROC 作为限制条件；(2) 增加消融实验，例如筛选 EN AUROC > 0.80 的层/模型子集重新评估迁移；(3) 将标题和 claims 限定为\"在中等质量源探针条件下的限制\"。\n\n**N2** [critical] 量化伪影与深层迁移负面结论混淆\n- 具体位置：Section 5.8, Table 18, Table 22\n- 问题：Table 18（Quantization validation, 5% data subset）显示 INT4 量化的 AUROC 下降随深度单调增加——Llama4 从 20% depth 的 Δ=−0.003 增长到 95% depth 的 Δ=−0.018；Qwen3 从 −0.005 到 −0.022。Table 22（Full quantization validation, 5 layer depth percentiles）证实了同样的模式。但论文的核心负面发现之一就是\"深层探针迁移效果差\"（Section 5.1, Pareto 前沿分析）——这恰好与量化在深层的退化重叠。论文在 Section 5.8 承认\"Quantization does not change the direction of any negative result but adds ∼7pp uncertainty to absolute AUROC values at deep layers\"，但 7pp 的不确定性在 AUROC 仅为 0.7x 的情况下是巨大的（占有效信号的 ~30%）。\n- 为什么影响接收：论文的 Pareto 前沿非泛化结论（Section 5.1）可能被量化偏差而非真实的跨语言限制所驱动。7pp 不确定性足以翻转许多边缘结果。\n- 建议修改方向：(1) 在 FP16 下重新运行深层探针实验（至少对关键模型的关键层）；(2) 或在报告 Pareto 分析时明确扣除量化偏差的估计影响；(3) 将量化限制提升为主体讨论而非附录级别。\n\n**N3** [critical] LaTeX 编译错误导致多处引用断裂\n- 具体位置：Page 1 (Abstract), 多处\n- 问题：论文第一页即出现多个 \"??\" 标记，表明 LaTeX \\cite 命令未能正确解析。在 Abstract 中出现引用断裂对任何 venue 都是不可接受的。这不仅是排版问题——审稿人无法核实论文声称的先行工作。\n- 为什么影响接收：违反基本投稿要求。审稿人无法验证引用声明的真实性。\n- 建议修改方向：修复 .bib 文件并重新编译。\n\n---\n\n## 5. Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 零图表——23 个表格、0 个 Figure\n- 具体位置：全文\n- 问题：一篇以 Pareto 前沿分析为核心的论文没有任何散点图、热力图或可视化。Table 1-4 中的逐语言 Spearman 相关数据完全可以用 scatter plot 展示（depth vs. cross-shot AUROC, 按语言着色），这将比纯数字表格直观得多。23 个密集表格使论文几乎不可读。\n- 建议：至少添加 (1) Pareto 前沿散点图；(2) CaCLR α-sweep 折线图；(3) 控制任务选择性热力图（Table 10-11 数据）。\n\n**W2** [warning] CaCLR 设计空间探索不足就做出\"有害\"结论\n- 具体位置：Section 3.2, Section 5.2, Table 3\n- 问题：CaCLR 仅测试了一种核心配置：Gaussian RBF kernel + median-heuristic bandwidth + α ∈ {0.01, 0.05, 0.1, 1.0}。Table 3 显示即使最小 α=0.01 也导致 ΔAUROC = −0.003（Qwen3, 50% depth），且所有 α 值均为负。论文据此声称 CaCLR \"uniformly harmful\"。但 (1) 仅测试 4 个 α 值和 1 个 kernel 选择；(2) 未尝试其他 MMD 变体或更低的 α（如 0.001）；(3) 未给出 CaCLR 不适用于 1-D logistic regression 的理论分析。\n- 建议：要么扩展搜索空间，要么提供更强的理论论证解释为什么 MMD 在此设定下必然有害。\n\n**W3** [warning] 控制任务发现（最强贡献）被埋没\n- 具体位置：Section 5.5, Table 10-11\n- 问题：42% LOW 伪影率（即 42% 的低资源语言层的探针性能可以完全被容量伪影解释）是本文最具影响力和方法论贡献的发现。但它被放在第 5 个子节（Section 5.5），在 Pareto、CaCLR、decomposition、CKA 之后。如果将此作为论文的 leading contribution 并重新组织叙事，会大大提升论文的 excitement 评分。\n- 建议：重新组织论文结构，以控制任务方法论发现为核心叙事。\n\n**W4** [warning] Related Work 过于简略\n- 具体位置：Section 2 (约半页)\n- 问题：Section 2 仅约半页，分为 4 个小节（Probe-based calibration, Cross-lingual probing, Probing methodology, Domain adaptation theory, Cross-lingual alignment），每节仅 2-4 句话。对于一篇声称是\"large-scale\"研究的论文，related work 的覆盖面不够。特别是：(1) 近期跨语言表示学习的重要工作（如 Conneau et al. 的多语言 probing 系列）讨论不足；(2) 负面结果论文的先例讨论缺失（该社区有哪些成功的负面结果论文？）；(3) 校准相关文献（Guo et al. 2017 温度缩放、Desai & Durrett 2020 等经典工作）未出现。\n- 建议：扩展 Related Work 至至少 1 页，增加上述缺失的讨论。\n\n**W5** [warning] Simpson's Paradox 解释不充分\n- 具体位置：Section 5.3, Table 6 (p.6)\n- 问题：Section 5.3 报告 CKA 分析中发现 Simpson's Paradox——pilot 阶段的 5 语言样本显示深度与 CKA-transfer 正相关，但扩展到 20 语言后变为负相关或不显著。论文将此归因于\"between-language heterogeneity in CKA patterns overwhelms the within-layer signal\"和\"small-sample artifacts that use small-sample artifacts\"，但没有给出具体机制解释——为什么恰好是这 5 种语言产生了正相关？它们有什么特殊性？Table 6 显示了 5-lang pilot 的 Simpson's partial ρ = +0.14 (p=0.22)，但这个 p 值本身就不显著，所以 pilot 阶段就不应该报告为\"positive finding\"。\n- 建议：(1) 说明 pilot 的 5 种语言是哪些及其选择标准；(2) 讨论这是否反映了 pilot 设计缺陷而非 Simpson's Paradox。\n\n**W6** [warning] 线性投影\"唯一可行路径\"但实用性讨论不足\n- 具体位置：Section 5.6, Table 13, Table 21\n- 问题：论文将线性投影（Procrustes alignment）称为\"the only viable transfer method\"（Abstract 及 Section 5.6），但 Table 13 显示需要 100-200 对平行数据，且 Table 21（Qwen3-235B, 5 transfer conditions）显示 LinProj 200 的 Δ vs ZS 仅为 +0.038（mean AUROC 从 0.572 到 0.610），仅 11/20 语言达到显著改善。Few-shot 100 达到 +0.051 且 13/20 显著。这引发两个问题：(1) 线性投影是否真的优于简单 few-shot？(2) 需要 100-200 对标注数据时，直接训练目标语言探针可能更经济。论文未讨论这一成本效益分析。\n- 建议：增加 few-shot vs. LinProj 的成本效益对比讨论。\n\n---\n\n## 6. 小问题（不影响接收）\n\n- Table 7（Same-layer cross-language CKA-transfer）中 Layer (%) 列的对齐不一致，部分行的 p 值格式不统一。\n- Section 5.9 \"Orthogonality Across Languages\" 内容较薄（不到半页），作为独立小节不太必要，可以合并到 Section 5.5 控制任务讨论中。\n- Table 23（Cross-lingual correctness-confidence cosine similarity）中\"mag. mismatch\"和\"elevated\"的注释缺乏明确定义。\n- Appendix B/C/D/E 的标题有但内容在本 PDF 中似乎只是表格罗列，缺少文字解释。\n- 论文声称\"We release complete overlay code and implementation specifications to enable independent verification\"（Section 6 末尾），但未提供链接或匿名仓库。\n\n---\n\n## 7. Questions for the Authors\n\n1. **EN AUROC 混淆**：如果仅保留 EN AUROC > 0.80 的层/模型组合（如 Gemma 的 0.742 已接近），Pareto 前沿和迁移结论是否改变？是否考虑过使用更强的探针架构（如 2-layer MLP）来排除源探针质量的混淆？\n\n2. **CaCLR 搜索空间**：α = 0.001 或更小的值是否测试过？论文仅报告 α ∈ {0.01, 0.05, 0.1, 1.0}，是否有理论理由认为更小的 α 也必然有害？\n\n3. **量化与深层**：是否可以在至少一个模型上提供 FP16 和 INT4 在相同深层的 head-to-head 迁移比较？当前 Table 18 仅报告单语言 AUROC 差异，不包含迁移性能。\n\n4. **控制任务的 42% 伪影率**：这个数字在不同模型/架构之间是否稳定？MoE（Qwen3）和 Dense（Gemma）架构的伪影率是否有系统差异？\n\n5. **Figure 缺失**：是否有技术原因导致无法生成图表？23 个表格的论文即使对审稿人也非常难以消化。\n\n6. **\"负面结果 + 方法论\"定位**：作者是否考虑过将论文重新定位为以控制任务方法论为核心（正面贡献），辅以负面迁移结果作为案例研究？\n\n---\n\n## 8. Missing References / Related Work\n\n- **断裂引用**：Page 1 出现多处 \"??\"，无法核实声称的先行工作。这是最严重的引用问题。\n- **缺失的关键引用**：\n  - Guo et al. (2017) \"On Calibration of Modern Neural Networks\" — 校准领域的奠基工作\n  - Desai & Durrett (2020) \"Calibration of Pre-trained Transformers\" — 直接相关的校准+LLM 工作\n  - Conneau et al. (2020) \"Emerging Cross-lingual Structure in Pretrained Language Models\" — 跨语言表示结构的经典工作\n  - Hewitt & Liang (2019) \"Designing and Interpreting Probes with Control Tasks\" — 论文方法论的核心依赖，需要确认是否在断裂引用中\n  - 近期的 Probing 综述文献\n\n---\n\n## 9. Experiment Coverage Assessment\n\n对照设计文档中的 13 个实验计划：\n\n| # | 实验 | 是否涵盖 | 位置 |\n|---|------|----------|------|\n| 1 | Depth-transferability Pareto (Qwen3-235B) | ✅ | Table 1, Section 5.1 |\n| 2 | Depth-transferability Pareto (Llama 4 Scout) | ✅ | Table 1, Section 5.1 |\n| 3 | Depth-transferability Pareto (Gemma 4 31B) | ✅ | Table 1/Table 20, Section 5.1 |\n| 4 | CaCLR sweep | ✅ | Table 3, Section 5.2 |\n| 5 | Difficulty decomposition ablation | ✅ | Table 9, Section 5.4 |\n| 6 | CKA geometric analysis (Simpson's Paradox) | ✅ | Table 6-7, Section 5.3 |\n| 7 | Control tasks / selectivity | ✅ | Table 10-11, Section 5.5 |\n| 8 | Linear projection (5 conditions) | ✅ | Table 13/21, Section 5.6 |\n| 9 | Cross-benchmark generalization | ✅ | Table 16, Section 5.7 |\n| 10 | Probe complexity comparison | ✅ | Table 17, Section 5.8 |\n| 11 | Quantization validation | ✅ | Table 18/22, Section 5.8 |\n| 12 | Extended language coverage (52 lang) | ✅ | Table 19, Appendix A |\n| 13 | Cross-lingual orthogonality | ✅ | Table 23, Section 5.9 |\n\n**覆盖率：13/13 (100%)**。所有实验计划均已执行。但多数实验的报告存在上述质量问题（低 EN AUROC 混淆、缺乏误差线/置信区间等）。\n\n---\n\n## 10. \"负面结果 + 方法论\"定位评估（EACL 适配性）\n\n**部分令人信服，但不足以支撑接收。** 具体分析：\n\n- **负面结果维度**：论文的实验规模确实大（3 架构 × 20 语言 × 5 条件），如果负面结论成立，对社区有重要价值。但 N1（低 EN AUROC）和 N2（量化混淆）两个未解决的 confound 意味着读者无法确信这些是真正的\"limits\"还是实验设计的局限。一篇好的负面结果论文需要排除替代解释——本文未做到。\n\n- **方法论维度**：将 Hewitt & Liang 控制任务引入跨语言探针文献是真实的贡献（Section 5.5），42% 伪影率发现意义重大。但这一贡献在当前论文结构中是从属地位（第 5 个子节），且仅占约 1 页篇幅。如果以此为核心重写论文，excitement 评分会显著提升。\n\n- **EACL 适配性**：EACL 欢迎负面结果和资源型论文，但仍要求 soundness。当前版本的 soundness 不足以通过 EACL 的审稿标准。\n\n---\n\n## 11. 主要优势\n\n1. **实验规模**：3 种架构（含 MoE 和 Dense）、20 种语言、5 种迁移条件——这是目前跨语言探针迁移文献中规模最大的研究。\n2. **诚实的负面结果报告**：论文没有试图美化结果，Section 5.1-5.4 的每个负面发现都有明确的数字支撑。\n3. **控制任务方法论**：首次将 selectivity-based control tasks 应用于跨语言探针，42% LOW 伪影率是有价值的发现。\n4. **丰富的 Appendix**：逐语言、逐层的完整结果（Table 10-23），支持独立验证。\n5. **52 语言扩展**：Table 19 将核心发现从 20 语言扩展到 52 语言，增强了泛化性声明。\n6. **Limitations 段落**（Section 6 末尾）坦诚地列出了 4 个限制，包括 MoE 架构的不确定性和 quantization 的影响。\n\n---\n\n## 12. Confidence\n\n**Confidence: 4/5** — 我对跨语言表示学习和探针方法论领域较为熟悉，已完整阅读论文全部 14 页及所有 23 个表格。对核心混淆因素的判断有较高把握。\n\n---\n\n## 13. 最终判断\n\n**Reject (2/5)**。论文方向有价值、规模可观，但两个关键混淆因素（低 EN AUROC、深层量化偏差）未被解决，使得\"基本限制\"的核心声明不可信。排版问题（\"??\" 断引、零图表）加剧了可读性困难。建议：(1) 以控制任务方法论为核心重写；(2) 解决 EN AUROC 混淆（至少讨论，最好做消融）；(3) 修复引用并添加关键图表；(4) 扩充 Related Work。在这些修改后，论文有潜力达到 EACL 的接收标准。",
    "reviewer_id": "1",
    "project": "xling_calib_direction"
  }
}
```

</details>

---

### Tool result

_source line 189 · 2026-05-21T14:05:25.544730+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4020
}
```

</details>

---

### Tool call

_source line 190 · 2026-05-21T14:05:31.623798+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
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

_source line 191 · 2026-05-21T14:05:31.674326+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 192 · 2026-05-21T14:05:36.742899+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images"
  }
}
```

</details>

---

### Tool result

_source line 193 · 2026-05-21T14:05:36.843501+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 100
}
```

</details>

---

### Assistant

_source line 194 · 2026-05-21T14:05:43.183686+00:00_

Worst paper 综合审稿报告已提交。评分 Overall 2/5 (Reject)，核心问题：(1) 低 EN AUROC (0.715-0.742) 系统混淆因素、(2) 深层量化偏差与 Pareto 负面结论重叠、(3) 多处 "??" 断引+零图表。实验覆盖率 13/13，但方法论贡献（控制任务 42% 伪影率）被埋没在论文结构中。建议以控制任务为核心重写。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1"
}
```

</details>

---
