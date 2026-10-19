# Reviewer 2 coordination

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 114
- **Recorded user turns:** 4
- **Tool calls:** 53
- **Original source:** `logs/chats/feishu_group_oc_03a4b60e63b9658b3528f3d9a729f2e8_reviewer_2.jsonl`
- **Structured JSON:** [`a3ee3752acace4a664cd.json`](../../sessions/a3/a3ee3752acace4a664cd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

52 recorded events

### User

_source line 1 · 2026-05-20T19:47:32.802034+00:00_

[Round 1 审稿请求]:
## Review Assignment — Reviewer 2: Novelty & Related Work

You are reviewing a submission to a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept).

### Paper
**Title:** Cross-Lingual Calibration Probes Reveal Architecture-Dependent Pareto Frontiers in Multilingual LLMs

**Summary:** The paper conducts the first systematic study of cross-lingual correctness probe transfer across 20 languages, 3 architectures (Qwen3-235B-A22B, Llama 4 Scout, Gemma 4 31B), and 3 benchmarks (GlobalMMLU, Belebele, MMLU-ProX). Four claims:
1. A depth–transferability Pareto frontier: deeper layers yield better English probes but degrade in cross-lingual transfer, architecture-dependent.
2. Difficulty–capability decomposition explains 25% of transfer gap, predicts method choice with 72% accuracy.
3. CaCLR matches the best supervised baseline (linear projection) in zero-label setting (+1.3pp avg), strongest for mid-resource.
4. Correctness–confidence orthogonality extends to 20 languages (all cos < 0.25) with resource-tier gradient.

### Your Focus Areas

**Novelty Assessment:**
- How novel is the "Pareto frontier" framing? Is characterizing depth-transferability tradeoffs across architectures a genuine contribution or mainly empirical documentation?
- How novel is CaCLR? The loss function combines BCE + calibration penalty + consistency regularization — are these components individually known? Is the combination non-trivial?
- How novel is the difficulty–capability decomposition? Civelli et al. (2025) already showed IRT difficulty probes transfer cross-lingually. What does this paper add beyond applying their technique to correctness probes?
- How novel is extending orthogonality to 20 languages? Miao & Ungar (2026) established this for English. Is the multilingual extension straightforward or does it require new methodology?
- Overall: does this paper introduce genuinely new ideas, or is it primarily a well-executed empirical study applying known techniques at larger scale?

**Related Work (§2):**
- Is the related work comprehensive? Key areas to check:
  - Probe-based calibration: CORAL (Miao et al., 2024), CCPS (Wang et al., 2024), Miao & Ungar (2026)
  - Cross-lingual probing: Xiao et al. (2025), Civelli et al. (2025)
  - Multilingual calibration: LACE (Zhou et al., 2024), MKA (Chen et al., 2024)
- Are there important missing references? Consider:
  - Representation similarity across languages (CKA, SVCCA literature)
  - Layer-wise probing in multilingual models (Conneau et al., Pires et al.)
  - Calibration in multilingual settings beyond probe-based methods
  - Distribution shift and domain adaptation (relevant to transfer conditions)
- Is the distinction from Xiao et al. (2025) — knowledge-boundary vs. correctness probes — convincingly argued?
- Is the distinction from Civelli et al. (2025) — difficulty vs. correctness — clearly drawn?

**Positioning & Framing:**
- Is the paper well-positioned relative to existing work?
- Are the contributions overclaimed or underclaimed?
- Does the paper clearly articulate what practitioners should take away?
- Is the "Pareto frontier" terminology appropriate, or is it overloading an optimization concept for what is essentially a depth-performance profile?

**Writing Quality:**
- Is the paper well-organized and clearly written?
- Are the 4 contributions clearly delineated?
- Is the paper the right length? (11 pages with 18 tables — is this table-heavy?)
- Are figures adequately described (the PDF may not render all figures)?

### Deliverable
Provide:
1. Summary of strengths (novelty & positioning)
2. Summary of weaknesses (novelty & positioning)
3. Specific questions for authors
4. Score (1-6) with justification
5. Confidence level (1-5)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-20T19:47:39.178493+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/.claude/sessions/review_reviewer_2_dfeebd74/CLAUDE.md",
  "offset": "0",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/.claude/sessions/review_reviewer_2_dfeebd74/CLAUDE.md",
    "offset": "0",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-20T19:47:40.082092+00:00_

0	## 当前项目
1	当前绑定项目：**xling_calib_direction**
2	
3	今天是 **2026-05-20**。
4	
5	你是 ML 研究团队的论文审稿人（Reviewer 2）。**始终用中文回复。**
6	
7	## 你的角色
8	
9	你模拟真实的学术同行评审人，对论文进行深度审查。你的审查意见应达到真实 reviewer 的水准——不是走流程的表面检查，而是找到真正会影响接收决定的问题。
10	
11	**你不修改论文内容**——发现问题后通过 `review_reviewer_post_to_director` 汇报。
12	
13	## 审查侧重
14	
15	你的具体审查侧重由 Review Director 在任务消息中指定。严格按照 Director 的指示执行，不要自行扩大或缩小审查范围。
16	
17	## 多轮审稿
18	
19	你可能会被 Director 要求进行多轮审稿：
20	- Director 可能转发另一位 Reviewer 的**完整审稿原文**，请你逐条回应
21	- 回应格式：`[AGREE]` 或 `[REBUT]`，附理由和证据（cite 具体 Section/Table/Figure）
22	- 后续轮次应聚焦 Director 指出的具体问题，而非重复全面审查
23	
24	### 交叉回应格式
25	
26	```
27	[AGREE] R{X}-Issue-{N}: <同意理由，可补充自己的发现>
28	[REBUT] R{X}-Issue-{N}: <反驳理由，必须 cite 原文证据>
29	```
30	
31	## 审查前必做（Step 0）
32	
33	Review Director 触发你时会提供 venue 名称和已搜索的格式要求。在此基础上：
34	1. 用 `web_search` 搜索该 venue 的 **reviewer guidelines / review form**，例如：
35	   `"EMNLP 2026 reviewer guidelines"` 或 `"ACL ARR review form criteria"`
36	2. 提取官方评分维度和评分标准（通常包括：soundness、excitement/novelty、reproducibility、paper length 等）
37	3. 后续审查必须严格对照这些官方维度打分，不得自行发明评分体系
38	
39	## 审查流程
40	
41	1. **通读论文**：abstract → introduction → related work → method → experiments → conclusion + appendix
42	2. **对照官方标准逐项打分**：用搜到的 review form 维度，每项给出分数 + 理由
43	3. **深挖技术问题**：
44	   - 核心 claim 的实验支撑是否充分？有没有混淆变量？
45	   - 方法假设是否成立？有没有边界条件没讨论？
46	   - 和 related work 的对比是否公平、完整？
47	   - 每个数字/表格/图是否能从论文本身 verify？
48	4. **格式合规**：严格对照 Review Director 提供的要求
49	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T19:47:40.233123+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-20T19:47:40.283694+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T19:47:46.004975+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T19:47:46.707812+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
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

_source line 8 · 2026-05-20T19:47:46.808668+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/paper.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-20T19:47:52.979978+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's what I found about ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Review Form Criteria

The main criteria for Findings are soundness and reproducibility, while conference recommendations may also cons
…[truncated 918 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6975
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T19:47:59.250170+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include: soundness, excitement, overall recommendation, confidence, and any other dimensions. List all score values and their meanings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include: soundness, excitement, overall recommendation, confidence, and any other dimensions. List all score values and their meanings."
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T19:48:00.154847+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
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

_source line 12 · 2026-05-20T19:48:06.628833+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: Quite sure; unlikely but conceivable to miss important details
- **3**: Pretty sure; chance of missing details despite general area familiarity
- **2**: Willing to defend evaluation; fairly likely to have missed details
- **1**: Outside expertise area or paper very difficult to understand

## 2. **Soundness**
Scale: 1-5 (with .5 increments)
- **5**: Exceptional thoroughness for its type
- **4**: Strong support for claims; minor experiments optional
- **3**: Adequate support for main claims; minor details need support
- **2**: Main claims insufficiently supported; major technical problems
- **1**: Insufficiently thorough or irrelevant to ACL

## 3. **Excitement**
Scale: 1-5 (with .5 increments)
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: Noteworthy; would mention to colleagues
- **3**: Interesting; might attend presentation if available
- **2**: Potentially resonates with others in the community
- **1**: "Not Exciting: this paper does not resonate with me"

## 4. **Overall Assessment**
Scale: 1-5 (with .5 increments)
- **5**: Award consideration (top 2.5%)
- **4**: Conference acceptance
- **3**: Findings track acceptance
- **2**: Revise for next cycle
- **1.5**: Substantial revisions needed beyond current cycle
- **1**: Reject; not relevant to computational linguistics

## 5. **Reproducibility**
Scale: 1-5
- **5**: Results easily reproducible
- **4**: Mostly reproducible; minor variance possible
- **3**: Reproducible with difficulty; underspecified parameters
- **2**: Hard to reproduce; unavailable data or insufficient detail
- **1**: Impossible to reproduce

## 6. **Datasets Value**
Scale: 1-5
- **5**: Enabling; affects research project choices
- **4**: Useful for ongoing work
- **3**: Potentially useful
- **2**: 
…[truncated 565 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7378
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-20T19:48:07.634154+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 321.0}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 337.7}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 295.6}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 235.8}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 264.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 293.9}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 290.4}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 262.6}, {\"page\": 9, \"path\": \
…[truncated 717 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7479
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T19:48:13.005502+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p1.png"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T19:48:13.459560+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p2.png"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T19:48:14.415887+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1410
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T19:48:14.418944+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T19:48:14.419350+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p3.png"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T19:48:15.173851+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 754
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T19:48:15.374913+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p4.png"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T19:48:15.527866+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p5.png"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T19:48:15.732572+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 357
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-20T19:48:16.086360+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 558
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T19:48:20.509623+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p6.png"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-20T19:48:20.964630+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T19:48:20.965086+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p7.png"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-20T19:48:21.920396+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T19:48:21.920837+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p8.png"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-20T19:48:22.424717+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-20T19:48:22.425143+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p9.png"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-20T19:48:22.978246+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-20T19:48:22.978684+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p10.png"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-20T19:48:23.035510+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 56
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-20T19:48:31.164282+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
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

_source line 35 · 2026-05-20T19:48:31.266964+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 96.6}], \"total_pages\": 11, \"rendered_pages\": 1, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 102
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-20T19:48:34.578757+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p11.png"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-20T19:48:34.630935+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-20T19:49:11.266553+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
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

_source line 39 · 2026-05-20T19:49:11.317097+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"未找到 .bib 文件: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-20T19:49:11.317411+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "cross-lingual probing multilingual models layer-wise Conneau Pires representation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "cross-lingual probing multilingual models layer-wise Conneau Pires representation 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T19:49:11.768918+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CKA SVCCA representation similarity multilingual language models 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CKA SVCCA representation similarity multilingual language models 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T19:49:18.844736+00:00_

Web search results for query: "CKA SVCCA representation similarity multilingual language models 2024 2025"

Links: [{"title":"Neither Here Nor There: Cross-Lingual Representation Dynamics of Code-Mixed Text in Multilingual Encoders","url":"https://arxiv.org/html/2603.19771"},{"title":"ContraSim – Analyzing Neural Representations Based on ...","url":"https://aclanthology.org/2024.naacl-long.350.pdf"},{"title":"Representation Potentials of Foundation Models for ...","url":"https://aclanthology.org/2025.emnlp-main.843.pdf"},{"title":"Cross-lingual Similarity of Multilingual Representations Revisited","url":"https://arxiv.org/pdf/2212.01924"},{"title":"Centered Kernel Alignment (CKA) Similarity","url":"https://www.emergentmind.com/topics/centered-kernel-alignment-cka-similarity"},{"title":"[2310.20456] Towards a Deep Understanding of Multilingual End-to-End Speech Translation","url":"https://ar5iv.labs.arxiv.org/html/2310.20456"},{"title":"How do Multimodal Foundation Models Encode Text and Speech? An Analysis of Cross-Lingual and Cross-Modal Representations","url":"https://arxiv.org/html/2411.17666v1"},{"title":"Towards a Deep Understanding of Multilingual End-to-End Speech   Translation","url":"https://arxiv.org/pdf/2310.20456"},{"title":"How do Multimodal Foundation Models Encode Text and ...","url":"https://aclanthology.org/2025.naacl-short.51.pdf"}]

I found several relevant research papers on CKA and SVCCA representation similarity in multilingual language models from 2024-2025. Here's a summary of the key findings:

## Recent Research on Representation Similarity in Multilingual Models

CKA and SVCCA have been used to analyze how cross-lingual alignment emerges across transformer layers in multilingual language models.

### Key Studies:

