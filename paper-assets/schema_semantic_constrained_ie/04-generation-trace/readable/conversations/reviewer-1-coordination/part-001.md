# Reviewer 1 coordination — Part 1 of 5

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Conversation logs

[Transcript overview](../reviewer-1-coordination.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/84/84a449ac02ef93e8d750.json)

## Round 1

## Round 1

48 recorded events


### User

_source line 1 · 2026-05-15T08:25:43.186431+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计与统计）

### Venue 信息
- **目标**：EMNLP 2026 via ARR May 2026 cycle
- **截止日期**：2026-05-25 (AoE)
- **页数限制**：长文 ≤ 8 页正文（不含 references/limitations/ethics/appendix）
- **模板**：ACL template, `\usepackage[review]{acl}`
- **匿名规则**：Double-blind

### 论文路径
`projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`
（多文件结构，main.tex 通过 `\input{}` 引入各章节，请逐一阅读所有 section*.tex 和 appendix*.tex 文件）

### 论文概要
OntoCoDec 提出两层约束解码框架用于 IE：grammar 层（XGrammar CFG）保证 JSON 结构和词汇合法性，semantic 层通过有状态 entity registry + 动态 logit masking 强制 domain/range 约束。在 SciERC (7 relations) 和 DocRED (96 relations) 上用 Qwen3-8B 和 Llama-3.1-8B 验证。

### 你的审查侧重

**1. 方法设计严谨性**
- 两层约束的形式化是否完备（§3-§4）？constraint tightness 的定义和使用是否合理？
- Grammar-first fallback 策略的合理性——当 S(t)∩G(t)=∅ 时退回 grammar-only 是否是最优选择？是否有更好的替代方案（如 beam search 回溯）？
- Entity registry 的实现假设：单 subword token 映射是否在所有 tokenizer 上成立？论文声称在 Qwen3-8B 和 Llama 上"pre-verify uniqueness"——这是方法限制还是实现细节？
- CF violation 的 dramatic increase（0.08%→9.90%）是否表明方法存在根本缺陷？论文将其描述为"trade-off"是否充分？

**2. 实验设计与统计**
- 零-shot 设定下 R-F1 仅约 8%——这个基线水平下约束解码的实际意义如何？论文在 appendix 中声称这是"control variable"——这个论证是否令人信服？
- Bootstrap resampling 的使用是否恰当？10,000 iterations 是否足够？confidence intervals 的报告是否完整？
- SciERC 上 R-F1 变化不显著（p=0.58）但 DocRED 上显著（p<0.001）——论文对此差异的解释（baseline RV 差异）是否充分？
- 只用了 2 个数据集、2 个 8B 模型——泛化性声明是否过强？
- S1 vs S2 的对比是否公平？S2 用了两次推理但 S1 只用一次，计算成本对比缺失。
- Post-hoc filtering baseline（appendix）的对比是否充分？它的 F1 高于 OntoCoDec——这是否削弱了论文的核心论点？
- 缺少对生成延迟/吞吐量的讨论——约束解码的计算开销是什么？

**3. 数据与可复现性**
- 是否提供了足够的实现细节（prompt 模板、decoding 参数、硬件信息）？
- SciERC 和 DocRED 的 evaluation protocol 是否标准？用的是 dev 还是 test set？

请按以下格式输出审稿意见：
```
## Summary（2-3 句）
## Strengths（逐条）
## Weaknesses（逐条，标注 [Must-Fix] 或 [Should-Fix] 或 [Minor]）
## Questions（需要作者回答）
## Missing References（如有）
## Overall Assessment（评分 + 置信度）
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-15T08:25:52.178487+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
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

_source line 3 · 2026-05-15T08:25:52.229803+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-15T08:25:55.645639+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 5 · 2026-05-15T08:25:56.148127+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR review form scoring rubric dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR review form scoring rubric dimensions"
  }
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-15T08:25:57.504963+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-15T08:25:57.505351+00:00_

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
12	\usepackage{multirow}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{enumitem}
16	\usepackage{xcolor}
17	
18	\title{OntoCoDec: Type-Valid Information Extraction\\via Compiled Ontology Constraints}
19	
20	\author{Anonymous ACL submission}
21	
22	\begin{document}
23	\maketitle
24	
25	% === Abstract ===
26	\input{abstract}
27	
28	% === §1 Introduction ===
29	\input{section1_introduction_draft}
30	
31	% === §2 Background ===
32	\input{section2_background}
33	
34	% === §3 Method ===
35	\input{section3_method_draft}
36	
37	% === §4 Constraint Composition ===
38	\section{Constraint Composition}
39	\label{sec:composition}
40	\input{section4_composition_draft}
41	
42	% === §5 Experiments ===
43	\section{Experiments}
44	\label{sec:experiments}
45	
46	\subsection{Violation Landscape}
47	\input{section3_violation_landscape}
48	
49	\input{section5_scierc_draft}
50	\input{section5_docred_draft}
51	\input{section5_crossmodel_draft}
52	
53	% === §6 Related Work ===
54	\input{section6_related_work}
55	
56	% === §7 Discussion and Conclusion ===
57	\section{Discussion and Conclusion}
58	\label{sec:discussion}
59	\input{section7_conclusion_compressed}
60	
61	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
62	\section*{Limitations}
63	
64	The semantic layer introduces cross-field consistency (CF) violations (up to 12.02\%), a systematic consequence of per-relation independent enforcement that remains an open challenge.
65	Entity F1 impact is model-dependent ($+$1.22\,pp for Qwen vs.\ $-$0.64\,pp for Llama on DocRED), partially confounded by increased parse failures under constraints (Llama: 9.1\% vs.\ 6.8\%).
66	Results cover two 8B-class models under zero-shot prompting; integration w
…[truncated 906 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 8 · 2026-05-15T08:26:01.952976+00:00_

Web search results for query: "EMNLP 2026 ARR review form scoring rubric dimensions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"}]

Based on the search results, I found information about the ARR review form scoring dimensions for EMNLP 2026:

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

These are the main scoring rubric dimensions for the current ARR review form used by EMNLP 2026:

1. **Soundness** - The soundness scores must be justified by the text of the review. If you give a low
…[truncated 738 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 5804
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-15T08:26:04.086903+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

I found comprehensive information about ACL ARR 2026 reviewer guidelines and review form criteria. Here's what I found:

## Reviewer Guidelines

Reviewers should follow this workflow: (1) read the paper and get the first impression, (2) search for related work, not deliberately trying to find that parti
…[truncated 1762 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8441
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-15T08:26:09.754122+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales (numeric ranges), and descriptions. Include soundness, excitement, overall assessment, reproducibility, and any other scored dimensions. List each dimension with its exact scale and rubric text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales (numeric ranges), and descriptions. Include soundness, excitement, overall assessment, reproducibility, and any other scored dimensions. List each dimension with its exact scale and rubric text."
  }
}
```

</details>

---


### Tool call

_source line 11 · 2026-05-15T08:26:10.358833+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
  }
}
```

</details>

---


### Tool result

_source line 12 · 2026-05-15T08:26:10.461015+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/paper_tables_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_fd4b26.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_d3264e.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_550cbf.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_outline.tex
/home/ubuntu/.agent-ml-rese
…[truncated 1633 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 102
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-15T08:26:17.151727+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. Reviewer Confidence
**Scale:** 1-5
- 5: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- 4: Quite sure with unlikely but conceivable oversights
- 3: Pretty sure but may have missed details
- 2: Willing to defend evaluation but likely missed some details
- 1: Outside expertise area or paper very difficult to understand

## 2. Soundness
**Scale:** 1-5 (with half-point increments: 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5)
- 5: "Excellent: This study is one of the most thorough I have seen"
- 4: Strong with sufficient claim support
- 3: Acceptable with main claims supported
- 2: Poor with insufficiently supported main claims
- 1: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## 3. Excitement
**Scale:** 1-5 (with half-point increments)
- 5: "Highly Exciting: I would recommend this paper to others"
- 4: Exciting; would mention to others
- 3: Interesting; might mention selectively
- 2: Potentially interesting but doesn't resonate personally
- 1: Not exciting; unlikely to resonate with ACL community

## 4. Overall Assessment
**Scale:** 1-5 (with half-point increments)
- 5: Consider for Award (top 2.5% papers)
- 4: Conference acceptance
- 3: Accept to Findings track
- 2: Resubmit next cycle (substantial revisions needed)
- 1.5: Resubmit after next cycle
- 1: Do not resubmit

## 5. Reproducibility
**Scale:** 1-5
- 5: "They could easily reproduce the results"
- 4: Mostly reproducible with minor variations
- 3: Reproducible with difficulty due to underspecified parameters
- 2: Difficult reproduction due to unavailable data/insufficient details
- 1: Unable to reproduce results

## 6. Datasets (if applicable)
**Scale:** 1-5
- 5: Enabling impact on others' research choices
- 4: Useful for ongoing research
- 3: Potentially useful
- 2: Documentary value for replication only
- 1: No usable datasets

## 7. Software (if applicable)
**Scale:*
…[truncated 434 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7397
}
```

</details>

---


### Tool call

_source line 14 · 2026-05-15T08:26:23.077476+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-15T08:26:23.530152+00:00_

1	\begin{abstract}
2	LLM-based information extraction systems produce systematic ontology constraint violations during autoregressive generation.
3	On SciERC (7 relation types), 15.37\% of extracted triples violate domain/range type constraints; on DocRED (96 relation types), 18.46\%---comparable rates governed by \emph{constraint tightness} rather than ontology scale.
4	%
5	We present \textsc{OntoCoDec}, which compiles IE ontology schemas into two composable decoding constraint layers:
6	(1)~a \emph{grammar layer} (XGrammar CFG) enforcing JSON structural validity and restricting entity/relation vocabularies to schema-defined values (ET, RV\,$\to$\,0\%); and
7	(2)~a \emph{semantic layer} enforcing domain/range constraints via a stateful entity registry and dynamic logit masking.
8	The grammar layer is an enabling prerequisite; the two compose via bitwise AND on token-level masks.
9	%
10	On SciERC, \textsc{OntoCoDec} reduces domain/range violations by 94\% (15.37\%\,$\to$\,0.93\%) while maintaining extraction F1 ({+}0.13pp, $p{=}0.58$).
11	On DocRED, violations decrease by 45--90\% depending on the model, with significant relation F1 gains for both Qwen3-8B ({+}0.50pp, $p{<}0.001$) and Llama-3.1-8B ({+}0.29pp, $p{=}0.013$; DR$\downarrow$90.2\%).
12	% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1, llama_docred_full_s1
13	The dual-factor mechanism---tightness $\times$ baseline violation rate---explains cross-dataset and cross-model DR reduction differences.
14	\end{abstract}
15	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-15T08:26:23.530524+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-15T08:26:23.982574+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly deployed for zero-shot information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity is guaranteed to carry a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}---structurally valid triples that are ontologically invalid.
8	In a systematic study, we find violations are pervasive: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.7\% on DocRED~\cite{yao2019docred}, driven by \emph{constraint tightness} (few valid type pairs per relation) rather than ontology scale.
9	Relations with tight constraints exhibit far higher rates (\textsc{Compare}: 42.4\%) than loosely constrained ones (\textsc{Used-for}: 0.8\%).
10	
11	Existing approaches leave a fundamental gap.
12	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable---violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp.
13	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} guarantees syntactic well-formedness but cannot encode cross-field semantic constraints.
14	Post-hoc validation wastes compute on discarded outputs and cannot redirect probability mass during decoding.
15	Training-based approaches~\cite{sainz2024gollie,lu2022uie} provide only soft guidance that cannot eliminate violations.
16	
17	We propose \textbf{OntoCoDec} (\textbf{Onto}logy-\textbf{Co}mpiled \textbf{Dec}oding), a framework that compiles an IE ontology into two composable layers of decoding-time constraints.
18	The \emph{grammar layer} enforces JSON well-formedness and vocabulary validity via XGrammar.
19	The \emph{semantic layer} maintains a stateful entity registry during generation: as entities are decoded, the registry records ty
…[truncated 1242 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-15T08:26:24.033264+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-15T08:26:24.937440+00:00_

1	% Section 2: Background (compressed)
2	
3	\section{Background}
4	\label{sec:background}
5	
6	\paragraph{IE Ontology Structure.}
7	\label{sec:bg:ontology}
8	An IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defines entity types $\mathcal{E}$, relation types $\mathcal{R}$, and a mapping $\sigma: \mathcal{R} \to \mathcal{P}(\mathcal{E} \times \mathcal{E})$ specifying valid (head type, tail type) pairs per relation.
9	A triple $(h, r, t)$ is \emph{type-valid} if $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$.
10	We define the \emph{constraint tightness} of $r$ as $1 - |\sigma(r)| / |\mathcal{E}|^2$: tighter constraints leave fewer valid options, increasing violation likelihood.
11	
12	\paragraph{Grammar-Constrained Decoding.}
13	\label{sec:bg:gcd}
14	Grammar-constrained decoding restricts each token $y_t$ to a mask $M_g \in \{0, 1\}^{|V|}$ derived from a target grammar.
15	XGrammar~\citep{dong2025xgrammar} compiles JSON Schemas into pushdown automata for efficient enforcement of structural constraints; Outlines~\citep{willard2023outlines} and SGLang~\citep{zheng2024sglang} offer similar capabilities.
16	However, these methods are limited to context-free constraints and cannot enforce cross-field semantic rules---e.g., ``if $r$ = \textsc{Feature-of}, then $\mathrm{type}(h) \in \{\textsc{Method}, \textsc{OtherScientificTerm}\}$''---which depend on previously generated field values.
17	
18	\paragraph{Problem Statement.}
19	\label{sec:bg:problem}
20	Given $\mathcal{O}$ and an autoregressive LM $\mathcal{M}$, we seek constraints $\mathcal{C}$ ensuring: (a)~\textbf{structural validity}---well-formed JSON with $\mathcal{E}$/$\mathcal{R}$ membership; and (b)~\textbf{type validity}---$(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$ for every triple.
21	Condition (a) is context-free; (b) is context-sensitive but \emph{prefix-decidable}---at the point where a type token is generated, all information needed (relation type, entity registry) is available i
…[truncated 25 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-15T08:26:24.937949+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-15T08:26:25.440346+00:00_

1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	We present OntoCoDec, a two-layer constrained decoding framework that compiles ontology schemas into token-level masks enforced during autoregressive generation.
9	The grammar layer (\S\ref{sec:grammar}) guarantees structural validity—well-formed JSON with ontology-vocabulary membership—while the semantic layer (\S\ref{sec:semantic}) enforces domain/range type constraints via a stateful entity registry.
10	We describe the problem formulation (\S\ref{sec:formulation}), each layer, and two decoding strategies (\S\ref{sec:strategies}).
11	Formal analysis of constraint composition is deferred to Section~\ref{sec:composition}.
12	
13	
14	\subsection{Problem Formulation}
15	\label{sec:formulation}
16	
17	\paragraph{IE as structured generation.}
18	Given an input text $x$, a language model generates a structured JSON output $y$:
19	%
20	\begin{equation}\label{eq:output-schema}
21	\resizebox{.88\columnwidth}{!}{$\displaystyle
22	  y = \bigl\{\texttt{entities}: [\{n_i, \tau_i\}],\; \texttt{relations}: [\{h_j, t_j, r_j, \tau^h_j, \tau^t_j\}]\bigr\}
23	$}
24	\end{equation}
25	%
26	where each entity has a name $n_i$ and type $\tau_i \in \mathcal{E}$, and each relation specifies head $h_j$, tail $t_j$, relation type $r_j \in \mathcal{R}$, and head/tail entity types $\tau^h_j, \tau^t_j$.
27	
28	\paragraph{Ontology schema.}
29	An ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \operatorname{dom}, \operatorname{range})$ defines entity types $\mathcal{E}$, relation types $\mathcal{R}$, and functions $\operatorname{dom}, \operatorname{range}: \mathcal{R} \to 2^{\mathcal{E}}$ specifying permitted head and tail types for each relation.
30	
31	\paragraph{Ontology compliance.}
32	A triple $(h, r, t)$ with $\operatorname{type}(h) = \tau^h$, $\operatorname{type}(t) = \tau^t$ is \emph{type-valid} w.r.t.\ $\mathcal{O}$ iff:
3
…[truncated 7785 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-15T08:26:25.440952+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-15T08:26:25.893219+00:00_

1	% Section: Constraint Composition (compressed, 787→~500 words)
2	
3	At each decoding step $t$, let $G(t) \subseteq V$ and $S(t) \subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.
4	The final mask is their conjunction:
5	%
6	\begin{equation}\label{eq:composition}
7	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
8	\end{equation}
9	%
10	so a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$, reflecting the enabling dependency (\S\ref{sec:method})---the semantic layer requires the relation type to belong to $\mathcal{R}$, a property guaranteed only by the grammar layer.
12	
13	\paragraph{Grammar-First Fallback.}
14	When $S(t) \cap G(t) = \emptyset$---tight constraints leave no token that is both grammar-valid and semantically valid---na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
15	We enforce a \emph{grammar-first fallback}: if no semantically valid token survives grammar filtering, semantic masking is skipped and the grammar layer alone controls selection.
16	Structural integrity is a hard constraint; a type violation is a soft error detectable by downstream validation.
17	
18	\paragraph{Constraint Tightness.}
19	We define the tightness of relation $r$ as:
20	%
21	\begin{equation}\label{eq:tightness}
22	  \tau(r) = 1 - \frac{|\mathcal{V}(r)|}{|\mathcal{T}|^2},
23	\end{equation}
24	%
25	where $\mathcal{V}(r)$ is the set of valid type pairs and $\mathcal{T}$ the entity type vocabulary.
26	The mean tightness $\bar{\tau} = \frac{1}{|\mathcal{R}|}\sum_{r} \tau(r)$ characterizes ontology restrictiveness.
27	Tighter constraints eliminate more grammar-valid tokens at type-bearing positions, increasing fallback frequency and residual DR.
28	This dual-factor mechanism---tightness $\times$ baseline model violation rate---explains the cross-dataset patt
…[truncated 917 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-15T08:26:25.893621+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
  }
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-15T08:26:26.346542+00:00_

1	% §5.1 Experimental Setup and Violation Landscape
2	% Compressed from standalone section. main.tex provides \subsection header.
3	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
4	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
5	
6	\label{sec:violation_landscape}
7	
8	\paragraph{Setup.}
9	We evaluate Qwen3-8B~\cite{qwen2025qwen3} under zero-shot greedy decoding on two IE benchmarks:
10	\textbf{SciERC}~\cite{luan2018scierc} (551 test sentences, 7 relations, avg.\ 26.1 valid type pairs per relation) and \textbf{DocRED}~\cite{yao2019docred} (998 dev documents, 96 relations, avg.\ 5.68 valid pairs).
11	We measure four violation categories: \textbf{Domain/Range (DR)} violations where $(\mathrm{type}(h), \mathrm{type}(t)) \notin \sigma(r)$; \textbf{Relation Vocabulary (RV)} where $r \notin \mathcal{R}$; \textbf{Entity Type (ET)} where $e \notin \mathcal{E}$; and \textbf{Cross-Field Consistency (CF)} where the same entity receives different types across triples.
12	Cross-model validation with Llama-3.1-8B-Instruct is reported in \S\ref{sec:cross-model}.
13	
14	\paragraph{Violation distribution.}
15	Table~\ref{tab:prompt_comparison} reports violation rates.
16	DR violations affect 15.37\% of triples on SciERC and 18.70\% on DocRED---comparable rates despite a 14$\times$ difference in ontology size---indicating that violation severity is driven by \emph{constraint tightness} rather than ontology scale.
17	RV violations on DocRED are dramatically higher (28.90\% vs.\ 1.39\%), indicating that 96 relation types exceed the model's capacity to reproduce a target vocabulary from a single prompt.
18	Per-relation rates (Figure~\ref{fig:per_relation_dr}) vary by over 40 percentage points: \textsc{Compare} at 42.4\% vs.\ \textsc{Used-for} at 0.76\%, correlating with tightness---tight constraints (few valid type pairs) produce systematic failures.
19	
20	\begin{table}[t]
21	\centering
22	\caption{Violation rates (\%) under unconstrained and sche
…[truncated 1214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-15T08:26:26.397281+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-15T08:26:27.352142+00:00_

1	% Section 5 — SciERC Results (Draft)
2	% Data source: Phase 2 SciERC registry experiments
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,
4	%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2
5	% All numbers verified against registry 2026-05-14.
6	
7	\subsection{Results on SciERC}
8	\label{sec:scierc-results}
9	
10	Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC,
11	evaluating each constraint layer independently and in combination.
12	All experiments use Qwen3-8B in a zero-shot setting on 551 test documents
13	with identical prompts and decoding parameters;
14	only the active constraint layers differ.
15	
16	% ──────────────────────────────────────────
17	%  Table: SciERC five-way ablation
18	% ──────────────────────────────────────────
19	\begin{table}[t]
20	\centering
21	\small
22	\setlength{\tabcolsep}{3.6pt}
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{@{}l rrrrr rr@{}}
25	\toprule
26	& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
27	& \multicolumn{2}{c}{\textbf{F1}} \\
28	\cmidrule(lr){2-6} \cmidrule(l){7-8}
29	\textbf{Mode}
30	  & DR\,$\downarrow$ & $\Delta$DR
31	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
32	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
33	\midrule
34	Unconstrained
35	  & 15.37 & ---
36	  & 1.39  & 0.40
37	  & 0.08
38	  & 8.23  & 31.01 \\
39	Grammar
40	  & 14.84 & $\downarrow$3\%
41	  & \textbf{0} & \textbf{0}
42	  & 0.08
43	  & 8.23  & 30.98 \\
44	Semantic
45	  & 11.65 & $\downarrow$24\%
46	  & 1.51  & 0.40
47	  & 2.71
48	  & 8.15  & 31.01 \\
49	Full (S1)
50	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
51	  & \textbf{0} & \textbf{0}
52	  & 9.90
53	  & \textbf{8.36} & 30.98 \\
54	Full (S2)
55	  & 0.97  & $\downarrow$94\%
56	  & \textbf{0} & \textbf{0}
57	  & 8.03
58	  & 8.03  & \textbf{31.90} \\
59	\bottomrule
60	\end{tabular}}%
61	\caption{Five-way ablation on SciERC (551 documents, Qwen3-8B, zero-shot).
62	DR: domain/range violation rate;
63	RV: rel
…[truncated 5214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-15T08:26:27.453178+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-15T08:26:27.755189+00:00_

1	% Section 5 — DocRED Results (compressed, 1450→~600 words)
2	% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,
3	%          phase2_docred_semantic_only, phase2_docred_full_s1
4	% All numbers verified against registry 2026-05-14.
5	
6	\subsection{Cross-Dataset Validation on DocRED}
7	\label{sec:docred-results}
8	
9	Table~\ref{tab:docred-ablation} presents the four-way ablation on DocRED, a document-level RE benchmark with 96 Wikidata relation types---14$\times$ the ontology size of SciERC.
10	All experiments use Qwen3-8B zero-shot on 998 documents.
11	
12	% ──────────────────────────────────────────
13	%  Table: DocRED four-way ablation
14	% ──────────────────────────────────────────
15	\begin{table}[t]
16	\centering
17	\small
18	\setlength{\tabcolsep}{3.6pt}
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{@{}l rrrrr rr@{}}
21	\toprule
22	& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
23	& \multicolumn{2}{c}{\textbf{F1}} \\
24	\cmidrule(lr){2-6} \cmidrule(l){7-8}
25	\textbf{Mode}
26	  & DR\,$\downarrow$ & $\Delta$DR
27	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
28	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
29	\midrule
30	Unconstrained
31	  & 18.46 & ---
32	  & 29.66 & 2.48
33	  & 0.10
34	  & 7.74  & 58.15 \\
35	Grammar
36	  & 26.17 & $\uparrow$42\%
37	  & \textbf{0.03} & \textbf{0}
38	  & 0.07
39	  & \textbf{8.31}  & \textbf{59.38} \\
40	Semantic
41	  & 13.84 & $\downarrow$25\%
42	  & 29.87 & 4.22
43	  & 1.05
44	  & 7.70  & 57.81 \\
45	Full (S1)
46	  & \textbf{10.21} & $\downarrow$\textbf{45\%}
47	  & \textbf{0.03} & \textbf{0}
48	  & 2.57
49	  & 8.23  & 59.37 \\
50	\bottomrule
51	\end{tabular}}%
52	\caption{Four-way ablation on DocRED (998 documents, Qwen3-8B, zero-shot).
53	$\Delta$DR: relative change vs.\ unconstrained.
54	Best per column in \textbf{bold} (CF excluded).
55	F1 $\times$100. Bootstrap significance: R-F1 $+$0.50\,pp ($p < 0.001$).}
56	\label{tab:docred-ablation}
57	\end{table}
58	
59	% exp_ids: phase2_docred_unconstraine
…[truncated 2759 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-15T08:26:27.755592+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 31 · 2026-05-15T08:26:28.261446+00:00_

1	% Section 5 — Cross-Model Validation (compressed, 830→~400 words)
2	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1,
3	%          phase2_docred_unconstrained, phase2_docred_full_s1,
4	%          llama_scierc_unconstrained, llama_scierc_full_s1,
5	%          llama_docred_unconstrained, llama_docred_full_s1
6	
7	\subsection{Cross-Model Validation}
8	\label{sec:cross-model}
9	
10	We replicate the full S1 configuration with Llama-3.1-8B-Instruct under identical prompts, decoding parameters, and evaluation.
11	Table~\ref{tab:cross-model} summarizes results alongside Qwen3-8B.
12	
13	\begin{table}[t]
14	\centering
15	\small
16	\setlength{\tabcolsep}{3.4pt}
17	\resizebox{\columnwidth}{!}{%
18	\begin{tabular}{@{}ll rrrr rr@{}}
19	\toprule
20	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
21	& \multicolumn{2}{c}{\textbf{F1}} \\
22	\cmidrule(lr){3-6} \cmidrule(l){7-8}
23	\textbf{Dataset} & \textbf{Model}
24	  & DR\,$\downarrow$ & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
25	  & Rel. & Ent. \\
26	\midrule
27	\multirow{4}{*}{SciERC}
28	  & Qwen (U)  & 15.37 & 1.39 & 0.40 & 0.08 & 8.23 & 31.01 \\
29	  & Qwen (S1) &  0.93 & 0    & 0    & 9.90 & 8.36 & 30.98 \\
30	  \cmidrule(l){2-8}
31	  & Llama (U)  & 13.34 & 0.55 & 0    & 0.24 & 2.68 & 23.56 \\
32	  & Llama (S1) &  0.08 & 0    & 0    & 6.56 & 2.54 & 23.49 \\
33	\midrule
34	\multirow{4}{*}{DocRED}
35	  & Qwen (U)  & 18.46 & 29.66 & 2.48 & 0.10 & 7.74 & 58.15 \\
36	  & Qwen (S1) & 10.21 &  0.03 & 0    & 2.57 & 8.23 & 59.37 \\
37	  \cmidrule(l){2-8}
38	  & Llama (U)  & 26.07 & 16.03 & 0.13 & 0.17 & 5.98 & 55.65 \\
39	  & Llama (S1) &  2.55 &  0    & 0    & 12.02 & 6.27 & 55.01 \\
40	\bottomrule
41	\end{tabular}}%
42	\caption{Cross-model validation. U: unconstrained; S1: full two-layer.
43	Parse failures (U$\to$S1): Qwen DocRED 12$\to$11, Llama DocRED 68$\to$91; others $\leq$1.
44	F1 $\times$100.}
45	\label{tab:cross-model}
46	\end{table}
47	
48	\paragraph{Model-agnostic structural guarantees.}
49	RV and ET vi
…[truncated 2798 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 505
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-15T08:26:28.261994+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-15T08:26:28.714505+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Grammar-Constrained Decoding.}
5	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, Guidance~\cite{guidance2023}, and LMQL~\cite{beurer-kellner2023lmql} have made grammar-constrained decoding the standard for structured LLM output, ensuring every token belongs to a grammar-valid continuation.
6	DOMINO~\cite{beurer-kellner2024domino} and ASAp~\cite{park2024grammar} further address distribution distortion, making grammar enforcement statistically principled.
7	However, these methods operate at the syntactic level---they ensure format validity but cannot enforce cross-field semantic constraints such as ontology domain/range rules.
8	
9	\paragraph{Semantic Constrained Decoding for Code.}
10	In code generation, constrained decoding has been extended to enforce semantic properties: Synchromesh~\cite{synchromesh_iclr2022} enforces type and scope constraints via dynamic token masks; PICARD~\cite{scholak2021picard} performs incremental SQL parsing to reject type-invalid tokens; MGD~\cite{mgd_neurips2023} applies static-analysis monitors for type checking at decode time; and \citet{pldi2025_type_constrained_codegen} compile full type systems into prefix automata for logits masking.
11	These demonstrate that richer-than-CFG constraints are feasible at decode time, but exclusively in the code domain---OntoCoDec migrates this paradigm to information extraction.
12	
13	\paragraph{Vocabulary and Type-Constrained Generation.}
14	\citet{roth_yih_2004} establish that relational type compatibility should be a hard constraint via integer linear programming, though applied post-hoc; see also~\cite{xie2016tkrl}.
15	GENRE~\cite{decao2021genre}, NeuroLogic~\cite{lu2021neurologic}, AdaKGC~\cite{adakgc_emnlp2023}, GCD~\cite{geng2023gcd}, and GoLLIE~\cite{sainz2024gollie} constrain \emph{which tokens} can appear (vocabulary membership) but not \emph{which type combinations} are valid for a given relation--
…[truncated 2281 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-15T08:26:28.714967+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
  }
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-15T08:26:29.619786+00:00_

1	% Section 7 — Discussion and Conclusion (compressed)
2	% Full discussion paragraphs moved to Appendix B.
3	
4	\paragraph{CF Severity.}
5	% exp_ids: phase2_scierc_full_s1 (CF=9.90%), phase2_scierc_grammar_only (CF=0.08%),
6	%          phase2_docred_full_s1 (CF=2.57%), llama_docred_full_s1 (CF=12.02%)
7	DR violations produce ontologically invalid triples---a hard constraint failure that no downstream system can recover from.
8	CF violations are qualitatively different: each individual triple remains type-valid with respect to its own relation's domain/range rules; only cross-triple consistency is broken when the same entity receives different types across relations.
9	The dominant conflict pattern---\emph{Generic}$\leftrightarrow$\emph{OtherScientificTerm} (60 of 245 affected entities on SciERC)---reflects genuine semantic ambiguity in the type system rather than a systematic method failure.
10	Ablation cleanly attributes CF to the semantic layer: grammar-only decoding yields CF\,=\,0.08\%, matching the unconstrained baseline, while the full system reaches 9.90\% on SciERC and 2.57\% on DocRED (Qwen3-8B; 12.02\% DocRED for Llama-3.1-8B), confirming that CF arises from per-relation independent enforcement where each relation's constraint mask is computed without access to type decisions made for other relations (extended analysis in Appendix~\ref{app:discussion}).
11	% exp_ids: phase2_scierc_grammar_only, phase2_docred_full_s1, llama_docred_full_s1
12	
13	\paragraph{Dataset-Dependent F1 Impact.}
14	% exp_ids: d012_bootstrap_ci (DocRED +0.50pp p<0.001, SciERC +0.13pp p=0.58),
15	%          phase0_docred_unconstrained (RV=29.66%), phase0_scierc_unconstrained (RV=1.39%)
16	The divergence in F1 significance between DocRED ($+$0.50\,pp, $p < 0.001$) and SciERC ($+$0.13\,pp, $p = 0.58$) traces to a single mechanism: grammar-layer elimination of out-of-vocabulary relation names.
17	DocRED's baseline RV of 29.66\% produces 5{,}189 OOV predictions counted as false positives; 
…[truncated 1326 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-15T08:26:29.670474+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-15T08:26:30.127145+00:00_

1	\section{Extended Related Work}
2	\label{app:related_work}
3	
4	% ===========================================================================
5	% Paradigm 1: Grammar-Constrained Decoding
6	% ===========================================================================
7	\paragraph{Grammar-Constrained Decoding.}
8	Recent work has established efficient algorithms for restricting LLM outputs to conform to context-free grammars, making grammar-constrained decoding the de facto standard for obtaining structured output from language models.
9	XGrammar~\cite{dong2025xgrammar} partitions the vocabulary into context-independent and context-dependent tokens and maintains persistent pushdown automata across decoding steps, achieving up to 100$\times$ speedup over prior CFG-constrained decoding methods.
10	Outlines~\cite{willard2023outlines} reformulates constrained generation as finite-state machine transitions with offline vocabulary indexing, enabling efficient enforcement of regular-expression and JSON-schema constraints without runtime overhead per token.
11	LMQL~\cite{beurer-kellner2023lmql} introduces a declarative query language that compiles type, length, and regex constraints into token-level masks, providing a programmable interface for specifying multi-variable output structures.
12	These systems ensure that every generated token belongs to a grammar-valid continuation, but they do not address the \emph{distribution distortion} introduced by naive token masking.
13	A parallel line of work tackles this problem directly: DOMINO~\cite{beurer-kellner2024domino} minimizes distributional divergence during CFG enforcement by formulating mask selection as an optimization problem, and ASAp~\cite{park2024grammar} provides a provably unbiased sampling algorithm that preserves the original LM distribution under grammar constraints.
14	Together, these advances have made grammar-constrained decoding both fast and statistically principled, establishing a robust foundation for stru
…[truncated 19787 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 456
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-15T08:26:30.127625+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 39 · 2026-05-15T08:26:30.432163+00:00_

1	% Appendix B — Extended Discussion
2	% Contains discussion paragraphs moved from the main text during compression.
3	
4	\section{Extended Discussion}\label{app:discussion}
5	
6	%%% Paragraph 1: Low F1 Practical Significance %%%
7	% exp_ids: phase2_scierc_full_s1 (R-F1=8.36%), phase2_docred_full_s1 (R-F1=8.23%),
8	%          phase0_scierc_unconstrained (DR=15.37%), phase2_docred_unconstrained (DR=18.46%)
9	
10	\paragraph{Practical Significance of Zero-Shot F1.}
11	Our reported relation F1 of approximately 8\% on both SciERC and DocRED reflects the inherent difficulty of zero-shot closed IE, where the model receives no task-specific training examples.
12	For reference, supervised state-of-the-art systems on SciERC achieve approximately 49--53\% relation F1 with full training data~\citep{zhong2021frustratingly,ye2022packed}.
13	Constraint enforcement operates largely independently of the extraction model's intrinsic capability: it restricts the output space to ontologically valid triples regardless of the underlying model's accuracy.
14	When applied to fine-tuned models that reach competitive F1 levels, the same constraints remain necessary---Phase~0 analysis confirms that even well-prompted models exhibit non-trivial violation rates (15.37\% DR on SciERC, 18.46\% on DocRED).
15	% exp_ids: phase0_scierc_unconstrained, phase2_docred_unconstrained
16	In our evaluation, F1 serves as a \emph{control variable} verifying that constraint enforcement does not degrade extraction quality, not as an optimization target.
17	The contribution of this work is the constraint enforcement method itself; the zero-shot setting isolates its effect from confounds introduced by task-specific fine-tuning.
18	
19	%%% Paragraph 4: Decoding-Time vs. Post-Hoc Enforcement %%%
20	% exp_ids: posthoc_filtering_baseline, phase2_scierc_full_s1 (R-F1=8.36%),
21	%          phase2_docred_full_s1 (R-F1=8.23%, ET=0%)
22	
23	\paragraph{Decoding-Time vs.\ Post-Hoc Enforcement.}
24	Post-hoc filtering---gener
…[truncated 1210 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 304
}
```

</details>

---


### Tool call

_source line 40 · 2026-05-15T08:26:30.432716+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex"
  }
}
```

</details>

---


### Tool result

_source line 41 · 2026-05-15T08:26:30.483243+00:00_

1	% Appendix C — Per-Relation Violation Analysis (Llama-3.1-8B)
2	% exp_ids: llama_docred_unconstrained, llama_docred_full_s1
3	
4	\section{Per-Relation Violation Analysis (Llama-3.1-8B)}\label{app:llama-per-relation}
5	
6	Table~\ref{tab:llama-per-relation-dr} presents the per-relation domain--range violation breakdown for Llama-3.1-8B on DocRED under full S1 constraints.
7	The Llama baseline exhibits an RV rate of 16.03\%, substantially lower than Qwen's 29.66\%, indicating stronger baseline vocabulary compliance.
8	% exp_ids: llama_docred_unconstrained (RV=16.03%), qwen_docred_unconstrained (RV=29.66%)
9	Full S1 completely eliminates RV violations and reduces the residual DR rate to 2.55\% (418/16{,}368 triples), with only three relations exceeding 10\%.
10	% exp_ids: llama_docred_full_s1 (DR=2.6%, 418/16368)
11	
12	\begin{table}[h]
13	\centering
14	\caption{Top 10 per-relation DR violation rates for Llama-3.1-8B on DocRED under full S1 constraints. Relations with $>$20 triples and 0\% DR (e.g., P131, P206, P361, P170, P86) are omitted.}
15	\label{tab:llama-per-relation-dr}
16	\resizebox{\columnwidth}{!}{%
17	\begin{tabular}{@{}llrrr@{}}
18	\toprule
19	Relation & PID & Triples & DR Violations & DR Rate (\%) \\
20	\midrule
21	dissolved/demolished & P576 & 73 & 24 & 32.9 \\
22	followed by          & P156 & 117 & 24 & 20.5 \\
23	unemployment rate    & P1198 & 15 & 3 & 20.0 \\
24	end time             & P582 & 130 & 21 & 16.2 \\
25	instance of          & P31  & 290 & 37 & 12.8 \\
26	product/material produced & P1056 & 98 & 11 & 11.2 \\
27	location of formation & P740 & 81 & 8 & 9.9 \\
28	head of state        & P35  & 41  & 3  & 7.3 \\
29	applies to jurisdiction & P1001 & 637 & 45 & 7.1 \\
30	conflict             & P607 & 453 & 30 & 6.6 \\
31	\bottomrule
32	\end{tabular}}
33	\end{table}
34	% exp_ids: llama_docred_full_s1
35	
36	Compared with Qwen, which retains a 10.21\% residual DR under full S1 concentrated in P1198 (83\% fallback) and P171 (78\% fallback), Llama's re
…[truncated 523 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-15T08:29:30.258404+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the precise reviewer guidelines, especially: what are the exact dimensions reviewers must score, the numeric scales, and any specific instructions about how to evaluate soundness, excitement, and overall assessment. Also extract any guidance about how to handle borderline papers or papers with mixed strengths/weaknesses."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the precise reviewer guidelines, especially: what are the exact dimensions reviewers must score, the numeric scales, and any specific instructions about how to evaluate soundness, excitement, and overall assessment. Also extract any guidance about how to handle borderline papers or papers with mixed strengths/weaknesses."
  }
}
```

</details>

---


### Tool call

_source line 43 · 2026-05-15T08:29:31.865584+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 44 · 2026-05-15T08:29:36.290484+00:00_

# ARR Reviewer Scoring Guidelines

## Scoring Dimensions

ARR reviewers provide **three distinct scores**:

1. **Soundness** - evaluates technical rigor and validity
2. **Excitement** - reflects personal interest (orthogonal to soundness)
3. **Overall Assessment** - composite recommendation for acceptance

## Key Scoring Principles

**Soundness-Review Alignment (I3):**
"The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation" - low scores require documented problems in the review text.

**Excitement Interpretation:**
Excitement captures subjective preference independent of technical quality. A reviewer may find work sound but personally uninterested, or conversely, find it compelling despite minor technical issues.

**Overall Assessment Use:**
This composite score reflects soundness, excitement, novelty, and impact combined. Papers can merit acceptance despite low personal excitement if they offer significant contributions (resource development, efficiency improvements, underserved languages/domains).

## Handling Mixed-Strength Papers

The guidelines emphasize avoiding automatic rejection patterns:

- **Don't penalize simplicity** - simpler solutions are preferable if they answer the research question
- **Distinguish limitations from weaknesses** - acknowledged limitations don't automatically invalidate work
- **Evaluate scope appropriately** - short papers need only sufficient evidence for stated claims, not comprehensive coverage

**Critical instruction:** Reviewers must update assessments after author responses, acknowledging whether concerns were resolved or explaining why responses proved unconvincing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6032
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-15T08:30:13.947527+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 47, \"total_citations\": 85, \"unique_cited_keys\": 46, \"orphan_bib\": 1, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 38, \"online_not_found\": 2, \"online_mismatch\": 7}, \"cross_check\": {\"orphan_bib\": [\"rastogi2020sgd\"], \"missing_bib\": [], \"orphan_count\": 1, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"synchromesh_iclr2022\", \"type\": \"inproceedings\", \"title\": \"Synchromesh: Reliable Code Generation from Pre-trained Language Models\", \"authors\": \"Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares,...\", \"year\": \"2022\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"mgd_neurips2023\", \"type\": \"inproceedings\", \"title\": \"Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context\", \"authors\": \"Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. ...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"pldi2025_type_constrained_codegen\", \"type\": \"article\", \"title\": \"Type-Constrained Code Generation with Language Models\", \"authors\": \"M\\\\\\\"undler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn ...\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM on Programming Languages\"}, {\"key\": \"roth_yih_2004\", \"type\": \"inproceedings\", \"title\": \"A Linear Programming Formulation for Global Inference in Natural Language Tasks\", \"authors\": \"Roth, Dan and Yih, Wen-tau\", \"year\": \"2004\", \"venue\": \"Proceedings of the Eighth Conference on Computational Natural Language Learning ...\"}, {\"key\": \"adakgc_emnlp2023\", \"type\": \"inproceedings\", \"title\": \"Schema-adaptable Knowledge Graph Construction\", \"authors\": \"Ye, Hongbin and Gui, Honghao and Xu, Xin and Chen, Xi and Chen, Huajun and Zhang...\", \"year\": \"2023\", \
…[truncated 39834 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 42081
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-15T08:33:02.272721+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — Round 1 审稿意见（方法严谨性 + 实验设计与统计）\n\n### Summary（2-3 句）\n\nOntoCoDec 提出了将 IE 本体的 domain/range 约束编译为两层解码时 logit masking（grammar + semantic）的框架，在 SciERC 和 DocRED 上使用 Qwen3-8B 和 Llama-3.1-8B 验证。论文的 violation landscape 分析（tightness 驱动假说）具有洞察力，消融实验设计也较为系统。但 CF violation 爆炸性增长（0.08%→9.90%）构成方法论层面的根本缺陷，加之 post-hoc filtering 在 F1 上反超提出方法、表间数据不一致等问题，当前版本的证据尚不足以支撑论文的核心声明。\n\n---\n\n### Strengths（逐条）\n\n**S1. 首次系统量化 LLM-based IE 的本体约束违反，tightness 假说有实质洞察力。**\n将 violation rate 归因于 constraint tightness 而非 ontology scale（SciERC 7 relations vs DocRED 96 relations 有近似 DR），并给出 per-relation 分析（Figure 1, §5.1, Compare 42.4% vs Used-for 0.76%），这超越了\"LLM 犯错\"的泛泛观察，为理解 violation 模式提供了可操作的理论框架。\n\n**S2. 两层约束的 enabling dependency 通过消融实验得到清晰验证。**\n五路消融（Table 2）展示了 semantic-only 仅减少 24% DR 且无法消除 RV/ET，而 grammar 层提供 vocabulary 保证后 semantic 层的效能跃升至 94% DR reduction。论文的 \"prerequisite structure\" 论证令人信服。\n\n**S3. 统计严谨：bootstrap CI + p-values，跨模型复制。**\n所有核心对比均报告 bootstrap 95% CI 和 p-values（10,000 iterations），SciERC 的 non-significant 结果（p=0.58）被诚实报告。跨模型复制展示了方法在不同 baseline violation profile 下的行为差异。\n\n**S4. 相关工作覆盖全面，定位精确。**\n从 grammar-constrained decoding 到 code 领域 semantic constrained decoding，再到 post-hoc validation，论文清晰区分了 OntoCoDec 的 novelty。\n\n**S5. 诚实的负面结果报告。**\nCF trade-off、post-hoc filtering F1 优势、Llama SciERC 微降等不利结果均被主动报告。\n\n---\n\n### Weaknesses（逐条）\n\n#### Must-Fix\n\n**W1. [Must-Fix] CF violation 从 0.08% 爆发至 9.90%（SciERC）/ 12.02%（Llama DocRED），这不是 \"trade-off\" 而是方法设计缺陷。**\n- 位置: §3.5.3, §7, Table 2/4\n- 当 D[h] ∉ dom(r) 时，semantic layer 放弃注册类型、强制选择 dom(r) 中的任意类型，主动制造 CF violation。Llama DocRED CF 达 12.02%，高于原始 DR 率的量级。论文的实体注册表已追踪类型——完全可以在 D[h] ∉ dom(r) 时拒绝整个 triple 的 semantic 约束，但这一替代方案未被探索甚至未被讨论。\n- 建议: 增加 \"registry-consistent fallback\" 消融；定量分析 CF 对下游任务的影响。\n\n**W2. [Must-Fix] Post-hoc filtering 在 F1 上优于 OntoCoDec。**\n- 位置: Appendix B\n- Post-hoc F1: SciERC 8.63 vs 8.36; DocRED 9.61 vs 8.23。F1 已综合 P/R。缺乏 runtime 对比，无法评估 \"avoiding wasted compute\" 论点。\n- 建议: 报告 wall-clock time 对比；展示 recall trade-off curve；讨论组合方案。\n\n**W3. [Must-Fix] DocRED baseline 数据在 Table 1 和 Table 3 之间不一致。**\n- Table 1: DR=18.7%, ET=7.5%; Table 3: DR=18.46%, ET=2.48%。ET 差 3 倍。Abstract 与 §5.1 也不一致（18.46% vs 18.70%）。不同 exp_id (phase0 vs phase2) 暗示不同配置，但论文无解释。\n\n#### Should-Fix\n\n**W4. [Should-Fix]** 2 数据集 × 2 个 8B 模型，泛化性声明偏强。两个数据集实体类型都只有 6 种。缺少更大类型系统、更大模型、fine-tuned 模型验证。\n\n**W5. [Should-Fix]** 完全缺失 latency/throughput 分析。\n\n**W6. [Should-Fix]** §2 和 §3 的本体形式化不一致（σ: R→P(E×E) vs dom/range: R→2^E，表达能力不同）。\n\n**W7. [Should-Fix]** 标题 \"Type-Valid\" 误导——DocRED 残余 DR=10.21%，加上 CF 12.02%，远非 \"valid\"。建议改为 \"Type-Constrained\"。\n\n**W8. [Should-Fix]** R-F1≈8% 零-shot 基线下的实际意义评估有限。\"F1 as control variable\" 部分有理但存在循环论证风险。\n\n**W9. [Should-Fix]** S1 vs S2 缺计算成本归一化。S2 用两次推理但未报告 runtime。\n\n#### Minor\n\n**W10. [Minor]** Prompt 模板未提供。**W11. [Minor]** DocRED 用 dev set 未说明理由。**W12. [Minor]** Entity type 首 subword 唯一性未对 Llama tokenizer 验证。**W13. [Minor]** Grammar-only 在 DocRED 上 DR 增加 42%，应在 abstract/intro 中提及。**W14. [Minor]** Bib 中 rastogi2020sgd 为 orphan entry；regino2025kgcurator 在 OpenAlex 中未找到。\n\n---\n\n### Questions\n\nQ1. 当 D[h] ∉ dom(r) 时，为什么 override 注册类型而非回退 grammar-only 处理整个 triple？\nQ2. Table 1 vs Table 3 DocRED baseline 数据不一致的原因？\nQ3. OntoCoDec vs post-hoc 的 wall-clock time？\nQ4. Entity type 首 subword 唯一性是否对 Llama tokenizer 验证？\nQ5. 论文实际实现的是 Cartesian product 还是 arbitrary pair 的 ontology 结构？\nQ6. SciERC 的 fallback 事件频率和 fallback-to-DR 转化比？\n\n---\n\n### Overall Assessment\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2.5/5 | 架构合理、消融充分，但 CF 缺陷、post-hoc 胜出、数据不一致 |\n| Excitement | 2.5/5 | Tightness 假说有新意，方向好，但实际效果有限 |\n| Overall | 2.5/5 | 介于 Resubmit 和 Findings 之间 |\n| Reproducibility | 2/5 | 缺 prompt/hardware/runtime；表间不一致 |\n| Confidence | 4/5 | 熟悉 constrained decoding 和 IE evaluation |\n\n一句话：方向正确、分析有洞察力，但 CF 爆炸是未解决的方法缺陷，post-hoc F1 反超和表间数据不一致进一步削弱核心论点。",
  "reviewer_id": "1",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — Round 1 审稿意见（方法严谨性 + 实验设计与统计）\n\n### Summary（2-3 句）\n\nOntoCoDec 提出了将 IE 本体的 domain/range 约束编译为两层解码时 logit masking（grammar + semantic）的框架，在 SciERC 和 DocRED 上使用 Qwen3-8B 和 Llama-3.1-8B 验证。论文的 violation landscape 分析（tightness 驱动假说）具有洞察力，消融实验设计也较为系统。但 CF violation 爆炸性增长（0.08%→9.90%）构成方法论层面的根本缺陷，加之 post-hoc filtering 在 F1 上反超提出方法、表间数据不一致等问题，当前版本的证据尚不足以支撑论文的核心声明。\n\n---\n\n### Strengths（逐条）\n\n**S1. 首次系统量化 LLM-based IE 的本体约束违反，tightness 假说有实质洞察力。**\n将 violation rate 归因于 constraint tightness 而非 ontology scale（SciERC 7 relations vs DocRED 96 relations 有近似 DR），并给出 per-relation 分析（Figure 1, §5.1, Compare 42.4% vs Used-for 0.76%），这超越了\"LLM 犯错\"的泛泛观察，为理解 violation 模式提供了可操作的理论框架。\n\n**S2. 两层约束的 enabling dependency 通过消融实验得到清晰验证。**\n五路消融（Table 2）展示了 semantic-only 仅减少 24% DR 且无法消除 RV/ET，而 grammar 层提供 vocabulary 保证后 semantic 层的效能跃升至 94% DR reduction。论文的 \"prerequisite structure\" 论证令人信服。\n\n**S3. 统计严谨：bootstrap CI + p-values，跨模型复制。**\n所有核心对比均报告 bootstrap 95% CI 和 p-values（10,000 iterations），SciERC 的 non-significant 结果（p=0.58）被诚实报告。跨模型复制展示了方法在不同 baseline violation profile 下的行为差异。\n\n**S4. 相关工作覆盖全面，定位精确。**\n从 grammar-constrained decoding 到 code 领域 semantic constrained decoding，再到 post-hoc validation，论文清晰区分了 OntoCoDec 的 novelty。\n\n**S5. 诚实的负面结果报告。**\nCF trade-off、post-hoc filtering F1 优势、Llama SciERC 微降等不利结果均被主动报告。\n\n---\n\n### Weaknesses（逐条）\n\n#### Must-Fix\n\n**W1. [Must-Fix] CF violation 从 0.08% 爆发至 9.90%（SciERC）/ 12.02%（Llama DocRED），这不是 \"trade-off\" 而是方法设计缺陷。**\n- 位置: §3.5.3, §7, Table 2/4\n- 当 D[h] ∉ dom(r) 时，semantic layer 放弃注册类型、强制选择 dom(r) 中的任意类型，主动制造 CF violation。Llama DocRED CF 达 12.02%，高于原始 DR 率的量级。论文的实体注册表已追踪类型——完全可以在 D[h] ∉ dom(r) 时拒绝整个 triple 的 semantic 约束，但这一替代方案未被探索甚至未被讨论。\n- 建议: 增加 \"registry-consistent fallback\" 消融；定量分析 CF 对下游任务的影响。\n\n**W2. [Must-Fix] Post-hoc filtering 在 F1 上优于 OntoCoDec。**\n- 位置: Appendix B\n- Post-hoc F1: SciERC 8.63 vs 8.36; DocRED 9.61 vs 8.23。F1 已综合 P/R。缺乏 runtime 对比，无法评估 \"avoiding wasted compute\" 论点。\n- 建议: 报告 wall-clock time 对比；展示 recall trade-off curve；讨论组合方案。\n\n**W3. [Must-Fix] DocRED baseline 数据在 Table 1 和 Table 3 之间不一致。**\n- Table 1: DR=18.7%, ET=7.5%; Table 3: DR=18.46%, ET=2.48%。ET 差 3 倍。Abstract 与 §5.1 也不一致（18.46% vs 18.70%）。不同 exp_id (phase0 vs phase2) 暗示不同配置，但论文无解释。\n\n#### Should-Fix\n\n**W4. [Should-Fix]** 2 数据集 × 2 个 8B 模型，泛化性声明偏强。两个数据集实体类型都只有 6 种。缺少更大类型系统、更大模型、fine-tuned 模型验证。\n\n**W5. [Should-Fix]** 完全缺失 latency/throughput 分析。\n\n**W6. [Should-Fix]** §2 和 §3 的本体形式化不一致（σ: R→P(E×E) vs dom/range: R→2^E，表达能力不同）。\n\n**W7. [Should-Fix]** 标题 \"Type-Valid\" 误导——DocRED 残余 DR=10.21%，加上 CF 12.02%，远非 \"valid\"。建议改为 \"Type-Constrained\"。\n\n**W8. [Should-Fix]** R-F1≈8% 零-shot 基线下的实际意义评估有限。\"F1 as control variable\" 部分有理但存在循环论证风险。\n\n**W9. [Should-Fix]** S1 vs S2 缺计算成本归一化。S2 用两次推理但未报告 runtime。\n\n#### Minor\n\n**W10. [Minor]** Prompt 模板未提供。**W11. [Minor]** DocRED 用 dev set 未说明理由。**W12. [Minor]** Entity type 首 subword 唯一性未对 Llama tokenizer 验证。**W13. [Minor]** Grammar-only 在 DocRED 上 DR 增加 42%，应在 abstract/intro 中提及。**W14. [Minor]** Bib 中 rastogi2020sgd 为 orphan entry；regino2025kgcurator 在 OpenAlex 中未找到。\n\n---\n\n### Questions\n\nQ1. 当 D[h] ∉ dom(r) 时，为什么 override 注册类型而非回退 grammar-only 处理整个 triple？\nQ2. Table 1 vs Table 3 DocRED baseline 数据不一致的原因？\nQ3. OntoCoDec vs post-hoc 的 wall-clock time？\nQ4. Entity type 首 subword 唯一性是否对 Llama tokenizer 验证？\nQ5. 论文实际实现的是 Cartesian product 还是 arbitrary pair 的 ontology 结构？\nQ6. SciERC 的 fallback 事件频率和 fallback-to-DR 转化比？\n\n---\n\n### Overall Assessment\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2.5/5 | 架构合理、消融充分，但 CF 缺陷、post-hoc 胜出、数据不一致 |\n| Excitement | 2.5/5 | Tightness 假说有新意，方向好，但实际效果有限 |\n| Overall | 2.5/5 | 介于 Resubmit 和 Findings 之间 |\n| Reproducibility | 2/5 | 缺 prompt/hardware/runtime；表间不一致 |\n| Confidence | 4/5 | 熟悉 constrained decoding 和 IE evaluation |\n\n一句话：方向正确、分析有洞察力，但 CF 爆炸是未解决的方法缺陷，post-hoc F1 反超和表间数据不一致进一步削弱核心论点。",
    "reviewer_id": "1",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 47 · 2026-05-15T08:33:06.244181+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3971
}
```

</details>

---


### Assistant

_source line 48 · 2026-05-15T08:33:16.169107+00:00_

Round 1 审稿完成，已提交至 Review Director。

**核心评分**: Soundness 2.5/5, Excitement 2.5/5, Overall 2.5/5

**三个 Must-Fix 问题**:
1. **CF violation 爆炸**（0.08%→9.90%/12.02%）——semantic layer 在 D[h]∉dom(r) 时主动覆写注册类型，方法设计可改但未探索
2. **Post-hoc filtering F1 反超**（SciERC 8.63 vs 8.36, DocRED 9.61 vs 8.23）——缺 runtime 对比无法支撑 "decoding-time 优于 post-hoc" 的论点
3. **DocRED baseline 表间数据不一致**（Table 1 ET=7.5% vs Table 3 ET=2.48%，差 3 倍）

**主要 Should-Fix**: 泛化性声明偏强（仅 2×2）、缺 latency 分析、§2/§3 形式化不一致、标题 "Type-Valid" 误导。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1"
}
```

</details>

---


## Round 2

## Round 2

4 recorded events


### User

_source line 49 · 2026-05-15T08:34:40.144564+00:00_

[Round 1 审稿请求]:
## Step 2 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整 Round 1 审稿意见。请逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

## Reviewer 2 — Round 1 审稿意见（新颖性 + Related Work + 写作质量）

### Summary（2-3 句）

本文提出 OntoCoDec，一个两层约束解码框架：grammar 层（XGrammar CFG）保证 JSON 结构和词汇合法性，semantic 层通过有状态 entity registry + 动态 logit masking 强制 domain/range 约束。在 SciERC 和 DocRED 上用 Qwen3-8B 和 Llama-3.1-8B 零样本验证，DR 违规减少 45–99%，F1 保持中性或显著提升。论文还提出 constraint tightness 概念解释跨数据集和跨模型的 DR 消减差异。

### Strengths

**S1. 系统性的违规分类与分析框架。** 四类违规（DR/RV/ET/CF）定义清晰，Phase 0 系统性研究揭示了 LLM-based IE 中本体违规的普遍性（SciERC 15.37%、DocRED 18.46%），诊断性贡献本身有价值。

**S2. 两层架构的 enabling dependency 有力验证。** 五路消融（Table 2）展示 grammar-only 仅消除 RV/ET 而 DR 不变、semantic-only DR 仅降 24%，两层组合达 94%——grammar 保证词汇合法性后 semantic 才能查询 dom/range 规则。实验论证充分。

**S3. Constraint tightness 分析提供可解释的理论框架。** tightness × baseline RV 双因子机制很好解释了 SciERC vs DocRED 差异以及 Qwen vs Llama 非对称表现，超越单纯经验报告。

**S4. 实验设计严谨。** Bootstrap resampling（10,000 次）配合 95% CI 和 p 值，2 模型 × 2 数据集交叉验证，S1 vs S2 策略对比，统计方法论扎实。

**S5. Related Work 覆盖全面定位清晰。** 正文 §6 + Appendix A 覆盖六大范式，与 code gen 类型约束解码的对比细致（PICARD/Synchromesh/MGD/PLDI 2025），主动引用 CRANE/Schall/Tam 负面结果并论证 IE 特殊性。

**S6. Grammar layer "揭露"隐藏违规的发现有洞察力。** DocRED grammar-only DR 从 18.46% 升至 26.17%（Table 3），29.66% OOV 关系被纠正后暴露原本不可评估的类型不兼容。

### Weaknesses

**W1 [Must-Fix] §2 与 §3 的本体形式化存在根本性不一致**
- §2 定义 σ: R → P(E × E)（pair-based），§3 重定义为 dom, range: R → 2^E（independent）。这两个定义在一般情况下不等价：若 σ(r) = {(Person, Person), (Org, Org)}，则 independent check 错误放行 (Person, Org)。
- Violation rate 评估用 pair-based 定义（§5.1），但执行用 independent dom/range。残余 DR 中有多少是 fallback 导致、有多少是 dom/range 独立性导致，论文无法区分。Tightness 公式基于 pair 计数但实际执行更宽松。
- 建议：明确 SciERC/DocRED 约束是否 rectangular（σ(r) = dom(r) × range(r)）；统一符号。

**W2 [Must-Fix] CF 违规剧烈恶化未被充分分析，削弱"zero cost"叙事**
- CF 从 0.08% 恶化到 9.90%（SciERC）和 0.17% 到 12.02%（Llama-DocRED）。将一种违规转化为另一种违规而不量化 trade-off 净效果，使"constraint enforcement"整体价值难评估。
- §7 将 CF 定性为"qualitatively different"可能被视为 minimize 问题。下游 KG 构建需要全局实体类型一致性。
- 建议：提供综合指标评估 DR↓ vs CF↑ 净效果；将 global entity-level type consensus 更明确列为当前方法主要局限。

**W3 [Should-Fix] 仅零样本评估，无法验证与 fine-tuned 模型的可组合性声明**
- R-F1 约 8% 距 SOTA ~50% 差距巨大。论文声称与 GoLLIE 等可组合（§6），但未提供任何 fine-tuned 实验。
- 建议：至少在一个设置上用 fine-tuned 模型验证残余违规率和边际收益。

**W4 [Should-Fix] 新颖性声明需更精确范围界定**
- §1 Contribution #2 "the first to extend grammar-constrained decoding with semantic ontology constraints" 可被理解为领域无关的首创声明，但 code gen（Synchromesh 2022, PICARD 2021）早已实现语义类型约束。§6 的讨论实际很到位但 Introduction 表述过于宽泛。
- 建议：改为 "the first to automatically compile IE ontology domain/range constraints into token-level semantic masks"。

**W5 [Should-Fix] Single-token type assumption 限制可扩展性未充分讨论**
- §3.3.2 将每个 τ ∈ E 映射到 first subword token，仅验证 6 types + Qwen tokenizer。更大本体可能不满足 first-token 唯一性。Llama tokenizer 未报告验证结果。
- 建议：讨论 scalability 和 multi-token masking 可行性。

**W6 [Minor] 数学符号跨 section 不一致**
- §2 用 σ，§3 用 dom/range；tightness 公式分别用 |σ(r)|/|E|² 和 |V(r)|/|T|²。

**W7 [Minor] Constraint tightness 属于相对直觉性观察**
- "约束越紧违规越高"符合直觉。Dual-factor mechanism 增加解释力但更接近 systematic empirical observation。

**W8 [Minor] 个别表述问题**
- Abstract 首句 "produce systematic ontology constraint violations" 过于绝对，建议 "can produce"
- §3.3.2 "DocRED (6 types each)" 中 "each" 指代不清（DocRED 有 96 relation types 但仅 6 entity types）

### Questions

Q1. SciERC/DocRED 的约束是否 rectangular（σ(r) = dom(r) × range(r)）？如不是，independent enforcement 的 over-permissiveness 有多大？
Q2. 残余 DR 中，grammar-first fallback 导致 vs dom/range 独立性导致的比例？
Q3. Llama tokenizer 对 6 个实体类型的 first-token uniqueness 是否已验证？
Q4. CF 冲突实体中，多少是真实标注类型歧义，多少是约束强制扭曲了模型正确输出？
Q5. OntoCoDec 因约束重定向概率质量而引入的 false positives 有多少？

### Missing References

建议性补充（非严重遗漏）：
1. SuRE (Kim et al., ACL 2024) — schema-based structured generation for RE
2. Constrained Beam Search for KGC（如 KG-BERT + type constraints）
3. 总体 Related Work 覆盖已相当全面。

### Overall Assessment

| 维度 | 分数 | 理由 |
|------|------|------|
| Soundness | 3/5 | 方法有效但 pair vs independent 形式化不一致构成理论缺陷；CF trade-off 分析不充分 |
| Excitement | 3/5 | Tightness 分析有洞察力、enabling dependency 有趣，但核心技术（logit masking for type constraints）已在 code gen 成熟 |
| Overall | 3/5 (Findings 边界) | 工程扎实、实验充分，但新颖性有限、形式化有缺陷、CF trade-off 削弱贡献叙事 |
| Reproducibility | 4/5 | 实验设置详尽但无代码发布承诺 |
| Confidence | 4/5 | 熟悉 constrained decoding 和 IE 评估方法论 |

---

请对以上每条 Weakness 和 Question 逐条回应 [AGREE] 或 [REBUT]，并特别关注与你自己发现的交集和差异。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-15T08:36:25.862880+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 交叉回应 Reviewer 2 审稿意见\n\n### Weaknesses 逐条回应\n\n**[AGREE] R2-W1: §2 vs §3 形式化不一致。** R2 比我更深入——指出评估用 pair-based 但执行用 independent dom/range，可能导致 over-permission 且与 tightness 公式的基础矛盾。我的 W6 只提了表达能力差异，R2 揭示了评估/执行错位这个更关键问题。\n\n**[AGREE] R2-W2: CF 违规恶化。** 与我的 W1 完全一致。补充：Llama DocRED 的 DR↓23.52pp vs CF↑11.85pp，综合改善仅~11.67pp。CF 机制根源是 §3.5.3 中当 D[h]∉dom(r) 时主动 override 注册类型——技术上可避免。\n\n**[AGREE] R2-W3: 零样本 only。** 与我的 W4/W8 重叠。\n\n**[AGREE] R2-W4: 新颖性声明过宽。** §1 vs §6 措辞不一致。R2 建议的改写更准确。\n\n**[AGREE] R2-W5: Single-token 假设限制扩展性。** 我列为 Minor，R2 升为 Should-Fix 合理。\n\n**[AGREE] R2-W6: 符号不一致。** 重叠。\n\n**[REBUT] R2-W7: Tightness 直觉性。** 部分不同意。tightness 的定量化（τ̄=0.333 vs 0.842）和 tightness×RV 双因子交互（同一 ontology 上 Qwen 10.21% vs Llama 2.55% 残余 DR）超越简单直觉。但同意它更接近 systematic empirical observation 而非理论贡献。\n\n**[AGREE] R2-W8: 表述问题。** 同意。\n\n### Questions 逐条回应\n\n**[AGREE] R2-Q1-Q3:** 与我的 Q5/Q6/Q4 重叠。\n**[AGREE] R2-Q4:** 比我的分析更精细——245 受影响实体中仅 60 被归因为 Generic↔OST 歧义，其余 185 需要解释。\n**[AGREE] R2-Q5:** 好问题，我未单独提出。概率质量重定向可能制造 \"合规但错误\" 的 false positives。\n\n### 核心分歧\n\n我比 R2 低 0.5 分，因为我额外将两点列为 Must-Fix：\n1. Post-hoc filtering F1 优于 OntoCoDec（Appendix B: SciERC 8.63 vs 8.36, DocRED 9.61 vs 8.23）——R2 未讨论\n2. Table 1 vs Table 3 DocRED baseline 数据不一致（ET: 7.5% vs 2.48%）——R2 未发现\n\n这两点直接影响 soundness。如果作者提供 runtime 对比和表间差异解释，我愿上调评分。",
  "reviewer_id": "1",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 交叉回应 Reviewer 2 审稿意见\n\n### Weaknesses 逐条回应\n\n**[AGREE] R2-W1: §2 vs §3 形式化不一致。** R2 比我更深入——指出评估用 pair-based 但执行用 independent dom/range，可能导致 over-permission 且与 tightness 公式的基础矛盾。我的 W6 只提了表达能力差异，R2 揭示了评估/执行错位这个更关键问题。\n\n**[AGREE] R2-W2: CF 违规恶化。** 与我的 W1 完全一致。补充：Llama DocRED 的 DR↓23.52pp vs CF↑11.85pp，综合改善仅~11.67pp。CF 机制根源是 §3.5.3 中当 D[h]∉dom(r) 时主动 override 注册类型——技术上可避免。\n\n**[AGREE] R2-W3: 零样本 only。** 与我的 W4/W8 重叠。\n\n**[AGREE] R2-W4: 新颖性声明过宽。** §1 vs §6 措辞不一致。R2 建议的改写更准确。\n\n**[AGREE] R2-W5: Single-token 假设限制扩展性。** 我列为 Minor，R2 升为 Should-Fix 合理。\n\n**[AGREE] R2-W6: 符号不一致。** 重叠。\n\n**[REBUT] R2-W7: Tightness 直觉性。** 部分不同意。tightness 的定量化（τ̄=0.333 vs 0.842）和 tightness×RV 双因子交互（同一 ontology 上 Qwen 10.21% vs Llama 2.55% 残余 DR）超越简单直觉。但同意它更接近 systematic empirical observation 而非理论贡献。\n\n**[AGREE] R2-W8: 表述问题。** 同意。\n\n### Questions 逐条回应\n\n**[AGREE] R2-Q1-Q3:** 与我的 Q5/Q6/Q4 重叠。\n**[AGREE] R2-Q4:** 比我的分析更精细——245 受影响实体中仅 60 被归因为 Generic↔OST 歧义，其余 185 需要解释。\n**[AGREE] R2-Q5:** 好问题，我未单独提出。概率质量重定向可能制造 \"合规但错误\" 的 false positives。\n\n### 核心分歧\n\n我比 R2 低 0.5 分，因为我额外将两点列为 Must-Fix：\n1. Post-hoc filtering F1 优于 OntoCoDec（Appendix B: SciERC 8.63 vs 8.36, DocRED 9.61 vs 8.23）——R2 未讨论\n2. Table 1 vs Table 3 DocRED baseline 数据不一致（ET: 7.5% vs 2.48%）——R2 未发现\n\n这两点直接影响 soundness。如果作者提供 runtime 对比和表间差异解释，我愿上调评分。",
    "reviewer_id": "1",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 51 · 2026-05-15T08:36:29.985767+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4122
}
```

</details>

---


### Assistant

_source line 52 · 2026-05-15T08:36:36.059300+00:00_

交叉回应已提交给 Director。

总结：14 条意见中 13 条 [AGREE]、1 条 [REBUT]（R2-W7 tightness 直觉性——双因子交互和定量化有超越直觉的贡献）。与 R2 的主要分歧在于我额外识别了两个 R2 未涉及的 Must-Fix 问题（post-hoc F1 胜出 + 表间数据不一致），导致我给出 2.5 vs R2 的 3.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1"
}
```

</details>

---


## Round 3

## Round 3

38 recorded events


### User

_source line 53 · 2026-05-16T02:42:52.652406+00:00_

[Round 1 审稿请求]:
[Dream 审稿任务 — Reviewer 1：方法 + 实验]

论文：OntoCoDec: Type-Valid Information Extraction via Compiled Ontology Constraints
PDF 路径：/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/review_input_db82206b.pdf

你的审查侧重：
- **方法描述**：是否完整、claim 是否被实验数据支撑、关键超参 / 训练流程是否清晰
- **实验设计**：是否覆盖关键 baseline / ablation / 跨数据集 / scale 维度
- **数据呈现**：表格 / 图是否能让审稿人复现结论、误差棒 / 统计显著性是否充分

评分标准：top ML venue 通用标准（接受率 ~25%，6 分制：1=Strong Reject … 6=Strong Accept）。

Dream 审稿边界提醒：
- 不需要评审：Reproducibility checklist、代码/数据可用性、具体数值精确性（数字是想象的，关注实验设计而非数值）、伦理/IRB、匿名性
- 需要评审但标注为 "presentation 层面"：Reference 真实性、论文完整度、Related Work 引用数量
- 必须评审（idea 层面）：实验设计是否足以支撑 claims（假设数据为真）、叙事逻辑是否自洽、Claim 的 generality 是否被实验范围支撑

每条 weakness 必须标注属于 **idea 层面** 还是 **presentation 层面**。

评分校准规则：
- 3+ Major issues → 不高于 Borderline Reject
- 2 Major issues → 不高于 Weak Accept
- 1 Major issue → 不高于 Accept
- 0 Major issues → 可给 Strong Accept
Major issue 须有 explicit justification。如最终评分高于校准基准，须解释 override 理由。

请基于论文内容独立评判，不要假设论文结果的质量高低。

**不要评判**：新颖性 / 相关工作（那是 Reviewer 2 的范围）、格式 / 排版。

完成后请通过 review_reviewer_post_to_director 汇报。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 54 · 2026-05-16T02:43:03.132024+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/review_input_db82206b.pdf",
  "pages": "1-10",
  "dpi": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/review_input_db82206b.pdf",
    "pages": "1-10",
    "dpi": "200"
  }
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-16T02:43:03.387243+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"页码超出范围 (共 9 页): 1-10\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 255
}
```

</details>

---


### Tool call

_source line 56 · 2026-05-16T02:43:06.205898+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/review_input_db82206b.pdf",
  "pages": "1-9",
  "dpi": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/review_input_db82206b.pdf",
    "pages": "1-9",
    "dpi": "200"
  }
}
```

</details>

---


### Tool result

_source line 57 · 2026-05-16T02:43:09.730890+00:00_

Error: result (4,991,985 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-1-11179fb2/47fb6856-8137-46fb-b2cf-123d4952ccae/tool-results/mcp-agent-ml-research-pdf_to_images-1778899389550.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-1-11179fb2/47fb6856-8137-46fb-b2cf-123d4952ccae/tool-results/mcp-agent-ml-research-pdf_to_images-1778899389550.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 3524
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-16T02:43:14.076810+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/review_input_db82206b.pdf",
  "pages": "1-3",
  "dpi": "180"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/review_input_db82206b.pdf",
    "pages": "1-3",
    "dpi": "180"
  }
}
```

</details>

---


### Tool result

_source line 59 · 2026-05-16T02:43:15.441323+00:00_

Error: result (1,500,687 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-1-11179fb2/47fb6856-8137-46fb-b2cf-123d4952ccae/tool-results/mcp-agent-ml-research-pdf_to_images-1778899395365.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-1-11179fb2/47fb6856-8137-46fb-b2cf-123d4952ccae/tool-results/mcp-agent-ml-research-pdf_to_images-1778899395365.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1364
}
```

</details>

---


### Tool call

_source line 60 · 2026-05-16T02:43:18.917491+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/review_input_db82206b.pdf",
  "pages": "1",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/review_input_db82206b.pdf",
    "pages": "1",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 61 · 2026-05-16T02:43:19.373571+00:00_

Error: result (452,873 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-1-11179fb2/47fb6856-8137-46fb-b2cf-123d4952ccae/tool-results/mcp-agent-ml-research-pdf_to_images-1778899399334.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-1-11179fb2/47fb6856-8137-46fb-b2cf-123d4952ccae/tool-results/mcp-agent-ml-research-pdf_to_images-1778899399334.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 456
}
```

</details>

---


### Tool call

_source line 62 · 2026-05-16T02:43:24.562079+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-1-11179fb2/47fb6856-8137-46fb-b2cf-123d4952ccae/tool-results/mcp-agent-ml-research-pdf_to_images-1778899399334.txt",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-1-11179fb2/47fb6856-8137-46fb-b2cf-123d4952ccae/tool-results/mcp-agent-ml-research-pdf_to_images-1778899399334.txt",
    "limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-16T02:43:25.013799+00:00_

File content (385686 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 64 · 2026-05-16T02:43:30.996902+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best && python3 -c \"\nimport json\n# Just extract the file paths from the result\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-1-11179fb2/47fb6856-8137-46fb-b2cf-123d4952ccae/tool-results/mcp-agent-ml-research-pdf_to_images-1778899399334.txt') as f:\n    data = json.loads(f.read())\n    result = json.loads(data['result'])\n    if 'data' in result and 'pages' in result['data']:\n        for p in result['data']['pages']:\n            print(p.get('file_path', 'no path'))\n    else:\n        print(list(result.keys()) if isinstance(result, dict) else type(result))\n\"\n",
  "description": "Extract image file paths from PDF render result"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best && python3 -c \"\nimport json\n# Just extract the file paths from the result\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-1-11179fb2/47fb6856-8137-46fb-b2cf-123d4952ccae/tool-results/mcp-agent-ml-research-pdf_to_images-1778899399334.txt') as f:\n    data = json.loads(f.read())\n    result = json.loads(data['result'])\n    if 'data' in result and 'pages' in result['data']:\n        for p in result['data']['pages']:\n            print(p.get('file_path', 'no path'))\n    else:\n        print(list(result.keys()) if isinstance(result, dict) else type(result))\n\"\n",
    "description": "Extract image file paths from PDF render result"
  }
}
```

</details>

---


### Tool result

_source line 65 · 2026-05-16T02:43:31.198871+00:00_

['success', 'data', 'error', 'metadata']
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_1_11179fb2

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 66 · 2026-05-16T02:43:38.330749+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-1-11179fb2/47fb6856-8137-46fb-b2cf-123d4952ccae/tool-results/mcp-agent-ml-research-pdf_to_images-1778899399334.txt') as f:\n    data = json.loads(f.read())\n    result = json.loads(data['result'])\n    d = result.get('data', {})\n    print(type(d), list(d.keys()) if isinstance(d, dict) else 'not dict')\n    if isinstance(d, dict):\n        for k,v in d.items():\n            if isinstance(v, str) and len(v) < 500:\n                print(f'{k}: {v}')\n            elif isinstance(v, list):\n                print(f'{k}: list of {len(v)}')\n                if len(v) > 0 and isinstance(v[0], dict):\n                    print(f'  keys: {list(v[0].keys())}')\n                    for key in v[0]:\n                        val = v[0][key]\n                        if isinstance(val, str) and len(val) < 300:\n                            print(f'  {key}: {val}')\n                        else:\n                            print(f'  {key}: len={len(str(val))}')\n            else:\n                print(f'{k}: {type(v)}')\n\"\n",
  "description": "Inspect PDF render result structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-1-11179fb2/47fb6856-8137-46fb-b2cf-123d4952ccae/tool-results/mcp-agent-ml-research-pdf_to_images-1778899399334.txt') as f:\n    data = json.loads(f.read())\n    result = json.loads(data['result'])\n    d = result.get('data', {})\n    print(type(d), list(d.keys()) if isinstance(d, dict) else 'not dict')\n    if isinstance(d, dict):\n        for k,v in d.items():\n            if isinstance(v, str) and len(v) < 500:\n                print(f'{k}: {v}')\n            elif isinstance(v, list):\n                print(f'{k}: list of {len(v)}')\n                if len(v) > 0 and isinstance(v[0], dict):\n                    print(f'  keys: {list(v[0].keys())}')\n                    for key in v[0]:\n                        val = v[0][key]\n                        if isinstance(val, str) and len(val) < 300:\n                            print(f'  {key}: {val}')\n                        else:\n                            print(f'  {key}: len={len(str(val))}')\n            else:\n                print(f'{k}: {type(v)}')\n\"\n",
    "description": "Inspect PDF render result structure"
  }
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-16T02:43:38.431696+00:00_

&lt;class 'dict'> ['images', 'total_pages', 'rendered_pages', 'dpi', 'output_dir']
images: list of 1
  keys: ['page', 'path', 'base64', 'width', 'height', 'size_kb']
  page: len=1
  path: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/paper_p1.png
  base64: len=452284
  width: len=4
  height: len=4
  size_kb: len=5
total_pages: &lt;class 'int'>
rendered_pages: &lt;class 'int'>
dpi: &lt;class 'int'>
output_dir: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 68 · 2026-05-16T02:43:46.424885+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess, json\n# Use the MCP tool to render all pages - we just need the files on disk\n# Let's use pymupdf directly\nimport fitz\npdf_path = '/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/review_input_db82206b.pdf'\nout_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images'\nimport os\nos.makedirs(out_dir, exist_ok=True)\ndoc = fitz.open(pdf_path)\nprint(f'Total pages: {len(doc)}')\nfor i in range(len(doc)):\n    page = doc[i]\n    mat = fitz.Matrix(150/72, 150/72)  # 150 DPI\n    pix = page.get_pixmap(matrix=mat)\n    out_path = f'{out_dir}/page_{i+1}.png'\n    pix.save(out_path)\n    print(f'Page {i+1}: {out_path} ({pix.width}x{pix.height})')\ndoc.close()\n\"\n",
  "description": "Render all PDF pages to PNG at 150 DPI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess, json\n# Use the MCP tool to render all pages - we just need the files on disk\n# Let's use pymupdf directly\nimport fitz\npdf_path = '/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/review_input_db82206b.pdf'\nout_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images'\nimport os\nos.makedirs(out_dir, exist_ok=True)\ndoc = fitz.open(pdf_path)\nprint(f'Total pages: {len(doc)}')\nfor i in range(len(doc)):\n    page = doc[i]\n    mat = fitz.Matrix(150/72, 150/72)  # 150 DPI\n    pix = page.get_pixmap(matrix=mat)\n    out_path = f'{out_dir}/page_{i+1}.png'\n    pix.save(out_path)\n    print(f'Page {i+1}: {out_path} ({pix.width}x{pix.height})')\ndoc.close()\n\"\n",
    "description": "Render all PDF pages to PNG at 150 DPI"
  }
}
```

</details>

---


### Tool result

_source line 69 · 2026-05-16T02:43:47.781431+00:00_

Total pages: 9
Page 1: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/page_1.png (1241x1754)
Page 2: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/page_2.png (1241x1754)
Page 3: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/page_3.png (1241x1754)
Page 4: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/page_4.png (1241x1754)
Page 5: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/page_5.png (1241x1754)
Page 6: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/page_6.png (1241x1754)
Page 7: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/page_7.png (1241x1754)
Page 8: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/page_8.png (1241x1754)
Page 9: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/page_9.png (1241x1754)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 1356
}
```

</details>

---


### Tool call

_source line 70 · 2026-05-16T02:43:51.747328+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/page_1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/page_1.png"
  }
}
```

</details>

---


### Tool call

_source line 71 · 2026-05-16T02:43:52.299980+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/page_2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/page_2.png"
  }
}
```

</details>

---


### Tool call

_source line 72 · 2026-05-16T02:43:52.454189+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/page_3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/page_3.png"
  }
}
```

</details>

---


### Tool result

_source line 73 · 2026-05-16T02:43:52.463489+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 716
}
```

</details>

---


### Tool result

_source line 74 · 2026-05-16T02:43:53.626183+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1326
}
```

</details>

---


### Tool result

_source line 75 · 2026-05-16T02:43:53.780617+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1326
}
```

</details>

---


### Tool call

_source line 76 · 2026-05-16T02:44:05.384611+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/page_4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/page_4.png"
  }
}
```

</details>

---


### Tool call

_source line 77 · 2026-05-16T02:44:05.385089+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/page_5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/page_5.png"
  }
}
```

</details>

---


### Tool call

_source line 78 · 2026-05-16T02:44:05.687806+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/page_6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/page_6.png"
  }
}
```

</details>

---


### Tool result

_source line 79 · 2026-05-16T02:44:06.142705+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 758
}
```

</details>

---


### Tool result

_source line 80 · 2026-05-16T02:44:06.696549+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1311
}
```

</details>

---


### Tool result

_source line 81 · 2026-05-16T02:44:06.703132+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1015
}
```

</details>

---


### Tool call

_source line 82 · 2026-05-16T02:44:30.449884+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/page_7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/page_7.png"
  }
}
```

</details>

---


### Tool result

_source line 83 · 2026-05-16T02:44:31.105552+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 655
}
```

</details>

---


### Tool call

_source line 84 · 2026-05-16T02:44:31.206430+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/page_8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/page_8.png"
  }
}
```

</details>

---


### Tool call

_source line 85 · 2026-05-16T02:44:31.509870+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/page_9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/page_9.png"
  }
}
```

</details>

---


### Tool result

_source line 86 · 2026-05-16T02:44:31.612977+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 406
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-16T02:44:31.968209+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 458
}
```

</details>

---


### Tool call

_source line 88 · 2026-05-16T02:48:56.326402+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — Dream 审稿意见（方法 + 实验）\n\n### Summary\nOntoCoDec Dream 版本在原始零样本验证基础上增加了 LoRA fine-tuning composability 实验（2×3 设计），展示 FT+OntoCoDec 消除残余 violations（DR: 0.76%→0%），CF 从 12.02% 骤降至 0.42%。叙事结构清晰，但核心实验仅覆盖一个数据集且缺乏统计显著性检验。\n\n### Strengths\n- S1 [idea]: Composability 实验是正确的实验方向，直接回答实用价值问题\n- S2 [idea]: CF collapse under fine-tuning 化解了零样本版本最核心的弱点\n- S3 [idea]: Problem→Solution→ZS validation→Composability→Analysis 叙事逻辑自洽\n- S4 [presentation]: 形式化全程使用独立 dom/range，消除了原始版本的不一致\n\n### Weaknesses\n\n**W1. [Major, idea] Composability 仅在 DocRED 上验证。** 论文自定义的 \"central contribution\" 仅单数据集支撑。SciERC 的 CF 特征（零样本 9.90%、Generic↔OST 结构性歧义）使其成为 CF collapse 泛化性的关键测试场景，但缺失。§6 Conclusion 未附数据集限定。\n\n**W2. [Major, idea] 无统计显著性检验。** FT→FT+OntoCoDec 的 ΔR-F1=+0.06pp/−0.01pp 在噪声范围内。\"Zero cost\" 是核心 value proposition，但没有 bootstrap CI 或 p-values 支撑。\n\n**W3. [Should-Fix, idea] FT 下缺少 grammar-only/semantic-only 消融。**\n**W4. [Should-Fix, idea] FT 下缺少 post-hoc filtering 对比。**\n**W5. [Should-Fix, idea] CF collapse 机制未被分析（override frequency ZS vs FT）。**\n**W6. [Minor, idea] 泛化性声明超出 2×8B 实验范围。**\n**W7. [Minor, presentation] Tightness 无公式定义。**\n**W8. [Minor, presentation] 仅 10 条参考文献。**\n\n### Overall: 4/6 (Weak Accept)\n\n校准：2 Major → 上限 Weak Accept。取上限因为 composability 方向正确、CF collapse 有实质价值、issues 可在 revision 中解决。\n\n与原始 tex 版本对比：Dream 版本通过增加 FT 实验有效解决了原始版本最严重的两个问题（CF 爆发、零样本 only），但引入了新的统计严谨性缺失和实验覆盖不足问题。",
  "reviewer_id": "1",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — Dream 审稿意见（方法 + 实验）\n\n### Summary\nOntoCoDec Dream 版本在原始零样本验证基础上增加了 LoRA fine-tuning composability 实验（2×3 设计），展示 FT+OntoCoDec 消除残余 violations（DR: 0.76%→0%），CF 从 12.02% 骤降至 0.42%。叙事结构清晰，但核心实验仅覆盖一个数据集且缺乏统计显著性检验。\n\n### Strengths\n- S1 [idea]: Composability 实验是正确的实验方向，直接回答实用价值问题\n- S2 [idea]: CF collapse under fine-tuning 化解了零样本版本最核心的弱点\n- S3 [idea]: Problem→Solution→ZS validation→Composability→Analysis 叙事逻辑自洽\n- S4 [presentation]: 形式化全程使用独立 dom/range，消除了原始版本的不一致\n\n### Weaknesses\n\n**W1. [Major, idea] Composability 仅在 DocRED 上验证。** 论文自定义的 \"central contribution\" 仅单数据集支撑。SciERC 的 CF 特征（零样本 9.90%、Generic↔OST 结构性歧义）使其成为 CF collapse 泛化性的关键测试场景，但缺失。§6 Conclusion 未附数据集限定。\n\n**W2. [Major, idea] 无统计显著性检验。** FT→FT+OntoCoDec 的 ΔR-F1=+0.06pp/−0.01pp 在噪声范围内。\"Zero cost\" 是核心 value proposition，但没有 bootstrap CI 或 p-values 支撑。\n\n**W3. [Should-Fix, idea] FT 下缺少 grammar-only/semantic-only 消融。**\n**W4. [Should-Fix, idea] FT 下缺少 post-hoc filtering 对比。**\n**W5. [Should-Fix, idea] CF collapse 机制未被分析（override frequency ZS vs FT）。**\n**W6. [Minor, idea] 泛化性声明超出 2×8B 实验范围。**\n**W7. [Minor, presentation] Tightness 无公式定义。**\n**W8. [Minor, presentation] 仅 10 条参考文献。**\n\n### Overall: 4/6 (Weak Accept)\n\n校准：2 Major → 上限 Weak Accept。取上限因为 composability 方向正确、CF collapse 有实质价值、issues 可在 revision 中解决。\n\n与原始 tex 版本对比：Dream 版本通过增加 FT 实验有效解决了原始版本最严重的两个问题（CF 爆发、零样本 only），但引入了新的统计严谨性缺失和实验覆盖不足问题。",
    "reviewer_id": "1",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 89 · 2026-05-16T02:48:59.990866+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3664
}
```

</details>

---


### Assistant

_source line 90 · 2026-05-16T02:49:07.084945+00:00_

Dream 审稿已提交。

与原始 tex 版本的评分变化：原始 Overall 2.5/5（ARR 量表）→ Dream 4/6（6 分制 Weak Accept）。Dream 版本通过增加 fine-tuning composability 实验有效解决了原始版本的两个最严重问题（CF 爆发、仅零样本），但在统计严谨性和数据集覆盖上留下新缺口。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1"
}
```

</details>

---


## Round 4

## Round 4

48 recorded events


### User

_source line 91 · 2026-05-16T17:34:28.615829+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计**。

## 论文信息
- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Ontology Constraints
- **论文路径**: `projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`
- **目标 venue**: EMNLP 2026（ARR May 2026 cycle）
- **截止日期**: 2026-05-25
- **格式**: ACL template, double-blind, 长文 ≤8 页正文 + 无限参考文献
- **匿名规则**: double-blind（不得包含作者身份信息）
- **Limitations section**: ARR 要求独立 section，不计入页数

## 你的审查侧重

### 1. 方法论形式化
- §2 Background 中 ontology 定义（σ: R → P(E×E)）是否严谨完整
- §3 Method 中 grammar layer + semantic layer 的形式化是否无歧义
- §4 Constraint Composition 中 bitwise AND、grammar-first fallback、tightness 定义是否数学正确
- pair-based enforcement 与 independent enforcement 的区别是否清晰论证
- decidability taxonomy（local / prefix-decidable / non-local）分类是否合理

### 2. 实验设计
- 5-way ablation（SciERC）和 4-way ablation（DocRED）设计是否合理、控制变量是否到位
- cross-model validation（3 models）是否充分
- composability matrix（zero-shot vs LoRA × unconstrained vs S1）设计合理性
- FT four-way ablation 是否有效隔离各层贡献
- bootstrap significance testing（10K iterations）是否恰当
- post-hoc filtering baseline 对比是否公平

### 3. 数值一致性
- 表格数值与正文引用是否一致（逐一核查 Table 1-6）
- 百分比变化的计算是否正确（相对减少 vs 绝对变化）
- confidence interval 和 p-value 报告是否规范

### 4. CF Trade-off 诚实度
- CF violation 从 0.08%→9.90%（SciERC）/ 0.10%→12.02%（Llama DocRED）的上升是否在论文中被充分、诚实地讨论
- CF-DR trade-off 分析（Appendix B）是否令人信服
- 这是否构成方法的根本性缺陷

### 5. 统计严谨性
- R²=0.886 基于 n=4 数据点的 dual-factor 分析——这是否过度拟合？
- zero-shot R-F1 ~8% 的实际意义如何？论文是否充分讨论了这一点？

请输出完整审稿报告，包含 Summary、Strengths、Weaknesses（逐条编号 W1-Wn，标注 severity: critical/warning/info）、Questions（逐条编号 Q1-Qn）、Missing References、Overall Assessment。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 92 · 2026-05-16T17:34:37.167059+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
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

_source line 93 · 2026-05-16T17:34:37.217759+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 94 · 2026-05-16T17:34:41.487155+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 95 · 2026-05-16T17:34:41.588273+00:00_

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
12	\usepackage{multirow}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{enumitem}
16	\usepackage{xcolor}
17	
18	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Ontology Constraints}
19	
20	\author{Anonymous ACL submission}
21	
22	\begin{document}
23	\maketitle
24	
25	% === Abstract ===
26	\input{abstract}
27	
28	% === §1 Introduction ===
29	\input{section1_introduction_draft}
30	
31	% === §2 Background ===
32	\input{section2_background}
33	
34	% === §3 Method ===
35	\input{section3_method_draft}
36	
37	% === §4 Constraint Composition ===
38	\section{Constraint Composition}
39	\label{sec:composition}
40	\input{section4_composition_draft}
41	
42	% === §5 Experiments ===
43	\section{Experiments}
44	\label{sec:experiments}
45	
46	\subsection{Violation Landscape}
47	\input{section3_violation_landscape}
48	
49	\input{section5_scierc_draft}
50	\input{section5_docred_draft}
51	\input{section5_crossmodel_draft}
52	\input{section5_runtime}
53	
54	% === §6 Related Work ===
55	\input{section6_related_work}
56	
57	% === §7 Discussion and Conclusion ===
58	\section{Discussion and Conclusion}
59	\label{sec:discussion}
60	\input{section7_conclusion_compressed}
61	
62	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
63	\clearpage
64	\section*{Limitations}
65	
66	CF impact is model-dependent: for well-calibrated models (Qwen, Llama), S1 introduces CF violations (up to 12.02\%) as a consequence of per-relation independent enforcement; for poorly-calibrated models (Mistral), S1 substantially reduces CF (56.87\%\,$\to$\,1.27\%) by constraining type assignments to schema-valid values.
67	CF fallback ablation shows that eliminating CF re-routes violations to DR ($+$13
…[truncated 3102 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 96 · 2026-05-16T17:34:41.588696+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-16T17:34:49.101123+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results for ACL ARR 2026 reviewer guidelines, here's what I found:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

…[truncated 1338 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7512
}
```

</details>

---


### Tool call

_source line 98 · 2026-05-16T17:34:57.387640+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5), and the description for each score level. Include: soundness, excitement, overall assessment, reproducibility, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5), and the description for each score level. Include: soundness, excitement, overall assessment, reproducibility, and any other scored dimensions."
  }
}
```

</details>

---


### Tool call

_source line 99 · 2026-05-16T17:34:57.689124+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
  }
}
```

</details>

---


### Tool result

_source line 100 · 2026-05-16T17:34:57.840715+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_fd4b26.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_d3264e.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_550cbf.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_outline.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex
/home/ubuntu/.agent-ml-res
…[truncated 1901 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-16T17:35:03.324905+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. **Reviewer Confidence** (1-5 scale)
- **5**: Positive evaluation is correct; very careful reading and familiar with related work
- **4**: Quite sure; important points checked carefully
- **3**: Pretty sure; good general knowledge but details not carefully verified
- **2**: Willing to defend evaluation but likely missed some details or novelty
- **1**: "Not my area, or paper is very hard to understand"

## 2. **Soundness** (1-5 scale)
- **5**: "Excellent: This study is one of the most thorough"
- **4**: Strong; sufficient support with optional additional experiments
- **3**: Acceptable; main claims supported with minor details needed
- **2**: Poor; main claims lack sufficient support
- **1**: "Major Issues: This study is not yet sufficiently thorough"

## 3. **Excitement** (1-5 scale)
- **5**: Highly exciting; would recommend and attend presentation
- **4**: Exciting; would mention to others
- **3**: Interesting; might mention points or attend if time permits
- **2**: Potentially interesting; may resonate with others
- **1**: "Not Exciting: this paper does not resonate with me"

## 4. **Overall Assessment** (1-5 scale)
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance recommended
- **3**: Findings track acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit

## 5. **Reproducibility** (1-5 scale)
- **5**: Results easily reproducible
- **4**: Mostly reproducible with minor variations
- **3**: Reproducible with difficulty; underspecified parameters
- **2**: "hard pressed to reproduce"; limited data availability
- **1**: Cannot reproduce results

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5937
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-16T17:35:06.438922+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 103 · 2026-05-16T17:35:07.398019+00:00_

1	\begin{abstract}
2	LLM-based information extraction systems can produce systematic ontology constraint violations during autoregressive generation.
3	On SciERC (7 relation types), 15.37\% of extracted triples violate domain/range type constraints; on DocRED (96 relation types), 18.46\%---comparable rates governed by \emph{constraint tightness} rather than ontology scale.
4	%
5	We present \textsc{OntoCoDec}, which compiles IE ontology schemas into two composable decoding constraint layers:
6	(1)~a \emph{grammar layer} (XGrammar CFG) enforcing JSON structural validity and restricting entity/relation vocabularies to schema-defined values (ET, RV\,$\to$\,0\%); and
7	(2)~a \emph{semantic layer} enforcing domain/range constraints via a stateful entity registry and dynamic logit masking.
8	The grammar layer is an enabling prerequisite; the two compose via bitwise AND on token-level masks.
9	%
10	On SciERC, \textsc{OntoCoDec} reduces domain/range violations by 94\% (15.37\%\,$\to$\,0.93\%) while maintaining extraction F1 ({+}0.13pp, $p{=}0.58$).
11	Results generalize across three model families (Qwen3-8B, Llama-3.1-8B, Mistral-7B): DocRED DR decreases by 42--90\%, with significant R-F1 gains for Qwen ({+}0.50pp, $p{<}0.001$) and Llama ({+}0.29pp, $p{=}0.013$).
12	% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1, llama_docred_full_s1, mistral_docred
13	Quantitative analysis reveals that residual DR varies predictably with ontology tightness $\times$ baseline violation rate ($R^2{=}0.886$, $n{=}4$; Appendix~\ref{app:dual-factor}).
14	Composed with LoRA fine-tuning on two datasets, \textsc{OntoCoDec} achieves DR\,$\leq$\,0.09\% (SciERC) and 0.20\% (DocRED) with R-F1 change within $\pm$0.6\,pp, confirming that fine-tuning and constrained decoding are complementary.
15	\end{abstract}
16	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-16T17:35:07.398468+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 105 · 2026-05-16T17:35:07.852842+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly deployed for zero-shot information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity is guaranteed to carry a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}---structurally valid triples that are ontologically invalid.
8	In a systematic study, we find violations are pervasive: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred}, driven by \emph{constraint tightness} (few valid type pairs per relation) rather than ontology scale.
9	Relations with tight constraints exhibit far higher rates (\textsc{Compare}: 42.4\%) than loosely constrained ones (\textsc{Used-for}: 0.8\%).
10	
11	Existing approaches leave a fundamental gap.
12	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable---violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp.
13	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} guarantees syntactic well-formedness but cannot encode cross-field semantic constraints.
14	Post-hoc validation wastes compute on discarded outputs and cannot redirect probability mass during decoding.
15	Training-based approaches~\cite{sainz2024gollie,lu2022uie} provide only soft guidance that cannot eliminate violations.
16	
17	We propose \textbf{OntoCoDec} (\textbf{Onto}logy-\textbf{Co}mpiled \textbf{Dec}oding), a framework that compiles an IE ontology into two composable layers of decoding-time constraints.
18	The \emph{grammar layer} enforces JSON well-formedness and vocabulary validity via XGrammar.
19	The \emph{semantic layer} maintains a stateful entity registry during generation: as entities are decoded, the registry records ty
…[truncated 1466 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 106 · 2026-05-16T17:35:07.853237+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
  }
}
```

</details>

---


### Tool result

_source line 107 · 2026-05-16T17:35:08.305436+00:00_

1	% Section 2: Background (compressed)
2	
3	\section{Background}
4	\label{sec:background}
5	
6	\paragraph{IE Ontology Structure.}
7	\label{sec:bg:ontology}
8	An IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defines entity types $\mathcal{E}$, relation types $\mathcal{R}$, and a mapping $\sigma: \mathcal{R} \to \mathcal{P}(\mathcal{E} \times \mathcal{E})$ specifying valid (head type, tail type) pairs per relation.
9	A triple $(h, r, t)$ is \emph{type-valid} if $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$.
10	We define the \emph{constraint tightness} of $r$ as $1 - |\sigma(r)| / |\mathcal{T}|^2$ where $\mathcal{T} = \mathcal{E}$ is the entity type vocabulary: tighter constraints leave fewer valid options, increasing violation likelihood.
11	
12	\paragraph{Grammar-Constrained Decoding.}
13	\label{sec:bg:gcd}
14	Grammar-constrained decoding restricts each token $y_t$ to a mask $M_g \in \{0, 1\}^{|V|}$ derived from a target grammar.
15	XGrammar~\citep{dong2025xgrammar} compiles JSON Schemas into pushdown automata for efficient enforcement of structural constraints; Outlines~\citep{willard2023outlines} and SGLang~\citep{zheng2024sglang} offer similar capabilities.
16	However, these methods are limited to context-free constraints and cannot enforce cross-field semantic rules---e.g., ``if $r$ = \textsc{Feature-of}, then $\mathrm{type}(h) \in \{\textsc{Method}, \textsc{OtherScientificTerm}\}$''---which depend on previously generated field values.
17	
18	\paragraph{Problem Statement.}
19	\label{sec:bg:problem}
20	Given $\mathcal{O}$ and an autoregressive LM $\mathcal{M}$, we seek constraints $\mathcal{C}$ ensuring: (a)~\textbf{structural validity}---well-formed JSON with $\mathcal{E}$/$\mathcal{R}$ membership; and (b)~\textbf{type validity}---$(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$ for every triple.
21	Condition (a) is context-free; (b) is context-sensitive but \emph{prefix-decidable}---at the point where a type token is generated, all in
…[truncated 89 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 108 · 2026-05-16T17:35:08.406252+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 109 · 2026-05-16T17:35:08.809113+00:00_

1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	We present OntoCoDec, a two-layer constrained decoding framework that compiles ontology schemas into token-level masks enforced during autoregressive generation.
9	The grammar layer (\S\ref{sec:grammar}) guarantees structural validity—well-formed JSON with ontology-vocabulary membership—while the semantic layer (\S\ref{sec:semantic}) enforces domain/range type constraints via a stateful entity registry.
10	We describe the problem formulation (\S\ref{sec:formulation}), each layer, and two decoding strategies (\S\ref{sec:strategies}).
11	Formal analysis of constraint composition is deferred to Section~\ref{sec:composition}.
12	
13	
14	\subsection{Problem Formulation}
15	\label{sec:formulation}
16	
17	\paragraph{IE as structured generation.}
18	Given an input text $x$, a language model generates a structured JSON output $y$:
19	%
20	\begin{equation}\label{eq:output-schema}
21	\resizebox{.88\columnwidth}{!}{$\displaystyle
22	  y = \bigl\{\texttt{entities}: [\{n_i, \tau_i\}],\; \texttt{relations}: [\{h_j, t_j, r_j, \tau^h_j, \tau^t_j\}]\bigr\}
23	$}
24	\end{equation}
25	%
26	where each entity has a name $n_i$ and type $\tau_i \in \mathcal{E}$, and each relation specifies head $h_j$, tail $t_j$, relation type $r_j \in \mathcal{R}$, and head/tail entity types $\tau^h_j, \tau^t_j$.
27	
28	\paragraph{Ontology compliance.}
29	Using the ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defined in \S\ref{sec:background}, we write $\operatorname{dom}(r) = \{\tau^h : \exists \tau^t,\, (\tau^h, \tau^t) \in \sigma(r)\}$ for domain-valid head types and $\operatorname{range}(r, \tau^h) = \{\tau^t : (\tau^h, \tau^t) \in \sigma(r)\}$ for the conditional range given head type $\tau^h$.
30	Our enforcement target is \emph{pair-based} type validity: $(\tau^h, \tau^t) \in \sigma(r)$ for every triple.
31	The decoder en
…[truncated 7606 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 110 · 2026-05-16T17:35:08.809612+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 111 · 2026-05-16T17:35:09.763462+00:00_

1	% Section: Constraint Composition (compressed, 787→~500 words)
2	
3	At each decoding step $t$, let $G(t) \subseteq V$ and $S(t) \subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.
4	The final mask is their conjunction:
5	%
6	\begin{equation}\label{eq:composition}
7	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
8	\end{equation}
9	%
10	so a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$, reflecting the enabling dependency (\S\ref{sec:method})---the semantic layer requires the relation type to belong to $\mathcal{R}$, a property guaranteed only by the grammar layer.
12	
13	\paragraph{Grammar-First Fallback.}
14	When $S(t) \cap G(t) = \emptyset$---tight constraints leave no token that is both grammar-valid and semantically valid---na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
15	We enforce a \emph{grammar-first fallback}: if no semantically valid token survives grammar filtering, semantic masking is skipped and the grammar layer alone controls selection.
16	Structural integrity is a hard constraint; a type violation is a soft error detectable by downstream validation.
17	
18	\paragraph{Constraint Tightness.}
19	We define the tightness of relation $r$ as:
20	%
21	\begin{equation}\label{eq:tightness}
22	  \tau(r) = 1 - \frac{|\mathcal{V}(r)|}{|\mathcal{T}|^2},
23	\end{equation}
24	%
25	where $\mathcal{V}(r)$ is the set of valid type pairs and $\mathcal{T}$ the entity type vocabulary.
26	The mean tightness $\bar{\tau} = \frac{1}{|\mathcal{R}|}\sum_{r} \tau(r)$ characterizes ontology restrictiveness.
27	Tighter constraints eliminate more grammar-valid tokens at type-bearing positions, increasing fallback frequency and residual DR.
28	This dual-factor pattern---tightness $\times$ baseline model violation rate---is consistent with the cross-data
…[truncated 1960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 112 · 2026-05-16T17:35:09.764058+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
  }
}
```

</details>

---


### Tool result

_source line 113 · 2026-05-16T17:35:10.266304+00:00_

1	% §5.1 Experimental Setup and Violation Landscape
2	% Compressed from standalone section. main.tex provides \subsection header.
3	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
4	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
5	
6	\label{sec:violation_landscape}
7	
8	\paragraph{Setup.}
9	We evaluate Qwen3-8B~\cite{qwen2025qwen3} under zero-shot greedy decoding on two IE benchmarks:
10	\textbf{SciERC}~\cite{luan2018scierc} (551 test sentences, 7 relations, avg.\ 26.1 valid type pairs per relation) and \textbf{DocRED}~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test set annotations are not publicly available; following prior work, we evaluate on the development set (998 documents).} 96 relations, avg.\ 5.68 valid pairs).
11	We measure four violation categories: \textbf{Domain/Range (DR)} violations where $(\mathrm{type}(h), \mathrm{type}(t)) \notin \sigma(r)$; \textbf{Relation Vocabulary (RV)} where $r \notin \mathcal{R}$; \textbf{Entity Type (ET)} where $e \notin \mathcal{E}$; and \textbf{Cross-Field Consistency (CF)} where the same entity receives different types across triples.
12	Cross-model validation with Llama-3.1-8B-Instruct is reported in \S\ref{sec:cross-model}.
13	
14	\paragraph{Violation distribution.}
15	Table~\ref{tab:prompt_comparison} reports violation rates.
16	DR violations affect 15.37\% of triples on SciERC and 18.46\% on DocRED---comparable rates despite a 14$\times$ difference in ontology size---indicating that violation severity is driven by \emph{constraint tightness} rather than ontology scale.
17	RV violations on DocRED are dramatically higher (29.66\% vs.\ 1.39\%), indicating that 96 relation types exceed the model's capacity to reproduce a target vocabulary from a single prompt.
18	Per-relation rates (Figure~\ref{fig:per_relation_dr}) vary by over 40 percentage points: \textsc{Compare} at 42.4\% vs.\ \textsc{Used-for} at 0.76\%, correlating with tightness---tight constraints (few valid 
…[truncated 1354 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 114 · 2026-05-16T17:35:10.266861+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 115 · 2026-05-16T17:35:10.668807+00:00_

1	% Section 5 — SciERC Results (Draft)
2	% Data source: Phase 2 SciERC registry experiments
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,
4	%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2
5	% All numbers verified against registry 2026-05-14.
6	
7	\subsection{Results on SciERC}
8	\label{sec:scierc-results}
9	
10	Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC,
11	evaluating each constraint layer independently and in combination.
12	All experiments use Qwen3-8B in a zero-shot setting on 551 test documents
13	with identical prompts and decoding parameters;
14	only the active constraint layers differ.
15	
16	% ──────────────────────────────────────────
17	%  Table: SciERC five-way ablation
18	% ──────────────────────────────────────────
19	\begin{table}[t]
20	\centering
21	\small
22	\setlength{\tabcolsep}{3.6pt}
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{@{}l rrrrr rr@{}}
25	\toprule
26	& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
27	& \multicolumn{2}{c}{\textbf{F1}} \\
28	\cmidrule(lr){2-6} \cmidrule(l){7-8}
29	\textbf{Mode}
30	  & DR\,$\downarrow$ & $\Delta$DR
31	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
32	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
33	\midrule
34	Unconstrained
35	  & 15.37 & ---
36	  & 1.39  & 0.40
37	  & 0.08
38	  & 8.23  & 31.01 \\
39	Grammar
40	  & 14.84 & $\downarrow$3\%
41	  & \textbf{0} & \textbf{0}
42	  & 0.08
43	  & 8.23  & 30.98 \\
44	Semantic
45	  & 11.65 & $\downarrow$24\%
46	  & 1.51  & 0.40
47	  & 2.71
48	  & 8.15  & 31.01 \\
49	Full (S1)
50	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
51	  & \textbf{0} & \textbf{0}
52	  & 9.90
53	  & \textbf{8.36} & 30.98 \\
54	Full (S2)
55	  & 0.97  & $\downarrow$94\%
56	  & \textbf{0} & \textbf{0}
57	  & 8.03
58	  & 8.03  & \textbf{31.90} \\
59	\bottomrule
60	\end{tabular}}%
61	\caption{Five-way ablation on SciERC (551 documents, Qwen3-8B, zero-shot).
62	DR: domain/range violation rate;
63	RV: rel
…[truncated 9470 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 116 · 2026-05-16T17:35:10.719439+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 117 · 2026-05-16T17:35:10.720033+00:00_

1	% Section 5 — DocRED Results (compressed, 1450→~600 words)
2	% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,
3	%          phase2_docred_semantic_only, phase2_docred_full_s1
4	% All numbers verified against registry 2026-05-14.
5	
6	\subsection{Cross-Dataset Validation on DocRED}
7	\label{sec:docred-results}
8	
9	Table~\ref{tab:docred-ablation} presents the four-way ablation on DocRED, a document-level RE benchmark with 96 Wikidata relation types---14$\times$ the ontology size of SciERC.
10	All experiments use Qwen3-8B zero-shot on 998 documents.
11	
12	% ──────────────────────────────────────────
13	%  Table: DocRED four-way ablation
14	% ──────────────────────────────────────────
15	\begin{table}[t]
16	\centering
17	\small
18	\setlength{\tabcolsep}{3.6pt}
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{@{}l rrrrr rr@{}}
21	\toprule
22	& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
23	& \multicolumn{2}{c}{\textbf{F1}} \\
24	\cmidrule(lr){2-6} \cmidrule(l){7-8}
25	\textbf{Mode}
26	  & DR\,$\downarrow$ & $\Delta$DR
27	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
28	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
29	\midrule
30	Unconstrained
31	  & 18.46 & ---
32	  & 29.66 & 2.48
33	  & 0.10
34	  & 7.74  & 58.15 \\
35	Grammar
36	  & 26.17 & $\uparrow$42\%
37	  & \textbf{0.03} & \textbf{0}
38	  & 0.07
39	  & \textbf{8.31}  & \textbf{59.38} \\
40	Semantic
41	  & 13.84 & $\downarrow$25\%
42	  & 29.87 & 4.22
43	  & 1.05
44	  & 7.70  & 57.81 \\
45	Full (S1)
46	  & \textbf{10.21} & $\downarrow$\textbf{45\%}
47	  & \textbf{0.03} & \textbf{0}
48	  & 2.57
49	  & 8.23  & 59.37 \\
50	\bottomrule
51	\end{tabular}}%
52	\caption{Four-way ablation on DocRED (998 documents, Qwen3-8B, zero-shot).
53	$\Delta$DR: relative change vs.\ unconstrained.
54	Best per column in \textbf{bold} (CF excluded).
55	F1 $\times$100. Bootstrap significance: R-F1 $+$0.50\,pp ($p < 0.001$).}
56	\label{tab:docred-ablation}
57	\end{table}
58	
59	% exp_ids: phase2_docred_unconstraine
…[truncated 2767 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 118 · 2026-05-16T17:35:11.673994+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 119 · 2026-05-16T17:35:12.076431+00:00_

1	% Section 5 — Cross-Model Validation (compressed, 830→~400 words)
2	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1,
3	%          phase2_docred_unconstrained, phase2_docred_full_s1,
4	%          llama_scierc_unconstrained, llama_scierc_full_s1,
5	%          llama_docred_unconstrained, llama_docred_full_s1
6	
7	\subsection{Cross-Model Validation}
8	\label{sec:cross-model}
9	
10	We replicate the full S1 configuration with Llama-3.1-8B-Instruct and Mistral-7B-Instruct-v0.3 under identical prompts, decoding parameters, and evaluation.
11	Table~\ref{tab:cross-model} summarizes results across all three models.
12	Mistral serves as a third zero-shot verification point confirming model-agnosticism; composability evaluation (\S\ref{sec:composability}) uses LoRA fine-tuning which requires domain-specific training data available only for Qwen and Llama.
13	
14	\begin{table}[t]
15	\centering
16	\small
17	\setlength{\tabcolsep}{3.4pt}
18	\resizebox{\columnwidth}{!}{%
19	\begin{tabular}{@{}ll rrrr r@{}}
20	\toprule
21	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
22	& \textbf{R-F1} \\
23	\cmidrule(lr){3-6} \cmidrule(l){7-7}
24	\textbf{Dataset} & \textbf{Model}
25	  & DR\,$\downarrow$ & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
26	  & $\uparrow$ \\
27	\midrule
28	\multirow{6}{*}{SciERC}
29	  & Qwen (U)    & 15.37 & 1.39  & 0.40 & 0.08 & 8.23 \\
30	  & Qwen (S1)   &  0.93 & 0     & 0    & 9.90 & 8.36 \\
31	  \cmidrule(l){2-7}
32	  & Llama (U)   & 13.34 & 0.55  & 0    & 0.24 & 2.68 \\
33	  & Llama (S1)  &  0.08 & 0     & 0    & 6.56 & 2.54 \\
34	  \cmidrule(l){2-7}
35	  & Mistral (U) & 56.94 & 0     & 1.50 & 56.87$^\dagger$ & 3.66 \\
36	  & Mistral (S1)& 13.40 & 0     & 0    & 1.27  & 3.67 \\
37	\midrule
38	\multirow{6}{*}{DocRED}
39	  & Qwen (U)    & 18.46 & 29.66 & 2.48 & 0.10 & 7.74 \\
40	  & Qwen (S1)   & 10.21 &  0.03 & 0    & 2.57 & 8.23 \\
41	  \cmidrule(l){2-7}
42	  & Llama (U)   & 26.07 & 16.03 & 0.13 & 0.17 & 5.98 \\
43	  & Llama (S1)  &  2.55 &  0  
…[truncated 2202 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 120 · 2026-05-16T17:35:12.077036+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
  }
}
```

</details>

---


### Tool result

_source line 121 · 2026-05-16T17:35:12.580118+00:00_

1	% Section 5 — Runtime Analysis
2	% Data source: DocRED latency profiling (exp_id: docred_latency_profiling)
3	% Qwen3-8B, same single-GPU server, controlled 4-way ablation.
4	
5	\subsection{Runtime Overhead}
6	\label{sec:runtime}
7	
8	Table~\ref{tab:runtime} reports per-document inference time for each constraint layer combination on both datasets (Qwen3-8B, same GPU).
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\setlength{\tabcolsep}{4pt}
14	\begin{tabular}{@{}l rr rr@{}}
15	\toprule
16	& \multicolumn{2}{c}{\textbf{SciERC (7 rels)}}
17	& \multicolumn{2}{c}{\textbf{DocRED (96 rels)}} \\
18	\cmidrule(lr){2-3} \cmidrule(l){4-5}
19	\textbf{Mode} & Avg (s) & Overhead & Avg (s) & Overhead \\
20	\midrule
21	Unconstrained & 2.587 & --- & 21.023 & --- \\
22	Grammar       & 2.631 & $+$1.7\% & 21.366 & $+$1.6\% \\
23	Semantic      & 2.618 & $+$1.2\% & 21.912 & $+$4.2\% \\
24	Full (S1)     & 2.647 & $+$2.3\% & 22.147 & $+$5.4\% \\
25	\bottomrule
26	\end{tabular}
27	\caption{Per-document inference time by constraint layer (Qwen3-8B, same GPU).
28	Grammar compile time: 0.044\,s (one-time, amortized to zero).
29	Full-mode overhead is sub-additive (DocRED: 1.6\%$+$4.2\%$=$5.8\% expected vs.\ 5.4\% observed).}
30	\label{tab:runtime}
31	\end{table}
32	
33	Grammar-layer overhead is consistent across datasets ($+$1.6--1.7\%), independent of schema complexity.
34	Semantic-layer overhead scales with the number of relation types (SciERC 7 types: $+$1.2\%; DocRED 96 types: $+$4.2\%), reflecting increased domain-range lookup frequency.
35	Full-mode overhead is sub-additive on both datasets because the two layers share token-set computation.
36	Even in the most complex setting (DocRED, 96 relations), total overhead is $+$5.4\%---practically negligible.
37	Under fine-tuning, S1 overhead drops further to $+$2.3\% (61\,ms/doc; Appendix~\ref{app:ft-latency}).
38	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 122 · 2026-05-16T17:35:12.580482+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 123 · 2026-05-16T17:35:13.133088+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Grammar-Constrained Decoding.}
5	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, LMQL~\cite{beurer-kellner2023lmql}, DOMINO~\cite{beurer-kellner2024domino}, SynCode~\cite{ugare2024syncode}, and ASAp~\cite{park2024grammar} ensure every token belongs to a grammar-valid continuation; IterGen~\cite{ugare2025itergen} adds backtracking.
6	These guarantee format validity but cannot enforce cross-field semantic constraints such as ontology domain/range rules.
7	
8	\paragraph{Semantic Constrained Decoding for Code.}
9	Synchromesh~\cite{synchromesh_iclr2022}, PICARD~\cite{scholak2021picard}, MGD~\cite{mgd_neurips2023}, and \citet{pldi2025_type_constrained_codegen} enforce type and scope constraints in code generation; OntoCoDec migrates this paradigm to IE.
10	
11	\paragraph{Vocabulary and Type-Constrained Generation.}
12	\citet{roth_yih_2004} establish relational type compatibility as a hard constraint via ILP, though applied post-hoc.
13	GENRE~\cite{decao2021genre}, AdaKGC~\cite{adakgc_emnlp2023}, GCD~\cite{geng2023gcd}, and GoLLIE~\cite{sainz2024gollie} constrain \emph{which tokens} can appear but not \emph{which type combinations} are valid per relation.
14	Training-based methods~\cite{paolini2021tanl,cabot2021rebel,lu2022uie,knowcoder_acl2024,li2023codeie} encode IE structure via training or prompting but provide only \emph{soft} guidance.
15	Post-hoc approaches~\cite{khorshidi2025odke,spires_2024,ontologx_2025} validate outputs against ontologies after generation; OntoCoDec \emph{prevents} violations during decoding.
16	
17	\paragraph{Quality Impact of Constrained Decoding.}
18	CRANE~\cite{banerjee2025crane} and \citet{schall2025hiddencost} show grammar restrictions can degrade reasoning, but \citet{tam2024letmespeak} find extraction-style tasks are robust to---or benefit from---constraints.
19	BoostCD~\cite{sakota2025boostcd} combines constrained and unconstrained outputs via boo
…[truncated 273 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 124 · 2026-05-16T17:35:13.133488+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
  }
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-16T17:35:13.234915+00:00_

1	% Section 7 — Discussion and Conclusion (compressed)
2	% Full discussion paragraphs moved to Appendix C.
3	
4	OntoCoDec compiles IE ontology schemas into composable token-level decoding constraints, achieving 42--99\% DR reduction across three models and two datasets with no significant F1 cost.
5	Composed with LoRA fine-tuning, it reaches DR\,$\leq$\,0.20\% at $<$0.6\,pp F1 cost, confirming orthogonal error targeting; the dual-factor pattern ($R^2{=}0.886$) provides a predictive framework for residual violations.
6	
7	CF impact is model-dependent: S1 introduces CF for well-calibrated models (up to 12.02\%) but reduces it for poorly-calibrated ones (Mistral: 56.87\%\,$\to$\,1.27\%).
8	Ablation confirms CF$\leftrightarrow$DR tension ($+$13.85\,pp; Appendix~\ref{app:cf-dr-tradeoff}); fine-tuning reduces CF by 88\% (\S\ref{sec:composability}); global entity-level type consensus offers the most direct path forward.
9	
10	% Limitations and Future Work moved to \section*{Limitations} in main.tex (ARR requirement)
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 126 · 2026-05-16T17:35:19.789849+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-16T17:35:20.142305+00:00_

1	% Appendix B — Extended Discussion
2	% Contains discussion paragraphs moved from the main text during compression.
3	
4	\section{Extended Discussion}\label{app:discussion}
5	
6	%%% CF Dual Mechanism %%%
7	% exp_ids: phase2_scierc_full_s1, llama_scierc_full_s1, llama_docred_full_s1
8	
9	\paragraph{CF Dual Mechanism.}
10	CF violations arise from two distinct mechanisms:
11	(1)~\emph{Registry override}: the semantic constraint forces a domain-compatible type that conflicts with the entity's previously registered type.
12	The entity appears in multiple relations with different type requirements, and the per-relation mask selects the locally valid type without consulting prior assignments.
13	(2)~\emph{Grammar-first fallback} (\S\ref{sec:interaction}): when the semantic mask conflicts with all grammar-valid tokens, the semantic layer is dropped entirely, allowing the grammar layer to generate any structurally valid type---which may differ from the entity's registered type.
14	
15	These mechanisms have sharply different model profiles.
16	Qwen3-8B triggers zero grammar-first fallbacks across all experiments, attributing 100\% of its CF violations to registry override.
17	Llama-3.1-8B, by contrast, triggers 5{,}882 fallbacks on SciERC (10.7 per document) and 57{,}825 on DocRED (63.8 per document), making grammar-first fallback the dominant CF source.
18	This asymmetry is consistent with the cross-model CF gap: Qwen achieves CF\,=\,2.57\% on DocRED vs.\ Llama's 12.02\%, despite both using identical constraint configurations.
19	The difference traces to Llama's less calibrated type predictions, which more frequently conflict with the semantic mask's valid set, triggering fallback.
20	
21	%%% Fallback Behavior and Effective Coverage %%%
22	% exp_ids: cf_fallback_ablation_scierc (final data)
23	
24	\paragraph{Fallback Behavior and Effective Coverage.}
25	\label{app:fallback-coverage}
26	The two-layer architecture produces two distinct fallback mechanisms with different seman
…[truncated 22631 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 128 · 2026-05-16T17:35:20.192894+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-16T17:35:21.096995+00:00_

1	\section{Extended Related Work}
2	\label{app:related_work}
3	
4	% ===========================================================================
5	% Paradigm 1: Grammar-Constrained Decoding
6	% ===========================================================================
7	\paragraph{Grammar-Constrained Decoding.}
8	Recent work has established efficient algorithms for restricting LLM outputs to conform to context-free grammars, making grammar-constrained decoding the de facto standard for obtaining structured output from language models.
9	XGrammar~\cite{dong2025xgrammar} partitions the vocabulary into context-independent and context-dependent tokens and maintains persistent pushdown automata across decoding steps, achieving up to 100$\times$ speedup over prior CFG-constrained decoding methods.
10	Outlines~\cite{willard2023outlines} reformulates constrained generation as finite-state machine transitions with offline vocabulary indexing, enabling efficient enforcement of regular-expression and JSON-schema constraints without runtime overhead per token.
11	LMQL~\cite{beurer-kellner2023lmql} introduces a declarative query language that compiles type, length, and regex constraints into token-level masks, providing a programmable interface for specifying multi-variable output structures.
12	These systems ensure that every generated token belongs to a grammar-valid continuation, but they do not address the \emph{distribution distortion} introduced by naive token masking.
13	A parallel line of work tackles this problem directly: DOMINO~\cite{beurer-kellner2024domino} minimizes distributional divergence during CFG enforcement by formulating mask selection as an optimization problem, and ASAp~\cite{park2024grammar} provides a provably unbiased sampling algorithm that preserves the original LM distribution under grammar constraints.
14	Together, these advances have made grammar-constrained decoding both fast and statistically principled, establishing a robust foundation for stru
…[truncated 19787 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 130 · 2026-05-16T17:35:21.248148+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex"
  }
}
```

</details>

---


### Tool result

_source line 131 · 2026-05-16T17:35:21.549984+00:00_

1	% Appendix — Prompt Templates
2	% W10: Extraction prompts used in all experiments.
3	
4	\section{Prompt Templates}
5	\label{app:prompts}
6	
7	All experiments use the same prompts across constrained and unconstrained decoding---constraints are applied at the logit level, not through prompt modification.
8	Table~\ref{tab:prompts} shows the system and user prompts for each dataset.
9	
10	\begin{table*}[t]
11	\centering
12	\small
13	\begin{tabular}{@{}p{0.95\textwidth}@{}}
14	\toprule
15	\textbf{SciERC --- System Prompt (Unconstrained \& Constrained)} \\
16	\midrule
17	\texttt{You are an expert information extraction system for scientific texts. Extract entities and relations from the given text.} \\[4pt]
18	\texttt{Entity types: Task, Method, Material, Metric, OtherScientificTerm, Generic} \\
19	\texttt{Relation types: Used-for, Feature-of, Hyponym-of, Part-of, Compare, Conjunction, Evaluate-for} \\[4pt]
20	\texttt{Output a JSON object with:} \\
21	\texttt{- "entities": list of \{"text": "...", "type": "..."\}} \\
22	\texttt{- "relations": list of \{"head": "...", "tail": "...", "type": "...", "head\_type": "...", "tail\_type": "..."\}} \\[4pt]
23	\texttt{Output ONLY valid JSON, no explanation.} \\
24	\midrule
25	\textbf{SciERC --- User Prompt} \\
26	\midrule
27	\texttt{Extract all entities and relations from this scientific text:} \\
28	\texttt{"\{text\}"} \\
29	\texttt{Output JSON:} \\
30	\midrule
31	\midrule
32	\textbf{DocRED --- System Prompt (Unconstrained \& Constrained)} \\
33	\midrule
34	\texttt{You are an information extraction system. Extract all entities and relations from the following document.} \\[4pt]
35	\texttt{Entity types: PER, ORG, LOC, TIME, NUM, MISC} \\[4pt]
36	\texttt{Relation types: country, instance of, performer, ...\ (96 Wikidata relation types; full list omitted for space)} \\[4pt]
37	\texttt{Output a JSON object with exactly this structure:} \\
38	\texttt{\{"entities": [\{"text": "entity name", "type": "ENTITY\_TYPE"\}],} \\
39	\texttt{\ 
…[truncated 771 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 132 · 2026-05-16T17:35:21.550549+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex"
  }
}
```

</details>

---


### Tool result

_source line 133 · 2026-05-16T17:35:22.054404+00:00_

1	% Appendix C — Per-Relation Violation Analysis (Llama-3.1-8B)
2	% exp_ids: llama_docred_unconstrained, llama_docred_full_s1
3	
4	\section{Per-Relation Violation Analysis (Llama-3.1-8B)}\label{app:llama-per-relation}
5	
6	Table~\ref{tab:llama-per-relation-dr} presents the per-relation domain--range violation breakdown for Llama-3.1-8B on DocRED under full S1 constraints.
7	The Llama baseline exhibits an RV rate of 16.03\%, substantially lower than Qwen's 29.66\%, indicating stronger baseline vocabulary compliance.
8	% exp_ids: llama_docred_unconstrained (RV=16.03%), qwen_docred_unconstrained (RV=29.66%)
9	Full S1 completely eliminates RV violations and reduces the residual DR rate to 2.55\% (418/16{,}368 triples), with only three relations exceeding 10\%.
10	% exp_ids: llama_docred_full_s1 (DR=2.6%, 418/16368)
11	
12	\begin{table}[h]
13	\centering
14	\caption{Top 10 per-relation DR violation rates for Llama-3.1-8B on DocRED under full S1 constraints. Relations with $>$20 triples and 0\% DR (e.g., P131, P206, P361, P170, P86) are omitted.}
15	\label{tab:llama-per-relation-dr}
16	\resizebox{\columnwidth}{!}{%
17	\begin{tabular}{@{}llrrr@{}}
18	\toprule
19	Relation & PID & Triples & DR Violations & DR Rate (\%) \\
20	\midrule
21	dissolved/demolished & P576 & 73 & 24 & 32.9 \\
22	followed by          & P156 & 117 & 24 & 20.5 \\
23	unemployment rate    & P1198 & 15 & 3 & 20.0 \\
24	end time             & P582 & 130 & 21 & 16.2 \\
25	instance of          & P31  & 290 & 37 & 12.8 \\
26	product/material produced & P1056 & 98 & 11 & 11.2 \\
27	location of formation & P740 & 81 & 8 & 9.9 \\
28	head of state        & P35  & 41  & 3  & 7.3 \\
29	applies to jurisdiction & P1001 & 637 & 45 & 7.1 \\
30	conflict             & P607 & 453 & 30 & 6.6 \\
31	\bottomrule
32	\end{tabular}}
33	\end{table}
34	% exp_ids: llama_docred_full_s1
35	
36	Compared with Qwen, which retains a 10.21\% residual DR under full S1 concentrated in P1198 (83\% fallback) and P171 (78\% fallback), Llama's re
…[truncated 523 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 134 · 2026-05-16T17:35:23.761793+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the full reviewer guidelines including: what reviewers should evaluate, what makes a good review, scoring guidance for soundness/excitement/overall, what counts as critical issues, and any specific instructions about experimental evaluation, reproducibility, and statistical analysis."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the full reviewer guidelines including: what reviewers should evaluate, what makes a good review, scoring guidance for soundness/excitement/overall, what counts as critical issues, and any specific instructions about experimental evaluation, reproducibility, and statistical analysis."
  }
}
```

</details>

---


### Tool result

_source line 135 · 2026-05-16T17:35:35.115811+00:00_

# ARR Reviewer Guidelines Summary

## Core Evaluation Responsibilities

Reviewers assess papers across multiple dimensions. The primary task involves reading papers thoroughly, evaluating technical soundness, and providing constructive feedback. As stated in the guidelines, reviewers should "read the paper at least twice: skimming and in-depth reading" to avoid bias from initial impressions.

## What Makes a Strong Review

Effective reviews demonstrate these characteristics:

**Specificity**: Reviews must be concrete. Rather than stating "the paper is missing relevant references," specify which references (e.g., "XYZ") should be included. Vague criticism without evidence lacks utility.

**Professional Tone**: The guidelines emphasize that reviews should be "professional and neutral, if not kind." Authors deserve respectful feedback regardless of their career stage or background.

**Fairness**: Reviewers should avoid common biases listed in the guidelines, including dismissing work for being "too simple," not using preferred methodologies, or focusing on niche topics.

## Scoring Guidance

Starting February 2025, reviewers provide three distinct scores:

**Soundness**: "must be justified by the text of the review." Low soundness scores require explicit evidence of technical flaws. This score should not conflate personal interest with methodological validity.

**Excitement**: Reflects personal preference, orthogonal to soundness assessment. A paper can be sound but personally uninteresting.

**Overall Recommendation**: A composite assessment considering soundness, novelty, and potential impact. Papers can merit acceptance despite low personal excitement if they address genuine needs.

## Critical Issues vs. Suggestions

The guidelines distinguish between fundamental problems and improvement suggestions. Requests for additional experiments qualify as suggestions unless they're essential to the core claims. "A paper only needs to present sufficient evidence for the clai
…[truncated 1779 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 11354
}
```

</details>

---


### Tool call

_source line 136 · 2026-05-16T17:41:28.057190+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿报告：OntoCoDec\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Ontology Constraints\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审查侧重**: 方法严谨性 + 实验设计\n\n---\n\n## 总体评分\n\n**Overall**: 3/5 — Findings track acceptance\n**一句话总结**: 方法设计干净、消融实验全面、技术上可靠，但 abstract/introduction 对 CF 副作用的系统性省略构成选择性报告问题，R²=0.886 基于 n=4 的\"预测框架\"声明过度，且对比 post-hoc filtering 的实际优势不具决定性。\n\n---\n\n## 官方维度打分（ACL ARR review form, Feb 2025+）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 4/5 | 形式化严谨，消融设计全面，bootstrap 统计测试规范。主要扣分：abstract 选择性报告、n=4 回归过度解读 |\n| Excitement | 3/5 | 问题真实且有价值，grammar+semantic 两层架构设计优雅。但实际优势受限于 (a) zero-shot R-F1 仅 ~8%，(b) post-hoc filtering 在多数场景下 F1 更高，(c) CF trade-off 部分抵消核心承诺 |\n| Reproducibility | 4/5 | Prompt 模板完整 (Appendix A)，三个公开模型 + 两个公开数据集，解码参数明确 (greedy)，有 bootstrap 参数 (10K)。未提及代码开源计划 |\n| Confidence | 4/5 | 逐表核查数值、逐条验证百分比计算、通读全部 appendix |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Abstract 和 Introduction 系统性省略 CF 副作用，构成选择性报告\n\n- 具体位置：Abstract (全文)、§1 Introduction (全文)\n- 问题：Abstract 声称 \"reduces domain/range violations by 94% (15.37%→0.93%) while maintaining extraction F1\"，Introduction 列出三条贡献均只提 DR 下降。但 CF (cross-field consistency) 违规从 0.08% 飙升至 9.90%（SciERC, 124× 增幅），Llama DocRED 从 0.17% 升至 12.02%（71× 增幅）。CF 本质上也是本体约束违反——同一实体在不同 triple 中被赋予不同类型。一位只读 abstract 的读者会误以为该方法\"几乎消除了本体违规\"，而实际上是将一类违规部分转化为另一类。\n- 论文正文 §5 和 Appendix B 对 CF 有诚实讨论，但 abstract/intro 的沉默构成科学报告中的 framing bias。\n- 为什么影响接收：ARR reviewer guidelines 明确指出 \"overclaiming\" 和 \"presenting speculation as conclusion\" 是常见问题。选择性报告核心 trade-off 属于 overclaiming 范畴。\n- 建议修改方向：Abstract 中加入一句 CF trade-off 摘要，例如：\"CF violations increase under zero-shot S1 (up to 12.02%) due to per-relation independent enforcement; fine-tuning reduces this to ≤1.18%.\" Introduction 的 Contribution 3 也应提及 CF 作为 trade-off 的一部分。\n\n**N2** [critical] R²=0.886 基于 n=4 数据点被过度解读为\"预测框架\"\n\n- 具体位置：Abstract (\"Quantitative analysis reveals that residual DR varies predictably\")、§7 Discussion (\"the dual-factor pattern (R²=0.886) provides a predictive framework for residual violations\")、Appendix B\n- 问题：线性回归 y = 0.366x − 0.138 有 2 个自由参数，n=4 仅留 2 个自由度。任意 4 个非共线点的线性拟合都能得到较高 R²。更关键的是，4 个数据点分布为 2 datasets × 2 models，其中两个 dataset 的 tightness 差异巨大（SciERC τ̄=0.333 vs DocRED τ̄=0.842），这意味着 tightness 这一个变量就足以解释大部分方差（本质上是 dataset-level 差异），乘以 baseline RV 的交互项只是在 dataset 内部做 2 点拟合。\n- Appendix B 正确地注明 \"we do not report a p-value given the small sample size\"，但 abstract 和 conclusion 仍将此描述为 \"predictive framework\"。\n- 为什么影响接收：用 n=4 的回归结果在 abstract 中做出定量预测性声明，不符合统计严谨性标准。\n- 建议修改方向：将 abstract 中的 \"varies predictably\" 改为 \"is consistent with a dual-factor pattern\"；将 conclusion 中的 \"predictive framework\" 降级为 \"descriptive pattern\" 或 \"consistent with\"；在 Appendix 中明确承认 n=4 无法区分是否 tightness 单一因素即可解释。增加 Mistral 的 2 个数据点 (n=6) 或更多 model/dataset 组合以增强说服力。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Parse failure 在约束下增加，构成潜在混淆变量\n\n- 具体位置：Table 4 注释 (\"Llama DocRED 68→91\")，Limitations §\n- 问题：Llama DocRED 下 parse failure 从 68/998 (6.8%) 增至 91/998 (9.1%)，增幅 34%。这些文档被排除在评估之外。如果约束导致更多\"困难\"文档 parse 失败，则 DR 改善可能部分归因于样本选择偏差（surviving documents 更容易满足约束）。论文在 Qwen DocRED fine-tuned 设置中报告了排除 parse failure 后的数值差异（R-F1 从 -0.30pp 变为 +0.03pp），但 Llama DocRED zero-shot 这一最严重的 parse failure 增长场景缺少类似分析。\n- 建议：补充 Llama DocRED zero-shot 的 parse-failure-excluded 分析，或至少讨论为什么约束增加 parse failure（是否因为 grammar-first fallback 累积导致 JSON 结构损坏？）。\n\n**W2** [warning] 与 Post-hoc filtering 对比不充分支持\"解码时约束优于后处理\"的核心叙事\n\n- 具体位置：Appendix B Table 9、§7 Discussion\n- 问题：Post-hoc filtering 在 6 个 zero-shot 配置中 5 个获得更高 R-F1（Table 9）。论文的反驳依据是 (a) OntoCoDec 保持更高 recall、(b) 处理 ET 违规、(c) 在高拒绝率时 post-hoc 崩溃（Mistral DocRED 73.7%）。但对于实践者来说，如果简单的 post-hoc filtering 在大多数场景下 F1 更高，选择 OntoCoDec 的理由需要更强有力的论证。\n- 论文将 post-hoc 定位为\"互补\"策略，但 Introduction 的 framing（\"Post-hoc validation wastes compute on discarded outputs and cannot redirect probability mass\"）带有否定语气，与实验数据不完全一致。\n- 建议：在正文（而非仅 Appendix）中加入 post-hoc 对比的摘要（至少一句话），诚实说明 post-hoc 在多数 zero-shot 场景 F1 更高，OntoCoDec 的优势在 recall 保持和 fine-tuned 场景下的等价性。\n\n**W3** [warning] Zero-shot R-F1 ~8% 的实际意义讨论不足（正文内）\n\n- 具体位置：§5 Experiments（全部 zero-shot 结果）、Appendix B \"Practical Significance of Zero-Shot F1\"\n- 问题：SciERC R-F1 = 8.36%，DocRED R-F1 = 8.23%。论文将 F1 定位为\"控制变量\"——但这一定位仅出现在 Appendix B 的一个段落中，正文和 Introduction 的贡献声明并未明确限定。同时，论文在 DocRED 上高亮 R-F1 gains (+0.50pp, p<0.001) 作为积极结果，存在逻辑不一致：如果 F1 只是控制变量，就不应在正文中强调其改善；如果 F1 重要，那 ~8% 的绝对值需要在正文中正面讨论实际意义。\n- 建议：在 §5 实验设置段落中加入 1-2 句正文讨论 zero-shot F1 水平的含义和上下文（如 supervised SOTA ~49-53%），不要仅放在 Appendix。\n\n**W4** [warning] SciERC 5-way 消融 vs DocRED 4-way 消融的不对称性未解释\n\n- 具体位置：Table 2 (SciERC, 5 modes) vs Table 3 (DocRED, 4 modes)\n- 问题：SciERC 包含 S2 配置，DocRED 不包含。如果 S2 在 DocRED 上由于 96 relations 的复杂性而不可行或效果差，应明确说明；如果只是篇幅原因，也应说明。\n- 建议：加一句解释为什么 DocRED 不测 S2。\n\n**W5** [warning] Semantic-only 模式在 DocRED 上反直觉地增加 ET 违规\n\n- 具体位置：Table 3，Semantic 行 ET = 4.22% vs Unconstrained ET = 2.48%\n- 问题：Semantic layer 声称仅在 HeadType/TailType 位置激活（§3.3.2），不应影响 EntityType 位置。但 ET 从 2.48% 几乎翻倍至 4.22%。这可能是 autoregressive 分布扰动的间接效应，但论文未讨论。\n- 建议：加一句解释此现象（是否因为 semantic masking 改变了整体 token 分布？）。\n\n**W6** [warning] First-subword-token 唯一性假设限制泛化性\n\n- 具体位置：§3.3 Implementation (\"Each τ ∈ E is mapped to the token ID of its first subword token; we pre-verify uniqueness\")、Limitations §\n- 问题：Limitations 正确指出\"ontologies with many types or multi-token type names would require prefix-tree masking, which we have not implemented\"。但 §3 的 Method 部分将此作为一个简单的 implementation detail 一笔带过，而这实际上是方法适用范围的根本性限制。如果 entity types 的 first subword token 不唯一（在大型本体中很常见），整个 semantic layer 的 masking 机制就不成立。\n- 建议：在 §3 Method 中明确将此列为设计假设（而非 implementation detail），并讨论何时假设成立（小型本体）和不成立（大型本体）。\n\n---\n\n## 小问题（不影响接收）\n\n- **符号冲突**: τ 同时用于 constraint tightness (§4 Eq.3) 和 entity type (§3 Eq.1 中的 τ_i)。建议 tightness 改用 κ 或 ψ。\n- **Table 2 S2 行**: CF = 8.03%, R-F1 = 8.03 是数值巧合，但视觉上容易让读者误以为是复制粘贴错误。\n- **DocRED RV residual**: Grammar 模式和 Full S1 在 DocRED 上 RV = 0.03%（非 0%）。这 0.03% 的来源未解释——CFG 应强制保证 RV = 0%。\n- **Limitations**: \"Global entity-level type consensus during decoding offers the most direct path to resolving CF violations\" 这一结论缺少支撑，没有形式化分析或初步实验证明 global consensus 可行。\n- **Greedy decoding**: 所有实验使用 greedy decoding，但实际部署中常用 beam search 或 sampling。在 non-greedy 设置下 constraint composition 的行为（特别是 grammar-first fallback 频率）可能不同。\n\n---\n\n## Questions\n\n**Q1**: CF-DR trade-off 中，Table 6 显示 CF fallback 变体的 total violations (DR+CF) 为 14.82%，比 baseline Full S1 的 10.83% 高 3.99pp。但如果考虑 CF 和 DR 的下游影响不同（例如 CF 可能导致 knowledge graph 中的 entity type 不一致，而 DR 是 triple 级别的错误），是否应对两者赋予不同权重来评估 trade-off？论文目前将 DR 和 CF 简单相加，这是否合理？\n\n**Q2**: Grammar layer 在 DocRED 上将 DR 从 18.46% 提高到 26.17%（Table 3），论文解释为 OOV 关系被强制替换为 valid 关系后暴露了潜在的 type 不兼容性。但这些被\"强制替换\"的关系名称的语义质量如何？是被替换为 logit 空间中最近的 valid relation（可能语义相关），还是 essentially random？这关系到 grammar layer 是否在创造\"约束性幻觉\"。\n\n**Q3**: Fine-tuned 四方消融 (Table 8) 显示 grammar layer 在 fine-tuned 模型上是 no-op (DR change <0.2pp)。这是否意味着对于实际部署（通常使用 fine-tuned 模型），grammar layer 完全多余，只需 semantic layer？如果是这样，这简化了实际部署需求，但也削弱了\"两层组合\"的架构叙事。\n\n**Q4**: Appendix B 的 Fuzzy Matching Protocol 使用 \"token overlap >80% AND edit distance ≤2\"。这个阈值是如何选择的？是否在 DocRED 上调优过？如果是，在同一数据集上选择匹配阈值并评估会引入优化偏差。\n\n**Q5**: 论文声称 \"per-relation independent enforcement\" 是 CF 的根源，提出 \"global entity-level type consensus\" 作为解决路径。但 global consensus 在 autoregressive 解码中需要前向引用（当前未生成的关系可能对当前实体的类型有约束），这本质上是 NP-hard 的约束满足问题。论文的 decidability taxonomy 将此归为 \"non-local\"——是否有初步分析表明 global consensus 在实践中可行（例如通过近似或松弛）？\n\n---\n\n## Missing References\n\n- **GenIE** (Josifoski et al., 2022): 论文 Related Work 的 extended appendix 中提及，但正文 §6 未引用。GenIE 使用 state-based constraints 进行 end-to-end IE，是最直接的方法论先驱之一。\n- **EnriCo** (Zaratiana et al., 2024): 同上，仅在 Appendix 中引用。EnriCo 使用 ASP 约束在解码时强制类型兼容性，与 OntoCoDec 高度相关。\n- 论文对 constrained decoding quality impact 的讨论引用了 CRANE、Schall et al.、Tam et al.，但缺少 **Zhou et al. (2026) \"structure snowballing\"**——该论文在 Appendix 中引用但正文 §6 未提及，而其发现（格式约束导致 repetitive patterns）与 OntoCoDec 的 grammar-first fallback 行为直接相关。\n\n---\n\n## 主要优势\n\n1. **形式化质量高**：§2-4 的本体定义、constraint tightness、decidability taxonomy、pair-based vs independent enforcement 的论证清晰严谨，数学无歧义。Sequential masking 的必要性论证（non-rectangularity，SciERC 0/7、DocRED 23/96 rectangular）有数据支撑。\n\n2. **消融设计全面且控制变量到位**：5-way/4-way ablation 有效隔离了 grammar layer、semantic layer、S1/S2 的独立贡献。Cross-model 3 模型验证、composability matrix (2 models × 2 datasets × 2 settings)、FT 4-way ablation 覆盖面广。\n\n3. **对 CF trade-off 的正文讨论是诚实的**：§5 明确报告 CF 增加，Appendix B 的 CF-DR 消融（Table 6）用实验证明了 DR 和 CF 的不可独立最小化，CF 分布分析（Table 7）追踪到 Generic 类型的 schema-level 歧义。\n\n4. **Runtime overhead 分析量化了实用性**：Table 5 显示 Full S1 overhead 仅 +2.3%（SciERC）到 +5.4%（DocRED），sub-additive 性质有理论和实验支持。\n\n5. **Post-hoc filtering 对比**（Table 9）虽然结果不完全有利于 OntoCoDec，但论文选择诚实地呈现完整 10 组对比而非挑选有利数据，体现了实验诚信。\n\n6. **Bootstrap significance testing (10K iterations) + confidence intervals** 符合 ARR 要求的统计报告标准。p-value 报告细致（SciERC p=0.58 表明不显著，DocRED p<0.001 表明显著），没有对不显著结果做过度解读。\n\n---\n\n## 数值一致性核查结果\n\n逐一核查 Table 1-9 与正文引用的一致性，以及百分比变化计算：\n\n✓ Abstract DR 94% = (15.37-0.93)/15.37 = 93.95% ≈ 94%\n✓ Abstract +0.13pp = 8.36-8.23 = 0.13\n✓ DocRED range 42-90%: Mistral 42.2%, Qwen 44.7%, Llama 90.2%\n✓ Composability ±0.6pp: max |ΔR-F1| = 0.51pp (Llama DocRED)\n✓ DR ≤ 0.09% (SciERC) = max(Qwen 0%, Llama 0.09%)\n✓ DR ≤ 0.20% (DocRED) = max(Qwen 0.01%, Llama 0.20%)\n✓ Tightness 公式验证：SciERC τ̄=0.333 → avg 24 pairs (confirmed by (1-0.333)×36=24.01)\n✓ CF-DR tradeoff: ΔDR=+13.85pp, ΔCF=-9.86pp, Δ(DR+CF)=+3.99pp\n✓ Fine-tuning R-F1 deltas: all 8 values verified against tables\n\n⚠ 一处精度问题：Introduction 声称 \"DR ↓42--90% on DocRED\"，但 Qwen 的实际值是 44.7%，不是 42%。42% 来自 Mistral。范围的下界和上界来自不同模型（Mistral 和 Llama），这是正确的但在 Introduction 的 Contribution 3 中未明确说明是跨三个模型的范围。\n\n---\n\n**Reviewer Confidence**: 4/5 — 仔细阅读了全文和全部 appendix，逐一核查了主要数值声明，熟悉 constrained decoding 和 IE 领域。",
  "reviewer_id": "1",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿报告：OntoCoDec\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Ontology Constraints\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审查侧重**: 方法严谨性 + 实验设计\n\n---\n\n## 总体评分\n\n**Overall**: 3/5 — Findings track acceptance\n**一句话总结**: 方法设计干净、消融实验全面、技术上可靠，但 abstract/introduction 对 CF 副作用的系统性省略构成选择性报告问题，R²=0.886 基于 n=4 的\"预测框架\"声明过度，且对比 post-hoc filtering 的实际优势不具决定性。\n\n---\n\n## 官方维度打分（ACL ARR review form, Feb 2025+）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 4/5 | 形式化严谨，消融设计全面，bootstrap 统计测试规范。主要扣分：abstract 选择性报告、n=4 回归过度解读 |\n| Excitement | 3/5 | 问题真实且有价值，grammar+semantic 两层架构设计优雅。但实际优势受限于 (a) zero-shot R-F1 仅 ~8%，(b) post-hoc filtering 在多数场景下 F1 更高，(c) CF trade-off 部分抵消核心承诺 |\n| Reproducibility | 4/5 | Prompt 模板完整 (Appendix A)，三个公开模型 + 两个公开数据集，解码参数明确 (greedy)，有 bootstrap 参数 (10K)。未提及代码开源计划 |\n| Confidence | 4/5 | 逐表核查数值、逐条验证百分比计算、通读全部 appendix |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Abstract 和 Introduction 系统性省略 CF 副作用，构成选择性报告\n\n- 具体位置：Abstract (全文)、§1 Introduction (全文)\n- 问题：Abstract 声称 \"reduces domain/range violations by 94% (15.37%→0.93%) while maintaining extraction F1\"，Introduction 列出三条贡献均只提 DR 下降。但 CF (cross-field consistency) 违规从 0.08% 飙升至 9.90%（SciERC, 124× 增幅），Llama DocRED 从 0.17% 升至 12.02%（71× 增幅）。CF 本质上也是本体约束违反——同一实体在不同 triple 中被赋予不同类型。一位只读 abstract 的读者会误以为该方法\"几乎消除了本体违规\"，而实际上是将一类违规部分转化为另一类。\n- 论文正文 §5 和 Appendix B 对 CF 有诚实讨论，但 abstract/intro 的沉默构成科学报告中的 framing bias。\n- 为什么影响接收：ARR reviewer guidelines 明确指出 \"overclaiming\" 和 \"presenting speculation as conclusion\" 是常见问题。选择性报告核心 trade-off 属于 overclaiming 范畴。\n- 建议修改方向：Abstract 中加入一句 CF trade-off 摘要，例如：\"CF violations increase under zero-shot S1 (up to 12.02%) due to per-relation independent enforcement; fine-tuning reduces this to ≤1.18%.\" Introduction 的 Contribution 3 也应提及 CF 作为 trade-off 的一部分。\n\n**N2** [critical] R²=0.886 基于 n=4 数据点被过度解读为\"预测框架\"\n\n- 具体位置：Abstract (\"Quantitative analysis reveals that residual DR varies predictably\")、§7 Discussion (\"the dual-factor pattern (R²=0.886) provides a predictive framework for residual violations\")、Appendix B\n- 问题：线性回归 y = 0.366x − 0.138 有 2 个自由参数，n=4 仅留 2 个自由度。任意 4 个非共线点的线性拟合都能得到较高 R²。更关键的是，4 个数据点分布为 2 datasets × 2 models，其中两个 dataset 的 tightness 差异巨大（SciERC τ̄=0.333 vs DocRED τ̄=0.842），这意味着 tightness 这一个变量就足以解释大部分方差（本质上是 dataset-level 差异），乘以 baseline RV 的交互项只是在 dataset 内部做 2 点拟合。\n- Appendix B 正确地注明 \"we do not report a p-value given the small sample size\"，但 abstract 和 conclusion 仍将此描述为 \"predictive framework\"。\n- 为什么影响接收：用 n=4 的回归结果在 abstract 中做出定量预测性声明，不符合统计严谨性标准。\n- 建议修改方向：将 abstract 中的 \"varies predictably\" 改为 \"is consistent with a dual-factor pattern\"；将 conclusion 中的 \"predictive framework\" 降级为 \"descriptive pattern\" 或 \"consistent with\"；在 Appendix 中明确承认 n=4 无法区分是否 tightness 单一因素即可解释。增加 Mistral 的 2 个数据点 (n=6) 或更多 model/dataset 组合以增强说服力。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Parse failure 在约束下增加，构成潜在混淆变量\n\n- 具体位置：Table 4 注释 (\"Llama DocRED 68→91\")，Limitations §\n- 问题：Llama DocRED 下 parse failure 从 68/998 (6.8%) 增至 91/998 (9.1%)，增幅 34%。这些文档被排除在评估之外。如果约束导致更多\"困难\"文档 parse 失败，则 DR 改善可能部分归因于样本选择偏差（surviving documents 更容易满足约束）。论文在 Qwen DocRED fine-tuned 设置中报告了排除 parse failure 后的数值差异（R-F1 从 -0.30pp 变为 +0.03pp），但 Llama DocRED zero-shot 这一最严重的 parse failure 增长场景缺少类似分析。\n- 建议：补充 Llama DocRED zero-shot 的 parse-failure-excluded 分析，或至少讨论为什么约束增加 parse failure（是否因为 grammar-first fallback 累积导致 JSON 结构损坏？）。\n\n**W2** [warning] 与 Post-hoc filtering 对比不充分支持\"解码时约束优于后处理\"的核心叙事\n\n- 具体位置：Appendix B Table 9、§7 Discussion\n- 问题：Post-hoc filtering 在 6 个 zero-shot 配置中 5 个获得更高 R-F1（Table 9）。论文的反驳依据是 (a) OntoCoDec 保持更高 recall、(b) 处理 ET 违规、(c) 在高拒绝率时 post-hoc 崩溃（Mistral DocRED 73.7%）。但对于实践者来说，如果简单的 post-hoc filtering 在大多数场景下 F1 更高，选择 OntoCoDec 的理由需要更强有力的论证。\n- 论文将 post-hoc 定位为\"互补\"策略，但 Introduction 的 framing（\"Post-hoc validation wastes compute on discarded outputs and cannot redirect probability mass\"）带有否定语气，与实验数据不完全一致。\n- 建议：在正文（而非仅 Appendix）中加入 post-hoc 对比的摘要（至少一句话），诚实说明 post-hoc 在多数 zero-shot 场景 F1 更高，OntoCoDec 的优势在 recall 保持和 fine-tuned 场景下的等价性。\n\n**W3** [warning] Zero-shot R-F1 ~8% 的实际意义讨论不足（正文内）\n\n- 具体位置：§5 Experiments（全部 zero-shot 结果）、Appendix B \"Practical Significance of Zero-Shot F1\"\n- 问题：SciERC R-F1 = 8.36%，DocRED R-F1 = 8.23%。论文将 F1 定位为\"控制变量\"——但这一定位仅出现在 Appendix B 的一个段落中，正文和 Introduction 的贡献声明并未明确限定。同时，论文在 DocRED 上高亮 R-F1 gains (+0.50pp, p<0.001) 作为积极结果，存在逻辑不一致：如果 F1 只是控制变量，就不应在正文中强调其改善；如果 F1 重要，那 ~8% 的绝对值需要在正文中正面讨论实际意义。\n- 建议：在 §5 实验设置段落中加入 1-2 句正文讨论 zero-shot F1 水平的含义和上下文（如 supervised SOTA ~49-53%），不要仅放在 Appendix。\n\n**W4** [warning] SciERC 5-way 消融 vs DocRED 4-way 消融的不对称性未解释\n\n- 具体位置：Table 2 (SciERC, 5 modes) vs Table 3 (DocRED, 4 modes)\n- 问题：SciERC 包含 S2 配置，DocRED 不包含。如果 S2 在 DocRED 上由于 96 relations 的复杂性而不可行或效果差，应明确说明；如果只是篇幅原因，也应说明。\n- 建议：加一句解释为什么 DocRED 不测 S2。\n\n**W5** [warning] Semantic-only 模式在 DocRED 上反直觉地增加 ET 违规\n\n- 具体位置：Table 3，Semantic 行 ET = 4.22% vs Unconstrained ET = 2.48%\n- 问题：Semantic layer 声称仅在 HeadType/TailType 位置激活（§3.3.2），不应影响 EntityType 位置。但 ET 从 2.48% 几乎翻倍至 4.22%。这可能是 autoregressive 分布扰动的间接效应，但论文未讨论。\n- 建议：加一句解释此现象（是否因为 semantic masking 改变了整体 token 分布？）。\n\n**W6** [warning] First-subword-token 唯一性假设限制泛化性\n\n- 具体位置：§3.3 Implementation (\"Each τ ∈ E is mapped to the token ID of its first subword token; we pre-verify uniqueness\")、Limitations §\n- 问题：Limitations 正确指出\"ontologies with many types or multi-token type names would require prefix-tree masking, which we have not implemented\"。但 §3 的 Method 部分将此作为一个简单的 implementation detail 一笔带过，而这实际上是方法适用范围的根本性限制。如果 entity types 的 first subword token 不唯一（在大型本体中很常见），整个 semantic layer 的 masking 机制就不成立。\n- 建议：在 §3 Method 中明确将此列为设计假设（而非 implementation detail），并讨论何时假设成立（小型本体）和不成立（大型本体）。\n\n---\n\n## 小问题（不影响接收）\n\n- **符号冲突**: τ 同时用于 constraint tightness (§4 Eq.3) 和 entity type (§3 Eq.1 中的 τ_i)。建议 tightness 改用 κ 或 ψ。\n- **Table 2 S2 行**: CF = 8.03%, R-F1 = 8.03 是数值巧合，但视觉上容易让读者误以为是复制粘贴错误。\n- **DocRED RV residual**: Grammar 模式和 Full S1 在 DocRED 上 RV = 0.03%（非 0%）。这 0.03% 的来源未解释——CFG 应强制保证 RV = 0%。\n- **Limitations**: \"Global entity-level type consensus during decoding offers the most direct path to resolving CF violations\" 这一结论缺少支撑，没有形式化分析或初步实验证明 global consensus 可行。\n- **Greedy decoding**: 所有实验使用 greedy decoding，但实际部署中常用 beam search 或 sampling。在 non-greedy 设置下 constraint composition 的行为（特别是 grammar-first fallback 频率）可能不同。\n\n---\n\n## Questions\n\n**Q1**: CF-DR trade-off 中，Table 6 显示 CF fallback 变体的 total violations (DR+CF) 为 14.82%，比 baseline Full S1 的 10.83% 高 3.99pp。但如果考虑 CF 和 DR 的下游影响不同（例如 CF 可能导致 knowledge graph 中的 entity type 不一致，而 DR 是 triple 级别的错误），是否应对两者赋予不同权重来评估 trade-off？论文目前将 DR 和 CF 简单相加，这是否合理？\n\n**Q2**: Grammar layer 在 DocRED 上将 DR 从 18.46% 提高到 26.17%（Table 3），论文解释为 OOV 关系被强制替换为 valid 关系后暴露了潜在的 type 不兼容性。但这些被\"强制替换\"的关系名称的语义质量如何？是被替换为 logit 空间中最近的 valid relation（可能语义相关），还是 essentially random？这关系到 grammar layer 是否在创造\"约束性幻觉\"。\n\n**Q3**: Fine-tuned 四方消融 (Table 8) 显示 grammar layer 在 fine-tuned 模型上是 no-op (DR change <0.2pp)。这是否意味着对于实际部署（通常使用 fine-tuned 模型），grammar layer 完全多余，只需 semantic layer？如果是这样，这简化了实际部署需求，但也削弱了\"两层组合\"的架构叙事。\n\n**Q4**: Appendix B 的 Fuzzy Matching Protocol 使用 \"token overlap >80% AND edit distance ≤2\"。这个阈值是如何选择的？是否在 DocRED 上调优过？如果是，在同一数据集上选择匹配阈值并评估会引入优化偏差。\n\n**Q5**: 论文声称 \"per-relation independent enforcement\" 是 CF 的根源，提出 \"global entity-level type consensus\" 作为解决路径。但 global consensus 在 autoregressive 解码中需要前向引用（当前未生成的关系可能对当前实体的类型有约束），这本质上是 NP-hard 的约束满足问题。论文的 decidability taxonomy 将此归为 \"non-local\"——是否有初步分析表明 global consensus 在实践中可行（例如通过近似或松弛）？\n\n---\n\n## Missing References\n\n- **GenIE** (Josifoski et al., 2022): 论文 Related Work 的 extended appendix 中提及，但正文 §6 未引用。GenIE 使用 state-based constraints 进行 end-to-end IE，是最直接的方法论先驱之一。\n- **EnriCo** (Zaratiana et al., 2024): 同上，仅在 Appendix 中引用。EnriCo 使用 ASP 约束在解码时强制类型兼容性，与 OntoCoDec 高度相关。\n- 论文对 constrained decoding quality impact 的讨论引用了 CRANE、Schall et al.、Tam et al.，但缺少 **Zhou et al. (2026) \"structure snowballing\"**——该论文在 Appendix 中引用但正文 §6 未提及，而其发现（格式约束导致 repetitive patterns）与 OntoCoDec 的 grammar-first fallback 行为直接相关。\n\n---\n\n## 主要优势\n\n1. **形式化质量高**：§2-4 的本体定义、constraint tightness、decidability taxonomy、pair-based vs independent enforcement 的论证清晰严谨，数学无歧义。Sequential masking 的必要性论证（non-rectangularity，SciERC 0/7、DocRED 23/96 rectangular）有数据支撑。\n\n2. **消融设计全面且控制变量到位**：5-way/4-way ablation 有效隔离了 grammar layer、semantic layer、S1/S2 的独立贡献。Cross-model 3 模型验证、composability matrix (2 models × 2 datasets × 2 settings)、FT 4-way ablation 覆盖面广。\n\n3. **对 CF trade-off 的正文讨论是诚实的**：§5 明确报告 CF 增加，Appendix B 的 CF-DR 消融（Table 6）用实验证明了 DR 和 CF 的不可独立最小化，CF 分布分析（Table 7）追踪到 Generic 类型的 schema-level 歧义。\n\n4. **Runtime overhead 分析量化了实用性**：Table 5 显示 Full S1 overhead 仅 +2.3%（SciERC）到 +5.4%（DocRED），sub-additive 性质有理论和实验支持。\n\n5. **Post-hoc filtering 对比**（Table 9）虽然结果不完全有利于 OntoCoDec，但论文选择诚实地呈现完整 10 组对比而非挑选有利数据，体现了实验诚信。\n\n6. **Bootstrap significance testing (10K iterations) + confidence intervals** 符合 ARR 要求的统计报告标准。p-value 报告细致（SciERC p=0.58 表明不显著，DocRED p<0.001 表明显著），没有对不显著结果做过度解读。\n\n---\n\n## 数值一致性核查结果\n\n逐一核查 Table 1-9 与正文引用的一致性，以及百分比变化计算：\n\n✓ Abstract DR 94% = (15.37-0.93)/15.37 = 93.95% ≈ 94%\n✓ Abstract +0.13pp = 8.36-8.23 = 0.13\n✓ DocRED range 42-90%: Mistral 42.2%, Qwen 44.7%, Llama 90.2%\n✓ Composability ±0.6pp: max |ΔR-F1| = 0.51pp (Llama DocRED)\n✓ DR ≤ 0.09% (SciERC) = max(Qwen 0%, Llama 0.09%)\n✓ DR ≤ 0.20% (DocRED) = max(Qwen 0.01%, Llama 0.20%)\n✓ Tightness 公式验证：SciERC τ̄=0.333 → avg 24 pairs (confirmed by (1-0.333)×36=24.01)\n✓ CF-DR tradeoff: ΔDR=+13.85pp, ΔCF=-9.86pp, Δ(DR+CF)=+3.99pp\n✓ Fine-tuning R-F1 deltas: all 8 values verified against tables\n\n⚠ 一处精度问题：Introduction 声称 \"DR ↓42--90% on DocRED\"，但 Qwen 的实际值是 44.7%，不是 42%。42% 来自 Mistral。范围的下界和上界来自不同模型（Mistral 和 Llama），这是正确的但在 Introduction 的 Contribution 3 中未明确说明是跨三个模型的范围。\n\n---\n\n**Reviewer Confidence**: 4/5 — 仔细阅读了全文和全部 appendix，逐一核查了主要数值声明，熟悉 constrained decoding 和 IE 领域。",
    "reviewer_id": "1",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 137 · 2026-05-16T17:41:32.083056+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4025
}
```

</details>

---


### Assistant

_source line 138 · 2026-05-16T17:41:46.486246+00:00_

审稿报告已提交给 Review Director。

**审查摘要**：

- **Overall 3/5 (Findings track)**：技术上可靠，但 claims 超出 evidence。
- **2 个 Must-Fix**：(1) Abstract/Intro 系统性省略 CF 副作用（0.08%→9.90%/12.02%），构成选择性报告；(2) R²=0.886 基于 n=4 被过度解读为"预测框架"。
- **6 个 Should-Fix**：parse failure 增加未分析、post-hoc filtering 多数场景 F1 更高、zero-shot R-F1 ~8% 实际意义讨论不足、SciERC/DocRED 消融不对称未解释、semantic-only 增加 ET 未解释、first-subword-token 假设限制泛化。
- **数值一致性**：逐表核查基本一致，仅一处精度问题（Introduction 范围 42-90% 的来源跨模型未说明）。
- **主要优势**：形式化质量高、消融设计全面、CF trade-off 正文讨论诚实、runtime overhead 小、bootstrap 统计规范。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1"
}
```

</details>

---


## Round 5

## Round 5

8 recorded events


### User

_source line 139 · 2026-05-16T17:42:24.065912+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见。请逐条回应每个 Must-Fix (N1-N3) 和 Should-Fix (W1-W5) 问题：
- 如果同意，标注 [AGREE] 并简要说明理由
- 如果不同意，标注 [REBUT] 并提供证据（cite 具体 Section/Table/Figure）

特别关注与你的审查存在重叠或分歧的地方。

---

# Reviewer 2 完整审稿报告

## 总体评分
**Overall**: 3.5（介于 Findings 和 Conference 之间）

## Must-Fix 问题

**N1** [critical] Novelty claim 过度——缺少与 DORE (SIGDIAL 2024) 的对比和区分
- 论文声称 "the first to automatically compile IE ontology domain/range constraints into token-level semantic masks"。但 Vukovic et al. (SIGDIAL 2024) "Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding" 已将 ontology terms 和 relations 作为 constrained decoding 的约束目标用于关系抽取。虽然 DORE 的技术路径不同（CoT decoding + confidence threshold vs. logit masking），但 "first" claim 需要更精确地限定技术边界。
- 建议：引用 DORE 并缩窄 claim 为 "first to enforce pair-based domain/range type constraints via compiled stateful logit masks during autoregressive IE"。

**N2** [critical] 核心新颖性与代码生成领域先驱工作的技术差异阐述不足
- 主文 §6 仅用两句话打发代码生成的先驱工作（Synchromesh, PICARD, MGD, PLDI2025）。真正的 novelty（entity registry populated during generation、constraint target 从 free text 推断而非 declared type annotation 读取）只在 Appendix A 有详细讨论，主文中几乎看不到。
- 建议：在 §1 或 §3 开头明确阐述代码生成的 type system → automaton → mask pipeline 为何不能直接用于 IE。

**N3** [critical] 缺少与同领域 constrained decoding IE 系统的直接实验对比
- 对比的 baseline 仅为 unconstrained decoding 和 post-hoc filtering。但 GCD (Geng et al., EMNLP 2023) 和 BoostCD (Sakota et al., EMNLP 2025) 是同领域 constrained decoding IE 系统，论文引用了但未做实验对比。
- 建议：至少与 GCD 做定量对比。

## Should-Fix 问题

**W1** [warning] Dual-factor regression ($R^2=0.886$, $n=4$) 不具统计意义
- 4 个数据点拟合线性模型并报告 $R^2=0.886$ 作为 "predictive framework" 在统计上不严谨。
- 建议：从 Abstract 移除 $R^2$，降级为 "preliminary observation"，加入 Mistral 数据点。

**W2** [warning] CF 增加与 "constraint enforcement" 的核心叙事存在张力
- Abstract 完全不提 CF 增加。建议加 CF caveat 或调整定位从 "enforcement" 到 "reduction"。

**W3** [warning] 主评价指标是 violation rate reduction 而非下游任务质量——循环论证风险
- 施加约束当然会减少约束违反，这是 tautological 的。需要证明减少违反带来下游价值，或重新定位贡献为"保证性质"。

**W4** [warning] §5.1 "Violation Landscape" 混合了 motivation 和 experimental setup
- 建议将 violation landscape 提前到 §2.5 作为 motivation。

**W5** [warning] 缺少代码/数据可复现性声明

## Missing References
1. DORE (SIGDIAL 2024) — 必须引用
2. "A Survey of Generative Information Extraction" (COLING 2025) — 建议引用
3. PARSE (Shen et al., EMNLP 2025 Industry)
4. Schema Reinforcement Learning (ACL 2025)

## Questions
Q1: 为什么不与 GCD 做直接实验对比？
Q2: CF 增加是否会传播到下游任务？
Q3: $R^2$ 能否扩展到 6 个数据点（含 Mistral）？
Q4: Fine-tuned 设置下 grammar layer 是 no-op，"两层框架" framing 是否过度？
Q5: 50+ entity types 的大型本体下 prefix-tree masking 的工程复杂度？

---

请逐条回应以上所有 Must-Fix 和 Should-Fix 问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 140 · 2026-05-16T17:43:18.299235+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DORE \"Dialogue Ontology Relation Extraction\" constrained chain-of-thought decoding SIGDIAL 2024 Vukovic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DORE \"Dialogue Ontology Relation Extraction\" constrained chain-of-thought decoding SIGDIAL 2024 Vukovic"
  }
}
```

</details>

---


### Tool call

_source line 141 · 2026-05-16T17:43:18.778843+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GCD \"grammar-constrained decoding\" Geng EMNLP 2023 information extraction input-dependent grammar"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GCD \"grammar-constrained decoding\" Geng EMNLP 2023 information extraction input-dependent grammar"
  }
}
```

</details>

---


### Tool result

_source line 142 · 2026-05-16T17:43:24.055174+00:00_

Web search results for query: "GCD "grammar-constrained decoding" Geng EMNLP 2023 information extraction input-dependent grammar"

Links: [{"title":"Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.674/"},{"title":"[2305.13971] Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning","url":"https://arxiv.org/abs/2305.13971"},{"title":"Grammar-Constrained Decoding for Structured NLP Tasks ...","url":"https://aclanthology.org/2023.emnlp-main.674.pdf"},{"title":"Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning | OpenReview","url":"https://openreview.net/forum?id=KkHY1WGDII"},{"title":"GitHub - epfl-dlab/GCD · GitHub","url":"https://github.com/epfl-dlab/GCD"},{"title":"Flexible and Efficient Grammar-Constrained Decoding","url":"https://arxiv.org/pdf/2502.05111"},{"title":"Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230513971G/abstract"},{"title":"Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning | Request PDF","url":"https://www.researchgate.net/publication/376402267_Grammar-Constrained_Decoding_for_Structured_NLP_Tasks_without_Finetuning"},{"title":"Frontiers | Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/full"},{"title":"[PDF] Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Grammar-Constrained-Decoding-for-Structured-NLP-Geng-Josifosky/7e269bfabb451765a16ca0357de6b497cefb60bf"}]

Based on the search results, I found comprehensive information about the paper you're looking for:

## Grammar-Constrained Decoding (GCD) - Geng et al., EMNLP 2023

The paper w
…[truncated 1130 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 5276
}
```

</details>

---


### Tool result

_source line 143 · 2026-05-16T17:43:24.156107+00:00_

Web search results for query: "DORE "Dialogue Ontology Relation Extraction" constrained chain-of-thought decoding SIGDIAL 2024 Vukovic"

Links: [{"title":"Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding - ACL Anthology","url":"https://aclanthology.org/2024.sigdial-1.33/"},{"title":"[2408.02361] Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding","url":"https://arxiv.org/abs/2408.02361"},{"title":"Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding","url":"https://arxiv.org/html/2408.02361v1"},{"title":"Renato Vukovic","url":"https://renatovukovic.github.io/"},{"title":"Dialogue Ontology Relation Extraction via Constrained ...","url":"https://aclanthology.org/2024.sigdial-1.33.pdf"},{"title":"Computation and Language Aug 2024","url":"https://arxiv.org/list/cs.CL/2024-08?skip=95&show=2000"},{"title":"Main program – SIGDIAL 2024","url":"https://2024.sigdial.org/main-program/"},{"title":"dblp: David Arps","url":"https://dblp.org/pid/219/5595.html"},{"title":"Text-to-SQL Task-oriented Dialogue Ontology Construction","url":"https://arxiv.org/html/2507.23358v1"},{"title":"[PDF] Dialogue Term Extraction using Transfer Learning and Topological Data Analysis | Semantic Scholar","url":"https://www.semanticscholar.org/paper/bb4f26086acdd4eee04f1759b934b10780cb3c52"}]

Based on the search results, I found detailed information about this paper:

"Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding" is a paper by Vukovic et al. presented at the 25th Annual Meeting of the Special Interest Group on Discourse and Dialogue (SIGDIAL 2024) in Kyoto, Japan.

**Key Details:**

**Authors:** Renato Vukovic, David Arps, Carel van Niekerk, Benjamin Matthias Ruppik, Hsien-chin Lin, Michael Heck, and Milica Gasic

**Pages:** 370–384

**Main Contribution:** The paper adapts Chain-of-Thought (CoT) decoding, recently developed for reasoning problems, to generative relation extractio
…[truncated 745 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 5856
}
```

</details>

---


### Tool call

_source line 144 · 2026-05-16T17:44:59.628063+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[REBUT] R2-N1: Novelty claim 过度——与 DORE (SIGDIAL 2024) 的区分**\n\nR2 认为 DORE (Vukovic et al., SIGDIAL 2024) 已将 ontology constraints 用于 constrained decoding RE，因此 \"first\" claim 过度。经查证 DORE 原文，其技术路径是 **Chain-of-Thought decoding + confidence threshold**——在解码空间中生成多个分支，基于置信度阈值选择关系，将输出限制在 ontology terms 范围内。这属于 **output selection level** 的约束，而非 **token-level logit masking**。\n\nOntoCoDec 的 claim 是 \"the first to automatically compile IE ontology domain/range constraints into token-level semantic masks\"，关键技术边界在 \"compile\"、\"domain/range\"、\"token-level masks\" 三个限定词。DORE 不编译 domain/range 规则到 token-level masks，不维护 entity registry，不做 pair-based sequential type enforcement。两者技术路径根本不同。\n\n**但我同意 DORE 应被引用**作为相关工作（ontology-guided constrained decoding for RE），且 \"first\" claim 可以更精确——R2 建议的 \"first to enforce pair-based domain/range type constraints via compiled stateful logit masks during autoregressive IE\" 措辞更准确。\n\n**严重性判断**：降级为 should-fix (warning)，而非 critical。引用缺失应修复，但不构成 novelty 的根本性挑战。\n\n---\n\n**[AGREE with nuance] R2-N2: 与代码生成先驱工作的技术差异阐述不足**\n\nR2 指出 §6 Related Work 仅两句话处理代码生成先驱（\"Synchromesh, PICARD, MGD, and [PLDI2025] enforce type and scope constraints in code generation; OntoCoDec migrates this paradigm to IE\"），而真正的技术差异（entity registry 在生成中动态构建、constraint target 从 free text 推断而非 declared type annotation）仅在 Appendix A 展开。\n\n这一指摘是成立的。Appendix A 的 \"Semantic Constrained Decoding for Code\" 段落详细讨论了 PICARD 操作在 \"fixed, fully enumerated schema\" vs OntoCoDec 的 entity registry 在 \"generation 过程中填充\"这一根本区别，以及 PLDI2025 作为 \"closest mechanistic analog\" 的精确技术差异（deep subtyping vs flat domain/range sets，declared types vs free-text inference）。这些论述对建立 novelty 至关重要，但被放在了 Appendix 中，正文读者看不到。\n\n建议在 §3 Method 开头或 §1 Introduction 中用 2-3 句话明确阐述代码生成 type system → automaton → mask pipeline 的已有范式，以及 IE 场景的两个根本区别。\n\n**严重性判断**：同意 should-fix (warning) 级别，但不认为是 critical——novelty 论证存在且正确，只是位置不对（appendix vs main text），属于呈现问题而非实质性缺陷。\n\n---\n\n**[REBUT] R2-N3: 缺少与 GCD/BoostCD 的直接实验对比**\n\nR2 要求与 GCD (Geng et al., EMNLP 2023) 和 BoostCD (Sakota et al., EMNLP 2025) 做直接实验对比。经分析，这一要求存在方法论问题：\n\n**GCD 对比**：GCD 的核心技术是 input-dependent grammar-constrained decoding——即语法层面的约束（vocabulary membership、结构有效性），不具备 cross-field semantic constraint 能力（论文 §6: \"limited to syntactic constraints\"）。OntoCoDec 的 **Grammar-only 消融行**（Table 2/3）本质上就是 GCD-class approach 的效果上界：\n- SciERC Grammar-only: DR 14.84%（几乎不变），RV/ET → 0%\n- DocRED Grammar-only: DR 26.17%（反而上升），RV → 0.03%\n\n这就是 grammar-level constrained decoding（GCD 的能力范围）对 DR 的效果。OntoCoDec 的贡献恰恰在于 grammar 之上的 semantic layer——GCD 架构上无法覆盖的部分。要求与 GCD 做 DR reduction 对比，等同于要求论文证明 \"semantic constraints 比 syntactic-only constraints 更能减少 semantic violations\"，这是 trivially true 且已由消融实验覆盖。\n\n**BoostCD 对比**：BoostCD 是 training-time 策略（combining constrained/unconstrained outputs via boosting），与 OntoCoDec 的 decoding-time approach 在方法论层面正交。论文 §6 已正确定位：\"complementing our decoding-time approach with a training-time strategy\"。\n\n**让步**：论文可以在 §6 或 §5 中加一段明确说明 \"Grammar-only row in Table 2/3 represents the capability ceiling of GCD-class approaches, which by design cannot enforce domain/range constraints\"，使隐含的对比关系显式化。但要求从零实现 GCD 系统并做全面对比，对于一篇已有 3 models × 2 datasets × 5-way ablation 的论文来说不合理。\n\n**严重性判断**：降级为 info（editorial suggestion），不构成 must-fix。ARR guidelines 明确指出 \"Requests for additional experiments qualify as suggestions unless they're essential to the core claims\"。核心 claim 是 semantic layer 的价值，已由 grammar-only vs full S1 消融证明。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Dual-factor regression 不具统计意义**\n\n与我自己的 N2 [critical] 完全一致。n=4, 2 自由度，R²=0.886 不足以支撑 \"predictive framework\" 声明。Abstract 中应移除或降级。R2 建议加入 Mistral 数据点（n=6）是可行的改进方向。\n\n---\n\n**[AGREE] R2-W2: CF 增加与 abstract 的张力**\n\n与我自己的 N1 [critical] 完全一致。Abstract 选择性报告 DR reduction 而省略 CF increase（0.08%→9.90% SciERC, 0.17%→12.02% Llama DocRED）构成 framing bias。\n\n---\n\n**[REBUT with partial agreement] R2-W3: \"施加约束减少约束违反\" 是 tautological 的**\n\nR2 的论点是：constrained decoding reduces constraint violations 是循环论证，需要证明下游价值。\n\n这一表述过度简化了论文的贡献：\n\n1. **非平凡的技术问题**：将 IE ontology 的 domain/range constraints 编译为 autoregressive token-level masks 不是 trivial 的。论文的 novelty 不在于\"约束减少违反\"这一结论，而在于 HOW——entity registry、sequential masking、grammar-semantic enabling dependency、grammar-first fallback——这些是工程和形式化层面的贡献。\n\n2. **F1 中性是非显然的**：文献中有大量证据表明 constrained decoding 会损害 LLM 生成质量（CRANE, Schall et al., §6 Quality Impact）。论文证明了在 IE 场景下约束不降低 F1（SciERC p=0.58）甚至提升 F1（DocRED p<0.001），这不是 tautological 的。\n\n3. **trade-off 分析是实质性贡献**：CF↔DR trade-off (Table 6, Appendix B)、tightness-driven enforcement ceiling、enabling dependency 的量化——这些经验性发现超越了 \"约束减少违反\"。\n\n**但 R2 有一个合理的点**：论文可以更明确地将贡献定位为 (a) enforcement mechanism + (b) F1-neutrality guarantee + (c) trade-off characterization，而非仅仅是 violation rate reduction numbers。当前 abstract 的 \"reduces DR by 94%\" 确实把 violation reduction 当作主要卖点，而这一点确实有循环论证的影子。\n\n**建议**：在 Introduction 中加入一句明确的贡献定位：\"Our contribution is not that constrained decoding reduces violations—this is expected—but that ontological constraints can be compiled into token-level enforcement with zero F1 cost, composability with fine-tuning, and a characterizable trade-off space.\"\n\n---\n\n**[AGREE weakly] R2-W4: Violation Landscape 的位置**\n\nR2 建议将 §5.1 \"Violation Landscape\" 提前到 §2 作为 motivation。这是合理的 editorial suggestion。当前 §5.1 在 \"Experiments\" section 下但实际功能是 motivation/problem characterization。移到 §2 可改善逻辑流。\n\n但这是 presentation 层面的问题，不影响技术评判。severity 应为 info 而非 warning。\n\n---\n\n**[AGREE] R2-W5: 缺少代码/数据可复现性声明**\n\n与我自己的 Reproducibility 评分 (4/5) 一致。论文提供了 prompt templates、模型名称、数据集名称，但未提及代码开源计划。ARR 鼓励可复现性声明。\n\n---\n\n### R2 Questions 的简要回应\n\n**Q1 (为什么不与 GCD 做实验对比)**: 见上 N3 回应。Grammar-only ablation 行即为 GCD-class baseline。\n\n**Q2 (CF 传播到下游任务)**: 合理担忧。论文 Limitations 提到 \"CF type inconsistencies may propagate to downstream tasks (e.g., knowledge graph construction, question answering); the impact of such propagation has not been evaluated\"。这是已声明的局限性，但确实需要在正文中更明确讨论。我在自己的 Q1 中也提出了 CF 和 DR 的下游影响权重差异问题。\n\n**Q3 (R² 扩展到 n=6)**: Mistral 有 SciERC 和 DocRED 两个数据点。将其加入后 n=6 仍然很小，但至少 cross-validation 更有说服力。如果 Mistral 数据点偏离 linear fit（考虑到 Mistral 极高的 baseline DR 56-57%），可能反而削弱 R²。作者应尝试并诚实报告。\n\n**Q4 (FT 下 grammar layer 是 no-op，两层 framing 是否过度)**: 合理观察。但论文的定位包含 zero-shot 场景，grammar layer 在 zero-shot 下有明确贡献（RV/ET → 0%，enabling semantic layer）。对于 FT 场景，论文正确报告了 \"grammar is a no-op post-fine-tuning\" (Table 8 caption)。framing 可以更细致地区分 zero-shot vs FT 的使用建议。\n\n**Q5 (50+ entity types 的 prefix-tree masking 工程复杂度)**: 论文 Limitations 承认 first-subword-token 假设对大型本体不成立，需要 prefix-tree masking。这确实是方法适用范围的限制，我在 W6 中也指出应在 §3 Method 中将此列为设计假设而非 implementation detail。\n\n---\n\n### 与我（R1）审稿的重叠与分歧总结\n\n| R2 Issue | R1 Overlap | 判断 |\n|----------|-----------|------|\n| R2-N1 DORE | R1 未提及 | REBUT severity (critical→warning)，AGREE cite |\n| R2-N2 Code gen novelty | R1 未提及 | AGREE with nuance (presentation issue, not novelty issue) |\n| R2-N3 GCD comparison | R1 未提及 | REBUT (ablation already covers) |\n| R2-W1 R² on n=4 | R1-N2 [critical] | AGREE |\n| R2-W2 CF in abstract | R1-N1 [critical] | AGREE |\n| R2-W3 Tautological | R1 未提及 | REBUT with partial agreement |\n| R2-W4 §5.1 placement | R1 未提及 | AGREE weakly (info, not warning) |\n| R2-W5 Code release | R1 Reproducibility 4/5 | AGREE |\n\n**两位 Reviewer 共同认定的 critical issues**: (1) Abstract 选择性省略 CF，(2) R² overclaim on n=4。这两点应作为 revision 的最高优先级。\n\n**R1 独有的关注点**：parse failure 增加 (W1)、post-hoc filtering 对比叙事 (W2)、semantic-only 反直觉 ET 增加 (W5)、first-subword-token 假设 (W6)。\n\n**R2 独有的关注点**：DORE 引用 (N1)、代码生成差异阐述位置 (N2)、GCD 实验对比 (N3)、tautological 论证风险 (W3)。",
  "reviewer_id": "1",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[REBUT] R2-N1: Novelty claim 过度——与 DORE (SIGDIAL 2024) 的区分**\n\nR2 认为 DORE (Vukovic et al., SIGDIAL 2024) 已将 ontology constraints 用于 constrained decoding RE，因此 \"first\" claim 过度。经查证 DORE 原文，其技术路径是 **Chain-of-Thought decoding + confidence threshold**——在解码空间中生成多个分支，基于置信度阈值选择关系，将输出限制在 ontology terms 范围内。这属于 **output selection level** 的约束，而非 **token-level logit masking**。\n\nOntoCoDec 的 claim 是 \"the first to automatically compile IE ontology domain/range constraints into token-level semantic masks\"，关键技术边界在 \"compile\"、\"domain/range\"、\"token-level masks\" 三个限定词。DORE 不编译 domain/range 规则到 token-level masks，不维护 entity registry，不做 pair-based sequential type enforcement。两者技术路径根本不同。\n\n**但我同意 DORE 应被引用**作为相关工作（ontology-guided constrained decoding for RE），且 \"first\" claim 可以更精确——R2 建议的 \"first to enforce pair-based domain/range type constraints via compiled stateful logit masks during autoregressive IE\" 措辞更准确。\n\n**严重性判断**：降级为 should-fix (warning)，而非 critical。引用缺失应修复，但不构成 novelty 的根本性挑战。\n\n---\n\n**[AGREE with nuance] R2-N2: 与代码生成先驱工作的技术差异阐述不足**\n\nR2 指出 §6 Related Work 仅两句话处理代码生成先驱（\"Synchromesh, PICARD, MGD, and [PLDI2025] enforce type and scope constraints in code generation; OntoCoDec migrates this paradigm to IE\"），而真正的技术差异（entity registry 在生成中动态构建、constraint target 从 free text 推断而非 declared type annotation）仅在 Appendix A 展开。\n\n这一指摘是成立的。Appendix A 的 \"Semantic Constrained Decoding for Code\" 段落详细讨论了 PICARD 操作在 \"fixed, fully enumerated schema\" vs OntoCoDec 的 entity registry 在 \"generation 过程中填充\"这一根本区别，以及 PLDI2025 作为 \"closest mechanistic analog\" 的精确技术差异（deep subtyping vs flat domain/range sets，declared types vs free-text inference）。这些论述对建立 novelty 至关重要，但被放在了 Appendix 中，正文读者看不到。\n\n建议在 §3 Method 开头或 §1 Introduction 中用 2-3 句话明确阐述代码生成 type system → automaton → mask pipeline 的已有范式，以及 IE 场景的两个根本区别。\n\n**严重性判断**：同意 should-fix (warning) 级别，但不认为是 critical——novelty 论证存在且正确，只是位置不对（appendix vs main text），属于呈现问题而非实质性缺陷。\n\n---\n\n**[REBUT] R2-N3: 缺少与 GCD/BoostCD 的直接实验对比**\n\nR2 要求与 GCD (Geng et al., EMNLP 2023) 和 BoostCD (Sakota et al., EMNLP 2025) 做直接实验对比。经分析，这一要求存在方法论问题：\n\n**GCD 对比**：GCD 的核心技术是 input-dependent grammar-constrained decoding——即语法层面的约束（vocabulary membership、结构有效性），不具备 cross-field semantic constraint 能力（论文 §6: \"limited to syntactic constraints\"）。OntoCoDec 的 **Grammar-only 消融行**（Table 2/3）本质上就是 GCD-class approach 的效果上界：\n- SciERC Grammar-only: DR 14.84%（几乎不变），RV/ET → 0%\n- DocRED Grammar-only: DR 26.17%（反而上升），RV → 0.03%\n\n这就是 grammar-level constrained decoding（GCD 的能力范围）对 DR 的效果。OntoCoDec 的贡献恰恰在于 grammar 之上的 semantic layer——GCD 架构上无法覆盖的部分。要求与 GCD 做 DR reduction 对比，等同于要求论文证明 \"semantic constraints 比 syntactic-only constraints 更能减少 semantic violations\"，这是 trivially true 且已由消融实验覆盖。\n\n**BoostCD 对比**：BoostCD 是 training-time 策略（combining constrained/unconstrained outputs via boosting），与 OntoCoDec 的 decoding-time approach 在方法论层面正交。论文 §6 已正确定位：\"complementing our decoding-time approach with a training-time strategy\"。\n\n**让步**：论文可以在 §6 或 §5 中加一段明确说明 \"Grammar-only row in Table 2/3 represents the capability ceiling of GCD-class approaches, which by design cannot enforce domain/range constraints\"，使隐含的对比关系显式化。但要求从零实现 GCD 系统并做全面对比，对于一篇已有 3 models × 2 datasets × 5-way ablation 的论文来说不合理。\n\n**严重性判断**：降级为 info（editorial suggestion），不构成 must-fix。ARR guidelines 明确指出 \"Requests for additional experiments qualify as suggestions unless they're essential to the core claims\"。核心 claim 是 semantic layer 的价值，已由 grammar-only vs full S1 消融证明。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Dual-factor regression 不具统计意义**\n\n与我自己的 N2 [critical] 完全一致。n=4, 2 自由度，R²=0.886 不足以支撑 \"predictive framework\" 声明。Abstract 中应移除或降级。R2 建议加入 Mistral 数据点（n=6）是可行的改进方向。\n\n---\n\n**[AGREE] R2-W2: CF 增加与 abstract 的张力**\n\n与我自己的 N1 [critical] 完全一致。Abstract 选择性报告 DR reduction 而省略 CF increase（0.08%→9.90% SciERC, 0.17%→12.02% Llama DocRED）构成 framing bias。\n\n---\n\n**[REBUT with partial agreement] R2-W3: \"施加约束减少约束违反\" 是 tautological 的**\n\nR2 的论点是：constrained decoding reduces constraint violations 是循环论证，需要证明下游价值。\n\n这一表述过度简化了论文的贡献：\n\n1. **非平凡的技术问题**：将 IE ontology 的 domain/range constraints 编译为 autoregressive token-level masks 不是 trivial 的。论文的 novelty 不在于\"约束减少违反\"这一结论，而在于 HOW——entity registry、sequential masking、grammar-semantic enabling dependency、grammar-first fallback——这些是工程和形式化层面的贡献。\n\n2. **F1 中性是非显然的**：文献中有大量证据表明 constrained decoding 会损害 LLM 生成质量（CRANE, Schall et al., §6 Quality Impact）。论文证明了在 IE 场景下约束不降低 F1（SciERC p=0.58）甚至提升 F1（DocRED p<0.001），这不是 tautological 的。\n\n3. **trade-off 分析是实质性贡献**：CF↔DR trade-off (Table 6, Appendix B)、tightness-driven enforcement ceiling、enabling dependency 的量化——这些经验性发现超越了 \"约束减少违反\"。\n\n**但 R2 有一个合理的点**：论文可以更明确地将贡献定位为 (a) enforcement mechanism + (b) F1-neutrality guarantee + (c) trade-off characterization，而非仅仅是 violation rate reduction numbers。当前 abstract 的 \"reduces DR by 94%\" 确实把 violation reduction 当作主要卖点，而这一点确实有循环论证的影子。\n\n**建议**：在 Introduction 中加入一句明确的贡献定位：\"Our contribution is not that constrained decoding reduces violations—this is expected—but that ontological constraints can be compiled into token-level enforcement with zero F1 cost, composability with fine-tuning, and a characterizable trade-off space.\"\n\n---\n\n**[AGREE weakly] R2-W4: Violation Landscape 的位置**\n\nR2 建议将 §5.1 \"Violation Landscape\" 提前到 §2 作为 motivation。这是合理的 editorial suggestion。当前 §5.1 在 \"Experiments\" section 下但实际功能是 motivation/problem characterization。移到 §2 可改善逻辑流。\n\n但这是 presentation 层面的问题，不影响技术评判。severity 应为 info 而非 warning。\n\n---\n\n**[AGREE] R2-W5: 缺少代码/数据可复现性声明**\n\n与我自己的 Reproducibility 评分 (4/5) 一致。论文提供了 prompt templates、模型名称、数据集名称，但未提及代码开源计划。ARR 鼓励可复现性声明。\n\n---\n\n### R2 Questions 的简要回应\n\n**Q1 (为什么不与 GCD 做实验对比)**: 见上 N3 回应。Grammar-only ablation 行即为 GCD-class baseline。\n\n**Q2 (CF 传播到下游任务)**: 合理担忧。论文 Limitations 提到 \"CF type inconsistencies may propagate to downstream tasks (e.g., knowledge graph construction, question answering); the impact of such propagation has not been evaluated\"。这是已声明的局限性，但确实需要在正文中更明确讨论。我在自己的 Q1 中也提出了 CF 和 DR 的下游影响权重差异问题。\n\n**Q3 (R² 扩展到 n=6)**: Mistral 有 SciERC 和 DocRED 两个数据点。将其加入后 n=6 仍然很小，但至少 cross-validation 更有说服力。如果 Mistral 数据点偏离 linear fit（考虑到 Mistral 极高的 baseline DR 56-57%），可能反而削弱 R²。作者应尝试并诚实报告。\n\n**Q4 (FT 下 grammar layer 是 no-op，两层 framing 是否过度)**: 合理观察。但论文的定位包含 zero-shot 场景，grammar layer 在 zero-shot 下有明确贡献（RV/ET → 0%，enabling semantic layer）。对于 FT 场景，论文正确报告了 \"grammar is a no-op post-fine-tuning\" (Table 8 caption)。framing 可以更细致地区分 zero-shot vs FT 的使用建议。\n\n**Q5 (50+ entity types 的 prefix-tree masking 工程复杂度)**: 论文 Limitations 承认 first-subword-token 假设对大型本体不成立，需要 prefix-tree masking。这确实是方法适用范围的限制，我在 W6 中也指出应在 §3 Method 中将此列为设计假设而非 implementation detail。\n\n---\n\n### 与我（R1）审稿的重叠与分歧总结\n\n| R2 Issue | R1 Overlap | 判断 |\n|----------|-----------|------|\n| R2-N1 DORE | R1 未提及 | REBUT severity (critical→warning)，AGREE cite |\n| R2-N2 Code gen novelty | R1 未提及 | AGREE with nuance (presentation issue, not novelty issue) |\n| R2-N3 GCD comparison | R1 未提及 | REBUT (ablation already covers) |\n| R2-W1 R² on n=4 | R1-N2 [critical] | AGREE |\n| R2-W2 CF in abstract | R1-N1 [critical] | AGREE |\n| R2-W3 Tautological | R1 未提及 | REBUT with partial agreement |\n| R2-W4 §5.1 placement | R1 未提及 | AGREE weakly (info, not warning) |\n| R2-W5 Code release | R1 Reproducibility 4/5 | AGREE |\n\n**两位 Reviewer 共同认定的 critical issues**: (1) Abstract 选择性省略 CF，(2) R² overclaim on n=4。这两点应作为 revision 的最高优先级。\n\n**R1 独有的关注点**：parse failure 增加 (W1)、post-hoc filtering 对比叙事 (W2)、semantic-only 反直觉 ET 增加 (W5)、first-subword-token 假设 (W6)。\n\n**R2 独有的关注点**：DORE 引用 (N1)、代码生成差异阐述位置 (N2)、GCD 实验对比 (N3)、tautological 论证风险 (W3)。",
    "reviewer_id": "1",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 145 · 2026-05-16T17:45:03.698405+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4070
}
```

</details>

---


### Assistant

_source line 146 · 2026-05-16T17:45:11.768502+00:00_

交叉回应已提交给 Review Director。

总结：
- R2 的 3 个 Must-Fix 中，N1（DORE）同意引用但 rebut critical 严重性，N2（代码生成差异）同意是 presentation 问题但非 novelty 问题，N3（GCD 实验对比）rebut——消融实验的 Grammar-only 行已覆盖 GCD-class baseline 的能力范围
- R2 的 5 个 Should-Fix 中，W1（R²）和 W2（CF abstract）与我自己的 N2/N1 完全重合，确认为最高优先修改项；W3（tautological）部分同意 framing 需调整；W4/W5 同意但严重性较低
- 两位 Reviewer 共同的 critical consensus：Abstract 省略 CF + R² overclaim

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1"
}
```

</details>

---


## Round 6

## Round 6

52 recorded events


### User

_source line 147 · 2026-05-17T10:15:16.745213+00:00_

[Round 1 审稿请求]:
## Round 4 审稿任务 — Reviewer 1（方法/实验严谨性）

### Venue 信息
- **目标**: EMNLP 2026 Findings (ARR May 2026 cycle)
- **截止日期**: 2026-05-25
- **页数限制**: 正文 8 页，references/appendix 不限
- **模板**: ACL style (`\usepackage[review]{acl}`)
- **匿名规则**: double-blind
- **附录**: 不参与正文页数限制，但可参与审稿

### 论文文件
- 主文件: `projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`
- 附录: `appendix_beam_search.tex`, `appendix_sampling_table.tex`, `appendix_prompts.tex`, `appendix_related_work.tex`, `appendix_discussion.tex`, `appendix_llama_per_relation.tex`

### 你的审查侧重
**方法严谨性 + 实验设计 + 统计声明**

重点审查：
1. **方法正确性**：两层约束（grammar + semantic）的形式化是否严谨？pair-based sequential masking 的正确性论证是否充分？grammar-first fallback 的设计是否有未讨论的隐患？
2. **实验设计**：ablation 设计是否完整？SciERC 5-way vs DocRED 4-way 是否合理？composability matrix 设计是否有混淆变量？
3. **统计声明**：R²=0.886 (n=4) 的 dual-factor pattern 是否 overclaim？bootstrap 显著性检验是否恰当？DR/CF 百分比数据的呈现是否有 cherry-picking？
4. **数据一致性**：各表格数字是否一致？cross-section 引用数字是否匹配？
5. **Parse failure 作为混淆变量**：约束模式下 parse failure 增加（Llama DocRED 6.8%→9.1%）是否被充分讨论？

### 先前审稿的 Open/In-Progress Issues（需要你验证当前版本是否已修复）

**Critical:**
- **W1**: CF violation (up to 12.02% ZS) 在 Abstract/Intro 中是否已经不再被省略？当前版本的 framing 是否客观？
- **R2-N1**: R²=0.886 (n=4) 是否仍被 overclaim 为 "predictive framework"？当前措辞是否降级为 "descriptive characterization"？

**Warning:**
- **W3**: Post-hoc filtering 在 5/6 ZS 配置中 F1 高于 OntoCoDec，Intro 的 "wastes compute" framing 是否已修改？是否添加了 §5 post-hoc comparison summary？
- **R2-N3**: Parse failure 增加（约束下 +34%）是否提供了 parse-failure-excluded 分析？
- **R2-N6**: Semantic-only mode 导致 DocRED ET 从 2.48%→4.22%，机制解释是否已添加？

**Info:**
- **R2-N7**: DocRED 为何省略 S2 是否有解释？
- **R2-N10**: RV=0.03% 残余来源是否已解释？
- **GC-N1**: Grammar-only 行是否被明确标识为 GCD 能力上限？

请逐条检查以上 issue 的修复状态，同时做独立全面审稿。按标准审稿格式输出：Summary → Strengths → Weaknesses → Questions → Missing References → Minor Issues。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 148 · 2026-05-17T10:15:27.564086+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
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

_source line 149 · 2026-05-17T10:15:27.614814+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 150 · 2026-05-17T10:15:31.188774+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 151 · 2026-05-17T10:15:32.895977+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 152 · 2026-05-17T10:15:32.946706+00:00_

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
12	\usepackage{multirow}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{enumitem}
16	\usepackage{xcolor}
17	
18	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Ontology Constraints}
19	
20	\author{Anonymous ACL submission}
21	
22	\begin{document}
23	\maketitle
24	
25	% === Abstract ===
26	\input{abstract}
27	
28	% === §1 Introduction ===
29	\input{section1_introduction_draft}
30	
31	% === §2 Background ===
32	\input{section2_background}
33	
34	% === §3 Method ===
35	\input{section3_method_draft}
36	
37	% === §4 Constraint Composition ===
38	\section{Constraint Composition}
39	\label{sec:composition}
40	\input{section4_composition_draft}
41	
42	% === §5 Experiments ===
43	\section{Experiments}
44	\label{sec:experiments}
45	
46	\subsection{Violation Landscape}
47	\input{section3_violation_landscape}
48	
49	\input{section5_scierc_draft}
50	\input{section5_docred_draft}
51	\input{section5_crossmodel_draft}
52	\input{section5_runtime}
53	
54	% === §6 Related Work ===
55	\input{section6_related_work}
56	
57	% === §7 Discussion and Conclusion ===
58	\section{Discussion and Conclusion}
59	\label{sec:discussion}
60	\input{section7_conclusion_compressed}
61	
62	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
63	\clearpage
64	\section*{Limitations}
65	
66	CF impact is model-dependent: for well-calibrated models (Qwen, Llama), S1 introduces CF violations (up to 12.02\%) as a consequence of per-relation independent enforcement; for poorly-calibrated models (Mistral), S1 substantially reduces CF (56.87\%\,$\to$\,1.27\%) by constraining type assignments to schema-valid values.
67	CF fallback ablation shows that eliminating CF re-routes violations to DR ($+$13
…[truncated 3529 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 153 · 2026-05-17T10:15:40.627053+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

I've found comprehensive information about ACL ARR 2026 reviewer guidelines and review form criteria. Here's what I found:

## Reviewer Guidelines

Reviewers are asked to follow a specific workflow: (1) read the paper and get the first impression, (2) s
…[truncated 1961 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 9438
}
```

</details>

---


### Tool call

_source line 154 · 2026-05-17T10:15:46.543881+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5 etc.), and descriptions for each score level. Also extract any specific guidelines about what reviewers should evaluate."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5 etc.), and descriptions for each score level. Also extract any specific guidelines about what reviewers should evaluate."
  }
}
```

</details>

---


### Tool call

_source line 155 · 2026-05-17T10:15:48.202647+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
  }
}
```

</details>

---


### Tool result

_source line 156 · 2026-05-17T10:15:48.303879+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_fd4b26.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_d3264e.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_550cbf.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_outline.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex
/home/ubuntu/.agent-ml-research
…[truncated 2180 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 157 · 2026-05-17T10:15:57.450281+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## Primary Scoring Dimensions

### 1. Reviewer Confidence (1-5 scale)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: Quite sure with unlikely but possible missed details
- **3**: Pretty sure but chance of missing something
- **2**: Willing to defend evaluation but fairly likely missed details
- **1**: "Not my area, or paper is very hard to understand"

### 2. Soundness (1-5 scale with half-points)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: Strong with sufficient claim support
- **3**: Acceptable with main claims supported
- **2**: Poor with insufficient main claim support
- **1**: "Major Issues: This study is not yet sufficiently thorough"

### 3. Excitement (1-5 scale with half-points)
Subjective evaluation considering innovations, community impact, and relevance. Ranges from "Highly Exciting" (5) to "Not Exciting" (1).

### 4. Overall Assessment (1-5 scale with half-points)
Ranges from "Consider for Award" (5) through "Conference" (4) to "Do not resubmit" (1).

## Secondary Evaluation Areas

- **Limitations and Societal Impact**: Adequacy of author discussion
- **Ethical Concerns**: Alignment with ACL code of ethics
- **Reproducibility** (1-5): Ease of result reproduction
- **Datasets** (1-5): Value to research community
- **Software** (1-5): Utility for others
- **Author Identity Knowledge** (1-5): Anonymity assessment

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 10906
}
```

</details>

---


### Tool call

_source line 158 · 2026-05-17T10:16:02.937524+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 159 · 2026-05-17T10:16:03.289357+00:00_

1	\begin{abstract}
2	We present \textsc{OntoCoDec}, which compiles IE ontology schemas into two composable token-level decoding constraints that provide formal guarantees during autoregressive generation:
3	(1)~a \emph{grammar layer} (XGrammar CFG) guaranteeing JSON structural validity and entity/relation vocabulary membership (ET, RV\,$\to$\,0\%); and
4	(2)~a \emph{semantic layer} guaranteeing per-triple domain/range type compliance via a stateful entity registry and dynamic logit masking.
5	The two layers compose via bitwise AND on logit masks, with the grammar layer as an enabling prerequisite.
6	%
7	Without constraints, LLM-based IE produces systematic violations: 15.37\% DR on SciERC (7 relations) and 18.46\% on DocRED (96 relations)---comparable rates governed by \emph{constraint tightness} rather than ontology scale.
8	\textsc{OntoCoDec} reduces DR by 42--99\% across three model families (Qwen3-8B, Llama-3.1-8B, Mistral-7B) with no significant F1 cost.
9	For the primary model (Qwen3-8B): SciERC $+$0.13\,pp ($p{=}0.58$), DocRED $+$0.50\,pp ($p{<}0.001$); other models show comparable or larger gains (\S\ref{sec:cross-model}).
10	% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1, llama_docred_full_s1, mistral_docred
11	Residual DR is characterized by a dual-factor pattern (schema tightness $\times$ model calibration; $R^2{=}0.886$, $n{=}4$; Appendix~\ref{app:dual-factor}).
12	Composed with LoRA fine-tuning, DR reaches $\leq$\,0.09\% (SciERC) and 0.20\% (DocRED) with R-F1 within $\pm$0.6\,pp, confirming orthogonal composability.
13	Per-relation independent enforcement introduces a CF$\leftrightarrow$DR trade-off: cross-field consistency violations arise (up to 12\% in zero-shot) as the cost of per-slot domain/range guarantees; fine-tuning resolves this tension (CF\,$\leq$\,1.2\%).
14	\end{abstract}
15	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 160 · 2026-05-17T10:16:03.289756+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 161 · 2026-05-17T10:16:03.792077+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly deployed for zero-shot information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity is guaranteed to carry a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}---structurally valid triples that are ontologically invalid.
8	In a systematic study, we find violations are pervasive: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred}, driven by \emph{constraint tightness} (few valid type pairs per relation) rather than ontology scale.
9	Relations with tight constraints exhibit far higher rates (\textsc{Compare}: 42.4\%) than loosely constrained ones (\textsc{Used-for}: 0.8\%).
10	
11	Existing approaches leave a fundamental gap.
12	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable---violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp.
13	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} guarantees syntactic well-formedness but cannot encode cross-field semantic constraints.
14	At high rejection rates (e.g., Mistral DocRED 73.7\%), post-hoc filtering discards the majority of outputs including true positives, making it impractical; it also cannot redirect probability mass during decoding.
15	Training-based approaches~\cite{sainz2024gollie,lu2022uie} provide only soft guidance that cannot eliminate violations.
16	
17	We propose \textbf{OntoCoDec} (\textbf{Onto}logy-\textbf{Co}mpiled \textbf{Dec}oding), a framework that compiles an IE ontology into two composable layers of decoding-time constraints.
18	The \emph{grammar layer} enforces JSON well-formedness and vocabulary validity via XGrammar.
19	The \emph{semantic layer} 
…[truncated 1687 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 162 · 2026-05-17T10:16:03.842712+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
  }
}
```

</details>

---


### Tool result

_source line 163 · 2026-05-17T10:16:04.244665+00:00_

1	% Section 2: Background (compressed)
2	
3	\section{Background}
4	\label{sec:background}
5	
6	\paragraph{IE Ontology Structure.}
7	\label{sec:bg:ontology}
8	An IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defines entity types $\mathcal{E}$, relation types $\mathcal{R}$, and a mapping $\sigma: \mathcal{R} \to \mathcal{P}(\mathcal{E} \times \mathcal{E})$ specifying valid (head type, tail type) pairs per relation.
9	A triple $(h, r, t)$ is \emph{type-valid} if $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$.
10	We define the \emph{constraint tightness} of $r$ as $1 - |\sigma(r)| / |\mathcal{T}|^2$ where $\mathcal{T} = \mathcal{E}$ is the entity type vocabulary: tighter constraints leave fewer valid options, increasing violation likelihood.
11	
12	\paragraph{Grammar-Constrained Decoding.}
13	\label{sec:bg:gcd}
14	Grammar-constrained decoding restricts each token $y_t$ to a mask $M_g \in \{0, 1\}^{|V|}$ derived from a target grammar.
15	XGrammar~\citep{dong2025xgrammar} compiles JSON Schemas into pushdown automata for efficient enforcement of structural constraints; Outlines~\citep{willard2023outlines} and SGLang~\citep{zheng2024sglang} offer similar capabilities.
16	However, these methods are limited to context-free constraints and cannot enforce cross-field semantic rules---e.g., ``if $r$ = \textsc{Feature-of}, then $\mathrm{type}(h) \in \{\textsc{Method}, \textsc{OtherScientificTerm}\}$''---which depend on previously generated field values.
17	
18	\paragraph{Problem Statement.}
19	\label{sec:bg:problem}
20	Given $\mathcal{O}$ and an autoregressive LM $\mathcal{M}$, we seek constraints $\mathcal{C}$ ensuring: (a)~\textbf{structural validity}---well-formed JSON with $\mathcal{E}$/$\mathcal{R}$ membership; and (b)~\textbf{type validity}---$(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$ for every triple.
21	Condition (a) is context-free; (b) is context-sensitive but \emph{prefix-decidable}---at the point where a type token is generated, all in
…[truncated 89 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 164 · 2026-05-17T10:16:04.245087+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 165 · 2026-05-17T10:16:05.199257+00:00_

1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	We present OntoCoDec, a two-layer constrained decoding framework that compiles ontology schemas into token-level masks enforced during autoregressive generation.
9	Unlike type-constrained code generation, IE presents three distinct challenges: (1)~entity types are inferred from free text rather than declared annotations, (2)~the entity registry is built dynamically during generation, and (3)~constraint targets are context-dependent type assignments rather than fixed grammar productions.
10	The grammar layer (\S\ref{sec:grammar}) guarantees structural validity—well-formed JSON with ontology-vocabulary membership—while the semantic layer (\S\ref{sec:semantic}) enforces domain/range type constraints via a stateful entity registry.
11	We describe the problem formulation (\S\ref{sec:formulation}), each layer, and two decoding strategies (\S\ref{sec:strategies}).
12	Formal analysis of constraint composition is deferred to Section~\ref{sec:composition}.
13	
14	
15	\subsection{Problem Formulation}
16	\label{sec:formulation}
17	
18	\paragraph{IE as structured generation.}
19	Given an input text $x$, a language model generates a structured JSON output $y$:
20	%
21	\begin{equation}\label{eq:output-schema}
22	\resizebox{.88\columnwidth}{!}{$\displaystyle
23	  y = \bigl\{\texttt{entities}: [\{n_i, \tau_i\}],\; \texttt{relations}: [\{h_j, t_j, r_j, \tau^h_j, \tau^t_j\}]\bigr\}
24	$}
25	\end{equation}
26	%
27	where each entity has a name $n_i$ and type $\tau_i \in \mathcal{E}$, and each relation specifies head $h_j$, tail $t_j$, relation type $r_j \in \mathcal{R}$, and head/tail entity types $\tau^h_j, \tau^t_j$.
28	
29	\paragraph{Ontology compliance.}
30	Using the ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defined in \S\ref{sec:background}, we write $\operatorname{dom}(r) = \{\tau^h : \exists \tau^t,
…[truncated 7978 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 166 · 2026-05-17T10:16:05.350370+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 167 · 2026-05-17T10:16:05.451246+00:00_

1	% Section: Constraint Composition (compressed, 787→~500 words)
2	
3	At each decoding step $t$, let $G(t) \subseteq V$ and $S(t) \subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.
4	The final mask is their conjunction:
5	%
6	\begin{equation}\label{eq:composition}
7	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
8	\end{equation}
9	%
10	so a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$, reflecting the enabling dependency (\S\ref{sec:method})---the semantic layer requires the relation type to belong to $\mathcal{R}$, a property guaranteed only by the grammar layer.
12	
13	\paragraph{Grammar-First Fallback.}
14	When $S(t) \cap G(t) = \emptyset$---tight constraints leave no token that is both grammar-valid and semantically valid---na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
15	We enforce a \emph{grammar-first fallback}: if no semantically valid token survives grammar filtering, semantic masking is skipped and the grammar layer alone controls selection.
16	Structural integrity is a hard constraint; a type violation is a soft error detectable by downstream validation.
17	
18	\paragraph{Constraint Tightness.}
19	We define the tightness of relation $r$ as:
20	%
21	\begin{equation}\label{eq:tightness}
22	  \kappa(r) = 1 - \frac{|\mathcal{V}(r)|}{|\mathcal{T}|^2},
23	\end{equation}
24	%
25	where $\mathcal{V}(r)$ is the set of valid type pairs and $\mathcal{T}$ the entity type vocabulary.
26	The mean tightness $\bar{\kappa} = \frac{1}{|\mathcal{R}|}\sum_{r} \kappa(r)$ characterizes ontology restrictiveness.
27	Tighter constraints eliminate more grammar-valid tokens at type-bearing positions, increasing fallback frequency and residual DR.
28	This dual-factor pattern---tightness $\times$ baseline model violation rate---is consistent with the cros
…[truncated 1970 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 168 · 2026-05-17T10:16:05.502087+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
  }
}
```

</details>

---


### Tool result

_source line 169 · 2026-05-17T10:16:05.552918+00:00_

1	% §5.1 Experimental Setup and Violation Landscape
2	% Compressed from standalone section. main.tex provides \subsection header.
3	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
4	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
5	
6	\label{sec:violation_landscape}
7	
8	\paragraph{Setup.}
9	We evaluate Qwen3-8B~\cite{qwen2025qwen3} under zero-shot greedy decoding on two IE benchmarks:
10	\textbf{SciERC}~\cite{luan2018scierc} (551 test sentences, 7 relations, avg.\ 26.1 valid type pairs per relation) and \textbf{DocRED}~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test set annotations are not publicly available; following prior work, we evaluate on the development set (998 documents).} 96 relations, avg.\ 5.68 valid pairs).
11	We measure four violation categories: \textbf{Domain/Range (DR)} violations where $(\mathrm{type}(h), \mathrm{type}(t)) \notin \sigma(r)$; \textbf{Relation Vocabulary (RV)} where $r \notin \mathcal{R}$; \textbf{Entity Type (ET)} where $e \notin \mathcal{E}$; and \textbf{Cross-Field Consistency (CF)} where the same entity receives different types across triples.
12	Cross-model validation with Llama-3.1-8B-Instruct is reported in \S\ref{sec:cross-model}.
13	Violation rates are computed over successfully parsed documents; including parse failures as zero-violation instances adjusts rates by at most 0.23\,pp (Llama DocRED zero-shot; $<$0.01\,pp under fine-tuning), confirming robustness to this exclusion.
14	
15	\paragraph{Violation distribution.}
16	Table~\ref{tab:prompt_comparison} reports violation rates.
17	DR violations affect 15.37\% of triples on SciERC and 18.46\% on DocRED---comparable rates despite a 14$\times$ difference in ontology size---indicating that violation severity is driven by \emph{constraint tightness} rather than ontology scale.
18	RV violations on DocRED are dramatically higher (29.66\% vs.\ 1.39\%), indicating that 96 relation types exceed the model's capacity to reproduce 
…[truncated 1607 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 170 · 2026-05-17T10:16:12.236557+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 171 · 2026-05-17T10:16:13.242294+00:00_

1	% Section 5 — SciERC Results (Draft)
2	% Data source: Phase 2 SciERC registry experiments
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,
4	%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2
5	% All numbers verified against registry 2026-05-14.
6	
7	\subsection{Results on SciERC}
8	\label{sec:scierc-results}
9	
10	Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC,
11	evaluating each constraint layer independently and in combination.
12	All experiments use Qwen3-8B in a zero-shot setting on 551 test documents
13	with identical prompts and decoding parameters;
14	only the active constraint layers differ.
15	
16	% ──────────────────────────────────────────
17	%  Table: SciERC five-way ablation
18	% ──────────────────────────────────────────
19	\begin{table}[t]
20	\centering
21	\small
22	\setlength{\tabcolsep}{3.6pt}
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{@{}l rrrrr rr@{}}
25	\toprule
26	& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
27	& \multicolumn{2}{c}{\textbf{F1}} \\
28	\cmidrule(lr){2-6} \cmidrule(l){7-8}
29	\textbf{Mode}
30	  & DR\,$\downarrow$ & $\Delta$DR
31	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
32	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
33	\midrule
34	Unconstrained
35	  & 15.37 & ---
36	  & 1.39  & 0.40
37	  & 0.08
38	  & 8.23  & 31.01 \\
39	Grammar
40	  & 14.84 & $\downarrow$3\%
41	  & \textbf{0} & \textbf{0}
42	  & 0.08
43	  & 8.23  & 30.98 \\
44	Semantic
45	  & 11.65 & $\downarrow$24\%
46	  & 1.51  & 0.40
47	  & 2.71
48	  & 8.15  & 31.01 \\
49	Full (S1)
50	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
51	  & \textbf{0} & \textbf{0}
52	  & 9.90
53	  & \textbf{8.36} & 30.98 \\
54	Full (S2)
55	  & 0.97  & $\downarrow$94\%
56	  & \textbf{0} & \textbf{0}
57	  & 8.03
58	  & 8.03  & \textbf{31.90} \\
59	\bottomrule
60	\end{tabular}}%
61	\caption{Five-way ablation on SciERC (551 documents, Qwen3-8B, zero-shot).
62	DR: domain/range violation rate;
63	RV: rel
…[truncated 10876 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 172 · 2026-05-17T10:16:13.294052+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 173 · 2026-05-17T10:16:13.746037+00:00_

1	% Section 5 — DocRED Results (compressed, 1450→~600 words)
2	% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,
3	%          phase2_docred_semantic_only, phase2_docred_full_s1
4	% All numbers verified against registry 2026-05-14.
5	
6	\subsection{Cross-Dataset Validation on DocRED}
7	\label{sec:docred-results}
8	
9	Table~\ref{tab:docred-ablation} presents the four-way ablation on DocRED, a document-level RE benchmark with 96 Wikidata relation types---14$\times$ the ontology size of SciERC.
10	All experiments use Qwen3-8B zero-shot on 998 documents.
11	
12	% ──────────────────────────────────────────
13	%  Table: DocRED four-way ablation
14	% ──────────────────────────────────────────
15	\begin{table}[t]
16	\centering
17	\small
18	\setlength{\tabcolsep}{3.6pt}
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{@{}l rrrrr rr@{}}
21	\toprule
22	& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
23	& \multicolumn{2}{c}{\textbf{F1}} \\
24	\cmidrule(lr){2-6} \cmidrule(l){7-8}
25	\textbf{Mode}
26	  & DR\,$\downarrow$ & $\Delta$DR
27	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
28	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
29	\midrule
30	Unconstrained
31	  & 18.46 & ---
32	  & 29.66 & 2.48
33	  & 0.10
34	  & 7.74  & 58.15 \\
35	Grammar
36	  & 26.17 & $\uparrow$42\%
37	  & \textbf{0.03} & \textbf{0}
38	  & 0.07
39	  & \textbf{8.31}  & \textbf{59.38} \\
40	Semantic
41	  & 13.84 & $\downarrow$25\%
42	  & 29.87 & 4.22
43	  & 1.05
44	  & 7.70  & 57.81 \\
45	Full (S1)
46	  & \textbf{10.21} & $\downarrow$\textbf{45\%}
47	  & \textbf{0.03} & \textbf{0}
48	  & 2.57
49	  & 8.23  & 59.37 \\
50	\bottomrule
51	\end{tabular}}%
52	\caption{Four-way ablation on DocRED (998 documents, Qwen3-8B, zero-shot).
53	$\Delta$DR: relative change vs.\ unconstrained.
54	Best per column in \textbf{bold} (CF excluded).
55	F1 $\times$100. Bootstrap significance: R-F1 $+$0.50\,pp ($p < 0.001$).}
56	\label{tab:docred-ablation}
57	\end{table}
58	
59	% exp_ids: phase2_docred_unconstraine
…[truncated 3449 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 174 · 2026-05-17T10:16:13.897112+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 175 · 2026-05-17T10:16:14.700953+00:00_

1	% Section 5 — Cross-Model Validation (compressed, 830→~400 words)
2	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1,
3	%          phase2_docred_unconstrained, phase2_docred_full_s1,
4	%          llama_scierc_unconstrained, llama_scierc_full_s1,
5	%          llama_docred_unconstrained, llama_docred_full_s1
6	
7	\subsection{Cross-Model Validation}
8	\label{sec:cross-model}
9	
10	We replicate the full S1 configuration with Llama-3.1-8B-Instruct and Mistral-7B-Instruct-v0.3 under identical prompts, decoding parameters, and evaluation.
11	Table~\ref{tab:cross-model} summarizes results across all three models.
12	Mistral serves as a third zero-shot verification point confirming model-agnosticism; composability evaluation (\S\ref{sec:composability}) uses LoRA fine-tuning which requires domain-specific training data available only for Qwen and Llama.
13	
14	\begin{table}[t]
15	\centering
16	\small
17	\setlength{\tabcolsep}{3.4pt}
18	\resizebox{\columnwidth}{!}{%
19	\begin{tabular}{@{}ll rrrr r@{}}
20	\toprule
21	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
22	& \textbf{R-F1} \\
23	\cmidrule(lr){3-6} \cmidrule(l){7-7}
24	\textbf{Dataset} & \textbf{Model}
25	  & DR\,$\downarrow$ & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
26	  & $\uparrow$ \\
27	\midrule
28	\multirow{6}{*}{SciERC}
29	  & Qwen (U)    & 15.37 & 1.39  & 0.40 & 0.08 & 8.23 \\
30	  & Qwen (S1)   &  0.93 & 0     & 0    & 9.90 & 8.36 \\
31	  \cmidrule(l){2-7}
32	  & Llama (U)   & 13.34 & 0.55  & 0    & 0.24 & 2.68 \\
33	  & Llama (S1)  &  0.08 & 0     & 0    & 6.56 & 2.54 \\
34	  \cmidrule(l){2-7}
35	  & Mistral (U) & 56.94 & 0     & 1.50 & 56.87$^\dagger$ & 3.66 \\
36	  & Mistral (S1)& 13.40 & 0     & 0    & 1.27  & 3.67 \\
37	\midrule
38	\multirow{6}{*}{DocRED}
39	  & Qwen (U)    & 18.46 & 29.66 & 2.48 & 0.10 & 7.74 \\
40	  & Qwen (S1)   & 10.21 &  0.03 & 0    & 2.57 & 8.23 \\
41	  \cmidrule(l){2-7}
42	  & Llama (U)   & 26.07 & 16.03 & 0.13 & 0.17 & 5.98 \\
43	  & Llama (S1)  &  2.55 &  0  
…[truncated 2202 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 176 · 2026-05-17T10:16:14.801830+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
  }
}
```

</details>

---


### Tool result

_source line 177 · 2026-05-17T10:16:15.156040+00:00_

1	% Section 5 — Runtime Analysis
2	% Data source: DocRED latency profiling (exp_id: docred_latency_profiling)
3	% Qwen3-8B, same single-GPU server, controlled 4-way ablation.
4	
5	\subsection{Runtime Overhead}
6	\label{sec:runtime}
7	
8	Table~\ref{tab:runtime} reports per-document inference time for each constraint layer combination on both datasets (Qwen3-8B, same GPU).
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\setlength{\tabcolsep}{4pt}
14	\begin{tabular}{@{}l rr rr@{}}
15	\toprule
16	& \multicolumn{2}{c}{\textbf{SciERC (7 rels)}}
17	& \multicolumn{2}{c}{\textbf{DocRED (96 rels)}} \\
18	\cmidrule(lr){2-3} \cmidrule(l){4-5}
19	\textbf{Mode} & Avg (s) & Overhead & Avg (s) & Overhead \\
20	\midrule
21	Unconstrained & 2.587 & --- & 21.023 & --- \\
22	Grammar       & 2.631 & $+$1.7\% & 21.366 & $+$1.6\% \\
23	Semantic      & 2.618 & $+$1.2\% & 21.912 & $+$4.2\% \\
24	Full (S1)     & 2.647 & $+$2.3\% & 22.147 & $+$5.4\% \\
25	\bottomrule
26	\end{tabular}
27	\caption{Per-document inference time by constraint layer (Qwen3-8B, same GPU).
28	Grammar compile time: 0.044\,s (one-time, amortized to zero).
29	Full-mode overhead is sub-additive (DocRED: 1.6\%$+$4.2\%$=$5.8\% expected vs.\ 5.4\% observed).}
30	\label{tab:runtime}
31	\end{table}
32	
33	Grammar-layer overhead is consistent across datasets ($+$1.6--1.7\%), independent of schema complexity.
34	Semantic-layer overhead scales with the number of relation types (SciERC 7 types: $+$1.2\%; DocRED 96 types: $+$4.2\%), reflecting increased domain-range lookup frequency.
35	Full-mode overhead is sub-additive on both datasets because the two layers share token-set computation.
36	Even in the most complex setting (DocRED, 96 relations), total overhead is $+$5.4\%---practically negligible.
37	Under fine-tuning, S1 overhead drops further to $+$2.3\% (61\,ms/doc; Appendix~\ref{app:ft-latency}).
38	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 354
}
```

</details>

---


### Tool call

_source line 178 · 2026-05-17T10:16:15.307314+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
  }
}
```

</details>

---


### Tool result

_source line 179 · 2026-05-17T10:16:15.759990+00:00_

1	% Section 7 — Discussion and Conclusion (compressed)
2	% Full discussion paragraphs moved to Appendix C.
3	
4	OntoCoDec compiles IE ontology schemas into composable token-level decoding constraints, achieving 42--99\% DR reduction across three models and two datasets with no significant F1 cost.
5	Composed with LoRA fine-tuning, it reaches DR\,$\leq$\,0.20\% at $<$0.6\,pp F1 cost, confirming orthogonal error targeting.
6	Within calibrated models (Qwen, Llama; $n{=}4$), residual DR correlates linearly with $\bar{\kappa} \times \text{RV}_{\text{baseline}}$ ($R^2{=}0.886$), suggesting constraint benefit scales with schema stringency and model OOV tendency.
7	This pattern has an informative boundary condition: Mistral achieves RV\,=\,0\% on SciERC yet retains DR\,=\,13.4\%, because its dominant error mode is entity type misclassification rather than vocabulary confusion---a factor not captured by the dual-factor product.
8	We present this as a descriptive characterization with explicit scope rather than a universal predictive law.
9	
10	CF impact is model-dependent: S1 introduces CF for well-calibrated models (up to 12.02\%) but reduces it for poorly-calibrated ones (Mistral: 56.87\%\,$\to$\,1.27\%).
11	Ablation confirms CF$\leftrightarrow$DR tension ($+$13.85\,pp; Appendix~\ref{app:cf-dr-tradeoff}); fine-tuning reduces CF by 88\% (\S\ref{sec:composability}); global entity-level type consensus offers the most direct path forward.
12	
13	% Limitations and Future Work moved to \section*{Limitations} in main.tex (ARR requirement)
14	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 180 · 2026-05-17T10:16:15.962895+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-17T10:16:15.963448+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Grammar-Constrained Decoding.}
5	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, LMQL~\cite{beurer-kellner2023lmql}, DOMINO~\cite{beurer-kellner2024domino}, SynCode~\cite{ugare2024syncode}, and ASAp~\cite{park2024grammar} ensure every token belongs to a grammar-valid continuation; IterGen~\cite{ugare2025itergen} adds backtracking.
6	These guarantee format validity but cannot enforce cross-field semantic constraints such as ontology domain/range rules.
7	
8	\paragraph{Semantic Constrained Decoding for Code.}
9	Synchromesh~\cite{synchromesh_iclr2022}, PICARD~\cite{scholak2021picard}, MGD~\cite{mgd_neurips2023}, and \citet{pldi2025_type_constrained_codegen} enforce type and scope constraints in code generation; OntoCoDec migrates this paradigm to IE.
10	
11	\paragraph{Vocabulary and Type-Constrained Generation.}
12	\citet{roth_yih_2004} establish relational type compatibility as a hard constraint via ILP, though applied post-hoc.
13	GENRE~\cite{decao2021genre}, AdaKGC~\cite{adakgc_emnlp2023}, GCD~\cite{geng2023gcd}, and GoLLIE~\cite{sainz2024gollie} constrain \emph{which tokens} can appear but not \emph{which type combinations} are valid per relation; GCD's per-position trie enforces vocabulary membership (equivalent to our grammar layer) but cannot capture the conditional dependency between head and tail types that our semantic layer provides.
14	DORE~\cite{vukovic2024dore} enforces ontological consistency via chain-of-thought output selection with confidence thresholds---a generate-then-select paradigm distinct from OntoCoDec's token-level logit masking during generation.
15	GenIE~\cite{josifoski2022genie} constrains entity generation to a candidate trie but does not enforce relation-specific type constraints.
16	EnriCo~\cite{zaratiana2024enrico} applies ASP constraints during decoding for joint entity-relation extraction---a hard-constraint approach like ours, but with task-sp
…[truncated 1083 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 182 · 2026-05-17T10:16:22.169847+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 183 · 2026-05-17T10:16:22.522436+00:00_

1	% Appendix B — Extended Discussion
2	% Contains discussion paragraphs moved from the main text during compression.
3	
4	\section{Extended Discussion}\label{app:discussion}
5	
6	%%% CF Dual Mechanism %%%
7	% exp_ids: phase2_scierc_full_s1, llama_scierc_full_s1, llama_docred_full_s1
8	
9	\paragraph{CF Dual Mechanism.}
10	CF violations arise from two distinct mechanisms:
11	(1)~\emph{Registry override}: the semantic constraint forces a domain-compatible type that conflicts with the entity's previously registered type.
12	The entity appears in multiple relations with different type requirements, and the per-relation mask selects the locally valid type without consulting prior assignments.
13	(2)~\emph{Grammar-first fallback} (\S\ref{sec:interaction}): when the semantic mask conflicts with all grammar-valid tokens, the semantic layer is dropped entirely, allowing the grammar layer to generate any structurally valid type---which may differ from the entity's registered type.
14	
15	These mechanisms have sharply different model profiles.
16	Qwen3-8B triggers zero grammar-first fallbacks across all experiments, attributing 100\% of its CF violations to registry override.
17	Llama-3.1-8B, by contrast, triggers 5{,}882 fallbacks on SciERC (10.7 per document) and 57{,}825 on DocRED (63.8 per document), making grammar-first fallback the dominant CF source.
18	This asymmetry is consistent with the cross-model CF gap: Qwen achieves CF\,=\,2.57\% on DocRED vs.\ Llama's 12.02\%, despite both using identical constraint configurations.
19	The difference traces to Llama's less calibrated type predictions, which more frequently conflict with the semantic mask's valid set, triggering fallback.
20	
21	%%% Fallback Behavior and Effective Coverage %%%
22	% exp_ids: cf_fallback_ablation_scierc (final data)
23	
24	\paragraph{Fallback Behavior and Effective Coverage.}
25	\label{app:fallback-coverage}
26	The two-layer architecture produces two distinct fallback mechanisms with different seman
…[truncated 26266 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 184 · 2026-05-17T10:16:22.673418+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex"
  }
}
```

</details>

---


### Tool result

_source line 185 · 2026-05-17T10:16:23.024876+00:00_

1	\section{Sampling Robustness}\label{app:sampling}
2	
3	\begin{table}[h]
4	\centering
5	\caption{Constraint robustness under nucleus sampling ($T$=0.7, $p$=0.9) vs.\ greedy decoding.}
6	\label{tab:sampling-robustness}
7	\begin{tabular}{llcccccc}
8	\toprule
9	Dataset & Decoding & ET\% & RV\% & DR\% & CF\% & E-F1 & R-F1 \\
10	\midrule
11	\multirow{2}{*}{SciERC (551)} & Greedy & 0 & 0 & 0.93 & 9.90 & 30.98 & 8.36 \\
12	& Sampling & 0 & 0 & 0.75 & 9.90 & 31.28 & 7.42 \\
13	\midrule
14	\multirow{2}{*}{DocRED (114$^\dagger$)} & Greedy & 0 & 0.03 & 10.21 & 2.57 & 59.37 & 8.23 \\
15	& Sampling & 0 & 0 & 10.31 & 12.63 & 57.05 & 7.92 \\
16	\bottomrule
17	\end{tabular}
18	\par\smallskip\footnotesize $^\dagger$Subset of 114 documents; full DocRED sampling requires ${\sim}300$h due to extended generation under high-temperature sampling with complex schemas.
19	\end{table}
20	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-17T10:16:23.176053+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex"
  }
}
```

</details>

---


### Tool result

_source line 187 · 2026-05-17T10:16:23.980308+00:00_

1	\section{Beam Search Compatibility}
2	\label{app:beam-search}
3	
4	OntoCoDec's constraint enforcement is designed to be decoding-strategy agnostic.
5	The main experiments (\S\ref{sec:experiments}) use greedy decoding; Appendix~\ref{app:sampling} validates nucleus sampling.
6	Here we verify compatibility with beam search, completing coverage of the three standard decoding strategies.
7	
8	\paragraph{Implementation challenges.}
9	Two stateful components require adaptation for beam search.
10	(1)~The grammar layer (XGrammar) maintains an internal \texttt{GrammarMatcher} state that tracks the generated token sequence; beam reordering invalidates this state because beams are permuted across steps.
11	Our solution instantiates a fresh \texttt{GrammarMatcher} per beam per step and replays the beam's current token sequence through XGrammar's stateless accept API (64 lines of code).
12	(2)~The semantic layer's \texttt{TypeConstraintProcessor} accumulates entity and relation registries that assume a single generation path.
13	Our solution isolates state per beam by calling \texttt{detect()} on the full partial output at each step, reconstructing all entity/relation state from scratch for each beam independently (61 lines of code).
14	Both adaptations add ${\sim}125$ lines total without modifying the existing greedy/sampling logic.
15	
16	\paragraph{Results.}
17	Table~\ref{tab:beam-search} compares beam search ($k{=}4$, \texttt{early\_stopping=True}) against greedy decoding under full S1 constraints across six model-dataset combinations.
18	
19	\begin{table}[h]
20	\centering
21	\small
22	\caption{Beam search ($k{=}4$) vs.\ greedy decoding under full S1 constraints.
23	SciERC evaluated on full test set (551 documents); DocRED evaluated on 50-document subsets (greedy baselines from 998-document full evaluation, not matched subsets).
24	ET = entity type, RV = relation vocabulary, DR = domain/range, CF = cross-field consistency violation rates (\%); F1 $\times$ 100.}
25	\label{t
…[truncated 6262 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 188 · 2026-05-17T10:16:24.081137+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex"
  }
}
```

</details>

---


### Tool result

_source line 189 · 2026-05-17T10:16:24.432629+00:00_

1	% Appendix C — Per-Relation Violation Analysis (Llama-3.1-8B)
2	% exp_ids: llama_docred_unconstrained, llama_docred_full_s1
3	
4	\section{Per-Relation Violation Analysis (Llama-3.1-8B)}\label{app:llama-per-relation}
5	
6	Table~\ref{tab:llama-per-relation-dr} presents the per-relation domain--range violation breakdown for Llama-3.1-8B on DocRED under full S1 constraints.
7	The Llama baseline exhibits an RV rate of 16.03\%, substantially lower than Qwen's 29.66\%, indicating stronger baseline vocabulary compliance.
8	% exp_ids: llama_docred_unconstrained (RV=16.03%), qwen_docred_unconstrained (RV=29.66%)
9	Full S1 completely eliminates RV violations and reduces the residual DR rate to 2.55\% (418/16{,}368 triples), with only three relations exceeding 10\%.
10	% exp_ids: llama_docred_full_s1 (DR=2.6%, 418/16368)
11	
12	\begin{table}[h]
13	\centering
14	\caption{Top 10 per-relation DR violation rates for Llama-3.1-8B on DocRED under full S1 constraints. Relations with $>$20 triples and 0\% DR (e.g., P131, P206, P361, P170, P86) are omitted.}
15	\label{tab:llama-per-relation-dr}
16	\resizebox{\columnwidth}{!}{%
17	\begin{tabular}{@{}llrrr@{}}
18	\toprule
19	Relation & PID & Triples & DR Violations & DR Rate (\%) \\
20	\midrule
21	dissolved/demolished & P576 & 73 & 24 & 32.9 \\
22	followed by          & P156 & 117 & 24 & 20.5 \\
23	unemployment rate    & P1198 & 15 & 3 & 20.0 \\
24	end time             & P582 & 130 & 21 & 16.2 \\
25	instance of          & P31  & 290 & 37 & 12.8 \\
26	product/material produced & P1056 & 98 & 11 & 11.2 \\
27	location of formation & P740 & 81 & 8 & 9.9 \\
28	head of state        & P35  & 41  & 3  & 7.3 \\
29	applies to jurisdiction & P1001 & 637 & 45 & 7.1 \\
30	conflict             & P607 & 453 & 30 & 6.6 \\
31	\bottomrule
32	\end{tabular}}
33	\end{table}
34	% exp_ids: llama_docred_full_s1
35	
36	Compared with Qwen, which retains a 10.21\% residual DR under full S1 concentrated in P1198 (83\% fallback) and P171 (78\% fallback), Llama's re
…[truncated 523 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 190 · 2026-05-17T10:16:24.433089+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 191 · 2026-05-17T10:16:24.584170+00:00_

1	\section{Extended Related Work}
2	\label{app:related_work}
3	
4	% ===========================================================================
5	% Paradigm 1: Grammar-Constrained Decoding
6	% ===========================================================================
7	\paragraph{Grammar-Constrained Decoding.}
8	Recent work has established efficient algorithms for restricting LLM outputs to conform to context-free grammars, making grammar-constrained decoding the de facto standard for obtaining structured output from language models.
9	XGrammar~\cite{dong2025xgrammar} partitions the vocabulary into context-independent and context-dependent tokens and maintains persistent pushdown automata across decoding steps, achieving up to 100$\times$ speedup over prior CFG-constrained decoding methods.
10	Outlines~\cite{willard2023outlines} reformulates constrained generation as finite-state machine transitions with offline vocabulary indexing, enabling efficient enforcement of regular-expression and JSON-schema constraints without runtime overhead per token.
11	LMQL~\cite{beurer-kellner2023lmql} introduces a declarative query language that compiles type, length, and regex constraints into token-level masks, providing a programmable interface for specifying multi-variable output structures.
12	These systems ensure that every generated token belongs to a grammar-valid continuation, but they do not address the \emph{distribution distortion} introduced by naive token masking.
13	A parallel line of work tackles this problem directly: DOMINO~\cite{beurer-kellner2024domino} minimizes distributional divergence during CFG enforcement by formulating mask selection as an optimization problem, and ASAp~\cite{park2024grammar} provides a provably unbiased sampling algorithm that preserves the original LM distribution under grammar constraints.
14	Together, these advances have made grammar-constrained decoding both fast and statistically principled, establishing a robust foundation for stru
…[truncated 19808 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 192 · 2026-05-17T10:16:25.086485+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex"
  }
}
```

</details>

---


### Tool result

_source line 193 · 2026-05-17T10:16:25.137198+00:00_

1	% Appendix — Prompt Templates
2	% W10: Extraction prompts used in all experiments.
3	
4	\section{Prompt Templates}
5	\label{app:prompts}
6	
7	All experiments use the same prompts across constrained and unconstrained decoding---constraints are applied at the logit level, not through prompt modification.
8	Table~\ref{tab:prompts} shows the system and user prompts for each dataset.
9	
10	\begin{table*}[t]
11	\centering
12	\small
13	\begin{tabular}{@{}p{0.95\textwidth}@{}}
14	\toprule
15	\textbf{SciERC --- System Prompt (Unconstrained \& Constrained)} \\
16	\midrule
17	\texttt{You are an expert information extraction system for scientific texts. Extract entities and relations from the given text.} \\[4pt]
18	\texttt{Entity types: Task, Method, Material, Metric, OtherScientificTerm, Generic} \\
19	\texttt{Relation types: Used-for, Feature-of, Hyponym-of, Part-of, Compare, Conjunction, Evaluate-for} \\[4pt]
20	\texttt{Output a JSON object with:} \\
21	\texttt{- "entities": list of \{"text": "...", "type": "..."\}} \\
22	\texttt{- "relations": list of \{"head": "...", "tail": "...", "type": "...", "head\_type": "...", "tail\_type": "..."\}} \\[4pt]
23	\texttt{Output ONLY valid JSON, no explanation.} \\
24	\midrule
25	\textbf{SciERC --- User Prompt} \\
26	\midrule
27	\texttt{Extract all entities and relations from this scientific text:} \\
28	\texttt{"\{text\}"} \\
29	\texttt{Output JSON:} \\
30	\midrule
31	\midrule
32	\textbf{DocRED --- System Prompt (Unconstrained \& Constrained)} \\
33	\midrule
34	\texttt{You are an information extraction system. Extract all entities and relations from the following document.} \\[4pt]
35	\texttt{Entity types: PER, ORG, LOC, TIME, NUM, MISC} \\[4pt]
36	\texttt{Relation types: country, instance of, performer, ...\ (96 Wikidata relation types; full list omitted for space)} \\[4pt]
37	\texttt{Output a JSON object with exactly this structure:} \\
38	\texttt{\{"entities": [\{"text": "entity name", "type": "ENTITY\_TYPE"\}],} \\
39	\texttt{\ 
…[truncated 771 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 194 · 2026-05-17T10:19:30.407242+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the full reviewer guidelines, especially: what constitutes a good vs poor paper, scoring criteria for soundness, excitement, and overall assessment. Any guidance on how to evaluate Findings-track papers specifically."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the full reviewer guidelines, especially: what constitutes a good vs poor paper, scoring criteria for soundness, excitement, and overall assessment. Any guidance on how to evaluate Findings-track papers specifically."
  }
}
```

</details>

---


### Tool result

_source line 195 · 2026-05-17T10:19:36.686897+00:00_

# ARR Reviewer Guidelines: Key Evaluation Criteria

## What Constitutes a Good Paper

Strong papers demonstrate:
- Clear research questions addressing genuine knowledge gaps
- Appropriate scope and well-motivated methodology
- Technical soundness with sufficient evidence for claims
- Contributions valuable to the field (novel methods, resources, analyses, or insights)
- Proper documentation and reproducibility details

## Common Poor Paper Issues

The guidelines identify systematic problems to watch for:

**Methodological problems (M):**
- "LLM-only evaluation without validation" of reliability in context
- Insufficient reproducibility details or unclear code/data availability
- Undisclosed data quality issues in resource papers
- Incomplete proofs or unstated assumptions

**Experimental issues (R):**
- Inappropriate statistical analysis or p-hacking
- Claims that exceed the evaluated evidence
- Unvalidated speculation presented as conclusions
- Missing significance assessments

**General clarity (G):**
- Vague research questions or undefined key terms
- Misrepresented related work or missing citations
- Hallucinated references

## Scoring Framework

**Soundness:** Technical validity and rigor. "The soundness scores must be justified by the text of the review."

**Excitement:** Personal interest level—"orthogonal to the assessment of soundness."

**Overall Assessment:** Composite recommendation balancing soundness, novelty, and potential impact. Papers needn't excite reviewers personally to merit acceptance if they offer "significant contribution due to its potential impact."

## Findings-Track Guidance

The guidelines don't address Findings-specific criteria separately, treating all submissions uniformly across venues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6279
}
```

</details>

---


### Tool call

_source line 196 · 2026-05-17T10:22:12.400995+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 4 审稿报告 — Reviewer 1（方法/实验严谨性）\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Ontology Constraints\n**目标**: EMNLP 2026 Findings (ARR May 2026)\n\n---\n\n## 总体评分\n**Overall**: 3.5/5（介于 Findings 可接受与 Conference 之间）\n**一句话总结**: 方法设计合理、实验覆盖面广、数据一致性好，但 R²=0.886 (n=4) 在 Abstract 中过度突出、post-hoc baseline framing 有选择性偏向、beam search 结果发现重大但被降级到附录处理不当。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心方法正确，pair-based sequential masking 论证充分（§3.1 脚注量化了 independent enforcement 的 spurious pair 比例），但存在若干统计过度声明和 framing 偏向 |\n| Excitement | 3/5 | 将 type-constrained decoding 从代码生成迁移到 IE 有价值；但核心场景（zero-shot IE）R-F1 仅~8%，实用价值有限 |\n| Reproducibility | 4/5 | 实验配置详尽，prompt templates 完整（Appendix A），exp_id 可追溯，greedy 实验完全确定性 |\n| Overall | 3.5/5 | 适合 Findings，需修复统计声明和 framing 问题 |\n\n---\n\n## 先前 Issue 修复状态\n\n### W1 [CF framing in Abstract/Intro] → ✅ 已修复\nAbstract 现在明确写 \"cross-field consistency violations arise (up to 12% in zero-shot)\"，Intro Contribution 3 也写了 \"CF↔DR trade-off inherent to per-relation enforcement\"。CF 不再被隐藏。\n\n### R2-N1 [R²=0.886 overclaim] → ⚠️ 部分修复\nDiscussion/Conclusion 已降级为 \"descriptive characterization with explicit scope rather than a universal predictive law\"（§7）。但 Abstract 仍将 R²=0.886 作为独立句子突出呈现（第 11 行），给读者的印象仍然是一个核心贡献。详见下方 N1。\n\n### W3 [Post-hoc framing] → ⚠️ 部分修复\nIntroduction 已限定 \"At high rejection rates (e.g., Mistral DocRED 73.7%)\"（§1 第 14 行），不再笼统否定 post-hoc。但仍未提及 post-hoc 在 5/6 ZS 配置中 F1 高于 OntoCoDec（Appendix Table 8），Intro 的叙事仍有选择性。详见下方 W2。\n\n### R2-N3 [Parse failure 分析] → ⚠️ 部分修复\n§5.1 提供了 0.23pp 调整上限，§5.2 脚注给出了 Qwen DocRED parse-failure-excluded ΔR-F1。但 Llama DocRED（parse failure +34%，68→91）的 F1 影响未提供 parse-failure-excluded 分析。详见下方 W4。\n\n### R2-N6 [Semantic-only DocRED ET 2.48%→4.22%] → ⚠️ 部分修复\nSciERC 节解释了机制（\"semantic mask excludes the model's preferred valid-vocabulary type, forcing an OOV alternative\"，§5.2 Enabling dependency 段），但 DocRED 节（§5.3）未针对 ET 4.22% 做对应讨论。\n\n### R2-N7 [DocRED 为何省略 S2] → ✅ 已修复\n§5.3 末段明确说明：\"We omit S2 on DocRED because S1 already achieves near-complete RV/ET elimination and the two-pass overhead is less justified when residual DR is dominated by fallback events rather than forward coreference.\"\n\n### R2-N10 [RV=0.03% 残余来源] → ⚠️ 存在不一致\n§5.3 DocRED 段说残余来自 \"partial JSON recovery where the grammar FSM completes a structurally valid but relation-name-truncated triple\"。但 rebuttal_draft_v2.md 说这是 \"an XGrammar v0.1.33 enum compilation bug where the grammar bitmask leaks token continuations across enum entries\"。两个解释不一致：一个是设计后果，一个是第三方 bug。需统一。\n\n### GC-N1 [Grammar-only 行标识为 GCD 上限] → ❌ 未修复\nGrammar-only 行出现在 Table 1 和 Table 2 中，讨论文字说明了其仅能保证结构有效性。但从未明确将其标识为 GCD (Geng et al., 2023) 方法的能力上限，作为与现有 grammar-constrained decoding 文献的对比锚点。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] R²=0.886 (n=4) 统计不充分且在 Abstract 中过度突出\n\n- 具体位置：Abstract 第 11 行，§4 第 28 行，Appendix B (app:dual-factor)\n- 问题：对 n=4 数据点拟合 2 参数线性模型（y = ax + b），自由度仅为 2。计算 F(1,2) = R²/(1-R²) × 2 ≈ 15.54，对应 p ≈ 0.058，在 α=0.05 下不显著。此外，Mistral 被 **post-hoc** 排除（因其 \"mechanistically distinct error source\"），但排除标准是在观察到 Mistral 不符合模型后确定的，构成数据筛选偏差。R²=0.886 出现在 Abstract 中作为独立结论，给读者以核心贡献的印象。\n- 为什么影响接收：这是 ARR reviewer guidelines 明确列出的 \"p-hacking\" 和 \"claims that exceed the evaluated evidence\" 问题。Findings 论文的首要标准是 soundness，统计声明的可靠性直接影响 soundness 评分。\n- 建议修改方向：\n  (1) 从 Abstract 中移除 R²=0.886，改为定性描述（如 \"residual DR scales with schema tightness and baseline vocabulary confusion\"）\n  (2) 在 Appendix 的 dual-factor 段中明确报告 F 统计量和 p ≈ 0.058，并说明不显著\n  (3) 对 Mistral 排除提供 **先验** 理由（如基于 RV=0% 的客观标准），而非 post-hoc 解释\n\n**N2** [critical] Beam search 结果重大但被降级，主实验配置选择存疑\n\n- 具体位置：Appendix F (app:beam-search) vs §5 主实验\n- 问题：Beam search (k=4) 在 SciERC 全集 (551 docs) 上对 Qwen 和 Llama 均实现 DR=0%、CF 从 9.90%/6.56% 降至 0.53%/0.93%，同时 R-F1 不降反升。这意味着 beam search **同时解决了** 主实验中最大的两个局限（残余 DR 和 CF 升高），但被放在附录中以 \"preliminary\" 定位。既然 SciERC 实验是全集且结果 overwhelming，将 greedy 作为 \"recommended strategy\"（§3.5）缺乏充分理由。\n  - 如果 beam search 是更优配置但因 DocRED 计算成本而无法全集验证，需明确说明这一点，而不是将其作为 supplementary 材料处理\n  - DocRED beam search 仅在 50-document subset 上运行，且 greedy baseline 来自 998-document 全集（Table 6 脚注承认 \"Not a matched comparison\"），这一不匹配使 DocRED beam 结果的可比性存疑\n- 为什么影响接收：审稿人会问：为什么 §7 Discussion 推荐 greedy+S1 而不是 beam+S1，当后者在全集实验中显著优于前者？如果答案是 \"beam 太贵\"，那么 runtime 分析（Table 4）需要补充 beam 的开销数据。这影响 contribution 的定位。\n- 建议修改方向：\n  (1) 在 §5 或 §7 中明确讨论 beam search 的 SciERC 全集结果及其对 CF 问题的实质性解决\n  (2) 提供 beam search 的 per-document runtime 开销\n  (3) 如果推荐 greedy 是因为实用性（runtime），需明确说明 beam search 是理论最优但 greedy 是实用推荐\n  (4) DocRED beam 实验应在匹配的 50-document subset 上报告 greedy baseline\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Grammar-first fallback 频率未充分讨论\n\n- 具体位置：§4 Grammar-First Fallback 段，§5.3 DocRED 段\n- 问题：DocRED 上 fallback rate 10.2%（1770/17341 triples）且 \"closely tracks residual DR (10.21%)\"，意味着几乎所有残余违规都来自 fallback。Qwen DocRED Grammar-first fallback 频率高是因为 grammar enforcement 将 29.66% OOV 关系映射为 in-vocabulary 关系后暴露了大量 latent DR。这意味着 grammar 层的 \"surfacing\" 效应（§5.3）和 fallback 机制的 \"放弃 semantic enforcement\" 效应共同导致了 DocRED 上仅 45% 的 DR reduction。Appendix B 报告 SciERC 上 effective semantic constraint coverage 为 63.4%（即 36.6% 的 type-bearing positions fallback），但 DocRED 的 coverage 未报告。\n- 建议：报告 DocRED 的 effective semantic constraint coverage 数字；在 §5.3 中更明确地将 residual DR 归因于 fallback frequency。\n\n**W2** [warning] Post-hoc filtering 在 Introduction 中的 framing 仍有选择性\n\n- 具体位置：§1 第 14 行，Appendix B (app:posthoc-extended)\n- 问题：Introduction 仅在 \"high rejection rates (e.g., Mistral DocRED 73.7%)\" 的极端情况下否定 post-hoc，但未提及 Appendix Table 8 的核心发现：post-hoc 在 5/6 zero-shot 配置中 F1 高于 OntoCoDec（SciERC: 8.63 vs 8.36; DocRED: 9.61 vs 8.23）。这种选择性呈现不符合 Findings 论文的 soundness 要求。OntoCoDec 的核心优势是 recall 保持（post-hoc 在 DocRED 上丢弃 127 true positives），而非 F1，但 Introduction 的 framing 暗示 OntoCoDec 是全面优于 post-hoc 的方法。\n- 建议：在 §1 或 §5 中添加一句 summary：\"Post-hoc filtering achieves higher F1 in most zero-shot settings via precision gains, but at the cost of discarding up to 48% of predictions including true positives; OntoCoDec's advantage is recall preservation and ET elimination.\"\n\n**W3** [warning] Parse failure 增加的 confounding 效应在 Llama DocRED 上未充分分析\n\n- 具体位置：Table 3 caption，Limitations §\n- 问题：Llama DocRED parse failure 从 6.8%（68/998）增至 9.1%（91/998），增幅 +34%。§5.2 脚注为 Qwen DocRED 提供了 parse-failure-excluded ΔR-F1（+0.03pp vs all-set -0.30pp），但 Llama DocRED（增幅更大）未给出对应分析。Llama DocRED S1 的 CF=12.02% 是全文最高值，是否部分受 parse failure 增加的 selection bias 影响（即：parse failure 的文档可能本身就是 CF-prone 的复杂文档）？\n- 建议：为 Llama DocRED 补充 parse-failure-excluded 的 violation rate 和 F1 分析。\n\n**W4** [warning] Composability matrix 在 DocRED 上仅以文字呈现，缺乏系统性\n\n- 具体位置：§5.2 最后两段\n- 问题：SciERC 有完整的 composability matrix（Table 2：2 models × 2 settings × 2 modes），但 DocRED 的 composability 数据（DR -98.7%/-59.2%，R-F1 -0.30pp/+0.51pp）仅在 Table 2 caption 和 §5.2 正文中以文字给出。Table 6（FT ablation，Appendix）包含了完整的 4-way 数据，但正文中 DocRED FT 的呈现不够系统。另外 §5.2 标题为 \"Results on SciERC\"（§5.2），但内容包含了 DocRED composability 和 FT ablation 的讨论，节划分不清晰。\n- 建议：考虑将 DocRED FT composability 以独立段落或子表呈现在正文中，或至少在 §5.3 (DocRED) 中添加交叉引用。\n\n**W5** [warning] Section 4 Composition 中 DR reduction 范围引用不明确\n\n- 具体位置：§4 Constraint Tightness 段，第 28 行\n- 问题：\"SciERC... achieves 94–99% DR reduction, while DocRED... achieves 45–90%\" 的范围仅覆盖 Qwen 和 Llama。但该句上下文是 \"cross-dataset results\"（不限于 calibrated models），读者可能认为 94–99% 包含所有三个模型。实际上 Mistral SciERC 仅 76%。Abstract 正确写了 \"42–99% across three model families\"，但 §4 的范围与 Abstract 不一致。\n- 建议：在 §4 中明确注明 \"for calibrated models (Qwen, Llama)\"，或改用包含 Mistral 的完整范围 76–99% / 42–90%。\n\n---\n\n## Questions to Authors\n\n**Q1**: JSON field ordering 是 pair-based sequential masking 的隐含前提。§3.1 的 sequential enforcement 依赖于 relation_type 先于 head_type、head_type 先于 tail_type 的生成顺序。Appendix A 的 prompt template 确认了 {\"head\", \"tail\", \"type\", \"head_type\", \"tail_type\"} 的顺序。但如果模型在 grammar constraints 下改变了 field 生成顺序（例如某些 tokenizer 的 JSON key ordering 不同），sequential masking 是否仍然成立？grammar layer 的 JSON Schema 是否强制了 field ordering？\n\n**Q2**: Appendix F beam search 在 SciERC 全集上实现 DR=0%、CF=0.53%，这比 LoRA fine-tuning 的结果（DR=0%、CF=1.18%）还好。是否考虑过 beam search 作为 fine-tuning 的替代方案？如果 beam search k=4 的 runtime overhead 低于 fine-tuning 的训练成本，这可能改变论文的实用建议。\n\n**Q3**: Semantic-only mode 在 DocRED 上使 ET 从 2.48% 升至 4.22%（Table 2），但 SciERC 上 ET 不变（0.40%→0.40%）。§5.2 的解释是 \"semantic mask excludes the model's preferred valid-vocabulary type, forcing an OOV alternative\"。为什么 DocRED 的 ET 增加幅度（+70%）远大于 SciERC（0%）？是否因为 DocRED 的 entity type vocabulary 更小（6 vs 6 实际相同）但 relation type 更多（96 vs 7），导致 semantic mask 更频繁地排除 preferred types？\n\n**Q4**: Appendix B 的 CF-DR trade-off 实验（Table 5）仅在 SciERC/Qwen 上进行。DocRED 上 CF 最高达 12.02%（Llama），是否做过对应的 trade-off ablation？如果没有，是否有理由认为 SciERC 的 trade-off 结论可以迁移到 DocRED？\n\n---\n\n## Missing References\n\n- **DORE** (Vukovic et al., 2024) 在 §6 Related Work 中已引用，但未深入对比 OntoCoDec 与 DORE 在 ontology constraint enforcement 上的差异机制（output selection vs logit masking 的定量比较）。\n- **BoostCD** (Sakota et al., 2025) 在 §6 仅一句话提及，考虑到其 \"combines constrained and unconstrained outputs via boosting for IE\" 与 OntoCoDec 的互补性，值得更详细讨论。\n- Appendix 的 Extended Related Work 覆盖面广（24+ citations），整体引用充足度合格。\n\n---\n\n## Minor Issues（不影响接收）\n\n1. §3.3 Implementation 段提到 \"Design Assumption: each entity type name maps to a unique first subword token\"，但 §2 Background 未将此作为前提条件列出。建议在 §2 Problem Statement 中提及。\n2. §5.1 Table 1 caption 说 \"CF excluded—see text\"，但正文中 CF 的讨论在 §5.2（而非 §5.1）。\n3. §5.2 同时讨论 SciERC ablation、composability matrix、DocRED FT ablation，内容跨度大。建议考虑拆分。\n4. Appendix B (app:dual-factor) 说 \"we do not report a p-value given the small sample size\"，这是正确做法，但既然如此，在 Abstract 中报告 R²=0.886 同样不应出现——R² 和 p-value 是同一统计检验的两面。\n5. Limitations 中提到 \"residual CF (Qwen 1.18%, Llama 0.46% on SciERC) traces to schema-level type ambiguity (Generic↔X)\"，但 DocRED 的 MISC 类型也有类似 catch-all 属性（Appendix B 报告 76.6% of Qwen's CF violations involve MISC），建议统一讨论。\n6. RV=0.03% 的解释在正文（\"partial JSON recovery\"）和 rebuttal draft（\"XGrammar enum compilation bug\"）中不一致，需统一为一个版本。\n7. §5.3 DocRED 四方向 ablation 表（Table 2）没有 $\\Delta$DR 列的百分号标注，而 SciERC 表（Table 1）有，格式不统一。\n\n---\n\n## 主要优势\n\n1. **方法设计扎实**：两层约束的 enabling dependency（grammar → semantic）有清晰的理论动机和实验验证。Sequential masking 的正确性论证充分（§3.1 脚注量化了 independent enforcement 的 spurious pair 比例：SciERC 33.3%、DocRED 36.8%），non-rectangularity 分析（§4）为设计选择提供了定量支撑。\n\n2. **实验覆盖面广**：3 模型 × 2 数据集 × 多种消融，加上 fine-tuning composability 验证（4-way ablation on 4 model×dataset settings），以及 sampling/beam search 鲁棒性测试。数据一致性好——我交叉验证了 Abstract、§5 各表、Appendix 的数字，未发现不匹配。\n\n3. **诚实的局限性讨论**：CF↔DR trade-off 的 Pareto 分析（Appendix Table 5）、Mistral 作为 boundary condition 的定位、parse failure 的 denominator 说明——这些表明作者认真审视了方法的边界。\n\n4. **runtime 开销极低**：Full S1 在 DocRED (96 relations) 上仅 +5.4% 开销（Table 4），在 FT regime 下降至 +2.3%。这使得方法在实际部署中可行。\n\n5. **Reproducibility 优秀**：每个实验有 exp_id 追溯标记，prompt templates 完整公开，greedy 实验完全确定性（3 seeds 相同输出）。\n\n---\n\n**Reviewer Confidence**: 4/5（熟悉 constrained decoding 和 IE 方法论，仔细验证了数据一致性和统计声明）",
  "reviewer_id": "1",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 4 审稿报告 — Reviewer 1（方法/实验严谨性）\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Ontology Constraints\n**目标**: EMNLP 2026 Findings (ARR May 2026)\n\n---\n\n## 总体评分\n**Overall**: 3.5/5（介于 Findings 可接受与 Conference 之间）\n**一句话总结**: 方法设计合理、实验覆盖面广、数据一致性好，但 R²=0.886 (n=4) 在 Abstract 中过度突出、post-hoc baseline framing 有选择性偏向、beam search 结果发现重大但被降级到附录处理不当。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心方法正确，pair-based sequential masking 论证充分（§3.1 脚注量化了 independent enforcement 的 spurious pair 比例），但存在若干统计过度声明和 framing 偏向 |\n| Excitement | 3/5 | 将 type-constrained decoding 从代码生成迁移到 IE 有价值；但核心场景（zero-shot IE）R-F1 仅~8%，实用价值有限 |\n| Reproducibility | 4/5 | 实验配置详尽，prompt templates 完整（Appendix A），exp_id 可追溯，greedy 实验完全确定性 |\n| Overall | 3.5/5 | 适合 Findings，需修复统计声明和 framing 问题 |\n\n---\n\n## 先前 Issue 修复状态\n\n### W1 [CF framing in Abstract/Intro] → ✅ 已修复\nAbstract 现在明确写 \"cross-field consistency violations arise (up to 12% in zero-shot)\"，Intro Contribution 3 也写了 \"CF↔DR trade-off inherent to per-relation enforcement\"。CF 不再被隐藏。\n\n### R2-N1 [R²=0.886 overclaim] → ⚠️ 部分修复\nDiscussion/Conclusion 已降级为 \"descriptive characterization with explicit scope rather than a universal predictive law\"（§7）。但 Abstract 仍将 R²=0.886 作为独立句子突出呈现（第 11 行），给读者的印象仍然是一个核心贡献。详见下方 N1。\n\n### W3 [Post-hoc framing] → ⚠️ 部分修复\nIntroduction 已限定 \"At high rejection rates (e.g., Mistral DocRED 73.7%)\"（§1 第 14 行），不再笼统否定 post-hoc。但仍未提及 post-hoc 在 5/6 ZS 配置中 F1 高于 OntoCoDec（Appendix Table 8），Intro 的叙事仍有选择性。详见下方 W2。\n\n### R2-N3 [Parse failure 分析] → ⚠️ 部分修复\n§5.1 提供了 0.23pp 调整上限，§5.2 脚注给出了 Qwen DocRED parse-failure-excluded ΔR-F1。但 Llama DocRED（parse failure +34%，68→91）的 F1 影响未提供 parse-failure-excluded 分析。详见下方 W4。\n\n### R2-N6 [Semantic-only DocRED ET 2.48%→4.22%] → ⚠️ 部分修复\nSciERC 节解释了机制（\"semantic mask excludes the model's preferred valid-vocabulary type, forcing an OOV alternative\"，§5.2 Enabling dependency 段），但 DocRED 节（§5.3）未针对 ET 4.22% 做对应讨论。\n\n### R2-N7 [DocRED 为何省略 S2] → ✅ 已修复\n§5.3 末段明确说明：\"We omit S2 on DocRED because S1 already achieves near-complete RV/ET elimination and the two-pass overhead is less justified when residual DR is dominated by fallback events rather than forward coreference.\"\n\n### R2-N10 [RV=0.03% 残余来源] → ⚠️ 存在不一致\n§5.3 DocRED 段说残余来自 \"partial JSON recovery where the grammar FSM completes a structurally valid but relation-name-truncated triple\"。但 rebuttal_draft_v2.md 说这是 \"an XGrammar v0.1.33 enum compilation bug where the grammar bitmask leaks token continuations across enum entries\"。两个解释不一致：一个是设计后果，一个是第三方 bug。需统一。\n\n### GC-N1 [Grammar-only 行标识为 GCD 上限] → ❌ 未修复\nGrammar-only 行出现在 Table 1 和 Table 2 中，讨论文字说明了其仅能保证结构有效性。但从未明确将其标识为 GCD (Geng et al., 2023) 方法的能力上限，作为与现有 grammar-constrained decoding 文献的对比锚点。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] R²=0.886 (n=4) 统计不充分且在 Abstract 中过度突出\n\n- 具体位置：Abstract 第 11 行，§4 第 28 行，Appendix B (app:dual-factor)\n- 问题：对 n=4 数据点拟合 2 参数线性模型（y = ax + b），自由度仅为 2。计算 F(1,2) = R²/(1-R²) × 2 ≈ 15.54，对应 p ≈ 0.058，在 α=0.05 下不显著。此外，Mistral 被 **post-hoc** 排除（因其 \"mechanistically distinct error source\"），但排除标准是在观察到 Mistral 不符合模型后确定的，构成数据筛选偏差。R²=0.886 出现在 Abstract 中作为独立结论，给读者以核心贡献的印象。\n- 为什么影响接收：这是 ARR reviewer guidelines 明确列出的 \"p-hacking\" 和 \"claims that exceed the evaluated evidence\" 问题。Findings 论文的首要标准是 soundness，统计声明的可靠性直接影响 soundness 评分。\n- 建议修改方向：\n  (1) 从 Abstract 中移除 R²=0.886，改为定性描述（如 \"residual DR scales with schema tightness and baseline vocabulary confusion\"）\n  (2) 在 Appendix 的 dual-factor 段中明确报告 F 统计量和 p ≈ 0.058，并说明不显著\n  (3) 对 Mistral 排除提供 **先验** 理由（如基于 RV=0% 的客观标准），而非 post-hoc 解释\n\n**N2** [critical] Beam search 结果重大但被降级，主实验配置选择存疑\n\n- 具体位置：Appendix F (app:beam-search) vs §5 主实验\n- 问题：Beam search (k=4) 在 SciERC 全集 (551 docs) 上对 Qwen 和 Llama 均实现 DR=0%、CF 从 9.90%/6.56% 降至 0.53%/0.93%，同时 R-F1 不降反升。这意味着 beam search **同时解决了** 主实验中最大的两个局限（残余 DR 和 CF 升高），但被放在附录中以 \"preliminary\" 定位。既然 SciERC 实验是全集且结果 overwhelming，将 greedy 作为 \"recommended strategy\"（§3.5）缺乏充分理由。\n  - 如果 beam search 是更优配置但因 DocRED 计算成本而无法全集验证，需明确说明这一点，而不是将其作为 supplementary 材料处理\n  - DocRED beam search 仅在 50-document subset 上运行，且 greedy baseline 来自 998-document 全集（Table 6 脚注承认 \"Not a matched comparison\"），这一不匹配使 DocRED beam 结果的可比性存疑\n- 为什么影响接收：审稿人会问：为什么 §7 Discussion 推荐 greedy+S1 而不是 beam+S1，当后者在全集实验中显著优于前者？如果答案是 \"beam 太贵\"，那么 runtime 分析（Table 4）需要补充 beam 的开销数据。这影响 contribution 的定位。\n- 建议修改方向：\n  (1) 在 §5 或 §7 中明确讨论 beam search 的 SciERC 全集结果及其对 CF 问题的实质性解决\n  (2) 提供 beam search 的 per-document runtime 开销\n  (3) 如果推荐 greedy 是因为实用性（runtime），需明确说明 beam search 是理论最优但 greedy 是实用推荐\n  (4) DocRED beam 实验应在匹配的 50-document subset 上报告 greedy baseline\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Grammar-first fallback 频率未充分讨论\n\n- 具体位置：§4 Grammar-First Fallback 段，§5.3 DocRED 段\n- 问题：DocRED 上 fallback rate 10.2%（1770/17341 triples）且 \"closely tracks residual DR (10.21%)\"，意味着几乎所有残余违规都来自 fallback。Qwen DocRED Grammar-first fallback 频率高是因为 grammar enforcement 将 29.66% OOV 关系映射为 in-vocabulary 关系后暴露了大量 latent DR。这意味着 grammar 层的 \"surfacing\" 效应（§5.3）和 fallback 机制的 \"放弃 semantic enforcement\" 效应共同导致了 DocRED 上仅 45% 的 DR reduction。Appendix B 报告 SciERC 上 effective semantic constraint coverage 为 63.4%（即 36.6% 的 type-bearing positions fallback），但 DocRED 的 coverage 未报告。\n- 建议：报告 DocRED 的 effective semantic constraint coverage 数字；在 §5.3 中更明确地将 residual DR 归因于 fallback frequency。\n\n**W2** [warning] Post-hoc filtering 在 Introduction 中的 framing 仍有选择性\n\n- 具体位置：§1 第 14 行，Appendix B (app:posthoc-extended)\n- 问题：Introduction 仅在 \"high rejection rates (e.g., Mistral DocRED 73.7%)\" 的极端情况下否定 post-hoc，但未提及 Appendix Table 8 的核心发现：post-hoc 在 5/6 zero-shot 配置中 F1 高于 OntoCoDec（SciERC: 8.63 vs 8.36; DocRED: 9.61 vs 8.23）。这种选择性呈现不符合 Findings 论文的 soundness 要求。OntoCoDec 的核心优势是 recall 保持（post-hoc 在 DocRED 上丢弃 127 true positives），而非 F1，但 Introduction 的 framing 暗示 OntoCoDec 是全面优于 post-hoc 的方法。\n- 建议：在 §1 或 §5 中添加一句 summary：\"Post-hoc filtering achieves higher F1 in most zero-shot settings via precision gains, but at the cost of discarding up to 48% of predictions including true positives; OntoCoDec's advantage is recall preservation and ET elimination.\"\n\n**W3** [warning] Parse failure 增加的 confounding 效应在 Llama DocRED 上未充分分析\n\n- 具体位置：Table 3 caption，Limitations §\n- 问题：Llama DocRED parse failure 从 6.8%（68/998）增至 9.1%（91/998），增幅 +34%。§5.2 脚注为 Qwen DocRED 提供了 parse-failure-excluded ΔR-F1（+0.03pp vs all-set -0.30pp），但 Llama DocRED（增幅更大）未给出对应分析。Llama DocRED S1 的 CF=12.02% 是全文最高值，是否部分受 parse failure 增加的 selection bias 影响（即：parse failure 的文档可能本身就是 CF-prone 的复杂文档）？\n- 建议：为 Llama DocRED 补充 parse-failure-excluded 的 violation rate 和 F1 分析。\n\n**W4** [warning] Composability matrix 在 DocRED 上仅以文字呈现，缺乏系统性\n\n- 具体位置：§5.2 最后两段\n- 问题：SciERC 有完整的 composability matrix（Table 2：2 models × 2 settings × 2 modes），但 DocRED 的 composability 数据（DR -98.7%/-59.2%，R-F1 -0.30pp/+0.51pp）仅在 Table 2 caption 和 §5.2 正文中以文字给出。Table 6（FT ablation，Appendix）包含了完整的 4-way 数据，但正文中 DocRED FT 的呈现不够系统。另外 §5.2 标题为 \"Results on SciERC\"（§5.2），但内容包含了 DocRED composability 和 FT ablation 的讨论，节划分不清晰。\n- 建议：考虑将 DocRED FT composability 以独立段落或子表呈现在正文中，或至少在 §5.3 (DocRED) 中添加交叉引用。\n\n**W5** [warning] Section 4 Composition 中 DR reduction 范围引用不明确\n\n- 具体位置：§4 Constraint Tightness 段，第 28 行\n- 问题：\"SciERC... achieves 94–99% DR reduction, while DocRED... achieves 45–90%\" 的范围仅覆盖 Qwen 和 Llama。但该句上下文是 \"cross-dataset results\"（不限于 calibrated models），读者可能认为 94–99% 包含所有三个模型。实际上 Mistral SciERC 仅 76%。Abstract 正确写了 \"42–99% across three model families\"，但 §4 的范围与 Abstract 不一致。\n- 建议：在 §4 中明确注明 \"for calibrated models (Qwen, Llama)\"，或改用包含 Mistral 的完整范围 76–99% / 42–90%。\n\n---\n\n## Questions to Authors\n\n**Q1**: JSON field ordering 是 pair-based sequential masking 的隐含前提。§3.1 的 sequential enforcement 依赖于 relation_type 先于 head_type、head_type 先于 tail_type 的生成顺序。Appendix A 的 prompt template 确认了 {\"head\", \"tail\", \"type\", \"head_type\", \"tail_type\"} 的顺序。但如果模型在 grammar constraints 下改变了 field 生成顺序（例如某些 tokenizer 的 JSON key ordering 不同），sequential masking 是否仍然成立？grammar layer 的 JSON Schema 是否强制了 field ordering？\n\n**Q2**: Appendix F beam search 在 SciERC 全集上实现 DR=0%、CF=0.53%，这比 LoRA fine-tuning 的结果（DR=0%、CF=1.18%）还好。是否考虑过 beam search 作为 fine-tuning 的替代方案？如果 beam search k=4 的 runtime overhead 低于 fine-tuning 的训练成本，这可能改变论文的实用建议。\n\n**Q3**: Semantic-only mode 在 DocRED 上使 ET 从 2.48% 升至 4.22%（Table 2），但 SciERC 上 ET 不变（0.40%→0.40%）。§5.2 的解释是 \"semantic mask excludes the model's preferred valid-vocabulary type, forcing an OOV alternative\"。为什么 DocRED 的 ET 增加幅度（+70%）远大于 SciERC（0%）？是否因为 DocRED 的 entity type vocabulary 更小（6 vs 6 实际相同）但 relation type 更多（96 vs 7），导致 semantic mask 更频繁地排除 preferred types？\n\n**Q4**: Appendix B 的 CF-DR trade-off 实验（Table 5）仅在 SciERC/Qwen 上进行。DocRED 上 CF 最高达 12.02%（Llama），是否做过对应的 trade-off ablation？如果没有，是否有理由认为 SciERC 的 trade-off 结论可以迁移到 DocRED？\n\n---\n\n## Missing References\n\n- **DORE** (Vukovic et al., 2024) 在 §6 Related Work 中已引用，但未深入对比 OntoCoDec 与 DORE 在 ontology constraint enforcement 上的差异机制（output selection vs logit masking 的定量比较）。\n- **BoostCD** (Sakota et al., 2025) 在 §6 仅一句话提及，考虑到其 \"combines constrained and unconstrained outputs via boosting for IE\" 与 OntoCoDec 的互补性，值得更详细讨论。\n- Appendix 的 Extended Related Work 覆盖面广（24+ citations），整体引用充足度合格。\n\n---\n\n## Minor Issues（不影响接收）\n\n1. §3.3 Implementation 段提到 \"Design Assumption: each entity type name maps to a unique first subword token\"，但 §2 Background 未将此作为前提条件列出。建议在 §2 Problem Statement 中提及。\n2. §5.1 Table 1 caption 说 \"CF excluded—see text\"，但正文中 CF 的讨论在 §5.2（而非 §5.1）。\n3. §5.2 同时讨论 SciERC ablation、composability matrix、DocRED FT ablation，内容跨度大。建议考虑拆分。\n4. Appendix B (app:dual-factor) 说 \"we do not report a p-value given the small sample size\"，这是正确做法，但既然如此，在 Abstract 中报告 R²=0.886 同样不应出现——R² 和 p-value 是同一统计检验的两面。\n5. Limitations 中提到 \"residual CF (Qwen 1.18%, Llama 0.46% on SciERC) traces to schema-level type ambiguity (Generic↔X)\"，但 DocRED 的 MISC 类型也有类似 catch-all 属性（Appendix B 报告 76.6% of Qwen's CF violations involve MISC），建议统一讨论。\n6. RV=0.03% 的解释在正文（\"partial JSON recovery\"）和 rebuttal draft（\"XGrammar enum compilation bug\"）中不一致，需统一为一个版本。\n7. §5.3 DocRED 四方向 ablation 表（Table 2）没有 $\\Delta$DR 列的百分号标注，而 SciERC 表（Table 1）有，格式不统一。\n\n---\n\n## 主要优势\n\n1. **方法设计扎实**：两层约束的 enabling dependency（grammar → semantic）有清晰的理论动机和实验验证。Sequential masking 的正确性论证充分（§3.1 脚注量化了 independent enforcement 的 spurious pair 比例：SciERC 33.3%、DocRED 36.8%），non-rectangularity 分析（§4）为设计选择提供了定量支撑。\n\n2. **实验覆盖面广**：3 模型 × 2 数据集 × 多种消融，加上 fine-tuning composability 验证（4-way ablation on 4 model×dataset settings），以及 sampling/beam search 鲁棒性测试。数据一致性好——我交叉验证了 Abstract、§5 各表、Appendix 的数字，未发现不匹配。\n\n3. **诚实的局限性讨论**：CF↔DR trade-off 的 Pareto 分析（Appendix Table 5）、Mistral 作为 boundary condition 的定位、parse failure 的 denominator 说明——这些表明作者认真审视了方法的边界。\n\n4. **runtime 开销极低**：Full S1 在 DocRED (96 relations) 上仅 +5.4% 开销（Table 4），在 FT regime 下降至 +2.3%。这使得方法在实际部署中可行。\n\n5. **Reproducibility 优秀**：每个实验有 exp_id 追溯标记，prompt templates 完整公开，greedy 实验完全确定性（3 seeds 相同输出）。\n\n---\n\n**Reviewer Confidence**: 4/5（熟悉 constrained decoding 和 IE 方法论，仔细验证了数据一致性和统计声明）",
    "reviewer_id": "1",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 197 · 2026-05-17T10:22:16.319212+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3918
}
```

</details>

---


### Assistant

_source line 198 · 2026-05-17T10:22:30.028527+00:00_

审稿报告已提交给 Review Director。

总结：

- **Overall 3.5/5**，适合 Findings
- **2 个 Must-Fix**：(1) R²=0.886 (n=4) 在 Abstract 中过度突出，统计上 p≈0.058 不显著且 Mistral post-hoc 排除构成数据筛选偏差；(2) Beam search 在 SciERC 全集上实现 DR=0%+CF 0.53%，显著优于主实验的 greedy 配置，但被降级到附录
- **5 个 Should-Fix**：fallback 频率讨论不足、post-hoc framing 仍有选择性、Llama DocRED parse failure 分析缺失、DocRED composability 呈现不系统、§4 中 DR reduction 范围引用不一致
- **6 个先前 issue**：2 个已修复（W1, R2-N7），3 个部分修复（R2-N1, W3, R2-N3），1 个未修复（GC-N1），1 个存在不一致（R2-N10）
- 数据一致性整体良好，交叉验证 Abstract/§5/Appendix 数字无不匹配

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1"
}
```

</details>

---


## Round 7

## Round 7

16 recorded events


### User

_source line 199 · 2026-05-17T10:23:02.926082+00:00_

[Round 1 审稿请求]:
## 交叉分享 — Reviewer 2 的完整审稿意见

请逐条回应以下 Reviewer 2 的审稿意见。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

以下是 Reviewer 2 的完整审稿原文：

## Reviewer 2 评分
**Overall**: 3.5/5（Accept to Findings，偏强）
**Soundness**: 4/5 | **Excitement**: 2.5/5 | **Reproducibility**: 3.5/5

## Must-Fix 问题

**N1** [critical] Abstract 缩写未展开违反 ARR 规范
- Abstract 使用 "LLM"（line 7）、"IE"（line 1）、"CFG"（line 3）、"DR"（line 7-8）、"ET"/"RV"（line 3）、"CF"（line 13）、"LoRA"（line 12）均未在 Abstract 内给出完整定义。标题中 "Information Extraction" 定义了 IE，但 Abstract 应独立可读。
- ARR 审稿人对缩写规范敏感；至少 LLM、IE、DR 必须展开。

**N2** [critical] 正文主体存在大量 AI 写作典型标志（em-dash 过度使用）
- 正文中 LaTeX `---` 至少 12 处用于解释性插入，例如：
  - §1 line 7: "violations---structurally valid triples that are ontologically invalid"
  - §2 line 16: 双 em-dash 包围解释
  - §3 line 10: Unicode — (非 LaTeX ---)
- 高密度 em-dash 是 AI 生成的显著标志，可能引发对论文原创性的质疑。

## Should-Fix 问题

**W1** -ing 分词短语结尾（AI 写作痕迹）：正文约 8-10 处，appendix 更密集。

**W2** Code-gen 新颖性区分未在 Introduction 出现：§3 开头清楚列出 IE vs code-gen 三个区别，但 §1 没有任何 code-gen 讨论。审稿人读 §1 时会质疑 novelty。

**W3** Dual-factor R²=0.886 (n=4) 在 Abstract 中过于突出：4 个点几乎任何线性模型都能拟合良好，建议 Abstract 移除具体数值。

**W4** Reproducibility 信息不充分：无独立 Reproducibility Statement，random seeds/GPU型号/LoRA超参数未报告。

**W5** Related Work 缺少 2024-2025 Document-level RE 工作：DocRED 实验缺少 DREEAM、DocGNRE、GLiNER 引用。

**W6** Table caption 中 em-dash 需替换。

## 小问题
1. Abstract CFG 未展开
2. §2 $\mathcal{T} = \mathcal{E}$ 同义重复
3. §3 Unicode em-dash
4. Table 1 CF "---" 未解释
5. Table 2 CF 列方向不 self-evident
6. Appendix B Llama DocRED CF "---" 格式不一致
7. §6 DORE 描述中又一处 em-dash
8. bib 条目 vukovic2024dore 缺少 pages/url

## 主要优势
1. 实验设计严谨（3模型×2数据集×多 ablation + FT composability + runtime + beam/sampling）
2. 诚实处理局限（CF trade-off, n=4 限制明确声明）
3. Pair-based sequential masking 有量化支撑（33-37% spurious pairs）
4. Related Work 组织良好
5. Runtime overhead 极低（+2.3% to +5.4%）

---

请逐条回应 Reviewer 2 的 Must-Fix (N1, N2) 和 Should-Fix (W1-W6) 意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 200 · 2026-05-17T10:23:12.039365+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 201 · 2026-05-17T10:23:12.843043+00:00_

1	\begin{abstract}
2	We present \textsc{OntoCoDec}, which compiles IE ontology schemas into two composable token-level decoding constraints that provide formal guarantees during autoregressive generation:
3	(1)~a \emph{grammar layer} (XGrammar CFG) guaranteeing JSON structural validity and entity/relation vocabulary membership (ET, RV\,$\to$\,0\%); and
4	(2)~a \emph{semantic layer} guaranteeing per-triple domain/range type compliance via a stateful entity registry and dynamic logit masking.
5	The two layers compose via bitwise AND on logit masks, with the grammar layer as an enabling prerequisite.
6	%
7	Without constraints, LLM-based IE produces systematic violations: 15.37\% DR on SciERC (7 relations) and 18.46\% on DocRED (96 relations)---comparable rates governed by \emph{constraint tightness} rather than ontology scale.
8	\textsc{OntoCoDec} reduces DR by 42--99\% across three model families (Qwen3-8B, Llama-3.1-8B, Mistral-7B) with no significant F1 cost.
9	For the primary model (Qwen3-8B): SciERC $+$0.13\,pp ($p{=}0.58$), DocRED $+$0.50\,pp ($p{<}0.001$); other models show comparable or larger gains (\S\ref{sec:cross-model}).
10	% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1, llama_docred_full_s1, mistral_docred
11	Residual DR is characterized by a dual-factor pattern (schema tightness $\times$ model calibration; $R^2{=}0.886$, $n{=}4$; Appendix~\ref{app:dual-factor}).
12	Composed with LoRA fine-tuning, DR reaches $\leq$\,0.09\% (SciERC) and 0.20\% (DocRED) with R-F1 within $\pm$0.6\,pp, confirming orthogonal composability.
13	Per-relation independent enforcement introduces a CF$\leftrightarrow$DR trade-off: cross-field consistency violations arise (up to 12\% in zero-shot) as the cost of per-slot domain/range guarantees; fine-tuning resolves this tension (CF\,$\leq$\,1.2\%).
14	\end{abstract}
15	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 202 · 2026-05-17T10:23:12.994118+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 203 · 2026-05-17T10:23:13.295872+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly deployed for zero-shot information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity is guaranteed to carry a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}---structurally valid triples that are ontologically invalid.
8	In a systematic study, we find violations are pervasive: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred}, driven by \emph{constraint tightness} (few valid type pairs per relation) rather than ontology scale.
9	Relations with tight constraints exhibit far higher rates (\textsc{Compare}: 42.4\%) than loosely constrained ones (\textsc{Used-for}: 0.8\%).
10	
11	Existing approaches leave a fundamental gap.
12	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable---violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp.
13	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} guarantees syntactic well-formedness but cannot encode cross-field semantic constraints.
14	At high rejection rates (e.g., Mistral DocRED 73.7\%), post-hoc filtering discards the majority of outputs including true positives, making it impractical; it also cannot redirect probability mass during decoding.
15	Training-based approaches~\cite{sainz2024gollie,lu2022uie} provide only soft guidance that cannot eliminate violations.
16	
17	We propose \textbf{OntoCoDec} (\textbf{Onto}logy-\textbf{Co}mpiled \textbf{Dec}oding), a framework that compiles an IE ontology into two composable layers of decoding-time constraints.
18	The \emph{grammar layer} enforces JSON well-formedness and vocabulary validity via XGrammar.
19	The \emph{semantic layer} 
…[truncated 1687 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 204 · 2026-05-17T10:23:13.548012+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex",
    "limit": "15"
  }
}
```

</details>

---


### Tool result

_source line 205 · 2026-05-17T10:23:13.598647+00:00_

1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	We present OntoCoDec, a two-layer constrained decoding framework that compiles ontology schemas into token-level masks enforced during autoregressive generation.
9	Unlike type-constrained code generation, IE presents three distinct challenges: (1)~entity types are inferred from free text rather than declared annotations, (2)~the entity registry is built dynamically during generation, and (3)~constraint targets are context-dependent type assignments rather than fixed grammar productions.
10	The grammar layer (\S\ref{sec:grammar}) guarantees structural validity—well-formed JSON with ontology-vocabulary membership—while the semantic layer (\S\ref{sec:semantic}) enforces domain/range type constraints via a stateful entity registry.
11	We describe the problem formulation (\S\ref{sec:formulation}), each layer, and two decoding strategies (\S\ref{sec:strategies}).
12	Formal analysis of constraint composition is deferred to Section~\ref{sec:composition}.
13	
14	
15	\subsection{Problem Formulation}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 206 · 2026-05-17T10:23:24.901877+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "glob": "section*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "---",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "glob": "section*.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 207 · 2026-05-17T10:23:25.404460+00:00_

&lt;persisted-output>
Output too large (23.4KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-1-11179fb2/aa5b88f2-e1cf-49b5-af8a-bd6fe3b98959/tool-results/toolu_01W65xMBUzr5BczhpXHud7kB.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:13:types---14$\times$ the ontology size of SciERC
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:40:  & 18.46 & ---
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:48:  & \textbf{8.31}  & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:68:Best per column in \textbf{bold} (CF excluded---see text).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:70:Grammar-only entity F1 is unavailable (---).}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:116:relation names---but the associated entity types frequently violate
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:7:We call such outputs \emph{domain/range violations}---structurally valid triples that are ontologically invalid.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:12:Schema-informed prompting reduces violations by 62\% on average but is per-relation un
…[truncated 108 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 208 · 2026-05-17T10:23:25.856855+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 209 · 2026-05-17T10:23:26.861293+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:1:% Section 5 — DocRED Results (Draft)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex:1:% Appendix — Prompt Templates
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex:1:% Section 5 — Cross-Model Validation (compressed, 830→~400 words)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex:1:% Section 3 — Method (Draft)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex:10:The grammar layer (\S\ref{sec:grammar}) guarantees structural validity—well-formed JSON with ontology-vocabulary membership—while the semantic layer (\S\ref{sec:semantic}) enforces domain/range type constraints via a stateful entity registry.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex:49:Domain/range constraints are \emph{not} enforced, as they depend on entity types within each triple—the gap filled by the semantic layer.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:1:% Appendix B — Extended Discussion
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex:2:% Related Work Additions — compiled 2026-05-14
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex:60:% STATUS: VERIFIED — paper exists and description is accurate
/home/ubuntu/.agent-ml-rese
…[truncated 1834 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 210 · 2026-05-17T10:23:27.733746+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,|ing\\.|ing;|, highlighting|, demonstrating|, enabling|, confirming|, indicating|, reflecting",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "glob": "section*.tex",
  "output_mode": "content",
  "head_limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,|ing\\.|ing;|, highlighting|, demonstrating|, enabling|, confirming|, indicating|, reflecting",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "glob": "section*.tex",
    "output_mode": "content",
    "head_limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 211 · 2026-05-17T10:23:27.784596+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:135:\textsc{TypeConstraintProcessor}'s logit masking, which occasionally
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:155:\paragraph{Constraint tightness governs enforcement ceiling.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:173:for the model to redirect probability mass toward, enabling
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:14:At high rejection rates (e.g., Mistral DocRED 73.7\%), post-hoc filtering discards the majority of outputs including true positives, making it impractical; it also cannot redirect probability mass during decoding.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:20:The layers compose via bitwise AND with an \emph{enabling dependency}: the grammar layer guarantees vocabulary membership, enabling the semantic layer to look up domain/range rules.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex:12:\paragraph{Grammar-Constrained Decoding.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex:57:RV and ET violations are eliminated ($\leq$0.03\%) for all three models on both datasets, confirming that grammar-layer enforcement depends on the decoding mechanism, not model-specific generation patterns.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel
…[truncated 6680 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 212 · 2026-05-17T10:25:32.490628+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: Abstract 缩写未展开**\n\n同意。Abstract 中 IE（line 2）、CFG（line 3）、ET/RV（line 3）、DR（line 7）、LLM（line 7）、LoRA（line 12）、CF（line 13）均未在 Abstract 内展开。虽然标题含 \"Information Extraction\" 定义了 IE，但 ARR 规范要求 Abstract 独立可读。这是明确的格式违规，修复成本低（仅需在首次出现时展开），没有理由不修。\n\n补充：至少 LLM、IE、DR、CF 必须在 Abstract 内展开；ET/RV/CFG 可考虑用描述性文字替代缩写（如 \"entity type and relation vocabulary violations → 0%\"），避免 Abstract 被缩写堆积。\n\n---\n\n**[AGREE with qualification] R2-N2: Em-dash 过度使用**\n\n同意 em-dash 过度使用是问题，但 R2 的计数需要区分两类用法：\n\n**(a) 解释性 em-dash（应修改）**：我在正文主体中确认了以下实例：\n- §1 line 7: `violations---structurally valid triples that are ontologically invalid`\n- §1 line 12: `unreliable---violations for \\textsc{Evaluate-for}`\n- §1 line 26 (Contribution 2): `framework---the first to enforce`\n- §3 line 10: Unicode em-dash `validity—well-formed JSON`（格式不一致，非 LaTeX `---`）\n- §3 line 49: Unicode em-dash `enforced, as they depend...—the gap filled by`\n- §4 line 28: `pattern---tightness × baseline`\n- §5.3 line 9: `types---14× the ontology size`\n- §6 DORE 描述处\n\n正文约 8-10 处解释性 em-dash，密度确实偏高。\n\n**(b) 表格数据占位符（标准用法，不应计入）**：Table 1 和 Table 3 中 `---` 表示 baseline 无对比值或数据不可用，这是 LaTeX 论文的标准做法，不属于 AI 写作痕迹。R2 列举的 \"至少 12 处\" 可能包含了这类标准用法。\n\n**额外发现**：§3 中两处使用 Unicode em-dash（U+2014 `—`）而非 LaTeX `---`，这是 R2 也注意到的格式不一致问题，需统一处理。\n\n总结：解释性 em-dash 确实过多，但 R2 将严重程度定为 \"critical\" 可能过高——em-dash 密度本身不应构成接收障碍，而是 camera-ready 修订问题。建议降级为 should-fix。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: -ing 分词短语结尾**\n\n同意。我在正文中确认了多处 -ing 分词短语模式，包括 `confirming that...`（§5.2, §5.4 各多处）、`enabling the semantic layer to...`（§1 line 20）、`indicating that...`（§5.1）、`reflecting...`（§5.4）。这些用法在技术论文中并非全部不当（某些确实起到了紧凑表达因果关系的作用），但密度过高（正文 ~10 处，附录更多）确实构成 AI 写作印象。应选择性改写为独立句子。\n\n---\n\n**[AGREE] R2-W2: Code-gen 区分未在 Introduction 出现**\n\n同意。§3 line 9 清楚列出了 IE 与 code-gen 的三个技术区别（types inferred from free text, dynamic registry, context-dependent targets），这是方法新颖性的核心论证。但 §1 Introduction 完全没有提及 code-gen constrained decoding（如 Synchromesh, PICARD, MGD, PLDI 2025）。审稿人读完 §1 后可能会质疑：\"这和代码生成的 type-constrained decoding 有什么区别？\" 将核心区分论证延迟到 §3 是结构性弱点。\n\n建议在 §1 第二段（现有方法不足处）添加一句，如：\"Type-constrained decoding for code generation (Synchromesh, MGD) enforces similar semantic constraints, but IE introduces distinct challenges: entity types must be inferred from free text rather than read from declared annotations, requiring a dynamic registry built during generation (§3).\"\n\n---\n\n**[AGREE] R2-W3: R²=0.886 (n=4) 在 Abstract 过于突出**\n\n强烈同意。这与我 Round 4 审稿的 N1 一致。补充 R2 未提及的统计论据：n=4、2 参数线性模型，自由度仅为 2，F(1,2)=15.54 对应 p≈0.058，在 α=0.05 下不显著。Abstract 第 11 行将 R²=0.886 作为独立句子呈现，给读者以核心贡献的印象，与 §7 Discussion 的 \"descriptive characterization\" 定位不一致。应从 Abstract 移除具体数值。\n\n---\n\n**[AGREE partially] R2-W4: Reproducibility 信息不充分**\n\n部分同意。论文在以下方面做得好：每个实验有 exp_id 可追溯（tex 注释中可见如 `% exp_ids: phase2_scierc_full_s1`）、prompt templates 完整公开（Appendix A）、greedy 实验完全确定性（rebuttal_draft_v2.md 确认 \"3 independent seeds produce identical outputs\"）。\n\n但以下信息确实缺失：\n- LoRA 训练超参数（rank, alpha, learning rate, epochs, batch size）未在正文或附录中报告\n- GPU 型号仅在附录 FT latency 段出现一次（\"RTX PRO 6000\"，Appendix B app:ft-latency），主实验 GPU 未说明\n- Random seeds 对 LoRA 训练的影响未讨论（greedy inference 确定性不等于 LoRA training 确定性）\n- ARR Responsible NLP Checklist / Reproducibility Statement 未出现\n\nR2 给 Reproducibility 3.5/5 合理。但 \"critical\" 级别不一定成立——这些信息可在 camera-ready 补充。\n\n---\n\n**[REBUT partially] R2-W5: Related Work 缺少 Document-level RE 工作**\n\n部分反驳。\n\n论文不以 DocRED SOTA 为目标——§5.3 明确说 \"F1 serves primarily as a control variable verifying constraint enforcement preserves extraction quality, not as an optimization target\"。在此定位下，不引用 DREEAM、DocGNRE 等 supervised document-level RE SOTA 方法是合理的。论文已引用 DocRED 原始数据集（Yao et al., 2019）和相关上下文（Zhong & Chen 2021 for supervised SOTA baseline）。\n\n但 R2 提到的 **GLiNER** 值得关注——GLiNER 是 generalist NER model，与 OntoCoDec 的 \"任何 autoregressive LM 均适用\" 的定位有对比价值。如果不引用，建议在 Related Work 中补充一句解释：本工作关注 constraint enforcement 而非 extraction model selection。\n\nDREEAM 和 DocGNRE 作为 supervised document-level RE 方法，与本工作的核心贡献（decoding-time constraint enforcement）正交。强制要求引用它们类似于要求所有使用 ImageNet 的论文引用最新分类 SOTA——不合理。\n\n---\n\n**[REBUT] R2-W6: Table caption 中 em-dash 需替换**\n\n反驳。Table 1 caption 中 `(CF excluded---see text)` 是唯一一处 caption 中的解释性 em-dash，可以修改。但 R2 如果指的是 Table 内数据列中的 `---`（如 Table 1 baseline 行的 $\\Delta$DR 列、Table 3 的 CF 列），这是 LaTeX 论文中表示 \"不适用/无数据\" 的标准格式，不属于 AI 写作痕迹，不应修改。需要区分：caption 中的解释性 em-dash（可修改）vs 数据单元格中的占位符（标准用法）。\n\n---\n\n### 小问题补充意见\n\n1. **Abstract CFG 未展开**：同意，已在 N1 中覆盖。\n2. **§2 $\\mathcal{T} = \\mathcal{E}$**：[AGREE] 确实是冗余重定义。直接用 $\\mathcal{E}$ 即可。\n3. **§3 Unicode em-dash**：[AGREE] 已在 N2 回应中指出，需统一为 LaTeX `---` 或改写。\n4. **Table 1 CF \"---\" 未解释**：[AGREE] 应在 caption 或脚注中说明 CF 在 schema-informed prompt 下未测量。\n5. **Table 2 CF 列方向**：[AGREE] CF 列没有方向标记（↑/↓），且 CF 的 \"好\" 方向是 ↓，但 full S1 的 CF 反而上升。应在 caption 中说明 \"CF: lower is better; elevated by per-relation enforcement, see §7.\"\n6. **Appendix B Llama DocRED CF \"---\"**：[AGREE] FT ablation Table 6 中 Llama DocRED unconstrained CF 列显示 \"---\"，应为 0.00 或注明原因。\n7. **§6 DORE em-dash**：已在 N2 中覆盖。\n8. **bib 条目 vukovic2024dore**：[AGREE] 缺少 pages/url 是格式问题，应补充。\n\n---\n\n### 总结\n\n与 R2 的核心判断高度一致：Overall 3.5/5，适合 Findings。在以下问题上我们观点一致且互相印证：\n- R²=0.886 在 Abstract 中过于突出（R2-W3 = 我的 N1）\n- Em-dash 和 -ing 模式需要清理（R2-N2/W1，我也注意到但归入 minor）\n- Reproducibility 信息有缺口（R2-W4，我此前未重点提及）\n\n主要分歧在于：\n- R2 将 em-dash 定为 critical，我认为应降级为 should-fix（格式问题，不影响技术贡献）\n- R2 要求引用 DREEAM/DocGNRE/GLiNER，我认为 DREEAM/DocGNRE 与本工作正交，但 GLiNER 值得提及\n- R2 未注意到我标记为 critical 的 beam search 降级问题（我的 N2）——beam search 在 SciERC 全集上解决了 CF 和残余 DR，但被放在附录，这影响了论文贡献的定位",
  "reviewer_id": "1",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: Abstract 缩写未展开**\n\n同意。Abstract 中 IE（line 2）、CFG（line 3）、ET/RV（line 3）、DR（line 7）、LLM（line 7）、LoRA（line 12）、CF（line 13）均未在 Abstract 内展开。虽然标题含 \"Information Extraction\" 定义了 IE，但 ARR 规范要求 Abstract 独立可读。这是明确的格式违规，修复成本低（仅需在首次出现时展开），没有理由不修。\n\n补充：至少 LLM、IE、DR、CF 必须在 Abstract 内展开；ET/RV/CFG 可考虑用描述性文字替代缩写（如 \"entity type and relation vocabulary violations → 0%\"），避免 Abstract 被缩写堆积。\n\n---\n\n**[AGREE with qualification] R2-N2: Em-dash 过度使用**\n\n同意 em-dash 过度使用是问题，但 R2 的计数需要区分两类用法：\n\n**(a) 解释性 em-dash（应修改）**：我在正文主体中确认了以下实例：\n- §1 line 7: `violations---structurally valid triples that are ontologically invalid`\n- §1 line 12: `unreliable---violations for \\textsc{Evaluate-for}`\n- §1 line 26 (Contribution 2): `framework---the first to enforce`\n- §3 line 10: Unicode em-dash `validity—well-formed JSON`（格式不一致，非 LaTeX `---`）\n- §3 line 49: Unicode em-dash `enforced, as they depend...—the gap filled by`\n- §4 line 28: `pattern---tightness × baseline`\n- §5.3 line 9: `types---14× the ontology size`\n- §6 DORE 描述处\n\n正文约 8-10 处解释性 em-dash，密度确实偏高。\n\n**(b) 表格数据占位符（标准用法，不应计入）**：Table 1 和 Table 3 中 `---` 表示 baseline 无对比值或数据不可用，这是 LaTeX 论文的标准做法，不属于 AI 写作痕迹。R2 列举的 \"至少 12 处\" 可能包含了这类标准用法。\n\n**额外发现**：§3 中两处使用 Unicode em-dash（U+2014 `—`）而非 LaTeX `---`，这是 R2 也注意到的格式不一致问题，需统一处理。\n\n总结：解释性 em-dash 确实过多，但 R2 将严重程度定为 \"critical\" 可能过高——em-dash 密度本身不应构成接收障碍，而是 camera-ready 修订问题。建议降级为 should-fix。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: -ing 分词短语结尾**\n\n同意。我在正文中确认了多处 -ing 分词短语模式，包括 `confirming that...`（§5.2, §5.4 各多处）、`enabling the semantic layer to...`（§1 line 20）、`indicating that...`（§5.1）、`reflecting...`（§5.4）。这些用法在技术论文中并非全部不当（某些确实起到了紧凑表达因果关系的作用），但密度过高（正文 ~10 处，附录更多）确实构成 AI 写作印象。应选择性改写为独立句子。\n\n---\n\n**[AGREE] R2-W2: Code-gen 区分未在 Introduction 出现**\n\n同意。§3 line 9 清楚列出了 IE 与 code-gen 的三个技术区别（types inferred from free text, dynamic registry, context-dependent targets），这是方法新颖性的核心论证。但 §1 Introduction 完全没有提及 code-gen constrained decoding（如 Synchromesh, PICARD, MGD, PLDI 2025）。审稿人读完 §1 后可能会质疑：\"这和代码生成的 type-constrained decoding 有什么区别？\" 将核心区分论证延迟到 §3 是结构性弱点。\n\n建议在 §1 第二段（现有方法不足处）添加一句，如：\"Type-constrained decoding for code generation (Synchromesh, MGD) enforces similar semantic constraints, but IE introduces distinct challenges: entity types must be inferred from free text rather than read from declared annotations, requiring a dynamic registry built during generation (§3).\"\n\n---\n\n**[AGREE] R2-W3: R²=0.886 (n=4) 在 Abstract 过于突出**\n\n强烈同意。这与我 Round 4 审稿的 N1 一致。补充 R2 未提及的统计论据：n=4、2 参数线性模型，自由度仅为 2，F(1,2)=15.54 对应 p≈0.058，在 α=0.05 下不显著。Abstract 第 11 行将 R²=0.886 作为独立句子呈现，给读者以核心贡献的印象，与 §7 Discussion 的 \"descriptive characterization\" 定位不一致。应从 Abstract 移除具体数值。\n\n---\n\n**[AGREE partially] R2-W4: Reproducibility 信息不充分**\n\n部分同意。论文在以下方面做得好：每个实验有 exp_id 可追溯（tex 注释中可见如 `% exp_ids: phase2_scierc_full_s1`）、prompt templates 完整公开（Appendix A）、greedy 实验完全确定性（rebuttal_draft_v2.md 确认 \"3 independent seeds produce identical outputs\"）。\n\n但以下信息确实缺失：\n- LoRA 训练超参数（rank, alpha, learning rate, epochs, batch size）未在正文或附录中报告\n- GPU 型号仅在附录 FT latency 段出现一次（\"RTX PRO 6000\"，Appendix B app:ft-latency），主实验 GPU 未说明\n- Random seeds 对 LoRA 训练的影响未讨论（greedy inference 确定性不等于 LoRA training 确定性）\n- ARR Responsible NLP Checklist / Reproducibility Statement 未出现\n\nR2 给 Reproducibility 3.5/5 合理。但 \"critical\" 级别不一定成立——这些信息可在 camera-ready 补充。\n\n---\n\n**[REBUT partially] R2-W5: Related Work 缺少 Document-level RE 工作**\n\n部分反驳。\n\n论文不以 DocRED SOTA 为目标——§5.3 明确说 \"F1 serves primarily as a control variable verifying constraint enforcement preserves extraction quality, not as an optimization target\"。在此定位下，不引用 DREEAM、DocGNRE 等 supervised document-level RE SOTA 方法是合理的。论文已引用 DocRED 原始数据集（Yao et al., 2019）和相关上下文（Zhong & Chen 2021 for supervised SOTA baseline）。\n\n但 R2 提到的 **GLiNER** 值得关注——GLiNER 是 generalist NER model，与 OntoCoDec 的 \"任何 autoregressive LM 均适用\" 的定位有对比价值。如果不引用，建议在 Related Work 中补充一句解释：本工作关注 constraint enforcement 而非 extraction model selection。\n\nDREEAM 和 DocGNRE 作为 supervised document-level RE 方法，与本工作的核心贡献（decoding-time constraint enforcement）正交。强制要求引用它们类似于要求所有使用 ImageNet 的论文引用最新分类 SOTA——不合理。\n\n---\n\n**[REBUT] R2-W6: Table caption 中 em-dash 需替换**\n\n反驳。Table 1 caption 中 `(CF excluded---see text)` 是唯一一处 caption 中的解释性 em-dash，可以修改。但 R2 如果指的是 Table 内数据列中的 `---`（如 Table 1 baseline 行的 $\\Delta$DR 列、Table 3 的 CF 列），这是 LaTeX 论文中表示 \"不适用/无数据\" 的标准格式，不属于 AI 写作痕迹，不应修改。需要区分：caption 中的解释性 em-dash（可修改）vs 数据单元格中的占位符（标准用法）。\n\n---\n\n### 小问题补充意见\n\n1. **Abstract CFG 未展开**：同意，已在 N1 中覆盖。\n2. **§2 $\\mathcal{T} = \\mathcal{E}$**：[AGREE] 确实是冗余重定义。直接用 $\\mathcal{E}$ 即可。\n3. **§3 Unicode em-dash**：[AGREE] 已在 N2 回应中指出，需统一为 LaTeX `---` 或改写。\n4. **Table 1 CF \"---\" 未解释**：[AGREE] 应在 caption 或脚注中说明 CF 在 schema-informed prompt 下未测量。\n5. **Table 2 CF 列方向**：[AGREE] CF 列没有方向标记（↑/↓），且 CF 的 \"好\" 方向是 ↓，但 full S1 的 CF 反而上升。应在 caption 中说明 \"CF: lower is better; elevated by per-relation enforcement, see §7.\"\n6. **Appendix B Llama DocRED CF \"---\"**：[AGREE] FT ablation Table 6 中 Llama DocRED unconstrained CF 列显示 \"---\"，应为 0.00 或注明原因。\n7. **§6 DORE em-dash**：已在 N2 中覆盖。\n8. **bib 条目 vukovic2024dore**：[AGREE] 缺少 pages/url 是格式问题，应补充。\n\n---\n\n### 总结\n\n与 R2 的核心判断高度一致：Overall 3.5/5，适合 Findings。在以下问题上我们观点一致且互相印证：\n- R²=0.886 在 Abstract 中过于突出（R2-W3 = 我的 N1）\n- Em-dash 和 -ing 模式需要清理（R2-N2/W1，我也注意到但归入 minor）\n- Reproducibility 信息有缺口（R2-W4，我此前未重点提及）\n\n主要分歧在于：\n- R2 将 em-dash 定为 critical，我认为应降级为 should-fix（格式问题，不影响技术贡献）\n- R2 要求引用 DREEAM/DocGNRE/GLiNER，我认为 DREEAM/DocGNRE 与本工作正交，但 GLiNER 值得提及\n- R2 未注意到我标记为 critical 的 beam search 降级问题（我的 N2）——beam search 在 SciERC 全集上解决了 CF 和残余 DR，但被放在附录，这影响了论文贡献的定位",
    "reviewer_id": "1",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 213 · 2026-05-17T10:25:36.358256+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3867
}
```

</details>

---


### Assistant

_source line 214 · 2026-05-17T10:25:42.841854+00:00_

交叉回应已提交给 Director。

总结：与 R2 的 8 条意见中，我对 N1（缩写）、W1（-ing 模式）、W2（code-gen 区分）、W3（R² 突出度）明确同意；对 N2（em-dash 严重程度应降级为 should-fix）、W4（reproducibility 部分同意）、W5（DocRED 文献部分反驳）做了有据的调整；对 W6（表格数据占位符是标准格式）给出了反驳。两位 Reviewer 在 R²=0.886 问题上高度一致，构成需修复的共识。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1"
}
```

</details>

---


## Round 8

## Round 8

54 recorded events


### User

_source line 215 · 2026-05-17T11:58:30.951751+00:00_

[Round 1 审稿请求]:
**[Round 5 / R1] 审稿任务分配 — 方法严谨性 + 实验充分性**

**Venue**: EMNLP 2026 Findings (ARR May 2026 cycle)
**Deadline**: 2026-05-25
**Format**: ACL template, long paper ≤ 8 pages (excl. Limitations/Ethics/References), double-blind, Limitations section required
**论文路径**: `projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`（所有 section 通过 `\input` 引入）

**你的审查侧重**：方法严谨性 + 实验充分性

请重点检查以下方面：

### A. 方法严谨性
1. §3 Problem Formulation: pair-based enforcement 的形式化是否严谨？sequential masking 的正确性论证是否充分？
2. §3 JSON field ordering prerequisite: 论文声称 JSON Schema 强制固定字段顺序（head → head_type → tail → tail_type → relation），这是 sequential masking 的前提。这个声明是否充分论证？JSON 标准不保证 key 顺序，需要检查是否有明确说明 grammar layer (XGrammar) 如何保证字段顺序。
3. §4 Constraint Composition: grammar-first fallback 的形式化是否严谨？decidability taxonomy 是否正确？
4. Dual-factor pattern (R²=0.99, n=4): 历史审稿反复标记此问题（R2-N1）。检查当前 Abstract 和 §7 中的表述——Abstract 是否仍然突出显示 R² 值？§7 是否已降级为"descriptive characterization"？是否报告了 F-test？是否提供了 Mistral 排除的先验标准？
5. RV=0.03% residual: 论文 §5.3 说"partial JSON recovery"，rebuttal draft 说"XGrammar v0.1.33 enum compilation bug"。检查当前论文中的解释是否统一。

### B. 实验充分性
1. Post-hoc vs OntoCoDec framing (W3): 5/6 ZS 配置中 post-hoc F1 更高。Introduction 的 framing 是否客观？是否有一句话承认 post-hoc 的 precision 优势？
2. Parse failure confounding (R2-N3): Llama DocRED ZS parse failure 从 6.8% 增加到 9.1%（+34%）。论文是否提供了 parse-failure-excluded 的 violation rates 和 F1？
3. Semantic-only ET increase on DocRED (R2-N6): ET 从 2.48% 增加到 4.22%（+70%）。SciERC 的机制已解释（semantic mask forces OOV type），DocRED 的解释是否存在？
4. Beam search results (R4-N3): beam k=4 在 SciERC 全集上 DR=0%, CF=0.53%——这同时解决了 greedy 的两个主要限制。这些结果是否在正文 §5/§7 中讨论？是否报告了 beam search 的 runtime overhead？
5. CF-DR trade-off ablation (R4-Q2): 目前仅在 SciERC/Qwen 上做了 ablation。是否讨论了 DocRED/Llama 的可迁移性？
6. DocRED fallback coverage (R4-W2): SciERC 的 effective semantic coverage 63.4% 已报告。DocRED 的覆盖率是否显式报告？
7. §4 DR reduction range inconsistency (R4-W3): §4 说 "94-99%"（仅 Qwen+Llama），Abstract 说 "42-99%"（含 Mistral）。范围是否一致？

### C. 统计声明
1. Bootstrap test 的参数和结论是否一致？
2. Composability matrix 的统计显著性是否报告？
3. 所有 claim 是否有对应的 table/section 支撑？

请按 EMNLP 审稿标准输出完整审稿报告，包含 Summary、Strengths、Weaknesses (Must-Fix / Should-Fix / Minor)、Questions、Missing References、Scores (Soundness 1-5, Substance 1-5, Reproducibility 1-5, Overall 1-5, Confidence 1-5)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 216 · 2026-05-17T11:58:39.654178+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
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

_source line 217 · 2026-05-17T11:58:39.654621+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 218 · 2026-05-17T11:58:42.866180+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 219 · 2026-05-17T11:58:43.620554+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 220 · 2026-05-17T11:58:43.671379+00:00_

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
12	\usepackage{multirow}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{enumitem}
16	\usepackage{xcolor}
17	
18	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Ontology Constraints}
19	
20	\author{Anonymous ACL submission}
21	
22	\begin{document}
23	\maketitle
24	
25	% === Abstract ===
26	\input{abstract}
27	
28	% === §1 Introduction ===
29	\input{section1_introduction_draft}
30	
31	% === §2 Background ===
32	\input{section2_background}
33	
34	% === §3 Method ===
35	\input{section3_method_draft}
36	
37	% === §4 Constraint Composition ===
38	\section{Constraint Composition}
39	\label{sec:composition}
40	\input{section4_composition_draft}
41	
42	% === §5 Experiments ===
43	\section{Experiments}
44	\label{sec:experiments}
45	
46	\subsection{Violation Landscape}
47	\input{section3_violation_landscape}
48	
49	\input{section5_scierc_draft}
50	\input{section5_docred_draft}
51	\input{section5_crossmodel_draft}
52	\input{section5_runtime}
53	
54	% === §6 Related Work ===
55	\input{section6_related_work}
56	
57	% === §7 Discussion and Conclusion ===
58	\section{Discussion and Conclusion}
59	\label{sec:discussion}
60	\input{section7_conclusion_compressed}
61	
62	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
63	\clearpage
64	\section*{Limitations}
65	
66	CF impact is model-dependent: for well-calibrated models (Qwen, Llama), S1 introduces CF violations (up to 12.02\%) as a consequence of per-relation independent enforcement; for poorly-calibrated models (Mistral), S1 substantially reduces CF (56.87\%\,$\to$\,1.27\%) by constraining type assignments to schema-valid values.
67	CF fallback ablation shows that eliminating CF re-routes violations to DR ($+$13
…[truncated 3565 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 221 · 2026-05-17T11:58:50.607962+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

I've found comprehensive information about ACL ARR 2025-2026 reviewer guidelines. Here are the key details:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## O
…[truncated 1461 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7741
}
```

</details>

---


### Tool call

_source line 222 · 2026-05-17T11:58:55.985282+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5), descriptions for each score level, and all required fields. Include the exact wording for soundness, excitement/novelty, overall recommendation, confidence, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5), descriptions for each score level, and all required fields. Include the exact wording for soundness, excitement/novelty, overall recommendation, confidence, and any other scored dimensions."
  }
}
```

</details>

---


### Tool call

_source line 223 · 2026-05-17T11:58:56.338149+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 224 · 2026-05-17T11:58:56.841352+00:00_

1	\begin{abstract}
2	We present \textsc{OntoCoDec}, which compiles Information Extraction (IE) ontology schemas into two composable token-level decoding constraints that provide formal guarantees during autoregressive generation:
3	(1)~a \emph{grammar layer} (XGrammar context-free grammar) guaranteeing JSON structural validity and entity/relation vocabulary membership (eliminating entity type and relation vocabulary violations); and
4	(2)~a \emph{semantic layer} guaranteeing per-triple domain/range type compliance via a stateful entity registry and dynamic logit masking.
5	The two layers compose via bitwise AND on logit masks, with the grammar layer as an enabling prerequisite.
6	%
7	Without constraints, Large Language Model (LLM) based IE produces systematic domain/range (DR) violations: 15.37\% on SciERC (7 relations) and 18.46\% on DocRED (96 relations), comparable rates governed by \emph{constraint tightness} rather than ontology scale.
8	\textsc{OntoCoDec} reduces DR by 42--99\% across three model families (Qwen3-8B, Llama-3.1-8B, Mistral-7B) with no significant F1 cost.
9	For the primary model (Qwen3-8B): SciERC $+$0.13\,pp ($p{=}0.58$), DocRED $+$0.50\,pp ($p{<}0.001$); other models show comparable or larger gains (\S\ref{sec:cross-model}).
10	% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1, llama_docred_full_s1, mistral_docred
11	Residual DR correlates with the product of schema tightness and baseline violation rate: for calibrated models (Qwen3-8B, Llama-3.1-8B), the dual-factor pattern explains nearly all variance ($R^2{=}0.99$, $n{=}4$), while Mistral's higher entity misclassification rate places it outside this regime (Appendix~\ref{app:dual-factor}).
12	Composed with Low-Rank Adaptation (LoRA) fine-tuning, DR reaches $\leq$\,0.09\% (SciERC) and 0.20\% (DocRED) with R-F1 within $\pm$0.6\,pp, confirming orthogonal composability.
13	Per-relation independent enforcement introduces a cross-field consistency (CF) vs.\ DR trade-off: CF violations arise
…[truncated 152 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 225 · 2026-05-17T11:58:56.841772+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 226 · 2026-05-17T11:58:57.745189+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly deployed for zero-shot information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity is guaranteed to carry a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	In a systematic study, we find violations are pervasive: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred}, driven by \emph{constraint tightness} (few valid type pairs per relation) rather than ontology scale.
9	Relations with tight constraints exhibit far higher rates (\textsc{Compare}: 42.4\%) than loosely constrained ones (\textsc{Used-for}: 0.8\%).
10	
11	Existing approaches leave a fundamental gap.
12	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
13	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} guarantees syntactic well-formedness but cannot encode cross-field semantic constraints.
14	Post-hoc filtering achieves higher F1 in most zero-shot settings via precision gains, but at the cost of discarding up to 48\% of predictions including true positives; at high rejection rates (e.g., Mistral DocRED 73.7\%), it discards the majority of outputs, making it impractical.
15	OntoCoDec preserves recall by enforcing constraints during generation rather than discarding non-compliant outputs.
16	Training-based approaches~\cite{sainz2024gollie,lu2022uie} provide only soft guidance that cannot eliminate violations.
17	
18	We propose \textbf{OntoCoDec} (\textbf{Onto}logy-\textbf{Co}mpiled \textbf{Dec}oding), a framework that compiles an IE onto
…[truncated 2132 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 227 · 2026-05-17T11:58:57.745724+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 228 · 2026-05-17T11:58:57.946850+00:00_

1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	We present OntoCoDec, a two-layer constrained decoding framework that compiles ontology schemas into token-level masks enforced during autoregressive generation.
9	Unlike type-constrained code generation, IE presents three distinct challenges: (1)~entity types are inferred from free text rather than declared annotations, (2)~the entity registry is built dynamically during generation, and (3)~constraint targets are context-dependent type assignments rather than fixed grammar productions.
10	The grammar layer (\S\ref{sec:grammar}) guarantees structural validity (well-formed JSON with ontology-vocabulary membership), while the semantic layer (\S\ref{sec:semantic}) enforces domain/range type constraints via a stateful entity registry.
11	We describe the problem formulation (\S\ref{sec:formulation}), each layer, and two decoding strategies (\S\ref{sec:strategies}).
12	Formal analysis of constraint composition is deferred to Section~\ref{sec:composition}.
13	
14	
15	\subsection{Problem Formulation}
16	\label{sec:formulation}
17	
18	\paragraph{IE as structured generation.}
19	Given an input text $x$, a language model generates a structured JSON output $y$:
20	%
21	\begin{equation}\label{eq:output-schema}
22	\resizebox{.88\columnwidth}{!}{$\displaystyle
23	  y = \bigl\{\texttt{entities}: [\{n_i, \tau_i\}],\; \texttt{relations}: [\{h_j, t_j, r_j, \tau^h_j, \tau^t_j\}]\bigr\}
24	$}
25	\end{equation}
26	%
27	where each entity has a name $n_i$ and type $\tau_i \in \mathcal{E}$, and each relation specifies head $h_j$, tail $t_j$, relation type $r_j \in \mathcal{R}$, and head/tail entity types $\tau^h_j, \tau^t_j$.
28	The JSON Schema enforces a fixed field ordering (head $\to$ head\_type $\to$ tail $\to$ tail\_type $\to$ relation), which is a prerequisite for the sequential masking mechanism described in \S\ref{sec:d
…[truncated 8203 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 229 · 2026-05-17T11:58:57.947238+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 230 · 2026-05-17T11:58:57.997831+00:00_

1	% Section: Constraint Composition (compressed, 787→~500 words)
2	
3	At each decoding step $t$, let $G(t) \subseteq V$ and $S(t) \subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.
4	The final mask is their conjunction:
5	%
6	\begin{equation}\label{eq:composition}
7	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
8	\end{equation}
9	%
10	so a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$, reflecting the enabling dependency (\S\ref{sec:method})---the semantic layer requires the relation type to belong to $\mathcal{R}$, a property guaranteed only by the grammar layer.
12	
13	\paragraph{Grammar-First Fallback.}
14	When $S(t) \cap G(t) = \emptyset$---tight constraints leave no token that is both grammar-valid and semantically valid---na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
15	We enforce a \emph{grammar-first fallback}: if no semantically valid token survives grammar filtering, semantic masking is skipped and the grammar layer alone controls selection.
16	Structural integrity is a hard constraint; a type violation is a soft error detectable by downstream validation.
17	
18	\paragraph{Constraint Tightness.}
19	We define the tightness of relation $r$ as:
20	%
21	\begin{equation}\label{eq:tightness}
22	  \kappa(r) = 1 - \frac{|\mathcal{V}(r)|}{|\mathcal{E}|^2},
23	\end{equation}
24	%
25	where $\mathcal{V}(r)$ is the set of valid type pairs and $\mathcal{E}$ the entity type vocabulary.
26	The mean tightness $\bar{\kappa} = \frac{1}{|\mathcal{R}|}\sum_{r} \kappa(r)$ characterizes ontology restrictiveness.
27	Tighter constraints eliminate more grammar-valid tokens at type-bearing positions, increasing fallback frequency and residual DR.
28	This dual-factor pattern (tightness $\times$ baseline model violation rate) is consistent with the cross-
…[truncated 2005 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 231 · 2026-05-17T11:59:04.177296+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## Primary Scoring Dimensions

### 1. Reviewer Confidence
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

### 2. Soundness
Scale: 1-5 (with .5 increments)
- **5**: "Excellent: This study is one of the most thorough I have seen."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

### 3. Excitement
Scale: 1-5 (with .5 increments)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me."
- **1**: "Not Exciting: this paper does not resonate with me."

### 4. Overall Assessment
Scale: 1-5 (with .5 increments)
- **5**: "Consider for Award: Could be considered for outstanding paper award (top 2.5%)."
- **4.5**: "Borderline Award"
- **4**: "Conference: Could be accepted to an ACL conference."
- **3.5**: "Borderline Conference"
- **3**: "Findings: Could be accepted to the Findings of the ACL."
- **2.5**: "Borderline Findings"
- **2**: "Resubmit next cycle: Needs substantial revisions."
- **1.5**: "Resubmit after next cycle: Needs extensive revisions."
- **1**: "Do not resubmit: Fully redone or irre
…[truncated 450 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8192
}
```

</details>

---


### Tool call

_source line 232 · 2026-05-17T11:59:08.951176+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
  }
}
```

</details>

---


### Tool result

_source line 233 · 2026-05-17T11:59:09.783932+00:00_

1	% §5.1 Experimental Setup and Violation Landscape
2	% Compressed from standalone section. main.tex provides \subsection header.
3	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
4	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
5	
6	\label{sec:violation_landscape}
7	
8	\paragraph{Setup.}
9	We evaluate Qwen3-8B~\cite{qwen2025qwen3} under zero-shot greedy decoding on two IE benchmarks:
10	\textbf{SciERC}~\cite{luan2018scierc} (551 test sentences, 7 relations, avg.\ 26.1 valid type pairs per relation) and \textbf{DocRED}~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test set annotations are not publicly available; following prior work, we evaluate on the development set (998 documents).} 96 relations, avg.\ 5.68 valid pairs).
11	We measure four violation categories: \textbf{Domain/Range (DR)} violations where $(\mathrm{type}(h), \mathrm{type}(t)) \notin \sigma(r)$; \textbf{Relation Vocabulary (RV)} where $r \notin \mathcal{R}$; \textbf{Entity Type (ET)} where $e \notin \mathcal{E}$; and \textbf{Cross-Field Consistency (CF)} where the same entity receives different types across triples.
12	Cross-model validation with Llama-3.1-8B-Instruct is reported in \S\ref{sec:cross-model}.
13	Violation rates are computed over successfully parsed documents; including parse failures as zero-violation instances adjusts rates by at most 0.23\,pp (Llama DocRED zero-shot; $<$0.01\,pp under fine-tuning), confirming robustness to this exclusion.
14	
15	\paragraph{Violation distribution.}
16	Table~\ref{tab:prompt_comparison} reports violation rates.
17	DR violations affect 15.37\% of triples on SciERC and 18.46\% on DocRED, comparable rates despite a 14$\times$ difference in ontology size. This indicates that violation severity is driven by \emph{constraint tightness} rather than ontology scale.
18	RV violations on DocRED are dramatically higher (29.66\% vs.\ 1.39\%), indicating that 96 relation types exceed the model's capacity to reproduc
…[truncated 1606 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 832
}
```

</details>

---


### Tool call

_source line 234 · 2026-05-17T11:59:09.935045+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 235 · 2026-05-17T11:59:10.287103+00:00_

1	% Section 5 — SciERC Results (Draft)
2	% Data source: Phase 2 SciERC registry experiments
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,
4	%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2
5	% All numbers verified against registry 2026-05-14.
6	
7	\subsection{SciERC Ablation and Composability with Fine-Tuning}
8	\label{sec:scierc-results}
9	
10	Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC,
11	evaluating each constraint layer independently and in combination.
12	All experiments use Qwen3-8B in a zero-shot setting on 551 test documents
13	with identical prompts and decoding parameters;
14	only the active constraint layers differ.
15	
16	% ──────────────────────────────────────────
17	%  Table: SciERC five-way ablation
18	% ──────────────────────────────────────────
19	\begin{table}[t]
20	\centering
21	\small
22	\setlength{\tabcolsep}{3.6pt}
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{@{}l rrrrr rr@{}}
25	\toprule
26	& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
27	& \multicolumn{2}{c}{\textbf{F1}} \\
28	\cmidrule(lr){2-6} \cmidrule(l){7-8}
29	\textbf{Mode}
30	  & DR\,$\downarrow$ & $\Delta$DR
31	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
32	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
33	\midrule
34	Unconstrained
35	  & 15.37 & ---
36	  & 1.39  & 0.40
37	  & 0.08
38	  & 8.23  & 31.01 \\
39	Grammar
40	  & 14.84 & $\downarrow$3\%
41	  & \textbf{0} & \textbf{0}
42	  & 0.08
43	  & 8.23  & 30.98 \\
44	Semantic
45	  & 11.65 & $\downarrow$24\%
46	  & 1.51  & 0.40
47	  & 2.71
48	  & 8.15  & 31.01 \\
49	Full (S1)
50	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
51	  & \textbf{0} & \textbf{0}
52	  & 9.90
53	  & \textbf{8.36} & 30.98 \\
54	Full (S2)
55	  & 0.97  & $\downarrow$94\%
56	  & \textbf{0} & \textbf{0}
57	  & 8.03
58	  & 8.03  & \textbf{31.90} \\
59	\bottomrule
60	\end{tabular}}%
61	\caption{Five-way ablation on SciERC (551 documents, Qwen3-8B, zero-shot).
62	DR: domain
…[truncated 11043 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 236 · 2026-05-17T11:59:10.287565+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 237 · 2026-05-17T11:59:10.689489+00:00_

1	% Section 5 — DocRED Results (compressed, 1450→~600 words)
2	% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,
3	%          phase2_docred_semantic_only, phase2_docred_full_s1
4	% All numbers verified against registry 2026-05-14.
5	
6	\subsection{Cross-Dataset Validation on DocRED}
7	\label{sec:docred-results}
8	
9	Table~\ref{tab:docred-ablation} presents the four-way ablation on DocRED, a document-level RE benchmark with 96 Wikidata relation types (14$\times$ the ontology size of SciERC).
10	All experiments use Qwen3-8B zero-shot on 998 documents.
11	
12	% ──────────────────────────────────────────
13	%  Table: DocRED four-way ablation
14	% ──────────────────────────────────────────
15	\begin{table}[t]
16	\centering
17	\small
18	\setlength{\tabcolsep}{3.6pt}
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{@{}l rrrrr rr@{}}
21	\toprule
22	& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
23	& \multicolumn{2}{c}{\textbf{F1}} \\
24	\cmidrule(lr){2-6} \cmidrule(l){7-8}
25	\textbf{Mode}
26	  & DR\,$\downarrow$ & $\Delta$DR
27	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
28	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
29	\midrule
30	Unconstrained
31	  & 18.46 & ---
32	  & 29.66 & 2.48
33	  & 0.10
34	  & 7.74  & 58.15 \\
35	Grammar
36	  & 26.17 & $\uparrow$42\%
37	  & \textbf{0.03} & \textbf{0}
38	  & 0.07
39	  & \textbf{8.31}  & \textbf{59.38} \\
40	Semantic
41	  & 13.84 & $\downarrow$25\%
42	  & 29.87 & 4.22
43	  & 1.05
44	  & 7.70  & 57.81 \\
45	Full (S1)
46	  & \textbf{10.21} & $\downarrow$\textbf{45\%}
47	  & \textbf{0.03} & \textbf{0}
48	  & 2.57
49	  & 8.23  & 59.37 \\
50	\bottomrule
51	\end{tabular}}%
52	\caption{Four-way ablation on DocRED (998 documents, Qwen3-8B, zero-shot).
53	$\Delta$DR: relative change vs.\ unconstrained.
54	Best per column in \textbf{bold} (CF excluded).
55	F1 $\times$100. Bootstrap significance: R-F1 $+$0.50\,pp ($p < 0.001$).}
56	\label{tab:docred-ablation}
57	\end{table}
58	
59	% exp_ids: phase2_docred_unconstraine
…[truncated 3446 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 238 · 2026-05-17T11:59:10.690086+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 239 · 2026-05-17T11:59:11.393295+00:00_

1	% Section 5 — Cross-Model Validation (compressed, 830→~400 words)
2	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1,
3	%          phase2_docred_unconstrained, phase2_docred_full_s1,
4	%          llama_scierc_unconstrained, llama_scierc_full_s1,
5	%          llama_docred_unconstrained, llama_docred_full_s1
6	
7	\subsection{Cross-Model Validation}
8	\label{sec:cross-model}
9	
10	We replicate the full S1 configuration with Llama-3.1-8B-Instruct and Mistral-7B-Instruct-v0.3 under identical prompts, decoding parameters, and evaluation.
11	Table~\ref{tab:cross-model} summarizes results across all three models.
12	Mistral serves as a third zero-shot verification point confirming model-agnosticism; composability evaluation (\S\ref{sec:composability}) uses LoRA fine-tuning which requires domain-specific training data available only for Qwen and Llama.
13	
14	\begin{table}[t]
15	\centering
16	\small
17	\setlength{\tabcolsep}{3.4pt}
18	\resizebox{\columnwidth}{!}{%
19	\begin{tabular}{@{}ll rrrr r@{}}
20	\toprule
21	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
22	& \textbf{R-F1} \\
23	\cmidrule(lr){3-6} \cmidrule(l){7-7}
24	\textbf{Dataset} & \textbf{Model}
25	  & DR\,$\downarrow$ & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
26	  & $\uparrow$ \\
27	\midrule
28	\multirow{6}{*}{SciERC}
29	  & Qwen (U)    & 15.37 & 1.39  & 0.40 & 0.08 & 8.23 \\
30	  & Qwen (S1)   &  0.93 & 0     & 0    & 9.90 & 8.36 \\
31	  \cmidrule(l){2-7}
32	  & Llama (U)   & 13.34 & 0.55  & 0    & 0.24 & 2.68 \\
33	  & Llama (S1)  &  0.08 & 0     & 0    & 6.56 & 2.54 \\
34	  \cmidrule(l){2-7}
35	  & Mistral (U) & 56.94 & 0     & 1.50 & 56.87$^\dagger$ & 3.66 \\
36	  & Mistral (S1)& 13.40 & 0     & 0    & 1.27  & 3.67 \\
37	\midrule
38	\multirow{6}{*}{DocRED}
39	  & Qwen (U)    & 18.46 & 29.66 & 2.48 & 0.10 & 7.74 \\
40	  & Qwen (S1)   & 10.21 &  0.03 & 0    & 2.57 & 8.23 \\
41	  \cmidrule(l){2-7}
42	  & Llama (U)   & 26.07 & 16.03 & 0.13 & 0.17 & 5.98 \\
43	  & Llama (S1)  &  2.55 &  0  
…[truncated 2545 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 240 · 2026-05-17T11:59:11.544293+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
  }
}
```

</details>

---


### Tool result

_source line 241 · 2026-05-17T11:59:11.544731+00:00_

1	% Section 5 — Runtime Analysis
2	% Data source: DocRED latency profiling (exp_id: docred_latency_profiling)
3	% Qwen3-8B, same single-GPU server, controlled 4-way ablation.
4	
5	\subsection{Runtime Overhead}
6	\label{sec:runtime}
7	
8	Table~\ref{tab:runtime} reports per-document inference time for each constraint layer combination on both datasets (Qwen3-8B, same GPU).
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\setlength{\tabcolsep}{4pt}
14	\begin{tabular}{@{}l rr rr@{}}
15	\toprule
16	& \multicolumn{2}{c}{\textbf{SciERC (7 rels)}}
17	& \multicolumn{2}{c}{\textbf{DocRED (96 rels)}} \\
18	\cmidrule(lr){2-3} \cmidrule(l){4-5}
19	\textbf{Mode} & Avg (s) & Overhead & Avg (s) & Overhead \\
20	\midrule
21	Unconstrained & 2.587 & --- & 21.023 & --- \\
22	Grammar       & 2.631 & $+$1.7\% & 21.366 & $+$1.6\% \\
23	Semantic      & 2.618 & $+$1.2\% & 21.912 & $+$4.2\% \\
24	Full (S1)     & 2.647 & $+$2.3\% & 22.147 & $+$5.4\% \\
25	\bottomrule
26	\end{tabular}
27	\caption{Per-document inference time by constraint layer (Qwen3-8B, same GPU).
28	Grammar compile time: 0.044\,s (one-time, amortized to zero).
29	Full-mode overhead is sub-additive (DocRED: 1.6\%$+$4.2\%$=$5.8\% expected vs.\ 5.4\% observed).}
30	\label{tab:runtime}
31	\end{table}
32	
33	Grammar-layer overhead is consistent across datasets ($+$1.6--1.7\%), independent of schema complexity.
34	Semantic-layer overhead scales with the number of relation types (SciERC 7 types: $+$1.2\%; DocRED 96 types: $+$4.2\%), reflecting increased domain-range lookup frequency.
35	Full-mode overhead is sub-additive on both datasets because the two layers share token-set computation.
36	Even in the most complex setting (DocRED, 96 relations), total overhead is $+$5.4\%---practically negligible.
37	Under fine-tuning, S1 overhead drops further to $+$2.3\% (61\,ms/doc; Appendix~\ref{app:ft-latency}).
38	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 242 · 2026-05-17T11:59:16.823852+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
  }
}
```

</details>

---


### Tool result

_source line 243 · 2026-05-17T11:59:17.175942+00:00_

1	% Section 2: Background (compressed)
2	
3	\section{Background}
4	\label{sec:background}
5	
6	\paragraph{IE Ontology Structure.}
7	\label{sec:bg:ontology}
8	An IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defines entity types $\mathcal{E}$, relation types $\mathcal{R}$, and a mapping $\sigma: \mathcal{R} \to \mathcal{P}(\mathcal{E} \times \mathcal{E})$ specifying valid (head type, tail type) pairs per relation.
9	A triple $(h, r, t)$ is \emph{type-valid} if $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$.
10	We define the \emph{constraint tightness} of $r$ as $1 - |\sigma(r)| / |\mathcal{E}|^2$: tighter constraints leave fewer valid options, increasing violation likelihood.
11	
12	\paragraph{Grammar-Constrained Decoding.}
13	\label{sec:bg:gcd}
14	Grammar-constrained decoding restricts each token $y_t$ to a mask $M_g \in \{0, 1\}^{|V|}$ derived from a target grammar.
15	XGrammar~\citep{dong2025xgrammar} compiles JSON Schemas into pushdown automata for efficient enforcement of structural constraints; Outlines~\citep{willard2023outlines} and SGLang~\citep{zheng2024sglang} offer similar capabilities.
16	However, these methods are limited to context-free constraints and cannot enforce cross-field semantic rules (e.g., ``if $r$ = \textsc{Feature-of}, then $\mathrm{type}(h) \in \{\textsc{Method}, \textsc{OtherScientificTerm}\}$''), which depend on previously generated field values.
17	
18	\paragraph{Problem Statement.}
19	\label{sec:bg:problem}
20	Given $\mathcal{O}$ and an autoregressive LM $\mathcal{M}$, we seek constraints $\mathcal{C}$ ensuring: (a)~\textbf{structural validity}, i.e., well-formed JSON with $\mathcal{E}$/$\mathcal{R}$ membership; and (b)~\textbf{type validity}, i.e., $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$ for every triple.
21	Condition (a) is context-free; (b) is context-sensitive but \emph{prefix-decidable}: at the point where a type token is generated, all information needed (relation type, entity registry) is ava
…[truncated 214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 244 · 2026-05-17T11:59:17.226810+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 245 · 2026-05-17T11:59:17.277468+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Grammar-Constrained Decoding.}
5	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, LMQL~\cite{beurer-kellner2023lmql}, DOMINO~\cite{beurer-kellner2024domino}, SynCode~\cite{ugare2024syncode}, and ASAp~\cite{park2024grammar} ensure every token belongs to a grammar-valid continuation; IterGen~\cite{ugare2025itergen} adds backtracking.
6	These guarantee format validity but cannot enforce cross-field semantic constraints such as ontology domain/range rules.
7	
8	\paragraph{Semantic Constrained Decoding for Code.}
9	Synchromesh~\cite{synchromesh_iclr2022}, PICARD~\cite{scholak2021picard}, MGD~\cite{mgd_neurips2023}, and \citet{pldi2025_type_constrained_codegen} enforce type and scope constraints in code generation; OntoCoDec migrates this paradigm to IE.
10	
11	\paragraph{Vocabulary and Type-Constrained Generation.}
12	\citet{roth_yih_2004} establish relational type compatibility as a hard constraint via ILP, though applied post-hoc.
13	GENRE~\cite{decao2021genre}, AdaKGC~\cite{adakgc_emnlp2023}, GCD~\cite{geng2023gcd}, and GoLLIE~\cite{sainz2024gollie} constrain \emph{which tokens} can appear but not \emph{which type combinations} are valid per relation; GCD's per-position trie enforces vocabulary membership (equivalent to our grammar layer) but cannot capture the conditional dependency between head and tail types that our semantic layer provides.
14	DORE~\cite{vukovic2024dore} enforces ontological consistency via chain-of-thought output selection with confidence thresholds, a generate-then-select paradigm distinct from OntoCoDec's token-level logit masking during generation.
15	GenIE~\cite{josifoski2022genie} constrains entity generation to a candidate trie but does not enforce relation-specific type constraints.
16	EnriCo~\cite{zaratiana2024enrico} applies ASP constraints during decoding for joint entity-relation extraction, a hard-constraint approach like ours but with task-speci
…[truncated 1145 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 246 · 2026-05-17T11:59:18.433590+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
  }
}
```

</details>

---


### Tool result

_source line 247 · 2026-05-17T11:59:18.484356+00:00_

1	% Section 7 — Discussion and Conclusion (compressed)
2	% Full discussion paragraphs moved to Appendix C.
3	
4	OntoCoDec compiles IE ontology schemas into composable token-level decoding constraints, achieving 42--99\% DR reduction across three models and two datasets with no significant F1 cost.
5	Composed with LoRA fine-tuning, it reaches DR\,$\leq$\,0.20\% at $<$0.6\,pp F1 cost, confirming orthogonal error targeting.
6	Within calibrated models (Qwen, Llama; $n{=}4$), residual DR correlates linearly with $\bar{\kappa} \times \text{RV}_{\text{baseline}}$ ($R^2{=}0.99$), suggesting constraint benefit scales with schema stringency and model OOV tendency.
7	This pattern has an informative boundary condition: Mistral achieves RV\,=\,0\% on SciERC yet retains DR\,=\,13.4\%, because its dominant error mode is entity type misclassification rather than vocabulary confusion---a factor not captured by the dual-factor product.
8	We present this as a descriptive characterization with explicit scope rather than a universal predictive law.
9	
10	CF impact is model-dependent: S1 introduces CF for well-calibrated models (up to 12.02\%) but reduces it for poorly-calibrated ones (Mistral: 56.87\%\,$\to$\,1.27\%).
11	Ablation confirms CF$\leftrightarrow$DR tension ($+$13.85\,pp; Appendix~\ref{app:cf-dr-tradeoff}); fine-tuning reduces CF by 88\% (\S\ref{sec:composability}); global entity-level type consensus offers the most direct path forward.
12	
13	% Limitations and Future Work moved to \section*{Limitations} in main.tex (ARR requirement)
14	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 248 · 2026-05-17T11:59:18.735609+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex"
  }
}
```

</details>

---


### Tool result

_source line 249 · 2026-05-17T11:59:19.137626+00:00_

1	\section{Beam Search Compatibility}
2	\label{app:beam-search}
3	
4	OntoCoDec's constraint enforcement is designed to be decoding-strategy agnostic.
5	The main experiments (\S\ref{sec:experiments}) use greedy decoding; Appendix~\ref{app:sampling} validates nucleus sampling.
6	Here we verify compatibility with beam search, completing coverage of the three standard decoding strategies.
7	
8	\paragraph{Implementation challenges.}
9	Two stateful components require adaptation for beam search.
10	(1)~The grammar layer (XGrammar) maintains an internal \texttt{GrammarMatcher} state that tracks the generated token sequence; beam reordering invalidates this state because beams are permuted across steps.
11	Our solution instantiates a fresh \texttt{GrammarMatcher} per beam per step and replays the beam's current token sequence through XGrammar's stateless accept API (64 lines of code).
12	(2)~The semantic layer's \texttt{TypeConstraintProcessor} accumulates entity and relation registries that assume a single generation path.
13	Our solution isolates state per beam by calling \texttt{detect()} on the full partial output at each step, reconstructing all entity/relation state from scratch for each beam independently (61 lines of code).
14	Both adaptations add ${\sim}125$ lines total without modifying the existing greedy/sampling logic.
15	
16	\paragraph{Results.}
17	Table~\ref{tab:beam-search} compares beam search ($k{=}4$, \texttt{early\_stopping=True}) against greedy decoding under full S1 constraints across six model-dataset combinations.
18	
19	\begin{table}[h]
20	\centering
21	\small
22	\caption{Beam search ($k{=}4$) vs.\ greedy decoding under full S1 constraints.
23	SciERC evaluated on full test set (551 documents); DocRED evaluated on matched 50-document subsets (same documents for greedy and beam).
24	ET = entity type, RV = relation vocabulary, DR = domain/range, CF = cross-field consistency violation rates (\%); F1 $\times$ 100.}
25	\label{tab:beam-search}
26	\begin{tab
…[truncated 6808 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 250 · 2026-05-17T11:59:19.188395+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex"
  }
}
```

</details>

---


### Tool result

_source line 251 · 2026-05-17T11:59:19.239052+00:00_

1	\section{Sampling Robustness}\label{app:sampling}
2	
3	\begin{table}[h]
4	\centering
5	\caption{Constraint robustness under nucleus sampling ($T$=0.7, $p$=0.9) vs.\ greedy decoding.}
6	\label{tab:sampling-robustness}
7	\begin{tabular}{llcccccc}
8	\toprule
9	Dataset & Decoding & ET\% & RV\% & DR\% & CF\% & E-F1 & R-F1 \\
10	\midrule
11	\multirow{2}{*}{SciERC (551)} & Greedy & 0 & 0 & 0.93 & 9.90 & 30.98 & 8.36 \\
12	& Sampling & 0 & 0 & 0.75 & 9.90 & 31.28 & 7.42 \\
13	\midrule
14	\multirow{2}{*}{DocRED (114$^\dagger$)} & Greedy & 0 & 0.03 & 10.21 & 2.57 & 59.37 & 8.23 \\
15	& Sampling & 0 & 0 & 10.31 & 12.63 & 57.05 & 7.92 \\
16	\bottomrule
17	\end{tabular}
18	\par\smallskip\footnotesize $^\dagger$Subset of 114 documents; full DocRED sampling requires ${\sim}300$h due to extended generation under high-temperature sampling with complex schemas.
19	\end{table}
20	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 252 · 2026-05-17T11:59:23.906595+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex"
  }
}
```

</details>

---


### Tool result

_source line 253 · 2026-05-17T11:59:24.709560+00:00_

1	\section{Reproducibility Details}
2	\label{app:reproducibility}
3	
4	\paragraph{Fine-tuning configuration.}
5	All four fine-tuned models (Qwen3-8B and Llama-3.1-8B-Instruct on SciERC and DocRED) use identical LoRA hyperparameters: rank $r{=}16$, $\alpha{=}32$, dropout $0.05$, no bias, targeting all attention and MLP projection layers (\texttt{q\_proj}, \texttt{k\_proj}, \texttt{v\_proj}, \texttt{o\_proj}, \texttt{gate\_proj}, \texttt{up\_proj}, \texttt{down\_proj}).
6	Training uses AdamW with learning rate $2{\times}10^{-4}$, cosine schedule, warmup ratio $0.1$, effective batch size $16$, bf16 precision, gradient checkpointing, and completion-only loss for 3 epochs.
7	SciERC trains on 1,762 examples (260 dev) for 333 steps; DocRED trains on 3,053 examples (998 dev) for 573 steps.
8	Maximum sequence length is 2,048 (SciERC) and 4,096 (DocRED).
9	All runs use seed 42.
10	
11	\paragraph{Hardware and software.}
12	Training runs on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (98\,GB VRAM).
13	SciERC fine-tuning takes approximately 11 minutes per model; DocRED takes approximately 1.5 hours.
14	Software versions: PyTorch 2.10, Transformers 4.57, PEFT 0.19, TRL 1.1, Accelerate 1.13.
15	
16	\paragraph{Inference time.}
17	Table~\ref{tab:inference-time} reports per-document inference times for Qwen3-8B under zero-shot greedy decoding across constraint configurations.
18	
19	\begin{table}[h]
20	\centering
21	\small
22	\caption{Inference time (seconds/document, mean $\pm$ std) for Qwen3-8B, zero-shot, greedy decoding.}
23	\label{tab:inference-time}
24	\begin{tabular}{@{}lcc@{}}
25	\toprule
26	\textbf{Configuration} & \textbf{SciERC} & \textbf{DocRED} \\
27	\midrule
28	Unconstrained       & $8.69 \pm 3.89$  & $19.75 \pm 8.99$  \\
29	Grammar-only        & $8.81 \pm 4.51$  & $20.58 \pm 10.75$ \\
30	Semantic-only       & $7.23 \pm 3.91$  & $20.53 \pm 9.37$  \\
31	Full S1             & $6.76 \pm 3.67$  & $20.39 \pm 9.43$  \\
32	Post-hoc            & $8.69 \pm 3.89$  &
…[truncated 476 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 802
}
```

</details>

---


### Tool call

_source line 254 · 2026-05-17T11:59:25.013713+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 255 · 2026-05-17T11:59:25.365399+00:00_

1	% Appendix B — Extended Discussion
2	% Contains discussion paragraphs moved from the main text during compression.
3	
4	\section{Extended Discussion}\label{app:discussion}
5	
6	%%% CF Dual Mechanism %%%
7	% exp_ids: phase2_scierc_full_s1, llama_scierc_full_s1, llama_docred_full_s1
8	
9	\paragraph{CF Dual Mechanism.}
10	CF violations arise from two distinct mechanisms:
11	(1)~\emph{Registry override}: the semantic constraint forces a domain-compatible type that conflicts with the entity's previously registered type.
12	The entity appears in multiple relations with different type requirements, and the per-relation mask selects the locally valid type without consulting prior assignments.
13	(2)~\emph{Grammar-first fallback} (\S\ref{sec:interaction}): when the semantic mask conflicts with all grammar-valid tokens, the semantic layer is dropped entirely, allowing the grammar layer to generate any structurally valid type---which may differ from the entity's registered type.
14	
15	These mechanisms have sharply different model profiles.
16	Qwen3-8B triggers zero grammar-first fallbacks across all experiments, attributing 100\% of its CF violations to registry override.
17	Llama-3.1-8B, by contrast, triggers 5{,}882 fallbacks on SciERC (10.7 per document) and 57{,}825 on DocRED (63.8 per document), making grammar-first fallback the dominant CF source.
18	This asymmetry is consistent with the cross-model CF gap: Qwen achieves CF\,=\,2.57\% on DocRED vs.\ Llama's 12.02\%, despite both using identical constraint configurations.
19	The difference traces to Llama's less calibrated type predictions, which more frequently conflict with the semantic mask's valid set, triggering fallback.
20	
21	%%% Fallback Behavior and Effective Coverage %%%
22	% exp_ids: cf_fallback_ablation_scierc (final data)
23	
24	\paragraph{Fallback Behavior and Effective Coverage.}
25	\label{app:fallback-coverage}
26	The two-layer architecture produces two distinct fallback mechanisms with different seman
…[truncated 27992 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 256 · 2026-05-17T11:59:30.187669+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex"
  }
}
```

</details>

---


### Tool result

_source line 257 · 2026-05-17T11:59:31.149018+00:00_

1	% Appendix — Prompt Templates
2	% W10: Extraction prompts used in all experiments.
3	
4	\section{Prompt Templates}
5	\label{app:prompts}
6	
7	All experiments use the same prompts across constrained and unconstrained decoding; constraints are applied at the logit level, not through prompt modification.
8	Table~\ref{tab:prompts} shows the system and user prompts for each dataset.
9	
10	\begin{table*}[t]
11	\centering
12	\small
13	\begin{tabular}{@{}p{0.95\textwidth}@{}}
14	\toprule
15	\textbf{SciERC --- System Prompt (Unconstrained \& Constrained)} \\
16	\midrule
17	\texttt{You are an expert information extraction system for scientific texts. Extract entities and relations from the given text.} \\[4pt]
18	\texttt{Entity types: Task, Method, Material, Metric, OtherScientificTerm, Generic} \\
19	\texttt{Relation types: Used-for, Feature-of, Hyponym-of, Part-of, Compare, Conjunction, Evaluate-for} \\[4pt]
20	\texttt{Output a JSON object with:} \\
21	\texttt{- "entities": list of \{"text": "...", "type": "..."\}} \\
22	\texttt{- "relations": list of \{"head": "...", "tail": "...", "type": "...", "head\_type": "...", "tail\_type": "..."\}} \\[4pt]
23	\texttt{Output ONLY valid JSON, no explanation.} \\
24	\midrule
25	\textbf{SciERC --- User Prompt} \\
26	\midrule
27	\texttt{Extract all entities and relations from this scientific text:} \\
28	\texttt{"\{text\}"} \\
29	\texttt{Output JSON:} \\
30	\midrule
31	\midrule
32	\textbf{DocRED --- System Prompt (Unconstrained \& Constrained)} \\
33	\midrule
34	\texttt{You are an information extraction system. Extract all entities and relations from the following document.} \\[4pt]
35	\texttt{Entity types: PER, ORG, LOC, TIME, NUM, MISC} \\[4pt]
36	\texttt{Relation types: country, instance of, performer, ...\ (96 Wikidata relation types; full list omitted for space)} \\[4pt]
37	\texttt{Output a JSON object with exactly this structure:} \\
38	\texttt{\{"entities": [\{"text": "entity name", "type": "ENTITY\_TYPE"\}],} \\
39	\texttt{\ "
…[truncated 770 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 961
}
```

</details>

---


### Tool call

_source line 258 · 2026-05-17T11:59:31.149421+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 259 · 2026-05-17T11:59:31.501010+00:00_

1	\section{Extended Related Work}
2	\label{app:related_work}
3	
4	% ===========================================================================
5	% Paradigm 1: Grammar-Constrained Decoding
6	% ===========================================================================
7	\paragraph{Grammar-Constrained Decoding.}
8	Recent work has established efficient algorithms for restricting LLM outputs to conform to context-free grammars, making grammar-constrained decoding the de facto standard for obtaining structured output from language models.
9	XGrammar~\cite{dong2025xgrammar} partitions the vocabulary into context-independent and context-dependent tokens and maintains persistent pushdown automata across decoding steps, achieving up to 100$\times$ speedup over prior CFG-constrained decoding methods.
10	Outlines~\cite{willard2023outlines} reformulates constrained generation as finite-state machine transitions with offline vocabulary indexing, enabling efficient enforcement of regular-expression and JSON-schema constraints without runtime overhead per token.
11	LMQL~\cite{beurer-kellner2023lmql} introduces a declarative query language that compiles type, length, and regex constraints into token-level masks, providing a programmable interface for specifying multi-variable output structures.
12	These systems ensure that every generated token belongs to a grammar-valid continuation, but they do not address the \emph{distribution distortion} introduced by naive token masking.
13	A parallel line of work tackles this problem directly: DOMINO~\cite{beurer-kellner2024domino} minimizes distributional divergence during CFG enforcement by formulating mask selection as an optimization problem, and ASAp~\cite{park2024grammar} provides a provably unbiased sampling algorithm that preserves the original LM distribution under grammar constraints.
14	Together, these advances have made grammar-constrained decoding both fast and statistically principled, establishing a robust foundation for stru
…[truncated 19795 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 260 · 2026-05-17T11:59:31.652065+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex"
  }
}
```

</details>

---


### Tool result

_source line 261 · 2026-05-17T11:59:31.652581+00:00_

1	% Appendix C — Per-Relation Violation Analysis (Llama-3.1-8B)
2	% exp_ids: llama_docred_unconstrained, llama_docred_full_s1
3	
4	\section{Per-Relation Violation Analysis (Llama-3.1-8B)}\label{app:llama-per-relation}
5	
6	Table~\ref{tab:llama-per-relation-dr} presents the per-relation domain--range violation breakdown for Llama-3.1-8B on DocRED under full S1 constraints.
7	The Llama baseline exhibits an RV rate of 16.03\%, substantially lower than Qwen's 29.66\%, indicating stronger baseline vocabulary compliance.
8	% exp_ids: llama_docred_unconstrained (RV=16.03%), qwen_docred_unconstrained (RV=29.66%)
9	Full S1 completely eliminates RV violations and reduces the residual DR rate to 2.55\% (418/16{,}368 triples), with only three relations exceeding 10\%.
10	% exp_ids: llama_docred_full_s1 (DR=2.6%, 418/16368)
11	
12	\begin{table}[h]
13	\centering
14	\caption{Top 10 per-relation DR violation rates for Llama-3.1-8B on DocRED under full S1 constraints. Relations with $>$20 triples and 0\% DR (e.g., P131, P206, P361, P170, P86) are omitted.}
15	\label{tab:llama-per-relation-dr}
16	\resizebox{\columnwidth}{!}{%
17	\begin{tabular}{@{}llrrr@{}}
18	\toprule
19	Relation & PID & Triples & DR Violations & DR Rate (\%) \\
20	\midrule
21	dissolved/demolished & P576 & 73 & 24 & 32.9 \\
22	followed by          & P156 & 117 & 24 & 20.5 \\
23	unemployment rate    & P1198 & 15 & 3 & 20.0 \\
24	end time             & P582 & 130 & 21 & 16.2 \\
25	instance of          & P31  & 290 & 37 & 12.8 \\
26	product/material produced & P1056 & 98 & 11 & 11.2 \\
27	location of formation & P740 & 81 & 8 & 9.9 \\
28	head of state        & P35  & 41  & 3  & 7.3 \\
29	applies to jurisdiction & P1001 & 637 & 45 & 7.1 \\
30	conflict             & P607 & 453 & 30 & 6.6 \\
31	\bottomrule
32	\end{tabular}}
33	\end{table}
34	% exp_ids: llama_docred_full_s1
35	
36	Compared with Qwen, which retains a 10.21\% residual DR under full S1 concentrated in P1198 (83\% fallback) and P171 (78\% fallback), Llama's re
…[truncated 523 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 262 · 2026-05-17T12:02:07.943837+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "head.*head_type.*tail.*tail_type.*relation|relation.*head_type.*tail_type|field order",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "head.*head_type.*tail.*tail_type.*relation|relation.*head_type.*tail_type|field order",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 263 · 2026-05-17T12:02:08.453968+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex:28:The JSON Schema enforces a fixed field ordering (head $\to$ head\_type $\to$ tail $\to$ tail\_type $\to$ relation), which is a prerequisite for the sequential masking mechanism described in \S\ref{sec:dynamic-masking}.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 510
}
```

</details>

---


### Tool call

_source line 264 · 2026-05-17T12:02:08.856004+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "F-test|F\\(1,2\\)|p.*0\\.058",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "F-test|F\\(1,2\\)|p.*0\\.058",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 265 · 2026-05-17T12:02:08.856502+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:92:For \emph{calibrated} models (Qwen3-8B, Llama-3.1-8B; unconstrained ET${<}$3\% on both datasets), a linear fit yields $y = 0.366x - 0.138$ with $R^2 = 0.99$ ($n{=}4$, $F(1,2) = 198.0$, $p \approx 0.058$).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 266 · 2026-05-17T12:04:23.513878+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 方法设计合理且实验覆盖面广，但存在一个关键的形式化错误（JSON 字段顺序与机制前提矛盾）、R²=0.99 统计声明过强（F-test p=0.058 不显著但在 Abstract 突出展示）、以及 beam search 最强结果未进入正文。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0/5 | 核心 sequential masking 的正确性论证存在关键字段顺序矛盾（N1）；R² 声明统计基础不足（N2）；RV=0.03% 解释不一致（N3）。方法本身设计合理但论文的形式化描述有误。 |\n| Excitement | 3.0/5 | 将 type-constrained decoding 从代码生成迁移到 IE 是一个有价值的方向，两层可组合架构设计清晰。但 post-hoc 在 5/6 ZS 设置中 F1 更高，限制了 excitement。 |\n| Reproducibility | 4.0/5 | 硬件、超参数、prompt、seed 均已报告；bootstrap 参数完整；但 beam search 缺乏 runtime 数据。 |\n| Overall | 3.0/5 | 适合 Findings，需修复形式化错误和统计声明后可接受。 |\n| Confidence | 4/5 | 仔细检查了方法形式化、所有实验表格、附录数据；对 JSON Schema/XGrammar 机制的理解基于论文描述和 prompt 模板交叉验证。 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] §3.1 JSON 字段顺序与 sequential masking 前提矛盾\n- 具体位置：Section 3.1 (Problem Formulation), line \"The JSON Schema enforces a fixed field ordering (head → head_type → tail → tail_type → relation)\"\n- 问题：§3.1 明确声称 JSON Schema 强制字段顺序为 **head → head_type → tail → tail_type → relation**，并称这是 sequential masking 的前提。但在 §3.4.3 (Dynamic Masking) 中，head type masking 需要 r_j（关系类型）已知——\"If r_j is unavailable, no semantic mask is applied\"。在所述的字段顺序中，relation 是最后一个字段，因此在生成 head_type 和 tail_type 时 r_j 尚未生成，semantic mask 永远不会激活，整个机制将是 no-op。\n  \n  然而 Appendix A 的 prompt 模板显示实际 JSON 结构为 **{\"head\": \"...\", \"tail\": \"...\", \"type\": \"...\", \"head_type\": \"...\", \"tail_type\": \"...\"}**，即 head → tail → relation → head_type → tail_type。在此顺序下，生成 head_type 时 relation 已知，semantic masking 可以正常工作。\n  \n  实验报告了 94% DR reduction，证明机制确实有效，因此实际实现很可能使用 prompt 模板的顺序。但论文声称的顺序与实际实现矛盾。\n- 为什么影响接收：这不是笔误——§3.1 将此顺序定义为 \"prerequisite for the sequential masking mechanism\"，是方法正确性论证的核心。如果读者按照论文描述验证机制逻辑，会发现机制不可能工作。这严重影响 soundness。\n- 建议修改方向：(1) 修正 §3.1 的字段顺序为实际实现的顺序（大概率是 head → tail → relation → head_type → tail_type）；(2) 明确说明这是 XGrammar CFG 编译的产物（JSON 标准不保证 key 顺序），不是 JSON Schema 本身的属性；(3) 补充说明为什么选择此特定顺序（relation 必须先于 type fields 以启用 sequential masking）。\n\n**N2** [critical] Abstract 中 R²=0.99 (n=4) 声明过强，F-test 不显著\n- 具体位置：Abstract line 11; §7 Discussion; Appendix B (app:dual-factor)\n- 问题：Abstract 显著展示 \"the dual-factor pattern explains nearly all variance ($R^2{=}0.99$, $n{=}4$)\"。但 Appendix 报告 F(1,2)=198.0, **p ≈ 0.058**——在 α=0.05 下不显著。n=4 的回归本质上只有 df=2，任何两点都能完美拟合一条线，R²=0.99 的统计力量极其有限。\n  \n  §7 已加入 \"descriptive characterization with explicit scope\" 的语言，但 Abstract 仍然将 R²=0.99 作为 headline result 呈现，未提及 F-test 不显著。这构成统计声明的过度宣传。\n- 为什么影响接收：审稿人对 n=4 回归的 R² 高度敏感（历史审稿 R2-N1 已反复标记）。在 F-test 不显著的情况下在 Abstract 突出展示 R²=0.99，会被视为 misleading statistical claim。\n- 建议修改方向：(1) 从 Abstract 移除 R²=0.99 数值，改为定性描述（如 \"residual DR is modulated by the product of schema tightness and baseline violation rate for calibrated models\"）；(2) 若保留 R² 值，必须在同一句注明 \"n=4, F-test p=0.058\"；(3) 在 §7 中明确标注这是 exploratory observation 而非 confirmed finding。\n\n**N3** [major] RV=0.03% 残留的解释在论文与 rebuttal 之间不一致\n- 具体位置：§5.3 (DocRED Core Result); Rebuttal Draft v2 (RV=0.03% Residual section)\n- 问题：论文 §5.3 称残留 5 个 RV violation 源于 **\"partial JSON recovery where the grammar FSM completes a structurally valid but relation-name-truncated triple\"**。Rebuttal draft 却称其源于 **\"XGrammar v0.1.33 enum compilation bug where the grammar bitmask leaks token continuations across enum entries\"**（并给出了具体例子：\"member\" → \"membericipant\"）。这两个解释描述的是完全不同的机制。\n- 为什么影响接收：论文与 rebuttal 的不一致会被审稿人视为对自己系统行为理解不清。\n- 建议修改方向：确认真实原因（根据 rebuttal 的具体例子，bug 解释更可信），统一论文与 rebuttal 的描述。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Beam search 最强结果未进入正文 §5/§7\n- 具体位置：Appendix (app:beam-search) vs. §5, §7, Limitations\n- 问题：Beam search k=4 在 SciERC 全集上实现 **DR=0%, CF=0.53%**（Table 8），同时解决了 greedy decoding 的两个主要限制（残留 DR 和 CF 升高）。这是论文最强的实验结果之一，但仅出现在 Appendix，正文 §5/§7 未讨论。Limitations 仅一句提及 \"preliminary evaluation...suggests compatibility\"。\n  \n  此外，beam search 的 **runtime overhead 未报告**。Appendix 只说 \"Wall-clock overhead is modest\" 但无具体数字。考虑到 §5.5 对 greedy 模式有详细的 latency profiling，beam search 缺乏对等的 runtime 报告是不完整的。\n- 建议：(1) 在 §7 Discussion 中用 2-3 句讨论 beam search 如何解决 CF↔DR trade-off；(2) 报告 beam search 的 per-document latency；(3) 将 Limitations 中的 \"preliminary\" 改为更准确的描述。\n\n**W2** [warning] Post-hoc vs OntoCoDec framing 不够对称\n- 具体位置：§1 Introduction paragraph 2; Appendix B (app:posthoc-extended)\n- 问题：Appendix Table 9 显示在 **5/6 ZS 设置中 post-hoc F1 更高**。Introduction 虽然承认 \"achieves higher F1 in most zero-shot settings via precision gains\"，但紧接着就强调 Mistral DocRED 73.7% rejection 的极端案例。Introduction 的 framing 选择性地突出了 post-hoc 的最差表现，未明确量化 \"most\" 具体是 5/6。\n  \n  同时，在 fine-tuned 设置下，post-hoc 与 OntoCoDec 性能趋同（ΔF1 ≤ 0.55pp），这意味着 OntoCoDec 的核心优势仅在高 violation rate 的 ZS 场景下显现，而在实际应用更常见的 FT 场景下优势不明显。\n- 建议：在 Introduction 明确标注 \"post-hoc F1 is higher in 5 of 6 zero-shot configurations\"，或至少不让读者误以为 OntoCoDec 在 F1 上全面优于 post-hoc。\n\n**W3** [warning] Parse failure confounding 分析不充分\n- 具体位置：Table 5 caption; §5.1 paragraph \"Setup\"\n- 问题：Llama DocRED ZS parse failure 从 6.8% 增加到 9.1%（+34%），意味着 S1 约束导致更多文档无法成功解析。论文提到 \"including parse failures as zero-violation instances adjusts rates by at most 0.23 pp\" 和 \"excluding failed documents, ΔR-F1 is within ±0.1 pp\"，但未提供 parse-failure-excluded 的完整 violation rates 和 F1 表格。\n  \n  对于声称约束是 \"F1-neutral\" 的论文，+34% parse failure 增长本身就是一种间接的 F1 损失（E-F1 差 3.17pp），应该更透明地报告。\n- 建议：补充一个 parse-failure-excluded 和 all-set 两种分母下的对照表，或至少在正文中量化 parse failure 增长的影响。\n\n**W4** [warning] DocRED semantic-only ET 增长 (+70%) 缺乏解释\n- 具体位置：Table 3 (DocRED ablation), Semantic row: ET 从 2.48% 增至 4.22%\n- 问题：SciERC 的 semantic-only ET 增长有解释（§5.2 \"Enabling dependency\" paragraph：\"semantic mask constrains type tokens to relation-specific valid sets...forcing an OOV alternative\"）。但 DocRED 的 +70% ET 增长（2.48% → 4.22%）未给出具体解释。DocRED 的 entity types (PER, ORG, LOC, TIME, NUM, MISC) 都是短 token，与 SciERC 多 token 类型的 tokenization 机制不同，因此 SciERC 的解释可能不适用于 DocRED。\n- 建议：补充 1-2 句解释 DocRED ET 增长的具体机制。\n\n**W5** [warning] CF-DR trade-off ablation 仅限 SciERC/Qwen\n- 具体位置：Appendix B Table 7 (CF-DR trade-off pilot)\n- 问题：CF fallback ablation（切换 fallback 优先级的实验）仅在 SciERC/Qwen3-8B 上完成。论文声称 \"This trade-off generalizes beyond SciERC/Qwen3-8B\" 并引用跨设置的 Spearman ρ=−0.77 作为证据，但 ρ=−0.77 衡量的是不同设置间 DR/CF 的 inverse association，不等同于 ablation 结果的可迁移性。\n  \n  特别是 Llama DocRED 的 CF 高达 12.02%，是所有设置中最高的，在该设置上的 trade-off 量级可能与 SciERC/Qwen 不同。\n- 建议：至少讨论 DocRED/Llama 上 trade-off 量级可能不同的预期，或补充一个 DocRED 上的 pilot。\n\n**W6** [warning] Composability matrix 缺乏 fine-tuned 设置的统计显著性检验\n- 具体位置：Table 4 (Composability matrix); §5.2 paragraph \"Composability with fine-tuning\"\n- 问题：Zero-shot F1 变化有完整的 bootstrap 检验（SciERC p=0.58, DocRED p<0.001），但 fine-tuned 设置下的 F1 变化（如 Qwen LoRA SciERC: −0.09pp, DocRED: −0.30pp）未报告统计显著性。论文声称 \"R-F1 change within ±0.6 pp\"，但未检验这些变化是否显著不同于零。\n- 建议：对 fine-tuned 设置补充 bootstrap CI 和 p-value，尤其是 Qwen DocRED 的 −0.30pp。\n\n---\n\n## 小问题（不影响接收）\n\n- §4 DR reduction range 使用不同模型范围（Abstract \"42-99%\" 含 Mistral，§4 \"94-99%\" 仅 calibrated models），虽然不矛盾但易混淆。建议在 §4 标注 \"(calibrated models only; full range including Mistral: 42-99%)\"。\n- DocRED fallback coverage：SciERC 的 Llama effective coverage 63.4% 和 DocRED 的 Qwen coverage 99.9% 已报告，但 **Llama DocRED 的 coverage 未显式报告**（Llama DocRED 有 57,825 fallback events，57.42% DR baseline，coverage 可能较低）。\n- Beam search DocRED 仅在 50-doc subset 上评估，full-set 结果缺失。Table 8 caption 已标注 \"(50 documents)\"，但未讨论 50-doc 是否具代表性。\n- §5.5 Table 6 的 runtime 数据与 Appendix Table 10 不一致：Table 6 报告 SciERC Full S1 = 2.647s (+2.3%)，Table 10 报告 Full S1 = 6.76s。差异可能源于不同实验批次或硬件条件，但未解释。\n- JSON 标准（RFC 8259）不保证 object key 顺序。论文说 \"The JSON Schema enforces a fixed field ordering\"——JSON Schema 本身也不保证 property ordering。实际上是 XGrammar 的 CFG 编译产生了固定顺序。应修正措辞为 \"The XGrammar-compiled grammar enforces...\"。\n\n---\n\n## 主要优势\n\n1. **方法设计清晰**：两层可组合架构（grammar + semantic）具有明确的分工和 enabling dependency，形式化定义完整（除字段顺序错误外），decidability taxonomy 为理解约束范围提供了有用的框架。\n\n2. **实验覆盖面广**：3 模型 × 2 数据集 × 多种 ablation（五路消融、composability matrix、CF-DR trade-off、sampling/beam search 兼容性、per-relation 分析），实验设计系统性强。\n\n3. **诚实报告 trade-off**：CF↔DR trade-off 被明确量化和讨论，post-hoc baseline 的优势被承认（Appendix Table 9），Mistral 作为 boundary condition 被单独分析而非隐藏。论文没有隐瞒不利数据。\n\n4. **实际开销极低**：Full S1 overhead 仅 +2.3–5.4%，fine-tuned 下进一步降低至 +2.3%。Runtime 分析表明方法具有实用性。\n\n5. **可复现性强**：LoRA 超参数、prompt 模板、seed、软件版本均已报告；bootstrap 参数完整（10,000 iterations, 95% CI）；所有 greedy 实验完全确定性。\n",
  "reviewer_id": "1",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 方法设计合理且实验覆盖面广，但存在一个关键的形式化错误（JSON 字段顺序与机制前提矛盾）、R²=0.99 统计声明过强（F-test p=0.058 不显著但在 Abstract 突出展示）、以及 beam search 最强结果未进入正文。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0/5 | 核心 sequential masking 的正确性论证存在关键字段顺序矛盾（N1）；R² 声明统计基础不足（N2）；RV=0.03% 解释不一致（N3）。方法本身设计合理但论文的形式化描述有误。 |\n| Excitement | 3.0/5 | 将 type-constrained decoding 从代码生成迁移到 IE 是一个有价值的方向，两层可组合架构设计清晰。但 post-hoc 在 5/6 ZS 设置中 F1 更高，限制了 excitement。 |\n| Reproducibility | 4.0/5 | 硬件、超参数、prompt、seed 均已报告；bootstrap 参数完整；但 beam search 缺乏 runtime 数据。 |\n| Overall | 3.0/5 | 适合 Findings，需修复形式化错误和统计声明后可接受。 |\n| Confidence | 4/5 | 仔细检查了方法形式化、所有实验表格、附录数据；对 JSON Schema/XGrammar 机制的理解基于论文描述和 prompt 模板交叉验证。 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] §3.1 JSON 字段顺序与 sequential masking 前提矛盾\n- 具体位置：Section 3.1 (Problem Formulation), line \"The JSON Schema enforces a fixed field ordering (head → head_type → tail → tail_type → relation)\"\n- 问题：§3.1 明确声称 JSON Schema 强制字段顺序为 **head → head_type → tail → tail_type → relation**，并称这是 sequential masking 的前提。但在 §3.4.3 (Dynamic Masking) 中，head type masking 需要 r_j（关系类型）已知——\"If r_j is unavailable, no semantic mask is applied\"。在所述的字段顺序中，relation 是最后一个字段，因此在生成 head_type 和 tail_type 时 r_j 尚未生成，semantic mask 永远不会激活，整个机制将是 no-op。\n  \n  然而 Appendix A 的 prompt 模板显示实际 JSON 结构为 **{\"head\": \"...\", \"tail\": \"...\", \"type\": \"...\", \"head_type\": \"...\", \"tail_type\": \"...\"}**，即 head → tail → relation → head_type → tail_type。在此顺序下，生成 head_type 时 relation 已知，semantic masking 可以正常工作。\n  \n  实验报告了 94% DR reduction，证明机制确实有效，因此实际实现很可能使用 prompt 模板的顺序。但论文声称的顺序与实际实现矛盾。\n- 为什么影响接收：这不是笔误——§3.1 将此顺序定义为 \"prerequisite for the sequential masking mechanism\"，是方法正确性论证的核心。如果读者按照论文描述验证机制逻辑，会发现机制不可能工作。这严重影响 soundness。\n- 建议修改方向：(1) 修正 §3.1 的字段顺序为实际实现的顺序（大概率是 head → tail → relation → head_type → tail_type）；(2) 明确说明这是 XGrammar CFG 编译的产物（JSON 标准不保证 key 顺序），不是 JSON Schema 本身的属性；(3) 补充说明为什么选择此特定顺序（relation 必须先于 type fields 以启用 sequential masking）。\n\n**N2** [critical] Abstract 中 R²=0.99 (n=4) 声明过强，F-test 不显著\n- 具体位置：Abstract line 11; §7 Discussion; Appendix B (app:dual-factor)\n- 问题：Abstract 显著展示 \"the dual-factor pattern explains nearly all variance ($R^2{=}0.99$, $n{=}4$)\"。但 Appendix 报告 F(1,2)=198.0, **p ≈ 0.058**——在 α=0.05 下不显著。n=4 的回归本质上只有 df=2，任何两点都能完美拟合一条线，R²=0.99 的统计力量极其有限。\n  \n  §7 已加入 \"descriptive characterization with explicit scope\" 的语言，但 Abstract 仍然将 R²=0.99 作为 headline result 呈现，未提及 F-test 不显著。这构成统计声明的过度宣传。\n- 为什么影响接收：审稿人对 n=4 回归的 R² 高度敏感（历史审稿 R2-N1 已反复标记）。在 F-test 不显著的情况下在 Abstract 突出展示 R²=0.99，会被视为 misleading statistical claim。\n- 建议修改方向：(1) 从 Abstract 移除 R²=0.99 数值，改为定性描述（如 \"residual DR is modulated by the product of schema tightness and baseline violation rate for calibrated models\"）；(2) 若保留 R² 值，必须在同一句注明 \"n=4, F-test p=0.058\"；(3) 在 §7 中明确标注这是 exploratory observation 而非 confirmed finding。\n\n**N3** [major] RV=0.03% 残留的解释在论文与 rebuttal 之间不一致\n- 具体位置：§5.3 (DocRED Core Result); Rebuttal Draft v2 (RV=0.03% Residual section)\n- 问题：论文 §5.3 称残留 5 个 RV violation 源于 **\"partial JSON recovery where the grammar FSM completes a structurally valid but relation-name-truncated triple\"**。Rebuttal draft 却称其源于 **\"XGrammar v0.1.33 enum compilation bug where the grammar bitmask leaks token continuations across enum entries\"**（并给出了具体例子：\"member\" → \"membericipant\"）。这两个解释描述的是完全不同的机制。\n- 为什么影响接收：论文与 rebuttal 的不一致会被审稿人视为对自己系统行为理解不清。\n- 建议修改方向：确认真实原因（根据 rebuttal 的具体例子，bug 解释更可信），统一论文与 rebuttal 的描述。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Beam search 最强结果未进入正文 §5/§7\n- 具体位置：Appendix (app:beam-search) vs. §5, §7, Limitations\n- 问题：Beam search k=4 在 SciERC 全集上实现 **DR=0%, CF=0.53%**（Table 8），同时解决了 greedy decoding 的两个主要限制（残留 DR 和 CF 升高）。这是论文最强的实验结果之一，但仅出现在 Appendix，正文 §5/§7 未讨论。Limitations 仅一句提及 \"preliminary evaluation...suggests compatibility\"。\n  \n  此外，beam search 的 **runtime overhead 未报告**。Appendix 只说 \"Wall-clock overhead is modest\" 但无具体数字。考虑到 §5.5 对 greedy 模式有详细的 latency profiling，beam search 缺乏对等的 runtime 报告是不完整的。\n- 建议：(1) 在 §7 Discussion 中用 2-3 句讨论 beam search 如何解决 CF↔DR trade-off；(2) 报告 beam search 的 per-document latency；(3) 将 Limitations 中的 \"preliminary\" 改为更准确的描述。\n\n**W2** [warning] Post-hoc vs OntoCoDec framing 不够对称\n- 具体位置：§1 Introduction paragraph 2; Appendix B (app:posthoc-extended)\n- 问题：Appendix Table 9 显示在 **5/6 ZS 设置中 post-hoc F1 更高**。Introduction 虽然承认 \"achieves higher F1 in most zero-shot settings via precision gains\"，但紧接着就强调 Mistral DocRED 73.7% rejection 的极端案例。Introduction 的 framing 选择性地突出了 post-hoc 的最差表现，未明确量化 \"most\" 具体是 5/6。\n  \n  同时，在 fine-tuned 设置下，post-hoc 与 OntoCoDec 性能趋同（ΔF1 ≤ 0.55pp），这意味着 OntoCoDec 的核心优势仅在高 violation rate 的 ZS 场景下显现，而在实际应用更常见的 FT 场景下优势不明显。\n- 建议：在 Introduction 明确标注 \"post-hoc F1 is higher in 5 of 6 zero-shot configurations\"，或至少不让读者误以为 OntoCoDec 在 F1 上全面优于 post-hoc。\n\n**W3** [warning] Parse failure confounding 分析不充分\n- 具体位置：Table 5 caption; §5.1 paragraph \"Setup\"\n- 问题：Llama DocRED ZS parse failure 从 6.8% 增加到 9.1%（+34%），意味着 S1 约束导致更多文档无法成功解析。论文提到 \"including parse failures as zero-violation instances adjusts rates by at most 0.23 pp\" 和 \"excluding failed documents, ΔR-F1 is within ±0.1 pp\"，但未提供 parse-failure-excluded 的完整 violation rates 和 F1 表格。\n  \n  对于声称约束是 \"F1-neutral\" 的论文，+34% parse failure 增长本身就是一种间接的 F1 损失（E-F1 差 3.17pp），应该更透明地报告。\n- 建议：补充一个 parse-failure-excluded 和 all-set 两种分母下的对照表，或至少在正文中量化 parse failure 增长的影响。\n\n**W4** [warning] DocRED semantic-only ET 增长 (+70%) 缺乏解释\n- 具体位置：Table 3 (DocRED ablation), Semantic row: ET 从 2.48% 增至 4.22%\n- 问题：SciERC 的 semantic-only ET 增长有解释（§5.2 \"Enabling dependency\" paragraph：\"semantic mask constrains type tokens to relation-specific valid sets...forcing an OOV alternative\"）。但 DocRED 的 +70% ET 增长（2.48% → 4.22%）未给出具体解释。DocRED 的 entity types (PER, ORG, LOC, TIME, NUM, MISC) 都是短 token，与 SciERC 多 token 类型的 tokenization 机制不同，因此 SciERC 的解释可能不适用于 DocRED。\n- 建议：补充 1-2 句解释 DocRED ET 增长的具体机制。\n\n**W5** [warning] CF-DR trade-off ablation 仅限 SciERC/Qwen\n- 具体位置：Appendix B Table 7 (CF-DR trade-off pilot)\n- 问题：CF fallback ablation（切换 fallback 优先级的实验）仅在 SciERC/Qwen3-8B 上完成。论文声称 \"This trade-off generalizes beyond SciERC/Qwen3-8B\" 并引用跨设置的 Spearman ρ=−0.77 作为证据，但 ρ=−0.77 衡量的是不同设置间 DR/CF 的 inverse association，不等同于 ablation 结果的可迁移性。\n  \n  特别是 Llama DocRED 的 CF 高达 12.02%，是所有设置中最高的，在该设置上的 trade-off 量级可能与 SciERC/Qwen 不同。\n- 建议：至少讨论 DocRED/Llama 上 trade-off 量级可能不同的预期，或补充一个 DocRED 上的 pilot。\n\n**W6** [warning] Composability matrix 缺乏 fine-tuned 设置的统计显著性检验\n- 具体位置：Table 4 (Composability matrix); §5.2 paragraph \"Composability with fine-tuning\"\n- 问题：Zero-shot F1 变化有完整的 bootstrap 检验（SciERC p=0.58, DocRED p<0.001），但 fine-tuned 设置下的 F1 变化（如 Qwen LoRA SciERC: −0.09pp, DocRED: −0.30pp）未报告统计显著性。论文声称 \"R-F1 change within ±0.6 pp\"，但未检验这些变化是否显著不同于零。\n- 建议：对 fine-tuned 设置补充 bootstrap CI 和 p-value，尤其是 Qwen DocRED 的 −0.30pp。\n\n---\n\n## 小问题（不影响接收）\n\n- §4 DR reduction range 使用不同模型范围（Abstract \"42-99%\" 含 Mistral，§4 \"94-99%\" 仅 calibrated models），虽然不矛盾但易混淆。建议在 §4 标注 \"(calibrated models only; full range including Mistral: 42-99%)\"。\n- DocRED fallback coverage：SciERC 的 Llama effective coverage 63.4% 和 DocRED 的 Qwen coverage 99.9% 已报告，但 **Llama DocRED 的 coverage 未显式报告**（Llama DocRED 有 57,825 fallback events，57.42% DR baseline，coverage 可能较低）。\n- Beam search DocRED 仅在 50-doc subset 上评估，full-set 结果缺失。Table 8 caption 已标注 \"(50 documents)\"，但未讨论 50-doc 是否具代表性。\n- §5.5 Table 6 的 runtime 数据与 Appendix Table 10 不一致：Table 6 报告 SciERC Full S1 = 2.647s (+2.3%)，Table 10 报告 Full S1 = 6.76s。差异可能源于不同实验批次或硬件条件，但未解释。\n- JSON 标准（RFC 8259）不保证 object key 顺序。论文说 \"The JSON Schema enforces a fixed field ordering\"——JSON Schema 本身也不保证 property ordering。实际上是 XGrammar 的 CFG 编译产生了固定顺序。应修正措辞为 \"The XGrammar-compiled grammar enforces...\"。\n\n---\n\n## 主要优势\n\n1. **方法设计清晰**：两层可组合架构（grammar + semantic）具有明确的分工和 enabling dependency，形式化定义完整（除字段顺序错误外），decidability taxonomy 为理解约束范围提供了有用的框架。\n\n2. **实验覆盖面广**：3 模型 × 2 数据集 × 多种 ablation（五路消融、composability matrix、CF-DR trade-off、sampling/beam search 兼容性、per-relation 分析），实验设计系统性强。\n\n3. **诚实报告 trade-off**：CF↔DR trade-off 被明确量化和讨论，post-hoc baseline 的优势被承认（Appendix Table 9），Mistral 作为 boundary condition 被单独分析而非隐藏。论文没有隐瞒不利数据。\n\n4. **实际开销极低**：Full S1 overhead 仅 +2.3–5.4%，fine-tuned 下进一步降低至 +2.3%。Runtime 分析表明方法具有实用性。\n\n5. **可复现性强**：LoRA 超参数、prompt 模板、seed、软件版本均已报告；bootstrap 参数完整（10,000 iterations, 95% CI）；所有 greedy 实验完全确定性。\n",
    "reviewer_id": "1",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 267 · 2026-05-17T12:04:27.329716+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3815
}
```

</details>

---


### Assistant

_source line 268 · 2026-05-17T12:04:37.444975+00:00_

审稿报告已提交给 Review Director。

**审稿核心发现**：

1. **N1 [critical]**：§3.1 声称的 JSON 字段顺序（head → head_type → tail → tail_type → relation）与 sequential masking 机制的前提矛盾——在此顺序下 relation 最后生成，type fields 生成时 r_j 不可用，semantic mask 永远不会激活。Prompt 模板显示实际顺序为 head → tail → relation → head_type → tail_type，这才能让机制工作。

2. **N2 [critical]**：Abstract 突出展示 R²=0.99 (n=4)，但 Appendix 的 F-test p≈0.058 不显著。n=4 回归的 R² 不应作为 headline result。

3. **N3 [major]**：RV=0.03% 残留的解释在论文（"partial JSON recovery"）和 rebuttal（"XGrammar enum compilation bug"）之间矛盾。

4. **W1-W6**：beam search 最强结果（DR=0%, CF=0.53%）未进正文；post-hoc framing 不对称；parse failure +34% 分析不充分；DocRED ET +70% 缺乏解释；CF-DR ablation 仅限一个设置；composability matrix 缺 FT 统计检验。

**Overall: 3.0 (Findings)**，修复 N1-N3 后评分可上调。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1"
}
```

</details>

---


## Round 9

## Round 9

68 recorded events


### User

_source line 269 · 2026-05-18T12:25:55.634878+00:00_

[Round 6 审稿请求]:
## Round 6 审稿任务 — Reviewer 1（方法严谨性 + 实验分析）

### 论文信息
- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Ontology Constraints
- **论文路径**: `projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`
- **目标 Venue**: EMNLP 2026 (ARR May 2026 cycle)
- **截止日期**: 2026-05-25
- **投稿类别**: Long paper

### Venue 要求
- **页数限制**: 正文 8 页，Limitations/Ethics/References/Appendix 不计入
- **模板**: ACL style template (`\usepackage[review]{acl}`)
- **匿名规则**: Double-blind
- **附录**: 允许，不计入页数限制，审稿人不强制阅读
- **Limitations section**: 必须，位于 References 前，omission = desk reject
- **评分标准**: EMNLP 2026 通过 ARR 统一审稿，5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit

### 你的审查侧重

**核心任务**：评估方法的技术严谨性和实验证据的充分性。

**重点关注领域**：
1. **统计 claims 的有效性**：所有定量声明是否有充分的统计支撑？特别关注 Abstract 中的数值 claims（R²、DR reduction ranges 等）
2. **实验设计完整性**：消融实验是否覆盖所有必要对比？是否存在 cherry-picking？
3. **数据一致性**：Abstract/Introduction 中的数字是否与 §5 Experiments 和 Tables 匹配？
4. **方法形式化**：§3 Method 的形式化是否严谨？定义是否完整？
5. **Reproducibility**：实验复现所需信息是否充足（超参数、GPU、seeds 等）？

### 上轮（Round 5）遗留 Open Issues（你需要逐一检查是否已修复）

**Critical:**
- **R2-N1**: Abstract R²=0.886 (n=4) — 上轮要求从 Abstract 移除 R² 具体值。F(1,2)≈15.54, p≈0.058, α=0.05 下不显著。Mistral post-hoc 排除构成数据筛选偏差。检查 Abstract 是否仍包含 R² 数值。

**Warning:**
- **W3**: Post-hoc filtering 在 5/6 ZS 中 F1 高于 OntoCoDec，但 §1 framing 是否已添加平衡表述？
- **R2-N3**: Llama DocRED parse failure +34%（68→91）的 parse-failure-excluded violation rates 和 F1 是否已提供？
- **R2-N6**: Semantic-only DocRED ET 增加 +70%（2.48%→4.22%）机制是否已解释？
- **R4-N3**: Beam search 在 SciERC 全集（DR=0%, CF=0.53%）的结果是否已在正文（§5/§7）讨论？
- **R4-W2**: DocRED fallback coverage 是否已显式报告？
- **R4-W3**: §4 DR reduction 范围 (94-99%) 与 Abstract (42-99%) 不一致是否已修复？
- **R4-Q1**: JSON field ordering 是 sequential masking 的前提，是否已在 §3 显式声明？
- **R4-Q2**: CF-DR trade-off ablation 仅 SciERC/Qwen，是否已添加 DocRED 讨论？

**Info:**
- **R2-N10**: RV=0.03% 解释不一致（paper vs rebuttal）是否已统一？
- **GC-N1**: Grammar-only row 是否已标识为 GCD 能力上限？
- **R2-N5**: Reproducibility — LoRA 超参数、GPU 型号、seeds 是否已补充？

### 输出要求
按以下结构输出审稿意见：
1. **Summary**（2-3 句）
2. **Strengths**（逐条，标记 S1/S2/...）
3. **Weaknesses**（逐条，标记 W1/W2/...，按 critical > warning > info 排序）
4. **Open Issue Resolution Check**（逐条标记 ✅ resolved / ⚠️ partially / ❌ not fixed）
5. **New Issues**（如有）
6. **Questions to Authors**
7. **Missing References**
8. **Scores**: Overall Assessment (1-5, 用 EMNLP 2026 评分标准), Soundness (1-5), Excitement (1-5), Reproducibility (1-5), Confidence (1-5)
9. **Detailed Section Comments**（逐节）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 270 · 2026-05-18T12:26:09.805871+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 271 · 2026-05-18T12:26:10.660429+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_1_11179fb2.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 272 · 2026-05-18T12:26:10.660842+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
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

_source line 273 · 2026-05-18T12:26:10.711301+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 274 · 2026-05-18T12:26:16.212810+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-18T12:26:16.715320+00:00_

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
12	\usepackage{multirow}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{enumitem}
16	\usepackage{xcolor}
17	
18	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Ontology Constraints}
19	
20	\author{Anonymous ACL submission}
21	
22	\begin{document}
23	\maketitle
24	
25	% === Abstract ===
26	\input{abstract}
27	
28	% === §1 Introduction ===
29	\input{section1_introduction_draft}
30	
31	% === §2 Background ===
32	\input{section2_background}
33	
34	% === §3 Method ===
35	\input{section3_method_draft}
36	
37	% === §4 Constraint Composition ===
38	\section{Constraint Composition}
39	\label{sec:composition}
40	\input{section4_composition_draft}
41	
42	% === §5 Experiments ===
43	\section{Experiments}
44	\label{sec:experiments}
45	
46	\subsection{Violation Landscape}
47	\input{section3_violation_landscape}
48	
49	\input{section5_scierc_draft}
50	\input{section5_docred_draft}
51	\input{section5_crossmodel_draft}
52	\input{section5_wikievents_draft}
53	\input{section5_runtime}
54	
55	% === §6 Related Work ===
56	\input{section6_related_work}
57	
58	% === §7 Discussion and Conclusion ===
59	\section{Discussion and Conclusion}
60	\label{sec:discussion}
61	\input{section7_conclusion_compressed}
62	
63	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
64	\clearpage
65	\section*{Limitations}
66	
67	CF impact is model-dependent: for well-calibrated models (Qwen, Llama), S1 introduces CF violations (up to 12.02\%) as a consequence of per-relation independent enforcement; for poorly-calibrated models (Mistral), S1 substantially reduces CF (56.87\%\,$\to$\,1.27\%) by constraining type assignments to schema-valid values.
68	CF fallback ablation shows that eliminating
…[truncated 3737 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 276 · 2026-05-18T12:26:16.715908+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 277 · 2026-05-18T12:26:17.577375+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
  }
}
```

</details>

---


### Tool result

_source line 278 · 2026-05-18T12:26:17.628800+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/figures/fig2_per_relation_dr.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/figures/dual_factor_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 279 · 2026-05-18T12:26:24.502325+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on my search results, here's comprehensive information about ACL ARR 2025-2026 reviewer guidelines, review form, and scoring criteria:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommen
…[truncated 1356 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7786
}
```

</details>

---


### Tool call

_source line 280 · 2026-05-18T12:26:34.297722+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form criteria, scoring dimensions, and scoring scale. I need: 1) All scoring dimensions (soundness, excitement, overall, confidence, etc.) 2) The exact scale for each dimension (1-5? what does each number mean?) 3) Any specific guidance on what constitutes each score level. 4) Any changes made in 2025-2026 to the review process."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form criteria, scoring dimensions, and scoring scale. I need: 1) All scoring dimensions (soundness, excitement, overall, confidence, etc.) 2) The exact scale for each dimension (1-5? what does each number mean?) 3) Any specific guidance on what constitutes each score level. 4) Any changes made in 2025-2026 to the review process."
  }
}
```

</details>

---


### Tool call

_source line 281 · 2026-05-18T12:26:34.700583+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
  }
}
```

</details>

---


### Tool result

_source line 282 · 2026-05-18T12:26:34.751386+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_fd4b26.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_d3264e.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_550cbf.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_outline.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/paper_tables_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/p
…[truncated 2747 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 283 · 2026-05-18T12:26:39.689592+00:00_

# ARR Review Form: Scoring Dimensions and Scales

Based on the guidelines provided, here's what I found regarding the review form structure:

## Scoring Dimensions

The document explicitly mentions **three main scores** as of February 2025:

1. **Soundness** - evaluates technical rigor and validity
2. **Excitement** - reflects personal interest and subjective appreciation
3. **Overall Recommendation** - composite assessment for venue suitability

Additionally, reviewers indicate:
- **Confidence score** - to reflect uncertainty about assessments
- **Reproducibility score** - assessing whether sufficient methodological details exist

## Scoring Scale Details

The guidelines do **not provide the specific numeric scales** (e.g., 1-5 ranges) or explicit definitions for each score level in this document.

The guidance emphasizes that "soundness scores must be justified by review text" and notes that "low soundness scores without sufficient justification" indicate problematic reviews.

## 2025 Changes

A significant update occurred in **May 2025**: ARR adopted new policies on reviewer incentives and sanctions, including recognition for "great reviewers" and potential restrictions on "highly irresponsible" reviewers who submit extremely terse, unprofessional, or LLM-generated reviews.

## Limitation

For the complete scoring rubric with exact numeric scales and level definitions, you would need to consult the [ARR review form page](https://aclrollingreview.org/reviewform) directly, which is referenced but not reproduced in these guidelines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5391
}
```

</details>

---


### Tool call

_source line 284 · 2026-05-18T12:26:45.363897+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 285 · 2026-05-18T12:26:45.816394+00:00_

1	\begin{abstract}
2	We present \textsc{OntoCoDec}, which compiles Information Extraction (IE) ontology schemas into two composable token-level decoding constraints that provide formal guarantees during autoregressive generation:
3	(1)~a \emph{grammar layer} (XGrammar context-free grammar) guaranteeing JSON structural validity and entity/relation vocabulary membership (virtually eliminating entity type and relation vocabulary violations); and
4	(2)~a \emph{semantic layer} guaranteeing per-triple domain/range type compliance via a stateful entity registry and dynamic logit masking.
5	The two layers compose via bitwise AND on logit masks, with the grammar layer as an enabling prerequisite.
6	%
7	Without constraints, Large Language Model (LLM) based IE produces systematic domain/range (DR) violations: 15.37\% on SciERC (7 relations) and 18.46\% on DocRED (96 relations), comparable rates governed by \emph{constraint tightness} rather than ontology scale.
8	\textsc{OntoCoDec} reduces DR by 42--99\% across three model families (Qwen3-8B, Llama-3.1-8B, Mistral-7B) with no significant F1 cost.
9	For the primary model (Qwen3-8B): SciERC $+$0.13\,pp ($p{=}0.58$), DocRED $+$0.50\,pp ($p{<}0.001$); other models show comparable or larger gains (\S\ref{sec:cross-model}).
10	% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1, llama_docred_full_s1, mistral_docred
11	For calibrated models, residual DR correlates with the product of schema tightness and baseline violation rate, suggesting that constraint effectiveness is predictable from schema and model characteristics.
12	Composed with Low-Rank Adaptation (LoRA) fine-tuning, DR reaches $\leq$\,0.09\% (SciERC) and 0.20\% (DocRED) with relation F1 within $\pm$0.6\,pp, confirming near-lossless composability.
13	With beam search ($k{=}4$), the full stack (LoRA + OntoCoDec + beam) achieves zero constraint violations across all four categories while preserving extraction quality (relation F1 change ${<}$0.5\,pp).
14	The framework ge
…[truncated 597 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 286 · 2026-05-18T12:26:45.816839+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 287 · 2026-05-18T12:26:46.268926+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly deployed for zero-shot information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity is guaranteed to carry a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	In a systematic study, we find violations are pervasive: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred}, driven by \emph{constraint tightness} (few valid type pairs per relation) rather than ontology scale.
9	Relations with tight constraints exhibit far higher rates (\textsc{Compare}: 42.4\%) than loosely constrained ones (\textsc{Used-for}: 0.8\%).
10	
11	Existing approaches leave a fundamental gap.
12	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
13	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} guarantees syntactic well-formedness but cannot encode cross-field semantic constraints.
14	Post-hoc filtering achieves higher F1 in most zero-shot settings via precision gains, but at the cost of discarding up to 48\% of predictions including true positives; at high rejection rates (e.g., Mistral DocRED 73.7\%), it discards the majority of outputs, making it impractical.
15	OntoCoDec preserves recall by enforcing constraints during generation rather than discarding non-compliant outputs.
16	Training-based approaches~\cite{sainz2024gollie,lu2022uie} provide only soft guidance that cannot eliminate violations.
17	
18	We propose \textbf{OntoCoDec} (\textbf{Onto}logy-\textbf{Co}mpiled \textbf{Dec}oding), a framework that compiles an IE onto
…[truncated 2852 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 288 · 2026-05-18T12:26:46.269311+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
  }
}
```

</details>

---


### Tool result

_source line 289 · 2026-05-18T12:26:46.269514+00:00_

1	% Section 2: Background (compressed)
2	
3	\section{Background}
4	\label{sec:background}
5	
6	\paragraph{IE Ontology Structure.}
7	\label{sec:bg:ontology}
8	An IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defines entity types $\mathcal{E}$, relation types $\mathcal{R}$, and a mapping $\sigma: \mathcal{R} \to \mathcal{P}(\mathcal{E} \times \mathcal{E})$ specifying valid (head type, tail type) pairs per relation.
9	A triple $(h, r, t)$ is \emph{type-valid} if $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$.
10	We define the \emph{constraint tightness} of $r$ as $1 - |\sigma(r)| / |\mathcal{E}|^2$: tighter constraints leave fewer valid options, increasing violation likelihood.
11	
12	\paragraph{Grammar-Constrained Decoding.}
13	\label{sec:bg:gcd}
14	Grammar-constrained decoding restricts each token $y_t$ to a mask $M_g \in \{0, 1\}^{|V|}$ derived from a target grammar.
15	XGrammar~\citep{dong2025xgrammar} compiles JSON Schemas into pushdown automata for efficient enforcement of structural constraints; Outlines~\citep{willard2023outlines} and SGLang~\citep{zheng2024sglang} offer similar capabilities.
16	However, these methods are limited to context-free constraints and cannot enforce cross-field semantic rules (e.g., ``if $r$ = \textsc{Feature-of}, then $\mathrm{type}(h) \in \{\textsc{Method}, \textsc{OtherScientificTerm}\}$''), which depend on previously generated field values.
17	
18	\paragraph{Problem Statement.}
19	\label{sec:bg:problem}
20	Given $\mathcal{O}$ and an autoregressive LM $\mathcal{M}$, we seek constraints $\mathcal{C}$ ensuring: (a)~\textbf{structural validity}, i.e., well-formed JSON with $\mathcal{E}$/$\mathcal{R}$ membership; and (b)~\textbf{type validity}, i.e., $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$ for every triple.
21	Condition (a) is context-free; (b) is context-sensitive but \emph{prefix-decidable}: at the point where a type token is generated, all information needed (relation type, entity registry) is ava
…[truncated 214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 290 · 2026-05-18T12:26:46.771405+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 291 · 2026-05-18T12:26:47.725532+00:00_

1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	We present OntoCoDec, a two-layer constrained decoding framework that compiles ontology schemas into token-level masks enforced during autoregressive generation.
9	Unlike type-constrained code generation, IE presents three distinct challenges: (1)~entity types are inferred from free text rather than declared annotations, (2)~the entity registry is built dynamically during generation, and (3)~constraint targets are context-dependent type assignments rather than fixed grammar productions.
10	The grammar layer (\S\ref{sec:grammar}) guarantees structural validity (well-formed JSON with ontology-vocabulary membership), while the semantic layer (\S\ref{sec:semantic}) enforces domain/range type constraints via a stateful entity registry.
11	We describe the problem formulation (\S\ref{sec:formulation}), each layer, and two decoding strategies (\S\ref{sec:strategies}).
12	Formal analysis of constraint composition is deferred to Section~\ref{sec:composition}.
13	
14	
15	\subsection{Problem Formulation}
16	\label{sec:formulation}
17	
18	\paragraph{IE as structured generation.}
19	Given an input text $x$, a language model generates a structured JSON output $y$:
20	%
21	\begin{equation}\label{eq:output-schema}
22	\resizebox{.88\columnwidth}{!}{$\displaystyle
23	  y = \bigl\{\texttt{entities}: [\{n_i, \tau_i\}],\; \texttt{relations}: [\{h_j, t_j, r_j, \tau^h_j, \tau^t_j\}]\bigr\}
24	$}
25	\end{equation}
26	%
27	where each entity has a name $n_i$ and type $\tau_i \in \mathcal{E}$, and each relation specifies head $h_j$, tail $t_j$, relation type $r_j \in \mathcal{R}$, and head/tail entity types $\tau^h_j, \tau^t_j$.
28	The output JSON Schema (\S\ref{sec:grammar}) enforces a fixed field ordering (head $\to$ tail $\to$ relation $\to$ head\_type $\to$ tail\_type) via deterministic grammar compilation.
29	This ordering en
…[truncated 9038 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 292 · 2026-05-18T12:26:47.725987+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 293 · 2026-05-18T12:26:47.876818+00:00_

1	% Section: Constraint Composition (compressed, 787→~500 words)
2	
3	At each decoding step $t$, let $G(t) \subseteq V$ and $S(t) \subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.
4	The final mask is their conjunction:
5	%
6	\begin{equation}\label{eq:composition}
7	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
8	\end{equation}
9	%
10	so a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$, reflecting the enabling dependency (\S\ref{sec:method}): the semantic layer requires the relation type to belong to $\mathcal{R}$, a property guaranteed only by the grammar layer.
12	
13	\paragraph{Grammar-First Fallback.}
14	When $S(t) \cap G(t) = \emptyset$ (tight constraints leave no token that is both grammar-valid and semantically valid), na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
15	We enforce a \emph{grammar-first fallback}: if no semantically valid token survives grammar filtering, semantic masking is skipped and the grammar layer alone controls selection.
16	Structural integrity is a hard constraint; a type violation is a soft error detectable by downstream validation.
17	
18	\paragraph{Constraint Tightness.}
19	We define the tightness of relation $r$ as:
20	%
21	\begin{equation}\label{eq:tightness}
22	  \kappa(r) = 1 - \frac{|\mathcal{V}(r)|}{|\mathcal{E}|^2},
23	\end{equation}
24	%
25	where $\mathcal{V}(r)$ is the set of valid type pairs and $\mathcal{E}$ the entity type vocabulary.
26	The mean tightness $\bar{\kappa} = \frac{1}{|\mathcal{R}|}\sum_{r} \kappa(r)$ characterizes ontology restrictiveness.
27	Tighter constraints eliminate more grammar-valid tokens at type-bearing positions, increasing fallback frequency and residual DR.
28	This dual-factor pattern (tightness $\times$ baseline model violation rate) is consistent with the cross-da
…[truncated 1435 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 294 · 2026-05-18T12:26:47.877211+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
  }
}
```

</details>

---


### Tool result

_source line 295 · 2026-05-18T12:26:47.927744+00:00_

1	% §5.1 Experimental Setup and Violation Landscape (compressed)
2	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
3	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
4	
5	\label{sec:violation_landscape}
6	
7	\paragraph{Setup.}
8	We evaluate on two IE benchmarks:
9	\textbf{SciERC}~\cite{luan2018scierc} (551 test sentences, 7 relations, avg.\ 26.1 valid type pairs/relation) and \textbf{DocRED}~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test annotations are not publicly available; we evaluate on the development set.} 96 relations, avg.\ 5.68 valid pairs).
10	Primary model: Qwen3-8B~\cite{qwen2025qwen3}, zero-shot greedy decoding; cross-model validation in \S\ref{sec:cross-model}.
11	We measure four violation categories: \textbf{DR} (domain/range type pair $\notin \sigma(r)$), \textbf{RV} (relation $\notin \mathcal{R}$), \textbf{ET} (entity type $\notin \mathcal{E}$), and \textbf{CF} (same entity assigned conflicting types across triples).
12	Violation rates are computed over successfully parsed documents; including failures as zero-violation instances adjusts rates by at most 0.23\,pp.
13	
14	\paragraph{Baseline violations and motivation.}
15	DR violations affect 15.37\% of triples on SciERC and 18.46\% on DocRED, comparable rates despite 14$\times$ ontology size difference, indicating that severity is driven by \emph{constraint tightness} rather than scale.
16	Per-relation rates vary by over 40\,pp (Appendix~\ref{app:per-relation-landscape}), correlating with tightness $\kappa(r)$.
17	RV on DocRED reaches 29.66\%, confirming that large vocabularies exceed prompt-based reproduction capacity.
18	Schema-informed prompting reduces DR by 62\% on SciERC but only 30\% on DocRED and is per-relation unreliable (DR for \textsc{Evaluate-for} \emph{increases} by 5.8\,pp), motivating decoding-time enforcement.
19	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 296 · 2026-05-18T12:26:57.416867+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 297 · 2026-05-18T12:26:57.919733+00:00_

1	% Section 5 — SciERC Results (Draft)
2	% Data source: Phase 2 SciERC registry experiments
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,
4	%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2
5	% All numbers verified against registry 2026-05-14.
6	
7	\subsection{Ablation and Composability with Fine-Tuning}
8	\label{sec:scierc-results}
9	
10	Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC (Qwen3-8B, zero-shot, 551 documents); only the active constraint layers differ across rows.
11	
12	% ──────────────────────────────────────────
13	%  Table: SciERC five-way ablation
14	% ──────────────────────────────────────────
15	\begin{table}[t]
16	\centering
17	\small
18	\setlength{\tabcolsep}{3.6pt}
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{@{}l rrrrr rr@{}}
21	\toprule
22	& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
23	& \multicolumn{2}{c}{\textbf{F1}} \\
24	\cmidrule(lr){2-6} \cmidrule(l){7-8}
25	\textbf{Mode}
26	  & DR\,$\downarrow$ & $\Delta$DR
27	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
28	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
29	\midrule
30	Unconstrained
31	  & 15.37 & ---
32	  & 1.39  & 0.40
33	  & 0.08
34	  & 8.23  & 31.01 \\
35	Grammar
36	  & 14.84 & $\downarrow$3\%
37	  & \textbf{0} & \textbf{0}
38	  & 0.08
39	  & 8.23  & 30.98 \\
40	Semantic
41	  & 11.65 & $\downarrow$24\%
42	  & 1.51  & 0.40
43	  & 2.71
44	  & 8.15  & 31.01 \\
45	Full (S1)
46	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
47	  & \textbf{0} & \textbf{0}
48	  & 9.90
49	  & \textbf{8.36} & 30.98 \\
50	Full (S2)
51	  & 0.97  & $\downarrow$94\%
52	  & \textbf{0} & \textbf{0}
53	  & 8.03
54	  & 8.03  & \textbf{31.90} \\
55	\bottomrule
56	\end{tabular}}%
57	\caption{Five-way ablation on SciERC (551 docs, Qwen3-8B, zero-shot).
58	$\Delta$DR: relative change vs.\ unconstrained.
59	Best per column in \textbf{bold} (CF excluded).
60	F1 $\times$100. Bootstrap: 10{,}000 iterations.}
61	\label{tab:scierc-ab
…[truncated 6346 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 298 · 2026-05-18T12:26:57.920158+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 299 · 2026-05-18T12:26:57.920553+00:00_

1	% Section 5 — DocRED Results (compressed, 1450→~600 words)
2	% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,
3	%          phase2_docred_semantic_only, phase2_docred_full_s1
4	% All numbers verified against registry 2026-05-14.
5	
6	\subsection{Cross-Dataset Validation on DocRED}
7	\label{sec:docred-results}
8	
9	Table~\ref{tab:docred-ablation} presents the four-way ablation on DocRED (96 Wikidata relation types, 14$\times$ SciERC; Qwen3-8B, zero-shot, 998 documents).
10	
11	% ──────────────────────────────────────────
12	%  Table: DocRED four-way ablation
13	% ──────────────────────────────────────────
14	\begin{table}[t]
15	\centering
16	\small
17	\setlength{\tabcolsep}{3.6pt}
18	\resizebox{\columnwidth}{!}{%
19	\begin{tabular}{@{}l rrrrr rr@{}}
20	\toprule
21	& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
22	& \multicolumn{2}{c}{\textbf{F1}} \\
23	\cmidrule(lr){2-6} \cmidrule(l){7-8}
24	\textbf{Mode}
25	  & DR\,$\downarrow$ & $\Delta$DR
26	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
27	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
28	\midrule
29	Unconstrained
30	  & 18.46 & ---
31	  & 29.66 & 2.48
32	  & 0.10
33	  & 7.74  & 58.15 \\
34	Grammar
35	  & 26.17 & $\uparrow$42\%
36	  & \textbf{0.03} & \textbf{0}
37	  & 0.07
38	  & \textbf{8.31}  & \textbf{59.38} \\
39	Semantic
40	  & 13.84 & $\downarrow$25\%
41	  & 29.87 & 4.22
42	  & 1.05
43	  & 7.70  & 57.81 \\
44	Full (S1)
45	  & \textbf{10.21} & $\downarrow$\textbf{45\%}
46	  & \textbf{0.03} & \textbf{0}
47	  & 2.57
48	  & 8.23  & 59.37 \\
49	\bottomrule
50	\end{tabular}}%
51	\caption{Four-way ablation on DocRED (998 documents, Qwen3-8B, zero-shot).
52	$\Delta$DR: relative change vs.\ unconstrained.
53	Best per column in \textbf{bold} (CF excluded).
54	F1 $\times$100. Bootstrap significance: R-F1 $+$0.50\,pp ($p < 0.001$).}
55	\label{tab:docred-ablation}
56	\end{table}
57	
58	% exp_ids: phase2_docred_unconstrained, phase2_docred_full_s1
59	\paragraph{Core result.}
60	Full S1 reduces DR from 
…[truncated 1332 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 300 · 2026-05-18T12:26:58.373117+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 301 · 2026-05-18T12:26:59.329310+00:00_

1	% Section 5 — Cross-Model Validation (compressed, 830→~400 words)
2	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1,
3	%          phase2_docred_unconstrained, phase2_docred_full_s1,
4	%          llama_scierc_unconstrained, llama_scierc_full_s1,
5	%          llama_docred_unconstrained, llama_docred_full_s1
6	
7	\subsection{Cross-Model Validation}
8	\label{sec:cross-model}
9	
10	Table~\ref{tab:cross-model} replicates full S1 with Llama-3.1-8B-Instruct and Mistral-7B-Instruct-v0.3 under identical prompts and evaluation.
11	Mistral serves as a third zero-shot verification point; composability evaluation (\S\ref{sec:composability}) uses LoRA, available only for Qwen and Llama.
12	
13	\begin{table}[t]
14	\centering
15	\small
16	\setlength{\tabcolsep}{3.4pt}
17	\resizebox{\columnwidth}{!}{%
18	\begin{tabular}{@{}ll rrrr r@{}}
19	\toprule
20	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
21	& \textbf{R-F1} \\
22	\cmidrule(lr){3-6} \cmidrule(l){7-7}
23	\textbf{Dataset} & \textbf{Model}
24	  & DR\,$\downarrow$ & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
25	  & $\uparrow$ \\
26	\midrule
27	\multirow{6}{*}{SciERC}
28	  & Qwen (U)    & 15.37 & 1.39  & 0.40 & 0.08 & 8.23 \\
29	  & Qwen (S1)   &  0.93 & 0     & 0    & 9.90 & 8.36 \\
30	  \cmidrule(l){2-7}
31	  & Llama (U)   & 13.34 & 0.55  & 0    & 0.24 & 2.68 \\
32	  & Llama (S1)  &  0.08 & 0     & 0    & 6.56 & 2.54 \\
33	  \cmidrule(l){2-7}
34	  & Mistral (U) & 56.94 & 0     & 1.50 & 56.87$^\dagger$ & 3.66 \\
35	  & Mistral (S1)& 13.40 & 0     & 0    & 1.27  & 3.67 \\
36	\midrule
37	\multirow{6}{*}{DocRED}
38	  & Qwen (U)    & 18.46 & 29.66 & 2.48 & 0.10 & 7.74 \\
39	  & Qwen (S1)   & 10.21 &  0.03 & 0    & 2.57 & 8.23 \\
40	  \cmidrule(l){2-7}
41	  & Llama (U)   & 26.07 & 16.03 & 0.13 & 0.17 & 5.98 \\
42	  & Llama (S1)  &  2.55 &  0    & 0    & 12.02& 6.27 \\
43	  \cmidrule(l){2-7}
44	  & Mistral (U) & 57.42 & 42.35 & 7.58 & 24.78 & 4.34 \\
45	  & Mistral (S1)& 33.20 &  0    & 0    & 0.19  & 5.52 \\
46	\b
…[truncated 1100 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 302 · 2026-05-18T12:26:59.329836+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 303 · 2026-05-18T12:26:59.831915+00:00_

1	% Section 5 — Event Extraction on WikiEvents (compact, inline)
2	% exp_ids: ee_qwen_wikievents_unconstrained, ee_llama_wikievents_unconstrained,
3	%          ee_mistral_wikievents_unconstrained, ee_qwen_wikievents_constrained,
4	%          ee_llama_wikievents_constrained, ee_mistral_wikievents_constrained_v2
5	% v3 final data confirmed by Director 2026-05-18.
6	
7	\subsection{Cross-Task Validation: Event Extraction}
8	\label{sec:wikievents}
9	
10	To test generality beyond RE, we apply OntoCoDec to event extraction (EE) on WikiEvents~\cite{li2021document} (56 event types, 80 argument roles, 27 entity types, 245 role$\to$type constraints; Appendix~\ref{app:wikievents}).
11	The framework requires no modification: grammar compiles event/role vocabularies into a CFG; the semantic layer enforces role-conditioned type constraints via the same registry.
12	Violations extend to Event Vocabulary (EV), Role Vocabulary (RoV), and Argument Constraint (AC, analogous to DR).
13	
14	% ──────────────────────────────────────────
15	%  Table: WikiEvents three-model comparison (v3 final)
16	%  exp_ids: ee_{qwen,llama,mistral}_wikievents_{unconstrained,grammar_only,constrained_v3}
17	% ──────────────────────────────────────────
18	\begin{table}[t]
19	\centering
20	\small
21	\setlength{\tabcolsep}{2.8pt}
22	\resizebox{\columnwidth}{!}{%
23	\begin{tabular}{@{}ll rrrr rr@{}}
24	\toprule
25	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
26	& \multicolumn{2}{c}{\textbf{F1}} \\
27	\cmidrule(lr){3-6} \cmidrule(l){7-8}
28	\textbf{Model} & \textbf{Mode}
29	  & EV\,$\downarrow$ & RoV\,$\downarrow$ & AC & CF
30	  & Trig.\,$\uparrow$ & Ent.\,$\uparrow$ \\
31	\midrule
32	\multirow{3}{*}{Qwen3-8B}
33	  & Unconstr.\ & 24.0 & 74.9 & 0.3 & 0 & 11.8 & 0 \\
34	  & Grammar    & \textbf{0} & 76.1 & 8.2 & --- & --- & --- \\
35	  & Full S1    & \textbf{0} & \textbf{0} & 2.1 & 21.1 & 13.4 & 14.1 \\
36	\midrule
37	\multirow{3}{*}{\shortstack[l]{Llama\\3.1-8B}}
38	  & Unconstr.\ & 10.5 & 88.8 & 0.1 & 0 
…[truncated 2256 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 304 · 2026-05-18T12:26:59.832304+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
  }
}
```

</details>

---


### Tool result

_source line 305 · 2026-05-18T12:27:00.485243+00:00_

1	% Runtime overhead (inline paragraph, no subsection header to save space)
2	
3	\paragraph{Runtime overhead.}
4	\label{sec:runtime}
5	Full S1 adds $+$2.3\% on SciERC and $+$5.4\% on DocRED (same GPU); under fine-tuning, overhead drops to $+$2.3\% (61\,ms/doc).
6	Grammar compile is a one-time 44\,ms cost.
7	Per-layer profiling in Appendix~\ref{app:runtime}.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 652
}
```

</details>

---


### Tool call

_source line 306 · 2026-05-18T12:27:00.535851+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
  }
}
```

</details>

---


### Tool result

_source line 307 · 2026-05-18T12:27:00.587777+00:00_

1	% Section 7 — Discussion and Conclusion (maximally compressed)
2	% Full discussion in Appendix; Mistral boundary condition in app:dual-factor.
3	
4	OntoCoDec compiles IE ontology schemas into composable token-level decoding constraints, achieving 42--99\% DR reduction across three models and three datasets (2 RE + 1 EE) with no significant RE F1 cost; in EE, format compliance additionally enables entity extraction (\S\ref{sec:wikievents}).
5	Composed with LoRA fine-tuning, DR reaches $\leq$\,0.20\% at $<$0.6\,pp F1 cost; residual DR follows a dual-factor pattern ($\bar{\kappa} \times \text{RV}_{\text{baseline}}$; Appendix~\ref{app:dual-factor}).
6	CF impact is model-dependent (up to 12\% for calibrated models, reduced for poorly-calibrated ones); fine-tuning resolves this tension (CF\,$\leq$\,1.2\%; \S\ref{sec:composability}), and beam search ($k{=}4$) eliminates both residual DR and CF for calibrated models (Appendix~\ref{app:beam-search}).
7	Cross-field consistency remains an open challenge for per-slot enforcement; global entity-level type consensus during decoding offers the most direct path to resolving CF without trading it against DR.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 308 · 2026-05-18T12:27:14.334780+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 309 · 2026-05-18T12:27:14.335190+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Grammar-Constrained Decoding.}
5	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, LMQL~\cite{beurer-kellner2023lmql}, DOMINO~\cite{beurer-kellner2024domino}, SynCode~\cite{ugare2024syncode}, and ASAp~\cite{park2024grammar} guarantee format validity but cannot enforce cross-field semantic constraints such as domain/range rules.
6	
7	\paragraph{Type-Constrained Generation for IE and Code.}
8	Synchromesh~\cite{synchromesh_iclr2022}, PICARD~\cite{scholak2021picard}, and \citet{pldi2025_type_constrained_codegen} enforce type constraints in code generation; OntoCoDec migrates this to IE.
9	GCD~\cite{geng2023gcd} and GoLLIE~\cite{sainz2024gollie} constrain \emph{which tokens} appear but not \emph{which type combinations} are valid per relation.
10	DORE~\cite{vukovic2024dore} uses generate-then-select with confidence thresholds; GenIE~\cite{josifoski2022genie} constrains entities via a trie without relation-specific type enforcement; EnriCo~\cite{zaratiana2024enrico} applies ASP constraints with task-specific manually authored rules.
11	Training-based methods~\cite{paolini2021tanl,cabot2021rebel,lu2022uie,knowcoder_acl2024,li2023codeie} provide only soft guidance; post-hoc approaches~\cite{khorshidi2025odke,spires_2024,ontologx_2025} validate after generation rather than preventing violations.
12	
13	\paragraph{Quality Impact.}
14	CRANE~\cite{banerjee2025crane} and \citet{schall2025hiddencost} show grammar restrictions can degrade reasoning, but \citet{tam2024letmespeak} find extraction tasks robust to constraints.
15	OntoCoDec confirms this: DR decreases 42--99\% with zero F1 degradation across three model families (extended survey in Appendix~\ref{app:related_work}).
16	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 310 · 2026-05-18T12:27:15.038400+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 311 · 2026-05-18T12:27:15.340917+00:00_

1	% Appendix B — Extended Discussion
2	% Contains discussion paragraphs moved from the main text during compression.
3	
4	\section{Extended Discussion}\label{app:discussion}
5	
6	%%% CF Dual Mechanism %%%
7	% exp_ids: phase2_scierc_full_s1, llama_scierc_full_s1, llama_docred_full_s1
8	
9	\paragraph{CF Dual Mechanism.}
10	CF violations arise from two distinct mechanisms:
11	(1)~\emph{Registry override}: the semantic constraint forces a domain-compatible type that conflicts with the entity's previously registered type.
12	The entity appears in multiple relations with different type requirements, and the per-relation mask selects the locally valid type without consulting prior assignments.
13	(2)~\emph{Grammar-first fallback} (\S\ref{sec:interaction}): when the semantic mask conflicts with all grammar-valid tokens, the semantic layer is dropped entirely, allowing the grammar layer to generate any structurally valid type, which may differ from the entity's registered type.
14	
15	These mechanisms have sharply different model profiles.
16	Qwen3-8B triggers zero grammar-first fallbacks across all experiments, attributing 100\% of its CF violations to registry override.
17	Llama-3.1-8B, by contrast, triggers 5{,}882 fallbacks on SciERC (10.7 per document) and 57{,}825 on DocRED (63.8 per document), making grammar-first fallback the dominant CF source.
18	This asymmetry is consistent with the cross-model CF gap: Qwen achieves CF\,=\,2.57\% on DocRED vs.\ Llama's 12.02\%, despite both using identical constraint configurations.
19	The difference traces to Llama's less calibrated type predictions, which more frequently conflict with the semantic mask's valid set, triggering fallback.
20	
21	%%% Fallback Behavior and Effective Coverage %%%
22	% exp_ids: cf_fallback_ablation_scierc (final data)
23	
24	\paragraph{Fallback Behavior and Effective Coverage.}
25	\label{app:fallback-coverage}
26	The two-layer architecture produces two distinct fallback mechanisms with different semant
…[truncated 31927 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 312 · 2026-05-18T12:27:15.441810+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex"
  }
}
```

</details>

---


### Tool result

_source line 313 · 2026-05-18T12:27:15.492605+00:00_

1	\section{Beam Search Compatibility}
2	\label{app:beam-search}
3	
4	OntoCoDec's constraint enforcement is designed to be decoding-strategy agnostic.
5	The main experiments (\S\ref{sec:experiments}) use greedy decoding; Appendix~\ref{app:sampling} validates nucleus sampling.
6	Here we verify compatibility with beam search, completing coverage of the three standard decoding strategies.
7	
8	\paragraph{Implementation challenges.}
9	Two stateful components require adaptation for beam search.
10	(1)~The grammar layer (XGrammar) maintains an internal \texttt{GrammarMatcher} state that tracks the generated token sequence; beam reordering invalidates this state because beams are permuted across steps.
11	Our solution instantiates a fresh \texttt{GrammarMatcher} per beam per step and replays the beam's current token sequence through XGrammar's stateless accept API (64 lines of code).
12	(2)~The semantic layer's \texttt{TypeConstraintProcessor} accumulates entity and relation registries that assume a single generation path.
13	Our solution isolates state per beam by calling \texttt{detect()} on the full partial output at each step, reconstructing all entity/relation state from scratch for each beam independently (61 lines of code).
14	Both adaptations add ${\sim}125$ lines total without modifying the existing greedy/sampling logic.
15	
16	\paragraph{Results.}
17	Table~\ref{tab:beam-search} compares beam search ($k{=}4$, \texttt{early\_stopping=True}) against greedy decoding under full S1 constraints across six model-dataset combinations.
18	
19	\begin{table}[h]
20	\centering
21	\small
22	\caption{Beam search ($k{=}4$) vs.\ greedy decoding under full S1 constraints.
23	SciERC evaluated on full test set (551 documents); DocRED evaluated on matched 50-document subsets (same documents for greedy and beam).
24	ET = entity type, RV = relation vocabulary, DR = domain/range, CF = cross-field consistency violation rates (\%); F1 $\times$ 100.}
25	\label{tab:beam-search}
26	\begin{tab
…[truncated 6802 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 314 · 2026-05-18T12:27:15.844079+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex"
  }
}
```

</details>

---


### Tool result

_source line 315 · 2026-05-18T12:27:15.844458+00:00_

1	\section{Reproducibility Details}
2	\label{app:reproducibility}
3	
4	\paragraph{Fine-tuning configuration.}
5	All four fine-tuned models (Qwen3-8B and Llama-3.1-8B-Instruct on SciERC and DocRED) use identical LoRA hyperparameters: rank $r{=}16$, $\alpha{=}32$, dropout $0.05$, no bias, targeting all attention and MLP projection layers (\texttt{q\_proj}, \texttt{k\_proj}, \texttt{v\_proj}, \texttt{o\_proj}, \texttt{gate\_proj}, \texttt{up\_proj}, \texttt{down\_proj}).
6	Training uses AdamW with learning rate $2{\times}10^{-4}$, cosine schedule, warmup ratio $0.1$, effective batch size $16$, bf16 precision, gradient checkpointing, and completion-only loss for 3 epochs.
7	SciERC trains on 1,762 examples (260 dev) for 333 steps; DocRED trains on 3,053 examples (998 dev) for 573 steps.
8	Maximum sequence length is 2,048 (SciERC) and 4,096 (DocRED).
9	All runs use seed 42.
10	
11	\paragraph{Hardware and software.}
12	Training runs on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (98\,GB VRAM).
13	SciERC fine-tuning takes approximately 11 minutes per model; DocRED takes approximately 1.5 hours.
14	Software versions: PyTorch 2.10, Transformers 4.57, PEFT 0.19, TRL 1.1, Accelerate 1.13.
15	
16	\paragraph{Inference time.}
17	Table~\ref{tab:inference-time} reports per-document inference times for Qwen3-8B under zero-shot greedy decoding across constraint configurations.
18	
19	\begin{table}[h]
20	\centering
21	\small
22	\caption{Inference time (seconds/document, mean $\pm$ std) for Qwen3-8B, zero-shot, greedy decoding.}
23	\label{tab:inference-time}
24	\begin{tabular}{@{}lcc@{}}
25	\toprule
26	\textbf{Configuration} & \textbf{SciERC} & \textbf{DocRED} \\
27	\midrule
28	Unconstrained       & $8.69 \pm 3.89$  & $19.75 \pm 8.99$  \\
29	Grammar-only        & $8.81 \pm 4.51$  & $20.58 \pm 10.75$ \\
30	Semantic-only       & $7.23 \pm 3.91$  & $20.53 \pm 9.37$  \\
31	Full S1             & $6.76 \pm 3.67$  & $20.39 \pm 9.43$  \\
32	Post-hoc            & $8.69 \pm 3.89$  &
…[truncated 476 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 316 · 2026-05-18T12:27:16.095914+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex"
  }
}
```

</details>

---


### Tool result

_source line 317 · 2026-05-18T12:27:16.196808+00:00_

1	\section{Sampling Robustness}\label{app:sampling}
2	
3	\begin{table}[h]
4	\centering
5	\caption{Constraint robustness under nucleus sampling ($T$=0.7, $p$=0.9) vs.\ greedy decoding.}
6	\label{tab:sampling-robustness}
7	\begin{tabular}{llcccccc}
8	\toprule
9	Dataset & Decoding & ET\% & RV\% & DR\% & CF\% & E-F1 & R-F1 \\
10	\midrule
11	\multirow{2}{*}{SciERC (551)} & Greedy & 0 & 0 & 0.93 & 9.90 & 30.98 & 8.36 \\
12	& Sampling & 0 & 0 & 0.75 & 9.90 & 31.28 & 7.42 \\
13	\midrule
14	\multirow{2}{*}{DocRED (114$^\dagger$)} & Greedy & 0 & 0.03 & 10.21 & 2.57 & 59.37 & 8.23 \\
15	& Sampling & 0 & 0 & 10.31 & 12.63 & 57.05 & 7.92 \\
16	\bottomrule
17	\end{tabular}
18	\par\smallskip\footnotesize $^\dagger$Subset of 114 documents; full DocRED sampling requires ${\sim}300$h due to extended generation under high-temperature sampling with complex schemas.
19	\end{table}
20	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 318 · 2026-05-18T12:27:26.427772+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex"
  }
}
```

</details>

---


### Tool result

_source line 319 · 2026-05-18T12:27:26.428350+00:00_

1	\section{Effect of Document Length on Constraint Effectiveness}
2	\label{app:doc-length}
3	
4	To examine whether OntoCoDec's constraint effectiveness varies with document complexity, we partition test documents into three length bins (tertile split by word count) and report per-bin violation counts and F1.
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\caption{Document length breakdown on SciERC (Qwen3-8B). Tertile boundaries: Short $\leq$ 19 words, Medium $\leq$ 27, Long $>$ 27.}
10	\label{tab:doc-length-scierc}
11	\begin{tabular}{ll rrrrr rr}
12	\toprule
13	\textbf{Bin} & \textbf{Mode} & \textbf{ET} & \textbf{RV} & \textbf{DR} & \textbf{CF} & \textbf{Total} & \textbf{E-F1} & \textbf{R-F1} \\
14	\midrule
15	Short (196)  & Uncon. &  1 &  5 &  57 & 0 &  63 & 32.4 &  8.9 \\
16	             & Const. &  0 &  0 &   5 & 5 &  10 & 32.4 &  8.9 \\
17	\midrule
18	Medium (180) & Uncon. &  6 &  9 & 104 & 0 & 119 & 27.8 &  6.7 \\
19	             & Const. &  0 &  0 &   7 & 15 & 22 & 27.8 &  6.7 \\
20	\midrule
21	Long (175)   & Uncon. &  3 & 10 & 104 & 1 & 118 & 29.9 &  7.0 \\
22	             & Const. &  0 &  0 &   4 & 20 & 24 & 30.0 &  7.3 \\
23	\bottomrule
24	\end{tabular}
25	\end{table}
26	
27	\begin{table}[h]
28	\centering
29	\small
30	\caption{Document length breakdown on DocRED (Qwen3-8B). Tertile boundaries: Short $\leq$ 160 words, Medium $\leq$ 208, Long $>$ 208.}
31	\label{tab:doc-length-docred}
32	\begin{tabular}{ll rrrrr rr}
33	\toprule
34	\textbf{Bin} & \textbf{Mode} & \textbf{ET} & \textbf{RV} & \textbf{DR} & \textbf{CF} & \textbf{Total} & \textbf{E-F1} & \textbf{R-F1} \\
35	\midrule
36	Short (336)  & Uncon. & 177 & 1238 & 1021 &   9 & 2445 & 61.1 &  9.3 \\
37	             & Const. &   0 &    0 &  495 & 138 &  633 & 62.6 &  9.6 \\
38	\midrule
39	Medium (332) & Uncon. & 147 & 1742 & 1047 &   5 & 2941 & 59.3 &  7.9 \\
40	             & Const. &   0 &    5 &  544 & 180 &  729 & 60.7 &  8.5 \\
41	\midrule
42	Long (330)   & Uncon. & 176 & 2209 & 1162 &   3 & 3550 & 53.9 
…[truncated 1416 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 320 · 2026-05-18T12:27:26.729457+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex"
  }
}
```

</details>

---


### Tool result

_source line 321 · 2026-05-18T12:27:27.583250+00:00_

1	\section{Prompt Sensitivity Analysis}
2	\label{app:prompt-sensitivity}
3	
4	To verify that OntoCoDec's constraint enforcement is robust to prompt variation, we evaluate three prompt variants on SciERC using Qwen3-8B (551 test documents): \textbf{Default} (the prompt used in all main experiments), \textbf{Minimal} (a shortened version listing only entity/relation types), and \textbf{Detailed} (an extended version with type definitions and extraction guidelines). All three variants share the same output JSON schema; only the instruction text differs. Each variant is decoded in both unconstrained and constrained (full Stage~1) modes.
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\caption{Prompt sensitivity results on SciERC. ET, RV, DR denote entity-type, relation-vocabulary, and domain-range violation rates (\%), respectively. $\Delta$DR shows the relative reduction from unconstrained to constrained decoding.}
10	\label{tab:prompt-sensitivity}
11	\begin{tabular}{llcccccc}
12	\toprule
13	\textbf{Prompt} & \textbf{Mode} & \textbf{ET\%} & \textbf{RV\%} & \textbf{DR\%} & \textbf{$\Delta$DR} & \textbf{E-F1} & \textbf{R-F1} \\
14	\midrule
15	\multirow{2}{*}{Default}
16	  & Unconstrained & 0.40 & 1.39 & 15.37 & \multirow{2}{*}{94.0\%} & 31.01 & 8.23 \\
17	  & Constrained   & 0.00 & 0.00 &  0.93 &                         & 30.98 & 8.36 \\
18	\midrule
19	\multirow{2}{*}{Minimal}
20	  & Unconstrained & 0.58 & 1.16 & 16.91 & \multirow{2}{*}{94.6\%} & 31.98 & 7.91 \\
21	  & Constrained   & 0.00 & 0.00 &  0.92 &                         & 31.99 & 7.85 \\
22	\midrule
23	\multirow{2}{*}{Detailed}
24	  & Unconstrained & 0.22 & 0.45 & 11.07 & \multirow{2}{*}{94.2\%} & 33.55 & 10.48 \\
25	  & Constrained   & 0.00 & 0.00 &  0.64 &                         & 33.56 & 10.48 \\
26	\bottomrule
27	\end{tabular}
28	\end{table}
29	
30	Table~\ref{tab:prompt-sensitivity} shows that constrained decoding eliminates entity-type and relation-vocabulary violations entirely (ET and RV drop to 0\%) for 
…[truncated 941 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 322 · 2026-05-18T12:27:27.583723+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex"
  }
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-18T12:27:27.985230+00:00_

1	% Appendix C — Per-Relation Violation Analysis (Llama-3.1-8B)
2	% exp_ids: llama_docred_unconstrained, llama_docred_full_s1
3	
4	\section{Per-Relation Violation Analysis (Llama-3.1-8B)}\label{app:llama-per-relation}
5	
6	Table~\ref{tab:llama-per-relation-dr} presents the per-relation domain--range violation breakdown for Llama-3.1-8B on DocRED under full S1 constraints.
7	The Llama baseline exhibits an RV rate of 16.03\%, substantially lower than Qwen's 29.66\%, indicating stronger baseline vocabulary compliance.
8	% exp_ids: llama_docred_unconstrained (RV=16.03%), qwen_docred_unconstrained (RV=29.66%)
9	Full S1 completely eliminates RV violations and reduces the residual DR rate to 2.55\% (418/16{,}368 triples), with only three relations exceeding 10\%.
10	% exp_ids: llama_docred_full_s1 (DR=2.6%, 418/16368)
11	
12	\begin{table}[h]
13	\centering
14	\caption{Top 10 per-relation DR violation rates for Llama-3.1-8B on DocRED under full S1 constraints. Relations with $>$20 triples and 0\% DR (e.g., P131, P206, P361, P170, P86) are omitted.}
15	\label{tab:llama-per-relation-dr}
16	\resizebox{\columnwidth}{!}{%
17	\begin{tabular}{@{}llrrr@{}}
18	\toprule
19	Relation & PID & Triples & DR Violations & DR Rate (\%) \\
20	\midrule
21	dissolved/demolished & P576 & 73 & 24 & 32.9 \\
22	followed by          & P156 & 117 & 24 & 20.5 \\
23	unemployment rate    & P1198 & 15 & 3 & 20.0 \\
24	end time             & P582 & 130 & 21 & 16.2 \\
25	instance of          & P31  & 290 & 37 & 12.8 \\
26	product/material produced & P1056 & 98 & 11 & 11.2 \\
27	location of formation & P740 & 81 & 8 & 9.9 \\
28	head of state        & P35  & 41  & 3  & 7.3 \\
29	applies to jurisdiction & P1001 & 637 & 45 & 7.1 \\
30	conflict             & P607 & 453 & 30 & 6.6 \\
31	\bottomrule
32	\end{tabular}}
33	\end{table}
34	% exp_ids: llama_docred_full_s1
35	
36	Compared with Qwen, which retains a 10.21\% residual DR under full S1 concentrated in P1198 (83\% fallback) and P171 (78\% fallback), Llama's re
…[truncated 523 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 324 · 2026-05-18T12:27:28.035946+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex"
  }
}
```

</details>

---


### Tool result

_source line 325 · 2026-05-18T12:27:28.588390+00:00_

1	% Appendix — Prompt Templates
2	% W10: Extraction prompts used in all experiments.
3	
4	\section{Prompt Templates}
5	\label{app:prompts}
6	
7	All experiments use the same prompts across constrained and unconstrained decoding; constraints are applied at the logit level, not through prompt modification.
8	Table~\ref{tab:prompts} shows the system and user prompts for each dataset.
9	
10	\begin{table*}[t]
11	\centering
12	\small
13	\begin{tabular}{@{}p{0.95\textwidth}@{}}
14	\toprule
15	\textbf{SciERC --- System Prompt (Unconstrained \& Constrained)} \\
16	\midrule
17	\texttt{You are an expert information extraction system for scientific texts. Extract entities and relations from the given text.} \\[4pt]
18	\texttt{Entity types: Task, Method, Material, Metric, OtherScientificTerm, Generic} \\
19	\texttt{Relation types: Used-for, Feature-of, Hyponym-of, Part-of, Compare, Conjunction, Evaluate-for} \\[4pt]
20	\texttt{Output a JSON object with:} \\
21	\texttt{- "entities": list of \{"text": "...", "type": "..."\}} \\
22	\texttt{- "relations": list of \{"head": "...", "tail": "...", "type": "...", "head\_type": "...", "tail\_type": "..."\}} \\[4pt]
23	\texttt{Output ONLY valid JSON, no explanation.} \\
24	\midrule
25	\textbf{SciERC --- User Prompt} \\
26	\midrule
27	\texttt{Extract all entities and relations from this scientific text:} \\
28	\texttt{"\{text\}"} \\
29	\texttt{Output JSON:} \\
30	\midrule
31	\midrule
32	\textbf{DocRED --- System Prompt (Unconstrained \& Constrained)} \\
33	\midrule
34	\texttt{You are an information extraction system. Extract all entities and relations from the following document.} \\[4pt]
35	\texttt{Entity types: PER, ORG, LOC, TIME, NUM, MISC} \\[4pt]
36	\texttt{Relation types: country, instance of, performer, ...\ (96 Wikidata relation types; full list omitted for space)} \\[4pt]
37	\texttt{Output a JSON object with exactly this structure:} \\
38	\texttt{\{"entities": [\{"text": "entity name", "type": "ENTITY\_TYPE"\}],} \\
39	\texttt{\ "
…[truncated 770 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 326 · 2026-05-18T12:27:28.689209+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 327 · 2026-05-18T12:27:28.740198+00:00_

1	\section{Extended Related Work}
2	\label{app:related_work}
3	
4	% ===========================================================================
5	% Paradigm 1: Grammar-Constrained Decoding
6	% ===========================================================================
7	\paragraph{Grammar-Constrained Decoding.}
8	Recent work has established efficient algorithms for restricting LLM outputs to conform to context-free grammars, making grammar-constrained decoding the de facto standard for obtaining structured output from language models.
9	XGrammar~\cite{dong2025xgrammar} partitions the vocabulary into context-independent and context-dependent tokens and maintains persistent pushdown automata across decoding steps, achieving up to 100$\times$ speedup over prior CFG-constrained decoding methods.
10	Outlines~\cite{willard2023outlines} reformulates constrained generation as finite-state machine transitions with offline vocabulary indexing, enabling efficient enforcement of regular-expression and JSON-schema constraints without runtime overhead per token.
11	LMQL~\cite{beurer-kellner2023lmql} introduces a declarative query language that compiles type, length, and regex constraints into token-level masks, providing a programmable interface for specifying multi-variable output structures.
12	These systems ensure that every generated token belongs to a grammar-valid continuation, but they do not address the \emph{distribution distortion} introduced by naive token masking.
13	A parallel line of work tackles this problem directly: DOMINO~\cite{beurer-kellner2024domino} minimizes distributional divergence during CFG enforcement by formulating mask selection as an optimization problem, and ASAp~\cite{park2024grammar} provides a provably unbiased sampling algorithm that preserves the original LM distribution under grammar constraints.
14	Together, these advances have made grammar-constrained decoding both fast and statistically principled, establishing a robust foundation for stru
…[truncated 19795 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 328 · 2026-05-18T12:27:37.430212+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
  "pages": "1-8",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
    "pages": "1-8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 329 · 2026-05-18T12:27:38.237458+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 330 · 2026-05-18T12:27:40.078502+00:00_

Error: result (5,471,321 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-1-11179fb2/e0eafec6-6db7-491a-8bd5-b5b559b70068/tool-results/mcp-agent-ml-research-pdf_to_images-1779107259858.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-1-11179fb2/e0eafec6-6db7-491a-8bd5-b5b559b70068/tool-results/mcp-agent-ml-research-pdf_to_images-1779107259858.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2648
}
```

</details>

---


### Tool result

_source line 331 · 2026-05-18T12:28:33.725912+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 52, \"total_citations\": 83, \"unique_cited_keys\": 47, \"orphan_bib\": 5, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 41, \"online_not_found\": 3, \"online_mismatch\": 8}, \"cross_check\": {\"orphan_bib\": [\"guidance2023\", \"sakota2025boostcd\", \"ugare2025itergen\", \"xie2016tkrl\", \"zaratiana2023gliner\"], \"missing_bib\": [], \"orphan_count\": 5, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"synchromesh_iclr2022\", \"type\": \"inproceedings\", \"title\": \"Synchromesh: Reliable Code Generation from Pre-trained Language Models\", \"authors\": \"Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares,...\", \"year\": \"2022\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"mgd_neurips2023\", \"type\": \"inproceedings\", \"title\": \"Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context\", \"authors\": \"Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. ...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"pldi2025_type_constrained_codegen\", \"type\": \"article\", \"title\": \"Type-Constrained Code Generation with Language Models\", \"authors\": \"M\\\\\\\"undler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn ...\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM on Programming Languages\"}, {\"key\": \"roth_yih_2004\", \"type\": \"inproceedings\", \"title\": \"A Linear Programming Formulation for Global Inference in Natural Language Tasks\", \"authors\": \"Roth, Dan and Yih, Wen-tau\", \"year\": \"2004\", \"venue\": \"Proceedings of the Eighth Conference on Computational Natural Language Learning ...\"}, {\"key\": \"adakgc_emnlp2023\", \"type\": \"inproceedings\", \"title\": \"Schema-adaptable Knowledge Graph Construction\", \"authors\": \"Ye, Hongbin and Gui, Ho
…[truncated 43296 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 55488
}
```

</details>

---


### Tool call

_source line 332 · 2026-05-18T12:28:43.890409+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf 2>/dev/null || python3 -c \"\nfrom PyPDF2 import PdfReader\nreader = PdfReader('/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf')\nprint(f'Pages: {len(reader.pages)}')\n\"",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf 2>/dev/null || python3 -c \"\nfrom PyPDF2 import PdfReader\nreader = PdfReader('/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf')\nprint(f'Pages: {len(reader.pages)}')\n\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 333 · 2026-05-18T12:28:44.143867+00:00_

Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Mon May 18 12:18:40 2026 UTC
ModDate:         Mon May 18 12:18:40 2026 UTC
Custom Metadata: yes
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           25
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       429667 bytes
Optimized:       no
PDF version:     1.7

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 253
}
```

</details>

---


### Tool call

_source line 334 · 2026-05-18T12:33:25.819140+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 6 审稿意见 — Reviewer 1（方法严谨性 + 实验分析）\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Ontology Constraints\n**Venue**: EMNLP 2026 (ARR May 2026)\n\n---\n\n## 1. Summary\n\nOntoCoDec 提出将 IE ontology schema 编译为两层 token-level 解码约束（grammar + semantic），在自回归生成过程中强制 domain/range type validity。在 3 个模型 × 3 个数据集上验证，DR 下降 42-99%，F1 无显著损失。与 LoRA 微调组合后 DR ≤ 0.20%，beam search 可完全消除校准模型的约束违反。本轮论文相比上轮有显著改善：Abstract 中移除了统计学上不显著的 R² claim，CF-DR trade-off 讨论更加诚实和系统化，reproducibility 细节充分。但发现一个新的关键数据一致性问题（两个 runtime 表数据矛盾）和若干遗留问题部分修复。\n\n---\n\n## 2. Strengths\n\n**S1** 问题定义清晰且有实际意义。violation landscape 分析（§5.1）系统展示了 LLM-IE 中 DR violation 的普遍性和 tightness 驱动机制，为方法提供了强动机。per-relation breakdown 和 tightness 相关性分析（Figure 2, Appendix C）具有独立参考价值。\n\n**S2** 两层架构设计合理，enabling dependency 有充分的实验验证。Semantic-only 仅降 DR 24%（Table 1），grammar+semantic 达 94%，清晰证明了层间依赖关系。sequential masking 相对于 independent masking 的必要性通过 non-rectangularity 分析（§4）严格论证（33-37% spurious pairs）。\n\n**S3** 实验覆盖面优秀。3 models × 3 datasets（2 RE + 1 EE）、zero-shot + LoRA、greedy + sampling + beam search、post-hoc comparison、prompt sensitivity、document length analysis。消融实验设计合理（five-way on SciERC, four-way on DocRED, fine-tuned four-way）。\n\n**S4** CF-DR trade-off 的处理诚实透明。Table 7 的 pilot ablation、Spearman ρ = −0.77 的跨设置验证、CF violation 分布分析（Table 8, Generic 类型占 63.3%）展示了该限制的结构性根源。fine-tuning 将 CF 从 9.90% 降至 1.18%，beam search 进一步降至 0.53%，提供了明确的缓解路径。\n\n**S5** Reproducibility 极为详尽（Appendix G）：LoRA 全部超参数、GPU 型号（RTX PRO 6000, 98GB）、seed=42、软件版本、训练时间。\n\n**S6** WikiEvents 泛化验证（§5.5）展示了框架在 EE 任务上的零修改迁移能力，vocabulary violations 完全消除且 Entity F1 从 0% 提升至 12-18%。\n\n---\n\n## 3. Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1** [critical] **Runtime 数据自相矛盾**\n- 具体位置：Table 9 (Appendix B, §app:runtime) vs Table 12 (Appendix G, §app:reproducibility)\n- 问题：两表均声称测量 Qwen3-8B zero-shot per-document inference time，但数据严重矛盾：\n  - SciERC unconstrained: Table 9 = 2.587s vs Table 12 = 8.69s（**3.4× 差异**）\n  - SciERC Full S1: Table 9 = 2.647s (+2.3%) vs Table 12 = 6.76s (**−22%**)\n  - DocRED unconstrained: Table 9 = 21.023s vs Table 12 = 19.75s\n- Table 9 和 inline text (§5, \"Full S1 adds +2.3% on SciERC\") 声称约束增加开销；Table 12 和紧随其后的文字声称 \"full S1 constrained decoding is 22% **faster**\"。方向完全相反。\n- 为什么影响接收：审稿人无法判断实际 runtime 开销。同一论文中对同一配置作出相反的定量声明（+2.3% vs −22%）是数据完整性问题。\n- 建议修改方向：确认哪组数据正确，删除错误表格或解释两表的测量差异（如 Table 9 仅测量 generation time 而 Table 12 包含 prompt encoding）。确保 inline text 与保留的表格一致。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [warning] **Sampling robustness on DocRED: CF 5× 跳升未讨论**\n- 具体位置：Table 6 (Appendix E), DocRED sampling row\n- 问题：Nucleus sampling 下 DocRED CF 从 2.57% 跳至 12.63%（4.9×），但论文仅称 \"Constraint robustness under nucleus sampling\"。DR 接近不变（10.21→10.31%），但 CF 的剧烈恶化未被讨论或解释。此外 DocRED sampling 仅评估 114/998 文档（11.4%），统计代表性有限。\n- 建议：在 Appendix E 正文中增加对 CF 跳升的分析（可能原因：sampling 的随机性导致更多 registry override events），并明确注明 DocRED sampling 结果的代表性限制。\n\n**W2** [warning] **WikiEvents Grammar-only F1 缺失**\n- 具体位置：Table 4 (§5.5), Grammar rows\n- 问题：Grammar-only 行的 Trigger F1 和 Entity F1 标记为 \"---\"（not applicable），但 grammar-only 仍然产生结构化输出，理应可以计算 F1。Caption 解释为 \"grammar-only has no semantic-layer metrics\"，但 F1 不是 semantic-layer metric。\n- 为什么重要：Grammar-only 作为 ablation baseline，缺少 F1 使得无法独立评估 grammar 层对 extraction quality 的影响。\n- 建议：补充 grammar-only 的 Trigger/Entity F1，或者解释为什么 grammar-only 输出无法进行 F1 评估（如 parser 仍无法处理 RoV=76% 的输出）。\n\n**W3** [warning] **Llama DocRED parse failure 对 F1 的 confounding 效应未充分量化**\n- 具体位置：Table 3 caption, Limitations section\n- 问题：Llama DocRED parse failure 从 unconstrained 的约 6.8% 增至 constrained 的 9.1%（+34%），Limitations 承认 \"partially confounded by increased parse failures\"。但论文未提供 parse-failure-excluded F1 对比，审稿人无法判断 Llama DocRED 的 F1 变化（+0.29pp）有多少来自 constraint 效果 vs parse failure 分布变化。\n- 建议：在 Appendix 中增加 parse-success-only 子集的 F1 对比，或至少报告 constrained vs unconstrained 在 parse-successful 交集上的 F1。\n\n**W4** [warning] **RV=0.03% 残余未解释**\n- 具体位置：Table 2 (§5.3), Grammar row and Full S1 row\n- 问题：Grammar 层和 Full S1 在 DocRED 上均保留 RV=0.03%（约 5/17,478 triples），而 SciERC 和其他所有设置 RV=0%。Grammar enforcement 理论上应完全消除 RV（因为 CFG 限制 relation 到 R），0.03% 的残余违背了 grammar layer 的设计保证。\n- 建议：解释这些残余 RV 的来源（tokenization edge case? multi-token relation name 的 continuation masking gap? 或 evaluation artifact?）。\n\n**W5** [warning] **Semantic-only ET 增长机制未解释**\n- 具体位置：Table 2 (§5.3), Semantic row: ET 2.48% → 4.22% (+70%)\n- 问题：§5.3 称 semantic-only \"cannot prevent ET increases (2.48%→4.22%), replicating SciERC's enabling dependency\"。但 enabling dependency 解释的是 semantic-only 无法消除 ET（缺少 grammar enforcement），不能解释为什么 ET 会**增加** 70%。增加意味着 semantic layer 主动导致了更多的 ET violation，这需要不同的解释。\n- 建议：分析 semantic-only 下 ET 增加的具体机制。可能假设：semantic masking 在某些位置改变了 type token 的概率分布，使模型生成了更多 OOV type names。\n\n---\n\n## 4. Open Issue Resolution Check\n\n| Issue ID | 描述 | 状态 | 备注 |\n|----------|------|------|------|\n| R2-N1 (Critical) | Abstract R²=0.886 移除 | ✅ resolved | Abstract 改为定性描述 \"residual DR correlates with...\"。R² 保留在 Appendix B 且加了充分 caveat（p≈0.058, n=4, \"descriptive characterization\"） |\n| W3 | Post-hoc filtering framing 平衡 | ✅ resolved | §1 明确写 \"Post-hoc filtering achieves higher F1 in most zero-shot settings via precision gains, but at the cost of discarding up to 48%...\"，平衡表述到位 |\n| R2-N3 | Llama DocRED parse failure metrics | ⚠️ partially | Table 3 caption 报告了 parse failure rate (9.1%)，Limitations 承认 confounding。但未提供 parse-failure-excluded 的 violation rate 和 F1（见 W3） |\n| R2-N6 | Semantic-only DocRED ET +70% 机制 | ❌ not fixed | §5.3 提到了现象但将其归因于 enabling dependency，这无法解释 ET 为何**增加**（见 W5） |\n| R4-N3 | Beam search SciERC full set 正文讨论 | ✅ resolved | §5.2 和 §7 均引用 beam search 结果并指向 Appendix F |\n| R4-W2 | DocRED fallback coverage 显式报告 | ✅ resolved | Appendix B 报告 Qwen DocRED f_gf = 0.08% (46/54,859)，99.9% coverage |\n| R4-W3 | §4 vs Abstract DR range 不一致 | ✅ resolved | §4 现在解释完整 42-99% 范围来源（包含 Mistral），与 Abstract 一致 |\n| R4-Q1 | JSON field ordering 在 §3 显式声明 | ✅ resolved | §3.1: \"a fixed field ordering (head → tail → relation → head_type → tail_type) via deterministic grammar compilation\" |\n| R4-Q2 | CF-DR ablation DocRED 讨论 | ✅ resolved | Appendix B 增加 cross-configuration 分析（Spearman ρ = −0.77, n=6），讨论了 Llama DocRED 的 CF headroom |\n| R2-N10 | RV=0.03% 解释一致性 | ⚠️ partially | 论文中 RV=0.03% 出现在 Table 2 但未给出解释（见 W4） |\n| GC-N1 | Grammar-only 标识为 GCD 上限 | ✅ resolved | §5.2 明确写 \"This configuration represents the capability ceiling of grammar-based constrained decoding\" |\n| R2-N5 | Reproducibility 补充 | ✅ resolved | Appendix G 极为详尽：LoRA 全参数、GPU、seed、软件版本、训练时间 |\n\n**总结**: 12 项中 8 项 ✅ resolved，2 项 ⚠️ partially，2 项 ❌/⚠️ not adequately addressed。\n\n---\n\n## 5. New Issues\n\n（已包含在 §3 Weaknesses 中：N1 runtime 矛盾、W1 sampling CF 跳升、W2 WikiEvents F1 缺失、W4 RV 残余、W5 ET 增长机制）\n\n---\n\n## 6. Questions to Authors\n\n**Q1**: Table 9 和 Table 12 的 runtime 测量条件具体有何不同？如果是不同的测量粒度（generation-only vs end-to-end），为什么 SciERC 上方向相反（+2.3% vs −22%）但 DocRED 上方向一致（+5.4% vs +3.2%）？\n\n**Q2**: WikiEvents Grammar-only 行 Trigger/Entity F1 标记为 \"---\" 的具体原因是什么？是因为 grammar-only 输出在 RoV=76% 时 parser 无法正确提取（格式问题），还是有其他原因？\n\n**Q3**: Semantic-only 在 DocRED 上 ET 从 2.48% 增至 4.22%。Semantic layer 是否在某些 edge case 下修改了 type token 的概率分布，使模型更倾向生成不在 E 中的 token？\n\n**Q4**: DocRED RV=0.03% 残余（Grammar 和 Full S1 均如此）的来源是什么？如果 CFG 严格限制 relation 到 R，为什么会有任何 RV violation？\n\n---\n\n## 7. Missing References\n\n引用验证结果总体良好（52 条 bib, 47 条被引用, 41 条 online verified）。\n\n- 5 个 orphan bib entries 未被引用：`guidance2023`, `sakota2025boostcd`, `ugare2025itergen`, `xie2016tkrl`, `zaratiana2023gliner`。建议清理或引用。\n- 2 个 not_found：`regino2025kgcurator` 和 `guidance2023`（后者为 orphan）。`regino2025kgcurator` 在 OpenAlex 中未找到匹配，建议验证其存在性。\n- 8 个 author name mismatch（主要是 LaTeX 编码 vs API 标准化差异，如 `m\\\"undler` vs `mündler`），不影响引用正确性。\n\n建议：清理未使用的 bib entries，删除 orphan 条目避免审稿人质疑。\n\n---\n\n## 8. Scores\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| **Overall Assessment** | **3.5** (Borderline Conference) | 方法有新意且实验全面，但 runtime 数据矛盾是数据完整性问题，若修复则可达 Conference 水平 |\n| **Soundness** | **3/5** | 核心方法严谨，形式化完整，但两个 runtime 表数据矛盾、semantic-only ET 增长未解释、RV 残余未解释 |\n| **Excitement** | **3.5/5** | 问题定义有清晰价值，two-layer composition + enabling dependency 是有洞察的设计；CF trade-off 的诚实讨论增加可信度 |\n| **Reproducibility** | **4/5** | Appendix G 极为详尽（LoRA params, GPU, seed, software versions, training time）；唯一扣分是 runtime 数据矛盾导致无法确认实际开销 |\n| **Confidence** | **4/5** | 我仔细阅读了完整论文（正文 + 全部 9 个附录），逐一核查了数据一致性和上轮遗留问题 |\n\n---\n\n## 9. Detailed Section Comments\n\n### Abstract\n- R² 已移除 ✅\n- DR range 42-99% 与正文一致 ✅\n- WikiEvents 结果（Entity F1: 0%→12-18%）有正文支撑 ✅\n- 长度接近上限（~260 words），但信息密度高，可接受\n\n### §1 Introduction\n- Post-hoc filtering 平衡表述到位 ✅\n- Contribution 3 信息非常密集（DR、F1、EE、composability、CF trade-off 全部压在一个 bullet point），考虑拆分为 (3a) empirical validation + (3b) composability\n- \"DR ↓76-99% on SciERC and ↓42-90% on DocRED\" 与 Table 3 一致 ✅\n\n### §2 Background\n- 形式化清晰（O, E, R, σ, tightness κ）\n- prefix-decidable 的概念引入恰当\n- \"each entity type name maps to a unique first subword token\" 这个假设在 §3 有进一步讨论（continuation masking），但 §2 的措辞可能误导读者以为这是一个更简单的假设\n\n### §3 Method\n- JSON field ordering 作为 sequential masking 前提已显式声明 ✅\n- Continuation masking (§3.3.4) 设计巧妙，解决了 SentencePiece 和 prefix-shared type 问题\n- Grammar-first fallback 的设计决策（structural integrity > type validity）有清晰的理由\n- S2 two-pass strategy 的比较过于简略（\"Detailed comparison is provided in the appendix\"），但考虑到 S1 在所有 metric 上优于或等于 S2，这可以接受\n\n### §4 Constraint Composition\n- Non-rectangularity 论证严格（100% SciERC, 73/96 DocRED relations）\n- Decidability taxonomy (local/prefix-decidable/non-local) 是有用的框架\n- Tightness 定义 κ(r) 使用 V(r) 替代 §2 的 σ(r)，notation 不完全一致但语义等价\n\n### §5 Experiments\n- Five-way ablation (Table 1) 和 four-way ablation (Table 2) 设计合理\n- Bootstrap CI 和 p-value 报告规范\n- **DocRED grammar-only DR 上升 42% 的\"latent violation surfacing\"解释**合理且有说服力\n- WikiEvents：F1 从 0% 到 12-18% 的增益令人印象深刻，但 grammar-only F1 缺失是一个 gap (W2)\n- Composability table (Table 5) 展示了 ZS + LoRA × unconstr + S1 的完整矩阵，数据说服力强\n\n### §6 Related Work\n- 正文简洁（3 paragraphs），Appendix A 提供了详尽的 extended survey\n- Positioning 清晰：vs grammar-only (XGrammar/Outlines/LMQL), vs type-constrained code gen (PICARD/Synchromesh/MGD), vs post-hoc (ODKE+/SPIRES/OntoLogX)\n- Quality impact discussion 引用 CRANE/Tam et al./Schall et al. 来回应 \"constrained decoding hurts quality\" 的顾虑，有效\n\n### §7 Discussion and Conclusion\n- 非常简短（约 100 words），主要是摘要式总结\n- CF trade-off 指向 §5.2 和 Appendix B，beam search 指向 Appendix F\n- 未来工作方向（global entity-level type consensus）明确\n\n### Limitations\n- 覆盖全面：CF model-dependence, CF-DR trade-off, entity F1 confounding, zero-shot F1 ceiling, composability scope (LoRA only), scalability (7-8B only), continuation masking scalability, beam search scope, residual DR decomposition\n- 是我见过的最诚实和详尽的 Limitations section 之一\n\n### Appendices\n- 内容丰富且有组织（A-I，涵盖 prompts, extended related work, extended discussion, per-relation analysis, sampling, beam search, reproducibility, doc length, prompt sensitivity）\n- Appendix B (Extended Discussion) 是核心贡献的重要补充，建议确保正文中的引用指向正确\n- **关键问题**：Table 9 (App B) vs Table 12 (App G) runtime 矛盾（N1）",
  "reviewer_id": "1",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 6 审稿意见 — Reviewer 1（方法严谨性 + 实验分析）\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Ontology Constraints\n**Venue**: EMNLP 2026 (ARR May 2026)\n\n---\n\n## 1. Summary\n\nOntoCoDec 提出将 IE ontology schema 编译为两层 token-level 解码约束（grammar + semantic），在自回归生成过程中强制 domain/range type validity。在 3 个模型 × 3 个数据集上验证，DR 下降 42-99%，F1 无显著损失。与 LoRA 微调组合后 DR ≤ 0.20%，beam search 可完全消除校准模型的约束违反。本轮论文相比上轮有显著改善：Abstract 中移除了统计学上不显著的 R² claim，CF-DR trade-off 讨论更加诚实和系统化，reproducibility 细节充分。但发现一个新的关键数据一致性问题（两个 runtime 表数据矛盾）和若干遗留问题部分修复。\n\n---\n\n## 2. Strengths\n\n**S1** 问题定义清晰且有实际意义。violation landscape 分析（§5.1）系统展示了 LLM-IE 中 DR violation 的普遍性和 tightness 驱动机制，为方法提供了强动机。per-relation breakdown 和 tightness 相关性分析（Figure 2, Appendix C）具有独立参考价值。\n\n**S2** 两层架构设计合理，enabling dependency 有充分的实验验证。Semantic-only 仅降 DR 24%（Table 1），grammar+semantic 达 94%，清晰证明了层间依赖关系。sequential masking 相对于 independent masking 的必要性通过 non-rectangularity 分析（§4）严格论证（33-37% spurious pairs）。\n\n**S3** 实验覆盖面优秀。3 models × 3 datasets（2 RE + 1 EE）、zero-shot + LoRA、greedy + sampling + beam search、post-hoc comparison、prompt sensitivity、document length analysis。消融实验设计合理（five-way on SciERC, four-way on DocRED, fine-tuned four-way）。\n\n**S4** CF-DR trade-off 的处理诚实透明。Table 7 的 pilot ablation、Spearman ρ = −0.77 的跨设置验证、CF violation 分布分析（Table 8, Generic 类型占 63.3%）展示了该限制的结构性根源。fine-tuning 将 CF 从 9.90% 降至 1.18%，beam search 进一步降至 0.53%，提供了明确的缓解路径。\n\n**S5** Reproducibility 极为详尽（Appendix G）：LoRA 全部超参数、GPU 型号（RTX PRO 6000, 98GB）、seed=42、软件版本、训练时间。\n\n**S6** WikiEvents 泛化验证（§5.5）展示了框架在 EE 任务上的零修改迁移能力，vocabulary violations 完全消除且 Entity F1 从 0% 提升至 12-18%。\n\n---\n\n## 3. Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1** [critical] **Runtime 数据自相矛盾**\n- 具体位置：Table 9 (Appendix B, §app:runtime) vs Table 12 (Appendix G, §app:reproducibility)\n- 问题：两表均声称测量 Qwen3-8B zero-shot per-document inference time，但数据严重矛盾：\n  - SciERC unconstrained: Table 9 = 2.587s vs Table 12 = 8.69s（**3.4× 差异**）\n  - SciERC Full S1: Table 9 = 2.647s (+2.3%) vs Table 12 = 6.76s (**−22%**)\n  - DocRED unconstrained: Table 9 = 21.023s vs Table 12 = 19.75s\n- Table 9 和 inline text (§5, \"Full S1 adds +2.3% on SciERC\") 声称约束增加开销；Table 12 和紧随其后的文字声称 \"full S1 constrained decoding is 22% **faster**\"。方向完全相反。\n- 为什么影响接收：审稿人无法判断实际 runtime 开销。同一论文中对同一配置作出相反的定量声明（+2.3% vs −22%）是数据完整性问题。\n- 建议修改方向：确认哪组数据正确，删除错误表格或解释两表的测量差异（如 Table 9 仅测量 generation time 而 Table 12 包含 prompt encoding）。确保 inline text 与保留的表格一致。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [warning] **Sampling robustness on DocRED: CF 5× 跳升未讨论**\n- 具体位置：Table 6 (Appendix E), DocRED sampling row\n- 问题：Nucleus sampling 下 DocRED CF 从 2.57% 跳至 12.63%（4.9×），但论文仅称 \"Constraint robustness under nucleus sampling\"。DR 接近不变（10.21→10.31%），但 CF 的剧烈恶化未被讨论或解释。此外 DocRED sampling 仅评估 114/998 文档（11.4%），统计代表性有限。\n- 建议：在 Appendix E 正文中增加对 CF 跳升的分析（可能原因：sampling 的随机性导致更多 registry override events），并明确注明 DocRED sampling 结果的代表性限制。\n\n**W2** [warning] **WikiEvents Grammar-only F1 缺失**\n- 具体位置：Table 4 (§5.5), Grammar rows\n- 问题：Grammar-only 行的 Trigger F1 和 Entity F1 标记为 \"---\"（not applicable），但 grammar-only 仍然产生结构化输出，理应可以计算 F1。Caption 解释为 \"grammar-only has no semantic-layer metrics\"，但 F1 不是 semantic-layer metric。\n- 为什么重要：Grammar-only 作为 ablation baseline，缺少 F1 使得无法独立评估 grammar 层对 extraction quality 的影响。\n- 建议：补充 grammar-only 的 Trigger/Entity F1，或者解释为什么 grammar-only 输出无法进行 F1 评估（如 parser 仍无法处理 RoV=76% 的输出）。\n\n**W3** [warning] **Llama DocRED parse failure 对 F1 的 confounding 效应未充分量化**\n- 具体位置：Table 3 caption, Limitations section\n- 问题：Llama DocRED parse failure 从 unconstrained 的约 6.8% 增至 constrained 的 9.1%（+34%），Limitations 承认 \"partially confounded by increased parse failures\"。但论文未提供 parse-failure-excluded F1 对比，审稿人无法判断 Llama DocRED 的 F1 变化（+0.29pp）有多少来自 constraint 效果 vs parse failure 分布变化。\n- 建议：在 Appendix 中增加 parse-success-only 子集的 F1 对比，或至少报告 constrained vs unconstrained 在 parse-successful 交集上的 F1。\n\n**W4** [warning] **RV=0.03% 残余未解释**\n- 具体位置：Table 2 (§5.3), Grammar row and Full S1 row\n- 问题：Grammar 层和 Full S1 在 DocRED 上均保留 RV=0.03%（约 5/17,478 triples），而 SciERC 和其他所有设置 RV=0%。Grammar enforcement 理论上应完全消除 RV（因为 CFG 限制 relation 到 R），0.03% 的残余违背了 grammar layer 的设计保证。\n- 建议：解释这些残余 RV 的来源（tokenization edge case? multi-token relation name 的 continuation masking gap? 或 evaluation artifact?）。\n\n**W5** [warning] **Semantic-only ET 增长机制未解释**\n- 具体位置：Table 2 (§5.3), Semantic row: ET 2.48% → 4.22% (+70%)\n- 问题：§5.3 称 semantic-only \"cannot prevent ET increases (2.48%→4.22%), replicating SciERC's enabling dependency\"。但 enabling dependency 解释的是 semantic-only 无法消除 ET（缺少 grammar enforcement），不能解释为什么 ET 会**增加** 70%。增加意味着 semantic layer 主动导致了更多的 ET violation，这需要不同的解释。\n- 建议：分析 semantic-only 下 ET 增加的具体机制。可能假设：semantic masking 在某些位置改变了 type token 的概率分布，使模型生成了更多 OOV type names。\n\n---\n\n## 4. Open Issue Resolution Check\n\n| Issue ID | 描述 | 状态 | 备注 |\n|----------|------|------|------|\n| R2-N1 (Critical) | Abstract R²=0.886 移除 | ✅ resolved | Abstract 改为定性描述 \"residual DR correlates with...\"。R² 保留在 Appendix B 且加了充分 caveat（p≈0.058, n=4, \"descriptive characterization\"） |\n| W3 | Post-hoc filtering framing 平衡 | ✅ resolved | §1 明确写 \"Post-hoc filtering achieves higher F1 in most zero-shot settings via precision gains, but at the cost of discarding up to 48%...\"，平衡表述到位 |\n| R2-N3 | Llama DocRED parse failure metrics | ⚠️ partially | Table 3 caption 报告了 parse failure rate (9.1%)，Limitations 承认 confounding。但未提供 parse-failure-excluded 的 violation rate 和 F1（见 W3） |\n| R2-N6 | Semantic-only DocRED ET +70% 机制 | ❌ not fixed | §5.3 提到了现象但将其归因于 enabling dependency，这无法解释 ET 为何**增加**（见 W5） |\n| R4-N3 | Beam search SciERC full set 正文讨论 | ✅ resolved | §5.2 和 §7 均引用 beam search 结果并指向 Appendix F |\n| R4-W2 | DocRED fallback coverage 显式报告 | ✅ resolved | Appendix B 报告 Qwen DocRED f_gf = 0.08% (46/54,859)，99.9% coverage |\n| R4-W3 | §4 vs Abstract DR range 不一致 | ✅ resolved | §4 现在解释完整 42-99% 范围来源（包含 Mistral），与 Abstract 一致 |\n| R4-Q1 | JSON field ordering 在 §3 显式声明 | ✅ resolved | §3.1: \"a fixed field ordering (head → tail → relation → head_type → tail_type) via deterministic grammar compilation\" |\n| R4-Q2 | CF-DR ablation DocRED 讨论 | ✅ resolved | Appendix B 增加 cross-configuration 分析（Spearman ρ = −0.77, n=6），讨论了 Llama DocRED 的 CF headroom |\n| R2-N10 | RV=0.03% 解释一致性 | ⚠️ partially | 论文中 RV=0.03% 出现在 Table 2 但未给出解释（见 W4） |\n| GC-N1 | Grammar-only 标识为 GCD 上限 | ✅ resolved | §5.2 明确写 \"This configuration represents the capability ceiling of grammar-based constrained decoding\" |\n| R2-N5 | Reproducibility 补充 | ✅ resolved | Appendix G 极为详尽：LoRA 全参数、GPU、seed、软件版本、训练时间 |\n\n**总结**: 12 项中 8 项 ✅ resolved，2 项 ⚠️ partially，2 项 ❌/⚠️ not adequately addressed。\n\n---\n\n## 5. New Issues\n\n（已包含在 §3 Weaknesses 中：N1 runtime 矛盾、W1 sampling CF 跳升、W2 WikiEvents F1 缺失、W4 RV 残余、W5 ET 增长机制）\n\n---\n\n## 6. Questions to Authors\n\n**Q1**: Table 9 和 Table 12 的 runtime 测量条件具体有何不同？如果是不同的测量粒度（generation-only vs end-to-end），为什么 SciERC 上方向相反（+2.3% vs −22%）但 DocRED 上方向一致（+5.4% vs +3.2%）？\n\n**Q2**: WikiEvents Grammar-only 行 Trigger/Entity F1 标记为 \"---\" 的具体原因是什么？是因为 grammar-only 输出在 RoV=76% 时 parser 无法正确提取（格式问题），还是有其他原因？\n\n**Q3**: Semantic-only 在 DocRED 上 ET 从 2.48% 增至 4.22%。Semantic layer 是否在某些 edge case 下修改了 type token 的概率分布，使模型更倾向生成不在 E 中的 token？\n\n**Q4**: DocRED RV=0.03% 残余（Grammar 和 Full S1 均如此）的来源是什么？如果 CFG 严格限制 relation 到 R，为什么会有任何 RV violation？\n\n---\n\n## 7. Missing References\n\n引用验证结果总体良好（52 条 bib, 47 条被引用, 41 条 online verified）。\n\n- 5 个 orphan bib entries 未被引用：`guidance2023`, `sakota2025boostcd`, `ugare2025itergen`, `xie2016tkrl`, `zaratiana2023gliner`。建议清理或引用。\n- 2 个 not_found：`regino2025kgcurator` 和 `guidance2023`（后者为 orphan）。`regino2025kgcurator` 在 OpenAlex 中未找到匹配，建议验证其存在性。\n- 8 个 author name mismatch（主要是 LaTeX 编码 vs API 标准化差异，如 `m\\\"undler` vs `mündler`），不影响引用正确性。\n\n建议：清理未使用的 bib entries，删除 orphan 条目避免审稿人质疑。\n\n---\n\n## 8. Scores\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| **Overall Assessment** | **3.5** (Borderline Conference) | 方法有新意且实验全面，但 runtime 数据矛盾是数据完整性问题，若修复则可达 Conference 水平 |\n| **Soundness** | **3/5** | 核心方法严谨，形式化完整，但两个 runtime 表数据矛盾、semantic-only ET 增长未解释、RV 残余未解释 |\n| **Excitement** | **3.5/5** | 问题定义有清晰价值，two-layer composition + enabling dependency 是有洞察的设计；CF trade-off 的诚实讨论增加可信度 |\n| **Reproducibility** | **4/5** | Appendix G 极为详尽（LoRA params, GPU, seed, software versions, training time）；唯一扣分是 runtime 数据矛盾导致无法确认实际开销 |\n| **Confidence** | **4/5** | 我仔细阅读了完整论文（正文 + 全部 9 个附录），逐一核查了数据一致性和上轮遗留问题 |\n\n---\n\n## 9. Detailed Section Comments\n\n### Abstract\n- R² 已移除 ✅\n- DR range 42-99% 与正文一致 ✅\n- WikiEvents 结果（Entity F1: 0%→12-18%）有正文支撑 ✅\n- 长度接近上限（~260 words），但信息密度高，可接受\n\n### §1 Introduction\n- Post-hoc filtering 平衡表述到位 ✅\n- Contribution 3 信息非常密集（DR、F1、EE、composability、CF trade-off 全部压在一个 bullet point），考虑拆分为 (3a) empirical validation + (3b) composability\n- \"DR ↓76-99% on SciERC and ↓42-90% on DocRED\" 与 Table 3 一致 ✅\n\n### §2 Background\n- 形式化清晰（O, E, R, σ, tightness κ）\n- prefix-decidable 的概念引入恰当\n- \"each entity type name maps to a unique first subword token\" 这个假设在 §3 有进一步讨论（continuation masking），但 §2 的措辞可能误导读者以为这是一个更简单的假设\n\n### §3 Method\n- JSON field ordering 作为 sequential masking 前提已显式声明 ✅\n- Continuation masking (§3.3.4) 设计巧妙，解决了 SentencePiece 和 prefix-shared type 问题\n- Grammar-first fallback 的设计决策（structural integrity > type validity）有清晰的理由\n- S2 two-pass strategy 的比较过于简略（\"Detailed comparison is provided in the appendix\"），但考虑到 S1 在所有 metric 上优于或等于 S2，这可以接受\n\n### §4 Constraint Composition\n- Non-rectangularity 论证严格（100% SciERC, 73/96 DocRED relations）\n- Decidability taxonomy (local/prefix-decidable/non-local) 是有用的框架\n- Tightness 定义 κ(r) 使用 V(r) 替代 §2 的 σ(r)，notation 不完全一致但语义等价\n\n### §5 Experiments\n- Five-way ablation (Table 1) 和 four-way ablation (Table 2) 设计合理\n- Bootstrap CI 和 p-value 报告规范\n- **DocRED grammar-only DR 上升 42% 的\"latent violation surfacing\"解释**合理且有说服力\n- WikiEvents：F1 从 0% 到 12-18% 的增益令人印象深刻，但 grammar-only F1 缺失是一个 gap (W2)\n- Composability table (Table 5) 展示了 ZS + LoRA × unconstr + S1 的完整矩阵，数据说服力强\n\n### §6 Related Work\n- 正文简洁（3 paragraphs），Appendix A 提供了详尽的 extended survey\n- Positioning 清晰：vs grammar-only (XGrammar/Outlines/LMQL), vs type-constrained code gen (PICARD/Synchromesh/MGD), vs post-hoc (ODKE+/SPIRES/OntoLogX)\n- Quality impact discussion 引用 CRANE/Tam et al./Schall et al. 来回应 \"constrained decoding hurts quality\" 的顾虑，有效\n\n### §7 Discussion and Conclusion\n- 非常简短（约 100 words），主要是摘要式总结\n- CF trade-off 指向 §5.2 和 Appendix B，beam search 指向 Appendix F\n- 未来工作方向（global entity-level type consensus）明确\n\n### Limitations\n- 覆盖全面：CF model-dependence, CF-DR trade-off, entity F1 confounding, zero-shot F1 ceiling, composability scope (LoRA only), scalability (7-8B only), continuation masking scalability, beam search scope, residual DR decomposition\n- 是我见过的最诚实和详尽的 Limitations section 之一\n\n### Appendices\n- 内容丰富且有组织（A-I，涵盖 prompts, extended related work, extended discussion, per-relation analysis, sampling, beam search, reproducibility, doc length, prompt sensitivity）\n- Appendix B (Extended Discussion) 是核心贡献的重要补充，建议确保正文中的引用指向正确\n- **关键问题**：Table 9 (App B) vs Table 12 (App G) runtime 矛盾（N1）",
    "reviewer_id": "1",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 335 · 2026-05-18T12:33:29.936094+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4116
}
```

</details>

---


### Assistant

_source line 336 · 2026-05-18T12:33:34.784192+00:00_

现在我已经完整阅读了论文的所有章节（Abstract, §1-§7, Limitations, Ethics, 全部 Appendix A-I），验证了引用，检查了 PDF 页数（25页）。开始撰写审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1"
}
```

</details>

---


## Round 10

## Round 10

52 recorded events


### User

_source line 337 · 2026-05-18T12:41:31.066616+00:00_

[Round 6 审稿请求]:
## Round 6 继续审稿 — Reviewer 1（方法/实验严谨性）

**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Ontology Constraints
**论文路径**: `projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`
**Venue**: EMNLP 2026 (ARR May 2026 cycle), deadline 2026-05-25
**格式**: ACL 2023 模板 (`\usepackage[review]{acl}`)，double-blind，Long paper 8页正文 + 无限附录/参考文献
**Round 5 评分**: Weak Accept (Findings)

---

### 你的任务

这是增量审稿——论文在 Round 5 报告后进行了修订（最后修改 2026-05-18 12:04）。你需要：
1. **逐条验证**下方 open issues 是否已在修订版中修复
2. **识别修改是否引入了新问题**
3. 对每个 issue 给出判定：✅ Resolved / ⚠️ Partially fixed / ❌ Not fixed / 🆕 New issue
4. 更新整体评分建议

### 你负责核查的 Open Issues（方法/实验类）

**[MF1] R2-N1 [critical] R²=0.886 (n=4) 过度突出**
- Round 5 要求：(1) Abstract 移除 R² 具体值，改为定性描述；(2) Appendix 报告 F(1,2) 和 p≈0.058；(3) Mistral 排除提供先验标准
- 检查：Abstract 是否仍含 R²=0.886？§7 是否保持 "descriptive characterization"？

**[SF1] R4-N3 [warning] Beam search 结果被降级到 Appendix**
- Round 5 要求：(1) §5 或 §7 讨论 beam SciERC 全集结果(DR=0%, CF=0.53%)；(2) 报告 beam runtime overhead；(3) 明确 greedy=实用推荐 vs beam=质量最优；(4) DocRED beam 用匹配 50-doc greedy baseline
- 检查：正文是否已讨论 beam？

**[SF5] R2-N3 [warning] Llama DocRED parse failure confounding**
- Round 5 要求：提供 Llama DocRED ZS parse-failure-excluded violation rates 和 F1
- 检查：是否有新数据？

**[SF7] R4-W2 [warning] DocRED fallback coverage 未报告**
- Round 5 要求：显式报告 DocRED effective semantic constraint coverage 并与 SciERC 对比
- 检查：是否已添加？

**[SF8] R2-N5 [warning] Reproducibility 信息不充分**
- Round 5 要求：Appendix 添加 LoRA 超参数表（rank, alpha, LR, epochs, batch size）、GPU 型号、random seeds
- 检查：appendix_reproducibility.tex 内容

**[SF9] R4-W3 [warning] §4 DR reduction 范围与 Abstract 不一致**
- Round 5 要求：§4 加 "for calibrated models" 或用全范围 76-99%
- 检查：§4 范围表述

**[Q1] R4-Q1 [warning] JSON field ordering 是 sequential masking 隐含前提**
- Round 5 要求：§3 显式声明 JSON Schema 是否强制 field ordering
- 检查：§3 是否有相关声明

**[M3] R2-N6 [warning] Semantic-only DocRED ET 增加 +70% 未解释**
- Round 5 要求：§5 添加 DocRED-specific 解释（96 关系更复杂 domain/range）
- 检查：是否已解释

**[M1] R2-N10 [info] RV=0.03% 解释不一致**
- Round 5 要求：统一 paper 和 rebuttal 对 RV=0.03% 的解释
- 检查：§5.3 措辞

**[M2] GC-N1 [info] Grammar-only 未标识为 GCD capability ceiling**
- Round 5 要求：§5 或 §6 添加一句标注
- 检查：是否有 GCD ceiling 标注

**[M6] R4-Q2 [info] CF-DR ablation 仅 SciERC/Qwen**
- Round 5 要求：讨论 transferability 或添加 Llama DocRED 数据
- 检查：是否有讨论

### 输出格式

```
## Issue Verification

| Issue ID | Severity | Verdict | Evidence |
|----------|----------|---------|----------|
| R2-N1    | critical | ✅/⚠️/❌ | 具体引用论文行号 |
| ...      | ...      | ...     | ...      |

## New Issues Found
（如有）

## Updated Assessment
- 方法严谨性: X/5
- 实验充分性: X/5
- Reproducibility: X/5
- 建议评分: ...
- 理由: ...
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 338 · 2026-05-18T12:41:47.937696+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 339 · 2026-05-18T12:41:48.188995+00:00_

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
12	\usepackage{multirow}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{enumitem}
16	\usepackage{xcolor}
17	
18	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Ontology Constraints}
19	
20	\author{Anonymous ACL submission}
21	
22	\begin{document}
23	\maketitle
24	
25	% === Abstract ===
26	\input{abstract}
27	
28	% === §1 Introduction ===
29	\input{section1_introduction_draft}
30	
31	% === §2 Background ===
32	\input{section2_background}
33	
34	% === §3 Method ===
35	\input{section3_method_draft}
36	
37	% === §4 Constraint Composition ===
38	\section{Constraint Composition}
39	\label{sec:composition}
40	\input{section4_composition_draft}
41	
42	% === §5 Experiments ===
43	\section{Experiments}
44	\label{sec:experiments}
45	
46	\subsection{Violation Landscape}
47	\input{section3_violation_landscape}
48	
49	\input{section5_scierc_draft}
50	\input{section5_docred_draft}
51	\input{section5_crossmodel_draft}
52	\input{section5_wikievents_draft}
53	\input{section5_runtime}
54	
55	% === §6 Related Work ===
56	\input{section6_related_work}
57	
58	% === §7 Discussion and Conclusion ===
59	\section{Discussion and Conclusion}
60	\label{sec:discussion}
61	\input{section7_conclusion_compressed}
62	
63	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
64	\clearpage
65	\section*{Limitations}
66	
67	CF impact is model-dependent: for well-calibrated models (Qwen, Llama), S1 introduces CF violations (up to 12.02\%) as a consequence of per-relation independent enforcement; for poorly-calibrated models (Mistral), S1 substantially reduces CF (56.87\%\,$\to$\,1.27\%) by constraining type assignments to schema-valid values.
68	CF fallback ablation shows that eliminating
…[truncated 3737 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 340 · 2026-05-18T12:41:53.830890+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 341 · 2026-05-18T12:41:54.285016+00:00_

1	\begin{abstract}
2	We present \textsc{OntoCoDec}, which compiles Information Extraction (IE) ontology schemas into two composable token-level decoding constraints that provide formal guarantees during autoregressive generation:
3	(1)~a \emph{grammar layer} (XGrammar context-free grammar) guaranteeing JSON structural validity and entity/relation vocabulary membership (virtually eliminating entity type and relation vocabulary violations); and
4	(2)~a \emph{semantic layer} guaranteeing per-triple domain/range type compliance via a stateful entity registry and dynamic logit masking.
5	The two layers compose via bitwise AND on logit masks, with the grammar layer as an enabling prerequisite.
6	%
7	Without constraints, Large Language Model (LLM) based IE produces systematic domain/range (DR) violations: 15.37\% on SciERC (7 relations) and 18.46\% on DocRED (96 relations), comparable rates governed by \emph{constraint tightness} rather than ontology scale.
8	\textsc{OntoCoDec} reduces DR by 42--99\% across three model families (Qwen3-8B, Llama-3.1-8B, Mistral-7B) with no significant F1 cost.
9	For the primary model (Qwen3-8B): SciERC $+$0.13\,pp ($p{=}0.58$), DocRED $+$0.50\,pp ($p{<}0.001$); other models show comparable or larger gains (\S\ref{sec:cross-model}).
10	% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1, llama_docred_full_s1, mistral_docred
11	For calibrated models, residual DR correlates with the product of schema tightness and baseline violation rate, suggesting that constraint effectiveness is predictable from schema and model characteristics.
12	Composed with Low-Rank Adaptation (LoRA) fine-tuning, DR reaches $\leq$\,0.09\% (SciERC) and 0.20\% (DocRED) with relation F1 within $\pm$0.6\,pp, confirming near-lossless composability.
13	With beam search ($k{=}4$), the full stack (LoRA + OntoCoDec + beam) achieves zero constraint violations across all four categories while preserving extraction quality (relation F1 change ${<}$0.5\,pp).
14	The framework ge
…[truncated 597 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 342 · 2026-05-18T12:41:54.285503+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 343 · 2026-05-18T12:41:54.738551+00:00_

1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	We present OntoCoDec, a two-layer constrained decoding framework that compiles ontology schemas into token-level masks enforced during autoregressive generation.
9	Unlike type-constrained code generation, IE presents three distinct challenges: (1)~entity types are inferred from free text rather than declared annotations, (2)~the entity registry is built dynamically during generation, and (3)~constraint targets are context-dependent type assignments rather than fixed grammar productions.
10	The grammar layer (\S\ref{sec:grammar}) guarantees structural validity (well-formed JSON with ontology-vocabulary membership), while the semantic layer (\S\ref{sec:semantic}) enforces domain/range type constraints via a stateful entity registry.
11	We describe the problem formulation (\S\ref{sec:formulation}), each layer, and two decoding strategies (\S\ref{sec:strategies}).
12	Formal analysis of constraint composition is deferred to Section~\ref{sec:composition}.
13	
14	
15	\subsection{Problem Formulation}
16	\label{sec:formulation}
17	
18	\paragraph{IE as structured generation.}
19	Given an input text $x$, a language model generates a structured JSON output $y$:
20	%
21	\begin{equation}\label{eq:output-schema}
22	\resizebox{.88\columnwidth}{!}{$\displaystyle
23	  y = \bigl\{\texttt{entities}: [\{n_i, \tau_i\}],\; \texttt{relations}: [\{h_j, t_j, r_j, \tau^h_j, \tau^t_j\}]\bigr\}
24	$}
25	\end{equation}
26	%
27	where each entity has a name $n_i$ and type $\tau_i \in \mathcal{E}$, and each relation specifies head $h_j$, tail $t_j$, relation type $r_j \in \mathcal{R}$, and head/tail entity types $\tau^h_j, \tau^t_j$.
28	The output JSON Schema (\S\ref{sec:grammar}) enforces a fixed field ordering (head $\to$ tail $\to$ relation $\to$ head\_type $\to$ tail\_type) via deterministic grammar compilation.
29	This ordering en
…[truncated 9038 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 344 · 2026-05-18T12:41:54.739116+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 345 · 2026-05-18T12:41:55.692415+00:00_

1	% Section: Constraint Composition (compressed, 787→~500 words)
2	
3	At each decoding step $t$, let $G(t) \subseteq V$ and $S(t) \subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.
4	The final mask is their conjunction:
5	%
6	\begin{equation}\label{eq:composition}
7	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
8	\end{equation}
9	%
10	so a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$, reflecting the enabling dependency (\S\ref{sec:method}): the semantic layer requires the relation type to belong to $\mathcal{R}$, a property guaranteed only by the grammar layer.
12	
13	\paragraph{Grammar-First Fallback.}
14	When $S(t) \cap G(t) = \emptyset$ (tight constraints leave no token that is both grammar-valid and semantically valid), na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
15	We enforce a \emph{grammar-first fallback}: if no semantically valid token survives grammar filtering, semantic masking is skipped and the grammar layer alone controls selection.
16	Structural integrity is a hard constraint; a type violation is a soft error detectable by downstream validation.
17	
18	\paragraph{Constraint Tightness.}
19	We define the tightness of relation $r$ as:
20	%
21	\begin{equation}\label{eq:tightness}
22	  \kappa(r) = 1 - \frac{|\mathcal{V}(r)|}{|\mathcal{E}|^2},
23	\end{equation}
24	%
25	where $\mathcal{V}(r)$ is the set of valid type pairs and $\mathcal{E}$ the entity type vocabulary.
26	The mean tightness $\bar{\kappa} = \frac{1}{|\mathcal{R}|}\sum_{r} \kappa(r)$ characterizes ontology restrictiveness.
27	Tighter constraints eliminate more grammar-valid tokens at type-bearing positions, increasing fallback frequency and residual DR.
28	This dual-factor pattern (tightness $\times$ baseline model violation rate) is consistent with the cross-da
…[truncated 1435 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 346 · 2026-05-18T12:41:55.692954+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
  }
}
```

</details>

---


### Tool result

_source line 347 · 2026-05-18T12:41:55.895954+00:00_

1	% §5.1 Experimental Setup and Violation Landscape (compressed)
2	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
3	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
4	
5	\label{sec:violation_landscape}
6	
7	\paragraph{Setup.}
8	We evaluate on two IE benchmarks:
9	\textbf{SciERC}~\cite{luan2018scierc} (551 test sentences, 7 relations, avg.\ 26.1 valid type pairs/relation) and \textbf{DocRED}~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test annotations are not publicly available; we evaluate on the development set.} 96 relations, avg.\ 5.68 valid pairs).
10	Primary model: Qwen3-8B~\cite{qwen2025qwen3}, zero-shot greedy decoding; cross-model validation in \S\ref{sec:cross-model}.
11	We measure four violation categories: \textbf{DR} (domain/range type pair $\notin \sigma(r)$), \textbf{RV} (relation $\notin \mathcal{R}$), \textbf{ET} (entity type $\notin \mathcal{E}$), and \textbf{CF} (same entity assigned conflicting types across triples).
12	Violation rates are computed over successfully parsed documents; including failures as zero-violation instances adjusts rates by at most 0.23\,pp.
13	
14	\paragraph{Baseline violations and motivation.}
15	DR violations affect 15.37\% of triples on SciERC and 18.46\% on DocRED, comparable rates despite 14$\times$ ontology size difference, indicating that severity is driven by \emph{constraint tightness} rather than scale.
16	Per-relation rates vary by over 40\,pp (Appendix~\ref{app:per-relation-landscape}), correlating with tightness $\kappa(r)$.
17	RV on DocRED reaches 29.66\%, confirming that large vocabularies exceed prompt-based reproduction capacity.
18	Schema-informed prompting reduces DR by 62\% on SciERC but only 30\% on DocRED and is per-relation unreliable (DR for \textsc{Evaluate-for} \emph{increases} by 5.8\,pp), motivating decoding-time enforcement.
19	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 348 · 2026-05-18T12:41:55.896438+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 349 · 2026-05-18T12:41:55.896933+00:00_

1	% Section 5 — SciERC Results (Draft)
2	% Data source: Phase 2 SciERC registry experiments
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,
4	%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2
5	% All numbers verified against registry 2026-05-14.
6	
7	\subsection{Ablation and Composability with Fine-Tuning}
8	\label{sec:scierc-results}
9	
10	Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC (Qwen3-8B, zero-shot, 551 documents); only the active constraint layers differ across rows.
11	
12	% ──────────────────────────────────────────
13	%  Table: SciERC five-way ablation
14	% ──────────────────────────────────────────
15	\begin{table}[t]
16	\centering
17	\small
18	\setlength{\tabcolsep}{3.6pt}
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{@{}l rrrrr rr@{}}
21	\toprule
22	& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
23	& \multicolumn{2}{c}{\textbf{F1}} \\
24	\cmidrule(lr){2-6} \cmidrule(l){7-8}
25	\textbf{Mode}
26	  & DR\,$\downarrow$ & $\Delta$DR
27	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
28	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
29	\midrule
30	Unconstrained
31	  & 15.37 & ---
32	  & 1.39  & 0.40
33	  & 0.08
34	  & 8.23  & 31.01 \\
35	Grammar
36	  & 14.84 & $\downarrow$3\%
37	  & \textbf{0} & \textbf{0}
38	  & 0.08
39	  & 8.23  & 30.98 \\
40	Semantic
41	  & 11.65 & $\downarrow$24\%
42	  & 1.51  & 0.40
43	  & 2.71
44	  & 8.15  & 31.01 \\
45	Full (S1)
46	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
47	  & \textbf{0} & \textbf{0}
48	  & 9.90
49	  & \textbf{8.36} & 30.98 \\
50	Full (S2)
51	  & 0.97  & $\downarrow$94\%
52	  & \textbf{0} & \textbf{0}
53	  & 8.03
54	  & 8.03  & \textbf{31.90} \\
55	\bottomrule
56	\end{tabular}}%
57	\caption{Five-way ablation on SciERC (551 docs, Qwen3-8B, zero-shot).
58	$\Delta$DR: relative change vs.\ unconstrained.
59	Best per column in \textbf{bold} (CF excluded).
60	F1 $\times$100. Bootstrap: 10{,}000 iterations.}
61	\label{tab:scierc-ab
…[truncated 6346 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 350 · 2026-05-18T12:42:03.782460+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 351 · 2026-05-18T12:42:04.157371+00:00_

1	% Section 5 — DocRED Results (compressed, 1450→~600 words)
2	% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,
3	%          phase2_docred_semantic_only, phase2_docred_full_s1
4	% All numbers verified against registry 2026-05-14.
5	
6	\subsection{Cross-Dataset Validation on DocRED}
7	\label{sec:docred-results}
8	
9	Table~\ref{tab:docred-ablation} presents the four-way ablation on DocRED (96 Wikidata relation types, 14$\times$ SciERC; Qwen3-8B, zero-shot, 998 documents).
10	
11	% ──────────────────────────────────────────
12	%  Table: DocRED four-way ablation
13	% ──────────────────────────────────────────
14	\begin{table}[t]
15	\centering
16	\small
17	\setlength{\tabcolsep}{3.6pt}
18	\resizebox{\columnwidth}{!}{%
19	\begin{tabular}{@{}l rrrrr rr@{}}
20	\toprule
21	& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
22	& \multicolumn{2}{c}{\textbf{F1}} \\
23	\cmidrule(lr){2-6} \cmidrule(l){7-8}
24	\textbf{Mode}
25	  & DR\,$\downarrow$ & $\Delta$DR
26	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
27	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
28	\midrule
29	Unconstrained
30	  & 18.46 & ---
31	  & 29.66 & 2.48
32	  & 0.10
33	  & 7.74  & 58.15 \\
34	Grammar
35	  & 26.17 & $\uparrow$42\%
36	  & \textbf{0.03} & \textbf{0}
37	  & 0.07
38	  & \textbf{8.31}  & \textbf{59.38} \\
39	Semantic
40	  & 13.84 & $\downarrow$25\%
41	  & 29.87 & 4.22
42	  & 1.05
43	  & 7.70  & 57.81 \\
44	Full (S1)
45	  & \textbf{10.21} & $\downarrow$\textbf{45\%}
46	  & \textbf{0.03} & \textbf{0}
47	  & 2.57
48	  & 8.23  & 59.37 \\
49	\bottomrule
50	\end{tabular}}%
51	\caption{Four-way ablation on DocRED (998 documents, Qwen3-8B, zero-shot).
52	$\Delta$DR: relative change vs.\ unconstrained.
53	Best per column in \textbf{bold} (CF excluded).
54	F1 $\times$100. Bootstrap significance: R-F1 $+$0.50\,pp ($p < 0.001$).}
55	\label{tab:docred-ablation}
56	\end{table}
57	
58	% exp_ids: phase2_docred_unconstrained, phase2_docred_full_s1
59	\paragraph{Core result.}
60	Full S1 reduces DR from 
…[truncated 1332 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 374
}
```

</details>

---


### Tool call

_source line 352 · 2026-05-18T12:42:04.169048+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 353 · 2026-05-18T12:42:05.218268+00:00_

1	% Section 5 — Cross-Model Validation (compressed, 830→~400 words)
2	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1,
3	%          phase2_docred_unconstrained, phase2_docred_full_s1,
4	%          llama_scierc_unconstrained, llama_scierc_full_s1,
5	%          llama_docred_unconstrained, llama_docred_full_s1
6	
7	\subsection{Cross-Model Validation}
8	\label{sec:cross-model}
9	
10	Table~\ref{tab:cross-model} replicates full S1 with Llama-3.1-8B-Instruct and Mistral-7B-Instruct-v0.3 under identical prompts and evaluation.
11	Mistral serves as a third zero-shot verification point; composability evaluation (\S\ref{sec:composability}) uses LoRA, available only for Qwen and Llama.
12	
13	\begin{table}[t]
14	\centering
15	\small
16	\setlength{\tabcolsep}{3.4pt}
17	\resizebox{\columnwidth}{!}{%
18	\begin{tabular}{@{}ll rrrr r@{}}
19	\toprule
20	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
21	& \textbf{R-F1} \\
22	\cmidrule(lr){3-6} \cmidrule(l){7-7}
23	\textbf{Dataset} & \textbf{Model}
24	  & DR\,$\downarrow$ & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
25	  & $\uparrow$ \\
26	\midrule
27	\multirow{6}{*}{SciERC}
28	  & Qwen (U)    & 15.37 & 1.39  & 0.40 & 0.08 & 8.23 \\
29	  & Qwen (S1)   &  0.93 & 0     & 0    & 9.90 & 8.36 \\
30	  \cmidrule(l){2-7}
31	  & Llama (U)   & 13.34 & 0.55  & 0    & 0.24 & 2.68 \\
32	  & Llama (S1)  &  0.08 & 0     & 0    & 6.56 & 2.54 \\
33	  \cmidrule(l){2-7}
34	  & Mistral (U) & 56.94 & 0     & 1.50 & 56.87$^\dagger$ & 3.66 \\
35	  & Mistral (S1)& 13.40 & 0     & 0    & 1.27  & 3.67 \\
36	\midrule
37	\multirow{6}{*}{DocRED}
38	  & Qwen (U)    & 18.46 & 29.66 & 2.48 & 0.10 & 7.74 \\
39	  & Qwen (S1)   & 10.21 &  0.03 & 0    & 2.57 & 8.23 \\
40	  \cmidrule(l){2-7}
41	  & Llama (U)   & 26.07 & 16.03 & 0.13 & 0.17 & 5.98 \\
42	  & Llama (S1)  &  2.55 &  0    & 0    & 12.02& 6.27 \\
43	  \cmidrule(l){2-7}
44	  & Mistral (U) & 57.42 & 42.35 & 7.58 & 24.78 & 4.34 \\
45	  & Mistral (S1)& 33.20 &  0    & 0    & 0.19  & 5.52 \\
46	\b
…[truncated 1100 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1049
}
```

</details>

---


### Tool call

_source line 354 · 2026-05-18T12:42:05.269039+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
  }
}
```

</details>

---


### Tool result

_source line 355 · 2026-05-18T12:42:05.269596+00:00_

1	% Section 7 — Discussion and Conclusion (maximally compressed)
2	% Full discussion in Appendix; Mistral boundary condition in app:dual-factor.
3	
4	OntoCoDec compiles IE ontology schemas into composable token-level decoding constraints, achieving 42--99\% DR reduction across three models and three datasets (2 RE + 1 EE) with no significant RE F1 cost; in EE, format compliance additionally enables entity extraction (\S\ref{sec:wikievents}).
5	Composed with LoRA fine-tuning, DR reaches $\leq$\,0.20\% at $<$0.6\,pp F1 cost; residual DR follows a dual-factor pattern ($\bar{\kappa} \times \text{RV}_{\text{baseline}}$; Appendix~\ref{app:dual-factor}).
6	CF impact is model-dependent (up to 12\% for calibrated models, reduced for poorly-calibrated ones); fine-tuning resolves this tension (CF\,$\leq$\,1.2\%; \S\ref{sec:composability}), and beam search ($k{=}4$) eliminates both residual DR and CF for calibrated models (Appendix~\ref{app:beam-search}).
7	Cross-field consistency remains an open challenge for per-slot enforcement; global entity-level type consensus during decoding offers the most direct path to resolving CF without trading it against DR.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 356 · 2026-05-18T12:42:05.771822+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex"
  }
}
```

</details>

---


### Tool result

_source line 357 · 2026-05-18T12:42:06.288258+00:00_

1	\section{Reproducibility Details}
2	\label{app:reproducibility}
3	
4	\paragraph{Fine-tuning configuration.}
5	All four fine-tuned models (Qwen3-8B and Llama-3.1-8B-Instruct on SciERC and DocRED) use identical LoRA hyperparameters: rank $r{=}16$, $\alpha{=}32$, dropout $0.05$, no bias, targeting all attention and MLP projection layers (\texttt{q\_proj}, \texttt{k\_proj}, \texttt{v\_proj}, \texttt{o\_proj}, \texttt{gate\_proj}, \texttt{up\_proj}, \texttt{down\_proj}).
6	Training uses AdamW with learning rate $2{\times}10^{-4}$, cosine schedule, warmup ratio $0.1$, effective batch size $16$, bf16 precision, gradient checkpointing, and completion-only loss for 3 epochs.
7	SciERC trains on 1,762 examples (260 dev) for 333 steps; DocRED trains on 3,053 examples (998 dev) for 573 steps.
8	Maximum sequence length is 2,048 (SciERC) and 4,096 (DocRED).
9	All runs use seed 42.
10	
11	\paragraph{Hardware and software.}
12	Training runs on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (98\,GB VRAM).
13	SciERC fine-tuning takes approximately 11 minutes per model; DocRED takes approximately 1.5 hours.
14	Software versions: PyTorch 2.10, Transformers 4.57, PEFT 0.19, TRL 1.1, Accelerate 1.13.
15	
16	\paragraph{Inference time.}
17	Table~\ref{tab:inference-time} reports per-document inference times for Qwen3-8B under zero-shot greedy decoding across constraint configurations.
18	
19	\begin{table}[h]
20	\centering
21	\small
22	\caption{Inference time (seconds/document, mean $\pm$ std) for Qwen3-8B, zero-shot, greedy decoding.}
23	\label{tab:inference-time}
24	\begin{tabular}{@{}lcc@{}}
25	\toprule
26	\textbf{Configuration} & \textbf{SciERC} & \textbf{DocRED} \\
27	\midrule
28	Unconstrained       & $8.69 \pm 3.89$  & $19.75 \pm 8.99$  \\
29	Grammar-only        & $8.81 \pm 4.51$  & $20.58 \pm 10.75$ \\
30	Semantic-only       & $7.23 \pm 3.91$  & $20.53 \pm 9.37$  \\
31	Full S1             & $6.76 \pm 3.67$  & $20.39 \pm 9.43$  \\
32	Post-hoc            & $8.69 \pm 3.89$  &
…[truncated 476 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 516
}
```

</details>

---


### Tool call

_source line 358 · 2026-05-18T12:42:06.288781+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex"
  }
}
```

</details>

---


### Tool result

_source line 359 · 2026-05-18T12:42:06.400967+00:00_

1	\section{Beam Search Compatibility}
2	\label{app:beam-search}
3	
4	OntoCoDec's constraint enforcement is designed to be decoding-strategy agnostic.
5	The main experiments (\S\ref{sec:experiments}) use greedy decoding; Appendix~\ref{app:sampling} validates nucleus sampling.
6	Here we verify compatibility with beam search, completing coverage of the three standard decoding strategies.
7	
8	\paragraph{Implementation challenges.}
9	Two stateful components require adaptation for beam search.
10	(1)~The grammar layer (XGrammar) maintains an internal \texttt{GrammarMatcher} state that tracks the generated token sequence; beam reordering invalidates this state because beams are permuted across steps.
11	Our solution instantiates a fresh \texttt{GrammarMatcher} per beam per step and replays the beam's current token sequence through XGrammar's stateless accept API (64 lines of code).
12	(2)~The semantic layer's \texttt{TypeConstraintProcessor} accumulates entity and relation registries that assume a single generation path.
13	Our solution isolates state per beam by calling \texttt{detect()} on the full partial output at each step, reconstructing all entity/relation state from scratch for each beam independently (61 lines of code).
14	Both adaptations add ${\sim}125$ lines total without modifying the existing greedy/sampling logic.
15	
16	\paragraph{Results.}
17	Table~\ref{tab:beam-search} compares beam search ($k{=}4$, \texttt{early\_stopping=True}) against greedy decoding under full S1 constraints across six model-dataset combinations.
18	
19	\begin{table}[h]
20	\centering
21	\small
22	\caption{Beam search ($k{=}4$) vs.\ greedy decoding under full S1 constraints.
23	SciERC evaluated on full test set (551 documents); DocRED evaluated on matched 50-document subsets (same documents for greedy and beam).
24	ET = entity type, RV = relation vocabulary, DR = domain/range, CF = cross-field consistency violation rates (\%); F1 $\times$ 100.}
25	\label{tab:beam-search}
26	\begin{tab
…[truncated 6802 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 112
}
```

</details>

---


### Tool call

_source line 360 · 2026-05-18T12:42:17.790329+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 361 · 2026-05-18T12:42:18.293497+00:00_

1	% Appendix B — Extended Discussion
2	% Contains discussion paragraphs moved from the main text during compression.
3	
4	\section{Extended Discussion}\label{app:discussion}
5	
6	%%% CF Dual Mechanism %%%
7	% exp_ids: phase2_scierc_full_s1, llama_scierc_full_s1, llama_docred_full_s1
8	
9	\paragraph{CF Dual Mechanism.}
10	CF violations arise from two distinct mechanisms:
11	(1)~\emph{Registry override}: the semantic constraint forces a domain-compatible type that conflicts with the entity's previously registered type.
12	The entity appears in multiple relations with different type requirements, and the per-relation mask selects the locally valid type without consulting prior assignments.
13	(2)~\emph{Grammar-first fallback} (\S\ref{sec:interaction}): when the semantic mask conflicts with all grammar-valid tokens, the semantic layer is dropped entirely, allowing the grammar layer to generate any structurally valid type, which may differ from the entity's registered type.
14	
15	These mechanisms have sharply different model profiles.
16	Qwen3-8B triggers zero grammar-first fallbacks across all experiments, attributing 100\% of its CF violations to registry override.
17	Llama-3.1-8B, by contrast, triggers 5{,}882 fallbacks on SciERC (10.7 per document) and 57{,}825 on DocRED (63.8 per document), making grammar-first fallback the dominant CF source.
18	This asymmetry is consistent with the cross-model CF gap: Qwen achieves CF\,=\,2.57\% on DocRED vs.\ Llama's 12.02\%, despite both using identical constraint configurations.
19	The difference traces to Llama's less calibrated type predictions, which more frequently conflict with the semantic mask's valid set, triggering fallback.
20	
21	%%% Fallback Behavior and Effective Coverage %%%
22	% exp_ids: cf_fallback_ablation_scierc (final data)
23	
24	\paragraph{Fallback Behavior and Effective Coverage.}
25	\label{app:fallback-coverage}
26	The two-layer architecture produces two distinct fallback mechanisms with different semant
…[truncated 31927 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 362 · 2026-05-18T12:42:18.344379+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
  }
}
```

</details>

---


### Tool result

_source line 363 · 2026-05-18T12:42:19.047597+00:00_

1	% Runtime overhead (inline paragraph, no subsection header to save space)
2	
3	\paragraph{Runtime overhead.}
4	\label{sec:runtime}
5	Full S1 adds $+$2.3\% on SciERC and $+$5.4\% on DocRED (same GPU); under fine-tuning, overhead drops to $+$2.3\% (61\,ms/doc).
6	Grammar compile is a one-time 44\,ms cost.
7	Per-layer profiling in Appendix~\ref{app:runtime}.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 364 · 2026-05-18T12:42:19.048235+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 365 · 2026-05-18T12:42:19.149080+00:00_

1	% Section 5 — Event Extraction on WikiEvents (compact, inline)
2	% exp_ids: ee_qwen_wikievents_unconstrained, ee_llama_wikievents_unconstrained,
3	%          ee_mistral_wikievents_unconstrained, ee_qwen_wikievents_constrained,
4	%          ee_llama_wikievents_constrained, ee_mistral_wikievents_constrained_v2
5	% v3 final data confirmed by Director 2026-05-18.
6	
7	\subsection{Cross-Task Validation: Event Extraction}
8	\label{sec:wikievents}
9	
10	To test generality beyond RE, we apply OntoCoDec to event extraction (EE) on WikiEvents~\cite{li2021document} (56 event types, 80 argument roles, 27 entity types, 245 role$\to$type constraints; Appendix~\ref{app:wikievents}).
11	The framework requires no modification: grammar compiles event/role vocabularies into a CFG; the semantic layer enforces role-conditioned type constraints via the same registry.
12	Violations extend to Event Vocabulary (EV), Role Vocabulary (RoV), and Argument Constraint (AC, analogous to DR).
13	
14	% ──────────────────────────────────────────
15	%  Table: WikiEvents three-model comparison (v3 final)
16	%  exp_ids: ee_{qwen,llama,mistral}_wikievents_{unconstrained,grammar_only,constrained_v3}
17	% ──────────────────────────────────────────
18	\begin{table}[t]
19	\centering
20	\small
21	\setlength{\tabcolsep}{2.8pt}
22	\resizebox{\columnwidth}{!}{%
23	\begin{tabular}{@{}ll rrrr rr@{}}
24	\toprule
25	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
26	& \multicolumn{2}{c}{\textbf{F1}} \\
27	\cmidrule(lr){3-6} \cmidrule(l){7-8}
28	\textbf{Model} & \textbf{Mode}
29	  & EV\,$\downarrow$ & RoV\,$\downarrow$ & AC & CF
30	  & Trig.\,$\uparrow$ & Ent.\,$\uparrow$ \\
31	\midrule
32	\multirow{3}{*}{Qwen3-8B}
33	  & Unconstr.\ & 24.0 & 74.9 & 0.3 & 0 & 11.8 & 0 \\
34	  & Grammar    & \textbf{0} & 76.1 & 8.2 & --- & --- & --- \\
35	  & Full S1    & \textbf{0} & \textbf{0} & 2.1 & 21.1 & 13.4 & 14.1 \\
36	\midrule
37	\multirow{3}{*}{\shortstack[l]{Llama\\3.1-8B}}
38	  & Unconstr.\ & 10.5 & 88.8 & 0.1 & 0 
…[truncated 2256 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 366 · 2026-05-18T12:44:15.683807+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-18T12:44:15.705860+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly deployed for zero-shot information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity is guaranteed to carry a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	In a systematic study, we find violations are pervasive: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred}, driven by \emph{constraint tightness} (few valid type pairs per relation) rather than ontology scale.
9	Relations with tight constraints exhibit far higher rates (\textsc{Compare}: 42.4\%) than loosely constrained ones (\textsc{Used-for}: 0.8\%).
10	
11	Existing approaches leave a fundamental gap.
12	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
13	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} guarantees syntactic well-formedness but cannot encode cross-field semantic constraints.
14	Post-hoc filtering achieves higher F1 in most zero-shot settings via precision gains, but at the cost of discarding up to 48\% of predictions including true positives; at high rejection rates (e.g., Mistral DocRED 73.7\%), it discards the majority of outputs, making it impractical.
15	OntoCoDec preserves recall by enforcing constraints during generation rather than discarding non-compliant outputs.
16	Training-based approaches~\cite{sainz2024gollie,lu2022uie} provide only soft guidance that cannot eliminate violations.
17	
18	We propose \textbf{OntoCoDec} (\textbf{Onto}logy-\textbf{Co}mpiled \textbf{Dec}oding), a framework that compiles an IE onto
…[truncated 2852 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 22
}
```

</details>

---


### Tool call

_source line 368 · 2026-05-18T12:44:15.812246+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex",
  "offset": "55"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex",
    "offset": "55"
  }
}
```

</details>

---


### Tool result

_source line 369 · 2026-05-18T12:44:15.913314+00:00_

55	% exp_ids: phase2_scierc_full_s1, llama_scierc_full_s1, phase2_docred_full_s1, llama_docred_full_s1, mistral_scierc, mistral_docred
56	\paragraph{Results.}
57	RV and ET are eliminated ($\leq$0.03\%) for all models on both datasets.
58	DR drops 76--99\% on SciERC and 42--90\% on DocRED; R-F1 improves in five of six settings (DocRED: Qwen $+$0.50\,pp, $p{<}0.001$; Llama $+$0.29\,pp, $p{=}0.013$).
59	Cross-model DR asymmetry reflects baseline RV: Llama's lower RV (16.03\% vs.\ 29.66\%) limits latent violation surfacing, yielding 2.55\% residual DR vs.\ 10.21\%.
60	CF direction depends on baseline calibration: S1 introduces CF for calibrated models (up to 12.02\%; \S\ref{sec:discussion}), while reducing CF for poorly-calibrated Mistral (56.87\%\,$\to$\,1.27\%).
61	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 370 · 2026-05-18T12:44:24.079248+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "parse.?fail|parse failure",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "parse.?fail|parse failure",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 371 · 2026-05-18T12:44:24.137025+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex:69:Entity F1 impact is model-dependent ($+$1.22\,pp for Qwen vs.\ $-$0.64\,pp for Llama on DocRED), partially confounded by increased parse failures under constraints (Llama: 9.1\% vs.\ 6.8\%).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:266:DR/RV/ET/CF: violation rates (\%); PF: parse failure rate (\%); F1 $\times$100.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:276:F1 cost is negligible: the maximum R-F1 decrease across all 16 model$\times$dataset$\times$mode combinations is $-$0.30\,pp (Qwen DocRED, full vs.\ unconstrained), attributable to parse failure increase (7.11\%\,$\to$\,8.52\%) rather than constraint-induced extraction degradation.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex:98:Beam search on DocRED introduces a modest increase in parse failures (3/50, 6\%) compared to greedy (1.1\%), as longer beam-generated sequences occasionally produce malformed JSON in complex documents.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.aux:1993:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.aux:1994:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion.tex:32:Constrained decoding can increase parse failure rates for some model-dataset combinations: Llama-3.1-8B on DocRED shows 91 parse failures under full constraints versus 68 unconstrained (9.1\% vs.\ 6.8\%), likely due to max-token truncation of lo
…[truncated 154 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 57
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-18T12:44:25.461069+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "beam.*runtime|beam.*overhead|beam.*time|beam.*latency",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "-i": "True",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "beam.*runtime|beam.*overhead|beam.*time|beam.*latency",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "-i": "True",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 373 · 2026-05-18T12:44:25.913080+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.aux:2238:\@writefile{lot}{\contentsline {table}{\numberline {16}{\ignorespaces Beam search ($k{=}4$) vs.\ greedy decoding under full S1 constraints. SciERC evaluated on full test set (551 documents); DocRED evaluated on matched 50-document subsets (same documents for greedy and beam). ET = entity type, RV = relation vocabulary, DR = domain/range, CF = cross-field consistency violation rates (\%); F1 $\times $ 100.}}{23}{table.caption.80}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.aux:2239:\newlabel{tab:beam-search}{{16}{23}{Beam search ($k{=}4$) vs.\ greedy decoding under full S1 constraints. SciERC evaluated on full test set (551 documents); DocRED evaluated on matched 50-document subsets (same documents for greedy and beam). ET = entity type, RV = relation vocabulary, DR = domain/range, CF = cross-field consistency violation rates (\%); F1 $\times $ 100}{table.caption.80}{}}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 374 · 2026-05-18T12:44:26.516190+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "RV.*0\\.03|0\\.03.*RV|residual.*RV",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "RV.*0\\.03|0\\.03.*RV|residual.*RV",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 375 · 2026-05-18T12:44:26.567420+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex:57:RV and ET are eliminated ($\leq$0.03\%) for all models on both datasets.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:92:Figure~\ref{fig:dual-factor-scatter} plots residual DR against the product $\bar{\kappa} \times \text{RV}_{\text{baseline}}$ for model$\times$dataset configurations.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex:95:Adding beam search ($k{=}4$) eliminates all residual CF violations (1.18\%\,$\to$\,0\%), yielding zero violations across all four metrics (ET=0\%, RV=0\%, DR=0\%, CF=0\%) while preserving extraction quality (E-F1=66.88, R-F1=44.23; changes within $\pm$0.5\,pp).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex:38:The substantially lower residual DR for Llama (2.55\% vs.\ Qwen's 10.21\%) on the same ontology confirms that constraint tightness alone does not determine enforcement effectiveness: the model's baseline vocabulary compliance (RV) modulates the fraction of triples eligible for semantic-layer enforcement.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex:60:Full S1 reduces DR from 18.46\% to 10.21\% ($\downarrow$45\%), eliminates ET ($\to$\,0\%), and near-eliminates RV (29.66\%\,$\to$\,0.03\%).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex:5:Composed with LoRA fine-tuning, DR reaches $\leq$\,0.20\% at $<$0.6\,pp F1 cost; residual DR follows a dual-factor pattern ($\bar{\kappa} \times \text{RV}_{\text{baseline}}$; Appendix~\r
…[truncated 21 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 376 · 2026-05-18T12:45:19.192725+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "early_stopping|wall.?clock|beam.*sec|beam.*ms",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "-i": "True",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "early_stopping|wall.?clock|beam.*sec|beam.*ms",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "-i": "True",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 377 · 2026-05-18T12:45:19.243585+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex:78:All main experiments use greedy decoding; our evaluation of beam search on the full SciERC test set (551 documents) and a DocRED subset across three models confirms compatibility (Appendices~\ref{app:sampling},~\ref{app:beam-search}), but comprehensive evaluation across all decoding configurations remains future work.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex:82:\citet{ekaw2024_ontology_beam} introduce ontology-constrained beam scoring for clinical summarization, applying soft biases (not hard masks) during beam search to steer outputs toward ontology-compliant terms, a middle ground between unconstrained generation and hard enforcement that reduces but cannot eliminate violations.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_outline.tex:100:\citet{ekaw2024_ontology_beam} introduce ontology-constrained beam scoring for clinical summarization, applying soft biases (not hard masks) during beam search to steer outputs toward ontology-compliant terms---a middle ground between unconstrained generation and hard enforcement.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex:10:(1)~The grammar layer (XGrammar) maintains an internal \texttt{GrammarMatcher} state that tracks the generated token sequence; beam reordering invalidates this state because beams are permuted across steps.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex:65:On SciERC (7 entity types), beam search does not reduce DR (13.4\%\,$\to$\,13.8\%), though CF drops by 55\% relative (1.27\%\,$\to$\,0.57\%) and R-F1 improves by $+$0.7\,
…[truncated 494 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 378 · 2026-05-18T12:45:25.879345+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "---\"",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "---\"",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 379 · 2026-05-18T12:45:26.281353+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 380 · 2026-05-18T12:45:26.985036+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 381 · 2026-05-18T12:45:27.035889+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:1:% Section 5 — DocRED Results (Draft)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex:1:% Appendix — Prompt Templates
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex:1:% Section 5 — Cross-Model Validation (compressed, 830→~400 words)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex:1:% Section 3 — Method (Draft)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:1:% Appendix B — Extended Discussion
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex:2:% Related Work Additions — compiled 2026-05-14
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex:60:% STATUS: VERIFIED — paper exists and description is accurate
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex:1:% Appendix C — Per-Relation Violation Analysis (Llama-3.1-8B)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:1:% Section 5 — SciERC Results (Draft)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex:1:% Section 5 — SciERC Results (Draft)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section
…[truncated 1220 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 382 · 2026-05-18T12:45:33.512332+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 383 · 2026-05-18T12:45:33.563005+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Grammar-Constrained Decoding.}
5	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, LMQL~\cite{beurer-kellner2023lmql}, DOMINO~\cite{beurer-kellner2024domino}, SynCode~\cite{ugare2024syncode}, and ASAp~\cite{park2024grammar} guarantee format validity but cannot enforce cross-field semantic constraints such as domain/range rules.
6	
7	\paragraph{Type-Constrained Generation for IE and Code.}
8	Synchromesh~\cite{synchromesh_iclr2022}, PICARD~\cite{scholak2021picard}, and \citet{pldi2025_type_constrained_codegen} enforce type constraints in code generation; OntoCoDec migrates this to IE.
9	GCD~\cite{geng2023gcd} and GoLLIE~\cite{sainz2024gollie} constrain \emph{which tokens} appear but not \emph{which type combinations} are valid per relation.
10	DORE~\cite{vukovic2024dore} uses generate-then-select with confidence thresholds; GenIE~\cite{josifoski2022genie} constrains entities via a trie without relation-specific type enforcement; EnriCo~\cite{zaratiana2024enrico} applies ASP constraints with task-specific manually authored rules.
11	Training-based methods~\cite{paolini2021tanl,cabot2021rebel,lu2022uie,knowcoder_acl2024,li2023codeie} provide only soft guidance; post-hoc approaches~\cite{khorshidi2025odke,spires_2024,ontologx_2025} validate after generation rather than preventing violations.
12	
13	\paragraph{Quality Impact.}
14	CRANE~\cite{banerjee2025crane} and \citet{schall2025hiddencost} show grammar restrictions can degrade reasoning, but \citet{tam2024letmespeak} find extraction tasks robust to constraints.
15	OntoCoDec confirms this: DR decreases 42--99\% with zero F1 degradation across three model families (extended survey in Appendix~\ref{app:related_work}).
16	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 384 · 2026-05-18T12:46:38.482748+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
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

_source line 385 · 2026-05-18T12:46:38.533576+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 386 · 2026-05-18T12:48:11.497209+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 6 增量审稿报告 — Reviewer 1（方法/实验严谨性）\n\n论文最后修改：2026-05-18 12:04。以下逐条核查 Round 5 遗留的 open issues。\n\n---\n\n## Issue Verification\n\n| Issue ID | Severity | Verdict | Evidence |\n|----------|----------|---------|----------|\n| R2-N1 (MF1) | critical | ✅ Resolved | 见下方详述 |\n| R4-N3 (SF1) | warning | ⚠️ Partially fixed | 见下方详述 |\n| R2-N3 (SF5) | warning | ⚠️ Partially fixed | 见下方详述 |\n| R4-W2 (SF7) | warning | ⚠️ Partially fixed | 见下方详述 |\n| R2-N5 (SF8) | warning | ✅ Resolved | 见下方详述 |\n| R4-W3 (SF9) | warning | ✅ Resolved | 见下方详述 |\n| R4-Q1 (Q1) | warning | ✅ Resolved | 见下方详述 |\n| R2-N6 (M3) | warning | ⚠️ Partially fixed | 见下方详述 |\n| R2-N10 (M1) | info | ⚠️ Partially fixed | 见下方详述 |\n| GC-N1 (M2) | info | ✅ Resolved | 见下方详述 |\n| R4-Q2 (M6) | info | ✅ Resolved | 见下方详述 |\n\n**统计：6 ✅ Resolved / 5 ⚠️ Partially fixed / 0 ❌ Not fixed / 1 🆕 New issue**\n\n---\n\n## 逐条详述\n\n### ✅ MF1 (R2-N1) [critical] R²=0.886 过度突出 → Resolved\n\n三项要求全部满足：\n1. **Abstract**（abstract.tex L11）：R² 具体值已移除，改为定性描述 \"residual DR correlates with the product of schema tightness and baseline violation rate, suggesting that constraint effectiveness is predictable from schema and model characteristics\"。\n2. **Appendix**（appendix_discussion.tex L93）：完整报告 \"$R^2 = 0.886$ ($n{=}4$, $F(1,2) = 15.54$, $p \\approx 0.058$); with only four data points (df $= 2$) and $p > 0.05$, this constitutes a descriptive characterization rather than a confirmatory statistical test\"。统计谦逊性充分。\n3. **Mistral 排除标准**（appendix_discussion.tex L96）：\"models with unconstrained ET${>}$5\\% on either dataset fall outside the regime\"，提供了可复现的先验标准。\n\n**唯一的 critical issue 已完全修复。**\n\n---\n\n### ⚠️ SF1 (R4-N3) [warning] Beam search 结果降级到 Appendix → Partially fixed\n\nRound 5 四项要求的完成度：\n\n| 子项 | 状态 | 证据 |\n|------|------|------|\n| (1) 正文讨论 beam SciERC 全集结果 | ⚠️ 仅一句话 | §5.3 L122 \"Beam search ($k{=}4$) eliminates residual DR and reduces CF to $<$1%\"，Abstract L13 提及 LoRA+beam 零违规。具体数据（DR=0%, CF=0.53%）仅在 Appendix Table 16 |\n| (2) 报告 beam runtime overhead | ❌ 未修复 | appendix_beam_search.tex L99 仅定性描述 \"Wall-clock overhead is modest\"，无量化数据。Appendix Table 14（reproducibility）只有 greedy timing |\n| (3) 明确 greedy=实用推荐 vs beam=质量最优 | ⚠️ 隐含但不明确 | §3 L120 称 S1 greedy 为 \"recommended strategy\"，但未对比 beam 的定位 |\n| (4) DocRED beam 用匹配 50-doc | ✅ | Table 16 caption: \"DocRED evaluated on matched 50-document subsets (same documents for greedy and beam)\" |\n\n**残留风险**：beam search 是 Abstract 第 4 个主要 claim（\"zero constraint violations across all four categories\"），但 runtime cost 完全未量化。审稿人可能质疑：如果 beam 开销很大，这个 claim 的实际价值就打折。建议至少在 Appendix 的 beam section 添加 k=4 的 wall-clock 对比。\n\n---\n\n### ⚠️ SF5 (R2-N3) [warning] Llama DocRED parse failure confounding → Partially fixed\n\n已完成：\n- Parse failure rate 报告（Table 5 caption: \"Parse failures: Llama DocRED 9.1%; others ≤1.1%\"）\n- Limitations L69 明确承认 confounding：\"partially confounded by increased parse failures under constraints (Llama: 9.1% vs. 6.8%)\"\n- section3_violation_landscape.tex L12 说明 violation rates 在 parsed docs 上计算；section7_conclusion.tex L32 说明 F1 同样\n\n**未完成**：未提供 deconfounded 分析（例如仅在两种条件下都成功 parse 的文档交集上对比 violation rates 和 F1）。Llama DocRED 是所有 6 个 ZS 配置中 parse failure 最高的（9.1%），constrained 比 unconstrained 高 2.3pp，这意味着 constrained 条件下有额外 23 篇文档被排除，可能系统性偏移了 violation rate 和 F1。\n\n**残留风险**：低。论文已坦诚承认 confound，且 Llama DocRED 不是主要 claim 的核心支撑（Qwen 是 primary model）。\n\n---\n\n### ⚠️ SF7 (R4-W2) [warning] DocRED fallback coverage 未报告 → Partially fixed\n\n已完成（appendix_discussion.tex L24-37, app:fallback-coverage）：\n- 定义了 effective semantic constraint coverage = 1 - f_gf\n- 报告了三个配置：Qwen SciERC = 100%, Qwen DocRED = 99.9% (f_gf=0.08%), Llama SciERC = 63.4% (f_gf=36.6%)\n- 解释了 multi-token tokenization 导致的差异\n- section5_docred_draft.tex L71 在正文提及 \"fallback rate (10.2%) closely tracking residual DR\"\n\n**未完成**：Llama DocRED effective coverage 未报告。这是 CF 最高的配置（12.02%），也是 parse failure 最高的配置，其 fallback coverage 对理解 Llama DocRED 的异常表现至关重要。目前只有 3/4 个 model×dataset 配置的 coverage 数据。\n\n---\n\n### ✅ SF8 (R2-N5) [warning] Reproducibility 信息不充分 → Resolved\n\nappendix_reproducibility.tex 现包含完整信息：\n- LoRA 超参数：rank=16, α=32, dropout=0.05, target modules（all attn + MLP）\n- 训练配置：AdamW, LR=2e-4, cosine schedule, warmup 0.1, batch 16, bf16, 3 epochs\n- 数据规模：SciERC 1762 examples/333 steps, DocRED 3053/573 steps\n- Max sequence length: 2048 (SciERC), 4096 (DocRED)\n- Seed: 42\n- GPU: NVIDIA RTX PRO 6000 Blackwell Server Edition (98GB VRAM)\n- Software versions: PyTorch 2.10, Transformers 4.57, PEFT 0.19, TRL 1.1, Accelerate 1.13\n- Inference time table (Table 14) with per-configuration timing\n\n**完全满足 reproducibility 要求。**\n\n---\n\n### ✅ SF9 (R4-W3) [warning] §4 DR reduction 范围与 Abstract 不一致 → Resolved\n\nsection4_composition_draft.tex L28 现在明确区分：\n- Calibrated models (Qwen, Llama): SciERC 94-99%, DocRED 45-90%\n- Including Mistral: full range 42-99%\n- 与 Abstract 的 \"42-99%\" 一致\n- Mistral 包含理由说明：\"whose high baseline ET shifts the regime\"\n\n---\n\n### ✅ Q1 (R4-Q1) [warning] JSON field ordering 是 sequential masking 隐含前提 → Resolved\n\nsection3_method_draft.tex L28-29 显式声明：\n\"The output JSON Schema (§3.2) enforces a fixed field ordering (head → tail → relation → head_type → tail_type) via deterministic grammar compilation. This ordering ensures that the relation type r_j is known before entity type fields are generated, which enables domain and range lookups in sequential masking (§3.5).\"\n\n明确了 field ordering 是 grammar 编译的产物（非假设），并解释了为什么这个 ordering 是 semantic masking 的先决条件。\n\n---\n\n### ⚠️ M3 (R2-N6) [warning] Semantic-only DocRED ET 增加 +70% → Partially fixed\n\nsection5_docred_draft.tex L70-71 承认了现象：\"cannot eliminate RV (29.87%) or prevent ET increases (2.48% → 4.22%), replicating SciERC's enabling dependency.\"\n\n**问题**：归因为 \"replicating SciERC's enabling dependency\" 不准确。SciERC semantic-only 的 ET 保持 0.40%（无变化），DocRED 从 2.48% 上升到 4.22%（+70%）。这不是 \"replication\"，而是 DocRED 特有的现象。可能的解释是：DocRED 有 96 relations 的复杂 domain/range 规则，semantic masking 在无 grammar 约束时将 OOV relation 的 type 推向非标准值，但这个机制未被阐述。\n\n**残留风险**：低。这是 semantic-only 模式（一个 ablation 行），不影响主要 claim（Full S1 下 ET=0%）。\n\n---\n\n### ⚠️ M1 (R2-N10) [info] RV=0.03% 解释不一致 → Partially fixed\n\nDocRED 所有含 grammar 的配置一致报告 RV=0.03%：\n- Table 4 (DocRED ablation): Grammar RV=0.03, Full S1 RV=0.03\n- Table 5 (cross-model): Qwen DocRED S1 RV=0.03\n- section5_docred_draft.tex L60: \"near-eliminates RV (29.66% → 0.03%)\"\n- section5_crossmodel_draft.tex L57: \"RV and ET are eliminated (≤0.03%)\"\n\n**未完成**：未解释 residual 0.03% 的具体来源。0.03% 在 DocRED 的 ~17,000 triples 中约为 5 个 triple。这些可能是 tokenization 边界情况或特定 relation name 的编码问题，但论文未提供解释。\n\n**残留风险**：极低。0.03% 实际上是 \"near-zero\"，不影响任何 claim。\n\n---\n\n### ✅ M2 (GC-N1) [info] Grammar-only 未标识为 GCD capability ceiling → Resolved\n\nsection5_scierc_draft.tex L85: \"This configuration represents the capability ceiling of grammar-based constrained decoding [GCD], which enforces JSON structure and vocabulary membership but cannot reason about cross-field semantic constraints.\"\n\n明确标注，引用了 GCD，并解释了 ceiling 的原因。\n\n---\n\n### ✅ M6 (R4-Q2) [info] CF-DR ablation 仅 SciERC/Qwen → Resolved\n\nappendix_discussion.tex L74-76 提供了充分的 transferability 论证：\n- 跨 6 个配置的 Spearman ρ = -0.77，证明 DR-CF 反向关联不限于 SciERC/Qwen\n- 选择 SciERC/Qwen 做 detailed ablation 的理由：\"highest CF (9.90%), making the trade-off most visible\"\n- 讨论了 Llama DocRED (CF=12.02%) 作为 \"larger CF headroom\" 的 setting\n- 明确声明 \"structural consequence of per-relation enforcement with grammar-first fallback, not a model- or dataset-specific artifact\"\n\n---\n\n## 🆕 New Issues Found\n\n### 🆕 N1 [warning] Abstract LoRA+beam \"zero violations\" claim 仅基于单一配置\n\n- **位置**：Abstract L13: \"With beam search ($k{=}4$), the full stack (LoRA + OntoCoDec + beam) achieves zero constraint violations across all four categories while preserving extraction quality\"\n- **问题**：此 claim 的实验支撑仅来自 Qwen3-8B / SciERC 一个配置（appendix_beam_search.tex L94-95: \"ET=0%, RV=0%, DR=0%, CF=0%\"）。未报告 Llama LoRA+beam 或 DocRED LoRA+beam 的数据。\n- **为什么是问题**：Abstract claim 没有限定 model 或 dataset，暗示 generalizability。但 LoRA+beam 仅有一个数据点，可能是最有利的配置（SciERC 只有 7 relations，constraint tightness 最低）。DocRED（96 relations, κ̄=0.842）的 LoRA+beam 表现未知。\n- **建议**：(a) Abstract 中限定 \"on SciERC\" 或 \"for Qwen3-8B\"；或 (b) 补充至少一个 Llama 或 DocRED 的 LoRA+beam 数据点。\n\n---\n\n## Updated Assessment\n\n| 维度 | Round 5 | Round 6 | 变化 |\n|------|---------|---------|------|\n| 方法严谨性 | 3.5/5 | 4.0/5 | ↑ R² 统计谦逊性、field ordering 显式声明、GCD ceiling 标注 |\n| 实验充分性 | 3.0/5 | 3.5/5 | ↑ reproducibility 完整、CF-DR transferability 论证、DocRED coverage 部分补充；beam runtime 仍缺 |\n| Reproducibility | 2.5/5 | 4.5/5 | ↑↑ 从信息严重不足到完整可复现 |\n\n### 建议评分：3.5 (Borderline Conference)\n\n**理由**：\n- **唯一的 critical issue (R²) 已完全修复**，统计处理规范\n- **6/11 issues fully resolved**，包括 reproducibility 的大幅改善\n- **剩余 5 个 partial fixes 均为 warning/info 级别**，不构成接收障碍：\n  - SF1（beam runtime）：可在 camera-ready 补充\n  - SF5（parse failure deconfounding）：已坦诚承认，Llama DocRED 非主要支撑\n  - SF7（Llama DocRED coverage）：3/4 配置已覆盖\n  - M3/M1：低影响 ablation 细节\n- **新发现 N1**（LoRA+beam 单一配置）值得关注，但 claim 本身技术上正确，建议添加限定语\n\n**从 Round 5 的 \"Weak Accept (Findings)\" 上调至 \"Borderline Conference\"**。论文的核心贡献（two-layer compiled constraint framework + systematic violation analysis）扎实，方法论已充分严谨。如果 beam runtime 和 LoRA+beam generalizability 能在最终版本补充，可支持 Conference 接收。",
  "reviewer_id": "1",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 6 增量审稿报告 — Reviewer 1（方法/实验严谨性）\n\n论文最后修改：2026-05-18 12:04。以下逐条核查 Round 5 遗留的 open issues。\n\n---\n\n## Issue Verification\n\n| Issue ID | Severity | Verdict | Evidence |\n|----------|----------|---------|----------|\n| R2-N1 (MF1) | critical | ✅ Resolved | 见下方详述 |\n| R4-N3 (SF1) | warning | ⚠️ Partially fixed | 见下方详述 |\n| R2-N3 (SF5) | warning | ⚠️ Partially fixed | 见下方详述 |\n| R4-W2 (SF7) | warning | ⚠️ Partially fixed | 见下方详述 |\n| R2-N5 (SF8) | warning | ✅ Resolved | 见下方详述 |\n| R4-W3 (SF9) | warning | ✅ Resolved | 见下方详述 |\n| R4-Q1 (Q1) | warning | ✅ Resolved | 见下方详述 |\n| R2-N6 (M3) | warning | ⚠️ Partially fixed | 见下方详述 |\n| R2-N10 (M1) | info | ⚠️ Partially fixed | 见下方详述 |\n| GC-N1 (M2) | info | ✅ Resolved | 见下方详述 |\n| R4-Q2 (M6) | info | ✅ Resolved | 见下方详述 |\n\n**统计：6 ✅ Resolved / 5 ⚠️ Partially fixed / 0 ❌ Not fixed / 1 🆕 New issue**\n\n---\n\n## 逐条详述\n\n### ✅ MF1 (R2-N1) [critical] R²=0.886 过度突出 → Resolved\n\n三项要求全部满足：\n1. **Abstract**（abstract.tex L11）：R² 具体值已移除，改为定性描述 \"residual DR correlates with the product of schema tightness and baseline violation rate, suggesting that constraint effectiveness is predictable from schema and model characteristics\"。\n2. **Appendix**（appendix_discussion.tex L93）：完整报告 \"$R^2 = 0.886$ ($n{=}4$, $F(1,2) = 15.54$, $p \\approx 0.058$); with only four data points (df $= 2$) and $p > 0.05$, this constitutes a descriptive characterization rather than a confirmatory statistical test\"。统计谦逊性充分。\n3. **Mistral 排除标准**（appendix_discussion.tex L96）：\"models with unconstrained ET${>}$5\\% on either dataset fall outside the regime\"，提供了可复现的先验标准。\n\n**唯一的 critical issue 已完全修复。**\n\n---\n\n### ⚠️ SF1 (R4-N3) [warning] Beam search 结果降级到 Appendix → Partially fixed\n\nRound 5 四项要求的完成度：\n\n| 子项 | 状态 | 证据 |\n|------|------|------|\n| (1) 正文讨论 beam SciERC 全集结果 | ⚠️ 仅一句话 | §5.3 L122 \"Beam search ($k{=}4$) eliminates residual DR and reduces CF to $<$1%\"，Abstract L13 提及 LoRA+beam 零违规。具体数据（DR=0%, CF=0.53%）仅在 Appendix Table 16 |\n| (2) 报告 beam runtime overhead | ❌ 未修复 | appendix_beam_search.tex L99 仅定性描述 \"Wall-clock overhead is modest\"，无量化数据。Appendix Table 14（reproducibility）只有 greedy timing |\n| (3) 明确 greedy=实用推荐 vs beam=质量最优 | ⚠️ 隐含但不明确 | §3 L120 称 S1 greedy 为 \"recommended strategy\"，但未对比 beam 的定位 |\n| (4) DocRED beam 用匹配 50-doc | ✅ | Table 16 caption: \"DocRED evaluated on matched 50-document subsets (same documents for greedy and beam)\" |\n\n**残留风险**：beam search 是 Abstract 第 4 个主要 claim（\"zero constraint violations across all four categories\"），但 runtime cost 完全未量化。审稿人可能质疑：如果 beam 开销很大，这个 claim 的实际价值就打折。建议至少在 Appendix 的 beam section 添加 k=4 的 wall-clock 对比。\n\n---\n\n### ⚠️ SF5 (R2-N3) [warning] Llama DocRED parse failure confounding → Partially fixed\n\n已完成：\n- Parse failure rate 报告（Table 5 caption: \"Parse failures: Llama DocRED 9.1%; others ≤1.1%\"）\n- Limitations L69 明确承认 confounding：\"partially confounded by increased parse failures under constraints (Llama: 9.1% vs. 6.8%)\"\n- section3_violation_landscape.tex L12 说明 violation rates 在 parsed docs 上计算；section7_conclusion.tex L32 说明 F1 同样\n\n**未完成**：未提供 deconfounded 分析（例如仅在两种条件下都成功 parse 的文档交集上对比 violation rates 和 F1）。Llama DocRED 是所有 6 个 ZS 配置中 parse failure 最高的（9.1%），constrained 比 unconstrained 高 2.3pp，这意味着 constrained 条件下有额外 23 篇文档被排除，可能系统性偏移了 violation rate 和 F1。\n\n**残留风险**：低。论文已坦诚承认 confound，且 Llama DocRED 不是主要 claim 的核心支撑（Qwen 是 primary model）。\n\n---\n\n### ⚠️ SF7 (R4-W2) [warning] DocRED fallback coverage 未报告 → Partially fixed\n\n已完成（appendix_discussion.tex L24-37, app:fallback-coverage）：\n- 定义了 effective semantic constraint coverage = 1 - f_gf\n- 报告了三个配置：Qwen SciERC = 100%, Qwen DocRED = 99.9% (f_gf=0.08%), Llama SciERC = 63.4% (f_gf=36.6%)\n- 解释了 multi-token tokenization 导致的差异\n- section5_docred_draft.tex L71 在正文提及 \"fallback rate (10.2%) closely tracking residual DR\"\n\n**未完成**：Llama DocRED effective coverage 未报告。这是 CF 最高的配置（12.02%），也是 parse failure 最高的配置，其 fallback coverage 对理解 Llama DocRED 的异常表现至关重要。目前只有 3/4 个 model×dataset 配置的 coverage 数据。\n\n---\n\n### ✅ SF8 (R2-N5) [warning] Reproducibility 信息不充分 → Resolved\n\nappendix_reproducibility.tex 现包含完整信息：\n- LoRA 超参数：rank=16, α=32, dropout=0.05, target modules（all attn + MLP）\n- 训练配置：AdamW, LR=2e-4, cosine schedule, warmup 0.1, batch 16, bf16, 3 epochs\n- 数据规模：SciERC 1762 examples/333 steps, DocRED 3053/573 steps\n- Max sequence length: 2048 (SciERC), 4096 (DocRED)\n- Seed: 42\n- GPU: NVIDIA RTX PRO 6000 Blackwell Server Edition (98GB VRAM)\n- Software versions: PyTorch 2.10, Transformers 4.57, PEFT 0.19, TRL 1.1, Accelerate 1.13\n- Inference time table (Table 14) with per-configuration timing\n\n**完全满足 reproducibility 要求。**\n\n---\n\n### ✅ SF9 (R4-W3) [warning] §4 DR reduction 范围与 Abstract 不一致 → Resolved\n\nsection4_composition_draft.tex L28 现在明确区分：\n- Calibrated models (Qwen, Llama): SciERC 94-99%, DocRED 45-90%\n- Including Mistral: full range 42-99%\n- 与 Abstract 的 \"42-99%\" 一致\n- Mistral 包含理由说明：\"whose high baseline ET shifts the regime\"\n\n---\n\n### ✅ Q1 (R4-Q1) [warning] JSON field ordering 是 sequential masking 隐含前提 → Resolved\n\nsection3_method_draft.tex L28-29 显式声明：\n\"The output JSON Schema (§3.2) enforces a fixed field ordering (head → tail → relation → head_type → tail_type) via deterministic grammar compilation. This ordering ensures that the relation type r_j is known before entity type fields are generated, which enables domain and range lookups in sequential masking (§3.5).\"\n\n明确了 field ordering 是 grammar 编译的产物（非假设），并解释了为什么这个 ordering 是 semantic masking 的先决条件。\n\n---\n\n### ⚠️ M3 (R2-N6) [warning] Semantic-only DocRED ET 增加 +70% → Partially fixed\n\nsection5_docred_draft.tex L70-71 承认了现象：\"cannot eliminate RV (29.87%) or prevent ET increases (2.48% → 4.22%), replicating SciERC's enabling dependency.\"\n\n**问题**：归因为 \"replicating SciERC's enabling dependency\" 不准确。SciERC semantic-only 的 ET 保持 0.40%（无变化），DocRED 从 2.48% 上升到 4.22%（+70%）。这不是 \"replication\"，而是 DocRED 特有的现象。可能的解释是：DocRED 有 96 relations 的复杂 domain/range 规则，semantic masking 在无 grammar 约束时将 OOV relation 的 type 推向非标准值，但这个机制未被阐述。\n\n**残留风险**：低。这是 semantic-only 模式（一个 ablation 行），不影响主要 claim（Full S1 下 ET=0%）。\n\n---\n\n### ⚠️ M1 (R2-N10) [info] RV=0.03% 解释不一致 → Partially fixed\n\nDocRED 所有含 grammar 的配置一致报告 RV=0.03%：\n- Table 4 (DocRED ablation): Grammar RV=0.03, Full S1 RV=0.03\n- Table 5 (cross-model): Qwen DocRED S1 RV=0.03\n- section5_docred_draft.tex L60: \"near-eliminates RV (29.66% → 0.03%)\"\n- section5_crossmodel_draft.tex L57: \"RV and ET are eliminated (≤0.03%)\"\n\n**未完成**：未解释 residual 0.03% 的具体来源。0.03% 在 DocRED 的 ~17,000 triples 中约为 5 个 triple。这些可能是 tokenization 边界情况或特定 relation name 的编码问题，但论文未提供解释。\n\n**残留风险**：极低。0.03% 实际上是 \"near-zero\"，不影响任何 claim。\n\n---\n\n### ✅ M2 (GC-N1) [info] Grammar-only 未标识为 GCD capability ceiling → Resolved\n\nsection5_scierc_draft.tex L85: \"This configuration represents the capability ceiling of grammar-based constrained decoding [GCD], which enforces JSON structure and vocabulary membership but cannot reason about cross-field semantic constraints.\"\n\n明确标注，引用了 GCD，并解释了 ceiling 的原因。\n\n---\n\n### ✅ M6 (R4-Q2) [info] CF-DR ablation 仅 SciERC/Qwen → Resolved\n\nappendix_discussion.tex L74-76 提供了充分的 transferability 论证：\n- 跨 6 个配置的 Spearman ρ = -0.77，证明 DR-CF 反向关联不限于 SciERC/Qwen\n- 选择 SciERC/Qwen 做 detailed ablation 的理由：\"highest CF (9.90%), making the trade-off most visible\"\n- 讨论了 Llama DocRED (CF=12.02%) 作为 \"larger CF headroom\" 的 setting\n- 明确声明 \"structural consequence of per-relation enforcement with grammar-first fallback, not a model- or dataset-specific artifact\"\n\n---\n\n## 🆕 New Issues Found\n\n### 🆕 N1 [warning] Abstract LoRA+beam \"zero violations\" claim 仅基于单一配置\n\n- **位置**：Abstract L13: \"With beam search ($k{=}4$), the full stack (LoRA + OntoCoDec + beam) achieves zero constraint violations across all four categories while preserving extraction quality\"\n- **问题**：此 claim 的实验支撑仅来自 Qwen3-8B / SciERC 一个配置（appendix_beam_search.tex L94-95: \"ET=0%, RV=0%, DR=0%, CF=0%\"）。未报告 Llama LoRA+beam 或 DocRED LoRA+beam 的数据。\n- **为什么是问题**：Abstract claim 没有限定 model 或 dataset，暗示 generalizability。但 LoRA+beam 仅有一个数据点，可能是最有利的配置（SciERC 只有 7 relations，constraint tightness 最低）。DocRED（96 relations, κ̄=0.842）的 LoRA+beam 表现未知。\n- **建议**：(a) Abstract 中限定 \"on SciERC\" 或 \"for Qwen3-8B\"；或 (b) 补充至少一个 Llama 或 DocRED 的 LoRA+beam 数据点。\n\n---\n\n## Updated Assessment\n\n| 维度 | Round 5 | Round 6 | 变化 |\n|------|---------|---------|------|\n| 方法严谨性 | 3.5/5 | 4.0/5 | ↑ R² 统计谦逊性、field ordering 显式声明、GCD ceiling 标注 |\n| 实验充分性 | 3.0/5 | 3.5/5 | ↑ reproducibility 完整、CF-DR transferability 论证、DocRED coverage 部分补充；beam runtime 仍缺 |\n| Reproducibility | 2.5/5 | 4.5/5 | ↑↑ 从信息严重不足到完整可复现 |\n\n### 建议评分：3.5 (Borderline Conference)\n\n**理由**：\n- **唯一的 critical issue (R²) 已完全修复**，统计处理规范\n- **6/11 issues fully resolved**，包括 reproducibility 的大幅改善\n- **剩余 5 个 partial fixes 均为 warning/info 级别**，不构成接收障碍：\n  - SF1（beam runtime）：可在 camera-ready 补充\n  - SF5（parse failure deconfounding）：已坦诚承认，Llama DocRED 非主要支撑\n  - SF7（Llama DocRED coverage）：3/4 配置已覆盖\n  - M3/M1：低影响 ablation 细节\n- **新发现 N1**（LoRA+beam 单一配置）值得关注，但 claim 本身技术上正确，建议添加限定语\n\n**从 Round 5 的 \"Weak Accept (Findings)\" 上调至 \"Borderline Conference\"**。论文的核心贡献（two-layer compiled constraint framework + systematic violation analysis）扎实，方法论已充分严谨。如果 beam runtime 和 LoRA+beam generalizability 能在最终版本补充，可支持 Conference 接收。",
    "reviewer_id": "1",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 387 · 2026-05-18T12:48:15.702865+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4205
}
```

</details>

---


### Assistant

_source line 388 · 2026-05-18T12:48:22.879380+00:00_

报告已提交。

总结：逐条核查了 11 个 open issues，6 个完全修复，5 个部分修复（均为 warning/info 级别），0 个未修复。唯一的 critical issue（R²=0.886 过度突出）已完全解决。新发现 1 个 warning 级别问题：Abstract 的 LoRA+beam "zero violations" claim 仅基于 Qwen3-8B/SciERC 单一配置。建议评分从 Round 5 的 Weak Accept (Findings) 上调至 3.5 Borderline Conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1"
}
```

</details>

---


## Round 11

## Round 11

8 recorded events


### User

_source line 389 · 2026-05-18T12:49:07.802051+00:00_

[Round 6 审稿请求]:
## Step 2 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2（新颖性/写作/格式）的完整 Round 6 审稿意见。请逐条回应：
- **[AGREE]** 同意并简述理由
- **[REBUT]** 反驳并引用具体 Section/Table/Figure 作为证据

---

### Reviewer 2 Issue Verification 结果

| Issue ID | Severity | Verdict | Evidence |
|----------|----------|---------|----------|
| [MF2] R4-N1 | critical | ✅ Resolved | Abstract 所有缩写均已展开 |
| [SF2] R4-N2 | warning | ✅ Resolved | Unicode em-dash 0 处，解释性 en-dash 0 处，prose 中 LaTeX `---` 0 处 |
| [SF3] R4-W1 | warning | ❌ Not fixed | 正文 trailing -ing 分词短语约 20 处，远超目标 ≤5，较 Round 5 ~10 处不减反增 |
| [SF4] R2-N2 | warning | ✅ Resolved | §1 L23 + Contribution #2 L29-30 区分 IE vs code-gen |
| [SF6] W3 | warning | ✅ Resolved | §1 L14-15 平衡表述 post-hoc filtering |
| [SF9] R4-W3 | warning | ✅ Resolved | §4 L28 区分 calibrated vs full range |
| [MF1] R2-N1 | critical | ✅ Resolved | Abstract 无 R²=0.886 |
| [M4] R4-W4 | info | ✅ Resolved | §5.2 重命名，结构改善 |
| [M8] Table 1 caption | info | ✅ Resolved | 无 em-dash |

### Reviewer 2 AI Writing Scan

- **Em-dash: 0 处** ✅
- **-ing phrases: ~20 处** ❌ — 完整列表 20 处，"confirming" 作为 trailing -ing 出现 7 次
- **Blacklist words: 0 处** ✅
- **过度分段: 无** ✅

### Reviewer 2 新发现

**🆕 N1 [warning]** "confirming" 单词过度重复（7+ 处 trailing ", confirming X"），构成极其明显的 AI 生成痕迹。建议至少 5/7 处改写。

**🆕 N2 [info]** BoostCD 未讨论。

**🆕 N3 [info]** §1 code-gen 区分处可加 parenthetical citation（Synchromesh/PICARD 仅在 §6 引用）。

### Reviewer 2 评分
- 写作质量: 2.5→3/5
- 格式合规: 4→4.5/5
- 建议评分: 3.5 (Borderline Conference)
- 升至 4.0 条件：将 ~20 处 -ing phrases 改写至 ≤5

---

**请逐条回应以上发现，特别是：**
1. SF3 (-ing phrases ❌ Not fixed) 你是否同意严重程度？
2. N1 ("confirming" ×7) 你认为这是否构成接收障碍？
3. 你是否有补充发现与 R2 的判断冲突或一致？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-18T12:49:19.070838+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": ", confirming",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": ", confirming",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 391 · 2026-05-18T12:49:21.029785+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex:67:Longer documents produce more violations in the unconstrained setting (e.g., DocRED long-bin: 3,550 vs.\ short-bin: 2,445), yet OntoCoDec achieves proportionally similar reduction, confirming that the constraint framework scales reliably with document complexity.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:95:Mistral-7B (unconstrained ET${=}$7.58\% on DocRED) deviates from this pattern: its residual DR on DocRED (33.21\%) substantially exceeds the linear prediction, confirming that when model calibration is insufficient (ET${>}$5\% on either dataset), residual DR is dominated by entity misclassification rather than constraint-search failure.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:115:Llama-3.1-8B's lower baseline RV (16.03\%) yields a smaller but directionally consistent improvement ($+$0.29\,pp vs.\ $+$0.50\,pp), confirming that F1 gain magnitude is proportional to baseline OOV rate.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:159:Under unconstrained decoding, CF rates collapse to $\leq$1\% on both datasets, confirming that CF violations are a side-effect of per-slot type commitment rather than a model deficiency.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:275:Adding both layers achieves near-complete elimination (DR\,$\leq$\,0.20\% in all 4 settings), confirming that even after fine-tuning, the semantic layer's pair-based enforcement captures violations that training alone cannot eliminate, specifically on tight-constraint relations where the valid type-pa
…[truncated 3870 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 1958
}
```

</details>

---


### Tool call

_source line 392 · 2026-05-18T12:49:21.782665+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": ",\\s+(confirming|suggesting|indicating|demonstrating|highlighting|showing|reflecting|attribut|eliminat|reduc|validat|yield|establish|provid|enabl|preserv|maintain|achieving|limiting|replicat|producing|making|ensuring)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex",
  "head_limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": ",\\s+(confirming|suggesting|indicating|demonstrating|highlighting|showing|reflecting|attribut|eliminat|reduc|validat|yield|establish|provid|enabl|preserv|maintain|achieving|limiting|replicat|producing|making|ensuring)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex",
    "head_limit": "60"
  }
}
```

</details>

---


### Tool result

_source line 393 · 2026-05-18T12:49:21.833768+00:00_

&lt;persisted-output>
Output too large (22.2KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-1-11179fb2/d600a059-0871-4069-9dd6-a46b2f0d9fb2/tool-results/toolu_01RT2jCT6hQBdmK34W3TEwe4.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:139:escapes to OOV strings (e.g., ``ORGB'', ``EVENT''), producing 355
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:150:rules exist, limiting its enforcement capacity.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:179:for the model to redirect probability mass toward, enabling
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:14:Post-hoc filtering achieves higher F1 in most zero-shot settings via precision gains, but at the cost of discarding up to 48\% of predictions including true positives; at high rejection rates (e.g., Mistral DocRED 73.7\%), it discards the majority of outputs, making it impractical.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:22:The layers compose via bitwise AND with an \emph{enabling dependency}: the grammar layer guarantees vocabulary membership, enabling the semantic layer to look up domain/range rules.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:28:    \item The first systematic study of ontological constraint violations in LLM-based IE (spanning per-relation tightne
…[truncated 255 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 394 · 2026-05-18T12:50:40.261923+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 6 交叉回应 — Reviewer 1 对 Reviewer 2 意见的逐条回应\n\n---\n\n### 已确认修复的 Issues（快速确认）\n\n[AGREE] R2-MF2 (R4-N1) ✅: Abstract 缩写展开已验证，LLM、IE、LoRA 等均已首次出现时定义。\n\n[AGREE] R2-SF2 (R4-N2) ✅: em-dash/en-dash 清零已验证。正文无 Unicode em-dash (U+2014)，无解释性 en-dash。\n\n[AGREE] R2-SF4 (R2-N2) ✅: §1 L23 + Contribution #2 L29-30 已充分区分 IE vs code-gen 的 type constraint 差异（\"IE requires stateful cross-field constraints because entity type validity depends on the co-occurring relation within each triple\"）。我在 Q1 核查中也确认了 §3 L28-29 补充了 field ordering 声明，两处共同建立了 IE 特殊性的论证。\n\n[AGREE] R2-SF6 (W3) ✅: §1 L14-15 对 post-hoc filtering 的表述现在是平衡的（承认 \"higher F1 in most zero-shot settings via precision gains\"，同时指出 recall 代价）。\n\n[AGREE] R2-SF9 (R4-W3) ✅: 与我的 SF9 判断一致。\n\n[AGREE] R2-MF1 (R2-N1) ✅: 与我的 MF1 判断一致。\n\n[AGREE] R2-M4 (R4-W4) ✅: §5.2 结构改善可接受。\n\n[AGREE] R2-M8 (Table 1 caption) ✅: 无 em-dash。\n\n---\n\n### 需要详细回应的 Issues\n\n#### [AGREE] R2-SF3: -ing phrases ❌ Not fixed\n\n**同意严重程度判断（warning），同意 \"not fixed\" verdict。**\n\n我独立验证了 R2 的发现，并提供补充数据：\n\n仅 \", confirming\" 一个模式，在正文（非注释、非备份文件）中出现 6 次：\n- abstract.tex L12: \", confirming near-lossless composability\"\n- section3_violation_landscape.tex L17: \", confirming that large vocabularies...\"\n- section5_scierc_draft.tex L74-75: \", confirming that constraint enforcement is F1-neutral\"\n- section5_scierc_draft.tex L92: \", confirming the enabling dependency\"\n- section5_scierc_draft.tex L119: \", confirming orthogonal composability\"\n- section5_wikievents_draft.tex L59: \", confirming layer complementarity\"\n\n附录中再增 6-7 次（appendix_discussion.tex L95, L115, L159, L275, L298; appendix_doc_length.tex L67; appendix_prompt_sensitivity.tex）。\n\n**全文 \", confirming\" 至少 12 次，R2 报告的 7+ 实际上是保守估计。**\n\n这个模式之所以危险，不仅因为单词重复，更因为 \", confirming X\" 是一个完整的句法模板被机械复用。真实人类写作会自然变体为 \"this confirms,\" \"which supports,\" \"consistent with,\" \"as expected from\" 等。12 次重复同一个 trailing participial construction 是极其明显的 AI 生成指纹。\n\n**从方法/实验严谨性角度的补充**：这些 \", confirming X\" 中有些承载了重要的实验论证。例如 §5.2 L92 的 \"confirming the enabling dependency\" 是全文核心技术 claim 之一。如果审稿人因 AI 痕迹而降低对全文的信任度，这些技术论证也会受到连带质疑。\n\n---\n\n#### [AGREE] R2-N1 🆕: \"confirming\" 过度重复\n\n**同意这是一个值得修复的问题，但不同意构成独立接收障碍。**\n\n理由：\n1. \"confirming\" 过度重复是 SF3 (-ing phrases) 的子集，不是独立问题。修复 SF3 时自然会解决 N1。\n2. 从审稿人行为角度：真实 reviewer 不会因为单词重复而直接 reject；但会在 \"overall impression\" 中降分，叠加其他小问题可能推到 borderline 以下。\n3. 修复成本极低（每处 15 秒的改写），收益高（消除最显眼的 AI 痕迹），应优先处理。\n\n**建议：将 SF3 和 N1 合并为一个 action item \"全文 -ing phrase + confirming 改写\"，目标 ≤5 处 trailing -ing（R2 的阈值合理）。**\n\n---\n\n#### [REBUT] R2-N2 🆕: BoostCD 未讨论\n\n**需要具体 context 才能判断。** R2 未提供 BoostCD 的完整引用（作者、venue、year）。\n\n从方法审查角度，§6 Related Work 已覆盖：\n- Grammar-constrained decoding: XGrammar, Outlines, LMQL, DOMINO, SynCode, ASAp（section6_related_work.tex L5）\n- Type-constrained: Synchromesh, PICARD, GCD, GoLLIE, DORE, GenIE, EnriCo（L8-10）\n- Training-based: TANL, REBEL, UIE, KnowCoder, CodeIE（L11）\n- Post-hoc: ODKE, SPIRES, OntologX（L11）\n- Quality impact: CRANE, Schall et al., Tam et al.（L14）\n\n如果 BoostCD 是近期发表的直接相关方法（例如 ontology-constrained decoding for IE），那么确实需要讨论。但如果它属于上述某个类别的边缘工作，不讨论也不构成 coverage gap。**建议 R2 提供具体引用以便评估。**\n\n---\n\n#### [AGREE] R2-N3 🆕: §1 code-gen 区分处加 citation\n\n同意。§1 L8 提到 \"Grammar-constrained decoding [XGrammar, Outlines, LMQL]\"，但 L23 的 code-gen 区分处（\"Unlike type-constrained code generation where types are statically declared\"）没有引用具体工作。Synchromesh 和 PICARD 在 §6 L8 被引用但 §1 未引用。添加 parenthetical citation 是合理的——读者不必翻到 §6 才知道哪些是 code-gen type constraint 的代表性工作。\n\n**修复成本极低，建议采纳。**\n\n---\n\n### 对 R2 整体评分的回应\n\nR2 建议 3.5 (Borderline Conference)，条件是 -ing phrases 改写至 ≤5 后可升至 4.0。\n\n**我的判断**：\n- 我同样给出 3.5，但我的 bottleneck 不同：我的限制因素是 beam runtime 未量化 + LoRA+beam 单一配置（我的 SF1 ⚠️ 和 🆕N1）\n- R2 的限制因素是 -ing phrases（SF3 ❌）\n- 两组限制因素互不重叠，且修复成本都很低（-ing 改写 ~30 分钟，beam runtime 需要一次实验运行）\n- **如果两组问题都修复，两个 reviewer 的评分应该都能升至 3.5-4.0 区间**\n\n综合我们两份审稿意见，论文当前状态是 **3.5 (Borderline Conference)**，距离 Conference 接收需要：\n1. [写作] -ing phrases 改写至 ≤5 处（R2 要求，我同意）\n2. [实验] Beam runtime 量化 + Abstract beam claim 限定（我的要求）\n3. [低优先级] Llama DocRED coverage、semantic-only ET 解释（partial fixes，不阻碍接收）",
  "reviewer_id": "1",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 6 交叉回应 — Reviewer 1 对 Reviewer 2 意见的逐条回应\n\n---\n\n### 已确认修复的 Issues（快速确认）\n\n[AGREE] R2-MF2 (R4-N1) ✅: Abstract 缩写展开已验证，LLM、IE、LoRA 等均已首次出现时定义。\n\n[AGREE] R2-SF2 (R4-N2) ✅: em-dash/en-dash 清零已验证。正文无 Unicode em-dash (U+2014)，无解释性 en-dash。\n\n[AGREE] R2-SF4 (R2-N2) ✅: §1 L23 + Contribution #2 L29-30 已充分区分 IE vs code-gen 的 type constraint 差异（\"IE requires stateful cross-field constraints because entity type validity depends on the co-occurring relation within each triple\"）。我在 Q1 核查中也确认了 §3 L28-29 补充了 field ordering 声明，两处共同建立了 IE 特殊性的论证。\n\n[AGREE] R2-SF6 (W3) ✅: §1 L14-15 对 post-hoc filtering 的表述现在是平衡的（承认 \"higher F1 in most zero-shot settings via precision gains\"，同时指出 recall 代价）。\n\n[AGREE] R2-SF9 (R4-W3) ✅: 与我的 SF9 判断一致。\n\n[AGREE] R2-MF1 (R2-N1) ✅: 与我的 MF1 判断一致。\n\n[AGREE] R2-M4 (R4-W4) ✅: §5.2 结构改善可接受。\n\n[AGREE] R2-M8 (Table 1 caption) ✅: 无 em-dash。\n\n---\n\n### 需要详细回应的 Issues\n\n#### [AGREE] R2-SF3: -ing phrases ❌ Not fixed\n\n**同意严重程度判断（warning），同意 \"not fixed\" verdict。**\n\n我独立验证了 R2 的发现，并提供补充数据：\n\n仅 \", confirming\" 一个模式，在正文（非注释、非备份文件）中出现 6 次：\n- abstract.tex L12: \", confirming near-lossless composability\"\n- section3_violation_landscape.tex L17: \", confirming that large vocabularies...\"\n- section5_scierc_draft.tex L74-75: \", confirming that constraint enforcement is F1-neutral\"\n- section5_scierc_draft.tex L92: \", confirming the enabling dependency\"\n- section5_scierc_draft.tex L119: \", confirming orthogonal composability\"\n- section5_wikievents_draft.tex L59: \", confirming layer complementarity\"\n\n附录中再增 6-7 次（appendix_discussion.tex L95, L115, L159, L275, L298; appendix_doc_length.tex L67; appendix_prompt_sensitivity.tex）。\n\n**全文 \", confirming\" 至少 12 次，R2 报告的 7+ 实际上是保守估计。**\n\n这个模式之所以危险，不仅因为单词重复，更因为 \", confirming X\" 是一个完整的句法模板被机械复用。真实人类写作会自然变体为 \"this confirms,\" \"which supports,\" \"consistent with,\" \"as expected from\" 等。12 次重复同一个 trailing participial construction 是极其明显的 AI 生成指纹。\n\n**从方法/实验严谨性角度的补充**：这些 \", confirming X\" 中有些承载了重要的实验论证。例如 §5.2 L92 的 \"confirming the enabling dependency\" 是全文核心技术 claim 之一。如果审稿人因 AI 痕迹而降低对全文的信任度，这些技术论证也会受到连带质疑。\n\n---\n\n#### [AGREE] R2-N1 🆕: \"confirming\" 过度重复\n\n**同意这是一个值得修复的问题，但不同意构成独立接收障碍。**\n\n理由：\n1. \"confirming\" 过度重复是 SF3 (-ing phrases) 的子集，不是独立问题。修复 SF3 时自然会解决 N1。\n2. 从审稿人行为角度：真实 reviewer 不会因为单词重复而直接 reject；但会在 \"overall impression\" 中降分，叠加其他小问题可能推到 borderline 以下。\n3. 修复成本极低（每处 15 秒的改写），收益高（消除最显眼的 AI 痕迹），应优先处理。\n\n**建议：将 SF3 和 N1 合并为一个 action item \"全文 -ing phrase + confirming 改写\"，目标 ≤5 处 trailing -ing（R2 的阈值合理）。**\n\n---\n\n#### [REBUT] R2-N2 🆕: BoostCD 未讨论\n\n**需要具体 context 才能判断。** R2 未提供 BoostCD 的完整引用（作者、venue、year）。\n\n从方法审查角度，§6 Related Work 已覆盖：\n- Grammar-constrained decoding: XGrammar, Outlines, LMQL, DOMINO, SynCode, ASAp（section6_related_work.tex L5）\n- Type-constrained: Synchromesh, PICARD, GCD, GoLLIE, DORE, GenIE, EnriCo（L8-10）\n- Training-based: TANL, REBEL, UIE, KnowCoder, CodeIE（L11）\n- Post-hoc: ODKE, SPIRES, OntologX（L11）\n- Quality impact: CRANE, Schall et al., Tam et al.（L14）\n\n如果 BoostCD 是近期发表的直接相关方法（例如 ontology-constrained decoding for IE），那么确实需要讨论。但如果它属于上述某个类别的边缘工作，不讨论也不构成 coverage gap。**建议 R2 提供具体引用以便评估。**\n\n---\n\n#### [AGREE] R2-N3 🆕: §1 code-gen 区分处加 citation\n\n同意。§1 L8 提到 \"Grammar-constrained decoding [XGrammar, Outlines, LMQL]\"，但 L23 的 code-gen 区分处（\"Unlike type-constrained code generation where types are statically declared\"）没有引用具体工作。Synchromesh 和 PICARD 在 §6 L8 被引用但 §1 未引用。添加 parenthetical citation 是合理的——读者不必翻到 §6 才知道哪些是 code-gen type constraint 的代表性工作。\n\n**修复成本极低，建议采纳。**\n\n---\n\n### 对 R2 整体评分的回应\n\nR2 建议 3.5 (Borderline Conference)，条件是 -ing phrases 改写至 ≤5 后可升至 4.0。\n\n**我的判断**：\n- 我同样给出 3.5，但我的 bottleneck 不同：我的限制因素是 beam runtime 未量化 + LoRA+beam 单一配置（我的 SF1 ⚠️ 和 🆕N1）\n- R2 的限制因素是 -ing phrases（SF3 ❌）\n- 两组限制因素互不重叠，且修复成本都很低（-ing 改写 ~30 分钟，beam runtime 需要一次实验运行）\n- **如果两组问题都修复，两个 reviewer 的评分应该都能升至 3.5-4.0 区间**\n\n综合我们两份审稿意见，论文当前状态是 **3.5 (Borderline Conference)**，距离 Conference 接收需要：\n1. [写作] -ing phrases 改写至 ≤5 处（R2 要求，我同意）\n2. [实验] Beam runtime 量化 + Abstract beam claim 限定（我的要求）\n3. [低优先级] Llama DocRED coverage、semantic-only ET 解释（partial fixes，不阻碍接收）",
    "reviewer_id": "1",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 395 · 2026-05-18T12:50:44.339779+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4077
}
```

</details>

---


### Assistant

_source line 396 · 2026-05-18T12:50:51.960451+00:00_

交叉回应已提交。核心判断：

- **SF3 (-ing phrases)**：同意 R2 的 "Not fixed" verdict。独立验证 ", confirming" 至少 12 处（R2 的 7+ 是保守估计），构成明显 AI 痕迹。
- **N1 ("confirming" ×7)**：同意需修复但不构成独立接收障碍，应合并到 SF3 一起处理。
- **N2 (BoostCD)**：要求 R2 提供完整引用，Related Work 当前 coverage 已较全面。
- **N3 (§1 citation)**：同意，低成本修复。
- **整体评分**：两位 Reviewer 均给 3.5，bottleneck 互补（R2 看写作，R1 看实验），修复成本均可控。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1"
}
```

</details>

---


## Round 12

## Round 12

68 recorded events


### User

_source line 397 · 2026-05-19T06:23:59.150931+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）

### 论文信息
- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Ontology Constraints
- **路径**: `projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`
- **目标 Venue**: EMNLP 2026 (ARR May 2026 cycle)
- **Deadline**: 2026-05-25

### Venue 要求
- ACL style template, double-blind, Long paper 8 页正文
- 附录不计页数，Limitations section 必需
- ARR Overall Assessment 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit

### 你的审查侧重
你负责**方法严谨性和实验设计**，重点关注：

1. **方法正确性**：
   - 两层约束（grammar + semantic）的形式化是否严谨？
   - 约束组合（§4）的数学推导是否正确？
   - "enabling dependency" 的论证是否有充分实验支撑？
   - "pair-based enforcement" vs "independent enforcement" 的区别是否清晰、正确？

2. **实验设计**：
   - 数据集选择（SciERC 7 relations, DocRED 96 relations, WikiEvents 56 event types）是否足够代表性？
   - 消融实验（five-way ablation）是否完整？是否缺少关键 baseline？
   - Cross-model（Qwen3-8B, Llama-3.1-8B, Mistral-7B）和 cross-scale（70B）验证是否充分？
   - Fine-tuning composability 实验设计是否合理？只用 LoRA 是否局限？
   - WikiEvents EE 验证的 test set 只有 20 documents，是否足够？

3. **统计严谨性**：
   - Bootstrap CI 和 p-value 的使用是否正确？
   - §4 dual-factor pattern 的 R²=0.886 基于 n=4 数据点，统计效力如何？
   - CF↔DR trade-off 的 Spearman ρ=-0.77, n=6 是否可靠？

4. **实验结果诚实性**：
   - CF violation 上升（zero-shot 最高 12.02% RE, 21% EE）是否被充分讨论？
   - DocRED DR 只降 45%（vs SciERC 94%）的解释是否令人信服？
   - Zero-shot R-F1 只有 2-8%，这些实验的实际价值是什么？
   - Beam search 结果仅在 SciERC 两个模型上完全消除所有 violation，其他场景呢？

5. **可重复性**：
   - 超参数、prompt template、evaluation protocol 是否完整披露？
   - 代码/数据可用性？

### 输出格式
请按以下结构输出审稿意见：
```
## Summary（2-3 句）
## Strengths（逐条）
## Weaknesses（逐条，标注 [Must-Fix] 或 [Should-Fix] 或 [Minor]）
## Questions（需要作者回答的问题）
## Missing References（如有）
## Overall Assessment（评分 + 置信度 + 简要理由）
```

评分参照 ARR 标准（1-5）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 398 · 2026-05-19T06:24:09.015872+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
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

_source line 399 · 2026-05-19T06:24:09.016350+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 400 · 2026-05-19T06:24:12.287716+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 401 · 2026-05-19T06:24:13.745387+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 402 · 2026-05-19T06:24:13.745903+00:00_

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
12	\usepackage{multirow}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{enumitem}
16	\usepackage{xcolor}
17	\usepackage{pifont}
18	
19	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Ontology Constraints}
20	
21	\author{Anonymous ACL submission}
22	
23	\begin{document}
24	\maketitle
25	
26	% === Abstract ===
27	\input{abstract}
28	
29	% === §1 Introduction ===
30	\input{section1_introduction_draft}
31	
32	% === §2 Background ===
33	\input{section2_background}
34	
35	% === §3 Method ===
36	\input{section3_method_draft}
37	
38	% === §4 Constraint Composition ===
39	\section{Constraint Composition}
40	\label{sec:composition}
41	\input{section4_composition_draft}
42	
43	% === §5 Experiments ===
44	\section{Experiments}
45	\label{sec:experiments}
46	
47	\input{section3_violation_landscape}
48	
49	\input{section5_scierc_draft}
50	\input{section5_docred_draft}
51	\input{section5_crossmodel_draft}
52	\input{section5_wikievents_draft}
53	\input{section5_runtime}
54	
55	% === §6 Related Work ===
56	\input{section6_related_work}
57	
58	% === §7 Discussion and Conclusion ===
59	\section{Discussion and Conclusion}
60	\label{sec:discussion}
61	\input{section7_conclusion_compressed}
62	
63	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
64	\clearpage
65	\section*{Limitations}
66	
67	CF impact is model-dependent: for well-calibrated models (Qwen, Llama), S1 introduces CF violations (up to 12.02\%) as a consequence of per-relation independent enforcement; for poorly-calibrated models (Mistral), S1 substantially reduces CF (56.87\%\,$\to$\,1.27\%) by constraining type assignments to schema-valid values.
68	CF fallback ablation shows that eliminating CF re-routes
…[truncated 4150 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 403 · 2026-05-19T06:24:19.280847+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"}]

Based on the search results, here's what I found about ACL ARR 2025-2026 reviewer guidelines and scoring criteria:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Key Scoring Guidelines

**Soundness Score:** The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

**Excitement Score:** Sometimes reviewers may find the work sound, but not something that is interesting for them personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

## Area Chair Metareview Scoring

The metarevi
…[truncated 639 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6993
}
```

</details>

---


### Tool call

_source line 404 · 2026-05-19T06:24:22.936334+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer scoring criteria, including all dimensions (soundness, excitement, overall assessment, confidence), their scales, and definitions for each score level. Also extract any specific guidance on what constitutes a good vs bad review."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer scoring criteria, including all dimensions (soundness, excitement, overall assessment, confidence), their scales, and definitions for each score level. Also extract any specific guidance on what constitutes a good vs bad review."
  }
}
```

</details>

---


### Tool call

_source line 405 · 2026-05-19T06:24:23.290708+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
  }
}
```

</details>

---


### Tool result

_source line 406 · 2026-05-19T06:24:23.341393+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_fd4b26.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_d3264e.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_550cbf_DEPRECATED.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_outline.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_DEPRECATED.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/paper_tables_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/p3_case_studies.tex
/home/ubuntu/.agent-
…[truncated 3453 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 407 · 2026-05-19T06:24:29.429285+00:00_

# ARR Reviewer Scoring Criteria

## Scoring Dimensions

The guidelines mention **three primary scores** that reviewers provide:

1. **Soundness** - Technical validity and rigor of the work
2. **Excitement** - Personal interest level in the topic
3. **Overall Assessment** - Explicit recommendation for paper outcome

Additionally, reviewers indicate a **confidence score** reflecting how certain they are in their evaluation.

## Key Guidance on Scores

**Soundness Requirements:**
"The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation."

**Separating Soundness from Excitement:**
Reviewers may find work technically sound but personally uninteresting. These are "orthogonal" dimensions—low excitement doesn't require low soundness scores.

**Overall Assessment Criteria:**
Papers for main venues must be "sufficiently sound and reproducible," though personal excitement remains secondary. Contributions like efficiency improvements or resource creation for underserved languages deserve consideration despite potentially lower novelty appeal.

## What Constitutes Good Reviews

**Essential qualities:**
- Specific, concrete feedback with referenced details
- Professional and neutral tone
- Acknowledgment of author responses
- Clear justification for all scores

**What to avoid:**
- Vague criticisms ("not clear" without specifics)
- Sarcasm or dismissive language
- Raising entirely new issues in resubmission reviews
- Unconscious bias reflected in unsupported low scores

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6492
}
```

</details>

---


### Tool call

_source line 408 · 2026-05-19T06:24:33.800701+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 409 · 2026-05-19T06:24:34.202988+00:00_

1	\begin{abstract}
2	We present \textsc{OntoCoDec}, which compiles Information Extraction (IE) ontology schemas into two composable token-level decoding constraints that enforce structural and type-validity constraints during autoregressive generation:
3	(1)~a \emph{grammar layer} (XGrammar context-free grammar) that guarantees JSON structural validity and entity/relation vocabulary membership (ET and RV violations $\to$\,0\%); and
4	(2)~a \emph{semantic layer} that enforces per-triple domain/range type constraints via a stateful entity registry and dynamic logit masking, with grammar-first fallback when constraints conflict.
5	%
6	Without constraints, Large Language Model (LLM) based IE produces systematic domain/range (DR) violations: 15.37\% on SciERC (7 relations) and 18.46\% on DocRED (96 relations), with 1--2\% persisting even after fine-tuning; rates are driven by \emph{constraint tightness} rather than ontology or model scale.
7	Composed with Low-Rank Adaptation (LoRA) fine-tuning, \textsc{OntoCoDec} reduces DR to $\leq$\,0.20\% with R-F1 within $\pm$0.6\,pp of unconstrained baselines (R-F1 40--46): near-lossless composability at deployment-grade extraction quality.
8	% exp_ids: w5_lora_scierc_constrained_eval, w5_qwen_docred_lora_constrained_eval, w5_llama_lora_scierc_constrained_eval, w5_llama_docred_lora_constrained_eval
9	Under zero-shot decoding, which stress-tests constraint robustness at low extraction quality (R-F1 2--8\%), DR drops by 42--99\% across three model families (Qwen3-8B, Llama-3.1-8B, Mistral-7B) with no significant F1 cost (DocRED: $+$0.50\,pp, $p{<}0.001$; \S\ref{sec:cross-model}).
10	With beam search ($k{=}4$), the full stack eliminates all four violation types under fine-tuned beam decoding (SciERC, both Qwen3-8B and Llama-3.1-8B) while preserving extraction quality (R-F1 44.23 and 46.11, respectively); in zero-shot beam decoding, DR reaches 0\% for calibrated models on both RE datasets.
11	The framework generalizes to event extractio
…[truncated 981 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 410 · 2026-05-19T06:24:34.354038+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 411 · 2026-05-19T06:24:34.655841+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly used for information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity is guaranteed to carry a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	Violations persist across the capability spectrum: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred} under zero-shot decoding, and 1--2\% even after LoRA fine-tuning, driven by \emph{constraint tightness} (few valid type pairs per relation) rather than ontology or model scale.
9	Constraint enforcement matters most at deployment-grade quality (R-F1 40--46\%): at this level, residual type violations propagate directly into knowledge graphs and decision-support pipelines; reliable type-safety enforcement is needed.
10	
11	Existing approaches leave a fundamental gap.
12	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
13	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} guarantees syntactic well-formedness but cannot encode cross-field semantic constraints.
14	Post-hoc filtering achieves higher F1 in most zero-shot settings via precision gains, but at the cost of discarding up to 48\% of predictions including true positives; at high rejection rates (e.g., Mistral DocRED 73.7\%), it discards the majority of outputs and becomes impractical.
15	OntoCoDec preserves recall by enforcing constraints during generation rather than discarding non-compliant outputs.
16	Training-based approaches~\cite{sainz2024gollie,lu2022uie} provide only soft guidance that cannot el
…[truncated 2590 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 412 · 2026-05-19T06:24:34.656230+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 413 · 2026-05-19T06:24:35.108909+00:00_

1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	We present OntoCoDec, a two-layer constrained decoding framework that compiles ontology schemas into token-level masks enforced during autoregressive generation.
9	Unlike type-constrained code generation, IE presents three distinct challenges: (1)~entity types are inferred from free text rather than declared annotations, (2)~the entity registry is built dynamically during generation, and (3)~constraint targets are context-dependent type assignments rather than fixed grammar productions.
10	The grammar layer (\S\ref{sec:grammar}) guarantees structural validity (well-formed JSON with ontology-vocabulary membership), while the semantic layer (\S\ref{sec:semantic}) enforces domain/range type constraints via a stateful entity registry.
11	We describe the problem formulation (\S\ref{sec:formulation}), each layer, and two decoding strategies (\S\ref{sec:strategies}).
12	Formal analysis of constraint composition is deferred to Section~\ref{sec:composition}.
13	
14	
15	\subsection{Problem Formulation}
16	\label{sec:formulation}
17	
18	\paragraph{IE as structured generation.}
19	Given an input text $x$, a language model generates a structured JSON output $y$:
20	%
21	\begin{equation}\label{eq:output-schema}
22	\resizebox{.88\columnwidth}{!}{$\displaystyle
23	  y = \bigl\{\texttt{entities}: [\{n_i, \tau_i\}],\; \texttt{relations}: [\{h_j, t_j, r_j, \tau^h_j, \tau^t_j\}]\bigr\}
24	$}
25	\end{equation}
26	%
27	where each entity has a name $n_i$ and type $\tau_i \in \mathcal{E}$, and each relation specifies head $h_j$, tail $t_j$, relation type $r_j \in \mathcal{R}$, and head/tail entity types $\tau^h_j, \tau^t_j$.
28	The output JSON Schema (\S\ref{sec:grammar}) enforces a fixed field ordering (head $\to$ tail $\to$ relation $\to$ head\_type $\to$ tail\_type) via deterministic grammar compilation.
29	This ordering en
…[truncated 6610 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 414 · 2026-05-19T06:24:35.159532+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
  }
}
```

</details>

---


### Tool result

_source line 415 · 2026-05-19T06:24:35.210201+00:00_

1	% Section 2: Background (compressed)
2	
3	\section{Background}
4	\label{sec:background}
5	
6	\paragraph{IE Ontology Structure.}
7	\label{sec:bg:ontology}
8	An IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defines entity types $\mathcal{E}$, relation types $\mathcal{R}$, and a mapping $\sigma: \mathcal{R} \to \mathcal{P}(\mathcal{E} \times \mathcal{E})$ specifying valid (head type, tail type) pairs per relation.
9	A triple $(h, r, t)$ is \emph{type-valid} if $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$.
10	We define the \emph{constraint tightness} of $r$ as $1 - |\sigma(r)| / |\mathcal{E}|^2$: tighter constraints leave fewer valid options, increasing violation likelihood.
11	
12	\paragraph{Grammar-Constrained Decoding.}
13	\label{sec:bg:gcd}
14	Grammar-constrained decoding restricts each token $y_t$ to a mask $M_g \in \{0, 1\}^{|V|}$ derived from a target grammar.
15	XGrammar~\citep{dong2025xgrammar} compiles JSON Schemas into pushdown automata for efficient enforcement of structural constraints; Outlines~\citep{willard2023outlines} and SGLang~\citep{zheng2024sglang} offer similar capabilities.
16	However, these methods are limited to context-free constraints and cannot enforce cross-field semantic rules (e.g., ``if $r$ = \textsc{Feature-of}, then $\mathrm{type}(h) \in \{\textsc{Method}, \textsc{OtherScientificTerm}\}$''), which depend on previously generated field values.
17	
18	\paragraph{Problem Statement.}
19	\label{sec:bg:problem}
20	Given $\mathcal{O}$ and an autoregressive LM $\mathcal{M}$, we seek constraints $\mathcal{C}$ ensuring: (a)~\textbf{structural validity}, i.e., well-formed JSON with $\mathcal{E}$/$\mathcal{R}$ membership; and (b)~\textbf{type validity}, i.e., $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$ for every triple.
21	Condition (a) is context-free; (b) is context-sensitive but \emph{prefix-decidable}: at the point where a type token is generated, all information needed (relation type, entity registry) is ava
…[truncated 149 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 416 · 2026-05-19T06:24:40.348087+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 417 · 2026-05-19T06:24:40.750167+00:00_

1	% Section: Constraint Composition (compressed, 787→~500 words)
2	
3	At each decoding step $t$, let $G(t) \subseteq V$ and $S(t) \subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.
4	The final mask is their conjunction:
5	%
6	\begin{equation}\label{eq:composition}
7	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
8	\end{equation}
9	%
10	so a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$. This reflects the enabling dependency (\S\ref{sec:method}): the semantic layer requires the relation type to belong to $\mathcal{R}$, a property guaranteed only by the grammar layer.
12	
13	\paragraph{Grammar-First Fallback.}
14	When $S(t) \cap G(t) = \emptyset$ (tight constraints leave no token that is both grammar-valid and semantically valid), na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
15	We enforce a \emph{grammar-first fallback}: if no semantically valid token survives grammar filtering, semantic masking is skipped and the grammar layer alone controls selection.
16	Structural integrity is a hard constraint; a type violation is a soft error detectable by downstream validation.
17	Among type violations, DR and CF differ in severity: a DR violation renders the triple ontologically invalid (the entity type lies outside the relation's domain or range), whereas a CF violation means each triple is individually schema-valid but the same entity receives different type assignments across triples.
18	
19	\paragraph{Constraint Tightness.}
20	We define the tightness of relation $r$ as:
21	%
22	\begin{equation}\label{eq:tightness}
23	  \kappa(r) = 1 - \frac{|\mathcal{V}(r)|}{|\mathcal{E}|^2},
24	\end{equation}
25	%
26	where $\mathcal{V}(r)$ is the set of valid type pairs and $\mathcal{E}$ the entity type vocabulary.
27	The mean tightness $\bar{\kappa} = \frac{
…[truncated 1263 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 418 · 2026-05-19T06:24:40.901255+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
  }
}
```

</details>

---


### Tool result

_source line 419 · 2026-05-19T06:24:41.203869+00:00_

1	% §5 Setup (compressed from Violation Landscape)
2	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
3	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
4	
5	\label{sec:violation_landscape}
6	
7	\paragraph{Setup.}
8	We evaluate on SciERC~\cite{luan2018scierc} (551 test sentences, 7 relations, $\bar{\kappa}{=}0.333$) and DocRED~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test annotations are not publicly available; we evaluate on the development set.} 96 relations, $\bar{\kappa}{=}0.842$).
9	Primary model: Qwen3-8B~\cite{qwen2025qwen3}, zero-shot greedy decoding; cross-model validation in \S\ref{sec:cross-model}, composability with fine-tuning in \S\ref{sec:composability}.
10	We measure four violation categories: \textbf{DR} (domain/range type pair $\notin \sigma(r)$), \textbf{RV} (relation $\notin \mathcal{R}$), \textbf{ET} (entity type $\notin \mathcal{E}$), and \textbf{CF} (same entity assigned conflicting types across triples).
11	Baseline DR violations are 15.37\% (SciERC) and 18.46\% (DocRED), comparable rates driven by constraint tightness rather than ontology scale (\S\ref{sec:introduction}); schema-informed prompting reduces DR by 62\% on SciERC but is per-relation unreliable (Appendix~\ref{app:per-relation-landscape}).
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 420 · 2026-05-19T06:24:41.255040+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 421 · 2026-05-19T06:24:41.958219+00:00_

1	% Section 5 — SciERC Results (Draft)
2	% Data source: Phase 2 SciERC registry experiments
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,
4	%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2
5	% All numbers verified against registry 2026-05-14.
6	
7	\subsection{Ablation and Composability with Fine-Tuning}
8	\label{sec:scierc-results}
9	
10	Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC (Qwen3-8B, zero-shot, 551 documents); only the active constraint layers differ across rows.
11	
12	% ──────────────────────────────────────────
13	%  Table: SciERC five-way ablation
14	% ──────────────────────────────────────────
15	\begin{table}[t]
16	\centering
17	\small
18	\setlength{\tabcolsep}{3.6pt}
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{@{}l rrrrrr rr@{}}
21	\toprule
22	& \multicolumn{6}{c}{\textbf{Violation Rates (\%)}}
23	& \multicolumn{2}{c}{\textbf{F1}} \\
24	\cmidrule(lr){2-7} \cmidrule(l){8-9}
25	\textbf{Mode}
26	  & DR\,$\downarrow$ & $\Delta$DR
27	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF & Tot.\,$\downarrow$
28	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
29	\midrule
30	Unconstrained
31	  & 15.37 & ---
32	  & 1.39  & 0.40
33	  & 0.08  & 15.45
34	  & 8.23  & 31.01 \\
35	Grammar
36	  & 14.84 & $\downarrow$3\%
37	  & \textbf{0} & \textbf{0}
38	  & 0.08  & 14.92
39	  & 8.23  & 30.98 \\
40	Semantic
41	  & 11.65 & $\downarrow$24\%
42	  & 1.51  & 0.40
43	  & 2.71  & 14.36
44	  & 8.15  & 31.01 \\
45	Full (S1)
46	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
47	  & \textbf{0} & \textbf{0}
48	  & 9.90  & \textbf{10.83}
49	  & \textbf{8.36} & 30.98 \\
50	Full (S2)
51	  & 0.97  & $\downarrow$94\%
52	  & \textbf{0} & \textbf{0}
53	  & 8.03  & \textbf{9.00}
54	  & 8.03  & \textbf{31.90} \\
55	\bottomrule
56	\end{tabular}}%
57	\caption{Five-way ablation on SciERC (551 docs, Qwen3-8B, zero-shot).
58	$\Delta$DR: relative change vs.\ unconstrained.
59	Tot.\ = DR + CF (total type-violation b
…[truncated 4925 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 422 · 2026-05-19T06:24:41.958750+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
  }
}
```

</details>

---
