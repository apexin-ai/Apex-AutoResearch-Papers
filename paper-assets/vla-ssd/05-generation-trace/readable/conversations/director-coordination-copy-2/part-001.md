# Director coordination — Part 1 of 5

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

[Transcript overview](../director-coordination-copy-2.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/55/55aa43168feffca83e03.json)

## Round 1

## Round 1

64 recorded events


### User

_source line 1 · 2026-05-17T04:29:05.387765+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: vla-ssd
- 论文路径: projects/vla-ssd/docs/paper/main.tex
- 目标 venue: CoRL 2026
- 截止日期: 2026-05-29

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-17T04:29:11.317118+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3 · 2026-05-17T04:29:11.368295+00:00_

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
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-17T04:29:15.044522+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 5 · 2026-05-17T04:29:15.045085+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-17T04:29:18.310204+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-17T04:29:19.264536+00:00_

{"result":"# 项目 vla-ssd 概况\n\n## 实验状态 (64 个)\n\n- **lg_extract_untrained_r2**: DONE (killed) — \n- **lg_extract_trained_r2**: DONE (killed) — \n- **lg_extract_untrained_r1**: DONE (killed) — \n- **lg_extract_trained_r1**: DONE (killed) — \n- **mvp2_delta_dino**: DONE (success) — \n- **mvp2_delta_untrained**: DONE (success) — \n- **mvp2_delta_trained**: DONE (success) — \n- **mvp2_action_dino**: DONE (success) — \n- **mvp2_action_untrained**: DONE (success) — \n- **mvp2_action_trained**: DONE (success) — \n- **mvp_controlb_untrained**: DONE (success) — \n- **mvp_controlb_trained**: DONE (success) — \n- **mvp_001**: DONE (negative) — \n- **mvp_probe_untrained**: DONE (success) — \n- **mvp_probe_trained**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- ablation_p2_demo_sensitivity: Demo count sensitivity: subsample 25 from 50 demos/task, rerun RSA + probe on trained_image_mean (33 layers). Tests whether inverted-U pattern is stable under reduced data.（准备中）\n- plan010_action_probe_spatial（准备中）\n- plan010_rsa_spatial（准备中）\n- fulllayer_action_probe（准备中）\n\n## 近期结论\n- **qa_probe_classification** (success): QA Probe: Test whether VLA LLM layers encode high-level task understanding (progress/subtask classification), not just low-level action prediction. If trained deep layers >> DINO/Projector on progress classification, LLM training provides semantic understanding. If DINO matches, vision encoder already encodes this information.\n- **cross_inst_extract_untrained** (success): Untrained VLA baseline: without task-specific training, instruction-conditioned features should show minimal instruction encoding (near chance-level 10% accuracy)\n- **cross_inst_extract_trained** (success): Trained VLA features encode instruction identity: same frame with different instructions should produce distinguishable representations, especially in mid-to-late layers where action planning occurs\n\n## 趋势\n成功 45 / 负向 7 / 失
…[truncated 429 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-17T04:29:19.415593+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-17T04:29:19.466215+00:00_

1	\documentclass{article}
2	
3	\usepackage{corl_2026}
4	
5	\usepackage[utf8]{inputenc}
6	\usepackage[T1]{fontenc}
7	\usepackage{url}
8	\usepackage{booktabs}
9	\usepackage{amsfonts}
10	\usepackage{amsmath}
11	\usepackage{nicefrac}
12	\usepackage[expansion=false]{microtype}
13	\usepackage{graphicx}
14	\usepackage{enumitem}
15	
16	\title{Vision Encodes, Language Routes:\\ A Representational Decomposition of Vision-Language-Action Models}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	
22	\maketitle
23	
24	\begin{abstract}
25	\input{abstract}
26	\end{abstract}
27	
28	\input{introduction}
29	\input{related_work}
30	\input{method}
31	\input{experiments}
32	\input{discussion}
33	\input{conclusion}
34	
35	\bibliography{references}
36	
37	\input{appendix}
38	
39	\end{document}
40	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-17T04:29:26.799898+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-17T04:29:26.800322+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-17T04:29:30.214261+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 call for papers submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 13 · 2026-05-17T04:29:30.716546+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 14 · 2026-05-17T04:29:30.767189+00:00_

1	Vision-language-action models (VLAs) fine-tune large language models (LLMs) on robot demonstrations, but how they internally process multimodal information at the token level remains unknown.
2	We perform the first token-level representational decomposition of a VLA (OpenVLA-7B on LIBERO), combining cross-instruction probes, attention analysis, Representational Similarity Analysis (RSA), and functional probes across all 32 LLM layers.
3	Three findings emerge.
4	First, the VLA exhibits strict token-level functional specialization: image tokens encode purely visual information (instruction classification at chance, $10\%$, across all layers), while the readout token serves as a multimodal convergence point ($100\%$ instruction classification from L1, LOOCV-verified).
5	Second, training learns deliberate instruction routing: at L1, 25/32 attention heads flip to instruction-dominant ($58\%$ attention to ${\sim}8\%$ of the sequence), creating a robust signal maintained through L31 ($100\%$), whereas untrained incidental routing decays to $82\%$.
6	Third, the LLM applies a non-monotonic refinement of vision encoder geometry: RSA peaks at L12, probe $R^2$ peaks at L8--L13, with self-supervised DINOv2 providing the highest geometric foundation ($\rho = 0.692$, exceeding all internal representations).
7	These results reveal that VLAs maintain a strict division of labor between visual and multimodal tokens, with training primarily reshaping readout-token information integration (routing $+18$pp, attention $+46$pp) rather than visual representations ($\Delta \leq 1.7\%$).
8	VLA architectures should optimize routing from image tokens to the readout position; vision encoder quality is the primary design lever.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 15 · 2026-05-17T04:29:31.169298+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 16 · 2026-05-17T04:29:31.220028+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Vision-language-action models (VLAs) process visual observations and language instructions through a large language model to produce robot actions~\cite{brohan2023_rt2,kim2024_openvla}.
5	A central but untested assumption is that all token types within the LLM contribute uniformly to action prediction.
6	Understanding the token-level division of labor is essential for designing efficient VLA architectures: if image tokens and readout tokens serve fundamentally different roles, then design choices (attention patterns, layer selection, action head placement) should reflect this specialization.
7	
8	Recent behavioral studies reveal that VLAs rely disproportionately on visual input~\cite{grant2026}, with language instructions largely ignored by the action pathway~\cite{haon2025}.
9	These findings hint at internal specialization but do not explain \emph{how} information is routed within the LLM, \emph{where} instruction identity is encoded, or \emph{what} training changes at the representational level.
10	No prior work has provided a systematic token-level decomposition of a VLA, leaving open whether image tokens carry instruction information, whether the readout token functions as a multimodal hub, and whether training creates new representational structure or reconfigures inherited geometry.
11	
12	We address this gap by decomposing OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a VLA chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2}, an MLP projector, and Llama-2 7B.
13	We extract representations from each of 32 LLM layers at both image-token and readout-token positions, and from external baselines (DINOv2~\cite{oquab2024_dinov2}, CLIP~\cite{radford2021_clip}).
14	We cross training status (trained vs.\ untrained, reinitializing 6.74B LLM parameters) with instruction presence in a $2\times 2$ factorial design, and apply four complementary analyses: cross-instruction probes fo
…[truncated 2184 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-17T04:29:37.494968+00:00_

Web search results for query: "CoRL 2026 call for papers submission guidelines author instructions"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 - Instruction for Presentations","url":"https://www.corl.org/contributions/instruction-for-presentations"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"ICML 2026 Author Instructions","url":"https://icml.cc/Conferences/2026/AuthorInstructions"}]

I found the CoRL 2026 submission guidelines and author instructions. Here's a summary of the key information:

## Paper Format and Structure

The camera-ready paper should follow the template: 8-page main text + acknowledgment + references + appendix (optional).

## Key Requirements

**Limitations Section:** All submissions should include a Limitations section (counted toward the 8-page limit), explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments, and how these might be addressed in the future.

**Reproducibility:** Authors are strongly encouraged to include all relevant details in the main paper and the appendix to ensure that future researchers can reproduce the methodology and results.

## Submission Content

Submissions should focus on a core
…[truncated 934 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "WebSearch",
  "elapsed_ms": 7280
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-17T04:29:41.818006+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 submission deadline page limit double blind review"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 submission deadline page limit double blind review"
  }
}
```

</details>

---


### Tool call

_source line 19 · 2026-05-17T04:29:42.270385+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 20 · 2026-05-17T04:29:42.482442+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We investigate how action-relevant structure is distributed across a VLA by combining four complementary analyses: cross-instruction probes, attention pattern analysis, RSA, and functional probes.
5	
6	%------------------------------------------------------------------
7	\subsection{Model and Data}
8	\label{sec:model_data}
9	
10	We study OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a generalist robot policy chaining three components: a frozen DinoSigLIP fused vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\to$ 4{,}096-D), and a Llama-2 7B language backbone (6.74B parameters) that autoregressively decodes 7-dimensional actions.
11	We use the base checkpoint pretrained on Open X-Embodiment (no task-specific fine-tuning) and evaluate on LIBERO-Goal~\cite{liu2023_libero} (10 tabletop tasks, 50 demonstrations each).
12	To isolate the LLM's contribution, we construct an untrained control by reinitializing all LLM parameters via \texttt{from\_config()} (6.74B random weights), preserving the frozen vision encoder and projector architecture.
13	
14	%------------------------------------------------------------------
15	\subsection{Representation Extraction}
16	\label{sec:repr_extraction}
17	
18	We extract representations from six sources spanning the VLA pipeline:
19	(a)~\textbf{DinoSigLIP+Projector}---projector output (4{,}096-D), immediately before LLM processing;
20	(b)~\textbf{LLM image\_mean}---mean image-token activation at each of 32 layers;
21	(c)~\textbf{LLM readout}---activation at the final pre-action token position at each layer;
22	(d)~\textbf{DINOv2 ViT-L/14}~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}), a self-supervised baseline;
23	(e)~\textbf{CLIP ViT-L/14}~\cite{radford2021_clip} (\texttt{patch\_mean}), a VL-pretrained baseline;
24	(f)~\textbf{Branch-split}---DINOv2 (1{,}024-D) and SigLIP (1{,}152-D) branches befor
…[truncated 2931 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 212
}
```

</details>

---


### Tool call

_source line 21 · 2026-05-17T04:29:42.482790+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 22 · 2026-05-17T04:29:42.533391+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We evaluate OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024} on LIBERO-Goal~\cite{liu2023_libero} (10 tasks, 50 demonstrations each).
8	Representations are extracted from six sources spanning the VLA pipeline (\S\ref{sec:repr_extraction}): DinoSigLIP+Projector, LLM image\_mean and readout tokens at each of 32 layers, DINOv2~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}), CLIP~\cite{radford2021_clip} (\texttt{patch\_mean}), and branch-split (DINOv2 1{,}024-D / SigLIP 1{,}152-D before fusion).
9	The $2\times 2$ factorial design crosses training status (trained vs.\ untrained LLM, reinitializing 6.74B parameters) with instruction presence (\S\ref{sec:model_data}).
10	RSA computes Spearman $\rho$ between cosine-distance representation RDMs and Euclidean-distance action RDMs, with 10{,}000 bootstrap CIs (\S\ref{sec:rsa}).
11	MLP probes (input $\to$ 256 $\to$ 7; Adam, lr${}=10^{-3}$, 50 epochs, early stopping) report mean $R^2$ (\S\ref{sec:probes}).
12	
13	%------------------------------------------------------------------
14	\subsection{Token-Level Functional Specialization}
15	\label{sec:token_specialization}
16	
17	We test whether image tokens and readout tokens encode different types of information by training cross-instruction probes (\S\ref{sec:cross_instruction_probes}): given the same visual frame paired with each of 10 task instructions, we classify which instruction was present from per-layer activations.
18	
19	\paragraph{Image tokens are instruction-blind.}
20	At the image\_mean position, instruction classification remains at chance ($10\%$) across all 32 layers, in both trained and untrained models (Table~\ref{tab:dense_routing_main}).
21	This result holds identically for standalone DINOv2 \texttt{cls\_token} ($10\%$), confirming that instruction blindness is a property of the visual representation itself, not an artifact of the 
…[truncated 12619 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-17T04:29:46.802787+00:00_

Web search results for query: "CoRL 2026 submission deadline page limit double blind review"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"ICWSM 2026: Submit","url":"https://www.icwsm.org/2026/submit.html"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"ICML 2026: Strictest New Rules Ever - LLMs Banned as Authors, Papers with AI Abuse Rejected","url":"https://eu.36kr.com/en/p/3540848514510723"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf?lang=en"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"}]

Based on the search results, here's the information about CoRL 2026 submission details:

**Submission Deadline:**
The paper submission deadline is Thursday (5/28) EOD rather than Friday, with an abstract submission deadline of May 25.

**Page Limit:**
The initial submission is 8 pages, with an additional 9th page for camera-ready submissions to incorporate reviewer feedback.

**Double-Blind Review:**
CoRL is double-blind, which means all papers must be anonymized.

**Reciprocal Review Requirement:**
Every author with 3 or more submissions must agree to serve as a reviewer, though authors are exempt from the review requirement if they serve as an AC, an SAC, or another organizing chair for CoRL 2026.

For more detailed information, you can visit the CoRL 2026 Instructions for Authors page at http
…[truncated 158 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "WebSearch",
  "elapsed_ms": 4984
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-17T04:29:52.145842+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-17T04:29:52.598405+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Synthesis.}
5	Our experiments reveal a coherent picture of token-level information processing in a VLA.
6	Image tokens maintain purely visual representations throughout all 32 LLM layers, never encoding instruction identity.
7	The readout token serves as the sole multimodal convergence point, integrating instruction information through a learned attention-based routing mechanism: training flips 25/32 L1 heads to instruction-dominant, creating a robust signal that survives the full depth of the network.
8	The LLM transforms the vision encoder's geometric foundation non-monotonically, with early-to-middle layers (L8--L13) containing the most action-relevant representations.
9	
10	\paragraph{Token specialization and routing.}
11	The strict division of labor between image and readout tokens suggests that the LLM does not blend modalities uniformly across token types.
12	Instead, visual information flows through image tokens while the readout token selectively attends to instruction tokens, with training creating a fundamentally different attention strategy (58\% deliberate routing vs.\ 12\% incidental leakage).
13	Training effects concentrate at the readout token (routing $+18$pp, attention $+46$pp, $R^2$ $+0.069$) while leaving image representations largely unchanged ($\Delta \leq 1.7\%$; Appendix~\ref{sec:training_effect_summary}).
14	
15	\paragraph{RSA--$R^2$ peak offset.}
16	The $R^2$ plateau (L8--L16) encompasses and partially precedes the RSA peak (L12), indicating that maximal geometric alignment does not coincide with maximal decodability.
17	Training causes these peaks to converge on LIBERO-Goal (RSA L12, $R^2$ L13) but not on LIBERO-Spatial (6-layer gap), suggesting benchmark-specific alignment.
18	
19	\paragraph{Implications for VLA design.}
20	Three practical considerations emerge.
21	\emph{First}, vision encoder pretraining quality is the primary design lever; investing in stronger self-supervi
…[truncated 1364 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-17T04:29:52.699562+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-17T04:29:53.001137+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We present the first token-level representational decomposition of a VLA, revealing three aspects of internal information processing.
5	(1)~Strict functional specialization: image tokens encode purely visual information (instruction classification at chance across all layers), while the readout token is the sole multimodal convergence point ($100\%$ instruction classification from L1, LOOCV-verified).
6	(2)~Training learns deliberate instruction routing: 25/32 L1 attention heads flip to instruction-dominant ($58\%$ attention to ${\sim}8\%$ of the sequence), creating a robust signal maintained through L31, whereas untrained incidental routing decays to $82\%$.
7	(3)~The LLM non-monotonically refines vision encoder geometry (RSA inverted-U peaking at L12, $R^2$ at L8--L13), with self-supervised DINOv2 providing the highest geometric foundation ($\rho = 0.692$) and training primarily reshaping readout-token integration ($R^2$ $+0.069$) rather than visual representations ($\Delta \leq 1.7\%$).
8	These results suggest that VLA architectures should optimize routing from image tokens to the readout position, and that vision encoder quality is the primary design lever.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-17T04:29:53.001656+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-17T04:29:53.053241+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Vision-language-action models.}
4	VLAs fine-tune LLMs on robot demonstrations~\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024}, assuming fine-tuning injects action-relevant knowledge.
5	We test this assumption at the representational level.
6	
7	\paragraph{Behavioral and mechanistic analysis.}
8	Behavioral studies show VLAs rely disproportionately on visual input, with language instructions largely ignored~\cite{grant2026,hou2026,fei2025}.
9	Mechanistic work has identified sparse semantic directions linked to action selection~\cite{haon2025}, memorized sequences via sparse autoencoders~\cite{swann2026,buurmeijer2026}, and probed for symbolic states and world models~\cite{lu2025,molinari2025}.
10	\cite{fang2025} showed fine-tuning erodes VLM reasoning.
11	These studies analyze individual components; we provide a systematic per-layer decomposition with trained-vs-untrained controls absent from prior work, revealing a non-monotonic transformation profile invisible to whole-model analyses.
12	
13	\paragraph{Representation analysis.}
14	We adopt RSA~\cite{kriegeskorte2008} and MLP probes~\cite{alain2017,belinkov2022} as geometric and functional metrics, with CKA~\cite{kornblith2019} in the appendix.
15	We compare self-supervised (DINOv2~\cite{oquab2024_dinov2}), VL-pretrained (CLIP~\cite{radford2021_clip}), and fused (DinoSigLIP~\cite{zhai2023_siglip}) encoders at matched ViT-L/14 scale to test whether language grounding contributes to action-relevant structure.
16	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-17T04:29:57.774258+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 31 · 2026-05-17T04:29:58.126197+00:00_

1	\appendix
2	
3	\section{Supplementary Material}
4	\label{sec:appendix}
5	
6	\subsection{CKA Analysis Method}
7	\label{sec:cka_appendix}
8	
9	We employ Centered Kernel Alignment (CKA)~\cite{kornblith2019} alongside RSA as a complementary perspective.
10	While RSA captures local geometric alignment via rank-order preservation, CKA measures global representational similarity through kernel-based comparisons.
11	
12	We compute both \emph{linear CKA}, which uses a linear kernel and is sensitive to second-order statistics, and \emph{RDM kernel CKA}, which operates on the same distance matrices as RSA but aggregates them differently.
13	Using both variants tests whether conclusions about representation structure are robust to the choice of similarity metric.
14	
15	Linear CKA between high-dimensional representations (4{,}096-D for LLM layers) and the 7-D action space is subject to a known dimension mismatch: the linear kernel in the low-dimensional space may not capture the same structure as in the high-dimensional space.
16	RDM kernel CKA avoids this issue by operating on distance matrices of equal size regardless of the original feature dimensionality.
17	
18	\subsection{Metric Sensitivity: RSA versus CKA}
19	\label{sec:metric_sensitivity_appendix}
20	
21	Linear CKA~\cite{kornblith2019} reverses the RSA ordering: untrained LLM ($\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially inverting the self-supervised advantage (Figure~\ref{fig:metric_comparison}).
22	RDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $\approx$ Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).
23	This divergence reflects the known sensitivity of representation similarity metrics to different geometric properties.
24	
25	At the per-layer level, linear CKA between image\_mean and the action space rises monotonically from L0 ($0.081$) to L32 ($0.098$), showing no inverted-U pattern.
26	RSA captures ran
…[truncated 13031 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-17T04:29:58.327353+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "literature_map.yaml",
  "max_chars": "6000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "literature_map.yaml",
    "max_chars": "6000"
  }
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-17T04:29:58.378153+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/literature_map.yaml\", \"content\": \"papers:\\n  # ============================================================\\n  # DIRECT COMPETITORS — VLA Representation Analysis / Interpretability\\n  # ============================================================\\n  - id: grant2026\\n    title: \\\"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models\\\"\\n    authors: \\\"Bryce Grant, Xijia Zhao, Peng Wang\\\"\\n    year: 2026\\n    venue: \\\"arXiv preprint (under review)\\\"\\n    arxiv_id: \\\"2603.19233\\\"\\n    category: direct-competitor\\n    role: competitor\\n    key_findings: >\\n      Visual pathway dominates action generation across all 6 tested VLA architectures (80M–7B params, 394K+ rollout episodes, 4 benchmarks).\\n      Language sensitivity depends on task structure: when visual context uniquely specifies the task, language is IGNORED;\\n      when multiple goals share a scene, language becomes essential (\\\"encoded but not used\\\").\\n      Cross-task activation injection steers robots toward source-task positions (99.8% trajectory alignment with source in X-VLA).\\n      Multi-pathway architectures (pi0.5, SmolVLA, GR00T) separate motor programs (expert pathway) from goal semantics (VLM pathway).\\n    relevance_to_us: >\\n      Most direct competitor. Behavioral intervention (activation injection, SAE, probing) reveals vision dominance + language encoded but not used.\\n      Uses OpenVLA-OFT checkpoint; we use standard fine-tuning — must qualify this difference in Related Work.\\n    novelty_gap: >\\n      No trained vs untrained representation analysis. They compare different model architectures,\\n      we compare trained vs untrained representation structure within the same architecture.\\n      Their \\\"encoded but not used\\\" is a behavioral-level conclusion; we demonstrate at the represent
…[truncated 4648 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-17T04:30:02.544872+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
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

_source line 35 · 2026-05-17T04:30:02.545344+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-17T04:30:06.621344+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-17T04:30:06.672120+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-17T04:30:07.224771+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 39 · 2026-05-17T04:30:07.526593+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 40 · 2026-05-17T04:30:10.540713+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 41 · 2026-05-17T04:30:10.992797+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-17T04:30:11.043557+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/agent"
  }
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-17T04:30:11.194668+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/agent. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/sessions/review_director_ae8c68a6.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-17T04:30:14.875279+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -20",
  "description": "Find YAML config files in project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -20",
    "description": "Find YAML config files in project"
  }
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-17T04:30:15.026246+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260516T011810/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260516T011810/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd
…[truncated 338 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-17T04:30:21.705231+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15",
  "output_mode": "files_with_matches",
  "head_limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15",
    "output_mode": "files_with_matches",
    "head_limit": "10"
  }
}
```

</details>

---


### Tool result

_source line 47 · 2026-05-17T04:30:21.806086+00:00_

Found 6 files
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/logs/chats/feishu_group_oc_554a5023cde4d603635cf97e6ab8151a_director.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/global/logs/system.log
AGENTS.md
CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/logs/chats/worker_code_sync_figures_local_20260516T081324.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/logs/workers/worker_code_sync_figures_local_20260516T081324.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-17T04:30:25.119467+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/CLAUDE.md",
  "output_mode": "content",
  "context": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/CLAUDE.md",
    "output_mode": "content",
    "context": "3"
  }
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-17T04:30:25.170096+00:00_

&lt;tool_use_error>Path does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/CLAUDE.md. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/sessions/review_director_ae8c68a6.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-17T04:30:28.985603+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15",
  "glob": "CLAUDE.md",
  "output_mode": "content",
  "context": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15",
    "glob": "CLAUDE.md",
    "output_mode": "content",
    "context": "2"
  }
}
```

</details>

---


### Tool result

_source line 51 · 2026-05-17T04:30:29.086694+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/sessions/review_director_ae8c68a6/CLAUDE.md-80-## 外部审稿线（Stanford Agentic Reviewer）
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/sessions/review_director_ae8c68a6/CLAUDE.md-81-
CLAUDE.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
CLAUDE.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/sessions/review_director_ae8c68a6/CLAUDE.md-84-- **不阻塞内部审稿**——内部圆桌照常进行，外部结果异步到达
CLAUDE.md-85-- 用户在群里粘贴 paperreview.ai 审稿结果后，将其作为 `[外部审稿: Stanford Agentic Reviewer]` 纳入最终报告的独立 section
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/sessions/review_director_ae8c68a6/CLAUDE.md-86-- 特别关注：外部 review 发现但内部 reviewer 遗漏的 related work 和 weakness
CLAUDE.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/sessions/review_director_ae8c68a6/CLAUDE.md-88-
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/sessions/review_director_ae8c68a6/CLAUDE.md-89-## 隔离规则（严格执行）
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/sessions/review_director_ae8c68a6/CLAUDE.md-149-你可以使用以下 9 个 MCP 工具，直接调用即可，不需要搜索：
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/sessions/review_director_ae8c68a6/CLAUDE.md-150-
CLAUDE.md:151:`director_get_project_overview`, `director_post_to_reviewer`, `get_external_review_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/sessions/review_director_ae8c68a6/CLAUDE.md-152-
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/sessions/review_director_ae8c68a6/CLAUDE.md
…[truncated 36 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Grep",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 52 · 2026-05-17T04:30:34.509186+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/constraints.yaml",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/constraints.yaml",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-17T04:30:34.559872+00:00_

1	_next_id: 2
2	constraints:
3	- id: C001
4	  added: 2026-05-15 19:40 UTC
5	  summary: Goal classification 实验必须 trained + untrained 对照数据齐全后才写 conclusion。单臂数据只记数字，禁止下结论。
6	  scope: all
7	  reason: Agent 两次在缺少 untrained 对照时错误归因（memory.md "language grounding" + lg_gc_trained_frame0
8	    "instruction integration"），均被 Reviewer CRITICAL 打回。
9	  decision_id: D018
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 54 · 2026-05-17T04:30:52.298626+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-17T04:30:52.349257+00:00_

1	% === VLA / Architecture ===
2	
3	@article{kim2024_openvla,
4	  title     = {{OpenVLA}: An Open-Source Vision-Language-Action Model},
5	  author    = {Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balakrishna, Ashwin and Nair, Suraj and Rafailov, Rafael and Foster, Ethan and Lam, Grace and Sanketi, Pannag and Lu, Quan and Kollar, Thomas and Burchfiel, Benjamin and Tedrake, Russ and Sadigh, Dorsa and Levine, Sergey and Liang, Percy and Finn, Chelsea},
6	  journal   = {arXiv preprint arXiv:2406.09246},
7	  year      = {2024},
8	}
9	
10	@article{karamcheti2024,
11	  title     = {Prismatic {VLMs}: Investigating the Design Space of Visually-Conditioned Language Models},
12	  author    = {Karamcheti, Siddharth and Nair, Suraj and Balakrishna, Ashwin and Liang, Percy and Kollar, Thomas and Sadigh, Dorsa},
13	  journal   = {arXiv preprint arXiv:2402.07865},
14	  year      = {2024},
15	}
16	
17	@article{brohan2023_rt2,
18	  title     = {{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
19	  author    = {Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},
20	  journal   = {arXiv preprint arXiv:2307.15818},
21	  year      = {2023},
22	}
23	
24	% === Benchmark ===
25	
26	@inproceedings{liu2023_libero,
27	  title     = {{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
28	  author    = {Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},
29	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
30	  year      = {2023},
31	}
32	
33	% === Representation Analysis Methods ===
34	
35	@article{kriegeskorte2008,
36	  title     = {Representational Similarity Analysis -- Connecting the Branches of Systems Neuroscience},
37	  author    = {Kriegeskorte, Nikolaus and Mur, Marieke and Ban
…[truncated 2645 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 56 · 2026-05-17T04:30:56.165395+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
  "offset": "100",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
    "offset": "100",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 57 · 2026-05-17T04:30:56.165843+00:00_

100	@article{hou2026,
101	  title     = {{LangGap}: Diagnosing and Closing the Language Gap in Vision-Language-Action Models},
102	  author    = {Hou, Yuchen and Zhao, Lin},
103	  journal   = {arXiv preprint arXiv:2603.00592},
104	  year      = {2026},
105	}
106	
107	@article{fei2025,
108	  title     = {{LIBERO-Plus}: In-depth Robustness Analysis of Vision-Language-Action Models},
109	  author    = {Fei, Senyu and Wang, Siyin and Shi, Junhao and Dai, Zihao and Cai, Jikun and Qian, Pengfang and Ji, Li and He, Xinzhe and Zhang, Shiduo and Fei, Zhaoye and Fu, Jinlan and Gong, Jingjing and Qiu, Xipeng},
110	  journal   = {arXiv preprint arXiv:2510.13626},
111	  year      = {2025},
112	}
113	
114	% === Mechanistic Interpretability of VLAs ===
115	
116	@article{swann2026,
117	  title     = {Sparse Autoencoders Reveal Interpretable and Steerable Features in {VLA} Models},
118	  author    = {Swann, Aiden and McGranahan, Lachlain and Buurmeijer, Hugo and Kennedy, Monroe and Schwager, Mac},
119	  journal   = {arXiv preprint arXiv:2603.19183},
120	  year      = {2026},
121	}
122	
123	@article{buurmeijer2026,
124	  title     = {Observing and Controlling Features in Vision-Language-Action Models},
125	  author    = {Buurmeijer, Hugo and Amo Alonso, Carmen and Swann, Aiden and Pavone, Marco},
126	  journal   = {arXiv preprint arXiv:2603.05487},
127	  year      = {2026},
128	}
129	
130	@article{lu2025,
131	  title     = {Probing a Vision-Language-Action Model for Symbolic States and Integration into a Cognitive Architecture},
132	  author    = {Lu, Hong and Li, Hengxu and Shahani, Prithviraj Singh and Herbers, Stephanie and Scheutz, Matthias},
133	  journal   = {arXiv preprint arXiv:2502.04558},
134	  year      = {2025},
135	}
136	
137	@article{molinari2025,
138	  title     = {Emergent World Representations in {OpenVLA}},
139	  author    = {Molinari, Marco and Nevali, Leonardo and Navani, Saharsha and Younis, Omar G.},
140	  journal   = {arXiv preprint arXiv:2509.24559},
141	  yea
…[truncated 1535 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-17T04:31:33.728722+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验有效性）\n\n### Venue 信息\n- **目标会议**: CoRL 2026\n- **截止日期**: 2026-05-28（论文）\n- **页数限制**: 8 页正文 + references + appendix\n- **模板**: corl_2026（已正确使用）\n- **匿名规则**: double-blind\n- **特殊要求**: 必须含 Limitations section（计入 8 页），需论证 robotics relevance\n\n### 论文路径\n`projects/vla-ssd/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, appendix.tex, references.bib）\n\n### 你的审查侧重\n\n**方法严谨性和实验有效性**，重点关注：\n\n1. **实验设计的因果推断力**：\n   - trained vs untrained 对照是否充分隔离了 LLM 训练的贡献？reinitialize 6.74B params 是否是合理的 baseline？（vs. 随机初始化的 LLM 可能表现完全不同于一个未经 VLA 训练但经过语言预训练的模型）\n   - 2×2 factorial design 的效力：instruction presence × training status 是否覆盖了关键混淆因素？\n   - 单一模型（OpenVLA-7B）、单一 benchmark family（LIBERO）的泛化性问题\n\n2. **统计方法的合理性**：\n   - Bootstrap 10,000 resamples 的假设检验是否恰当\n   - RSA best-vs-best 比较（trained L12 vs untrained L0）是否存在 cherry-picking 问题\n   - 多重比较校正是否充分\n   - LOOCV 10-fold 是否有足够 power 给出 100%±0.00 的可信结论\n\n3. **Probing 方法论的局限**：\n   - Linear/MLP probe 是否能区分 \"information present\" vs \"information used\"\n   - Probe 的容量控制（2-layer 256-hidden MLP）是否合理\n   - R² 作为 metric 的选择是否有 ceiling/floor 效应\n\n4. **具体实验细节**：\n   - 数据量（10 tasks × 50 demos）是否足以支撑 per-layer 32-point profile 的结论\n   - Attention analysis 仅在 L1 做是否有选择性报告嫌疑\n   - \"instruction-blind\" 的结论是否过强（chance-level 分类 ≠ no instruction information）\n\n5. **可复现性**：\n   - 实验细节是否充分支撑复现\n   - 代码/数据是否可用\n\n请给出结构化审稿报告：Summary → Strengths → Weaknesses → Questions → Minor Issues"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验有效性）\n\n### Venue 信息\n- **目标会议**: CoRL 2026\n- **截止日期**: 2026-05-28（论文）\n- **页数限制**: 8 页正文 + references + appendix\n- **模板**: corl_2026（已正确使用）\n- **匿名规则**: double-blind\n- **特殊要求**: 必须含 Limitations section（计入 8 页），需论证 robotics relevance\n\n### 论文路径\n`projects/vla-ssd/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, appendix.tex, references.bib）\n\n### 你的审查侧重\n\n**方法严谨性和实验有效性**，重点关注：\n\n1. **实验设计的因果推断力**：\n   - trained vs untrained 对照是否充分隔离了 LLM 训练的贡献？reinitialize 6.74B params 是否是合理的 baseline？（vs. 随机初始化的 LLM 可能表现完全不同于一个未经 VLA 训练但经过语言预训练的模型）\n   - 2×2 factorial design 的效力：instruction presence × training status 是否覆盖了关键混淆因素？\n   - 单一模型（OpenVLA-7B）、单一 benchmark family（LIBERO）的泛化性问题\n\n2. **统计方法的合理性**：\n   - Bootstrap 10,000 resamples 的假设检验是否恰当\n   - RSA best-vs-best 比较（trained L12 vs untrained L0）是否存在 cherry-picking 问题\n   - 多重比较校正是否充分\n   - LOOCV 10-fold 是否有足够 power 给出 100%±0.00 的可信结论\n\n3. **Probing 方法论的局限**：\n   - Linear/MLP probe 是否能区分 \"information present\" vs \"information used\"\n   - Probe 的容量控制（2-layer 256-hidden MLP）是否合理\n   - R² 作为 metric 的选择是否有 ceiling/floor 效应\n\n4. **具体实验细节**：\n   - 数据量（10 tasks × 50 demos）是否足以支撑 per-layer 32-point profile 的结论\n   - Attention analysis 仅在 L1 做是否有选择性报告嫌疑\n   - \"instruction-blind\" 的结论是否过强（chance-level 分类 ≠ no instruction information）\n\n5. **可复现性**：\n   - 实验细节是否充分支撑复现\n   - 代码/数据是否可用\n\n请给出结构化审稿报告：Summary → Strengths → Weaknesses → Questions → Minor Issues"
  }
}
```

</details>

---


### Tool result

_source line 59 · 2026-05-17T04:31:52.445193+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18716
}
```

</details>

---


### Tool call

_source line 60 · 2026-05-17T04:31:52.947034+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + Related Work + 实际意义）\n\n### Venue 信息\n- **目标会议**: CoRL 2026\n- **截止日期**: 2026-05-28（论文）\n- **页数限制**: 8 页正文 + references + appendix\n- **模板**: corl_2026（已正确使用）\n- **匿名规则**: double-blind\n- **特殊要求**: 必须含 Limitations section（计入 8 页），需论证 robotics relevance，鼓励 real-robot experiments 或 sim-to-real 证据\n\n### 论文路径\n`projects/vla-ssd/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, appendix.tex, references.bib）\n\n### 你的审查侧重\n\n**新颖性、Related Work 覆盖度、对机器人社区的实际意义**，重点关注：\n\n1. **新颖性评估**：\n   - 相对于 Grant 2026（vision dominance behavioral study）、Haon 2025（mechanistic interp for VLA steering）、Swann 2026（SAE on VLA）、Buurmeijer/Rizzardo 2026（feature observability/controllability）的增量贡献是什么？\n   - \"First token-level representational decomposition\" 这一 claim 是否成立？检查是否有未引用的先行工作\n   - RSA + probing + attention analysis 组合是否构成方法论创新，还是标准工具的直接应用？\n   - trained vs untrained 对照的 novelty：是否有其他工作已做过类似比较？\n\n2. **Related Work 完整性**：\n   - 检查是否遗漏关键 related work（特别是 2025-2026 年 VLA interpretability/analysis 方向）\n   - 检查 VLM representation analysis 文献（非 VLA 领域但方法高度相关的工作）\n   - 引用密度是否符合 CoRL 水准（当前约 17 篇引用，是否偏少）\n   - Related Work section 是否做到了有效 positioning（不是 survey 而是建立 gap）\n\n3. **对 Robotics 社区的实际意义**：\n   - 三个 finding 是否能转化为可操作的设计建议？\n   - \"vision encoder quality is the primary design lever\" 是否有足够证据？\n   - 没有 real-robot 实验或 sim-to-real 验证——这对 CoRL 是否是致命缺陷？\n   - 纯分析论文在 CoRL 的历史接受率如何？\n\n4. **Claim 与 evidence 的匹配**：\n   - \"strict functional specialization\" 是否 overclaim（仅在 LIBERO 上验证）\n   - Design implications 是否过于 speculative（未验证 early-exit at L12 等）\n   - Abstract 中的强结论与 Discussion 中的 limitations 是否矛盾\n\n请给出结构化审稿报告：Summary → Strengths → Weaknesses → Questions → Missing References"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + Related Work + 实际意义）\n\n### Venue 信息\n- **目标会议**: CoRL 2026\n- **截止日期**: 2026-05-28（论文）\n- **页数限制**: 8 页正文 + references + appendix\n- **模板**: corl_2026（已正确使用）\n- **匿名规则**: double-blind\n- **特殊要求**: 必须含 Limitations section（计入 8 页），需论证 robotics relevance，鼓励 real-robot experiments 或 sim-to-real 证据\n\n### 论文路径\n`projects/vla-ssd/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, appendix.tex, references.bib）\n\n### 你的审查侧重\n\n**新颖性、Related Work 覆盖度、对机器人社区的实际意义**，重点关注：\n\n1. **新颖性评估**：\n   - 相对于 Grant 2026（vision dominance behavioral study）、Haon 2025（mechanistic interp for VLA steering）、Swann 2026（SAE on VLA）、Buurmeijer/Rizzardo 2026（feature observability/controllability）的增量贡献是什么？\n   - \"First token-level representational decomposition\" 这一 claim 是否成立？检查是否有未引用的先行工作\n   - RSA + probing + attention analysis 组合是否构成方法论创新，还是标准工具的直接应用？\n   - trained vs untrained 对照的 novelty：是否有其他工作已做过类似比较？\n\n2. **Related Work 完整性**：\n   - 检查是否遗漏关键 related work（特别是 2025-2026 年 VLA interpretability/analysis 方向）\n   - 检查 VLM representation analysis 文献（非 VLA 领域但方法高度相关的工作）\n   - 引用密度是否符合 CoRL 水准（当前约 17 篇引用，是否偏少）\n   - Related Work section 是否做到了有效 positioning（不是 survey 而是建立 gap）\n\n3. **对 Robotics 社区的实际意义**：\n   - 三个 finding 是否能转化为可操作的设计建议？\n   - \"vision encoder quality is the primary design lever\" 是否有足够证据？\n   - 没有 real-robot 实验或 sim-to-real 验证——这对 CoRL 是否是致命缺陷？\n   - 纯分析论文在 CoRL 的历史接受率如何？\n\n4. **Claim 与 evidence 的匹配**：\n   - \"strict functional specialization\" 是否 overclaim（仅在 LIBERO 上验证）\n   - Design implications 是否过于 speculative（未验证 early-exit at L12 等）\n   - Abstract 中的强结论与 Discussion 中的 limitations 是否矛盾\n\n请给出结构化审稿报告：Summary → Strengths → Weaknesses → Questions → Missing References"
  }
}
```

</details>

---


### Tool result

_source line 61 · 2026-05-17T04:32:08.753369+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15806
}
```

</details>

---


### Tool call

_source line 62 · 2026-05-17T04:32:08.904409+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "3",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 3（写作质量 + 格式合规 + 呈现清晰度）\n\n### Venue ��息\n- **目标会议**: CoRL 2026\n- **截止日期**: 2026-05-28（论文）\n- **页数限制**: 8 页正文 + references + appendix\n- **模板**: corl_2026（已正确使用）\n- **匿名规则**: double-blind\n- **特殊要求**: 必须含 Limitations section（计入 8 页），Limitations 需描述 limiting assumptions, failure modes, and limitations\n\n### 论文路径\n`projects/vla-ssd/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, appendix.tex, references.bib）\n\n### 你的审查侧重\n\n**写作质量、格式合规、呈现效果**，重点关注：\n\n1. **格式合规**：\n   - 8 页限制是否满足（估算当前页数）\n   - Limitations section 是否存在且计入正文（CoRL 2026 硬要求）\n   - 匿名化是否完整（无 GitHub link、无 author self-citation 暴露身份）\n   - 参考文献格式是否一致（bib 条目完整性）\n\n2. **写作风格（参照 paper-writing-norms）**：\n   - 检查 AI 写作痕迹：em-dash（—）、解释性 en-dash（–）、-ing phrase 结尾、过度分段\n   - Abstract 是否满足 4 个必答问题（问题/重要性/方法/结果），150-250 words\n   - Introduction 是否有清晰的 5 段叙事结构\n   - Related Work 是否 survey 风格 vs positioning 风格\n   - 全文主线是否统一（Abstract → Intro → Method → Experiments → Discussion → Conclusion 一条线）\n\n3. **呈现效果**：\n   - Figure 数量和信息密度是否合理\n   - Table 格式：小数精度统一性、最优加粗、caption 自包含性\n   - 术语定义：首次出现的缩写是否有定义（VLA, RSA, RDM, CKA, LOOCV 等）\n   - 数字引用的精度和一致性\n\n4. **叙事连贯性**：\n   - 三个 findings 的呈现顺序是否最优\n   - Discussion implications 与 Experiments 的对应关系是否清晰\n   - Conclusion 是否有新信息（应只总结，不引入新内容）\n\n5. **CoRL 特定要求**：\n   - 是否讨论了对 robotics 的直接影响\n   - 是否提供/承诺 code/data/video supplementary\n\n请给出结构化审稿报告：Summary → Strengths → Weaknesses → Questions → Format Issues"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "3",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 3（写作质量 + 格式合规 + 呈现清晰度）\n\n### Venue ��息\n- **目标会议**: CoRL 2026\n- **截止日期**: 2026-05-28（论文）\n- **页数限制**: 8 页正文 + references + appendix\n- **模板**: corl_2026（已正确使用）\n- **匿名规则**: double-blind\n- **特殊要求**: 必须含 Limitations section（计入 8 页），Limitations 需描述 limiting assumptions, failure modes, and limitations\n\n### 论文路径\n`projects/vla-ssd/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, appendix.tex, references.bib）\n\n### 你的审查侧重\n\n**写作质量、格式合规、呈现效果**，重点关注：\n\n1. **格式合规**：\n   - 8 页限制是否满足（估算当前页数）\n   - Limitations section 是否存在且计入正文（CoRL 2026 硬要求）\n   - 匿名化是否完整（无 GitHub link、无 author self-citation 暴露身份）\n   - 参考文献格式是否一致（bib 条目完整性）\n\n2. **写作风格（参照 paper-writing-norms）**：\n   - 检查 AI 写作痕迹：em-dash（—）、解释性 en-dash（–）、-ing phrase 结尾、过度分段\n   - Abstract 是否满足 4 个必答问题（问题/重要性/方法/结果），150-250 words\n   - Introduction 是否有清晰的 5 段叙事结构\n   - Related Work 是否 survey 风格 vs positioning 风格\n   - 全文主线是否统一（Abstract → Intro → Method → Experiments → Discussion → Conclusion 一条线）\n\n3. **呈现效果**：\n   - Figure 数量和信息密度是否合理\n   - Table 格式：小数精度统一性、最优加粗、caption 自包含性\n   - 术语定义：首次出现的缩写是否有定义（VLA, RSA, RDM, CKA, LOOCV 等）\n   - 数字引用的精度和一致性\n\n4. **叙事连贯性**：\n   - 三个 findings 的呈现顺序是否最优\n   - Discussion implications 与 Experiments 的对应关系是否清晰\n   - Conclusion 是否有新信息（应只总结，不引入新内容）\n\n5. **CoRL 特定要求**：\n   - 是否讨论了对 robotics 的直接影响\n   - 是否提供/承诺 code/data/video supplementary\n\n请给出结构化审稿报告：Summary → Strengths → Weaknesses → Questions → Format Issues"
  }
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-17T04:32:10.363570+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_3\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1459
}
```

</details>

---


### Assistant

_source line 64 · 2026-05-17T04:32:15.291037+00:00_

三名 Reviewer 已触发，Round 1 独立审稿进行中：

| Reviewer | 侧重 | 状态 |
|----------|------|------|
| R1 | 方法严谨性 + 实验有效性 | 审稿中 |
| R2 | 新颖性 + Related Work + 实际意义 | 审稿中 |
| R3 | 写作质量 + 格式合规 + 呈现 | 审稿中 |

等待各 Reviewer 返回 Round 1 报告后，将进入交叉分享（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 2

## Round 2

2 recorded events


### User

_source line 65 · 2026-05-17T04:35:57.223629+00:00_

[Reviewer 1 审稿意见]:
## Round 1 审稿报告 — Reviewer 1（方法严谨性 + 实验有效性）

**论文标题**: Vision Encodes, Language Routes: A Representational Decomposition of Vision-Language-Action Models

---

## 总体评分

**Overall**: 5/10 (Marginally below acceptance threshold)

**一句话总结**: 论文提出了有价值的分析框架，但核心实验设计存在关键混淆（untrained baseline 不能隔离 VLA fine-tuning 的贡献），单一模型+单一 benchmark family 的泛化性不足以支撑关于"VLAs"的一般性结论。

---

## 官方维度打分（基于 CoRL review form：Originality / Quality / Clarity / Significance / Relevance / Limitations）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Originality | 7/10 | 首次做 token-level representational decomposition 的 VLA 分析，分析框架（cross-instruction probe + attention + RSA + functional probe 的组合）有新意 |
| Quality | 4/10 | 关键对照设计有根本缺陷（见 N1）；RSA best-vs-best 存在 cherry-picking（N3）；probing 的 encoding vs. use 混淆（N4）；统计检验力不足 |
| Clarity | 7/10 | 写作清晰，结构合理，图表信息密度高；但部分 claim 的措辞过强，超出证据支撑范围 |
| Significance | 5/10 | 如果结论成立，对 VLA 架构设计有实际指导意义；但单模型单 benchmark 限制了影响力，且部分结论（如 vision encoder is primary design lever）缺乏因果支撑 |
| Relevance | 8/10 | 直接分析 robot learning 核心模型架构，高度相关 |
| Limitations | 6/10 | Section 5 诚实讨论了主要限制，但低估了 untrained baseline 的根本问题和 probing 方法论的局限性 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Untrained control 不能隔离 VLA fine-tuning 的贡献

- 具体位置：Section 3.1, "reinitializing all LLM parameters via `from_config()` (6.74B random weights)"
- 问题：论文将 trained（OpenVLA-7B，含 Llama-2 预训练 + VLA fine-tuning）与 untrained（完全随机权重）对比，声称差异反映 "training learns deliberate routing"。但这个对照混淆了两个因素：(1) Llama-2 语言预训练的贡献（结构化 attention pattern、语言理解能力）；(2) VLA fine-tuning 的贡献。随机初始化的 6.74B 参数 LLM 缺乏任何结构化处理能力，routing 的 decay（82% at L31）可能仅仅反映随机网络的 signal degradation，而非 "absence of deliberate routing"。
- 正确的对照应包括：Llama-2 原始 checkpoint（无 VLA fine-tuning但有语言预训练）——这才能隔离 VLA 训练本身的贡献。
- 为什么影响接收：论文三个核心发现中的第二个（"training learns deliberate instruction routing"）和所有 trained vs. untrained 的定量比较（Table 3 所有 Δ 值）都依赖这个对照。如果差异主要来自语言预训练而非 VLA fine-tuning，则论文的核心叙事（"VLA training reshapes routing"）不成立。
- 建议修改方向：增加 Llama-2 base checkpoint 作为第三个条件（pretrained-but-not-VLA-finetuned），形成三级对照：random → language-pretrained → VLA-finetuned。至少对 attention analysis 和 cross-instruction probe 做这个消融。

**N2** [critical] 单一模型、单一 benchmark family 无法支撑关于 "VLAs" 的一般性结论

- 具体位置：Title（"Vision-Language-Action Models"，复数）；Abstract（"VLAs maintain a strict division of labor"）；Conclusion（"VLA architectures should optimize routing"）
- 问题：所有实验仅在 OpenVLA-7B（一个特定架构：frozen DinoSigLIP + MLP projector + Llama-2）上进行，仅在 LIBERO（tabletop manipulation，简单视觉场景）上评估。论文的 claims 却使用复数 "VLAs" 并给出架构设计建议。不同 VLA 架构差异巨大：RT-2 使用 PaLM-E，π₀ 使用 flow matching，Octo 使用 transformer decoder。frozen vision encoder 的设计也是 OpenVLA 的特定选择，其他 VLA 可能 fine-tune encoder。
- 为什么影响接收：CoRL reviewer guidelines 要求评估 "significance and novelty of the results" 及 "potential for scientific and technological impact"。单个数据点无法建立一般性规律，特别是当结论明确为架构设计建议时。
- 建议修改方向：(1) 将所有 claim 限定为 "OpenVLA-7B" 或 "frozen-encoder VLAs"；(2) 至少在一个不同架构的 VLA 上验证核心发现（如 RT-2 family 或任何 fine-tune encoder 的 VLA）；(3) 如果无法增加模型，则明确讨论哪些发现可能是架构特异性的（如 frozen encoder → instruction-blind image tokens 可能是 trivial 推论）。

**N3** [critical] RSA best-vs-best 比较存在 selection bias

- 具体位置：Table 3, "Best-vs-best image_mean: trained L12 vs. untrained L0, Δ = +0.017, CI incl. 0, n.s."
- 问题：best-vs-best 比较允许每个条件独立选择最优层。在 32 层中取 max，统计上会引入正偏置（winner's curse / multiple comparisons）。论文报告此差异不显著（CI 包含 0），但仍在 narrative 中积极解读为 "training redistributes geometry"（Section 4.3 标题）。更令人担忧的是 LIBERO-Spatial 的 Δ = +0.023, p < 0.001 被用来 "confirm that the n.s. result on Goal reflects limited power"（Section 4.4），这是用一个独立数据集的显著结果来否定另一个数据集的零结果，方法论上不成立。
- 此外，readout token 的 best-vs-best（trained L13 vs. untrained L32）比较的两个层差距 19 层，功能完全不同，这种比较的解释价值存疑。
- 为什么影响接收：核心定量结论（training effect size）的可信度受损。审稿人和读者无法区分真实效应和统计噪音。
- 建议修改方向：(1) 报告 same-layer paired comparison 作为主要结果（已有 L12 same-layer Δ = +0.079, p < 0.0001）；(2) 对 best-vs-best 做 multiple comparisons correction（如 Bonferroni 或 permutation-based max-statistic）；(3) 明确区分 "training shifts peak location" vs. "training improves peak magnitude" 两个独立 claim。

**N4** [critical] Probing 结果不能支撑 "functional" 或 "used" 的结论

- 具体位置：Section 3.6 标题 "Functional Action Probes"；Section 4.1 "Functional implications"；Discussion "vision encoder quality is the primary design lever"
- 问题：论文在标题中使用 "functional" 来描述 MLP probe，并将 probe R² 解释为 "functional capacity"。但 probing 文献已充分论证（Belinkov 2022，论文自己引用），probe accuracy 证明 information is linearly/nonlinearly extractable，不证明 model uses this information for downstream task。同样，高 RSA 证明 geometric alignment，不证明 causal contribution。论文的核心设计建议（"vision encoder quality is the primary design lever"）完全基于 DINOv2 有最高 RSA，但没有任何因果证据（如 intervention、ablation）表明更好的 RSA 导致更好的 task performance。
- 此外，2-layer 256-hidden MLP probe 的容量控制值得质疑：对 4096-D input 预测 7-D output，256-hidden 可能过小（underfitting）或过大（overfitting 到 probe-specific features）。没有报告 probe 的 train/test split 细节或 overfitting 诊断。
- 为什么影响接收：论文最重要的实际建议（"invest in stronger self-supervised encoders"）没有因果支撑。如果仅仅是 "DINOv2 representations happen to be geometrically similar to the action space" 但 VLA 并不通过这种 geometry 来生成 action，则建议无实际价值。
- 建议修改方向：(1) 将 "functional" 改为 "decodable" 以准确描述 probe 测量的是什么；(2) 增加因果证据：用不同 vision encoder 的 VLA variant（如 CLIP-only vs. DINOv2-only）训练并比较 task success rate；(3) 或至少在 Discussion 中明确这是 correlational evidence，不直接支撑因果设计建议。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] "Instruction-blind" claim 过强

- 具体位置：Section 4.1, "Image tokens are instruction-blind"；Abstract, "instruction classification at chance, 10%, across all layers"
- 问题：chance-level linear probe accuracy (10%) 不等于 "no instruction information"。这仅证明 10-way instruction identity 不是 linearly separable from image_mean activations。论文用了 MLP probe 做 action prediction 但只用 linear probe 做 instruction classification——如果对 instruction 也用 MLP probe 或更高容量模型，结果是否一致？此外，instruction influence 可能以 non-identity 方式存在（如 shift attention to task-relevant spatial regions），这种 graded influence 不会被 10-way classification probe 捕捉到。
- 建议：(1) 补充 MLP probe 对 instruction classification 的结果；(2) 将 claim 限定为 "instruction identity is not linearly decodable from image tokens"；(3) 讨论 subtler forms of instruction influence（如 conditional attention to different image regions）。

**W2** [warning] CKA 与 RSA 结论矛盾，处理不充分

- 具体位置：Appendix B (Section A.2), "Linear CKA reverses the RSA ordering"
- 问题：Linear CKA 显示 untrained > trained > DINOv2，完全逆转 RSA 的 DINOv2 > trained > untrained。论文将此作为 "different metrics capture different things" 一笔带过。但这引发根本问题：如果两个标准度量给出相反结论，论文选择 RSA 作为主要结论的依据是什么？仅仅因为 RSA 支持了论文想要的 narrative（DINOv2 最好、training helps）吗？
- RDM kernel CKA 部分解决（trained ≈ projector > untrained > DINOv2），但仍然显示 DINOv2 最差，与 RSA 的 DINOv2 最优完全相反。
- 建议：正文中讨论 metric divergence，解释为什么 RSA（rank-order preservation）比 CKA（linear covariance structure）更适合评估 action-relevant geometry，或者承认结论是 metric-dependent 的。

**W3** [warning] Attention analysis 仅限 L1，可能存在选择性报告

- 具体位置：Section 4.2, "We analyze L1 attention distributions"
- 问题：为什么只分析 L1？如果 routing 真的是 "maintained through L31"（如 cross-instruction probe 显示），那 intermediate layers 的 attention pattern 如何？是否所有层都维持 instruction-dominant pattern，还是仅 L1 如此而后续层通过 residual connection 传递信号？只报告支持结论的单一层，令人怀疑是否其他层的 attention pattern 不支持 narrative。
- 建议：至少报告 L8、L16、L31 的 attention distribution（或在 appendix 给出全层 attention profile），以证明没有选择性报告。

**W4** [warning] LOOCV 100%±0.00 的统计检验力问题

- 具体位置：Section 4.1, "Leave-one-out cross-validation over 10 folds confirms perfect generalization: 100% ± 0.00"
- 问题：10-fold LOOCV 在 10-way classification 中得到 100%，这个设计的 statistical power 需要审视。(1) 每 fold 只 hold out 1 个 class，train on 9 classes——如果 representations 是 4096-D 且 classes 仅 10 个，线性分离几乎是 trivial 的（d >> k）；(2) 需要 baseline：random Gaussian features 在同样维度下做 10-way classification 能达到什么精度？如果也接近 100%，则 probe 结果无信息量。
- 论文未报告每 fold 的样本数。如果每 task 50 demos，总共 500 samples 做 10-way with 4096-D features，即使是 random features 也可能 linearly separable。
- 建议：报告 random feature baseline（permutation test for probe accuracy），报告每 fold 的 n，讨论 dimensionality vs. sample size ratio 对分类精度 ceiling 的影响。

**W5** [warning] 数据规模对结论稳定性的影响

- 具体位置：Section 3.1, "10 tasks, 50 demonstrations each"
- 问题：500 total demonstrations 用于拟合 per-layer 32-point profiles。虽然 Appendix F.5 的 demo subsample analysis（25 demos）显示 RSA profile r = 0.970，但 probe R² profile r 仅 0.819，peak layer 从 L9 shift 到 L11。这表明 probe 结果对数据量敏感。论文中多处基于 peak layer 的精确位置做结论（"L8-L13 region"、"peak at L12"），但这些位置在 plateau region 内对数据量敏感。
- 建议：在正文中承认 peak layer 的精确位置不应过度解读，重点放在 "inverted-U exists" 而非 "peak is at exactly L12"。

---

## 小问题（不影响接收）

- Abstract 第 6 句 "RSA peaks at L8--L13"：en-dash 此处表示范围，可接受，但 Section 4.3 中 "$R^2$ peaks in the L8--L10 region" 与 Table 2 中 "L8--L10†" 不一致（seed analysis 显示 4/5 seeds peak at L9-L10，1 seed at L16），建议统一表述。
- Table 2 footnote 中 "$R^2$ peak region across 5 seeds (0.655 ± 0.002)"——±0.002 是 std 还是 95% CI？未明确。
- Section 4.1 "QA probes for task progress": 训练和未训练模型差距仅 1pp (86.3% vs 85.3%)，但文中表述 "trained last_preaction achieves 86.3% (L20), exceeding DINOv2 cls_token (82.7%)" 只与 DINOv2 比而不强调与 untrained 的微小差异，有 framing bias。
- References: grant2026 (arXiv:2603.19233) 和 hou2026 (arXiv:2603.00592) 的 arXiv ID 格式为 26xx，需确认这些是否为真实存在的 preprints（2026 年 3 月）。
- 论文未包含 code/data availability statement（CoRL 鼓励 reproducibility）。

---

## 主要优势

1. **分析框架的系统性**：四种互补方法（cross-instruction probe、attention analysis、RSA、functional probe）的组合比单一 metric 更有说服力，且 2×2 factorial design 的思路清晰。
2. **Robustness analyses 全面**：distance metric invariance、per-DOF decomposition、permutation test、seed sensitivity、demo subsampling——附录内容扎实。
3. **写作清晰**：论文结构好，图表信息密度高，叙事线清晰（specialization → routing → transformation），读起来不费力。
4. **Cross-benchmark replication**：在 LIBERO-Spatial 上复制核心 inverted-U pattern，增加了 pattern 存在性的可信度（虽然仍是同一 benchmark family）。
5. **诚实的 null results**：报告了 RSA best-vs-best CI 包含 0、CKA 与 RSA 矛盾、RSA-R² peak convergence 不跨 benchmark 复制等 "不利" 结果，说明作者没有只挑好看的数据。

---

## 对作者的核心问题（期待 rebuttal 回应）

1. 是否有 Llama-2 base checkpoint（无 VLA fine-tuning）的 attention 和 routing 数据？如果没有，能否在 rebuttal 期间补充？
2. Random features baseline 在同维度同样本量下做 10-way classification 的精度是多少？
3. L8、L16 或 L31 的 attention head distribution 是什么样的？是否也是 instruction-dominant？
4. 如果用 MLP probe（而非 linear probe）做 instruction classification on image_mean，结果是否仍为 chance？
5. "Vision encoder quality is the primary design lever" 这个建议是否有任何因果验证（如替换 encoder 后的 task success rate 对比）？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 66 · 2026-05-17T04:36:06.720256+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 和 Reviewer 3 完成独立审稿后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 3

## Round 3

2 recorded events


### User

_source line 67 · 2026-05-17T04:36:09.298138+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**核心判断**：Overall 5/10，略低于接收线。论文分析框架有新意且写作清晰，但存在四个 critical 问题：

1. **Untrained baseline 设计缺陷**：random weights vs. trained 不能隔离 VLA fine-tuning 的贡献（混淆了 Llama-2 语言预训练 vs. VLA 训练）
2. **N=1 模型泛化性不足**：仅 OpenVLA-7B + LIBERO，无法支撑关于 "VLAs" 的一般性结论和架构设计建议
3. **RSA best-vs-best 存在 selection bias**：32 层取 max 有正偏置，且主 benchmark 结果不显著
4. **Probing 的 encoding ≠ use**：核心设计建议（"vision encoder is primary lever"）缺乏因果证据

最关键的修改是补充 Llama-2 base checkpoint 作为中间对照，这会根本改变对 "training effect" 的解释。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 68 · 2026-05-17T04:36:17.277567+00:00_

Reviewer 1 报告已收录。等待 Reviewer 2 和 Reviewer 3 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 4

## Round 4

2 recorded events


### User

_source line 69 · 2026-05-17T04:36:45.106777+00:00_

[Reviewer 2 审稿意见]:
## Round 1 审稿报告 — Reviewer 2（新颖性 + Related Work + 实际意义）

**论文**: "Vision Encodes, Language Routes: A Representational Decomposition of Vision-Language-Action Models"

---

## 总体评分

**Overall**: 4/10 (Borderline Reject)
**一句话总结**: 实验设计严谨但贡献增量有限——标准分析工具的组合应用于单一模型/单一 benchmark，无方法论创新，design implications 未经验证，且 Related Work 过于单薄。

## 官方维度打分（CoRL review form，参照 CoRL 2023/2024 标准）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Originality | 3/10 | 方法是标准工具 (RSA+probing+attention) 的直接组合，"first token-level decomposition" claim 站不住脚（见 N1） |
| Quality | 6/10 | 实验严谨（bootstrap CI、LOOCV、cross-benchmark），但关键 RSA 结果 n.s.，CKA 反转 RSA 结论未充分讨论 |
| Clarity | 7/10 | 写作清晰、结构良好，但 Related Work 过短 |
| Significance | 3/10 | design implications 全部 speculative，无验证；对 robotics 社区 actionable value 低 |
| Relevance | 5/10 | 研究对象是 VLA 但完全是离线分析，无 robot 实验，对 CoRL 社区实际价值存疑 |
| Limitations | 7/10 | Limitations section 诚实，覆盖了主要弱点 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] "First token-level representational decomposition" claim 不成立

- 具体位置：Abstract L2, Introduction L10, Conclusion L1
- 问题：Neo et al. (ICLR 2025, "Towards Interpreting Visual Information Processing in Vision-Language Models") 已对 VLM (LLaVA) 进行了 token-level 分析，发现 (1) object information 高度 localized 到对应 visual token 位置，(2) visual token representations 跨 layer 逐步与 textual tokens 对齐，(3) 最终 token 位置通过 mid-late layer attention 提取 object information。虽然该工作针对 VLM 而非 VLA，但方法论框架（per-token probing + layer-wise analysis + attention mechanism 分析）高度重合。此外 Grant 2026 (Action Atlas) 明确做了 per-token 分析（"per-token processing is generally essential"），训练了 424 SAEs 做 per-token 分解，且覆盖 6 个模型 + 4 个 benchmark。本文的 "first" claim 需要大幅限定或删除。
- 为什么影响接收：novelty claim 的核心基础被削弱
- 建议：改为 "first systematic *trained-vs-untrained* per-layer decomposition of a VLA with factorial design"，同时必须引用并讨论 Neo et al. 2025

**N2** [critical] 方法无创新——标准工具的直接应用

- 具体位置：Section 3 (Method) 整体
- 问题：RSA (Kriegeskorte 2008)、linear/MLP probing (Alain 2017)、attention pattern analysis 都是 20+ 年 / 10+ 年历史的标准工具。论文没有提出任何新的分析方法、新的 metric、或新的实验范式。"Cross-instruction probe" 本质是标准 linear probe 的一个 application scenario。$2\times 2$ factorial design 是实验设计上的好实践，但不构成方法贡献。对于 CoRL 这种重视方法创新和实际应用的会议，纯用现有工具做分析、不产出新方法或新系统，竞争力不足。
- 为什么影响接收：CoRL 期望 either novel methods or actionable design insights backed by experiments；本文两者都不提供
- 建议：要么 (1) 基于发现设计并验证新架构（如 early-exit action head at L12），要么 (2) 提出可复用的新分析框架

**N3** [critical] Design implications 完全 speculative，未经任何验证

- 具体位置：Discussion §6 "Implications for VLA design"
- 问题：三条 design implications（vision encoder quality 是 primary lever；action head 应读 L12-L13；instruction 仅通过 readout token 影响 action）全部是从分析结果外推的假设，没有任何验证实验。例如：
  - "early exit at L12" 未测试——作者自己在 Limitations 中承认 "they do not address whether architectural interventions would alter the patterns we observe"
  - "vision encoder quality is the primary design lever" 仅基于 RSA 排序 (DINOv2 > CLIP)，但 (1) 这忽略了 CKA 完全反转该排序（Appendix §A.2: untrained > trained > projector > DINOv2），(2) 从 representation 相似性到 task performance 的推断缺乏因果证据
  - 没有 ablation 测试替换不同质量的 vision encoder 对下游 task success rate 的影响
- 为什么影响接收：CoRL 审稿标准要求 "significance" 和对 robot learning 的实际贡献；纯 speculative implications 不满足
- 建议：至少做一组验证实验（如 early-exit probe at L12 vs full-depth，或 swap vision encoder quality 对 LIBERO success rate 的影响）

**N4** [critical] 单一模型 + 单一 benchmark 家族，泛化性严重不足

- 具体位置：Section 4.1 (Setup), Discussion Limitations
- 问题：仅研究 OpenVLA-7B 在 LIBERO 上的表现。LIBERO 是 tabletop manipulation 的简单仿真 benchmark（10 tasks, 50 demos each）。其他主流 VLA（RT-2、π₀、Octo）使用不同架构（encoder-decoder vs decoder-only、diffusion action head vs autoregressive）。Grant 2026 覆盖了 6 个模型（80M-7B）和 4 个 benchmark。Buurmeijer 2026 在 π₀.5 和 OpenVLA 上验证。本文的 "strict functional specialization" 结论可能是 OpenVLA 特定架构（frozen vision encoder + Llama-2 backbone）的 artifact，不能推广为 VLA 的通用属性。
- 为什么影响接收：结论的普适性不成立，大幅降低影响力
- 建议：至少在一个额外架构（如 π₀ 或 RT-2-X）上验证核心 finding

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Related Work 严重不足（21 篇引用，3 段 15 行）

- 具体位置：Section 2
- 问题：
  1. **引用量偏低**：CoRL 2024/2025 录用论文通常有 40-60+ 篇引用，本文仅 21 篇
  2. **缺失关键 VLM 分析文献**：Neo et al. (ICLR 2025) 是 VLM token-level 分析的核心先行工作，必须引用。VLM-LENS (EMNLP 2025) 提供了系统化 probing 框架。"Visual Representations inside the Language Model" (arXiv 2510.04819) 研究了 LLM 内部视觉表征演化。
  3. **缺失 LLM interpretability 经典文献**：logit lens (nostalgebraist 2020)、residual stream analysis (Elhage et al. 2021)、information flow in transformers
  4. **缺失 representation learning 比较文献**：Raghu et al. (NeurIPS 2021) "Do Vision Transformers See Like CNNs?"、Nguyen et al. 2021 对 CKA/RSA 的比较分析
  5. **Related Work 缺乏 positioning**：当前仅列举先行工作，没有清楚说明本文与 Grant 2026、Swann 2026、Buurmeijer 2026 的具体差异和增量贡献
- 建议：扩展 Related Work 至少到 1 页，增加 VLM 分析、LLM interpretability、representation comparison 三个子节，明确 differentiation

**W2** [warning] CKA 结果与 RSA 结论矛盾，处理不够充分

- 具体位置：Appendix §A.2 (Metric Sensitivity)
- 问题：Linear CKA 完全反转 RSA 排序——untrained > trained > projector > DINOv2。这意味着 "DINOv2 provides the highest geometric foundation" 这一核心 narrative（Abstract L6, Discussion §6）仅在 RSA 这一特定 metric 下成立。论文将此放在 appendix 一笔带过（"reflects the known sensitivity of representation similarity metrics"），但这实际上严重动摇了 "vision encoder quality is the primary design lever" 的推论。如果不同 metric 给出相反结论，那么基于单一 metric 的 design recommendation 就不可靠。
- 建议：在正文 Discussion 中显式讨论这一矛盾，说明为什么 RSA（rank-order preservation）比 CKA（global linear structure）更适合作为 action-relevant quality 的 proxy，或者承认该 design implication 是 metric-dependent 的

**W3** [warning] 核心 RSA 结果统计不显著

- 具体位置：Table 3 (Training Effects), Experiments §4.3
- 问题：LIBERO-Goal 上 RSA best-vs-best 的 training effect ($\Delta = +0.017$) CI 包含零，即 n.s.。论文试图用 LIBERO-Spatial 的显著结果 ($\Delta = +0.023$, $p < 0.001$) 来 rescue，称 Goal 的 n.s. "reflects limited power"。但如果主实验的核心指标不显著，而依赖一个 appendix 中的辅助 benchmark 来支撑结论，这在审稿中是不够 convincing 的。
- 建议：要么增加 LIBERO-Goal 的样本量使 CI 缩小，要么将 LIBERO-Spatial 提升为 co-primary 分析并在正文充分呈现

**W4** [warning] 无 real-robot 实验——CoRL 期望 robotics grounding

- 具体位置：全文
- 问题：CoRL CFP 明确 "highly encouraged to submit real-robot experiments or sim-to-real evidence"。纯仿真 + 纯离线分析论文在 CoRL 的接受率偏低。论文的分析完全基于 frozen representations，不涉及任何 closed-loop 行为评估。即使是分析论文，Grant 2026 做了 394,000+ rollout episodes 的 behavioral validation，Buurmeijer 2026 做了 closed-loop steering 实验。本文没有任何 rollout-level 验证。
- 建议：至少补充 (1) 用 best-layer representation 做 action prediction 后在 LIBERO 上的 success rate 对比，或 (2) 验证 early-exit 架构在 rollout 中的表现

---

## 小问题（不影响接收）

- Abstract 中 "instruction classification at chance, $10\%$" 括号使用略显突兀，建议改为独立从句
- Table 1 caption 提到 "L0-L8 shown" 但表格实际包含 L0, L1, L4, L8, L16, L31——caption 不准确
- $R^2$ peak 在 Table 2 中标注为 "L8--L10†"，但正文多处使用不同范围（L8-L13, L8-L10, L8-L16）——术语不统一
- Figure 3 和 Figure 5(a) 内容高度重叠（都是 per-layer RSA profile），空间效率低

---

## 主要优势

1. **实验设计严谨**：$2\times 2$ factorial design（training status × instruction presence）是分析论文的 best practice；bootstrap CI + LOOCV + cross-benchmark replication + permutation test + seed sensitivity 构成完整的统计验证体系
2. **清晰的叙事结构**：三个 finding 层层递进（what → how → where），读者容易跟随
3. **Trained vs untrained 对照有价值**：揭示了 "architecture provides incidental routing but training makes it robust" 这一洞察，区分了架构贡献 vs 学习贡献
4. **DINOv2 > CLIP 在 action alignment 上的发现**：虽然在单一 metric 下，但对 vision encoder 选择有参考意义
5. **论文写作质量高**：简洁、technical precision 好、结果呈现清晰

---

## 缺失引用（必须补充）

1. **Neo et al. (ICLR 2025)** "Towards Interpreting Visual Information Processing in Vision-Language Models" — VLM token-level 分析的直接先行工作
2. **"Visual Representations inside the Language Model" (arXiv 2510.04819)** — LLM 内部视觉表征演化
3. **LLM interpretability 经典**: logit lens, residual stream analysis (Elhage et al. 2021, "A Mathematical Framework for Transformer Circuits")
4. **Raghu et al. (NeurIPS 2021)** "Do Vision Transformers See Like Convolutional Neural Networks?" — ViT layer-wise representation analysis 方法论
5. **CoRL/RSS 接受的 VLA 分析论文**（如有）

---

## Questions to Authors

1. 既然 CKA 反转了 RSA 的 encoder 排序，你们如何论证 "vision encoder quality is the primary design lever" 不是 metric-dependent 的结论？
2. Neo et al. (ICLR 2025) 已经在 VLM 中做了 token-level analysis 并发现了 localized information + last-token integration，你们的工作相对于他们的具体增量是什么？
3. 如果 "early exit at L12" 被验证为不改变 action prediction quality（因为改变了 forward pass 可能改变 representation），你们的 design implication 还剩什么 actionable content？
4. Grant 2026 覆盖了 6 个模型并发现 "per-token processing is generally essential"——这是否已经涵盖了你们的 "token-level specialization" finding？
5. 为什么不做至少一个 rollout-level 实验（如用 L12 representation 直接预测 action 并在 LIBERO 上评估 success rate）来 ground 你们的分析发现？

---

## 总结判断

本文是一篇执行良好的分析研究，但对 CoRL 2026 而言存在根本性的竞争力问题：(1) 方法无创新（标准工具的组合），(2) novelty claim 不成立（先行工作已覆盖相似分析），(3) design implications 完全 speculative，(4) 单模型单 benchmark 泛化性不足，(5) 无任何 robot 实验或 behavioral validation。建议作者增加验证实验（early-exit 或 encoder swap 对 task success 的影响）、扩大模型覆盖、或投稿至更适合纯分析工作的 venue（如 TMLR 或 NeurIPS Workshops）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 70 · 2026-05-17T04:37:00.629157+00:00_

收到 Reviewer 2 审稿报告。当前状态：

- Reviewer 1 ✅（5/10，方法严谨性）
- Reviewer 2 ✅（4/10，新颖性+意义）
- Reviewer 3 ⏳（写作+格式，等待中）

等待 Reviewer 3 完成后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 5

## Round 5

2 recorded events


### User

_source line 71 · 2026-05-17T04:37:03.257480+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**核心判断**：4/10 (Borderline Reject)。四个 critical 问题：

1. **"First token-level decomposition" claim 不成立** — Neo et al. (ICLR 2025) 已对 VLM 做了 token-level 分析，Grant 2026 (Action Atlas) 对 6 个 VLA 做了 per-token 分析
2. **无方法论创新** — RSA + probing + attention 全是标准工具的直接应用
3. **Design implications 全部 speculative** — "early exit at L12"、"vision encoder quality is primary lever" 均未验证，且 CKA 反转 RSA 结论
4. **单模型单 benchmark** — 仅 OpenVLA + LIBERO，无法支撑 "VLA 通用属性" 的结论

Related Work 仅 21 篇引用、3 段 15 行，缺失 VLM token-level 分析的核心先行工作。对 CoRL 而言，无 real-robot 实验、无 rollout-level behavioral validation 是额外劣势。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 72 · 2026-05-17T04:37:13.655569+00:00_

收到 Reviewer 1（5/10）和 Reviewer 2（4/10）的报告。等待 Reviewer 3 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 6

## Round 6

8 recorded events


### User

_source line 73 · 2026-05-17T04:37:15.161871+00:00_

[Reviewer 3 审稿意见]:
## Reviewer 3 — Round 1 审稿报告（写作质量 + 格式合规 + 呈现清晰度）

**论文**: "Vision Encodes, Language Routes: A Representational Decomposition of Vision-Language-Action Models"
**Venue**: CoRL 2026

---

## 总体评分
**Overall**: 6/10 (Weak Accept — 写作质量和呈现效果总体良好，但存在若干格式合规问题和 AI 写作痕迹需要修正)
**一句话总结**: 论文叙事结构清晰、数据呈现严谨，但 em-dash 使用过多暴露 AI 写作痕迹，Limitations 格式不满足 CoRL 2026 硬性要求，且缺少 code/data 释放声明。

## 官方维度打分（基于 CoRL review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Clarity / Presentation | 3/4 (Good) | 叙事主线统一，三个 findings 的逻辑递进合理；但 em-dash 和 -ing phrase 存在 AI 痕迹，部分术语首次出现未定义 |
| Significance | 2/4 (Fair) | 提供设计洞察但无架构干预验证；对 robotics 的直接影响停留在建议层面 |
| Relevance | 3/4 (Good) | 直接分析 robot learning 核心模型(VLA)的内部机制，CoRL 受众会感兴趣 |
| Soundness | 3/4 (Good) | 实验设计严谨（factorial design, bootstrap CI, cross-benchmark），但非写作审查重点 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Limitations 格式不满足 CoRL 2026 硬性要求
- 具体位置：discussion.tex, `\paragraph{Limitations.}`
- 问题：CoRL 2026 Call for Papers 明确要求 "All submissions should include a **Limitations section** (counted toward the 8-page limit), explicitly describing limiting assumptions, failure modes, and other limitations." 当前 Limitations 是 Discussion 内的一个 `\paragraph{}`，不是独立的 `\section{}` 或 `\subsection{}`。
- 此外，CoRL 要求描述 **failure modes**，当前文本只讨论了 generalization scope、statistical power、post-hoc nature，未提及任何 failure mode（如：什么情况下 routing 分析会给出误导性结论？什么输入条件下 inverted-U 可能不成立？）
- 为什么影响接收：格式硬性要求不满足可能导致 desk reject 或被 AC 标记为 non-compliant。
- 建议修改方向：将 Limitations 提升为独立 `\section{Limitations}` 或至少 `\subsection{Limitations}`（放在 Discussion 最后或 Conclusion 之前均可），补充 1-2 个具体 failure mode。

**N2** [critical] Em-dash（---）作为解释性标点使用，是最显著的 AI 写作标志
- 具体位置：
  - experiments.tex L31: `"division of labor---instruction-blind...---means"`
  - experiments.tex L69: `"does not enable routing---architecture provides...---but transforms"`
  - method.tex L19-24: 列表项中 `"DinoSigLIP+Projector---projector output"` 等 4 处
  - appendix.tex L81: `"---consistent with increased task difficulty"`
  - appendix.tex L138: `"---the inverted-U plateau"`
- 问题：正文中至少有 8 处非表格的 `---` em-dash，其中 experiments.tex 两处是典型的解释性双 em-dash pair（parenthetical aside），是 AI 生成文本最容易被审稿人识别的标志。
- 为什么影响接收：CoRL 审稿人若怀疑大量 AI 生成，可能对论文整体质量产生负面偏见；部分会议已开始标记 AI-generated submissions。
- 建议修改方向：
  - experiments.tex L31: 改用逗号或拆分句子："...functional specialization. Instruction-blind image tokens... This means..."
  - experiments.tex L69: 同上，改用括号或分号
  - method.tex 列表项：改用冒号 "(a) DinoSigLIP+Projector: projector output..."
  - appendix 中同理处理

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 术语首次出现未定义
- LOOCV：Abstract 第4行使用 "LOOCV-verified"，但 LOOCV 的全称 "leave-one-out cross-validation" 直到 method.tex §3.3 才给出。Abstract 应自包含。
- MLP：method.tex L10 首次出现 "MLP projector"，未展开为 "multi-layer perceptron"。虽然 ML 社区普遍知道此缩写，但 CoRL 受众包含非 ML 背景的 robotics 研究者。
- CKA：method.tex L58 使用 "CKA~\cite{kornblith2019}" 但主文中未给出全称 "Centered Kernel Alignment"，仅在 appendix.tex L9 定义。
- 建议：在 Abstract 中将 "LOOCV-verified" 改为 "leave-one-out cross-validated" 或去掉（Abstract 用 "cross-validated" 即可）。MLP 和 CKA 在首次出现时展开。

**W2** [warning] 页数可能逼近或超出 8 页限制
- 问题：正文含 5 个 full-column-width figures + 3 个 tables（experiments section），加上 6 个 sections 的文本。按 CoRL 单栏格式粗估：title+abstract(0.5p) + intro(1.2p) + related(0.4p) + method(1.5p) + experiments(4.5p, 含大量浮动体) + discussion(0.8p) + conclusion(0.2p) ≈ 9.1 pages。即使 LaTeX 浮动体优化排版，仍可能超出 8 页。
- 建议：考虑将 Fig 5 (factorial/instruction invariance) 移入 appendix（其信息在 Table 3 中已部分覆盖），或合并 Fig 2 (RSA bar) 与 Fig 3 (layer curves) 为双面板图。编译后确认实际页数。

**W3** [warning] -ing 分词短语结尾（次要 AI 痕迹）
- 具体位置：
  - abstract.tex L6: "exceeding all internal representations"
  - experiments.tex L77 (caption): "creating a robust signal maintained through L31"
  - appendix.tex L81: "requiring deeper processing"
- 问题：虽非密集出现，但审稿人对此模式敏感。每处 -ing 结尾都可以改写为独立短句。
- 建议：逐一改写，如 "exceeding all internal representations" → "which exceeds all internal representations" 或直接重构句式。

**W4** [warning] Related Work 过短
- 具体位置：related_work.tex（仅 16 行源码，3 个 `\paragraph{}`）
- 问题：对于 CoRL 顶会论文，Related Work 只有三小段略显单薄。缺少对以下工作的讨论：(1) NLP 中的 probing 文献更广泛的上下文（如 Hewitt & Manning 2019 structural probes）；(2) attention analysis 在 Transformer 中的已有工作（如 Clark et al. 2019, Vig & Belinkov 2019）；(3) VLA 架构设计的更多工作（如 Octo, CrossFormer 等）。
- 为什么影响评分：审稿人可能认为 literature survey 不充分，positioning 不够明确。
- 建议：扩展至 4-5 段，增加 probing/attention 分析的 NLP 背景和更多 VLA 架构对比。

**W5** [warning] 无 code/data 释放声明
- 问题：CoRL 鼓励 reproducibility。论文未在任何位置声明是否会释放分析代码、提取的表征数据、或 probe 训练脚本。
- 建议：在 Conclusion 或 Limitations 后加一句 reproducibility statement（如 "Code and extracted representations will be released upon acceptance"），注意 double-blind 阶段不要包含任何可识别 URL。

---

## 小问题（不影响接收）

- **Table 2 (tab_rsa_overview)**：$R^2$ 列中 "Fused DinoSigLIP" 显示 `---`（无数据），但未说明为何该 source 未做 probe。Caption 应补充解释或在 footnote 中说明。
- **Introduction L8**: `\cite{grant2026}` 是 2026 年 3 月 arXiv 预印本，作为核心论据（"VLAs rely disproportionately on visual input"）的唯一支撑可能被审稿人质疑其 peer-review 状态。建议同时引用 `\cite{fei2025}` 或 `\cite{hou2026}` 作为补充证据（related_work 中已引但 introduction 未用）。
- **Conclusion**: 结论段几乎逐字重复 abstract 的三个 findings + 最后一句设计建议。虽然不引入新信息是正确的，但完全复述降低了阅读价值。建议 Conclusion 侧重 broader impact 或 future direction 的一句话升华。
- **Figure captions**: Fig 3 和 Fig 5 的 caption 中使用了 LaTeX math-mode 内的数字范围 `L0 $= 0.612 \to$ L12`，视觉上稍显拥挤但不算错误。
- **Appendix 引用完整性**: 主文中 appendix 引用了 `\ref{sec:instruction_invariance_appendix}`（experiments.tex L22）但 appendix.tex 中未见此 label——可能在 Additional RSA Values (§A.4) 中但 label 名不匹配，需确认编译无 undefined reference warning。

---

## 主要优势

- **叙事主线高度统一**：Abstract → Introduction → Experiments → Discussion → Conclusion 围绕同一条 "三个 findings" 主线展开，读者不会迷失。ordering（what → how → geometry）逻辑递进自然。
- **数据呈现严谨**：所有数值均有 confidence interval 或 p-value，Table format 精度统一（3位小数），最优值加粗，caption 基本自包含。
- **Introduction 五段结构完整**：背景(¶1) → 问题重要性(¶1-2) → 现有不足(¶2) → 本文方法(¶3) → 贡献列表(¶4)。每条 contribution 在后文有对应 section 支撑。
- **Abstract 满足四问题要求**：问题(L1)、方法(L2)、findings(L3-7)、implication(L8)，约 200 words，在范围内。
- **匿名化完整**：author 为 "Anonymous"，bib 中无 self-citation 暴露，无 GitHub/institutional URL。

---

## 总结建议

按优先级排序的行动项：
1. 【必须】将 Limitations 提升为独立 section，补充 failure modes
2. 【必须】清除所有解释性 em-dash（至少正文 experiments.tex 2处 + method.tex 4处）
3. 【强烈建议】确认编译后页数 ≤ 8，必要时移动一个 figure 至 appendix
4. 【建议】修复术语定义问题（LOOCV in abstract, MLP, CKA）
5. 【建议】扩展 Related Work
6. 【建议】添加 reproducibility statement

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_3"
}
```

</details>

---


### Tool call

_source line 74 · 2026-05-17T04:37:57.731897+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 2 和 Reviewer 3 的意见\n\n以下是 Reviewer 2 和 Reviewer 3 的完整审稿原文。请对每个 Must-Fix (N) 和 Should-Fix (W) 问题逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 2 的完整审稿意见（4/10, Borderline Reject）\n\n**Must-Fix:**\n\n**N1** [critical] \"First token-level representational decomposition\" claim 不成立\n- Neo et al. (ICLR 2025) 已对 VLM (LLaVA) 做了 token-level 分析；Grant 2026 (Action Atlas) 对 6 个 VLA 做了 per-token SAE 分析（424 SAEs）。本文的 \"first\" claim 需大幅限定或删除。\n\n**N2** [critical] 方法无创新——标准工具 (RSA+probing+attention) 的直接应用\n- 无新 metric、无新实验范式。Cross-instruction probe 本质是标准 linear probe 的 application。对 CoRL 而言缺乏方法贡献。\n\n**N3** [critical] Design implications 完全 speculative，未经验证\n- \"early exit at L12\"、\"vision encoder quality is primary lever\" 均无因果实验支撑。CKA 反转 RSA 排序进一步动摇结论。\n\n**N4** [critical] 单一模型 + 单一 benchmark 家族，泛化性不足\n- Grant 2026 覆盖 6 个模型 + 4 benchmark；本文仅 OpenVLA + LIBERO。\n\n**Should-Fix:**\n\n**W1** Related Work 严重不足（21 篇引用，3 段 15 行）。缺失 Neo et al. (ICLR 2025)、VLM-LENS、logit lens、Raghu et al. 2021 等关键文献。\n**W2** CKA 与 RSA 结论矛盾处理不充分。\n**W3** 核心 RSA 结果（LIBERO-Goal best-vs-best Δ=+0.017）统计不显著。\n**W4** 无 real-robot 实验或 rollout-level behavioral validation。\n\n---\n\n### Reviewer 3 的完整审稿意见（6/10, Weak Accept）\n\n**Must-Fix:**\n\n**N1** Limitations 格式不满足 CoRL 2026 硬性要求——当前是 Discussion 内的 \\paragraph{}，应为独立 section/subsection，且缺少 failure modes 描述。\n**N2** Em-dash (---) 作为解释性标点至少 8 处——AI 写作的最显著标志，需全部清除。\n\n**Should-Fix:**\n\n**W1** 术语首次出现未定义（LOOCV in abstract, MLP, CKA 未在主文展开）\n**W2** 页数可能逼近/超出 8 页限制（估算约 9.1 页）\n**W3** -ing 分词短语结尾（次要 AI 痕迹）\n**W4** Related Work 过短（仅 16 行源码）\n**W5** 无 code/data 释放声明\n\n---\n\n请逐条给出你的 [AGREE] 或 [REBUT] 回应，特别关注：\n1. R2-N1 的 novelty claim 问题——你是否同意 Neo et al. 和 Grant 2026 已涵盖了本文的 token-level 分析？\n2. R2-N2 的方法创新问题——你是否认为 $2\\times 2$ factorial + 四种方法组合构成足够贡献？\n3. R2-N3 与你的 N4（probing encoding ≠ use）是否为同一问题的不同表述？\n4. R3 的格式问题是否影响你对论文科学质量的评估？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 2 和 Reviewer 3 的意见\n\n以下是 Reviewer 2 和 Reviewer 3 的完整审稿原文。请对每个 Must-Fix (N) 和 Should-Fix (W) 问题逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 2 的完整审稿意见（4/10, Borderline Reject）\n\n**Must-Fix:**\n\n**N1** [critical] \"First token-level representational decomposition\" claim 不成立\n- Neo et al. (ICLR 2025) 已对 VLM (LLaVA) 做了 token-level 分析；Grant 2026 (Action Atlas) 对 6 个 VLA 做了 per-token SAE 分析（424 SAEs）。本文的 \"first\" claim 需大幅限定或删除。\n\n**N2** [critical] 方法无创新——标准工具 (RSA+probing+attention) 的直接应用\n- 无新 metric、无新实验范式。Cross-instruction probe 本质是标准 linear probe 的 application。对 CoRL 而言缺乏方法贡献。\n\n**N3** [critical] Design implications 完全 speculative，未经验证\n- \"early exit at L12\"、\"vision encoder quality is primary lever\" 均无因果实验支撑。CKA 反转 RSA 排序进一步动摇结论。\n\n**N4** [critical] 单一模型 + 单一 benchmark 家族，泛化性不足\n- Grant 2026 覆盖 6 个模型 + 4 benchmark；本文仅 OpenVLA + LIBERO。\n\n**Should-Fix:**\n\n**W1** Related Work 严重不足（21 篇引用，3 段 15 行）。缺失 Neo et al. (ICLR 2025)、VLM-LENS、logit lens、Raghu et al. 2021 等关键文献。\n**W2** CKA 与 RSA 结论矛盾处理不充分。\n**W3** 核心 RSA 结果（LIBERO-Goal best-vs-best Δ=+0.017）统计不显著。\n**W4** 无 real-robot 实验或 rollout-level behavioral validation。\n\n---\n\n### Reviewer 3 的完整审稿意见（6/10, Weak Accept）\n\n**Must-Fix:**\n\n**N1** Limitations 格式不满足 CoRL 2026 硬性要求——当前是 Discussion 内的 \\paragraph{}，应为独立 section/subsection，且缺少 failure modes 描述。\n**N2** Em-dash (---) 作为解释性标点至少 8 处——AI 写作的最显著标志，需全部清除。\n\n**Should-Fix:**\n\n**W1** 术语首次出现未定义（LOOCV in abstract, MLP, CKA 未在主文展开）\n**W2** 页数可能逼近/超出 8 页限制（估算约 9.1 页）\n**W3** -ing 分词短语结尾（次要 AI 痕迹）\n**W4** Related Work 过短（仅 16 行源码）\n**W5** 无 code/data 释放声明\n\n---\n\n请逐条给出你的 [AGREE] 或 [REBUT] 回应，特别关注：\n1. R2-N1 的 novelty claim 问题——你是否同意 Neo et al. 和 Grant 2026 已涵盖了本文的 token-level 分析？\n2. R2-N2 的方法创新问题——你是否认为 $2\\times 2$ factorial + 四种方法组合构成足够贡献？\n3. R2-N3 与你的 N4（probing encoding ≠ use）是否为同一问题的不同表述？\n4. R3 的格式问题是否影响你对论文科学质量的评估？"
  }
}
```

</details>

---


### Tool result

_source line 75 · 2026-05-17T04:38:16.769572+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19037
}
```

</details>

---


### Tool call

_source line 76 · 2026-05-17T04:38:17.070701+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 1 和 Reviewer 3 的意见\n\n以下是 Reviewer 1 和 Reviewer 3 的完整审稿原文。请对每个 Must-Fix (N) 和 Should-Fix (W) 问题逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 的完整审稿意见（5/10, Marginally below acceptance）\n\n**Must-Fix:**\n\n**N1** [critical] Untrained control 不能隔离 VLA fine-tuning 的贡献\n- Random weights vs trained 混淆了 Llama-2 语言预训练 vs VLA fine-tuning。需增加 Llama-2 base checkpoint 作为中间对照。\n\n**N2** [critical] 单一模型 + 单一 benchmark family 无法支撑 \"VLAs\" 的一般性结论\n- Title/Abstract 用复数 \"VLAs\"，但仅测试 OpenVLA-7B + LIBERO。\n\n**N3** [critical] RSA best-vs-best 比较存在 selection bias\n- 32 层取 max 有正偏置(winner's curse)；主 benchmark 结果 n.s.；用 LIBERO-Spatial 显著性来 rescue Goal 的零结果方法论不成立。\n\n**N4** [critical] Probing 的 encoding ≠ use\n- MLP probe R² 证明 information extractable，不证明 model uses it。\"Vision encoder is primary lever\" 缺乏因果支撑。\n\n**Should-Fix:**\n\n**W1** \"Instruction-blind\" claim 过强——chance-level linear probe ≠ no instruction information。未测 MLP probe on instruction classification。\n**W2** CKA 与 RSA 结论矛盾处理不充分。\n**W3** Attention analysis 仅限 L1，可能存在选择性报告。\n**W4** LOOCV 100%±0.00 的统计检验力问题——4096-D 做 10-way classification 可能对 random features 也接近 100%。\n**W5** 数据规模（500 demos）对 peak layer 精确位置的影响。\n\n---\n\n### Reviewer 3 的完整审稿意见（6/10, Weak Accept）\n\n**Must-Fix:**\n\n**N1** Limitations 格式不满足 CoRL 2026 硬性要求。\n**N2** Em-dash (---) 作为解释性标点至少 8 处（AI 写作标志）。\n\n**Should-Fix:**\n\n**W1** 术语首次出现未定义（LOOCV, MLP, CKA）\n**W2** 页数可能超出 8 页（估算 ~9.1 页）\n**W3** -ing 分词短语结尾\n**W4** Related Work 过短\n**W5** 无 code/data 释放声明\n\n---\n\n请逐条给出你的 [AGREE] 或 [REBUT] 回应，特别关注：\n1. R1-N1 的 untrained baseline 问题——你是否同意这比你提出的 N4（单模型泛化性）更根本？\n2. R1-N3 的 statistical bias 问题——你的 W3 也提到 RSA n.s.，是否同意 R1 对 selection bias 的分析？\n3. R1-W1 的 \"instruction-blind\" claim——这与你对 novelty 的评估有何关联？\n4. R3 的格式问题是否会改变你的整体评分？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 1 和 Reviewer 3 的意见\n\n以下是 Reviewer 1 和 Reviewer 3 的完整审稿原文。请对每个 Must-Fix (N) 和 Should-Fix (W) 问题逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 的完整审稿意见（5/10, Marginally below acceptance）\n\n**Must-Fix:**\n\n**N1** [critical] Untrained control 不能隔离 VLA fine-tuning 的贡献\n- Random weights vs trained 混淆了 Llama-2 语言预训练 vs VLA fine-tuning。需增加 Llama-2 base checkpoint 作为中间对照。\n\n**N2** [critical] 单一模型 + 单一 benchmark family 无法支撑 \"VLAs\" 的一般性结论\n- Title/Abstract 用复数 \"VLAs\"，但仅测试 OpenVLA-7B + LIBERO。\n\n**N3** [critical] RSA best-vs-best 比较存在 selection bias\n- 32 层取 max 有正偏置(winner's curse)；主 benchmark 结果 n.s.；用 LIBERO-Spatial 显著性来 rescue Goal 的零结果方法论不成立。\n\n**N4** [critical] Probing 的 encoding ≠ use\n- MLP probe R² 证明 information extractable，不证明 model uses it。\"Vision encoder is primary lever\" 缺乏因果支撑。\n\n**Should-Fix:**\n\n**W1** \"Instruction-blind\" claim 过强——chance-level linear probe ≠ no instruction information。未测 MLP probe on instruction classification。\n**W2** CKA 与 RSA 结论矛盾处理不充分。\n**W3** Attention analysis 仅限 L1，可能存在选择性报告。\n**W4** LOOCV 100%±0.00 的统计检验力问题——4096-D 做 10-way classification 可能对 random features 也接近 100%。\n**W5** 数据规模（500 demos）对 peak layer 精确位置的影响。\n\n---\n\n### Reviewer 3 的完整审稿意见（6/10, Weak Accept）\n\n**Must-Fix:**\n\n**N1** Limitations 格式不满足 CoRL 2026 硬性要求。\n**N2** Em-dash (---) 作为解释性标点至少 8 处（AI 写作标志）。\n\n**Should-Fix:**\n\n**W1** 术语首次出现未定义（LOOCV, MLP, CKA）\n**W2** 页数可能超出 8 页（估算 ~9.1 页）\n**W3** -ing 分词短语结尾\n**W4** Related Work 过短\n**W5** 无 code/data 释放声明\n\n---\n\n请逐条给出你的 [AGREE] 或 [REBUT] 回应，特别关注：\n1. R1-N1 的 untrained baseline 问题——你是否同意这比你提出的 N4（单模型泛化性）更根本？\n2. R1-N3 的 statistical bias 问题——你的 W3 也提到 RSA n.s.，是否同意 R1 对 selection bias 的分析？\n3. R1-W1 的 \"instruction-blind\" claim——这与你对 novelty 的评估有何关联？\n4. R3 的格式问题是否会改变你的整体评分？"
  }
}
```

</details>

---


### Tool result

_source line 77 · 2026-05-17T04:38:30.090287+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 13019
}
```

</details>

---


### Tool call

_source line 78 · 2026-05-17T04:38:30.446323+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "3",
  "round_number": "1",
  "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 1 和 Reviewer 2 的意见\n\n以下是 Reviewer 1 和 Reviewer 2 的完整审稿原文。请对每个 Must-Fix (N) 和 Should-Fix (W) 问题逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 的完整审稿意见（5/10, Marginally below acceptance）\n\n**Must-Fix:**\n\n**N1** [critical] Untrained control 不能隔离 VLA fine-tuning 的贡献\n- Random weights vs trained 混淆 Llama-2 预训练 vs VLA fine-tuning。\n\n**N2** [critical] 单一模型 + 单一 benchmark 无法支撑 \"VLAs\" 的一般性结论。\n\n**N3** [critical] RSA best-vs-best 存在 selection bias（32 层取 max 有正偏置；n.s. result）。\n\n**N4** [critical] Probing encoding ≠ use；\"vision encoder is primary lever\" 缺乏因果证据。\n\n**Should-Fix:**\n\n**W1** \"Instruction-blind\" claim 过强。\n**W2** CKA 与 RSA 矛盾处理不充分。\n**W3** Attention 仅 L1，选择性报告嫌疑。\n**W4** LOOCV 100% 的统计检验力问题。\n**W5** 数据规模对 peak layer 位置的影响。\n\n---\n\n### Reviewer 2 的完整审稿意见（4/10, Borderline Reject）\n\n**Must-Fix:**\n\n**N1** [critical] \"First token-level decomposition\" claim 不成立——Neo et al. (ICLR 2025) 和 Grant 2026 已有类似分析。\n\n**N2** [critical] 无方法论创新——标准工具直接应用。\n\n**N3** [critical] Design implications 完全 speculative，未验证。CKA 反转 RSA。\n\n**N4** [critical] 单模型单 benchmark 泛化性不足。\n\n**Should-Fix:**\n\n**W1** Related Work 严重不足（21 引用，3 段 15 行），缺失关键文献（Neo et al., logit lens, Raghu et al.）。\n**W2** CKA 与 RSA 矛盾。\n**W3** 核心 RSA 结果 n.s.。\n**W4** 无 real-robot 或 rollout-level 实验。\n\n---\n\n请逐条给出你的 [AGREE] 或 [REBUT] 回应，特别关注：\n1. R1-N1 的 untrained baseline 缺陷——从写作/呈现角度，这是否也构成叙事连贯性问题？（论文声称 \"training learns routing\" 但实际分离的可能只是 language pretraining）\n2. R2-N2 的方法创新问题——作为写作评审，你是否认为没有方法创新的分析论文能通过清晰的 framing 和呈现来弥补？\n3. R1-N2 和 R2-N4 都关注泛化性——title/abstract 中的 \"VLAs\"（复数）在写作层面是否构成 overclaim？\n4. R2-W1 与你的 W4 都指出 Related Work 不足——从写作规范看，当前密度是否达到 CoRL 论文的下限？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "3",
    "round_number": "1",
    "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 1 和 Reviewer 2 的意见\n\n以下是 Reviewer 1 和 Reviewer 2 的完整审稿原文。请对每个 Must-Fix (N) 和 Should-Fix (W) 问题逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 的完整审稿意见（5/10, Marginally below acceptance）\n\n**Must-Fix:**\n\n**N1** [critical] Untrained control 不能隔离 VLA fine-tuning 的贡献\n- Random weights vs trained 混淆 Llama-2 预训练 vs VLA fine-tuning。\n\n**N2** [critical] 单一模型 + 单一 benchmark 无法支撑 \"VLAs\" 的一般性结论。\n\n**N3** [critical] RSA best-vs-best 存在 selection bias（32 层取 max 有正偏置；n.s. result）。\n\n**N4** [critical] Probing encoding ≠ use；\"vision encoder is primary lever\" 缺乏因果证据。\n\n**Should-Fix:**\n\n**W1** \"Instruction-blind\" claim 过强。\n**W2** CKA 与 RSA 矛盾处理不充分。\n**W3** Attention 仅 L1，选择性报告嫌疑。\n**W4** LOOCV 100% 的统计检验力问题。\n**W5** 数据规模对 peak layer 位置的影响。\n\n---\n\n### Reviewer 2 的完整审稿意见（4/10, Borderline Reject）\n\n**Must-Fix:**\n\n**N1** [critical] \"First token-level decomposition\" claim 不成立——Neo et al. (ICLR 2025) 和 Grant 2026 已有类似分析。\n\n**N2** [critical] 无方法论创新——标准工具直接应用。\n\n**N3** [critical] Design implications 完全 speculative，未验证。CKA 反转 RSA。\n\n**N4** [critical] 单模型单 benchmark 泛化性不足。\n\n**Should-Fix:**\n\n**W1** Related Work 严重不足（21 引用，3 段 15 行），缺失关键文献（Neo et al., logit lens, Raghu et al.）。\n**W2** CKA 与 RSA 矛盾。\n**W3** 核心 RSA 结果 n.s.。\n**W4** 无 real-robot 或 rollout-level 实验。\n\n---\n\n请逐条给出你的 [AGREE] 或 [REBUT] 回应，特别关注：\n1. R1-N1 的 untrained baseline 缺陷——从写作/呈现角度，这是否也构成叙事连贯性问题？（论文声称 \"training learns routing\" 但实际分离的可能只是 language pretraining）\n2. R2-N2 的方法创新问题——作为写作评审，你是否认为没有方法创新的分析论文能通过清晰的 framing 和呈现来弥补？\n3. R1-N2 和 R2-N4 都关注泛化性——title/abstract 中的 \"VLAs\"（复数）在写作层面是否构成 overclaim？\n4. R2-W1 与你的 W4 都指出 Related Work 不足——从写作规范看，当前密度是否达到 CoRL 论文的下限？"
  }
}
```

</details>

---


### Tool result

_source line 79 · 2026-05-17T04:38:31.907588+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_3\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1461
}
```

</details>

---


### Assistant

_source line 80 · 2026-05-17T04:38:34.966394+00:00_

交叉分享已发出。等待三位 Reviewer 的逐条 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 7

## Round 7

2 recorded events


### User

_source line 81 · 2026-05-17T04:38:37.580361+00:00_

[Reviewer 3 审稿结果]:
审稿报告已提交给 Review Director。

主要发现：
- **2 个 Must-Fix**：Limitations 格式不满足 CoRL 2026 硬性要求（需独立 section + failure modes）；正文 8 处 em-dash 是显著 AI 写作痕迹
- **5 个 Should-Fix**：术语未定义（LOOCV/MLP/CKA）、页数可能超限、-ing phrase 结尾、Related Work 过短、无 code/data 释放声明
- **优势**：叙事主线统一、数据呈现严谨、Introduction 结构完整、匿名化合规

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_3"
}
```

</details>

---


### Assistant

_source line 82 · 2026-05-17T04:38:43.525862+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 8

## Round 8

2 recorded events


### User

_source line 83 · 2026-05-17T04:40:09.196121+00:00_

[Reviewer 1 审稿意见]:
## Step 2 交叉回应 — Reviewer 1 对 Reviewer 2 & Reviewer 3 意见的逐条回应

---

### 对 Reviewer 2 的回应

**[AGREE] R2-N1: "First token-level representational decomposition" claim 过强**

同意该 claim 需要限定，但程度上与 R2 有分歧。

理由：
- Neo et al. (ICLR 2025) 分析的是 VLM (LLaVA)，不是 VLA。VLM 不产生 action，没有 action-relevant geometry 的概念，其 token-level 分析的目标和方法框架与本文不同。因此 Neo et al. 不直接 invalidate 本文对 VLA 的 "first" claim。
- Grant 2026 (Action Atlas) 使用 SAE 做 per-token 分析，确实是 VLA 的 token-level 分析。但 SAE 找 sparse directions 与本文的 multi-metric decomposition（RSA geometric alignment + probe decodability + attention routing + cross-instruction encoding）是不同的分析框架。
- 建议将 claim 限定为 "first systematic multi-metric token-level decomposition with trained/untrained controls"，而非 blanket "first token-level decomposition"。

**[REBUT] R2-N2: 方法无创新**

部分反驳。

理由：
- 同意单个工具（RSA、probing、attention visualization）均非新方法。但 R2 低估了实验设计的贡献：2×2 factorial (training status × instruction presence) 交叉 token position (image vs. readout) 交叉 layer depth (32 layers)，这个三维分解框架本身是分析设计上的贡献，不是 "标准工具的直接应用"。
- Cross-instruction probe 的设计（同一 visual frame × 10 instructions，测试哪个 token type 编码 instruction identity）虽然在方法上是 linear probe，但其实验逻辑（通过 instruction 交叉来隔离 token-level specialization）在 VLA 文献中未见先例。
- 然而，我承认对 CoRL 而言，纯分析论文（no new algorithm, no new system, no architectural intervention）确实面临更高的 bar。CoRL 审稿标准强调 "significance and novelty of results, either theoretical or empirical"——如果结论本身足够 significant 且 well-supported，分析贡献是可以被接受的。但问题在于结论是否 well-supported（见我的 N1-N4），这才是核心矛盾。
- 总结：方法新颖性确实不高（5/10），但这不应该是 rejection 的主要理由——结论的可靠性才是。

**[AGREE] R2-N3: Design implications 完全 speculative**

强烈同意。这与我的 N4 是同一问题的不同表述。

理由：
- 我的 N4 指出：probe R² 和 RSA ρ 证明 information extractability / geometric alignment，不证明 causal contribution to action generation。论文却据此给出 "vision encoder quality is the primary design lever" 和 "action heads should read from L12-L13" 等因果性设计建议。
- R2 补充的 CKA 反转论证进一步强化这一点：如果 metric 选择就能翻转 "哪个 encoder 最好" 的结论（RSA: DINOv2 > trained > CLIP；CKA: untrained > trained > DINOv2），那么基于单一 metric 的设计建议毫无可操作性。
- 这是本文最严重的问题之一：分析工作的价值在于 insights，如果 insights 不可靠或不可操作，论文的 significance 大打折扣。

**[AGREE] R2-N4: 单一模型 + 单一 benchmark 家族**

完全同意，与我的 N2 一致。

补充一点：R2 提到 Grant 2026 覆盖 6 个模型 + 4 benchmark。如果直接竞争者已经做到了更广覆盖度，本文单一模型的分析深度必须远超 Grant 2026 才能 justify——但目前 N1（baseline 缺陷）和 N4（无因果验证）削弱了这种深度优势。

**[AGREE] R2-W1: Related Work 过短，缺失关键引用**

同意。

Related Work 仅 3 段 ~16 行（Section 2），引用 21 篇。对于一篇分析论文而言，Related Work 应该更详尽地 positioning：
- 缺失 VLM token-level 分析文献（Neo et al.）
- 缺失 representation analysis 方法论文献（logit lens、Raghu et al. 2021 CKA-based layer analysis）
- 缺失 neuroscience-inspired probing 的局限性讨论（Hewitt & Liang 2019 control tasks）
- 引用密度明显低于 CoRL 近年录用论文的水平

**[AGREE] R2-W2: CKA 与 RSA 矛盾处理不充分**

完全同意，与我的 W2 一致。不再重复。

**[AGREE] R2-W3: 核心 RSA 结果统计不显著**

同意，与我的 N3 一致。这不仅是 "should-fix"——一个核心定量 claim 的 p-value 不显著且 CI 包含 0，却在叙事中被积极解读，这动摇了论文的 rigor。我将其放在 Must-Fix 级别。

**[REBUT] R2-W4: 无 real-robot 实验**

部分反驳。

理由：
- 本文定位为 representation analysis / mechanistic understanding paper，不是 systems paper。要求 real-robot rollout 等于要求分析论文同时做 system contribution，这超出了论文的 scope。
- 但 R2 的 underlying concern 是合理的：论文的设计建议（"optimize routing"、"early exit at L12"）如果加一个 proof-of-concept intervention（哪怕在 simulation 中），说服力会大幅提升。这不需要 real robot——在 LIBERO 中实现 early-exit action head 并测 task success rate 就足够了。
- 因此我将其归类为 "强烈建议但非必须"：如果作者能在 rebuttal 期间添加一个 simulation-based intervention（如 early exit），论文的 significance 可以从 5/10 提升到 7/10。

---

### 对 Reviewer 3 的回应

**[AGREE] R3-N1: Limitations 格式不满足 CoRL 2026 要求**

同意这是合规问题。

理由：
- 当前 Limitations 是 Discussion (Section 5) 内的 `\paragraph{Limitations.}`，不是独立 section/subsection。
- CoRL 2026 明确要求 "必须含 Limitations section（计入 8 页）"。格式不合规有 desk reject 风险。
- 但这是 trivially fixable（改为 `\subsection{Limitations}` 或独立 `\section{Limitations}`），不影响科学质量评估。
- 关于缺少 failure modes：同意。当前 Limitations 只讨论了泛化性和方法论局限，没有具体描述分析可能 fail 的场景（如 when would the inverted-U not hold? What architectural features would break token specialization?）。

**[AGREE] R3-N2: Em-dash 作为 AI 写作标志需清除**

同意，但对 "critical" 级别有异议。

理由：
- 确实在 tex 源码中观察到解释性 em-dash（如 Section 4.1 "instruction-blind image tokens and instruction-conditioned readout token---means the readout token is the sole locus"）。
- 这是 presentation issue，不是 scientific issue。对论文是否应被接收的判断应基于 contribution quality，不是排版风格。
- 但 R3 的 underlying logic 有一定道理：如果审稿人怀疑论文大量使用 AI 生成，会降低对 intellectual contribution 的信任。在 double-blind review 中这确实可能影响评分。
- 建议作者清除所有解释性 em-dash，但不应列为 "Must-Fix affecting acceptance decision"。

**[AGREE] R3-W1: 术语首次出现未定义**

同意。LOOCV 在 Abstract 中使用但未展开（Leave-One-Out Cross-Validation），MLP 首次出现在 Section 3.6 但未展开（Multi-Layer Perceptron），CKA 在正文 Section 3.6 引用但仅在 Appendix 展开（Centered Kernel Alignment）。这是基本写作规范问题，容易修复。

**[REBUT] R3-W2: 页数可能超出 8 页**

无法确认，暂不同意。

理由：
- 没有编译后的 PDF，无法验证。R3 估算 "约 9.1 页" 但未说明估算方法。
- 正文含 6 个 section（Introduction、Related Work、Method、Experiments、Discussion、Conclusion），其中 Related Work 仅 16 行，Discussion 含 Limitations 但不长。6 个 figure + 3 个 table 确实占空间较大。
- 如果确实超页，这是 desk-reject 级问题。但在未编译验证前，我不将其列为 confirmed issue。建议作者自查并压缩（如将 Fig 5 的两个 panel 合并、缩小 Table 2）。

**[AGREE] R3-W3: -ing 分词短语结尾**

同意是 minor AI 风格痕迹，但优先级远低于科学问题。

**[AGREE] R3-W4: Related Work 过短**

同意，与 R2-W1 一致。

**[AGREE] R3-W5: 无 code/data 释放声明**

同意，我在 minor issues 中也提到了这一点。CoRL 鼓励 reproducibility，缺少声明是减分项。

---

### Director 提出的四个具体问题

**Q1: R2-N1 的 novelty claim——Neo et al. 和 Grant 2026 是否已涵盖本文的 token-level 分析？**

不完全涵盖，但 "first" claim 确实过强。
- Neo et al. 分析 VLM 不是 VLA，目标不同（visual QA vs. action generation），不直接覆盖本文工作。
- Grant 2026 的 SAE 分析是 per-token 的但方法框架不同（feature discovery vs. multi-metric decomposition with controlled ablation）。
- 本文的 specific novelty 在于：(1) trained vs. untrained 对照；(2) image vs. readout token 的系统对比；(3) 四种 metric 的交叉验证。这些 Grant 2026 没有做。
- 但 "first token-level decomposition" 作为 absolute novelty claim 不成立。应改为 conditional claim。

**Q2: 2×2 factorial + 四种方法组合是否构成足够贡献？**

作为分析设计贡献，有价值但不充分独立支撑 acceptance。
- 如果结论可靠且 impactful，实验设计的系统性足以构成贡献（类似 neuroscience 中 well-designed but standard-tool 的分析论文）。
- 但当前结论可靠性受 N1（baseline 缺陷）和 N3/N4（no causal validation）严重削弱。如果结论不可靠，再好的实验设计也无法 save 论文。
- 对 CoRL 而言，分析论文的 bar 是：insights 必须直接可操作。当前 insights 的 actionability 存疑。

**Q3: R2-N3 与我的 N4 是否为同一问题？**

是同一问题的不同表述。
- 我的 N4：probing encoding ≠ functional use → 因果设计建议缺乏支撑。
- R2-N3：design implications completely speculative → 无因果实验验证。
- 两者都指向：correlational representation analysis → causal architectural recommendations 的推理跳跃无 justification。
- 这是本文最核心的 weakness：分析做得系统，但 so what? 如果不能可靠地转化为可验证的设计原则，论文的 practical significance 大打折扣。

**Q4: R3 的格式问题是否影响科学质量评估？**

不影响科学质量评估，但影响 acceptance probability。
- Limitations 格式（R3-N1）：合规问题，trivially fixable，不反映科学 rigor。
- Em-dash（R3-N2）：presentation issue，不影响方法和结论的有效性。
- 但两者结合如果导致 desk-reject 或降低审稿人初始印象，则间接影响 acceptance。
- 我的评分（5/10）完全基于科学问题（N1-N4），不受格式影响。即使所有格式问题修复，我的评分不会因此提高。

---

### 总结：三位 Reviewer 的共识问题

| 问题 | R1 | R2 | R3 |
|------|----|----|-----|
| 单一模型泛化性不足 | N2 (critical) | N4 (critical) | — |
| 设计建议缺乏因果支撑 | N4 (critical) | N3 (critical) | — |
| Related Work 过短 | — | W1 | W4 |
| CKA/RSA 矛盾 | W2 | W2 | — |
| 无 code/data 声明 | minor | — | W5 |

三位 Reviewer 的共识 critical issue：(1) 泛化性不足；(2) 因果验证缺失。这两个问题如果不能在 rebuttal 中实质性解决（而非仅限定 claim），论文难以达到 acceptance threshold。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 84 · 2026-05-17T04:40:15.371790+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 9

## Round 9

2 recorded events


### User

_source line 85 · 2026-05-17T04:40:17.961851+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。核心判断：与 R2 在泛化性不足和因果验证缺失上达成共识（两项 critical），对 R2-N2（方法无创新）和 R2-W4（需要 real-robot）部分反驳，对 R3 的格式问题全部同意但不认为影响科学质量评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 86 · 2026-05-17T04:40:27.392404+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 10

## Round 10

2 recorded events


### User

_source line 87 · 2026-05-17T04:41:12.939226+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Step 2 交叉回应（R1 + R3）

### 回应 Reviewer 1

**[AGREE] R1-N1: Untrained control 不能隔离 VLA fine-tuning 的贡献**
同意，且认为这比我的 N4（单模型泛化性）更根本。Random weights vs trained 混淆了 Llama-2 语言预训练和 VLA fine-tuning。25/32 heads 翻转为 instruction-dominant 可能是语言预训练的产物而非 VLA-specific learning。需要三级对照：random → Llama-2 base → VLA。这是 internal validity 问题，动摇论文核心叙事。

**[AGREE] R1-N2: 单模型 + 单 benchmark 无法支撑一般性结论**
同意。补充：Grant 2026 Action Atlas 已在 6 个 VLA 模型上做了类似分析，本文应引用作为跨模型支持证据。

**[AGREE] R1-N3: RSA best-vs-best selection bias**
完全同意。32 层取 max 有 winner's curse；用 LIBERO-Spatial 显著性 rescue Goal 的 null 是 post-hoc rationalization。应报告 FDR-corrected 或 permutation-based max-statistic。

**[AGREE] R1-N4: Probing encoding ≠ use**
同意。Discussion 承认 encoding ≠ use，但随即做出因果性设计建议（"vision encoder quality is the primary design lever"），构成内部矛盾。

**[AGREE] R1-W1: "Instruction-blind" claim 过强**
同意，且直接影响 novelty。未用 MLP probe 测 instruction classification on image tokens。如果 nonlinear probe 能超越 chance，"strict" specialization 弱化为 "predominantly visual"，与 Grant 2026 behavioral findings 的区分度降低。

**[AGREE] R1-W2: CKA 与 RSA 矛盾**
同意。两个标准度量给出相反结论，仅选择支持叙事的指标构成 confirmation bias。

**[REBUT] R1-W3: Attention analysis 仅限 L1**
部分不同意。L1 是 instruction info 首次流入 readout 的位置（L0=chance, L1=100%），分析这层逻辑自洽。但直接展示 L16/L31 attention pattern 会更有说服力。

**[REBUT] R1-W4: LOOCV 100% 的统计检验力**
部分不同意。Image_mean（同为 4096-D）在所有层 = 10%，反证高维度本身不足以解释 100%。真正的区分力来自 routing mechanism。但同意 100%±0.00 说明 task 太 easy，QA probe（86.3% vs 82.7%）是更 informative 的证据。

**[AGREE] R1-W5: 数据规模影响**
部分同意。Appendix Table 8 显示 peak region 稳定但精确位置敏感。应弱化为 "L8-L16 plateau"。

---

### 回应 Reviewer 3

**[AGREE] R3-N1: Limitations 格式违规** — 需从 \paragraph 改为 \section，格式问题可快速修复。

**[AGREE] R3-N2: Em-dash** — 确实存在，但我认为应为 Should-Fix 而非 Must-Fix。

**[AGREE] R3-W1-W5** — 全部同意：术语未定义、页数可能超限、-ing 短语、Related Work 过短（强烈同意，遗漏 Neo et al. ICLR 2025 等关键工作）、无 code 释放声明。

---

### Director 四个问题的直接回答

**Q1**: 是的，R1-N1 比我的 N4 更根本。N4 是 external validity（能否推广），N1 是 internal validity（核心 claim 的因果归因是否成立）。

**Q2**: 完全同意 R1 对 selection bias 的分析。我原来将 RSA n.s. 视为 underpowered，R1 指出这可能是 effect doesn't exist + selection bias 的叠加。

**Q3**: 如果 "strict specialization" 弱化，novelty 从 "revealing unexpected strict separation" 降级为 "confirming known dominance at representation level with standard tools"。方法论层面的 "first decomposition" 仍成立，但 surprise value 降低。

**Q4**: R3 格式问题不改变科学评分，但页数超限 + Limitations 格式不符有 desk-reject 风险。

---

### 评估更新

综合 R1+R3 后：
- **Novelty**: moderate → incremental（R1-N1 confound + W1 overclaim）
- **Soundness**: adequate → below threshold（N1 + N3 + N4 叠加）
- **Overall**: 维持 5/10 (marginally below acceptance)。如修复 R1-N1（加 Llama-2 base 对照）+ 弱化 overclaims，可升至 6/10。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 88 · 2026-05-17T04:41:19.868648+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 11

## Round 11

6 recorded events


### User

_source line 89 · 2026-05-17T04:41:20.879559+00:00_

[Reviewer 3 审稿结果]:
逐条回应如下。

---

## 对 Reviewer 1 的逐条回应

### R1-N1: Untrained control 不能隔离 VLA fine-tuning 的贡献

**[AGREE]** 这也是一个**叙事连贯性问题**。

论文的核心叙事是 "training learns deliberate instruction routing"（§4.2 标题、Abstract L5、Conclusion L6），但 "trained" = Llama-2 pretrained + VLA fine-tuned，而 "untrained" = random weights。这意味着论文无法区分：是 VLA fine-tuning 创建了 routing，还是 Llama-2 的 language pretraining 已经具备这种能力。

从写作角度，这构成 **framing 与证据的错位**：
- Abstract/Intro/Discussion 的叙事暗示 "VLA training"（即 robot demonstration fine-tuning）是关键变量
- 但实际 experimental design（§3.1, method.tex L12: "reinitializing all LLM parameters via `from_config()`"）分离的是 "any pretrained weights vs random"
- 一个中间 baseline（Llama-2 pretrained but not VLA fine-tuned）缺失，使得核心 claim "training learns routing" 的 "training" 指代模糊

Limitations（discussion.tex ¶5）未提及这一混淆。如果 Llama-2 pretrained-only 也展现 25/32 instruction-dominant heads，那么 "training learns" 的叙事会彻底瓦解。

---

### R1-N2: 单一模型 + 单一 benchmark 无法支撑 "VLAs" 一般性结论

**[AGREE]** 从写作层面，这构成 **title/abstract overclaim**。

- Title: "A Representational Decomposition of **Vision-Language-Action Models**"（类属名词，暗示一般性）
- Abstract L8: "**VLA architectures** should optimize routing..."（一般性设计建议）
- Discussion §5 ¶4: "Three practical considerations emerge"（泛化性建议语气）

但证据仅来自 OpenVLA-7B（一个特定架构：DinoSigLIP + Llama-2）在 LIBERO（tabletop manipulation）上的分析。Limitations 虽然承认了这一点（discussion.tex ¶5 L26），但 title 和 abstract 的 framing 并未反映这一限制。

建议：Title 改为 "...of a Vision-Language-Action Model" 或 "...of OpenVLA"，abstract 最后一句加限定词 "In this architecture, ..."。

---

### R1-N3: RSA best-vs-best selection bias

**[REBUT]** R1-N3-Issue-N3: 论文对此处理是**透明且合理的**。

论文在 experiments.tex L100 明确报告 CI includes zero 并标注 n.s.，随后用 LIBERO-Spatial（Appendix §A.5, $\Delta = +0.023$, $p < 0.001$）作为 replication。Table 3（tab_training_effects）同时报告了 same-layer comparison（L12 trained vs untrained, $\Delta = +0.079$, $p < 0.0001$），这消除了 selection bias（同层无 max 选择）。

从呈现角度，论文的处理符合最佳实践：报告 n.s. → 提供解释 → 用独立数据 replicate。不过，R1 的担忧确有道理——main text 应更早、更显著地呈现 same-layer comparison 的 significance，而非以 best-vs-best 作为 primary framing。

---

### R1-N4: Probing ≠ causal use；"vision encoder is primary lever" 缺乏因果证据

**[AGREE]** 从写作角度，这是 **claim 强度与证据类型的错配**。

- Abstract L8: "VLA architectures **should** optimize routing; vision encoder quality **is** the primary design lever."
- Discussion §5 ¶4: 三条 "practical considerations" 以祈使语气呈现

但支撑这些 design implications 的只有 correlational evidence（RSA, probes）。Limitations（discussion.tex L27）承认 "RSA does not establish causal contribution"，但这一 caveat 与 abstract/discussion 中未加限定的祈使语气不一致。

建议：在 abstract 最后一句和 discussion implications 段加 hedge（"Our results suggest that..." / "These correlational findings indicate that..."），或在 discussion 中明确声明 "验证这些 implications 需要架构干预实验"。

---

### R1-W1: "Instruction-blind" claim 过强

**[AGREE]** 从呈现精度看，"instruction-blind" 和 "purely visual"（experiments.tex L19, L31）语言过强。

证据是 **linear** classifier 在 image_mean 上为 chance（§3.3: "A linear classifier (10-way)"）。如果 instruction 信息以非线性方式编码在 image tokens 中，线性 probe 会 miss 它。论文用 MLP probe 预测 action（§3.6）但用 linear probe 检测 instruction——方法不对称削弱了 "purely visual" 的 claim。

建议改为 "instruction information is not linearly accessible from image tokens" 或 "image tokens show no linearly decodable instruction signal"。

---

### R1-W2: CKA 与 RSA 矛盾处理不充分

**[AGREE]** 这也是一个**呈现问题**。

主文 method.tex L58 仅一句 "CKA results are reported in Appendix"，但 CKA 反转了核心结论之一（DINOv2 最优 → CKA 下 DINOv2 最差，appendix.tex L21-22）。当两个度量对同一核心 claim 给出相反结论时，将不利证据完全放入 appendix 有 **selective reporting** 的外观。

建议：在 main text §4.3 或 Discussion 中加 1-2 句承认 CKA divergence 并解释为何 RSA 更适合本文问题（rank-order alignment vs global covariance structure）。

---

### R1-W3: Attention 仅 L1，选择性报告嫌疑

**[REBUT]** R1-W3-Issue-W3: L1 的选择有合理的 **data-driven justification**。

Cross-instruction probe 显示 L0→L1 是 step-function onset（Table 1: 10% → 100%），说明 routing 发生在 L1。分析 routing mechanism 自然应在 routing 发生的层。论文在 §4.2 ¶2（experiments.tex L65）解释了这一逻辑。

不过，从呈现完整性角度，加一句解释为何不报告更深层 attention（"deeper layers have residual connections that make attention less interpretable as information flow"）会预防这一质疑。

---

### R1-W4: LOOCV 100% 的统计检验力问题

**[AGREE]** 从呈现角度，100% accuracy with zero variance 的 "validation" 实际上证明了**任务过于简单**而非模型能力强。

10-way classification over 10 highly distinct task instructions（每个 instruction 是完全不同的自然语言句子）对 frozen tokenizer embeddings 来说可能是 trivially separable。这削弱了 "LOOCV-verified" 作为方法论 rigor 标志的说服力。论文应在呈现时 acknowledge 任务难度，而非将 100% accuracy 作为 robustness 的证据。

---

### R1-W5: 数据规模对 peak layer 位置的影响

**[REBUT]** R1-W5-Issue-W5: 论文已在 Appendix §A.7（appendix.tex Table 8, L139-161）充分处理。

Demo subsampling（50→25）保持 RSA peak at L12（profile $r = 0.970$），R² peak 从 L9→L11（within plateau）。这是合理的 robustness check，且结果支持稳定性。从呈现角度，主文 experiments.tex L109 也提到了 "replicate under halved demonstration counts"。

---

## 对 Reviewer 2 的逐条回应

### R2-N1: "First token-level decomposition" claim 不成立

**[AGREE]** 从写作规范看，未经充分文献调研的 "first" claim 是**高风险 framing**。

论文 Introduction L27 和 Conclusion L2 均使用 "the first token-level representational decomposition of a VLA"。如果 Neo et al. (ICLR 2025) 已做了类似 token-level analysis（且 references.bib 中未见 "Neo" 条目），这构成：
1. Related Work 调研遗漏
2. Novelty claim 不成立
3. 审稿人信任度下降

建议：(1) 确认 Neo et al. 的具体内容后决定是否保留 "first" claim；(2) 如果确实有 overlap，改为 "the first systematic per-layer decomposition combining cross-instruction probes, attention analysis, RSA, and functional probes in a $2\times2$ factorial design"——强调 comprehensiveness 而非 temporal priority。

---

### R2-N2: 无方法论创新——标准工具直接应用

**[REBUT]** R2-N2-Issue-N2: 分析论文的贡献在于 **findings 和 experimental design**，不必然需要方法论创新。

CoRL 和 NeurIPS 均接收过大量使用标准工具（probing, RSA, attention analysis）但提供新 empirical insights 的论文（如 Raghu et al. 2021 "Do Vision Transformers See Like CNNs?" 使用 CKA/attention distance，Clark et al. 2019 使用 attention probing）。

**但从写作/framing 角度，论文需要更明确地 position 自己为 empirical contribution paper**：
- 当前 Introduction 的 contribution list（L27）以 "the first..." 开头，暗示 novelty 在于 priority
- 应改为强调 insight novelty："We reveal [specific finding] that challenges the assumption of [X]"
- 如果 framing 清晰地传达 "我们用成熟工具发现了改变设计思路的新事实"，method innovation 的缺失就不是致命问题

---

### R2-N3: Design implications speculative；CKA 反转 RSA

**[AGREE]** 同 R1-N4 + R1-W2 的综合。

从写作层面：
- Speculative implications 以 definitive 语气呈现（"should optimize", "is the primary lever"）→ claim 强度超出证据
- CKA 反转在主文中完全不可见 → selective presentation concern

这两点叠加使 Discussion §5 的 "Implications for VLA design" 段成为全文最弱的环节。

---

### R2-N4: 单模型单 benchmark 泛化性不足

**[AGREE]** 同 R1-N2。从写作角度额外补充：论文在 cross-benchmark validation（LIBERO-Spatial）中已展示了 partial replication，但这仍是同一模型在同一 benchmark suite 的两个 split 上。Title 的 "Vision-Language-Action Models"（类属复数）在写作层面构成 overclaim。

---

### R2-W1: Related Work 严重不足

**[AGREE]** 这与我的 W4 一致，且 R2 提供了更具体的缺失文献列表。

从写作规范定量评估：
- 当前：21 citations, 3 paragraphs, ~15 lines source
- CoRL 2024 录用 analysis 论文的典型水平：40-60 citations, 4-6 paragraphs
- 缺失的关键类别：
  - Probing 方法论背景（Hewitt & Manning 2019, Tenney et al. 2019）
  - Attention interpretability（Clark et al. 2019, Vig & Belinkov 2019）
  - Representation geometry in vision（Raghu et al. 2021, Nguyen et al. 2021）
  - VLA 架构多样性（Octo, CrossFormer, RT-X）
  - 如 R2 所指，Neo et al. (ICLR 2025), logit lens

当前密度**明确低于 CoRL 论文下限**。Related Work 的目标是让审稿人相信 "作者理解这个领域"——3 段 15 行做不到这一点。

---

### R2-W2: CKA 与 RSA 矛盾

**[AGREE]** 同 R1-W2。不再重复。

---

### R2-W3: 核心 RSA 结果 n.s.

**[REBUT]** R2-W3-Issue-W3: 同 R1-N3 回应。论文处理透明，cross-benchmark replication 提供了补充证据。但同意 framing 应以 same-layer significant comparison 为主，best-vs-best n.s. 结果为辅。

---

### R2-W4: 无 real-robot 或 rollout-level 实验

**[AGREE]** 对 CoRL venue 而言，纯 representation analysis without any deployment validation 是一个 relevance concern。论文的 design implications（"action heads at L12-L13", "optimize routing"）如果能用哪怕一个简单的 architectural intervention + rollout success rate 来 validate，说服力会大幅提升。

从写作角度：当前论文在 Discussion 中以 definitive 语气给出设计建议，但既没有 real-robot 验证也没有 simulation rollout。这加剧了 R1-N4 和 R2-N3 的 speculative concern。建议至少在 Future Work 中明确声明计划做 architectural intervention。

---

## Director 提出的 4 个专项问题

### Q1: R1-N1 是否也构成叙事连贯性问题？

**是的。** "Training learns deliberate instruction routing" 是全文第二大 finding 的标题（§4.2）、Abstract 的第二个 claim、Conclusion 的第二个要点。如果 "training" 的实际含义是 "Llama-2 pretraining + VLA fine-tuning"（而非仅 VLA fine-tuning），那么这一 finding 的 **framing 精度** 有问题。论文在所有这些位置都暗示是 VLA-specific training 创造了 routing，但证据无法排除 Llama-2 language pretraining 就已经具备这种能力的可能。这是一个从 Abstract 到 Conclusion 贯穿全文的 framing 问题。

### Q2: 无方法创新的分析论文能否通过 framing 弥补？

**可以，但需要更好的 framing。** 成功案例如 "Do Vision Transformers See Like CNNs?"（Raghu et al., NeurIPS 2021）使用标准 CKA 但被广泛引用，因为 findings 改变了社区对 ViT 的理解。当前论文的 framing 问题在于：(1) "first" claim 可能不成立，削弱 priority-based novelty；(2) design implications 以 definitive 语气呈现但无验证，削弱 practical novelty。如果将 framing 调整为 "我们的分析揭示了一个此前未被认知的 strict division of labor，这一发现挑战了 uniform-processing 假设并为未来架构设计提供了可检验的假说"，说服力会更强。

### Q3: "VLAs"（复数）是否构成 overclaim？

**是的。** Title 使用 "Vision-Language-Action Models"（复数类属名词），Abstract 最后一句 "VLA architectures should..."（一般性建议），这些都暗示 findings 对整个 VLA 类别成立。但证据仅来自一个架构（DinoSigLIP + Llama-2 7B）。从写作规范看，single-model study 的 title 应使用限定表达（"A Case Study of OpenVLA" / "Evidence from OpenVLA-7B"），或在 abstract 中明确限定 "In OpenVLA-7B, we find that..."。

### Q4: Related Work 密度是否达到 CoRL 下限？

**未达到。** 定量对比：
- 本文：21 citations, 3 paragraphs, ~150 words
- CoRL 2024 录用论文 median（analysis 类）：估计 45-55 citations, 5-7 paragraphs
- 缺失整个类别：probing methodology (NLP), attention interpretability, representation geometry (vision), broader VLA architectures

21 citations 在 CoRL 论文中属于 bottom 5% 水平。即使论文本身工作扎实，这种 Related Work 密度会给审稿人 "调研不充分" 的第一印象，对 acceptance decision 有负面影响。

---

[Reviewer 2 审稿结果]:
已完成交叉回应并提交给 Director。核心判断：

- R1-N1（baseline confound）和 R1-N3（selection bias）是最具杀伤力的问题，我全部 AGREE
- 仅对 R1-W3（L1 attention 选择性报告）和 R1-W4（LOOCV 统计力）部分 REBUT，因为论文内部证据已部分回应
- R3 格式问题全部同意，但不应影响科学评分
- 综合评估维持 5/10，核心瓶颈是 internal validity（untrained baseline 的 confound 设计）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_3"
}
```

</details>

---


### Tool call

_source line 90 · 2026-05-17T04:42:45.760851+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "vla-ssd",
  "issues_yaml": "issues:\n  - id: R1-N1\n    summary: \"Untrained baseline (random weights) 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献，核心叙事 'training learns routing' 的因果归因不成立\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识。需增加 Llama-2 base checkpoint 作为中间对照（random → pretrained → VLA-finetuned）\"\n    action_items:\n      - round: 1\n        action: \"增加 Llama-2 base checkpoint 对照实验（至少 attention analysis + cross-instruction probe）\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N2\n    summary: \"单一模型(OpenVLA-7B) + 单一 benchmark family(LIBERO) 无法支撑 title/abstract 中关于 'VLAs' 的一般性结论和架构设计建议\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识。Title 使用复数 'VLAs' 构成 overclaim。Grant 2026 已覆盖 6 模型 + 4 benchmark。\"\n    action_items:\n      - round: 1\n        action: \"限定所有 claim 为 OpenVLA-7B 或 frozen-encoder VLAs；或增加至少一个额外架构验证\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N4\n    summary: \"Design implications ('vision encoder is primary lever', 'early exit at L12') 完全基于 correlational evidence (RSA/probes)，缺乏因果验证，且 CKA 反转 RSA 排序\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识。Probing encoding ≠ use。Abstract/Discussion 中未加限定的祈使语气与 correlational 证据不匹配。\"\n    action_items:\n      - round: 1\n        action: \"弱化 design implications 语气为 hypothesis/suggestion；或增加因果验证实验（encoder swap / early-exit rollout）\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N3\n    summary: \"RSA best-vs-best 比较存在 selection bias (32层取max, winner's curse)；LIBERO-Goal 主结果 n.s. (CI incl. 0)\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R1+R2 认为 critical，R3 rebut 认为论文处理透明（same-layer comparison p<0.0001）。2:1 共识为 critical。\"\n    action_items:\n      - round: 1\n        action: \"以 same-layer paired comparison 作为 primary framing；对 best-vs-best 做 multiple comparisons correction\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-N1\n    summary: \"'First token-level representational decomposition' novelty claim 过强——Neo et al. (ICLR 2025) VLM token-level 分析 + Grant 2026 Action Atlas per-token SAE 已有类似工作\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R1 部分同意(Neo是VLM不是VLA，但Grant 2026覆盖)，R2+R3 完全同意。需限定 claim。\"\n    action_items:\n      - round: 1\n        action: \"删除或限定 'first' claim；改为强调 trained/untrained factorial design 的 specific novelty；引用 Neo et al.\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W1\n    summary: \"Related Work 严重不足：21 篇引用、3 段 15 行，缺失 Neo et al. (ICLR 2025)、logit lens、Raghu et al. 2021 等关键文献\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识。21 citations 在 CoRL 属 bottom 5%。缺失 VLM analysis、LLM interpretability、representation geometry 整个类别。\"\n    action_items:\n      - round: 1\n        action: \"扩展 Related Work 至 4-6 段，增加引用至 40+ 篇，覆盖 probing methodology / attention interpretability / representation geometry / VLA architectures\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W1\n    summary: \"'Instruction-blind' / 'purely visual' claim 过强——仅 linear probe 为 chance，未用 MLP probe 测 instruction classification on image tokens\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识。方法不对称：action 用 MLP probe，instruction 用 linear probe。\"\n    action_items:\n      - round: 1\n        action: \"补充 MLP probe instruction classification 实验；或弱化 claim 为 'not linearly decodable'\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W2\n    summary: \"CKA 反转 RSA 排序 (DINOv2 最优→CKA下最差)，仅放 appendix 处理不充分，主文选择性呈现\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识。需在正文讨论 metric divergence。\"\n    action_items:\n      - round: 1\n        action: \"在 Discussion 中加 1-2 句承认 CKA divergence，解释为何 RSA 更适合评估 action-relevant geometry\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-N1\n    summary: \"Limitations 格式不满足 CoRL 2026 硬性要求：当前是 Discussion 内 \\\\paragraph{}，应为独立 section/subsection，且缺少 failure modes\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R3 标为 critical (格式合规)，R1+R2 同意但认为 trivially fixable 不影响科学评分。\"\n    action_items:\n      - round: 1\n        action: \"将 Limitations 改为独立 \\\\subsection{} 或 \\\\section{}；补充 2-3 个具体 failure modes\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-N2\n    summary: \"正文至少 8 处解释性 em-dash (---) 是显著 AI 写作标志\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R3 标为 critical，R1+R2 同意存在但认为是 presentation issue。\"\n    action_items:\n      - round: 1\n        action: \"全文清除所有解释性 em-dash，改用逗号/括号/分句\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-W5\n    summary: \"无 code/data 释放声明，CoRL 鼓励 reproducibility\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 3]\n        note: \"添加 reproducibility statement（不含可识别 URL）\"\n    action_items:\n      - round: 1\n        action: \"在 Conclusion 后加 reproducibility statement\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "vla-ssd",
    "issues_yaml": "issues:\n  - id: R1-N1\n    summary: \"Untrained baseline (random weights) 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献，核心叙事 'training learns routing' 的因果归因不成立\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识。需增加 Llama-2 base checkpoint 作为中间对照（random → pretrained → VLA-finetuned）\"\n    action_items:\n      - round: 1\n        action: \"增加 Llama-2 base checkpoint 对照实验（至少 attention analysis + cross-instruction probe）\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N2\n    summary: \"单一模型(OpenVLA-7B) + 单一 benchmark family(LIBERO) 无法支撑 title/abstract 中关于 'VLAs' 的一般性结论和架构设计建议\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识。Title 使用复数 'VLAs' 构成 overclaim。Grant 2026 已覆盖 6 模型 + 4 benchmark。\"\n    action_items:\n      - round: 1\n        action: \"限定所有 claim 为 OpenVLA-7B 或 frozen-encoder VLAs；或增加至少一个额外架构验证\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N4\n    summary: \"Design implications ('vision encoder is primary lever', 'early exit at L12') 完全基于 correlational evidence (RSA/probes)，缺乏因果验证，且 CKA 反转 RSA 排序\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识。Probing encoding ≠ use。Abstract/Discussion 中未加限定的祈使语气与 correlational 证据不匹配。\"\n    action_items:\n      - round: 1\n        action: \"弱化 design implications 语气为 hypothesis/suggestion；或增加因果验证实验（encoder swap / early-exit rollout）\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N3\n    summary: \"RSA best-vs-best 比较存在 selection bias (32层取max, winner's curse)；LIBERO-Goal 主结果 n.s. (CI incl. 0)\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R1+R2 认为 critical，R3 rebut 认为论文处理透明（same-layer comparison p<0.0001）。2:1 共识为 critical。\"\n    action_items:\n      - round: 1\n        action: \"以 same-layer paired comparison 作为 primary framing；对 best-vs-best 做 multiple comparisons correction\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-N1\n    summary: \"'First token-level representational decomposition' novelty claim 过强——Neo et al. (ICLR 2025) VLM token-level 分析 + Grant 2026 Action Atlas per-token SAE 已有类似工作\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R1 部分同意(Neo是VLM不是VLA，但Grant 2026覆盖)，R2+R3 完全同意。需限定 claim。\"\n    action_items:\n      - round: 1\n        action: \"删除或限定 'first' claim；改为强调 trained/untrained factorial design 的 specific novelty；引用 Neo et al.\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W1\n    summary: \"Related Work 严重不足：21 篇引用、3 段 15 行，缺失 Neo et al. (ICLR 2025)、logit lens、Raghu et al. 2021 等关键文献\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识。21 citations 在 CoRL 属 bottom 5%。缺失 VLM analysis、LLM interpretability、representation geometry 整个类别。\"\n    action_items:\n      - round: 1\n        action: \"扩展 Related Work 至 4-6 段，增加引用至 40+ 篇，覆盖 probing methodology / attention interpretability / representation geometry / VLA architectures\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W1\n    summary: \"'Instruction-blind' / 'purely visual' claim 过强——仅 linear probe 为 chance，未用 MLP probe 测 instruction classification on image tokens\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识。方法不对称：action 用 MLP probe，instruction 用 linear probe。\"\n    action_items:\n      - round: 1\n        action: \"补充 MLP probe instruction classification 实验；或弱化 claim 为 'not linearly decodable'\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W2\n    summary: \"CKA 反转 RSA 排序 (DINOv2 最优→CKA下最差)，仅放 appendix 处理不充分，主文选择性呈现\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识。需在正文讨论 metric divergence。\"\n    action_items:\n      - round: 1\n        action: \"在 Discussion 中加 1-2 句承认 CKA divergence，解释为何 RSA 更适合评估 action-relevant geometry\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-N1\n    summary: \"Limitations 格式不满足 CoRL 2026 硬性要求：当前是 Discussion 内 \\\\paragraph{}，应为独立 section/subsection，且缺少 failure modes\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R3 标为 critical (格式合规)，R1+R2 同意但认为 trivially fixable 不影响科学评分。\"\n    action_items:\n      - round: 1\n        action: \"将 Limitations 改为独立 \\\\subsection{} 或 \\\\section{}；补充 2-3 个具体 failure modes\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-N2\n    summary: \"正文至少 8 处解释性 em-dash (---) 是显著 AI 写作标志\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R3 标为 critical，R1+R2 同意存在但认为是 presentation issue。\"\n    action_items:\n      - round: 1\n        action: \"全文清除所有解释性 em-dash，改用逗号/括号/分句\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-W5\n    summary: \"无 code/data 释放声明，CoRL 鼓励 reproducibility\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 3]\n        note: \"添加 reproducibility statement（不含可识别 URL）\"\n    action_items:\n      - round: 1\n        action: \"在 Conclusion 后加 reproducibility statement\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 91 · 2026-05-17T04:42:45.812242+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml\", \"bytes\": 6697}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 92 · 2026-05-17T04:44:22.426482+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "vla-ssd",
  "report": "# 圆桌审稿报告 — Round 1\n\n**论文**: \"Vision Encodes, Language Routes: A Representational Decomposition of Vision-Language-Action Models\"\n**Venue**: CoRL 2026 (Deadline: 2026-05-28)\n**Reviewers**: R1 (方法/实验), R2 (新颖性/意义), R3 (写作/格式)\n\n---\n\n## Summary\n\n论文对 OpenVLA-7B 进行了 token-level 表征分解，结合 cross-instruction probes、attention analysis、RSA 和 functional probes，在 LIBERO 上发现三个现象：(1) image tokens 与 readout token 的功能特化；(2) 训练学习了 deliberate instruction routing；(3) LLM 对 vision encoder 输出的 non-monotonic refinement（inverted-U）。分析设计系统、robustness checks 全面、写作清晰，但存在根本性的实验设计缺陷和 overclaiming 问题。\n\n---\n\n## Strengths\n\n1. **系统化分析框架**：四种互补方法 + 2×2 factorial design + trained/untrained 对照，比单一 metric 更有说服力（R1, R2 共识）\n2. **统计严谨性**：Bootstrap CI、LOOCV、permutation test、seed sensitivity、cross-benchmark replication、demo subsampling——附录 robustness analyses 扎实（R1 强调）\n3. **写作清晰度高**：叙事主线统一（specialization → routing → geometry），三个 findings 层层递进，图表信息密度高（R3 确认）\n4. **诚实报告 null/adverse results**：RSA best-vs-best CI 包含 0、CKA 反转 RSA、peak convergence 不跨 benchmark 复制等均如实报告（R1 认可）\n5. **有潜在的 design insight 价值**：如果 findings 经因果验证成立，对 VLA 架构设计有实际指导意义\n\n---\n\n## Weaknesses（按严重性排序）\n\n### Critical（影响接收决定，全票共识）\n\n**W-Critical-1: Untrained baseline 无法隔离 VLA fine-tuning 的贡献**\n- 论文将 trained (Llama-2 pretrained + VLA fine-tuned) 与 untrained (6.74B random weights) 对比，声称差异反映 \"training learns deliberate routing\"\n- 这混淆了两个因素：(1) Llama-2 语言预训练；(2) VLA fine-tuning。25/32 heads 翻转为 instruction-dominant 可能是语言预训练的产物\n- 缺失关键中间对照：Llama-2 base checkpoint (pretrained but not VLA-finetuned)\n- 影响范围：论文核心 Finding 2（routing）和所有 trained vs untrained Δ 值的解释\n- **全票共识 (R1 critical, R2 AGREE, R3 AGREE)**\n\n**W-Critical-2: 单一模型 + 单一 benchmark family，结论过度泛化**\n- 仅 OpenVLA-7B (DinoSigLIP + Llama-2) 在 LIBERO (tabletop manipulation) 上验证\n- Title 使用复数 \"Vision-Language-Action Models\"，Abstract/Discussion 给出一般性架构设计建议\n- 直接竞争者 Grant 2026 已覆盖 6 模型 + 4 benchmark\n- OpenVLA 的 frozen vision encoder 是特定设计选择，其他 VLA 可能 fine-tune encoder——此时 \"instruction-blind image tokens\" 可能是 trivial 推论\n- **全票共识 (R1 critical, R2 critical, R3 AGREE)**\n\n**W-Critical-3: Design implications 完全 speculative，无因果验证**\n- \"Vision encoder quality is the primary design lever\"、\"action heads should read from L12-L13\"、\"optimize routing\" 均无任何 intervention/ablation 支撑\n- Probing R² 证明 information extractable，不证明 model uses it (encoding ≠ use，Belinkov 2022)\n- CKA 完全反转 RSA 的 encoder 排序 (Linear CKA: untrained > trained > DINOv2)，表明 design recommendation 是 metric-dependent\n- Discussion 自承 \"RSA does not establish causal contribution\" 但随即给出未加限定的祈使语气建议\n- **全票共识 (R1 critical, R2 critical, R3 AGREE)**\n\n**W-Critical-4: \"First token-level decomposition\" novelty claim 不成立**\n- Neo et al. (ICLR 2025) 已对 VLM (LLaVA) 做 token-level 分析 (object localization + cross-layer alignment + last-token integration)\n- Grant 2026 (Action Atlas) 对 6 个 VLA 做 per-token SAE 分析 (424 SAEs)\n- 论文未引用 Neo et al.，Related Work 调研存在明显遗漏\n- **R2 critical, R1 部分同意（Neo 是 VLM 非 VLA，但 Grant 2026 覆盖），R3 AGREE**\n\n### Warning（影响评分，全票或多数共识）\n\n**W-Warning-1: RSA best-vs-best 存在 selection bias**\n- 32 层取 max 有正偏置 (winner's curse)；主 benchmark LIBERO-Goal 结果 n.s. (CI incl. 0)\n- 用 LIBERO-Spatial 显著结果 rescue 主实验零结果方法论存疑\n- R3 rebut：same-layer comparison (L12, Δ=+0.079, p<0.0001) 已提供——但论文以 best-vs-best 作为 primary framing 是问题\n- **2:1 共识 (R1 critical, R2 AGREE, R3 REBUT)**\n\n**W-Warning-2: Related Work 严重不足**\n- 21 篇引用、3 段 15 行，属 CoRL 论文 bottom 5% 水平\n- 缺失：Neo et al. (ICLR 2025)、logit lens、Raghu et al. 2021、Hewitt & Manning 2019、attention interpretability (Clark et al. 2019)\n- 缺失整个类别：VLM analysis、LLM interpretability、representation geometry\n- **全票共识**\n\n**W-Warning-3: \"Instruction-blind\" / \"purely visual\" claim 过强**\n- 仅 linear probe 为 chance，未用 MLP probe 测 instruction classification on image tokens\n- 方法不对称：action prediction 用 MLP probe，instruction classification 用 linear probe\n- **全票共识**\n\n**W-Warning-4: CKA 与 RSA 矛盾仅放 appendix，主文选择性呈现**\n- Linear CKA 完全反转核心结论 (DINOv2 最优 → CKA 下最差)\n- 两个标准度量给出相反结论，选择支持叙事的指标有 confirmation bias 外观\n- **全票共识**\n\n**W-Warning-5: Limitations 格式不满足 CoRL 2026 要求**\n- 当前是 Discussion 内 \\paragraph{}，非独立 section/subsection\n- 缺少 failure modes 描述 (CoRL 明确要求)\n- **全票共识 (R3 标为 critical 格式合规问题)**\n\n**W-Warning-6: AI 写作痕迹 (em-dash)**\n- 正文至少 8 处解释性 em-dash，是最显著 AI 生成标志\n- **全票共识**\n\n---\n\n## Reviewer Consensus [AGREE]\n\n所有 Reviewer 达成共识的关键判断：\n1. Untrained baseline confound 是最根本的 internal validity 问题\n2. 单模型泛化性 + speculative implications 叠加使论文 significance 不足\n3. Related Work 密度明确低于 CoRL 标准\n4. 写作质量本身良好，但 claim 强度系统性超出证据支撑范围\n5. Robustness analyses 做得扎实，统计报告总体透明\n\n---\n\n## Reviewer Divergence [REBUT]\n\n| 分歧点 | 立场 | 理由 |\n|--------|------|------|\n| RSA selection bias 严重性 | R1+R2: critical / R3: REBUT | R3 认为 same-layer comparison 已充分处理 |\n| 方法创新是否必须 | R2: critical / R1+R3: REBUT | R1+R3 认为分析论文可通过 insight novelty 弥补 |\n| Real-robot 是否必须 | R2+R3: concern / R1: REBUT | R1 认为分析论文不必做 system contribution |\n| Em-dash 是否 critical | R3: critical / R1+R2: warning | R1+R2 认为不影响科学质量 |\n\n---\n\n## Questions（需作者澄清）\n\n1. 是否有 Llama-2 base checkpoint（无 VLA fine-tuning）的 attention 和 routing 数据？\n2. Random features baseline 在同维度同样本量下做 10-way classification 的精度？\n3. MLP probe 对 image_mean 做 instruction classification 的结果？\n4. 为何选择 RSA 而非 CKA 作为 primary metric 的 principled justification？\n5. 是否计划做任何 architectural intervention 验证（如 early-exit、encoder swap）？\n\n---\n\n## Missing References\n\n1. **Neo et al. (ICLR 2025)** — \"Towards Interpreting Visual Information Processing in Vision-Language Models\" — VLM token-level analysis 直接先行工作\n2. **Elhage et al. 2021** — \"A Mathematical Framework for Transformer Circuits\" — residual stream / information flow\n3. **Raghu et al. (NeurIPS 2021)** — \"Do Vision Transformers See Like CNNs?\" — ViT layer-wise representation analysis\n4. **Hewitt & Manning 2019** — structural probes + control tasks for probing methodology\n5. **Clark et al. 2019** — attention pattern analysis in Transformers\n6. **logit lens (nostalgebraist 2020)** — layer-wise prediction decomposition\n\n---\n\n## Overall Assessment\n\n**Score: Weak Reject (4.5/10)**\n**Confidence: High (4/5)**\n\n| Reviewer | Score | Post-cross-response |\n|----------|-------|-------------------|\n| R1 | 5/10 | 维持 |\n| R2 | 4/10 | 调整至 5/10（如修复 N1+限定 claims 可升至 6） |\n| R3 | 6/10 | 维持（写作/格式视角） |\n| **Consensus** | **4.5/10** | **Weak Reject** |\n\n**核心判断**：论文提出了有价值的分析框架，写作质量良好，robustness checks 全面。但存在三个相互叠加的根本性问题使其低于 acceptance threshold：\n1. **Internal validity**：untrained baseline 的 confound 使核心 \"training learns routing\" 叙事的因果归因不成立\n2. **External validity**：单模型 + 单 benchmark family 无法支撑一般性结论，title/abstract 系统性 overclaim\n3. **Practical significance**：design implications 完全 speculative，CKA 反转 RSA 表明 recommendations 是 metric-dependent\n\n**Rebuttal 路径（如能实质性解决以下任一，可重新评估）**：\n- 补充 Llama-2 base checkpoint 中间对照（解决 internal validity）\n- 补充至少一个 architectural intervention 实验（解决 practical significance）\n- 大幅限定所有 claims 至 OpenVLA-specific + correlational（解决 overclaiming，但可能降低 impact）\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- \"LOOCV-verified\" 未展开；建议改为 \"cross-validated\"\n- 最后一句 \"VLA architectures should...\" 语气过强，缺乏因果支撑\n- 约 200 words，长度合适\n\n### Introduction\n- 五段结构完整，叙事从 gap 切入\n- L8 仅引用 grant2026 作为 visual dominance 唯一支撑——建议补充 fei2025、hou2026\n- Contribution list (L27) \"the first...\" claim 需限定\n\n### Related Work\n- 3 段 ~16 行严重不足\n- 缺失整个类别：VLM analysis、probing methodology、attention interpretability\n- 未与 Grant 2026、Swann 2026 做明确 differentiation\n\n### Method\n- 2×2 factorial design 清晰\n- \"untrained control by reinitializing all LLM parameters\" 的描述准确但未讨论其局限\n- 列表项 em-dash 格式问题（改用冒号）\n\n### Experiments\n- 数据呈现严谨，所有数值有 CI/p-value\n- Table 1 caption 声称 \"L0-L8 shown\" 但实际含 L16, L31\n- Fig 3 和 Fig 5(a) 信息重叠，空间效率低\n- §4.3 应以 same-layer comparison 为 primary evidence，best-vs-best 为 supplementary\n\n### Discussion\n- Implications 段是全文最弱环节——definitive 语气 + correlational evidence = 内部矛盾\n- Limitations 内容基本到位但格式不合规，缺 failure modes\n- RSA-R² peak offset 的讨论有价值\n\n### Conclusion\n- 几乎逐字重复 Abstract，阅读价值低\n- 建议增加 1 句 future direction 或 broader implication\n\n### Appendix\n- CKA metric sensitivity 分析应部分移入正文\n- Robustness analyses (seed, demo subsample, distance metric, permutation) 全面且支持 pattern 稳定性\n- Cross-benchmark (LIBERO-Spatial) replication 有价值但仍是同一 benchmark family",
  "reviewer_ids_acknowledged": "[1, 2, 3]",
  "cross_response_reviewer_ids": "[1, 2, 3]",
  "overall_score": "weak reject"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "vla-ssd",
    "report": "# 圆桌审稿报告 — Round 1\n\n**论文**: \"Vision Encodes, Language Routes: A Representational Decomposition of Vision-Language-Action Models\"\n**Venue**: CoRL 2026 (Deadline: 2026-05-28)\n**Reviewers**: R1 (方法/实验), R2 (新颖性/意义), R3 (写作/格式)\n\n---\n\n## Summary\n\n论文对 OpenVLA-7B 进行了 token-level 表征分解，结合 cross-instruction probes、attention analysis、RSA 和 functional probes，在 LIBERO 上发现三个现象：(1) image tokens 与 readout token 的功能特化；(2) 训练学习了 deliberate instruction routing；(3) LLM 对 vision encoder 输出的 non-monotonic refinement（inverted-U）。分析设计系统、robustness checks 全面、写作清晰，但存在根本性的实验设计缺陷和 overclaiming 问题。\n\n---\n\n## Strengths\n\n1. **系统化分析框架**：四种互补方法 + 2×2 factorial design + trained/untrained 对照，比单一 metric 更有说服力（R1, R2 共识）\n2. **统计严谨性**：Bootstrap CI、LOOCV、permutation test、seed sensitivity、cross-benchmark replication、demo subsampling——附录 robustness analyses 扎实（R1 强调）\n3. **写作清晰度高**：叙事主线统一（specialization → routing → geometry），三个 findings 层层递进，图表信息密度高（R3 确认）\n4. **诚实报告 null/adverse results**：RSA best-vs-best CI 包含 0、CKA 反转 RSA、peak convergence 不跨 benchmark 复制等均如实报告（R1 认可）\n5. **有潜在的 design insight 价值**：如果 findings 经因果验证成立，对 VLA 架构设计有实际指导意义\n\n---\n\n## Weaknesses（按严重性排序）\n\n### Critical（影响接收决定，全票共识）\n\n**W-Critical-1: Untrained baseline 无法隔离 VLA fine-tuning 的贡献**\n- 论文将 trained (Llama-2 pretrained + VLA fine-tuned) 与 untrained (6.74B random weights) 对比，声称差异反映 \"training learns deliberate routing\"\n- 这混淆了两个因素：(1) Llama-2 语言预训练；(2) VLA fine-tuning。25/32 heads 翻转为 instruction-dominant 可能是语言预训练的产物\n- 缺失关键中间对照：Llama-2 base checkpoint (pretrained but not VLA-finetuned)\n- 影响范围：论文核心 Finding 2（routing）和所有 trained vs untrained Δ 值的解释\n- **全票共识 (R1 critical, R2 AGREE, R3 AGREE)**\n\n**W-Critical-2: 单一模型 + 单一 benchmark family，结论过度泛化**\n- 仅 OpenVLA-7B (DinoSigLIP + Llama-2) 在 LIBERO (tabletop manipulation) 上验证\n- Title 使用复数 \"Vision-Language-Action Models\"，Abstract/Discussion 给出一般性架构设计建议\n- 直接竞争者 Grant 2026 已覆盖 6 模型 + 4 benchmark\n- OpenVLA 的 frozen vision encoder 是特定设计选择，其他 VLA 可能 fine-tune encoder——此时 \"instruction-blind image tokens\" 可能是 trivial 推论\n- **全票共识 (R1 critical, R2 critical, R3 AGREE)**\n\n**W-Critical-3: Design implications 完全 speculative，无因果验证**\n- \"Vision encoder quality is the primary design lever\"、\"action heads should read from L12-L13\"、\"optimize routing\" 均无任何 intervention/ablation 支撑\n- Probing R² 证明 information extractable，不证明 model uses it (encoding ≠ use，Belinkov 2022)\n- CKA 完全反转 RSA 的 encoder 排序 (Linear CKA: untrained > trained > DINOv2)，表明 design recommendation 是 metric-dependent\n- Discussion 自承 \"RSA does not establish causal contribution\" 但随即给出未加限定的祈使语气建议\n- **全票共识 (R1 critical, R2 critical, R3 AGREE)**\n\n**W-Critical-4: \"First token-level decomposition\" novelty claim 不成立**\n- Neo et al. (ICLR 2025) 已对 VLM (LLaVA) 做 token-level 分析 (object localization + cross-layer alignment + last-token integration)\n- Grant 2026 (Action Atlas) 对 6 个 VLA 做 per-token SAE 分析 (424 SAEs)\n- 论文未引用 Neo et al.，Related Work 调研存在明显遗漏\n- **R2 critical, R1 部分同意（Neo 是 VLM 非 VLA，但 Grant 2026 覆盖），R3 AGREE**\n\n### Warning（影响评分，全票或多数共识）\n\n**W-Warning-1: RSA best-vs-best 存在 selection bias**\n- 32 层取 max 有正偏置 (winner's curse)；主 benchmark LIBERO-Goal 结果 n.s. (CI incl. 0)\n- 用 LIBERO-Spatial 显著结果 rescue 主实验零结果方法论存疑\n- R3 rebut：same-layer comparison (L12, Δ=+0.079, p<0.0001) 已提供——但论文以 best-vs-best 作为 primary framing 是问题\n- **2:1 共识 (R1 critical, R2 AGREE, R3 REBUT)**\n\n**W-Warning-2: Related Work 严重不足**\n- 21 篇引用、3 段 15 行，属 CoRL 论文 bottom 5% 水平\n- 缺失：Neo et al. (ICLR 2025)、logit lens、Raghu et al. 2021、Hewitt & Manning 2019、attention interpretability (Clark et al. 2019)\n- 缺失整个类别：VLM analysis、LLM interpretability、representation geometry\n- **全票共识**\n\n**W-Warning-3: \"Instruction-blind\" / \"purely visual\" claim 过强**\n- 仅 linear probe 为 chance，未用 MLP probe 测 instruction classification on image tokens\n- 方法不对称：action prediction 用 MLP probe，instruction classification 用 linear probe\n- **全票共识**\n\n**W-Warning-4: CKA 与 RSA 矛盾仅放 appendix，主文选择性呈现**\n- Linear CKA 完全反转核心结论 (DINOv2 最优 → CKA 下最差)\n- 两个标准度量给出相反结论，选择支持叙事的指标有 confirmation bias 外观\n- **全票共识**\n\n**W-Warning-5: Limitations 格式不满足 CoRL 2026 要求**\n- 当前是 Discussion 内 \\paragraph{}，非独立 section/subsection\n- 缺少 failure modes 描述 (CoRL 明确要求)\n- **全票共识 (R3 标为 critical 格式合规问题)**\n\n**W-Warning-6: AI 写作痕迹 (em-dash)**\n- 正文至少 8 处解释性 em-dash，是最显著 AI 生成标志\n- **全票共识**\n\n---\n\n## Reviewer Consensus [AGREE]\n\n所有 Reviewer 达成共识的关键判断：\n1. Untrained baseline confound 是最根本的 internal validity 问题\n2. 单模型泛化性 + speculative implications 叠加使论文 significance 不足\n3. Related Work 密度明确低于 CoRL 标准\n4. 写作质量本身良好，但 claim 强度系统性超出证据支撑范围\n5. Robustness analyses 做得扎实，统计报告总体透明\n\n---\n\n## Reviewer Divergence [REBUT]\n\n| 分歧点 | 立场 | 理由 |\n|--------|------|------|\n| RSA selection bias 严重性 | R1+R2: critical / R3: REBUT | R3 认为 same-layer comparison 已充分处理 |\n| 方法创新是否必须 | R2: critical / R1+R3: REBUT | R1+R3 认为分析论文可通过 insight novelty 弥补 |\n| Real-robot 是否必须 | R2+R3: concern / R1: REBUT | R1 认为分析论文不必做 system contribution |\n| Em-dash 是否 critical | R3: critical / R1+R2: warning | R1+R2 认为不影响科学质量 |\n\n---\n\n## Questions（需作者澄清）\n\n1. 是否有 Llama-2 base checkpoint（无 VLA fine-tuning）的 attention 和 routing 数据？\n2. Random features baseline 在同维度同样本量下做 10-way classification 的精度？\n3. MLP probe 对 image_mean 做 instruction classification 的结果？\n4. 为何选择 RSA 而非 CKA 作为 primary metric 的 principled justification？\n5. 是否计划做任何 architectural intervention 验证（如 early-exit、encoder swap）？\n\n---\n\n## Missing References\n\n1. **Neo et al. (ICLR 2025)** — \"Towards Interpreting Visual Information Processing in Vision-Language Models\" — VLM token-level analysis 直接先行工作\n2. **Elhage et al. 2021** — \"A Mathematical Framework for Transformer Circuits\" — residual stream / information flow\n3. **Raghu et al. (NeurIPS 2021)** — \"Do Vision Transformers See Like CNNs?\" — ViT layer-wise representation analysis\n4. **Hewitt & Manning 2019** — structural probes + control tasks for probing methodology\n5. **Clark et al. 2019** — attention pattern analysis in Transformers\n6. **logit lens (nostalgebraist 2020)** — layer-wise prediction decomposition\n\n---\n\n## Overall Assessment\n\n**Score: Weak Reject (4.5/10)**\n**Confidence: High (4/5)**\n\n| Reviewer | Score | Post-cross-response |\n|----------|-------|-------------------|\n| R1 | 5/10 | 维持 |\n| R2 | 4/10 | 调整至 5/10（如修复 N1+限定 claims 可升至 6） |\n| R3 | 6/10 | 维持（写作/格式视角） |\n| **Consensus** | **4.5/10** | **Weak Reject** |\n\n**核心判断**：论文提出了有价值的分析框架，写作质量良好，robustness checks 全面。但存在三个相互叠加的根本性问题使其低于 acceptance threshold：\n1. **Internal validity**：untrained baseline 的 confound 使核心 \"training learns routing\" 叙事的因果归因不成立\n2. **External validity**：单模型 + 单 benchmark family 无法支撑一般性结论，title/abstract 系统性 overclaim\n3. **Practical significance**：design implications 完全 speculative，CKA 反转 RSA 表明 recommendations 是 metric-dependent\n\n**Rebuttal 路径（如能实质性解决以下任一，可重新评估）**：\n- 补充 Llama-2 base checkpoint 中间对照（解决 internal validity）\n- 补充至少一个 architectural intervention 实验（解决 practical significance）\n- 大幅限定所有 claims 至 OpenVLA-specific + correlational（解决 overclaiming，但可能降低 impact）\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- \"LOOCV-verified\" 未展开；建议改为 \"cross-validated\"\n- 最后一句 \"VLA architectures should...\" 语气过强，缺乏因果支撑\n- 约 200 words，长度合适\n\n### Introduction\n- 五段结构完整，叙事从 gap 切入\n- L8 仅引用 grant2026 作为 visual dominance 唯一支撑——建议补充 fei2025、hou2026\n- Contribution list (L27) \"the first...\" claim 需限定\n\n### Related Work\n- 3 段 ~16 行严重不足\n- 缺失整个类别：VLM analysis、probing methodology、attention interpretability\n- 未与 Grant 2026、Swann 2026 做明确 differentiation\n\n### Method\n- 2×2 factorial design 清晰\n- \"untrained control by reinitializing all LLM parameters\" 的描述准确但未讨论其局限\n- 列表项 em-dash 格式问题（改用冒号）\n\n### Experiments\n- 数据呈现严谨，所有数值有 CI/p-value\n- Table 1 caption 声称 \"L0-L8 shown\" 但实际含 L16, L31\n- Fig 3 和 Fig 5(a) 信息重叠，空间效率低\n- §4.3 应以 same-layer comparison 为 primary evidence，best-vs-best 为 supplementary\n\n### Discussion\n- Implications 段是全文最弱环节——definitive 语气 + correlational evidence = 内部矛盾\n- Limitations 内容基本到位但格式不合规，缺 failure modes\n- RSA-R² peak offset 的讨论有价值\n\n### Conclusion\n- 几乎逐字重复 Abstract，阅读价值低\n- 建议增加 1 句 future direction 或 broader implication\n\n### Appendix\n- CKA metric sensitivity 分析应部分移入正文\n- Robustness analyses (seed, demo subsample, distance metric, permutation) 全面且支持 pattern 稳定性\n- Cross-benchmark (LIBERO-Spatial) replication 有价值但仍是同一 benchmark family",
    "reviewer_ids_acknowledged": "[1, 2, 3]",
    "cross_response_reviewer_ids": "[1, 2, 3]",
    "overall_score": "weak reject"
  }
}
```

</details>

---


### Tool result

_source line 93 · 2026-05-17T04:44:26.442832+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a1d032cbe70bdd2058438e67e0d57613:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4016
}
```

</details>

---


### Assistant

_source line 94 · 2026-05-17T04:44:38.041571+00:00_

审稿报告已投递给 Research Director。

**圆桌审稿完成。** 最终评分 **Weak Reject (4.5/10)**，三位 Reviewer 在四项 critical issue 上达成全票共识：

1. **Untrained baseline confound** — 无法区分 Llama-2 预训练 vs VLA fine-tuning 的贡献
2. **单模型泛化性 + overclaim** — 仅 OpenVLA + LIBERO 无法支撑 "VLAs" 一般性结论
3. **Design implications 无因果验证** — RSA/probe 的 correlational evidence 不能支撑祈使语气的架构设计建议
4. **Novelty claim 过强** — "first token-level decomposition" 被先行工作覆盖

最有力的 rebuttal 路径是补充 Llama-2 base checkpoint 中间对照实验。Issue tracker 已同步更新至 `artifacts/review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 12

## Round 12

44 recorded events


### User

_source line 95 · 2026-05-17T06:00:56.472150+00:00_

[Round 2 - 继续审稿]
论文已更新。请基于上一轮审稿意见，重点审查修改是否充分回应了之前提出的问题。
重点关注：
1. 上轮提出的问题是否已充分解决
2. 修改是否引入了新问题
3. 整体评分是否需要调整

上一轮审稿报告: `projects/vla-ssd/artifacts/review_reports/round_1.md`
跨轮次问题追踪: `projects/vla-ssd/artifacts/review_issues.yaml`
请用 read_local_file 先读这两个文件,重点验证 status=in_progress 的 issue 是否已被充分修复。
派 Reviewer 时把 open/in_progress 的 issue 列表附在任务里,要求逐条标 [RESOLVED] 或 [STILL_OPEN] + 理由。

[论文提交]
- 项目: vla-ssd
- 论文路径: projects/vla-ssd/docs/paper/main.tex
- 目标 venue: CoRL 2026
- 截止日期: 2026-05-29

请继续审稿流程。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 96 · 2026-05-17T06:01:14.782954+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "review_issues.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "review_issues.yaml",
    "max_chars": "0"
  }
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-17T06:01:15.938010+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1155
}
```

</details>

---


### Tool call

_source line 98 · 2026-05-17T06:01:15.938528+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 99 · 2026-05-17T06:01:16.040052+00:00_

1	\documentclass{article}
2	
3	\usepackage{corl_2026}
4	
5	\usepackage[utf8]{inputenc}
6	\usepackage[T1]{fontenc}
7	\usepackage{url}
8	\usepackage{booktabs}
9	\usepackage{amsfonts}
10	\usepackage{amsmath}
11	\usepackage{nicefrac}
12	\usepackage[expansion=false]{microtype}
13	\usepackage{graphicx}
14	\usepackage{enumitem}
15	
16	\title{Vision Encodes, Language Routes:\\ A Representational Decomposition of Vision-Language-Action Models}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	
22	\maketitle
23	
24	\begin{abstract}
25	\input{abstract}
26	\end{abstract}
27	
28	\input{introduction}
29	\input{related_work}
30	\input{method}
31	\input{experiments}
32	\input{discussion}
33	\input{conclusion}
34	
35	\bibliography{references}
36	
37	\input{appendix}
38	
39	\end{document}
40	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 100 · 2026-05-17T06:01:19.453391+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-17T06:01:19.655001+00:00_

1	issues:
2	  - id: R1-N1
3	    summary: "Untrained baseline (random weights) 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献，核心叙事 'training learns routing' 的因果归因不成立"
4	    category: experiment
5	    severity: critical
6	    status: in_progress
7	    first_raised_round: 1
8	    last_seen_round: 1
9	    mentions:
10	      - round: 1
11	        reviewers: [1, 2, 3]
12	        note: "全票共识。需增加 Llama-2 base checkpoint 作为中间对照（random → pretrained → VLA-finetuned）"
13	    action_items:
14	      - round: 1
15	        action: "增加 Llama-2 base checkpoint 对照实验（至少 attention analysis + cross-instruction probe）"
16	        assigned_to: research
17	        status: open
18	      - round: 1
19	        action: "已派 Agent 执行 Llama-2-7B base cross-instruction probe + L1 attention analysis（P0 优先级）"
20	        assigned_to: agent
21	        status: in_progress
22	    resolution: ""
23	    resolution_round: null
24	
25	  - id: R1-N2
26	    summary: "单一模型(OpenVLA-7B) + 单一 benchmark family(LIBERO) 无法支撑 title/abstract 中关于 'VLAs' 的一般性结论和架构设计建议"
27	    category: experiment
28	    severity: critical
29	    status: in_progress
30	    first_raised_round: 1
31	    last_seen_round: 1
32	    mentions:
33	      - round: 1
34	        reviewers: [1, 2, 3]
35	        note: "全票共识。Title 使用复数 'VLAs' 构成 overclaim。Grant 2026 已覆盖 6 模型 + 4 benchmark。"
36	    action_items:
37	      - round: 1
38	        action: "限定所有 claim 为 OpenVLA-7B 或 frozen-encoder VLAs；或增加至少一个额外架构验证"
39	        assigned_to: research
40	        status: open
41	      - round: 1
42	        action: "已派 Paper Agent 软化 claims，限定为 OpenVLA-7B"
43	        assigned_to: paper_agent
44	        status: in_progress
45	    resolution: ""
46	    resolution_round: null
47	
48	  - id: R1-N4
49	    summary: "Design implications ('vision encoder is primary lever', 'early exit at L12') 完全基于 correlational evidence (RSA/probes)，缺乏因果验证，且 CKA 反转 RSA 排序"
50	    category: framing
51	    severity: critical
52	    status: in_progress
53	    first_raised_round: 1
54	    last_see
…[truncated 7363 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-17T06:01:19.655480+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 103 · 2026-05-17T06:01:19.706006+00:00_

1	Vision-language-action models (VLAs) fine-tune large language models (LLMs) on robot demonstrations, but how they internally process multimodal information at the token level remains unknown.
2	We perform a systematic token-level representational decomposition of a VLA (OpenVLA-7B on LIBERO) with factorial trained-vs-untrained control, combining cross-instruction probes, attention analysis, Representational Similarity Analysis (RSA), and functional probes across all 32 LLM layers.
3	Three findings emerge.
4	First, the VLA exhibits strict token-level functional specialization: image tokens encode purely visual information (instruction classification at chance, $10\%$, across all layers), while the readout token serves as a multimodal convergence point ($100\%$ instruction classification from L1, LOOCV-verified).
5	Second, VLA training establishes deliberate instruction routing: at L1, 25/32 attention heads become instruction-dominant ($58\%$ attention to ${\sim}8\%$ of the sequence), creating a robust signal maintained through L31 ($100\%$), whereas the untrained baseline's incidental routing decays to $82\%$.
6	Third, the LLM applies a non-monotonic refinement of vision encoder geometry: RSA peaks at L12, probe $R^2$ peaks at L8--L13, with self-supervised DINOv2 providing the highest geometric foundation ($\rho = 0.692$, exceeding all internal representations).
7	These results reveal that VLAs maintain a strict division of labor between visual and multimodal tokens, with training primarily reshaping readout-token information integration (routing $+18$pp, attention $+46$pp) rather than visual representations ($\Delta \leq 1.7\%$).
8	VLA architectures should optimize routing from image tokens to the readout position; vision encoder quality is the primary design lever.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-17T06:01:27.134708+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 105 · 2026-05-17T06:01:27.285784+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Vision-language-action models (VLAs) process visual observations and language instructions through a large language model to produce robot actions~\cite{brohan2023_rt2,kim2024_openvla}.
5	A central but untested assumption is that all token types within the LLM contribute uniformly to action prediction.
6	Understanding the token-level division of labor is essential for designing efficient VLA architectures: if image tokens and readout tokens serve fundamentally different roles, then design choices (attention patterns, layer selection, action head placement) should reflect this specialization.
7	
8	Recent behavioral studies reveal that VLAs rely disproportionately on visual input~\cite{grant2026}, with language instructions largely ignored by the action pathway~\cite{haon2025}.
9	These findings hint at internal specialization but do not explain \emph{how} information is routed within the LLM, \emph{where} instruction identity is encoded, or \emph{what} training changes at the representational level.
10	No prior work has provided a systematic token-level decomposition of a VLA, leaving open whether image tokens carry instruction information, whether the readout token functions as a multimodal hub, and whether training creates new representational structure or reconfigures inherited geometry.
11	
12	We address this gap by decomposing OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a VLA chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2}, an MLP projector, and Llama-2 7B.
13	We extract representations from each of 32 LLM layers at both image-token and readout-token positions, and from external baselines (DINOv2~\cite{oquab2024_dinov2}, CLIP~\cite{radford2021_clip}).
14	We cross training status (trained vs.\ untrained, reinitializing 6.74B LLM parameters) with instruction presence in a $2\times 2$ factorial design, and apply four complementary analyses: cross-instruction probes fo
…[truncated 2282 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 106 · 2026-05-17T06:01:27.286588+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 107 · 2026-05-17T06:01:27.337204+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Vision-language-action models.}
4	VLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}.
5	This architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.
6	A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.
7	We test this assumption at the representational level through per-layer, per-token-type decomposition.
8	
9	\paragraph{Mechanistic interpretability in transformers.}
10	A growing body of work analyzes transformer internals at the level of individual attention heads and circuits.
11	Elhage et al.~\cite{elhage2021} introduced the residual stream framework, in which each layer reads from and writes to a shared communication channel.
12	Building on this, Olsson et al.~\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning; these specialized attention heads implement token-copying algorithms.
13	Circuit-level analyses have since traced complete computational subgraphs for tasks such as indirect object identification~\cite{wang2023_ioi} and greater-than comparison~\cite{conmy2023}.
14	In parallel, attention probing studies have shown that individual heads encode syntactic relations~\cite{clark2019}, capture positional and structural patterns at different depths~\cite{vig2019}, and that a small subset of specialized heads accounts for most model performance~\cite{voita2019}.
15	Our Layer-1 attention head analysis extends this tradition to the VLA domain, where we find that 25 of 32 heads become instruction-dominant after fine-tuning.
16	
17	\paragraph{Behavioral and mechanistic analysis of VLAs.}
18	Behavioral evaluations reveal that current VLAs rel
…[truncated 3810 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 108 · 2026-05-17T06:01:31.506659+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 109 · 2026-05-17T06:01:31.507232+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We evaluate OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024} on LIBERO-Goal~\cite{liu2023_libero} (10 tasks, 50 demonstrations each).
8	Representations are extracted from six sources spanning the VLA pipeline (\S\ref{sec:repr_extraction}): DinoSigLIP+Projector, LLM image\_mean and readout tokens at each of 32 layers, DINOv2~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}), CLIP~\cite{radford2021_clip} (\texttt{patch\_mean}), and branch-split (DINOv2 1{,}024-D / SigLIP 1{,}152-D before fusion).
9	The $2\times 2$ factorial design crosses training status (trained vs.\ untrained LLM, reinitializing 6.74B parameters) with instruction presence (\S\ref{sec:model_data}).
10	RSA computes Spearman $\rho$ between cosine-distance representation RDMs and Euclidean-distance action RDMs, with 10{,}000 bootstrap CIs (\S\ref{sec:rsa}).
11	MLP probes (input $\to$ 256 $\to$ 7; Adam, lr${}=10^{-3}$, 50 epochs, early stopping) report mean $R^2$ (\S\ref{sec:probes}).
12	
13	%------------------------------------------------------------------
14	\subsection{Token-Level Functional Specialization}
15	\label{sec:token_specialization}
16	
17	We test whether image tokens and readout tokens encode different types of information by training cross-instruction probes (\S\ref{sec:cross_instruction_probes}): given the same visual frame paired with each of 10 task instructions, we classify which instruction was present from per-layer activations.
18	
19	\paragraph{Image tokens are instruction-blind.}
20	At the image\_mean position, instruction classification remains at chance ($10\%$) across all 32 layers, in both trained and untrained models (Table~\ref{tab:dense_routing_main}).
21	This result holds identically for standalone DINOv2 \texttt{cls\_token} ($10\%$), confirming that instruction blindness is a property of the visual representation itself, not an artifact of the 
…[truncated 10719 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 110 · 2026-05-17T06:01:31.507476+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 111 · 2026-05-17T06:01:31.608471+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Synthesis.}
5	Our experiments reveal a coherent picture of token-level information processing in a VLA.
6	Image tokens maintain purely visual representations throughout all 32 LLM layers, never encoding instruction identity.
7	The readout token serves as the sole multimodal convergence point, integrating instruction information through a routing mechanism that training strengthens: 25/32 L1 heads become instruction-dominant in the trained model, creating a robust signal that survives the full depth of the network.
8	The LLM transforms the vision encoder's geometric foundation non-monotonically, with early-to-middle layers (L8--L13) containing the most action-relevant representations.
9	
10	\paragraph{Token specialization and routing.}
11	The strict division of labor between image and readout tokens suggests that the LLM does not blend modalities uniformly across token types.
12	Instead, visual information flows through image tokens while the readout token selectively attends to instruction tokens, with training creating a fundamentally different attention strategy (58\% deliberate routing vs.\ 12\% incidental leakage).
13	Training effects concentrate at the readout token (routing $+18$pp, attention $+46$pp, $R^2$ $+0.069$) while leaving image representations largely unchanged ($\Delta \leq 1.7\%$; Appendix~\ref{sec:training_effect_summary}).
14	
15	\paragraph{RSA--$R^2$ peak offset.}
16	The $R^2$ plateau (L8--L16) encompasses and partially precedes the RSA peak (L12). This suggests that maximal geometric alignment does not coincide with maximal decodability.
17	Training causes these peaks to converge on LIBERO-Goal (RSA L12, $R^2$ L13) but not on LIBERO-Spatial (6-layer gap), which may reflect benchmark-specific alignment.
18	
19	\paragraph{Implications for VLA design.}
20	Three practical considerations emerge.
21	\emph{First}, vision encoder pretraining quality is the primary design lever; investing in
…[truncated 2171 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 112 · 2026-05-17T06:01:36.407655+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 113 · 2026-05-17T06:01:36.608842+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We present a systematic token-level representational decomposition of a VLA with factorial trained-vs-untrained control, revealing three aspects of internal information processing.
5	(1)~Strict functional specialization: image tokens encode purely visual information (instruction classification at chance across all layers), while the readout token is the sole multimodal convergence point ($100\%$ instruction classification from L1, LOOCV-verified).
6	(2)~VLA training establishes deliberate instruction routing: 25/32 L1 attention heads become instruction-dominant ($58\%$ attention to ${\sim}8\%$ of the sequence), creating a robust signal maintained through L31, whereas the untrained baseline's incidental routing decays to $82\%$.
7	(3)~The LLM non-monotonically refines vision encoder geometry (RSA inverted-U peaking at L12, $R^2$ at L8--L13), with self-supervised DINOv2 providing the highest geometric foundation ($\rho = 0.692$) and training primarily reshaping readout-token integration ($R^2$ $+0.069$) rather than visual representations ($\Delta \leq 1.7\%$).
8	These results suggest that VLA architectures should optimize routing from image tokens to the readout position, and that vision encoder quality is the primary design lever.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 114 · 2026-05-17T06:01:36.609269+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 115 · 2026-05-17T06:01:36.659867+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We investigate how action-relevant structure is distributed across a VLA by combining four complementary analyses: cross-instruction probes, attention pattern analysis, RSA, and functional probes.
5	
6	%------------------------------------------------------------------
7	\subsection{Model and Data}
8	\label{sec:model_data}
9	
10	We study OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a generalist robot policy chaining three components: a frozen DinoSigLIP fused vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\to$ 4{,}096-D), and a Llama-2 7B language backbone (6.74B parameters) that autoregressively decodes 7-dimensional actions.
11	We use the base checkpoint pretrained on Open X-Embodiment (no task-specific fine-tuning) and evaluate on LIBERO-Goal~\cite{liu2023_libero} (10 tabletop tasks, 50 demonstrations each).
12	To isolate the LLM's contribution, we construct an untrained control by reinitializing all LLM parameters via \texttt{from\_config()} (6.74B random weights), preserving the frozen vision encoder and projector architecture.
13	
14	%------------------------------------------------------------------
15	\subsection{Representation Extraction}
16	\label{sec:repr_extraction}
17	
18	We extract representations from six sources spanning the VLA pipeline:
19	(a)~\textbf{DinoSigLIP+Projector}, the projector output (4{,}096-D), immediately before LLM processing;
20	(b)~\textbf{LLM image\_mean}, the mean image-token activation at each of 32 layers;
21	(c)~\textbf{LLM readout}, the activation at the final pre-action token position at each layer;
22	(d)~\textbf{DINOv2 ViT-L/14}~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}), a self-supervised baseline;
23	(e)~\textbf{CLIP ViT-L/14}~\cite{radford2021_clip} (\texttt{patch\_mean}), a VL-pretrained baseline;
24	(f)~\textbf{Branch-split}, the DINOv2 (1{,}024-D) and SigLIP (1{,}152-D) br
…[truncated 3645 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 116 · 2026-05-17T06:01:39.773917+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 117 · 2026-05-17T06:01:39.774649+00:00_

1	% === VLA / Architecture ===
2	
3	@article{kim2024_openvla,
4	  title     = {{OpenVLA}: An Open-Source Vision-Language-Action Model},
5	  author    = {Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balakrishna, Ashwin and Nair, Suraj and Rafailov, Rafael and Foster, Ethan and Lam, Grace and Sanketi, Pannag and Lu, Quan and Kollar, Thomas and Burchfiel, Benjamin and Tedrake, Russ and Sadigh, Dorsa and Levine, Sergey and Liang, Percy and Finn, Chelsea},
6	  journal   = {arXiv preprint arXiv:2406.09246},
7	  year      = {2024},
8	}
9	
10	@article{karamcheti2024,
11	  title     = {Prismatic {VLMs}: Investigating the Design Space of Visually-Conditioned Language Models},
12	  author    = {Karamcheti, Siddharth and Nair, Suraj and Balakrishna, Ashwin and Liang, Percy and Kollar, Thomas and Sadigh, Dorsa},
13	  journal   = {arXiv preprint arXiv:2402.07865},
14	  year      = {2024},
15	}
16	
17	@article{brohan2023_rt2,
18	  title     = {{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
19	  author    = {Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},
20	  journal   = {arXiv preprint arXiv:2307.15818},
21	  year      = {2023},
22	}
23	
24	% === Benchmark ===
25	
26	@inproceedings{liu2023_libero,
27	  title     = {{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
28	  author    = {Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},
29	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
30	  year      = {2023},
31	}
32	
33	% === Representation Analysis Methods ===
34	
35	@article{kriegeskorte2008,
36	  title     = {Representational Similarity Analysis -- Connecting the Branches of Systems Neuroscience},
37	  author    = {Kriegeskorte, Nikolaus and Mur, Marieke and Ban
…[truncated 12088 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 118 · 2026-05-17T06:01:45.848090+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 119 · 2026-05-17T06:01:46.902624+00:00_

1	\appendix
2	
3	\section{Supplementary Material}
4	\label{sec:appendix}
5	
6	\subsection{CKA Analysis Method}
7	\label{sec:cka_appendix}
8	
9	We employ Centered Kernel Alignment (CKA)~\cite{kornblith2019} alongside RSA as a complementary perspective.
10	While RSA captures local geometric alignment via rank-order preservation, CKA measures global representational similarity through kernel-based comparisons.
11	
12	We compute both \emph{linear CKA}, which uses a linear kernel and is sensitive to second-order statistics, and \emph{RDM kernel CKA}, which operates on the same distance matrices as RSA but aggregates them differently.
13	Using both variants tests whether conclusions about representation structure are robust to the choice of similarity metric.
14	
15	Linear CKA between high-dimensional representations (4{,}096-D for LLM layers) and the 7-D action space is subject to a known dimension mismatch: the linear kernel in the low-dimensional space may not capture the same structure as in the high-dimensional space.
16	RDM kernel CKA avoids this issue by operating on distance matrices of equal size regardless of the original feature dimensionality.
17	
18	\subsection{Metric Sensitivity: RSA versus CKA}
19	\label{sec:metric_sensitivity_appendix}
20	
21	Linear CKA~\cite{kornblith2019} reverses the RSA ordering: untrained LLM ($\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially inverting the self-supervised advantage (Figure~\ref{fig:metric_comparison}).
22	RDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $\approx$ Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).
23	This divergence reflects the known sensitivity of representation similarity metrics to different geometric properties.
24	
25	At the per-layer level, linear CKA between image\_mean and the action space rises monotonically from L0 ($0.081$) to L32 ($0.098$), showing no inverted-U pattern.
26	RSA captures ran
…[truncated 1947 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool call

_source line 120 · 2026-05-17T06:01:47.455186+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "llama|Llama|llm_base|pretrained.*base",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "llama|Llama|llm_base|pretrained.*base",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 121 · 2026-05-17T06:01:47.505942+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:73:Note that this comparison uses a randomly initialized LLM baseline rather than the pretrained Llama-2 checkpoint; the observed routing changes may therefore reflect a combination of language pretraining and VLA fine-tuning (see \S\ref{sec:discussion} for discussion).
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex:33:A pretrained Llama-2 base checkpoint (without VLA fine-tuning) would isolate the VLA-specific contribution; we are currently conducting this experiment.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex:10:We study OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a generalist robot policy chaining three components: a frozen DinoSigLIP fused vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\to$ 4{,}096-D), and a Llama-2 7B language backbone (6.74B parameters) that autoregressively decodes 7-dimensional actions.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex:23:(e)~\textbf{CLIP ViT-L/14}~\cite{radford2021_clip} (\texttt{patch\_mean}), a VL-pretrained baseline;
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex:12:We address this gap by decomposing OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a VLA chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2}, an MLP projector, and Llama-2 7B.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 122 · 2026-05-17T06:01:52.277107+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "---",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 123 · 2026-05-17T06:01:52.629091+00:00_

13:%------------------------------------------------------------------
53:%------------------------------------------------------------------
82:%------------------------------------------------------------------
114:DINOv2 cls\_token & \textbf{0.692} & 0.634 & --- & --- \\
116:Fused DinoSigLIP & 0.634 & --- & --- & --- \\
118:DinoSigLIP+Projector & 0.615 & 0.630 & --- & --- \\
121:CLIP ViT-L/14$^\ddagger$ & 0.557 & 0.587 & --- & --- \\
149:Instruction effect (max $|\Delta|$) & 0.006 & --- & n.s. \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Grep",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 124 · 2026-05-17T06:01:52.679792+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "---",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-17T06:01:52.730459+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 126 · 2026-05-17T06:02:11.225143+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "---",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-17T06:02:11.929626+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Grep",
  "elapsed_ms": 704
}
```

</details>

---


### Tool call

_source line 128 · 2026-05-17T06:02:12.130750+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "---",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-17T06:02:12.582683+00:00_

6:%------------------------------------------------------------------
14:%------------------------------------------------------------------
27:%------------------------------------------------------------------
35:%------------------------------------------------------------------
42:%------------------------------------------------------------------
51:%------------------------------------------------------------------

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Grep",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 130 · 2026-05-17T06:02:12.583088+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "---",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 131 · 2026-05-17T06:02:12.633588+00:00_

193:RSA profile $r$ & --- & 0.970 & --- \\
194:$R^2$ profile $r$ & --- & 0.819 & --- \\
278:DINOv2 cls\_token & --- & 82.7\% \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 132 · 2026-05-17T06:03:35.304124+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "2",
  "text": "## Round 2 修订评估 ��� Reviewer 1（方法严谨性 + 实验有效性）\n\n**模式**：继续审稿。你在 Round 1 给出 5/10。现在评估修��是否充分回应了你的问题。\n\n### Venue 信息（不变）\n- CoRL 2026, Deadline 2026-05-29, 8 页���文, double-blind\n\n### 论文路径\n`projects/vla-ssd/docs/paper/main.tex`\n\n### 你的 Round 1 主要发现摘要\n- **N1** (critical): Untrained baseline confound（random vs trained 混淆 Llama-2 预训练 + VLA fine-tuning）\n- **N3** (critical): RSA best-vs-best selection bias（32层取max，主结果 n.s.）\n- **N4** (critical): Probing encoding ≠ use，design implications 缺乏因果验证\n- **W1** (warning): \"Instruction-blind\" claim 过强（仅 linear probe）\n- **W2** (warning): CKA 反转 RSA 处理不充分\n\n### 当前 Open/In-Progress Issues（逐条标注 [RESOLVED] / [STILL_OPEN]）\n\n请���取更新后的论文，对以下 issue 逐条判定：\n\n1. **R1-N1** [in_progress]: Untrained baseline confound\n   - Action: 增加 Llama-2 base checkpoint 对照\n   - 检查：是否有新实验数据？���否���在 Limitations 中 acknowledge？acknowledge 是否充分？\n\n2. **R1-N3** [in_progress]: RSA best-vs-best selection bias\n   - Action: same-layer comparison 作为 primary framing\n   - 检查：Table 3 / §4.3 的叙事结构是否调整？best-vs-best 是否降级？\n\n3. **R1-N4** [in_progress]: Design implications speculative\n   - Action: 弱化为 hypothesis/suggestion\n   - 检查：Discussion \"Implications\" 段、Abstract 最后一句、Conclusion 最后一句的语气是否软化？\n\n4. **R1-W1** [in_progress]: \"Instruction-blind\" claim 过强\n   - Action: 补充 MLP probe 或弱化 claim\n   - 检查：§4.1 标题和正文措辞是否调整？是否有 MLP probe 结果？\n\n5. **R1-W2** [in_progress]: CKA/RSA 矛盾\n   - Action: 正文讨论 metric divergence\n   - 检查：是否在 Method 或 Discussion 中解释了为何选择 RSA？\n\n### 输出格式\n对每个 issue：[RESOLVED] / [PARTIALLY_RESOLVED] / [STILL_OPEN] + 理由（cite 具体位置）\n最后给出更新后的 Overall Score 和理由。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "2",
    "text": "## Round 2 修订评估 ��� Reviewer 1（方法严谨性 + 实验有效性）\n\n**模式**：继续审稿。你在 Round 1 给出 5/10。现在评估修��是否充分回应了你的问题。\n\n### Venue 信息（不变）\n- CoRL 2026, Deadline 2026-05-29, 8 页���文, double-blind\n\n### 论文路径\n`projects/vla-ssd/docs/paper/main.tex`\n\n### 你的 Round 1 主要发现摘要\n- **N1** (critical): Untrained baseline confound（random vs trained 混淆 Llama-2 预训练 + VLA fine-tuning）\n- **N3** (critical): RSA best-vs-best selection bias（32层取max，主结果 n.s.）\n- **N4** (critical): Probing encoding ≠ use，design implications 缺乏因果验证\n- **W1** (warning): \"Instruction-blind\" claim 过强（仅 linear probe）\n- **W2** (warning): CKA 反转 RSA 处理不充分\n\n### 当前 Open/In-Progress Issues（逐条标注 [RESOLVED] / [STILL_OPEN]）\n\n请���取更新后的论文，对以下 issue 逐条判定：\n\n1. **R1-N1** [in_progress]: Untrained baseline confound\n   - Action: 增加 Llama-2 base checkpoint 对照\n   - 检查：是否有新实验数据？���否���在 Limitations 中 acknowledge？acknowledge 是否充分？\n\n2. **R1-N3** [in_progress]: RSA best-vs-best selection bias\n   - Action: same-layer comparison 作为 primary framing\n   - 检查：Table 3 / §4.3 的叙事结构是否调整？best-vs-best 是否降级？\n\n3. **R1-N4** [in_progress]: Design implications speculative\n   - Action: 弱化为 hypothesis/suggestion\n   - 检查：Discussion \"Implications\" 段、Abstract 最后一句、Conclusion 最后一句的语气是否软化？\n\n4. **R1-W1** [in_progress]: \"Instruction-blind\" claim 过强\n   - Action: 补充 MLP probe 或弱化 claim\n   - 检查：§4.1 标题和正文措辞是否调整？是否有 MLP probe 结果？\n\n5. **R1-W2** [in_progress]: CKA/RSA 矛盾\n   - Action: 正文讨论 metric divergence\n   - 检查：是否在 Method 或 Discussion 中解释了为何选择 RSA？\n\n### 输出格式\n对每个 issue：[RESOLVED] / [PARTIALLY_RESOLVED] / [STILL_OPEN] + 理由（cite 具体位置）\n最后给出更新后的 Overall Score 和理由。"
  }
}
```

</details>

---


### Tool result

_source line 133 · 2026-05-17T06:03:51.580548+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16276
}
```

</details>

---


### Tool call

_source line 134 · 2026-05-17T06:03:51.731381+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "2",
  "text": "## Round 2 修订评估 — Reviewer 2（新颖性 + Related Work + 实际意义）\n\n**模式**：继续审稿。你在 Round 1 给出 4/10。现在评估修改是否充分回应了你的问题。\n\n### Venue 信息（不变）\n- CoRL 2026, Deadline 2026-05-29, 8 页正文, double-blind\n\n### 论文路径\n`projects/vla-ssd/docs/paper/main.tex`\n\n### 你的 Round 1 主要发现摘要\n- **N1** (critical): \"First token-level decomposition\" claim 不成立（Neo et al. ICLR 2025 + Grant 2026）\n- **N2** (critical): 无方法论创新，标准��具直接应用\n- **N3** (critical): Design implications 完全 speculative\n- **N4** (critical): 单模型单 benchmark 泛化性不足\n- **W1** (warning): Related Work 严重不足（21 引用，缺失关键文献）\n\n### 当前 Open/In-Progress Issues（逐条标注 [RESOLVED] / [STILL_OPEN]）\n\n请读取更新后的论文，对以下 issue 逐条判定：\n\n1. **R2-N1** [in_progress]: \"First\" novelty claim\n   - Action: 删除 \"first\"，引用 Neo et al.，重定位 novelty\n   - 检查：Abstract/Intro/Conclusion 是否仍含 \"first\"？Neo et al. (ICLR 2025) 是否被引用？novelty 如何重新定位？\n\n2. **R2-N2** [in_progress]: 无方法创新\n   - 上轮判断：CoRL 期望 method 或 actionable insight。R1+R3 rebut 认为 insight novelty 可弥补。\n   - 检查：论文是否增加了任何新实验/方法/��证来强化 insight novelty？\n\n3. **R2-N3** [in_progress]: Design implications speculative\n   - Action: 弱化语气或���加因果验证\n   - 检查：Discussion/Abstract/Conclusion 中 design implications 的语气是否软化？是否有新���证实验？\n\n4. **R2-N4** [in_progress]: 单模型单 benchmark\n   - 同 R1-N2��检查 Title 是否限定？claims 是否加 scope qualifier？\n\n5. **R2-W1** [in_progress]: Related Work 不足\n   - Action: 扩展至 4-6 段，40+ 引用\n   - 检查：段数、引用数、覆盖的类别。特别关注：Neo et al. (ICLR 2025) 是否被引用？logit lens？Raghu et al. 2021（ViT representation）？\n\n### 关键新问题检查\n- Related Work 扩展后，与 Grant 2026 的 differentiation 是否清晰？\n- 新增引用是否改善了 positioning？\n- 是否引入了新的问题（如过度引用无关文献）？\n\n### 输出格式\n对每个 issue：[RESOLVED] / [PARTIALLY_RESOLVED] / [STILL_OPEN] + 理由\n最后给出更新后的 Overall Score 和理由。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "2",
    "text": "## Round 2 修订评估 — Reviewer 2（新颖性 + Related Work + 实际意义）\n\n**模式**：继续审稿。你在 Round 1 给出 4/10。现在评估修改是否充分回应了你的问题。\n\n### Venue 信息（不变）\n- CoRL 2026, Deadline 2026-05-29, 8 页正文, double-blind\n\n### 论文路径\n`projects/vla-ssd/docs/paper/main.tex`\n\n### 你的 Round 1 主要发现摘要\n- **N1** (critical): \"First token-level decomposition\" claim 不成立（Neo et al. ICLR 2025 + Grant 2026）\n- **N2** (critical): 无方法论创新，标准��具直接应用\n- **N3** (critical): Design implications 完全 speculative\n- **N4** (critical): 单模型单 benchmark 泛化性不足\n- **W1** (warning): Related Work 严重不足（21 引用，缺失关键文献）\n\n### 当前 Open/In-Progress Issues（逐条标注 [RESOLVED] / [STILL_OPEN]）\n\n请读取更新后的论文，对以下 issue 逐条判定：\n\n1. **R2-N1** [in_progress]: \"First\" novelty claim\n   - Action: 删除 \"first\"，引用 Neo et al.，重定位 novelty\n   - 检查：Abstract/Intro/Conclusion 是否仍含 \"first\"？Neo et al. (ICLR 2025) 是否被引用？novelty 如何重新定位？\n\n2. **R2-N2** [in_progress]: 无方法创新\n   - 上轮判断：CoRL 期望 method 或 actionable insight。R1+R3 rebut 认为 insight novelty 可弥补。\n   - 检查：论文是否增加了任何新实验/方法/��证来强化 insight novelty？\n\n3. **R2-N3** [in_progress]: Design implications speculative\n   - Action: 弱化语气或���加因果验证\n   - 检查：Discussion/Abstract/Conclusion 中 design implications 的语气是否软化？是否有新���证实验？\n\n4. **R2-N4** [in_progress]: 单模型单 benchmark\n   - 同 R1-N2��检查 Title 是否限定？claims 是否加 scope qualifier？\n\n5. **R2-W1** [in_progress]: Related Work 不足\n   - Action: 扩展至 4-6 段，40+ 引用\n   - 检查：段数、引用数、覆盖的类别。特别关注：Neo et al. (ICLR 2025) 是否被引用？logit lens？Raghu et al. 2021（ViT representation）？\n\n### 关键新问题检查\n- Related Work 扩展后，与 Grant 2026 的 differentiation 是否清晰？\n- 新增引用是否改善了 positioning？\n- 是否引入了新的问题（如过度引用无关文献）？\n\n### 输出格式\n对每个 issue：[RESOLVED] / [PARTIALLY_RESOLVED] / [STILL_OPEN] + 理由\n最后给出更新后的 Overall Score 和理由。"
  }
}
```

</details>

---


### Tool result

_source line 135 · 2026-05-17T06:04:06.913616+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15182
}
```

</details>

---


### Tool call

_source line 136 · 2026-05-17T06:04:07.068144+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "3",
  "round_number": "2",
  "text": "## Round 2 修订评估 — Reviewer 3（写作质量 + 格式合规 + 呈现清晰度）\n\n**模式**：继续审稿。你在 Round 1 给出 6/10。现在评估修改是否充分回应了你的问题。\n\n### Venue 信息（不变）\n- CoRL 2026, Deadline 2026-05-29, 8 页正文, double-blind, 需含 Limitations section\n\n### 论文路径\n`projects/vla-ssd/docs/paper/main.tex`\n\n### 你的 Round 1 主要发现摘要\n- **N1** (critical): Limitations 格式不满足 CoRL 要求（\\paragraph{} 非独立 section，缺 failure modes）\n- **N2** (critical): 8 处解释性 em-dash\n- **W1**: 术语未定义（LOOCV, MLP, CKA）\n- **W2**: 页数可能超限\n- **W3**: -ing 分词短语\n- **W4**: Related Work 过短\n- **W5**: 无 code/data 声明\n\n### 当前 Open/In-Progress Issues（逐条标注 [RESOLVED] / [STILL_OPEN]）\n\n请读取更新后的论文，对以下 issue 逐条判定：\n\n1. **R3-N1** [in_progress]: Limitations 格式\n   - Action: 改为独立 \\subsection{} 或 \\section{}，补充 failure modes\n   - 检查：discussion.tex 中 Limitations 的格式级别。是否有 \\subsection{Limitations} 或 \\section{Limitations}？failure modes 是否被描述？\n\n2. **R3-N2** [in_progress]: Em-dash 清除\n   - Action: 全文清除所有解释性 em-dash\n   - 检查：grep \"---\" 全文，区分表格���隔符（允许）和解释性使用（禁止）。确认正文 prose 中无残留。\n\n3. **R3-W1** [in_progress]: 术语定义\n   - 检查：LOOCV 在 abstract 中是否展开或简化？MLP 首次出现是否定义？CKA 在正文首次出现是否给出全称？\n\n4. **R3-W2** [in_progress]: 页数\n   - 检查：2 个 figure 已移入 appendix（fig_rsa_bar + fig_factorial）。估算��前正文是否在 8 页内。\n\n5. **R3-W4** [in_progress]: Related Work 过短\n   - 检查：当前 Related Work 的段数和���数。是否达到 CoRL 标准（4-6 段）？\n\n6. **R3-W5** [in_progress]: Code/data 声明\n   - 检查：Conclusion 或 Limitations 后是否有 reproducibility statement？\n\n### 额外检查\n- -ing 分词短语结尾是否有改善？\n- 新增的 Related Work 文字是否有新的 AI 写作痕迹？\n- Table 1 caption 是否修正（���轮提到 \"L0-L8 shown\" 不准确）？\n- 新增 \"Why RSA over CKA\" 段落的写作质量？\n\n### 输出格式\n对每个 issue：[RESOLVED] / [PARTIALLY_RESOLVED] / [STILL_OPEN] + 理由\n最后给出更新后的 Overall Score 和理由。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "3",
    "round_number": "2",
    "text": "## Round 2 修订评估 — Reviewer 3（写作质量 + 格式合规 + 呈现清晰度）\n\n**模式**：继续审稿。你在 Round 1 给出 6/10。现在评估修改是否充分回应了你的问题。\n\n### Venue 信息（不变）\n- CoRL 2026, Deadline 2026-05-29, 8 页正文, double-blind, 需含 Limitations section\n\n### 论文路径\n`projects/vla-ssd/docs/paper/main.tex`\n\n### 你的 Round 1 主要发现摘要\n- **N1** (critical): Limitations 格式不满足 CoRL 要求（\\paragraph{} 非独立 section，缺 failure modes）\n- **N2** (critical): 8 处解释性 em-dash\n- **W1**: 术语未定义（LOOCV, MLP, CKA）\n- **W2**: 页数可能超限\n- **W3**: -ing 分词短语\n- **W4**: Related Work 过短\n- **W5**: 无 code/data 声明\n\n### 当前 Open/In-Progress Issues（逐条标注 [RESOLVED] / [STILL_OPEN]）\n\n请读取更新后的论文，对以下 issue 逐条判定：\n\n1. **R3-N1** [in_progress]: Limitations 格式\n   - Action: 改为独立 \\subsection{} 或 \\section{}，补充 failure modes\n   - 检查：discussion.tex 中 Limitations 的格式级别。是否有 \\subsection{Limitations} 或 \\section{Limitations}？failure modes 是否被描述？\n\n2. **R3-N2** [in_progress]: Em-dash 清除\n   - Action: 全文清除所有解释性 em-dash\n   - 检查：grep \"---\" 全文，区分表格���隔符（允许）和解释性使用（禁止）。确认正文 prose 中无残留。\n\n3. **R3-W1** [in_progress]: 术语定义\n   - 检查：LOOCV 在 abstract 中是否展开或简化？MLP 首次出现是否定义？CKA 在正文首次出现是否给出全称？\n\n4. **R3-W2** [in_progress]: 页数\n   - 检查：2 个 figure 已移入 appendix（fig_rsa_bar + fig_factorial）。估算��前正文是否在 8 页内。\n\n5. **R3-W4** [in_progress]: Related Work 过短\n   - 检查：当前 Related Work 的段数和���数。是否达到 CoRL 标准（4-6 段）？\n\n6. **R3-W5** [in_progress]: Code/data 声明\n   - 检查：Conclusion 或 Limitations 后是否有 reproducibility statement？\n\n### 额外检查\n- -ing 分词短语结尾是否有改善？\n- 新增的 Related Work 文字是否有新的 AI 写作痕迹？\n- Table 1 caption 是否修正（���轮提到 \"L0-L8 shown\" 不准确）？\n- 新增 \"Why RSA over CKA\" 段落的写作质量？\n\n### 输出格式\n对每个 issue：[RESOLVED] / [PARTIALLY_RESOLVED] / [STILL_OPEN] + 理由\n最后给出更新后的 Overall Score 和理由。"
  }
}
```

</details>

---


### Tool result

_source line 137 · 2026-05-17T06:04:08.531356+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_3\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1463
}
```

</details>

---


### Assistant

_source line 138 · 2026-05-17T06:04:13.223474+00:00_

Round 2 审稿任务已分配给三位 Reviewer。等待回收修订评估结果后进入交叉分享或直接汇总（取决于收敛情况）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 13

## Round 13

2 recorded events


### User

_source line 139 · 2026-05-17T06:05:40.845617+00:00_

[Reviewer 1 审稿意见]:
## Round 2 修订评估 — Reviewer 1（方法严谨性 + 实验有效性）

---

### 逐条评估

---

**1. R1-N1 [PARTIALLY_RESOLVED]: Untrained baseline confound**

修改内容：
- Section 4.2 (experiments.tex) 新增关键 caveat："Note that this comparison uses a randomly initialized LLM baseline rather than the pretrained Llama-2 checkpoint; the observed routing changes may therefore reflect a combination of language pretraining and VLA fine-tuning (see §5 for discussion)."
- Discussion Limitations 段明确承认："Our untrained control reinitializes all 6.74B LLM parameters to random weights, conflating language pretraining and VLA fine-tuning effects. A pretrained Llama-2 base checkpoint (without VLA fine-tuning) would isolate the VLA-specific contribution; we are currently conducting this experiment."

评估：
- (+) 问题被显式 acknowledge，且 caveat 放在实验章节正文中（不仅在 Limitations），这让读者在第一次遇到 trained vs. untrained 比较时就能理解局限性。
- (+) 承诺正在进行 Llama-2 base 实验。
- (-) 但核心问题仍然存在：**没有新实验数据**。Section 4.2 标题仍为 "Training Establishes Deliberate Instruction Routing"，这个 causal claim（"training establishes"）仍然超出证据支撑——如果不知道 Llama-2 base 的 attention pattern，不能排除 routing 主要来自语言预训练而非 VLA fine-tuning。
- (-) Abstract（line 5）仍写 "VLA training establishes deliberate instruction routing"，虽然从 "training learns" 改为 "VLA training establishes"，但措辞仍暗示 VLA-specific 的贡献。
- 建议：如果无法在 deadline 前完成 Llama-2 base 实验，应将标题改为 "Trained models exhibit deliberate instruction routing" 或 "The trained VLA's routing differs from random baseline"，避免 causal attribution to "VLA training"。

**判定：PARTIALLY_RESOLVED**——acknowledge 充分，但核心 claim 的措辞仍超出证据。

---

**2. R1-N3 [PARTIALLY_RESOLVED]: RSA best-vs-best selection bias**

修改内容：
- Section 4.3 叙事调整：现在先报告 best-vs-best（"modest"，acknowledged n.s.），然后强调 same-layer L12 比较（Δ = +0.079, p < 0.0001），结论为 "training has a substantial effect on *where* geometry peaks but only a modest effect on *how high*"。
- 解读策略分离为两个独立 claim（位置 shift vs. 幅度提升），这更精确。

评估：
- (+) 正文叙事确实将解读重心转向 same-layer comparison，"where" vs. "how high" 的区分是有洞察力的 framing。
- (-) Table 3 (tab:training_effects) 结构未变：best-vs-best 仍为第一行，same-layer 为第二行。表格是审稿人快速浏览的焦点——应将显著的 same-layer 结果放在更突出位置。
- (-) best-vs-best 的 n.s. 结果仍被保留在 table 中且没有 correction for multiple comparisons 的讨论。
- (-) 用 LIBERO-Spatial (p < 0.001) 来 argue LIBERO-Goal n.s. "reflects limited power" 的逻辑仍在 Appendix 中出现（虽然正文不再强调），这在方法论上仍有问题。

**判定：PARTIALLY_RESOLVED**——叙事改善明显，但 Table 结构和 multiple comparison 问题未完全解决。

---

**3. R1-N4 [PARTIALLY_RESOLVED]: Design implications speculative**

修改内容：
- Discussion "Implications" 段新增 caveat："though validating any specific architectural change would require policy rollout experiments"
- Conclusion 从 "These results reveal" 改为 "These results suggest"
- Limitations 新增 "Post-hoc analysis" 段："Our analyses characterize frozen representations; they do not address whether architectural interventions based on these observations would preserve the same action quality in closed-loop evaluation."

评估：
- (+) Discussion 中的 caveat 是正确的——承认了 representational analysis → architectural recommendation 的推理跳跃需要 rollout validation。
- (+) Limitations 的 "Post-hoc analysis" 段直接回应了我和 R2 共同指出的核心问题。
- (-) **但 Abstract 最后一句（line 8）仍为**："VLA architectures should optimize routing from image tokens to the readout position; vision encoder quality is the primary design lever." 没有任何 hedging。Abstract 是审稿人最先读到的部分，这里的强断言与 Discussion 的 caveats 不一致。
- (-) Discussion 第一条 implication 仍然是 "vision encoder pretraining quality is the primary design lever"——直接断言，未加 "our results suggest" 或 "consistent with the hypothesis that"。
- (-) "Primary design lever" 这个表述暗示因果优先级排序（投资 encoder > 投资 LLM），但论文的证据是 RSA correlation，不是因果干预。

**判定：PARTIALLY_RESOLVED**——Limitations 和 Discussion 有改善，但 Abstract 和 Discussion implications 的核心措辞仍然过于因果化。

---

**4. R1-W1 [STILL_OPEN]: "Instruction-blind" claim 过强**

修改内容：
- Section 4.1 段落标题仍为 "Image tokens are instruction-blind."
- 正文将解释性 em-dash 改为括号："This strict division of labor (instruction-blind image tokens, instruction-conditioned readout token) indicates..."
- 未添加 MLP probe 对 instruction classification 的结果。
- 未对 "instruction-blind" 的定义或 scope 进行限定。

评估：
- (-) 核心问题未回应：仍仅基于 linear probe 的 chance-level 结果声称 "instruction-blind"。
- (-) 没有新实验（MLP instruction probe 或 higher-capacity probe）来验证 claim 的鲁棒性。
- (-) 没有对 claim 进行措辞限定（如改为 "instruction identity is not linearly decodable from image tokens" 或 "image tokens lack linearly accessible instruction information"）。
- 这不影响接收决定（W-level），但作为 analytical rigor，一个标题级 claim 的证据应当匹配其强度。

**判定：STILL_OPEN**——未做任何回应。

---

**5. R1-W2 [RESOLVED]: CKA/RSA 矛盾**

修改内容：
- Method Section 3.6 新增 "Why RSA over CKA" 段（lines 59-62）：
  - 给出了选择 RSA 的 principled justification：Spearman rank correlation 的 scale-invariance 和 monotonic-transformation robustness 适合比较 dimensionality 差异大的空间。
  - 解释了 CKA linear variant 的 known dimension mismatch 问题。
  - 承认 "the partial divergence between RSA and CKA orderings confirms that neither metric alone fully characterizes representational structure"。

评估：
- (+) 这是一个 well-reasoned methodological justification。不是 post-hoc cherry-picking，而是基于 metric 的数学性质选择。
- (+) 同时承认了单一 metric 的局限性，CKA 作为 appendix complement 的定位合理。
- (+) 对审稿人的 concern 做了实质性回应：不是"两个 metric 都对"的回避，而是"为什么 RSA 更适合这个具体比较"。

**判定：RESOLVED**

---

### 总体评估

**修订力度**：中等。作者在 Limitations 和 caveats 方面做了实质性改进（尤其是 N1 的 confound acknowledge、N4 的 post-hoc caveat、W2 的 metric justification）。但三个核心问题的**实质性解决**（新实验数据、statistical correction、claim 强度与证据匹配）均未完成。

**关键残留问题**：
1. Abstract 和 Conclusion 的措辞仍然过于 assertive——Limitations 中的 caveats 不能弥补 headline claims 的过度。
2. 无 Llama-2 base 实验数据（仅 promise "currently conducting"）。
3. "Instruction-blind" claim 完全未修改。

---

### 更新后评分

**Overall: 5.5/10 → 维持 5/10（marginally below acceptance threshold）**

理由：
- 修订展示了作者对问题的理解和诚实态度（特别是 Limitations 的扩展和 "Why RSA over CKA" 段），这值得肯定。
- 但 CoRL 的 acceptance bar 要求结论可靠且 actionable。当前状态：(1) 核心对照仍有根本混淆（N1 无新数据）；(2) design implications 仍以 assertive 措辞出现在 Abstract（审稿人第一印象）；(3) 论文的 practical contribution（"optimize routing, invest in encoder"）在没有 rollout validation 的情况下仍然是 hypothesis 而非 established finding。
- 如果 Llama-2 base 实验能在 camera-ready 前完成并支持现有结论，且 Abstract/Conclusion 措辞调整为 hypothesis-generating language，我愿意将评分提升至 6/10（borderline accept）。但在当前状态下，5/10 维持不变。

**具体 actionable items（如果还有修改机会）**：
1. Abstract line 8：将 "should" 改为 "may benefit from"；将 "is the primary design lever" 改为 "emerges as a candidate primary design lever in our analysis"
2. Section 4.2 标题：从 "Training Establishes Deliberate Instruction Routing" 改为 "Trained VLA Exhibits Deliberate Instruction Routing"
3. Table 3：将 same-layer comparison 调整为第一行，best-vs-best 降级
4. Section 4.1 标题：从 "instruction-blind" 改为 "instruction-invariant at image-token positions" 或加注 "(under linear probing)"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 140 · 2026-05-17T06:05:46.219454+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 14

## Round 14

2 recorded events


### User

_source line 141 · 2026-05-17T06:05:50.384323+00:00_

[Reviewer 1 审稿结果]:
Round 2 评估已提交。总结：

- **R1-N1** (baseline confound): PARTIALLY_RESOLVED — acknowledge 充分但无新数据，标题/Abstract 措辞仍 causal
- **R1-N3** (RSA best-vs-best): PARTIALLY_RESOLVED — 叙事改善（same-layer 强调），Table 结构未调整
- **R1-N4** (speculative implications): PARTIALLY_RESOLVED — Limitations 添加了正确 caveats，但 Abstract 仍 assertive
- **R1-W1** (instruction-blind): STILL_OPEN — 无任何修改
- **R1-W2** (CKA/RSA): RESOLVED — 新增 "Why RSA over CKA" 段给出 principled justification

评分维持 **5/10**。核心原因：Limitations 中的 caveats 不能弥补 Abstract/Conclusion 中 headline claims 的过度断言，且缺少 Llama-2 base 实验的实际数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 142 · 2026-05-17T06:05:55.596439+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 15

## Round 15

2 recorded events


### User

_source line 143 · 2026-05-17T06:07:10.119282+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 2 修订评估

### 逐条判定

1. **R2-N1 "First" novelty claim** → [PARTIALLY_RESOLVED]
   - "First" 已删除，novelty 重定位为 "systematic + factorial control" ✓
   - 但 Introduction line 10 仍写 "No prior work has provided a systematic token-level decomposition"（换皮 "first"）
   - **Neo et al. (ICLR 2025) 仍未引用** — 该工作在 LLaVA 上做了 token-level layer-wise 分析（probing + attention + ablation by position），方法高度可比。不引此文，"no prior work" claim 不成立。

2. **R2-N2 无方法创新** → [STILL_OPEN]
   - 无新实验/方法/因果验证
   - "Why RSA over CKA" 段落是 justification 而非 innovation
   - 核心问题不变：标准工具直接应用

3. **R2-N3 Design implications speculative** → [PARTIALLY_RESOLVED]
   - Discussion 加了 "requires policy rollout experiments" + Limitations 加了 "Post-hoc analysis" ✓
   - 但 Abstract line 8 仍为强处方性语言："should optimize"/"primary design lever"，无 hedge
   - Abstract/Conclusion vs Discussion/Limitations 的 claims 强度不一致

4. **R2-N4 单模型单 benchmark** → [PARTIALLY_RESOLVED]
   - Abstract 现在限定 "(OpenVLA-7B on LIBERO)" ✓
   - Limitations 拆分为 Architecture scope + Task diversity ✓
   - Title 仍为复数 "Vision-Language-Action Models"，暗示一般性

5. **R2-W1 Related Work** → [PARTIALLY_RESOLVED]
   - 3→5 段，21→35 引用 ✓
   - Grant 2026 三点 differentiation 清晰有效 ✓
   - 仍缺：Neo et al. (ICLR 2025)、Raghu et al. 2021 (ViT RSA/CKA)、logit lens 系列

### Overall Score: 4/10 → 5/10 (Marginally below acceptance)

修订体现诚意但核心问题未完全解决：Neo et al. 缺失、无新方法、Abstract overclaims。

**升至 6/10 的条件（均为文字修改）：**
(a) 引用 Neo et al. 并 differentiate
(b) Abstract 最后一句改为 hypothesis 而非 prescription
(c) Title 加限定或改为不暗示一般性

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 144 · 2026-05-17T06:07:15.120338+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 16

## Round 16

2 recorded events


### User

_source line 145 · 2026-05-17T06:07:17.705212+00:00_

[Reviewer 2 审稿结果]:
已提交 Round 2 评估。核心结论：

- **5/10**（从 4/10 上调 1 分）
- 修订有实质改善（删 "first"、扩展 Related Work、增加 caveats），但三个关键问题仍在：Neo et al. 未引（直接削弱 novelty positioning）、无新方法/实验、Abstract 与 Limitations 的语气不一致
- 升至 6/10 只需文字修改：引 Neo et al.、软化 Abstract 最后一句、Title 加限定

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 146 · 2026-05-17T06:07:23.014910+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 17

## Round 17

2 recorded events


### User

_source line 147 · 2026-05-17T06:07:33.443173+00:00_

[Reviewer 3 审稿意见]:
## Reviewer 3 — Round 2 修订评估（写作质量 + 格式合规 + 呈现清晰度）

---

## 逐条状态判定

### 1. R3-N1 [PARTIALLY_RESOLVED] — Limitations 格式

**格式级别未变**：discussion.tex 中仍为 `\paragraph{Limitations.}`（第26行），未提升为 `\subsection{Limitations}` 或独立 `\section{Limitations}`。CoRL 2026 CFP 原文为 "include a Limitations section"，`\paragraph{}` 在技术上不构成 "section"。

**内容大幅改善**：从原来的4行扩展至13行，新增5个子主题：
- Architecture scope（单模型局限）✓
- Task diversity（tabletop 局限）✓ NEW
- Trained vs. untrained confound（承认 conflates language pretraining and VLA fine-tuning）✓ NEW — 直接回应 R1-N1
- Probing methodology（探针可能低估容量；RSA 非因果）✓ NEW
- Post-hoc analysis（干预可能改变观察到的模式）✓ NEW

**Failure modes**：仍未使用 "failure mode" 一词，但 "Probing methodology" 段（probes may underestimate）和 "Post-hoc analysis" 段（architectural interventions may not preserve patterns）在实质上描述了方法可能失败的情形。接近合规但不完全满足 CFP 中 "failure modes" 的明确要求。

**建议**：将 `\paragraph{Limitations.}` 改为 `\subsection{Limitations}`（一行改动），并在一处子主题中加入 "failure mode" 显式表述（如 "A potential failure mode of our probe methodology is..."）。

---

### 2. R3-N2 [RESOLVED] — Em-dash 清除

Grep 确认：正文 prose 中零残留解释性 em-dash。

修改清单：
- experiments.tex L31：`---instruction-blind...---means` → 括号改写 "(instruction-blind image tokens, instruction-conditioned readout token) indicates" ✓
- experiments.tex L69：`---architecture provides...---but` → 括号重构 "(the architecture provides incidental leakage) but strengthens" ✓
- method.tex L19-24：`\textbf{Name}---description` → `\textbf{Name}, the description` ✓（全部4处）
- appendix.tex L93, L150：em-dash 已移除，改为句号分割或括号 ✓

剩余 `---` 全部为表格 N/A 标记或 LaTeX 注释分隔线（`%---`），完全合规。

---

### 3. R3-W1 [PARTIALLY_RESOLVED] — 术语定义

| 术语 | 状态 | 详情 |
|------|------|------|
| CKA | ✓ RESOLVED | related_work.tex L36: "Centered Kernel Alignment (CKA)~\cite{kornblith2019}" — 主文首次出现即有定义 |
| LOOCV | ✗ STILL OPEN | abstract.tex L4 仍为 "LOOCV-verified"，未展开。method.tex §3.3 L33 定义了全称，但 abstract 先于 method 出现。Introduction L19 也用了未展开的 "LOOCV-verified" |
| MLP | ✗ STILL OPEN | method.tex L10 "an MLP projector"、introduction.tex L14 "MLP probes" 均未展开为 "multi-layer perceptron"。虽然 ML 社区普遍知晓，但 CoRL 受众含 robotics 工程师 |

**建议**：Abstract 中将 "LOOCV-verified" 改为 "cross-validated" 或 "leave-one-out cross-validated"。Method §3.1 首次出现 MLP 时展开一次。

---

### 4. R3-W2 [PARTIALLY_RESOLVED] — 页数

**改善明显**：主文从 5 figures + 3 tables 减至 2 figures + 3 tables。三个 figure 移入 appendix：
- fig_rsa_bar → Appendix §A.4 ✓
- fig_probe_bars → Appendix §A.6 ✓  
- fig_factorial → Appendix §A.5 ✓

**抵消因素**：Related Work 新增约 24 行文本，Method 新增 "Why RSA over CKA" 段（4行），Discussion Limitations 新增约 9 行。

**估算**：
- 减少：3 full-width figures ≈ 释放 1.0-1.2 页
- 增加：文本扩展 ≈ 0.5-0.7 页
- 净效果：节省约 0.5 页

修订后粗估：8.3-8.6 页（从原 ~9.1 页下降）。仍可能略超 8 页，但取决于 LaTeX 浮动体排版。

**建议**：编译确认。若仍超限，可考虑将 Table 1（tab_dense_routing_main）合并入正文一句话描述（"从10%跳至100%"已在文字中说明），或缩减 Method §3 的重复叙述（部分内容在 Experiments §4.1 重复出现）。

---

### 5. R3-W4 [RESOLVED] — Related Work 过短

**显著改善**：从 3 段 16 行扩展至 5 段 40 行。

新增内容覆盖：
- ¶2 "Mechanistic interpretability in transformers"：Elhage (residual stream)、Olsson (induction heads)、Wang (IOI circuits)、Conmy (greater-than)、Clark/Vig/Voita (attention analysis) ✓
- ¶4 "Token-level functional specialization"：Dosovitskiy (CLS token)、Darcet (register tokens)、Geva (FF key-value)、Tenney (pipeline probing) ✓
- ¶5 "Representation similarity and probing methodology"：RSA、SVCCA/Raghu、Morcos (PWCCA)、CKA、Hewitt (structural probes)、Belinkov ✓

**定位质量**：¶3 末尾对 Grant 2026 做了三点显式差异化（token-level vs feature-level；32-layer profile；factorial control），这是真正的 positioning 而非 survey。

**引用密度**：新增约 12 条引用（Elhage, Olsson, Wang, Conmy, Clark, Vig, Voita, Dosovitskiy, Darcet, Geva, Tenney, Raghu, Morcos, Hewitt），总引用数从 ~21 增至 ~33，达到 CoRL 论文的合理水平。

---

### 6. R3-W5 [STILL_OPEN] — Code/data 声明

Conclusion 和 Discussion 中均无 reproducibility statement。论文未在任何位置承诺释放代码、数据或分析脚本。

**建议**：在 Conclusion 末尾加一句："Code for representation extraction and analysis will be released upon acceptance." 注意 double-blind 阶段不可包含可识别 URL。

---

## 额外检查

### -ing 分词短语
有改善但未完全消除：
- experiments.tex L69：原 "does not enable routing...but transforms" 改为 "does not create routing from scratch...but strengthens" — 去除了 -ing ✓
- experiments.tex L78 (caption)："creating a robust signal maintained through L31" — 仍保留 ✗ (minor)
- appendix.tex L93："requiring deeper processing" — 仍保留 ✗ (appendix, 影响很小)
- 总体密度大幅降低，不再构成系统性 AI 痕迹

### 新增 Related Work 写作质量
写作清晰，无 AI 标志：
- 无 em-dash ✓
- 无 "Furthermore/Moreover/Additionally" 连续使用 ✓
- 各段有明确 positioning 角度（不是 "A did X. B did Y." 列表）✓
- 最后一句都回扣本文贡献 ✓

### Table 1 Caption
**仍有问题**：Caption 写 "(L0--L8 shown; full profile in Appendix)" 但表格实际展示 L0, L1, L4, L8, L16, L31（远超 L8）。这是一个 factual inaccuracy。应改为 "(selected layers shown; full L0--L31 profile in Appendix)"。

### "Why RSA over CKA" 段落（method.tex L59-62）
写作质量优秀：
- 清晰说明 RSA 的 scale-invariance 优势 ✓
- 点明 CKA linear kernel 的 dimension mismatch 问题 ✓
- 诚实承认 divergence ✓
- 无 AI 痕迹 ✓
- 为 appendix 中详细 CKA 结果提供了合理 framing

### 叙事一致性改善
- Introduction L20: "training learns" → "VLA training establishes" — 更精确，避免过度拟人
- Introduction L27: "the first" → "a systematic" — 降低 novelty claim 强度
- Conclusion L4: 同步更新 — 主线一致性良好
- experiments.tex L73: 新增对 confound 的显式 caveat — 增加了写作诚实度

---

## 更新后评分

**Overall: 7/10 (Accept — conditional on minor format fixes)**

**评分变化理由（6→7）**：
1. **Em-dash 完全清除** — 最显著的 AI 痕迹已消除，这是 Round 1 最高优先级问题
2. **Related Work 达标** — 从严重不足变为 CoRL 标准的充分 positioning
3. **"Why RSA over CKA" 增加** — 正面回应了方法论选择的 transparency
4. **Confound 显式承认** — 在 experiments 和 limitations 中都增加了 caveat，写作诚实度提升
5. **Figures 移入 appendix** — 信息密度更合理

**仍需修复才能 Accept**（均为一行/一句改动）：
1. `\paragraph{Limitations.}` → `\subsection{Limitations}` （格式合规硬性要求）
2. Abstract "LOOCV-verified" → "cross-validated" 或展开
3. Table 1 caption "(L0--L8 shown)" → "(selected layers shown)"
4. 加入 reproducibility statement

**无法在本轮升至 8/10 的原因**：
- Limitations 格式仍不满足 CoRL CFP 字面要求（非 section）
- 页数未经编译确认（写作审查只能估算）
- 缺少 reproducibility statement（CoRL 社区重视开源）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_3"
}
```

</details>

---


### Assistant

_source line 148 · 2026-05-17T06:07:38.308522+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 18

## Round 18

8 recorded events


### User

_source line 149 · 2026-05-17T06:07:44.158123+00:00_

[Reviewer 3 审稿结果]:
Round 2 评估已提交。总结：从 6/10 提升至 7/10。Em-dash 清除、Related Work 扩展、confound 承认等核心问题已解决。剩余 4 个 minor 修复项（Limitations 格式提升为 subsection、LOOCV 展开、Table 1 caption 修正、reproducibility statement），均为一行改动。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_3"
}
```

</details>

---


### Tool call

_source line 150 · 2026-05-17T06:08:17.365715+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "2",
  "text": "## Round 2 Step 2 交叉确认（简化版）\n\nR2 评分 5/10，R3 评分 7/10。请简要回应：\n\n**R2 关键判定**：\n- R2-N1: Neo et al. (ICLR 2025) 仍未引用，Introduction \"No prior work has provided a systematic token-level decomposition\" 构成换皮 \"first\" claim\n- R2-N2: 无方法创新问题维持 STILL_OPEN\n- R2 认为 Abstract 与 Limitations 语气不一致是核心残留问题\n\n**R3 关键判定**（7/10, conditional accept）：\n- Em-dash 完全清除 ✓\n- Related Work 达标 ✓\n- 剩余问题均为一行修改（Limitations \\subsection、LOOCV 展开、Table 1 caption、reproducibility statement）\n- R3 认为如果这 4 个 minor fix 完成，论文在写作/格式维度达到 accept 标准\n\n**问题**：\n1. R2 指出的 Neo et al. 缺失是否影响你对论文 internal validity 的评估？（即：如果 novelty positioning 进一步被削弱，你的 5/10 是否会下调？）\n2. R3 的 conditional accept (7/10) 是否改变你对论文整体 acceptability 的判断？\n\n请用 2-3 句话回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "2",
    "text": "## Round 2 Step 2 交叉确认（简化版）\n\nR2 评分 5/10，R3 评分 7/10。请简要回应：\n\n**R2 关键判定**：\n- R2-N1: Neo et al. (ICLR 2025) 仍未引用，Introduction \"No prior work has provided a systematic token-level decomposition\" 构成换皮 \"first\" claim\n- R2-N2: 无方法创新问题维持 STILL_OPEN\n- R2 认为 Abstract 与 Limitations 语气不一致是核心残留问题\n\n**R3 关键判定**（7/10, conditional accept）：\n- Em-dash 完全清除 ✓\n- Related Work 达标 ✓\n- 剩余问题均为一行修改（Limitations \\subsection、LOOCV 展开、Table 1 caption、reproducibility statement）\n- R3 认为如果这 4 个 minor fix 完成，论文在写作/格式维度达到 accept 标准\n\n**问题**：\n1. R2 指出的 Neo et al. 缺失是否影响你对论文 internal validity 的评估？（即：如果 novelty positioning 进一步被削弱，你的 5/10 是否会下调？）\n2. R3 的 conditional accept (7/10) 是否改变你对论文整体 acceptability 的判断？\n\n请用 2-3 句话回应。"
  }
}
```

</details>

---


### Tool result

_source line 151 · 2026-05-17T06:08:27.369106+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 10003
}
```

</details>

---


### Tool call

_source line 152 · 2026-05-17T06:08:27.419887+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "2",
  "text": "## Round 2 Step 2 交叉确认（简化版）\n\nR1 评分 5/10，R3 评分 7/10。请简要回应：\n\n**R1 关键判定**：\n- R1-W2 RESOLVED: \"Why RSA over CKA\" 段提供了 principled justification\n- R1-N1: baseline confound — acknowledge 充分但无数据，标题/abstract 措辞仍 causal\n- R1 指出具体 actionable items: Abstract \"should\"→\"may benefit from\"，Section 4.2 标题改为观察性\n- R1 认为 5/10 维持，若 Llama-2 base 数据 + Abstract 软化可升至 6\n\n**R3 关键判定**（7/10）：\n- 从写作维度 conditional accept\n- 仅需 4 个一行修改\n- R3 的 7/10 是基于写作/格式评价，不含科学方法论评估\n\n**问题**：\n1. R1 将 CKA/RSA 问题标为 RESOLVED——你是否同意 \"Why RSA over CKA\" 段充分回应了你在 R1 轮提出的 metric divergence concern？\n2. 如果 Abstract 最后一句如 R1 建议改为 hypothesis 语气，是否足以消除你对 overclaiming 的核心 concern？\n\n请用 2-3 句话回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "2",
    "text": "## Round 2 Step 2 交叉确认（简化版）\n\nR1 评分 5/10，R3 评分 7/10。请简要回应：\n\n**R1 关键判定**：\n- R1-W2 RESOLVED: \"Why RSA over CKA\" 段提供了 principled justification\n- R1-N1: baseline confound — acknowledge 充分但无数据，标题/abstract 措辞仍 causal\n- R1 指出具体 actionable items: Abstract \"should\"→\"may benefit from\"，Section 4.2 标题改为观察性\n- R1 认为 5/10 维持，若 Llama-2 base 数据 + Abstract 软化可升至 6\n\n**R3 关键判定**（7/10）：\n- 从写作维度 conditional accept\n- 仅需 4 个一行修改\n- R3 的 7/10 是基于写作/格式评价，不含科学方法论评估\n\n**问题**：\n1. R1 将 CKA/RSA 问题标为 RESOLVED——你是否同意 \"Why RSA over CKA\" 段充分回应了你在 R1 轮提出的 metric divergence concern？\n2. 如果 Abstract 最后一句如 R1 建议改为 hypothesis 语气，是否足以消除你对 overclaiming 的核心 concern？\n\n请用 2-3 句话回应。"
  }
}
```

</details>

---


### Tool result

_source line 153 · 2026-05-17T06:08:34.127350+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 6707
}
```

</details>

---


### Tool call

_source line 154 · 2026-05-17T06:08:34.127705+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "3",
  "round_number": "2",
  "text": "## Round 2 Step 2 交叉确认（简化版）\n\nR1 和 R2 均给出 5/10，你给出 7/10。请简要回应：\n\n**R1+R2 的核心残留问题**：\n1. Abstract line 8 仍为强处方性语言（\"should optimize\"/\"primary design lever\"），与 Limitations 的 caveats 不一致\n2. Neo et al. (ICLR 2025) 仍未引用（VLM token-level 分析直接先行工作）\n3. 无 Llama-2 base 实验数据，Finding 2 \"VLA training establishes routing\" 的因果归因仍有混淆\n4. Title \"Vision-Language-Action Models\"（复数）仍暗示一般性\n\n**问题**：\n1. 作为写作审查者，你是否认为 Abstract/Conclusion 与 Limitations 的语气不一致构成**写作层面**的问题（独立于科学问题）？\n2. 这些科学层面的残留问题是否会让你将整体推荐从 7/10 下调？\n\n请用 2-3 句话回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "3",
    "round_number": "2",
    "text": "## Round 2 Step 2 交叉确认（简化版）\n\nR1 和 R2 均给出 5/10，你给出 7/10。请简要回应：\n\n**R1+R2 的核心残留问题**：\n1. Abstract line 8 仍为强处方性语言（\"should optimize\"/\"primary design lever\"），与 Limitations 的 caveats 不一致\n2. Neo et al. (ICLR 2025) 仍未引用（VLM token-level 分析直接先行工作）\n3. 无 Llama-2 base 实验数据，Finding 2 \"VLA training establishes routing\" 的因果归因仍有混淆\n4. Title \"Vision-Language-Action Models\"（复数）仍暗示一般性\n\n**问题**：\n1. 作为写作审查者，你是否认为 Abstract/Conclusion 与 Limitations 的语气不一致构成**写作层面**的问题（独立于科学问题）？\n2. 这些科学层面的残留问题是否会让你将整体推荐从 7/10 下调？\n\n请用 2-3 句话回应。"
  }
}
```

</details>

---


### Tool result

_source line 155 · 2026-05-17T06:08:35.493421+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_3\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1365
}
```

</details>

---


### Assistant

_source line 156 · 2026-05-17T06:08:40.283576+00:00_

Round 2 交叉确认已发送，等待三位 Reviewer 简短回应后汇总最终报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 19

## Round 19

2 recorded events


### User

_source line 157 · 2026-05-17T06:08:45.032565+00:00_

[Reviewer 1 审稿意见]:
## Round 2 Step 2 交叉确认 — Reviewer 1

**Q1: Neo et al. 缺失是否影响 internal validity 评估？**

不影响我的评分。Neo et al. 分析 VLM (LLaVA) 而非 VLA，方法也不同（他们未做 trained/untrained factorial control）。Introduction 的 "No prior work has provided a systematic token-level decomposition of a VLA" 如果严格限定在 VLA + systematic multi-metric，仍可站住脚。这是 novelty positioning/framing 问题，不是 internal validity 问题。我的 5/10 基于实验设计缺陷（N1 baseline confound、N4 无因果验证），不基于 novelty claim 的措辞——即使 novelty 进一步削弱，评分不会下调（已在 borderline 区间）。但同意 R2 的建议：应引用 Neo et al. 并明确区分。

**Q2: R3 的 7/10 是否改变我的判断？**

不改变。R3 的 7/10 基于写作/格式/presentation 维度的评估，这些问题确实 trivially fixable。但我的 5/10 基于方法论问题（baseline confound、causal gap），这些不是格式修复能解决的。三位 reviewer 的分歧反映了审查侧重不同：R3 看 presentation readiness，我看 scientific rigor。两个维度都重要，但在 CoRL 的 acceptance decision 中，如果 contribution 的可靠性存疑（trained vs. random 的混淆无法通过 Limitations ���落解决），presentation 达标不足以 compensate。维持 5/10。

---

[Reviewer 2 审稿意见]:
## Reviewer 2 ��� Round 2 Step 2 交叉确认

**Q1 (CKA/RSA)**: 同意 RESOLVED。method.tex "Why RSA over CKA" 段提供了 principled argument（scale-invariance + dimension mismatch），且明确将 CKA 作为 complementary perspective 在 appendix 报告。这比 Round 1 的"两个指标说不同的话我们选对我们有利的"处理方式好得多��

**Q2 (Abstract overclaiming)**: Abstract 最后一句改为 hypothesis 语气能消除 overclaiming concern 的大部分（约 80%）。但如果 Neo et al. 仍不引用，即使语气软化，novelty positioning 仍有缺陷——那是一个独立问题，不被 hedging 解决。两者都做到才能让我升至 6/10。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 158 · 2026-05-17T06:08:53.067546+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 20

## Round 20

2 recorded events


### User

_source line 159 · 2026-05-17T06:08:54.139436+00:00_

[Reviewer 1 审稿结果]:


---

[Reviewer 2 审稿结果]:
已提交。两个回答的要点：

1. **CKA/RSA**: 同意 R1 的 RESOLVED 判定。"Why RSA over CKA" 段提供了有原则的论证。
2. **Abstract hedge**: 能消除 overclaiming 的大部分，但如果 Neo et al. 仍不引用，novelty positioning 仍有独立缺陷。两者都需要才能升至 6/10。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 160 · 2026-05-17T06:08:59.298597+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 21

## Round 21

6 recorded events


### User

_source line 161 · 2026-05-17T06:09:06.252513+00:00_

[Reviewer 3 审稿意见]:
## Reviewer 3 — Round 2 Step 2 交叉确认

**Q1: Abstract/Conclusion 与 Limitations 的语气不一致是否构成写作问题？**

是的。Abstract L8 "should optimize" / "primary design lever" 是未经 hedge 的处方性断言，而 Discussion §Limitations "Post-hoc analysis" 段明确承认 "they do not address whether architectural interventions... would preserve the same action quality"。同一篇论文中，开头做强处方 → 结尾否认验证能力，构成 §1.2 主线统一性问题。修复方式：Abstract 末句加 hedge（如 "our results suggest that..."已在 Conclusion L8 使用，但 Abstract L8 缺少），或改为 "These findings motivate optimizing routing... and prioritizing vision encoder quality as a design lever."

**Q2: 是否下调 7/10？**

不下调。语气不一致属 should-fix（一句话可修），Neo et al. 缺引属 Related Work 完整性（加一句即可），两者不足以拉回 critical 级别。科学层面的 confound 和 title 泛化性问题在我审查维度（写作/格式/呈现）上只体现为措辞选择，非结构性缺陷。维持 7/10，附加条件：Abstract 末句需 hedge。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_3"
}
```

</details>

---


### Tool call

_source line 162 · 2026-05-17T06:10:18.187203+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "vla-ssd",
  "issues_yaml": "issues:\n  - id: R1-N1\n    summary: \"Untrained baseline (random weights) 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识。需增加 Llama-2 base checkpoint 作为中间对照\"\n      - round: 2\n        reviewers: [1, 2, 3]\n        note: \"PARTIALLY_RESOLVED: experiments.tex L73 + Limitations 均 acknowledge confound，但无新实验数据。Section 4.2 标题和 Abstract L5 仍使用 causal language ('VLA training establishes')\"\n    action_items:\n      - round: 1\n        action: \"增加 Llama-2 base checkpoint 对照实验\"\n        assigned_to: research\n        status: in_progress\n      - round: 2\n        action: \"Section 4.2 标题改为观察性 ('Trained VLA Exhibits...')；Abstract L5 弱化 causal attribution\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N2\n    summary: \"单一模型(OpenVLA-7B) + 单一 benchmark family(LIBERO)，Title/Abstract 使用复数 'VLAs' 构成 overclaim\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识\"\n      - round: 2\n        reviewers: [1, 2, 3]\n        note: \"PARTIALLY_RESOLVED: Abstract 限定了 '(OpenVLA-7B on LIBERO)'，Limitations 拆分为 Architecture scope + Task diversity。但 Title 仍为复数。\"\n    action_items:\n      - round: 2\n        action: \"Title 加限定（如 'A Case Study of OpenVLA' 或改为单数 'a Vision-Language-Action Model'）\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N4\n    summary: \"Design implications 完全基于 correlational evidence，Abstract/Conclusion 以 assertive 语气呈现，与 Limitations 的 caveats 不一致\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识\"\n      - round: 2\n        reviewers: [1, 2, 3]\n        note: \"PARTIALLY_RESOLVED: Discussion 加了 'requires rollout experiments' caveat + Limitations 加了 'Post-hoc analysis'。但 Abstract L8 仍为 'should optimize'/'primary design lever'，无 hedge。全票认为 Abstract 需修改。\"\n    action_items:\n      - round: 2\n        action: \"Abstract L8 改为 hypothesis 语气：'These findings suggest that VLA architectures may benefit from optimizing routing...; vision encoder quality emerges as a candidate primary design lever'\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N3\n    summary: \"RSA best-vs-best selection bias；same-layer comparison 应为 primary framing\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"2:1 critical\"\n      - round: 2\n        reviewers: [1]\n        note: \"PARTIALLY_RESOLVED: 叙事改善（'where vs how high' 区分），但 Table 3 结构未变（best-vs-best 仍为首行）\"\n    action_items:\n      - round: 2\n        action: \"Table 3 将 same-layer comparison 调整为第一行\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-N1\n    summary: \"Neo et al. (ICLR 2025) 仍未引用；Introduction 'No prior work' 构成换皮 first claim\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R2 critical, R1+R3 同意需限定\"\n      - round: 2\n        reviewers: [2]\n        note: \"PARTIALLY_RESOLVED: 'first' 删除，但 Neo et al. 仍未引用。R1 认为限定为 'VLA + systematic multi-metric' 可站住脚但仍应引用。\"\n    action_items:\n      - round: 2\n        action: \"引用 Neo et al. (ICLR 2025)；Introduction L10 改为 'No prior work has provided a systematic multi-metric decomposition of a VLA with factorial controls'\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W1\n    summary: \"Related Work 引用覆盖度\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"21 citations 严重不足\"\n      - round: 2\n        reviewers: [2, 3]\n        note: \"PARTIALLY_RESOLVED: 扩展至 5 段 ~33 citations，Grant 2026 三点 differentiation 清晰。仍缺 Neo et al.、Raghu et al. 2021、logit lens。\"\n    action_items:\n      - round: 2\n        action: \"补充 Neo et al., Raghu et al. 2021, logit lens 引用\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W1\n    summary: \"'Instruction-blind' claim 过强（仅 linear probe 为 chance）\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识\"\n      - round: 2\n        reviewers: [1]\n        note: \"STILL_OPEN: 段落标题、正文措辞、实验均未修改\"\n    action_items:\n      - round: 2\n        action: \"补充 MLP probe instruction classification 结果；或将 §4.1 标题改为 'instruction-invariant (under linear probing)'\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W2\n    summary: \"CKA 反转 RSA 排序处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"RESOLVED: Method §3.6 'Why RSA over CKA' 段提供 principled justification（scale-invariance + dimension mismatch），全票认可。\"\n    action_items: []\n    resolution: \"Method 新增 'Why RSA over CKA' 段落，解释 RSA 的 scale-invariance 优势和 CKA linear kernel 的 dimension mismatch 问题\"\n    resolution_round: 2\n\n  - id: R3-N1\n    summary: \"Limitations 格式不满足 CoRL 2026 要求（\\\\paragraph{} 非独立 section）\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R3 标为 critical 格式合规问题\"\n      - round: 2\n        reviewers: [3]\n        note: \"PARTIALLY_RESOLVED: 内容大幅扩展（5 子主题），但格式仍为 \\\\paragraph{}。一行改动即可修复。\"\n    action_items:\n      - round: 2\n        action: \"\\\\paragraph{Limitations.} → \\\\subsection{Limitations}\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-N2\n    summary: \"正文解释性 em-dash 是 AI 写作标志\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"至少 8 处\"\n      - round: 2\n        reviewers: [3]\n        note: \"RESOLVED: 正文 prose 中零残留解释性 em-dash（grep 确认）\"\n    action_items: []\n    resolution: \"所有解释性 em-dash 已改为逗号/括号/分句，剩余 --- 仅为表格 N/A 和注释分隔线\"\n    resolution_round: 2\n\n  - id: R3-W5\n    summary: \"无 code/data 释放声明\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 3]\n        note: \"CoRL 鼓励 reproducibility\"\n      - round: 2\n        reviewers: [3]\n        note: \"STILL_OPEN: Conclusion 和 Discussion 中均无 reproducibility statement\"\n    action_items:\n      - round: 2\n        action: \"Conclusion 末尾加 'Code and extracted representations will be released upon acceptance.'\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "vla-ssd",
    "issues_yaml": "issues:\n  - id: R1-N1\n    summary: \"Untrained baseline (random weights) 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识。需增加 Llama-2 base checkpoint 作为中间对照\"\n      - round: 2\n        reviewers: [1, 2, 3]\n        note: \"PARTIALLY_RESOLVED: experiments.tex L73 + Limitations 均 acknowledge confound，但无新实验数据。Section 4.2 标题和 Abstract L5 仍使用 causal language ('VLA training establishes')\"\n    action_items:\n      - round: 1\n        action: \"增加 Llama-2 base checkpoint 对照实验\"\n        assigned_to: research\n        status: in_progress\n      - round: 2\n        action: \"Section 4.2 标题改为观察性 ('Trained VLA Exhibits...')；Abstract L5 弱化 causal attribution\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N2\n    summary: \"单一模型(OpenVLA-7B) + 单一 benchmark family(LIBERO)，Title/Abstract 使用复数 'VLAs' 构成 overclaim\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识\"\n      - round: 2\n        reviewers: [1, 2, 3]\n        note: \"PARTIALLY_RESOLVED: Abstract 限定了 '(OpenVLA-7B on LIBERO)'，Limitations 拆分为 Architecture scope + Task diversity。但 Title 仍为复数。\"\n    action_items:\n      - round: 2\n        action: \"Title 加限定（如 'A Case Study of OpenVLA' 或改为单数 'a Vision-Language-Action Model'）\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N4\n    summary: \"Design implications 完全基于 correlational evidence，Abstract/Conclusion 以 assertive 语气呈现，与 Limitations 的 caveats 不一致\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识\"\n      - round: 2\n        reviewers: [1, 2, 3]\n        note: \"PARTIALLY_RESOLVED: Discussion 加了 'requires rollout experiments' caveat + Limitations 加了 'Post-hoc analysis'。但 Abstract L8 仍为 'should optimize'/'primary design lever'，无 hedge。全票认为 Abstract 需修改。\"\n    action_items:\n      - round: 2\n        action: \"Abstract L8 改为 hypothesis 语气：'These findings suggest that VLA architectures may benefit from optimizing routing...; vision encoder quality emerges as a candidate primary design lever'\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N3\n    summary: \"RSA best-vs-best selection bias；same-layer comparison 应为 primary framing\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"2:1 critical\"\n      - round: 2\n        reviewers: [1]\n        note: \"PARTIALLY_RESOLVED: 叙事改善（'where vs how high' 区分），但 Table 3 结构未变（best-vs-best 仍为首行）\"\n    action_items:\n      - round: 2\n        action: \"Table 3 将 same-layer comparison 调整为第一行\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-N1\n    summary: \"Neo et al. (ICLR 2025) 仍未引用；Introduction 'No prior work' 构成换皮 first claim\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R2 critical, R1+R3 同意需限定\"\n      - round: 2\n        reviewers: [2]\n        note: \"PARTIALLY_RESOLVED: 'first' 删除，但 Neo et al. 仍未引用。R1 认为限定为 'VLA + systematic multi-metric' 可站住脚但仍应引用。\"\n    action_items:\n      - round: 2\n        action: \"引用 Neo et al. (ICLR 2025)；Introduction L10 改为 'No prior work has provided a systematic multi-metric decomposition of a VLA with factorial controls'\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W1\n    summary: \"Related Work 引用覆盖度\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"21 citations 严重不足\"\n      - round: 2\n        reviewers: [2, 3]\n        note: \"PARTIALLY_RESOLVED: 扩展至 5 段 ~33 citations，Grant 2026 三点 differentiation 清晰。仍缺 Neo et al.、Raghu et al. 2021、logit lens。\"\n    action_items:\n      - round: 2\n        action: \"补充 Neo et al., Raghu et al. 2021, logit lens 引用\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W1\n    summary: \"'Instruction-blind' claim 过强（仅 linear probe 为 chance）\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识\"\n      - round: 2\n        reviewers: [1]\n        note: \"STILL_OPEN: 段落标题、正文措辞、实验均未修改\"\n    action_items:\n      - round: 2\n        action: \"补充 MLP probe instruction classification 结果；或将 §4.1 标题改为 'instruction-invariant (under linear probing)'\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W2\n    summary: \"CKA 反转 RSA 排序处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"RESOLVED: Method §3.6 'Why RSA over CKA' 段提供 principled justification（scale-invariance + dimension mismatch），全票认可。\"\n    action_items: []\n    resolution: \"Method 新增 'Why RSA over CKA' 段落，解释 RSA 的 scale-invariance 优势和 CKA linear kernel 的 dimension mismatch 问题\"\n    resolution_round: 2\n\n  - id: R3-N1\n    summary: \"Limitations 格式不满足 CoRL 2026 要求（\\\\paragraph{} 非独立 section）\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R3 标为 critical 格式合规问题\"\n      - round: 2\n        reviewers: [3]\n        note: \"PARTIALLY_RESOLVED: 内容大幅扩展（5 子主题），但格式仍为 \\\\paragraph{}。一行改动即可修复。\"\n    action_items:\n      - round: 2\n        action: \"\\\\paragraph{Limitations.} → \\\\subsection{Limitations}\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-N2\n    summary: \"正文解释性 em-dash 是 AI 写作标志\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"至少 8 处\"\n      - round: 2\n        reviewers: [3]\n        note: \"RESOLVED: 正文 prose 中零残留解释性 em-dash（grep 确认）\"\n    action_items: []\n    resolution: \"所有解释性 em-dash 已改为逗号/括号/分句，剩余 --- 仅为表格 N/A 和注释分隔线\"\n    resolution_round: 2\n\n  - id: R3-W5\n    summary: \"无 code/data 释放声明\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 3]\n        note: \"CoRL 鼓励 reproducibility\"\n      - round: 2\n        reviewers: [3]\n        note: \"STILL_OPEN: Conclusion 和 Discussion 中均无 reproducibility statement\"\n    action_items:\n      - round: 2\n        action: \"Conclusion 末尾加 'Code and extracted representations will be released upon acceptance.'\"\n        assigned_to: research\n        status: open\n    resolution: \"\"\n    resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 163 · 2026-05-17T06:10:18.238037+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml\", \"bytes\": 7545}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 164 · 2026-05-17T06:11:31.834681+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "vla-ssd",
  "report": "# 圆桌审稿报告 — Round 2（修订评估）\n\n**论文**: \"Vision Encodes, Language Routes: A Representational Decomposition of Vision-Language-Action Models\"\n**Venue**: CoRL 2026 (Deadline: 2026-05-29)\n**Reviewers**: R1 (方法/实验), R2 (新颖性/意义), R3 (写作/格式)\n\n---\n\n## Summary\n\nRound 2 论文在写作和 framing 层面有实质改善：删除 \"first\" novelty claim、Related Work 从 3 段扩展至 5 段（+12 引用）、新增 \"Why RSA over CKA\" 方法论辩护、正文 em-dash 全部清除、Limitations 内容大幅扩展、confound 在实验章节显式 acknowledge。但核心科学问题（Llama-2 base 对照缺失、design implications 的因果 gap）未通过新实验数据解决，Abstract/Conclusion 的 assertive 语气与 Limitations 的 caveats 存在不一致。\n\n---\n\n## Round 1 → Round 2 变化总结\n\n### 已解决 (RESOLVED)\n| Issue | 状态 | 修改内容 |\n|-------|------|----------|\n| R1-W2 CKA/RSA 矛盾 | ✅ RESOLVED | Method 新增 \"Why RSA over CKA\" 段，全票认可 |\n| R3-N2 Em-dash AI 痕迹 | ✅ RESOLVED | 正文 prose 零残留解释性 em-dash |\n| R3-W4 Related Work 过短 | ✅ RESOLVED | 3→5 段，21→33 引用，覆盖 4 个新类别 |\n\n### 部分解决 (PARTIALLY_RESOLVED)\n| Issue | 状态 | 残留问题 |\n|-------|------|----------|\n| R1-N1 Baseline confound | ⚠️ | 充分 acknowledge，但无新数据；标题/Abstract 仍 causal |\n| R1-N4 Speculative implications | ⚠️ | Discussion caveat 良好，但 Abstract L8 仍为 \"should\"/\"primary lever\" 无 hedge |\n| R1-N2/R2-N4 单模型泛化性 | ⚠️ | Abstract 限定了 \"(OpenVLA-7B)\"，但 Title 仍复数 |\n| R2-N1 Novelty positioning | ⚠️ | \"First\" 删除，但 Neo et al. 仍未引用 |\n| R1-N3 RSA selection bias | ⚠️ | 叙事改善（\"where vs how high\"），Table 结构未调整 |\n| R2-W1 Related Work 覆盖 | ⚠️ | 33 引用达标，但仍缺 Neo et al. + Raghu et al. 2021 |\n| R3-N1 Limitations 格式 | ⚠️ | 内容充分，格式仍为 \\paragraph{}（需改 \\subsection） |\n\n### 未解决 (STILL_OPEN)\n| Issue | 状态 | 说明 |\n|-------|------|------|\n| R1-W1 \"Instruction-blind\" overclaim | ❌ | 无任何修改（标题、措辞、实验均未动） |\n| R3-W5 Code/data 声明 | ❌ | 未添加 |\n| R2-N2 无方法创新 | ❌ | 无新方法/验证实验（R1+R3 认为可通过 insight novelty 弥补）|\n\n---\n\n## Strengths（Round 2 新增/强化）\n\n1. **Confound 的透明度显著提升**：在实验章节正文（非仅 Limitations）即 acknowledge baseline 的局限性，让读者在遇到数据时就能正确理解 scope\n2. **\"Why RSA over CKA\" 方法论辩护**：不是 post-hoc cherry-picking，而是基于 metric 数学性质的 principled argument（scale-invariance for cross-dimensional comparison）\n3. **Related Work positioning 质量高**：Grant 2026 的三点显式差异化（token-level vs feature-level；32-layer profile；factorial control）是真正的 positioning 而非 survey\n4. **写作修订到位**：em-dash 清除、section 标题从 \"learns\" → \"establishes\"、contribution list 重定位\n\n---\n\n## Weaknesses（Round 2 残留）\n\n### Critical（影响接收决定）\n\n**W-Critical-1: Abstract/Conclusion 与 Limitations 的语气不一致**\n- Abstract L8: \"VLA architectures should optimize routing; vision encoder quality is the primary design lever\" — 未加任何 hedge\n- Conclusion L8: \"These results suggest that VLA architectures should optimize routing...\" — 有 \"suggest\" 但 \"should\" 仍在\n- Discussion Limitations: \"they do not address whether architectural interventions... would preserve action quality\"\n- **内部矛盾**：开头做强处方 → 结尾否认验证能力\n- **全票共识需修改**\n\n**W-Critical-2: 无 Llama-2 base 实验数据（核心 confound 未消除）**\n- 论文承认 \"currently conducting\" 但未在本版呈现数据\n- Finding 2 \"VLA training establishes deliberate instruction routing\" 的因果归因仍不完全成立\n- 如果 Llama-2 base 也展现 instruction-dominant attention → 核心叙事需根本重写\n- **R1 核心 concern，R2 AGREE**\n\n**W-Critical-3: Neo et al. (ICLR 2025) 未引用**\n- VLM token-level layer-wise 分析的直接先行工作（probing + attention + position ablation on LLaVA）\n- Introduction L10 \"No prior work has provided a systematic token-level decomposition\" 在 VLM 文献存在的情况下不完全成立\n- **R2 核心 concern，R1 同意应引用但认为不影响 internal validity**\n\n### Warning（影响评分）\n\n**W-Warning-1: Title 仍为复数 \"Vision-Language-Action Models\"**\n- 暗示一般性结论，与单模型证据不匹配\n- **全票共识**\n\n**W-Warning-2: \"Instruction-blind\" claim 完全未修改**\n- Section 4.1 段落标题仍为 \"Image tokens are instruction-blind\"\n- 无 MLP probe instruction classification 实验\n- 无措辞限定\n- **R1 标为 STILL_OPEN**\n\n**W-Warning-3: Limitations 格式仍为 \\paragraph{}**\n- CoRL 2026 CFP: \"include a Limitations section\"\n- 一行改动 (\\paragraph → \\subsection) 即可修复\n- **R3 标注**\n\n---\n\n## Reviewer Consensus [Round 2]\n\n所有 Reviewer 达成共识：\n1. Abstract L8 必须加 hedge（\"suggest\"/\"may benefit from\"/\"emerges as a candidate\"）\n2. Neo et al. 应被引用并 differentiate\n3. CKA/RSA 问题已 RESOLVED\n4. 修订展示了作者的诚实态度和对问题的理解\n5. 论文在写作/呈现维度已达 accept 标准（R3 确认）\n6. 核心瓶颈是科学层面：无 Llama-2 base 数据 + assertive claims 超出证据\n\n---\n\n## Reviewer Divergence [Round 2]\n\n| 分歧点 | 立场 | 分析 |\n|--------|------|------|\n| 整体评分 | R1: 5, R2: 5, R3: 7 | 由评审维度差异解释，非实质矛盾 |\n| 无方法创新是否致命 | R2: concern / R1+R3: 可接受 | 多数认为 insight novelty 可弥补 |\n| Neo et al. 影响程度 | R2: critical / R1: positioning issue only | R1 认为不影响 internal validity |\n\n---\n\n## Overall Assessment\n\n**Score: Weak Reject → Borderline (5/10)**\n**Confidence: High (4/5)**\n\n| Reviewer | Round 1 | Round 2 | 变化 |\n|----------|---------|---------|------|\n| R1 | 5/10 | 5/10 | 维持 |\n| R2 | 4/10 | 5/10 | +1 |\n| R3 | 6/10 | 7/10 | +1 |\n| **Consensus** | **4.5/10** | **5.3/10** | **+0.8** |\n\n**与 Round 1 的差异**：\n- 论文在 presentation readiness 上从 \"below standard\" 提升至 \"at standard\"\n- 科学问题的 transparency 提升（confound acknowledge、metric justification）\n- 但核心科学 gap（无对照数据、无因果验证）未通过新实验消除\n\n---\n\n## 具体可操作修改建议（按优先级）\n\n### P0（可能改变 acceptance decision）\n1. **Llama-2 base checkpoint 实验数据**（如能在 deadline 前完成）\n2. **Abstract L8 hedge**: \"should optimize\" → \"may benefit from optimizing\"; \"is the primary design lever\" → \"emerges as a candidate primary design lever in our analysis\"\n\n### P1（全票共识的必要修改）\n3. **Neo et al. 引用** + Introduction L10 限定为 \"systematic multi-metric decomposition of a VLA with factorial controls\"\n4. **Limitations 格式**: \\paragraph{Limitations.} → \\subsection{Limitations}\n5. **Title 限定**: 改为 \"...of a Vision-Language-Action Model\" (单数) 或加副标题 \"A Case Study of OpenVLA\"\n6. **Section 4.2 标题**: \"Training Establishes...\" → \"Trained VLA Exhibits...\"\n\n### P2（改善评分但非 blocking）\n7. §4.1 标题 \"instruction-blind\" → \"instruction-invariant under linear probing\"\n8. Table 3 same-layer comparison 调整为首行\n9. Table 1 caption \"(L0--L8 shown)\" → \"(selected layers shown)\"\n10. Conclusion 加 reproducibility statement\n11. Abstract \"LOOCV-verified\" → \"cross-validated\"\n\n---\n\n## 给 Research Director 的判断\n\n**当前状态**：论文处于 borderline (5/10)。写作已达标，科学方法论有一个不可通过文字修改完全解决的 gap（Llama-2 base 对照）。\n\n**升至 Accept (6/10) 的路径**：\n- **路径 A（最优）**：P0.1（Llama-2 base 数据）+ P0.2（Abstract hedge）+ P1 全部 → 预计 R1 升至 6，R2 升至 6，整体 6.3/10\n- **路径 B（纯文字修改）**：P0.2 + P1 全部 + P2 全部 → 预计 R2 升至 6，R1 仍为 5-5.5，整体 5.8/10（仍在 borderline）\n- **路径 C（最小修改）**：仅做 P0.2 + P1.3-4 → 预计变化不大\n\n**建议**：如果 Llama-2 base 实验能在 deadline (05-29) 前获得至少 attention analysis + cross-instruction probe 结果，论文有实质性机会突破 acceptance threshold。否则，纯文字修改只能将论文从 weak reject 推至 borderline，最终 decision 将取决于 AC 对 \"well-executed analysis paper with acknowledged confound\" 的容忍度。",
  "reviewer_ids_acknowledged": "[1, 2, 3]",
  "cross_response_reviewer_ids": "[1, 2, 3]",
  "overall_score": "borderline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "vla-ssd",
    "report": "# 圆桌审稿报告 — Round 2（修订评估）\n\n**论文**: \"Vision Encodes, Language Routes: A Representational Decomposition of Vision-Language-Action Models\"\n**Venue**: CoRL 2026 (Deadline: 2026-05-29)\n**Reviewers**: R1 (方法/实验), R2 (新颖性/意义), R3 (写作/格式)\n\n---\n\n## Summary\n\nRound 2 论文在写作和 framing 层面有实质改善：删除 \"first\" novelty claim、Related Work 从 3 段扩展至 5 段（+12 引用）、新增 \"Why RSA over CKA\" 方法论辩护、正文 em-dash 全部清除、Limitations 内容大幅扩展、confound 在实验章节显式 acknowledge。但核心科学问题（Llama-2 base 对照缺失、design implications 的因果 gap）未通过新实验数据解决，Abstract/Conclusion 的 assertive 语气与 Limitations 的 caveats 存在不一致。\n\n---\n\n## Round 1 → Round 2 变化总结\n\n### 已解决 (RESOLVED)\n| Issue | 状态 | 修改内容 |\n|-------|------|----------|\n| R1-W2 CKA/RSA 矛盾 | ✅ RESOLVED | Method 新增 \"Why RSA over CKA\" 段，全票认可 |\n| R3-N2 Em-dash AI 痕迹 | ✅ RESOLVED | 正文 prose 零残留解释性 em-dash |\n| R3-W4 Related Work 过短 | ✅ RESOLVED | 3→5 段，21→33 引用，覆盖 4 个新类别 |\n\n### 部分解决 (PARTIALLY_RESOLVED)\n| Issue | 状态 | 残留问题 |\n|-------|------|----------|\n| R1-N1 Baseline confound | ⚠️ | 充分 acknowledge，但无新数据；标题/Abstract 仍 causal |\n| R1-N4 Speculative implications | ⚠️ | Discussion caveat 良好，但 Abstract L8 仍为 \"should\"/\"primary lever\" 无 hedge |\n| R1-N2/R2-N4 单模型泛化性 | ⚠️ | Abstract 限定了 \"(OpenVLA-7B)\"，但 Title 仍复数 |\n| R2-N1 Novelty positioning | ⚠️ | \"First\" 删除，但 Neo et al. 仍未引用 |\n| R1-N3 RSA selection bias | ⚠️ | 叙事改善（\"where vs how high\"），Table 结构未调整 |\n| R2-W1 Related Work 覆盖 | ⚠️ | 33 引用达标，但仍缺 Neo et al. + Raghu et al. 2021 |\n| R3-N1 Limitations 格式 | ⚠️ | 内容充分，格式仍为 \\paragraph{}（需改 \\subsection） |\n\n### 未解决 (STILL_OPEN)\n| Issue | 状态 | 说明 |\n|-------|------|------|\n| R1-W1 \"Instruction-blind\" overclaim | ❌ | 无任何修改（标题、措辞、实验均未动） |\n| R3-W5 Code/data 声明 | ❌ | 未添加 |\n| R2-N2 无方法创新 | ❌ | 无新方法/验证实验（R1+R3 认为可通过 insight novelty 弥补）|\n\n---\n\n## Strengths（Round 2 新增/强化）\n\n1. **Confound 的透明度显著提升**：在实验章节正文（非仅 Limitations）即 acknowledge baseline 的局限性，让读者在遇到数据时就能正确理解 scope\n2. **\"Why RSA over CKA\" 方法论辩护**：不是 post-hoc cherry-picking，而是基于 metric 数学性质的 principled argument（scale-invariance for cross-dimensional comparison）\n3. **Related Work positioning 质量高**：Grant 2026 的三点显式差异化（token-level vs feature-level；32-layer profile；factorial control）是真正的 positioning 而非 survey\n4. **写作修订到位**：em-dash 清除、section 标题从 \"learns\" → \"establishes\"、contribution list 重定位\n\n---\n\n## Weaknesses（Round 2 残留）\n\n### Critical（影响接收决定）\n\n**W-Critical-1: Abstract/Conclusion 与 Limitations 的语气不一致**\n- Abstract L8: \"VLA architectures should optimize routing; vision encoder quality is the primary design lever\" — 未加任何 hedge\n- Conclusion L8: \"These results suggest that VLA architectures should optimize routing...\" — 有 \"suggest\" 但 \"should\" 仍在\n- Discussion Limitations: \"they do not address whether architectural interventions... would preserve action quality\"\n- **内部矛盾**：开头做强处方 → 结尾否认验证能力\n- **全票共识需修改**\n\n**W-Critical-2: 无 Llama-2 base 实验数据（核心 confound 未消除）**\n- 论文承认 \"currently conducting\" 但未在本版呈现数据\n- Finding 2 \"VLA training establishes deliberate instruction routing\" 的因果归因仍不完全成立\n- 如果 Llama-2 base 也展现 instruction-dominant attention → 核心叙事需根本重写\n- **R1 核心 concern，R2 AGREE**\n\n**W-Critical-3: Neo et al. (ICLR 2025) 未引用**\n- VLM token-level layer-wise 分析的直接先行工作（probing + attention + position ablation on LLaVA）\n- Introduction L10 \"No prior work has provided a systematic token-level decomposition\" 在 VLM 文献存在的情况下不完全成立\n- **R2 核心 concern，R1 同意应引用但认为不影响 internal validity**\n\n### Warning（影响评分）\n\n**W-Warning-1: Title 仍为复数 \"Vision-Language-Action Models\"**\n- 暗示一般性结论，与单模型证据不匹配\n- **全票共识**\n\n**W-Warning-2: \"Instruction-blind\" claim 完全未修改**\n- Section 4.1 段落标题仍为 \"Image tokens are instruction-blind\"\n- 无 MLP probe instruction classification 实验\n- 无措辞限定\n- **R1 标为 STILL_OPEN**\n\n**W-Warning-3: Limitations 格式仍为 \\paragraph{}**\n- CoRL 2026 CFP: \"include a Limitations section\"\n- 一行改动 (\\paragraph → \\subsection) 即可修复\n- **R3 标注**\n\n---\n\n## Reviewer Consensus [Round 2]\n\n所有 Reviewer 达成共识：\n1. Abstract L8 必须加 hedge（\"suggest\"/\"may benefit from\"/\"emerges as a candidate\"）\n2. Neo et al. 应被引用并 differentiate\n3. CKA/RSA 问题已 RESOLVED\n4. 修订展示了作者的诚实态度和对问题的理解\n5. 论文在写作/呈现维度已达 accept 标准（R3 确认）\n6. 核心瓶颈是科学层面：无 Llama-2 base 数据 + assertive claims 超出证据\n\n---\n\n## Reviewer Divergence [Round 2]\n\n| 分歧点 | 立场 | 分析 |\n|--------|------|------|\n| 整体评分 | R1: 5, R2: 5, R3: 7 | 由评审维度差异解释，非实质矛盾 |\n| 无方法创新是否致命 | R2: concern / R1+R3: 可接受 | 多数认为 insight novelty 可弥补 |\n| Neo et al. 影响程度 | R2: critical / R1: positioning issue only | R1 认为不影响 internal validity |\n\n---\n\n## Overall Assessment\n\n**Score: Weak Reject → Borderline (5/10)**\n**Confidence: High (4/5)**\n\n| Reviewer | Round 1 | Round 2 | 变化 |\n|----------|---------|---------|------|\n| R1 | 5/10 | 5/10 | 维持 |\n| R2 | 4/10 | 5/10 | +1 |\n| R3 | 6/10 | 7/10 | +1 |\n| **Consensus** | **4.5/10** | **5.3/10** | **+0.8** |\n\n**与 Round 1 的差异**：\n- 论文在 presentation readiness 上从 \"below standard\" 提升至 \"at standard\"\n- 科学问题的 transparency 提升（confound acknowledge、metric justification）\n- 但核心科学 gap（无对照数据、无因果验证）未通过新实验消除\n\n---\n\n## 具体可操作修改建议（按优先级）\n\n### P0（可能改变 acceptance decision）\n1. **Llama-2 base checkpoint 实验数据**（如能在 deadline 前完成）\n2. **Abstract L8 hedge**: \"should optimize\" → \"may benefit from optimizing\"; \"is the primary design lever\" → \"emerges as a candidate primary design lever in our analysis\"\n\n### P1（全票共识的必要修改）\n3. **Neo et al. 引用** + Introduction L10 限定为 \"systematic multi-metric decomposition of a VLA with factorial controls\"\n4. **Limitations 格式**: \\paragraph{Limitations.} → \\subsection{Limitations}\n5. **Title 限定**: 改为 \"...of a Vision-Language-Action Model\" (单数) 或加副标题 \"A Case Study of OpenVLA\"\n6. **Section 4.2 标题**: \"Training Establishes...\" → \"Trained VLA Exhibits...\"\n\n### P2（改善评分但非 blocking）\n7. §4.1 标题 \"instruction-blind\" → \"instruction-invariant under linear probing\"\n8. Table 3 same-layer comparison 调整为首行\n9. Table 1 caption \"(L0--L8 shown)\" → \"(selected layers shown)\"\n10. Conclusion 加 reproducibility statement\n11. Abstract \"LOOCV-verified\" → \"cross-validated\"\n\n---\n\n## 给 Research Director 的判断\n\n**当前状态**：论文处于 borderline (5/10)。写作已达标，科学方法论有一个不可通过文字修改完全解决的 gap（Llama-2 base 对照）。\n\n**升至 Accept (6/10) 的路径**：\n- **路径 A（最优）**：P0.1（Llama-2 base 数据）+ P0.2（Abstract hedge）+ P1 全部 → 预计 R1 升至 6，R2 升至 6，整体 6.3/10\n- **路径 B（纯文字修改）**：P0.2 + P1 全部 + P2 全部 → 预计 R2 升至 6，R1 仍为 5-5.5，整体 5.8/10（仍在 borderline）\n- **路径 C（最小修改）**：仅做 P0.2 + P1.3-4 → 预计变化不大\n\n**建议**：如果 Llama-2 base 实验能在 deadline (05-29) 前获得至少 attention analysis + cross-instruction probe 结果，论文有实质性机会突破 acceptance threshold。否则，纯文字修改只能将论文从 weak reject 推至 borderline，最终 decision 将取决于 AC 对 \"well-executed analysis paper with acknowledged confound\" 的容忍度。",
    "reviewer_ids_acknowledged": "[1, 2, 3]",
    "cross_response_reviewer_ids": "[1, 2, 3]",
    "overall_score": "borderline"
  }
}
```

</details>

---


### Tool result

_source line 165 · 2026-05-17T06:11:35.856122+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a1d032cbe70bdd2058438e67e0d57613:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4021
}
```

</details>

---


### Assistant

_source line 166 · 2026-05-17T06:11:44.896559+00:00_

**Round 2 审稿完成。**

报告已投递至 Research Director。核心结论：

- **评分**：从 Round 1 的 4.5/10 (Weak Reject) 提升至 5.3/10 (Borderline)
- **已解决**：CKA/RSA 矛盾、em-dash、Related Work 密度
- **核心瓶颈**：Llama-2 base 对照实验缺失 + Abstract 语气过强
- **升至 Accept 的关键路径**：Llama-2 base 数据（P0 优先）+ Abstract hedge + Neo et al. 引用 + 格式微调

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 22

## Round 22

2 recorded events


### User

_source line 167 · 2026-05-17T06:11:47.471692+00:00_

[Reviewer 3 审稿结果]:


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_3"
}
```

</details>

---


### Assistant

_source line 168 · 2026-05-17T06:11:52.631609+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 23

## Round 23

68 recorded events


### User

_source line 169 · 2026-05-17T17:58:14.180493+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: vla-ssd
- 论文路径: projects/vla-ssd/docs/paper/main.tex
- 目标 venue: CoRL 2026
- 截止日期: 2026-05-29

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 170 · 2026-05-17T17:58:20.652390+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 171 · 2026-05-17T17:58:20.703252+00:00_

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
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 172 · 2026-05-17T17:58:26.124372+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_local_file",
  "max_results": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_local_file",
    "max_results": "8"
  }
}
```

</details>

---


### Tool result

_source line 173 · 2026-05-17T17:58:26.124816+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 174 · 2026-05-17T17:58:26.426181+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
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

_source line 175 · 2026-05-17T17:58:26.577859+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 176 · 2026-05-17T17:58:34.409220+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 177 · 2026-05-17T17:58:34.911592+00:00_

{"result":"# 项目 vla-ssd 概况\n\n## 实验状态 (67 个)\n\n- **lg_extract_untrained_r2**: DONE (killed) — \n- **lg_extract_trained_r2**: DONE (killed) — \n- **lg_extract_untrained_r1**: DONE (killed) — \n- **lg_extract_trained_r1**: DONE (killed) — \n- **mvp2_delta_dino**: DONE (success) — \n- **mvp2_delta_untrained**: DONE (success) — \n- **mvp2_delta_trained**: DONE (success) — \n- **mvp2_action_dino**: DONE (success) — \n- **mvp2_action_untrained**: DONE (success) — \n- **mvp2_action_trained**: DONE (success) — \n- **mvp_controlb_untrained**: DONE (success) — \n- **mvp_controlb_trained**: DONE (success) — \n- **mvp_001**: DONE (negative) — \n- **mvp_probe_untrained**: DONE (success) — \n- **mvp_probe_trained**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- ablation_p2_demo_sensitivity: Demo count sensitivity: subsample 25 from 50 demos/task, rerun RSA + probe on trained_image_mean (33 layers). Tests whether inverted-U pattern is stable under reduced data.（准备中）\n- fulllayer_action_probe（准备中）\n\n## 近期结论\n- **l1_head_ablation** (success): L1 instruction-dominant heads (24/32 with >50% text attention) are causally necessary for instruction routing: ablating their instruction attention should collapse downstream instruction classification accuracy from ~100% to near-chance, while ablating non-dominant heads (control) should have minimal effect. This upgrades C2 (front-loaded routing) from correlational to partially causal.\n- **cross_inst_spatial_trained** (success): LIBERO-Spatial cross-instruction probe: trained VLA should show same token specialization as LIBERO-Goal (last_preaction=100% classification at all layers, image_mean=10% chance). Cross-benchmark replication strengthens C1 claim that readout token is instruction-conditioned while image tokens are instruction-blind.\n- **plan010_rsa_spatial** (success): LIBERO-Spatial RSA cross-benchmark validation: trained VLA should show inverted-U RSA profi
…[truncated 596 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 178 · 2026-05-17T17:58:34.912003+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "literature_map.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "literature_map.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 179 · 2026-05-17T17:58:35.816055+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/literature_map.yaml\", \"content\": \"papers:\\n  # ============================================================\\n  # DIRECT COMPETITORS — VLA Representation Analysis / Interpretability\\n  # ============================================================\\n  - id: grant2026\\n    title: \\\"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models\\\"\\n    authors: \\\"Bryce Grant, Xijia Zhao, Peng Wang\\\"\\n    year: 2026\\n    venue: \\\"arXiv preprint (under review)\\\"\\n    arxiv_id: \\\"2603.19233\\\"\\n    category: direct-competitor\\n    role: competitor\\n    key_findings: >\\n      Visual pathway dominates action generation across all 6 tested VLA architectures (80M–7B params, 394K+ rollout episodes, 4 benchmarks).\\n      Language sensitivity depends on task structure: when visual context uniquely specifies the task, language is IGNORED;\\n      when multiple goals share a scene, language becomes essential (\\\"encoded but not used\\\").\\n      Cross-task activation injection steers robots toward source-task positions (99.8% trajectory alignment with source in X-VLA).\\n      Multi-pathway architectures (pi0.5, SmolVLA, GR00T) separate motor programs (expert pathway) from goal semantics (VLM pathway).\\n    relevance_to_us: >\\n      Most direct competitor. Behavioral intervention (activation injection, SAE, probing) reveals vision dominance + language encoded but not used.\\n      Uses OpenVLA-OFT checkpoint; we use standard fine-tuning — must qualify this difference in Related Work.\\n    novelty_gap: >\\n      No trained vs untrained representation analysis. They compare different model architectures,\\n      we compare trained vs untrained representation structure within the same architecture.\\n      Their \\\"encoded but not used\\\" is a behavioral-level conclusion; we demonstrate at the represent
…[truncated 3580 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 180 · 2026-05-17T17:58:35.816556+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 call for papers submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 181 · 2026-05-17T17:58:36.067855+00:00_

called mcp__agent-ml-research__read_local_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_local_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_local_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 182 · 2026-05-17T17:58:36.068301+00:00_

&lt;tool_use_error>Error: No such tool available: mcp__agent-ml-research__read_local_file&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_local_file",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 183 · 2026-05-17T17:58:43.151944+00:00_

Web search results for query: "CoRL 2026 call for papers submission guidelines author instructions"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 - Instruction for Presentations","url":"https://www.corl.org/contributions/instruction-for-presentations"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"ICML 2026 Author Instructions","url":"https://icml.cc/Conferences/2026/AuthorInstructions"}]

Based on the search results, here are the key submission guidelines and author instructions for CoRL 2026:

## Paper Format

The camera-ready paper should follow the template: 8-page main text + acknowledgment + references + appendix (optional).

## Reciprocal Review Requirement

Every author with 3 or more submissions must agree to serve as a reviewer. Authors are exempt from the review requirement if they serve as an AC, an SAC, or another organizing chair for CoRL 2026. Submissions that do not meet this reciprocal review requirement may be desk-rejected.

## Required Content

All submissions should include a Limitations section (counted toward the 8-page limit), explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments, and how these might be addre
…[truncated 804 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "WebSearch",
  "elapsed_ms": 7335
}
```

</details>

---


### Tool call

_source line 184 · 2026-05-17T17:58:48.700606+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,WebFetch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file,WebFetch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 185 · 2026-05-17T17:58:48.751296+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-17T17:58:53.620792+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl.org/contributions/instruction-for-authors",
  "prompt": "Extract ALL submission requirements: page limit, template (LaTeX class/style), anonymity rules (double-blind?), deadline dates, supplementary material rules, appendix rules, reference format, any checklist requirements. Be exhaustive."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl.org/contributions/instruction-for-authors",
    "prompt": "Extract ALL submission requirements: page limit, template (LaTeX class/style), anonymity rules (double-blind?), deadline dates, supplementary material rules, appendix rules, reference format, any checklist requirements. Be exhaustive."
  }
}
```

</details>

---


### Tool call

_source line 187 · 2026-05-17T17:58:53.872205+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool call

_source line 188 · 2026-05-17T17:58:55.428709+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 189 · 2026-05-17T17:58:59.193166+00:00_

# CoRL 2026 Submission Requirements

## Page Limits
- **Initial submission:** 8 pages main text
- **Camera-ready:** 9 pages main text
- Acknowledgments, references, and appendix do **not** count toward page limits

## Template & Formatting
- **LaTeX template required:** Available via Google Drive link
- Camera-ready uses `\usepackage[final]{corl_2026}`
- Footer requirement: "10th Conference on Robot Learning (CoRL 2026), Austin, Texas, USA."
- Match template's text density, fonts, spacing, and margins

## Anonymity
- **Double-blind review:** "all papers must be anonymized"
- Camera-ready version includes author names (de-anonymized)

## Deadlines
- Abstract submission deadline (firm, no exceptions)
- Paper submission: Thursday 5/28 EOD
- Camera-ready: October 12, 2026 (23:59 AOE)
- Rebuttal deadline (specific date not listed)

## Supplementary Materials
- Submitted as **single zip file** via OpenReview
- Video: maximum 250 MB, ≤3 minutes suggested
- Appendix may be included with main paper or supplement
- **Camera-ready note:** Videos cannot be PMLR supplementary material; host externally (YouTube, GitHub, etc.) with links in main text

## Required Sections
- **Limitations section:** Mandatory, counts toward 8-page limit for initial submission

## Additional Requirements
- Disclose generative AI usage
- Reciprocal reviewing obligation for qualified authors
- No fake citations permitted

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "WebFetch",
  "elapsed_ms": 5572
}
```

</details>

---


### Tool result

_source line 190 · 2026-05-17T17:58:59.243918+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'vla-ssd'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5371
}
```

</details>

---


### Tool result

_source line 191 · 2026-05-17T17:58:59.244297+00:00_

1	\documentclass{article}
2	
3	\usepackage{corl_2026}
4	
5	\usepackage[utf8]{inputenc}
6	\usepackage[T1]{fontenc}
7	\usepackage{url}
8	\usepackage{booktabs}
9	\usepackage{amsfonts}
10	\usepackage{amsmath}
11	\usepackage{nicefrac}
12	\usepackage[expansion=false]{microtype}
13	\usepackage{graphicx}
14	\usepackage{enumitem}
15	
16	\title{Vision Encodes, Language Routes:\\ Token-Level Functional Specialization in a Vision-Language-Action Model}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	
22	\maketitle
23	
24	\begin{abstract}
25	\input{abstract}
26	\end{abstract}
27	
28	\input{introduction}
29	\input{related_work}
30	\input{method}
31	\input{experiments}
32	\input{discussion}
33	
34	\bibliography{references}
35	
36	\input{appendix}
37	
38	\end{document}
39	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 3815
}
```

</details>

---


### Tool call

_source line 192 · 2026-05-17T17:59:05.328126+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 193 · 2026-05-17T17:59:05.831008+00:00_

1	Vision-language-action models (VLAs) fine-tune large language models (LLMs) on robot demonstrations, but how they internally process multimodal information at the token level remains unknown.
2	We perform a systematic token-level representational decomposition of a VLA (OpenVLA-7B on LIBERO) with factorial trained-vs-untrained control, combining cross-instruction probes, attention analysis, Representational Similarity Analysis (RSA), and functional probes across all 32 LLM layers.
3	Three findings emerge.
4	First, the VLA exhibits strict token-level functional specialization: image tokens are instruction-blind (instruction classification at chance, $10\%$, across all layers), while the readout token serves as a multimodal convergence point ($100\%$ instruction classification from L1, cross-validated).
5	Second, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth (L9--L16, 15--22 heads), while VLA training shifts this to entry-layer routing (L0--L1: 21--25 heads) with exit-layer re-engagement (L31: 18 heads), enabling immediate instruction access ($99.6\%$ at L1 vs.\ pretrained $80.2\%$); untrained instruction attention remains below $12\%$ at every layer.
6	Third, the LLM applies a non-monotonic refinement of vision encoder geometry: RSA peaks at L12, probe $R^2$ peaks at L8--L13, with self-supervised DINOv2 providing the highest geometric foundation ($\rho = 0.692$, exceeding all internal representations).
7	These results reveal that VLAs maintain a strict division of labor between visual and multimodal tokens, with training primarily reshaping readout-token information integration (probe accuracy $+18$pp at L31, instruction attention $+46$pp at L1) rather than visual representations ($\Delta\rho \leq 0.017$).
8	These findings suggest that routing efficiency to the readout position may be a key design consideration; vision encoder quality emerges as a key lever for action-relevant representation qu
…[truncated 9 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 194 · 2026-05-17T17:59:06.082390+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 195 · 2026-05-17T17:59:06.133139+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Vision-language-action models (VLAs) process visual observations and language instructions through a large language model to produce robot actions~\cite{brohan2023_rt2,kim2024_openvla}.
5	A central but untested assumption is that all token types within the LLM contribute uniformly to action prediction.
6	Understanding the token-level division of labor is essential for characterizing how VLAs process multimodal information: if image tokens and readout tokens serve fundamentally different roles, design choices (attention patterns, layer selection, action head placement) should reflect this specialization.
7	
8	Recent behavioral studies reveal that VLAs rely disproportionately on visual input~\cite{grant2026}, with language instructions largely ignored by the action pathway~\cite{haon2025}.
9	These findings hint at internal specialization but do not explain \emph{how} information is routed within the LLM, \emph{where} instruction identity is encoded, or \emph{what} training changes at the representational level.
10	Existing analyses have not yet combined systematic multi-metric probing with factorial trained/untrained controls in VLAs, leaving open whether image tokens carry instruction information, whether the readout token functions as a multimodal hub, and whether training creates new representational structure or reconfigures inherited geometry.
11	
12	We address this gap by decomposing OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a VLA chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2}, an MLP projector, and Llama-2 7B.
13	We extract representations from each of 32 LLM layers at both image-token and readout-token positions, and from external baselines (DINOv2~\cite{oquab2024_dinov2}, CLIP~\cite{radford2021_clip}).
14	We compare three LLM conditions (VLA-trained, pretrained Llama-2 base, and randomly initialized) crossed with instruction presence, and apply four compleme
…[truncated 2409 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 196 · 2026-05-17T17:59:07.187650+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 197 · 2026-05-17T17:59:07.188135+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Vision-language-action models.}
4	VLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}.
5	This architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.
6	A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.
7	We test this assumption at the representational level through per-layer, per-token-type decomposition.
8	
9	\paragraph{Mechanistic interpretability in transformers.}
10	A growing body of work analyzes transformer internals at the level of individual attention heads and circuits.
11	Elhage et al.~\cite{elhage2021} introduced the residual stream framework, in which each layer reads from and writes to a shared communication channel.
12	Building on this, Olsson et al.~\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning; these specialized attention heads implement token-copying algorithms.
13	Circuit-level analyses have since traced complete computational subgraphs for tasks such as indirect object identification~\cite{wang2023_ioi} and greater-than comparison~\cite{conmy2023}.
14	In parallel, attention probing studies have shown that individual heads encode syntactic relations~\cite{clark2019}, capture positional and structural patterns at different depths~\cite{vig2019}, and that a small subset of specialized heads accounts for most model performance~\cite{voita2019}.
15	Our Layer-1 attention head analysis extends this tradition to the VLA domain, where we find that 25 of 32 heads become instruction-dominant after fine-tuning.
16	
17	\paragraph{Behavioral and mechanistic analysis of VLAs.}
18	Behavioral evaluations reveal that current VLAs rel
…[truncated 2687 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 198 · 2026-05-17T17:59:07.701142+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 199 · 2026-05-17T17:59:07.902719+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We investigate how action-relevant structure is distributed across a VLA by combining four complementary analyses: cross-instruction probes, attention pattern analysis, RSA, and functional probes.
5	
6	%------------------------------------------------------------------
7	\subsection{Model and Data}
8	\label{sec:model_data}
9	
10	We study OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a generalist robot policy chaining three components: a frozen DinoSigLIP fused vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), a Multi-Layer Perceptron (MLP) projector (2{,}176-D $\to$ 4{,}096-D), and a Llama-2 7B language backbone (6.74B parameters) that autoregressively decodes 7-dimensional actions.
11	We use the base checkpoint pretrained on Open X-Embodiment (no task-specific fine-tuning) and evaluate on LIBERO-Goal~\cite{liu2023_libero} (10 tabletop tasks, 50 demonstrations each).
12	To disentangle the contributions of language pretraining and VLA fine-tuning, we compare three LLM conditions: (1)~VLA-trained (the released checkpoint), (2)~Llama-2 base (the pretrained LLM backbone without VLA fine-tuning), and (3)~untrained (all 6.74B LLM parameters reinitialized via \texttt{from\_config()}).
13	All three conditions share the same frozen vision encoder and projector architecture.
14	
15	%------------------------------------------------------------------
16	\subsection{Representation Extraction}
17	\label{sec:repr_extraction}
18	
19	We extract representations from six sources spanning the VLA pipeline:
20	(a)~\textbf{DinoSigLIP+Projector}, the projector output (4{,}096-D), immediately before LLM processing;
21	(b)~\textbf{LLM image\_mean}, the mean image-token activation at each of 32 layers;
22	(c)~\textbf{LLM readout}, the activation at the final pre-action token position at each layer;
23	(d)~\textbf{DINOv2 ViT-L/14}~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}), a self
…[truncated 4027 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 200 · 2026-05-17T17:59:11.567505+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 201 · 2026-05-17T17:59:11.969704+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We evaluate OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024} on LIBERO-Goal~\cite{liu2023_libero} (10 tasks, 50 demonstrations each).
8	Representations are extracted from six sources spanning the VLA pipeline (\S\ref{sec:repr_extraction}): DinoSigLIP+Projector, LLM image\_mean and readout tokens at each of 32 layers, DINOv2~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}), CLIP~\cite{radford2021_clip} (\texttt{patch\_mean}), and branch-split (DINOv2 1{,}024-D / SigLIP 1{,}152-D before fusion).
9	Three LLM conditions are compared: VLA-trained, pretrained Llama-2 base (no VLA fine-tuning), and untrained (6.74B parameters reinitialized to random weights), crossed with instruction presence (\S\ref{sec:model_data}).
10	RSA computes Spearman $\rho$ between cosine-distance representation RDMs and Euclidean-distance action RDMs, with 10{,}000 bootstrap CIs (\S\ref{sec:rsa}).
11	MLP probes (input $\to$ 256 $\to$ 7; Adam, lr${}=10^{-3}$, 50 epochs, early stopping) report mean $R^2$ (\S\ref{sec:probes}).
12	
13	%------------------------------------------------------------------
14	\subsection{Token-Level Functional Specialization}
15	\label{sec:token_specialization}
16	
17	We test whether image tokens and readout tokens encode different types of information by training cross-instruction probes (\S\ref{sec:cross_instruction_probes}): given the same visual frame paired with each of 10 task instructions, we classify which instruction was present from per-layer activations.
18	
19	\paragraph{Image tokens are instruction-blind.}
20	At the image\_mean position, instruction classification remains at chance ($10\%$) across all 32 layers, in both trained and untrained models (Table~\ref{tab:dense_routing_main}).
21	Both linear and MLP probes confirm chance-level performance ($10\%$), as does standalone DINOv2 \texttt{cls\_token} ($10\%$), ruling out probe ca
…[truncated 10294 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 202 · 2026-05-17T17:59:11.970161+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 203 · 2026-05-17T17:59:12.522481+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Synthesis.}
5	Our experiments reveal strict functional specialization: image tokens remain instruction-blind across all 32 layers, while the readout token serves as the sole multimodal convergence point.
6	VLA fine-tuning shifts instruction routing from mid-depth (L9--L16) to an entry-exit pattern (L0--L1, L31), with training effects concentrated at the readout token ($R^2$ $+0.069$) rather than image representations ($\Delta \leq 1.7\%$).
7	
8	\paragraph{Mechanism-behavior connection.}
9	The instruction-blindness of image tokens provides a mechanistic explanation for the visual dominance reported by Grant et al.~\cite{grant2026}: with no instruction-specific information in image representations ($|\Delta| < 0.006$), the action pathway relies on the readout token for task conditioning.
10	This clarifies a dissociation between geometric and functional alignment: DINOv2 achieves the highest RSA ($\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\ $0.634$), indicating that the LLM routes and integrates instruction-conditioned information rather than enhancing visual geometry.
11	
12	\paragraph{Architectural implications.}
13	First, vision encoder quality may matter more than LLM scale: the external encoder ceiling ($\rho = 0.692$) exceeds all internal representations, and training yields only modest geometric gains ($\Delta = 0.017$, $3\%$).
14	Second, attention ablation at L1 confirms functional specialization: removing instruction attention does not disrupt classification (maintained via the residual stream) but redistributes attention to image tokens, recovering action encoding ($R^2$ $+46\%$, $p < 0.0001$), with deep layers unaffected ($|\Delta R^2| < 0.01$).
15	This dissociation confirms genuine functional specialization of attention heads, while cautioning against interpreting attention as a causal bottleneck.
16	
17	\paragraph{Limitations.}
18	We study OpenVLA-7B on LIB
…[truncated 475 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 204 · 2026-05-17T17:59:12.573268+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 205 · 2026-05-17T17:59:12.624441+00:00_

1	\appendix
2	
3	\section{Supplementary Material}
4	\label{sec:appendix}
5	
6	\subsection{CKA Analysis Method}
7	\label{sec:cka_appendix}
8	
9	We employ Centered Kernel Alignment (CKA)~\cite{kornblith2019} alongside RSA as a complementary perspective.
10	While RSA captures local geometric alignment via rank-order preservation, CKA measures global representational similarity through kernel-based comparisons.
11	
12	We compute both \emph{linear CKA}, which uses a linear kernel and is sensitive to second-order statistics, and \emph{RDM kernel CKA}, which operates on the same distance matrices as RSA but aggregates them differently.
13	Using both variants tests whether conclusions about representation structure are robust to the choice of similarity metric.
14	
15	Linear CKA between high-dimensional representations (4{,}096-D for LLM layers) and the 7-D action space is subject to a known dimension mismatch: the linear kernel in the low-dimensional space may not capture the same structure as in the high-dimensional space.
16	RDM kernel CKA avoids this issue by operating on distance matrices of equal size regardless of the original feature dimensionality.
17	
18	\subsection{Metric Sensitivity: RSA versus CKA}
19	\label{sec:metric_sensitivity_appendix}
20	
21	Linear CKA~\cite{kornblith2019} reverses the RSA ordering: untrained LLM ($\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially inverting the self-supervised advantage (Figure~\ref{fig:metric_comparison}).
22	RDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $\approx$ Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).
23	This divergence reflects the known sensitivity of representation similarity metrics to different geometric properties.
24	
25	At the per-layer level, linear CKA between image\_mean and the action space rises monotonically from L0 ($0.081$) to L32 ($0.098$), showing no inverted-U pattern.
26	RSA captures ran
…[truncated 21943 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 206 · 2026-05-17T17:59:33.856114+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "offset": "416"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "offset": "416"
  }
}
```

</details>

---


### Tool result

_source line 207 · 2026-05-17T17:59:34.810111+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (416). The file has 416 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 208 · 2026-05-17T17:59:34.860761+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 209 · 2026-05-17T17:59:35.262777+00:00_

1	% === VLA / Architecture ===
2	
3	@article{kim2024_openvla,
4	  title     = {{OpenVLA}: An Open-Source Vision-Language-Action Model},
5	  author    = {Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balakrishna, Ashwin and Nair, Suraj and Rafailov, Rafael and Foster, Ethan and Lam, Grace and Sanketi, Pannag and Lu, Quan and Kollar, Thomas and Burchfiel, Benjamin and Tedrake, Russ and Sadigh, Dorsa and Levine, Sergey and Liang, Percy and Finn, Chelsea},
6	  journal   = {arXiv preprint arXiv:2406.09246},
7	  year      = {2024},
8	}
9	
10	@article{karamcheti2024,
11	  title     = {Prismatic {VLMs}: Investigating the Design Space of Visually-Conditioned Language Models},
12	  author    = {Karamcheti, Siddharth and Nair, Suraj and Balakrishna, Ashwin and Liang, Percy and Kollar, Thomas and Sadigh, Dorsa},
13	  journal   = {arXiv preprint arXiv:2402.07865},
14	  year      = {2024},
15	}
16	
17	@article{brohan2023_rt2,
18	  title     = {{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
19	  author    = {Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},
20	  journal   = {arXiv preprint arXiv:2307.15818},
21	  year      = {2023},
22	}
23	
24	% === Benchmark ===
25	
26	@inproceedings{liu2023_libero,
27	  title     = {{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
28	  author    = {Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},
29	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
30	  year      = {2023},
31	}
32	
33	% === Representation Analysis Methods ===
34	
35	@article{kriegeskorte2008,
36	  title     = {Representational Similarity Analysis -- Connecting the Branches of Systems Neuroscience},
37	  author    = {Kriegeskorte, Nikolaus and Mur, Marieke and Ban
…[truncated 13237 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 210 · 2026-05-17T17:59:35.614473+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 211 · 2026-05-17T17:59:35.765666+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/decisions.yaml\", \"content\": \"_next_id: 60\\ndecisions:\\n- id: D001\\n  date: 2026-05-15 11:03 UTC\\n  summary: MVP 三分支判定标准校准：ρ下限0.3→0.5, Δρ加bootstrap CI, subtask gate加DINO baseline对比\\n  rationale: Reviewer 审查发现四项校准缺陷：(1) ρ>0.3 下限过低（DINO-V2 已达0.833，0.3只挡彻底失败）→ 提至0.5；(2)\\n    Δρ>0.1 仅为点估计缺统计检验 → 追加 bootstrapped 95% CI must exclude 0；(3) subtask_AUC>0.7\\n    无 baseline 锚点（不知道 DINO-V2 能做到多少）→ 增加条件 subtask_AUC > DINO_subtask_AUC + 0.05；(4)\\n    layer profile 不入正式判定但作为 mandatory supplementary analysis。修改后标准更严谨，降低 false positive\\n    PASS 风险。\\n  related_experiments:\\n  - exp_id: dino-v2-baseline\\n    role: baseline\\n    result: ρ=0.833\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-15 12:02 UTC\\n  summary: MVP 判定全面切换到 per-task mean ρ，弃用 pooled ρ\\n  rationale: Reviewer 指出 pooled ρ 受 cross-task variance 膨胀（DINO pooled=0.833 vs per-task\\n    mean=0.554）。pooled-vs-pooled 虽对称但偏严（可能 false negative）。切换 per-task mean 与 task-level\\n    bootstrap CI 方法论一致，且是更公平的 apples-to-apples 比较。影响：VLA≥DINO gate 从 ρ≥0.833 变为 per-task\\n    mean≥0.554；ρ>0.5 下限同样改为 per-task mean。\\n  related_experiments:\\n  - exp_id: dinov2_baseline\\n    role: baseline\\n    result: pooled ρ=0.833, per-task mean=0.554\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-15 12:31 UTC\\n  summary: 移除 subtask AUC gate，MVP 判定简化为纯 temporal distance (ρ) 路径\\n  rationale: DINO-V2 subtask AUC = 0.9717，Path B 要求 VLA > DINO + 0.05 = 1.0217，数学不可达（AUC\\n    上限 1.0）。根因：subtask 间视觉差异大，任何强视觉编码器都能高 AUC 区分——subtask discrimination 不是 VLA 的差异化能力。Temporal\\n    distance（连续进度信号）才是 VLA 可能独有的编码维度。简化后判定：PASS 需 VLA_ρ ≥ DINO_ρ (0.833)；CONDITIONAL\\n    需 Δρ > 0.1 但 VLA_ρ < DINO_ρ；FAIL 需 ρ ≤ 0.5 或 Δρ ≤ 0.1。Subtask AUC 保留为补充分析，不参与\\n    gate。\\n  related_experiments:\\n  - exp_id: dinov2_baseline\\n    role: trigger\\n    result: subtask AUC 0.9717 使 Path B 数学不可达\\n  depends_on:\\n  - D001\\n- id:
…[truncated 1435 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 212 · 2026-05-17T17:59:42.145232+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "paper_framing.md",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "paper_framing.md",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 213 · 2026-05-17T17:59:43.553359+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_framing.md\", \"content\": \"# Paper Framing — vla-ssd (Plan B: Functional Specialization)\\n\\n> D048: PI 批准按最大质量重构。A+ 版本保留为 fallback (branch paper-a-plus-backup)。\\n\\n## Target Venue\\n- Primary: CoRL 2026\\n- Deadline: Abstract May 26, Paper May 29\\n- Format: 8 pages + references\\n\\n## Core Insight\\n\\nVLA 内部存在 token-level 功能分离：image tokens 始终是纯视觉表征（instruction-blind at ALL layers），readout/action token 是多模态 instruction-conditioned planning 的汇聚点。训练学习了 deliberate instruction routing（25/32 heads 翻转为 instruction-dominant），创建了 robust multimodal signal 并维护其在深层不衰减。\\n\\n## Core Claims (3 条，重构后)\\n\\n### C1: Token-Level Functional Specialization\\nVLA 中 image tokens 和 readout token 有完全不同的功能：\\n- **Image tokens**: instruction-blind at ALL layers (cross-instruction classification = 10% = chance, both trained/untrained)\\n- **Readout token**: instruction-conditioned multimodal convergence (100% classification from L8, LOOCV 100%±0.00 across 10 folds)\\n- **DINOv2 baseline**: 10% (structurally cannot access instruction)\\n- **Implication**: LLM 不把 instruction 信息注入视觉表征——信息路由是 position-specific 的\\n\\nKey evidence:\\n- Cross-instruction probe: same frame × 10 instructions → 10-way classification\\n- Dense L0-L8: L0=10% → L1=100% (step function)\\n- LOOCV: 100%±0.00 all folds, all layers L8-L31 (trained)\\n- image_mean at ALL layers = chance (10%)\\n\\n### C2: Three Qualitatively Different Routing Strategies — VLA Fine-tuning Achieves Immediate Dedicated Routing\\n三条件揭示三种定性不同的 routing 模式：\\n\\n**L1 Attention Routing (heads + attention fraction):**\\n- **Untrained (random init)**: 0/32 heads, 12% text attention\\n- **Llama-2 base (pretrained, no VLA)**: 9/32 heads, 36.5% text attention\\n- **VLA Trained**: 25/32 heads, 58% text attention\\n\\n**Full-Layer Probe Profile (instruction classification accuracy):**\\n- **Trained**: L1=99.6% → 全程 100% — \\\
…[truncated 3485 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1408
}
```

</details>

---


### Tool call

_source line 214 · 2026-05-17T17:59:43.553911+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 215 · 2026-05-17T17:59:43.654601+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 216 · 2026-05-17T17:59:43.655149+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 217 · 2026-05-17T17:59:43.705645+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 218 · 2026-05-17T17:59:45.724892+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 219 · 2026-05-17T17:59:45.775691+00:00_

1	issues:
2	  - id: R1-N1
3	    summary: "Untrained baseline (random weights) 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献"
4	    category: experiment
5	    severity: critical
6	    status: resolved
7	    first_raised_round: 1
8	    last_seen_round: 2
9	    mentions:
10	      - round: 1
11	        reviewers: [1, 2, 3]
12	        note: "全票共识。需增加 Llama-2 base checkpoint 作为中间对照"
13	      - round: 2
14	        reviewers: [1, 2, 3]
15	        note: "PARTIALLY_RESOLVED: acknowledge confound 但无数据"
16	    action_items:
17	      - round: 1
18	        action: "增加 Llama-2 base checkpoint 对照实验"
19	        assigned_to: research
20	        status: done
21	      - round: 2
22	        action: "Section 标题改为观察性；Abstract 弱化 causal attribution"
23	        assigned_to: paper_agent
24	        status: done
25	    resolution: "B版本完整整合三条件数据：untrained 0/32, Llama-2 base 9/32, trained 25/32 heads。§4.3 以三条件梯度为核心证据，Table 2 + Figure 4 呈现完整 32 层 profile。"
26	    resolution_round: 3
27	
28	  - id: R1-N2
29	    summary: "单一模型(OpenVLA-7B) + 单一 benchmark family(LIBERO)，Title/Abstract 使用复数 'VLAs' 构成 overclaim"
30	    category: framing
31	    severity: critical
32	    status: resolved
33	    first_raised_round: 1
34	    last_seen_round: 2
35	    mentions:
36	      - round: 1
37	        reviewers: [1, 2, 3]
38	        note: "全票共识"
39	      - round: 2
40	        reviewers: [1, 2, 3]
41	        note: "PARTIALLY_RESOLVED: Abstract 限定但 Title 仍复数"
42	    action_items:
43	      - round: 2
44	        action: "Title 改为单数"
45	        assigned_to: paper_agent
46	        status: done
47	    resolution: "B版本 Title = 'Token-Level Functional Specialization in a Vision-Language-Action Model'（单数）。Abstract 明确 '(OpenVLA-7B on LIBERO)'。"
48	    resolution_round: 3
49	
50	  - id: R1-N4
51	    summary: "Design implications 完全基于 correlational evidence，Abstract/Conclusion 以 assertive 语气呈现"
52	    category: framing
53	    severity: critical
54	    status: resolved
55	    first_raised_round: 1
56	    last_seen_round: 2
57	    menti
…[truncated 6020 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 220 · 2026-05-17T18:00:21.740328+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "ROADMAP.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "ROADMAP.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 221 · 2026-05-17T18:00:23.146122+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/ROADMAP.md\", \"content\": \"# vla-ssd — Research Dashboard\\n\\n> 最后更新: 2026-05-17 16:01 UTC | 更新原因: D058 ablation results integrated, capacity trade-off finding, Paper Agent dispatched for §4.3 integration\\n\\n## 核心方向\\nToken-level functional specialization in VLA: image tokens instruction-blind, readout token as multimodal hub, VLA fine-tuning front-loads instruction routing, non-monotonic vision encoder refinement. 详见 paper_framing.md。\\n\\n## 当前进展\\n**Paper Polish Phase — Ablation 整合中**\\n\\n- 全部 11 项 Round 1-2 审稿问题已修复\\n- Story-level 审读完成（Discussion 扩展、CKA caveat、consistency fixes）\\n- **D058 L1 Ablation 关键发现**：\\n  - Classification 全 1.0（instruction identity 通过 residual stream 保留）\\n  - Action R² L1: +0.119 (p<0.0001, 10/10 tasks)——capacity trade-off 证明 functional specialization\\n  - 深层 L8/L13 不受影响（ns）——网络通过更深层补偿\\n  - Paper Agent 正在整合进 §4.3（新段落 + 小表 + Discussion 更新）\\n- Threshold sensitivity: three-condition gradient 在 30%-70% 稳健（Appendix）\\n- Limitations 扩展：C1 architecture-general（causal mask）vs C2 potentially architecture-specific\\n- 50 个成功实验 + 7 个 negative + 2 benchmarks + 5 项 robustness + 1 causal intervention\\n\\n## 近期任务\\n- [ ] Paper Agent 完成 ablation 整合（§4.3 + Table + Discussion）\\n- [ ] 确认正文 ≤ 8 页\\n- [ ] 提交 Round 3 审稿\\n- [ ] Round 3 修复（如需要）\\n- [ ] Abstract DDL: May 26 / Paper DDL: May 29\\n\\n## GPU 预算\\nwestd-19183: cuda:0 + cuda:1（2× GPU）\\n已用 ~20 GPU·h（含 ablation ~2h），剩余 ~4 GPU·h 保留给 Round 3\\n\\n## 投稿信息\\n- 目标: CoRL 2026\\n- Abstract DDL: 2026-05-26\\n- Paper DDL: 2026-05-29\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D059 | 2026-05-17 | 保留 GPU 预算给 Round 3 响应，不主动补做 L1 MLP ablation；Claim  | l1_head_ablation |\\n| D058 | 2026-05-17 | L1 ablation 发现 capacity trade-off：instruction head | l1_head_ablation |\\n| D057 | 2026-05-17 | 启动 L1 attention head ablation 实验，将 C2 从 correlatio | plan_0
…[truncated 902 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 222 · 2026-05-17T18:00:23.450301+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd -name \"config.yaml\" -o -name \"project.yaml\" -o -name \"*.toml\" 2>/dev/null | head -5",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd -name \"config.yaml\" -o -name \"project.yaml\" -o -name \"*.toml\" 2>/dev/null | head -5",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 223 · 2026-05-17T18:00:23.601915+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 224 · 2026-05-17T18:00:27.017706+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_15 -maxdepth 2 -name \"config.yaml\" 2>/dev/null",
  "description": "Find config.yaml in project root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_15 -maxdepth 2 -name \"config.yaml\" 2>/dev/null",
    "description": "Find config.yaml in project root"
  }
}
```

</details>

---


### Tool result

_source line 225 · 2026-05-17T18:00:27.068373+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 226 · 2026-05-17T18:00:30.632533+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_15 -maxdepth 3 -name \"*.yaml\" -path \"*/config*\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0509_15 -maxdepth 1 -name \"*.yaml\" 2>/dev/null | head -10",
  "description": "Find yaml config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_15 -maxdepth 3 -name \"*.yaml\" -path \"*/config*\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0509_15 -maxdepth 1 -name \"*.yaml\" 2>/dev/null | head -10",
    "description": "Find yaml config files"
  }
}
```

</details>

---


### Tool result

_source line 227 · 2026-05-17T18:00:30.733371+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/config/projects/vla-ssd.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/config/venue_rules/corl-2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/config/venue_rules/emnlp-2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/config/resources.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/config/pending_approval_notifications.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 228 · 2026-05-17T18:00:32.946600+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/config/projects/vla-ssd.yaml",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/config/projects/vla-ssd.yaml",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 229 · 2026-05-17T18:00:33.398871+00:00_

1	execution:
2	  gpu_ids:
3	  - cuda:0
4	  - cuda:1
5	  project_path: /root/vla-ssd
6	  servers:
7	  - westd-19183
8	feishu:
9	  chat_id: oc_a1d032cbe70bdd2058438e67e0d57613
10	  operational_chat_id: oc_9e9aef1687e6abd097aa0edaf0551ee3
11	  review_paper_path: projects/vla-ssd/docs/paper/main.tex
12	  review_round: 3
13	  review_supplementary_paths: ''
14	  submission_chat_id: oc_554a5023cde4d603635cf97e6ab8151a
15	project:
16	  created_at: '2026-05-15T04:32:26.871Z'
17	  description: 'VLA-SSD: Do VLAs Know Which Demonstrations Are Good? Self-Referential
18	    Quality Scoring from Pretrained Representations'
19	  name: vla-ssd
20	  phase: research
21	  source_idea_id: idea_004
22	venue: corl-2026
23	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 230 · 2026-05-17T18:00:33.399271+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/config/venue_rules/corl-2026.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/config/venue_rules/corl-2026.yaml"
  }
}
```

</details>

---


### Tool result

_source line 231 · 2026-05-17T18:00:33.449650+00:00_

1	rules:
2	  research: []
3	  review: []
4	  writing: []
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 232 · 2026-05-17T18:01:31.731046+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查**方法与实验严谨性**。\n\n## 论文信息\n- **标题**: Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\n- **文件路径**: `projects/vla-ssd/docs/paper/main.tex`（多文件结构：abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, appendix.tex, references.bib）\n- **目标 Venue**: CoRL 2026（10th Conference on Robot Learning）\n- **截止日期**: Paper 2026-05-28 EOD\n- **格式**: 8 页正文 + references + appendix，双盲审稿，corl_2026 模板\n- **匿名规则**: 双盲（double-blind）\n- **Limitations**: 必须包含，计入 8 页\n\n## 你的审查侧重\n\n**方法与实验严谨性**，具体关注：\n\n1. **Probing 方法论**：\n   - Cross-instruction probe (10-way classification) 的设计是否合理？10 个 task 做 10-way classification 是否有 confound？\n   - MLP probe 的 capacity 控制是否充分？2 层 256 hidden 是否 overly expressive 或 underpowered？\n   - LOOCV 的实施是否正确？leave-one-out 在这个 setting 下的含义是什么？\n\n2. **RSA 正确性**：\n   - Cosine distance for representations + Euclidean for actions 的混合距离函数是否有理论依据？\n   - Within-task RSA 设计（50 demos per task）的统计 power 是否足够？\n   - \"Inverted-U\" claim 的统计支撑（bootstrap CI 是否 exclude zero at peak vs. endpoints）\n\n3. **统计检验**：\n   - Bootstrap 10,000 resamples 的置信区间报告是否一致？\n   - p 值的多重比较校正（family-wise error）是否需要？\n   - \"n.s.\" 结果（RSA best-vs-best Δ=+0.017, CI includes 0）的解释是否恰当\n\n4. **Ablation 设计**：\n   - L1 attention ablation（zeroing instruction attention）的设计合理性\n   - 5 demos vs 50 demos 的 probe 是否 comparable？论文说 \"absolute values are not directly comparable\" 但仍做 within-condition comparison，是否 valid？\n   - 三条件（trained/pretrained/untrained）是否充分隔离各因素？\n\n5. **实验控制**：\n   - Vision encoder 在三个条件下都是 frozen 的——这是 feature 还是 confound？\n   - 只用 OpenVLA-7B + LIBERO 的 generalizability 限制\n   - Cross-benchmark validation (LIBERO-Spatial) 是否构成足够的外部效度\n\n6. **数据一致性**：\n   - 正文 Table vs Appendix Table 的数值是否一致\n   - L1 heads 数量在不同位置报告是否一致（25 vs 24 vs ±1 解释）\n\n请按标准审稿格式输出：Summary → Strengths → Weaknesses → Questions → Minor Issues。\nWeakness 分为 Must-Fix / Should-Fix / Nice-to-Have 三级。",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责审查**方法与实验严谨性**。\n\n## 论文信息\n- **标题**: Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\n- **文件路径**: `projects/vla-ssd/docs/paper/main.tex`（多文件结构：abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, appendix.tex, references.bib）\n- **目标 Venue**: CoRL 2026（10th Conference on Robot Learning）\n- **截止日期**: Paper 2026-05-28 EOD\n- **格式**: 8 页正文 + references + appendix，双盲审稿，corl_2026 模板\n- **匿名规则**: 双盲（double-blind）\n- **Limitations**: 必须包含，计入 8 页\n\n## 你的审查侧重\n\n**方法与实验严谨性**，具体关注：\n\n1. **Probing 方法论**：\n   - Cross-instruction probe (10-way classification) 的设计是否合理？10 个 task 做 10-way classification 是否有 confound？\n   - MLP probe 的 capacity 控制是否充分？2 层 256 hidden 是否 overly expressive 或 underpowered？\n   - LOOCV 的实施是否正确？leave-one-out 在这个 setting 下的含义是什么？\n\n2. **RSA 正确性**：\n   - Cosine distance for representations + Euclidean for actions 的混合距离函数是否有理论依据？\n   - Within-task RSA 设计（50 demos per task）的统计 power 是否足够？\n   - \"Inverted-U\" claim 的统计支撑（bootstrap CI 是否 exclude zero at peak vs. endpoints）\n\n3. **统计检验**：\n   - Bootstrap 10,000 resamples 的置信区间报告是否一致？\n   - p 值的多重比较校正（family-wise error）是否需要？\n   - \"n.s.\" 结果（RSA best-vs-best Δ=+0.017, CI includes 0）的解释是否恰当\n\n4. **Ablation 设计**：\n   - L1 attention ablation（zeroing instruction attention）的设计合理性\n   - 5 demos vs 50 demos 的 probe 是否 comparable？论文说 \"absolute values are not directly comparable\" 但仍做 within-condition comparison，是否 valid？\n   - 三条件（trained/pretrained/untrained）是否充分隔离各因素？\n\n5. **实验控制**：\n   - Vision encoder 在三个条件下都是 frozen 的——这是 feature 还是 confound？\n   - 只用 OpenVLA-7B + LIBERO 的 generalizability 限制\n   - Cross-benchmark validation (LIBERO-Spatial) 是否构成足够的外部效度\n\n6. **数据一致性**：\n   - 正文 Table vs Appendix Table 的数值是否一致\n   - L1 heads 数量在不同位置报告是否一致（25 vs 24 vs ±1 解释）\n\n请按标准审稿格式输出：Summary → Strengths → Weaknesses → Questions → Minor Issues。\nWeakness 分为 Must-Fix / Should-Fix / Nice-to-Have 三级。",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 233 · 2026-05-17T18:01:55.561126+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 23830
}
```

</details>

---


### Tool call

_source line 234 · 2026-05-17T18:01:55.762285+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查**新颖性/影响力 + 写作/格式合规**。\n\n## 论文信息\n- **标题**: Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\n- **文件路径**: `projects/vla-ssd/docs/paper/main.tex`（多文件结构：abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, appendix.tex, references.bib）\n- **目标 Venue**: CoRL 2026（10th Conference on Robot Learning）\n- **截止日期**: Paper 2026-05-28 EOD\n- **格式**: 8 页正文 + references + appendix，双盲审稿，corl_2026 模板\n- **匿名规则**: 双盲（double-blind）\n- **Limitations**: 必须包含，计入 8 页\n\n## 你的审查侧重\n\n**新颖性/影响力 + 写作/格式**，具体关注：\n\n### A. 新颖性与影响力\n\n1. **与直接竞争者的区分度**：\n   - Grant et al. (2026, arXiv:2603.19233) — 同为 VLA 内部表征分析，behavioral intervention（activation injection, SAE, probing）发现 visual dominance + language \"encoded but not used\"。本文的 token-level decomposition + trained-vs-untrained factorial control 是否构成足够增量？\n   - Swann et al. (2026) — SAE on OpenVLA。本文与之的互补性如何？\n   - Rizzardo/Buurmeijer et al. (2026) — feature observability/controllability on VLAs。\n   - Häon et al. (CoRL 2025) — 第一篇 VLA mechanistic interpretability（activation steering）。\n\n2. **贡献的显著性**：\n   - C1（token-level specialization）：image tokens instruction-blind 是否可以从 causal mask 的 architecture 直接预测？如果 image tokens 在 causal attention 中看不到后面的 instruction tokens，那么 instruction-blind 是 trivial consequence 还是 empirical finding？\n   - C2（front-loaded routing）：entry-exit attention pattern 的 practical implication 是什么？\n   - C3（inverted-U refinement）：non-monotonic RSA 在 neuroscience 和 deep learning 中已有先例，novelty 在于 VLA-specific application？\n\n3. **对 CoRL 社区的价值**：\n   - 分析型论文（无新方法/无新 benchmark/无性能提升）在 CoRL 的接受度\n   - Actionable insights 是否足够——论文的 findings 是否能指导 VLA 设计？\n\n### B. 写作质量\n\n1. **叙事结构**：Abstract/Intro/Method/Experiments/Discussion 的主线是否连贯一致\n2. **AI 写作痕迹**：\n   - grep 检查 em-dash（—）和 en-dash（ – ）\n   - 检查 -ing 分词短语结尾\n   - 检查 \"Furthermore\"/\"Moreover\"/\"Additionally\" 过度使用\n   - 检查 \"leverage\"/\"utilize\"/\"delve into\" 等 AI 高频词\n3. **数字和精度一致性**：全文数字精度是否统一\n4. **图表质量**：信息密度、字体大小、caption 自包含性\n5. **专有名词定义**：首次出现是否定义\n\n### C. CoRL 2026 格式合规\n\n1. **页数**：正文是否 ≤ 8 页\n2. **模板**：`\\usepackage{corl_2026}` 是否正确（review 版不应用 `[final]`）\n3. **匿名化**：是否有泄露身份的信息（致谢、代码链接、自引）\n4. **Limitations section**：是否存在且在 8 页内\n5. **引用格式**：bib 格式一致性，是否有 preprint 应更新为正式发表版本\n6. **引用充足度**：引用数量和覆盖范围是否达标\n\n请按标准审稿格式输出：Summary → Strengths → Weaknesses → Questions → Minor Issues。\nWeakness 分为 Must-Fix / Should-Fix / Nice-to-Have 三级。",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责审查**新颖性/影响力 + 写作/格式合规**。\n\n## 论文信息\n- **标题**: Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\n- **文件路径**: `projects/vla-ssd/docs/paper/main.tex`（多文件结构：abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, appendix.tex, references.bib）\n- **目标 Venue**: CoRL 2026（10th Conference on Robot Learning）\n- **截止日期**: Paper 2026-05-28 EOD\n- **格式**: 8 页正文 + references + appendix，双盲审稿，corl_2026 模板\n- **匿名规则**: 双盲（double-blind）\n- **Limitations**: 必须包含，计入 8 页\n\n## 你的审查侧重\n\n**新颖性/影响力 + 写作/格式**，具体关注：\n\n### A. 新颖性与影响力\n\n1. **与直接竞争者的区分度**：\n   - Grant et al. (2026, arXiv:2603.19233) — 同为 VLA 内部表征分析，behavioral intervention（activation injection, SAE, probing）发现 visual dominance + language \"encoded but not used\"。本文的 token-level decomposition + trained-vs-untrained factorial control 是否构成足够增量？\n   - Swann et al. (2026) — SAE on OpenVLA。本文与之的互补性如何？\n   - Rizzardo/Buurmeijer et al. (2026) — feature observability/controllability on VLAs。\n   - Häon et al. (CoRL 2025) — 第一篇 VLA mechanistic interpretability（activation steering）。\n\n2. **贡献的显著性**：\n   - C1（token-level specialization）：image tokens instruction-blind 是否可以从 causal mask 的 architecture 直接预测？如果 image tokens 在 causal attention 中看不到后面的 instruction tokens，那么 instruction-blind 是 trivial consequence 还是 empirical finding？\n   - C2（front-loaded routing）：entry-exit attention pattern 的 practical implication 是什么？\n   - C3（inverted-U refinement）：non-monotonic RSA 在 neuroscience 和 deep learning 中已有先例，novelty 在于 VLA-specific application？\n\n3. **对 CoRL 社区的价值**：\n   - 分析型论文（无新方法/无新 benchmark/无性能提升）在 CoRL 的接受度\n   - Actionable insights 是否足够——论文的 findings 是否能指导 VLA 设计？\n\n### B. 写作质量\n\n1. **叙事结构**：Abstract/Intro/Method/Experiments/Discussion 的主线是否连贯一致\n2. **AI 写作痕迹**：\n   - grep 检查 em-dash（—）和 en-dash（ – ）\n   - 检查 -ing 分词短语结尾\n   - 检查 \"Furthermore\"/\"Moreover\"/\"Additionally\" 过度使用\n   - 检查 \"leverage\"/\"utilize\"/\"delve into\" 等 AI 高频词\n3. **数字和精度一致性**：全文数字精度是否统一\n4. **图表质量**：信息密度、字体大小、caption 自包含性\n5. **专有名词定义**：首次出现是否定义\n\n### C. CoRL 2026 格式合规\n\n1. **页数**：正文是否 ≤ 8 页\n2. **模板**：`\\usepackage{corl_2026}` 是否正确（review 版不应用 `[final]`）\n3. **匿名化**：是否有泄露身份的信息（致谢、代码链接、自引）\n4. **Limitations section**：是否存在且在 8 页内\n5. **引用格式**：bib 格式一致性，是否有 preprint 应更新为正式发表版本\n6. **引用充足度**：引用数量和覆盖范围是否达标\n\n请按标准审稿格式输出：Summary → Strengths → Weaknesses → Questions → Minor Issues。\nWeakness 分为 Must-Fix / Should-Fix / Nice-to-Have 三级。",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 235 · 2026-05-17T18:01:57.122043+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1359
}
```

</details>

---


### Assistant

_source line 236 · 2026-05-17T18:02:06.336715+00:00_

Reviewer 1（方法/实验严谨性）和 Reviewer 2（新颖性/影响力 + 写作/格式）已分配。等待两位 Reviewer 独立审稿结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 24

## Round 24

2 recorded events


### User

_source line 237 · 2026-05-17T18:07:41.814546+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1: 方法与实验严谨性审查

## 论文信息
- **标题**: Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model
- **Venue**: CoRL 2026

---

## 总体评分

**Overall**: 3/5 (Borderline)

**一句话总结**: 实验设计思路清晰、factorial control 有价值，但核心 probing 任务过于简单导致 claim 强度与证据不匹配，RSA inverted-U 的效应量极小，ablation 使用不同数据规模削弱因果推断力度。

---

## 官方维度打分（基于 CoRL reviewer guidelines: Originality, Quality, Clarity, Significance, Relevance）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Originality | 4/5 | Token-level factorial decomposition of VLA 是新颖的分析框架，prior work 没有做过 trained-vs-untrained 的系统对比 |
| Quality (Technical Soundness) | 2.5/5 | 核心 probe 任务 trivially easy，RSA 效应量极小且 metric-dependent，ablation 数据规模不一致，缺乏多重比较校正 |
| Clarity | 4/5 | 写作清晰、结构完整，数据呈现系统化 |
| Significance | 3/5 | 对 VLA 内部机制提供了描述性洞察，但因证据力度不足，architectural implications 缺乏可操作性 |
| Relevance | 4/5 | VLA 内部机制分析直接服务于 robot learning 社区的模型设计需求 |

---

## Summary

本文对 OpenVLA-7B 在 LIBERO 上进行 token 级别表征分析，通过 cross-instruction probes、attention 分析、RSA 和 MLP probes 四种方法，比较 trained/pretrained/untrained 三个条件。主要发现：(1) image tokens 不编码 instruction 信息，readout token 是唯一的多模态汇聚点；(2) VLA fine-tuning 将 instruction routing 从中层转移到 entry-exit 模式；(3) LLM 对 vision encoder 输出进行非单调变换（inverted-U）。实验设计的 factorial structure 值得肯定，但多个核心 claim 的证据强度存在问题。

---

## Strengths

**S1. 系统化的实验设计框架**
三条件（trained/pretrained/untrained）× 两因素（instruction presence）的 factorial design 是分析 VLA 的好范式。这比 prior work（如 Grant et al., Häon et al.）的单条件分析更有控制力。Appendix 的 robustness checks（distance metric invariance, per-DOF decomposition, permutation test, seed sensitivity, demo subsampling）体现了实验严谨态度。

**S2. 多指标互相验证**
RSA + MLP probe + attention analysis + cross-instruction probe 四种方法从不同角度切入同一问题，且 CKA 作为 supplementary metric 在 appendix 中报告，体现了方法论意识。

**S3. 诚实报告 negative/null results**
RSA best-vs-best Δ=+0.017 (CI includes 0) 被如实标记为 n.s.；CKA 与 RSA 的 ordering 矛盾被正面讨论而非隐藏。这是好的学术实践。

**S4. Cross-benchmark validation**
LIBERO-Spatial 上的复现增加了核心发现的可信度（尽管仍在同一 simulator 内）。

---

## Weaknesses

### Must-Fix 问题（影响接收决定）

**N1** [critical] Cross-instruction probe 任务 trivially easy，不支撑 "multimodal convergence" 的强 claim

- 具体位置：Section 4.2 (Token-Level Functional Specialization), Table 1
- 问题：10-way classification over 10 distinct instruction strings 对任何能 attend to instruction tokens 的位置都是 trivial 的。论文自己在 Appendix D.1 承认 "even incidental attention (~12%) suffices for linear classification at L1"。事实上，untrained model（随机权重）在 L1 也达到 100%（Table 1）。这意味着 100% 分类准确率不能作为 "multimodal convergence" 或 "functional specialization" 的强证据——它只反映 instruction embeddings 本身是线性可分的（这是 tokenizer 的 trivial 性质）。
- 为什么影响接收：Finding 1（"strict token-level functional specialization"）是论文三大贡献之首，也是标题的核心 claim。如果 readout token 的 100% 准确率是 trivial baseline（随机权重也能达到），那么这个发现的 novelty 大幅缩水。真正有价值的发现是 image token 保持 chance level，但论文的对称叙事（"image blind + readout as hub"）过度依赖 readout 侧的结果。
- 建议修改方向：(a) 增加更困难的 probe 任务（如区分语义相近的指令、或 fine-grained instruction attribute prediction）；(b) 调整 framing——将重点放在 image token 的 instruction-blindness（这是 non-trivial 的 negative result）而非 readout 的 100%（这是 trivial 的 positive result）；(c) 对 untrained 也达到 100%@L1 做更深入讨论——如果随机权重即可实现，trained model 维持 100% 的 significance 需要重新定义。

**N2** [critical] RSA "inverted-U" 的 rise phase 效应量极小（Δρ = 0.016），且 metric-dependent

- 具体位置：Section 4.3, Figure 3, Table 3; Appendix B.2
- 问题：Trained image_mean RSA 从 L0 (0.612) 到 L12 (0.628) 的升幅仅为 0.016（2.6%）。Best-vs-best training effect (+0.017) 的 CI 包含 0。更严重的是，Appendix B.2 显示 linear CKA 完全逆转了 RSA ordering（untrained > trained > DINOv2），且 linear CKA per-layer profile 呈单调上升，完全没有 inverted-U。这意味着 "non-monotonic refinement" 是 metric-specific 的描述，而非 representation 的 intrinsic property。
- 为什么影响接收：Finding 3（"non-monotonic refinement of vision encoder output"）是论文贡献之一。如果这个 pattern 仅在 RSA（Spearman rank correlation on cosine-distance RDMs）下成立，在另一个标准 metric（CKA）下消失甚至逆转，那么 generalizability 成问题。论文的 architectural implication（"vision encoder quality matters more than LLM scale"）建立在 DINOv2 RSA 最高这个 RSA-specific 结果上。
- 建议修改方向：(a) 明确 qualify claims 的 metric-dependence（"under RSA, we observe..."）；(b) 讨论为什么 RSA 比 CKA 更 appropriate for this question（目前 Method §3.5 的 justification 不够充分——"CKA is sensitive to kernel choice" 同样可以反过来说 RSA 对 distance function 选择敏感）；(c) 考虑 inverted-U 的 rise phase 是否在统计上 significant——L0→L12 的 +0.016 需要 CI。

**N3** [critical] L1 attention ablation 使用 5 demos（vs 主实验 50 demos），因果推断的可靠性存疑

- 具体位置：Section 4.2, paragraph "Ablation reveals functional specialization"（第76行）
- 问题：Ablation 实验仅使用 5 demos per task（50 个 total datapoints），而主实验 Table 3 使用 50 demos per task。论文承认 "absolute values are not directly comparable" 但仍得出强因果结论（"instruction-dominant heads redirect attention from image to instruction tokens at the cost of local action encoding"）。用 50 个数据点训练一个 2-layer MLP probe（>1M 参数），然后报告 R² 从 0.256 到 0.375 的提升——这个 R² 的 baseline 本身就非常低（0.256），暗示 probe 在 5 demos 下严重 underfitting，ablation "improvement" 可能是 reduced effective input dimensionality 带来的 regularization effect 而非 genuine functional specialization。
- 为什么影响接收：这是论文中唯一的 causal intervention（其余都是 observational）。如果 ablation 不可靠，论文就只有 correlational evidence。
- 建议修改方向：(a) 用 50 demos 重跑 ablation，使 baseline R² 与 Table 3 直接 comparable；(b) 如果 50 demos 不可行，至少报告 N（总 observation-action pairs 数）并讨论 probe capacity vs sample size 的比率；(c) 添加 random ablation control（随机 zero 同等数量的 non-instruction-dominant heads）以排除 "任何 attention zeroing 都能提升 R²" 的 confound。

---

### Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 缺乏多重比较校正（family-wise error）

- 具体位置：贯穿全文所有统计检验
- 问题：论文对 32 层 × 3 条件 × 多个 metric 进行了大量逐层比较，但没有任何 Bonferroni、Holm、或 FDR 校正。虽然单个 bootstrap CI 是 valid 的，但在数十个比较中找到 p < 0.05 的概率很高。
- 建议：至少对 key claims（inverted-U peak significance、training effects per layer）应用 FDR correction 并报告 adjusted p-values。

**W2** [warning] Probe 的 total N 未报告，capacity 控制不充分

- 具体位置：Section 3.5 (Functional Action Probes), Section 4.1 (Experimental Setup)
- 问题：50 demos per task × 10 tasks = 500 demonstrations，但每个 demo 有多少 timesteps？Total N（observation-action pairs for probe training）从未明确报告。2-layer MLP (4096→256→7) 有 ~1.05M 参数。如果 N < 10,000，probe 可能 overfit；如果 N > 100,000，probe 可能 underfit。Early stopping (patience 5) 是部分 mitigation 但不充分。
- 建议：报告 exact N；添加 linear probe 作为 capacity lower-bound（Method 中提到 linear probe 也在 image_mean 上得 10%，但未对 R² 做 linear vs MLP 对比）。

**W3** [warning] "Untrained" condition 的 L1 = 100% 结果削弱 Finding 1 的 interpretation

- 具体位置：Table 1, Appendix D.1
- 问题：随机初始化的 LLM 在 L1 也能实现 100% instruction classification。论文将此解释为 "incidental"（附录说 ~12% attention 即可），但这暴露了 probe 任务的 trivial nature。更重要的是，untrained model 的 100%→82% 衰减 pattern 很有趣但讨论不足——为什么随机权重会导致信息逐层丢失？这可能揭示 residual stream 中 signal-to-noise ratio 的衰减，值得展开。
- 建议：增加讨论 untrained 的 decay mechanism；考虑 probe 任务难度是否足以区分 "genuine multimodal integration" 和 "trivial linear separability"。

**W4** [warning] Frozen vision encoder 是 feature 但也是 confound

- 具体位置：Section 3.1 (Model and Data)
- 问题：三个条件共享 frozen vision encoder 和 projector，这使得 image_mean 在 L0 的起始 representation 完全相同。论文因此无法评估 VLA training 对 vision processing 的 full effect（只能评估 LLM 如何处理固定的 vision output）。然而论文在 Discussion 中得出 "vision encoder quality may matter more than LLM scale" 这一 architectural implication——这个结论需要 across-encoder 实验（如换 CLIP-only encoder），而非单一 frozen encoder 内的分析。
- 建议：qualify 这个 architectural implication 为 "under fixed encoder" 条件下的观察；或增加对比实验（不同 vision encoder 的 RSA comparison）。

**W5** [warning] 25 vs 24 heads 不一致需要更清晰解释

- 具体位置：Table 2 报告 L1 VLA-trained = 25/32；Appendix Table 10 (threshold sensitivity) 在 50% threshold 报告 24；Appendix Table 9 也报告 24/32
- 问题：同一数据、同一阈值（50%）下，Table 2 得 25 而 Appendix 得 24。论文解释为 "bulk extraction vs dedicated per-layer analysis"，但如果分析的是同一个 model checkpoint 的同一层同一 batch 的 attention weights，结果应一致。这暗示可能存在 batch sampling variance 或计算细节差异（如 attention 是否 averaged over all readout positions）。
- 建议：明确说明两个分析使用了哪些不同的 input samples 或 averaging 方式导致了 ±1 差异。

---

## Questions to Authors

**Q1**: Cross-instruction probe 使用 linear classifier 还是 MLP？Section 3.3 说 "linear classifier (10-way)"，但 Section 4.2 又说 "Both linear and MLP probes confirm chance-level performance (10%)"。主结果（Table 1 的 100%）用的是哪个？

**Q2**: Ablation 中 "5 demonstrations per task" 对应多少 total observation-action pairs？每个 demo 的平均 trajectory 长度是多少？

**Q3**: RSA 中 "within-task observation pairs from 50 demonstrations" — 每个 demo 取一个 observation 还是多个？如果是多个，同一 demo 内的 temporal autocorrelation 是否 inflate 了 RSA？

**Q4**: Table 3 中 "VLA Trained readout" RSA peak = L12 (ρ=0.643)，但 Section 4.3 说 "trained image_mean RSA peaks at L12 (ρ=0.628)"。Readout 的 peak RSA (0.643) 也在 L12？这在正文中未明确标注 readout 的 per-layer profile——readout RSA 是否也呈 inverted-U？

**Q5**: Untrained readout 在 Table 3 中 R² peak = L32 (0.609)。这意味着随机权重经过 32 层变换后反而是最好的 action-prediction representation？这如何解释？

---

## Minor Issues（不影响接收）

- Abstract 第6行 "self-supervised DINOv2 providing the highest geometric foundation (ρ = 0.692, exceeding all internal representations)" — 建议加 "under RSA" qualifier，因为 CKA 下结论相反。
- Section 4.2 第76行的长括号句（"using 5 demonstrations per task; absolute values are not directly comparable to Table 3 but within-condition comparisons are valid"）应移至方法描述处而非嵌入结果报告。
- Discussion "C1 likely generalizes via the causal mask; C2 may be Llama-2-specific" — 这种无证据的猜测不应出现在学术论文中，建议删除或改为 explicit future work。
- Appendix §D.4 Table 9 caption 中 "Head counts from the 32-layer bulk extraction vary by ±1 from dedicated per-layer analyses (Table 2) due to threshold boundary cases" — 此解释应在正文 Table 2 附近出现，不应让读者到 appendix 才发现不一致的原因。

---

## 主要优势总结

- Factorial trained-vs-untrained control 是分析 VLA 的优秀实验范式
- 四种互补分析方法（probe + attention + RSA + MLP）提供多角度验证
- 诚实报告 null results 和 metric divergence
- Appendix 中大量 robustness checks 体现严谨态度
- Cross-benchmark (LIBERO-Spatial) validation 增加可信度

---

## 总体判断

论文的实验框架和 factorial design 是其最大优势，但三个核心 claims 的证据强度均有问题：(1) readout 100% 是 trivial baseline；(2) inverted-U rise phase 极小且 metric-dependent；(3) ablation 使用不同数据规模。如果作者能在 rebuttal 中 (a) 用更难的 probe 任务验证 Finding 1、(b) 报告 L0→L12 升幅的 CI、(c) 用 50 demos 重跑 ablation，评分可提升至 borderline accept。当前状态下，claim-evidence mismatch 是主要顾虑。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 238 · 2026-05-17T18:07:51.533393+00:00_

Reviewer 1 审稿已收到。核心发现：3/5 Borderline，三个 critical issues（probe trivially easy、inverted-U 效应量小且 metric-dependent、ablation 数据规模不一致）。

等待 Reviewer 2 审稿完成后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 25

## Round 25

2 recorded events


### User

_source line 239 · 2026-05-17T18:07:54.073756+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**核心判断**：Overall 3/5 (Borderline)。论文的 factorial experimental design 是优势，但三个主要 findings 的证据强度均存在问题：

1. **N1 [critical]**: Cross-instruction probe 10-way 分类对 readout token 是 trivially easy（随机权重也达到 100%@L1），不支撑 "multimodal convergence hub" 的强 claim
2. **N2 [critical]**: RSA inverted-U 的 rise phase 仅 Δρ=0.016（2.6%），且 CKA 下完全消失/逆转，metric-dependent
3. **N3 [critical]**: L1 attention ablation 用 5 demos vs 主实验 50 demos，因果推断可靠性不足

如果作者能在 rebuttal 中解决这三个问题（更难 probe 任务、报告 rise CI、50-demo ablation），评分可上调。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 240 · 2026-05-17T18:08:05.558510+00:00_

Reviewer 1 审稿已收到。3 个 critical issues（probe trivially easy、RSA rise phase 极小且 metric-dependent、ablation 数据规模不一致）。等待 Reviewer 2 完成后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 26

## Round 26

6 recorded events


### User

_source line 241 · 2026-05-17T18:13:36.739872+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见：Vision Encodes, Language Routes

**Overall: 5/10 (Marginally below acceptance threshold)**
**Confidence: 4/5**

**一句话总结**: 方法论严谨、写作清晰，但核心贡献 C1（image tokens instruction-blind）是 causal attention mask 的数学必然结果而非经验性发现，显著削弱新颖性；其余贡献效应量小或存在度量敏感性问题，对 CoRL 社区缺乏 actionable insights。

---

### 主要优势
- S1: 系统化 2×2 factorial control（trained/untrained × instruction/no-instruction），三条件对比有效 disentangle language pretraining 与 VLA fine-tuning
- S2: 充分的 robustness analysis（distance metric invariance, per-DOF, permutation test, seed sensitivity, demo subsampling, cross-benchmark）
- S3: 写作质量良好，无 AI 写作痕迹，叙事连贯
- S4: L1 attention ablation 提供了少有的 interventional causal evidence

---

### Must-Fix 问题

**N1 [critical] C1 是 causal mask 的数学必然结果**
OpenVLA 的 token 序列为 [image] → [instruction] → [readout/action]。Causal attention 中位置 i 的表征仅依赖位置 ≤ i。Image tokens 先于 instruction tokens，因此 image tokens 在任何层都无法 attend to instruction tokens——这是架构决定的数学性质，非 empirical finding。Frozen vision encoder 只接收图像，instruction invariance 同样 trivially expected。Discussion 仅一句话承认（"C1 likely generalizes via the causal mask"），但全文将 C1 作为首要贡献和标题基础。untrained 模型 L1 即达 100% classification 进一步支持 trivial 判断。建议重新定位 C1 或澄清 token ordering。

**N2 [critical] RSA 与 CKA 矛盾未充分解决**
Linear CKA 完全反转 RSA ordering（untrained > trained > DINOv2），直接否定 "DINOv2 provides highest geometric foundation"。RDM kernel CKA 中 DINOv2 在所有变体排名最低。Linear CKA per-layer profile 无 inverted-U。论文将此放在 appendix 归因于 "metrics capture different properties"，但未给出 principled argument 解释为何应信任 RSA。如果核心 claims 依赖度量选择，它们就不是 robust findings。

---

### Should-Fix 问题

**W1** RSA best-vs-best 训练效应在 LIBERO-Goal 不显著（Δ=+0.017, CI includes 0, n.s.），但 Abstract/Intro 中未标注
**W2** L1 ablation 使用 5 demos（vs. 主实验 50），R² 基准差异大（0.256 vs. ~0.65），可比性存疑
**W3** 缺少 Llama-2 和 Open X-Embodiment 关键引用
**W4** Architectural implications 仅为 observational insights，未通过设计实验验证（如 encoder swap），对 CoRL 实践社区 actionable value 不足
**W5** 单模型（OpenVLA-7B）、单 benchmark family（LIBERO），泛化性有限

---

### 小问题
- M1: Intro "untested assumption" 是 straw man（causal mask 下无人会这样假设）
- M2: "readout token" 与 "last_preaction" 交替使用未定义等价性
- M3: conclusion.tex 未被 main.tex \input
- M4: alain2017 实际年份应为 2016；nostalgebraist2020 blog post 格式不规范
- M5: 多个 arXiv preprints 可能已有正式发表版本
- M6: 个别 R² 精度不统一（2位 vs. 3位）

---

### 格式合规
- 模板 ✓，匿名化 ✓，AI 痕迹 ✓
- ⚠ 缺 Llama-2/OXE 引用，部分 preprint 应更新
- ⚠ Limitations section 较简短

### 与竞争者区分度
Grant et al. (2026) 已发现 visual dominance + language "encoded but not used"。本文的 token-level 分解在 causal mask 约束下提供的额外 insight 有限。Häon et al. (CoRL 2025) 提供了 interventional analysis（activation steering），本文主要是 observational。整体增量有限。

### 建议
若能解决 N1（重新定位 C1 或论证 non-trivial token ordering）和 N2（正文讨论 CKA 矛盾），并增加一个 analysis-to-design bridge experiment，论文可提升至 borderline accept。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 242 · 2026-05-17T18:14:05.039446+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每一条使用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n**Overall: 5/10 (Marginally below acceptance threshold)**\n**Confidence: 4/5**\n\n**一句话总结**: 方法论严谨、写作清晰，但核心贡献 C1（image tokens instruction-blind）是 causal attention mask 的数学必然结果而非经验性发现，显著削弱新颖性；其余贡献效应量小或存在度量敏感性问题，对 CoRL 社区缺乏 actionable insights。\n\n### Must-Fix 问题\n\n**N1 [critical] C1 是 causal mask 的数学必然结果**\nOpenVLA 的 token 序列为 [image] → [instruction] → [readout/action]。Causal attention 中位置 i 的表征仅依赖位置 ≤ i。Image tokens 先于 instruction tokens，因此 image tokens 在任何层都无法 attend to instruction tokens——这是架构决定的数学性质，非 empirical finding。Frozen vision encoder 只接收图像，instruction invariance 同样 trivially expected。Discussion 仅一句话承认（\"C1 likely generalizes via the causal mask\"），但全文将 C1 作为首要贡献和标题基础。untrained 模型 L1 即达 100% classification 进一步支持 trivial 判断。建议重新定位 C1 或澄清 token ordering。\n\n**N2 [critical] RSA 与 CKA 矛盾未充分解决**\nLinear CKA 完全反转 RSA ordering（untrained > trained > DINOv2），直接否定 \"DINOv2 provides highest geometric foundation\"。RDM kernel CKA 中 DINOv2 在所有变体排名最低。Linear CKA per-layer profile 无 inverted-U。论文将此放在 appendix 归因于 \"metrics capture different properties\"，但未给出 principled argument 解释为何应信任 RSA。如果核心 claims 依赖度量选择，它们就不是 robust findings。\n\n### Should-Fix 问题\n\n**W1** RSA best-vs-best 训练效应在 LIBERO-Goal 不显著（Δ=+0.017, CI includes 0, n.s.），但 Abstract/Intro 中未标注\n**W2** L1 ablation 使用 5 demos（vs. 主实验 50），R² 基准差异大（0.256 vs. ~0.65），可比性存疑\n**W3** 缺少 Llama-2 和 Open X-Embodiment 关键引用\n**W4** Architectural implications 仅为 observational insights，未通过设计实验验证（如 encoder swap），对 CoRL 实践社区 actionable value 不足\n**W5** 单模型（OpenVLA-7B）、单 benchmark family（LIBERO），泛化性有限\n\n### 小问题\n- M1: Intro \"untested assumption\" 是 straw man（causal mask 下无人会这样假设）\n- M2: \"readout token\" 与 \"last_preaction\" 交替使用未定义等价性\n- M3: conclusion.tex 未被 main.tex \\input\n- M4: alain2017 实际年份应为 2016；nostalgebraist2020 blog post 格式不规范\n- M5: 多个 arXiv preprints 可能已有正式发表版本\n- M6: 个别 R² 精度不统一（2位 vs. 3位）\n\n### 与竞争者区分度\nGrant et al. (2026) 已发现 visual dominance + language \"encoded but not used\"。本文的 token-level 分解在 causal mask 约束下提供的额外 insight 有限。Häon et al. (CoRL 2025) 提供了 interventional analysis（activation steering），本文主要是 observational。整体增量有限。\n\n---\n\n请逐条回应。",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每一条使用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n**Overall: 5/10 (Marginally below acceptance threshold)**\n**Confidence: 4/5**\n\n**一句话总结**: 方法论严谨、写作清晰，但核心贡献 C1（image tokens instruction-blind）是 causal attention mask 的数学必然结果而非经验性发现，显著削弱新颖性；其余贡献效应量小或存在度量敏感性问题，对 CoRL 社区缺乏 actionable insights。\n\n### Must-Fix 问题\n\n**N1 [critical] C1 是 causal mask 的数学必然结果**\nOpenVLA 的 token 序列为 [image] → [instruction] → [readout/action]。Causal attention 中位置 i 的表征仅依赖位置 ≤ i。Image tokens 先于 instruction tokens，因此 image tokens 在任何层都无法 attend to instruction tokens——这是架构决定的数学性质，非 empirical finding。Frozen vision encoder 只接收图像，instruction invariance 同样 trivially expected。Discussion 仅一句话承认（\"C1 likely generalizes via the causal mask\"），但全文将 C1 作为首要贡献和标题基础。untrained 模型 L1 即达 100% classification 进一步支持 trivial 判断。建议重新定位 C1 或澄清 token ordering。\n\n**N2 [critical] RSA 与 CKA 矛盾未充分解决**\nLinear CKA 完全反转 RSA ordering（untrained > trained > DINOv2），直接否定 \"DINOv2 provides highest geometric foundation\"。RDM kernel CKA 中 DINOv2 在所有变体排名最低。Linear CKA per-layer profile 无 inverted-U。论文将此放在 appendix 归因于 \"metrics capture different properties\"，但未给出 principled argument 解释为何应信任 RSA。如果核心 claims 依赖度量选择，它们就不是 robust findings。\n\n### Should-Fix 问题\n\n**W1** RSA best-vs-best 训练效应在 LIBERO-Goal 不显著（Δ=+0.017, CI includes 0, n.s.），但 Abstract/Intro 中未标注\n**W2** L1 ablation 使用 5 demos（vs. 主实验 50），R² 基准差异大（0.256 vs. ~0.65），可比性存疑\n**W3** 缺少 Llama-2 和 Open X-Embodiment 关键引用\n**W4** Architectural implications 仅为 observational insights，未通过设计实验验证（如 encoder swap），对 CoRL 实践社区 actionable value 不足\n**W5** 单模型（OpenVLA-7B）、单 benchmark family（LIBERO），泛化性有限\n\n### 小问题\n- M1: Intro \"untested assumption\" 是 straw man（causal mask 下无人会这样假设）\n- M2: \"readout token\" 与 \"last_preaction\" 交替使用未定义等价性\n- M3: conclusion.tex 未被 main.tex \\input\n- M4: alain2017 实际年份应为 2016；nostalgebraist2020 blog post 格式不规范\n- M5: 多个 arXiv preprints 可能已有正式发表版本\n- M6: 个别 R² 精度不统一（2位 vs. 3位）\n\n### 与竞争者区分度\nGrant et al. (2026) 已发现 visual dominance + language \"encoded but not used\"。本文的 token-level 分解在 causal mask 约束下提供的额外 insight 有限。Häon et al. (CoRL 2025) 提供了 interventional analysis（activation steering），本文主要是 observational。整体增量有限。\n\n---\n\n请逐条回应。",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 243 · 2026-05-17T18:14:31.753158+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 26713
}
```

</details>

---


### Tool call

_source line 244 · 2026-05-17T18:14:31.854068+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每一条使用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n**Overall: 3/5 (Borderline)**\n\n### Must-Fix 问题\n\n**N1 [critical]** Cross-instruction probe 任务 trivially easy，不支撑 \"multimodal convergence\" 的强 claim\n- 10-way classification over 10 distinct instruction strings 对任何能 attend to instruction tokens 的位置都是 trivial 的\n- 论文自己在 Appendix D.1 承认 \"even incidental attention (~12%) suffices for linear classification at L1\"\n- untrained model（随机权重）在 L1 也达到 100%（Table 1）\n- 100% 分类准确率不能作为 \"multimodal convergence\" 或 \"functional specialization\" 的强证据——它只反映 instruction embeddings 本身是线性可分的\n- 真正有价值的发现是 image token 保持 chance level，但论文的对称叙事过度依赖 readout 侧的结果\n- 建议增加更困难的 probe 任务或调整 framing\n\n**N2 [critical]** RSA \"inverted-U\" 的 rise phase 效应量极小（Δρ = 0.016），且 metric-dependent\n- Trained image_mean RSA 从 L0 (0.612) 到 L12 (0.628) 的升幅仅为 0.016（2.6%）\n- Best-vs-best training effect (+0.017) 的 CI 包含 0\n- Appendix B.2 显示 linear CKA 完全逆转了 RSA ordering\n- \"non-monotonic refinement\" 是 metric-specific 的描述，而非 representation 的 intrinsic property\n- 建议明确 qualify claims 的 metric-dependence，讨论为什么 RSA 比 CKA 更 appropriate\n\n**N3 [critical]** L1 attention ablation 使用 5 demos（vs 主实验 50 demos），因果推断的可靠性存疑\n- 用 50 个 total datapoints 训练 2-layer MLP probe（~1M 参数），baseline R²=0.256 暗示严重 underfitting\n- ablation \"improvement\" 可能是 reduced effective input dimensionality 带来的 regularization effect\n- 建议用 50 demos 重跑 ablation 或添加 random ablation control\n\n### Should-Fix 问题\n\n**W1** 缺乏多重比较校正（32 层 × 3 条件 × 多 metric 的逐层比较无 FDR/Bonferroni 校正）\n**W2** Probe 的 total N 未报告，capacity 控制不充分（4096→256→7 有 ~1.05M 参数）\n**W3** Untrained L1=100% 削弱 Finding 1 的 interpretation，讨论不足\n**W4** Frozen vision encoder 是 feature 但也是 confound：\"vision encoder quality > LLM scale\" 的 implication 需要 across-encoder 实验支持\n**W5** 25 vs 24 heads 不一致需要更清晰解释\n\n### Questions\n\nQ1: Cross-instruction probe 主结果（Table 1 的 100%）用的是 linear 还是 MLP？\nQ2: Ablation 中 5 demos 对应多少 total observation-action pairs？\nQ3: RSA 中每个 demo 取一个 observation 还是多个？同一 demo 的 temporal autocorrelation 是否 inflate RSA？\nQ4: Readout RSA 是否也呈 inverted-U？\nQ5: Untrained readout R² peak 在 L32 (0.609) 如何解释？\n\n---\n\n请逐条回应。",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每一条使用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n**Overall: 3/5 (Borderline)**\n\n### Must-Fix 问题\n\n**N1 [critical]** Cross-instruction probe 任务 trivially easy，不支撑 \"multimodal convergence\" 的强 claim\n- 10-way classification over 10 distinct instruction strings 对任何能 attend to instruction tokens 的位置都是 trivial 的\n- 论文自己在 Appendix D.1 承认 \"even incidental attention (~12%) suffices for linear classification at L1\"\n- untrained model（随机权重）在 L1 也达到 100%（Table 1）\n- 100% 分类准确率不能作为 \"multimodal convergence\" 或 \"functional specialization\" 的强证据——它只反映 instruction embeddings 本身是线性可分的\n- 真正有价值的发现是 image token 保持 chance level，但论文的对称叙事过度依赖 readout 侧的结果\n- 建议增加更困难的 probe 任务或调整 framing\n\n**N2 [critical]** RSA \"inverted-U\" 的 rise phase 效应量极小（Δρ = 0.016），且 metric-dependent\n- Trained image_mean RSA 从 L0 (0.612) 到 L12 (0.628) 的升幅仅为 0.016（2.6%）\n- Best-vs-best training effect (+0.017) 的 CI 包含 0\n- Appendix B.2 显示 linear CKA 完全逆转了 RSA ordering\n- \"non-monotonic refinement\" 是 metric-specific 的描述，而非 representation 的 intrinsic property\n- 建议明确 qualify claims 的 metric-dependence，讨论为什么 RSA 比 CKA 更 appropriate\n\n**N3 [critical]** L1 attention ablation 使用 5 demos（vs 主实验 50 demos），因果推断的可靠性存疑\n- 用 50 个 total datapoints 训练 2-layer MLP probe（~1M 参数），baseline R²=0.256 暗示严重 underfitting\n- ablation \"improvement\" 可能是 reduced effective input dimensionality 带来的 regularization effect\n- 建议用 50 demos 重跑 ablation 或添加 random ablation control\n\n### Should-Fix 问题\n\n**W1** 缺乏多重比较校正（32 层 × 3 条件 × 多 metric 的逐层比较无 FDR/Bonferroni 校正）\n**W2** Probe 的 total N 未报告，capacity 控制不充分（4096→256→7 有 ~1.05M 参数）\n**W3** Untrained L1=100% 削弱 Finding 1 的 interpretation，讨论不足\n**W4** Frozen vision encoder 是 feature 但也是 confound：\"vision encoder quality > LLM scale\" 的 implication 需要 across-encoder 实验支持\n**W5** 25 vs 24 heads 不一致需要更清晰解释\n\n### Questions\n\nQ1: Cross-instruction probe 主结果（Table 1 的 100%）用的是 linear 还是 MLP？\nQ2: Ablation 中 5 demos 对应多少 total observation-action pairs？\nQ3: RSA 中每个 demo 取一个 observation 还是多个？同一 demo 的 temporal autocorrelation 是否 inflate RSA？\nQ4: Readout RSA 是否也呈 inverted-U？\nQ5: Untrained readout R² peak 在 L32 (0.609) 如何解释？\n\n---\n\n请逐条回应。",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 245 · 2026-05-17T18:14:33.213620+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1359
}
```

</details>

---


### Assistant

_source line 246 · 2026-05-17T18:14:39.219405+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 27

## Round 27

2 recorded events


### User

_source line 247 · 2026-05-17T18:14:41.743541+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

总结：评分 **5/10**（marginally below acceptance threshold）。两个 critical 问题：(1) C1 是 causal mask 的数学必然而非经验发现，但论文将其作为首要贡献和标题基础；(2) CKA 完全反转 RSA 的 ordering，核心 claims 的 robustness 存疑。论文方法论扎实、写作清晰是优势，但缺乏 actionable design insights 且泛化性有限。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 248 · 2026-05-17T18:14:59.072200+00:00_

Reviewer 2 交叉回应已收。等待 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 28

## Round 28

2 recorded events


### User

_source line 249 · 2026-05-17T18:16:41.872959+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 交叉回应：对 Reviewer 2 审稿意见的逐条评价

---

## Must-Fix 问题

**[AGREE] R2-N1: C1 是 causal mask 的数学必然结果**

完全同意。这是一个根本性批评。OpenVLA 的 token 序列为 [image₁...imageₙ] → [instruction₁...instructionₘ] → [readout/action]。在 causal attention mask 下，位置 i 只能 attend to 位置 ≤ i。Image tokens 排在 instruction tokens 之前，因此 image tokens 在任何层的 representation 都不可能包含 instruction 信息——无论 LLM 权重是 trained、pretrained 还是 random。

这正解释了我在 R1-N1 中指出的现象：untrained model 在 L1 也达到 100% classification。不是因为 "incidental attention suffices"，而是因为 image tokens 的 instruction-invariance 根本就是 architecture-guaranteed 的。Cross-instruction probe 在 image_mean 上得 10%（chance）不是一个 empirical finding，而是在 verify 一个已知的数学性质。

我的 R1-N1 从 "probe 太简单" 角度质疑了 C1，R2-N1 从更根本的 "架构决定论" 角度指出同一问题。两者互补：
- R2-N1 说明 image-token instruction-blindness 是 trivial（causal mask）
- R1-N1 说明 readout-token 100% 也是 trivial（instruction embeddings linearly separable + any attention suffices）

合在一起，C1 整体上缺乏 empirical novelty。论文 Discussion 仅一句 "C1 likely generalizes via the causal mask" 的承认远远不够——这应该从一开始就作为已知约束讨论，而非作为 "discovery" 呈现。

补充证据：Section 3.2 明确定义 token ordering（"DinoSigLIP+Projector, the projector output, immediately before LLM processing"），Section 3.1 确认 vision encoder 是 frozen 且不接收 instruction input。这两点已经从 architecture 层面 guarantee 了 C1。

---

**[AGREE] R2-N2: RSA 与 CKA 矛盾未充分解决**

同意，与我的 R1-N2 一致。补充几点：

1. 论文 Section 3.5 给出的 RSA preference 论据是 "CKA sensitive to kernel choice" + "linear CKA has dimension mismatch"。但 RSA 同样 sensitive to distance function choice（representation 用 cosine、action 用 Euclidean，这本身就是一个 design choice）。论文的 Appendix C.6.1 验证了 action distance 的 metric invariance（cosine vs Euclidean for actions），但未验证 representation distance 的选择（如 Euclidean vs cosine for 4096-D representations）。

2. Appendix B.2 的关键数据：Linear CKA per-layer profile 是**单调递增**的（L0: 0.081 → L32: 0.098），完全没有 inverted-U。这直接否定了 "non-monotonic refinement" 作为 representation 的 intrinsic property——它仅在 RSA 下成立。

3. RDM kernel CKA 中 DINOv2 排名最低（0.241），而 RSA 中 DINOv2 排名最高（0.692）。这个完全反转使得 "vision encoder quality emerges as a key design lever"（Discussion 第3段）的结论变成 metric-contingent claim。

不过，我认为论文在 Appendix 中诚实报告了 CKA divergence（Figure 6），这比隐瞒好。问题在于正文的 claims 没有相应 qualify。

---

## Should-Fix 问题

**[AGREE] R2-W1: RSA n.s. 在 Abstract/Intro 未标注**

同意。Abstract 第6行报告 "DINOv2 providing the highest geometric foundation (ρ = 0.692)" 未加 qualifier；Introduction 第25行写 "modest geometric gain (Δ = 0.017–0.023, 3–4%)" 但未标注 LIBERO-Goal 的 Δ=+0.017 为 n.s.。这构成 selective reporting——读者必须到 Appendix Table 8 才能发现 CI includes 0。正文应在首次提到时标注统计显著性状态。

---

**[AGREE] R2-W2: L1 ablation 5 demos 可比性存疑**

完全同意，与我的 R1-N3 一致。R² baseline 从 ~0.65（50 demos, Table 3）降到 0.256（5 demos, Section 4.2）说明 probe 在 5 demos 下严重 underfitting。在这种 regime 下，zeroing attention 可能通过 reduced effective dimensionality 起到类似 regularization 的效果（fewer attended positions → lower variance representation → better generalization for small N），而非反映 genuine functional specialization。

---

**[PARTIALLY AGREE] R2-W3: 缺少关键引用**

未读 references.bib，无法完全确认。但如果 Llama-2（Touvron et al., 2023）和 Open X-Embodiment（Padalkar et al., 2023）确实未直接引用，这是应修复的遗漏。这两个是模型核心组件和训练数据的 primary sources。

---

**[AGREE] R2-W4: Architectural implications 缺乏 actionable verification**

同意，与我的 R1-W4 一致。"Vision encoder quality may matter more than LLM scale" 需要 across-encoder 实验（如替换为 CLIP-only encoder 或 weaker DINOv2 variant）来验证。当前证据仅是 "DINOv2 RSA 最高"（且 CKA 下不成立），从 correlational observation 到 design recommendation 的跳跃太大。对 CoRL 这个实践导向的社区，缺乏 actionable takeaway 是显著弱点。

---

**[AGREE] R2-W5: 单模型单 benchmark 泛化性有限**

同意，与我的观点一致。LIBERO-Goal 和 LIBERO-Spatial 同属一个 simulator、同一类 tabletop manipulation。真正的 generalization evidence 需要：(a) 不同 VLA architecture（RT-2, π₀）；(b) 不同 task domain（navigation, dexterous manipulation）；(c) 不同 backbone（non-Llama）。

---

## 小问题

**[AGREE] R2-M1: "untested assumption" 是 straw man**

部分同意。Introduction 第5行 "A central but untested assumption is that all token types within the LLM contribute uniformly to action prediction" — 在 causal mask 下，没有人会假设 image tokens 能编码 instruction 信息。但我对 R2 的判断做一个小修正：这个 "assumption" 如果理解为 "all token types contribute equally to action prediction quality"（而非 instruction encoding），则不完全是 straw man——image tokens 确实可能通过 visual information 对 action quality 有贡献。然而论文的 cross-instruction probe 测试的是 instruction encoding 而非 action contribution，所以 R2 的批评基本成立。

---

**[REBUT] R2-M2: "readout token" 与 "last_preaction" 未定义等价性**

不同意。Section 3.2 (Representation Extraction) 第(c)项明确定义："**LLM readout**, the activation at the final pre-action token position at each layer"。这里 "readout" 和 "last pre-action position" 在首次出现时就被定义为等价。后续交替使用不构成歧义。

---

**[AGREE] R2-M3: conclusion.tex 未被 main.tex \input**

确认。main.tex 的 \input 序列为：introduction → related_work → method → experiments → discussion → (bibliography) → appendix。conclusion.tex 存在但未被包含，导致编译后的论文没有独立的 Conclusion section。Discussion 最后一句 "code will be released upon acceptance" 勉强充当结尾，但格式上不规范。CoRL 2026 模板是否要求独立 Conclusion section 需确认，但多数会议论文包含该 section。

---

**[AGREE] R2-M4: 引用格式问题**

同意。Alain & Bengio 的 probe paper 虽然 2016 年上 arXiv，但正式发表于 ICLR 2017 Workshop，引用年份取决于 bib entry 如何标注。nostalgebraist (2020) 的 logit lens 是 blog post，应标注为 @misc 或 @online，且在学术论文中引用 blog post 需谨慎。

---

**[AGREE] R2-M5 & M6**: 有效的 minor issues，不影响核心判断。

---

## 对 "竞争者区分度" 的回应

**[PARTIALLY AGREE]**

R2 的核心论点是：在 causal mask 约束下，本文相对 Grant et al. (2026) 的增量有限。我同意 C1 的增量被 causal mask argument 大幅削弱。但我认为 R2 对 C2（routing shift from mid-depth to entry-exit）的评价不够：

- C2 不是 causal mask 能 predict 的——它需要实际比较 trained vs pretrained attention patterns 才能观察到。Llama-2 base 的 mid-depth routing (L9-L16, 15-22 heads) vs VLA-trained 的 entry-exit routing (L0-L1, L31) 这个 redistribution 是 genuine empirical finding。
- 然而 C2 的 practical significance 仍然有限：knowing routing shifts to L1 后如何改进 VLA design？论文未给出答案。

对 Häon et al. (CoRL 2025) 的对比：R2 正确指出该工作有 interventional evidence (activation steering)，而本文主要是 observational。本文的 L1 ablation 是唯一的 intervention，但如 R1-N3 和 R2-W2 所指出，其可靠性存疑。

---

## 综合判断

R2 的 N1（causal mask argument）是比我的 R1-N1（probe too easy）更根本的批评。两者共同指向同一结论：**C1 不是一个有意义的 empirical finding**。结合 RSA 的 metric-dependence（R2-N2, R1-N2）和 ablation 的数据规模问题（R2-W2, R1-N3），论文的三个核心贡献中只有 C2（routing redistribution）有 genuine novelty，但效应的 practical significance 未被验证。

我维持我的 Overall 3/5 (Borderline) 评分。R2 的 causal mask argument 进一步坚定了我对 C1 novelty 的怀疑，但论文的实验框架（factorial design + multi-metric）仍有 methodological value。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 250 · 2026-05-17T18:16:45.931377+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 29

## Round 29

2 recorded events


### User

_source line 251 · 2026-05-17T18:16:53.007784+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。核心判断：

- **R2-N1（causal mask）**：完全同意——比我的 "probe too easy" 批评更根本，从架构层面 trivialize 了 C1
- **R2-N2（RSA/CKA 矛盾）**：同意，与我的 R1-N2 一致
- **R2-W1–W5**：基本全部同意，多数与我的发现重叠
- **唯一 REBUT**：R2-M2（readout/last_preaction 术语），Section 3.2 已明确定义等价性

两位 reviewer 的核心共识：C1 缺乏 empirical novelty（R2 从 causal mask，R1 从 probe triviality），RSA claims 是 metric-dependent 的，ablation 数据规模问题削弱因果推断。C2（routing redistribution）是论文唯一有 genuine novelty 的贡献。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 252 · 2026-05-17T18:17:04.996186+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 30

## Round 30

6 recorded events


### User

_source line 253 · 2026-05-17T18:17:36.650297+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

### Must-Fix

**[AGREE] R1-N1: Cross-instruction probe trivially easy**
同意。与我的 N1（causal mask 使 C1 trivially true）高度一致但视角互补——R1 从 probe difficulty，我从 architecture。两者指向同一结论：C1 证据链薄弱。补充：(1) untrained L1=100% + 论文自承 "~12% attention suffices" 是论文自己提供的 trivial 证据；(2) QA probe 差异仅 3.6pp (86.3% vs 82.7%) 不足以支撑 "sole locus" 强 claim；(3) trained vs untrained trajectory 差异是唯一值得保留的信号。

**[AGREE] R1-N2: RSA inverted-U rise phase 极小且 metric-dependent**
完全同意。与我的 N2 一致。补充：R1 的 Δρ=0.016 (rise) 和我的 Δ=0.017 (training effect) 共同表明 inverted-U 的 rise phase 在 noise floor。Linear CKA per-layer 单调递增无 inverted-U（Appendix D.1 line 25-26）。RDM kernel CKA 中 DINOv2 排名最低（0.241），进一步削弱 "DINOv2 geometric ceiling" claim 的 robustness。

**[AGREE] R1-N3: L1 ablation 5 demos 不可靠**
同意核心关切。补充：论文用 L8/L13 null result 排除 artifact（Section 4.3 line 77-78），但如果 L8/L13 本身不受 L1 attention 影响（有独立 attention patterns），null result 不能排除 L1 level confound。支持 R1 的 random ablation control 建议。

### Should-Fix

**[AGREE] R1-W1**: 多重比较校正缺失是合理关切。Bootstrap CIs 为 per-comparison，无 family-wise 校正。
**[AGREE] R1-W2**: Total N 未报告。同意 capacity 控制不充分。
**[AGREE] R1-W3**: 强烈同意。untrained L1=100% 直接削弱 Finding 1 的 trained-side interpretation。
**[AGREE] R1-W4**: 同意。"encoder quality > LLM scale" 需要 across-encoder 实验，否则只是 restatement。与我的 W4 一致。

**[REBUT] R1-W5**: 部分反驳。论文在 3 处解释了 25/24 差异（Section 4.3 line 68, line 76, Table 7 caption），来源是 dedicated vs. bulk extraction 的 threshold boundary。Appendix Table 8 提供了 30%-70% threshold sensitivity 验证。但同意解释分散，建议集中说明。

### Questions

Q1: 主结果用 linear classifier（Method 3.3），MLP 仅作 corroboration。Linear 就达 100% 进一步支持 R1-N1。
Q2: 未明确报告。估计 50 demos × 50-200 steps/demo × 10 tasks ≈ 2,500-10,000 pairs for 5-demo ablation。
Q3: 好问题。论文未说明 temporal autocorrelation 处理和 bootstrap 是否 block by demo。可能 inflate RSA ρ。
Q4: Table 3 显示 readout RSA peak L12 (0.643)，但 Figure 3 只画了 image_mean。Spatial appendix 暗示 readout 也 non-monotonic。建议补充 readout 曲线。
Q5: 推测 L32 layer norm 对 random projections 的 normalization 可能产生 probe-friendly scaling，但论文未讨论。

### 综合评估

R1 和 R2 独立发现高度一致的核心问题：C1 trivial（R1 从 probe difficulty，R2 从 causal mask）；C3 metric-dependent（两人都指出 CKA 矛盾）；ablation 数据量不足。建议将这三个问题合并为 rebuttal 必须回应的核心关切。论文的实验设计和写作质量是真正的优势。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 254 · 2026-05-17T18:19:28.204262+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "vla-ssd",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-3 历史 issues（全部 resolved）\n  # ============================================================\n  - id: R1-N1-old\n    summary: \"Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识。需增加 Llama-2 base checkpoint 作为中间对照\"\n      - round: 2\n        reviewers: [1, 2, 3]\n        note: \"PARTIALLY_RESOLVED: acknowledge confound 但无数据\"\n    action_items:\n      - round: 1\n        action: \"增加 Llama-2 base checkpoint 对照实验\"\n        assigned_to: research\n        status: done\n      - round: 2\n        action: \"Section 标题改为观察性；Abstract 弱化 causal attribution\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"B版本完整整合三条件数据：untrained 0/32, Llama-2 base 9/32, trained 25/32 heads。§4.3 以三条件梯度为核心证据，Table 2 + Figure 4 呈现完整 32 层 profile。\"\n    resolution_round: 3\n\n  - id: R1-N2-old\n    summary: \"单一模型(OpenVLA-7B) + 单一 benchmark family(LIBERO)，Title/Abstract 使用复数 'VLAs' 构成 overclaim\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识\"\n      - round: 2\n        reviewers: [1, 2, 3]\n        note: \"PARTIALLY_RESOLVED: Abstract 限定但 Title 仍复数\"\n    action_items:\n      - round: 2\n        action: \"Title 改为单数\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"B版本 Title = 'Token-Level Functional Specialization in a Vision-Language-Action Model'（单数）。\"\n    resolution_round: 3\n\n  - id: R1-N4-old\n    summary: \"Design implications 完全基于 correlational evidence\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本 Abstract 使用 hedge 语气。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识\"\n    action_items: []\n\n  - id: R1-N3-old\n    summary: \"RSA best-vs-best selection bias\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本 same-layer comparison 为 primary evidence。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"2:1 critical\"\n    action_items: []\n\n  - id: R2-N1-old\n    summary: \"Neo et al. (ICLR 2025) 未引用\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本 Related Work 已引用 Neo et al.\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R2 critical\"\n    action_items: []\n\n  - id: R2-W1-old\n    summary: \"Related Work 引用覆盖度不足\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本引用数量达标。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"21 citations 严重不足\"\n    action_items: []\n\n  - id: R1-W1-old\n    summary: \"'Instruction-blind' claim 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本补充 MLP probe 双重验证。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识\"\n    action_items: []\n\n  - id: R1-W2-old\n    summary: \"CKA 反转 RSA 排序处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Method 新增 'Why RSA over CKA' 段落。\"\n    resolution_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识\"\n    action_items: []\n\n  - id: R3-N1-old\n    summary: \"Limitations 格式不满足 CoRL 2026 要求\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"改为 \\\\subsection{Limitations}。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R3 标为 critical\"\n    action_items: []\n\n  - id: R3-N2-old\n    summary: \"正文解释性 em-dash 是 AI 写作标志\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"零残留。\"\n    resolution_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"至少 8 处\"\n    action_items: []\n\n  - id: R3-W5-old\n    summary: \"无 code/data 释放声明\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本 Conclusion 加声明。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 3]\n        note: \"CoRL 鼓励 reproducibility\"\n    action_items: []\n\n  # ============================================================\n  # Round 4 新发现\n  # ============================================================\n  - id: R4-N1\n    summary: \"C1（token-level functional specialization）是 causal mask 的数学必然结果 + probe 任务 trivially easy，不构成 empirical finding\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"全票共识。R2 从 causal mask 架构决定论论证，R1 从 probe difficulty 论证，两者互补指向同一结论：C1 整体缺乏 empirical novelty。untrained L1=100% 是双方共同引用的关键证据。交叉回应中 R1 完全同意 R2 的 causal mask argument 更根本。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-N2\n    summary: \"RSA inverted-U 的 rise phase 效应量极小（Δρ=0.016）且 metric-dependent：CKA 完全反转 RSA ordering 和 per-layer profile\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"全票共识。Linear CKA per-layer 单调递增无 inverted-U；DINOv2 在 CKA 下排名最低（RSA 下最高）。'non-monotonic refinement' 和 'DINOv2 geometric ceiling' 均为 metric-contingent claims。Method §3.5 的 RSA preference justification 不充分。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-N3\n    summary: \"L1 attention ablation 使用 5 demos（vs 主实验 50 demos），R² baseline 0.256 vs ~0.65，因果推断可靠性不足\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"全票共识。5 demos 下 probe 严重 underfitting，ablation improvement 可能是 reduced dimensionality 的 regularization effect。缺少 random ablation control。R2 补充：L8/L13 null result 不能排除 L1-level confound。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W1\n    summary: \"RSA best-vs-best training effect n.s.（Δ=+0.017, CI includes 0）在 Abstract/Intro 未标注显著性状态\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"全票共识。读者须到 Appendix Table 8 才知 CI includes 0，构成 selective reporting。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W2\n    summary: \"缺乏多重比较校正（32 层 × 3 条件 × 多 metric 无 FDR/Bonferroni）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 交叉回应 AGREE。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W3\n    summary: \"Probe total N 未报告，MLP probe capacity 控制不充分（~1.05M params vs unknown N）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 AGREE。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W4\n    summary: \"Frozen encoder confound：'vision encoder quality > LLM scale' 的 architectural implication 需要 across-encoder 实验\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"全票共识。当前结论是 RSA-specific 且仅 within fixed encoder，从 correlational observation 到 design recommendation 跳跃太大。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W5\n    summary: \"单模型（OpenVLA-7B）+ 单 benchmark family（LIBERO），泛化性有限\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"全票共识。LIBERO-Goal + LIBERO-Spatial 同属一个 simulator。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W6\n    summary: \"缺少 Llama-2 和 Open X-Embodiment 关键引用\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [2]\n        note: \"R2 提出，R1 partially agree（未验证 bib 但认为合理）。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    summary: \"Introduction 'untested assumption' 是 straw man（causal mask 下无人会假设 image tokens 编码 instruction）\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 partially agree（如果理解为 action contribution 而非 instruction encoding 则不完全是 straw man，但论文测试的是后者）。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-I1\n    summary: \"conclusion.tex 未被 main.tex \\\\input，论文无独立 Conclusion section\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [2]\n        note: \"R2 提出，R1 AGREE。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-I2\n    summary: \"引用格式问题：alain2017 年份存疑、nostalgebraist2020 blog post 格式不规范、部分 preprint 应更新\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 AGREE。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-I3\n    summary: \"25 vs 24 heads 数值不一致的解释分散在正文和 appendix 多处\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R1 提出 should-fix，R2 partially rebut（解释存在但分散）。降级为 info。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "vla-ssd",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-3 历史 issues（全部 resolved）\n  # ============================================================\n  - id: R1-N1-old\n    summary: \"Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识。需增加 Llama-2 base checkpoint 作为中间对照\"\n      - round: 2\n        reviewers: [1, 2, 3]\n        note: \"PARTIALLY_RESOLVED: acknowledge confound 但无数据\"\n    action_items:\n      - round: 1\n        action: \"增加 Llama-2 base checkpoint 对照实验\"\n        assigned_to: research\n        status: done\n      - round: 2\n        action: \"Section 标题改为观察性；Abstract 弱化 causal attribution\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"B版本完整整合三条件数据：untrained 0/32, Llama-2 base 9/32, trained 25/32 heads。§4.3 以三条件梯度为核心证据，Table 2 + Figure 4 呈现完整 32 层 profile。\"\n    resolution_round: 3\n\n  - id: R1-N2-old\n    summary: \"单一模型(OpenVLA-7B) + 单一 benchmark family(LIBERO)，Title/Abstract 使用复数 'VLAs' 构成 overclaim\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识\"\n      - round: 2\n        reviewers: [1, 2, 3]\n        note: \"PARTIALLY_RESOLVED: Abstract 限定但 Title 仍复数\"\n    action_items:\n      - round: 2\n        action: \"Title 改为单数\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"B版本 Title = 'Token-Level Functional Specialization in a Vision-Language-Action Model'（单数）。\"\n    resolution_round: 3\n\n  - id: R1-N4-old\n    summary: \"Design implications 完全基于 correlational evidence\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本 Abstract 使用 hedge 语气。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识\"\n    action_items: []\n\n  - id: R1-N3-old\n    summary: \"RSA best-vs-best selection bias\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本 same-layer comparison 为 primary evidence。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"2:1 critical\"\n    action_items: []\n\n  - id: R2-N1-old\n    summary: \"Neo et al. (ICLR 2025) 未引用\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本 Related Work 已引用 Neo et al.\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R2 critical\"\n    action_items: []\n\n  - id: R2-W1-old\n    summary: \"Related Work 引用覆盖度不足\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本引用数量达标。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"21 citations 严重不足\"\n    action_items: []\n\n  - id: R1-W1-old\n    summary: \"'Instruction-blind' claim 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本补充 MLP probe 双重验证。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识\"\n    action_items: []\n\n  - id: R1-W2-old\n    summary: \"CKA 反转 RSA 排序处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Method 新增 'Why RSA over CKA' 段落。\"\n    resolution_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识\"\n    action_items: []\n\n  - id: R3-N1-old\n    summary: \"Limitations 格式不满足 CoRL 2026 要求\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"改为 \\\\subsection{Limitations}。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R3 标为 critical\"\n    action_items: []\n\n  - id: R3-N2-old\n    summary: \"正文解释性 em-dash 是 AI 写作标志\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"零残留。\"\n    resolution_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"至少 8 处\"\n    action_items: []\n\n  - id: R3-W5-old\n    summary: \"无 code/data 释放声明\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本 Conclusion 加声明。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 3]\n        note: \"CoRL 鼓励 reproducibility\"\n    action_items: []\n\n  # ============================================================\n  # Round 4 新发现\n  # ============================================================\n  - id: R4-N1\n    summary: \"C1（token-level functional specialization）是 causal mask 的数学必然结果 + probe 任务 trivially easy，不构成 empirical finding\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"全票共识。R2 从 causal mask 架构决定论论证，R1 从 probe difficulty 论证，两者互补指向同一结论：C1 整体缺乏 empirical novelty。untrained L1=100% 是双方共同引用的关键证据。交叉回应中 R1 完全同意 R2 的 causal mask argument 更根本。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-N2\n    summary: \"RSA inverted-U 的 rise phase 效应量极小（Δρ=0.016）且 metric-dependent：CKA 完全反转 RSA ordering 和 per-layer profile\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"全票共识。Linear CKA per-layer 单调递增无 inverted-U；DINOv2 在 CKA 下排名最低（RSA 下最高）。'non-monotonic refinement' 和 'DINOv2 geometric ceiling' 均为 metric-contingent claims。Method §3.5 的 RSA preference justification 不充分。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-N3\n    summary: \"L1 attention ablation 使用 5 demos（vs 主实验 50 demos），R² baseline 0.256 vs ~0.65，因果推断可靠性不足\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"全票共识。5 demos 下 probe 严重 underfitting，ablation improvement 可能是 reduced dimensionality 的 regularization effect。缺少 random ablation control。R2 补充：L8/L13 null result 不能排除 L1-level confound。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W1\n    summary: \"RSA best-vs-best training effect n.s.（Δ=+0.017, CI includes 0）在 Abstract/Intro 未标注显著性状态\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"全票共识。读者须到 Appendix Table 8 才知 CI includes 0，构成 selective reporting。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W2\n    summary: \"缺乏多重比较校正（32 层 × 3 条件 × 多 metric 无 FDR/Bonferroni）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 交叉回应 AGREE。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W3\n    summary: \"Probe total N 未报告，MLP probe capacity 控制不充分（~1.05M params vs unknown N）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 AGREE。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W4\n    summary: \"Frozen encoder confound：'vision encoder quality > LLM scale' 的 architectural implication 需要 across-encoder 实验\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"全票共识。当前结论是 RSA-specific 且仅 within fixed encoder，从 correlational observation 到 design recommendation 跳跃太大。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W5\n    summary: \"单模型（OpenVLA-7B）+ 单 benchmark family（LIBERO），泛化性有限\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"全票共识。LIBERO-Goal + LIBERO-Spatial 同属一个 simulator。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W6\n    summary: \"缺少 Llama-2 和 Open X-Embodiment 关键引用\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [2]\n        note: \"R2 提出，R1 partially agree（未验证 bib 但认为合理）。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    summary: \"Introduction 'untested assumption' 是 straw man（causal mask 下无人会假设 image tokens 编码 instruction）\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 partially agree（如果理解为 action contribution 而非 instruction encoding 则不完全是 straw man，但论文测试的是后者）。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-I1\n    summary: \"conclusion.tex 未被 main.tex \\\\input，论文无独立 Conclusion section\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [2]\n        note: \"R2 提出，R1 AGREE。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-I2\n    summary: \"引用格式问题：alain2017 年份存疑、nostalgebraist2020 blog post 格式不规范、部分 preprint 应更新\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 AGREE。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-I3\n    summary: \"25 vs 24 heads 数值不一致的解释分散在正文和 appendix 多处\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R1 提出 should-fix，R2 partially rebut（解释存在但分散）。降级为 info。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 255 · 2026-05-17T18:19:28.306131+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml\", \"bytes\": 10692}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 256 · 2026-05-17T18:21:34.461277+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "vla-ssd",
  "report": "# 审稿报告：Vision Encodes, Language Routes — Token-Level Functional Specialization in a Vision-Language-Action Model\n\n**目标 Venue**: CoRL 2026 | **截止日期**: Paper 2026-05-28 EOD\n**审稿轮次**: Round 4（B 版本全新审稿）\n**Reviewer 配置**: 2 人（R1 方法/实验严谨性，R2 新颖性/影响力 + 写作/格式）\n\n---\n\n## Summary\n\n本文对 OpenVLA-7B 在 LIBERO 上进行 token 级别表征分析，通过 cross-instruction probes、attention 分析、RSA 和 MLP probes 四种方法，比较 trained/pretrained/untrained 三个条件。主要 claims：(1) image tokens 不编码 instruction 信息（instruction-blind），readout token 是唯一的多模态汇聚点；(2) VLA fine-tuning 将 instruction routing 从中层转移到 entry-exit 模式；(3) LLM 对 vision encoder 输出进行非单调变换（inverted-U RSA profile）。\n\n---\n\n## Strengths\n\n- **S1 [全票]**: 系统化的 2×2 factorial design（trained/untrained × instruction presence）+ 三条件对比（trained/pretrained/untrained）有效 disentangle 各因素贡献，是分析 VLA 的优秀实验范式\n- **S2 [全票]**: 四种互补分析方法（probe + attention + RSA + MLP）从不同角度验证同一问题；CKA 作为 supplementary metric 在 appendix 诚实报告，包括与 RSA 的矛盾\n- **S3 [全票]**: 充分的 robustness analysis（distance metric invariance, per-DOF, permutation test, seed sensitivity, demo subsampling, cross-benchmark validation on LIBERO-Spatial）\n- **S4 [R1]**: 诚实报告 negative/null results（RSA best-vs-best Δ=+0.017, CI includes 0 标为 n.s.；CKA ordering 矛盾正面讨论）\n- **S5 [R2]**: 写作质量良好，无 AI 写作痕迹，叙事连贯\n- **S6 [R2]**: L1 attention ablation 提供了少有的 interventional evidence（尽管数据规模存在问题）\n\n---\n\n## Weaknesses\n\n### Must-Fix（3 个 critical，全票共识）\n\n**N1 [critical, 全票共识] C1 不构成 empirical finding — causal mask 的数学必然 + probe 任务 trivially easy**\n\nOpenVLA 的 token 序列为 [image] → [instruction] → [readout/action]。Causal attention mask 下，位置 i 的表征仅依赖位置 ≤ i。Image tokens 先于 instruction tokens，因此 image tokens 在任何层都无法 attend to instruction tokens。这是架构决定的数学性质，非 empirical finding。此外，frozen vision encoder 不接收 instruction input，instruction invariance 同样 trivially expected。\n\nReadout token 侧同样有问题：10-way classification over 10 distinct instruction strings 对任何能 attend to instruction tokens 的位置都是 trivial 的。论文自己承认 \"even incidental attention (~12%) suffices for linear classification at L1\"（Appendix D.1）。Untrained model（随机权重）在 L1 也达到 100%（Table 1），进一步证实 trivial nature。100% 准确率反映 instruction embeddings 的线性可分性（tokenizer 的性质），非 \"multimodal convergence\" 的证据。\n\nC1 是论文三大贡献之首、标题的核心基础。Discussion 仅一句话承认 \"C1 likely generalizes via the causal mask\"，远远不够。如果 C1 的两侧（image-blind + readout-hub）都是 trivial，论文的核心叙事需要根本性重构。\n\nR1 视角（probe difficulty）和 R2 视角（causal mask）互补，交叉回应中 R1 完全同意 R2 的 causal mask argument 更根本。\n\n**N2 [critical, 全票共识] RSA inverted-U 效应量极小且 metric-dependent，CKA 完全反转核心结论**\n\n(a) Rise phase 极小：Trained image_mean RSA 从 L0 (0.612) 到 L12 (0.628) 升幅仅 Δρ=0.016（2.6%），L0→L12 的 CI 未报告。Best-vs-best training effect (+0.017) 的 CI 包含 0（n.s.）。\n\n(b) Metric-dependent：Appendix B.2 显示 linear CKA 完全反转 RSA ordering（untrained > trained > DINOv2），per-layer profile 呈单调递增（无 inverted-U）。RDM kernel CKA 中 DINOv2 排名最低（0.241），而 RSA 中 DINOv2 排名最高（0.692）——完全反转。\n\n(c) 核心 claims 受影响：\"non-monotonic refinement of vision encoder output\" 仅在 RSA 下成立；\"DINOv2 provides the highest geometric foundation\" 在 CKA 下不成立；\"vision encoder quality emerges as a key design lever\" 是 metric-contingent claim。\n\nMethod §3.5 的 RSA preference justification（\"CKA sensitive to kernel choice\"）不充分——RSA 同样 sensitive to distance function choice（representation 用 cosine、action 用 Euclidean）。仅验证了 action distance 的 metric invariance（Appendix C.6.1），未验证 representation distance 的选择。\n\n**N3 [critical, 全票共识] L1 attention ablation 使用 5 demos，因果推断可靠性不足**\n\nAblation 使用 5 demos per task（~50-500 total datapoints），而主实验 Table 3 使用 50 demos per task。R² baseline 从 ~0.65 降到 0.256，表明 probe 严重 underfitting。在此 regime 下：\n- Zeroing attention 可能通过 reduced effective dimensionality 起到 regularization effect（fewer attended positions → lower variance → better generalization for small N）\n- 这是论文中唯一的 causal intervention；如果不可靠，全文仅有 correlational evidence\n- 缺少 random ablation control（随机 zero 同等数量的 non-instruction-dominant heads）\n- R2 补充：L8/L13 null result 不能排除 L1-level confound（L8/L13 有独立 attention patterns）\n\n---\n\n### Should-Fix（7 个 warning）\n\n**W1 [warning, 全票共识]** RSA best-vs-best training effect（Δ=+0.017, CI includes 0, n.s.）在 Abstract（L7 \"modest geometric gain\"）和 Introduction（L25）中未标注 n.s. 状态。读者须到 Appendix Table 8 才发现 CI includes 0，构成 selective reporting。\n\n**W2 [warning, 全票共识]** 缺乏多重比较校正。32 层 × 3 条件 × 多 metric 的逐层比较无 FDR/Bonferroni 校正。至少对 key claims（inverted-U peak significance、per-layer training effects）应报告 adjusted p-values。\n\n**W3 [warning, 全票共识]** Probe total N 从未明确报告。50 demos per task × 10 tasks = 500 demos，每 demo 多少 timesteps 未知。MLP probe（4096→256→7）有 ~1.05M 参数，N/params 比率影响 overfitting 风险评估。应报告 exact N 并讨论 capacity 控制。\n\n**W4 [warning, 全票共识]** Frozen vision encoder 是 confound。\"Vision encoder quality may matter more than LLM scale\" 需要 across-encoder 实验（如 CLIP-only encoder 或 weaker DINOv2 variant）。当前仅在单一 frozen encoder 内分析，从 correlational observation 到 design recommendation 跳跃过大。\n\n**W5 [warning, 全票共识]** 单模型（OpenVLA-7B）+ 单 benchmark family（LIBERO-Goal/Spatial，同一 simulator）。真正的 generalization evidence 需要不同 VLA architecture（RT-2, π₀）、不同 task domain（navigation, dexterous manipulation）、不同 backbone（non-Llama）。\n\n**W6 [warning, R2 提出, R1 partially agree]** 缺少 Llama-2（Touvron et al., 2023）和 Open X-Embodiment（Padalkar et al., 2023）的直接引用。这两个是模型核心组件和训练数据的 primary sources。\n\n**W7 [warning, R2 提出, R1 partially agree]** Introduction 第5行 \"A central but untested assumption is that all token types within the LLM contribute uniformly to action prediction\" 在 causal mask 约束下接近 straw man——没有人会假设 causal mask 前的 image tokens 能编码后面的 instruction 信息。需重新措辞。\n\n---\n\n## Reviewer Consensus\n\n以下为两位 Reviewer 达成共识的核心判断：\n\n1. **[AGREE, 全票] C1 缺乏 empirical novelty**：R2 从 causal mask（数学必然），R1 从 probe difficulty（trivially easy），交叉回应后 R1 完全同意 R2 的论证更根本\n2. **[AGREE, 全票] C3 的 inverted-U 是 metric-specific**：RSA 下成立，CKA 下消失或反转，\"non-monotonic refinement\" 不是 robust finding\n3. **[AGREE, 全票] Ablation 数据规模问题**：5 demos 下 R² baseline 仅 0.256，因果推断受损\n4. **[AGREE, 全票] C2（routing redistribution）是论文唯一有 genuine novelty 的贡献**：三条件 attention profile 的 mid-depth → entry-exit shift 是 genuine empirical finding，但 practical significance 未验证\n5. **[AGREE, 全票] 实验框架（factorial design + multi-metric）具有方法论价值**\n\n---\n\n## Reviewer Divergence\n\n仅一处小分歧，已在交叉回应中解决：\n\n- **R2-M2（readout/last_preaction 术语）**：R2 认为交替使用未定义等价性，R1 反驳指出 Section 3.2(c) 已明确定义。R2 未在交叉回应中继续争论。结论：非问题。\n\n---\n\n## Questions to Authors\n\n1. **Token ordering**：如果 image tokens 在 causal mask 中先于 instruction tokens，C1 的 image-token instruction-blindness 是否是 architecture-guaranteed 而非 empirical finding？如果是，论文如何重新定位 C1 的贡献？\n2. **Probe difficulty**：是否考虑过更难的 probe 任务（如语义相近指令区分、fine-grained instruction attribute prediction）来验证 readout token 的 \"multimodal convergence\" 超越 trivial linear separability？\n3. **RSA vs CKA**：Linear CKA per-layer profile 单调递增（Appendix B.2），DINOv2 在 RDM kernel CKA 中排名最低。请给出 principled argument 解释为何 RSA 应被优先信任，或 qualify C3 claims 为 metric-dependent。\n4. **Ablation N**：5 demos per task 对应多少 total observation-action pairs？R² baseline 0.256 是否暗示 probe underfitting？是否可用 50 demos 重跑？\n5. **RSA temporal autocorrelation**：同一 demo 内的多个 observation 是否引入 temporal autocorrelation？Bootstrap 是否 block by demo？\n6. **Readout RSA profile**：Table 3 显示 readout RSA peak 在 L12 (0.643)，但 Figure 3 仅画 image_mean。Readout 是否也呈 inverted-U？\n\n---\n\n## Missing References\n\n- Touvron et al. (2023) — Llama 2: Open Foundation and Fine-Tuned Chat Models（模型核心组件）\n- Padalkar et al. (2023) — Open X-Embodiment（训练数据 primary source）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目配置中 external_review 未启用）。\n\n---\n\n## Overall Assessment\n\n**Overall Score: Weak Reject**\n**Confidence: High (4/5)**\n\n论文的实验框架（factorial design + multi-metric analysis）具有方法论价值，写作质量高，robustness analysis 充分。但三个核心贡献中：\n\n- **C1**（token-level specialization）：causal mask 的数学必然 + probe trivially easy → 不构成 meaningful empirical finding\n- **C2**（front-loaded routing）：唯一有 genuine novelty 的贡献，三条件 attention profile 的 entry-exit vs mid-depth 对比是 real finding，但 practical significance 未验证\n- **C3**（inverted-U refinement）：RSA-specific，CKA 下消失/反转，效应量极小（Δρ=0.016），不是 robust finding\n\n仅凭 C2 一个 finding 不足以支撑 CoRL 2026 的投稿。L1 ablation 的 5-demo 数据规模问题进一步削弱因果推断力度。\n\n**如果作者能在 rebuttal 中**：(1) 论证 token ordering 使 C1 non-trivial 或根本性重构 C1 定位；(2) 对 inverted-U rise phase 提供 CI 并 qualify metric-dependence；(3) 用 50 demos 重跑 ablation + random control，评分可能上调至 borderline accept。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- L1-2: 清晰概括了方法\n- L4-5: \"strict token-level functional specialization: image tokens are instruction-blind\" — 需要 qualify 这是 causal mask 的结构性约束\n- L6: \"self-supervised DINOv2 providing the highest geometric foundation\" — 需加 \"under RSA\" qualifier（CKA 下不成立）\n- L7: \"modest geometric gain (Δ = 0.017)\" — 未标注 n.s.\n\n### Introduction\n- L5: \"untested assumption\" 接近 straw man，需重新措辞\n- L19-22: C2 的描述是论文最有价值的贡献，建议提升其在叙事中的权重\n- L27: Contributions 列表中 (i) 应降权或重新定位\n\n### Method\n- §3.3: \"linear classifier (10-way)\" 与 §4.2 \"both linear and MLP probes\" 的关系需在方法中提前说明\n- §3.5: \"Why RSA over CKA\" justification 需加强——当前论据可被对称地反驳\n\n### Experiments\n- §4.2 Table 1: Untrained L1=100% 的 interpretation 需要更多讨论（不仅是 \"incidental\"）\n- §4.2 L76: 5-demo ablation 的方法细节（N, probe architecture, training procedure）应单独说明而非嵌入结果段落\n- §4.3 Figure 3: 应增加 readout token 的 per-layer RSA 曲线\n- §4.3: L0→L12 升幅的 bootstrap CI 需报告\n\n### Discussion\n- \"C1 likely generalizes via the causal mask; C2 may be Llama-2-specific\" — 这种无证据猜测不应出现，要么提供证据要么删除\n- Limitations section 较简短，应扩展讨论 metric-dependence（RSA vs CKA divergence）\n\n### Appendix\n- B.2: CKA divergence 的讨论质量好，但应在正文有 pointer 和 qualification\n- Table 9 vs Table 2 的 25/24 差异解释应集中在一处\n\n### Format\n- conclusion.tex 未被 main.tex \\input\n- references.bib 缺少 Llama-2 和 Open X-Embodiment\n- 部分 R² 精度不统一（2位 vs 3位）\n",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "weak reject",
  "review_chat_id": "oc_554a5023cde4d603635cf97e6ab8151a"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "vla-ssd",
    "report": "# 审稿报告：Vision Encodes, Language Routes — Token-Level Functional Specialization in a Vision-Language-Action Model\n\n**目标 Venue**: CoRL 2026 | **截止日期**: Paper 2026-05-28 EOD\n**审稿轮次**: Round 4（B 版本全新审稿）\n**Reviewer 配置**: 2 人（R1 方法/实验严谨性，R2 新颖性/影响力 + 写作/格式）\n\n---\n\n## Summary\n\n本文对 OpenVLA-7B 在 LIBERO 上进行 token 级别表征分析，通过 cross-instruction probes、attention 分析、RSA 和 MLP probes 四种方法，比较 trained/pretrained/untrained 三个条件。主要 claims：(1) image tokens 不编码 instruction 信息（instruction-blind），readout token 是唯一的多模态汇聚点；(2) VLA fine-tuning 将 instruction routing 从中层转移到 entry-exit 模式；(3) LLM 对 vision encoder 输出进行非单调变换（inverted-U RSA profile）。\n\n---\n\n## Strengths\n\n- **S1 [全票]**: 系统化的 2×2 factorial design（trained/untrained × instruction presence）+ 三条件对比（trained/pretrained/untrained）有效 disentangle 各因素贡献，是分析 VLA 的优秀实验范式\n- **S2 [全票]**: 四种互补分析方法（probe + attention + RSA + MLP）从不同角度验证同一问题；CKA 作为 supplementary metric 在 appendix 诚实报告，包括与 RSA 的矛盾\n- **S3 [全票]**: 充分的 robustness analysis（distance metric invariance, per-DOF, permutation test, seed sensitivity, demo subsampling, cross-benchmark validation on LIBERO-Spatial）\n- **S4 [R1]**: 诚实报告 negative/null results（RSA best-vs-best Δ=+0.017, CI includes 0 标为 n.s.；CKA ordering 矛盾正面讨论）\n- **S5 [R2]**: 写作质量良好，无 AI 写作痕迹，叙事连贯\n- **S6 [R2]**: L1 attention ablation 提供了少有的 interventional evidence（尽管数据规模存在问题）\n\n---\n\n## Weaknesses\n\n### Must-Fix（3 个 critical，全票共识）\n\n**N1 [critical, 全票共识] C1 不构成 empirical finding — causal mask 的数学必然 + probe 任务 trivially easy**\n\nOpenVLA 的 token 序列为 [image] → [instruction] → [readout/action]。Causal attention mask 下，位置 i 的表征仅依赖位置 ≤ i。Image tokens 先于 instruction tokens，因此 image tokens 在任何层都无法 attend to instruction tokens。这是架构决定的数学性质，非 empirical finding。此外，frozen vision encoder 不接收 instruction input，instruction invariance 同样 trivially expected。\n\nReadout token 侧同样有问题：10-way classification over 10 distinct instruction strings 对任何能 attend to instruction tokens 的位置都是 trivial 的。论文自己承认 \"even incidental attention (~12%) suffices for linear classification at L1\"（Appendix D.1）。Untrained model（随机权重）在 L1 也达到 100%（Table 1），进一步证实 trivial nature。100% 准确率反映 instruction embeddings 的线性可分性（tokenizer 的性质），非 \"multimodal convergence\" 的证据。\n\nC1 是论文三大贡献之首、标题的核心基础。Discussion 仅一句话承认 \"C1 likely generalizes via the causal mask\"，远远不够。如果 C1 的两侧（image-blind + readout-hub）都是 trivial，论文的核心叙事需要根本性重构。\n\nR1 视角（probe difficulty）和 R2 视角（causal mask）互补，交叉回应中 R1 完全同意 R2 的 causal mask argument 更根本。\n\n**N2 [critical, 全票共识] RSA inverted-U 效应量极小且 metric-dependent，CKA 完全反转核心结论**\n\n(a) Rise phase 极小：Trained image_mean RSA 从 L0 (0.612) 到 L12 (0.628) 升幅仅 Δρ=0.016（2.6%），L0→L12 的 CI 未报告。Best-vs-best training effect (+0.017) 的 CI 包含 0（n.s.）。\n\n(b) Metric-dependent：Appendix B.2 显示 linear CKA 完全反转 RSA ordering（untrained > trained > DINOv2），per-layer profile 呈单调递增（无 inverted-U）。RDM kernel CKA 中 DINOv2 排名最低（0.241），而 RSA 中 DINOv2 排名最高（0.692）——完全反转。\n\n(c) 核心 claims 受影响：\"non-monotonic refinement of vision encoder output\" 仅在 RSA 下成立；\"DINOv2 provides the highest geometric foundation\" 在 CKA 下不成立；\"vision encoder quality emerges as a key design lever\" 是 metric-contingent claim。\n\nMethod §3.5 的 RSA preference justification（\"CKA sensitive to kernel choice\"）不充分——RSA 同样 sensitive to distance function choice（representation 用 cosine、action 用 Euclidean）。仅验证了 action distance 的 metric invariance（Appendix C.6.1），未验证 representation distance 的选择。\n\n**N3 [critical, 全票共识] L1 attention ablation 使用 5 demos，因果推断可靠性不足**\n\nAblation 使用 5 demos per task（~50-500 total datapoints），而主实验 Table 3 使用 50 demos per task。R² baseline 从 ~0.65 降到 0.256，表明 probe 严重 underfitting。在此 regime 下：\n- Zeroing attention 可能通过 reduced effective dimensionality 起到 regularization effect（fewer attended positions → lower variance → better generalization for small N）\n- 这是论文中唯一的 causal intervention；如果不可靠，全文仅有 correlational evidence\n- 缺少 random ablation control（随机 zero 同等数量的 non-instruction-dominant heads）\n- R2 补充：L8/L13 null result 不能排除 L1-level confound（L8/L13 有独立 attention patterns）\n\n---\n\n### Should-Fix（7 个 warning）\n\n**W1 [warning, 全票共识]** RSA best-vs-best training effect（Δ=+0.017, CI includes 0, n.s.）在 Abstract（L7 \"modest geometric gain\"）和 Introduction（L25）中未标注 n.s. 状态。读者须到 Appendix Table 8 才发现 CI includes 0，构成 selective reporting。\n\n**W2 [warning, 全票共识]** 缺乏多重比较校正。32 层 × 3 条件 × 多 metric 的逐层比较无 FDR/Bonferroni 校正。至少对 key claims（inverted-U peak significance、per-layer training effects）应报告 adjusted p-values。\n\n**W3 [warning, 全票共识]** Probe total N 从未明确报告。50 demos per task × 10 tasks = 500 demos，每 demo 多少 timesteps 未知。MLP probe（4096→256→7）有 ~1.05M 参数，N/params 比率影响 overfitting 风险评估。应报告 exact N 并讨论 capacity 控制。\n\n**W4 [warning, 全票共识]** Frozen vision encoder 是 confound。\"Vision encoder quality may matter more than LLM scale\" 需要 across-encoder 实验（如 CLIP-only encoder 或 weaker DINOv2 variant）。当前仅在单一 frozen encoder 内分析，从 correlational observation 到 design recommendation 跳跃过大。\n\n**W5 [warning, 全票共识]** 单模型（OpenVLA-7B）+ 单 benchmark family（LIBERO-Goal/Spatial，同一 simulator）。真正的 generalization evidence 需要不同 VLA architecture（RT-2, π₀）、不同 task domain（navigation, dexterous manipulation）、不同 backbone（non-Llama）。\n\n**W6 [warning, R2 提出, R1 partially agree]** 缺少 Llama-2（Touvron et al., 2023）和 Open X-Embodiment（Padalkar et al., 2023）的直接引用。这两个是模型核心组件和训练数据的 primary sources。\n\n**W7 [warning, R2 提出, R1 partially agree]** Introduction 第5行 \"A central but untested assumption is that all token types within the LLM contribute uniformly to action prediction\" 在 causal mask 约束下接近 straw man——没有人会假设 causal mask 前的 image tokens 能编码后面的 instruction 信息。需重新措辞。\n\n---\n\n## Reviewer Consensus\n\n以下为两位 Reviewer 达成共识的核心判断：\n\n1. **[AGREE, 全票] C1 缺乏 empirical novelty**：R2 从 causal mask（数学必然），R1 从 probe difficulty（trivially easy），交叉回应后 R1 完全同意 R2 的论证更根本\n2. **[AGREE, 全票] C3 的 inverted-U 是 metric-specific**：RSA 下成立，CKA 下消失或反转，\"non-monotonic refinement\" 不是 robust finding\n3. **[AGREE, 全票] Ablation 数据规模问题**：5 demos 下 R² baseline 仅 0.256，因果推断受损\n4. **[AGREE, 全票] C2（routing redistribution）是论文唯一有 genuine novelty 的贡献**：三条件 attention profile 的 mid-depth → entry-exit shift 是 genuine empirical finding，但 practical significance 未验证\n5. **[AGREE, 全票] 实验框架（factorial design + multi-metric）具有方法论价值**\n\n---\n\n## Reviewer Divergence\n\n仅一处小分歧，已在交叉回应中解决：\n\n- **R2-M2（readout/last_preaction 术语）**：R2 认为交替使用未定义等价性，R1 反驳指出 Section 3.2(c) 已明确定义。R2 未在交叉回应中继续争论。结论：非问题。\n\n---\n\n## Questions to Authors\n\n1. **Token ordering**：如果 image tokens 在 causal mask 中先于 instruction tokens，C1 的 image-token instruction-blindness 是否是 architecture-guaranteed 而非 empirical finding？如果是，论文如何重新定位 C1 的贡献？\n2. **Probe difficulty**：是否考虑过更难的 probe 任务（如语义相近指令区分、fine-grained instruction attribute prediction）来验证 readout token 的 \"multimodal convergence\" 超越 trivial linear separability？\n3. **RSA vs CKA**：Linear CKA per-layer profile 单调递增（Appendix B.2），DINOv2 在 RDM kernel CKA 中排名最低。请给出 principled argument 解释为何 RSA 应被优先信任，或 qualify C3 claims 为 metric-dependent。\n4. **Ablation N**：5 demos per task 对应多少 total observation-action pairs？R² baseline 0.256 是否暗示 probe underfitting？是否可用 50 demos 重跑？\n5. **RSA temporal autocorrelation**：同一 demo 内的多个 observation 是否引入 temporal autocorrelation？Bootstrap 是否 block by demo？\n6. **Readout RSA profile**：Table 3 显示 readout RSA peak 在 L12 (0.643)，但 Figure 3 仅画 image_mean。Readout 是否也呈 inverted-U？\n\n---\n\n## Missing References\n\n- Touvron et al. (2023) — Llama 2: Open Foundation and Fine-Tuned Chat Models（模型核心组件）\n- Padalkar et al. (2023) — Open X-Embodiment（训练数据 primary source）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目配置中 external_review 未启用）。\n\n---\n\n## Overall Assessment\n\n**Overall Score: Weak Reject**\n**Confidence: High (4/5)**\n\n论文的实验框架（factorial design + multi-metric analysis）具有方法论价值，写作质量高，robustness analysis 充分。但三个核心贡献中：\n\n- **C1**（token-level specialization）：causal mask 的数学必然 + probe trivially easy → 不构成 meaningful empirical finding\n- **C2**（front-loaded routing）：唯一有 genuine novelty 的贡献，三条件 attention profile 的 entry-exit vs mid-depth 对比是 real finding，但 practical significance 未验证\n- **C3**（inverted-U refinement）：RSA-specific，CKA 下消失/反转，效应量极小（Δρ=0.016），不是 robust finding\n\n仅凭 C2 一个 finding 不足以支撑 CoRL 2026 的投稿。L1 ablation 的 5-demo 数据规模问题进一步削弱因果推断力度。\n\n**如果作者能在 rebuttal 中**：(1) 论证 token ordering 使 C1 non-trivial 或根本性重构 C1 定位；(2) 对 inverted-U rise phase 提供 CI 并 qualify metric-dependence；(3) 用 50 demos 重跑 ablation + random control，评分可能上调至 borderline accept。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- L1-2: 清晰概括了方法\n- L4-5: \"strict token-level functional specialization: image tokens are instruction-blind\" — 需要 qualify 这是 causal mask 的结构性约束\n- L6: \"self-supervised DINOv2 providing the highest geometric foundation\" — 需加 \"under RSA\" qualifier（CKA 下不成立）\n- L7: \"modest geometric gain (Δ = 0.017)\" — 未标注 n.s.\n\n### Introduction\n- L5: \"untested assumption\" 接近 straw man，需重新措辞\n- L19-22: C2 的描述是论文最有价值的贡献，建议提升其在叙事中的权重\n- L27: Contributions 列表中 (i) 应降权或重新定位\n\n### Method\n- §3.3: \"linear classifier (10-way)\" 与 §4.2 \"both linear and MLP probes\" 的关系需在方法中提前说明\n- §3.5: \"Why RSA over CKA\" justification 需加强——当前论据可被对称地反驳\n\n### Experiments\n- §4.2 Table 1: Untrained L1=100% 的 interpretation 需要更多讨论（不仅是 \"incidental\"）\n- §4.2 L76: 5-demo ablation 的方法细节（N, probe architecture, training procedure）应单独说明而非嵌入结果段落\n- §4.3 Figure 3: 应增加 readout token 的 per-layer RSA 曲线\n- §4.3: L0→L12 升幅的 bootstrap CI 需报告\n\n### Discussion\n- \"C1 likely generalizes via the causal mask; C2 may be Llama-2-specific\" — 这种无证据猜测不应出现，要么提供证据要么删除\n- Limitations section 较简短，应扩展讨论 metric-dependence（RSA vs CKA divergence）\n\n### Appendix\n- B.2: CKA divergence 的讨论质量好，但应在正文有 pointer 和 qualification\n- Table 9 vs Table 2 的 25/24 差异解释应集中在一处\n\n### Format\n- conclusion.tex 未被 main.tex \\input\n- references.bib 缺少 Llama-2 和 Open X-Embodiment\n- 部分 R² 精度不统一（2位 vs 3位）\n",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "weak reject",
    "review_chat_id": "oc_554a5023cde4d603635cf97e6ab8151a"
  }
}
```

</details>

---


### Tool result

_source line 257 · 2026-05-17T18:21:38.529862+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a1d032cbe70bdd2058438e67e0d57613:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4068
}
```

</details>

---


### Assistant

_source line 258 · 2026-05-17T18:21:51.430855+00:00_

审稿报告已投递至 Research Director。

**Round 4 审稿完成总结**：

| 项目 | 内容 |
|------|------|
| **Overall** | **Weak Reject** (Confidence 4/5) |
| **Reviewer 配置** | R1（方法/实验）3/5 Borderline + R2（新颖性/写作）5/10 |
| **共识度** | 高——3 个 critical issue 全票共识，仅 1 处 minor 分歧已解决 |

**3 个 Critical Issues（全票共识）**：
1. **C1 是 causal mask 的数学必然**：image tokens 在 causal attention 中先于 instruction tokens，instruction-blindness 是架构保证；readout 100% 是 tokenizer 线性可分性的 trivial 结果
2. **RSA inverted-U metric-dependent**：rise phase 仅 Δρ=0.016，CKA 完全反转 ordering 和 per-layer profile
3. **L1 ablation 用 5 demos**：R² baseline 0.256 暗示 underfitting，缺少 random ablation control

**唯一被认可的 genuine novelty**：C2（三条件 attention routing 的 mid-depth → entry-exit redistribution），但 practical significance 未验证。

Issue Tracker 已同步更新（11 个历史 resolved + 13 个新 open issues）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 31

## Round 31

2 recorded events


### User

_source line 259 · 2026-05-17T18:21:53.952297+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

总结：R1 的 6 条 Must-Fix/Should-Fix 中我同意 5 条、部分反驳 1 条（W5，论文已在多处解释 25/24 差异，只是分散）。R1 和我的审稿独立发现了三个共同核心问题：(1) C1 trivially true（R1 从 probe difficulty 角度，我从 causal mask 角度）；(2) inverted-U 和 DINOv2 ceiling claim 的 metric sensitivity；(3) ablation 数据量不足。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 260 · 2026-05-17T18:22:05.942233+00:00_

审稿报告已提交给 Research Director。

**本轮审稿总结**：

- **Overall Score**: Weak Reject
- **Reviewer 配置**: 2 人，Round 1 + 交叉回应，1 轮收敛
- **3 个 critical 全票共识**：
  1. C1（token-level specialization）是 causal mask 的数学必然 + probe trivially easy，不构成 empirical finding
  2. RSA inverted-U 效应量极小（Δρ=0.016）且 CKA 完全反转，metric-dependent
  3. L1 ablation 仅用 5 demos，因果推断不可靠
- **唯一有 genuine novelty 的贡献**：C2（routing redistribution，entry-exit vs mid-depth attention pattern），但 practical significance 未验证
- **Issue Tracker 已更新**：3 critical + 7 warning + 3 info 新增至 `review_issues.yaml`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 32

## Round 32

74 recorded events


### User

_source line 261 · 2026-05-18T01:46:35.266159+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: vla-ssd
- 论文路径: projects/vla-ssd/docs/paper/main.tex
- 目标 venue: CoRL 2026
- 截止日期: 2026-05-29

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 262 · 2026-05-18T01:46:41.298393+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 263 · 2026-05-18T01:46:41.399750+00:00_

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
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 264 · 2026-05-18T01:46:44.529098+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 265 · 2026-05-18T01:46:44.579722+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 266 · 2026-05-18T01:46:47.241039+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 267 · 2026-05-18T01:46:47.241385+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 268 · 2026-05-18T01:46:50.103611+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 269 · 2026-05-18T01:46:50.204378+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 270 · 2026-05-18T01:46:54.422446+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 271 · 2026-05-18T01:46:55.828378+00:00_

{"result":"# 项目 vla-ssd 概况\n\n## 实验状态 (72 个)\n\n- **lg_extract_untrained_r2**: DONE (killed) — \n- **lg_extract_trained_r2**: DONE (killed) — \n- **lg_extract_untrained_r1**: DONE (killed) — \n- **lg_extract_trained_r1**: DONE (killed) — \n- **mvp2_delta_dino**: DONE (success) — \n- **mvp2_delta_untrained**: DONE (success) — \n- **mvp2_delta_trained**: DONE (success) — \n- **mvp2_action_dino**: DONE (success) — \n- **mvp2_action_untrained**: DONE (success) — \n- **mvp2_action_trained**: DONE (success) — \n- **mvp_controlb_untrained**: DONE (success) — \n- **mvp_controlb_trained**: DONE (success) — \n- **mvp_001**: DONE (negative) — \n- **mvp_probe_untrained**: DONE (success) — \n- **mvp_probe_trained**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- l1_head_ablation_50demos（准备中）\n- l1_head_ablation_control8（准备中）\n- fulllayer_action_probe（准备中）\n\n## 近期结论\n- **llama2base_action_probe** (success): Llama-2 base (pretrained LLM, no VLA training) action R² follows the three-condition gradient: untrained < llama2base < trained, completing the C2 evidence chain for action encoding specialization.\n- **ablation_50demos_main** (success): 50-demo full-data ablation: L1 instruction-dominant heads capacity trade-off (R² increase under ablation) persists with adequate probe training data, eliminating underfitting confound from 5-demo version.\n- **ablation_p2_demo_sensitivity** (success): C3 inverted-U RSA pattern (image_mean, trained) is stable under reduced data (25 demos/task subsample from 50), confirming it is not an artifact of sample size.\n\n## 趋势\n成功 54 / 负向 7 / 失败 0 / 共 69\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-19183: 无 GPU 信息\n\n## 告警\n- mvp2_action_probe: 已被终止 — unknown\n- lg_extract_trained_r2: 已被终止 — unknown\n- lg_extract_untrained_r2: 已被终止 — unknown\n- lg_extract_trained_r1: 已被终止 — unknown\n- lg_extract_untrained_r1: 已被终止 — unknown\n- lg_shuffled_token_control: 已被终止 — unknown
…[truncated 88 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 272 · 2026-05-18T01:46:55.828755+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 273 · 2026-05-18T01:46:56.330874+00:00_

1	\documentclass{article}
2	
3	\usepackage{corl_2026}
4	
5	\usepackage[utf8]{inputenc}
6	\usepackage[T1]{fontenc}
7	\usepackage{url}
8	\usepackage{booktabs}
9	\usepackage{amsfonts}
10	\usepackage{amsmath}
11	\usepackage{nicefrac}
12	\usepackage[expansion=false]{microtype}
13	\usepackage{graphicx}
14	\usepackage{enumitem}
15	
16	\title{Vision Encodes, Language Routes:\\ Token-Level Functional Specialization in a Vision-Language-Action Model}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	
22	\maketitle
23	
24	\begin{abstract}
25	\input{abstract}
26	\end{abstract}
27	
28	\input{introduction}
29	\input{related_work}
30	\input{method}
31	\input{experiments}
32	\input{discussion}
33	
34	\bibliography{references}
35	
36	\input{appendix}
37	
38	\end{document}
39	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 274 · 2026-05-18T01:46:56.331262+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 call for papers submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-18T01:47:04.667684+00:00_

Web search results for query: "CoRL 2026 call for papers submission guidelines author instructions"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 - Instruction for Presentations","url":"https://www.corl.org/contributions/instruction-for-presentations"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"ICML 2026 Author Instructions","url":"https://icml.cc/Conferences/2026/AuthorInstructions"}]

I found the CoRL 2026 submission guidelines and author instructions. Here are the key details:

## Paper Format and Structure

The camera-ready paper should follow the template: 8-page main text + acknowledgment + references + appendix (optional).

## Limitations Section

All submissions should include a Limitations section (counted toward the 8-page limit), explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments, and how these might be addressed in the future.

## Reviewer Participation Requirement

Every author with 3 or more submissions must agree to serve as a reviewer. Authors are exempt from the review requirement if they serve as an AC, an SAC, or another organizing chair for CoRL 2026.

## Rebuttal Process

Papers that receive all reviews in
…[truncated 938 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "WebSearch",
  "elapsed_ms": 8336
}
```

</details>

---


### Tool call

_source line 276 · 2026-05-18T01:47:10.896701+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 instruction for authors page limit template double blind anonymous submission format",
  "allowed_domains": "['corl.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 instruction for authors page limit template double blind anonymous submission format",
    "allowed_domains": "['corl.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool call

_source line 277 · 2026-05-18T01:47:11.098132+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 278 · 2026-05-18T01:47:11.148799+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_example.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 279 · 2026-05-18T01:47:16.281497+00:00_

Web search results for query: "CoRL 2026 instruction for authors page limit template double blind anonymous submission format"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2024 - Instruction for Authors","url":"https://2024.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"},{"title":"FORMATTING INSTRUCTIONS FOR ICLR 2026 ...","url":"https://openreview.net/pdf?id=qioDi3afqm"},{"title":"CoRL 2026 - Instruction for Presentations","url":"https://www.corl.org/contributions/instruction-for-presentations"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2021 - Submission Instructions","url":"https://2021.corl.org/author-information/submission-instructions"},{"title":"CoRL 2026 - Registration","url":"https://www.corl.org/attending/registration"}]

Based on the search results for CoRL 2026, here's what I found regarding the instructions for authors:

## Page Limit
The page limit is 8 pages for the main paper, with Acknowledgments, References, and Appendix (optional) not counting towards the page limit.

## Template
The LaTeX template is available here. The camera-ready paper should follow the template: 8-page main text + acknowledgment + references + appendix (optional).

## Regarding Double-Blind Anonymous Submission
The search results do not contain specific information about whether CoRL 2026 submissions require double-blind anonymous review or details about anonymity requirements. For this information, I recommend visiting the full instruction for authors page at https://www.corl.org/contributions/instruction-for-authors directly, as the format requirements 
…[truncated 270 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "WebSearch",
  "elapsed_ms": 5384
}
```

</details>

---


### Tool call

_source line 280 · 2026-05-18T01:47:20.499621+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,WebFetch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,WebFetch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 281 · 2026-05-18T01:47:20.550386+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 282 · 2026-05-18T01:47:24.236201+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl.org/contributions/instruction-for-authors",
  "prompt": "Extract ALL submission requirements: page limit, template details, anonymous/double-blind rules, appendix rules, citation format, supplementary material rules, any checklist requirements, limitations section requirement. Be exhaustive."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl.org/contributions/instruction-for-authors",
    "prompt": "Extract ALL submission requirements: page limit, template details, anonymous/double-blind rules, appendix rules, citation format, supplementary material rules, any checklist requirements, limitations section requirement. Be exhaustive."
  }
}
```

</details>

---


### Tool call

_source line 283 · 2026-05-18T01:47:24.688457+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 284 · 2026-05-18T01:47:25.241204+00:00_

1	Vision-language-action models (VLAs) fine-tune large language models (LLMs) on robot demonstrations, but how training reshapes information routing at the token level remains uncharacterized.
2	We present a systematic experimental framework for token-level analysis of VLAs, applying cross-instruction probes, attention analysis, Representational Similarity Analysis (RSA), and functional probes across all 32 LLM layers of OpenVLA-7B on LIBERO, with factorial trained/pretrained/untrained controls.
3	Three findings emerge.
4	First, we verify and quantify architecture-expected token specialization: image tokens are instruction-blind (classification at chance, $10\%$, across all layers and conditions), consistent with the causal mask and frozen encoder, while the readout token serves as the sole multimodal convergence point ($100\%$ instruction classification from L1, cross-validated).
5	Second, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth (L9--L16, 15--22 heads), while VLA training shifts this to entry-layer routing (L0--L1: 21--24 heads) with exit-layer re-engagement (L31: 18 heads), enabling immediate instruction access ($99.6\%$ at L1 vs.\ pretrained $80.2\%$); untrained models show zero instruction-dominant heads throughout.
6	Third, functional probes reveal a non-monotonic trajectory through LLM layers ($R^2$ peaks at L8--L13 before declining), with RSA showing a corresponding geometric pattern ($\rho$ peak at L12, declining to $0.422$); however, both the per-layer profile and encoder rankings are metric-dependent (CKA yields monotonically increasing profiles and different encoder orderings; Appendix).
7	Training effects concentrate at the readout token (probe $R^2$ $+0.069$, instruction attention $+46$pp) rather than visual geometry ($\Delta\rho \leq 0.017$, non-significant), identifying instruction routing reorganization as the primary learned contribution of VLA fine-tuning.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 285 · 2026-05-18T01:47:25.241726+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 286 · 2026-05-18T01:47:25.292343+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Vision-language-action models (VLAs) process visual observations and language instructions through a large language model to produce robot actions~\cite{brohan2023_rt2,kim2024_openvla}.
5	While the decoder-only architecture imposes structural constraints on information flow (the causal mask prevents image tokens from attending to subsequent instruction tokens), how VLA fine-tuning reshapes the routing and integration of multimodal information within the LLM backbone remains uncharacterized.
6	
7	Recent behavioral studies reveal that VLAs rely disproportionately on visual input~\cite{grant2026}, with language instructions largely ignored by the action pathway~\cite{haon2025}.
8	These findings suggest internal specialization but do not explain \emph{how} instruction information reaches the action-generating readout token, \emph{what} routing strategy fine-tuning learns compared to language pretraining alone, or \emph{whether} training creates new representational structure or reconfigures inherited geometry.
9	Existing analyses have not combined systematic per-layer probing with factorial trained/pretrained/untrained controls, leaving the representational mechanisms of VLA fine-tuning opaque.
10	
11	We address this gap by decomposing OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a VLA chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2}, an MLP projector, and Llama-2 7B~\cite{touvron2023_llama2}.
12	We extract representations from each of 32 LLM layers at both image-token and readout-token positions, and from external baselines (DINOv2~\cite{oquab2024_dinov2}, CLIP~\cite{radford2021_clip}).
13	We compare three LLM conditions (VLA-trained, pretrained Llama-2 base, and randomly initialized) crossed with instruction presence, and apply four complementary analyses: cross-instruction probes for token-level specialization, L1 attention pattern analysis for routing mechanisms, RSA~\c
…[truncated 2465 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 287 · 2026-05-18T01:47:30.212041+00:00_

# CoRL 2026 Submission Requirements

## Page Limits
- **Initial submission:** "8 pages for the main paper"
- **Camera-ready:** 9 pages for main text
- Acknowledgments, references, and appendix do not count toward page limits
- Appendix inclusion is optional; reviewers are not obligated to read it

## Template & Formatting
- Use the provided LaTeX template (separate links for initial and camera-ready submissions)
- Camera-ready template requires `\usepackage[final]{corl_2026}`
- Maintain identical text density, fonts, spacing, and margins as template
- Footer on first page must read: "10th Conference on Robot Learning (CoRL 2026), Austin, Texas, USA."

## Anonymization
- Papers must be "double-blind," meaning all submissions require anonymization
- Camera-ready versions are NOT anonymous; author names must appear

## Appendix Rules
- Optional but may be included with main paper or supplementary materials
- Reviewers are not required to read appendices
- Camera-ready: append to main PDF rather than submit separately

## Limitations Section
Submissions must include "a Limitations section (counted toward the 8-page limit), explicitly describing limiting assumptions, failure modes, and other limitations"

## Supplementary Materials
- Encouraged but optional
- Single zip file format via OpenReview
- Video: maximum 250 MB, suggested 3-minute length limit
- PMLR prohibits video supplementary submissions; host externally instead
- Reviewers may optionally consult supplements

## Citation Format
Not specified in document

## Checklist
Not explicitly provided

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "WebFetch",
  "elapsed_ms": 5975
}
```

</details>

---


### Tool call

_source line 288 · 2026-05-18T01:47:37.242130+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 289 · 2026-05-18T01:47:37.343026+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Vision-language-action models.}
4	VLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}.
5	This architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.
6	A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.
7	We test this assumption at the representational level through per-layer, per-token-type decomposition.
8	
9	\paragraph{Mechanistic interpretability in transformers.}
10	A growing body of work analyzes transformer internals at the level of individual attention heads and circuits.
11	Elhage et al.~\cite{elhage2021} introduced the residual stream framework, in which each layer reads from and writes to a shared communication channel.
12	Building on this, Olsson et al.~\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning; these specialized attention heads implement token-copying algorithms.
13	Circuit-level analyses have since traced complete computational subgraphs for tasks such as indirect object identification~\cite{wang2023_ioi} and greater-than comparison~\cite{conmy2023}.
14	In parallel, attention probing studies have shown that individual heads encode syntactic relations~\cite{clark2019}, capture positional and structural patterns at different depths~\cite{vig2019}, and that a small subset of specialized heads accounts for most model performance~\cite{voita2019}.
15	Our Layer-1 attention head analysis extends this tradition to the VLA domain, where we find that 24 of 32 heads become instruction-dominant after fine-tuning.
16	
17	\paragraph{Behavioral and mechanistic analysis of VLAs.}
18	Behavioral evaluations reveal that current VLAs rel
…[truncated 2687 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 290 · 2026-05-18T01:47:37.393725+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 291 · 2026-05-18T01:47:37.845938+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We investigate how action-relevant structure is distributed across a VLA by combining four complementary analyses: cross-instruction probes, attention pattern analysis, RSA, and functional probes.
5	
6	%------------------------------------------------------------------
7	\subsection{Model and Data}
8	\label{sec:model_data}
9	
10	We study OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a generalist robot policy chaining three components: a frozen DinoSigLIP fused vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), a Multi-Layer Perceptron (MLP) projector (2{,}176-D $\to$ 4{,}096-D), and a Llama-2 7B~\cite{touvron2023_llama2} language backbone (6.74B parameters) that autoregressively decodes 7-dimensional actions.
11	We use the base checkpoint pretrained on Open X-Embodiment~\cite{padalkar2023_oxe} (no task-specific fine-tuning) and evaluate on LIBERO-Goal~\cite{liu2023_libero} (10 tabletop tasks, 50 demonstrations each).
12	To disentangle the contributions of language pretraining and VLA fine-tuning, we compare three LLM conditions: (1)~VLA-trained (the released checkpoint), (2)~Llama-2 base (the pretrained LLM backbone without VLA fine-tuning), and (3)~untrained (all 6.74B LLM parameters reinitialized via \texttt{from\_config()}).
13	All three conditions share the same frozen vision encoder and projector architecture.
14	
15	%------------------------------------------------------------------
16	\subsection{Representation Extraction}
17	\label{sec:repr_extraction}
18	
19	We extract representations from six sources spanning the VLA pipeline:
20	(a)~\textbf{DinoSigLIP+Projector}, the projector output (4{,}096-D), immediately before LLM processing;
21	(b)~\textbf{LLM image\_mean}, the mean image-token activation at each of 32 layers;
22	(c)~\textbf{LLM readout}, the activation at the final pre-action token position at each layer;
23	(d)~\textbf{DINOv2 ViT-L/14}~\cite{oquab2024_dinov2} 
…[truncated 4077 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 292 · 2026-05-18T01:47:37.846395+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 293 · 2026-05-18T01:47:37.947368+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We evaluate OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024} on LIBERO-Goal~\cite{liu2023_libero} (10 tasks, 50 demonstrations each).
8	Representations are extracted from six sources spanning the VLA pipeline (\S\ref{sec:repr_extraction}): DinoSigLIP+Projector, LLM image\_mean and readout tokens at each of 32 layers, DINOv2~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}), CLIP~\cite{radford2021_clip} (\texttt{patch\_mean}), and branch-split (DINOv2 1{,}024-D / SigLIP 1{,}152-D before fusion).
9	Three LLM conditions are compared: VLA-trained, pretrained Llama-2 base (no VLA fine-tuning), and untrained (6.74B parameters reinitialized to random weights), crossed with instruction presence (\S\ref{sec:model_data}).
10	RSA computes Spearman $\rho$ between cosine-distance representation RDMs and Euclidean-distance action RDMs, with 10{,}000 bootstrap CIs (\S\ref{sec:rsa}).
11	MLP probes (input $\to$ 256 $\to$ 7; Adam, lr${}=10^{-3}$, 50 epochs, early stopping) report mean $R^2$ (\S\ref{sec:probes}).
12	This yields $N = 63{,}228$ observations (50 demonstrations $\times$ 10 tasks $\times$ $\sim$127 timesteps per demonstration). For the MLP probe (2-layer, 256 hidden units), the ratio $N/\text{params} \approx 0.05$, ensuring adequate training signal.
13	
14	%------------------------------------------------------------------
15	\subsection{Token-Level Functional Specialization}
16	\label{sec:token_specialization}
17	
18	We test whether image tokens and readout tokens encode different types of information by training cross-instruction probes (\S\ref{sec:cross_instruction_probes}): given the same visual frame paired with each of 10 task instructions, we classify which instruction was present from per-layer activations.
19	
20	\paragraph{Image tokens are instruction-blind.}
21	At the image\_mean position, instruction classification remains at chance (
…[truncated 11520 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 294 · 2026-05-18T01:47:43.369046+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 295 · 2026-05-18T01:47:43.922021+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Synthesis.}
5	Image tokens remain instruction-blind across all 32 layers (causal mask, frozen encoder); the readout token is the sole multimodal convergence point.
6	VLA fine-tuning shifts routing from mid-depth (L9--L16) to entry-exit (L0--L1, L31), concentrating effects at the readout ($R^2$ $+0.069$) rather than image representations ($\Delta \leq 1.7\%$).
7	
8	\paragraph{Mechanism-behavior connection.}
9	Image-token instruction-blindness explains the visual dominance reported by Grant et al.~\cite{grant2026}: actions rely on readout-token conditioning.
10	Under RSA, DINOv2 achieves the highest geometric alignment ($\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\ $0.634$), indicating instruction-conditioned integration rather than enhanced geometry.
11	
12	\paragraph{Speculative mechanistic interpretation.}
13	The per-layer RSA curves reveal a functional bifurcation after L12 (Figure~\ref{fig:rsa_perlayer_curve}): readout $\rho$ declines gradually ($0.628 \to 0.584$) while image\_mean $\rho$ drops sharply ($0.628 \to 0.422$).
14	This pattern suggests that deeper layers prioritize task-specific output conditioning at the readout token while progressively compressing image token geometry.
15	One interpretation is that mid-layers (L8--L13) perform cross-modal feature integration, producing the $R^2$ peak observed in functional probes, while deeper layers specialize for action generation.
16	Testing this hypothesis requires layer-wise interventions beyond the L1 ablation presented here.
17	
18	\paragraph{Architectural implications.}
19	Attention ablation at L1 confirms functional specialization: removing instruction-dominant heads' attention to instruction tokens increases action $R^2$ by $+0.059$ ($p < 0.0001$), while removing non-dominant heads yields $+0.017$, a 3.5$\times$ smaller effect that rules out generic attention removal as an explanation.
20	The effect is conf
…[truncated 1341 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 296 · 2026-05-18T01:47:44.073075+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 297 · 2026-05-18T01:47:44.425358+00:00_

1	\appendix
2	
3	\section{Supplementary Material}
4	\label{sec:appendix}
5	
6	\subsection{CKA Analysis Method}
7	\label{sec:cka_appendix}
8	
9	We employ Centered Kernel Alignment (CKA)~\cite{kornblith2019} alongside RSA as a complementary perspective.
10	While RSA captures local geometric alignment via rank-order preservation, CKA measures global representational similarity through kernel-based comparisons.
11	
12	We compute both \emph{linear CKA}, which uses a linear kernel and is sensitive to second-order statistics, and \emph{RDM kernel CKA}, which operates on the same distance matrices as RSA but aggregates them differently.
13	Using both variants tests whether conclusions about representation structure are robust to the choice of similarity metric.
14	
15	Linear CKA between high-dimensional representations (4{,}096-D for LLM layers) and the 7-D action space is subject to a known dimension mismatch: the linear kernel in the low-dimensional space may not capture the same structure as in the high-dimensional space.
16	RDM kernel CKA avoids this issue by operating on distance matrices of equal size regardless of the original feature dimensionality.
17	
18	\subsection{Metric Sensitivity: RSA versus CKA}
19	\label{sec:metric_sensitivity_appendix}
20	
21	Linear CKA~\cite{kornblith2019} reverses the RSA ordering: untrained LLM ($\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially inverting the self-supervised advantage (Figure~\ref{fig:metric_comparison}).
22	RDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $\approx$ Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).
23	This divergence reflects the known sensitivity of representation similarity metrics to different geometric properties.
24	
25	At the per-layer level, linear CKA between image\_mean and the action space rises monotonically from L0 ($0.081$) to L32 ($0.098$), showing no inverted-U pattern.
26	RSA captures ran
…[truncated 24863 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 298 · 2026-05-18T01:47:49.750200+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 299 · 2026-05-18T01:47:50.102528+00:00_

1	% === VLA / Architecture ===
2	
3	@article{kim2024_openvla,
4	  title     = {{OpenVLA}: An Open-Source Vision-Language-Action Model},
5	  author    = {Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balakrishna, Ashwin and Nair, Suraj and Rafailov, Rafael and Foster, Ethan and Lam, Grace and Sanketi, Pannag and Lu, Quan and Kollar, Thomas and Burchfiel, Benjamin and Tedrake, Russ and Sadigh, Dorsa and Levine, Sergey and Liang, Percy and Finn, Chelsea},
6	  journal   = {arXiv preprint arXiv:2406.09246},
7	  year      = {2024},
8	}
9	
10	@article{karamcheti2024,
11	  title     = {Prismatic {VLMs}: Investigating the Design Space of Visually-Conditioned Language Models},
12	  author    = {Karamcheti, Siddharth and Nair, Suraj and Balakrishna, Ashwin and Liang, Percy and Kollar, Thomas and Sadigh, Dorsa},
13	  journal   = {arXiv preprint arXiv:2402.07865},
14	  year      = {2024},
15	}
16	
17	@article{brohan2023_rt2,
18	  title     = {{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
19	  author    = {Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},
20	  journal   = {arXiv preprint arXiv:2307.15818},
21	  year      = {2023},
22	}
23	
24	% === Benchmark ===
25	
26	@inproceedings{liu2023_libero,
27	  title     = {{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
28	  author    = {Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},
29	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
30	  year      = {2023},
31	}
32	
33	% === Representation Analysis Methods ===
34	
35	@article{kriegeskorte2008,
36	  title     = {Representational Similarity Analysis -- Connecting the Branches of Systems Neuroscience},
37	  author    = {Kriegeskorte, Nikolaus and Mur, Marieke and Ban
…[truncated 14015 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 300 · 2026-05-18T01:47:50.102959+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 301 · 2026-05-18T01:47:50.153451+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'vla-ssd'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 302 · 2026-05-18T01:47:55.125673+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures"
  }
}
```

</details>

---


### Tool result

_source line 303 · 2026-05-18T01:47:56.582215+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures/fig2.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures/fig3.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures/fig6.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures/fig5.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures/fig4.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures/libero_spatial_rsa_perlayer.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures/libero_spatial_r2_perlayer.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures/fig7.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures/fig8a_trained_summary.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures/fig8a_trained_task0.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures/fig8b_untrained.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures/fig8_attention.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures/fig_probe_conditions.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures/fig_multi_layer_attn.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures/fig_l1_stacked_bar.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures/fig_32layer_attention.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures/fig_rsa_perlayer_curve.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures/fig_action_r2_threecond.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "elapsed_ms": 1456
}
```

</details>

---


### Tool call

_source line 304 · 2026-05-18T01:47:56.733249+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 305 · 2026-05-18T01:47:56.884384+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 306 · 2026-05-18T01:48:00.449151+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
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

_source line 307 · 2026-05-18T01:48:00.499802+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 308 · 2026-05-18T01:48:03.966544+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 309 · 2026-05-18T01:48:04.620374+00:00_

1	issues:
2	  # ============================================================
3	  # Round 1-3 历史 issues（全部 resolved）
4	  # ============================================================
5	  - id: R1-N1-old
6	    summary: "Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献"
7	    category: experiment
8	    severity: critical
9	    status: resolved
10	    first_raised_round: 1
11	    last_seen_round: 2
12	    mentions:
13	      - round: 1
14	        reviewers: [1, 2, 3]
15	        note: "全票共识。需增加 Llama-2 base checkpoint 作为中间对照"
16	      - round: 2
17	        reviewers: [1, 2, 3]
18	        note: "PARTIALLY_RESOLVED: acknowledge confound 但无数据"
19	    action_items:
20	      - round: 1
21	        action: "增加 Llama-2 base checkpoint 对照实验"
22	        assigned_to: research
23	        status: done
24	      - round: 2
25	        action: "Section 标题改为观察性；Abstract 弱化 causal attribution"
26	        assigned_to: paper_agent
27	        status: done
28	    resolution: "B版本完整整合三条件数据：untrained 0/32, Llama-2 base 9/32, trained 25/32 heads。§4.3 以三条件梯度为核心证据，Table 2 + Figure 4 呈现完整 32 层 profile。"
29	    resolution_round: 3
30	
31	  - id: R1-N2-old
32	    summary: "单一模型(OpenVLA-7B) + 单一 benchmark family(LIBERO)，Title/Abstract 使用复数 'VLAs' 构成 overclaim"
33	    category: framing
34	    severity: critical
35	    status: resolved
36	    first_raised_round: 1
37	    last_seen_round: 2
38	    mentions:
39	      - round: 1
40	        reviewers: [1, 2, 3]
41	        note: "全票共识"
42	      - round: 2
43	        reviewers: [1, 2, 3]
44	        note: "PARTIALLY_RESOLVED: Abstract 限定但 Title 仍复数"
45	    action_items:
46	      - round: 2
47	        action: "Title 改为单数"
48	        assigned_to: paper_agent
49	        status: done
50	    resolution: "B版本 Title = 'Token-Level Functional Specialization in a Vision-Language-Action Model'（单数）。"
51	    resolution_round: 3
52	
53	  - id: R1-N4-old
54	    summary: "Design implications 完全基于 correlational evidence"
55	    category: framing
56	    severity: cri
…[truncated 11882 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 310 · 2026-05-18T01:48:04.671093+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_reports/round_1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_reports/round_1.md"
  }
}
```

</details>

---


### Tool result

_source line 311 · 2026-05-18T01:48:04.721868+00:00_

1	---
2	round: 1
3	overall_score: weak reject
4	timestamp: 2026-05-17T04:44:22.453130+00:00
5	reviewer_ids: [1, 2, 3]
6	cross_response_reviewer_ids: [1, 2, 3]
7	force_resubmit: False
8	---
9	
10	# 圆桌审稿报告 — Round 1
11	
12	**论文**: "Vision Encodes, Language Routes: A Representational Decomposition of Vision-Language-Action Models"
13	**Venue**: CoRL 2026 (Deadline: 2026-05-28)
14	**Reviewers**: R1 (方法/实验), R2 (新颖性/意义), R3 (写作/格式)
15	
16	---
17	
18	## Summary
19	
20	论文对 OpenVLA-7B 进行了 token-level 表征分解，结合 cross-instruction probes、attention analysis、RSA 和 functional probes，在 LIBERO 上发现三个现象：(1) image tokens 与 readout token 的功能特化；(2) 训练学习了 deliberate instruction routing；(3) LLM 对 vision encoder 输出的 non-monotonic refinement（inverted-U）。分析设计系统、robustness checks 全面、写作清晰，但存在根本性的实验设计缺陷和 overclaiming 问题。
21	
22	---
23	
24	## Strengths
25	
26	1. **系统化分析框架**：四种互补方法 + 2×2 factorial design + trained/untrained 对照，比单一 metric 更有说服力（R1, R2 共识）
27	2. **统计严谨性**：Bootstrap CI、LOOCV、permutation test、seed sensitivity、cross-benchmark replication、demo subsampling——附录 robustness analyses 扎实（R1 强调）
28	3. **写作清晰度高**：叙事主线统一（specialization → routing → geometry），三个 findings 层层递进，图表信息密度高（R3 确认）
29	4. **诚实报告 null/adverse results**：RSA best-vs-best CI 包含 0、CKA 反转 RSA、peak convergence 不跨 benchmark 复制等均如实报告（R1 认可）
30	5. **有潜在的 design insight 价值**：如果 findings 经因果验证成立，对 VLA 架构设计有实际指导意义
31	
32	---
33	
34	## Weaknesses（按严重性排序）
35	
36	### Critical（影响接收决定，全票共识）
37	
38	**W-Critical-1: Untrained baseline 无法隔离 VLA fine-tuning 的贡献**
39	- 论文将 trained (Llama-2 pretrained + VLA fine-tuned) 与 untrained (6.74B random weights) 对比，声称差异反映 "training learns deliberate routing"
40	- 这混淆了两个因素：(1) Llama-2 语言预训练；(2) VLA fine-tuning。25/32 heads 翻转为 instruction-dominant 可能是语言预训练的产物
41	- 缺失关键中间对照：Llama-2 base checkpoint (pretrained but not VLA-finetuned)
42	- 影响范围：论文核心 Finding 2（routing）和所有 trained vs untrained Δ 值的解释
43	- **全票共识 (R1 critical, R2 AGREE, R3 AGREE)**
44	
45	**W-Critical-2: 单一模型 + 单一 benchmark family，结论过度泛化**
46	- 仅 Op
…[truncated 7055 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 312 · 2026-05-18T01:48:56.674608+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "paper_framing.md"
  }
}
```

</details>

---


### Tool result

_source line 313 · 2026-05-18T01:48:56.775781+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_framing.md\", \"content\": \"# Paper Framing — vla-ssd (Plan B → D060 Reframe)\\n\\n> D048: PI 批准按最大质量重构。A+ 版本保留为 fallback (branch paper-a-plus-backup)。\\n> D060: Round 4 weak reject → C1 降为框架, C2 升为唯一核心 claim, C3 降为 qualified observation。\\n\\n## Target Venue\\n- Primary: CoRL 2026\\n- Deadline: Abstract May 26, Paper May 29\\n- Format: 8 pages + references\\n\\n## Core Insight\\n\\nVLA fine-tuning 的核心贡献是学习 deliberate instruction routing：将 instruction attention 从语言预训练的中层模式（L9-L16）reorganize 到 entry-exit 模式（L0-L1 + L31），实现即时 instruction access。这个三条件梯度（untrained 0/32 → pretrained 9/32 → trained 25/32）是 genuine empirical finding，具有 causal evidence 支撑。Token-level specialization（image-blind, readout-hub）是 causal mask 架构保证的性质，我们通过系统实验 verify 和 quantify 其在实际 VLA 中的表现。\\n\\n## Core Claims (D060 重构：1 核心 + 1 框架 + 1 观察)\\n\\n### C1: Experimental Framework + Architecture-Verified Specialization [方法论贡献，非 empirical finding]\\n**重新定位（D060）**: Token-level specialization 是 causal mask 的数学必然（image tokens 在序列中先于 instruction tokens，无法 attend to instructions）+ frozen encoder 不接收 instruction input。论文贡献不是\\\"发现\\\"这一点，而是：\\n- **(a) 系统实验框架**：factorial design (trained/pretrained/untrained × instruction presence) + 四种互补分析方法（cross-instruction probe + attention + RSA + MLP probe），适用于任何 decoder-only VLA\\n- **(b) 量化验证**：即使 residual stream 理论上可以 leak information，image tokens 在实际模型的全部 32 层均保持 chance（10%）。这不是 trivial——frozen encoder 权重与 LLM 权重共享 residual stream，验证了 no leakage\\n- **(c) 训练差异的量化**：untrained readout L1=100% 但 L31=82%（信号衰减）vs trained 100% 全程稳定——framework 揭示了训练影响 routing robustness 而非 routing existence\\n\\nKey evidence (unchanged):\\n- Cross-instruction probe: same frame × 10 instructions → 10-way classification\\n- Dense L0-L32: image_mean = chance at ALL layers\\n- LOOCV: 100%±0.00 trained, decaying untrained\\n- **承认**: 10-way classification 本身 trivially ea
…[truncated 8969 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 314 · 2026-05-18T01:48:56.776303+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "round_*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_reports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "round_*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_reports"
  }
}
```

</details>

---


### Tool result

_source line 315 · 2026-05-18T01:48:56.826775+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_reports/round_3.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 316 · 2026-05-18T01:49:54.342312+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 审稿任务 — Reviewer 1: 方法/实验严谨性\n\n**论文**: \"Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\"\n**路径**: `projects/vla-ssd/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, appendix.tex, references.bib）\n**Venue**: CoRL 2026, double-blind, 8 页正文 + refs + appendix, Limitations section 必须（计入 8 页）\n**Deadline**: 2026-05-29\n\n### 你的审查侧重\n\n**1. 统计方法论**\n- 多重比较校正：论文声称使用 FDR correction (Benjamini-Hochberg)，验证其是否恰当应用于 32 层 × 多条件 × 多 metric 的比较\n- Bootstrap CI 报告是否完整（特别是 RSA rise phase L0→L12 的 CI）\n- Probe 的 N/params ratio 报告（论文声称 N=63,228, ratio≈0.05）是否合理\n- Permutation test 和 seed sensitivity 的充分性\n\n**2. 实验设计**\n- 三条件对照（trained/pretrained/untrained）是否充分隔离 VLA fine-tuning 的贡献？Llama-2 base 数据是否完整整合？\n- L1 attention ablation：论文现在声称使用 50 demonstrations（N=63,228）。检查 ablation 设计：dominant 24 heads vs non-dominant 8 heads control 的因果推断是否合理\n- Cross-benchmark validation (LIBERO-Goal + LIBERO-Spatial) 的独立性和充分性\n\n**3. Round 4 Critical Issues 修复检查**\n以下是上轮审稿的 critical issues，请逐条验证当前版本是否充分解决：\n- **R4-N1 (critical)**: C1（token-level specialization）被批为 causal mask 必然结果 + probe trivially easy。论文应已 reframe 为\"experimental framework + empirical verification\"而非\"empirical finding\"\n- **R4-N2 (critical)**: RSA inverted-U 的 rise phase 极小（Δρ=0.016）且 metric-dependent（CKA 反转）。论文应已加\"under RSA\" qualifier 并在正文讨论 CKA 分歧\n- **R4-N3 (critical)**: L1 ablation 原用 5 demos（严重 underfitting）。论文应已改用 50 demos\n- **R4-W2 (warning)**: 缺乏多重比较校正。论文应已加 FDR correction\n- **R4-W3 (warning)**: Probe N 和 capacity 未报告。论文应已报告 N=63,228 和 N/params\n\n**4. 新发现的方法论问题**\n- 除检查上轮问题外，以独立审稿人视角评估是否存在新的方法论缺陷\n- 特别关注：probing methodology (Belinkov 2022 批判)、RSA vs CKA 选择的 principled justification、attention 分析的 threshold sensitivity\n\n### 输出格式\n按以下结构输出审稿意见：\n1. Summary（2-3 句）\n2. Strengths（逐条）\n3. Weaknesses（分 critical / warning / info 三级，逐条）\n4. Round 4 Issue Status（逐条标注 RESOLVED / PARTIALLY_RESOLVED / NOT_RESOLVED）\n5. Questions for Authors\n6. Overall Score（1-10）和 Confidence（1-5）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 审稿任务 — Reviewer 1: 方法/实验严谨性\n\n**论文**: \"Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\"\n**路径**: `projects/vla-ssd/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, appendix.tex, references.bib）\n**Venue**: CoRL 2026, double-blind, 8 页正文 + refs + appendix, Limitations section 必须（计入 8 页）\n**Deadline**: 2026-05-29\n\n### 你的审查侧重\n\n**1. 统计方法论**\n- 多重比较校正：论文声称使用 FDR correction (Benjamini-Hochberg)，验证其是否恰当应用于 32 层 × 多条件 × 多 metric 的比较\n- Bootstrap CI 报告是否完整（特别是 RSA rise phase L0→L12 的 CI）\n- Probe 的 N/params ratio 报告（论文声称 N=63,228, ratio≈0.05）是否合理\n- Permutation test 和 seed sensitivity 的充分性\n\n**2. 实验设计**\n- 三条件对照（trained/pretrained/untrained）是否充分隔离 VLA fine-tuning 的贡献？Llama-2 base 数据是否完整整合？\n- L1 attention ablation：论文现在声称使用 50 demonstrations（N=63,228）。检查 ablation 设计：dominant 24 heads vs non-dominant 8 heads control 的因果推断是否合理\n- Cross-benchmark validation (LIBERO-Goal + LIBERO-Spatial) 的独立性和充分性\n\n**3. Round 4 Critical Issues 修复检查**\n以下是上轮审稿的 critical issues，请逐条验证当前版本是否充分解决：\n- **R4-N1 (critical)**: C1（token-level specialization）被批为 causal mask 必然结果 + probe trivially easy。论文应已 reframe 为\"experimental framework + empirical verification\"而非\"empirical finding\"\n- **R4-N2 (critical)**: RSA inverted-U 的 rise phase 极小（Δρ=0.016）且 metric-dependent（CKA 反转）。论文应已加\"under RSA\" qualifier 并在正文讨论 CKA 分歧\n- **R4-N3 (critical)**: L1 ablation 原用 5 demos（严重 underfitting）。论文应已改用 50 demos\n- **R4-W2 (warning)**: 缺乏多重比较校正。论文应已加 FDR correction\n- **R4-W3 (warning)**: Probe N 和 capacity 未报告。论文应已报告 N=63,228 和 N/params\n\n**4. 新发现的方法论问题**\n- 除检查上轮问题外，以独立审稿人视角评估是否存在新的方法论缺陷\n- 特别关注：probing methodology (Belinkov 2022 批判)、RSA vs CKA 选择的 principled justification、attention 分析的 threshold sensitivity\n\n### 输出格式\n按以下结构输出审稿意见：\n1. Summary（2-3 句）\n2. Strengths（逐条）\n3. Weaknesses（分 critical / warning / info 三级，逐条）\n4. Round 4 Issue Status（逐条标注 RESOLVED / PARTIALLY_RESOLVED / NOT_RESOLVED）\n5. Questions for Authors\n6. Overall Score（1-10）和 Confidence（1-5）"
  }
}
```

</details>

---


### Tool result

_source line 317 · 2026-05-18T01:50:13.348657+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19006
}
```

</details>

---


### Tool call

_source line 318 · 2026-05-18T01:50:13.600187+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 审稿任务 — Reviewer 2: 新颖性/意义 + 相关工作 + Framing\n\n**论文**: \"Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\"\n**路径**: `projects/vla-ssd/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, appendix.tex, references.bib）\n**Venue**: CoRL 2026, double-blind, 8 页正文 + refs + appendix, Limitations section 必须（计入 8 页）\n**Deadline**: 2026-05-29\n\n### 你的审查侧重\n\n**1. 新颖性与意义评估**\n- 三个 claims 的 novelty 层级：C1（framework + architecture verification）、C2（instruction routing reorganization, 核心 finding）、C3（vision encoder geometry observation）\n- 与最近的直接竞争者对比 novelty：Grant et al. 2026 (Action Atlas, 6 models), Häon et al. 2025 (steering directions), Swann/Buurmeijer 2026 (SAE features)\n- C2 的 three-condition routing gradient（0/32 → 9/32 → 24/32）是否构成 genuine empirical contribution？\n- 对 CoRL 社区（robotics + learning）的实际意义：分析论文的 finding 能否指导 VLA 设计？\n\n**2. 相关工作覆盖度**\n- 当前 references.bib 有 29 entries。评估是否达到 CoRL 论文的引用覆盖标准\n- 检查是否缺失重要相关工作（特别是：2025-2026 年的 VLA 分析论文、VLM token-level analysis、probing methodology 经典文献）\n- Related Work section 的组织结构和 positioning 是否清晰\n\n**3. Framing 与 Claim 范围**\n- Abstract 和 Introduction 的 claim 强度是否匹配证据：\n  - C1 是否恰当定位为 framework 而非 finding？\n  - C2 \"front-loads instruction routing\" 是否有充分支撑？\n  - C3 \"non-monotonic\" observation 是否恰当标注了 metric-dependence？\n- Title 使用单数\"a Vision-Language-Action Model\"——是否已消除 overclaiming？\n- Discussion 的 design implications 是否仍然过强？\n\n**4. Round 4 Framing Issues 修复检查**\n- **R4-N1 (critical)**: C1 reframe 是否到位（从\"empirical finding\"到\"experimental framework + empirical verification\"）\n- **R4-W1 (warning)**: RSA best-vs-best n.s. 在 Abstract/Intro 是否已标注\n- **R4-W4 (warning)**: Frozen encoder confound caveat 是否在 Discussion 中充分说明\n- **R4-W5 (warning)**: 单模型局限性是否已在 Limitations 中充分展开\n- **R4-W7 (warning)**: Introduction 的 \"untested assumption\" straw man 是否已修复\n- **R4-I1 (info)**: conclusion.tex 是否已整合或 Discussion 结尾是否充分\n\n**5. 写作风格**\n- 检查 AI 写作痕迹（em-dash、-ing phrases、过度分段）\n- 专有名词是否首次出现即定义\n- Abstract 是否满足 150-250 words 和四个必答问题\n\n### 输出格式\n按以下结构输出审稿意见：\n1. Summary（2-3 句）\n2. Strengths（逐条）\n3. Weaknesses（分 critical / warning / info 三级，逐条）\n4. Round 4 Issue Status（逐条标注 RESOLVED / PARTIALLY_RESOLVED / NOT_RESOLVED）\n5. Missing References（如有）\n6. Questions for Authors\n7. Overall Score（1-10）和 Confidence（1-5）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 审稿任务 — Reviewer 2: 新颖性/意义 + 相关工作 + Framing\n\n**论文**: \"Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\"\n**路径**: `projects/vla-ssd/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, appendix.tex, references.bib）\n**Venue**: CoRL 2026, double-blind, 8 页正文 + refs + appendix, Limitations section 必须（计入 8 页）\n**Deadline**: 2026-05-29\n\n### 你的审查侧重\n\n**1. 新颖性与意义评估**\n- 三个 claims 的 novelty 层级：C1（framework + architecture verification）、C2（instruction routing reorganization, 核心 finding）、C3（vision encoder geometry observation）\n- 与最近的直接竞争者对比 novelty：Grant et al. 2026 (Action Atlas, 6 models), Häon et al. 2025 (steering directions), Swann/Buurmeijer 2026 (SAE features)\n- C2 的 three-condition routing gradient（0/32 → 9/32 → 24/32）是否构成 genuine empirical contribution？\n- 对 CoRL 社区（robotics + learning）的实际意义：分析论文的 finding 能否指导 VLA 设计？\n\n**2. 相关工作覆盖度**\n- 当前 references.bib 有 29 entries。评估是否达到 CoRL 论文的引用覆盖标准\n- 检查是否缺失重要相关工作（特别是：2025-2026 年的 VLA 分析论文、VLM token-level analysis、probing methodology 经典文献）\n- Related Work section 的组织结构和 positioning 是否清晰\n\n**3. Framing 与 Claim 范围**\n- Abstract 和 Introduction 的 claim 强度是否匹配证据：\n  - C1 是否恰当定位为 framework 而非 finding？\n  - C2 \"front-loads instruction routing\" 是否有充分支撑？\n  - C3 \"non-monotonic\" observation 是否恰当标注了 metric-dependence？\n- Title 使用单数\"a Vision-Language-Action Model\"——是否已消除 overclaiming？\n- Discussion 的 design implications 是否仍然过强？\n\n**4. Round 4 Framing Issues 修复检查**\n- **R4-N1 (critical)**: C1 reframe 是否到位（从\"empirical finding\"到\"experimental framework + empirical verification\"）\n- **R4-W1 (warning)**: RSA best-vs-best n.s. 在 Abstract/Intro 是否已标注\n- **R4-W4 (warning)**: Frozen encoder confound caveat 是否在 Discussion 中充分说明\n- **R4-W5 (warning)**: 单模型局限性是否已在 Limitations 中充分展开\n- **R4-W7 (warning)**: Introduction 的 \"untested assumption\" straw man 是否已修复\n- **R4-I1 (info)**: conclusion.tex 是否已整合或 Discussion 结尾是否充分\n\n**5. 写作风格**\n- 检查 AI 写作痕迹（em-dash、-ing phrases、过度分段）\n- 专有名词是否首次出现即定义\n- Abstract 是否满足 150-250 words 和四个必答问题\n\n### 输出格式\n按以下结构输出审稿意见：\n1. Summary（2-3 句）\n2. Strengths（逐条）\n3. Weaknesses（分 critical / warning / info 三级，逐条）\n4. Round 4 Issue Status（逐条标注 RESOLVED / PARTIALLY_RESOLVED / NOT_RESOLVED）\n5. Missing References（如有）\n6. Questions for Authors\n7. Overall Score（1-10）和 Confidence（1-5）"
  }
}
```

</details>

---


### Tool result

_source line 319 · 2026-05-18T01:50:15.276046+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1675
}
```

</details>

---


### Tool call

_source line 320 · 2026-05-18T01:50:21.255184+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 321 · 2026-05-18T01:50:21.406189+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 322 · 2026-05-18T01:50:27.698201+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-18T01:50:27.798882+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 324 · 2026-05-18T01:50:31.771135+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15"
  }
}
```

</details>

---


### Tool result

_source line 325 · 2026-05-18T01:50:31.872095+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 326 · 2026-05-18T01:50:35.091081+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/agent"
  }
}
```

</details>

---


### Tool result

_source line 327 · 2026-05-18T01:50:35.091588+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/agent. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/sessions/review_director_ae8c68a6.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 328 · 2026-05-18T01:50:38.456692+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_15 -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" | head -20",
  "description": "Find config files in project root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_15 -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" | head -20",
    "description": "Find config files in project root"
  }
}
```

</details>

---


### Tool result

_source line 329 · 2026-05-18T01:50:38.608660+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/idea_generator/ideas.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/global/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/config/resources.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/config/pending_approval_notifications.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 330 · 2026-05-18T01:50:42.523105+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd -maxdepth 3 -name \"*.yaml\" -o -name \"*.yml\" | head -20",
  "description": "Find project-level config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd -maxdepth 3 -name \"*.yaml\" -o -name \"*.yml\" | head -20",
    "description": "Find project-level config files"
  }
}
```

</details>

---


### Tool result

_source line 331 · 2026-05-18T01:50:42.623938+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/manifest.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/experiment_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 332 · 2026-05-18T01:50:47.147595+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15",
  "glob": "*.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15",
    "glob": "*.yaml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 333 · 2026-05-18T01:50:47.147964+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 334 · 2026-05-18T01:50:57.637039+00:00_

外部审稿未配置（`external_review.paperreview_ai.enabled` 未设置），跳过外部审稿线。

**当前状态**: 两位 Reviewer 已收到任务，正在独立审稿中。等待审稿结果返回后进行交叉分享（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 33

## Round 33

2 recorded events


### User

_source line 335 · 2026-05-18T01:55:14.248593+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见 — 方法/实验严谨性

**论文**: "Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model"

---

## 总体评分
**Overall**: 6/10 (Marginally above acceptance threshold)
**Confidence**: 4/5 (Confident in evaluation)
**一句话总结**: 实验框架系统性强，但 L1 ablation 的因果推断存在 per-head normalization 缺陷，削弱了核心贡献(ii)的支撑力度；probe overparameterization 的错误解读亦需修正。

## 官方维度打分（基于 CoRL review form: Originality/Quality/Clarity/Significance/Relevance/Limitations）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Originality | 3/5 | Token-level分解框架对VLA领域有增量贡献，但C1(specialization)本质是架构必然结果，C3(inverted-U)metric-dependent |
| Quality | 3/5 | 三条件控制设计合理，但ablation因果推断有缺陷(per-head normalization)，N/params解读错误 |
| Clarity | 4/5 | 写作清晰，结构合理，metric divergence透明报告 |
| Significance | 3/5 | 对VLA理解有帮助，但缺乏行为验证（无success rate），单模型限制泛化性 |
| Relevance | 4/5 | 直接面向robot learning社区关心的VLA内部机制问题 |
| Limitations | 4/5 | 诚实报告了scope限制和metric依赖性，但未报告ablation normalization问题 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] L1 Ablation 的 3.5× specificity claim 被 per-head normalization 严重削弱

- 具体位置：Section 4.2 (experiments.tex lines 78-82)
- 问题：Ablating 24 dominant heads → +0.059 R²; ablating 8 non-dominant heads (control) → +0.017。论文声称 "3.5× smaller" 证明 graded specificity。但 per-head 归一化后：dominant = 0.059/24 ≈ 0.00246/head，non-dominant = 0.017/8 ≈ 0.00213/head，差异仅 ~15%。若将 non-dominant per-head rate 外推到 24 heads，预期效果 = 24 × 0.00213 = 0.051，观测值 0.059，excess 仅 0.008（16% above generic head-removal baseline）。
- 为什么影响接收：这是 contribution (ii) "VLA fine-tuning front-loads instruction routing" 的唯一因果证据。若不能排除 "removing any 24 heads increases R²" 的 null hypothesis，则 "functional specialization" claim 缺乏因果支撑。
- 建议修改方向：(1) 报告 per-head normalized effect size；(2) 补充 random-subset ablation（随机采样 24/32 heads，重复 k 次）作为恰当的 null baseline；(3) 或将 claim 从 "3.5× specificity" 调整为更保守的表述。

**N2** [critical] N/params ≈ 0.05 被错误解读为 "ensuring adequate training signal"

- 具体位置：Section 4.1 (experiments.tex line 12)
- 问题：MLP probe (4096→256→7) 约有 ~1.05M parameters，N=63,228。N/params ≈ 0.06 意味着数据量仅为参数数的 1/17——严重 overparameterization。Belinkov (2022) 明确指出过高容量 probe 可从任何表征中 decode 信息，降低 probe 结论的解释性。论文声称此 ratio "ensuring adequate training signal" 是错误的。
- 为什么影响接收：(1) 表明作者可能误解 probe methodology 的 selectivity concern；(2) 影响所有 absolute R² 值的可信度。
- 建议修改方向：(1) 承认 overparameterized，说明依赖 early stopping；(2) 补充 linear probe 或小容量 probe baseline；(3) 强调 comparative claims (trained vs. untrained Δ) 不受 absolute R² inflation 影响。

---

## Should-Fix 问题

**W1** [warning] Pretrained Llama-2 condition 的 OOD confound 未讨论
- 位置：Method Section 3.1
- Llama-2 base 从未被训练处理 projected visual tokens，对其而言这是完全 OOD 输入。"language pretraining seeds instruction-attending structure" 的因果解读需弱化。

**W2** [warning] Bootstrap CI 未报告具体数值
- 位置：Table 5 (Appendix), main text experiments.tex line 119
- RSA rise phase Δ=+0.017 的 CI 仅标 "incl. 0"，未给 [lower, upper]。核心 claims 应报告具体 CI bounds。

**W3** [warning] Cross-benchmark 仅限 LIBERO suite 内部
- LIBERO-Goal 和 LIBERO-Spatial 共享 simulator/objects/action space，非真正独立验证。

**W4** [warning] 缺乏行为层面验证
- 位置：Discussion lines 25-26
- 无 policy rollout success rate 数据。对 CoRL 而言，representation→behavior 的连接是核心价值。

---

## 小问题

- N/params 分子分母可能写反（或架构描述与数字矛盾）
- Appendix A.6 single-seed analysis 支撑主文 capacity trade-off narrative，应补 3+ seeds
- Belinkov (2022) 应在 Method 中引用以讨论 probe selectivity

---

## Round 4 Issue Status

| Issue | Status | 证据 |
|-------|--------|------|
| R4-N1: C1 reframe | RESOLVED | Abstract+Intro 已改为 "verify and quantify architecture-expected" |
| R4-N2: RSA+CKA divergence | RESOLVED | Abstract/Intro/Method/Appendix 均有 metric-dependent qualifier |
| R4-N3: 5→50 demos | RESOLVED | 明确写 "50 demonstrations per task (N=63,228)" |
| R4-W2: FDR correction | RESOLVED | "survive FDR correction at 29-30 of 33 layers (Benjamini-Hochberg)" |
| R4-W3: Probe N/capacity | PARTIALLY_RESOLVED | 数字已报告但解读错误 |

---

## Questions for Authors

1. 能否提供 random-subset ablation (随机抽 24 heads ablated, 重复 k 次) 的 R² 变化分布？这能明确 dominant-head specificity 的真实 excess。
2. 是否尝试过 smaller probes (4096→32→7 或 linear)？如果也能 reproduce inverted-U 和 Δ，则大幅增强可信度。
3. Pretrained Llama-2 处理 OOD visual tokens 时，intermediate activations 是否在 reasonable range？
4. 是否有任何 policy rollout 数据（即使 5-10 episodes）？

---

## 主要优势

- 系统性四分析方法 + 三条件控制构成完整方法学模板
- RSA vs CKA divergence 的透明报告体现科学诚信
- Robustness analyses 覆盖充分（distance metric, per-DOF, permutation, seeds, demo subsample, threshold）
- 三条件 gradient 设计优雅（attention routing 在三条件间单调递增）
- Round 4 issues 的 reframing 恰当到位

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 336 · 2026-05-18T01:55:31.391355+00:00_

Reviewer 1 审稿意见已收到。评分 6/10，提出 2 个 critical issues（L1 ablation per-head normalization 缺陷、probe overparameterization 误读）和 4 个 warnings。等待 Reviewer 2 完成后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 34

## Round 34

2 recorded events


### User

_source line 337 · 2026-05-18T01:55:34.205829+00:00_

[Reviewer 1 审稿结果]:
审稿完成。核心发现：

1. **N1 [critical]**: L1 ablation 的 "3.5× specificity" claim 在 per-head normalization 后仅剩 ~15% excess，因果推断被严重削弱
2. **N2 [critical]**: N/params ≈ 0.05 被错误地解读为 "adequate"，实际上 probe 严重 overparameterized（参数量是数据量 17 倍）
3. Round 4 的 5 个旧 issues 中 4 个 RESOLVED，1 个 PARTIALLY_RESOLVED（W3: 数字报告了但解读错误）

Overall score: 6/10，borderline above threshold。主要优势是系统性框架和透明的 metric divergence 报告；主要风险是 ablation 的因果推断力度不足以支撑 contribution (ii) 的 strength。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 338 · 2026-05-18T01:55:41.570315+00:00_

Reviewer 1 审稿已收。等待 Reviewer 2 完成后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 35

## Round 35

6 recorded events


### User

_source line 339 · 2026-05-18T01:56:52.195271+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见 — Round 1

**论文**: "Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model"
**Venue**: CoRL 2026
**审查侧重**: 新颖性/意义 + 相关工作 + Framing + Round 4 修复检查 + 写作风格

---

## 1. Summary

本文对 OpenVLA-7B 在 LIBERO 上进行了系统性的 token 级表征分析，使用 trained/pretrained/untrained 三条件 factorial 设计，结合 cross-instruction probes、attention 分析、RSA 和 functional probes 四种互补方法。核心发现是 VLA fine-tuning 将 instruction routing 从 mid-depth (L9-L16) 前移至 entry-exit pattern (L0-L1, L31)，且训练效果集中在 readout token 而非 image tokens。论文方法论严谨，统计分析充分，对 metric dependence 坦诚（RSA vs CKA 分歧），但受限于单模型单 benchmark 的 scope。

---

## 2. Strengths

**S1. 方法论系统性强。** 四种分析方法（probes, attention, RSA, functional probes）相互验证，三条件 factorial 设计（trained/pretrained/untrained × instruction presence）是本文最大的方法论贡献。这种设计在 VLA 分析文献中尚属首次，能有效隔离 language pretraining 和 VLA fine-tuning 各自的贡献。

**S2. C2 routing finding 是 genuine empirical contribution。** 三条件 routing gradient（0/32 → 9/32 → 24/32 instruction-dominant heads at L1）和 entry-exit pattern 的发现具有真正的新颖性。L1 ablation（dominant heads: +0.059 vs control: +0.017, 3.5× specificity, Section 4.3）提供了因果支持，效果集中在 L1（deeper layers: Δ ≈ 0）进一步确认了 head specialization 的 layer specificity。

**S3. 统计严谨性和 robustness 分析充分。** Bootstrap CIs (10,000 resamples)、LOOCV、permutation tests、distance metric invariance (profile r > 0.989)、seed sensitivity (0.655 ± 0.002)、demonstration subsampling (RSA profile r = 0.97)、threshold sensitivity (30%-70%)、cross-benchmark validation (LIBERO-Spatial) — 对于一篇分析论文来说，robustness 分析的覆盖度达到了高标准。

**S4. 对 metric dependence 的坦诚处理。** 论文明确报告 CKA 与 RSA 产生不同的 layer profiles 和 encoder rankings（Appendix A.1-A.2），没有回避这一分歧，而是将其作为结论的重要 qualifier。这种透明性增强了可信度。

**S5. 写作质量高，AI 痕迹极少。** 全文无 em-dash (—) 或解释性 en-dash (–)，无 AI 典型用词（Moreover/Furthermore/Additionally/Notably/delve/leverage/utilize/facilitate 均未出现）。-ing 分词短语在正文中使用频率在可接受范围内（主要出现在 technical descriptions 中如 "enabling immediate instruction access", "indicating that..."），不构成风格问题。

---

## 3. Weaknesses

### Must-Fix 问题（影响接收决定）

**N1** [critical] **单模型局限性对 C2 generalizability 的根本约束**
- 具体位置：Discussion "Limitations and scope" (Section 5, para 5)；全文 C2 claims
- 问题：C2（entry-exit routing pattern）是本文核心贡献，但仅在 OpenVLA-7B 一个模型上验证。Discussion 用两句话概括了单模型局限（"We study OpenVLA-7B on LIBERO; generalization to other VLAs and backbones remains open"），然后以架构相似性做类推（"shares the dominant VLA design pattern... with RT-2 and π₀"）。但类推不等于验证：(a) RT-2 使用不同的 LLM backbone（PaLM-E），routing pattern 可能完全不同；(b) π₀ 使用 flow matching 而非 autoregressive decoding，entry-exit pattern 的前提（readout token attending to instruction tokens）在其架构中可能不成立；(c) 即使架构相似，不同预训练数据和 fine-tuning 策略可能产生不同的 routing reorganization。Grant et al. 2026 (Action Atlas) 在 6 个 VLAs 上进行分析恰恰表明了 cross-model 验证的可行性和必要性。
- 为什么影响接收：CoRL 社区关心的是 VLA 设计的通用规律。如果 entry-exit pattern 是 OpenVLA-specific 而非 VLA-general 的，则 C2 的 significance 大幅降低。当前的 limitations 描述不足以让读者判断 generalizability risk 的大小。
- 建议修改方向：(1) 在 Limitations 中具体列举哪些架构变量可能改变 routing pattern（backbone size/family, frozen vs unfrozen encoder, action head design, pretraining data）；(2) 明确说明 C2 的 claim scope 为 "demonstrated on OpenVLA-7B" 而非暗示 VLA-general；(3) 如果可能，至少在一个架构不同的 VLA（如 smaller model 或不同 backbone）上跑一个 lightweight 验证。

**N2** [critical] **Discussion "Architectural implications" 段落的 speculative leap 缺乏 behavioral validation**
- 具体位置：Discussion Section 5, "Architectural implications" 段落最后一句
- 问题：该段从 L1 attention ablation 的 representational effect（action probe R² 变化）直接推导出 practical design implication："The concentration of instruction routing at L0-L1 suggests that adapting a VLA's instruction-following behavior may require updating only early-layer attention parameters, rather than full-model fine-tuning." 这个跳跃有两个 gap：(1) probe R² 的变化不等于 behavioral performance（success rate）的变化，论文自己在 Limitations 中承认 "whether the observed routing reorganization translates to behavioral performance differences requires task-level evaluation"；(2) 即使 routing 集中在 early layers，fine-tuning 的效果可能仍然需要 deep layers 的协同更新（论文自身数据显示 L31 也有 18 heads instruction-dominant）。
- 为什么影响接收：这是论文对 CoRL 社区最具 actionable 价值的 claim，但缺乏验证使其停留在 speculation 层面。如果审稿人以此为 contribution 接受论文，后续无法 reproduce 这个 design implication 会是问题。
- 建议修改方向：(1) 将 "suggests" 改为更弱的措辞（如 "raises the hypothesis that..."）；(2) 明确标注这是 speculative interpretation 而非 evidence-supported conclusion；(3) 指出 L31 的 re-engagement (18 heads) 对这一 implication 构成的 complication。

### Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **C1 的 contribution 定位仍有模糊之处**
- 具体位置：Introduction contributions list (i)；Abstract 第 4 句
- 问题：C1 已从 "finding" 重新定位为 "experimental framework + empirical verification"，这是正确的方向。但 contributions list (i) 混合了两个层次：框架贡献（"a systematic experimental framework for token-level representational analysis"）和验证结果（"verifying architecture-expected specialization"）。对于 CoRL 审稿人来说，"验证架构预期的东西" 本身作为 contribution 的说服力有限，因为 causal mask + frozen encoder 的逻辑是先验显然的。建议在 (i) 中更强调框架的 reusability（可以应用于其他 VLAs / 不同架构），将验证结果作为框架的 demonstration 而非独立贡献。
- 建议：Rewrite (i) to foreground the framework's applicability to future VLAs and downplay the verification as a demonstration case.

**W2** [warning] **C3 non-monotonic observation 的贡献权重与证据强度不匹配**
- 具体位置：Abstract 第 6 句；Introduction 第 20 行；Section 4.4
- 问题：C3 在 Abstract 和 Introduction 中获得了与 C1、C2 等量的篇幅，但它的 evidence 是 metric-dependent 的（RSA shows inverted-U, CKA shows monotonic increase）。论文正确标注了这一分歧，但在呈现顺序上，inverted-U 仍作为主结论，CKA 作为 qualifier 放在句末。对于一个核心结论被另一种标准方法直接否定的 finding，当前的权重分配可能 overclaim 其 robustness。
- 建议：在 Abstract 中缩减 C3 篇幅，将节省空间用于 C2 的 detail（如 ablation evidence），或将 metric divergence 前置为 C3 statement 的一部分而非后置 qualifier。

**W3** [warning] **Related Work 缺少 causal tracing / activation patching 相关文献**
- 具体位置：Section 2 "Mechanistic interpretability in transformers" 段落
- 问题：Related Work 覆盖了 residual stream framework (Elhage 2021)、induction heads (Olsson 2022)、circuit discovery (Wang 2023, Conmy 2023)、attention probing (Clark 2019, Vig 2019, Voita 2019)。但缺少了 mechanistic interpretability 中另一个重要方向：causal tracing / activation patching (Meng et al. 2022, "Locating and Editing Factual Associations in GPT", NeurIPS; Goldowsky-Dill et al. 2023, "Localizing Model Behavior with Path Patching")。这些方法与本文的 L1 ablation 在方法论上直接相关（都是通过 intervention 建立因果关系），不引用会让审稿人质疑方法论 awareness。
- 建议：在 "Mechanistic interpretability" 段落中加入 activation patching / causal tracing 的引用，并说明本文的 ablation 方法与其的关系（如 本文的 attention ablation 是一种 targeted intervention，与 activation patching 的思路一致但 granularity 不同）。

**W4** [warning] **Related Work 缺少 tuned lens 等 logit lens 后续工作**
- 具体位置：Section 2 "Token-level functional specialization" 段落
- 问题：论文引用了 nostalgebraist 2020 (logit lens)，但 logit lens 有已知的 representation misalignment 问题，tuned lens (Belrose et al. 2023, "Eliciting Latent Predictions from Transformers with the Tuned Lens", NeurIPS 2023 Workshop → 后续 full paper) 是直接改进。本文的 per-layer probe analysis 在精神上更接近 tuned lens（per-layer 学习映射到 output space），不引用这个 closely related method 是遗漏。
- 建议：引用 tuned lens，说明 per-layer MLP probes 与 tuned lens 的联系（都学习 per-layer 映射），但本文的 target 是 action space 而非 vocabulary。

**W5** [warning] **conclusion.tex 存在但未被 main.tex \input**
- 具体位置：main.tex 未包含 conclusion.tex；conclusion.tex 为 6 行独立文件
- 问题：conclusion.tex 存在，包含一段 3 句话的 Conclusion section (Section label `\ref{sec:conclusion}`)，但 main.tex 中未 `\input{conclusion}`。Discussion 以 "Limitations and scope" 段落结尾。CoRL 不强制要求 Conclusion section，但 (a) 未使用的文件暗示编辑遗漏；(b) Discussion 结尾以 limitations 收束，叙事上以消极信息结尾不理想；(c) conclusion.tex 的内容（3 句精炼总结 + code release 承诺）适合作为论文结尾。
- 建议：将 conclusion.tex 整合到 Discussion 末尾或作为独立 section 加入 main.tex。

### 小问题（不影响接收）

**I1** [info] **Abstract 词数偏高（~241 words raw LaTeX）。** CoRL 未明确规定 abstract 词数上限，但渲染后可能超过 250 words（考虑 LaTeX 公式展开）。建议自查渲染后词数。

**I2** [info] **-ing 分词短语数量较多。** 正文中有约 15+ 处 ", enabling/indicating/confirming/suggesting/revealing/showing..." 模式。虽不构成严重 AI 痕迹（无其他 AI markers），但 pattern 的密度偏高。建议在 final pass 中将部分改写为独立句子。

**I3** [info] **References 数量 (29) 处于 CoRL 论文的中等偏低水平。** CoRL 2024 accepted papers 的引用中位数约 35-45。当前覆盖度合理但不充裕，特别是在加入 W3/W4 建议的引用后仍有空间。

---

## 4. Round 4 Issue Status

| Issue | Status | 说明 |
|-------|--------|------|
| **R4-N1** C1 reframe (finding → framework+verification) | **RESOLVED** | Abstract: "we verify and quantify architecture-expected token specialization"; Introduction: "consistent with architectural expectations"; Contributions (i): "systematic experimental framework...verifying architecture-expected specialization". Reframe 到位。 |
| **R4-W1** RSA best-vs-best n.s. 标注 | **RESOLVED** | Abstract: "Δρ ≤ 0.017, non-significant"; Introduction: "non-significant geometric gain (Δρ = 0.017, 3%)". 两处均明确标注。 |
| **R4-W4** Frozen encoder confound caveat | **RESOLVED** | Introduction line 16: "consistent with the causal mask and frozen encoder"; Discussion: 明确列出 "frozen vision encoder" 作为 shared design pattern. C1 的 instruction-blindness 被正确归因为架构特性而非 learned property。 |
| **R4-W5** 单模型局限性展开 | **PARTIALLY_RESOLVED** | Discussion 提到 "generalization to other VLAs and backbones remains open" 并给出架构类推。但如 N1 所述，类推论证不足以覆盖架构差异可能带来的 routing pattern 变化。需更具体地列举潜在 confounds。 |
| **R4-W7** Introduction "untested assumption" straw man | **RESOLVED** | Introduction 使用 "remains uncharacterized" (line 5) 和 "opaque" (line 9)，无 straw man 语言。Related Work 中 "A central assumption" 是对领域的客观描述，不构成 straw man。 |
| **R4-I1** conclusion.tex 整合 | **NOT_RESOLVED** | conclusion.tex (6 行) 存在但未被 main.tex \input。见 W5。 |

---

## 5. Missing References

| 类别 | 缺失引用 | 重要性 |
|------|----------|--------|
| Causal tracing / activation patching | Meng et al. 2022 "Locating and Editing Factual Associations in GPT" (NeurIPS) | **High** — 与本文 L1 ablation 方法论直接相关 |
| Causal tracing | Goldowsky-Dill et al. 2023 "Localizing Model Behavior with Path Patching" | Medium — 更全面的 patching methodology |
| Logit lens improvement | Belrose et al. 2023 "Eliciting Latent Predictions from Transformers with the Tuned Lens" | **High** — 与 per-layer probing 方法论紧密相关 |
| Other VLA architectures | Ghosh et al. 2024 "Octo: An Open-Source Generalist Robot Policy" | Low — 讨论 generalizability 时作为不同架构的例子 |

---

## 6. Questions for Authors

**Q1.** C2 的 entry-exit pattern 是否可能是 Llama-2 7B 这一特定 backbone 的 artifact？如果使用不同的 LLM backbone（如 Mistral 或 Phi），是否预期同样的 routing reorganization？请提供架构层面的论证。

**Q2.** L1 ablation 显示 dominant head removal 增加 action R² (+0.059)。这意味着 instruction routing heads 在 action encoding 上有 cost。是否测量过这种 ablation 对 instruction-following accuracy 的影响（即 cross-instruction classification accuracy 是否下降）？这将完善 capacity trade-off 的论证。

**Q3.** Discussion 提出 early-layer-only fine-tuning 的 design implication。是否考虑过做一个简单验证：只 fine-tune L0-L1 的 attention parameters，比较其与 full fine-tuning 的 behavioral performance？即使只在 LIBERO 上做，也能显著增强这个 claim。

**Q4.** 29 篇引用对 CoRL 论文偏少。作者是否有意控制引用数量？是否考虑过加入 activation patching (Meng et al. 2022) 和 tuned lens (Belrose et al. 2023)？

---

## 7. Overall Assessment

**Overall Score: 6/10 — Marginally above acceptance threshold**

**Confidence: 4/5 — Confident but not absolutely certain**

**一句话总结**: 方法论严谨的 VLA 分析论文，C2 routing finding 有真正的新颖性，但单模型 scope 和 speculative design implications 限制了对 CoRL 社区的实际指导价值。

### 官方维度打分（基于 CoRL review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Originality** | 6/10 | C2 (entry-exit routing) 是 genuine novel finding；C1 (framework) 有方法论价值但验证结果是预期的；C3 (non-monotonic) 被 metric dependence 削弱。与 Grant 2026 (6 models, feature-level) 相比，本文 depth > breadth。 |
| **Quality** | 7/10 | 统计分析严谨（bootstrap, LOOCV, permutation, robustness suite）；factorial 设计得当；metric dependence 坦诚报告。扣分：单模型、无 behavioral validation、speculative design implications。 |
| **Clarity** | 8/10 | 写作清晰，结构合理，几乎无 AI 痕迹。Abstract 四要素齐全。-ing phrases 稍多但不影响可读性。conclusion.tex 未整合是小问题。 |
| **Significance** | 5/10 | 核心问题：对 CoRL 社区的 practical impact 有限。C2 的 routing finding 有启发性但无 behavioral validation，design implications 是 speculative 的。单模型 scope 进一步限制 significance。如果能在第二个 VLA 上验证 C2 或做一个 early-layer fine-tuning 实验，significance 可提升至 7。 |
| **Relevance** | 8/10 | 直接分析 VLA 内部机制，完全在 CoRL scope 内。理解 VLA 内部工作原理对 robotics community 有长期价值。 |
| **Limitations** | 7/10 | 主要限制已报告（单模型、metric dependence、无 behavioral validation）。但单模型局限性的讨论不够具体（见 N1），frozen encoder confound 的 generalizability implications 可以更详细。 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 340 · 2026-05-18T01:57:30.814635+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的意见。对每条使用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n### Must-Fix (Critical)\n\n**R2-N1** [critical] 单模型局限性对 C2 generalizability 的根本约束\n- C2（entry-exit routing pattern）仅在 OpenVLA-7B 一个模型上验证\n- Discussion 以架构相似性类推（RT-2, π₀），但类推不等于验证：RT-2 用 PaLM-E backbone，π₀ 用 flow matching 非 autoregressive\n- Grant et al. 2026 在 6 个 VLAs 上分析，表明 cross-model 验证可行\n- 建议：Limitations 中具体列举哪些架构变量可能改变 routing pattern\n\n**R2-N2** [critical] Discussion \"Architectural implications\" 段的 speculative leap\n- 从 L1 ablation 的 representational effect 直接推导 design implication：\"adapting instruction-following behavior may require updating only early-layer attention parameters\"\n- 两个 gap：(1) probe R² ≠ behavioral performance；(2) L31 也有 18 heads instruction-dominant，说明 deep layers 也参与\n- 建议：弱化措辞 + 标注 speculative + 指出 L31 complication\n\n### Should-Fix (Warning)\n\n**R2-W1** C1 contribution 定位仍有模糊：contributions (i) 混合框架贡献和验证结果，\"验证预期结果\"作为独立 contribution 说服力有限\n**R2-W2** C3 non-monotonic observation 在 Abstract/Intro 获得与 C1/C2 等量篇幅，但 metric-dependent evidence 不支撑这个权重\n**R2-W3** Related Work 缺少 causal tracing / activation patching 文献（Meng et al. 2022, Goldowsky-Dill et al. 2023）\n**R2-W4** Related Work 缺少 tuned lens（Belrose et al. 2023），与 per-layer probing 方法论紧密相关\n**R2-W5** conclusion.tex 存在但未被 main.tex \\input（R4-I1 NOT_RESOLVED）\n\n### Info\n\n**R2-I1** Abstract 词数偏高（~241 words）\n**R2-I2** -ing 分词短语约 15+ 处\n**R2-I3** References 29 篇处于 CoRL 中等偏低\n\n### R2 评分\n- Overall: 6/10\n- Originality: 6/10, Quality: 7/10, Clarity: 8/10, Significance: 5/10, Relevance: 8/10, Limitations: 7/10\n\n请逐条回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的意见。对每条使用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n### Must-Fix (Critical)\n\n**R2-N1** [critical] 单模型局限性对 C2 generalizability 的根本约束\n- C2（entry-exit routing pattern）仅在 OpenVLA-7B 一个模型上验证\n- Discussion 以架构相似性类推（RT-2, π₀），但类推不等于验证：RT-2 用 PaLM-E backbone，π₀ 用 flow matching 非 autoregressive\n- Grant et al. 2026 在 6 个 VLAs 上分析，表明 cross-model 验证可行\n- 建议：Limitations 中具体列举哪些架构变量可能改变 routing pattern\n\n**R2-N2** [critical] Discussion \"Architectural implications\" 段的 speculative leap\n- 从 L1 ablation 的 representational effect 直接推导 design implication：\"adapting instruction-following behavior may require updating only early-layer attention parameters\"\n- 两个 gap：(1) probe R² ≠ behavioral performance；(2) L31 也有 18 heads instruction-dominant，说明 deep layers 也参与\n- 建议：弱化措辞 + 标注 speculative + 指出 L31 complication\n\n### Should-Fix (Warning)\n\n**R2-W1** C1 contribution 定位仍有模糊：contributions (i) 混合框架贡献和验证结果，\"验证预期结果\"作为独立 contribution 说服力有限\n**R2-W2** C3 non-monotonic observation 在 Abstract/Intro 获得与 C1/C2 等量篇幅，但 metric-dependent evidence 不支撑这个权重\n**R2-W3** Related Work 缺少 causal tracing / activation patching 文献（Meng et al. 2022, Goldowsky-Dill et al. 2023）\n**R2-W4** Related Work 缺少 tuned lens（Belrose et al. 2023），与 per-layer probing 方法论紧密相关\n**R2-W5** conclusion.tex 存在但未被 main.tex \\input（R4-I1 NOT_RESOLVED）\n\n### Info\n\n**R2-I1** Abstract 词数偏高（~241 words）\n**R2-I2** -ing 分词短语约 15+ 处\n**R2-I3** References 29 篇处于 CoRL 中等偏低\n\n### R2 评分\n- Overall: 6/10\n- Originality: 6/10, Quality: 7/10, Clarity: 8/10, Significance: 5/10, Relevance: 8/10, Limitations: 7/10\n\n请逐条回应。"
  }
}
```

</details>

---


### Tool result

_source line 341 · 2026-05-18T01:57:53.287672+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22473
}
```

</details>

---


### Tool call

_source line 342 · 2026-05-18T01:57:53.438699+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的意见。对每条使用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n### Must-Fix (Critical)\n\n**R1-N1** [critical] L1 Ablation 的 3.5× specificity claim 被 per-head normalization 严重削弱\n- Ablating 24 dominant heads → +0.059 R²; ablating 8 non-dominant heads → +0.017\n- Per-head: dominant = 0.059/24 ≈ 0.00246, non-dominant = 0.017/8 ≈ 0.00213, 差异仅 ~15%\n- 外推 24 heads at non-dominant rate = 0.051, 观测值 0.059, excess 仅 0.008 (16%)\n- 建议：报告 per-head normalized effect; 补充 random-subset ablation (随机 24/32 heads, k 次); 或弱化 claim\n\n**R1-N2** [critical] N/params ≈ 0.05 被错误解读为 \"ensuring adequate training signal\"\n- MLP probe (4096→256→7) 约 1.05M params, N=63,228\n- N/params ≈ 0.06 → 参数量是数据量 17 倍 → 严重 overparameterization\n- Belinkov 2022: 过高容量 probe 可从任何表征 decode 信息\n- 建议：承认 overparameterized + 依赖 early stopping; 补充 linear/small probe baseline; 强调 Δ 不受 absolute R² inflation 影响\n\n### Should-Fix (Warning)\n\n**R1-W1** Pretrained Llama-2 condition 的 OOD confound 未讨论：Llama-2 从未被训练处理 projected visual tokens，对其而言是 OOD 输入\n**R1-W2** Bootstrap CI 未报告具体数值：RSA rise phase Δ=+0.017 仅标 \"incl. 0\"，未给 [lower, upper]\n**R1-W3** Cross-benchmark 仅限 LIBERO suite 内部（shared simulator/objects/action space）\n**R1-W4** 缺乏行为层面验证（无 policy rollout success rate）\n\n### Info\n- N/params 分子分母可能写反\n- Appendix A.6 single-seed analysis 应补 3+ seeds\n- Belinkov 2022 应在 Method 中引用\n\n### R1 评分\n- Overall: 6/10\n- Originality: 3/5, Quality: 3/5, Clarity: 4/5, Significance: 3/5, Relevance: 4/5, Limitations: 4/5\n\n### Round 4 Issue Status (R1 判断)\n- R4-N1 C1 reframe: RESOLVED\n- R4-N2 RSA+CKA divergence: RESOLVED\n- R4-N3 5→50 demos: RESOLVED\n- R4-W2 FDR correction: RESOLVED\n- R4-W3 Probe N/capacity: PARTIALLY_RESOLVED (数字报告了但解读错误)\n\n请逐条回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的意见。对每条使用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n### Must-Fix (Critical)\n\n**R1-N1** [critical] L1 Ablation 的 3.5× specificity claim 被 per-head normalization 严重削弱\n- Ablating 24 dominant heads → +0.059 R²; ablating 8 non-dominant heads → +0.017\n- Per-head: dominant = 0.059/24 ≈ 0.00246, non-dominant = 0.017/8 ≈ 0.00213, 差异仅 ~15%\n- 外推 24 heads at non-dominant rate = 0.051, 观测值 0.059, excess 仅 0.008 (16%)\n- 建议：报告 per-head normalized effect; 补充 random-subset ablation (随机 24/32 heads, k 次); 或弱化 claim\n\n**R1-N2** [critical] N/params ≈ 0.05 被错误解读为 \"ensuring adequate training signal\"\n- MLP probe (4096→256→7) 约 1.05M params, N=63,228\n- N/params ≈ 0.06 → 参数量是数据量 17 倍 → 严重 overparameterization\n- Belinkov 2022: 过高容量 probe 可从任何表征 decode 信息\n- 建议：承认 overparameterized + 依赖 early stopping; 补充 linear/small probe baseline; 强调 Δ 不受 absolute R² inflation 影响\n\n### Should-Fix (Warning)\n\n**R1-W1** Pretrained Llama-2 condition 的 OOD confound 未讨论：Llama-2 从未被训练处理 projected visual tokens，对其而言是 OOD 输入\n**R1-W2** Bootstrap CI 未报告具体数值：RSA rise phase Δ=+0.017 仅标 \"incl. 0\"，未给 [lower, upper]\n**R1-W3** Cross-benchmark 仅限 LIBERO suite 内部（shared simulator/objects/action space）\n**R1-W4** 缺乏行为层面验证（无 policy rollout success rate）\n\n### Info\n- N/params 分子分母可能写反\n- Appendix A.6 single-seed analysis 应补 3+ seeds\n- Belinkov 2022 应在 Method 中引用\n\n### R1 评分\n- Overall: 6/10\n- Originality: 3/5, Quality: 3/5, Clarity: 4/5, Significance: 3/5, Relevance: 4/5, Limitations: 4/5\n\n### Round 4 Issue Status (R1 判断)\n- R4-N1 C1 reframe: RESOLVED\n- R4-N2 RSA+CKA divergence: RESOLVED\n- R4-N3 5→50 demos: RESOLVED\n- R4-W2 FDR correction: RESOLVED\n- R4-W3 Probe N/capacity: PARTIALLY_RESOLVED (数字报告了但解读错误)\n\n请逐条回应。"
  }
}
```

</details>

---


### Tool result

_source line 343 · 2026-05-18T01:57:55.004615+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1565
}
```

</details>

---


### Assistant

_source line 344 · 2026-05-18T01:57:57.658223+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 36

## Round 36

2 recorded events


### User

_source line 345 · 2026-05-18T01:58:00.365192+00:00_

[Reviewer 2 审稿结果]:
Round 1 审稿完成，已汇报给 Director。

核心判断：**6/10，marginally above threshold**。

- **最大优势**：C2 routing finding（entry-exit pattern + 三条件 gradient）有真正的新颖性，方法论严谨，统计分析充分
- **两个 critical issues**：(N1) 单模型 scope 对 C2 generalizability 的根本约束，当前 Limitations 讨论不够具体；(N2) Discussion 的 "early-layer-only fine-tuning" design implication 缺乏 behavioral validation，属 speculative leap
- **Round 4 修复状态**：R4-N1/W1/W4/W7 已 RESOLVED；R4-W5 PARTIALLY_RESOLVED（单模型局限讨论不够具体）；R4-I1 NOT_RESOLVED（conclusion.tex 未整合）
- **缺失引用**：Meng et al. 2022 (activation patching) 和 Belrose et al. 2023 (tuned lens) 应补充
- **写作风格**：无 AI 痕迹，质量高

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 346 · 2026-05-18T01:58:05.940368+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 37

## Round 37

2 recorded events


### User

_source line 347 · 2026-05-18T01:59:27.331130+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 意见的交叉回应

---

### Must-Fix

**[AGREE] R2-N1**: 单模型局限性。同意类推不等于验证（RT-2 用 PaLM-E, π₀ 用 flow matching）。但 contribution claim 已限定 "demonstrated on OpenVLA-7B/LIBERO" (Intro line 23)，我倾向将此降为 strong warning 而非 critical。建议 Limitations 应具体列举可能改变 routing 的架构变量（token ordering, decoder type, backbone scale, projector arch）。

**[AGREE] R2-N2**: Architectural implications speculative leap。完全同意。probe R² ≠ behavioral performance，且 L31 的 18 heads (Fig 1, experiments.tex line 69) 直接矛盾 "only early-layer" 的暗示。应标注 speculative + 讨论 L31 complication。

### Should-Fix

**[REBUT] R2-W1**: C1 contribution 定位。部分不同意——experimental framework 本身（四方法 × 三条件 × 两 token × 32层 grid）有独立方法学贡献，prior work 均未做此 systematic verification。但同意"混合框架和验证"的措辞可改进。

**[AGREE] R2-W2**: C3 权重过高。RSA inverted-U 在 CKA 下不成立 (Appendix A.2)，不应与 C2（跨 threshold/条件一致）等权呈现。

**[AGREE] R2-W3/W4**: 缺 causal tracing + tuned lens。均为 Related Work 的实质 gap。

**[AGREE] R2-W5**: conclusion.tex 遗漏。低严重性，Discussion 已覆盖。

### Info

**[AGREE] R2-I1/I2**: 非关键。
**[REBUT] R2-I3**: 29 篇数量本身不是问题，实际 gap 是 W3/W4 指出的具体文献缺失（补充后 ~31-33 篇，合理）。

### 与 R2 的关键分歧

1. R2 给 Quality 7/10，我给 3/5。我认为 ablation per-head normalization 问题（我的 N1）比 R2 的评估更严重——3.5× claim 归一化后仅 ~15% excess，这是 C2 因果证据的核心缺陷。R2 似乎未注意到此问题。
2. R2 将单模型定为 critical，我倾向 strong warning（scope 已限定）。但这取决于 AC 是否认为 CoRL 期望 cross-model validation。

### 综合判断

两位 reviewer 均给 6/10，核心担忧不同但互补：R2 关注 generalizability + speculation，我关注 statistical validity + causal inference。若两组 critical issues 都需 must-fix，论文工作量较大但不是不可能（random ablation baseline + framing 修正 + Limitations 扩展）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 348 · 2026-05-18T01:59:40.389151+00:00_

收到 Reviewer 1 的交叉回应。等待 Reviewer 2 对 Reviewer 1 意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 38

## Round 38

2 recorded events


### User

_source line 349 · 2026-05-18T01:59:45.099633+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

核心判断：与 R2 一致程度高（7/10 条 AGREE），主要分歧在 C1 框架贡献的独立价值（我认为 R2 低估）和引用数量问题（gap 比数量重要）。两人均给 6/10 但关注点互补——R2 侧重 generalizability，我侧重 statistical/causal rigor。最大的未被 R2 发现的问题是 ablation per-head normalization（我的 N1）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 350 · 2026-05-18T01:59:50.761526+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 39

## Round 39

8 recorded events


### User

_source line 351 · 2026-05-18T02:00:19.443105+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix (Critical)

**[AGREE] R1-N1: L1 Ablation 的 3.5× specificity claim 被 per-head normalization 削弱**

R1 的 per-head 分析是有效的。24 dominant heads 产生 +0.059（per-head ≈ 0.00246），8 non-dominant heads 产生 +0.017（per-head ≈ 0.00213），per-head 差异仅约 15%。外推 24 heads at non-dominant rate 得到 0.051，与观测值 0.059 的 excess 仅 0.008（16%），远弱于 "3.5×" 的表面印象。

论文原文（Section 4.3）："Ablating 8 non-dominant heads (control) yields +0.017, 3.5× smaller than the dominant-head effect, confirming a graded specificity rather than a generic attention-removal artifact." 这里的 "3.5×" 混淆了 head 数量差异和 per-head specificity。

不过我认为需补充两点 nuance：
1. 论文还报告了 "specificity contrast is significant (dominant − control = +0.042, p < 0.0001)"（Section 4.3, line 81）。这个 total difference 的 p-value 是关于 aggregate 效果的统计检验，本身没问题，问题在于 "3.5×" 的 framing 暗示 per-head specificity 远大于实际。
2. 更关键的 specificity 证据来自 layer confinement：L1 effect = +0.059, L8 = +0.018, L13 ≈ 0（Section 4.3, line 82）。这个 layer gradient 不受 head 数量 confound 的影响，是更干净的 specificity 证据。

**建议：** 同意 R1 的修改方向。作者应 (a) 报告 per-head normalized effect；(b) 弱化 "3.5×" 为 "aggregate effect comparison"；(c) 将 layer confinement 作为 specificity 的主要证据而非 head-count comparison。R1 建议的 random-subset ablation 是理想方案但可能 scope 过大。

---

**[AGREE] R1-N2: N/params ≈ 0.05 被错误解读**

R1 的计算正确。MLP probe (4096→256→7) 参数量：
- Layer 1: 4096×256 + 256 = 1,048,832
- Layer 2: 256×7 + 7 = 1,799
- Total ≈ 1.05M params

N = 63,228, 所以 N/params ≈ 0.06，即参数量是数据量的 ~17 倍。论文称此 "ensuring adequate training signal"（Section 4.1, line 12）是错误的——这是严重 overparameterized 的 regime。

R1 的 Info section 指出 "N/params 分子分母可能写反" 也是合理推测。即使 params/N ≈ 17，这同样表明 overparameterization 而非 adequate signal。

关键缓解因素：
1. 论文使用 early stopping (patience 5)（Section 3.5），这在 overparameterized probes 中是标准 regularization
2. 核心 claims 基于 Δ (trained vs untrained) 而非 absolute R²，如 R1 所指出的，Δ 不受 absolute inflation 影响（假设 overfitting degree 在 conditions 间相似）
3. Seed sensitivity 分析（Appendix A.9）显示 R² 跨 seed 标准差 < 0.01，表明结果不是 overfit artifact

**建议：** 同意 R1 的全部修改建议。(a) 修正 "ensuring adequate training signal" 为 "the probe is overparameterized (N/params ≈ 0.06); we rely on early stopping for regularization"；(b) 补充 linear probe 或 smaller MLP (64 hidden) baseline 以验证 conclusions 对 probe capacity 的 robustness；(c) 在 Method 中引用 Belinkov 2022 讨论 probe complexity-capability tradeoff。

---

### Should-Fix (Warning)

**[AGREE] R1-W1: Pretrained Llama-2 OOD confound**

有效的方法论关切。Llama-2 base 从未见过 visual tokens（来自 DinoSigLIP projector 的 4096-D vectors），其 routing 行为可能反映 OOD 处理策略（如 default 到最近的 known distribution）而非对 visual input 的 genuine 处理。

这不完全否定三条件比较的价值——pretrained condition 的意义恰恰在于展示 language pretraining 单独在面对 multimodal input 时贡献了什么（Section 3.1, line 12-13 描述了设计意图）。但论文应明确讨论这一 confound：
- L1 的 9/32 instruction-dominant heads（Table 2）可能反映 Llama-2 对 unfamiliar input 的 default 行为（attention fallback 到 known token types 即 instruction tokens），而非 language pretraining 对 instruction routing 的真正 "seeding"
- 这会影响 C2 的叙事：当前 "language pretraining seeds instruction routing, VLA fine-tuning amplifies it" 的故事可能过于 clean

**补充我的 review 未涉及的角度：** 如果 OOD confound 成立，那么 untrained → pretrained 的变化（0/32 → 9/32 heads）可能主要反映 trained weights 对 OOD inputs 的 generic response 而非 instruction-specific routing learning。这进一步加强了我在 N1 中对 single-model generalizability 的担忧。

---

**[AGREE] R1-W2: Bootstrap CI 未报告具体数值**

论文多处仅标注 "95% CI includes zero"（如 Table 5: RSA best-vs-best Δ=+0.017）或 "95% CI excludes zero"，但未给出 [lower, upper] 区间。这是统计报告的基本规范问题。Section 4.4, line 125: "best-vs-best gain is non-significant (Δ = +0.017, 3%, 95% CI includes zero; Appendix Table 5)" —— Appendix Table 5 同样只写 "incl. 0" 和 "excl. 0"。

补充：LIBERO-Spatial 的 CI 报告更完整：Appendix A.7, line 123 给出了 "95% CI [0.012, 0.036]"。这种不一致性使得主实验的 CI 缺失更加显眼。

---

**[AGREE] R1-W3: Cross-benchmark 局限于 LIBERO suite**

LIBERO-Goal 和 LIBERO-Spatial 共享 simulator (MuJoCo)、object set 和 7-D action space，cross-benchmark validation 的力度有限。Appendix A.7 指出 Spatial 是 "out-of-distribution tasks requiring spatial reasoning"，但 OOD 仅在 task semantics 层面，底层 environment dynamics 完全相同。

此问题与我 review 中的 N1（单模型 scope）性质相同，从不同角度指出了 generalizability 的局限。在可操作性上，考虑到 deadline (2026-05-29)，在不同 simulator 上做 cross-benchmark 不太现实，但可以在 Limitations 中更明确地区分 "task-level generalization"（已测试）和 "environment-level generalization"（未测试）。

---

**[AGREE] R1-W4: 缺乏行为层面验证**

与我 review 中的 N2 一致。论文 Discussion (Section 5, Limitations para) 自己承认 "whether the observed routing reorganization translates to behavioral performance differences requires task-level evaluation beyond this work"。这个 gap 同时削弱了 C2 的 practical significance 和 "Architectural implications" 段落的 design suggestion。

---

### Info

**[AGREE] N/params 分子分母可能写反：** 见 R1-N2 分析。

**[AGREE] Appendix A.6 single-seed analysis 应补 3+ seeds：** Appendix A.6 (Figure 7) 的 three-condition action R² comparison 使用 single seed（该 section 最后一句 "This analysis uses a single seed without confidence intervals and should be interpreted as a supplementary observation"）。既然 main results 有 5-seed sensitivity analysis (Appendix A.9, Table 8)，A.6 没有理由不做同样的处理。

**[AGREE] Belinkov 2022 应在 Method 中引用：** 当前 Belinkov 2022 仅在 Related Work (Section 2) 和 Method Section 3.5 的 citation list 中出现 ([alain2017,hewitt2019,belinkov2022])。但 probe complexity 的讨论（如 R1-N2 所指出的 overparameterization 问题）应在 Method 中有明确段落讨论 probe design choices 和 complexity-capability tradeoff。

---

### R1 Round 4 Issue Status 的回应

| R1 判断 | 我的判断 | 说明 |
|---------|---------|------|
| R4-N1 C1 reframe: RESOLVED | **一致** | C1 已从 "finding" 重新定位为 "framework + verification"。 |
| R4-N2 RSA+CKA divergence: RESOLVED | **一致** | 论文在 Abstract、Introduction、Section 4.4、Appendix 中均明确报告了 metric divergence。 |
| R4-N3 5→50 demos: RESOLVED | **一致** | 当前使用 50 demonstrations per task (Section 3.1)，subsample sensitivity 在 Appendix A.10 中报告。 |
| R4-W2 FDR correction: RESOLVED | **一致** | Section 4.4, line 127: "Benjamini-Hochberg, Wilcoxon signed-rank, n=10 tasks" 有明确 FDR 报告。 |
| R4-W3 Probe N/capacity: PARTIALLY_RESOLVED | **一致** | 数字已报告但解读错误（R1-N2）。 |

---

### R1 评分的回应

R1 Overall: 6/10。我的 Overall: 6/10。**一致。**

维度层面：
- Originality: R1 给 3/5，我给 6/10（等价 3/5）。**一致。**
- Quality: R1 给 3/5。我给 7/10（≈3.5/5）。**我略高。** 原因：我认为 statistical rigor（bootstrap, LOOCV, permutation, robustness suite）是质量的加分项，值得肯定，尽管 R1-N1 和 R1-N2 是有效的质量问题。
- Clarity: R1 给 4/5，我给 8/10（4/5）。**一致。**
- Significance: R1 给 3/5，我给 5/10（2.5/5）。**我略低。** 原因：单模型 scope 对 CoRL 社区的 practical impact 构成更严重的限制。
- Relevance: R1 给 4/5，我给 8/10（4/5）。**一致。**

---

### 总结

R1 和 R2 在所有 critical issues 上形成一致：
1. **Ablation specificity claim 需要修正**（R1-N1，R2 同意）
2. **Probe overparameterization 需要承认和补充**（R1-N2，R2 同意）
3. **单模型 scope 限制 significance**（R2-N1，R1 隐含于 Significance 评分）
4. **Design implications 缺乏 behavioral validation**（R2-N2 = R1-W4）

主要分歧：R1 在 Quality 上比我更严格（3/5 vs 我的 3.5/5），原因是 R1 更侧重方法论细节问题（N1, N2），而我更多考虑了整体 statistical apparatus 的充分性。

**综合判断维持 6/10（marginally above threshold）。** 如果作者在 rebuttal 中能 (a) 修正 ablation framing, (b) 承认 probe overparameterization 并补充 linear probe baseline, (c) 充实 single-model limitations，论文有条件接收。最大风险是 significance——如果审稿人认为单模型分析论文对 CoRL 社区的指导价值有限，可能从 borderline 滑向 reject。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 352 · 2026-05-18T02:00:51.408584+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 353 · 2026-05-18T02:00:51.459230+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 354 · 2026-05-18T02:03:33.211805+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "vla-ssd",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-3 历史 issues（全部 resolved）\n  # ============================================================\n  - id: R1-N1-old\n    summary: \"Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识。需增加 Llama-2 base checkpoint 作为中间对照\"\n      - round: 2\n        reviewers: [1, 2, 3]\n        note: \"PARTIALLY_RESOLVED: acknowledge confound 但无数据\"\n    action_items:\n      - round: 1\n        action: \"增加 Llama-2 base checkpoint 对照实验\"\n        assigned_to: research\n        status: done\n      - round: 2\n        action: \"Section 标题改为观察性；Abstract 弱化 causal attribution\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"B版本完整整合三条件数据：untrained 0/32, Llama-2 base 9/32, trained 25/32 heads。§4.3 以三条件梯度为核心证据，Table 2 + Figure 4 呈现完整 32 层 profile。\"\n    resolution_round: 3\n\n  - id: R1-N2-old\n    summary: \"单一模型(OpenVLA-7B) + 单一 benchmark family(LIBERO)，Title/Abstract 使用复数 'VLAs' 构成 overclaim\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识\"\n      - round: 2\n        reviewers: [1, 2, 3]\n        note: \"PARTIALLY_RESOLVED: Abstract 限定但 Title 仍复数\"\n    action_items:\n      - round: 2\n        action: \"Title 改为单数\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"B版本 Title = 'Token-Level Functional Specialization in a Vision-Language-Action Model'（单数）。\"\n    resolution_round: 3\n\n  - id: R1-N4-old\n    summary: \"Design implications 完全基于 correlational evidence\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本 Abstract 使用 hedge 语气。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识\"\n    action_items: []\n\n  - id: R1-N3-old\n    summary: \"RSA best-vs-best selection bias\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本 same-layer comparison 为 primary evidence。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"2:1 critical\"\n    action_items: []\n\n  - id: R2-N1-old\n    summary: \"Neo et al. (ICLR 2025) 未引用\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本 Related Work 已引用 Neo et al.\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R2 critical\"\n    action_items: []\n\n  - id: R2-W1-old\n    summary: \"Related Work 引用覆盖度不足\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本引用数量达标。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"21 citations 严重不足\"\n    action_items: []\n\n  - id: R1-W1-old\n    summary: \"'Instruction-blind' claim 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本补充 MLP probe 双重验证。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识\"\n    action_items: []\n\n  - id: R1-W2-old\n    summary: \"CKA 反转 RSA 排序处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Method 新增 'Why RSA over CKA' 段落。\"\n    resolution_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识\"\n    action_items: []\n\n  - id: R3-N1-old\n    summary: \"Limitations 格式不满足 CoRL 2026 要求\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"改为 \\\\subsection{Limitations}。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R3 标为 critical\"\n    action_items: []\n\n  - id: R3-N2-old\n    summary: \"正文解释性 em-dash 是 AI 写作标志\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"零残留。\"\n    resolution_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"至少 8 处\"\n    action_items: []\n\n  - id: R3-W5-old\n    summary: \"无 code/data 释放声明\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本 Conclusion 加声明。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 3]\n        note: \"CoRL 鼓励 reproducibility\"\n    action_items: []\n\n  # ============================================================\n  # Round 4 issues — 修复状态更新（Round 5 验证）\n  # ============================================================\n  - id: R4-N1\n    summary: \"C1（token-level functional specialization）是 causal mask 的数学必然结果 + probe 任务 trivially easy，不构成 empirical finding\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"全票共识。R2 从 causal mask 架构决定论论证，R1 从 probe difficulty 论证。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED: Abstract 改为 'verify and quantify architecture-expected', Intro 用 'consistent with architectural expectations', Contributions (i) 定位为 framework+verification\"\n    action_items:\n      - round: 4\n        action: \"Reframe C1 from 'empirical finding' to 'experimental framework + empirical verification'\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"C1 已从 empirical finding 重新定位为 experimental framework + architecture verification。Abstract/Intro/Contributions 全面到位。\"\n    resolution_round: 5\n\n  - id: R4-N2\n    summary: \"RSA inverted-U 的 rise phase 效应量极小（Δρ=0.016）且 metric-dependent：CKA 完全反转 RSA ordering 和 per-layer profile\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"全票共识。Linear CKA per-layer 单调递增无 inverted-U；DINOv2 在 CKA 下排名最低。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED: Abstract 含 metric-dependent qualifier, Method 有 'Why RSA over CKA', Appendix A.1-A.2 详细报告 CKA 分歧\"\n    action_items:\n      - round: 4\n        action: \"Downgrade C3 to qualified observation. Add 'under RSA' qualifier everywhere.\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"C3 已降为 qualified observation。RSA 结论全部加 metric-dependent qualifier。CKA 分歧在正文和附录均有报告。\"\n    resolution_round: 5\n\n  - id: R4-N3\n    summary: \"L1 attention ablation 使用 5 demos（vs 主实验 50 demos），R² baseline 0.256 vs ~0.65，因果推断可靠性不足\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"全票共识。5 demos 下 probe 严重 underfitting，ablation improvement 可能是 regularization effect。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED: 当前使用 50 demos (N=63,228)，R² baseline 0.557，underfitting confound 消除\"\n    action_items:\n      - round: 4\n        action: \"50 demos ablation rerun\"\n        assigned_to: research\n        status: done\n    resolution: \"Ablation 已改用 50 demos per task (N=63,228)，R² baseline 从 0.256 提升至 0.557。\"\n    resolution_round: 5\n\n  - id: R4-W1\n    summary: \"RSA best-vs-best training effect n.s.（Δ=+0.017, CI includes 0）在 Abstract/Intro 未标注显著性状态\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"全票共识。读者须到 Appendix Table 8 才知 CI includes 0。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED: Abstract 'Δρ ≤ 0.017, non-significant', Intro 'non-significant geometric gain (Δρ = 0.017, 3%)'\"\n    action_items:\n      - round: 4\n        action: \"Add n.s. marker to Abstract and Intro\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Abstract 和 Intro 均明确标注 non-significant。\"\n    resolution_round: 5\n\n  - id: R4-W2\n    summary: \"缺乏多重比较校正（32 层 × 3 条件 × 多 metric 无 FDR/Bonferroni）\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 交叉回应 AGREE。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED: Section 4.4 报告 Benjamini-Hochberg FDR correction (29-30/33 layers survive)\"\n    action_items:\n      - round: 4\n        action: \"FDR correction for key per-layer comparisons\"\n        assigned_to: research\n        status: done\n    resolution: \"FDR correction (Benjamini-Hochberg) 已应用，29-30/33 layers for R², 25/33 for RSA image_mean。\"\n    resolution_round: 5\n\n  - id: R4-W3\n    summary: \"Probe total N 未报告，MLP probe capacity 控制不充分（~1.05M params vs unknown N）\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 AGREE。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"PARTIALLY_RESOLVED: N=63,228 已报告，但 N/params≈0.06 被错误解读为 'ensuring adequate training signal'——实际是严重 overparameterized (params 是 N 的 17 倍)\"\n    action_items:\n      - round: 4\n        action: \"Report exact N in §4.1 Setup and discuss N/params ratio\"\n        assigned_to: paper_agent\n        status: done\n      - round: 5\n        action: \"修正 'ensuring adequate training signal' 为承认 overparameterized + 依赖 early stopping; 补充 linear/small probe baseline\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W4\n    summary: \"Frozen encoder confound：'vision encoder quality > LLM scale' 需要 across-encoder 实验\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"全票共识。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED: Intro 明确归因 'consistent with the causal mask and frozen encoder'; Discussion 列出 frozen encoder 为 shared design pattern\"\n    action_items:\n      - round: 4\n        action: \"Add frozen encoder confound caveat in Discussion Limitations\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Frozen encoder confound 在 Introduction 和 Discussion 中均有恰当说明。\"\n    resolution_round: 5\n\n  - id: R4-W5\n    summary: \"单模型（OpenVLA-7B）+ 单 benchmark family（LIBERO），泛化性有限\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"全票共识。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"PARTIALLY_RESOLVED: Discussion 提到 generalization open + 架构类推，但类推不等于验证。需具体列举哪些架构变量可能改变 routing pattern\"\n    action_items:\n      - round: 4\n        action: \"Expand Limitations with specific future work targets (RT-2, π₀)\"\n        assigned_to: paper_agent\n        status: done\n      - round: 5\n        action: \"在 Limitations 中具体列举可能改变 routing 的架构变量（backbone size/family, decoder type, frozen vs unfrozen encoder, projector arch, pretraining data）\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W6\n    summary: \"缺少 Llama-2 和 Open X-Embodiment 关键引用\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [2]\n        note: \"R2 提出，R1 partially agree。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED: references.bib 包含 touvron2023_llama2 和 padalkar2023_oxe\"\n    action_items:\n      - round: 4\n        action: \"Add Touvron et al. 2023 and Padalkar et al. 2023\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"两篇引用均已加入 references.bib 并在正文引用。\"\n    resolution_round: 5\n\n  - id: R4-W7\n    summary: \"Introduction 'untested assumption' 是 straw man\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 partially agree。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED: Introduction 使用 'remains uncharacterized' 和 'opaque'，无 straw man 语言\"\n    action_items:\n      - round: 4\n        action: \"Rewrite Intro — merged with C1 reframe\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Introduction 重写，使用客观描述替换 straw man 表述。\"\n    resolution_round: 5\n\n  - id: R4-I1\n    summary: \"conclusion.tex 未被 main.tex \\\\input，论文无独立 Conclusion section\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [2]\n        note: \"R2 提出，R1 AGREE。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"NOT_RESOLVED: conclusion.tex 仍存在但未被 main.tex \\\\input。Discussion 以 Limitations 段落结尾。\"\n    action_items:\n      - round: 5\n        action: \"将 conclusion.tex 整合到 main.tex 或 Discussion 末尾\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-I2\n    summary: \"引用格式问题：alain2017 年份存疑、nostalgebraist2020 blog post 格式不规范、部分 preprint 应更新\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 AGREE。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"本轮未专门检查，待 Research Director 确认\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-I3\n    summary: \"25 vs 24 heads 数值不一致的解释分散在正文和 appendix 多处\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R1 提出 should-fix，R2 partially rebut（解释存在但分散）。降级为 info。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED: 当前版本全文统一使用 24/32，Appendix Table 11 注释 threshold boundary effects\"\n    action_items: []\n    resolution: \"全文统一为 24/32 heads，Appendix 注释 bulk extraction 差异原因。\"\n    resolution_round: 5\n\n  # ============================================================\n  # Round 5 新发现 issues\n  # ============================================================\n  - id: R5-N1\n    summary: \"L1 ablation '3.5× specificity' claim 被 per-head normalization 严重削弱：per-head excess 仅 ~15%\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"全票共识。dominant 0.00246/head vs non-dominant 0.00213/head，差异仅 15%。外推 24 heads at non-dominant rate = 0.051 vs 观测 0.059，excess 仅 0.008。R2 补充：layer confinement (L1 +0.059, L8 +0.018, L13 ≈ 0) 是更干净的 specificity 证据。\"\n    action_items:\n      - round: 5\n        action: \"报告 per-head normalized effect; 弱化 '3.5×' 为 aggregate comparison; 将 layer confinement 作为 specificity 主要证据; 考虑 random-subset ablation baseline\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-N2\n    summary: \"N/params ≈ 0.06 被错误解读为 'ensuring adequate training signal'——probe 严重 overparameterized\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"全票共识。MLP probe ~1.05M params vs N=63,228。Belinkov 2022 指出高容量 probe 可从任何表征 decode。缓解因素：early stopping + comparative Δ claims 不受 absolute inflation 影响。\"\n    action_items:\n      - round: 5\n        action: \"修正 'ensuring adequate' 措辞为承认 overparameterized; 补充 linear/small probe baseline; Method 中引用 Belinkov 2022 讨论 probe complexity\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-N3\n    summary: \"单模型 scope 对 C2 generalizability 的根本约束——Limitations 讨论不够具体\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"全票共识。R2 标 critical，R1 倾向 strong warning（scope 已在 Intro 限定）。类推论证不足：RT-2 用 PaLM-E, π₀ 用 flow matching。Grant 2026 在 6 VLAs 上分析表明 cross-model 验证可行。合并升级至 warning。\"\n    action_items:\n      - round: 5\n        action: \"Limitations 中具体列举可能改变 routing 的架构变量（backbone size/family, decoder type, frozen vs unfrozen encoder, projector arch）\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-N4\n    summary: \"Discussion 'Architectural implications' 的 early-layer fine-tuning suggestion 是 speculative leap + 无 behavioral validation\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"全票共识。probe R² ≠ behavioral performance; L31 也有 18 heads instruction-dominant 矛盾 'only early-layer' 暗示。R1-W4 (无 rollout data) 和 R2-N2 指向同一问题。\"\n    action_items:\n      - round: 5\n        action: \"弱化 'suggests' 为 'raises the hypothesis'; 明确标注 speculative; 指出 L31 re-engagement 对此 implication 的 complication\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-W1\n    summary: \"Pretrained Llama-2 condition 的 OOD confound 未讨论\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 AGREE。Llama-2 base 从未见过 projected visual tokens，9/32 heads 可能是 OOD fallback 而非 genuine routing seeding。\"\n    action_items:\n      - round: 5\n        action: \"在 Method 或 Discussion 中讨论 Llama-2 OOD confound 及其对三条件叙事的影响\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-W2\n    summary: \"Bootstrap CI 未报告具体 [lower, upper] 数值（仅标 'incl. 0' / 'excl. 0'）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 AGREE。LIBERO-Spatial 有完整 CI [0.012, 0.036] 但 Goal 的核心 Δ=+0.017 仅标 'incl. 0'。\"\n    action_items:\n      - round: 5\n        action: \"报告 RSA rise phase 和 best-vs-best 的具体 CI bounds\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-W3\n    summary: \"C3 non-monotonic observation 在 Abstract/Intro 获得与 C1/C2 等量篇幅，权重过高\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 AGREE。RSA inverted-U 在 CKA 下不成立，不应与 C2 等权呈现。\"\n    action_items:\n      - round: 5\n        action: \"Abstract 中缩减 C3 篇幅，将空间用于 C2 detail 或将 metric divergence 前置\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-W4\n    summary: \"Related Work 缺少 causal tracing / activation patching (Meng et al. 2022) 和 tuned lens (Belrose et al. 2023)\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 提出 (W3+W4)，R1 AGREE。Meng 2022 与 L1 ablation 方法论直接相关；Belrose 2023 与 per-layer probing 紧密相关。\"\n    action_items:\n      - round: 5\n        action: \"在 Related Work mechanistic interpretability 段加入 Meng et al. 2022 和 Belrose et al. 2023\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-I1\n    summary: \"Appendix A.6 three-condition action R² comparison 使用 single seed，应补 3+ seeds\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 AGREE。Main results 有 5-seed analysis (A.9)，A.6 应做同等处理。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "vla-ssd",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-3 历史 issues（全部 resolved）\n  # ============================================================\n  - id: R1-N1-old\n    summary: \"Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识。需增加 Llama-2 base checkpoint 作为中间对照\"\n      - round: 2\n        reviewers: [1, 2, 3]\n        note: \"PARTIALLY_RESOLVED: acknowledge confound 但无数据\"\n    action_items:\n      - round: 1\n        action: \"增加 Llama-2 base checkpoint 对照实验\"\n        assigned_to: research\n        status: done\n      - round: 2\n        action: \"Section 标题改为观察性；Abstract 弱化 causal attribution\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"B版本完整整合三条件数据：untrained 0/32, Llama-2 base 9/32, trained 25/32 heads。§4.3 以三条件梯度为核心证据，Table 2 + Figure 4 呈现完整 32 层 profile。\"\n    resolution_round: 3\n\n  - id: R1-N2-old\n    summary: \"单一模型(OpenVLA-7B) + 单一 benchmark family(LIBERO)，Title/Abstract 使用复数 'VLAs' 构成 overclaim\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识\"\n      - round: 2\n        reviewers: [1, 2, 3]\n        note: \"PARTIALLY_RESOLVED: Abstract 限定但 Title 仍复数\"\n    action_items:\n      - round: 2\n        action: \"Title 改为单数\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"B版本 Title = 'Token-Level Functional Specialization in a Vision-Language-Action Model'（单数）。\"\n    resolution_round: 3\n\n  - id: R1-N4-old\n    summary: \"Design implications 完全基于 correlational evidence\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本 Abstract 使用 hedge 语气。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识\"\n    action_items: []\n\n  - id: R1-N3-old\n    summary: \"RSA best-vs-best selection bias\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本 same-layer comparison 为 primary evidence。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"2:1 critical\"\n    action_items: []\n\n  - id: R2-N1-old\n    summary: \"Neo et al. (ICLR 2025) 未引用\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本 Related Work 已引用 Neo et al.\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R2 critical\"\n    action_items: []\n\n  - id: R2-W1-old\n    summary: \"Related Work 引用覆盖度不足\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本引用数量达标。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"21 citations 严重不足\"\n    action_items: []\n\n  - id: R1-W1-old\n    summary: \"'Instruction-blind' claim 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本补充 MLP probe 双重验证。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识\"\n    action_items: []\n\n  - id: R1-W2-old\n    summary: \"CKA 反转 RSA 排序处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Method 新增 'Why RSA over CKA' 段落。\"\n    resolution_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"全票共识\"\n    action_items: []\n\n  - id: R3-N1-old\n    summary: \"Limitations 格式不满足 CoRL 2026 要求\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"改为 \\\\subsection{Limitations}。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"R3 标为 critical\"\n    action_items: []\n\n  - id: R3-N2-old\n    summary: \"正文解释性 em-dash 是 AI 写作标志\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"零残留。\"\n    resolution_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2, 3]\n        note: \"至少 8 处\"\n    action_items: []\n\n  - id: R3-W5-old\n    summary: \"无 code/data 释放声明\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"B版本 Conclusion 加声明。\"\n    resolution_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 3]\n        note: \"CoRL 鼓励 reproducibility\"\n    action_items: []\n\n  # ============================================================\n  # Round 4 issues — 修复状态更新（Round 5 验证）\n  # ============================================================\n  - id: R4-N1\n    summary: \"C1（token-level functional specialization）是 causal mask 的数学必然结果 + probe 任务 trivially easy，不构成 empirical finding\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"全票共识。R2 从 causal mask 架构决定论论证，R1 从 probe difficulty 论证。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED: Abstract 改为 'verify and quantify architecture-expected', Intro 用 'consistent with architectural expectations', Contributions (i) 定位为 framework+verification\"\n    action_items:\n      - round: 4\n        action: \"Reframe C1 from 'empirical finding' to 'experimental framework + empirical verification'\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"C1 已从 empirical finding 重新定位为 experimental framework + architecture verification。Abstract/Intro/Contributions 全面到位。\"\n    resolution_round: 5\n\n  - id: R4-N2\n    summary: \"RSA inverted-U 的 rise phase 效应量极小（Δρ=0.016）且 metric-dependent：CKA 完全反转 RSA ordering 和 per-layer profile\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"全票共识。Linear CKA per-layer 单调递增无 inverted-U；DINOv2 在 CKA 下排名最低。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED: Abstract 含 metric-dependent qualifier, Method 有 'Why RSA over CKA', Appendix A.1-A.2 详细报告 CKA 分歧\"\n    action_items:\n      - round: 4\n        action: \"Downgrade C3 to qualified observation. Add 'under RSA' qualifier everywhere.\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"C3 已降为 qualified observation。RSA 结论全部加 metric-dependent qualifier。CKA 分歧在正文和附录均有报告。\"\n    resolution_round: 5\n\n  - id: R4-N3\n    summary: \"L1 attention ablation 使用 5 demos（vs 主实验 50 demos），R² baseline 0.256 vs ~0.65，因果推断可靠性不足\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"全票共识。5 demos 下 probe 严重 underfitting，ablation improvement 可能是 regularization effect。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED: 当前使用 50 demos (N=63,228)，R² baseline 0.557，underfitting confound 消除\"\n    action_items:\n      - round: 4\n        action: \"50 demos ablation rerun\"\n        assigned_to: research\n        status: done\n    resolution: \"Ablation 已改用 50 demos per task (N=63,228)，R² baseline 从 0.256 提升至 0.557。\"\n    resolution_round: 5\n\n  - id: R4-W1\n    summary: \"RSA best-vs-best training effect n.s.（Δ=+0.017, CI includes 0）在 Abstract/Intro 未标注显著性状态\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"全票共识。读者须到 Appendix Table 8 才知 CI includes 0。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED: Abstract 'Δρ ≤ 0.017, non-significant', Intro 'non-significant geometric gain (Δρ = 0.017, 3%)'\"\n    action_items:\n      - round: 4\n        action: \"Add n.s. marker to Abstract and Intro\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Abstract 和 Intro 均明确标注 non-significant。\"\n    resolution_round: 5\n\n  - id: R4-W2\n    summary: \"缺乏多重比较校正（32 层 × 3 条件 × 多 metric 无 FDR/Bonferroni）\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 交叉回应 AGREE。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED: Section 4.4 报告 Benjamini-Hochberg FDR correction (29-30/33 layers survive)\"\n    action_items:\n      - round: 4\n        action: \"FDR correction for key per-layer comparisons\"\n        assigned_to: research\n        status: done\n    resolution: \"FDR correction (Benjamini-Hochberg) 已应用，29-30/33 layers for R², 25/33 for RSA image_mean。\"\n    resolution_round: 5\n\n  - id: R4-W3\n    summary: \"Probe total N 未报告，MLP probe capacity 控制不充分（~1.05M params vs unknown N）\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 AGREE。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"PARTIALLY_RESOLVED: N=63,228 已报告，但 N/params≈0.06 被错误解读为 'ensuring adequate training signal'——实际是严重 overparameterized (params 是 N 的 17 倍)\"\n    action_items:\n      - round: 4\n        action: \"Report exact N in §4.1 Setup and discuss N/params ratio\"\n        assigned_to: paper_agent\n        status: done\n      - round: 5\n        action: \"修正 'ensuring adequate training signal' 为承认 overparameterized + 依赖 early stopping; 补充 linear/small probe baseline\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W4\n    summary: \"Frozen encoder confound：'vision encoder quality > LLM scale' 需要 across-encoder 实验\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"全票共识。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED: Intro 明确归因 'consistent with the causal mask and frozen encoder'; Discussion 列出 frozen encoder 为 shared design pattern\"\n    action_items:\n      - round: 4\n        action: \"Add frozen encoder confound caveat in Discussion Limitations\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Frozen encoder confound 在 Introduction 和 Discussion 中均有恰当说明。\"\n    resolution_round: 5\n\n  - id: R4-W5\n    summary: \"单模型（OpenVLA-7B）+ 单 benchmark family（LIBERO），泛化性有限\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"全票共识。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"PARTIALLY_RESOLVED: Discussion 提到 generalization open + 架构类推，但类推不等于验证。需具体列举哪些架构变量可能改变 routing pattern\"\n    action_items:\n      - round: 4\n        action: \"Expand Limitations with specific future work targets (RT-2, π₀)\"\n        assigned_to: paper_agent\n        status: done\n      - round: 5\n        action: \"在 Limitations 中具体列举可能改变 routing 的架构变量（backbone size/family, decoder type, frozen vs unfrozen encoder, projector arch, pretraining data）\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W6\n    summary: \"缺少 Llama-2 和 Open X-Embodiment 关键引用\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [2]\n        note: \"R2 提出，R1 partially agree。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED: references.bib 包含 touvron2023_llama2 和 padalkar2023_oxe\"\n    action_items:\n      - round: 4\n        action: \"Add Touvron et al. 2023 and Padalkar et al. 2023\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"两篇引用均已加入 references.bib 并在正文引用。\"\n    resolution_round: 5\n\n  - id: R4-W7\n    summary: \"Introduction 'untested assumption' 是 straw man\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 partially agree。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED: Introduction 使用 'remains uncharacterized' 和 'opaque'，无 straw man 语言\"\n    action_items:\n      - round: 4\n        action: \"Rewrite Intro — merged with C1 reframe\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Introduction 重写，使用客观描述替换 straw man 表述。\"\n    resolution_round: 5\n\n  - id: R4-I1\n    summary: \"conclusion.tex 未被 main.tex \\\\input，论文无独立 Conclusion section\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [2]\n        note: \"R2 提出，R1 AGREE。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"NOT_RESOLVED: conclusion.tex 仍存在但未被 main.tex \\\\input。Discussion 以 Limitations 段落结尾。\"\n    action_items:\n      - round: 5\n        action: \"将 conclusion.tex 整合到 main.tex 或 Discussion 末尾\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-I2\n    summary: \"引用格式问题：alain2017 年份存疑、nostalgebraist2020 blog post 格式不规范、部分 preprint 应更新\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 AGREE。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"本轮未专门检查，待 Research Director 确认\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-I3\n    summary: \"25 vs 24 heads 数值不一致的解释分散在正文和 appendix 多处\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R1 提出 should-fix，R2 partially rebut（解释存在但分散）。降级为 info。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED: 当前版本全文统一使用 24/32，Appendix Table 11 注释 threshold boundary effects\"\n    action_items: []\n    resolution: \"全文统一为 24/32 heads，Appendix 注释 bulk extraction 差异原因。\"\n    resolution_round: 5\n\n  # ============================================================\n  # Round 5 新发现 issues\n  # ============================================================\n  - id: R5-N1\n    summary: \"L1 ablation '3.5× specificity' claim 被 per-head normalization 严重削弱：per-head excess 仅 ~15%\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"全票共识。dominant 0.00246/head vs non-dominant 0.00213/head，差异仅 15%。外推 24 heads at non-dominant rate = 0.051 vs 观测 0.059，excess 仅 0.008。R2 补充：layer confinement (L1 +0.059, L8 +0.018, L13 ≈ 0) 是更干净的 specificity 证据。\"\n    action_items:\n      - round: 5\n        action: \"报告 per-head normalized effect; 弱化 '3.5×' 为 aggregate comparison; 将 layer confinement 作为 specificity 主要证据; 考虑 random-subset ablation baseline\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-N2\n    summary: \"N/params ≈ 0.06 被错误解读为 'ensuring adequate training signal'——probe 严重 overparameterized\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"全票共识。MLP probe ~1.05M params vs N=63,228。Belinkov 2022 指出高容量 probe 可从任何表征 decode。缓解因素：early stopping + comparative Δ claims 不受 absolute inflation 影响。\"\n    action_items:\n      - round: 5\n        action: \"修正 'ensuring adequate' 措辞为承认 overparameterized; 补充 linear/small probe baseline; Method 中引用 Belinkov 2022 讨论 probe complexity\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-N3\n    summary: \"单模型 scope 对 C2 generalizability 的根本约束——Limitations 讨论不够具体\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"全票共识。R2 标 critical，R1 倾向 strong warning（scope 已在 Intro 限定）。类推论证不足：RT-2 用 PaLM-E, π₀ 用 flow matching。Grant 2026 在 6 VLAs 上分析表明 cross-model 验证可行。合并升级至 warning。\"\n    action_items:\n      - round: 5\n        action: \"Limitations 中具体列举可能改变 routing 的架构变量（backbone size/family, decoder type, frozen vs unfrozen encoder, projector arch）\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-N4\n    summary: \"Discussion 'Architectural implications' 的 early-layer fine-tuning suggestion 是 speculative leap + 无 behavioral validation\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"全票共识。probe R² ≠ behavioral performance; L31 也有 18 heads instruction-dominant 矛盾 'only early-layer' 暗示。R1-W4 (无 rollout data) 和 R2-N2 指向同一问题。\"\n    action_items:\n      - round: 5\n        action: \"弱化 'suggests' 为 'raises the hypothesis'; 明确标注 speculative; 指出 L31 re-engagement 对此 implication 的 complication\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-W1\n    summary: \"Pretrained Llama-2 condition 的 OOD confound 未讨论\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 AGREE。Llama-2 base 从未见过 projected visual tokens，9/32 heads 可能是 OOD fallback 而非 genuine routing seeding。\"\n    action_items:\n      - round: 5\n        action: \"在 Method 或 Discussion 中讨论 Llama-2 OOD confound 及其对三条件叙事的影响\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-W2\n    summary: \"Bootstrap CI 未报告具体 [lower, upper] 数值（仅标 'incl. 0' / 'excl. 0'）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 AGREE。LIBERO-Spatial 有完整 CI [0.012, 0.036] 但 Goal 的核心 Δ=+0.017 仅标 'incl. 0'。\"\n    action_items:\n      - round: 5\n        action: \"报告 RSA rise phase 和 best-vs-best 的具体 CI bounds\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-W3\n    summary: \"C3 non-monotonic observation 在 Abstract/Intro 获得与 C1/C2 等量篇幅，权重过高\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 AGREE。RSA inverted-U 在 CKA 下不成立，不应与 C2 等权呈现。\"\n    action_items:\n      - round: 5\n        action: \"Abstract 中缩减 C3 篇幅，将空间用于 C2 detail 或将 metric divergence 前置\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-W4\n    summary: \"Related Work 缺少 causal tracing / activation patching (Meng et al. 2022) 和 tuned lens (Belrose et al. 2023)\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 提出 (W3+W4)，R1 AGREE。Meng 2022 与 L1 ablation 方法论直接相关；Belrose 2023 与 per-layer probing 紧密相关。\"\n    action_items:\n      - round: 5\n        action: \"在 Related Work mechanistic interpretability 段加入 Meng et al. 2022 和 Belrose et al. 2023\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-I1\n    summary: \"Appendix A.6 three-condition action R² comparison 使用 single seed，应补 3+ seeds\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 AGREE。Main results 有 5-seed analysis (A.9)，A.6 应做同等处理。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 355 · 2026-05-18T02:03:33.313065+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml\", \"bytes\": 20498}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 356 · 2026-05-18T02:05:46.605318+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 圆桌审稿报告 — Round 5\n\n**论文**: \"Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\"\n**Venue**: CoRL 2026 (Paper deadline: 2026-05-29, double-blind, 8pp + refs + appendix)\n**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/意义 + 相关工作 + Framing)\n**交叉回应**: 完成。R2 对 R1 全部 AGREE; R1 对 R2 有 7 AGREE + 2 partial REBUT（C1 框架独立价值、引用数量 vs gap）。共识程度高。\n\n---\n\n## Summary\n\n论文对 OpenVLA-7B 在 LIBERO 上进行了系统性 token 级表征分析，使用 trained/pretrained/untrained 三条件 factorial 设计结合四种互补方法（cross-instruction probes, attention analysis, RSA, functional probes）。核心发现是 VLA fine-tuning 将 instruction routing 从 mid-depth (L9-L16) 前移至 entry-exit pattern (L0-L1, L31)，效果集中在 readout token (+0.069 R², +46pp attention) 而非 image tokens。论文方法论系统、统计分析充分、对 metric dependence 坦诚报告。与 Round 4 相比，C1 reframe、RSA qualifier、50-demo ablation 等 critical issues 已修复，但出现新的方法论问题（ablation per-head normalization、probe overparameterization 误解读）。\n\n---\n\n## Strengths\n\n1. **系统性四分析方法 + 三条件控制**：cross-instruction probes × attention × RSA × functional probes，交叉 trained/pretrained/untrained × instruction presence，是 VLA 分析文献中首个此级别的系统化框架。（R1+R2 共识）\n2. **C2 routing finding 有真正新颖性**：三条件 routing gradient (0/32 → 9/32 → 24/32 heads at L1) + entry-exit vs mid-depth pattern 的发现，是 genuine empirical contribution。Grant et al. 2026 做 feature-level analysis，本文做 token-level + layer-level decomposition，深度互补。（R2 强调）\n3. **统计严谨性和 robustness 分析充分**：Bootstrap CIs (10,000)、LOOCV、permutation tests、distance metric invariance (r > 0.989)、seed sensitivity (0.655 ± 0.002)、demo subsampling (r = 0.97)、threshold sensitivity (30%-70%)、cross-benchmark (LIBERO-Spatial)、FDR correction (Benjamini-Hochberg, 29-30/33 layers)。（R1 确认）\n4. **Metric dependence 坦诚报告**：CKA 与 RSA 分歧在 Abstract、Method (\"Why RSA over CKA\")、Appendix 中均如实呈现，增强可信度。（R1+R2 共识）\n5. **Round 4 critical issues 实质性修复**：C1 reframe 到位、50-demo ablation 消除 underfitting confound、RSA qualifier 全面、FDR correction 已应用、straw man 已消除、头数统一为 24/32。（R1+R2 共识）\n6. **写作质量高，AI 痕迹极少**：无 em-dash、无 AI 典型用词、结构清晰。（R2 确认）\n\n---\n\n## Weaknesses（按严重性排序）\n\n### Critical（影响接收决定，全票共识）\n\n**W-Critical-1: L1 Ablation 的 \"3.5× specificity\" claim 在 per-head normalization 后仅剩 ~15% excess**\n- 位置：Section 4.2, experiments.tex lines 78-82\n- 问题：Ablating 24 dominant heads → +0.059 R²; ablating 8 non-dominant heads → +0.017。论文声称 \"3.5× smaller\" 证明 graded specificity。Per-head: dominant = 0.059/24 ≈ 0.00246, non-dominant = 0.017/8 ≈ 0.00213，差异仅 ~15%。外推 24 heads at non-dominant rate = 0.051，观测 0.059，excess 仅 0.008 (16%)。\n- 影响：这是 C2 \"VLA fine-tuning front-loads instruction routing\" 的唯一因果证据。\"3.5×\" 混淆了 head 数量差异和 per-head specificity。\n- 缓解因素（R2 补充）：layer confinement (L1: +0.059, L8: +0.018, L13: ≈0) 不受 head 数量 confound，是更干净的 specificity 证据。\n- **修复方案**：(a) 报告 per-head normalized effect size; (b) 弱化 \"3.5×\" 为 aggregate comparison; (c) 将 layer confinement 作为 specificity 主要证据; (d) 理想情况补充 random-subset ablation (随机 24/32 heads, k 次)。\n- **全票共识 (R1 critical, R2 AGREE)**\n\n**W-Critical-2: N/params ≈ 0.06 被错误解读为 \"ensuring adequate training signal\"**\n- 位置：Section 4.1, experiments.tex line 12\n- 问题：MLP probe (4096→256→7) ≈ 1.05M params, N = 63,228。N/params ≈ 0.06 意味着参数量是数据量的 ~17 倍，是严重 overparameterized regime。Belinkov (2022) 指出高容量 probe 可从任何表征 decode 信息。论文称此 ratio \"ensuring adequate training signal\" 是错误的。\n- 缓解因素：(a) 使用 early stopping (patience 5)；(b) 核心 claims 基于 Δ 而非 absolute R²，Δ 不受 absolute inflation 影响（假设 overfitting degree 跨条件相似）；(c) seed sensitivity < 0.01 std。\n- **修复方案**：(a) 修正措辞为 \"probe is overparameterized; we rely on early stopping\"; (b) 补充 linear probe 或 small MLP (64 hidden) baseline; (c) Method 中引用 Belinkov 2022 讨论 probe complexity-capability tradeoff。\n- **全票共识 (R1 critical, R2 AGREE)**\n\n### Warning（影响评分，全票或多数共识）\n\n**W-Warning-1: 单模型 scope 对 C2 generalizability 的约束 + Limitations 讨论不够具体**\n- Discussion 以架构类推（RT-2, π₀）论证潜在 generalizability，但类推不等于验证：RT-2 用 PaLM-E，π₀ 用 flow matching。Grant 2026 在 6 VLAs 上分析表明 cross-model 验证可行。\n- Contributions list 已限定 \"demonstrated on OpenVLA-7B/LIBERO\"，但 Limitations 应具体列举可能改变 routing 的架构变量（backbone size/family, decoder type, frozen vs unfrozen encoder, projector arch, pretraining data）。\n- **R2 标 critical, R1 倾向 strong warning（scope 已限定）。合并为 warning。**\n\n**W-Warning-2: Discussion \"Architectural implications\" 的 early-layer fine-tuning suggestion 属 speculative leap**\n- probe R² 变化 ≠ behavioral performance 变化。L31 也有 18 heads instruction-dominant，直接矛盾 \"only early-layer\" 暗示。论文自己承认 \"requires task-level evaluation beyond this work\"。\n- **修复**：弱化 \"suggests\" → \"raises the hypothesis\"；标注 speculative；讨论 L31 complication。\n- **全票共识 (R2 critical, R1 AGREE → 合并为 warning，因措辞已部分 hedged)**\n\n**W-Warning-3: Pretrained Llama-2 condition 的 OOD confound 未讨论**\n- Llama-2 base 从未见过 projected visual tokens (DinoSigLIP 4096-D)。9/32 instruction-dominant heads 可能反映 OOD 输入下的 default attention fallback，而非 language pretraining 对 instruction routing 的真正 \"seeding\"。\n- 影响 C2 叙事：\"language pretraining seeds routing, VLA fine-tuning amplifies it\" 可能 too clean。\n- **全票共识 (R1 提出, R2 AGREE)**\n\n**W-Warning-4: Bootstrap CI 缺具体 [lower, upper] 数值**\n- RSA best-vs-best Δ=+0.017 及多处核心数据仅标 \"CI incl. 0\" / \"excl. 0\"，未给区间。LIBERO-Spatial 有完整 CI [0.012, 0.036]，主实验的缺失更显眼。\n- **全票共识 (R1 提出, R2 AGREE)**\n\n**W-Warning-5: C3 non-monotonic observation 在 Abstract/Intro 权重过高**\n- RSA inverted-U 在 CKA 下不成立（monotonic increase），不应与 C2 等权呈现。当前 Abstract 中 C3 获得与 C1/C2 等量篇幅。\n- **修复**：缩减 C3 Abstract 篇幅或将 metric divergence 前置。\n- **全票共识 (R2 提出, R1 AGREE)**\n\n**W-Warning-6: Related Work 缺 causal tracing / activation patching + tuned lens**\n- 缺 Meng et al. 2022 (NeurIPS, \"Locating and Editing Factual Associations in GPT\") — 与 L1 ablation 方法论直接相关\n- 缺 Belrose et al. 2023 (tuned lens) — 与 per-layer probing 紧密相关\n- 当前 29 citations，补充后 ~31-33，引用密度合理。\n- **全票共识 (R2 提出, R1 AGREE)**\n\n### Info（低严重性）\n\n**I1**: conclusion.tex 存在但未被 main.tex `\\input`。Discussion 以 Limitations 收尾，叙事以消极信息结束。（R4-I1 仍未修复）\n**I2**: Appendix A.6 single-seed three-condition analysis 应补 3+ seeds（main results 有 5-seed sensitivity）。\n**I3**: Abstract 渲染后词数可能超 250 words（raw LaTeX ~241）。\n**I4**: -ing 分词短语约 15+ 处（\", enabling/indicating/confirming/suggesting...\"），密度偏高但不构成严重问题。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n所有 Reviewer 达成共识的关键判断：\n1. **Ablation per-head normalization 是新发现的最大方法论问题**——\"3.5× specificity\" 在归一化后仅 ~15% excess，C2 因果证据被削弱（但 layer confinement 提供替代 specificity 证据）\n2. **Probe overparameterization 的错误解读需修正**——措辞错误但有缓解因素（early stopping, Δ claims）\n3. **单模型 scope 是最大的 significance 限制**——Contributions 已限定 scope，但 Limitations 讨论不够具体\n4. **Design implications 缺乏 behavioral validation 属 speculative**——当前措辞部分 hedged 但仍 overcommitted\n5. **Round 4 的 3 个 critical issues (C1 reframe, RSA qualifier, 50-demo ablation) 全部实质性修复**\n6. **写作质量高，统计报告整体透明**\n\n---\n\n## Reviewer Divergence [REBUT]\n\n| 分歧点 | R1 立场 | R2 立场 | 最终处理 |\n|--------|---------|---------|----------|\n| 单模型 severity | strong warning（scope 已限定） | critical（generalizability 根本约束） | warning（Intro 已限定 scope，但 Limitations 需更具体） |\n| C1 框架独立价值 | 有独立方法学贡献（REBUT R2-W1） | 混合框架+验证，验证部分说服力有限 | 保留 R2-W1 为 info — 措辞可改进但不影响接收 |\n| Quality 评分 | 3/5（ablation N1+N2 严重） | 3.5/5（statistical apparatus 加分） | 取中间值 3.25/5 |\n| 引用数量 | 数量不是问题，gap 是问题（REBUT R2-I3） | 29 篇中等偏低 | 采纳 R1 判断——补充 W6 指出的 gap 后 ~31-33 篇，量级合理 |\n\n---\n\n## Questions（需作者澄清）\n\n1. **[R1-Q1, R2 AGREE]** 能否提供 random-subset ablation（随机抽 24/32 heads ablated，重复 k 次）的 R² 分布？这是明确 dominant-head specificity 的 gold standard。\n2. **[R1-Q2, R2 AGREE]** 是否尝试过 smaller probes (4096→32→7 或 linear)？如果 inverted-U 和 Δ 在低容量 probe 下 reproduce，大幅增强可信度。\n3. **[R1-Q3]** Pretrained Llama-2 处理 OOD visual tokens 时，intermediate activations 是否在 reasonable range？（排除 OOD 导致的 degenerate behavior）\n4. **[R2-Q1]** C2 的 entry-exit pattern 是否可能是 Llama-2 7B 特定 backbone 的 artifact？不同 backbone（如 Mistral, Phi）是否预期同样的 reorganization？\n5. **[R2-Q2]** L1 ablation 对 instruction-following accuracy（cross-instruction classification）的影响是否测量过？这将完善 capacity trade-off 论证。\n6. **[R2-Q3]** 是否考虑过验证 early-layer-only fine-tuning 的 behavioral performance？即使 5-10 episodes 也有价值。\n\n---\n\n## Missing References\n\n| 引用 | 重要性 | 理由 |\n|------|--------|------|\n| Meng et al. 2022, \"Locating and Editing Factual Associations in GPT\" (NeurIPS) | **High** | 与 L1 ablation 方法论直接相关（causal tracing / activation patching） |\n| Belrose et al. 2023, \"Eliciting Latent Predictions from Transformers with the Tuned Lens\" | **High** | 与 per-layer probing 紧密相关（tuned lens → per-layer learned mapping） |\n| Goldowsky-Dill et al. 2023, \"Localizing Model Behavior with Path Patching\" | Medium | 更全面的 patching methodology |\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置/未请求。\n\n---\n\n## Overall Assessment\n\n**Score: Borderline (6/10)**\n**Confidence: High (4/5)**\n\n| Reviewer | Initial | Post-Cross | 变化理由 |\n|----------|---------|------------|----------|\n| R1 | 6/10 | 6/10 | 维持。R2 的 concerns 与自身互补但不改变总评 |\n| R2 | 6/10 | 6/10 | 维持。R1 的 per-head normalization 分析加强了 ablation concern 但有 layer confinement 缓解 |\n| **Consensus** | **6/10** | **Borderline** | |\n\n### 维度评分（R1+R2 加权平均）\n\n| 维度 | 分数 | 说明 |\n|------|------|------|\n| Originality | 6/10 | C2 routing finding 有真正新颖性；C1 框架有方法论价值；C3 被 metric dependence 削弱 |\n| Quality | 6.5/10 | 统计 apparatus 充分，但 ablation 因果推断有缺陷 + probe overparameterization 误解读 |\n| Clarity | 8/10 | 写作清晰，AI 痕迹极少，结构合理 |\n| Significance | 5/10 | 单模型 scope + 无 behavioral validation + speculative implications 限制 practical impact |\n| Relevance | 8/10 | 直接面向 CoRL 核心关注：VLA 内部机制理解 |\n| Limitations | 7/10 | 主要限制已报告，但单模型讨论不够具体 + probe 解读错误 |\n\n### 核心判断\n\n论文是一篇方法论严谨的 VLA 分析论文，C2 routing finding 有真正新颖性，三条件 factorial 设计是该领域的方法学进步，Round 4 的 critical issues 已实质性修复。但存在两类新问题削弱了 contribution strength：\n\n1. **方法论瑕疵**（可修复）：ablation \"3.5× specificity\" 的 per-head normalization 问题 + probe overparameterization 的错误解读。这些是 framing/reporting 问题而非根本性实验缺陷——layer confinement 提供替代 specificity 证据，comparative Δ 不受 absolute R² inflation 影响。\n2. **Significance ceiling**（难以快速修复）：单模型 scope + 无 behavioral validation + speculative design implications。对 CoRL 社区而言，representation → behavior 的连接是核心价值。\n\n**Rebuttal 路径**：\n- **Likely sufficient**：(a) 修正 ablation framing（报告 per-head effect + 强调 layer confinement）; (b) 修正 probe 措辞; (c) 充实 single-model limitations; (d) 弱化 architectural implications; (e) 补充缺失引用\n- **Would strengthen significantly**：(a) random-subset ablation baseline; (b) linear/small probe reproducing inverted-U; (c) Llama-2 OOD analysis\n- **Ideal but out of scope for deadline**：second VLA / behavioral rollout\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract (~241 words raw)\n- C1 reframe 到位：\"verify and quantify architecture-expected token specialization\"\n- C3 metric-dependent qualifier 到位：\"metric-dependent\"\n- **问题**：C3 与 C1/C2 等权篇幅，建议缩减 C3 让出空间给 C2 ablation detail\n- \"non-significant\" marker 已加（Δρ ≤ 0.017, non-significant）\n\n### Introduction\n- 五段结构完整，从 gap 切入\n- Straw man 已消除（\"remains uncharacterized\" / \"opaque\"）\n- Contributions (i) 混合框架+验证——建议更强调框架 reusability\n- **新问题**：无 Llama-2 OOD confound 讨论\n\n### Related Work\n- 五段主题组织清晰（VLAs, mechanistic interpretability, behavioral analysis, token specialization, RSA methodology）\n- 29 citations，密度中等\n- **缺失**：causal tracing / activation patching (Meng 2022); tuned lens (Belrose 2023)\n- 与 Grant 2026 的 differentiation 清晰（三点对比）\n\n### Method\n- Factorial design 清晰\n- \"Why RSA over CKA\" 段落解决了 R4-W2\n- **新问题**：N/params ratio 解读错误（Section 4.1）；未讨论 probe complexity-capability tradeoff (Belinkov 2022)\n\n### Experiments\n- 三条件 gradient 数据完整（Table 2, Figure 1）\n- Ablation 已改用 50 demos (N=63,228)\n- **新问题**：Section 4.2 \"3.5×\" claim 需 per-head normalization 修正\n- FDR correction 已应用\n\n### Discussion\n- Synthesis 段准确\n- Mechanism-behavior connection 有价值\n- Speculative mechanistic interpretation 合理标注\n- **新问题**：Architectural implications 最后一句 overcommitted（early-layer-only suggestion + L31 complication）\n- Limitations 提到单模型但不够具体\n\n### Appendix\n- Robustness suite 全面（distance metric, per-DOF, permutation, seeds, demo subsample, threshold, cross-benchmark）\n- A.6 single-seed 应补 multi-seed\n- CKA divergence 报告充分\n\n### References (29 entries)\n- 覆盖 VLA, benchmarks, RSA/CKA, vision encoders, mechanistic interpretability, probing, attention analysis\n- **缺失**：activation patching (Meng 2022), tuned lens (Belrose 2023)\n- 格式总体规范；nostalgebraist 2020 blog post 格式可接受",
  "project": "vla-ssd",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 圆桌审稿报告 — Round 5\n\n**论文**: \"Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\"\n**Venue**: CoRL 2026 (Paper deadline: 2026-05-29, double-blind, 8pp + refs + appendix)\n**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/意义 + 相关工作 + Framing)\n**交叉回应**: 完成。R2 对 R1 全部 AGREE; R1 对 R2 有 7 AGREE + 2 partial REBUT（C1 框架独立价值、引用数量 vs gap）。共识程度高。\n\n---\n\n## Summary\n\n论文对 OpenVLA-7B 在 LIBERO 上进行了系统性 token 级表征分析，使用 trained/pretrained/untrained 三条件 factorial 设计结合四种互补方法（cross-instruction probes, attention analysis, RSA, functional probes）。核心发现是 VLA fine-tuning 将 instruction routing 从 mid-depth (L9-L16) 前移至 entry-exit pattern (L0-L1, L31)，效果集中在 readout token (+0.069 R², +46pp attention) 而非 image tokens。论文方法论系统、统计分析充分、对 metric dependence 坦诚报告。与 Round 4 相比，C1 reframe、RSA qualifier、50-demo ablation 等 critical issues 已修复，但出现新的方法论问题（ablation per-head normalization、probe overparameterization 误解读）。\n\n---\n\n## Strengths\n\n1. **系统性四分析方法 + 三条件控制**：cross-instruction probes × attention × RSA × functional probes，交叉 trained/pretrained/untrained × instruction presence，是 VLA 分析文献中首个此级别的系统化框架。（R1+R2 共识）\n2. **C2 routing finding 有真正新颖性**：三条件 routing gradient (0/32 → 9/32 → 24/32 heads at L1) + entry-exit vs mid-depth pattern 的发现，是 genuine empirical contribution。Grant et al. 2026 做 feature-level analysis，本文做 token-level + layer-level decomposition，深度互补。（R2 强调）\n3. **统计严谨性和 robustness 分析充分**：Bootstrap CIs (10,000)、LOOCV、permutation tests、distance metric invariance (r > 0.989)、seed sensitivity (0.655 ± 0.002)、demo subsampling (r = 0.97)、threshold sensitivity (30%-70%)、cross-benchmark (LIBERO-Spatial)、FDR correction (Benjamini-Hochberg, 29-30/33 layers)。（R1 确认）\n4. **Metric dependence 坦诚报告**：CKA 与 RSA 分歧在 Abstract、Method (\"Why RSA over CKA\")、Appendix 中均如实呈现，增强可信度。（R1+R2 共识）\n5. **Round 4 critical issues 实质性修复**：C1 reframe 到位、50-demo ablation 消除 underfitting confound、RSA qualifier 全面、FDR correction 已应用、straw man 已消除、头数统一为 24/32。（R1+R2 共识）\n6. **写作质量高，AI 痕迹极少**：无 em-dash、无 AI 典型用词、结构清晰。（R2 确认）\n\n---\n\n## Weaknesses（按严重性排序）\n\n### Critical（影响接收决定，全票共识）\n\n**W-Critical-1: L1 Ablation 的 \"3.5× specificity\" claim 在 per-head normalization 后仅剩 ~15% excess**\n- 位置：Section 4.2, experiments.tex lines 78-82\n- 问题：Ablating 24 dominant heads → +0.059 R²; ablating 8 non-dominant heads → +0.017。论文声称 \"3.5× smaller\" 证明 graded specificity。Per-head: dominant = 0.059/24 ≈ 0.00246, non-dominant = 0.017/8 ≈ 0.00213，差异仅 ~15%。外推 24 heads at non-dominant rate = 0.051，观测 0.059，excess 仅 0.008 (16%)。\n- 影响：这是 C2 \"VLA fine-tuning front-loads instruction routing\" 的唯一因果证据。\"3.5×\" 混淆了 head 数量差异和 per-head specificity。\n- 缓解因素（R2 补充）：layer confinement (L1: +0.059, L8: +0.018, L13: ≈0) 不受 head 数量 confound，是更干净的 specificity 证据。\n- **修复方案**：(a) 报告 per-head normalized effect size; (b) 弱化 \"3.5×\" 为 aggregate comparison; (c) 将 layer confinement 作为 specificity 主要证据; (d) 理想情况补充 random-subset ablation (随机 24/32 heads, k 次)。\n- **全票共识 (R1 critical, R2 AGREE)**\n\n**W-Critical-2: N/params ≈ 0.06 被错误解读为 \"ensuring adequate training signal\"**\n- 位置：Section 4.1, experiments.tex line 12\n- 问题：MLP probe (4096→256→7) ≈ 1.05M params, N = 63,228。N/params ≈ 0.06 意味着参数量是数据量的 ~17 倍，是严重 overparameterized regime。Belinkov (2022) 指出高容量 probe 可从任何表征 decode 信息。论文称此 ratio \"ensuring adequate training signal\" 是错误的。\n- 缓解因素：(a) 使用 early stopping (patience 5)；(b) 核心 claims 基于 Δ 而非 absolute R²，Δ 不受 absolute inflation 影响（假设 overfitting degree 跨条件相似）；(c) seed sensitivity < 0.01 std。\n- **修复方案**：(a) 修正措辞为 \"probe is overparameterized; we rely on early stopping\"; (b) 补充 linear probe 或 small MLP (64 hidden) baseline; (c) Method 中引用 Belinkov 2022 讨论 probe complexity-capability tradeoff。\n- **全票共识 (R1 critical, R2 AGREE)**\n\n### Warning（影响评分，全票或多数共识）\n\n**W-Warning-1: 单模型 scope 对 C2 generalizability 的约束 + Limitations 讨论不够具体**\n- Discussion 以架构类推（RT-2, π₀）论证潜在 generalizability，但类推不等于验证：RT-2 用 PaLM-E，π₀ 用 flow matching。Grant 2026 在 6 VLAs 上分析表明 cross-model 验证可行。\n- Contributions list 已限定 \"demonstrated on OpenVLA-7B/LIBERO\"，但 Limitations 应具体列举可能改变 routing 的架构变量（backbone size/family, decoder type, frozen vs unfrozen encoder, projector arch, pretraining data）。\n- **R2 标 critical, R1 倾向 strong warning（scope 已限定）。合并为 warning。**\n\n**W-Warning-2: Discussion \"Architectural implications\" 的 early-layer fine-tuning suggestion 属 speculative leap**\n- probe R² 变化 ≠ behavioral performance 变化。L31 也有 18 heads instruction-dominant，直接矛盾 \"only early-layer\" 暗示。论文自己承认 \"requires task-level evaluation beyond this work\"。\n- **修复**：弱化 \"suggests\" → \"raises the hypothesis\"；标注 speculative；讨论 L31 complication。\n- **全票共识 (R2 critical, R1 AGREE → 合并为 warning，因措辞已部分 hedged)**\n\n**W-Warning-3: Pretrained Llama-2 condition 的 OOD confound 未讨论**\n- Llama-2 base 从未见过 projected visual tokens (DinoSigLIP 4096-D)。9/32 instruction-dominant heads 可能反映 OOD 输入下的 default attention fallback，而非 language pretraining 对 instruction routing 的真正 \"seeding\"。\n- 影响 C2 叙事：\"language pretraining seeds routing, VLA fine-tuning amplifies it\" 可能 too clean。\n- **全票共识 (R1 提出, R2 AGREE)**\n\n**W-Warning-4: Bootstrap CI 缺具体 [lower, upper] 数值**\n- RSA best-vs-best Δ=+0.017 及多处核心数据仅标 \"CI incl. 0\" / \"excl. 0\"，未给区间。LIBERO-Spatial 有完整 CI [0.012, 0.036]，主实验的缺失更显眼。\n- **全票共识 (R1 提出, R2 AGREE)**\n\n**W-Warning-5: C3 non-monotonic observation 在 Abstract/Intro 权重过高**\n- RSA inverted-U 在 CKA 下不成立（monotonic increase），不应与 C2 等权呈现。当前 Abstract 中 C3 获得与 C1/C2 等量篇幅。\n- **修复**：缩减 C3 Abstract 篇幅或将 metric divergence 前置。\n- **全票共识 (R2 提出, R1 AGREE)**\n\n**W-Warning-6: Related Work 缺 causal tracing / activation patching + tuned lens**\n- 缺 Meng et al. 2022 (NeurIPS, \"Locating and Editing Factual Associations in GPT\") — 与 L1 ablation 方法论直接相关\n- 缺 Belrose et al. 2023 (tuned lens) — 与 per-layer probing 紧密相关\n- 当前 29 citations，补充后 ~31-33，引用密度合理。\n- **全票共识 (R2 提出, R1 AGREE)**\n\n### Info（低严重性）\n\n**I1**: conclusion.tex 存在但未被 main.tex `\\input`。Discussion 以 Limitations 收尾，叙事以消极信息结束。（R4-I1 仍未修复）\n**I2**: Appendix A.6 single-seed three-condition analysis 应补 3+ seeds（main results 有 5-seed sensitivity）。\n**I3**: Abstract 渲染后词数可能超 250 words（raw LaTeX ~241）。\n**I4**: -ing 分词短语约 15+ 处（\", enabling/indicating/confirming/suggesting...\"），密度偏高但不构成严重问题。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n所有 Reviewer 达成共识的关键判断：\n1. **Ablation per-head normalization 是新发现的最大方法论问题**——\"3.5× specificity\" 在归一化后仅 ~15% excess，C2 因果证据被削弱（但 layer confinement 提供替代 specificity 证据）\n2. **Probe overparameterization 的错误解读需修正**——措辞错误但有缓解因素（early stopping, Δ claims）\n3. **单模型 scope 是最大的 significance 限制**——Contributions 已限定 scope，但 Limitations 讨论不够具体\n4. **Design implications 缺乏 behavioral validation 属 speculative**——当前措辞部分 hedged 但仍 overcommitted\n5. **Round 4 的 3 个 critical issues (C1 reframe, RSA qualifier, 50-demo ablation) 全部实质性修复**\n6. **写作质量高，统计报告整体透明**\n\n---\n\n## Reviewer Divergence [REBUT]\n\n| 分歧点 | R1 立场 | R2 立场 | 最终处理 |\n|--------|---------|---------|----------|\n| 单模型 severity | strong warning（scope 已限定） | critical（generalizability 根本约束） | warning（Intro 已限定 scope，但 Limitations 需更具体） |\n| C1 框架独立价值 | 有独立方法学贡献（REBUT R2-W1） | 混合框架+验证，验证部分说服力有限 | 保留 R2-W1 为 info — 措辞可改进但不影响接收 |\n| Quality 评分 | 3/5（ablation N1+N2 严重） | 3.5/5（statistical apparatus 加分） | 取中间值 3.25/5 |\n| 引用数量 | 数量不是问题，gap 是问题（REBUT R2-I3） | 29 篇中等偏低 | 采纳 R1 判断——补充 W6 指出的 gap 后 ~31-33 篇，量级合理 |\n\n---\n\n## Questions（需作者澄清）\n\n1. **[R1-Q1, R2 AGREE]** 能否提供 random-subset ablation（随机抽 24/32 heads ablated，重复 k 次）的 R² 分布？这是明确 dominant-head specificity 的 gold standard。\n2. **[R1-Q2, R2 AGREE]** 是否尝试过 smaller probes (4096→32→7 或 linear)？如果 inverted-U 和 Δ 在低容量 probe 下 reproduce，大幅增强可信度。\n3. **[R1-Q3]** Pretrained Llama-2 处理 OOD visual tokens 时，intermediate activations 是否在 reasonable range？（排除 OOD 导致的 degenerate behavior）\n4. **[R2-Q1]** C2 的 entry-exit pattern 是否可能是 Llama-2 7B 特定 backbone 的 artifact？不同 backbone（如 Mistral, Phi）是否预期同样的 reorganization？\n5. **[R2-Q2]** L1 ablation 对 instruction-following accuracy（cross-instruction classification）的影响是否测量过？这将完善 capacity trade-off 论证。\n6. **[R2-Q3]** 是否考虑过验证 early-layer-only fine-tuning 的 behavioral performance？即使 5-10 episodes 也有价值。\n\n---\n\n## Missing References\n\n| 引用 | 重要性 | 理由 |\n|------|--------|------|\n| Meng et al. 2022, \"Locating and Editing Factual Associations in GPT\" (NeurIPS) | **High** | 与 L1 ablation 方法论直接相关（causal tracing / activation patching） |\n| Belrose et al. 2023, \"Eliciting Latent Predictions from Transformers with the Tuned Lens\" | **High** | 与 per-layer probing 紧密相关（tuned lens → per-layer learned mapping） |\n| Goldowsky-Dill et al. 2023, \"Localizing Model Behavior with Path Patching\" | Medium | 更全面的 patching methodology |\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置/未请求。\n\n---\n\n## Overall Assessment\n\n**Score: Borderline (6/10)**\n**Confidence: High (4/5)**\n\n| Reviewer | Initial | Post-Cross | 变化理由 |\n|----------|---------|------------|----------|\n| R1 | 6/10 | 6/10 | 维持。R2 的 concerns 与自身互补但不改变总评 |\n| R2 | 6/10 | 6/10 | 维持。R1 的 per-head normalization 分析加强了 ablation concern 但有 layer confinement 缓解 |\n| **Consensus** | **6/10** | **Borderline** | |\n\n### 维度评分（R1+R2 加权平均）\n\n| 维度 | 分数 | 说明 |\n|------|------|------|\n| Originality | 6/10 | C2 routing finding 有真正新颖性；C1 框架有方法论价值；C3 被 metric dependence 削弱 |\n| Quality | 6.5/10 | 统计 apparatus 充分，但 ablation 因果推断有缺陷 + probe overparameterization 误解读 |\n| Clarity | 8/10 | 写作清晰，AI 痕迹极少，结构合理 |\n| Significance | 5/10 | 单模型 scope + 无 behavioral validation + speculative implications 限制 practical impact |\n| Relevance | 8/10 | 直接面向 CoRL 核心关注：VLA 内部机制理解 |\n| Limitations | 7/10 | 主要限制已报告，但单模型讨论不够具体 + probe 解读错误 |\n\n### 核心判断\n\n论文是一篇方法论严谨的 VLA 分析论文，C2 routing finding 有真正新颖性，三条件 factorial 设计是该领域的方法学进步，Round 4 的 critical issues 已实质性修复。但存在两类新问题削弱了 contribution strength：\n\n1. **方法论瑕疵**（可修复）：ablation \"3.5× specificity\" 的 per-head normalization 问题 + probe overparameterization 的错误解读。这些是 framing/reporting 问题而非根本性实验缺陷——layer confinement 提供替代 specificity 证据，comparative Δ 不受 absolute R² inflation 影响。\n2. **Significance ceiling**（难以快速修复）：单模型 scope + 无 behavioral validation + speculative design implications。对 CoRL 社区而言，representation → behavior 的连接是核心价值。\n\n**Rebuttal 路径**：\n- **Likely sufficient**：(a) 修正 ablation framing（报告 per-head effect + 强调 layer confinement）; (b) 修正 probe 措辞; (c) 充实 single-model limitations; (d) 弱化 architectural implications; (e) 补充缺失引用\n- **Would strengthen significantly**：(a) random-subset ablation baseline; (b) linear/small probe reproducing inverted-U; (c) Llama-2 OOD analysis\n- **Ideal but out of scope for deadline**：second VLA / behavioral rollout\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract (~241 words raw)\n- C1 reframe 到位：\"verify and quantify architecture-expected token specialization\"\n- C3 metric-dependent qualifier 到位：\"metric-dependent\"\n- **问题**：C3 与 C1/C2 等权篇幅，建议缩减 C3 让出空间给 C2 ablation detail\n- \"non-significant\" marker 已加（Δρ ≤ 0.017, non-significant）\n\n### Introduction\n- 五段结构完整，从 gap 切入\n- Straw man 已消除（\"remains uncharacterized\" / \"opaque\"）\n- Contributions (i) 混合框架+验证——建议更强调框架 reusability\n- **新问题**：无 Llama-2 OOD confound 讨论\n\n### Related Work\n- 五段主题组织清晰（VLAs, mechanistic interpretability, behavioral analysis, token specialization, RSA methodology）\n- 29 citations，密度中等\n- **缺失**：causal tracing / activation patching (Meng 2022); tuned lens (Belrose 2023)\n- 与 Grant 2026 的 differentiation 清晰（三点对比）\n\n### Method\n- Factorial design 清晰\n- \"Why RSA over CKA\" 段落解决了 R4-W2\n- **新问题**：N/params ratio 解读错误（Section 4.1）；未讨论 probe complexity-capability tradeoff (Belinkov 2022)\n\n### Experiments\n- 三条件 gradient 数据完整（Table 2, Figure 1）\n- Ablation 已改用 50 demos (N=63,228)\n- **新问题**：Section 4.2 \"3.5×\" claim 需 per-head normalization 修正\n- FDR correction 已应用\n\n### Discussion\n- Synthesis 段准确\n- Mechanism-behavior connection 有价值\n- Speculative mechanistic interpretation 合理标注\n- **新问题**：Architectural implications 最后一句 overcommitted（early-layer-only suggestion + L31 complication）\n- Limitations 提到单模型但不够具体\n\n### Appendix\n- Robustness suite 全面（distance metric, per-DOF, permutation, seeds, demo subsample, threshold, cross-benchmark）\n- A.6 single-seed 应补 multi-seed\n- CKA divergence 报告充分\n\n### References (29 entries)\n- 覆盖 VLA, benchmarks, RSA/CKA, vision encoders, mechanistic interpretability, probing, attention analysis\n- **缺失**：activation patching (Meng 2022), tuned lens (Belrose 2023)\n- 格式总体规范；nostalgebraist 2020 blog post 格式可接受",
    "project": "vla-ssd",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline"
  }
}
```

</details>

---


### Tool result

_source line 357 · 2026-05-18T02:05:51.324294+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a1d032cbe70bdd2058438e67e0d57613:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4718
}
```

</details>

---


### Assistant

_source line 358 · 2026-05-18T02:05:58.952648+00:00_

审稿报告已投递至 Research Director。

---

**Round 5 审稿完成。** 两位 Reviewer 评分一致 6/10 (borderline)，交叉回应高度收敛。

核心结论：
- **Round 4 的 3 个 critical issues 全部修复**（C1 reframe, RSA qualifier, 50-demo ablation）
- **2 个新 critical issues**：(1) ablation "3.5× specificity" per-head normalization 后仅 ~15% excess; (2) probe N/params 误解读
- **4 个 warning**：单模型 Limitations 不够具体、architectural implications speculative、Llama-2 OOD confound、CI 缺具体数值
- **总评 borderline**：C2 routing finding 有真正新颖性 + 方法论系统，但 significance 受限于单模型 scope + 无 behavioral validation

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 40

## Round 40

2 recorded events


### User

_source line 359 · 2026-05-18T02:06:01.857215+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。R1 的所有意见我均 [AGREE]，两位 reviewer 在关键问题上形成共识：ablation specificity claim 需修正、probe overparameterization 需承认、单模型 scope 限制 significance、design implications 缺 behavioral validation。综合评分维持 6/10。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 360 · 2026-05-18T02:06:15.331439+00:00_

审稿报告已于交叉回应收敛后提交至 Research Director，Issue Tracker 已同步更新。

**本轮审稿总结**：

- **评分**: Borderline (6/10)，两位 Reviewer 一致
- **Round 4 修复状态**: 3 个 critical 全部 RESOLVED（C1 reframe、RSA qualifier、50-demo ablation）；7/10 个 warning+ 已 RESOLVED
- **新发现 2 个 critical**：(1) L1 ablation "3.5×" claim per-head normalization 后仅 ~15% excess；(2) probe N/params 误解读为 "adequate"——均为 framing 问题而非根本实验缺陷
- **最大 significance 瓶颈**: 单模型 + 无 behavioral validation + speculative design implications
- **Rebuttal 可行性**: 方法论瑕疵可通过修正 framing + 补充 linear probe baseline 修复；significance ceiling 短期难以突破

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 41

## Round 41

58 recorded events


### User

_source line 361 · 2026-05-18T08:49:30.505545+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: vla-ssd
- 论文路径: projects/vla-ssd/docs/paper/main.tex
- 目标 venue: CoRL 2026
- 截止日期: 2026-05-29

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 362 · 2026-05-18T08:49:39.234298+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 363 · 2026-05-18T08:49:39.285209+00:00_

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
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 364 · 2026-05-18T08:49:47.168769+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file",
  "max_results": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file",
    "max_results": "8"
  }
}
```

</details>

---


### Tool result

_source line 365 · 2026-05-18T08:49:47.320644+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 366 · 2026-05-18T08:49:53.100662+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-18T08:49:53.654259+00:00_

{"result":"# 项目 vla-ssd 概况\n\n## 实验状态 (76 个)\n\n- **lg_extract_untrained_r2**: DONE (killed) — \n- **lg_extract_trained_r2**: DONE (killed) — \n- **lg_extract_untrained_r1**: DONE (killed) — \n- **lg_extract_trained_r1**: DONE (killed) — \n- **mvp2_delta_dino**: DONE (success) — \n- **mvp2_delta_untrained**: DONE (success) — \n- **mvp2_delta_trained**: DONE (success) — \n- **mvp2_action_dino**: DONE (success) — \n- **mvp2_action_untrained**: DONE (success) — \n- **mvp2_action_trained**: DONE (success) — \n- **mvp_controlb_untrained**: DONE (success) — \n- **mvp_controlb_trained**: DONE (success) — \n- **mvp_001**: DONE (negative) — \n- **mvp_probe_untrained**: DONE (success) — \n- **mvp_probe_trained**: DONE (negative) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-18T08:47:25Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 76 个实验 — ANALYZING 1, DONE 72, PREPARING 3\n**DONE 分布**: killed 8, negative 7, success 57\n\n### GPU 占用\n- **分配**: 2 张 — westd-19183:cuda:0, westd-19183:cuda:1\n- **空闲（分配了没跑）**: westd-19183:cuda:0, westd-19183:cuda:1\n\n### 💾 磁盘余量\n- **westd-19183**:\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\n  - `/init`: 150M/150M 可用（已用 0%）\n  - `/usr/bin/nvidia-smi`: 816G/879G 可用（已用 3%）\n\n### 🏃 RUNNING\n_（无）_\n\n### 📌 最近完成 (top 5)\n- `random_subset_ablation` [success] — 2026-05-18T08:27:15\n- `threecond_multiseed_r2` [success] — 2026-05-18T08:04:22\n- `linear_probe_last_preaction` [success] — 2026-05-18T07:40:44\n- `llama2base_action_probe` [success] — 2026-05-17T22:02:32\n- `ablation_50demos_main` [success] — 2026-05-17T21:49:51\n\n&lt;!-- AUTO-FACTS-END -->\n\n---\n\n# Handover — 2026-05-18\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| threecond_multiseed_r2_v2 | Multi-seed action probes (3 seeds, sequential split matching original experiment) will confirm trained > llama2base > untrained R² gradient with low se
…[truncated 1498 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 368 · 2026-05-18T08:49:53.654769+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "literature_map.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "literature_map.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 369 · 2026-05-18T08:49:53.906177+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/literature_map.yaml\", \"content\": \"papers:\\n  # ============================================================\\n  # DIRECT COMPETITORS — VLA Representation Analysis / Interpretability\\n  # ============================================================\\n  - id: grant2026\\n    title: \\\"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models\\\"\\n    authors: \\\"Bryce Grant, Xijia Zhao, Peng Wang\\\"\\n    year: 2026\\n    venue: \\\"arXiv preprint (under review)\\\"\\n    arxiv_id: \\\"2603.19233\\\"\\n    category: direct-competitor\\n    role: competitor\\n    key_findings: >\\n      Visual pathway dominates action generation across all 6 tested VLA architectures (80M–7B params, 394K+ rollout episodes, 4 benchmarks).\\n      Language sensitivity depends on task structure: when visual context uniquely specifies the task, language is IGNORED;\\n      when multiple goals share a scene, language becomes essential (\\\"encoded but not used\\\").\\n      Cross-task activation injection steers robots toward source-task positions (99.8% trajectory alignment with source in X-VLA).\\n      Multi-pathway architectures (pi0.5, SmolVLA, GR00T) separate motor programs (expert pathway) from goal semantics (VLM pathway).\\n    relevance_to_us: >\\n      Most direct competitor. Behavioral intervention (activation injection, SAE, probing) reveals vision dominance + language encoded but not used.\\n      Uses OpenVLA-OFT checkpoint; we use standard fine-tuning — must qualify this difference in Related Work.\\n    novelty_gap: >\\n      No trained vs untrained representation analysis. They compare different model architectures,\\n      we compare trained vs untrained representation structure within the same architecture.\\n      Their \\\"encoded but not used\\\" is a behavioral-level conclusion; we demonstrate at the represent
…[truncated 3580 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 370 · 2026-05-18T08:49:53.956759+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
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

_source line 371 · 2026-05-18T08:49:54.007387+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-18T08:49:58.796260+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 call for papers submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 373 · 2026-05-18T08:49:59.801403+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 374 · 2026-05-18T08:50:00.258838+00:00_

1	\documentclass{article}
2	
3	\usepackage{corl_2026}
4	
5	\usepackage[utf8]{inputenc}
6	\usepackage[T1]{fontenc}
7	\usepackage{url}
8	\usepackage{booktabs}
9	\usepackage{amsfonts}
10	\usepackage{amsmath}
11	\usepackage{nicefrac}
12	\usepackage[expansion=false]{microtype}
13	\usepackage{graphicx}
14	\usepackage{enumitem}
15	
16	\title{Vision Encodes, Language Routes:\\ Token-Level Functional Specialization in a Vision-Language-Action Model}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	
22	\maketitle
23	
24	\begin{abstract}
25	\input{abstract}
26	\end{abstract}
27	
28	\input{introduction}
29	\input{related_work}
30	\input{method}
31	\input{experiments}
32	\input{discussion}
33	
34	\bibliography{references}
35	
36	\input{appendix}
37	
38	\end{document}
39	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 457
}
```

</details>

---


### Tool call

_source line 375 · 2026-05-18T08:50:00.361943+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---