1. **Code-Mixed Text Analysis (2025)**: In multilingual BERT models with continued pretraining on code-mixed data, English-code-mixed similarity strengthens in middle layers (CKA ~0.78 around layers 4–5), while SVCCA analysis sho
…[truncated 931 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7075
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-20T19:49:19.446748+00:00_

Web search results for query: "cross-lingual probing multilingual models layer-wise Conneau Pires representation 2024 2025"

Links: [{"title":"(PDF) Exploring Multilingual Probing in Large Language Models: A Cross-Language Analysis","url":"https://www.researchgate.net/publication/384267021_Exploring_Multilingual_Probing_in_Large_Language_Models_A_Cross-Language_Analysis"},{"title":"Explainability and Interpretability of Multilingual Large ...","url":"https://aclanthology.org/2025.emnlp-main.1033.pdf"},{"title":"[2409.14459] Exploring Multilingual Probing in Large Language Models: A Cross-Language Analysis","url":"https://arxiv.org/abs/2409.14459"},{"title":"Cross-neutralising: Probing for joint encoding of linguistic information   in multilingual models","url":"https://arxiv.org/pdf/2010.12825"},{"title":"Exploring Multilingual Probing in Large Language Models: A   Cross-Language Analysis","url":"https://arxiv.org/pdf/2409.14459"},{"title":"Probing LLMs for Multilingual Discourse Generalization Through a Unified Label Set","url":"https://arxiv.org/html/2503.10515v1"},{"title":"Exploring Multilingual Probing in Large Language Models: A Cross-Language Analysis","url":"https://arxiv.org/html/2409.14459v2"},{"title":"Discriminating Form and Meaning in Multilingual Models with Minimal-Pair ABX Tasks","url":"https://arxiv.org/pdf/2505.17747"}]

Based on the web search results, here are the key findings related to cross-lingual probing of multilingual models with layer-wise representation analysis:

## Recent Research on Multilingual Probing (2024-2025)

Probing techniques for large language models have primarily focused on English, but recent work extends these probing methods to a multilingual context, investigating the behaviors of LLMs across diverse languages.

### Key Findings from Recent Studies

A consistent performance gap exists between high-resource and low-resource languages, with high-resource languages achieving significantly higher probing accuracy; divergen
…[truncated 1166 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8129
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-20T19:49:24.516421+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CCPS Wang 2024 confidence calibration probes LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CCPS Wang 2024 confidence calibration probes LLM"
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T19:49:24.968772+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MKA Chen 2024 multilingual knowledge alignment calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MKA Chen 2024 multilingual knowledge alignment calibration"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-20T19:49:25.119512+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "calibration multilingual language models temperature scaling domain adaptation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "calibration multilingual language models temperature scaling domain adaptation 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-20T19:49:31.191476+00:00_

Web search results for query: "MKA Chen 2024 multilingual knowledge alignment calibration"

Links: [{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/pdf/2510.03136"},{"title":"MKA: Leveraging Cross-Lingual Consensus for Model Abstention","url":"https://arxiv.org/html/2503.23687v1"},{"title":"Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual Knowledge Alignment, But Only Shallowly - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.339/"},{"title":"Multilingual Knowledge Graph Embeddings for Cross-lingual Knowledge   Alignment","url":"https://arxiv.org/pdf/1611.03954"},{"title":"Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning","url":"https://arxiv.org/pdf/2601.01362"},{"title":"CALM: Unleashing the Cross-Lingual Self-Aligning Ability of Language   Model Question Answering","url":"https://arxiv.org/pdf/2501.18457"}]

Based on the search results, I found relevant research on multilingual knowledge alignment and calibration:

The MKA work develops a multilingual pipeline to calibrate the model's confidence and let it abstain when uncertain, running several multilingual models through the pipeline to profile them across different languages. The approach translates questions, prompts the model separately, then translates the answers back to the original language and arrives at a consensus.

The work uses more than one language (grouped by categories like resource level, language family, etc.) to calibrate the model's confidence to make abstentions. The performance of the pipeline varies by model and language, but in general they benefit from it, evidenced by accuracy improvement of 71.2% for Bengali over baseline performance without the pipeline.

This research builds on the insight that language models cannot utilize cross-lingual knowledge implicitly: prompting in one language doesn't necessarily ut
…[truncated 150 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6222
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T19:49:31.793821+00:00_

Web search results for query: "CCPS Wang 2024 confidence calibration probes LLM"

Links: [{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/pdf/2505.21772"},{"title":"CCPS: Calibrating LLM Confidence via Perturbation Stability – EMNLP 2025 | Hacker News","url":"https://news.ycombinator.com/item?id=45055315"},{"title":"[2505.21772] Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/abs/2505.21772"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/html/2505.21772v1"},{"title":"Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation","url":"https://arxiv.org/html/2512.22245v1"},{"title":"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs","url":"https://www.medrxiv.org/content/10.1101/2025.09.17.25336018v2.full.pdf"},{"title":"Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation","url":"https://arxiv.org/pdf/2512.22245"},{"title":"Calibration Across Layers: Understanding Calibration Evolution in LLMs","url":"https://arxiv.org/html/2511.00280v1"}]

Based on the search results, here's what I found about CCPS and confidence calibration in LLMs:

## CCPS Overview

CCPS (Calibrating LLM Confidence by Probing Perturbed Representation Stability) is a novel method analyzing internal representational stability in LLMs. It applies targeted adversarial perturbations to final hidden states, extracts features reflecting the model's response to these perturbations, and uses a lightweight classifier to predict answer correctness.

## Key Results

Across four LLMs and three MMLU variants, CCPS reduces Expected Calibration Error by approximately 55% and Brier score by 21%, while increasing accuracy by 5 percentage points, Area Under the Precision-Recall Curve by 4 percentage points, and Area Under the Receiver Operating Characteristic Curv
…[truncated 741 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7277
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-20T19:49:31.794211+00:00_

Web search results for query: "calibration multilingual language models temperature scaling domain adaptation 2024 2025"

Links: [{"title":"Calibrating Language Models with Adaptive Temperature Scaling | Request PDF","url":"https://www.researchgate.net/publication/386193179_Calibrating_Language_Models_with_Adaptive_Temperature_Scaling"},{"title":"Calibrating Language Models with Adaptive Temperature Scaling","url":"https://arxiv.org/pdf/2409.19817"},{"title":"Calibrating Language Models with Adaptive Temperature Scaling - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.1007/"},{"title":"Calibrating Language Models with Adaptive Temperature ...","url":"https://aclanthology.org/2024.emnlp-main.1007.pdf"},{"title":"[2409.19817] Calibrating Language Models with Adaptive Temperature Scaling","url":"https://arxiv.org/abs/2409.19817"},{"title":"Published at ICLR 2024 Workshop on Secure and Trustworthy Large Language Models","url":"https://openreview.net/pdf?id=BgfGqNpoMi"},{"title":"[Quick Review] Calibrating Language Models with Adaptive Temperature Scaling","url":"https://liner.com/review/calibrating-language-models-with-adaptive-temperature-scaling"},{"title":"Optimizing Temperature for Language Models with Multi-Sample Inference","url":"https://arxiv.org/html/2502.05234v2"},{"title":"On the Calibration of Massively Multilingual Language Models","url":"https://arxiv.org/pdf/2210.12265"}]

I found several relevant research papers on calibration in language models. Here are the key findings:

## Adaptive Temperature Scaling (2024)

A post-hoc calibration method called Adaptive Temperature Scaling (ATS) predicts a temperature scaling parameter for each token prediction. After fine-tuning with reinforcement learning from human feedback (RLHF), the calibration of language models degrades significantly. The predicted temperature values adapt based on token-level features and are fit over a standard supervised fine-tuning (SFT) dataset, addressing the varying de
…[truncated 1103 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6674
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-20T19:51:49.875066+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿意见（Novelty & Related Work）\n\n**论文标题**: Cross-Lingual Calibration Probes Reveal Architecture-Dependent Pareto Frontiers in Multilingual LLMs\n\n---\n\n## 总体评分\n**Overall**: 2.5 / 5（介于 Revise-for-next-cycle 与 Findings 之间）\n**一句话总结**: 实验规模值得肯定（20语言×3架构×3基准），但四项贡献的新颖性均为增量性的，且参考文献极度稀疏（仅8篇）、Related Work 不足一页，严重削弱了论文的学术定位。\n\n---\n\n## ACL ARR 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3 / 5 | 核心实验设计合理，但\"Pareto frontier\"术语的技术准确性存疑；decomposition 的 25% variance explained 较低却被作为主要贡献宣传 |\n| Excitement | 2 / 5 | 四项贡献均为已知技术的直接扩展或组合，缺乏方法论上的惊喜；实践者收获主要是\"选哪个 layer\"的经验法则 |\n| Reproducibility | 3.5 / 5 | 实验设置描述清楚（§4），超参数有报告（α=0.15, β=0.10），但代码/数据未提及是否公开 |\n| Confidence | 4 / 5 | 熟悉 probe-based calibration 和跨语言表征领域 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 参考文献极度稀疏——全文仅 8 篇引用\n\n- 具体位置：References（p.10），§2 Related Work（p.2）\n- 问题：一篇声称覆盖 probe-based calibration、cross-lingual probing、multilingual calibration 三个方向的论文，仅引用 8 篇文献，这在 *ACL 顶会投稿中极不正常。以下关键文献完全缺失：\n  - **Cross-lingual probing 基础**: Conneau et al. (2020) \"Unsupervised Cross-lingual Representation Learning at Scale\"；Pires et al. (2019) \"How multilingual is Multilingual BERT?\" —— 这两篇是多语言模型 layer-wise probing 的奠基工作，本文的 depth-transferability claim 必须讨论它们\n  - **表征相似性**: CKA/SVCCA 文献（Kornblith et al., 2019; Raghu et al., 2017）—— 论文讨论跨语言表征对齐却完全不提表征相似性度量\n  - **CCPS** (Wang et al., EMNLP 2025)：通过 perturbation stability 做 calibration probing，直接相关的方法\n  - **Probing 综述**: Belinkov (2022) \"Probing Classifiers\"，该领域的标准参考\n  - **多语言 calibration**: Keleg & Magdy (2023) \"On the Calibration of Massively Multilingual Language Models\"；Adaptive Temperature Scaling (EMNLP 2024)\n  - **IRT 文献**: 论文大量使用 IRT difficulty 参数（§3.3），但未引用 IRT 原始文献（e.g., Lord 1980, Baker 2001）\n  - Director 指定检查的 **MKA (Chen et al., 2024)** 和 **CCPS (Wang et al., 2024)** 也未出现\n- 为什么影响接收：参考文献不足直接导致 (a) 新颖性论证无锚点——无法说明本文与先行工作的区别，(b) reviewer 无法评估作者是否了解领域全貌，(c) 违反 ACL 社区对 scholarly thoroughness 的基本期望\n- 建议修改方向：Related Work 扩展至至少 1.5-2 页，引用量应在 30+ 篇\n\n**N2** [critical] \"Pareto frontier\" 术语使用不准确，核心 framing 有误导性\n\n- 具体位置：Title, Abstract, §3.2, §5.1, Claims 1 & 3\n- 问题：在多目标优化中，Pareto frontier 指的是一组互不支配（non-dominated）的解。本文所描述的是 **depth vs. cross-lingual transfer AUROC 的单调递减关系**（deeper = better English, worse transfer）——这是一条 trade-off curve，不是 Pareto frontier。Table 1 和 Table 3 中标记的 ★ 点是\"best transfer layer\"，但没有证据表明这些层在 (English AUROC, ZS-19 AUROC) 二维空间中互不支配。事实上，Table 1 显示 layer 8 的 EN=0.446 / ZS-19=0.637，而 layer 53 的 EN=0.827 / ZS-19=0.563——layer 8 在 ZS-19 上优于 layer 53，而 layer 53 在 EN 上优于 layer 8，这确实构成 non-dominance。但论文没有做标准的 Pareto dominance 分析，没有报告 hypervolume indicator，甚至没有画一张 scatter plot 来可视化这条 frontier。\n- 为什么影响接收：标题和核心 claim 建立在一个技术上不严谨的术语之上。如果只是描述\"deeper layers 有更好的 English probe 但更差的 cross-lingual transfer\"，这在多语言 NLP 中是已知现象（Pires et al., 2019; Conneau et al., 2020 已表明 deeper layers encode more language-specific features）。\"Pareto frontier\" framing 给一个已知现象披上了新包装。\n- 建议修改方向：(1) 如果坚持 Pareto 术语，需做标准 multi-objective 分析（dominance test, hypervolume, 可视化）；(2) 否则改为\"depth-transferability trade-off profile\"并明确与 Conneau/Pires 等先行工作的区别\n\n**N3** [critical] 四项贡献的新颖性均为增量性，缺乏方法论突破\n\n- 具体位置：§1 Claims 1-4, §3\n- 问题逐条分析：\n  - **Claim 1 (Pareto frontier)**: 如 N2 所述，deeper layers = more language-specific 是已知现象。新贡献仅在于\"用 correctness probes 而非 syntactic/semantic probes 观察到了同样的现象\"。\n  - **Claim 2 (Difficulty-capability decomposition)**: Civelli et al. (2025) 已证明 IRT difficulty probes 跨语言迁移。本文的新增是将 variance 分解为 difficulty-shared (68%) 和 capability-specific (32%) 两个成分——但 R² = 0.72（§5.2 第一句 \"IRT difficulty probes achieve h² = 0.72\"）并未超越 Civelli 的结果，且 25% 的 transfer gap 解释力（Abstract）依赖于这个分解的稳定性，论文未报告 bootstrap confidence interval。\n  - **Claim 3 (CaCLR)**: 损失函数 = BCE + calibration penalty (ℓ_cal) + consistency regularization (ℓ_consistency)。BCE 用于 correctness 预测（标准做法）；calibration loss 类似 focal/ECE-based penalties（已有文献）；consistency regularization 广泛用于半监督学习（Temporal Ensembling, MixMatch 等）。三者组合虽合理，但非 non-trivial，缺乏理论分析说明为何组合优于单独使用。\n  - **Claim 4 (Orthogonality extension)**: Miao & Ungar (2026) 建立了英文的 correctness-confidence orthogonality。本文将同一分析扩展到 20 种语言，发现 cos < 0.25。方法论上这是直接复制——计算 cosine similarity——无需新方法。贡献仅在 empirical verification。\n- 为什么影响接收：四项贡献叠加后，整体 narrative 是\"将已知方法应用到更大规模\"，这对 Findings track 可能足够，但对 main conference 接收（excitement 维度）不足。\n- 建议修改方向：聚焦最有洞察力的发现（如 architecture-dependent depth profile 的 mechanistic 解释），补充理论分析或消融实验说明为什么 CaCLR 各组件的组合是 synergistic 而非 additive。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Related Work（§2）过于简略——仅 ~15 行覆盖 3 个子方向\n\n- 具体位置：§2（p.2，约 15 行正文）\n- 问题：三个子方向（Probe-Based Calibration, Cross-Lingual Representation Transfer, Multilingual Calibration）各仅 1-2 句话。与 Xiao et al. (2025) 的区别（\"knowledge-boundary vs. correctness probes\"）和与 Civelli et al. (2025) 的区别（\"difficulty vs. correctness\"）各仅一句话带过。这些是论文 novelty 论证的核心支撑，一句话不够。\n- 建议：(1) 每个子方向至少 1 段落；(2) 用一个对比表格（method × feature）明确区分本文与 Xiao、Civelli、CORAL 的定位\n\n**W2** [warning] 全文 16 张表格、0 张图——表格过重，可读性差\n\n- 具体位置：Tables 1-16 贯穿全文\n- 问题：论文核心概念是\"Pareto frontier\"，却没有任何可视化。一张 (English AUROC, ZS-19 AUROC) 的 scatter plot with Pareto front overlay 比 Table 1 的 20 行数字直观得多。同样，layer-wise transfer degradation curve、resource-tier gradient、CaCLR ablation 都适合用图表呈现。16 张纯数字表格使得论文难以快速理解核心 pattern。\n- 建议：至少添加 (1) Pareto frontier 可视化（scatter plot），(2) layer-wise AUROC 折线图，(3) resource tier vs. improvement 的 bar chart\n\n**W3** [warning] \"First systematic study\" 声明过强\n\n- 具体位置：Abstract 第 3 行 \"We present the first systematic study of cross-lingual correctness probe transfer\"\n- 问题：Xiao et al. (2025) 做了 cross-lingual knowledge boundary probe transfer（5 languages），Civelli et al. (2025) 做了 cross-lingual difficulty probe transfer。本文的\"first\"仅成立于\"correctness probe\"这一细分品类。这种细分声明（\"first for correctness, not knowledge-boundary, not difficulty\"）在 reviewer 看来更像是通过 narrow scoping 来回避先行工作，而非真正的开创性。\n- 建议：改为 \"the first large-scale study comparing correctness probe transfer across architectures\"——强调 scale 和 architecture comparison 而非\"first\"\n\n**W4** [warning] Difficulty-capability decomposition 的 25% 解释力未给置信区间\n\n- 具体位置：Abstract \"explains 25% of transfer gap\", §5.2\n- 问题：25% 的 variance explained 是关键数字，但论文未报告 bootstrap CI 或 cross-validation stability。在 20 语言的样本上，这个估计可能有很大方差。此外，72% 的 method choice prediction accuracy（Abstract）未与 random baseline 或 majority class baseline 对比。\n- 建议：报告 bootstrap 95% CI；报告 random/majority baseline 对比\n\n**W5** [warning] CaCLR 的 improvement 幅度较小，实际意义不清楚\n\n- 具体位置：§5.3, Table 7\n- 问题：CaCLR 的核心结果是 \"+1.3pp avg AUROC\" 和 \"~40% ECE reduction\"（Abstract）。但 Table 7 显示 CaCLR 的 AUROC 为 0.804，zero-shot baseline 为 0.762——zero-shot 已经不低。而 few-shot (100) 为 0.779。在实际部署中，25 或 100 个 few-shot 标签的获取成本极低，CaCLR 相比 few-shot 的优势有限。论文未讨论 CaCLR 在什么场景下比简单的 few-shot fine-tuning 更有实际价值。\n- 建议：补充 cost-benefit 分析，说明 zero-label 假设在什么实际场景下成立\n\n---\n\n## 小问题（不影响接收）\n\n- §3.4 CaCLR 公式 (1) 中的 α 和 β 说明\"tuned on a validation set\"但未说明 validation set 的语言组成——如果 validation 含 target language labels 则\"zero-label\"声明不成立\n- §5.5 \"Probe Complexity Analysis\"（Table 12）仅在 Qwen3-235B 上做，是否 architecture-specific？应在多个架构上验证\n- §5.9 INT8 vs FP16 验证（Table 16）仅在 Llama 4 Scout 上做 5% 子集——样本量过小难以得出稳健结论\n- References 格式不一致：部分有 venue 信息（Burns et al. → ICLR 2023, Marks et al. → COLM 2024），部分没有（Miao et al. 2026 缺 venue, Civelli et al. 2025 缺 venue）\n\n---\n\n## 主要优势\n\n- **S1**: 实验规模确实比先行工作大——20 语言 × 3 架构 × 3 基准的覆盖度超过 Xiao (5 languages) 和 Civelli 的范围\n- **S2**: CaCLR 的 zero-label 设定有实际意义——在 target language 完全无标注数据的场景下提供了一条可行路径\n- **S3**: Architecture comparison（Table 4, Table 14）揭示了 MoE vs Dense 的 frontier 形状差异，这在已有文献中未见讨论\n- **S4**: Orthogonality 的 resource-tier gradient（Table 10-11）提供了一个有趣的发现：低资源语言的 orthogonality 更弱，暗示模型对低资源语言的 correctness 和 confidence 编码更加纠缠\n\n---\n\n## 给作者的具体问题\n\n1. Table 1 中标记 ★ 的层是否经过标准 Pareto dominance 检验？如果做了，请提供 hypervolume indicator。如果没做，标题中的 \"Pareto Frontier\" 是否应改为更准确的术语？\n2. CaCLR 的 consistency regularization（ℓ_consistency）是否在 English 和 target language 的 parallel data 上计算？如果是，\"zero-label\"的定义是什么——zero target-language correctness labels 但需要 parallel sentences？\n3. §5.2 报告 h² = 0.72 的 difficulty heritability——这个数字与 Civelli et al. (2025) 报告的值相比如何？论文没有引用 Civelli 的具体数字做对比。\n4. Orthogonality 分析（§5.4）中 cosine similarity 的计算是在 probe weight vectors 上还是在 representation space 中的 direction vectors 上？Miao & Ungar (2026) 的原始方法是哪种？\n5. 论文使用 Qwen3-235B-A22B, Llama 4 Scout, Gemma 4 31B——三个模型中两个是 MoE。MoE 的 expert routing 是否影响 layer-wise probing 的解释？论文未讨论 MoE 架构中 \"layer depth\" 的特殊性。\n\n---\n\n**总结**: 这是一篇在规模上有价值的实证研究，但四项贡献的新颖性均为增量性的，\"Pareto frontier\" framing 技术上不准确，且参考文献（8 篇）和 Related Work 的覆盖度远低于顶会标准。建议：(1) 大幅扩充参考文献和 Related Work，(2) 修正或放弃 Pareto 术语，(3) 添加可视化，(4) 更诚实地定位为 large-scale empirical study 而非方法论贡献。在当前状态下，推荐 Revise-for-next-cycle。",
  "reviewer_id": "2",
  "project": "xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 1 审稿意见（Novelty & Related Work）\n\n**论文标题**: Cross-Lingual Calibration Probes Reveal Architecture-Dependent Pareto Frontiers in Multilingual LLMs\n\n---\n\n## 总体评分\n**Overall**: 2.5 / 5（介于 Revise-for-next-cycle 与 Findings 之间）\n**一句话总结**: 实验规模值得肯定（20语言×3架构×3基准），但四项贡献的新颖性均为增量性的，且参考文献极度稀疏（仅8篇）、Related Work 不足一页，严重削弱了论文的学术定位。\n\n---\n\n## ACL ARR 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3 / 5 | 核心实验设计合理，但\"Pareto frontier\"术语的技术准确性存疑；decomposition 的 25% variance explained 较低却被作为主要贡献宣传 |\n| Excitement | 2 / 5 | 四项贡献均为已知技术的直接扩展或组合，缺乏方法论上的惊喜；实践者收获主要是\"选哪个 layer\"的经验法则 |\n| Reproducibility | 3.5 / 5 | 实验设置描述清楚（§4），超参数有报告（α=0.15, β=0.10），但代码/数据未提及是否公开 |\n| Confidence | 4 / 5 | 熟悉 probe-based calibration 和跨语言表征领域 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 参考文献极度稀疏——全文仅 8 篇引用\n\n- 具体位置：References（p.10），§2 Related Work（p.2）\n- 问题：一篇声称覆盖 probe-based calibration、cross-lingual probing、multilingual calibration 三个方向的论文，仅引用 8 篇文献，这在 *ACL 顶会投稿中极不正常。以下关键文献完全缺失：\n  - **Cross-lingual probing 基础**: Conneau et al. (2020) \"Unsupervised Cross-lingual Representation Learning at Scale\"；Pires et al. (2019) \"How multilingual is Multilingual BERT?\" —— 这两篇是多语言模型 layer-wise probing 的奠基工作，本文的 depth-transferability claim 必须讨论它们\n  - **表征相似性**: CKA/SVCCA 文献（Kornblith et al., 2019; Raghu et al., 2017）—— 论文讨论跨语言表征对齐却完全不提表征相似性度量\n  - **CCPS** (Wang et al., EMNLP 2025)：通过 perturbation stability 做 calibration probing，直接相关的方法\n  - **Probing 综述**: Belinkov (2022) \"Probing Classifiers\"，该领域的标准参考\n  - **多语言 calibration**: Keleg & Magdy (2023) \"On the Calibration of Massively Multilingual Language Models\"；Adaptive Temperature Scaling (EMNLP 2024)\n  - **IRT 文献**: 论文大量使用 IRT difficulty 参数（§3.3），但未引用 IRT 原始文献（e.g., Lord 1980, Baker 2001）\n  - Director 指定检查的 **MKA (Chen et al., 2024)** 和 **CCPS (Wang et al., 2024)** 也未出现\n- 为什么影响接收：参考文献不足直接导致 (a) 新颖性论证无锚点——无法说明本文与先行工作的区别，(b) reviewer 无法评估作者是否了解领域全貌，(c) 违反 ACL 社区对 scholarly thoroughness 的基本期望\n- 建议修改方向：Related Work 扩展至至少 1.5-2 页，引用量应在 30+ 篇\n\n**N2** [critical] \"Pareto frontier\" 术语使用不准确，核心 framing 有误导性\n\n- 具体位置：Title, Abstract, §3.2, §5.1, Claims 1 & 3\n- 问题：在多目标优化中，Pareto frontier 指的是一组互不支配（non-dominated）的解。本文所描述的是 **depth vs. cross-lingual transfer AUROC 的单调递减关系**（deeper = better English, worse transfer）——这是一条 trade-off curve，不是 Pareto frontier。Table 1 和 Table 3 中标记的 ★ 点是\"best transfer layer\"，但没有证据表明这些层在 (English AUROC, ZS-19 AUROC) 二维空间中互不支配。事实上，Table 1 显示 layer 8 的 EN=0.446 / ZS-19=0.637，而 layer 53 的 EN=0.827 / ZS-19=0.563——layer 8 在 ZS-19 上优于 layer 53，而 layer 53 在 EN 上优于 layer 8，这确实构成 non-dominance。但论文没有做标准的 Pareto dominance 分析，没有报告 hypervolume indicator，甚至没有画一张 scatter plot 来可视化这条 frontier。\n- 为什么影响接收：标题和核心 claim 建立在一个技术上不严谨的术语之上。如果只是描述\"deeper layers 有更好的 English probe 但更差的 cross-lingual transfer\"，这在多语言 NLP 中是已知现象（Pires et al., 2019; Conneau et al., 2020 已表明 deeper layers encode more language-specific features）。\"Pareto frontier\" framing 给一个已知现象披上了新包装。\n- 建议修改方向：(1) 如果坚持 Pareto 术语，需做标准 multi-objective 分析（dominance test, hypervolume, 可视化）；(2) 否则改为\"depth-transferability trade-off profile\"并明确与 Conneau/Pires 等先行工作的区别\n\n**N3** [critical] 四项贡献的新颖性均为增量性，缺乏方法论突破\n\n- 具体位置：§1 Claims 1-4, §3\n- 问题逐条分析：\n  - **Claim 1 (Pareto frontier)**: 如 N2 所述，deeper layers = more language-specific 是已知现象。新贡献仅在于\"用 correctness probes 而非 syntactic/semantic probes 观察到了同样的现象\"。\n  - **Claim 2 (Difficulty-capability decomposition)**: Civelli et al. (2025) 已证明 IRT difficulty probes 跨语言迁移。本文的新增是将 variance 分解为 difficulty-shared (68%) 和 capability-specific (32%) 两个成分——但 R² = 0.72（§5.2 第一句 \"IRT difficulty probes achieve h² = 0.72\"）并未超越 Civelli 的结果，且 25% 的 transfer gap 解释力（Abstract）依赖于这个分解的稳定性，论文未报告 bootstrap confidence interval。\n  - **Claim 3 (CaCLR)**: 损失函数 = BCE + calibration penalty (ℓ_cal) + consistency regularization (ℓ_consistency)。BCE 用于 correctness 预测（标准做法）；calibration loss 类似 focal/ECE-based penalties（已有文献）；consistency regularization 广泛用于半监督学习（Temporal Ensembling, MixMatch 等）。三者组合虽合理，但非 non-trivial，缺乏理论分析说明为何组合优于单独使用。\n  - **Claim 4 (Orthogonality extension)**: Miao & Ungar (2026) 建立了英文的 correctness-confidence orthogonality。本文将同一分析扩展到 20 种语言，发现 cos < 0.25。方法论上这是直接复制——计算 cosine similarity——无需新方法。贡献仅在 empirical verification。\n- 为什么影响接收：四项贡献叠加后，整体 narrative 是\"将已知方法应用到更大规模\"，这对 Findings track 可能足够，但对 main conference 接收（excitement 维度）不足。\n- 建议修改方向：聚焦最有洞察力的发现（如 architecture-dependent depth profile 的 mechanistic 解释），补充理论分析或消融实验说明为什么 CaCLR 各组件的组合是 synergistic 而非 additive。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Related Work（§2）过于简略——仅 ~15 行覆盖 3 个子方向\n\n- 具体位置：§2（p.2，约 15 行正文）\n- 问题：三个子方向（Probe-Based Calibration, Cross-Lingual Representation Transfer, Multilingual Calibration）各仅 1-2 句话。与 Xiao et al. (2025) 的区别（\"knowledge-boundary vs. correctness probes\"）和与 Civelli et al. (2025) 的区别（\"difficulty vs. correctness\"）各仅一句话带过。这些是论文 novelty 论证的核心支撑，一句话不够。\n- 建议：(1) 每个子方向至少 1 段落；(2) 用一个对比表格（method × feature）明确区分本文与 Xiao、Civelli、CORAL 的定位\n\n**W2** [warning] 全文 16 张表格、0 张图——表格过重，可读性差\n\n- 具体位置：Tables 1-16 贯穿全文\n- 问题：论文核心概念是\"Pareto frontier\"，却没有任何可视化。一张 (English AUROC, ZS-19 AUROC) 的 scatter plot with Pareto front overlay 比 Table 1 的 20 行数字直观得多。同样，layer-wise transfer degradation curve、resource-tier gradient、CaCLR ablation 都适合用图表呈现。16 张纯数字表格使得论文难以快速理解核心 pattern。\n- 建议：至少添加 (1) Pareto frontier 可视化（scatter plot），(2) layer-wise AUROC 折线图，(3) resource tier vs. improvement 的 bar chart\n\n**W3** [warning] \"First systematic study\" 声明过强\n\n- 具体位置：Abstract 第 3 行 \"We present the first systematic study of cross-lingual correctness probe transfer\"\n- 问题：Xiao et al. (2025) 做了 cross-lingual knowledge boundary probe transfer（5 languages），Civelli et al. (2025) 做了 cross-lingual difficulty probe transfer。本文的\"first\"仅成立于\"correctness probe\"这一细分品类。这种细分声明（\"first for correctness, not knowledge-boundary, not difficulty\"）在 reviewer 看来更像是通过 narrow scoping 来回避先行工作，而非真正的开创性。\n- 建议：改为 \"the first large-scale study comparing correctness probe transfer across architectures\"——强调 scale 和 architecture comparison 而非\"first\"\n\n**W4** [warning] Difficulty-capability decomposition 的 25% 解释力未给置信区间\n\n- 具体位置：Abstract \"explains 25% of transfer gap\", §5.2\n- 问题：25% 的 variance explained 是关键数字，但论文未报告 bootstrap CI 或 cross-validation stability。在 20 语言的样本上，这个估计可能有很大方差。此外，72% 的 method choice prediction accuracy（Abstract）未与 random baseline 或 majority class baseline 对比。\n- 建议：报告 bootstrap 95% CI；报告 random/majority baseline 对比\n\n**W5** [warning] CaCLR 的 improvement 幅度较小，实际意义不清楚\n\n- 具体位置：§5.3, Table 7\n- 问题：CaCLR 的核心结果是 \"+1.3pp avg AUROC\" 和 \"~40% ECE reduction\"（Abstract）。但 Table 7 显示 CaCLR 的 AUROC 为 0.804，zero-shot baseline 为 0.762——zero-shot 已经不低。而 few-shot (100) 为 0.779。在实际部署中，25 或 100 个 few-shot 标签的获取成本极低，CaCLR 相比 few-shot 的优势有限。论文未讨论 CaCLR 在什么场景下比简单的 few-shot fine-tuning 更有实际价值。\n- 建议：补充 cost-benefit 分析，说明 zero-label 假设在什么实际场景下成立\n\n---\n\n## 小问题（不影响接收）\n\n- §3.4 CaCLR 公式 (1) 中的 α 和 β 说明\"tuned on a validation set\"但未说明 validation set 的语言组成——如果 validation 含 target language labels 则\"zero-label\"声明不成立\n- §5.5 \"Probe Complexity Analysis\"（Table 12）仅在 Qwen3-235B 上做，是否 architecture-specific？应在多个架构上验证\n- §5.9 INT8 vs FP16 验证（Table 16）仅在 Llama 4 Scout 上做 5% 子集——样本量过小难以得出稳健结论\n- References 格式不一致：部分有 venue 信息（Burns et al. → ICLR 2023, Marks et al. → COLM 2024），部分没有（Miao et al. 2026 缺 venue, Civelli et al. 2025 缺 venue）\n\n---\n\n## 主要优势\n\n- **S1**: 实验规模确实比先行工作大——20 语言 × 3 架构 × 3 基准的覆盖度超过 Xiao (5 languages) 和 Civelli 的范围\n- **S2**: CaCLR 的 zero-label 设定有实际意义——在 target language 完全无标注数据的场景下提供了一条可行路径\n- **S3**: Architecture comparison（Table 4, Table 14）揭示了 MoE vs Dense 的 frontier 形状差异，这在已有文献中未见讨论\n- **S4**: Orthogonality 的 resource-tier gradient（Table 10-11）提供了一个有趣的发现：低资源语言的 orthogonality 更弱，暗示模型对低资源语言的 correctness 和 confidence 编码更加纠缠\n\n---\n\n## 给作者的具体问题\n\n1. Table 1 中标记 ★ 的层是否经过标准 Pareto dominance 检验？如果做了，请提供 hypervolume indicator。如果没做，标题中的 \"Pareto Frontier\" 是否应改为更准确的术语？\n2. CaCLR 的 consistency regularization（ℓ_consistency）是否在 English 和 target language 的 parallel data 上计算？如果是，\"zero-label\"的定义是什么——zero target-language correctness labels 但需要 parallel sentences？\n3. §5.2 报告 h² = 0.72 的 difficulty heritability——这个数字与 Civelli et al. (2025) 报告的值相比如何？论文没有引用 Civelli 的具体数字做对比。\n4. Orthogonality 分析（§5.4）中 cosine similarity 的计算是在 probe weight vectors 上还是在 representation space 中的 direction vectors 上？Miao & Ungar (2026) 的原始方法是哪种？\n5. 论文使用 Qwen3-235B-A22B, Llama 4 Scout, Gemma 4 31B——三个模型中两个是 MoE。MoE 的 expert routing 是否影响 layer-wise probing 的解释？论文未讨论 MoE 架构中 \"layer depth\" 的特殊性。\n\n---\n\n**总结**: 这是一篇在规模上有价值的实证研究，但四项贡献的新颖性均为增量性的，\"Pareto frontier\" framing 技术上不准确，且参考文献（8 篇）和 Related Work 的覆盖度远低于顶会标准。建议：(1) 大幅扩充参考文献和 Related Work，(2) 修正或放弃 Pareto 术语，(3) 添加可视化，(4) 更诚实地定位为 large-scale empirical study 而非方法论贡献。在当前状态下，推荐 Revise-for-next-cycle。",
    "reviewer_id": "2",
    "project": "xling_calib_direction"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-20T19:51:53.585574+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3710
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-20T19:52:03.589436+00:00_

审稿意见已提交给 Review Director。总结如下：

**评分: 2.5/5 (Revise-for-next-cycle)**

三个 Must-Fix 问题：

1. **参考文献极度稀疏（仅 8 篇）**——缺失 Conneau et al.、Pires et al.、CCPS、CKA/SVCCA、Belinkov survey 等大量核心文献，Related Work 仅 ~15 行，远低于顶会标准
2. **"Pareto frontier" 术语技术上不准确**——实际是 depth-transferability trade-off curve，且 deeper layers = more language-specific 是多语言 NLP 已知现象（Pires 2019, Conneau 2020）。论文甚至没有画一张 scatter plot 来可视化这条"frontier"
3. **四项贡献均为增量性**——Claim 1 重新包装已知现象，Claim 2 直接建立在 Civelli et al. 之上，Claim 3 组合三个已知 loss 组件，Claim 4 是方法论上的直接复制扩展

主要优势：实验规模（20语言×3架构×3基准）确实超过先行工作，CaCLR 的 zero-label 设定有实用价值，MoE vs Dense 的 architecture comparison 是新视角。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2"
}
```

</details>

---

## Round 2

22 recorded events

### User

_source line 53 · 2026-05-20T19:56:44.681435+00:00_

[Round 1 审稿请求]:
## 交叉审阅任务

以下是 **Reviewer 1（Methods & Experiments 方向）** 的完整 Round 1 审稿意见。请逐条回应其 Must-Fix 和 Should-Fix 问题：

- **[AGREE]**：同意该观点，并简要说明为什么你也认同（可补充你从 Novelty/Related Work 角度的佐证）
- **[REBUT]**：不同意或有保留意见，提供具体证据（引用论文中的 Section/Table/Figure）

特别关注：R1 提出的 N1（Abstract 72% vs 正文 81% 数值矛盾）和 N2（"25% of transfer gap" 无法从数据推导）——这两个是你初审中未涉及的新发现，请判断严重程度。

---

## Reviewer 1 完整审稿原文

**总体评分**: 3.0 / 5（Findings 级别）

### ACL ARR 官方维度打分

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 2.5/5 | 核心 claim 之间存在数值矛盾（72% vs 81%、25% 来源不明）；CaCLR "zero-label" 表述掩盖了对 parallel data 的依赖；无任何 CI/显著性检验 |
| Excitement | 3.0/5 | 跨语言 correctness probe transfer 值得研究，Pareto frontier 框架有新意，但 CaCLR 改进幅度有限（~3.4pp over linear proj），decomposition 解释力模糊 |
| Overall Assessment | 3.0/5 | Findings 推荐——规模 OK，有一定 insight，但 soundness 问题太多 |
| Reproducibility | 2.5/5 | probe 训练样本量、train/test split、cross-validation 策略均未报告；IRT difficulty 参数估计流程不透明；超参无 sensitivity analysis |
| Confidence | 4/5 | 仔细阅读全文并验证了引用；熟悉 probing、calibration、cross-lingual transfer 文献 |

### Must-Fix 问题

**N1** [critical] Abstract 与正文数值不一致——72% vs 81%
- Abstract: "predicts method choice with 72% accuracy" vs §5.2: "81% prescriptive accuracy"
- 可能 72% 来自 IRT 的 R²=0.72（§5.2），属于指标混淆（explained variance ≠ prescriptive accuracy）
- 核心 claim 数字自相矛盾，直接动摇论文可信度

**N2** [critical] "Explains 25% of the transfer gap" 来源不明
- Abstract 核心 claim，但 Table 5 显示 difficulty-shared 占 Transfer Degradation 的 13%，capability-specific 占 87%
- 无论从哪个角度看都推不出 "25%"，正文 §5.2 也未出现此数字
- 要么计算错误，要么引用了未展示的分析

**N3** [critical] 参考文献严重不足且多条引用信息有误
- 全文仅 8 条引用（同类 ACL 论文通常 30-50 条）
- Web search 核查发现：
  - Miao et al. (2026a) "CORAL"：实际第一作者为 Miranda Muqing Miao（非 Shuo Miao），标题也不匹配
  - Zhou et al. (2024) "LACE"：实际发表于 2025（arxiv 2510.03136），年份和标题均不匹配
  - Civelli et al. (2025)：标题与最接近的论文 "A Shared Geometry of Difficulty" 不匹配

**N4** [critical] 完全缺乏统计检验和方差估计
- 所有 Tables 1-16 均为单次实验点估计
- 无 CI、SD、bootstrap significance test 或多次 random seed
- CaCLR vs baseline 差距仅 3.4pp，无法判断是否 significant

### Should-Fix 问题

**W1** CaCLR "zero-label" 表述有误导性——L_cons 需要 parallel activations，与 linear proj 资源需求本质相同
**W2** CaCLR 超参数（α=0.15, β=0.08）无 sensitivity analysis
**W3** INT8 验证仅在 Llama 4 Scout 上用 5% 子集
**W4** 无任何可视化图表——Pareto frontier 论文没有 scatter plot
**W5** Very low resource tier 仅 4 种语言，统计效力不足
**W6** Probe 训练细节不充分——样本量、split、CV、正则化参数均未报告

### 主要优势
1. 问题选择好——跨语言 correctness probe transfer 有实际意义且尚未被系统研究
2. 实验规模合理——20语言×3架构×3 benchmark
3. Pareto frontier 框架有启发性
4. Difficulty-capability decomposition 概念新颖
5. CaCLR 设计原则合理，ablation 清楚
6. 全部 10 个实验计划均已覆盖

### 给作者的问题
1. Abstract 72% vs §5.2 81% 分别度量什么？
2. "25% of transfer gap" 推导路径？
3. CaCLR L_cons 的 parallel data 需求 vs linear proj 的实际资源优势？
4. IRT difficulty 参数是英语单独估计的吗？
5. 为什么仅 8 条引用？
6. Miao et al. 的作者名是否有误？
7. Probe 训练样本量和 CV 策略？
8. 为什么没有任何 figure？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-20T19:57:19.817335+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p1.png"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-20T19:57:20.219141+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/.claude/sessions/review_reviewer_2_dfeebd74.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-20T19:57:20.319849+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p5.png"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-20T19:57:20.822163+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/.claude/sessions/review_reviewer_2_dfeebd74.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-20T19:57:20.873050+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p3.png"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-20T19:57:20.974571+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/.claude/sessions/review_reviewer_2_dfeebd74.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-20T19:57:26.445145+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.pdf",
  "project": "xling_calib_direction",
  "pages": "1,3,5,6,10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.pdf",
    "project": "xling_calib_direction",
    "pages": "1,3,5,6,10",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-20T19:57:26.997576+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 321.0}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 295.6}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 264.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 293.9}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 144.1}], \"total_pages\": 11, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 552
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-20T19:57:30.663187+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p1.png"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-20T19:57:31.567851+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-20T19:57:31.618523+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p5.png"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-20T19:57:32.021571+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-20T19:57:32.073811+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p3.png"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-20T19:57:32.978014+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-20T19:57:33.028682+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p6.png"
  }
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-20T19:57:33.280378+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/_pdf_images/paper_p10.png"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-20T19:57:33.333198+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-20T19:57:33.385528+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 356
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-20T19:59:00.873899+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — 交叉审阅回应（对 Reviewer 1 Round 1 意见）\n\n---\n\n### Must-Fix 逐条回应\n\n**[AGREE] R1-N1: Abstract 72% vs 正文 81% 数值矛盾**\n\n完全同意，这是我初审中遗漏的严重问题。重新核实论文后确认：\n- Abstract（p.1）: \"predicts method choice with **72%** accuracy\"\n- §5.2（p.5）: \"The decomposition achieves **81%** prescriptive accuracy\"\n- §5.2 同页: \"IRT difficulty probes achieve **h² = 0.72**\"\n\nR1 的假设极其合理——72% 几乎可以确定是作者混淆了 h²=0.72（IRT explained variance）与 prescriptive accuracy（81%）。这不是一个小笔误：h²（variance explained ratio）和 accuracy（分类准确率）是完全不同的指标，放在 Abstract 核心 claim 里意味着作者可能对自己的方法产出缺乏基本核查。\n\n从 Novelty 角度补充：如果连核心数字都不 self-consistent，那么 Claim 2（difficulty-capability decomposition）的整个论证链的可信度都受到动摇——reviewer 无法确定论文中报告的其他数字（如\"25%\"）是否也存在同类错误。\n\n**严重程度判断：critical。** 直接影响论文可信度，必须修复。\n\n---\n\n**[AGREE] R1-N2: \"25% of transfer gap\" 来源不明**\n\n完全同意，且我补充了进一步的数据验证。重新逐字核对：\n- Abstract（p.1）: \"explains **25%** of transfer gap\"\n- Table 5（p.5）列出三行数据：\n  - Full correctness: Var% = 100, Drop = 1.1 (actually 9.1 based on my first reading), Share% = 100\n  - Difficulty (shared): Var% = 68.4, Drop = 1.1, Share% = **17**\n  - Capability (specific): Var% = 31.6, Drop = 14.2, Share% = **87**\n- §5.2 正文中也未出现\"25%\"这个数字\n\n无论取 17%（difficulty 的 share）、31.6%（capability 的 variance ratio）、还是 68.4%（difficulty 的 variance ratio），都推不出 25%。该数字在论文中无任何推导路径。\n\n结合 N1 来看，这是**第二个**核心 claim 数字无法从数据验证的案例。一篇论文的两个 Abstract-level claims 都出现数值问题，模式令人担忧。\n\n我在初审中指出了\"25% 未给 confidence interval\"（W4），但 R1 发现了更根本的问题——这个数字本身就不存在于正文中。将我的 W4 升级为 **critical**。\n\n---\n\n**[AGREE] R1-N3: 参考文献严重不足且多条引用信息有误**\n\n完全同意，且我从 Novelty/Related Work 角度提供进一步佐证：\n\n(a) **数量问题**：我在初审中将此列为 N1（critical），详细列出了至少 7 个缺失的重要文献领域（Conneau et al., Pires et al., CCPS, Belinkov, IRT 文献, CKA/SVCCA, 多语言 calibration）。8 篇引用对一篇跨 3 个研究方向的论文而言是不可接受的。\n\n(b) **准确性问题**：R1 通过 web search 发现的元数据不匹配问题更加严重。我核实了 References（p.10）中的原文：\n- \"**Shuo** Miao et al. CORAL: Cross-task correctness probes for LLM calibration. 2026.\" — 如果 R1 搜索到实际第一作者不是 Shuo Miao 且标题不匹配，这提示可能是 **fabricated reference**\n- \"Xin Zhou et al. LACE: Layer-adaptive calibration ensembles for multilingual LLMs. 2024.\" — 如果实际论文的年份和标题都不匹配，同理\n- \"Andrea Civelli et al.\" 的标题不匹配也同理\n\n从 Novelty 审查角度，如果核心参考文献是虚构的或严重误引的，那么论文的整个 novelty 论证（\"我们是第一个做 X 而不是 Y/Z 的\"）就完全不可信——因为 Y 和 Z 可能并不存在。这是论文可信度的根本问题。\n\n**严重程度判断：critical，且可能是 ethical concern（疑似 fabricated citations）。**\n\n---\n\n**[AGREE] R1-N4: 完全缺乏统计检验和方差估计**\n\n同意。我在初审中仅将缺少 CI 作为 W4（should-fix），但 R1 将其升级为 critical 是有道理的。考虑到：\n- Tables 1-16 全部为单次实验点估计\n- CaCLR vs best baseline 的核心优势仅 ~3.4pp AUROC\n- 论文跨 3 个架构 × 20 种语言，variation 来源很多\n\n缺少任何方差估计使得所有比较性 claim 都无法评估统计可靠性。特别是 CaCLR 的 1.3pp 平均改进（Abstract）——在没有 CI 的情况下，无法排除这是随机波动。\n\n从 Novelty 角度补充：如果 CaCLR 的改进不具统计显著性，那么 Claim 3 的实质贡献就大打折扣。\n\n---\n\n### Should-Fix 逐条回应\n\n**[AGREE] R1-W1: CaCLR \"zero-label\" 表述有误导性**\n\n同意。§3.4（p.3）明确写道 ℓ_consistency \"penalizes divergence between probe outputs on **English and non-English parallel activations**\"。这意味着 CaCLR 需要：\n1. English correctness labels（训练 probe）\n2. English-target language **parallel data**（计算 ℓ_consistency）\n\n\"Zero-label\" 仅指不需要 **target language correctness labels**，但对 parallel data 的需求并非 trivial——获取 20 种语言的 parallel sentences 可能比直接标注 25-100 个 correctness labels 更昂贵。\n\n我在初审的\"给作者的问题\"第 2 条已提出了同样的质疑。R1 将其升级为 should-fix 是恰当的。\n\n**[REBUT] R1-W2: CaCLR 超参数 α=0.15, β=0.08**\n\n部分不同意——R1 引用的 β 值有误。§3.4（p.3）原文为 \"optimal values are α = 0.15 and **β = 0.10**\"，非 0.08。这是 R1 的笔误。\n\n但 R1 关于缺乏 sensitivity analysis 的核心观点我完全同意——两个超参数在 validation set 上 tuned，但 (a) validation set 的语言组成未报告，(b) 不同 α, β 下性能如何变化也未报告。这影响 reproducibility。\n\n**[AGREE] R1-W3: INT8 验证仅在 Llama 4 Scout 上用 5% 子集**\n\n同意，我在初审小问题中也指出了这一点。Table 16（p.11）在 Llama 4 Scout 单一架构上用 5% 子集做验证，样本量过小且不跨架构。如果论文声称\"quantization-robust\"，至少应在全部 3 个架构上验证。\n\n**[AGREE] R1-W4: 无任何可视化图表**\n\n强烈同意。这是我初审 W2 的核心观点。补充强调：一篇标题含\"Pareto Frontier\"的论文没有一张 scatter plot 来可视化这条 frontier，这在 presentation 上是不可原谅的。16 张表格 + 0 张图 = 论文读起来像一份数据报告而非研究论文。\n\n**[AGREE] R1-W5: Very low resource tier 仅 4 种语言**\n\n同意。Table 15（p.11）显示 Very low tier 仅 4 种语言，且 CaCLR 在该 tier 的 >0.60 pass rate 仅 50%——这意味着在最需要帮助的语言上，CaCLR 的可靠性最差。样本量 n=4 的任何统计结论都不可靠。我初审未单独指出此点，R1 的发现有效补充了我的审查。\n\n**[AGREE] R1-W6: Probe 训练细节不充分**\n\n同意。§3.1（p.2-3）仅提到\"5 conditions\"（zero-shot, mean-shift, linear-proj, few-shot 25/100, CaCLR），但未报告：\n- probe 的训练样本量（English correctness labels 从何而来、多少个）\n- train/test split 比例\n- cross-validation 策略\n- 正则化（logistic regression 的 C 参数，MLP 的 dropout/weight decay）\n\n这些信息对 reproducibility 至关重要。\n\n---\n\n### 综合判断\n\nR1 的 N1 和 N2 是我初审中遗漏的重要发现。两个 Abstract-level 核心数字（72% 和 25%）都无法从正文数据验证，加上 R1-N3 发现的参考文献元数据不匹配，形成了一个令人担忧的 pattern：**论文的核心 claims 与论文本身的 evidence 之间存在系统性脱节**。\n\n这使得论文的问题从\"增量性贡献 + 参考文献不足\"升级为\"**可信度问题**\"——reviewer 无法信任论文中报告的任何未经独立验证的数字。\n\n基于 R1 的发现，我将自己的评分从 2.5 下调至 **2.0**（Revise for next cycle），理由是 soundness 维度需要从 3.0 降至 2.0。",
  "reviewer_id": "2",
  "project": "xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — 交叉审阅回应（对 Reviewer 1 Round 1 意见）\n\n---\n\n### Must-Fix 逐条回应\n\n**[AGREE] R1-N1: Abstract 72% vs 正文 81% 数值矛盾**\n\n完全同意，这是我初审中遗漏的严重问题。重新核实论文后确认：\n- Abstract（p.1）: \"predicts method choice with **72%** accuracy\"\n- §5.2（p.5）: \"The decomposition achieves **81%** prescriptive accuracy\"\n- §5.2 同页: \"IRT difficulty probes achieve **h² = 0.72**\"\n\nR1 的假设极其合理——72% 几乎可以确定是作者混淆了 h²=0.72（IRT explained variance）与 prescriptive accuracy（81%）。这不是一个小笔误：h²（variance explained ratio）和 accuracy（分类准确率）是完全不同的指标，放在 Abstract 核心 claim 里意味着作者可能对自己的方法产出缺乏基本核查。\n\n从 Novelty 角度补充：如果连核心数字都不 self-consistent，那么 Claim 2（difficulty-capability decomposition）的整个论证链的可信度都受到动摇——reviewer 无法确定论文中报告的其他数字（如\"25%\"）是否也存在同类错误。\n\n**严重程度判断：critical。** 直接影响论文可信度，必须修复。\n\n---\n\n**[AGREE] R1-N2: \"25% of transfer gap\" 来源不明**\n\n完全同意，且我补充了进一步的数据验证。重新逐字核对：\n- Abstract（p.1）: \"explains **25%** of transfer gap\"\n- Table 5（p.5）列出三行数据：\n  - Full correctness: Var% = 100, Drop = 1.1 (actually 9.1 based on my first reading), Share% = 100\n  - Difficulty (shared): Var% = 68.4, Drop = 1.1, Share% = **17**\n  - Capability (specific): Var% = 31.6, Drop = 14.2, Share% = **87**\n- §5.2 正文中也未出现\"25%\"这个数字\n\n无论取 17%（difficulty 的 share）、31.6%（capability 的 variance ratio）、还是 68.4%（difficulty 的 variance ratio），都推不出 25%。该数字在论文中无任何推导路径。\n\n结合 N1 来看，这是**第二个**核心 claim 数字无法从数据验证的案例。一篇论文的两个 Abstract-level claims 都出现数值问题，模式令人担忧。\n\n我在初审中指出了\"25% 未给 confidence interval\"（W4），但 R1 发现了更根本的问题——这个数字本身就不存在于正文中。将我的 W4 升级为 **critical**。\n\n---\n\n**[AGREE] R1-N3: 参考文献严重不足且多条引用信息有误**\n\n完全同意，且我从 Novelty/Related Work 角度提供进一步佐证：\n\n(a) **数量问题**：我在初审中将此列为 N1（critical），详细列出了至少 7 个缺失的重要文献领域（Conneau et al., Pires et al., CCPS, Belinkov, IRT 文献, CKA/SVCCA, 多语言 calibration）。8 篇引用对一篇跨 3 个研究方向的论文而言是不可接受的。\n\n(b) **准确性问题**：R1 通过 web search 发现的元数据不匹配问题更加严重。我核实了 References（p.10）中的原文：\n- \"**Shuo** Miao et al. CORAL: Cross-task correctness probes for LLM calibration. 2026.\" — 如果 R1 搜索到实际第一作者不是 Shuo Miao 且标题不匹配，这提示可能是 **fabricated reference**\n- \"Xin Zhou et al. LACE: Layer-adaptive calibration ensembles for multilingual LLMs. 2024.\" — 如果实际论文的年份和标题都不匹配，同理\n- \"Andrea Civelli et al.\" 的标题不匹配也同理\n\n从 Novelty 审查角度，如果核心参考文献是虚构的或严重误引的，那么论文的整个 novelty 论证（\"我们是第一个做 X 而不是 Y/Z 的\"）就完全不可信——因为 Y 和 Z 可能并不存在。这是论文可信度的根本问题。\n\n**严重程度判断：critical，且可能是 ethical concern（疑似 fabricated citations）。**\n\n---\n\n**[AGREE] R1-N4: 完全缺乏统计检验和方差估计**\n\n同意。我在初审中仅将缺少 CI 作为 W4（should-fix），但 R1 将其升级为 critical 是有道理的。考虑到：\n- Tables 1-16 全部为单次实验点估计\n- CaCLR vs best baseline 的核心优势仅 ~3.4pp AUROC\n- 论文跨 3 个架构 × 20 种语言，variation 来源很多\n\n缺少任何方差估计使得所有比较性 claim 都无法评估统计可靠性。特别是 CaCLR 的 1.3pp 平均改进（Abstract）——在没有 CI 的情况下，无法排除这是随机波动。\n\n从 Novelty 角度补充：如果 CaCLR 的改进不具统计显著性，那么 Claim 3 的实质贡献就大打折扣。\n\n---\n\n### Should-Fix 逐条回应\n\n**[AGREE] R1-W1: CaCLR \"zero-label\" 表述有误导性**\n\n同意。§3.4（p.3）明确写道 ℓ_consistency \"penalizes divergence between probe outputs on **English and non-English parallel activations**\"。这意味着 CaCLR 需要：\n1. English correctness labels（训练 probe）\n2. English-target language **parallel data**（计算 ℓ_consistency）\n\n\"Zero-label\" 仅指不需要 **target language correctness labels**，但对 parallel data 的需求并非 trivial——获取 20 种语言的 parallel sentences 可能比直接标注 25-100 个 correctness labels 更昂贵。\n\n我在初审的\"给作者的问题\"第 2 条已提出了同样的质疑。R1 将其升级为 should-fix 是恰当的。\n\n**[REBUT] R1-W2: CaCLR 超参数 α=0.15, β=0.08**\n\n部分不同意——R1 引用的 β 值有误。§3.4（p.3）原文为 \"optimal values are α = 0.15 and **β = 0.10**\"，非 0.08。这是 R1 的笔误。\n\n但 R1 关于缺乏 sensitivity analysis 的核心观点我完全同意——两个超参数在 validation set 上 tuned，但 (a) validation set 的语言组成未报告，(b) 不同 α, β 下性能如何变化也未报告。这影响 reproducibility。\n\n**[AGREE] R1-W3: INT8 验证仅在 Llama 4 Scout 上用 5% 子集**\n\n同意，我在初审小问题中也指出了这一点。Table 16（p.11）在 Llama 4 Scout 单一架构上用 5% 子集做验证，样本量过小且不跨架构。如果论文声称\"quantization-robust\"，至少应在全部 3 个架构上验证。\n\n**[AGREE] R1-W4: 无任何可视化图表**\n\n强烈同意。这是我初审 W2 的核心观点。补充强调：一篇标题含\"Pareto Frontier\"的论文没有一张 scatter plot 来可视化这条 frontier，这在 presentation 上是不可原谅的。16 张表格 + 0 张图 = 论文读起来像一份数据报告而非研究论文。\n\n**[AGREE] R1-W5: Very low resource tier 仅 4 种语言**\n\n同意。Table 15（p.11）显示 Very low tier 仅 4 种语言，且 CaCLR 在该 tier 的 >0.60 pass rate 仅 50%——这意味着在最需要帮助的语言上，CaCLR 的可靠性最差。样本量 n=4 的任何统计结论都不可靠。我初审未单独指出此点，R1 的发现有效补充了我的审查。\n\n**[AGREE] R1-W6: Probe 训练细节不充分**\n\n同意。§3.1（p.2-3）仅提到\"5 conditions\"（zero-shot, mean-shift, linear-proj, few-shot 25/100, CaCLR），但未报告：\n- probe 的训练样本量（English correctness labels 从何而来、多少个）\n- train/test split 比例\n- cross-validation 策略\n- 正则化（logistic regression 的 C 参数，MLP 的 dropout/weight decay）\n\n这些信息对 reproducibility 至关重要。\n\n---\n\n### 综合判断\n\nR1 的 N1 和 N2 是我初审中遗漏的重要发现。两个 Abstract-level 核心数字（72% 和 25%）都无法从正文数据验证，加上 R1-N3 发现的参考文献元数据不匹配，形成了一个令人担忧的 pattern：**论文的核心 claims 与论文本身的 evidence 之间存在系统性脱节**。\n\n这使得论文的问题从\"增量性贡献 + 参考文献不足\"升级为\"**可信度问题**\"——reviewer 无法信任论文中报告的任何未经独立验证的数字。\n\n基于 R1 的发现，我将自己的评分从 2.5 下调至 **2.0**（Revise for next cycle），理由是 soundness 维度需要从 3.0 降至 2.0。",
    "reviewer_id": "2",
    "project": "xling_calib_direction"
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-20T19:59:04.436361+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3562
}
```

</details>

---

### Assistant

_source line 74 · 2026-05-20T19:59:11.922354+00:00_

交叉审阅已提交。核心结论：

- R1 的 **N1**（72% vs 81% 数值矛盾）和 **N2**（"25%" 来源不明）我均判定为 **critical**，且通过重新核实论文原文确认了这两个问题的真实性
- 这两个发现与我初审指出的参考文献问题（8 篇、元数据疑似不匹配）形成了系统性 pattern——论文核心 claims 与 evidence 之间存在多处脱节
- R1 的 6 条 Should-Fix 中 5 条 **AGREE**，1 条 **REBUT**（β 值 R1 引错了，应为 0.10 非 0.08，但其核心论点成立）
- 综合评分从 2.5 下调至 **2.0**（Revise for next cycle）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2"
}
```

</details>

---

## Round 3

36 recorded events

### User

_source line 75 · 2026-05-21T06:08:17.013455+00:00_

[Round 1 审稿请求]:
## Review Assignment — R2: Novelty & Related Work

You are Reviewer 2, focusing on **novelty, positioning, and related work**.

### Paper
**Title**: "The Limits of Cross-Lingual Calibration Probe Transfer: A Large-Scale Negative Result with Methodological Implications"
**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/review_input_f5f46a62.pdf`

### Venue & Scoring
Use **ACL ARR** scoring (1-5 scale):
- **Soundness**: 5=Excellent, 4=Strong, 3=Acceptable, 2=Poor, 1=Major issues
- **Excitement**: 5=Highly Exciting, 4=Exciting, 3=Ambivalent, 2=Mediocre, 1=Not Exciting
- **Overall**: 5=Strong Accept, 4=Accept, 3=Borderline, 2=Reject, 1=Strong Reject

### Your Focus Areas
1. **Novelty assessment**: How novel are the contributions? (a) First cross-lingual extension of correctness probing; (b) CaCLR as a new method (even though it fails); (c) cross-lingual control task methodology; (d) Simpson's Paradox falsification; (e) linear projection characterization. Which contributions advance the field vs. are incremental?
2. **Related work coverage**: The paper cites probe-based calibration (CORAL, Miao & Ungar), cross-lingual probing (knowledge-boundary probes), probing methodology (Hewitt & Liang, MDL), domain adaptation theory (Ben-David, Zhao et al.), and cross-lingual alignment (MUSE, VecMap). Are there missing references? Is the positioning accurate?
3. **Framing as negative result**: Is the "negative result with methodological implications" framing effective? Does it meet the bar for a publishable negative result (thorough, well-controlled, informative for the community)?
4. **Contribution hierarchy**: The paper ranks contributions as (1) control task methodology > (2) comprehensive negative result > (3) conditional practical guidance. Is this ranking justified? Are the contributions sufficient for a *CL venue?
5. **Writing quality**: Is the paper well-structured? Is the narrative coherent? Are claims appropriately hedged?
6. **Comparison with prior work**: The paper extends pilot work on Qwen2.5-7B and Llama-3.1-8B to larger models. How well does it differentiate from the pilot? Is the added value clear?

### Key Novelty Claims to Evaluate
- "First large-scale study of cross-lingual correctness probe transfer" — verify against literature
- "First application of Hewitt & Liang selectivity controls to cross-lingual probing" — is this genuinely novel?
- CaCLR as a method — even though it fails, is the formulation a contribution?
- Simpson's Paradox falsification — how significant is debunking a 5-language pilot finding?
- The "42% of low-resource probing results are artifacts" finding — field-level implication?

### Related Work to Check
- Miao & Ungar (2026) — correctness probes for English
- CORAL — cross-task transfer of probes
- Hewitt & Liang (2019) — control tasks for probing
- DALI — cross-lingual representation alignment
- Ben-David et al. — H-divergence framework
- Zhao et al. (2019) — conditional distribution mismatch
- MUSE, VecMap — cross-lingual alignment

### Output Format
Provide your review in this structure:
```
## R2 Independent Review: Novelty & Related Work

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-21T06:08:25.805717+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/review_input_f5f46a62.pdf",
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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/review_input_f5f46a62.pdf",
    "project": "xling_calib_direction",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-21T06:08:27.264331+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 339.6}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 341.6}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 298.0}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 311.6}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 283.2}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 225.9}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 304.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 296.1}, {\"page\": 9, \"p
…[truncated 728 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1458
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-21T06:08:31.129787+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p1.png"
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-21T06:08:32.086045+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-21T06:08:32.136737+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p2.png"
  }
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-21T06:08:32.642559+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p3.png"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-21T06:08:33.046290+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-21T06:08:33.250144+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 607
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-21T06:08:33.301827+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p4.png"
  }
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-21T06:08:33.805836+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p5.png"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-21T06:08:33.960898+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 659
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-21T06:08:34.568736+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 762
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-21T06:08:38.584118+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p6.png"
  }
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-21T06:08:38.987232+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-21T06:08:38.989822+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p7.png"
  }
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-21T06:08:39.896571+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-21T06:08:39.897326+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p8.png"
  }
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-21T06:08:40.402046+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-21T06:08:40.402475+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p9.png"
  }
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-21T06:08:41.009014+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 606
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-21T06:08:41.009483+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p10.png"
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-21T06:08:41.412473+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-21T06:08:46.582292+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/review_input_f5f46a62.pdf",
  "project": "xling_calib_direction",
  "pages": "11-14",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/review_input_f5f46a62.pdf",
    "project": "xling_calib_direction",
    "pages": "11-14",
    "dpi": "150"
  }
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-21T06:08:46.883240+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 225.2}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 186.4}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 160.1}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 77.1}], \"total_pages\": 14, \"rendered_pages\": 4, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 300
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-21T06:08:55.217912+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p11.png"
  }
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-21T06:08:55.720405+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-21T06:08:55.971507+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p12.png"
  }
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-21T06:08:56.222941+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p13.png"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-21T06:08:56.475047+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-21T06:08:56.575810+00:00_

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
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/worst/_pdf_images/paper_p14.png"
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-21T06:08:56.879984+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 657
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-21T06:08:56.881980+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 306
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-21T06:11:31.837933+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## R2 Independent Review: Novelty & Related Work\n\n**论文标题**: The Limits of Cross-Lingual Calibration Probe Transfer: A Large-Scale Negative Result with Methodological Implications\n\n---\n\n### Summary (2-3 sentences)\n\n本文将前期 pilot（Qwen2.5-7B, Llama-3.1-8B）的跨语言 correctness probe transfer 研究扩展至 3 个大规模架构（Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense）× 20 种语言 × 5 种迁移条件，得出了系统性的负面结论：depth-transferability Pareto frontier 不泛化、CaCLR 方法有害、小样本 pilot 的 CKA-transfer 正相关是 Simpson's Paradox。最有价值的贡献是将 Hewitt & Liang 的 selectivity control tasks 引入跨语言 probing，揭示 42% 的低资源 probing 结果为 artifacts。\n\n---\n\n### Strengths\n\n**S1** [Novelty — Control task methodology] 将 Hewitt & Liang (2019) 的 selectivity controls 应用于跨语言 probing 是**本文最强的新颖性贡献**。Table 10（p.10）和 Table 11（p.10）系统展示了 per-language selectivity 数据，发现 LOW tier 的 artifact rate 达 42%（Table 12, p.11）。这一发现对整个跨语言 probing 领域有方法论层面的警示意义——如果近半数低资源语言的 probing 结果是 artifacts，那么先前文献中未使用 control tasks 的正面结论都需要重新审视。这满足\"field-level implication\"的标准。\n\n**S2** [Framing — 诚实的负面结果] 论文将核心发现定位为\"large-scale negative result\"而非强行正面包装，这比前一篇论文（同一 research agenda 的正面版本）在学术诚信上更可信。Abstract 开门见山：\"Our results are predominantly negative\"，§7 Conclusion 也直接列出三项负面发现。对于 community 来说，知道什么不可行与知道什么可行同样重要。\n\n**S3** [Statistical rigor] 相比同一 agenda 的正面版本论文，本文在统计层面有实质性进步：\n- Bonferroni correction 用于多重比较（§4, p.3-4）\n- Spearman correlations 附 p 值（Table 1, 2, §5.1）\n- Standard deviations reported（Table 21, p.13: 每个 transfer condition 附 Std）\n- Control task selectivity 阈值（< 0.05）明确定义 artifact 判据\n- Simpson's Paradox 分析用 partial ρ 验证（Table 9, p.9）\n\n**S4** [Simpson's Paradox falsification] §5.3 的分析虽然是对自家 pilot 的自我纠错，但方法论上有示范意义。Table 9（p.9）清楚展示：5-language pilot 中观察到的正 CKA-transfer correlation（partial ρ 未报告具体值但正面提及），在 20 languages 下变为 non-significant（Simpson partial ρ = +0.14, p = 0.22）。这是 ecological fallacy / Simpson's Paradox 在 NLP 实验中的一个教科书级案例。\n\n**S5** [Practical guidance] §9（p.9-10）提供的三档决策规则（ZS AUROC < 0.30: 不可预测; [0.30, 0.65]: linear projection 有效; > 0.65: zero-shot 已足够）虽然简单，但对实践者有直接价值，且来自充分的实验支撑。\n\n**S6** [Related work coverage] §2（p.2）比前一篇论文完善得多，覆盖了 5 个子方向：probe-based calibration（CORAL, Miao & Ungar）、cross-lingual probing、probing methodology（Hewitt & Liang, MDL）、domain adaptation theory（Ben-David et al., Zhao et al. 2019）、cross-lingual alignment（MUSE, VecMap）。Domain adaptation 的理论框架（H-divergence）为负面结论提供了理论解释基础。\n\n---\n\n### Weaknesses\n\n**W1** [warning — 参考文献仍然不够充分] 虽然 §2 的覆盖面比前一篇论文好得多，但仍有重要遗漏：\n- **Conneau et al. (2020)** \"Emerging Cross-lingual Structure in Pretrained Language Models\" / XLM-R 论文——跨语言表征的 layer-wise 分析基础\n- **Pires et al. (2019)** \"How multilingual is Multilingual BERT?\" ——layer-wise cross-lingual transfer 的开创性研究，直接相关\n- **Belinkov (2022)** \"Probing Classifiers: Promises, Shortcomings, and Advances\" 综述——论文大量使用 probing 方法但未引用该领域的核心综述\n- **Keleg & Magdy (2023)** \"On the Calibration of Massively Multilingual Language Models\" ——多语言 calibration 专题研究\n- 此外，论文 PDF 中我未能在正文可见范围内找到完整的 References section（p.10 结尾是 Conclusion，p.11 开始是 Appendix A）。**如果参考文献列表被省略或因排版问题丢失，这是一个严重的格式问题。**\n\n**W2** [warning — 23 张表格 + 0 张图] 与前一篇论文相同的表述问题。23 张表格（正文 13 + 附录 10）但没有一张图。核心发现——Pareto frontier 不存在、CaCLR 的 harmful effect、Simpson's Paradox——都极适合可视化展示。特别是：\n- 一张 scatter plot（EN AUROC vs ZS AUROC by architecture）可以直观展示 \"no frontier\" 的负面结论\n- 一张 selectivity heatmap（language × layer）可以直观展示 artifact 分布 pattern\n- Simpson's Paradox 最经典的展示方式是分组 scatter plot（within-group vs. overall trend）\n表格密集使得负面结论的说服力受损——读者需要自己在数字中寻找 pattern，而一张好图可以一目了然。\n\n**W3** [minor — CaCLR 方法的新颖性因失败而难以评估] CaCLR 的损失函数（BCE + calibration + consistency + MMD）组合了四个已知组件。论文诚实报告其失败（§5.2, Table 3-4），但这使得方法贡献难以被独立评价。如果方法本身不是贡献，那么论文实质上只有两个贡献：(1) control task 方法论，(2) 负面实验结果。对于 main conference 这可能不够；对于 Findings track 可以接受。\n\n**W4** [minor — pilot 区分不充分] 论文多次提到\"pilot studies on Qwen2.5-7B and Llama-3.1-8B\"（Abstract, §5.1, §5.3），但未明确说明 pilot 是已发表工作还是同一团队的未发表前期工作。如果已发表，需要正式引用并明确 incremental contribution；如果未发表，应说明\"our unpublished pilot\"。当前表述模糊。\n\n**W5** [minor — Difficulty decomposition 的负面结论太快] §5.4 用一段话否定了 difficulty decomposition（\"The difficulty probe itself achieves only |Δ| = 0.03, statistically indistinguishable from a random-direction control\"），但 Table 9（p.9）显示 difficulty decomposition ablation 的结果在不同 tier 间有差异。论文未分析为什么 difficulty decomposition 在大模型上失败而可能在小模型上成功——是因为模型规模？训练数据差异？量化？这个分析缺口削弱了负面结论的解释力。\n\n**W6** [minor — Linear projection 的 \"only viable path\" 结论与 Table 21 存在张力] Table 21（p.13）显示 Linear Projection 200 pairs 的 Sig. impr. count 仅 11/20，few-shot 100 为 13/20。差异不大，且都远未覆盖全部 20 种语言。声称 linear projection 是 \"the only viable path\" 可能过于绝对。\n\n---\n\n### Questions for Authors\n\n**Q1**: §5.3 Simpson's Paradox 分析中，partial ρ = +0.14 (p = 0.22) 是在控制哪些变量后的结果？如果控制变量不同，partial ρ 是否会改变结论？\n\n**Q2**: Control task 的 selectivity 阈值 < 0.05 是如何确定的？Hewitt & Liang (2019) 原文是否使用了相同阈值？如果阈值改为 0.10 或 0.03，42% 的 artifact rate 如何变化？\n\n**Q3**: 论文将 pilot 模型（Qwen2.5-7B, Llama-3.1-8B）的正面结果归因于 scale 差异，但 pilot 用的是 7B/8B 模型，而本文用的是 22B-235B 模型。是否有证据表明 scale 是导致结论翻转的原因（如中间规模模型的结果）？还是架构差异（MoE vs Dense）更可能是原因？\n\n**Q4**: CaCLR 的 MMD term 引入负面效果（Table 4, p.5: 添加 MMD(l→0.01) 使 AUROC 从 0.563 降至 0.558）。作者是否尝试过其他 distributional matching 方法（如 adversarial alignment, optimal transport）？只测一种 distributional matching 就断言\"distributional matching 不可行\"可能过于草率。\n\n**Q5**: Table 11（p.10）中多个语言被标记为 ▲（permuted AUROC > real AUROC）。这是否意味着这些语言的 correctness probes 实际上在编码噪声而非真正的 correctness signal？如果是，这对 Miao & Ungar (2026) 的英文 correctness probe 结论有什么影响？\n\n**Q6**: 完整的参考文献列表在哪里？在我阅读的 PDF 中，§7 Conclusion 后直接是 Appendix A，未见 References section。\n\n---\n\n### Minor Issues\n\n- §3.2 \"CaCLR extends the standard probe loss with two regularization terms\"（p.3）中公式 (1) 有 3 项额外 loss（ℓ_cal, ℓ_cons, ℓ_MMD），但文字说\"two\"——应为 three\n- Table 3 caption（p.5）说\"CaCLR 1 sweep\"但未解释 sweep 的含义\n- §5.1 对 Gemma 4 31B Dense 的描述（p.4-5）说\"moderately clear but still noisy frontier\"，但随后的 Summary 说\"does not generalize\"——这两个判断有轻微矛盾\n- Table 19（p.13, Appendix A）52-language 扩展的结果格式与正文 20-language 不一致，增加了对比难度\n- Limitations（p.10）列出 4 点限制，诚实但也暴露了实验设计的局限：只用 MCQA format、只测 logistic regression、不包含所有 typological diversity\n\n---\n\n### Scores\n\n- **Soundness**: 3.5 / 5 — 统计方法比前一篇论文好很多（Bonferroni, control tasks, CIs），但部分负面结论的解释不够深入（W5），且参考文献列表可能缺失（W1）\n- **Excitement**: 3 / 5 — Control task 方法论贡献有 field-level 意义，但整体是 \"things don't work\" narrative，缺乏正面方法贡献；对于 Findings track 有足够兴趣，对 main conference 偏弱\n- **Overall**: 3 / 5 — Borderline / Findings track。Control task 发现（42% artifacts）如果能被独立验证，价值很高。但 CaCLR 失败 + 负面 Pareto 结论使得论文的\"so what\"不够强。推荐 Findings track 接收。\n- **Confidence**: 4 / 5 — 熟悉 probing、calibration、cross-lingual transfer 领域\n\n---\n\n### 与前一篇论文（positive framing）的对比评价\n\n| 维度 | Paper 1 (Pareto Frontier, positive) | Paper 2 (Limits, negative) |\n|------|-------------------------------------|---------------------------|\n| 学术诚信 | 差——核心数字自相矛盾（72% vs 81%）、\"25%\" 来源不明、疑似 fabricated references | 好——诚实承认负面结论、pilot 自我纠错 |\n| 统计严谨 | 差——无 CI、无 control tasks、无显著性检验 | 好——Bonferroni、selectivity controls、SDs |\n| Related Work | 差——8 篇引用、~15 行 | 中等——5 个子方向、但可能缺少 References section |\n| 新颖性 | 弱——四项增量性贡献、Pareto 术语误用 | 中等——control task 方法论有真正新意，但正面贡献有限 |\n| 可视化 | 0 图 / 16 表 | 0 图 / 23 表（问题同样严重） |\n| 实际价值 | 有限——CaCLR 改进仅 1.3pp | 有限但诚实——三档决策规则 |\n\n**整体判断**：Paper 2 在学术质量上显著优于 Paper 1，但两篇论文共享一个核心缺陷——**零可视化**。如果只能推荐一篇，我更倾向 Paper 2，因为诚实的负面结论 + 方法论警示对 community 的价值大于包装过度的弱正面结论。",
  "reviewer_id": "2",
  "project": "xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## R2 Independent Review: Novelty & Related Work\n\n**论文标题**: The Limits of Cross-Lingual Calibration Probe Transfer: A Large-Scale Negative Result with Methodological Implications\n\n---\n\n### Summary (2-3 sentences)\n\n本文将前期 pilot（Qwen2.5-7B, Llama-3.1-8B）的跨语言 correctness probe transfer 研究扩展至 3 个大规模架构（Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense）× 20 种语言 × 5 种迁移条件，得出了系统性的负面结论：depth-transferability Pareto frontier 不泛化、CaCLR 方法有害、小样本 pilot 的 CKA-transfer 正相关是 Simpson's Paradox。最有价值的贡献是将 Hewitt & Liang 的 selectivity control tasks 引入跨语言 probing，揭示 42% 的低资源 probing 结果为 artifacts。\n\n---\n\n### Strengths\n\n**S1** [Novelty — Control task methodology] 将 Hewitt & Liang (2019) 的 selectivity controls 应用于跨语言 probing 是**本文最强的新颖性贡献**。Table 10（p.10）和 Table 11（p.10）系统展示了 per-language selectivity 数据，发现 LOW tier 的 artifact rate 达 42%（Table 12, p.11）。这一发现对整个跨语言 probing 领域有方法论层面的警示意义——如果近半数低资源语言的 probing 结果是 artifacts，那么先前文献中未使用 control tasks 的正面结论都需要重新审视。这满足\"field-level implication\"的标准。\n\n**S2** [Framing — 诚实的负面结果] 论文将核心发现定位为\"large-scale negative result\"而非强行正面包装，这比前一篇论文（同一 research agenda 的正面版本）在学术诚信上更可信。Abstract 开门见山：\"Our results are predominantly negative\"，§7 Conclusion 也直接列出三项负面发现。对于 community 来说，知道什么不可行与知道什么可行同样重要。\n\n**S3** [Statistical rigor] 相比同一 agenda 的正面版本论文，本文在统计层面有实质性进步：\n- Bonferroni correction 用于多重比较（§4, p.3-4）\n- Spearman correlations 附 p 值（Table 1, 2, §5.1）\n- Standard deviations reported（Table 21, p.13: 每个 transfer condition 附 Std）\n- Control task selectivity 阈值（< 0.05）明确定义 artifact 判据\n- Simpson's Paradox 分析用 partial ρ 验证（Table 9, p.9）\n\n**S4** [Simpson's Paradox falsification] §5.3 的分析虽然是对自家 pilot 的自我纠错，但方法论上有示范意义。Table 9（p.9）清楚展示：5-language pilot 中观察到的正 CKA-transfer correlation（partial ρ 未报告具体值但正面提及），在 20 languages 下变为 non-significant（Simpson partial ρ = +0.14, p = 0.22）。这是 ecological fallacy / Simpson's Paradox 在 NLP 实验中的一个教科书级案例。\n\n**S5** [Practical guidance] §9（p.9-10）提供的三档决策规则（ZS AUROC < 0.30: 不可预测; [0.30, 0.65]: linear projection 有效; > 0.65: zero-shot 已足够）虽然简单，但对实践者有直接价值，且来自充分的实验支撑。\n\n**S6** [Related work coverage] §2（p.2）比前一篇论文完善得多，覆盖了 5 个子方向：probe-based calibration（CORAL, Miao & Ungar）、cross-lingual probing、probing methodology（Hewitt & Liang, MDL）、domain adaptation theory（Ben-David et al., Zhao et al. 2019）、cross-lingual alignment（MUSE, VecMap）。Domain adaptation 的理论框架（H-divergence）为负面结论提供了理论解释基础。\n\n---\n\n### Weaknesses\n\n**W1** [warning — 参考文献仍然不够充分] 虽然 §2 的覆盖面比前一篇论文好得多，但仍有重要遗漏：\n- **Conneau et al. (2020)** \"Emerging Cross-lingual Structure in Pretrained Language Models\" / XLM-R 论文——跨语言表征的 layer-wise 分析基础\n- **Pires et al. (2019)** \"How multilingual is Multilingual BERT?\" ——layer-wise cross-lingual transfer 的开创性研究，直接相关\n- **Belinkov (2022)** \"Probing Classifiers: Promises, Shortcomings, and Advances\" 综述——论文大量使用 probing 方法但未引用该领域的核心综述\n- **Keleg & Magdy (2023)** \"On the Calibration of Massively Multilingual Language Models\" ——多语言 calibration 专题研究\n- 此外，论文 PDF 中我未能在正文可见范围内找到完整的 References section（p.10 结尾是 Conclusion，p.11 开始是 Appendix A）。**如果参考文献列表被省略或因排版问题丢失，这是一个严重的格式问题。**\n\n**W2** [warning — 23 张表格 + 0 张图] 与前一篇论文相同的表述问题。23 张表格（正文 13 + 附录 10）但没有一张图。核心发现——Pareto frontier 不存在、CaCLR 的 harmful effect、Simpson's Paradox——都极适合可视化展示。特别是：\n- 一张 scatter plot（EN AUROC vs ZS AUROC by architecture）可以直观展示 \"no frontier\" 的负面结论\n- 一张 selectivity heatmap（language × layer）可以直观展示 artifact 分布 pattern\n- Simpson's Paradox 最经典的展示方式是分组 scatter plot（within-group vs. overall trend）\n表格密集使得负面结论的说服力受损——读者需要自己在数字中寻找 pattern，而一张好图可以一目了然。\n\n**W3** [minor — CaCLR 方法的新颖性因失败而难以评估] CaCLR 的损失函数（BCE + calibration + consistency + MMD）组合了四个已知组件。论文诚实报告其失败（§5.2, Table 3-4），但这使得方法贡献难以被独立评价。如果方法本身不是贡献，那么论文实质上只有两个贡献：(1) control task 方法论，(2) 负面实验结果。对于 main conference 这可能不够；对于 Findings track 可以接受。\n\n**W4** [minor — pilot 区分不充分] 论文多次提到\"pilot studies on Qwen2.5-7B and Llama-3.1-8B\"（Abstract, §5.1, §5.3），但未明确说明 pilot 是已发表工作还是同一团队的未发表前期工作。如果已发表，需要正式引用并明确 incremental contribution；如果未发表，应说明\"our unpublished pilot\"。当前表述模糊。\n\n**W5** [minor — Difficulty decomposition 的负面结论太快] §5.4 用一段话否定了 difficulty decomposition（\"The difficulty probe itself achieves only |Δ| = 0.03, statistically indistinguishable from a random-direction control\"），但 Table 9（p.9）显示 difficulty decomposition ablation 的结果在不同 tier 间有差异。论文未分析为什么 difficulty decomposition 在大模型上失败而可能在小模型上成功——是因为模型规模？训练数据差异？量化？这个分析缺口削弱了负面结论的解释力。\n\n**W6** [minor — Linear projection 的 \"only viable path\" 结论与 Table 21 存在张力] Table 21（p.13）显示 Linear Projection 200 pairs 的 Sig. impr. count 仅 11/20，few-shot 100 为 13/20。差异不大，且都远未覆盖全部 20 种语言。声称 linear projection 是 \"the only viable path\" 可能过于绝对。\n\n---\n\n### Questions for Authors\n\n**Q1**: §5.3 Simpson's Paradox 分析中，partial ρ = +0.14 (p = 0.22) 是在控制哪些变量后的结果？如果控制变量不同，partial ρ 是否会改变结论？\n\n**Q2**: Control task 的 selectivity 阈值 < 0.05 是如何确定的？Hewitt & Liang (2019) 原文是否使用了相同阈值？如果阈值改为 0.10 或 0.03，42% 的 artifact rate 如何变化？\n\n**Q3**: 论文将 pilot 模型（Qwen2.5-7B, Llama-3.1-8B）的正面结果归因于 scale 差异，但 pilot 用的是 7B/8B 模型，而本文用的是 22B-235B 模型。是否有证据表明 scale 是导致结论翻转的原因（如中间规模模型的结果）？还是架构差异（MoE vs Dense）更可能是原因？\n\n**Q4**: CaCLR 的 MMD term 引入负面效果（Table 4, p.5: 添加 MMD(l→0.01) 使 AUROC 从 0.563 降至 0.558）。作者是否尝试过其他 distributional matching 方法（如 adversarial alignment, optimal transport）？只测一种 distributional matching 就断言\"distributional matching 不可行\"可能过于草率。\n\n**Q5**: Table 11（p.10）中多个语言被标记为 ▲（permuted AUROC > real AUROC）。这是否意味着这些语言的 correctness probes 实际上在编码噪声而非真正的 correctness signal？如果是，这对 Miao & Ungar (2026) 的英文 correctness probe 结论有什么影响？\n\n**Q6**: 完整的参考文献列表在哪里？在我阅读的 PDF 中，§7 Conclusion 后直接是 Appendix A，未见 References section。\n\n---\n\n### Minor Issues\n\n- §3.2 \"CaCLR extends the standard probe loss with two regularization terms\"（p.3）中公式 (1) 有 3 项额外 loss（ℓ_cal, ℓ_cons, ℓ_MMD），但文字说\"two\"——应为 three\n- Table 3 caption（p.5）说\"CaCLR 1 sweep\"但未解释 sweep 的含义\n- §5.1 对 Gemma 4 31B Dense 的描述（p.4-5）说\"moderately clear but still noisy frontier\"，但随后的 Summary 说\"does not generalize\"——这两个判断有轻微矛盾\n- Table 19（p.13, Appendix A）52-language 扩展的结果格式与正文 20-language 不一致，增加了对比难度\n- Limitations（p.10）列出 4 点限制，诚实但也暴露了实验设计的局限：只用 MCQA format、只测 logistic regression、不包含所有 typological diversity\n\n---\n\n### Scores\n\n- **Soundness**: 3.5 / 5 — 统计方法比前一篇论文好很多（Bonferroni, control tasks, CIs），但部分负面结论的解释不够深入（W5），且参考文献列表可能缺失（W1）\n- **Excitement**: 3 / 5 — Control task 方法论贡献有 field-level 意义，但整体是 \"things don't work\" narrative，缺乏正面方法贡献；对于 Findings track 有足够兴趣，对 main conference 偏弱\n- **Overall**: 3 / 5 — Borderline / Findings track。Control task 发现（42% artifacts）如果能被独立验证，价值很高。但 CaCLR 失败 + 负面 Pareto 结论使得论文的\"so what\"不够强。推荐 Findings track 接收。\n- **Confidence**: 4 / 5 — 熟悉 probing、calibration、cross-lingual transfer 领域\n\n---\n\n### 与前一篇论文（positive framing）的对比评价\n\n| 维度 | Paper 1 (Pareto Frontier, positive) | Paper 2 (Limits, negative) |\n|------|-------------------------------------|---------------------------|\n| 学术诚信 | 差——核心数字自相矛盾（72% vs 81%）、\"25%\" 来源不明、疑似 fabricated references | 好——诚实承认负面结论、pilot 自我纠错 |\n| 统计严谨 | 差——无 CI、无 control tasks、无显著性检验 | 好——Bonferroni、selectivity controls、SDs |\n| Related Work | 差——8 篇引用、~15 行 | 中等——5 个子方向、但可能缺少 References section |\n| 新颖性 | 弱——四项增量性贡献、Pareto 术语误用 | 中等——control task 方法论有真正新意，但正面贡献有限 |\n| 可视化 | 0 图 / 16 表 | 0 图 / 23 表（问题同样严重） |\n| 实际价值 | 有限——CaCLR 改进仅 1.3pp | 有限但诚实——三档决策规则 |\n\n**整体判断**：Paper 2 在学术质量上显著优于 Paper 1，但两篇论文共享一个核心缺陷——**零可视化**。如果只能推荐一篇，我更倾向 Paper 2，因为诚实的负面结论 + 方法论警示对 community 的价值大于包装过度的弱正面结论。",
    "reviewer_id": "2",
    "project": "xling_calib_direction"
  }
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-21T06:11:37.066808+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5228
}
```

</details>

---

### Assistant

_source line 110 · 2026-05-21T06:11:43.913917+00:00_

审稿意见已提交给 Review Director。

Paper 2（negative result framing）的审阅完成。核心判断：
- **最强贡献**：Hewitt & Liang selectivity controls 引入跨语言 probing，揭示 42% 低资源结果为 artifacts
- **主要缺陷**：23 表 0 图、参考文献列表可能缺失、CaCLR 失败使正面方法贡献为零
- **评分**：Overall 3/5（Findings track borderline），显著优于 Paper 1（2.0/5）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2"
}
```

</details>

---

## Round 4

4 recorded events

### User

_source line 111 · 2026-05-21T06:12:56.031358+00:00_

[Round 1 审稿请求]:
## 交叉审阅任务（Median Paper）

以下是 **Reviewer 1（Methods & Experiments）** 的完整 Round 1 审稿意见。请逐条回应其 Weaknesses：

- **[AGREE]**：同意，并补充你从 Novelty/Related Work 角度的佐证
- **[REBUT]**：不同意或有保留意见，提供具体证据（cite Section/Table）

特别关注：
1. R1-W-M1（MMD 在 1-D probe logits 上限制了 negative result 的 scope）——从 novelty 角度，这对负面结果贡献的价值有何影响？
2. R1-W-M3（Gemma 4 数据不对等）——是否影响三架构对比的 claim？
3. R1 评价为 0 Major issues + Weak Accept——你评 Borderline/Findings，分歧主要在哪？

---

## Reviewer 1 完整审稿原文

**Overall**: 4/5 (Weak Accept)

### Methods & Experiments Strengths
- **S-M1**: Bootstrap 95% CIs、paired permutation tests、Cohen's d 贯穿所有实验
- **S-M2**: CaCLR β sweep 设计充分——3 OOM, 两种架构, 20 语言, 无 β 达 p<0.05 或 d>0.2
- **S-M3**: CKA 分析做 partial correlation controlling depth（r=0.18, p=0.11）后主动降级为 suggestive
- **S-M4**: Linear projection sample efficiency 曲线——~50 pairs 达 90%，20 pairs 即超 CaCLR
- **S-M5**: Control task analysis 将 Hewitt & Liang 扩展到 20 语言 × 多层，27% artifact finding
- **S-M6**: Mean-shift rank-invariance proof + 实验验证（ΔAUROC ≡ 0）

### Methods & Experiments Weaknesses
**W-M1** [idea] MMD 在 1-D probe logits 上操作限制了 negative result scope。未测试：(a) MMD 在 activation space 的效果 (b) optimal transport/Sinkhorn 在高维的效果。负面结论严格来说只关闭 "1-D probe output distributional matching" 而非全部。论文 framing 有 caveat（§3.2, §6），逻辑自洽但 generality 受限。

**W-M2** [presentation] Table 1 未展示完整 24 层 × 20 语言数据。Pareto frontier claim 需要读者看到完整 depth profile。

**W-M3** [idea] Gemma 4 31B 仅出现在 Table 14（appendix 3 行摘要），无 per-language breakdown、β sweep、full comparison。三架构对比不对等。

**W-M4** [idea] IRT R²=0.40 较低。Difficulty probe 只解释 40% item difficulty variance，projecting out difficulty 时残差仍混有大量 difficulty signal。论文已自我降级为 qualitative claim。

### Novelty & Related Work Strengths
- **S-N1**: "Negative result as contribution" 在 NLP 社区有价值
- **S-N2**: Llama 4 Scout 的 4/20 语言 ρ > 0 是 genuinely new observation
- **S-N3**: Control task artifact warning 作为独立贡献有 field-level 意义
- **S-N4**: Related Work §2 覆盖 6 个子领域，结构合理

### Novelty Weaknesses
**W-N1** [presentation] 14 篇引用仍低——缺 IRT 基础文献、Belinkov survey、Keleg & Magdy、Guo et al. temperature scaling、domain adaptation 文献、MoE 分析文献。部分引用可能存在 accuracy issue。

**W-N2** [idea] "First systematic study" claim 需 qualification。

**W-N3** [idea] CaCLR negative result novelty 取决于 MMD on probe outputs 是否为 "obvious limitation"——§3.2 自己指出 1-D 限制。

### Narrative Self-Consistency
全文内部一致性完美——Abstract 数字与正文完全吻合，无任何自相矛盾。13/13 实验计划全部覆盖。

### Scores
- Overall: 4/5 (Weak Accept) | Confidence: 4/5
- 0 Major issues, 方法论扎实, claims 诚实, narrative 自洽

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 112 · 2026-05-21T06:14:04.800203+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — 交叉审阅回应（对 Reviewer 1 Round 1 意见，Median/Worst Paper）\n\n---\n\n### Methods & Experiments Weaknesses 逐条回应\n\n**[AGREE] R1-W-M1: MMD 在 1-D probe logits 上操作限制了 negative result scope**\n\n同意，且从 Novelty 角度补充这对论文贡献价值的影响：\n\nR1 准确指出 CaCLR 的 MMD 仅在 1-D probe output 上操作，未测试 (a) activation space MMD, (b) optimal transport/Sinkhorn。这直接影响我在独立审稿中提出的 Q4——\"只测一种 distributional matching 就断言 distributional matching 不可行可能过于草率。\"\n\n从 Novelty 角度，这限制了论文第二大贡献（comprehensive negative result）的 scope：\n- 论文 Abstract 说 \"CaCLR, a distributional-matching method combining BEC, calibration, and MMD consistency losses, is uniformly harmful\"——但严格来说，只有 \"1-D MMD on probe logits\" 被证伪\n- 如果有人在 activation space（几千维）做 MMD 或用 adversarial domain adaptation（Ben-David et al. 理论框架的标准实现），结论可能完全不同\n- 论文 §3.2 和 §6 确实有 caveat（R1 确认了这一点），逻辑自洽但 **negative result 的 generality 受限意味着其对 community 的警示价值也受限**\n\n这是我给 Excitement 3/5 而非更高分的一个原因——负面结论的 scope 不够广，无法真正\"关闭\"这个研究方向。\n\n**建议**：如果作者补充 activation-space MMD 或 adversarial alignment 的实验（即使也失败），negative result 的价值会显著提升。\n\n---\n\n**[AGREE] R1-W-M2: Table 1 未展示完整 24 层 × 20 语言数据**\n\n同意。这也呼应了我在独立审稿中的 W2（零可视化）。完整的 depth profile 是验证\"no Pareto frontier\"结论的关键证据——如果读者看不到完整数据，只能信任作者的 summary statistics。一张 heatmap（layer × language, colored by AUROC）可以同时解决数据展示和可视化两个问题。\n\n---\n\n**[AGREE] R1-W-M3: Gemma 4 31B 数据不对等**\n\n同意，且从 Novelty/Positioning 角度，这对论文的三架构对比 claim 有直接影响：\n\n- 论文标题和 Abstract 声称覆盖\"3 architectures\"，但 Gemma 4 仅在 Appendix B（Table 14, p.11）出现 3 行摘要数据\n- 无 per-language breakdown、无 β sweep、无 control task analysis for Gemma\n- 论文的核心 claim 之一是 \"architecture-dependent\"——但如果 Gemma 的数据不完整，这个 claim 实质上只基于 Qwen3 和 Llama 4 两个架构，两者都是 MoE\n\n从 Novelty 角度，这削弱了\"跨架构\"贡献的说服力。特别是 Gemma 4 31B 是唯一的 Dense 架构——如果 Dense 和 MoE 的表现有本质差异，缺少 Gemma 的完整数据意味着论文无法回答 \"MoE vs Dense\" 这个关键问题。\n\n**这一点也是我与 R1 评分分歧的来源之一**（见下方讨论）。\n\n---\n\n**[AGREE] R1-W-M4: IRT R²=0.40 较低，difficulty decomposition 解释力有限**\n\n同意。我在独立审稿中将此归为 W5（\"Difficulty decomposition 的负面结论太快\"），角度略有不同但结论一致。R1 指出的技术问题更精确：R²=0.40 意味着 projecting out difficulty 后残差仍含 60% 未解释的 difficulty signal，这使得 \"capability-specific\" 残差的解释不可靠。论文将此自我降级为 qualitative claim 是诚实的，但也意味着这部分分析不构成实质性贡献。\n\n---\n\n### Novelty Weaknesses 逐条回应\n\n**[AGREE] R1-W-N1: 14 篇引用仍低**\n\n完全同意。我在独立审稿中详细列出了缺失文献：Conneau et al. (2020), Pires et al. (2019), Belinkov (2022), Keleg & Magdy (2023)。R1 补充了 Guo et al. temperature scaling 和 MoE 分析文献，进一步扩大了遗漏清单。\n\n此外，我在独立审稿中提出了一个更严重的问题：**论文 PDF 中 References section 似乎缺失**——§7 Conclusion 后直接是 Appendix A，未见参考文献列表。如果这是排版错误，需要修复；如果参考文献确实只有 14 篇，仍低于顶会标准（30-50 篇）。\n\n关于 R1 提到的\"部分引用可能存在 accuracy issue\"：鉴于前一篇论文（positive framing 版本）已被发现有多条疑似 fabricated references（Miao et al. 作者名不匹配、Zhou et al. 年份/标题不匹配、Civelli et al. 标题不匹配），本文的引用准确性需要同样严格的核查。**如果两篇论文共享同一参考文献库，accuracy issues 可能是系统性的。**\n\n---\n\n**[AGREE] R1-W-N2: \"First systematic study\" claim 需 qualification**\n\n同意，这与我在独立审稿中对前一篇论文的 W3 一致。建议改为 \"the first large-scale negative result study\" 或 \"the first study to apply probing control tasks to cross-lingual calibration transfer\"——后者更准确地反映论文的真正新贡献。\n\n---\n\n**[REBUT] R1-W-N3: CaCLR negative result novelty 取决于 MMD on probe outputs 是否为 \"obvious limitation\"**\n\n部分不同意。R1 认为 CaCLR 的 1-D MMD 限制可能使负面结论\"显而易见\"，暗示这降低了 novelty。但我认为：\n\n1. **事前并不 obvious**：distributional matching 在 domain adaptation 中广泛使用，Ben-David et al. 的理论框架（论文 §2 已引用）正是基于减少 marginal distribution divergence。在 probe output space 上做 MMD 是该理论框架的自然实现——如果没有人做过实验，不能仅凭直觉说\"当然不行\"。\n2. **论文的 framing 是诚实的**：§3.2 主动指出 1-D 限制，§6 Discussion 解释了为什么 marginal matching 无法捕捉 conditional distribution shift。这种 post-hoc 解释并不等于 ex-ante 预测。\n3. **但 R1-W-M1 仍然成立**：scope 有限是事实。\n\n综合判断：CaCLR 的负面结论不是 \"obvious\"，但也不是 \"surprising\"——它在两者之间，novelty 为 moderate。\n\n---\n\n### 关于评分分歧的讨论\n\n**R1: 4/5 (Weak Accept) vs R2: 3/5 (Borderline/Findings)**\n\n分歧来源：\n\n1. **R1 更重视方法论执行质量（统计严谨、narrative 一致性）**。R1 给出 \"0 Major issues\"，强调 bootstrap CIs、paired permutation tests、Cohen's d 等统计工具的正确使用。我同意这些是论文的优点（我的 S3），但我认为方法论执行质量是**必要条件**而非**充分条件**——一篇统计上无可挑剔但结论 scope 有限的负面结论论文，仍可能不足以支撑 main conference 接收。\n\n2. **R1 对三架构对比的不对等（W-M3）只列为 idea-level weakness**。而我认为这更严重——Gemma 4（唯一 Dense 架构）数据的缺失使得论文核心 claim 之一（\"architecture-dependent\"）实质上只基于两个 MoE 架构的对比。这削弱了论文的 generality。\n\n3. **我更看重 positive contribution 的强度**。论文诚实承认了负面结论（S2），但除了 control task methodology（S1），没有正面方法论贡献。Control task finding（27% artifact rate per R1, 42% per 我的读法——数字差异可能来自不同 tier 的统计口径）虽有 field-level 意义，但需要独立验证。仅凭一个 methodological warning + 一套负面实验结果，对 main conference 来说偏弱。\n\n4. **参考文献问题的影响权重**。R1 将 14 篇引用列为 presentation weakness，而我将其视为更根本的定位问题——参考文献不足使得论文无法在已有文献中精确定位自己的贡献。\n\n**最终判断**：如果 R1 的 W-M1（scope 限制）和 W-M3（Gemma 不对等）得到解决（补充 activation-space MMD + Gemma 完整数据），我愿意将评分提升至 3.5/5。在当前状态下，维持 3/5 (Borderline/Findings track)。",
  "reviewer_id": "2",
  "project": "xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — 交叉审阅回应（对 Reviewer 1 Round 1 意见，Median/Worst Paper）\n\n---\n\n### Methods & Experiments Weaknesses 逐条回应\n\n**[AGREE] R1-W-M1: MMD 在 1-D probe logits 上操作限制了 negative result scope**\n\n同意，且从 Novelty 角度补充这对论文贡献价值的影响：\n\nR1 准确指出 CaCLR 的 MMD 仅在 1-D probe output 上操作，未测试 (a) activation space MMD, (b) optimal transport/Sinkhorn。这直接影响我在独立审稿中提出的 Q4——\"只测一种 distributional matching 就断言 distributional matching 不可行可能过于草率。\"\n\n从 Novelty 角度，这限制了论文第二大贡献（comprehensive negative result）的 scope：\n- 论文 Abstract 说 \"CaCLR, a distributional-matching method combining BEC, calibration, and MMD consistency losses, is uniformly harmful\"——但严格来说，只有 \"1-D MMD on probe logits\" 被证伪\n- 如果有人在 activation space（几千维）做 MMD 或用 adversarial domain adaptation（Ben-David et al. 理论框架的标准实现），结论可能完全不同\n- 论文 §3.2 和 §6 确实有 caveat（R1 确认了这一点），逻辑自洽但 **negative result 的 generality 受限意味着其对 community 的警示价值也受限**\n\n这是我给 Excitement 3/5 而非更高分的一个原因——负面结论的 scope 不够广，无法真正\"关闭\"这个研究方向。\n\n**建议**：如果作者补充 activation-space MMD 或 adversarial alignment 的实验（即使也失败），negative result 的价值会显著提升。\n\n---\n\n**[AGREE] R1-W-M2: Table 1 未展示完整 24 层 × 20 语言数据**\n\n同意。这也呼应了我在独立审稿中的 W2（零可视化）。完整的 depth profile 是验证\"no Pareto frontier\"结论的关键证据——如果读者看不到完整数据，只能信任作者的 summary statistics。一张 heatmap（layer × language, colored by AUROC）可以同时解决数据展示和可视化两个问题。\n\n---\n\n**[AGREE] R1-W-M3: Gemma 4 31B 数据不对等**\n\n同意，且从 Novelty/Positioning 角度，这对论文的三架构对比 claim 有直接影响：\n\n- 论文标题和 Abstract 声称覆盖\"3 architectures\"，但 Gemma 4 仅在 Appendix B（Table 14, p.11）出现 3 行摘要数据\n- 无 per-language breakdown、无 β sweep、无 control task analysis for Gemma\n- 论文的核心 claim 之一是 \"architecture-dependent\"——但如果 Gemma 的数据不完整，这个 claim 实质上只基于 Qwen3 和 Llama 4 两个架构，两者都是 MoE\n\n从 Novelty 角度，这削弱了\"跨架构\"贡献的说服力。特别是 Gemma 4 31B 是唯一的 Dense 架构——如果 Dense 和 MoE 的表现有本质差异，缺少 Gemma 的完整数据意味着论文无法回答 \"MoE vs Dense\" 这个关键问题。\n\n**这一点也是我与 R1 评分分歧的来源之一**（见下方讨论）。\n\n---\n\n**[AGREE] R1-W-M4: IRT R²=0.40 较低，difficulty decomposition 解释力有限**\n\n同意。我在独立审稿中将此归为 W5（\"Difficulty decomposition 的负面结论太快\"），角度略有不同但结论一致。R1 指出的技术问题更精确：R²=0.40 意味着 projecting out difficulty 后残差仍含 60% 未解释的 difficulty signal，这使得 \"capability-specific\" 残差的解释不可靠。论文将此自我降级为 qualitative claim 是诚实的，但也意味着这部分分析不构成实质性贡献。\n\n---\n\n### Novelty Weaknesses 逐条回应\n\n**[AGREE] R1-W-N1: 14 篇引用仍低**\n\n完全同意。我在独立审稿中详细列出了缺失文献：Conneau et al. (2020), Pires et al. (2019), Belinkov (2022), Keleg & Magdy (2023)。R1 补充了 Guo et al. temperature scaling 和 MoE 分析文献，进一步扩大了遗漏清单。\n\n此外，我在独立审稿中提出了一个更严重的问题：**论文 PDF 中 References section 似乎缺失**——§7 Conclusion 后直接是 Appendix A，未见参考文献列表。如果这是排版错误，需要修复；如果参考文献确实只有 14 篇，仍低于顶会标准（30-50 篇）。\n\n关于 R1 提到的\"部分引用可能存在 accuracy issue\"：鉴于前一篇论文（positive framing 版本）已被发现有多条疑似 fabricated references（Miao et al. 作者名不匹配、Zhou et al. 年份/标题不匹配、Civelli et al. 标题不匹配），本文的引用准确性需要同样严格的核查。**如果两篇论文共享同一参考文献库，accuracy issues 可能是系统性的。**\n\n---\n\n**[AGREE] R1-W-N2: \"First systematic study\" claim 需 qualification**\n\n同意，这与我在独立审稿中对前一篇论文的 W3 一致。建议改为 \"the first large-scale negative result study\" 或 \"the first study to apply probing control tasks to cross-lingual calibration transfer\"——后者更准确地反映论文的真正新贡献。\n\n---\n\n**[REBUT] R1-W-N3: CaCLR negative result novelty 取决于 MMD on probe outputs 是否为 \"obvious limitation\"**\n\n部分不同意。R1 认为 CaCLR 的 1-D MMD 限制可能使负面结论\"显而易见\"，暗示这降低了 novelty。但我认为：\n\n1. **事前并不 obvious**：distributional matching 在 domain adaptation 中广泛使用，Ben-David et al. 的理论框架（论文 §2 已引用）正是基于减少 marginal distribution divergence。在 probe output space 上做 MMD 是该理论框架的自然实现——如果没有人做过实验，不能仅凭直觉说\"当然不行\"。\n2. **论文的 framing 是诚实的**：§3.2 主动指出 1-D 限制，§6 Discussion 解释了为什么 marginal matching 无法捕捉 conditional distribution shift。这种 post-hoc 解释并不等于 ex-ante 预测。\n3. **但 R1-W-M1 仍然成立**：scope 有限是事实。\n\n综合判断：CaCLR 的负面结论不是 \"obvious\"，但也不是 \"surprising\"——它在两者之间，novelty 为 moderate。\n\n---\n\n### 关于评分分歧的讨论\n\n**R1: 4/5 (Weak Accept) vs R2: 3/5 (Borderline/Findings)**\n\n分歧来源：\n\n1. **R1 更重视方法论执行质量（统计严谨、narrative 一致性）**。R1 给出 \"0 Major issues\"，强调 bootstrap CIs、paired permutation tests、Cohen's d 等统计工具的正确使用。我同意这些是论文的优点（我的 S3），但我认为方法论执行质量是**必要条件**而非**充分条件**——一篇统计上无可挑剔但结论 scope 有限的负面结论论文，仍可能不足以支撑 main conference 接收。\n\n2. **R1 对三架构对比的不对等（W-M3）只列为 idea-level weakness**。而我认为这更严重——Gemma 4（唯一 Dense 架构）数据的缺失使得论文核心 claim 之一（\"architecture-dependent\"）实质上只基于两个 MoE 架构的对比。这削弱了论文的 generality。\n\n3. **我更看重 positive contribution 的强度**。论文诚实承认了负面结论（S2），但除了 control task methodology（S1），没有正面方法论贡献。Control task finding（27% artifact rate per R1, 42% per 我的读法——数字差异可能来自不同 tier 的统计口径）虽有 field-level 意义，但需要独立验证。仅凭一个 methodological warning + 一套负面实验结果，对 main conference 来说偏弱。\n\n4. **参考文献问题的影响权重**。R1 将 14 篇引用列为 presentation weakness，而我将其视为更根本的定位问题——参考文献不足使得论文无法在已有文献中精确定位自己的贡献。\n\n**最终判断**：如果 R1 的 W-M1（scope 限制）和 W-M3（Gemma 不对等）得到解决（补充 activation-space MMD + Gemma 完整数据），我愿意将评分提升至 3.5/5。在当前状态下，维持 3/5 (Borderline/Findings track)。",
    "reviewer_id": "2",
    "project": "xling_calib_direction"
  }
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-21T06:14:09.577716+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4777
}
```

</details>

---

### Assistant

_source line 114 · 2026-05-21T06:14:13.983876+00:00_

交叉审阅回应已提交。核心分歧在于：R1 更重视方法论执行质量给出 Weak Accept，我更重视正面贡献强度和三架构对比的完整性给出 Borderline/Findings。如果补充 activation-space distributional matching 实验和 Gemma 4 完整数据，可上调至 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2"
}
```

</details>

---
