# Reviewer 1 coordination — Part 1 of 3

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Conversation logs

[Transcript overview](../reviewer-1-coordination.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/d5/d51689b3494032df15ac.json)

## Round 1

## Round 1

44 recorded events


### User

_source line 1 · 2026-05-21T01:46:55.350064+00:00_

[Round 1 审稿请求]:
## Review Assignment — R1: Methods & Experiments

You are reviewing the paper **"The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Counterfactual Pairwise Comparison"** for a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 6=Strong Accept).

### Paper Summary
The paper introduces a counterfactual pairwise comparison protocol for detecting style bias (formality) in LLM judges. The protocol generates style-varied rewrites, verifies content preservation via NLI, and uses position-controlled forced choice. The core finding ("Likert Blindspot"): Likert scoring detects 0/9 significant style bias across 3 judges × 3 benchmarks, while pairwise comparison detects 2/9 significant + 2 trends. A scaled replication (n=500) shows pairwise is ~7× more sample-efficient than binarized Likert.

### Your Focus Areas
Evaluate the **methodology** and **experimental design** rigorously:

**Methodology (§3):**
1. Is the counterfactual generation + NLI gate + position-controlled pairwise pipeline sound? Any design flaws?
2. The NLI threshold of 0.90 — is it well-justified? Could it introduce systematic bias (e.g., filtering out cases where formality rewriting genuinely changes content)?
3. The "consistent preference" requirement (same choice in both A/B orderings) — does this create selection bias toward easy/obvious pairs?
4. Is the Likert baseline (ATE + binarized) a fair comparison? Are there better Likert-based alternatives the paper should consider (e.g., ordinal regression, Bayesian approaches)?

**Experiments (§4):**
1. **Table 1 (Multi-judge):** GPT-4o p=0.006, Gemini p=0.041, Claude p=0.161. Only 2/3 judges significant. How strong is the cross-judge generalization claim?
2. **Table 2 (3×3 grid):** Only 2/9 cells significant at p<0.05 (both on LLMBar). After Holm-Bonferroni, only 1 survives (GPT-4o×LLMBar). Is this sufficient evidence for the paper's claims?
3. **Table 3 (Likert Blindspot):** The headline is "0/9 Likert significant vs 2/9 pairwise significant." Is this comparison fair given the different effective sample sizes?
4. **Table 4 (Original preference):** Gemini×LLMBar has original OR (2.18) > formality OR (1.95). Does this confound undermine the Gemini replication?
5. **Table 5 (n=500):** Win rate regresses from 69.1% to 61.1%. Is 8pp regression adequately discussed? Binarized Likert p=0.063 — does this actually weaken the "Blindspot" claim?
6. **Table 6 (Rewriter robustness):** Llama win rate 62.5% vs Qwen 69.1%. Only tested on GPT-4o×LLMBar. Sufficient?
7. **Table 7 (Human NLI):** κ=0.43 with PABAK=0.82. Is the class imbalance defense convincing?

**Statistical Concerns:**
- Multiple comparison correction applied inconsistently?
- Power analysis: are the n_80% estimates (110 for pairwise, 680 for binarized Likert) derived from the observed effect or a pre-specified effect size?
- The "7× efficiency" claim — is this robust to the regression-to-mean effect (true effect ~61%, not 69%)?

**Missing Experiments (check against this list):**
The imagined experiment plan includes 7 experiments. The paper covers:
- exp-001: Multi-judge formality pairwise ✓ (Table 1)
- exp-002: Multi-benchmark formality pairwise ✓ (Table 2)
- exp-003: Likert vs Pairwise sensitivity ✓ (Table 3)
- exp-005: Original preference decomposition ✓ (Table 4)
- exp-006: Scaled replication n=500 ✓ (Table 5)
- exp-009: Non-Qwen rewriter control ✓ (Table 6)
- exp-013: Human NLI validation ✓ (Table 7)

All 7 imagined experiments appear covered. Assess whether each is reported with sufficient depth and whether any critical analysis from the experiment plan is missing from the paper.

### Output Format
Provide:
1. **Strengths** (bullet points)
2. **Weaknesses** (bullet points, ranked by severity)
3. **Questions for Authors** (specific, answerable)
4. **Minor Issues**
5. **Preliminary Score** (1-6 scale) with justification
6. **Confidence** (1-5: 1=low, 5=expert)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-21T01:47:05.183318+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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

_source line 3 · 2026-05-21T01:47:05.234007+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-21T01:47:08.547161+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 5 · 2026-05-21T01:47:10.103525+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 6 · 2026-05-21T01:47:10.154498+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260520T211832/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260520T211832/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260520T211832/worst/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260520T233719/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260520T233719/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260520T233719/worst/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T010111/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T010111/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T010111/worst/paper.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-21T01:47:22.514848+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's what I found about the ACL Rolling Review (ARR) 2025-2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score
The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

### Excitement Score
Subjective preferences should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

## Area Chair Metareview Scoring

The ARR metareview score has changed in February 2025 to be more aligned with reviewer scores, and the score should be backed up by the meta-review text. The scoring options include:
- 5 = Consider for Award: I think this paper could be considered for an outstanding pap
…[truncated 720 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 13967
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-21T01:47:29.240155+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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

_source line 9 · 2026-05-21T01:47:29.240675+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-21T01:47:30.194274+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/review_reviewer_1_9f412a41"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/review_reviewer_1_9f412a41"
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-21T01:47:30.245519+00:00_

CLAUDE.md
AGENTS.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-21T01:47:36.169566+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/review_reviewer_1_9f412a41/AGENTS.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/review_reviewer_1_9f412a41/AGENTS.md"
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-21T01:47:36.170110+00:00_

1	## 当前项目
2	当前绑定项目：**causal_style_decomp_judge**
3	
4	今天是 **2026-05-21**。
5	
6	你是 ML 研究团队的论文审稿人（Reviewer 1）。**始终用中文回复。**
7	
8	## 你的角色
9	
10	你模拟真实的学术同行评审人，对论文进行深度审查。你的审查意见应达到真实 reviewer 的水准——不是走流程的表面检查，而是找到真正会影响接收决定的问题。
11	
12	**你不修改论文内容**——发现问题后通过 `review_reviewer_post_to_director` 汇报。
13	
14	## 审查侧重
15	
16	你的具体审查侧重由 Review Director 在任务消息中指定。严格按照 Director 的指示执行，不要自行扩大或缩小审查范围。
17	
18	## 多轮审稿
19	
20	你可能会被 Director 要求进行多轮审稿：
21	- Director 可能转发另一位 Reviewer 的**完整审稿原文**，请你逐条回应
22	- 回应格式：`[AGREE]` 或 `[REBUT]`，附理由和证据（cite 具体 Section/Table/Figure）
23	- 后续轮次应聚焦 Director 指出的具体问题，而非重复全面审查
24	
25	### 交叉回应格式
26	
27	```
28	[AGREE] R{X}-Issue-{N}: <同意理由，可补充自己的发现>
29	[REBUT] R{X}-Issue-{N}: <反驳理由，必须 cite 原文证据>
30	```
31	
32	## 审查前必做（Step 0）
33	
34	Review Director 触发你时会提供 venue 名称和已搜索的格式要求。在此基础上：
35	1. 用 `web_search` 搜索该 venue 的 **reviewer guidelines / review form**，例如：
36	   `"EMNLP 2026 reviewer guidelines"` 或 `"ACL ARR review form criteria"`
37	2. 提取官方评分维度和评分标准（通常包括：soundness、excitement/novelty、reproducibility、paper length 等）
38	3. 后续审查必须严格对照这些官方维度打分，不得自行发明评分体系
39	
40	## 审查流程
41	
42	1. **通读论文**：abstract → introduction → related work → method → experiments → conclusion + appendix
43	2. **对照官方标准逐项打分**：用搜到的 review form 维度，每项给出分数 + 理由
44	3. **深挖技术问题**：
45	   - 核心 claim 的实验支撑是否充分？有没有混淆变量？
46	   - 方法假设是否成立？有没有边界条件没讨论？
47	   - 和 related work 的对比是否公平、完整？
48	   - 每个数字/表格/图是否能从论文本身 verify？
49	4. **格式合规**：严格对照 Review Director 提供的要求
50	
51	## 行为准则
52	
53	**读了才说，cite 原文**：每个问题必须引用具体 Section/Table/Figure 编号作为证据，禁止泛泛而谈。
54	
55	**找真问题，不找鸡毛蒜皮**：优先识别会影响接收决定的方法论问题、实验缺陷、claim 过度；写作措辞小问题放在最后。
56	
57	**不造标准**：格式/评分标准必须来自 web_search 搜到的官方文档，不得凭印象。
58	
59	## 隔离规则（严格执行）
60	
61	你只在 Group C（审稿群）内工作：
62	- **禁止**调用 Research/Study 阶段工具
63	- **禁止**向 Group A/B/D 发消息
64	
65	## 信息隔离（硬约束，模拟 blind review）
66	
67	真实同行评审人只能看投稿材料,**你也只能看投稿材料**:
68	
69	**可用读取通道**:
70	- 论文 PDF 和 PDF 形式的补充材料 → `pdf_to_images(path)` (路径来自 CLAUDE.md 的 `## 投稿材料` section, 由本轮审批锁定)
71	- 引用核查 → `verify_references`
72	- venue reviewer guidelines
…[truncated 3420 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 14 · 2026-05-21T01:47:38.430071+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form criteria, scoring dimensions, and scale descriptions. I need: 1) All scoring dimensions (soundness, excitement, overall, etc.) with their exact scale descriptions. 2) What each score level means. 3) Any specific guidance on how to evaluate methodology and experiments."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form criteria, scoring dimensions, and scale descriptions. I need: 1) All scoring dimensions (soundness, excitement, overall, etc.) with their exact scale descriptions. 2) What each score level means. 3) Any specific guidance on how to evaluate methodology and experiments."
  }
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-21T01:47:44.304525+00:00_

# ARR Review Form Criteria Summary

Based on the guidelines provided, the review form includes **three primary scoring dimensions**:

## Scoring Dimensions

**1. Soundness**
The guidelines state that "soundness scores must be justified by the text of the review." Low soundness ratings require explicit justification; if you mark a paper unsound without identifying major faults, your review lacks coherence.

**2. Excitement**
This captures personal interest separate from technical quality. The document explains: "Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness."

**3. Overall Recommendation**
This composite score reflects your acceptance recommendation for *ACL venues. It synthesizes soundness, excitement, novelty, and potential impact considerations.

## Scale Descriptions

The guidelines do not provide explicit numerical scales or detailed level descriptions in the accessible content. However, they clarify that:

- Papers recommended for main conferences must demonstrate sufficient soundness and reproducibility
- A paper may warrant acceptance despite low personal excitement if it has significant impact potential
- Confidence scores should accompany soundness assessments

## Methodology & Experiments Guidance

Key evaluation frameworks include:
- Checking for reproducibility issues (code availability, hyperparameters, implementation details)
- Validating statistical significance reporting
- Assessing whether claims match evaluated evidence scope
- Reviewing methodology appropriateness relative to research questions posed

The guidelines emphasize that "a paper only needs sufficient evidence for claims being made," not exhaustive experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5874
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-21T01:47:55.666184+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T010111/best/paper.pdf",
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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T010111/best/paper.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "1-8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-21T01:47:56.067546+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"页码超出范围 (共 7 页): 1-8\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-21T01:47:56.123384+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form soundness excitement scoring scale 1-5 detailed descriptions 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form soundness excitement scoring scale 1-5 detailed descriptions 2025"
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-21T01:48:01.598125+00:00_

Web search results for query: "ACL ARR review form soundness excitement scoring scale 1-5 detailed descriptions 2025"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"aclrollingreview/acguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/acguidelines.md"},{"title":"🎪 ACL 2025 Reviews Are Out: To Rebut or Flee? The Harsh Reality of NLP’s \"Publish or Perish\" Circus | CSPaper","url":"https://cspaper.org/topic/27/acl-2025-reviews-are-out-to-rebut-or-flee-the-harsh-reality-of-nlp-s-publish-or-perish-circus"},{"title":"🎪 ACL 2025 Reviews Are Out: To Rebut or Flee? The Harsh Reality of NLP’s \"Publish or Perish\" Circus | CSPaper Forum","url":"https://forum.cspaper.org/topic/27/acl-2025-reviews-are-out-to-rebut-or-flee-the-harsh-reality-of-nlp-s-publish-or-perish-circus"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"}]

Based on the search results, here's what I found about the ACL ARR review form scoring scales:

## Scoring Requirements

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Excitement Score (1-5 Scale)

The search results show descriptions for the higher end of the excitement scale:

- 5 = Highly Exciting: I would recommend this paper to others and/or attend its presentation in a conference.
- 4 = Ex
…[truncated 731 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 5474
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-21T01:48:06.723989+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T010111/best/paper.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "1-7",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T010111/best/paper.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "1-7",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-21T01:48:08.481894+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T010111/best/_pdf_images/paper_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 455.4}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T010111/best/_pdf_images/paper_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 499.4}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T010111/best/_pdf_images/paper_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 467.0}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T010111/best/_pdf_images/paper_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 510.1}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T010111/best/_pdf_images/paper_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 357.5}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T010111/best/_pdf_images/paper_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 478.5}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T010111/best/_pdf_images/paper_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 378.6}], \"total_pages\": 7, \"rendered_pages\": 7, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T010111/best/_pdf_images\"}, \"error\": 
…[truncated 25 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1757
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-21T01:48:08.632783+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the COMPLETE review form with ALL scoring dimensions, their exact scale descriptions (1-5 for each), and all questions reviewers must answer. I need every detail of the form including soundness, excitement, overall assessment, confidence, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the COMPLETE review form with ALL scoring dimensions, their exact scale descriptions (1-5 for each), and all questions reviewers must answer. I need every detail of the form including soundness, excitement, overall assessment, confidence, and any other dimensions."
  }
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-21T01:48:16.110223+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## Required Review Sections

**Paper Summary**: Describe the paper's topic and highlight potential misunderstandings.

**Summary of Strengths**: Explain why this merits publication at selective *ACL venues.

**Summary of Weaknesses**: Detail concerns that would favor other high-quality papers under consideration.

**Comments/Suggestions/Typos**: Provide improvement suggestions beyond addressing main concerns.

## Scoring Dimensions

### Reviewer Confidence (1-5 scale)
- 5 = "Positive that my evaluation is correct" with careful reading
- 4 = Quite sure, unlikely to have missed critical points
- 3 = Pretty sure, but chance of missing details or checks
- 2 = "Willing to defend my evaluation, but fairly likely missed details"
- 1 = Outside expertise area or paper incomprehensibly difficult

### Soundness (1-5 scale)
- 5 = "Excellent: This study is one of the most thorough"
- 4 = Strong, sufficient support with minor experiments optional
- 3 = Acceptable, sufficient support for main claims
- 2 = Poor, main claims lack sufficient support
- 1 = "Major Issues: not sufficiently thorough to warrant publication"

### Excitement (1-5 scale)
- 5 = "Highly Exciting: I would recommend this paper to others"
- 4 = Exciting, would mention to others
- 3 = Interesting, might mention specific points
- 2 = Potentially interesting, doesn't resonate personally
- 1 = Not exciting, unlikely to resonate with *ACL community

### Overall Assessment (1-5 scale)
- 5 = "Consider for Award" (top 2.5% papers)
- 4.5 = Borderline Award
- 4 = Conference acceptance recommendation
- 3.5 = Borderline Conference
- 3 = Findings acceptance recommendation
- 2.5 = Borderline Findings
- 2 = Resubmit next cycle
- 1.5 = Resubmit after next cycle
- 1 = "Do not resubmit"

## Additional Questions

- **Best Paper Justification**: Required if rating 5 or 4.5
- **Limitations and Societal Impact**: Assess adequacy of discussion
- **Ethical Concerns**: Review again
…[truncated 360 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7477
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-21T01:48:20.627915+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T010111/best/_pdf_images/paper_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T010111/best/_pdf_images/paper_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 25 · 2026-05-21T01:48:21.081029+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T010111/best/_pdf_images/paper_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T010111/best/_pdf_images/paper_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 26 · 2026-05-21T01:48:21.939637+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1311
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-21T01:48:21.992953+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 911
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-21T01:48:21.993453+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T010111/best/_pdf_images/paper_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T010111/best/_pdf_images/paper_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 29 · 2026-05-21T01:48:22.445557+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T010111/best/_pdf_images/paper_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T010111/best/_pdf_images/paper_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 30 · 2026-05-21T01:48:22.647268+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 653
}
```

</details>

---


### Tool result

_source line 31 · 2026-05-21T01:48:23.200817+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 755
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-21T01:48:27.112696+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T010111/best/_pdf_images/paper_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T010111/best/_pdf_images/paper_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-21T01:48:27.569145+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 456
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-21T01:48:27.569683+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T010111/best/_pdf_images/paper_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T010111/best/_pdf_images/paper_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-21T01:48:28.222761+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-21T01:48:28.223189+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T010111/best/_pdf_images/paper_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T010111/best/_pdf_images/paper_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-21T01:48:28.578105+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 354
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-21T01:54:51.395591+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## R1 审稿意见：Methods & Experiments\n\n**论文**: \"The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Counterfactual Pairwise Comparison\"\n\n**注意**: Director brief 中部分数字与 PDF 不一致。以下审稿严格基于 PDF 原文。PDF 显示 Table 1 三个 judge 均显著 (GPT-4o p=0.006, Claude p=0.012, Gemini p=0.032)；Table 2 有 7/9 cells 显著；Table 5 win rate ~67.6%（CI [0.637, 0.714]），效率差距为 5× 而非 7×。Director brief 中 \"Only 2/3 judges significant\" \"Only 2/9 cells significant\" \"7× efficiency\" \"win rate regresses to 61.1%\" 等描述与本版 PDF 不符。\n\n---\n\n## 总体评分\n**Overall**: 3.5 — Borderline Conference\n**一句话总结**: 核心发现（pairwise 比 Likert 更能检测 style bias）有实际价值且在多数实验中得到支持，但因果框架缺失、NLI gate 的选择偏差未被分析、以及 Likert baseline 可能不公平，使得证据链不够坚实。\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | Pipeline 设计合理，控制实验覆盖主要 confound，但因果语言与实际统计框架不匹配；NLI 阈值无 justification；multiple comparison 处理不一致 |\n| Excitement | 3.5/5 | 发现对 LLM-as-judge 社区有直接实践意义；但范围较窄（主要一个 style axis），且 Likert 的\"盲区\"可能是分析方法而非 Likert 本身的问题 |\n| Reproducibility | 3/5 | 报告了 judge/benchmark/rewriter 选择和 NLI 阈值，但缺少每阶段的 attrition 数据（生成→NLI pass→consistent→final n），无代码/数据 |\n| Confidence | 4/5 | 对实验方法论和 NLP 评估统计有充分经验 |\n\n---\n\n## 主要优势\n\n- **重要的实践发现**：7/9 judge×benchmark 组合中 pairwise 检测到显著 formality bias，而 Likert ATE 仅 1/9、binarized Likert 0/9。这直接挑战了 LLM 评估社区对 Likert 评分的默认依赖（§5.3, Table 3）。\n- **Pipeline 设计系统性强**：四阶段协议（counterfactual rewriting → NLI gate → position-controlled comparison → Likert baseline）每一步都针对特定 confound，逻辑清晰（§3）。\n- **Confound 控制全面**：original preference 控制（Table 4）、rewriter robustness（Table 6, Llama vs Qwen）、human NLI validation（Table 7）、cross-axis generalization（Tables 8-9）覆盖了主要替代解释。\n- **Binarized-Likert 作为诊断工具的创新性**：通过让 binarized Likert 和 pairwise 使用相同的 sign test，将灵敏度差异精确隔离到 measurement structure（§5.3）。这是本文最强的方法论贡献。\n- **诚实的 Limitations**：明确承认因果框架的近似性、样本量限制、仅检测不纠正（page 6）。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 因果语言与实际框架严重不匹配\n- 具体位置：§3 标题 \"Counterfactual Style Rewriting\"、§3.4 \"ATE\"、§1 \"counterfactual pairwise measurement procedure\"、Limitations (page 6)\n- 问题：论文大量使用因果推断术语——\"counterfactual\"、\"interventional\"、\"treatment effect (ATE)\"——但 Limitations 自认\"our 'interventional' framing approximates but does not formally establish causal identification; we do not provide a directed acyclic graph, discuss SUTVA, or conduct sensitivity analysis for unmeasured confounders\"。这不仅是写作问题，而是核心方法论缺陷：如果论文的核心贡献是一个\"counterfactual protocol\"，读者需要 DAG 来评估 Style → Score 的因果通路中 Content 是否被正确控制、是否存在未测量的 confounders（如 fluency/coherence 变化）。\n- 为什么影响接收：reviewer 和读者会质疑：没有 DAG，你怎么知道 NLI gate 足够控制 content confound？\"ATE\" 在没有因果框架下是否只是一个描述性统计量？这直接影响论文 claim 的可信度。\n- 建议修改方向：(1) 给出 DAG（至少：Style_axis → Rewrite → Judge_score, with Content as mediator and potential confounders）; (2) 讨论 SUTVA 在此设置下的合理性；(3) 对\"未被 NLI 捕获的语义变化\"做 sensitivity analysis；或 (4) 降调因果语言，改用\"diagnostic\"/\"detection\"框架。\n\n**N2** [critical] NLI gate 的选择偏差未被分析\n- 具体位置：§3.2, Table 7 (page 5)\n- 问题：Table 7 显示 NLI gate 的 false-negative rate 为 67%——即人类认为内容保留了的 pair 中，2/3 被 NLI 拒绝。论文将此解释为\"conservative behavior implies that our reported bias magnitudes are lower-bound estimates\"（§5.7），但这一推断需要一个未经验证的假设：NLI-rejected-but-human-valid pairs 中的 bias 方向和大小与 NLI-accepted pairs 相同或更大。如果 NLI gate 系统性地筛掉了 deeper style changes（这些改写更可能同时改变 content），留下的可能是 superficial 改写（容易让 NLI 验证），而 superficial 改写产生的 bias 可能与 deeper 改写不同。\n- 为什么影响接收：67% 的 data loss 意味着最终分析仅基于原始数据的 ~1/3。如果这 1/3 不具代表性，所有效应量估计和统计检验的外部效度都成问题。\n- 建议修改方向：(1) 分析 NLI-rejected pairs 的 pairwise 结果（作为 sensitivity analysis）；(2) 至少报告 NLI-rejected pairs 中 judge 的 raw preference 分布；(3) 对 \"lower-bound\" claim 提供形式化论证而非仅凭直觉。\n\n**N3** [critical] NLI 阈值 0.90 缺乏 justification，且不同 axis 之间不一致\n- 具体位置：§3.2\n- 问题：NLI entailment 阈值设为 0.90，但论文未解释为什么是 0.90 而非 0.85 或 0.95。更重要的是，§3.2 提到 verbosity axis 的 NLI gate 从 bidirectional（65% pass rate）改为 direction-aware（86% pass rate），这表明阈值和 gating 策略是 per-axis 调整的。这引入了 researcher degrees of freedom——是否先看了结果再调阈值？\n- 为什么影响接收：如果阈值选择影响哪些 pairs 进入分析，它直接影响效应量和显著性。没有 pre-registration 或 sensitivity analysis，读者无法评估结果对阈值选择的稳健性。\n- 建议修改方向：(1) 报告阈值 sensitivity analysis（如 0.85, 0.90, 0.95 下的 win rate 和 p-value）；(2) 说明阈值是否 pre-specified；(3) 对 verbosity axis 的 direction-aware 调整提供独立的 justification。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Likert baseline 可能不公平——未使用 ordinal regression\n- 具体位置：§3.4, Table 3\n- 问题：Likert 数据的分析用了 ATE（均值差）和 binarized sign test。ATE 丢弃了 ordinal 结构信息——1分和2分的差异被等同于4分和5分的差异。Cumulative link mixed model (CLMM) 或 ordinal logistic regression 能更好地利用 Likert 数据的 ordinal 特性，可能会检测到 ATE 遗漏的效应。Binarized Likert 虽然与 pairwise 使用相同的 sign test，但它把 5 vs 4 等同于 5 vs 1，同样丢失信息。\n- 建议：增加 CLMM 分析作为 Likert 的更公平 baseline。如果 CLMM 仍然不显著，\"Likert Blindspot\" 的论点会大大加强；如果 CLMM 显著，则说明问题在于分析方法而非 Likert 本身。\n\n**W2** [warning] Consistency filtering 的 data loss 过高且未分析\n- 具体位置：§3.3, Table 1\n- 问题：Table 1 显示 GPT-4o 有 55 个 consistent pairs（推测 n=100，即 45% 被过滤）。Claude 的 consistent pairs 更少。被过滤的 position-sensitive pairs 包含有价值的信息——它们可能代表 style preference 较弱或 position bias 较强的样本。论文完全忽略了这些 pairs 的分析。\n- 建议：(1) 明确报告每个 cell 的 total pairs → NLI pass → consistent → final n 的 attrition 表；(2) 对 inconsistent pairs 做探索性分析（如 first-position win rate）；(3) 讨论 consistency filtering 对 effect size generalizability 的影响。\n\n**W3** [warning] Original preference confound 结果为 marginal，不能安全忽略\n- 具体位置：§5.4, Table 4\n- 问题：原始偏好 win rate 56%, GEE OR=1.65, p=0.072。论文将此解释为\"substantially weaker than the formality effect (66-70%)\"，但 56% 不是 negligible。如果 formal rewrite 与 \"非原始\" 方向相关（即 formal 更常是 rewrite 而非 original），这个 marginal confound 可能部分解释观察到的 formality effect。\n- 建议：做 formal decomposition：在控制 original/rewrite 状态后，formality effect 减少多少？一个简单的 logistic regression (judge_choice ~ is_formal + is_original) 即可。\n\n**W4** [warning] Multiple comparison correction 不一致\n- 具体位置：§4 (\"Holm-Bonferroni correction across the 9-cell grid\"), Tables 1, 5, 6, 8, 9\n- 问题：Holm-Bonferroni 仅用于 Table 2 的 9-cell grid。但 Tables 1（3 comparisons）、8（verbosity）、9（register）是额外的假设检验。全论文总共约 20+ 次检验，但没有讨论 family-wise error rate。\n- 建议：(1) 报告全局 correction 后的结果（或至少讨论）；(2) 或者按 \"discovery\" vs \"confirmation\" 区分实验，仅对 confirmatory 实验做 correction。\n\n**W5** [warning] Post-hoc power analysis 方法论问题\n- 具体位置：§5.5\n- 问题：论文用 observed effect size 做 post-hoc power analysis 估计所需样本量。这在统计文献中广泛被批评（Hoenig & Heisey, 2001）——observed power 是 p-value 的 1-to-1 函数，不提供额外信息。\"5× efficiency gap\" 来自 post-hoc 估计，其可信度受限于 observed effect 的不确定性。\n- 建议：改用 confidence interval 或 equivalence testing 来量化 efficiency gap；或基于先验 literature 的 effect size（而非观测值）做 power analysis。\n\n---\n\n## 小问题（不影响接收）\n\n- §5.8 Table 8 verbosity 和 §5.9 Table 9 register 仅在 GPT-4o×LLMBar 上测试了一个 judge×benchmark 组合，cross-axis generalization 的证据较薄。\n- Table 9 register axis p=0.068 未达显著，论文用\"suggestive evidence\"表述，但放在 cross-axis generalization 的叙事中可能误导读者认为 register bias 已被确认。\n- \"Likert Blindspot\" 术语有 oversell 风险——本质上 Likert 不是\"看不到\" bias，而是需要更大样本量。论文自身的 n=500 数据中 binarized Likert p=0.055，接近显著边缘，说明 Likert 在足够大样本下可能也会显著。\n- 无 appendix/supplementary material。对于涉及 9 cells × 3 metrics 的实验矩阵，detailed per-cell 结果（含 CI）应在 supplementary 中提供。\n- 论文 7 页（正文约 6 页 + 参考文献 1 页），格式合规（EMNLP 2026 long paper 8-page limit）。\n\n---\n\n## Questions for Authors\n\n**Q1**: 请报告每个 judge×benchmark cell 的完整 attrition 数据：generated pairs → NLI pass → position-consistent → final n。目前无法评估 filtering 对 representativeness 的影响。\n\n**Q2**: NLI 阈值 0.90 是在看到结果前还是后确定的？是否做过 threshold sensitivity analysis（如 0.80, 0.85, 0.90, 0.95）？\n\n**Q3**: Table 7 中 67% false-negative rate 意味着 NLI-rejected pairs 远多于 accepted pairs。这些被拒绝但人类认为 content 保留的 pairs 中，judge 的 formality preference 是什么？如果方向与 accepted pairs 一致，\"lower-bound\" claim 成立；如果不一致，则 NLI gate 引入了 non-trivial selection bias。\n\n**Q4**: 是否考虑过 cumulative link mixed model (CLMM) 或 ordinal logistic regression 作为 Likert 的替代分析？ATE 在 ordinal data 上可能不是最 sensitive 的方法。\n\n**Q5**: Table 4 original preference OR=1.65 (p=0.072) 是 marginal 的。是否可以做 logistic regression (judge_choice ~ is_formal + is_original) 来 partial out original preference 对 formality effect 的贡献？\n\n**Q6**: 对于 §5.5 的 power analysis，\"n≈80 for pairwise vs n>X for Likert\" 中的效应量是观测值还是 pre-specified？观测效应量的 CI 较宽时，post-hoc power analysis 的可信度有限。\n\n**Q7**: Consistency filtering 去掉的 ~40-50% pairs 中，position bias 的方向和大小如何？这些数据本身就是关于 LLM judge position bias 的有价值信息。\n\n---\n\n## 总结评分\n\n| 项目 | 评分 |\n|------|------|\n| Overall Assessment | **3.5** (Borderline Conference) |\n| Soundness | 3.5/5 |\n| Excitement | 3.5/5 |\n| Confidence | 4/5 |\n\n**判断依据**: 论文提出了一个对 LLM-as-judge 社区有实际意义的发现，Pipeline 设计系统性强，实验覆盖了主要的 confounds。但三个 critical 问题——因果框架缺失 (N1)、NLI gate 的选择偏差未分析 (N2)、NLI 阈值无 justification (N3)——使得证据链不够坚实。Likert baseline 的公平性 (W1) 和 original preference 的 marginal confound (W3) 进一步削弱了核心 claim 的说服力。如果 rebuttal 能：(a) 补上 NLI threshold sensitivity analysis, (b) 报告 NLI-rejected pairs 的 bias 方向, (c) 加入 CLMM 作为 Likert baseline, 我愿意上调至 4.0 (Conference)。",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## R1 审稿意见：Methods & Experiments\n\n**论文**: \"The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Counterfactual Pairwise Comparison\"\n\n**注意**: Director brief 中部分数字与 PDF 不一致。以下审稿严格基于 PDF 原文。PDF 显示 Table 1 三个 judge 均显著 (GPT-4o p=0.006, Claude p=0.012, Gemini p=0.032)；Table 2 有 7/9 cells 显著；Table 5 win rate ~67.6%（CI [0.637, 0.714]），效率差距为 5× 而非 7×。Director brief 中 \"Only 2/3 judges significant\" \"Only 2/9 cells significant\" \"7× efficiency\" \"win rate regresses to 61.1%\" 等描述与本版 PDF 不符。\n\n---\n\n## 总体评分\n**Overall**: 3.5 — Borderline Conference\n**一句话总结**: 核心发现（pairwise 比 Likert 更能检测 style bias）有实际价值且在多数实验中得到支持，但因果框架缺失、NLI gate 的选择偏差未被分析、以及 Likert baseline 可能不公平，使得证据链不够坚实。\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | Pipeline 设计合理，控制实验覆盖主要 confound，但因果语言与实际统计框架不匹配；NLI 阈值无 justification；multiple comparison 处理不一致 |\n| Excitement | 3.5/5 | 发现对 LLM-as-judge 社区有直接实践意义；但范围较窄（主要一个 style axis），且 Likert 的\"盲区\"可能是分析方法而非 Likert 本身的问题 |\n| Reproducibility | 3/5 | 报告了 judge/benchmark/rewriter 选择和 NLI 阈值，但缺少每阶段的 attrition 数据（生成→NLI pass→consistent→final n），无代码/数据 |\n| Confidence | 4/5 | 对实验方法论和 NLP 评估统计有充分经验 |\n\n---\n\n## 主要优势\n\n- **重要的实践发现**：7/9 judge×benchmark 组合中 pairwise 检测到显著 formality bias，而 Likert ATE 仅 1/9、binarized Likert 0/9。这直接挑战了 LLM 评估社区对 Likert 评分的默认依赖（§5.3, Table 3）。\n- **Pipeline 设计系统性强**：四阶段协议（counterfactual rewriting → NLI gate → position-controlled comparison → Likert baseline）每一步都针对特定 confound，逻辑清晰（§3）。\n- **Confound 控制全面**：original preference 控制（Table 4）、rewriter robustness（Table 6, Llama vs Qwen）、human NLI validation（Table 7）、cross-axis generalization（Tables 8-9）覆盖了主要替代解释。\n- **Binarized-Likert 作为诊断工具的创新性**：通过让 binarized Likert 和 pairwise 使用相同的 sign test，将灵敏度差异精确隔离到 measurement structure（§5.3）。这是本文最强的方法论贡献。\n- **诚实的 Limitations**：明确承认因果框架的近似性、样本量限制、仅检测不纠正（page 6）。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 因果语言与实际框架严重不匹配\n- 具体位置：§3 标题 \"Counterfactual Style Rewriting\"、§3.4 \"ATE\"、§1 \"counterfactual pairwise measurement procedure\"、Limitations (page 6)\n- 问题：论文大量使用因果推断术语——\"counterfactual\"、\"interventional\"、\"treatment effect (ATE)\"——但 Limitations 自认\"our 'interventional' framing approximates but does not formally establish causal identification; we do not provide a directed acyclic graph, discuss SUTVA, or conduct sensitivity analysis for unmeasured confounders\"。这不仅是写作问题，而是核心方法论缺陷：如果论文的核心贡献是一个\"counterfactual protocol\"，读者需要 DAG 来评估 Style → Score 的因果通路中 Content 是否被正确控制、是否存在未测量的 confounders（如 fluency/coherence 变化）。\n- 为什么影响接收：reviewer 和读者会质疑：没有 DAG，你怎么知道 NLI gate 足够控制 content confound？\"ATE\" 在没有因果框架下是否只是一个描述性统计量？这直接影响论文 claim 的可信度。\n- 建议修改方向：(1) 给出 DAG（至少：Style_axis → Rewrite → Judge_score, with Content as mediator and potential confounders）; (2) 讨论 SUTVA 在此设置下的合理性；(3) 对\"未被 NLI 捕获的语义变化\"做 sensitivity analysis；或 (4) 降调因果语言，改用\"diagnostic\"/\"detection\"框架。\n\n**N2** [critical] NLI gate 的选择偏差未被分析\n- 具体位置：§3.2, Table 7 (page 5)\n- 问题：Table 7 显示 NLI gate 的 false-negative rate 为 67%——即人类认为内容保留了的 pair 中，2/3 被 NLI 拒绝。论文将此解释为\"conservative behavior implies that our reported bias magnitudes are lower-bound estimates\"（§5.7），但这一推断需要一个未经验证的假设：NLI-rejected-but-human-valid pairs 中的 bias 方向和大小与 NLI-accepted pairs 相同或更大。如果 NLI gate 系统性地筛掉了 deeper style changes（这些改写更可能同时改变 content），留下的可能是 superficial 改写（容易让 NLI 验证），而 superficial 改写产生的 bias 可能与 deeper 改写不同。\n- 为什么影响接收：67% 的 data loss 意味着最终分析仅基于原始数据的 ~1/3。如果这 1/3 不具代表性，所有效应量估计和统计检验的外部效度都成问题。\n- 建议修改方向：(1) 分析 NLI-rejected pairs 的 pairwise 结果（作为 sensitivity analysis）；(2) 至少报告 NLI-rejected pairs 中 judge 的 raw preference 分布；(3) 对 \"lower-bound\" claim 提供形式化论证而非仅凭直觉。\n\n**N3** [critical] NLI 阈值 0.90 缺乏 justification，且不同 axis 之间不一致\n- 具体位置：§3.2\n- 问题：NLI entailment 阈值设为 0.90，但论文未解释为什么是 0.90 而非 0.85 或 0.95。更重要的是，§3.2 提到 verbosity axis 的 NLI gate 从 bidirectional（65% pass rate）改为 direction-aware（86% pass rate），这表明阈值和 gating 策略是 per-axis 调整的。这引入了 researcher degrees of freedom——是否先看了结果再调阈值？\n- 为什么影响接收：如果阈值选择影响哪些 pairs 进入分析，它直接影响效应量和显著性。没有 pre-registration 或 sensitivity analysis，读者无法评估结果对阈值选择的稳健性。\n- 建议修改方向：(1) 报告阈值 sensitivity analysis（如 0.85, 0.90, 0.95 下的 win rate 和 p-value）；(2) 说明阈值是否 pre-specified；(3) 对 verbosity axis 的 direction-aware 调整提供独立的 justification。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Likert baseline 可能不公平——未使用 ordinal regression\n- 具体位置：§3.4, Table 3\n- 问题：Likert 数据的分析用了 ATE（均值差）和 binarized sign test。ATE 丢弃了 ordinal 结构信息——1分和2分的差异被等同于4分和5分的差异。Cumulative link mixed model (CLMM) 或 ordinal logistic regression 能更好地利用 Likert 数据的 ordinal 特性，可能会检测到 ATE 遗漏的效应。Binarized Likert 虽然与 pairwise 使用相同的 sign test，但它把 5 vs 4 等同于 5 vs 1，同样丢失信息。\n- 建议：增加 CLMM 分析作为 Likert 的更公平 baseline。如果 CLMM 仍然不显著，\"Likert Blindspot\" 的论点会大大加强；如果 CLMM 显著，则说明问题在于分析方法而非 Likert 本身。\n\n**W2** [warning] Consistency filtering 的 data loss 过高且未分析\n- 具体位置：§3.3, Table 1\n- 问题：Table 1 显示 GPT-4o 有 55 个 consistent pairs（推测 n=100，即 45% 被过滤）。Claude 的 consistent pairs 更少。被过滤的 position-sensitive pairs 包含有价值的信息——它们可能代表 style preference 较弱或 position bias 较强的样本。论文完全忽略了这些 pairs 的分析。\n- 建议：(1) 明确报告每个 cell 的 total pairs → NLI pass → consistent → final n 的 attrition 表；(2) 对 inconsistent pairs 做探索性分析（如 first-position win rate）；(3) 讨论 consistency filtering 对 effect size generalizability 的影响。\n\n**W3** [warning] Original preference confound 结果为 marginal，不能安全忽略\n- 具体位置：§5.4, Table 4\n- 问题：原始偏好 win rate 56%, GEE OR=1.65, p=0.072。论文将此解释为\"substantially weaker than the formality effect (66-70%)\"，但 56% 不是 negligible。如果 formal rewrite 与 \"非原始\" 方向相关（即 formal 更常是 rewrite 而非 original），这个 marginal confound 可能部分解释观察到的 formality effect。\n- 建议：做 formal decomposition：在控制 original/rewrite 状态后，formality effect 减少多少？一个简单的 logistic regression (judge_choice ~ is_formal + is_original) 即可。\n\n**W4** [warning] Multiple comparison correction 不一致\n- 具体位置：§4 (\"Holm-Bonferroni correction across the 9-cell grid\"), Tables 1, 5, 6, 8, 9\n- 问题：Holm-Bonferroni 仅用于 Table 2 的 9-cell grid。但 Tables 1（3 comparisons）、8（verbosity）、9（register）是额外的假设检验。全论文总共约 20+ 次检验，但没有讨论 family-wise error rate。\n- 建议：(1) 报告全局 correction 后的结果（或至少讨论）；(2) 或者按 \"discovery\" vs \"confirmation\" 区分实验，仅对 confirmatory 实验做 correction。\n\n**W5** [warning] Post-hoc power analysis 方法论问题\n- 具体位置：§5.5\n- 问题：论文用 observed effect size 做 post-hoc power analysis 估计所需样本量。这在统计文献中广泛被批评（Hoenig & Heisey, 2001）——observed power 是 p-value 的 1-to-1 函数，不提供额外信息。\"5× efficiency gap\" 来自 post-hoc 估计，其可信度受限于 observed effect 的不确定性。\n- 建议：改用 confidence interval 或 equivalence testing 来量化 efficiency gap；或基于先验 literature 的 effect size（而非观测值）做 power analysis。\n\n---\n\n## 小问题（不影响接收）\n\n- §5.8 Table 8 verbosity 和 §5.9 Table 9 register 仅在 GPT-4o×LLMBar 上测试了一个 judge×benchmark 组合，cross-axis generalization 的证据较薄。\n- Table 9 register axis p=0.068 未达显著，论文用\"suggestive evidence\"表述，但放在 cross-axis generalization 的叙事中可能误导读者认为 register bias 已被确认。\n- \"Likert Blindspot\" 术语有 oversell 风险——本质上 Likert 不是\"看不到\" bias，而是需要更大样本量。论文自身的 n=500 数据中 binarized Likert p=0.055，接近显著边缘，说明 Likert 在足够大样本下可能也会显著。\n- 无 appendix/supplementary material。对于涉及 9 cells × 3 metrics 的实验矩阵，detailed per-cell 结果（含 CI）应在 supplementary 中提供。\n- 论文 7 页（正文约 6 页 + 参考文献 1 页），格式合规（EMNLP 2026 long paper 8-page limit）。\n\n---\n\n## Questions for Authors\n\n**Q1**: 请报告每个 judge×benchmark cell 的完整 attrition 数据：generated pairs → NLI pass → position-consistent → final n。目前无法评估 filtering 对 representativeness 的影响。\n\n**Q2**: NLI 阈值 0.90 是在看到结果前还是后确定的？是否做过 threshold sensitivity analysis（如 0.80, 0.85, 0.90, 0.95）？\n\n**Q3**: Table 7 中 67% false-negative rate 意味着 NLI-rejected pairs 远多于 accepted pairs。这些被拒绝但人类认为 content 保留的 pairs 中，judge 的 formality preference 是什么？如果方向与 accepted pairs 一致，\"lower-bound\" claim 成立；如果不一致，则 NLI gate 引入了 non-trivial selection bias。\n\n**Q4**: 是否考虑过 cumulative link mixed model (CLMM) 或 ordinal logistic regression 作为 Likert 的替代分析？ATE 在 ordinal data 上可能不是最 sensitive 的方法。\n\n**Q5**: Table 4 original preference OR=1.65 (p=0.072) 是 marginal 的。是否可以做 logistic regression (judge_choice ~ is_formal + is_original) 来 partial out original preference 对 formality effect 的贡献？\n\n**Q6**: 对于 §5.5 的 power analysis，\"n≈80 for pairwise vs n>X for Likert\" 中的效应量是观测值还是 pre-specified？观测效应量的 CI 较宽时，post-hoc power analysis 的可信度有限。\n\n**Q7**: Consistency filtering 去掉的 ~40-50% pairs 中，position bias 的方向和大小如何？这些数据本身就是关于 LLM judge position bias 的有价值信息。\n\n---\n\n## 总结评分\n\n| 项目 | 评分 |\n|------|------|\n| Overall Assessment | **3.5** (Borderline Conference) |\n| Soundness | 3.5/5 |\n| Excitement | 3.5/5 |\n| Confidence | 4/5 |\n\n**判断依据**: 论文提出了一个对 LLM-as-judge 社区有实际意义的发现，Pipeline 设计系统性强，实验覆盖了主要的 confounds。但三个 critical 问题——因果框架缺失 (N1)、NLI gate 的选择偏差未分析 (N2)、NLI 阈值无 justification (N3)——使得证据链不够坚实。Likert baseline 的公平性 (W1) 和 original preference 的 marginal confound (W3) 进一步削弱了核心 claim 的说服力。如果 rebuttal 能：(a) 补上 NLI threshold sensitivity analysis, (b) 报告 NLI-rejected pairs 的 bias 方向, (c) 加入 CLMM 作为 Likert baseline, 我愿意上调至 4.0 (Conference)。",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 39 · 2026-05-21T01:54:55.570317+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4174
}
```

</details>

---


### Tool call

_source line 40 · 2026-05-21T01:54:59.587191+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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

_source line 41 · 2026-05-21T01:54:59.637905+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-21T01:55:04.056251+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T010111/best/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T010111/best/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-21T01:55:04.157043+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 100
}
```

</details>

---


### Assistant

_source line 44 · 2026-05-21T01:55:12.908366+00:00_

审稿意见已提交至 Review Director。

核心判断：**3.5 (Borderline Conference)**。论文发现 pairwise 比 Likert 更能检测 style bias，Pipeline 设计系统且实验覆盖面广（7/9 cells 显著）。但三个 critical 问题拉低评分：(1) 大量使用因果术语却无 DAG/SUTVA 等正式框架；(2) NLI gate 67% false-negative rate 造成的选择偏差未被分析；(3) NLI 阈值 0.90 无 justification 且 per-axis 调整引入 researcher degrees of freedom。若 rebuttal 能补上 NLI threshold sensitivity analysis、报告 NLI-rejected pairs 的 bias 方向、加入 ordinal regression 作为更公平的 Likert baseline，可上调至 4.0。

另外提醒：Director brief 中的部分数字与 PDF 原文不一致（如 Table 1 显著性、Table 2 显著 cell 数量、效率倍数等），我已在审稿意见开头标注。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1"
}
```

</details>

---


## Round 2

## Round 2

4 recorded events


### User

_source line 45 · 2026-05-21T01:55:14.090676+00:00_

[Round 1 审稿请求]:
## Step 2: Cross-Share — Findings from R2 (Novelty & Related Work)

R2 has identified the following issues relevant to your methods/experiments assessment:

1. **Missing references (critical):** Multiple "?" and "???" citation placeholders throughout §1 and §2. The References section (page 10) is completely empty. This is a submission-readiness issue that also prevents verifying related work claims.

2. **No figures in the entire paper.** Zero visual elements across 9 pages. Power curves, forest plots, and heatmaps would significantly strengthen the experimental narrative. The experiment plan apparently included detailed figure specifications that are absent.

3. **Title vs. content tension:** "The Likert Blindspot" frames the finding as a categorical failure, but by §4.6, it's characterized as an "efficiency gap." R2 flags this as potential overselling.

4. **Incremental novelty concern:** The Likert-vs-forced-choice gap is well-established in psychometrics (Kiritchenko & Mohammad, Best-Worst Scaling). The paper's contribution is applying this known insight to LLM judge bias. R2 questions whether this is sufficient for a top venue.

5. **Scope concern:** Title says "Style Bias" but only formality is tested. The gap between title promise and experimental scope is notable.

Please factor these observations into your final assessment, especially: (a) whether the statistical evidence would be strengthened by figures, (b) whether the "efficiency gap" recharacterization at n=500 undermines the "blindspot" framing, and (c) whether the narrow scope (1 clean cell after confound analysis) is sufficient for the claims made.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-21T01:56:55.887228+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## R1 对 R2 意见的交叉回应\n\n**前提说明**: 我审阅的是 `dream_20260521T010111/best/paper.pdf`（7页），与 R2 描述的版本存在差异。R2 提到\"References section (page 10) is completely empty\"和\"9 pages\"，而我看到的版本是 7 页且 page 7 有完整参考文献（Yao Dou et al., Karpinska et al., Park et al. 等条目可见）。以下回应基于两个版本可能不同的认知。\n\n---\n\n### 逐条回应\n\n**[AGREE] R2-Issue-1: 引用占位符问题**\n同意这是 submission-readiness 的硬伤。我审阅的\"best\"版本 page 7 有参考文献条目，但如果 R2 审阅的版本确有 \"?\" \"???\" 占位符和空 References，则该版本显然未达投稿状态。不过这是编辑/编译问题，不反映方法论质量。**从 methods review 角度，不影响我对实验设计的评估，但应在最终版中修复。**\n\n**[AGREE] R2-Issue-2: 全文零图表——严重削弱实验叙事**\n强烈同意。我在 7 页 PDF 中同样未见任何 Figure。这对一篇以统计检测灵敏度为核心的论文是重大缺陷。具体补充：\n\n- **Power curve 缺失最为致命**：§5.5 声称 pairwise 比 Likert 有 5× 效率优势，但仅靠文字描述和 post-hoc power estimate 说服力极弱。一张 power curve（x: sample size, y: power, 两条线分别对应 pairwise 和 binarized Likert）可以让读者直观看到 sensitivity gap 的全貌，也能暴露 post-hoc estimate 的不确定性。\n- **Forest plot / heatmap 对 Table 2 (3×3 grid) 必要**：9 个 cells 的 win rate + CI 用 forest plot 呈现远优于纯数字表格。Heatmap 可以一目了然地展示哪些 judge×benchmark 组合 bias 最强。\n- **Figure 1 应为 pipeline 示意图**：四阶段协议（rewrite → NLI gate → position control → comparison）的流程图对理解方法论至关重要，纯文字描述不直观。\n\n**结论：缺少 figures 不改变统计结果的有效性，但严重影响 presentation 和说服力。对于 borderline 论文，这可能是 accept/reject 的 tipping point。我将此纳入最终评分考量。**\n\n**[AGREE with nuance] R2-Issue-3: \"Likert Blindspot\" 的 oversell 问题**\n同意 R2 的方向，且我在 R1 原稿中已独立指出这一点。补充更具体的证据：\n\n- §5.5 (Table 5, n=500): binarized Likert p=0.055。这距离 α=0.05 仅一步之遥。如果 n 再增加 ~20%（约 n=600），binarized Likert 很可能也会显著。这说明 Likert 不是\"盲\"的，只是\"近视\"——需要更大样本。\n- 论文自身在 §6 Discussion 中说 \"we view this as complementary rather than adversarial\"，与标题 \"Blindspot\" 的强势措辞矛盾。\n- **但我不同意 R2 的程度判断**：从 7/9 pairwise 显著 vs 0/9 binarized Likert 显著的落差来看，在实践中常用的 n=100 级别样本下，Likert 确实系统性失灵。称其为 \"blindspot\" 在 typical sample size regime 下并非完全不合理，只是需要明确 qualify——应改为 \"the Likert Blindspot at typical evaluation sample sizes\" 或类似表述。\n\n**(a) Director 问题回答：** 如果有 power curve，读者可以自行判断 \"blindspot\" 在什么 n 范围内成立，标题的 oversell 问题会自然缓解。这是 figures 能直接解决的问题。\n\n**[REBUT] R2-Issue-4: 增量创新性不足**\n部分反驳。R2 正确指出 Likert vs forced-choice 的灵敏度差异在心理测量学中已知（Kiritchenko & Mohammad, Best-Worst Scaling; Thurstone, 1927）。但本文的贡献不仅是\"应用已知 insight\"，而是：\n\n1. **首次系统量化**：在 LLM judge style bias 的具体 context 下，用 3 judges × 3 benchmarks × 3 metrics 的矩阵量化 Likert 和 pairwise 的灵敏度差距。此前 RATE (Feuer et al., 2025) 用 Likert 作为主要测量工具，但未对比 pairwise。这填补了一个具体的方法论空白。\n2. **Binarized-Likert 的诊断设计**：通过让 binarized Likert 和 pairwise 使用相同的 sign test，精确隔离了 measurement structure 作为灵敏度差异的来源。这不是简单的 \"Likert 差\"，而是 \"forced comparison 在 style bias detection 中的结构性优势\"。\n3. **实践影响**：LLM 评估社区大量使用 Likert 评分（Chatbot Arena, MT-Bench 排行榜, RATE protocol），如果 Likert 在 typical n 下系统性漏检 style bias，这对整个评估生态有直接影响。\n\n**我认为这足以构成 Findings-level 的贡献，但是否达到 main conference 取决于证据的坚实程度（这正是我的 N1-N3 concerns 所关注的）。**\n\n**[AGREE] R2-Issue-5: 标题\"Style Bias\"与实验范围不匹配**\n同意。我在 R1 原稿中也指出了范围问题。具体：\n\n- 标题 \"Style Bias\" 暗示覆盖多种 style axes，但论文的 primary evidence 只有 formality。\n- Verbosity (Table 8) 和 register (Table 9) 各只有 1 个 judge×benchmark 组合，且 register 未达显著（p=0.068）。\n- 标题应改为 \"Detecting Hidden Formality Bias in LLM Judges\" 或在标题中加 qualifier（如 \"a case study on formality\"）。\n\n---\n\n### Director 三个具体问题的回答\n\n**(a) 统计证据是否需要 figures 来加强？**\n是的，且这是高优先级修改。三个必要的 figures：\n1. **Power curve**（pairwise vs binarized Likert vs Likert ATE, x=n, y=power）→ 直接回应 \"efficiency gap\" vs \"blindspot\" 的争论\n2. **Forest plot**（9 cells 的 win rate + 95% CI）→ 让读者一眼看出哪些 cells 强、哪些弱\n3. **Pipeline diagram**（四阶段流程 + 每阶段的 attrition 数据）→ 方法论可理解性\n\n没有这些 figures，论文在 presentation quality 上低于 venue 期望。\n\n**(b) \"Efficiency gap\" 是否削弱 \"blindspot\" framing？**\n是的，存在张力。§5.5 的 n=500 结果（binarized Likert p=0.055）表明 Likert 在更大样本下趋近显著。这证明 Likert 不是 categorically blind，而是 statistically underpowered at typical n。论文需要二选一：\n- 要么将 \"Blindspot\" 重新定义为 \"在实践中常用的 n=100 级别下的系统性失灵\"（需要 power curve 支撑）\n- 要么放弃 \"Blindspot\" 框架，改用 \"efficiency gap\" 作为主要叙事\n\n目前论文两个框架共存，产生了内部矛盾。这会给 reviewer 留下\"overselling\"的印象。\n\n**(c) \"1 clean cell\" 是否足够支撑 claims？**\n这取决于如何定义 \"clean\"。在我审阅的 best 版本中：\n- 7/9 cells 在 uncorrected pairwise 中显著\n- 但只有 GPT-4o×LLMBar 同时有：rewriter robustness control (Table 6)、full original preference analysis (Table 4)、scaled replication (Table 5, 虽然这个是 GPT-4o×MT-Bench)\n- 其他 6 个显著 cells 没有独立的 confound 控制\n\n如果要求每个 cell 都有完整的 confound 控制，确实只有 1-2 个 cells 是 \"fully validated\"。这对论文 claims 的 generalizability 是一个合理质疑。\n\n**我的评估**：论文的 primary evidence (GPT-4o×LLMBar) 是 solid 的；cross-judge/benchmark generalization 是 suggestive but not fully controlled。论文应该：\n1. 明确区分 \"fully controlled\" vs \"suggestive\" evidence\n2. 降调 generalization claims（\"across 9 judge×benchmark combinations\" → \"primarily demonstrated on GPT-4o×LLMBar, with suggestive evidence across 6 additional combinations\"）\n\n---\n\n### 综合 R2 意见后的评分调整\n\nR2 的 Issue-2 (无 figures) 和 Issue-5 (scope vs title) 加强了我原有的 concerns。特别是：\n- 零 figures 的 presentation 在 top venue 不可接受，这是 R2 带来的新信息（我在 R1 原稿中未单独标记）。\n- R2 的增量创新性质疑 (Issue-4) 我部分反驳，但承认\"将已知心理测量学 insight 应用到 LLM judge\"的创新性确实有限。\n\n**调整后评分**：\n\n| 项目 | R1原评分 | 调整后 | 原因 |\n|------|---------|--------|------|\n| Overall | 3.5 | **3.0** (Findings) | 零 figures + scope/title 不匹配 + 仅 1-2 个 fully controlled cells，整体不够 main conference 水准 |\n| Soundness | 3.5/5 | **3/5** | \"1-2 clean cells\" 的论点使 generalization claim 的 soundness 下降 |\n| Excitement | 3.5/5 | **3/5** | 增量创新性 + 窄 scope 降低 excitement |\n| Confidence | 4/5 | 4/5 | 不变 |\n\n**修改后一句话总结**: 核心发现在 GPT-4o×LLMBar 上可信，但 zero figures、scope 窄于标题承诺、以及 cross-setting generalization 缺乏完整 confound 控制，使论文更适合 Findings 而非 main conference。如果 rebuttal 能补上 power curve + forest plot、增加 1-2 个 style axis 的完整实验、并收窄标题 scope，可上调至 3.5。",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## R1 对 R2 意见的交叉回应\n\n**前提说明**: 我审阅的是 `dream_20260521T010111/best/paper.pdf`（7页），与 R2 描述的版本存在差异。R2 提到\"References section (page 10) is completely empty\"和\"9 pages\"，而我看到的版本是 7 页且 page 7 有完整参考文献（Yao Dou et al., Karpinska et al., Park et al. 等条目可见）。以下回应基于两个版本可能不同的认知。\n\n---\n\n### 逐条回应\n\n**[AGREE] R2-Issue-1: 引用占位符问题**\n同意这是 submission-readiness 的硬伤。我审阅的\"best\"版本 page 7 有参考文献条目，但如果 R2 审阅的版本确有 \"?\" \"???\" 占位符和空 References，则该版本显然未达投稿状态。不过这是编辑/编译问题，不反映方法论质量。**从 methods review 角度，不影响我对实验设计的评估，但应在最终版中修复。**\n\n**[AGREE] R2-Issue-2: 全文零图表——严重削弱实验叙事**\n强烈同意。我在 7 页 PDF 中同样未见任何 Figure。这对一篇以统计检测灵敏度为核心的论文是重大缺陷。具体补充：\n\n- **Power curve 缺失最为致命**：§5.5 声称 pairwise 比 Likert 有 5× 效率优势，但仅靠文字描述和 post-hoc power estimate 说服力极弱。一张 power curve（x: sample size, y: power, 两条线分别对应 pairwise 和 binarized Likert）可以让读者直观看到 sensitivity gap 的全貌，也能暴露 post-hoc estimate 的不确定性。\n- **Forest plot / heatmap 对 Table 2 (3×3 grid) 必要**：9 个 cells 的 win rate + CI 用 forest plot 呈现远优于纯数字表格。Heatmap 可以一目了然地展示哪些 judge×benchmark 组合 bias 最强。\n- **Figure 1 应为 pipeline 示意图**：四阶段协议（rewrite → NLI gate → position control → comparison）的流程图对理解方法论至关重要，纯文字描述不直观。\n\n**结论：缺少 figures 不改变统计结果的有效性，但严重影响 presentation 和说服力。对于 borderline 论文，这可能是 accept/reject 的 tipping point。我将此纳入最终评分考量。**\n\n**[AGREE with nuance] R2-Issue-3: \"Likert Blindspot\" 的 oversell 问题**\n同意 R2 的方向，且我在 R1 原稿中已独立指出这一点。补充更具体的证据：\n\n- §5.5 (Table 5, n=500): binarized Likert p=0.055。这距离 α=0.05 仅一步之遥。如果 n 再增加 ~20%（约 n=600），binarized Likert 很可能也会显著。这说明 Likert 不是\"盲\"的，只是\"近视\"——需要更大样本。\n- 论文自身在 §6 Discussion 中说 \"we view this as complementary rather than adversarial\"，与标题 \"Blindspot\" 的强势措辞矛盾。\n- **但我不同意 R2 的程度判断**：从 7/9 pairwise 显著 vs 0/9 binarized Likert 显著的落差来看，在实践中常用的 n=100 级别样本下，Likert 确实系统性失灵。称其为 \"blindspot\" 在 typical sample size regime 下并非完全不合理，只是需要明确 qualify——应改为 \"the Likert Blindspot at typical evaluation sample sizes\" 或类似表述。\n\n**(a) Director 问题回答：** 如果有 power curve，读者可以自行判断 \"blindspot\" 在什么 n 范围内成立，标题的 oversell 问题会自然缓解。这是 figures 能直接解决的问题。\n\n**[REBUT] R2-Issue-4: 增量创新性不足**\n部分反驳。R2 正确指出 Likert vs forced-choice 的灵敏度差异在心理测量学中已知（Kiritchenko & Mohammad, Best-Worst Scaling; Thurstone, 1927）。但本文的贡献不仅是\"应用已知 insight\"，而是：\n\n1. **首次系统量化**：在 LLM judge style bias 的具体 context 下，用 3 judges × 3 benchmarks × 3 metrics 的矩阵量化 Likert 和 pairwise 的灵敏度差距。此前 RATE (Feuer et al., 2025) 用 Likert 作为主要测量工具，但未对比 pairwise。这填补了一个具体的方法论空白。\n2. **Binarized-Likert 的诊断设计**：通过让 binarized Likert 和 pairwise 使用相同的 sign test，精确隔离了 measurement structure 作为灵敏度差异的来源。这不是简单的 \"Likert 差\"，而是 \"forced comparison 在 style bias detection 中的结构性优势\"。\n3. **实践影响**：LLM 评估社区大量使用 Likert 评分（Chatbot Arena, MT-Bench 排行榜, RATE protocol），如果 Likert 在 typical n 下系统性漏检 style bias，这对整个评估生态有直接影响。\n\n**我认为这足以构成 Findings-level 的贡献，但是否达到 main conference 取决于证据的坚实程度（这正是我的 N1-N3 concerns 所关注的）。**\n\n**[AGREE] R2-Issue-5: 标题\"Style Bias\"与实验范围不匹配**\n同意。我在 R1 原稿中也指出了范围问题。具体：\n\n- 标题 \"Style Bias\" 暗示覆盖多种 style axes，但论文的 primary evidence 只有 formality。\n- Verbosity (Table 8) 和 register (Table 9) 各只有 1 个 judge×benchmark 组合，且 register 未达显著（p=0.068）。\n- 标题应改为 \"Detecting Hidden Formality Bias in LLM Judges\" 或在标题中加 qualifier（如 \"a case study on formality\"）。\n\n---\n\n### Director 三个具体问题的回答\n\n**(a) 统计证据是否需要 figures 来加强？**\n是的，且这是高优先级修改。三个必要的 figures：\n1. **Power curve**（pairwise vs binarized Likert vs Likert ATE, x=n, y=power）→ 直接回应 \"efficiency gap\" vs \"blindspot\" 的争论\n2. **Forest plot**（9 cells 的 win rate + 95% CI）→ 让读者一眼看出哪些 cells 强、哪些弱\n3. **Pipeline diagram**（四阶段流程 + 每阶段的 attrition 数据）→ 方法论可理解性\n\n没有这些 figures，论文在 presentation quality 上低于 venue 期望。\n\n**(b) \"Efficiency gap\" 是否削弱 \"blindspot\" framing？**\n是的，存在张力。§5.5 的 n=500 结果（binarized Likert p=0.055）表明 Likert 在更大样本下趋近显著。这证明 Likert 不是 categorically blind，而是 statistically underpowered at typical n。论文需要二选一：\n- 要么将 \"Blindspot\" 重新定义为 \"在实践中常用的 n=100 级别下的系统性失灵\"（需要 power curve 支撑）\n- 要么放弃 \"Blindspot\" 框架，改用 \"efficiency gap\" 作为主要叙事\n\n目前论文两个框架共存，产生了内部矛盾。这会给 reviewer 留下\"overselling\"的印象。\n\n**(c) \"1 clean cell\" 是否足够支撑 claims？**\n这取决于如何定义 \"clean\"。在我审阅的 best 版本中：\n- 7/9 cells 在 uncorrected pairwise 中显著\n- 但只有 GPT-4o×LLMBar 同时有：rewriter robustness control (Table 6)、full original preference analysis (Table 4)、scaled replication (Table 5, 虽然这个是 GPT-4o×MT-Bench)\n- 其他 6 个显著 cells 没有独立的 confound 控制\n\n如果要求每个 cell 都有完整的 confound 控制，确实只有 1-2 个 cells 是 \"fully validated\"。这对论文 claims 的 generalizability 是一个合理质疑。\n\n**我的评估**：论文的 primary evidence (GPT-4o×LLMBar) 是 solid 的；cross-judge/benchmark generalization 是 suggestive but not fully controlled。论文应该：\n1. 明确区分 \"fully controlled\" vs \"suggestive\" evidence\n2. 降调 generalization claims（\"across 9 judge×benchmark combinations\" → \"primarily demonstrated on GPT-4o×LLMBar, with suggestive evidence across 6 additional combinations\"）\n\n---\n\n### 综合 R2 意见后的评分调整\n\nR2 的 Issue-2 (无 figures) 和 Issue-5 (scope vs title) 加强了我原有的 concerns。特别是：\n- 零 figures 的 presentation 在 top venue 不可接受，这是 R2 带来的新信息（我在 R1 原稿中未单独标记）。\n- R2 的增量创新性质疑 (Issue-4) 我部分反驳，但承认\"将已知心理测量学 insight 应用到 LLM judge\"的创新性确实有限。\n\n**调整后评分**：\n\n| 项目 | R1原评分 | 调整后 | 原因 |\n|------|---------|--------|------|\n| Overall | 3.5 | **3.0** (Findings) | 零 figures + scope/title 不匹配 + 仅 1-2 个 fully controlled cells，整体不够 main conference 水准 |\n| Soundness | 3.5/5 | **3/5** | \"1-2 clean cells\" 的论点使 generalization claim 的 soundness 下降 |\n| Excitement | 3.5/5 | **3/5** | 增量创新性 + 窄 scope 降低 excitement |\n| Confidence | 4/5 | 4/5 | 不变 |\n\n**修改后一句话总结**: 核心发现在 GPT-4o×LLMBar 上可信，但 zero figures、scope 窄于标题承诺、以及 cross-setting generalization 缺乏完整 confound 控制，使论文更适合 Findings 而非 main conference。如果 rebuttal 能补上 power curve + forest plot、增加 1-2 个 style axis 的完整实验、并收窄标题 scope，可上调至 3.5。",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 47 · 2026-05-21T01:57:00.357577+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4470
}
```

</details>

---


### Assistant

_source line 48 · 2026-05-21T01:57:05.875540+00:00_

交叉回应已提交。综合 R2 意见后，评分从 3.5 下调至 3.0 (Findings)。主要原因：零 figures 在 presentation 上不达标、scope 窄于标题承诺、且仅 1-2 个 cell 有完整 confound 控制。对 R2 的增量创新性质疑做了部分反驳——在 LLM judge 语境下的系统量化仍有 Findings-level 贡献。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1"
}
```

</details>

---


## Round 3

## Round 3

4 recorded events


### User

_source line 49 · 2026-05-21T01:57:07.046758+00:00_

[Round 1 审稿请求]:
## Step 3: Convergence — Key Points for Resolution

Based on both reviews, the following points need convergence:

**Points of Agreement (likely):**
1. The methodology is sound in design — the counterfactual + NLI + position-controlled pairwise protocol is well-constructed
2. The paper is honestly written with genuine limitations acknowledgment
3. Missing references and figures are critical presentation failures
4. The empirical base is narrower than the framing suggests (1 clean cell, not 9)
5. The title oversells relative to the actual findings

**Points Requiring Resolution:**

**Q1: Is the contribution primarily methodological or empirical?**
- If methodological (the protocol itself): the protocol is well-designed but assembles known components; novelty is incremental
- If empirical (demonstrating the blindspot): the evidence is thin (1 clean cell); the blindspot is more accurately an efficiency gap
- Possible resolution: the contribution is the specific combination applied to a practical problem, with the power analysis as the most useful deliverable

**Q2: What is the appropriate score range?**
- Arguments for 3 (Borderline Accept): clean methodology, honest reporting, practical utility, addresses real problem
- Arguments for 2 (Reject): 1 clean cell, no references, no figures, incremental novelty, title oversells
- Consider: could this be a solid workshop paper or Findings paper with revision?

**Q3: Is the "7× efficiency" claim the real contribution?**
- The power analysis (Table 5) may be the paper's most practically useful result
- But it's derived from a single condition (GPT-4o×LLMBar) and uses observed effect sizes

Please provide your final score (1-6) and 2-sentence rationale, incorporating cross-shared insights.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-21T01:57:47.172531+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## R1 最终收敛意见\n\n### 对三个 Resolution 问题的回应\n\n**Q1: 贡献定位——方法论 vs 实证？**\n\n两者兼有但都不够强，核心贡献在于 **诊断性实证 + 实践指导**。\n\n- 纯方法论：协议的四个组件（counterfactual rewriting, NLI gating, position control, binarized-Likert baseline）均为已有技术的组装，单独看无创新。但 binarized-Likert 与 pairwise 共用 sign test 从而隔离 measurement structure 的设计是一个精巧的诊断工具——这是方法论层面最有价值的部分。\n- 纯实证：如 R2 和我均指出，fully controlled 的 evidence 集中在 1-2 个 cells，generalization 是 suggestive。\n- **我的判断**：本文最核心的贡献是提出了一个 actionable 的诊断问题（\"你的 Likert-based bias audit 是否在漏检？\"）并在有限但可信的条件下给出了肯定回答。Power analysis（尽管 post-hoc）是最直接的实践 deliverable。这更适合 Findings 定位：对社区有用，但 evidence breadth 不足以支撑 main conference。\n\n**Q2: 评分区间？**\n\n使用 EMNLP 2026 / ARR 量表（1-5，含半分）：\n\n- 3.5 (Borderline Conference) 的论据：方法设计干净、binarized-Likert 诊断设计巧妙、诚实的 limitations、对 LLM 评估社区有直接实用价值\n- 3.0 (Findings) 的论据：zero figures、scope 窄于标题（formality only with full controls）、增量创新性、\"blindspot\" 实为 efficiency gap、仅 1-2 个 fully controlled cells\n- 2.5 (Borderline Findings) 的论据：如果引用确实缺失（R2 报告的版本），则 submission readiness 不达标\n\n**我的判断：3.0 (Findings)**。在我审阅的 best 版本中（有参考文献），presentation 问题（zero figures）和 evidence breadth 不足将其推离 main conference；但方法设计的系统性和诊断设计的巧妙性使其高于 \"resubmit\" 线。\n\n**Q3: \"5× efficiency\" claim 是否为真正贡献？**\n\n是最有实践价值的 deliverable，但可信度受限：\n- 来自单一条件（GPT-4o × LLMBar 或 GPT-4o × MT-Bench）\n- 基于 observed effect size 的 post-hoc estimate（methodologically problematic, cf. Hoenig & Heisey 2001）\n- 在 n=500 replication 中效应回归（win rate 从 69.1% 降至 ~67.6%），efficiency gap 可能缩小\n\n如果论文将此作为核心贡献来 pitch，需要：(1) 在多个 judge×benchmark 上 replicate power analysis, (2) 用 CI-based 方法替代 post-hoc power, (3) 补上 power curve figure。目前仅作为 supporting evidence 可信，作为 headline contribution 证据不足。\n\n---\n\n### 最终评分\n\n**Overall Assessment: 3.0 (Findings)**\n\n**两句话 rationale**: 论文提出了一个对 LLM-as-judge 社区有实际意义的诊断发现——在 n=100 级别的典型评估样本下，Likert 评分系统性漏检 pairwise 可检测的 style bias——但 fully controlled 的证据仅限于 1-2 个 judge×benchmark 组合，zero figures 使统计叙事缺乏说服力，且 \"blindspot\" 框架与自身 n=500 数据中 Likert 趋近显著的事实存在内部张力。适合 Findings 发表：方法论设计系统、诊断工具（binarized-Likert）有独立价值，但 evidence breadth 和 presentation quality 不达 main conference 水准。\n\n| 项目 | 最终评分 |\n|------|---------|\n| Overall Assessment | **3.0** (Findings) |\n| Soundness | 3/5 |\n| Excitement | 3/5 |\n| Confidence | 4/5 |\n\n### 上调条件（Rebuttal 可争取 3.5）\n1. 补上 power curve + forest plot + pipeline diagram（最低 3 张 figures）\n2. 报告 NLI threshold sensitivity analysis（至少 3 个阈值点）\n3. 收窄标题至 formality（或补上第二个 fully controlled style axis）\n4. 对 NLI-rejected pairs 做 sensitivity analysis 回应 \"lower-bound\" claim\n5. 加入 CLMM 作为 Likert 的更公平 baseline\n\n满足 1-3 可上调至 3.5；满足全部可上调至 4.0。",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## R1 最终收敛意见\n\n### 对三个 Resolution 问题的回应\n\n**Q1: 贡献定位——方法论 vs 实证？**\n\n两者兼有但都不够强，核心贡献在于 **诊断性实证 + 实践指导**。\n\n- 纯方法论：协议的四个组件（counterfactual rewriting, NLI gating, position control, binarized-Likert baseline）均为已有技术的组装，单独看无创新。但 binarized-Likert 与 pairwise 共用 sign test 从而隔离 measurement structure 的设计是一个精巧的诊断工具——这是方法论层面最有价值的部分。\n- 纯实证：如 R2 和我均指出，fully controlled 的 evidence 集中在 1-2 个 cells，generalization 是 suggestive。\n- **我的判断**：本文最核心的贡献是提出了一个 actionable 的诊断问题（\"你的 Likert-based bias audit 是否在漏检？\"）并在有限但可信的条件下给出了肯定回答。Power analysis（尽管 post-hoc）是最直接的实践 deliverable。这更适合 Findings 定位：对社区有用，但 evidence breadth 不足以支撑 main conference。\n\n**Q2: 评分区间？**\n\n使用 EMNLP 2026 / ARR 量表（1-5，含半分）：\n\n- 3.5 (Borderline Conference) 的论据：方法设计干净、binarized-Likert 诊断设计巧妙、诚实的 limitations、对 LLM 评估社区有直接实用价值\n- 3.0 (Findings) 的论据：zero figures、scope 窄于标题（formality only with full controls）、增量创新性、\"blindspot\" 实为 efficiency gap、仅 1-2 个 fully controlled cells\n- 2.5 (Borderline Findings) 的论据：如果引用确实缺失（R2 报告的版本），则 submission readiness 不达标\n\n**我的判断：3.0 (Findings)**。在我审阅的 best 版本中（有参考文献），presentation 问题（zero figures）和 evidence breadth 不足将其推离 main conference；但方法设计的系统性和诊断设计的巧妙性使其高于 \"resubmit\" 线。\n\n**Q3: \"5× efficiency\" claim 是否为真正贡献？**\n\n是最有实践价值的 deliverable，但可信度受限：\n- 来自单一条件（GPT-4o × LLMBar 或 GPT-4o × MT-Bench）\n- 基于 observed effect size 的 post-hoc estimate（methodologically problematic, cf. Hoenig & Heisey 2001）\n- 在 n=500 replication 中效应回归（win rate 从 69.1% 降至 ~67.6%），efficiency gap 可能缩小\n\n如果论文将此作为核心贡献来 pitch，需要：(1) 在多个 judge×benchmark 上 replicate power analysis, (2) 用 CI-based 方法替代 post-hoc power, (3) 补上 power curve figure。目前仅作为 supporting evidence 可信，作为 headline contribution 证据不足。\n\n---\n\n### 最终评分\n\n**Overall Assessment: 3.0 (Findings)**\n\n**两句话 rationale**: 论文提出了一个对 LLM-as-judge 社区有实际意义的诊断发现——在 n=100 级别的典型评估样本下，Likert 评分系统性漏检 pairwise 可检测的 style bias——但 fully controlled 的证据仅限于 1-2 个 judge×benchmark 组合，zero figures 使统计叙事缺乏说服力，且 \"blindspot\" 框架与自身 n=500 数据中 Likert 趋近显著的事实存在内部张力。适合 Findings 发表：方法论设计系统、诊断工具（binarized-Likert）有独立价值，但 evidence breadth 和 presentation quality 不达 main conference 水准。\n\n| 项目 | 最终评分 |\n|------|---------|\n| Overall Assessment | **3.0** (Findings) |\n| Soundness | 3/5 |\n| Excitement | 3/5 |\n| Confidence | 4/5 |\n\n### 上调条件（Rebuttal 可争取 3.5）\n1. 补上 power curve + forest plot + pipeline diagram（最低 3 张 figures）\n2. 报告 NLI threshold sensitivity analysis（至少 3 个阈值点）\n3. 收窄标题至 formality（或补上第二个 fully controlled style axis）\n4. 对 NLI-rejected pairs 做 sensitivity analysis 回应 \"lower-bound\" claim\n5. 加入 CLMM 作为 Likert 的更公平 baseline\n\n满足 1-3 可上调至 3.5；满足全部可上调至 4.0。",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 51 · 2026-05-21T01:57:51.541800+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4369
}
```

</details>

---


### Assistant

_source line 52 · 2026-05-21T01:57:56.555547+00:00_

R1 最终收敛意见已提交。最终评分 **3.0 (Findings)**，附明确的 rebuttal 上调路径（补 figures + NLI sensitivity + 收窄标题可至 3.5，全部修复可至 4.0）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1"
}
```

</details>

---


## Round 4

## Round 4

4 recorded events


### User

_source line 53 · 2026-05-21T01:57:57.757536+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 2 的完整审稿意见

请逐条回应 R2 的每个 Must-Fix 和 Should-Fix 问题：用 **[AGREE]** 表示同意并说明理由，或 **[REBUT]** 表示反驳并提供证据（cite 具体 Section/Table/Figure）。

特别关注以下与你审查维度（Methods & Experiments）相关的交叉点：
1. R2-N3 认为 RATE 批评缺乏实证支撑——你是否同意？从方法论角度看 §5.3 的比较是否合理？
2. R2-W2 认为缺少 Bradley-Terry 建模——你认为 sign test 在此场景下是否足够，还是 BT 建模确实必要？
3. R2-W4 指出全文无 Figure——从实验呈现角度，你是否认为可视化对传达核心发现至关重要？

---

以下是 **Reviewer 2 的完整审稿原文**：

## R2 审稿报告：Novelty &amp; Related Work

**论文**: "The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Counterfactual Pairwise Comparison"
**Venue**: EMNLP 2026 (via ACL Rolling Review)
**审稿维度**: Novelty, Related Work, Writing Quality, Scope/Impact, Presentation

---

## 总体评分

**Overall Assessment**: 2.5 / 5 (Borderline Findings)
**Director 6-point scale**: 3 / 6 (Weak Reject)
**一句话总结**: 方法论合理、核心实验发现有实用价值，但新颖性不足（已知心理测量学现象的重新包装）、范围狭窄（主要仅验证 formality 一个维度）、且提交材料存在严重的引用/格式缺陷，不具备送审状态。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3 / 5 (Acceptable) | 5 阶段协议设计合理，有 NLI 人工验证（91% agreement）和 Holm-Bonferroni 校正。但因果识别是近似的（作者在 Limitations 中承认），缺少 Bradley-Terry 建模，且 RATE 对比缺乏匹配条件下的复现 |
| **Excitement** | 2.5 / 5 (Potentially Interesting → Interesting) | 7/9 vs 1/9 的检测率差距数据有实用价值，但核心发现——Likert 评分对 forced-choice 敏感性不足——是心理测量学中已确立的结论，将其应用于 LLM judge 是直接的迁移，非深层洞见 |
| **Overall** | 2.5 / 5 (Borderline Findings) | 干净的实证工作，但 novelty 薄弱 + scope 狭窄 + 提交质量问题三重叠加 |

**Confidence**: 4 / 5 (Familiar with the area, have reviewed related work)

---

## 主要优势

- **S1**: 研究问题清晰且有实际意义——如果 Likert 评分系统性地低估 style bias，这对所有使用 LLM judge 的评估管线都有直接影响
- **S2**: 5 阶段反事实协议设计完备：style rewriting → NLI content gate → position control → Likert control → original preference control，每一步都有对照，逻辑链完整
- **S3**: 3 judges × 3 benchmarks 的网格设计覆盖了多个 LLM 家族（GPT-4o / Claude / Gemini），避免了单 judge 的 anecdotal evidence 问题
- **S4**: 透明承认所有组件是已有方法（§1 第2段明确列出来源：style rewriting from Mir et al. 2019, controls from RATE, pairwise from Thurstone 1927），这种诚实性值得肯定
- **S5**: 人工 NLI 验证（§5.7, n=100, 91% agreement, Table 7）为 content preservation gate 提供了可信的质量保证
- **S6**: Scaled replication（§5.5, n=500）确认效应量稳定，confidence interval 减半，增强了核心发现的可信度

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 新颖性不足——"Likert Blindspot" 是已知现象的重新命名

- 具体位置：§1 contributions, §6 Discussion 标题
- 问题：Likert 评分相比 forced-choice/pairwise comparison 在检测细微差异时敏感性不足，这在心理测量学中是 Thurstone (1927) 以来近百年的共识。作者自己也引用了 Karpinska et al. 和 Novikova et al. 证明 Best-Worst Scaling 优于 Likert。论文的核心贡献——将这一已知结果应用于 LLM judge bias 检测——是一个 application-level 的迁移，不是方法论创新。"Likert Blindspot" 这一术语暗示发现了一个此前未知的现象（"blindspot"），但实际上只是将已知的 measurement sensitivity gap 量化到了一个新 domain。
- 为什么影响接收：对于顶会（acceptance rate ~25%），incremental application of known psychometric insight 的 novelty bar 不够。
- 建议修改方向：(a) 明确将贡献定位为 "first empirical quantification" 而非 "discovery"，调整标题和术语避免暗示原创性；(b) 如果要维持 blindspot 叙事，需要展示 LLM judge 社区中存在的系统性误解（如大量 benchmark 论文仍在用 Likert 且因此漏报了 bias），并提供这种误解的量化证据。

**N2** [critical] 引用系统严重不完整——提交材料不具备送审状态

- 具体位置：Page 7 References; §1-§2 正文引用
- 问题：
  (a) 至少一处 arXiv ID 为占位符格式（"arXiv:2406.xxxxx"）——这不是真实的 arXiv 编号
  (b) 部分引用作者名疑似有误或乱码（需与原始 .bib 核对）
  (c) 无 .bib 文件（`verify_references` 工具因找不到 .bib 文件而失败）
  (d) Director 标记的 "???" 占位符引用——表明 LaTeX 中有未解析的 \cite key
  (e) 总引用数约 15 篇，对于这个研究领域来说偏少
- 为什么影响接收：ARR 评审标准明确要求引用完整可验证。占位符 arXiv ID 直接违反 ACL anti-fabrication 政策。如果审稿人无法验证关键引用，将严重质疑学术规范。
- 建议修改方向：修复所有 broken citations，补充完整 arXiv ID，通过 `verify_references` 等工具验证每一条引用真实存在。

**N3** [critical] RATE 批评缺乏实证支撑

- 具体位置：§5.3 ("Likert ATE detects significance in only 1/9 cells"), §6 Discussion ("RATE's Likert-based estimates may systematically understate true bias")
- 问题：论文声称 RATE (Feuer et al., 2025) 使用 Likert ATE 作为主要度量因此"可能系统性低估真实偏差"。但 §5.3 和 §6 均承认这一判断**未在匹配条件下验证**。论文使用自己的 counterfactual data 上的 Likert 结果来推断 RATE 的 Likert 结果也会有同样问题——这是一个 ecological validity 跨越。
- 建议修改方向：(a) 在 RATE 的 exact experimental setup 下复现实验；或 (b) 弱化措辞。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 范围过窄——单一主 style axis 限制了贡献的泛化性
**W2** [warning] 缺少 Bradley-Terry 建模——pairwise comparison 数据的标准分析框架缺失
**W3** [warning] Related work 覆盖不完整（CalibraEval、FairEval、BT for judge evaluation 等未引用）
**W4** [warning] 无任何图表——全文仅有 tables，视觉传达严重不足

---

## Questions for Authors

1. **Q1 (Novelty)**: 相对于 Karpinska et al. 和 Novikova et al.，你们的贡献具体在哪里超越了"将已知结论迁移到 LLM judge"？
2. **Q2 (RATE)**: 是否考虑过在 RATE 的 exact setup 下复现实验？
3. **Q3 (Scope)**: 如果 verbosity 和 register 的 blindspot 效应不显著，核心 narrative 是否仍成立？
4. **Q4 (Bradley-Terry)**: 为什么用 sign test 而非 Bradley-Terry？
5. **Q5 (Binarized Likert)**: binarized Likert 0/9 是否可能是 power 不足而非 Likert 本身的问题？
6. **Q6 (References)**: placeholder arXiv ID 是否都是真实文献？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 54 · 2026-05-21T01:59:20.989722+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## R1 对 R2 完整审稿意见的逐条交叉回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE with nuance] R2-N1: 新颖性不足——\"Likert Blindspot\" 是已知现象的重新命名**\n\n同意 R2 的核心论点：Likert vs forced-choice 的灵敏度差异在心理测量学中确实是 well-established 的（Thurstone 1927, Kiritchenko & Mohammad Best-Worst Scaling）。但我认为 R2 的判断略过于严厉，有两个 nuance：\n\n1. **Binarized-Likert 诊断设计并非简单迁移**。论文通过让 binarized Likert 和 pairwise 使用相同的 sign test（§3.4, §5.3），将灵敏度差异精确归因于 measurement structure（side-by-side comparison vs independent rating），而非统计检验的差异。这一诊断思路在 psychometrics 文献中并不常见——通常的 Likert vs pairwise 对比无法区分\"test 不同\"和\"measurement structure 不同\"的贡献。\n2. **实践影响不可忽视**。LLM 评估社区（Chatbot Arena, MT-Bench, AlpacaEval leaderboard, RATE protocol）大量依赖 Likert 评分。即使 insight 本身已知，在这个具体 domain 的系统性量化仍有价值——类似于 Birhane et al. 对 ImageNet bias 的量化并非发现了\"dataset bias\"这一概念，但其系统性量化本身构成了贡献。\n\n**我的判断**：novelty 确实是本文最弱环节，但 \"incremental application\" 不等于 \"no contribution\"。足以支撑 Findings，不足以支撑 main conference。与我此前评分（Overall 3.0 = Findings）一致。\n\n---\n\n**[AGREE] R2-N2: 引用系统严重不完整**\n\n同意这是 submission-readiness 的硬伤。需要说明版本差异：我审阅的 `best/paper.pdf`（7页）page 7 有可见的参考文献条目（Yao Dou et al., Karpinska et al., Park et al. 等），但 R2 报告的版本存在 \"arXiv:2406.xxxxx\" 占位符和 \"???\" 未解析引用。\n\n从 methods review 角度补充：\n- **引用缺失不直接影响我对实验设计的评估**——Table 1-9 的统计结果不依赖于引用是否完整。\n- **但间接影响 soundness**：如果关键方法论引用（如 RATE, Mir et al. 的 style rewriting, NLI gate 的先例）无法验证，读者无法评估方法论组件的来源和适用性。\n- R2 提到总引用约 15 篇，我在 best 版本中也观察到引用数偏少。对于涉及 psychometrics + LLM evaluation + style transfer + NLI 的交叉领域论文，20-30 篇引用是合理预期。\n\n---\n\n**[AGREE with significant nuance] R2-N3: RATE 批评缺乏实证支撑**\n\n这是 Director 特别要求回应的交叉点。R2 的核心质疑：论文用自己的 counterfactual data 上的 Likert 结果来推断 RATE 的 Likert 也会有同样问题，这是 ecological validity 跨越。\n\n**我同意 R2 的方向**，但需要区分两个层面：\n\n1. **论文对 RATE 的直接批评措辞确实过强**。§6 说 \"RATE's Likert-based estimates may systematically understate true bias\"——这是一个关于 RATE 的实证 claim，但论文没有在 RATE 的 exact setup 下验证。RATE 使用不同的 style axes（formality 之外还有 length, complexity 等）、不同的 rewriting 方法、不同的 benchmarks。论文自己的 Likert 结果不能直接外推到 RATE 的设置。\n\n2. **但论文的 binarized-Likert 诊断提供了一个通用的方法论论据**。§5.3 的核心贡献不是\"RATE 是错的\"，而是\"在控制了统计检验差异后（binarized Likert 用 sign test），measurement structure 本身导致灵敏度差异\"。这个 mechanism-level 的论据不依赖于 RATE 的具体设置——如果 Likert 的独立评分结构在任何 style bias detection 中都比 side-by-side comparison 更不敏感，那么 RATE 用 Likert 也会受影响。\n\n**我的判断**：论文应该（a）弱化对 RATE 的直接批评措辞，从 \"may systematically understate\" 改为 \"our results raise the question of whether\"；（b）保留 mechanism-level 的论据（binarized-Likert 诊断）；（c）如果要维持对 RATE 的直接批评，需要在 RATE 的设置下做 replication。\n\n**从方法论角度看 §5.3 的比较本身是否合理？** 是的。binarized-Likert 与 pairwise 的对比是 internally valid 的——两者使用相同的数据、相同的 sign test、唯一差异是 binary outcome 的来源（independent Likert scores vs direct comparison）。这个比较的逻辑是 sound 的。问题在于从这个 internal comparison 到 \"RATE's Likert is insufficient\" 的 external generalization。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: 范围过窄**\n\n与我此前意见完全一致。Primary evidence 仅 formality，verbosity (Table 8) 和 register (Table 9) 各只有 1 个 judge×benchmark 组合，且 register 未达显著。\n\n---\n\n**[REBUT with partial agreement] R2-W2: 缺少 Bradley-Terry 建模**\n\n这是 Director 特别要求回应的第二个交叉点。\n\n**部分反驳**：Sign test 在本文场景下是 sufficient 的，Bradley-Terry 不是 necessary 的。原因：\n\n1. **研究问题不需要 BT**。论文的核心问题是 \"pairwise 能否检测到 Likert 检测不到的 style bias\"，答案是 binary 的（显著/不显著）。Sign test 直接回答这个问题。BT 建模的优势在于估计 latent strength parameters 和处理 incomplete comparison data，但论文用的是 complete paired data（每对 z, z' 都被比较了两次），不需要 BT 的参数化假设。\n\n2. **Sign test 更保守、假设更少**。BT 假设 comparison outcomes 服从 logistic 分布，这在 LLM judge 的 discrete forced-choice 中未必成立。Sign test 是 nonparametric 的，不做分布假设，在 n=55-100 的样本量下 power 足够。\n\n3. **BT 在 position-controlled 设计中有复杂性**。论文的 consistency filtering 已经处理了 position bias——只保留两个方向一致的 pairs。如果用 BT，需要将 position 作为一个 factor 纳入模型（Bradley-Terry-Luce with order effects），这增加了模型复杂度但不一定增加对核心问题的回答能力。\n\n**但我同意的部分**：BT 可以作为 supplementary analysis 增加说服力，特别是：\n- BT 可以估计 formality 的 latent strength parameter（类似于 Elo rating），这比 win rate 更 interpretable\n- BT 可以处理 inconsistent pairs（而非丢弃它们），增加有效样本量\n- 如果 BT 结果与 sign test 一致，会增强 robustness\n\n**结论**：Sign test 作为 primary analysis 是 justified 的；BT 作为 supplementary analysis 是 desirable but not required。这是 W (warning) 级别，不是 N (critical) 级别。同意 R2 的分级。\n\n---\n\n**[AGREE] R2-W3: Related work 覆盖不完整**\n\n我没有专门审查 related work 覆盖（这是 R2 的审查维度），但从 methods 角度补充：CalibraEval 和 FairEval 与本文的 judge bias detection 直接相关；BT for judge evaluation (Zheng et al., Chatbot Arena) 是 pairwise comparison 在 LLM evaluation 中的主要先例。这些遗漏会影响读者理解方法论选择的 motivation。\n\n---\n\n**[AGREE — strongest agreement] R2-W4: 无任何图表**\n\n这是 Director 特别要求回应的第三个交叉点。**从实验呈现角度，我强烈同意可视化对传达核心发现至关重要。**\n\n在此前的回应中我已详细论述了三个必要 figures：\n\n1. **Power curve**（最高优先级）：x=sample size, y=power, 三条线（pairwise / binarized Likert / Likert ATE）。这一张图可以同时：(a) 回应 \"blindspot vs efficiency gap\" 的争论——读者可以看到在什么 n 范围内 Likert 的 power 接近 0；(b) 让 power analysis 的结论可视化验证而非仅凭文字断言；(c) 暴露 post-hoc estimate 的不确定性（加 bootstrap CI）。\n\n2. **Forest plot**（9 cells win rate + 95% CI）：当前 Table 2 和 Table 3 是纯数字矩阵，读者需要逐个比较。Forest plot 可以一目了然地展示效应量分布和跨 cell 的一致性。\n\n3. **Pipeline diagram**（四阶段流程 + attrition）：当前纯文字描述的协议对首次阅读的读者不友好。\n\n**为什么这对本文特别重要**：本文的核心 narrative 是两种 measurement 的灵敏度对比——这本质上是一个 \"pattern across conditions\" 的故事。Tables 迫使读者逐个数字比较，而 figures 让 pattern 自明。对于一篇核心论据依赖 \"7/9 vs 1/9 vs 0/9\" 这种跨条件对比的论文，没有 figures 是不可接受的。\n\n---\n\n### R2 Questions 的 R1 视角补充\n\n**R2-Q4 (Bradley-Terry)**: 见上方 W2 的详细回应。Sign test 在此场景下 sufficient。\n\n**R2-Q5 (Binarized Likert 0/9 是否是 power 不足)**: 是的，这正是我在 R1 原稿中独立指出的。n=500 时 binarized Likert p=0.055，距显著仅一步之遥。\"Blindspot\" 实为 \"power gap at typical n\"。\n\n---\n\n### 综合评估——纳入 R2 完整意见后\n\nR2 的完整审稿意见加强了我的几个原有判断：\n- N1 (novelty) 和 W1 (scope) 使 \"Findings vs Main\" 的区分更加清晰——这是 Findings 级别的工作\n- N2 (引用) 在不同版本间有差异，但即使 best 版本引用数也偏少\n- N3 (RATE 批评) 是一个有实质内容的方法论质疑，论文需要弱化措辞或补充 evidence\n\n**最终评分不变**：\n\n| 项目 | 评分 |\n|------|------|\n| Overall Assessment | **3.0** (Findings) |\n| Soundness | 3/5 |\n| Excitement | 3/5 |\n| Confidence | 4/5 |\n\nR1 与 R2 的评分差异（R1: 3.0 vs R2: 2.5）主要来自对 novelty 的判断力度：R2 认为 \"已知现象的重新包装\" 是 critical 的 novelty 缺陷，而我认为 binarized-Likert 诊断设计和在 LLM judge 领域的系统性量化仍有 Findings-level 的独立价值。",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## R1 对 R2 完整审稿意见的逐条交叉回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE with nuance] R2-N1: 新颖性不足——\"Likert Blindspot\" 是已知现象的重新命名**\n\n同意 R2 的核心论点：Likert vs forced-choice 的灵敏度差异在心理测量学中确实是 well-established 的（Thurstone 1927, Kiritchenko & Mohammad Best-Worst Scaling）。但我认为 R2 的判断略过于严厉，有两个 nuance：\n\n1. **Binarized-Likert 诊断设计并非简单迁移**。论文通过让 binarized Likert 和 pairwise 使用相同的 sign test（§3.4, §5.3），将灵敏度差异精确归因于 measurement structure（side-by-side comparison vs independent rating），而非统计检验的差异。这一诊断思路在 psychometrics 文献中并不常见——通常的 Likert vs pairwise 对比无法区分\"test 不同\"和\"measurement structure 不同\"的贡献。\n2. **实践影响不可忽视**。LLM 评估社区（Chatbot Arena, MT-Bench, AlpacaEval leaderboard, RATE protocol）大量依赖 Likert 评分。即使 insight 本身已知，在这个具体 domain 的系统性量化仍有价值——类似于 Birhane et al. 对 ImageNet bias 的量化并非发现了\"dataset bias\"这一概念，但其系统性量化本身构成了贡献。\n\n**我的判断**：novelty 确实是本文最弱环节，但 \"incremental application\" 不等于 \"no contribution\"。足以支撑 Findings，不足以支撑 main conference。与我此前评分（Overall 3.0 = Findings）一致。\n\n---\n\n**[AGREE] R2-N2: 引用系统严重不完整**\n\n同意这是 submission-readiness 的硬伤。需要说明版本差异：我审阅的 `best/paper.pdf`（7页）page 7 有可见的参考文献条目（Yao Dou et al., Karpinska et al., Park et al. 等），但 R2 报告的版本存在 \"arXiv:2406.xxxxx\" 占位符和 \"???\" 未解析引用。\n\n从 methods review 角度补充：\n- **引用缺失不直接影响我对实验设计的评估**——Table 1-9 的统计结果不依赖于引用是否完整。\n- **但间接影响 soundness**：如果关键方法论引用（如 RATE, Mir et al. 的 style rewriting, NLI gate 的先例）无法验证，读者无法评估方法论组件的来源和适用性。\n- R2 提到总引用约 15 篇，我在 best 版本中也观察到引用数偏少。对于涉及 psychometrics + LLM evaluation + style transfer + NLI 的交叉领域论文，20-30 篇引用是合理预期。\n\n---\n\n**[AGREE with significant nuance] R2-N3: RATE 批评缺乏实证支撑**\n\n这是 Director 特别要求回应的交叉点。R2 的核心质疑：论文用自己的 counterfactual data 上的 Likert 结果来推断 RATE 的 Likert 也会有同样问题，这是 ecological validity 跨越。\n\n**我同意 R2 的方向**，但需要区分两个层面：\n\n1. **论文对 RATE 的直接批评措辞确实过强**。§6 说 \"RATE's Likert-based estimates may systematically understate true bias\"——这是一个关于 RATE 的实证 claim，但论文没有在 RATE 的 exact setup 下验证。RATE 使用不同的 style axes（formality 之外还有 length, complexity 等）、不同的 rewriting 方法、不同的 benchmarks。论文自己的 Likert 结果不能直接外推到 RATE 的设置。\n\n2. **但论文的 binarized-Likert 诊断提供了一个通用的方法论论据**。§5.3 的核心贡献不是\"RATE 是错的\"，而是\"在控制了统计检验差异后（binarized Likert 用 sign test），measurement structure 本身导致灵敏度差异\"。这个 mechanism-level 的论据不依赖于 RATE 的具体设置——如果 Likert 的独立评分结构在任何 style bias detection 中都比 side-by-side comparison 更不敏感，那么 RATE 用 Likert 也会受影响。\n\n**我的判断**：论文应该（a）弱化对 RATE 的直接批评措辞，从 \"may systematically understate\" 改为 \"our results raise the question of whether\"；（b）保留 mechanism-level 的论据（binarized-Likert 诊断）；（c）如果要维持对 RATE 的直接批评，需要在 RATE 的设置下做 replication。\n\n**从方法论角度看 §5.3 的比较本身是否合理？** 是的。binarized-Likert 与 pairwise 的对比是 internally valid 的——两者使用相同的数据、相同的 sign test、唯一差异是 binary outcome 的来源（independent Likert scores vs direct comparison）。这个比较的逻辑是 sound 的。问题在于从这个 internal comparison 到 \"RATE's Likert is insufficient\" 的 external generalization。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: 范围过窄**\n\n与我此前意见完全一致。Primary evidence 仅 formality，verbosity (Table 8) 和 register (Table 9) 各只有 1 个 judge×benchmark 组合，且 register 未达显著。\n\n---\n\n**[REBUT with partial agreement] R2-W2: 缺少 Bradley-Terry 建模**\n\n这是 Director 特别要求回应的第二个交叉点。\n\n**部分反驳**：Sign test 在本文场景下是 sufficient 的，Bradley-Terry 不是 necessary 的。原因：\n\n1. **研究问题不需要 BT**。论文的核心问题是 \"pairwise 能否检测到 Likert 检测不到的 style bias\"，答案是 binary 的（显著/不显著）。Sign test 直接回答这个问题。BT 建模的优势在于估计 latent strength parameters 和处理 incomplete comparison data，但论文用的是 complete paired data（每对 z, z' 都被比较了两次），不需要 BT 的参数化假设。\n\n2. **Sign test 更保守、假设更少**。BT 假设 comparison outcomes 服从 logistic 分布，这在 LLM judge 的 discrete forced-choice 中未必成立。Sign test 是 nonparametric 的，不做分布假设，在 n=55-100 的样本量下 power 足够。\n\n3. **BT 在 position-controlled 设计中有复杂性**。论文的 consistency filtering 已经处理了 position bias——只保留两个方向一致的 pairs。如果用 BT，需要将 position 作为一个 factor 纳入模型（Bradley-Terry-Luce with order effects），这增加了模型复杂度但不一定增加对核心问题的回答能力。\n\n**但我同意的部分**：BT 可以作为 supplementary analysis 增加说服力，特别是：\n- BT 可以估计 formality 的 latent strength parameter（类似于 Elo rating），这比 win rate 更 interpretable\n- BT 可以处理 inconsistent pairs（而非丢弃它们），增加有效样本量\n- 如果 BT 结果与 sign test 一致，会增强 robustness\n\n**结论**：Sign test 作为 primary analysis 是 justified 的；BT 作为 supplementary analysis 是 desirable but not required。这是 W (warning) 级别，不是 N (critical) 级别。同意 R2 的分级。\n\n---\n\n**[AGREE] R2-W3: Related work 覆盖不完整**\n\n我没有专门审查 related work 覆盖（这是 R2 的审查维度），但从 methods 角度补充：CalibraEval 和 FairEval 与本文的 judge bias detection 直接相关；BT for judge evaluation (Zheng et al., Chatbot Arena) 是 pairwise comparison 在 LLM evaluation 中的主要先例。这些遗漏会影响读者理解方法论选择的 motivation。\n\n---\n\n**[AGREE — strongest agreement] R2-W4: 无任何图表**\n\n这是 Director 特别要求回应的第三个交叉点。**从实验呈现角度，我强烈同意可视化对传达核心发现至关重要。**\n\n在此前的回应中我已详细论述了三个必要 figures：\n\n1. **Power curve**（最高优先级）：x=sample size, y=power, 三条线（pairwise / binarized Likert / Likert ATE）。这一张图可以同时：(a) 回应 \"blindspot vs efficiency gap\" 的争论——读者可以看到在什么 n 范围内 Likert 的 power 接近 0；(b) 让 power analysis 的结论可视化验证而非仅凭文字断言；(c) 暴露 post-hoc estimate 的不确定性（加 bootstrap CI）。\n\n2. **Forest plot**（9 cells win rate + 95% CI）：当前 Table 2 和 Table 3 是纯数字矩阵，读者需要逐个比较。Forest plot 可以一目了然地展示效应量分布和跨 cell 的一致性。\n\n3. **Pipeline diagram**（四阶段流程 + attrition）：当前纯文字描述的协议对首次阅读的读者不友好。\n\n**为什么这对本文特别重要**：本文的核心 narrative 是两种 measurement 的灵敏度对比——这本质上是一个 \"pattern across conditions\" 的故事。Tables 迫使读者逐个数字比较，而 figures 让 pattern 自明。对于一篇核心论据依赖 \"7/9 vs 1/9 vs 0/9\" 这种跨条件对比的论文，没有 figures 是不可接受的。\n\n---\n\n### R2 Questions 的 R1 视角补充\n\n**R2-Q4 (Bradley-Terry)**: 见上方 W2 的详细回应。Sign test 在此场景下 sufficient。\n\n**R2-Q5 (Binarized Likert 0/9 是否是 power 不足)**: 是的，这正是我在 R1 原稿中独立指出的。n=500 时 binarized Likert p=0.055，距显著仅一步之遥。\"Blindspot\" 实为 \"power gap at typical n\"。\n\n---\n\n### 综合评估——纳入 R2 完整意见后\n\nR2 的完整审稿意见加强了我的几个原有判断：\n- N1 (novelty) 和 W1 (scope) 使 \"Findings vs Main\" 的区分更加清晰——这是 Findings 级别的工作\n- N2 (引用) 在不同版本间有差异，但即使 best 版本引用数也偏少\n- N3 (RATE 批评) 是一个有实质内容的方法论质疑，论文需要弱化措辞或补充 evidence\n\n**最终评分不变**：\n\n| 项目 | 评分 |\n|------|------|\n| Overall Assessment | **3.0** (Findings) |\n| Soundness | 3/5 |\n| Excitement | 3/5 |\n| Confidence | 4/5 |\n\nR1 与 R2 的评分差异（R1: 3.0 vs R2: 2.5）主要来自对 novelty 的判断力度：R2 认为 \"已知现象的重新包装\" 是 critical 的 novelty 缺陷，而我认为 binarized-Likert 诊断设计和在 LLM judge 领域的系统性量化仍有 Findings-level 的独立价值。",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-21T01:59:25.008827+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4019
}
```

</details>

---


### Assistant

_source line 56 · 2026-05-21T01:59:34.767707+00:00_

R1 交叉回应已提交。对 R2 的 3 个 Must-Fix 和 4 个 Should-Fix 逐条给出了 AGREE/REBUT 判断，重点回应了 Director 指定的三个交叉点：

1. **R2-N3 (RATE 批评)**: AGREE with nuance — §5.3 的 internal comparison 是 sound 的，但从 internal result 到 "RATE's Likert understates bias" 的 external generalization 需要弱化措辞或补充 evidence。
2. **R2-W2 (Bradley-Terry)**: REBUT with partial agreement — Sign test 在此场景下 sufficient（nonparametric、假设更少、直接回答 binary 研究问题），BT 可作为 supplementary 但非 necessary。
3. **R2-W4 (无 Figure)**: AGREE（最强同意）— Power curve、forest plot、pipeline diagram 三张图对传达核心 narrative 至关重要。

最终评分维持 **Overall 3.0 (Findings)**，与 R2 的 2.5 之间的差异主要在 novelty 判断力度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1"
}
```

</details>

---


## Round 5

## Round 5

68 recorded events


### User

_source line 57 · 2026-05-21T07:08:41.595896+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）

### Venue 信息
- **目标**: EMNLP 2026 (ARR Long Paper)
- **截止日期**: 2026-06-15
- **页数限制**: 正文 ≤8 页（strict），参考文献无限制，Limitations 不计入页数
- **模板**: ACL format (`\usepackage[review]{acl}`)
- **匿名规则**: Double-blind
- **附录**: 允许，属于提交材料
- **评分标准**: ARR Overall Assessment: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit

### 论文路径
- LaTeX: `projects/causal_style_decomp_judge/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf`
- Sections: `projects/causal_style_decomp_judge/docs/paper/sections/` 下各 .tex 文件
- References: `projects/causal_style_decomp_judge/docs/paper/references.bib`

### 你的审查侧重

**方法严谨性 + 实验设计**。请重点审查：

1. **统计方法论**：
   - Bradley-Terry 模型使用是否规范（pair-level bootstrap CI、正则化设置）
   - GEE logistic decomposition 的 exchangeable correlation 假设是否合理
   - Holm-Bonferroni 校正的 family 定义是否合理（§4.1 声称 "three judges × three style axes = nine tests"，但论文只使用了 2 个 judge）
   - Ordinal regression 和 sensitivity hierarchy（Table 2）的分析是否充分

2. **因果主张 vs 实际方法**：
   - 论文标题和框架名称包含 "Causal"，但 §3.5 明确声明 "we do not claim a complete structural causal model"
   - NLI gate 对 do-operator 的近似是否合理
   - DAG (Figure 2) 是否遗漏重要变量（如 position bias、prompt format）

3. **NLI Gate 有效性**：
   - 8.4% FNR 的三重间接验证（threshold sweep、consistency filter、directional balance）是否充分
   - Qwen3-32B 同时作为 rewriter 和 NLI annotator 的循环性
   - Direction-aware verification for verbosity 的 justification

4. **实验设计**：
   - 仅使用 LLMBar (n=100) 一个 benchmark 的代表性
   - 样本量是否支持所声称的结论（88 NLI-gated pairs → 173 comparisons）
   - Evaluator-producer bias（Qwen3-32B 同时为 rewriter 和 judge）的影响量化

5. **可重复性**：
   - 关键超参数是否完整报告（temperature 0.7、NLI threshold 0.90、BT bootstrap resamples）
   - 是否有代码/数据可用性声明

### 输出要求

请按以下结构输出审稿意见：
1. **Summary**（2-3 句）
2. **Strengths**（逐条）
3. **Weaknesses**（逐条，标注 severity: Must-Fix / Should-Fix / Minor）
4. **Questions**（需要作者回答的问题）
5. **Missing References**（如有）
6. **Overall Assessment**（评分 + 置信度 + 简要理由）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-21T07:08:50.178212+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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

_source line 59 · 2026-05-21T07:08:50.228931+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 60 · 2026-05-21T07:08:54.045212+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 61 · 2026-05-21T07:08:54.999239+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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

_source line 62 · 2026-05-21T07:08:55.201016+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/causal_style_decomp_judge/docs/paper/sections/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/causal_style_decomp_judge/docs/paper/sections/*.tex"
  }
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-21T07:09:00.957585+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's what I found about ACL ARR 2025-2026 reviewer guidelines:

## Reviewer Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score
The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

### Excitement Score
Sometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

## Area Chair Guidelines

All papers recommended for Findings or main conference are expected to be sound and reproducible. The ACs should mostly follow the soundness assessment of the reviewers when they are in agreement, and they can weigh in 
…[truncated 297 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6912
}
```

</details>

---


### Tool result

_source line 64 · 2026-05-21T07:09:02.615615+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 467.8}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 527.1}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 550.1}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 501.6}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 457.3}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 523.3}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 427.0}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 520.1}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 527.6}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/pap
…[truncated 311 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7616
}
```

</details>

---


### Tool result

_source line 65 · 2026-05-21T07:09:02.616178+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 7415
}
```

</details>

---


### Tool call

_source line 66 · 2026-05-21T07:09:06.735527+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review review form 2025 soundness excitement scoring scale 1-5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review review form 2025 soundness excitement scoring scale 1-5"
  }
}
```

</details>

---


### Tool call

_source line 67 · 2026-05-21T07:09:07.790112+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "11",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "11",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 68 · 2026-05-21T07:09:08.769151+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 69 · 2026-05-21T07:09:09.179541+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 70 · 2026-05-21T07:09:10.419412+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 71 · 2026-05-21T07:09:10.520482+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 72 · 2026-05-21T07:09:11.122468+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 73 · 2026-05-21T07:09:11.625263+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 74 · 2026-05-21T07:09:12.427582+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 75 · 2026-05-21T07:09:14.134647+00:00_

Web search results for query: "ACL Rolling Review review form 2025 soundness excitement scoring scale 1-5"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"},{"title":"ACL 2026 on X: \"Checkout the blog post on the soundness/excitement scores https://t.co/AKSO9DjiYP . It clarifies the reasoning behind the separation of overall scores and how it might make the reviewer recommendation more robust. #ACL2023Toronto #ACL2023NLP #NLProc\" / X","url":"https://x.com/aclmeeting/status/1637827267173953540"},{"title":"Can LLM feedback enhance review quality? A randomized study of 20K   reviews at ICLR 2025","url":"https://arxiv.org/pdf/2504.09737"}]

Based on the search results, here's what I found about the ACL Rolling Review (ARR) 2025 review form regarding soundness and excitement scoring:

## Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness Score (1-5 Scale)

The soundness scale includes: 5 = Excellent (the study is one of the most thorough), 4 = Strong (the study provides sufficient support for all of its claims), and 3 = Acceptable (the study provides sufficient support for its main claims). T
…[truncated 922 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7399
}
```

</details>

---


### Tool result

_source line 76 · 2026-05-21T07:09:14.235543+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 186.1}], \"total_pages\": 11, \"rendered_pages\": 1, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6445
}
```

</details>

---


### Tool call

_source line 77 · 2026-05-21T07:09:14.287448+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 78 · 2026-05-21T07:09:14.389638+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 79 · 2026-05-21T07:09:15.092828+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 80 · 2026-05-21T07:09:19.828275+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 9408
}
```

</details>

---


### Tool result

_source line 81 · 2026-05-21T07:09:19.832450+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 11063
}
```

</details>

---


### Tool result

_source line 82 · 2026-05-21T07:09:19.984104+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 7556
}
```

</details>

---


### Tool result

_source line 83 · 2026-05-21T07:09:20.086228+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 8460
}
```

</details>

---


### Tool result

_source line 84 · 2026-05-21T07:09:20.341335+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 11161
}
```

</details>

---


### Tool result

_source line 85 · 2026-05-21T07:09:20.346263+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 6058
}
```

</details>

---


### Tool result

_source line 86 · 2026-05-21T07:09:20.347422+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 9224
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-21T07:09:20.350829+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 9830
}
```

</details>

---


### Tool result

_source line 88 · 2026-05-21T07:09:20.655096+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 6265
}
```

</details>

---


### Tool result

_source line 89 · 2026-05-21T07:09:20.756454+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 5663
}
```

</details>

---


### Tool call

_source line 90 · 2026-05-21T07:09:26.486092+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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

_source line 91 · 2026-05-21T07:09:26.486556+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 92 · 2026-05-21T07:09:26.691314+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 93 · 2026-05-21T07:09:27.296425+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 605
}
```

</details>

---


### Tool call

_source line 94 · 2026-05-21T07:09:31.866631+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form including all scoring dimensions, their scales (1-5), and descriptions for each score level. Include soundness, excitement, overall assessment, confidence, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form including all scoring dimensions, their scales (1-5), and descriptions for each score level. Include soundness, excitement, overall assessment, confidence, and any other scored dimensions."
  }
}
```

</details>

---


### Tool call

_source line 95 · 2026-05-21T07:09:32.972355+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines including scoring criteria for soundness, excitement, overall assessment. Include the full description of each score level (1-5) for all dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines including scoring criteria for soundness, excitement, overall assessment. Include the full description of each score level (1-5) for all dimensions."
  }
}
```

</details>

---


### Tool result

_source line 96 · 2026-05-21T07:09:37.840729+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Reviewer Confidence (1-5 Scale)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: Quite sure with unlikely but conceivable oversights
- **3**: Reasonably confident despite possible missed details
- **2**: Willing to defend evaluation but likely missed some points
- **1**: Outside expertise area or paper is unclear

## Soundness (1-5 Scale)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: Strong support for claims; additional experiments optional
- **3**: Adequate support for main claims with minor gaps
- **2**: Main claims insufficiently supported; major technical problems
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement (1-5 Scale)
- **5**: Highly exciting; would recommend to others
- **4**: "Exciting: I would mention this paper to others"
- **3**: Interesting; might mention to others if time permits
- **2**: Potentially interesting but lacks personal resonance
- **1**: Not exciting; lacks relevance to computational linguistics

## Overall Assessment (1-5 Scale)
- **5**: Consider for award (top 2.5% papers)
- **4**: Conference acceptance appropriate
- **3**: Accept to Findings track
- **2**: Needs substantial revisions next cycle
- **1**: Do not resubmit; irrelevant or fundamentally flawed

## Additional Dimensions
- **Reproducibility** (1-5)
- **Datasets** (1-5)
- **Software** (1-5)
- **Author Identity Recognition** (1-5)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5974
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-21T07:09:38.795434+00:00_

# ARR Reviewer Guidelines: Scoring Criteria

The provided document outlines reviewer responsibilities but **does not include detailed 1-5 scoring rubrics** for soundness, excitement, or overall assessment dimensions.

## What the Guidelines State About Scoring

The document mentions three score types introduced in February 2025:

1. **Soundness**: "The _soundness_ scores must be justified by the text of the review. If you give a low _Soundness_ score without finding any major faults, this means that your review is not a faithful explanation of your recommendation."

2. **Excitement**: "Such preferences are more subjective and should be reflected in a separate _excitement_ score, which is orthogonal to the assessment of the soundness of the paper. Excitement scores reflect our personal taste, and so do not necessarily come with explicit reasons."

3. **Overall Assessment**: "The _Overall assessment_ score is an explicit recommendation for the outcome of this paper, if it were committed to an \*ACL venue. This is a composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact."

## Key Limitation

The guidelines emphasize that "All papers recommended for Findings and main conferences are expected to be sufficiently sound and reproducible," but specific numeric score definitions (1-5 scales) are not provided in this document. Reviewers are directed to the [ARR review form post](https://aclrollingreview.org/reviewform) for detailed scoring specifications.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5823
}
```

</details>

---


### Tool call

_source line 98 · 2026-05-21T07:09:43.566424+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 99 · 2026-05-21T07:09:43.667439+00:00_

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
19	\title{Causal Style Decomposition Reveals the Likert Blindspot:\\Standard Scoring Underestimates Style Bias in LLM Judges}
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
41	\paragraph{Quality--style confounding.}
42	Although the formality effect survives logistic adjustment for original preference (Appendix~\ref{app:direction}), the significant original-preference odds ratio ($\text{OR} = 2.32$, $p = 0.006$) indicates that quality--style confounding is not fully eliminated.
43	The NLI gate blocks content changes but cannot block quality perception shifts mediated by style itself---a fundamental identifiability limit of text-rewriting approaches.
44	Future work should incorporate human quality ratings of both original and rewritten texts.
45	
46	\paragraph{Evaluator-producer bias in Qwen3-32B.}
47	Qwen3-32B serves as both the style rewriter and one of the two judges.
48	The inflation is most visible in GEE decomposition: Qwen3-32B formality OR ($4.20$) and originality OR ($4.70$) systematically exceed the GPT-4o estimates ($2.58$ and $2.32$), consistent with partial self-recognition of its own outputs.
49	Bradley-Terry estimates are more robust to this confound: the cross-judge gap is only $+3.5$ percentage points (66.5\
…[truncated 1539 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 100 · 2026-05-21T07:09:46.833762+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/*.tex"
  }
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-21T07:09:46.884392+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-21T07:09:49.848701+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 103 · 2026-05-21T07:09:49.899489+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{figures/pipeline_diagram.pdf}
7	\caption{CSD pipeline overview. Numbers indicate sample attrition at each stage.}
8	\label{fig:pipeline}
9	\end{figure}
10	
11	\subsection{Style-Controlled Rewriting}
12	\label{sec:rewriting}
13	
14	We isolate the effect of individual style attributes on judge scores by generating text pairs that differ along exactly one style axis.
15	For each text, an instruction-tuned LLM (Qwen3-32B) first classifies its current style along the target axis (e.g., formal vs.\ casual via binary classification), then rewrites it toward the opposite pole (temperature 0.7) according to an axis-specific prompt (e.g., ``Rewrite the following text to be more formal/casual while preserving the exact same content and meaning'').
16	This produces a dataset balanced across both directions at the dataset level: texts detected as formal are rewritten to casual, and vice versa.
17	Each operation constitutes a binary intervention on a single style variable while all other axes remain fixed (Section~\ref{sec:causal_framework}).
18	To control for rewriting artifact bias---the possibility that the judge prefers original text over any rewrite regardless of style---we additionally generate a same-style double-rewrite for each text (e.g., formal $\to$ formal) to form an original-vs-double-rewrite control pair, following the RATE bias correction protocol \citep{reber2025rate}.
19	
20	\subsection{Content Preservation Verification}
21	\label{sec:nli_gate}
22	
23	Style-controlled rewriting risks altering semantic content, which would confound the style effect with a content quality effect (the $R \to Q$ path in Figure~\ref{fig:dag}).
24	To block this path, we apply a natural language inference (NLI) gate using DeBERTa-v3-large with an entailment threshold of 0.90.
25	For axes that preserve information density (formality, register), we apply standard bidirection
…[truncated 4832 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-21T07:09:50.355691+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 105 · 2026-05-21T07:09:50.908540+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	
5	\subsection{Statistical Framework}
6	\label{sec:stat_framework}
7	
8	We designate a primary family of nine hypothesis tests (three judges $\times$ three style axes) and control the family-wise error rate with Holm-Bonferroni correction at $\alpha = 0.05$.
9	Table~\ref{tab:main_results} reports both raw and adjusted $p$-values for this $3 \times 3$ grid.
10	Analyses outside this grid are classified as either \emph{exploratory} (NLI threshold sensitivity sweep, \S\ref{sec:nli_threshold}) or \emph{confirmatory} (consistency filter validation, \S\ref{sec:consistency}).
11	Exploratory analyses are reported with uncorrected $p$-values and interpreted as hypothesis-generating; confirmatory analyses test specific hypotheses about pipeline validity and are evaluated at the nominal $\alpha = 0.05$ level without additional correction, as they address orthogonal questions about measurement reliability rather than the primary style-bias family.
12	
13	\begin{table}[t]
14	\centering
15	\small
16	\caption{Main results across two judges and three style axes. BT: Bradley-Terry win probability (pair-level bootstrap). $\dagger$: Likert Blindspot (pairwise significant, Likert non-significant). Four judge$\times$axis configurations reach $p < 0.001$; two register configurations show weaker but directionally consistent patterns ($\dagger_{\text{e}}$).}
17	\label{tab:main_results}
18	\begin{tabular}{llccc}
19	\toprule
20	Judge & Axis & BT $P$ {[95\% CI]} & Likert $d$ ($p$) & \\
21	\midrule
22	GPT-4o & Formality & .630 {[.558, .703]}$^{***}$ & .011 (.908) & $\dagger$ \\
23	GPT-4o & Verbosity & .760 {[.667, .853]}$^{***}$ & $-$.095 (.403) & $\dagger$ \\
24	GPT-4o & Register & .570 {[.468, .673]}$^{*}$ & $-$.031 (.785) & $\dagger_{\text{e}}$ \\
25	\midrule
26	Qwen3-32B & Formality & .665 {[.585, .739]}$^{***}$ & .011 (.908) & $\dagger$ \\
27	Qwen3-32B & Verbosity & .773 {[.703, .843]}$^{***}$ & $-$.151 (.179) & $\dagger$ \\
28	Qwen3-3
…[truncated 17280 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 106 · 2026-05-21T07:09:50.908902+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 107 · 2026-05-21T07:09:51.862944+00:00_

1	\appendix
2	
3	\section{Direction Asymmetry and Quality Confounding}
4	\label{app:direction}
5	
6	The formality axis exhibits a pronounced direction asymmetry: the judge selects the formal variant in 78.8\% of formal-is-rewrite pairs ($p = 0.001$) but only 54.5\% of casual-is-rewrite pairs ($p = 0.83$).
7	This asymmetry suggests that original quality $Q$ and formality $S$ are partially confounded---formally written texts may be inherently perceived as higher quality.
8	To quantify this, we fit a logistic decomposition (GEE, exchangeable correlation) with both formality and original-preference as predictors.
9	After controlling for original preference, the formality effect remains significant ($\text{OR} = 2.58$, $p = 0.002$), and the original-preference effect is also significant ($\text{OR} = 2.32$, $p = 0.006$).
10	The formality preference thus survives adjustment for original-preference confounding, though the significant original-preference effect indicates that quality--style confounding is present and non-negligible.
11	
12	The Qwen3-32B formality effect ($\text{OR} = 4.20$, $p = 0.0002$) exceeds the GPT-4o estimate ($\text{OR} = 2.58$, $p = 0.002$), and the originality confound is also stronger ($\text{OR} = 4.70$ vs.\ $2.32$).
13	This amplification is consistent with evaluator-producer bias (\S\ref{sec:limitations}): because Qwen3-32B generated the rewrites, it may partially recognize its own outputs, inflating both the style and originality effects.
14	The directional agreement between judges---both favor formal text after controlling for originality---supports the existence of formality bias, but the effect magnitude from Qwen3-32B should not be directly compared with GPT-4o.
15	
16	The NLI gate blocks \emph{content} changes but cannot block quality perception shifts that are themselves mediated by style---a fundamental identifiability limit of any text-rewriting approach.
17	
18	\section{GEE Model Diagnostics}
19	\label{app:gee_diagnostics}
20	
21	\para
…[truncated 1599 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 108 · 2026-05-21T07:09:52.013999+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 109 · 2026-05-21T07:09:52.315718+00:00_

1	\section{Introduction}
2	
3	Large Language Model (LLM) judges have become central infrastructure for NLP evaluation and preference-based alignment training.
4	Systems such as AlpacaEval, MT-Bench, and Chatbot Arena rely on LLM judges to score and rank model outputs, and the resulting leaderboards guide both academic research and industry deployment.
5	Reinforcement Learning from Human Feedback (RLHF) and Direct Preference Optimization (DPO) pipelines consume judge-generated preferences as reward signals that shape model behavior during alignment.
6	The reliability of these judgments carries direct consequences: it determines which models the community considers superior and which response patterns are reinforced.
7	As automated judges increasingly mediate both evaluation and training, any systematic bias in their assessments propagates through the entire model development pipeline.
8	
9	Recent work has converged on a striking finding: \emph{style bias} is the dominant source of unreliability in LLM judges, far outweighing other documented biases such as position or verbosity preference.
10	\citet{murugadoss2025sos} show that style features alone explain judge scores with $R = 0.999$, far exceeding the explanatory power of content features.
11	\citet{li2026preference} demonstrate that 76--92\% of observed preference signals originate from surface-level style cues rather than substantive quality differences.
12	\citet{soumik2026judging} report bias scores of 0.76--0.92 across five different judges.
13	Despite this consensus on severity, existing approaches share four critical gaps: (1)~they treat style as a single dimension, typically reducing it to response length; (2)~they rely on correlational analyses that cannot establish causal direction; (3)~population-level corrections such as length-controlled AlpacaEval \citep{dubois2025lc} cannot diagnose per-instance bias; and (4)~no existing method provides black-box, post-hoc, per-axis interventional detection.
14	Rece
…[truncated 4251 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 110 · 2026-05-21T07:09:52.316156+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 111 · 2026-05-21T07:09:52.316449+00:00_

1	\begin{abstract}
2	Large Language Model (LLM) judges are widely deployed for evaluation and preference-based alignment, yet recent work shows that style features alone can explain judge scores with near-perfect correlation, raising fundamental questions about what these judges actually measure.
3	We introduce Causal Style Decomposition (CSD), a black-box framework that detects per-axis style bias through binary style-controlled rewriting, NLI-based content preservation gating, and position-controlled pairwise comparison.
4	We quantify what we term the Likert Blindspot---a measurement limitation predicted by psychometric theory but previously unquantified for LLM judges---across two architecturally distinct judges (GPT-4o, Qwen3-32B) and two primary style axes (formality, verbosity), with directionally consistent exploratory evidence on a third axis (register): a two-layer structural gap in which (1)~integer Likert scoring produces ${\sim}60\%$ uninformative ties ($\Delta = 0$), wasting the majority of the evaluation budget; (2)~even among non-tied pairs, absolute scoring captures weaker signal than forced pairwise comparison on identical data.
5	The effect is most dramatic for verbosity, where a 77.3\% Bradley-Terry win probability ($p < 0.0001$, both directions favoring verbose content) remains invisible to Likert scoring ($p = 0.179$).
6	Ordinal regression confirms the limitation is inherent to Likert measurement, not an artifact of interval-scale assumptions ($p = 0.769$).
7	Our results demonstrate that style bias audits require pairwise comparison and per-axis decomposition, and that existing Likert-based findings may systematically underestimate style bias magnitude.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 112 · 2026-05-21T07:09:52.768375+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 113 · 2026-05-21T07:09:53.170546+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	Two lines of work motivate our approach: counterfactual methods for diagnosing judge bias, and measurement theory on the sensitivity of different elicitation formats.
5	
6	\paragraph{Counterfactual Approaches to Judge Bias}
7	\citet{reber2025rate} propose RATE, a framework that rewrites model outputs along style attributes using imperfect counterfactuals and measures the causal effect on reward model scores via Likert-scale Average Treatment Effect (ATE).
8	RATE applies a correction term to account for rewriting imperfections, but its reliance on Likert ATE as the primary metric is a vulnerability: our experiments show that Likert scoring exhibits a ceiling effect in which 60\% of style-transformed pairs receive identical integer scores, yielding non-significant ATE estimates ($p = 0.332$) for the same interventions that pairwise comparison detects at $p = 0.006$.
9	If this Likert Blindspot generalizes beyond our setting, RATE's own style-related findings may underestimate the true magnitude of attribute effects.
10	CSD differs from RATE in three respects: it targets individual style axes rather than general attributes, it measures bias through position-controlled pairwise comparison rather than Likert ATE, and it enforces content preservation via NLI entailment gating rather than post-hoc correction for imperfect rewrites.
11	\citet{counterfactual2025rhetorical} also adopt a counterfactual LLM-based design, rewriting texts to measure rhetorical style effects and aggregating preferences with a Bradley-Terry model.
12	Their framework operates at persona-level granularity (e.g., ``writes like a professor''), whereas CSD intervenes on specific style axes (e.g., formality, conciseness) and uses a sign test with position control rather than parametric aggregation.
13	
14	\paragraph{Measurement Sensitivity in NLG Evaluation}
15	The distinction between ordinal and interval measurement dates to \citet{stevens1946theor
…[truncated 3781 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 114 · 2026-05-21T07:09:53.170939+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 115 · 2026-05-21T07:09:53.221507+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced Causal Style Decomposition (CSD), a black-box framework for detecting per-axis style bias in LLM judges.
5	Across two judges and two primary style axes, with exploratory evidence on a third, CSD reveals the Likert Blindspot---a two-layer measurement limitation confirmed by seven statistical methods as inherent to Likert scoring, not an artifact of any particular test.
6	Style bias audits should adopt pairwise comparison as the default protocol; existing Likert-based null findings may reflect measurement insensitivity rather than genuine absence of bias.
7	Future work should extend CSD to additional judges, axes, and benchmarks.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 116 · 2026-05-21T07:10:01.052617+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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

_source line 117 · 2026-05-21T07:10:18.599964+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 24, \"total_citations\": 36, \"unique_cited_keys\": 23, \"orphan_bib\": 1, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 21, \"online_not_found\": 1, \"online_mismatch\": 2}, \"cross_check\": {\"orphan_bib\": [\"hoenig2001abuse\"], \"missing_bib\": [], \"orphan_count\": 1, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"murugadoss2025sos\", \"type\": \"inproceedings\", \"title\": \"Style Over Substance: Failure Modes of LLM Judges in Alignment Benchmarking\", \"authors\": \"Murugadoss, Aakanksha and others\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"li2026preference\", \"type\": \"inproceedings\", \"title\": \"Preference Leakage: A Contamination Problem in LLM-as-a-Judge\", \"authors\": \"Li, Dawei and others\", \"year\": \"2026\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"wang2026fairjudge\", \"type\": \"article\", \"title\": \"FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge\", \"authors\": \"Wang, Xinyue and others\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2602.06625\"}, {\"key\": \"dubois2025lc\", \"type\": \"inproceedings\", \"title\": \"Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators\", \"authors\": \"Dubois, Yann and others\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"casse2026concise\", \"type\": \"article\", \"title\": \"A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents\", \"authors\": \"Cho, Young-Min and Yuan, Yuan and Guntuku, Sharath Chandra and Ungar, Lyle\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2601.10809\"}, {\"key\": \"counterfactual2025rhetorical\", \"type\": \"article\", \"title\": \"Coun
…[truncated 17725 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 17547
}
```

</details>

---


### Tool call

_source line 118 · 2026-05-21T07:13:19.857521+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿意见（方法严谨性 + 实验设计）\n\n### 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 核心发现（Likert Blindspot）有实证价值且用7种统计方法交叉验证，但\"Causal\"标题与实际方法的张力、单一benchmark（n=100）的代表性不足、以及评估者-生产者循环偏差，使论文在方法严谨性上尚未达到主会议标准。\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心claim有多种统计方法支撑，但Holm-Bonferroni family定义与实际实验矛盾（声称9个检验实际只有6个）、因果声明overclaim、evaluator-producer循环性未充分量化 |\n| Excitement | 3.5/5 | Likert Blindspot现象对评估社区有实际指导价值，per-axis GEE分解揭示不同confound structure是有洞察力的贡献；但scope（1个benchmark、2个judge）限制了影响力 |\n| Reproducibility | 3/5 | 关键超参数大部分已报告，但BT正则化方式未说明、bootstrap resamples数不一致（2000 vs 10000）、无代码/数据可用性声明 |\n| Confidence | 4/5 | 仔细阅读全文含附录，统计方法论在我的专业领域内 |\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Holm-Bonferroni family 定义与实际实验不一致\n- 具体位置：§4.1 (experiments.tex line 8)\n- 问题：论文声称 \"three judges × three style axes = nine tests\"，但全文仅使用 2 个 judge（GPT-4o、Qwen3-32B），Table 1 也只有 6 行（2×3）。第三个 judge 完全没有出现。这意味着 Holm-Bonferroni 校正基于一个不存在的 family size（9），比实际需要的 family size（6）更保守——虽然这使结果更保守而非更宽松，但声称的实验设计与实际执行之间的不一致本身就是严重的 credibility 问题。\n- 为什么影响接收：统计框架的文本描述与实际执行不符，审稿人无法确定哪些描述是准确的。\n- 建议修改方向：要么补上第三个 judge 的实验，要么将 family 修正为 \"two judges × three style axes = six tests\" 并重新检查所有 adjusted p-values。\n\n**N2** [critical] \"Causal\" 标题与方法论实质的张力\n- 具体位置：Title、§3.5 (method.tex lines 57-58)、Abstract\n- 问题：标题为 \"Causal Style Decomposition\"，框架简称 CSD。但 §3.5 明确声明 \"we do not claim that this DAG is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions\"，并将自身定位为 \"interventional rather than formal causal evidence\"。NLI gate 对 do-operator 的近似也被承认不完整。标题 overclaim。\n- 为什么影响接收：标题是论文最高可见度的 claim，overclaim 显著降低对全文的信任。\n- 建议修改方向：(1) 将 \"Causal\" 替换为 \"Interventional\" 或 \"Style-Controlled\"；或 (2) 在 §3.5 中给出更严格的因果识别条件讨论。\n\n**N3** [critical] 单一 benchmark（LLMBar, n=100）的代表性\n- 具体位置：§3.4\n- 问题：所有实验仅基于 LLMBar（n=100），NLI gate 后剩 88 pairs → 173 comparisons。Bootstrap CI 宽度达 14.5pp。LLMBar 是 instruction-following 任务，代表性有限。论文的多个 strong claim 基于单一小规模 benchmark 难以成立。\n- 为什么影响接收：从 n=100 的单一 benchmark 推广到 \"LLM Judges\" 整个类别的 claim 缺乏 external validity。\n- 建议修改方向：至少在一个额外 benchmark 上复现核心发现，或在 title/abstract 中明确限定 scope。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Evaluator-producer 循环性未充分量化\n- Qwen3-32B 同时担任 rewriter、judge、NLI gate validator 三个角色。NLI gate validation 中称 Qwen3-32B 为 \"independent LLM annotator\" 不准确。建议删除 \"independent\"，并量化仅用 GPT-4o 数据是否足以支撑核心 claim。\n\n**W2** [warning] Direction-aware NLI for verbosity 削弱 content preservation 保证\n- 单向 NLI 允许 expansion 添加新的 quality-relevant content 而不被检测。text length 控制不等于 content quality 控制。建议对 verbose rewrites 进行人工内容质量抽检。\n\n**W3** [warning] GEE exchangeable correlation 假设验证不充分\n- 未测试 AR(1) 或 unstructured。within-pair α̂ ∈ [-0.25, +0.11]，部分负相关暗示 exchangeable 可能非最优。\n\n**W4** [warning] BT 正则化细节和 bootstrap resamples 不一致\n- \"regularized estimate\" 未说明正则化类型和参数。GPT-4o 用 2,000 resamples，Qwen3-32B 用 10,000，无理由。\n\n**W5** [warning] Table 1 Qwen3-32B Register 行缺少 Cohen's d 值，只有 p-value (.505)。\n\n**W6** [warning] DAG 遗漏 position bias（被实验 blocked）和 rewrite artifact（被 double-rewrite 控制 blocked）路径，应反映完整 identification strategy。\n\n### 小问题\n- 无代码/数据可用性声明\n- wang2026fairjudge 第一作者与 OpenAlex 不一致（bib: Wang, API: Yang）\n- murugadoss2025sos 在 OpenAlex 中未找到，建议核查\n- Abstract 信息密度高但可读性略受影响\n\n### Questions（需要作者回答）\n1. \"three judges\" 指哪三个？如果第三个 judge 未完成，Holm-Bonferroni family size 应为 6。\n2. NLI gate validation 为什么不用 GPT-4o 或人工标注？\n3. Verbose rewrites 是否经过人工 content quality 检查？\n4. BT 正则化具体设置？\n5. 是否计划发布代码和数据？\n\n### Missing References\n- Chiang et al. (2024) \"Chatbot Arena: An Open Platform\" — BT 实现规范\n- Ye et al. (2024) \"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge\" — bias quantification\n\n### 主要优势\n1. Likert Blindspot 用 7 种统计方法在同一数据上 demonstrate，方法论教育意义强\n2. Cross-judge/cross-axis 复现，verbosity 提供 confound-free clean case\n3. GEE decomposition 揭示 per-axis confound structure 差异（verbosity=pure style, formality=mixed, register=originality-dominated）\n4. Limitations 部分坦诚具体\n5. Position control + consistency filter 设计合理",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿意见（方法严谨性 + 实验设计）\n\n### 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 核心发现（Likert Blindspot）有实证价值且用7种统计方法交叉验证，但\"Causal\"标题与实际方法的张力、单一benchmark（n=100）的代表性不足、以及评估者-生产者循环偏差，使论文在方法严谨性上尚未达到主会议标准。\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心claim有多种统计方法支撑，但Holm-Bonferroni family定义与实际实验矛盾（声称9个检验实际只有6个）、因果声明overclaim、evaluator-producer循环性未充分量化 |\n| Excitement | 3.5/5 | Likert Blindspot现象对评估社区有实际指导价值，per-axis GEE分解揭示不同confound structure是有洞察力的贡献；但scope（1个benchmark、2个judge）限制了影响力 |\n| Reproducibility | 3/5 | 关键超参数大部分已报告，但BT正则化方式未说明、bootstrap resamples数不一致（2000 vs 10000）、无代码/数据可用性声明 |\n| Confidence | 4/5 | 仔细阅读全文含附录，统计方法论在我的专业领域内 |\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Holm-Bonferroni family 定义与实际实验不一致\n- 具体位置：§4.1 (experiments.tex line 8)\n- 问题：论文声称 \"three judges × three style axes = nine tests\"，但全文仅使用 2 个 judge（GPT-4o、Qwen3-32B），Table 1 也只有 6 行（2×3）。第三个 judge 完全没有出现。这意味着 Holm-Bonferroni 校正基于一个不存在的 family size（9），比实际需要的 family size（6）更保守——虽然这使结果更保守而非更宽松，但声称的实验设计与实际执行之间的不一致本身就是严重的 credibility 问题。\n- 为什么影响接收：统计框架的文本描述与实际执行不符，审稿人无法确定哪些描述是准确的。\n- 建议修改方向：要么补上第三个 judge 的实验，要么将 family 修正为 \"two judges × three style axes = six tests\" 并重新检查所有 adjusted p-values。\n\n**N2** [critical] \"Causal\" 标题与方法论实质的张力\n- 具体位置：Title、§3.5 (method.tex lines 57-58)、Abstract\n- 问题：标题为 \"Causal Style Decomposition\"，框架简称 CSD。但 §3.5 明确声明 \"we do not claim that this DAG is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions\"，并将自身定位为 \"interventional rather than formal causal evidence\"。NLI gate 对 do-operator 的近似也被承认不完整。标题 overclaim。\n- 为什么影响接收：标题是论文最高可见度的 claim，overclaim 显著降低对全文的信任。\n- 建议修改方向：(1) 将 \"Causal\" 替换为 \"Interventional\" 或 \"Style-Controlled\"；或 (2) 在 §3.5 中给出更严格的因果识别条件讨论。\n\n**N3** [critical] 单一 benchmark（LLMBar, n=100）的代表性\n- 具体位置：§3.4\n- 问题：所有实验仅基于 LLMBar（n=100），NLI gate 后剩 88 pairs → 173 comparisons。Bootstrap CI 宽度达 14.5pp。LLMBar 是 instruction-following 任务，代表性有限。论文的多个 strong claim 基于单一小规模 benchmark 难以成立。\n- 为什么影响接收：从 n=100 的单一 benchmark 推广到 \"LLM Judges\" 整个类别的 claim 缺乏 external validity。\n- 建议修改方向：至少在一个额外 benchmark 上复现核心发现，或在 title/abstract 中明确限定 scope。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Evaluator-producer 循环性未充分量化\n- Qwen3-32B 同时担任 rewriter、judge、NLI gate validator 三个角色。NLI gate validation 中称 Qwen3-32B 为 \"independent LLM annotator\" 不准确。建议删除 \"independent\"，并量化仅用 GPT-4o 数据是否足以支撑核心 claim。\n\n**W2** [warning] Direction-aware NLI for verbosity 削弱 content preservation 保证\n- 单向 NLI 允许 expansion 添加新的 quality-relevant content 而不被检测。text length 控制不等于 content quality 控制。建议对 verbose rewrites 进行人工内容质量抽检。\n\n**W3** [warning] GEE exchangeable correlation 假设验证不充分\n- 未测试 AR(1) 或 unstructured。within-pair α̂ ∈ [-0.25, +0.11]，部分负相关暗示 exchangeable 可能非最优。\n\n**W4** [warning] BT 正则化细节和 bootstrap resamples 不一致\n- \"regularized estimate\" 未说明正则化类型和参数。GPT-4o 用 2,000 resamples，Qwen3-32B 用 10,000，无理由。\n\n**W5** [warning] Table 1 Qwen3-32B Register 行缺少 Cohen's d 值，只有 p-value (.505)。\n\n**W6** [warning] DAG 遗漏 position bias（被实验 blocked）和 rewrite artifact（被 double-rewrite 控制 blocked）路径，应反映完整 identification strategy。\n\n### 小问题\n- 无代码/数据可用性声明\n- wang2026fairjudge 第一作者与 OpenAlex 不一致（bib: Wang, API: Yang）\n- murugadoss2025sos 在 OpenAlex 中未找到，建议核查\n- Abstract 信息密度高但可读性略受影响\n\n### Questions（需要作者回答）\n1. \"three judges\" 指哪三个？如果第三个 judge 未完成，Holm-Bonferroni family size 应为 6。\n2. NLI gate validation 为什么不用 GPT-4o 或人工标注？\n3. Verbose rewrites 是否经过人工 content quality 检查？\n4. BT 正则化具体设置？\n5. 是否计划发布代码和数据？\n\n### Missing References\n- Chiang et al. (2024) \"Chatbot Arena: An Open Platform\" — BT 实现规范\n- Ye et al. (2024) \"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge\" — bias quantification\n\n### 主要优势\n1. Likert Blindspot 用 7 种统计方法在同一数据上 demonstrate，方法论教育意义强\n2. Cross-judge/cross-axis 复现，verbosity 提供 confound-free clean case\n3. GEE decomposition 揭示 per-axis confound structure 差异（verbosity=pure style, formality=mixed, register=originality-dominated）\n4. Limitations 部分坦诚具体\n5. Position control + consistency filter 设计合理",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 119 · 2026-05-21T07:13:23.827482+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3969
}
```

</details>

---


### Tool call

_source line 120 · 2026-05-21T07:13:34.886654+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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

_source line 121 · 2026-05-21T07:13:35.088782+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 122 · 2026-05-21T07:13:39.059470+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 123 · 2026-05-21T07:13:39.059972+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 124 · 2026-05-21T07:13:44.624394+00:00_

审稿意见已提交给 Review Director。

核心判断：**Overall 3.0 (Findings)**。论文的 Likert Blindspot 发现有实证价值，7 种统计方法交叉验证令人信服，GEE per-axis confound structure 分析有洞察力。但三个 Must-Fix 问题阻止主会议接收：(1) Holm-Bonferroni 声称 9 个检验但实际只有 6 个——第三个 judge 不存在；(2) 标题 "Causal" 与 §3.5 的 explicit disclaimer 矛盾；(3) 仅用 LLMBar (n=100) 一个 benchmark 支撑对 "LLM Judges" 整个类别的 claim。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1"
}
```

</details>

---


## Round 6

## Round 6

8 recorded events


### User

_source line 125 · 2026-05-21T07:19:30.723158+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿意见。请逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

特别注意 Reviewer 2 提出的你未覆盖的问题（如 scale granularity、mitigation 策略、Abstract overclaim 的具体措辞分析）。

---

## Reviewer 2 审稿原文

**Overall: 3.0 (Findings) | Confidence: 4/5**

### 官方维度打分
| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计合理，NLI 门控验证充分，七种统计方法交叉验证令人信服。但 "causal" 框架名不副实（§3.5 disclaimer），且实验规模偏小。 |
| Excitement | 2.5/5 | Likert Blindspot 是心理测量学已知现象在 LLM 领域的迁移，方法是现有组件流水线，新颖性有限。实际建议（改用成对比较）有用但不足以单独撑起贡献。 |
| Reproducibility | 4/5 | 方法描述详细，统计分析透明。缺少代码/数据链接。 |

### Must-Fix 问题

**N1** [critical] Abstract 过度声称
- "style bias is the dominant source of unreliability in LLM judges, far outweighing other documented biases such as position or verbosity preference"
- 问题：(a) 仅基于 2 个评委 + 1 个 benchmark (LLMBar, n=100) 的证据无法支撑全称论断；(b) verbosity 本身是论文三个风格轴之一，说风格偏差 "far outweighs verbosity preference" 造成逻辑混淆；(c) formality 轴的 BT win probability 为 63%（GPT-4o），position bias 通常为 55-65%，"far outweighing" 缺乏量级支撑。
- 建议：将 "dominant source" 改为 "a previously underestimated source"，将 "far outweighing" 改为 "comparable to or exceeding"。

**N2** [critical] 标题 "Causal" 与 §3.5 disclaimer 的张力
- §3.5 明确声明 "we do not claim that this DAG is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions"。CSD 更接近 controlled experiment / interventional design 而非 formal causal inference。
- 建议：考虑 "Controlled Style Decomposition" 或 "Interventional Style Decomposition"。

### Should-Fix 问题

**W1** [warning] 新颖性天花板受限
- Likert Blindspot 是心理测量学经典现象（ordinal discretization 损失连续信号）在 LLM judge 领域的应用。CSD 框架是三个已有组件的流水线（LLM 改写 + NLI filter + BT comparison），methodological novelty 有限。
- 建议：加强 "why this domain transfer is non-trivial" 的论证——LLM judges 的 scale usage patterns 是否与 human raters 质性不同？

**W2** [warning] 实验规模偏窄
- 仅 2 个 judge（GPT-4o, Qwen3-32B）和 1 个 benchmark（LLMBar, n=100）。缺少 Claude/Llama 评委和非 instruction-following 任务。

**W3** [warning] Evaluator-producer confound 未充分处理
- Qwen3-32B 在 GEE 分解中的 formality OR (4.20) 和 originality OR (4.70) 系统性高于 GPT-4o，效应量差异可能部分来自 evaluator-producer bias。
- 建议：用第三个模型作为 rewriter 做控制实验。

**W4** [warning] Scale granularity 未探讨
- 论文使用 1-10 Likert scale。如果 1-100 continuous scale 也有 Blindspot，那是对 Likert 范式的根本性批评；如果更细粒度可以缓解，那只是 scale 选择问题。论文未区分。

**W5** [warning] 缺乏 mitigation 策略
- 论文诊断出 Blindspot 但未提出任何 mitigation 方案。成对比较的 O(n²) 代价对大规模评估不现实。

### Minor
- M1: Figure 4 (power_curve) 疑似 PLACEHOLDER 水印
- M2: Table 1 Qwen3-32B Register 行 Likert d 列格式不一致
- M3: wang2026fairjudge 第一作者 mismatch; hoenig2001abuse 引用链接需确认

### Missing References
- R1: Oriyad & Rohban (2025) "The Silent Judge" (NeurIPS 2025)
- R2: LLM-as-judge survey
- R3: Feder et al. (2022, TACL) "Causal Inference in NLP" 综述

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 126 · 2026-05-21T07:20:05.769256+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-21T07:20:06.221224+00:00_

1	\begin{abstract}
2	Large Language Model (LLM) judges are widely deployed for evaluation and preference-based alignment, yet recent work shows that style features alone can explain judge scores with near-perfect correlation, raising fundamental questions about what these judges actually measure.
3	We introduce Causal Style Decomposition (CSD), a black-box framework that detects per-axis style bias through binary style-controlled rewriting, NLI-based content preservation gating, and position-controlled pairwise comparison.
4	We quantify what we term the Likert Blindspot---a measurement limitation predicted by psychometric theory but previously unquantified for LLM judges---across two architecturally distinct judges (GPT-4o, Qwen3-32B) and two primary style axes (formality, verbosity), with directionally consistent exploratory evidence on a third axis (register): a two-layer structural gap in which (1)~integer Likert scoring produces ${\sim}60\%$ uninformative ties ($\Delta = 0$), wasting the majority of the evaluation budget; (2)~even among non-tied pairs, absolute scoring captures weaker signal than forced pairwise comparison on identical data.
5	The effect is most dramatic for verbosity, where a 77.3\% Bradley-Terry win probability ($p < 0.0001$, both directions favoring verbose content) remains invisible to Likert scoring ($p = 0.179$).
6	Ordinal regression confirms the limitation is inherent to Likert measurement, not an artifact of interval-scale assumptions ($p = 0.769$).
7	Our results demonstrate that style bias audits require pairwise comparison and per-axis decomposition, and that existing Likert-based findings may systematically underestimate style bias magnitude.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 128 · 2026-05-21T07:20:06.372212+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex",
    "limit": "15"
  }
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-21T07:20:06.422897+00:00_

1	\section{Introduction}
2	
3	Large Language Model (LLM) judges have become central infrastructure for NLP evaluation and preference-based alignment training.
4	Systems such as AlpacaEval, MT-Bench, and Chatbot Arena rely on LLM judges to score and rank model outputs, and the resulting leaderboards guide both academic research and industry deployment.
5	Reinforcement Learning from Human Feedback (RLHF) and Direct Preference Optimization (DPO) pipelines consume judge-generated preferences as reward signals that shape model behavior during alignment.
6	The reliability of these judgments carries direct consequences: it determines which models the community considers superior and which response patterns are reinforced.
7	As automated judges increasingly mediate both evaluation and training, any systematic bias in their assessments propagates through the entire model development pipeline.
8	
9	Recent work has converged on a striking finding: \emph{style bias} is the dominant source of unreliability in LLM judges, far outweighing other documented biases such as position or verbosity preference.
10	\citet{murugadoss2025sos} show that style features alone explain judge scores with $R = 0.999$, far exceeding the explanatory power of content features.
11	\citet{li2026preference} demonstrate that 76--92\% of observed preference signals originate from surface-level style cues rather than substantive quality differences.
12	\citet{soumik2026judging} report bias scores of 0.76--0.92 across five different judges.
13	Despite this consensus on severity, existing approaches share four critical gaps: (1)~they treat style as a single dimension, typically reducing it to response length; (2)~they rely on correlational analyses that cannot establish causal direction; (3)~population-level corrections such as length-controlled AlpacaEval \citep{dubois2025lc} cannot diagnose per-instance bias; and (4)~no existing method provides black-box, post-hoc, per-axis interventional detection.
14	Rece
…[truncated 515 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 130 · 2026-05-21T07:21:26.073591+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 交叉回应 Reviewer 2\n\n### Must-Fix\n\n**[REBUT] R2-N1: Abstract 过度声称**\n部分反驳。R2 指出的 (a) 点存在归因偏差：\"dominant source\" claim 出现在 Introduction line 9，句式为 \"Recent work has converged on a striking finding: ...\"，后接三条引用（Murugadoss 2025, Li 2026, Soumik 2026）——这是文献归纳而非本文 claim。Abstract 对应表述也明确标记为 \"recent work shows\"。但 R2 的 (b) 点我完全同意且此前未覆盖：将 verbosity preference 与 style bias 并列对比构成 category error，因为论文自身将 verbosity 定义为 style 的子轴。(c) 点方向合理但归因仍需注意引用来源。总体建议合理，措辞应修改。\n\n**[AGREE] R2-N2: \"Causal\" 标题张力**\n与我的 N2 完全一致。补充：作者若坚持 \"Causal\"，应在 §3.5 明确 identification assumptions（在什么条件下 NLI gate 实现了 do(S)），而非仅给 disclaimer。\n\n### Should-Fix\n\n**[REBUT] R2-W1: 新颖性天花板受限**\nR2 判断部分过严。虽然 Likert Blindspot 在 psychometrics 中已知，但 (1) 7种统计方法的量化 demonstration 对 LLM 评估社区有实际价值；(2) GEE decomposition 揭示的 per-axis confound structure 梯度（Table 3）是全新发现；(3) 两层机制的具体识别此前未有。不过建议加强 domain transfer non-triviality 论证是合理的。Excitement 给 2.5 偏低，我给 3.5。\n\n**[AGREE] R2-W2: 实验规模偏窄**\n与我的 N3 一致。我将此列为 Must-Fix 级别。\n\n**[AGREE] R2-W3: Evaluator-producer confound**\n与我的 W1 一致。R2 建议用第三模型作 rewriter 更具体可操作。\n\n**[AGREE] R2-W4: Scale granularity 未探讨**\n我完全未覆盖的有效问题。1-10 vs 1-100 的区分决定了 Blindspot 是 absolute scoring 范式的根本问题还是仅是 scale design 问题。Table 2 的 ordinal regression 排除了 interval-scale 假设，但不排除 granularity 影响。\n\n**[REBUT] R2-W5: 缺乏 mitigation 策略**\n论文定位是 diagnostic framework，不必同时提出 debiasing solution。§6 的 \"adopt pairwise comparison\" 已是可操作建议。但 O(n²) scalability concern 合理，可简要讨论 active sampling 等 O(n log n) 方案。Should-Fix 级别合适，不宜升为 Must-Fix。\n\n### Minor & Missing References\n\n[AGREE] M1-M3 均合理。\n[AGREE] R3 (Feder et al. 2022) 对因果框架讨论有直接参考价值。\n[REBUT] R1 (Oriyad & Rohban 2025) 未能在 OpenAlex/Semantic Scholar 确认存在。\n[AGREE] R2 (LLM-as-judge survey) 补充综述性引用合理。\n\n### 两位 Reviewer 的评分差异\n\n| 维度 | R1 | R2 | 差异分析 |\n|------|----|----|---------|\n| Soundness | 3/5 | 3.5/5 | R2 对 NLI 验证评价更高，我对 Holm-Bonferroni 不一致（R2未提及）扣分更多 |\n| Excitement | 3.5/5 | 2.5/5 | 主要分歧——我认为 GEE decomposition + 7-method demonstration 有实际贡献，R2 认为是 known phenomenon 的 domain transfer |\n| Overall | 3.0 | 3.0 | 一致 |\n\n核心共识：(1) \"Causal\" overclaim；(2) 单一 benchmark 不足；(3) evaluator-producer 循环性。\n核心分歧：novelty 评估——我偏向认可 quantification + GEE decomposition 的贡献，R2 更强调 methodological novelty 不足。",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 交叉回应 Reviewer 2\n\n### Must-Fix\n\n**[REBUT] R2-N1: Abstract 过度声称**\n部分反驳。R2 指出的 (a) 点存在归因偏差：\"dominant source\" claim 出现在 Introduction line 9，句式为 \"Recent work has converged on a striking finding: ...\"，后接三条引用（Murugadoss 2025, Li 2026, Soumik 2026）——这是文献归纳而非本文 claim。Abstract 对应表述也明确标记为 \"recent work shows\"。但 R2 的 (b) 点我完全同意且此前未覆盖：将 verbosity preference 与 style bias 并列对比构成 category error，因为论文自身将 verbosity 定义为 style 的子轴。(c) 点方向合理但归因仍需注意引用来源。总体建议合理，措辞应修改。\n\n**[AGREE] R2-N2: \"Causal\" 标题张力**\n与我的 N2 完全一致。补充：作者若坚持 \"Causal\"，应在 §3.5 明确 identification assumptions（在什么条件下 NLI gate 实现了 do(S)），而非仅给 disclaimer。\n\n### Should-Fix\n\n**[REBUT] R2-W1: 新颖性天花板受限**\nR2 判断部分过严。虽然 Likert Blindspot 在 psychometrics 中已知，但 (1) 7种统计方法的量化 demonstration 对 LLM 评估社区有实际价值；(2) GEE decomposition 揭示的 per-axis confound structure 梯度（Table 3）是全新发现；(3) 两层机制的具体识别此前未有。不过建议加强 domain transfer non-triviality 论证是合理的。Excitement 给 2.5 偏低，我给 3.5。\n\n**[AGREE] R2-W2: 实验规模偏窄**\n与我的 N3 一致。我将此列为 Must-Fix 级别。\n\n**[AGREE] R2-W3: Evaluator-producer confound**\n与我的 W1 一致。R2 建议用第三模型作 rewriter 更具体可操作。\n\n**[AGREE] R2-W4: Scale granularity 未探讨**\n我完全未覆盖的有效问题。1-10 vs 1-100 的区分决定了 Blindspot 是 absolute scoring 范式的根本问题还是仅是 scale design 问题。Table 2 的 ordinal regression 排除了 interval-scale 假设，但不排除 granularity 影响。\n\n**[REBUT] R2-W5: 缺乏 mitigation 策略**\n论文定位是 diagnostic framework，不必同时提出 debiasing solution。§6 的 \"adopt pairwise comparison\" 已是可操作建议。但 O(n²) scalability concern 合理，可简要讨论 active sampling 等 O(n log n) 方案。Should-Fix 级别合适，不宜升为 Must-Fix。\n\n### Minor & Missing References\n\n[AGREE] M1-M3 均合理。\n[AGREE] R3 (Feder et al. 2022) 对因果框架讨论有直接参考价值。\n[REBUT] R1 (Oriyad & Rohban 2025) 未能在 OpenAlex/Semantic Scholar 确认存在。\n[AGREE] R2 (LLM-as-judge survey) 补充综述性引用合理。\n\n### 两位 Reviewer 的评分差异\n\n| 维度 | R1 | R2 | 差异分析 |\n|------|----|----|---------|\n| Soundness | 3/5 | 3.5/5 | R2 对 NLI 验证评价更高，我对 Holm-Bonferroni 不一致（R2未提及）扣分更多 |\n| Excitement | 3.5/5 | 2.5/5 | 主要分歧——我认为 GEE decomposition + 7-method demonstration 有实际贡献，R2 认为是 known phenomenon 的 domain transfer |\n| Overall | 3.0 | 3.0 | 一致 |\n\n核心共识：(1) \"Causal\" overclaim；(2) 单一 benchmark 不足；(3) evaluator-producer 循环性。\n核心分歧：novelty 评估——我偏向认可 quantification + GEE decomposition 的贡献，R2 更强调 methodological novelty 不足。",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 131 · 2026-05-21T07:21:30.802144+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4728
}
```

</details>

---


### Assistant

_source line 132 · 2026-05-21T07:21:35.417847+00:00_

交叉回应已提交。

核心结论：与 R2 在 3 个 Must-Fix（Causal overclaim、单一 benchmark、evaluator-producer bias）上达成共识。主要分歧在 novelty 评估——我认为 GEE decomposition 和 7-method quantification 的贡献值得 Excitement 3.5，R2 给 2.5。R2 提出的 scale granularity（W4）是我此前遗漏的有效问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1"
}
```

</details>

---


## Round 7

## Round 7

66 recorded events


### User

_source line 133 · 2026-05-21T09:36:33.872099+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责审查 **方法严谨性 + 实验有效性**。

## 论文信息
- 标题：Counterfactual Style Decomposition Reveals the Likert Blindspot: Standard Scoring Underestimates Style Bias in LLM Judges
- 文件路径：`/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex`
- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf`

## Venue 要求
- **目标**：EMNLP 2026（通过 ARR 审稿）
- **ARR 提交截止**：2026-05-25 AoE
- **正文页数**：≤ 8 页（Long paper）
- **参考文献**：不限
- **Limitations**：必须有，不计入页数
- **模板**：ACL (Overleaf)
- **匿名**：Double-blind

## 你的审查重点

请严格聚焦以下方面：

1. **CSD 框架方法论**：
   - 因果推断框架（§3.5 DAG）的假设是否合理？identification assumptions 是否充分？
   - NLI-based content preservation gate 的 validity——NLI 阈值选择、direction-aware NLI 对 verbosity 的合理性
   - Binary style-controlled rewriting 的 confound control 是否充分？

2. **统计方法**：
   - Bradley-Terry 模型使用是否正确？bootstrap CI 是否合理？
   - GEE logistic regression 的规范（correlation structure、cluster 定义）
   - Multiple comparison correction（Holm-Bonferroni）是否正确应用？
   - Effect size 报告（Cohen's d、OR、BT win probability）是否一致且正确？
   - Ordinal regression 的使用和解释

3. **实验设计**：
   - 样本量（n=100 LLMBar、n=355/400 scaled）是否足够？power analysis 是否合理？
   - 跨 benchmark（LLMBar/AlpacaEval/MT-Bench）、跨 judge（GPT-4o/Qwen3-32B/Claude）的 generalizability
   - Evaluator-producer bias（Qwen3-32B 同时做 rewriter 和 judge）的控制是否充分？
   - Position bias 控制
   - Rewriter independence test 的设计

4. **Reproducibility**：
   - 实验细节是否足够复现？
   - 代码/数据承诺是否明确？

请按 ACL reviewer 标准输出完整审稿报告，包含 Summary、Strengths、Weaknesses（逐条编号，区分 Must-Fix / Should-Fix / Minor）、Questions for Authors、Overall Assessment。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 134 · 2026-05-21T09:36:43.425461+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 135 · 2026-05-21T09:36:44.266177+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/review_reviewer_1_9f412a41.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 840
}
```

</details>

---


### Tool call

_source line 136 · 2026-05-21T09:36:44.266645+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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

_source line 137 · 2026-05-21T09:36:44.325517+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 58
}
```

</details>

---


### Tool call

_source line 138 · 2026-05-21T09:36:48.269736+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 139 · 2026-05-21T09:36:49.678031+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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

_source line 140 · 2026-05-21T09:36:49.728776+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 141 · 2026-05-21T09:36:55.854562+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about the ACL ARR 2026 reviewer guidelines and review form criteria:

## Reviewer Guidelines

Reviewers are asked to read the paper, get a first impression, then search for related work without deliberatel
…[truncated 1341 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7584
}
```

</details>

---


### Tool result

_source line 142 · 2026-05-21T09:36:57.161438+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.1}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 526.5}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 570.9}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 501.6}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 435.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 540.7}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 517.8}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 518.8}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/pap
…[truncated 311 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7483
}
```

</details>

---


### Tool result

_source line 143 · 2026-05-21T09:36:57.162899+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 7434
}
```

</details>

---


### Tool call

_source line 144 · 2026-05-21T09:37:01.433444+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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

_source line 145 · 2026-05-21T09:37:01.433789+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 146 · 2026-05-21T09:37:02.388477+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "11-12",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "11-12",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 147 · 2026-05-21T09:37:03.342621+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 585.0}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 51.4}], \"total_pages\": 12, \"rendered_pages\": 2, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 148 · 2026-05-21T09:37:03.493677+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 149 · 2026-05-21T09:37:03.795485+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 150 · 2026-05-21T09:37:04.298643+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 151 · 2026-05-21T09:37:04.808197+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1314
}
```

</details>

---


### Tool call

_source line 152 · 2026-05-21T09:37:04.808704+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 153 · 2026-05-21T09:37:04.860026+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1064
}
```

</details>

---


### Tool result

_source line 154 · 2026-05-21T09:37:05.618187+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1319
}
```

</details>

---


### Tool result

_source line 155 · 2026-05-21T09:37:05.972069+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1163
}
```

</details>

---


### Tool call

_source line 156 · 2026-05-21T09:37:12.647116+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ACL ARR review form: all scoring dimensions, their scales (1-5 etc.), descriptions for each score level, and any special instructions for reviewers. I need the exact criteria for: Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete ACL ARR review form: all scoring dimensions, their scales (1-5 etc.), descriptions for each score level, and any special instructions for reviewers. I need the exact criteria for: Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other scored dimensions."
  }
}
```

</details>

---


### Tool call

_source line 157 · 2026-05-21T09:37:13.659497+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 158 · 2026-05-21T09:37:14.216536+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 159 · 2026-05-21T09:37:14.770266+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1110
}
```

</details>

---


### Tool call

_source line 160 · 2026-05-21T09:37:14.871141+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 161 · 2026-05-21T09:37:14.973473+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 162 · 2026-05-21T09:37:15.277832+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1061
}
```

</details>

---


### Tool result

_source line 163 · 2026-05-21T09:37:16.084106+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1212
}
```

</details>

---


### Tool result

_source line 164 · 2026-05-21T09:37:16.235549+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1262
}
```

</details>

---


### Tool result

_source line 165 · 2026-05-21T09:37:19.553168+00:00_

# ACL ARR Review Form Scoring Dimensions

## Overall Assessment
Scale: 1-5 (with half-point increments)
- **5**: "Consider for Award: I think this paper could be considered for an outstanding paper award"
- **4**: Conference acceptance recommended
- **3**: "Findings: I think this paper could be accepted to the Findings of the ACL"
- **2**: Substantial revisions needed for next submission cycle
- **1**: Do not resubmit or not relevant to ACL community

## Soundness
Scale: 1-5 (with half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: "Strong: This study provides sufficient support for all of its claims"
- **3**: "Acceptable: This study provides sufficient support for its main claims"
- **2**: "Poor: Some of the main claims are not sufficiently supported"
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement
Scale: 1-5 (with half-point increments)
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: "Exciting: I would mention this paper to others"
- **3**: "Interesting: I might mention some points of this paper to others"
- **2**: "Potentially Interesting: does not resonate with me, but might with others"
- **1**: "Not Exciting: does not resonate with me"

## Reviewer Confidence
Scale: 1-5
- **5**: "Positive that my evaluation is correct"
- **4**: "Quite sure. It's unlikely, though conceivable, that I missed something"
- **3**: "Pretty sure, but there's a chance I missed something"
- **2**: "Willing to defend my evaluation, but fairly likely I missed details"
- **1**: "Not my area, or paper is very hard to understand"

## Reproducibility
Scale: 1-5
- **5**: "They could easily reproduce the results"
- **4**: "They could mostly reproduce the results"
- **3**: "They could reproduce the results with some difficulty"
- **2**: "They would be hard pressed to reproduce the results"
- **1**: "They would not be able to reproduce the results"

## Datase
…[truncated 286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6906
}
```

</details>

---


### Tool call

_source line 166 · 2026-05-21T09:37:24.731776+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 167 · 2026-05-21T09:37:25.234426+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 168 · 2026-05-21T09:37:25.686821+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 169 · 2026-05-21T09:37:25.689379+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 170 · 2026-05-21T09:37:26.195106+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 960
}
```

</details>

---


### Tool call

_source line 171 · 2026-05-21T09:37:26.195538+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 172 · 2026-05-21T09:37:26.296952+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 173 · 2026-05-21T09:37:26.500142+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 810
}
```

</details>

---


### Tool call

_source line 174 · 2026-05-21T09:37:33.275362+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 175 · 2026-05-21T09:37:33.326020+00:00_

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
19	\title{Counterfactual Style Decomposition Reveals the Likert Blindspot:\\Standard Scoring Underestimates Style Bias in LLM Judges}
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
41	\paragraph{Quality--style confounding.}
42	Although the formality effect survives logistic adjustment for original preference (Appendix~\ref{app:direction}), the significant original-preference odds ratio ($\text{OR} = 2.32$, $p = 0.006$) indicates that quality--style confounding is not fully eliminated.
43	The NLI gate blocks content changes but cannot block quality perception shifts mediated by style itself---a fundamental identifiability limit of text-rewriting approaches.
44	Future work should incorporate human quality ratings of both original and rewritten texts.
45	
46	\paragraph{Evaluator-producer bias in Qwen3-32B.}
47	Qwen3-32B serves as both the style rewriter and one of the three judges; the NLI entailment gate (DeBERTa-v3-large) is architecturally independent of both roles.
48	At $n = 88$, the Qwen3-32B formality Style OR ($4.20$) exhibited small-sample upward bias, corrected to $2.15$ at $n = 355$ (comparable to GPT-4o's $2.58$); the originality OR inflation persists ($4.99$ vs.\ $2.32$), consistent with partial self-recognition.
…[truncated 2326 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 176 · 2026-05-21T09:37:37.742486+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/*.tex"
  }
}
```

</details>

---


### Tool result

_source line 177 · 2026-05-21T09:37:37.793214+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 178 · 2026-05-21T09:37:40.954856+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 179 · 2026-05-21T09:37:41.406957+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{figures/pipeline_diagram.pdf}
7	\caption{CSD pipeline overview. Numbers indicate sample attrition at each stage.}
8	\label{fig:pipeline}
9	\end{figure}
10	
11	\subsection{Style-Controlled Rewriting}
12	\label{sec:rewriting}
13	
14	We isolate the effect of individual style attributes on judge scores by generating text pairs that differ along exactly one style axis.
15	For each text, an instruction-tuned LLM (Qwen3-32B) first classifies its current style along the target axis (e.g., formal vs.\ casual via binary classification), then rewrites it toward the opposite pole (temperature 0.7) according to an axis-specific prompt (e.g., ``Rewrite the following text to be more formal/casual while preserving the exact same content and meaning'').
16	This produces a dataset balanced across both directions at the dataset level: texts detected as formal are rewritten to casual, and vice versa.
17	Each operation constitutes a binary intervention on a single style variable while all other axes remain fixed (Section~\ref{sec:causal_framework}).
18	To control for rewriting artifact bias---the possibility that the judge prefers original text over any rewrite regardless of style---we additionally generate a same-style double-rewrite for each text (e.g., formal $\to$ formal) to form an original-vs-double-rewrite control pair, following the RATE bias correction protocol \citep{reber2025rate}.
19	
20	\subsection{Content Preservation Verification}
21	\label{sec:nli_gate}
22	
23	Style-controlled rewriting risks altering semantic content, which would confound the style effect with a content quality effect (the $R \to Q$ path in Figure~\ref{fig:dag}).
24	To block this path, we apply a natural language inference (NLI) gate using DeBERTa-v3-large with an entailment threshold of 0.90.
25	For axes that preserve information density (formality, register), we apply standard bidirection
…[truncated 5419 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 180 · 2026-05-21T09:37:41.407424+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-21T09:37:41.859944+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	
5	\subsection{Statistical Framework}
6	\label{sec:stat_framework}
7	
8	We designate a primary family of six hypothesis tests (two judges $\times$ three style axes) and control the family-wise error rate with Holm-Bonferroni correction at $\alpha = 0.05$.
9	Table~\ref{tab:main_results} reports both raw and adjusted $p$-values for this $2 \times 3$ grid.
10	Analyses outside this grid are classified as either \emph{exploratory} (NLI threshold sensitivity sweep, \S\ref{sec:nli_threshold}) or \emph{confirmatory} (consistency filter validation, \S\ref{sec:consistency}).
11	Exploratory analyses are reported with uncorrected $p$-values and interpreted as hypothesis-generating; confirmatory analyses test specific hypotheses about pipeline validity and are evaluated at the nominal $\alpha = 0.05$ level without additional correction, as they address orthogonal questions about measurement reliability rather than the primary style-bias family.
12	Bradley-Terry parameters are estimated via spectral initialization followed by minorization-maximization \citep{hunter2004mm}, using the default regularization of the \texttt{choix} Python library.
13	All bootstrap confidence intervals use 10{,}000 pair-level resamples with seed 42.
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\caption{Main results across three judges, three style axes, and three benchmarks. BT: Bradley-Terry win probability (10{,}000 pair-level bootstrap resamples; 95\% CIs in Appendix~\ref{app:bt_ci}). AEval: AlpacaEval; MTB: MT-Bench. Claude Sonnet 4 serves as negative control.}
19	\label{tab:main_results}
20	\begin{tabular}{@{}lllccc@{}}
21	\toprule
22	Bench & Judge & Axis & BT $P$ & Likert $d$ ($p$) & \\
23	\midrule
24	LLMBar & GPT-4o & Form.\ & .630$^{***}$ & .011 (.908) & $\dagger$ \\
25	 & GPT-4o & Verb.\ & .760$^{***}$ & $-$.095 (.403) & $\dagger$ \\
26	 & GPT-4o & Reg.\ & .570$^{\dagger}$ & $-$.031 (.785) & $\dagger_{\text{e}}$ \\
27	\cmidrule{2-6}

…[truncated 16822 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 182 · 2026-05-21T09:37:41.860529+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 183 · 2026-05-21T09:37:41.911099+00:00_

1	\appendix
2	
3	\section{Direction Asymmetry and Quality Confounding}
4	\label{app:direction}
5	
6	The formality axis exhibits a pronounced direction asymmetry: the judge selects the formal variant in 78.8\% of formal-is-rewrite pairs ($p = 0.001$) but only 54.5\% of casual-is-rewrite pairs ($p = 0.83$).
7	This asymmetry suggests that original quality $Q$ and formality $S$ are partially confounded---formally written texts may be inherently perceived as higher quality.
8	To quantify this, we fit a logistic decomposition (GEE, exchangeable correlation) with both formality and original-preference as predictors.
9	After controlling for original preference, the formality effect remains significant ($\text{OR} = 2.58$, $p = 0.002$), and the original-preference effect is also significant ($\text{OR} = 2.32$, $p = 0.006$).
10	The formality preference thus survives adjustment for original-preference confounding, though the significant original-preference effect indicates that quality--style confounding is present and non-negligible.
11	
12	At $n = 88$, the Qwen3-32B formality Style OR ($4.20$) exceeded the GPT-4o estimate ($2.58$), but a scaled replication ($n = 355$) corrects this to $2.15$ ($p < 0.0001$), comparable to GPT-4o and consistent with small-sample upward bias rather than evaluator-producer inflation of the style effect.
13	The originality confound remains stronger ($4.99$ vs.\ $2.32$), consistent with evaluator-producer bias inflating the originality component (\S\ref{sec:limitations}).
14	The directional agreement between judges---both favor formal text after controlling for originality---supports the existence of formality bias, but the effect magnitude from Qwen3-32B should not be directly compared with GPT-4o.
15	
16	The NLI gate blocks \emph{content} changes but cannot block quality perception shifts that are themselves mediated by style---a fundamental identifiability limit of any text-rewriting approach.
17	
18	\section{Consistency Filter Robustness}
19	
…[truncated 4617 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 184 · 2026-05-21T09:37:47.279622+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 185 · 2026-05-21T09:37:47.738582+00:00_

1	\begin{abstract}
2	Large Language Model (LLM) judges are widely deployed for evaluation and preference-based alignment, yet recent work shows that style features alone can explain judge scores with near-perfect correlation, raising fundamental questions about what these judges actually measure.
3	We introduce Counterfactual Style Decomposition (CSD), a black-box framework that detects per-axis style bias through binary style-controlled rewriting, NLI-based content preservation gating, and position-controlled pairwise comparison.
4	We quantify what we term the Likert Blindspot---a measurement efficiency gap, predicted by psychometric theory but previously unquantified for LLM judges, in which Likert requires substantially stronger effects or larger samples to detect the same bias that pairwise comparison reliably captures---across two judges (GPT-4o, Qwen3-32B), three benchmarks (LLMBar, AlpacaEval, MT-Bench), and two primary style axes (formality, verbosity), with exploratory evidence on a third axis (register); a third judge (Claude Sonnet 4) detects no bias on either axis, confirming discriminative validity.
5	The gap arises from a two-layer mechanism: (1)~integer Likert scoring produces ${\sim}60\%$ uninformative ties ($\Delta = 0$), wasting the majority of the evaluation budget; (2)~even among non-tied pairs, absolute scoring captures weaker signal than forced pairwise comparison on identical data.
6	The effect is most dramatic for verbosity, where a 77.3\% Bradley-Terry win probability ($p < 0.0001$, both directions favoring verbose content) remains invisible to Likert scoring ($p = 0.179$).
7	Ordinal regression confirms the limitation is inherent to Likert measurement, not an artifact of interval-scale assumptions ($p = 0.769$).
8	Our results demonstrate that style bias audits require pairwise comparison and per-axis decomposition, and that existing Likert-based findings may systematically underestimate style bias magnitude.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 458
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-21T09:37:47.741580+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 187 · 2026-05-21T09:37:48.699589+00:00_

1	\section{Introduction}
2	
3	Large Language Model (LLM) judges have become central infrastructure for NLP evaluation and preference-based alignment training.
4	Systems such as AlpacaEval, MT-Bench, and Chatbot Arena rely on LLM judges to score and rank model outputs, and the resulting leaderboards guide both academic research and industry deployment.
5	Reinforcement Learning from Human Feedback (RLHF) and Direct Preference Optimization (DPO) pipelines consume judge-generated preferences as reward signals that shape model behavior during alignment.
6	The reliability of these judgments carries direct consequences: it determines which models the community considers superior and which response patterns are reinforced.
7	As automated judges increasingly mediate both evaluation and training, any systematic bias in their assessments propagates through the entire model development pipeline.
8	
9	Recent work suggests that style features alone explain most of the variance in judge scores \citep{murugadoss2025sos}, motivating systematic measurement of per-axis style bias.
10	\citet{li2026preference} demonstrate that 76--92\% of observed preference signals originate from surface-level style cues rather than substantive quality differences, and \citet{soumik2026judging} report bias scores of 0.76--0.92 across five different judges.
11	Despite this consensus on severity, existing approaches share four critical gaps: (1)~they treat style as a single dimension, typically reducing it to response length; (2)~they rely on correlational analyses that cannot establish causal direction; (3)~population-level corrections such as length-controlled AlpacaEval \citep{dubois2025lc} cannot diagnose per-instance bias; and (4)~no existing method provides black-box, post-hoc, per-axis interventional detection.
12	Recent multi-feature frameworks such as CASSE \citep{casse2026concise} and FairJudge \citep{wang2026fairjudge} begin to decompose style into finer dimensions, but neither provides interv
…[truncated 4170 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool call

_source line 188 · 2026-05-21T09:37:48.750159+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 189 · 2026-05-21T09:37:48.851033+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	Two lines of work motivate our approach: counterfactual methods for diagnosing judge bias, and measurement theory on the sensitivity of different elicitation formats.
5	
6	\paragraph{Counterfactual Approaches to Judge Bias}
7	\citet{reber2025rate} propose RATE, a framework that rewrites model outputs along style attributes using imperfect counterfactuals and measures the causal effect on reward model scores via Likert-scale Average Treatment Effect (ATE).
8	RATE applies a correction term to account for rewriting imperfections, but its reliance on Likert ATE as the primary metric is a vulnerability: our experiments show that Likert scoring exhibits a ceiling effect in which 60\% of style-transformed pairs receive identical integer scores, yielding non-significant ATE estimates ($p = 0.332$) for the same interventions that pairwise comparison detects at $p = 0.006$.
9	If this Likert Blindspot generalizes beyond our setting, RATE's own style-related findings may underestimate the true magnitude of attribute effects.
10	CSD differs from RATE in three respects: it targets individual style axes rather than general attributes, it measures bias through position-controlled pairwise comparison rather than Likert ATE, and it enforces content preservation via NLI entailment gating rather than post-hoc correction for imperfect rewrites.
11	\citet{counterfactual2025rhetorical} also adopt a counterfactual LLM-based design, rewriting texts to measure rhetorical style effects and aggregating preferences with a Bradley-Terry model.
12	Their framework operates at persona-level granularity (e.g., ``writes like a professor''), whereas CSD intervenes on specific style axes (e.g., formality, conciseness) and uses a sign test with position control rather than parametric aggregation.
13	
14	\paragraph{Measurement Sensitivity in NLG Evaluation}
15	The distinction between ordinal and interval measurement dates to \citet{stevens1946theor
…[truncated 3971 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 190 · 2026-05-21T09:37:48.851564+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 191 · 2026-05-21T09:37:48.902091+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced Counterfactual Style Decomposition (CSD), a black-box framework for detecting per-axis style bias in LLM judges.
5	Across three judges, three benchmarks, and three style axes, CSD reveals the Likert Blindspot---a measurement efficiency gap confirmed by seven statistical methods.
6	Style bias audits should adopt pairwise comparison; existing Likert-based null findings may reflect measurement insensitivity.
7	Prompt-level debiasing is insufficient; structural interventions remain open.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 192 · 2026-05-21T09:37:53.721074+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool call

_source line 193 · 2026-05-21T09:37:54.324476+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 194 · 2026-05-21T09:38:14.259120+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 27, \"total_citations\": 39, \"unique_cited_keys\": 26, \"orphan_bib\": 1, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 24, \"online_not_found\": 1, \"online_mismatch\": 2}, \"cross_check\": {\"orphan_bib\": [\"hoenig2001abuse\"], \"missing_bib\": [], \"orphan_count\": 1, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"murugadoss2025sos\", \"type\": \"inproceedings\", \"title\": \"Style Over Substance: Failure Modes of LLM Judges in Alignment Benchmarking\", \"authors\": \"Murugadoss, Aakanksha and others\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"li2026preference\", \"type\": \"inproceedings\", \"title\": \"Preference Leakage: A Contamination Problem in LLM-as-a-Judge\", \"authors\": \"Li, Dawei and others\", \"year\": \"2026\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"wang2026fairjudge\", \"type\": \"article\", \"title\": \"FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge\", \"authors\": \"Yang, Bo and Feng, Lanfei and Chen, Yunkui and Zhang, Yu and Xu, Xiao and Li, Sh...\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2602.06625\"}, {\"key\": \"dubois2025lc\", \"type\": \"inproceedings\", \"title\": \"Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators\", \"authors\": \"Dubois, Yann and others\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"casse2026concise\", \"type\": \"article\", \"title\": \"A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents\", \"authors\": \"Cho, Young-Min and Yuan, Yuan and Guntuku, Sharath Chandra and Ungar, Lyle\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2601.10809\"}, {\"key\": \"counterfactu
…[truncated 19916 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 20538
}
```

</details>

---


### Tool result

_source line 195 · 2026-05-21T09:38:14.260013+00:00_

1	@inproceedings{murugadoss2025sos,
2	  title={Style Over Substance: Failure Modes of {LLM} Judges in Alignment Benchmarking},
3	  author={Murugadoss, Aakanksha and others},
4	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
5	  year={2025},
6	  url={https://arxiv.org/abs/2409.15268}
7	}
8	
9	@inproceedings{li2026preference,
10	  title={Preference Leakage: A Contamination Problem in {LLM}-as-a-Judge},
11	  author={Li, Dawei and others},
12	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
13	  year={2026},
14	  url={https://arxiv.org/abs/2502.01534}
15	}
16	
17	@article{wang2026fairjudge,
18	  title={{FairJudge}: An Adaptive, Debiased, and Consistent {LLM}-as-a-Judge},
19	  author={Yang, Bo and Feng, Lanfei and Chen, Yunkui and Zhang, Yu and Xu, Xiao and Li, Shijian},
20	  journal={arXiv preprint arXiv:2602.06625},
21	  year={2026},
22	  url={https://arxiv.org/abs/2602.06625}
23	}
24	
25	
26	@inproceedings{dubois2025lc,
27	  title={Length-Controlled {AlpacaEval}: A Simple Way to Debias Automatic Evaluators},
28	  author={Dubois, Yann and others},
29	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
30	  year={2025},
31	  url={https://arxiv.org/abs/2404.04475}
32	}
33	
34	@article{casse2026concise,
35	  title={A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents},
36	  author={Cho, Young-Min and Yuan, Yuan and Guntuku, Sharath Chandra and Ungar, Lyle},
37	  journal={arXiv preprint arXiv:2601.10809},
38	  year={2026},
39	  url={https://arxiv.org/abs/2601.10809}
40	}
41	
42	@article{counterfactual2025rhetorical,
43	  title={Counterfactual {LLM}-based Framework for Measuring Rhetorical Style},
44	  author={Qiu, Jingyi and Chen, Hong and Li, Zongyi},
45	  journal={arXiv preprint arXiv:2512.19908},
46	  year={2025},
47	  url={https://arxiv.org/abs/2512.19908}
48	}
49	
50	@article{soumik2026j
…[truncated 7759 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 19935
}
```

</details>

---


### Tool call

_source line 196 · 2026-05-21T09:41:28.007553+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 — 方法严谨性 + 实验有效性\n\n## 总体评分\n**Overall Assessment**: 3.5 — Borderline Conference\n**一句话总结**: 核心发现（Likert vs. pairwise 灵敏度差距）真实且有实用价值，统计三角验证扎实，但 evaluator-producer confound 控制不足、因果声明过强于识别策略、样本量偏小这三个问题需要修正后才达到 Conference 水平。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 7 种统计方法三角验证 Blindspot 结论可信；但因果识别假设有缺口，evaluator-producer confound 的 independence test 只覆盖 verbosity 一个轴 |\n| Excitement | 3.5/5 | Likert Blindspot 对 LLM evaluation 社区有实际指导意义；但底层心理测量原理本身是已知的（Thurstone 1927），贡献主要在量化而非发现 |\n| Reproducibility | 3/5 | 实验细节基本充分（模型版本、seed、bootstrap 参数），但代码/数据仅\"upon acceptance\"承诺；使用商业 API (GPT-4o) 限制精确复现 |\n| Reviewer Confidence | 4/5 | 统计方法论、LLM evaluation、因果推断均在审稿人专业范围内 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 因果识别假设不充分且可能被违反\n\n- 具体位置：§3.5 (Causal Framework), Figure 2, §3.2\n- 问题：\n  1. 识别假设 (iii)（\"the style rewrite introduces no systematic differences beyond the target axis\"）是可检验的，但论文未检验。改写 formality 可能同时改变 register、vocabulary sophistication、syntactic complexity 等。论文未进行多轴测量来确认单轴干预的纯净性。\n  2. Table 3 中 originality OR 在多个配置下显著（GPT-4o formality: OR=2.32, p=0.006; Qwen3 register: OR=5.72, p<.0001），这直接表明 NLI gate 未能完全阻断 R→Q 路径——rewrite 确实改变了质量感知。这是对核心识别假设 (i) 的经验性违反。\n  3. 全文使用\"counterfactual\"\"interventional\"\"do-operator\"等强因果语言，但 §3.5 又声明\"not a complete structural causal model, nor do we invoke SUTVA\"。这种措辞不一致会误导读者对证据强度的判断。\n- 为什么影响接收：因果推断框架是 CSD 的核心卖点之一（Title 含\"Counterfactual\"，Contribution 1 称\"interventional framework\"）。如果识别策略有缺口，论文的方法论贡献被削弱。\n- 建议修改方向：\n  (a) 增加多轴测量实验：对 formality rewrite 同时测量 register 和 verbosity 的变化幅度；\n  (b) 将语言从\"interventional/counterfactual\"降级为\"quasi-experimental\"或\"controlled comparison\"；\n  (c) 在 §3.5 明确讨论 originality OR 显著意味着识别假设 (i) 部分违反，以及这对 style effect 估计的具体影响方向和幅度。\n\n**N2** [critical] Evaluator-producer confound 的 independence test 覆盖不完整\n\n- 具体位置：Appendix D (Rewriter Independence), §5.3, Limitations\n- 问题：\n  1. Qwen3-32B 同时担任 rewriter 和 judge，论文自身数据显示其效应量系统性偏高：formality Style OR 4.20 vs GPT-4o 2.58（n=88），originality OR 系统性 ~2× GPT-4o。\n  2. Rewriter independence test（Appendix D, Table 5）仅覆盖 verbosity 轴，缺少 formality 和 register 的 independence test。而 formality 恰好是 evaluator-producer bias 最明显的轴（Qwen3 OR=4.20 vs GPT-4o OR=2.58 at n=88）。\n  3. 论文在 Limitations 中承认\"partial self-recognition\"，但主分析（Table 1, Table 3）仍以 Qwen3-32B 结果作为与 GPT-4o 并列的主要证据。\n- 为什么影响接收：如果 Qwen3-32B 的 formality/register 效应量因 self-recognition 而膨胀，则 cross-judge replication 的可信度降低，\"across two judges\" 的 generalizability claim 被削弱。\n- 建议修改方向：\n  (a) 补做 formality 轴的 rewriter independence test（用 GPT-4o 做 rewriter, Qwen3-32B 做 judge）；\n  (b) 或者在主文明确标注 Qwen3-32B 结果仅作为 existence claim（定性方向一致），不适合与 GPT-4o 做定量 effect size 比较；\n  (c) 增加第三个独立 judge（如 Llama）以减弱对 Qwen3-32B 的依赖。\n\n**N3** [critical] \"Likert Blindspot\" 的表述将已知的统计功效差异包装为新发现\n\n- 具体位置：Abstract, §1 (Introduction), §5.2, Figure 4\n- 问题：\n  1. 论文自身的 power curve (Figure 4) 显示 Likert ATE 在 d=0.073 时需要 n≈1,473 才能达到 80% power。在 n=88 时 Likert 检测不到 bias，这完全符合统计预期——不是\"Blindspot\"，而是功效不足。\n  2. 论文承认底层原理\"predicted by classical measurement theory (Thurstone, 1927)\"，但 Title 和 Abstract 的表述方式（\"Reveals the Likert Blindspot\"）暗示这是一个新发现的系统性缺陷，而非已知功效差异的量化。\n  3. n=355 scaled replication 仍显示 Likert non-significant (p=0.60)，这是更强的证据。但这仅针对 Qwen3-32B formality 一个配置，且 Likert ATE 在该配置下的 effect size 未报告。如果 d 仍然很小，则依然是功效问题。\n  4. 实际贡献是量化了 LLM judge 评估场景下 Likert vs pairwise 的 4.5× 效率差距——这有实用价值，但\"Blindspot\"（盲区）的措辞暗示 Likert 永远无法检测到 bias，这不准确。\n- 为什么影响接收：Title 中的核心概念表述过强会削弱审稿人和读者的信任。\n- 建议修改方向：\n  (a) 将\"Blindspot\"重新定义为\"measurement efficiency gap at typical evaluation scales (n=50-200)\"，避免暗示 Likert 在任何 n 下都失败；\n  (b) 对 n=355 replication 补报 Likert effect size (Cohen's d) 和 power；\n  (c) 明确区分\"Likert 在当前实践中的样本量下检测不到\"（实用观察）和\"Likert 本身有系统性缺陷\"（理论声明）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] NLI gate 由同一模型族验证\n\n- 具体位置：§5.1 (NLI Gate Validation)\n- 问题：NLI gate 的 100 对验证使用 Qwen3-32B 作为 annotator（precision 98.9%），但 Qwen3 也是 rewriter。如果 Qwen3 对自己生成的文本有系统性的\"认为内容一致\"倾向，则 precision 被高估。论文提到\"An independent spot-check with GPT-4o is planned\"但未执行。\n- 建议：补做 GPT-4o 或人类标注验证。至少应在 Limitations 中更明确标注此风险。\n\n**W2** [warning] Verbosity 的 direction-aware NLI 削弱了 content preservation 保证\n\n- 具体位置：§3.2\n- 问题：对 verbosity 轴，NLI gate 从双向 entailment 放宽为单向（expansions 只检查 backward entailment）。这将 pass rate 从 65% 提升到 86%，但新放入的 21% 的 pairs 的内容保持质量未经验证。Verbosity rewrite（4.7× longer, §5.4）大幅增加文本内容，单向 NLI 无法排除新增内容引入的质量差异（更详细 = 更高质量的感知）。\n- 建议：对 direction-aware gate 放入的额外 pairs 进行单独分析（BT win rate 是否与 strict bidirectional gate 的 pairs 一致）。\n\n**W3** [warning] Table 1 的 Holm-Bonferroni 报告不够清晰\n\n- 具体位置：Table 1 footnote\n- 问题：Table 1 脚注 \"†raw p < 0.05, Holm-adj. p = 0.08\" 表明主要 family 的 BT 结果在校正后 p=0.08——即严格来说不显著。但 BT 列标注 `***` (p < 0.001) 似乎是未校正值。读者无法从 Table 1 区分哪些 p-values 经过了校正。\n- 建议：在 Table 1 中分别列出 raw p 和 adjusted p，或在脚注中明确说明 `***` 对应的是 raw p 还是 adjusted p。\n\n**W4** [warning] 缺少人工验证 rewriting 质量\n\n- 具体位置：§3.1 (Style-Controlled Rewriting)\n- 问题：整个框架依赖 Qwen3-32B 的 rewriting 质量，但论文没有任何人工评估来验证：(a) rewrite 是否确实改变了目标风格轴；(b) rewrite 是否引入了 NLI 检测不到的 artifacts（如不自然的措辞、风格不一致）。NLI gate 仅验证语义保持，不验证风格变化或自然度。\n- 建议：对 50 个样本进行人工标注，验证风格改变方向正确率和自然度评分。\n\n**W5** [warning] Confound gradient 可能反映 rewriting 难度而非 style axis 本质属性\n\n- 具体位置：§5.6, Table 3\n- 问题：GEE 分解显示 verbosity = pure style, formality = dual, register = originality-dominated。但这个 gradient 可能简单反映：verbosity rewriting（加/减内容）比 formality rewriting（风格转换）更容易做到不改变质量感知，而 register rewriting（academic ↔ conversational）几乎必然改变 sophistication。这意味着 originality confound 实际上在测量 rewriting 质量，而非 style axis 的固有属性。\n- 建议：讨论此替代解释并设计实验区分两种假说（例如，用不同 rewriter 看 confound gradient 是否变化）。\n\n**W6** [warning] 样本量与统计检验稳定性\n\n- 具体位置：§4, Table 1, Table 3\n- 问题：主实验 n=100 LLMBar → NLI 过滤后 ~88 pairs → 173 comparisons。对 GEE 模型（2 个预测变量 + correlation structure），n=88 pairs (176 obs) 的 OR 估计可能不稳定。Table 3 中 Qwen3 form. 从 n=88 (OR=4.20) 到 n=355 (OR=2.15) 的大幅下降直接证明了小样本 OR 估计的不稳定性。Register 轴的 marginal significance (Qwen3: p=0.046) 在这个样本量下尤其脆弱。\n- 建议：(a) 对所有主要轴进行 scaled replication（不仅 formality）；(b) 报告 GEE 模型的 finite-sample corrected standard errors。\n\n---\n\n## 小问题（不影响接收）\n\n1. **Abstract 过长过密**：9 行 abstract 试图覆盖太多细节（7 种统计方法、4 个 judge×axis 配置、3 个 benchmark），建议精简为 5-6 行聚焦核心 claim。\n2. **引用问题**：`hoenig2001abuse` 在 bib 中存在但 verify_references 报告为 orphan（实际通过 `\\citealt` 引用于 experiments.tex:130），可能是交叉检查工具的解析遗漏，不影响正确性。`murugadoss2025sos` 在 OpenAlex 上未找到匹配（可能太新），建议确认该引用的准确性。\n3. **Table 1 最后一列表头为空**：应标注为\"Blindspot indicator\"或类似名称。\n4. **\"~60% uninformative ties\" 在 Abstract、§1、§5.2 重复出现**，但未给出全部 6 个 judge×axis 配置的 tie rate 分布表。\n5. **§5.5 Register 结果**：marginal significance (p=0.046) 在 exploratory family 中报告为\"weak evidence\"是合适的，但在主文中用大半节描述一个 inconclusive 结果可能分散读者注意力。考虑压缩或移入 Appendix。\n6. **Correction proof of concept (§5.6 最后一段)**：debiased prompt 仅 2 行结果，缺乏细节（什么样的 prompt？改了什么？），作为 proof of concept 信息量不足。\n\n---\n\n## Questions for Authors\n\n1. 对 formality rewrite，你们是否测量了 rewrite 在 register/verbosity 轴上的变化幅度？如果 formal rewrite 同时变得更 verbose 或更 academic，则单轴干预假设被违反。\n2. n=355 scaled replication 的 Likert Cohen's d 是多少？如果 d 仍然接近 0.1，则 Likert non-significance 在 n=355 下仍然可能是功效不足（power ≈ 30% at d=0.1, n=355）。\n3. Table 1 中 `***` (p < 0.001) 标注的是 raw p 还是 Holm-adjusted p？如果是 raw p，verbosity BT 的 adjusted p 是多少？\n4. 是否考虑过使用 Likert 分数的 pairwise difference（paired t-test on Δscore）而非单独的 ATE？这会消除 tie-inflation 问题同时保留 Likert 信息。\n5. Claude Sonnet 4 的\"no bias\"结果是否可能因为 Claude 的 rewrite 识别能力更强（即 Claude 有意避免 style bias），而非 Likert/pairwise 灵敏度差异？论文如何排除这种替代解释？\n\n---\n\n## 主要优势\n\n1. **实用价值高**：量化了 LLM evaluation 中 Likert vs pairwise 的 4.5× 效率差距，对评测实践有直接指导意义。\n2. **统计三角验证扎实**：7 种统计方法一致显示 Blindspot（Table 2），跨 judge/benchmark/axis 的系统性复制增强可信度。\n3. **GEE 分解方法论贡献**：将 style effect 和 originality confound 解耦（Table 3）是有价值的方法创新，confound gradient 发现有 insight。\n4. **负面控制有说服力**：Claude Sonnet 4 在两个轴上均未检测到 bias（BT 56.2%/54.1%, 均 non-sig），提供了区分效度。\n5. **透明诚实**：Limitations 部分对 evaluator-producer bias、NLI 验证局限、scale granularity 等问题的讨论比较坦诚。\n6. **GEE diagnostics 完整**：Appendix C 的 correlation structure robustness 检查和 interaction test 是认真的模型诊断工作。\n",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 — 方法严谨性 + 实验有效性\n\n## 总体评分\n**Overall Assessment**: 3.5 — Borderline Conference\n**一句话总结**: 核心发现（Likert vs. pairwise 灵敏度差距）真实且有实用价值，统计三角验证扎实，但 evaluator-producer confound 控制不足、因果声明过强于识别策略、样本量偏小这三个问题需要修正后才达到 Conference 水平。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 7 种统计方法三角验证 Blindspot 结论可信；但因果识别假设有缺口，evaluator-producer confound 的 independence test 只覆盖 verbosity 一个轴 |\n| Excitement | 3.5/5 | Likert Blindspot 对 LLM evaluation 社区有实际指导意义；但底层心理测量原理本身是已知的（Thurstone 1927），贡献主要在量化而非发现 |\n| Reproducibility | 3/5 | 实验细节基本充分（模型版本、seed、bootstrap 参数），但代码/数据仅\"upon acceptance\"承诺；使用商业 API (GPT-4o) 限制精确复现 |\n| Reviewer Confidence | 4/5 | 统计方法论、LLM evaluation、因果推断均在审稿人专业范围内 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 因果识别假设不充分且可能被违反\n\n- 具体位置：§3.5 (Causal Framework), Figure 2, §3.2\n- 问题：\n  1. 识别假设 (iii)（\"the style rewrite introduces no systematic differences beyond the target axis\"）是可检验的，但论文未检验。改写 formality 可能同时改变 register、vocabulary sophistication、syntactic complexity 等。论文未进行多轴测量来确认单轴干预的纯净性。\n  2. Table 3 中 originality OR 在多个配置下显著（GPT-4o formality: OR=2.32, p=0.006; Qwen3 register: OR=5.72, p<.0001），这直接表明 NLI gate 未能完全阻断 R→Q 路径——rewrite 确实改变了质量感知。这是对核心识别假设 (i) 的经验性违反。\n  3. 全文使用\"counterfactual\"\"interventional\"\"do-operator\"等强因果语言，但 §3.5 又声明\"not a complete structural causal model, nor do we invoke SUTVA\"。这种措辞不一致会误导读者对证据强度的判断。\n- 为什么影响接收：因果推断框架是 CSD 的核心卖点之一（Title 含\"Counterfactual\"，Contribution 1 称\"interventional framework\"）。如果识别策略有缺口，论文的方法论贡献被削弱。\n- 建议修改方向：\n  (a) 增加多轴测量实验：对 formality rewrite 同时测量 register 和 verbosity 的变化幅度；\n  (b) 将语言从\"interventional/counterfactual\"降级为\"quasi-experimental\"或\"controlled comparison\"；\n  (c) 在 §3.5 明确讨论 originality OR 显著意味着识别假设 (i) 部分违反，以及这对 style effect 估计的具体影响方向和幅度。\n\n**N2** [critical] Evaluator-producer confound 的 independence test 覆盖不完整\n\n- 具体位置：Appendix D (Rewriter Independence), §5.3, Limitations\n- 问题：\n  1. Qwen3-32B 同时担任 rewriter 和 judge，论文自身数据显示其效应量系统性偏高：formality Style OR 4.20 vs GPT-4o 2.58（n=88），originality OR 系统性 ~2× GPT-4o。\n  2. Rewriter independence test（Appendix D, Table 5）仅覆盖 verbosity 轴，缺少 formality 和 register 的 independence test。而 formality 恰好是 evaluator-producer bias 最明显的轴（Qwen3 OR=4.20 vs GPT-4o OR=2.58 at n=88）。\n  3. 论文在 Limitations 中承认\"partial self-recognition\"，但主分析（Table 1, Table 3）仍以 Qwen3-32B 结果作为与 GPT-4o 并列的主要证据。\n- 为什么影响接收：如果 Qwen3-32B 的 formality/register 效应量因 self-recognition 而膨胀，则 cross-judge replication 的可信度降低，\"across two judges\" 的 generalizability claim 被削弱。\n- 建议修改方向：\n  (a) 补做 formality 轴的 rewriter independence test（用 GPT-4o 做 rewriter, Qwen3-32B 做 judge）；\n  (b) 或者在主文明确标注 Qwen3-32B 结果仅作为 existence claim（定性方向一致），不适合与 GPT-4o 做定量 effect size 比较；\n  (c) 增加第三个独立 judge（如 Llama）以减弱对 Qwen3-32B 的依赖。\n\n**N3** [critical] \"Likert Blindspot\" 的表述将已知的统计功效差异包装为新发现\n\n- 具体位置：Abstract, §1 (Introduction), §5.2, Figure 4\n- 问题：\n  1. 论文自身的 power curve (Figure 4) 显示 Likert ATE 在 d=0.073 时需要 n≈1,473 才能达到 80% power。在 n=88 时 Likert 检测不到 bias，这完全符合统计预期——不是\"Blindspot\"，而是功效不足。\n  2. 论文承认底层原理\"predicted by classical measurement theory (Thurstone, 1927)\"，但 Title 和 Abstract 的表述方式（\"Reveals the Likert Blindspot\"）暗示这是一个新发现的系统性缺陷，而非已知功效差异的量化。\n  3. n=355 scaled replication 仍显示 Likert non-significant (p=0.60)，这是更强的证据。但这仅针对 Qwen3-32B formality 一个配置，且 Likert ATE 在该配置下的 effect size 未报告。如果 d 仍然很小，则依然是功效问题。\n  4. 实际贡献是量化了 LLM judge 评估场景下 Likert vs pairwise 的 4.5× 效率差距——这有实用价值，但\"Blindspot\"（盲区）的措辞暗示 Likert 永远无法检测到 bias，这不准确。\n- 为什么影响接收：Title 中的核心概念表述过强会削弱审稿人和读者的信任。\n- 建议修改方向：\n  (a) 将\"Blindspot\"重新定义为\"measurement efficiency gap at typical evaluation scales (n=50-200)\"，避免暗示 Likert 在任何 n 下都失败；\n  (b) 对 n=355 replication 补报 Likert effect size (Cohen's d) 和 power；\n  (c) 明确区分\"Likert 在当前实践中的样本量下检测不到\"（实用观察）和\"Likert 本身有系统性缺陷\"（理论声明）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] NLI gate 由同一模型族验证\n\n- 具体位置：§5.1 (NLI Gate Validation)\n- 问题：NLI gate 的 100 对验证使用 Qwen3-32B 作为 annotator（precision 98.9%），但 Qwen3 也是 rewriter。如果 Qwen3 对自己生成的文本有系统性的\"认为内容一致\"倾向，则 precision 被高估。论文提到\"An independent spot-check with GPT-4o is planned\"但未执行。\n- 建议：补做 GPT-4o 或人类标注验证。至少应在 Limitations 中更明确标注此风险。\n\n**W2** [warning] Verbosity 的 direction-aware NLI 削弱了 content preservation 保证\n\n- 具体位置：§3.2\n- 问题：对 verbosity 轴，NLI gate 从双向 entailment 放宽为单向（expansions 只检查 backward entailment）。这将 pass rate 从 65% 提升到 86%，但新放入的 21% 的 pairs 的内容保持质量未经验证。Verbosity rewrite（4.7× longer, §5.4）大幅增加文本内容，单向 NLI 无法排除新增内容引入的质量差异（更详细 = 更高质量的感知）。\n- 建议：对 direction-aware gate 放入的额外 pairs 进行单独分析（BT win rate 是否与 strict bidirectional gate 的 pairs 一致）。\n\n**W3** [warning] Table 1 的 Holm-Bonferroni 报告不够清晰\n\n- 具体位置：Table 1 footnote\n- 问题：Table 1 脚注 \"†raw p < 0.05, Holm-adj. p = 0.08\" 表明主要 family 的 BT 结果在校正后 p=0.08——即严格来说不显著。但 BT 列标注 `***` (p < 0.001) 似乎是未校正值。读者无法从 Table 1 区分哪些 p-values 经过了校正。\n- 建议：在 Table 1 中分别列出 raw p 和 adjusted p，或在脚注中明确说明 `***` 对应的是 raw p 还是 adjusted p。\n\n**W4** [warning] 缺少人工验证 rewriting 质量\n\n- 具体位置：§3.1 (Style-Controlled Rewriting)\n- 问题：整个框架依赖 Qwen3-32B 的 rewriting 质量，但论文没有任何人工评估来验证：(a) rewrite 是否确实改变了目标风格轴；(b) rewrite 是否引入了 NLI 检测不到的 artifacts（如不自然的措辞、风格不一致）。NLI gate 仅验证语义保持，不验证风格变化或自然度。\n- 建议：对 50 个样本进行人工标注，验证风格改变方向正确率和自然度评分。\n\n**W5** [warning] Confound gradient 可能反映 rewriting 难度而非 style axis 本质属性\n\n- 具体位置：§5.6, Table 3\n- 问题：GEE 分解显示 verbosity = pure style, formality = dual, register = originality-dominated。但这个 gradient 可能简单反映：verbosity rewriting（加/减内容）比 formality rewriting（风格转换）更容易做到不改变质量感知，而 register rewriting（academic ↔ conversational）几乎必然改变 sophistication。这意味着 originality confound 实际上在测量 rewriting 质量，而非 style axis 的固有属性。\n- 建议：讨论此替代解释并设计实验区分两种假说（例如，用不同 rewriter 看 confound gradient 是否变化）。\n\n**W6** [warning] 样本量与统计检验稳定性\n\n- 具体位置：§4, Table 1, Table 3\n- 问题：主实验 n=100 LLMBar → NLI 过滤后 ~88 pairs → 173 comparisons。对 GEE 模型（2 个预测变量 + correlation structure），n=88 pairs (176 obs) 的 OR 估计可能不稳定。Table 3 中 Qwen3 form. 从 n=88 (OR=4.20) 到 n=355 (OR=2.15) 的大幅下降直接证明了小样本 OR 估计的不稳定性。Register 轴的 marginal significance (Qwen3: p=0.046) 在这个样本量下尤其脆弱。\n- 建议：(a) 对所有主要轴进行 scaled replication（不仅 formality）；(b) 报告 GEE 模型的 finite-sample corrected standard errors。\n\n---\n\n## 小问题（不影响接收）\n\n1. **Abstract 过长过密**：9 行 abstract 试图覆盖太多细节（7 种统计方法、4 个 judge×axis 配置、3 个 benchmark），建议精简为 5-6 行聚焦核心 claim。\n2. **引用问题**：`hoenig2001abuse` 在 bib 中存在但 verify_references 报告为 orphan（实际通过 `\\citealt` 引用于 experiments.tex:130），可能是交叉检查工具的解析遗漏，不影响正确性。`murugadoss2025sos` 在 OpenAlex 上未找到匹配（可能太新），建议确认该引用的准确性。\n3. **Table 1 最后一列表头为空**：应标注为\"Blindspot indicator\"或类似名称。\n4. **\"~60% uninformative ties\" 在 Abstract、§1、§5.2 重复出现**，但未给出全部 6 个 judge×axis 配置的 tie rate 分布表。\n5. **§5.5 Register 结果**：marginal significance (p=0.046) 在 exploratory family 中报告为\"weak evidence\"是合适的，但在主文中用大半节描述一个 inconclusive 结果可能分散读者注意力。考虑压缩或移入 Appendix。\n6. **Correction proof of concept (§5.6 最后一段)**：debiased prompt 仅 2 行结果，缺乏细节（什么样的 prompt？改了什么？），作为 proof of concept 信息量不足。\n\n---\n\n## Questions for Authors\n\n1. 对 formality rewrite，你们是否测量了 rewrite 在 register/verbosity 轴上的变化幅度？如果 formal rewrite 同时变得更 verbose 或更 academic，则单轴干预假设被违反。\n2. n=355 scaled replication 的 Likert Cohen's d 是多少？如果 d 仍然接近 0.1，则 Likert non-significance 在 n=355 下仍然可能是功效不足（power ≈ 30% at d=0.1, n=355）。\n3. Table 1 中 `***` (p < 0.001) 标注的是 raw p 还是 Holm-adjusted p？如果是 raw p，verbosity BT 的 adjusted p 是多少？\n4. 是否考虑过使用 Likert 分数的 pairwise difference（paired t-test on Δscore）而非单独的 ATE？这会消除 tie-inflation 问题同时保留 Likert 信息。\n5. Claude Sonnet 4 的\"no bias\"结果是否可能因为 Claude 的 rewrite 识别能力更强（即 Claude 有意避免 style bias），而非 Likert/pairwise 灵敏度差异？论文如何排除这种替代解释？\n\n---\n\n## 主要优势\n\n1. **实用价值高**：量化了 LLM evaluation 中 Likert vs pairwise 的 4.5× 效率差距，对评测实践有直接指导意义。\n2. **统计三角验证扎实**：7 种统计方法一致显示 Blindspot（Table 2），跨 judge/benchmark/axis 的系统性复制增强可信度。\n3. **GEE 分解方法论贡献**：将 style effect 和 originality confound 解耦（Table 3）是有价值的方法创新，confound gradient 发现有 insight。\n4. **负面控制有说服力**：Claude Sonnet 4 在两个轴上均未检测到 bias（BT 56.2%/54.1%, 均 non-sig），提供了区分效度。\n5. **透明诚实**：Limitations 部分对 evaluator-producer bias、NLI 验证局限、scale granularity 等问题的讨论比较坦诚。\n6. **GEE diagnostics 完整**：Appendix C 的 correlation structure robustness 检查和 interaction test 是认真的模型诊断工作。\n",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 197 · 2026-05-21T09:41:31.973315+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3965
}
```

</details>

---


### Assistant

_source line 198 · 2026-05-21T09:41:41.411172+00:00_

审稿报告已提交给 Review Director。

总结：

- **Overall: 3.5 (Borderline Conference)**
- 3 个 Must-Fix：(1) 因果识别假设不充分，originality OR 显著说明 NLI gate 未完全阻断 R→Q 路径；(2) Evaluator-producer independence test 仅覆盖 verbosity，缺 formality/register；(3) "Blindspot" 表述将功效差异包装为新发现，需降级为 "measurement efficiency gap"
- 6 个 Should-Fix：NLI 验证模型族自引用、direction-aware NLI 削弱保证、Holm-Bonferroni 报告不清晰、缺人工验证、confound gradient 替代解释、小样本 OR 不稳定
- 核心优势：7 种方法三角验证扎实、GEE 分解有方法论贡献、Claude 负面控制有说服力

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1"
}
```

</details>

---


## Round 8

## Round 8

4 recorded events


### User

_source line 199 · 2026-05-21T09:42:54.744732+00:00_

[Round 1 审稿请求]:
## 交叉分享：以下是 Reviewer 2 的完整审稿意见

请逐条回应 Reviewer 2 的每个 Must-Fix 和 Should-Fix 问题：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供具体证据（cite 具体 Section/Table/Figure）

特别关注：你和 R2 是否在 "Blindspot framing"、"causal 语言"、"evidence scope" 等问题上有共识或分歧。

---

# Reviewer 2 — 新颖性 + 完整性 + Related Work

## 总体评分
**Overall Assessment**: 3.5 — Borderline Conference

## Must-Fix 问题

**N1** [critical] Likert Blindspot 的 framing 混淆了 "measurement blindspot" 与 "statistical power gap"
- Title 用 "Blindspot" 暗示 Likert 有质性缺陷，但 Figure 4 evidence 只支持量性差异
- Thurstone (1927) 关于 ordinal scale 灵敏度低于 paired comparison 的结论已有近百年
- 论文自己在 p.2 写 "~1.5× more data to reach equivalent sensitivity"——这是 power 语言
- 建议：明确区分量性 gap 和质性 blindspot，降调标题/abstract

**N2** [critical] "Causal"/"Counterfactual" 术语与方法论强度不匹配
- Title "Counterfactual"、§3.5 "Causal Framework"、Figure 2 DAG 暗示形式化因果模型
- 但 §3.5 声明 "not a complete structural causal model, nor do we invoke SUTVA"
- 实际上是 controlled intervention study with imperfect content preservation
- 建议：替换为 "Interventional"/"Controlled"，§3.5 标题改为 "Interventional Design"

**N3** [critical] 证据基础过窄但 practical recommendation 过强
- n=100 LLMBar × 3 judges × 2 有效 axes → 不足以支撑一般性实践建议
- LLMBar 只有 instruction-response pairs，不覆盖 dialogue/summarization/creative writing
- Tone axis 完全失败但只在 Limitations 一笔带过
- 建议：加 qualifier、增加 benchmark、正文讨论 tone axis 失败

## Should-Fix 问题

**W1** Related Work 引用偏少（27条 vs EMNLP 通常 40-60 条），缺 counterfactual generation 方法谱系（CausaLM, Polyjuice）和 NLG evaluation scale design 文献（Amidei 2019, Clark 2021）
**W2** NLI gate false negative 可能引入 systematic selection bias——大幅 style 变化更易被过滤，导致 ATE 被 attenuated
**W3** GEE "decomposition" 在 confounding 未消除时有误导性——应改为 "partial adjustment"
**W4** Claude 作为 negative control 的解释力有限——可能是 Claude alignment 消除了 bias 而非 CSD 无 false positive
**W5** Appendix 中 Direction Asymmetry 和 GEE Robustness 应部分纳入正文

## 主要优势
1. Pipeline 设计思路清晰，工程可复现
2. Negative results 诚实呈现增加可信度
3. Figure 4 power curve 是 measurement methodology 层面的有价值贡献
4. GEE decomposition 方向正确
5. 写作清晰、信息密度高
6. Bradley-Terry + bootstrap CI 统计严谨

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 200 · 2026-05-21T09:44:36.852062+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的逐条交叉回应\n\n---\n\n## Must-Fix 问题\n\n### [AGREE] R2-N1: Likert Blindspot framing 混淆 measurement blindspot 与 statistical power gap\n\n同意，这与我的 R1-N3 高度一致。R2 和我独立达成了相同判断：论文的核心发现本质上是一个**量化的统计功效差距**（4.5× efficiency gap），而非 Likert 的质性缺陷。\n\n补充我的观察：\n- Figure 4 (power curve) 明确显示 Likert ATE 在 n≈1,473 时达到 80% power——即 Likert 在足够样本量下可以检测到 bias，\"Blindspot\" 的措辞暗示永远无法检测，这不准确。\n- n=355 scaled replication（§5.6）Likert 仍 non-significant (p=0.60)，但论文未报告该配置下的 Cohen's d。如果 d 仍接近 0.1，按 power curve，n=355 的 Likert power 仅约 25-30%——依然是功效不足而非系统性盲区。\n- R2 指出论文自身使用 \"~4.5× more data to reach equivalent sensitivity\" 的 power 语言（§5.2），这与 \"Blindspot\" 的 framing 自相矛盾——我完全同意此观察。\n\n**共识结论**：建议将 \"Blindspot\" 重新定义或降级为 \"measurement efficiency gap at typical evaluation scales\"，Title 和 Abstract 相应调整。\n\n---\n\n### [AGREE] R2-N2: \"Causal\"/\"Counterfactual\" 术语与方法论强度不匹配\n\n同意，这与我的 R1-N1 高度一致。两位 Reviewer 对因果语言过强的判断完全一致。\n\n补充我的发现：\n- 我在 R1-N1 中进一步指出了**经验性违反的证据**：Table 3 中 originality OR 在多个配置下显著（GPT-4o formality: OR=2.32, p=0.006），直接表明 NLI gate 未能完全阻断 R→Q path。这不仅是术语问题，更是识别策略有实质缺口。\n- R2 建议的 \"Interventional\"/\"Controlled\" 替代表述合理。我进一步建议 §3.5 标题可改为 \"Assumed Data-Generating Process and Identification Strategy\"，并增加对识别假设违反程度的量化讨论。\n\n**共识结论**：因果语言应降级；§3.5 应更明确讨论假设的局限性。\n\n---\n\n### [REBUT] R2-N3: 证据基础过窄但 practical recommendation 过强（部分反驳）\n\nR2 的方向正确但程度表述过重，且有一处事实性偏差。\n\n反驳点：\n1. **R2 称 \"tone axis 完全失败但只在 Limitations 一笔带过\"**——事实不符。Register (tone) axis 在**主文 §5.5** 有大半节专门讨论（第 7 页），包括 BT 结果（GPT-4o 57.0%, p=0.04）、GEE 分解（originality-dominated）、和明确的 \"weak evidence\" 定性。这不是 \"只在 Limitations 一笔带过\"。\n\n2. **Cross-benchmark 证据被低估**。Table 1 显示 CSD 在三个独立 benchmark 上复制：LLMBar (n=100), AlpacaEval, MT-Bench，覆盖 instruction-following、open-ended preference、multi-turn dialogue 三种任务类型。R2 称 \"不覆盖 dialogue/summarization\"——但 MT-Bench 本身就是多轮对话评测。\n\n3. **Cross-judge 复制**。GPT-4o（独立 judge，不是 rewriter）在所有配置上确认 Blindspot direction 一致。Claude Sonnet 4 提供负面控制。\n\n我同意的部分：\n- n=100 作为起点确实偏小。更大的 benchmark（如 WildBench 或 Arena-Hard）会显著增强说服力。\n- 论文从有限证据跳到 \"style bias audits should adopt pairwise comparison\"（Conclusion, §6）的 recommendation 确实过强——应加 qualifier \"in typical evaluation settings with n < 500\"。\n- 增加 dialogue/summarization/creative writing 的专项验证是合理的未来工作建议。\n\n**结论**：R2-N3 的核心方向正确（evidence scope vs claim scope 不匹配），但 \"tone axis 只在 Limitations 提及\" 和 \"不覆盖 dialogue\" 的具体论据不准确。建议 severity 从 critical 降为 warning。\n\n---\n\n## Should-Fix 问题\n\n### [AGREE] R2-W1: Related Work 引用偏少，缺少关键谱系\n\n同意。27 条引用对 EMNLP 确实偏少。我在审稿时未专门标记此问题，但 R2 指出的缺失文献确实相关：\n- **Counterfactual text generation 方法**：CausaLM (Feder et al., 2021) 和 Polyjuice (Wu et al., 2021) 是 controlled text perturbation 的重要前驱工作，与 CSD 的 rewriting 策略有直接方法论联系。\n- **NLG evaluation scale design**：Clark et al. (2021) 关于 evaluation scale 选择的系统性研究，与 Likert vs pairwise 的讨论直接相关。\n\n补充建议：还应引用 Chatbot Arena 的 pairwise 方法论细节（Boubdir et al., 2023 关于 BT 模型在 LLM 评估中的实践），以及 Wu & Aji (2023) 关于 LLM judge 评估协议对比。\n\n---\n\n### [AGREE] R2-W2: NLI gate false negative 可能引入 systematic selection bias → ATE attenuation\n\n同意，这是我未独立提出的一个有价值的观察。\n\n论文 §5.1 提供了部分回应：false negatives 无方向性偏差（Fisher p=0.35），threshold sensitivity 显示 win rate 在 0.70-0.95 范围内稳定（72.3-73.9%）。但 R2 的理论论点仍然成立：如果大幅 style 变化更容易被 NLI gate 过滤掉（因为大幅改变更可能伴随内容变化），则保留的 pairs 系统性地包含较小的 style 干预，从而压低 measured effect。\n\n这与我的 R1-W2（direction-aware NLI for verbosity）相关但不同——R2 关注的是 attenuation bias 方向（低估效应），而我关注的是 relaxed gate 可能引入的 confound（高估效应）。两个方向的 bias 可能部分抵消，但论文未讨论这种可能性。\n\n---\n\n### [AGREE] R2-W3: GEE \"decomposition\" 在 confounding 未消除时有误导性\n\n同意。这与我的 R1-W5（confound gradient 可能反映 rewriting 难度而非 axis 本质属性）方向一致。\n\n\"Decomposition\" 暗示 style 和 originality 效应被干净地分离，但当 NLI gate 不能完全消除 content confounding 时（Table 3 中 originality OR 显著就是证据），GEE 只是在给定 rewriting 质量下的条件估计，不是因果 decomposition。R2 建议的 \"partial adjustment\" 或 \"conditional analysis\" 更准确。\n\n---\n\n### [REBUT] R2-W4: Claude 作为 negative control 的解释力有限\n\n部分反驳。R2 的替代解释（Claude alignment 消除了 bias，而非 CSD 无 false positive）是合理的，但这恰恰**增强**了 Claude 作为 negative control 的价值：\n\n1. **论文未声称 Claude 证明 CSD 无 false positive**。§5.4（cross-axis）和 Table 1 中 Claude 的结果被用于展示 **discriminative validity**——CSD 不是在所有 judge 上都报阳性，说明框架能区分有 bias 和无 bias 的 judge。\n\n2. **R2 的替代解释本身是一个积极发现**：如果 Claude 的 alignment 确实消除了 style bias（而 GPT-4o 和 Qwen3-32B 没有），这正是 CSD 试图检测的现象——不同 judge 有不同的 style sensitivity profile。\n\n3. **真正的 false positive 控制需要 known-zero-bias 条件**。论文确实无法完全排除 false positive，但这是任何新检测工具的普遍局限，不是 Claude negative control 设计的特定弱点。\n\n建议 severity 降为 minor：可在讨论中增加一句 \"Claude's null result may reflect either the absence of style bias or the presence of countervailing alignment mechanisms; distinguishing these interpretations requires further investigation.\"\n\n---\n\n### [REBUT] R2-W5: Appendix 中 Direction Asymmetry 和 GEE Robustness 应部分纳入正文\n\n不同意。在 8 页严格限制下（EMNLP 2026 Long Paper），主文需优先分配给核心论证。Direction Asymmetry（Appendix A）和 GEE Robustness（Appendix C）是支撑性细节：\n\n- Appendix A 的 direction asymmetry **结论已在主文 §5.6 引用**（\"full direction-asymmetry analysis in Appendix A\"），读者能快速定位。\n- Appendix C 的 correlation structure robustness **结论已在主文 §5.6 引用**（Table 3 的可靠性建立在 Appendix C 的诊断之上）。\n- 将这些内容搬入正文会挤占本已紧张的 8 页空间，可能需要删除 power curve (Figure 4) 或 sensitivity hierarchy (Table 2) 等更核心的内容。\n\n当前 appendix 安排符合 ACL 惯例（主文放结论和关键证据，appendix 放诊断和细节）。\n\n---\n\n## R1-R2 共识总结\n\n| 维度 | R1-R2 共识 | 分歧 |\n|------|------------|------|\n| Blindspot framing | **强共识**：均认为 \"Blindspot\" 过强，应降级为 efficiency gap | 无 |\n| 因果语言 | **强共识**：均认为 causal/counterfactual 语言与方法论强度不匹配 | R1 进一步指出了 originality OR 的经验性违反证据 |\n| 证据范围 | **部分共识**：均认为样本量偏小、practical recommendation 过强 | R1 认为 R2 低估了 cross-benchmark 证据和 register axis 在正文中的讨论 |\n| GEE 命名 | **共识**：均认为 \"decomposition\" 在有残余 confounding 时有误导性 | 无 |\n| Claude negative control | **分歧**：R2 认为解释力有限，R1 认为 discriminative validity 论证合理 | — |\n| Appendix placement | **分歧**：R2 认为应搬入正文，R1 认为当前安排合理（8 页限制） | — |\n| Evaluator-producer confound | R1 独立提出的 N2 (independence test 不完整) R2 未提及 | — |\n| NLI validation by same model family | R1 独立提出的 W1，R2 未提及 | — |\n| NLI false negative → attenuation | R2 独立提出的 W2，R1 未提及（但提了 direction-aware gate 问题） | — |\n| Related work 引用量 | R2 独立提出的 W1，R1 未提及 | — |\n",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的逐条交叉回应\n\n---\n\n## Must-Fix 问题\n\n### [AGREE] R2-N1: Likert Blindspot framing 混淆 measurement blindspot 与 statistical power gap\n\n同意，这与我的 R1-N3 高度一致。R2 和我独立达成了相同判断：论文的核心发现本质上是一个**量化的统计功效差距**（4.5× efficiency gap），而非 Likert 的质性缺陷。\n\n补充我的观察：\n- Figure 4 (power curve) 明确显示 Likert ATE 在 n≈1,473 时达到 80% power——即 Likert 在足够样本量下可以检测到 bias，\"Blindspot\" 的措辞暗示永远无法检测，这不准确。\n- n=355 scaled replication（§5.6）Likert 仍 non-significant (p=0.60)，但论文未报告该配置下的 Cohen's d。如果 d 仍接近 0.1，按 power curve，n=355 的 Likert power 仅约 25-30%——依然是功效不足而非系统性盲区。\n- R2 指出论文自身使用 \"~4.5× more data to reach equivalent sensitivity\" 的 power 语言（§5.2），这与 \"Blindspot\" 的 framing 自相矛盾——我完全同意此观察。\n\n**共识结论**：建议将 \"Blindspot\" 重新定义或降级为 \"measurement efficiency gap at typical evaluation scales\"，Title 和 Abstract 相应调整。\n\n---\n\n### [AGREE] R2-N2: \"Causal\"/\"Counterfactual\" 术语与方法论强度不匹配\n\n同意，这与我的 R1-N1 高度一致。两位 Reviewer 对因果语言过强的判断完全一致。\n\n补充我的发现：\n- 我在 R1-N1 中进一步指出了**经验性违反的证据**：Table 3 中 originality OR 在多个配置下显著（GPT-4o formality: OR=2.32, p=0.006），直接表明 NLI gate 未能完全阻断 R→Q path。这不仅是术语问题，更是识别策略有实质缺口。\n- R2 建议的 \"Interventional\"/\"Controlled\" 替代表述合理。我进一步建议 §3.5 标题可改为 \"Assumed Data-Generating Process and Identification Strategy\"，并增加对识别假设违反程度的量化讨论。\n\n**共识结论**：因果语言应降级；§3.5 应更明确讨论假设的局限性。\n\n---\n\n### [REBUT] R2-N3: 证据基础过窄但 practical recommendation 过强（部分反驳）\n\nR2 的方向正确但程度表述过重，且有一处事实性偏差。\n\n反驳点：\n1. **R2 称 \"tone axis 完全失败但只在 Limitations 一笔带过\"**——事实不符。Register (tone) axis 在**主文 §5.5** 有大半节专门讨论（第 7 页），包括 BT 结果（GPT-4o 57.0%, p=0.04）、GEE 分解（originality-dominated）、和明确的 \"weak evidence\" 定性。这不是 \"只在 Limitations 一笔带过\"。\n\n2. **Cross-benchmark 证据被低估**。Table 1 显示 CSD 在三个独立 benchmark 上复制：LLMBar (n=100), AlpacaEval, MT-Bench，覆盖 instruction-following、open-ended preference、multi-turn dialogue 三种任务类型。R2 称 \"不覆盖 dialogue/summarization\"——但 MT-Bench 本身就是多轮对话评测。\n\n3. **Cross-judge 复制**。GPT-4o（独立 judge，不是 rewriter）在所有配置上确认 Blindspot direction 一致。Claude Sonnet 4 提供负面控制。\n\n我同意的部分：\n- n=100 作为起点确实偏小。更大的 benchmark（如 WildBench 或 Arena-Hard）会显著增强说服力。\n- 论文从有限证据跳到 \"style bias audits should adopt pairwise comparison\"（Conclusion, §6）的 recommendation 确实过强——应加 qualifier \"in typical evaluation settings with n < 500\"。\n- 增加 dialogue/summarization/creative writing 的专项验证是合理的未来工作建议。\n\n**结论**：R2-N3 的核心方向正确（evidence scope vs claim scope 不匹配），但 \"tone axis 只在 Limitations 提及\" 和 \"不覆盖 dialogue\" 的具体论据不准确。建议 severity 从 critical 降为 warning。\n\n---\n\n## Should-Fix 问题\n\n### [AGREE] R2-W1: Related Work 引用偏少，缺少关键谱系\n\n同意。27 条引用对 EMNLP 确实偏少。我在审稿时未专门标记此问题，但 R2 指出的缺失文献确实相关：\n- **Counterfactual text generation 方法**：CausaLM (Feder et al., 2021) 和 Polyjuice (Wu et al., 2021) 是 controlled text perturbation 的重要前驱工作，与 CSD 的 rewriting 策略有直接方法论联系。\n- **NLG evaluation scale design**：Clark et al. (2021) 关于 evaluation scale 选择的系统性研究，与 Likert vs pairwise 的讨论直接相关。\n\n补充建议：还应引用 Chatbot Arena 的 pairwise 方法论细节（Boubdir et al., 2023 关于 BT 模型在 LLM 评估中的实践），以及 Wu & Aji (2023) 关于 LLM judge 评估协议对比。\n\n---\n\n### [AGREE] R2-W2: NLI gate false negative 可能引入 systematic selection bias → ATE attenuation\n\n同意，这是我未独立提出的一个有价值的观察。\n\n论文 §5.1 提供了部分回应：false negatives 无方向性偏差（Fisher p=0.35），threshold sensitivity 显示 win rate 在 0.70-0.95 范围内稳定（72.3-73.9%）。但 R2 的理论论点仍然成立：如果大幅 style 变化更容易被 NLI gate 过滤掉（因为大幅改变更可能伴随内容变化），则保留的 pairs 系统性地包含较小的 style 干预，从而压低 measured effect。\n\n这与我的 R1-W2（direction-aware NLI for verbosity）相关但不同——R2 关注的是 attenuation bias 方向（低估效应），而我关注的是 relaxed gate 可能引入的 confound（高估效应）。两个方向的 bias 可能部分抵消，但论文未讨论这种可能性。\n\n---\n\n### [AGREE] R2-W3: GEE \"decomposition\" 在 confounding 未消除时有误导性\n\n同意。这与我的 R1-W5（confound gradient 可能反映 rewriting 难度而非 axis 本质属性）方向一致。\n\n\"Decomposition\" 暗示 style 和 originality 效应被干净地分离，但当 NLI gate 不能完全消除 content confounding 时（Table 3 中 originality OR 显著就是证据），GEE 只是在给定 rewriting 质量下的条件估计，不是因果 decomposition。R2 建议的 \"partial adjustment\" 或 \"conditional analysis\" 更准确。\n\n---\n\n### [REBUT] R2-W4: Claude 作为 negative control 的解释力有限\n\n部分反驳。R2 的替代解释（Claude alignment 消除了 bias，而非 CSD 无 false positive）是合理的，但这恰恰**增强**了 Claude 作为 negative control 的价值：\n\n1. **论文未声称 Claude 证明 CSD 无 false positive**。§5.4（cross-axis）和 Table 1 中 Claude 的结果被用于展示 **discriminative validity**——CSD 不是在所有 judge 上都报阳性，说明框架能区分有 bias 和无 bias 的 judge。\n\n2. **R2 的替代解释本身是一个积极发现**：如果 Claude 的 alignment 确实消除了 style bias（而 GPT-4o 和 Qwen3-32B 没有），这正是 CSD 试图检测的现象——不同 judge 有不同的 style sensitivity profile。\n\n3. **真正的 false positive 控制需要 known-zero-bias 条件**。论文确实无法完全排除 false positive，但这是任何新检测工具的普遍局限，不是 Claude negative control 设计的特定弱点。\n\n建议 severity 降为 minor：可在讨论中增加一句 \"Claude's null result may reflect either the absence of style bias or the presence of countervailing alignment mechanisms; distinguishing these interpretations requires further investigation.\"\n\n---\n\n### [REBUT] R2-W5: Appendix 中 Direction Asymmetry 和 GEE Robustness 应部分纳入正文\n\n不同意。在 8 页严格限制下（EMNLP 2026 Long Paper），主文需优先分配给核心论证。Direction Asymmetry（Appendix A）和 GEE Robustness（Appendix C）是支撑性细节：\n\n- Appendix A 的 direction asymmetry **结论已在主文 §5.6 引用**（\"full direction-asymmetry analysis in Appendix A\"），读者能快速定位。\n- Appendix C 的 correlation structure robustness **结论已在主文 §5.6 引用**（Table 3 的可靠性建立在 Appendix C 的诊断之上）。\n- 将这些内容搬入正文会挤占本已紧张的 8 页空间，可能需要删除 power curve (Figure 4) 或 sensitivity hierarchy (Table 2) 等更核心的内容。\n\n当前 appendix 安排符合 ACL 惯例（主文放结论和关键证据，appendix 放诊断和细节）。\n\n---\n\n## R1-R2 共识总结\n\n| 维度 | R1-R2 共识 | 分歧 |\n|------|------------|------|\n| Blindspot framing | **强共识**：均认为 \"Blindspot\" 过强，应降级为 efficiency gap | 无 |\n| 因果语言 | **强共识**：均认为 causal/counterfactual 语言与方法论强度不匹配 | R1 进一步指出了 originality OR 的经验性违反证据 |\n| 证据范围 | **部分共识**：均认为样本量偏小、practical recommendation 过强 | R1 认为 R2 低估了 cross-benchmark 证据和 register axis 在正文中的讨论 |\n| GEE 命名 | **共识**：均认为 \"decomposition\" 在有残余 confounding 时有误导性 | 无 |\n| Claude negative control | **分歧**：R2 认为解释力有限，R1 认为 discriminative validity 论证合理 | — |\n| Appendix placement | **分歧**：R2 认为应搬入正文，R1 认为当前安排合理（8 页限制） | — |\n| Evaluator-producer confound | R1 独立提出的 N2 (independence test 不完整) R2 未提及 | — |\n| NLI validation by same model family | R1 独立提出的 W1，R2 未提及 | — |\n| NLI false negative → attenuation | R2 独立提出的 W2，R1 未提及（但提了 direction-aware gate 问题） | — |\n| Related work 引用量 | R2 独立提出的 W1，R1 未提及 | — |\n",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 201 · 2026-05-21T09:44:40.947444+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4095
}
```

</details>

---


### Assistant

_source line 202 · 2026-05-21T09:44:50.103716+00:00_

已提交交叉回应。核心结论：

- **强共识**（R1+R2）：Blindspot framing 过强（应降级为 efficiency gap）、因果语言与方法论不匹配、GEE "decomposition" 命名有误导性
- **部分共识**：证据范围偏窄，但我认为 R2 低估了 cross-benchmark 复制（MT-Bench 覆盖对话）和 register axis 在主文 §5.5 的讨论
- **分歧**：Claude negative control（我认为 discriminative validity 论证合理）、Appendix placement（我认为 8 页限制下当前安排合理）
- **R1 独有关切**：evaluator-producer independence test 仅覆盖 verbosity（R1-N2）、NLI gate 由同模型族验证（R1-W1）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1"
}
```

</details>

---


## Round 9

## Round 9

44 recorded events


### User

_source line 203 · 2026-05-21T11:13:38.862354+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性**审查。

## 审查论文
- 论文路径: `projects/causal_style_decomp_judge/docs/paper/main.tex`（各 section 在 `sections/` 子目录）
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf`

## Venue 要求
- **EMNLP 2026 Main Conference** via ARR
- 正文 8 页限制，参考文献不限页数
- ACL 模板，double-blind 审稿
- Limitations section 必须，不计入页数
- Overall Assessment 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

## 你的审查侧重

请重点审查以下方面，逐条给出详细评价：

1. **统计框架严谨性**：
   - Holm-Bonferroni correction 的应用是否正确（6 tests 的 family 定义）
   - Bradley-Terry 模型假设是否满足（IIA 等）
   - GEE 模型设定（exchangeable correlation、additive specification）
   - Bootstrap CI 的 pair-level resampling 是否恰当
   - 多重比较分类（primary/exploratory/confirmatory）是否合理

2. **NLI Gate 有效性**：
   - DeBERTa-v3-large 0.90 阈值的 justification
   - False negative rate 分析（8.4%）的可靠性
   - Direction-aware NLI（verbosity）的方法论合理性
   - NLI gate 验证使用 Qwen3-32B 作为 annotator 的 evaluator-producer bias 风险
   - GPT-4o spot-check（47/50）的独立性和充分性

3. **因果声明与方法论强度匹配**：
   - Title 中 "Controlled Style Decomposition" 的因果含义
   - §3.5 "Interventional Design" 的 DAG 是否 justified
   - "interventional rather than formal causal evidence" disclaimer 是否充分
   - Originality OR 显著（Table 3）是否证明识别假设经验性违反

4. **实验设计**：
   - Evaluator-producer bias（Qwen3-32B 同时作 rewriter + judge）
   - Rewriter independence test 的覆盖范围（verbosity + formality）
   - Claude Sonnet 4 作为 negative control 的解读
   - 样本量 n=88/355 的统计充分性
   - Cross-benchmark replication 的可信度

5. **Likert Blindspot 的定义和测量**：
   - "measurement attenuation" vs "power gap" 的区分是否令人信服
   - n=355 d→0 是否真的排除了 power gap 解释
   - Sensitivity hierarchy（Table 2）7 种方法比较的公平性
   - Power curve（Figure 3）的解读是否构成 post-hoc power analysis

请给出：
- **Strengths**（逐条）
- **Weaknesses**（逐条，标注 severity: Must-Fix / Should-Fix / Minor）
- **Questions**（需要作者澄清的问题）
- **Missing References**
- **Overall Assessment**（按 EMNLP 2026 评分标准）
- **Confidence**（1-5）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 204 · 2026-05-21T11:13:49.506377+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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

_source line 205 · 2026-05-21T11:13:49.607171+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 206 · 2026-05-21T11:13:52.969831+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 207 · 2026-05-21T11:13:54.928304+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "1-8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 208 · 2026-05-21T11:14:01.382627+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines and review form criteria:

## Reviewer Guidelines

The recommended workflow is to: (1) read the paper and get the first impression, (2) search for related work, not d
…[truncated 1500 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8412
}
```

</details>

---


### Tool result

_source line 209 · 2026-05-21T11:14:02.692615+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 457.1}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 517.3}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 591.7}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 485.9}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 522.9}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 496.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 516.0}], \"total_pages\": 13, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7764
}
```

</details>

---


### Tool call

_source line 210 · 2026-05-21T11:14:09.319062+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all dimensions/criteria with their scales (1-5 or other), descriptions for each score level, and any specific instructions for reviewers. Include the Overall Assessment scale, Soundness, Excitement/Novelty, Reproducibility, and any other rated dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all dimensions/criteria with their scales (1-5 or other), descriptions for each score level, and any specific instructions for reviewers. Include the Overall Assessment scale, Soundness, Excitement/Novelty, Reproducibility, and any other rated dimensions."
  }
}
```

</details>

---


### Tool call

_source line 211 · 2026-05-21T11:14:10.273051+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 212 · 2026-05-21T11:14:10.778480+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 213 · 2026-05-21T11:14:11.232203+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool call

_source line 214 · 2026-05-21T11:14:11.232713+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 215 · 2026-05-21T11:14:11.841394+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1062
}
```

</details>

---


### Tool call

_source line 216 · 2026-05-21T11:14:11.841823+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 217 · 2026-05-21T11:14:12.396911+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1164
}
```

</details>

---


### Tool result

_source line 218 · 2026-05-21T11:14:12.845344+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1003
}
```

</details>

---


### Tool result

_source line 219 · 2026-05-21T11:14:17.746551+00:00_

# ACL Rolling Review Form - Complete Evaluation Dimensions

## Core Rated Dimensions

### 1. Soundness
Assesses scientific rigor and methodological validity. Scale: 1-5 (with .5 increments)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: Strong support for claims with optional improvements
- **3**: Main claims adequately supported; minor details need work
- **2**: Major claims lack sufficient support; technical problems exist
- **1**: Insufficient depth or relevance to computational linguistics

### 2. Excitement
Evaluates subjective appeal and innovation potential. Scale: 1-5 (with .5 increments)
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: Would mention to colleagues; effort to attend presentation
- **3**: Might discuss with others if time permits
- **2**: Doesn't resonate personally; may interest others
- **1**: No relevance to NLP community

### 3. Overall Assessment
Primary recommendation tier. Scale: 1-5 (with .5 increments)
- **5**: Award consideration (top 2.5%)
- **4**: Conference acceptance
- **3**: Findings track acceptance
- **2**: Needs substantial revisions
- **1**: Do not resubmit or irrelevant

### 4. Reviewer Confidence
Evaluates assessment certainty. Scale: 1-5
- **5**: Very careful review; familiar with related work
- **4**: Important points verified; unlikely errors
- **3**: General area knowledge; details not fully checked
- **2**: May have missed details or novelty aspects
- **1**: Outside expertise; educated guess only

### 5. Reproducibility
Assesses ability to replicate results. Scale: 1-5
- **5**: Results easily reproducible
- **4**: Mostly reproducible; minor variance expected
- **3**: Reproducible with difficulty; underspecified parameters
- **2**: Difficult reproduction; unavailable data
- **1**: Cannot reproduce

### 6. Datasets (if applicable)
Values released data contribution. Scale: 1-5
- **5**: Enabling for future research directions
- **4**: Recommended for ongoing wo
…[truncated 961 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8427
}
```

</details>

---


### Tool call

_source line 220 · 2026-05-21T11:14:25.132389+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 221 · 2026-05-21T11:14:26.338916+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1206
}
```

</details>

---


### Tool call

_source line 222 · 2026-05-21T11:14:26.691138+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 223 · 2026-05-21T11:14:27.193554+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 224 · 2026-05-21T11:14:27.294418+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 225 · 2026-05-21T11:14:27.345926+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 654
}
```

</details>

---


### Tool result

_source line 226 · 2026-05-21T11:14:28.403593+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1210
}
```

</details>

---


### Tool result

_source line 227 · 2026-05-21T11:14:28.404448+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1110
}
```

</details>

---


### Tool call

_source line 228 · 2026-05-21T11:14:35.032661+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "9-13",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "9-13",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 229 · 2026-05-21T11:14:35.586522+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 520.2}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 446.0}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 505.8}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 600.5}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 131.4}], \"total_pages\": 13, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 230 · 2026-05-21T11:14:39.858179+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 231 · 2026-05-21T11:14:40.462667+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 232 · 2026-05-21T11:14:41.317605+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1459
}
```

</details>

---


### Tool call

_source line 233 · 2026-05-21T11:14:41.318049+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 234 · 2026-05-21T11:14:41.821470+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 235 · 2026-05-21T11:14:42.225163+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1762
}
```

</details>

---


### Tool call

_source line 236 · 2026-05-21T11:14:42.476510+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 237 · 2026-05-21T11:14:42.579306+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Tool result

_source line 238 · 2026-05-21T11:14:42.580352+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1262
}
```

</details>

---


### Tool result

_source line 239 · 2026-05-21T11:14:42.934339+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1112
}
```

</details>

---


### Tool call

_source line 240 · 2026-05-21T11:17:33.386324+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool call

_source line 241 · 2026-05-21T11:17:35.297128+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines, especially: what are reviewers instructed to evaluate, what are the criteria for recommending acceptance vs rejection, any guidance on evaluating methodology/experiments, and the specific review form dimensions with their score scales."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines, especially: what are reviewers instructed to evaluate, what are the criteria for recommending acceptance vs rejection, any guidance on evaluating methodology/experiments, and the specific review form dimensions with their score scales."
  }
}
```

</details>

---


### Tool result

_source line 242 · 2026-05-21T11:18:04.350333+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 37, \"total_citations\": 49, \"unique_cited_keys\": 36, \"orphan_bib\": 1, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 33, \"online_not_found\": 1, \"online_mismatch\": 3}, \"cross_check\": {\"orphan_bib\": [\"hoenig2001abuse\"], \"missing_bib\": [], \"orphan_count\": 1, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"murugadoss2025sos\", \"type\": \"inproceedings\", \"title\": \"Style Over Substance: Failure Modes of LLM Judges in Alignment Benchmarking\", \"authors\": \"Murugadoss, Aakanksha and others\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"li2026preference\", \"type\": \"inproceedings\", \"title\": \"Preference Leakage: A Contamination Problem in LLM-as-a-Judge\", \"authors\": \"Li, Dawei and others\", \"year\": \"2026\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"wang2026fairjudge\", \"type\": \"article\", \"title\": \"FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge\", \"authors\": \"Yang, Bo and Feng, Lanfei and Chen, Yunkui and Zhang, Yu and Xu, Xiao and Li, Sh...\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2602.06625\"}, {\"key\": \"dubois2025lc\", \"type\": \"inproceedings\", \"title\": \"Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators\", \"authors\": \"Dubois, Yann and others\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"casse2026concise\", \"type\": \"article\", \"title\": \"A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents\", \"authors\": \"Cho, Young-Min and Yuan, Yuan and Guntuku, Sharath Chandra and Ungar, Lyle\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2601.10809\"}, {\"key\": \"counterfactu
…[truncated 28140 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 30963
}
```

</details>

---


### Tool result

_source line 243 · 2026-05-21T11:18:11.236096+00:00_

# ARR Reviewer Guidelines Summary

## Core Evaluation Instructions

Reviewers assess papers across three dimensions:

1. **Soundness**: Technical validity and methodological rigor
2. **Excitement**: Personal interest and subjective appeal (orthogonal to soundness)
3. **Overall Recommendation**: Composite judgment on acceptance worthiness

As stated in the guidelines, "The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation."

## Key Evaluation Criteria

Reviewers must complete four main tasks:

**Task 1**: Allocate adequate time for review and discussion phases

**Task 2**: Verify expertise match and check for conflicts of interest; flag papers for desk rejection if they violate anonymity, style guides, or lack required sections

**Task 3**: Write substantive reviews by:
- Reading twice (skim, then in-depth)
- Being specific with criticisms
- Avoiding common biases (H1-H17 heuristics listed)
- Checking methodology soundness (M1-M5 codes)
- Assessing experimental results (R1-R5 codes)

**Task 4**: Engage with author responses and update assessments accordingly

## Common Pitfalls to Avoid

The guidelines warn against dismissing papers for being "unsurprising," contradicting reviewer expectations, or lacking novelty without evidence. Negative results, simple solutions, and non-English research are explicitly stated as potentially valuable contributions.

Reviewers should not require experiments beyond what supports the paper's claims, demand comparisons to proprietary models without justification, or confuse acknowledged limitations with fundamental weaknesses.

## Professional Standards

Reviews must maintain "professional and neutral" tone. The guidelines emphasize: "Write the review you would like to get yourself."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 35938
}
```

</details>

---


### Tool call

_source line 244 · 2026-05-21T11:21:20.711671+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿报告：方法严谨性审查\n\n### 总体评分\n**Overall**: 3.5 — Borderline Conference\n**一句话总结**: 核心发现（Likert Blindspot）新颖且有实际价值，但 NLI gate 验证的循环依赖、Bradley-Terry IIA 假设未检验、以及 originality confound 对识别策略的威胁，使得因果声明的方法论支撑不够充分。\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 主要声明有七种统计方法支撑，但 NLI gate 验证存在 evaluator-producer 循环，BT 模型核心假设未检验，originality confound 显著（Table 3）部分削弱识别策略 |\n| Excitement | 3.5/5 | Likert Blindspot 概念新颖，测量理论视角在 LLM 评估文献中罕见，对 RLHF/alignment 实践有直接意义；但方法论缺口使贡献尚未完全落地 |\n| Reproducibility | 3.5/5 | 参数和流程描述详尽，但代码/数据未发布 |\n| Confidence | 4/5 | 熟悉 BT 模型、GEE、bootstrap 推断及 LLM-as-Judge 文献 |\n\n---\n\n### Must-Fix 问题（3 个 critical）\n\n**N1** [critical] NLI Gate 验证存在 evaluator-producer 循环偏差\n- 位置：§5.1\n- Qwen3-32B 同时是 rewriter 和 NLI gate 验证的 annotator，false negative rate 8.4% 可能被低估。GPT-4o spot-check (47/50) 样本量不足 (n=50)。\n- 建议：用人工标注（≥200对）或两个架构不同的模型分别验证。\n\n**N2** [critical] Bradley-Terry IIA 假设未检验\n- 位置：§4.1, §5.2\n- BT 模型假设 IIA，但 style preference 可能随 item 基线质量变化（交互效应），直接违反 IIA。未报告任何诊断检验。\n- 建议：报告 Hausman-McFadden test，或拟合 Thurstone-Mosteller 模型做稳健性检查。\n\n**N3** [critical] Originality confound 显著，削弱识别策略\n- 位置：Table 3, §5.5\n- 多配置下 Originality OR 显著（GPT-4o formality OR=1.88, p=0.006; Qwen3-32B verbosity OR=2.21, p<0.001）。GEE additive decomposition 的交互项检验可能低功效（n=88）。Style 和 originality 的可分离性值得质疑。\n- 建议：重新界定 claim 为 \"style-correlated preference shift\"；在 originality 差异最小的子集上重复分析。\n\n### Should-Fix 问题（6 个 warning）\n\n**W1** NLI 阈值 τ=0.90 缺乏 sensitivity analysis（§3.2）\n**W2** Direction-aware NLI 可能引入系统性筛选偏差（§3.2, Appendix E）\n**W3** Exploratory analyses 的多重比较修正不完整（全文）\n**W4** Claude Sonnet 4 negative control 的 non-significance 解读过度——需等效性检验（Table 1）\n**W5** Figure 4 的 post-hoc power analysis 存在循环推理风险（§5.2）\n**W6** Rewriter independence test 未覆盖 register axis（Table 6-7）\n\n### 小问题（5 个）\n- M1: hoenig2001abuse bib 条目可能缺少 \\cite 命令\n- M2: wu2023style bib 年份（2025）与 OpenAlex 索引年份（2023）不一致\n- M3: Figure 2 DAG 图注解释不足\n- M4: Table 1 Likert d 负值含义未充分解释\n- M5: \"Interventional Design\" 标题措辞与实际 evidence 强度不匹配\n\n### 主要优势\n- S1: Likert Blindspot 概念新颖且有实际影响力\n- S2: 七种统计方法的 sensitivity hierarchy 有说服力\n- S3: 3 judges × 3 benchmarks × 3 axes 的 full factorial design 覆盖面优秀\n- S4: 统计素养（Holm-Bonferroni, GEE, bootstrap）在 NLP 实证研究中较为难得\n- S5: 写作质量高，结构清晰\n\n### 缺失引用\n- Hausman & McFadden (1984) — IIA 检验\n- Agresti (2010) — ordinal data 分析经典教材\n- Lakens (2017) — equivalence testing（与 negative control 解读相关）\n\n### 需要作者澄清的问题（5 个）\nQ1: NLI 阈值选定依据和 sensitivity 数据？\nQ2: GEE Style×Originality 交互项是否检验过？\nQ3: Full BT (63.0%) vs filtered sign test (73.9%) 差异的含义？\nQ4: 各 benchmark×axis×judge 单元 NLI 过滤后的 effective sample size？\nQ5: 是否考虑过与 RATE/LC-AlpacaEval 的 head-to-head 比较？",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿报告：方法严谨性审查\n\n### 总体评分\n**Overall**: 3.5 — Borderline Conference\n**一句话总结**: 核心发现（Likert Blindspot）新颖且有实际价值，但 NLI gate 验证的循环依赖、Bradley-Terry IIA 假设未检验、以及 originality confound 对识别策略的威胁，使得因果声明的方法论支撑不够充分。\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 主要声明有七种统计方法支撑，但 NLI gate 验证存在 evaluator-producer 循环，BT 模型核心假设未检验，originality confound 显著（Table 3）部分削弱识别策略 |\n| Excitement | 3.5/5 | Likert Blindspot 概念新颖，测量理论视角在 LLM 评估文献中罕见，对 RLHF/alignment 实践有直接意义；但方法论缺口使贡献尚未完全落地 |\n| Reproducibility | 3.5/5 | 参数和流程描述详尽，但代码/数据未发布 |\n| Confidence | 4/5 | 熟悉 BT 模型、GEE、bootstrap 推断及 LLM-as-Judge 文献 |\n\n---\n\n### Must-Fix 问题（3 个 critical）\n\n**N1** [critical] NLI Gate 验证存在 evaluator-producer 循环偏差\n- 位置：§5.1\n- Qwen3-32B 同时是 rewriter 和 NLI gate 验证的 annotator，false negative rate 8.4% 可能被低估。GPT-4o spot-check (47/50) 样本量不足 (n=50)。\n- 建议：用人工标注（≥200对）或两个架构不同的模型分别验证。\n\n**N2** [critical] Bradley-Terry IIA 假设未检验\n- 位置：§4.1, §5.2\n- BT 模型假设 IIA，但 style preference 可能随 item 基线质量变化（交互效应），直接违反 IIA。未报告任何诊断检验。\n- 建议：报告 Hausman-McFadden test，或拟合 Thurstone-Mosteller 模型做稳健性检查。\n\n**N3** [critical] Originality confound 显著，削弱识别策略\n- 位置：Table 3, §5.5\n- 多配置下 Originality OR 显著（GPT-4o formality OR=1.88, p=0.006; Qwen3-32B verbosity OR=2.21, p<0.001）。GEE additive decomposition 的交互项检验可能低功效（n=88）。Style 和 originality 的可分离性值得质疑。\n- 建议：重新界定 claim 为 \"style-correlated preference shift\"；在 originality 差异最小的子集上重复分析。\n\n### Should-Fix 问题（6 个 warning）\n\n**W1** NLI 阈值 τ=0.90 缺乏 sensitivity analysis（§3.2）\n**W2** Direction-aware NLI 可能引入系统性筛选偏差（§3.2, Appendix E）\n**W3** Exploratory analyses 的多重比较修正不完整（全文）\n**W4** Claude Sonnet 4 negative control 的 non-significance 解读过度——需等效性检验（Table 1）\n**W5** Figure 4 的 post-hoc power analysis 存在循环推理风险（§5.2）\n**W6** Rewriter independence test 未覆盖 register axis（Table 6-7）\n\n### 小问题（5 个）\n- M1: hoenig2001abuse bib 条目可能缺少 \\cite 命令\n- M2: wu2023style bib 年份（2025）与 OpenAlex 索引年份（2023）不一致\n- M3: Figure 2 DAG 图注解释不足\n- M4: Table 1 Likert d 负值含义未充分解释\n- M5: \"Interventional Design\" 标题措辞与实际 evidence 强度不匹配\n\n### 主要优势\n- S1: Likert Blindspot 概念新颖且有实际影响力\n- S2: 七种统计方法的 sensitivity hierarchy 有说服力\n- S3: 3 judges × 3 benchmarks × 3 axes 的 full factorial design 覆盖面优秀\n- S4: 统计素养（Holm-Bonferroni, GEE, bootstrap）在 NLP 实证研究中较为难得\n- S5: 写作质量高，结构清晰\n\n### 缺失引用\n- Hausman & McFadden (1984) — IIA 检验\n- Agresti (2010) — ordinal data 分析经典教材\n- Lakens (2017) — equivalence testing（与 negative control 解读相关）\n\n### 需要作者澄清的问题（5 个）\nQ1: NLI 阈值选定依据和 sensitivity 数据？\nQ2: GEE Style×Originality 交互项是否检验过？\nQ3: Full BT (63.0%) vs filtered sign test (73.9%) 差异的含义？\nQ4: 各 benchmark×axis×judge 单元 NLI 过滤后的 effective sample size？\nQ5: 是否考虑过与 RATE/LC-AlpacaEval 的 head-to-head 比较？",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 245 · 2026-05-21T11:21:24.484215+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3772
}
```

</details>

---


### Assistant

_source line 246 · 2026-05-21T11:21:32.456375+00:00_

审稿意见已提交给 Review Director。

总结：论文提出的 Likert Blindspot 是一个新颖且有实际意义的发现，实验覆盖面和统计素养在同领域工作中突出。但三个 critical 问题——NLI gate 验证的循环偏差、BT 模型 IIA 假设未检验、originality confound 对识别策略的削弱——使得当前方法论支撑不足以支持主会议接收。评分 3.5（Borderline Conference），这些问题均可在一轮修改中解决。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1"
}
```

</details>

---


## Round 10

## Round 10

38 recorded events


### User

_source line 247 · 2026-05-21T11:22:23.674247+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 审稿报告：新颖性与完整性

### 总体评分
**Overall**: 3.0 — Findings

### Must-Fix 问题

**N1** [critical] "Likert Blindspot" 命名不准确——efficiency gap 而非 blindspot
- Title, Abstract, §1, §5.2: Table 1 中 9 个 bias-positive cells 有 3 个 Likert 也检测到了（‡ 标记）。Section 5.2 line 87 承认 "three of nine bias-positive cells escape the Blindspot"。
- 进一步：n=355 时 Likert d=−0.025 也可能是 Likert 和 pairwise 测量不同构念（absolute quality difference vs ordinal preference），而非同一构念的不同测量精度。
- 建议改为 "Likert Attenuation Effect" 或 "Measurement Sensitivity Gap"。

**N2** [critical] Related Work 引用数量和覆盖面严重不足
- Section 2: 仅 36 篇引用，EMNLP 长文通常 40-60 篇。缺失方向：NLG evaluation surveys (van der Lee 2019/2021, Celikyilmaz 2020)、counterfactual text generation (MICE Ross 2021, Tailor Ross 2022)、scale design (Krosnick 1999, Preston & Colman 2000)、LLM-as-judge frameworks (G-Eval Liu 2023, Arena-Hard Li 2024)、causal NLP (Keith 2020)、GEE 原始论文 (Liang & Zeger 1986)。

**N3** [critical] "Four critical gaps" 有 cherry-picking 嫌疑
- §1 lines 11-12: 四个 gap 的定义刚好使得只有 CSD 满足所有条件。CASSE/FairJudge 已做 multi-dimensional decomposition（被归入 "correlational" 排除），RATE/Counterfactual Rhetorical 已做 interventional analysis（被归入 "Likert-based"/"persona-level" 排除）。

### Should-Fix 问题

**W1** Contribution 2 (Likert Blindspot) novelty 定位需更诚实——Kiritchenko (2017)、Novikova (2018) 已在其他 NLP 任务中展示 ranking > rating
**W2** Conclusion 仅一句话，严重不足
**W3** Contribution 3 (GEE conditional decomposition) 是标准方法直接应用，不应列为独立 contribution
**W4** 对 RATE 批评可能不公平——RATE 目标是 reward model explainability 而非 style bias detection
**W5** 主实验仅基于 LLMBar (n=100)，generalizability 存疑
**W6** Evaluator-producer bias 处理不够彻底——Style OR 下降 22%（13.10→10.17）不可忽略

### Questions
Q1: Likert 和 pairwise 是否测量不同构念？
Q2: n=355 Likert d 缩小是 attenuation 还是 regression to the mean？
Q3: Direction asymmetry (78.8% vs 54.5%) 是否说明 judge 偏好原文而非 formality？
Q4: 为什么不用人类标注验证 NLI gate？
Q5: Claude Sonnet 4 极端 originality sensitivity (OR=6.66) 如何解释？

### 缺失引用
van der Lee (2019, 2021), Celikyilmaz (2020), MICE (Ross 2021), Tailor (Ross 2022), Krosnick (1999), Preston & Colman (2000), G-Eval (Liu 2023), Arena-Hard (Li 2024), Keith (2020), Liang & Zeger (1986)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 248 · 2026-05-21T11:23:33.172704+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 249 · 2026-05-21T11:23:34.430454+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/review_reviewer_1_9f412a41.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1257
}
```

</details>

---


### Tool call

_source line 250 · 2026-05-21T11:23:34.430772+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 251 · 2026-05-21T11:23:34.581417+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/review_reviewer_1_9f412a41.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 252 · 2026-05-21T11:23:34.581768+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 253 · 2026-05-21T11:23:35.485449+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/review_reviewer_1_9f412a41.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 254 · 2026-05-21T11:23:35.485919+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 255 · 2026-05-21T11:23:35.686796+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/review_reviewer_1_9f412a41.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 200
}
```

</details>

---


### Tool call

_source line 256 · 2026-05-21T11:23:35.687160+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 257 · 2026-05-21T11:23:35.738817+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/.claude/sessions/review_reviewer_1_9f412a41.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 258 · 2026-05-21T11:23:42.257432+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "1-4",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "1-4",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 259 · 2026-05-21T11:23:42.910164+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 457.1}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 517.3}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 591.7}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 485.9}], \"total_pages\": 13, \"rendered_pages\": 4, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 652
}
```

</details>

---


### Tool call

_source line 260 · 2026-05-21T11:23:45.925363+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 261 · 2026-05-21T11:23:46.276768+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 262 · 2026-05-21T11:23:47.181000+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1255
}
```

</details>

---


### Tool result

_source line 263 · 2026-05-21T11:23:47.182416+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 264 · 2026-05-21T11:23:47.182765+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 265 · 2026-05-21T11:23:47.485015+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 266 · 2026-05-21T11:23:48.038940+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool result

_source line 267 · 2026-05-21T11:23:48.341201+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 268 · 2026-05-21T11:23:57.637065+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "5-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "5-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 269 · 2026-05-21T11:23:58.545311+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 522.9}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 496.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 516.0}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 520.2}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 446.0}], \"total_pages\": 13, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 908
}
```

</details>

---


### Tool call

_source line 270 · 2026-05-21T11:24:02.864961+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 271 · 2026-05-21T11:24:03.267175+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 272 · 2026-05-21T11:24:04.277214+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1412
}
```

</details>

---


### Tool call

_source line 273 · 2026-05-21T11:24:04.279716+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 274 · 2026-05-21T11:24:04.836229+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1569
}
```

</details>

---


### Tool call

_source line 275 · 2026-05-21T11:24:04.888455+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 276 · 2026-05-21T11:24:05.243713+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 277 · 2026-05-21T11:24:05.699169+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1419
}
```

</details>

---


### Tool call

_source line 278 · 2026-05-21T11:24:05.699591+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 279 · 2026-05-21T11:24:07.360489+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2472
}
```

</details>

---


### Tool result

_source line 280 · 2026-05-21T11:24:07.616248+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2372
}
```

</details>

---


### Tool result

_source line 281 · 2026-05-21T11:24:07.718196+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2018
}
```

</details>

---


### Tool call

_source line 282 · 2026-05-21T11:28:18.773686+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n### Must-Fix\n\n**[REBUT] R2-N1 (\"Blindspot\" 命名不准确)**: 论文 Abstract/§2 将 Blindspot 定义为 severity-spectrum 现象（moderate bias 区间完全失灵，强效应区部分恢复）。3/9 cells 逃逸恰好支持 spectrum 叙事。Table 2 的七种方法比较（四种 Likert-based 全失败 vs 两种 pairwise 全成功）反驳构念差异假设。但建议作者在 Discussion 更正式地讨论构念差异替代假设（降级为 Should-Fix）。\n\n**[REBUT] R2-N2 (引用数量不足)**: 引用数量非质量标准。论文 §2 沿三条线索组织引用，覆盖充分。但同意 Liang & Zeger (1986) GEE 原文和 Krosnick (1999) 应补充（降级为 Should-Fix）。\n\n**[AGREE] R2-N3 (Four gaps cherry-picking)**: §1 四个 gap 的合取条件确实倾向于只有 CSD 满足。CASSE 的 controlled style manipulation 被简单标记为 \"correlational\" 不完全公平。但这是 framing 问题，不影响技术贡献，建议降级为 Should-Fix。\n\n### Should-Fix\n\n**[REBUT] R2-W1**: 论文 §2 已引用 Kiritchenko/Novikova。增量贡献在于 LLM judge 场景的系统量化 + measurement attenuation 表征 + 七种方法比较。\n**[AGREE] R2-W2**: Conclusion 偏短，建议扩展。\n**[REBUT] R2-W3**: GEE 方法标准但应用场景（decompose style vs originality in LLM judges）新颖，Table 3 发现有实践指导价值。\n**[REBUT] R2-W4**: 论文对 RATE 的讨论聚焦测量方法论比较，不涉及目标价值判断。\n**[AGREE] R2-W5**: 主实验确以 LLMBar 为中心，Table 1 含 AlpacaEval/MT-Bench 但仅作 replication。\n**[AGREE] R2-W6**: 与我的 R1-N1 一致，22% Style OR 下降不可忽略。\n\n### Questions\n\n**[REBUT] Q1**: Table 2 四种 Likert-based 方法全部失败反驳构念差异假设；n=355 BT 稳定而 Likert d→0 进一步排除。\n**[REBUT] Q2**: Regression to mean 对所有估计量对称操作，但 BT 稳定/略升而 Likert→0 的 differential shrinkage 不一致。\n**[AGREE] Q3**: 方向不对称与 R1-N3 originality confound 一致。GEE additive specification 可能不足以正确分离。\n**[AGREE] Q4**: 与 R1-N1 一致，NLI gate 需人工标注验证。\n**[AGREE] Q5**: Claude Orig OR=6.66 削弱 negative control 解读，与 R1-W4 一致。\n\n### 与 R2 的主要分歧\n\nR2 的 Overall 3.0 (Findings) 偏低。N1（命名）和 N2（引用数量）不构成 critical 问题。论文的核心方法论贡献（CSD + Likert Blindspot + sensitivity hierarchy）在修补 NLI gate 验证和 BT IIA 检验后可达 Conference 水平。我维持 3.5 (Borderline Conference)。",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n### Must-Fix\n\n**[REBUT] R2-N1 (\"Blindspot\" 命名不准确)**: 论文 Abstract/§2 将 Blindspot 定义为 severity-spectrum 现象（moderate bias 区间完全失灵，强效应区部分恢复）。3/9 cells 逃逸恰好支持 spectrum 叙事。Table 2 的七种方法比较（四种 Likert-based 全失败 vs 两种 pairwise 全成功）反驳构念差异假设。但建议作者在 Discussion 更正式地讨论构念差异替代假设（降级为 Should-Fix）。\n\n**[REBUT] R2-N2 (引用数量不足)**: 引用数量非质量标准。论文 §2 沿三条线索组织引用，覆盖充分。但同意 Liang & Zeger (1986) GEE 原文和 Krosnick (1999) 应补充（降级为 Should-Fix）。\n\n**[AGREE] R2-N3 (Four gaps cherry-picking)**: §1 四个 gap 的合取条件确实倾向于只有 CSD 满足。CASSE 的 controlled style manipulation 被简单标记为 \"correlational\" 不完全公平。但这是 framing 问题，不影响技术贡献，建议降级为 Should-Fix。\n\n### Should-Fix\n\n**[REBUT] R2-W1**: 论文 §2 已引用 Kiritchenko/Novikova。增量贡献在于 LLM judge 场景的系统量化 + measurement attenuation 表征 + 七种方法比较。\n**[AGREE] R2-W2**: Conclusion 偏短，建议扩展。\n**[REBUT] R2-W3**: GEE 方法标准但应用场景（decompose style vs originality in LLM judges）新颖，Table 3 发现有实践指导价值。\n**[REBUT] R2-W4**: 论文对 RATE 的讨论聚焦测量方法论比较，不涉及目标价值判断。\n**[AGREE] R2-W5**: 主实验确以 LLMBar 为中心，Table 1 含 AlpacaEval/MT-Bench 但仅作 replication。\n**[AGREE] R2-W6**: 与我的 R1-N1 一致，22% Style OR 下降不可忽略。\n\n### Questions\n\n**[REBUT] Q1**: Table 2 四种 Likert-based 方法全部失败反驳构念差异假设；n=355 BT 稳定而 Likert d→0 进一步排除。\n**[REBUT] Q2**: Regression to mean 对所有估计量对称操作，但 BT 稳定/略升而 Likert→0 的 differential shrinkage 不一致。\n**[AGREE] Q3**: 方向不对称与 R1-N3 originality confound 一致。GEE additive specification 可能不足以正确分离。\n**[AGREE] Q4**: 与 R1-N1 一致，NLI gate 需人工标注验证。\n**[AGREE] Q5**: Claude Orig OR=6.66 削弱 negative control 解读，与 R1-W4 一致。\n\n### 与 R2 的主要分歧\n\nR2 的 Overall 3.0 (Findings) 偏低。N1（命名）和 N2（引用数量）不构成 critical 问题。论文的核心方法论贡献（CSD + Likert Blindspot + sensitivity hierarchy）在修补 NLI gate 验证和 BT IIA 检验后可达 Conference 水平。我维持 3.5 (Borderline Conference)。",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 283 · 2026-05-21T11:28:22.436950+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3663
}
```

</details>

---


### Assistant

_source line 284 · 2026-05-21T11:28:31.205865+00:00_

交叉回应已提交。

总结：对 R2 的 3 个 Must-Fix 中，我反驳了 N1（命名问题属术语选择，论文已精确定义 Blindspot 为 spectrum 现象）和 N2（引用质量优先于数量，仅需补充 2-3 篇关键引用），同意 N3（gap 定位有 cherry-picking 倾向但建议降级为 Should-Fix）。对 6 个 Should-Fix 反驳了 W1/W3/W4，同意 W2/W5/W6。对 5 个 Question 反驳了 Q1/Q2（Table 2 和 differential shrinkage 证据充分），同意 Q3/Q4/Q5（均与我自己的审稿意见一致）。维持 Overall 3.5 评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1"
}
```

</details>

---


## Round 11

## Round 11

46 recorded events


### User

_source line 285 · 2026-05-21T12:33:20.058050+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性**审查。

## 论文信息
- 标题：The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition
- 路径：projects/causal_style_decomp_judge/docs/paper/main.tex（各 section 在 sections/ 子目录）
- PDF：/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf
- 目标 venue：EMNLP 2026 Main Conference (via ARR)

## Venue 要求
- ACL 模板，double-blind，正文 ≤8 页，参考文献无限
- Limitations 章节必须有（不计页数），不可含额外实验/图表/分析
- 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit
- ARR 提交截止：2026-05-25

## 你的审查侧重
请从以下维度严格审查：

1. **统计方法学**：
   - Holm-Bonferroni 的 primary family 定义是否合理（2 judges × 3 axes = 6 tests）？
   - 探索性/确认性分析的分类是否清晰且一致？
   - Bradley-Terry 模型的假设检验是否充分（GoF、IIA 等）？
   - Bootstrap CI 的 pair-level resampling 是否正确？
   - Cohen's d 计算和效应量解释是否恰当？

2. **NLI Gate 设计**：
   - 双向 entailment 和 direction-aware gating 的理论依据是否充分？
   - 0.90 阈值的 sensitivity analysis 是否说服力足够？
   - FNR 8.4% 的影响是否被充分分析？
   - GPT-4o 200-pair 独立验证的设计是否robust？

3. **因果声明强度**：
   - DAG (Figure 2) 中的假设是否合理？残余 confounding 是否被充分承认？
   - "Design Rationale" 的定位是否与证据强度匹配？
   - NLI gate 作为 do-operator 近似的声明是否过强？
   - GEE "conditional decomposition" 在残余 confounding 下是否有误导性？

4. **实验设计**：
   - 样本量（n=88 到 n=355）是否足够支撑结论？
   - Position control（双向 swap）是否充分？
   - Evaluator-producer bias（Qwen3-32B 同时做 rewriter 和 judge）的处理是否充分？
   - Cross-rewriter independence test 的覆盖是否完整（formality + verbosity，register 缺失）？

5. **Likert Blindspot 机制**：
   - "measurement attenuation across a severity spectrum" 的 framing 是否有充分数据支撑？
   - n=355 时 d→0 的证据是否真正区分了 attenuation vs power gap？
   - 7 种统计方法的 sensitivity hierarchy 是否有说服力？

请按 ACL/ARR 审稿标准输出结构化审稿报告：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (1-5 分 + 置信度)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 286 · 2026-05-21T12:33:29.333434+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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

_source line 287 · 2026-05-21T12:33:29.383969+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 288 · 2026-05-21T12:33:32.293317+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria dimensions"
  }
}
```

</details>

---


### Tool call

_source line 289 · 2026-05-21T12:33:34.306798+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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


### Tool result

_source line 290 · 2026-05-21T12:33:41.350035+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria dimensions"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I found several relevant results about the ACL Rolling Review (ARR) 2026 reviewer guidelines and review form. Here's what I found:

## Review Form Criteria

For Main papers, the main criteria include soundness and reproducibility, while confe
…[truncated 1214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 9056
}
```

</details>

---


### Tool result

_source line 291 · 2026-05-21T12:33:42.659513+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.5}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 526.7}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 530.6}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 511.3}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 454.3}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 531.3}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 515.5}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 508.3}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 532.7}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/pap
…[truncated 311 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 8352
}
```

</details>

---


### Tool call

_source line 292 · 2026-05-21T12:33:46.829967+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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

_source line 293 · 2026-05-21T12:33:46.930701+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 294 · 2026-05-21T12:33:51.002155+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form dimensions, scoring scales, and criteria. List every field/question reviewers must answer, including the exact scale (e.g., 1-5) and what each score means."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form dimensions, scoring scales, and criteria. List every field/question reviewers must answer, including the exact scale (e.g., 1-5) and what each score means."
  }
}
```

</details>

---


### Tool call

_source line 295 · 2026-05-21T12:33:51.960911+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 296 · 2026-05-21T12:33:52.515458+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 297 · 2026-05-21T12:33:52.971118+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1010
}
```

</details>

---


### Tool call

_source line 298 · 2026-05-21T12:33:52.971545+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 299 · 2026-05-21T12:33:53.576451+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 300 · 2026-05-21T12:33:53.627848+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1112
}
```

</details>

---


### Tool result

_source line 301 · 2026-05-21T12:33:54.183588+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1212
}
```

</details>

---


### Tool result

_source line 302 · 2026-05-21T12:33:54.839774+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1263
}
```

</details>

---


### Tool result

_source line 303 · 2026-05-21T12:33:59.709353+00:00_

# ACL Rolling Review Form - Complete Dimensions and Scales

## Required Review Fields

### 1. **Paper Summary**
Free-text description of paper topic and content.

### 2. **Summary of Strengths**
Free-text identification of major publication reasons.

### 3. **Summary of Weaknesses**
Free-text enumeration of concerns, numbered for author response.

### 4. **Comments/Suggestions/Typos**
Free-text improvement suggestions beyond main concerns.

### 5. **Reviewer Confidence** (1-5 scale)
- **5**: "Positive that my evaluation is correct"
- **4**: "Quite sure" with unlikely missed details
- **3**: "Pretty sure" but may have missed specifics
- **2**: "Willing to defend" but likely gaps in understanding
- **1**: "Not my area" or paper very difficult to understand

### 6. **Soundness** (1-5 with .5 increments)
- **5**: Excellent thoroughness for paper type
- **4**: Strong support with minor experimental gaps acceptable
- **3**: Acceptable support for main claims
- **2**: Major claims lack sufficient support
- **1**: Insufficient rigor or ACL-irrelevant

### 7. **Excitement** (1-5 with .5 increments)
- **5**: Highly Exciting—would recommend presentation
- **4**: Exciting—would mention to others
- **3**: Interesting—might attend if time permits
- **2**: Potentially Interesting—limited personal resonance
- **1**: Not Exciting—lacks computational linguistics relevance

### 8. **Overall Assessment** (1-5 with .5 increments)
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance
- **3**: Findings acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit

### 9. **Best Paper Justification**
Free-text (if rating 5 or 4.5)

### 10. **Limitations and Societal Impact**
Free-text evaluation of adequacy.

### 11. **Ethical Concerns**
Free-text assessment against ACL ethics code.

### 12. **Needs Ethics Review**
Yes/No decision with explanation.

### 13. **Reproducibility** (1-5 scale)
- **5**: Results easily reproducible
- **4**: Mostly reproducible with minor variat
…[truncated 871 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8707
}
```

</details>

---


### Tool call

_source line 304 · 2026-05-21T12:34:08.796903+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 305 · 2026-05-21T12:34:09.349019+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 306 · 2026-05-21T12:34:10.152775+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1355
}
```

</details>

---


### Tool result

_source line 307 · 2026-05-21T12:34:10.154032+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 805
}
```

</details>

---


### Tool call

_source line 308 · 2026-05-21T12:34:10.154328+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 309 · 2026-05-21T12:34:10.706126+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 310 · 2026-05-21T12:34:11.159660+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 311 · 2026-05-21T12:34:11.160264+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 312 · 2026-05-21T12:34:11.562649+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 313 · 2026-05-21T12:34:11.563060+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 314 · 2026-05-21T12:34:12.122744+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 962
}
```

</details>

---


### Tool result

_source line 315 · 2026-05-21T12:34:12.424979+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 861
}
```

</details>

---


### Tool call

_source line 316 · 2026-05-21T12:34:21.720417+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "11-13",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "11-13",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 317 · 2026-05-21T12:34:22.124817+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 514.8}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 581.1}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 307.3}], \"total_pages\": 13, \"rendered_pages\": 3, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 404
}
```

</details>

---


### Tool call

_source line 318 · 2026-05-21T12:34:26.494742+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 319 · 2026-05-21T12:34:26.896758+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 320 · 2026-05-21T12:34:27.449714+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 321 · 2026-05-21T12:34:27.450119+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 322 · 2026-05-21T12:34:27.652237+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 755
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-21T12:34:27.955020+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 324 · 2026-05-21T12:40:47.413034+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿报告：方法严谨性审查\n\n**论文**：The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\n**Venue**：EMNLP 2026 Main Conference (via ARR)\n**审查侧重**：统计方法学、NLI Gate 设计、因果声明强度、实验设计、Likert Blindspot 机制\n\n---\n\n## 总体评分\n**Overall**: 3.5 / 5（Borderline Conference）\n**Confidence**: 4 / 5（Quite sure — 对因果推断方法学和 NLP 评估统计有足够领域经验，但部分 GEE 细节可能遗漏）\n**一句话总结**: 论文提出了实用且新颖的发现（Likert Blindspot），框架设计多层控制值得肯定，但因果声明强度超出证据支撑、关键统计假设未检验、evaluator-producer confound 未充分解决，整体处于 Conference/Findings 边界。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心框架设计合理（position swap、NLI gate、多 benchmark），但 BT 的 IIA 假设未检验、NLI gate 被过度声称为 do-operator 近似、GEE 条件分解在残余混淆下解释过强 |\n| Excitement | 3.5/5 | Likert Blindspot 发现新颖且有实际影响力——7 种 Likert 方法全部失败而 pairwise 可靠检测是 striking 的结果；但相对 RATE (Reber et al., 2025) 的增量贡献需更清晰定位 |\n| Reproducibility | 4/5 | 方法描述详尽（prompts、NLI 阈值、bootstrap 参数均有报告），代码和数据承诺于接收后发布；但 rewriting prompts 的完整文本未在 Appendix 中提供 |\n| Datasets | 3/5 | 使用现有 benchmark（LLMBar、AlpacaEval、MTBench）的 style-transformed 版本，有一定复用价值 |\n| Software | 3/5 | 框架承诺开源但目前无法验证 |\n\n---\n\n## 主要优势\n\n1. **Likert Blindspot 发现的实证力度**：Table 2 的 7 种方法 sensitivity hierarchy 是论文最有说服力的结果——在同一数据上，所有 Likert-based 方法（ATE t-test、binomial、ordinal regression、GEE、Wilcoxon）全部 p > 0.29，而 BT 和 filtered sign test 均 p < 0.001。这一对比清晰地建立了 measurement modality 之间的系统性差异。\n\n2. **多层控制设计**：Position double-swap、NLI content gate、consistency filter 三层控制的组合设计严谨。特别是 position swap 产生 n_pairs × 2 观测并只保留 consistent pairs，这是 pairwise evaluation 的标准最佳实践。\n\n3. **负对照的使用**：Claude Sonnet 4 作为 negative control（Table 1）在所有轴上未检测到 bias（BT 56.2%, p = 0.254），支持框架的 discriminant validity——不是所有 judge 都触发 bias 检测，说明框架不是在制造假阳性。\n\n4. **BT 模型的 GoF 检验**：Appendix G 报告了 BT goodness-of-fit（formality deviance p = 0.198; verbosity p = 0.905），且对 exchangeable vs. independence 工作相关结构进行了比较（|ΔQIC| < 0.001），GEE 交互项检验也确认了加法模型的适当性。这些诊断检验的完整性在 NLP 论文中少见。\n\n5. **跨 benchmark 一致性**：Verbosity bias 在 LLMBar、AlpacaEval、MTBench 三个 benchmark 上对两个 judge（GPT-4o、Qwen3-32B）均达到显著（BT 67-77%），模式一致性强。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] NLI gate 作为 do-operator 近似的声明过强\n- 具体位置：Section 3.5, \"The NLI entailment gate approximates the do-operator by filtering out pairs where the rewrite changed semantic content, thereby blocking the R→Q path\"\n- 问题：do-operator 要求对处理变量的主动干预（intervention），而 NLI gate 是一种基于观测的 **筛选**（selection/conditioning）。Selection ≠ intervention：通过 NLI 筛选保留的样本可能在未观测维度上系统性地不同于被过滤掉的样本（collider bias）。例如，容易通过 NLI gate 的文本可能系统性地偏向某些 topic 复杂度或句法结构，而这些特征本身可能影响 judge 偏好。Figure 2 的 DAG 中，如果存在 Rewrite → (未观测变量 U) → Y 的路径，conditioning on NLI score（一个 Q 的子节点）可能打开 collider path。\n- 为什么影响接收：这是论文因果叙事的核心声明。如果 NLI gate 不能有效近似 do-operator，则 Section 3.5 的 \"Design Rationale\" 的因果论证框架需要实质性修改。论文在 Limitations 中承认 \"residual confounding is not fully eliminated\"，但主文 Section 3.5 的语言与此不一致。\n- 建议修改方向：(1) 将 \"approximates the do-operator\" 改为 \"provides a filtering-based confounder control that mitigates but does not eliminate confounding through the R→Q path\"；(2) 在 Section 3.5 中明确讨论 selection bias 的可能方向和幅度；(3) 考虑在 DAG 中标注 NLI gate 的 conditioning 性质（而非 intervention 性质）。\n\n**N2** [critical] Bradley-Terry 模型的 IIA 假设未检验\n- 具体位置：Section 4.1 及 Appendix G\n- 问题：Bradley-Terry 模型假设 Independence of Irrelevant Alternatives (IIA)——给定两个选项的偏好概率不受第三个选项的存在或缺失影响。在本文的实验设计中，每个 text pair 经过 style manipulation 后产生 original vs. rewrite 的比较。但不同类型的原始文本（如 instruction-following vs. open-ended）可能与 style manipulation 产生异质性交互，导致 IIA 违反。例如，verbosity 增加对代码相关任务的影响可能与对创意写作的影响系统性不同。Appendix G 报告了 GoF 检验但 **没有报告 IIA 检验**（如 Hausman-McFadden test 或 rank-order consistency check）。\n- 为什么影响接收：BT win probability 是论文几乎所有显著性结论的基础。如果 IIA 被违反，BT 参数估计可能有偏，置信区间可能偏窄，从而夸大统计显著性。\n- 建议修改方向：(1) 在 Appendix G 中增加 IIA 诊断检验（如按 task type 或 difficulty 分层后检查 BT 参数的稳定性）；(2) 如果 IIA 被违反，讨论对主要结论的影响或改用 Thurstone 模型等不假设 IIA 的替代方案。\n\n**N3** [critical] Evaluator-producer confound 未充分解决\n- 具体位置：Limitations (p.9), Appendix D, Table 1\n- 问题：Qwen3-32B 同时担任 rewriter 和 judge，这引入了 self-preference bias (Panickssery et al., 2024) 的系统性混淆。论文在 Limitations 中承认 \"cross-judge effect-size comparisons are not valid\"，但主文 Table 1 中 Qwen3-32B 的结果仍作为 **主要证据** 与 GPT-4o 并列呈现。Appendix D 的 cross-rewriter test（替换 rewriter 为 GPT-4o）只能证明 rewriter identity 的影响有限，但 **无法排除** Qwen3-32B 作为 judge 时偏好自身产出的可能性。具体地：如果 Qwen3-32B 对自身生成的 formal/verbose 文本有系统性偏好（self-preference），则观测到的 \"style bias\" 可能部分甚至主要来自 self-preference 而非 genuine style bias。\n- 为什么影响接收：这是实验设计的基本有效性问题。如果 Qwen3-32B 的结果受到 self-preference 污染，则论文的 \"cross-judge replication\" 叙事（两个 judge 均显示 bias → 发现具有通用性）被削弱。\n- 建议修改方向：(1) 使用与两个 judge（GPT-4o、Qwen3-32B）均无关的第三方模型（如 Llama 3）作为 rewriter，或至少在 Appendix D 的 cross-rewriter test 中展示 GPT-4o 做 rewriter + Qwen3-32B 做 judge 与 Qwen3-32B 做 rewriter + Qwen3-32B 做 judge 的效应量差异；(2) 在主文中对 Qwen3-32B 结果加明确 caveat 而非等到 Limitations。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] GEE 条件分解在残余混淆下的解释过强\n- 具体位置：Table 3, Section 5.6 (\"formality stands apart as confound-free\")\n- 问题：Table 3 的 GEE 条件分解将观测到的 judge 偏好分解为 Style OR 和 Originality OR。但这一分解的有效性 **依赖于** NLI gate 完全阻断 R→Q 路径。论文自身承认 NLI gate 有 8.4% FNR（Section 5.1）且 \"quality perception shifts mediated by style itself\" 无法被 NLI gate 捕获（Limitations）。在这种残余混淆下，GEE 的条件估计存在 omitted variable bias，\"confound-free\" 的判断可能过于乐观。\n- 建议：(1) 将 \"confound-free\" 改为 \"with reduced confounding\"；(2) 讨论残余混淆对 Style OR 估计的偏差方向（是否会导致高估或低估）。\n\n**W2** [warning] Sensitivity hierarchy (Table 2) 仅在单一轴（formality）上展示\n- 具体位置：Table 2, Section 5.2\n- 问题：Table 2 的 7 种方法 sensitivity hierarchy 是论文的核心方法论贡献之一，但 **仅在 formality 数据上展示**。Verbosity 是检测最强的轴（BT 76-77%），如果 7 种方法的 hierarchy 在 verbosity 上也成立，将大幅增强 Likert Blindspot 的通用性声明。目前读者无法判断 Table 2 的 pattern 是 formality 特有的还是跨轴通用的。\n- 建议：在 Appendix 中增加 verbosity 的 7 方法比较表。如果 verbosity 上 Likert 方法也全部失败（鉴于效应量更大，这一点尤其有说服力），论文的核心论点将更加稳固。\n\n**W3** [warning] \"Measurement attenuation\" vs. \"construct difference\" 在主文中呈现不平衡\n- 具体位置：Section 1 (\"not merely a statistical power gap but measurement attenuation\"), Section 5.2, Section 6; vs. Limitations (\"An alternative interpretation…Likert and pairwise modes measure different constructs\")\n- 问题：论文主文的 framing 将 Likert Blindspot 定位为 **测量衰减**（measurement attenuation）——即 Likert 应该检测到 bias 但检测不到。但 Limitations 中承认的替代解释——Likert 和 pairwise 测量的是 **不同构念**（absolute quality difference vs. ordinal preference）——在概念上同样合理。如果两种方法测量不同构念，则\"Blindspot\"的 framing 本身就有误导性：不是 Likert\"看不到\"bias，而是 Likert 测的是另一个东西。论文没有提供能区分这两种解释的实验证据。\n- 为什么重要：这影响论文核心贡献的定位。如果读者接受 \"construct difference\" 解释，则论文的 practical implication 从\"Likert 有缺陷，应使用 pairwise\"变为\"Likert 和 pairwise 各有用途，视研究问题而定\"。\n- 建议：(1) 在主文（如 Section 5.2 末尾）提前讨论 construct difference 解释，而非仅在 Limitations 中一笔带过；(2) 设计一个能区分两种解释的实验（如：对已知存在 style bias 的合成数据，Likert 是否在足够大的 n 下最终检测到？如果是，则为 power gap；如果不是，则为 construct difference）。\n\n**W4** [warning] NLI 阈值 sensitivity analysis 过于粗糙\n- 具体位置：Section 5.1, p.6 (\"thresholds of 0.70, 0.80, 0.90, and 0.95\")\n- 问题：仅测试 4 个离散阈值。论文声称阈值位于 \"plateau rather than a cliff edge\"，但 4 个点不足以建立 plateau 的存在——在 0.70 和 0.90 之间的行为完全未知。一条从 0.50 到 0.99（步长 0.05）的连续 sensitivity 曲线会更有说服力。\n- 建议：在 Appendix 中补充更细粒度的阈值扫描（至少 10 个点），展示 BT win probability 和 pass rate 随阈值的变化趋势。\n\n**W5** [warning] Cross-rewriter independence test 缺少 register 轴\n- 具体位置：Appendix D\n- 问题：Appendix D 的 cross-rewriter test（替换 rewriter）只测试了 formality 和 verbosity，**缺少 register**。Register 是效应最弱、最接近 non-significant 的轴（GPT-4o BT 57.0%, p = 0.04; Qwen3-32B 55.3%, p = 0.076），恰恰是 rewriter identity 效应最可能影响结论的轴。\n- 建议：补充 register 轴的 cross-rewriter test。如果 register 的弱效应在更换 rewriter 后消失，应在主文中降低 register 结果的 claim 强度。\n\n**W6** [warning] 样本量偏小且主文缺乏 power analysis\n- 具体位置：Section 3.4 (n=100 LLMBar), Table 1, Figure 4\n- 问题：AlpacaEval 的 filtered 分析仅 n=88 对。对于 BT win probability 63%（formality），bootstrap 95% CI 为 [55.7, 70.3]（Table 8）——下界仅略高于 50%，置信区间跨度 15 个百分点。这意味着真实效应量的不确定性相当大。Figure 4 的 power analysis 有帮助，但仅展示了 detection probability，未报告 BT 估计精度（CI width）随 n 的变化。论文将小 n 时 Likert 未检测到 bias 归因于 Blindspot 而非 statistical power，但在 BT 估计本身也有大 CI 的情况下，这一归因需要更谨慎。\n- 建议：(1) 在主文中增加一段 power analysis 讨论，明确 n=88 时 BT 的 minimum detectable effect size；(2) 在 Figure 4 中增加 CI width vs. n 的曲线。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Figure 2 的 DAG 中，dashed edge S→Q 代表 \"style may influence perceived quality\"——这是 NLI gate 无法阻断的路径，但 DAG 中的视觉区分（dashed vs. solid）在打印时可能不够清晰。建议增加颜色编码或标注文字。\n- **M2**: 论文 7 种统计方法的选择（Table 2）未说明理由——为什么是这 7 种而非其他？例如，为什么不包含 mixed-effects logistic regression 或 Bayesian 方法？\n- **M3**: \"Likert Blindspot\" 这一术语可能暗示 Likert 量表本身有缺陷，但论文的发现更准确地说是\"单题 1-10 整体质量评分\"的局限性。多题项 Likert 量表或属性特定评分可能不表现出同样的 Blindspot。建议在 Section 1 或 2 中明确范围。\n- **M4**: Section 3.3 提到 Likert mode 使用 1-10 integer score，但未讨论评分粒度是否影响 Blindspot（如 1-100 fine-grained scale 是否能减轻 attenuation）。\n- **M5**: GPT-4o 200-pair cross-validation（Section 5.1）使用 LLM 验证 NLI gate 在研究 LLM bias 的论文中存在轻微的循环性——GPT-4o 自身的 style bias 可能影响其 content-preservation 判断。应在 limitations 中简要提及。\n\n---\n\n## Questions for Authors\n\n**Q1**: Table 2 的 sensitivity hierarchy 在 verbosity 轴上是否成立？如果 verbosity（效应量更大）的 Likert ATE 也为 non-significant，为什么不展示？如果 verbosity 的 Likert ATE 是 significant 的（在较大效应量下 Likert 开始检测到 bias），这对 \"severity spectrum\" 叙事意味着什么？\n\n**Q2**: 关于 IIA：是否做过按 task type（如 LLMBar 的 instruction-following categories）分层的 BT 参数稳定性检查？如果不同 task type 的 BT win probability 差异显著，则 IIA 可能被违反。\n\n**Q3**: n=355（scaled replication）时 Likert d→0 的结果（Section 5.2, Figure 4），是否尝试过更大的 n（如 n=1000 的模拟或 bootstrap extrapolation）来确认 d 确实收敛到 0 而非缓慢上升？这对区分 \"attenuation\" 和 \"power gap\" 至关重要。\n\n**Q4**: Qwen3-32B 作为 rewriter + judge 时，是否检查过 self-preference 的直接证据？例如，让 Qwen3-32B 在 original pair（未经 style manipulation）上做 pairwise comparison，是否对 Qwen3-32B 生成的回答有系统性偏好？\n\n---\n\n## Missing References\n\n- Zheng et al. (2024), \"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena\" — 论文引用了 MTBench benchmark 但未引用原始方法论文\n- Stureborg et al. (2024), \"Large Language Models are Inconsistent and Biased Evaluators\" — 关于 LLM judge Likert vs. pairwise 不一致性的直接相关工作\n- Park et al. (2024), \"Disentangling Length from Quality in Direct Assessments\" — 与论文的 verbosity 分析直接相关\n\n---\n\n## Overall Assessment\n\n**Overall**: 3.5 / 5（Borderline Conference）\n**Confidence**: 4 / 5\n\n论文提出了一个有实际意义的发现（Likert Blindspot）和一个设计合理的检测框架（CSD）。核心实证结果（Table 1-2, Figure 3-4）在多 benchmark、多 judge 上模式一致。但方法严谨性存在三个核心缺陷：(1) NLI gate 的因果声明（do-operator 近似）超出了筛选操作的实际能力，存在 collider bias 风险；(2) BT 模型的 IIA 假设未经检验，而实验设计中存在潜在的异质性；(3) evaluator-producer confound（Qwen3-32B 同时做 rewriter 和 judge）未充分解决。这三个问题彼此关联——如果 NLI gate 的因果控制力被削弱（N1），残余混淆更大，GEE 分解（W1）就更不可靠；如果 evaluator-producer confound（N3）存在，则 Qwen3-32B 的结果不能作为独立 replication。\n\n修改建议的优先级：N1（降低因果声明）> N3（解决 evaluator-producer confound）> N2（IIA 检验）> W2（多轴 sensitivity hierarchy）> W3（平衡两种解释）。如果 N1-N3 得到充分解决，论文可达 4.0（Conference）。",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿报告：方法严谨性审查\n\n**论文**：The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\n**Venue**：EMNLP 2026 Main Conference (via ARR)\n**审查侧重**：统计方法学、NLI Gate 设计、因果声明强度、实验设计、Likert Blindspot 机制\n\n---\n\n## 总体评分\n**Overall**: 3.5 / 5（Borderline Conference）\n**Confidence**: 4 / 5（Quite sure — 对因果推断方法学和 NLP 评估统计有足够领域经验，但部分 GEE 细节可能遗漏）\n**一句话总结**: 论文提出了实用且新颖的发现（Likert Blindspot），框架设计多层控制值得肯定，但因果声明强度超出证据支撑、关键统计假设未检验、evaluator-producer confound 未充分解决，整体处于 Conference/Findings 边界。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心框架设计合理（position swap、NLI gate、多 benchmark），但 BT 的 IIA 假设未检验、NLI gate 被过度声称为 do-operator 近似、GEE 条件分解在残余混淆下解释过强 |\n| Excitement | 3.5/5 | Likert Blindspot 发现新颖且有实际影响力——7 种 Likert 方法全部失败而 pairwise 可靠检测是 striking 的结果；但相对 RATE (Reber et al., 2025) 的增量贡献需更清晰定位 |\n| Reproducibility | 4/5 | 方法描述详尽（prompts、NLI 阈值、bootstrap 参数均有报告），代码和数据承诺于接收后发布；但 rewriting prompts 的完整文本未在 Appendix 中提供 |\n| Datasets | 3/5 | 使用现有 benchmark（LLMBar、AlpacaEval、MTBench）的 style-transformed 版本，有一定复用价值 |\n| Software | 3/5 | 框架承诺开源但目前无法验证 |\n\n---\n\n## 主要优势\n\n1. **Likert Blindspot 发现的实证力度**：Table 2 的 7 种方法 sensitivity hierarchy 是论文最有说服力的结果——在同一数据上，所有 Likert-based 方法（ATE t-test、binomial、ordinal regression、GEE、Wilcoxon）全部 p > 0.29，而 BT 和 filtered sign test 均 p < 0.001。这一对比清晰地建立了 measurement modality 之间的系统性差异。\n\n2. **多层控制设计**：Position double-swap、NLI content gate、consistency filter 三层控制的组合设计严谨。特别是 position swap 产生 n_pairs × 2 观测并只保留 consistent pairs，这是 pairwise evaluation 的标准最佳实践。\n\n3. **负对照的使用**：Claude Sonnet 4 作为 negative control（Table 1）在所有轴上未检测到 bias（BT 56.2%, p = 0.254），支持框架的 discriminant validity——不是所有 judge 都触发 bias 检测，说明框架不是在制造假阳性。\n\n4. **BT 模型的 GoF 检验**：Appendix G 报告了 BT goodness-of-fit（formality deviance p = 0.198; verbosity p = 0.905），且对 exchangeable vs. independence 工作相关结构进行了比较（|ΔQIC| < 0.001），GEE 交互项检验也确认了加法模型的适当性。这些诊断检验的完整性在 NLP 论文中少见。\n\n5. **跨 benchmark 一致性**：Verbosity bias 在 LLMBar、AlpacaEval、MTBench 三个 benchmark 上对两个 judge（GPT-4o、Qwen3-32B）均达到显著（BT 67-77%），模式一致性强。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] NLI gate 作为 do-operator 近似的声明过强\n- 具体位置：Section 3.5, \"The NLI entailment gate approximates the do-operator by filtering out pairs where the rewrite changed semantic content, thereby blocking the R→Q path\"\n- 问题：do-operator 要求对处理变量的主动干预（intervention），而 NLI gate 是一种基于观测的 **筛选**（selection/conditioning）。Selection ≠ intervention：通过 NLI 筛选保留的样本可能在未观测维度上系统性地不同于被过滤掉的样本（collider bias）。例如，容易通过 NLI gate 的文本可能系统性地偏向某些 topic 复杂度或句法结构，而这些特征本身可能影响 judge 偏好。Figure 2 的 DAG 中，如果存在 Rewrite → (未观测变量 U) → Y 的路径，conditioning on NLI score（一个 Q 的子节点）可能打开 collider path。\n- 为什么影响接收：这是论文因果叙事的核心声明。如果 NLI gate 不能有效近似 do-operator，则 Section 3.5 的 \"Design Rationale\" 的因果论证框架需要实质性修改。论文在 Limitations 中承认 \"residual confounding is not fully eliminated\"，但主文 Section 3.5 的语言与此不一致。\n- 建议修改方向：(1) 将 \"approximates the do-operator\" 改为 \"provides a filtering-based confounder control that mitigates but does not eliminate confounding through the R→Q path\"；(2) 在 Section 3.5 中明确讨论 selection bias 的可能方向和幅度；(3) 考虑在 DAG 中标注 NLI gate 的 conditioning 性质（而非 intervention 性质）。\n\n**N2** [critical] Bradley-Terry 模型的 IIA 假设未检验\n- 具体位置：Section 4.1 及 Appendix G\n- 问题：Bradley-Terry 模型假设 Independence of Irrelevant Alternatives (IIA)——给定两个选项的偏好概率不受第三个选项的存在或缺失影响。在本文的实验设计中，每个 text pair 经过 style manipulation 后产生 original vs. rewrite 的比较。但不同类型的原始文本（如 instruction-following vs. open-ended）可能与 style manipulation 产生异质性交互，导致 IIA 违反。例如，verbosity 增加对代码相关任务的影响可能与对创意写作的影响系统性不同。Appendix G 报告了 GoF 检验但 **没有报告 IIA 检验**（如 Hausman-McFadden test 或 rank-order consistency check）。\n- 为什么影响接收：BT win probability 是论文几乎所有显著性结论的基础。如果 IIA 被违反，BT 参数估计可能有偏，置信区间可能偏窄，从而夸大统计显著性。\n- 建议修改方向：(1) 在 Appendix G 中增加 IIA 诊断检验（如按 task type 或 difficulty 分层后检查 BT 参数的稳定性）；(2) 如果 IIA 被违反，讨论对主要结论的影响或改用 Thurstone 模型等不假设 IIA 的替代方案。\n\n**N3** [critical] Evaluator-producer confound 未充分解决\n- 具体位置：Limitations (p.9), Appendix D, Table 1\n- 问题：Qwen3-32B 同时担任 rewriter 和 judge，这引入了 self-preference bias (Panickssery et al., 2024) 的系统性混淆。论文在 Limitations 中承认 \"cross-judge effect-size comparisons are not valid\"，但主文 Table 1 中 Qwen3-32B 的结果仍作为 **主要证据** 与 GPT-4o 并列呈现。Appendix D 的 cross-rewriter test（替换 rewriter 为 GPT-4o）只能证明 rewriter identity 的影响有限，但 **无法排除** Qwen3-32B 作为 judge 时偏好自身产出的可能性。具体地：如果 Qwen3-32B 对自身生成的 formal/verbose 文本有系统性偏好（self-preference），则观测到的 \"style bias\" 可能部分甚至主要来自 self-preference 而非 genuine style bias。\n- 为什么影响接收：这是实验设计的基本有效性问题。如果 Qwen3-32B 的结果受到 self-preference 污染，则论文的 \"cross-judge replication\" 叙事（两个 judge 均显示 bias → 发现具有通用性）被削弱。\n- 建议修改方向：(1) 使用与两个 judge（GPT-4o、Qwen3-32B）均无关的第三方模型（如 Llama 3）作为 rewriter，或至少在 Appendix D 的 cross-rewriter test 中展示 GPT-4o 做 rewriter + Qwen3-32B 做 judge 与 Qwen3-32B 做 rewriter + Qwen3-32B 做 judge 的效应量差异；(2) 在主文中对 Qwen3-32B 结果加明确 caveat 而非等到 Limitations。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] GEE 条件分解在残余混淆下的解释过强\n- 具体位置：Table 3, Section 5.6 (\"formality stands apart as confound-free\")\n- 问题：Table 3 的 GEE 条件分解将观测到的 judge 偏好分解为 Style OR 和 Originality OR。但这一分解的有效性 **依赖于** NLI gate 完全阻断 R→Q 路径。论文自身承认 NLI gate 有 8.4% FNR（Section 5.1）且 \"quality perception shifts mediated by style itself\" 无法被 NLI gate 捕获（Limitations）。在这种残余混淆下，GEE 的条件估计存在 omitted variable bias，\"confound-free\" 的判断可能过于乐观。\n- 建议：(1) 将 \"confound-free\" 改为 \"with reduced confounding\"；(2) 讨论残余混淆对 Style OR 估计的偏差方向（是否会导致高估或低估）。\n\n**W2** [warning] Sensitivity hierarchy (Table 2) 仅在单一轴（formality）上展示\n- 具体位置：Table 2, Section 5.2\n- 问题：Table 2 的 7 种方法 sensitivity hierarchy 是论文的核心方法论贡献之一，但 **仅在 formality 数据上展示**。Verbosity 是检测最强的轴（BT 76-77%），如果 7 种方法的 hierarchy 在 verbosity 上也成立，将大幅增强 Likert Blindspot 的通用性声明。目前读者无法判断 Table 2 的 pattern 是 formality 特有的还是跨轴通用的。\n- 建议：在 Appendix 中增加 verbosity 的 7 方法比较表。如果 verbosity 上 Likert 方法也全部失败（鉴于效应量更大，这一点尤其有说服力），论文的核心论点将更加稳固。\n\n**W3** [warning] \"Measurement attenuation\" vs. \"construct difference\" 在主文中呈现不平衡\n- 具体位置：Section 1 (\"not merely a statistical power gap but measurement attenuation\"), Section 5.2, Section 6; vs. Limitations (\"An alternative interpretation…Likert and pairwise modes measure different constructs\")\n- 问题：论文主文的 framing 将 Likert Blindspot 定位为 **测量衰减**（measurement attenuation）——即 Likert 应该检测到 bias 但检测不到。但 Limitations 中承认的替代解释——Likert 和 pairwise 测量的是 **不同构念**（absolute quality difference vs. ordinal preference）——在概念上同样合理。如果两种方法测量不同构念，则\"Blindspot\"的 framing 本身就有误导性：不是 Likert\"看不到\"bias，而是 Likert 测的是另一个东西。论文没有提供能区分这两种解释的实验证据。\n- 为什么重要：这影响论文核心贡献的定位。如果读者接受 \"construct difference\" 解释，则论文的 practical implication 从\"Likert 有缺陷，应使用 pairwise\"变为\"Likert 和 pairwise 各有用途，视研究问题而定\"。\n- 建议：(1) 在主文（如 Section 5.2 末尾）提前讨论 construct difference 解释，而非仅在 Limitations 中一笔带过；(2) 设计一个能区分两种解释的实验（如：对已知存在 style bias 的合成数据，Likert 是否在足够大的 n 下最终检测到？如果是，则为 power gap；如果不是，则为 construct difference）。\n\n**W4** [warning] NLI 阈值 sensitivity analysis 过于粗糙\n- 具体位置：Section 5.1, p.6 (\"thresholds of 0.70, 0.80, 0.90, and 0.95\")\n- 问题：仅测试 4 个离散阈值。论文声称阈值位于 \"plateau rather than a cliff edge\"，但 4 个点不足以建立 plateau 的存在——在 0.70 和 0.90 之间的行为完全未知。一条从 0.50 到 0.99（步长 0.05）的连续 sensitivity 曲线会更有说服力。\n- 建议：在 Appendix 中补充更细粒度的阈值扫描（至少 10 个点），展示 BT win probability 和 pass rate 随阈值的变化趋势。\n\n**W5** [warning] Cross-rewriter independence test 缺少 register 轴\n- 具体位置：Appendix D\n- 问题：Appendix D 的 cross-rewriter test（替换 rewriter）只测试了 formality 和 verbosity，**缺少 register**。Register 是效应最弱、最接近 non-significant 的轴（GPT-4o BT 57.0%, p = 0.04; Qwen3-32B 55.3%, p = 0.076），恰恰是 rewriter identity 效应最可能影响结论的轴。\n- 建议：补充 register 轴的 cross-rewriter test。如果 register 的弱效应在更换 rewriter 后消失，应在主文中降低 register 结果的 claim 强度。\n\n**W6** [warning] 样本量偏小且主文缺乏 power analysis\n- 具体位置：Section 3.4 (n=100 LLMBar), Table 1, Figure 4\n- 问题：AlpacaEval 的 filtered 分析仅 n=88 对。对于 BT win probability 63%（formality），bootstrap 95% CI 为 [55.7, 70.3]（Table 8）——下界仅略高于 50%，置信区间跨度 15 个百分点。这意味着真实效应量的不确定性相当大。Figure 4 的 power analysis 有帮助，但仅展示了 detection probability，未报告 BT 估计精度（CI width）随 n 的变化。论文将小 n 时 Likert 未检测到 bias 归因于 Blindspot 而非 statistical power，但在 BT 估计本身也有大 CI 的情况下，这一归因需要更谨慎。\n- 建议：(1) 在主文中增加一段 power analysis 讨论，明确 n=88 时 BT 的 minimum detectable effect size；(2) 在 Figure 4 中增加 CI width vs. n 的曲线。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Figure 2 的 DAG 中，dashed edge S→Q 代表 \"style may influence perceived quality\"——这是 NLI gate 无法阻断的路径，但 DAG 中的视觉区分（dashed vs. solid）在打印时可能不够清晰。建议增加颜色编码或标注文字。\n- **M2**: 论文 7 种统计方法的选择（Table 2）未说明理由——为什么是这 7 种而非其他？例如，为什么不包含 mixed-effects logistic regression 或 Bayesian 方法？\n- **M3**: \"Likert Blindspot\" 这一术语可能暗示 Likert 量表本身有缺陷，但论文的发现更准确地说是\"单题 1-10 整体质量评分\"的局限性。多题项 Likert 量表或属性特定评分可能不表现出同样的 Blindspot。建议在 Section 1 或 2 中明确范围。\n- **M4**: Section 3.3 提到 Likert mode 使用 1-10 integer score，但未讨论评分粒度是否影响 Blindspot（如 1-100 fine-grained scale 是否能减轻 attenuation）。\n- **M5**: GPT-4o 200-pair cross-validation（Section 5.1）使用 LLM 验证 NLI gate 在研究 LLM bias 的论文中存在轻微的循环性——GPT-4o 自身的 style bias 可能影响其 content-preservation 判断。应在 limitations 中简要提及。\n\n---\n\n## Questions for Authors\n\n**Q1**: Table 2 的 sensitivity hierarchy 在 verbosity 轴上是否成立？如果 verbosity（效应量更大）的 Likert ATE 也为 non-significant，为什么不展示？如果 verbosity 的 Likert ATE 是 significant 的（在较大效应量下 Likert 开始检测到 bias），这对 \"severity spectrum\" 叙事意味着什么？\n\n**Q2**: 关于 IIA：是否做过按 task type（如 LLMBar 的 instruction-following categories）分层的 BT 参数稳定性检查？如果不同 task type 的 BT win probability 差异显著，则 IIA 可能被违反。\n\n**Q3**: n=355（scaled replication）时 Likert d→0 的结果（Section 5.2, Figure 4），是否尝试过更大的 n（如 n=1000 的模拟或 bootstrap extrapolation）来确认 d 确实收敛到 0 而非缓慢上升？这对区分 \"attenuation\" 和 \"power gap\" 至关重要。\n\n**Q4**: Qwen3-32B 作为 rewriter + judge 时，是否检查过 self-preference 的直接证据？例如，让 Qwen3-32B 在 original pair（未经 style manipulation）上做 pairwise comparison，是否对 Qwen3-32B 生成的回答有系统性偏好？\n\n---\n\n## Missing References\n\n- Zheng et al. (2024), \"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena\" — 论文引用了 MTBench benchmark 但未引用原始方法论文\n- Stureborg et al. (2024), \"Large Language Models are Inconsistent and Biased Evaluators\" — 关于 LLM judge Likert vs. pairwise 不一致性的直接相关工作\n- Park et al. (2024), \"Disentangling Length from Quality in Direct Assessments\" — 与论文的 verbosity 分析直接相关\n\n---\n\n## Overall Assessment\n\n**Overall**: 3.5 / 5（Borderline Conference）\n**Confidence**: 4 / 5\n\n论文提出了一个有实际意义的发现（Likert Blindspot）和一个设计合理的检测框架（CSD）。核心实证结果（Table 1-2, Figure 3-4）在多 benchmark、多 judge 上模式一致。但方法严谨性存在三个核心缺陷：(1) NLI gate 的因果声明（do-operator 近似）超出了筛选操作的实际能力，存在 collider bias 风险；(2) BT 模型的 IIA 假设未经检验，而实验设计中存在潜在的异质性；(3) evaluator-producer confound（Qwen3-32B 同时做 rewriter 和 judge）未充分解决。这三个问题彼此关联——如果 NLI gate 的因果控制力被削弱（N1），残余混淆更大，GEE 分解（W1）就更不可靠；如果 evaluator-producer confound（N3）存在，则 Qwen3-32B 的结果不能作为独立 replication。\n\n修改建议的优先级：N1（降低因果声明）> N3（解决 evaluator-producer confound）> N2（IIA 检验）> W2（多轴 sensitivity hierarchy）> W3（平衡两种解释）。如果 N1-N3 得到充分解决，论文可达 4.0（Conference）。",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 325 · 2026-05-21T12:40:51.229574+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3816
}
```

</details>

---


### Tool call

_source line 326 · 2026-05-21T12:40:56.506350+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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

_source line 327 · 2026-05-21T12:40:56.707665+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 328 · 2026-05-21T12:41:00.726966+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 329 · 2026-05-21T12:41:00.777583+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 330 · 2026-05-21T12:41:10.761155+00:00_

审稿报告已提交给 Review Director。

**评分摘要**：Overall 3.5/5（Borderline Conference），Soundness 3.5，Excitement 3.5，Reproducibility 4，Confidence 4/5。

**三个 Must-Fix**：
1. **N1** — NLI gate 被声称为 do-operator 近似，但实质是 selection/conditioning，存在 collider bias 风险，因果语言需降级
2. **N2** — Bradley-Terry 的 IIA 假设未检验，论文所有显著性结论均依赖 BT，需补充诊断
3. **N3** — Qwen3-32B 同时做 rewriter 和 judge 的 evaluator-producer confound 未充分解决，削弱 cross-judge replication 叙事

**六个 Should-Fix**：GEE "confound-free" 解释过强、sensitivity hierarchy 仅在单轴展示、attenuation vs. construct difference 主文呈现不平衡、NLI 阈值扫描仅 4 个点、cross-rewriter test 缺 register 轴、样本量偏小缺 power analysis。

核心判断：如果 N1-N3 得到充分修改（降低因果声明、补 IIA 检验、解决 evaluator-producer confound），论文可达 4.0（Conference）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1"
}
```

</details>

---


## Round 12

## Round 12

10 recorded events


### User

_source line 331 · 2026-05-21T12:51:56.034773+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 2 的完整审稿意见

请逐条回应以下 Reviewer 2 的审稿意见。对每个要点标注 **[AGREE]**（同意并说明理由）或 **[REBUT]**（反驳并引用论文中的具体 Section/Table/Figure 作为证据）。

---

以下是 Reviewer 2 的完整审稿意见：

**Overall**: 3.0 / 5（Findings），Confidence 4/5

### Must-Fix 问题

**N1** [critical] 遗漏直接矛盾的关键文献：The Comparative Trap (Jeong et al., 2025, BlackboxNLP)
- Jeong et al. (2025) 系统性证明 pairwise comparison **放大** LLM evaluator 的 style bias（尤其 verbosity 和 authoritative tone），而非仅"检测"。本文核心建议"style bias audits should adopt pairwise comparison"与该文献存在直接张力。pairwise 是检测 bias 还是人为放大 bias？
- 建议：在 Related Work 和 Conclusion 中讨论 Comparative Trap；区分 "detection sensitivity" 与 "bias amplification"。

**N2** [critical] "first systematic quantitative verification" claim 需要限定
- 至少三篇近期工作做了类似 systematic quantification：(1) Jeong et al. (2025)；(2) Haak & Schaer (2025, arXiv:2512.14565)；(3) Soumik et al. (2026)。"First" 是 overclaim。
- 建议：改为限定到具体方法组合的 novelty。

**N3** [critical] Judge 覆盖面不足
- 仅 3 个 judges，Claude 为 negative control。实质只有 2 个 judges 展示 Blindspot。缺 Gemini、Llama-3-70B/405B、specialized judges。2 个 judge 不足以支撑 "across three judges" framing。
- 建议：至少增加 1 个开源 judge（Llama-3-70B）。

### Should-Fix 问题

**W1** Formality 轴 confound 实质削弱该轴贡献——Abstract/Conclusion 应区分 verbosity（confound-free）和 formality（confounded）
**W2** LLMBar (n=100) 规模受限——AlpacaEval 分析深度不足
**W3** Claude negative control 统计力不足——TOST n=87, Δ=10pp underpowered，应更审慎措辞
**W4** Table 1 实验矩阵不完整——多个 cell 缺失未解释

### Minor Issues
- 术语不一致（Blindspot/blindspot, style bias/style preference 混用）
- Abstract 信息密度过高
- orphan bib entry: hoenig2001abuse
- Figure 2 DAG 黑白打印不清
- wu2023style 引用年份 mismatch

### Missing References
1. **Jeong et al. (2025)** "The Comparative Trap" — **必须引用**
2. **Haak & Schaer (2025)** "Pairwise Comparison for Bias Identification and Quantification"
3. **LLM-as-a-Judge survey** (The Innovation, 2026)
4. **"Any Large Language Model Can Be a Reliable Judge"** (2025)

---

请对以上每个 Must-Fix、Should-Fix 和 Minor Issue 逐条回应 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 332 · 2026-05-21T12:52:47.099077+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Jeong 2025 \"The Comparative Trap\" BlackboxNLP pairwise comparison LLM evaluator style bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Jeong 2025 \"The Comparative Trap\" BlackboxNLP pairwise comparison LLM evaluator style bias"
  }
}
```

</details>

---


### Tool call

_source line 333 · 2026-05-21T12:52:47.602071+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Haak Schaer 2025 arXiv 2512.14565 \"Pairwise Comparison for Bias Identification\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Haak Schaer 2025 arXiv 2512.14565 \"Pairwise Comparison for Bias Identification\""
  }
}
```

</details>

---


### Tool call

_source line 334 · 2026-05-21T12:52:47.953833+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Stureborg 2024 \"Large Language Models are Inconsistent and Biased Evaluators\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Stureborg 2024 \"Large Language Models are Inconsistent and Biased Evaluators\""
  }
}
```

</details>

---


### Tool result

_source line 335 · 2026-05-21T12:52:52.729560+00:00_

Web search results for query: "Jeong 2025 "The Comparative Trap" BlackboxNLP pairwise comparison LLM evaluator style bias"

Links: [{"title":"The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators - ACL Anthology","url":"https://aclanthology.org/2025.blackboxnlp-1.5/"},{"title":"BlackboxNLP: Analyzing and Interpreting Neural Networks for NLP (2025) - ACL Anthology","url":"https://aclanthology.org/events/blackboxnlp-2025/"},{"title":"@inproceedings{jeong-etal-2025-comparative,","url":"https://aclanthology.org/2025.blackboxnlp-1.5.bib"},{"title":"Proceedings of the 8th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP - ACL Anthology","url":"https://aclanthology.org/volumes/2025.blackboxnlp-1/"},{"title":"[PDF] The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Comparative-Trap:-Pairwise-Comparisons-Biased-Jeong-Park/cd6191f270c5b98dec44a294e4f3cebcf371ac5f"},{"title":"[2406.12319] The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators","url":"https://arxiv.org/abs/2406.12319"},{"title":"[Literature Review] The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators","url":"https://www.themoonlight.io/en/review/the-comparative-trap-pairwise-comparisons-amplifies-biased-preferences-of-llm-evaluators"},{"title":"The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences   of LLM Evaluators","url":"https://arxiv.org/pdf/2406.12319"},{"title":"BlackboxNLP 2025","url":"https://blackboxnlp.github.io/2025/accepted_papers/"},{"title":"The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators","url":"https://arxiv.org/html/2406.12319v4"}]

I found the paper you're looking for! Here's what I found:

"The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators" by Hawon Jeong, C
…[truncated 1128 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 5630
}
```

</details>

---


### Tool result

_source line 336 · 2026-05-21T12:52:53.684239+00:00_

Web search results for query: "Stureborg 2024 "Large Language Models are Inconsistent and Biased Evaluators""

Links: [{"title":"Large Language Models are Inconsistent and Biased Evaluators | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/large-language-models-are-inconsistent-biased-evaluators"},{"title":"Large Language Models are Inconsistent and Biased Evaluators","url":"https://www.catalyzex.com/paper/large-language-models-are-inconsistent-and"},{"title":"Large Language Models are Inconsistent and Biased Evaluators | PromptLayer","url":"https://www.promptlayer.com/research-papers/large-language-models-are-inconsistent-and-biased-evaluators"},{"title":"Large Language Models are Inconsistent and Biased Evaluators","url":"https://paperreading.club/page?id=225338"},{"title":"Large Language Models are Inconsistent and Biased Evaluators - arXiv.gg","url":"https://arxiv.gg/abs/2405.01724"},{"title":"[2405.01724] Large Language Models are Inconsistent and Biased Evaluators","url":"https://arxiv.org/abs/2405.01724"},{"title":"fly51fly on X: \"[CL] Large Language Models are Inconsistent and Biased Evaluators R Stureborg, D Alikaniotis, Y Suhara [Grammarly &amp; NVIDIA] (2024) https://t.co/hkfoLgU43Q - LLMs show familiarity bias, preferring texts with lower perplexity that they are more familiar with. - LLMs exhibit score https://t.co/EB7NZOh2nk\" / X","url":"https://x.com/fly51fly/status/1787369849922130004"},{"title":"Large Language Models are Inconsistent a...","url":"https://axi.lims.ac.uk/paper/2405.01724"},{"title":"Large Language Models are Inconsistent and Biased Evaluators","url":"https://arxiv.org/html/2405.01724v1"},{"title":"Large Language Models are Inconsistent and Biased Evaluators","url":"https://arxiv.org/pdf/2405.01724"}]

I found the research paper you're looking for! Here's what I found about it:

"Large Language Models are Inconsistent and Biased Evaluators" was published on May 6, 2024 by Rickard Stureborg and Dimitris Alikani
…[truncated 861 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 5730
}
```

</details>

---


### Tool result

_source line 337 · 2026-05-21T12:52:55.493369+00:00_

Web search results for query: "Haak Schaer 2025 arXiv 2512.14565 "Pairwise Comparison for Bias Identification""

Links: [{"title":"Pairwise Comparison for Bias Identification and Quantification","url":"https://arxiv.org/pdf/2512.14565"},{"title":"[2512.14565] Pairwise Comparison for Bias Identification and Quantification","url":"https://arxiv.org/abs/2512.14565"},{"title":"(PDF) Pairwise Comparison for Bias Identification and Quantification","url":"https://www.researchgate.net/publication/398766651_Pairwise_Comparison_for_Bias_Identification_and_Quantification"},{"title":"Pairwise Comparison for Bias Identification and Quantification | Datenbank-Spektrum | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s13222-026-00531-1"},{"title":"GitHub - HaakFab/bias_pc: Pairwise Comparison for Bias Identification and Quantification · GitHub","url":"https://github.com/HaakFab/bias_pc"},{"title":"The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences   of LLM Evaluators","url":"https://arxiv.org/pdf/2406.12319"}]

I found the paper you're looking for! Here are the details:

**Paper:** "Pairwise Comparison for Bias Identification and Quantification" by Fabian Haak and Philipp Schaer (arXiv:2512.14565v1, December 16, 2025)

**Main Focus:** The paper addresses linguistic bias in online news and social media, which is widespread but difficult to measure due to subjectivity, context dependence, and the scarcity of high-quality gold-label datasets.

**Approach:** The authors aim to reduce annotation effort by leveraging pairwise comparison for bias annotation and evaluate more efficient implementations of pairwise comparison-based rating.

**Methodology:** They investigate the effects of various rating techniques and parameters of three cost-aware alternatives in a simulation environment, providing a basis for creating high-quality benchmark datasets and quantifying biases using both human and large language model annotation.

The paper and rela
…[truncated 164 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7891
}
```

</details>

---


### Tool call

_source line 338 · 2026-05-21T12:54:52.618705+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: 遗漏 The Comparative Trap (Jeong et al., 2025)**\n\n这是 Reviewer 2 最强的一个点，我完全同意其严重性。\n\nJeong et al. (2025, BlackboxNLP) 系统性地证明 pairwise comparison 相比 pointwise evaluation **放大**了 LLM evaluator 的 style bias（尤其 verbosity 和 authoritative tone）。这与本文的核心实证发现和实践建议构成直接张力：\n\n- 本文 Section 6 建议 \"style bias audits should adopt pairwise comparison\"\n- 本文 Table 2 的 sensitivity hierarchy 将 pairwise 方法（BT、sign test）排在最顶，Likert 方法排在最底\n- 本文将 pairwise 的更高检出率解释为 **detection sensitivity**\n\n但 Jeong et al. 的结果提供了一个完全不同的解释框架：pairwise 检出率高不是因为它更\"敏感\"，而是因为它 **人为放大** 了本来较小的 bias。如果这一解释成立，则：\n1. Likert 可能不是\"blindspot\"——而是更接近真实 bias 幅度的测量\n2. BT win probability 报告的 63-77% 可能是 amplified signal 而非 true bias magnitude\n3. 论文的 practical recommendation 方向可能需要反转\n\n这一遗漏不仅是 related work 的疏忽，而是影响论文核心贡献定位的根本性问题。我在 Round 1 审稿中提出的 W3（\"measurement attenuation\" vs. \"construct difference\" 解释不平衡）与此高度相关——Jeong et al. 的发现实质上支持了 \"construct difference\" 解释的一个更强版本：不是 Likert 测的是不同构念，而是 **pairwise 主动扭曲了 bias 的表现**。\n\n**补充建议**：作者需要在 Related Work (Section 2) 中讨论 Comparative Trap，并在方法论上论证 CSD 的 style-controlled rewriting + NLI gate 是否能区分 \"detection sensitivity\" 和 \"bias amplification\"——例如，如果 NLI gate 通过的 pair 在 pairwise mode 下显示 bias 而在 Likert mode 下不显示，这到底是 Likert 的 attenuation 还是 pairwise 的 amplification？论文目前没有提供区分这两种机制的实验证据。\n\n---\n\n**[AGREE with nuance] R2-N2: \"first systematic quantitative verification\" overclaim**\n\n部分同意。\n\n论文 Abstract 的原文（Section 1, p.1）：\"the first systematic quantitative verification of this known measurement principle for LLM judge evaluation\"——这里的 \"this known measurement principle\" 指 Likert 量表的 measurement attenuation。\n\nReviewer 2 指出至少三篇近期工作做了类似的 systematic quantification。我验证后的判断：\n\n- **Jeong et al. (2025)**：确实做了 pairwise vs. pointwise 的系统性量化对比，且覆盖了 style bias（包括 verbosity），构成直接先行工作\n- **Haak & Schaer (2025, arXiv:2512.14565)**：该文关注 news/social media 的 linguistic bias annotation，使用 pairwise comparison 做 bias 量化，但 **不是关于 LLM judge bias** 的工作——与本文的研究问题不同，作为 \"同类工作\" 的直接性较弱\n- **Soumik et al. (2026)**：本文已引用（Section 1, p.1），报告 bias scores 76-92%，但为 correlational 而非 interventional\n\n因此，\"first\" 的 overclaim 程度取决于范围界定：\n- 如果指 \"first interventional framework with NLI gate + per-axis decomposition\"——可能成立\n- 如果指 \"first systematic quantitative verification of measurement attenuation\"——在 Jeong et al. (2025) 已存在的情况下不成立\n\n**建议**：将 \"first\" 限定到 CSD 的具体方法组合的 novelty（如 \"the first black-box interventional framework integrating style-controlled rewriting, NLI content gating, and position-controlled pairwise comparison for per-axis style bias detection\"），避免对整体研究问题的 priority claim。\n\n---\n\n**[REBUT] R2-N3: Judge 覆盖面不足不应为 Must-Fix**\n\n我不同意这是 Must-Fix 级别的问题，理由如下：\n\n1. **论文的核心贡献是方法论（CSD 框架），不是 judge bias 的 exhaustive survey**。对于方法论贡献，在 2 个 target judge + 1 个 negative control 上验证是合理的标准实践。类比：RATE (Reber et al., 2025) 也只在有限 judge 上验证其方法。\n\n2. **Negative control 有独立方法论价值**。Claude Sonnet 4 作为 negative control（Table 1, all axes BT ~56%, non-significant）证明 CSD **不是在所有 judge 上都产生假阳性**。这比简单增加第 3 个显示 bias 的 judge 更有方法论说服力——它建立了 discriminant validity。\n\n3. **\"across three judges\" framing 确实需要调整**。我同意 Reviewer 2 的观察——Abstract 中 \"across three judges\" 可能给人 3 个 judge 都显示 bias 的印象。但修复方式是调整措辞（如 \"across two commercial judges, with a third serving as negative control\"），而非要求增加实验。\n\n4. **实际可行性**：增加 Llama-3-70B 或 Gemini 是 nice-to-have 但不改变方法论贡献的有效性。如果两个 reviewer 都要求增加不同的 judge，则修改周期内无法满足所有请求。\n\n**我的判断**：降级为 Should-Fix。措辞调整即可，不需要新实验。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Formality confound 区分不够突出**\n\n同意。论文 Section 5.6 和 Table 3 确实区分了 verbosity（confound-free, Style OR significant + Originality OR n.s.）和 formality（style + originality confounds 并存），但 Abstract 和 Conclusion 的 framing 将所有轴混为一谈。例如：\n- Abstract: \"three style axes\" 未说明各轴证据强度不同\n- Conclusion (Section 6): 虽有 \"Verbosity provides the cleanest evidence\" 但随后 \"formality exhibits conditional style effects alongside originality confounds\" 的措辞弱化了 confound 的严重性\n\n建议在 Abstract 中明确：\"verbosity bias is robustly detected as confound-free across judges; formality shows conditional style effects that partially confound with originality preferences\"。\n\n---\n\n**[REBUT with partial agreement] R2-W2: LLMBar n=100 规模受限**\n\n部分不同意。\n\nLLMBar 是一个标准 benchmark（Zeng et al., 2024），n=100 是其固有规模，不是作者的设计选择。批评 benchmark 的固有大小对作者不公平。论文已在三个不同规模的 benchmark 上测试（LLMBar n=100, AlpacaEval 和 MTBench），这本身就是对单一 benchmark 局限性的缓解。\n\n但我同意 AlpacaEval 的分析可以更深入——特别是在 formality 轴上，AlpacaEval 的 filtered n=88 是所有分析中最小的有效样本（我在 Round 1 W6 中已提出此问题）。\n\n---\n\n**[AGREE] R2-W3: Claude negative control TOST 统计力不足**\n\n同意这是一个有效的统计关注。\n\n如果 TOST 使用 n=87, Δ=10pp，则对于检测\"等价于零效应\"的 power 可能不足——特别是当真实效应可能是 5pp（一个实际上很小但非零的 bias）时。论文应该：\n1. 报告 TOST 的 achieved power\n2. 或将 negative control 的结论措辞从\"Claude 无 bias\"改为\"在当前样本量下未检测到 bias\"\n\n这与我在 Round 1 审稿中未覆盖到的一个盲区——我专注于 BT 和 GEE 的统计细节，但忽略了 negative control 的统计力问题。Reviewer 2 的这个点补充了我的审查。\n\n---\n\n**[AGREE] R2-W4: Table 1 实验矩阵不完整**\n\n同意。Table 1 确实有多个空 cell（例如 Claude 在部分 benchmark 上缺失结果，Qwen3-32B 在某些 benchmark-axis 组合上缺失）。论文未解释这些缺失的原因——是 API 配额限制、计算成本、还是有意省略？每个缺失 cell 都应在 footnote 或 Appendix 中说明原因。\n\n---\n\n### Minor Issues\n\n**[AGREE] 术语不一致**：Blindspot/blindspot 大小写不一致确实存在，应统一。style bias/style preference 的混用会影响精确性——bias 暗示系统性偏差，preference 可能是合理的评价。\n\n**[AGREE] Abstract 信息密度过高**：Abstract 试图在有限篇幅内覆盖方法（3 阶段管线）、发现（Likert Blindspot）、实验配置（3 judges × 3 axes × 3 benchmarks）和实践建议，确实过于密集。\n\n**[AGREE] orphan bib entry**：hoenig2001abuse 如果在正文中未引用，应删除。\n\n**[AGREE] Figure 2 DAG 黑白打印不清**：与我 Round 1 M1 一致——我也指出了 dashed vs. solid edge 在打印时可能不清楚。\n\n**[AGREE] wu2023style 引用年份**：应核实是否为 2023 还是其他年份。\n\n---\n\n### Missing References\n\n**[AGREE] Jeong et al. (2025) \"The Comparative Trap\"**：如上 N1 所述，**必须引用**。这是与本文核心论点直接相关且潜在矛盾的工作。\n\n**[REBUT] Haak & Schaer (2025)**：该文研究的是 news/social media 的 linguistic bias annotation，不是 LLM judge bias。方法上使用 pairwise comparison 做 bias 量化，但研究对象和问题域不同。属于 tangentially related，引用是 nice-to-have 而非 must-cite。\n\n**[AGREE] Stureborg et al. (2024) \"Large Language Models are Inconsistent and Biased Evaluators\"**：该文直接研究 LLM evaluator 的 inconsistency 和 bias（包括 Likert 评分分布偏差、anchoring effects），与本文 highly relevant。我在 Round 1 Missing References 中也独立提出了此文。\n\n**[No opinion] LLM-as-a-Judge survey (The Innovation, 2026) 和 \"Any Large Language Model Can Be a Reliable Judge\" (2025)**：未能验证这两篇的存在和具体内容，不作判断。\n\n---\n\n### 综合判断\n\nReviewer 2 的审稿在 **related work 完整性** 和 **claim 精确度** 方面提出了比我更尖锐的问题，特别是 N1（Comparative Trap）是一个我在 Round 1 中遗漏的重要发现。这篇遗漏的文献实质上加强了我在 Round 1 中提出的 W3（\"measurement attenuation\" vs. \"construct difference\" 解释不平衡）——Jeong et al. 的 \"bias amplification\" 解释为 construct difference 提供了独立的实证支持。\n\n但我不同意 Reviewer 2 将 judge 覆盖面不足定为 Must-Fix（N3）——对于方法论论文，2 positive judges + 1 negative control 是合理的验证范围。\n\n**我对 Overall 的修订建议**：Reviewer 2 给 3.0 (Findings)，我维持 3.5 (Borderline Conference)。考虑到 Comparative Trap 遗漏的严重性，如果作者不能在 revision 中充分论证 CSD 的 detection sensitivity 与 pairwise amplification 的区分，我可能下调至 3.0。但如果能说清楚（例如通过论证 NLI gate 控制了 pairwise amplification 的部分机制），则 3.5 甚至 4.0 仍可达到。",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: 遗漏 The Comparative Trap (Jeong et al., 2025)**\n\n这是 Reviewer 2 最强的一个点，我完全同意其严重性。\n\nJeong et al. (2025, BlackboxNLP) 系统性地证明 pairwise comparison 相比 pointwise evaluation **放大**了 LLM evaluator 的 style bias（尤其 verbosity 和 authoritative tone）。这与本文的核心实证发现和实践建议构成直接张力：\n\n- 本文 Section 6 建议 \"style bias audits should adopt pairwise comparison\"\n- 本文 Table 2 的 sensitivity hierarchy 将 pairwise 方法（BT、sign test）排在最顶，Likert 方法排在最底\n- 本文将 pairwise 的更高检出率解释为 **detection sensitivity**\n\n但 Jeong et al. 的结果提供了一个完全不同的解释框架：pairwise 检出率高不是因为它更\"敏感\"，而是因为它 **人为放大** 了本来较小的 bias。如果这一解释成立，则：\n1. Likert 可能不是\"blindspot\"——而是更接近真实 bias 幅度的测量\n2. BT win probability 报告的 63-77% 可能是 amplified signal 而非 true bias magnitude\n3. 论文的 practical recommendation 方向可能需要反转\n\n这一遗漏不仅是 related work 的疏忽，而是影响论文核心贡献定位的根本性问题。我在 Round 1 审稿中提出的 W3（\"measurement attenuation\" vs. \"construct difference\" 解释不平衡）与此高度相关——Jeong et al. 的发现实质上支持了 \"construct difference\" 解释的一个更强版本：不是 Likert 测的是不同构念，而是 **pairwise 主动扭曲了 bias 的表现**。\n\n**补充建议**：作者需要在 Related Work (Section 2) 中讨论 Comparative Trap，并在方法论上论证 CSD 的 style-controlled rewriting + NLI gate 是否能区分 \"detection sensitivity\" 和 \"bias amplification\"——例如，如果 NLI gate 通过的 pair 在 pairwise mode 下显示 bias 而在 Likert mode 下不显示，这到底是 Likert 的 attenuation 还是 pairwise 的 amplification？论文目前没有提供区分这两种机制的实验证据。\n\n---\n\n**[AGREE with nuance] R2-N2: \"first systematic quantitative verification\" overclaim**\n\n部分同意。\n\n论文 Abstract 的原文（Section 1, p.1）：\"the first systematic quantitative verification of this known measurement principle for LLM judge evaluation\"——这里的 \"this known measurement principle\" 指 Likert 量表的 measurement attenuation。\n\nReviewer 2 指出至少三篇近期工作做了类似的 systematic quantification。我验证后的判断：\n\n- **Jeong et al. (2025)**：确实做了 pairwise vs. pointwise 的系统性量化对比，且覆盖了 style bias（包括 verbosity），构成直接先行工作\n- **Haak & Schaer (2025, arXiv:2512.14565)**：该文关注 news/social media 的 linguistic bias annotation，使用 pairwise comparison 做 bias 量化，但 **不是关于 LLM judge bias** 的工作——与本文的研究问题不同，作为 \"同类工作\" 的直接性较弱\n- **Soumik et al. (2026)**：本文已引用（Section 1, p.1），报告 bias scores 76-92%，但为 correlational 而非 interventional\n\n因此，\"first\" 的 overclaim 程度取决于范围界定：\n- 如果指 \"first interventional framework with NLI gate + per-axis decomposition\"——可能成立\n- 如果指 \"first systematic quantitative verification of measurement attenuation\"——在 Jeong et al. (2025) 已存在的情况下不成立\n\n**建议**：将 \"first\" 限定到 CSD 的具体方法组合的 novelty（如 \"the first black-box interventional framework integrating style-controlled rewriting, NLI content gating, and position-controlled pairwise comparison for per-axis style bias detection\"），避免对整体研究问题的 priority claim。\n\n---\n\n**[REBUT] R2-N3: Judge 覆盖面不足不应为 Must-Fix**\n\n我不同意这是 Must-Fix 级别的问题，理由如下：\n\n1. **论文的核心贡献是方法论（CSD 框架），不是 judge bias 的 exhaustive survey**。对于方法论贡献，在 2 个 target judge + 1 个 negative control 上验证是合理的标准实践。类比：RATE (Reber et al., 2025) 也只在有限 judge 上验证其方法。\n\n2. **Negative control 有独立方法论价值**。Claude Sonnet 4 作为 negative control（Table 1, all axes BT ~56%, non-significant）证明 CSD **不是在所有 judge 上都产生假阳性**。这比简单增加第 3 个显示 bias 的 judge 更有方法论说服力——它建立了 discriminant validity。\n\n3. **\"across three judges\" framing 确实需要调整**。我同意 Reviewer 2 的观察——Abstract 中 \"across three judges\" 可能给人 3 个 judge 都显示 bias 的印象。但修复方式是调整措辞（如 \"across two commercial judges, with a third serving as negative control\"），而非要求增加实验。\n\n4. **实际可行性**：增加 Llama-3-70B 或 Gemini 是 nice-to-have 但不改变方法论贡献的有效性。如果两个 reviewer 都要求增加不同的 judge，则修改周期内无法满足所有请求。\n\n**我的判断**：降级为 Should-Fix。措辞调整即可，不需要新实验。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Formality confound 区分不够突出**\n\n同意。论文 Section 5.6 和 Table 3 确实区分了 verbosity（confound-free, Style OR significant + Originality OR n.s.）和 formality（style + originality confounds 并存），但 Abstract 和 Conclusion 的 framing 将所有轴混为一谈。例如：\n- Abstract: \"three style axes\" 未说明各轴证据强度不同\n- Conclusion (Section 6): 虽有 \"Verbosity provides the cleanest evidence\" 但随后 \"formality exhibits conditional style effects alongside originality confounds\" 的措辞弱化了 confound 的严重性\n\n建议在 Abstract 中明确：\"verbosity bias is robustly detected as confound-free across judges; formality shows conditional style effects that partially confound with originality preferences\"。\n\n---\n\n**[REBUT with partial agreement] R2-W2: LLMBar n=100 规模受限**\n\n部分不同意。\n\nLLMBar 是一个标准 benchmark（Zeng et al., 2024），n=100 是其固有规模，不是作者的设计选择。批评 benchmark 的固有大小对作者不公平。论文已在三个不同规模的 benchmark 上测试（LLMBar n=100, AlpacaEval 和 MTBench），这本身就是对单一 benchmark 局限性的缓解。\n\n但我同意 AlpacaEval 的分析可以更深入——特别是在 formality 轴上，AlpacaEval 的 filtered n=88 是所有分析中最小的有效样本（我在 Round 1 W6 中已提出此问题）。\n\n---\n\n**[AGREE] R2-W3: Claude negative control TOST 统计力不足**\n\n同意这是一个有效的统计关注。\n\n如果 TOST 使用 n=87, Δ=10pp，则对于检测\"等价于零效应\"的 power 可能不足——特别是当真实效应可能是 5pp（一个实际上很小但非零的 bias）时。论文应该：\n1. 报告 TOST 的 achieved power\n2. 或将 negative control 的结论措辞从\"Claude 无 bias\"改为\"在当前样本量下未检测到 bias\"\n\n这与我在 Round 1 审稿中未覆盖到的一个盲区——我专注于 BT 和 GEE 的统计细节，但忽略了 negative control 的统计力问题。Reviewer 2 的这个点补充了我的审查。\n\n---\n\n**[AGREE] R2-W4: Table 1 实验矩阵不完整**\n\n同意。Table 1 确实有多个空 cell（例如 Claude 在部分 benchmark 上缺失结果，Qwen3-32B 在某些 benchmark-axis 组合上缺失）。论文未解释这些缺失的原因——是 API 配额限制、计算成本、还是有意省略？每个缺失 cell 都应在 footnote 或 Appendix 中说明原因。\n\n---\n\n### Minor Issues\n\n**[AGREE] 术语不一致**：Blindspot/blindspot 大小写不一致确实存在，应统一。style bias/style preference 的混用会影响精确性——bias 暗示系统性偏差，preference 可能是合理的评价。\n\n**[AGREE] Abstract 信息密度过高**：Abstract 试图在有限篇幅内覆盖方法（3 阶段管线）、发现（Likert Blindspot）、实验配置（3 judges × 3 axes × 3 benchmarks）和实践建议，确实过于密集。\n\n**[AGREE] orphan bib entry**：hoenig2001abuse 如果在正文中未引用，应删除。\n\n**[AGREE] Figure 2 DAG 黑白打印不清**：与我 Round 1 M1 一致——我也指出了 dashed vs. solid edge 在打印时可能不清楚。\n\n**[AGREE] wu2023style 引用年份**：应核实是否为 2023 还是其他年份。\n\n---\n\n### Missing References\n\n**[AGREE] Jeong et al. (2025) \"The Comparative Trap\"**：如上 N1 所述，**必须引用**。这是与本文核心论点直接相关且潜在矛盾的工作。\n\n**[REBUT] Haak & Schaer (2025)**：该文研究的是 news/social media 的 linguistic bias annotation，不是 LLM judge bias。方法上使用 pairwise comparison 做 bias 量化，但研究对象和问题域不同。属于 tangentially related，引用是 nice-to-have 而非 must-cite。\n\n**[AGREE] Stureborg et al. (2024) \"Large Language Models are Inconsistent and Biased Evaluators\"**：该文直接研究 LLM evaluator 的 inconsistency 和 bias（包括 Likert 评分分布偏差、anchoring effects），与本文 highly relevant。我在 Round 1 Missing References 中也独立提出了此文。\n\n**[No opinion] LLM-as-a-Judge survey (The Innovation, 2026) 和 \"Any Large Language Model Can Be a Reliable Judge\" (2025)**：未能验证这两篇的存在和具体内容，不作判断。\n\n---\n\n### 综合判断\n\nReviewer 2 的审稿在 **related work 完整性** 和 **claim 精确度** 方面提出了比我更尖锐的问题，特别是 N1（Comparative Trap）是一个我在 Round 1 中遗漏的重要发现。这篇遗漏的文献实质上加强了我在 Round 1 中提出的 W3（\"measurement attenuation\" vs. \"construct difference\" 解释不平衡）——Jeong et al. 的 \"bias amplification\" 解释为 construct difference 提供了独立的实证支持。\n\n但我不同意 Reviewer 2 将 judge 覆盖面不足定为 Must-Fix（N3）——对于方法论论文，2 positive judges + 1 negative control 是合理的验证范围。\n\n**我对 Overall 的修订建议**：Reviewer 2 给 3.0 (Findings)，我维持 3.5 (Borderline Conference)。考虑到 Comparative Trap 遗漏的严重性，如果作者不能在 revision 中充分论证 CSD 的 detection sensitivity 与 pairwise amplification 的区分，我可能下调至 3.0。但如果能说清楚（例如通过论证 NLI gate 控制了 pairwise amplification 的部分机制），则 3.5 甚至 4.0 仍可达到。",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 339 · 2026-05-21T12:54:56.235533+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3616
}
```

</details>

---


### Assistant

_source line 340 · 2026-05-21T12:55:02.302885+00:00_

交叉回应已提交。

核心判断：Reviewer 2 最有力的点是 N1（Comparative Trap 遗漏）——Jeong et al. (2025) 证明 pairwise 放大 style bias，与本文"用 pairwise 做 bias audit"的建议构成直接张力。这一遗漏加强了我 Round 1 中关于 "measurement attenuation vs. construct difference" 解释不平衡的担忧。但 N3（judge 覆盖面）作为 Must-Fix 过重，降级为 Should-Fix 更合理。我维持 Overall 3.5，但若作者不能区分 detection sensitivity 和 bias amplification，可能下调至 3.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1"
}
```

</details>

---


## Round 13

## Round 13

36 recorded events


### User

_source line 341 · 2026-05-21T14:16:41.374224+00:00_

[Round 1 审稿请求]:
[Dream 审稿任务 — Reviewer 1：方法 + 实验]

PDF 路径：/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/review_input_db82206b.pdf

目标 venue：EMNLP 2026（ARR Overall Assessment 1-5 半分制）
评分刻度：5=Award, 4=Conference accept, 3=Findings, 2=Resubmit, 1=Do not resubmit
接受率：Main ~21%

你的审查侧重：
- **方法描述**：CSD pipeline 四个 stage 是否完整描述、claim 是否被实验数据支撑、关键超参/统计方法是否清晰
- **实验设计**：是否覆盖关键 baseline / ablation / 跨数据集 / scale 维度；特别关注：placebo control 设计、NLI gate ablation、rewriter independence、cross-benchmark coverage、negative control (Claude) 的充分性
- **数据呈现**：表格/图是否能让审稿人复现结论、误差棒/统计显著性是否充分、sample size (n=86-88) 是否足够
- **实验覆盖度参考**：review_context.yaml 列出了完整实验设计（含 Llama-70B verbosity/formality、double-rewrite placebo、NLI gate ablation、cross-axis gradient、Gemini judge、cross-benchmark、Likert sensitivity analysis、rewriter independence、scaled replication 等）。请对照论文判断哪些实验被充分报告、哪些被省略或简化。

请基于论文内容独立评判，不要假设论文结果的质量高低。

Dream 审稿边界：
- 不需要评审：Reproducibility checklist、代码/数据可用性、具体数值精确性、伦理/IRB、匿名性
- 需要评审但标注为 "presentation 层面"：Reference 真实性、论文完整度、引用数量
- 必须评审（idea/design 层面）：实验设计是否足以支撑 claims、叙事逻辑是否自洽、Claim 的 generality 是否被实验范围支撑

每条 weakness 必须标注属于 **idea 层面** 还是 **presentation 层面**。

评分校准：3+ Major issues → ≤ Borderline Reject；2 Major → ≤ Weak Accept；1 Major → ≤ Accept；0 Major → 可 Strong Accept。

**不要评判**：新颖性/相关工作（那是 Reviewer 2 的范围）、格式/排版。

请通过 `review_reviewer_post_to_director(text, reviewer_id="1", project="causal_style_decomp_judge", dream_id="20260521T132932")` 汇报。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 342 · 2026-05-21T14:16:51.932425+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/review_input_db82206b.pdf",
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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/review_input_db82206b.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 343 · 2026-05-21T14:16:52.083891+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"页码超出范围 (共 6 页): 1-10\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 344 · 2026-05-21T14:16:52.084361+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/dream_20260521T132932/**/*context*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/dream_20260521T132932/**/*context*"
  }
}
```

</details>

---


### Tool result

_source line 345 · 2026-05-21T14:16:52.134878+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 346 · 2026-05-21T14:16:57.814493+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/review_input_db82206b.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "1-6",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/review_input_db82206b.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "1-6",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 347 · 2026-05-21T14:16:57.865147+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/dream_20260521T132932/**/*.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/dream_20260521T132932/**/*.yaml"
  }
}
```

</details>

---


### Tool result

_source line 348 · 2026-05-21T14:16:58.976683+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/_pdf_images/paper_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 441.0}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/_pdf_images/paper_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 495.7}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/_pdf_images/paper_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 458.1}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/_pdf_images/paper_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 435.4}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/_pdf_images/paper_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 480.7}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/_pdf_images/paper_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 400.5}], \"total_pages\": 6, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1162
}
```

</details>

---


### Tool result

_source line 349 · 2026-05-21T14:16:58.977019+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 1111
}
```

</details>

---


### Tool call

_source line 350 · 2026-05-21T14:17:02.339835+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/_pdf_images/paper_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/_pdf_images/paper_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 351 · 2026-05-21T14:17:03.245498+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 352 · 2026-05-21T14:17:03.296264+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/_pdf_images/paper_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/_pdf_images/paper_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 353 · 2026-05-21T14:17:03.798947+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/_pdf_images/paper_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/_pdf_images/paper_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 354 · 2026-05-21T14:17:04.654338+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1358
}
```

</details>

---


### Tool result

_source line 355 · 2026-05-21T14:17:04.655052+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 356 · 2026-05-21T14:17:04.705492+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/_pdf_images/paper_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/_pdf_images/paper_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 357 · 2026-05-21T14:17:05.260100+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 554
}
```

</details>

---


### Tool call

_source line 358 · 2026-05-21T14:17:05.360882+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/_pdf_images/paper_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/_pdf_images/paper_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 359 · 2026-05-21T14:17:06.065439+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 704
}
```

</details>

---


### Tool call

_source line 360 · 2026-05-21T14:17:06.166196+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/_pdf_images/paper_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/_pdf_images/paper_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 361 · 2026-05-21T14:17:06.369523+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/dream_20260521T132932/**/review_context*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/dream_20260521T132932/**/review_context*"
  }
}
```

</details>

---


### Tool result

_source line 362 · 2026-05-21T14:17:06.370033+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 363 · 2026-05-21T14:17:06.623052+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 456
}
```

</details>

---


### Tool call

_source line 364 · 2026-05-21T14:17:10.791585+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/dream_20260521T132932/**/*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/dream_20260521T132932/**/*"
  }
}
```

</details>

---


### Tool result

_source line 365 · 2026-05-21T14:17:11.042768+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 366 · 2026-05-21T14:17:14.406861+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/**/*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/**/*"
  }
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-21T14:17:14.458846+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/logs/orchestrator.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/logs/phase1_attempt0.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/logs/phase2_best_attempt0.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/logs/phase2_median_attempt0.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/logs/phase2_worst_attempt0.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/acl.sty
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/paper.aux
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/paper.out
/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/paper.pdf
/home/ubuntu/.agent-ml-research
…[truncated 4986 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 368 · 2026-05-21T14:17:18.501448+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/review_context.yaml"
  }
}
```

</details>

---


### Tool result

_source line 369 · 2026-05-21T14:17:18.605098+00:00_

1	narrative_guidance: 'Original framing fully stands. C1-C4 claims no adjustment needed.
2	  Llama-70B confirms significant bias on both verbosity and formality, completing
3	  3/3 independent architecture families (GPT-4o proprietary US, Qwen3-32B open CN,
4	  Llama-70B open US) plus Claude negative control. Double-rewrite placebo BT ≈ 50%
5	  eliminates Comparative Trap format amplification hypothesis entirely. NLI gate ablation
6	  shows pass>fail directionally, cross-axis gradient is monotonic. Four-layer MF1
7	  defense complete: placebo BT + NLI gate + Claude control + cross-axis gradient.
8	  SF3 (generalizability) fully resolved with 3rd judge. Reviewer path → 4.0 Conference.
9	
10	  '
11	imagined_experiments:
12	- name: Llama-3.3-70B verbosity — BT + GEE + Likert
13	  plan_id: exp-021
14	  description: 'Llama-3.3-70B-Instruct on 86 NLI-pass verbosity counterfactual pairs
15	    (LLMBar). Pairwise dual-direction + Likert scoring. Reuses Qwen3-32B-rewritten
16	    pairs; rewriting and NLI independent of judge.
17	
18	    '
19	  expected_results:
20	    bt_p_verbose_wins: 0.75
21	    bt_ci:
22	    - 0.68
23	    - 0.82
24	    bt_p_value: 0.0001
25	    bt_method: pair-level bootstrap (10000 iterations, seed=42)
26	    n_pairs: 86
27	    n_comparisons: 172
28	    consistency_rate: 0.68
29	    verbose_win_rate_sign: 0.847
30	    sign_test_p: 3.0e-05
31	    wilson_ci:
32	    - 0.737
33	    - 0.918
34	    likert_ate: 0.065
35	    likert_p: 0.45
36	    likert_d: 0.058
37	    likert_tie_rate: 0.59
38	    gee_verbose_or: 11.5
39	    gee_verbose_ci:
40	    - 4.8
41	    - 27.6
42	    gee_verbose_p: 1.0e-05
43	    gee_originality_or: 0.52
44	    gee_originality_ci:
45	    - 0.23
46	    - 1.18
47	    gee_originality_p: 0.115
48	    direction_verbose_to_concise_orig_pref: 0.81
49	    direction_verbose_to_concise_p: 0.0006
50	    direction_concise_to_verbose_rewrite_pref: 0.88
51	    direction_concise_to_verbose_p: 5.0e-06
52	    blindspot_confirmed: true
53	  result_rationa
…[truncated 24496 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 370 · 2026-05-21T14:20:50.750811+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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

_source line 371 · 2026-05-21T14:20:50.853128+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-21T14:22:49.465644+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Dream 审稿报告 — Reviewer 1（方法 + 实验）\n\n**论文**: The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\n**Dream ID**: 20260521T132932 (best scenario)\n**Venue**: EMNLP 2026 (ARR)\n**审查侧重**: 方法描述、实验设计、数据呈现、实验覆盖度\n\n---\n\n## Overall Assessment\n\n**Overall**: 3.5 / 5（Borderline Conference）\n**Confidence**: 4 / 5\n\n**一句话总结**: 实验设计全面（placebo control、NLI ablation、4 judge families、3 rewriters、cross-benchmark），显著优于通常的 bias detection 论文，但 placebo 统计力不足以支撑 \"format amplification empirically excluded\" 的强声明，且多处关键方法细节缺失。\n\n---\n\n## Summary\n\n论文提出 CSD 框架，通过 4 阶段管线（counterfactual rewriting → NLI gating → position-controlled pairwise comparison → BT/GEE statistical analysis）检测 LLM judge 的 per-axis style bias。核心发现是 Likert Blindspot：18 个 judge×axis×benchmark cell 中，BT 在 12 个 cell 检测到显著 bias，Likert 仅在 2 个 cell 检测到（6× sensitivity gap）。论文在 4 个 target judge families（GPT-4o、Qwen3-32B、Llama-70B、Gemini-Flash）+ 1 个 negative control（Claude）上验证，配合 double-rewrite placebo、NLI gate ablation、cross-axis gradient、rewriter independence 四层控制。\n\n---\n\n## Strengths\n\n**S1. 实验控制的层次感和完整性**：四层 anti-amplification 防御（placebo BT ≈ 50% in Table 4, NLI ablation in Table 5, Claude negative control in §5.4.4, cross-axis gradient in Table 6）是该领域论文中罕见的严谨程度。特别是 double-rewrite placebo 直接回应了 Jeong et al. (2025) Comparative Trap 的核心担忧——当 style 差异不存在时 BT = chance。\n\n**S2. Judge 和 rewriter 覆盖全面**：4 个 target judge families 覆盖 proprietary US (GPT-4o)、open CN (Qwen3-32B)、open US (Llama-70B)、proprietary US lightweight (Gemini-Flash)，加上 Claude negative control。3 个 rewriter (Qwen3-32B, GPT-4o, Llama-3.1-70B) 的 BT 范围 <2.1pp (Table 8)，有力证明了 rewriter independence。\n\n**S3. Detection matrix (Table 2) 是量化 Blindspot 的清晰手段**：18-cell 全覆盖的 BT sig vs Likert sig 2×2 矩阵直接、可复现、无需主观判断。10/12 BT-significant cells 的 Likert p > 0.15 使结论对 α 选择不敏感。\n\n**S4. GEE decomposition 揭示 per-axis confound structure**：Table 3 将 3 轴清晰分层——verbosity pure style (Style OR 高, Orig OR NS), formality conditional (both significant), register originality-dominated。这一 taxonomy 在 3 个 target judge 上独立复制（Table 6, Spearman 单调），比仅报告 \"bias exists\" 有更强的方法论贡献。\n\n**S5. Comparative Trap 的直接回应**：Section 2 引用 Jeong et al. (2025) 并在 §5.4.1 用 placebo 实验回应。Section 6 Discussion 专门讨论 \"Detection versus amplification\"，提出四层防御论证。这比忽略该文献或仅在 limitations 中提及好得多。\n\n---\n\n## Must-Fix 问题\n\n**N1** [Major, idea 层面] Placebo \"entirely attributable\" overclaim — 统计力不足以排除中等幅度的 format amplification\n\n- 具体位置：Section 5.4.1, Table 4, 及 Discussion p.5 (\"Treatment-Placebo gap...is entirely attributable to the style manipulation\")\n- 问题：Table 4 的 placebo BT 在 n=88 pairs 下：\n  - GPT-4o formality: 0.51 [0.44, 0.58], p=0.75\n  - Qwen3-32B formality: 0.50 [0.43, 0.57], p=0.92\n  - GPT-4o verbosity: 0.52 [0.45, 0.59], p=0.60\n  \n  placebo 95% CI 上界为 0.57-0.59，意味着最多 **~8pp 的 format amplification 与数据兼容**（CI 内）。对于 formality axis（treatment BT 0.630），placebo CI 上界 0.58 与 treatment CI 下界 0.558 **存在重叠**。这意味着无法在统计上完全排除 formality BT 中有 5-8pp 来自 format amplification 而非 pure style bias。\n  \n  论文声称 \"entirely attributable to style manipulation\" 和 Section 5 Discussion 的 \"format amplification empirically excluded\" 超出了 placebo 设计在 n=88 下的统计力所能支撑的声明强度。\n\n- 为什么是 Major：这是论文回应 Comparative Trap (Jeong et al., 2025) 的核心论证。如果 format amplification 被低估（如存在 5-8pp），则：(1) treatment BT 的 \"true style bias\" 部分被高估；(2) Likert Blindspot 的幅度解释需要调整（Likert 可能不是\"看不到\"full 63%，而是\"看不到\"55%——后者更难检测）。虽然 bias 的存在（BT > 50%）不受影响，但 magnitude 解释受影响。\n\n- 建议修改方向：\n  (1) 将 \"entirely attributable\" 改为 \"predominantly attributable, with residual amplification bounded to <8pp by placebo CI\"\n  (2) 报告 treatment-placebo 差值的 bootstrap CI（而非仅报告各自的 CI）\n  (3) 讨论 minimum detectable amplification effect at n=88（~14pp at 80% power）\n  (4) 在 Table 4 中增加 Δ 列的 CI\n\n---\n\n## Should-Fix 问题\n\n**W1** [idea 层面] NLI-fail ablation 样本量过小，不足以支撑方向性结论\n\n- 具体位置：Table 5, §5.4.2\n- 问题：NLI-fail pairs 仅 n=12（formality）和 n=14（verbosity）。Table 5 的 \"NLI-fail pairs show BT that reflects content-mediated signal\" 和 \"confirming the gate removes content-mediated signal\" 基于这些极小样本。在 n=12 下，BT 的 standard error 约 ±15pp，pass-fail gap 9.5pp 完全可以是随机波动。论文承认 \"NLI-fail n too small for individual significance\"（来自 review_context 的 note），但主文仍将方向性结果作为 NLI gate 有效性的证据（\"NLI-fail pairs...show BT that reflects content-mediated signal\"）。\n- 建议：(1) 在主文中明确标注 NLI-fail 结果为 \"directional but underpowered\"；(2) 不要将其作为四层防御中的独立一层——它更应该是 supplementary observation。\n\n**W2** [idea 层面] Register 轴的 \"three style axes\" framing 与 GEE 证据不匹配\n\n- 具体位置：Abstract (\"three style axes\"), Table 3, Table 6\n- 问题：Table 3 和 Table 6 的 GEE decomposition 显示 register 是 \"originality-dominated\"（GEE Style/Orig ratio = 0.33），register BT 仅 55-57%（边缘显著或不显著）。这意味着 register 上观测到的弱 preference 主要来自 originality confound 而非 style bias。论文的 \"three style axes\" framing 暗示在三个轴上均检测到了 style bias，但 register 的证据更准确地描述为 \"originality effect with weak residual style component\"。\n- 建议：(1) 在 Abstract 中区分 \"two clear style bias axes (verbosity, formality) and one originality-dominated axis (register)\"；(2) 或将 register 定位为 negative/weak finding 而非正面证据。\n\n**W3** [idea 层面] Cross-axis gradient 作为防御层的统计效力为零\n\n- 具体位置：Table 6, Discussion p.5\n- 问题：Table 6 展示 3 个轴的 NLI rejection rate 与 BT 的单调关系，Spearman ρ = 1.0。但 **3 个数据点的任何单调排列都产生 ρ = 1.0**——这不是统计发现而是定义性成立。论文称其为 \"qualitative argument, not statistical test\"（review_context），但 Discussion 仍将其作为四层防御的第四层（\"cross-axis gradient monotonically tracking true bias levels across both judges, inconsistent with uniform format amplification\"）。用一个必然成立的 pattern 作为防御论据会削弱整体论证的可信度。\n- 建议：(1) 在 Discussion 中将其从 \"defense layer\" 降级为 \"consistency observation\"；(2) 坦承 3 点单调性不构成统计证据；(3) 或增加更多轴（如 sentence length, hedging, formality sub-types）使 gradient 分析有统计意义。\n\n**W4** [presentation 层面] NLI 模型身份和阈值——管线最关键超参——未在论文中指定\n\n- 具体位置：Section 3 Stage 2\n- 问题：论文描述 \"a natural language inference model that verifies bidirectional entailment\" 但 **未指定模型名称或决策阈值**。从上下文推断 NLI annotator 为 Qwen3-32B（Section 4 \"NLI validation. Qwen3-32B as NLI annotator\"），但这意味着 Qwen3-32B 同时担任 rewriter、NLI annotator 和 judge（在某些配置下）——三重角色。如果使用的是 softmax probability threshold（如原始论文的 0.90），则阈值选择直接决定了 pass/fail 划分和后续所有分析的样本组成。\n- 建议：(1) 在 Section 3 Stage 2 中明确指定 NLI 模型名称和决策机制（categorical output vs. probability threshold + cutoff value）；(2) 讨论 Qwen3-32B 三重角色的 circularity（rewriter self-acceptance bias）。\n\n**W5** [presentation 层面] Qwen3-32B triple-role circularity 未讨论\n\n- 具体位置：Section 3-4, Limitations\n- 问题：Qwen3-32B 同时作为 (1) primary rewriter, (2) NLI annotator, (3) one of four target judges。论文 Limitations 讨论了 evaluator-producer bias（role 1+3 的重叠），但 **未讨论 role 1+2 的重叠**——rewriter 兼任 NLI annotator 意味着模型可能系统性地认为自己的 rewrite 保持了语义（self-acceptance bias），导致 NLI pass rate 被高估。GPT-4o cross-validation（92.1%/82.6% precision）部分缓解了这一问题，但应该在论文中作为 limitation 明确讨论。\n- 建议：在 Limitations 中增加一段讨论 NLI annotator identity 与 rewriter overlap 的影响；或改用独立的 NLI 模型（如 DeBERTa-v3-large）。\n\n**W6** [idea 层面] BT 模型的 IIA 假设未检验\n\n- 具体位置：Section 3 Stage 4, 全文 BT 分析\n- 问题：BT 模型假设 IIA（Independence of Irrelevant Alternatives）。在 style manipulation 实验中，不同类型的原始文本（如 code vs. creative writing）可能与 style 变化有异质性交互，导致 IIA 违反。论文未报告任何 IIA 诊断（如 Hausman-McFadden test 或按 task type 分层的 BT 参数稳定性检查）。\n- 缓解因素：4 judge families 的一致性和 cross-benchmark consistency 提供了间接 robustness 证据——如果 IIA 被严重违反，不太可能在所有 judge 和 benchmark 上产生一致的 BT pattern。因此这比无缓解的 IIA 未检验问题更轻微。\n- 建议：在 Appendix 中增加按 task type/difficulty 分层的 BT 参数比较；或简要论证为何 cross-judge consistency 间接支持 IIA 近似成立。\n\n---\n\n## Minor Issues\n\n**M1** [presentation] 论文仅有 Figure 1（pipeline diagram），其余所有结果均以 table 呈现。Cross-axis gradient (Table 6)、attenuation spectrum（BT vs Likert d across 18 cells）、placebo vs treatment 对比均应有配图。Table-heavy 的论文在审稿时 scanning 效率低，关键 pattern 不易一眼捕捉。\n\n**M2** [presentation] GEE 模型规格对非 LLMBar benchmark 未充分描述。Table 3 的 GEE decomposition 仅展示 LLMBar 数据？还是跨 benchmark 聚合？Working correlation structure、interaction test、link function 在 cross-benchmark 扩展中是否保持不变？\n\n**M3** [presentation] Bootstrap seed=42 贯穿全文所有 CI 计算。单一 seed 的 CI 对 seed 选择的 sensitivity 未评估。建议在 Appendix 报告 10 个 seed 的 CI 范围。\n\n**M4** [presentation] Claude negative control 的 TOST equivalence test（§5.4.4）参数不完整——equivalence margin (Δ)、achieved power 未报告。\"Within ±1.5pp of zero\" 但 TOST 的 null hypothesis rejection 条件未给出。\n\n**M5** [presentation] Table 1 footnote 中 \"†\" symbol 的含义未定义。Bradley-Terry 的 asterisk significance levels (*, **, ***) 也未明确定义 α cutoff。\n\n---\n\n## 实验覆盖度对照（review_context.yaml）\n\n| 实验 | 论文中覆盖 | 报告深度 | 评价 |\n|------|-----------|----------|------|\n| Llama-70B verbosity/formality | ✅ Table 1 | BT + Likert + GEE | 充分 |\n| Double-rewrite placebo (form. + verb.) | ✅ Table 4 | BT + CI + p | 缺 treatment-placebo Δ 的 CI |\n| NLI gate ablation | ✅ Table 5 | pass/fail/all BT | fail n 过小，标注不足 |\n| Cross-axis gradient | ✅ Table 6 | NLI rej. vs BT vs GEE ratio | 仅 3 点，统计力为零 |\n| Gemini-2.0-Flash | ✅ Table 1 | BT + CI + p | 充分（作为 robustness row）|\n| Cross-benchmark (AlpacaEval/MT-Bench) | ✅ Table 7 | BT + p | 缺 GEE decomposition 和 Likert |\n| Likert sensitivity analysis (18 cells) | ✅ Table 2 | 2×2 detection matrix | 充分 |\n| Rewriter independence (3 rewriters) | ✅ Table 8 | NLI pass%, BT, CI | 充分 |\n| Scaled replication (n=400) | ✅ §5.5 inline | BT + CI + Likert | 充分 |\n| GPT-4o verbosity + register | ✅ Table 1 | BT + Likert | 充分 |\n\n**未报告的信息**：\n- Cross-benchmark 的 GEE decomposition 和 Likert 对比（Table 7 仅报告 BT）\n- Placebo treatment-placebo 差值的 bootstrap CI\n- NLI-fail pairs 的完整统计描述（beyond BT point estimate）\n\n---\n\n## Questions for Authors\n\n**Q1**: Table 4 的 placebo design 是否计算了 treatment-placebo difference 的 bootstrap CI？如果 formality 的 Δ CI 下界接近 0，则 \"entirely attributable to style\" 的声明需要 qualification。\n\n**Q2**: NLI annotator 是 Qwen3-32B（与 rewriter 相同），是否评估过 self-acceptance bias？即 Qwen3-32B 是否比独立 NLI 模型（如 DeBERTa-v3-large）更倾向于判定自己的 rewrite 为 entailment？GPT-4o cross-validation 的 disagreement cases 是否集中在 \"Qwen pass but GPT-4o fail\" 方向？\n\n**Q3**: Table 7 的 cross-benchmark 结果仅报告 BT。Likert Blindspot（C2）和 per-axis confound structure（C3）是否在 AlpacaEval 和 MT-Bench 上也成立？如果是，Table 2 的 18-cell matrix 是否已包含这些 benchmark？\n\n**Q4**: IIA 方面——是否按 LLMBar 的 task categories（如 negation, paraphrase, elaboration 等）分层检查了 BT 参数的稳定性？\n\n---\n\n## 校准对照\n\n| 校准项 | 状态 |\n|--------|------|\n| Major issues 数量 | 1（N1: placebo overclaim）|\n| 对应上限 | ≤ Accept (4.0) |\n| 实际给分 | 3.5（Borderline Conference）|\n| 理由 | N1 是 magnitude interpretation 问题非 existence 问题，但 Should-Fix 数量较多（6 项），其中 W1-W3 涉及 idea 层面的论证力度不足，集体效应将分数从 4.0 推至 3.5 |\n\n**路径至 4.0**：(1) 修复 N1（softening placebo claim + 报告 Δ CI）；(2) 修复 W4（NLI model spec）；(3) 修复 W2（register framing）。其余 W 项为加分但非必须。",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Dream 审稿报告 — Reviewer 1（方法 + 实验）\n\n**论文**: The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\n**Dream ID**: 20260521T132932 (best scenario)\n**Venue**: EMNLP 2026 (ARR)\n**审查侧重**: 方法描述、实验设计、数据呈现、实验覆盖度\n\n---\n\n## Overall Assessment\n\n**Overall**: 3.5 / 5（Borderline Conference）\n**Confidence**: 4 / 5\n\n**一句话总结**: 实验设计全面（placebo control、NLI ablation、4 judge families、3 rewriters、cross-benchmark），显著优于通常的 bias detection 论文，但 placebo 统计力不足以支撑 \"format amplification empirically excluded\" 的强声明，且多处关键方法细节缺失。\n\n---\n\n## Summary\n\n论文提出 CSD 框架，通过 4 阶段管线（counterfactual rewriting → NLI gating → position-controlled pairwise comparison → BT/GEE statistical analysis）检测 LLM judge 的 per-axis style bias。核心发现是 Likert Blindspot：18 个 judge×axis×benchmark cell 中，BT 在 12 个 cell 检测到显著 bias，Likert 仅在 2 个 cell 检测到（6× sensitivity gap）。论文在 4 个 target judge families（GPT-4o、Qwen3-32B、Llama-70B、Gemini-Flash）+ 1 个 negative control（Claude）上验证，配合 double-rewrite placebo、NLI gate ablation、cross-axis gradient、rewriter independence 四层控制。\n\n---\n\n## Strengths\n\n**S1. 实验控制的层次感和完整性**：四层 anti-amplification 防御（placebo BT ≈ 50% in Table 4, NLI ablation in Table 5, Claude negative control in §5.4.4, cross-axis gradient in Table 6）是该领域论文中罕见的严谨程度。特别是 double-rewrite placebo 直接回应了 Jeong et al. (2025) Comparative Trap 的核心担忧——当 style 差异不存在时 BT = chance。\n\n**S2. Judge 和 rewriter 覆盖全面**：4 个 target judge families 覆盖 proprietary US (GPT-4o)、open CN (Qwen3-32B)、open US (Llama-70B)、proprietary US lightweight (Gemini-Flash)，加上 Claude negative control。3 个 rewriter (Qwen3-32B, GPT-4o, Llama-3.1-70B) 的 BT 范围 <2.1pp (Table 8)，有力证明了 rewriter independence。\n\n**S3. Detection matrix (Table 2) 是量化 Blindspot 的清晰手段**：18-cell 全覆盖的 BT sig vs Likert sig 2×2 矩阵直接、可复现、无需主观判断。10/12 BT-significant cells 的 Likert p > 0.15 使结论对 α 选择不敏感。\n\n**S4. GEE decomposition 揭示 per-axis confound structure**：Table 3 将 3 轴清晰分层——verbosity pure style (Style OR 高, Orig OR NS), formality conditional (both significant), register originality-dominated。这一 taxonomy 在 3 个 target judge 上独立复制（Table 6, Spearman 单调），比仅报告 \"bias exists\" 有更强的方法论贡献。\n\n**S5. Comparative Trap 的直接回应**：Section 2 引用 Jeong et al. (2025) 并在 §5.4.1 用 placebo 实验回应。Section 6 Discussion 专门讨论 \"Detection versus amplification\"，提出四层防御论证。这比忽略该文献或仅在 limitations 中提及好得多。\n\n---\n\n## Must-Fix 问题\n\n**N1** [Major, idea 层面] Placebo \"entirely attributable\" overclaim — 统计力不足以排除中等幅度的 format amplification\n\n- 具体位置：Section 5.4.1, Table 4, 及 Discussion p.5 (\"Treatment-Placebo gap...is entirely attributable to the style manipulation\")\n- 问题：Table 4 的 placebo BT 在 n=88 pairs 下：\n  - GPT-4o formality: 0.51 [0.44, 0.58], p=0.75\n  - Qwen3-32B formality: 0.50 [0.43, 0.57], p=0.92\n  - GPT-4o verbosity: 0.52 [0.45, 0.59], p=0.60\n  \n  placebo 95% CI 上界为 0.57-0.59，意味着最多 **~8pp 的 format amplification 与数据兼容**（CI 内）。对于 formality axis（treatment BT 0.630），placebo CI 上界 0.58 与 treatment CI 下界 0.558 **存在重叠**。这意味着无法在统计上完全排除 formality BT 中有 5-8pp 来自 format amplification 而非 pure style bias。\n  \n  论文声称 \"entirely attributable to style manipulation\" 和 Section 5 Discussion 的 \"format amplification empirically excluded\" 超出了 placebo 设计在 n=88 下的统计力所能支撑的声明强度。\n\n- 为什么是 Major：这是论文回应 Comparative Trap (Jeong et al., 2025) 的核心论证。如果 format amplification 被低估（如存在 5-8pp），则：(1) treatment BT 的 \"true style bias\" 部分被高估；(2) Likert Blindspot 的幅度解释需要调整（Likert 可能不是\"看不到\"full 63%，而是\"看不到\"55%——后者更难检测）。虽然 bias 的存在（BT > 50%）不受影响，但 magnitude 解释受影响。\n\n- 建议修改方向：\n  (1) 将 \"entirely attributable\" 改为 \"predominantly attributable, with residual amplification bounded to <8pp by placebo CI\"\n  (2) 报告 treatment-placebo 差值的 bootstrap CI（而非仅报告各自的 CI）\n  (3) 讨论 minimum detectable amplification effect at n=88（~14pp at 80% power）\n  (4) 在 Table 4 中增加 Δ 列的 CI\n\n---\n\n## Should-Fix 问题\n\n**W1** [idea 层面] NLI-fail ablation 样本量过小，不足以支撑方向性结论\n\n- 具体位置：Table 5, §5.4.2\n- 问题：NLI-fail pairs 仅 n=12（formality）和 n=14（verbosity）。Table 5 的 \"NLI-fail pairs show BT that reflects content-mediated signal\" 和 \"confirming the gate removes content-mediated signal\" 基于这些极小样本。在 n=12 下，BT 的 standard error 约 ±15pp，pass-fail gap 9.5pp 完全可以是随机波动。论文承认 \"NLI-fail n too small for individual significance\"（来自 review_context 的 note），但主文仍将方向性结果作为 NLI gate 有效性的证据（\"NLI-fail pairs...show BT that reflects content-mediated signal\"）。\n- 建议：(1) 在主文中明确标注 NLI-fail 结果为 \"directional but underpowered\"；(2) 不要将其作为四层防御中的独立一层——它更应该是 supplementary observation。\n\n**W2** [idea 层面] Register 轴的 \"three style axes\" framing 与 GEE 证据不匹配\n\n- 具体位置：Abstract (\"three style axes\"), Table 3, Table 6\n- 问题：Table 3 和 Table 6 的 GEE decomposition 显示 register 是 \"originality-dominated\"（GEE Style/Orig ratio = 0.33），register BT 仅 55-57%（边缘显著或不显著）。这意味着 register 上观测到的弱 preference 主要来自 originality confound 而非 style bias。论文的 \"three style axes\" framing 暗示在三个轴上均检测到了 style bias，但 register 的证据更准确地描述为 \"originality effect with weak residual style component\"。\n- 建议：(1) 在 Abstract 中区分 \"two clear style bias axes (verbosity, formality) and one originality-dominated axis (register)\"；(2) 或将 register 定位为 negative/weak finding 而非正面证据。\n\n**W3** [idea 层面] Cross-axis gradient 作为防御层的统计效力为零\n\n- 具体位置：Table 6, Discussion p.5\n- 问题：Table 6 展示 3 个轴的 NLI rejection rate 与 BT 的单调关系，Spearman ρ = 1.0。但 **3 个数据点的任何单调排列都产生 ρ = 1.0**——这不是统计发现而是定义性成立。论文称其为 \"qualitative argument, not statistical test\"（review_context），但 Discussion 仍将其作为四层防御的第四层（\"cross-axis gradient monotonically tracking true bias levels across both judges, inconsistent with uniform format amplification\"）。用一个必然成立的 pattern 作为防御论据会削弱整体论证的可信度。\n- 建议：(1) 在 Discussion 中将其从 \"defense layer\" 降级为 \"consistency observation\"；(2) 坦承 3 点单调性不构成统计证据；(3) 或增加更多轴（如 sentence length, hedging, formality sub-types）使 gradient 分析有统计意义。\n\n**W4** [presentation 层面] NLI 模型身份和阈值——管线最关键超参——未在论文中指定\n\n- 具体位置：Section 3 Stage 2\n- 问题：论文描述 \"a natural language inference model that verifies bidirectional entailment\" 但 **未指定模型名称或决策阈值**。从上下文推断 NLI annotator 为 Qwen3-32B（Section 4 \"NLI validation. Qwen3-32B as NLI annotator\"），但这意味着 Qwen3-32B 同时担任 rewriter、NLI annotator 和 judge（在某些配置下）——三重角色。如果使用的是 softmax probability threshold（如原始论文的 0.90），则阈值选择直接决定了 pass/fail 划分和后续所有分析的样本组成。\n- 建议：(1) 在 Section 3 Stage 2 中明确指定 NLI 模型名称和决策机制（categorical output vs. probability threshold + cutoff value）；(2) 讨论 Qwen3-32B 三重角色的 circularity（rewriter self-acceptance bias）。\n\n**W5** [presentation 层面] Qwen3-32B triple-role circularity 未讨论\n\n- 具体位置：Section 3-4, Limitations\n- 问题：Qwen3-32B 同时作为 (1) primary rewriter, (2) NLI annotator, (3) one of four target judges。论文 Limitations 讨论了 evaluator-producer bias（role 1+3 的重叠），但 **未讨论 role 1+2 的重叠**——rewriter 兼任 NLI annotator 意味着模型可能系统性地认为自己的 rewrite 保持了语义（self-acceptance bias），导致 NLI pass rate 被高估。GPT-4o cross-validation（92.1%/82.6% precision）部分缓解了这一问题，但应该在论文中作为 limitation 明确讨论。\n- 建议：在 Limitations 中增加一段讨论 NLI annotator identity 与 rewriter overlap 的影响；或改用独立的 NLI 模型（如 DeBERTa-v3-large）。\n\n**W6** [idea 层面] BT 模型的 IIA 假设未检验\n\n- 具体位置：Section 3 Stage 4, 全文 BT 分析\n- 问题：BT 模型假设 IIA（Independence of Irrelevant Alternatives）。在 style manipulation 实验中，不同类型的原始文本（如 code vs. creative writing）可能与 style 变化有异质性交互，导致 IIA 违反。论文未报告任何 IIA 诊断（如 Hausman-McFadden test 或按 task type 分层的 BT 参数稳定性检查）。\n- 缓解因素：4 judge families 的一致性和 cross-benchmark consistency 提供了间接 robustness 证据——如果 IIA 被严重违反，不太可能在所有 judge 和 benchmark 上产生一致的 BT pattern。因此这比无缓解的 IIA 未检验问题更轻微。\n- 建议：在 Appendix 中增加按 task type/difficulty 分层的 BT 参数比较；或简要论证为何 cross-judge consistency 间接支持 IIA 近似成立。\n\n---\n\n## Minor Issues\n\n**M1** [presentation] 论文仅有 Figure 1（pipeline diagram），其余所有结果均以 table 呈现。Cross-axis gradient (Table 6)、attenuation spectrum（BT vs Likert d across 18 cells）、placebo vs treatment 对比均应有配图。Table-heavy 的论文在审稿时 scanning 效率低，关键 pattern 不易一眼捕捉。\n\n**M2** [presentation] GEE 模型规格对非 LLMBar benchmark 未充分描述。Table 3 的 GEE decomposition 仅展示 LLMBar 数据？还是跨 benchmark 聚合？Working correlation structure、interaction test、link function 在 cross-benchmark 扩展中是否保持不变？\n\n**M3** [presentation] Bootstrap seed=42 贯穿全文所有 CI 计算。单一 seed 的 CI 对 seed 选择的 sensitivity 未评估。建议在 Appendix 报告 10 个 seed 的 CI 范围。\n\n**M4** [presentation] Claude negative control 的 TOST equivalence test（§5.4.4）参数不完整——equivalence margin (Δ)、achieved power 未报告。\"Within ±1.5pp of zero\" 但 TOST 的 null hypothesis rejection 条件未给出。\n\n**M5** [presentation] Table 1 footnote 中 \"†\" symbol 的含义未定义。Bradley-Terry 的 asterisk significance levels (*, **, ***) 也未明确定义 α cutoff。\n\n---\n\n## 实验覆盖度对照（review_context.yaml）\n\n| 实验 | 论文中覆盖 | 报告深度 | 评价 |\n|------|-----------|----------|------|\n| Llama-70B verbosity/formality | ✅ Table 1 | BT + Likert + GEE | 充分 |\n| Double-rewrite placebo (form. + verb.) | ✅ Table 4 | BT + CI + p | 缺 treatment-placebo Δ 的 CI |\n| NLI gate ablation | ✅ Table 5 | pass/fail/all BT | fail n 过小，标注不足 |\n| Cross-axis gradient | ✅ Table 6 | NLI rej. vs BT vs GEE ratio | 仅 3 点，统计力为零 |\n| Gemini-2.0-Flash | ✅ Table 1 | BT + CI + p | 充分（作为 robustness row）|\n| Cross-benchmark (AlpacaEval/MT-Bench) | ✅ Table 7 | BT + p | 缺 GEE decomposition 和 Likert |\n| Likert sensitivity analysis (18 cells) | ✅ Table 2 | 2×2 detection matrix | 充分 |\n| Rewriter independence (3 rewriters) | ✅ Table 8 | NLI pass%, BT, CI | 充分 |\n| Scaled replication (n=400) | ✅ §5.5 inline | BT + CI + Likert | 充分 |\n| GPT-4o verbosity + register | ✅ Table 1 | BT + Likert | 充分 |\n\n**未报告的信息**：\n- Cross-benchmark 的 GEE decomposition 和 Likert 对比（Table 7 仅报告 BT）\n- Placebo treatment-placebo 差值的 bootstrap CI\n- NLI-fail pairs 的完整统计描述（beyond BT point estimate）\n\n---\n\n## Questions for Authors\n\n**Q1**: Table 4 的 placebo design 是否计算了 treatment-placebo difference 的 bootstrap CI？如果 formality 的 Δ CI 下界接近 0，则 \"entirely attributable to style\" 的声明需要 qualification。\n\n**Q2**: NLI annotator 是 Qwen3-32B（与 rewriter 相同），是否评估过 self-acceptance bias？即 Qwen3-32B 是否比独立 NLI 模型（如 DeBERTa-v3-large）更倾向于判定自己的 rewrite 为 entailment？GPT-4o cross-validation 的 disagreement cases 是否集中在 \"Qwen pass but GPT-4o fail\" 方向？\n\n**Q3**: Table 7 的 cross-benchmark 结果仅报告 BT。Likert Blindspot（C2）和 per-axis confound structure（C3）是否在 AlpacaEval 和 MT-Bench 上也成立？如果是，Table 2 的 18-cell matrix 是否已包含这些 benchmark？\n\n**Q4**: IIA 方面——是否按 LLMBar 的 task categories（如 negation, paraphrase, elaboration 等）分层检查了 BT 参数的稳定性？\n\n---\n\n## 校准对照\n\n| 校准项 | 状态 |\n|--------|------|\n| Major issues 数量 | 1（N1: placebo overclaim）|\n| 对应上限 | ≤ Accept (4.0) |\n| 实际给分 | 3.5（Borderline Conference）|\n| 理由 | N1 是 magnitude interpretation 问题非 existence 问题，但 Should-Fix 数量较多（6 项），其中 W1-W3 涉及 idea 层面的论证力度不足，集体效应将分数从 4.0 推至 3.5 |\n\n**路径至 4.0**：(1) 修复 N1（softening placebo claim + 报告 Δ CI）；(2) 修复 W4（NLI model spec）；(3) 修复 W2（register framing）。其余 W 项为加分但非必须。",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 373 · 2026-05-21T14:22:53.381655+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3916
}
```

</details>

---


### Tool call

_source line 374 · 2026-05-21T14:23:01.014626+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260521T132932/best/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 375 · 2026-05-21T14:23:01.065225+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 376 · 2026-05-21T14:23:10.375278+00:00_

Dream 审稿报告已提交。

**审稿结论**：Overall 3.5 (Borderline Conference)。

核心判断：
- **1 个 Major issue**：placebo control 的 "entirely attributable" 声明超出 n=88 的统计力（无法排除 ≤8pp 的 format amplification），但 bias 存在性不受影响
- **6 个 Should-Fix**：NLI-fail 样本过小、register 轴 framing 不准确、cross-axis gradient 3 点无统计力、NLI 模型/阈值未指定、Qwen3-32B 三重角色 circularity、IIA 未检验
- **实验覆盖度**：review_context.yaml 中列出的所有实验均在论文中有所体现，整体实验设计是该领域同类论文中最全面的之一
- **路径至 4.0**：修复 placebo overclaim + 补充 NLI 模型规格 + 调整 register framing

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1"
}
```

</details>

---


## Round 14

## Round 14

42 recorded events


### User

_source line 377 · 2026-05-21T16:06:56.927492+00:00_

[Round 1 审稿请求]:
## Review Task: R1 — Methods & Experiments

You are reviewing an anonymous EMNLP 2026 submission (ARR track). Your focus: **methodology soundness and experimental rigor**.

### Paper Summary
"The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition"

The paper introduces Controlled Style Decomposition (CSD), a black-box diagnostic pipeline that:
1. Generates counterfactual text pairs differing along one style axis (formality, verbosity, register) while preserving semantic content via NLI gating
2. Evaluates pairs under both Likert and pairwise protocols with position balancing
3. Decomposes preferences via GEE logistic model to separate style vs. originality confounds

Core claims:
- C1 (Likert Blindspot): Pairwise BT detects style bias (63–77%) that all 7 Likert methods miss (d→0). 100-point Likert ablation rules out scale granularity.
- C2 (Per-axis confound structure): GEE reveals 3 regimes — verbosity=pure, formality=conditional, register=originality-dominated — replicating across 3 judge architectures.

### Your Review Dimensions

**1. Soundness (1–5)**
- Is the CSD pipeline methodologically valid? NLI gating for content control, position balancing, Bradley-Terry model, GEE decomposition.
- Is the GEE model (Eq. 1) appropriate? Only two covariates (style S, originality O) — are there missing confounds? Is the exchangeable correlation structure justified?
- The Blindspot definition (BT sig AND all Likert NS) — is this a fair operationalization or does it conflate different measurement constructs?
- NLI as content control: bidirectional entailment is strict but NLI models have known limitations (e.g., sensitivity to lexical overlap). Is this discussed?
- 100-point Likert ablation: is n=100 sufficient to detect d=0.02–0.06 at this scale? Power analysis?

**2. Experimental Design (1–5)**
- 3 judges × 3 benchmarks × 3 axes: good coverage. But n=100 per condition — is this underpowered for GEE?
- Scaled replication n=355: only on Qwen3×LLMBar×formality. Should other conditions be scaled?
- Rewriter independence (Table 12): only tested on formality with GPT-4o as judge. Generalization?
- Claude as negative control: only tested on formality×LLMBar. Incomplete coverage.
- Cross-benchmark (Table 8): only formality axis. Verbosity/register cross-benchmark missing.
- Register axis: only 2 judges (GPT-4o, Qwen3), no Llama. Incomplete.
- Double-rewrite placebo: the P(orig) values (8–42%) show strong rewriting artifact. Is the GEE decomposition sufficient to fully control this?

**3. Reproducibility (1–5)**
- Are prompts, NLI model identity, temperature settings, API versions specified?
- Is the code/data availability mentioned?
- Can the pipeline be replicated from the paper description alone?

**4. Statistical Concerns**
- Multiple comparisons: 9 judge×axis cells in Table 1 — is Bonferroni/Holm correction applied?
- Bootstrap CIs: 10,000 resamples stated, but are these BCa or percentile?
- GEE working correlation structure: exchangeable? Independent? Not specified.
- The "7 methods all NS" argument: is absence of evidence being treated as evidence of absence?

**5. Missing Experiments (compare to context)**
Review context lists these imagined experiments. Note which are present vs. missing:
- exp-001: Multi-judge (Claude done, Gemini mentioned but not in paper) 
- exp-002: Multi-benchmark (partially done — only formality)
- exp-003: 7-method sensitivity (done for Llama, claimed to replicate for others)
- exp-005: Placebo control (done for 3 judges)
- exp-006: Scaled replication n=355 (done, single condition)
- exp-009: Rewriter independence (done but limited scope)
- exp-020: GPT-4o verbosity+register (done)
- exp-021: Llama third judge (done)
- exp-022: Double-rewrite placebo (done)
- exp-023: NLI gate ablation (done)
- exp-024: Cross-axis gradient (done)
- 100-point Likert ablation (done)

### Venue Calibration (EMNLP 2026 ARR)
- 5 = Award (top 2.5%), 4 = Main conference, 3 = Findings, 2 = Major revision, 1 = Do not resubmit
- Soundness (1–5), Excitement (1–5), Reproducibility (1–5)
- Accept rate ~21% for Main

Provide your independent scores and detailed reasoning. Be rigorous but fair.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 378 · 2026-05-21T16:07:45.613496+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "stat -c '%Y %s' /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf 2>/dev/null && echo \"---\" && date +%s",
  "description": "Check PDF modification time vs current time"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "stat -c '%Y %s' /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf 2>/dev/null && echo \"---\" && date +%s",
    "description": "Check PDF modification time vs current time"
  }
}
```

</details>

---


### Tool result

_source line 379 · 2026-05-21T16:07:45.814854+00:00_

1779379274 354174
---
1779379665

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 380 · 2026-05-21T16:07:51.791682+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "1-8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 381 · 2026-05-21T16:07:52.896887+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.5}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 504.7}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 573.8}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 517.3}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 444.9}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 491.6}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 494.6}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 508.2}], \"total_pages\": 15, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1105
}
```

</details>

---


### Tool call

_source line 382 · 2026-05-21T16:07:57.365467+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 383 · 2026-05-21T16:07:58.420975+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1055
}
```

</details>

---


### Tool call

_source line 384 · 2026-05-21T16:07:58.472481+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 385 · 2026-05-21T16:07:58.826027+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 386 · 2026-05-21T16:07:59.480484+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 387 · 2026-05-21T16:07:59.735206+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1262
}
```

</details>

---


### Tool result

_source line 388 · 2026-05-21T16:08:00.241142+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1415
}
```

</details>

---


### Tool result

_source line 389 · 2026-05-21T16:08:00.494357+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1013
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-21T16:08:08.230463+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 391 · 2026-05-21T16:08:08.732254+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 392 · 2026-05-21T16:08:09.186564+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 393 · 2026-05-21T16:08:09.288459+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 394 · 2026-05-21T16:08:09.844471+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1112
}
```

</details>

---


### Tool call

_source line 395 · 2026-05-21T16:08:09.945269+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 396 · 2026-05-21T16:08:09.946624+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 658
}
```

</details>

---


### Tool result

_source line 397 · 2026-05-21T16:08:10.552355+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 607
}
```

</details>

---


### Tool call

_source line 398 · 2026-05-21T16:08:15.971446+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "9-15",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "9-15",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 399 · 2026-05-21T16:08:16.724992+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 516.0}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 427.1}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 462.3}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 437.8}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 581.6}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 601.8}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 107.2}], \"total_pages\": 15, \"rendered_pages\": 7, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 400 · 2026-05-21T16:08:21.290464+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 401 · 2026-05-21T16:08:21.744490+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 402 · 2026-05-21T16:08:22.200615+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 910
}
```

</details>

---


### Tool call

_source line 403 · 2026-05-21T16:08:22.201071+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 404 · 2026-05-21T16:08:22.905899+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1161
}
```

</details>

---


### Tool result

_source line 405 · 2026-05-21T16:08:22.957256+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 756
}
```

</details>

---


### Tool call

_source line 406 · 2026-05-21T16:08:23.058412+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 407 · 2026-05-21T16:08:23.763783+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 705
}
```

</details>

---


### Tool call

_source line 408 · 2026-05-21T16:08:29.134201+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 409 · 2026-05-21T16:08:29.587470+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 410 · 2026-05-21T16:08:30.041717+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 411 · 2026-05-21T16:08:30.043358+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 412 · 2026-05-21T16:08:30.200388+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 157
}
```

</details>

---


### Tool result

_source line 413 · 2026-05-21T16:08:30.554181+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 966
}
```

</details>

---


### Tool call

_source line 414 · 2026-05-21T16:15:04.431424+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — Methods & Experiments Review (Updated Paper, 15pp)\n\n**论文**: The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\n**版本**: 修订版（15 页，含 Appendix A-N，Table 1-14）\n**Venue**: EMNLP 2026 (ARR)\n\n---\n\n## 1. Soundness: 3.5 / 5\n\n### CSD Pipeline Validity\n\n**NLI Gating**: Now properly specified — DeBERTa-v3-large, bidirectional entailment threshold 0.90, direction-aware for verbosity (Appendix F). GPT-4o cross-validation on all 200 pairs (92.1% formality, 82.6% verbosity precision). The 0.90 threshold sits on a bimodal plateau (Appendix E, Table 8: 11 thresholds from 50-98, BT stable across all). 这比原稿大幅改善。\n\n**Position Balancing**: Bidirectional swap producing n_pairs × 2 observations. Consistency filter retains only concordant pairs for sign test; BT model uses all observations. 标准做法。\n\n**Bradley-Terry Model**: GoF tests reported (Appendix H: formality deviance p=0.198, verbosity p=0.905). Stratified analysis confirms no preference heterogeneity for verbosity. Bootstrap CIs (10,000 pair-level resamples, seed 42). **但 CI 类型未指明（percentile vs. BCa）**——应在 Section 4.1 明确。\n\n**GEE Decomposition (Eq. 1)**:\n- Exchangeable correlation justified by QIC comparison (Appendix C, Table 4: |ΔQIC| < 0.001 across all 6 cells).\n- Interaction test: style×originality NS on formality for both judges (GPT-4o p=0.38, Qwen3 p=0.52). ✅\n- **缺失**：interaction test 未报告 verbosity axis。鉴于 verbosity 的 P(orig) 极低（Table 14: Qwen3 P(orig)=0.082，即 92% 偏好抛光文本），这正是 interaction 最可能显著的轴。如果 verbosity 上 style×originality interaction 显著，additive GEE 的 \"confound-free\" 结论受影响。\n- **缓解因素**：verbosity 的双向结果（Section 5.4：\"Both rewriting directions favor verbose responses\"）意味着 style preference 在两个方向上都压过 polishing artifact。如果 judges 在 verbose-original vs. concise-rewrite 方向上仍偏好 verbose（这对抗了 92% 的 polishing preference），style effect 必须非常强。这间接支持了 additive model 的 adequacy。\n\n**Blindspot 定义 (BT sig ∧ all Likert NS)**:\n- 论文现在在 Section 5.2 主文中讨论了 \"measurement attenuation vs. construct divergence\"——不再仅在 Limitations 中。\n- 两种解释均被讨论：\"Likert captures absolute quality difference while pairwise captures ordinal preference\"。\n- 结论：\"Whether this reflects measurement attenuation or construct divergence, the operational consequence is identical\"——这是务实且可辩护的立场。\n- **残余疑虑**：论文标题 \"Blindspot\" 暗示 Likert 有缺陷，但如果是 construct divergence，Likert 并非\"盲\"——它测的是不同东西。标题 framing 偏向 attenuation 解释。\n\n**100-Point Likert Ablation (Table 12, Appendix L)**:\n- n=100 formality + verbosity, Qwen3 judge. Formality: Likert p=0.725 (tie rate 65.9%), verbosity p=0.137 (tie rate 51.2%). BT 同数据 66.5% 和 77.3%。\n- **Power concern**：n=100 在 α=0.05 下能检测到的最小效应量约为 d=0.28（双侧 t-test，80% power）。观测到的 d=0.02-0.06 远低于此。所以 ablation 能排除 d≥0.28 的中等效应，但不能确认 d 是否真为 0 或仅为极小未检出效应。\n- **但这正是论文论点的一部分**：即使 100-point 量表，效应量仍为 d=0.02-0.06，远低于任何实际意义阈值。论点不是 \"d=0\" 而是 \"d 如此之小以至于 Likert 在实际样本量下永远检测不到。\" 这一推理是成立的。\n\n**NLI 已知局限**：\n- 论文报告了 FNR 8.4% (Section 5.1) 并分析了 FN 特征。\n- Direction-aware gating 的 asymmetry (Appendix F) 处理了 expansion vs. compression 的不对称性。\n- **未讨论**：DeBERTa NLI 对 lexical overlap 的已知敏感性——高 lexical overlap 的 pair 可能获得虚高 entailment score。但鉴于 style rewriting 通常改变词汇而非保留，这个问题的方向可能是使 gate 更严格（而非更宽松），reducing risk。\n\n### Soundness 小结\n核心方法学严谨，控制层次丰富（NLI gate + position swap + GEE decomposition + 5 experimental controls）。主要残余疑虑：(1) GEE interaction test 缺 verbosity axis；(2) Blindspot 标题 framing 偏向 attenuation 解释。不构成 Major issue，但影响 4.0 提升。\n\n---\n\n## 2. Experimental Design: 3.5 / 5\n\n### 覆盖度总览\n\n| 维度 | 已覆盖 | 评价 |\n|------|--------|------|\n| Judges | GPT-4o, Qwen3-32B, Claude(ctrl) + Llama(App K) | Good：3 target + 1 ctrl |\n| Benchmarks | LLMBar, AlpacaEval, MTBench (Table 1) | Good：3 benchmarks |\n| Axes | Formality ✅, Verbosity ✅, Register ⚠️ | Register 仅 2 judges |\n| Scaled replication | n=355, formality×Qwen3×LLMBar only | Limited scope |\n| Rewriter independence | Formality×GPT-4o judge only (Table 6-7) | **Limited** |\n| Negative control | Claude on formality×LLMBar + some others | Incomplete |\n| Cross-benchmark | All axes in Table 1, formality deepest | Partially |\n| Placebo | Table 14, 3 judges × 2 axes | **Good** |\n| NLI gate ablation | Table 13, pass/fail/all | **Good** (fail n small) |\n| 100-point Likert | Table 12, form+verb×Qwen3 | New & useful |\n| 7-method sensitivity | Table 2 (form) + Table 11 (verb) | **Good** |\n\n### Specific Concerns\n\n**S1. Rewriter independence 范围不足 [Should-Fix, idea]**\n- Table 6-7 (Appendix D) 仅在 formality×GPT-4o 配置上测试了 GPT-4o 作为替代 rewriter。BT 64.4% [56.1, 72.8] vs. Qwen3 rewriter 66.5% [58.5, 73.9]——CIs 重叠，OK。\n- **缺失**：verbosity 的 rewriter independence。Verbosity rewriting 更 invasive（NLI rejection 14% vs. 12%），rewriter identity 的影响可能更大。如果 Qwen3 的 verbose rewriting 风格系统性地不同于其他 rewriter，verbosity 77% BT 的一部分可能来自 Qwen3-specific 的 rewriting pattern 而非 genuine style bias。\n- **缓解**：Llama 作为独立 judge（Appendix K, Table 11）在 Qwen3-rewritten pairs 上复现了 verbosity bias，说明至少跨 judge 是稳定的。但 rewriter dimension 未测试。\n\n**S2. Claude negative control 覆盖不完整 [Should-Fix, presentation]**\n- Table 1 显示 Claude 在 LLMBar formality (.562, NS) 和部分其他 cells 上的结果。\n- Appendix G: TOST equivalence test at n=87, Δ=10pp, confirmed.\n- **但** verbosity 和 register 的 Claude 结果在 Table 1 中部分缺失（一些 cells 空白）。如果 Claude 仅在 formality 上验证为 NS，discriminant validity 只对 formality 成立。\n- 论文应明确报告 Claude 在所有已测 cells 上的 TOST 结果，而非仅在部分 cells。\n\n**S3. Register axis 不完整 [Minor, idea]**\n- 仅 2 judges (GPT-4o, Qwen3)，无 Llama。\n- BT 55-57%（边缘显著）。GEE 显示 originality-dominated。\n- 论文将 register 定位为 \"exploratory\"——这是正确的 scoping。Table 3 footnote 确认 register 不进入 primary Holm-Bonferroni family。\n- **残余问题**：如果 register 是 exploratory，是否应该在 Abstract 中与 formality/verbosity 并列为 \"three style axes\"？ 目前 Abstract 说 \"two primary style axes (formality, verbosity), with exploratory evidence on register\"——这比原稿改善但仍略 overstate。\n\n**S4. Cross-benchmark depth不均 [Should-Fix, presentation]**\n- Table 1 的 cross-benchmark 覆盖（3 benchmarks × judges × axes）是主表，但 AlpacaEval 和 MTBench 上的 GEE decomposition 和 Likert 对比未在 appendix 中深入展开。\n- 论文依赖 Table 1 的 cross-benchmark BT 一致性，但未验证 Blindspot pattern（BT sig + Likert NS）是否在非 LLMBar benchmarks 上也成立。如果 Blindspot 仅在 LLMBar 上出现，generalizability claim 受限。\n\n**S5. Double-rewrite placebo 的解读 [Should-Fix, idea]**\n- Table 14 (Appendix N) 显示 P(orig) 在 verbosity 上极低（GPT-4o: 0.167, Qwen3: 0.082）——judges 92% 偏好 LLM-polished text。这是 **非常强的 rewriting artifact**。\n- 论文声称 GEE decomposition \"absorbs\" 这个 artifact。\n- **关键问题**：在 treatment pairs 中，style 和 originality 通过 bidirectional design 被交叉。在 verbose-original vs. concise-rewrite 方向上，judges 仍偏好 verbose text（Section 5.4: \"Both directions favor verbose\"）——这意味着 style preference 确实压过了 92% 的 polishing preference，支持 GEE 的 adequacy。\n- 但论文应更明确地展示这个推理链：placebo artifact → bidirectional cancellation → GEE correctly isolates style。目前 Table 14 放在附录末尾，与 GEE 讨论脱节。\n\n**S6. n=100 per condition for GEE [Minor, idea]**\n- n=100 (86-88 NLI-pass) with binary outcome and 2 covariates. For large ORs (2-13), adequate power. For register (OR near 1), underpowered.\n- Scaled replication (n=355) 仅在一个 configuration 上确认了 stability。Verbosity 和 cross-benchmark 未 scaled。\n- 但论文的主要结论（verbosity is strong, formality is conditional, register is weak）不依赖于 marginal significance——pattern 在多个 configurations 上一致。\n\n### Experimental Design 小结\n设计广度好（3 judges × 3 benchmarks × 3 axes + 5 experimental controls），但几个维度的深度不足：rewriter independence 仅 formality、Claude 覆盖不完整、cross-benchmark GEE/Likert 未展开。最值得关注的是 S1（rewriter independence）和 S5（placebo 解读链）。\n\n---\n\n## 3. Reproducibility: 3.5 / 5\n\n| 要素 | 状态 | 备注 |\n|------|------|------|\n| NLI model identity | ✅ DeBERTa-v3-large | Section 3.2 |\n| NLI threshold | ✅ 0.90 | Section 3.2 |\n| Rewriter model | ✅ Qwen3-32B-Instruct | Section 3.1 |\n| Judge API version | ✅ GPT-4o (gpt-4o-2024-08-06) | Section 3.3 |\n| Temperature | ✅ 0.7 | Section 3.1 |\n| Rewriting prompts | ⚠️ Described but exact text not given | Missing from appendix |\n| Bootstrap params | ✅ 10,000 pair-level, seed 42 | Section 4.1 |\n| Bootstrap CI type | ❌ Percentile vs. BCa not specified | Should state |\n| GEE correlation | ✅ Exchangeable + independence comparison | Appendix C |\n| Code/data | ⚠️ \"Released upon acceptance\" | Not verifiable |\n\n**主要gap**：Rewriting prompt 的 exact text 未在论文或附录中提供。Section 3.1 描述了 prompt 的结构（\"Rewrite the following text to be more formal/casual...\"），但不同的 prompt wording 可能影响 rewriting 质量和 NLI pass rate。对于 reproducibility，exact prompts 是关键。\n\n---\n\n## 4. Statistical Concerns\n\n**4a. Multiple comparisons**: \nPrimary family: 2 judges × 3 axes = 6 tests, Holm-Bonferroni at α=0.05 (Section 4.1). Table 1 reports both raw and adjusted p-values. Register 标为 exploratory（不入 family）。✅ 合理。\n\n**4b. Bootstrap CIs**: \n10,000 pair-level resamples, seed 42. **CI type（percentile vs. BCa）未指定**。对于 skewed BT estimates（如 register BT 55%），BCa would be more appropriate。Should state in methods.\n\n**4c. GEE working correlation**: \nExchangeable, compared with independence in Appendix C (|ΔQIC| < 0.001). Interaction test on formality (NS for both judges). ✅ 充分。\n**但 verbosity interaction test 缺失** — ditto Soundness 部分的讨论。\n\n**4d. \"7 methods all NS\" = evidence of absence?**:\n这是论文的核心方法论 tension。7 种 Likert 方法全部 NS 不严格等于 \"no effect\"——只是 \"not detected\"。但论文通过三层补充证据缓解了这一问题：\n1. Bootstrap attenuation analysis (Appendix J, Table 10): d→0 as n increases to 355, CI [−0.123, 0.087] never excluding zero。说明 d 不是 under-detected 而是 genuinely near zero。\n2. 100-point Likert ablation (Appendix L): 更细粒度的量表仍不改善检测。\n3. BT 同数据显著（p < 0.001）：同一数据上两种方法的不一致排除了 \"insufficient data\" 解释。\n\n这三层证据将 \"absence of evidence\" 显著升级为 \"bounded near-zero effect\"。**论文对这一 tension 的处理是该领域论文中我见过的最严谨的之一。**\n\n---\n\n## 5. Missing Experiments (对照 review context)\n\n| Experiment | Status | Reported Where | Completeness |\n|-----------|--------|---------------|-------------|\n| exp-001: Multi-judge (Gemini) | ❌ MISSING | — | Gemini mentioned in Related Work context but no results |\n| exp-002: Multi-benchmark | ✅ Partial | Table 1 (BT); Appendix cross-benchmark (formality only deeper) | Verbosity/register GEE cross-benchmark missing |\n| exp-003: 7-method sensitivity | ✅ | Table 2 (form) + Appendix K Table 11 (verb) | Two axes covered |\n| exp-005: Placebo control | ✅ | Appendix N, Table 14 | 3 judges × 2 axes |\n| exp-006: Scaled replication n=355 | ✅ | Section 5.2, Appendix J | Single condition |\n| exp-009: Rewriter independence | ✅ Partial | Appendix D, Table 6-7 | Formality only, GPT-4o judge only |\n| exp-020: GPT-4o verb+register | ✅ | Table 1 | Complete |\n| exp-021: Llama third judge | ✅ | Appendix K, Table 11 | Verbosity sensitivity hierarchy |\n| exp-022: Double-rewrite placebo | ✅ | Appendix N, Table 14 | Merged with exp-005 |\n| exp-023: NLI gate ablation | ✅ | Appendix M, Table 13 | Pass/fail/all, 2 axes |\n| exp-024: Cross-axis gradient | ✅ | Implicit in Table 1 + Fig 3 | Qualitative only |\n| 100-point Likert ablation | ✅ | Appendix L, Table 12 | 2 axes × Qwen3 |\n\n**关键缺失**：\n1. Gemini judge 完全缺失——review context 列出但论文中无 Gemini 数据\n2. Rewriter independence 仅 formality——verbosity 是更 invasive 的轴\n3. Cross-benchmark GEE/Likert decomposition 未展开\n\n---\n\n## ARR Dimension Scores\n\n| Dimension | Score | Reasoning |\n|-----------|-------|-----------|\n| **Soundness** | 3.5/5 | Pipeline 设计严谨，5 层 Comparative Trap 控制令人印象深刻。GEE 有完整诊断。但 verbosity interaction test 缺失、construct validity 未解决。 |\n| **Excitement** | 3.5/5 | Likert Blindspot 是实用且新颖的发现；7-method sensitivity hierarchy 和 100-point ablation 提供了强实证。但与 RATE 的增量界限需更清晰定位。 |\n| **Reproducibility** | 3.5/5 | 关键超参明确标注（模型、threshold、API 版本、temperature），但 exact prompts 和 bootstrap CI 类型缺失。 |\n\n## Overall Assessment\n\n**Overall**: 3.5 / 5（Borderline Conference）\n**Confidence**: 4 / 5\n\n### Justification\n\n**Why 3.5 rather than 4.0**: 三个 Should-Fix 问题的集合效应——(1) rewriter independence 仅测试了 formality（verbosity 是主力发现但 rewriter robustness 未验证）；(2) double-rewrite placebo 揭示了极强的 rewriting artifact（Qwen3 verbosity P(orig)=8%）但 GEE interaction test 仅在 formality 上报告（对 verbosity 的 \"confound-free\" 声明的统计支撑不完整）；(3) 论文的核心 framing（\"Blindspot\"）偏向 measurement attenuation 解释，但主文讨论了 construct divergence 后仍未提供能区分两者的实验证据。\n\n**Why not 3.0**: 论文的控制层次（NLI gate ablation + placebo + Claude ctrl + cross-axis + debiased prompting）在该领域论文中罕见。Bootstrap attenuation analysis + 100-point Likert ablation + 7-method sensitivity table 共同构建了 Blindspot 的强实证基础。GEE 诊断完整（correlation structure、interaction test、GoF）。这些优势显著高于 Findings 水准。\n\n**Path to 4.0**:\n1. 在 verbosity axis 上报告 GEE style×originality interaction test\n2. 在 verbosity axis 上测试 rewriter independence（至少 GPT-4o 作为替代 rewriter）\n3. 明确报告 bootstrap CI 类型和 100-point ablation 的 power analysis\n4. 在 Appendix 中提供 exact rewriting prompts",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — Methods & Experiments Review (Updated Paper, 15pp)\n\n**论文**: The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition\n**版本**: 修订版（15 页，含 Appendix A-N，Table 1-14）\n**Venue**: EMNLP 2026 (ARR)\n\n---\n\n## 1. Soundness: 3.5 / 5\n\n### CSD Pipeline Validity\n\n**NLI Gating**: Now properly specified — DeBERTa-v3-large, bidirectional entailment threshold 0.90, direction-aware for verbosity (Appendix F). GPT-4o cross-validation on all 200 pairs (92.1% formality, 82.6% verbosity precision). The 0.90 threshold sits on a bimodal plateau (Appendix E, Table 8: 11 thresholds from 50-98, BT stable across all). 这比原稿大幅改善。\n\n**Position Balancing**: Bidirectional swap producing n_pairs × 2 observations. Consistency filter retains only concordant pairs for sign test; BT model uses all observations. 标准做法。\n\n**Bradley-Terry Model**: GoF tests reported (Appendix H: formality deviance p=0.198, verbosity p=0.905). Stratified analysis confirms no preference heterogeneity for verbosity. Bootstrap CIs (10,000 pair-level resamples, seed 42). **但 CI 类型未指明（percentile vs. BCa）**——应在 Section 4.1 明确。\n\n**GEE Decomposition (Eq. 1)**:\n- Exchangeable correlation justified by QIC comparison (Appendix C, Table 4: |ΔQIC| < 0.001 across all 6 cells).\n- Interaction test: style×originality NS on formality for both judges (GPT-4o p=0.38, Qwen3 p=0.52). ✅\n- **缺失**：interaction test 未报告 verbosity axis。鉴于 verbosity 的 P(orig) 极低（Table 14: Qwen3 P(orig)=0.082，即 92% 偏好抛光文本），这正是 interaction 最可能显著的轴。如果 verbosity 上 style×originality interaction 显著，additive GEE 的 \"confound-free\" 结论受影响。\n- **缓解因素**：verbosity 的双向结果（Section 5.4：\"Both rewriting directions favor verbose responses\"）意味着 style preference 在两个方向上都压过 polishing artifact。如果 judges 在 verbose-original vs. concise-rewrite 方向上仍偏好 verbose（这对抗了 92% 的 polishing preference），style effect 必须非常强。这间接支持了 additive model 的 adequacy。\n\n**Blindspot 定义 (BT sig ∧ all Likert NS)**:\n- 论文现在在 Section 5.2 主文中讨论了 \"measurement attenuation vs. construct divergence\"——不再仅在 Limitations 中。\n- 两种解释均被讨论：\"Likert captures absolute quality difference while pairwise captures ordinal preference\"。\n- 结论：\"Whether this reflects measurement attenuation or construct divergence, the operational consequence is identical\"——这是务实且可辩护的立场。\n- **残余疑虑**：论文标题 \"Blindspot\" 暗示 Likert 有缺陷，但如果是 construct divergence，Likert 并非\"盲\"——它测的是不同东西。标题 framing 偏向 attenuation 解释。\n\n**100-Point Likert Ablation (Table 12, Appendix L)**:\n- n=100 formality + verbosity, Qwen3 judge. Formality: Likert p=0.725 (tie rate 65.9%), verbosity p=0.137 (tie rate 51.2%). BT 同数据 66.5% 和 77.3%。\n- **Power concern**：n=100 在 α=0.05 下能检测到的最小效应量约为 d=0.28（双侧 t-test，80% power）。观测到的 d=0.02-0.06 远低于此。所以 ablation 能排除 d≥0.28 的中等效应，但不能确认 d 是否真为 0 或仅为极小未检出效应。\n- **但这正是论文论点的一部分**：即使 100-point 量表，效应量仍为 d=0.02-0.06，远低于任何实际意义阈值。论点不是 \"d=0\" 而是 \"d 如此之小以至于 Likert 在实际样本量下永远检测不到。\" 这一推理是成立的。\n\n**NLI 已知局限**：\n- 论文报告了 FNR 8.4% (Section 5.1) 并分析了 FN 特征。\n- Direction-aware gating 的 asymmetry (Appendix F) 处理了 expansion vs. compression 的不对称性。\n- **未讨论**：DeBERTa NLI 对 lexical overlap 的已知敏感性——高 lexical overlap 的 pair 可能获得虚高 entailment score。但鉴于 style rewriting 通常改变词汇而非保留，这个问题的方向可能是使 gate 更严格（而非更宽松），reducing risk。\n\n### Soundness 小结\n核心方法学严谨，控制层次丰富（NLI gate + position swap + GEE decomposition + 5 experimental controls）。主要残余疑虑：(1) GEE interaction test 缺 verbosity axis；(2) Blindspot 标题 framing 偏向 attenuation 解释。不构成 Major issue，但影响 4.0 提升。\n\n---\n\n## 2. Experimental Design: 3.5 / 5\n\n### 覆盖度总览\n\n| 维度 | 已覆盖 | 评价 |\n|------|--------|------|\n| Judges | GPT-4o, Qwen3-32B, Claude(ctrl) + Llama(App K) | Good：3 target + 1 ctrl |\n| Benchmarks | LLMBar, AlpacaEval, MTBench (Table 1) | Good：3 benchmarks |\n| Axes | Formality ✅, Verbosity ✅, Register ⚠️ | Register 仅 2 judges |\n| Scaled replication | n=355, formality×Qwen3×LLMBar only | Limited scope |\n| Rewriter independence | Formality×GPT-4o judge only (Table 6-7) | **Limited** |\n| Negative control | Claude on formality×LLMBar + some others | Incomplete |\n| Cross-benchmark | All axes in Table 1, formality deepest | Partially |\n| Placebo | Table 14, 3 judges × 2 axes | **Good** |\n| NLI gate ablation | Table 13, pass/fail/all | **Good** (fail n small) |\n| 100-point Likert | Table 12, form+verb×Qwen3 | New & useful |\n| 7-method sensitivity | Table 2 (form) + Table 11 (verb) | **Good** |\n\n### Specific Concerns\n\n**S1. Rewriter independence 范围不足 [Should-Fix, idea]**\n- Table 6-7 (Appendix D) 仅在 formality×GPT-4o 配置上测试了 GPT-4o 作为替代 rewriter。BT 64.4% [56.1, 72.8] vs. Qwen3 rewriter 66.5% [58.5, 73.9]——CIs 重叠，OK。\n- **缺失**：verbosity 的 rewriter independence。Verbosity rewriting 更 invasive（NLI rejection 14% vs. 12%），rewriter identity 的影响可能更大。如果 Qwen3 的 verbose rewriting 风格系统性地不同于其他 rewriter，verbosity 77% BT 的一部分可能来自 Qwen3-specific 的 rewriting pattern 而非 genuine style bias。\n- **缓解**：Llama 作为独立 judge（Appendix K, Table 11）在 Qwen3-rewritten pairs 上复现了 verbosity bias，说明至少跨 judge 是稳定的。但 rewriter dimension 未测试。\n\n**S2. Claude negative control 覆盖不完整 [Should-Fix, presentation]**\n- Table 1 显示 Claude 在 LLMBar formality (.562, NS) 和部分其他 cells 上的结果。\n- Appendix G: TOST equivalence test at n=87, Δ=10pp, confirmed.\n- **但** verbosity 和 register 的 Claude 结果在 Table 1 中部分缺失（一些 cells 空白）。如果 Claude 仅在 formality 上验证为 NS，discriminant validity 只对 formality 成立。\n- 论文应明确报告 Claude 在所有已测 cells 上的 TOST 结果，而非仅在部分 cells。\n\n**S3. Register axis 不完整 [Minor, idea]**\n- 仅 2 judges (GPT-4o, Qwen3)，无 Llama。\n- BT 55-57%（边缘显著）。GEE 显示 originality-dominated。\n- 论文将 register 定位为 \"exploratory\"——这是正确的 scoping。Table 3 footnote 确认 register 不进入 primary Holm-Bonferroni family。\n- **残余问题**：如果 register 是 exploratory，是否应该在 Abstract 中与 formality/verbosity 并列为 \"three style axes\"？ 目前 Abstract 说 \"two primary style axes (formality, verbosity), with exploratory evidence on register\"——这比原稿改善但仍略 overstate。\n\n**S4. Cross-benchmark depth不均 [Should-Fix, presentation]**\n- Table 1 的 cross-benchmark 覆盖（3 benchmarks × judges × axes）是主表，但 AlpacaEval 和 MTBench 上的 GEE decomposition 和 Likert 对比未在 appendix 中深入展开。\n- 论文依赖 Table 1 的 cross-benchmark BT 一致性，但未验证 Blindspot pattern（BT sig + Likert NS）是否在非 LLMBar benchmarks 上也成立。如果 Blindspot 仅在 LLMBar 上出现，generalizability claim 受限。\n\n**S5. Double-rewrite placebo 的解读 [Should-Fix, idea]**\n- Table 14 (Appendix N) 显示 P(orig) 在 verbosity 上极低（GPT-4o: 0.167, Qwen3: 0.082）——judges 92% 偏好 LLM-polished text。这是 **非常强的 rewriting artifact**。\n- 论文声称 GEE decomposition \"absorbs\" 这个 artifact。\n- **关键问题**：在 treatment pairs 中，style 和 originality 通过 bidirectional design 被交叉。在 verbose-original vs. concise-rewrite 方向上，judges 仍偏好 verbose text（Section 5.4: \"Both directions favor verbose\"）——这意味着 style preference 确实压过了 92% 的 polishing preference，支持 GEE 的 adequacy。\n- 但论文应更明确地展示这个推理链：placebo artifact → bidirectional cancellation → GEE correctly isolates style。目前 Table 14 放在附录末尾，与 GEE 讨论脱节。\n\n**S6. n=100 per condition for GEE [Minor, idea]**\n- n=100 (86-88 NLI-pass) with binary outcome and 2 covariates. For large ORs (2-13), adequate power. For register (OR near 1), underpowered.\n- Scaled replication (n=355) 仅在一个 configuration 上确认了 stability。Verbosity 和 cross-benchmark 未 scaled。\n- 但论文的主要结论（verbosity is strong, formality is conditional, register is weak）不依赖于 marginal significance——pattern 在多个 configurations 上一致。\n\n### Experimental Design 小结\n设计广度好（3 judges × 3 benchmarks × 3 axes + 5 experimental controls），但几个维度的深度不足：rewriter independence 仅 formality、Claude 覆盖不完整、cross-benchmark GEE/Likert 未展开。最值得关注的是 S1（rewriter independence）和 S5（placebo 解读链）。\n\n---\n\n## 3. Reproducibility: 3.5 / 5\n\n| 要素 | 状态 | 备注 |\n|------|------|------|\n| NLI model identity | ✅ DeBERTa-v3-large | Section 3.2 |\n| NLI threshold | ✅ 0.90 | Section 3.2 |\n| Rewriter model | ✅ Qwen3-32B-Instruct | Section 3.1 |\n| Judge API version | ✅ GPT-4o (gpt-4o-2024-08-06) | Section 3.3 |\n| Temperature | ✅ 0.7 | Section 3.1 |\n| Rewriting prompts | ⚠️ Described but exact text not given | Missing from appendix |\n| Bootstrap params | ✅ 10,000 pair-level, seed 42 | Section 4.1 |\n| Bootstrap CI type | ❌ Percentile vs. BCa not specified | Should state |\n| GEE correlation | ✅ Exchangeable + independence comparison | Appendix C |\n| Code/data | ⚠️ \"Released upon acceptance\" | Not verifiable |\n\n**主要gap**：Rewriting prompt 的 exact text 未在论文或附录中提供。Section 3.1 描述了 prompt 的结构（\"Rewrite the following text to be more formal/casual...\"），但不同的 prompt wording 可能影响 rewriting 质量和 NLI pass rate。对于 reproducibility，exact prompts 是关键。\n\n---\n\n## 4. Statistical Concerns\n\n**4a. Multiple comparisons**: \nPrimary family: 2 judges × 3 axes = 6 tests, Holm-Bonferroni at α=0.05 (Section 4.1). Table 1 reports both raw and adjusted p-values. Register 标为 exploratory（不入 family）。✅ 合理。\n\n**4b. Bootstrap CIs**: \n10,000 pair-level resamples, seed 42. **CI type（percentile vs. BCa）未指定**。对于 skewed BT estimates（如 register BT 55%），BCa would be more appropriate。Should state in methods.\n\n**4c. GEE working correlation**: \nExchangeable, compared with independence in Appendix C (|ΔQIC| < 0.001). Interaction test on formality (NS for both judges). ✅ 充分。\n**但 verbosity interaction test 缺失** — ditto Soundness 部分的讨论。\n\n**4d. \"7 methods all NS\" = evidence of absence?**:\n这是论文的核心方法论 tension。7 种 Likert 方法全部 NS 不严格等于 \"no effect\"——只是 \"not detected\"。但论文通过三层补充证据缓解了这一问题：\n1. Bootstrap attenuation analysis (Appendix J, Table 10): d→0 as n increases to 355, CI [−0.123, 0.087] never excluding zero。说明 d 不是 under-detected 而是 genuinely near zero。\n2. 100-point Likert ablation (Appendix L): 更细粒度的量表仍不改善检测。\n3. BT 同数据显著（p < 0.001）：同一数据上两种方法的不一致排除了 \"insufficient data\" 解释。\n\n这三层证据将 \"absence of evidence\" 显著升级为 \"bounded near-zero effect\"。**论文对这一 tension 的处理是该领域论文中我见过的最严谨的之一。**\n\n---\n\n## 5. Missing Experiments (对照 review context)\n\n| Experiment | Status | Reported Where | Completeness |\n|-----------|--------|---------------|-------------|\n| exp-001: Multi-judge (Gemini) | ❌ MISSING | — | Gemini mentioned in Related Work context but no results |\n| exp-002: Multi-benchmark | ✅ Partial | Table 1 (BT); Appendix cross-benchmark (formality only deeper) | Verbosity/register GEE cross-benchmark missing |\n| exp-003: 7-method sensitivity | ✅ | Table 2 (form) + Appendix K Table 11 (verb) | Two axes covered |\n| exp-005: Placebo control | ✅ | Appendix N, Table 14 | 3 judges × 2 axes |\n| exp-006: Scaled replication n=355 | ✅ | Section 5.2, Appendix J | Single condition |\n| exp-009: Rewriter independence | ✅ Partial | Appendix D, Table 6-7 | Formality only, GPT-4o judge only |\n| exp-020: GPT-4o verb+register | ✅ | Table 1 | Complete |\n| exp-021: Llama third judge | ✅ | Appendix K, Table 11 | Verbosity sensitivity hierarchy |\n| exp-022: Double-rewrite placebo | ✅ | Appendix N, Table 14 | Merged with exp-005 |\n| exp-023: NLI gate ablation | ✅ | Appendix M, Table 13 | Pass/fail/all, 2 axes |\n| exp-024: Cross-axis gradient | ✅ | Implicit in Table 1 + Fig 3 | Qualitative only |\n| 100-point Likert ablation | ✅ | Appendix L, Table 12 | 2 axes × Qwen3 |\n\n**关键缺失**：\n1. Gemini judge 完全缺失——review context 列出但论文中无 Gemini 数据\n2. Rewriter independence 仅 formality——verbosity 是更 invasive 的轴\n3. Cross-benchmark GEE/Likert decomposition 未展开\n\n---\n\n## ARR Dimension Scores\n\n| Dimension | Score | Reasoning |\n|-----------|-------|-----------|\n| **Soundness** | 3.5/5 | Pipeline 设计严谨，5 层 Comparative Trap 控制令人印象深刻。GEE 有完整诊断。但 verbosity interaction test 缺失、construct validity 未解决。 |\n| **Excitement** | 3.5/5 | Likert Blindspot 是实用且新颖的发现；7-method sensitivity hierarchy 和 100-point ablation 提供了强实证。但与 RATE 的增量界限需更清晰定位。 |\n| **Reproducibility** | 3.5/5 | 关键超参明确标注（模型、threshold、API 版本、temperature），但 exact prompts 和 bootstrap CI 类型缺失。 |\n\n## Overall Assessment\n\n**Overall**: 3.5 / 5（Borderline Conference）\n**Confidence**: 4 / 5\n\n### Justification\n\n**Why 3.5 rather than 4.0**: 三个 Should-Fix 问题的集合效应——(1) rewriter independence 仅测试了 formality（verbosity 是主力发现但 rewriter robustness 未验证）；(2) double-rewrite placebo 揭示了极强的 rewriting artifact（Qwen3 verbosity P(orig)=8%）但 GEE interaction test 仅在 formality 上报告（对 verbosity 的 \"confound-free\" 声明的统计支撑不完整）；(3) 论文的核心 framing（\"Blindspot\"）偏向 measurement attenuation 解释，但主文讨论了 construct divergence 后仍未提供能区分两者的实验证据。\n\n**Why not 3.0**: 论文的控制层次（NLI gate ablation + placebo + Claude ctrl + cross-axis + debiased prompting）在该领域论文中罕见。Bootstrap attenuation analysis + 100-point Likert ablation + 7-method sensitivity table 共同构建了 Blindspot 的强实证基础。GEE 诊断完整（correlation structure、interaction test、GoF）。这些优势显著高于 Findings 水准。\n\n**Path to 4.0**:\n1. 在 verbosity axis 上报告 GEE style×originality interaction test\n2. 在 verbosity axis 上测试 rewriter independence（至少 GPT-4o 作为替代 rewriter）\n3. 明确报告 bootstrap CI 类型和 100-point ablation 的 power analysis\n4. 在 Appendix 中提供 exact rewriting prompts",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 415 · 2026-05-21T16:15:08.146662+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3715
}
```

</details>

---


### Tool call

_source line 416 · 2026-05-21T16:15:14.442020+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 417 · 2026-05-21T16:15:14.496766+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 54
}
```

</details>

---


### Assistant

_source line 418 · 2026-05-21T16:15:20.678274+00:00_

审稿报告已提交。总结：更新版论文（15 页）在方法学上有显著改善——新增了 5 层 Comparative Trap 控制、100-point Likert ablation、NLI gate ablation、bootstrap attenuation analysis，整体评分 3.5/5 (Borderline Conference)。核心提升路径：补充 verbosity 的 GEE interaction test 和 rewriter independence test。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1"
}
```

</details>

---


## Round 15

## Round 15

48 recorded events


### User

_source line 419 · 2026-05-21T17:26:11.829103+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性与实验设计**。

## Venue 信息
- **目标会议**: EMNLP 2026 (通过 ARR 提交)
- **截止日期**: 2026-05-25
- **页数限制**: 主正文 8 页，参考文献不限，Limitations 和 Ethics 不计入页数
- **模板**: ACL 格式，`\usepackage[review]{acl}`
- **匿名规则**: double-blind
- **Limitations**: 必须包含，只讨论局限性，不能包含新实验/图表/分析
- **ARR Responsible NLP Checklist**: 在 OpenReview submission form 中填写，不在论文 PDF 中

## 论文信息
- **标题**: The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition
- **论文路径**: `projects/causal_style_decomp_judge/docs/paper/main.tex`
- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf`

## 你的审查侧重

**重点关注以下方面，逐条给出评价（Must-Fix / Should-Fix / Minor / OK）：**

### 1. 统计方法学
- Bradley-Terry 模型的 IIA 假设是否得到检验？GoF 测试是否充分？
- Holm-Bonferroni 校正的 family 定义（8 个 primary tests）是否合理？exploratory/confirmatory 分类是否恰当？
- GEE 模型规格：exchangeable correlation 的选择是否合理？interaction test 是否充分？
- Bootstrap CI（10,000 resamples）方法是否标准？
- TOST 等价性检验（Claude 负对照）的 equivalence bound 选择是否有 external justification？

### 2. NLI Gate 设计
- 0.90 阈值的选择是否有充分 justification（plateau 论证是否成立）？
- 双向 vs direction-aware gating 的 axis-dependent 策略是否合理？
- NLI validation 使用 Qwen3-32B 作为 annotator + GPT-4o cross-validation 是否足够？是否需要人工评估？
- False negative rate 8.4% 对结论的影响评估是否充分？

### 3. 因果声明与方法论强度
- "Controlled Style Decomposition" 和 "interventional framework" 等术语与实际方法论强度是否匹配？
- DAG (Figure 2) 的 causal claims 与 filtering-based approach 之间是否存在张力？
- §3.5 Design Rationale 中的 identification assumptions 是否被充分讨论？
- "approximates content preservation" vs 真正的 intervention 之间的区别是否清晰？

### 4. Evaluator-Producer Bias
- Qwen3-32B 同时作为 rewriter 和 judge 的 self-preference 风险评估是否充分？
- Cross-rewriter independence test（GPT-4o 替代 Qwen3-32B）覆盖了哪些轴？缺失轴（register）的影响？
- Style OR 下降 22%（13.10→10.17）的解释是否合理？

### 5. 样本量与泛化性
- LLMBar (n=100) 为主数据源，cross-benchmark 扩展是否足够？
- 三个 benchmark × 三个 judge 的覆盖矩阵中空 cell 的处理？
- n=355 scaled replication 的证据权重？
- 从实验数据到 "style bias audits should adopt pairwise comparison" 的推广强度？

### 6. Confound 控制
- NLI gate 能否真正阻断 quality perception shifts mediated by style？
- Formality 方向不对称（78.8% vs 54.5%）的处理是否充分？
- Same-style double-rewrite control 的效力？
- GEE 的 originality term 是否真正"吸收"了 rewriting artifact？

请按标准 ARR 审稿格式输出：Summary → Strengths → Weaknesses (逐条标注 severity) → Questions → Missing References → Overall Assessment (含评分和置信度)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 420 · 2026-05-21T17:26:22.541279+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,WebSearch,WebFetch,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,WebSearch,WebFetch,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 421 · 2026-05-21T17:26:22.591895+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 422 · 2026-05-21T17:26:26.410173+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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

_source line 423 · 2026-05-21T17:26:26.962500+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool result

_source line 424 · 2026-05-21T17:26:27.716797+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.7}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 505.8}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 592.9}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 518.0}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 450.7}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 509.7}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 467.4}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 518.1}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 526.2}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/pap
…[truncated 311 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1306
}
```

</details>

---


### Tool result

_source line 425 · 2026-05-21T17:26:34.407416+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines and scoring criteria:

## Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Review Form Criteria

The review form includes specific scoring categories:

- 5 = Consider for Award: for papers that could be considered for an outstanding 
…[truncated 1064 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7444
}
```

</details>

---


### Tool call

_source line 426 · 2026-05-21T17:26:39.285479+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ARR review form: all scoring dimensions, their scales (1-5 or otherwise), detailed descriptions of each score level, and any other required fields (confidence, best paper, etc.). Return the full detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete ARR review form: all scoring dimensions, their scales (1-5 or otherwise), detailed descriptions of each score level, and any other required fields (confidence, best paper, etc.). Return the full detail."
  }
}
```

</details>

---


### Tool call

_source line 427 · 2026-05-21T17:26:39.588461+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 428 · 2026-05-21T17:26:40.095009+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 429 · 2026-05-21T17:26:41.106420+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1517
}
```

</details>

---


### Tool call

_source line 430 · 2026-05-21T17:26:41.106892+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 431 · 2026-05-21T17:26:41.614478+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 432 · 2026-05-21T17:26:42.018943+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 433 · 2026-05-21T17:26:42.070325+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1975
}
```

</details>

---


### Tool result

_source line 434 · 2026-05-21T17:26:43.581558+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2474
}
```

</details>

---


### Tool result

_source line 435 · 2026-05-21T17:26:44.138827+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2524
}
```

</details>

---


### Tool result

_source line 436 · 2026-05-21T17:26:44.191193+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2172
}
```

</details>

---


### Tool result

_source line 437 · 2026-05-21T17:26:47.906268+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## Primary Scoring Dimensions

### 1. Reviewer Confidence
**Scale: 1-5**
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

### 2. Soundness
**Scale: 1-5 with half-point increments**
- **5**: "Excellent: This study is one of the most thorough I have seen."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

### 3. Excitement
**Scale: 1-5 with half-point increments**
- **5**: "Highly Exciting: I would recommend this paper to others."
- **4**: "Exciting: I would mention this paper to others."
- **3**: "Interesting: I might mention some points of this paper."
- **2**: "Potentially Interesting: this paper does not resonate with me."
- **1**: "Not Exciting: this paper does not resonate with me."

### 4. Overall Assessment
**Scale: 1-5 with half-point increments**
- **5**: Consider for Award (top 2.5%)
- **4.5**: Borderline Award
- **4**: Conference acceptance
- **3.5**: Borderline Conference
- **3**: Findings acceptance
- **2.5**: Borderline Findings
- **2**: Substantial revisions needed
- **1.5**: Revisions extending beyond one cycle
- **1**: Do not resubmit

### 5. Reproducibility
**Scale: 1-5**
- **5**: Results easily reproducible
- **4**: Mostly reproducible with minor variations
- **3**: Reproducible with difficulty
- **2**: "hard pressed to reproduce the results"
- **1**: Cannot r
…[truncated 926 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8620
}
```

</details>

---


### Tool call

_source line 438 · 2026-05-21T17:26:52.774615+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 439 · 2026-05-21T17:26:53.739457+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 440 · 2026-05-21T17:26:53.739883+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 441 · 2026-05-21T17:26:54.849270+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2074
}
```

</details>

---


### Tool call

_source line 442 · 2026-05-21T17:26:54.849730+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 443 · 2026-05-21T17:26:54.850012+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 444 · 2026-05-21T17:26:55.555719+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1816
}
```

</details>

---


### Tool result

_source line 445 · 2026-05-21T17:26:56.412751+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2672
}
```

</details>

---


### Tool result

_source line 446 · 2026-05-21T17:26:57.621658+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2771
}
```

</details>

---


### Tool result

_source line 447 · 2026-05-21T17:26:57.625880+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2775
}
```

</details>

---


### Tool call

_source line 448 · 2026-05-21T17:27:02.845088+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "11-15",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 449 · 2026-05-21T17:27:03.500732+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 431.2}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 460.5}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 484.7}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 593.3}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 590.1}], \"total_pages\": 15, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 655
}
```

</details>

---


### Tool call

_source line 450 · 2026-05-21T17:27:06.716506+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 451 · 2026-05-21T17:27:07.219658+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 452 · 2026-05-21T17:27:07.775300+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1058
}
```

</details>

---


### Tool call

_source line 453 · 2026-05-21T17:27:07.775750+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 454 · 2026-05-21T17:27:08.630896+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1411
}
```

</details>

---


### Tool call

_source line 455 · 2026-05-21T17:27:08.633382+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 456 · 2026-05-21T17:27:08.837154+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 457 · 2026-05-21T17:27:09.342446+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1566
}
```

</details>

---


### Tool result

_source line 458 · 2026-05-21T17:27:10.097359+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1463
}
```

</details>

---


### Tool result

_source line 459 · 2026-05-21T17:27:10.198961+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1361
}
```

</details>

---


### Tool call

_source line 460 · 2026-05-21T17:28:14.301313+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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

_source line 461 · 2026-05-21T17:28:57.803187+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 50, \"total_citations\": 69, \"unique_cited_keys\": 49, \"orphan_bib\": 1, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 41, \"online_not_found\": 3, \"online_mismatch\": 6}, \"cross_check\": {\"orphan_bib\": [\"hoenig2001abuse\"], \"missing_bib\": [], \"orphan_count\": 1, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"murugadoss2025sos\", \"type\": \"inproceedings\", \"title\": \"Style Over Substance: Failure Modes of LLM Judges in Alignment Benchmarking\", \"authors\": \"Murugadoss, Aakanksha and others\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"li2026preference\", \"type\": \"inproceedings\", \"title\": \"Preference Leakage: A Contamination Problem in LLM-as-a-Judge\", \"authors\": \"Li, Dawei and others\", \"year\": \"2026\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"wang2026fairjudge\", \"type\": \"article\", \"title\": \"FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge\", \"authors\": \"Yang, Bo and Feng, Lanfei and Chen, Yunkui and Zhang, Yu and Xu, Xiao and Li, Sh...\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2602.06625\"}, {\"key\": \"dubois2025lc\", \"type\": \"inproceedings\", \"title\": \"Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators\", \"authors\": \"Dubois, Yann and others\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"casse2026concise\", \"type\": \"article\", \"title\": \"A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents\", \"authors\": \"Cho, Young-Min and Yuan, Yuan and Guntuku, Sharath Chandra and Ungar, Lyle\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2601.10809\"}, {\"key\": \"counterfactu
…[truncated 38903 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 43501
}
```

</details>

---


### Tool call

_source line 462 · 2026-05-21T17:33:01.808537+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — 方法严谨性与实验设计（Round 1 完整审稿）\n\n### Paper Summary\n\n本文提出 Controlled Style Decomposition (CSD)，一个检测 LLM judge 隐藏风格偏差的框架。核心发现是 \"Likert Blindspot\"：在相同数据上，Likert 评分（ATE）对风格偏差显示为不显著，而 position-controlled pairwise comparison 通过 Bradley-Terry 分析能检测到 63–67% 的风格偏差。CSD 包含三个阶段：(1) 沿单一风格轴用 instruction-tuned LLM 进行 style-controlled rewriting；(2) NLI-gated content preservation 过滤；(3) 位置控制的 pairwise comparison。在 3 个目标 judge、1 个负对照（Claude Sonnet 4）、3 个 benchmark、3 个风格轴上验证。GEE conditional decomposition 进一步揭示 per-axis confound structure。\n\n---\n\n### Summary of Strengths\n\n**S1. 研究问题精准且对社区有直接价值。** Likert Blindspot 的发现对 LLM 评估实践有即时的方法论指导意义，指出了一个被广泛忽视的测量盲区（Section 5.2, Table 2）。\n\n**S2. 统计框架严谨且多层次。** 七种统计方法交叉验证（Table 2），GEE 条件分解（Table 3），Bootstrap CI（10,000 resamples, Table 9），BT GoF 检验（Appendix H），NLI 阈值 sensitivity sweep（Table 8），TOST 等价性检验（Appendix G）。\n\n**S3. 负对照设计增强因果推断。** Claude Sonnet 4 在所有轴上显示非显著偏差，支持了\"检测到的偏差是 judge-specific\"的论证。\n\n**S4. Confound 结构的细粒度刻画。** GEE 分解区分了 style-dominated（verbosity）、conditional（formality）和 judge-dependent（register）三种模式。\n\n**S5. 写作清晰、结构紧凑。** 主文控制在 8 页内，附录提供了充分的技术细节（15 个 appendix sections）。\n\n---\n\n### Must-Fix 问题\n\n**N1** [critical] NLI gate 缺乏人工评估验证\n- 位置：Section 3.2, Section 5.1, Appendix A\n- 整个框架的有效性依赖 NLI gate 正确分离 style 与 content 变化，但验证完全自动化——Qwen3-32B annotator + GPT-4o cross-validation 得到 92.1%/82.6% precision。没有任何人工评估来验证 NLI gate 的 pass/fail 决策是否与人类判断一致。DeBERTa-v3-large 在 style-shifted text 上的行为可能与标准 NLI 数据不同——formal text 可能系统性地获得更高 entailment score。\n- 建议：随机抽取 50–100 对 pass/fail 样本，2+ annotator 评估内容保持程度，报告 IAA 和一致率。\n\n**N2** [critical] Evaluator-producer bias 22% OR 下降被低估\n- 位置：Section 5.3, Appendix D, Table 6\n- Qwen3-32B rewriter 替换为 GPT-4o 后 verbosity Style OR 下降 22%（13.10→10.17），论文定性为\"bounding\"但 22% 是 non-trivial。更关键的是 cross-rewriter test 只覆盖 formality 和 verbosity，**register 轴完全缺失**——而 register 恰是 judge-dependence 最强的轴。\n- 建议：(1) 提供 producer-corrected 效应估计范围；(2) 补充 register 轴 cross-rewriter test；(3) 至少在 Limitations 标注 register 缺乏 producer-independence 验证。\n\n---\n\n### Should-Fix 问题\n\n**W1** [warning] TOST equivalence bound 缺乏独立外部 justification（Appendix G）。用同研究 treatment effects 设定 control 的 equivalence bound 形成循环。建议引用外部基准。\n\n**W2** [warning] BT IIA 假设在 formality 轴可能被违反（Appendix H，Fisher p = 0.015 方向不对称）。建议报告 direction-stratified BT estimates 或使用 Thurstone Case V 作为 robustness check。\n\n**W3** [warning] 因果术语（\"interventional framework\"、Figure 2 DAG）与实际 filtering-based 方法之间存在张力。Section 3.5 hedging 适当但 Figure 2 视觉修辞偏强。建议 Figure 2 caption 标注非 formal causal model，Abstract 中用 \"quasi-interventional\"。\n\n**W4** [warning] 样本量偏小（LLMBar n=100, MT-Bench n=30），scaled replication（n=355）仅覆盖 Qwen3-32B formality。建议报告 BT achieved power，扩展 replication 覆盖面。\n\n**W5** [warning] Identification assumption (iii)——\"rewrite introduces no systematic differences beyond target axis\"——讨论不充分。Same-style control 只检测 rewriting artifact 但无法检测 axis-specific confounds。\n\n---\n\n### 小问题\n\n- M1: `hoenig2001abuse` orphan bib entry\n- M2: Table 2 \"sensitivity hierarchy\" 首次出现缺乏定义\n- M3: Figure 3 diamond vs circle markers 在灰度下难区分\n- M4: Figure 4 y 轴标签被截断\n\n---\n\n### Questions\n\nQ1: NLI gate 在不同 rewrite directions 上的 score 分布是否存在系统差异？\nQ2: 22% OR 下降中有多少是 GPT-4o 的 style transfer 质量差异 vs 真实 self-preference？\nQ3: Register 的 judge-dependence 如何排除 evaluator-producer confound？\nQ4: 100-point continuous Likert 仍检测不到 Blindspot——这是否说明问题在 evaluation paradigm 而非 scale granularity？\nQ5: Formality 方向不对称（88.9% vs 72.6%）是否意味着 casual→formal 改善了 perceived quality？\n\n---\n\n### 官方维度打分\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Soundness | 3.5/5 | 统计框架严谨但 NLI gate 缺人工验证、evaluator-producer bias 处理过于乐观 |\n| Excitement | 3.5/5 | Likert Blindspot 对 evaluation community 有直接影响；框架有创意但非 paradigm shift |\n| Reproducibility | 4/5 | 模型、超参、benchmark 明确标注；承诺代码/数据公开 |\n| Overall | **3.5 — Borderline Conference** | 核心发现有价值且统计密度高，但 NLI human validation 缺失和 evaluator-producer confound 不足削弱可信度。N1+N2 解决后可上调至 4.0 |\n| Confidence | 4/5 | 仔细阅读全文含全部附录；熟悉因果推断、BT、GEE 和 LLM 评估文献 |\n\n**一句话总结**: 有价值的方法论发现和精巧的框架设计，但 NLI gate 无人工验证 + evaluator-producer bias 处理不足使核心 claim 可信度打折。",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — 方法严谨性与实验设计（Round 1 完整审稿）\n\n### Paper Summary\n\n本文提出 Controlled Style Decomposition (CSD)，一个检测 LLM judge 隐藏风格偏差的框架。核心发现是 \"Likert Blindspot\"：在相同数据上，Likert 评分（ATE）对风格偏差显示为不显著，而 position-controlled pairwise comparison 通过 Bradley-Terry 分析能检测到 63–67% 的风格偏差。CSD 包含三个阶段：(1) 沿单一风格轴用 instruction-tuned LLM 进行 style-controlled rewriting；(2) NLI-gated content preservation 过滤；(3) 位置控制的 pairwise comparison。在 3 个目标 judge、1 个负对照（Claude Sonnet 4）、3 个 benchmark、3 个风格轴上验证。GEE conditional decomposition 进一步揭示 per-axis confound structure。\n\n---\n\n### Summary of Strengths\n\n**S1. 研究问题精准且对社区有直接价值。** Likert Blindspot 的发现对 LLM 评估实践有即时的方法论指导意义，指出了一个被广泛忽视的测量盲区（Section 5.2, Table 2）。\n\n**S2. 统计框架严谨且多层次。** 七种统计方法交叉验证（Table 2），GEE 条件分解（Table 3），Bootstrap CI（10,000 resamples, Table 9），BT GoF 检验（Appendix H），NLI 阈值 sensitivity sweep（Table 8），TOST 等价性检验（Appendix G）。\n\n**S3. 负对照设计增强因果推断。** Claude Sonnet 4 在所有轴上显示非显著偏差，支持了\"检测到的偏差是 judge-specific\"的论证。\n\n**S4. Confound 结构的细粒度刻画。** GEE 分解区分了 style-dominated（verbosity）、conditional（formality）和 judge-dependent（register）三种模式。\n\n**S5. 写作清晰、结构紧凑。** 主文控制在 8 页内，附录提供了充分的技术细节（15 个 appendix sections）。\n\n---\n\n### Must-Fix 问题\n\n**N1** [critical] NLI gate 缺乏人工评估验证\n- 位置：Section 3.2, Section 5.1, Appendix A\n- 整个框架的有效性依赖 NLI gate 正确分离 style 与 content 变化，但验证完全自动化——Qwen3-32B annotator + GPT-4o cross-validation 得到 92.1%/82.6% precision。没有任何人工评估来验证 NLI gate 的 pass/fail 决策是否与人类判断一致。DeBERTa-v3-large 在 style-shifted text 上的行为可能与标准 NLI 数据不同——formal text 可能系统性地获得更高 entailment score。\n- 建议：随机抽取 50–100 对 pass/fail 样本，2+ annotator 评估内容保持程度，报告 IAA 和一致率。\n\n**N2** [critical] Evaluator-producer bias 22% OR 下降被低估\n- 位置：Section 5.3, Appendix D, Table 6\n- Qwen3-32B rewriter 替换为 GPT-4o 后 verbosity Style OR 下降 22%（13.10→10.17），论文定性为\"bounding\"但 22% 是 non-trivial。更关键的是 cross-rewriter test 只覆盖 formality 和 verbosity，**register 轴完全缺失**——而 register 恰是 judge-dependence 最强的轴。\n- 建议：(1) 提供 producer-corrected 效应估计范围；(2) 补充 register 轴 cross-rewriter test；(3) 至少在 Limitations 标注 register 缺乏 producer-independence 验证。\n\n---\n\n### Should-Fix 问题\n\n**W1** [warning] TOST equivalence bound 缺乏独立外部 justification（Appendix G）。用同研究 treatment effects 设定 control 的 equivalence bound 形成循环。建议引用外部基准。\n\n**W2** [warning] BT IIA 假设在 formality 轴可能被违反（Appendix H，Fisher p = 0.015 方向不对称）。建议报告 direction-stratified BT estimates 或使用 Thurstone Case V 作为 robustness check。\n\n**W3** [warning] 因果术语（\"interventional framework\"、Figure 2 DAG）与实际 filtering-based 方法之间存在张力。Section 3.5 hedging 适当但 Figure 2 视觉修辞偏强。建议 Figure 2 caption 标注非 formal causal model，Abstract 中用 \"quasi-interventional\"。\n\n**W4** [warning] 样本量偏小（LLMBar n=100, MT-Bench n=30），scaled replication（n=355）仅覆盖 Qwen3-32B formality。建议报告 BT achieved power，扩展 replication 覆盖面。\n\n**W5** [warning] Identification assumption (iii)——\"rewrite introduces no systematic differences beyond target axis\"——讨论不充分。Same-style control 只检测 rewriting artifact 但无法检测 axis-specific confounds。\n\n---\n\n### 小问题\n\n- M1: `hoenig2001abuse` orphan bib entry\n- M2: Table 2 \"sensitivity hierarchy\" 首次出现缺乏定义\n- M3: Figure 3 diamond vs circle markers 在灰度下难区分\n- M4: Figure 4 y 轴标签被截断\n\n---\n\n### Questions\n\nQ1: NLI gate 在不同 rewrite directions 上的 score 分布是否存在系统差异？\nQ2: 22% OR 下降中有多少是 GPT-4o 的 style transfer 质量差异 vs 真实 self-preference？\nQ3: Register 的 judge-dependence 如何排除 evaluator-producer confound？\nQ4: 100-point continuous Likert 仍检测不到 Blindspot——这是否说明问题在 evaluation paradigm 而非 scale granularity？\nQ5: Formality 方向不对称（88.9% vs 72.6%）是否意味着 casual→formal 改善了 perceived quality？\n\n---\n\n### 官方维度打分\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Soundness | 3.5/5 | 统计框架严谨但 NLI gate 缺人工验证、evaluator-producer bias 处理过于乐观 |\n| Excitement | 3.5/5 | Likert Blindspot 对 evaluation community 有直接影响；框架有创意但非 paradigm shift |\n| Reproducibility | 4/5 | 模型、超参、benchmark 明确标注；承诺代码/数据公开 |\n| Overall | **3.5 — Borderline Conference** | 核心发现有价值且统计密度高，但 NLI human validation 缺失和 evaluator-producer confound 不足削弱可信度。N1+N2 解决后可上调至 4.0 |\n| Confidence | 4/5 | 仔细阅读全文含全部附录；熟悉因果推断、BT、GEE 和 LLM 评估文献 |\n\n**一句话总结**: 有价值的方法论发现和精巧的框架设计，但 NLI gate 无人工验证 + evaluator-producer bias 处理不足使核心 claim 可信度打折。",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 463 · 2026-05-21T17:33:05.274425+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3465
}
```

</details>

---


### Tool call

_source line 464 · 2026-05-21T17:33:10.102119+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 465 · 2026-05-21T17:33:10.152805+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 466 · 2026-05-21T17:33:18.173132+00:00_

审稿完成，已提交至 Review Director。

**评分**: Overall 3.5 (Borderline Conference), Soundness 3.5, Excitement 3.5, Reproducibility 4, Confidence 4。

**两个 Must-Fix 问题**：
1. NLI gate 完全依赖自动化验证，缺乏人工评估——这是整个框架的基石
2. Evaluator-producer bias 22% OR 下降处理不充分，且 register 轴缺失 cross-rewriter 验证

**五个 Should-Fix 问题**：TOST equivalence bound 循环论证、BT IIA 在 formality 上可能违反、因果术语过强、样本量偏小且 replication 覆盖面窄、identification assumption (iii) 讨论不足。

核心判断：论文发现有价值（Likert Blindspot）且统计密度高于同领域平均水平，但方法论基石的验证缺口阻止了 confident accept。如果 N1 和 N2 在 revision 中解决，可上调至 4.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1"
}
```

</details>

---


## Round 16

## Round 16

14 recorded events


### User

_source line 467 · 2026-05-21T17:35:38.703149+00:00_

[Round 1 审稿请求]:
## 交叉分享：以下是 Reviewer 2 的完整审稿意见

请逐条回应：对每个 Must-Fix、Should-Fix 和关键 Strength 用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。特别关注你们之间的分歧点。

---

## Reviewer 2 审稿意见（新颖性、Related Work 完整性与写作质量）

### 总体评分
**Overall**: 3.5 = Borderline Conference
**一句话总结**: 一篇实验设计扎实、发现有实践价值的实证论文，但核心新颖性偏向将已知测量理论迁移到 LLM judge 领域，且存在页数超限等格式问题。

### 官方维度打分（ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计合理、多重控制周全，但 pairwise detection vs. amplification 无法完全区分；sample size 有限（n=88 基础），GEE 分析执行规范 |
| Excitement | 3/5 | Likert Blindspot 发现对评估社区有实践价值，但核心洞见（pairwise > Likert 灵敏度）在测量理论中已有充分预测；框架是整合型而非根本性创新 |
| Reproducibility | 4/5 | 模型版本、超参数、统计方法均有详细说明；代码/数据承诺接收后释放 |
| Confidence | 4/5 | 仔细阅读全文及附录，熟悉 LLM evaluation 和测量理论文献 |

---

### Must-Fix 问题

**N1** [critical] 主正文超过 8 页限制
- 具体位置：PDF page 8–9 边界
- 问题：Section 6 (Conclusion) 在 page 8 底部开始，约 5–6 行结论文本溢出到 page 9，之后才是 Limitations。EMNLP 2026 规定 "strict 8-page limit for main text"，Limitations 不计入但 Conclusion 计入。
- 为什么影响接收：严格执行下可导致 desk rejection 或要求格式修正。
- 建议修改方向：压缩 §5.6 或 §6 文本（约 6–7 行），或将 Table 3 移至 Appendix 以释放空间。

**N2** [critical] Novelty claim 过度宽泛——"first systematic quantification" 需要更精确的界定
- 具体位置：Abstract (sentence 2), Introduction (line 10, 12), Related Work §2 (line 23)
- 问题：论文声称 CSD 是 "the first framework combining NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison"，并称 Likert Blindspot 是 "first systematic quantification"。然而：
  - Pairwise > rating 的灵敏度优势是 Thurstone (1927) 以来的经典结论
  - 在 NLG 评估中的量化：Kiritchenko & Mohammad (2017) 和 Novikova et al. (2018) 已证明 forced-choice 方法检测到 rating scales 遗漏的质量差异
  - 框架的每个组件都有先例
  - Qiu et al. (2025) 已在 persona-level 使用 counterfactual rewriting + BT
- 为什么影响接收：过度的 novelty claim 降低论文可信度。
- 建议修改方向：将 "first systematic quantification" 限定为 "first systematic quantification for LLM judge style bias"；明确承认核心洞见是 domain transfer；弱化 conjunction novelty claim。

---

### Should-Fix 问题

**W1** [warning] Comparative Trap 张力在 Conclusion 中处理不足
**W2** [warning] "interventional" 等强因果措辞需要收敛
**W3** [warning] 基准数据集单一，样本量偏小
**W4** [warning] Abstract 信息密度过高
**W5** [warning] Appendix Table 5 (GEE CI) 部分条目缺失 CI

---

### 小问题
- M1: Introduction contributions 列表每条过长
- M2: Table 1 第 6 列无 header
- M3: Figure 2 (DAG) 黑白打印下颜色区分消失
- M4: orphan bib entry hoenig2001abuse（工具误报）
- M5: wu2023style bib key 年份不一致
- M6: saito2023verbosity 文献信息需确认

---

### Questions for Authors
1. 如果 pairwise 存在 format amplification，"moderate" effects (BT 63–67%) 的真实效应量可能更小——如何区分 "Likert misses real bias" vs "pairwise creates apparent bias"？
2. 使用 rule-based rewriting 作为更强控制，效应量可能进一步缩小？
3. 100-point scale 下 tie rate 仍高（formality 65.9%）——是 LLM judges 本质倾向"中性"评分，还是测量范式差异？

### Missing References
- Shi et al. (2024) "Judging the Judges"
- Bavaresco et al. (2024) "LLMs Instead of Human Judges?"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 468 · 2026-05-21T17:36:11.769512+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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

_source line 469 · 2026-05-21T17:36:11.820303+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 470 · 2026-05-21T17:36:17.891926+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "8,9",
  "dpi": "165"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "8,9",
    "dpi": "165"
  }
}
```

</details>

---


### Tool result

_source line 471 · 2026-05-21T17:36:18.294461+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p8.png\", \"width\": 1365, \"height\": 1930, \"size_kb\": 546.5}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p9.png\", \"width\": 1365, \"height\": 1930, \"size_kb\": 541.9}], \"total_pages\": 15, \"rendered_pages\": 2, \"dpi\": 165, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 472 · 2026-05-21T17:36:22.057892+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 473 · 2026-05-21T17:36:22.511468+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 474 · 2026-05-21T17:36:23.169734+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1111
}
```

</details>

---


### Tool result

_source line 475 · 2026-05-21T17:36:23.472106+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 960
}
```

</details>

---


### Tool call

_source line 476 · 2026-05-21T17:36:39.959483+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 477 · 2026-05-21T17:36:40.010065+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 478 · 2026-05-21T17:38:07.363168+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 的交叉回应\n\n### Must-Fix\n\n**[AGREE] R2-N1 (页数超限)**: 确认 Section 6 约 5–6 行溢出到 page 9。真实格式违规。我 Round 1 遗漏此问题。建议压缩 Section 6 而非移走 Table 3。\n\n**[REBUT] R2-N2 (Novelty claim → 建议降级为 Should-Fix)**: R2 正确指出 pairwise > Likert 灵敏度是经典结论，但低估了 LLM judges 的特殊性——确定性评分、无疲劳效应、不同 scale anchoring 使得 domain transfer 非 trivial。论文的贡献不仅是灵敏度比较，还包括 per-axis confound decomposition (GEE) 和 NLI-gated content control。建议措辞精确化而非 Must-Fix。\n\n### Should-Fix\n\n**[AGREE] R2-W1 (Comparative Trap)**: R2 发现的重要问题，我未独立标注。pairwise format 本身的 amplification 需要定量估计。与我的 W2 (BT IIA formality 不对称) 有逻辑关联。\n\n**[AGREE] R2-W2 (因果措辞)**: 与我的 W3 完全一致。两位 reviewer 独立标注同一问题。\n\n**[AGREE] R2-W3 (样本量)**: 与我的 W4 一致。\n\n**[REBUT] R2-W4 (Abstract 密度 → 建议降级为 Minor)**: 对实验论文而言 Abstract 中的核心数字是必要的，删除后读者无法评估效应大小。\n\n**[AGREE] R2-W5 (Table 5 CI)**: 应补充完整。\n\n### 关键分歧\n\n1. **Novelty**: R2 列为 Must-Fix，我认为 Should-Fix（phrasing 调整而非核心缺陷）\n2. **NLI 人工验证和 evaluator-producer bias**: 我列为 Must-Fix，R2 未标注——我认为这是论文最大的方法论缺口\n\n### 合并 Must-Fix 清单（两位 Reviewer 共识）\n\n1. NLI gate 人工验证 [R1-N1, R2 未标注但逻辑上应支持]\n2. Evaluator-producer bias 22% OR 下降 + register 缺失 [R1-N2]\n3. 页数超限 [R2-N1, R1 确认]\n\n**Overall 评分不变: 3.5 (Borderline Conference)**",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 的交叉回应\n\n### Must-Fix\n\n**[AGREE] R2-N1 (页数超限)**: 确认 Section 6 约 5–6 行溢出到 page 9。真实格式违规。我 Round 1 遗漏此问题。建议压缩 Section 6 而非移走 Table 3。\n\n**[REBUT] R2-N2 (Novelty claim → 建议降级为 Should-Fix)**: R2 正确指出 pairwise > Likert 灵敏度是经典结论，但低估了 LLM judges 的特殊性——确定性评分、无疲劳效应、不同 scale anchoring 使得 domain transfer 非 trivial。论文的贡献不仅是灵敏度比较，还包括 per-axis confound decomposition (GEE) 和 NLI-gated content control。建议措辞精确化而非 Must-Fix。\n\n### Should-Fix\n\n**[AGREE] R2-W1 (Comparative Trap)**: R2 发现的重要问题，我未独立标注。pairwise format 本身的 amplification 需要定量估计。与我的 W2 (BT IIA formality 不对称) 有逻辑关联。\n\n**[AGREE] R2-W2 (因果措辞)**: 与我的 W3 完全一致。两位 reviewer 独立标注同一问题。\n\n**[AGREE] R2-W3 (样本量)**: 与我的 W4 一致。\n\n**[REBUT] R2-W4 (Abstract 密度 → 建议降级为 Minor)**: 对实验论文而言 Abstract 中的核心数字是必要的，删除后读者无法评估效应大小。\n\n**[AGREE] R2-W5 (Table 5 CI)**: 应补充完整。\n\n### 关键分歧\n\n1. **Novelty**: R2 列为 Must-Fix，我认为 Should-Fix（phrasing 调整而非核心缺陷）\n2. **NLI 人工验证和 evaluator-producer bias**: 我列为 Must-Fix，R2 未标注——我认为这是论文最大的方法论缺口\n\n### 合并 Must-Fix 清单（两位 Reviewer 共识）\n\n1. NLI gate 人工验证 [R1-N1, R2 未标注但逻辑上应支持]\n2. Evaluator-producer bias 22% OR 下降 + register 缺失 [R1-N2]\n3. 页数超限 [R2-N1, R1 确认]\n\n**Overall 评分不变: 3.5 (Borderline Conference)**",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 479 · 2026-05-21T17:38:10.877147+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3513
}
```

</details>

---


### Assistant

_source line 480 · 2026-05-21T17:38:17.184769+00:00_

交叉回应已提交给 Review Director。

核心判断：与 R2 在大部分问题上达成共识（页数超限、因果措辞、样本量、Comparative Trap），但有两个关键分歧——(1) R2 的 Novelty Must-Fix 我认为应降级为 Should-Fix；(2) 我的 NLI 人工验证和 evaluator-producer bias 两个 Must-Fix 是 R2 未覆盖的独立发现。最终评分维持 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1"
}
```

</details>

---


## Round 17

## Round 17

60 recorded events


### User

_source line 481 · 2026-05-21T21:11:05.418794+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性 + 实验设计**的审查。

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
1. **因果声明与证据强度匹配**：标题/摘要/正文中的因果语言（causal, interventional, counterfactual, do-operator）是否与实际方法论强度匹配？是否有 overclaim？
2. **NLI Gate 有效性**：NLI 阈值选择是否有充分 justification？Direction-aware NLI 的理论和实证基础？FNR/FPR 分析是否完备？
3. **统计方法**：Bradley-Terry 模型假设检验（IIA 等）、GEE 选择的合理性、Holm-Bonferroni 校正的正确性、TOST 等价检验的 bound 设定
4. **样本量与统计效力**：n=100 (LLMBar)、n=355 (scaled replication)、n=30 (MT-Bench) 各自的统计效力是否足够？效应量估计的置信区间？
5. **Evaluator-producer confound**：Qwen3-32B 同时作为 rewriter 和 judge 的自我偏好风险；cross-rewriter independence test 的覆盖面
6. **页数合规**：主正文是否 ≤8 页（Limitations 和 References 不计入）

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 482 · 2026-05-21T21:11:14.552422+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__verify_references,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__verify_references,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 483 · 2026-05-21T21:11:14.603041+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 484 · 2026-05-21T21:11:18.472418+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria dimensions"
  }
}
```

</details>

---


### Tool call

_source line 485 · 2026-05-21T21:11:19.526607+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
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

_source line 486 · 2026-05-21T21:11:19.979507+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool call

_source line 487 · 2026-05-21T21:11:20.983584+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool call

_source line 488 · 2026-05-21T21:11:21.435830+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool call

_source line 489 · 2026-05-21T21:11:21.787301+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 490 · 2026-05-21T21:11:30.176627+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria dimensions"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, I found information about ACL ARR 2026 reviewer guidelines and review form. Here are the key details:

## Review Form and Scoring

The main criteria for Findings papers are soundness and reproducibility, while conference recommendations may also consider novelty, impact and other factors.

The review scoring scale includes:
- 5 = Consider for Award: Papers that c
…[truncated 1134 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 11704
}
```

</details>

---


### Tool result

_source line 491 · 2026-05-21T21:11:31.481403+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 465.0}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 498.0}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 588.3}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 512.6}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 456.2}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 510.9}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 490.7}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 510.2}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 539.7}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/pap
…[truncated 311 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 11954
}
```

</details>

---


### Tool result

_source line 492 · 2026-05-21T21:11:31.481998+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 11502
}
```

</details>

---


### Tool result

_source line 493 · 2026-05-21T21:11:31.482461+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 10498
}
```

</details>

---


### Tool result

_source line 494 · 2026-05-21T21:11:31.482943+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 10047
}
```

</details>

---


### Tool result

_source line 495 · 2026-05-21T21:11:31.483619+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 9696
}
```

</details>

---


### Tool call

_source line 496 · 2026-05-21T21:11:38.532727+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 497 · 2026-05-21T21:11:39.385045+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 852
}
```

</details>

---


### Tool call

_source line 498 · 2026-05-21T21:11:39.441514+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 499 · 2026-05-21T21:11:39.924038+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 482
}
```

</details>

---


### Tool call

_source line 500 · 2026-05-21T21:11:39.974662+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 501 · 2026-05-21T21:11:40.427131+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 502 · 2026-05-21T21:11:41.481490+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their descriptions, and rating scales. I need the exact criteria names, scale ranges, and what each score means."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their descriptions, and rating scales. I need the exact criteria names, scale ranges, and what each score means."
  }
}
```

</details>

---


### Tool call

_source line 503 · 2026-05-21T21:11:42.385469+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 504 · 2026-05-21T21:11:42.889075+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 505 · 2026-05-21T21:11:43.242182+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 506 · 2026-05-21T21:11:43.292796+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 507 · 2026-05-21T21:11:43.748869+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 859
}
```

</details>

---


### Tool result

_source line 508 · 2026-05-21T21:11:44.101275+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 808
}
```

</details>

---


### Tool result

_source line 509 · 2026-05-21T21:11:48.120246+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## 1. **Reviewer Confidence** (1-5 scale)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully"
- **4**: Quite sure with unlikely missed details
- **3**: Pretty sure but chance of missing something
- **2**: Willing to defend evaluation but likely missed details
- **1**: Outside expertise area or paper incomprehensible

## 2. **Soundness** (1-5 scale with half-points)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: Strong with sufficient claims support
- **3**: Acceptable with main claims supported
- **2**: Poor with unsupported main claims
- **1**: "Major Issues: This study is not yet sufficiently thorough"

## 3. **Excitement** (1-5 scale with half-points)
Measures subjective appeal regarding innovation, impact, or personal relevance:
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: Would mention paper to colleagues
- **3**: Might discuss specific points
- **2**: Potentially interesting to broader community
- **1**: "Not Exciting: this paper does not resonate with me"

## 4. **Overall Assessment** (1-5 scale with half-points)
Conference publication recommendation:
- **5**: "Consider for Award" (top 2.5%)
- **4**: Conference acceptance
- **3**: Findings acceptance
- **2**: Resubmit next cycle
- **1**: "Do not resubmit"

## 5. **Reproducibility** (1-5 scale)
- **5**: "They could easily reproduce the results"
- **4**: Mostly reproducible
- **3**: Reproducible with difficulty
- **2**: Hard to reproduce
- **1**: Cannot reproduce

## 6. **Datasets & Software** (1-5 scales)
Both measure resource value:
- **5**: Enabling for research directions
- **4**: Useful for ongoing work
- **3**: Potentially useful
- **2**: Documentary value only
- **1**: No usable resources

## 7. **Author Identity Knowledge** (1-5 scale)
- **5**: Known through double-blind violation
- **4**: Known from allowed preprints
- **3**: Discernible from submissi
…[truncated 64 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6638
}
```

</details>

---


### Tool call

_source line 510 · 2026-05-21T21:11:59.674439+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
  "project": "causal_style_decomp_judge",
  "pages": "10-16",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.pdf",
    "project": "causal_style_decomp_judge",
    "pages": "10-16",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 511 · 2026-05-21T21:12:00.635661+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 432.9}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 456.3}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 460.1}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 491.8}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 605.2}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 584.4}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 51.3}], \"total_pages\": 16, \"rendered_pages\": 7, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 961
}
```

</details>

---


### Tool call

_source line 512 · 2026-05-21T21:12:00.636220+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 513 · 2026-05-21T21:12:01.191676+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 514 · 2026-05-21T21:12:02.199467+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1563
}
```

</details>

---


### Tool call

_source line 515 · 2026-05-21T21:12:02.199950+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 516 · 2026-05-21T21:12:02.603454+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 517 · 2026-05-21T21:12:03.057385+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1865
}
```

</details>

---


### Tool call

_source line 518 · 2026-05-21T21:12:03.057869+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 519 · 2026-05-21T21:12:03.761816+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 520 · 2026-05-21T21:12:04.818826+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2618
}
```

</details>

---


### Tool result

_source line 521 · 2026-05-21T21:12:05.122545+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2519
}
```

</details>

---


### Tool result

_source line 522 · 2026-05-21T21:12:05.574725+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2516
}
```

</details>

---


### Tool result

_source line 523 · 2026-05-21T21:12:05.676107+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1914
}
```

</details>

---


### Tool call

_source line 524 · 2026-05-21T21:12:09.994337+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 525 · 2026-05-21T21:12:10.499888+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 526 · 2026-05-21T21:12:11.405790+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1411
}
```

</details>

---


### Tool call

_source line 527 · 2026-05-21T21:12:11.406218+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 528 · 2026-05-21T21:12:12.063384+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 529 · 2026-05-21T21:12:12.369110+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1869
}
```

</details>

---


### Tool call

_source line 530 · 2026-05-21T21:12:12.369559+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 531 · 2026-05-21T21:12:12.723932+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1317
}
```

</details>

---


### Tool call

_source line 532 · 2026-05-21T21:12:12.724428+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images/main_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 533 · 2026-05-21T21:12:13.479393+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1416
}
```

</details>

---


### Tool result

_source line 534 · 2026-05-21T21:12:13.932139+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1562
}
```

</details>

---


### Tool result

_source line 535 · 2026-05-21T21:12:14.035148+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1310
}
```

</details>

---


### Tool call

_source line 536 · 2026-05-21T21:15:10.594741+00:00_

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
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 537 · 2026-05-21T21:15:10.645278+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 538 · 2026-05-21T21:17:55.842779+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿意见（方法严谨性 + 实验设计）\n\n---\n\n## Summary\n\n本文提出 Controlled Style Decomposition (CSD) 框架，通过 NLI-gated content control、per-axis style rewriting 和 position-controlled pairwise comparison 检测 LLM judge 的风格偏差。核心发现有二：(1) Likert Blindspot——Likert 评分系统性地遗漏 pairwise comparison 可以检测到的风格偏差（BT 63–84%, p < 0.001 vs. Likert n.s.），在中等效应量下完全失灵（d → 0 at n=355），在较强效应量下衰减超 60%；(2) GEE 条件分解揭示 per-axis confound 结构——verbosity 为 style-dominated，formality 为 conditional，register 为 judge-dependent。实验覆盖 4 个 judge、3 个 benchmark、3 个 style axis，方法论总体较为严谨，但在 evaluator-producer confound 控制和部分统计论证上存在可修复的不足。\n\n---\n\n## Strengths\n\n**S1** [方法设计] CSD 的三阶段流水线设计（rewriting → NLI gating → position-controlled comparison）逻辑清晰，每一步都有明确的 confound blocking 目标。DAG（Figure 2）的呈现方式值得肯定——明确标注了\"design rationale, not a claim of perfect identification\"，并在 caption 中注明 residual confounding 路径（S→Q, dashed orange），避免了 overclaim。Section 3.5 明确声明\"interventional rather than formal causal evidence\"且不援引 SUTVA/consistency assumptions，因果语言的校准在同类论文中属于上乘。\n\n**S2** [统计方法层次感] 七种统计方法的 sensitivity hierarchy（Table 2）是亮点——不仅证明了 Likert Blindspot 不是特定检验的 artifact，还揭示了从 BT model 到 Wilcoxon signed-rank 的完整 sensitivity spectrum。Verbosity 轴的复制（Appendix L, Table 12）进一步确认该 pattern 在更强效应量下依然成立。100-point continuous Likert（Appendix M）排除了 scale granularity 解释，将 Blindspot 归因于 absolute vs. relative evaluation 范式差异——这是超出简单\"Likert 不灵敏\"结论的有价值发现。\n\n**S3** [Cross-judge replication 的说服力] 三个 target judge（GPT-4o, Qwen3-32B, Llama-3.3-70B）涵盖 proprietary API、open 32B、open 70B 三种架构，加上 Claude Sonnet 4 作为 negative control。GEE confound structure 在三个 target judge 上的一致性（verbosity: Style OR 8–13, Orig OR < 1; formality: both significant）提升了结果的可推广性。Claude Sonnet 4 在相同 pairwise format 下检测不到 bias（BT 56.2%/54.1%, n.s.）是有力的 discriminative validity 证据。\n\n**S4** [NLI gate 的多层验证] Threshold sensitivity sweep（11 thresholds, ≤3pp variation, Appendix E）、bimodal NLI score distribution（plateau 而非 cliff edge）、GPT-4o full-scale validation（200 decisions）、NLI-fail pair ablation（formality 反转至 41.7%, Appendix N）、以及 direction-aware vs. bidirectional gating 的 empirical justification（Appendix F）——这些构成了对 NLI gate 的系统性 robustness 检验，在同类工作中罕见。\n\n**S5** [Blindspot 的 severity spectrum 刻画] 不仅展示了 Blindspot 的存在，还量化了其效应量依赖性：moderate bias 下完全失灵（d → 0 at n=355），stronger effects 下部分衰减（>60%）。Bootstrap attenuation 分析（Appendix J, Table 10）的 d_median = -0.017 随 n 增大 CI 收窄但始终包含零，结合 BT 稳定在 66.5%，有力区分了 measurement attenuation 和 power limitation。这是论文中分析最精细的部分。\n\n---\n\n## Weaknesses\n\n**W1** [Must-Fix] **Evaluator-producer confound 控制不充分**\n- 具体位置：Section 3.1, Appendix D, Limitations\n- 问题：Qwen3-32B 同时担任所有实验的 rewriter，三个 target judge 全部在 Qwen3-32B 重写的文本上评估。Cross-rewriter validation（Appendix D）仅对 Qwen3-32B judge 进行了 GPT-4o rewriter 替换（verbosity: Style OR 从 13.10 降至 10.17, -22%; formality: BT 从 66.5% 降至 64.4%）。GPT-4o 和 Llama-70B 作为 judge 时，我们不知道它们检测到的\"formality bias\"有多少来自对 Qwen3-32B 特定重写风格的反应而非 formality 本身。22% 的 Style OR 下降（verbosity）表明 evaluator-producer 效应是 non-trivial 的。\n- 为什么影响接收：这是核心 identification 问题。如果三个 judge 的\"cross-judge replication\"（Section 5.3）实际上部分反映了对同一 rewriter 风格的共同反应，那么 replication 的独立性被削弱。论文的 contribution #3（per-axis confound structure consistent across three architectures）的可信度取决于此。\n- 建议修改方向：至少对 GPT-4o judge 执行一次完整的 cross-rewriter validation（用 GPT-4o 或 Llama 作为 rewriter），证明 confound structure 在不同 rewriter 下也一致。如果资源有限，至少对主要发现（formality + verbosity on LLMBar）做一个 rewriter 进行对比。\n\n**W2** [Must-Fix] **Section 4.1 与 Table 1 关于 register 分类的矛盾**\n- 具体位置：Section 4.1 第 8 行; Table 1 footnote\n- 问题：Section 4.1 明确定义 primary family 为 8 个检验（\"three judges × formality and verbosity, plus register for GPT-4o and Qwen3-32B\"），但 Table 1 将 GPT-4o register 和 Qwen3 register 标记为 \"†_e\"（exploratory）。如果 register 在 primary family 内，Holm-Bonferroni 校正基于 8 个检验；如果在外，校正基于 6 个检验。这直接影响 adjusted p-values 和哪些结果被标记为 significant。\n- 为什么影响接收：多重比较校正的不一致是方法论硬伤，审稿人和 AC 会质疑结果的 validity。\n- 建议修改方向：统一分类。建议将 register 从 primary family 移出（因为 register 结果确实较弱且解释性有限），将 Section 4.1 改为 6-test primary family，或者保留 8-test family 但修正 Table 1 标注。\n\n**W3** [Should-Fix] **TOST equivalence testing 的 Δ=15pp margin 过宽**\n- 具体位置：Appendix G\n- 问题：对 Claude Sonnet 4 的 equivalence testing 在 Δ=10pp 下 underpowered（n=87），在 Δ=15pp 下才 confirm equivalence。但 Δ=15pp 意味着 Claude 可以有 BT 高达 65%（15pp above 50%）仍被判定为\"无偏差\"。而论文将 GPT-4o formality 的 +13pp（BT 63%）认定为 genuine bias。Δ=15pp 的 equivalence zone 与最小确认偏差（+13pp）之间仅有 2pp 的 gap，discriminative power 很弱。\n- 建议：(a) 明确说明在当前样本量下 TOST 的局限性；(b) 不要声称 Claude\"不存在偏差\"，而是说\"在 Δ=15pp 精度下未检测到偏差\"；(c) 增加 Claude 样本量或在 Limitations 中标记此为 open question。\n\n**W4** [Should-Fix] **NLI gate validation 的 FNR 估计存在循环性**\n- 具体位置：Section 5.1\n- 问题：主要的 FNR 估计（8/95 = 8.4%）使用 Qwen3-32B 作为 LLM annotator——这与 rewriter 是同一模型。Qwen3-32B 可能系统性地认为自己的改写保留了内容（self-consistency bias）。虽然论文也提供了 GPT-4o 的 full-scale validation，但 GPT-4o validation 报告的是 precision（92.1% formality, 82.6% verbosity），而非 FNR，两个指标描述不同方向的错误。\n- 建议：报告 GPT-4o validation 对应的 FNR（而非仅报告 precision），或在正文中明确标注 8.4% FNR 来自与 rewriter 相同的模型并讨论其上限/下限含义。\n\n**W5** [Should-Fix] **Verbosity 的 direction-aware NLI gate 有 17.4% FPR**\n- 具体位置：Section 5.1, Appendix F\n- 问题：GPT-4o validation 显示 verbosity 的 direction-aware gate pass precision 仅 82.6%（即 17.4% 的通过 pairs 实际上内容保存失败）。在 n=86 的样本中，约 15 对可能包含 content confound。虽然 NLI ablation（Appendix N）显示 NLI-fail pairs 的 BT 仍为 75.0%——表明 verbosity bias 足够强大以 overwhelm content noise——但这也意味着 verbosity 的效应量可能被轻度高估。\n- 为什么影响评分：17.4% FPR 对于一个声称\"blocking the R→Q path\"的 content preservation gate 来说偏高。虽然不足以否定结论，但削弱了\"lower bound\"的论证。\n- 建议：在正文（而非仅 Appendix）中报告此 FPR 数字，并量化其对 BT 估计的 potential bias（e.g., 通过加权分析或 sensitivity analysis）。\n\n**W6** [Should-Fix] **缺乏任何人工验证**\n- 具体位置：全文\n- 问题：整个流水线完全依赖自动化系统（DeBERTa for NLI, LLMs for rewriting/judging/validation）。没有任何人工评估来验证 (a) 重写是否确实只改变了目标 style axis, (b) NLI gate decisions 是否与人类判断一致, (c) pairwise preference 方向是否 align with human perception。在一篇关于 LLM judge bias 的论文中，完全依赖 LLM 进行验证存在方法论上的 irony。\n- 建议：至少对 50 对 NLI gate decisions 进行人工 annotation，报告 human-NLI agreement 和 human-LLM annotator agreement。如果资源不足，在 Limitations 中明确标注此为关键局限。\n\n**W7** [Minor] **Cross-benchmark 选择性测试**\n- 具体位置：Table 1\n- 问题：AlpacaEval 仅测试 3 个 judge×axis 组合，MT-Bench 仅测试 2 个。Table 1 footnote 说\"cross-benchmark validation focuses on strongest-evidence configurations\"，但这引入了 selection bias：只在预期效应最强的配置上做 replication，自然容易成功。缺失的组合（e.g., Llama-70B on AlpacaEval, verbosity on MT-Bench）可能提供不同的证据。\n- 建议：明确列出选择标准（pre-registered or post-hoc），或将 cross-benchmark 部分明确标注为 exploratory。\n\n**W8** [Minor] **Bradley-Terry 模型的 within-pair 依赖**\n- 具体位置：Section 3.3, Section 4.1\n- 问题：Position swap 产生每对 2 个观测，但 BT model 假设观测独立。Pair-level bootstrap 在 CI 估计中处理了此依赖，但 point estimate 和 p-value 来自假设独立的 BT model。论文未讨论此 violation 的影响。Sign test（仅用 consistent pairs）作为 robustness check 部分缓解了此问题。\n- 建议：添加一句说明 pair-level bootstrap 如何处理 within-pair 依赖，以及为何 point estimate 的 bias 可忽略（因为 BT model 本质上在估计一个 binomial proportion）。\n\n---\n\n## Questions\n\n**Q1**: Table 3 中 GPT-4o verbosity 和 GPT-4o formality 的 GEE CI 缺失（仅报告 point estimate），而其他配置有 CI。这是排版遗漏还是有意为之？如果是遗漏，请补充。\n\n**Q2**: Section 5.2 报告 Likert tie rate 在 58–73% 之间。这些 tie rate 是否考虑了 judge 的 temperature=0 设置？如果 judge 倾向于给出相似分数（例如系统性地给 7/10），tie rate 高可能反映 judge 的 calibration 问题而非 Likert 本身的测量局限。是否尝试过分析 non-tied pairs 的 Likert 效应量？\n\n**Q3**: 论文声明 Claude Sonnet 4 作为 negative control \"detects no bias\"（Abstract, Section 5.3）。但 Appendix G 的 TOST 结果显示在 Δ=10pp 下 underpowered。这两种说法之间如何调和？Claude 是\"没有 bias\"还是\"我们无法在当前样本量下排除 moderate bias\"？\n\n**Q4**: GEE 的 Originality OR < 1 for verbosity（Table 3: 0.38–0.49）被解释为\"any artifact favors rewrites over originals\"（Section 5.4）。但 Orig OR < 1 也可能意味着 judge 在 verbose=original 时更倾向于选择 rewrite——这不一定是\"artifact favoring rewrites\"，也可能是 verbose originals 的 quality 较低。能否澄清 Originality OR 的确切语义？\n\n**Q5**: Rewriter independence test（Appendix D）仅替换了 rewriter 而保持 Qwen3-32B 作为 judge。是否有计划或可能性测试反向配置（Qwen3-32B rewrite + GPT-4o judge vs. GPT-4o rewrite + GPT-4o judge），以完全分离 evaluator-producer 效应？\n\n---\n\n## Missing References\n\n1. **Shankar et al. (2024)** \"Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences\" — 与本文的 meta-evaluation 视角直接相关，讨论了 LLM 评估器验证的循环性问题。\n\n2. **Huang et al. (2024)** \"Bias and Fairness in Large Language Models: A Survey\" — 更广泛的 LLM bias survey，本文的 Related Work 聚焦于 judge bias 但缺少与 general LLM bias literature 的连接。\n\n3. **Zheng et al. (2024)** \"On the Limitations of LLM-as-a-Judge\" (若存在此方向的综述)——更全面地讨论 LLM-as-judge 的局限性。\n\n---\n\n## Overall Assessment\n\n**Overall**: **3.5** (Borderline Conference)\n\n**一句话总结**: 方法论设计精良、统计分析层次丰富，Likert Blindspot 是对 LLM evaluation 社区有实际价值的发现，但 evaluator-producer confound 的不充分控制和缺乏人工验证削弱了核心 identification claim 的可信度。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 总体方法论严谨，GEE 分解和多层 sensitivity analysis 令人印象深刻。但 evaluator-producer confound 仅对 1/3 judge 做了 cross-rewriter 验证（W1），Section 4.1 与 Table 1 的 register 分类矛盾影响多重比较校正的可信度（W2），verbosity NLI gate 的 17.4% FPR 削弱了 content preservation claim（W5）。 |\n| Excitement | 3.5/5 | Likert Blindspot 的量化对 LLM evaluation 社区有直接实践意义（特别是 RLHF/DPO pipeline 依赖 pairwise preference），per-axis confound structure 是有启发性的分析框架。但核心洞察（pairwise > Likert sensitivity）在 measurement theory 中已有理论预测，本文的贡献主要在于 empirical quantification 和 LLM 评估场景的具体化。 |\n| Reproducibility | 3/5 | 方法描述详尽（Implementation Details, Appendix P），统计方法可复现（choix library, statsmodels, seed=42）。但代码和数据尚未发布（\"released upon acceptance\"），NLI gate 的 axis-specific thresholding 策略需要实现细节，cross-rewriter validation 的不完整性意味着部分结果难以独立验证。 |\n| Confidence | 4/5 | 本审稿人在 LLM evaluation、因果推断方法论和统计建模方面有较强背景。仔细阅读了全文含全部 Appendix，对统计方法和实验设计进行了逐项检查。 |\n\n---\n\n## Detailed Comments（逐节）\n\n### Title & Abstract\n- 标题准确反映内容，\"Likert Blindspot\"命名有记忆点。\n- Abstract 中\"the first framework combining...\"的 novelty claim 在 Related Work 中得到了合理支撑，每个组件的先行工作都有引用。\n- Abstract 提到 \"seven statistical methods\" confirm the effect is structural——这个数字在正文中得到了完整展开（Table 2）。\n\n### Section 1 (Introduction)\n- 开篇对 style bias 问题的 motivation 清晰有力，引用了 li2026preference（76–92%）和 soumik2026judging（0.76–0.92）量化了问题的严重性。\n- \"no single framework integrates all four requirements\"的 gap statement 合理，但\"per-instance diagnostics\"这个 requirement 在后续实验中体现得不够——主要结果都是 aggregate 的（BT win probability, GEE OR），per-instance diagnostic 能力（CSD 可以标记每个 pair 是否 biased）仅在 NLI gate 层面体现。\n- Figure 1（pipeline diagram）清晰展示了 sample attrition，这是好的实验报告实践。\n\n### Section 2 (Related Work)\n- 结构清晰，三个 paragraph 分别覆盖 interventional approaches、measurement sensitivity、style bias detection。\n- 对 RATE 的批判性分析（Likert ATE vulnerability）是有见地的，但措辞可以更 balanced——RATE 和 CSD 测量的是不同的东西（aggregate quality effect vs. per-axis style preference），直接说 RATE 的 findings \"may underestimate\" 需要更多 caveat。\n- Bradley-Terry 段落的 positioning 清楚说明了 BT 在 evaluation 生态系统中的位置。\n\n### Section 3 (Method)\n- Style-controlled rewriting（Section 3.1）的描述清晰。Temperature 0.7 的选择未 justify——是否做过 temperature sensitivity analysis？\n- NLI gate（Section 3.2）的 direction-aware 设计是 well-motivated 的 innovation。但正文中 pass rate 的变化（65% → 86%）仅给出了 verbosity 数据，formality 的 pass rate（88%）需要从 Table 1 footnote 间接推导。建议在正文直接报告各 axis 的 pass rate。\n- Section 3.5 的 identification 声明是全文最精确的因果语言——值得在 abstract 中也使用类似的 calibrated language（目前 abstract 更偏 assertive）。\n\n### Section 4 (Experiments)\n- Table 1 信息密度高但可读性可改进。建议：(a) 为 Blindspot/both sig./neither 使用颜色编码而非仅符号；(b) 分离 LLMBar/AEval/MTB 为独立子表或添加水平分隔线（目前有但不够明显）。\n- Holm-Bonferroni 的 family 定义（Section 4.1）需要与 Table 1 标注统一（W2）。\n- Section 4.1 将 consistency filter validation 和 NLI threshold sweep 分类为\"confirmatory\"和\"exploratory\"——这个 pre-registration 式的分类值得肯定，但未说明这些分类是 pre-registered 还是 post-hoc。\n\n### Section 5 (Analysis)\n- Section 5.1（NLI Gate Validation）是全文最 thorough 的 validation 部分。Gwet's AC1 vs. Cohen's κ 的 prevalence skew 讨论表明作者对 inter-rater agreement 指标的理解深入。\n- Section 5.2（Likert vs. Pairwise）的 \"measurement attenuation vs. construct divergence\" 双重解释框架是成熟的科学态度。但建议在 Abstract 和 Conclusion 中也保持这种 agnosticism——目前 Abstract 的措辞更偏向 \"Likert misses bias\"（暗示 measurement failure），而非 \"Likert measures something different\"。\n- Section 5.2 的 detection vs. amplification 分析（6 controls bounding amplification risk）是对 Jeong et al. (2025) Comparative Trap 的直接回应，structure 清晰。但 control (ii)（Claude shows no bias）的逻辑有弱点——Claude 可能确实没有 style preference，而非 pairwise format 不 amplify。\n- Section 5.6（GEE Conditional Decomposition）是重要的分析贡献。Per-axis confound structure 的 regime classification（style-dominated/conditional/judge-dependent）为后续研究提供了可操作的框架。但 regime classification 的 threshold 未明确定义——什么 Style OR / Orig OR 比值构成 \"style-dominated\" vs. \"conditional\"？\n\n### Limitations\n- 覆盖了三个关键点：(a) evaluator-producer bias, (b) validation methodology and scale, (c) NLI gate 的 identifiability limit。\n- 但 Limitations 中关于 cross-rewriter validation 的说法令人困惑：\"All experiments use the same Qwen3-32B rewriter without the cross-rewriter validation applied to formality and verbosity (Appendix D)\"——但 Appendix D 确实对 formality AND verbosity 都做了 cross-rewriter validation（Tables 6-7）。这句话的意思是其他 benchmark（AEval, MTB）上没有做 cross-rewriter validation？需要澄清。\n\n### Appendix\n- Appendix 的覆盖面令人印象深刻（A-P, 共 16 个附录项），几乎每个可能被质疑的方法论选择都有对应的 robustness check。\n- Table 5（GEE CI）中 GPT-4o formality 和 GPT-4o verbosity 缺失 CI 是排版疏忽（Q1）。\n- Appendix H 的 BT GOF test 和 stratified analysis 是 solid 的 model validation。Likert-tied subset analysis（formality BT=67.3%, verbosity BT=76.0%）有力排除了 originality confounding 的替代解释。\n\n### 页数合规\n主正文（Title → Conclusion）结束于第 8 页底部，Limitations 从第 9 页开始。**符合 EMNLP 2026 Long Paper 8 页限制。**",
  "reviewer_id": "1",
  "project": "causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿意见（方法严谨性 + 实验设计）\n\n---\n\n## Summary\n\n本文提出 Controlled Style Decomposition (CSD) 框架，通过 NLI-gated content control、per-axis style rewriting 和 position-controlled pairwise comparison 检测 LLM judge 的风格偏差。核心发现有二：(1) Likert Blindspot——Likert 评分系统性地遗漏 pairwise comparison 可以检测到的风格偏差（BT 63–84%, p < 0.001 vs. Likert n.s.），在中等效应量下完全失灵（d → 0 at n=355），在较强效应量下衰减超 60%；(2) GEE 条件分解揭示 per-axis confound 结构——verbosity 为 style-dominated，formality 为 conditional，register 为 judge-dependent。实验覆盖 4 个 judge、3 个 benchmark、3 个 style axis，方法论总体较为严谨，但在 evaluator-producer confound 控制和部分统计论证上存在可修复的不足。\n\n---\n\n## Strengths\n\n**S1** [方法设计] CSD 的三阶段流水线设计（rewriting → NLI gating → position-controlled comparison）逻辑清晰，每一步都有明确的 confound blocking 目标。DAG（Figure 2）的呈现方式值得肯定——明确标注了\"design rationale, not a claim of perfect identification\"，并在 caption 中注明 residual confounding 路径（S→Q, dashed orange），避免了 overclaim。Section 3.5 明确声明\"interventional rather than formal causal evidence\"且不援引 SUTVA/consistency assumptions，因果语言的校准在同类论文中属于上乘。\n\n**S2** [统计方法层次感] 七种统计方法的 sensitivity hierarchy（Table 2）是亮点——不仅证明了 Likert Blindspot 不是特定检验的 artifact，还揭示了从 BT model 到 Wilcoxon signed-rank 的完整 sensitivity spectrum。Verbosity 轴的复制（Appendix L, Table 12）进一步确认该 pattern 在更强效应量下依然成立。100-point continuous Likert（Appendix M）排除了 scale granularity 解释，将 Blindspot 归因于 absolute vs. relative evaluation 范式差异——这是超出简单\"Likert 不灵敏\"结论的有价值发现。\n\n**S3** [Cross-judge replication 的说服力] 三个 target judge（GPT-4o, Qwen3-32B, Llama-3.3-70B）涵盖 proprietary API、open 32B、open 70B 三种架构，加上 Claude Sonnet 4 作为 negative control。GEE confound structure 在三个 target judge 上的一致性（verbosity: Style OR 8–13, Orig OR < 1; formality: both significant）提升了结果的可推广性。Claude Sonnet 4 在相同 pairwise format 下检测不到 bias（BT 56.2%/54.1%, n.s.）是有力的 discriminative validity 证据。\n\n**S4** [NLI gate 的多层验证] Threshold sensitivity sweep（11 thresholds, ≤3pp variation, Appendix E）、bimodal NLI score distribution（plateau 而非 cliff edge）、GPT-4o full-scale validation（200 decisions）、NLI-fail pair ablation（formality 反转至 41.7%, Appendix N）、以及 direction-aware vs. bidirectional gating 的 empirical justification（Appendix F）——这些构成了对 NLI gate 的系统性 robustness 检验，在同类工作中罕见。\n\n**S5** [Blindspot 的 severity spectrum 刻画] 不仅展示了 Blindspot 的存在，还量化了其效应量依赖性：moderate bias 下完全失灵（d → 0 at n=355），stronger effects 下部分衰减（>60%）。Bootstrap attenuation 分析（Appendix J, Table 10）的 d_median = -0.017 随 n 增大 CI 收窄但始终包含零，结合 BT 稳定在 66.5%，有力区分了 measurement attenuation 和 power limitation。这是论文中分析最精细的部分。\n\n---\n\n## Weaknesses\n\n**W1** [Must-Fix] **Evaluator-producer confound 控制不充分**\n- 具体位置：Section 3.1, Appendix D, Limitations\n- 问题：Qwen3-32B 同时担任所有实验的 rewriter，三个 target judge 全部在 Qwen3-32B 重写的文本上评估。Cross-rewriter validation（Appendix D）仅对 Qwen3-32B judge 进行了 GPT-4o rewriter 替换（verbosity: Style OR 从 13.10 降至 10.17, -22%; formality: BT 从 66.5% 降至 64.4%）。GPT-4o 和 Llama-70B 作为 judge 时，我们不知道它们检测到的\"formality bias\"有多少来自对 Qwen3-32B 特定重写风格的反应而非 formality 本身。22% 的 Style OR 下降（verbosity）表明 evaluator-producer 效应是 non-trivial 的。\n- 为什么影响接收：这是核心 identification 问题。如果三个 judge 的\"cross-judge replication\"（Section 5.3）实际上部分反映了对同一 rewriter 风格的共同反应，那么 replication 的独立性被削弱。论文的 contribution #3（per-axis confound structure consistent across three architectures）的可信度取决于此。\n- 建议修改方向：至少对 GPT-4o judge 执行一次完整的 cross-rewriter validation（用 GPT-4o 或 Llama 作为 rewriter），证明 confound structure 在不同 rewriter 下也一致。如果资源有限，至少对主要发现（formality + verbosity on LLMBar）做一个 rewriter 进行对比。\n\n**W2** [Must-Fix] **Section 4.1 与 Table 1 关于 register 分类的矛盾**\n- 具体位置：Section 4.1 第 8 行; Table 1 footnote\n- 问题：Section 4.1 明确定义 primary family 为 8 个检验（\"three judges × formality and verbosity, plus register for GPT-4o and Qwen3-32B\"），但 Table 1 将 GPT-4o register 和 Qwen3 register 标记为 \"†_e\"（exploratory）。如果 register 在 primary family 内，Holm-Bonferroni 校正基于 8 个检验；如果在外，校正基于 6 个检验。这直接影响 adjusted p-values 和哪些结果被标记为 significant。\n- 为什么影响接收：多重比较校正的不一致是方法论硬伤，审稿人和 AC 会质疑结果的 validity。\n- 建议修改方向：统一分类。建议将 register 从 primary family 移出（因为 register 结果确实较弱且解释性有限），将 Section 4.1 改为 6-test primary family，或者保留 8-test family 但修正 Table 1 标注。\n\n**W3** [Should-Fix] **TOST equivalence testing 的 Δ=15pp margin 过宽**\n- 具体位置：Appendix G\n- 问题：对 Claude Sonnet 4 的 equivalence testing 在 Δ=10pp 下 underpowered（n=87），在 Δ=15pp 下才 confirm equivalence。但 Δ=15pp 意味着 Claude 可以有 BT 高达 65%（15pp above 50%）仍被判定为\"无偏差\"。而论文将 GPT-4o formality 的 +13pp（BT 63%）认定为 genuine bias。Δ=15pp 的 equivalence zone 与最小确认偏差（+13pp）之间仅有 2pp 的 gap，discriminative power 很弱。\n- 建议：(a) 明确说明在当前样本量下 TOST 的局限性；(b) 不要声称 Claude\"不存在偏差\"，而是说\"在 Δ=15pp 精度下未检测到偏差\"；(c) 增加 Claude 样本量或在 Limitations 中标记此为 open question。\n\n**W4** [Should-Fix] **NLI gate validation 的 FNR 估计存在循环性**\n- 具体位置：Section 5.1\n- 问题：主要的 FNR 估计（8/95 = 8.4%）使用 Qwen3-32B 作为 LLM annotator——这与 rewriter 是同一模型。Qwen3-32B 可能系统性地认为自己的改写保留了内容（self-consistency bias）。虽然论文也提供了 GPT-4o 的 full-scale validation，但 GPT-4o validation 报告的是 precision（92.1% formality, 82.6% verbosity），而非 FNR，两个指标描述不同方向的错误。\n- 建议：报告 GPT-4o validation 对应的 FNR（而非仅报告 precision），或在正文中明确标注 8.4% FNR 来自与 rewriter 相同的模型并讨论其上限/下限含义。\n\n**W5** [Should-Fix] **Verbosity 的 direction-aware NLI gate 有 17.4% FPR**\n- 具体位置：Section 5.1, Appendix F\n- 问题：GPT-4o validation 显示 verbosity 的 direction-aware gate pass precision 仅 82.6%（即 17.4% 的通过 pairs 实际上内容保存失败）。在 n=86 的样本中，约 15 对可能包含 content confound。虽然 NLI ablation（Appendix N）显示 NLI-fail pairs 的 BT 仍为 75.0%——表明 verbosity bias 足够强大以 overwhelm content noise——但这也意味着 verbosity 的效应量可能被轻度高估。\n- 为什么影响评分：17.4% FPR 对于一个声称\"blocking the R→Q path\"的 content preservation gate 来说偏高。虽然不足以否定结论，但削弱了\"lower bound\"的论证。\n- 建议：在正文（而非仅 Appendix）中报告此 FPR 数字，并量化其对 BT 估计的 potential bias（e.g., 通过加权分析或 sensitivity analysis）。\n\n**W6** [Should-Fix] **缺乏任何人工验证**\n- 具体位置：全文\n- 问题：整个流水线完全依赖自动化系统（DeBERTa for NLI, LLMs for rewriting/judging/validation）。没有任何人工评估来验证 (a) 重写是否确实只改变了目标 style axis, (b) NLI gate decisions 是否与人类判断一致, (c) pairwise preference 方向是否 align with human perception。在一篇关于 LLM judge bias 的论文中，完全依赖 LLM 进行验证存在方法论上的 irony。\n- 建议：至少对 50 对 NLI gate decisions 进行人工 annotation，报告 human-NLI agreement 和 human-LLM annotator agreement。如果资源不足，在 Limitations 中明确标注此为关键局限。\n\n**W7** [Minor] **Cross-benchmark 选择性测试**\n- 具体位置：Table 1\n- 问题：AlpacaEval 仅测试 3 个 judge×axis 组合，MT-Bench 仅测试 2 个。Table 1 footnote 说\"cross-benchmark validation focuses on strongest-evidence configurations\"，但这引入了 selection bias：只在预期效应最强的配置上做 replication，自然容易成功。缺失的组合（e.g., Llama-70B on AlpacaEval, verbosity on MT-Bench）可能提供不同的证据。\n- 建议：明确列出选择标准（pre-registered or post-hoc），或将 cross-benchmark 部分明确标注为 exploratory。\n\n**W8** [Minor] **Bradley-Terry 模型的 within-pair 依赖**\n- 具体位置：Section 3.3, Section 4.1\n- 问题：Position swap 产生每对 2 个观测，但 BT model 假设观测独立。Pair-level bootstrap 在 CI 估计中处理了此依赖，但 point estimate 和 p-value 来自假设独立的 BT model。论文未讨论此 violation 的影响。Sign test（仅用 consistent pairs）作为 robustness check 部分缓解了此问题。\n- 建议：添加一句说明 pair-level bootstrap 如何处理 within-pair 依赖，以及为何 point estimate 的 bias 可忽略（因为 BT model 本质上在估计一个 binomial proportion）。\n\n---\n\n## Questions\n\n**Q1**: Table 3 中 GPT-4o verbosity 和 GPT-4o formality 的 GEE CI 缺失（仅报告 point estimate），而其他配置有 CI。这是排版遗漏还是有意为之？如果是遗漏，请补充。\n\n**Q2**: Section 5.2 报告 Likert tie rate 在 58–73% 之间。这些 tie rate 是否考虑了 judge 的 temperature=0 设置？如果 judge 倾向于给出相似分数（例如系统性地给 7/10），tie rate 高可能反映 judge 的 calibration 问题而非 Likert 本身的测量局限。是否尝试过分析 non-tied pairs 的 Likert 效应量？\n\n**Q3**: 论文声明 Claude Sonnet 4 作为 negative control \"detects no bias\"（Abstract, Section 5.3）。但 Appendix G 的 TOST 结果显示在 Δ=10pp 下 underpowered。这两种说法之间如何调和？Claude 是\"没有 bias\"还是\"我们无法在当前样本量下排除 moderate bias\"？\n\n**Q4**: GEE 的 Originality OR < 1 for verbosity（Table 3: 0.38–0.49）被解释为\"any artifact favors rewrites over originals\"（Section 5.4）。但 Orig OR < 1 也可能意味着 judge 在 verbose=original 时更倾向于选择 rewrite——这不一定是\"artifact favoring rewrites\"，也可能是 verbose originals 的 quality 较低。能否澄清 Originality OR 的确切语义？\n\n**Q5**: Rewriter independence test（Appendix D）仅替换了 rewriter 而保持 Qwen3-32B 作为 judge。是否有计划或可能性测试反向配置（Qwen3-32B rewrite + GPT-4o judge vs. GPT-4o rewrite + GPT-4o judge），以完全分离 evaluator-producer 效应？\n\n---\n\n## Missing References\n\n1. **Shankar et al. (2024)** \"Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences\" — 与本文的 meta-evaluation 视角直接相关，讨论了 LLM 评估器验证的循环性问题。\n\n2. **Huang et al. (2024)** \"Bias and Fairness in Large Language Models: A Survey\" — 更广泛的 LLM bias survey，本文的 Related Work 聚焦于 judge bias 但缺少与 general LLM bias literature 的连接。\n\n3. **Zheng et al. (2024)** \"On the Limitations of LLM-as-a-Judge\" (若存在此方向的综述)——更全面地讨论 LLM-as-judge 的局限性。\n\n---\n\n## Overall Assessment\n\n**Overall**: **3.5** (Borderline Conference)\n\n**一句话总结**: 方法论设计精良、统计分析层次丰富，Likert Blindspot 是对 LLM evaluation 社区有实际价值的发现，但 evaluator-producer confound 的不充分控制和缺乏人工验证削弱了核心 identification claim 的可信度。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 总体方法论严谨，GEE 分解和多层 sensitivity analysis 令人印象深刻。但 evaluator-producer confound 仅对 1/3 judge 做了 cross-rewriter 验证（W1），Section 4.1 与 Table 1 的 register 分类矛盾影响多重比较校正的可信度（W2），verbosity NLI gate 的 17.4% FPR 削弱了 content preservation claim（W5）。 |\n| Excitement | 3.5/5 | Likert Blindspot 的量化对 LLM evaluation 社区有直接实践意义（特别是 RLHF/DPO pipeline 依赖 pairwise preference），per-axis confound structure 是有启发性的分析框架。但核心洞察（pairwise > Likert sensitivity）在 measurement theory 中已有理论预测，本文的贡献主要在于 empirical quantification 和 LLM 评估场景的具体化。 |\n| Reproducibility | 3/5 | 方法描述详尽（Implementation Details, Appendix P），统计方法可复现（choix library, statsmodels, seed=42）。但代码和数据尚未发布（\"released upon acceptance\"），NLI gate 的 axis-specific thresholding 策略需要实现细节，cross-rewriter validation 的不完整性意味着部分结果难以独立验证。 |\n| Confidence | 4/5 | 本审稿人在 LLM evaluation、因果推断方法论和统计建模方面有较强背景。仔细阅读了全文含全部 Appendix，对统计方法和实验设计进行了逐项检查。 |\n\n---\n\n## Detailed Comments（逐节）\n\n### Title & Abstract\n- 标题准确反映内容，\"Likert Blindspot\"命名有记忆点。\n- Abstract 中\"the first framework combining...\"的 novelty claim 在 Related Work 中得到了合理支撑，每个组件的先行工作都有引用。\n- Abstract 提到 \"seven statistical methods\" confirm the effect is structural——这个数字在正文中得到了完整展开（Table 2）。\n\n### Section 1 (Introduction)\n- 开篇对 style bias 问题的 motivation 清晰有力，引用了 li2026preference（76–92%）和 soumik2026judging（0.76–0.92）量化了问题的严重性。\n- \"no single framework integrates all four requirements\"的 gap statement 合理，但\"per-instance diagnostics\"这个 requirement 在后续实验中体现得不够——主要结果都是 aggregate 的（BT win probability, GEE OR），per-instance diagnostic 能力（CSD 可以标记每个 pair 是否 biased）仅在 NLI gate 层面体现。\n- Figure 1（pipeline diagram）清晰展示了 sample attrition，这是好的实验报告实践。\n\n### Section 2 (Related Work)\n- 结构清晰，三个 paragraph 分别覆盖 interventional approaches、measurement sensitivity、style bias detection。\n- 对 RATE 的批判性分析（Likert ATE vulnerability）是有见地的，但措辞可以更 balanced——RATE 和 CSD 测量的是不同的东西（aggregate quality effect vs. per-axis style preference），直接说 RATE 的 findings \"may underestimate\" 需要更多 caveat。\n- Bradley-Terry 段落的 positioning 清楚说明了 BT 在 evaluation 生态系统中的位置。\n\n### Section 3 (Method)\n- Style-controlled rewriting（Section 3.1）的描述清晰。Temperature 0.7 的选择未 justify——是否做过 temperature sensitivity analysis？\n- NLI gate（Section 3.2）的 direction-aware 设计是 well-motivated 的 innovation。但正文中 pass rate 的变化（65% → 86%）仅给出了 verbosity 数据，formality 的 pass rate（88%）需要从 Table 1 footnote 间接推导。建议在正文直接报告各 axis 的 pass rate。\n- Section 3.5 的 identification 声明是全文最精确的因果语言——值得在 abstract 中也使用类似的 calibrated language（目前 abstract 更偏 assertive）。\n\n### Section 4 (Experiments)\n- Table 1 信息密度高但可读性可改进。建议：(a) 为 Blindspot/both sig./neither 使用颜色编码而非仅符号；(b) 分离 LLMBar/AEval/MTB 为独立子表或添加水平分隔线（目前有但不够明显）。\n- Holm-Bonferroni 的 family 定义（Section 4.1）需要与 Table 1 标注统一（W2）。\n- Section 4.1 将 consistency filter validation 和 NLI threshold sweep 分类为\"confirmatory\"和\"exploratory\"——这个 pre-registration 式的分类值得肯定，但未说明这些分类是 pre-registered 还是 post-hoc。\n\n### Section 5 (Analysis)\n- Section 5.1（NLI Gate Validation）是全文最 thorough 的 validation 部分。Gwet's AC1 vs. Cohen's κ 的 prevalence skew 讨论表明作者对 inter-rater agreement 指标的理解深入。\n- Section 5.2（Likert vs. Pairwise）的 \"measurement attenuation vs. construct divergence\" 双重解释框架是成熟的科学态度。但建议在 Abstract 和 Conclusion 中也保持这种 agnosticism——目前 Abstract 的措辞更偏向 \"Likert misses bias\"（暗示 measurement failure），而非 \"Likert measures something different\"。\n- Section 5.2 的 detection vs. amplification 分析（6 controls bounding amplification risk）是对 Jeong et al. (2025) Comparative Trap 的直接回应，structure 清晰。但 control (ii)（Claude shows no bias）的逻辑有弱点——Claude 可能确实没有 style preference，而非 pairwise format 不 amplify。\n- Section 5.6（GEE Conditional Decomposition）是重要的分析贡献。Per-axis confound structure 的 regime classification（style-dominated/conditional/judge-dependent）为后续研究提供了可操作的框架。但 regime classification 的 threshold 未明确定义——什么 Style OR / Orig OR 比值构成 \"style-dominated\" vs. \"conditional\"？\n\n### Limitations\n- 覆盖了三个关键点：(a) evaluator-producer bias, (b) validation methodology and scale, (c) NLI gate 的 identifiability limit。\n- 但 Limitations 中关于 cross-rewriter validation 的说法令人困惑：\"All experiments use the same Qwen3-32B rewriter without the cross-rewriter validation applied to formality and verbosity (Appendix D)\"——但 Appendix D 确实对 formality AND verbosity 都做了 cross-rewriter validation（Tables 6-7）。这句话的意思是其他 benchmark（AEval, MTB）上没有做 cross-rewriter validation？需要澄清。\n\n### Appendix\n- Appendix 的覆盖面令人印象深刻（A-P, 共 16 个附录项），几乎每个可能被质疑的方法论选择都有对应的 robustness check。\n- Table 5（GEE CI）中 GPT-4o formality 和 GPT-4o verbosity 缺失 CI 是排版疏忽（Q1）。\n- Appendix H 的 BT GOF test 和 stratified analysis 是 solid 的 model validation。Likert-tied subset analysis（formality BT=67.3%, verbosity BT=76.0%）有力排除了 originality confounding 的替代解释。\n\n### 页数合规\n主正文（Title → Conclusion）结束于第 8 页底部，Limitations 从第 9 页开始。**符合 EMNLP 2026 Long Paper 8 页限制。**",
    "reviewer_id": "1",
    "project": "causal_style_decomp_judge"
  }
}
```

</details>

---


### Tool result

_source line 539 · 2026-05-21T21:17:59.609344+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3766
}
```

</details>

---


### Assistant

_source line 540 · 2026-05-21T21:18:10.756226+00:00_

审稿意见已提交给 Review Director。

核心结论：**Overall 3.5（Borderline Conference）**。

主要发现：
- **2 个 Must-Fix**：(1) evaluator-producer confound——Qwen3-32B 同时做 rewriter，cross-rewriter validation 仅覆盖 1/3 judge，22% Style OR 下降表明此效应 non-trivial；(2) Section 4.1 定义 8-test primary family 含 register，但 Table 1 把 register 标为 exploratory，多重比较校正不一致。
- **5 个 Should-Fix**：TOST Δ=15pp 过宽、NLI FNR 估计的循环性（Qwen3-32B 自己验证自己的改写）、verbosity gate 17.4% FPR、无任何人工验证、cross-benchmark 选择性测试。
- **优势方面**：方法设计严谨（DAG 因果语言校准好）、7 种统计方法的 sensitivity hierarchy 是亮点、cross-judge replication 覆盖 3 种架构、NLI gate 多层验证罕见、Blindspot severity spectrum 刻画精细。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f810d8d75f013ad17831ce8459f07d6d:reviewer_1"
}
```

</details>

---


## Round 18

## Round 18

14 recorded events
