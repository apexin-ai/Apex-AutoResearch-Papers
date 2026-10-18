# Director coordination — Part 9 of 10

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

[← Part 8](part-008.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 10 →](part-010.md) · [Structured JSON](../../../sessions/0f/0fa49ecfe50583d66f9a.json)

## Round 226

### Tool result

_source line 2715 · 2026-05-21T21:05:31.905439+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2716 · 2026-05-21T21:05:38.637925+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 2717 · 2026-05-21T21:05:38.688537+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2718 · 2026-05-21T21:05:41.483003+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 2719 · 2026-05-21T21:05:42.788230+00:00_

{"result":"# 项目 schema-dag-extraction 概况\n\n## 实验状态 (69 个)\n\n- **exp012_llama_8b_r2_exp2**: DONE (negative) — \n- **exp012_llama_8b_r2**: DONE (success) — \n- **exp006_interaction_2x2**: DONE (negative) — \n- **exp012_llama_awq**: DONE (killed) — \n- **exp012_llama_8b_r3**: DONE (failed) — \n- **exp012_llama_8b**: DONE (killed) — \n- **exp_fewrel_40rel_r3**: DONE (failed) — \n- **exp_fewrel_40rel_r2**: DONE (failed) — \n- **exp012_llama_fewnerd_r4**: DONE (failed) — \n- **exp012_llama_8b_fewnerd**: DONE (failed) — \n- **exp_fewrel_40rel**: DONE (failed) — \n- **exp012_llama_fewnerd_r3**: DONE (failed) — \n- **exp012_llama_fewnerd_r2**: DONE (failed) — \n- **exp012_llama_fewnerd**: DONE (failed) — \n- **exp008_sdgd_zero_fewnerd**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- prompt_sensitivity（准备中）\n- prompt_sensitivity_dry4（准备中）\n- prompt_sensitivity_dry3（准备中）\n- prompt_sensitivity_dry2（准备中）\n- prompt_sensitivity_dry（准备中）\n- exp_aggregation_monte_carlo（准备中）\n- exp_scs_name_def_ablation（准备中）\n- exp_fewrel_contamination_check（准备中）\n- exp017_gpt4o_mini_fewrel（准备中）\n- exp_cross_embedding_sensitivity（准备中）\n- …另有 2 项\n\n## 近期结论\n- **exp_llama70b_ner_bcs_null** (success): Batch-level BCS does not correlate with NER F1 for LLaMA-3.1-70B-FP8, consistent with the BCS null observed in Qwen3-32B (r=0.004) and LLaMA-8B (r=-0.12). The confusability metric is not predictive of extraction quality at the batch level. ← 基于 exp012_llama_8b_r2_exp2\n  [LLaMA-70B NER BCS-null analysis](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_llama70b_ner_bcs_null/data/bcs_null_analysis.json)\n- **exp_gemini_flash_bcs_controlled** (success): BCS-accuracy negative correlation observed on open-weight models (Qwen3-32B, LLaMA) generalizes to proprietary API models. Gemini 2.5 Flash should show significant BCS gap on extreme-BCS batches at count 8 and count 16, confirming Dimension 2 is architecture-family-in
…[truncated 1221 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1305
}
```

</details>

---


### Tool call

_source line 2720 · 2026-05-21T21:05:42.939357+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2721 · 2026-05-21T21:05:42.939801+00:00_

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
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	\usepackage{listings}
16	
17	\title{How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	
28	\input{related_work}
29	
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	\begin{enumerate}[leftmargin=*,itemsep=2pt]
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B; cross-model validation (LLaMA-8B, LLaMA-70B, Gemini Flash) covers Dimensions~1--2 (count curves, BCS-controlled extremes) but does not replicate secondary analyses (error taxonomy, prompt sensitivity, TOST equivalence). DocRED $R^2 = 0.58$ and the error taxonomy are single-model results. Gemini provides only partial, leverage-sensitive corroboration (leave-one-out $r{:}\;{-}0.80 \to {-}0.42$; Appendix~\ref{sec:appendix_cross_model_gemini}); proprietary-model generalization remains open.
41	
42	\item \textbf{Effect size and statistical design.} Pairwise SCS explains a small fraction of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\times$ BCS interaction is bounded on FewRel but nonzero on DocRED, partially confounded by BCS range restriction at higher counts (Appendix~\ref{sec:appendix_factorial}); logit-scale evidence remains inconclusive. DocRED count curves use 5 batches per level due to higher per-batch evaluation cost. BCS-controlled experiments use a single seed with greedy decoding; residual variance is small (Appendix~\ref{app:variance-de
…[truncated 5286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2722 · 2026-05-21T21:05:50.722211+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2723 · 2026-05-21T21:05:50.823217+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2724 · 2026-05-21T21:05:55.391400+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 2725 · 2026-05-21T21:05:57.700938+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 2726 · 2026-05-21T21:05:58.153366+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2727 · 2026-05-21T21:05:58.254235+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 2728 · 2026-05-21T21:06:03.177341+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here are the key submission guidelines and author instructions for the ACL Rolling Review (ARR) 2026:

## Key Requirements

**Originality and Content:** All submitted papers are expected to describe original, completed and unpublished work. See the publication ethics guidelines on re-use of text from other publications (no more than 10% total tokens).

**Anonymity:** Papers must not include authors' names and affiliations. Furthermore, self-references that reveal the authors' id
…[truncated 1141 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 7785
}
```

</details>

---


### Tool result

_source line 2729 · 2026-05-21T21:06:03.228055+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'schema-dag-extraction'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 4973
}
```

</details>

---


### Tool call

_source line 2730 · 2026-05-21T21:06:07.853520+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline page limit requirements site:2026.emnlp.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline page limit requirements site:2026.emnlp.org"
  }
}
```

</details>

---


### Tool call

_source line 2731 · 2026-05-21T21:06:08.305560+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2732 · 2026-05-21T21:06:09.410387+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction degrades as schema complexity grows, yet prior work conflates two factors: type count and type confusability. We present what is, to our knowledge, the first controlled study isolating these factors across NER, RE, and event detection on four datasets, using the Schema Confusability Score (SCS) and its batch-level aggregation (BCS) as operational tools. Three findings emerge.
3	(1)~Degradation operates along two dimensions: count-related recall decline (up to $-$49\,pp) and confusability-related type substitution, with bounded interaction on FewRel.
4	(2)~In RE, BCS explains ${\sim}$22\% of cross-batch accuracy variance on FewRel ($R^2 = 0.218$, ecological level), replicating across three open-weight model families (8B--70B), two formats, and five prompts; NER batch-level signal is not detected at current power, revealing a task asymmetry.
5	(3)~Schema decomposition fails due to merge amplification (NER, ED) and routing failure (RE), though oracle routing confirms the two dimensions are independently addressable.
6	\end{abstract}
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 1104
}
```

</details>

---


### Tool call

_source line 2733 · 2026-05-21T21:06:09.461051+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2734 · 2026-05-21T21:06:09.662217+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\footnote{Code and data will be released upon acceptance.} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, and is attractive for applications where annotation is expensive or schemas evolve frequently \citep{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level), near-halving or worse. This degradation is not academic: real-world ontologies routinely define 50--200+ types, which places them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What explains this degradation? Prior decomposition strategies \citep{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	This study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accuracy.
9	
10	We ask three questions. \textbf{RQ1}: Does type confusability independently predi
…[truncated 3540 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 2735 · 2026-05-21T21:06:09.712804+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "writing_plan.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "writing_plan.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 2736 · 2026-05-21T21:06:13.025364+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline page limit requirements site:2026.emnlp.org"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"EMNLP 2026 Paper Integrity Policy - EMNLP 2026","url":"https://2026.emnlp.org/paper-integrity-policy/"},{"title":"Organizing Committee - EMNLP 2026 - SIGDAT","url":"https://2026.emnlp.org/organization/"}]

I found relevant information about EMNLP 2026 call for papers. Based on the search results from the official EMNLP 2026 website, here's what I found:

## Submission Deadline

The paper submission deadline for the Industry Track is June 16, 2026 (11:59 PM UTC-12:00, AoE). All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

## Page Limit Requirements

Unfortunately, the search results from the main conference call for papers page did not include specific page limit information in the excerpts returned. However, I did find page limit-related information for the Industry Track in the form of limitations:

Authors are required to discuss the limitations of their work in a dedicated section titled "Limitations", which should be included at the end of the paper, before the references, and it will not count toward the page limit.
…[truncated 397 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 5171
}
```

</details>

---


### Tool result

_source line 2737 · 2026-05-21T21:06:13.025943+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/writing_plan.yaml\", \"content\": \"# Writing Plan — schema-dag-extraction\\n# Generated: 2026-05-15\\n# Venue: EMNLP 2026 (ARR May 25 cycle)\\n# Format: 8 pages main text + unlimited references\\n# Mode: Full Draft (2-claim analysis paper + SDGD negative result)\\n\\nmeta:\\n  title: \\\"Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\\\"\\n  venue: EMNLP 2026 Main\\n  submission_deadline: \\\"2026-05-25\\\"\\n  page_limit: 8\\n  template: \\\"acl2023\\\"  # ARR uses ACL rolling review LaTeX template\\n  template_note: \\\"No EMNLP 2026 template found locally. Using acl2023.sty (standard ARR template). Worker must download from https://github.com/acl-org/acl-style-files if not available.\\\"\\n  primary_model: \\\"Qwen3-32B-FP8\\\"\\n  secondary_model: \\\"LLaMA-3.1-8B-Instruct (exp-012, D022: 70B→8B cross-scale validation)\\\"\\n  datasets: [\\\"Few-NERD (66 types)\\\", \\\"FewRel (80 relations)\\\", \\\"MAVEN (168 event types)\\\"]\\n\\n# =============================================================================\\n# PAPER OUTLINE\\n# =============================================================================\\n\\npaper_outline:\\n  - section: abstract\\n    word_budget: 250\\n    dependencies: [introduction, experiments, results, sdgd_negative, conclusion]\\n    key_content:\\n      - Problem: training-free LLM IE degrades on complex schemas; prior work conflates count and confusability\\n      - Method: first controlled empirical study isolating type confusability from count across 3 tasks\\n      - Findings: multi-channel degradation (count→recall, confusability→type confusion); pairwise SCS robust cross-task (r=0.11-0.13); effect amplifies 3.4× with schema complexity; per-type aggregation confounded on homogeneous schemas\\n      - Negative result: naive confusability-aw
…[truncated 1469 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 3313
}
```

</details>

---


### Tool call

_source line 2738 · 2026-05-21T21:06:17.391706+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "limit": "120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "limit": "120"
  }
}
```

</details>

---


### Tool result

_source line 2739 · 2026-05-21T21:06:17.845395+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	All experiments use Qwen3-32B unless noted; cross-model validation covers Dimensions~1--2, while secondary analyses (error taxonomy, DocRED $R^2$, TOST) remain single-model. Unless otherwise noted, all experiments use the v1 prompt (\S\ref{sec:model}; Appendix~\ref{sec:appendix_prompts}).
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	Figure~\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where the elimination of type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\%$\to$38.7\%, $-$56\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}). The pattern is stable across three seeds (max $\Delta = 10.7$\,pp, within 1\,SD; intra-batch variance exceeds inter-seed variance by ${>}$5$\times$; Appendix~\ref{app:variance-decomposition}). Formal trend analysis confirms monotonic RE decline (Jonckheere-Terpstra $J = 109{,}707$, $p < 0.001$). Count curves establish trend direction; magnitude estimation relies on the higher-powered BCS-controlled experiments (\S\ref{sec:bcs_controlled}).
10	
11	\subsection{Pairwise Confusability and Type Confusion}
12	\label{sec:pairwise}
13	
14	We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate (the fraction of $t_i$ gold instances misclassified as $t_j$) and correlate it with $\text{SCS}(t_i, t_j)$. Table~\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\% CIs.
15	
16	\begin{table}[t]
17	\centering
18	\small
19	\resizebox{\columnwidth}{!}{
…[truncated 12041 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 2740 · 2026-05-21T21:06:17.845902+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 2741 · 2026-05-21T21:06:18.448896+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \citep{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains and is suitable for cross-domain evaluation. We sample 1{,}000 instances uniformly from the test set; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \citep{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). A held-out validation confirms SCS--confusion generalization across the split boundary (Appendix~\ref{app:scs-heldout-validation}). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound; this balance makes it the primary dataset for BCS analysis.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \citep{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We s
…[truncated 9195 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 2742 · 2026-05-21T21:06:18.650024+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 2743 · 2026-05-21T21:06:18.750834+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention is to partition the schema so confusable types never co-occur. We test \textbf{Schema-DAG-Guided Decomposition} (SDGD), which applies greedy graph coloring on the SCS graph to assign types to low-confusability batches.
5	
6	\paragraph{NER and ED: merge amplification.}
7	All decomposition modes fall below the single-pass NER baseline (F1\,=\,0.445): SDGD obtains 0.251, random batching 0.320. The core failure is \emph{merge amplification}: presenting text $k$ times collapses precision (0.563$\to$0.210--0.249). MAVEN event detection replicates this (precision 0.287$\to$0.091; Appendix~\ref{sec:appendix_sdgd}).
8	
9	\paragraph{RE: routing failure.}
10	Oracle routing recovers accuracy (0.802 vs.\ 0.504 single-pass; Table~\ref{tab:batch_composition}), but confusability-aware grouping yields only +1.4\,pp over random ($p \approx 0.19$, n.s.). All practical routing strategies fall below the single-pass baseline (Appendix~\ref{sec:appendix_routing}); the bottleneck is routing accuracy rather than partitioning quality.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2744 · 2026-05-21T21:06:18.751229+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2745 · 2026-05-21T21:06:18.803140+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions and mechanisms.}
5	\looseness=-1
6	The decomposition applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\S\ref{sec:centrality_confound}). RE effects replicate across three open-weight models (8B--70B), two formats, five prompts, and two datasets; NER null not detected on three models (8B--70B). Weak pairwise signals ($R^2 {=}\, 1.3\%$) compound into batch effects ($R^2 {\approx}\, 22\%$ on FewRel, ecological level); the NER--RE asymmetry reflects different error-mode structures (\S\ref{sec:multi_channel}) and compressed BCS variance (Appendix~\ref{sec:appendix_ner_power}).
7	
8	\paragraph{Practical implications and conclusion.}
9	\label{sec:conclusion}
10	\looseness=-1
11	For NER, reducing candidate types is the primary lever. For RE, BCS enables pre-hoc diagnostics (flag SCS${}\,>\,0.85$ pairs; $R^2 {\approx}\, 0.22$ on FewRel); high-SCS pairs dominate type substitution errors (Appendix~\ref{app:error-analysis}). Practitioners can pre-compute SCS to identify high-risk type pairs before deployment, enabling schema-aware pool selection as a preprocessing step. Decompose-then-merge fails (\S\ref{sec:sdgd}), but oracle routing recovers accuracy (72.4\% vs.\ 50.4\%), confirming that count and confusability are independently addressable.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2746 · 2026-05-21T21:06:23.220661+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2747 · 2026-05-21T21:06:23.672933+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \citep{instructuie-2023}, code-style schema encoding \citep{knowcoder-2024,codeie-2023}, annotation-guided extraction \citep{gollie-2024,adelie-2024}, schema-driven decoding \citep{slot-2025,oneke-2025}, and constrained JSON decoding \citep{json-schema-bench-2025,willard2023efficient}. NER methods include zero-shot decomposition \citep{xie-zeroshot-ner-2023,promptner-2023}, distillation \citep{uniner-2024}, and bidirectional encoders \citep{gliner-2024,gliner2-2025}; RE methods include zero-shot triplet extraction \citep{relationprompt-2022}, constrained generation \citep{josifoski-2022-genie}, and shared embedding spaces \citep{boylan-2025-glirel,wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \citep{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. LLM-PEE's union merge suffers the same precision collapse (0.56$\to$0.21; \S\ref{sec:sdgd}). In short, LLM-PEE assumes decomposition helps; we show why it should (confusability), why it does not (merge amplification), and what predicts the degradation (BCS). Other approaches address schema complexity via hard negative mining \citep{iepile-2024}, schema definition optimization \citep{parse-2025}, multi-agent debate \citep{crossagentie-2025,cmas-ner-2025}, and active prompting
…[truncated 2414 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2748 · 2026-05-21T21:06:24.125106+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 2749 · 2026-05-21T21:06:24.677851+00:00_

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
11	\title{Supplementary Material for: How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
12	
13	\author{Anonymous}
14	
15	\begin{document}
16	\maketitle
17	
18	All supplementary material is included in the appendix of the main paper.
19	
20	\end{document}
21	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 2750 · 2026-05-21T21:06:24.878982+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "decisions.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "decisions.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 2751 · 2026-05-21T21:06:24.929952+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/decisions.yaml\", \"content\": \"_next_id: 71\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 16:10 UTC\\n  summary: 项目立项，MVP 验证方案：Experiment 2 (Confusability Controlled) 为核心验证实验\\n  rationale: 'IDEA_BRIEF 的核心假设是 type confusability 独立于 type count 驱动 LLM IE 质量下降。Experiment\\n    2（固定 count 变 BCS）是最直接的假设检验。Pass 标准: |r|≥0.3 且 p<0.05。ACE05 RE + Few-NERD 双数据集验证。ARR\\n    May 25 DDL（11天），MVP 需 1-2 天完成。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 16:15 UTC\\n  summary: 修正 MVP 统计设计：random samples 从 10 增至 25/档，加入 per-type solo baseline 控制变量，核心指标改为\\n    Δ(solo_F1 - batch_F1)\\n  rationale: Reviewer 指出 n=12 下 |r|=0.3 对应 p≈0.34，无法同时满足 |r|≥0.3 且 p<0.05。增至 25 random\\n    batches/档 → n≈54，|r|≥0.27 即可达 p<0.05。同时加入 solo F1 控制 type 固有难度，避免将\\\"类型本身难抽取\\\"误归因于\\\"confusability\\n    效应\\\"。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 23:11 UTC\\n  summary: MVP 分析方法从 Δ(solo-batch) 切换到 within-count Pearson r(F1, BCS)，pass 标准更新为\\n    |r|≥0.3 at fixed count\\n  rationale: Exp 1 发现 count curve 方向反转（F1 随 count 上升），根因是低 count 时模型过度 hallucinate（pred/gold=8x\\n    at count=1）。solo baseline 处于极端行为模式，Δ 被跨 count 行为差异污染。改为 within-count 对比更干净：同一\\n    count 下比较不同 BCS 的 F1，直接检验 confusability 独立效应。\\n  related_experiments:\\n  - exp_id: exp001_count_baseline\\n    role: evidence\\n    result: count curve reversed, hallucination at low count\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 23:31 UTC\\n  summary: MVP 主指标更新为 within-count r(recall, BCS)，F1 因 over-prediction confound 降为补充指标\\n  rationale: Exp 1 text-match 重评估发现：recall 单调下降（0.72→0.42，符合预期），precision 单调上升（0.11→0.52，over-prediction\\n    减少），F1 受 precision 主导而反转。within-count 分析中 precision confound 在同一 count 下近似恒定，F1\\n    仍可用；但 recall 更干净且直接反映 type confusion。WrongType 错误（text 正确但 type 错标）随 count 从 0\\n    升至 2434，直
…[truncated 3541 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2752 · 2026-05-21T21:06:29.900422+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 2753 · 2026-05-21T21:06:30.302533+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 2754 · 2026-05-21T21:06:30.457195+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
  "pages": "1-2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
    "pages": "1-2"
  }
}
```

</details>

---


### Tool result

_source line 2755 · 2026-05-21T21:06:30.608324+00:00_

PDF pages extracted: 2 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf (463.1KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2756 · 2026-05-21T21:06:33.926982+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
  "pages": "3-8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
    "pages": "3-8"
  }
}
```

</details>

---


### Tool result

_source line 2757 · 2026-05-21T21:06:34.358019+00:00_

PDF pages extracted: 6 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf (463.1KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 431
}
```

</details>

---


### Tool call

_source line 2758 · 2026-05-21T21:06:41.125530+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
  "pages": "9-16"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
    "pages": "9-16"
  }
}
```

</details>

---


### Tool result

_source line 2759 · 2026-05-21T21:06:41.629517+00:00_

PDF pages extracted: 8 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf (463.1KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 2760 · 2026-05-21T21:06:42.391700+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 2761 · 2026-05-21T21:06:43.094941+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 2762 · 2026-05-21T21:06:43.546974+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent/config.yaml 2>/dev/null || find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent -name \"*.yaml\" -maxdepth 1 2>/dev/null | head -5",
  "description": "Check project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent/config.yaml 2>/dev/null || find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent -name \"*.yaml\" -maxdepth 1 2>/dev/null | head -5",
    "description": "Check project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 2763 · 2026-05-21T21:06:43.748365+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 2764 · 2026-05-21T21:06:51.731634+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2765 · 2026-05-21T21:06:52.685911+00:00_

1	
2	# Review Issues Tracker
3	# Updated: 2026-05-21 (Round 24 Fresh — Action Matrix dispatched, D070)
4	
5	# ============================================================
6	# R24 MUST-FIX (5 items, R1+R2 consensus)
7	# ============================================================
8	
9	- id: R24-C1
10	  summary: "DocRED R²=58% confounded by centrality (VIF=50.9), must not be headline claim"
11	  category: method
12	  severity: critical
13	  status: in_progress
14	  first_raised_round: 23
15	  last_seen_round: 24
16	  mentions:
17	    - {round: 23, reviewers: [R1, R2], note: "R23-C2: VIF=50.9, 弱化措辞"}
18	    - {round: 24, reviewers: [R1, R2], note: "Fresh reviewers still anchored on 58% in Abstract. Must recenter on FewRel R²=22%."}
19	  action_items:
20	    - {round: 23, action: "弱化 DocRED 偏相关措辞 → 'reported for completeness'", assigned_to: "Agent", status: resolved}
21	    - {round: 24, action: "Abstract/正文 recenter on FewRel R²≈22% as headline; DocRED demoted to 'directionally consistent but confounded'", assigned_to: "Agent", status: in_progress}
22	  resolution: ""
23	  resolution_round: null
24	
25	- id: R24-C2
26	  summary: "Gemini BCS-controlled driven by single leverage point, statistically fragile"
27	  category: experiment
28	  severity: critical
29	  status: in_progress
30	  first_raised_round: 23
31	  last_seen_round: 24
32	  mentions:
33	    - {round: 23, reviewers: [R1, R2], note: "R23-W4: leave-one-out sensitivity"}
34	    - {round: 24, reviewers: [R1, R2], note: "升级为 Must-Fix。Pearson r -0.80→-0.42, Spearman ρ -0.40→-0.18 (p=0.64)."}
35	  action_items:
36	    - {round: 23, action: "报告 leave-one-out + open-weight vs proprietary 分层", assigned_to: "Agent", status: resolved}
37	    - {round: 24, action: "正文改为 'directionally consistent but statistically fragile'; cross-model claim → '3 open-weight families + partial proprietary'", assigned_to: "Agent", status: in_progress}
38	  resolution: ""
39	  resolution_round: null
40	
41	- id: R24-C3
42	  summary: "Ecolo
…[truncated 12848 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 2766 · 2026-05-21T21:06:52.686397+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
  "pages": "17-20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
    "pages": "17-20"
  }
}
```

</details>

---


### Tool result

_source line 2767 · 2026-05-21T21:06:54.142062+00:00_

PDF pages extracted: 4 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf (463.1KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 1455
}
```

</details>

---


### Tool call

_source line 2768 · 2026-05-21T21:06:54.448958+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" -l 2>/dev/null; grep -r \"paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/ --include=\"*.yaml\" --include=\"*.yml\" -l 2>/dev/null | head -5",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" -l 2>/dev/null; grep -r \"paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/ --include=\"*.yaml\" --include=\"*.yml\" -l 2>/dev/null | head -5",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 2769 · 2026-05-21T21:06:54.750615+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 2770 · 2026-05-21T21:07:42.804743+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "schema-dag-extraction",
  "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "schema-dag-extraction",
    "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
  }
}
```

</details>

---


### Tool call

_source line 2771 · 2026-05-21T21:07:43.306881+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 2772 · 2026-05-21T21:08:10.682683+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 27877
}
```

</details>

---


### Tool result

_source line 2773 · 2026-05-21T21:08:10.683151+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 27376
}
```

</details>

---


### Tool call

_source line 2774 · 2026-05-21T21:08:11.039355+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。\n\n## Venue 信息\n- **Venue**: EMNLP 2026 (ACL Rolling Review, May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **格式**: Long paper, 正文 8 页 + 无限 references\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名**: Double-blind\n- **Limitations**: 必须有独立 Limitations 章节（不计入页数）\n- **Checklist**: 在 OpenReview form 中填写，不在 PDF 中\n\n## 论文路径\n- LaTeX: `projects/schema-dag-extraction/docs/paper/main.tex`（含 `\\input` 子文件）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf`\n\n## 论文概要\n标题: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n这是一篇实证分析论文，研究 training-free LLM 信息抽取中 schema 复杂度（type count 和 type confusability）如何独立驱动性能下降。提出 SCS/BCS 指标量化 confusability，在 4 个数据集（Few-NERD, FewRel, DocRED, MAVEN）上做了 count curve 和 BCS-controlled 实验。主要发现：(1) 两维度独立降级（count→recall, confusability→type substitution）；(2) BCS 在 FewRel 上解释 ~22% RE accuracy variance（ecological level），NER 无 batch-level 信号；(3) Schema decomposition 因 merge amplification 和 routing failure 失败。\n\n## 你的审查侧重\n请严格聚焦以下方面：\n\n1. **统计方法有效性**\n   - SCS/BCS 指标定义是否合理？embedding cosine similarity 作为 confusability proxy 的局限性\n   - BCS-controlled 实验设计：greedy extreme-batch construction 是否引入系统偏差？\n   - TOST 等价检验：margin 选择（±3pp）是否合理？logit-scale 不一致如何解读？\n   - ecological correlation (pairwise r²~1.3% → batch R²~22%)：Robinson (1950) ecological fallacy 风险评估\n\n2. **实验设计与控制**\n   - Confound 控制：type frequency、degree centrality、domain coverage 的处理是否充分？\n   - DocRED VIF=50.9 对 R²=58% 的影响——这个数字是否可信？\n   - Within-pool vs independent pool comparison 的有效性\n   - Single seed + greedy decoding + FP8 non-determinism：variance decomposition 是否充分？\n\n3. **Cross-model validation 覆盖度**\n   - 主要发现（count curves, BCS-controlled）在 3 open-weight models 上验证；但 error taxonomy, DocRED R², TOST, SDGD 均为 single-model\n   - Gemini Flash：leave-one-out sensitivity (r: -0.80→-0.42, p=0.22) 的严重性\n   - NER batch-level null 在 3 模型上确认但未在 Gemini 上测试\n\n4. **Effect size 诚实性**\n   - pairwise r²~1.3% 是否过小？\"amplification\" 叙事是否令人信服？\n   - IQR-predicted gap 仅 2.2pp——实际意义有多大？\n   - NER null 的解释：insufficient power vs genuine absence——论文的叙述是否自洽？\n\n5. **可复现性**\n   - 数据和代码 \"released upon acceptance\"——是否提供了足够的实验细节？\n   - FewRel train+val 合并使用是否有 contamination 风险？\n\n请输出标准审稿报告：Summary → Strengths → Weaknesses (编号 W1, W2, ...) → Questions → Missing References → Overall Assessment (评分 + 置信度)。Weaknesses 按严重性排序（Must-Fix / Should-Fix / Minor）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。\n\n## Venue 信息\n- **Venue**: EMNLP 2026 (ACL Rolling Review, May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **格式**: Long paper, 正文 8 页 + 无限 references\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名**: Double-blind\n- **Limitations**: 必须有独立 Limitations 章节（不计入页数）\n- **Checklist**: 在 OpenReview form 中填写，不在 PDF 中\n\n## 论文路径\n- LaTeX: `projects/schema-dag-extraction/docs/paper/main.tex`（含 `\\input` 子文件）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf`\n\n## 论文概要\n标题: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n这是一篇实证分析论文，研究 training-free LLM 信息抽取中 schema 复杂度（type count 和 type confusability）如何独立驱动性能下降。提出 SCS/BCS 指标量化 confusability，在 4 个数据集（Few-NERD, FewRel, DocRED, MAVEN）上做了 count curve 和 BCS-controlled 实验。主要发现：(1) 两维度独立降级（count→recall, confusability→type substitution）；(2) BCS 在 FewRel 上解释 ~22% RE accuracy variance（ecological level），NER 无 batch-level 信号；(3) Schema decomposition 因 merge amplification 和 routing failure 失败。\n\n## 你的审查侧重\n请严格聚焦以下方面：\n\n1. **统计方法有效性**\n   - SCS/BCS 指标定义是否合理？embedding cosine similarity 作为 confusability proxy 的局限性\n   - BCS-controlled 实验设计：greedy extreme-batch construction 是否引入系统偏差？\n   - TOST 等价检验：margin 选择（±3pp）是否合理？logit-scale 不一致如何解读？\n   - ecological correlation (pairwise r²~1.3% → batch R²~22%)：Robinson (1950) ecological fallacy 风险评估\n\n2. **实验设计与控制**\n   - Confound 控制：type frequency、degree centrality、domain coverage 的处理是否充分？\n   - DocRED VIF=50.9 对 R²=58% 的影响——这个数字是否可信？\n   - Within-pool vs independent pool comparison 的有效性\n   - Single seed + greedy decoding + FP8 non-determinism：variance decomposition 是否充分？\n\n3. **Cross-model validation 覆盖度**\n   - 主要发现（count curves, BCS-controlled）在 3 open-weight models 上验证；但 error taxonomy, DocRED R², TOST, SDGD 均为 single-model\n   - Gemini Flash：leave-one-out sensitivity (r: -0.80→-0.42, p=0.22) 的严重性\n   - NER batch-level null 在 3 模型上确认但未在 Gemini 上测试\n\n4. **Effect size 诚实性**\n   - pairwise r²~1.3% 是否过小？\"amplification\" 叙事是否令人信服？\n   - IQR-predicted gap 仅 2.2pp——实际意义有多大？\n   - NER null 的解释：insufficient power vs genuine absence——论文的叙述是否自洽？\n\n5. **可复现性**\n   - 数据和代码 \"released upon acceptance\"——是否提供了足够的实验细节？\n   - FewRel train+val 合并使用是否有 contamination 风险？\n\n请输出标准审稿报告：Summary → Strengths → Weaknesses (编号 W1, W2, ...) → Questions → Missing References → Overall Assessment (评分 + 置信度)。Weaknesses 按严重性排序（Must-Fix / Should-Fix / Minor）。"
  }
}
```

</details>

---


### Tool result

_source line 2775 · 2026-05-21T21:08:32.106319+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21066
}
```

</details>

---


### Tool call

_source line 2776 · 2026-05-21T21:08:32.257227+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量** 审查。\n\n## Venue 信息\n- **Venue**: EMNLP 2026 (ACL Rolling Review, May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **格式**: Long paper, 正文 8 页 + 无限 references\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名**: Double-blind\n- **Limitations**: 必须有独立 Limitations 章节（不计入页数）\n- **Checklist**: 在 OpenReview form 中填写，不在 PDF 中\n\n## 论文路径\n- LaTeX: `projects/schema-dag-extraction/docs/paper/main.tex`（含 `\\input` 子文件）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf`\n\n## 论文概要\n标题: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n实证分析论文，首次通过 controlled design 隔离 type count 和 type confusability 对 training-free LLM IE 性能的独立影响。使用 SCS（Schema Confusability Score）和 BCS（Batch Confusability Score），在 NER/RE/ED 三个任务、四个数据集上实验。核心贡献是 BCS-controlled batch design methodology（隔离 confusability vs count），而非 SCS 指标本身（继承自 LLM-PEE）。\n\n## 你的审查侧重\n请严格聚焦以下方面：\n\n1. **新颖性评估（vs prior work）**\n   - SCS/BCS 与 LLM-PEE (Liu et al., 2025) 的 embedding-similarity criterion 的区别：论文声称 \"metric is a means; methodology is the contribution\"——这个定位是否令人信服？\n   - BCS-controlled batch design 作为方法论贡献的新颖性：是否只是 confound control 的标准统计实践？\n   - 与其他 schema complexity 工作（UniNER, PARSE, CROSSAGENTIE, CMAS-NER）的区分是否清晰？\n   - 负面结果（SDGD 失败）的贡献价值\n\n2. **贡献完整性**\n   - 三个 contributions 是否 well-supported？有无 overclaim？\n   - \"first controlled study\"——是否真的是 first？Related work 覆盖是否遗漏了类似的 controlled study？\n   - Task asymmetry (RE works, NER doesn't) 的解释深度是否足够？\n   - Discussion/Conclusion 是否过度压缩？是否有遗漏的 practical implications？\n\n3. **Related Work 覆盖**\n   - 是否遗漏重要相关工作？特别关注：\n     - 2025-2026 年的 schema complexity / LLM IE 新工作\n     - 其他领域的 confusability/confusion 研究（CV label confusion, taxonomy design）\n     - ecological correlation / Simpson's paradox 在 NLP 中的先例\n   - 引用是否真实？是否有可疑的 fabricated citation？\n\n4. **写作质量**\n   - Abstract：信息密度是否过高？关键 takeaway 是否清晰？\n   - Introduction：RQ 设置是否自然？贡献列表是否过长/过细？\n   - 正文信息密度：统计数字是否过多导致可读性下降？\n   - Limitations 章节：6 条 + 2 段补充——是否过长/冗余？EMNLP 要求只需一小段覆盖 ~3 个点\n   - §5 (SDGD) 和 §6 (Discussion) 篇幅是否合理？\n\n5. **格式合规性**\n   - 正文是否在 8 页以内？\n   - 匿名性检查：是否有泄露作者身份的线索？\n   - References 格式是否一致？\n   - 图表质量和 caption 信息量\n\n请输出标准审稿报告：Summary → Strengths → Weaknesses (编号 W1, W2, ...) → Questions → Missing References → Overall Assessment (评分 + 置信度)。Weaknesses 按严重性排序（Must-Fix / Should-Fix / Minor）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量** 审查。\n\n## Venue 信息\n- **Venue**: EMNLP 2026 (ACL Rolling Review, May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **格式**: Long paper, 正文 8 页 + 无限 references\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名**: Double-blind\n- **Limitations**: 必须有独立 Limitations 章节（不计入页数）\n- **Checklist**: 在 OpenReview form 中填写，不在 PDF 中\n\n## 论文路径\n- LaTeX: `projects/schema-dag-extraction/docs/paper/main.tex`（含 `\\input` 子文件）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf`\n\n## 论文概要\n标题: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n实证分析论文，首次通过 controlled design 隔离 type count 和 type confusability 对 training-free LLM IE 性能的独立影响。使用 SCS（Schema Confusability Score）和 BCS（Batch Confusability Score），在 NER/RE/ED 三个任务、四个数据集上实验。核心贡献是 BCS-controlled batch design methodology（隔离 confusability vs count），而非 SCS 指标本身（继承自 LLM-PEE）。\n\n## 你的审查侧重\n请严格聚焦以下方面：\n\n1. **新颖性评估（vs prior work）**\n   - SCS/BCS 与 LLM-PEE (Liu et al., 2025) 的 embedding-similarity criterion 的区别：论文声称 \"metric is a means; methodology is the contribution\"——这个定位是否令人信服？\n   - BCS-controlled batch design 作为方法论贡献的新颖性：是否只是 confound control 的标准统计实践？\n   - 与其他 schema complexity 工作（UniNER, PARSE, CROSSAGENTIE, CMAS-NER）的区分是否清晰？\n   - 负面结果（SDGD 失败）的贡献价值\n\n2. **贡献完整性**\n   - 三个 contributions 是否 well-supported？有无 overclaim？\n   - \"first controlled study\"——是否真的是 first？Related work 覆盖是否遗漏了类似的 controlled study？\n   - Task asymmetry (RE works, NER doesn't) 的解释深度是否足够？\n   - Discussion/Conclusion 是否过度压缩？是否有遗漏的 practical implications？\n\n3. **Related Work 覆盖**\n   - 是否遗漏重要相关工作？特别关注：\n     - 2025-2026 年的 schema complexity / LLM IE 新工作\n     - 其他领域的 confusability/confusion 研究（CV label confusion, taxonomy design）\n     - ecological correlation / Simpson's paradox 在 NLP 中的先例\n   - 引用是否真实？是否有可疑的 fabricated citation？\n\n4. **写作质量**\n   - Abstract：信息密度是否过高？关键 takeaway 是否清晰？\n   - Introduction：RQ 设置是否自然？贡献列表是否过长/过细？\n   - 正文信息密度：统计数字是否过多导致可读性下降？\n   - Limitations 章节：6 条 + 2 段补充——是否过长/冗余？EMNLP 要求只需一小段覆盖 ~3 个点\n   - §5 (SDGD) 和 §6 (Discussion) 篇幅是否合理？\n\n5. **格式合规性**\n   - 正文是否在 8 页以内？\n   - 匿名性检查：是否有泄露作者身份的线索？\n   - References 格式是否一致？\n   - 图表质量和 caption 信息量\n\n请输出标准审稿报告：Summary → Strengths → Weaknesses (编号 W1, W2, ...) → Questions → Missing References → Overall Assessment (评分 + 置信度)。Weaknesses 按严重性排序（Must-Fix / Should-Fix / Minor）。"
  }
}
```

</details>

---


### Tool result

_source line 2777 · 2026-05-21T21:08:33.666597+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1409
}
```

</details>

---


### Tool call

_source line 2778 · 2026-05-21T21:08:42.908085+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent -type f 2>/dev/null | head -20; find /home/ubuntu/.agent-ml-research-idea_gen_0509_18 -maxdepth 2 -name \"config*.yaml\" -o -name \"config*.yml\" -o -name \"project*.yaml\" 2>/dev/null | head -10",
  "description": "Find project config files for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent -type f 2>/dev/null | head -20; find /home/ubuntu/.agent-ml-research-idea_gen_0509_18 -maxdepth 2 -name \"config*.yaml\" -o -name \"config*.yml\" -o -name \"project*.yaml\" 2>/dev/null | head -10",
    "description": "Find project config files for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 2779 · 2026-05-21T21:08:43.008981+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2780 · 2026-05-21T21:08:47.885036+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18 -maxdepth 3 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | grep -i config | head -10; find /home/ubuntu/agent-ml-research -maxdepth 2 -name \"*.yaml\" 2>/dev/null | grep -i config | head -5",
  "description": "Search for project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18 -maxdepth 3 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | grep -i config | head -10; find /home/ubuntu/agent-ml-research -maxdepth 2 -name \"*.yaml\" 2>/dev/null | grep -i config | head -5",
    "description": "Search for project config files"
  }
}
```

</details>

---


### Tool result

_source line 2781 · 2026-05-21T21:08:47.985913+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/collapse-aware-mixing.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/schema-dag-extraction.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/venue_rules/corl-2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/venue_rules/emnlp-2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/resources.yaml
/home/ubuntu/agent-ml-research/config/ralph_loop.yaml
/home/ubuntu/agent-ml-research/config/images.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2782 · 2026-05-21T21:08:52.103687+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/schema-dag-extraction.yaml 2>/dev/null",
  "description": "Check external review config for project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/schema-dag-extraction.yaml 2>/dev/null",
    "description": "Check external review config for project"
  }
}
```

</details>

---


### Tool result

_source line 2783 · 2026-05-21T21:08:52.204933+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2784 · 2026-05-21T21:08:56.831038+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -i \"external\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/schema-dag-extraction.yaml 2>/dev/null; echo \"---\"; grep -i \"external\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/backend.yaml 2>/dev/null",
  "description": "Search for external review or paperreview config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -i \"external\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/schema-dag-extraction.yaml 2>/dev/null; echo \"---\"; grep -i \"external\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/backend.yaml 2>/dev/null",
    "description": "Search for external review or paperreview config"
  }
}
```

</details>

---


### Tool result

_source line 2785 · 2026-05-21T21:08:56.882984+00:00_

---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Assistant

_source line 2786 · 2026-05-21T21:09:08.997250+00:00_

外部审稿未配置（项目 config 中无 `external_review.paperreview_ai` 字段），跳过。

**当前状态**：
- Reviewer 1（方法严谨性）：已派发 ✓
- Reviewer 2（新颖性+完整性）：已派发 ✓
- 视觉审查 Agent：已启动 ✓
- 外部审稿（Stanford Agentic Reviewer）：未配置，跳过

等待两位 Reviewer 返回初审报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 227

## Round 227

4 recorded events


### User

_source line 2787 · 2026-05-21T21:14:44.392150+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿报告：新颖性 + 完整性 + 写作质量

**论文**: "How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?"
**Venue**: EMNLP 2026 (ACL Rolling Review, May 2026 cycle)

---

## Paper Summary

本文通过受控实验设计研究 schema complexity 如何影响 training-free LLM 信息抽取性能。作者将 schema complexity 分解为两个正交维度——type count 和 type confusability——并使用 Schema Confusability Score (SCS, 继承自 LLM-PEE) 及其 batch 级聚合 Batch Confusability Score (BCS) 作为量化工具。核心方法论贡献是 BCS-controlled batch design：通过构造高/低 BCS batch 来隔离 confusability 对性能的独立影响，排除 count 这一混淆变量。在 NER (Few-NERD)、RE (FewRel, DocRED)、ED (MAVEN) 三个任务四个数据集上，使用 Qwen3-32B 进行实验。主要发现：(1) count 增加单调降低性能（所有任务）；(2) confusability（BCS）独立预测 RE 准确率变异（~22%），但在 NER 中未检测到显著信号；(3) Schema-DAG-Guided Decomposition (SDGD) 未能改善性能，失败原因是 merge amplification 和 routing failure。

---

## 主要优势

**S1. 实验设计严谨**：BCS-controlled batch design 有效隔离了 count 与 confusability 两个因素。factorial analysis (§4.3, Appendix C)、TOST equivalence testing (Appendix C)、bootstrap CIs 等统计方法运用得当，在 NLP 实证研究中属于较高水平。

**S2. 任务覆盖广且分析深入**：跨 NER/RE/ED 三个核心 IE 任务、四个标准数据集，且 error taxonomy decomposition (§4.4, Figure 2) 将 BCS 效应分解到具体错误类型（IntraSub, missed entities），提供了 actionable 的诊断信息。

**S3. 负面结果的诚实报告**：§5 完整报告了 SDGD 的失败及其原因分析（merge amplification, routing failure），这在文献中少见且有价值。Table 7-8 的 decomposition mode 对比清晰展示了失败机制。

**S4. 统计严谨性超出 NLP 论文平均水平**：使用 TOST 检验 NER null result (§4.3)、ecological correlation caveat (引用 Robinson 1950)、cross-model validation (Appendix T, U)、prompt sensitivity analysis (Appendix H)、pair-to-batch aggregation simulation (Appendix N) 等——这些反映了作者对统计推断陷阱的清醒认识。

**S5. 丰富的附录**：26 页附录覆盖了几乎所有可预见的 reviewer 质疑（cross-prompt variants, constrained vs unconstrained decoding, cross-model replication, confound control for degree centrality, batch composition analysis 等），显示了极高的实验完整度。

---

## Must-Fix 问题（影响接收决定）

**W1** [critical] **方法论新颖性不足：BCS-controlled batch design 本质上是标准的分层实验设计**
- 具体位置：§1 Contribution 1, §3.3 Experiment 2, §4.3
- 问题：论文将 "BCS-controlled batch design methodology" 定位为核心贡献（§1: "the contribution is the methodology, not the metric"），但 BCS-controlled batching 本质上是经典的 confound control / stratified experimental design——在统计学和实验心理学中已有数十年历史。具体做法（按 BCS 分层采样 batch，在每个 count level 固定 BCS 高/低组进行比较）就是标准的 blocking design。论文未引用任何实验设计方法论文献（如 Fisher 的 experimental design 原理），也未解释为什么将这一标准技术应用于 LLM IE 领域本身构成方法论贡献。
- 为什么影响接收：如果核心贡献是"标准方法在新领域的应用"，那贡献等级需要降级为 empirical findings 而非 methodology。这会显著影响 excitement 评分。
- 建议修改方向：(a) 重新定位贡献重心——将核心贡献从 "methodology" 转向 "empirical findings enabled by controlled design"，强调发现本身（count-confusability 独立效应、task asymmetry、SDGD 失败机制）的价值；(b) 如坚持 methodology 定位，需要解释 BCS-controlled batching 相对于标准 blocking design 有何领域特定的创新（如 BCS 的 batch-level aggregation 如何处理 IE 特有的 multi-label / variable-instance 问题）。

**W2** [critical] **NER null result 的机制解释不充分**
- 具体位置：§4.3 ("NER batch-level signal is not detected"), §4.4, Limitations #3
- 问题：NER 在所有分析中对 BCS 无显著响应——这是论文最令人意外的发现之一，但机制解释停留在描述层面。§4.4 将错误分解为 IntraSub 和 missed rates，发现 NER missed rates "substantially higher (43-65%)" 且 "non-monotonic"，但仅归因于 "type modes rather than concentrating in type substitution"（第 7 页）。Appendix E.2 的 NER BCS-null power analysis 表明 r ≈ −0.11 "under this restricted range"，但不清楚是统计功效不足（样本量问题）还是真正的零效应。论文同时提出两个矛盾的可能解释：(a) NER 的 confusability 效应确实为零；(b) 效应存在但被 NER 固有的 boundary detection noise 掩盖。这两个假设有不同的 practical implications，但论文未提供区分它们的证据。
- 为什么影响接收：Task asymmetry 是三个 contribution 之一（Contribution 2），但对其最核心的 puzzle（为什么 NER 不响应 BCS）缺乏深入解释，削弱了该贡献的价值。
- 建议修改方向：(a) 设计针对性实验区分上述两个假设——例如在 NER 中仅分析 type substitution errors（排除 boundary errors）后 BCS 是否显著；(b) 至少在正文而非仅附录中明确表述："基于现有证据，我们无法区分零效应与被噪声掩盖的效应"，并讨论各自的 implications。

---

## Should-Fix 问题（影响评分但不一票否决）

**W3** [warning] **Limitations 章节过长，不符合 EMNLP 写作惯例**
- 具体位置：Page 9, Limitations section
- 问题：Limitations 列出 6 个编号点 + 2 段额外讨论（"Causal mechanism" 和 "Data contamination"），占据近整页篇幅。EMNLP 2026 要求 Limitations 章节必须存在但不应包含过多额外内容（"provided they do not contain excessive additional content"）。当前版本的信息密度更像一个 extended discussion section 而非简洁的 limitations 声明。
- 建议：压缩至 3-4 个核心点的一段式写作（~10-15 行），将统计功效分析、data contamination 等技术细节移至附录。

**W4** [warning] **跨模型验证结果未充分整合入正文**
- 具体位置：§3.5 ("All experiments use Qwen3-32B unless noted"), Appendix T, U
- 问题：主实验全部基于 Qwen3-32B 单一模型。跨模型验证（LLaMA-3.1-8B, LLaMA-70B, Gemini 2.5 Flash）仅出现在附录 T 和 U 中。虽然附录结果支持 cross-architecture generalization，但正文中对此的讨论仅有一句话（§6: "Both dimensions thus replicate on a proprietary architecture with unknown training details"）。对于一篇声称发现 "general degradation pattern" 的论文，将泛化证据完全放在附录中不够convincing。
- 建议：在 §4 Results 或 §6 Discussion 中用 1-2 段总结跨模型验证的核心结果（至少报告 LLaMA-70B 和 Gemini 的 count-curve slopes 和 BCS-accuracy correlations），表明发现不依赖于特定模型。

**W5** [warning] **Abstract 信息密度过高，关键 takeaway 被数字淹没**
- 具体位置：Abstract (Page 1)
- 问题：Abstract 在约 150 词中塞入了大量具体数字："`~22% of cross-batch RE accuracy variance`", "`R² = 0.218`", "`p < 0.001`", "`~49 pp`", "`0.72 to ~0.27`"。这使得非专业读者难以提取核心 takeaway。Abstract 应该传达 findings 的 *significance* 而非 *statistical details*。
- 建议：将具体数字移入正文，Abstract 用定性语言概括核心发现（如 "confusability independently explains a substantial portion of RE accuracy variance"）。

**W6** [warning] **Discussion/Conclusion 过度压缩**
- 具体位置：§6 Discussion and Conclusion (Page 8, bottom half)
- 问题：Discussion 和 Conclusion 合并在 Page 8 的下半页（约 25 行），涵盖 SDGD failure diagnosis、boundary conditions、practical implications 三个主题，每个仅 2-3 句。特别是 practical implications（SCS 作为 pre-deployment 诊断工具、schema-aware pool selection、decompose-then-merge 的 precision-recall tradeoff）是论文最有应用价值的部分，但每个仅一句话带过。对于一篇以 empirical insights 为核心贡献的论文，Discussion 应该是 payoff section，当前版本未能充分展开。
- 建议：将 §5 (SDGD, 约 1/3 页) 压缩后释放空间给 Discussion；或将 SDGD 部分整合进 Discussion 作为一个 subsection。

**W7** [warning] **"First controlled study" claim 需要更谨慎的措辞**
- 具体位置：§1 ("To our knowledge, we present the first controlled study isolating type confusability from type count")
- 问题：虽然我未找到直接的 prior controlled study 隔离这两个因素，但 "first" claim 在 NLP 文献中总是有风险的。Chen et al. (2026, 引用于本文) 的 multi-instance processing 研究同样隔离了 count 和 context length 两个因素——虽然 target variable 不同（context length vs confusability），但实验设计逻辑相同。PARSE (Shrimal et al., 2025) 也研究 schema complexity 对抽取性能的影响并进行了 controlled comparison（虽然不是用 BCS）。
- 建议：改为 "To our knowledge, this is the first study to *explicitly isolate* type confusability from type count using *embedding-based batch-level controls* in training-free LLM IE"——更精确地限定 novelty scope。

---

## 小问题（不影响接收）

- **M1**: 8 个 orphan bib entries（在 .bib 中但未在正文引用）：dee-2024, gillick-2014-entity-typing, novack-2023-chils, schall-2025-hidden-cost, tam-2024-let-me-speak, volkanovska2025ner, wei-2023-chatie, zhou-2025-rethinking。应清理。
- **M2**: Table 1 caption 中 "†Trigger mentions across 8,042 sentences" 的 dagger 符号含义不够清晰。
- **M3**: Figure 1 的 (b) panel y 轴标签 "Accuracy" 对于 RE 来说应该更具体（是 F1? 还是 exact match accuracy?），需与 §3.4 的 metric 定义对齐。
- **M4**: §3.2 定义 SCS 时使用 `embed()` 函数但未在正文指定默认 embedding model（MiniLM 仅在后文 §3.2 尾部提及），建议在定义处即注明。
- **M5**: 可能遗漏的相关工作：ScrapeGraphAI-100k (2025, arXiv:2602.15189) 研究了 schema complexity 对 LLM extraction 的影响，虽然领域不同（web extraction），但研究问题有重叠。

---

## Questions to Authors

**Q1**: 在 BCS-controlled 实验中，高 BCS 和低 BCS batch 的 type distribution 是否完全一致？即除了 confusability 之外，是否可能存在其他 systematic differences（如高 BCS batch 倾向包含特定 semantic domain 的 types）？Appendix O (BCS Independence from Type Composition) 部分回答了这个问题，但仅展示 variance decomposition 而非直接的 type overlap 分析。

**Q2**: SDGD 的 routing failure rate (Table 8) 在 oracle routing 条件下显著降低——这是否意味着 SDGD 的核心瓶颈是 routing quality 而非 decomposition strategy 本身？如果使用更强的 routing model（如 GPT-4 级别），是否可能翻转结论？

**Q3**: Few-NERD 的 66 fine-grained types 组织为 8 coarse categories——BCS 计算是否考虑了这个层级结构？如果两个 type 属于同一 coarse category（如 "person-artist" 和 "person-athlete"），它们的高 confusability 是否比跨 category 的高 confusability 更影响性能？

---

## Missing References

- **ScrapeGraphAI-100k** (Cataldo et al., 2025, arXiv:2602.15189): 研究 schema complexity 对 LLM extraction reliability 的影响，与本文研究问题直接相关。
- **The Ecological Fallacy in Annotation** (Baan et al., 2023, ACL 2023): 论文引用了 Robinson (1950) 的 ecological correlation 概念，但未引用 NLP 领域中直接讨论 ecological fallacy 的近期工作。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 实验设计严谨（controlled design, TOST, bootstrap），但 NER null result 的解释不充分，且 BCS-controlled batching 作为方法论贡献的新颖性定位有争议 |
| **Excitement** | 3/5 | 研究问题重要且 timely，findings 有实践价值（SCS 作为诊断工具），但核心方法论贡献（分层实验设计）缺乏足够新颖性，发现本身（count 和 confusability 影响性能）在直觉上不令人意外 |
| **Reproducibility** | 4/5 | 详细的实验配置（seeds, hardware, prompt templates 完整列出），代码和数据承诺开源，但部分关键实现细节（如 BCS batch construction 的具体算法）分散在附录中 |
| **Confidence** | 4/5 | 熟悉 LLM IE 和实验设计方法论，仔细阅读了正文和全部附录 |

---

## 总体评分

**Overall**: **3.5** (Borderline Conference)

**一句话总结**: 实验设计严谨、分析深入的实证研究，但核心方法论贡献（BCS-controlled batch design）本质上是标准分层实验设计的领域应用，新颖性不足以支撑 methodology contribution 的定位；NER null result 作为关键发现缺乏充分的机制解释。

**接收建议**: 如果作者能 (1) 将贡献重心从 methodology 转向 empirical findings，(2) 深化 NER null result 的解释（或承认其为 open question），(3) 适当压缩 Limitations/SDGD 以扩展 Discussion——本文有潜力达到 Conference 水平。当前版本更接近 strong Findings 或 borderline Conference。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2788 · 2026-05-21T21:15:01.158053+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "schema-dag-extraction",
  "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "schema-dag-extraction",
    "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
  }
}
```

</details>

---


### Tool result

_source line 2789 · 2026-05-21T21:15:05.389580+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 4231
}
```

</details>

---


### Assistant

_source line 2790 · 2026-05-21T21:15:09.413647+00:00_

视觉审查 Agent 已启动（fire-and-forget）。Reviewer 2 报告已到，等待 Reviewer 1。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 228

## Round 228

2 recorded events


### User

_source line 2791 · 2026-05-21T21:15:12.059085+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**审稿完成摘要**：

- **Overall: 3.5** (Borderline Conference)
- **Soundness: 3.5/5** — 实验设计严谨但 NER null result 解释不足
- **Excitement: 3/5** — 问题重要，但 BCS-controlled batching 的方法论新颖性有限

**两个 Must-Fix 问题**：
1. BCS-controlled batch design 本质上是标准分层实验设计，作为 "methodology contribution" 定位不够 convincing——建议将贡献重心转向 empirical findings
2. NER 对 BCS 无响应的机制解释不充分，无法区分"零效应"与"被噪声掩盖的效应"

**四个 Should-Fix 问题**：Limitations 过长、跨模型验证未整合入正文、Abstract 数字过密、Discussion 过度压缩

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2792 · 2026-05-21T21:15:19.191741+00:00_

Reviewer 2 报告已记录。等待 Reviewer 1 完成初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 229

## Round 229

6 recorded events


### User

_source line 2793 · 2026-05-21T21:15:23.674216+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告：方法严谨性 + 实验设计

**论文**: "How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?"
**Venue**: EMNLP 2026 (ACL Rolling Review, May 2026 cycle)

---

## Summary

本文是一篇实证分析论文，研究 training-free LLM 信息抽取中 schema 复杂度的两个维度——type count 和 type confusability——如何独立驱动性能下降。作者提出 Schema Confusability Score (SCS) 和 Batch Confusability Score (BCS) 基于 embedding 余弦相似度量化 confusability，在 4 个数据集（Few-NERD, FewRel, DocRED, MAVEN）上通过 count curve 和 BCS-controlled 实验验证。主要发现：(1) count 驱动 recall 下降，confusability 驱动 type substitution；(2) BCS 在 FewRel 上解释 ~22% batch-level RE accuracy variance；(3) NER batch-level 无显著 BCS 信号；(4) Schema decomposition 因 merge amplification 和 routing failure 而失败。

---

## 总体评分

**Overall Assessment**: 3.5 / 5 (Borderline Conference)
**一句话总结**: 研究问题重要、实验设计严谨、统计方法娴熟，但 confusability 发现的可推广性受限于 FewRel RE 单一任务，effect size 偏小，且部分关键分析（DocRED R², error taxonomy, TOST, SDGD）为 single-model，削弱了结论的普遍性。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5 / 5 | 核心 FewRel BCS-controlled 实验设计合理（within-pool 控制、factorial analysis、TOST），但 DocRED VIF=50.9 严重削弱 R²=58% 的可信度；ecological amplification 叙事需更严格论证；多项关键二级分析仅限单模型 |
| Excitement | 3 / 5 | 研究问题实用（SCS 作为 pre-hoc proxy），两维度分解框架清晰。但 pairwise r²~1.3%、IQR-predicted gap 仅 2.2pp，实际意义有限；count 退化（更 robust 的发现）新颖性较低；confusability 仅在 FewRel RE 上稳健成立 |
| Reproducibility | 3 / 5 | 方法论细节充分（18 个 appendix），但代码数据 "released upon acceptance"；single seed + greedy decoding + FP8 quantization 的 variance 仅在 Appendix R 简要分析 |
| Confidence | 4 / 5 | 仔细审阅了全部统计方法论、实验设计和 18 个附录；熟悉 LLM IE、schema 复杂度、统计分析方法的相关文献 |

---

## 主要优势

**S1. 研究问题明确且实用。** 将 schema 复杂度分解为 count 和 confusability 两个独立维度是一个干净、有说服力的框架。SCS 作为无需运行抽取即可计算的 pre-hoc proxy（§3.2），对 practitioners 有直接部署价值。

**S2. FewRel BCS-controlled 实验设计严谨。** Within-pool 80-relation 比较（§4.3）有效控制了 type frequency 混淆；2×2 factorial analysis（Appendix C）正式检验了 interaction 的 boundedness；TOST 等价检验引入了 NLP 领域罕见的统计严谨性。

**S3. 统计方法远超同领域平均水平。** Bootstrap CIs、permutation tests、partial correlation controlling for degree centrality/type frequency（Appendix E, Table 11）、TOST 等价检验（Appendix C）、power analysis for NER null（§E.2）——这种统计意识在 NLP 投稿中非常突出。

**S4. Null results 的诚实报告。** NER batch-level BCS null 在 3 个模型上确认（Table 5），并明确标注可能是 insufficient power 而非 genuine absence（§E.2: minimum detectable effect = 5.5pp at 80% power for n=25）。这种透明度值得肯定。

**S5. 极为丰富的补充材料。** 18 个附录（Appendix A–Y）系统性地回应了可预见的审稿问题：cross-model validation（T, U）、prompt sensitivity（H）、confound analysis（E, Q）、ecological simulation（N）、format independence（K）、relaxed matching（Y）。

**S6. Cross-model validation 覆盖了核心发现。** Count curves 和 BCS-controlled 在 Qwen3-32B + LLaMA-3.1-8B/70B + Gemini 2.5 Flash 上验证（Appendix T, U, Table 24），direction 一致。

---

## Must-Fix 问题（影响接收决定）

**W1** [critical] **DocRED VIF=50.9 严重削弱 R²=58% 的可解释性**
- 具体位置：Table 11（p.16）、§4.3 footnote
- 问题：DocRED BCS-centrality collinearity VIF=50.9（Table 11 右列），远超公认阈值 10。在如此严重的多重共线性下，BCS 和 degree centrality 的个体回归系数估计极不稳定。论文声称 "the partial correlation remains highly significant"（p.16），但 partial r = −0.344 对应的解释力远低于 R²=58%。读者无法区分 DocRED 上 BCS 的独立贡献和 centrality 的混淆效应。
- 为什么影响接收：DocRED R²=58% 是论文中最大的 effect size，也是 document-level RE 推广到更复杂任务的关键证据。如果这个数字主要由 VIF=50.9 的多重共线性膨胀，则 confusability 对 document-level RE 的独立预测力大幅缩水，论文的核心 claim 之一失去支撑。
- 建议：(a) 报告 DocRED 的 semipartial R²（BCS 独立于 centrality 的增量解释力），而非 full model R²；(b) 或使用 ridge/LASSO 回归估计稳健系数；(c) 至少在正文中明确标注 VIF=50.9 的局限，而非仅在 appendix table 一个数字中带过。

**W2** [critical] **Confusability 发现仅在 FewRel RE 上稳健成立，普遍性不足以支撑论文的 general claims**
- 具体位置：Title, Abstract ("across NER, RE, and event detection"), §1 贡献列表, §5 Discussion
- 问题：逐一检查各任务/数据集的 confusability 证据：
  - **FewRel RE**: ✓ 批次级 R²≈22%，factorial TOST 确认独立性，跨模型一致（Table 24）
  - **NER (Few-NERD)**: ✗ 批次级 BCS null，3 模型均未检测到（Table 5）。§E.2 power analysis 给出 minimum detectable effect=5.5pp，但这恰好与 FewRel 的 IQR-predicted gap 2.2pp 在同一量级——说明即使 NER 存在 BCS 效应，其大小也很可能小于可检测阈值
  - **DocRED**: △ VIF=50.9 使 BCS 的独立贡献不可识别（W1）
  - **MAVEN**: △ Appendix E 显示 per-type BCS-F1 correlation 主要由 type frequency confound 驱动（MiniLM embedding 下）；只有 Qwen3 embedding 在控制 frequency 后保留 BCS 关联
  - **Gemini Flash**: △ Leave-one-out sensitivity 从 r=−0.80 降至 r=−0.42, p=0.22（Appendix U, Table 23），依赖单一杠杆点
- 为什么影响接收：论文标题 "How Does Schema Complexity Predict Performance" 和 abstract 中 "across NER, RE, and event detection" 暗示了跨任务的普遍性。但 confusability（论文最核心的新颖贡献）实际上只在一个数据集的一个任务上稳健成立。Count 退化虽然跨任务 robust，但新颖性较低（Chen et al., 2026; Li et al., 2023 已有类似观察）。
- 建议：(a) 弱化 title/abstract/conclusion 中的 generality claims，明确表述 confusability 的证据主要来自 FewRel RE；(b) 在 Discussion 中用一段专门讨论 task asymmetry 的根本原因（而非仅在 Limitations item 3 简要提及）；(c) 考虑添加一个 NER 数据集的更高 power 实验（如增大每层 batch 数量至 50+）。

**W3** [critical] **Ecological amplification 叙事的因果推断基础薄弱**
- 具体位置：§4.3（"BCS explains ~22% of cross-batch RE accuracy variance"）、Appendix N
- 问题：从 pairwise r²≈1.3% 到 batch R²≈22% 是 ~17× amplification。论文将此框架为 "ecological amplification"（引用 Robinson 1950），并在 Appendix N 提供了 Monte Carlo simulation。但该 simulation 有循环论证风险：
  - Simulation 假设 pair-level SCS correlation ρ=0.35（从共享 common type 的 pair 估计），而非观测的 pairwise r≈0.112–0.167
  - Simulation 产出的 batch R²=0.218 恰好匹配观测值——但这只证明了 "如果假设 ρ=0.35，则可以重现 0.218"，并未排除其他 batch-level confounds（如 domain coherence、entity density、batch 内 type 的 knowledge asymmetry）导致了相同的 pattern
  - Appendix N 最后一段承认 "the simulation is illustrative; the observed batch R²=0.218 is the primary evidence"——但如果 batch R² 是 primary evidence，那么 ecological fallacy 的风险正好适用于它
- 为什么影响接收：22% 是论文最有冲击力的数字之一，也是 practitioners 最可能引用的指标。如果它主要反映 aggregation artifact 而非 confusability 的真实预测力，则论文的实践价值被高估。
- 建议：(a) 报告 batch-level 回归中加入 batch-mean type frequency、batch domain diversity 等额外控制变量后的 R² 变化；(b) 如果 R² 在加入这些控制后大幅下降，应修正叙述；(c) 在正文中明确区分 "ecological description"（batch-level association）和 "predictive utility"（individual pair-level），避免读者将 22% 误解为 pair-level 效应。

---

## Should-Fix 问题（影响评分但不一票否决）

**W4** [warning] **Error taxonomy、TOST、SDGD 均为 single-model（Qwen3-32B），削弱多个重要二级发现**
- 具体位置：Figure 2（error taxonomy，§4.2）、Appendix C（TOST factorial）、§5/Appendix B（SDGD）
- 问题：这三项分析支撑了论文的三个重要 claim：(a) confusability 驱动 type substitution 而非 omission（Figure 2）；(b) count × confusability interaction 是 bounded 的（TOST）；(c) decomposition 因 merge amplification 失败（SDGD）。但它们均仅在 Qwen3-32B 上验证。给定 Gemini Flash 的 leave-one-out fragility（W2 中讨论），单模型结论的可迁移性存疑。
- 建议：至少在一个 alternative model（如 LLaMA-3.1-70B）上复现 error taxonomy 和 TOST 核心结果。如果资源不允许，在 Limitations 中明确标注这些是 single-model 发现。

**W5** [warning] **TOST ±3pp margin 在高准确率区间偏宽松**
- 具体位置：Appendix C, Table 9（p.15）
- 问题：FewRel 准确率 ~80%，±3pp equivalence margin 对应相对误差 ~15%（3pp / (1−0.80)）。论文在 probability scale 上 TOST 通过（interaction 0.47pp ≪ 3pp），但在 logit scale 上 TOST inconclusive at ±1pp（Table 9）。论文保留 probability-scale TOST 作为 primary test，但未充分论证为什么 probability scale 比 logit scale 更合适。在高准确率区间，logit scale 对效应大小的解读通常更有信息量（因为 probability 压缩了接近 ceiling 的差异）。Back-transformed interaction 在 median baseline 处为 2.78pp——接近 ±3pp boundary。
- 建议：(a) 在正文中承认 logit-scale 的不一致性（目前仅在 appendix 报告）；(b) 讨论为什么 probability scale 是合理的 primary metric（例如：practitioners 关心的是 absolute accuracy change）；(c) 考虑报告 ±2pp 的 TOST 结果作为 sensitivity analysis。

**W6** [warning] **FewRel train+val 合并的 pretraining contamination 风险**
- 具体位置：§3.1（"We combine the training and validation splits"）
- 问题：FewRel 是一个广泛使用的 few-shot 基准，其 train split 很可能出现在 Qwen3-32B 的 pretraining corpus 中。Appendix Q 显示 train-origin types 准确率低 ~8.5pp（p=0.06, borderline significant），BCS partial effect 在控制 split origin 后不变（ΔR²=0.00）。但 borderline p=0.06 意味着 contamination 效应的方向与预期相反（train types 更低而非更高），这本身也令人困惑——可能反映 train split 包含更难的 relation types，而非 contamination。
- 建议：在正文的 experimental setup 或 Limitations 中简要讨论此问题，引用 Appendix Q 的控制分析。

**W7** [warning] **Pairwise r²≈1.3% 与 "confusability predicts degradation" 的 claim 之间存在张力**
- 具体位置：Abstract（"BCS explains ~22%"）、§4.2（Table 2, r=0.167）
- 问题：Abstract 突出了 22% ecological-level variance，但 pair-level r² 仅 1.3–2.8%。IQR-predicted gap 仅 2.2pp（§4.3 footnote）。论文的叙事主要建立在 batch-level 上（ecological），但 pair-level 效应才是避免 ecological fallacy 的 ground truth。2.2pp 的实际意义取决于部署场景：对于 80 relations 的 full-schema RE，这可能可以忽略；但论文未讨论在什么 use case 下 2.2pp 是 actionable 的。
- 建议：(a) 在 Abstract/Conclusion 中同时报告 pair-level 和 batch-level effect size，避免单独强调 22%；(b) 加一段讨论 "practical significance"——在什么场景下 SCS 预测的 2.2pp gap 足以指导 schema 设计决策。

---

## 小问题（不影响接收）

**M1.** 8 个 orphan bib entries（在 .bib 中但未在正文引用）：dee-2024, gillick-2014-entity-typing, novack-2023-chils, schall-2025-hidden-cost, tam-2024-let-me-speak, volkanovska2025ner, wei-2023-chatie, zhou-2025-rethinking。投稿前应清理。

**M2.** Appendix M（Table 19, SCS name-only vs name+definition）的结论对 MAVEN 的解读（"name-only SCS conflates confusability with centrality"）应在正文 §3.2 而非仅在 appendix 中提及，因为它直接影响 SCS 作为 proxy 的局限性。

**M3.** §3.2: "Centrality (§4.5) consistently yields equal or stronger correlations"——但 §4.5 的 centrality 分析实际只在 MAVEN 上成立，在 FewRel/Few-NERD 上 centrality 是 non-significant 的。应更精确表述。

**M4.** Figure 1 caption 提到 "Error bars: ±1 SD across 3 batch-composition seeds × 25 batches"，但正文 §3.3 说 "we sample 25 random type batches for Few-NERD and FewRel (5 for DocRED and MAVEN)"——SD 的 sample size 对解读 error bar 重要，应在 caption 中明确。

**M5.** 引用格式方面：4 篇引用（gemini-2025, dror-2018-significance, sclar-sensitivity-2024, li2023evaluating）未被 OpenAlex 验证到，疑似索引延迟或 title 轻微不匹配，但经核查均为真实存在的论文，无 fabrication 问题。

---

## Questions for Authors

**Q1.** DocRED 的 full-model R²=58% 中，BCS 的 semipartial R²（unique variance explained by BCS after partialing out degree centrality）是多少？如果远低于 58%，应如何修正 §4.3 中的叙述？

**Q2.** 论文在 FewRel BCS-controlled 实验中使用了 within-pool 16-relation subsets，greedy 选择 high/low BCS batches。这些 extreme batches 在 domain distribution 上是否有系统偏差？例如，high-BCS batches 是否倾向于来自同一 Wikidata domain？

**Q3.** NER batch-level null 在 Gemini Flash 上是否测试过？如果 Gemini 也是 null，则 NER null 的跨模型 robustness 更强；如果 Gemini 有信号，则可能揭示 model capacity 的影响。

**Q4.** 论文提到 FP8 quantization 引入 non-determinism（§3.5 footnote）。greedy decoding + FP8 的 batch-to-batch variance 是多少？Appendix R 的 Cross-Seed Variance Decomposition 显示 "batch variance dominates inter-seed variance by 5–474×"（Table 21），但仅报告了 3 seeds × 25 batches。能否提供单 seed 的 bootstrap SE 以量化 FP8 noise 的上界？

**Q5.** Ecological simulation（Appendix N）中使用的 ρ=0.35 是从 "pairs sharing a common type" 估计的。这个条件子集的 ρ 是否能代表 random batch 内的平均 pair-level correlation？如果 random batches 的 within-batch ρ 远低于 0.35，simulation 产出的 batch R² 也会远低于 0.218。

---

## Missing References

1. **Ding et al. (2024)** "GraphER: A Structure-aware Text-to-Graph Model for Entity and Relation Extraction" — 与 schema-guided extraction 直接相关，讨论了 schema 结构对 extraction 的影响
2. **Xu et al. (2024)** "How to Handle Different Types of Out-of-Distribution Scenarios in Computational Argumentation? A Comprehensive and Fine-Grained Field Study" — 研究了 label space 扩展对 OOD 性能的影响，与 type count 退化相关
3. **Cohen (1988)** "Statistical Power Analysis for the Behavioral Sciences" — 论文使用了 power analysis 但未引用此经典参考

---

## Overall Assessment

**3.5 / 5 (Borderline Conference)**

本文做了一项有价值的实证研究，研究问题重要且实用。统计方法论的严谨性（TOST、partial correlation、power analysis、bootstrap CIs）远超同领域平均水平，18 个 appendix 的覆盖面令人印象深刻。SCS 作为 pre-hoc complexity proxy 有直接的工程应用价值。

然而，三个 must-fix 问题限制了当前版本的接收：(1) DocRED VIF=50.9 严重削弱了最大 effect size 的可信度；(2) confusability 的核心新颖贡献实际仅在 FewRel RE 上稳健成立，NER null + DocRED confounded + MAVEN frequency-driven 使跨任务推广证据不足；(3) ecological amplification 叙事（1.3% → 22%）的因果推断基础需要更严格的 confound 控制。

如果作者能 (a) 诚实报告 DocRED semipartial R²，(b) 弱化 generality claims 并在 title/abstract 中准确反映 evidence scope，(c) 在 ecological 回归中加入 batch-level confound 控制，本文有潜力达到 Conference 接收水平。当前版本更适合 Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2794 · 2026-05-21T21:16:24.337078+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Weakness 和 Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿报告：新颖性 + 完整性 + 写作质量\n\n## Must-Fix 问题\n\n**W1** [critical] **方法论新颖性不足：BCS-controlled batch design 本质上是标准的分层实验设计**\n- 论文将 \"BCS-controlled batch design methodology\" 定位为核心贡献（§1: \"the contribution is the methodology, not the metric\"），但 BCS-controlled batching 本质上是经典的 confound control / stratified experimental design——在统计学和实验心理学中已有数十年历史。具体做法（按 BCS 分层采样 batch，在每个 count level 固定 BCS 高/低组进行比较）就是标准的 blocking design。论文未引用任何实验设计方法论文献（如 Fisher 的 experimental design 原理），也未解释为什么将这一标准技术应用于 LLM IE 领域本身构成方法论贡献。\n- 建议：(a) 重新定位贡献重心——将核心贡献从 \"methodology\" 转向 \"empirical findings enabled by controlled design\"；(b) 如坚持 methodology 定位，需要解释 BCS-controlled batching 相对于标准 blocking design 有何领域特定的创新。\n\n**W2** [critical] **NER null result 的机制解释不充分**\n- NER 在所有分析中对 BCS 无显著响应——这是论文最令人意外的发现之一，但机制解释停留在描述层面。§4.4 将错误分解为 IntraSub 和 missed rates，发现 NER missed rates \"substantially higher (43-65%)\" 且 \"non-monotonic\"，但仅归因于 \"type modes rather than concentrating in type substitution\"。Appendix E.2 的 NER BCS-null power analysis 表明 r ≈ −0.11 \"under this restricted range\"，但不清楚是统计功效不足（样本量问题）还是真正的零效应。论文同时提出两个矛盾的可能解释。\n- 建议：(a) 设计针对性实验区分两个假设——例如在 NER 中仅分析 type substitution errors（排除 boundary errors）后 BCS 是否显著；(b) 至少在正文中明确表述：\"基于现有证据，我们无法区分零效应与被噪声掩盖的效应\"。\n\n## Should-Fix 问题\n\n**W3** [warning] **Limitations 章节过长，不符合 EMNLP 写作惯例** — 6 个编号点 + 2 段额外讨论，占据近整页。EMNLP 2026 要求 Limitations 不应包含过多额外内容。建议压缩至 3-4 个核心点。\n\n**W4** [warning] **跨模型验证结果未充分整合入正文** — 主实验全部基于 Qwen3-32B 单一模型。跨模型验证（LLaMA-3.1-8B, LLaMA-70B, Gemini 2.5 Flash）仅出现在附录。建议在 §4 或 §6 用 1-2 段总结。\n\n**W5** [warning] **Abstract 信息密度过高，关键 takeaway 被数字淹没** — Abstract 在约 150 词中塞入大量具体数字，非专业读者难以提取核心 takeaway。\n\n**W6** [warning] **Discussion/Conclusion 过度压缩** — Discussion 和 Conclusion 合并在 Page 8 的下半页（约 25 行），practical implications 每个仅一句话带过。\n\n**W7** [warning] **\"First controlled study\" claim 需要更谨慎的措辞** — Chen et al. (2026) 的 multi-instance processing 研究同样隔离了 count 和 context length 两个因素——虽然 target variable 不同，但实验设计逻辑相同。PARSE (Shrimal et al., 2025) 也研究 schema complexity。建议改为更精确限定 novelty scope。\n\n## Questions\n\n**Q1**: BCS-controlled 实验中，高 BCS 和低 BCS batch 的 type distribution 是否完全一致？除 confusability 外是否存在 systematic differences（如高 BCS batch 倾向包含特定 semantic domain 的 types）？\n\n**Q2**: SDGD 的 routing failure 在 oracle routing 条件下显著降低——是否意味着核心瓶颈是 routing quality 而非 decomposition strategy 本身？如果使用更强的 routing model 是否可能翻转结论？\n\n**Q3**: Few-NERD 的 66 fine-grained types 组织为 8 coarse categories——BCS 计算是否考虑了层级结构？同 coarse category 内的高 confusability 是否比跨 category 的更影响性能？\n\n## Missing References\n\n- ScrapeGraphAI-100k (Cataldo et al., 2025): 研究 schema complexity 对 LLM extraction reliability 的影响\n- The Ecological Fallacy in Annotation (Baan et al., 2023, ACL 2023): NLP 领域中直接讨论 ecological fallacy 的近期工作\n\n---\n\n请对每个 W 和 Q 逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Weakness 和 Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿报告：新颖性 + 完整性 + 写作质量\n\n## Must-Fix 问题\n\n**W1** [critical] **方法论新颖性不足：BCS-controlled batch design 本质上是标准的分层实验设计**\n- 论文将 \"BCS-controlled batch design methodology\" 定位为核心贡献（§1: \"the contribution is the methodology, not the metric\"），但 BCS-controlled batching 本质上是经典的 confound control / stratified experimental design——在统计学和实验心理学中已有数十年历史。具体做法（按 BCS 分层采样 batch，在每个 count level 固定 BCS 高/低组进行比较）就是标准的 blocking design。论文未引用任何实验设计方法论文献（如 Fisher 的 experimental design 原理），也未解释为什么将这一标准技术应用于 LLM IE 领域本身构成方法论贡献。\n- 建议：(a) 重新定位贡献重心——将核心贡献从 \"methodology\" 转向 \"empirical findings enabled by controlled design\"；(b) 如坚持 methodology 定位，需要解释 BCS-controlled batching 相对于标准 blocking design 有何领域特定的创新。\n\n**W2** [critical] **NER null result 的机制解释不充分**\n- NER 在所有分析中对 BCS 无显著响应——这是论文最令人意外的发现之一，但机制解释停留在描述层面。§4.4 将错误分解为 IntraSub 和 missed rates，发现 NER missed rates \"substantially higher (43-65%)\" 且 \"non-monotonic\"，但仅归因于 \"type modes rather than concentrating in type substitution\"。Appendix E.2 的 NER BCS-null power analysis 表明 r ≈ −0.11 \"under this restricted range\"，但不清楚是统计功效不足（样本量问题）还是真正的零效应。论文同时提出两个矛盾的可能解释。\n- 建议：(a) 设计针对性实验区分两个假设——例如在 NER 中仅分析 type substitution errors（排除 boundary errors）后 BCS 是否显著；(b) 至少在正文中明确表述：\"基于现有证据，我们无法区分零效应与被噪声掩盖的效应\"。\n\n## Should-Fix 问题\n\n**W3** [warning] **Limitations 章节过长，不符合 EMNLP 写作惯例** — 6 个编号点 + 2 段额外讨论，占据近整页。EMNLP 2026 要求 Limitations 不应包含过多额外内容。建议压缩至 3-4 个核心点。\n\n**W4** [warning] **跨模型验证结果未充分整合入正文** — 主实验全部基于 Qwen3-32B 单一模型。跨模型验证（LLaMA-3.1-8B, LLaMA-70B, Gemini 2.5 Flash）仅出现在附录。建议在 §4 或 §6 用 1-2 段总结。\n\n**W5** [warning] **Abstract 信息密度过高，关键 takeaway 被数字淹没** — Abstract 在约 150 词中塞入大量具体数字，非专业读者难以提取核心 takeaway。\n\n**W6** [warning] **Discussion/Conclusion 过度压缩** — Discussion 和 Conclusion 合并在 Page 8 的下半页（约 25 行），practical implications 每个仅一句话带过。\n\n**W7** [warning] **\"First controlled study\" claim 需要更谨慎的措辞** — Chen et al. (2026) 的 multi-instance processing 研究同样隔离了 count 和 context length 两个因素——虽然 target variable 不同，但实验设计逻辑相同。PARSE (Shrimal et al., 2025) 也研究 schema complexity。建议改为更精确限定 novelty scope。\n\n## Questions\n\n**Q1**: BCS-controlled 实验中，高 BCS 和低 BCS batch 的 type distribution 是否完全一致？除 confusability 外是否存在 systematic differences（如高 BCS batch 倾向包含特定 semantic domain 的 types）？\n\n**Q2**: SDGD 的 routing failure 在 oracle routing 条件下显著降低——是否意味着核心瓶颈是 routing quality 而非 decomposition strategy 本身？如果使用更强的 routing model 是否可能翻转结论？\n\n**Q3**: Few-NERD 的 66 fine-grained types 组织为 8 coarse categories——BCS 计算是否考虑了层级结构？同 coarse category 内的高 confusability 是否比跨 category 的更影响性能？\n\n## Missing References\n\n- ScrapeGraphAI-100k (Cataldo et al., 2025): 研究 schema complexity 对 LLM extraction reliability 的影响\n- The Ecological Fallacy in Annotation (Baan et al., 2023, ACL 2023): NLP 领域中直接讨论 ecological fallacy 的近期工作\n\n---\n\n请对每个 W 和 Q 逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 2795 · 2026-05-21T21:16:48.367792+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 24030
}
```

</details>

---


### Tool call

_source line 2796 · 2026-05-21T21:16:51.230091+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Weakness 和 Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿报告：方法严谨性 + 实验设计\n\n## Must-Fix 问题\n\n**W1** [critical] **DocRED VIF=50.9 严重削弱 R²=58% 的可解释性**\n- DocRED BCS-centrality collinearity VIF=50.9（Table 11），远超公认阈值 10。BCS 和 degree centrality 的个体回归系数估计极不稳定。论文声称 \"the partial correlation remains highly significant\"，但 partial r = −0.344 对应的解释力远低于 R²=58%。读者无法区分 DocRED 上 BCS 的独立贡献和 centrality 的混淆效应。\n- 建议：报告 DocRED semipartial R²（BCS unique variance），或使用 ridge/LASSO 回归估计稳健系数。\n\n**W2** [critical] **Confusability 发现仅在 FewRel RE 上稳健成立，普遍性不足以支撑论文的 general claims**\n- 逐一检查各任务/数据集：\n  - FewRel RE: ✓ 批次级 R²≈22%，跨模型一致\n  - NER (Few-NERD): ✗ 批次级 BCS null，3 模型均未检测到\n  - DocRED: △ VIF=50.9 使 BCS 独立贡献不可识别\n  - MAVEN: △ per-type BCS-F1 正相关主要由 frequency confound 驱动\n  - Gemini Flash: △ leave-one-out r: −0.80→−0.42, p=0.22\n- 论文 title/abstract 暗示跨任务普遍性，但 confusability 实际只在 FewRel RE 上稳健。Count 退化虽 robust 但新颖性较低。\n- 建议：弱化 generality claims，明确 confusability 证据主要来自 FewRel RE。\n\n**W3** [critical] **Ecological amplification 叙事的因果推断基础薄弱**\n- 从 pairwise r²≈1.3% 到 batch R²≈22% 是 ~17× amplification。Appendix N 的 Monte Carlo simulation 假设 pair-level ρ=0.35（条件子集），而非观测的 pairwise r≈0.112–0.167。Simulation 产出 batch R²=0.218 恰好匹配观测值——但这只证明了\"如果假设 ρ=0.35 则可重现 0.218\"，未排除其他 batch-level confounds。\n- 建议：batch-level 回归中加入 batch-mean type frequency、batch domain diversity 等额外控制变量后报告 R² 变化。\n\n## Should-Fix 问题\n\n**W4** [warning] **Error taxonomy、TOST、SDGD 均为 single-model（Qwen3-32B），削弱多个重要二级发现**\n- 这三项分析支撑了三个重要 claim：(a) confusability 驱动 type substitution 而非 omission；(b) count × confusability interaction bounded；(c) decomposition 因 merge amplification 失败。但均仅在 Qwen3-32B 上验证。\n- 建议：至少在一个 alternative model 上复现核心结果，或在 Limitations 中明确标注。\n\n**W5** [warning] **TOST ±3pp margin 在高准确率区间偏宽松**\n- FewRel 准确率 ~80%，±3pp equivalence margin 对应相对误差 ~15%。probability scale TOST 通过但 logit scale inconclusive at ±1pp。Back-transformed interaction 在 median baseline 处为 2.78pp——接近 ±3pp boundary。\n- 建议：在正文承认 logit-scale 不一致性，讨论 probability scale 作为 primary metric 的理由。\n\n**W6** [warning] **FewRel train+val 合并的 pretraining contamination 风险**\n- FewRel train split 可能出现在 Qwen3-32B pretraining corpus。Appendix Q 显示 train-origin types 准确率低 ~8.5pp（p=0.06），方向与预期相反。BCS partial effect 控制 split origin 后不变。\n- 建议：在正文 experimental setup 或 Limitations 简要讨论。\n\n**W7** [warning] **Pairwise r²≈1.3% 与 \"confusability predicts degradation\" 的 claim 之间存在张力**\n- IQR-predicted gap 仅 2.2pp。论文未讨论在什么 use case 下 2.2pp 是 actionable 的。\n- 建议：Abstract/Conclusion 同时报告 pair-level 和 batch-level effect size；讨论 practical significance。\n\n## Questions\n\n**Q1.** DocRED full-model R²=58% 中，BCS 的 semipartial R²（unique variance explained by BCS after partialing out degree centrality）是多少？\n\n**Q2.** FewRel BCS-controlled 实验中 extreme batches 在 domain distribution 上是否有系统偏差？high-BCS batches 是否倾向来自同一 Wikidata domain？\n\n**Q3.** NER batch-level null 在 Gemini Flash 上是否测试过？\n\n**Q4.** Greedy decoding + FP8 的 batch-to-batch variance 是多少？能否提供单 seed bootstrap SE 量化 FP8 noise 上界？\n\n**Q5.** Ecological simulation（Appendix N）中 ρ=0.35 是否能代表 random batch 内平均 pair-level correlation？\n\n## Missing References\n\n1. Ding et al. (2024) \"GraphER\" — schema-guided extraction\n2. Xu et al. (2024) \"How to Handle Different Types of OOD Scenarios\" — label space expansion\n3. Cohen (1988) \"Statistical Power Analysis\" — power analysis 经典参考\n\n---\n\n请对每个 W 和 Q 逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Weakness 和 Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿报告：方法严谨性 + 实验设计\n\n## Must-Fix 问题\n\n**W1** [critical] **DocRED VIF=50.9 严重削弱 R²=58% 的可解释性**\n- DocRED BCS-centrality collinearity VIF=50.9（Table 11），远超公认阈值 10。BCS 和 degree centrality 的个体回归系数估计极不稳定。论文声称 \"the partial correlation remains highly significant\"，但 partial r = −0.344 对应的解释力远低于 R²=58%。读者无法区分 DocRED 上 BCS 的独立贡献和 centrality 的混淆效应。\n- 建议：报告 DocRED semipartial R²（BCS unique variance），或使用 ridge/LASSO 回归估计稳健系数。\n\n**W2** [critical] **Confusability 发现仅在 FewRel RE 上稳健成立，普遍性不足以支撑论文的 general claims**\n- 逐一检查各任务/数据集：\n  - FewRel RE: ✓ 批次级 R²≈22%，跨模型一致\n  - NER (Few-NERD): ✗ 批次级 BCS null，3 模型均未检测到\n  - DocRED: △ VIF=50.9 使 BCS 独立贡献不可识别\n  - MAVEN: △ per-type BCS-F1 正相关主要由 frequency confound 驱动\n  - Gemini Flash: △ leave-one-out r: −0.80→−0.42, p=0.22\n- 论文 title/abstract 暗示跨任务普遍性，但 confusability 实际只在 FewRel RE 上稳健。Count 退化虽 robust 但新颖性较低。\n- 建议：弱化 generality claims，明确 confusability 证据主要来自 FewRel RE。\n\n**W3** [critical] **Ecological amplification 叙事的因果推断基础薄弱**\n- 从 pairwise r²≈1.3% 到 batch R²≈22% 是 ~17× amplification。Appendix N 的 Monte Carlo simulation 假设 pair-level ρ=0.35（条件子集），而非观测的 pairwise r≈0.112–0.167。Simulation 产出 batch R²=0.218 恰好匹配观测值——但这只证明了\"如果假设 ρ=0.35 则可重现 0.218\"，未排除其他 batch-level confounds。\n- 建议：batch-level 回归中加入 batch-mean type frequency、batch domain diversity 等额外控制变量后报告 R² 变化。\n\n## Should-Fix 问题\n\n**W4** [warning] **Error taxonomy、TOST、SDGD 均为 single-model（Qwen3-32B），削弱多个重要二级发现**\n- 这三项分析支撑了三个重要 claim：(a) confusability 驱动 type substitution 而非 omission；(b) count × confusability interaction bounded；(c) decomposition 因 merge amplification 失败。但均仅在 Qwen3-32B 上验证。\n- 建议：至少在一个 alternative model 上复现核心结果，或在 Limitations 中明确标注。\n\n**W5** [warning] **TOST ±3pp margin 在高准确率区间偏宽松**\n- FewRel 准确率 ~80%，±3pp equivalence margin 对应相对误差 ~15%。probability scale TOST 通过但 logit scale inconclusive at ±1pp。Back-transformed interaction 在 median baseline 处为 2.78pp——接近 ±3pp boundary。\n- 建议：在正文承认 logit-scale 不一致性，讨论 probability scale 作为 primary metric 的理由。\n\n**W6** [warning] **FewRel train+val 合并的 pretraining contamination 风险**\n- FewRel train split 可能出现在 Qwen3-32B pretraining corpus。Appendix Q 显示 train-origin types 准确率低 ~8.5pp（p=0.06），方向与预期相反。BCS partial effect 控制 split origin 后不变。\n- 建议：在正文 experimental setup 或 Limitations 简要讨论。\n\n**W7** [warning] **Pairwise r²≈1.3% 与 \"confusability predicts degradation\" 的 claim 之间存在张力**\n- IQR-predicted gap 仅 2.2pp。论文未讨论在什么 use case 下 2.2pp 是 actionable 的。\n- 建议：Abstract/Conclusion 同时报告 pair-level 和 batch-level effect size；讨论 practical significance。\n\n## Questions\n\n**Q1.** DocRED full-model R²=58% 中，BCS 的 semipartial R²（unique variance explained by BCS after partialing out degree centrality）是多少？\n\n**Q2.** FewRel BCS-controlled 实验中 extreme batches 在 domain distribution 上是否有系统偏差？high-BCS batches 是否倾向来自同一 Wikidata domain？\n\n**Q3.** NER batch-level null 在 Gemini Flash 上是否测试过？\n\n**Q4.** Greedy decoding + FP8 的 batch-to-batch variance 是多少？能否提供单 seed bootstrap SE 量化 FP8 noise 上界？\n\n**Q5.** Ecological simulation（Appendix N）中 ρ=0.35 是否能代表 random batch 内平均 pair-level correlation？\n\n## Missing References\n\n1. Ding et al. (2024) \"GraphER\" — schema-guided extraction\n2. Xu et al. (2024) \"How to Handle Different Types of OOD Scenarios\" — label space expansion\n3. Cohen (1988) \"Statistical Power Analysis\" — power analysis 经典参考\n\n---\n\n请对每个 W 和 Q 逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 2797 · 2026-05-21T21:16:52.642051+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1411
}
```

</details>

---


### Assistant

_source line 2798 · 2026-05-21T21:16:56.497308+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 230

## Round 230

2 recorded events


### User

_source line 2799 · 2026-05-21T21:16:59.050824+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**审稿结论摘要**：

- **Overall**: 3.5/5（Borderline Conference）
- **Soundness**: 3.5/5 | **Excitement**: 3/5 | **Reproducibility**: 3/5

**三个 Must-Fix 问题**：
1. **DocRED VIF=50.9** 使 R²=58% 的可信度严重存疑——BCS 与 degree centrality 高度共线，无法分离独立贡献
2. **Confusability 发现仅在 FewRel RE 上稳健**——NER 为 null，DocRED 被 confound，MAVEN 被 frequency 驱动，Gemini 依赖单一杠杆点。Title/Abstract 的跨任务普遍性 claim 过度
3. **Ecological amplification 叙事**（pairwise 1.3% → batch 22%）缺乏充分的 confound 控制，simulation 使用的 ρ=0.35 是否代表 random batch 内的平均 correlation 未经验证

**四个 Should-Fix**：TOST ±3pp margin 偏宽松（W5）、error taxonomy/TOST/SDGD 均为 single-model（W4）、FewRel contamination 风险（W6）、pair-level effect size 2.2pp 的实际意义未讨论（W7）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2800 · 2026-05-21T21:17:06.127388+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 231

## Round 231

2 recorded events


### User

_source line 2801 · 2026-05-21T21:18:51.453009+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 的交叉回应

---

## Must-Fix

**[AGREE] R1-W1: DocRED VIF=50.9 削弱 R²=58% 的可解释性**

同意这是一个实质性统计问题。VIF=50.9 远超常规阈值 10，说明 BCS 和 degree centrality 在 DocRED 上高度共线。论文在 Table 11 中报告了 partial correlation r = −0.344（p < 0.001），但在 VIF 如此高的条件下，partial r 的置信区间会非常宽，系数估计不稳定。R1 建议报告 semipartial R²（BCS unique variance）是完全合理的——这是处理多重共线性时的标准做法。

**补充发现**：值得注意的是，论文的 confusability 核心证据主要依赖 FewRel（VIF=1.18, Table 11），而非 DocRED。DocRED 的 R²=58% 在论文中作为 supporting evidence 而非 primary evidence 出现。因此这个问题虽然真实，但对论文核心 claim 的威胁程度低于 R1 的措辞暗示的程度——前提是作者在修改中明确标注 DocRED 结果的这一 caveat。

---

**[AGREE with nuance] R1-W2: Confusability 发现普遍性不足**

这是本文最根本的问题之一，与我自己的 W1（方法论新颖性）和 W2（NER null result 解释不充分）直接相关。R1 的逐数据集 audit 是准确的：

- FewRel RE: ✓ 唯一稳健的 confusability 证据来源
- NER (Few-NERD): ✗ 所有模型均 null（我在 W2 中也指出了这一点）
- DocRED: △ VIF 问题（同意 R1-W1）
- MAVEN: △ 我在审稿中未单独标记此点，但 R1 正确指出 Appendix E 的 per-type BCS-F1 正相关被 frequency confound 驱动（Appendix E.1 承认 "the dominant confound differs by embedding"，且 MiniLM 的正相关主要来自 log frequency）

**部分反驳**：R1 将论文描述为 "title/abstract 暗示跨任务普遍性" 略有过度。论文 Abstract 明确限定了 confusability 发现的范围："In RE, BCS explains ~22% of cross-batch RE accuracy variance on FewRel"（强调 "In RE" 和 "on FewRel"），且 Contribution 2 专门标记了 task asymmetry。Title 用 "How Does Schema Complexity Predict Performance" 确实有 general framing，但 schema complexity 包括 count 和 confusability 两个维度——count degradation 确实是跨任务 robust 的（所有任务、所有模型一致）。

**净结论**：R1 的核心判断正确——confusability 的 actionable 证据集中于 FewRel RE。但论文并未完全忽视这一限制。建议作者在 Abstract 和 Conclusion 中进一步明确："confusability 作为独立预测因子的证据目前仅在 sentence-level RE 上稳健成立，跨任务推广需要未来工作验证。"

---

**[REBUT] R1-W3: Ecological amplification 叙事的因果推断基础薄弱**

R1 的批评核心是 Appendix N simulation 使用 ρ=0.35 而非观测的 pairwise r ≈ 0.112–0.167。但这一批评混淆了 marginal correlation 和 conditional correlation：

1. **ρ=0.35 的来源**：论文 Appendix N（Page 21）明确说明 ρ=0.35 来自 "pairs sharing a common type"（条件子集），不是全部 type pair 的 marginal correlation。全部 pair 的 r ≈ 0.112–0.167 包含大量零混淆对（zero-confusion pairs），这些对在 batch 内不产生 confusability 信号。用 conditional ρ 建模 batch 内的有效信号是合理的。

2. **Simulation 的定位**：论文明确声明 "The simulation is illustrative; the observed batch R² = 0.218 is the primary evidence"（Page 21）。Appendix N 不是核心证据，而是一个 explanatory model，帮助读者理解为什么 pair-level 弱信号能在 batch-level 放大。论文的核心因果证据来自 BCS-controlled 实验（§4.3），而非 simulation。

3. **额外控制变量**：R1 建议加入 "batch-mean type frequency、batch domain diversity" 作为 batch-level confounds。这个建议合理，但论文已在 Appendix E.1（controlling for degree centrality）和 Appendix O（BCS independence from type composition）中部分回应了这一关切。Appendix O 显示 BCS 捕获的是 confusability-specific signal 而非 type frequency 的 proxy（variance decomposition: BCS unique = 0.298, shared with frequency = 0.147）。

**净结论**：R1 对 simulation 参数选择的质疑有一定道理，但将其上升为 "因果推断基础薄弱" 过度了。论文的因果推断主要依赖 controlled experiment（§4.3），不依赖 simulation。建议作者在正文中明确 simulation 的 illustrative 定位，并在 Appendix N 中补充使用 marginal ρ 的 sensitivity analysis。

---

## Should-Fix

**[AGREE] R1-W4: Error taxonomy / TOST / SDGD 均为 single-model**

完全同意。这与我的 W4（跨模型验证未充分整合入正文）互补。特别是 SDGD 的 merge amplification failure（§5, Table 7-8）——如果这是 Qwen3-32B 特定的 instruction-following 问题（如 merge step 的 JSON format adherence），则结论不可推广。至少需要在一个 alternative model 上复现 SDGD 失败，或者在 Limitations 中明确标注 "SDGD 分析仅基于 Qwen3-32B"。

---

**[AGREE] R1-W5: TOST ±3pp margin 偏宽松**

同意这是一个值得讨论的 calibration 问题。论文在 Appendix C 中确实报告了 logit-scale 结果（"At ±1pp, equivalence is inconclusive (p = 0.275)"），但这一不一致性被 buried 在附录中。在 FewRel ~80% 准确率区间，±3pp 对应 ±3.75% 相对变化——对于 claim "interaction is bounded well below practical significance"（§4.3），这个 margin 的合理性需要在正文中讨论。

**补充**：更根本的问题是 TOST 的 margin 选择缺乏 domain-specific justification。论文引用了 Lakens (2017) 和 Schuirmann (1987) 的方法论，但 ±3pp 是 "the smallest effect size of interest" 的 author judgment——在 NLP 实证研究中尚无公认的 equivalence margin 标准。建议作者至少讨论 margin 选择的 sensitivity（已在附录有 ±1pp/±5pp 的 TOST，但正文应提及这一 robustness check）。

---

**[REBUT] R1-W6: FewRel train+val pretraining contamination风险**

R1 将此标为 should-fix，但论文已在 Appendix Q 中提供了有力的反驳证据：

1. **方向相反**：Appendix Q 显示 train-origin types 准确率 *低* ~8.5pp（p = 0.06），与 contamination 预期方向（应更高）相反。
2. **BCS 效应不受影响**：控制 split-origin 后，BCS partial effect "unchanged"（Appendix Q）。
3. **Spearman correlation robust**：控制 train_origin_ratio 后 BCS-accuracy correlation "remains significant"（Appendix Q, p = 0.001）。

R1 建议 "在正文简要讨论" 是合理的——但将此标为 should-fix 暗示论文存在未处理的问题，而实际上论文已处理得当。建议的修改仅是将 Appendix Q 的核心结论（1-2 句话）搬至正文 §3.1 或 Limitations。

---

**[AGREE] R1-W7: Pairwise r²≈1.3% 与 "confusability predicts degradation" 的张力**

同意这是一个 framing 问题。论文的核心叙事是 batch-level R²≈22%，但 pair-level r²≈1.3%（IQR gap 仅 2.2pp）在 practical significance 层面确实需要讨论。

不过要补充一个 nuance：pair-level 和 batch-level 是不同的 unit of analysis，对应不同的 practical scenario。Batch-level effect 对应 "为一组 types 设计 prompt schema" 的场景（这是 training-free LLM IE 的典型 use case），此时 22% variance explained 是 actionable 的。Pair-level effect 对应 "预测单个 type pair 的混淆率"，此时 1.3% 确实 marginal。建议作者在讨论中明确这两个 granularity 的 practical implications 差异。

---

## Questions

**[对 Q1 的回应]**：同意应报告 DocRED semipartial R²。这是解决 W1 的关键数据点。

**[对 Q2 的回应]**：这个问题与我自己的 Q1 高度重合（"高 BCS 和低 BCS batch 的 type distribution 是否完全一致？"）。Appendix O 的 variance decomposition 部分回答了这个问题，但 domain-level 分析确实缺失。

**[对 Q3 的回应]**：好问题。Appendix U（Gemini cross-model validation）仅覆盖了 FewRel count curves 和 BCS-controlled RE，未报告 NER。如果 Gemini 上 NER 也是 BCS-null，则加强了 task asymmetry 的 robustness；如果不是，则 Qwen3-32B 上的 null 可能是 model-specific artifact。这是一个关键的缺失验证。

**[对 Q4 的回应]**：论文在 §3.5 提到 "greedy decoding substantially reduces model-level randomness (residual SD = 0.88pp at count 80)"，且 Appendix R（Cross-Seed Variance Decomposition）显示 "intra-batch variance dominates inter-seed variance by 5-47× across count levels"。这间接表明 FP8 noise 相对于 batch composition 效应是 negligible 的。但直接的 single-seed bootstrap SE 确实未报告。

**[对 Q5 的回应]**：部分同意——见我对 W3 的回应。ρ=0.35 来自条件子集，不代表 random batch 内的平均 pair-level correlation。但论文已声明 simulation 是 illustrative 而非 confirmatory。

---

## Missing References 回应

**R1 建议的三个引用**：
1. **Ding et al. (2024) "GraphER"**：需要验证。如果确实存在且与 schema-guided extraction 直接相关，应补充。
2. **Xu et al. (2024) "How to Handle Different Types of OOD Scenarios"**：与本文的 label space expansion 主题相关性较弱——本文研究的是固定 schema 内的 complexity，而非 OOD label space。建议作者评估后决定。
3. **Cohen (1988) "Statistical Power Analysis"**：同意。论文使用了 TOST 和 power analysis 但未引用 Cohen 的经典著作——这在统计方法论论文中是常见的引用遗漏。

---

## 综合评估

R1 的审稿意见整体质量高，统计方法论审查深入。最有价值的贡献是 W1（DocRED VIF 问题）和 W2（confusability 普遍性审计）——这两点我在自己的审稿中未充分强调。

**与我的评估的主要分歧**：
- R1 重点在统计方法论层面（VIF、TOST margin、ecological amplification），我的重点在贡献定位层面（BCS-controlled design 的方法论新颖性、NER null result 的机制解释）。两者互补。
- R1 对 W3（ecological amplification）的批评力度我认为偏强——simulation 是 illustrative 而非 core evidence，不应视为因果推断链的薄弱环节。
- R1 对 W6（contamination）的担忧我认为论文已有充分回应（Appendix Q）。

**总评不变**：3.5 (Borderline Conference)。R1 的 W1 和 W2 强化了我对论文 generality claims 需要弱化的判断。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2802 · 2026-05-21T21:19:00.797196+00:00_

Reviewer 2 的交叉回应已收到。等待 Reviewer 1 对 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 232

## Round 232

4 recorded events


### User

_source line 2803 · 2026-05-21T21:19:03.416237+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- **W1 (DocRED VIF)**: [AGREE]，VIF=50.9 确实严重，但补充指出核心证据在 FewRel（VIF=1.18），DocRED 是 supporting evidence
- **W2 (普遍性不足)**: [AGREE with nuance]，confusability 证据确实集中于 FewRel RE，但论文 abstract 已做了范围限定，且 count degradation 跨任务稳健
- **W3 (Ecological amplification)**: [REBUT]，simulation 是 illustrative 而非 core evidence，ρ=0.35 来自条件子集而非 marginal correlation，核心因果证据在 §4.3 controlled experiment
- **W4 (Single-model secondary analyses)**: [AGREE]
- **W5 (TOST margin)**: [AGREE]，logit-scale 不一致性应在正文讨论
- **W6 (Contamination)**: [REBUT]，Appendix Q 已提供有力反驳（方向相反 + BCS 效应不受影响）
- **W7 (Pair-level effect size)**: [AGREE]，但补充 pair-level 和 batch-level 对应不同 practical scenario

总评维持 **3.5 (Borderline Conference)**。R1 的 W1/W2 强化了 generality claims 需弱化的判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2804 · 2026-05-21T21:19:10.994081+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2805 · 2026-05-21T21:19:11.094831+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Assistant

_source line 2806 · 2026-05-21T21:19:14.644354+00:00_

Reviewer 2 的交叉回应已收到。等待 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 233

## Round 233

10 recorded events


### User

_source line 2807 · 2026-05-21T21:19:16.153798+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 意见的逐条回应

---

### Must-Fix

**R2-W1 [critical]: BCS-controlled batch design 本质是标准 blocking design，方法论新颖性不足**

[AGREE] 部分同意，但严重性评估与 R2 不同。

R2 的核心论点是正确的：BCS-controlled batching 确实是经典的 blocking/stratified experimental design，而非全新的方法论范式。论文 §1 (p.2) 将 "the methodology—BCS-stratified batch construction with partial correlation controls—is the contribution" 作为首要贡献声明，这一表述确实过度抬高了实验设计技术本身的新颖性。

然而，我认为 R2 低估了**领域特定的操作化贡献**。论文的实际贡献不是 blocking design 本身，而是：(a) 将 type confusability 定义为 embedding cosine similarity 并将其操作化为 SCS/BCS（§3.2）；(b) 构造了 greedy extreme-batch selection 的具体算法使得在 80-relation pool 内可以实现足够大的 BCS 分离度；(c) 在 4 个数据集 × 3 任务上验证了该操作化的有效性。这些构成了一个 "applied methodology contribution"——将已知统计技术首次系统应用于一个特定的未解问题。

**建议调整方向**：同意 R2 所说的 "重新定位贡献重心"——作者应将核心贡献表述为 "empirical findings about confusability's independent predictive role, enabled by a controlled design using SCS/BCS"，而非将 blocking design 本身标为方法论贡献。这是 framing 问题而非 substance 问题，不应构成 rejection 理由。

---

**R2-W2 [critical]: NER null result 的机制解释不充分**

[AGREE] 同意，且这与我的 W2（confusability 仅在 FewRel RE 上稳健）高度一致。

R2 正确指出了论文在 §4.4 和 Appendix E.2 中对 NER null 的解释存在张力：一方面说 "type modes rather than concentrating in type substitution"（暗示 NER 的错误机制不同），另一方面 power analysis 给出 minimum detectable r≈−0.11（暗示可能只是统计功效不足）。论文确实同时持有两个未区分的假设。

但我不同意 R2 建议的 "(a) 设计针对性实验区分两个假设" 作为 revision 要求——这实质上是要求额外实验，超出了 revision cycle 的合理范围。更合理的要求是：

1. 在正文（而非仅 appendix）中明确承认 "基于现有证据无法区分零效应与被噪声掩盖的效应"（R2 建议 b，合理）
2. 在 Limitations 中增加一句 power analysis 的 quantitative summary（n=25, detectable effect=5.5pp, observed r≈−0.11）
3. **关键补充**：我在 Q3 中问过 NER null 是否在 Gemini 上测试——如果答案为否，这应在 Limitations 中标注。

---

### Should-Fix

**R2-W3 [warning]: Limitations 章节过长**

[REBUT] 不同意这是一个 should-fix 级别的问题。

EMNLP 2026 的格式规定是 "Mandatory limitations and optional ethical considerations do not count towards this page limit, **provided they do not contain excessive additional content**"。R2 认为 6 个点 + 额外讨论构成 "excessive additional content"。但我认为：

1. 论文的 Limitations（p.9）中每个点都针对一个真实的方法论局限，没有冗余或 padding。例如 item 1（model coverage）、item 2（effect size and statistical design）、item 3（task scope）每个都回应了 reviewers 可能提出的核心关切。
2. 一篇以实证分析为核心的论文，其 limitations 章节比普通方法论文更长是合理且应被鼓励的。详尽的 limitations 帮助读者正确解读 effect sizes，避免 over-interpretation。
3. 实际操作上，ARR reviewers 很少因 Limitations "太详尽" 而扣分——通常是因为不够详尽。

**建议**：可以将 6 个点压缩至 4-5 个（合并 item 4 和 item 5，都涉及 causal inference），但这是 minor polish，不应列为 should-fix。

---

**R2-W4 [warning]: 跨模型验证未整合入正文**

[AGREE] 完全同意，且与我的 W4 高度一致。

论文的主实验（§4.1–§4.4）全部基于 Qwen3-32B，跨模型验证仅在 Appendix T（LLaMA）和 U（Gemini）中报告。对于一篇声称 "across three open-weight model families" (Abstract, §1) 的论文，核心 cross-model 结果应出现在正文中。具体建议：在 §4.1 末尾加 1-2 句 summary（如 "Count curves replicate on LLaMA-3.1-8B/70B and Gemini 2.5 Flash with near-identical slopes; see Appendix T-U"），在 §4.3 末尾加 Table 24 的摘要。这不需要额外篇幅——几句话即可。

---

**R2-W5 [warning]: Abstract 信息密度过高**

[AGREE] 同意这是一个写作质量问题，但属于 minor 而非 should-fix。

Abstract 确实在 ~150 词中塞入了过多具体数字（"0.72 → ~0.27"、"85.7% → 50.4%"、"88.0% → 38.7%"、"~22%"、"~49pp" 等）。核心 takeaway 被数字流淹没。一个更好的 abstract 应该先明确 conceptual message（"confusability independently predicts type substitution errors beyond the effect of type count"），然后选择性报告 1-2 个最重要的数字。

但这是 stylistic polish，不影响技术评审。不应因此降低 soundness/excitement 评分。

---

**R2-W6 [warning]: Discussion/Conclusion 过度压缩**

[AGREE] 同意，且这与 abstract 的过度压缩形成对比——论文在 abstract 和 results 中花了大量篇幅报告数字，但在 interpretation 和 practical implications 上留的空间不足。

§5 Discussion 和 §6 Conclusion 合并在 p.8 下半页约 25 行，其中 practical implications（§5.2）每个仅一句话。例如 "For RE, reducing candidate types is the primary lever"——这对 practitioners 有什么具体操作建议？BCS 预测的 2.2pp gap 在什么使用场景下是 actionable 的？这些问题在当前版本中未回答。

建议：从 Limitations（R2-W3 建议压缩的部分）挤出 0.5 页给 Discussion，增加 practical guidance。

---

**R2-W7 [warning]: "First controlled study" claim 需更谨慎**

[AGREE] 部分同意。

论文 §1 (p.1) 声称 "the first controlled study isolating type confusability from type count via stratified design in zero-shot LLM IE"。R2 指出 Chen et al. (2026) 隔离了 instance count 和 context length，PARSE (Shrimal et al., 2025) 也研究 schema complexity。

检查论文原文（p.2 Related Work 最后一段），论文确实引用了 Chen et al. (2026) 并区分其研究变量（instance count + context length）与本文的（type count + confusability）。因此论文的 "first" claim 在技术上是成立的——它特指 "isolating type confusability from type count"，而非更宽泛的 controlled study in LLM IE。

但 R2 的建议合理：应将 "first controlled study" 限定为 "first controlled study specifically isolating type confusability from type count in zero-shot LLM IE"，避免歧义。这是 wording refinement，非 substance issue。

---

### Questions

**R2-Q1: 高/低 BCS batch 是否存在 type distribution 以外的系统差异？**

[AGREE] 这是一个重要问题，与我的 Q2 完全一致。

论文的 greedy extreme-batch construction（§3.3: "starts from the least/most similar type pair and iteratively adds the type with maximum/minimum similarity"）可能导致 high-BCS batches 聚集在语义相近的 Wikidata domain（如 social relations），而 low-BCS batches 分散在不同 domain。如果 domain coherence 本身影响 LLM 性能（例如 domain-specific knowledge asymmetry），则 BCS-accuracy 关联可能部分由 domain confound 驱动。

论文的 within-pool comparison（§4.3）部分控制了这一点（pool 内 type 已固定），但 greedy selection 在 pool 内仍可能引入 domain clustering。Appendix K (Format Independence, p.20) 验证了 format 不是 confound，但未分析 domain distribution。这是作者应在 rebuttal 中补充的分析。

---

**R2-Q2: SDGD routing failure 是否意味着瓶颈在 routing 而非 decomposition？**

[AGREE] 这是一个犀利的问题，R2 正确识别了论文叙事中的一个张力。

Table 8 (p.13): Oracle routing 恢复了大部分准确率（72.4% vs 50.4% for single-pass baseline），这确实意味着 decomposition 策略本身不是问题——问题在于 routing quality。论文 §5 (p.8) 将此框架为 "merge amplification (NER, ED) and routing failure (RE)"，但 oracle routing 的成功实际上表明：**如果 routing 问题被解决，schema decomposition 是一个可行的策略。** 这与论文 §5 的结论（"schema decomposition falls due to ... routing failure"）存在微妙矛盾——更准确的说法是 "schema decomposition with current routing methods fails; the decompose-then-merge paradigm is viable but requires better routing。"

建议作者调整 §5 的措辞：承认 decomposition 的 failure 是 routing-conditional 的，而非绝对的。

---

**R2-Q3: Few-NERD 层级结构对 BCS 的影响**

[AGREE] 这是一个有见地的问题，论文未讨论。

Few-NERD 的 66 fine-grained types 嵌套在 8 coarse categories（person, location, organization, building, art, product, event, other）下。直觉上，同一 coarse category 内的 type pairs（如 person-artist vs person-athlete）应该比跨 category pairs（如 person-artist vs location-city）有更高的 SCS 且更容易被混淆。论文的 SCS 计算（§3.2）对所有 type pairs 一视同仁，未区分层级内外的 confusability。

这对 Few-NERD 的 NER null result 可能有影响：如果大部分 high-SCS pairs 来自同一 coarse category，而 NER 的主要错误是 boundary detection（而非 intra-category type substitution），则 BCS 可能无法捕捉 NER 的核心错误模式。论文应在 Discussion 或 Limitations 中讨论 hierarchical structure 的影响。

---

### Missing References

**Baan et al. (2023) "The Ecological Fallacy in Annotation"**: [AGREE] 这是一篇直接相关的工作，论文讨论了 ecological correlation（§4.3, Appendix N）并引用了 Robinson (1950)，但未引用 NLP 领域内对 ecological fallacy 的近期讨论。建议添加。

**ScrapeGraphAI-100k (Cataldo et al., 2025)**: [REBUT] 需要更多信息。如果该工作研究的是 web scraping 场景下的 schema complexity 对 extraction reliability 的影响，其与本文的 training-free LLM IE + type-level confusability 分析在 task setting 上差异较大，不是必须引用的文献。但如果其中有关于 type count 退化的定量分析，可考虑加入 Related Work。

---

### 总结

R2 的 7 个 Weaknesses 和 3 个 Questions 中：

| 编号 | 判断 | 说明 |
|------|------|------|
| W1 | AGREE (部分) | 贡献 framing 应从 "methodology" 转向 "empirical findings"；是 framing 而非 substance 问题 |
| W2 | AGREE | 与我的 W2 一致；NER null 机制解释确实不充分 |
| W3 | REBUT | Limitations 详尽是优势而非缺陷；降级为 minor |
| W4 | AGREE | 与我的 W4 一致；跨模型结果应在正文 summary |
| W5 | AGREE (降级) | 同意但属 minor stylistic issue |
| W6 | AGREE | Discussion 需更多空间阐述 practical implications |
| W7 | AGREE (部分) | 技术上 "first" 成立但措辞应更精确 |
| Q1 | AGREE | 与我的 Q2 一致；domain confound 是关键问题 |
| Q2 | AGREE | 犀利——routing vs decomposition 的因果归因需修正 |
| Q3 | AGREE | 层级结构对 BCS 的影响未讨论，可能影响 NER null 解读 |

**整体评价**：R2 的审稿在写作质量和新颖性维度上提出了合理问题。W1 的严重性我认为略低于 R2 的评估（framing issue, not substance），W3 我明确不同意（Limitations 的详尽是加分项）。最有价值的贡献是 Q2（routing vs decomposition 因果归因）和 Q3（层级结构），这两点从不同角度补充了我在 Round 1 中未充分关注的方面。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2808 · 2026-05-21T21:19:58.759027+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 2809 · 2026-05-21T21:19:58.860019+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T21:15:04.974430+00:00\", \"completed_at\": \"2026-05-21T21:18:29.546754+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-3\", \"message\": \"前 3 页连续纯文本，无任何 display item。审稿人打开论文前 3 页看不到视觉锚点——对于一篇以实证为核心的 controlled study，第一个 figure 直到 page 5 才出现，严重影响第一印象。建议将核心结果图（如 Figure 1 的关键 panel）提前到 page 2 或 Introduction 末尾\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-8\", \"message\": \"主文仅 4 个 display items（2 figure + 2 table），对于 4 个数据集、多维度分析的实证论文偏少（经验值 5-8 个）。大量关键数据被推到 14 页附录（20+ 表格），主文读起来像文字摘要而非数据驱动的论证。建议从附录提升 1-2 个关键表格/图到主文\"}, {\"severity\": \"warning\", \"dimension\": \"page 8-9\", \"message\": \"Section 5 (Schema Decomposition) + Section 6 (Discussion/Conclusion) + Limitations 连续 2 页纯文本，无 display item 穿插。Section 5 讨论 decomposition 策略的效果，可考虑加一个对比表或示意图增强可读性\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 1 右侧 bar chart 内部标注文字（如 \\\"r=4.1yp\\\"）字号偏小，低缩放下可能难以阅读。建议增大标注字号或移到 bar 外部\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2 中 IntraSub (红色)、Extrable (橙色) 线条颜色较接近，部分色盲读者可能难以区分。建议辅以不同 line style (dashed/dotted) 或 marker shape\"}, {\"severity\": \"info\", \"dimension\": \"page 13-26\", \"message\": \"附录 14 页全部为表格和文字，无任何 figure。对于深入阅读附录的审稿人，视觉上极度单调。若有空间，可将部分 ablation 数据可视化为图表\"}, {\"severity\": \"info\", \"dimension\": \"page 26\", \"message\": \"最后一页底部约 1/3 空白\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 1 caption 较为详尽（包含误差说明、条件描述），自包含性好\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Table 1 使用 booktabs 风格，无竖线，排版专业\"}], \"counts\": {\"critical\": 0, \"warning\": 3, \"info\": 6}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2810 · 2026-05-21T21:19:58.910650+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 2811 · 2026-05-21T21:19:59.011496+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2812 · 2026-05-21T21:22:38.424826+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "schema-dag-extraction",
  "issues_yaml": "# Review Issues Tracker\n# Updated: 2026-05-21 (Round 25 Fresh — Consolidated Report)\n\n# ============================================================\n# R25 MUST-FIX (4 items, R1+R2 consensus)\n# ============================================================\n\n- id: R25-C1\n  summary: \"DocRED VIF=50.9 invalidates R²=58% as independent BCS evidence; must report semipartial R²\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-C2: VIF=50.9, weaken wording\"}\n    - {round: 24, reviewers: [R1, R2], note: \"R24-C1: Must recenter on FewRel R²=22%\"}\n    - {round: 25, reviewers: [R1, R2], note: \"R1-W1 raised, R2 AGREE. VIF=50.9 far exceeds threshold 10. partial r=-0.344 解释力远低于 R²=58%. Must report semipartial R² or use ridge/LASSO. R2 adds nuance: core evidence is FewRel (VIF=1.18), DocRED is supporting.\"}\n  action_items:\n    - {round: 25, action: \"Report DocRED semipartial R² (BCS unique variance after partialing centrality); demote DocRED R²=58% to 'directionally consistent but confounded by VIF=50.9' in §4.3 and Abstract\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R25-C2\n  summary: \"Confusability finding robust only on FewRel RE; generality claims in title/abstract overstate evidence scope\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: [R1, R2], note: \"R1-W2 raised, R2 AGREE with nuance. Per-dataset audit: FewRel ✓, NER ✗ (null on 3 models), DocRED △ (VIF), MAVEN △ (frequency confound), Gemini △ (leverage-sensitive). R2 notes Abstract already scopes 'In RE' and count degradation is cross-task robust. Both agree confusability evidence concentrated on FewRel RE.\"}\n  action_items:\n    - {round: 25, action: \"Weaken title/abstract/conclusion generality claims; explicitly state confusability evidence is primarily from FewRel RE; count degradation is the cross-task finding\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R25-C3\n  summary: \"NER null result mechanism: cannot distinguish zero effect from noise-masked effect; paper holds both hypotheses without resolution\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-C3: NER null narrative tension\"}\n    - {round: 24, reviewers: [R1, R2], note: \"R24-C5: dual-layer still reads ambiguous\"}\n    - {round: 25, reviewers: [R1, R2], note: \"R2-W2 raised, R1 AGREE. Two hypotheses (zero effect vs insufficient power) have different practical implications but paper provides no distinguishing evidence. R1 adds: requesting new experiments unreasonable for revision, but must explicitly acknowledge ambiguity in main text + quantitative power summary.\"}\n  action_items:\n    - {round: 25, action: \"In main text (not just appendix): explicitly state 'current evidence cannot distinguish zero effect from noise-masked effect'; add power analysis summary (n=25, detectable=5.5pp, observed r≈-0.11); note Gemini NER untested\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R25-C4\n  summary: \"Contribution framing: BCS-controlled batch design is standard blocking/stratified design, not a novel methodology\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-W1: SCS vs LLM-PEE novelty\"}\n    - {round: 24, reviewers: [R1, R2], note: \"R24-C4: methodology vs metric separation needed\"}\n    - {round: 25, reviewers: [R1, R2], note: \"R2-W1 raised, R1 AGREE partially. R2: BCS-controlled batching is classic blocking design with decades of history; contribution should shift to empirical findings. R1: agrees on reframing but notes domain-specific operationalization (SCS definition, greedy extreme-batch algorithm, multi-dataset validation) has value as 'applied methodology'. Both agree: core contribution = empirical findings, not the experimental design technique itself.\"}\n  action_items:\n    - {round: 25, action: \"Reframe Contribution 1: 'empirical findings about confusability's independent predictive role, enabled by BCS-controlled design' rather than 'methodology is the contribution'. Acknowledge blocking design is standard; emphasize domain-specific operationalization.\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R25 SHOULD-FIX (8 items)\n# ============================================================\n\n- id: R25-W1\n  summary: \"Error taxonomy, TOST, SDGD all single-model (Qwen3-32B); secondary claims lack cross-model support\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - {round: 24, reviewers: [R1, R2], note: \"R24-W2: Core analyses lack cross-model validation\"}\n    - {round: 25, reviewers: [R1, R2], note: \"R1-W4 raised, R2-W4 independently raised. Both AGREE. SDGD merge amplification could be Qwen3-specific instruction-following issue. At minimum, Limitations must label these as single-model findings.\"}\n  action_items:\n    - {round: 25, action: \"Replicate error taxonomy or TOST on one alternative model; if infeasible, explicitly label in Limitations as single-model pending replication\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R25-W2\n  summary: \"Cross-model validation results buried in appendix; main text lacks summary of LLaMA-70B/Gemini findings\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: [R1, R2], note: \"R2-W4 raised, R1 AGREE. Paper claims 'across three open-weight model families' but all main-text experiments are Qwen3-32B only. Need 1-2 sentences in §4.1 and §4.3 summarizing cross-model results.\"}\n  action_items:\n    - {round: 25, action: \"Add brief cross-model summary in §4.1 (count curves) and §4.3 (BCS-controlled): 1-2 sentences each referencing Appendix T-U\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R25-W3\n  summary: \"Ecological amplification (1.3%→22%) needs batch-level confound control beyond BCS\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: [R1, R2], note: \"R1-W3 raised as Must-Fix, R2 REBUT. R2 argues simulation is illustrative (paper explicitly states this), core evidence is §4.3 controlled experiment, and Appendix O provides variance decomposition. R1's concern about batch-mean type frequency and domain diversity as confounds is valid but partially addressed. DIVERGENCE: R1=Must-Fix, R2=Not an issue. Director downgrades to Should-Fix.\"}\n  action_items:\n    - {round: 25, action: \"In §4.3 or Appendix: report batch-level regression with additional controls (batch-mean type frequency, domain diversity) to show R² stability; clarify simulation is illustrative in main text\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R25-W4\n  summary: \"TOST ±3pp margin: logit-scale inconclusive, margin justification insufficient in main text\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: [R1, R2], note: \"R1-W5 raised, R2 AGREE. At FewRel ~80% accuracy, ±3pp is ~15% relative error. Back-transformed interaction at median=2.78pp, near boundary. Logit-scale TOST inconclusive (p=0.209 at ±3pp equivalent). Margin lacks domain-specific justification. R2 adds: sensitivity analysis (±1pp/±5pp) exists in appendix but should be referenced in main text.\"}\n  action_items:\n    - {round: 25, action: \"In main text §4.4: acknowledge logit-scale inconsistency; justify probability-scale as primary (practitioners care about absolute pp); reference sensitivity analysis from Appendix C\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R25-W5\n  summary: \"Abstract information overload: too many numbers obscure key takeaways\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - {round: 24, reviewers: [R1, R2], note: \"R24-W5: Too many numbers in Abstract\"}\n    - {round: 25, reviewers: [R1, R2], note: \"R2-W5 raised, R1 AGREE (downgrades to minor). ~150 words with 6+ specific numbers. Core takeaway buried under statistical details. R1: stylistic polish, doesn't affect soundness.\"}\n  action_items:\n    - {round: 25, action: \"Rewrite Abstract: lead with conceptual message, retain only 1-2 key numbers (R²≈22%, -49pp decline), move rest to main text\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R25-W6\n  summary: \"Discussion/Conclusion over-compressed (~25 lines); practical implications under-developed\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - {round: 24, reviewers: [R1, R2], note: \"R24-W6: §5-6 过度压缩\"}\n    - {round: 25, reviewers: [R1, R2], note: \"R2-W6 raised, R1 AGREE. Discussion merges 3 themes in ~25 lines. Practical implications (SCS as diagnostic, schema-aware pool selection) each get one sentence. For an empirical-findings paper, Discussion should be the payoff section.\"}\n  action_items:\n    - {round: 25, action: \"Compress §2 (Related Work) or Limitations by ~0.3 pages; expand Discussion with practical guidance (when is 2.2pp gap actionable? concrete SCS threshold recommendations)\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R25-W7\n  summary: \"Pairwise r²≈1.3% (IQR gap 2.2pp) practical significance undiscussed\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: [R1, R2], note: \"R1-W7 raised, R2 AGREE with nuance. R2: pair-level and batch-level correspond to different practical scenarios (individual pair prediction vs prompt schema design). Both agree paper should discuss when 2.2pp is actionable.\"}\n  action_items:\n    - {round: 25, action: \"In Discussion: distinguish pair-level (1.3%, marginal for individual prediction) vs batch-level (22%, actionable for schema design); discuss practical threshold for SCS-guided decisions\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R25-W8\n  summary: \"'First controlled study' claim should be more precisely scoped\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: [R1, R2], note: \"R2-W7 raised, R1 AGREE partially. Chen et al. (2026) isolates instance count + context length with similar design logic. R1 notes claim is technically accurate but should be more precisely worded. Both agree: minor wording fix.\"}\n  action_items:\n    - {round: 25, action: \"Refine to 'first controlled study specifically isolating type confusability from type count using embedding-based batch-level controls in zero-shot LLM IE'\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R25 MINOR (3 items)\n# ============================================================\n\n- id: R25-M1\n  summary: \"8 orphan bib entries (uncited in text)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: [R1, R2], note: \"Both independently identified: dee-2024, gillick-2014, novack-2023, schall-2025, tam-2024, volkanovska2025ner, wei-2023, zhou-2025-rethinking\"}\n  action_items:\n    - {round: 25, action: \"Clean .bib file before submission\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R25-M2\n  summary: \"Limitations section length: detailed but borderline excessive for EMNLP\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: [R1, R2], note: \"R2-W3 raised as Should-Fix, R1 REBUT (detailed limitations is a strength for empirical paper). DIVERGENCE. Director notes: 6 points + 2 paragraphs is long but each addresses real concern. Compress items 4+5 (both causal inference) and move technical details to appendix.\"}\n  action_items:\n    - {round: 25, action: \"Consider compressing to 4-5 points; merge items 4 (causal mechanism) and 5 (data contamination)\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R25-M3\n  summary: \"SDGD failure framing: routing-conditional, not absolute\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: [R1, R2], note: \"R2-Q2 raised, R1 AGREE. Oracle routing recovers 72.4% vs 50.4%. §5 says 'decomposition fails due to routing failure' but oracle success means decomposition is viable with better routing. Wording should be 'decomposition with current routing methods fails; paradigm is viable but requires better routing'.\"}\n  action_items:\n    - {round: 25, action: \"Adjust §5 wording to acknowledge routing-conditional nature of SDGD failure\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R24 issues — R25 status update\n# ============================================================\n\n- id: R24-C1\n  summary: \"DocRED R²=58% confounded by centrality (VIF=50.9)\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 25\n  resolution: \"Merged into R25-C1. Paper partially addressed in previous rounds but R25 fresh reviewers still flag as critical.\"\n  resolution_round: null\n\n- id: R24-C2\n  summary: \"Gemini BCS-controlled driven by single leverage point\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: [R1], note: \"R1 mentions in W2 audit (Gemini leave-one-out r: -0.80→-0.42, p=0.22) but as part of broader generality issue, not standalone must-fix. Paper already describes as 'partial but fragile corroboration' with leave-one-out stats. May be adequately addressed in current version.\"}\n  resolution: \"Subsumed by R25-C2 (generality issue). Paper's current framing ('partial but fragile') is appropriate.\"\n  resolution_round: null\n\n- id: R24-C3\n  summary: \"Ecological correlation caveat needs more prominent framing\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: [R1], note: \"R1-W3 raises different angle (batch-level confound control), R2 rebuts. Robinson (1950) citation now present. Original caveat issue partially addressed; new angle tracked as R25-W3.\"}\n  resolution: \"Original caveat issue (Robinson citation) resolved; new confound control angle tracked as R25-W3.\"\n  resolution_round: null\n\n- id: R24-C4\n  summary: \"SCS/BCS novelty insufficient\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 25\n  resolution: \"Merged into R25-C4. 'Metric is a means; methodology is the contribution' sentence now present but R25 still flags methodology framing as overclaim.\"\n  resolution_round: null\n\n- id: R24-C5\n  summary: \"NER null narrative tension\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 25\n  resolution: \"Merged into R25-C3. Dual-layer framing improved but R25 still finds ambiguity between zero-effect and noise-masked hypotheses.\"\n  resolution_round: null\n\n- id: R24-W1\n  summary: \"DocRED 5 batches/level — small sample R² bias\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 25\n  resolution: \"Subsumed by R25-C1 (DocRED demotion). Not independently raised in R25.\"\n  resolution_round: null\n\n- id: R24-W2\n  summary: \"Core analyses lack cross-model validation\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 25\n  resolution: \"Merged into R25-W1 and R25-W2.\"\n  resolution_round: null\n\n- id: R24-W3\n  summary: \"BCS-controlled greedy construction introduces domain coverage bias\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: [R1, R2], note: \"Re-raised as R1-Q2 and R2-Q1. Both agree domain-level analysis missing from Appendix O.\"}\n  resolution: \"Still open; tracked via R25-W3 (batch-level confound control) and Questions.\"\n  resolution_round: null\n\n- id: R24-W4\n  summary: \"Single seed + FP8 non-determinism\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: [R1], note: \"R1-Q4 asks for single-seed bootstrap SE but acknowledges Appendix R variance decomposition (batch >> seed by 5-47×) is adequate. Not flagged as weakness.\"}\n  resolution: \"Adequately addressed in Limitations + Appendix R. Residual SD=0.88pp, batch variance dominates.\"\n  resolution_round: 25\n\n- id: R24-W5\n  summary: \"Abstract information overload\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 24\n  last_seen_round: 25\n  resolution: \"Merged into R25-W5. Still flagged by R25 fresh reviewers.\"\n  resolution_round: null\n\n- id: R24-W6\n  summary: \"§5-6 过度压缩; §2 可压缩\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 25\n  resolution: \"Merged into R25-W6. Still flagged by R25 fresh reviewers.\"\n  resolution_round: null\n\n- id: R24-W7\n  summary: \"BCS clean validation limited to FewRel only\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 24\n  last_seen_round: 25\n  resolution: \"Subsumed by R25-C2 (confusability generality).\"\n  resolution_round: null\n\n# ============================================================\n# R23 issues — status (carried forward from R24)\n# ============================================================\n\n- id: R23-C1\n  summary: \"Logit-scale TOST inconclusive\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"v32: logit results in main text, claim adjusted. R25-W4 raises margin justification as new angle.\"\n  resolution_round: 23\n\n- id: R23-W2\n  summary: \"TOST margin circularity\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"v32: deleted IQR argument, pure conceptual + Cohen's d\"\n  resolution_round: 23\n\n- id: R23-W7\n  summary: \"Bootstrap CI non-independence\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"v32 Limitations added across-batch correlation discussion\"\n  resolution_round: 23\n\n- id: R23-F1\n  summary: \"Checklist in PDF — format violation\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"v32 removed checklist from PDF\"\n  resolution_round: 23\n\n# ============================================================\n# R22 RESOLVED (compact, carried forward)\n# ============================================================\n\n- id: R22-C1\n  summary: \"Title/Abstract scope overclaim\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 22\n  resolution: \"v12 Abstract rewrite\"\n  resolution_round: 22\n\n- id: R22-C4\n  summary: \"Page violation\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"v12 Conclusion merged into Discussion\"\n  resolution_round: 22"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "schema-dag-extraction",
    "issues_yaml": "# Review Issues Tracker\n# Updated: 2026-05-21 (Round 25 Fresh — Consolidated Report)\n\n# ============================================================\n# R25 MUST-FIX (4 items, R1+R2 consensus)\n# ============================================================\n\n- id: R25-C1\n  summary: \"DocRED VIF=50.9 invalidates R²=58% as independent BCS evidence; must report semipartial R²\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-C2: VIF=50.9, weaken wording\"}\n    - {round: 24, reviewers: [R1, R2], note: \"R24-C1: Must recenter on FewRel R²=22%\"}\n    - {round: 25, reviewers: [R1, R2], note: \"R1-W1 raised, R2 AGREE. VIF=50.9 far exceeds threshold 10. partial r=-0.344 解释力远低于 R²=58%. Must report semipartial R² or use ridge/LASSO. R2 adds nuance: core evidence is FewRel (VIF=1.18), DocRED is supporting.\"}\n  action_items:\n    - {round: 25, action: \"Report DocRED semipartial R² (BCS unique variance after partialing centrality); demote DocRED R²=58% to 'directionally consistent but confounded by VIF=50.9' in §4.3 and Abstract\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R25-C2\n  summary: \"Confusability finding robust only on FewRel RE; generality claims in title/abstract overstate evidence scope\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: [R1, R2], note: \"R1-W2 raised, R2 AGREE with nuance. Per-dataset audit: FewRel ✓, NER ✗ (null on 3 models), DocRED △ (VIF), MAVEN △ (frequency confound), Gemini △ (leverage-sensitive). R2 notes Abstract already scopes 'In RE' and count degradation is cross-task robust. Both agree confusability evidence concentrated on FewRel RE.\"}\n  action_items:\n    - {round: 25, action: \"Weaken title/abstract/conclusion generality claims; explicitly state confusability evidence is primarily from FewRel RE; count degradation is the cross-task finding\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R25-C3\n  summary: \"NER null result mechanism: cannot distinguish zero effect from noise-masked effect; paper holds both hypotheses without resolution\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-C3: NER null narrative tension\"}\n    - {round: 24, reviewers: [R1, R2], note: \"R24-C5: dual-layer still reads ambiguous\"}\n    - {round: 25, reviewers: [R1, R2], note: \"R2-W2 raised, R1 AGREE. Two hypotheses (zero effect vs insufficient power) have different practical implications but paper provides no distinguishing evidence. R1 adds: requesting new experiments unreasonable for revision, but must explicitly acknowledge ambiguity in main text + quantitative power summary.\"}\n  action_items:\n    - {round: 25, action: \"In main text (not just appendix): explicitly state 'current evidence cannot distinguish zero effect from noise-masked effect'; add power analysis summary (n=25, detectable=5.5pp, observed r≈-0.11); note Gemini NER untested\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R25-C4\n  summary: \"Contribution framing: BCS-controlled batch design is standard blocking/stratified design, not a novel methodology\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-W1: SCS vs LLM-PEE novelty\"}\n    - {round: 24, reviewers: [R1, R2], note: \"R24-C4: methodology vs metric separation needed\"}\n    - {round: 25, reviewers: [R1, R2], note: \"R2-W1 raised, R1 AGREE partially. R2: BCS-controlled batching is classic blocking design with decades of history; contribution should shift to empirical findings. R1: agrees on reframing but notes domain-specific operationalization (SCS definition, greedy extreme-batch algorithm, multi-dataset validation) has value as 'applied methodology'. Both agree: core contribution = empirical findings, not the experimental design technique itself.\"}\n  action_items:\n    - {round: 25, action: \"Reframe Contribution 1: 'empirical findings about confusability's independent predictive role, enabled by BCS-controlled design' rather than 'methodology is the contribution'. Acknowledge blocking design is standard; emphasize domain-specific operationalization.\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R25 SHOULD-FIX (8 items)\n# ============================================================\n\n- id: R25-W1\n  summary: \"Error taxonomy, TOST, SDGD all single-model (Qwen3-32B); secondary claims lack cross-model support\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - {round: 24, reviewers: [R1, R2], note: \"R24-W2: Core analyses lack cross-model validation\"}\n    - {round: 25, reviewers: [R1, R2], note: \"R1-W4 raised, R2-W4 independently raised. Both AGREE. SDGD merge amplification could be Qwen3-specific instruction-following issue. At minimum, Limitations must label these as single-model findings.\"}\n  action_items:\n    - {round: 25, action: \"Replicate error taxonomy or TOST on one alternative model; if infeasible, explicitly label in Limitations as single-model pending replication\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R25-W2\n  summary: \"Cross-model validation results buried in appendix; main text lacks summary of LLaMA-70B/Gemini findings\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: [R1, R2], note: \"R2-W4 raised, R1 AGREE. Paper claims 'across three open-weight model families' but all main-text experiments are Qwen3-32B only. Need 1-2 sentences in §4.1 and §4.3 summarizing cross-model results.\"}\n  action_items:\n    - {round: 25, action: \"Add brief cross-model summary in §4.1 (count curves) and §4.3 (BCS-controlled): 1-2 sentences each referencing Appendix T-U\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R25-W3\n  summary: \"Ecological amplification (1.3%→22%) needs batch-level confound control beyond BCS\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: [R1, R2], note: \"R1-W3 raised as Must-Fix, R2 REBUT. R2 argues simulation is illustrative (paper explicitly states this), core evidence is §4.3 controlled experiment, and Appendix O provides variance decomposition. R1's concern about batch-mean type frequency and domain diversity as confounds is valid but partially addressed. DIVERGENCE: R1=Must-Fix, R2=Not an issue. Director downgrades to Should-Fix.\"}\n  action_items:\n    - {round: 25, action: \"In §4.3 or Appendix: report batch-level regression with additional controls (batch-mean type frequency, domain diversity) to show R² stability; clarify simulation is illustrative in main text\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R25-W4\n  summary: \"TOST ±3pp margin: logit-scale inconclusive, margin justification insufficient in main text\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: [R1, R2], note: \"R1-W5 raised, R2 AGREE. At FewRel ~80% accuracy, ±3pp is ~15% relative error. Back-transformed interaction at median=2.78pp, near boundary. Logit-scale TOST inconclusive (p=0.209 at ±3pp equivalent). Margin lacks domain-specific justification. R2 adds: sensitivity analysis (±1pp/±5pp) exists in appendix but should be referenced in main text.\"}\n  action_items:\n    - {round: 25, action: \"In main text §4.4: acknowledge logit-scale inconsistency; justify probability-scale as primary (practitioners care about absolute pp); reference sensitivity analysis from Appendix C\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R25-W5\n  summary: \"Abstract information overload: too many numbers obscure key takeaways\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - {round: 24, reviewers: [R1, R2], note: \"R24-W5: Too many numbers in Abstract\"}\n    - {round: 25, reviewers: [R1, R2], note: \"R2-W5 raised, R1 AGREE (downgrades to minor). ~150 words with 6+ specific numbers. Core takeaway buried under statistical details. R1: stylistic polish, doesn't affect soundness.\"}\n  action_items:\n    - {round: 25, action: \"Rewrite Abstract: lead with conceptual message, retain only 1-2 key numbers (R²≈22%, -49pp decline), move rest to main text\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R25-W6\n  summary: \"Discussion/Conclusion over-compressed (~25 lines); practical implications under-developed\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - {round: 24, reviewers: [R1, R2], note: \"R24-W6: §5-6 过度压缩\"}\n    - {round: 25, reviewers: [R1, R2], note: \"R2-W6 raised, R1 AGREE. Discussion merges 3 themes in ~25 lines. Practical implications (SCS as diagnostic, schema-aware pool selection) each get one sentence. For an empirical-findings paper, Discussion should be the payoff section.\"}\n  action_items:\n    - {round: 25, action: \"Compress §2 (Related Work) or Limitations by ~0.3 pages; expand Discussion with practical guidance (when is 2.2pp gap actionable? concrete SCS threshold recommendations)\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R25-W7\n  summary: \"Pairwise r²≈1.3% (IQR gap 2.2pp) practical significance undiscussed\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: [R1, R2], note: \"R1-W7 raised, R2 AGREE with nuance. R2: pair-level and batch-level correspond to different practical scenarios (individual pair prediction vs prompt schema design). Both agree paper should discuss when 2.2pp is actionable.\"}\n  action_items:\n    - {round: 25, action: \"In Discussion: distinguish pair-level (1.3%, marginal for individual prediction) vs batch-level (22%, actionable for schema design); discuss practical threshold for SCS-guided decisions\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R25-W8\n  summary: \"'First controlled study' claim should be more precisely scoped\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: [R1, R2], note: \"R2-W7 raised, R1 AGREE partially. Chen et al. (2026) isolates instance count + context length with similar design logic. R1 notes claim is technically accurate but should be more precisely worded. Both agree: minor wording fix.\"}\n  action_items:\n    - {round: 25, action: \"Refine to 'first controlled study specifically isolating type confusability from type count using embedding-based batch-level controls in zero-shot LLM IE'\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R25 MINOR (3 items)\n# ============================================================\n\n- id: R25-M1\n  summary: \"8 orphan bib entries (uncited in text)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: [R1, R2], note: \"Both independently identified: dee-2024, gillick-2014, novack-2023, schall-2025, tam-2024, volkanovska2025ner, wei-2023, zhou-2025-rethinking\"}\n  action_items:\n    - {round: 25, action: \"Clean .bib file before submission\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R25-M2\n  summary: \"Limitations section length: detailed but borderline excessive for EMNLP\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: [R1, R2], note: \"R2-W3 raised as Should-Fix, R1 REBUT (detailed limitations is a strength for empirical paper). DIVERGENCE. Director notes: 6 points + 2 paragraphs is long but each addresses real concern. Compress items 4+5 (both causal inference) and move technical details to appendix.\"}\n  action_items:\n    - {round: 25, action: \"Consider compressing to 4-5 points; merge items 4 (causal mechanism) and 5 (data contamination)\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R25-M3\n  summary: \"SDGD failure framing: routing-conditional, not absolute\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: [R1, R2], note: \"R2-Q2 raised, R1 AGREE. Oracle routing recovers 72.4% vs 50.4%. §5 says 'decomposition fails due to routing failure' but oracle success means decomposition is viable with better routing. Wording should be 'decomposition with current routing methods fails; paradigm is viable but requires better routing'.\"}\n  action_items:\n    - {round: 25, action: \"Adjust §5 wording to acknowledge routing-conditional nature of SDGD failure\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R24 issues — R25 status update\n# ============================================================\n\n- id: R24-C1\n  summary: \"DocRED R²=58% confounded by centrality (VIF=50.9)\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 25\n  resolution: \"Merged into R25-C1. Paper partially addressed in previous rounds but R25 fresh reviewers still flag as critical.\"\n  resolution_round: null\n\n- id: R24-C2\n  summary: \"Gemini BCS-controlled driven by single leverage point\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: [R1], note: \"R1 mentions in W2 audit (Gemini leave-one-out r: -0.80→-0.42, p=0.22) but as part of broader generality issue, not standalone must-fix. Paper already describes as 'partial but fragile corroboration' with leave-one-out stats. May be adequately addressed in current version.\"}\n  resolution: \"Subsumed by R25-C2 (generality issue). Paper's current framing ('partial but fragile') is appropriate.\"\n  resolution_round: null\n\n- id: R24-C3\n  summary: \"Ecological correlation caveat needs more prominent framing\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: [R1], note: \"R1-W3 raises different angle (batch-level confound control), R2 rebuts. Robinson (1950) citation now present. Original caveat issue partially addressed; new angle tracked as R25-W3.\"}\n  resolution: \"Original caveat issue (Robinson citation) resolved; new confound control angle tracked as R25-W3.\"\n  resolution_round: null\n\n- id: R24-C4\n  summary: \"SCS/BCS novelty insufficient\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 25\n  resolution: \"Merged into R25-C4. 'Metric is a means; methodology is the contribution' sentence now present but R25 still flags methodology framing as overclaim.\"\n  resolution_round: null\n\n- id: R24-C5\n  summary: \"NER null narrative tension\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 25\n  resolution: \"Merged into R25-C3. Dual-layer framing improved but R25 still finds ambiguity between zero-effect and noise-masked hypotheses.\"\n  resolution_round: null\n\n- id: R24-W1\n  summary: \"DocRED 5 batches/level — small sample R² bias\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 25\n  resolution: \"Subsumed by R25-C1 (DocRED demotion). Not independently raised in R25.\"\n  resolution_round: null\n\n- id: R24-W2\n  summary: \"Core analyses lack cross-model validation\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 25\n  resolution: \"Merged into R25-W1 and R25-W2.\"\n  resolution_round: null\n\n- id: R24-W3\n  summary: \"BCS-controlled greedy construction introduces domain coverage bias\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: [R1, R2], note: \"Re-raised as R1-Q2 and R2-Q1. Both agree domain-level analysis missing from Appendix O.\"}\n  resolution: \"Still open; tracked via R25-W3 (batch-level confound control) and Questions.\"\n  resolution_round: null\n\n- id: R24-W4\n  summary: \"Single seed + FP8 non-determinism\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - {round: 25, reviewers: [R1], note: \"R1-Q4 asks for single-seed bootstrap SE but acknowledges Appendix R variance decomposition (batch >> seed by 5-47×) is adequate. Not flagged as weakness.\"}\n  resolution: \"Adequately addressed in Limitations + Appendix R. Residual SD=0.88pp, batch variance dominates.\"\n  resolution_round: 25\n\n- id: R24-W5\n  summary: \"Abstract information overload\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 24\n  last_seen_round: 25\n  resolution: \"Merged into R25-W5. Still flagged by R25 fresh reviewers.\"\n  resolution_round: null\n\n- id: R24-W6\n  summary: \"§5-6 过度压缩; §2 可压缩\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 25\n  resolution: \"Merged into R25-W6. Still flagged by R25 fresh reviewers.\"\n  resolution_round: null\n\n- id: R24-W7\n  summary: \"BCS clean validation limited to FewRel only\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 24\n  last_seen_round: 25\n  resolution: \"Subsumed by R25-C2 (confusability generality).\"\n  resolution_round: null\n\n# ============================================================\n# R23 issues — status (carried forward from R24)\n# ============================================================\n\n- id: R23-C1\n  summary: \"Logit-scale TOST inconclusive\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"v32: logit results in main text, claim adjusted. R25-W4 raises margin justification as new angle.\"\n  resolution_round: 23\n\n- id: R23-W2\n  summary: \"TOST margin circularity\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"v32: deleted IQR argument, pure conceptual + Cohen's d\"\n  resolution_round: 23\n\n- id: R23-W7\n  summary: \"Bootstrap CI non-independence\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"v32 Limitations added across-batch correlation discussion\"\n  resolution_round: 23\n\n- id: R23-F1\n  summary: \"Checklist in PDF — format violation\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"v32 removed checklist from PDF\"\n  resolution_round: 23\n\n# ============================================================\n# R22 RESOLVED (compact, carried forward)\n# ============================================================\n\n- id: R22-C1\n  summary: \"Title/Abstract scope overclaim\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 22\n  resolution: \"v12 Abstract rewrite\"\n  resolution_round: 22\n\n- id: R22-C4\n  summary: \"Page violation\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"v12 Conclusion merged into Discussion\"\n  resolution_round: 22"
  }
}
```

</details>

---


### Tool result

_source line 2813 · 2026-05-21T21:22:38.475790+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml\", \"bytes\": 20157}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2814 · 2026-05-21T21:25:45.611959+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 25 (Fresh)\n\n**论文**: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n**Venue**: EMNLP 2026 (ACL Rolling Review, May 2026 cycle, Long Paper)\n**Deadline**: 2026-05-25\n**审稿模式**: Fresh (重新审稿，无上轮记忆)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量）\n\n---\n\n## Summary\n\n本文通过受控实验设计研究 training-free LLM 信息抽取中 schema 复杂度的两个维度——type count 和 type confusability——如何独立预测性能下降。使用 Schema Confusability Score (SCS) 和 Batch Confusability Score (BCS) 量化 confusability，在 Few-NERD (NER)、FewRel (RE)、DocRED (document-level RE)、MAVEN (ED) 上通过 count curve 和 BCS-controlled 实验验证。核心发现：(1) count 驱动 recall 下降（跨任务 robust），(2) confusability 驱动 type substitution（BCS 在 FewRel 解释 ~22% batch-level RE accuracy variance），(3) NER batch-level BCS 信号未检测到（task asymmetry），(4) Schema decomposition 因 merge amplification 和 routing failure 失败。\n\n---\n\n## Strengths\n\n**S1. 研究问题明确且实用。** 将 schema 复杂度分解为 count 和 confusability 两个独立维度是干净、有说服力的框架。SCS 作为无需运行抽取即可计算的 pre-hoc proxy，对 practitioners 有直接部署价值。\n\n**S2. FewRel BCS-controlled 实验设计严谨。** Within-pool 80-relation 比较有效控制 type frequency 混淆；2×2 factorial analysis 正式检验了 interaction boundedness；TOST 等价检验引入了 NLP 领域罕见的统计严谨性。[R1, R2 共识]\n\n**S3. 统计方法论远超同领域平均水平。** Bootstrap CIs、permutation tests、partial correlation (controlling degree centrality/type frequency)、TOST、power analysis for NER null——这种统计意识在 NLP 投稿中非常突出。[R1, R2 共识]\n\n**S4. 负面结果的诚实报告。** §5 完整报告 SDGD 失败及其原因分析（merge amplification, routing failure）。NER batch-level null 在 3 模型上确认并明确标注可能是 insufficient power。[R1, R2 共识]\n\n**S5. 极为丰富的补充材料。** 18 个附录（A–Y）系统性地回应可预见审稿问题：cross-model validation, prompt sensitivity, confound analysis, ecological simulation, format independence, relaxed matching 等，显示极高实验完整度。[R1, R2 共识]\n\n**S6. 跨任务覆盖与 error taxonomy。** 跨 NER/RE/ED 三个核心 IE 任务、四个标准数据集。Error taxonomy decomposition (§4.4, Figure 2) 将 BCS 效应分解到具体错误类型（IntraSub, missed），提供 actionable 诊断信息。[R2]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定，4 项，R1+R2 共识）\n\n**C1. DocRED VIF=50.9 严重削弱 R²=58% 的可解释性** [R1-W1, R2 AGREE]\n- DocRED BCS-centrality collinearity VIF=50.9（Table 11），远超阈值 10。partial r=−0.344 的解释力远低于 full model R²=58%。读者无法区分 BCS 独立贡献与 centrality 混淆效应。\n- **要求**：报告 DocRED semipartial R²（BCS unique variance），或使用 ridge/LASSO 回归；在 §4.3 和 Abstract 中明确标注 VIF=50.9 的局限，将 DocRED 定位为 \"directionally consistent but confounded\"。\n- **R2 补充**：核心证据在 FewRel（VIF=1.18），DocRED 是 supporting evidence——问题真实但对核心 claim 的威胁低于表面上看到的程度（前提是作者修正措辞）。\n\n**C2. Confusability 发现仅在 FewRel RE 上稳健成立，generality claims 过度** [R1-W2, R2 AGREE with nuance]\n- 逐数据集审计：\n  - **FewRel RE**: ✓ 批次级 R²≈22%，跨模型一致（3 open-weight families）\n  - **NER (Few-NERD)**: ✗ 批次级 BCS null，3 模型均未检测到（Table 5）\n  - **DocRED**: △ VIF=50.9 使 BCS 独立贡献不可识别（C1）\n  - **MAVEN**: △ Per-type BCS-F1 正相关主要由 frequency/centrality confound 驱动（Appendix E）\n  - **Gemini Flash**: △ Leave-one-out sensitivity r: −0.80→−0.42, p=0.22（Appendix U）\n- **要求**：弱化 title/abstract/conclusion 中的跨任务 generality claims；明确 confusability 证据主要来自 FewRel RE。Count degradation（跨任务 robust）可保持 general framing。\n- **R2 nuance**：Abstract 已部分限定（\"In RE, BCS explains...\"），且 count degradation 确实跨任务稳健。论文未完全忽视此限制，但需进一步明确。\n\n**C3. NER null result 机制解释不充分** [R2-W2, R1 AGREE]\n- NER 对 BCS 无显著响应是论文最意外的发现之一，但机制解释停留在描述层面。论文同时持有两个未区分的假设：(a) NER 错误模式不同（miss/boundary/type 分散，而非集中于 type substitution）；(b) BCS range restriction（SD ratio 19%）导致 insufficient power（detectable r≈0.132 at 80% power, n=450）。两者有不同 practical implications，但论文未提供区分证据。\n- **要求**：在正文（非仅附录）明确承认 \"基于现有证据无法区分零效应与被噪声掩盖的效应\"；加入 power analysis 定量摘要（n=25 per condition, detectable effect=5.5pp, observed r≈−0.11）；标注 Gemini NER 未测试。\n- **R1 补充**：要求新实验超出 revision 范围；文字上的诚实表述即可。\n\n**C4. 贡献定位：BCS-controlled batch design 是标准分层实验设计** [R2-W1, R1 AGREE partially]\n- BCS-controlled batching 是经典 blocking/stratified experimental design，在统计学和实验心理学中已有数十年历史。论文 §1 将 \"the methodology—BCS-stratified batch construction with partial-correlation controls—is the contribution\" 作为首要贡献，过度抬高了实验设计技术本身的新颖性。\n- **要求**：将核心贡献从 \"methodology\" 重新定位为 \"empirical findings about confusability's independent predictive role, enabled by controlled design using SCS/BCS\"。\n- **R1 nuance**：领域特定的操作化（SCS 定义、greedy extreme-batch 算法、多数据集验证）有 applied methodology 价值。这是 framing 问题而非 substance 问题，不应构成 rejection 理由。\n\n### Should-Fix（影响评分但不一票否决，8 项）\n\n**W1. Error taxonomy / TOST / SDGD 均为 single-model** [R1-W4, R2-W4, 双方独立提出]\n- 这三项分析支撑重要 claim（confusability→type substitution; count×BCS interaction bounded; decomposition fails），但均仅在 Qwen3-32B 上验证。SDGD 的 merge amplification 可能是 Qwen3-32B 特定的 instruction-following 问题。\n- **建议**：至少在一个 alternative model 上复现 error taxonomy/TOST 核心结果；如资源不允许，在 Limitations 明确标注。\n\n**W2. 跨模型验证结果未整合入正文** [R2-W4, R1 AGREE]\n- 主实验全部基于 Qwen3-32B，cross-model 结果仅在 Appendix T/U。对声称 \"across three open-weight model families\" 的论文，核心 cross-model 结果应出现在正文。\n- **建议**：§4.1 和 §4.3 末尾各加 1-2 句 cross-model summary。\n\n**W3. Ecological amplification (1.3%→22%) 需更多 batch-level confound 控制** [R1-W3 Must-Fix, R2 REBUT → Director 降级为 Should-Fix]\n- Appendix N 的 Monte Carlo simulation 使用 conditional ρ=0.35（pairs sharing common type），非 marginal r≈0.112–0.167。论文已声明 simulation 是 illustrative，核心因果证据在 §4.3 controlled experiment。但 batch-level 回归未加入 domain diversity、type frequency 等额外控制变量。\n- **R2 反驳要点**：(1) ρ=0.35 来自条件子集合理；(2) simulation 是 illustrative 非 confirmatory；(3) Appendix O variance decomposition 部分回应了 confound 关切。\n- **Director 判断**：R2 的反驳有说服力（核心证据在 controlled experiment 而非 simulation），但 R1 关于 batch-level confound 的关切有效。降级为 Should-Fix。\n- **建议**：batch-level 回归中加入 batch-mean type frequency 和 domain diversity 控制变量，报告 R² 变化；正文明确 simulation 的 illustrative 定位。\n\n**W4. TOST ±3pp margin: logit-scale 不一致性** [R1-W5, R2 AGREE]\n- FewRel ~80% 准确率下 ±3pp 对应 ~15% 相对误差。Probability-scale TOST 通过（p=0.003），logit-scale inconclusive（p=0.209）。Back-transformed interaction at median=2.78pp 接近 boundary。Margin 缺乏 domain-specific justification。\n- **建议**：正文承认 logit-scale 不一致性；讨论 probability-scale 作为 primary metric 的理由；引用附录 sensitivity analysis。\n\n**W5. Abstract 信息密度过高** [R2-W5, R1 AGREE as minor]\n- ~150 词中 6+ 具体数字（\"0.72→~0.27\", \"85.7%→50.4%\", \"~22%\", \"~49pp\" 等），核心 takeaway 被数字流淹没。\n- **建议**：以定性 conceptual message 开头，保留 1-2 个最重要的数字。\n\n**W6. Discussion/Conclusion 过度压缩** [R2-W6, R1 AGREE]\n- Discussion + Conclusion 合并在 p.8 下半页约 25 行，practical implications（SCS 诊断工具、schema-aware pool selection）每个仅一句话。\n- **建议**：从 §2 (Related Work) 或 Limitations 挤出空间（~0.3 页）给 Discussion。\n\n**W7. Pairwise r²≈1.3% 实际意义未讨论** [R1-W7, R2 AGREE with nuance]\n- IQR-predicted gap 仅 2.2pp。论文未讨论在什么使用场景下 2.2pp 是 actionable 的。\n- **R2 nuance**：pair-level（1.3%）和 batch-level（22%）对应不同 practical scenario——pair-level 对应单个 type pair 混淆预测，batch-level 对应 prompt schema 设计。后者是 training-free IE 的典型 use case。\n- **建议**：Discussion 中区分两个 granularity 的 practical implications；讨论 SCS 阈值建议。\n\n**W8. \"First controlled study\" claim 需更精确限定** [R2-W7, R1 AGREE partially]\n- Chen et al. (2026) 以类似设计逻辑隔离 instance count + context length。Claim 技术上成立但易引发歧义。\n- **建议**：改为 \"first controlled study specifically isolating type confusability from type count using embedding-based batch-level controls in zero-shot LLM IE\"。\n\n---\n\n## Reviewer Consensus\n\n以下问题 R1、R2 达成共识：\n\n| 编号 | 问题 | 共识 |\n|------|------|------|\n| C1 | DocRED VIF=50.9 | [AGREE] 必须报告 semipartial R²，demote DocRED |\n| C2 | Confusability 仅 FewRel RE 稳健 | [AGREE] 弱化 generality claims |\n| C3 | NER null 机制不明 | [AGREE] 正文承认无法区分两假设 |\n| C4 | 贡献定位 methodology→findings | [AGREE] reframe 核心贡献 |\n| W1 | Single-model 二级分析 | [AGREE] 标注或补充验证 |\n| W2 | Cross-model 不在正文 | [AGREE] 加 summary |\n| W4 | TOST logit 不一致 | [AGREE] 正文讨论 |\n| W5 | Abstract 数字过多 | [AGREE] 简化 |\n| W6 | Discussion 压缩 | [AGREE] 扩展 |\n| W7 | 2.2pp 实际意义 | [AGREE] 讨论 practical threshold |\n| W8 | \"First\" claim | [AGREE] 更精确措辞 |\n\n## Reviewer Divergence\n\n| 编号 | R1 | R2 | Director 判断 |\n|------|-----|-----|-------------|\n| W3 (Ecological amplification) | Must-Fix: batch-level confounds 未控制 | REBUT: simulation 是 illustrative，核心证据在 §4.3 controlled experiment | **降级为 Should-Fix**。R2 反驳有说服力（因果证据在 controlled experiment 非 simulation），但 R1 的 batch-level confound 关切合理，应补充控制变量分析 |\n| Limitations 长度 | REBUT: 详尽是优势 | Should-Fix: EMNLP 不应过长 | **降级为 Minor**。6 条各有实质内容，略作压缩即可（合并 items 4+5） |\n| FewRel contamination | Should-Fix | REBUT: Appendix Q 已充分回应（方向相反 + BCS 效应不变） | **降级为 Minor**。论文已有力回应，正文加 1 句 summary 即可 |\n\n---\n\n## Questions to Authors\n\n**Q1** [R1+R2 共同关切]: BCS-controlled 实验中 high-BCS 和 low-BCS extreme batches 在 domain distribution 上是否有系统偏差？高 BCS batches 是否聚集在同一 Wikidata semantic domain？Appendix O 的 variance decomposition 未分析 domain-level。\n\n**Q2** [R2, R1 AGREE]: SDGD routing failure (Table 8) 在 oracle routing 下显著降低——是否意味着核心瓶颈是 routing quality 而非 decomposition strategy 本身？如果使用更强 routing model（GPT-4 级别），结论是否可能翻转？\n\n**Q3** [R2, R1 AGREE]: Few-NERD 的 66 types 嵌套在 8 coarse categories——BCS 是否考虑了层级结构？同 coarse category 内的 high-SCS pairs 与跨 category 的 high-SCS pairs 对性能的影响是否不同？这可能影响 NER null 的解读。\n\n**Q4** [R1]: DocRED full-model R²=58% 中 BCS 的 semipartial R²（unique variance after partialing centrality）是多少？如果远低于 58%，§4.3 的叙述应如何修正？\n\n**Q5** [R1]: NER batch-level null 在 Gemini Flash 上是否测试过？如果 Gemini 也是 null，则 task asymmetry 的跨架构 robustness 更强。\n\n**Q6** [R1]: Appendix N ecological simulation 的 ρ=0.35 是否代表 random batch 内平均 pair-level correlation？如果 random batch 的 within-batch ρ 远低于 0.35，simulated batch R² 会远低于 0.218。\n\n---\n\n## Missing References\n\n以下由两位 Reviewer 建议，经 Director 评估后保留：\n1. **Cohen (1988)** \"Statistical Power Analysis for the Behavioral Sciences\" — 论文使用 power analysis 和 TOST 但未引用此经典参考 [R1 建议, R2 同意]\n2. **Baan et al. (2023)** \"The Ecological Fallacy in Annotation\" (ACL 2023) — NLP 领域对 ecological fallacy 的直接讨论，与 §4.3 的 ecological correlation 主题直接相关 [R2 建议, R1 同意]\n\n以下需作者评估后决定：\n3. **ScrapeGraphAI-100k** (Cataldo et al., 2025) — web extraction 场景的 schema complexity 研究 [R2 建议, R1 认为 task setting 差异大]\n4. **Ding et al. (2024) \"GraphER\"** — schema-guided extraction [R1 建议, 需验证相关性]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 项目配置中未启用外部审稿（`external_review.paperreview_ai.enabled` 未找到配置项）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成** (2026-05-21 21:15→21:18, ~3 min)\n\n| 严重性 | 数量 | 关键发现 |\n|--------|------|----------|\n| Warning | 3 | 见下 |\n| Info | 6 | 见下 |\n\n**Warning findings:**\n1. **前 3 页无 display item**：审稿人打开论文前 3 页看不到视觉锚点。第一个 figure 直到 page 5 才出现。对于以实证为核心的 controlled study，建议将 Figure 1 关键 panel 提前到 page 2 或 Introduction 末尾。\n2. **主文仅 4 个 display items**（2 figure + 2 table），对于 4 数据集、多维度分析的实证论文偏少（经验值 5-8）。大量关键数据被推到 14 页附录（20+ 表格），主文读起来像文字摘要而非数据驱动论证。建议从附录提升 1-2 个关键表格到主文。\n3. **Page 8-9 连续 2 页纯文本**（§5 + §6 + Limitations），无 display item 穿插。§5 讨论 decomposition 效果可加对比表。\n\n**Info findings:**\n- Figure 1(b) 标注文字字号偏小，低缩放下难以阅读\n- Figure 2 中 IntraSub/ExtraSub 线条颜色接近，色盲不友好——建议辅以不同 line style/marker\n- 附录 14 页全部表格+文字，无 figure\n- Page 26 底部约 1/3 空白\n- Figure 1 caption 自包含性好（正面）\n- Table 1 使用 booktabs 风格，排版专业（正面）\n\n---\n\n## Overall Assessment\n\n### 评分\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| **Soundness** | 3.5/5 | 3.5/5 | **3.5/5** |\n| **Excitement** | 3/5 | 3/5 | **3/5** |\n| **Reproducibility** | 3/5 | 4/5 | **3.5/5** |\n\n### Overall: **3.5 (Borderline Conference)**\n\n**EMNLP 2026 ARR 评分标准**: 3.5 = Borderline Conference\n\n### 综合评语\n\n这是一篇研究问题重要、实验设计严谨、统计方法远超 NLP 平均水平的实证分析论文。SCS 作为 pre-hoc schema complexity proxy 有直接工程应用价值。18 个附录的覆盖面令人印象深刻。负面结果（NER null, SDGD failure）的诚实报告值得肯定。\n\n然而，四个 Must-Fix 问题限制了当前版本的接收：\n\n1. **DocRED R²=58% 因 VIF=50.9 不可信**——必须报告 semipartial R² 并降级 DocRED 在论文中的地位\n2. **Confusability 核心贡献实际仅在 FewRel RE 上稳健成立**——NER null + DocRED confounded + MAVEN frequency-driven + Gemini fragile，使得 title/abstract 的跨任务推广 claims 缺乏充分支撑\n3. **NER null 机制解释不充分**——论文同时持有零效应和 noise-masked 两个假设但未提供区分证据\n4. **贡献定位过高**——BCS-controlled batch design 是标准分层实验设计在新领域的应用，应重新定位为 empirical findings 而非 methodology contribution\n\n**修改路径**: 如果作者能 (a) 报告 DocRED semipartial R² 并修正措辞, (b) 将 generality claims 收窄到证据实际支撑的范围（FewRel RE for confusability, cross-task for count）, (c) 诚实承认 NER null 的 open status, (d) 将贡献重心从 methodology 转向 empirical findings——本文有潜力达到 Conference 接收水平。当前版本更接近 strong Findings 或 borderline Conference。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 信息密度过高：6+ 具体数字挤在 ~150 词中。核心 conceptual message（\"confusability independently predicts type substitution in RE\"）被数字淹没。\n- \"across NER, RE, and event detection\" 暗示三任务均有 confusability 证据，但 NER 为 null、ED 被 centrality confound。建议改为 \"with evidence primarily from RE\"。\n- 应加 \"ecological (batch-aggregate) level\" 修饰 R²≈22%。\n\n### §1 Introduction\n- Contribution 1 的 \"methodology is the contribution\" 定位需重新表述（C4）。\n- \"first controlled study\" 应更精确限定（W8）。\n- 四个 findings 的叙述清晰，RQ 设置自然。\n\n### §2 Related Work\n- \"SCS novelty\" 段落（p.3）明确了 metric vs methodology 区分——这个 positioning 应提前到 §1。\n- §2 有压缩空间（~0.2-0.3 页），可为 Discussion 让步。\n\n### §3 Experimental Setup\n- FewRel train+val 合并使用：Appendix Q 已回应（方向相反 + BCS 不受影响），正文可加 1 句 summary。\n- §3.2 SCS 定义处未指定默认 embedding model（MiniLM 在后文才提及）。\n\n### §4 Results\n- §4.1 Count Curves：跨模型验证结果（LLaMA-8B/70B, Gemini）应有 1-2 句 summary 而非仅引用 appendix。\n- §4.3 BCS-Controlled：DocRED R²=58% 需降级处理（C1）；ecological qualifier 应更突出。\n- §4.4 Multi-Dimensional Degradation：NER null 解释需在此处加入 power analysis summary（C3）。TOST logit 不一致性应正文提及（W4）。\n- §4.5 Centrality Confound：分析仅在 MAVEN 上成立，§3.2 的引用（\"centrality consistently yields equal or stronger correlations\"）应更精确。\n\n### §5 Schema Decomposition\n- 过度压缩（~1/3 页）。Oracle routing 成功（72.4% vs 50.4%）意味着 decomposition 是 routing-conditional failure，非绝对失败——措辞应调整。\n- 建议加 Table 7 或类似 summary 到正文。\n\n### §6 Discussion and Conclusion\n- ~25 行过度压缩。Practical implications（SCS 作为诊断、schema-aware pool selection）每个仅一句。\n- 未讨论 pair-level 2.2pp vs batch-level 22% 的 practical significance 差异（W7）。\n\n### Limitations\n- 内容充实且诚实。6 条 + 2 段技术上各有实质，但总体偏长。建议合并 items 4（causal mechanism）和 5（data contamination）。\n- \"Across-batch correlation\" 和 \"Multiple comparisons\" 两段可压缩或移至附录。\n\n### References / Format\n- 8 个 orphan bib entries（uncited）应清理：dee-2024, gillick-2014, novack-2023, schall-2025, tam-2024, volkanovska2025ner, wei-2023, zhou-2025-rethinking。\n- 正文 8 页（含 Limitations），格式合规。\n- 匿名性无问题（\"Anonymous ACL submission\"，无作者标识泄露）。\n- 缺少 Cohen (1988) 和 Baan et al. (2023) 引用。",
  "project": "schema-dag-extraction",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 25 (Fresh)\n\n**论文**: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n**Venue**: EMNLP 2026 (ACL Rolling Review, May 2026 cycle, Long Paper)\n**Deadline**: 2026-05-25\n**审稿模式**: Fresh (重新审稿，无上轮记忆)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量）\n\n---\n\n## Summary\n\n本文通过受控实验设计研究 training-free LLM 信息抽取中 schema 复杂度的两个维度——type count 和 type confusability——如何独立预测性能下降。使用 Schema Confusability Score (SCS) 和 Batch Confusability Score (BCS) 量化 confusability，在 Few-NERD (NER)、FewRel (RE)、DocRED (document-level RE)、MAVEN (ED) 上通过 count curve 和 BCS-controlled 实验验证。核心发现：(1) count 驱动 recall 下降（跨任务 robust），(2) confusability 驱动 type substitution（BCS 在 FewRel 解释 ~22% batch-level RE accuracy variance），(3) NER batch-level BCS 信号未检测到（task asymmetry），(4) Schema decomposition 因 merge amplification 和 routing failure 失败。\n\n---\n\n## Strengths\n\n**S1. 研究问题明确且实用。** 将 schema 复杂度分解为 count 和 confusability 两个独立维度是干净、有说服力的框架。SCS 作为无需运行抽取即可计算的 pre-hoc proxy，对 practitioners 有直接部署价值。\n\n**S2. FewRel BCS-controlled 实验设计严谨。** Within-pool 80-relation 比较有效控制 type frequency 混淆；2×2 factorial analysis 正式检验了 interaction boundedness；TOST 等价检验引入了 NLP 领域罕见的统计严谨性。[R1, R2 共识]\n\n**S3. 统计方法论远超同领域平均水平。** Bootstrap CIs、permutation tests、partial correlation (controlling degree centrality/type frequency)、TOST、power analysis for NER null——这种统计意识在 NLP 投稿中非常突出。[R1, R2 共识]\n\n**S4. 负面结果的诚实报告。** §5 完整报告 SDGD 失败及其原因分析（merge amplification, routing failure）。NER batch-level null 在 3 模型上确认并明确标注可能是 insufficient power。[R1, R2 共识]\n\n**S5. 极为丰富的补充材料。** 18 个附录（A–Y）系统性地回应可预见审稿问题：cross-model validation, prompt sensitivity, confound analysis, ecological simulation, format independence, relaxed matching 等，显示极高实验完整度。[R1, R2 共识]\n\n**S6. 跨任务覆盖与 error taxonomy。** 跨 NER/RE/ED 三个核心 IE 任务、四个标准数据集。Error taxonomy decomposition (§4.4, Figure 2) 将 BCS 效应分解到具体错误类型（IntraSub, missed），提供 actionable 诊断信息。[R2]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定，4 项，R1+R2 共识）\n\n**C1. DocRED VIF=50.9 严重削弱 R²=58% 的可解释性** [R1-W1, R2 AGREE]\n- DocRED BCS-centrality collinearity VIF=50.9（Table 11），远超阈值 10。partial r=−0.344 的解释力远低于 full model R²=58%。读者无法区分 BCS 独立贡献与 centrality 混淆效应。\n- **要求**：报告 DocRED semipartial R²（BCS unique variance），或使用 ridge/LASSO 回归；在 §4.3 和 Abstract 中明确标注 VIF=50.9 的局限，将 DocRED 定位为 \"directionally consistent but confounded\"。\n- **R2 补充**：核心证据在 FewRel（VIF=1.18），DocRED 是 supporting evidence——问题真实但对核心 claim 的威胁低于表面上看到的程度（前提是作者修正措辞）。\n\n**C2. Confusability 发现仅在 FewRel RE 上稳健成立，generality claims 过度** [R1-W2, R2 AGREE with nuance]\n- 逐数据集审计：\n  - **FewRel RE**: ✓ 批次级 R²≈22%，跨模型一致（3 open-weight families）\n  - **NER (Few-NERD)**: ✗ 批次级 BCS null，3 模型均未检测到（Table 5）\n  - **DocRED**: △ VIF=50.9 使 BCS 独立贡献不可识别（C1）\n  - **MAVEN**: △ Per-type BCS-F1 正相关主要由 frequency/centrality confound 驱动（Appendix E）\n  - **Gemini Flash**: △ Leave-one-out sensitivity r: −0.80→−0.42, p=0.22（Appendix U）\n- **要求**：弱化 title/abstract/conclusion 中的跨任务 generality claims；明确 confusability 证据主要来自 FewRel RE。Count degradation（跨任务 robust）可保持 general framing。\n- **R2 nuance**：Abstract 已部分限定（\"In RE, BCS explains...\"），且 count degradation 确实跨任务稳健。论文未完全忽视此限制，但需进一步明确。\n\n**C3. NER null result 机制解释不充分** [R2-W2, R1 AGREE]\n- NER 对 BCS 无显著响应是论文最意外的发现之一，但机制解释停留在描述层面。论文同时持有两个未区分的假设：(a) NER 错误模式不同（miss/boundary/type 分散，而非集中于 type substitution）；(b) BCS range restriction（SD ratio 19%）导致 insufficient power（detectable r≈0.132 at 80% power, n=450）。两者有不同 practical implications，但论文未提供区分证据。\n- **要求**：在正文（非仅附录）明确承认 \"基于现有证据无法区分零效应与被噪声掩盖的效应\"；加入 power analysis 定量摘要（n=25 per condition, detectable effect=5.5pp, observed r≈−0.11）；标注 Gemini NER 未测试。\n- **R1 补充**：要求新实验超出 revision 范围；文字上的诚实表述即可。\n\n**C4. 贡献定位：BCS-controlled batch design 是标准分层实验设计** [R2-W1, R1 AGREE partially]\n- BCS-controlled batching 是经典 blocking/stratified experimental design，在统计学和实验心理学中已有数十年历史。论文 §1 将 \"the methodology—BCS-stratified batch construction with partial-correlation controls—is the contribution\" 作为首要贡献，过度抬高了实验设计技术本身的新颖性。\n- **要求**：将核心贡献从 \"methodology\" 重新定位为 \"empirical findings about confusability's independent predictive role, enabled by controlled design using SCS/BCS\"。\n- **R1 nuance**：领域特定的操作化（SCS 定义、greedy extreme-batch 算法、多数据集验证）有 applied methodology 价值。这是 framing 问题而非 substance 问题，不应构成 rejection 理由。\n\n### Should-Fix（影响评分但不一票否决，8 项）\n\n**W1. Error taxonomy / TOST / SDGD 均为 single-model** [R1-W4, R2-W4, 双方独立提出]\n- 这三项分析支撑重要 claim（confusability→type substitution; count×BCS interaction bounded; decomposition fails），但均仅在 Qwen3-32B 上验证。SDGD 的 merge amplification 可能是 Qwen3-32B 特定的 instruction-following 问题。\n- **建议**：至少在一个 alternative model 上复现 error taxonomy/TOST 核心结果；如资源不允许，在 Limitations 明确标注。\n\n**W2. 跨模型验证结果未整合入正文** [R2-W4, R1 AGREE]\n- 主实验全部基于 Qwen3-32B，cross-model 结果仅在 Appendix T/U。对声称 \"across three open-weight model families\" 的论文，核心 cross-model 结果应出现在正文。\n- **建议**：§4.1 和 §4.3 末尾各加 1-2 句 cross-model summary。\n\n**W3. Ecological amplification (1.3%→22%) 需更多 batch-level confound 控制** [R1-W3 Must-Fix, R2 REBUT → Director 降级为 Should-Fix]\n- Appendix N 的 Monte Carlo simulation 使用 conditional ρ=0.35（pairs sharing common type），非 marginal r≈0.112–0.167。论文已声明 simulation 是 illustrative，核心因果证据在 §4.3 controlled experiment。但 batch-level 回归未加入 domain diversity、type frequency 等额外控制变量。\n- **R2 反驳要点**：(1) ρ=0.35 来自条件子集合理；(2) simulation 是 illustrative 非 confirmatory；(3) Appendix O variance decomposition 部分回应了 confound 关切。\n- **Director 判断**：R2 的反驳有说服力（核心证据在 controlled experiment 而非 simulation），但 R1 关于 batch-level confound 的关切有效。降级为 Should-Fix。\n- **建议**：batch-level 回归中加入 batch-mean type frequency 和 domain diversity 控制变量，报告 R² 变化；正文明确 simulation 的 illustrative 定位。\n\n**W4. TOST ±3pp margin: logit-scale 不一致性** [R1-W5, R2 AGREE]\n- FewRel ~80% 准确率下 ±3pp 对应 ~15% 相对误差。Probability-scale TOST 通过（p=0.003），logit-scale inconclusive（p=0.209）。Back-transformed interaction at median=2.78pp 接近 boundary。Margin 缺乏 domain-specific justification。\n- **建议**：正文承认 logit-scale 不一致性；讨论 probability-scale 作为 primary metric 的理由；引用附录 sensitivity analysis。\n\n**W5. Abstract 信息密度过高** [R2-W5, R1 AGREE as minor]\n- ~150 词中 6+ 具体数字（\"0.72→~0.27\", \"85.7%→50.4%\", \"~22%\", \"~49pp\" 等），核心 takeaway 被数字流淹没。\n- **建议**：以定性 conceptual message 开头，保留 1-2 个最重要的数字。\n\n**W6. Discussion/Conclusion 过度压缩** [R2-W6, R1 AGREE]\n- Discussion + Conclusion 合并在 p.8 下半页约 25 行，practical implications（SCS 诊断工具、schema-aware pool selection）每个仅一句话。\n- **建议**：从 §2 (Related Work) 或 Limitations 挤出空间（~0.3 页）给 Discussion。\n\n**W7. Pairwise r²≈1.3% 实际意义未讨论** [R1-W7, R2 AGREE with nuance]\n- IQR-predicted gap 仅 2.2pp。论文未讨论在什么使用场景下 2.2pp 是 actionable 的。\n- **R2 nuance**：pair-level（1.3%）和 batch-level（22%）对应不同 practical scenario——pair-level 对应单个 type pair 混淆预测，batch-level 对应 prompt schema 设计。后者是 training-free IE 的典型 use case。\n- **建议**：Discussion 中区分两个 granularity 的 practical implications；讨论 SCS 阈值建议。\n\n**W8. \"First controlled study\" claim 需更精确限定** [R2-W7, R1 AGREE partially]\n- Chen et al. (2026) 以类似设计逻辑隔离 instance count + context length。Claim 技术上成立但易引发歧义。\n- **建议**：改为 \"first controlled study specifically isolating type confusability from type count using embedding-based batch-level controls in zero-shot LLM IE\"。\n\n---\n\n## Reviewer Consensus\n\n以下问题 R1、R2 达成共识：\n\n| 编号 | 问题 | 共识 |\n|------|------|------|\n| C1 | DocRED VIF=50.9 | [AGREE] 必须报告 semipartial R²，demote DocRED |\n| C2 | Confusability 仅 FewRel RE 稳健 | [AGREE] 弱化 generality claims |\n| C3 | NER null 机制不明 | [AGREE] 正文承认无法区分两假设 |\n| C4 | 贡献定位 methodology→findings | [AGREE] reframe 核心贡献 |\n| W1 | Single-model 二级分析 | [AGREE] 标注或补充验证 |\n| W2 | Cross-model 不在正文 | [AGREE] 加 summary |\n| W4 | TOST logit 不一致 | [AGREE] 正文讨论 |\n| W5 | Abstract 数字过多 | [AGREE] 简化 |\n| W6 | Discussion 压缩 | [AGREE] 扩展 |\n| W7 | 2.2pp 实际意义 | [AGREE] 讨论 practical threshold |\n| W8 | \"First\" claim | [AGREE] 更精确措辞 |\n\n## Reviewer Divergence\n\n| 编号 | R1 | R2 | Director 判断 |\n|------|-----|-----|-------------|\n| W3 (Ecological amplification) | Must-Fix: batch-level confounds 未控制 | REBUT: simulation 是 illustrative，核心证据在 §4.3 controlled experiment | **降级为 Should-Fix**。R2 反驳有说服力（因果证据在 controlled experiment 非 simulation），但 R1 的 batch-level confound 关切合理，应补充控制变量分析 |\n| Limitations 长度 | REBUT: 详尽是优势 | Should-Fix: EMNLP 不应过长 | **降级为 Minor**。6 条各有实质内容，略作压缩即可（合并 items 4+5） |\n| FewRel contamination | Should-Fix | REBUT: Appendix Q 已充分回应（方向相反 + BCS 效应不变） | **降级为 Minor**。论文已有力回应，正文加 1 句 summary 即可 |\n\n---\n\n## Questions to Authors\n\n**Q1** [R1+R2 共同关切]: BCS-controlled 实验中 high-BCS 和 low-BCS extreme batches 在 domain distribution 上是否有系统偏差？高 BCS batches 是否聚集在同一 Wikidata semantic domain？Appendix O 的 variance decomposition 未分析 domain-level。\n\n**Q2** [R2, R1 AGREE]: SDGD routing failure (Table 8) 在 oracle routing 下显著降低——是否意味着核心瓶颈是 routing quality 而非 decomposition strategy 本身？如果使用更强 routing model（GPT-4 级别），结论是否可能翻转？\n\n**Q3** [R2, R1 AGREE]: Few-NERD 的 66 types 嵌套在 8 coarse categories——BCS 是否考虑了层级结构？同 coarse category 内的 high-SCS pairs 与跨 category 的 high-SCS pairs 对性能的影响是否不同？这可能影响 NER null 的解读。\n\n**Q4** [R1]: DocRED full-model R²=58% 中 BCS 的 semipartial R²（unique variance after partialing centrality）是多少？如果远低于 58%，§4.3 的叙述应如何修正？\n\n**Q5** [R1]: NER batch-level null 在 Gemini Flash 上是否测试过？如果 Gemini 也是 null，则 task asymmetry 的跨架构 robustness 更强。\n\n**Q6** [R1]: Appendix N ecological simulation 的 ρ=0.35 是否代表 random batch 内平均 pair-level correlation？如果 random batch 的 within-batch ρ 远低于 0.35，simulated batch R² 会远低于 0.218。\n\n---\n\n## Missing References\n\n以下由两位 Reviewer 建议，经 Director 评估后保留：\n1. **Cohen (1988)** \"Statistical Power Analysis for the Behavioral Sciences\" — 论文使用 power analysis 和 TOST 但未引用此经典参考 [R1 建议, R2 同意]\n2. **Baan et al. (2023)** \"The Ecological Fallacy in Annotation\" (ACL 2023) — NLP 领域对 ecological fallacy 的直接讨论，与 §4.3 的 ecological correlation 主题直接相关 [R2 建议, R1 同意]\n\n以下需作者评估后决定：\n3. **ScrapeGraphAI-100k** (Cataldo et al., 2025) — web extraction 场景的 schema complexity 研究 [R2 建议, R1 认为 task setting 差异大]\n4. **Ding et al. (2024) \"GraphER\"** — schema-guided extraction [R1 建议, 需验证相关性]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 项目配置中未启用外部审稿（`external_review.paperreview_ai.enabled` 未找到配置项）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成** (2026-05-21 21:15→21:18, ~3 min)\n\n| 严重性 | 数量 | 关键发现 |\n|--------|------|----------|\n| Warning | 3 | 见下 |\n| Info | 6 | 见下 |\n\n**Warning findings:**\n1. **前 3 页无 display item**：审稿人打开论文前 3 页看不到视觉锚点。第一个 figure 直到 page 5 才出现。对于以实证为核心的 controlled study，建议将 Figure 1 关键 panel 提前到 page 2 或 Introduction 末尾。\n2. **主文仅 4 个 display items**（2 figure + 2 table），对于 4 数据集、多维度分析的实证论文偏少（经验值 5-8）。大量关键数据被推到 14 页附录（20+ 表格），主文读起来像文字摘要而非数据驱动论证。建议从附录提升 1-2 个关键表格到主文。\n3. **Page 8-9 连续 2 页纯文本**（§5 + §6 + Limitations），无 display item 穿插。§5 讨论 decomposition 效果可加对比表。\n\n**Info findings:**\n- Figure 1(b) 标注文字字号偏小，低缩放下难以阅读\n- Figure 2 中 IntraSub/ExtraSub 线条颜色接近，色盲不友好——建议辅以不同 line style/marker\n- 附录 14 页全部表格+文字，无 figure\n- Page 26 底部约 1/3 空白\n- Figure 1 caption 自包含性好（正面）\n- Table 1 使用 booktabs 风格，排版专业（正面）\n\n---\n\n## Overall Assessment\n\n### 评分\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| **Soundness** | 3.5/5 | 3.5/5 | **3.5/5** |\n| **Excitement** | 3/5 | 3/5 | **3/5** |\n| **Reproducibility** | 3/5 | 4/5 | **3.5/5** |\n\n### Overall: **3.5 (Borderline Conference)**\n\n**EMNLP 2026 ARR 评分标准**: 3.5 = Borderline Conference\n\n### 综合评语\n\n这是一篇研究问题重要、实验设计严谨、统计方法远超 NLP 平均水平的实证分析论文。SCS 作为 pre-hoc schema complexity proxy 有直接工程应用价值。18 个附录的覆盖面令人印象深刻。负面结果（NER null, SDGD failure）的诚实报告值得肯定。\n\n然而，四个 Must-Fix 问题限制了当前版本的接收：\n\n1. **DocRED R²=58% 因 VIF=50.9 不可信**——必须报告 semipartial R² 并降级 DocRED 在论文中的地位\n2. **Confusability 核心贡献实际仅在 FewRel RE 上稳健成立**——NER null + DocRED confounded + MAVEN frequency-driven + Gemini fragile，使得 title/abstract 的跨任务推广 claims 缺乏充分支撑\n3. **NER null 机制解释不充分**——论文同时持有零效应和 noise-masked 两个假设但未提供区分证据\n4. **贡献定位过高**——BCS-controlled batch design 是标准分层实验设计在新领域的应用，应重新定位为 empirical findings 而非 methodology contribution\n\n**修改路径**: 如果作者能 (a) 报告 DocRED semipartial R² 并修正措辞, (b) 将 generality claims 收窄到证据实际支撑的范围（FewRel RE for confusability, cross-task for count）, (c) 诚实承认 NER null 的 open status, (d) 将贡献重心从 methodology 转向 empirical findings——本文有潜力达到 Conference 接收水平。当前版本更接近 strong Findings 或 borderline Conference。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 信息密度过高：6+ 具体数字挤在 ~150 词中。核心 conceptual message（\"confusability independently predicts type substitution in RE\"）被数字淹没。\n- \"across NER, RE, and event detection\" 暗示三任务均有 confusability 证据，但 NER 为 null、ED 被 centrality confound。建议改为 \"with evidence primarily from RE\"。\n- 应加 \"ecological (batch-aggregate) level\" 修饰 R²≈22%。\n\n### §1 Introduction\n- Contribution 1 的 \"methodology is the contribution\" 定位需重新表述（C4）。\n- \"first controlled study\" 应更精确限定（W8）。\n- 四个 findings 的叙述清晰，RQ 设置自然。\n\n### §2 Related Work\n- \"SCS novelty\" 段落（p.3）明确了 metric vs methodology 区分——这个 positioning 应提前到 §1。\n- §2 有压缩空间（~0.2-0.3 页），可为 Discussion 让步。\n\n### §3 Experimental Setup\n- FewRel train+val 合并使用：Appendix Q 已回应（方向相反 + BCS 不受影响），正文可加 1 句 summary。\n- §3.2 SCS 定义处未指定默认 embedding model（MiniLM 在后文才提及）。\n\n### §4 Results\n- §4.1 Count Curves：跨模型验证结果（LLaMA-8B/70B, Gemini）应有 1-2 句 summary 而非仅引用 appendix。\n- §4.3 BCS-Controlled：DocRED R²=58% 需降级处理（C1）；ecological qualifier 应更突出。\n- §4.4 Multi-Dimensional Degradation：NER null 解释需在此处加入 power analysis summary（C3）。TOST logit 不一致性应正文提及（W4）。\n- §4.5 Centrality Confound：分析仅在 MAVEN 上成立，§3.2 的引用（\"centrality consistently yields equal or stronger correlations\"）应更精确。\n\n### §5 Schema Decomposition\n- 过度压缩（~1/3 页）。Oracle routing 成功（72.4% vs 50.4%）意味着 decomposition 是 routing-conditional failure，非绝对失败——措辞应调整。\n- 建议加 Table 7 或类似 summary 到正文。\n\n### §6 Discussion and Conclusion\n- ~25 行过度压缩。Practical implications（SCS 作为诊断、schema-aware pool selection）每个仅一句。\n- 未讨论 pair-level 2.2pp vs batch-level 22% 的 practical significance 差异（W7）。\n\n### Limitations\n- 内容充实且诚实。6 条 + 2 段技术上各有实质，但总体偏长。建议合并 items 4（causal mechanism）和 5（data contamination）。\n- \"Across-batch correlation\" 和 \"Multiple comparisons\" 两段可压缩或移至附录。\n\n### References / Format\n- 8 个 orphan bib entries（uncited）应清理：dee-2024, gillick-2014, novack-2023, schall-2025, tam-2024, volkanovska2025ner, wei-2023, zhou-2025-rethinking。\n- 正文 8 页（含 Limitations），格式合规。\n- 匿名性无问题（\"Anonymous ACL submission\"，无作者标识泄露）。\n- 缺少 Cohen (1988) 和 Baan et al. (2023) 引用。",
    "project": "schema-dag-extraction",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
  }
}
```

</details>

---


### Tool result

_source line 2815 · 2026-05-21T21:25:50.033149+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_51326259fe46fbae9da26b81cf03f1f8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4421
}
```

</details>

---


### Assistant

_source line 2816 · 2026-05-21T21:25:58.940016+00:00_

审稿报告已投递至 Research Director。

**Round 25 (Fresh) 审稿完成汇报：**

**Overall: 3.5 (Borderline Conference)**  — R1、R2 评分一致

**4 个 Must-Fix：**
1. DocRED VIF=50.9 → 必须报告 semipartial R²，降级 DocRED 地位
2. Confusability 证据仅 FewRel RE 稳健 → 收窄 generality claims
3. NER null 机制不明 → 正文承认无法区分零效应与 noise-masked
4. 贡献定位过高 → methodology → empirical findings

**8 个 Should-Fix** + **3 个 Minor** + **6 个 Questions to Authors**

**修改路径**：如果 4 个 Must-Fix 得到解决（DocRED semipartial R²、收窄 scope claims、NER null 诚实表述、贡献 reframe），本文有潜力达到 Conference 接收水平。

Issue Tracker 已同步更新至 `artifacts/review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 234

## Round 234

2 recorded events


### User

_source line 2817 · 2026-05-21T21:26:01.534384+00:00_

[Reviewer 1 审稿结果]:
已完成对 Reviewer 2 全部 W1-W7 和 Q1-Q3 的逐条交叉回应，已提交给 Review Director。

核心判断：
- **7 同意（含 3 个部分同意）、1 反驳**：R2-W3（Limitations 过长）是唯一明确反驳项，理由是详尽的 Limitations 对实证分析论文是加分项而非扣分项
- **最有价值的新发现**：R2-Q2（SDGD 的 routing vs decomposition 因果归因存在矛盾）和 R2-Q3（Few-NERD 层级结构可能解释 NER null），这两点补充了我 Round 1 未覆盖的角度
- **与我 Round 1 的一致性**：R2-W2/W4 与我的 W2/W4 高度重合；R2-Q1 与我的 Q2 一致

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2818 · 2026-05-21T21:26:15.371119+00:00_

审稿报告已投递至 Research Director。

**Round 25 (Fresh) 审稿完成摘要：**

**Overall: 3.5 (Borderline Conference)** — R1、R2 一致

**4 项 Must-Fix（共识）：**
1. DocRED VIF=50.9 → 必须报告 semipartial R²，降级 DocRED 地位
2. Confusability 仅 FewRel RE 稳健 → 弱化跨任务 generality claims
3. NER null 机制解释不充分 → 正文承认两假设不可区分
4. 贡献定位过高 → methodology → empirical findings

**8 项 Should-Fix + 3 项 Minor** 已记录在 Issue Tracker (`review_issues.yaml`)。

**1 项分歧**：Ecological amplification（R1=Must-Fix, R2=REBUT）→ Director 降级为 Should-Fix。

**修改路径**：修正上述 4 项 + 收窄 generality claims + 扩展 Discussion → 有潜力达到 Conference 水平。当前版本更接近 strong Findings / borderline Conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 235

## Round 235

2 recorded events


### User

_source line 2819 · 2026-05-21T22:57:47.189891+00:00_

[RESET REQUEST] Research Reviewer 达到硬限
  触发原因：运行时长 16h24m
  本轮累计 23 条消息 / 16h 24min

⚠️ 你自己的 context 状态：已 23 条消息 / 16h 24min

请回复：
  [RESET AGENT]     只重置 Research Reviewer，你继续
  [RESET BOTH]      顺便也重置你自己（推荐，如果本轮讨论已收敛）
  [DEFER Xm]        Xm 后再说
  [DENY <原因>]     不重置，让 Research Reviewer 继续带着上下文工作

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 2820 · 2026-05-21T22:57:57.769231+00:00_

审稿报告已提交完毕，圆桌会议全部流程已结束。无需保留 Reviewer context。

[RESET BOTH]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 236

## Round 236

2 recorded events


### User

_source line 2821 · 2026-05-21T23:01:31.775566+00:00_

[SYSTEM] Research Reviewer 刚完成 context rotation (Loop 13)，已读取 handoff 并就绪。如有待办任务请立即分配。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 2822 · 2026-05-21T23:01:47.459247+00:00_

审稿报告已在上一轮完成并投递给 Research Director。无待办任务需要分配给 Research Reviewer。

**本轮审稿已完成，摘要：**

- **Overall**: 3.5 (Borderline Conference)
- **4 个 Must-Fix**: DocRED VIF=50.9、confusability 仅 FewRel RE 稳健、NER null 机制不明、贡献定位过高
- **8 个 Should-Fix**: single-model 二级分析、cross-model 不在正文、ecological confound 控制、TOST margin、Abstract 密度、Discussion 压缩、2.2pp 实际意义、"first" claim 措辞
- **Issue Tracker**: 已同步更新至 `review_issues.yaml` (Round 25)
- **报告**: 已通过 `submit_review_report_to_research_director` 投递

[RESET BOTH] — 本轮讨论已完全收敛（两位 Reviewer 评分一致、交叉回应完成、报告已投递），建议同时重置 Review Director 和 Research Reviewer。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 237

## Round 237

38 recorded events


### User

_source line 2823 · 2026-05-22T02:02:12.702535+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: schema-dag-extraction
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2025 cycle (Main + Findings unified)
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2824 · 2026-05-22T02:02:20.011324+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2825 · 2026-05-22T02:02:20.062387+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2826 · 2026-05-22T02:02:26.239322+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 2827 · 2026-05-22T02:02:26.289937+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2828 · 2026-05-22T02:02:30.607633+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 2829 · 2026-05-22T02:02:31.964683+00:00_

{"result":"# 项目 schema-dag-extraction 概况\n\n## 实验状态 (69 个)\n\n- **exp012_llama_8b_r2_exp2**: DONE (negative) — \n- **exp012_llama_8b_r2**: DONE (success) — \n- **exp006_interaction_2x2**: DONE (negative) — \n- **exp012_llama_awq**: DONE (killed) — \n- **exp012_llama_8b_r3**: DONE (failed) — \n- **exp012_llama_8b**: DONE (killed) — \n- **exp_fewrel_40rel_r3**: DONE (failed) — \n- **exp_fewrel_40rel_r2**: DONE (failed) — \n- **exp012_llama_fewnerd_r4**: DONE (failed) — \n- **exp012_llama_8b_fewnerd**: DONE (failed) — \n- **exp_fewrel_40rel**: DONE (failed) — \n- **exp012_llama_fewnerd_r3**: DONE (failed) — \n- **exp012_llama_fewnerd_r2**: DONE (failed) — \n- **exp012_llama_fewnerd**: DONE (failed) — \n- **exp008_sdgd_zero_fewnerd**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- prompt_sensitivity（准备中）\n- prompt_sensitivity_dry4（准备中）\n- prompt_sensitivity_dry3（准备中）\n- prompt_sensitivity_dry2（准备中）\n- prompt_sensitivity_dry（准备中）\n- exp_aggregation_monte_carlo（准备中）\n- exp_scs_name_def_ablation（准备中）\n- exp_fewrel_contamination_check（准备中）\n- exp017_gpt4o_mini_fewrel（准备中）\n- exp_cross_embedding_sensitivity（准备中）\n- …另有 2 项\n\n## 近期结论\n- **exp_llama70b_ner_bcs_null** (success): Batch-level BCS does not correlate with NER F1 for LLaMA-3.1-70B-FP8, consistent with the BCS null observed in Qwen3-32B (r=0.004) and LLaMA-8B (r=-0.12). The confusability metric is not predictive of extraction quality at the batch level. ← 基于 exp012_llama_8b_r2_exp2\n  [LLaMA-70B NER BCS-null analysis](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_llama70b_ner_bcs_null/data/bcs_null_analysis.json)\n- **exp_gemini_flash_bcs_controlled** (success): BCS-accuracy negative correlation observed on open-weight models (Qwen3-32B, LLaMA) generalizes to proprietary API models. Gemini 2.5 Flash should show significant BCS gap on extreme-BCS batches at count 8 and count 16, confirming Dimension 2 is architecture-family-in
…[truncated 1221 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1357
}
```

</details>

---


### Tool call

_source line 2830 · 2026-05-22T02:02:32.517471+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2831 · 2026-05-22T02:02:33.371946+00:00_

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
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	\usepackage{listings}
16	
17	\title{How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	
28	\input{related_work}
29	
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	\begin{enumerate}[leftmargin=*,itemsep=2pt]
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B; cross-model validation (LLaMA-8B, LLaMA-70B, Gemini Flash) covers Dimensions~1--2 (count curves, BCS-controlled extremes) but does not replicate secondary analyses (error taxonomy, prompt sensitivity, TOST equivalence). Specifically, TOST factorial interaction (\S\ref{sec:multi_channel}) and SDGD failure analysis (\S\ref{sec:sdgd}) are established on Qwen3-32B alone; error taxonomy replicates on two additional models (Table~\ref{tab:cross_model_error_taxonomy}), but TOST and SDGD cross-model replication remains the most pressing extension. Gemini provides only partial, leverage-sensitive corroboration (leave-one-out $r{:}\;{-}0.80 \to {-}0.42$; Appendix~\ref{sec:appendix_cross_model_gemini}); proprietary-model generalization remains open.
41	
42	\item \textbf{Effect size and statistical design.} Pairwise SCS explains a small fraction of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\times$ BCS interaction is bounded on FewRel but nonzero on DocRED, partially confounded by BCS range restriction at higher counts (Appendix~\ref{sec:appendix_factoria
…[truncated 5422 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 2832 · 2026-05-22T02:02:33.422649+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 2833 · 2026-05-22T02:02:33.423134+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2834 · 2026-05-22T02:02:41.863277+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2835 · 2026-05-22T02:02:41.863750+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2836 · 2026-05-22T02:02:43.590676+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/main.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/main.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 2837 · 2026-05-22T02:02:43.641422+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/paper/main.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2838 · 2026-05-22T02:02:48.720431+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2025 2026 submission guidelines page limit author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2025 2026 submission guidelines page limit author instructions"
  }
}
```

</details>

---


### Tool call

_source line 2839 · 2026-05-22T02:02:49.424086+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 2840 · 2026-05-22T02:02:59.717428+00:00_

Web search results for query: "ACL Rolling Review ARR 2025 2026 submission guidelines page limit author instructions"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Instructions for *ACL Proceedings","url":"https://arxiv.org/html/2506.06751v2"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's the key information about ACL Rolling Review (ARR) submission guidelines for 2025-2026:

## Formatting Requirements

All long, short, and theme papers must follow the ACL Author Guidelines. Paper submissions must use the official ACL style template.

## Page Limits

While the search results reference that paper
…[truncated 1448 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 10996
}
```

</details>

---


### Tool result

_source line 2841 · 2026-05-22T02:02:59.769176+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/decisions.yaml\", \"content\": \"_next_id: 72\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 16:10 UTC\\n  summary: 项目立项，MVP 验证方案：Experiment 2 (Confusability Controlled) 为核心验证实验\\n  rationale: 'IDEA_BRIEF 的核心假设是 type confusability 独立于 type count 驱动 LLM IE 质量下降。Experiment\\n    2（固定 count 变 BCS）是最直接的假设检验。Pass 标准: |r|≥0.3 且 p<0.05。ACE05 RE + Few-NERD 双数据集验证。ARR\\n    May 25 DDL（11天），MVP 需 1-2 天完成。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 16:15 UTC\\n  summary: 修正 MVP 统计设计：random samples 从 10 增至 25/档，加入 per-type solo baseline 控制变量，核心指标改为\\n    Δ(solo_F1 - batch_F1)\\n  rationale: Reviewer 指出 n=12 下 |r|=0.3 对应 p≈0.34，无法同时满足 |r|≥0.3 且 p<0.05。增至 25 random\\n    batches/档 → n≈54，|r|≥0.27 即可达 p<0.05。同时加入 solo F1 控制 type 固有难度，避免将\\\"类型本身难抽取\\\"误归因于\\\"confusability\\n    效应\\\"。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 23:11 UTC\\n  summary: MVP 分析方法从 Δ(solo-batch) 切换到 within-count Pearson r(F1, BCS)，pass 标准更新为\\n    |r|≥0.3 at fixed count\\n  rationale: Exp 1 发现 count curve 方向反转（F1 随 count 上升），根因是低 count 时模型过度 hallucinate（pred/gold=8x\\n    at count=1）。solo baseline 处于极端行为模式，Δ 被跨 count 行为差异污染。改为 within-count 对比更干净：同一\\n    count 下比较不同 BCS 的 F1，直接检验 confusability 独立效应。\\n  related_experiments:\\n  - exp_id: exp001_count_baseline\\n    role: evidence\\n    result: count curve reversed, hallucination at low count\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 23:31 UTC\\n  summary: MVP 主指标更新为 within-count r(recall, BCS)，F1 因 over-prediction confound 降为补充指标\\n  rationale: Exp 1 text-match 重评估发现：recall 单调下降（0.72→0.42，符合预期），precision 单调上升（0.11→0.52，over-prediction\\n    减少），F1 受 precision 主导而反转。within-count 分析中 precision confound 在同一 count 下近似恒定，F1\\n    仍可用；但 recall 更干净且直接反映 type confusion。WrongType 错误（text 正确但 type 错标）随 count 从 0\\n    升至 2434，直
…[truncated 1449 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 10345
}
```

</details>

---


### Tool call

_source line 2842 · 2026-05-22T02:03:05.803009+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline ARR commitment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline ARR commitment"
  }
}
```

</details>

---


### Tool call

_source line 2843 · 2026-05-22T02:03:06.154985+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2844 · 2026-05-22T02:03:06.255795+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 2845 · 2026-05-22T02:03:12.936317+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline ARR commitment"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 2026 Deadlines — Submission, Rebuttal & Dates | Paperpin | Paperpin","url":"https://www.getpaperpin.com/deadlines/emnlp26"}]

Based on the search results, here's the key information about EMNLP 2026 call for papers, submission deadline, and ARR commitment:

## Submission Deadline

The ARR submission deadl
…[truncated 933 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 7133
}
```

</details>

---


### Tool call

_source line 2846 · 2026-05-22T02:03:16.917668+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 page limits long paper short paper formatting requirements template",
  "allowed_domains": "['aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 page limits long paper short paper formatting requirements template",
    "allowed_domains": "['aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 2847 · 2026-05-22T02:03:17.119392+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read_local_file project",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "read_local_file project",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 2848 · 2026-05-22T02:03:17.170159+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2849 · 2026-05-22T02:03:23.954645+00:00_

Web search results for query: "ACL Rolling Review 2026 page limits long paper short paper formatting requirements template"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Changelog – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/changelog"}]

Based on the search results, here is the information about ACL Rolling Review 2026 formatting requirements:

## Page Limits

Short papers: 4 content pages maximum, Long papers: 8 content pages maximum.

## Sections That Don't Count Toward Page Limits

Sections on ethical considerations and limitations do not count towards page limit. Authors are required to discuss the limitations of their work in a dedicated section titled "Limitations". This section should be included at the end of the paper, before the references, and it will not count toward the page limit.

## Formatting Requirements

The paper should be properly formatted according to the ACL guidelines. ACL has separate LaTeX and Microsoft Word templates, and PDFs produced by these templates look different from each other.

## Official Template

There is an off
…[truncated 520 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 7036
}
```

</details>

---


### Tool call

_source line 2850 · 2026-05-22T02:03:30.444410+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "output_mode": "content",
  "-C": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
    "output_mode": "content",
    "-C": "3"
  }
}
```

</details>

---


### Tool call

_source line 2851 · 2026-05-22T02:03:31.049460+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*config*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*config*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 2852 · 2026-05-22T02:03:31.100391+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_fix_exp006_batch_config_20260515T174929.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_fix_exp006_batch_config_20260515T174929_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/pip/_internal/commands/configuration.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/pip/_internal/configuration.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/pip/_internal/locations/_sysconfig.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/pip/_internal/commands/__pycache__/configuration.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/pip/_internal/__pycache__/configuration.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/pip/_internal/locations/__pycache__/_sysconfig.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/numpy/__config__.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/numpy/__config__.pyi
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/numpy/_configtool.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/numpy/_configtool.pyi
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/numpy/_core/_ufunc_config.py
/home/ubuntu/.agent-ml-research-i
…[truncated 14064 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2853 · 2026-05-22T02:03:31.101470+00:00_

&lt;persisted-output>
Output too large (41.2KB). Full output saved to: /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-director-338aa0a5/651145ba-9294-4ea8-a106-4e85546b307d/tool-results/toolu_01S9D1ebAET4o9cb6J5knAjE.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_14.md-156-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_14.md-157-## External Review (Stanford Agentic Reviewer)
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_14.md-158-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_14.md:159:外部审稿：未请求（项目配置未启用 `external_review.paperreview_ai.enabled`）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_14.md-160-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_14.md-161----
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_14.md-162-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_18.md-130-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_18.md-131-## External Review (Stanford Agentic Reviewer)
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_18.md-132-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_18.md:133:外部审稿：未配置（项目 `external_review.paperreview_ai.enabled` 未设置）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_r
…[truncated 297 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "elapsed_ms": 657
}
```

</details>

---


### Tool call

_source line 2854 · 2026-05-22T02:03:59.625939+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "schema-dag-extraction",
  "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "schema-dag-extraction",
    "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
  }
}
```

</details>

---


### Tool result

_source line 2855 · 2026-05-22T02:04:16.948037+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 17322
}
```

</details>

---


### Tool call

_source line 2856 · 2026-05-22T02:04:17.902682+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "text": "你是 Reviewer 1，负责审查本文的**方法严谨性、实验设计和统计分析**。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR May 2026 cycle 提交）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper, 正文 8 页，参考文献无限制，Limitations 不计入页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（禁止出现作者信息或可识别自引）\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n1. **实验设计的严谨性**：\n   - 控制变量是否合理？是否有混淆因素未被处理？\n   - 样本量是否足够支撑声称的统计结论？\n   - Batch 构造方式是否引入 sampling bias？\n\n2. **统计方法**：\n   - 相关系数的使用是否恰当（Pearson vs Spearman）？\n   - 多重比较校正是否充分？\n   - 置信区间/p-value 的报告是否规范？\n   - TOST 等价检验的设计是否合理（margin 选择、power）？\n\n3. **Claims vs Evidence 对齐**：\n   - 每个核心 claim 是否有充分的实验证据支撑？\n   - 是否存在 overclaiming（结论超出数据支持范围）？\n   - 因果推断 vs 相关性的区分是否清晰？\n\n4. **跨模型验证**：\n   - 主实验在 Qwen3-32B 上进行，跨模型验证（LLaMA-8B/70B, Gemini Flash）的覆盖是否足够？\n   - 部分结果仅在单模型上验证，是否影响 generalizability 声称？\n\n5. **格式合规**：\n   - 正文是否超过 8 页？\n   - 是否存在 double-blind 违规？\n   - Limitations 章节是否存在且合理？\n\n请按以下格式输出审稿意见：\n```\n## Summary（2-3句）\n## Strengths（逐条）\n## Weaknesses（逐条，标注 severity: Critical/Major/Minor）\n## Questions（需要作者回答的问题）\n## Missing References（如有）\n## Overall Assessment（评分 + 理由）\n```\n\n评分参考（EMNLP 2026 ARR 标准）：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit。",
  "reviewer_id": "1",
  "project": "schema-dag-extraction",
  "round_number": "1"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 1，负责审查本文的**方法严谨性、实验设计和统计分析**。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR May 2026 cycle 提交）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper, 正文 8 页，参考文献无限制，Limitations 不计入页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（禁止出现作者信息或可识别自引）\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n1. **实验设计的严谨性**：\n   - 控制变量是否合理？是否有混淆因素未被处理？\n   - 样本量是否足够支撑声称的统计结论？\n   - Batch 构造方式是否引入 sampling bias？\n\n2. **统计方法**：\n   - 相关系数的使用是否恰当（Pearson vs Spearman）？\n   - 多重比较校正是否充分？\n   - 置信区间/p-value 的报告是否规范？\n   - TOST 等价检验的设计是否合理（margin 选择、power）？\n\n3. **Claims vs Evidence 对齐**：\n   - 每个核心 claim 是否有充分的实验证据支撑？\n   - 是否存在 overclaiming（结论超出数据支持范围）？\n   - 因果推断 vs 相关性的区分是否清晰？\n\n4. **跨模型验证**：\n   - 主实验在 Qwen3-32B 上进行，跨模型验证（LLaMA-8B/70B, Gemini Flash）的覆盖是否足够？\n   - 部分结果仅在单模型上验证，是否影响 generalizability 声称？\n\n5. **格式合规**：\n   - 正文是否超过 8 页？\n   - 是否存在 double-blind 违规？\n   - Limitations 章节是否存在且合理？\n\n请按以下格式输出审稿意见：\n```\n## Summary（2-3句）\n## Strengths（逐条）\n## Weaknesses（逐条，标注 severity: Critical/Major/Minor）\n## Questions（需要作者回答的问题）\n## Missing References（如有）\n## Overall Assessment（评分 + 理由）\n```\n\n评分参考（EMNLP 2026 ARR 标准）：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit。",
    "reviewer_id": "1",
    "project": "schema-dag-extraction",
    "round_number": "1"
  }
}
````

</details>

---


### Tool result

_source line 2857 · 2026-05-22T02:04:29.874927+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 11972
}
```

</details>

---


### Tool call

_source line 2858 · 2026-05-22T02:04:30.278052+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "text": "你是 Reviewer 2，负责审查本文的**新颖性、Related Work 完整性和写作质量**。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR May 2026 cycle 提交）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper, 正文 8 页，参考文献无限制，Limitations 不计入页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（禁止出现作者信息或可识别自引）\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n1. **新颖性与贡献**：\n   - 核心 idea（schema complexity 的两维度分解：count + confusability）是否有足够新颖性？\n   - 与已有 schema/ontology complexity 研究相比，增量贡献是什么？\n   - BCS (Batch Confusability Score) 作为新指标是否有独立价值？\n   - SDGD 负面结果的价值和呈现方式\n\n2. **Related Work 完整性**：\n   - 是否遗漏了重要相关工作（特别是 LLM-based IE、schema complexity、type confusion、few-shot IE 等方向）？\n   - 与现有工作的对比/定位是否准确？\n   - 引用是否真实（不是幻觉引用）？\n\n3. **写作质量**：\n   - 论文结构是否清晰？叙事逻辑是否连贯？\n   - 术语使用是否一致？\n   - 图表是否高质量且有信息密度？\n   - Abstract/Introduction 是否准确反映了贡献？\n\n4. **Presentation 与 Reproducibility**：\n   - 方法描述是否足够详细以供复现？\n   - 超参数、prompt 模板等是否公开？\n   - 数据集处理细节是否充分？\n\n5. **格式合规**（辅助检查）：\n   - 匿名性（无作者信息、无可识别自引）\n   - 引用格式是否统一规范\n\n请按以下格式输出审稿意见：\n```\n## Summary（2-3句）\n## Strengths（逐条）\n## Weaknesses（逐条，标注 severity: Critical/Major/Minor）\n## Questions（需要作者回答的问题）\n## Missing References（如有）\n## Overall Assessment（评分 + 理由）\n```\n\n评分参考（EMNLP 2026 ARR 标准）：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit。",
  "reviewer_id": "2",
  "project": "schema-dag-extraction",
  "round_number": "1"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 2，负责审查本文的**新颖性、Related Work 完整性和写作质量**。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR May 2026 cycle 提交）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper, 正文 8 页，参考文献无限制，Limitations 不计入页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（禁止出现作者信息或可识别自引）\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n1. **新颖性与贡献**：\n   - 核心 idea（schema complexity 的两维度分解：count + confusability）是否有足够新颖性？\n   - 与已有 schema/ontology complexity 研究相比，增量贡献是什么？\n   - BCS (Batch Confusability Score) 作为新指标是否有独立价值？\n   - SDGD 负面结果的价值和呈现方式\n\n2. **Related Work 完整性**：\n   - 是否遗漏了重要相关工作（特别是 LLM-based IE、schema complexity、type confusion、few-shot IE 等方向）？\n   - 与现有工作的对比/定位是否准确？\n   - 引用是否真实（不是幻觉引用）？\n\n3. **写作质量**：\n   - 论文结构是否清晰？叙事逻辑是否连贯？\n   - 术语使用是否一致？\n   - 图表是否高质量且有信息密度？\n   - Abstract/Introduction 是否准确反映了贡献？\n\n4. **Presentation 与 Reproducibility**：\n   - 方法描述是否足够详细以供复现？\n   - 超参数、prompt 模板等是否公开？\n   - 数据集处理细节是否充分？\n\n5. **格式合规**（辅助检查）：\n   - 匿名性（无作者信息、无可识别自引）\n   - 引用格式是否统一规范\n\n请按以下格式输出审稿意见：\n```\n## Summary（2-3句）\n## Strengths（逐条）\n## Weaknesses（逐条，标注 severity: Critical/Major/Minor）\n## Questions（需要作者回答的问题）\n## Missing References（如有）\n## Overall Assessment（评分 + 理由）\n```\n\n评分参考（EMNLP 2026 ARR 标准）：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit。",
    "reviewer_id": "2",
    "project": "schema-dag-extraction",
    "round_number": "1"
  }
}
````

</details>

---


### Tool result

_source line 2859 · 2026-05-22T02:04:32.323192+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 2045
}
```

</details>

---


### Assistant

_source line 2860 · 2026-05-22T02:04:48.401791+00:00_

Round 1 已启动：

| 角色 | 状态 | 侧重 |
|------|------|------|
| Reviewer 1 | 已派发 | 方法严谨性 + 实验设计 + 统计分析 |
| Reviewer 2 | 已派发 | 新颖性 + Related Work + 写作质量 |
| Visual Check Agent | 已启动 | 排版/图表/布局（非评分项） |
| External Review | 跳过 | 项目未配置 |

等待两位 Reviewer 返回初审意见后，进入 Step 2（交叉分享 + 逐条回应）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 238

## Round 238

2 recorded events


### User

_source line 2861 · 2026-05-22T02:07:58.088191+00:00_

[Reviewer 2 审稿结果]:
搜索更多可能遗漏的相关工作方向。

---

[Reviewer 1 审稿结果]:
已读完正文（1-10 页），现在读取附录部分（11-26 页），这些包含补充实验和统计细节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2862 · 2026-05-22T02:08:12.157984+00:00_

两位 Reviewer 均在审稿中：

- **Reviewer 1**：正文已读完，正在读附录（pp.11-26）
- **Reviewer 2**：正在补充搜索可能遗漏的 related work

等待两位完成 Round 1 初审后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 239

## Round 239

64 recorded events


### User

_source line 2863 · 2026-05-22T04:12:18.413504+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: schema-dag-extraction
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2025 cycle (Main + Findings unified)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2864 · 2026-05-22T04:12:30.951758+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2865 · 2026-05-22T04:12:31.053159+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2866 · 2026-05-22T04:12:44.769054+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,read_project_file,request_external_review,submit_review_report_to_research_director,update_review_issues,WebSearch",
  "max_results": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,read_project_file,request_external_review,submit_review_report_to_research_director,update_review_issues,WebSearch",
    "max_results": "15"
  }
}
```

</details>

---


### Tool result

_source line 2867 · 2026-05-22T04:12:44.869997+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2868 · 2026-05-22T04:12:47.431713+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,read_project_file,request_external_review,submit_review_report_to_research_director,update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,read_project_file,request_external_review,submit_review_report_to_research_director,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2869 · 2026-05-22T04:12:47.482574+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2870 · 2026-05-22T04:12:51.801902+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2871 · 2026-05-22T04:12:51.802385+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2872 · 2026-05-22T04:12:56.938410+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 2873 · 2026-05-22T04:12:58.445450+00:00_

{"result":"# 项目 schema-dag-extraction 概况\n\n## 实验状态 (69 个)\n\n- **exp012_llama_8b_r2_exp2**: DONE (negative) — \n- **exp012_llama_8b_r2**: DONE (success) — \n- **exp006_interaction_2x2**: DONE (negative) — \n- **exp012_llama_awq**: DONE (killed) — \n- **exp012_llama_8b_r3**: DONE (failed) — \n- **exp012_llama_8b**: DONE (killed) — \n- **exp_fewrel_40rel_r3**: DONE (failed) — \n- **exp_fewrel_40rel_r2**: DONE (failed) — \n- **exp012_llama_fewnerd_r4**: DONE (failed) — \n- **exp012_llama_8b_fewnerd**: DONE (failed) — \n- **exp_fewrel_40rel**: DONE (failed) — \n- **exp012_llama_fewnerd_r3**: DONE (failed) — \n- **exp012_llama_fewnerd_r2**: DONE (failed) — \n- **exp012_llama_fewnerd**: DONE (failed) — \n- **exp008_sdgd_zero_fewnerd**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- prompt_sensitivity（准备中）\n- prompt_sensitivity_dry4（准备中）\n- prompt_sensitivity_dry3（准备中）\n- prompt_sensitivity_dry2（准备中）\n- prompt_sensitivity_dry（准备中）\n- exp_aggregation_monte_carlo（准备中）\n- exp_scs_name_def_ablation（准备中）\n- exp_fewrel_contamination_check（准备中）\n- exp017_gpt4o_mini_fewrel（准备中）\n- exp_cross_embedding_sensitivity（准备中）\n- …另有 2 项\n\n## 近期结论\n- **exp_llama70b_ner_bcs_null** (success): Batch-level BCS does not correlate with NER F1 for LLaMA-3.1-70B-FP8, consistent with the BCS null observed in Qwen3-32B (r=0.004) and LLaMA-8B (r=-0.12). The confusability metric is not predictive of extraction quality at the batch level. ← 基于 exp012_llama_8b_r2_exp2\n  [LLaMA-70B NER BCS-null analysis](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_llama70b_ner_bcs_null/data/bcs_null_analysis.json)\n- **exp_gemini_flash_bcs_controlled** (success): BCS-accuracy negative correlation observed on open-weight models (Qwen3-32B, LLaMA) generalizes to proprietary API models. Gemini 2.5 Flash should show significant BCS gap on extreme-BCS batches at count 8 and count 16, confirming Dimension 2 is architecture-family-in
…[truncated 1221 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1507
}
```

</details>

---


### Tool call

_source line 2874 · 2026-05-22T04:12:58.496271+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2875 · 2026-05-22T04:12:59.451735+00:00_

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
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	\usepackage{listings}
16	
17	\title{How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	
28	\input{related_work}
29	
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	\begin{enumerate}[leftmargin=*,itemsep=2pt]
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B; cross-model validation (LLaMA-8B, LLaMA-70B, Gemini Flash) covers Dimensions~1--2 (count curves, BCS-controlled extremes) but does not replicate secondary analyses (error taxonomy, prompt sensitivity, TOST equivalence). Specifically, TOST factorial interaction (\S\ref{sec:multi_channel}) and SDGD failure analysis (\S\ref{sec:sdgd}) are established on Qwen3-32B alone; error taxonomy replicates on two additional models (Table~\ref{tab:cross_model_error_taxonomy}), but TOST and SDGD cross-model replication remains the most pressing extension. Gemini provides only partial, leverage-sensitive corroboration (leave-one-out $r{:}\;{-}0.80 \to {-}0.42$; Appendix~\ref{sec:appendix_cross_model_gemini}); proprietary-model generalization remains open.
41	
42	\item \textbf{Effect size and statistical design.} Pairwise SCS explains a small fraction of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\times$ BCS interaction is bounded on FewRel but nonzero on DocRED, partially confounded by BCS range restriction at higher counts (Appendix~\ref{sec:appendix_factoria
…[truncated 5422 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 2876 · 2026-05-22T04:12:59.502456+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 2877 · 2026-05-22T04:13:00.658522+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_round_29/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_round_29/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 2878 · 2026-05-22T04:13:00.861583+00:00_

-rw-r--r-- 1 ubuntu ubuntu 467485 May 22 04:11 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_round_29/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 203
}
```

</details>

---


### Tool result

_source line 2879 · 2026-05-22T04:13:06.338436+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"}]

Based on the search results, I found relevant information about EMNLP 2026 submissions, th
…[truncated 1405 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 6835
}
```

</details>

---


### Tool call

_source line 2880 · 2026-05-22T04:13:10.762112+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 submission guidelines page limit anonymity policy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 submission guidelines page limit anonymity policy"
  }
}
```

</details>

---


### Tool call

_source line 2881 · 2026-05-22T04:13:11.264616+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers deadline submission"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers deadline submission"
  }
}
```

</details>

---


### Tool call

_source line 2882 · 2026-05-22T04:13:12.269241+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": "100",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "offset": "100",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2883 · 2026-05-22T04:13:12.771864+00:00_

100	\small
101	\caption{NER batch-level BCS--F1 correlation across models. $^\dagger$Partial correlation controlling for type frequency. $^\ddagger$LLaMA-70B count\_12 shows $r{=}{-}0.42$ ($p{=}0.034$, uncorrected; Bonferroni $p{=}0.069$); pooled and count\_6 are null, consistent with sampling noise at $n{=}25$. The null is observed on three models; Gemini remains untested.}
102	\label{tab:cross_model_ner_null}
103	\begin{tabular}{lcl}
104	\toprule
105	\textbf{Model} & \textbf{NER BCS--F1 $r$} & \textbf{Status} \\
106	\midrule
107	Qwen3-32B & $0.004$ ($p = 0.94$) & Null \\
108	LLaMA-3.1-8B & $-0.12$ ($p = 0.29$)\rlap{$^\dagger$} & Null \\
109	LLaMA-3.1-70B & $-0.13$ ($p = 0.36$)\rlap{$^\ddagger$} & Null \\
110	Gemini 2.5 Flash & --- & Not tested \\
111	\bottomrule
112	\end{tabular}
113	\end{table}
114	
115	\begin{table}[h]
116	\centering
117	\small
118	\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin. Spearman $\rho$ computed over $n=148$ batches (NER), $n=154$ (RE), and $n=110$ (DocRE). IntraSub scales monotonically with BCS across all three datasets. DocRE missed rates decrease with BCS, indicating high-confusability errors shift from omission to substitution.}
119	\label{tab:error_taxonomy}
120	\resizebox{\columnwidth}{!}{%
121	\begin{tabular}{llrrrrrrr}
122	\toprule
123	 & & \multicolumn{5}{c}{\textbf{BCS Bin}} & & \\
124	\cmidrule(lr){3-7}
125	\textbf{Task} & \textbf{Error} & \textbf{Solo} & \textbf{Low} & \textbf{Mid} & \textbf{High} & \textbf{V.High} & \textbf{$\rho$} & \textbf{$p$} \\
126	\midrule
127	NER & IntraSub & 0\% & 1.6\% & 10.6\% & 49.4\% & --- & 1.000 & ${<}0.001$ \\
128	RE  & IntraSub & 0\% & 4.2\% & 13.0\% & 20.3\% & 32.3\% & 0.954 & ${<}\,0.001$ \\
129	DocRE & IntraSub & --- & 4.8\% & 22.4\% & 37.0\% & 41.9\% & 0.843 & ${<}\,0.001$ \\
130	\midrule
131	NER & Missed & --- & 42.8\% & 64.8\% & 49.9\% & --- & --- & --- \\
132	RE  & Missed & --- & 10.4\% & 11.3\% & 13.1\% & 15.7\% & --- & --- \\
133	DocRE & Missed & --- 
…[truncated 4583 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2884 · 2026-05-22T04:13:13.123768+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/",
  "description": "List paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/",
    "description": "List paper directory contents"
  }
}
```

</details>

---


### Tool result

_source line 2885 · 2026-05-22T04:13:13.174590+00:00_

_pdf_check
_pdf_check10
_pdf_check2
_pdf_check3
_pdf_check4
_pdf_check5
_pdf_check6
_pdf_check7
_pdf_check8
_pdf_check9
_pdf_images
abstract.tex
acl.sty
acl_natbib.bst
checklist.tex
conclusion.tex
discussion.tex
experimental_setup.tex
introduction.tex
main.aux
main.bbl
main.blg
main.fdb_latexmk
main.fls
main.log
main.out
main.pdf
main.tex
prompt_appendix.tex
references.bib
related_work.tex
results.tex
sdgd_negative.tex
supplementary.bbl
supplementary.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2886 · 2026-05-22T04:13:16.240066+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 submission guidelines page limit anonymity policy"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Update to Anonymity Policy – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/anonymity/"}]

Based on my search results, here's information about ACL Rolling Review (ARR) 2026 submission guidelines regarding page limits and anonymity policy:

## Page Limits

Papers should be desk-rejected if they go over the page limit (4 pages for short papers, 8 for long papers, excluding the ethical considerations and limitations).

## Anonymity Policy

Papers must not include authors' n
…[truncated 844 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 5477
}
```

</details>

---


### Tool result

_source line 2887 · 2026-05-22T04:13:17.144120+00:00_

Web search results for query: "EMNLP 2026 call for papers deadline submission"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"}]

Based on t
…[truncated 1113 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 5879
}
```

</details>

---


### Tool call

_source line 2888 · 2026-05-22T04:13:21.873420+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:2026.emnlp.org calls main conference papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:2026.emnlp.org calls main conference papers"
  }
}
```

</details>

---


### Tool call

_source line 2889 · 2026-05-22T04:13:24.253192+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_REVIEW_ISSUES\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_REVIEW_ISSUES\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 2890 · 2026-05-22T04:13:24.706049+00:00_

# Review Issues Tracker
# Updated: 2026-05-21 (v34 fixes applied for all R25 issues)

# ============================================================
# R25 MUST-FIX (4 items) — ALL ADDRESSED IN v34
# ============================================================

- id: R25-C1
  summary: "DocRED VIF=50.9 invalidates R²=58% as independent BCS evidence; must report semipartial R²"
  category: method
  severity: critical
  status: in_progress
  first_raised_round: 23
  last_seen_round: 25
  mentions:
    - {round: 23, reviewers: [R1, R2], note: "R23-C2: VIF=50.9, weaken wording"}
    - {round: 24, reviewers: [R1, R2], note: "R24-C1: Must recenter on FewRel R²=22%"}
    - {round: 25, reviewers: [R1, R2], note: "R1-W1 raised, R2 AGREE. VIF=50.9 far exceeds threshold 10. Must report semipartial R²."}
  action_items:
    - {round: 25, action: "Report DocRED semipartial R² (BCS unique variance after partialing centrality)", assigned_to: "Agent", status: done}
  resolution: "v34: True semipartial ΔR²_BCS=0.056 (5.6%) reported in §4.3. DocRED framed as 'partially confounded, 90% shared with centrality'. Clean evidence anchored to FewRel (semipartial ΔR²=0.273, VIF=1.18)."
  resolution_round: null

- id: R25-C2
  summary: "Confusability finding robust only on FewRel RE; generality claims in title/abstract overstate evidence scope"
  category: framing
  severity: critical
  status: in_progress
  first_raised_round: 25
  last_seen_round: 25
  mentions:
    - {round: 25, reviewers: [R1, R2], note: "Confusability evidence concentrated on FewRel RE."}
  action_items:
    - {round: 25, action: "Weaken title/abstract/conclusion generality claims", assigned_to: "Agent", status: done}
  resolution: "v34: Abstract says 'documented primarily in RE'; Intro scopes confusability to FewRel RE. Count degradation retains cross-task framing."
  resolution_round: null

- id: R25-C3
  summary: "NER null result mechanism: cannot distinguish zero effect from noise-masked effect"
  category: framing
  s
…[truncated 14663 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2891 · 2026-05-22T04:13:24.706561+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2892 · 2026-05-22T04:13:25.164302+00:00_

1	\begin{abstract}
2	Schema complexity affects training-free LLM information extraction through two independent dimensions: type count drives recall decline, while inter-type confusability drives type substitution errors. We present what is, to our knowledge, the first controlled study isolating these factors in zero-shot LLM IE across NER, RE, and event detection on four datasets. Using embedding-based confusability metrics (SCS/BCS) with controlled batch design, we find:
3	(1)~count degradation spans all three tasks (up to $-$49\,pp); confusability-driven substitution is documented primarily in RE, with bounded interaction;
4	(2)~BCS explains ${\sim}$22\% of cross-batch RE accuracy variance on FewRel (ecological level), replicating across three open-weight model families (8B--70B); NER batch-level signal is not detected at current power;
5	(3)~schema decomposition fails due to merge amplification and routing failure, though oracle routing confirms the two dimensions are independently addressable.
6	\end{abstract}
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 457
}
```

</details>

---


### Tool call

_source line 2893 · 2026-05-22T04:13:25.215007+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2894 · 2026-05-22T04:13:25.316089+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\looseness=-1
5	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\footnote{Code and data will be released upon acceptance.} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, and is attractive for applications where annotation is expensive or schemas evolve frequently \citep{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level), near-halving or worse. This degradation is not academic: real-world ontologies routinely define 50--200+ types, which places them squarely in the regime where training-free extraction becomes unreliable.
6	
7	\looseness=-1
8	What explains this degradation? Prior decomposition strategies \citep{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
9	
10	This study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accuracy.
11	
12	We ask three questions. \textbf{RQ1}: Does type
…[truncated 3215 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 2895 · 2026-05-22T04:13:28.381314+00:00_

Web search results for query: "site:2026.emnlp.org calls main conference papers"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"Leveraging Large Language Models for Improved Understanding of Communications With Patients With Cancer in a Call Center Setting: Proof-of-Concept Study","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11669882/"},{"title":"Natural language processing for humanitarian action: Opportunities, challenges, and the path toward humanitarian NLP","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10080095/"}]

Based on the web search results, here's the information about EMNLP 2026's call for main conference papers:

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

The conference aims to curate a diverse technical program—in addition to traditional research results, papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

**Important Submission Details:**

- For the ARR 2026 May cycle aligned with EMNLP, authors must explicitly declare which conference they intend to commit to at submission time, and this choice is binding for EMNLP 2026.
- Dual submissions are not allowed.
- Papers that have received reviews and a meta-review from ARR may be committed to EMN
…[truncated 380 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 6507
}
```

</details>

---


### Tool call

_source line 2896 · 2026-05-22T04:13:32.838228+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ACL Rolling Review\" 2026 May cycle deadline submission format requirements long paper short paper page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"ACL Rolling Review\" 2026 May cycle deadline submission format requirements long paper short paper page limit"
  }
}
```

</details>

---


### Tool call

_source line 2897 · 2026-05-22T04:13:34.696511+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2898 · 2026-05-22T04:13:34.998555+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	\looseness=-1
6	Training-free LLM IE spans instruction tuning \citep{instructuie-2023}, code-style schema encoding \citep{knowcoder-2024,codeie-2023}, annotation-guided extraction \citep{gollie-2024,adelie-2024}, schema-driven decoding \citep{slot-2025,oneke-2025}, and constrained JSON decoding \citep{json-schema-bench-2025,willard2023efficient}. NER methods include zero-shot decomposition \citep{xie-zeroshot-ner-2023,promptner-2023}, distillation \citep{uniner-2024}, and bidirectional encoders \citep{gliner-2024,gliner2-2025}; RE methods include zero-shot triplet extraction \citep{relationprompt-2022}, constrained generation \citep{josifoski-2022-genie}, and shared embedding spaces \citep{boylan-2025-glirel,wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales.
7	
8	\paragraph{Schema complexity in IE.}
9	\looseness=-1
10	The most directly related work is LLM-PEE \citep{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. LLM-PEE's union merge suffers the same precision collapse (0.56$\to$0.21; \S\ref{sec:sdgd}). In short, LLM-PEE assumes decomposition helps; we show why it should (confusability), why it does not (merge amplification), and what predicts the degradation (BCS). Other approaches address schema complexity via hard negative mining \citep{iepile-2024}, schema definition optimization \citep{parse-2025}, multi-agent debate \citep{crossagentie-2025,cma
…[truncated 2068 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 2899 · 2026-05-22T04:13:34.999192+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 2900 · 2026-05-22T04:13:35.050052+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \citep{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains and is suitable for cross-domain evaluation. We sample 1{,}000 instances uniformly from the test set; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \citep{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). A held-out validation confirms SCS--confusion generalization across the split boundary (Appendix~\ref{app:scs-heldout-validation}). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound; this balance makes it the primary dataset for BCS analysis. Contamination analysis (Appendix~\ref{app:split-origin}) shows extraction difficulty correlates inversely with training-set prevalence, and BCS effects are unchanged when controlling for contamination.
14	
15	\p
…[truncated 9432 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2901 · 2026-05-22T04:13:38.315332+00:00_

Web search results for query: ""ACL Rolling Review" 2026 May cycle deadline submission format requirements long paper short paper page limit"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on my search results for ACL Rolling Review 2026 May cycle information, here's what I found about the submission requirements:

## Submission Format and Page Limits

All ARR submissions are anonymous and in the format of a short paper (up to 4 pages) or long paper (up to 8 pages).

## Submission Requirements

Starting in May 2025, all submitting authors have to also sign up as reviewers (deadline: 48h
…[truncated 871 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 5477
}
```

</details>

---


### Tool call

_source line 2902 · 2026-05-22T04:13:43.446263+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 2903 · 2026-05-22T04:13:43.899617+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	All experiments use Qwen3-32B and the v1 prompt (\S\ref{sec:model}; Appendix~\ref{sec:appendix_prompts}) unless noted; cross-model validation covers Dimensions~1--2, while secondary analyses (error taxonomy, DocRED $R^2$, TOST) remain single-model.
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	Figure~\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where eliminating type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\%$\to$38.7\%, $-$56\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}). The pattern is stable across three seeds (max $\Delta = 10.7$\,pp, within 1\,SD; intra-batch variance exceeds inter-seed variance by ${>}$5$\times$; Appendix~\ref{app:variance-decomposition}). Formal trend analysis confirms monotonic RE decline (Jonckheere-Terpstra $J = 109{,}707$, $p < 0.001$). Count decline replicates on LLaMA-70B with comparable magnitude and on Gemini Flash (Appendix~\ref{sec:appendix_cross_model_gemini}). Count curves establish trend direction; magnitude estimation relies on the higher-powered BCS-controlled experiments (\S\ref{sec:bcs_controlled}).
10	
11	\subsection{Pairwise Confusability and Type Confusion}
12	\label{sec:pairwise}
13	
14	We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate (the fraction of $t_i$ gold instances misclassified as $t_j$) and correlate it with $\text{SCS}(t_i, t_j)$. Table~\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\
…[truncated 12725 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 2904 · 2026-05-22T04:13:43.900088+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 2905 · 2026-05-22T04:13:44.460239+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention is to partition the schema so confusable types never co-occur. We test \textbf{Schema-DAG-Guided Decomposition} (SDGD), which applies greedy graph coloring on the SCS graph to assign types to low-confusability batches.
5	
6	\paragraph{NER and ED: merge amplification.}
7	\looseness=-1
8	All decomposition modes fall below the single-pass NER baseline (F1\,=\,0.445): SDGD obtains 0.251, random batching 0.320. The core failure is \emph{merge amplification}: presenting text $k$ times collapses precision (0.563$\to$0.210--0.249). MAVEN event detection replicates this (precision 0.287$\to$0.091; Appendix~\ref{sec:appendix_sdgd}).
9	
10	\paragraph{RE: routing failure.}
11	\looseness=-1
12	Oracle routing recovers accuracy (0.802 vs.\ 0.504 single-pass; Table~\ref{tab:batch_composition}), but confusability-aware grouping yields only +1.4\,pp over random ($p \approx 0.19$, n.s.). All practical routing strategies fall below the single-pass baseline (Appendix~\ref{sec:appendix_routing}); the bottleneck is routing accuracy rather than partitioning quality.
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 560
}
```

</details>

---


### Tool call

_source line 2906 · 2026-05-22T04:13:44.460727+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2907 · 2026-05-22T04:13:44.562074+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions and mechanisms.}
5	\looseness=-1
6	The decomposition applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\S\ref{sec:centrality_confound}). RE effects replicate across three open-weight models (8B--70B), two formats, five prompts, and two datasets; no NER BCS effect detected across three models (8B--70B). At the type-pair level, confusability explains ${\sim}$1.3\% of variance---individually modest---but practitioners deploy full schemas as batches, where correlated pairwise effects compound. Batch-level $R^2 {\approx}\, 22\%$ on FewRel corresponds to a ${\sim}$31\,pp gap between extreme batches, the relevant practical construct for real-world zero-shot IE. The NER--RE asymmetry reflects different error-mode structures (\S\ref{sec:multi_channel}) and compressed BCS variance (Appendix~\ref{sec:appendix_ner_power}).
7	
8	\paragraph{Practical implications and conclusion.}
9	\label{sec:conclusion}
10	\looseness=-1
11	For NER, reducing candidate types is the primary lever. For RE, BCS enables pre-hoc diagnostics (flag SCS${}\,>\,0.85$ pairs; $R^2 {\approx}\, 0.22$ on FewRel); high-SCS pairs dominate type substitution errors (Appendix~\ref{app:error-analysis}). Practitioners can pre-compute SCS to identify high-risk type pairs before deployment, enabling schema-aware pool selection as a preprocessing step. Decompose-then-merge fails (\S\ref{sec:sdgd}), but oracle routing recovers accuracy (72.4\% vs.\ 50.4\%), confirming that count and confusability are independently addressable.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2908 · 2026-05-22T04:13:50.899068+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 2909 · 2026-05-22T04:13:53.329287+00:00_

{"result":"# 项目 schema-dag-extraction 概况\n\n## 实验状态 (69 个)\n\n- **exp012_llama_8b_r2_exp2**: DONE (negative) — \n- **exp012_llama_8b_r2**: DONE (success) — \n- **exp006_interaction_2x2**: DONE (negative) — \n- **exp012_llama_awq**: DONE (killed) — \n- **exp012_llama_8b_r3**: DONE (failed) — \n- **exp012_llama_8b**: DONE (killed) — \n- **exp_fewrel_40rel_r3**: DONE (failed) — \n- **exp_fewrel_40rel_r2**: DONE (failed) — \n- **exp012_llama_fewnerd_r4**: DONE (failed) — \n- **exp012_llama_8b_fewnerd**: DONE (failed) — \n- **exp_fewrel_40rel**: DONE (failed) — \n- **exp012_llama_fewnerd_r3**: DONE (failed) — \n- **exp012_llama_fewnerd_r2**: DONE (failed) — \n- **exp012_llama_fewnerd**: DONE (failed) — \n- **exp008_sdgd_zero_fewnerd**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- prompt_sensitivity（准备中）\n- prompt_sensitivity_dry4（准备中）\n- prompt_sensitivity_dry3（准备中）\n- prompt_sensitivity_dry2（准备中）\n- prompt_sensitivity_dry（准备中）\n- exp_aggregation_monte_carlo（准备中）\n- exp_scs_name_def_ablation（准备中）\n- exp_fewrel_contamination_check（准备中）\n- exp017_gpt4o_mini_fewrel（准备中）\n- exp_cross_embedding_sensitivity（准备中）\n- …另有 2 项\n\n## 近期结论\n- **exp_llama70b_ner_bcs_null** (success): Batch-level BCS does not correlate with NER F1 for LLaMA-3.1-70B-FP8, consistent with the BCS null observed in Qwen3-32B (r=0.004) and LLaMA-8B (r=-0.12). The confusability metric is not predictive of extraction quality at the batch level. ← 基于 exp012_llama_8b_r2_exp2\n  [LLaMA-70B NER BCS-null analysis](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_llama70b_ner_bcs_null/data/bcs_null_analysis.json)\n- **exp_gemini_flash_bcs_controlled** (success): BCS-accuracy negative correlation observed on open-weight models (Qwen3-32B, LLaMA) generalizes to proprietary API models. Gemini 2.5 Flash should show significant BCS gap on extreme-BCS batches at count 8 and count 16, confirming Dimension 2 is architecture-family-in
…[truncated 1221 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 2430
}
```

</details>

---


### Tool call

_source line 2910 · 2026-05-22T04:13:53.531028+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_round_29/submitted.pdf 2>/dev/null | grep -i \"pages\" || echo \"PDFINFO_NOT_AVAILABLE\"",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_round_29/submitted.pdf 2>/dev/null | grep -i \"pages\" || echo \"PDFINFO_NOT_AVAILABLE\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 2911 · 2026-05-22T04:13:54.285311+00:00_

Pages:           27

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 754
}
```

</details>

---


### Tool call

_source line 2912 · 2026-05-22T04:13:54.436485+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 2913 · 2026-05-22T04:13:54.437123+00:00_

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
11	\title{Supplementary Material for: How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
12	
13	\author{Anonymous}
14	
15	\begin{document}
16	\maketitle
17	
18	All supplementary material is included in the appendix of the main paper.
19	
20	\end{document}
21	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2914 · 2026-05-22T04:14:02.150668+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 2915 · 2026-05-22T04:14:04.059805+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/decisions.yaml\", \"content\": \"_next_id: 72\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 16:10 UTC\\n  summary: 项目立项，MVP 验证方案：Experiment 2 (Confusability Controlled) 为核心验证实验\\n  rationale: 'IDEA_BRIEF 的核心假设是 type confusability 独立于 type count 驱动 LLM IE 质量下降。Experiment\\n    2（固定 count 变 BCS）是最直接的假设检验。Pass 标准: |r|≥0.3 且 p<0.05。ACE05 RE + Few-NERD 双数据集验证。ARR\\n    May 25 DDL（11天），MVP 需 1-2 天完成。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 16:15 UTC\\n  summary: 修正 MVP 统计设计：random samples 从 10 增至 25/档，加入 per-type solo baseline 控制变量，核心指标改为\\n    Δ(solo_F1 - batch_F1)\\n  rationale: Reviewer 指出 n=12 下 |r|=0.3 对应 p≈0.34，无法同时满足 |r|≥0.3 且 p<0.05。增至 25 random\\n    batches/档 → n≈54，|r|≥0.27 即可达 p<0.05。同时加入 solo F1 控制 type 固有难度，避免将\\\"类型本身难抽取\\\"误归因于\\\"confusability\\n    效应\\\"。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 23:11 UTC\\n  summary: MVP 分析方法从 Δ(solo-batch) 切换到 within-count Pearson r(F1, BCS)，pass 标准更新为\\n    |r|≥0.3 at fixed count\\n  rationale: Exp 1 发现 count curve 方向反转（F1 随 count 上升），根因是低 count 时模型过度 hallucinate（pred/gold=8x\\n    at count=1）。solo baseline 处于极端行为模式，Δ 被跨 count 行为差异污染。改为 within-count 对比更干净：同一\\n    count 下比较不同 BCS 的 F1，直接检验 confusability 独立效应。\\n  related_experiments:\\n  - exp_id: exp001_count_baseline\\n    role: evidence\\n    result: count curve reversed, hallucination at low count\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 23:31 UTC\\n  summary: MVP 主指标更新为 within-count r(recall, BCS)，F1 因 over-prediction confound 降为补充指标\\n  rationale: Exp 1 text-match 重评估发现：recall 单调下降（0.72→0.42，符合预期），precision 单调上升（0.11→0.52，over-prediction\\n    减少），F1 受 precision 主导而反转。within-count 分析中 precision confound 在同一 count 下近似恒定，F1\\n    仍可用；但 recall 更干净且直接反映 type confusion。WrongType 错误（text 正确但 type 错标）随 count 从 0\\n    升至 2434，直
…[truncated 1449 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1909
}
```

</details>

---


### Tool call

_source line 2916 · 2026-05-22T04:14:04.362395+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport yaml\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/project_config.yaml') as f:\n    cfg = yaml.safe_load(f)\nprint(yaml.dump(cfg.get('external_review', {}), default_flow_style=False))\n\" 2>/dev/null || echo \"CONFIG_READ_FAILED\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport yaml\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/project_config.yaml') as f:\n    cfg = yaml.safe_load(f)\nprint(yaml.dump(cfg.get('external_review', {}), default_flow_style=False))\n\" 2>/dev/null || echo \"CONFIG_READ_FAILED\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 2917 · 2026-05-22T04:14:04.664824+00:00_

CONFIG_READ_FAILED

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 2918 · 2026-05-22T04:14:11.755863+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A 5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/project_config.yaml 2>/dev/null || grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ --include=\"*.yaml\" -l 2>/dev/null || echo \"NOT_FOUND\"",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A 5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/project_config.yaml 2>/dev/null || grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ --include=\"*.yaml\" -l 2>/dev/null || echo \"NOT_FOUND\"",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 2919 · 2026-05-22T04:14:11.906991+00:00_

NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2920 · 2026-05-22T04:14:44.534127+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "schema-dag-extraction",
  "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "schema-dag-extraction",
    "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
  }
}
```

</details>

---


### Tool result

_source line 2921 · 2026-05-22T04:14:59.947752+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 15413
}
```

</details>

---


### Tool call

_source line 2922 · 2026-05-22T04:15:00.150034+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 审稿任务 — Reviewer 1（方法严谨性）\n\n**论文**: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**格式要求**: Long paper, 正文 ≤ 8 页, references 不限, Limitations 不计入页数, ACL template, 双盲匿名\n**论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex`\n**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_round_29/submitted.pdf`\n\n### 你的审查侧重\n\n**方法严谨性**——重点审查：\n\n1. **实验设计**：BCS-controlled 实验的内部效度（confound 控制是否充分、batch 构造方法是否引入偏差）\n2. **统计分析**：\n   - R² 和 partial correlation 的可信度（DocRED VIF=50.9 的处理是否恰当）\n   - TOST 等价性检验的 margin 选择是否合理（概率/logit 尺度不一致）\n   - Bootstrap CI 的适当性（across-batch correlation 问题）\n   - 多重比较修正\n3. **因果推断**：correlational → causal claims 的边界是否诚实\n4. **跨模型验证**：LLaMA-8B/70B/Gemini Flash 的验证范围和力度是否支持论文声称\n5. **NER null 结果**：power analysis 和\"cannot distinguish\"表述是否充分\n6. **SDGD 失败分析**：merge amplification 诊断的证据链是否完整\n7. **页数合规**：确认正文不超过 8 页\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n- **Summary**: 2-3 句总结\n- **Strengths**: 逐条列出（S1, S2, ...）\n- **Weaknesses**: 逐条列出（W1, W2, ...），标注严重程度 [Critical/Major/Minor]\n- **Questions**: 需要作者澄清的问题（Q1, Q2, ...）\n- **Missing References**: 遗漏的重要相关工作\n- **Overall Assessment**: 评分 + 置信度 + 简短理由"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 审稿任务 — Reviewer 1（方法严谨性）\n\n**论文**: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**格式要求**: Long paper, 正文 ≤ 8 页, references 不限, Limitations 不计入页数, ACL template, 双盲匿名\n**论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex`\n**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_round_29/submitted.pdf`\n\n### 你的审查侧重\n\n**方法严谨性**——重点审查：\n\n1. **实验设计**：BCS-controlled 实验的内部效度（confound 控制是否充分、batch 构造方法是否引入偏差）\n2. **统计分析**：\n   - R² 和 partial correlation 的可信度（DocRED VIF=50.9 的处理是否恰当）\n   - TOST 等价性检验的 margin 选择是否合理（概率/logit 尺度不一致）\n   - Bootstrap CI 的适当性（across-batch correlation 问题）\n   - 多重比较修正\n3. **因果推断**：correlational → causal claims 的边界是否诚实\n4. **跨模型验证**：LLaMA-8B/70B/Gemini Flash 的验证范围和力度是否支持论文声称\n5. **NER null 结果**：power analysis 和\"cannot distinguish\"表述是否充分\n6. **SDGD 失败分析**：merge amplification 诊断的证据链是否完整\n7. **页数合规**：确认正文不超过 8 页\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n- **Summary**: 2-3 句总结\n- **Strengths**: 逐条列出（S1, S2, ...）\n- **Weaknesses**: 逐条列出（W1, W2, ...），标注严重程度 [Critical/Major/Minor]\n- **Questions**: 需要作者澄清的问题（Q1, Q2, ...）\n- **Missing References**: 遗漏的重要相关工作\n- **Overall Assessment**: 评分 + 置信度 + 简短理由"
  }
}
```

</details>

---


### Tool result

_source line 2923 · 2026-05-22T04:15:11.662919+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 11512
}
```

</details>

---


### Tool call

_source line 2924 · 2026-05-22T04:15:11.814207+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 审稿任务 — Reviewer 2（新颖性与完整性）\n\n**论文**: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**格式要求**: Long paper, 正文 ≤ 8 页, references 不限, Limitations 不计入页数, ACL template, 双盲匿名\n**论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex`\n**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_round_29/submitted.pdf`\n\n### 你的审查侧重\n\n**新颖性与完整性**——重点审查：\n\n1. **贡献新颖性**：\n   - SCS/BCS 指标与 LLM-PEE (2025) 的 embedding similarity 有何本质区别？\n   - \"first controlled study\" claim 是否过度？Chen et al. (2026) 等同期工作关系？\n   - 实证发现 vs 方法论贡献的定位是否清晰\n2. **Related Work 完整性**：\n   - 是否遗漏重要的 schema complexity / LLM IE 近期工作（2025-2026）\n   - Label confusion / type similarity 的跨领域文献覆盖\n3. **写作质量**：\n   - Abstract 信息密度是否合适\n   - 论文叙事逻辑（RQ → Method → Results → Discussion）是否流畅\n   - Discussion/Conclusion 是否充分展开 practical implications\n   - Limitations 是否全面且精炼\n4. **结构完整性**：\n   - 4 个数据集（Few-NERD, FewRel, DocRED, MAVEN）的角色是否清晰\n   - 正面结果和负面结果（NER null, SDGD failure）的平衡\n   - Appendix 内容是否应提升到正文\n5. **格式合规**：\n   - ACL template 正确使用\n   - 双盲匿名（无身份泄露）\n   - References 格式一致性\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n- **Summary**: 2-3 句总结\n- **Strengths**: 逐条列出（S1, S2, ...）\n- **Weaknesses**: 逐条列出（W1, W2, ...），标注严重程度 [Critical/Major/Minor]\n- **Questions**: 需要作者澄清的问题（Q1, Q2, ...）\n- **Missing References**: 遗漏的重要相关工作\n- **Overall Assessment**: 评分 + 置信度 + 简短理由"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 审稿任务 — Reviewer 2（新颖性与完整性）\n\n**论文**: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**格式要求**: Long paper, 正文 ≤ 8 页, references 不限, Limitations 不计入页数, ACL template, 双盲匿名\n**论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex`\n**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_round_29/submitted.pdf`\n\n### 你的审查侧重\n\n**新颖性与完整性**——重点审查：\n\n1. **贡献新颖性**：\n   - SCS/BCS 指标与 LLM-PEE (2025) 的 embedding similarity 有何本质区别？\n   - \"first controlled study\" claim 是否过度？Chen et al. (2026) 等同期工作关系？\n   - 实证发现 vs 方法论贡献的定位是否清晰\n2. **Related Work 完整性**：\n   - 是否遗漏重要的 schema complexity / LLM IE 近期工作（2025-2026）\n   - Label confusion / type similarity 的跨领域文献覆盖\n3. **写作质量**：\n   - Abstract 信息密度是否合适\n   - 论文叙事逻辑（RQ → Method → Results → Discussion）是否流畅\n   - Discussion/Conclusion 是否充分展开 practical implications\n   - Limitations 是否全面且精炼\n4. **结构完整性**：\n   - 4 个数据集（Few-NERD, FewRel, DocRED, MAVEN）的角色是否清晰\n   - 正面结果和负面结果（NER null, SDGD failure）的平衡\n   - Appendix 内容是否应提升到正文\n5. **格式合规**：\n   - ACL template 正确使用\n   - 双盲匿名（无身份泄露）\n   - References 格式一致性\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n- **Summary**: 2-3 句总结\n- **Strengths**: 逐条列出（S1, S2, ...）\n- **Weaknesses**: 逐条列出（W1, W2, ...），标注严重程度 [Critical/Major/Minor]\n- **Questions**: 需要作者澄清的问题（Q1, Q2, ...）\n- **Missing References**: 遗漏的重要相关工作\n- **Overall Assessment**: 评分 + 置信度 + 简短理由"
  }
}
```

</details>

---


### Tool result

_source line 2925 · 2026-05-22T04:15:13.500661+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1686
}
```

</details>

---


### Assistant

_source line 2926 · 2026-05-22T04:15:23.581168+00:00_

已完成 Step 1 派发：

- ✅ 视觉审查 Agent 已启动（fire-and-forget）
- ✅ Reviewer 1（方法严谨性）已分配任务
- ✅ Reviewer 2（新颖性与完整性）已分配任务

等待两位 Reviewer 返回独立初审意见。收到后进入 Step 2（交叉分享）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 240

## Round 240

2 recorded events


### User

_source line 2927 · 2026-05-22T04:21:34.306645+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见 — 新颖性与完整性

**论文**: "How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?"
**Venue**: EMNLP 2026 (ARR May 2026)

---

## Summary

本文研究 schema 复杂度（类型数量 + 类型间混淆度）如何影响 training-free LLM 信息抽取性能。提出 Schema Confusability Score (SCS) 和 Batch Confusability Score (BCS) 两个指标，通过 BCS-controlled batch 设计在 4 个数据集（Few-NERD, FewRel, DocRED, MAVEN）上隔离 count 和 confusability 两个维度的影响。主要发现：(1) 类型数量驱动 recall 单调下降；(2) BCS 解释 FewRel 上约 22% 的跨 batch 准确率方差；(3) Schema 分解（SDGD）因 merge amplification 和 routing failure 而失败。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计严谨（BCS-controlled batches、factorial ANOVA、bootstrap CIs、TOST equivalence tests），统计方法论扎实。但 confusability 的核心发现主要依赖 FewRel 单一数据集，NER BCS 结果为 null（Table 5），MAVEN 被 degree centrality 混淆（Appendix E.1），削弱了多任务叙事。 |
| Excitement | 3/5 | 研究问题具有实际意义，controlled study 设计是方法论贡献。但核心指标（embedding cosine similarity）继承自 LLM-PEE，发现本身（类型多→recall 降、相似类型→混淆）在直觉上不令人意外，novelty 更多在实验方法而非发现本身。 |
| Reproducibility | 4/5 | 19 页 appendix 提供完整 prompt templates（Appendix G）、超参数、统计检验细节、cross-model validation。承诺 code/data release。仅 Gemini 2.5 Flash 验证涉及 proprietary API。 |
| Overall Assessment | 3.5/5 | Borderline Conference。扎实的实证研究，controlled experimental design 是真正的贡献，统计严谨度高于同类工作。但指标新颖性有限（继承 LLM-PEE），confusability 发现过度依赖 FewRel，"first controlled study" claim 需要更审慎表述。适合 Findings。 |
| Confidence | 4/5 | 熟悉 LLM IE、zero-shot extraction、实验方法论领域。仔细阅读了全文及全部 appendix。 |

---

## Strengths

**S1: BCS-controlled batch 设计是真正的方法论贡献。** Experiment 2（§3.3）通过构造 extreme batches（低 BCS vs 高 BCS）在固定类型数量下隔离 confusability 效应，这比典型的观测性研究更干净。Factorial analysis（Appendix C）形式化验证了 count 和 confusability 的独立性（交互项不显著，p = 0.47）。这一实验范式可被后续研究复用。

**S2: 统计严谨度显著高于同类工作。** 论文使用了 bootstrap CIs、TOST equivalence tests（Appendix C, Table 10）、statistical power analysis（Appendix E.2）、permutation tests（Appendix L）、partial correlations controlling for confounders（Appendix E.1, Table 12）。这种程度的统计素养在 NLP 实证研究中少见。

**S3: 诚实报告负面结果。** NER BCS null result（Section 4.5, Table 5）没有被掩盖，而是通过 power analysis 解释（检测效应量 |r| = 0.11 需要 n ≈ 150，实际 n = 25）。SDGD 分解失败（Section 5）同样如实报告。这种透明度值得肯定。

**S4: 跨任务、跨模型、跨数据集的覆盖面。** 主实验覆盖 NER/RE/ED 三个任务，cross-model validation（Appendix S: LLaMA-3.1-8B-Instruct; Appendix T: LLaMA-70B; Appendix U: Gemini 2.5 Flash）展示了方向一致性。Cross-domain connections（Appendix S, Table 23）验证跨架构泛化。

**S5: Practical implications 具体可操作。** Section 6 和 Section 8 提出的 SCS pre-computation、schema-aware pool selection、decompose-then-merge 框架的失败教训，对 production IE 系统有直接参考价值。

---

## Weaknesses

**W1 [Major]: SCS/BCS 相对于 LLM-PEE (Liu et al., 2025) 的技术新颖性不足。**

论文在 Section 2（p.3）明确承认 "SCS inherits the embedding-similarity criterion from LLM-PEE"。核心指标就是类型名称的 embedding cosine similarity，BCS 是其 batch 级 max 聚合。虽然论文声称贡献在于 controlled experimental methodology 而非指标本身，但读者可能质疑：如果指标不新，那这是一篇关于"用已有指标做更好实验"的论文——这在方法论贡献上是否足够支撑 conference-level 接收？

Appendix I 比较了 mean vs max BCS 聚合，Appendix M 比较了 name-only vs name+definition embeddings——这些消融研究存在但未在正文中充分讨论。建议在 Section 3.2 中更明确地阐述 SCS/BCS 相对于 LLM-PEE 的技术差异点，特别是双 embedding（Qwen3 + MiniLM）互补性和 BCS 聚合策略的设计理由。

**W2 [Major]: Confusability 发现过度依赖 FewRel，多任务叙事被削弱。**

论文声称跨 NER/RE/ED 研究 confusability，但：
- NER (Few-NERD): BCS 效应为 null（Table 5, p.6, 三个模型中 Qwen3-32B p=0.091, LLaMA-3.1-8B r=−0.12 p=0.26, LLaMA-70B r=−0.13 p=0.46）
- MAVEN (ED): BCS 被 degree centrality 完全混淆（Appendix E.1, Table 11, controlling for centrality 后 BCS 变为 non-significant）
- DocRED: 仅用于 count curves，未做 BCS-controlled 实验

这意味着 BCS 作为 confusability predictor 的核心证据基本仅来自 FewRel。这是一个单数据集发现（R² ≈ 0.22），而非论文暗示的跨任务普遍规律。建议在 abstract 和 introduction 中更精确地限定 confusability 发现的适用范围，或者补充更多数据集的 BCS-controlled 实验。

**W3 [Major]: "First controlled study" claim 需要更审慎的表述。**

Abstract 声称 "to our knowledge, the first controlled study isolating these factors in zero-shot LLM IE"。但：
- Chen et al. (2026)（论文自身在 p.2 引用）也量化了 training-evaluation type similarity 对 zero-shot NER 的影响，虽然角度不同（cross-set vs within-set），但同属"controlled study of schema complexity"
- GoLLIE (Sainz et al., 2024, ICLR) 通过 annotation guidelines 隐式控制了 schema 对 zero-shot IE 的影响
- "Reflect then Learn" (Zhang et al., AAAI 2026) 研究了 IE 中的 introspective confusion，概念上与 type confusability 相关

建议将 claim 限定为 "first controlled study *simultaneously isolating count and inter-type confusability as independent dimensions* in zero-shot LLM IE"，而非泛化的 "first controlled study"。

**W4 [Minor]: Schema 分解（Section 5）在正文中的定位不当。**

Section 5 介绍 SDGD，展示所有分解模式均低于 single-pass baseline（Appendix B, Table 8: 最佳 F1 = 0.292 vs single-pass 0.580），然后分析失败原因（merge amplification, routing failure）。这一节读起来像是一个"我们尝试了但失败了"的探索性报告。对于一篇 8 页正文的论文，用一整个 section 报告一个失败的方法，挤压了其他更有价值内容（如 cross-model validation）的正文空间。

建议选择以下之一：(1) 将 SDGD 降级为 appendix，把 cross-model validation 的关键结果提升到正文；(2) 如果保留在正文，需要更深入地分析失败机制并提出可行的改进方向。

**W5 [Minor]: Discussion/Conclusion（Section 6）对理论 implications 展开不足。**

Section 6 讨论了 boundary conditions 和 practical implications，但缺少对更深层问题的讨论：为什么 embedding similarity 能预测 LLM 的 type confusion？这暗示了 LLM 内部的 type representation 与 external embedding space 有什么关系？SCS 基于 Qwen3 的 embedding——这意味着模型的"自我认知"可以预测其行为吗？这些理论层面的讨论会提升论文的 intellectual contribution。

**W6 [Minor]: 写作细节问题。**

- Abstract 信息密度可提高："using embedding-based confusability metrics (SCS/BCS) with controlled batch design" 过于笼统，读者无法从 abstract 理解 SCS 具体量化什么。建议明确为 "pairwise cosine similarity between type-name embeddings"。
- Section 4.2（p.5-6）同时报告 FewRel 和 DocRED 的结果，但 DocRED 的处理显著少于 FewRel，造成不平衡感。
- Table 1（p.3）的 SCS/BCS ranges 列标注 "not comparable across embedding models"，但正文中未充分解释这一限制对结论的影响。

---

## Questions

**Q1**: SCS 基于类型名称的 embedding similarity。但 FewRel 使用 Wikidata property descriptions 作为类型定义（§3.1），而 Few-NERD 使用层级分类名。Appendix M 比较了 name-only vs name+definition，结果如何？是否 definition-based embeddings 能改善 NER 上的 null result？

**Q2**: BCS 聚合策略使用 max pairwise SCS（§3.2, formula (2)）。Appendix I 比较了 mean vs max——在什么条件下 mean 优于 max？这个选择对 FewRel R² ≈ 0.22 的 headline result 有多敏感？

**Q3**: Factorial analysis（Appendix C）显示交互项不显著（p = 0.47），但 TOST equivalence test 也不确定（p = 0.28）。如果 count × confusability 存在交互效应，这对 "independently addressable" 的核心 claim 意味着什么？是否需要更大的样本量来 resolve 这个问题？

**Q4**: SDGD（Section 5）使用 SCS matrix 上的 graph coloring。阈值 τ 的选择标准是什么（Appendix B 提到 LARGEST_FIRST）？是否尝试过其他阈值或 clustering 策略？

**Q5**: Cross-model validation（Appendix S-U）显示 LLaMA-3.1-8B 和 Gemini 2.5 Flash 的 degradation pattern 方向一致。但对于更大的 frontier models（如 GPT-4o 级别），confusability 效应是否可能因模型容量增大而减弱？论文是否有预测？

---

## Missing References

1. **"Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion" (Zhang et al., AAAI 2026)** — 提出 dual-level introspective uncertainty (format + content uncertainty) 来量化 LLM 在 IE 中的 confusion。"Content uncertainty" 概念与本文的 type confusability 直接相关，应在 Related Work 中讨论。

2. **"Diagnosing Structural Failures in LLM-Based Evidence Extraction for Meta-Analysis" (arXiv 2602.10881, 2026)** — 另一项通过 tiered query framework 控制 schema 结构复杂度来研究 LLM 抽取性能的研究，虽然领域不同（meta-analysis），但 controlled study 设计思路高度相关。

3. **"NER Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings" (Findings of EMNLP 2025)** — 使用 contrastive projection 对齐 type-compatible entities，与 SCS 的 embedding similarity 方法论直接相关。

4. **"Show Less, Instruct More: Enriching Prompts with Definitions and Guidelines for Zero-Shot NER" (2024)** — 研究 definition quality 对 zero-shot NER 的影响，与本文 Appendix M 的 name vs definition embedding 比较相关。

---

## 主要优势（总结）

- BCS-controlled batch 设计是该领域的方法论创新，可被广泛复用
- 统计严谨度（bootstrap CIs, TOST, power analysis, partial correlations）显著高于同类工作
- 诚实报告 NER null result 和 SDGD 失败，附带详细的 failure analysis
- 19 页 appendix 提供的 cross-model validation、sensitivity analysis、confound controls 为 reproducibility 树立了高标准
- 实用建议（SCS pre-computation, schema-aware pool selection）对 production IE 有直接价值

---

## Overall Assessment

**Overall**: 3.5/5 — Borderline Conference

**一句话总结**: 扎实的实证研究，BCS-controlled 实验设计是真正的方法论贡献，但核心指标新颖性有限（继承 LLM-PEE），confusability 的核心发现过度依赖 FewRel 单一数据集，"first controlled study" claim 需更审慎表述。统计严谨度和 appendix 质量优秀，建议 Findings 接收。

**Confidence**: 4/5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2928 · 2026-05-22T04:21:47.209191+00:00_

Reviewer 2 审稿意见已收到。核心评价：3.5/5（Borderline Conference），主要 concern 集中在指标新颖性、FewRel 单数据集依赖、以及 "first controlled study" claim 的表述精度。

等待 Reviewer 1 审稿意见返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 241

## Round 241

2 recorded events


### User

_source line 2929 · 2026-05-22T04:21:54.183834+00:00_

[Reviewer 2 审稿结果]:
审稿完成。核心评价：

- **Overall 3.5/5 (Borderline Conference)**，建议 Findings 接收
- **3 个 Major 问题**：SCS/BCS 相对 LLM-PEE 技术新颖性不足；confusability 发现过度依赖 FewRel 单数据集（NER null, MAVEN 被 centrality 混淆）；"first controlled study" claim 需限定范围
- **3 个 Minor 问题**：SDGD section 正文定位不当、Discussion 理论 implications 不足、写作细节
- **主要优势**：BCS-controlled batch 实验设计是方法论创新、统计严谨度高（TOST/bootstrap/power analysis）、负面结果诚实报告、appendix 质量优秀
- 补充了 4 篇可能遗漏的相关工作，提出了 5 个需作者澄清的问题

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2930 · 2026-05-22T04:22:03.844758+00:00_

收到 Reviewer 2 审稿意见。等待 Reviewer 1 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 242

## Round 242

6 recorded events


### User

_source line 2931 · 2026-05-22T04:23:27.452508+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见（方法严谨性）

**论文**: "How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?"
**Venue**: EMNLP 2026 (ARR May 2026 cycle)

---

## 总体评分

**Overall Assessment**: 3.5 / 5 (Borderline Conference)
**一句话总结**: 实验设计有真正的方法论创新（BCS-controlled batches），count 维度的退化故事扎实，但 BCS 度量的干净证据仅限 FewRel RE 一个数据集，且多处统计分析存在需要解决的方法论问题。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5 / 5 | Count 退化有充分支撑；BCS 核心证据局限于 FewRel，DocRED 多重共线性严重（VIF=50.9），MAVEN BCS-accuracy 相关性完全可归因于 centrality 混淆变量；TOST 结论依赖于量表选择 |
| Excitement | 3 / 5 | 研究问题实际相关，BCS-controlled 实验范式有方法论贡献；但发现偏确认性（类型多→性能降），可操作洞见有限（分解方案失败但未提供有效替代） |
| Overall Assessment | 3.5 / 5 | Borderline Conference——count 维度是 solid contribution，但 BCS 度量的泛化证据不足以支撑主要叙事 |
| Confidence | 4 / 5 | 仔细阅读全文及所有附录，逐一核查了统计方法论 |
| Reproducibility | 4 / 5 | 附录提供了完整的 prompt 模板、超参、batch 构造细节；代码/数据待发布 |

---

## Summary

本文研究 schema 复杂度（类型数量和类型间可混淆性）如何影响 zero-shot LLM 信息抽取。引入 SCS/BCS 度量，在 4 个数据集、3 个任务上进行控制实验。主要发现：(1) count 退化在所有任务上单调存在；(2) BCS 在 FewRel RE 上解释 ~22% 的跨 batch 准确率方差；(3) schema 分解因 merge amplification 和 routing failure 而失败。实验设计（BCS-controlled batches）是真正的方法论创新，但 BCS 证据的可推广性受到 multicollinearity、confound 和 null results 的严重限制。

---

## Strengths

**S1. 新颖且有价值的实验范式。** BCS-controlled batch design（§3.3, Experiment 2）是本文最重要的方法论贡献。通过固定 count 变化 BCS 来隔离 confusability 效应，这在 schema complexity 研究中是真正的 first。

**S2. 异常透明和诚实的报告。** 论文对 null results（NER batch-level BCS, §4.1-4.3）、confounders（centrality, Appendix E.1）、MAVEN BCS-accuracy 完全可归因于混淆变量（§4.5, Table 11-12）的报告堪称模范。很多论文会隐藏这些不利发现，本文选择正面讨论。

**S3. 极其详尽的附录。** 从 Appendix A 到 Y，涵盖 factorial analysis (C)、TOST sensitivity (C)、power analysis (E.2)、confound identification (E.1)、BCS aggregation comparison (I)、variance decomposition (R)、prompt sensitivity (H)、cross-model validation (S-U) 等。几乎每一个可能的方法论质疑都在附录中有预判性讨论。

**S4. 多模型验证方向正确。** 在 Qwen3-32B 基础上增加 LLaMA-3.1-8B、LLaMA-70B、Gemini 2.5 Flash 三个模型的验证（Appendix S-U），且覆盖了开源/闭源、不同规模。Count 退化模式在所有模型上复现。

**S5. Count 退化的实证基础扎实。** Experiment 1（count curves, §4.1）在 4 个数据集上的结果一致且清晰（Figure 1），效应量大（FewRel RE recall 从 0.72 降至 ~0.27），cross-model 复现良好。这一维度的贡献本身就有价值。

---

## Must-Fix 问题（影响接收决定）

**W1** [Critical] **BCS 度量的干净证据仅限 FewRel RE 一个数据集，但论文叙事暗示更广泛的适用性**

- 具体位置：Abstract ("confusability drives type substitution errors")、§1 ("isolating these factors in zero-shot LLM IE across NER, RE, and event detection")、§4.3、§4.5、Appendix E.1
- 问题：逐一梳理 4 个数据集的 BCS 证据状态：
  - **FewRel RE**：BCS 效应显著且干净（VIF=1.18, Table 12），R²=0.22——唯一的干净证据
  - **DocRED RE**：VIF=50.9（Table 12），BCS 与 degree centrality 的相关系数 r=0.99，partial correlation 在如此极端的多重共线性下不可信——标准误膨胀 √50.9 ≈ 7.1 倍，"显著"的 partial correlation 可能是数值伪影
  - **MAVEN ED**：Appendix E.1 明确承认 "Under joint control, both embeddings yield p > 0.2; the raw positive BCS-F1 correlation on MAVEN is thus fully attributable to centrality-related confounders"
  - **Few-NERD NER**：batch-level BCS-F1 correlation 为 null（§4.1, §4.3）
- 为什么影响接收：论文的核心创新是 BCS 度量及其 controlled 验证。如果 4 个数据集中只有 1 个（FewRel）提供干净证据，title 中的 "Schema Complexity Predict Performance" 和 abstract 中的 "across NER, RE, and event detection" 就存在过度概括风险。Pairwise SCS-confusion correlation（Table 2）虽然更广泛成立，但 batch-level BCS——论文的主要实用贡献——仅在 FewRel 上经受住了严格检验。
- 建议修改方向：(a) 在 abstract/introduction 中更明确区分 "count 退化"（4 数据集一致）和 "BCS 效应"（FewRel 干净, DocRED confounded, MAVEN confounded, NER null）；(b) 考虑将 title 或主要 claim 的范围缩窄为 RE；(c) 补充 1 个 VIF 可控的数据集上的 BCS-controlled 实验以增强泛化性。

**W2** [Critical] **DocRED VIF=50.9 的处理不充分**

- 具体位置：Table 12 (p.16)、§4.5、Appendix E.1
- 问题：VIF > 10 已属严重多重共线性；VIF=50.9 意味着 BCS 和 degree centrality 几乎完全线性相关。在这种条件下：
  - Partial regression 系数的标准误膨胀约 7 倍，置信区间极宽
  - "Partial correlation remains highly significant" 这一表述可能误导读者——在 VIF=50.9 下，partial correlation 的 p-value 不可信
  - 论文虽然承认 "does not uniquely identify the causal channel"，但 DocRED 仍出现在 §4.3 的 main text 结果中，且 §6 的 Discussion 中未专门讨论 DocRED 结果的可解释性
- 为什么影响接收：DocRED 是论文使用的两个 RE 数据集之一。如果 DocRED 的 BCS 证据不可用，RE 的 BCS 故事就仅剩 FewRel 一个数据集，进一步削弱泛化性。
- 建议修改方向：(a) 在 main text 中明确标注 DocRED BCS 结果因 VIF=50.9 而不可解释（而非仅在附录中讨论）；(b) 考虑使用 ridge regression 或 PCA 降维来处理 multicollinearity；(c) 如果 partial correlation 不可信，就不应在结果中呈现为支持 BCS 的证据。

---

## Should-Fix 问题（影响评分但不一票否决）

**W3** [Major] **TOST 等价性检验的结论依赖于量表选择（probability vs. logit），论文未充分讨论其含义**

- 具体位置：§4.4、Appendix C (p.14-15)、Table 10
- 问题：Factorial interaction 的 TOST 检验在 probability 量表上得出等价（±2pp: p=0.017; ±3pp: p=0.003），但在 logit 量表上直到 ±4pp 才得出等价（Table 10）。论文选择 probability 量表为 "primary analysis"，理由是 "accuracy values of 0.37-0.66 reside in the mid-range"。但：
  - 准确率 0.37 对应 logit ≈ -0.53，非线性已非可忽略
  - Logit 量表的交互效应（0.111 logit units, p=0.047）达到边缘显著——这与 probability 量表上的 "negligible interaction" 叙事矛盾
  - 两个量表的 TOST 在关键 margin (±2-3pp) 上给出相反结论，说明 "count 和 BCS 效应是可加的" 这一 claim 处于刀刃上
- 建议：(a) 在 main text 中明确报告两个量表的 TOST 结论差异（目前仅在附录中提及 logit 结果）；(b) 讨论在什么条件下选择哪个量表更合适；(c) 将 "additive" claim 弱化为 "approximately additive on the probability scale, with some evidence of interaction on the logit scale"。

**W4** [Major] **Abstract 和 Introduction 对相关性证据使用因果语言**

- 具体位置：Abstract ("confusability drives type substitution errors")、§1 ("confusability-driven substitution is documented primarily in RE")
- 问题：论文的核心证据是 correlational evidence with controlled stratification（§6 也诚实承认）。"drives" 一词暗示因果关系，超出了证据支撑范围。§6 正确地指出 "mechanistic analysis at the attention or logit level is needed to confirm the causal pathway"，但这与 abstract 中的 "drives" 矛盾。
- 建议：将 "drives" 替换为 "is associated with" 或 "predicts"——后者在统计学中有明确含义且不暗示因果。

**W5** [Major] **Greedy batch 构造可能引入 BCS 之外的系统偏差（domain concentration confound）**

- 具体位置：§3.3 Experiment 2、Appendix O
- 问题：High-BCS batch 的 greedy 构造倾向于选择语义相近的类型（如都是 person-related relations），形成 domain-concentrated batches。这类 batch 的抽取难度可能不仅因为 confusability，还因为：
  - 同一语义域的关系共享语言模式，使 LLM 更难区分
  - 实体在同一域内的指代方式更相似
  - 这种效应在 pairwise BCS 之上可能独立存在（超越了 pairwise metric 的捕获能力）
- Appendix O 通过 per-type solo difficulty 分析部分缓解了这一担忧（BCS unique R²=0.259），但 solo difficulty 不能捕获 cluster-level 的 domain concentration 效应。
- 建议：(a) 报告 high-BCS 和 low-BCS batches 的 type domain 分布（例如 FewRel 的 relation 类别统计）；(b) 考虑构造 matched batches——在 domain distribution 相似的条件下变化 BCS。

**W6** [Major] **共享 text instances 的 bootstrap 依赖性问题**

- 具体位置：§3.3 ("evaluate the same 1,000 text samples across all batches")、§4.3、Limitations ("Across-batch correlation")
- 问题：BCS-controlled 实验中，不同 batch 评估同一组 1,000 个 text samples（不同 batch 的 gold-positive 子集不同）。同一 text instance 在不同 type composition 下的抽取难度是相关的（instance difficulty 是共享因素），但 batch-level bootstrap 将每个 batch 的 accuracy 视为独立观测。这导致 bootstrap CI 可能反保守（anti-conservative）。
- Limitations 中提到 "type composition is independently sampled per batch"，但 text instance 层面的依赖性未被 batch-level bootstrap 正确处理。
- Appendix R（variance decomposition）显示 batch variance 远大于 seed variance，表明 type composition 是主要方差来源，部分缓解了这一担忧。但未量化 instance-level correlation 对 CI 宽度的影响。
- 建议：(a) 使用 cluster-robust standard errors（以 text instance 为 cluster）作为 robustness check；(b) 或者报告 batch-level vs. instance-level variance 分解以量化依赖性的影响。

---

## 小问题（不影响接收）

**M1** [Minor] **页数合规性：Section 6 似乎延伸至第 9 页开头 1-2 行**
- 具体位置：p.8 末尾 → p.9 开头
- Section 6 最后一句 "fails (§5), but oracle routing recovers accuracy (72.4% vs. 50.4%), confirming that count and confusability are independently addressable" 出现在 page 9 顶部，紧接 Limitations。技术上 main text 超出 8 页（约 1-2 行），虽然极度边缘，但严格而言属于 formatting violation。
- 建议：通过微调措辞或压缩 Section 5-6 将 main text 严格控制在 8 页内。

**M2** [Minor] **NER null result 的 framing 偏向 "低 power" 解释，未充分考虑 "真正无效应" 的可能**
- 具体位置：§4.1、§4.3、Appendix E.2、Limitations #2
- 问题：NER BCS null 在两个 prompt 版本（v1, v2）、三个模型（Qwen3-32B, LLaMA-8B, LLaMA-70B）上一致复现，且 error taxonomy（Figure 2）显示 NER 的错误模式与 RE 根本不同。这些证据更倾向于 "NER 的 batch-level confusability 效应确实不存在或极弱"，而非 "power 不足无法检测"。
- 建议：平衡呈现两种解释——(a) BCS range 过窄导致 power 不足，(b) NER 的错误机制（boundary detection、type distribution 等）与 RE 根本不同，confusability 在 NER 中可能主要通过其他路径（如 type-level IntraSub 而非 batch-level BCS）发挥作用。

**M3** [Minor] **多重比较未做正式校正**
- 具体位置：Limitations ("core claims rest on p < 0.001")
- 问题：论文在 4 个数据集 × 多个分析 × 多个模型上运行大量检验，仅以 "核心 claim 基于 p < 0.001" 作为非正式校正。虽然实际上大多数核心发现确实 p < 0.001，但对边缘结果（如 logit-scale TOST p=0.047, Table 10）缺乏校正可能影响结论稳健性。
- 建议：至少对 main text 中引用的 p-values 报告 Bonferroni 或 Holm-corrected 值作为 sensitivity check。

---

## Questions（需要作者澄清）

**Q1.** 能否在一个 BCS-centrality VIF 适中（比如 VIF < 5）的新数据集上重复 BCS-controlled 实验？这将大大增强 BCS 度量泛化性的证据。

**Q2.** Table 12 中 DocRED VIF=50.9 的 partial correlation p < 0.001 ——在如此极端的 multicollinearity 下，这个 p-value 是否经过了 variance inflation 的适当调整？能否报告 ridge regression 或 PCA-based partial correlation 作为 robustness check？

**Q3.** BCS-controlled 实验的 high-BCS batches 中，relation type 是否系统性地集中在特定语义域（如 person-related, location-related）？能否报告 extreme batches 的 type domain 分布统计？

**Q4.** 论文用 "the same 1,000 text samples across all batches" 但不同 batch 的 gold-positive 子集不同。跨 batch 共享 text instances 对 bootstrap CI 的宽度有多大影响？能否用 split-sample bootstrap（每个 batch 使用独立 text sample）验证 CI 的稳健性？

**Q5.** NER batch-level BCS null 在所有模型和 prompt 上一致复现——作者是否认为这更可能反映 NER 任务本身的特性（而非仅仅是 power 不足）？如果是，BCS 度量的适用范围是否应限定为 RE 和 ED？

**Q6.** Probability-scale TOST 在 ±3pp 给出等价，logit-scale 在 ±3pp 给出 inconclusive（Table 10）。如果 logit scale 更适合 bounded accuracy metrics（这是统计学界的通常建议），"additive" claim 是否需要弱化？

---

## Missing References

未发现明显遗漏的关键相关工作。论文的 Related Work（§2）和 References 覆盖了 schema complexity in IE、LLM-based extraction、confusability metrics 的主要文献。

---

## 主要优势（总结）

1. BCS-controlled batch design 是 schema complexity 研究中真正的方法论创新
2. Count 退化的实证基础极其扎实——4 数据集、3 任务、4 模型一致
3. 对 null results 和 confounders 的报告达到了罕见的透明度
4. 附录的详尽程度堪称典范（从 factorial analysis 到 variance decomposition 到 prompt sensitivity）
5. 写作质量高，结构清晰，密度大但可读性好

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2932 · 2026-05-22T04:24:06.471406+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1（方法严谨性）的完整审稿原文。请逐条回应：对每个 Weakness/Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 1 评分\n- Soundness: 3.5/5\n- Excitement: 3/5\n- Overall: 3.5/5 (Borderline Conference)\n- Confidence: 4/5\n\n### Reviewer 1 Strengths\n- S1: BCS-controlled batch design 是真正的方法论创新\n- S2: 异常透明和诚实的报告（NER null, centrality confound, MAVEN）\n- S3: 极其详尽的附录（A-Y）\n- S4: 多模型验证方向正确（Qwen3-32B + LLaMA-8B/70B + Gemini Flash）\n- S5: Count 退化的实证基础扎实（4 数据集一致）\n\n### Reviewer 1 Must-Fix (Critical)\n\n**W1: BCS 度量的干净证据仅限 FewRel RE 一个数据集，但论文叙事暗示更广泛的适用性**\n- FewRel RE: VIF=1.18, R²=0.22 — 唯一干净证据\n- DocRED RE: VIF=50.9, BCS-centrality r=0.99, partial correlation 不可信\n- MAVEN ED: BCS-accuracy 完全归因于 centrality confound\n- Few-NERD NER: batch-level BCS-F1 null\n- 建议：abstract/intro 明确区分 count 退化（4 数据集）和 BCS 效应（仅 FewRel 干净）\n\n**W2: DocRED VIF=50.9 的处理不充分**\n- VIF>10 已属严重多重共线性；VIF=50.9 下 partial correlation 标准误膨胀 ~7 倍\n- DocRED 仍出现在 §4.3 main text 结果中，可能误导读者\n- 建议：main text 明确标注 DocRED BCS 不可解释，或使用 ridge regression/PCA\n\n### Reviewer 1 Should-Fix (Major)\n\n**W3: TOST 等价性检验结论依赖量表选择**\n- Probability scale: ±3pp TOST p=0.003（等价）\n- Logit scale: ±3pp TOST inconclusive; logit 交互效应 p=0.047（边缘显著）\n- 两个量表在关键 margin 给出相反结论\n\n**W4: Abstract/Introduction 对相关性证据使用因果语言**\n- \"drives\" 暗示因果关系，超出 correlational evidence 支撑范围\n- 建议替换为 \"predicts\" 或 \"is associated with\"\n\n**W5: Greedy batch 构造可能引入 domain concentration confound**\n- High-BCS batch 倾向选择同一语义域的类型\n- Solo difficulty 不能捕获 cluster-level domain concentration\n- 建议报告 extreme batches 的 type domain 分布\n\n**W6: 共享 text instances 的 bootstrap 依赖性问题**\n- 不同 batch 评估同一 1000 个 text samples，instance-level correlation 未被 bootstrap 处理\n- Bootstrap CI 可能 anti-conservative\n- 建议使用 cluster-robust standard errors 或 split-sample bootstrap\n\n### Reviewer 1 Minor\n- M1: 页数可能超出 8 页（Section 6 延伸至 p.9 开头 1-2 行）\n- M2: NER null framing 偏向 \"低 power\" 解释，未充分考虑 \"真正无效应\"\n- M3: 多重比较未做正式校正\n\n### Reviewer 1 Questions\n- Q1: 能否在 VIF 适中的新数据集上重复 BCS-controlled 实验？\n- Q2: DocRED VIF=50.9 的 partial correlation p-value 是否经过 variance inflation 调整？\n- Q3: High-BCS batches 中 relation type 是否集中在特定语义域？\n- Q4: 跨 batch 共享 text instances 对 bootstrap CI 宽度的影响？\n- Q5: NER null 是否更可能反映任务特性而非 power 不足？\n- Q6: Logit scale 通常更适合 bounded metrics——\"additive\" claim 是否需弱化？\n\n---\n\n请逐条回应以上 W1-W6、M1-M3、Q1-Q6。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1（方法严谨性）的完整审稿原文。请逐条回应：对每个 Weakness/Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 1 评分\n- Soundness: 3.5/5\n- Excitement: 3/5\n- Overall: 3.5/5 (Borderline Conference)\n- Confidence: 4/5\n\n### Reviewer 1 Strengths\n- S1: BCS-controlled batch design 是真正的方法论创新\n- S2: 异常透明和诚实的报告（NER null, centrality confound, MAVEN）\n- S3: 极其详尽的附录（A-Y）\n- S4: 多模型验证方向正确（Qwen3-32B + LLaMA-8B/70B + Gemini Flash）\n- S5: Count 退化的实证基础扎实（4 数据集一致）\n\n### Reviewer 1 Must-Fix (Critical)\n\n**W1: BCS 度量的干净证据仅限 FewRel RE 一个数据集，但论文叙事暗示更广泛的适用性**\n- FewRel RE: VIF=1.18, R²=0.22 — 唯一干净证据\n- DocRED RE: VIF=50.9, BCS-centrality r=0.99, partial correlation 不可信\n- MAVEN ED: BCS-accuracy 完全归因于 centrality confound\n- Few-NERD NER: batch-level BCS-F1 null\n- 建议：abstract/intro 明确区分 count 退化（4 数据集）和 BCS 效应（仅 FewRel 干净）\n\n**W2: DocRED VIF=50.9 的处理不充分**\n- VIF>10 已属严重多重共线性；VIF=50.9 下 partial correlation 标准误膨胀 ~7 倍\n- DocRED 仍出现在 §4.3 main text 结果中，可能误导读者\n- 建议：main text 明确标注 DocRED BCS 不可解释，或使用 ridge regression/PCA\n\n### Reviewer 1 Should-Fix (Major)\n\n**W3: TOST 等价性检验结论依赖量表选择**\n- Probability scale: ±3pp TOST p=0.003（等价）\n- Logit scale: ±3pp TOST inconclusive; logit 交互效应 p=0.047（边缘显著）\n- 两个量表在关键 margin 给出相反结论\n\n**W4: Abstract/Introduction 对相关性证据使用因果语言**\n- \"drives\" 暗示因果关系，超出 correlational evidence 支撑范围\n- 建议替换为 \"predicts\" 或 \"is associated with\"\n\n**W5: Greedy batch 构造可能引入 domain concentration confound**\n- High-BCS batch 倾向选择同一语义域的类型\n- Solo difficulty 不能捕获 cluster-level domain concentration\n- 建议报告 extreme batches 的 type domain 分布\n\n**W6: 共享 text instances 的 bootstrap 依赖性问题**\n- 不同 batch 评估同一 1000 个 text samples，instance-level correlation 未被 bootstrap 处理\n- Bootstrap CI 可能 anti-conservative\n- 建议使用 cluster-robust standard errors 或 split-sample bootstrap\n\n### Reviewer 1 Minor\n- M1: 页数可能超出 8 页（Section 6 延伸至 p.9 开头 1-2 行）\n- M2: NER null framing 偏向 \"低 power\" 解释，未充分考虑 \"真正无效应\"\n- M3: 多重比较未做正式校正\n\n### Reviewer 1 Questions\n- Q1: 能否在 VIF 适中的新数据集上重复 BCS-controlled 实验？\n- Q2: DocRED VIF=50.9 的 partial correlation p-value 是否经过 variance inflation 调整？\n- Q3: High-BCS batches 中 relation type 是否集中在特定语义域？\n- Q4: 跨 batch 共享 text instances 对 bootstrap CI 宽度的影响？\n- Q5: NER null 是否更可能反映任务特性而非 power 不足？\n- Q6: Logit scale 通常更适合 bounded metrics——\"additive\" claim 是否需弱化？\n\n---\n\n请逐条回应以上 W1-W6、M1-M3、Q1-Q6。"
  }
}
```

</details>

---


### Tool result

_source line 2933 · 2026-05-22T04:24:31.749391+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 25277
}
```

</details>

---


### Tool call

_source line 2934 · 2026-05-22T04:24:32.101540+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2（新颖性与完整性）的完整审稿原文。请逐条回应：对每个 Weakness/Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 2 评分\n- Soundness: 3.5/5\n- Excitement: 3/5\n- Overall: 3.5/5 (Borderline Conference)\n- Confidence: 4/5\n\n### Reviewer 2 Strengths\n- S1: BCS-controlled batch 设计是真正的方法论贡献\n- S2: 统计严谨度显著高于同类工作\n- S3: 诚实报告负面结果（NER null, SDGD failure）\n- S4: 跨任务、跨模型、跨数据集覆盖面广\n- S5: Practical implications 具体可操作\n\n### Reviewer 2 Major Weaknesses\n\n**W1: SCS/BCS 相对于 LLM-PEE (Liu et al., 2025) 的技术新颖性不足**\n- 核心指标就是 embedding cosine similarity，继承自 LLM-PEE\n- BCS 是 batch 级 max 聚合\n- 论文声称贡献在 controlled methodology 而非指标本身\n- 质疑：如果指标不新，\"用已有指标做更好实验\"是否足够支撑 conference-level？\n- 建议：Section 3.2 更明确阐述 SCS/BCS 的技术差异点\n\n**W2: Confusability 发现过度依赖 FewRel，多任务叙事被削弱**\n- NER: BCS 效应为 null（三个模型一致）\n- MAVEN: BCS 被 degree centrality 完全混淆\n- DocRED: VIF=50.9 证据不可靠\n- 核心证据基本仅来自 FewRel（R² ≈ 0.22）\n- 建议：限定 confusability 发现的适用范围\n\n**W3: \"First controlled study\" claim 需要更审慎表述**\n- Chen et al. (2026) 也量化了 schema complexity 对 zero-shot NER 的影响\n- GoLLIE (2024, ICLR) 隐式控制了 schema 对 IE 的影响\n- \"Reflect then Learn\" (Zhang et al., AAAI 2026) 研究了 introspective confusion\n- 建议：限定为 \"first controlled study simultaneously isolating count and inter-type confusability as independent dimensions\"\n\n### Reviewer 2 Minor Weaknesses\n\n**W4: SDGD Section 5 在正文的定位不当**\n- 用一整个 section 报告失败的方法，挤压其他内容空间\n- 建议降级为 appendix 或更深入分析改进方向\n\n**W5: Discussion/Conclusion 对理论 implications 展开不足**\n- 缺少深层讨论：为什么 embedding similarity 能预测 LLM type confusion？\n- 模型的\"自我认知\"能否预测其行为？\n\n**W6: 写作细节**\n- Abstract 中 SCS 定义不够具体\n- DocRED 处理不平衡\n- Table 1 \"not comparable across embedding models\" 限制未充分讨论\n\n### Reviewer 2 Questions\n- Q1: Name-only vs name+definition embedding 对 NER null 的影响？\n- Q2: Mean vs max BCS 聚合对 headline R²=0.22 的敏感性？\n- Q3: Factorial interaction 如果存在，对 \"independently addressable\" claim 的影响？\n- Q4: SDGD 阈值 τ 的选择标准？\n- Q5: 更大的 frontier models 是否可能减弱 confusability 效应？\n\n### Reviewer 2 Missing References\n1. \"Reflect then Learn\" (Zhang et al., AAAI 2026) — introspective confusion\n2. \"Diagnosing Structural Failures in LLM-Based Evidence Extraction\" (arXiv 2602.10881)\n3. \"NER Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings\" (Findings EMNLP 2025)\n4. \"Show Less, Instruct More\" (2024) — definition quality for zero-shot NER\n\n---\n\n请逐条回应以上 W1-W6、Q1-Q5。特别关注：你是否同意 Reviewer 2 关于 SCS/BCS 新颖性不足的判断？以及 SDGD section 是否应降级为 appendix？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2（新颖性与完整性）的完整审稿原文。请逐条回应：对每个 Weakness/Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 2 评分\n- Soundness: 3.5/5\n- Excitement: 3/5\n- Overall: 3.5/5 (Borderline Conference)\n- Confidence: 4/5\n\n### Reviewer 2 Strengths\n- S1: BCS-controlled batch 设计是真正的方法论贡献\n- S2: 统计严谨度显著高于同类工作\n- S3: 诚实报告负面结果（NER null, SDGD failure）\n- S4: 跨任务、跨模型、跨数据集覆盖面广\n- S5: Practical implications 具体可操作\n\n### Reviewer 2 Major Weaknesses\n\n**W1: SCS/BCS 相对于 LLM-PEE (Liu et al., 2025) 的技术新颖性不足**\n- 核心指标就是 embedding cosine similarity，继承自 LLM-PEE\n- BCS 是 batch 级 max 聚合\n- 论文声称贡献在 controlled methodology 而非指标本身\n- 质疑：如果指标不新，\"用已有指标做更好实验\"是否足够支撑 conference-level？\n- 建议：Section 3.2 更明确阐述 SCS/BCS 的技术差异点\n\n**W2: Confusability 发现过度依赖 FewRel，多任务叙事被削弱**\n- NER: BCS 效应为 null（三个模型一致）\n- MAVEN: BCS 被 degree centrality 完全混淆\n- DocRED: VIF=50.9 证据不可靠\n- 核心证据基本仅来自 FewRel（R² ≈ 0.22）\n- 建议：限定 confusability 发现的适用范围\n\n**W3: \"First controlled study\" claim 需要更审慎表述**\n- Chen et al. (2026) 也量化了 schema complexity 对 zero-shot NER 的影响\n- GoLLIE (2024, ICLR) 隐式控制了 schema 对 IE 的影响\n- \"Reflect then Learn\" (Zhang et al., AAAI 2026) 研究了 introspective confusion\n- 建议：限定为 \"first controlled study simultaneously isolating count and inter-type confusability as independent dimensions\"\n\n### Reviewer 2 Minor Weaknesses\n\n**W4: SDGD Section 5 在正文的定位不当**\n- 用一整个 section 报告失败的方法，挤压其他内容空间\n- 建议降级为 appendix 或更深入分析改进方向\n\n**W5: Discussion/Conclusion 对理论 implications 展开不足**\n- 缺少深层讨论：为什么 embedding similarity 能预测 LLM type confusion？\n- 模型的\"自我认知\"能否预测其行为？\n\n**W6: 写作细节**\n- Abstract 中 SCS 定义不够具体\n- DocRED 处理不平衡\n- Table 1 \"not comparable across embedding models\" 限制未充分讨论\n\n### Reviewer 2 Questions\n- Q1: Name-only vs name+definition embedding 对 NER null 的影响？\n- Q2: Mean vs max BCS 聚合对 headline R²=0.22 的敏感性？\n- Q3: Factorial interaction 如果存在，对 \"independently addressable\" claim 的影响？\n- Q4: SDGD 阈值 τ 的选择标准？\n- Q5: 更大的 frontier models 是否可能减弱 confusability 效应？\n\n### Reviewer 2 Missing References\n1. \"Reflect then Learn\" (Zhang et al., AAAI 2026) — introspective confusion\n2. \"Diagnosing Structural Failures in LLM-Based Evidence Extraction\" (arXiv 2602.10881)\n3. \"NER Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings\" (Findings EMNLP 2025)\n4. \"Show Less, Instruct More\" (2024) — definition quality for zero-shot NER\n\n---\n\n请逐条回应以上 W1-W6、Q1-Q5。特别关注：你是否同意 Reviewer 2 关于 SCS/BCS 新颖性不足的判断？以及 SDGD section 是否应降级为 appendix？"
  }
}
```

</details>

---


### Tool result

_source line 2935 · 2026-05-22T04:24:33.610272+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1508
}
```

</details>

---


### Assistant

_source line 2936 · 2026-05-22T04:24:37.907597+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 243

## Round 243

2 recorded events


### User

_source line 2937 · 2026-05-22T04:24:40.513456+00:00_

[Reviewer 1 审稿结果]:
审稿完成。

**评分**: Overall 3.5 (Borderline Conference), Soundness 3.5, Excitement 3, Confidence 4

**核心判断**: Count 退化故事扎实（4 数据集一致），但 BCS 度量的干净证据仅限 FewRel RE 一个数据集。两个 Critical 问题：(1) 4 个数据集中 3 个的 BCS 证据存在严重问题（DocRED VIF=50.9 multicollinearity、MAVEN 完全归因于 centrality confound、NER null），论文叙事暗示的适用范围超出证据支撑；(2) DocRED 的 partial correlation 在 VIF=50.9 下不可信但仍作为支持证据呈现。另有 TOST 量表依赖性、因果语言、batch 构造 confound、bootstrap 依赖性等 Major 问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2938 · 2026-05-22T04:24:47.629487+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 244

## Round 244

2 recorded events


### User

_source line 2939 · 2026-05-22T04:26:19.499085+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 对 Reviewer 1 审稿意见

---

### Must-Fix (Critical)

**[AGREE] R1-W1: BCS 干净证据仅限 FewRel RE**

完全同意。这与我的 W2 一致。逐数据集审查：
- FewRel RE: R²=0.22, VIF=1.18（Table 12, Appendix E.1）——唯一 confound-free 证据
- DocRED RE: VIF=50.9，partial correlation 不可信（见下 W2 讨论）
- MAVEN ED: controlling for degree centrality 后 BCS 变 non-significant（Table 11, Appendix E.1）
- Few-NERD NER: 三个模型的 BCS-F1 correlation 全部 null（Table 5, p.6）

论文 abstract 的 "inter-type confusability drives type substitution errors" 和 Introduction 的 "BCS explains ∼22% of cross-batch RE accuracy variance on FewRel" 虽然后者有限定，但前者的泛化语气与证据不匹配。Count 退化的 4 数据集一致性（Figure 1, Tables 3/23/24）与 BCS 效应的 FewRel 单数据集性质形成鲜明对比。作者应在 abstract/intro 中明确这一不对称性。

**[AGREE] R1-W2: DocRED VIF=50.9 处理不充分**

同意，且这一点我在初审时未充分展开。VIF=50.9 意味着 partial correlation 的标准误膨胀约 √50.9 ≈ 7.1 倍，此条件下的 p-value 几乎不可解释。Table 12（Appendix E.1）报告 DocRED partial correlation remains "highly significant"（VIF=50.9, p<0.001），但这个 p-value 的可靠性值得严重质疑。

更关键的是：§4.3（p.6）main text 报告 DocRED BCS 结果时写道 "the substantially higher R² relative to FewRel (0.218) largely reflects BCS-centrality collinearity"——这句话虽然承认了问题，但仍然在正文报告了这个 R² 数值，可能给粗读读者造成"DocRED 效应更强"的错误印象。R1 建议的 ridge regression 或 PCA 是合理的替代方案。

---

### Should-Fix (Major)

**[AGREE] R1-W3: TOST 等价性检验的量表依赖性**

同意这是一个实质性问题。Appendix C（Table 10, p.14-15）在 probability scale 上 ±3pp TOST 给出 equivalence 结论（p=0.003），但 logit scale 上同一 margin 的交互效应 p=0.047（边缘显著），TOST 则 inconclusive。这意味着 "count 和 confusability independently addressable"（论文核心 claim 之一）的支撑取决于量表选择。

对于 bounded metrics（accuracy 在 [0,1] 区间），logit transformation 通常是更理论合理的选择，因为它消除了 ceiling/floor effects 并使误差分布更接近正态。如果 logit scale 上交互效应边缘显著，这暗示 confusability 的效应大小可能随 count 水平而变——高 count 时 confusability 效应可能更大（或反之），这与 "independent" claim 矛盾。作者至少应将此作为 caveat 在正文中报告。

**[AGREE] R1-W4: 因果语言超出证据支撑**

同意。Abstract 中 "type count drives recall decline" 和 "inter-type confusability drives type substitution errors" 中的 "drives" 暗示因果机制。虽然 BCS-controlled 设计比纯观测研究更接近因果推断（通过人工控制 batch composition），但这仍非 randomized intervention——batch 构造是确定性的（基于 SCS matrix），而非随机分配。 "predicts" 或 "is associated with" 更准确。

补充一点 R1 未提及的：Section 6（p.8）使用 "confusability effect arises from schema composition, not prompt-specific phrasing" 这一表述也接近因果 claim。Cross-prompt validation（Appendix H）确实提供了跨 prompt 的稳健性证据，但 "arises from" 仍然是因果语言。

**[REBUT] R1-W5: Greedy batch 构造的 domain concentration confound**

部分反驳。R1 的担忧有道理（high-BCS batches 可能集中于同一语义域），但论文提供了部分证据来缓解这一担忧：

1. **FewRel 的 balanced design**（§3.1, p.3）："FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound"——这意味着每个 relation type 的 instance 数量相同，domain concentration 不会通过 frequency 通道影响结果。

2. **Within-pool controlled comparison**（Appendix L, p.20）报告 within-pool analysis confirms slope consistency across pools（permutation p = 0.60），暗示 80-relation extreme-batch 的 BCS range 反映的是 within-pool 的 confusability 差异而非跨 pool 的 domain 差异。

3. **Cross-prompt validation**（Appendix H, p.18-19）在 v1 和 v2 两种 prompt 下 BCS-accuracy 关系方向一致，如果效应完全归因于 domain concentration，更换 prompt 格式不太可能保持一致。

但我承认这些证据是间接的。R1 建议直接报告 extreme batches 的 type domain 分布是一个低成本高信息量的建议，应当采纳。

**[AGREE] R1-W6: 共享 text instances 的 bootstrap 依赖性**

同意这是一个有效的统计关切。§3.3（p.4）描述 "evaluate the same 1,000 text samples across all batches"——不同 batch 共享完全相同的 text instances。标准 bootstrap（resample batches independently）不能捕获 instance-level 的跨 batch 相关性。

影响方向取决于相关结构：如果某些 text instances 对所有 batch 都难（或都易），batch-level accuracy estimates 之间存在正相关，standard bootstrap CIs 会偏窄（anti-conservative）。R1 建议的 cluster-robust standard errors（以 text instance 为 cluster）是合理的修正方案。

不过，实际影响可能有限：(1) batch composition 变化大（25 types per batch, 不同 type 组合），instance-level correlation 可能较弱；(2) Appendix J（p.19-20, Table 15）报告的 BCS aggregation sensitivity 分析和 Appendix L 的 within-pool comparison 提供了部分 robustness 证据。但形式上 R1 的批评成立。

---

### Minor

**[REBUT] R1-M1: 页数可能超出 8 页**

根据我对 PDF 的逐页审查：Section 6（Discussion and Conclusion）结束于 page 8 底部，Limitations 从 page 9 开始。ACL 2026 guidelines 明确 "Mandatory limitations and optional ethical considerations do not count towards this page limit"。Section 6 作为正文最后一节确实写到 page 8 的最底部，但未观察到 Section 6 内容溢出到 page 9。如果确实有 1-2 行溢出，这是作者需要在 camera-ready 修正的格式问题，但不影响实质审查。建议 R1 精确标注溢出行的内容以便确认。

**[AGREE] R1-M2: NER null framing 偏向 power 解释**

同意。Appendix E.2 详细论证了 power 不足（detectable |r|=0.11 at n=25 需要 n≈150），但论文未充分考虑替代假设：NER confusability 可能通过不同于 RE 的机制运作。NER 涉及 span boundary detection + type classification，而 RE 的输入已经是 identified entity pairs。Type confusion 在 NER 中可能被 span detection errors 稀释——即使两个类型的 embedding 相似，如果 span 检测本身就是主要错误来源，BCS 的预测力会被遮蔽。

此外，Table 31（Appendix Z, p.27）的 relaxed matching 分析显示 BCS 在 NER 上仍然近乎 null（Pearson r 接近 0），进一步暗示这可能不仅是 power 问题。作者应在正文中至少提及 "NER 任务特性可能导致 confusability 通过不同通道表现" 这一替代解释。

**[AGREE] R1-M3: 多重比较未做正式校正**

同意。论文在 Limitations（p.9）提到 "we report individual p-values"，但对于跨 4 数据集、3 模型、多个 count levels 的大量检验，uncorrected p-values 增加了 Type I error 风险。特别是一些 "marginal significance"（如 logit scale 交互效应 p=0.047）在 Bonferroni/BH 校正后很可能变为 non-significant。

不过，论文的核心 claims（count degradation, FewRel BCS R²=0.22）的效应量足够大，不太可能被多重比较校正推翻。更受影响的是那些边缘结果的解读。

---

### Questions 回应

**[AGREE] R1-Q1**: 在 VIF 适中的新数据集上重复 BCS-controlled 实验是加强论文最直接的路径。当前仅 FewRel（VIF=1.18）提供干净证据，增加一个独立数据集会显著提升可信度。

**[AGREE] R1-Q2**: DocRED VIF=50.9 下的 p-value 确实需要 variance inflation 调整或替代方法（ridge regression）。当前报告的 p<0.001 在 VIF=50.9 下不可靠。

**[AGREE] R1-Q3**: 这与 W5 相关。直接报告 high-BCS batches 的 relation type 语义域分布是低成本高价值的信息。如果 high-BCS batches 集中于 kinship 或 spatial relations 等特定域，需要考虑 domain-specific difficulty 这一替代解释。

**[AGREE] R1-Q4**: 跨 batch 共享 text instances 的 bootstrap 影响值得量化。一个简单检验：对比 split-sample bootstrap（每个 batch 用不同的 500 text instances）和 full-sample bootstrap 的 CI 宽度，如果差异不大，说明依赖性影响可忽略。

**[AGREE] R1-Q5**: 如我在 M2 回应中所述，NER null 更可能反映任务特性（span detection dominates type classification error）而非纯粹 power 不足。Table 31 的 relaxed matching 结果支持这一解读。作者应在正文中讨论这一可能性。

**[REBUT] R1-Q6: Logit scale 是否必然更合适**

部分反驳。R1 正确指出 logit scale 对 bounded metrics 更理论合理，但论文在 Appendix C（p.14）实际上已经做了 logit-scale 分析并报告了两种结果。"Additive" claim 确实更适合在 probability scale 上的中间范围成立（论文数据大多在 0.3-0.8 范围），此时 probability 和 logit 的差异较小。

更重要的是，论文的 practical claim 是面向 practitioners 的（"count 和 confusability 可以独立处理"），probability scale 对 practitioners 更直观。但论文确实应弱化 "independently addressable" 的措辞，改为 "approximately additive on the probability scale within the observed range"，并在正文中注明 logit scale 上的边缘交互。

---

### 总结

与 R1 在绝大多数问题上一致。核心共识：
1. **BCS 证据的 FewRel 局限性**是最关键的问题（R1-W1 = 我的 W2）
2. **DocRED VIF=50.9** 需要更严肃的处理（R1-W2）
3. **因果语言**需修正（R1-W4 = 我的隐含关切）
4. **NER null 的解释**应更平衡（R1-M2）

唯一实质分歧在 **W5（domain concentration）**：我认为论文的 balanced design 和 cross-prompt validation 提供了部分缓解证据，但仍建议作者直接报告 domain 分布。

评分维持不变：Overall 3.5/5（Borderline Conference），Confidence 4/5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2940 · 2026-05-22T04:26:28.907401+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 245

## Round 245

10 recorded events


### User

_source line 2941 · 2026-05-22T04:26:30.074637+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

### Major Weaknesses 回应

**[AGREE] R2-W1: SCS/BCS 相对于 LLM-PEE 的技术新颖性不足**

同意核心判断。SCS 本质上就是 embedding cosine similarity，论文自己也承认继承自 LLM-PEE（§2, p.3: "SCS inherits the embedding-similarity criterion from LLM-PEE"）。BCS 的 max 聚合（§3.2）技术含量有限。

但我要补充一个区分：**指标不新 ≠ 方法论不新**。BCS-controlled batch design（§3.3, Experiment 2）——固定 count、greedy 构造 extreme-BCS batches 来隔离 confusability——这个实验范式本身是新的，且有方法论价值。问题是这个贡献够不够 conference-level。我认为如果 BCS 在多个数据集上都有干净证据，"旧指标+新实验范式+广泛验证" 足以支撑 conference paper。但正如我在 R1-W1 中指出的，干净证据仅限 FewRel，这使得 novelty 和 evidence 同时偏弱。

R2 建议 "Section 3.2 更明确阐述技术差异点" 是合理的，但我认为更关键的是增强实证覆盖——如果 BCS 在更多数据集上 work，novelty 问题就不那么突出。

**[AGREE] R2-W2: Confusability 发现过度依赖 FewRel**

完全同意，这与我的 R1-W1 (Critical) 判断一致。逐数据集梳理：

- FewRel: 干净（VIF=1.18, Table 12）——唯一可靠证据
- DocRED: VIF=50.9（Table 12），不可解释——我在 R1-W2 中详细论证了为什么 partial correlation 在此条件下不可信
- MAVEN: BCS-accuracy 完全归因于 centrality（Appendix E.1: "Under joint control, both embeddings yield p > 0.2"）
- Few-NERD NER: Null（§4.1, §4.3），且跨模型、跨 prompt 一致复现

R2 和我在这一点上完全收敛。这是本文最核心的方法论弱点。

**[REBUT] R2-W3: "First controlled study" claim 需要更审慎表述**

部分反驳。R2 引用的三个工作与本文的 claim 有明确区别：

- **Chen et al. (2026)** 量化 schema complexity 对 zero-shot NER 的影响，但据论文引用方式（§2: "Chen et al. (2025) show that instance count degrades LLM multi-instance processing"），其 focus 是 instance count / multi-instance processing，并非同时隔离 count 和 inter-type confusability 两个维度。
- **GoLLIE (2024, ICLR)** 通过 annotation guidelines 控制 schema 对 IE 的影响，但这是一种 training-time 干预（使用 guidelines 作为 prompt），不是 post-hoc controlled experiment 来量化 confusability 效应。
- **"Reflect then Learn" (Zhang et al., AAAI 2026)** 研究 introspective confusion，但 introspection 是让 LLM 自己识别混淆，而非通过 embedding similarity 外部度量+controlled batch 来隔离变量。

本文的特定 claim 是 "first controlled study **simultaneously** isolating count and inter-type confusability as **independent** dimensions"（§1）。上述工作都没有同时做到 (a) 用 embedding-based metric 量化 confusability，(b) 通过 controlled batch design 在固定 count 下变化 confusability。

**但 R2 的建议仍然合理**——将 claim 限定为 "first controlled study simultaneously isolating count and inter-type confusability as independent dimensions using embedding-based metrics and controlled batch design" 会更精确，避免被误读为泛化到所有 schema complexity 研究。这是措辞精度问题，不是 claim 本身的错误。

---

### Minor Weaknesses 回应

**[REBUT] R2-W4: SDGD Section 5 应降级为 appendix**

不同意。理由：

1. **Section 5 是论文叙事弧的关键环节。** 论文的逻辑是：schema complexity 导致退化（§4）→ 自然解法是 schema decomposition → decomposition 失败且原因可诊断（§5）→ 两个维度可独立处理（§6）。如果去掉 §5，叙事断裂——读者自然会问 "如果 BCS 预测退化，那降低 BCS（即分解 schema）能否解决？"
2. **负面结果+诊断是实质贡献。** Merge amplification（presenting text k times collapses predictions, §5）和 routing failure（oracle 恢复 72.4% vs. 50.4%, §5）的诊断不是简单的 "方法失败"报告，而是揭示了 decompose-then-merge 范式的根本局限——这对后续工作有直接指导价值。
3. **空间问题可以通过压缩解决。** Section 5 目前约 0.7 column，确实可以更精简（例如将 SDGD 算法细节移入附录，main text 只保留核心发现和诊断）。但解法是压缩，不是移除。

**[AGREE] R2-W5: Discussion 对理论 implications 展开不足**

同意。论文在 §6 说 "mechanistic analysis at the attention or logit level is needed to confirm the causal pathway"，但没有讨论一个更基本的问题：**为什么静态 embedding similarity（Qwen3/MiniLM 的 type name embedding）能预测动态 LLM inference 中的 type confusion？** 可能的解释包括：

- LLM 的 type representation 本身就依赖于类似的 embedding 空间
- Confusability 反映了 type 定义在自然语言中的固有语义重叠，而非模型特异性
- Appendix E.1 Table 12 中 Qwen3 和 MiniLM 编码了同一 confound 的不同方面，这暗示 confusability 可能是数据属性而非模型属性

缺少这一层讨论使论文停留在 "什么在发生" 而未触及 "为什么发生"，限制了理论贡献。

**[AGREE] R2-W6: 写作细节**

同意全部三点。特别是 DocRED 处理不平衡的问题——main text 对 DocRED VIF=50.9 的讨论不充分（我在 R1-W2 中也指出），读者如果不读附录会高估 DocRED 证据的可靠性。

---

### Questions 回应

**[AGREE] R2-Q1: Name-only vs name+definition 对 NER null 的影响**

好问题。Appendix M（Table 20）确实比较了 name-only vs name+definition，但仅报告了 SCS 预测 confusion 的相关系数，未单独报告 name+definition embedding 下的 batch-level BCS-accuracy 分析。如果 type definition 包含更丰富的语义信息，BCS 可能在 NER 上从 null 变为 detectable。这是一个作者应该回应的实验缺口。

**[AGREE] R2-Q2: Mean vs max BCS 聚合对 R²=0.22 的敏感性**

Appendix I（Table 15, p.19）已比较了 mean vs max aggregation，结论方向一致。但 R2 的关切是合理的——应在 main text 中明确报告 mean-BCS 下的 R² 值，让读者不必翻附录即可评估 headline number 的稳健性。据 Table 15，mean 和 max 给出相似的 correlation 强度，所以 R²=0.22 对聚合方式不太敏感。

**[AGREE] R2-Q3: Factorial interaction 对 "independently addressable" claim 的影响**

与我的 R1-W3 高度相关。如果 logit-scale interaction 确实存在（p=0.047, Table 10），"independently addressable" 需要弱化为 "approximately additive on the probability scale"。论文 §6 的 "independently addressable" 表述过于绝对——Appendix C 的 TOST sensitivity analysis 显示这个 claim 在量表选择上处于刀刃。

**[REBUT] R2-Q4: SDGD 阈值 τ 的选择标准**

Appendix B（p.13）描述了 SDGD 使用 LARGEST_FIRST greedy graph coloring，构建 thresholded confusability graph G = (V, E)，其中 edge (t_i, t_j) 当且仅当 SCS(t_i, t_j) > τ。但 τ 的选择并非任意：论文测试了多个策略（single_pass, sdgd_zero, random_batch, per_type），Table 8（p.14）显示 **所有** decomposition modes 都产生低于 single-pass baseline 的 F1，且 Table 9 详细比较了不同 routing strategies。因此 SDGD 失败不是 τ 敏感性问题——是根本性的 merge amplification 问题。τ 的具体值对核心结论影响有限。

**[AGREE] R2-Q5: 更大的 frontier models 是否减弱 confusability 效应**

合理推测。论文在 Appendix U（Table 24-25）测试了 Gemini 2.5 Flash，显示 higher baseline accuracy（90.5% vs. Qwen3-32B 的 ~82%）但 degradation pattern 仍然存在（BCS gap 仍显著）。LLaMA-70B（Appendix S）也显示类似退化。但论文未测试 truly frontier models（GPT-4o, Claude 3.5 Sonnet 等），这些模型可能因更强的 in-context 能力而减弱 confusability 效应。Limitations #1（p.9）承认了这一点但未深入讨论。这是论文泛化性的一个合理质疑。

---

### Missing References 回应

1. **"Reflect then Learn" (Zhang et al., AAAI 2026)**：同意应引用——与论文的 confusability 主题直接相关，introspective confusion 是互补视角。
2. **"Diagnosing Structural Failures in LLM-Based Evidence Extraction" (arXiv 2602.10881)**：不确定其相关性——需要作者判断是否涉及 schema complexity。
3. **"NER Retriever" (Findings EMNLP 2025)**：同意——type-aware embeddings 与 SCS 方法论相关。
4. **"Show Less, Instruct More" (2024)**：同意——definition quality 对 zero-shot NER 的影响与本文 prompt design 讨论相关。

---

### 总结

R2 和我在两个核心判断上完全一致：(1) BCS 证据过度依赖 FewRel（R2-W2 = R1-W1），(2) 论文的主要优势在实验方法论而非指标创新。主要分歧在 SDGD Section 5 的定位——我认为应保留在 main text 但需压缩，R2 建议降级为 appendix。"First controlled study" claim 我认为实质正确但需要更精确的措辞限定。

综合两份 review，论文的核心问题是 **BCS 泛化性不足**：如果作者能在 rebuttal 中补充 1 个 VIF 可控的新数据集的 BCS-controlled 结果，或对 DocRED 提供 ridge regression robustness check，评分可能上调至 Conference (4.0)。否则维持 3.5 (Borderline Conference)。

---

[Reviewer 2 审稿结果]:
交叉回应已提交。与 R1 在大部分问题上达成共识，核心分歧仅在 W5（domain concentration confound）——我认为论文的 balanced design 和 cross-prompt validation 提供了部分缓解，但仍建议作者补充 domain 分布数据。评分维持 3.5/5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2942 · 2026-05-22T04:26:51.782342+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 2943 · 2026-05-22T04:26:52.285100+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T04:14:48.703140+00:00\", \"completed_at\": \"2026-05-22T04:18:28.174018+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"page 26\", \"message\": \"Appendix Table 28 仅占页面顶部约 1/4，其下\\\"ruling out count as a confound.\\\"一行文字后约 3/4 页面完全空白。审稿人可能认为排版粗糙。应将 Table 28 与前后内容合并页面，或调整 float 位置消除空白。\"}, {\"severity\": \"warning\", \"dimension\": \"pages 1-2\", \"message\": \"前 2 页无任何 display item（纯 Abstract + Intro + Related Work 文字），审稿人在第一个视觉锚点（Table 1, p.3）前需阅读 ~2.5 页纯文本。对实证论文而言，建议在 Introduction 末尾或 page 2 加入一个概览 figure（如方法流程图或核心发现 teaser），帮助审稿人快速建立认知框架。\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"正文最后一页压缩了 4 个 section（4.4 Centrality Confound, 4.5 后半, 5 Schema Decomposition, 6 Discussion and Conclusion）。Section 6 Discussion 起始于右栏下半部分，整体感觉偏挤。审稿人可能感到 conclusion 被草草收尾。\"}, {\"severity\": \"warning\", \"dimension\": \"pages 5-8\", \"message\": \"正文仅 4 个 display items（2 fig + 2 table），大量实验结果（28+ tables）被推到 appendix。审稿人评估实验力度时主要看正文，建议将最关键的 1-2 个 appendix 表（如 cross-model validation 或 factorial analysis 结果）提升到正文。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 1(b) 柱状图的 x 轴标签（\\\"intA_type\\\", \\\"intA_3pp\\\"）使用下划线缩写，不如使用更直观的全称或短语（如\\\"Intra-type\\\"），帮助审稿人快速理解。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2 使用 5 种颜色区分错误类型。在灰度打印下 IntraSub（蓝）和 Correct（深蓝/灰）可能难以区分。建议辅以不同 marker shape 或 line style 增强区分度。\"}, {\"severity\": \"info\", \"dimension\": \"page 17\", \"message\": \"Prompt template 展示（Appendix G）使用代码块格式，排版清晰。但 v1/v2 两版 prompt 间的视觉分隔不够明显，可考虑加粗子标题或增加间距。\"}, {\"severity\": \"info\", \"dimension\": \"pages 13-25\", \"message\": \"Appendix 表格整体使用 booktabs 风格，格式一致，最优值有加粗标注。部分表格（如 Table 18, p.20）行数较多，字号偏小但仍可读。\"}, {\"severity\": \"info\", \"dimension\": \"全文\", \"message\": \"未发现 LaTeX 渲染错误、margin 溢出、[?] 未解析引用或 section heading 孤悬页底。公式渲染正确，references 格式一致。整体排版质量专业。\"}], \"counts\":
…[truncated 86 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2944 · 2026-05-22T04:26:52.285555+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 2945 · 2026-05-22T04:26:52.386346+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2946 · 2026-05-22T04:28:30.889171+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "schema-dag-extraction",
  "issues_yaml": "# Review Issues Tracker\n# Updated: 2026-05-22 (Round 29 fresh review)\n\n# ============================================================\n# R29 CRITICAL (2 items)\n# ============================================================\n\n- id: R29-C1\n  summary: \"BCS 度量的干净证据仅限 FewRel RE 一个数据集，论文叙事暗示更广泛适用性\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 29\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-C2: weaken wording\"}\n    - {round: 24, reviewers: [R1, R2], note: \"R24-C1: recenter on FewRel\"}\n    - {round: 25, reviewers: [R1, R2], note: \"R25-C2: confusability scope overclaim\"}\n    - {round: 29, reviewers: [R1, R2], note: \"R1-W1 + R2-W2, cross-share AGREE. 4 datasets: FewRel clean (VIF=1.18), DocRED confounded (VIF=50.9), MAVEN confounded (centrality), NER null (3 models). Abstract 'drives type substitution errors' overgeneralizes.\"}\n  action_items:\n    - {round: 25, action: \"Weaken title/abstract/conclusion generality claims\", assigned_to: \"Agent\", status: done}\n    - {round: 29, action: \"Abstract/Intro must explicitly distinguish count degradation (4 datasets) from BCS effect (FewRel only clean). Consider narrowing title scope to RE.\", assigned_to: \"Agent\", status: open}\n  resolution: \"v34 narrowed some claims but R29 reviewers still find abstract/intro overgeneralizes\"\n  resolution_round: null\n\n- id: R29-C2\n  summary: \"DocRED VIF=50.9 的 partial correlation 不可信但仍作为支持证据呈现\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 29\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-C2: VIF=50.9\"}\n    - {round: 25, reviewers: [R1, R2], note: \"R25-C1: must report semipartial R²\"}\n    - {round: 29, reviewers: [R1, R2], note: \"R1-W2, R2 AGREE. VIF=50.9 → SE inflated ~7x, p-value unreliable. §4.3 still presents DocRED R² in main text, giving 'stronger effect' impression to cursory readers.\"}\n  action_items:\n    - {round: 25, action: \"Report semipartial ΔR²_BCS=5.6%\", assigned_to: \"Agent\", status: done}\n    - {round: 29, action: \"Main text must explicitly mark DocRED BCS as uninterpretable due to VIF=50.9. Consider ridge regression or PCA as robustness check. Do not present as supporting evidence.\", assigned_to: \"Agent\", status: open}\n  resolution: \"v34 reported semipartial R² but R29 reviewers still find presentation misleading\"\n  resolution_round: null\n\n# ============================================================\n# R29 MAJOR (5 items)\n# ============================================================\n\n- id: R29-W1\n  summary: \"SCS/BCS 相对 LLM-PEE 技术新颖性不足，贡献定位需更清晰\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 29\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-W1: SCS vs LLM-PEE novelty\"}\n    - {round: 25, reviewers: [R1, R2], note: \"R25-C4: reframe contribution\"}\n    - {round: 29, reviewers: [R1, R2], note: \"R2-W1, R1 AGREE. SCS = embedding cosine (inherited from LLM-PEE). Novelty is experimental methodology not metric. If BCS only works on FewRel, 'old metric + limited evidence' doubly weakens novelty.\"}\n  action_items:\n    - {round: 25, action: \"Reframe Contribution 1 to empirical findings\", assigned_to: \"Agent\", status: done}\n    - {round: 29, action: \"§3.2 should more explicitly articulate what is new vs inherited. Novelty rests on experimental design + empirical findings, not metric.\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R29-W2\n  summary: \"TOST 等价性检验结论依赖量表选择（probability vs logit 给出相反结论）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 29\n  mentions:\n    - {round: 23, reviewers: [R1], note: \"R23-C1: logit TOST inconclusive\"}\n    - {round: 25, reviewers: [R1, R2], note: \"R25-W4: acknowledge logit-scale in main text\"}\n    - {round: 29, reviewers: [R1, R2], note: \"R1-W3, R2 AGREE. Probability ±3pp: p=0.003 (equivalence). Logit ±3pp: inconclusive, interaction p=0.047. 'Independently addressable' claim on knife-edge.\"}\n  action_items:\n    - {round: 25, action: \"Acknowledge logit-scale in §4.4\", assigned_to: \"Agent\", status: done}\n    - {round: 29, action: \"Weaken 'independently addressable' to 'approximately additive on probability scale'. Report both scales in main text explicitly.\", assigned_to: \"Agent\", status: open}\n  resolution: \"v34 added logit mention but R29 finds claim still too strong\"\n  resolution_round: null\n\n- id: R29-W3\n  summary: \"Abstract/Introduction 使用因果语言（'drives'）超出 correlational evidence 支撑\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 29\n  last_seen_round: 29\n  mentions:\n    - {round: 29, reviewers: [R1, R2], note: \"R1-W4, R2 AGREE. 'drives' implies causation. BCS-controlled design is quasi-experimental but not randomized intervention. §6 acknowledges correlational nature, contradicting abstract.\"}\n  action_items:\n    - {round: 29, action: \"Replace 'drives' with 'predicts' or 'is associated with' throughout abstract/intro/conclusion.\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R29-W4\n  summary: \"Greedy batch 构造可能引入 domain concentration confound（high-BCS batches 集中同一语义域）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 29\n  last_seen_round: 29\n  mentions:\n    - {round: 29, reviewers: [R1, R2], note: \"R1-W5, R2 partial REBUT (balanced design + cross-prompt partially mitigate). Both agree: report domain distribution of extreme batches.\"}\n  action_items:\n    - {round: 29, action: \"Report type domain distribution for high-BCS and low-BCS extreme batches (FewRel). Consider domain-matched batch construction as robustness check.\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R29-W5\n  summary: \"共享 text instances 的 bootstrap CI 可能 anti-conservative（instance-level correlation 未处理）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 29\n  last_seen_round: 29\n  mentions:\n    - {round: 29, reviewers: [R1, R2], note: \"R1-W6, R2 AGREE. Same 1000 text instances across all batches. Batch-level bootstrap treats batches as independent but instance difficulty creates cross-batch correlation. Practical impact may be limited (Appendix R) but formally valid concern.\"}\n  action_items:\n    - {round: 29, action: \"Add cluster-robust SE (cluster on text instance) or split-sample bootstrap as robustness check.\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R29 MINOR (6 items)\n# ============================================================\n\n- id: R29-M1\n  summary: \"'First controlled study' claim needs more precise scoping\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 29\n  mentions:\n    - {round: 25, reviewers: [R1, R2], note: \"R25-W8: scope more precisely\"}\n    - {round: 29, reviewers: [R1, R2], note: \"R2-W3, R1 partial REBUT (claim substantively correct, Chen/GoLLIE/Reflect different scope). Both agree on precise wording.\"}\n  action_items:\n    - {round: 29, action: \"Refine to 'first controlled study simultaneously isolating count and inter-type confusability as independent dimensions using embedding-based metrics and controlled batch design in zero-shot LLM IE'\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R29-M2\n  summary: \"NER null framing biased toward 'low power'; should equally consider 'genuinely no effect'\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 29\n  mentions:\n    - {round: 25, reviewers: [R1, R2], note: \"R25-C3: add power analysis + cannot distinguish statement\"}\n    - {round: 29, reviewers: [R1, R2], note: \"R1-M2, R2 AGREE. Null replicates across 3 models, 2 prompts. Relaxed matching (Table 31) still null. More likely task property than pure power issue.\"}\n  action_items:\n    - {round: 25, action: \"Add 'cannot distinguish' statement\", assigned_to: \"Agent\", status: done}\n    - {round: 29, action: \"Balance discussion: mention NER span detection dominance as alternative explanation alongside power.\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R29-M3\n  summary: \"Discussion 缺少理论层面讨论（为什么 embedding similarity 能预测 LLM type confusion）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 29\n  mentions:\n    - {round: 25, reviewers: [R1, R2], note: \"R25-W6: practical implications under-developed\"}\n    - {round: 29, reviewers: [R1, R2], note: \"R2-W5, R1 AGREE. Missing 'why' discussion: model representation alignment, data property vs model property, semantic overlap as inherent property.\"}\n  action_items:\n    - {round: 29, action: \"Add 1-2 sentences on possible mechanism: embedding similarity as proxy for inherent semantic overlap in type definitions.\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R29-M4\n  summary: \"SDGD Section 5 应压缩（保留但精简），cross-model validation 应提升到正文\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 29\n  last_seen_round: 29\n  mentions:\n    - {round: 29, reviewers: [R1, R2], note: \"R2-W4 suggests demote to appendix; R1 REBUT (narrative arc requires it). Consensus: keep in main text but compress (~0.5 col), move algorithm details to appendix. Promote 1-2 key cross-model tables to main text.\"}\n  action_items:\n    - {round: 29, action: \"Compress §5 (move SDGD algorithm to appendix, keep findings+diagnosis). Consider promoting cross-model BCS table to main text.\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R29-M5\n  summary: \"多重比较无正式校正（Bonferroni/BH），边缘结果受影响\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 29\n  last_seen_round: 29\n  mentions:\n    - {round: 29, reviewers: [R1, R2], note: \"R1-M3, R2 AGREE. Core claims p<0.001 survive any correction. Marginal results (logit interaction p=0.047) would not.\"}\n  action_items:\n    - {round: 29, action: \"Report Bonferroni/BH-corrected p-values for marginal results as sensitivity check.\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R29-M6\n  summary: \"Missing references: Reflect then Learn (AAAI 2026), NER Retriever (EMNLP 2025 Findings), Show Less Instruct More (2024)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 29\n  last_seen_round: 29\n  mentions:\n    - {round: 29, reviewers: [R1, R2], note: \"R2 identified 4 missing refs. R1 agrees on 3 (Reflect then Learn, NER Retriever, Show Less Instruct More). Diagnosing Structural Failures relevance uncertain.\"}\n  action_items:\n    - {round: 29, action: \"Add citations for Zhang et al. AAAI 2026 (introspective confusion), NER Retriever EMNLP 2025, and Show Less Instruct More 2024.\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# HISTORICAL — Issues from R23-R25 now superseded by R29\n# ============================================================\n# All R25 issues merged into R29 where applicable.\n# R25-C1 → R29-C2 (DocRED VIF)\n# R25-C2 → R29-C1 (FewRel scope)\n# R25-C3 → R29-M2 (NER null)\n# R25-C4 → R29-W1 (novelty framing)\n# R25-W1 → noted in R29-M4 (single-model analyses)\n# R25-W2 → R29-M4 (cross-model in appendix)\n# R25-W3 → R29-W4 (domain confound)\n# R25-W4 → R29-W2 (TOST)\n# R25-W5 → absorbed (abstract simplified in v34, R29 finds acceptable)\n# R25-W6 → R29-M3 (discussion depth)\n# R25-W7 → absorbed (pair vs batch distinction now in v34)\n# R25-W8 → R29-M1 (first controlled study)\n# R25-M1 → resolved (orphan bib cleaned)\n# R25-M2 → absorbed (limitations length acceptable)\n# R25-M3 → absorbed (SDGD framing improved)\n# R24-W4 → resolved (single seed + FP8 adequately addressed)\n# R23-C1, R23-W2, R23-W7, R23-F1 → resolved\n# R22-C1, R22-C4 → resolved\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "schema-dag-extraction",
    "issues_yaml": "# Review Issues Tracker\n# Updated: 2026-05-22 (Round 29 fresh review)\n\n# ============================================================\n# R29 CRITICAL (2 items)\n# ============================================================\n\n- id: R29-C1\n  summary: \"BCS 度量的干净证据仅限 FewRel RE 一个数据集，论文叙事暗示更广泛适用性\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 29\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-C2: weaken wording\"}\n    - {round: 24, reviewers: [R1, R2], note: \"R24-C1: recenter on FewRel\"}\n    - {round: 25, reviewers: [R1, R2], note: \"R25-C2: confusability scope overclaim\"}\n    - {round: 29, reviewers: [R1, R2], note: \"R1-W1 + R2-W2, cross-share AGREE. 4 datasets: FewRel clean (VIF=1.18), DocRED confounded (VIF=50.9), MAVEN confounded (centrality), NER null (3 models). Abstract 'drives type substitution errors' overgeneralizes.\"}\n  action_items:\n    - {round: 25, action: \"Weaken title/abstract/conclusion generality claims\", assigned_to: \"Agent\", status: done}\n    - {round: 29, action: \"Abstract/Intro must explicitly distinguish count degradation (4 datasets) from BCS effect (FewRel only clean). Consider narrowing title scope to RE.\", assigned_to: \"Agent\", status: open}\n  resolution: \"v34 narrowed some claims but R29 reviewers still find abstract/intro overgeneralizes\"\n  resolution_round: null\n\n- id: R29-C2\n  summary: \"DocRED VIF=50.9 的 partial correlation 不可信但仍作为支持证据呈现\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 29\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-C2: VIF=50.9\"}\n    - {round: 25, reviewers: [R1, R2], note: \"R25-C1: must report semipartial R²\"}\n    - {round: 29, reviewers: [R1, R2], note: \"R1-W2, R2 AGREE. VIF=50.9 → SE inflated ~7x, p-value unreliable. §4.3 still presents DocRED R² in main text, giving 'stronger effect' impression to cursory readers.\"}\n  action_items:\n    - {round: 25, action: \"Report semipartial ΔR²_BCS=5.6%\", assigned_to: \"Agent\", status: done}\n    - {round: 29, action: \"Main text must explicitly mark DocRED BCS as uninterpretable due to VIF=50.9. Consider ridge regression or PCA as robustness check. Do not present as supporting evidence.\", assigned_to: \"Agent\", status: open}\n  resolution: \"v34 reported semipartial R² but R29 reviewers still find presentation misleading\"\n  resolution_round: null\n\n# ============================================================\n# R29 MAJOR (5 items)\n# ============================================================\n\n- id: R29-W1\n  summary: \"SCS/BCS 相对 LLM-PEE 技术新颖性不足，贡献定位需更清晰\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 29\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-W1: SCS vs LLM-PEE novelty\"}\n    - {round: 25, reviewers: [R1, R2], note: \"R25-C4: reframe contribution\"}\n    - {round: 29, reviewers: [R1, R2], note: \"R2-W1, R1 AGREE. SCS = embedding cosine (inherited from LLM-PEE). Novelty is experimental methodology not metric. If BCS only works on FewRel, 'old metric + limited evidence' doubly weakens novelty.\"}\n  action_items:\n    - {round: 25, action: \"Reframe Contribution 1 to empirical findings\", assigned_to: \"Agent\", status: done}\n    - {round: 29, action: \"§3.2 should more explicitly articulate what is new vs inherited. Novelty rests on experimental design + empirical findings, not metric.\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R29-W2\n  summary: \"TOST 等价性检验结论依赖量表选择（probability vs logit 给出相反结论）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 29\n  mentions:\n    - {round: 23, reviewers: [R1], note: \"R23-C1: logit TOST inconclusive\"}\n    - {round: 25, reviewers: [R1, R2], note: \"R25-W4: acknowledge logit-scale in main text\"}\n    - {round: 29, reviewers: [R1, R2], note: \"R1-W3, R2 AGREE. Probability ±3pp: p=0.003 (equivalence). Logit ±3pp: inconclusive, interaction p=0.047. 'Independently addressable' claim on knife-edge.\"}\n  action_items:\n    - {round: 25, action: \"Acknowledge logit-scale in §4.4\", assigned_to: \"Agent\", status: done}\n    - {round: 29, action: \"Weaken 'independently addressable' to 'approximately additive on probability scale'. Report both scales in main text explicitly.\", assigned_to: \"Agent\", status: open}\n  resolution: \"v34 added logit mention but R29 finds claim still too strong\"\n  resolution_round: null\n\n- id: R29-W3\n  summary: \"Abstract/Introduction 使用因果语言（'drives'）超出 correlational evidence 支撑\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 29\n  last_seen_round: 29\n  mentions:\n    - {round: 29, reviewers: [R1, R2], note: \"R1-W4, R2 AGREE. 'drives' implies causation. BCS-controlled design is quasi-experimental but not randomized intervention. §6 acknowledges correlational nature, contradicting abstract.\"}\n  action_items:\n    - {round: 29, action: \"Replace 'drives' with 'predicts' or 'is associated with' throughout abstract/intro/conclusion.\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R29-W4\n  summary: \"Greedy batch 构造可能引入 domain concentration confound（high-BCS batches 集中同一语义域）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 29\n  last_seen_round: 29\n  mentions:\n    - {round: 29, reviewers: [R1, R2], note: \"R1-W5, R2 partial REBUT (balanced design + cross-prompt partially mitigate). Both agree: report domain distribution of extreme batches.\"}\n  action_items:\n    - {round: 29, action: \"Report type domain distribution for high-BCS and low-BCS extreme batches (FewRel). Consider domain-matched batch construction as robustness check.\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R29-W5\n  summary: \"共享 text instances 的 bootstrap CI 可能 anti-conservative（instance-level correlation 未处理）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 29\n  last_seen_round: 29\n  mentions:\n    - {round: 29, reviewers: [R1, R2], note: \"R1-W6, R2 AGREE. Same 1000 text instances across all batches. Batch-level bootstrap treats batches as independent but instance difficulty creates cross-batch correlation. Practical impact may be limited (Appendix R) but formally valid concern.\"}\n  action_items:\n    - {round: 29, action: \"Add cluster-robust SE (cluster on text instance) or split-sample bootstrap as robustness check.\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R29 MINOR (6 items)\n# ============================================================\n\n- id: R29-M1\n  summary: \"'First controlled study' claim needs more precise scoping\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 29\n  mentions:\n    - {round: 25, reviewers: [R1, R2], note: \"R25-W8: scope more precisely\"}\n    - {round: 29, reviewers: [R1, R2], note: \"R2-W3, R1 partial REBUT (claim substantively correct, Chen/GoLLIE/Reflect different scope). Both agree on precise wording.\"}\n  action_items:\n    - {round: 29, action: \"Refine to 'first controlled study simultaneously isolating count and inter-type confusability as independent dimensions using embedding-based metrics and controlled batch design in zero-shot LLM IE'\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R29-M2\n  summary: \"NER null framing biased toward 'low power'; should equally consider 'genuinely no effect'\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 29\n  mentions:\n    - {round: 25, reviewers: [R1, R2], note: \"R25-C3: add power analysis + cannot distinguish statement\"}\n    - {round: 29, reviewers: [R1, R2], note: \"R1-M2, R2 AGREE. Null replicates across 3 models, 2 prompts. Relaxed matching (Table 31) still null. More likely task property than pure power issue.\"}\n  action_items:\n    - {round: 25, action: \"Add 'cannot distinguish' statement\", assigned_to: \"Agent\", status: done}\n    - {round: 29, action: \"Balance discussion: mention NER span detection dominance as alternative explanation alongside power.\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R29-M3\n  summary: \"Discussion 缺少理论层面讨论（为什么 embedding similarity 能预测 LLM type confusion）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 29\n  mentions:\n    - {round: 25, reviewers: [R1, R2], note: \"R25-W6: practical implications under-developed\"}\n    - {round: 29, reviewers: [R1, R2], note: \"R2-W5, R1 AGREE. Missing 'why' discussion: model representation alignment, data property vs model property, semantic overlap as inherent property.\"}\n  action_items:\n    - {round: 29, action: \"Add 1-2 sentences on possible mechanism: embedding similarity as proxy for inherent semantic overlap in type definitions.\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R29-M4\n  summary: \"SDGD Section 5 应压缩（保留但精简），cross-model validation 应提升到正文\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 29\n  last_seen_round: 29\n  mentions:\n    - {round: 29, reviewers: [R1, R2], note: \"R2-W4 suggests demote to appendix; R1 REBUT (narrative arc requires it). Consensus: keep in main text but compress (~0.5 col), move algorithm details to appendix. Promote 1-2 key cross-model tables to main text.\"}\n  action_items:\n    - {round: 29, action: \"Compress §5 (move SDGD algorithm to appendix, keep findings+diagnosis). Consider promoting cross-model BCS table to main text.\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R29-M5\n  summary: \"多重比较无正式校正（Bonferroni/BH），边缘结果受影响\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 29\n  last_seen_round: 29\n  mentions:\n    - {round: 29, reviewers: [R1, R2], note: \"R1-M3, R2 AGREE. Core claims p<0.001 survive any correction. Marginal results (logit interaction p=0.047) would not.\"}\n  action_items:\n    - {round: 29, action: \"Report Bonferroni/BH-corrected p-values for marginal results as sensitivity check.\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R29-M6\n  summary: \"Missing references: Reflect then Learn (AAAI 2026), NER Retriever (EMNLP 2025 Findings), Show Less Instruct More (2024)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 29\n  last_seen_round: 29\n  mentions:\n    - {round: 29, reviewers: [R1, R2], note: \"R2 identified 4 missing refs. R1 agrees on 3 (Reflect then Learn, NER Retriever, Show Less Instruct More). Diagnosing Structural Failures relevance uncertain.\"}\n  action_items:\n    - {round: 29, action: \"Add citations for Zhang et al. AAAI 2026 (introspective confusion), NER Retriever EMNLP 2025, and Show Less Instruct More 2024.\", assigned_to: \"Agent\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# HISTORICAL — Issues from R23-R25 now superseded by R29\n# ============================================================\n# All R25 issues merged into R29 where applicable.\n# R25-C1 → R29-C2 (DocRED VIF)\n# R25-C2 → R29-C1 (FewRel scope)\n# R25-C3 → R29-M2 (NER null)\n# R25-C4 → R29-W1 (novelty framing)\n# R25-W1 → noted in R29-M4 (single-model analyses)\n# R25-W2 → R29-M4 (cross-model in appendix)\n# R25-W3 → R29-W4 (domain confound)\n# R25-W4 → R29-W2 (TOST)\n# R25-W5 → absorbed (abstract simplified in v34, R29 finds acceptable)\n# R25-W6 → R29-M3 (discussion depth)\n# R25-W7 → absorbed (pair vs batch distinction now in v34)\n# R25-W8 → R29-M1 (first controlled study)\n# R25-M1 → resolved (orphan bib cleaned)\n# R25-M2 → absorbed (limitations length acceptable)\n# R25-M3 → absorbed (SDGD framing improved)\n# R24-W4 → resolved (single seed + FP8 adequately addressed)\n# R23-C1, R23-W2, R23-W7, R23-F1 → resolved\n# R22-C1, R22-C4 → resolved\n"
  }
}
```

</details>

---


### Tool result

_source line 2947 · 2026-05-22T04:28:30.990182+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml\", \"bytes\": 12002}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2948 · 2026-05-22T04:30:34.843148+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 29 (Fresh Review)\n\n**论文**: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性与完整性）\n**轮次**: 1 轮独立审稿 + 1 轮交叉分享（共识达成，无需 Round 2）\n\n---\n\n## Summary\n\n本文研究 schema 复杂度（类型数量 + 类型间混淆度）如何影响 training-free LLM 信息抽取性能。提出 SCS/BCS 两个 embedding-based 指标，通过 BCS-controlled batch design 在 4 个数据集（Few-NERD/FewRel/DocRED/MAVEN）上隔离 count 和 confusability 两个维度。主要发现：(1) count 退化跨 4 数据集、4 模型一致；(2) BCS 解释 FewRel RE 上 ~22% 的跨 batch 准确率方差；(3) schema 分解因 merge amplification 和 routing failure 而失败。\n\n---\n\n## Strengths\n\n**S1 [共识]**: BCS-controlled batch design（固定 count 变 BCS 隔离 confusability）是真正的方法论创新，可被后续研究复用。\n\n**S2 [共识]**: 统计严谨度显著高于同类 NLP 实证工作——bootstrap CIs、TOST equivalence tests、power analysis、partial correlations、permutation tests、variance decomposition。\n\n**S3 [共识]**: 对负面结果和 confounders 的报告达到罕见的透明度——NER batch-level null（3 模型一致）、MAVEN centrality confound、SDGD 失败均如实呈现并附带诊断分析。\n\n**S4 [共识]**: Count 退化的实证基础极其扎实——4 数据集、3 任务、4 模型方向一致，效应量大（FewRel -36pp, DocRED -49pp）。\n\n**S5 [共识]**: 19 页 Appendix 提供完整 prompt templates、cross-model validation、sensitivity analysis、confound controls，reproducibility 标准极高。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1 [Critical, R1+R2 AGREE]: BCS 度量的干净证据仅限 FewRel RE，但论文叙事暗示跨任务适用性。**\n\n逐数据集审查：\n- FewRel RE: R²=0.22, VIF=1.18 — **唯一 confound-free 证据**\n- DocRED RE: VIF=50.9, BCS-centrality r=0.99, partial correlation 标准误膨胀 ~7x, 不可信\n- MAVEN ED: controlling for centrality 后 BCS → non-significant (p>0.2)\n- Few-NERD NER: batch-level null, 3 模型 × 2 prompts 一致\n\nAbstract \"inter-type confusability drives type substitution errors\" 的泛化语气与证据不匹配。Count 退化的 4 数据集一致性与 BCS 的 FewRel 局限性形成鲜明对比。\n\n**必须修改**: Abstract/Introduction 明确区分 count 退化（跨任务一致）和 BCS 效应（clean evidence 仅 FewRel RE）。考虑在补充 1 个 VIF 可控的新数据集上验证 BCS。\n\n**W2 [Critical, R1+R2 AGREE]: DocRED VIF=50.9 的处理不充分。**\n\nVIF=50.9 意味着 BCS 和 degree centrality 几乎完全线性相关，partial correlation 的 SE 膨胀 √50.9 ≈ 7.1 倍。在此条件下报告的 p<0.001 几乎不可解释。然而 §4.3 main text 仍呈现 DocRED R²=0.578，虽附注说明了 collinearity，但可能给粗读读者造成 \"DocRED 效应更强\" 的错误印象。\n\n**必须修改**: Main text 明确标注 DocRED BCS 因 VIF=50.9 不可解释，不作为支持证据呈现。提供 ridge regression 或 PCA-based partial correlation 作为 robustness check。\n\n### Should-Fix（影响评分）\n\n**W3 [Major, R2 raised + R1 AGREE]: SCS/BCS 相对 LLM-PEE 技术新颖性有限。**\n\nSCS = embedding cosine similarity，论文自认继承自 LLM-PEE。BCS 的 max 聚合技术含量有限。贡献定位为 \"旧指标 + 新实验范式 + 实证发现\"。如果 BCS 仅在 FewRel 有干净证据，novelty 和 evidence 同时偏弱。\n\n**建议**: §3.2 更明确阐述 SCS/BCS 与 LLM-PEE 的技术差异。增强实证覆盖比修饰指标新颖性更有效。\n\n**W4 [Major, R1 raised + R2 AGREE]: TOST 等价性检验结论依赖量表选择。**\n\n- Probability scale ±3pp: TOST p=0.003 → equivalence\n- Logit scale ±3pp: TOST inconclusive; interaction p=0.047 (边缘显著)\n\n两个量表在关键 margin 给出相反结论。\"Count 和 confusability independently addressable\" 这一核心 claim 处于刀刃上。Logit scale 对 bounded metrics 通常更理论合理。\n\n**建议**: 弱化为 \"approximately additive on the probability scale within the observed range\"。Main text 明确报告两个量表的结论差异。\n\n**W5 [Major, R1 raised + R2 AGREE]: Abstract/Introduction 使用因果语言超出证据支撑。**\n\n\"Drives\" 暗示因果关系。BCS-controlled design 是 quasi-experimental 但非 randomized intervention。§6 承认 \"correlational evidence with controlled stratification\"，与 abstract 中的 \"drives\" 矛盾。\n\n**建议**: 将 \"drives\" 替换为 \"predicts\" 或 \"is associated with\"。\n\n**W6 [Major, R1 raised + R2 partial REBUT]: Greedy batch 构造可能引入 domain concentration confound。**\n\nHigh-BCS batches 倾向选择同一语义域的类型。FewRel 的 balanced design 和 cross-prompt validation 部分缓解，但不能排除 cluster-level domain difficulty 这一替代解释。\n\n**建议**: 报告 extreme batches 的 type domain 分布。考虑 domain-matched batch construction 作为 robustness check。\n\n**W7 [Major, R1 raised + R2 AGREE]: 共享 text instances 的 bootstrap CI 可能 anti-conservative。**\n\n1000 个 text instances 跨所有 batches 共享。Instance-level cross-batch correlation 未被 batch-level bootstrap 处理。Appendix R 的 variance decomposition 部分缓解，但形式上 CI 可能偏窄。\n\n**建议**: 提供 cluster-robust SE（cluster on text instance）或 split-sample bootstrap 作为 sensitivity check。\n\n### Minor\n\n**M1**: \"First controlled study\" claim 实质正确但需更精确措辞限定（\"simultaneously isolating count and inter-type confusability as independent dimensions using embedding-based metrics and controlled batch design\"）。[R2 raised, R1 partial REBUT — 同意限定措辞]\n\n**M2**: NER null framing 偏向 \"低 power\" 解释，应同等考虑 \"NER 任务特性\"（span detection dominance over type classification）作为替代解释。Relaxed matching (Appendix) 仍 null 支持此解读。[R1+R2 AGREE]\n\n**M3**: Discussion 缺少理论层面讨论——为什么 embedding similarity 能预测 LLM type confusion？[R1+R2 AGREE]\n\n**M4**: §5 SDGD 应保留在正文（叙事弧需要）但需压缩，将算法细节移入 appendix。Cross-model validation 的关键表应提升到正文。[R1 keep + R2 demote → 共识: keep but compress]\n\n**M5**: 多重比较无正式校正。核心 claims (p<0.001) 不受影响，但边缘结果（logit interaction p=0.047）在校正后可能 non-significant。[R1+R2 AGREE]\n\n**M6**: 遗漏引用 3 篇: Zhang et al. AAAI 2026 (Reflect then Learn, introspective confusion), NER Retriever (Findings EMNLP 2025, type-aware embeddings), Show Less Instruct More (2024, definition quality for zero-shot NER)。[R2 identified, R1 agrees on 3/4]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. BCS 干净证据仅 FewRel RE，论文需明确限定适用范围\n2. DocRED VIF=50.9 下的 partial correlation 不可信，不应作为支持证据\n3. Count 退化故事跨 4 数据集 4 模型扎实，是 solid contribution\n4. BCS-controlled batch design 是方法论创新\n5. 统计严谨度和 appendix 质量显著高于同类工作\n6. \"Drives\" 应替换为 \"predicts\"\n7. TOST \"independently addressable\" claim 需弱化\n\n## Reviewer Divergence [Partial disagreement]\n\n1. **Domain concentration confound (W6)**: R1 认为需要严格验证；R2 认为 balanced design + cross-prompt 提供部分缓解但同意报告 domain 分布。**结论**: 建议作为 should-fix（报告 domain 分布），非 must-fix。\n\n2. **SDGD section 定位 (M4)**: R2 建议降级为 appendix；R1 认为叙事弧需要保留。**结论**: 保留但压缩。\n\n3. **\"First controlled study\" claim (M1)**: R2 认为 Chen et al./GoLLIE/Reflect 相关；R1 认为这些工作 scope 不同，claim 实质正确。**结论**: 措辞限定即可。\n\n---\n\n## Questions（需作者澄清）\n\nQ1. 能否在一个 BCS-centrality VIF < 5 的新数据集上重复 BCS-controlled 实验？这是提升论文最直接的路径。\n\nQ2. DocRED VIF=50.9 下报告的 partial correlation p<0.001 是否经过 variance inflation 调整？能否提供 ridge regression 结果？\n\nQ3. High-BCS extreme batches 中的 relation types 是否集中在特定语义域（如 kinship, spatial）？\n\nQ4. 跨 batch 共享 text instances 对 bootstrap CI 宽度的影响有多大？Split-sample bootstrap 结果如何？\n\nQ5. NER batch-level null 在 3 模型 + 2 prompts + relaxed matching 上一致——作者是否认为这更可能反映 NER 任务特性而非 power 不足？\n\nQ6. 如果 logit scale 上存在边缘显著的 count×BCS interaction (p=0.047)，\"independently addressable\" claim 是否需要根本性修改？\n\n---\n\n## Missing References\n\n1. Zhang et al. \"Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion\" (AAAI 2026) — content uncertainty 与 type confusability 直接相关\n2. \"NER Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings\" (Findings EMNLP 2025) — type-aware embeddings 方法论相关\n3. \"Show Less, Instruct More: Enriching Prompts with Definitions and Guidelines for Zero-Shot NER\" (2024) — definition quality 影响 zero-shot NER\n\n---\n\n## External Review\n\n**状态**: 未请求（项目未启用外部审稿）\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（2026-05-22 04:14 → 04:18）。发现：\n\n- **[Critical]** Appendix p.26: Table 28 仅占页面 1/4，下方 ~3/4 空白。应调整 float 位置消除空白。\n- **[Warning]** pp.1-2: 前 2 页纯文本无 display item，建议 Introduction 末尾加概览 figure（方法流程图或核心发现 teaser）。\n- **[Warning]** p.8: 正文末页压缩 4 个 section（4.4/4.5后半/5/6），Discussion 感觉草草收尾。\n- **[Warning]** pp.5-8: 正文仅 4 个 display items（2 fig + 2 table），大量结果在 appendix。建议提升 1-2 个关键 appendix 表到正文。\n- **[Info]** Figure 1(b) x 轴标签使用缩写（intA_type 等），不够直观。\n- **[Info]** Figure 2 灰度打印下颜色区分度不足。\n- **[Info]** 整体排版专业，无 LaTeX 渲染错误、margin 溢出或未解析引用。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 / 5 (Borderline Conference)\n\n**EMNLP 2026 标准**: 3.5 = Borderline Conference（可被主会议接收的边缘）\n\n**置信度**: 4/5（两位 Reviewer 均仔细阅读全文及全部 appendix，逐一核查统计方法论）\n\n**理由**:\n\n论文有两个明确的贡献维度：(1) Count 退化的系统性实证——4 数据集、4 模型一致，效应量大，是 solid contribution；(2) BCS-controlled batch design 是方法论创新。然而，BCS 作为 confusability predictor 的核心证据仅在 FewRel RE 上 confound-free（VIF=1.18），另外 3 个数据集均有严重问题（DocRED VIF=50.9 不可解释、MAVEN 归因于 centrality、NER null）。这使得论文的主要叙事——confusability 是独立退化维度——在泛化性上显著受限。\n\n如果作者能在 rebuttal 中：(a) 补充 1 个 VIF 可控的新数据集 BCS-controlled 结果，或 (b) 对 DocRED 提供 ridge regression robustness check 证实 BCS 有独立贡献，或 (c) 将 claim scope 明确限定为 RE 并相应调整 title/abstract，评分可上调至 4.0 (Conference)。\n\n当前状态建议 **Findings 接收**——统计严谨度和实验方法论质量足以接收，但泛化性不足以支撑 main conference。\n\n---\n\n## Detailed Comments（逐节）\n\n**Abstract**: 信息密度可接受但 \"drives\" 需改为 \"predicts\"。SCS 的具体含义（pairwise cosine similarity between type-name embeddings）应在 abstract 中明确。\n\n**§1 Introduction**: RQ 设置清晰。\"First controlled study\" claim 需限定。Contribution list 的第 2 点（task asymmetry）与第 1 点有较多重叠。\n\n**§2 Related Work**: 覆盖面良好。缺 Zhang et al. AAAI 2026。\"SCS novelty\" 段的自我定位诚实但可能不够自信。\n\n**§3 Experimental Setup**: 设计精良。Table 1 \"BCS ranges not comparable across embedding models\" 这一限制对结论的影响应展开讨论。\n\n**§4 Results**: Count curves (§4.1) 扎实。BCS-controlled (§4.3) 的 FewRel 结果令人信服。DocRED 结果需 downgrade 呈现方式。TOST (§4.4) 需报告两个量表结论。NER null 需平衡解释。\n\n**§5 SDGD**: 叙事逻辑合理但需压缩。Oracle routing insight (72.4% vs 50.4%) 有价值。\n\n**§6 Discussion**: 过短。需添加 \"why embedding similarity predicts LLM confusion\" 的理论讨论。Practical implications 已改善但仍可更具体。\n\n**Limitations**: 全面。Item 1 正确标注了单模型分析的范围。\"Cannot distinguish\" 表述正确但应同等权重讨论 \"NER 任务特性\" 替代解释。\n",
  "project": "schema-dag-extraction",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5",
  "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 29 (Fresh Review)\n\n**论文**: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性与完整性）\n**轮次**: 1 轮独立审稿 + 1 轮交叉分享（共识达成，无需 Round 2）\n\n---\n\n## Summary\n\n本文研究 schema 复杂度（类型数量 + 类型间混淆度）如何影响 training-free LLM 信息抽取性能。提出 SCS/BCS 两个 embedding-based 指标，通过 BCS-controlled batch design 在 4 个数据集（Few-NERD/FewRel/DocRED/MAVEN）上隔离 count 和 confusability 两个维度。主要发现：(1) count 退化跨 4 数据集、4 模型一致；(2) BCS 解释 FewRel RE 上 ~22% 的跨 batch 准确率方差；(3) schema 分解因 merge amplification 和 routing failure 而失败。\n\n---\n\n## Strengths\n\n**S1 [共识]**: BCS-controlled batch design（固定 count 变 BCS 隔离 confusability）是真正的方法论创新，可被后续研究复用。\n\n**S2 [共识]**: 统计严谨度显著高于同类 NLP 实证工作——bootstrap CIs、TOST equivalence tests、power analysis、partial correlations、permutation tests、variance decomposition。\n\n**S3 [共识]**: 对负面结果和 confounders 的报告达到罕见的透明度——NER batch-level null（3 模型一致）、MAVEN centrality confound、SDGD 失败均如实呈现并附带诊断分析。\n\n**S4 [共识]**: Count 退化的实证基础极其扎实——4 数据集、3 任务、4 模型方向一致，效应量大（FewRel -36pp, DocRED -49pp）。\n\n**S5 [共识]**: 19 页 Appendix 提供完整 prompt templates、cross-model validation、sensitivity analysis、confound controls，reproducibility 标准极高。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1 [Critical, R1+R2 AGREE]: BCS 度量的干净证据仅限 FewRel RE，但论文叙事暗示跨任务适用性。**\n\n逐数据集审查：\n- FewRel RE: R²=0.22, VIF=1.18 — **唯一 confound-free 证据**\n- DocRED RE: VIF=50.9, BCS-centrality r=0.99, partial correlation 标准误膨胀 ~7x, 不可信\n- MAVEN ED: controlling for centrality 后 BCS → non-significant (p>0.2)\n- Few-NERD NER: batch-level null, 3 模型 × 2 prompts 一致\n\nAbstract \"inter-type confusability drives type substitution errors\" 的泛化语气与证据不匹配。Count 退化的 4 数据集一致性与 BCS 的 FewRel 局限性形成鲜明对比。\n\n**必须修改**: Abstract/Introduction 明确区分 count 退化（跨任务一致）和 BCS 效应（clean evidence 仅 FewRel RE）。考虑在补充 1 个 VIF 可控的新数据集上验证 BCS。\n\n**W2 [Critical, R1+R2 AGREE]: DocRED VIF=50.9 的处理不充分。**\n\nVIF=50.9 意味着 BCS 和 degree centrality 几乎完全线性相关，partial correlation 的 SE 膨胀 √50.9 ≈ 7.1 倍。在此条件下报告的 p<0.001 几乎不可解释。然而 §4.3 main text 仍呈现 DocRED R²=0.578，虽附注说明了 collinearity，但可能给粗读读者造成 \"DocRED 效应更强\" 的错误印象。\n\n**必须修改**: Main text 明确标注 DocRED BCS 因 VIF=50.9 不可解释，不作为支持证据呈现。提供 ridge regression 或 PCA-based partial correlation 作为 robustness check。\n\n### Should-Fix（影响评分）\n\n**W3 [Major, R2 raised + R1 AGREE]: SCS/BCS 相对 LLM-PEE 技术新颖性有限。**\n\nSCS = embedding cosine similarity，论文自认继承自 LLM-PEE。BCS 的 max 聚合技术含量有限。贡献定位为 \"旧指标 + 新实验范式 + 实证发现\"。如果 BCS 仅在 FewRel 有干净证据，novelty 和 evidence 同时偏弱。\n\n**建议**: §3.2 更明确阐述 SCS/BCS 与 LLM-PEE 的技术差异。增强实证覆盖比修饰指标新颖性更有效。\n\n**W4 [Major, R1 raised + R2 AGREE]: TOST 等价性检验结论依赖量表选择。**\n\n- Probability scale ±3pp: TOST p=0.003 → equivalence\n- Logit scale ±3pp: TOST inconclusive; interaction p=0.047 (边缘显著)\n\n两个量表在关键 margin 给出相反结论。\"Count 和 confusability independently addressable\" 这一核心 claim 处于刀刃上。Logit scale 对 bounded metrics 通常更理论合理。\n\n**建议**: 弱化为 \"approximately additive on the probability scale within the observed range\"。Main text 明确报告两个量表的结论差异。\n\n**W5 [Major, R1 raised + R2 AGREE]: Abstract/Introduction 使用因果语言超出证据支撑。**\n\n\"Drives\" 暗示因果关系。BCS-controlled design 是 quasi-experimental 但非 randomized intervention。§6 承认 \"correlational evidence with controlled stratification\"，与 abstract 中的 \"drives\" 矛盾。\n\n**建议**: 将 \"drives\" 替换为 \"predicts\" 或 \"is associated with\"。\n\n**W6 [Major, R1 raised + R2 partial REBUT]: Greedy batch 构造可能引入 domain concentration confound。**\n\nHigh-BCS batches 倾向选择同一语义域的类型。FewRel 的 balanced design 和 cross-prompt validation 部分缓解，但不能排除 cluster-level domain difficulty 这一替代解释。\n\n**建议**: 报告 extreme batches 的 type domain 分布。考虑 domain-matched batch construction 作为 robustness check。\n\n**W7 [Major, R1 raised + R2 AGREE]: 共享 text instances 的 bootstrap CI 可能 anti-conservative。**\n\n1000 个 text instances 跨所有 batches 共享。Instance-level cross-batch correlation 未被 batch-level bootstrap 处理。Appendix R 的 variance decomposition 部分缓解，但形式上 CI 可能偏窄。\n\n**建议**: 提供 cluster-robust SE（cluster on text instance）或 split-sample bootstrap 作为 sensitivity check。\n\n### Minor\n\n**M1**: \"First controlled study\" claim 实质正确但需更精确措辞限定（\"simultaneously isolating count and inter-type confusability as independent dimensions using embedding-based metrics and controlled batch design\"）。[R2 raised, R1 partial REBUT — 同意限定措辞]\n\n**M2**: NER null framing 偏向 \"低 power\" 解释，应同等考虑 \"NER 任务特性\"（span detection dominance over type classification）作为替代解释。Relaxed matching (Appendix) 仍 null 支持此解读。[R1+R2 AGREE]\n\n**M3**: Discussion 缺少理论层面讨论——为什么 embedding similarity 能预测 LLM type confusion？[R1+R2 AGREE]\n\n**M4**: §5 SDGD 应保留在正文（叙事弧需要）但需压缩，将算法细节移入 appendix。Cross-model validation 的关键表应提升到正文。[R1 keep + R2 demote → 共识: keep but compress]\n\n**M5**: 多重比较无正式校正。核心 claims (p<0.001) 不受影响，但边缘结果（logit interaction p=0.047）在校正后可能 non-significant。[R1+R2 AGREE]\n\n**M6**: 遗漏引用 3 篇: Zhang et al. AAAI 2026 (Reflect then Learn, introspective confusion), NER Retriever (Findings EMNLP 2025, type-aware embeddings), Show Less Instruct More (2024, definition quality for zero-shot NER)。[R2 identified, R1 agrees on 3/4]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. BCS 干净证据仅 FewRel RE，论文需明确限定适用范围\n2. DocRED VIF=50.9 下的 partial correlation 不可信，不应作为支持证据\n3. Count 退化故事跨 4 数据集 4 模型扎实，是 solid contribution\n4. BCS-controlled batch design 是方法论创新\n5. 统计严谨度和 appendix 质量显著高于同类工作\n6. \"Drives\" 应替换为 \"predicts\"\n7. TOST \"independently addressable\" claim 需弱化\n\n## Reviewer Divergence [Partial disagreement]\n\n1. **Domain concentration confound (W6)**: R1 认为需要严格验证；R2 认为 balanced design + cross-prompt 提供部分缓解但同意报告 domain 分布。**结论**: 建议作为 should-fix（报告 domain 分布），非 must-fix。\n\n2. **SDGD section 定位 (M4)**: R2 建议降级为 appendix；R1 认为叙事弧需要保留。**结论**: 保留但压缩。\n\n3. **\"First controlled study\" claim (M1)**: R2 认为 Chen et al./GoLLIE/Reflect 相关；R1 认为这些工作 scope 不同，claim 实质正确。**结论**: 措辞限定即可。\n\n---\n\n## Questions（需作者澄清）\n\nQ1. 能否在一个 BCS-centrality VIF < 5 的新数据集上重复 BCS-controlled 实验？这是提升论文最直接的路径。\n\nQ2. DocRED VIF=50.9 下报告的 partial correlation p<0.001 是否经过 variance inflation 调整？能否提供 ridge regression 结果？\n\nQ3. High-BCS extreme batches 中的 relation types 是否集中在特定语义域（如 kinship, spatial）？\n\nQ4. 跨 batch 共享 text instances 对 bootstrap CI 宽度的影响有多大？Split-sample bootstrap 结果如何？\n\nQ5. NER batch-level null 在 3 模型 + 2 prompts + relaxed matching 上一致——作者是否认为这更可能反映 NER 任务特性而非 power 不足？\n\nQ6. 如果 logit scale 上存在边缘显著的 count×BCS interaction (p=0.047)，\"independently addressable\" claim 是否需要根本性修改？\n\n---\n\n## Missing References\n\n1. Zhang et al. \"Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion\" (AAAI 2026) — content uncertainty 与 type confusability 直接相关\n2. \"NER Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings\" (Findings EMNLP 2025) — type-aware embeddings 方法论相关\n3. \"Show Less, Instruct More: Enriching Prompts with Definitions and Guidelines for Zero-Shot NER\" (2024) — definition quality 影响 zero-shot NER\n\n---\n\n## External Review\n\n**状态**: 未请求（项目未启用外部审稿）\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（2026-05-22 04:14 → 04:18）。发现：\n\n- **[Critical]** Appendix p.26: Table 28 仅占页面 1/4，下方 ~3/4 空白。应调整 float 位置消除空白。\n- **[Warning]** pp.1-2: 前 2 页纯文本无 display item，建议 Introduction 末尾加概览 figure（方法流程图或核心发现 teaser）。\n- **[Warning]** p.8: 正文末页压缩 4 个 section（4.4/4.5后半/5/6），Discussion 感觉草草收尾。\n- **[Warning]** pp.5-8: 正文仅 4 个 display items（2 fig + 2 table），大量结果在 appendix。建议提升 1-2 个关键 appendix 表到正文。\n- **[Info]** Figure 1(b) x 轴标签使用缩写（intA_type 等），不够直观。\n- **[Info]** Figure 2 灰度打印下颜色区分度不足。\n- **[Info]** 整体排版专业，无 LaTeX 渲染错误、margin 溢出或未解析引用。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 / 5 (Borderline Conference)\n\n**EMNLP 2026 标准**: 3.5 = Borderline Conference（可被主会议接收的边缘）\n\n**置信度**: 4/5（两位 Reviewer 均仔细阅读全文及全部 appendix，逐一核查统计方法论）\n\n**理由**:\n\n论文有两个明确的贡献维度：(1) Count 退化的系统性实证——4 数据集、4 模型一致，效应量大，是 solid contribution；(2) BCS-controlled batch design 是方法论创新。然而，BCS 作为 confusability predictor 的核心证据仅在 FewRel RE 上 confound-free（VIF=1.18），另外 3 个数据集均有严重问题（DocRED VIF=50.9 不可解释、MAVEN 归因于 centrality、NER null）。这使得论文的主要叙事——confusability 是独立退化维度——在泛化性上显著受限。\n\n如果作者能在 rebuttal 中：(a) 补充 1 个 VIF 可控的新数据集 BCS-controlled 结果，或 (b) 对 DocRED 提供 ridge regression robustness check 证实 BCS 有独立贡献，或 (c) 将 claim scope 明确限定为 RE 并相应调整 title/abstract，评分可上调至 4.0 (Conference)。\n\n当前状态建议 **Findings 接收**——统计严谨度和实验方法论质量足以接收，但泛化性不足以支撑 main conference。\n\n---\n\n## Detailed Comments（逐节）\n\n**Abstract**: 信息密度可接受但 \"drives\" 需改为 \"predicts\"。SCS 的具体含义（pairwise cosine similarity between type-name embeddings）应在 abstract 中明确。\n\n**§1 Introduction**: RQ 设置清晰。\"First controlled study\" claim 需限定。Contribution list 的第 2 点（task asymmetry）与第 1 点有较多重叠。\n\n**§2 Related Work**: 覆盖面良好。缺 Zhang et al. AAAI 2026。\"SCS novelty\" 段的自我定位诚实但可能不够自信。\n\n**§3 Experimental Setup**: 设计精良。Table 1 \"BCS ranges not comparable across embedding models\" 这一限制对结论的影响应展开讨论。\n\n**§4 Results**: Count curves (§4.1) 扎实。BCS-controlled (§4.3) 的 FewRel 结果令人信服。DocRED 结果需 downgrade 呈现方式。TOST (§4.4) 需报告两个量表结论。NER null 需平衡解释。\n\n**§5 SDGD**: 叙事逻辑合理但需压缩。Oracle routing insight (72.4% vs 50.4%) 有价值。\n\n**§6 Discussion**: 过短。需添加 \"why embedding similarity predicts LLM confusion\" 的理论讨论。Practical implications 已改善但仍可更具体。\n\n**Limitations**: 全面。Item 1 正确标注了单模型分析的范围。\"Cannot distinguish\" 表述正确但应同等权重讨论 \"NER 任务特性\" 替代解释。\n",
    "project": "schema-dag-extraction",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5",
    "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
  }
}
```

</details>

---


### Tool result

_source line 2949 · 2026-05-22T04:30:39.403192+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_51326259fe46fbae9da26b81cf03f1f8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4560
}
```

</details>

---


### Assistant

_source line 2950 · 2026-05-22T04:30:49.501936+00:00_

审稿报告已投递至 Research Director。

---

**Round 29 审稿完成**

| 项目 | 结果 |
|------|------|
| Overall | **3.5/5 (Borderline Conference)** |
| 建议 | Findings 接收 |
| Reviewer 共识 | 两位 Reviewer 一致评分，交叉分享后核心判断完全收敛 |
| Critical 问题 | 2 个（BCS 证据仅 FewRel 干净 + DocRED VIF=50.9 不可信） |
| Major 问题 | 5 个（novelty 有限、TOST 量表依赖、因果语言、domain confound、bootstrap 依赖） |
| Minor 问题 | 6 个 |
| 上调路径 | 补充 1 个 VIF 可控数据集 BCS 实验 / DocRED ridge regression / 明确限定 scope 为 RE → 可至 4.0 |

Issue Tracker 已同步更新（13 条活跃 issue）。视觉审查结果已纳入报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 246

## Round 246

2 recorded events


### User

_source line 2951 · 2026-05-22T04:30:52.228378+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。核心判断：

- **与 R2 收敛**：BCS 证据过度依赖 FewRel（R2-W2 = R1-W1）、指标本身非新（R2-W1）
- **与 R2 分歧**：SDGD §5 应保留在 main text（[REBUT] R2-W4）——它是叙事弧的关键环节；"First controlled study" claim 实质正确但需限定措辞（[REBUT] R2-W3）
- **升分条件**：补充 1 个 VIF 可控数据集的 BCS-controlled 结果，或 DocRED ridge regression robustness check

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2952 · 2026-05-22T04:31:04.969127+00:00_

审稿报告已投递完毕。

**本轮审稿总结**：

- **Overall**: 3.5/5 (Borderline Conference)，建议 Findings 接收
- **2 个 Critical**: BCS 干净证据仅 FewRel（4 数据集中 3 个有问题）；DocRED VIF=50.9 处理不充分
- **5 个 Major**: SCS/BCS 新颖性有限、TOST 量表依赖、因果语言、domain concentration confound、bootstrap 依赖性
- **6 个 Minor**: claim 措辞精度、NER null 解释平衡、Discussion 理论深度、SDGD 压缩、多重比较校正、缺 3 篇引用
- **升分路径**: 补 1 个 VIF 可控数据集 BCS 验证 / DocRED ridge regression / 明确限定 scope 为 RE

Issue Tracker 已同步更新至 `review_issues.yaml`（13 个 open issues）。报告已投递至 Research Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 247

## Round 247

70 recorded events


### User

_source line 2953 · 2026-05-22T07:26:13.702594+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: schema-dag-extraction
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2026
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2954 · 2026-05-22T07:26:20.285772+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2955 · 2026-05-22T07:26:20.337469+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2956 · 2026-05-22T07:26:27.280042+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,WebSearch",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,WebSearch",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 2957 · 2026-05-22T07:26:27.280486+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2958 · 2026-05-22T07:26:30.352759+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer",
    "max_results": "6"
  }
}
```

</details>

---


### Tool result

_source line 2959 · 2026-05-22T07:26:30.353868+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 2960 · 2026-05-22T07:26:34.120821+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer",
    "max_results": "6"
  }
}
```

</details>

---


### Tool result

_source line 2961 · 2026-05-22T07:26:34.171497+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2962 · 2026-05-22T07:26:38.439727+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 2963 · 2026-05-22T07:26:39.344432+00:00_

{"result":"# 项目 schema-dag-extraction 概况\n\n## 实验状态 (69 个)\n\n- **exp012_llama_8b_r2_exp2**: DONE (negative) — \n- **exp012_llama_8b_r2**: DONE (success) — \n- **exp006_interaction_2x2**: DONE (negative) — \n- **exp012_llama_awq**: DONE (killed) — \n- **exp012_llama_8b_r3**: DONE (failed) — \n- **exp012_llama_8b**: DONE (killed) — \n- **exp_fewrel_40rel_r3**: DONE (failed) — \n- **exp_fewrel_40rel_r2**: DONE (failed) — \n- **exp012_llama_fewnerd_r4**: DONE (failed) — \n- **exp012_llama_8b_fewnerd**: DONE (failed) — \n- **exp_fewrel_40rel**: DONE (failed) — \n- **exp012_llama_fewnerd_r3**: DONE (failed) — \n- **exp012_llama_fewnerd_r2**: DONE (failed) — \n- **exp012_llama_fewnerd**: DONE (failed) — \n- **exp008_sdgd_zero_fewnerd**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- prompt_sensitivity（准备中）\n- prompt_sensitivity_dry4（准备中）\n- prompt_sensitivity_dry3（准备中）\n- prompt_sensitivity_dry2（准备中）\n- prompt_sensitivity_dry（准备中）\n- exp_aggregation_monte_carlo（准备中）\n- exp_scs_name_def_ablation（准备中）\n- exp_fewrel_contamination_check（准备中）\n- exp017_gpt4o_mini_fewrel（准备中）\n- exp_cross_embedding_sensitivity（准备中）\n- …另有 2 项\n\n## 近期结论\n- **exp_llama70b_ner_bcs_null** (success): Batch-level BCS does not correlate with NER F1 for LLaMA-3.1-70B-FP8, consistent with the BCS null observed in Qwen3-32B (r=0.004) and LLaMA-8B (r=-0.12). The confusability metric is not predictive of extraction quality at the batch level. ← 基于 exp012_llama_8b_r2_exp2\n  [LLaMA-70B NER BCS-null analysis](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_llama70b_ner_bcs_null/data/bcs_null_analysis.json)\n- **exp_gemini_flash_bcs_controlled** (success): BCS-accuracy negative correlation observed on open-weight models (Qwen3-32B, LLaMA) generalizes to proprietary API models. Gemini 2.5 Flash should show significant BCS gap on extreme-BCS batches at count 8 and count 16, confirming Dimension 2 is architecture-family-in
…[truncated 1221 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 2964 · 2026-05-22T07:26:39.848518+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 2965 · 2026-05-22T07:26:40.803130+00:00_

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
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	\usepackage{listings}
16	
17	\title{How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	
28	\input{related_work}
29	
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	\begin{enumerate}[leftmargin=*,itemsep=2pt]
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B; cross-model validation (LLaMA-8B, LLaMA-70B, Gemini Flash) covers Dimensions~1--2 (count curves, BCS-controlled extremes) but does not replicate secondary analyses (error taxonomy, prompt sensitivity, TOST equivalence). Specifically, TOST factorial interaction (\S\ref{sec:multi_channel}) and SDGD failure analysis (\S\ref{sec:sdgd}) are established on Qwen3-32B alone; error taxonomy replicates on two additional models (Table~\ref{tab:cross_model_error_taxonomy}), but TOST and SDGD cross-model replication remains the most pressing extension. Gemini provides only partial, leverage-sensitive corroboration (leave-one-out $r{:}\;{-}0.80 \to {-}0.42$; Appendix~\ref{sec:appendix_cross_model_gemini}); proprietary-model generalization remains open.
41	
42	\item \textbf{Effect size and statistical design.} Pairwise SCS explains a small fraction of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\times$ BCS interaction is bounded on FewRel but nonzero on DocRED, partially confounded by BCS range restriction at higher counts (Appendix~\ref{sec:appendix_factoria
…[truncated 4758 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 2966 · 2026-05-22T07:26:40.803751+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 author guidelines submission format requirements site:aclrollingreview.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 author guidelines submission format requirements site:aclrollingreview.org"
  }
}
```

</details>

---


### Tool call

_source line 2967 · 2026-05-22T07:26:41.205626+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "memory.md"
  }
}
```

</details>

---


### Tool result

_source line 2968 · 2026-05-22T07:26:49.438227+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 author guidelines submission format requirements site:aclrollingreview.org"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

Based on the search results from the ACL Rolling Review website, here are the key author guidelines and submiss
…[truncated 1393 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 8634
}
```

</details>

---


### Tool result

_source line 2969 · 2026-05-22T07:26:49.489953+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/memory.md\", \"content\": \"# Memory — schema-dag-extraction\\n\\n## DocRED expanded: interaction reversed, R² increased (2026-05-19)\\n- 原 n=5 per condition: interaction=+5.7pp CI[-1.6, 13.0], R²=0.525 (count16)\\n- 扩展 n=15 per condition (n=55 per count level): interaction=-9.4pp CI[-12.9, -6.0], R²=0.653 (count16), R²=0.614 (count32)\\n- **方向翻转**: 从不确定(+5.7pp, CI 含零)变为确定 sub-additive(-9.4pp, CI 不含零)\\n- BCS effect 从 -25.0pp (count16) 衰减到 -15.7pp (count32)，符合 floor compression\\n- **教训**: 小样本(n=5)的交互估计极不稳定，符号都可以翻转\\n- 论文范围从 \\\"22-53%\\\" 更新为 \\\"22-65%\\\"\\n\\n## MAVEN SDGD: merge amplification 跨任务确认 (2026-05-19)\\n- Single-pass F1=0.207 > SDGD-zero F1=0.123 > random-batch F1=0.111\\n- Precision collapse 0.287→0.091 (-19.6pp), pred_count inflation 3.7×\\n- 与 Few-NERD NER 一致：分解策略在所有 span-based tasks 上因 merge amplification 失败\\n- SDGD-zero 略优于 random (+1.2pp F1)，但均远低于 single-pass\\n\\n## exp_schema_intervention: renaming 不是有效干预手段 (2026-05-17, negative)\\n- Renaming 降低两组 accuracy：high-BCS -8.83pp, low-BCS -2.96pp (both p<0.001)\\n- Interaction 显著 (-5.88pp, p<0.001)：high-BCS 受损更大，但方向是 renaming 损害而非改善\\n- 根因：LLM 对 original type names 有 strong prior，renaming 引入 label unfamiliarity confound\\n- Solo sanity check 11/12 通过，但 multi-type batch 中 compound effect 出现 (r=-0.625)\\n- **教训**：post-hoc renaming 无法分离 SCS 降低效果与 label unfamiliarity，不可用作因果干预\\n- D059 (Greedy auto-renaming) 基于相同逻辑，也已停止\\n\\n## TUM proxy 不是运行中的服务 (2026-05-17)\\n- TUM 是飞书 key 收集机制，不是 API proxy server\\n- localhost:8001 没有进程监听\\n- `tum_` 前缀的 token 不是有效的 Google/OpenAI API key\\n- 本机能直连 Google API（需要真实 Gemini key, 格式 AIza...）\\n- **教训**：API 实验前必须先验证 (a) proxy 是否运行 (b) key 格式是否匹配目标 API\\n\\n## Q3 held-out validation: FewRel val-origin SCS-confusion (2026-05-17, CORRECTED)\\n- 从 80-type confusion matrix 提取 16 val-origin types 的 C(16,2)=120 pairs\\n- 16 val types 与 64 train types
…[truncated 2866 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 8284
}
```

</details>

---


### Tool call

_source line 2970 · 2026-05-22T07:26:56.188509+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 CFP long paper short paper page limit format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 CFP long paper short paper page limit format"
  }
}
```

</details>

---


### Tool call

_source line 2971 · 2026-05-22T07:26:57.444594+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_round_30/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_round_30/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 2972 · 2026-05-22T07:26:57.946580+00:00_

-rw-r--r-- 1 ubuntu ubuntu 480119 May 22 07:26 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_round_30/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 2973 · 2026-05-22T07:26:58.147512+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 2974 · 2026-05-22T07:27:02.871921+00:00_

Web search results for query: "ACL Rolling Review 2026 CFP long paper short paper page limit format"

Links: [{"title":"LINGUIST List 36.2627 Confs: 19th Conference of the European Chapter of the Association for Computational Linguistics (Morocco)","url":"https://linguistlist.org/issues/36/2627/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, here's the information about ACL Rolling Review 2026 CFP for long and short papers:

## Page Limits

For long papers, the page limit is 8 pages; for short papers, it is 4 pages, not including limitations and ethical considerations. Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

## Format and Requirements

Papers must not include authors' names and affiliations, and self-referen
…[truncated 675 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 6683
}
```

</details>

---


### Tool result

_source line 2975 · 2026-05-22T07:27:02.922790+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/decisions.yaml\", \"content\": \"_next_id: 72\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 16:10 UTC\\n  summary: 项目立项，MVP 验证方案：Experiment 2 (Confusability Controlled) 为核心验证实验\\n  rationale: 'IDEA_BRIEF 的核心假设是 type confusability 独立于 type count 驱动 LLM IE 质量下降。Experiment\\n    2（固定 count 变 BCS）是最直接的假设检验。Pass 标准: |r|≥0.3 且 p<0.05。ACE05 RE + Few-NERD 双数据集验证。ARR\\n    May 25 DDL（11天），MVP 需 1-2 天完成。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 16:15 UTC\\n  summary: 修正 MVP 统计设计：random samples 从 10 增至 25/档，加入 per-type solo baseline 控制变量，核心指标改为\\n    Δ(solo_F1 - batch_F1)\\n  rationale: Reviewer 指出 n=12 下 |r|=0.3 对应 p≈0.34，无法同时满足 |r|≥0.3 且 p<0.05。增至 25 random\\n    batches/档 → n≈54，|r|≥0.27 即可达 p<0.05。同时加入 solo F1 控制 type 固有难度，避免将\\\"类型本身难抽取\\\"误归因于\\\"confusability\\n    效应\\\"。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 23:11 UTC\\n  summary: MVP 分析方法从 Δ(solo-batch) 切换到 within-count Pearson r(F1, BCS)，pass 标准更新为\\n    |r|≥0.3 at fixed count\\n  rationale: Exp 1 发现 count curve 方向反转（F1 随 count 上升），根因是低 count 时模型过度 hallucinate（pred/gold=8x\\n    at count=1）。solo baseline 处于极端行为模式，Δ 被跨 count 行为差异污染。改为 within-count 对比更干净：同一\\n    count 下比较不同 BCS 的 F1，直接检验 confusability 独立效应。\\n  related_experiments:\\n  - exp_id: exp001_count_baseline\\n    role: evidence\\n    result: count curve reversed, hallucination at low count\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 23:31 UTC\\n  summary: MVP 主指标更新为 within-count r(recall, BCS)，F1 因 over-prediction confound 降为补充指标\\n  rationale: Exp 1 text-match 重评估发现：recall 单调下降（0.72→0.42，符合预期），precision 单调上升（0.11→0.52，over-prediction\\n    减少），F1 受 precision 主导而反转。within-count 分析中 precision confound 在同一 count 下近似恒定，F1\\n    仍可用；但 recall 更干净且直接反映 type confusion。WrongType 错误（text 正确但 type 错标）随 count 从 0\\n    升至 2434，直
…[truncated 1449 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 4775
}
```

</details>

---


### Tool call

_source line 2976 · 2026-05-22T07:27:12.472049+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/",
  "description": "List paper directory files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/",
    "description": "List paper directory files"
  }
}
```

</details>

---


### Tool result

_source line 2977 · 2026-05-22T07:27:12.673409+00:00_

_pdf_check
_pdf_check10
_pdf_check2
_pdf_check3
_pdf_check4
_pdf_check5
_pdf_check6
_pdf_check7
_pdf_check8
_pdf_check9
_pdf_images
abstract.tex
acl.sty
acl_natbib.bst
checklist.tex
conclusion.tex
discussion.tex
experimental_setup.tex
introduction.tex
main.aux
main.bbl
main.blg
main.fdb_latexmk
main.fls
main.log
main.out
main.pdf
main.tex
prompt_appendix.tex
references.bib
related_work.tex
results.tex
sdgd_negative.tex
supplementary.bbl
supplementary.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 2978 · 2026-05-22T07:27:13.175580+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent/config.yaml 2>/dev/null | head -100",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent/config.yaml 2>/dev/null | head -100",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 2979 · 2026-05-22T07:27:13.780138+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 604
}
```

</details>

---


### Tool call

_source line 2980 · 2026-05-22T07:27:14.236089+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NO_FILE\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NO_FILE\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 2981 · 2026-05-22T07:27:14.286744+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2982 · 2026-05-22T07:27:18.058059+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent/config.yaml 2>/dev/null; echo \"---END---\"; find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent/ -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -20",
  "description": "Find and read project config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent/config.yaml 2>/dev/null; echo \"---END---\"; find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent/ -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -20",
    "description": "Find and read project config"
  }
}
```

</details>

---


### Tool result

_source line 2983 · 2026-05-22T07:27:18.510409+00:00_

---END---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2984 · 2026-05-22T07:27:18.661555+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2985 · 2026-05-22T07:27:18.712384+00:00_

1	# Review Issues Tracker
2	# Updated: 2026-05-22 (ALL R29 fixes complete)
3	
4	# ============================================================
5	# R29 CRITICAL (2 items)
6	# ============================================================
7	
8	- id: R29-C1
9	  summary: "BCS 度量的干净证据仅限 FewRel RE 一个数据集，论文叙事暗示更广泛适用性"
10	  category: framing
11	  severity: critical
12	  status: in_progress
13	  first_raised_round: 23
14	  last_seen_round: 29
15	  mentions:
16	    - {round: 23, reviewers: [R1, R2], note: "R23-C2: weaken wording"}
17	    - {round: 24, reviewers: [R1, R2], note: "R24-C1: recenter on FewRel"}
18	    - {round: 25, reviewers: [R1, R2], note: "R25-C2: confusability scope overclaim"}
19	    - {round: 29, reviewers: [R1, R2], note: "R1-W1 + R2-W2 AGREE. Abstract 'drives' overgeneralizes."}
20	  action_items:
21	    - {round: 25, action: "Weaken title/abstract/conclusion generality claims", assigned_to: "Agent", status: done}
22	    - {round: 29, action: "Abstract rewritten: 'predicts' not 'drives', explicit FewRel RE scope (R²≈0.22, VIF=1.18), NER null stated. Intro contribution limited to FewRel.", assigned_to: "Agent", status: done}
23	  resolution: "Abstract + Intro rewritten with explicit FewRel-only BCS scope. 'drives'→'predicts' throughout."
24	  resolution_round: null
25	
26	- id: R29-C2
27	  summary: "DocRED VIF=50.9 的 partial correlation 不可信但仍作为支持证据呈现"
28	  category: method
29	  severity: critical
30	  status: in_progress
31	  first_raised_round: 23
32	  last_seen_round: 29
33	  mentions:
34	    - {round: 23, reviewers: [R1, R2], note: "R23-C2: VIF=50.9"}
35	    - {round: 25, reviewers: [R1, R2], note: "R25-C1: must report semipartial R²"}
36	    - {round: 29, reviewers: [R1, R2], note: "R1-W2, R2 AGREE. §4.3 still presents DocRED R² misleadingly."}
37	  action_items:
38	    - {round: 25, action: "Report semipartial ΔR²_BCS=5.6%", assigned_to: "Agent", status: done}
39	    - {round: 29, action: "Added explicit VIF=50.9 caveat ('SE inflated ~7x, directional ev
…[truncated 3195 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2986 · 2026-05-22T07:27:22.679468+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml",
  "offset": "100",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml",
    "offset": "100",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2987 · 2026-05-22T07:27:23.387990+00:00_

100	  first_raised_round: 29
101	  last_seen_round: 29
102	  mentions:
103	    - {round: 29, reviewers: [R1, R2], note: "R1-W5, R2 partial REBUT. Both agree: report domain distribution."}
104	  action_items:
105	    - {round: 29, action: "FewRel domain distribution analysis done (χ²=230.74, p<0.001). High-BCS→taxonomy/temporal, low-BCS→geography/creative. Framed as mediator (error taxonomy IntraSub evidence confirms type substitution mechanism). Added to Appendix E.4.", assigned_to: "Agent", status: done}
106	  resolution: "Domain distribution reported transparently. Mediator argument supported by IntraSub-BCS correlation."
107	  resolution_round: null
108	
109	- id: R29-W5
110	  summary: "共享 text instances 的 bootstrap CI 可能 anti-conservative"
111	  category: method
112	  severity: warning
113	  status: in_progress
114	  first_raised_round: 29
115	  last_seen_round: 29
116	  mentions:
117	    - {round: 29, reviewers: [R1, R2], note: "R1-W6, R2 AGREE. Formal concern about cross-batch correlation."}
118	  action_items:
119	    - {round: 29, action: "Cluster-robust SE analysis (n=164, 6 Jaccard thresholds): SE inflation 0.96-0.97× (no inflation). CI width change -1.5%. All p<10⁻¹¹. Added to Appendix E.3.", assigned_to: "Agent", status: done}
120	  resolution: "Cluster-robust SE confirms no CI inflation from shared instances. DEFF=5.4 but slope estimation unaffected."
121	  resolution_round: null
122	
123	# ============================================================
124	# R29 MINOR (6 items)
125	# ============================================================
126	
127	- id: R29-M1
128	  summary: "'First controlled study' claim needs more precise scoping"
129	  category: writing
130	  severity: info
131	  status: in_progress
132	  first_raised_round: 25
133	  last_seen_round: 29
134	  mentions:
135	    - {round: 25, reviewers: [R1, R2], note: "R25-W8: scope more precisely"}
136	    - {round: 29, reviewers: [R1, R2], note: "R2-W3, R1 partial REBUT. Both agree on precise wo
…[truncated 3121 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 708
}
```

</details>

---


### Tool call

_source line 2988 · 2026-05-22T07:27:23.538914+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ -path \"*/agent/*\" -name \"*.yaml\" -o -path \"*/agent/*\" -name \"*.yml\" 2>/dev/null | head -20",
  "description": "Find config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ -path \"*/agent/*\" -name \"*.yaml\" -o -path \"*/agent/*\" -name \"*.yml\" 2>/dev/null | head -20",
    "description": "Find config files"
  }
}
```

</details>

---


### Tool result

_source line 2989 · 2026-05-22T07:27:23.640164+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2990 · 2026-05-22T07:27:26.890031+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ -maxdepth 3 -name \"config*\" 2>/dev/null | head -20",
  "description": "Find config files in project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ -maxdepth 3 -name \"config*\" 2>/dev/null | head -20",
    "description": "Find config files in project"
  }
}
```

</details>

---


### Tool result

_source line 2991 · 2026-05-22T07:27:27.191631+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/ace05_code/configs
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/maven_code/configs
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/configs

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 2992 · 2026-05-22T07:27:27.242429+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml",
  "offset": "199"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml",
    "offset": "199"
  }
}
```

</details>

---


### Tool result

_source line 2993 · 2026-05-22T07:27:27.293066+00:00_

199	
200	- id: R29-M6
201	  summary: "Missing references: Reflect then Learn (AAAI 2026), NER Retriever (EMNLP 2025 Findings), Show Less Instruct More (2024)"
202	  category: writing
203	  severity: info
204	  status: in_progress
205	  first_raised_round: 29
206	  last_seen_round: 29
207	  mentions:
208	    - {round: 29, reviewers: [R1, R2], note: "R2 identified, R1 agrees on 3. Reviewer notes Golde 2025 already cited, Show Less may overlap with GoLLIE."}
209	  action_items:
210	    - {round: 29, action: "NER Retriever (EMNLP 2025 Findings) added to bib + related_work.tex. Reflect then Learn reused existing bib key reflect-learn-2026 + added citation in related_work.tex. Show Less skipped (redundant with GoLLIE).", assigned_to: "Agent", status: done}
211	  resolution: "2/3 references added. Show Less skipped per reviewer's own GoLLIE overlap note. Compile: 0 errors, 0 undefined refs, body=8pp."
212	  resolution_round: null
213	
214	# ============================================================
215	# HISTORICAL — Issues from R23-R25 now superseded by R29
216	# ============================================================
217	# All R25 issues merged into R29 where applicable.
218	# R25-C1 → R29-C2 (DocRED VIF)
219	# R25-C2 → R29-C1 (BCS scope)
220	# R25-C3 → R29-M2 (NER null)
221	# R25-C4 → R29-W1 (contribution framing)
222	# R25-W4 → R29-W2 (TOST scale)
223	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2994 · 2026-05-22T07:27:30.660041+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/configs/*.yaml 2>/dev/null | head -150",
  "description": "Read project configs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/configs/*.yaml 2>/dev/null | head -150",
    "description": "Read project configs"
  }
}
```

</details>

---


### Tool result

_source line 2995 · 2026-05-22T07:27:30.710771+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2996 · 2026-05-22T07:27:34.025548+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/configs/ 2>/dev/null",
  "description": "List config directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/configs/ 2>/dev/null",
    "description": "List config directory"
  }
}
```

</details>

---


### Tool result

_source line 2997 · 2026-05-22T07:27:34.076476+00:00_

few_nerd_types.json
fewrel_relation_types.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2998 · 2026-05-22T07:27:37.292036+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/ -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | grep -i config | head -20",
  "description": "Find project config yaml files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/ -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | grep -i config | head -20",
    "description": "Find project config yaml files"
  }
}
```

</details>

---


### Tool result

_source line 2999 · 2026-05-22T07:27:37.443102+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/resources.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/pending_approval_notifications.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 3000 · 2026-05-22T07:27:41.160030+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/ 2>/dev/null; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ --include=\"*.yaml\" --include=\"*.yml\" 2>/dev/null | head -10",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/ 2>/dev/null; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ --include=\"*.yaml\" --include=\"*.yml\" 2>/dev/null | head -10",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 3001 · 2026-05-22T07:27:41.261151+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 3002 · 2026-05-22T07:27:55.345471+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 3003 · 2026-05-22T07:27:55.646967+00:00_

1	\begin{abstract}
2	Schema complexity affects training-free LLM information extraction through two independent dimensions: type count drives recall decline, while inter-type confusability predicts type substitution errors. We present what is, to our knowledge, the first controlled study isolating these factors in zero-shot LLM IE across NER, RE, and event detection on four datasets. Using embedding-based confusability metrics (SCS/BCS) with controlled batch design, we find:
3	(1)~count degradation spans all three tasks (up to $-$49\,pp); inter-type confusability (measured by BCS) independently predicts RE type substitution errors (VIF${}\,=\,1.18$ on FewRel);
4	(2)~BCS explains ${\sim}$22\% of cross-batch RE accuracy variance on FewRel ($R^2 \approx 0.22$, ecological level), replicating across three open-weight model families (8B--70B); NER batch-level signal is not detected at current power;
5	(3)~schema decomposition fails due to merge amplification and routing failure, though oracle routing confirms the two dimensions are independently addressable.
6	\end{abstract}
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 3004 · 2026-05-22T07:27:55.647285+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 3005 · 2026-05-22T07:27:56.149479+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\looseness=-1
5	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\footnote{Code and data will be released upon acceptance.} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, and is attractive for applications where annotation is expensive or schemas evolve frequently \citep{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level), near-halving or worse. This degradation is not academic: real-world ontologies routinely define 50--200+ types, which places them squarely in the regime where training-free extraction becomes unreliable.
6	
7	\looseness=-1
8	What explains this degradation? Prior decomposition strategies \citep{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
9	
10	This study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accuracy.
11	
12	We ask three questions. \textbf{RQ1}: Does type
…[truncated 3297 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 3006 · 2026-05-22T07:27:56.149901+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 3007 · 2026-05-22T07:27:56.602007+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	\looseness=-1
6	Training-free LLM IE spans instruction tuning \citep{instructuie-2023}, code-style schema encoding \citep{knowcoder-2024,codeie-2023}, annotation-guided extraction \citep{gollie-2024,adelie-2024}, schema-driven decoding \citep{slot-2025,oneke-2025}, and constrained JSON decoding \citep{json-schema-bench-2025,willard2023efficient}. NER methods include zero-shot decomposition \citep{xie-zeroshot-ner-2023,promptner-2023}, distillation \citep{uniner-2024}, and bidirectional encoders \citep{gliner-2024,gliner2-2025}; RE methods include zero-shot triplet extraction \citep{relationprompt-2022}, constrained generation \citep{josifoski-2022-genie}, and shared embedding spaces \citep{boylan-2025-glirel,wadhwa-re-llm-2023}. Related work also exploits type embeddings for retrieval \citep{shachar-2025-ner-retriever} and introspective confusion for example selection \citep{reflect-learn-2026}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales.
7	
8	\paragraph{Schema complexity in IE.}
9	\looseness=-1
10	The most directly related work is LLM-PEE \citep{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. LLM-PEE's union merge suffers the same precision collapse (0.56$\to$0.21; \S\ref{sec:sdgd}). In short, LLM-PEE assumes decomposition helps; we show why it should (confusability), why it does not (merge amplification), and what predicts the degradation (BCS). Other approaches 
…[truncated 2503 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 3008 · 2026-05-22T07:27:56.702744+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 3009 · 2026-05-22T07:27:56.703397+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \citep{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains. We sample 1{,}000 instances uniformly from the test set; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \citep{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments. We sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). A held-out validation confirms SCS--confusion generalization across the split boundary (Appendix~\ref{app:scs-heldout-validation}). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound; this balance makes it the primary dataset for BCS analysis. Contamination analysis (Appendix~\ref{app:split-origin}) shows extraction difficulty correlates inversely with training-set prevalence, and BCS effects are unchanged when controlling for contamination.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocR
…[truncated 9385 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 3010 · 2026-05-22T07:27:57.055176+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 3011 · 2026-05-22T07:27:58.009635+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	All experiments use Qwen3-32B and the v1 prompt (\S\ref{sec:model}; Appendix~\ref{sec:appendix_prompts}) unless noted; cross-model validation covers Dimensions~1--2, while secondary analyses (error taxonomy, DocRED $R^2$, TOST) remain single-model.
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	\looseness=-1
10	Figure~\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where eliminating type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\%$\to$38.7\%, $-$56\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}). The pattern is stable across three seeds (max $\Delta = 10.7$\,pp, within 1\,SD; intra-batch variance exceeds inter-seed variance by ${>}$5$\times$; Appendix~\ref{app:variance-decomposition}). Formal trend analysis confirms monotonic RE decline (Jonckheere-Terpstra $J = 109{,}707$, $p < 0.001$). Count decline replicates on LLaMA-70B with comparable magnitude and on Gemini Flash (Appendix~\ref{sec:appendix_cross_model_gemini}). Count curves establish trend direction; magnitude estimation relies on the higher-powered BCS-controlled experiments (\S\ref{sec:bcs_controlled}).
11	
12	\subsection{Pairwise Confusability and Type Confusion}
13	\label{sec:pairwise}
14	
15	We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate (the fraction of $t_i$ gold instances misclassified as $t_j$) and correlate it with $\text{SCS}(t_i, t_j)$. Table~\ref{tab:pairwise} reports Pearson correlations w
…[truncated 13118 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 3012 · 2026-05-22T07:27:58.010174+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 3013 · 2026-05-22T07:27:58.161158+00:00_

1	\section{Schema Decomposition}
2	\label{sec:sdgd}
3	
4	\looseness=-1
5	A natural intervention is to partition the schema so confusable types never co-occur. We tested Schema-DAG-Guided Decomposition (SDGD), which applies greedy graph coloring on the SCS graph to assign types to low-confusability batches. While oracle routing recovers accuracy (0.802 vs.\ 0.504 single-pass), all practical routing strategies fall below the single-pass baseline, and NER decomposition amplifies false positives (F1: 0.445$\to$0.251). The bottleneck is routing accuracy rather than partitioning quality. Full protocol, results, and analysis are in Appendix~\ref{sec:appendix_sdgd}.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 3014 · 2026-05-22T07:27:58.161511+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 3015 · 2026-05-22T07:27:58.212508+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	\looseness=-1
6	The confusability signal applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\S\ref{sec:centrality_confound}). Modest pairwise $r^2$ compounds at the batch level because correlated type interactions aggregate within shared prompts (\S\ref{sec:bcs_controlled}). The NER--RE asymmetry reflects dispersed error modes and compressed BCS variance (Appendix~\ref{sec:appendix_ner_power}).
7	
8	\paragraph{Practical implications and conclusion.}
9	\label{sec:conclusion}
10	\looseness=-1
11	For NER, reducing candidate types is the primary lever; for RE, pre-computing SCS flags high-risk type pairs before deployment. Decompose-then-merge fails (\S\ref{sec:sdgd}), but oracle routing recovers accuracy, confirming approximate additivity of count and confusability (\S\ref{sec:multi_channel}); separability holds on the linear scale but remains open on the logit scale.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3016 · 2026-05-22T07:28:19.972364+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "schema-dag-extraction",
  "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "schema-dag-extraction",
    "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
  }
}
```

</details>

---


### Tool result

_source line 3017 · 2026-05-22T07:28:35.355100+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 15382
}
```

</details>

---


### Tool call

_source line 3018 · 2026-05-22T07:28:36.360259+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 1，负责审查**方法严谨性**。\n\n## 论文信息\n- **标题**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n- **Venue**: EMNLP 2026 via ARR May 2026\n- **格式**: ACL 模板，long paper 8页正文限制 + 无限参考文献，Limitations 不计入页数\n- **匿名规则**: Double-blind\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_round_30/submitted.pdf`\n\n## 你的审查侧重\n\n重点审查以下方面：\n\n1. **实验设计合理性**：\n   - 两种实验范式（Count Curves + BCS-Controlled）是否足以支撑论文的核心 claim\n   - 控制变量是否充分（type frequency、domain、prompt sensitivity 等）\n   - 样本量是否足够（每个 count level 的 batch 数量、评估样本数）\n   - BCS-controlled 极端 batch 构造方法（greedy search）是否引入 bias\n\n2. **统计分析严谨性**：\n   - 相关性分析（Pearson/Spearman）的使用是否恰当\n   - TOST 等价性检验的 margin 选择是否合理（±2-3pp）\n   - Bootstrap CI 的使用是否正确（特别是共享 text instances 的跨 batch 相关性问题）\n   - 多重比较问题处理\n   - DocRED VIF=50.9 的 partial correlation 可信度\n   - R² 解释（ecological level vs individual level）\n\n3. **跨模型验证**：\n   - Qwen3-32B 为主模型，LLaMA-8B/70B/Gemini Flash 为验证\n   - 验证覆盖哪些维度、哪些未覆盖\n   - Gemini Flash 的 leverage sensitivity（leave-one-out r 从 -0.80 变到 -0.42）\n\n4. **可重复性**：\n   - 单 seed greedy decoding 的结果稳定性\n   - 数据/代码是否承诺公开\n   - FewRel 潜在数据污染问题的处理\n\n5. **格式合规**：\n   - 正文是否在 8 页内\n   - 是否符合 ACL 模板要求\n   - 匿名性是否满足\n\n请逐项给出详细评审意见，标注 [STRENGTH] 或 [WEAKNESS]，weakness 按严重程度分 [CRITICAL]、[MAJOR]、[MINOR]。",
  "reviewer_id": "1",
  "project": "schema-dag-extraction",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 1，负责审查**方法严谨性**。\n\n## 论文信息\n- **标题**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n- **Venue**: EMNLP 2026 via ARR May 2026\n- **格式**: ACL 模板，long paper 8页正文限制 + 无限参考文献，Limitations 不计入页数\n- **匿名规则**: Double-blind\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_round_30/submitted.pdf`\n\n## 你的审查侧重\n\n重点审查以下方面：\n\n1. **实验设计合理性**：\n   - 两种实验范式（Count Curves + BCS-Controlled）是否足以支撑论文的核心 claim\n   - 控制变量是否充分（type frequency、domain、prompt sensitivity 等）\n   - 样本量是否足够（每个 count level 的 batch 数量、评估样本数）\n   - BCS-controlled 极端 batch 构造方法（greedy search）是否引入 bias\n\n2. **统计分析严谨性**：\n   - 相关性分析（Pearson/Spearman）的使用是否恰当\n   - TOST 等价性检验的 margin 选择是否合理（±2-3pp）\n   - Bootstrap CI 的使用是否正确（特别是共享 text instances 的跨 batch 相关性问题）\n   - 多重比较问题处理\n   - DocRED VIF=50.9 的 partial correlation 可信度\n   - R² 解释（ecological level vs individual level）\n\n3. **跨模型验证**：\n   - Qwen3-32B 为主模型，LLaMA-8B/70B/Gemini Flash 为验证\n   - 验证覆盖哪些维度、哪些未覆盖\n   - Gemini Flash 的 leverage sensitivity（leave-one-out r 从 -0.80 变到 -0.42）\n\n4. **可重复性**：\n   - 单 seed greedy decoding 的结果稳定性\n   - 数据/代码是否承诺公开\n   - FewRel 潜在数据污染问题的处理\n\n5. **格式合规**：\n   - 正文是否在 8 页内\n   - 是否符合 ACL 模板要求\n   - 匿名性是否满足\n\n请逐项给出详细评审意见，标注 [STRENGTH] 或 [WEAKNESS]，weakness 按严重程度分 [CRITICAL]、[MAJOR]、[MINOR]。",
    "reviewer_id": "1",
    "project": "schema-dag-extraction",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 3019 · 2026-05-22T07:28:49.235994+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 12875
}
```

</details>

---


### Tool call

_source line 3020 · 2026-05-22T07:28:49.587416+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 2，负责审查**新颖性与完整性**。\n\n## 论文信息\n- **标题**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n- **Venue**: EMNLP 2026 via ARR May 2026\n- **格式**: ACL 模板，long paper 8页正文限制 + 无限参考文献，Limitations 不计入页数\n- **匿名规则**: Double-blind\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_round_30/submitted.pdf`\n\n## 你的审查侧重\n\n重点审查以下方面：\n\n1. **贡献新颖性**：\n   - SCS/BCS 度量相对于 LLM-PEE 的技术新颖性\n   - \"首个控制研究\" 的 claim 是否成立\n   - 实证发现本身的价值（count degradation + confusability prediction）\n   - SDGD 失败是否构成有意义的贡献\n\n2. **Related Work 覆盖**：\n   - 是否遗漏重要相关工作（特别是 2025-2026 年的新工作）\n   - 与 LLM-PEE 的区分是否清晰充分\n   - label confusion / metric learning 方向的引用是否完整\n\n3. **写作质量与 Framing**：\n   - Abstract/Introduction 的 claim 是否与实验证据匹配\n   - 因果语言使用是否恰当（\"drives\" vs \"predicts\"）\n   - 论文叙事结构是否连贯（RQ→实验→发现 的逻辑链）\n   - 结论是否过度泛化（特别是 BCS 仅在 FewRel RE 上干净可证）\n   - Discussion 是否充分讨论了 \"为什么 embedding similarity 预测 LLM type confusion\"\n\n4. **完整性检查**：\n   - Limitations 是否涵盖关键局限\n   - NER null 的讨论是否平衡（power vs task structure）\n   - MAVEN centrality confound 的处理\n   - 是否有需要但缺失的实验\n\n5. **Missing References**：\n   - 搜索 2025-2026 年与 schema complexity、LLM IE、type confusion 相关的新工作\n   - 检查 label space reduction、decomposition 方向的引用\n\n请逐项给出详细评审意见，标注 [STRENGTH] 或 [WEAKNESS]，weakness 按严重程度分 [CRITICAL]、[MAJOR]、[MINOR]。",
  "reviewer_id": "2",
  "project": "schema-dag-extraction",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 2，负责审查**新颖性与完整性**。\n\n## 论文信息\n- **标题**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n- **Venue**: EMNLP 2026 via ARR May 2026\n- **格式**: ACL 模板，long paper 8页正文限制 + 无限参考文献，Limitations 不计入页数\n- **匿名规则**: Double-blind\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_round_30/submitted.pdf`\n\n## 你的审查侧重\n\n重点审查以下方面：\n\n1. **贡献新颖性**：\n   - SCS/BCS 度量相对于 LLM-PEE 的技术新颖性\n   - \"首个控制研究\" 的 claim 是否成立\n   - 实证发现本身的价值（count degradation + confusability prediction）\n   - SDGD 失败是否构成有意义的贡献\n\n2. **Related Work 覆盖**：\n   - 是否遗漏重要相关工作（特别是 2025-2026 年的新工作）\n   - 与 LLM-PEE 的区分是否清晰充分\n   - label confusion / metric learning 方向的引用是否完整\n\n3. **写作质量与 Framing**：\n   - Abstract/Introduction 的 claim 是否与实验证据匹配\n   - 因果语言使用是否恰当（\"drives\" vs \"predicts\"）\n   - 论文叙事结构是否连贯（RQ→实验→发现 的逻辑链）\n   - 结论是否过度泛化（特别是 BCS 仅在 FewRel RE 上干净可证）\n   - Discussion 是否充分讨论了 \"为什么 embedding similarity 预测 LLM type confusion\"\n\n4. **完整性检查**：\n   - Limitations 是否涵盖关键局限\n   - NER null 的讨论是否平衡（power vs task structure）\n   - MAVEN centrality confound 的处理\n   - 是否有需要但缺失的实验\n\n5. **Missing References**：\n   - 搜索 2025-2026 年与 schema complexity、LLM IE、type confusion 相关的新工作\n   - 检查 label space reduction、decomposition 方向的引用\n\n请逐项给出详细评审意见，标注 [STRENGTH] 或 [WEAKNESS]，weakness 按严重程度分 [CRITICAL]、[MAJOR]、[MINOR]。",
    "reviewer_id": "2",
    "project": "schema-dag-extraction",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 3021 · 2026-05-22T07:28:51.247252+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1659
}
```

</details>

---


### Assistant

_source line 3022 · 2026-05-22T07:28:59.493140+00:00_

Round 1 已启动：

- ✅ **视觉审查 Agent** — 已派发（fire-and-forget）
- ✅ **Reviewer 1**（方法严谨性）— 已分配
- ✅ **Reviewer 2**（新颖性与完整性）— 已分配

等待两位 Reviewer 返回独立审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 248

## Round 248

2 recorded events


### User

_source line 3023 · 2026-05-22T07:34:48.755804+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见（新颖性与完整性）

**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?
**Venue**: EMNLP 2026 via ARR May 2026

---

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 实验设计扎实、统计分析细致，但核心发现的泛化性受限（BCS 仅在 FewRel RE 上干净可证），Discussion 过于单薄，且 embedding similarity 预测 LLM confusion 的机制解释缺失，削弱了论文作为分析性贡献的深度。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 统计方法严谨（TOST、partial correlation、ridge regression、bootstrap CI），但核心 claim 的可泛化性受限：BCS 独立预测力仅在 FewRel RE 上干净成立 |
| Excitement | 3/5 | 研究问题有价值（why does schema complexity hurt?），但发现偏 incremental——count degradation 并不新颖，confusability 的独立贡献局限于一个任务/数据集 |
| Reproducibility | 4/5 | 实验细节充分，承诺代码/数据开源，prompt 模板在 appendix 中完整给出 |
| Confidence | 4/5 | 仔细阅读全文及 19 页 appendix，熟悉 LLM IE 和实验设计文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [CRITICAL] BCS 独立预测力的泛化性不足，但 framing 暗示通用性

- 具体位置：Abstract ("BCS independently predicts RE type substitution errors")、Section 1 Contributions、Section 6
- 问题：论文的核心贡献——BCS 独立于 count 预测 accuracy——在四个数据集中只有 FewRel 一个是干净可证的：
  - **NER (Few-NERD)**: batch-level BCS-F1 相关为 null（r=0.004, p=0.94），三个模型均如此（Table 5）
  - **DocRED**: VIF=50.9，BCS 与 centrality 的 r=0.99，semipartial R²_BCS 仅 0.056（Section 4.3 footnote）
  - **MAVEN**: 正相关，控制 centrality 后消失（p>0.2，Appendix E）
  
  换言之，BCS 的独立预测力 (R²≈22%, VIF=1.18) 仅建立在 FewRel 80-relation RE 的 100 个随机 batch 上。Abstract 和 Introduction 的 framing 给读者留下了"BCS 在多任务上有效"的印象，但实际上论文自己的数据表明 BCS 在 NER、ED 上无效，在 document-level RE 上无法与 centrality 区分。

- 为什么影响接收：这是论文最核心的发现。如果仅限一个数据集，contribution 的 significance 大幅降低。论文诚实地讨论了这些限制（Limitations §2, §3），但 abstract/introduction/conclusion 的 framing 与实际证据之间存在 gap。

- 建议修改方向：(1) Abstract 和 Introduction 需要更显式地限定 "BCS independently predicts accuracy" 的范围为 "sentence-level RE on FewRel"；(2) 在 Contributions 部分将第一条的 scope 从 "RE" 收窄并明确说明其他任务/数据集上的状态；(3) Discussion 应专门讨论为什么 BCS 在 RE 上有效但在 NER/ED 上无效，这本身可以是一个有价值的发现。

---

**N2** [CRITICAL] Discussion 极度单薄，缺少对核心机制的分析

- 具体位置：Section 6 (Discussion and Conclusion)，仅约 12 行
- 问题：对于一篇以"理解 why"为核心定位的分析性论文（"we conduct controlled analysis to understand *why* extraction degrades"，Section 2 Related Work），Discussion 却几乎没有讨论 *why*：
  
  1. **为什么 embedding similarity 能预测 LLM type confusion？** MiniLM（一个 384-d 的 sentence encoder）的 type name embedding 的 cosine similarity 为什么能预测 Qwen3-32B（一个完全不同的 5120-d causal LM）做 IE 时的类型混淆？这是论文最需要解释但完全回避的核心问题。Appendix X (renaming experiment) 暗示 "SCS may proxy deeper conceptual overlap rather than surface similarity"，但没有展开。
  
  2. **NER null 的含义？** 论文用 power analysis (Appendix E.2) 解释 NER null 是 "absence of evidence"，但没有探讨另一个可能性：NER 的类型混淆机制可能与 RE 根本不同（NER 错误分散在 miss/boundary/type 三种模式，而 RE 几乎全部集中在 type substitution），这暗示 confusability 可能只影响 classification-dominant 的任务（RE）而不影响 span-detection-dominant 的任务（NER）。这是一个有实质意义的发现，值得在 Discussion 中展开。
  
  3. **为什么 decompose-then-merge 失败？** 论文准确诊断了问题（merge amplification + routing failure），但没有讨论这对 training-free IE pipeline 的设计意味着什么——是否存在其他架构（如 verify-then-merge、cascade）可以绕过？

- 为什么影响接收：一篇定位为"分析性"而非"工程性"的论文，如果 Discussion 比 Limitations 还短，reviewer 会质疑论文是否真正推进了对问题的理解，还是仅仅报告了一组相关性。

- 建议修改方向：Discussion 至少需要覆盖上述三个问题。特别是第一个问题——embedding similarity 为什么 work——可以从以下角度展开：(a) type name embedding 可能 capture 了 ontological proximity，而 LLM 在做 IE 时也依赖类似的 semantic space；(b) SCS 可能是 LLM 内部 type representation overlap 的一个粗糙 proxy；(c) 引用 label confusion matrix / prototypical network 文献来建立理论连接。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [MAJOR] Abstract 中 "drives" 的因果语言过强

- 具体位置：Abstract 第一句 "type count drives recall decline"
- 问题：论文建立的是 controlled correlational evidence（Section 6, Limitations §4 也承认 "mechanistic analysis at the attention or logit level is needed to confirm the causal pathway"）。"drives" 暗示 causation，而 "predicts" 更准确。正文中一般用 "predicts"，但 abstract 用了 "drives"。
- 建议：将 "drives" 改为 "predicts" 或 "is associated with"。

**W2** [MAJOR] "首个控制研究" 的 claim 需要更仔细的界定

- 具体位置：Abstract "the first controlled study isolating these factors"；Section 1 "To our knowledge, we present the first controlled study simultaneously isolating type count and inter-type confusability"
- 问题：这个 claim 需要更精确的 scope。论文在 Related Work 中承认 visual recognition 领域有 similar precedent（Dubey et al. 2018; Deng et al. 2010），label confusion matrices 也有研究。"First" claim 的 scope 应限定为 "in training-free LLM IE"（正文第 1 页第 15 行有这个限定语，但 abstract 中缺失）。另外，Golde et al. (2025) 的 training-evaluation similarity work 可能也在做类似的 controlled analysis，论文应更明确地区分。
- 建议：Abstract 中加上 "in training-free LLM IE" 的限定语；在 Related Work 中更具体地讨论与 Golde et al. (2025) 的区别。

**W3** [MAJOR] Ecological correlation 的局限性讨论不充分

- 具体位置：Section 4.3 (Practical magnitude)，"The amplification from pairwise r²≈1.5% to batch-level R²≈22% is not a statistical artifact but the operative mechanism"
- 问题：论文引用 Robinson (1950) 和 Baan et al. (2023) 来解释 ecological amplification，但措辞过于自信。Ecological correlation 确实不是 "artifact"，但它反映的是 batch-level 的群体效应，不能直接推断到 individual instance level。论文在 abstract 中加了 "(ecological level)" 的标注，这很好，但正文中 "not a statistical artifact but the operative mechanism" 的措辞暗示 22% 是对 confusability 独立贡献的准确估计，而实际上它是一个 ecological-level 估计。
- 建议：修改措辞，明确 R²=22% 是 batch-level ecological estimate，不能直接推断 instance-level effect size。

**W4** [MAJOR] 结论过度泛化——BCS 仅在 FewRel RE 上 "干净可证"

- 具体位置：Section 1 Contribution 1 ("independently predicts type substitution errors in RE on FewRel (VIF=1.18)")
- 问题：Contribution 1 的措辞是准确的（限定在 FewRel RE），但 Contribution 2 ("We document a task asymmetry") 将 NER null 归因于 "dispersed error modes and BCS range compression"——后者 (range compression) 是对 null 的一种解释，但不是已被证实的 causal explanation。BCS range compression 可能是 symptom 而非 cause：Few-NERD 的 type embedding 空间本身就更紧凑（BCS range 0.77-0.93 vs FewRel 0.42-0.97），这可能反映 NER type space 的结构性差异，而非仅仅是 "statistical power 不足"。
- 建议：Contribution 2 应更谨慎地措辞：NER null 可能反映 (a) insufficient power，(b) NER task structure，或 (c) NER type space 的本质不同，这三个解释目前无法区分。

**W5** [MINOR] Related Work 中 label confusion / metric learning 方向引用可更完整

- 具体位置：Section 2, "SCS novelty" paragraph
- 问题：论文引用了 Snell et al. (2017) (Prototypical Networks) 和 Yin et al. (2019) (zero-shot classification)，但遗漏了一些更直接相关的工作：
  - **Local Metric NER** (2024, Knowledge-Based Systems) 用 Mahalanobis distance 做 per-category NER，与 SCS 的 per-type similarity idea 有直接关联
  - **Feature-dependent confusion matrices for NER** (2019, EMNLP) 用 feature-dependent noise modeling 处理 label confusion，与本文的 confusability analysis 直接相关
  - PARSE (2025, EMNLP Industry) 已被引用（parse-2025），good
  - Reflect then Learn (2026) 已被引用（reflect-learn-2026），good
- 建议：补充 label confusion / metric learning for NER 方向的引用。

---

## 小问题（不影响接收）

- Section 3.2 (SCS definition)：SCS 的 name 说是 "Schema Confusability Score"，但实际上它是 pairwise type name embedding cosine similarity，与 "schema" 的复杂性关系不大——名字可能 misleading。BCS (Batch Confusability Score) 作为 schema-level metric 的名称更合理。
- Table 1：BCS Range 列的值跨 embedding model 不可比（Qwen3 vs MiniLM），但同一个表格中混合展示，容易误导读者直接比较不同数据集的 BCS range。建议加注或分开。
- Appendix G 中的 prompt template 展示非常完整，是 good practice。
- 论文格式合规：8 页正文 + references + Limitations（不计入页数），符合 EMNLP 2026 long paper 要求。
- Double-blind compliance：通篇未发现违规（作者信息、GitHub link 等均匿名）。

---

## 主要优势

- [STRENGTH] **实验设计方法论**：BCS-controlled batch design 是一个有价值的方法论贡献。通过固定 count 变 BCS 来隔离 confusability 的效应，这个设计在 training-free LLM IE 领域确实是新颖的（Section 3.3, Experiment 2）。
- [STRENGTH] **统计分析深度**：TOST 等价性检验、partial correlation（控制 centrality）、VIF 多重共线性检查、ridge regression、cluster-robust bootstrap——这种统计严谨性在 NLP 实证论文中不常见，值得肯定。
- [STRENGTH] **诚实的负面结果**：NER null 的完整讨论（含 power analysis）、SDGD 失败的详细剖析、MAVEN centrality confound 的识别——这些负面发现的坦诚处理比隐藏它们更有价值。
- [STRENGTH] **Cross-model replication**：在 3 个 open-weight model families（8B/32B/70B）+ Gemini Flash 上验证 count curves 和 BCS effects，增强了结果的可信度。
- [STRENGTH] **Appendix 的完整性**：19 页 appendix 几乎预见并回答了所有合理的质疑（variance decomposition、format independence、prompt sensitivity、split-origin contamination、domain distribution、range-matched robustness 等）。

---

## 总结

论文提出了一个有价值的研究问题（schema complexity 的两个维度如何分别影响 LLM IE），实验设计和统计分析都很扎实。但核心发现（BCS 独立预测 accuracy）的泛化性受限于 FewRel RE 这一个 setting，而论文的 framing 与实际证据之间存在 gap。Discussion 部分过于单薄，未能为 "why embedding similarity predicts LLM confusion" 提供机制性解释，这对一篇以"理解 why"为定位的分析性论文而言是重大缺陷。建议 (1) 收窄 abstract/intro 的 claim scope，(2) 大幅扩充 Discussion，(3) 更谨慎地处理因果语言和泛化陈述。如果这些问题得到解决，论文可以达到 Conference 水准。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 3024 · 2026-05-22T07:35:04.984217+00:00_

Reviewer 2 审稿意见已收到（3.5 分，Borderline Conference）。核心问题：BCS 泛化性受限 + Discussion 过于单薄。等待 Reviewer 1 的意见后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 249

## Round 249

2 recorded events


### User

_source line 3025 · 2026-05-22T07:35:08.548811+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**总结**：评分 Overall 3.5 (Borderline Conference)。论文的实验设计和统计分析水准很高（BCS-controlled batch design、TOST 等价性检验、cross-model replication），但有两个 critical 问题：(1) BCS 独立预测力仅在 FewRel RE 上干净可证，而 abstract/intro 的 framing 暗示更广泛的泛化性；(2) Discussion 极度单薄（仅 12 行），对于一篇以"理解 why"为核心定位的分析性论文，缺少 embedding similarity 为何能预测 LLM type confusion 的机制解释。如果收窄 claim scope 并大幅扩充 Discussion，可达 Conference 水准。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 3026 · 2026-05-22T07:35:17.200807+00:00_

Reviewer 2 审稿已收到，评分 3.5（Borderline Conference）。2 个 CRITICAL + 4 个 MAJOR。等待 Reviewer 1 完成初审后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 250

## Round 250

2 recorded events


### User

_source line 3027 · 2026-05-22T07:36:55.575519+00:00_

[Reviewer 1 审稿意见]:
## 总体评分
**Overall**: 3.5 / 5 — Borderline Conference
**一句话总结**: 方法论扎实、统计处理细致的实证研究，但核心 claim 的覆盖范围在多处超出了证据支撑——NER 批次级 BCS 信号为 null、DocRED 多重共线性严重、Gemini 跨模型验证脆弱——需要收窄论断或补充证据。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 双实验范式设计合理，统计检验丰富（TOST、cluster-robust bootstrap、partial correlation），但 DocRED VIF=50.9 下的偏相关不可信，NER 批次级 null 与标题声称的"IE"泛化性矛盾，BCS-controlled 极端 batch 仅各 1 个 |
| Excitement | 3/5 | 对 schema 复杂度如何影响 LLM IE 的量化分析有实用价值，BCS 指标新颖，但核心发现（类型多→性能降、类型相似→混淆多）在直觉上可预期，schema decomposition 负面结果限制了实践影响力 |
| Reproducibility | 4/5 | Greedy decoding 确保推理确定性，附录 17 页提供了详尽的 robustness check（seed variance、cluster bootstrap、within-pool analysis 等），承诺代码数据公开 |
| Reviewer Confidence | 4/5 | 完整阅读了 27 页全文含所有附录，统计方法论在我的专业范围内 |

---

## Must-Fix 问题（影响接收决定）

**N1** [CRITICAL] 标题与 NER 批次级 null 之间的 claim-evidence gap
- 具体位置：Title、Abstract（第1页）、§9.1（第8-9页）、Table 5（Appendix E.1, p13）
- 问题：标题 "Training-Free LLM Information Extraction" 暗示结论适用于所有 IE 任务。但 BCS（batch-level confusability）信号在 NER 上跨所有模型和数据集均为 null（Table 5：Few-NERD r=0.004, p=0.91; Qwen3-32B, LLaMA-8B, LLaMA-70B 均 null）。论文的核心贡献之一——confusability 独立预测 IE 性能——实际上仅在 RE 任务的 batch level 成立。Type-pair level 的 SCS-confusion correlation（§4.2, Table 2）虽然跨任务显著，但效应量极小（Pearson r=1.3-1.7%，Spearman ρ=0.114-0.227）。
- 为什么影响接收：Claim scope 超出 evidence scope 是 soundness 问题。如果一篇论文声称研究"IE"但核心发现仅在 RE 的一个分析层面成立，reviewer 有理由质疑其 generality。
- 建议修改方向：(1) 标题改为更精确的表述，如 "...in Relation Extraction" 或明确标注 "with task-dependent confusability effects"；(2) Abstract 和 Introduction 中更前置地说明 NER 批次级 null 及其 power limitation；(3) 将当前 §9.1 的讨论从 Limitations 提升到 Results 或 Discussion 的显著位置。

**N2** [CRITICAL] DocRED VIF=50.9 下偏相关结论不可靠
- 具体位置：Table 12（Appendix E.1, p16）、§4.5（p7-8）
- 问题：论文在 §4.5 声称 "BCS effect survives nearly intact after partialling"（partialled r = −0.537 vs. raw r_BCS = −0.570），用以论证 confusability 独立于 degree centrality。但 DocRED 的 VIF=50.9（Table 12），远超传统阈值 10，表明 BCS 和 centrality 近乎完全共线（论文自己也承认 r=0.99, p16）。在此共线性水平下，偏相关系数的标准误被极度放大，点估计不稳定——微小的数据扰动可导致偏相关符号翻转。论文虽然承认 "impossible to fully separate the two predictors"，但仍将 DocRED 纳入跨数据集叙事中，给读者留下 "控制 centrality 后 BCS 仍显著" 的印象。
- 为什么影响接收：这是一个 interpretability 问题。将统计不可信的结果与其他数据集并列呈现，会误导读者对 confusability 独立性的判断。
- 建议修改方向：(1) 在正文 §4.5 中明确标注 DocRED 偏相关因 VIF>50 而不可解释，不应作为 BCS 独立性的证据；(2) 将 cross-dataset 的 centrality-控制叙事限定在 FewRel（VIF 合理）和 MAVEN（VIF 可接受）上；(3) 对 DocRED 改为讨论 "BCS 和 centrality 在该数据集上不可分离" 的结论。

**N3** [CRITICAL] BCS-Controlled 极端 batch 各仅 1 个，高杠杆风险
- 具体位置：§3.3（p4）、Figure 1b（p5）、§4.3（p6）
- 问题：BCS-controlled 实验的核心比较依赖每个 count level 仅 1 个 low-BCS batch 和 1 个 high-BCS batch（加 25 个 random，共 27 个）。Figure 1b 的 extreme-batch accuracy gap 是整篇论文最醒目的可视化结果之一，但它本质上是 N=1 vs N=1 的比较。虽然 25 个 random batch 提供了中间分布、OLS 回归（R²=0.218）使用了全部 27 个 batch，但极端 batch 的 regression leverage 极高。如果 low-BCS batch 恰好包含了对模型特别"容易"的类型（与 confusability 无关的原因，如预训练频率、example prototypicality），整个 BCS 效应的估计会被扭曲。Appendix E.4 的 domain 分析部分缓解了这一担忧（低 BCS batch 偏 geography/creative work，高 BCS batch 偏 science/event），但 domain skew 本身就是一个 confound。
- 为什么影响接收：单极端 batch 设计使核心 BCS 效应的 internal validity 依赖于该特定 batch 的代表性，这是实验设计的结构性弱点。
- 建议修改方向：(1) 在多个 count level 上构造多组极端 batch（如对 FewRel 80 关系，count=8 时理论上可构造多个 near-extreme batch）；(2) 报告 leave-one-out 回归，展示去掉极端 batch 后 R² 和 slope 的变化；(3) 如果无法增加极端 batch 数量，至少在正文中明确标注 "extreme-batch comparison is illustrative (N=1 per condition); the quantitative BCS-accuracy relationship is estimated from the full 27-batch regression"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [MAJOR] Gemini 2.5 Flash leverage sensitivity 严重削弱跨模型泛化
- 具体位置：§7（p7）、Table 5（p13）、Table 25（p25）
- 问题：Gemini 2.5 Flash 是唯一的 proprietary model 验证点。但 FewRel RE 上 leave-one-out Pearson r 从 −0.80 骤降至 −0.42（§7），说明某单个 count level 贡献了绝大部分相关性。Table 5 中 Gemini 的 NER BCS-F1 标注为 "Not tested"。Table 25 显示 Gemini count=8 时仅 8 个 batch（远少于其他模型的 27 个）。这意味着论文对 proprietary model generalization 的证据极其脆弱。
- 建议：(1) 在 cross-model validation 叙事中将 Gemini 降级为 "preliminary/partial evidence"；(2) 报告完整的 leave-one-out 分析（哪个 count level 是 leverage point、去掉后 CI 如何变化）；(3) 坦承 proprietary model 验证目前证据不足。

**W2** [MAJOR] R²=0.218 的生态相关性 vs 个体预测力的 gap 未充分讨论
- 具体位置：§4.3（p6）、§9.2（p9）、Appendix N（p22）
- 问题：论文标题问 "How Does Schema Complexity Predict Performance?"——暗示预测能力。Batch-level R²=0.218 经 Appendix N 的 Monte Carlo 模拟，effective EF≈3.35，推算 individual-level R²≈0.065。这意味着对于实践者关心的个体类型或实例预测，BCS 仅解释约 6.5% 的方差。§9.2 承认了这一点但讨论不够显著——读者容易带着 "BCS 解释 22% 方差" 的印象离开，而实际个体预测力远低于此。
- 建议：(1) 在 §4.3 首次报告 R²=0.218 时立即注明这是 ecological-level estimate；(2) 将 Appendix N 的 individual-level 估计纳入正文讨论；(3) 在 Conclusion 中明确指出 BCS 作为 schema 设计的定性指导（区分"高混淆"vs"低混淆" schema）比作为定量预测器更可靠。

**W3** [MAJOR] TOST 等价性检验的 margin 设定缺乏外部锚定
- 具体位置：Appendix C（p14-15）、Table 10（p15）
- 问题：TOST 的 ±3pp margin 基于 within-cell SD（2.3pp）和 Cohen's d=0.5 推导。但 Cohen's d=0.5 是"中等效应"的通用阈值，并非 IE 领域的 meaningful difference 标准。对于一个 baseline accuracy 在 80-90% 的任务（如 Few-NERD NER），3pp 可能是 practically significant 的（例如将 F1 从 85% 降到 82%）。Table 10 显示在 ±2pp 时等价性结论不变，但在 ±1pp 时结论翻转为 "inconclusive"——这说明结论对 margin 选择敏感。论文未提供 IE 领域中什么程度的性能差异被视为 "practically equivalent" 的外部参考。
- 建议：(1) 引用 IE 领域的 effect size 基准（如 SoTA 模型间的典型差异幅度）来锚定 margin；(2) 至少在附录中讨论为什么 3pp 而非 1pp 或 5pp 是合理的 practical equivalence boundary。

**W4** [MAJOR] FewRel 数据污染风险的处理不完整
- 具体位置：§9.4（p9）、Appendix Q（p23）
- 问题：FewRel 基于 Wikipedia/Wikidata 构建，而 Qwen3-32B 的预训练数据极大概率包含这些来源。论文在 Appendix Q 中通过 split-origin covariate 分析证明 BCS-accuracy 关系不受 train/val split 差异的影响，但这只能控制 "是否在 FewRel 训练集中出现"，无法控制 "是否在 LLM 预训练语料中出现" 这一更根本的污染。论文未进行任何直接的 memorization detection（如 canary insertion、membership inference 等），也未在 §3.1 中讨论为什么 FewRel 相比其他数据集更容易受到 contamination 影响。
- 建议：(1) 加入一个简单的 contamination probe（如测试模型能否在无 context 情况下正确预测 FewRel 的 relation label）；(2) 在 §3.1 或 Limitations 中明确指出 FewRel 的 contamination risk，并说明为什么 BCS 效应不太可能完全由 memorization 驱动（例如：如果模型记住了所有 FewRel 实例，accuracy 应该不随 schema 变化）。

**W5** [MODERATE] Within-pool analysis（§4.3）的 type composition confound
- 具体位置：§4.3（p6）、Appendix D（p15）、Appendix L（p21）
- 问题：Within-pool analysis 从 80-relation pool 中抽取 100 个 16-relation 子集来获取更多 BCS 变异。但 Appendix L（p21）显示 within-pool slope（−0.509, p=0.60）不显著，smaller gap（−3.92pp vs −5.31pp from full pool）。论文将此归因于 "narrow BCS range" 限制了 effect size。但另一种解释是：从同一 pool 抽取的子集在 type composition 上高度相关（共享大量类型），使得 BCS 变异实际上反映的是 "哪些特定类型被包含/排除" 而非 confusability 本身。
- 建议：在 Appendix L 中增加 permutation test 或 type-overlap adjusted regression 来排除 type identity confound。

---

## 小问题（不影响接收）

- §3.5（p5）：v1→v2 prompt 修改同时改变了 format constraints 和 natural language framing，无法完全隔离哪项改变导致了 attenuation。建议在 Appendix H 中补充讨论。
- Table 1（p4）：DocRED 的 "†Trigger mentions across 8,042 sentences" 注释容易误读为 ED 任务的统计量，但 DocRED 是 RE 数据集。请确认这是否是排版错误。
- Figure 2（p7）：Error taxonomy 的 BCS bin 划分（Low/Med-low/Med-high/High）未给出具体 BCS 阈值，读者无法验证 bin 边界的合理性。
- §3.2（p3-4）：SCS 定义使用 cosine embedding similarity，但未讨论 embedding 模型选择的敏感性。Table 1 列出了 embedding model（MiniLM/Qwen3），但正文未分析换用不同 embedding 后 SCS 排序是否稳定。Appendix I 的 aggregation sensitivity 不等同于 embedding sensitivity。
- Limitations Item 3（p9）："Task scope" 仅提及 NER/RE/ED，未讨论 schema complexity 对其他结构化预测任务（如 event argument extraction、slot filling）的 transferability。

---

## 主要优势

1. **[STRENGTH] 双实验范式互补性强**：Count Curves 提供 macro-level 趋势，BCS-Controlled 隔离 confusability 效应。两者结合使 "count 和 confusability 是独立维度" 的 claim 比单一范式更有说服力。§4.4 的 TOST 和 factorial analysis 进一步验证了 separability。

2. **[STRENGTH] 统计处理在 NLP 经验论文中属上乘**：Cluster-robust bootstrap CI（Appendix E.3）正确处理了 shared-instance dependence；partial correlation 控制了 frequency 和 centrality confounders（Table 12，FewRel VIF 合理）；TOST 等价性检验避免了 "absence of evidence ≠ evidence of absence" 的常见谬误；seed variance decomposition（Appendix R）量化了量化非确定性。这些做法远超大多数 NLP 实证论文的统计标准。

3. **[STRENGTH] 诚实的 null reporting**：NER 批次级 BCS null（Table 5）、Gemini leverage sensitivity（§7）、schema decomposition failure（§5）均被直接报告而非隐藏。这增强了论文的可信度。

4. **[STRENGTH] 跨模型复制覆盖面广**：Count curves 在 4 个模型（Qwen3-32B, LLaMA-8B, LLaMA-70B, Gemini Flash）上复制，BCS-controlled 在 3 个开放权重模型上复制（Table 3-5, 23-25）。RE direction consistency 在所有模型上确认。

5. **[STRENGTH] 附录质量高**：17 页附录覆盖了 robustness check 的几乎所有可预见质疑（seed variance、format independence、BCS aggregation、split-origin covariate、label renaming、relaxed matching）。这为论文的 reproducibility 和 defensibility 提供了坚实基础。

6. **[STRENGTH] Schema decomposition 的负面结果有实践价值**：§5 和 Appendix B 系统地展示了 SDGD 的四种 failure mode（merge amplification、routing failure），节省了后续研究者探索这一方向的时间。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 3028 · 2026-05-22T07:37:21.307512+00:00_

Reviewer 1 审稿意见已收到。两位 Reviewer 都已完成独立初审，现在进入交叉分享阶段（Step 2）。

两位 Reviewer 评分一致（均 3.5 Borderline Conference），且关注点有显著重叠。现在将各自的完整意见转发给对方，要求逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 251

## Round 251

14 recorded events


### User

_source line 3029 · 2026-05-22T07:37:40.407418+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审稿摘要**：Overall 3.5（Borderline Conference）。

三个 CRITICAL 问题：
1. **NER 批次级 BCS 信号为 null**，但标题声称覆盖"IE"——claim scope 超出 evidence
2. **DocRED VIF=50.9** 使偏相关控制 centrality 的结论不可解释
3. **BCS-controlled 极端 batch 各仅 1 个**，Figure 1b 的核心对比本质上是 N=1 vs N=1

四个 MAJOR 问题：Gemini leverage sensitivity（r: −0.80→−0.42）、R²=0.218 的生态谬误风险、TOST margin 缺乏领域锚定、FewRel 数据污染未做 memorization detection。

主要优势：双实验范式设计精巧、统计处理在 NLP 实证论文中属上乘（cluster-robust bootstrap、TOST、seed variance decomposition）、null reporting 诚实、17 页附录质量高。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 3030 · 2026-05-22T07:37:57.108585+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3031 · 2026-05-22T07:37:57.511675+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 3032 · 2026-05-22T07:37:57.864049+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,get_external_review_status,get_visual_check_status",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,get_external_review_status,get_visual_check_status",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 3033 · 2026-05-22T07:37:57.965188+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 3034 · 2026-05-22T07:38:02.236703+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 3035 · 2026-05-22T07:38:02.287423+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3036 · 2026-05-22T07:38:15.849993+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 3037 · 2026-05-22T07:38:16.201605+00:00_

{"result":"# 项目 schema-dag-extraction 概况\n\n## 实验状态 (69 个)\n\n- **exp012_llama_8b_r2_exp2**: DONE (negative) — \n- **exp012_llama_8b_r2**: DONE (success) — \n- **exp006_interaction_2x2**: DONE (negative) — \n- **exp012_llama_awq**: DONE (killed) — \n- **exp012_llama_8b_r3**: DONE (failed) — \n- **exp012_llama_8b**: DONE (killed) — \n- **exp_fewrel_40rel_r3**: DONE (failed) — \n- **exp_fewrel_40rel_r2**: DONE (failed) — \n- **exp012_llama_fewnerd_r4**: DONE (failed) — \n- **exp012_llama_8b_fewnerd**: DONE (failed) — \n- **exp_fewrel_40rel**: DONE (failed) — \n- **exp012_llama_fewnerd_r3**: DONE (failed) — \n- **exp012_llama_fewnerd_r2**: DONE (failed) — \n- **exp012_llama_fewnerd**: DONE (failed) — \n- **exp008_sdgd_zero_fewnerd**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- prompt_sensitivity（准备中）\n- prompt_sensitivity_dry4（准备中）\n- prompt_sensitivity_dry3（准备中）\n- prompt_sensitivity_dry2（准备中）\n- prompt_sensitivity_dry（准备中）\n- exp_aggregation_monte_carlo（准备中）\n- exp_scs_name_def_ablation（准备中）\n- exp_fewrel_contamination_check（准备中）\n- exp017_gpt4o_mini_fewrel（准备中）\n- exp_cross_embedding_sensitivity（准备中）\n- …另有 2 项\n\n## 近期结论\n- **exp_llama70b_ner_bcs_null** (success): Batch-level BCS does not correlate with NER F1 for LLaMA-3.1-70B-FP8, consistent with the BCS null observed in Qwen3-32B (r=0.004) and LLaMA-8B (r=-0.12). The confusability metric is not predictive of extraction quality at the batch level. ← 基于 exp012_llama_8b_r2_exp2\n  [LLaMA-70B NER BCS-null analysis](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_llama70b_ner_bcs_null/data/bcs_null_analysis.json)\n- **exp_gemini_flash_bcs_controlled** (success): BCS-accuracy negative correlation observed on open-weight models (Qwen3-32B, LLaMA) generalizes to proprietary API models. Gemini 2.5 Flash should show significant BCS gap on extreme-BCS batches at count 8 and count 16, confirming Dimension 2 is architecture-family-in
…[truncated 1221 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 3038 · 2026-05-22T07:38:16.202240+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 3039 · 2026-05-22T07:38:16.252766+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3040 · 2026-05-22T07:38:16.253224+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 3041 · 2026-05-22T07:38:16.404128+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T07:28:24.100979+00:00\", \"completed_at\": \"2026-05-22T07:32:44.679549+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-3\", \"message\": \"连续 3 页纯文本无任何 display item。审稿人前 2 分钟内看不到任何视觉锚点，缺少概念总览图/架构图帮助快速建立认知。对于实证分析型论文，建议在页 1-2 加入一个概念框架图或核心结果预览图\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-8\", \"message\": \"主文仅 2 个 figure + 2 个 table（共 4 个 display items），对于实证驱动的论文偏少（典型范围 5-8 个/8-9 页）。大量统计结论仅通过文字传达，视觉传达力不足\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 1 质量良好：双面板布局清晰，blue/orange 配色色盲友好，error bars 标注完整，caption 自包含。轴标签和 legend 字号可读\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2 双面板线图（Error taxonomy decomposition），多色线条（blue/orange/green/red）可区分。轴标签字号偏小，接近正文字号 70% 下限，建议适当放大\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Table 1 使用 booktabs 风格（toprule/midrule/bottomrule），格式规范\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 2 格式规范，booktabs 风格，相关性系数清晰\"}, {\"severity\": \"warning\", \"dimension\": \"page 8-9\", \"message\": \"Discussion + Conclusion + Limitations 连续 2 页纯文本。可考虑加入一个总结性 figure（如核心发现概览图）帮助审稿人回顾\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 1(b) 柱状图使用 blue/orange 配色区分 Low BCS vs High BCS，标注了具体数值和箭头标记差异幅度，信息传达有效\"}, {\"severity\": \"info\", \"dimension\": \"page 10-12\", \"message\": \"参考文献 3 页，格式统一，未见 [?] 未解析引用，编号连续\"}, {\"severity\": \"info\", \"dimension\": \"page 13-27\", \"message\": \"附录含约 28 个表格（Table 3-31），内容详实但仅有 2 个 figure（全在主文）。附录表格普遍使用 booktabs 风格，精度一致\"}, {\"severity\": \"info\", \"dimension\": \"page 18\", \"message\": \"Prompt template 展示使用代码块格式（JSON schema），排版清晰可读\"}, {\"severity\": \"info\", \"dimension\": \"page 27\", \"message\": \"末页内容约占 55%，底部空白约 40%，作为附录末页可接受\"}, {\"severity\": \"info\", \"dimension\": \"page 1-8\", \"message\": \"未发现 margin 溢出、公式渲染错误、section heading
…[truncated 234 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 150
}
```

</details>

---


### Assistant

_source line 3042 · 2026-05-22T07:38:35.682870+00:00_

**Reviewer 1 初审已收到，记录如下关键发现：**

| 级别 | # | 问题 |
|------|---|------|
| CRITICAL | C1 | NER BCS null → 标题 "IE" scope overclaim |
| CRITICAL | C2 | DocRED VIF=50.9 → 偏相关不可解释 |
| CRITICAL | C3 | Figure 1b 核心对比 N=1 vs N=1 |
| MAJOR | M1 | Gemini leverage sensitivity (r: −0.80→−0.42) |
| MAJOR | M2 | R²=0.218 生态谬误风险 |
| MAJOR | M3 | TOST margin 无领域锚定 |
| MAJOR | M4 | FewRel 数据污染无 memorization detection |

**当前状态：**
- Reviewer 1：✅ 已完成（3.5 Borderline Conference）
- Reviewer 2：⏳ 等待中
- 外部审稿：未请求
- 视觉审查：✅ 已完成（3 warnings, 0 critical）

等 Reviewer 2 初审结果到达后，立即启动交叉分享（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 252

## Round 252

44 recorded events


### User

_source line 3043 · 2026-05-22T22:49:49.293709+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: schema-dag-extraction
- 论文路径: projects/schema-dag-extraction/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2026
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 3044 · 2026-05-22T22:49:55.295719+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3045 · 2026-05-22T22:49:55.346656+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3046 · 2026-05-22T22:50:01.400105+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,read_project_file,request_external_review,submit_review_report_to_research_director,update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,read_project_file,request_external_review,submit_review_report_to_research_director,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 3047 · 2026-05-22T22:50:01.400584+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 3048 · 2026-05-22T22:50:04.764863+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 3049 · 2026-05-22T22:50:04.815540+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3050 · 2026-05-22T22:50:07.175317+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 3051 · 2026-05-22T22:50:07.276134+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 3052 · 2026-05-22T22:50:11.800734+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 3053 · 2026-05-22T22:50:13.159095+00:00_

{"result":"# 项目 schema-dag-extraction 概况\n\n## 实验状态 (69 个)\n\n- **exp012_llama_8b_r2_exp2**: DONE (negative) — \n- **exp012_llama_8b_r2**: DONE (success) — \n- **exp006_interaction_2x2**: DONE (negative) — \n- **exp012_llama_awq**: DONE (killed) — \n- **exp012_llama_8b_r3**: DONE (failed) — \n- **exp012_llama_8b**: DONE (killed) — \n- **exp_fewrel_40rel_r3**: DONE (failed) — \n- **exp_fewrel_40rel_r2**: DONE (failed) — \n- **exp012_llama_fewnerd_r4**: DONE (failed) — \n- **exp012_llama_8b_fewnerd**: DONE (failed) — \n- **exp_fewrel_40rel**: DONE (failed) — \n- **exp012_llama_fewnerd_r3**: DONE (failed) — \n- **exp012_llama_fewnerd_r2**: DONE (failed) — \n- **exp012_llama_fewnerd**: DONE (failed) — \n- **exp008_sdgd_zero_fewnerd**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 当前阶段\n**v34+ submission-ready** — R26 审稿修复完成，ARR 预检通过，DDL 2026-05-25（剩 3 天）。\n\n## 运行中\n（无）\n\n## R26 修复完成（2026-05-22）\n\n### 论文修改（8 项）\n- W5: \"drives\" → \"predicts\"（confusability 语境，abstract.tex）\n- W1: Abstract BCS scope 限定（R²≈0.22, VIF=1.18, NER null）+ Intro contribution VIF 限定\n- W2: DocRED caveat 加强（VIF=50.9, 7-fold SE inflation, ridge 方向确认）\n- W3: SCS/BCS vs LLM-PEE 技术差异（related_work.tex，BCS=MEAN）\n- W4: TOST \"independently addressable\" → \"approximately additive on probability scale\" + logit inconclusive\n- M1: \"first controlled study\" 完整限定语\n- M2: NER null 平衡解释（error-mode structure）\n- M5: 多重比较 Bonferroni robustness 声明\n- M4: SDGD §5 移入 Appendix（省 ~0.7 页）\n- M6: 添加 NER Retriever + Reflect then Learn 引用\n\n### 补充分析（3 项，0 GPU）\n- DocRED Ridge Regression: β_BCS=−1.53（所有 λ≥0 为负），R²=0.594 → Appendix E.1\n- Split-Sample Bootstrap CI: cluster-robust SE=0.96–0.97× OLS，CI robust → Appendix E.3\n- FewRel Domain Distribution: χ²=230.74 (p<0.001)，mediator 非 confound → Appendix E.4\n\n### 写作打磨\n- Prose tightening: results.tex 5 处 + discussion.tex 2 处\n- Appendix 表格格式一致性: 29 表 caption 位置 + 3 列对齐 + 1 数字格式\n- Camera-ready polish: 13 处 prose 优化\
…[truncated 906 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1358
}
```

</details>

---


### Tool call

_source line 3054 · 2026-05-22T22:50:13.661441+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 3055 · 2026-05-22T22:50:14.565962+00:00_

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
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	\usepackage{listings}
16	
17	\title{How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	
28	\input{related_work}
29	
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	
40	Our findings are subject to three main limitations.
41	\textbf{(1)~Model and statistical scope.}
42	Primary experiments use Qwen3-32B; cross-model validation (LLaMA-8B/70B, Gemini Flash) covers Dimensions~1--2 but not secondary analyses such as TOST factorial interaction (\S\ref{sec:multi_channel}) or SDGD failure analysis (\S\ref{sec:sdgd}), and proprietary-model generalization remains open.
43	TOST dimensional separability holds on the probability scale but logit-scale evidence is inconclusive, reflecting the inflated variance of logit-transformed proportions in the 0.37--0.86 accuracy range rather than a qualitative divergence from the linear-scale finding; the interaction point estimate (0.47\,pp) falls within the $\pm 3$\,pp equivalence margin.
44	BCS-controlled experiments use greedy decoding with a single seed; residual SD${}\,=\,0.88$\,pp is 18--44\% of the observed effect size (Appendix~\ref{app:variance-decomposition}), so detection is robust but point estimates carry meaningful uncertainty.
45	All evidence is correlational with controlled stratification; mechanistic confirmation at the attention or logit level remains future work.
46	%
47	\textbf{(2)~DocRED VIF confounding.}
48	DocRED exhibits severe multicollinearity (VI
…[truncated 2016 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 3056 · 2026-05-22T22:50:15.119188+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions",
  "allowed_domains": "['aclweb.org', 'aclrollingreview.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions",
    "allowed_domains": "['aclweb.org', 'aclrollingreview.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool call

_source line 3057 · 2026-05-22T22:50:15.721968+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_round_31/submitted.pdf",
  "pages": "1-2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_round_31/submitted.pdf",
    "pages": "1-2"
  }
}
```

</details>

---


### Tool result

_source line 3058 · 2026-05-22T22:50:15.923214+00:00_

PDF pages extracted: 2 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_round_31/submitted.pdf (466.2KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool result

_source line 3059 · 2026-05-22T22:50:22.676092+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

I found comprehensive information about ACL Rolling Review (ARR) 2026 submission guidelines. Here's what you need to know:

## Key Submission Requirements

**Originality and Content:**
All submitted papers are expected to describe original, completed and unpublished work. There is a limit on re-use of text from other publications (no more than 10% total tokens). ARR discourages thinly sliced contributio
…[truncated 1281 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 7556
}
```

</details>

---


### Tool call

_source line 3060 · 2026-05-22T22:50:36.782105+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline ARR commitment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline ARR commitment"
  }
}
```

</details>

---


### Tool call

_source line 3061 · 2026-05-22T22:50:36.782529+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARR May 2026 submission deadline dates",
  "allowed_domains": "['aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ARR May 2026 submission deadline dates",
    "allowed_domains": "['aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 3062 · 2026-05-22T22:50:36.782776+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_round_31/submitted.pdf",
  "pages": "3-9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_round_31/submitted.pdf",
    "pages": "3-9"
  }
}
```

</details>

---


### Tool result

_source line 3063 · 2026-05-22T22:50:37.284772+00:00_

PDF pages extracted: 7 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_round_31/submitted.pdf (466.2KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool result

_source line 3064 · 2026-05-22T22:50:41.008942+00:00_

Web search results for query: "ARR May 2026 submission deadline dates"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026","url":"http://aclrollingreview.org/incentives2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review","url":"http://aclrollingreview.org/reviewing"},{"title":"Dates","url":"http://aclrollingreview.org/some-important-dates/"},{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Submission dates and process for 2024 Conferences","url":"http://aclrollingreview.org/submission-dates-for-2024/"},{"title":"ARR Dashboard","url":"http://stats.aclrollingreview.org/"}]

Based on the search results, I found information about ARR submission deadlines. ARR switched from 8-week to 10-week review cycles starting in May 2025, which affects the May 2026 cycle.

Unfortunately, the search results don't contain the specific detailed dates for the May 2026 ARR submission deadline cycle. However, the submission deadline is always the 15th of the month, though other dates vary due to the length of months and timing of weekends. This means the May 2026 submission deadline would be May 15, 2026.

For the most current and complete timeline including all review and meta-review deadlines for the May 2026 cycle, I recommend checking the official ARR Dates and Venues page at aclrollingreview.org/dates, which maintains the authoritative schedule for all upcoming cycles.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 4226
}
```

</details>

---


### Tool result

_source line 3065 · 2026-05-22T22:50:41.963157+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline ARR commitment"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"}]

Based on the search results, here's the key information about EMNLP 2026 call for papers submission deadline and ARR commitment:

## Submissio
…[truncated 857 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 5181
}
```

</details>

---


### Tool call

_source line 3066 · 2026-05-22T22:50:58.239325+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission format page limit style guidelines long short paper",
  "allowed_domains": "['2026.emnlp.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission format page limit style guidelines long short paper",
    "allowed_domains": "['2026.emnlp.org']"
  }
}
```

</details>

---


### Tool call

_source line 3067 · 2026-05-22T22:50:58.691412+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 3068 · 2026-05-22T22:50:58.741962+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 3069 · 2026-05-22T22:51:04.966531+00:00_

Web search results for query: "EMNLP 2026 submission format page limit style guidelines long short paper"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"EMNLP 2026 Paper Integrity Policy - EMNLP 2026","url":"https://2026.emnlp.org/paper-integrity-policy/"},{"title":"EMNLP 2026 AI Reviewing Experiment - EMNLP 2026","url":"https://2026.emnlp.org/ai-reviewing-experiment/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"}]

Based on the search results, I found information about EMNLP 2026 submission guidelines. Here's what I found:

## EMNLP 2026 Submission Format and Guidelines

**Main Conference:**
EMNLP 2026 will use ACL Rolling Review (ARR) as a reviewing system, but final decisions will be made by the conference. Both submissions of articles for review and commitment of reviewed articles to the conference will be performed via the Open Review platform.

**Industry Track:**
Industry track papers have a maximum of 6 pages in length, and manuscripts should be submitted electronically in PDF format and formatted using templates available for the conference, and these style files should not be modified.

Submissions that do not conform to the required styles, including paper size, margin width, and font size restrictions, will be desk-rejected.

Indu
…[truncated 852 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 6727
}
```

</details>

---


### Tool call

_source line 3070 · 2026-05-22T22:51:11.040686+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 long paper 8 pages short paper 4 pages format requirements template",
  "allowed_domains": "['aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 long paper 8 pages short paper 4 pages format requirements template",
    "allowed_domains": "['aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 3071 · 2026-05-22T22:51:12.948608+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 3072 · 2026-05-22T22:51:13.100926+00:00_

# Review Issues Tracker
# Updated: 2026-05-22 (ALL R29 fixes complete)

# ============================================================
# R29 CRITICAL (2 items)
# ============================================================

- id: R29-C1
  summary: "BCS 度量的干净证据仅限 FewRel RE 一个数据集，论文叙事暗示更广泛适用性"
  category: framing
  severity: critical
  status: in_progress
  first_raised_round: 23
  last_seen_round: 29
  mentions:
    - {round: 23, reviewers: [R1, R2], note: "R23-C2: weaken wording"}
    - {round: 24, reviewers: [R1, R2], note: "R24-C1: recenter on FewRel"}
    - {round: 25, reviewers: [R1, R2], note: "R25-C2: confusability scope overclaim"}
    - {round: 29, reviewers: [R1, R2], note: "R1-W1 + R2-W2 AGREE. Abstract 'drives' overgeneralizes."}
  action_items:
    - {round: 25, action: "Weaken title/abstract/conclusion generality claims", assigned_to: "Agent", status: done}
    - {round: 29, action: "Abstract rewritten: 'predicts' not 'drives', explicit FewRel RE scope (R²≈0.22, VIF=1.18), NER null stated. Intro contribution limited to FewRel.", assigned_to: "Agent", status: done}
  resolution: "Abstract + Intro rewritten with explicit FewRel-only BCS scope. 'drives'→'predicts' throughout."
  resolution_round: null

- id: R29-C2
  summary: "DocRED VIF=50.9 的 partial correlation 不可信但仍作为支持证据呈现"
  category: method
  severity: critical
  status: in_progress
  first_raised_round: 23
  last_seen_round: 29
  mentions:
    - {round: 23, reviewers: [R1, R2], note: "R23-C2: VIF=50.9"}
    - {round: 25, reviewers: [R1, R2], note: "R25-C1: must report semipartial R²"}
    - {round: 29, reviewers: [R1, R2], note: "R1-W2, R2 AGREE. §4.3 still presents DocRED R² misleadingly."}
  action_items:
    - {round: 25, action: "Report semipartial ΔR²_BCS=5.6%", assigned_to: "Agent", status: done}
    - {round: 29, action: "Added explicit VIF=50.9 caveat ('SE inflated ~7x, directional evidence only'). Ridge regression (β_BCS=-1.53, sign-stable for all λ≥0) added to Appendix E.1.", assigned_to:
…[truncated 8877 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 152
}
```

</details>

---


### Tool result

_source line 3073 · 2026-05-22T22:51:17.082607+00:00_

Web search results for query: "ACL Rolling Review 2026 long paper 8 pages short paper 4 pages format requirements template"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Discontinuation of the MS Word Template – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/discontinuation-word-template"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here is the ACL Rolling Review 2026 format requirements information:

## Paper Length Requirements

Short papers: 4 content pages maximum, Long papers: 8 content pages maximum. Sections on ethical considerations and limitations do not count towards page limit.

## Formatting Guidelines

Appendices are in double-column format, with the exception of math-heavy sections where single-column is needed for readability 
…[truncated 750 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 6041
}
```

</details>

---


### Tool call

_source line 3074 · 2026-05-22T22:51:43.985764+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "schema-dag-extraction",
  "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "schema-dag-extraction",
    "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
  }
}
```

</details>

---


### Tool call

_source line 3075 · 2026-05-22T22:51:44.136724+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 3076 · 2026-05-22T22:51:47.714992+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 3729
}
```

</details>

---


### Tool result

_source line 3077 · 2026-05-22T22:51:47.715417+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 3578
}
```

</details>

---


### Tool call

_source line 3078 · 2026-05-22T22:52:25.613621+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "schema-dag-extraction",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026（通过 ARR May 2026 提交）\n- **截止日期**：2026-05-25\n- **格式要求**：Long paper ≤8 页正文，参考文献不限页数，Limitations/Ethical Considerations 不计入页数\n- **模板**：ACL LaTeX，`[review]` 模式\n- **匿名**：double-blind\n- **评分标准**：5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit（含 0.5 级 borderline）\n\n## 论文路径\n- LaTeX 源码：`projects/schema-dag-extraction/docs/paper/main.tex`（含 `\\input` 的各子文件）\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_round_31/submitted.pdf`\n\n## 你的审查侧重\n\n**方法严谨性**——重点关注以下方面：\n\n1. **统计方法学**：\n   - 回归分析的假设检验是否恰当（VIF、多重共线性处理）\n   - Bootstrap CI 的构造是否合理（共享样本的 anti-conservative 风险）\n   - TOST 等价性检验的 margin 选择和量表依赖性\n   - 多重比较校正（Bonferroni 或其他）\n   - 效应量报告的完整性\n\n2. **实验设计**：\n   - BCS-controlled batch 构造方法的有效性\n   - 因果 vs 相关性 claim 是否与证据匹配\n   - Cross-model validation 的充分性（3 个开源模型 + 1 API 模型）\n   - Greedy decoding + single seed 对结论稳健性的影响\n\n3. **指标有效性**：\n   - SCS/BCS 作为 confusability proxy 的理论基础\n   - Embedding 选择（MiniLM vs Qwen3 hidden states）的合理性\n   - 评估指标（text-match F1, accuracy, relaxed F1）的适当性\n\n4. **证据强度**：\n   - 核心 claim 的证据链是否完整\n   - 负面结果（NER null, SDGD failure）的报告是否充分\n   - DocRED VIF=50.9 下的 partial correlation 可信度\n\n请输出完整审稿意见，包括：Summary、Strengths（逐条）、Weaknesses（逐条，标注 severity: Must-Fix / Should-Fix / Minor）、Questions、Missing References、Overall Assessment（评分 + 置信度）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "schema-dag-extraction",
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026（通过 ARR May 2026 提交）\n- **截止日期**：2026-05-25\n- **格式要求**：Long paper ≤8 页正文，参考文献不限页数，Limitations/Ethical Considerations 不计入页数\n- **模板**：ACL LaTeX，`[review]` 模式\n- **匿名**：double-blind\n- **评分标准**：5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit（含 0.5 级 borderline）\n\n## 论文路径\n- LaTeX 源码：`projects/schema-dag-extraction/docs/paper/main.tex`（含 `\\input` 的各子文件）\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_round_31/submitted.pdf`\n\n## 你的审查侧重\n\n**方法严谨性**——重点关注以下方面：\n\n1. **统计方法学**：\n   - 回归分析的假设检验是否恰当（VIF、多重共线性处理）\n   - Bootstrap CI 的构造是否合理（共享样本的 anti-conservative 风险）\n   - TOST 等价性检验的 margin 选择和量表依赖性\n   - 多重比较校正（Bonferroni 或其他）\n   - 效应量报告的完整性\n\n2. **实验设计**：\n   - BCS-controlled batch 构造方法的有效性\n   - 因果 vs 相关性 claim 是否与证据匹配\n   - Cross-model validation 的充分性（3 个开源模型 + 1 API 模型）\n   - Greedy decoding + single seed 对结论稳健性的影响\n\n3. **指标有效性**：\n   - SCS/BCS 作为 confusability proxy 的理论基础\n   - Embedding 选择（MiniLM vs Qwen3 hidden states）的合理性\n   - 评估指标（text-match F1, accuracy, relaxed F1）的适当性\n\n4. **证据强度**：\n   - 核心 claim 的证据链是否完整\n   - 负面结果（NER null, SDGD failure）的报告是否充分\n   - DocRED VIF=50.9 下的 partial correlation 可信度\n\n请输出完整审稿意见，包括：Summary、Strengths（逐条）、Weaknesses（逐条，标注 severity: Must-Fix / Should-Fix / Minor）、Questions、Missing References、Overall Assessment（评分 + 置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 3079 · 2026-05-22T22:52:39.473976+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 13860
}
```

</details>

---


### Tool call

_source line 3080 · 2026-05-22T22:52:39.675194+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "schema-dag-extraction",
  "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026（通过 ARR May 2026 提交）\n- **截止日期**：2026-05-25\n- **格式要求**：Long paper ≤8 页正文，参考文献不限页数，Limitations/Ethical Considerations 不计入页数\n- **模板**：ACL LaTeX，`[review]` 模式\n- **匿名**：double-blind\n- **评分标准**：5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit（含 0.5 级 borderline）\n\n## 论文路径\n- LaTeX 源码：`projects/schema-dag-extraction/docs/paper/main.tex`（含 `\\input` 的各子文件）\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_round_31/submitted.pdf`\n\n## 你的审查侧重\n\n**新颖性与完整性**——重点关注以下方面：\n\n1. **贡献定位与新颖性**：\n   - 与 LLM-PEE (Liu et al., 2025) 的技术差异是否充分——SCS/BCS 作为 analytical metric vs partition tool\n   - \"First controlled study\" claim 的合理性和限定语\n   - 方法论贡献（BCS-controlled batch design）vs 纯 empirical findings 的平衡\n   - Schema decomposition (SDGD) 负面结果的价值\n\n2. **Related Work 覆盖**：\n   - Training-free LLM IE 文献是否全面（特别是 2025-2026 新工作）\n   - Schema complexity 相关文献（label confusion, hierarchical classification）\n   - 是否遗漏关键 baseline 或竞品\n   - 引用格式和完整性\n\n3. **叙事一致性**：\n   - Abstract → Introduction → Results → Discussion 的逻辑链\n   - 三个 RQ 是否被充分回答\n   - 正面结果和负面结果的平衡呈现\n   - Claim 与 evidence 的匹配度（是否存在 overclaim）\n\n4. **写作质量**：\n   - 学术英语质量\n   - 术语定义的清晰度（SCS, BCS, count curves, BCS-controlled）\n   - 图表的信息密度和可读性\n   - Limitations 的充分性和诚实度\n   - 8 页内容的空间分配是否合理\n\n5. **可复现性**：\n   - 实验细节是否足以复现\n   - 代码/数据承诺（footnote 提到 acceptance 后释放）\n   - Hyperparameter 报告\n\n请输出完整审稿意见，包括：Summary、Strengths（逐条）、Weaknesses（逐条，标注 severity: Must-Fix / Should-Fix / Minor）、Questions、Missing References、Overall Assessment（评分 + 置信度）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "schema-dag-extraction",
    "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026（通过 ARR May 2026 提交）\n- **截止日期**：2026-05-25\n- **格式要求**：Long paper ≤8 页正文，参考文献不限页数，Limitations/Ethical Considerations 不计入页数\n- **模板**：ACL LaTeX，`[review]` 模式\n- **匿名**：double-blind\n- **评分标准**：5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit（含 0.5 级 borderline）\n\n## 论文路径\n- LaTeX 源码：`projects/schema-dag-extraction/docs/paper/main.tex`（含 `\\input` 的各子文件）\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_round_31/submitted.pdf`\n\n## 你的审查侧重\n\n**新颖性与完整性**——重点关注以下方面：\n\n1. **贡献定位与新颖性**：\n   - 与 LLM-PEE (Liu et al., 2025) 的技术差异是否充分——SCS/BCS 作为 analytical metric vs partition tool\n   - \"First controlled study\" claim 的合理性和限定语\n   - 方法论贡献（BCS-controlled batch design）vs 纯 empirical findings 的平衡\n   - Schema decomposition (SDGD) 负面结果的价值\n\n2. **Related Work 覆盖**：\n   - Training-free LLM IE 文献是否全面（特别是 2025-2026 新工作）\n   - Schema complexity 相关文献（label confusion, hierarchical classification）\n   - 是否遗漏关键 baseline 或竞品\n   - 引用格式和完整性\n\n3. **叙事一致性**：\n   - Abstract → Introduction → Results → Discussion 的逻辑链\n   - 三个 RQ 是否被充分回答\n   - 正面结果和负面结果的平衡呈现\n   - Claim 与 evidence 的匹配度（是否存在 overclaim）\n\n4. **写作质量**：\n   - 学术英语质量\n   - 术语定义的清晰度（SCS, BCS, count curves, BCS-controlled）\n   - 图表的信息密度和可读性\n   - Limitations 的充分性和诚实度\n   - 8 页内容的空间分配是否合理\n\n5. **可复现性**：\n   - 实验细节是否足以复现\n   - 代码/数据承诺（footnote 提到 acceptance 后释放）\n   - Hyperparameter 报告\n\n请输出完整审稿意见，包括：Summary、Strengths（逐条）、Weaknesses（逐条，标注 severity: Must-Fix / Should-Fix / Minor）、Questions、Missing References、Overall Assessment（评分 + 置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 3081 · 2026-05-22T22:52:41.149043+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1473
}
```

</details>

---


### Tool call

_source line 3082 · 2026-05-22T22:52:48.909960+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:TodoWrite",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 3083 · 2026-05-22T22:52:48.960757+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3084 · 2026-05-22T22:52:58.232439+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排（2 人）', 'status': 'completed', 'activeForm': '完成 Reviewer 编排决策'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '已派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿（等待 R1 + R2 返回）', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 和 Reviewer 2 完成独立审稿'}, {'content': 'Step 2: 交叉分享（转发审稿原文 + 收集 AGREE/REBUT）', 'status': 'pending', 'activeForm': '执行交叉分享流程'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '分析收敛状态'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '合成审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排（2 人）', 'status': 'completed', 'activeForm': '完成 Reviewer 编排决策'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '已派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿（等待 R1 + R2 返回）', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 和 Reviewer 2 完成独立审稿'}, {'content': 'Step 2: 交叉分享（转发审稿原文 + 收集 AGREE/REBUT）', 'status': 'pending', 'activeForm': '执行交叉分享流程'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '分析收敛状态'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '合成审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 3085 · 2026-05-22T22:52:58.283102+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 3086 · 2026-05-22T22:53:01.875898+00:00_

Round 1 已启动。两名 Reviewer 正在独立审稿，视觉审查 Agent 并行运行中。等待审稿结果返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 253

## Round 253

4 recorded events


### User

_source line 3087 · 2026-05-22T22:59:25.378153+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见：新颖性与完整性

---

### Paper Summary

本文研究 schema complexity 如何影响 training-free LLM 信息抽取性能，将"schema complexity"分解为两个独立维度：(1) candidate type 数量（count）和 (2) type 间语义混淆度（通过 embedding similarity 衡量的 SCS/BCS 指标）。通过在 4 个数据集（Few-NERD NER、FewRel RE、DocRED RE、MAVEN ED）上进行 BCS-controlled batch 实验，论文发现 count 产生单调性能下降，BCS 独立预测 type substitution errors，解释 FewRel 上约 27% 的跨 batch 准确率方差。论文还尝试了 Schema-DAG-Guided Decomposition (SDGD) 方法但报告了负面结果。论文的核心贡献是一个设计良好的受控实证研究，而非新方法。

---

### Strengths

**S1. 精心设计的受控实验方法论。** BCS-controlled batch design 在固定 count 的同时变化 confusability，这是该领域少见的严格实验设计。VIF 验证独立性、bootstrap CIs、equivalence tests、Bonferroni corrections、2×2 factorial analysis (Appendix C) 等统计工具的运用展现了高水平的方法论素养。在 training-free LLM IE 领域，大多数工作只做 benchmark 评测，本文的 controlled study 视角是值得肯定的。

**S2. 有价值的错误分类体系。** Section 4.4 和 Figure 2 的 error taxonomy (IntraSub, merge amplification, routing failure) 提供了超越简单相关性分析的机制性洞察。Figure 2 按 BCS bin 展示 IntraSub 单调递增的趋势，直接支撑了混淆度→替换错误的因果链条。这种 fine-grained error analysis 对后续工程优化有实际指导价值。

**S3. 诚实报告负面结果。** Section 5 的 SDGD 失败案例（routing accuracy 不足导致 decompose-then-merge 范式无法提升性能）对社区是有价值的信息。论文没有通过 cherry-picking 数据或过度包装来掩盖这一失败，这种学术诚实度值得赞赏。

**S4. 极其详尽的补充材料。** 18 页附录 (Appendix A–Y) 涵盖 factorial analysis、prompt sensitivity、cross-model validation、bootstrap CI robustness、domain distribution analysis、Monte Carlo simulation 等。这极大增强了可信度和可复现性，远超同类 empirical study 的平均水准。

**S5. 跨任务验证的广度。** 4 个数据集覆盖 NER (Few-NERD)、sentence-level RE (FewRel)、document-level RE (DocRED)、ED (MAVEN)，展示了 BCS-performance 关系在不同 IE 任务上的一致性趋势（尽管强度不同）。

**S6. SCS 作为 lightweight proxy 的实用价值。** Section 3.2 指出 SCS 是 pre-computed proxy，无需运行抽取即可估计 schema 难度。这对实际部署中的 schema 设计决策有直接应用价值。

---

### Weaknesses

**N1 [Must-Fix] 模型多样性不足，削弱 generalizability claim。**

- 具体位置：Section 3.5, Section 6, Appendix T/U
- 问题：主实验仅使用 Qwen3-32B（通过 vLLM API）。Cross-model validation 分散在 Appendix T (Gemini 2.5 Flash, LLaMA-3.1-8B) 和 Appendix U (LLaMA-3.1-70B)，但这些被定位为 confirmatory 而非 primary 分析。然而 Section 6 声称 "BCS captures a structural property of the schema-model interaction"——这是一个关于 schema-model 交互的通用性声明，但主要证据仅来自单一模型家族。不同模型架构（如 GPT-4、Claude）、不同 instruction-tuning 策略、不同 tokenizer 对 type name 的处理方式都可能产生不同的 BCS-performance relationship。
- 为什么影响接收：如果 BCS 的预测力在 Qwen 家族之外显著减弱，论文的核心 claim 将被大幅限制。一个声称揭示"结构性质"的研究不应仅依赖单一模型。
- 建议修改方向：将至少一个非 Qwen 家族模型（如 LLaMA-3.1-70B 或 Gemini 2.5 Flash）的 BCS-controlled 实验提升为 primary 分析，在正文中报告关键结果。或者，将 Section 6 的声明严格限定为 "在 Qwen3-32B 上观察到的模式"。

**N2 [Must-Fix] 相对于 LLM-PEE 的新颖性边际狭窄。**

- 具体位置：Section 2 (Related Work), Section 3.2
- 问题：SCS 本质上是 type label embedding 的 cosine similarity——这与 LLM-PEE (Liu et al., 2025) 用于 schema partitioning 的操作在计算层面相同。论文在 Section 2 提出三点差异：(1) controlled analysis vs. engineering solution, (2) BCS-controlled experiments isolate count from confusability, (3) SDGD reveals merge amplification bottleneck。但 (1) 是视角差异而非技术创新；(3) 是负面结果。真正有新颖性的是 (2) BCS-controlled experimental design，但这是实验方法论贡献而非 metric 层面的创新。论文未充分论证 SCS/BCS 作为 "analytical metric" 比 LLM-PEE 的 similarity-based partitioning 提供了什么新的 scientific understanding。
- 为什么影响接收：如果审稿人认为核心 metric 与已有工作重叠度过高，可能质疑论文的技术贡献。
- 建议修改方向：(a) 更明确地将贡献定位为 "controlled empirical study using embedding similarity as an analytical lens"，弱化 SCS/BCS 作为独立贡献的叙事；(b) 增加与 LLM-PEE 的直接实验对比（例如：用 LLM-PEE 的 partitioning 策略 vs. SDGD 在相同数据集上的对比）；(c) 讨论 SCS/BCS 何时比 LLM-PEE 的 similarity 提供更好的预测。

**W1 [Should-Fix] 未解释方差与因果模糊性。**

- 具体位置：Section 4.3, Section 6
- 问题：BCS 解释 FewRel 上约 27% 的 accuracy variance（adjusted R² = 0.273）。73% 的方差未被解释。Section 4.5 讨论了 centrality 作为潜在 confound 但发现与 BCS 混淆。Section 6 使用了半因果性语言（"BCS captures a structural property"），但相关性证据无法完全支撑这一声明。论文未充分讨论什么其他因素（如 prompt formatting、type definition 质量、sentence complexity）可能解释剩余方差。
- 建议：(a) 在 Discussion 中明确列出可能的未解释因素；(b) 将 "captures a structural property" 改为更审慎的措辞（如 "serves as a useful predictor of"）；(c) 讨论在什么条件下 27% 的解释力对实际应用有足够的指导价值。

**W2 [Should-Fix] Schema Decomposition (RQ3) 分析不充分。**

- 具体位置：Section 5（仅约半栏正文）
- 问题：RQ3 是论文提出的三个研究问题之一，但 Section 5 仅用约半栏篇幅处理。SDGD 失败的原因分析停留在 "routing accuracy 不足" 层面，缺乏深入探究：为什么 graph coloring 的 routing 不可靠？是否有 oracle routing 的 upper bound 分析（Appendix B Table 9 提供了一些，但应在正文中讨论）？是否存在不需要 merge 步骤的分解策略？论文承诺了一个完整 RQ 但交付了一个初步观察。
- 建议：将 Appendix B 的 oracle routing 结果和 Table 9 的策略对比提升到正文；讨论 routing 失败的具体模式；至少简要讨论避免 merge 的替代架构（如 hierarchical extraction、confidence-gated selection）。

**W3 [Should-Fix] BCS 指标设计选择未经消融。**

- 具体位置：Section 3.2
- 问题：BCS 对 batch 内所有 pairwise SCS 取均值。但在实际混淆场景中，一个高度相似的 type pair 可能主导大部分错误，而均值会稀释这一信号。论文未比较 max-based BCS (max pairwise SCS)、top-k 均值、或加权方案。此外，embedding 模型选择对 SCS 值有显著影响——论文使用 MiniLM 作为主要 embedding（Section 3.2），但仅在 Appendix I 简要提及 cross-embedding 验证（Qwen3 hidden states）。
- 建议：至少比较 mean-BCS vs. max-BCS vs. top-3-mean-BCS 的预测力差异；讨论为什么均值优于（或不如）max 作为混淆度代理。

**W4 [Minor] 非线性关系建模不足。**

- 具体位置：Figure 1a, Section 4.1
- 问题：Few-NERD NER 的 count curve 明显呈 U 形（先降后升），但论文在讨论 count-performance 关系时主要使用 Pearson 线性相关。虽然也报告了 Spearman 相关，但未系统地使用 piecewise linear 或多项式回归来刻画这一非线性模式。U 形的机制解释（"type-filtering overhead"）值得更严格的验证。
- 建议：对 NER count curve 做 piecewise regression 或至少报告分段 Pearson 相关（如 count ≤ 16 和 count > 16 分别的趋势）。

**W5 [Minor] 部分 Related Work 覆盖缺失。**

- 具体位置：Section 2
- 问题：以下近期工作与论文主题直接相关但未被引用：
  - **GLiREL** (NAACL 2025)：zero-shot RE 使用 label embedding similarity 计算，与 SCS 的 label confusability 主题直接相关
  - **PARSE** (Shrinivas et al., 2025)：LLM-driven schema optimization for entity extraction，从工程角度处理 schema complexity
  - **ASEE** (2025)：Adaptive Schema-Aware Event Extraction，用 retrieval 动态选择 schema，是处理 schema scalability 的替代方案
- 建议：在 Section 2 补充讨论这些工作，特别是 GLiREL 的 label embedding approach 与 SCS 的异同。

**W6 [Minor] Figure 1b 可读性。**

- 具体位置：Figure 1b
- 问题：Figure 1b 包含多个 overlapping bars（3 个 batch composition × 多个条件），在当前尺寸下难以准确读取个别条件的数值。slope 趋势可见但具体差异不清晰。
- 建议：考虑改用 grouped line chart 或增大 figure 尺寸。

---

### Questions to Authors

**Q1.** 是否测试过 max-based confusability metric（batch 内最大 pairwise SCS）是否比 mean-based BCS 在预测性能方面表现更好？

**Q2.** Figure 1a 中 NER 的 U 形 count curve——你们将其部分归因于低 count 时的 type-filtering overhead。是否通过检查不同 count level 的 per-type recall 来验证了这一解释？

**Q3.** VIF < 1.15 证明了实验设计中 count 和 BCS 的低共线性，但这是否保证它们对 performance 的效应是 additive 的？Appendix C 的 factorial analysis 部分回答了这个问题，但仅在 2 个数据集上验证。

**Q4.** 为什么选择 Qwen3-32B 作为主模型？是否有证据表明 BCS-performance 关系在训练数据分布根本不同的模型（如 GPT-4o、Claude）上同样成立？

**Q5.** 对于 SDGD 负面结果 (Section 5)，是否考虑过完全避免 merge 步骤的分解方案（如 hierarchical extraction with type-level confidence gating）？

---

### Missing References

1. GLiREL (NAACL 2025) — zero-shot RE using label embeddings and similarity computation
2. PARSE (Shrinivas et al., 2025) — LLM-driven schema optimization for entity extraction
3. ASEE (2025) — Adaptive Schema-Aware Event Extraction with retrieval-augmented schema selection

---

## 总体评分

**Overall Assessment: 3.5 — Borderline Conference**

**一句话总结**: 一篇方法论严谨的受控实证研究，揭示了 schema confusability 对 training-free LLM IE 的独立预测作用，但核心 metric 相对于 LLM-PEE 新颖性有限，且单一主模型设计削弱了 generalizability claim。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计严谨（BCS-controlled batches, factorial analysis, bootstrap CIs），统计方法论水准高。但单一主模型限制了结论的普适性，Section 6 的因果性语言超出相关性证据的支撑范围。 |
| Excitement | 3/5 | 研究问题实际重要（理解 schema complexity 为何降低 LLM IE 性能），controlled study 视角在该领域新颖。但核心洞察（更多类型→性能下降；相似类型→混淆）在直觉上可预期，SCS/BCS 指标创新度有限。 |
| Reproducibility | 4/5 | Prompt 模板 (Appendix G)、batch 构建细节 (Section 3.3)、统计方法均有详细描述。18 页附录提供了极其充分的实验细节。代码/数据承诺 acceptance 后发布。扣分项：未报告计算成本和 API 调用量。 |
| Reviewer Confidence | 4/5 | 熟悉 training-free LLM IE 和 schema complexity 研究领域，仔细检查了实验方法论和统计分析。 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 模型多样性不足
- 具体位置：Section 3.5, Section 6
- 主实验仅 Qwen3-32B，cross-model validation 在附录。声称揭示 "structural property of schema-model interaction" 但主要证据来自单一模型家族。
- 影响接收：核心 claim 的 generalizability 无法确认。
- 建议：提升至少一个非 Qwen 模型为主分析，或严格限定 claim 范围。

**N2** [critical] 相对于 LLM-PEE 的新颖性论证不充分
- 具体位置：Section 2, Section 3.2
- SCS 与 LLM-PEE 的 embedding similarity partitioning 在计算层面相同。论文未充分论证 "analytical metric vs. engineering tool" 的区分带来了什么新的科学理解。
- 影响接收：技术贡献的独特性可能受到质疑。
- 建议：增加与 LLM-PEE 的直接实验对比或更清晰地定位为 empirical study。

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 未解释方差讨论不足（73% unexplained, Section 4.3/6）
**W2** [warning] RQ3 (Schema Decomposition) 分析不充分（Section 5 仅半栏）
**W3** [warning] BCS 指标设计未经消融（mean vs. max vs. top-k, Section 3.2）

## 小问题（不影响接收）

- W4: NER U 形 count curve 的非线性建模不足 (Figure 1a)
- W5: 遗漏 GLiREL, PARSE, ASEE 等相关文献 (Section 2)
- W6: Figure 1b 在当前尺寸下可读性欠佳

## 主要优势

- S1: BCS-controlled batch design 是该领域少见的严格实验方法论
- S2: Error taxonomy (IntraSub, merge amplification) 提供机制性洞察
- S3: SDGD 负面结果的诚实报告
- S4: 18 页附录提供极其详尽的统计 robustness checks
- S5: 跨 4 个数据集/3 个 IE 任务的验证广度
- S6: SCS 作为 schema 难度 pre-deployment proxy 的实用价值

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 3088 · 2026-05-22T22:59:49.858141+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排（2 人）', 'status': 'completed', 'activeForm': '完成 Reviewer 编排决策'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '已派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿（等待 R1 返回，R2 已完成）', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 完成独立审稿（Reviewer 2 已返回 3.5 分）'}, {'content': 'Step 2: 交叉分享（转发审稿原文 + 收集 AGREE/REBUT）', 'status': 'pending', 'activeForm': '执行交叉分享流程'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '分析收敛状态'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '合成审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排（2 人）', 'status': 'completed', 'activeForm': '完成 Reviewer 编排决策'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '已派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿（等待 R1 返回，R2 已完成）', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 完成独立审稿（Reviewer 2 已返回 3.5 分）'}, {'content': 'Step 2: 交叉分享（转发审稿原文 + 收集 AGREE/REBUT）', 'status': 'pending', 'activeForm': '执行交叉分享流程'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '分析收敛状态'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '合成审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 3089 · 2026-05-22T22:59:49.908776+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 3090 · 2026-05-22T22:59:52.354385+00:00_

等待 Reviewer 1 审稿意见返回后进入 Step 2 交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 254

## Round 254

2 recorded events


### User

_source line 3091 · 2026-05-22T22:59:54.931139+00:00_

[Reviewer 2 审稿结果]:
审稿完成。总结：

- **Overall: 3.5 (Borderline Conference)**
- **Soundness 3.5/5 | Excitement 3/5 | Reproducibility 4/5 | Confidence 4/5**
- **2 个 Must-Fix**：单一主模型削弱 generalizability claim；SCS/BCS 相对于 LLM-PEE 新颖性论证不足
- **3 个 Should-Fix**：73% 未解释方差讨论缺失；RQ3 分析过浅；BCS 指标设计未消融
- **3 个 Minor**：非线性建模不足；遗漏相关文献；Figure 1b 可读性

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 3092 · 2026-05-22T23:00:00.830278+00:00_

R2 结果已确认（与之前收到的详细意见一致）。继续等待 Reviewer 1 返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 255

## Round 255

8 recorded events


### User

_source line 3093 · 2026-05-22T23:01:13.040625+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见（方法严谨性）

### 总体评分
**Overall**: 3.5 / 5（Borderline Conference）
**Confidence**: 4/5（Quite sure）

**一句话总结**: FewRel 上的 BCS-可分离性分析方法严谨、结论可信，但核心 confusability claim 实质上仅在 RE 任务上成立——NER 为 null、MAVEN 被 centrality 完全混淆、DocRED 因 VIF=50.9 无法可靠量化——标题和摘要对 "Information Extraction" 的泛化声明超出了证据支撑范围。

### 官方维度打分

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | FewRel 分析严谨（VIF=1.18, cluster bootstrap, Bonferroni 后 p<0.001），但 DocRED VIF=50.9 下 partial correlation 不可靠，MAVEN BCS 信号被 centrality 完全解释，证据链仅在 FewRel RE 上完整 |
| Excitement | 3/5 | 研究问题实用，BCS 指标有新意；但 confusability 效应仅限 RE、SDGD 全面失败、actionable guidance 有限 |
| Reproducibility | 4/5 | 实验设置详细，使用开源模型，承诺代码/数据开源；Gemini API 调用不可完全复现 |

---

### 主要优势

**S1.** FewRel 上的实验设计严谨度高于领域平均水平：BCS-controlled batch 构造（§3.3）、VIF=1.18 确认正交性、cluster bootstrap（Appendix E.3）处理 shared-instance 依赖、Bonferroni 校正后核心结论仍成立。

**S2.** 负面结果的诚实报告有社区价值：NER null（§4.3）、MAVEN centrality confound（§4.5）、SDGD 全面失败（§5）。Few-NERD null power analysis（Appendix E.2）正确描述为 "absence of evidence"。

**S3.** BCS 作为 deployment 前 proxy 有实用潜力——仅依赖 schema 结构和 MiniLM embedding，无需运行抽取。

**S4.** 18 页附录覆盖 prompt sensitivity、cross-model、Monte Carlo simulation 等，提供了大量可验证细节。

---

### Must-Fix（影响接收决定）

**N1** [critical] 标题与摘要泛化声明超出证据范围
- Title 覆盖 NER/RE/ED，但 confusability 独立预测效应仅在 FewRel RE 成立。NER 为 null，MAVEN 被 centrality 混淆，DocRED 因 VIF=50.9 不可靠。
- 建议：标题改为 RE-specific 或加限定词；摘要首段即标注 task-specificity。

**N2** [critical] DocRED 主文分析与 VIF=50.9 的矛盾处理
- §4.3 报告 partial ρ=−0.762 并称 "persists under ridge regularization"，语气像有意义的 replication。但 §6 承认 "usable only as directional evidence"。VIF=50.9 下标准误膨胀 ~7x，ridge 不解决共线性的根本语义问题。
- 建议：§4.3 首句标注 VIF=50.9 + "仅供方向性参考"；将详细数值报告移至 appendix。

---

### Should-Fix（影响评分）

**W1** TOST logit-scale 不通过仅在 Limitations 提及，主文 §4.4 未标注量表依赖性。Probability 和 logit scale 上的 ±3pp 语义不同。

**W2** Cross-model validation 未覆盖 TOST 和 SDGD 分析，且无闭源 frontier model（GPT-4o, Claude）。

**W3** Extreme-BCS batch 可能 confound domain composition（Appendix E.4 显示 low/high-BCS 有 domain 偏向），regression 未控制 domain diversity。

**W4** MiniLM vs. Qwen3 embedding 捕获不同维度（§4.5）但论文未讨论哪个更接近 LLM 实际 confusability 机制。

**W5** FP8 量化 non-determinism（SD=0.83pp）占 observed effect 18-44%，未提供对 regression CI 影响的 power analysis。

---

### 小问题
- Type name 粒度差异（Few-NERD "person-scholar" vs. MAVEN "Catastrophe"）对 SCS 跨数据集可比性的影响未讨论
- Table 1 Few-NERD "trigger mentions" 术语与 NER 不一致
- Figure 1(b) accuracy 定义应直接标注
- Type-level r²=1.3-1.7% 过低，在主文讨论价值有限
- Appendix N Monte Carlo ρ_pair=0.35 来源不清

---

### Questions
1. DocRED 的 BCS semipartial R² 数值是多少？在 VIF=50.9 下如何解读？
2. FewRel 是否检查过 centrality 作为 confound（类似 MAVEN §4.5）？
3. Oracle routing 仅达 72.4%（vs. single-type ~85%+），说明 decomposition 本身有问题——是否充分讨论？

### Missing References
- Li et al. (2023) "Evaluating ChatGPT's Information Extraction Capabilities"
- Josifoski et al. (2022) "GenIE: Generative Information Extraction"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 3094 · 2026-05-22T23:01:35.210070+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-0.7: 初始化 + 派发', 'status': 'completed', 'activeForm': '已完成初始化和派发'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': 'R1=3.5, R2=3.5 均已返回'}, {'content': 'Step 2: 交叉分享（转发审稿原文 + 收集 AGREE/REBUT）', 'status': 'in_progress', 'activeForm': '向 R1 和 R2 转发对方审稿原文，收集逐条回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '分析收敛状态'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '合成审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0-0.7: 初始化 + 派发', 'status': 'completed', 'activeForm': '已完成初始化和派发'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': 'R1=3.5, R2=3.5 均已返回'}, {'content': 'Step 2: 交叉分享（转发审稿原文 + 收集 AGREE/REBUT）', 'status': 'in_progress', 'activeForm': '向 R1 和 R2 转发对方审稿原文，收集逐条回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '分析收敛状态'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '合成审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 3095 · 2026-05-22T23:01:35.311017+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "TodoWrite",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 3096 · 2026-05-22T23:02:13.384734+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "schema-dag-extraction",
  "text": "以下是 Reviewer 2（新颖性与完整性）的完整审稿意见。请逐条回应：对每个 Weakness 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见\n\n### Strengths\nS1. 精心设计的受控实验方法论（BCS-controlled batch design，VIF 验证，bootstrap CIs，Bonferroni corrections，2×2 factorial analysis）\nS2. 有价值的错误分类体系（IntraSub, merge amplification, routing failure）\nS3. 诚实报告负面结果（SDGD Section 5）\nS4. 极其详尽的补充材料（18 页附录）\nS5. 跨任务验证的广度（4 个数据集，3 个 IE 任务）\nS6. SCS 作为 lightweight proxy 的实用价值\n\n### Must-Fix\n**N1 [Must-Fix] 模型多样性不足，削弱 generalizability claim。**\n主实验仅 Qwen3-32B，cross-model validation 在 Appendix T/U（Gemini 2.5 Flash, LLaMA-3.1-8B/70B）。Section 6 声称 \"BCS captures a structural property of the schema-model interaction\"，但主要证据仅来自单一模型家族。不同模型架构、instruction-tuning 策略、tokenizer 对 type name 的处理方式都可能产生不同的 BCS-performance relationship。\n\n**N2 [Must-Fix] 相对于 LLM-PEE 的新颖性边际狭窄。**\nSCS 本质上是 type label embedding 的 cosine similarity——与 LLM-PEE (Liu et al., 2025) 计算层面相同。论文提出三点差异：(1) controlled analysis vs. engineering solution, (2) BCS-controlled experiments, (3) SDGD reveals merge amplification。但 (1) 是视角差异非技术创新；(3) 是负面结果。真正有新颖性的是 (2) BCS-controlled design，但这是实验方法论贡献非 metric 创新。\n\n### Should-Fix\n**W1 [Should-Fix] 未解释方差与因果模糊性。**\nBCS 仅解释 FewRel 约 27% accuracy variance，73% 未解释。Section 6 使用半因果性语言但相关性证据无法完全支撑。未讨论 prompt formatting、type definition 质量、sentence complexity 等其他因素。\n\n**W2 [Should-Fix] Schema Decomposition (RQ3) 分析不充分。**\nRQ3 是三个研究问题之一，但 Section 5 仅约半栏。SDGD 失败原因停留在 \"routing accuracy 不足\"，缺乏深入探究（oracle routing upper bound, 替代架构如 hierarchical extraction）。\n\n**W3 [Should-Fix] BCS 指标设计选择未经消融。**\nBCS 对 batch 内所有 pairwise SCS 取均值，但一个高度相似的 type pair 可能主导大部分错误。未比较 max-based BCS, top-k 均值, 或加权方案。MiniLM embedding 选择仅在 Appendix I 简要验证。\n\n### Minor\n**W4** NER U 形 count curve 非线性建模不足（Figure 1a）\n**W5** 遗漏 GLiREL (NAACL 2025), PARSE, ASEE 相关文献\n**W6** Figure 1b 可读性欠佳\n\n### Questions\nQ1. 是否测试过 max-based BCS vs mean-based BCS？\nQ2. NER U 形 count curve 是否通过 per-type recall 验证了 type-filtering overhead 解释？\nQ3. VIF < 1.15 是否保证 count 和 BCS 效应是 additive 的？\nQ4. 为什么选择 Qwen3-32B 作为主模型？\nQ5. SDGD 是否考虑过避免 merge 步骤的分解方案？\n\n### Missing References\nGLiREL (NAACL 2025), PARSE (Shrinivas et al., 2025), ASEE (2025)\n\n### Overall: 3.5 Borderline Conference\nSoundness 3.5/5 | Excitement 3/5 | Reproducibility 4/5 | Confidence 4/5\n\n---\n\n请对 R2 的每个 Must-Fix (N1, N2)、Should-Fix (W1, W2, W3)、Minor (W4, W5, W6) 和 Questions (Q1-Q5) 逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "schema-dag-extraction",
    "text": "以下是 Reviewer 2（新颖性与完整性）的完整审稿意见。请逐条回应：对每个 Weakness 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见\n\n### Strengths\nS1. 精心设计的受控实验方法论（BCS-controlled batch design，VIF 验证，bootstrap CIs，Bonferroni corrections，2×2 factorial analysis）\nS2. 有价值的错误分类体系（IntraSub, merge amplification, routing failure）\nS3. 诚实报告负面结果（SDGD Section 5）\nS4. 极其详尽的补充材料（18 页附录）\nS5. 跨任务验证的广度（4 个数据集，3 个 IE 任务）\nS6. SCS 作为 lightweight proxy 的实用价值\n\n### Must-Fix\n**N1 [Must-Fix] 模型多样性不足，削弱 generalizability claim。**\n主实验仅 Qwen3-32B，cross-model validation 在 Appendix T/U（Gemini 2.5 Flash, LLaMA-3.1-8B/70B）。Section 6 声称 \"BCS captures a structural property of the schema-model interaction\"，但主要证据仅来自单一模型家族。不同模型架构、instruction-tuning 策略、tokenizer 对 type name 的处理方式都可能产生不同的 BCS-performance relationship。\n\n**N2 [Must-Fix] 相对于 LLM-PEE 的新颖性边际狭窄。**\nSCS 本质上是 type label embedding 的 cosine similarity——与 LLM-PEE (Liu et al., 2025) 计算层面相同。论文提出三点差异：(1) controlled analysis vs. engineering solution, (2) BCS-controlled experiments, (3) SDGD reveals merge amplification。但 (1) 是视角差异非技术创新；(3) 是负面结果。真正有新颖性的是 (2) BCS-controlled design，但这是实验方法论贡献非 metric 创新。\n\n### Should-Fix\n**W1 [Should-Fix] 未解释方差与因果模糊性。**\nBCS 仅解释 FewRel 约 27% accuracy variance，73% 未解释。Section 6 使用半因果性语言但相关性证据无法完全支撑。未讨论 prompt formatting、type definition 质量、sentence complexity 等其他因素。\n\n**W2 [Should-Fix] Schema Decomposition (RQ3) 分析不充分。**\nRQ3 是三个研究问题之一，但 Section 5 仅约半栏。SDGD 失败原因停留在 \"routing accuracy 不足\"，缺乏深入探究（oracle routing upper bound, 替代架构如 hierarchical extraction）。\n\n**W3 [Should-Fix] BCS 指标设计选择未经消融。**\nBCS 对 batch 内所有 pairwise SCS 取均值，但一个高度相似的 type pair 可能主导大部分错误。未比较 max-based BCS, top-k 均值, 或加权方案。MiniLM embedding 选择仅在 Appendix I 简要验证。\n\n### Minor\n**W4** NER U 形 count curve 非线性建模不足（Figure 1a）\n**W5** 遗漏 GLiREL (NAACL 2025), PARSE, ASEE 相关文献\n**W6** Figure 1b 可读性欠佳\n\n### Questions\nQ1. 是否测试过 max-based BCS vs mean-based BCS？\nQ2. NER U 形 count curve 是否通过 per-type recall 验证了 type-filtering overhead 解释？\nQ3. VIF < 1.15 是否保证 count 和 BCS 效应是 additive 的？\nQ4. 为什么选择 Qwen3-32B 作为主模型？\nQ5. SDGD 是否考虑过避免 merge 步骤的分解方案？\n\n### Missing References\nGLiREL (NAACL 2025), PARSE (Shrinivas et al., 2025), ASEE (2025)\n\n### Overall: 3.5 Borderline Conference\nSoundness 3.5/5 | Excitement 3/5 | Reproducibility 4/5 | Confidence 4/5\n\n---\n\n请对 R2 的每个 Must-Fix (N1, N2)、Should-Fix (W1, W2, W3)、Minor (W4, W5, W6) 和 Questions (Q1-Q5) 逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 3097 · 2026-05-22T23:02:45.711173+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 32326
}
```

</details>

---


### Tool call

_source line 3098 · 2026-05-22T23:02:45.862084+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "schema-dag-extraction",
  "text": "以下是 Reviewer 1（方法严谨性）的完整审稿意见。请逐条回应：对每个 Weakness 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见\n\n### Overall: 3.5 Borderline Conference | Confidence 4/5\nSoundness 3.5/5 | Excitement 3/5 | Reproducibility 4/5\n\n**一句话总结**: FewRel 上的 BCS-可分离性分析方法严谨、结论可信，但核心 confusability claim 实质上仅在 RE 任务上成立——NER 为 null、MAVEN 被 centrality 完全混淆、DocRED 因 VIF=50.9 无法可靠量化——标题和摘要对 \"Information Extraction\" 的泛化声明超出了证据支撑范围。\n\n### Strengths\nS1. FewRel 实验设计严谨度高于领域平均水平（BCS-controlled batch, VIF=1.18, cluster bootstrap, Bonferroni）\nS2. 负面结果的诚实报告有社区价值（NER null, MAVEN centrality confound, SDGD 失败）\nS3. BCS 作为 deployment 前 proxy 有实用潜力\nS4. 18 页附录提供大量可验证细节\n\n### Must-Fix\n**N1 [critical] 标题与摘要泛化声明超出证据范围**\nTitle 覆盖 NER/RE/ED，但 confusability 独立预测效应仅在 FewRel RE 成立。NER 为 null，MAVEN 被 centrality 混淆，DocRED 因 VIF=50.9 不可靠。建议标题改为 RE-specific 或加限定词；摘要首段即标注 task-specificity。\n\n**N2 [critical] DocRED 主文分析与 VIF=50.9 的矛盾处理**\n§4.3 报告 partial ρ=−0.762 并称 \"persists under ridge regularization\"，语气像有意义的 replication。但 §6 承认 \"usable only as directional evidence\"。VIF=50.9 下标准误膨胀 ~7x，ridge 不解决共线性的根本语义问题。建议 §4.3 首句标注 VIF=50.9 + \"仅供方向性参考\"；详细数值移至 appendix。\n\n### Should-Fix\n**W1** TOST logit-scale 不通过仅在 Limitations 提及，主文 §4.4 未标注量表依赖性。Probability 和 logit scale 上的 ±3pp 语义不同。\n\n**W2** Cross-model validation 未覆盖 TOST 和 SDGD 分析，且无闭源 frontier model（GPT-4o, Claude）。\n\n**W3** Extreme-BCS batch 可能 confound domain composition（Appendix E.4 显示 low/high-BCS 有 domain 偏向），regression 未控制 domain diversity。\n\n**W4** MiniLM vs. Qwen3 embedding 捕获不同维度（§4.5）但论文未讨论哪个更接近 LLM 实际 confusability 机制。\n\n**W5** FP8 量化 non-determinism（SD=0.83pp）占 observed effect 18-44%，未提供对 regression CI 影响的 power analysis。\n\n### Minor\n- Type name 粒度差异对 SCS 跨数据集可比性的影响未讨论\n- Table 1 Few-NERD \"trigger mentions\" 术语不一致\n- Figure 1(b) accuracy 定义应直接标注\n- Type-level r²=1.3-1.7% 过低，讨论价值有限\n- Appendix N Monte Carlo ρ_pair=0.35 来源不清\n\n### Questions\nQ1. DocRED 的 BCS semipartial R² 数值是多少？在 VIF=50.9 下如何解读？\nQ2. FewRel 是否检查过 centrality 作为 confound（类似 MAVEN §4.5）？\nQ3. Oracle routing 仅达 72.4%（vs. single-type ~85%+），说明 decomposition 本身有问题——是否充分讨论？\n\n### Missing References\n- Li et al. (2023) \"Evaluating ChatGPT's Information Extraction Capabilities\"\n- Josifoski et al. (2022) \"GenIE: Generative Information Extraction\"\n\n---\n\n请对 R1 的每个 Must-Fix (N1, N2)、Should-Fix (W1-W5)、Minor 和 Questions (Q1-Q3) 逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "schema-dag-extraction",
    "text": "以下是 Reviewer 1（方法严谨性）的完整审稿意见。请逐条回应：对每个 Weakness 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见\n\n### Overall: 3.5 Borderline Conference | Confidence 4/5\nSoundness 3.5/5 | Excitement 3/5 | Reproducibility 4/5\n\n**一句话总结**: FewRel 上的 BCS-可分离性分析方法严谨、结论可信，但核心 confusability claim 实质上仅在 RE 任务上成立——NER 为 null、MAVEN 被 centrality 完全混淆、DocRED 因 VIF=50.9 无法可靠量化——标题和摘要对 \"Information Extraction\" 的泛化声明超出了证据支撑范围。\n\n### Strengths\nS1. FewRel 实验设计严谨度高于领域平均水平（BCS-controlled batch, VIF=1.18, cluster bootstrap, Bonferroni）\nS2. 负面结果的诚实报告有社区价值（NER null, MAVEN centrality confound, SDGD 失败）\nS3. BCS 作为 deployment 前 proxy 有实用潜力\nS4. 18 页附录提供大量可验证细节\n\n### Must-Fix\n**N1 [critical] 标题与摘要泛化声明超出证据范围**\nTitle 覆盖 NER/RE/ED，但 confusability 独立预测效应仅在 FewRel RE 成立。NER 为 null，MAVEN 被 centrality 混淆，DocRED 因 VIF=50.9 不可靠。建议标题改为 RE-specific 或加限定词；摘要首段即标注 task-specificity。\n\n**N2 [critical] DocRED 主文分析与 VIF=50.9 的矛盾处理**\n§4.3 报告 partial ρ=−0.762 并称 \"persists under ridge regularization\"，语气像有意义的 replication。但 §6 承认 \"usable only as directional evidence\"。VIF=50.9 下标准误膨胀 ~7x，ridge 不解决共线性的根本语义问题。建议 §4.3 首句标注 VIF=50.9 + \"仅供方向性参考\"；详细数值移至 appendix。\n\n### Should-Fix\n**W1** TOST logit-scale 不通过仅在 Limitations 提及，主文 §4.4 未标注量表依赖性。Probability 和 logit scale 上的 ±3pp 语义不同。\n\n**W2** Cross-model validation 未覆盖 TOST 和 SDGD 分析，且无闭源 frontier model（GPT-4o, Claude）。\n\n**W3** Extreme-BCS batch 可能 confound domain composition（Appendix E.4 显示 low/high-BCS 有 domain 偏向），regression 未控制 domain diversity。\n\n**W4** MiniLM vs. Qwen3 embedding 捕获不同维度（§4.5）但论文未讨论哪个更接近 LLM 实际 confusability 机制。\n\n**W5** FP8 量化 non-determinism（SD=0.83pp）占 observed effect 18-44%，未提供对 regression CI 影响的 power analysis。\n\n### Minor\n- Type name 粒度差异对 SCS 跨数据集可比性的影响未讨论\n- Table 1 Few-NERD \"trigger mentions\" 术语不一致\n- Figure 1(b) accuracy 定义应直接标注\n- Type-level r²=1.3-1.7% 过低，讨论价值有限\n- Appendix N Monte Carlo ρ_pair=0.35 来源不清\n\n### Questions\nQ1. DocRED 的 BCS semipartial R² 数值是多少？在 VIF=50.9 下如何解读？\nQ2. FewRel 是否检查过 centrality 作为 confound（类似 MAVEN §4.5）？\nQ3. Oracle routing 仅达 72.4%（vs. single-type ~85%+），说明 decomposition 本身有问题——是否充分讨论？\n\n### Missing References\n- Li et al. (2023) \"Evaluating ChatGPT's Information Extraction Capabilities\"\n- Josifoski et al. (2022) \"GenIE: Generative Information Extraction\"\n\n---\n\n请对 R1 的每个 Must-Fix (N1, N2)、Should-Fix (W1-W5)、Minor 和 Questions (Q1-Q3) 逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 3099 · 2026-05-22T23:02:47.321959+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1459
}
```

</details>

---


### Assistant

_source line 3100 · 2026-05-22T23:02:49.850315+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 256

## Round 256

2 recorded events


### User

_source line 3101 · 2026-05-22T23:02:52.439794+00:00_

[Reviewer 1 审稿结果]:
已清理完毕。

**审稿完成。** 评分 3.5（Borderline Conference），核心判断：FewRel RE 上的 BCS 可分离性分析方法扎实（VIF=1.18, cluster bootstrap, semipartial R²=0.273），但 confusability claim 的泛化性受限——NER null、MAVEN centrality confound、DocRED VIF=50.9。两个 Must-Fix：(1) 标题/摘要 scope 与证据不匹配，(2) DocRED 主文处理与 Limitations 自相矛盾。五个 Should-Fix 覆盖 TOST 量表依赖、cross-model 覆盖缺口、domain confound、embedding 选择理论基础、FP8 non-determinism。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 3102 · 2026-05-22T23:02:56.475420+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 257

## Round 257

2 recorded events


### User

_source line 3103 · 2026-05-22T23:04:52.721342+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 的交叉回应

### Must-Fix

**[AGREE] R2-N1 模型多样性不足**
同意是实质问题（与我的 W2 一致），但 severity 建议降至 Should-Fix。论文在 4 模型 3 家族上验证了 BCS slope 方向一致性（Table 4, Appendix T/U），一阶 replication 达领域惯例。核心缺口在二阶分析（TOST、SDGD）仅 Qwen3-32B。

**[REBUT] R2-N2 新颖性边际狭窄**
R2 以 metric 新颖性标准评判方法论论文，框架不匹配。SCS metric 本身非新（= cosine similarity），但 BCS-controlled batch design + VIF verification + cluster bootstrap 的受控实验方法论在零样本 IE 领域是首次。LLM-PEE 用 embedding similarity 做 engineering partition，本文用它做 controlled study 的自变量——从工程到诊断的转变是实质性方法论创新。ARR guidelines 也反对 reject negative results（SDGD）。建议作者在 §2 更显式对比 LLM-PEE 的 uncontrolled 设计。

### Should-Fix

**[AGREE with nuance] R2-W1** 因果语言应更谨慎，但 73% 未解释方差的批评需上下文——27% semipartial R² 在 NLP 实验中已属 large effect。

**[AGREE] R2-W2** §5 主文对 RQ3 处理确实偏薄，oracle 仅 72.4% 说明 decomposition 框架有结构性问题。

**[REBUT partially] R2-W3** Appendix I (Table 15) 已做 mean vs max BCS 对比，R2 可能遗漏。但 top-k/加权方案未探索，部分同意。

### Minor

**[AGREE] R2-W4** NER U 形未正式建模。
**[REBUT partially] R2-W5** GLiREL 已被引用（References p.9, Boyler et al. 2025），R2 事实有误。PARSE/ASEE 待确认相关性。
**[AGREE] R2-W6** Figure 1b 可读性问题，与我的 minor issue 一致。

### Questions

**[REBUT] Q1** Appendix I Table 15 已对比 mean vs max BCS。
**[AGREE] Q2** Per-type recall by count level 可强化 U 形解释。
**[REBUT with nuance] Q3** VIF 不保证 additivity，论文用 TOST 回答此问题，但 logit-scale TOST 未通过（我的 W1）。
**[AGREE] Q4** Qwen3-32B 选择理由应明确。
**[AGREE] Q5** 无 merge 替代方案应在 Discussion 提及。

### 关键分歧
与 R2 的核心分歧在 N2（新颖性）：我认为本文的贡献是受控实验方法论，不应以 metric 新颖性标准评判。N1 同意但建议降级。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 3104 · 2026-05-22T23:05:06.001587+00:00_

Reviewer 1 交叉回应已收到。关键记录：

- **R2-N1 模型多样性**：[AGREE] 但建议降至 Should-Fix（4 模型 3 家族一阶 replication 达惯例）
- **R2-N2 LLM-PEE 新颖性**：[REBUT]（方法论贡献不应以 metric 新颖性标准评判）← **核心分歧**
- **R2-W1 未解释方差**：[AGREE with nuance]（27% 在 NLP 已属 large effect）
- **R2-W2 RQ3**：[AGREE]
- **R2-W3 BCS 消融**：[REBUT partially]（Appendix I Table 15 已有 mean vs max 对比）
- **R2-W5 GLiREL**：[REBUT]（R2 事实有误，GLiREL 已被引用）

等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 258

## Round 258

2 recorded events


### User

_source line 3105 · 2026-05-22T23:05:08.615613+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。核心分歧在 R2-N2（新颖性）：我认为本文贡献是受控实验方法论而非 metric，不应以 metric 新颖性标准评判。其余 Must-Fix/Should-Fix 大部分同意，W3 部分反驳（Appendix I 已有 mean vs max 消融）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 3106 · 2026-05-22T23:05:21.725902+00:00_

Reviewer 1 交叉回应已收到。核心分歧：R2-N2（新颖性标准）——R1 认为应以方法论而非 metric 创新评判。R2-N1 同意但建议降级为 Should-Fix。R2-W3 部分反驳（Appendix I Table 15 已有 mean vs max 对比）。

等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 259

## Round 259

14 recorded events


### User

_source line 3107 · 2026-05-22T23:06:47.910192+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 的交叉回应

---

### Must-Fix

**[AGREE] R1-N1: 标题与摘要泛化声明超出证据范围**

R1 的核心论断——confusability 的独立预测效应实质上仅在 FewRel RE 上干净成立——我基本同意，但认为 R1 对 NER 结果的概括稍有过度简化。

证据梳理：
- **FewRel RE**: BCS-controlled experiments, adjusted R²=0.273, VIF=1.18，Appendix E.1 确认 centrality 非 confound (VIF=1.25)。这是唯一干净的独立效应证据。
- **Few-NERD NER**: R1 称 "NER 为 null"，但 Figure 2(a) 显示 IntraSub 错误率确实随 BCS 单调递增（ρ=0.84–1.1 across BCS bins），说明混淆度→替换错误的*机制*在 NER 上仍然存在。整体准确率效应为 null 是因为 NER schema 的 achievable BCS range 过窄（Appendix D），无法产生可检测的准确率差异。这是一个有信息量的 boundary condition 发现，不应简单等同于 "NER 上不成立"。
- **DocRED**: VIF=50.9，R1 完全正确——不可靠。
- **MAVEN**: centrality confound，R1 正确。

**结论**：标题中的 "Information Extraction" 确实过度泛化。count-degradation 是跨任务通用的（Figure 1a, 4 个数据集），但 confusability 的独立效应仅在 sentence-level RE 上有清晰证据。建议标题加限定词或在 abstract 首句标注 task-specificity。但 R1 应该承认 NER 的 IntraSub 机制性证据（Figure 2a）比简单说 "null" 更有信息量。

---

**[AGREE] R1-N2: DocRED §4.3 的呈现顺序与 VIF=50.9 矛盾**

同意 R1 的具体批评。§4.3 的 DocRED 段落先报告 ρ=−0.762 和效应量（−25.0pp, −15.7pp），然后才在同段后半说 "this is uninterpretable as BCS-specific evidence"——这种先给数字再 qualify 的写法确实容易让读者产生 replication 的印象。虽然论文确实在同一段落内承认了 VIF=50.9 的问题（semipartial R²_BCS=0.056，即仅 5.6% unique variance），且 §6 再次标注为 "directional evidence only"，但 R1 关于呈现顺序的批评是对的——应该首句标注 VIF caveat。

补充我自己的观察：ridge regularization 保留了 negative BCS coefficient 方向，但 ridge 通过引入 bias 来换取 variance reduction，不解决两个预测变量在语义层面近乎等价的根本问题。论文应该更明确地承认 ridge 结果的局限性。

---

### Should-Fix

**[AGREE] R1-W1: TOST logit-scale 不通过应在主文标注**

R1 说得对。±3pp 在 probability scale 上和 logit scale 上的语义不同——probability space 的 0.40→0.43 vs. logit space 的 −0.41→−0.29 差异显著。TOST 在 logit scale 不通过意味着 "两个维度在非线性变换下的 additivity 无法确认"，这是一个影响结论强度的限制，不应仅出现在 Limitations。建议在 §4.4 讨论 factorial analysis 时直接标注量表依赖性。

---

**[AGREE] R1-W2: Cross-model 未覆盖 TOST/SDGD 且缺 frontier models**

与我自己的 N1（模型多样性不足）完全一致。Cross-model validation (Appendix T/U) 仅覆盖 count curves 和 BCS-controlled accuracy 分析，不包括 TOST equivalence test 和 SDGD 负面结果。这意味着这两个重要结论没有任何跨模型验证。缺少闭源 frontier models (GPT-4o, Claude) 进一步限制了 generalizability。

---

**[AGREE] R1-W3: Extreme-BCS batch 的 domain composition confound**

Appendix E.4 清楚显示 low-BCS batches 偏向 geography (45.5%) 和 creative work (25.5%)，high-BCS batches 偏向 science/taxonomy (49.5%) 和 event/temporal (26.0%)。如果不同 domain 的抽取难度本身不同，observed BCS-performance 关系可能部分反映 domain difficulty 而非 confusability per se。论文的 regression 未将 domain diversity 或 domain entropy 作为 control variable，这是一个实质性的遗漏。

我补充一个观察：Appendix E.4 报告了 normalized Shannon entropy 差异（low-BCS 更高），但未做 domain-controlled regression 或 stratified analysis。这可以作为修改建议的具体方向。

---

**[REBUT] R1-W4: MiniLM vs. Qwen3 embedding 机制讨论**

R1 的方向是对的（哪个 embedding 更接近 LLM 实际 confusability 机制？），但我认为论文在 Appendix I（BCS Aggregation Sensitivity, Table 15）和 §3.2 中已经提供了部分回答。论文使用 MiniLM 作为 primary BCS embedding 的理由是它是 "a pre-computed proxy comparable without running extraction"（§3.2）——即 SCS 的价值恰在于它是 deployment 前的轻量级代理，不需要访问目标 LLM 的内部表示。论文在 §4.5 讨论了 Qwen3 embedding 与 MiniLM 在 centrality 维度的差异，并在 Appendix I 做了 cross-embedding 验证（MEAN vs. MAX aggregation 方向一致）。

不过，R1 的深层问题——"MiniLM 的 cosine similarity 是否真正捕获了 Qwen3-32B 处理 type labels 时的混淆机制"——确实值得更多讨论。论文显示两种 embedding 在 FewRel 上方向一致，但这不等于它们捕获了相同的 confusability 维度。这是一个 Should-Fix 级别的讨论缺失，但不是方法论错误。

---

**[AGREE] R1-W5: FP8 量化 non-determinism 的 power 影响**

SD=0.83pp 占 observed BCS effect (Δ≈1.9–4.6pp based on BCS quartile gaps) 的 18–44%，这是不可忽视的测量噪声。论文报告了 bootstrap CIs 来处理采样方差，但 bootstrap 不区分信号方差和测量噪声——如果每次运行的同一 batch 产生 ±0.83pp 的随机波动，这会膨胀 residual variance 并削弱 regression 的 power。

虽然 power analysis 在这类 empirical study 中不常见，但 R1 的担忧是合理的：论文应至少讨论 FP8 noise floor 对 smallest detectable BCS effect 的影响（即：在 SD=0.83pp 下，regression 能可靠检测的最小 BCS slope 是多少？）。

---

### Minor

**[AGREE]** Type name 粒度差异对 SCS 跨数据集可比性的影响未讨论——确实，Few-NERD 的 fine-grained 66 types vs. FewRel 的 80 relation types 在 label name 长度和语义粒度上差异显著，这直接影响 embedding similarity 的分布，进而影响 SCS/BCS 的可比性。

**[AGREE]** Table 1 "trigger mentions" 术语不一致——Few-NERD 是 NER 数据集，使用 "trigger mentions" 是 ED 术语，应统一。

**[AGREE]** Figure 1(b) accuracy 定义应标注——BCS-controlled FewRel accuracy 的具体定义（是 batch-level accuracy 还是 per-type accuracy？）应在 figure caption 中明确。

**[REBUT]** Type-level r²=1.3–1.7% 讨论价值有限——我不完全同意这一点。虽然 r² 很低，但论文将其定位为 "statistically significant but modest"（§4.2），且明确指出 "Type-level cluster bootstrap yields wider but still significant CIs"，目的是建立 SCS→confusion 的 pair-level 基础证据，为后续的 batch-level BCS 分析铺路。如果完全不报告 type-level 结果，读者会质疑 "为什么跳到 batch-level"。问题不在于该不该讨论，而在于应降低其在叙事中的权重。

**[AGREE]** Appendix N Monte Carlo ρ_pair=0.35 来源不清——应标注这个参数的来源和 sensitivity（如 ρ_pair 取 0.2 或 0.5 时模拟结果如何变化）。

---

### Questions

**[AGREE] R1-Q1**: 论文已在 §4.3 报告 semipartial R²_BCS=0.056。在 VIF=50.9 下，这意味着仅 5.6% 的方差可唯一归因于 BCS，其余 90%+ 与 centrality 共享。这个数字本身就说明了 DocRED 上的 BCS 独立效应极弱。

**[REBUT] R1-Q2**: R1 问 FewRel 是否检查过 centrality 作为 confound。答案是**是的**——Appendix E.1 (Table 12) 明确报告了 FewRel 上 BCS-centrality 的 partial correlation controlling for degree centrality。结果：FewRel VIF=1.25（低共线性），partial correlation remains significant (p < 0.001)。这与 DocRED (VIF=50.9) 和 MAVEN 形成对比，恰恰证实了 FewRel 是唯一 centrality 不构成 confound 的数据集。R1 可能遗漏了这个附录分析。

**[AGREE] R1-Q3**: Oracle routing 仅达 72.4% (Table 9, Appendix B)，而 single-type baseline 的 per-type accuracy 通常 >85%。这确实说明 decomposition 本身有根本性问题——不仅仅是 routing 策略可以优化。论文在 Section 5 将失败归因于 "routing accuracy"，但 oracle routing 的上限也不高这一事实暗示 decompose-then-merge 架构本身引入了 merge amplification noise，即使 routing 完美也无法完全避免。论文对此的讨论确实不充分（与我自己的 W2 一致）。

---

### Missing References

**[AGREE]** Li et al. (2023) "Evaluating ChatGPT's Information Extraction Capabilities" 和 Josifoski et al. (2022) "GenIE" 都是该领域的重要参考文献，应被引用。

---

### 总体评估

R1 的审稿质量很高，核心论断（confusability claim 的 task-specificity）是这篇论文最重要的方法论约束。我的评分与 R1 一致：**3.5 Borderline Conference**。

R1 和我的主要分歧在于：
1. **NER 结果的性质**：R1 简单称 "null"，但 Figure 2(a) 的 IntraSub 机制性证据不应被忽视——这是 "null overall accuracy but active mechanism" 的 boundary condition，不同于 "no effect"。
2. **FewRel centrality check**：R1 问是否做过，实际上 Appendix E.1 Table 12 已做，且确认 centrality 非 confound (VIF=1.25)。

R1 和我一致的关键点：
- 标题/摘要的泛化程度超出证据
- DocRED 分析不可靠
- 模型多样性不足
- SDGD 分析不充分
- BCS 指标设计选择未经充分论证

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 3108 · 2026-05-22T23:07:29.042989+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-1: 初始化 + 独立审稿', 'status': 'completed', 'activeForm': '已完成'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': 'R1 和 R2 交叉回应均已收到'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '关键问题达成共识，1 处分歧记录在案'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'in_progress', 'activeForm': '合成审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0-1: 初始化 + 独立审稿', 'status': 'completed', 'activeForm': '已完成'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': 'R1 和 R2 交叉回应均已收到'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '关键问题达成共识，1 处分歧记录在案'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'in_progress', 'activeForm': '合成审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 3109 · 2026-05-22T23:07:29.095077+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "TodoWrite",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 3110 · 2026-05-22T23:07:33.965694+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool call

_source line 3111 · 2026-05-22T23:07:33.966197+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 3112 · 2026-05-22T23:07:34.017214+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T22:51:47.441284+00:00\", \"completed_at\": \"2026-05-22T22:55:23.304485+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-3\", \"message\": \"前 3 页连续纯文本，无任何 display item（figure/table）。审稿人打开论文后需翻到第 5 页才看到第一个 figure（Figure 1）。对于实证型论文，视觉锚点出现过晚，影响第一印象锚定。建议在前 2 页内加入一个概览图（如 schema complexity 与 performance 的关系示意图）或将 Figure 1 的核心 panel 前置\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-8\", \"message\": \"主正文 8 页仅含 4 个 display items（Figure 1-2, Table 1-2），密度 0.5/页。实证为主的论文通常 5-8 个/9 页。大量实验结果（Tables 3-30+）被放入 15 页 appendix，导致主正文视觉上偏\\\"文字墙\\\"。建议从 appendix 提升 1-2 个关键表格到正文\"}, {\"severity\": \"warning\", \"dimension\": \"page 2-3\", \"message\": \"连续 2 页纯文本（Related Work + Experimental Setup 开头），无 equation/figure/table 穿插。审稿人在此区间容易失去注意力\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"Title/Author/Abstract 排版整洁，符合 ACL 匿名投稿格式，无拥挤感\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Table 1（Dataset statistics）使用 booktabs 风格，排版规范。SCS 定义的数学公式（SCS(t_i, t_j)、BCS(B)）为页面增加了视觉变化，部分缓解了文字密集感\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 1 双 panel 设计合理：(a) 折线图展示 count-degradation curves，(b) 柱状图展示 BCS-controlled accuracy。蓝+橙配色色盲友好。Caption 自包含，包含误差线说明和统计证据引用。图内文字可读\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 2 格式规范，booktabs 风格。表格较小，页面以文字为主\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2 双 panel（Error taxonomy decomposition）信息量充足，多条线+标记点可区分。Caption 详细描述了 IntraSub 与 BCS 的单调关系。颜色区分度可接受\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"正文最后一页内容充实：Section 5（Schema Decomposition）+ Section 6（Discussion and Conclusion）+ Limitations 开头。页面填充 >90%，无大面积空白。Section heading 无孤悬\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Limitations 章节简短，覆盖 3 个限制点（模型范围、统计能力、维度覆盖），长度适中，符合 EMNLP 规范\"}, {\"severity\": 
…[truncated 722 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 3113 · 2026-05-22T23:07:34.067974+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 3114 · 2026-05-22T23:09:36.474300+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "schema-dag-extraction",
  "issues_yaml": "\n# Review Issues Tracker\n# Updated: 2026-05-22 Round 31 (fresh review)\n\n# ============================================================\n# R31 CRITICAL (2 items — consensus)\n# ============================================================\n\n- id: R31-C1\n  summary: \"标题/摘要对 'Information Extraction' 的泛化声明超出证据支撑：confusability 独立预测效应仅在 FewRel RE 上干净成立\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R1-N1, R2 AGREE. NER null（Figure 2a IntraSub 机制存在但 accuracy 无效应）, MAVEN centrality confound, DocRED VIF=50.9 不可靠. Count-degradation 跨任务通用，但 confusability 独立效应仅 sentence-level RE.\"}\n  action_items:\n    - {round: 31, action: \"标题加 RE-specific 限定词或通用限定；摘要首段标注 task-specificity；区分 count（通用）和 confusability（RE-specific）的 generalizability\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R31-C2\n  summary: \"DocRED §4.3 VIF=50.9 下 partial correlation 呈现顺序产生 replication 错觉\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R1-N2, R2 AGREE. §4.3 先报告 ρ=-0.762 和效应量再 qualify，容易让读者产生 replication 印象。Ridge 不解决共线性语义问题。Semipartial R²_BCS=0.056 仅 5.6% unique variance.\"}\n  action_items:\n    - {round: 31, action: \"§4.3 DocRED 段首句标注 VIF=50.9 + '仅供方向性参考'；详细数值移至 appendix；明确 ridge 局限性\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R31 DIVERGENT (1 item — reviewers disagree)\n# ============================================================\n\n- id: R31-D1\n  summary: \"SCS/BCS 相对于 LLM-PEE 的新颖性论证：metric 创新 vs 方法论创新之争\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R2-N2 Must-Fix: SCS 计算与 LLM-PEE 相同。R1 REBUT: 本文贡献是受控实验方法论（BCS-controlled batch + VIF + cluster bootstrap），不应以 metric 新颖性标准评判。双方各有道理，属评审视角差异。\"}\n  action_items:\n    - {round: 31, action: \"§2 更显式对比 LLM-PEE 的 uncontrolled 设计 vs 本文的 controlled study；明确定位为 empirical methodology 贡献\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R31 SHOULD-FIX (7 items — consensus)\n# ============================================================\n\n- id: R31-W1\n  summary: \"模型多样性不足：主实验仅 Qwen3-32B，cross-model 仅覆盖 count curves 和 BCS-accuracy\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R2-N1 Must-Fix, R1 AGREE 但建议降级 Should-Fix（4 模型 3 家族方向一致，一阶达领域惯例）。核心缺口：TOST、SDGD 无跨模型验证；缺闭源 frontier model。\"}\n  action_items:\n    - {round: 31, action: \"提升至少一个非 Qwen 模型为主分析，或严格限定 Section 6 claim 范围为 Qwen3-32B\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R31-W2\n  summary: \"TOST logit-scale 不通过仅在 Limitations 提及，主文 §4.4 未标注量表依赖性\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R1-W1, R2 AGREE. ±3pp 在 probability 和 logit scale 语义不同。影响 dimensional separability 结论强度。\"}\n  action_items:\n    - {round: 31, action: \"§4.4 factorial analysis 处直接标注量表依赖性（probability scale 通过，logit scale 不通过）\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R31-W3\n  summary: \"Extreme-BCS batch domain composition confound 未控制\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R1-W3, R2 AGREE 并补充。Appendix E.4 显示 low/high-BCS 有 domain 偏向，regression 未控制 domain diversity/entropy。\"}\n  action_items:\n    - {round: 31, action: \"做 domain-controlled regression 或 stratified analysis；将 domain entropy 作为 control variable\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R31-W4\n  summary: \"RQ3 (Schema Decomposition) Section 5 分析不充分：仅半栏，oracle routing 上限问题未讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R2-W2, R1 AGREE. Oracle routing 仅 72.4% vs single-type >85%，说明 decompose-then-merge 架构本身有结构性问题。应讨论 merge amplification 即使 routing 完美也无法避免。\"}\n  action_items:\n    - {round: 31, action: \"正文引用 Appendix B oracle routing 结果；讨论 merge amplification 根本问题；提及避免 merge 的替代架构\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R31-W5\n  summary: \"FP8 量化 non-determinism (SD=0.83pp) 占效应 18-44%，缺 power analysis\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R1-W5, R2 AGREE. Bootstrap CI 不区分信号与测量噪声。应讨论 noise floor 对 smallest detectable BCS slope 的影响。\"}\n  action_items:\n    - {round: 31, action: \"讨论 FP8 noise floor 对 regression detectable effect size 的影响\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R31-W6\n  summary: \"未解释方差讨论不足（FewRel 73% unexplained）+ Section 6 因果性语言\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R2-W1, R1 AGREE with nuance（27% semipartial R² 在 NLP 中属 large effect）。但应讨论 prompt formatting、type definition quality 等未解释因素。\"}\n  action_items:\n    - {round: 31, action: \"Discussion 列出可能的未解释因素；'captures structural property' 改为 'serves as a useful predictor of'\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R31-W7\n  summary: \"BCS 指标设计 mean aggregation 选择：Appendix I 有 mean vs max 但缺 top-k/加权方案\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R2-W3, R1 partial REBUT（Appendix I Table 15 已有 mean vs max，方向一致）。但 top-k/加权方案未探索。R1 建议在正文引用 Appendix I 结果。\"}\n  action_items:\n    - {round: 31, action: \"正文引用 Appendix I mean vs max 对比结果；讨论为什么均值优于（或不如）max\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R31 MINOR (7 items)\n# ============================================================\n\n- id: R31-M1\n  summary: \"NER U 形 count curve 非线性建模不足\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R2-W4, R1 AGREE. 应做 piecewise regression 或分段相关。\"}\n\n- id: R31-M2\n  summary: \"Missing references: PARSE (2025), ASEE (2025), Li et al. (2023), GenIE (2022)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R2-W5（GLiREL 已被引用，R1 correct）。R1 补充 Li 2023, GenIE 2022。PARSE/ASEE 待确认相关性。\"}\n\n- id: R31-M3\n  summary: \"Figure 1b 可读性不足（overlapping bars 在当前尺寸下难以准确读取）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"Both agree. 建议改用 grouped line chart 或增大尺寸。\"}\n\n- id: R31-M4\n  summary: \"Table 1 Few-NERD 'trigger mentions' 术语与 NER 不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"Both agree.\"}\n\n- id: R31-M5\n  summary: \"Type name 粒度差异对 SCS 跨数据集可比性影响未讨论\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"Both agree. Few-NERD fine-grained 66 types vs FewRel 80 relations 粒度差异影响 embedding similarity 分布。\"}\n\n- id: R31-M6\n  summary: \"Appendix N Monte Carlo ρ_pair=0.35 来源和 sensitivity 不清\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"Both agree. 应标注来源和 sensitivity analysis。\"}\n\n- id: R31-M7\n  summary: \"MiniLM vs Qwen3 embedding 机制讨论不足（哪个更接近 LLM 实际 confusability）\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R1-W4, R2 partial REBUT（MiniLM 作为 pre-deployment proxy 有合理性，Appendix I 方向一致）。但深层问题值得讨论。\"}\n\n# ============================================================\n# HISTORICAL (R29 issues — for cross-round tracking)\n# ============================================================\n# R29-C1 (BCS scope) → R31-C1 recurring\n# R29-C2 (DocRED VIF) → R31-C2 recurring\n# R29-W1 (SCS vs LLM-PEE) → R31-D1 recurring\n# R29-W2 (TOST scale) → R31-W2 recurring\n# R29-W3 (causal language) → partially addressed, subsumed by R31-C1\n# R29-W4 (domain confound) → R31-W3 recurring\n# R29-W5 (bootstrap CI) → addressed; new issue R31-W5 (FP8 noise)\n# R29-M1 ('first controlled study') → not raised in R31\n# R29-M2 (NER null framing) → R2 nuanced: IntraSub mechanism exists\n# R29-M3 (theoretical discussion) → not raised in R31\n# R29-M4 (SDGD compress) → R31-W4 (still insufficient)\n# R29-M5 (multiple comparisons) → not raised in R31\n# R29-M6 (missing refs) → R31-M2 (different refs)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "schema-dag-extraction",
    "issues_yaml": "\n# Review Issues Tracker\n# Updated: 2026-05-22 Round 31 (fresh review)\n\n# ============================================================\n# R31 CRITICAL (2 items — consensus)\n# ============================================================\n\n- id: R31-C1\n  summary: \"标题/摘要对 'Information Extraction' 的泛化声明超出证据支撑：confusability 独立预测效应仅在 FewRel RE 上干净成立\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R1-N1, R2 AGREE. NER null（Figure 2a IntraSub 机制存在但 accuracy 无效应）, MAVEN centrality confound, DocRED VIF=50.9 不可靠. Count-degradation 跨任务通用，但 confusability 独立效应仅 sentence-level RE.\"}\n  action_items:\n    - {round: 31, action: \"标题加 RE-specific 限定词或通用限定；摘要首段标注 task-specificity；区分 count（通用）和 confusability（RE-specific）的 generalizability\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R31-C2\n  summary: \"DocRED §4.3 VIF=50.9 下 partial correlation 呈现顺序产生 replication 错觉\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R1-N2, R2 AGREE. §4.3 先报告 ρ=-0.762 和效应量再 qualify，容易让读者产生 replication 印象。Ridge 不解决共线性语义问题。Semipartial R²_BCS=0.056 仅 5.6% unique variance.\"}\n  action_items:\n    - {round: 31, action: \"§4.3 DocRED 段首句标注 VIF=50.9 + '仅供方向性参考'；详细数值移至 appendix；明确 ridge 局限性\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R31 DIVERGENT (1 item — reviewers disagree)\n# ============================================================\n\n- id: R31-D1\n  summary: \"SCS/BCS 相对于 LLM-PEE 的新颖性论证：metric 创新 vs 方法论创新之争\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R2-N2 Must-Fix: SCS 计算与 LLM-PEE 相同。R1 REBUT: 本文贡献是受控实验方法论（BCS-controlled batch + VIF + cluster bootstrap），不应以 metric 新颖性标准评判。双方各有道理，属评审视角差异。\"}\n  action_items:\n    - {round: 31, action: \"§2 更显式对比 LLM-PEE 的 uncontrolled 设计 vs 本文的 controlled study；明确定位为 empirical methodology 贡献\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R31 SHOULD-FIX (7 items — consensus)\n# ============================================================\n\n- id: R31-W1\n  summary: \"模型多样性不足：主实验仅 Qwen3-32B，cross-model 仅覆盖 count curves 和 BCS-accuracy\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R2-N1 Must-Fix, R1 AGREE 但建议降级 Should-Fix（4 模型 3 家族方向一致，一阶达领域惯例）。核心缺口：TOST、SDGD 无跨模型验证；缺闭源 frontier model。\"}\n  action_items:\n    - {round: 31, action: \"提升至少一个非 Qwen 模型为主分析，或严格限定 Section 6 claim 范围为 Qwen3-32B\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R31-W2\n  summary: \"TOST logit-scale 不通过仅在 Limitations 提及，主文 §4.4 未标注量表依赖性\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R1-W1, R2 AGREE. ±3pp 在 probability 和 logit scale 语义不同。影响 dimensional separability 结论强度。\"}\n  action_items:\n    - {round: 31, action: \"§4.4 factorial analysis 处直接标注量表依赖性（probability scale 通过，logit scale 不通过）\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R31-W3\n  summary: \"Extreme-BCS batch domain composition confound 未控制\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R1-W3, R2 AGREE 并补充。Appendix E.4 显示 low/high-BCS 有 domain 偏向，regression 未控制 domain diversity/entropy。\"}\n  action_items:\n    - {round: 31, action: \"做 domain-controlled regression 或 stratified analysis；将 domain entropy 作为 control variable\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R31-W4\n  summary: \"RQ3 (Schema Decomposition) Section 5 分析不充分：仅半栏，oracle routing 上限问题未讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R2-W2, R1 AGREE. Oracle routing 仅 72.4% vs single-type >85%，说明 decompose-then-merge 架构本身有结构性问题。应讨论 merge amplification 即使 routing 完美也无法避免。\"}\n  action_items:\n    - {round: 31, action: \"正文引用 Appendix B oracle routing 结果；讨论 merge amplification 根本问题；提及避免 merge 的替代架构\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R31-W5\n  summary: \"FP8 量化 non-determinism (SD=0.83pp) 占效应 18-44%，缺 power analysis\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R1-W5, R2 AGREE. Bootstrap CI 不区分信号与测量噪声。应讨论 noise floor 对 smallest detectable BCS slope 的影响。\"}\n  action_items:\n    - {round: 31, action: \"讨论 FP8 noise floor 对 regression detectable effect size 的影响\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R31-W6\n  summary: \"未解释方差讨论不足（FewRel 73% unexplained）+ Section 6 因果性语言\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R2-W1, R1 AGREE with nuance（27% semipartial R² 在 NLP 中属 large effect）。但应讨论 prompt formatting、type definition quality 等未解释因素。\"}\n  action_items:\n    - {round: 31, action: \"Discussion 列出可能的未解释因素；'captures structural property' 改为 'serves as a useful predictor of'\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R31-W7\n  summary: \"BCS 指标设计 mean aggregation 选择：Appendix I 有 mean vs max 但缺 top-k/加权方案\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R2-W3, R1 partial REBUT（Appendix I Table 15 已有 mean vs max，方向一致）。但 top-k/加权方案未探索。R1 建议在正文引用 Appendix I 结果。\"}\n  action_items:\n    - {round: 31, action: \"正文引用 Appendix I mean vs max 对比结果；讨论为什么均值优于（或不如）max\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R31 MINOR (7 items)\n# ============================================================\n\n- id: R31-M1\n  summary: \"NER U 形 count curve 非线性建模不足\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R2-W4, R1 AGREE. 应做 piecewise regression 或分段相关。\"}\n\n- id: R31-M2\n  summary: \"Missing references: PARSE (2025), ASEE (2025), Li et al. (2023), GenIE (2022)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R2-W5（GLiREL 已被引用，R1 correct）。R1 补充 Li 2023, GenIE 2022。PARSE/ASEE 待确认相关性。\"}\n\n- id: R31-M3\n  summary: \"Figure 1b 可读性不足（overlapping bars 在当前尺寸下难以准确读取）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"Both agree. 建议改用 grouped line chart 或增大尺寸。\"}\n\n- id: R31-M4\n  summary: \"Table 1 Few-NERD 'trigger mentions' 术语与 NER 不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"Both agree.\"}\n\n- id: R31-M5\n  summary: \"Type name 粒度差异对 SCS 跨数据集可比性影响未讨论\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"Both agree. Few-NERD fine-grained 66 types vs FewRel 80 relations 粒度差异影响 embedding similarity 分布。\"}\n\n- id: R31-M6\n  summary: \"Appendix N Monte Carlo ρ_pair=0.35 来源和 sensitivity 不清\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"Both agree. 应标注来源和 sensitivity analysis。\"}\n\n- id: R31-M7\n  summary: \"MiniLM vs Qwen3 embedding 机制讨论不足（哪个更接近 LLM 实际 confusability）\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 31\n  last_seen_round: 31\n  mentions:\n    - {round: 31, reviewers: [R1, R2], note: \"R1-W4, R2 partial REBUT（MiniLM 作为 pre-deployment proxy 有合理性，Appendix I 方向一致）。但深层问题值得讨论。\"}\n\n# ============================================================\n# HISTORICAL (R29 issues — for cross-round tracking)\n# ============================================================\n# R29-C1 (BCS scope) → R31-C1 recurring\n# R29-C2 (DocRED VIF) → R31-C2 recurring\n# R29-W1 (SCS vs LLM-PEE) → R31-D1 recurring\n# R29-W2 (TOST scale) → R31-W2 recurring\n# R29-W3 (causal language) → partially addressed, subsumed by R31-C1\n# R29-W4 (domain confound) → R31-W3 recurring\n# R29-W5 (bootstrap CI) → addressed; new issue R31-W5 (FP8 noise)\n# R29-M1 ('first controlled study') → not raised in R31\n# R29-M2 (NER null framing) → R2 nuanced: IntraSub mechanism exists\n# R29-M3 (theoretical discussion) → not raised in R31\n# R29-M4 (SDGD compress) → R31-W4 (still insufficient)\n# R29-M5 (multiple comparisons) → not raised in R31\n# R29-M6 (missing refs) → R31-M2 (different refs)\n"
  }
}
```

</details>

---


### Tool result

_source line 3115 · 2026-05-22T23:09:36.525278+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml\", \"bytes\": 9313}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 50
}
```

</details>

---
