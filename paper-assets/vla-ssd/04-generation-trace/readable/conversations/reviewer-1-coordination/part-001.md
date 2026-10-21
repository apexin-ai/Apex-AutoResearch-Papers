# Reviewer 1 coordination — Part 1 of 2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

[Transcript overview](../reviewer-1-coordination.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/49/497e6584b4dbc2a30271.json)

## Round 1

## Round 1

40 recorded events


### User

_source line 1 · 2026-05-17T04:31:37.923107+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验有效性）

### Venue 信息
- **目标会议**: CoRL 2026
- **截止日期**: 2026-05-28（论文）
- **页数限制**: 8 页正文 + references + appendix
- **模板**: corl_2026（已正确使用）
- **匿名规则**: double-blind
- **特殊要求**: 必须含 Limitations section（计入 8 页），需论证 robotics relevance

### 论文路径
`projects/vla-ssd/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, appendix.tex, references.bib）

### 你的审查侧重

**方法严谨性和实验有效性**，重点关注：

1. **实验设计的因果推断力**：
   - trained vs untrained 对照是否充分隔离了 LLM 训练的贡献？reinitialize 6.74B params 是否是合理的 baseline？（vs. 随机初始化的 LLM 可能表现完全不同于一个未经 VLA 训练但经过语言预训练的模型）
   - 2×2 factorial design 的效力：instruction presence × training status 是否覆盖了关键混淆因素？
   - 单一模型（OpenVLA-7B）、单一 benchmark family（LIBERO）的泛化性问题

2. **统计方法的合理性**：
   - Bootstrap 10,000 resamples 的假设检验是否恰当
   - RSA best-vs-best 比较（trained L12 vs untrained L0）是否存在 cherry-picking 问题
   - 多重比较校正是否充分
   - LOOCV 10-fold 是否有足够 power 给出 100%±0.00 的可信结论

3. **Probing 方法论的局限**：
   - Linear/MLP probe 是否能区分 "information present" vs "information used"
   - Probe 的容量控制（2-layer 256-hidden MLP）是否合理
   - R² 作为 metric 的选择是否有 ceiling/floor 效应

4. **具体实验细节**：
   - 数据量（10 tasks × 50 demos）是否足以支撑 per-layer 32-point profile 的结论
   - Attention analysis 仅在 L1 做是否有选择性报告嫌疑
   - "instruction-blind" 的结论是否过强（chance-level 分类 ≠ no instruction information）

5. **可复现性**：
   - 实验细节是否充分支撑复现
   - 代码/数据是否可用

请给出结构化审稿报告：Summary → Strengths → Weaknesses → Questions → Minor Issues

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-17T04:31:55.780080+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
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

_source line 3 · 2026-05-17T04:31:55.780488+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-17T04:31:59.397038+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 5 · 2026-05-17T04:32:00.402368+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 6 · 2026-05-17T04:32:00.403624+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-17T04:32:06.495804+00:00_

Web search results for query: "CoRL 2026 reviewer guidelines review form criteria"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CVPR 2026 Reviewer Guidelines","url":"https://cvpr.thecvf.com/Conferences/2026/ReviewerGuidelinesq"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"}]

Based on the search results, I found information about CoRL 2026, though specific detailed reviewer guidelines and review form criteria for CoRL 2026 don't appear to be fully available yet. However, I can share what I found:

## CoRL 2026 Reviewer Information

All submissions to CoRL 2026 must include at least one author who agrees to serve as a CoRL reviewer, and they are qualified if they have at least one accepted publication at a previous robotics (CoRL/ICRA/IROS/RSS) or learning conference (ICLR/NeurIPS/ICML) or equivalent journal.

## Related Review Criteria (from CoRL 2024)

While specific CoRL 2026 review form criteria aren't detailed in the current search results, based on the most recent available CoRL reviewer guidelines from previous years, submissions are evaluated based on the significance and novelty of the results, either theoretical or empirical.

From CoRL 2023 reviewer guidelines, evaluation
…[truncated 604 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7098
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-17T04:32:09.761599+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2024 \"instruction for reviews\" reviewer form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2024 \"instruction for reviews\" reviewer form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 9 · 2026-05-17T04:32:10.167203+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 10 · 2026-05-17T04:32:10.624137+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 456
}
```

</details>

---


### Tool call

_source line 11 · 2026-05-17T04:32:10.624622+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 12 · 2026-05-17T04:32:11.128455+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 13 · 2026-05-17T04:32:11.179070+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 14 · 2026-05-17T04:32:11.229752+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-17T04:32:16.709097+00:00_

Web search results for query: "CoRL 2024 "instruction for reviews" reviewer form criteria scoring"

Links: [{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2024 - Instruction for Authors","url":"https://2024.corl.org/contributions/instruction-for-authors"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"Instructions for Reviewers","url":"https://corl2022.org/instructions-for-reviewers/"},{"title":"CoRL 2024 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/corl-paper-list/corl-2024-paper-list/"},{"title":"Conference on Robot Learning","url":"https://twitter.com/corl_conf/status/1666663426339508224"},{"title":"ICML 2024 Reviewer Instructions","url":"https://icml.cc/Conferences/2024/ReviewerInstructions"},{"title":"Frequently Asked Questions","url":"https://corl2022.org/frequently-asked-questions/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

I found the CoRL 2024 Instructions for Reviews page. Here's what the search revealed about the review criteria and scoring:

## CoRL 2024 Review Criteria

Submissions are evaluated based on the significance and novelty of the results (either theoretical or empirical), judged on the degree to which they have been objectively established and/or their potential for scientific and technological impact, as well as their relevance to robotic learning.

## Reviewer Qualifications

Reviewers need to have expertise in robotics, robot learning, machine learning and complementary fields, and ideally have a minimum of 3 first author publications in major robotics conferences and journals (e.g., CoRL, RSS, ICRA, IROS, IJRR
…[truncated 821 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6947
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-17T04:32:20.425706+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-17T04:32:20.879373+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-17T04:32:20.879833+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-17T04:32:21.181209+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-17T04:32:21.181865+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-17T04:32:21.282507+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-17T04:32:26.209055+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-17T04:32:26.610881+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-17T04:32:26.611283+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-17T04:32:27.264282+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 652
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-17T04:32:27.265049+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2023 reviewer guidelines scoring scale rating criteria \"overall recommendation\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2023 reviewer guidelines scoring scale rating criteria \"overall recommendation\""
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-17T04:32:31.280413+00:00_

Web search results for query: "CoRL 2023 reviewer guidelines scoring scale rating criteria "overall recommendation""

Links: [{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"ICLR 2023 Reviewer Guide","url":"https://iclr.cc/Conferences/2023/ReviewerGuide"},{"title":"CoRL 2023 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/corl-statistics/corl-2023-statistics/"},{"title":"CoRL 2023 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2023%2FConference"},{"title":"CoRL 2023 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/corl-paper-list/corl-2023-paper-list/"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"Frequently Asked Questions","url":"https://corl2022.org/frequently-asked-questions/"},{"title":"Conference on Robot Learning","url":"https://twitter.com/corl_conf/status/1666663426339508224"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"},{"title":"CORLcleared Vendor Scoring Process – CORL_Portal","url":"https://corl-portal.zendesk.com/hc/en-us/articles/14440881933339-CORLcleared-Vendor-Scoring-Process"}]

Based on the web search results, I found the CoRL 2023 Reviewer Guidelines page. However, the search result excerpt from the official CoRL 2023 reviewer guidelines (source 1) does not contain the specific scoring scale ratings and "overall recommendation" criteria you're looking for. 

The excerpt I retrieved focuses on guidelines about how to write constructive reviews, the treatment of limitations sections, and the review timeline, but it doesn't include the detailed scoring scale or rating criteria for the "overall recommendation" field.

To get the complete scoring scale and rating criteria for CoRL 2023, you would need to visit the full Reviewer Guidelines pag
…[truncated 236 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 4015
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-17T04:32:34.495667+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
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

_source line 29 · 2026-05-17T04:32:34.596565+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-17T04:32:40.884590+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl2023.org/reviewer-guidelines",
  "prompt": "Extract the complete scoring scale / rating criteria for CoRL reviews. I need: 1) All review dimensions (e.g., overall recommendation, novelty, significance, clarity, etc.) 2) The numerical scale for each dimension 3) What each score means. Return the full rating rubric."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl2023.org/reviewer-guidelines",
    "prompt": "Extract the complete scoring scale / rating criteria for CoRL reviews. I need: 1) All review dimensions (e.g., overall recommendation, novelty, significance, clarity, etc.) 2) The numerical scale for each dimension 3) What each score means. Return the full rating rubric."
  }
}
```

</details>

---


### Tool call

_source line 31 · 2026-05-17T04:32:41.941237+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2024.corl.org/contributions/instruction-for-reviews",
  "prompt": "Extract the complete review form criteria, scoring dimensions, and rating scale for CoRL 2024 reviews. I need all review dimensions, the numerical scale, and what each score means."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2024.corl.org/contributions/instruction-for-reviews",
    "prompt": "Extract the complete review form criteria, scoring dimensions, and rating scale for CoRL 2024 reviews. I need all review dimensions, the numerical scale, and what each score means."
  }
}
```

</details>

---


### Tool result

_source line 32 · 2026-05-17T04:32:45.417897+00:00_

# CoRL 2023 Review Scoring Scale

Based on the provided guidelines page, **the complete numerical scoring rubric is not included in this document**.

The page outlines six evaluation dimensions that reviewers should address:

1. **Originality** - novelty of problems/methods and differentiation from prior work
2. **Quality** - technical soundness and claim support
3. **Clarity** - writing quality and organization
4. **Significance** - importance and state-of-art advancement
5. **Relevance** - alignment with robot learning focus
6. **Limitations** - honest assessment of shortcomings

However, the document does not provide:
- Numerical scales (e.g., 1-5, 1-10)
- Specific score definitions (e.g., what "4/5" means)
- An overall recommendation scale

The guidelines emphasize that reviewers should be "constructive and concrete" and provide "substantiated" evaluations, but the actual rating rubric with point values and score interpretations appears to be distributed separately, likely through the OpenReview submission platform mentioned in the timeline section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 4533
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-17T04:32:45.669702+00:00_

# CoRL 2024 Review Criteria Summary

Based on the provided webpage content, **the complete review form, scoring dimensions, and numerical rating scale are not included** in the document.

## What IS Available:

The page describes **review evaluation criteria** for regular papers:

> "Submissions will be evaluated based on the significance and novelty of the results, either theoretical or empirical."

Reviewers assess papers on:
- Degree of objective establishment of results
- Potential for scientific and technological impact
- Relevance to robotic learning

## What IS NOT Available:

The document does not specify:
- Numbered scoring scales (e.g., 1-5, 1-10)
- Specific rating categories or score meanings
- Detailed rubrics or weighted dimensions
- The actual review form template

The webpage focuses instead on desk rejection criteria, reviewer qualifications, and general evaluation principles rather than the quantitative assessment framework reviewers would use when completing reviews.

To obtain the complete scoring rubric and review form, you would need to access the CoRL 2024 submission system or contact the conference organizers directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 3728
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-17T04:32:55.148223+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2024 OpenReview review form \"overall score\" scale 1 2 3 4 5 6 7 8 9 10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2024 OpenReview review form \"overall score\" scale 1 2 3 4 5 6 7 8 9 10"
  }
}
```

</details>

---


### Tool call

_source line 35 · 2026-05-17T04:32:56.302842+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 36 · 2026-05-17T04:32:56.353731+00:00_

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
…[truncated 6159 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-17T04:33:07.172389+00:00_

Web search results for query: "CoRL 2024 OpenReview review form "overall score" scale 1 2 3 4 5 6 7 8 9 10"

Links: [{"title":"CoRL 2024 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2024"},{"title":"CORL 2024 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/corl-statistics/corl-2024-statistics/"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"CoRL 2024 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FConference"},{"title":"CoRL 2024 Conference Submissions | OpenReview","url":"https://openreview.net/submissions?venue=robot-learning.org/CoRL/2024/Conference"},{"title":"CoRL | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL"},{"title":"CoRL 2024 Workshop XE | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FWorkshop%2FXE"},{"title":"CoRL 2024 Workshop | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FWorkshop"},{"title":"CoRL 2024 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/corl-paper-list/corl-2024-paper-list/"},{"title":"CoRL 2024 Workshop WCBM | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FWorkshop%2FWCBM"}]

The search results don't contain specific information about the CoRL 2024 review form's overall score scale. Let me try a more specific search:

Links: [{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"CoRL 2024 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2024"},{"title":"CoRL 2024 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FConference"},{"title":"ICLR 2024 Reviewer
…[truncated 4621 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 12024
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-17T04:35:51.231252+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 1 审稿报告 — Reviewer 1（方法严谨性 + 实验有效性）\n\n**论文标题**: Vision Encodes, Language Routes: A Representational Decomposition of Vision-Language-Action Models\n\n---\n\n## 总体评分\n\n**Overall**: 5/10 (Marginally below acceptance threshold)\n\n**一句话总结**: 论文提出了有价值的分析框架，但核心实验设计存在关键混淆（untrained baseline 不能隔离 VLA fine-tuning 的贡献），单一模型+单一 benchmark family 的泛化性不足以支撑关于\"VLAs\"的一般性结论。\n\n---\n\n## 官方维度打分（基于 CoRL review form：Originality / Quality / Clarity / Significance / Relevance / Limitations）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 7/10 | 首次做 token-level representational decomposition 的 VLA 分析，分析框架（cross-instruction probe + attention + RSA + functional probe 的组合）有新意 |\n| Quality | 4/10 | 关键对照设计有根本缺陷（见 N1）；RSA best-vs-best 存在 cherry-picking（N3）；probing 的 encoding vs. use 混淆（N4）；统计检验力不足 |\n| Clarity | 7/10 | 写作清晰，结构合理，图表信息密度高；但部分 claim 的措辞过强，超出证据支撑范围 |\n| Significance | 5/10 | 如果结论成立，对 VLA 架构设计有实际指导意义；但单模型单 benchmark 限制了影响力，且部分结论（如 vision encoder is primary design lever）缺乏因果支撑 |\n| Relevance | 8/10 | 直接分析 robot learning 核心模型架构，高度相关 |\n| Limitations | 6/10 | Section 5 诚实讨论了主要限制，但低估了 untrained baseline 的根本问题和 probing 方法论的局限性 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Untrained control 不能隔离 VLA fine-tuning 的贡献\n\n- 具体位置：Section 3.1, \"reinitializing all LLM parameters via `from_config()` (6.74B random weights)\"\n- 问题：论文将 trained（OpenVLA-7B，含 Llama-2 预训练 + VLA fine-tuning）与 untrained（完全随机权重）对比，声称差异反映 \"training learns deliberate routing\"。但这个对照混淆了两个因素：(1) Llama-2 语言预训练的贡献（结构化 attention pattern、语言理解能力）；(2) VLA fine-tuning 的贡献。随机初始化的 6.74B 参数 LLM 缺乏任何结构化处理能力，routing 的 decay（82% at L31）可能仅仅反映随机网络的 signal degradation，而非 \"absence of deliberate routing\"。\n- 正确的对照应包括：Llama-2 原始 checkpoint（无 VLA fine-tuning但有语言预训练）——这才能隔离 VLA 训练本身的贡献。\n- 为什么影响接收：论文三个核心发现中的第二个（\"training learns deliberate instruction routing\"）和所有 trained vs. untrained 的定量比较（Table 3 所有 Δ 值）都依赖这个对照。如果差异主要来自语言预训练而非 VLA fine-tuning，则论文的核心叙事（\"VLA training reshapes routing\"）不成立。\n- 建议修改方向：增加 Llama-2 base checkpoint 作为第三个条件（pretrained-but-not-VLA-finetuned），形成三级对照：random → language-pretrained → VLA-finetuned。至少对 attention analysis 和 cross-instruction probe 做这个消融。\n\n**N2** [critical] 单一模型、单一 benchmark family 无法支撑关于 \"VLAs\" 的一般性结论\n\n- 具体位置：Title（\"Vision-Language-Action Models\"，复数）；Abstract（\"VLAs maintain a strict division of labor\"）；Conclusion（\"VLA architectures should optimize routing\"）\n- 问题：所有实验仅在 OpenVLA-7B（一个特定架构：frozen DinoSigLIP + MLP projector + Llama-2）上进行，仅在 LIBERO（tabletop manipulation，简单视觉场景）上评估。论文的 claims 却使用复数 \"VLAs\" 并给出架构设计建议。不同 VLA 架构差异巨大：RT-2 使用 PaLM-E，π₀ 使用 flow matching，Octo 使用 transformer decoder。frozen vision encoder 的设计也是 OpenVLA 的特定选择，其他 VLA 可能 fine-tune encoder。\n- 为什么影响接收：CoRL reviewer guidelines 要求评估 \"significance and novelty of the results\" 及 \"potential for scientific and technological impact\"。单个数据点无法建立一般性规律，特别是当结论明确为架构设计建议时。\n- 建议修改方向：(1) 将所有 claim 限定为 \"OpenVLA-7B\" 或 \"frozen-encoder VLAs\"；(2) 至少在一个不同架构的 VLA 上验证核心发现（如 RT-2 family 或任何 fine-tune encoder 的 VLA）；(3) 如果无法增加模型，则明确讨论哪些发现可能是架构特异性的（如 frozen encoder → instruction-blind image tokens 可能是 trivial 推论）。\n\n**N3** [critical] RSA best-vs-best 比较存在 selection bias\n\n- 具体位置：Table 3, \"Best-vs-best image_mean: trained L12 vs. untrained L0, Δ = +0.017, CI incl. 0, n.s.\"\n- 问题：best-vs-best 比较允许每个条件独立选择最优层。在 32 层中取 max，统计上会引入正偏置（winner's curse / multiple comparisons）。论文报告此差异不显著（CI 包含 0），但仍在 narrative 中积极解读为 \"training redistributes geometry\"（Section 4.3 标题）。更令人担忧的是 LIBERO-Spatial 的 Δ = +0.023, p < 0.001 被用来 \"confirm that the n.s. result on Goal reflects limited power\"（Section 4.4），这是用一个独立数据集的显著结果来否定另一个数据集的零结果，方法论上不成立。\n- 此外，readout token 的 best-vs-best（trained L13 vs. untrained L32）比较的两个层差距 19 层，功能完全不同，这种比较的解释价值存疑。\n- 为什么影响接收：核心定量结论（training effect size）的可信度受损。审稿人和读者无法区分真实效应和统计噪音。\n- 建议修改方向：(1) 报告 same-layer paired comparison 作为主要结果（已有 L12 same-layer Δ = +0.079, p < 0.0001）；(2) 对 best-vs-best 做 multiple comparisons correction（如 Bonferroni 或 permutation-based max-statistic）；(3) 明确区分 \"training shifts peak location\" vs. \"training improves peak magnitude\" 两个独立 claim。\n\n**N4** [critical] Probing 结果不能支撑 \"functional\" 或 \"used\" 的结论\n\n- 具体位置：Section 3.6 标题 \"Functional Action Probes\"；Section 4.1 \"Functional implications\"；Discussion \"vision encoder quality is the primary design lever\"\n- 问题：论文在标题中使用 \"functional\" 来描述 MLP probe，并将 probe R² 解释为 \"functional capacity\"。但 probing 文献已充分论证（Belinkov 2022，论文自己引用），probe accuracy 证明 information is linearly/nonlinearly extractable，不证明 model uses this information for downstream task。同样，高 RSA 证明 geometric alignment，不证明 causal contribution。论文的核心设计建议（\"vision encoder quality is the primary design lever\"）完全基于 DINOv2 有最高 RSA，但没有任何因果证据（如 intervention、ablation）表明更好的 RSA 导致更好的 task performance。\n- 此外，2-layer 256-hidden MLP probe 的容量控制值得质疑：对 4096-D input 预测 7-D output，256-hidden 可能过小（underfitting）或过大（overfitting 到 probe-specific features）。没有报告 probe 的 train/test split 细节或 overfitting 诊断。\n- 为什么影响接收：论文最重要的实际建议（\"invest in stronger self-supervised encoders\"）没有因果支撑。如果仅仅是 \"DINOv2 representations happen to be geometrically similar to the action space\" 但 VLA 并不通过这种 geometry 来生成 action，则建议无实际价值。\n- 建议修改方向：(1) 将 \"functional\" 改为 \"decodable\" 以准确描述 probe 测量的是什么；(2) 增加因果证据：用不同 vision encoder 的 VLA variant（如 CLIP-only vs. DINOv2-only）训练并比较 task success rate；(3) 或至少在 Discussion 中明确这是 correlational evidence，不直接支撑因果设计建议。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] \"Instruction-blind\" claim 过强\n\n- 具体位置：Section 4.1, \"Image tokens are instruction-blind\"；Abstract, \"instruction classification at chance, 10%, across all layers\"\n- 问题：chance-level linear probe accuracy (10%) 不等于 \"no instruction information\"。这仅证明 10-way instruction identity 不是 linearly separable from image_mean activations。论文用了 MLP probe 做 action prediction 但只用 linear probe 做 instruction classification——如果对 instruction 也用 MLP probe 或更高容量模型，结果是否一致？此外，instruction influence 可能以 non-identity 方式存在（如 shift attention to task-relevant spatial regions），这种 graded influence 不会被 10-way classification probe 捕捉到。\n- 建议：(1) 补充 MLP probe 对 instruction classification 的结果；(2) 将 claim 限定为 \"instruction identity is not linearly decodable from image tokens\"；(3) 讨论 subtler forms of instruction influence（如 conditional attention to different image regions）。\n\n**W2** [warning] CKA 与 RSA 结论矛盾，处理不充分\n\n- 具体位置：Appendix B (Section A.2), \"Linear CKA reverses the RSA ordering\"\n- 问题：Linear CKA 显示 untrained > trained > DINOv2，完全逆转 RSA 的 DINOv2 > trained > untrained。论文将此作为 \"different metrics capture different things\" 一笔带过。但这引发根本问题：如果两个标准度量给出相反结论，论文选择 RSA 作为主要结论的依据是什么？仅仅因为 RSA 支持了论文想要的 narrative（DINOv2 最好、training helps）吗？\n- RDM kernel CKA 部分解决（trained ≈ projector > untrained > DINOv2），但仍然显示 DINOv2 最差，与 RSA 的 DINOv2 最优完全相反。\n- 建议：正文中讨论 metric divergence，解释为什么 RSA（rank-order preservation）比 CKA（linear covariance structure）更适合评估 action-relevant geometry，或者承认结论是 metric-dependent 的。\n\n**W3** [warning] Attention analysis 仅限 L1，可能存在选择性报告\n\n- 具体位置：Section 4.2, \"We analyze L1 attention distributions\"\n- 问题：为什么只分析 L1？如果 routing 真的是 \"maintained through L31\"（如 cross-instruction probe 显示），那 intermediate layers 的 attention pattern 如何？是否所有层都维持 instruction-dominant pattern，还是仅 L1 如此而后续层通过 residual connection 传递信号？只报告支持结论的单一层，令人怀疑是否其他层的 attention pattern 不支持 narrative。\n- 建议：至少报告 L8、L16、L31 的 attention distribution（或在 appendix 给出全层 attention profile），以证明没有选择性报告。\n\n**W4** [warning] LOOCV 100%±0.00 的统计检验力问题\n\n- 具体位置：Section 4.1, \"Leave-one-out cross-validation over 10 folds confirms perfect generalization: 100% ± 0.00\"\n- 问题：10-fold LOOCV 在 10-way classification 中得到 100%，这个设计的 statistical power 需要审视。(1) 每 fold 只 hold out 1 个 class，train on 9 classes——如果 representations 是 4096-D 且 classes 仅 10 个，线性分离几乎是 trivial 的（d >> k）；(2) 需要 baseline：random Gaussian features 在同样维度下做 10-way classification 能达到什么精度？如果也接近 100%，则 probe 结果无信息量。\n- 论文未报告每 fold 的样本数。如果每 task 50 demos，总共 500 samples 做 10-way with 4096-D features，即使是 random features 也可能 linearly separable。\n- 建议：报告 random feature baseline（permutation test for probe accuracy），报告每 fold 的 n，讨论 dimensionality vs. sample size ratio 对分类精度 ceiling 的影响。\n\n**W5** [warning] 数据规模对结论稳定性的影响\n\n- 具体位置：Section 3.1, \"10 tasks, 50 demonstrations each\"\n- 问题：500 total demonstrations 用于拟合 per-layer 32-point profiles。虽然 Appendix F.5 的 demo subsample analysis（25 demos）显示 RSA profile r = 0.970，但 probe R² profile r 仅 0.819，peak layer 从 L9 shift 到 L11。这表明 probe 结果对数据量敏感。论文中多处基于 peak layer 的精确位置做结论（\"L8-L13 region\"、\"peak at L12\"），但这些位置在 plateau region 内对数据量敏感。\n- 建议：在正文中承认 peak layer 的精确位置不应过度解读，重点放在 \"inverted-U exists\" 而非 \"peak is at exactly L12\"。\n\n---\n\n## 小问题（不影响接收）\n\n- Abstract 第 6 句 \"RSA peaks at L8--L13\"：en-dash 此处表示范围，可接受，但 Section 4.3 中 \"$R^2$ peaks in the L8--L10 region\" 与 Table 2 中 \"L8--L10†\" 不一致（seed analysis 显示 4/5 seeds peak at L9-L10，1 seed at L16），建议统一表述。\n- Table 2 footnote 中 \"$R^2$ peak region across 5 seeds (0.655 ± 0.002)\"——±0.002 是 std 还是 95% CI？未明确。\n- Section 4.1 \"QA probes for task progress\": 训练和未训练模型差距仅 1pp (86.3% vs 85.3%)，但文中表述 \"trained last_preaction achieves 86.3% (L20), exceeding DINOv2 cls_token (82.7%)\" 只与 DINOv2 比而不强调与 untrained 的微小差异，有 framing bias。\n- References: grant2026 (arXiv:2603.19233) 和 hou2026 (arXiv:2603.00592) 的 arXiv ID 格式为 26xx，需确认这些是否为真实存在的 preprints（2026 年 3 月）。\n- 论文未包含 code/data availability statement（CoRL 鼓励 reproducibility）。\n\n---\n\n## 主要优势\n\n1. **分析框架的系统性**：四种互补方法（cross-instruction probe、attention analysis、RSA、functional probe）的组合比单一 metric 更有说服力，且 2×2 factorial design 的思路清晰。\n2. **Robustness analyses 全面**：distance metric invariance、per-DOF decomposition、permutation test、seed sensitivity、demo subsampling——附录内容扎实。\n3. **写作清晰**：论文结构好，图表信息密度高，叙事线清晰（specialization → routing → transformation），读起来不费力。\n4. **Cross-benchmark replication**：在 LIBERO-Spatial 上复制核心 inverted-U pattern，增加了 pattern 存在性的可信度（虽然仍是同一 benchmark family）。\n5. **诚实的 null results**：报告了 RSA best-vs-best CI 包含 0、CKA 与 RSA 矛盾、RSA-R² peak convergence 不跨 benchmark 复制等 \"不利\" 结果，说明作者没有只挑好看的数据。\n\n---\n\n## 对作者的核心问题（期待 rebuttal 回应）\n\n1. 是否有 Llama-2 base checkpoint（无 VLA fine-tuning）的 attention 和 routing 数据？如果没有，能否在 rebuttal 期间补充？\n2. Random features baseline 在同维度同样本量下做 10-way classification 的精度是多少？\n3. L8、L16 或 L31 的 attention head distribution 是什么样的？是否也是 instruction-dominant？\n4. 如果用 MLP probe（而非 linear probe）做 instruction classification on image_mean，结果是否仍为 chance？\n5. \"Vision encoder quality is the primary design lever\" 这个建议是否有任何因果验证（如替换 encoder 后的 task success rate 对比）？",
  "reviewer_id": "1",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 1 审稿报告 — Reviewer 1（方法严谨性 + 实验有效性）\n\n**论文标题**: Vision Encodes, Language Routes: A Representational Decomposition of Vision-Language-Action Models\n\n---\n\n## 总体评分\n\n**Overall**: 5/10 (Marginally below acceptance threshold)\n\n**一句话总结**: 论文提出了有价值的分析框架，但核心实验设计存在关键混淆（untrained baseline 不能隔离 VLA fine-tuning 的贡献），单一模型+单一 benchmark family 的泛化性不足以支撑关于\"VLAs\"的一般性结论。\n\n---\n\n## 官方维度打分（基于 CoRL review form：Originality / Quality / Clarity / Significance / Relevance / Limitations）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 7/10 | 首次做 token-level representational decomposition 的 VLA 分析，分析框架（cross-instruction probe + attention + RSA + functional probe 的组合）有新意 |\n| Quality | 4/10 | 关键对照设计有根本缺陷（见 N1）；RSA best-vs-best 存在 cherry-picking（N3）；probing 的 encoding vs. use 混淆（N4）；统计检验力不足 |\n| Clarity | 7/10 | 写作清晰，结构合理，图表信息密度高；但部分 claim 的措辞过强，超出证据支撑范围 |\n| Significance | 5/10 | 如果结论成立，对 VLA 架构设计有实际指导意义；但单模型单 benchmark 限制了影响力，且部分结论（如 vision encoder is primary design lever）缺乏因果支撑 |\n| Relevance | 8/10 | 直接分析 robot learning 核心模型架构，高度相关 |\n| Limitations | 6/10 | Section 5 诚实讨论了主要限制，但低估了 untrained baseline 的根本问题和 probing 方法论的局限性 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Untrained control 不能隔离 VLA fine-tuning 的贡献\n\n- 具体位置：Section 3.1, \"reinitializing all LLM parameters via `from_config()` (6.74B random weights)\"\n- 问题：论文将 trained（OpenVLA-7B，含 Llama-2 预训练 + VLA fine-tuning）与 untrained（完全随机权重）对比，声称差异反映 \"training learns deliberate routing\"。但这个对照混淆了两个因素：(1) Llama-2 语言预训练的贡献（结构化 attention pattern、语言理解能力）；(2) VLA fine-tuning 的贡献。随机初始化的 6.74B 参数 LLM 缺乏任何结构化处理能力，routing 的 decay（82% at L31）可能仅仅反映随机网络的 signal degradation，而非 \"absence of deliberate routing\"。\n- 正确的对照应包括：Llama-2 原始 checkpoint（无 VLA fine-tuning但有语言预训练）——这才能隔离 VLA 训练本身的贡献。\n- 为什么影响接收：论文三个核心发现中的第二个（\"training learns deliberate instruction routing\"）和所有 trained vs. untrained 的定量比较（Table 3 所有 Δ 值）都依赖这个对照。如果差异主要来自语言预训练而非 VLA fine-tuning，则论文的核心叙事（\"VLA training reshapes routing\"）不成立。\n- 建议修改方向：增加 Llama-2 base checkpoint 作为第三个条件（pretrained-but-not-VLA-finetuned），形成三级对照：random → language-pretrained → VLA-finetuned。至少对 attention analysis 和 cross-instruction probe 做这个消融。\n\n**N2** [critical] 单一模型、单一 benchmark family 无法支撑关于 \"VLAs\" 的一般性结论\n\n- 具体位置：Title（\"Vision-Language-Action Models\"，复数）；Abstract（\"VLAs maintain a strict division of labor\"）；Conclusion（\"VLA architectures should optimize routing\"）\n- 问题：所有实验仅在 OpenVLA-7B（一个特定架构：frozen DinoSigLIP + MLP projector + Llama-2）上进行，仅在 LIBERO（tabletop manipulation，简单视觉场景）上评估。论文的 claims 却使用复数 \"VLAs\" 并给出架构设计建议。不同 VLA 架构差异巨大：RT-2 使用 PaLM-E，π₀ 使用 flow matching，Octo 使用 transformer decoder。frozen vision encoder 的设计也是 OpenVLA 的特定选择，其他 VLA 可能 fine-tune encoder。\n- 为什么影响接收：CoRL reviewer guidelines 要求评估 \"significance and novelty of the results\" 及 \"potential for scientific and technological impact\"。单个数据点无法建立一般性规律，特别是当结论明确为架构设计建议时。\n- 建议修改方向：(1) 将所有 claim 限定为 \"OpenVLA-7B\" 或 \"frozen-encoder VLAs\"；(2) 至少在一个不同架构的 VLA 上验证核心发现（如 RT-2 family 或任何 fine-tune encoder 的 VLA）；(3) 如果无法增加模型，则明确讨论哪些发现可能是架构特异性的（如 frozen encoder → instruction-blind image tokens 可能是 trivial 推论）。\n\n**N3** [critical] RSA best-vs-best 比较存在 selection bias\n\n- 具体位置：Table 3, \"Best-vs-best image_mean: trained L12 vs. untrained L0, Δ = +0.017, CI incl. 0, n.s.\"\n- 问题：best-vs-best 比较允许每个条件独立选择最优层。在 32 层中取 max，统计上会引入正偏置（winner's curse / multiple comparisons）。论文报告此差异不显著（CI 包含 0），但仍在 narrative 中积极解读为 \"training redistributes geometry\"（Section 4.3 标题）。更令人担忧的是 LIBERO-Spatial 的 Δ = +0.023, p < 0.001 被用来 \"confirm that the n.s. result on Goal reflects limited power\"（Section 4.4），这是用一个独立数据集的显著结果来否定另一个数据集的零结果，方法论上不成立。\n- 此外，readout token 的 best-vs-best（trained L13 vs. untrained L32）比较的两个层差距 19 层，功能完全不同，这种比较的解释价值存疑。\n- 为什么影响接收：核心定量结论（training effect size）的可信度受损。审稿人和读者无法区分真实效应和统计噪音。\n- 建议修改方向：(1) 报告 same-layer paired comparison 作为主要结果（已有 L12 same-layer Δ = +0.079, p < 0.0001）；(2) 对 best-vs-best 做 multiple comparisons correction（如 Bonferroni 或 permutation-based max-statistic）；(3) 明确区分 \"training shifts peak location\" vs. \"training improves peak magnitude\" 两个独立 claim。\n\n**N4** [critical] Probing 结果不能支撑 \"functional\" 或 \"used\" 的结论\n\n- 具体位置：Section 3.6 标题 \"Functional Action Probes\"；Section 4.1 \"Functional implications\"；Discussion \"vision encoder quality is the primary design lever\"\n- 问题：论文在标题中使用 \"functional\" 来描述 MLP probe，并将 probe R² 解释为 \"functional capacity\"。但 probing 文献已充分论证（Belinkov 2022，论文自己引用），probe accuracy 证明 information is linearly/nonlinearly extractable，不证明 model uses this information for downstream task。同样，高 RSA 证明 geometric alignment，不证明 causal contribution。论文的核心设计建议（\"vision encoder quality is the primary design lever\"）完全基于 DINOv2 有最高 RSA，但没有任何因果证据（如 intervention、ablation）表明更好的 RSA 导致更好的 task performance。\n- 此外，2-layer 256-hidden MLP probe 的容量控制值得质疑：对 4096-D input 预测 7-D output，256-hidden 可能过小（underfitting）或过大（overfitting 到 probe-specific features）。没有报告 probe 的 train/test split 细节或 overfitting 诊断。\n- 为什么影响接收：论文最重要的实际建议（\"invest in stronger self-supervised encoders\"）没有因果支撑。如果仅仅是 \"DINOv2 representations happen to be geometrically similar to the action space\" 但 VLA 并不通过这种 geometry 来生成 action，则建议无实际价值。\n- 建议修改方向：(1) 将 \"functional\" 改为 \"decodable\" 以准确描述 probe 测量的是什么；(2) 增加因果证据：用不同 vision encoder 的 VLA variant（如 CLIP-only vs. DINOv2-only）训练并比较 task success rate；(3) 或至少在 Discussion 中明确这是 correlational evidence，不直接支撑因果设计建议。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] \"Instruction-blind\" claim 过强\n\n- 具体位置：Section 4.1, \"Image tokens are instruction-blind\"；Abstract, \"instruction classification at chance, 10%, across all layers\"\n- 问题：chance-level linear probe accuracy (10%) 不等于 \"no instruction information\"。这仅证明 10-way instruction identity 不是 linearly separable from image_mean activations。论文用了 MLP probe 做 action prediction 但只用 linear probe 做 instruction classification——如果对 instruction 也用 MLP probe 或更高容量模型，结果是否一致？此外，instruction influence 可能以 non-identity 方式存在（如 shift attention to task-relevant spatial regions），这种 graded influence 不会被 10-way classification probe 捕捉到。\n- 建议：(1) 补充 MLP probe 对 instruction classification 的结果；(2) 将 claim 限定为 \"instruction identity is not linearly decodable from image tokens\"；(3) 讨论 subtler forms of instruction influence（如 conditional attention to different image regions）。\n\n**W2** [warning] CKA 与 RSA 结论矛盾，处理不充分\n\n- 具体位置：Appendix B (Section A.2), \"Linear CKA reverses the RSA ordering\"\n- 问题：Linear CKA 显示 untrained > trained > DINOv2，完全逆转 RSA 的 DINOv2 > trained > untrained。论文将此作为 \"different metrics capture different things\" 一笔带过。但这引发根本问题：如果两个标准度量给出相反结论，论文选择 RSA 作为主要结论的依据是什么？仅仅因为 RSA 支持了论文想要的 narrative（DINOv2 最好、training helps）吗？\n- RDM kernel CKA 部分解决（trained ≈ projector > untrained > DINOv2），但仍然显示 DINOv2 最差，与 RSA 的 DINOv2 最优完全相反。\n- 建议：正文中讨论 metric divergence，解释为什么 RSA（rank-order preservation）比 CKA（linear covariance structure）更适合评估 action-relevant geometry，或者承认结论是 metric-dependent 的。\n\n**W3** [warning] Attention analysis 仅限 L1，可能存在选择性报告\n\n- 具体位置：Section 4.2, \"We analyze L1 attention distributions\"\n- 问题：为什么只分析 L1？如果 routing 真的是 \"maintained through L31\"（如 cross-instruction probe 显示），那 intermediate layers 的 attention pattern 如何？是否所有层都维持 instruction-dominant pattern，还是仅 L1 如此而后续层通过 residual connection 传递信号？只报告支持结论的单一层，令人怀疑是否其他层的 attention pattern 不支持 narrative。\n- 建议：至少报告 L8、L16、L31 的 attention distribution（或在 appendix 给出全层 attention profile），以证明没有选择性报告。\n\n**W4** [warning] LOOCV 100%±0.00 的统计检验力问题\n\n- 具体位置：Section 4.1, \"Leave-one-out cross-validation over 10 folds confirms perfect generalization: 100% ± 0.00\"\n- 问题：10-fold LOOCV 在 10-way classification 中得到 100%，这个设计的 statistical power 需要审视。(1) 每 fold 只 hold out 1 个 class，train on 9 classes——如果 representations 是 4096-D 且 classes 仅 10 个，线性分离几乎是 trivial 的（d >> k）；(2) 需要 baseline：random Gaussian features 在同样维度下做 10-way classification 能达到什么精度？如果也接近 100%，则 probe 结果无信息量。\n- 论文未报告每 fold 的样本数。如果每 task 50 demos，总共 500 samples 做 10-way with 4096-D features，即使是 random features 也可能 linearly separable。\n- 建议：报告 random feature baseline（permutation test for probe accuracy），报告每 fold 的 n，讨论 dimensionality vs. sample size ratio 对分类精度 ceiling 的影响。\n\n**W5** [warning] 数据规模对结论稳定性的影响\n\n- 具体位置：Section 3.1, \"10 tasks, 50 demonstrations each\"\n- 问题：500 total demonstrations 用于拟合 per-layer 32-point profiles。虽然 Appendix F.5 的 demo subsample analysis（25 demos）显示 RSA profile r = 0.970，但 probe R² profile r 仅 0.819，peak layer 从 L9 shift 到 L11。这表明 probe 结果对数据量敏感。论文中多处基于 peak layer 的精确位置做结论（\"L8-L13 region\"、\"peak at L12\"），但这些位置在 plateau region 内对数据量敏感。\n- 建议：在正文中承认 peak layer 的精确位置不应过度解读，重点放在 \"inverted-U exists\" 而非 \"peak is at exactly L12\"。\n\n---\n\n## 小问题（不影响接收）\n\n- Abstract 第 6 句 \"RSA peaks at L8--L13\"：en-dash 此处表示范围，可接受，但 Section 4.3 中 \"$R^2$ peaks in the L8--L10 region\" 与 Table 2 中 \"L8--L10†\" 不一致（seed analysis 显示 4/5 seeds peak at L9-L10，1 seed at L16），建议统一表述。\n- Table 2 footnote 中 \"$R^2$ peak region across 5 seeds (0.655 ± 0.002)\"——±0.002 是 std 还是 95% CI？未明确。\n- Section 4.1 \"QA probes for task progress\": 训练和未训练模型差距仅 1pp (86.3% vs 85.3%)，但文中表述 \"trained last_preaction achieves 86.3% (L20), exceeding DINOv2 cls_token (82.7%)\" 只与 DINOv2 比而不强调与 untrained 的微小差异，有 framing bias。\n- References: grant2026 (arXiv:2603.19233) 和 hou2026 (arXiv:2603.00592) 的 arXiv ID 格式为 26xx，需确认这些是否为真实存在的 preprints（2026 年 3 月）。\n- 论文未包含 code/data availability statement（CoRL 鼓励 reproducibility）。\n\n---\n\n## 主要优势\n\n1. **分析框架的系统性**：四种互补方法（cross-instruction probe、attention analysis、RSA、functional probe）的组合比单一 metric 更有说服力，且 2×2 factorial design 的思路清晰。\n2. **Robustness analyses 全面**：distance metric invariance、per-DOF decomposition、permutation test、seed sensitivity、demo subsampling——附录内容扎实。\n3. **写作清晰**：论文结构好，图表信息密度高，叙事线清晰（specialization → routing → transformation），读起来不费力。\n4. **Cross-benchmark replication**：在 LIBERO-Spatial 上复制核心 inverted-U pattern，增加了 pattern 存在性的可信度（虽然仍是同一 benchmark family）。\n5. **诚实的 null results**：报告了 RSA best-vs-best CI 包含 0、CKA 与 RSA 矛盾、RSA-R² peak convergence 不跨 benchmark 复制等 \"不利\" 结果，说明作者没有只挑好看的数据。\n\n---\n\n## 对作者的核心问题（期待 rebuttal 回应）\n\n1. 是否有 Llama-2 base checkpoint（无 VLA fine-tuning）的 attention 和 routing 数据？如果没有，能否在 rebuttal 期间补充？\n2. Random features baseline 在同维度同样本量下做 10-way classification 的精度是多少？\n3. L8、L16 或 L31 的 attention head distribution 是什么样的？是否也是 instruction-dominant？\n4. 如果用 MLP probe（而非 linear probe）做 instruction classification on image_mean，结果是否仍为 chance？\n5. \"Vision encoder quality is the primary design lever\" 这个建议是否有任何因果验证（如替换 encoder 后的 task success rate 对比）？",
    "reviewer_id": "1",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 39 · 2026-05-17T04:35:55.772001+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4540
}
```

</details>

---


### Assistant

_source line 40 · 2026-05-17T04:36:05.957048+00:00_

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
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1"
}
```

</details>

---


## Round 2

## Round 2

4 recorded events


### User

_source line 41 · 2026-05-17T04:38:01.440327+00:00_

[Round 1 审稿请求]:
## Step 2 交叉分享 — 请逐条回应 Reviewer 2 和 Reviewer 3 的意见

以下是 Reviewer 2 和 Reviewer 3 的完整审稿原文。请对每个 Must-Fix (N) 和 Should-Fix (W) 问题逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

### Reviewer 2 的完整审稿意见（4/10, Borderline Reject）

**Must-Fix:**

**N1** [critical] "First token-level representational decomposition" claim 不成立
- Neo et al. (ICLR 2025) 已对 VLM (LLaVA) 做了 token-level 分析；Grant 2026 (Action Atlas) 对 6 个 VLA 做了 per-token SAE 分析（424 SAEs）。本文的 "first" claim 需大幅限定或删除。

**N2** [critical] 方法无创新——标准工具 (RSA+probing+attention) 的直接应用
- 无新 metric、无新实验范式。Cross-instruction probe 本质是标准 linear probe 的 application。对 CoRL 而言缺乏方法贡献。

**N3** [critical] Design implications 完全 speculative，未经验证
- "early exit at L12"、"vision encoder quality is primary lever" 均无因果实验支撑。CKA 反转 RSA 排序进一步动摇结论。

**N4** [critical] 单一模型 + 单一 benchmark 家族，泛化性不足
- Grant 2026 覆盖 6 个模型 + 4 benchmark；本文仅 OpenVLA + LIBERO。

**Should-Fix:**

**W1** Related Work 严重不足（21 篇引用，3 段 15 行）。缺失 Neo et al. (ICLR 2025)、VLM-LENS、logit lens、Raghu et al. 2021 等关键文献。
**W2** CKA 与 RSA 结论矛盾处理不充分。
**W3** 核心 RSA 结果（LIBERO-Goal best-vs-best Δ=+0.017）统计不显著。
**W4** 无 real-robot 实验或 rollout-level behavioral validation。

---

### Reviewer 3 的完整审稿意见（6/10, Weak Accept）

**Must-Fix:**

**N1** Limitations 格式不满足 CoRL 2026 硬性要求——当前是 Discussion 内的 \paragraph{}，应为独立 section/subsection，且缺少 failure modes 描述。
**N2** Em-dash (---) 作为解释性标点至少 8 处——AI 写作的最显著标志，需全部清除。

**Should-Fix:**

**W1** 术语首次出现未定义（LOOCV in abstract, MLP, CKA 未在主文展开）
**W2** 页数可能逼近/超出 8 页限制（估算约 9.1 页）
**W3** -ing 分词短语结尾（次要 AI 痕迹）
**W4** Related Work 过短（仅 16 行源码）
**W5** 无 code/data 释放声明

---

请逐条给出你的 [AGREE] 或 [REBUT] 回应，特别关注：
1. R2-N1 的 novelty claim 问题——你是否同意 Neo et al. 和 Grant 2026 已涵盖了本文的 token-level 分析？
2. R2-N2 的方法创新问题——你是否认为 $2\times 2$ factorial + 四种方法组合构成足够贡献？
3. R2-N3 与你的 N4（probing encoding ≠ use）是否为同一问题的不同表述？
4. R3 的格式问题是否影响你对论文科学质量的评估？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-17T04:40:03.534569+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Step 2 交叉回应 — Reviewer 1 对 Reviewer 2 & Reviewer 3 意见的逐条回应\n\n---\n\n### 对 Reviewer 2 的回应\n\n**[AGREE] R2-N1: \"First token-level representational decomposition\" claim 过强**\n\n同意该 claim 需要限定，但程度上与 R2 有分歧。\n\n理由：\n- Neo et al. (ICLR 2025) 分析的是 VLM (LLaVA)，不是 VLA。VLM 不产生 action，没有 action-relevant geometry 的概念，其 token-level 分析的目标和方法框架与本文不同。因此 Neo et al. 不直接 invalidate 本文对 VLA 的 \"first\" claim。\n- Grant 2026 (Action Atlas) 使用 SAE 做 per-token 分析，确实是 VLA 的 token-level 分析。但 SAE 找 sparse directions 与本文的 multi-metric decomposition（RSA geometric alignment + probe decodability + attention routing + cross-instruction encoding）是不同的分析框架。\n- 建议将 claim 限定为 \"first systematic multi-metric token-level decomposition with trained/untrained controls\"，而非 blanket \"first token-level decomposition\"。\n\n**[REBUT] R2-N2: 方法无创新**\n\n部分反驳。\n\n理由：\n- 同意单个工具（RSA、probing、attention visualization）均非新方法。但 R2 低估了实验设计的贡献：2×2 factorial (training status × instruction presence) 交叉 token position (image vs. readout) 交叉 layer depth (32 layers)，这个三维分解框架本身是分析设计上的贡献，不是 \"标准工具的直接应用\"。\n- Cross-instruction probe 的设计（同一 visual frame × 10 instructions，测试哪个 token type 编码 instruction identity）虽然在方法上是 linear probe，但其实验逻辑（通过 instruction 交叉来隔离 token-level specialization）在 VLA 文献中未见先例。\n- 然而，我承认对 CoRL 而言，纯分析论文（no new algorithm, no new system, no architectural intervention）确实面临更高的 bar。CoRL 审稿标准强调 \"significance and novelty of results, either theoretical or empirical\"——如果结论本身足够 significant 且 well-supported，分析贡献是可以被接受的。但问题在于结论是否 well-supported（见我的 N1-N4），这才是核心矛盾。\n- 总结：方法新颖性确实不高（5/10），但这不应该是 rejection 的主要理由——结论的可靠性才是。\n\n**[AGREE] R2-N3: Design implications 完全 speculative**\n\n强烈同意。这与我的 N4 是同一问题的不同表述。\n\n理由：\n- 我的 N4 指出：probe R² 和 RSA ρ 证明 information extractability / geometric alignment，不证明 causal contribution to action generation。论文却据此给出 \"vision encoder quality is the primary design lever\" 和 \"action heads should read from L12-L13\" 等因果性设计建议。\n- R2 补充的 CKA 反转论证进一步强化这一点：如果 metric 选择就能翻转 \"哪个 encoder 最好\" 的结论（RSA: DINOv2 > trained > CLIP；CKA: untrained > trained > DINOv2），那么基于单一 metric 的设计建议毫无可操作性。\n- 这是本文最严重的问题之一：分析工作的价值在于 insights，如果 insights 不可靠或不可操作，论文的 significance 大打折扣。\n\n**[AGREE] R2-N4: 单一模型 + 单一 benchmark 家族**\n\n完全同意，与我的 N2 一致。\n\n补充一点：R2 提到 Grant 2026 覆盖 6 个模型 + 4 benchmark。如果直接竞争者已经做到了更广覆盖度，本文单一模型的分析深度必须远超 Grant 2026 才能 justify——但目前 N1（baseline 缺陷）和 N4（无因果验证）削弱了这种深度优势。\n\n**[AGREE] R2-W1: Related Work 过短，缺失关键引用**\n\n同意。\n\nRelated Work 仅 3 段 ~16 行（Section 2），引用 21 篇。对于一篇分析论文而言，Related Work 应该更详尽地 positioning：\n- 缺失 VLM token-level 分析文献（Neo et al.）\n- 缺失 representation analysis 方法论文献（logit lens、Raghu et al. 2021 CKA-based layer analysis）\n- 缺失 neuroscience-inspired probing 的局限性讨论（Hewitt & Liang 2019 control tasks）\n- 引用密度明显低于 CoRL 近年录用论文的水平\n\n**[AGREE] R2-W2: CKA 与 RSA 矛盾处理不充分**\n\n完全同意，与我的 W2 一致。不再重复。\n\n**[AGREE] R2-W3: 核心 RSA 结果统计不显著**\n\n同意，与我的 N3 一致。这不仅是 \"should-fix\"——一个核心定量 claim 的 p-value 不显著且 CI 包含 0，却在叙事中被积极解读，这动摇了论文的 rigor。我将其放在 Must-Fix 级别。\n\n**[REBUT] R2-W4: 无 real-robot 实验**\n\n部分反驳。\n\n理由：\n- 本文定位为 representation analysis / mechanistic understanding paper，不是 systems paper。要求 real-robot rollout 等于要求分析论文同时做 system contribution，这超出了论文的 scope。\n- 但 R2 的 underlying concern 是合理的：论文的设计建议（\"optimize routing\"、\"early exit at L12\"）如果加一个 proof-of-concept intervention（哪怕在 simulation 中），说服力会大幅提升。这不需要 real robot——在 LIBERO 中实现 early-exit action head 并测 task success rate 就足够了。\n- 因此我将其归类为 \"强烈建议但非必须\"：如果作者能在 rebuttal 期间添加一个 simulation-based intervention（如 early exit），论文的 significance 可以从 5/10 提升到 7/10。\n\n---\n\n### 对 Reviewer 3 的回应\n\n**[AGREE] R3-N1: Limitations 格式不满足 CoRL 2026 要求**\n\n同意这是合规问题。\n\n理由：\n- 当前 Limitations 是 Discussion (Section 5) 内的 `\\paragraph{Limitations.}`，不是独立 section/subsection。\n- CoRL 2026 明确要求 \"必须含 Limitations section（计入 8 页）\"。格式不合规有 desk reject 风险。\n- 但这是 trivially fixable（改为 `\\subsection{Limitations}` 或独立 `\\section{Limitations}`），不影响科学质量评估。\n- 关于缺少 failure modes：同意。当前 Limitations 只讨论了泛化性和方法论局限，没有具体描述分析可能 fail 的场景（如 when would the inverted-U not hold? What architectural features would break token specialization?）。\n\n**[AGREE] R3-N2: Em-dash 作为 AI 写作标志需清除**\n\n同意，但对 \"critical\" 级别有异议。\n\n理由：\n- 确实在 tex 源码中观察到解释性 em-dash（如 Section 4.1 \"instruction-blind image tokens and instruction-conditioned readout token---means the readout token is the sole locus\"）。\n- 这是 presentation issue，不是 scientific issue。对论文是否应被接收的判断应基于 contribution quality，不是排版风格。\n- 但 R3 的 underlying logic 有一定道理：如果审稿人怀疑论文大量使用 AI 生成，会降低对 intellectual contribution 的信任。在 double-blind review 中这确实可能影响评分。\n- 建议作者清除所有解释性 em-dash，但不应列为 \"Must-Fix affecting acceptance decision\"。\n\n**[AGREE] R3-W1: 术语首次出现未定义**\n\n同意。LOOCV 在 Abstract 中使用但未展开（Leave-One-Out Cross-Validation），MLP 首次出现在 Section 3.6 但未展开（Multi-Layer Perceptron），CKA 在正文 Section 3.6 引用但仅在 Appendix 展开（Centered Kernel Alignment）。这是基本写作规范问题，容易修复。\n\n**[REBUT] R3-W2: 页数可能超出 8 页**\n\n无法确认，暂不同意。\n\n理由：\n- 没有编译后的 PDF，无法验证。R3 估算 \"约 9.1 页\" 但未说明估算方法。\n- 正文含 6 个 section（Introduction、Related Work、Method、Experiments、Discussion、Conclusion），其中 Related Work 仅 16 行，Discussion 含 Limitations 但不长。6 个 figure + 3 个 table 确实占空间较大。\n- 如果确实超页，这是 desk-reject 级问题。但在未编译验证前，我不将其列为 confirmed issue。建议作者自查并压缩（如将 Fig 5 的两个 panel 合并、缩小 Table 2）。\n\n**[AGREE] R3-W3: -ing 分词短语结尾**\n\n同意是 minor AI 风格痕迹，但优先级远低于科学问题。\n\n**[AGREE] R3-W4: Related Work 过短**\n\n同意，与 R2-W1 一致。\n\n**[AGREE] R3-W5: 无 code/data 释放声明**\n\n同意，我在 minor issues 中也提到了这一点。CoRL 鼓励 reproducibility，缺少声明是减分项。\n\n---\n\n### Director 提出的四个具体问题\n\n**Q1: R2-N1 的 novelty claim——Neo et al. 和 Grant 2026 是否已涵盖本文的 token-level 分析？**\n\n不完全涵盖，但 \"first\" claim 确实过强。\n- Neo et al. 分析 VLM 不是 VLA，目标不同（visual QA vs. action generation），不直接覆盖本文工作。\n- Grant 2026 的 SAE 分析是 per-token 的但方法框架不同（feature discovery vs. multi-metric decomposition with controlled ablation）。\n- 本文的 specific novelty 在于：(1) trained vs. untrained 对照；(2) image vs. readout token 的系统对比；(3) 四种 metric 的交叉验证。这些 Grant 2026 没有做。\n- 但 \"first token-level decomposition\" 作为 absolute novelty claim 不成立。应改为 conditional claim。\n\n**Q2: 2×2 factorial + 四种方法组合是否构成足够贡献？**\n\n作为分析设计贡献，有价值但不充分独立支撑 acceptance。\n- 如果结论可靠且 impactful，实验设计的系统性足以构成贡献（类似 neuroscience 中 well-designed but standard-tool 的分析论文）。\n- 但当前结论可靠性受 N1（baseline 缺陷）和 N3/N4（no causal validation）严重削弱。如果结论不可靠，再好的实验设计也无法 save 论文。\n- 对 CoRL 而言，分析论文的 bar 是：insights 必须直接可操作。当前 insights 的 actionability 存疑。\n\n**Q3: R2-N3 与我的 N4 是否为同一问题？**\n\n是同一问题的不同表述。\n- 我的 N4：probing encoding ≠ functional use → 因果设计建议缺乏支撑。\n- R2-N3：design implications completely speculative → 无因果实验验证。\n- 两者都指向：correlational representation analysis → causal architectural recommendations 的推理跳跃无 justification。\n- 这是本文最核心的 weakness：分析做得系统，但 so what? 如果不能可靠地转化为可验证的设计原则，论文的 practical significance 大打折扣。\n\n**Q4: R3 的格式问题是否影响科学质量评估？**\n\n不影响科学质量评估，但影响 acceptance probability。\n- Limitations 格式（R3-N1）：合规问题，trivially fixable，不反映科学 rigor。\n- Em-dash（R3-N2）：presentation issue，不影响方法和结论的有效性。\n- 但两者结合如果导致 desk-reject 或降低审稿人初始印象，则间接影响 acceptance。\n- 我的评分（5/10）完全基于科学问题（N1-N4），不受格式影响。即使所有格式问题修复，我的评分不会因此提高。\n\n---\n\n### 总结：三位 Reviewer 的共识问题\n\n| 问题 | R1 | R2 | R3 |\n|------|----|----|-----|\n| 单一模型泛化性不足 | N2 (critical) | N4 (critical) | — |\n| 设计建议缺乏因果支撑 | N4 (critical) | N3 (critical) | — |\n| Related Work 过短 | — | W1 | W4 |\n| CKA/RSA 矛盾 | W2 | W2 | — |\n| 无 code/data 声明 | minor | — | W5 |\n\n三位 Reviewer 的共识 critical issue：(1) 泛化性不足；(2) 因果验证缺失。这两个问题如果不能在 rebuttal 中实质性解决（而非仅限定 claim），论文难以达到 acceptance threshold。",
  "reviewer_id": "1",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Step 2 交叉回应 — Reviewer 1 对 Reviewer 2 & Reviewer 3 意见的逐条回应\n\n---\n\n### 对 Reviewer 2 的回应\n\n**[AGREE] R2-N1: \"First token-level representational decomposition\" claim 过强**\n\n同意该 claim 需要限定，但程度上与 R2 有分歧。\n\n理由：\n- Neo et al. (ICLR 2025) 分析的是 VLM (LLaVA)，不是 VLA。VLM 不产生 action，没有 action-relevant geometry 的概念，其 token-level 分析的目标和方法框架与本文不同。因此 Neo et al. 不直接 invalidate 本文对 VLA 的 \"first\" claim。\n- Grant 2026 (Action Atlas) 使用 SAE 做 per-token 分析，确实是 VLA 的 token-level 分析。但 SAE 找 sparse directions 与本文的 multi-metric decomposition（RSA geometric alignment + probe decodability + attention routing + cross-instruction encoding）是不同的分析框架。\n- 建议将 claim 限定为 \"first systematic multi-metric token-level decomposition with trained/untrained controls\"，而非 blanket \"first token-level decomposition\"。\n\n**[REBUT] R2-N2: 方法无创新**\n\n部分反驳。\n\n理由：\n- 同意单个工具（RSA、probing、attention visualization）均非新方法。但 R2 低估了实验设计的贡献：2×2 factorial (training status × instruction presence) 交叉 token position (image vs. readout) 交叉 layer depth (32 layers)，这个三维分解框架本身是分析设计上的贡献，不是 \"标准工具的直接应用\"。\n- Cross-instruction probe 的设计（同一 visual frame × 10 instructions，测试哪个 token type 编码 instruction identity）虽然在方法上是 linear probe，但其实验逻辑（通过 instruction 交叉来隔离 token-level specialization）在 VLA 文献中未见先例。\n- 然而，我承认对 CoRL 而言，纯分析论文（no new algorithm, no new system, no architectural intervention）确实面临更高的 bar。CoRL 审稿标准强调 \"significance and novelty of results, either theoretical or empirical\"——如果结论本身足够 significant 且 well-supported，分析贡献是可以被接受的。但问题在于结论是否 well-supported（见我的 N1-N4），这才是核心矛盾。\n- 总结：方法新颖性确实不高（5/10），但这不应该是 rejection 的主要理由——结论的可靠性才是。\n\n**[AGREE] R2-N3: Design implications 完全 speculative**\n\n强烈同意。这与我的 N4 是同一问题的不同表述。\n\n理由：\n- 我的 N4 指出：probe R² 和 RSA ρ 证明 information extractability / geometric alignment，不证明 causal contribution to action generation。论文却据此给出 \"vision encoder quality is the primary design lever\" 和 \"action heads should read from L12-L13\" 等因果性设计建议。\n- R2 补充的 CKA 反转论证进一步强化这一点：如果 metric 选择就能翻转 \"哪个 encoder 最好\" 的结论（RSA: DINOv2 > trained > CLIP；CKA: untrained > trained > DINOv2），那么基于单一 metric 的设计建议毫无可操作性。\n- 这是本文最严重的问题之一：分析工作的价值在于 insights，如果 insights 不可靠或不可操作，论文的 significance 大打折扣。\n\n**[AGREE] R2-N4: 单一模型 + 单一 benchmark 家族**\n\n完全同意，与我的 N2 一致。\n\n补充一点：R2 提到 Grant 2026 覆盖 6 个模型 + 4 benchmark。如果直接竞争者已经做到了更广覆盖度，本文单一模型的分析深度必须远超 Grant 2026 才能 justify——但目前 N1（baseline 缺陷）和 N4（无因果验证）削弱了这种深度优势。\n\n**[AGREE] R2-W1: Related Work 过短，缺失关键引用**\n\n同意。\n\nRelated Work 仅 3 段 ~16 行（Section 2），引用 21 篇。对于一篇分析论文而言，Related Work 应该更详尽地 positioning：\n- 缺失 VLM token-level 分析文献（Neo et al.）\n- 缺失 representation analysis 方法论文献（logit lens、Raghu et al. 2021 CKA-based layer analysis）\n- 缺失 neuroscience-inspired probing 的局限性讨论（Hewitt & Liang 2019 control tasks）\n- 引用密度明显低于 CoRL 近年录用论文的水平\n\n**[AGREE] R2-W2: CKA 与 RSA 矛盾处理不充分**\n\n完全同意，与我的 W2 一致。不再重复。\n\n**[AGREE] R2-W3: 核心 RSA 结果统计不显著**\n\n同意，与我的 N3 一致。这不仅是 \"should-fix\"——一个核心定量 claim 的 p-value 不显著且 CI 包含 0，却在叙事中被积极解读，这动摇了论文的 rigor。我将其放在 Must-Fix 级别。\n\n**[REBUT] R2-W4: 无 real-robot 实验**\n\n部分反驳。\n\n理由：\n- 本文定位为 representation analysis / mechanistic understanding paper，不是 systems paper。要求 real-robot rollout 等于要求分析论文同时做 system contribution，这超出了论文的 scope。\n- 但 R2 的 underlying concern 是合理的：论文的设计建议（\"optimize routing\"、\"early exit at L12\"）如果加一个 proof-of-concept intervention（哪怕在 simulation 中），说服力会大幅提升。这不需要 real robot——在 LIBERO 中实现 early-exit action head 并测 task success rate 就足够了。\n- 因此我将其归类为 \"强烈建议但非必须\"：如果作者能在 rebuttal 期间添加一个 simulation-based intervention（如 early exit），论文的 significance 可以从 5/10 提升到 7/10。\n\n---\n\n### 对 Reviewer 3 的回应\n\n**[AGREE] R3-N1: Limitations 格式不满足 CoRL 2026 要求**\n\n同意这是合规问题。\n\n理由：\n- 当前 Limitations 是 Discussion (Section 5) 内的 `\\paragraph{Limitations.}`，不是独立 section/subsection。\n- CoRL 2026 明确要求 \"必须含 Limitations section（计入 8 页）\"。格式不合规有 desk reject 风险。\n- 但这是 trivially fixable（改为 `\\subsection{Limitations}` 或独立 `\\section{Limitations}`），不影响科学质量评估。\n- 关于缺少 failure modes：同意。当前 Limitations 只讨论了泛化性和方法论局限，没有具体描述分析可能 fail 的场景（如 when would the inverted-U not hold? What architectural features would break token specialization?）。\n\n**[AGREE] R3-N2: Em-dash 作为 AI 写作标志需清除**\n\n同意，但对 \"critical\" 级别有异议。\n\n理由：\n- 确实在 tex 源码中观察到解释性 em-dash（如 Section 4.1 \"instruction-blind image tokens and instruction-conditioned readout token---means the readout token is the sole locus\"）。\n- 这是 presentation issue，不是 scientific issue。对论文是否应被接收的判断应基于 contribution quality，不是排版风格。\n- 但 R3 的 underlying logic 有一定道理：如果审稿人怀疑论文大量使用 AI 生成，会降低对 intellectual contribution 的信任。在 double-blind review 中这确实可能影响评分。\n- 建议作者清除所有解释性 em-dash，但不应列为 \"Must-Fix affecting acceptance decision\"。\n\n**[AGREE] R3-W1: 术语首次出现未定义**\n\n同意。LOOCV 在 Abstract 中使用但未展开（Leave-One-Out Cross-Validation），MLP 首次出现在 Section 3.6 但未展开（Multi-Layer Perceptron），CKA 在正文 Section 3.6 引用但仅在 Appendix 展开（Centered Kernel Alignment）。这是基本写作规范问题，容易修复。\n\n**[REBUT] R3-W2: 页数可能超出 8 页**\n\n无法确认，暂不同意。\n\n理由：\n- 没有编译后的 PDF，无法验证。R3 估算 \"约 9.1 页\" 但未说明估算方法。\n- 正文含 6 个 section（Introduction、Related Work、Method、Experiments、Discussion、Conclusion），其中 Related Work 仅 16 行，Discussion 含 Limitations 但不长。6 个 figure + 3 个 table 确实占空间较大。\n- 如果确实超页，这是 desk-reject 级问题。但在未编译验证前，我不将其列为 confirmed issue。建议作者自查并压缩（如将 Fig 5 的两个 panel 合并、缩小 Table 2）。\n\n**[AGREE] R3-W3: -ing 分词短语结尾**\n\n同意是 minor AI 风格痕迹，但优先级远低于科学问题。\n\n**[AGREE] R3-W4: Related Work 过短**\n\n同意，与 R2-W1 一致。\n\n**[AGREE] R3-W5: 无 code/data 释放声明**\n\n同意，我在 minor issues 中也提到了这一点。CoRL 鼓励 reproducibility，缺少声明是减分项。\n\n---\n\n### Director 提出的四个具体问题\n\n**Q1: R2-N1 的 novelty claim——Neo et al. 和 Grant 2026 是否已涵盖本文的 token-level 分析？**\n\n不完全涵盖，但 \"first\" claim 确实过强。\n- Neo et al. 分析 VLM 不是 VLA，目标不同（visual QA vs. action generation），不直接覆盖本文工作。\n- Grant 2026 的 SAE 分析是 per-token 的但方法框架不同（feature discovery vs. multi-metric decomposition with controlled ablation）。\n- 本文的 specific novelty 在于：(1) trained vs. untrained 对照；(2) image vs. readout token 的系统对比；(3) 四种 metric 的交叉验证。这些 Grant 2026 没有做。\n- 但 \"first token-level decomposition\" 作为 absolute novelty claim 不成立。应改为 conditional claim。\n\n**Q2: 2×2 factorial + 四种方法组合是否构成足够贡献？**\n\n作为分析设计贡献，有价值但不充分独立支撑 acceptance。\n- 如果结论可靠且 impactful，实验设计的系统性足以构成贡献（类似 neuroscience 中 well-designed but standard-tool 的分析论文）。\n- 但当前结论可靠性受 N1（baseline 缺陷）和 N3/N4（no causal validation）严重削弱。如果结论不可靠，再好的实验设计也无法 save 论文。\n- 对 CoRL 而言，分析论文的 bar 是：insights 必须直接可操作。当前 insights 的 actionability 存疑。\n\n**Q3: R2-N3 与我的 N4 是否为同一问题？**\n\n是同一问题的不同表述。\n- 我的 N4：probing encoding ≠ functional use → 因果设计建议缺乏支撑。\n- R2-N3：design implications completely speculative → 无因果实验验证。\n- 两者都指向：correlational representation analysis → causal architectural recommendations 的推理跳跃无 justification。\n- 这是本文最核心的 weakness：分析做得系统，但 so what? 如果不能可靠地转化为可验证的设计原则，论文的 practical significance 大打折扣。\n\n**Q4: R3 的格式问题是否影响科学质量评估？**\n\n不影响科学质量评估，但影响 acceptance probability。\n- Limitations 格式（R3-N1）：合规问题，trivially fixable，不反映科学 rigor。\n- Em-dash（R3-N2）：presentation issue，不影响方法和结论的有效性。\n- 但两者结合如果导致 desk-reject 或降低审稿人初始印象，则间接影响 acceptance。\n- 我的评分（5/10）完全基于科学问题（N1-N4），不受格式影响。即使所有格式问题修复，我的评分不会因此提高。\n\n---\n\n### 总结：三位 Reviewer 的共识问题\n\n| 问题 | R1 | R2 | R3 |\n|------|----|----|-----|\n| 单一模型泛化性不足 | N2 (critical) | N4 (critical) | — |\n| 设计建议缺乏因果支撑 | N4 (critical) | N3 (critical) | — |\n| Related Work 过短 | — | W1 | W4 |\n| CKA/RSA 矛盾 | W2 | W2 | — |\n| 无 code/data 声明 | minor | — | W5 |\n\n三位 Reviewer 的共识 critical issue：(1) 泛化性不足；(2) 因果验证缺失。这两个问题如果不能在 rebuttal 中实质性解决（而非仅限定 claim），论文难以达到 acceptance threshold。",
    "reviewer_id": "1",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-17T04:40:07.757431+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4222
}
```

</details>

---


### Assistant

_source line 44 · 2026-05-17T04:40:13.088133+00:00_

交叉回应已提交。核心判断：与 R2 在泛化性不足和因果验证缺失上达成共识（两项 critical），对 R2-N2（方法无创新）和 R2-W4（需要 real-robot）部分反驳，对 R3 的格式问题全部同意但不认为影响科学质量评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1"
}
```

</details>

---


## Round 3

## Round 3

16 recorded events


### User

_source line 45 · 2026-05-17T06:03:39.281071+00:00_

[Round 2 审稿请求]:
## Round 2 修订评估 ��� Reviewer 1（方法严谨性 + 实验有效性）

**模式**：继续审稿。你在 Round 1 给出 5/10。现在评估修��是否充分回应了你的问题。

### Venue 信息（不变）
- CoRL 2026, Deadline 2026-05-29, 8 页���文, double-blind

### 论文路径
`projects/vla-ssd/docs/paper/main.tex`

### 你的 Round 1 主要发现摘要
- **N1** (critical): Untrained baseline confound（random vs trained 混淆 Llama-2 预训练 + VLA fine-tuning）
- **N3** (critical): RSA best-vs-best selection bias（32层取max，主结果 n.s.）
- **N4** (critical): Probing encoding ≠ use，design implications 缺乏因果验证
- **W1** (warning): "Instruction-blind" claim 过强（仅 linear probe）
- **W2** (warning): CKA 反转 RSA 处理不充分

### 当前 Open/In-Progress Issues（逐条标注 [RESOLVED] / [STILL_OPEN]）

请���取更新后的论文，对以下 issue 逐条判定：

1. **R1-N1** [in_progress]: Untrained baseline confound
   - Action: 增加 Llama-2 base checkpoint 对照
   - 检查：是否有新实验数据？���否���在 Limitations 中 acknowledge？acknowledge 是否充分？

2. **R1-N3** [in_progress]: RSA best-vs-best selection bias
   - Action: same-layer comparison 作为 primary framing
   - 检查：Table 3 / §4.3 的叙事结构是否调整？best-vs-best 是否降级？

3. **R1-N4** [in_progress]: Design implications speculative
   - Action: 弱化为 hypothesis/suggestion
   - 检查：Discussion "Implications" 段、Abstract 最后一句、Conclusion 最后一句的语气是否软化？

4. **R1-W1** [in_progress]: "Instruction-blind" claim 过强
   - Action: 补充 MLP probe 或弱化 claim
   - 检查：§4.1 标题和正文措辞是否调整？是否有 MLP probe 结果？

5. **R1-W2** [in_progress]: CKA/RSA 矛盾
   - Action: 正文讨论 metric divergence
   - 检查：是否在 Method 或 Discussion 中解释了为何选择 RSA？

### 输出格式
对每个 issue：[RESOLVED] / [PARTIALLY_RESOLVED] / [STILL_OPEN] + 理由（cite 具体位置）
最后给出更新后的 Overall Score 和理由。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-17T06:03:47.514840+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 47 · 2026-05-17T06:03:47.967830+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-17T06:03:47.968218+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-17T06:03:48.269410+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-17T06:03:48.269902+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 51 · 2026-05-17T06:03:48.320433+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 52 · 2026-05-17T06:03:52.385174+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-17T06:03:52.636876+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 54 · 2026-05-17T06:03:52.637280+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-17T06:03:52.689186+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 56 · 2026-05-17T06:03:57.824653+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 57 · 2026-05-17T06:03:57.825151+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-17T06:05:32.721392+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 2 修订评估 — Reviewer 1（方法严谨性 + 实验有效性）\n\n---\n\n### 逐条评估\n\n---\n\n**1. R1-N1 [PARTIALLY_RESOLVED]: Untrained baseline confound**\n\n修改内容：\n- Section 4.2 (experiments.tex) 新增关键 caveat：\"Note that this comparison uses a randomly initialized LLM baseline rather than the pretrained Llama-2 checkpoint; the observed routing changes may therefore reflect a combination of language pretraining and VLA fine-tuning (see §5 for discussion).\"\n- Discussion Limitations 段明确承认：\"Our untrained control reinitializes all 6.74B LLM parameters to random weights, conflating language pretraining and VLA fine-tuning effects. A pretrained Llama-2 base checkpoint (without VLA fine-tuning) would isolate the VLA-specific contribution; we are currently conducting this experiment.\"\n\n评估：\n- (+) 问题被显式 acknowledge，且 caveat 放在实验章节正文中（不仅在 Limitations），这让读者在第一次遇到 trained vs. untrained 比较时就能理解局限性。\n- (+) 承诺正在进行 Llama-2 base 实验。\n- (-) 但核心问题仍然存在：**没有新实验数据**。Section 4.2 标题仍为 \"Training Establishes Deliberate Instruction Routing\"，这个 causal claim（\"training establishes\"）仍然超出证据支撑——如果不知道 Llama-2 base 的 attention pattern，不能排除 routing 主要来自语言预训练而非 VLA fine-tuning。\n- (-) Abstract（line 5）仍写 \"VLA training establishes deliberate instruction routing\"，虽然从 \"training learns\" 改为 \"VLA training establishes\"，但措辞仍暗示 VLA-specific 的贡献。\n- 建议：如果无法在 deadline 前完成 Llama-2 base 实验，应将标题改为 \"Trained models exhibit deliberate instruction routing\" 或 \"The trained VLA's routing differs from random baseline\"，避免 causal attribution to \"VLA training\"。\n\n**判定：PARTIALLY_RESOLVED**——acknowledge 充分，但核心 claim 的措辞仍超出证据。\n\n---\n\n**2. R1-N3 [PARTIALLY_RESOLVED]: RSA best-vs-best selection bias**\n\n修改内容：\n- Section 4.3 叙事调整：现在先报告 best-vs-best（\"modest\"，acknowledged n.s.），然后强调 same-layer L12 比较（Δ = +0.079, p < 0.0001），结论为 \"training has a substantial effect on *where* geometry peaks but only a modest effect on *how high*\"。\n- 解读策略分离为两个独立 claim（位置 shift vs. 幅度提升），这更精确。\n\n评估：\n- (+) 正文叙事确实将解读重心转向 same-layer comparison，\"where\" vs. \"how high\" 的区分是有洞察力的 framing。\n- (-) Table 3 (tab:training_effects) 结构未变：best-vs-best 仍为第一行，same-layer 为第二行。表格是审稿人快速浏览的焦点——应将显著的 same-layer 结果放在更突出位置。\n- (-) best-vs-best 的 n.s. 结果仍被保留在 table 中且没有 correction for multiple comparisons 的讨论。\n- (-) 用 LIBERO-Spatial (p < 0.001) 来 argue LIBERO-Goal n.s. \"reflects limited power\" 的逻辑仍在 Appendix 中出现（虽然正文不再强调），这在方法论上仍有问题。\n\n**判定：PARTIALLY_RESOLVED**——叙事改善明显，但 Table 结构和 multiple comparison 问题未完全解决。\n\n---\n\n**3. R1-N4 [PARTIALLY_RESOLVED]: Design implications speculative**\n\n修改内容：\n- Discussion \"Implications\" 段新增 caveat：\"though validating any specific architectural change would require policy rollout experiments\"\n- Conclusion 从 \"These results reveal\" 改为 \"These results suggest\"\n- Limitations 新增 \"Post-hoc analysis\" 段：\"Our analyses characterize frozen representations; they do not address whether architectural interventions based on these observations would preserve the same action quality in closed-loop evaluation.\"\n\n评估：\n- (+) Discussion 中的 caveat 是正确的——承认了 representational analysis → architectural recommendation 的推理跳跃需要 rollout validation。\n- (+) Limitations 的 \"Post-hoc analysis\" 段直接回应了我和 R2 共同指出的核心问题。\n- (-) **但 Abstract 最后一句（line 8）仍为**：\"VLA architectures should optimize routing from image tokens to the readout position; vision encoder quality is the primary design lever.\" 没有任何 hedging。Abstract 是审稿人最先读到的部分，这里的强断言与 Discussion 的 caveats 不一致。\n- (-) Discussion 第一条 implication 仍然是 \"vision encoder pretraining quality is the primary design lever\"——直接断言，未加 \"our results suggest\" 或 \"consistent with the hypothesis that\"。\n- (-) \"Primary design lever\" 这个表述暗示因果优先级排序（投资 encoder > 投资 LLM），但论文的证据是 RSA correlation，不是因果干预。\n\n**判定：PARTIALLY_RESOLVED**——Limitations 和 Discussion 有改善，但 Abstract 和 Discussion implications 的核心措辞仍然过于因果化。\n\n---\n\n**4. R1-W1 [STILL_OPEN]: \"Instruction-blind\" claim 过强**\n\n修改内容：\n- Section 4.1 段落标题仍为 \"Image tokens are instruction-blind.\"\n- 正文将解释性 em-dash 改为括号：\"This strict division of labor (instruction-blind image tokens, instruction-conditioned readout token) indicates...\"\n- 未添加 MLP probe 对 instruction classification 的结果。\n- 未对 \"instruction-blind\" 的定义或 scope 进行限定。\n\n评估：\n- (-) 核心问题未回应：仍仅基于 linear probe 的 chance-level 结果声称 \"instruction-blind\"。\n- (-) 没有新实验（MLP instruction probe 或 higher-capacity probe）来验证 claim 的鲁棒性。\n- (-) 没有对 claim 进行措辞限定（如改为 \"instruction identity is not linearly decodable from image tokens\" 或 \"image tokens lack linearly accessible instruction information\"）。\n- 这不影响接收决定（W-level），但作为 analytical rigor，一个标题级 claim 的证据应当匹配其强度。\n\n**判定：STILL_OPEN**——未做任何回应。\n\n---\n\n**5. R1-W2 [RESOLVED]: CKA/RSA 矛盾**\n\n修改内容：\n- Method Section 3.6 新增 \"Why RSA over CKA\" 段（lines 59-62）：\n  - 给出了选择 RSA 的 principled justification：Spearman rank correlation 的 scale-invariance 和 monotonic-transformation robustness 适合比较 dimensionality 差异大的空间。\n  - 解释了 CKA linear variant 的 known dimension mismatch 问题。\n  - 承认 \"the partial divergence between RSA and CKA orderings confirms that neither metric alone fully characterizes representational structure\"。\n\n评估：\n- (+) 这是一个 well-reasoned methodological justification。不是 post-hoc cherry-picking，而是基于 metric 的数学性质选择。\n- (+) 同时承认了单一 metric 的局限性，CKA 作为 appendix complement 的定位合理。\n- (+) 对审稿人的 concern 做了实质性回应：不是\"两个 metric 都对\"的回避，而是\"为什么 RSA 更适合这个具体比较\"。\n\n**判定：RESOLVED**\n\n---\n\n### 总体评估\n\n**修订力度**：中等。作者在 Limitations 和 caveats 方面做了实质性改进（尤其是 N1 的 confound acknowledge、N4 的 post-hoc caveat、W2 的 metric justification）。但三个核心问题的**实质性解决**（新实验数据、statistical correction、claim 强度与证据匹配）均未完成。\n\n**关键残留问题**：\n1. Abstract 和 Conclusion 的措辞仍然过于 assertive——Limitations 中的 caveats 不能弥补 headline claims 的过度。\n2. 无 Llama-2 base 实验数据（仅 promise \"currently conducting\"）。\n3. \"Instruction-blind\" claim 完全未修改。\n\n---\n\n### 更新后评分\n\n**Overall: 5.5/10 → 维持 5/10（marginally below acceptance threshold）**\n\n理由：\n- 修订展示了作者对问题的理解和诚实态度（特别是 Limitations 的扩展和 \"Why RSA over CKA\" 段），这值得肯定。\n- 但 CoRL 的 acceptance bar 要求结论可靠且 actionable。当前状态：(1) 核心对照仍有根本混淆（N1 无新数据）；(2) design implications 仍以 assertive 措辞出现在 Abstract（审稿人第一印象）；(3) 论文的 practical contribution（\"optimize routing, invest in encoder\"）在没有 rollout validation 的情况下仍然是 hypothesis 而非 established finding。\n- 如果 Llama-2 base 实验能在 camera-ready 前完成并支持现有结论，且 Abstract/Conclusion 措辞调整为 hypothesis-generating language，我愿意将评分提升至 6/10（borderline accept）。但在当前状态下，5/10 维持不变。\n\n**具体 actionable items（如果还有修改机会）**：\n1. Abstract line 8：将 \"should\" 改为 \"may benefit from\"；将 \"is the primary design lever\" 改为 \"emerges as a candidate primary design lever in our analysis\"\n2. Section 4.2 标题：从 \"Training Establishes Deliberate Instruction Routing\" 改为 \"Trained VLA Exhibits Deliberate Instruction Routing\"\n3. Table 3：将 same-layer comparison 调整为第一行，best-vs-best 降级\n4. Section 4.1 标题：从 \"instruction-blind\" 改为 \"instruction-invariant at image-token positions\" 或加注 \"(under linear probing)\"",
  "reviewer_id": "1",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 2 修订评估 — Reviewer 1（方法严谨性 + 实验有效性）\n\n---\n\n### 逐条评估\n\n---\n\n**1. R1-N1 [PARTIALLY_RESOLVED]: Untrained baseline confound**\n\n修改内容：\n- Section 4.2 (experiments.tex) 新增关键 caveat：\"Note that this comparison uses a randomly initialized LLM baseline rather than the pretrained Llama-2 checkpoint; the observed routing changes may therefore reflect a combination of language pretraining and VLA fine-tuning (see §5 for discussion).\"\n- Discussion Limitations 段明确承认：\"Our untrained control reinitializes all 6.74B LLM parameters to random weights, conflating language pretraining and VLA fine-tuning effects. A pretrained Llama-2 base checkpoint (without VLA fine-tuning) would isolate the VLA-specific contribution; we are currently conducting this experiment.\"\n\n评估：\n- (+) 问题被显式 acknowledge，且 caveat 放在实验章节正文中（不仅在 Limitations），这让读者在第一次遇到 trained vs. untrained 比较时就能理解局限性。\n- (+) 承诺正在进行 Llama-2 base 实验。\n- (-) 但核心问题仍然存在：**没有新实验数据**。Section 4.2 标题仍为 \"Training Establishes Deliberate Instruction Routing\"，这个 causal claim（\"training establishes\"）仍然超出证据支撑——如果不知道 Llama-2 base 的 attention pattern，不能排除 routing 主要来自语言预训练而非 VLA fine-tuning。\n- (-) Abstract（line 5）仍写 \"VLA training establishes deliberate instruction routing\"，虽然从 \"training learns\" 改为 \"VLA training establishes\"，但措辞仍暗示 VLA-specific 的贡献。\n- 建议：如果无法在 deadline 前完成 Llama-2 base 实验，应将标题改为 \"Trained models exhibit deliberate instruction routing\" 或 \"The trained VLA's routing differs from random baseline\"，避免 causal attribution to \"VLA training\"。\n\n**判定：PARTIALLY_RESOLVED**——acknowledge 充分，但核心 claim 的措辞仍超出证据。\n\n---\n\n**2. R1-N3 [PARTIALLY_RESOLVED]: RSA best-vs-best selection bias**\n\n修改内容：\n- Section 4.3 叙事调整：现在先报告 best-vs-best（\"modest\"，acknowledged n.s.），然后强调 same-layer L12 比较（Δ = +0.079, p < 0.0001），结论为 \"training has a substantial effect on *where* geometry peaks but only a modest effect on *how high*\"。\n- 解读策略分离为两个独立 claim（位置 shift vs. 幅度提升），这更精确。\n\n评估：\n- (+) 正文叙事确实将解读重心转向 same-layer comparison，\"where\" vs. \"how high\" 的区分是有洞察力的 framing。\n- (-) Table 3 (tab:training_effects) 结构未变：best-vs-best 仍为第一行，same-layer 为第二行。表格是审稿人快速浏览的焦点——应将显著的 same-layer 结果放在更突出位置。\n- (-) best-vs-best 的 n.s. 结果仍被保留在 table 中且没有 correction for multiple comparisons 的讨论。\n- (-) 用 LIBERO-Spatial (p < 0.001) 来 argue LIBERO-Goal n.s. \"reflects limited power\" 的逻辑仍在 Appendix 中出现（虽然正文不再强调），这在方法论上仍有问题。\n\n**判定：PARTIALLY_RESOLVED**——叙事改善明显，但 Table 结构和 multiple comparison 问题未完全解决。\n\n---\n\n**3. R1-N4 [PARTIALLY_RESOLVED]: Design implications speculative**\n\n修改内容：\n- Discussion \"Implications\" 段新增 caveat：\"though validating any specific architectural change would require policy rollout experiments\"\n- Conclusion 从 \"These results reveal\" 改为 \"These results suggest\"\n- Limitations 新增 \"Post-hoc analysis\" 段：\"Our analyses characterize frozen representations; they do not address whether architectural interventions based on these observations would preserve the same action quality in closed-loop evaluation.\"\n\n评估：\n- (+) Discussion 中的 caveat 是正确的——承认了 representational analysis → architectural recommendation 的推理跳跃需要 rollout validation。\n- (+) Limitations 的 \"Post-hoc analysis\" 段直接回应了我和 R2 共同指出的核心问题。\n- (-) **但 Abstract 最后一句（line 8）仍为**：\"VLA architectures should optimize routing from image tokens to the readout position; vision encoder quality is the primary design lever.\" 没有任何 hedging。Abstract 是审稿人最先读到的部分，这里的强断言与 Discussion 的 caveats 不一致。\n- (-) Discussion 第一条 implication 仍然是 \"vision encoder pretraining quality is the primary design lever\"——直接断言，未加 \"our results suggest\" 或 \"consistent with the hypothesis that\"。\n- (-) \"Primary design lever\" 这个表述暗示因果优先级排序（投资 encoder > 投资 LLM），但论文的证据是 RSA correlation，不是因果干预。\n\n**判定：PARTIALLY_RESOLVED**——Limitations 和 Discussion 有改善，但 Abstract 和 Discussion implications 的核心措辞仍然过于因果化。\n\n---\n\n**4. R1-W1 [STILL_OPEN]: \"Instruction-blind\" claim 过强**\n\n修改内容：\n- Section 4.1 段落标题仍为 \"Image tokens are instruction-blind.\"\n- 正文将解释性 em-dash 改为括号：\"This strict division of labor (instruction-blind image tokens, instruction-conditioned readout token) indicates...\"\n- 未添加 MLP probe 对 instruction classification 的结果。\n- 未对 \"instruction-blind\" 的定义或 scope 进行限定。\n\n评估：\n- (-) 核心问题未回应：仍仅基于 linear probe 的 chance-level 结果声称 \"instruction-blind\"。\n- (-) 没有新实验（MLP instruction probe 或 higher-capacity probe）来验证 claim 的鲁棒性。\n- (-) 没有对 claim 进行措辞限定（如改为 \"instruction identity is not linearly decodable from image tokens\" 或 \"image tokens lack linearly accessible instruction information\"）。\n- 这不影响接收决定（W-level），但作为 analytical rigor，一个标题级 claim 的证据应当匹配其强度。\n\n**判定：STILL_OPEN**——未做任何回应。\n\n---\n\n**5. R1-W2 [RESOLVED]: CKA/RSA 矛盾**\n\n修改内容：\n- Method Section 3.6 新增 \"Why RSA over CKA\" 段（lines 59-62）：\n  - 给出了选择 RSA 的 principled justification：Spearman rank correlation 的 scale-invariance 和 monotonic-transformation robustness 适合比较 dimensionality 差异大的空间。\n  - 解释了 CKA linear variant 的 known dimension mismatch 问题。\n  - 承认 \"the partial divergence between RSA and CKA orderings confirms that neither metric alone fully characterizes representational structure\"。\n\n评估：\n- (+) 这是一个 well-reasoned methodological justification。不是 post-hoc cherry-picking，而是基于 metric 的数学性质选择。\n- (+) 同时承认了单一 metric 的局限性，CKA 作为 appendix complement 的定位合理。\n- (+) 对审稿人的 concern 做了实质性回应：不是\"两个 metric 都对\"的回避，而是\"为什么 RSA 更适合这个具体比较\"。\n\n**判定：RESOLVED**\n\n---\n\n### 总体评估\n\n**修订力度**：中等。作者在 Limitations 和 caveats 方面做了实质性改进（尤其是 N1 的 confound acknowledge、N4 的 post-hoc caveat、W2 的 metric justification）。但三个核心问题的**实质性解决**（新实验数据、statistical correction、claim 强度与证据匹配）均未完成。\n\n**关键残留问题**：\n1. Abstract 和 Conclusion 的措辞仍然过于 assertive——Limitations 中的 caveats 不能弥补 headline claims 的过度。\n2. 无 Llama-2 base 实验数据（仅 promise \"currently conducting\"）。\n3. \"Instruction-blind\" claim 完全未修改。\n\n---\n\n### 更新后评分\n\n**Overall: 5.5/10 → 维持 5/10（marginally below acceptance threshold）**\n\n理由：\n- 修订展示了作者对问题的理解和诚实态度（特别是 Limitations 的扩展和 \"Why RSA over CKA\" 段），这值得肯定。\n- 但 CoRL 的 acceptance bar 要求结论可靠且 actionable。当前状态：(1) 核心对照仍有根本混淆（N1 无新数据）；(2) design implications 仍以 assertive 措辞出现在 Abstract（审稿人第一印象）；(3) 论文的 practical contribution（\"optimize routing, invest in encoder\"）在没有 rollout validation 的情况下仍然是 hypothesis 而非 established finding。\n- 如果 Llama-2 base 实验能在 camera-ready 前完成并支持现有结论，且 Abstract/Conclusion 措辞调整为 hypothesis-generating language，我愿意将评分提升至 6/10（borderline accept）。但在当前状态下，5/10 维持不变。\n\n**具体 actionable items（如果还有修改机会）**：\n1. Abstract line 8：将 \"should\" 改为 \"may benefit from\"；将 \"is the primary design lever\" 改为 \"emerges as a candidate primary design lever in our analysis\"\n2. Section 4.2 标题：从 \"Training Establishes Deliberate Instruction Routing\" 改为 \"Trained VLA Exhibits Deliberate Instruction Routing\"\n3. Table 3：将 same-layer comparison 调整为第一行，best-vs-best 降级\n4. Section 4.1 标题：从 \"instruction-blind\" 改为 \"instruction-invariant at image-token positions\" 或加注 \"(under linear probing)\"",
    "reviewer_id": "1",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 59 · 2026-05-17T06:05:39.408264+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 6686
}
```

</details>

---


### Assistant

_source line 60 · 2026-05-17T06:05:47.824440+00:00_

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
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1"
}
```

</details>

---


## Round 4

## Round 4

3 recorded events


### User

_source line 61 · 2026-05-17T06:08:21.305006+00:00_

[Round 2 审稿请求]:
## Round 2 Step 2 交叉确认（简化版）

R2 评分 5/10，R3 评分 7/10。请简要回应：

**R2 关键判定**：
- R2-N1: Neo et al. (ICLR 2025) 仍未引用，Introduction "No prior work has provided a systematic token-level decomposition" 构成换皮 "first" claim
- R2-N2: 无方法创新问题维持 STILL_OPEN
- R2 认为 Abstract 与 Limitations 语气不一致是核心残留问题

**R3 关键判定**（7/10, conditional accept）：
- Em-dash 完全清除 ✓
- Related Work 达标 ✓
- 剩余问题均为一行修改（Limitations \subsection、LOOCV 展开、Table 1 caption、reproducibility statement）
- R3 认为如果这 4 个 minor fix 完成，论文在写作/格式维度达到 accept 标准

**问题**：
1. R2 指出的 Neo et al. 缺失是否影响你对论文 internal validity 的评估？（即：如果 novelty positioning 进一步被削弱，你的 5/10 是否会下调？）
2. R3 的 conditional accept (7/10) 是否改变你对论文整体 acceptability 的判断？

请用 2-3 句话回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 62 · 2026-05-17T06:08:38.576266+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 2 Step 2 交叉确认 — Reviewer 1\n\n**Q1: Neo et al. 缺失是否影响 internal validity 评估？**\n\n不影响我的评分。Neo et al. 分析 VLM (LLaVA) 而非 VLA，方法也不同（他们未做 trained/untrained factorial control）。Introduction 的 \"No prior work has provided a systematic token-level decomposition of a VLA\" 如果严格限定在 VLA + systematic multi-metric，仍可站住脚。这是 novelty positioning/framing 问题，不是 internal validity 问题。我的 5/10 基于实验设计缺陷（N1 baseline confound、N4 无因果验证），不基于 novelty claim 的措辞——即使 novelty 进一步削弱，评分不会下调（已在 borderline 区间）。但同意 R2 的建议：应引用 Neo et al. 并明确区分。\n\n**Q2: R3 的 7/10 是否改变我的判断？**\n\n不改变。R3 的 7/10 基于写作/格式/presentation 维度的评估，这些问题确实 trivially fixable。但我的 5/10 基于方法论问题（baseline confound、causal gap），这些不是格式修复能解决的。三位 reviewer 的分歧反映了审查侧重不同：R3 看 presentation readiness，我看 scientific rigor。两个维度都重要，但在 CoRL 的 acceptance decision 中，如果 contribution 的可靠性存疑（trained vs. random 的混淆无法通过 Limitations ���落解决），presentation 达标不足以 compensate。维持 5/10。",
  "reviewer_id": "1",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 2 Step 2 交叉确认 — Reviewer 1\n\n**Q1: Neo et al. 缺失是否影响 internal validity 评估？**\n\n不影响我的评分。Neo et al. 分析 VLM (LLaVA) 而非 VLA，方法也不同（他们未做 trained/untrained factorial control）。Introduction 的 \"No prior work has provided a systematic token-level decomposition of a VLA\" 如果严格限定在 VLA + systematic multi-metric，仍可站住脚。这是 novelty positioning/framing 问题，不是 internal validity 问题。我的 5/10 基于实验设计缺陷（N1 baseline confound、N4 无因果验证），不基于 novelty claim 的措辞——即使 novelty 进一步削弱，评分不会下调（已在 borderline 区间）。但同意 R2 的建议：应引用 Neo et al. 并明确区分。\n\n**Q2: R3 的 7/10 是否改变我的判断？**\n\n不改变。R3 的 7/10 基于写作/格式/presentation 维度的评估，这些问题确实 trivially fixable。但我的 5/10 基于方法论问题（baseline confound、causal gap），这些不是格式修复能解决的。三位 reviewer 的分歧反映了审查侧重不同：R3 看 presentation readiness，我看 scientific rigor。两个维度都重要，但在 CoRL 的 acceptance decision 中，如果 contribution 的可靠性存疑（trained vs. random 的混淆无法通过 Limitations ���落解决），presentation 达标不足以 compensate。维持 5/10。",
    "reviewer_id": "1",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-17T06:08:43.588553+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5012
}
```

</details>

---


## Round 5

## Round 5

52 recorded events


### User

_source line 64 · 2026-05-17T18:01:35.502779+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责审查**方法与实验严谨性**。

## 论文信息
- **标题**: Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model
- **文件路径**: `projects/vla-ssd/docs/paper/main.tex`（多文件结构：abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, appendix.tex, references.bib）
- **目标 Venue**: CoRL 2026（10th Conference on Robot Learning）
- **截止日期**: Paper 2026-05-28 EOD
- **格式**: 8 页正文 + references + appendix，双盲审稿，corl_2026 模板
- **匿名规则**: 双盲（double-blind）
- **Limitations**: 必须包含，计入 8 页

## 你的审查侧重

**方法与实验严谨性**，具体关注：

1. **Probing 方法论**：
   - Cross-instruction probe (10-way classification) 的设计是否合理？10 个 task 做 10-way classification 是否有 confound？
   - MLP probe 的 capacity 控制是否充分？2 层 256 hidden 是否 overly expressive 或 underpowered？
   - LOOCV 的实施是否正确？leave-one-out 在这个 setting 下的含义是什么？

2. **RSA 正确性**：
   - Cosine distance for representations + Euclidean for actions 的混合距离函数是否有理论依据？
   - Within-task RSA 设计（50 demos per task）的统计 power 是否足够？
   - "Inverted-U" claim 的统计支撑（bootstrap CI 是否 exclude zero at peak vs. endpoints）

3. **统计检验**：
   - Bootstrap 10,000 resamples 的置信区间报告是否一致？
   - p 值的多重比较校正（family-wise error）是否需要？
   - "n.s." 结果（RSA best-vs-best Δ=+0.017, CI includes 0）的解释是否恰当

4. **Ablation 设计**：
   - L1 attention ablation（zeroing instruction attention）的设计合理性
   - 5 demos vs 50 demos 的 probe 是否 comparable？论文说 "absolute values are not directly comparable" 但仍做 within-condition comparison，是否 valid？
   - 三条件（trained/pretrained/untrained）是否充分隔离各因素？

5. **实验控制**：
   - Vision encoder 在三个条件下都是 frozen 的——这是 feature 还是 confound？
   - 只用 OpenVLA-7B + LIBERO 的 generalizability 限制
   - Cross-benchmark validation (LIBERO-Spatial) 是否构成足够的外部效度

6. **数据一致性**：
   - 正文 Table vs Appendix Table 的数值是否一致
   - L1 heads 数量在不同位置报告是否一致（25 vs 24 vs ±1 解释）

请按标准审稿格式输出：Summary → Strengths → Weaknesses → Questions → Minor Issues。
Weakness 分为 Must-Fix / Should-Fix / Nice-to-Have 三级。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 65 · 2026-05-17T18:01:46.197116+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find paper tex files",
  "prompt": "Find all .tex and .bib files under projects/vla-ssd/docs/paper/. List their full paths. Search breadth: medium."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Find paper tex files",
    "prompt": "Find all .tex and .bib files under projects/vla-ssd/docs/paper/. List their full paths. Search breadth: medium."
  }
}
```

</details>

---


### Tool call

_source line 66 · 2026-05-17T18:01:46.749958+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-17T18:01:46.800553+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 68 · 2026-05-17T18:01:47.754890+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/vla-ssd/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/vla-ssd/docs/paper/**/*.tex"
  }
}
```

</details>

---


### Tool call

_source line 69 · 2026-05-17T18:01:47.755448+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/vla-ssd/docs/paper/**/*.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/vla-ssd/docs/paper/**/*.bib"
  }
}
```

</details>

---


### Tool result

_source line 70 · 2026-05-17T18:01:47.755945+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 1
}
```

</details>

---


### Tool result

_source line 71 · 2026-05-17T18:01:47.756253+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 72 · 2026-05-17T18:01:49.665691+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs -type f \\( -name \"*.tex\" -o -name \"*.bib\" \\) 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs -type f \\( -name \"*.tex\" -o -name \"*.bib\" \\) 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 73 · 2026-05-17T18:01:49.866797+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_example.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper-a-plus-backup/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper-a-plus-backup/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper-a-plus-backup/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper-a-plus-backup/corl_example.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper-a-plus-backup/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper-a-plus-backup/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper-a-plus-backup/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper-a-plus-backup/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper-a-plus-backup/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/p
…[truncated 57 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 74 · 2026-05-17T18:01:49.968174+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/ 2>/dev/null || echo \"Directory not found\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/ 2>/dev/null || echo \"Directory not found\""
  }
}
```

</details>

---


### Tool result

_source line 75 · 2026-05-17T18:01:50.069379+00:00_

total 56
drwxr-xr-x 5 ubuntu ubuntu  4096 May 17 04:20 .
drwxr-xr-x 9 ubuntu ubuntu  4096 May 17 17:44 ..
-rw-r--r-- 1 ubuntu ubuntu 36462 May 15 22:27 IDEA_BRIEF.md
drwxr-xr-x 3 ubuntu ubuntu  4096 May 17 17:08 paper
drwxr-xr-x 2 ubuntu ubuntu  4096 May 17 04:20 paper-a-plus-backup
drwxr-xr-x 3 ubuntu ubuntu  4096 May 15 05:23 results

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 76 · 2026-05-17T18:01:53.283736+00:00_

Perfect! I found all the .tex and .bib files. Here are the results for files specifically under projects/vla-ssd/docs/paper/:

**Full paths of .tex and .bib files in projects/vla-ssd/docs/paper/:**

.bib files:
- /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib

.tex files:
- /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_example.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex

**Summary:** Found 1 .bib file and 10 .tex files, for a total of 11 files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Agent",
  "elapsed_ms": 7086
}
```

</details>

---


### Tool call

_source line 77 · 2026-05-17T18:01:58.207545+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 78 · 2026-05-17T18:01:58.608915+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 79 · 2026-05-17T18:01:58.609400+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 80 · 2026-05-17T18:01:59.062751+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 81 · 2026-05-17T18:01:59.114111+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 82 · 2026-05-17T18:01:59.114685+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 83 · 2026-05-17T18:01:59.566586+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 84 · 2026-05-17T18:01:59.868325+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 85 · 2026-05-17T18:01:59.919039+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool result

_source line 86 · 2026-05-17T18:02:05.540587+00:00_

Web search results for query: "CoRL 2026 reviewer guidelines review form criteria"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CVPR 2026 Reviewer Guidelines","url":"https://cvpr.thecvf.com/Conferences/2026/ReviewerGuidelinesq"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"}]

Based on the search results, I found some information about CoRL 2026, though specific detailed reviewer guidelines and review form criteria were not fully available in the search results. Here's what I found:

## CoRL 2026 Reviewer Information

All submissions must include at least one author who agrees to serve as a CoRL reviewer, and they are qualified if they have at least one accepted publication at a previous robotics (CoRL/ICRA/IROS/RSS) or learning conference (ICLR/NeurIPS/ICML) or equivalent journal.

The aim is to have at least two reviewers per paper.

## Related Review Criteria (from CoRL 2024)

While I couldn't locate the specific 2026 reviewer form criteria in these results, the search did return information from CoRL 2024 that may be informative. Submissions are evaluated based on the significance and novelty of the results, either theoretical or empirical.

For more detailed and specific inform
…[truncated 373 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 5621
}
```

</details>

---


### Tool call

_source line 87 · 2026-05-17T18:02:12.026094+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 88 · 2026-05-17T18:02:12.327787+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 89 · 2026-05-17T18:02:12.378432+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 90 · 2026-05-17T18:02:12.782358+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 91 · 2026-05-17T18:02:13.986779+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2024.corl.org/contributions/instruction-for-reviews",
  "prompt": "Extract the complete reviewer guidelines, review form dimensions/criteria, scoring scales, and what reviewers should evaluate. I need the full list of review dimensions and their descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2024.corl.org/contributions/instruction-for-reviews",
    "prompt": "Extract the complete reviewer guidelines, review form dimensions/criteria, scoring scales, and what reviewers should evaluate. I need the full list of review dimensions and their descriptions."
  }
}
```

</details>

---


### Tool result

_source line 92 · 2026-05-17T18:02:18.253668+00:00_

# CoRL 2024 Review Guidelines Summary

Based on the provided content, here's what's available:

## Review Criteria for Regular Papers

Reviewers should evaluate submissions on:

- **Significance and novelty** of theoretical or empirical results
- **Objective establishment** of findings and their potential scientific/technological impact
- **Relevance to robotic learning**

The document emphasizes a "broad view of robot learning," welcoming papers combining experimental and theoretical contributions.

## Notable Limitation

The provided webpage excerpt does **not include**:
- A complete review form with scoring scales
- Specific evaluation dimensions (e.g., clarity, originality, significance ratings)
- Numerical scoring rubrics
- Detailed assessment criteria beyond the three areas mentioned above

## Scope Requirements

The document specifies papers must demonstrate relevance through either:
- "Explicitly address a learning question for physical robots" (intent), or
- "Test the proposed learning solution on physical robots" (outcome)

## Reviewer Qualifications

Reviewers should have "expertise in robotics, robot learning, machine learning" with ideally "a minimum of 3 first author publications in major robotics conferences and journals" and relevant ML venues.

**The full review form dimensions and detailed scoring scales are not present in this excerpt.**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 4266
}
```

</details>

---


### Tool call

_source line 93 · 2026-05-17T18:02:24.981047+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 94 · 2026-05-17T18:02:25.433114+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 95 · 2026-05-17T18:02:25.433712+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 96 · 2026-05-17T18:02:25.986405+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We decompose a VLA's internal representations with factorial trained-vs-untrained control, revealing: (1)~strict token-level specialization (instruction-blind image tokens, cross-validated readout hub); (2)~front-loaded instruction routing, shifted from mid-depth (L9--L16) to entry-exit (L0--L1, L31); and (3)~non-monotonic vision encoder refinement (peak L12, readout $R^2$ $+0.069$, image $\Delta \leq 1.7\%$).
5	Vision encoder quality emerges as a key design lever.
6	Code and representations will be released upon acceptance.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 97 · 2026-05-17T18:02:25.986749+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2025 2024 OpenReview review form scoring scale soundness clarity novelty significance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2025 2024 OpenReview review form scoring scale soundness clarity novelty significance"
  }
}
```

</details>

---


### Tool result

_source line 98 · 2026-05-17T18:02:41.706863+00:00_

Web search results for query: "CoRL 2025 2024 OpenReview review form scoring scale soundness clarity novelty significance"

Links: [{"title":"CORL 2025 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/corl-statistics/corl-2025-statistics/"},{"title":"CoRL | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL"},{"title":"Venues | OpenReview","url":"https://openreview.net/"},{"title":"CoRL 2025 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/corl-paper-list/corl-2025-paper-list/"},{"title":"GitHub - ANLGBOY/ICLR-2024-OpenReview-Ratings · GitHub","url":"https://github.com/ANLGBOY/ICLR-2024-OpenReview-Ratings"},{"title":"CoRL 2025 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2025%2FConference"},{"title":"CORL 2024 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/corl-statistics/corl-2024-statistics/"},{"title":"CoRL 2025 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2025"},{"title":"CoRL 2024 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2024"},{"title":"CoRL 2024 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FConference"}]

The search results found the OpenReview pages for CoRL 2024 and 2025, but they don't show the actual review form details. Let me search more specifically for the review form information.

Links: [{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"CoRL 2024 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2024"},{"title":"ICML 2024 Reviewer Instructions","url":"https://icml.cc/Conferences/2024/ReviewerInstructions"},{"title":"CoRL 2024 Conference | OpenReview","url":"https://openreview.net/group?i
…[truncated 5603 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 15720
}
```

</details>

---


### Tool call

_source line 99 · 2026-05-17T18:02:47.546500+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl2023.org/reviewer-guidelines",
  "prompt": "Extract the complete reviewer guidelines including: all evaluation dimensions, scoring scales/ratings (numeric), what each score means, review form structure, and any specific instructions about what makes a paper acceptable vs rejectable. I need the exact scoring system."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl2023.org/reviewer-guidelines",
    "prompt": "Extract the complete reviewer guidelines including: all evaluation dimensions, scoring scales/ratings (numeric), what each score means, review form structure, and any specific instructions about what makes a paper acceptable vs rejectable. I need the exact scoring system."
  }
}
```

</details>

---


### Tool call

_source line 100 · 2026-05-17T18:02:47.898304+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-17T18:02:47.949030+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 102 · 2026-05-17T18:02:53.019965+00:00_

# CoRL 2023 Reviewer Guidelines Summary

## Evaluation Dimensions

The guidelines specify six key assessment areas:

1. **Originality**: "Are the problems or methods new?" Novel combinations of techniques are valued; clarity on differentiation from prior work is essential.

2. **Quality**: Technical soundness, empirical/theoretical support, methodological appropriateness, and honest evaluation of strengths and weaknesses.

3. **Clarity**: Writing quality, organization, and whether "an expert reader" could reproduce results from the information provided.

4. **Significance**: Importance of results and potential impact on researchers or practitioners.

5. **Relevance**: Robot learning focus, learning-based methods, simulation or real robot evaluation.

6. **Limitations**: Papers must include a limitations section; honestly reported limitations should be "treated kindly."

## Scoring System

**The document does not specify numeric scoring scales or rating definitions.** No point values, letter grades, or scoring rubric is provided in this content.

## Scoring Criteria Implications

The guidelines emphasize that papers need not meet strict requirements for:
- Publishing datasets/code
- Including theorems
- Real robot demonstrations
- State-of-the-art performance

However, they should provide "novel perspectives, insights, and sufficient knowledge advancement."

## Key Instruction

Reviewers must be constructive, provide evidence for criticisms, and avoid common mistakes like unsupported claims or ranking papers purely on SOTA performance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5473
}
```

</details>

---


### Tool call

_source line 103 · 2026-05-17T18:02:58.795085+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2025 OpenReview review form \"overall score\" \"1\" \"2\" \"3\" rating scale accept reject"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2025 OpenReview review form \"overall score\" \"1\" \"2\" \"3\" rating scale accept reject"
  }
}
```

</details>

---


### Tool result

_source line 104 · 2026-05-17T18:03:10.398895+00:00_

Web search results for query: "CoRL 2025 OpenReview review form "overall score" "1" "2" "3" rating scale accept reject"

Links: [{"title":"CORL 2025 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/corl-statistics/corl-2025-statistics/"},{"title":"CoRL 2025 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2025"},{"title":"Default Review Form | OpenReview","url":"https://docs.openreview.net/reference/default-forms/default-review-form"},{"title":"CoRL 2025 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2025%2FConference"},{"title":"CoRL 2025 Workshop Robot Data | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2025%2FWorkshop%2FRobot_Data"},{"title":"CoRL 2025 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/corl-paper-list/corl-2025-paper-list/"},{"title":"CoRL | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL"},{"title":"Why are the \"rating\" and \"confidence\" fields in my PC Console wrong? | OpenReview","url":"https://docs.openreview.net/getting-started/frequently-asked-questions/why-are-the-rating-and-confidence-fields-in-my-pc-console-wrong"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"ICLR 2025 Reviewer Guide","url":"https://iclr.cc/Conferences/2025/ReviewerGuide"}]

The search results don't provide specific details about the CoRL 2025 review form's overall score rating scale. Let me search more specifically for the review form details.

Links: [{"title":"Default Review Form | OpenReview","url":"https://docs.openreview.net/reference/default-forms/default-review-form"},{"title":"ICLR 2025 Reviewer Guide","url":"https://iclr.cc/Conferences/2025/ReviewerGuide"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"Accept More, Reject Less: Reducing 
…[truncated 3925 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 11603
}
```

</details>

---


### Tool call

_source line 105 · 2026-05-17T18:03:16.573613+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://papercopilot.com/statistics/corl-statistics/corl-2025-statistics/",
  "prompt": "Extract the review scoring scale used at CoRL 2025. What are the rating options? What is the scale (1-5? 1-10?)? What are the thresholds for acceptance? Any information about review dimensions (soundness, clarity, significance, etc.)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://papercopilot.com/statistics/corl-statistics/corl-2025-statistics/",
    "prompt": "Extract the review scoring scale used at CoRL 2025. What are the rating options? What is the scale (1-5? 1-10?)? What are the thresholds for acceptance? Any information about review dimensions (soundness, clarity, significance, etc.)."
  }
}
```

</details>

---


### Tool call

_source line 106 · 2026-05-17T18:03:18.330247+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://docs.openreview.net/reference/default-forms/default-review-form",
  "prompt": "Extract the complete default review form used by OpenReview. Include: the overall rating scale with all numeric values and their labels, confidence scale, all review dimensions (soundness, presentation, contribution, etc.), and any additional fields. I need the complete form structure."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://docs.openreview.net/reference/default-forms/default-review-form",
    "prompt": "Extract the complete default review form used by OpenReview. Include: the overall rating scale with all numeric values and their labels, confidence scale, all review dimensions (soundness, presentation, contribution, etc.), and any additional fields. I need the complete form structure."
  }
}
```

</details>

---


### Tool result

_source line 107 · 2026-05-17T18:03:20.388278+00:00_

Based on the webpage content provided, I cannot find specific information about CoRL 2025's review scoring scale, rating options, or acceptance thresholds.

The page displays aggregate statistics showing that CoRL 2025 had 263 total submissions with 221 accepted (84.03%) and 42 oral presentations (15.97%), but it does not reveal the underlying review metrics or scoring dimensions used.

Notably, the comparison with CoRL 2024 shows reviews were scored on "1.70 to 4.00" scale, while CoRL 2023 used "4.70 to 10.00" scale, suggesting the scales vary by year. However, the specific 2025 scoring details are not documented in this excerpt.

To find this information, you would need to consult the actual CoRL 2025 call for papers or review guidelines, likely available through the OpenReview platform link referenced on the page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 3814
}
```

</details>

---


### Tool result

_source line 108 · 2026-05-17T18:03:27.013689+00:00_

# OpenReview Default Review Form Structure

Based on the documentation provided, the default review form contains **four main fields**:

## 1. Title
- **Type:** Text string (0-500 characters)
- **Purpose:** Brief summary of review
- **Order:** 1

## 2. Review
- **Type:** Textarea with Markdown and LaTeX support
- **Length:** 1-20,000 characters (description mentions max 200,000)
- **Purpose:** "Please provide an evaluation of the quality, clarity, originality and significance of this work, including a list of its pros and cons"
- **Order:** 2

## 3. Rating
- **Type:** Dropdown selection (integer 1-10)
- **Scale includes:**
  - 10: "Top 5% of accepted papers, seminal paper"
  - 9: "Top 15% of accepted papers, strong accept"
  - 8: "Top 50% of accepted papers, clear accept"
  - 7-6: Accept/marginally above threshold
  - 5-4: Below threshold/rejection
  - 3-1: Clear rejection through trivial/wrong
- **Order:** 3

## 4. Confidence
- **Type:** Radio selection (integer 1-5)
- **Scale:** Ranges from "absolutely certain" (5) to "educated guess" (1)
- **Order:** 4

**Note:** The form does not appear to include separate dimension scores (soundness, presentation, contribution). Instead, reviewers provide holistic evaluation within the review field.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8683
}
```

</details>

---


### Tool call

_source line 109 · 2026-05-17T18:05:21.218358+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://papercopilot.com/statistics/corl-statistics/corl-2024-statistics/",
  "prompt": "What is the rating scale used for CoRL 2024 reviews? What are the specific rating labels (e.g., \"strong accept\", \"accept\", \"borderline\", etc.) and their numeric values? What was the acceptance threshold?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://papercopilot.com/statistics/corl-statistics/corl-2024-statistics/",
    "prompt": "What is the rating scale used for CoRL 2024 reviews? What are the specific rating labels (e.g., \"strong accept\", \"accept\", \"borderline\", etc.) and their numeric values? What was the acceptance threshold?"
  }
}
```

</details>

---


### Tool result

_source line 110 · 2026-05-17T18:05:24.485144+00:00_

Based on the provided content, I cannot definitively answer your question about the specific rating scale labels and their numeric values for CoRL 2024.

The page shows that CoRL 2024 had "min:1.70 max:4.00 avg:3.01" for ratings, indicating a numeric scale ranging from approximately 1.70 to 4.00. However, the document does not explicitly list the rating labels (such as "strong accept" or "borderline") or their corresponding numeric values.

The content also does not specify an acceptance threshold. We only know that 264 out of 671 submissions were accepted, yielding a 39.34% acceptance rate.

To obtain the specific rating scale labels and acceptance decision criteria for CoRL 2024, you would need to consult the official OpenReview submission guidelines or conference documentation directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 3266
}
```

</details>

---


### Tool call

_source line 111 · 2026-05-17T18:05:35.232091+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
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

_source line 112 · 2026-05-17T18:05:35.282692+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 113 · 2026-05-17T18:07:36.503234+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1: 方法与实验严谨性审查\n\n## 论文信息\n- **标题**: Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\n- **Venue**: CoRL 2026\n\n---\n\n## 总体评分\n\n**Overall**: 3/5 (Borderline)\n\n**一句话总结**: 实验设计思路清晰、factorial control 有价值，但核心 probing 任务过于简单导致 claim 强度与证据不匹配，RSA inverted-U 的效应量极小，ablation 使用不同数据规模削弱因果推断力度。\n\n---\n\n## 官方维度打分（基于 CoRL reviewer guidelines: Originality, Quality, Clarity, Significance, Relevance）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 4/5 | Token-level factorial decomposition of VLA 是新颖的分析框架，prior work 没有做过 trained-vs-untrained 的系统对比 |\n| Quality (Technical Soundness) | 2.5/5 | 核心 probe 任务 trivially easy，RSA 效应量极小且 metric-dependent，ablation 数据规模不一致，缺乏多重比较校正 |\n| Clarity | 4/5 | 写作清晰、结构完整，数据呈现系统化 |\n| Significance | 3/5 | 对 VLA 内部机制提供了描述性洞察，但因证据力度不足，architectural implications 缺乏可操作性 |\n| Relevance | 4/5 | VLA 内部机制分析直接服务于 robot learning 社区的模型设计需求 |\n\n---\n\n## Summary\n\n本文对 OpenVLA-7B 在 LIBERO 上进行 token 级别表征分析，通过 cross-instruction probes、attention 分析、RSA 和 MLP probes 四种方法，比较 trained/pretrained/untrained 三个条件。主要发现：(1) image tokens 不编码 instruction 信息，readout token 是唯一的多模态汇聚点；(2) VLA fine-tuning 将 instruction routing 从中层转移到 entry-exit 模式；(3) LLM 对 vision encoder 输出进行非单调变换（inverted-U）。实验设计的 factorial structure 值得肯定，但多个核心 claim 的证据强度存在问题。\n\n---\n\n## Strengths\n\n**S1. 系统化的实验设计框架**\n三条件（trained/pretrained/untrained）× 两因素（instruction presence）的 factorial design 是分析 VLA 的好范式。这比 prior work（如 Grant et al., Häon et al.）的单条件分析更有控制力。Appendix 的 robustness checks（distance metric invariance, per-DOF decomposition, permutation test, seed sensitivity, demo subsampling）体现了实验严谨态度。\n\n**S2. 多指标互相验证**\nRSA + MLP probe + attention analysis + cross-instruction probe 四种方法从不同角度切入同一问题，且 CKA 作为 supplementary metric 在 appendix 中报告，体现了方法论意识。\n\n**S3. 诚实报告 negative/null results**\nRSA best-vs-best Δ=+0.017 (CI includes 0) 被如实标记为 n.s.；CKA 与 RSA 的 ordering 矛盾被正面讨论而非隐藏。这是好的学术实践。\n\n**S4. Cross-benchmark validation**\nLIBERO-Spatial 上的复现增加了核心发现的可信度（尽管仍在同一 simulator 内）。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Cross-instruction probe 任务 trivially easy，不支撑 \"multimodal convergence\" 的强 claim\n\n- 具体位置：Section 4.2 (Token-Level Functional Specialization), Table 1\n- 问题：10-way classification over 10 distinct instruction strings 对任何能 attend to instruction tokens 的位置都是 trivial 的。论文自己在 Appendix D.1 承认 \"even incidental attention (~12%) suffices for linear classification at L1\"。事实上，untrained model（随机权重）在 L1 也达到 100%（Table 1）。这意味着 100% 分类准确率不能作为 \"multimodal convergence\" 或 \"functional specialization\" 的强证据——它只反映 instruction embeddings 本身是线性可分的（这是 tokenizer 的 trivial 性质）。\n- 为什么影响接收：Finding 1（\"strict token-level functional specialization\"）是论文三大贡献之首，也是标题的核心 claim。如果 readout token 的 100% 准确率是 trivial baseline（随机权重也能达到），那么这个发现的 novelty 大幅缩水。真正有价值的发现是 image token 保持 chance level，但论文的对称叙事（\"image blind + readout as hub\"）过度依赖 readout 侧的结果。\n- 建议修改方向：(a) 增加更困难的 probe 任务（如区分语义相近的指令、或 fine-grained instruction attribute prediction）；(b) 调整 framing——将重点放在 image token 的 instruction-blindness（这是 non-trivial 的 negative result）而非 readout 的 100%（这是 trivial 的 positive result）；(c) 对 untrained 也达到 100%@L1 做更深入讨论——如果随机权重即可实现，trained model 维持 100% 的 significance 需要重新定义。\n\n**N2** [critical] RSA \"inverted-U\" 的 rise phase 效应量极小（Δρ = 0.016），且 metric-dependent\n\n- 具体位置：Section 4.3, Figure 3, Table 3; Appendix B.2\n- 问题：Trained image_mean RSA 从 L0 (0.612) 到 L12 (0.628) 的升幅仅为 0.016（2.6%）。Best-vs-best training effect (+0.017) 的 CI 包含 0。更严重的是，Appendix B.2 显示 linear CKA 完全逆转了 RSA ordering（untrained > trained > DINOv2），且 linear CKA per-layer profile 呈单调上升，完全没有 inverted-U。这意味着 \"non-monotonic refinement\" 是 metric-specific 的描述，而非 representation 的 intrinsic property。\n- 为什么影响接收：Finding 3（\"non-monotonic refinement of vision encoder output\"）是论文贡献之一。如果这个 pattern 仅在 RSA（Spearman rank correlation on cosine-distance RDMs）下成立，在另一个标准 metric（CKA）下消失甚至逆转，那么 generalizability 成问题。论文的 architectural implication（\"vision encoder quality matters more than LLM scale\"）建立在 DINOv2 RSA 最高这个 RSA-specific 结果上。\n- 建议修改方向：(a) 明确 qualify claims 的 metric-dependence（\"under RSA, we observe...\"）；(b) 讨论为什么 RSA 比 CKA 更 appropriate for this question（目前 Method §3.5 的 justification 不够充分——\"CKA is sensitive to kernel choice\" 同样可以反过来说 RSA 对 distance function 选择敏感）；(c) 考虑 inverted-U 的 rise phase 是否在统计上 significant——L0→L12 的 +0.016 需要 CI。\n\n**N3** [critical] L1 attention ablation 使用 5 demos（vs 主实验 50 demos），因果推断的可靠性存疑\n\n- 具体位置：Section 4.2, paragraph \"Ablation reveals functional specialization\"（第76行）\n- 问题：Ablation 实验仅使用 5 demos per task（50 个 total datapoints），而主实验 Table 3 使用 50 demos per task。论文承认 \"absolute values are not directly comparable\" 但仍得出强因果结论（\"instruction-dominant heads redirect attention from image to instruction tokens at the cost of local action encoding\"）。用 50 个数据点训练一个 2-layer MLP probe（>1M 参数），然后报告 R² 从 0.256 到 0.375 的提升——这个 R² 的 baseline 本身就非常低（0.256），暗示 probe 在 5 demos 下严重 underfitting，ablation \"improvement\" 可能是 reduced effective input dimensionality 带来的 regularization effect 而非 genuine functional specialization。\n- 为什么影响接收：这是论文中唯一的 causal intervention（其余都是 observational）。如果 ablation 不可靠，论文就只有 correlational evidence。\n- 建议修改方向：(a) 用 50 demos 重跑 ablation，使 baseline R² 与 Table 3 直接 comparable；(b) 如果 50 demos 不可行，至少报告 N（总 observation-action pairs 数）并讨论 probe capacity vs sample size 的比率；(c) 添加 random ablation control（随机 zero 同等数量的 non-instruction-dominant heads）以排除 \"任何 attention zeroing 都能提升 R²\" 的 confound。\n\n---\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 缺乏多重比较校正（family-wise error）\n\n- 具体位置：贯穿全文所有统计检验\n- 问题：论文对 32 层 × 3 条件 × 多个 metric 进行了大量逐层比较，但没有任何 Bonferroni、Holm、或 FDR 校正。虽然单个 bootstrap CI 是 valid 的，但在数十个比较中找到 p < 0.05 的概率很高。\n- 建议：至少对 key claims（inverted-U peak significance、training effects per layer）应用 FDR correction 并报告 adjusted p-values。\n\n**W2** [warning] Probe 的 total N 未报告，capacity 控制不充分\n\n- 具体位置：Section 3.5 (Functional Action Probes), Section 4.1 (Experimental Setup)\n- 问题：50 demos per task × 10 tasks = 500 demonstrations，但每个 demo 有多少 timesteps？Total N（observation-action pairs for probe training）从未明确报告。2-layer MLP (4096→256→7) 有 ~1.05M 参数。如果 N < 10,000，probe 可能 overfit；如果 N > 100,000，probe 可能 underfit。Early stopping (patience 5) 是部分 mitigation 但不充分。\n- 建议：报告 exact N；添加 linear probe 作为 capacity lower-bound（Method 中提到 linear probe 也在 image_mean 上得 10%，但未对 R² 做 linear vs MLP 对比）。\n\n**W3** [warning] \"Untrained\" condition 的 L1 = 100% 结果削弱 Finding 1 的 interpretation\n\n- 具体位置：Table 1, Appendix D.1\n- 问题：随机初始化的 LLM 在 L1 也能实现 100% instruction classification。论文将此解释为 \"incidental\"（附录说 ~12% attention 即可），但这暴露了 probe 任务的 trivial nature。更重要的是，untrained model 的 100%→82% 衰减 pattern 很有趣但讨论不足——为什么随机权重会导致信息逐层丢失？这可能揭示 residual stream 中 signal-to-noise ratio 的衰减，值得展开。\n- 建议：增加讨论 untrained 的 decay mechanism；考虑 probe 任务难度是否足以区分 \"genuine multimodal integration\" 和 \"trivial linear separability\"。\n\n**W4** [warning] Frozen vision encoder 是 feature 但也是 confound\n\n- 具体位置：Section 3.1 (Model and Data)\n- 问题：三个条件共享 frozen vision encoder 和 projector，这使得 image_mean 在 L0 的起始 representation 完全相同。论文因此无法评估 VLA training 对 vision processing 的 full effect（只能评估 LLM 如何处理固定的 vision output）。然而论文在 Discussion 中得出 \"vision encoder quality may matter more than LLM scale\" 这一 architectural implication——这个结论需要 across-encoder 实验（如换 CLIP-only encoder），而非单一 frozen encoder 内的分析。\n- 建议：qualify 这个 architectural implication 为 \"under fixed encoder\" 条件下的观察；或增加对比实验（不同 vision encoder 的 RSA comparison）。\n\n**W5** [warning] 25 vs 24 heads 不一致需要更清晰解释\n\n- 具体位置：Table 2 报告 L1 VLA-trained = 25/32；Appendix Table 10 (threshold sensitivity) 在 50% threshold 报告 24；Appendix Table 9 也报告 24/32\n- 问题：同一数据、同一阈值（50%）下，Table 2 得 25 而 Appendix 得 24。论文解释为 \"bulk extraction vs dedicated per-layer analysis\"，但如果分析的是同一个 model checkpoint 的同一层同一 batch 的 attention weights，结果应一致。这暗示可能存在 batch sampling variance 或计算细节差异（如 attention 是否 averaged over all readout positions）。\n- 建议：明确说明两个分析使用了哪些不同的 input samples 或 averaging 方式导致了 ±1 差异。\n\n---\n\n## Questions to Authors\n\n**Q1**: Cross-instruction probe 使用 linear classifier 还是 MLP？Section 3.3 说 \"linear classifier (10-way)\"，但 Section 4.2 又说 \"Both linear and MLP probes confirm chance-level performance (10%)\"。主结果（Table 1 的 100%）用的是哪个？\n\n**Q2**: Ablation 中 \"5 demonstrations per task\" 对应多少 total observation-action pairs？每个 demo 的平均 trajectory 长度是多少？\n\n**Q3**: RSA 中 \"within-task observation pairs from 50 demonstrations\" — 每个 demo 取一个 observation 还是多个？如果是多个，同一 demo 内的 temporal autocorrelation 是否 inflate 了 RSA？\n\n**Q4**: Table 3 中 \"VLA Trained readout\" RSA peak = L12 (ρ=0.643)，但 Section 4.3 说 \"trained image_mean RSA peaks at L12 (ρ=0.628)\"。Readout 的 peak RSA (0.643) 也在 L12？这在正文中未明确标注 readout 的 per-layer profile——readout RSA 是否也呈 inverted-U？\n\n**Q5**: Untrained readout 在 Table 3 中 R² peak = L32 (0.609)。这意味着随机权重经过 32 层变换后反而是最好的 action-prediction representation？这如何解释？\n\n---\n\n## Minor Issues（不影响接收）\n\n- Abstract 第6行 \"self-supervised DINOv2 providing the highest geometric foundation (ρ = 0.692, exceeding all internal representations)\" — 建议加 \"under RSA\" qualifier，因为 CKA 下结论相反。\n- Section 4.2 第76行的长括号句（\"using 5 demonstrations per task; absolute values are not directly comparable to Table 3 but within-condition comparisons are valid\"）应移至方法描述处而非嵌入结果报告。\n- Discussion \"C1 likely generalizes via the causal mask; C2 may be Llama-2-specific\" — 这种无证据的猜测不应出现在学术论文中，建议删除或改为 explicit future work。\n- Appendix §D.4 Table 9 caption 中 \"Head counts from the 32-layer bulk extraction vary by ±1 from dedicated per-layer analyses (Table 2) due to threshold boundary cases\" — 此解释应在正文 Table 2 附近出现，不应让读者到 appendix 才发现不一致的原因。\n\n---\n\n## 主要优势总结\n\n- Factorial trained-vs-untrained control 是分析 VLA 的优秀实验范式\n- 四种互补分析方法（probe + attention + RSA + MLP）提供多角度验证\n- 诚实报告 null results 和 metric divergence\n- Appendix 中大量 robustness checks 体现严谨态度\n- Cross-benchmark (LIBERO-Spatial) validation 增加可信度\n\n---\n\n## 总体判断\n\n论文的实验框架和 factorial design 是其最大优势，但三个核心 claims 的证据强度均有问题：(1) readout 100% 是 trivial baseline；(2) inverted-U rise phase 极小且 metric-dependent；(3) ablation 使用不同数据规模。如果作者能在 rebuttal 中 (a) 用更难的 probe 任务验证 Finding 1、(b) 报告 L0→L12 升幅的 CI、(c) 用 50 demos 重跑 ablation，评分可提升至 borderline accept。当前状态下，claim-evidence mismatch 是主要顾虑。\n",
  "reviewer_id": "1",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1: 方法与实验严谨性审查\n\n## 论文信息\n- **标题**: Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\n- **Venue**: CoRL 2026\n\n---\n\n## 总体评分\n\n**Overall**: 3/5 (Borderline)\n\n**一句话总结**: 实验设计思路清晰、factorial control 有价值，但核心 probing 任务过于简单导致 claim 强度与证据不匹配，RSA inverted-U 的效应量极小，ablation 使用不同数据规模削弱因果推断力度。\n\n---\n\n## 官方维度打分（基于 CoRL reviewer guidelines: Originality, Quality, Clarity, Significance, Relevance）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 4/5 | Token-level factorial decomposition of VLA 是新颖的分析框架，prior work 没有做过 trained-vs-untrained 的系统对比 |\n| Quality (Technical Soundness) | 2.5/5 | 核心 probe 任务 trivially easy，RSA 效应量极小且 metric-dependent，ablation 数据规模不一致，缺乏多重比较校正 |\n| Clarity | 4/5 | 写作清晰、结构完整，数据呈现系统化 |\n| Significance | 3/5 | 对 VLA 内部机制提供了描述性洞察，但因证据力度不足，architectural implications 缺乏可操作性 |\n| Relevance | 4/5 | VLA 内部机制分析直接服务于 robot learning 社区的模型设计需求 |\n\n---\n\n## Summary\n\n本文对 OpenVLA-7B 在 LIBERO 上进行 token 级别表征分析，通过 cross-instruction probes、attention 分析、RSA 和 MLP probes 四种方法，比较 trained/pretrained/untrained 三个条件。主要发现：(1) image tokens 不编码 instruction 信息，readout token 是唯一的多模态汇聚点；(2) VLA fine-tuning 将 instruction routing 从中层转移到 entry-exit 模式；(3) LLM 对 vision encoder 输出进行非单调变换（inverted-U）。实验设计的 factorial structure 值得肯定，但多个核心 claim 的证据强度存在问题。\n\n---\n\n## Strengths\n\n**S1. 系统化的实验设计框架**\n三条件（trained/pretrained/untrained）× 两因素（instruction presence）的 factorial design 是分析 VLA 的好范式。这比 prior work（如 Grant et al., Häon et al.）的单条件分析更有控制力。Appendix 的 robustness checks（distance metric invariance, per-DOF decomposition, permutation test, seed sensitivity, demo subsampling）体现了实验严谨态度。\n\n**S2. 多指标互相验证**\nRSA + MLP probe + attention analysis + cross-instruction probe 四种方法从不同角度切入同一问题，且 CKA 作为 supplementary metric 在 appendix 中报告，体现了方法论意识。\n\n**S3. 诚实报告 negative/null results**\nRSA best-vs-best Δ=+0.017 (CI includes 0) 被如实标记为 n.s.；CKA 与 RSA 的 ordering 矛盾被正面讨论而非隐藏。这是好的学术实践。\n\n**S4. Cross-benchmark validation**\nLIBERO-Spatial 上的复现增加了核心发现的可信度（尽管仍在同一 simulator 内）。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Cross-instruction probe 任务 trivially easy，不支撑 \"multimodal convergence\" 的强 claim\n\n- 具体位置：Section 4.2 (Token-Level Functional Specialization), Table 1\n- 问题：10-way classification over 10 distinct instruction strings 对任何能 attend to instruction tokens 的位置都是 trivial 的。论文自己在 Appendix D.1 承认 \"even incidental attention (~12%) suffices for linear classification at L1\"。事实上，untrained model（随机权重）在 L1 也达到 100%（Table 1）。这意味着 100% 分类准确率不能作为 \"multimodal convergence\" 或 \"functional specialization\" 的强证据——它只反映 instruction embeddings 本身是线性可分的（这是 tokenizer 的 trivial 性质）。\n- 为什么影响接收：Finding 1（\"strict token-level functional specialization\"）是论文三大贡献之首，也是标题的核心 claim。如果 readout token 的 100% 准确率是 trivial baseline（随机权重也能达到），那么这个发现的 novelty 大幅缩水。真正有价值的发现是 image token 保持 chance level，但论文的对称叙事（\"image blind + readout as hub\"）过度依赖 readout 侧的结果。\n- 建议修改方向：(a) 增加更困难的 probe 任务（如区分语义相近的指令、或 fine-grained instruction attribute prediction）；(b) 调整 framing——将重点放在 image token 的 instruction-blindness（这是 non-trivial 的 negative result）而非 readout 的 100%（这是 trivial 的 positive result）；(c) 对 untrained 也达到 100%@L1 做更深入讨论——如果随机权重即可实现，trained model 维持 100% 的 significance 需要重新定义。\n\n**N2** [critical] RSA \"inverted-U\" 的 rise phase 效应量极小（Δρ = 0.016），且 metric-dependent\n\n- 具体位置：Section 4.3, Figure 3, Table 3; Appendix B.2\n- 问题：Trained image_mean RSA 从 L0 (0.612) 到 L12 (0.628) 的升幅仅为 0.016（2.6%）。Best-vs-best training effect (+0.017) 的 CI 包含 0。更严重的是，Appendix B.2 显示 linear CKA 完全逆转了 RSA ordering（untrained > trained > DINOv2），且 linear CKA per-layer profile 呈单调上升，完全没有 inverted-U。这意味着 \"non-monotonic refinement\" 是 metric-specific 的描述，而非 representation 的 intrinsic property。\n- 为什么影响接收：Finding 3（\"non-monotonic refinement of vision encoder output\"）是论文贡献之一。如果这个 pattern 仅在 RSA（Spearman rank correlation on cosine-distance RDMs）下成立，在另一个标准 metric（CKA）下消失甚至逆转，那么 generalizability 成问题。论文的 architectural implication（\"vision encoder quality matters more than LLM scale\"）建立在 DINOv2 RSA 最高这个 RSA-specific 结果上。\n- 建议修改方向：(a) 明确 qualify claims 的 metric-dependence（\"under RSA, we observe...\"）；(b) 讨论为什么 RSA 比 CKA 更 appropriate for this question（目前 Method §3.5 的 justification 不够充分——\"CKA is sensitive to kernel choice\" 同样可以反过来说 RSA 对 distance function 选择敏感）；(c) 考虑 inverted-U 的 rise phase 是否在统计上 significant——L0→L12 的 +0.016 需要 CI。\n\n**N3** [critical] L1 attention ablation 使用 5 demos（vs 主实验 50 demos），因果推断的可靠性存疑\n\n- 具体位置：Section 4.2, paragraph \"Ablation reveals functional specialization\"（第76行）\n- 问题：Ablation 实验仅使用 5 demos per task（50 个 total datapoints），而主实验 Table 3 使用 50 demos per task。论文承认 \"absolute values are not directly comparable\" 但仍得出强因果结论（\"instruction-dominant heads redirect attention from image to instruction tokens at the cost of local action encoding\"）。用 50 个数据点训练一个 2-layer MLP probe（>1M 参数），然后报告 R² 从 0.256 到 0.375 的提升——这个 R² 的 baseline 本身就非常低（0.256），暗示 probe 在 5 demos 下严重 underfitting，ablation \"improvement\" 可能是 reduced effective input dimensionality 带来的 regularization effect 而非 genuine functional specialization。\n- 为什么影响接收：这是论文中唯一的 causal intervention（其余都是 observational）。如果 ablation 不可靠，论文就只有 correlational evidence。\n- 建议修改方向：(a) 用 50 demos 重跑 ablation，使 baseline R² 与 Table 3 直接 comparable；(b) 如果 50 demos 不可行，至少报告 N（总 observation-action pairs 数）并讨论 probe capacity vs sample size 的比率；(c) 添加 random ablation control（随机 zero 同等数量的 non-instruction-dominant heads）以排除 \"任何 attention zeroing 都能提升 R²\" 的 confound。\n\n---\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 缺乏多重比较校正（family-wise error）\n\n- 具体位置：贯穿全文所有统计检验\n- 问题：论文对 32 层 × 3 条件 × 多个 metric 进行了大量逐层比较，但没有任何 Bonferroni、Holm、或 FDR 校正。虽然单个 bootstrap CI 是 valid 的，但在数十个比较中找到 p < 0.05 的概率很高。\n- 建议：至少对 key claims（inverted-U peak significance、training effects per layer）应用 FDR correction 并报告 adjusted p-values。\n\n**W2** [warning] Probe 的 total N 未报告，capacity 控制不充分\n\n- 具体位置：Section 3.5 (Functional Action Probes), Section 4.1 (Experimental Setup)\n- 问题：50 demos per task × 10 tasks = 500 demonstrations，但每个 demo 有多少 timesteps？Total N（observation-action pairs for probe training）从未明确报告。2-layer MLP (4096→256→7) 有 ~1.05M 参数。如果 N < 10,000，probe 可能 overfit；如果 N > 100,000，probe 可能 underfit。Early stopping (patience 5) 是部分 mitigation 但不充分。\n- 建议：报告 exact N；添加 linear probe 作为 capacity lower-bound（Method 中提到 linear probe 也在 image_mean 上得 10%，但未对 R² 做 linear vs MLP 对比）。\n\n**W3** [warning] \"Untrained\" condition 的 L1 = 100% 结果削弱 Finding 1 的 interpretation\n\n- 具体位置：Table 1, Appendix D.1\n- 问题：随机初始化的 LLM 在 L1 也能实现 100% instruction classification。论文将此解释为 \"incidental\"（附录说 ~12% attention 即可），但这暴露了 probe 任务的 trivial nature。更重要的是，untrained model 的 100%→82% 衰减 pattern 很有趣但讨论不足——为什么随机权重会导致信息逐层丢失？这可能揭示 residual stream 中 signal-to-noise ratio 的衰减，值得展开。\n- 建议：增加讨论 untrained 的 decay mechanism；考虑 probe 任务难度是否足以区分 \"genuine multimodal integration\" 和 \"trivial linear separability\"。\n\n**W4** [warning] Frozen vision encoder 是 feature 但也是 confound\n\n- 具体位置：Section 3.1 (Model and Data)\n- 问题：三个条件共享 frozen vision encoder 和 projector，这使得 image_mean 在 L0 的起始 representation 完全相同。论文因此无法评估 VLA training 对 vision processing 的 full effect（只能评估 LLM 如何处理固定的 vision output）。然而论文在 Discussion 中得出 \"vision encoder quality may matter more than LLM scale\" 这一 architectural implication——这个结论需要 across-encoder 实验（如换 CLIP-only encoder），而非单一 frozen encoder 内的分析。\n- 建议：qualify 这个 architectural implication 为 \"under fixed encoder\" 条件下的观察；或增加对比实验（不同 vision encoder 的 RSA comparison）。\n\n**W5** [warning] 25 vs 24 heads 不一致需要更清晰解释\n\n- 具体位置：Table 2 报告 L1 VLA-trained = 25/32；Appendix Table 10 (threshold sensitivity) 在 50% threshold 报告 24；Appendix Table 9 也报告 24/32\n- 问题：同一数据、同一阈值（50%）下，Table 2 得 25 而 Appendix 得 24。论文解释为 \"bulk extraction vs dedicated per-layer analysis\"，但如果分析的是同一个 model checkpoint 的同一层同一 batch 的 attention weights，结果应一致。这暗示可能存在 batch sampling variance 或计算细节差异（如 attention 是否 averaged over all readout positions）。\n- 建议：明确说明两个分析使用了哪些不同的 input samples 或 averaging 方式导致了 ±1 差异。\n\n---\n\n## Questions to Authors\n\n**Q1**: Cross-instruction probe 使用 linear classifier 还是 MLP？Section 3.3 说 \"linear classifier (10-way)\"，但 Section 4.2 又说 \"Both linear and MLP probes confirm chance-level performance (10%)\"。主结果（Table 1 的 100%）用的是哪个？\n\n**Q2**: Ablation 中 \"5 demonstrations per task\" 对应多少 total observation-action pairs？每个 demo 的平均 trajectory 长度是多少？\n\n**Q3**: RSA 中 \"within-task observation pairs from 50 demonstrations\" — 每个 demo 取一个 observation 还是多个？如果是多个，同一 demo 内的 temporal autocorrelation 是否 inflate 了 RSA？\n\n**Q4**: Table 3 中 \"VLA Trained readout\" RSA peak = L12 (ρ=0.643)，但 Section 4.3 说 \"trained image_mean RSA peaks at L12 (ρ=0.628)\"。Readout 的 peak RSA (0.643) 也在 L12？这在正文中未明确标注 readout 的 per-layer profile——readout RSA 是否也呈 inverted-U？\n\n**Q5**: Untrained readout 在 Table 3 中 R² peak = L32 (0.609)。这意味着随机权重经过 32 层变换后反而是最好的 action-prediction representation？这如何解释？\n\n---\n\n## Minor Issues（不影响接收）\n\n- Abstract 第6行 \"self-supervised DINOv2 providing the highest geometric foundation (ρ = 0.692, exceeding all internal representations)\" — 建议加 \"under RSA\" qualifier，因为 CKA 下结论相反。\n- Section 4.2 第76行的长括号句（\"using 5 demonstrations per task; absolute values are not directly comparable to Table 3 but within-condition comparisons are valid\"）应移至方法描述处而非嵌入结果报告。\n- Discussion \"C1 likely generalizes via the causal mask; C2 may be Llama-2-specific\" — 这种无证据的猜测不应出现在学术论文中，建议删除或改为 explicit future work。\n- Appendix §D.4 Table 9 caption 中 \"Head counts from the 32-layer bulk extraction vary by ±1 from dedicated per-layer analyses (Table 2) due to threshold boundary cases\" — 此解释应在正文 Table 2 附近出现，不应让读者到 appendix 才发现不一致的原因。\n\n---\n\n## 主要优势总结\n\n- Factorial trained-vs-untrained control 是分析 VLA 的优秀实验范式\n- 四种互补分析方法（probe + attention + RSA + MLP）提供多角度验证\n- 诚实报告 null results 和 metric divergence\n- Appendix 中大量 robustness checks 体现严谨态度\n- Cross-benchmark (LIBERO-Spatial) validation 增加可信度\n\n---\n\n## 总体判断\n\n论文的实验框架和 factorial design 是其最大优势，但三个核心 claims 的证据强度均有问题：(1) readout 100% 是 trivial baseline；(2) inverted-U rise phase 极小且 metric-dependent；(3) ablation 使用不同数据规模。如果作者能在 rebuttal 中 (a) 用更难的 probe 任务验证 Finding 1、(b) 报告 L0→L12 升幅的 CI、(c) 用 50 demos 重跑 ablation，评分可提升至 borderline accept。当前状态下，claim-evidence mismatch 是主要顾虑。\n",
    "reviewer_id": "1",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 114 · 2026-05-17T18:07:40.375975+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3872
}
```

</details>

---


### Assistant

_source line 115 · 2026-05-17T18:07:49.422496+00:00_

审稿意见已提交给 Review Director。

**核心判断**：Overall 3/5 (Borderline)。论文的 factorial experimental design 是优势，但三个主要 findings 的证据强度均存在问题：

1. **N1 [critical]**: Cross-instruction probe 10-way 分类对 readout token 是 trivially easy（随机权重也达到 100%@L1），不支撑 "multimodal convergence hub" 的强 claim
2. **N2 [critical]**: RSA inverted-U 的 rise phase 仅 Δρ=0.016（2.6%），且 CKA 下完全消失/逆转，metric-dependent
3. **N3 [critical]**: L1 attention ablation 用 5 demos vs 主实验 50 demos，因果推断可靠性不足

如果作者能在 rebuttal 中解决这三个问题（更难 probe 任务、报告 rise CI、50-demo ablation），评分可上调。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1"
}
```

</details>

---


## Round 6

## Round 6

4 recorded events


### User

_source line 116 · 2026-05-17T18:14:08.784967+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 2 的完整审稿意见

请逐条回应以下 Reviewer 2 的审稿意见。对每一条使用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

以下是 Reviewer 2 的完整审稿原文：

**Overall: 5/10 (Marginally below acceptance threshold)**
**Confidence: 4/5**

**一句话总结**: 方法论严谨、写作清晰，但核心贡献 C1（image tokens instruction-blind）是 causal attention mask 的数学必然结果而非经验性发现，显著削弱新颖性；其余贡献效应量小或存在度量敏感性问题，对 CoRL 社区缺乏 actionable insights。

### Must-Fix 问题

**N1 [critical] C1 是 causal mask 的数学必然结果**
OpenVLA 的 token 序列为 [image] → [instruction] → [readout/action]。Causal attention 中位置 i 的表征仅依赖位置 ≤ i。Image tokens 先于 instruction tokens，因此 image tokens 在任何层都无法 attend to instruction tokens——这是架构决定的数学性质，非 empirical finding。Frozen vision encoder 只接收图像，instruction invariance 同样 trivially expected。Discussion 仅一句话承认（"C1 likely generalizes via the causal mask"），但全文将 C1 作为首要贡献和标题基础。untrained 模型 L1 即达 100% classification 进一步支持 trivial 判断。建议重新定位 C1 或澄清 token ordering。

**N2 [critical] RSA 与 CKA 矛盾未充分解决**
Linear CKA 完全反转 RSA ordering（untrained > trained > DINOv2），直接否定 "DINOv2 provides highest geometric foundation"。RDM kernel CKA 中 DINOv2 在所有变体排名最低。Linear CKA per-layer profile 无 inverted-U。论文将此放在 appendix 归因于 "metrics capture different properties"，但未给出 principled argument 解释为何应信任 RSA。如果核心 claims 依赖度量选择，它们就不是 robust findings。

### Should-Fix 问题

**W1** RSA best-vs-best 训练效应在 LIBERO-Goal 不显著（Δ=+0.017, CI includes 0, n.s.），但 Abstract/Intro 中未标注
**W2** L1 ablation 使用 5 demos（vs. 主实验 50），R² 基准差异大（0.256 vs. ~0.65），可比性存疑
**W3** 缺少 Llama-2 和 Open X-Embodiment 关键引用
**W4** Architectural implications 仅为 observational insights，未通过设计实验验证（如 encoder swap），对 CoRL 实践社区 actionable value 不足
**W5** 单模型（OpenVLA-7B）、单 benchmark family（LIBERO），泛化性有限

### 小问题
- M1: Intro "untested assumption" 是 straw man（causal mask 下无人会这样假设）
- M2: "readout token" 与 "last_preaction" 交替使用未定义等价性
- M3: conclusion.tex 未被 main.tex \input
- M4: alain2017 实际年份应为 2016；nostalgebraist2020 blog post 格式不规范
- M5: 多个 arXiv preprints 可能已有正式发表版本
- M6: 个别 R² 精度不统一（2位 vs. 3位）

### 与竞争者区分度
Grant et al. (2026) 已发现 visual dominance + language "encoded but not used"。本文的 token-level 分解在 causal mask 约束下提供的额外 insight 有限。Häon et al. (CoRL 2025) 提供了 interventional analysis（activation steering），本文主要是 observational。整体增量有限。

---

请逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 117 · 2026-05-17T18:16:36.523195+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 交叉回应：对 Reviewer 2 审稿意见的逐条评价\n\n---\n\n## Must-Fix 问题\n\n**[AGREE] R2-N1: C1 是 causal mask 的数学必然结果**\n\n完全同意。这是一个根本性批评。OpenVLA 的 token 序列为 [image₁...imageₙ] → [instruction₁...instructionₘ] → [readout/action]。在 causal attention mask 下，位置 i 只能 attend to 位置 ≤ i。Image tokens 排在 instruction tokens 之前，因此 image tokens 在任何层的 representation 都不可能包含 instruction 信息——无论 LLM 权重是 trained、pretrained 还是 random。\n\n这正解释了我在 R1-N1 中指出的现象：untrained model 在 L1 也达到 100% classification。不是因为 \"incidental attention suffices\"，而是因为 image tokens 的 instruction-invariance 根本就是 architecture-guaranteed 的。Cross-instruction probe 在 image_mean 上得 10%（chance）不是一个 empirical finding，而是在 verify 一个已知的数学性质。\n\n我的 R1-N1 从 \"probe 太简单\" 角度质疑了 C1，R2-N1 从更根本的 \"架构决定论\" 角度指出同一问题。两者互补：\n- R2-N1 说明 image-token instruction-blindness 是 trivial（causal mask）\n- R1-N1 说明 readout-token 100% 也是 trivial（instruction embeddings linearly separable + any attention suffices）\n\n合在一起，C1 整体上缺乏 empirical novelty。论文 Discussion 仅一句 \"C1 likely generalizes via the causal mask\" 的承认远远不够——这应该从一开始就作为已知约束讨论，而非作为 \"discovery\" 呈现。\n\n补充证据：Section 3.2 明确定义 token ordering（\"DinoSigLIP+Projector, the projector output, immediately before LLM processing\"），Section 3.1 确认 vision encoder 是 frozen 且不接收 instruction input。这两点已经从 architecture 层面 guarantee 了 C1。\n\n---\n\n**[AGREE] R2-N2: RSA 与 CKA 矛盾未充分解决**\n\n同意，与我的 R1-N2 一致。补充几点：\n\n1. 论文 Section 3.5 给出的 RSA preference 论据是 \"CKA sensitive to kernel choice\" + \"linear CKA has dimension mismatch\"。但 RSA 同样 sensitive to distance function choice（representation 用 cosine、action 用 Euclidean，这本身就是一个 design choice）。论文的 Appendix C.6.1 验证了 action distance 的 metric invariance（cosine vs Euclidean for actions），但未验证 representation distance 的选择（如 Euclidean vs cosine for 4096-D representations）。\n\n2. Appendix B.2 的关键数据：Linear CKA per-layer profile 是**单调递增**的（L0: 0.081 → L32: 0.098），完全没有 inverted-U。这直接否定了 \"non-monotonic refinement\" 作为 representation 的 intrinsic property——它仅在 RSA 下成立。\n\n3. RDM kernel CKA 中 DINOv2 排名最低（0.241），而 RSA 中 DINOv2 排名最高（0.692）。这个完全反转使得 \"vision encoder quality emerges as a key design lever\"（Discussion 第3段）的结论变成 metric-contingent claim。\n\n不过，我认为论文在 Appendix 中诚实报告了 CKA divergence（Figure 6），这比隐瞒好。问题在于正文的 claims 没有相应 qualify。\n\n---\n\n## Should-Fix 问题\n\n**[AGREE] R2-W1: RSA n.s. 在 Abstract/Intro 未标注**\n\n同意。Abstract 第6行报告 \"DINOv2 providing the highest geometric foundation (ρ = 0.692)\" 未加 qualifier；Introduction 第25行写 \"modest geometric gain (Δ = 0.017–0.023, 3–4%)\" 但未标注 LIBERO-Goal 的 Δ=+0.017 为 n.s.。这构成 selective reporting——读者必须到 Appendix Table 8 才能发现 CI includes 0。正文应在首次提到时标注统计显著性状态。\n\n---\n\n**[AGREE] R2-W2: L1 ablation 5 demos 可比性存疑**\n\n完全同意，与我的 R1-N3 一致。R² baseline 从 ~0.65（50 demos, Table 3）降到 0.256（5 demos, Section 4.2）说明 probe 在 5 demos 下严重 underfitting。在这种 regime 下，zeroing attention 可能通过 reduced effective dimensionality 起到类似 regularization 的效果（fewer attended positions → lower variance representation → better generalization for small N），而非反映 genuine functional specialization。\n\n---\n\n**[PARTIALLY AGREE] R2-W3: 缺少关键引用**\n\n未读 references.bib，无法完全确认。但如果 Llama-2（Touvron et al., 2023）和 Open X-Embodiment（Padalkar et al., 2023）确实未直接引用，这是应修复的遗漏。这两个是模型核心组件和训练数据的 primary sources。\n\n---\n\n**[AGREE] R2-W4: Architectural implications 缺乏 actionable verification**\n\n同意，与我的 R1-W4 一致。\"Vision encoder quality may matter more than LLM scale\" 需要 across-encoder 实验（如替换为 CLIP-only encoder 或 weaker DINOv2 variant）来验证。当前证据仅是 \"DINOv2 RSA 最高\"（且 CKA 下不成立），从 correlational observation 到 design recommendation 的跳跃太大。对 CoRL 这个实践导向的社区，缺乏 actionable takeaway 是显著弱点。\n\n---\n\n**[AGREE] R2-W5: 单模型单 benchmark 泛化性有限**\n\n同意，与我的观点一致。LIBERO-Goal 和 LIBERO-Spatial 同属一个 simulator、同一类 tabletop manipulation。真正的 generalization evidence 需要：(a) 不同 VLA architecture（RT-2, π₀）；(b) 不同 task domain（navigation, dexterous manipulation）；(c) 不同 backbone（non-Llama）。\n\n---\n\n## 小问题\n\n**[AGREE] R2-M1: \"untested assumption\" 是 straw man**\n\n部分同意。Introduction 第5行 \"A central but untested assumption is that all token types within the LLM contribute uniformly to action prediction\" — 在 causal mask 下，没有人会假设 image tokens 能编码 instruction 信息。但我对 R2 的判断做一个小修正：这个 \"assumption\" 如果理解为 \"all token types contribute equally to action prediction quality\"（而非 instruction encoding），则不完全是 straw man——image tokens 确实可能通过 visual information 对 action quality 有贡献。然而论文的 cross-instruction probe 测试的是 instruction encoding 而非 action contribution，所以 R2 的批评基本成立。\n\n---\n\n**[REBUT] R2-M2: \"readout token\" 与 \"last_preaction\" 未定义等价性**\n\n不同意。Section 3.2 (Representation Extraction) 第(c)项明确定义：\"**LLM readout**, the activation at the final pre-action token position at each layer\"。这里 \"readout\" 和 \"last pre-action position\" 在首次出现时就被定义为等价。后续交替使用不构成歧义。\n\n---\n\n**[AGREE] R2-M3: conclusion.tex 未被 main.tex \\input**\n\n确认。main.tex 的 \\input 序列为：introduction → related_work → method → experiments → discussion → (bibliography) → appendix。conclusion.tex 存在但未被包含，导致编译后的论文没有独立的 Conclusion section。Discussion 最后一句 \"code will be released upon acceptance\" 勉强充当结尾，但格式上不规范。CoRL 2026 模板是否要求独立 Conclusion section 需确认，但多数会议论文包含该 section。\n\n---\n\n**[AGREE] R2-M4: 引用格式问题**\n\n同意。Alain & Bengio 的 probe paper 虽然 2016 年上 arXiv，但正式发表于 ICLR 2017 Workshop，引用年份取决于 bib entry 如何标注。nostalgebraist (2020) 的 logit lens 是 blog post，应标注为 @misc 或 @online，且在学术论文中引用 blog post 需谨慎。\n\n---\n\n**[AGREE] R2-M5 & M6**: 有效的 minor issues，不影响核心判断。\n\n---\n\n## 对 \"竞争者区分度\" 的回应\n\n**[PARTIALLY AGREE]**\n\nR2 的核心论点是：在 causal mask 约束下，本文相对 Grant et al. (2026) 的增量有限。我同意 C1 的增量被 causal mask argument 大幅削弱。但我认为 R2 对 C2（routing shift from mid-depth to entry-exit）的评价不够：\n\n- C2 不是 causal mask 能 predict 的——它需要实际比较 trained vs pretrained attention patterns 才能观察到。Llama-2 base 的 mid-depth routing (L9-L16, 15-22 heads) vs VLA-trained 的 entry-exit routing (L0-L1, L31) 这个 redistribution 是 genuine empirical finding。\n- 然而 C2 的 practical significance 仍然有限：knowing routing shifts to L1 后如何改进 VLA design？论文未给出答案。\n\n对 Häon et al. (CoRL 2025) 的对比：R2 正确指出该工作有 interventional evidence (activation steering)，而本文主要是 observational。本文的 L1 ablation 是唯一的 intervention，但如 R1-N3 和 R2-W2 所指出，其可靠性存疑。\n\n---\n\n## 综合判断\n\nR2 的 N1（causal mask argument）是比我的 R1-N1（probe too easy）更根本的批评。两者共同指向同一结论：**C1 不是一个有意义的 empirical finding**。结合 RSA 的 metric-dependence（R2-N2, R1-N2）和 ablation 的数据规模问题（R2-W2, R1-N3），论文的三个核心贡献中只有 C2（routing redistribution）有 genuine novelty，但效应的 practical significance 未被验证。\n\n我维持我的 Overall 3/5 (Borderline) 评分。R2 的 causal mask argument 进一步坚定了我对 C1 novelty 的怀疑，但论文的实验框架（factorial design + multi-metric）仍有 methodological value。\n",
  "reviewer_id": "1",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 交叉回应：对 Reviewer 2 审稿意见的逐条评价\n\n---\n\n## Must-Fix 问题\n\n**[AGREE] R2-N1: C1 是 causal mask 的数学必然结果**\n\n完全同意。这是一个根本性批评。OpenVLA 的 token 序列为 [image₁...imageₙ] → [instruction₁...instructionₘ] → [readout/action]。在 causal attention mask 下，位置 i 只能 attend to 位置 ≤ i。Image tokens 排在 instruction tokens 之前，因此 image tokens 在任何层的 representation 都不可能包含 instruction 信息——无论 LLM 权重是 trained、pretrained 还是 random。\n\n这正解释了我在 R1-N1 中指出的现象：untrained model 在 L1 也达到 100% classification。不是因为 \"incidental attention suffices\"，而是因为 image tokens 的 instruction-invariance 根本就是 architecture-guaranteed 的。Cross-instruction probe 在 image_mean 上得 10%（chance）不是一个 empirical finding，而是在 verify 一个已知的数学性质。\n\n我的 R1-N1 从 \"probe 太简单\" 角度质疑了 C1，R2-N1 从更根本的 \"架构决定论\" 角度指出同一问题。两者互补：\n- R2-N1 说明 image-token instruction-blindness 是 trivial（causal mask）\n- R1-N1 说明 readout-token 100% 也是 trivial（instruction embeddings linearly separable + any attention suffices）\n\n合在一起，C1 整体上缺乏 empirical novelty。论文 Discussion 仅一句 \"C1 likely generalizes via the causal mask\" 的承认远远不够——这应该从一开始就作为已知约束讨论，而非作为 \"discovery\" 呈现。\n\n补充证据：Section 3.2 明确定义 token ordering（\"DinoSigLIP+Projector, the projector output, immediately before LLM processing\"），Section 3.1 确认 vision encoder 是 frozen 且不接收 instruction input。这两点已经从 architecture 层面 guarantee 了 C1。\n\n---\n\n**[AGREE] R2-N2: RSA 与 CKA 矛盾未充分解决**\n\n同意，与我的 R1-N2 一致。补充几点：\n\n1. 论文 Section 3.5 给出的 RSA preference 论据是 \"CKA sensitive to kernel choice\" + \"linear CKA has dimension mismatch\"。但 RSA 同样 sensitive to distance function choice（representation 用 cosine、action 用 Euclidean，这本身就是一个 design choice）。论文的 Appendix C.6.1 验证了 action distance 的 metric invariance（cosine vs Euclidean for actions），但未验证 representation distance 的选择（如 Euclidean vs cosine for 4096-D representations）。\n\n2. Appendix B.2 的关键数据：Linear CKA per-layer profile 是**单调递增**的（L0: 0.081 → L32: 0.098），完全没有 inverted-U。这直接否定了 \"non-monotonic refinement\" 作为 representation 的 intrinsic property——它仅在 RSA 下成立。\n\n3. RDM kernel CKA 中 DINOv2 排名最低（0.241），而 RSA 中 DINOv2 排名最高（0.692）。这个完全反转使得 \"vision encoder quality emerges as a key design lever\"（Discussion 第3段）的结论变成 metric-contingent claim。\n\n不过，我认为论文在 Appendix 中诚实报告了 CKA divergence（Figure 6），这比隐瞒好。问题在于正文的 claims 没有相应 qualify。\n\n---\n\n## Should-Fix 问题\n\n**[AGREE] R2-W1: RSA n.s. 在 Abstract/Intro 未标注**\n\n同意。Abstract 第6行报告 \"DINOv2 providing the highest geometric foundation (ρ = 0.692)\" 未加 qualifier；Introduction 第25行写 \"modest geometric gain (Δ = 0.017–0.023, 3–4%)\" 但未标注 LIBERO-Goal 的 Δ=+0.017 为 n.s.。这构成 selective reporting——读者必须到 Appendix Table 8 才能发现 CI includes 0。正文应在首次提到时标注统计显著性状态。\n\n---\n\n**[AGREE] R2-W2: L1 ablation 5 demos 可比性存疑**\n\n完全同意，与我的 R1-N3 一致。R² baseline 从 ~0.65（50 demos, Table 3）降到 0.256（5 demos, Section 4.2）说明 probe 在 5 demos 下严重 underfitting。在这种 regime 下，zeroing attention 可能通过 reduced effective dimensionality 起到类似 regularization 的效果（fewer attended positions → lower variance representation → better generalization for small N），而非反映 genuine functional specialization。\n\n---\n\n**[PARTIALLY AGREE] R2-W3: 缺少关键引用**\n\n未读 references.bib，无法完全确认。但如果 Llama-2（Touvron et al., 2023）和 Open X-Embodiment（Padalkar et al., 2023）确实未直接引用，这是应修复的遗漏。这两个是模型核心组件和训练数据的 primary sources。\n\n---\n\n**[AGREE] R2-W4: Architectural implications 缺乏 actionable verification**\n\n同意，与我的 R1-W4 一致。\"Vision encoder quality may matter more than LLM scale\" 需要 across-encoder 实验（如替换为 CLIP-only encoder 或 weaker DINOv2 variant）来验证。当前证据仅是 \"DINOv2 RSA 最高\"（且 CKA 下不成立），从 correlational observation 到 design recommendation 的跳跃太大。对 CoRL 这个实践导向的社区，缺乏 actionable takeaway 是显著弱点。\n\n---\n\n**[AGREE] R2-W5: 单模型单 benchmark 泛化性有限**\n\n同意，与我的观点一致。LIBERO-Goal 和 LIBERO-Spatial 同属一个 simulator、同一类 tabletop manipulation。真正的 generalization evidence 需要：(a) 不同 VLA architecture（RT-2, π₀）；(b) 不同 task domain（navigation, dexterous manipulation）；(c) 不同 backbone（non-Llama）。\n\n---\n\n## 小问题\n\n**[AGREE] R2-M1: \"untested assumption\" 是 straw man**\n\n部分同意。Introduction 第5行 \"A central but untested assumption is that all token types within the LLM contribute uniformly to action prediction\" — 在 causal mask 下，没有人会假设 image tokens 能编码 instruction 信息。但我对 R2 的判断做一个小修正：这个 \"assumption\" 如果理解为 \"all token types contribute equally to action prediction quality\"（而非 instruction encoding），则不完全是 straw man——image tokens 确实可能通过 visual information 对 action quality 有贡献。然而论文的 cross-instruction probe 测试的是 instruction encoding 而非 action contribution，所以 R2 的批评基本成立。\n\n---\n\n**[REBUT] R2-M2: \"readout token\" 与 \"last_preaction\" 未定义等价性**\n\n不同意。Section 3.2 (Representation Extraction) 第(c)项明确定义：\"**LLM readout**, the activation at the final pre-action token position at each layer\"。这里 \"readout\" 和 \"last pre-action position\" 在首次出现时就被定义为等价。后续交替使用不构成歧义。\n\n---\n\n**[AGREE] R2-M3: conclusion.tex 未被 main.tex \\input**\n\n确认。main.tex 的 \\input 序列为：introduction → related_work → method → experiments → discussion → (bibliography) → appendix。conclusion.tex 存在但未被包含，导致编译后的论文没有独立的 Conclusion section。Discussion 最后一句 \"code will be released upon acceptance\" 勉强充当结尾，但格式上不规范。CoRL 2026 模板是否要求独立 Conclusion section 需确认，但多数会议论文包含该 section。\n\n---\n\n**[AGREE] R2-M4: 引用格式问题**\n\n同意。Alain & Bengio 的 probe paper 虽然 2016 年上 arXiv，但正式发表于 ICLR 2017 Workshop，引用年份取决于 bib entry 如何标注。nostalgebraist (2020) 的 logit lens 是 blog post，应标注为 @misc 或 @online，且在学术论文中引用 blog post 需谨慎。\n\n---\n\n**[AGREE] R2-M5 & M6**: 有效的 minor issues，不影响核心判断。\n\n---\n\n## 对 \"竞争者区分度\" 的回应\n\n**[PARTIALLY AGREE]**\n\nR2 的核心论点是：在 causal mask 约束下，本文相对 Grant et al. (2026) 的增量有限。我同意 C1 的增量被 causal mask argument 大幅削弱。但我认为 R2 对 C2（routing shift from mid-depth to entry-exit）的评价不够：\n\n- C2 不是 causal mask 能 predict 的——它需要实际比较 trained vs pretrained attention patterns 才能观察到。Llama-2 base 的 mid-depth routing (L9-L16, 15-22 heads) vs VLA-trained 的 entry-exit routing (L0-L1, L31) 这个 redistribution 是 genuine empirical finding。\n- 然而 C2 的 practical significance 仍然有限：knowing routing shifts to L1 后如何改进 VLA design？论文未给出答案。\n\n对 Häon et al. (CoRL 2025) 的对比：R2 正确指出该工作有 interventional evidence (activation steering)，而本文主要是 observational。本文的 L1 ablation 是唯一的 intervention，但如 R1-N3 和 R2-W2 所指出，其可靠性存疑。\n\n---\n\n## 综合判断\n\nR2 的 N1（causal mask argument）是比我的 R1-N1（probe too easy）更根本的批评。两者共同指向同一结论：**C1 不是一个有意义的 empirical finding**。结合 RSA 的 metric-dependence（R2-N2, R1-N2）和 ablation 的数据规模问题（R2-W2, R1-N3），论文的三个核心贡献中只有 C2（routing redistribution）有 genuine novelty，但效应的 practical significance 未被验证。\n\n我维持我的 Overall 3/5 (Borderline) 评分。R2 的 causal mask argument 进一步坚定了我对 C1 novelty 的怀疑，但论文的实验框架（factorial design + multi-metric）仍有 methodological value。\n",
    "reviewer_id": "1",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 118 · 2026-05-17T18:16:40.407615+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3884
}
```

</details>

---


### Assistant

_source line 119 · 2026-05-17T18:16:50.444320+00:00_

交叉回应已提交。核心判断：

- **R2-N1（causal mask）**：完全同意——比我的 "probe too easy" 批评更根本，从架构层面 trivialize 了 C1
- **R2-N2（RSA/CKA 矛盾）**：同意，与我的 R1-N2 一致
- **R2-W1–W5**：基本全部同意，多数与我的发现重叠
- **唯一 REBUT**：R2-M2（readout/last_preaction 术语），Section 3.2 已明确定义等价性

两位 reviewer 的核心共识：C1 缺乏 empirical novelty（R2 从 causal mask，R1 从 probe triviality），RSA claims 是 metric-dependent 的，ablation 数据规模问题削弱因果推断。C2（routing redistribution）是论文唯一有 genuine novelty 的贡献。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1"
}
```

</details>

---


## Round 7

## Round 7

40 recorded events


### User

_source line 120 · 2026-05-18T01:49:58.316275+00:00_

[Round 1 审稿请求]:
## 审稿任务 — Reviewer 1: 方法/实验严谨性

**论文**: "Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model"
**路径**: `projects/vla-ssd/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, appendix.tex, references.bib）
**Venue**: CoRL 2026, double-blind, 8 页正文 + refs + appendix, Limitations section 必须（计入 8 页）
**Deadline**: 2026-05-29

### 你的审查侧重

**1. 统计方法论**
- 多重比较校正：论文声称使用 FDR correction (Benjamini-Hochberg)，验证其是否恰当应用于 32 层 × 多条件 × 多 metric 的比较
- Bootstrap CI 报告是否完整（特别是 RSA rise phase L0→L12 的 CI）
- Probe 的 N/params ratio 报告（论文声称 N=63,228, ratio≈0.05）是否合理
- Permutation test 和 seed sensitivity 的充分性

**2. 实验设计**
- 三条件对照（trained/pretrained/untrained）是否充分隔离 VLA fine-tuning 的贡献？Llama-2 base 数据是否完整整合？
- L1 attention ablation：论文现在声称使用 50 demonstrations（N=63,228）。检查 ablation 设计：dominant 24 heads vs non-dominant 8 heads control 的因果推断是否合理
- Cross-benchmark validation (LIBERO-Goal + LIBERO-Spatial) 的独立性和充分性

**3. Round 4 Critical Issues 修复检查**
以下是上轮审稿的 critical issues，请逐条验证当前版本是否充分解决：
- **R4-N1 (critical)**: C1（token-level specialization）被批为 causal mask 必然结果 + probe trivially easy。论文应已 reframe 为"experimental framework + empirical verification"而非"empirical finding"
- **R4-N2 (critical)**: RSA inverted-U 的 rise phase 极小（Δρ=0.016）且 metric-dependent（CKA 反转）。论文应已加"under RSA" qualifier 并在正文讨论 CKA 分歧
- **R4-N3 (critical)**: L1 ablation 原用 5 demos（严重 underfitting）。论文应已改用 50 demos
- **R4-W2 (warning)**: 缺乏多重比较校正。论文应已加 FDR correction
- **R4-W3 (warning)**: Probe N 和 capacity 未报告。论文应已报告 N=63,228 和 N/params

**4. 新发现的方法论问题**
- 除检查上轮问题外，以独立审稿人视角评估是否存在新的方法论缺陷
- 特别关注：probing methodology (Belinkov 2022 批判)、RSA vs CKA 选择的 principled justification、attention 分析的 threshold sensitivity

### 输出格式
按以下结构输出审稿意见：
1. Summary（2-3 句）
2. Strengths（逐条）
3. Weaknesses（分 critical / warning / info 三级，逐条）
4. Round 4 Issue Status（逐条标注 RESOLVED / PARTIALLY_RESOLVED / NOT_RESOLVED）
5. Questions for Authors
6. Overall Score（1-10）和 Confidence（1-5）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 121 · 2026-05-18T01:50:11.076297+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
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

_source line 122 · 2026-05-18T01:50:11.177120+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 123 · 2026-05-18T01:50:16.013258+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 124 · 2026-05-18T01:50:16.868610+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-18T01:50:16.970289+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 126 · 2026-05-18T01:50:23.099661+00:00_

Web search results for query: "CoRL 2026 reviewer guidelines review form criteria"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CVPR 2026 Reviewer Guidelines","url":"https://cvpr.thecvf.com/Conferences/2026/ReviewerGuidelinesq"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"2026 Reviewer Guidelines","url":"https://neurips.cc/Conferences/2026/ReviewerGuidelines"}]

Based on my search results, I found information about CoRL 2026, though the specific reviewer guidelines and review form criteria appear to be primarily available through the official conference websites. Here's what I found:

## CoRL 2026 Reviewer Requirements

All submissions must include at least one author who agrees to serve as a CoRL reviewer. They are qualified if they have at least one accepted publication at a previous robotics (CoRL/ICRA/IROS/RSS) or learning conference (ICLR/NeurIPS/ICML) or equivalent journal. Additionally, every author with 3 or more submissions must agree to serve as a reviewer.

## Related Review Information

While I found detailed reviewer guidelines from CoRL 2023 that may reflect similar criteria, the specific 2026 review form criteria don't appear to be fully detailed in the available search results. However, based on previous CoRL guidance, reviewers are asked to e
…[truncated 632 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7086
}
```

</details>

---


### Tool call

_source line 127 · 2026-05-18T01:50:29.404386+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl.org/contributions/instruction-for-authors",
  "prompt": "Extract all review criteria, review form dimensions, scoring scales, and reviewer guidelines for CoRL 2026. Include page limits, formatting requirements, and any mandatory sections."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl.org/contributions/instruction-for-authors",
    "prompt": "Extract all review criteria, review form dimensions, scoring scales, and reviewer guidelines for CoRL 2026. Include page limits, formatting requirements, and any mandatory sections."
  }
}
```

</details>

---


### Tool call

_source line 128 · 2026-05-18T01:50:30.811024+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2024.corl.org/contributions/instruction-for-reviews",
  "prompt": "Extract all review form dimensions, scoring scales (1-10, 1-5 etc.), criteria descriptions, and reviewer guidelines for CoRL. I need the complete review form structure including all questions reviewers must answer."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2024.corl.org/contributions/instruction-for-reviews",
    "prompt": "Extract all review form dimensions, scoring scales (1-10, 1-5 etc.), criteria descriptions, and reviewer guidelines for CoRL. I need the complete review form structure including all questions reviewers must answer."
  }
}
```

</details>

---


### Tool call

_source line 129 · 2026-05-18T01:50:31.213716+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 130 · 2026-05-18T01:50:31.670327+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 456
}
```

</details>

---


### Tool call

_source line 131 · 2026-05-18T01:50:31.721106+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 132 · 2026-05-18T01:50:32.175820+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 133 · 2026-05-18T01:50:32.178611+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 134 · 2026-05-18T01:50:32.631608+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 135 · 2026-05-18T01:50:32.632122+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 136 · 2026-05-18T01:50:33.185090+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 137 · 2026-05-18T01:50:33.185627+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 138 · 2026-05-18T01:50:33.587427+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 139 · 2026-05-18T01:50:33.587776+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 140 · 2026-05-18T01:50:34.140351+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 141 · 2026-05-18T01:50:34.140716+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 142 · 2026-05-18T01:50:34.643053+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 143 · 2026-05-18T01:50:34.643428+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 144 · 2026-05-18T01:50:34.694019+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 145 · 2026-05-18T01:50:35.097004+00:00_

# CoRL 2024 Review Form Structure

Based on the provided content, **the complete review form structure with specific scoring scales and detailed question dimensions is not included** in this document.

## What IS Provided:

The page outlines **review principles** rather than the actual form:

**Review Criteria:** Papers are assessed on "significance and novelty of the results, either theoretical or empirical" and "their potential for scientific and technological impact, as well as their relevance to robotic learning."

**Scope Requirements:** Submissions must demonstrate robot learning relevance through either:
- Intent: "Explicitly address a learning question for physical robots"
- Outcome: "Test the proposed learning solution on physical robots"

**Reviewer Qualifications:** Reviewers should demonstrate expertise with "a minimum of 3 first author publications in major robotics conferences and journals" plus relevant machine learning venue publications.

## Missing Information:

The document does **not** contain:
- Numbered scoring scales (1-10, 1-5, etc.)
- Specific review form questions
- Detailed evaluation dimensions
- Weighting systems for different criteria
- Answer format specifications

To obtain the actual review form, you would need to access CoRL's review submission platform or contact the organizing committee directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 4285
}
```

</details>

---


### Tool result

_source line 146 · 2026-05-18T01:50:35.197883+00:00_

# CoRL 2026 Review Criteria and Submission Guidelines

## Page Limits & Formatting

**Main Paper:**
- "8 pages for the main paper" for initial submission
- "9-page main text" for camera-ready versions
- Acknowledgments, references, and appendix do not count toward limits
- LaTeX template required (provided via Google Drive link)

## Mandatory Sections

- **Limitations Section**: Required, counted within the 8-page limit. Must describe "limiting assumptions, failure modes, and other limitations"
- **Anonymization**: Papers must be double-blind (de-anonymized after decisions)

## Submission Requirements

**Primary Materials:**
- Main PDF via OpenReview
- Optional supplementary file (single zip) containing further details
- Video submission encouraged: "not exceeding 250 MB" and "not more than 3 minutes"

**Additional Elements:**
- Reproducibility details encouraged in appendix
- Generative AI disclosure required during submission

## Reviewer Guidelines & Reciprocal Requirements

**Reviewer Obligations:**
- At least one qualified author must agree to review
- Qualified authors have prior publications at robotics (CoRL/ICRA/IROS/RSS) or learning conferences (ICLR/NeurIPS/ICML)
- Authors with 3+ submissions must review

## Review Process Notes

Papers receiving all "reject" reviews skip the rebuttal phase. Other authors may submit a 1-page rebuttal addressing factual errors only.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5793
}
```

</details>

---


### Tool call

_source line 147 · 2026-05-18T01:50:42.278435+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl2023.org/reviewer-guidelines",
  "prompt": "Extract the complete reviewer evaluation criteria, scoring scales (1-10 or similar), review form dimensions, and any specific questions reviewers must answer. I need the full review form structure."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl2023.org/reviewer-guidelines",
    "prompt": "Extract the complete reviewer evaluation criteria, scoring scales (1-10 or similar), review form dimensions, and any specific questions reviewers must answer. I need the full review form structure."
  }
}
```

</details>

---


### Tool call

_source line 148 · 2026-05-18T01:50:42.781263+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2025 2026 OpenReview review form scoring scale soundness significance novelty"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2025 2026 OpenReview review form scoring scale soundness significance novelty"
  }
}
```

</details>

---


### Tool result

_source line 149 · 2026-05-18T01:50:47.516573+00:00_

Web search results for query: "CoRL 2025 2026 OpenReview review form scoring scale soundness significance novelty"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"Paper Copilot: Tracking the Evolution of Peer Review in AI Conferences","url":"https://arxiv.org/html/2510.13201v1"},{"title":"CoRL 2025 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2025"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CoRL 2025 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2025%2FConference"},{"title":"CoRL | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL"},{"title":"CoRL 2025 Conference Submissions","url":"https://openreview.net/submissions?venue=robot-learning.org%2FCoRL%2F2025%2FConference"},{"title":"CoRL 2026 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2026"},{"title":"CoRL 2025 Workshop H2R | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2025%2FWorkshop%2FH2R"}]

Based on the search results, I found information about CoRL 2025 and CoRL 2026, but the search results don't contain specific information about the OpenReview review form scoring scale for soundness, significance, and novelty dimensions.

The search results show:

- CoRL 2025 and 2026 do use OpenReview for submissions and reviews
- General information about CoRL 2026 author instructions and submission requirements

However, the specific details about the review form scoring scale for dimensions like soundness, significance, and novelty are not included in these results. To get this information, you would likely need to:

1. Visit the CoRL 2025 or 2026 OpenReview page directly at:
   - CoRL 2025: https://openreview.net/group?id=robot-learning.org/
…[truncated 513 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 4735
}
```

</details>

---


### Tool result

_source line 150 · 2026-05-18T01:50:49.374040+00:00_

# CoRL 2023 Reviewer Evaluation Criteria

Based on the provided guidelines, CoRL 2023 specifies six primary evaluation dimensions for reviewers:

## Core Evaluation Dimensions

1. **Originality**: "Are the problems or methods new?" Assess novelty and how work differentiates from prior contributions.

2. **Quality**: Evaluate technical soundness, claim support through analysis/experiments, and methodological appropriateness.

3. **Clarity**: Judge writing quality, organization, and whether readers can reproduce results based on information provided.

4. **Significance**: Determine if results advance the state of the art and whether the community will build upon them.

5. **Relevance**: Confirm the paper addresses robot learning problems and applies learning-based methods, assessed in simulation or real robots.

6. **Limitations**: Appreciate honestly reported limitations while noting unreported flaws or shortcomings.

## Review Form Structure

The guidelines indicate a two-part review format:

- **Summary section**: Restate contributions in reviewers' own words
- **Main review section**: Address the six dimensions above with constructive, concrete feedback

## Scoring Scale

The document does not explicitly specify numerical scoring scales (e.g., 1-10 ratings). It emphasizes providing substantiated, constructive feedback rather than detailing a particular scoring rubric.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7095
}
```

</details>

---


### Tool call

_source line 151 · 2026-05-18T01:50:55.248307+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://openreview.net/group?id=robot-learning.org/CoRL/2025/Conference",
  "prompt": "Extract the review form details including scoring scales, evaluation dimensions, and any review criteria for CoRL 2025. I need the specific scoring rubric (1-10 scale, etc.) and what dimensions reviewers score on."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://openreview.net/group?id=robot-learning.org/CoRL/2025/Conference",
    "prompt": "Extract the review form details including scoring scales, evaluation dimensions, and any review criteria for CoRL 2025. I need the specific scoring rubric (1-10 scale, etc.) and what dimensions reviewers score on."
  }
}
```

</details>

---


### Tool result

_source line 152 · 2026-05-18T01:50:57.861130+00:00_

I cannot extract the review form details you've requested from the provided content. The webpage excerpt shows only the OpenReview.net navigation menu and footer information—it does not contain any specific information about CoRL 2025's review form, scoring scales, evaluation dimensions, or review criteria.

To find this information, you would need to:
1. Navigate directly to the CoRL 2025 conference page on OpenReview
2. Look for a "Review Form" or "Author Instructions" section
3. Check the conference's official guidelines document

I can only provide information that's actually present in the source material provided.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 2612
}
```

</details>

---


### Tool call

_source line 153 · 2026-05-18T01:51:03.643111+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"CoRL\" OpenReview review form \"overall score\" \"1:\" \"10:\" confidence rating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"CoRL\" OpenReview review form \"overall score\" \"1:\" \"10:\" confidence rating"
  }
}
```

</details>

---


### Tool result

_source line 154 · 2026-05-18T01:51:09.570482+00:00_

Web search results for query: ""CoRL" OpenReview review form "overall score" "1:" "10:" confidence rating"

Links: [{"title":"Why are the \"rating\" and \"confidence\" fields in my PC Console wrong? | OpenReview","url":"https://docs.openreview.net/getting-started/frequently-asked-questions/why-are-the-rating-and-confidence-fields-in-my-pc-console-wrong"},{"title":"Default Review Form | OpenReview","url":"https://docs.openreview.net/reference/default-forms/default-review-form"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"CORL 2025 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/corl-statistics/corl-2025-statistics/"},{"title":"CoRL | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL"},{"title":"CORL 2024 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/corl-statistics/corl-2024-statistics/"},{"title":"Frequently Asked Questions","url":"https://corl2022.org/frequently-asked-questions/"},{"title":"Simple and Efficient Confidence Score for Grading Whole Slide Images | OpenReview","url":"https://openreview.net/forum?id=DA1hOTvcMWa"},{"title":"CoRL 2025 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/corl-paper-list/corl-2025-paper-list/"},{"title":"What Have We Learned from OpenReview?","url":"https://arxiv.org/pdf/2103.05885"}]

Based on the search results, I found information about OpenReview review forms and their rating/confidence scales:

The default OpenReview review form includes rating options ranging from 1 to 10, with 1 representing "Trivial or wrong" and 10 representing "Top 5% of accepted papers, seminal paper," along with confidence ratings on a 5-point scale where 5 means "The reviewer is absolutely certain that the evaluation is correct and very familiar with the relevant literature".

The search results confirm that OpenReview review form options follow the format "number: description", for 
…[truncated 516 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 5927
}
```

</details>

---


### Tool call

_source line 155 · 2026-05-18T01:51:14.391274+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://docs.openreview.net/reference/default-forms/default-review-form",
  "prompt": "Extract the complete default review form including all scoring scales, rating dimensions with their numerical scales and descriptions, and confidence levels. I need the full rubric with all score descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://docs.openreview.net/reference/default-forms/default-review-form",
    "prompt": "Extract the complete default review form including all scoring scales, rating dimensions with their numerical scales and descriptions, and confidence levels. I need the full rubric with all score descriptions."
  }
}
```

</details>

---


### Tool result

_source line 156 · 2026-05-18T01:51:17.956973+00:00_

# Default Review Form - Complete Rubric

## Form Fields and Structure

The default review form contains four required fields ordered as follows:

**1. Title** (0-500 characters)
Brief summary capturing the essence of the review.

**2. Review** (1-20,000 characters)
Detailed evaluation assessing quality, clarity, originality, and significance. Supports Markdown formatting and LaTeX formulas.

**3. Rating Scale** (10-point scale)
- **10**: "Top 5% of accepted papers, seminal paper"
- **9**: "Top 15% of accepted papers, strong accept"
- **8**: "Top 50% of accepted papers, clear accept"
- **7**: Good paper warranting acceptance
- **6**: Marginally above acceptance threshold
- **5**: Marginally below acceptance threshold
- **4**: "Ok but not good enough - rejection"
- **3**: Clear rejection
- **2**: Strong rejection
- **1**: Trivial or fundamentally flawed

**4. Confidence Level** (5-point scale)
- **5**: Absolutely certain with extensive relevant literature familiarity
- **4**: Confident but not absolutely certain of evaluation correctness
- **3**: Fairly confident in the evaluation
- **2**: Willing to defend evaluation despite potential misunderstanding
- **1**: Evaluation represents an educated estimate

Both API V2 and V1 formats support these identical dimensions with different structural implementations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 3565
}
```

</details>

---


### Tool call

_source line 157 · 2026-05-18T01:55:08.594905+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿意见 — 方法/实验严谨性\n\n**论文**: \"Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\"\n\n---\n\n## 总体评分\n**Overall**: 6/10 (Marginally above acceptance threshold)\n**Confidence**: 4/5 (Confident in evaluation)\n**一句话总结**: 实验框架系统性强，但 L1 ablation 的因果推断存在 per-head normalization 缺陷，削弱了核心贡献(ii)的支撑力度；probe overparameterization 的错误解读亦需修正。\n\n## 官方维度打分（基于 CoRL review form: Originality/Quality/Clarity/Significance/Relevance/Limitations）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 3/5 | Token-level分解框架对VLA领域有增量贡献，但C1(specialization)本质是架构必然结果，C3(inverted-U)metric-dependent |\n| Quality | 3/5 | 三条件控制设计合理，但ablation因果推断有缺陷(per-head normalization)，N/params解读错误 |\n| Clarity | 4/5 | 写作清晰，结构合理，metric divergence透明报告 |\n| Significance | 3/5 | 对VLA理解有帮助，但缺乏行为验证（无success rate），单模型限制泛化性 |\n| Relevance | 4/5 | 直接面向robot learning社区关心的VLA内部机制问题 |\n| Limitations | 4/5 | 诚实报告了scope限制和metric依赖性，但未报告ablation normalization问题 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] L1 Ablation 的 3.5× specificity claim 被 per-head normalization 严重削弱\n\n- 具体位置：Section 4.2 (experiments.tex lines 78-82)\n- 问题：Ablating 24 dominant heads → +0.059 R²; ablating 8 non-dominant heads (control) → +0.017。论文声称 \"3.5× smaller\" 证明 graded specificity。但 per-head 归一化后：dominant = 0.059/24 ≈ 0.00246/head，non-dominant = 0.017/8 ≈ 0.00213/head，差异仅 ~15%。若将 non-dominant per-head rate 外推到 24 heads，预期效果 = 24 × 0.00213 = 0.051，观测值 0.059，excess 仅 0.008（16% above generic head-removal baseline）。\n- 为什么影响接收：这是 contribution (ii) \"VLA fine-tuning front-loads instruction routing\" 的唯一因果证据。若不能排除 \"removing any 24 heads increases R²\" 的 null hypothesis，则 \"functional specialization\" claim 缺乏因果支撑。\n- 建议修改方向：(1) 报告 per-head normalized effect size；(2) 补充 random-subset ablation（随机采样 24/32 heads，重复 k 次）作为恰当的 null baseline；(3) 或将 claim 从 \"3.5× specificity\" 调整为更保守的表述。\n\n**N2** [critical] N/params ≈ 0.05 被错误解读为 \"ensuring adequate training signal\"\n\n- 具体位置：Section 4.1 (experiments.tex line 12)\n- 问题：MLP probe (4096→256→7) 约有 ~1.05M parameters，N=63,228。N/params ≈ 0.06 意味着数据量仅为参数数的 1/17——严重 overparameterization。Belinkov (2022) 明确指出过高容量 probe 可从任何表征中 decode 信息，降低 probe 结论的解释性。论文声称此 ratio \"ensuring adequate training signal\" 是错误的。\n- 为什么影响接收：(1) 表明作者可能误解 probe methodology 的 selectivity concern；(2) 影响所有 absolute R² 值的可信度。\n- 建议修改方向：(1) 承认 overparameterized，说明依赖 early stopping；(2) 补充 linear probe 或小容量 probe baseline；(3) 强调 comparative claims (trained vs. untrained Δ) 不受 absolute R² inflation 影响。\n\n---\n\n## Should-Fix 问题\n\n**W1** [warning] Pretrained Llama-2 condition 的 OOD confound 未讨论\n- 位置：Method Section 3.1\n- Llama-2 base 从未被训练处理 projected visual tokens，对其而言这是完全 OOD 输入。\"language pretraining seeds instruction-attending structure\" 的因果解读需弱化。\n\n**W2** [warning] Bootstrap CI 未报告具体数值\n- 位置：Table 5 (Appendix), main text experiments.tex line 119\n- RSA rise phase Δ=+0.017 的 CI 仅标 \"incl. 0\"，未给 [lower, upper]。核心 claims 应报告具体 CI bounds。\n\n**W3** [warning] Cross-benchmark 仅限 LIBERO suite 内部\n- LIBERO-Goal 和 LIBERO-Spatial 共享 simulator/objects/action space，非真正独立验证。\n\n**W4** [warning] 缺乏行为层面验证\n- 位置：Discussion lines 25-26\n- 无 policy rollout success rate 数据。对 CoRL 而言，representation→behavior 的连接是核心价值。\n\n---\n\n## 小问题\n\n- N/params 分子分母可能写反（或架构描述与数字矛盾）\n- Appendix A.6 single-seed analysis 支撑主文 capacity trade-off narrative，应补 3+ seeds\n- Belinkov (2022) 应在 Method 中引用以讨论 probe selectivity\n\n---\n\n## Round 4 Issue Status\n\n| Issue | Status | 证据 |\n|-------|--------|------|\n| R4-N1: C1 reframe | RESOLVED | Abstract+Intro 已改为 \"verify and quantify architecture-expected\" |\n| R4-N2: RSA+CKA divergence | RESOLVED | Abstract/Intro/Method/Appendix 均有 metric-dependent qualifier |\n| R4-N3: 5→50 demos | RESOLVED | 明确写 \"50 demonstrations per task (N=63,228)\" |\n| R4-W2: FDR correction | RESOLVED | \"survive FDR correction at 29-30 of 33 layers (Benjamini-Hochberg)\" |\n| R4-W3: Probe N/capacity | PARTIALLY_RESOLVED | 数字已报告但解读错误 |\n\n---\n\n## Questions for Authors\n\n1. 能否提供 random-subset ablation (随机抽 24 heads ablated, 重复 k 次) 的 R² 变化分布？这能明确 dominant-head specificity 的真实 excess。\n2. 是否尝试过 smaller probes (4096→32→7 或 linear)？如果也能 reproduce inverted-U 和 Δ，则大幅增强可信度。\n3. Pretrained Llama-2 处理 OOD visual tokens 时，intermediate activations 是否在 reasonable range？\n4. 是否有任何 policy rollout 数据（即使 5-10 episodes）？\n\n---\n\n## 主要优势\n\n- 系统性四分析方法 + 三条件控制构成完整方法学模板\n- RSA vs CKA divergence 的透明报告体现科学诚信\n- Robustness analyses 覆盖充分（distance metric, per-DOF, permutation, seeds, demo subsample, threshold）\n- 三条件 gradient 设计优雅（attention routing 在三条件间单调递增）\n- Round 4 issues 的 reframing 恰当到位",
  "reviewer_id": "1",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿意见 — 方法/实验严谨性\n\n**论文**: \"Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\"\n\n---\n\n## 总体评分\n**Overall**: 6/10 (Marginally above acceptance threshold)\n**Confidence**: 4/5 (Confident in evaluation)\n**一句话总结**: 实验框架系统性强，但 L1 ablation 的因果推断存在 per-head normalization 缺陷，削弱了核心贡献(ii)的支撑力度；probe overparameterization 的错误解读亦需修正。\n\n## 官方维度打分（基于 CoRL review form: Originality/Quality/Clarity/Significance/Relevance/Limitations）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 3/5 | Token-level分解框架对VLA领域有增量贡献，但C1(specialization)本质是架构必然结果，C3(inverted-U)metric-dependent |\n| Quality | 3/5 | 三条件控制设计合理，但ablation因果推断有缺陷(per-head normalization)，N/params解读错误 |\n| Clarity | 4/5 | 写作清晰，结构合理，metric divergence透明报告 |\n| Significance | 3/5 | 对VLA理解有帮助，但缺乏行为验证（无success rate），单模型限制泛化性 |\n| Relevance | 4/5 | 直接面向robot learning社区关心的VLA内部机制问题 |\n| Limitations | 4/5 | 诚实报告了scope限制和metric依赖性，但未报告ablation normalization问题 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] L1 Ablation 的 3.5× specificity claim 被 per-head normalization 严重削弱\n\n- 具体位置：Section 4.2 (experiments.tex lines 78-82)\n- 问题：Ablating 24 dominant heads → +0.059 R²; ablating 8 non-dominant heads (control) → +0.017。论文声称 \"3.5× smaller\" 证明 graded specificity。但 per-head 归一化后：dominant = 0.059/24 ≈ 0.00246/head，non-dominant = 0.017/8 ≈ 0.00213/head，差异仅 ~15%。若将 non-dominant per-head rate 外推到 24 heads，预期效果 = 24 × 0.00213 = 0.051，观测值 0.059，excess 仅 0.008（16% above generic head-removal baseline）。\n- 为什么影响接收：这是 contribution (ii) \"VLA fine-tuning front-loads instruction routing\" 的唯一因果证据。若不能排除 \"removing any 24 heads increases R²\" 的 null hypothesis，则 \"functional specialization\" claim 缺乏因果支撑。\n- 建议修改方向：(1) 报告 per-head normalized effect size；(2) 补充 random-subset ablation（随机采样 24/32 heads，重复 k 次）作为恰当的 null baseline；(3) 或将 claim 从 \"3.5× specificity\" 调整为更保守的表述。\n\n**N2** [critical] N/params ≈ 0.05 被错误解读为 \"ensuring adequate training signal\"\n\n- 具体位置：Section 4.1 (experiments.tex line 12)\n- 问题：MLP probe (4096→256→7) 约有 ~1.05M parameters，N=63,228。N/params ≈ 0.06 意味着数据量仅为参数数的 1/17——严重 overparameterization。Belinkov (2022) 明确指出过高容量 probe 可从任何表征中 decode 信息，降低 probe 结论的解释性。论文声称此 ratio \"ensuring adequate training signal\" 是错误的。\n- 为什么影响接收：(1) 表明作者可能误解 probe methodology 的 selectivity concern；(2) 影响所有 absolute R² 值的可信度。\n- 建议修改方向：(1) 承认 overparameterized，说明依赖 early stopping；(2) 补充 linear probe 或小容量 probe baseline；(3) 强调 comparative claims (trained vs. untrained Δ) 不受 absolute R² inflation 影响。\n\n---\n\n## Should-Fix 问题\n\n**W1** [warning] Pretrained Llama-2 condition 的 OOD confound 未讨论\n- 位置：Method Section 3.1\n- Llama-2 base 从未被训练处理 projected visual tokens，对其而言这是完全 OOD 输入。\"language pretraining seeds instruction-attending structure\" 的因果解读需弱化。\n\n**W2** [warning] Bootstrap CI 未报告具体数值\n- 位置：Table 5 (Appendix), main text experiments.tex line 119\n- RSA rise phase Δ=+0.017 的 CI 仅标 \"incl. 0\"，未给 [lower, upper]。核心 claims 应报告具体 CI bounds。\n\n**W3** [warning] Cross-benchmark 仅限 LIBERO suite 内部\n- LIBERO-Goal 和 LIBERO-Spatial 共享 simulator/objects/action space，非真正独立验证。\n\n**W4** [warning] 缺乏行为层面验证\n- 位置：Discussion lines 25-26\n- 无 policy rollout success rate 数据。对 CoRL 而言，representation→behavior 的连接是核心价值。\n\n---\n\n## 小问题\n\n- N/params 分子分母可能写反（或架构描述与数字矛盾）\n- Appendix A.6 single-seed analysis 支撑主文 capacity trade-off narrative，应补 3+ seeds\n- Belinkov (2022) 应在 Method 中引用以讨论 probe selectivity\n\n---\n\n## Round 4 Issue Status\n\n| Issue | Status | 证据 |\n|-------|--------|------|\n| R4-N1: C1 reframe | RESOLVED | Abstract+Intro 已改为 \"verify and quantify architecture-expected\" |\n| R4-N2: RSA+CKA divergence | RESOLVED | Abstract/Intro/Method/Appendix 均有 metric-dependent qualifier |\n| R4-N3: 5→50 demos | RESOLVED | 明确写 \"50 demonstrations per task (N=63,228)\" |\n| R4-W2: FDR correction | RESOLVED | \"survive FDR correction at 29-30 of 33 layers (Benjamini-Hochberg)\" |\n| R4-W3: Probe N/capacity | PARTIALLY_RESOLVED | 数字已报告但解读错误 |\n\n---\n\n## Questions for Authors\n\n1. 能否提供 random-subset ablation (随机抽 24 heads ablated, 重复 k 次) 的 R² 变化分布？这能明确 dominant-head specificity 的真实 excess。\n2. 是否尝试过 smaller probes (4096→32→7 或 linear)？如果也能 reproduce inverted-U 和 Δ，则大幅增强可信度。\n3. Pretrained Llama-2 处理 OOD visual tokens 时，intermediate activations 是否在 reasonable range？\n4. 是否有任何 policy rollout 数据（即使 5-10 episodes）？\n\n---\n\n## 主要优势\n\n- 系统性四分析方法 + 三条件控制构成完整方法学模板\n- RSA vs CKA divergence 的透明报告体现科学诚信\n- Robustness analyses 覆盖充分（distance metric, per-DOF, permutation, seeds, demo subsample, threshold）\n- 三条件 gradient 设计优雅（attention routing 在三条件间单调递增）\n- Round 4 issues 的 reframing 恰当到位",
    "reviewer_id": "1",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 158 · 2026-05-18T01:55:12.765122+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4170
}
```

</details>

---


### Assistant

_source line 159 · 2026-05-18T01:55:21.516705+00:00_

审稿完成。核心发现：

1. **N1 [critical]**: L1 ablation 的 "3.5× specificity" claim 在 per-head normalization 后仅剩 ~15% excess，因果推断被严重削弱
2. **N2 [critical]**: N/params ≈ 0.05 被错误地解读为 "adequate"，实际上 probe 严重 overparameterized（参数量是数据量 17 倍）
3. Round 4 的 5 个旧 issues 中 4 个 RESOLVED，1 个 PARTIALLY_RESOLVED（W3: 数字报告了但解读错误）

Overall score: 6/10，borderline above threshold。主要优势是系统性框架和透明的 metric divergence 报告；主要风险是 ablation 的因果推断力度不足以支撑 contribution (ii) 的 strength。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1"
}
```

</details>

---


## Round 8

## Round 8

4 recorded events


### User

_source line 160 · 2026-05-18T01:57:35.067911+00:00_

[Round 1 审稿请求]:
## 交叉分享 — Reviewer 2 的完整审稿意见

请逐条回应以下 Reviewer 2 的意见。对每条使用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

以下是 Reviewer 2 的完整审稿原文：

### Must-Fix (Critical)

**R2-N1** [critical] 单模型局限性对 C2 generalizability 的根本约束
- C2（entry-exit routing pattern）仅在 OpenVLA-7B 一个模型上验证
- Discussion 以架构相似性类推（RT-2, π₀），但类推不等于验证：RT-2 用 PaLM-E backbone，π₀ 用 flow matching 非 autoregressive
- Grant et al. 2026 在 6 个 VLAs 上分析，表明 cross-model 验证可行
- 建议：Limitations 中具体列举哪些架构变量可能改变 routing pattern

**R2-N2** [critical] Discussion "Architectural implications" 段的 speculative leap
- 从 L1 ablation 的 representational effect 直接推导 design implication："adapting instruction-following behavior may require updating only early-layer attention parameters"
- 两个 gap：(1) probe R² ≠ behavioral performance；(2) L31 也有 18 heads instruction-dominant，说明 deep layers 也参与
- 建议：弱化措辞 + 标注 speculative + 指出 L31 complication

### Should-Fix (Warning)

**R2-W1** C1 contribution 定位仍有模糊：contributions (i) 混合框架贡献和验证结果，"验证预期结果"作为独立 contribution 说服力有限
**R2-W2** C3 non-monotonic observation 在 Abstract/Intro 获得与 C1/C2 等量篇幅，但 metric-dependent evidence 不支撑这个权重
**R2-W3** Related Work 缺少 causal tracing / activation patching 文献（Meng et al. 2022, Goldowsky-Dill et al. 2023）
**R2-W4** Related Work 缺少 tuned lens（Belrose et al. 2023），与 per-layer probing 方法论紧密相关
**R2-W5** conclusion.tex 存在但未被 main.tex \input（R4-I1 NOT_RESOLVED）

### Info

**R2-I1** Abstract 词数偏高（~241 words）
**R2-I2** -ing 分词短语约 15+ 处
**R2-I3** References 29 篇处于 CoRL 中等偏低

### R2 评分
- Overall: 6/10
- Originality: 6/10, Quality: 7/10, Clarity: 8/10, Significance: 5/10, Relevance: 8/10, Limitations: 7/10

请逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 161 · 2026-05-18T01:59:21.866105+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 意见的交叉回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-N1**: 单模型局限性。同意类推不等于验证（RT-2 用 PaLM-E, π₀ 用 flow matching）。但 contribution claim 已限定 \"demonstrated on OpenVLA-7B/LIBERO\" (Intro line 23)，我倾向将此降为 strong warning 而非 critical。建议 Limitations 应具体列举可能改变 routing 的架构变量（token ordering, decoder type, backbone scale, projector arch）。\n\n**[AGREE] R2-N2**: Architectural implications speculative leap。完全同意。probe R² ≠ behavioral performance，且 L31 的 18 heads (Fig 1, experiments.tex line 69) 直接矛盾 \"only early-layer\" 的暗示。应标注 speculative + 讨论 L31 complication。\n\n### Should-Fix\n\n**[REBUT] R2-W1**: C1 contribution 定位。部分不同意——experimental framework 本身（四方法 × 三条件 × 两 token × 32层 grid）有独立方法学贡献，prior work 均未做此 systematic verification。但同意\"混合框架和验证\"的措辞可改进。\n\n**[AGREE] R2-W2**: C3 权重过高。RSA inverted-U 在 CKA 下不成立 (Appendix A.2)，不应与 C2（跨 threshold/条件一致）等权呈现。\n\n**[AGREE] R2-W3/W4**: 缺 causal tracing + tuned lens。均为 Related Work 的实质 gap。\n\n**[AGREE] R2-W5**: conclusion.tex 遗漏。低严重性，Discussion 已覆盖。\n\n### Info\n\n**[AGREE] R2-I1/I2**: 非关键。\n**[REBUT] R2-I3**: 29 篇数量本身不是问题，实际 gap 是 W3/W4 指出的具体文献缺失（补充后 ~31-33 篇，合理）。\n\n### 与 R2 的关键分歧\n\n1. R2 给 Quality 7/10，我给 3/5。我认为 ablation per-head normalization 问题（我的 N1）比 R2 的评估更严重——3.5× claim 归一化后仅 ~15% excess，这是 C2 因果证据的核心缺陷。R2 似乎未注意到此问题。\n2. R2 将单模型定为 critical，我倾向 strong warning（scope 已限定）。但这取决于 AC 是否认为 CoRL 期望 cross-model validation。\n\n### 综合判断\n\n两位 reviewer 均给 6/10，核心担忧不同但互补：R2 关注 generalizability + speculation，我关注 statistical validity + causal inference。若两组 critical issues 都需 must-fix，论文工作量较大但不是不可能（random ablation baseline + framing 修正 + Limitations 扩展）。",
  "reviewer_id": "1",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 意见的交叉回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-N1**: 单模型局限性。同意类推不等于验证（RT-2 用 PaLM-E, π₀ 用 flow matching）。但 contribution claim 已限定 \"demonstrated on OpenVLA-7B/LIBERO\" (Intro line 23)，我倾向将此降为 strong warning 而非 critical。建议 Limitations 应具体列举可能改变 routing 的架构变量（token ordering, decoder type, backbone scale, projector arch）。\n\n**[AGREE] R2-N2**: Architectural implications speculative leap。完全同意。probe R² ≠ behavioral performance，且 L31 的 18 heads (Fig 1, experiments.tex line 69) 直接矛盾 \"only early-layer\" 的暗示。应标注 speculative + 讨论 L31 complication。\n\n### Should-Fix\n\n**[REBUT] R2-W1**: C1 contribution 定位。部分不同意——experimental framework 本身（四方法 × 三条件 × 两 token × 32层 grid）有独立方法学贡献，prior work 均未做此 systematic verification。但同意\"混合框架和验证\"的措辞可改进。\n\n**[AGREE] R2-W2**: C3 权重过高。RSA inverted-U 在 CKA 下不成立 (Appendix A.2)，不应与 C2（跨 threshold/条件一致）等权呈现。\n\n**[AGREE] R2-W3/W4**: 缺 causal tracing + tuned lens。均为 Related Work 的实质 gap。\n\n**[AGREE] R2-W5**: conclusion.tex 遗漏。低严重性，Discussion 已覆盖。\n\n### Info\n\n**[AGREE] R2-I1/I2**: 非关键。\n**[REBUT] R2-I3**: 29 篇数量本身不是问题，实际 gap 是 W3/W4 指出的具体文献缺失（补充后 ~31-33 篇，合理）。\n\n### 与 R2 的关键分歧\n\n1. R2 给 Quality 7/10，我给 3/5。我认为 ablation per-head normalization 问题（我的 N1）比 R2 的评估更严重——3.5× claim 归一化后仅 ~15% excess，这是 C2 因果证据的核心缺陷。R2 似乎未注意到此问题。\n2. R2 将单模型定为 critical，我倾向 strong warning（scope 已限定）。但这取决于 AC 是否认为 CoRL 期望 cross-model validation。\n\n### 综合判断\n\n两位 reviewer 均给 6/10，核心担忧不同但互补：R2 关注 generalizability + speculation，我关注 statistical validity + causal inference。若两组 critical issues 都需 must-fix，论文工作量较大但不是不可能（random ablation baseline + framing 修正 + Limitations 扩展）。",
    "reviewer_id": "1",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 162 · 2026-05-18T01:59:25.882885+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4016
}
```

</details>

---


### Assistant

_source line 163 · 2026-05-18T01:59:35.003651+00:00_

交叉回应已提交。

核心判断：与 R2 一致程度高（7/10 条 AGREE），主要分歧在 C1 框架贡献的独立价值（我认为 R2 低估）和引用数量问题（gap 比数量重要）。两人均给 6/10 但关注点互补——R2 侧重 generalizability，我侧重 statistical/causal rigor。最大的未被 R2 发现的问题是 ablation per-head normalization（我的 N1）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1"
}
```

</details>

---


## Round 9

## Round 9

46 recorded events


### User

_source line 164 · 2026-05-18T08:52:26.190254+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1

### 你的审查侧重：方法严谨性 + 实验设计

### 论文信息
- **标题**: Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model
- **论文文件**: `projects/vla-ssd/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, appendix.tex）
- **目标 venue**: CoRL 2026
- **Deadline**: Abstract May 26, Paper May 29, 2026

### CoRL 2026 格式要求
- 正文 8 页 + 无限参考文献（初始提交）
- 必须包含 Limitations section（计入 8 页限制）
- Double-blind 匿名审稿
- 模板: `corl_2026` 样式包
- 需要 Generative AI 使用声明
- 鼓励提交 video/code/data 补充材料

### 你需要重点评估的方面

1. **Probing 方法论**：
   - Cross-instruction probe（10-way classification）的设计是否合理？是否存在 trivially easy 的问题？
   - MLP probe vs linear probe 的 capacity 控制是否充分？
   - Probe 的 train/test split 是否存在信息泄漏风险？

2. **统计检验**：
   - RSA、R²、attention 分析的统计显著性检验是否恰当？
   - 多重比较校正（FDR）是否正确应用？
   - 效应量报告是否充分？置信区间是否合理？

3. **Ablation 设计**：
   - L1 head ablation 的因果推断是否有效？
   - 样本量（N）、demo 数量是否充分？
   - 控制条件（control8, all32）是否能排除混淆因素？

4. **Baseline 充分性**：
   - 三条件对照（untrained / Llama-2 base / trained）是否能支撑 claims？
   - 是否缺少关键 baseline（如其他 VLA 架构、其他 probe 方法）？
   - RSA 与 CKA metric 分歧的处理是否恰当？

5. **因果 vs 相关**：
   - 每个 claim 的证据链是否支撑其因果强度？
   - 是否存在 overclaim（相关性证据声称因果性）？

请通读全文（含附录），按以下格式输出审稿意见：

```
## Summary (2-3 sentences)

## Strengths
- S1: ...
- S2: ...

## Weaknesses (按严重程度排序: [CRITICAL] / [WARNING] / [INFO])
- W1 [CRITICAL]: ...
- W2 [WARNING]: ...

## Questions for Authors
- Q1: ...

## Missing References

## Overall Assessment
Score: {strong reject / weak reject / borderline / weak accept / strong accept}
Confidence: {low / medium / high}

## Detailed Comments (逐节)
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 165 · 2026-05-18T08:52:38.722399+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 166 · 2026-05-18T08:52:40.379404+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/sessions/review_reviewer_1_458aa27f.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1657
}
```

</details>

---


### Tool call

_source line 167 · 2026-05-18T08:52:40.379762+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
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

_source line 168 · 2026-05-18T08:52:40.430223+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 169 · 2026-05-18T08:52:44.598945+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 170 · 2026-05-18T08:52:46.465110+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/vla-ssd/docs/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/vla-ssd/docs/paper/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15"
  }
}
```

</details>

---


### Tool result

_source line 171 · 2026-05-18T08:52:46.515812+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 172 · 2026-05-18T08:52:52.599085+00:00_

Web search results for query: "CoRL 2026 reviewer guidelines review form criteria"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CVPR 2026 Reviewer Guidelines","url":"https://cvpr.thecvf.com/Conferences/2026/ReviewerGuidelinesq"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"2026 Reviewer Guidelines","url":"https://neurips.cc/Conferences/2026/ReviewerGuidelines"}]

Based on the search results, I found information about CoRL 2026, though the most specific reviewer guidelines and review form criteria I found were from CoRL 2023 and 2024. Here's what I discovered:

## CoRL 2026 Reviewer Requirements

All submissions must include at least one author who agrees to serve as a CoRL reviewer. They are qualified if they have at least one accepted publication at a previous robotics (CoRL/ ICRA/ IROS/ RSS) or learning conference (ICLR/ NeurIPS/ ICML) or equivalent journal.

## Review Criteria (Based on CoRL 2024)

While specific CoRL 2026 review form criteria weren't fully detailed in the results, here are the review criteria from CoRL 2024:

Submissions will be evaluated based on the significance and novelty of the results, either theoretical or empirical.

For CoRL 2023, reviewers were expected to evaluate papers on:

- Relevance: Does the paper address a problem in robo
…[truncated 834 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8000
}
```

</details>

---


### Tool call

_source line 173 · 2026-05-18T08:52:57.019130+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 174 · 2026-05-18T08:52:57.471093+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_example.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 175 · 2026-05-18T08:52:58.878291+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2024.corl.org/contributions/instruction-for-reviews",
  "prompt": "Extract the complete reviewer guidelines, review form criteria, scoring dimensions, and rating scales. List every dimension reviewers are asked to score, with the scale for each."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2024.corl.org/contributions/instruction-for-reviews",
    "prompt": "Extract the complete reviewer guidelines, review form criteria, scoring dimensions, and rating scales. List every dimension reviewers are asked to score, with the scale for each."
  }
}
```

</details>

---


### Tool call

_source line 176 · 2026-05-18T08:52:59.835234+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl.org/contributions/instruction-for-authors",
  "prompt": "Extract all submission requirements, page limits, formatting rules, required sections, and any reviewer-relevant criteria mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl.org/contributions/instruction-for-authors",
    "prompt": "Extract all submission requirements, page limits, formatting rules, required sections, and any reviewer-relevant criteria mentioned."
  }
}
```

</details>

---


### Tool result

_source line 177 · 2026-05-18T08:53:03.209134+00:00_

# CoRL 2024 Reviewer Guidelines Summary

Based on the provided content, here are the key reviewer guidelines:

## Review Criteria
Reviewers evaluate submissions on:
- "Significance and novelty of the results, either theoretical or empirical"
- Objective establishment of results and potential scientific/technological impact
- Relevance to robotic learning

## Desk Rejection Criteria
Papers may be rejected at desk stage for:
- **Formatting issues**: Exceeding length limits or incorrect format
- **Anonymity violations**: Author identification in manuscript, supplementary materials, or links
- **Scope failures**: Lacking demonstrated relevance to robot learning through either intent (explicitly addressing learning for physical robots) or outcome (testing on physical robots)

## Reviewer Qualifications
Reviewers should possess:
- "Expertise in robotics, robot learning, machine learning and complementary fields"
- Ideally, minimum of 3 first-author publications in major robotics venues (CoRL, RSS, ICRA, IROS, IJRR, TRO, RAL) and machine learning conferences (NeurIPS, ICML, AIStats, JMLR, PAMI)

## Scoring Dimensions
**Note**: The provided document does not include a detailed review form with specific scoring dimensions or numerical rating scales. Only the evaluation criteria and qualifications are specified.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 4330
}
```

</details>

---


### Tool result

_source line 178 · 2026-05-18T08:53:05.637040+00:00_

# CoRL 2026 Submission Requirements Summary

## Page Limits
- **Initial submission:** 8 pages maximum for main paper
- **Camera-ready:** 9 pages maximum for main paper
- Acknowledgments, references, and appendix do not count toward limits

## Required Formatting
- Must use provided LaTeX template
- Double-blind anonymization required for initial submission
- Footer on first page: "10th Conference on Robot Learning (CoRL 2026), Austin, Texas, USA."
- Standard margins and text density matching template specifications

## Mandatory Sections
- **Limitations section** (counted in 8-page limit): must explicitly describe "limiting assumptions, failure modes, and other limitations"
- Acknowledgments, references, and optional appendix

## Recommended Submissions
- Supplementary materials as single zip file via OpenReview
- Video submission (≤250 MB, ≤3 minutes suggested)

## Reviewer-Relevant Criteria
- At least one author must commit to reviewing, if qualified (prior publication at robotics/learning conferences)
- Authors with 3+ submissions must review
- Reciprocal reviewing requirement may trigger desk rejection if unmet
- Papers with all "reject" reviews skip rebuttal phase
- Fake citations result in automatic desk rejection

## Key Submission Constraints
- No dual submission to other archival venues without prior approval
- Generative AI use must be disclosed; LLMs cannot be listed as authors

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5801
}
```

</details>

---


### Tool call

_source line 179 · 2026-05-18T08:53:11.964209+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl2023.org/reviewer-guidelines",
  "prompt": "Extract the complete review form, all scoring dimensions, rating scales (numerical scales), and detailed criteria for each dimension. I need the exact review form fields and scales."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl2023.org/reviewer-guidelines",
    "prompt": "Extract the complete review form, all scoring dimensions, rating scales (numerical scales), and detailed criteria for each dimension. I need the exact review form fields and scales."
  }
}
```

</details>

---


### Tool call

_source line 180 · 2026-05-18T08:53:13.120009+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL OpenReview review form scoring dimensions \"overall score\" \"confidence\" rating scale robotics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL OpenReview review form scoring dimensions \"overall score\" \"confidence\" rating scale robotics"
  }
}
```

</details>

---


### Tool call

_source line 181 · 2026-05-18T08:53:13.120333+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 182 · 2026-05-18T08:53:13.172122+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 183 · 2026-05-18T08:53:17.239101+00:00_

# CoRL 2023 Review Form Analysis

Based on the provided content, I cannot extract a complete review form with specific rating scales because **the document does not include the actual numerical scoring dimensions or rating scales**.

## What the Guidelines Do Specify:

The guidelines outline **six evaluation dimensions** that reviewers should assess:

1. **Originality** - "Are the problems or methods new?" and how the work differs from prior contributions
2. **Quality** - Technical soundness and supporting evidence for claims
3. **Clarity** - Writing quality and organization
4. **Significance** - Importance and potential impact of results
5. **Relevance** - Connection to robot learning and CoRL's audience
6. **Limitations** - Assessment of authors' reported limitations

## Critical Gap:

The document states reviewers will evaluate these dimensions but does not provide:
- Specific numerical scales (e.g., 1-5, 1-10)
- Anchor descriptions for rating levels
- The actual review form template fields
- Score ranges or decision categories

The guidelines reference that "technical instructions" will be provided via OpenReview email, suggesting the detailed form and scales exist elsewhere in their submission system rather than in this public guideline document.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5274
}
```

</details>

---


### Tool result

_source line 184 · 2026-05-18T08:53:27.180234+00:00_

Web search results for query: "CoRL OpenReview review form scoring dimensions "overall score" "confidence" rating scale robotics"

Links: [{"title":"CoRL 2023 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2023%2FConference"},{"title":"Paper scoring through individual reviewer quality estimates for Open Peer Review","url":"https://arxiv.org/html/2501.13014"},{"title":"CONFIDENCE CALIBRATION IN VISION-LANGUAGE-ACTION ...","url":"https://openreview.net/pdf/527841d8920adc2a9d18b71659aa6ad7720a134c.pdf"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"CoRL | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL"},{"title":"CoRL 2024 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FConference"},{"title":"CoRL 2025 Workshop H2R | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2025%2FWorkshop%2FH2R"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2022 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2022%2FConference"}]

I found some results related to CoRL and review guidelines, but the search results don't specifically contain information about the OpenReview review form scoring dimensions with "overall score," "confidence," and rating scales. Let me search more specifically for the review form structure.

Links: [{"title":"Why are the \"rating\" and \"confidence\" fields in my PC Console wrong? | OpenReview","url":"https://docs.openreview.net/getting-started/frequently-asked-questions/why-are-the-rating-and-confidence-fields-in-my-pc-console-wrong"},{"title":"Default Review Form | OpenReview","url":"https://doc
…[truncated 3829 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 14060
}
```

</details>

---


### Tool call

_source line 185 · 2026-05-18T08:53:33.009204+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://docs.openreview.net/reference/default-forms/default-review-form",
  "prompt": "Extract the complete default review form fields, all scoring dimensions, and their rating scales (numerical values and descriptions). I need every field, its scale, and anchor descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://docs.openreview.net/reference/default-forms/default-review-form",
    "prompt": "Extract the complete default review form fields, all scoring dimensions, and their rating scales (numerical values and descriptions). I need every field, its scale, and anchor descriptions."
  }
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-18T08:53:35.333119+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 187 · 2026-05-18T08:53:35.333653+00:00_

1	Vision-language-action models (VLAs) fine-tune large language models (LLMs) on robot demonstrations, but how training reshapes information routing at the token level remains uncharacterized.
2	We present a systematic experimental framework for token-level analysis of VLAs, applying cross-instruction probes, attention analysis, Representational Similarity Analysis (RSA), and functional probes across all 32 LLM layers of OpenVLA-7B on LIBERO, with factorial trained/pretrained/untrained controls.
3	Three findings emerge.
4	First, we verify and quantify architecture-expected token specialization: image tokens are instruction-blind (classification at chance, $10\%$, across all layers and conditions), consistent with the causal mask and frozen encoder, while the readout token serves as the sole multimodal convergence point ($100\%$ instruction classification from L1, cross-validated).
5	Second, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth (L9--L16, 15--22 heads), while VLA training shifts this to entry-layer routing (L0--L1: 21--24 heads) with exit-layer re-engagement (L31: 18 heads); instruction classification reaches $99.6\%$ at L1 (vs.\ pretrained $80.2\%$), and L1 ablation reveals that instruction-dominant heads serve dual routing-encoding function (random-subset control, $z = -2.73$, L1-confined). Untrained models show zero instruction-dominant heads throughout.
6	Third, vision encoder representations follow a metric-dependent non-monotonic trajectory through LLM layers ($R^2$ peaks at L8--L14; RSA confirms but CKA diverges; Appendix).
7	Training effects concentrate at the readout token (probe $R^2$ $+0.069$, instruction attention $+46$pp) rather than visual geometry ($\Delta\rho \leq 0.017$, non-significant); instruction routing reorganization is the primary learned contribution of VLA fine-tuning.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 188 · 2026-05-18T08:53:35.835737+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 189 · 2026-05-18T08:53:36.338280+00:00_

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
…[truncated 2511 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 190 · 2026-05-18T08:53:36.338680+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 191 · 2026-05-18T08:53:36.597183+00:00_

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
…[truncated 4157 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 258
}
```

</details>

---


### Tool call

_source line 192 · 2026-05-18T08:53:36.597635+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 193 · 2026-05-18T08:53:36.655735+00:00_

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
12	This yields $N = 63{,}228$ observations (50 demonstrations $\times$ 10 tasks $\times$ $\sim$127 timesteps per demonstration). The MLP probe is overparameterized ($N/\text{params} \approx 0.06$); early stopping mitigates overfitting, and all patterns reproduce with a linear probe ($N/\text{params} \approx 2.2$; Appendix~\ref{sec:linear_probe}).
13	
14	%------------------------------------------------------------------
15	\subsection{Token-Level Functional Specialization}
16	\label{sec:token_specialization}
17	
18	We test whether image tokens and readout tokens encode different types of information by training cross-instruction probes (\S\ref{sec:cross_instruction_probes}): given the same visual frame paired with each of 10 task instructions, we classify which instruction was present from per-layer activations.
19	
20	\paragraph{Image tokens are in
…[truncated 11778 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 58
}
```

</details>

---


### Tool result

_source line 194 · 2026-05-18T08:53:36.838263+00:00_

# Default Review Form Fields and Scales

## Form Fields

**1. Title**
- Type: String (0-500 characters)
- Purpose: "Brief summary of your review"
- Order: 1

**2. Review**
- Type: String (1-20,000 characters)
- Input: Textarea with Markdown support
- Purpose: "evaluation of the quality, clarity, originality and significance"
- Order: 2

**3. Rating**
- Type: Integer (dropdown selection)
- Order: 3

**4. Confidence**
- Type: Integer (radio buttons)
- Order: 4

---

## Rating Scale (1-10)

| Value | Description |
|-------|-------------|
| 10 | "Top 5% of accepted papers, seminal paper" |
| 9 | "Top 15% of accepted papers, strong accept" |
| 8 | "Top 50% of accepted papers, clear accept" |
| 7 | "Good paper, accept" |
| 6 | "Marginally above acceptance threshold" |
| 5 | "Marginally below acceptance threshold" |
| 4 | "Ok but not good enough - rejection" |
| 3 | "Clear rejection" |
| 2 | "Strong rejection" |
| 1 | "Trivial or wrong" |

---

## Confidence Scale (1-5)

| Value | Description |
|-------|-------------|
| 5 | "absolutely certain that the evaluation is correct and very familiar" |
| 4 | "confident but not absolutely certain that the evaluation is correct" |
| 3 | "fairly confident that the evaluation is correct" |
| 2 | "willing to defend the evaluation, but quite likely didn't understand central parts" |
| 1 | "evaluation is an educated guess" |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 3829
}
```

</details>

---


### Tool call

_source line 195 · 2026-05-18T08:53:42.681076+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 196 · 2026-05-18T08:53:43.183515+00:00_

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
14	Meng et al.~\cite{meng2022_rome} developed causal tracing to locate factual associations in specific MLP layers, and Belrose et al.~\cite{belrose2023_tunedlens} introduced the tuned lens for tracking per-layer prediction evolution through learned projections.
15	In parallel, attention probing studies have shown that individual heads encode syntactic relations~\cite{clark2019}, capture positional and structural patterns at different depths~\cite{vig2019}, and that a small subset of specialized heads accounts for most model performance~\cite{voita2019}.
16	Our Layer-1 at
…[truncated 3059 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 197 · 2026-05-18T08:53:43.184339+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 198 · 2026-05-18T08:53:44.338888+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Synthesis.}
5	Image tokens remain instruction-blind (causal mask, frozen encoder); the readout is the sole convergence point.
6	Training shifts routing from mid-depth to entry-exit (L0--L1, L31), with effects at the readout ($R^2$ $+0.069$) rather than images ($\Delta \leq 1.7\%$).
7	
8	\paragraph{Mechanism-behavior connection.}
9	Image-token instruction-blindness explains the visual dominance reported by Grant et al.~\cite{grant2026}: actions rely on readout-token conditioning.
10	Under RSA, DINOv2 achieves the highest geometric alignment ($\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\ $0.634$). This gap points to instruction-conditioned integration rather than enhanced geometry.
11	
12	\paragraph{Speculative mechanistic interpretation.}
13	Per-layer RSA shows a bifurcation after L12 (Figure~\ref{fig:rsa_perlayer_curve}): readout $\rho$ declines gradually while image\_mean drops sharply ($\to 0.422$), consistent with mid-layer integration and deep-layer compression; testing this requires interventions beyond L1.
14	
15	\paragraph{Architectural implications.}
16	L1 attention ablation (\S\ref{sec:learned_routing}) reveals that instruction routing is functionally integrated with action encoding: instruction-dominant heads yield smaller $R^2$ changes than random subsets ($z = -2.73$), indicating dual function rather than capacity competition. The effect is L1-confined ($|\Delta R^2| < 0.02$ at deeper layers); routing concentration at L0--L1 suggests early-layer parameters may suffice for instruction adaptation, though behavioral validation is needed.
17	
18	\paragraph{Limitations and scope.}
19	We study OpenVLA-7B on LIBERO. OpenVLA shares the dominant VLA design (frozen encoder, MLP projector, autoregressive LLM) with RT-2~\cite{brohan2023_rt2} and $\pi_0$~\cite{black2024_pi0}; C1 follows from shared architectural constraints, but C2 may differ across backbone scales, de
…[truncated 445 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1154
}
```

</details>

---


### Tool call

_source line 199 · 2026-05-18T08:53:44.389764+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool call

_source line 200 · 2026-05-18T08:53:44.390215+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 201 · 2026-05-18T08:53:44.440674+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We decompose a VLA's internal representations with factorial trained-vs-untrained control, revealing: (1)~strict token-level specialization (instruction-blind image tokens, cross-validated readout hub); (2)~front-loaded instruction routing, shifted from mid-depth (L9--L16) to entry-exit (L0--L1, L31); and (3)~non-monotonic vision encoder refinement (peak L12, readout $R^2$ $+0.069$, image $\Delta \leq 1.7\%$).
5	Vision encoder quality emerges as a key design lever.
6	Code and representations will be released upon acceptance.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 202 · 2026-05-18T08:53:44.742437+00:00_

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
…[truncated 29108 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 203 · 2026-05-18T08:53:51.873148+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool call

_source line 204 · 2026-05-18T08:53:52.625749+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2024 2025 OpenReview review form \"overall recommendation\" \"soundness\" \"significance\" rating 1-10 scale robotics conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2024 2025 OpenReview review form \"overall recommendation\" \"soundness\" \"significance\" rating 1-10 scale robotics conference"
  }
}
```

</details>

---


### Tool result

_source line 205 · 2026-05-18T09:03:29.178228+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 42, \"total_citations\": 72, \"unique_cited_keys\": 42, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 32, \"online_not_found\": 4, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"kim2024_openvla\", \"type\": \"article\", \"title\": \"OpenVLA: An Open-Source Vision-Language-Action Model\", \"authors\": \"Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balak...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2406.09246\"}, {\"key\": \"karamcheti2024\", \"type\": \"article\", \"title\": \"Prismatic VLMs: Investigating the Design Space of Visually-Conditioned Language Models\", \"authors\": \"Karamcheti, Siddharth and Nair, Suraj and Balakrishna, Ashwin and Liang, Percy a...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2402.07865\"}, {\"key\": \"brohan2023_rt2\", \"type\": \"article\", \"title\": \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\", \"authors\": \"Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and C...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2307.15818\"}, {\"key\": \"liu2023_libero\", \"type\": \"inproceedings\", \"title\": \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\", \"authors\": \"Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"kriegeskorte2008\", \"type\": \"article\", \"title\": \"Representational Similarity Analysis -- Connecting the Branches of Systems Neuroscience\", \"authors\": \"Kriegeskorte, Nikolaus and Mur, Marieke and Bandettini, Peter\", \"year\": \"2008\", \"venue\": \"Frontiers in Systems Neuroscience\"}, {\"key\": \"korn
…[truncated 32408 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 577305
}
```

</details>

---


### Tool result

_source line 206 · 2026-05-18T09:03:35.000753+00:00_

Web search results for query: "CoRL 2024 2025 OpenReview review form "overall recommendation" "soundness" "significance" rating 1-10 scale robotics conference"

Links: [{"title":"CoRL | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"CoRL 2025 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2025%2FConference"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"CoRL 2024 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FConference"},{"title":"CoRL 2024 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2024"},{"title":"CoRL 2025 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2025"},{"title":"CoRL 2025 Demos | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2025%2FDemos"},{"title":"CoRL 2024 Conference Submissions | OpenReview","url":"https://openreview.net/submissions?venue=robot-learning.org/CoRL/2024/Conference"},{"title":"CoRL 2024 Workshop WCBM | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FWorkshop%2FWCBM"}]

Based on the search results, I found relevant information about CoRL review guidelines. The search results include links to the OpenReview pages for CoRL 2024 and 2025, as well as detailed reviewer guidelines information.

From the available information, here's what I found regarding the review form criteria:

The review form asks for an evaluation of the originality, quality, clarity, significance, relevance and limitations of the work. More specifically, reviewers are asked whether the submission is technically sound under the "Quality" criterion.

The search results show that submissions will be evaluated based on the significan
…[truncated 737 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 582375
}
```

</details>

---


### Tool call

_source line 207 · 2026-05-18T09:07:39.051097+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 — Round 1 Review\n\n**Paper**: \"Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\"\n**Target Venue**: CoRL 2026\n**审查侧重**: 方法严谨性 + 实验设计\n\n---\n\n## Summary (2-3 sentences)\n\n本文对 OpenVLA-7B 在 LIBERO 上进行了 per-layer、per-token-type 的表征分析，使用 cross-instruction probes、attention pattern analysis、RSA 和 functional probes，配合 trained/pretrained/untrained 三条件对照。核心发现是：(1) image token 对 instruction 不敏感（架构必然）；(2) VLA 训练将 instruction routing 从中层移至 entry-exit 层；(3) vision encoder 表征经 LLM 层呈 inverted-U 变换。这是一篇分析型论文，方法论工作扎实但存在若干统计推断和因果推断层面的问题。\n\n---\n\n## Strengths\n\n- **S1: 系统性的实验框架设计。** 三条件因子控制（VLA-trained / Llama-2 base / untrained）× 指令有无的 2×2 factorial 设计是合理的。与大多数 VLA 分析工作相比，这种控制更完整，可以隔离语言预训练和 VLA fine-tuning 各自的贡献（Section 3.1）。\n\n- **S2: 多角度互验。** RSA（几何对齐）+ functional probes（可解码性）+ attention analysis（机制）+ cross-instruction probes（信息内容）四种互补工具的组合使用是方法论上的优势。Linear probe 复制（Appendix A.6）进一步增强了 functional probe 结论的可信度。\n\n- **S3: 丰富的 robustness 分析。** 附录中的 distance metric invariance（Table A.5）、demonstration subsampling（Table A.7）、seed sensitivity（Table A.6）、threshold sensitivity（Table A.10）、cross-benchmark validation（LIBERO-Spatial, Appendix A.4）显示作者认真检验了结论的鲁棒性。\n\n- **S4: 对 CKA 分歧的诚实处理。** 多数论文会回避不利结果。作者坦承 linear CKA 完全反转了 RSA 排序（Appendix A.2, Figure A.1），并提供了合理（虽然不完全令人信服）的解释。\n\n- **S5: 与 behavioral 文献的连接。** 将 image-token instruction-blindness 与 Grant et al. [2026] 和 Häon et al. [2025] 发现的 visual dominance 建立联系（Discussion），帮助读者理解分析发现的实际意义。\n\n---\n\n## Weaknesses (按严重程度排序)\n\n### W1 [CRITICAL]: Cross-instruction probe（Finding 1）近乎 trivially easy，削弱了核心贡献的新颖性\n\n**位置**: Section 4.2, Table 1\n\n**问题**: 10-way cross-instruction classification 在 readout token 位置上，ALL THREE 条件（trained, pretrained, untrained）在 L1 均达到 99.6-100%。作者自己在 Appendix A.8.1 承认 \"even incidental attention (~12%) suffices for linear classification at L1\"。这意味着只要有任何 attention 到 instruction tokens——哪怕是随机初始化权重产生的微弱 attention——probe 就能轻松区分 10 条差异很大的 LIBERO 指令。\n\n10 条 LIBERO-Goal 指令（如 \"pick up the red cup\" vs \"push the blue block\"）在 token 层面差异巨大。一个 linear classifier 只需检测到 instruction embedding 的最微小残留即可达到 100%。这不是关于 VLA 如何处理指令信息的深层洞察，而是 tokenizer + 单层 attention 的 trivial 后果。\n\n更有信息量的比较是 DECAY PATTERN（untrained 从 100% 降至 82%，trained 维持 100%），但论文将 \"100% from L1\" 作为主要发现来呈现，而非衰减差异。\n\n**为什么影响接收**: Finding 1（token-level functional specialization）是三个核心贡献之一。如果它大部分由架构约束直接推出（causal mask → image tokens blind，tokenizer + any attention → readout trivially classifiable），那么作为 \"contribution\" 的增量价值大幅降低。\n\n**建议**: (a) 增加更难的 probe task（如语义近似但不同的指令，或 paraphrase 指令）以测试真正的指令理解 vs. 表面 token 检测；(b) 重新 framing Finding 1 为 \"验证架构预期\" 而非 \"发现\"，论文部分已做但不够彻底。\n\n---\n\n### W2 [CRITICAL]: L1 head ablation 的因果推断方向存在根本性问题\n\n**位置**: Section 4.3, Appendix A.4\n\n**问题**: Ablating 24/32 dominant heads at L1 increases action R² by +0.042（baseline 0.517）。Random 24-head ablation increases by +0.077。作者解释为 dominant heads 具有 \"dual routing-encoding function\"。\n\n但基本事实是：ablating ANY 24 out of 32 heads (75%) at L1 IMPROVES action prediction。无论是 dominant heads 还是 random heads，移除都提高 R²。这意味着 L1 的大多数 heads 对 action prediction 是 net-negative 的。如果研究者声称 L1 的 instruction-dominant heads 具有功能性重要作用，那么 ablation 应该 DECREASE R²（性能变差），而非 increase。\n\n论文的 \"dual function\" 解释是一种 post-hoc rationalization：dominant heads 虽然 R² 增幅小于 random heads，但两者都是正增幅。等效的替代解释是：L1 heads 普遍对 action probe 添加噪声，dominant heads 因为 attention pattern 更结构化所以噪声更少。这不需要 \"dual function\" 假设。\n\n此外，random-subset 只用了 N=10 个子集（C(32,24) = 10,518,300 种可能），z-test 的统计检验力极低且分布假设可疑。\n\n**为什么影响接收**: L1 ablation 是论文中唯一的因果证据（区别于纯相关性分析）。如果因果推断不成立，Finding 2 的证据链从 \"相关+因果\" 降级为 \"仅相关\"。\n\n**建议**: (a) 增加更细粒度的 ablation（如 ablate 4/8/12/16/20/24/28 heads，观察 R² 变化曲线）；(b) 尝试 SELECTIVE ablation（只 ablate dominant heads 的 instruction attention，保留 image attention），这能更精确地测试 \"dual function\" 假设；(c) 大幅增加 random subsets 数量（≥100）；(d) 修改 framing 以反映实际发现（所有 ablation 都提高 R²）。\n\n---\n\n### W3 [CRITICAL]: Action probe 的 train/test split 未明确说明，overparameterized MLP probe 的 R² 可信度存疑\n\n**位置**: Section 3.6, Section 4.1\n\n**问题**: MLP probe 的 N/params ≈ 0.06（作者自认 \"overparameterized\"）。论文称 \"early stopping mitigates overfitting\"，但：\n\n(a) R² 是在哪个数据集上计算的？论文未明确说明 train/test/validation split。如果 R² 是 training data 上的值，那么 overparameterized model 可以达到任意高的 R²，所有结论无效。如果是 validation set（early stopping 的依据），那么 R² 也可能被 early stopping 的选择偏倚。\n\n(b) Linear probe 复制（Appendix A.6）显示 trained-untrained gap 在 linear probe 下为 Δ = +0.324（L14），在 MLP probe 下仅为 Δ = +0.015（L8），相差 ~20 倍。这暗示 MLP probe 过于强大，rescues 了 untrained representations 的信息，压缩了条件间差异。这意味着 MLP probe R² 的绝对值和条件间差异都可能是 misleading 的。\n\n(c) N=63,228 observations 但时间步之间高度自相关（连续 frames of same demo），有效样本量远小于名义值。Bootstrap CI 基于独立重抽样假设，可能严重低估不确定性。\n\n**为什么影响接收**: 几乎所有 functional decodability 结论都依赖 probe R²。如果 R² 不可信，Finding 3（non-monotonic refinement）的 functional 证据和 trained vs. untrained 比较的定量结论都受影响。\n\n**建议**: (a) 明确报告 train/test split 策略（建议按 demo 或 task 分组以避免 temporal leakage）；(b) 报告 test-set R²，not training/validation R²；(c) 使用 task-level 或 demo-level bootstrap（而非 timestep-level）以反映真实不确定性；(d) 讨论 MLP vs linear probe gap 的含义。\n\n---\n\n### W4 [WARNING]: RSA 统计推断中的依赖性问题未处理\n\n**位置**: Section 3.5, Section 4.4\n\n**问题**: RSA 使用 Spearman ρ 比较 N×N RDM 的上三角。但 N(N-1)/2 pairwise distances 不是独立的（共享 observations），标准 bootstrap 会低估 variance。作者使用 10,000 bootstrap resamples 计算 CI，但 bootstrap 的 resampling unit 不明确。如果是 timestep-level resampling，CI 会因依赖性被严重低估。\n\nPermutation test（Appendix A.9.3）仅测试 \"是否存在 ANY structure\"（observed ρ vs. null），这个 trivially significant（ρ = 0.4-0.6 vs null max 0.08-0.10），但不测试条件间差异的显著性。\n\n训练效应的核心比较：best-vs-best Δ = +0.017 是 n.s.，same-layer L12 Δ = +0.079 是 p < 0.0001。但 same-layer 比较存在 selection bias（选择了差异最大的层）。正确的做法是 pre-register 比较层或对所有 33 层做 FDR correction。\n\n**建议**: (a) 使用 Mantel test 或 stimulus-level bootstrap（resample observations, not distances）作为更合适的 RSA 统计检验；(b) 明确 bootstrap resampling unit；(c) 对条件间 RSA 差异进行适当的多重比较校正。\n\n---\n\n### W5 [WARNING]: RSA vs CKA 分歧对 Finding 3 的影响被低估\n\n**位置**: Appendix A.1-A.2, Section 4.4\n\n**问题**: Linear CKA 完全反转 RSA 排序：untrained LLM (0.089) > trained LLM (0.083) > DINOv2 (0.066)（Appendix A.2）。更重要的是，linear CKA 的 per-layer profile 是 MONOTONICALLY INCREASING（L0: 0.081 → L32: 0.098），完全没有 inverted-U。\n\n论文的解释是 \"RSA captures rank-order geometry; CKA captures global linear structure\"，但这只是重述了数学定义，没有论证为什么 rank-order geometry 对 VLA action prediction 更相关。如果 CKA（度量 global covariance structure）才是更相关的 metric，那么 Finding 3 的 \"non-monotonic refinement\" 完全不存在——实际上是 monotonic improvement。\n\nRDM kernel CKA 部分支持 RSA（trained > untrained），但 encoder ordering 仍不同。三个 metrics 给出三种不同的故事，论文选择了 RSA 的故事作为主叙事。\n\n**为什么影响接收**: Finding 3 是论文三个核心发现之一，而它是 metric-dependent 的。不同读者可能合理地选择 CKA 而得出完全不同的结论。\n\n**建议**: (a) 提供理论或实证论证说明为什么 rank-order preservation（RSA）比 covariance alignment（CKA）更预测 downstream action performance；(b) 或者将 Finding 3 重新表述为 \"under RSA\" 并承认在 CKA 下不成立，降低 claim strength。\n\n---\n\n### W6 [WARNING]: 单模型单 benchmark，泛化性不足以支撑 general claims\n\n**位置**: Title, Abstract, Discussion (Section 5)\n\n**问题**: 论文标题 \"Vision Encodes, Language Routes\" 暗示对 VLA 的一般性结论，但所有实验仅在 OpenVLA-7B + LIBERO 上进行。LIBERO 仅包含 10 个 tabletop manipulation tasks，50 demos each。\n\n- 无其他 VLA 模型（如 RT-2, π₀, Octo 等）\n- 无 real-robot 数据\n- 无多样化任务域（所有 tasks 都是 tabletop manipulation）\n- LIBERO-Spatial 作为 cross-benchmark validation 仍在 LIBERO 框架内，任务域相同\n\nDiscussion 声称 \"OpenVLA shares the dominant VLA design... with RT-2 and π₀\"，但 π₀ 使用 flow matching 而非 autoregressive decoding，RT-2 使用不同的 vision encoder。这些架构差异可能导致完全不同的 representation dynamics。\n\n**建议**: (a) 将所有 claims 明确限定在 \"OpenVLA-7B on LIBERO\" 范围内；(b) 或至少在一个架构差异较大的 VLA 上复制核心发现（如使用 diffusion/flow decoder 的模型）。\n\n---\n\n### W7 [WARNING]: 缺少行为验证——表征分析与任务表现之间的 gap 未弥合\n\n**位置**: Discussion Section 5\n\n**问题**: 论文的所有发现都在 representation space 中，没有任何一个发现被连接到 actual task success rate。例如：\n\n- \"Front-loaded instruction routing\" 是否意味着更好的 instruction following？\n- Inverted-U 的 peak layer 是否预测 task performance？\n- L1 attention ablation 如何影响 rollout success？\n\n作者在 Limitations 中承认 \"linking routing to behavioral outcomes requires task-level evaluation\"，但对于 CoRL（一个 robotics 会议），representational analysis 如果不能连接到 robot behavior，其实用价值有限。\n\n**建议**: 即使是 pilot 级别的行为验证（如：ablate L1 instruction routing → rollout success 变化）也能大幅提升论文说服力。\n\n---\n\n### W8 [INFO]: Pretrained Llama-2 的 visual token 处理是否有意义\n\n**位置**: Section 3.1, Appendix A.5\n\n**问题**: Pretrained Llama-2 从未见过 projected visual tokens。Appendix A.5 的 OOD diagnostics 仅证明 representations 非退化（activation magnitude 合理、cosine similarity progressive decline、PC variance stable），但非退化不等于有意义的处理。一个 non-degenerate but meaningless 的 representation 也能通过这些测试。\n\n这个条件的 cross-instruction probe 结果（L1: 80.2% → L31: 100%）可能反映了 Llama-2 的 generic 序列处理能力（任何 token 序列都会被逐层整合），而非对 visual+instruction 的有意义处理。\n\n**建议**: 加一个 diagnostic：用 random noise tokens（相同维度）替代 visual tokens 输入 Llama-2 base，如果 probe 结果类似，则 Llama-2 base 条件的可解释性大幅降低。\n\n---\n\n## Questions for Authors\n\n**Q1**: Action probe 的 R² 是在 training set 还是 held-out test set 上计算的？如果是 test set，train/test split 策略是什么（random timestep split? demo-level? task-level?）？\n\n**Q2**: 所有 head ablation（dominant 和 random）都 INCREASE R²。这是否意味着 L1 的大多数 heads 对 action prediction 实际上是有害的？如果是，\"dual routing-encoding function\" 的解释还成立吗？\n\n**Q3**: 如果将 Finding 1 的 10-way classification 替换为更难的任务（如 paraphrase 指令或语义相近的指令对），结果是否会不同？是否有定量估计 probe task difficulty 的方法？\n\n**Q4**: 为什么 linear probe 的 trained-untrained gap（Δ = +0.324 at L14）是 MLP probe gap（Δ = +0.015 at L8）的 ~20 倍？这对结果解释有什么影响？\n\n**Q5**: Bootstrap CI 的 resampling unit 是什么？如果是 timestep-level，如何处理同一 demo 内时间步之间的高度自相关？\n\n**Q6**: 能否提供 RSA 条件间差异的 permutation test 或 Mantel test（而非仅测试 \"是否存在 structure\"）？\n\n---\n\n## Missing References\n\n引用覆盖基本充分（42 篇，含 VLA、mechanistic interpretability、probing methodology 的关键文献）。以下可考虑补充：\n\n- **Probing methodology 的 criticism**: Hewitt & Liang (2019) \"Designing and Interpreting Probes with Control Tasks\"——关于 probe selectivity 的重要讨论，与本文 probe 方法论直接相关\n- **VLA behavioral evaluation**: 论文引用了 Grant et al. 和 Häon et al.，但缺少 Zheng et al. (2024) \"3D-VLA\" 等在表征层面分析 VLA 的工作\n- **RSA 统计方法**: Nili et al. (2014) \"A Toolbox for Representational Similarity Analysis\"——包含 RSA 统计推断最佳实践的工具箱论文\n\n---\n\n## Overall Assessment\n\n**Score: 5 (Marginally below acceptance threshold)**\n\n**Confidence: 4 (Confident but not absolutely certain)**\n\n---\n\n## 官方维度打分（基于 CoRL review dimensions + OpenReview default form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 6/10 | 三条件 factorial design 和 per-layer per-token-type 分析框架有新意；但 Finding 1 大部分由架构推出，Finding 3 是 metric-dependent 的 |\n| Quality (Soundness) | 4/10 | Ablation 因果推断方向有问题（W2）；probe train/test split 未说明（W3）；RSA 统计推断有依赖性问题（W4）；MLP probe overparameterized |\n| Clarity | 7/10 | 写作清晰，结构合理，图表信息密度高；附录组织良好。但部分关键方法细节缺失（train/test split, bootstrap unit）|\n| Significance | 5/10 | 分析框架可复用，但缺少行为验证（W7），泛化性不足（W6），且核心发现中 2/3 有方法论隐忧 |\n| Relevance to CoRL | 5/10 | 研究 VLA 是 relevant 的，但 CoRL 更看重 actionable 的机器人学习贡献；纯表征分析无 behavioral validation 对 robotics community 的直接价值有限 |\n| Limitations honesty | 7/10 | 作者诚实报告了单模型限制、CKA 分歧、n.s. results；但未充分讨论 probe methodology 的局限 |\n\n---\n\n## Detailed Comments (逐节)\n\n### Abstract\n- Abstract 结构合理，覆盖了四个必答问题。\n- \"100% instruction classification from L1, cross-validated\" 在不提及 untrained 也达到 100% 的情况下显得 misleading。\n- \"$z = -2.73$\" 级别的细节不适合 abstract。\n\n### Introduction\n- 叙事线清晰：behavioral observation → gap → our approach → three findings → contributions。\n- 但 contribution (i) \"verifying architecture-expected specialization\" 在 Introduction 中被 framed 为一个积极贡献，实际上它更像是一个 sanity check。将 sanity check 升格为 contribution 降低了论文的 novelty 感知。\n- Contribution (iii) 中 \"RSA confirms geometrically but CKA diverges\" 的 parenthetical 承认了问题但在 contribution 列表中提及让读者困惑——核心贡献是否 metric-dependent？\n\n### Method (Section 3)\n- 方法描述清晰完整。\n- Section 3.6 \"Why RSA over CKA\" 给出了合理理由（scale invariance, dimension mismatch），但 dimension mismatch 主要影响 linear CKA，而 RDM kernel CKA 不受此问题影响却仍与 RSA 部分分歧。\n\n### Experiments (Section 4)\n\n**4.2 Token-Level Functional Specialization:**\n- Image-token instruction-blindness 是 causal mask 的直接后果，不是发现。论文部分承认 (\"consistent with the causal mask and frozen encoder\") 但仍将其作为 Finding 1 的主要组成部分。\n- Readout token 100% 分类的 trivially easy 问题见 W1。\n\n**4.3 VLA Fine-Tuning Front-Loads Instruction Routing:**\n- 三条件 gradient（untrained 0/32 → Llama-2 base 9/32 → VLA-trained 24/32）是论文最有说服力的发现。\n- Threshold sensitivity analysis（Table A.10）增强了 confidence。\n- 但 ablation 的问题（W2）削弱了因果推断链。\n\n**4.4 Non-Monotonic Refinement:**\n- 这是论文最 nuanced 也最有争议的发现。\n- Inverted-U 在 RSA 下 reproducible（across seeds, demos, metrics, benchmarks），但在 CKA 下不存在。\n- \"Training reshapes WHERE geometry peaks rather than HOW HIGH\" 基于 best-vs-best Δ = +0.017 (n.s.)。严格来说，n.s. 结果不能用来支撑 \"reshapes where\" 的 claim——n.s. 只说明我们不能拒绝 \"no difference\" 的 null。\n\n### Discussion (Section 5)\n- \"Speculative mechanistic interpretation\" 段落的 speculative 标记值得肯定。\n- \"Early-layer parameters may suffice for instruction adaptation\" 是有趣的 architectural implication 但缺少任何验证。\n- Limitations 段落诚实但不完整（未提 probe methodology 的局限）。\n\n### Appendix\n- 组织良好，robustness 分析充分。\n- OOD diagnostics（A.5）是有帮助的 but insufficient（见 W8）。\n- QA probe（A.8.3）是一个有趣的补充，但 trained vs untrained 差异极小（86.3% vs 85.3%），不支持 \"training creates richer task-relevant information at the readout\" 的 claim。\n",
  "reviewer_id": "1",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 — Round 1 Review\n\n**Paper**: \"Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\"\n**Target Venue**: CoRL 2026\n**审查侧重**: 方法严谨性 + 实验设计\n\n---\n\n## Summary (2-3 sentences)\n\n本文对 OpenVLA-7B 在 LIBERO 上进行了 per-layer、per-token-type 的表征分析，使用 cross-instruction probes、attention pattern analysis、RSA 和 functional probes，配合 trained/pretrained/untrained 三条件对照。核心发现是：(1) image token 对 instruction 不敏感（架构必然）；(2) VLA 训练将 instruction routing 从中层移至 entry-exit 层；(3) vision encoder 表征经 LLM 层呈 inverted-U 变换。这是一篇分析型论文，方法论工作扎实但存在若干统计推断和因果推断层面的问题。\n\n---\n\n## Strengths\n\n- **S1: 系统性的实验框架设计。** 三条件因子控制（VLA-trained / Llama-2 base / untrained）× 指令有无的 2×2 factorial 设计是合理的。与大多数 VLA 分析工作相比，这种控制更完整，可以隔离语言预训练和 VLA fine-tuning 各自的贡献（Section 3.1）。\n\n- **S2: 多角度互验。** RSA（几何对齐）+ functional probes（可解码性）+ attention analysis（机制）+ cross-instruction probes（信息内容）四种互补工具的组合使用是方法论上的优势。Linear probe 复制（Appendix A.6）进一步增强了 functional probe 结论的可信度。\n\n- **S3: 丰富的 robustness 分析。** 附录中的 distance metric invariance（Table A.5）、demonstration subsampling（Table A.7）、seed sensitivity（Table A.6）、threshold sensitivity（Table A.10）、cross-benchmark validation（LIBERO-Spatial, Appendix A.4）显示作者认真检验了结论的鲁棒性。\n\n- **S4: 对 CKA 分歧的诚实处理。** 多数论文会回避不利结果。作者坦承 linear CKA 完全反转了 RSA 排序（Appendix A.2, Figure A.1），并提供了合理（虽然不完全令人信服）的解释。\n\n- **S5: 与 behavioral 文献的连接。** 将 image-token instruction-blindness 与 Grant et al. [2026] 和 Häon et al. [2025] 发现的 visual dominance 建立联系（Discussion），帮助读者理解分析发现的实际意义。\n\n---\n\n## Weaknesses (按严重程度排序)\n\n### W1 [CRITICAL]: Cross-instruction probe（Finding 1）近乎 trivially easy，削弱了核心贡献的新颖性\n\n**位置**: Section 4.2, Table 1\n\n**问题**: 10-way cross-instruction classification 在 readout token 位置上，ALL THREE 条件（trained, pretrained, untrained）在 L1 均达到 99.6-100%。作者自己在 Appendix A.8.1 承认 \"even incidental attention (~12%) suffices for linear classification at L1\"。这意味着只要有任何 attention 到 instruction tokens——哪怕是随机初始化权重产生的微弱 attention——probe 就能轻松区分 10 条差异很大的 LIBERO 指令。\n\n10 条 LIBERO-Goal 指令（如 \"pick up the red cup\" vs \"push the blue block\"）在 token 层面差异巨大。一个 linear classifier 只需检测到 instruction embedding 的最微小残留即可达到 100%。这不是关于 VLA 如何处理指令信息的深层洞察，而是 tokenizer + 单层 attention 的 trivial 后果。\n\n更有信息量的比较是 DECAY PATTERN（untrained 从 100% 降至 82%，trained 维持 100%），但论文将 \"100% from L1\" 作为主要发现来呈现，而非衰减差异。\n\n**为什么影响接收**: Finding 1（token-level functional specialization）是三个核心贡献之一。如果它大部分由架构约束直接推出（causal mask → image tokens blind，tokenizer + any attention → readout trivially classifiable），那么作为 \"contribution\" 的增量价值大幅降低。\n\n**建议**: (a) 增加更难的 probe task（如语义近似但不同的指令，或 paraphrase 指令）以测试真正的指令理解 vs. 表面 token 检测；(b) 重新 framing Finding 1 为 \"验证架构预期\" 而非 \"发现\"，论文部分已做但不够彻底。\n\n---\n\n### W2 [CRITICAL]: L1 head ablation 的因果推断方向存在根本性问题\n\n**位置**: Section 4.3, Appendix A.4\n\n**问题**: Ablating 24/32 dominant heads at L1 increases action R² by +0.042（baseline 0.517）。Random 24-head ablation increases by +0.077。作者解释为 dominant heads 具有 \"dual routing-encoding function\"。\n\n但基本事实是：ablating ANY 24 out of 32 heads (75%) at L1 IMPROVES action prediction。无论是 dominant heads 还是 random heads，移除都提高 R²。这意味着 L1 的大多数 heads 对 action prediction 是 net-negative 的。如果研究者声称 L1 的 instruction-dominant heads 具有功能性重要作用，那么 ablation 应该 DECREASE R²（性能变差），而非 increase。\n\n论文的 \"dual function\" 解释是一种 post-hoc rationalization：dominant heads 虽然 R² 增幅小于 random heads，但两者都是正增幅。等效的替代解释是：L1 heads 普遍对 action probe 添加噪声，dominant heads 因为 attention pattern 更结构化所以噪声更少。这不需要 \"dual function\" 假设。\n\n此外，random-subset 只用了 N=10 个子集（C(32,24) = 10,518,300 种可能），z-test 的统计检验力极低且分布假设可疑。\n\n**为什么影响接收**: L1 ablation 是论文中唯一的因果证据（区别于纯相关性分析）。如果因果推断不成立，Finding 2 的证据链从 \"相关+因果\" 降级为 \"仅相关\"。\n\n**建议**: (a) 增加更细粒度的 ablation（如 ablate 4/8/12/16/20/24/28 heads，观察 R² 变化曲线）；(b) 尝试 SELECTIVE ablation（只 ablate dominant heads 的 instruction attention，保留 image attention），这能更精确地测试 \"dual function\" 假设；(c) 大幅增加 random subsets 数量（≥100）；(d) 修改 framing 以反映实际发现（所有 ablation 都提高 R²）。\n\n---\n\n### W3 [CRITICAL]: Action probe 的 train/test split 未明确说明，overparameterized MLP probe 的 R² 可信度存疑\n\n**位置**: Section 3.6, Section 4.1\n\n**问题**: MLP probe 的 N/params ≈ 0.06（作者自认 \"overparameterized\"）。论文称 \"early stopping mitigates overfitting\"，但：\n\n(a) R² 是在哪个数据集上计算的？论文未明确说明 train/test/validation split。如果 R² 是 training data 上的值，那么 overparameterized model 可以达到任意高的 R²，所有结论无效。如果是 validation set（early stopping 的依据），那么 R² 也可能被 early stopping 的选择偏倚。\n\n(b) Linear probe 复制（Appendix A.6）显示 trained-untrained gap 在 linear probe 下为 Δ = +0.324（L14），在 MLP probe 下仅为 Δ = +0.015（L8），相差 ~20 倍。这暗示 MLP probe 过于强大，rescues 了 untrained representations 的信息，压缩了条件间差异。这意味着 MLP probe R² 的绝对值和条件间差异都可能是 misleading 的。\n\n(c) N=63,228 observations 但时间步之间高度自相关（连续 frames of same demo），有效样本量远小于名义值。Bootstrap CI 基于独立重抽样假设，可能严重低估不确定性。\n\n**为什么影响接收**: 几乎所有 functional decodability 结论都依赖 probe R²。如果 R² 不可信，Finding 3（non-monotonic refinement）的 functional 证据和 trained vs. untrained 比较的定量结论都受影响。\n\n**建议**: (a) 明确报告 train/test split 策略（建议按 demo 或 task 分组以避免 temporal leakage）；(b) 报告 test-set R²，not training/validation R²；(c) 使用 task-level 或 demo-level bootstrap（而非 timestep-level）以反映真实不确定性；(d) 讨论 MLP vs linear probe gap 的含义。\n\n---\n\n### W4 [WARNING]: RSA 统计推断中的依赖性问题未处理\n\n**位置**: Section 3.5, Section 4.4\n\n**问题**: RSA 使用 Spearman ρ 比较 N×N RDM 的上三角。但 N(N-1)/2 pairwise distances 不是独立的（共享 observations），标准 bootstrap 会低估 variance。作者使用 10,000 bootstrap resamples 计算 CI，但 bootstrap 的 resampling unit 不明确。如果是 timestep-level resampling，CI 会因依赖性被严重低估。\n\nPermutation test（Appendix A.9.3）仅测试 \"是否存在 ANY structure\"（observed ρ vs. null），这个 trivially significant（ρ = 0.4-0.6 vs null max 0.08-0.10），但不测试条件间差异的显著性。\n\n训练效应的核心比较：best-vs-best Δ = +0.017 是 n.s.，same-layer L12 Δ = +0.079 是 p < 0.0001。但 same-layer 比较存在 selection bias（选择了差异最大的层）。正确的做法是 pre-register 比较层或对所有 33 层做 FDR correction。\n\n**建议**: (a) 使用 Mantel test 或 stimulus-level bootstrap（resample observations, not distances）作为更合适的 RSA 统计检验；(b) 明确 bootstrap resampling unit；(c) 对条件间 RSA 差异进行适当的多重比较校正。\n\n---\n\n### W5 [WARNING]: RSA vs CKA 分歧对 Finding 3 的影响被低估\n\n**位置**: Appendix A.1-A.2, Section 4.4\n\n**问题**: Linear CKA 完全反转 RSA 排序：untrained LLM (0.089) > trained LLM (0.083) > DINOv2 (0.066)（Appendix A.2）。更重要的是，linear CKA 的 per-layer profile 是 MONOTONICALLY INCREASING（L0: 0.081 → L32: 0.098），完全没有 inverted-U。\n\n论文的解释是 \"RSA captures rank-order geometry; CKA captures global linear structure\"，但这只是重述了数学定义，没有论证为什么 rank-order geometry 对 VLA action prediction 更相关。如果 CKA（度量 global covariance structure）才是更相关的 metric，那么 Finding 3 的 \"non-monotonic refinement\" 完全不存在——实际上是 monotonic improvement。\n\nRDM kernel CKA 部分支持 RSA（trained > untrained），但 encoder ordering 仍不同。三个 metrics 给出三种不同的故事，论文选择了 RSA 的故事作为主叙事。\n\n**为什么影响接收**: Finding 3 是论文三个核心发现之一，而它是 metric-dependent 的。不同读者可能合理地选择 CKA 而得出完全不同的结论。\n\n**建议**: (a) 提供理论或实证论证说明为什么 rank-order preservation（RSA）比 covariance alignment（CKA）更预测 downstream action performance；(b) 或者将 Finding 3 重新表述为 \"under RSA\" 并承认在 CKA 下不成立，降低 claim strength。\n\n---\n\n### W6 [WARNING]: 单模型单 benchmark，泛化性不足以支撑 general claims\n\n**位置**: Title, Abstract, Discussion (Section 5)\n\n**问题**: 论文标题 \"Vision Encodes, Language Routes\" 暗示对 VLA 的一般性结论，但所有实验仅在 OpenVLA-7B + LIBERO 上进行。LIBERO 仅包含 10 个 tabletop manipulation tasks，50 demos each。\n\n- 无其他 VLA 模型（如 RT-2, π₀, Octo 等）\n- 无 real-robot 数据\n- 无多样化任务域（所有 tasks 都是 tabletop manipulation）\n- LIBERO-Spatial 作为 cross-benchmark validation 仍在 LIBERO 框架内，任务域相同\n\nDiscussion 声称 \"OpenVLA shares the dominant VLA design... with RT-2 and π₀\"，但 π₀ 使用 flow matching 而非 autoregressive decoding，RT-2 使用不同的 vision encoder。这些架构差异可能导致完全不同的 representation dynamics。\n\n**建议**: (a) 将所有 claims 明确限定在 \"OpenVLA-7B on LIBERO\" 范围内；(b) 或至少在一个架构差异较大的 VLA 上复制核心发现（如使用 diffusion/flow decoder 的模型）。\n\n---\n\n### W7 [WARNING]: 缺少行为验证——表征分析与任务表现之间的 gap 未弥合\n\n**位置**: Discussion Section 5\n\n**问题**: 论文的所有发现都在 representation space 中，没有任何一个发现被连接到 actual task success rate。例如：\n\n- \"Front-loaded instruction routing\" 是否意味着更好的 instruction following？\n- Inverted-U 的 peak layer 是否预测 task performance？\n- L1 attention ablation 如何影响 rollout success？\n\n作者在 Limitations 中承认 \"linking routing to behavioral outcomes requires task-level evaluation\"，但对于 CoRL（一个 robotics 会议），representational analysis 如果不能连接到 robot behavior，其实用价值有限。\n\n**建议**: 即使是 pilot 级别的行为验证（如：ablate L1 instruction routing → rollout success 变化）也能大幅提升论文说服力。\n\n---\n\n### W8 [INFO]: Pretrained Llama-2 的 visual token 处理是否有意义\n\n**位置**: Section 3.1, Appendix A.5\n\n**问题**: Pretrained Llama-2 从未见过 projected visual tokens。Appendix A.5 的 OOD diagnostics 仅证明 representations 非退化（activation magnitude 合理、cosine similarity progressive decline、PC variance stable），但非退化不等于有意义的处理。一个 non-degenerate but meaningless 的 representation 也能通过这些测试。\n\n这个条件的 cross-instruction probe 结果（L1: 80.2% → L31: 100%）可能反映了 Llama-2 的 generic 序列处理能力（任何 token 序列都会被逐层整合），而非对 visual+instruction 的有意义处理。\n\n**建议**: 加一个 diagnostic：用 random noise tokens（相同维度）替代 visual tokens 输入 Llama-2 base，如果 probe 结果类似，则 Llama-2 base 条件的可解释性大幅降低。\n\n---\n\n## Questions for Authors\n\n**Q1**: Action probe 的 R² 是在 training set 还是 held-out test set 上计算的？如果是 test set，train/test split 策略是什么（random timestep split? demo-level? task-level?）？\n\n**Q2**: 所有 head ablation（dominant 和 random）都 INCREASE R²。这是否意味着 L1 的大多数 heads 对 action prediction 实际上是有害的？如果是，\"dual routing-encoding function\" 的解释还成立吗？\n\n**Q3**: 如果将 Finding 1 的 10-way classification 替换为更难的任务（如 paraphrase 指令或语义相近的指令对），结果是否会不同？是否有定量估计 probe task difficulty 的方法？\n\n**Q4**: 为什么 linear probe 的 trained-untrained gap（Δ = +0.324 at L14）是 MLP probe gap（Δ = +0.015 at L8）的 ~20 倍？这对结果解释有什么影响？\n\n**Q5**: Bootstrap CI 的 resampling unit 是什么？如果是 timestep-level，如何处理同一 demo 内时间步之间的高度自相关？\n\n**Q6**: 能否提供 RSA 条件间差异的 permutation test 或 Mantel test（而非仅测试 \"是否存在 structure\"）？\n\n---\n\n## Missing References\n\n引用覆盖基本充分（42 篇，含 VLA、mechanistic interpretability、probing methodology 的关键文献）。以下可考虑补充：\n\n- **Probing methodology 的 criticism**: Hewitt & Liang (2019) \"Designing and Interpreting Probes with Control Tasks\"——关于 probe selectivity 的重要讨论，与本文 probe 方法论直接相关\n- **VLA behavioral evaluation**: 论文引用了 Grant et al. 和 Häon et al.，但缺少 Zheng et al. (2024) \"3D-VLA\" 等在表征层面分析 VLA 的工作\n- **RSA 统计方法**: Nili et al. (2014) \"A Toolbox for Representational Similarity Analysis\"——包含 RSA 统计推断最佳实践的工具箱论文\n\n---\n\n## Overall Assessment\n\n**Score: 5 (Marginally below acceptance threshold)**\n\n**Confidence: 4 (Confident but not absolutely certain)**\n\n---\n\n## 官方维度打分（基于 CoRL review dimensions + OpenReview default form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 6/10 | 三条件 factorial design 和 per-layer per-token-type 分析框架有新意；但 Finding 1 大部分由架构推出，Finding 3 是 metric-dependent 的 |\n| Quality (Soundness) | 4/10 | Ablation 因果推断方向有问题（W2）；probe train/test split 未说明（W3）；RSA 统计推断有依赖性问题（W4）；MLP probe overparameterized |\n| Clarity | 7/10 | 写作清晰，结构合理，图表信息密度高；附录组织良好。但部分关键方法细节缺失（train/test split, bootstrap unit）|\n| Significance | 5/10 | 分析框架可复用，但缺少行为验证（W7），泛化性不足（W6），且核心发现中 2/3 有方法论隐忧 |\n| Relevance to CoRL | 5/10 | 研究 VLA 是 relevant 的，但 CoRL 更看重 actionable 的机器人学习贡献；纯表征分析无 behavioral validation 对 robotics community 的直接价值有限 |\n| Limitations honesty | 7/10 | 作者诚实报告了单模型限制、CKA 分歧、n.s. results；但未充分讨论 probe methodology 的局限 |\n\n---\n\n## Detailed Comments (逐节)\n\n### Abstract\n- Abstract 结构合理，覆盖了四个必答问题。\n- \"100% instruction classification from L1, cross-validated\" 在不提及 untrained 也达到 100% 的情况下显得 misleading。\n- \"$z = -2.73$\" 级别的细节不适合 abstract。\n\n### Introduction\n- 叙事线清晰：behavioral observation → gap → our approach → three findings → contributions。\n- 但 contribution (i) \"verifying architecture-expected specialization\" 在 Introduction 中被 framed 为一个积极贡献，实际上它更像是一个 sanity check。将 sanity check 升格为 contribution 降低了论文的 novelty 感知。\n- Contribution (iii) 中 \"RSA confirms geometrically but CKA diverges\" 的 parenthetical 承认了问题但在 contribution 列表中提及让读者困惑——核心贡献是否 metric-dependent？\n\n### Method (Section 3)\n- 方法描述清晰完整。\n- Section 3.6 \"Why RSA over CKA\" 给出了合理理由（scale invariance, dimension mismatch），但 dimension mismatch 主要影响 linear CKA，而 RDM kernel CKA 不受此问题影响却仍与 RSA 部分分歧。\n\n### Experiments (Section 4)\n\n**4.2 Token-Level Functional Specialization:**\n- Image-token instruction-blindness 是 causal mask 的直接后果，不是发现。论文部分承认 (\"consistent with the causal mask and frozen encoder\") 但仍将其作为 Finding 1 的主要组成部分。\n- Readout token 100% 分类的 trivially easy 问题见 W1。\n\n**4.3 VLA Fine-Tuning Front-Loads Instruction Routing:**\n- 三条件 gradient（untrained 0/32 → Llama-2 base 9/32 → VLA-trained 24/32）是论文最有说服力的发现。\n- Threshold sensitivity analysis（Table A.10）增强了 confidence。\n- 但 ablation 的问题（W2）削弱了因果推断链。\n\n**4.4 Non-Monotonic Refinement:**\n- 这是论文最 nuanced 也最有争议的发现。\n- Inverted-U 在 RSA 下 reproducible（across seeds, demos, metrics, benchmarks），但在 CKA 下不存在。\n- \"Training reshapes WHERE geometry peaks rather than HOW HIGH\" 基于 best-vs-best Δ = +0.017 (n.s.)。严格来说，n.s. 结果不能用来支撑 \"reshapes where\" 的 claim——n.s. 只说明我们不能拒绝 \"no difference\" 的 null。\n\n### Discussion (Section 5)\n- \"Speculative mechanistic interpretation\" 段落的 speculative 标记值得肯定。\n- \"Early-layer parameters may suffice for instruction adaptation\" 是有趣的 architectural implication 但缺少任何验证。\n- Limitations 段落诚实但不完整（未提 probe methodology 的局限）。\n\n### Appendix\n- 组织良好，robustness 分析充分。\n- OOD diagnostics（A.5）是有帮助的 but insufficient（见 W8）。\n- QA probe（A.8.3）是一个有趣的补充，但 trained vs untrained 差异极小（86.3% vs 85.3%），不支持 \"training creates richer task-relevant information at the readout\" 的 claim。\n",
    "reviewer_id": "1",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 208 · 2026-05-18T09:07:43.419241+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4368
}
```

</details>

---


### Assistant

_source line 209 · 2026-05-18T09:07:52.316519+00:00_

审稿意见已提交给 Review Director。

**评审总结**:

- **评分**: 5/10（Marginally below acceptance threshold）
- **信心**: 4/5

**核心问题（3 个 CRITICAL）**:
1. **Cross-instruction probe trivially easy** — untrained 模型在 L1 也达 100%，10-way 分类任务难度不足以支撑 Finding 1 的 contribution 级别
2. **L1 ablation 因果推断方向有问题** — 所有 ablation（dominant 和 random heads）都提高 R²，说明 L1 大多数 heads 对 action prediction 是 net-negative 的，"dual function" 解释是 post-hoc rationalization
3. **Action probe train/test split 未说明** — overparameterized MLP probe (N/params ≈ 0.06) 的 R² 在不清楚评估集的情况下不可信

**次要问题（4 个 WARNING）**: RSA 统计依赖性未处理、CKA 分歧对 Finding 3 影响被低估、单模型单 benchmark 泛化性不足、缺少行为验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1"
}
```

</details>

---


## Round 10

## Round 10

4 recorded events


### User

_source line 210 · 2026-05-18T09:08:41.857649+00:00_

[Round 1 审稿请求]:
## Step 2 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整 Round 1 审稿意见。请逐条回应：
- **[AGREE]**：同意并说明理由
- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）

特别关注与你意见分歧的地方。

---

# Reviewer 2 — Round 1 审稿意见

**Score: Weak Reject (4/10), Confidence: High**

## Strengths
- S1: 实验设计严谨的阶乘控制（2×3 设计）
- S2: 统计报告高标准（bootstrap CI, FDR, permutation test, seed/demo sensitivity）
- S3: C2 routing reorganization 发现有价值（三条件梯度 30%-70% 阈值稳定）
- S4: 方法互补性好（四种分析方法交叉验证 + CKA 分歧坦诚报告）
- S5: Related Work 定位清晰（与 Grant 2026 三点差异明确）

## Weaknesses

**W1 [CRITICAL]: C1（token specialization）是架构必然结果，不构成实质新颖性**
- Image tokens instruction-blind 由 causal mask + frozen encoder 保证
- 将其列为三大贡献之首让审稿人质疑 novelty bar
- 三大贡献中 C1 架构必然 + C3 metric-dependent → 实质新颖性只有 C2
- 建议降格为 methodology validation

**W2 [CRITICAL]: 单模型（OpenVLA-7B）+ 单 benchmark（LIBERO），泛化性严重不足**
- Abstract 写 "instruction routing reorganization is the primary learned contribution of VLA fine-tuning" 是对所有 VLA 的一般性声明
- Grant 2026 覆盖 6 个 VLA，本文范围更窄
- π₀ 用 flow matching，entry-exit routing pattern 可能完全不同

**W3 [CRITICAL]: 缺少行为层面验证——representational finding 未与 task performance 连接**
- 从未测量 ablation 对 task success rate 的影响
- R² 是离线指标，不等于 behavioral importance
- "early-layer parameters may suffice for instruction adaptation" 是 speculative，无实验支撑
- 对 CoRL（机器人学习会议）是重大缺口

**W4 [WARNING]: Ablation 解释逻辑不够 convincing**
- dominant heads +0.042 vs random +0.077，"dual function" 解释需额外证据
- 同样合理的解释：ablation 普遍通过移除 noise 提高 R²
- z-score 基于仅 10 个 random subsets，统计功效有限

**W5 [WARNING]: C3 metric-dependent，CKA 直接矛盾**
- Linear CKA 单调递增，完全没有 inverted-U
- 论文选择 RSA 的故事作为主叙事
- NLP 领域已有 non-monotonic probing profile（Tenney 2019），增量有限

**W6 [WARNING]: Abstract/Introduction 数据密度过高（~15 个数字），叙事可读性受损**

**W7 [WARNING]: 缺少 Generative AI 使用声明（CoRL 2026 要求）**

**W8 [WARNING]: conclusion.tex 存在但未被 main.tex 编译**

**Minor**: M1 -ing phrases 约 30+ 处; M2 code release 声明可能泄露信息; M3 Table 2 caption 不自包含; M4 nostalgebraist2020 access date 暴露写作日期; M5 "Speculative" 标题过于自贬

## Questions
- Q1: 12% incidental attention 就够 100% classification，那 57.7% 的功能意义是什么？
- Q2: RSA 最高 vs R² 最高指向不同 "best" representation，"vision encoder quality" 如何操作化？
- Q3: Pretrained Llama-2 的 mid-depth routing 是 meaningful 还是 OOD artifact？
- Q4: feature reconstruction pipeline baseline R² (0.517) 与 Table 3 (0.557-0.678) 不同，来源？

## Missing References
Rizzardo 2026, Bills 2023, Templeton 2024, Nanda 2023, VLA fine-tuning efficiency 文献

---

请对以上每个 Weakness (W1-W8)、Question (Q1-Q4) 和 Missing References 逐条回应 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 211 · 2026-05-18T09:10:11.520239+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 交叉回应 — 对 Reviewer 2 Round 1 意见\n\n---\n\n## Weaknesses 逐条回应\n\n**[AGREE] R2-W1: C1 是架构必然结果，不构成实质新颖性**\n\n完全同意。这与我的 W1 一致。补充一点 R2 未强调的证据：Table 1 显示 untrained model 在 L1 也达到 100% classification，Appendix A.8.1 作者自己承认 \"even incidental attention (~12%) suffices for linear classification at L1\"。将 trivially verifiable 的架构属性列为三大贡献之首确实降低了 novelty 感知。降格为 methodology validation / sanity check 是合理建议。\n\n---\n\n**[AGREE] R2-W2: 单模型 + 单 benchmark，泛化性不足**\n\n同意，与我的 W6 一致。补充：LIBERO-Spatial 作为 cross-benchmark validation（Appendix A.4）仍在 LIBERO 框架内，任务域相同（tabletop manipulation），不能算真正的泛化验证。R2 指出 Grant 2026 覆盖了 6 个 VLA 是有力对比——本文范围确实更窄。Abstract 中 \"instruction routing reorganization is the primary learned contribution of VLA fine-tuning\" 的一般性措辞与单模型证据不匹配。\n\n---\n\n**[AGREE] R2-W3: 缺少行为层面验证**\n\n同意，与我的 W7 一致。对于 CoRL 这个强调 robot learning 实际应用的会议，representational analysis 不连接 task performance 是重大缺口。R2 正确指出 \"early-layer parameters may suffice for instruction adaptation\"（Discussion Section 5）是 speculative 的。即使是 pilot 级别的 rollout 验证（如 L1 ablation → success rate 变化）也能显著提升论文价值。\n\n---\n\n**[AGREE with stronger formulation] R2-W4: Ablation 解释逻辑不够 convincing**\n\n同意 R2 的判断，但我认为问题比 R2 所述更严重。R2 提到 \"同样合理的解释：ablation 普遍通过移除 noise 提高 R²\"，这是正确的，但更根本的问题是：dominant-head ablation (+0.042) 和 random-head ablation (+0.077) 都是 POSITIVE（R² 增加）。如果 instruction-dominant heads 真的具有作者声称的功能重要性，ablation 应该 DECREASE R²。所有 ablation 都提高 R² 这一事实意味着 L1 的 75% heads 对 action prediction 是 net-negative 的。\"dual function\" 解释是 post-hoc rationalization，且仅基于 N=10 random subsets 的 z-test。见我的 W2 获取更详细分析。\n\n---\n\n**[AGREE] R2-W5: C3 metric-dependent，CKA 直接矛盾**\n\n同意，与我的 W5 一致。补充一点：R2 提到 \"NLP 领域已有 non-monotonic probing profile（Tenney 2019）\"，这个 incremental novelty 的论点成立。不过公平地说，本文在 VLA 领域（而非 NLP）做这个分析是有增量的，因为 VLA 的 multimodal fusion + action prediction 设定与 NLP 不同。关键问题仍然是 metric-dependency：论文未提供理论或实证论据解释为何 RSA（rank-order preservation）比 CKA（covariance structure）更适合度量 action-relevant representational quality。\n\n---\n\n**[REBUT] R2-W6: Abstract/Introduction 数据密度过高**\n\n部分不同意。数据密度高确实影响可读性，但对于一篇分析型论文（与 methods 论文不同），Abstract 中报告关键数值是合理的。问题不在于数字多，而在于哪些数字 informative：例如 \"$z = -2.73$\" 属于过细的统计细节不适合 Abstract，但 \"100% instruction classification from L1\" 和 \"R² +0.069\" 这类数字是核心 claims 的量化支撑，应该保留。这是写作风格问题（WARNING 级别偏高），而非方法论缺陷。建议降级为 [INFO]。\n\n---\n\n**[AGREE] R2-W7: 缺少 Generative AI 使用声明**\n\n同意。CoRL 2026 明确要求 Generative AI 使用声明（见 Instruction for Authors: \"Generative AI use must be disclosed\"）。main.tex 中未包含此声明。这是一个 desk reject risk 的格式问题。\n\n---\n\n**[AGREE] R2-W8: conclusion.tex 存在但未被 main.tex 编译**\n\n同意。我验证了 main.tex 的 \\input 列表：introduction → related_work → method → experiments → discussion → bibliography → appendix。conclusion.tex 文件存在（含 \\section{Conclusion}）但未被 \\input。这意味着编译后的论文缺少独立的 Conclusion section。虽然 Discussion（Section 5）的最后一段有总结性内容，但缺少独立 Conclusion 不符合学术论文惯例。对 CoRL 不一定是格式违规（官方模板无强制要求），但结构不完整。\n\n---\n\n## Questions 逐条回应\n\n**[AGREE] R2-Q1: 12% attention 够 100% classification，57.7% 的功能意义是什么？**\n\n这是一个尖锐的好问题。与我的 W1 直接相关。如果 12% incidental attention 已足够 100% 分类，那么 VLA training 将 text attention 提升到 57.7% 的功能意义是什么？论文未回答这个关键问题。可能的答案是：更高的 attention 比例服务于更细粒度的 instruction-conditioned processing（不仅是\"识别哪条指令\"，而是\"如何根据指令调整 action\"），但这需要额外实验验证（如 instruction-conditioned action prediction accuracy vs. attention fraction 的相关性）。\n\n---\n\n**[AGREE] R2-Q2: RSA 最高 vs R² 最高指向不同 \"best\" representation**\n\n同意这是一个重要问题。Table 3 显示 DINOv2 cls_token RSA 最高（0.692）但 R² 不是最高（0.634），而 VLA trained readout R² 最高（0.678）但 RSA 不是最高（0.643）。Conclusion 声称 \"vision encoder quality emerges as a key design lever\" 但两个 metrics 对 \"quality\" 的定义不一致。这个 claim 需要操作化定义。\n\n---\n\n**[AGREE with caveat] R2-Q3: Pretrained Llama-2 的 mid-depth routing 是 meaningful 还是 OOD artifact？**\n\n这与我的 W8 一致。但需要 nuance：Appendix A.5 的 OOD diagnostics（activation magnitude, cosine similarity progressive decline, PC variance stability）确实排除了 degenerate representations 的可能性。问题是 \"non-degenerate\" 不等于 \"meaningful\"。如果 Llama-2 对 random noise tokens 也产生类似的 mid-depth routing pattern，那么 pretrained 条件的解释价值大幅降低。我在自己的审稿中建议了这个 control experiment。\n\n---\n\n**[REBUT] R2-Q4: Feature reconstruction pipeline baseline R² 差异**\n\n这个问题论文已明确回答。Section 4.3 有显式脚注：\"R² values in this random-subset analysis differ from Table 3 (baseline 0.557) due to the feature reconstruction pipeline used for head-level manipulation; all comparisons are within-experiment.\"（experiments.tex line 79）。Ablation 使用 feature reconstruction pipeline 重建 per-head contributions，引入了 reconstruction error，导致 baseline R² 低于直接 extraction pipeline。关键是所有 ablation 比较都在同一 pipeline 内进行，internal validity 不受影响。R2 可能遗漏了这个脚注。\n\n---\n\n## Missing References 回应\n\n**[AGREE] Bills 2023 / Templeton 2024 / Nanda 2023**: 这些 mechanistic interpretability 的标志性工作（neuron interpretation, scaling monosemanticity, TransformerLens）与本文的 Related Work \"Mechanistic interpretability in transformers\" 段落直接相关。当前引用侧重 circuit-level 和 attention head 分析（Elhage 2021, Olsson 2022, Wang 2023），缺少 feature/neuron-level 的代表性工作。不过这些遗漏对论文核心论点影响有限——它们是 background completeness 问题而非 missing direct comparisons。\n\n**[PARTIAL AGREE] VLA fine-tuning efficiency 文献**: 如果论文的 Discussion 要做 \"early-layer parameters may suffice for instruction adaptation\" 的推测，引用 LoRA/adapter 在 VLA 上的应用（如 parameter-efficient fine-tuning 文献）会增强上下文。但这属于 speculative implication 的 supporting context，非核心缺失。\n\n**[CANNOT VERIFY] Rizzardo 2026**: 未查到此引用的具体信息，无法判断其相关性。\n\n---\n\n## 总结：与 R2 的一致性和分歧\n\n**高度一致（6/8 Weaknesses）**: W1(C1 trivial), W2(generalization), W3(behavioral validation), W4(ablation logic), W5(CKA divergence), W7(GenAI statement), W8(conclusion.tex)。\n\n**主要分歧**:\n- W4: 我认为问题比 R2 所述更严重（ablation 方向性问题，不仅是 \"解释不够 convincing\"）。\n- W6: 我认为数据密度问题 severity 偏高，建议降级为 INFO。\n- Q4: R2 提问的 baseline R² 差异已被论文脚注解释。\n\n**整体评分对比**: R2 给 4/10 (Weak Reject)，我给 5/10 (Marginally below threshold)。差距主要在于我对 Finding 2（routing reorganization, three-condition gradient）的评价稍高——这是论文中最有说服力的贡献，threshold sensitivity 和 cross-benchmark replication 增强了可信度。但 W2(ablation) 和 W3(no behavioral validation) 的联合影响使我也倾向于 below threshold。\n",
  "reviewer_id": "1",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 交叉回应 — 对 Reviewer 2 Round 1 意见\n\n---\n\n## Weaknesses 逐条回应\n\n**[AGREE] R2-W1: C1 是架构必然结果，不构成实质新颖性**\n\n完全同意。这与我的 W1 一致。补充一点 R2 未强调的证据：Table 1 显示 untrained model 在 L1 也达到 100% classification，Appendix A.8.1 作者自己承认 \"even incidental attention (~12%) suffices for linear classification at L1\"。将 trivially verifiable 的架构属性列为三大贡献之首确实降低了 novelty 感知。降格为 methodology validation / sanity check 是合理建议。\n\n---\n\n**[AGREE] R2-W2: 单模型 + 单 benchmark，泛化性不足**\n\n同意，与我的 W6 一致。补充：LIBERO-Spatial 作为 cross-benchmark validation（Appendix A.4）仍在 LIBERO 框架内，任务域相同（tabletop manipulation），不能算真正的泛化验证。R2 指出 Grant 2026 覆盖了 6 个 VLA 是有力对比——本文范围确实更窄。Abstract 中 \"instruction routing reorganization is the primary learned contribution of VLA fine-tuning\" 的一般性措辞与单模型证据不匹配。\n\n---\n\n**[AGREE] R2-W3: 缺少行为层面验证**\n\n同意，与我的 W7 一致。对于 CoRL 这个强调 robot learning 实际应用的会议，representational analysis 不连接 task performance 是重大缺口。R2 正确指出 \"early-layer parameters may suffice for instruction adaptation\"（Discussion Section 5）是 speculative 的。即使是 pilot 级别的 rollout 验证（如 L1 ablation → success rate 变化）也能显著提升论文价值。\n\n---\n\n**[AGREE with stronger formulation] R2-W4: Ablation 解释逻辑不够 convincing**\n\n同意 R2 的判断，但我认为问题比 R2 所述更严重。R2 提到 \"同样合理的解释：ablation 普遍通过移除 noise 提高 R²\"，这是正确的，但更根本的问题是：dominant-head ablation (+0.042) 和 random-head ablation (+0.077) 都是 POSITIVE（R² 增加）。如果 instruction-dominant heads 真的具有作者声称的功能重要性，ablation 应该 DECREASE R²。所有 ablation 都提高 R² 这一事实意味着 L1 的 75% heads 对 action prediction 是 net-negative 的。\"dual function\" 解释是 post-hoc rationalization，且仅基于 N=10 random subsets 的 z-test。见我的 W2 获取更详细分析。\n\n---\n\n**[AGREE] R2-W5: C3 metric-dependent，CKA 直接矛盾**\n\n同意，与我的 W5 一致。补充一点：R2 提到 \"NLP 领域已有 non-monotonic probing profile（Tenney 2019）\"，这个 incremental novelty 的论点成立。不过公平地说，本文在 VLA 领域（而非 NLP）做这个分析是有增量的，因为 VLA 的 multimodal fusion + action prediction 设定与 NLP 不同。关键问题仍然是 metric-dependency：论文未提供理论或实证论据解释为何 RSA（rank-order preservation）比 CKA（covariance structure）更适合度量 action-relevant representational quality。\n\n---\n\n**[REBUT] R2-W6: Abstract/Introduction 数据密度过高**\n\n部分不同意。数据密度高确实影响可读性，但对于一篇分析型论文（与 methods 论文不同），Abstract 中报告关键数值是合理的。问题不在于数字多，而在于哪些数字 informative：例如 \"$z = -2.73$\" 属于过细的统计细节不适合 Abstract，但 \"100% instruction classification from L1\" 和 \"R² +0.069\" 这类数字是核心 claims 的量化支撑，应该保留。这是写作风格问题（WARNING 级别偏高），而非方法论缺陷。建议降级为 [INFO]。\n\n---\n\n**[AGREE] R2-W7: 缺少 Generative AI 使用声明**\n\n同意。CoRL 2026 明确要求 Generative AI 使用声明（见 Instruction for Authors: \"Generative AI use must be disclosed\"）。main.tex 中未包含此声明。这是一个 desk reject risk 的格式问题。\n\n---\n\n**[AGREE] R2-W8: conclusion.tex 存在但未被 main.tex 编译**\n\n同意。我验证了 main.tex 的 \\input 列表：introduction → related_work → method → experiments → discussion → bibliography → appendix。conclusion.tex 文件存在（含 \\section{Conclusion}）但未被 \\input。这意味着编译后的论文缺少独立的 Conclusion section。虽然 Discussion（Section 5）的最后一段有总结性内容，但缺少独立 Conclusion 不符合学术论文惯例。对 CoRL 不一定是格式违规（官方模板无强制要求），但结构不完整。\n\n---\n\n## Questions 逐条回应\n\n**[AGREE] R2-Q1: 12% attention 够 100% classification，57.7% 的功能意义是什么？**\n\n这是一个尖锐的好问题。与我的 W1 直接相关。如果 12% incidental attention 已足够 100% 分类，那么 VLA training 将 text attention 提升到 57.7% 的功能意义是什么？论文未回答这个关键问题。可能的答案是：更高的 attention 比例服务于更细粒度的 instruction-conditioned processing（不仅是\"识别哪条指令\"，而是\"如何根据指令调整 action\"），但这需要额外实验验证（如 instruction-conditioned action prediction accuracy vs. attention fraction 的相关性）。\n\n---\n\n**[AGREE] R2-Q2: RSA 最高 vs R² 最高指向不同 \"best\" representation**\n\n同意这是一个重要问题。Table 3 显示 DINOv2 cls_token RSA 最高（0.692）但 R² 不是最高（0.634），而 VLA trained readout R² 最高（0.678）但 RSA 不是最高（0.643）。Conclusion 声称 \"vision encoder quality emerges as a key design lever\" 但两个 metrics 对 \"quality\" 的定义不一致。这个 claim 需要操作化定义。\n\n---\n\n**[AGREE with caveat] R2-Q3: Pretrained Llama-2 的 mid-depth routing 是 meaningful 还是 OOD artifact？**\n\n这与我的 W8 一致。但需要 nuance：Appendix A.5 的 OOD diagnostics（activation magnitude, cosine similarity progressive decline, PC variance stability）确实排除了 degenerate representations 的可能性。问题是 \"non-degenerate\" 不等于 \"meaningful\"。如果 Llama-2 对 random noise tokens 也产生类似的 mid-depth routing pattern，那么 pretrained 条件的解释价值大幅降低。我在自己的审稿中建议了这个 control experiment。\n\n---\n\n**[REBUT] R2-Q4: Feature reconstruction pipeline baseline R² 差异**\n\n这个问题论文已明确回答。Section 4.3 有显式脚注：\"R² values in this random-subset analysis differ from Table 3 (baseline 0.557) due to the feature reconstruction pipeline used for head-level manipulation; all comparisons are within-experiment.\"（experiments.tex line 79）。Ablation 使用 feature reconstruction pipeline 重建 per-head contributions，引入了 reconstruction error，导致 baseline R² 低于直接 extraction pipeline。关键是所有 ablation 比较都在同一 pipeline 内进行，internal validity 不受影响。R2 可能遗漏了这个脚注。\n\n---\n\n## Missing References 回应\n\n**[AGREE] Bills 2023 / Templeton 2024 / Nanda 2023**: 这些 mechanistic interpretability 的标志性工作（neuron interpretation, scaling monosemanticity, TransformerLens）与本文的 Related Work \"Mechanistic interpretability in transformers\" 段落直接相关。当前引用侧重 circuit-level 和 attention head 分析（Elhage 2021, Olsson 2022, Wang 2023），缺少 feature/neuron-level 的代表性工作。不过这些遗漏对论文核心论点影响有限——它们是 background completeness 问题而非 missing direct comparisons。\n\n**[PARTIAL AGREE] VLA fine-tuning efficiency 文献**: 如果论文的 Discussion 要做 \"early-layer parameters may suffice for instruction adaptation\" 的推测，引用 LoRA/adapter 在 VLA 上的应用（如 parameter-efficient fine-tuning 文献）会增强上下文。但这属于 speculative implication 的 supporting context，非核心缺失。\n\n**[CANNOT VERIFY] Rizzardo 2026**: 未查到此引用的具体信息，无法判断其相关性。\n\n---\n\n## 总结：与 R2 的一致性和分歧\n\n**高度一致（6/8 Weaknesses）**: W1(C1 trivial), W2(generalization), W3(behavioral validation), W4(ablation logic), W5(CKA divergence), W7(GenAI statement), W8(conclusion.tex)。\n\n**主要分歧**:\n- W4: 我认为问题比 R2 所述更严重（ablation 方向性问题，不仅是 \"解释不够 convincing\"）。\n- W6: 我认为数据密度问题 severity 偏高，建议降级为 INFO。\n- Q4: R2 提问的 baseline R² 差异已被论文脚注解释。\n\n**整体评分对比**: R2 给 4/10 (Weak Reject)，我给 5/10 (Marginally below threshold)。差距主要在于我对 Finding 2（routing reorganization, three-condition gradient）的评价稍高——这是论文中最有说服力的贡献，threshold sensitivity 和 cross-benchmark replication 增强了可信度。但 W2(ablation) 和 W3(no behavioral validation) 的联合影响使我也倾向于 below threshold。\n",
    "reviewer_id": "1",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 212 · 2026-05-18T09:10:16.040493+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4520
}
```

</details>

---


### Assistant

_source line 213 · 2026-05-18T09:10:20.207042+00:00_

交叉回应已提交。与 Reviewer 2 在 6/8 个 Weaknesses 上高度一致，主要分歧在 W4（我认为 ablation 问题更严重）和 W6（我认为数据密度问题 severity 偏高应降级）。对 Q4 做了 REBUT，因为论文脚注已明确解释了 baseline R² 差异。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1"
}
```

</details>

---


## Round 11

## Round 11

20 recorded events


### User

_source line 214 · 2026-05-18T13:36:00.834898+00:00_

[Round 2 审稿请求]:
## Round 2 修订评估 — Reviewer 1

### 背景
上一轮（Round 1）你侧重方法严谨性+实验设计，给出 5/10。论文已根据审稿意见进行修改。本轮任务是**逐条验证 open/in_progress issues 是否已充分修复**，并识别修改是否引入新问题。

### 论文路径
`projects/vla-ssd/docs/paper/main.tex`（含所有 .tex 子文件）
**Venue**: CoRL 2026, Deadline May 29

### Open/In-Progress Issues（你的上轮主要发现）

请逐条标注 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由：

**R6-C1 [CRITICAL]: Ablation 因果推断方向问题**
- 上轮问题：所有 ablation increase R²，"dual function" 是 post-hoc rationalization
- 修改措施：叙事改为 "routing-first specialization"（Section 4.3 ¶4, line 80）；新增 "Action trajectory validation" 段落（lines 83-87）：L1 ablation 改变 72.3% action tokens (d=0.65)，control ablation d=0.41
- 验证要点：(a) "routing-first" 解释是否比 "dual function" 更 convincing？(b) 所有 ablation 仍 increase R² 的基本事实是否被充分 address？(c) action trajectory analysis 是否弥补了因果推断？(d) N=10 random subsets 是否增加？

**R6-C2 [CRITICAL]: Probe train/test split 未说明 + 时间自相关**
- 上轮问题：train/test split 未说明，时间步自相关导致 CI 低估
- 修改措施：Method §3.6 (line 59) 新增 "Probes are trained on demos 0--39 and evaluated on held-out demos 40--49 (demo-level split), ensuring zero temporal overlap"
- 验证要点：(a) demo-level split 是否完全消除时间泄漏？(b) 80/20 split (40 train, 10 test) 是否合理？(c) linear vs MLP 20× gap 是否被讨论？

**R6-C4 [CRITICAL]: 缺 behavioral validation**
- 上轮问题：无 task success rate 连接
- 修改措施：新增 "Action trajectory validation"（Section 4.3 lines 83-87）：open-loop action trajectory 分析（d=0.65, 72.3% token divergence）。Behavioral rollout 因 mujoco 版本不匹配无法实现。
- 验证要点：(a) open-loop action trajectory 是否算 behavioral validation？(b) 是否足够回应 CoRL 审稿人对 behavioral evidence 的期望？(c) 这是 output-level 证据还是 representation-level 证据？

**R6-W1 [WARNING]: RSA pairwise dependency**
- 上轮问题：bootstrap 低估 variance
- 修改措施：Method §3.5 (line 51) 改为 task-level block resampling，引用 Nili 2014
- 验证要点：task-level resampling (N=10 tasks) 是否充分处理了依赖性？N=10 的 bootstrap 功效如何？

### 同时检查
- 上轮你的 W3（MLP probe overparameterization, linear vs MLP 20× gap）是否在正文讨论？
- 修改是否引入新的方法论问题？

### 输出格式
```
## Issue Verification
- R6-C1: [RESOLVED/STILL_OPEN] — 理由
- R6-C2: [RESOLVED/STILL_OPEN] — 理由
- R6-C4: [RESOLVED/STILL_OPEN] — 理由
- R6-W1: [RESOLVED/STILL_OPEN] — 理由

## New Issues (if any)
## Updated Assessment
Score: X/10 (vs 上轮 5/10)
Direction: ↑/↓/→
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 215 · 2026-05-18T13:36:11.888776+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 216 · 2026-05-18T13:36:12.290953+00:00_

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
…[truncated 4675 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 217 · 2026-05-18T13:36:12.291455+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 218 · 2026-05-18T13:36:12.392355+00:00_

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
12	This yields $N = 63{,}228$ observations (50 demonstrations $\times$ 10 tasks $\times$ $\sim$127 timesteps per demonstration). The MLP probe is overparameterized ($N/\text{params} \approx 0.06$); early stopping mitigates overfitting, and all patterns reproduce with a linear probe ($N/\text{params} \approx 2.2$; Appendix~\ref{sec:linear_probe}).
13	
14	%------------------------------------------------------------------
15	\subsection{Token-Level Functional Specialization}
16	\label{sec:token_specialization}
17	
18	We train cross-instruction probes (\S\ref{sec:cross_instruction_probes}): given the same visual frame with each of 10 task instructions, we classify which instruction was present from per-layer activations.
19	
20	\paragraph{Image tokens are instruction-blind.}
21	At the image\_mean position, instruction classification remains at chance (
…[truncated 11395 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 219 · 2026-05-18T13:36:17.677118+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 220 · 2026-05-18T13:36:18.734334+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Synthesis.}
5	Image tokens remain instruction-blind; the readout is the sole multimodal convergence point.
6	Training shifts routing from mid-depth to entry-exit (L0--L1, L31), with effects at the readout ($R^2$ $+0.069$) rather than images ($\Delta \leq 1.7\%$).
7	This instruction-blindness explains the visual dominance reported by Grant et al.~\cite{grant2026}: under RSA, DINOv2 achieves the highest geometric alignment ($\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\ $0.634$), pointing to instruction-conditioned integration.
8	
9	\paragraph{Mechanistic hypothesis and implications.}
10	Per-layer RSA bifurcates after L12 (Figure~\ref{fig:rsa_perlayer_curve}): readout $\rho$ declines gradually while image\_mean drops sharply ($\to 0.422$), consistent with mid-layer integration and deep-layer compression.
11	L1 ablation confirms routing-first specialization ($z = -2.73$ vs.\ random subsets) and is L1-confined ($|\Delta R^2| < 0.02$ at deeper layers).
12	Action trajectory analysis confirms the causal role ($d = 0.65$, $72.3\%$ divergence); the effect distributes across L1 heads rather than concentrating in instruction-dominant ones, yet L0--L1 routing concentration suggests early-layer parameters may suffice for adaptation.
13	
14	\paragraph{Limitations and scope.}
15	We study OpenVLA-7B on LIBERO. OpenVLA shares the dominant VLA design with RT-2~\cite{brohan2023_rt2} and $\pi_0$~\cite{black2024_pi0}; C1 follows from shared architectural constraints, but C2 may differ across backbone scales and decoder paradigms (Appendix~\ref{sec:ood_diagnostics},~\ref{sec:cka_appendix}).
16	
17	\paragraph{Use of Generative AI.}
18	Generative AI tools (Claude, GPT-4) assisted with code implementation and manuscript editing; all scientific content was produced by the authors.
19	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1057
}
```

</details>

---


### Tool call

_source line 221 · 2026-05-18T13:36:18.734738+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 222 · 2026-05-18T13:36:19.238735+00:00_

1	Vision-language-action models (VLAs) fine-tune large language models (LLMs) on robot demonstrations, but how training reshapes information routing at the token level remains uncharacterized.
2	We present a systematic experimental framework for token-level analysis of VLAs, applying cross-instruction probes, attention analysis, Representational Similarity Analysis (RSA), and functional probes across all 32 LLM layers of OpenVLA-7B on LIBERO, with factorial trained/pretrained/untrained controls.
3	Three findings emerge.
4	First, we validate the framework by confirming architecture-expected token specialization: image tokens are instruction-blind (classification at chance across all layers and conditions), while the readout token serves as the sole multimodal convergence point ($100\%$ instruction classification from L1, cross-validated).
5	Second, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth, while VLA training shifts this to entry-layer routing (L0--L1) with exit-layer re-engagement (L31); instruction classification reaches $99.6\%$ at L1 (vs.\ pretrained $80.2\%$), and L1 ablation confirms routing-first head specialization (random-subset control, L1-confined). Untrained models show zero instruction-dominant heads throughout.
6	Third, vision encoder representations follow a metric-dependent non-monotonic trajectory through LLM layers ($R^2$ peaks at L8--L14; RSA confirms but CKA diverges; Appendix).
7	Training effects concentrate at the readout token (probe $R^2$ $+0.069$, instruction attention $+46$pp) rather than visual geometry ($\Delta\rho \leq 0.017$, non-significant); instruction routing reorganization is the primary learned contribution of fine-tuning in the model studied.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 223 · 2026-05-18T13:36:19.239217+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 224 · 2026-05-18T13:36:19.342136+00:00_

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
…[truncated 2520 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 225 · 2026-05-18T13:36:19.342565+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 226 · 2026-05-18T13:36:19.695510+00:00_

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
…[truncated 30597 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 227 · 2026-05-18T13:37:27.585352+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 228 · 2026-05-18T13:37:27.585880+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 229 · 2026-05-18T13:37:27.736603+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 230 · 2026-05-18T13:37:27.887494+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We decompose a VLA's internal representations with factorial trained-vs-untrained control, revealing: (1)~strict token-level specialization (instruction-blind image tokens, cross-validated readout hub); (2)~front-loaded instruction routing, shifted from mid-depth (L9--L16) to entry-exit (L0--L1, L31); and (3)~non-monotonic vision encoder refinement (peak L12, readout $R^2$ $+0.069$, image $\Delta \leq 1.7\%$).
5	Vision encoder quality emerges as a key design lever.
6	Code and representations will be released upon acceptance.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 231 · 2026-05-18T13:39:03.423125+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

````json
{
  "text": "\n# Reviewer 1 — Round 2 修订评估\n\n---\n\n## Issue Verification\n\n### R6-C1 [CRITICAL]: Ablation 因果推断方向问题 — [STILL_OPEN] (partially improved)\n\n**修改内容确认**:\n- Section 4.3 ¶4 (line 80): \"dual routing-encoding function\" → \"routing-first specialization\"，新解释为 dominant heads 携带 organized instruction signals 被 probe 视为 structured noise，因此 ablation 增幅较小\n- 新增 \"Action trajectory validation\"（lines 83-87）: L1 ablation 改变 72.3% action tokens (d=0.65)，control ablation d=0.41; gripper dimension 主导效应 (shift 0.291 vs <0.034)\n- Appendix A.6: per-dimension 分析，per-task Cohen's d (0.43-0.73)，KL divergence (5.08 vs 1.69)\n\n**仍存在的问题**:\n\n(a) **核心矛盾未解决**: ALL ablation（dominant 和 random）仍然 increase R²。\"Routing-first specialization\" 是对 \"dual function\" 的措辞改进，但逻辑结构相同——仍是对 \"为什么 dominant heads ablation 增幅更小\" 的 post-hoc 解释，未正面回答 \"为什么移除任何 24/32 heads 都提升 action prediction\" 这个根本问题。\n\n(b) **Discussion 的自相矛盾**: Discussion line 12 写 \"the effect distributes across L1 heads rather than concentrating in instruction-dominant ones\"。如果 ablation 效应均匀分布在所有 L1 heads 上（而非集中在 instruction-dominant heads），这恰恰削弱了 \"routing-first specialization\" 的 claim——因为 instruction-dominant heads 没有表现出与其他 heads 不同的特殊功能。\n\n(c) **N=10 random subsets 未增加**: 仍然是 10 个随机子集的 z-test。上轮我和 R2 都指出这个样本量对统计推断不足。未修改。\n\n(d) **效应范围窄于 claim**: 新的 trajectory analysis 揭示效应主要集中在 gripper dimension (0.291 vs continuous dimensions <0.034)。这意味着 L1 instruction routing 的 \"causal role\" 主要影响 discrete open/close 决策，而非连续运动控制。但正文仍将其叙述为 general \"routing function\"，未缩小 claim scope。\n\n**积极改进**: Trajectory analysis 本身有价值——从 representation-level（probe R²）推进到 output-level（action token prediction），是正确方向。但不足以完全 resolve 因果推断问题。\n\n**建议**: (a) 正文中显式承认 \"所有 24-head ablation 均提高 R²\" 这一事实并讨论其含义（如 L1 heads 可能普遍冗余）；(b) 增加 random subsets 至 ≥50；(c) 限定 claim scope 至 gripper/discrete 控制。\n\n---\n\n### R6-C2 [CRITICAL]: Probe train/test split + 时间自相关 — [RESOLVED]\n\n**修改内容确认**:\n- Method §3.6 line 59: \"Probes are trained on demos 0-39 and evaluated on held-out demos 40-49 (demo-level split), ensuring zero temporal overlap between training and evaluation trajectories.\"\n\n**评估**:\n- Demo-level split 完全消除了时间泄漏（不同 demo 之间无时间连续性）\n- 80/20 split (40 train / 10 test per task) 是合理比例\n- R² 现在明确是 held-out 数据上的值，解决了上轮对 overparameterized MLP probe R² 可信度的核心担忧\n- Section 4.1 line 12 对 overparameterization 的讨论已有，指向 linear probe 复制\n\n**残余小问题**: Linear vs MLP 20× gap（Δ = +0.324 vs +0.015）仍未在主正文中讨论。Appendix A.6 的 framing（\"VLA training reorganizes representations to make action information more linearly decodable\"）是一种合理解释但排除了替代解释（MLP 过于强大压缩了条件间差异）。这是 [INFO] 级别问题，不阻碍接收。\n\n---\n\n### R6-C4 [CRITICAL]: 缺 behavioral validation — [STILL_OPEN] (partially improved)\n\n**修改内容确认**:\n- 新增 \"Action trajectory validation\"（Section 4.3, lines 83-87）\n- MuJoCo 版本不匹配导致无法 rollout\n\n**评估**:\n\n(a) **Open-loop trajectory analysis 不是 behavioral validation**。它测量的是 \"ablation 改变了模型的 action token 预测\"，这是 output-level 证据而非 behavioral 证据。真正的 behavioral validation 需要 closed-loop rollout：在环境中执行修改后的 action 序列并测量 task success rate。\n\n(b) **对 CoRL 仍是显著缺口**: Cohen's d = 0.65 和 72.3% token divergence 告诉我们 ablation 改变了预测，但不知道预测变好还是变差。可能 ablation 后的 actions 更好（R² 增加暗示如此），也可能在实际环境中因失去 instruction conditioning 而失败。\n\n(c) **进步方向正确**: 从纯 representation-level（R², RSA ρ）推进到 output-level（action token comparison）是有意义的改善。MuJoCo 版本限制是可理解的技术障碍。\n\n(d) **建议**: 如果 closed-loop rollout 确实不可行，至少在 Discussion/Limitations 中明确承认这一 gap 并讨论 output-level 与 behavioral-level 证据的区别。当前 Discussion（line 12）将 trajectory analysis 描述为 \"confirms the causal role\"，这对 \"causal role\" 的定义过宽。\n\n---\n\n### R6-W1 [WARNING]: RSA pairwise dependency — [RESOLVED]\n\n**修改内容确认**:\n- Method §3.5 line 51: \"resampling is performed at the task level (N=10), treating each task's pairwise RDM entries as a block to preserve within-task dependency structure [nili2014toolbox].\"\n\n**评估**:\n- Task-level block resampling 是处理 RDM pairwise dependency 的标准做法（Nili et al. 2014）\n- 引用正确的方法论文献\n- 这解决了核心统计问题：不再将非独立的 pairwise distances 当作独立样本\n\n**残余注意**: N=10 tasks 的 bootstrap 功效有限（10^10 种可能的重抽样中很多高度相似），但这是实验设计的固有限制（LIBERO 只有 10 tasks），非方法论错误。论文应意识到这使得 CI 偏宽，但不需要额外修改。\n\n---\n\n## 上轮 W3（MLP probe overparameterization）检查\n\n- **主正文**: Section 4.1 line 12 承认 overparameterized 并指向 linear probe。未讨论 20× gap。\n- **Appendix A.6**: 讨论了 gap 但 framing 单一（仅 \"linear decodability\" 解释）\n- **评估**: 现在 R² 是 held-out 数据上的值（R6-C2 resolved），overparameterization 的实际危害已大幅降低。20× gap 的 under-discussion 降级为 minor concern。\n\n---\n\n## New Issues\n\n### N1 [WARNING]: Discussion 中的自相矛盾\n\nDiscussion line 12: \"the effect distributes across L1 heads rather than concentrating in instruction-dominant ones, yet L0-L1 routing concentration suggests early-layer parameters may suffice for adaptation.\"\n\n这两个半句互相矛盾：\n- 前半句说 ablation 效应均匀分布（不集中在 instruction-dominant heads）\n- 后半句仍然推论 L0-L1 instruction routing 的特殊意义\n\n如果 ablation 效应不集中在 instruction-dominant heads，那么 \"routing concentration\" 的功能特异性就被削弱了。这里需要更 careful 的逻辑连接。\n\n### N2 [INFO]: conclusion.tex 仍未编译\n\nmain.tex 仍然不包含 `\\input{conclusion}`。R2 上轮指出的 W8 未修复。虽然 Discussion 末尾有总结性内容，但结构不完整。\n\n### N3 [INFO]: Conclusion 中的 claim 未更新\n\nconclusion.tex line 5: \"Vision encoder quality emerges as a key design lever\" — 此 claim 在上轮两位 reviewer 的交叉审查中被质疑（RSA 最高 vs R² 最高指向不同表征），修订后未修改。但因 conclusion.tex 未编译，此问题暂不影响已编译的论文。\n\n---\n\n## Updated Assessment\n\n```\nScore: 6/10 (vs 上轮 5/10)\nDirection: ↑ (小幅上升)\n```\n\n**评分理由**:\n\n**上升因素**:\n- R6-C2 完全解决（demo-level split，R² 现为 held-out 值）→ 消除了 probe 结果可信度的根本疑虑\n- R6-W1 完全解决（task-level block resampling + Nili 2014）\n- Action trajectory analysis 虽非 behavioral validation 但提供了 output-level 因果证据\n- Abstract 修改改善了 claim scope（\"in the model studied\"、C1 降格为 \"validate\"）\n- GenAI 声明已添加\n- \"routing-first specialization\" 比 \"dual function\" 更准确（虽仍不完全 convincing）\n\n**限制上升幅度的因素**:\n- R6-C1 核心矛盾未解决（all ablation increase R²，Discussion 自相矛盾）\n- R6-C4 仍无 behavioral validation（trajectory analysis ≠ rollout success）\n- N=10 random subsets 未增加\n- 单模型+单 benchmark 的 generalization 问题未改变（上轮 W6，无法在修订期间解决）\n- Linear vs MLP 20× gap 仍未在正文讨论\n\n**总结**: 方法论层面的两个关键修复（probe split 和 RSA bootstrap）显著提升了统计推断的可信度，使 Finding 2（routing reorganization）和 Finding 3（inverted-U）的定量证据更可信。但 ablation 的因果推断逻辑和 behavioral validation 缺口仍是影响接收决定的 open issues。论文从 \"marginally below\" 升至 \"marginally above\"，条件是：(a) ablation 的 claim scope 需要缩小/限定；(b) behavioral gap 需在 Limitations 中更坦诚讨论。\n\n**Confidence**: 4/5 (confident)\n",
  "reviewer_id": "1",
  "project": "vla-ssd"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 — Round 2 修订评估\n\n---\n\n## Issue Verification\n\n### R6-C1 [CRITICAL]: Ablation 因果推断方向问题 — [STILL_OPEN] (partially improved)\n\n**修改内容确认**:\n- Section 4.3 ¶4 (line 80): \"dual routing-encoding function\" → \"routing-first specialization\"，新解释为 dominant heads 携带 organized instruction signals 被 probe 视为 structured noise，因此 ablation 增幅较小\n- 新增 \"Action trajectory validation\"（lines 83-87）: L1 ablation 改变 72.3% action tokens (d=0.65)，control ablation d=0.41; gripper dimension 主导效应 (shift 0.291 vs <0.034)\n- Appendix A.6: per-dimension 分析，per-task Cohen's d (0.43-0.73)，KL divergence (5.08 vs 1.69)\n\n**仍存在的问题**:\n\n(a) **核心矛盾未解决**: ALL ablation（dominant 和 random）仍然 increase R²。\"Routing-first specialization\" 是对 \"dual function\" 的措辞改进，但逻辑结构相同——仍是对 \"为什么 dominant heads ablation 增幅更小\" 的 post-hoc 解释，未正面回答 \"为什么移除任何 24/32 heads 都提升 action prediction\" 这个根本问题。\n\n(b) **Discussion 的自相矛盾**: Discussion line 12 写 \"the effect distributes across L1 heads rather than concentrating in instruction-dominant ones\"。如果 ablation 效应均匀分布在所有 L1 heads 上（而非集中在 instruction-dominant heads），这恰恰削弱了 \"routing-first specialization\" 的 claim——因为 instruction-dominant heads 没有表现出与其他 heads 不同的特殊功能。\n\n(c) **N=10 random subsets 未增加**: 仍然是 10 个随机子集的 z-test。上轮我和 R2 都指出这个样本量对统计推断不足。未修改。\n\n(d) **效应范围窄于 claim**: 新的 trajectory analysis 揭示效应主要集中在 gripper dimension (0.291 vs continuous dimensions <0.034)。这意味着 L1 instruction routing 的 \"causal role\" 主要影响 discrete open/close 决策，而非连续运动控制。但正文仍将其叙述为 general \"routing function\"，未缩小 claim scope。\n\n**积极改进**: Trajectory analysis 本身有价值——从 representation-level（probe R²）推进到 output-level（action token prediction），是正确方向。但不足以完全 resolve 因果推断问题。\n\n**建议**: (a) 正文中显式承认 \"所有 24-head ablation 均提高 R²\" 这一事实并讨论其含义（如 L1 heads 可能普遍冗余）；(b) 增加 random subsets 至 ≥50；(c) 限定 claim scope 至 gripper/discrete 控制。\n\n---\n\n### R6-C2 [CRITICAL]: Probe train/test split + 时间自相关 — [RESOLVED]\n\n**修改内容确认**:\n- Method §3.6 line 59: \"Probes are trained on demos 0-39 and evaluated on held-out demos 40-49 (demo-level split), ensuring zero temporal overlap between training and evaluation trajectories.\"\n\n**评估**:\n- Demo-level split 完全消除了时间泄漏（不同 demo 之间无时间连续性）\n- 80/20 split (40 train / 10 test per task) 是合理比例\n- R² 现在明确是 held-out 数据上的值，解决了上轮对 overparameterized MLP probe R² 可信度的核心担忧\n- Section 4.1 line 12 对 overparameterization 的讨论已有，指向 linear probe 复制\n\n**残余小问题**: Linear vs MLP 20× gap（Δ = +0.324 vs +0.015）仍未在主正文中讨论。Appendix A.6 的 framing（\"VLA training reorganizes representations to make action information more linearly decodable\"）是一种合理解释但排除了替代解释（MLP 过于强大压缩了条件间差异）。这是 [INFO] 级别问题，不阻碍接收。\n\n---\n\n### R6-C4 [CRITICAL]: 缺 behavioral validation — [STILL_OPEN] (partially improved)\n\n**修改内容确认**:\n- 新增 \"Action trajectory validation\"（Section 4.3, lines 83-87）\n- MuJoCo 版本不匹配导致无法 rollout\n\n**评估**:\n\n(a) **Open-loop trajectory analysis 不是 behavioral validation**。它测量的是 \"ablation 改变了模型的 action token 预测\"，这是 output-level 证据而非 behavioral 证据。真正的 behavioral validation 需要 closed-loop rollout：在环境中执行修改后的 action 序列并测量 task success rate。\n\n(b) **对 CoRL 仍是显著缺口**: Cohen's d = 0.65 和 72.3% token divergence 告诉我们 ablation 改变了预测，但不知道预测变好还是变差。可能 ablation 后的 actions 更好（R² 增加暗示如此），也可能在实际环境中因失去 instruction conditioning 而失败。\n\n(c) **进步方向正确**: 从纯 representation-level（R², RSA ρ）推进到 output-level（action token comparison）是有意义的改善。MuJoCo 版本限制是可理解的技术障碍。\n\n(d) **建议**: 如果 closed-loop rollout 确实不可行，至少在 Discussion/Limitations 中明确承认这一 gap 并讨论 output-level 与 behavioral-level 证据的区别。当前 Discussion（line 12）将 trajectory analysis 描述为 \"confirms the causal role\"，这对 \"causal role\" 的定义过宽。\n\n---\n\n### R6-W1 [WARNING]: RSA pairwise dependency — [RESOLVED]\n\n**修改内容确认**:\n- Method §3.5 line 51: \"resampling is performed at the task level (N=10), treating each task's pairwise RDM entries as a block to preserve within-task dependency structure [nili2014toolbox].\"\n\n**评估**:\n- Task-level block resampling 是处理 RDM pairwise dependency 的标准做法（Nili et al. 2014）\n- 引用正确的方法论文献\n- 这解决了核心统计问题：不再将非独立的 pairwise distances 当作独立样本\n\n**残余注意**: N=10 tasks 的 bootstrap 功效有限（10^10 种可能的重抽样中很多高度相似），但这是实验设计的固有限制（LIBERO 只有 10 tasks），非方法论错误。论文应意识到这使得 CI 偏宽，但不需要额外修改。\n\n---\n\n## 上轮 W3（MLP probe overparameterization）检查\n\n- **主正文**: Section 4.1 line 12 承认 overparameterized 并指向 linear probe。未讨论 20× gap。\n- **Appendix A.6**: 讨论了 gap 但 framing 单一（仅 \"linear decodability\" 解释）\n- **评估**: 现在 R² 是 held-out 数据上的值（R6-C2 resolved），overparameterization 的实际危害已大幅降低。20× gap 的 under-discussion 降级为 minor concern。\n\n---\n\n## New Issues\n\n### N1 [WARNING]: Discussion 中的自相矛盾\n\nDiscussion line 12: \"the effect distributes across L1 heads rather than concentrating in instruction-dominant ones, yet L0-L1 routing concentration suggests early-layer parameters may suffice for adaptation.\"\n\n这两个半句互相矛盾：\n- 前半句说 ablation 效应均匀分布（不集中在 instruction-dominant heads）\n- 后半句仍然推论 L0-L1 instruction routing 的特殊意义\n\n如果 ablation 效应不集中在 instruction-dominant heads，那么 \"routing concentration\" 的功能特异性就被削弱了。这里需要更 careful 的逻辑连接。\n\n### N2 [INFO]: conclusion.tex 仍未编译\n\nmain.tex 仍然不包含 `\\input{conclusion}`。R2 上轮指出的 W8 未修复。虽然 Discussion 末尾有总结性内容，但结构不完整。\n\n### N3 [INFO]: Conclusion 中的 claim 未更新\n\nconclusion.tex line 5: \"Vision encoder quality emerges as a key design lever\" — 此 claim 在上轮两位 reviewer 的交叉审查中被质疑（RSA 最高 vs R² 最高指向不同表征），修订后未修改。但因 conclusion.tex 未编译，此问题暂不影响已编译的论文。\n\n---\n\n## Updated Assessment\n\n```\nScore: 6/10 (vs 上轮 5/10)\nDirection: ↑ (小幅上升)\n```\n\n**评分理由**:\n\n**上升因素**:\n- R6-C2 完全解决（demo-level split，R² 现为 held-out 值）→ 消除了 probe 结果可信度的根本疑虑\n- R6-W1 完全解决（task-level block resampling + Nili 2014）\n- Action trajectory analysis 虽非 behavioral validation 但提供了 output-level 因果证据\n- Abstract 修改改善了 claim scope（\"in the model studied\"、C1 降格为 \"validate\"）\n- GenAI 声明已添加\n- \"routing-first specialization\" 比 \"dual function\" 更准确（虽仍不完全 convincing）\n\n**限制上升幅度的因素**:\n- R6-C1 核心矛盾未解决（all ablation increase R²，Discussion 自相矛盾）\n- R6-C4 仍无 behavioral validation（trajectory analysis ≠ rollout success）\n- N=10 random subsets 未增加\n- 单模型+单 benchmark 的 generalization 问题未改变（上轮 W6，无法在修订期间解决）\n- Linear vs MLP 20× gap 仍未在正文讨论\n\n**总结**: 方法论层面的两个关键修复（probe split 和 RSA bootstrap）显著提升了统计推断的可信度，使 Finding 2（routing reorganization）和 Finding 3（inverted-U）的定量证据更可信。但 ablation 的因果推断逻辑和 behavioral validation 缺口仍是影响接收决定的 open issues。论文从 \"marginally below\" 升至 \"marginally above\"，条件是：(a) ablation 的 claim scope 需要缩小/限定；(b) behavioral gap 需在 Limitations 中更坦诚讨论。\n\n**Confidence**: 4/5 (confident)\n",
    "reviewer_id": "1",
    "project": "vla-ssd"
  }
}
````

</details>

---


### Tool result

_source line 232 · 2026-05-18T13:39:07.488106+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4064
}
```

</details>

---


### Assistant

_source line 233 · 2026-05-18T13:39:14.212761+00:00_

Round 2 修订评估已提交。

核心结论：
- **R6-C2 (probe split)** 和 **R6-W1 (RSA bootstrap)** 已完全解决
- **R6-C1 (ablation)** 部分改善但核心矛盾未解——所有 ablation 增加 R² 的事实未正面回应，Discussion 存在自相矛盾
- **R6-C4 (behavioral validation)** 部分改善——trajectory analysis 提供 output-level 证据，但非 behavioral validation
- 评分从 5/10 上升至 6/10（marginally above threshold），方向 ↑

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1"
}
```

</details>

---


## Round 12

## Round 12

4 recorded events


### User

_source line 234 · 2026-05-18T13:40:13.851626+00:00_

[Round 2 审稿请求]:
## Step 2 交叉分享 — 请回应 Reviewer 2 的 Round 2 评估

R2 评分从 4/10 上升至 5/10 (Borderline)。以下是 R2 的关键判断，请逐条 [AGREE] 或 [REBUT]。

---

### Issue Verification 差异

**R6-C1 (Ablation)**: R2 将严重程度从 CRITICAL 降为 WARNING。理由：新叙事更准确，trajectory validation 增加了因果证据。但 R2 指出两个新问题：
1. R² ablation 测连续动作维度（improvement），trajectory analysis 测离散 gripper 维度（divergence）——两个结果讲不同故事，论文未讨论这一维度分离
2. Line 86 "Per-head effects are comparable" 实际上 undermines instruction-dominant heads 作为 functionally distinct group 的叙事

**你上轮保持 CRITICAL**，R2 降为 WARNING。你同意降级还是维持 CRITICAL？

**R6-C3 (Overclaim)**: R2 降为 WARNING。Abstract 改善，但 Introduction lines 16-20 的 "Three findings emerge" 仍用一般化语言，Contribution (i) 和 (iii) 仍无 model-specific qualification。你上轮未单独追踪此 issue——你同意 R2 的评估吗？

**R6-C4 (Behavioral validation)**: R2 保持 CRITICAL。理由：
- Open-loop trajectory ≠ closed-loop task success
- 72.3% token divergence 不知道是变好还是变差
- Limitations 未明确承认 behavioral validation 缺失
- "early-layer parameters may suffice" 仍 speculative

你上轮也标 STILL_OPEN 但未明确 severity。你同意保持 CRITICAL 还是降级？

### R2 新发现

**N1 [WARNING]: R² vs trajectory 维度分离**——gripper shift 0.291 vs continuous <0.034。这是否对 "routing-first" 解释产生重大影响？

**N2 [INFO]: Per-head comparability undermines dominant-head narrative**——如果所有 heads per-head effect 类似，instruction-dominant heads 的特殊地位何在？

### R2 的 Persistent Issues

**P1**: C1 仍作为 compound contribution (framework + verification) 在 Contribution (i) 中，建议拆开
**P2**: CKA 矛盾仍未在正文充分讨论（仅 Appendix 指针）
**P3**: conclusion.tex 仍未编译（你也在 N2 中指出）

### 评分对比
- 你: 6/10 (↑ from 5)
- R2: 5/10 (↑ from 4)

请就上述差异点给出 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 235 · 2026-05-18T13:41:23.594658+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 交叉回应 — 对 Reviewer 2 Round 2 评估\n\n---\n\n## Issue Verification 差异\n\n### R6-C1 (Ablation): R2 降为 WARNING vs 我保持 CRITICAL — [PARTIAL AGREE, 降为 WARNING]\n\n经过 R2 的分析，我同意将 severity 从 CRITICAL 降为 WARNING，理由如下：\n\n(a) **新增 trajectory analysis 确实增加了因果证据层**。虽然不完美，但 output-level 证据（d=0.65, 72.3% token divergence, KL=5.08 vs 1.69）补充了纯 representation-level 分析，使因果推断从\"仅有相关性\"升级为\"相关性 + output-level 影响\"。这足以将 severity 从 CRITICAL（阻碍接收）降至 WARNING（影响评分但不一票否决）。\n\n(b) 但我**完全同意 R2 新发现的两个问题**：\n\n- **R2-N1（维度分离）**: R² ablation 的 improvement 主要反映连续动作维度（因为 R² 是 7-D 均值），而 trajectory 的 divergence 主要来自 gripper（shift 0.291 vs <0.034）。两个结果确实在讲不同维度的故事，但论文将它们并列呈现仿佛互相支撑。这个 gap 需要正文讨论。\n\n- **R2-N2（Per-head comparability）**: Section 4.3 line 86 \"Per-head effects are comparable\" 是修改中引入的新问题。如果每个 head 的 per-head ablation 效应类似（无论是否 instruction-dominant），那么 instruction-dominant heads 作为 functionally distinct group 的叙事就失去了基础。\"Routing-first specialization\" 隐含 \"这些 heads 在功能上与其他 heads 不同\"，但 per-head comparability 正好说明它们在 ablation 效应上并不特殊。我在 Round 2 报告的 N1（Discussion 自相矛盾）本质上指出了同一问题。\n\n**结论**: 降为 WARNING。Ablation 的核心逻辑仍有问题（all increase R²、per-head comparability、维度分离），但 trajectory analysis 提供了有意义的补充证据，使这不再是 reject-level 的致命缺陷，而是需要在 claim scope 上做限定的问题。\n\n---\n\n### R6-C3 (Overclaim): — [AGREE]\n\n同意 R2 的评估。我在 Round 1 将 overclaim 分散在多个 weakness 中讨论（W1 的 C1 novelty、W5 的 C3 metric-dependency、W6 的 generalization），未单独追踪。R2 的系统性检查更好：\n\n- Abstract line 7 已改善（\"in the model studied\"）— 正面确认\n- Introduction lines 16-20 \"Three findings emerge\" 仍用一般化语言，无 model-specific 限定 — 问题存在\n- Contribution (i) \"verifying architecture-expected specialization between image and readout tokens\" 未限定模型 — 虽然此条本身是架构通用的（causal mask 对所有 decoder-only VLA 成立），但措辞暗示这是 empirical 验证而非逻辑推导\n- Contribution (iii) \"vision encoder representations are non-monotonically transformed by the LLM\" 也未加 model-specific 限定\n\nWARNING 级别合理。修复成本低（加几个 \"in OpenVLA-7B\" / \"on LIBERO\"），但当前状态下确实影响审稿人对 claim 诚实度的判断。\n\n---\n\n### R6-C4 (Behavioral validation): — [AGREE, 保持 CRITICAL]\n\n同意 R2 保持 CRITICAL。我的 Round 2 标注为 \"STILL_OPEN (partially improved)\" 但未明确 severity。现在明确：\n\n(a) **对 CoRL 来说 behavioral validation 是 critical bar**。CoRL 审稿维度明确包含 \"relevance to robot learning\"，纯 representational findings 无 behavioral 连接对 robotics venue 是显著缺陷。\n\n(b) R2 的论证精确：72.3% token divergence 不知道是变好还是变差。如果 ablation 后的 action sequence 实际上更好（R² 增加暗示如此），那意味着 instruction routing 对 action quality 是有害的——这会颠覆论文的核心叙事。如果更差，那需要 rollout 证明。两种可能性都对论文的 story 不利，而作者没有数据来区分。\n\n(c) Discussion line 12 \"Action trajectory analysis confirms the causal role\" 中 \"causal role\" 的措辞过强。Trajectory analysis 确认了 L1 ablation 影响了 output，但未确认影响的方向（正面还是负面）。\"Causal influence\" 比 \"causal role\" 更准确。\n\n(d) Limitations（Discussion line 14-15）仍未明确承认 behavioral validation 缺失。只说 \"C2 may differ across backbone scales and decoder paradigms\"，这是 generalization 的 limitation，不是 behavioral gap 的 limitation。\n\n**结论**: 保持 CRITICAL。MuJoCo 版本限制是可理解的技术障碍，但论文需要至少在 Limitations 中明确承认 \"our analyses are representational; connecting these findings to task success requires closed-loop evaluation, which we leave to future work\"。当前的 Limitations 段落回避了这个问题。\n\n---\n\n## R2 Persistent Issues\n\n### P1 (C1 作为 compound contribution) — [AGREE]\n\n将 \"framework\" 和 \"architecture verification\" 拆分为独立贡献是合理建议。当前 Contribution (i) 同时 claim \"systematic experimental framework\" 和 \"verifying architecture-expected specialization\"。前者是方法论贡献（framework 可用于其他 VLA），后者是 empirical sanity check。合并后读起来像是一个 contribution，但实质是两个不同性质的 claim——一个有持久价值，一个是 trivial verification。拆分后更诚实。\n\n### P2 (CKA 矛盾仅在 Appendix 讨论) — [AGREE with nuance]\n\n主要同意。正文 Section 3.6 line 64-66 现在扩展了 RSA over CKA 的 justification（\"it captures the relative distance structure among representations, which directly governs action prediction quality\"），这是一个改进。但 \"directly governs action prediction quality\" 是一个需要 empirical 支撑的 claim，而非不证自明的事实——CKA 拥护者可以同样论证 global subspace overlap 与 downstream performance 更相关。\n\n正文中应至少用一句话承认 CKA 给出不同 story（目前完全依赖 Appendix 指针），让读者不读 Appendix 也能知道 Finding 3 的 metric-dependency。\n\n### P3 (conclusion.tex 未编译) — [AGREE]\n\n我在 Round 2 N2 中也指出了这个问题。main.tex 仍无 `\\input{conclusion}`。Discussion 末段有总结功能但缺少独立 Conclusion section。修复成本极低。\n\n---\n\n## 评分差异讨论\n\nR2: 5/10, 我: 6/10。差距为 1 分。\n\n**差异来源**: 我给 6 的主要理由是 R6-C2（probe split）和 R6-W1（RSA bootstrap）的完全解决显著提升了 Finding 2 和 Finding 3 定量结论的可信度。R2 可能更看重 behavioral validation gap（保持 CRITICAL）和 overclaim（systematic tracking），这些问题确实未改善。\n\n**经过交叉讨论后的调整**: 我同意将 R6-C4 维持 CRITICAL 和 R6-C1 降为 WARNING。综合来看：\n- 1 个 CRITICAL 仍 open (behavioral validation)\n- 2 个 WARNING 仍 open (ablation logic + overclaim)\n- 2 个 RESOLVED (probe split + RSA bootstrap)\n- 多个 INFO 级别 issues\n\n这个 profile 对应 borderline 到 marginally above。我维持 6/10 但承认 5/10 也有合理依据——取决于审稿人对 \"CoRL 是否接受无 behavioral validation 的纯分析论文\" 这个 meta-question 的判断。如果 CoRL AC 认为 behavioral evidence 是 hard requirement，论文在 5 以下；如果分析框架本身有价值且修复路径清晰，6 合理。\n\n**最终评分**: 6/10 (Marginally above acceptance threshold)\n**Confidence**: 4/5\n",
  "reviewer_id": "1",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 交叉回应 — 对 Reviewer 2 Round 2 评估\n\n---\n\n## Issue Verification 差异\n\n### R6-C1 (Ablation): R2 降为 WARNING vs 我保持 CRITICAL — [PARTIAL AGREE, 降为 WARNING]\n\n经过 R2 的分析，我同意将 severity 从 CRITICAL 降为 WARNING，理由如下：\n\n(a) **新增 trajectory analysis 确实增加了因果证据层**。虽然不完美，但 output-level 证据（d=0.65, 72.3% token divergence, KL=5.08 vs 1.69）补充了纯 representation-level 分析，使因果推断从\"仅有相关性\"升级为\"相关性 + output-level 影响\"。这足以将 severity 从 CRITICAL（阻碍接收）降至 WARNING（影响评分但不一票否决）。\n\n(b) 但我**完全同意 R2 新发现的两个问题**：\n\n- **R2-N1（维度分离）**: R² ablation 的 improvement 主要反映连续动作维度（因为 R² 是 7-D 均值），而 trajectory 的 divergence 主要来自 gripper（shift 0.291 vs <0.034）。两个结果确实在讲不同维度的故事，但论文将它们并列呈现仿佛互相支撑。这个 gap 需要正文讨论。\n\n- **R2-N2（Per-head comparability）**: Section 4.3 line 86 \"Per-head effects are comparable\" 是修改中引入的新问题。如果每个 head 的 per-head ablation 效应类似（无论是否 instruction-dominant），那么 instruction-dominant heads 作为 functionally distinct group 的叙事就失去了基础。\"Routing-first specialization\" 隐含 \"这些 heads 在功能上与其他 heads 不同\"，但 per-head comparability 正好说明它们在 ablation 效应上并不特殊。我在 Round 2 报告的 N1（Discussion 自相矛盾）本质上指出了同一问题。\n\n**结论**: 降为 WARNING。Ablation 的核心逻辑仍有问题（all increase R²、per-head comparability、维度分离），但 trajectory analysis 提供了有意义的补充证据，使这不再是 reject-level 的致命缺陷，而是需要在 claim scope 上做限定的问题。\n\n---\n\n### R6-C3 (Overclaim): — [AGREE]\n\n同意 R2 的评估。我在 Round 1 将 overclaim 分散在多个 weakness 中讨论（W1 的 C1 novelty、W5 的 C3 metric-dependency、W6 的 generalization），未单独追踪。R2 的系统性检查更好：\n\n- Abstract line 7 已改善（\"in the model studied\"）— 正面确认\n- Introduction lines 16-20 \"Three findings emerge\" 仍用一般化语言，无 model-specific 限定 — 问题存在\n- Contribution (i) \"verifying architecture-expected specialization between image and readout tokens\" 未限定模型 — 虽然此条本身是架构通用的（causal mask 对所有 decoder-only VLA 成立），但措辞暗示这是 empirical 验证而非逻辑推导\n- Contribution (iii) \"vision encoder representations are non-monotonically transformed by the LLM\" 也未加 model-specific 限定\n\nWARNING 级别合理。修复成本低（加几个 \"in OpenVLA-7B\" / \"on LIBERO\"），但当前状态下确实影响审稿人对 claim 诚实度的判断。\n\n---\n\n### R6-C4 (Behavioral validation): — [AGREE, 保持 CRITICAL]\n\n同意 R2 保持 CRITICAL。我的 Round 2 标注为 \"STILL_OPEN (partially improved)\" 但未明确 severity。现在明确：\n\n(a) **对 CoRL 来说 behavioral validation 是 critical bar**。CoRL 审稿维度明确包含 \"relevance to robot learning\"，纯 representational findings 无 behavioral 连接对 robotics venue 是显著缺陷。\n\n(b) R2 的论证精确：72.3% token divergence 不知道是变好还是变差。如果 ablation 后的 action sequence 实际上更好（R² 增加暗示如此），那意味着 instruction routing 对 action quality 是有害的——这会颠覆论文的核心叙事。如果更差，那需要 rollout 证明。两种可能性都对论文的 story 不利，而作者没有数据来区分。\n\n(c) Discussion line 12 \"Action trajectory analysis confirms the causal role\" 中 \"causal role\" 的措辞过强。Trajectory analysis 确认了 L1 ablation 影响了 output，但未确认影响的方向（正面还是负面）。\"Causal influence\" 比 \"causal role\" 更准确。\n\n(d) Limitations（Discussion line 14-15）仍未明确承认 behavioral validation 缺失。只说 \"C2 may differ across backbone scales and decoder paradigms\"，这是 generalization 的 limitation，不是 behavioral gap 的 limitation。\n\n**结论**: 保持 CRITICAL。MuJoCo 版本限制是可理解的技术障碍，但论文需要至少在 Limitations 中明确承认 \"our analyses are representational; connecting these findings to task success requires closed-loop evaluation, which we leave to future work\"。当前的 Limitations 段落回避了这个问题。\n\n---\n\n## R2 Persistent Issues\n\n### P1 (C1 作为 compound contribution) — [AGREE]\n\n将 \"framework\" 和 \"architecture verification\" 拆分为独立贡献是合理建议。当前 Contribution (i) 同时 claim \"systematic experimental framework\" 和 \"verifying architecture-expected specialization\"。前者是方法论贡献（framework 可用于其他 VLA），后者是 empirical sanity check。合并后读起来像是一个 contribution，但实质是两个不同性质的 claim——一个有持久价值，一个是 trivial verification。拆分后更诚实。\n\n### P2 (CKA 矛盾仅在 Appendix 讨论) — [AGREE with nuance]\n\n主要同意。正文 Section 3.6 line 64-66 现在扩展了 RSA over CKA 的 justification（\"it captures the relative distance structure among representations, which directly governs action prediction quality\"），这是一个改进。但 \"directly governs action prediction quality\" 是一个需要 empirical 支撑的 claim，而非不证自明的事实——CKA 拥护者可以同样论证 global subspace overlap 与 downstream performance 更相关。\n\n正文中应至少用一句话承认 CKA 给出不同 story（目前完全依赖 Appendix 指针），让读者不读 Appendix 也能知道 Finding 3 的 metric-dependency。\n\n### P3 (conclusion.tex 未编译) — [AGREE]\n\n我在 Round 2 N2 中也指出了这个问题。main.tex 仍无 `\\input{conclusion}`。Discussion 末段有总结功能但缺少独立 Conclusion section。修复成本极低。\n\n---\n\n## 评分差异讨论\n\nR2: 5/10, 我: 6/10。差距为 1 分。\n\n**差异来源**: 我给 6 的主要理由是 R6-C2（probe split）和 R6-W1（RSA bootstrap）的完全解决显著提升了 Finding 2 和 Finding 3 定量结论的可信度。R2 可能更看重 behavioral validation gap（保持 CRITICAL）和 overclaim（systematic tracking），这些问题确实未改善。\n\n**经过交叉讨论后的调整**: 我同意将 R6-C4 维持 CRITICAL 和 R6-C1 降为 WARNING。综合来看：\n- 1 个 CRITICAL 仍 open (behavioral validation)\n- 2 个 WARNING 仍 open (ablation logic + overclaim)\n- 2 个 RESOLVED (probe split + RSA bootstrap)\n- 多个 INFO 级别 issues\n\n这个 profile 对应 borderline 到 marginally above。我维持 6/10 但承认 5/10 也有合理依据——取决于审稿人对 \"CoRL 是否接受无 behavioral validation 的纯分析论文\" 这个 meta-question 的判断。如果 CoRL AC 认为 behavioral evidence 是 hard requirement，论文在 5 以下；如果分析框架本身有价值且修复路径清晰，6 合理。\n\n**最终评分**: 6/10 (Marginally above acceptance threshold)\n**Confidence**: 4/5\n",
    "reviewer_id": "1",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 236 · 2026-05-18T13:41:27.471448+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3876
}
```

</details>

---


### Assistant

_source line 237 · 2026-05-18T13:41:32.926306+00:00_

Round 2 交叉回应已提交。

核心判断：同意 R2 将 R6-C1 (ablation) 降为 WARNING、R6-C4 (behavioral validation) 保持 CRITICAL。维持 6/10 评分，与 R2 的 5/10 差距主要在于对 probe split 和 RSA bootstrap 修复带来的可信度提升的权重不同。最终评价取决于 CoRL AC 对纯分析论文是否需要 behavioral evidence 的 meta-level 判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1"
}
```

</details>

---


## Round 13

## Round 13

14 recorded events


### User

_source line 238 · 2026-05-18T14:11:34.845842+00:00_

[Round 8 审稿请求]:
# Round 8 — Reviewer 1 任务（方法/实验严谨性）

**模式**: 继续审稿（验证 Round 7 open issues 的修复）
**Venue**: CoRL 2026, 8 pages + unlimited refs, double-blind
**论文路径**: `projects/vla-ssd/docs/paper/main.tex`

## 你的任务

逐条验证以下 in_progress issues 是否已充分修复。每条标 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由。同时检查修改是否引入新问题。

---

## Open Issues 清单

### 🔴 R6-C4 [CRITICAL] 缺 behavioral validation
**Round 7 诊断**: Discussion "confirms the causal role" 过强；Limitations 未承认 behavioral gap。
**预期修复**: (P1) Discussion 弱化措辞；(P2) Limitations 新增 behavioral gap 声明。
**验证要点**:
- 读 Discussion 全文，检查是否仍有过强的因果措辞（特别关注 "establishing"/"confirms"/"proves" 等词）
- 读 Limitations 段落，检查是否明确承认 open-loop 限制
- 评估修复是否充分降低了 CoRL 审稿人的 rejection risk

### 🟡 R6-C1 [WARNING] Ablation 因果推断 + internal inconsistency
**Round 7 诊断**: (a) R² 测连续维度 vs trajectory 测 gripper 维度未讨论；(b) per-head effects comparable 削弱 dominant-head 叙事；(c) Discussion 自相矛盾。
**预期修复**: (P5) 正文讨论维度分离；(P6) Discussion 重写 attention/ablation interpretation。
**验证要点**:
- 读 Discussion "Mechanistic interpretation" 段落，检查维度分离是否有合理解释
- 检查 "collective role" 叙事是否与 Experiments 的 "per-head effects are comparable" 一致
- 检查新 Discussion 是否消除了 Round 7 的自相矛盾

### 🟡 R7-W1 [WARNING] 维度分离未讨论
**与 R6-C1 合并验证**。检查 Discussion 是否讨论 R² (continuous) vs trajectory (gripper) 的分离。

### 🟡 R7-W2 [WARNING] Per-head comparability + Discussion 矛盾
**与 R6-C1 合并验证**。检查 "effect distributes across L1 heads" 与 routing concentration 的逻辑是否自洽。

### ℹ️ R5-N4 [WARNING, in_progress] Behavioral gap in Limitations
**与 R6-C4 合并验证**。

---

## 也请检查

1. **新 Discussion 结构的整体连贯性**: Synthesis → Mechanistic interpretation → Predictions → Limitations。逻辑链是否通畅？
2. **Predictions 段落** (新增): 是否过度推测？是否有足够证据支撑？
3. **Experiments 是否有冗余或遗漏**: ablation + trajectory 段落是否仍 self-consistent？
4. **修改是否引入新的 overclaim 或逻辑断裂**

## 输出格式

```
## Issue Verification
[逐条 RESOLVED/STILL_OPEN]

## New Issues (if any)
[新发现]

## Discussion Quality Assessment
[新 Discussion 结构评价]

## Score
[评分 /10 + 理由]
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 239 · 2026-05-18T14:11:46.214006+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 240 · 2026-05-18T14:11:46.264649+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Synthesis.}
5	Image tokens remain instruction-blind; the readout is the sole multimodal convergence point.
6	Training shifts routing from mid-depth to entry-exit (L0--L1, L31), with effects at the readout ($R^2$ $+0.069$) rather than images ($\Delta \leq 1.7\%$).
7	This explains the visual dominance of Grant et al.~\cite{grant2026}: DINOv2 has the highest geometric alignment ($\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\ $0.634$).
8	Two independent analyses converge on L1 as the routing hub: attention shows training-dependent entry-exit reorganization (\S\ref{sec:learned_routing}), and representational probes show a cross-layer ablation gradient confined to L1 ($R^2$ $+0.059$ at L1 vs.\ $+0.018$ at L8 vs.\ $\approx 0$ at L13). Action trajectory analysis further confirms that L1 ablation alters $72.3\%$ of tokens ($d = 0.65$), establishing a causal link from routing to output.
9	
10	\paragraph{Mechanistic interpretation.}
11	Per-layer RSA bifurcates after L12 (Figure~\ref{fig:rsa_perlayer_curve}): readout $\rho$ declines gradually while image\_mean drops sharply ($\to 0.422$), consistent with mid-layer integration and deep-layer compression.
12	L1 ablation demonstrates causal influence on action output ($z = -2.73$ vs.\ random subsets) and is L1-confined ($|\Delta R^2| < 0.02$ at deeper layers).
13	The $R^2$ improvement reflects information gain in continuous dimensions (removing routing signals frees bandwidth), while the gripper-concentrated trajectory effect ($72.3\%$ divergence) reflects discrete manipulation sensitivity.
14	The attention analysis reveals what the model learns (reorganized routing), while ablation reveals how the function is implemented (distributed across the layer). Routing reorganization is the observable signature of L1's acquired collective role, not a property of individual heads.
15	
16	\paragraph{Predictions.}
17	Other decoder-only VLAs (e.
…[truncated 1027 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 241 · 2026-05-18T14:11:46.265059+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 242 · 2026-05-18T14:11:46.517317+00:00_

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
12	This yields $N = 63{,}228$ observations; all patterns reproduce with a linear probe (Appendix~\ref{sec:linear_probe}).
13	
14	%------------------------------------------------------------------
15	\subsection{Token-Level Functional Specialization}
16	\label{sec:token_specialization}
17	
18	We train cross-instruction probes (\S\ref{sec:cross_instruction_probes}): given the same visual frame with each of 10 task instructions, we classify which instruction was present from per-layer activations.
19	
20	\paragraph{Image tokens are instruction-blind.}
21	Image\_mean instruction classification remains at chance ($10\%$) across all 32 layers in all conditions (Table~\ref{tab:dense_routing_main}), consistent with the causal mask and frozen encoder.
22	Both linear and MLP probes confirm this, as does standalone DINOv2 ($10\%$), ruling out probe capacity.

…[truncated 10100 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 243 · 2026-05-18T14:11:53.154483+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 244 · 2026-05-18T14:11:53.707568+00:00_

1	Vision-language-action models (VLAs) fine-tune large language models (LLMs) on robot demonstrations, but how training reshapes information routing at the token level remains uncharacterized.
2	We present a systematic experimental framework for token-level analysis of VLAs, applying cross-instruction probes, attention analysis, Representational Similarity Analysis (RSA), and functional probes across all 32 LLM layers of OpenVLA-7B on LIBERO, with factorial trained/pretrained/untrained controls.
3	Three findings emerge.
4	First, we validate the framework by confirming architecture-expected token specialization: image tokens are instruction-blind (classification at chance across all layers and conditions), while the readout token serves as the sole multimodal convergence point ($100\%$ instruction classification from L1, cross-validated).
5	Second, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth, while VLA training shifts this to entry-layer routing (L0--L1) with exit-layer re-engagement (L31); instruction classification reaches $99.6\%$ at L1 (vs.\ pretrained $80.2\%$), and L1 ablation confirms routing-first head specialization (random-subset control, L1-confined). Untrained models show zero instruction-dominant heads throughout.
6	Third, vision encoder representations follow a metric-dependent non-monotonic trajectory through LLM layers ($R^2$ peaks at L8--L14; RSA confirms but CKA diverges; Appendix).
7	Training effects concentrate at the readout token (probe $R^2$ $+0.069$, instruction attention $+46$pp) rather than visual geometry ($\Delta\rho \leq 0.017$, non-significant); instruction routing reorganization is the primary learned contribution of fine-tuning in the model studied.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 245 · 2026-05-18T14:11:53.758839+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 246 · 2026-05-18T14:11:53.810779+00:00_

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
…[truncated 2307 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 247 · 2026-05-18T14:11:53.862146+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 248 · 2026-05-18T14:11:53.912886+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 249 · 2026-05-18T14:13:37.827224+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

````json
{
  "text": "\n# Reviewer 1 — Round 8 修订评估\n\n---\n\n## Issue Verification\n\n### 🔴 R6-C4 [CRITICAL]: 缺 behavioral validation — [RESOLVED as WARNING]\n\n**修改确认**:\n- Discussion line 12: \"confirms the causal role\" → \"demonstrates causal influence on action output\"。措辞从 \"confirms\" 降为 \"demonstrates\"，不再隐含因果链已完全建立。\n- Limitations line 22（新增）: \"Our analyses are representational and open-loop; connecting routing reorganization to task success requires closed-loop evaluation, which we leave to future work.\"\n- Predictions line 18: \"L1 ablation on a fine-tuned model should produce measurable task degradation, particularly on instruction-discriminative tasks\" — 将 behavioral 验证定位为可验证的 prediction 而非已有结论。\n\n**评估**:\n- P2（Limitations 声明）**完全达标**。Line 22 精准承认了两个 gap：(a) representational vs behavioral；(b) open-loop vs closed-loop。措辞克制且具体。\n- P1（Discussion 弱化措辞）**大部分达标**。Line 12 \"demonstrates causal influence\" 是合理的——trajectory analysis 确实 demonstrates L1 ablation 影响 output，这比 \"confirms the causal role\" 准确得多。\n\n**残余问题**: Discussion line 8 仍使用 \"establishing a causal link from routing to output\"。\"Establishing\" 在学术写作中通常意味着 \"证实\"，比 line 12 的 \"demonstrates\" 更强。两处措辞不一致：line 8 claim 已 \"establish\" 因果链，line 22 又承认需要 closed-loop evaluation。建议将 \"establishing\" 改为 \"suggesting\" 或 \"providing evidence for\"。\n\n**Severity 降级理由**: Limitations 的显式 acknowledgment 大幅降低了 CoRL 审稿人的 rejection risk。behavioral gap 仍然存在，但论文不再回避它——这是一个 acknowledged scope limitation 而非 hidden weakness。从 CRITICAL 降为 WARNING。\n\n---\n\n### 🟡 R6-C1 + R7-W1 + R7-W2 [WARNING]: Ablation 因果推断 + 维度分离 + Per-head comparability — [RESOLVED]\n\n**修改确认**:\n\n**(a) 维度分离（R7-W1）**: Discussion line 13:\n> \"The R² improvement reflects information gain in continuous dimensions (removing routing signals frees bandwidth), while the gripper-concentrated trajectory effect (72.3% divergence) reflects discrete manipulation sensitivity.\"\n\n这是一个合理且诚实的 framing：显式承认两个分析探测不同维度，并给出各自的解释（R² → continuous bandwidth；trajectory → discrete gripper sensitivity），而非假装两者一致。\n\n**(b) Per-head comparability + Discussion 矛盾（R7-W2）**: Discussion line 14:\n> \"The attention analysis reveals what the model learns (reorganized routing), while ablation reveals how the function is implemented (distributed across the layer). Routing reorganization is the observable signature of L1's acquired collective role, not a property of individual heads.\"\n\n这个重写消除了之前的核心矛盾。新叙事结构：\n- Attention analysis 度量的是 WHAT（L1 学到了 routing reorganization → 24/32 heads 变为 instruction-dominant）\n- Ablation 度量的是 HOW（功能实现是 distributed → per-head effects comparable）\n- \"Collective role\" 替代了 \"individual head specialization\"\n\n这与 Experiments line 79 \"L1 attention collectively influences action generation rather than through a specialized subset\" 完全一致。不再有逻辑断裂。\n\n**(c) Experiments self-consistency**: Ablation 段落（lines 69-74）的 \"routing-first specialization\" 叙述与 Discussion 的 \"collective role\" 叙述现在兼容：individual heads carry routing signals（attention analysis shows this），但 functional importance is collective（ablation shows this）。\n\n**残余注意**: Discussion line 8 提到 \"R² +0.059 at L1\"。此数值未在 Experiments 中出现（Experiments 报告 dominant-head +0.042 和 random-mean +0.077）。推测这是某种平均或中间值，但来源不透明。Minor issue，不影响 resolved 判定。\n\n---\n\n## New Issues\n\n### N1 [INFO]: \"Establishing\" vs \"demonstrates\" 措辞不一致\n\nDiscussion line 8 \"establishing a causal link from routing to output\" vs line 12 \"demonstrates causal influence\" vs Limitations line 22 承认需要 closed-loop evaluation。三处对因果链强度的描述不一致。Line 8 最强（establish），line 12 居中（demonstrate），line 22 最弱（leave to future work）。一次 sed 替换即可修复（establishing → supporting）。\n\n### N2 [INFO]: R² +0.059 来源不明\n\nDiscussion line 8 的 \"+0.059 at L1\" 数值未在 Experiments 或 Appendix 中出现。可能是 dominant (0.042) 和 random (0.077) 的某种加权平均或新计算，但读者无法追溯。建议标明来源或改用已报告的数值。\n\n---\n\n## Discussion Quality Assessment\n\nDiscussion 现在是四段结构：Synthesis → Mechanistic interpretation → Predictions → Limitations。\n\n**Synthesis（lines 4-8）**: 逻辑清晰。两条独立证据线（attention reorganization + ablation gradient）收敛于 L1 routing hub，加上 trajectory 确认 output-level 影响。叙事紧凑。Minor issue: \"establishing\" 过强（见 N1）。\n\n**Mechanistic interpretation（lines 10-14）**: 本轮最大改进。维度分离和 what-vs-how 区分使 ablation 结果的解释从之前的自相矛盾变为逻辑自洽。\"Collective role\" 的 framing 是对 per-head comparability 的正确回应。RSA bifurcation 的描述简洁有效。\n\n**Predictions（lines 16-18）**: 两条 testable predictions 是好的添加。(1) 其他 decoder-only VLA 应有类似 entry-layer routing（vs cross-attention 架构）；(2) L1 ablation 应导致 task degradation。这些 predictions 使论文的分析发现从描述性升级为可证伪的假设。但需注意 prediction (2) 与 Experiments 的 ablation 结果之间的张力：如果 L1 ablation increases R²（Experiments 所示），为什么作者 predict 它会导致 task degradation？这里隐含假设 R² 增加不等于 behavioral improvement——这与 Limitations line 22 的 acknowledgment 一致，但可以更显式地讨论。\n\n**Limitations（lines 20-22）**: 显著改善。\"representational and open-loop\" + \"closed-loop evaluation...leave to future work\" 直接回应了多轮 behavioral validation 的 concern。简洁准确。\n\n**整体连贯性**: 四段之间逻辑链通畅。Synthesis 总结 findings → Mechanistic interpretation 解释 why → Predictions 提出可验证假设 → Limitations 界定 scope。没有明显的逻辑跳跃。\n\n---\n\n## 其他修改检查\n\n### Introduction model-specific qualifiers\n- Line 15: \"Three findings emerge from our analysis of OpenVLA-7B on LIBERO\" — **Good**，明确限定模型和 benchmark。\n- Line 23: Contribution (i) \"in the model studied\"; Contribution (iii) \"in this architecture\" — **Good**，消除了 overclaim。\n\n### CKA 分歧主文 acknowledgment\n- Experiments line 124（新增）: \"Under linear CKA, the inverted-U disappears (per-layer similarity increases monotonically) and encoder ordering reverses (Appendix). The non-monotonic trajectory reported here characterizes RSA-specific rank-order geometry; its generality across similarity metrics remains open.\"\n- **Good**. 这是之前多轮要求的修改。读者无需翻阅 Appendix 即可知道 Finding 3 的 metric-dependency。\"Its generality across similarity metrics remains open\" 是准确的 scope limitation。\n\n### conclusion.tex 编译\n- main.tex line 33: `\\input{conclusion}` — **Fixed**。R2 多轮指出的 W8 终于修复。\n\n### Experiments 段落一致性\n- Ablation（lines 69-74）+ Trajectory（lines 76-80）: 与 Discussion 的 collective role 叙事一致。无新矛盾。\n\n---\n\n## Score\n\n```\nScore: 6/10 → 7/10 (↑)\nConfidence: 4/5\n```\n\n**升分理由**:\n\n1. **R6-C4 从 CRITICAL 降为 WARNING**: Limitations 显式承认 open-loop + representational scope 是本轮最重要的修复。对 CoRL 审稿人来说，\"论文知道自己的局限并坦诚表述\" 与 \"论文回避 behavioral gap\" 是截然不同的审稿体验。\n2. **R6-C1 完全 RESOLVED**: Discussion rewrite 消除了维度分离矛盾和 per-head comparability 与 routing specialization 之间的逻辑断裂。Collective role framing 是对实验证据的准确叙述。\n3. **CKA 分歧进入主文**: Line 124 是一个小但重要的修改，让 Finding 3 的 claim strength 与证据匹配。\n4. **Introduction overclaim 修复**: Model-specific qualifiers 遍及全文。\n5. **conclusion.tex 编译修复**: 论文结构完整。\n\n**限制升分至 7 的因素**:\n\n1. **\"Establishing\" 仍过强**（N1）: Discussion line 8 与 Limitations line 22 措辞不一致。修复成本极低但尚未完成。\n2. **Behavioral validation 仍是 WARNING**: 论文承认了 gap 但 gap 本身仍在。对 CoRL 来说，纯 representational analysis without rollout 的 novelty bar 更高。\n3. **单模型+单 benchmark**: 结构性限制无法在修订中解决。\n4. **N=10 random subsets 始终未增加**: 从 Round 1 至今一直是 open concern，统计检验力有限。\n\n**为什么 7 而非 6**: Round 7 到 Round 8 的修改集中解决了 Discussion 的逻辑一致性问题（维度分离、collective role、behavioral gap acknowledgment），这些是上一轮阻碍升分的主要因素。论文现在的 claim 强度与证据基本匹配——剩余问题（N1 措辞、N=10 subsets、单模型泛化）是 minor/structural limitations，不再是方法论缺陷。\n",
  "reviewer_id": "1",
  "project": "vla-ssd"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 — Round 8 修订评估\n\n---\n\n## Issue Verification\n\n### 🔴 R6-C4 [CRITICAL]: 缺 behavioral validation — [RESOLVED as WARNING]\n\n**修改确认**:\n- Discussion line 12: \"confirms the causal role\" → \"demonstrates causal influence on action output\"。措辞从 \"confirms\" 降为 \"demonstrates\"，不再隐含因果链已完全建立。\n- Limitations line 22（新增）: \"Our analyses are representational and open-loop; connecting routing reorganization to task success requires closed-loop evaluation, which we leave to future work.\"\n- Predictions line 18: \"L1 ablation on a fine-tuned model should produce measurable task degradation, particularly on instruction-discriminative tasks\" — 将 behavioral 验证定位为可验证的 prediction 而非已有结论。\n\n**评估**:\n- P2（Limitations 声明）**完全达标**。Line 22 精准承认了两个 gap：(a) representational vs behavioral；(b) open-loop vs closed-loop。措辞克制且具体。\n- P1（Discussion 弱化措辞）**大部分达标**。Line 12 \"demonstrates causal influence\" 是合理的——trajectory analysis 确实 demonstrates L1 ablation 影响 output，这比 \"confirms the causal role\" 准确得多。\n\n**残余问题**: Discussion line 8 仍使用 \"establishing a causal link from routing to output\"。\"Establishing\" 在学术写作中通常意味着 \"证实\"，比 line 12 的 \"demonstrates\" 更强。两处措辞不一致：line 8 claim 已 \"establish\" 因果链，line 22 又承认需要 closed-loop evaluation。建议将 \"establishing\" 改为 \"suggesting\" 或 \"providing evidence for\"。\n\n**Severity 降级理由**: Limitations 的显式 acknowledgment 大幅降低了 CoRL 审稿人的 rejection risk。behavioral gap 仍然存在，但论文不再回避它——这是一个 acknowledged scope limitation 而非 hidden weakness。从 CRITICAL 降为 WARNING。\n\n---\n\n### 🟡 R6-C1 + R7-W1 + R7-W2 [WARNING]: Ablation 因果推断 + 维度分离 + Per-head comparability — [RESOLVED]\n\n**修改确认**:\n\n**(a) 维度分离（R7-W1）**: Discussion line 13:\n> \"The R² improvement reflects information gain in continuous dimensions (removing routing signals frees bandwidth), while the gripper-concentrated trajectory effect (72.3% divergence) reflects discrete manipulation sensitivity.\"\n\n这是一个合理且诚实的 framing：显式承认两个分析探测不同维度，并给出各自的解释（R² → continuous bandwidth；trajectory → discrete gripper sensitivity），而非假装两者一致。\n\n**(b) Per-head comparability + Discussion 矛盾（R7-W2）**: Discussion line 14:\n> \"The attention analysis reveals what the model learns (reorganized routing), while ablation reveals how the function is implemented (distributed across the layer). Routing reorganization is the observable signature of L1's acquired collective role, not a property of individual heads.\"\n\n这个重写消除了之前的核心矛盾。新叙事结构：\n- Attention analysis 度量的是 WHAT（L1 学到了 routing reorganization → 24/32 heads 变为 instruction-dominant）\n- Ablation 度量的是 HOW（功能实现是 distributed → per-head effects comparable）\n- \"Collective role\" 替代了 \"individual head specialization\"\n\n这与 Experiments line 79 \"L1 attention collectively influences action generation rather than through a specialized subset\" 完全一致。不再有逻辑断裂。\n\n**(c) Experiments self-consistency**: Ablation 段落（lines 69-74）的 \"routing-first specialization\" 叙述与 Discussion 的 \"collective role\" 叙述现在兼容：individual heads carry routing signals（attention analysis shows this），但 functional importance is collective（ablation shows this）。\n\n**残余注意**: Discussion line 8 提到 \"R² +0.059 at L1\"。此数值未在 Experiments 中出现（Experiments 报告 dominant-head +0.042 和 random-mean +0.077）。推测这是某种平均或中间值，但来源不透明。Minor issue，不影响 resolved 判定。\n\n---\n\n## New Issues\n\n### N1 [INFO]: \"Establishing\" vs \"demonstrates\" 措辞不一致\n\nDiscussion line 8 \"establishing a causal link from routing to output\" vs line 12 \"demonstrates causal influence\" vs Limitations line 22 承认需要 closed-loop evaluation。三处对因果链强度的描述不一致。Line 8 最强（establish），line 12 居中（demonstrate），line 22 最弱（leave to future work）。一次 sed 替换即可修复（establishing → supporting）。\n\n### N2 [INFO]: R² +0.059 来源不明\n\nDiscussion line 8 的 \"+0.059 at L1\" 数值未在 Experiments 或 Appendix 中出现。可能是 dominant (0.042) 和 random (0.077) 的某种加权平均或新计算，但读者无法追溯。建议标明来源或改用已报告的数值。\n\n---\n\n## Discussion Quality Assessment\n\nDiscussion 现在是四段结构：Synthesis → Mechanistic interpretation → Predictions → Limitations。\n\n**Synthesis（lines 4-8）**: 逻辑清晰。两条独立证据线（attention reorganization + ablation gradient）收敛于 L1 routing hub，加上 trajectory 确认 output-level 影响。叙事紧凑。Minor issue: \"establishing\" 过强（见 N1）。\n\n**Mechanistic interpretation（lines 10-14）**: 本轮最大改进。维度分离和 what-vs-how 区分使 ablation 结果的解释从之前的自相矛盾变为逻辑自洽。\"Collective role\" 的 framing 是对 per-head comparability 的正确回应。RSA bifurcation 的描述简洁有效。\n\n**Predictions（lines 16-18）**: 两条 testable predictions 是好的添加。(1) 其他 decoder-only VLA 应有类似 entry-layer routing（vs cross-attention 架构）；(2) L1 ablation 应导致 task degradation。这些 predictions 使论文的分析发现从描述性升级为可证伪的假设。但需注意 prediction (2) 与 Experiments 的 ablation 结果之间的张力：如果 L1 ablation increases R²（Experiments 所示），为什么作者 predict 它会导致 task degradation？这里隐含假设 R² 增加不等于 behavioral improvement——这与 Limitations line 22 的 acknowledgment 一致，但可以更显式地讨论。\n\n**Limitations（lines 20-22）**: 显著改善。\"representational and open-loop\" + \"closed-loop evaluation...leave to future work\" 直接回应了多轮 behavioral validation 的 concern。简洁准确。\n\n**整体连贯性**: 四段之间逻辑链通畅。Synthesis 总结 findings → Mechanistic interpretation 解释 why → Predictions 提出可验证假设 → Limitations 界定 scope。没有明显的逻辑跳跃。\n\n---\n\n## 其他修改检查\n\n### Introduction model-specific qualifiers\n- Line 15: \"Three findings emerge from our analysis of OpenVLA-7B on LIBERO\" — **Good**，明确限定模型和 benchmark。\n- Line 23: Contribution (i) \"in the model studied\"; Contribution (iii) \"in this architecture\" — **Good**，消除了 overclaim。\n\n### CKA 分歧主文 acknowledgment\n- Experiments line 124（新增）: \"Under linear CKA, the inverted-U disappears (per-layer similarity increases monotonically) and encoder ordering reverses (Appendix). The non-monotonic trajectory reported here characterizes RSA-specific rank-order geometry; its generality across similarity metrics remains open.\"\n- **Good**. 这是之前多轮要求的修改。读者无需翻阅 Appendix 即可知道 Finding 3 的 metric-dependency。\"Its generality across similarity metrics remains open\" 是准确的 scope limitation。\n\n### conclusion.tex 编译\n- main.tex line 33: `\\input{conclusion}` — **Fixed**。R2 多轮指出的 W8 终于修复。\n\n### Experiments 段落一致性\n- Ablation（lines 69-74）+ Trajectory（lines 76-80）: 与 Discussion 的 collective role 叙事一致。无新矛盾。\n\n---\n\n## Score\n\n```\nScore: 6/10 → 7/10 (↑)\nConfidence: 4/5\n```\n\n**升分理由**:\n\n1. **R6-C4 从 CRITICAL 降为 WARNING**: Limitations 显式承认 open-loop + representational scope 是本轮最重要的修复。对 CoRL 审稿人来说，\"论文知道自己的局限并坦诚表述\" 与 \"论文回避 behavioral gap\" 是截然不同的审稿体验。\n2. **R6-C1 完全 RESOLVED**: Discussion rewrite 消除了维度分离矛盾和 per-head comparability 与 routing specialization 之间的逻辑断裂。Collective role framing 是对实验证据的准确叙述。\n3. **CKA 分歧进入主文**: Line 124 是一个小但重要的修改，让 Finding 3 的 claim strength 与证据匹配。\n4. **Introduction overclaim 修复**: Model-specific qualifiers 遍及全文。\n5. **conclusion.tex 编译修复**: 论文结构完整。\n\n**限制升分至 7 的因素**:\n\n1. **\"Establishing\" 仍过强**（N1）: Discussion line 8 与 Limitations line 22 措辞不一致。修复成本极低但尚未完成。\n2. **Behavioral validation 仍是 WARNING**: 论文承认了 gap 但 gap 本身仍在。对 CoRL 来说，纯 representational analysis without rollout 的 novelty bar 更高。\n3. **单模型+单 benchmark**: 结构性限制无法在修订中解决。\n4. **N=10 random subsets 始终未增加**: 从 Round 1 至今一直是 open concern，统计检验力有限。\n\n**为什么 7 而非 6**: Round 7 到 Round 8 的修改集中解决了 Discussion 的逻辑一致性问题（维度分离、collective role、behavioral gap acknowledgment），这些是上一轮阻碍升分的主要因素。论文现在的 claim 强度与证据基本匹配——剩余问题（N1 措辞、N=10 subsets、单模型泛化）是 minor/structural limitations，不再是方法论缺陷。\n",
    "reviewer_id": "1",
    "project": "vla-ssd"
  }
}
````

</details>

---


### Tool result

_source line 250 · 2026-05-18T14:13:41.793213+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3965
}
```

</details>

---


### Assistant

_source line 251 · 2026-05-18T14:13:49.141043+00:00_

Round 8 评估已提交。评分从 6/10 升至 7/10。

核心变化：
- **R6-C4**（behavioral validation）从 CRITICAL 降为 WARNING：Limitations 新增了显式的 open-loop/representational scope 声明
- **R6-C1**（ablation 逻辑矛盾）RESOLVED：Discussion rewrite 用 "collective role" + what-vs-how 区分消除了维度分离和 per-head comparability 的自相矛盾
- **CKA 分歧**进入主文（experiments line 124），Finding 3 的 metric-dependency 不再被隐藏
- **conclusion.tex** 终于编译，Introduction 加了 model-specific qualifiers

剩余 minor issues：Discussion line 8 的 "establishing" 与 Limitations 的 open-loop acknowledgment 措辞不一致；R² +0.059 来源不明；N=10 random subsets 始终未增加。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1"
}
```

</details>

---


## Round 14

## Round 14

3 recorded events


### User

_source line 252 · 2026-05-18T14:15:06.746162+00:00_

[Round 8 审稿请求]:
# Round 8 交叉分享 — 请回应 Reviewer 2 的评估

以下是 Reviewer 2 的完整 Round 8 评估。请逐条回应 [AGREE] 或 [REBUT]，特别关注评分差异（你给 7/10，R2 给 6/10）。

---

## R2 的 Issue Verification

### R6-C3 [RESOLVED]: 单模型 overclaim
R2 逐处验证通过：Introduction line 15 model-specific 前缀、Contribution (i)(iii) 限定、Abstract "in the model studied"、Discussion Predictions 用 "should"。残余极小（Conclusion 用 generic "VLA"）。

### R7-W3 [RESOLVED]: CKA 主文讨论
R2 确认 Experiments line 124 两句话完成三件事：告知 CKA 结果相反、限定为 RSA-specific、坦诚承认 generality open。

### R4-I1 [RESOLVED]: conclusion.tex
R2 确认编译正确。评价 Conclusion 2 句话偏短但可接受。

## R2 的新发现

### N1 [INFO]: Conclusion 过于简短
2 句话作为 8 页论文收尾偏短。可加 broader impact 或 future direction。Polish 级别。

## R2 的 Discussion 评价

- **Predictions**: 最有价值的新增之一。Falsifiable framework。
- **Mechanistic interpretation**: 彻底修复了 Round 7 的 self-contradiction。
- **Limitations**: 直接满足 R2 在 Round 7 交叉回应中的升分条件。

## R2 的评分: 6/10

### R2 保持 6 而非更高的原因
1. 单模型 + 无 behavioral validation 仍是 structural limitation
2. C1 novelty 仍 modest
3. Ablation 方向性问题事实不变
4. 10 random subsets 未增加

---

## 请特别回应

1. **评分差异**：你给 7/10，R2 给 6/10。你认为差异来自哪里？是否调整？
2. **你的 N1**（"establishing" 措辞不一致）和 **N2**（R² +0.059 来源不明）：R2 未提及这两个问题。你认为这两个 INFO 是否需要在最终报告中标记？
3. **R2 的 Conclusion 偏短问题**：你是否同意？
4. **Predictions 段落评价**：R2 高度肯定。你在初审中对 prediction (2) 与 ablation R² 增加之间的张力表示了关注。这是否仍是一个 concern？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 253 · 2026-05-18T14:16:00.457040+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 交叉回应 — 对 Reviewer 2 Round 8 评估\n\n---\n\n## R2 Issue Verification 回应\n\n**[AGREE] R6-C3 [RESOLVED]**: 逐处验证结果与我的观察一致。Introduction line 15、Contribution (i)(iii)、Abstract line 7 的 model-specific qualifiers 全部到位。Conclusion 用 generic \"VLA\" 是 R2 指出的残余，但 Conclusion 仅 2 句且紧跟在 fully-qualified Discussion 之后，context 足够。不影响 resolved 判定。\n\n**[AGREE] R7-W3 [RESOLVED]**: Experiments line 124 的两句话是高效的修复。我在自己的报告中也确认了这一点。\n\n**[AGREE] R4-I1 [RESOLVED]**: conclusion.tex 编译确认。\n\n---\n\n## 评分差异分析：R1 7/10 vs R2 6/10\n\n差距为 1 分。我仔细考虑了 R2 维持 6 的四个理由：\n\n**(1) 单模型 + 无 behavioral validation**: 同意这是 structural limitation。但我的权重分配不同：论文现在在 Limitations line 22 显式承认了 open-loop scope，在 Predictions 段落提出了 falsifiable behavioral hypothesis。对我来说，\"承认 gap + 提出可验证 prediction\" 与 \"隐藏 gap\" 是质的不同——前者是 honest scope choice（类似 NLP 领域大量 probing/analysis papers 不做 downstream task 修改），后者才是 rejection-level 问题。CoRL 确实比 NLP venues 更看重 behavioral evidence，但我认为一篇分析框架论文在 Limitations 坦诚界定 scope 后，6 偏保守。\n\n**(2) C1 novelty modest**: 同意。但论文已将 C1 降格为 \"validate the framework by confirming architecture-expected specialization\"（Abstract line 4），不再主张这是 novel finding。作为 framework validation 它服务于方法论贡献，novelty 负担由 C2 承担。\n\n**(3) Ablation 方向性问题**: 同意事实不变（all ablation increase R²）。但 Discussion 现在提供了 coherent interpretation（R² reflects continuous bandwidth freeing; trajectory reflects discrete gripper sensitivity; collective role not individual head property），且 Predictions line 18 将 behavioral consequence 定位为 future work。这意味着 ablation 结果从 \"论文无法解释的矛盾\" 变为 \"已解释的现象 + 待验证的 prediction\"。对我来说这足以使其不再是扣分项，而是 acknowledged nuance。\n\n**(4) 10 random subsets 未增加**: 同意这始终是一个 open concern。但它是单个实验的统计功效问题，不影响论文的整体证据结构——三条件 gradient、32-layer attention profile、cross-benchmark replication 等核心发现不依赖这 10 subsets 的 z-test。\n\n**结论**: 我理解 R2 的保守立场，这四点都是 legitimate concerns。差异核心在于对 \"analysis paper without behavioral validation at CoRL\" 的 meta-judgment：我认为 honest scope + testable predictions 足以 justify acceptance（7），R2 认为 structural limitation 仍构成 barrier（6）。两种判断都有合理依据。\n\n**我维持 7/10，不调整。** 理由：本轮修改集中解决了 Discussion 逻辑一致性（我此前升分的 bottleneck），剩余问题均为已承认的 scope limitations 或 minor issues，不构成方法论缺陷。\n\n---\n\n## 关于我的 N1 和 N2\n\n**N1（\"establishing\" 措辞不一致）**: 应在最终报告中保留为 INFO。虽然 R2 未提及，但 Discussion line 8 \"establishing a causal link\" 与 Limitations line 22 \"leave to future work\" 之间确实存在张力。这是一个一行 fix（establishing → supporting/suggesting），不影响评分但属于 polishing checklist 项。\n\n**N2（R² +0.059 来源不明）**: 同样保留为 INFO。可追溯性是学术写作的基本要求——正文引用的数值应在 Experiments 或 Appendix 中可找到来源。但这是 copyediting 级别问题。\n\n---\n\n## R2 的 Conclusion 偏短问题 — [AGREE, INFO 级别]\n\n同意 Conclusion 偏短（2 句话，~40 words）。对于 8 页正文的论文，标准做法是 3-5 句话覆盖：(a) 核心发现总结；(b) 方法论贡献的可复用性；(c) broader implications 或 future directions。当前 Conclusion 缺少 (b) 和 (c)。\n\n但这是 polish 级别问题。Discussion 已承担了大部分总结功能（Synthesis + Predictions + Limitations），Conclusion 更像是 structural formality。不影响评分。\n\n---\n\n## Predictions 段落与 ablation R² 增加之间的张力\n\nR2 高度肯定 Predictions 段落，我也认为这是本轮最有价值的新增之一。但我在初审报告中指出的张力仍存在：\n\n**Prediction (2)**: \"L1 ablation on a fine-tuned model should produce measurable task degradation, particularly on instruction-discriminative tasks.\"\n\n**张力**: Experiments 显示 L1 ablation increases probe R²（+0.042 for dominant, +0.077 for random）。如果移除 L1 routing 提高了 action prediction quality（R² 上升），为什么 prediction 是 task degradation（performance 下降）？\n\n**论文隐含的 bridge**: R² 度量 offline action prediction，不等于 behavioral success。Probe 可能因为 routing signals 被移除而更容易拟合（noise reduction for the probe），但实际 rollout 需要 instruction conditioning 才能选择正确 action（尤其在 instruction-discriminative tasks 上）。这个 bridge 是合理的，但论文未显式讨论。\n\n**我的判断**: 这个张力是一个 productive intellectual gap 而非 fatal flaw。Prediction (2) 是 falsifiable 的，且其验证/否定都会对 VLA 理解有贡献。张力本身的存在说明论文的分析开辟了有价值的 future questions。不扣分，但建议作者在 camera-ready 中加一句解释 R²-behavior 的 dissociation 可能性。\n\n---\n\n## 最终评分\n\n**Score: 7/10 (Good paper, accept)**\n**Confidence: 4/5**\n\n**一句话总结**: 论文提供了一个系统性的 VLA 表征分析框架，核心发现（entry-exit routing reorganization）有充分的多角度证据支撑，修订后 claim 强度与证据匹配，剩余 limitations（单模型、无 behavioral rollout）已坦诚界定且不构成方法论缺陷。\n",
  "reviewer_id": "1",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 交叉回应 — 对 Reviewer 2 Round 8 评估\n\n---\n\n## R2 Issue Verification 回应\n\n**[AGREE] R6-C3 [RESOLVED]**: 逐处验证结果与我的观察一致。Introduction line 15、Contribution (i)(iii)、Abstract line 7 的 model-specific qualifiers 全部到位。Conclusion 用 generic \"VLA\" 是 R2 指出的残余，但 Conclusion 仅 2 句且紧跟在 fully-qualified Discussion 之后，context 足够。不影响 resolved 判定。\n\n**[AGREE] R7-W3 [RESOLVED]**: Experiments line 124 的两句话是高效的修复。我在自己的报告中也确认了这一点。\n\n**[AGREE] R4-I1 [RESOLVED]**: conclusion.tex 编译确认。\n\n---\n\n## 评分差异分析：R1 7/10 vs R2 6/10\n\n差距为 1 分。我仔细考虑了 R2 维持 6 的四个理由：\n\n**(1) 单模型 + 无 behavioral validation**: 同意这是 structural limitation。但我的权重分配不同：论文现在在 Limitations line 22 显式承认了 open-loop scope，在 Predictions 段落提出了 falsifiable behavioral hypothesis。对我来说，\"承认 gap + 提出可验证 prediction\" 与 \"隐藏 gap\" 是质的不同——前者是 honest scope choice（类似 NLP 领域大量 probing/analysis papers 不做 downstream task 修改），后者才是 rejection-level 问题。CoRL 确实比 NLP venues 更看重 behavioral evidence，但我认为一篇分析框架论文在 Limitations 坦诚界定 scope 后，6 偏保守。\n\n**(2) C1 novelty modest**: 同意。但论文已将 C1 降格为 \"validate the framework by confirming architecture-expected specialization\"（Abstract line 4），不再主张这是 novel finding。作为 framework validation 它服务于方法论贡献，novelty 负担由 C2 承担。\n\n**(3) Ablation 方向性问题**: 同意事实不变（all ablation increase R²）。但 Discussion 现在提供了 coherent interpretation（R² reflects continuous bandwidth freeing; trajectory reflects discrete gripper sensitivity; collective role not individual head property），且 Predictions line 18 将 behavioral consequence 定位为 future work。这意味着 ablation 结果从 \"论文无法解释的矛盾\" 变为 \"已解释的现象 + 待验证的 prediction\"。对我来说这足以使其不再是扣分项，而是 acknowledged nuance。\n\n**(4) 10 random subsets 未增加**: 同意这始终是一个 open concern。但它是单个实验的统计功效问题，不影响论文的整体证据结构——三条件 gradient、32-layer attention profile、cross-benchmark replication 等核心发现不依赖这 10 subsets 的 z-test。\n\n**结论**: 我理解 R2 的保守立场，这四点都是 legitimate concerns。差异核心在于对 \"analysis paper without behavioral validation at CoRL\" 的 meta-judgment：我认为 honest scope + testable predictions 足以 justify acceptance（7），R2 认为 structural limitation 仍构成 barrier（6）。两种判断都有合理依据。\n\n**我维持 7/10，不调整。** 理由：本轮修改集中解决了 Discussion 逻辑一致性（我此前升分的 bottleneck），剩余问题均为已承认的 scope limitations 或 minor issues，不构成方法论缺陷。\n\n---\n\n## 关于我的 N1 和 N2\n\n**N1（\"establishing\" 措辞不一致）**: 应在最终报告中保留为 INFO。虽然 R2 未提及，但 Discussion line 8 \"establishing a causal link\" 与 Limitations line 22 \"leave to future work\" 之间确实存在张力。这是一个一行 fix（establishing → supporting/suggesting），不影响评分但属于 polishing checklist 项。\n\n**N2（R² +0.059 来源不明）**: 同样保留为 INFO。可追溯性是学术写作的基本要求——正文引用的数值应在 Experiments 或 Appendix 中可找到来源。但这是 copyediting 级别问题。\n\n---\n\n## R2 的 Conclusion 偏短问题 — [AGREE, INFO 级别]\n\n同意 Conclusion 偏短（2 句话，~40 words）。对于 8 页正文的论文，标准做法是 3-5 句话覆盖：(a) 核心发现总结；(b) 方法论贡献的可复用性；(c) broader implications 或 future directions。当前 Conclusion 缺少 (b) 和 (c)。\n\n但这是 polish 级别问题。Discussion 已承担了大部分总结功能（Synthesis + Predictions + Limitations），Conclusion 更像是 structural formality。不影响评分。\n\n---\n\n## Predictions 段落与 ablation R² 增加之间的张力\n\nR2 高度肯定 Predictions 段落，我也认为这是本轮最有价值的新增之一。但我在初审报告中指出的张力仍存在：\n\n**Prediction (2)**: \"L1 ablation on a fine-tuned model should produce measurable task degradation, particularly on instruction-discriminative tasks.\"\n\n**张力**: Experiments 显示 L1 ablation increases probe R²（+0.042 for dominant, +0.077 for random）。如果移除 L1 routing 提高了 action prediction quality（R² 上升），为什么 prediction 是 task degradation（performance 下降）？\n\n**论文隐含的 bridge**: R² 度量 offline action prediction，不等于 behavioral success。Probe 可能因为 routing signals 被移除而更容易拟合（noise reduction for the probe），但实际 rollout 需要 instruction conditioning 才能选择正确 action（尤其在 instruction-discriminative tasks 上）。这个 bridge 是合理的，但论文未显式讨论。\n\n**我的判断**: 这个张力是一个 productive intellectual gap 而非 fatal flaw。Prediction (2) 是 falsifiable 的，且其验证/否定都会对 VLA 理解有贡献。张力本身的存在说明论文的分析开辟了有价值的 future questions。不扣分，但建议作者在 camera-ready 中加一句解释 R²-behavior 的 dissociation 可能性。\n\n---\n\n## 最终评分\n\n**Score: 7/10 (Good paper, accept)**\n**Confidence: 4/5**\n\n**一句话总结**: 论文提供了一个系统性的 VLA 表征分析框架，核心发现（entry-exit routing reorganization）有充分的多角度证据支撑，修订后 claim 强度与证据匹配，剩余 limitations（单模型、无 behavioral rollout）已坦诚界定且不构成方法论缺陷。\n",
    "reviewer_id": "1",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 254 · 2026-05-18T14:16:04.986264+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4529
}
```

</details>

---


## Round 15

## Round 15

52 recorded events


### User

_source line 255 · 2026-05-19T00:49:57.788167+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。

## Venue 信息
- **目标会议**: CoRL 2026
- **Deadline**: 2026-05-29
- **页数限制**: 正文 8 页 + Acknowledgments/References/Appendix 不计页
- **模板**: corl_2026
- **匿名规则**: double-blind
- **附录规则**: 允许，不计入页数限制
- **需要**: Limitations section (计入 8 页)；Generative AI 使用声明

## 论文路径
`projects/vla-ssd/docs/paper/main.tex`（各 section 通过 `\input{}` 引用同目录下的 .tex 文件）

## 你的审查侧重

**核心关注**：
1. **统计方法严谨性**：bootstrap CI 是否正确应用、多重比较校正是否充分、效应量报告是否完整
2. **Ablation 设计质量**：L1 head ablation 的因果推断强度——random-subset control 的解释是否合理、dose-response 是否真正支持因果链
3. **Probe 方法论**：MLP probe vs linear probe 的 capacity control、训练/测试划分是否消除时间自相关、N/params 比
4. **控制条件充分性**：三条件设计 (trained/pretrained/untrained) 的有效性——pretrained Llama-2 处理视觉 token 的 OOD 问题是否被充分控制
5. **RSA 方法论**：pairwise dependency 处理、distance metric 选择的 robustness、CKA 反转的处理
6. **Counterfactual instruction analysis**：4 种 perturbation 的选择合理性、效应量解读
7. **数据规模与统计功效**：N=63,228 是否真实独立、10 tasks 是否足够支撑 task-level 统计
8. **Reproducibility**：实验细节是否足以复现

**硬规则**：
- 不给修改建议——只评估和报告问题
- 用 CoRL 2026 的标准评判（robotics + learning 社区，重视实验严谨性和实际意义）
- 必须给出：Strengths (逐条)、Weaknesses (逐条，按 severity: critical/warning/info 分级)、Questions、Overall Assessment

请读取论文全文并完成审稿。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 256 · 2026-05-19T00:50:06.529907+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 257 · 2026-05-19T00:50:06.631385+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/sessions/review_reviewer_1_458aa27f.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 258 · 2026-05-19T00:50:11.050931+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15"
  }
}
```

</details>

---


### Tool result

_source line 259 · 2026-05-19T00:50:11.253870+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 260 · 2026-05-19T00:50:11.306146+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 261 · 2026-05-19T00:50:11.761109+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 262 · 2026-05-19T00:50:15.938300+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 263 · 2026-05-19T00:50:16.090514+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 264 · 2026-05-19T00:50:16.446514+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
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

_source line 265 · 2026-05-19T00:50:16.497298+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 266 · 2026-05-19T00:50:20.567262+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
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

_source line 267 · 2026-05-19T00:50:20.618250+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_example.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 268 · 2026-05-19T00:50:23.433253+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 269 · 2026-05-19T00:50:23.985590+00:00_

1	Vision-language-action models (VLAs) fine-tune large language models (LLMs) on robot demonstrations, but what fine-tuning changes at the representational level remains unclear.
2	We present a systematic framework for token-level analysis of VLAs, applying cross-instruction probes, attention analysis, Representational Similarity Analysis (RSA), and functional probes across all 32 LLM layers of OpenVLA-7B on LIBERO, with factorial trained/pretrained/untrained controls.
3	Three findings emerge.
4	First, our framework validates architecture-expected token specialization: image tokens are instruction-blind while the readout token serves as the sole multimodal convergence point ($100\%$ instruction classification from L1, cross-validated).
5	Second, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth, while VLA training shifts this to entry-layer routing (L0--L1) with exit-layer re-engagement (L31).
6	Seven complementary analyses, including dose-response ablation (8 conditions, monotonic $d = 0.48 \to 0.64$) and counterfactual instruction analysis (4 perturbation types, $d = 0.63$--$0.97$), support instruction-conditioned action generation through distributed L1 routing, where instruction-attention fraction predicts per-head contribution magnitude.
7	Third, under RSA and action probes, vision encoder representations show a middle-layer peak, but this pattern is metric-dependent (CKA diverges).
8	Training effects concentrate at the readout token (probe $R^2$ $+0.069$, instruction attention $+46$pp) rather than visual geometry ($\Delta\rho \leq 0.017$, non-significant); instruction routing reorganization is the primary learned contribution of fine-tuning in the model studied.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 270 · 2026-05-19T00:50:24.337131+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 271 · 2026-05-19T00:50:24.387841+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	What does fine-tuning change inside a Vision-Language-Action model (VLA)?
5	VLAs fine-tune large language models on robot demonstrations to produce actions from visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla}, but the decoder-only causal mask prevents image tokens from attending to instructions.
6	Instruction information must reach action-generating positions through learned attention routing, yet how fine-tuning reshapes this routing remains uncharacterized.
7	
8	Recent behavioral studies reveal that VLAs rely disproportionately on visual input~\cite{grant2026}, with language instructions largely ignored by the action pathway~\cite{haon2025}.
9	These findings suggest internal specialization but do not explain \emph{how} instruction information reaches the action-generating readout token, \emph{what} routing strategy fine-tuning learns compared to language pretraining alone, or \emph{whether} training creates new representational structure or reconfigures inherited geometry.
10	Existing analyses have not combined systematic per-layer probing with factorial trained/pretrained/untrained controls, leaving the representational mechanisms of VLA fine-tuning opaque.
11	
12	We address this gap by decomposing OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a VLA chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2}, an MLP projector, and Llama-2 7B~\cite{touvron2023_llama2}.
13	We extract representations from each of 32 LLM layers at both image-token and readout-token positions, and from external baselines (DINOv2~\cite{oquab2024_dinov2}, CLIP~\cite{radford2021_clip}).
14	We compare three LLM conditions (VLA-trained, pretrained Llama-2 base, and randomly initialized) crossed with instruction presence, and apply four complementary analyses: cross-instruction probes for token-level specialization, L1 attention pattern analysis for routing mechanisms, R
…[truncated 2239 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 272 · 2026-05-19T00:50:24.589173+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 273 · 2026-05-19T00:50:24.589667+00:00_

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
14	Meng et al.~\cite{meng2022_rome} developed causal tracing for factual associations, Belrose et al.~\cite{belrose2023_tunedlens} introduced the tuned lens for per-layer prediction, and feature-level methods have scaled to dictionary learning over millions of features~\cite{bills2023language,templeton2024scaling}.
15	Attention probing has shown that individual heads encode syntactic relations~\cite{clark2019}, capture depth-dependent patterns~\cite{vig2019}, and that a small subset accounts for most performance~\cite{voita2019}.
16	Our Layer-1 attention head analysis ext
…[truncated 3039 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 274 · 2026-05-19T00:50:24.740407+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-19T00:50:25.192277+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We investigate how action-relevant structure is distributed across a VLA by combining four complementary analyses: cross-instruction probes, attention pattern analysis, RSA, and functional probes.
5	
6	%------------------------------------------------------------------
7	\subsection{Model and Data}
8	\label{sec:model_data}
9	
10	We study OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\to$ 4{,}096-D), and Llama-2 7B~\cite{touvron2023_llama2} (6.74B parameters) that autoregressively decodes 7-D actions.
11	We use the base checkpoint pretrained on Open X-Embodiment~\cite{padalkar2023_oxe} and evaluate on LIBERO-Goal~\cite{liu2023_libero} (10 tasks, 50 demonstrations each).
12	We compare three LLM conditions: (1)~VLA-trained (released checkpoint), (2)~Llama-2 base (pretrained backbone, no VLA fine-tuning), and (3)~untrained (6.74B parameters reinitialized via \texttt{from\_config()}).
13	All three share the same frozen vision encoder and projector.
14	
15	%------------------------------------------------------------------
16	\subsection{Representation Extraction}
17	\label{sec:repr_extraction}
18	
19	We extract representations from six sources spanning the VLA pipeline:
20	(a)~\textbf{DinoSigLIP+Projector}, the projector output (4{,}096-D), immediately before LLM processing;
21	(b)~\textbf{LLM image\_mean}, the mean image-token activation at each of 32 layers;
22	(c)~\textbf{LLM readout}, the hidden state at the final pre-action token position at each layer (located after both image and instruction tokens in the causal sequence, it can attend to all preceding context and is thus the natural site for multimodal integration before action prediction);
23	(d)~\textbf{DINOv2 ViT-L/14}~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}), a self-supervised baseline;
24
…[truncated 3943 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 276 · 2026-05-19T00:50:25.242874+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 277 · 2026-05-19T00:50:26.097175+00:00_

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
12	This yields $N = 63{,}228$ observations (after excluding terminal frames without next-action labels; $63{,}728$ total); all patterns reproduce with a linear probe (Appendix~\ref{sec:linear_probe}).
13	
14	%------------------------------------------------------------------
15	\subsection{Framework Validation: Token-Level Specialization}
16	\label{sec:token_specialization}
17	
18	As a sanity check on the experimental framework, we train cross-instruction probes (\S\ref{sec:cross_instruction_probes}): given the same visual frame with each of 10 task instructions, we classify which instruction was present from per-layer activations.
19	
20	\paragraph{Image tokens are instruction-blind (expected).}
21	As predicted by the causal mask and frozen encoder, image\_mean instruction classification remains at chance ($10\%$) across all 32 layers in all condit
…[truncated 9696 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 278 · 2026-05-19T00:50:26.097768+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 279 · 2026-05-19T00:50:26.600080+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Synthesis.}
5	VLA fine-tuning primarily reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\Delta \leq 1.7\%$).
6	This explains the visual dominance of Grant et al.~\cite{grant2026}: DINOv2 has the highest geometric alignment ($\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\ $0.634$).
7	Seven complementary analyses support instruction-conditioned action generation through distributed L1 routing, where instruction-attention fraction predicts per-head contribution magnitude.
8	\emph{Causal}: (1)~dose-response curve across 8 conditions ($d = 0.48 \to 0.64$; Figure~\ref{fig:dose_response}); (2)~counterfactual instruction analysis across 4 perturbation types ($d = 0.63$--$0.97$; Table~\ref{tab:counterfactual}).
9	\emph{Supporting}: (3)~three-condition attention gradient ($0 \to 9 \to 24$ instruction-dominant heads); (4)~$R^2$ ablation gradient confined to L1 ($+0.059$ at L1, $\approx 0$ at L13); (5)~trajectory divergence under L1 ablation ($d = 0.65$, $72.3\%$ token divergence).
10	\emph{Constraining}: (6)~per-head bootstrap CIs (individual instruction $d = 0.027$ vs.\ control $d = 0.051$; collective instruction $d = 0.65$ vs.\ control $d = 0.41$; $p = 0.0018$); and~(7)~specificity control ($d$ ratio $1.15\times$; Table~\ref{tab:specificity_control}).
11	
12	\paragraph{Mechanistic interpretation.}
13	The dose-response curve reveals distributed routing: steep rise through 12 heads with diminishing returns beyond 20, consistent with many-weak-head coordination.
14	Token-level specificity (KL ratio $1.56\times$; Table~\ref{tab:specificity_control}) is compressed by the 7-D action bottleneck; counterfactual ordering follows semantic distance.
15	That ablation increases probe $R^2$ yet alters trajectories ($d = 0.65$) is not contradictory: $R^2$ captures continuous pose a
…[truncated 1719 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 280 · 2026-05-19T00:50:26.600490+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 281 · 2026-05-19T00:50:27.052636+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We present a token-level analysis framework for VLAs, finding that fine-tuning reorganizes instruction routing to entry-exit layers rather than reshaping visual geometry; seven complementary analyses identify L1 as the primary routing hub.
5	The framework generalizes to decoder-only VLAs with frozen vision encoders. Code and representations will be released upon acceptance.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 282 · 2026-05-19T00:50:27.053077+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool call

_source line 283 · 2026-05-19T00:50:27.254003+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool result

_source line 284 · 2026-05-19T00:50:27.455452+00:00_

1	\paragraph{Use of Generative AI.}
2	Generative AI tools (Claude, GPT-4) assisted with code implementation and manuscript editing; all scientific content was produced by the authors.
3	
4	\appendix
5	
6	\section{Supplementary Material}
7	\label{sec:appendix}
8	
9	\subsection{CKA Analysis Method}
10	\label{sec:cka_appendix}
11	
12	We employ Centered Kernel Alignment (CKA)~\cite{kornblith2019} alongside RSA as a complementary perspective.
13	While RSA captures local geometric alignment via rank-order preservation, CKA measures global representational similarity through kernel-based comparisons.
14	
15	We compute both \emph{linear CKA}, which uses a linear kernel and is sensitive to second-order statistics, and \emph{RDM kernel CKA}, which operates on the same distance matrices as RSA but aggregates them differently.
16	Using both variants tests whether conclusions about representation structure are robust to the choice of similarity metric.
17	
18	Linear CKA between high-dimensional representations (4{,}096-D for LLM layers) and the 7-D action space is subject to a known dimension mismatch: the linear kernel in the low-dimensional space may not capture the same structure as in the high-dimensional space.
19	RDM kernel CKA avoids this issue by operating on distance matrices of equal size regardless of the original feature dimensionality.
20	
21	\subsection{Metric Sensitivity: RSA versus CKA}
22	\label{sec:metric_sensitivity_appendix}
23	
24	Linear CKA~\cite{kornblith2019} reverses the RSA ordering: untrained LLM ($\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially inverting the self-supervised advantage (Figure~\ref{fig:metric_comparison}).
25	RDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $\approx$ Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).
26	This divergence reflects the known sensitivity of representation similarity metrics to different geometric properties.
…[truncated 41578 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool result

_source line 285 · 2026-05-19T00:50:33.882816+00:00_

Web search results for query: "CoRL 2026 reviewer guidelines review form criteria"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"CVPR 2026 Reviewer Guidelines","url":"https://cvpr.thecvf.com/Conferences/2026/ReviewerGuidelinesq"},{"title":"Which Coauthor Should I Nominate in My 99 ICLR Submissions? A Mathematical Analysis of the ICLR 2026 Reciprocal Reviewer Nomination Policy","url":"https://arxiv.org/pdf/2512.17950"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"}]

Based on the search results, I found information about CoRL 2026, though specific CoRL 2026 reviewer guidelines and review form criteria were not explicitly detailed in the results. However, here's what I found:

## CoRL 2026 Reviewer Requirements

All submissions must include at least one author who agrees to serve as a CoRL reviewer, and they are qualified if they have at least one accepted publication at a previous robotics (CoRL/ICRA/IROS/RSS) or learning conference (ICLR/NeurIPS/ICML) or equivalent journal. Additionally, every author with 3 or more submissions must agree to serve as a reviewer.

## Related Submission Criteria

For reviewing purposes, submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics, with authors encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots. All submissions should include a Limitations section, explicitly describing limiting assumptions, failure modes, and ot
…[truncated 458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6628
}
```

</details>

---


### Tool call

_source line 286 · 2026-05-19T00:50:39.153465+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
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

_source line 287 · 2026-05-19T00:50:39.204018+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 288 · 2026-05-19T00:50:53.165128+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2024.corl.org/contributions/instruction-for-reviews",
  "prompt": "Extract the complete review form criteria, scoring dimensions, rating scales, and any specific evaluation guidelines for reviewers. Include all numbered questions, rating scales (e.g., 1-5 or 1-10), and descriptions of what each score means."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2024.corl.org/contributions/instruction-for-reviews",
    "prompt": "Extract the complete review form criteria, scoring dimensions, rating scales, and any specific evaluation guidelines for reviewers. Include all numbered questions, rating scales (e.g., 1-5 or 1-10), and descriptions of what each score means."
  }
}
```

</details>

---


### Tool call

_source line 289 · 2026-05-19T00:50:53.617796+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2024 2025 review form scoring dimensions rating scale soundness significance novelty"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2024 2025 review form scoring dimensions rating scale soundness significance novelty"
  }
}
```

</details>

---


### Tool result

_source line 290 · 2026-05-19T00:50:58.007950+00:00_

# CoRL 2024 Review Criteria - Summary

Based on the provided content, the document does **not contain a complete review form with scoring dimensions or rating scales**. 

The available guidance includes:

## Review Criteria for Regular Papers

Reviewers should evaluate submissions on:
- "Significance and novelty of the results, either theoretical or empirical"
- Degree of objective establishment and potential scientific/technological impact
- Relevance to robotic learning

The conference accepts papers with "both experimental and theoretical results relevant to robot learning."

## Desk Rejection Criteria

Rather than a scoring rubric, the document outlines three grounds for desk rejection:
1. Formatting issues (length or format violations)
2. Anonymity violations
3. Scope issues—submissions must demonstrate relevance through either intent (addressing learning questions for physical robots) or outcome (testing solutions on physical robots)

## Reviewer Qualifications

Reviewers should demonstrate expertise through "a minimum of 3 first author publications in major robotics conferences and journals" and core machine learning venues.

**Note:** The document provides evaluation principles but does not include a structured rating scale (such as 1-5 or 1-10), numbered evaluation questions, or detailed score interpretations that are typical of formal review forms.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 4842
}
```

</details>

---


### Tool result

_source line 291 · 2026-05-19T00:51:00.769729+00:00_

Web search results for query: "CoRL 2024 2025 review form scoring dimensions rating scale soundness significance novelty"

Links: [{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"What Drives Paper Acceptance? A Process-Centric Analysis of Modern Peer Review","url":"https://arxiv.org/pdf/2509.25701"},{"title":"Correction: Measuring novelty in science with word embedding","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12857975/"},{"title":"Can Small and Reasoning Large Language Models Score Journal Articles for Research Quality and Do Averaging and Few-shot Help?","url":"https://arxiv.org/pdf/2510.22389"},{"title":"CoRL 2024 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/corl-paper-list/corl-2024-paper-list/"},{"title":"CoRL 2024 - Instruction for Authors","url":"https://2024.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2025 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/corl-paper-list/corl-2025-paper-list/"}]

Based on the search results, I found relevant information about CoRL review criteria:

## CoRL 2024 Review Criteria

Submissions are evaluated based on the significance and novelty of the results, either theoretical or empirical. Results are judged on the degree to which they have been objectively established and/or their potential for scientific and technological impact, as well as their relevance to robotic learning.

## Reviewer Guidelines

While the search results don't contain a detailed 2024/2025 rating scale, the CoRL 2023 reviewer guidelines provide insight into the evaluation dimensions used:

- **Quality (Soundness)**: Is the submission technically sound? Are claims well supported (e.g., by theoretical analysis or experi
…[truncated 728 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7151
}
```

</details>

---


### Tool call

_source line 292 · 2026-05-19T00:51:04.691045+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl2023.org/reviewer-guidelines",
  "prompt": "Extract the COMPLETE review form: all scoring dimensions, rating scales (1-5, 1-10 etc), what each score means, all questions reviewers must answer, confidence rating, overall recommendation scale. Include everything."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl2023.org/reviewer-guidelines",
    "prompt": "Extract the COMPLETE review form: all scoring dimensions, rating scales (1-5, 1-10 etc), what each score means, all questions reviewers must answer, confidence rating, overall recommendation scale. Include everything."
  }
}
```

</details>

---


### Tool result

_source line 293 · 2026-05-19T00:51:09.863455+00:00_

# CoRL 2023 Review Form Analysis

Based on the provided guidelines, **the complete review form structure is not fully detailed in this document**. Here's what is specified:

## Review Dimensions Required

The guidelines mandate evaluation across six criteria:

1. **Originality** – novelty of problems/methods and differentiation from prior work
2. **Quality** – technical soundness and substantiation of claims
3. **Clarity** – writing quality and reproducibility of results
4. **Significance** – importance and potential impact on the field
5. **Relevance** – alignment with robot learning and CoRL audience interests
6. **Limitations** – assessment of how authors acknowledge constraints

## Missing Details

The document **does not provide**:
- Specific rating scales (e.g., 1-5, 1-10)
- Numerical score definitions for each dimension
- Confidence rating scale
- Overall recommendation options (accept/reject/borderline)
- Complete question wording for the formal review form

## What Is Specified

Reviewers must include:
- "Summary of Paper" section using original language
- "Main Review" addressing the six dimensions above
- Constructive feedback with concrete citations when critiquing novelty or methodology

**Note**: The full scoring rubric and recommendation scale appear to be delivered separately via OpenReview system email, not in these guidelines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5172
}
```

</details>

---


### Tool call

_source line 294 · 2026-05-19T00:51:13.227302+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL OpenReview review form \"overall score\" \"1:\" \"2:\" \"3:\" rating scale accept reject"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL OpenReview review form \"overall score\" \"1:\" \"2:\" \"3:\" rating scale accept reject"
  }
}
```

</details>

---


### Tool result

_source line 295 · 2026-05-19T00:51:18.801146+00:00_

Web search results for query: "CoRL OpenReview review form "overall score" "1:" "2:" "3:" rating scale accept reject"

Links: [{"title":"Default Review Form | OpenReview","url":"https://docs.openreview.net/reference/default-forms/default-review-form"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"Paper Ranking Methodology","url":"https://openreview-copilot.eamag.me/ranking"},{"title":"Why are the \"rating\" and \"confidence\" fields in my PC Console wrong? | OpenReview","url":"https://docs.openreview.net/getting-started/frequently-asked-questions/why-are-the-rating-and-confidence-fields-in-my-pc-console-wrong"},{"title":"An Open Review of OpenReview: A Critical Analysis of the Machine   Learning Conference Review Process","url":"https://arxiv.org/pdf/2010.05137"},{"title":"ICML 2024 Reviewer Instructions","url":"https://icml.cc/Conferences/2024/ReviewerInstructions"}]

I found information about OpenReview's default review form rating scale. The standard OpenReview default review form uses a 10-point rating scale with options ranging from "10: Top 5% of accepted papers, seminal paper" down through "1: Trivial or wrong".

However, the search results don't contain specific information about CoRL's (Conference on Robot Learning) custom review form with the exact format you mentioned ("overall score" with "1:", "2:", "3:" ratings and accept/reject language). The search returned general OpenReview documentation and CoRL 2023 reviewer guidelines, but not the specific review form configuration you're looking for.

To find the exact CoRL OpenReview review form with those specific rating options, you might want to:
1. Visit the specific CoRL conference year's OpenReview page directly
2. Check the CoRL call for papers or reviewer guidelines for that year
3. Contact the CoRL organizers directly

Would you like me to search for a specific year of CoRL or other related information?


REMINDER: You MUST include the sourc
…[truncated 64 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 5573
}
```

</details>

---


### Tool call

_source line 296 · 2026-05-19T00:51:24.279376+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://docs.openreview.net/reference/default-forms/default-review-form",
  "prompt": "Extract the complete default review form: all fields, all rating scales with exact text for each score level (1-10 or whatever scale), confidence scale, soundness scale, presentation scale, contribution scale, overall rating scale. Include every score option text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://docs.openreview.net/reference/default-forms/default-review-form",
    "prompt": "Extract the complete default review form: all fields, all rating scales with exact text for each score level (1-10 or whatever scale), confidence scale, soundness scale, presentation scale, contribution scale, overall rating scale. Include every score option text."
  }
}
```

</details>

---


### Tool result

_source line 297 · 2026-05-19T00:51:28.348499+00:00_

# Default Review Form - Complete Field Extract

## Fields Present

The form contains **4 fields**:

1. **Title** - Text input (0-500 characters): "Brief summary of your review."

2. **Review** - Textarea with Markdown support (1-20,000 characters): Evaluation of quality, clarity, originality, and significance with pros/cons.

3. **Rating** - Dropdown selection with 10-point scale

4. **Confidence** - Radio buttons with 5-point scale

## Rating Scale (10-Point)

| Score | Description |
|-------|-------------|
| 10 | "Top 5% of accepted papers, seminal paper" |
| 9 | "Top 15% of accepted papers, strong accept" |
| 8 | "Top 50% of accepted papers, clear accept" |
| 7 | "Good paper, accept" |
| 6 | "Marginally above acceptance threshold" |
| 5 | "Marginally below acceptance threshold" |
| 4 | "Ok but not good enough - rejection" |
| 3 | "Clear rejection" |
| 2 | "Strong rejection" |
| 1 | "Trivial or wrong" |

## Confidence Scale (5-Point)

| Level | Description |
|-------|-------------|
| 5 | "Absolutely certain...very familiar with relevant literature" |
| 4 | "Confident but not absolutely certain" |
| 3 | "Fairly confident" |
| 2 | "Willing to defend...likely didn't understand central parts" |
| 1 | "Evaluation is an educated guess" |

**Note:** No separate soundness, presentation, or contribution scales exist in this default form.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 4069
}
```

</details>

---


### Tool call

_source line 298 · 2026-05-19T00:51:34.527192+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 299 · 2026-05-19T00:51:34.527653+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 300 · 2026-05-19T00:51:37.491833+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 301 · 2026-05-19T00:51:37.542807+00:00_

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
…[truncated 16770 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 302 · 2026-05-19T00:53:04.963262+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
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

_source line 303 · 2026-05-19T00:53:05.014105+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 304 · 2026-05-19T00:54:56.940230+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 审稿报告：方法严谨性 + 实验设计\n\n**论文**: \"Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\"\n**Venue**: CoRL 2026\n**审稿模式**: fresh\n\n---\n\n## 总体评分\n**Overall**: 5/10 — Marginally below acceptance threshold\n**一句话总结**: 方法框架全面、透明度高，但核心因果推断 claim 被 open-loop 局限和 ablation 结果内部矛盾所削弱；统计方法存在多处效力/独立性问题；单模型单 benchmark 范围过窄。\n\n---\n\n## 官方维度打分（CoRL review form / OpenReview 标准）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 3/5 | Token-level 分解 + factorial control 的组合有新意，但各分析方法(RSA/probing/attention analysis)均为已有技术的直接应用，无方法论创新 |\n| Quality (Soundness) | 2/5 | 多处统计方法问题（详见下文）；random-subset ablation 结果与核心叙事矛盾；\"causal\" claim 在 open-loop 设定下过度 |\n| Clarity | 4/5 | 写作清晰，结构合理，robustness 分析详尽；Appendix 丰富 |\n| Significance | 2/5 | 单模型(OpenVLA-7B) + 单 benchmark 族(LIBERO)，无闭环验证，实际影响有限；对 robotics 社区的 actionable takeaway 不足 |\n| Relevance | 3/5 | VLA 内部机制分析对 robotics community 有价值，但缺乏真实机器人实验或 sim-to-real 讨论 |\n| Limitations | 4/5 | 诚实标注了 open-loop 和 single-model 限制，但对统计方法局限的讨论不足 |\n\n**Confidence**: 4/5 — 对 representational analysis 和统计方法较熟悉\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Random-subset ablation 结果与核心叙事矛盾\n- 具体位置：§4.3 第 4 段 + Appendix §A.6 (Figure A.5)\n- 问题：论文的核心 claim 是 L1 的 24 个 instruction-dominant heads 是 instruction routing 的功能载体。但 ablation 实验显示，移除这 24 个 dominant heads 使 action probe R² **增加** +0.042，而随机 24 heads 的 ablation R² 增加更大（+0.077）。这意味着：(a) 移除 instruction routing 反而让 action 更容易解码，与 routing 的功能重要性矛盾；(b) dominant heads 的效应甚至弱于随机 heads，z=-2.73 的方向与\"这些 heads 功能重要\"的预期相反。\n- 论文的解释（\"dominant heads 携带 structured noise for the probe\"）是 post-hoc rationalization，缺乏独立验证。如果 instruction signal 真的是\"结构化噪声\"，那么论文关于 instruction routing 驱动 action generation 的整个叙事都需要重新审视。\n- 为什么影响接收：这是论文最核心 claim（C2: instruction routing）的直接实验反证。论文在 Discussion §5 中试图用\"R² captures continuous pose accuracy, whereas task success also requires correct discrete gripper timing\"来调和，但这个解释同样适用于 random ablation，无法解释为什么 random ablation 效果更大。\n\n**N2** [critical] \"Causal\" claim 在 open-loop 设定下不成立\n- 具体位置：Discussion §5 第 1 段，将 dose-response 和 counterfactual 标记为 \"Causal\" 证据\n- 问题：所有分析均为 representational/open-loop——在冻结的模型上修改 attention 并测量 action token 变化。这不是因果推断的标准含义。真正的因果验证需要闭环评估：ablate L1 heads → 部署模型 → 测量 task success rate。论文在 Limitations 中承认了这一点（\"closed-loop evaluation is future work\"），但 Discussion 中仍然明确使用 \"Causal\" 标签分类证据。\n- 为什么影响接收：CoRL 社区重视实际机器人性能。在缺乏闭环验证的情况下声称因果关系，会被审稿人视为 overclaim。应将措辞改为 \"interventional\" 或 \"quasi-causal\"，或提供至少一个 task 的闭环结果。\n\n**N3** [critical] Counterfactual instruction ordering 与 semantic distance 叙事不符\n- 具体位置：§4.3 第 7 段 + Table A.7\n- 问题：论文声称 counterfactual 排序 \"follows semantic distance from the original instruction\"：empty (d=0.968) > wrong (d=0.844) > paraphrased (d=0.697) > shuffled (d=0.625)。但 paraphrased（同义不同词）在语义上应比 shuffled（同词乱序）更**接近**原始指令。paraphrased 产生更大 divergence (0.697 > 0.625) 说明模型对 token identity 比对语义更敏感——这恰好支持 Grant et al. [2026] 的 \"language instructions largely ignored\" 结论，与本文叙事（instruction routing 有功能意义）形成张力。\n- 论文未讨论这一 ordering anomaly。\n- 为什么影响接收：这直接关系到 instruction routing 是否真的在做语义层面的 instruction-conditioned action generation，还是仅仅对 token surface form 敏感。\n\n**N4** [critical] 统计功效不足以支撑核心比较\n- 具体位置：§3.5 (RSA bootstrap)；§4.4 (training effects)\n- 问题：RSA bootstrap 在 task level 重采样，有效 N=10。论文自己在 Appendix §A.10 承认 \"the n.s. result on Goal reflects limited statistical power rather than a true null\"。但主文 §4.4 仍将 best-vs-best RSA gain 报告为 \"non-significant (Δρ=0.017, 3%)\" 并据此得出 \"training enhances decodability, not geometry\" 这一核心结论。在 N=10 下，power 分析表明检测 Δ=0.017 的 effect 需要远大于 10 的样本量。论文不能基于 underpowered 的 non-significance 得出 negative conclusion。\n- 建议：要么增加 task 数量，要么明确标注为 \"inconclusive due to limited power\"，不能将 absence of evidence 等同于 evidence of absence。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Probe 严重过参数化\n- 具体位置：§3.6 + Appendix §A.9\n- 问题：MLP probe（input→256→7）的 N/params 约 0.06，严重过参数化。虽然 Appendix 用 linear probe 复现了定性模式，但主文报告的所有具体 R² 值和差异（如 +0.069）均来自过参数化的 MLP probe。在 N/params < 1 的条件下，R² 差异的精确数值不可信。\n- 建议：主文应以 linear probe 结果为主，或增加 regularization (dropout/weight decay) 的 MLP 变体。\n\n**W2** [warning] N=63,228 的独立性假设\n- 具体位置：§4.1\n- 问题：63,228 个 observations 来自 10 tasks × 50 demos × ~126 frames/demo。同一 demo 内的 frames 存在强时间自相关。Demo-level 的 train/test split 解决了泄露问题，但 probe R² 的 bootstrap 比较中，有效独立单元数远小于 63,228。论文未报告按 demo-level 或 task-level 聚合后的统计量。\n- 建议：报告 cluster-robust 标准误或按 demo 聚合后的统计量。\n\n**W3** [warning] Cohen's d 的独立性假设违反\n- 具体位置：§4.3（dose-response, counterfactual, trajectory divergence）\n- 问题：Cohen's d 假设 observations 独立。Action tokens 在同一 trajectory 内强烈相关。将每个 action token 作为独立观测计算 d 会系统性高估 effect size。论文报告的 d=0.48-0.97 的绝对值不可靠。\n- 建议：以 trajectory 为单位计算 d，或使用 mixed-effects model。\n\n**W4** [warning] Pretrained Llama-2 base control 的有效性\n- 具体位置：§3.2 + Appendix §A.8\n- 问题：Llama-2 base 从未见过 projected visual tokens。Appendix 的三项诊断（activation magnitude, cosine decay, PCA variance）仅证明表征非退化，但不证明其与 VLA-trained 表征具有可比性。关键混淆因素：Llama-2 base 在 L1 显示 9/32 instruction-dominant heads，但这可能纯粹因为 instruction tokens 是 Llama-2 的 in-distribution input，而 image tokens 是 OOD——模型自然更多 attend to 它\"认识\"的 tokens。这与\"language pretraining seeds partial instruction routing\"的解读不同。\n- 论文未控制这一混淆因素。\n\n**W5** [warning] Specificity control 效果有限\n- 具体位置：Appendix §A.16, Table A.18\n- 问题：Top-24 vs Bottom-24 heads 有 16 heads 重叠。d ratio 仅 1.15×，说明 instruction-dominant 标签的特异性有限——任何 24 heads 的 ablation 都产生类似效果。KL ratio 1.56× 稍好，但两个指标的不一致性削弱了 specificity 的 claim。\n\n**W6** [warning] 单模型范围\n- 具体位置：全文\n- 问题：仅研究 OpenVLA-7B。Discussion §5 对 π₀ (cross-attention) 和 RT-2 (decoder-only) 做出三条预测，但均未验证。CoRL 社区期望至少覆盖一个额外架构来支撑泛化性 claim。\n- Contribution (i) 声称 \"a systematic experimental framework\"，但 framework 的泛化性仅在同一模型的两个 LIBERO suite 上验证过。\n\n---\n\n## 小问题（不影响接收）\n\n- Table 1 caption 中 \"Accuracy gap (99.6% vs. 100.0%)\" 的解释不够清晰，需要读正文才能理解两个 split 的区别。\n- §4.3 脚注提到 \"R² values differ from Table 3 due to the feature reconstruction pipeline\"——同一指标在不同 pipelines 下取不同值，会让读者困惑。建议统一或更明确解释差异来源。\n- Appendix Table A.5 (per-dim MAE) 的 Control 行缺少 dx-rz 的具体数值（只有 \"---\"），与 Table A.9 重复但格式不同。\n- 论文未提供 Generative AI 使用声明的具体 section 编号（在 appendix 开头，但未编号），CoRL 可能要求更规范的标注。\n- references.bib 中 nostalgebraist2020 的 note 字段包含 \"Accessed: 2026-05-18\"——这暴露了准确的写作时间，在 double-blind 审稿中虽不是 anonymity violation，但不够审慎。\n\n---\n\n## 主要优势\n\n1. **多方法互证框架**：结合 cross-instruction probes、attention analysis、RSA、functional probes、dose-response ablation、counterfactual analysis、specificity controls，形成了迄今为止最系统的 VLA 内部表征分析。\n2. **三条件 factorial 设计**（trained/pretrained/untrained）是该领域的方法论进步，大多数先前工作缺少 untrained 和 pretrained baselines 的对比。\n3. **透明报告 metric divergence**：RSA 与 CKA 的分歧被正面讨论而非回避（§4.4, Appendix §A.1-A.2），这在分析类论文中属于高标准。\n4. **丰富的 robustness 分析**：seed sensitivity (5 seeds)、demo subsampling、distance metric invariance、threshold sensitivity、linear vs MLP probe、cross-benchmark，覆盖面广。\n5. **清晰的写作**：主文紧凑，关键发现在 Introduction 和 Discussion 中有一致的叙事线。\n\n---\n\n## Questions for Authors\n\nQ1: 关于 N1——如果移除 instruction-dominant heads 使 R² 增加而非减少，且增幅小于 random ablation，你们如何排除以下解释：instruction routing 实际上是一个与 action prediction 无关（甚至有害）的 artifact，而非功能性贡献？\n\nQ2: 关于 N3——你们是否计算了 paraphrased 和 shuffled instructions 的 token overlap rate 或 embedding-level cosine similarity？如果 paraphrased 的 token overlap 远低于 shuffled，那么 d ordering 反映的是 token-level sensitivity 而非 semantic distance。\n\nQ3: 关于 W2——如果将 bootstrap 单位从 observation-level 改为 demo-level (N_eff ≈ 500)，主要结论的 p-values 是否仍然显著？\n\nQ4: Discussion §5 提到 L14-L32 (~56% 参数) 是 \"potential pruning or distillation targets\"。这个 claim 基于 open-loop probe R² 下降。是否有任何证据（即使是 preliminary 的）表明 pruning 这些层不会严重损害 closed-loop 性能？\n\n---\n\n## 格式合规检查\n\n- [x] Double-blind：满足（author 为 Anonymous）\n- [x] 页数：主文约 8 页（需编译确认）\n- [x] Limitations section：在 Discussion §5 中\n- [x] Generative AI 声明：在 Appendix 开头\n- [ ] 模板：使用 `\\usepackage{corl_2026}`，无法从 .tex 确认是否为官方最新版\n- 行号：未在 .tex 中看到 `\\usepackage{lineno}` 或类似设置，需确认 corl_2026.sty 是否自带行号\n\n",
  "reviewer_id": "1",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 审稿报告：方法严谨性 + 实验设计\n\n**论文**: \"Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\"\n**Venue**: CoRL 2026\n**审稿模式**: fresh\n\n---\n\n## 总体评分\n**Overall**: 5/10 — Marginally below acceptance threshold\n**一句话总结**: 方法框架全面、透明度高，但核心因果推断 claim 被 open-loop 局限和 ablation 结果内部矛盾所削弱；统计方法存在多处效力/独立性问题；单模型单 benchmark 范围过窄。\n\n---\n\n## 官方维度打分（CoRL review form / OpenReview 标准）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 3/5 | Token-level 分解 + factorial control 的组合有新意，但各分析方法(RSA/probing/attention analysis)均为已有技术的直接应用，无方法论创新 |\n| Quality (Soundness) | 2/5 | 多处统计方法问题（详见下文）；random-subset ablation 结果与核心叙事矛盾；\"causal\" claim 在 open-loop 设定下过度 |\n| Clarity | 4/5 | 写作清晰，结构合理，robustness 分析详尽；Appendix 丰富 |\n| Significance | 2/5 | 单模型(OpenVLA-7B) + 单 benchmark 族(LIBERO)，无闭环验证，实际影响有限；对 robotics 社区的 actionable takeaway 不足 |\n| Relevance | 3/5 | VLA 内部机制分析对 robotics community 有价值，但缺乏真实机器人实验或 sim-to-real 讨论 |\n| Limitations | 4/5 | 诚实标注了 open-loop 和 single-model 限制，但对统计方法局限的讨论不足 |\n\n**Confidence**: 4/5 — 对 representational analysis 和统计方法较熟悉\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Random-subset ablation 结果与核心叙事矛盾\n- 具体位置：§4.3 第 4 段 + Appendix §A.6 (Figure A.5)\n- 问题：论文的核心 claim 是 L1 的 24 个 instruction-dominant heads 是 instruction routing 的功能载体。但 ablation 实验显示，移除这 24 个 dominant heads 使 action probe R² **增加** +0.042，而随机 24 heads 的 ablation R² 增加更大（+0.077）。这意味着：(a) 移除 instruction routing 反而让 action 更容易解码，与 routing 的功能重要性矛盾；(b) dominant heads 的效应甚至弱于随机 heads，z=-2.73 的方向与\"这些 heads 功能重要\"的预期相反。\n- 论文的解释（\"dominant heads 携带 structured noise for the probe\"）是 post-hoc rationalization，缺乏独立验证。如果 instruction signal 真的是\"结构化噪声\"，那么论文关于 instruction routing 驱动 action generation 的整个叙事都需要重新审视。\n- 为什么影响接收：这是论文最核心 claim（C2: instruction routing）的直接实验反证。论文在 Discussion §5 中试图用\"R² captures continuous pose accuracy, whereas task success also requires correct discrete gripper timing\"来调和，但这个解释同样适用于 random ablation，无法解释为什么 random ablation 效果更大。\n\n**N2** [critical] \"Causal\" claim 在 open-loop 设定下不成立\n- 具体位置：Discussion §5 第 1 段，将 dose-response 和 counterfactual 标记为 \"Causal\" 证据\n- 问题：所有分析均为 representational/open-loop——在冻结的模型上修改 attention 并测量 action token 变化。这不是因果推断的标准含义。真正的因果验证需要闭环评估：ablate L1 heads → 部署模型 → 测量 task success rate。论文在 Limitations 中承认了这一点（\"closed-loop evaluation is future work\"），但 Discussion 中仍然明确使用 \"Causal\" 标签分类证据。\n- 为什么影响接收：CoRL 社区重视实际机器人性能。在缺乏闭环验证的情况下声称因果关系，会被审稿人视为 overclaim。应将措辞改为 \"interventional\" 或 \"quasi-causal\"，或提供至少一个 task 的闭环结果。\n\n**N3** [critical] Counterfactual instruction ordering 与 semantic distance 叙事不符\n- 具体位置：§4.3 第 7 段 + Table A.7\n- 问题：论文声称 counterfactual 排序 \"follows semantic distance from the original instruction\"：empty (d=0.968) > wrong (d=0.844) > paraphrased (d=0.697) > shuffled (d=0.625)。但 paraphrased（同义不同词）在语义上应比 shuffled（同词乱序）更**接近**原始指令。paraphrased 产生更大 divergence (0.697 > 0.625) 说明模型对 token identity 比对语义更敏感——这恰好支持 Grant et al. [2026] 的 \"language instructions largely ignored\" 结论，与本文叙事（instruction routing 有功能意义）形成张力。\n- 论文未讨论这一 ordering anomaly。\n- 为什么影响接收：这直接关系到 instruction routing 是否真的在做语义层面的 instruction-conditioned action generation，还是仅仅对 token surface form 敏感。\n\n**N4** [critical] 统计功效不足以支撑核心比较\n- 具体位置：§3.5 (RSA bootstrap)；§4.4 (training effects)\n- 问题：RSA bootstrap 在 task level 重采样，有效 N=10。论文自己在 Appendix §A.10 承认 \"the n.s. result on Goal reflects limited statistical power rather than a true null\"。但主文 §4.4 仍将 best-vs-best RSA gain 报告为 \"non-significant (Δρ=0.017, 3%)\" 并据此得出 \"training enhances decodability, not geometry\" 这一核心结论。在 N=10 下，power 分析表明检测 Δ=0.017 的 effect 需要远大于 10 的样本量。论文不能基于 underpowered 的 non-significance 得出 negative conclusion。\n- 建议：要么增加 task 数量，要么明确标注为 \"inconclusive due to limited power\"，不能将 absence of evidence 等同于 evidence of absence。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Probe 严重过参数化\n- 具体位置：§3.6 + Appendix §A.9\n- 问题：MLP probe（input→256→7）的 N/params 约 0.06，严重过参数化。虽然 Appendix 用 linear probe 复现了定性模式，但主文报告的所有具体 R² 值和差异（如 +0.069）均来自过参数化的 MLP probe。在 N/params < 1 的条件下，R² 差异的精确数值不可信。\n- 建议：主文应以 linear probe 结果为主，或增加 regularization (dropout/weight decay) 的 MLP 变体。\n\n**W2** [warning] N=63,228 的独立性假设\n- 具体位置：§4.1\n- 问题：63,228 个 observations 来自 10 tasks × 50 demos × ~126 frames/demo。同一 demo 内的 frames 存在强时间自相关。Demo-level 的 train/test split 解决了泄露问题，但 probe R² 的 bootstrap 比较中，有效独立单元数远小于 63,228。论文未报告按 demo-level 或 task-level 聚合后的统计量。\n- 建议：报告 cluster-robust 标准误或按 demo 聚合后的统计量。\n\n**W3** [warning] Cohen's d 的独立性假设违反\n- 具体位置：§4.3（dose-response, counterfactual, trajectory divergence）\n- 问题：Cohen's d 假设 observations 独立。Action tokens 在同一 trajectory 内强烈相关。将每个 action token 作为独立观测计算 d 会系统性高估 effect size。论文报告的 d=0.48-0.97 的绝对值不可靠。\n- 建议：以 trajectory 为单位计算 d，或使用 mixed-effects model。\n\n**W4** [warning] Pretrained Llama-2 base control 的有效性\n- 具体位置：§3.2 + Appendix §A.8\n- 问题：Llama-2 base 从未见过 projected visual tokens。Appendix 的三项诊断（activation magnitude, cosine decay, PCA variance）仅证明表征非退化，但不证明其与 VLA-trained 表征具有可比性。关键混淆因素：Llama-2 base 在 L1 显示 9/32 instruction-dominant heads，但这可能纯粹因为 instruction tokens 是 Llama-2 的 in-distribution input，而 image tokens 是 OOD——模型自然更多 attend to 它\"认识\"的 tokens。这与\"language pretraining seeds partial instruction routing\"的解读不同。\n- 论文未控制这一混淆因素。\n\n**W5** [warning] Specificity control 效果有限\n- 具体位置：Appendix §A.16, Table A.18\n- 问题：Top-24 vs Bottom-24 heads 有 16 heads 重叠。d ratio 仅 1.15×，说明 instruction-dominant 标签的特异性有限——任何 24 heads 的 ablation 都产生类似效果。KL ratio 1.56× 稍好，但两个指标的不一致性削弱了 specificity 的 claim。\n\n**W6** [warning] 单模型范围\n- 具体位置：全文\n- 问题：仅研究 OpenVLA-7B。Discussion §5 对 π₀ (cross-attention) 和 RT-2 (decoder-only) 做出三条预测，但均未验证。CoRL 社区期望至少覆盖一个额外架构来支撑泛化性 claim。\n- Contribution (i) 声称 \"a systematic experimental framework\"，但 framework 的泛化性仅在同一模型的两个 LIBERO suite 上验证过。\n\n---\n\n## 小问题（不影响接收）\n\n- Table 1 caption 中 \"Accuracy gap (99.6% vs. 100.0%)\" 的解释不够清晰，需要读正文才能理解两个 split 的区别。\n- §4.3 脚注提到 \"R² values differ from Table 3 due to the feature reconstruction pipeline\"——同一指标在不同 pipelines 下取不同值，会让读者困惑。建议统一或更明确解释差异来源。\n- Appendix Table A.5 (per-dim MAE) 的 Control 行缺少 dx-rz 的具体数值（只有 \"---\"），与 Table A.9 重复但格式不同。\n- 论文未提供 Generative AI 使用声明的具体 section 编号（在 appendix 开头，但未编号），CoRL 可能要求更规范的标注。\n- references.bib 中 nostalgebraist2020 的 note 字段包含 \"Accessed: 2026-05-18\"——这暴露了准确的写作时间，在 double-blind 审稿中虽不是 anonymity violation，但不够审慎。\n\n---\n\n## 主要优势\n\n1. **多方法互证框架**：结合 cross-instruction probes、attention analysis、RSA、functional probes、dose-response ablation、counterfactual analysis、specificity controls，形成了迄今为止最系统的 VLA 内部表征分析。\n2. **三条件 factorial 设计**（trained/pretrained/untrained）是该领域的方法论进步，大多数先前工作缺少 untrained 和 pretrained baselines 的对比。\n3. **透明报告 metric divergence**：RSA 与 CKA 的分歧被正面讨论而非回避（§4.4, Appendix §A.1-A.2），这在分析类论文中属于高标准。\n4. **丰富的 robustness 分析**：seed sensitivity (5 seeds)、demo subsampling、distance metric invariance、threshold sensitivity、linear vs MLP probe、cross-benchmark，覆盖面广。\n5. **清晰的写作**：主文紧凑，关键发现在 Introduction 和 Discussion 中有一致的叙事线。\n\n---\n\n## Questions for Authors\n\nQ1: 关于 N1——如果移除 instruction-dominant heads 使 R² 增加而非减少，且增幅小于 random ablation，你们如何排除以下解释：instruction routing 实际上是一个与 action prediction 无关（甚至有害）的 artifact，而非功能性贡献？\n\nQ2: 关于 N3——你们是否计算了 paraphrased 和 shuffled instructions 的 token overlap rate 或 embedding-level cosine similarity？如果 paraphrased 的 token overlap 远低于 shuffled，那么 d ordering 反映的是 token-level sensitivity 而非 semantic distance。\n\nQ3: 关于 W2——如果将 bootstrap 单位从 observation-level 改为 demo-level (N_eff ≈ 500)，主要结论的 p-values 是否仍然显著？\n\nQ4: Discussion §5 提到 L14-L32 (~56% 参数) 是 \"potential pruning or distillation targets\"。这个 claim 基于 open-loop probe R² 下降。是否有任何证据（即使是 preliminary 的）表明 pruning 这些层不会严重损害 closed-loop 性能？\n\n---\n\n## 格式合规检查\n\n- [x] Double-blind：满足（author 为 Anonymous）\n- [x] 页数：主文约 8 页（需编译确认）\n- [x] Limitations section：在 Discussion §5 中\n- [x] Generative AI 声明：在 Appendix 开头\n- [ ] 模板：使用 `\\usepackage{corl_2026}`，无法从 .tex 确认是否为官方最新版\n- 行号：未在 .tex 中看到 `\\usepackage{lineno}` 或类似设置，需确认 corl_2026.sty 是否自带行号\n\n",
    "reviewer_id": "1",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 305 · 2026-05-19T00:55:01.061534+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4121
}
```

</details>

---


### Assistant

_source line 306 · 2026-05-19T00:55:09.206864+00:00_

审稿报告已提交给 Review Director。

核心判断：**5/10，borderline reject**。论文的多方法互证框架和三条件 factorial 设计有明显方法论贡献，但存在四个 critical 问题：

1. **Random-subset ablation 结果自相矛盾** — 移除 instruction-dominant heads 反而提升 R²，且效果弱于随机 heads，直接削弱核心 routing claim
2. **"Causal" 标签过度** — 全部 open-loop 分析，无闭环验证
3. **Counterfactual ordering 与 semantic distance 叙事不符** — paraphrased > shuffled 暗示 token-level sensitivity 而非语义理解
4. **N=10 tasks 的统计功效不足** — 基于 underpowered non-significance 得出 negative conclusion ("not geometry")

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1"
}
```

</details>

---


## Round 16

## Round 16

4 recorded events


### User

_source line 307 · 2026-05-19T00:56:54.848796+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 2 的完整审稿意见

请逐条回应以下 Reviewer 2 的意见。对每个 Must-Fix 和 Should-Fix 条目，标注 **[AGREE]** 或 **[REBUT]**，并说明理由。如有 REBUT，请引用论文中的具体 Section/Table/Figure 作为证据。

---

以下是 Reviewer 2 的完整审稿原文：

### 总体评分
Overall: 5/10 (Marginally below acceptance threshold)
Confidence: 4/5

### Must-Fix 问题

**N1** [critical] 单模型单基准范围严重限制 generalizability
- 仅研究 OpenVLA-7B，在 LIBERO-Goal 上做主实验（LIBERO-Spatial 为同一模拟器的交叉验证）。Section 5 对 π₀、RT-2、更大 VLA 做了三个预测，但无一经过验证。VLA 领域正快速多样化，单模型发现的迁移性不确定。

**N2** [critical] 完全缺失 closed-loop / task-performance 验证
- 所有分析均为 representational/open-loop。论文声称的最具 robotics 价值的 implications（routing monitoring、layer pruning/distillation、56% 参数潜在可删减）均为未验证的猜测。probe R² 和 trajectory divergence 衡量的是表征质量和动作偏移，而非任务完成率。CoRL 评审标准要求论文 "explicitly address a learning question for physical robots" 或 "test the proposed learning solution on physical robots"。

**N3** [critical] CoRL scope fit 存疑
- 论文本质上是 transformer mechanistic interpretability 论文，碰巧分析对象是 VLA。主要方法来自 NLP interpretability；主要 positioning 对标 NLP/ML 的 interp 工作；主要发现对 robot learning 的指导意义停留在 Discussion 推测层面。更适合 NeurIPS/ICML。

### Should-Fix 问题

**W1** [warning] C1（architecture validation）占比失衡
- C1 是 causal mask + frozen encoder 的必然结果，论文自己称之为 "sanity check"。但 C1 占据了 Abstract 最长的 finding 描述、Introduction 的第一个 finding 段落、一个完整 subsection + Table 1、以及 Contribution 列表的 (i)。权重过高。

**W2** [warning] Vision representation 的训练效果小到可能无实际意义
- RSA best-vs-best Δρ = +0.017 (3%), n.s.。image_mean R² Δ = +0.015 (p=0.006, borderline)。VLA fine-tuning 对 vision representations 的改变非常有限，核心改变集中在 readout routing。Framing 上未充分强调这对 headline question 的含义。

**W3** [warning] 消融 R² 解释反直觉且不充分
- Instruction-dominant heads 消融使 R² 增加 +0.042，random subset 增加更多 (+0.077±0.013)。论文解释 "structured noise for the probe" 反直觉。用 trajectory divergence 和 R² 两个指标得出相反结论，读者难以判断哪个更可信。

**W4** [warning] Counterfactual ordering 与 semantic distance claim 不完全一致
- paraphrased d=0.697 > shuffled d=0.625，但 paraphrase 语义上更接近原始 instruction。实际数据表明模型对 lexical identity 比 syntactic structure 更敏感。

**W5** [warning] 竞争者工作的 positioning 不够深入
- Swann et al. 2026 和 Buurmeijer et al. 2026 的差异化不足。Häon et al. 2025 与 attention-based routing mechanism 的关系未讨论。

**W6** [warning] 缺失引用
- Octo (Ghosh et al. 2024)、Rizzardo et al. 2026 未引用。46 篇引用对 CoRL 在拥挤的 VLA 分析领域偏少。

---

请逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 308 · 2026-05-19T00:58:23.441975+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n## Must-Fix 条目\n\n**[AGREE] R2-N1: 单模型单基准范围严重限制 generalizability**\n\n同意。这与我的 W6 一致。补充一点：论文在 LIBERO-Spatial 上的交叉验证（Appendix §A.10, Figure A.7）虽然复现了 inverted-U 和 cross-instruction probe 的定性模式，但这仍是同一模型 (OpenVLA-7B) 在同一模拟器 (LIBERO) 的不同 task suite 上的测试，不能算 model-level generalization。Discussion §5 的三条预测（π₀ 无 L1 routing heads、RT-2 有类似 entry-layer routing、larger VLAs 更平坦的 per-head contribution）是论文最有价值的可检验假设，但全部停留在推测。至少应验证一个预测（例如 RT-2 的 attention profile）来增强说服力。\n\n---\n\n**[AGREE] R2-N2: 完全缺失 closed-loop / task-performance 验证**\n\n强烈同意。这与我的 N2 一致。进一步补充：论文中最具 actionable 意味的 claim 有三个——(a) L1 routing monitoring 可在部署时检测 routing integrity (Discussion §5 倒数第 2 段)；(b) L14-L32 约 56% 参数为 pruning/distillation targets (Discussion §5 第 3 段)；(c) instruction-discriminative tasks 对 L1 routing 依赖更强 (Table A.15)。这三个 claim 的实际价值完全取决于闭环验证。特别是 pruning claim：open-loop probe R² 在 L14+ 下降不等于这些层对 closed-loop task success 无贡献——后面的层可能负责 action token decoding 的 fine-grained timing（如 gripper 时机），这恰好是 R² 无法捕捉的。\n\n---\n\n**[REBUT] R2-N3: CoRL scope fit 存疑**\n\n部分不同意，不应作为 critical/must-fix。\n\n理由：\n\n1. CoRL 2023 reviewer guidelines 明确列出 \"Relevance\" 作为评审维度，其定义为 \"alignment with robot learning and CoRL audience interests\"，而非要求必须有 real-robot experiments。CoRL 2024 的 scope 说明也接受 \"results relevant to robot learning\"，包含 theoretical 和 empirical 两类。\n\n2. 论文分析的对象 (OpenVLA-7B) 和 benchmark (LIBERO) 均为 robotics community 的核心产物。与纯 NLP interpretability 工作的区别在于：(a) 分析的 token 类型包括 image tokens 和 action-generating readout tokens，这些在 NLP 中不存在；(b) probe target 是 7-D robot actions 而非 language prediction；(c) 发现的 entry-exit routing pattern 是 VLA fine-tuning 特有的，Llama-2 base 的 mid-depth pattern 恰好证明这不是 LLM 的通用属性。\n\n3. CoRL 历史上接收过多篇纯分析/理解类论文（不含 real-robot experiments），只要其发现对 robot learning 有直接 implications。\n\n4. 不过，R2 的底层担忧是合理的：论文的 positioning 确实过度对标 NLP interpretability 文献（Related Work §2 中 Elhage、Olsson、Wang、Meng、Belrose 等引用占了大量篇幅），而对 robotics-specific 的启示讨论不够具体。建议降级为 warning 而非 critical。\n\n---\n\n## Should-Fix 条目\n\n**[AGREE] R2-W1: C1（architecture validation）占比失衡**\n\n同意。论文在 §4.2 自己将 C1 定位为 \"sanity check on the experimental framework\"，但 C1 占据了：Abstract 第 4 行（最长的 finding 描述）、Introduction §1 第 17 行的 \"First\" 段落、§4.2 完整 subsection + Table 1、Contribution 列表的 (i)。如果作者认为这是预期结果和 framework validation，应压缩到 1-2 句话 + 一个 table，将 page budget 让给更有新意的 C2 和 C3。当前 framing 让读者误以为 C1 是一个实质性发现。\n\n---\n\n**[AGREE] R2-W2: Vision representation 训练效果小到可能无实际意义**\n\n同意。补充定量证据：Table A.14 汇总了所有训练效果——image_mean RSA Δ=+0.017 (n.s.)、R² Δ=+0.015 (p=0.006, borderline under multiple comparisons)。与 last_preaction 的效果对比（R² Δ=+0.069, attention +46pp），vision pathway 的训练效果小一个数量级。论文的叙事应更直接地承认：VLA fine-tuning 对 visual representations 的改变在统计上微弱且可能无实际意义，核心改变完全集中在 readout token 的 routing 机制。当前 framing（§4.4 标题 \"Training enhances decodability, not geometry\"）虽然技术上准确，但用 \"enhances\" 来描述 image_mean R² Δ=+0.015 有夸大嫌疑。\n\n---\n\n**[AGREE] R2-W3: 消融 R² 解释反直觉且不充分**\n\n强烈同意。这与我的 N1 (critical) 一致，我甚至认为应升级为 must-fix 而非 should-fix。核心矛盾：如果 instruction-dominant heads 携带功能性 routing signal，ablation 应该降低 action decodability (R² 下降)，但实验显示 R² 反而增加，且增幅小于 random ablation。\"structured noise\" 的解释需要独立验证——例如，可以检验 ablation 后 readout token 的 representation 维度是否降低（如果 instruction signal 占据了独立的子空间，移除后 effective dimensionality 下降，probe 更容易拟合）。没有这样的验证，\"structured noise\" 仅仅是一个 unfalsifiable 的 post-hoc story。\n\n---\n\n**[AGREE] R2-W4: Counterfactual ordering 与 semantic distance claim 不完全一致**\n\n同意。这与我的 N3 一致。补充：如果论文能报告 4 种 perturbation 条件下 instruction tokens 的 token-level overlap rate（例如 shuffled 保留 100% tokens、paraphrased 可能仅保留 30-50%），读者就能判断 d ordering 反映的是 token identity sensitivity 还是 semantic sensitivity。当前数据实际上暗示 OpenVLA 对 lexical identity 比 semantic content 更敏感，这与 Grant et al. 和 Häon et al. 关于 VLA 语言理解肤浅的发现一致，但论文的 framing 回避了这一解读。\n\n---\n\n**[REBUT] R2-W5: 竞争者工作的 positioning 不够深入**\n\n部分不同意。\n\nRelated Work §2 第 3 段对 Grant et al. [2026] 的差异化是充分的——明确列出三点区别（token-level vs feature-level、per-layer vs whole-model、factorial controls）。Swann et al. [2026] 和 Buurmeijer et al. [2026] 属于 SAE-based interpretability，与本文的 probing + attention analysis 方法正交，不需要逐一深入对比。\n\n但我同意 Häon et al. [2025] 的处理确实不足。Häon et al. 发现了 VLA residual stream 中的 sparse semantic directions linked to action selection，这与本文的 L1 routing heads 发现存在直接互补关系（一个在 feature 层面，一个在 head 层面），应该讨论两者是否捕捉同一机制的不同视角。\n\n---\n\n**[AGREE] R2-W6: 缺失引用**\n\n部分同意。Octo (Ghosh et al. 2024) 是 robotics community 的重要 VLA baseline，应该在 Related Work §2 第 1 段 (VLA 列表) 中被引用，尽管其架构（non-LLM-based）与本文分析对象不同。引用密度对于一篇 analysis/survey 性质的论文确实偏低——同类论文（如 Grant et al. 2026 的 mechanistic study）通常有 50-70 篇引用。\n\n不过，\"46 篇偏少\" 的判断需要对照 CoRL 的平均引用量。CoRL 论文平均引用量通常低于 NeurIPS/ICML（因为 robotics 子领域相对集中），46 篇不一定构成硬伤。\n\n---\n\n## 总结\n\n与 Reviewer 2 的主要共识：N1（单模型）、N2（无闭环验证）、W1-W4。\n主要分歧：N3（scope fit）——我认为降级为 warning 更合适；W5（competitor positioning）——大部分已充分，仅 Häon et al. 需要补充。\n我独有的 critical issues（R2 未覆盖）：N1（random-subset ablation 矛盾）、N3（counterfactual 升级为 critical）、N4（N=10 统计功效不足以支撑 negative conclusion）。\n",
  "reviewer_id": "1",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n## Must-Fix 条目\n\n**[AGREE] R2-N1: 单模型单基准范围严重限制 generalizability**\n\n同意。这与我的 W6 一致。补充一点：论文在 LIBERO-Spatial 上的交叉验证（Appendix §A.10, Figure A.7）虽然复现了 inverted-U 和 cross-instruction probe 的定性模式，但这仍是同一模型 (OpenVLA-7B) 在同一模拟器 (LIBERO) 的不同 task suite 上的测试，不能算 model-level generalization。Discussion §5 的三条预测（π₀ 无 L1 routing heads、RT-2 有类似 entry-layer routing、larger VLAs 更平坦的 per-head contribution）是论文最有价值的可检验假设，但全部停留在推测。至少应验证一个预测（例如 RT-2 的 attention profile）来增强说服力。\n\n---\n\n**[AGREE] R2-N2: 完全缺失 closed-loop / task-performance 验证**\n\n强烈同意。这与我的 N2 一致。进一步补充：论文中最具 actionable 意味的 claim 有三个——(a) L1 routing monitoring 可在部署时检测 routing integrity (Discussion §5 倒数第 2 段)；(b) L14-L32 约 56% 参数为 pruning/distillation targets (Discussion §5 第 3 段)；(c) instruction-discriminative tasks 对 L1 routing 依赖更强 (Table A.15)。这三个 claim 的实际价值完全取决于闭环验证。特别是 pruning claim：open-loop probe R² 在 L14+ 下降不等于这些层对 closed-loop task success 无贡献——后面的层可能负责 action token decoding 的 fine-grained timing（如 gripper 时机），这恰好是 R² 无法捕捉的。\n\n---\n\n**[REBUT] R2-N3: CoRL scope fit 存疑**\n\n部分不同意，不应作为 critical/must-fix。\n\n理由：\n\n1. CoRL 2023 reviewer guidelines 明确列出 \"Relevance\" 作为评审维度，其定义为 \"alignment with robot learning and CoRL audience interests\"，而非要求必须有 real-robot experiments。CoRL 2024 的 scope 说明也接受 \"results relevant to robot learning\"，包含 theoretical 和 empirical 两类。\n\n2. 论文分析的对象 (OpenVLA-7B) 和 benchmark (LIBERO) 均为 robotics community 的核心产物。与纯 NLP interpretability 工作的区别在于：(a) 分析的 token 类型包括 image tokens 和 action-generating readout tokens，这些在 NLP 中不存在；(b) probe target 是 7-D robot actions 而非 language prediction；(c) 发现的 entry-exit routing pattern 是 VLA fine-tuning 特有的，Llama-2 base 的 mid-depth pattern 恰好证明这不是 LLM 的通用属性。\n\n3. CoRL 历史上接收过多篇纯分析/理解类论文（不含 real-robot experiments），只要其发现对 robot learning 有直接 implications。\n\n4. 不过，R2 的底层担忧是合理的：论文的 positioning 确实过度对标 NLP interpretability 文献（Related Work §2 中 Elhage、Olsson、Wang、Meng、Belrose 等引用占了大量篇幅），而对 robotics-specific 的启示讨论不够具体。建议降级为 warning 而非 critical。\n\n---\n\n## Should-Fix 条目\n\n**[AGREE] R2-W1: C1（architecture validation）占比失衡**\n\n同意。论文在 §4.2 自己将 C1 定位为 \"sanity check on the experimental framework\"，但 C1 占据了：Abstract 第 4 行（最长的 finding 描述）、Introduction §1 第 17 行的 \"First\" 段落、§4.2 完整 subsection + Table 1、Contribution 列表的 (i)。如果作者认为这是预期结果和 framework validation，应压缩到 1-2 句话 + 一个 table，将 page budget 让给更有新意的 C2 和 C3。当前 framing 让读者误以为 C1 是一个实质性发现。\n\n---\n\n**[AGREE] R2-W2: Vision representation 训练效果小到可能无实际意义**\n\n同意。补充定量证据：Table A.14 汇总了所有训练效果——image_mean RSA Δ=+0.017 (n.s.)、R² Δ=+0.015 (p=0.006, borderline under multiple comparisons)。与 last_preaction 的效果对比（R² Δ=+0.069, attention +46pp），vision pathway 的训练效果小一个数量级。论文的叙事应更直接地承认：VLA fine-tuning 对 visual representations 的改变在统计上微弱且可能无实际意义，核心改变完全集中在 readout token 的 routing 机制。当前 framing（§4.4 标题 \"Training enhances decodability, not geometry\"）虽然技术上准确，但用 \"enhances\" 来描述 image_mean R² Δ=+0.015 有夸大嫌疑。\n\n---\n\n**[AGREE] R2-W3: 消融 R² 解释反直觉且不充分**\n\n强烈同意。这与我的 N1 (critical) 一致，我甚至认为应升级为 must-fix 而非 should-fix。核心矛盾：如果 instruction-dominant heads 携带功能性 routing signal，ablation 应该降低 action decodability (R² 下降)，但实验显示 R² 反而增加，且增幅小于 random ablation。\"structured noise\" 的解释需要独立验证——例如，可以检验 ablation 后 readout token 的 representation 维度是否降低（如果 instruction signal 占据了独立的子空间，移除后 effective dimensionality 下降，probe 更容易拟合）。没有这样的验证，\"structured noise\" 仅仅是一个 unfalsifiable 的 post-hoc story。\n\n---\n\n**[AGREE] R2-W4: Counterfactual ordering 与 semantic distance claim 不完全一致**\n\n同意。这与我的 N3 一致。补充：如果论文能报告 4 种 perturbation 条件下 instruction tokens 的 token-level overlap rate（例如 shuffled 保留 100% tokens、paraphrased 可能仅保留 30-50%），读者就能判断 d ordering 反映的是 token identity sensitivity 还是 semantic sensitivity。当前数据实际上暗示 OpenVLA 对 lexical identity 比 semantic content 更敏感，这与 Grant et al. 和 Häon et al. 关于 VLA 语言理解肤浅的发现一致，但论文的 framing 回避了这一解读。\n\n---\n\n**[REBUT] R2-W5: 竞争者工作的 positioning 不够深入**\n\n部分不同意。\n\nRelated Work §2 第 3 段对 Grant et al. [2026] 的差异化是充分的——明确列出三点区别（token-level vs feature-level、per-layer vs whole-model、factorial controls）。Swann et al. [2026] 和 Buurmeijer et al. [2026] 属于 SAE-based interpretability，与本文的 probing + attention analysis 方法正交，不需要逐一深入对比。\n\n但我同意 Häon et al. [2025] 的处理确实不足。Häon et al. 发现了 VLA residual stream 中的 sparse semantic directions linked to action selection，这与本文的 L1 routing heads 发现存在直接互补关系（一个在 feature 层面，一个在 head 层面），应该讨论两者是否捕捉同一机制的不同视角。\n\n---\n\n**[AGREE] R2-W6: 缺失引用**\n\n部分同意。Octo (Ghosh et al. 2024) 是 robotics community 的重要 VLA baseline，应该在 Related Work §2 第 1 段 (VLA 列表) 中被引用，尽管其架构（non-LLM-based）与本文分析对象不同。引用密度对于一篇 analysis/survey 性质的论文确实偏低——同类论文（如 Grant et al. 2026 的 mechanistic study）通常有 50-70 篇引用。\n\n不过，\"46 篇偏少\" 的判断需要对照 CoRL 的平均引用量。CoRL 论文平均引用量通常低于 NeurIPS/ICML（因为 robotics 子领域相对集中），46 篇不一定构成硬伤。\n\n---\n\n## 总结\n\n与 Reviewer 2 的主要共识：N1（单模型）、N2（无闭环验证）、W1-W4。\n主要分歧：N3（scope fit）——我认为降级为 warning 更合适；W5（competitor positioning）——大部分已充分，仅 Häon et al. 需要补充。\n我独有的 critical issues（R2 未覆盖）：N1（random-subset ablation 矛盾）、N3（counterfactual 升级为 critical）、N4（N=10 统计功效不足以支撑 negative conclusion）。\n",
    "reviewer_id": "1",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 309 · 2026-05-19T00:58:27.410580+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3968
}
```

</details>

---


### Assistant

_source line 310 · 2026-05-19T00:58:33.378281+00:00_

交叉回应已提交。总结：

- **与 R2 共识**：N1（单模型）、N2（无闭环验证）、W1-W4 全部 AGREE
- **与 R2 分歧**：N3（CoRL scope fit）REBUT，建议降级为 warning；W5（competitor positioning）部分 REBUT，仅 Häon et al. 需补充
- **我独有的 critical issues**（R2 未覆盖）：random-subset ablation 结果与核心叙事矛盾、counterfactual ordering 暗示 token-level 而非 semantic sensitivity、N=10 统计功效不足以支撑 negative conclusion

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1"
}
```

</details>

---


## Round 17

## Round 17

24 recorded events


### User

_source line 311 · 2026-05-19T05:53:20.986555+00:00_

[Round 2 审稿请求]:
## Round 10 修订评估（继续审稿）

你是 Reviewer 1，负责 **方法严谨性 + 实验设计**。这是继续审稿模式——上轮你给出 5/10 (borderline reject)，核心问题是 random-subset ablation 矛盾、"Causal" overclaim、counterfactual ordering anomaly、N=10 统计功效不足。

论文已更新。请读取 `projects/vla-ssd/docs/paper/` 下所有 .tex 文件，逐条验证以下 open issues 是否已充分修复。

## Venue 信息（同上轮）
CoRL 2026 | Deadline 2026-05-29 | 8 页正文 | double-blind | Limitations section required

## Open Issues 清单（标 [RESOLVED] 或 [STILL_OPEN] + 理由）

### Critical
**R9-N1** 单模型(OpenVLA-7B)单基准(LIBERO)范围严重限制 generalizability
- 上轮建议：至少在一个额外 VLA 架构上验证 C2

**R9-N2** 完全缺失 closed-loop / task-performance 验证
- 上轮建议：基于 routing analysis 做 layer pruning + closed-loop success rate

### Warning（你上轮提出的）
**R9-N3** Discussion 使用 'Causal' 标签 → 应改为 'interventional'
**R9-N4** Ablation R² 与 routing 叙事张力，'structured noise' post-hoc
- 上轮建议：提供 R² vs d 分离的独立验证或更清晰讨论
**R9-N5** Counterfactual ordering (paraphrased > shuffled) 与 semantic distance 不一致
- 上轮建议：修正措辞 + 报告 token overlap rate
**R9-N6** N=10 统计功效不足 → "not geometry" negative conclusion
- 上轮建议：引入 LIBERO-Spatial significant result + 修正措辞
**R9-W4** Cohen's d 独立性假设违反
- 上轮建议：报告 trajectory-level d
**R9-W5** Llama-2 base 的 in-distribution text bias 替代解释
- 上轮建议：Discussion 提及替代解释
**R9-W6** Specificity control 效果有限 (d ratio 1.15×)
**R9-W7** N=63,228 的有效独立单元数未说明

### Info
**R9-I1** 缺 Octo 引用
**R9-I3** Table 1 caption 不清 + nostalgebraist2020 accessed date

## 要求
1. 逐条标注 [RESOLVED] 或 [STILL_OPEN]
2. 检查修改是否引入新问题
3. 给出更新后的评分（是否有变化）
4. 格式：Strengths / Weaknesses / Questions / Overall

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 312 · 2026-05-19T05:53:28.349316+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 313 · 2026-05-19T05:53:28.814104+00:00_

1	Vision-language-action models (VLAs) fine-tune large language models (LLMs) on robot demonstrations, but what fine-tuning changes at the representational level remains unclear.
2	We present a systematic framework for token-level analysis of VLAs, applying cross-instruction probes, attention analysis, Representational Similarity Analysis (RSA), and functional probes across all 32 LLM layers of OpenVLA-7B on LIBERO, with factorial trained/pretrained/untrained controls.
3	Three findings emerge.
4	First, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth, while VLA training shifts this to entry-layer routing (L0--L1) with exit-layer re-engagement (L31).
5	Seven complementary analyses, including dose-response ablation (8 conditions, monotonic $d = 0.48 \to 0.64$) and counterfactual instruction analysis (4 perturbation types, $d = 0.63$--$0.97$), support instruction-conditioned action generation through distributed L1 routing, with routing dependence $2.5\times$ stronger for instruction-discriminative tasks ($p = 0.033$).
6	Second, vision encoder representations show a metric-dependent middle-layer peak (RSA/probes corroborate; CKA diverges), with training effects concentrated at the readout token ($R^2$ $+0.069$, attention $+46$pp) rather than visual geometry.
7	Architecture-expected token specialization (instruction-blind image tokens, perfect readout classification from L1) is empirically verified as a framework sanity check.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 464
}
```

</details>

---


### Tool call

_source line 314 · 2026-05-19T05:53:28.828434+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 315 · 2026-05-19T05:53:29.258377+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	What does fine-tuning change inside a Vision-Language-Action model (VLA)?
5	VLAs fine-tune large language models on robot demonstrations to produce actions from visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla}, but the decoder-only causal mask prevents image tokens from attending to instructions.
6	Instruction information must reach action-generating positions through learned attention routing, yet how fine-tuning reshapes this routing remains uncharacterized.
7	
8	Recent behavioral studies reveal that VLAs rely disproportionately on visual input~\cite{grant2026}, with language instructions largely ignored by the action pathway~\cite{haon2025}.
9	These findings suggest internal specialization but do not explain \emph{how} instruction information reaches the action-generating readout token, \emph{what} routing strategy fine-tuning learns compared to language pretraining alone, or \emph{whether} training creates new representational structure or reconfigures inherited geometry.
10	Existing analyses have not combined systematic per-layer probing with factorial trained/pretrained/untrained controls, leaving the representational mechanisms of VLA fine-tuning opaque.
11	
12	We address this gap by decomposing OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a VLA chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2}, an MLP projector, and Llama-2 7B~\cite{touvron2023_llama2}.
13	We extract representations from each of 32 LLM layers at both image-token and readout-token positions, and from external baselines (DINOv2~\cite{oquab2024_dinov2}, CLIP~\cite{radford2021_clip}).
14	We compare three LLM conditions (VLA-trained, pretrained Llama-2 base, and randomly initialized) crossed with instruction presence, and apply four complementary analyses: cross-instruction probes for token-level specialization, L1 attention pattern analysis for routing mechanisms, R
…[truncated 2054 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 429
}
```

</details>

---


### Tool call

_source line 316 · 2026-05-19T05:53:29.310114+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 317 · 2026-05-19T05:53:29.763895+00:00_

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
14	Meng et al.~\cite{meng2022_rome} developed causal tracing for factual associations, Belrose et al.~\cite{belrose2023_tunedlens} introduced the tuned lens for per-layer prediction, and feature-level methods have scaled to dictionary learning over millions of features~\cite{bills2023language,templeton2024scaling}.
15	Attention probing has shown that individual heads encode syntactic relations~\cite{clark2019}, capture depth-dependent patterns~\cite{vig2019}, and that a small subset accounts for most performance~\cite{voita2019}.
16	Our Layer-1 attention head analysis ext
…[truncated 3039 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 318 · 2026-05-19T05:53:29.764361+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 319 · 2026-05-19T05:53:30.220193+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We investigate how action-relevant structure is distributed across a VLA by combining four complementary analyses: cross-instruction probes, attention pattern analysis, RSA, and functional probes.
5	
6	%------------------------------------------------------------------
7	\subsection{Model and Data}
8	\label{sec:model_data}
9	
10	We study OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\to$ 4{,}096-D), and Llama-2 7B~\cite{touvron2023_llama2} (6.74B parameters) that autoregressively decodes 7-D actions.
11	We use the base checkpoint pretrained on Open X-Embodiment~\cite{padalkar2023_oxe} and evaluate on LIBERO-Goal~\cite{liu2023_libero} (10 tasks, 50 demonstrations each).
12	We compare three LLM conditions: (1)~VLA-trained (released checkpoint), (2)~Llama-2 base (pretrained backbone, no VLA fine-tuning), and (3)~untrained (6.74B parameters reinitialized via \texttt{from\_config()}).
13	All three share the same frozen vision encoder and projector.
14	
15	%------------------------------------------------------------------
16	\subsection{Representation Extraction}
17	\label{sec:repr_extraction}
18	
19	We extract representations from six sources spanning the VLA pipeline:
20	(a)~\textbf{DinoSigLIP+Projector}, the projector output (4{,}096-D), immediately before LLM processing;
21	(b)~\textbf{LLM image\_mean}, the mean image-token activation at each of 32 layers;
22	(c)~\textbf{LLM readout}, the hidden state at the final pre-action token position at each layer (located after both image and instruction tokens in the causal sequence, it can attend to all preceding context and is thus the natural site for multimodal integration before action prediction);
23	(d)~\textbf{DINOv2 ViT-L/14}~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}), a self-supervised baseline;
24
…[truncated 3943 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 320 · 2026-05-19T05:53:30.220635+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 321 · 2026-05-19T05:53:31.130065+00:00_

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
12	This yields $N = 63{,}228$ observations (after excluding terminal frames without next-action labels; $63{,}728$ total); RSA uses task-level blocking ($N_\text{eff} = 10$) and probes use demo-level train/test splits.
13	All patterns reproduce with a linear probe (Appendix~\ref{sec:linear_probe}).
14	
15	%------------------------------------------------------------------
16	\subsection{Framework Validation: Token-Level Specialization}
17	\label{sec:token_specialization}
18	
19	As a sanity check on the experimental framework, we train cross-instruction probes (\S\ref{sec:cross_instruction_probes}): given the same visual frame with each of 10 task instructions, we classify which instruction was present from per-layer activations.
20	
21	\paragraph{Image tokens are instruction-blind (expected).}
22	As predicted by the causal mask and frozen encoder, i
…[truncated 10269 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool call

_source line 322 · 2026-05-19T05:53:31.130797+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-19T05:53:31.647963+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Synthesis.}
5	VLA fine-tuning primarily reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\Delta \leq 1.7\%$).
6	This explains the visual dominance of Grant et al.~\cite{grant2026}: DINOv2 has the highest geometric alignment ($\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\ $0.634$).
7	Seven complementary analyses support instruction-conditioned action generation through distributed L1 routing, where instruction-attention fraction predicts per-head contribution magnitude.
8	\emph{Interventional}: (1)~dose-response curve across 8 conditions ($d = 0.48 \to 0.64$; Figure~\ref{fig:dose_response}); (2)~counterfactual instruction analysis across 4 perturbation types ($d = 0.63$--$0.97$; Table~\ref{tab:counterfactual}).
9	\emph{Supporting}: (3)~three-condition attention gradient ($0 \to 9 \to 24$ instruction-dominant heads); (4)~$R^2$ ablation gradient confined to L1 ($+0.059$ at L1, $\approx 0$ at L13); (5)~trajectory divergence under L1 ablation ($d = 0.65$, $72.3\%$ token divergence).
10	\emph{Constraining}: (6)~per-head bootstrap CIs (individual instruction $d = 0.027$ vs.\ control $d = 0.051$; collective instruction $d = 0.65$ vs.\ control $d = 0.41$; $p = 0.0018$); and~(7)~specificity control ($d$ ratio $1.08\times$; Table~\ref{tab:specificity_control}).
11	
12	\paragraph{Mechanistic interpretation.}
13	Matched-size ablation (instruction $d = 0.65$, random $0.60$, image-dominant $0.58$; Table~\ref{tab:specificity_control}) and the dose-response curve (steep rise through 12 heads, plateau beyond 20) indicate distributed, attention-graded routing; counterfactual ordering follows token novelty ($\rho = 1.0$; \S\ref{sec:learned_routing}).
14	That ablation raises $R^2$ yet alters trajectories ($d = 0.65$) without increasing ground-truth error ($\Delta\text{MSE} \appr
…[truncated 2191 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 517
}
```

</details>

---


### Tool call

_source line 324 · 2026-05-19T05:53:31.648482+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 325 · 2026-05-19T05:53:32.150550+00:00_

1	\paragraph{Conclusion.}
2	We present a token-level analysis framework for VLAs and find that fine-tuning reorganizes instruction routing to entry-exit layers; seven complementary analyses identify L1 as the primary hub.
3	Code and representations will be released upon acceptance.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 326 · 2026-05-19T05:53:32.201356+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 327 · 2026-05-19T05:53:32.654569+00:00_

1	\paragraph{Use of Generative AI.}
2	Generative AI tools (Claude, GPT-4) assisted with code implementation and manuscript editing; all scientific content was produced by the authors.
3	
4	\appendix
5	
6	\section{Supplementary Material}
7	\label{sec:appendix}
8	
9	\subsection{CKA Analysis Method}
10	\label{sec:cka_appendix}
11	
12	We employ Centered Kernel Alignment (CKA)~\cite{kornblith2019} alongside RSA as a complementary perspective.
13	While RSA captures local geometric alignment via rank-order preservation, CKA measures global representational similarity through kernel-based comparisons.
14	
15	We compute both \emph{linear CKA}, which uses a linear kernel and is sensitive to second-order statistics, and \emph{RDM kernel CKA}, which operates on the same distance matrices as RSA but aggregates them differently.
16	Using both variants tests whether conclusions about representation structure are robust to the choice of similarity metric.
17	
18	Linear CKA between high-dimensional representations (4{,}096-D for LLM layers) and the 7-D action space is subject to a known dimension mismatch: the linear kernel in the low-dimensional space may not capture the same structure as in the high-dimensional space.
19	RDM kernel CKA avoids this issue by operating on distance matrices of equal size regardless of the original feature dimensionality.
20	
21	\subsection{Metric Sensitivity: RSA versus CKA}
22	\label{sec:metric_sensitivity_appendix}
23	
24	Linear CKA~\cite{kornblith2019} reverses the RSA ordering: untrained LLM ($\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially inverting the self-supervised advantage (Figure~\ref{fig:metric_comparison}).
25	RDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $\approx$ Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).
26	This divergence reflects the known sensitivity of representation similarity metrics to different geometric properties.
…[truncated 44569 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 328 · 2026-05-19T05:53:32.655074+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 329 · 2026-05-19T05:53:32.908101+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 253
}
```

</details>

---


### Tool call

_source line 330 · 2026-05-19T05:53:32.958646+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 331 · 2026-05-19T05:53:33.009570+00:00_

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
…[truncated 17235 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 332 · 2026-05-19T05:56:12.333068+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 — Round 10 修订评估\n\n**论文**: \"Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\"\n**上轮评分**: 5/10 (marginally below)\n**Confidence**: 4/5\n\n---\n\n## Open Issues 逐条核查\n\n### Critical\n\n**R9-N1** 单模型(OpenVLA-7B)单基准(LIBERO) → **[STILL_OPEN]**\n- 未新增任何额外 VLA 架构的实验。Discussion §5 的预测列表新增了 Octo 引用 (ghosh2024_octo)，但三条预测仍均为未验证推测。\n- 理解这属于 scope 限制，不太可能在修订周期内解决。降级为 **residual weakness** 而非 blocker。\n\n**R9-N2** 完全缺失 closed-loop 验证 → **[STILL_OPEN]**\n- Discussion §5 末段: \"All analyses are open-loop; combining routing with activation steering and closed-loop evaluation are natural extensions.\" 措辞未变。\n- 同上，属 scope 限制。但论文保留了 pruning target (56% 参数) 的 claim（Discussion §5 第 3 段）却未做任何验证，这依然是 overclaim。降级为 **residual weakness**。\n\n---\n\n### Warning\n\n**R9-N3** \"Causal\" 标签 → **[RESOLVED]**\n- Discussion §5 第 1 段: 原 \"Causal:\" 已改为 **\"Interventional:\"**。全文搜索确认无残留的 \"causal\" 用于描述本文证据。\n- §4.3 段标题从 \"Ablation confirms routing function\" 改为 **\"Open-loop functional sensitivity\"**，claim 力度恰当降低。\n\n**R9-N4** Ablation R² 与 routing 叙事张力 → **[PARTIALLY RESOLVED]**\n- **新增内容**:\n  - Appendix §A.8 新增 \"Ground-truth action error\" 段: ablation 后 MSE 不变（原 0.498 → instruction-head ablation 0.497, Δ=-0.001, Wilcoxon p=0.52 n.s.; bottom-24 heads 0.506, Δ=+0.008）。这是关键新数据。\n  - Discussion §5 第 2 段引入 **information-computation dissociation** 框架 (cite Hewitt & Liang 2019): \"routing controls direction rather than precision.\" 理论锚点清晰。\n- **改善了什么**: R² ↑ + trajectory divergence + MSE 不变 的三角关系现在可以自洽解释——instruction heads 控制\"做什么\"(direction)，不控制\"做得多准\"(precision)。ablation 改变了行动方向但未降低精度。\n- **仍然存在的张力**: random-subset ablation (R² +0.077) > instruction-dominant ablation (R² +0.042) 仍未充分解释。主文 §4.3 仍保留 \"structured noise for the probe\" 措辞但无独立验证。如果 direction-selection 是 routing heads 的功能，那么移除 routing heads 应该产生**更大的**方向偏移（进而更大的 R² 变化），但实际上 random 的效果更大。MSE 数据虽然帮助了主叙事，但未直接回答这个 specificity 问题。\n- 降级为 minor weakness（从 critical 降至 warning）。\n\n**R9-N5** Counterfactual ordering anomaly → **[RESOLVED]**\n- §4.3 counterfactual 段重写: \"Token novelty (1−Jaccard) perfectly predicts the divergence ordering (ρ=1.0; Table~6): paraphrased (Jaccard 0.533) exceeds shuffled (Jaccard 1.0), consistent with **token identity as the primary driver**, though the shuffled d=0.625 with identical tokens reveals additional positional sensitivity.\"\n- Table 6 新增 Jaccard 列，定量数据充分。\n- \"semantic distance\" 措辞已完全移除，替换为 \"token novelty\"。\n- 额外正面: 承认了 shuffled d=0.625 揭示 positional sensitivity，比上轮更细致。\n\n**R9-N6** N=10 统计功效 → **[PARTIALLY RESOLVED]**\n- §4.4 第 3 段: \"Best-vs-best RSA gain is non-significant on LIBERO-Goal (Δρ=0.017, 3%, **N=10 tasks**; Appendix Table), though LIBERO-Spatial yields a significant geometric gain (Δ=+0.023, p<0.001; Appendix).\"\n  - N=10 现在显式标注 ✓\n  - LIBERO-Spatial 显著结果引入主文 ✓\n  - 段标题从 \"Training enhances decodability, not geometry\" 改为 **\"Training primarily enhances readout decodability\"** — \"primarily\" 比 \"not\" 更审慎 ✓\n- **仍缺**: 主文中没有明确的 power limitation 声明（仅 Appendix §A.10 隐含提及）。\"non-significant on LIBERO-Goal\" 仍可能被误读为 \"evidence of no effect\"。一句话如 \"the non-significant result on LIBERO-Goal may reflect limited statistical power (N=10 tasks)\" 在主文中会更完善。\n\n**R9-W4** Cohen's d 独立性假设 → **[RESOLVED]**\n- Appendix §A.8 新增 \"Trajectory-level aggregation\" 段: trajectory d=2.943 (CI [2.469, 3.707])，约为 token-level 的 4×。\n- Discussion §5 第 2 段: \"Trajectory-level aggregation yields d=2.1–3.8 (~4× token-level; Appendix).\"\n- 报告了 trajectory-level d 和 CI，token-level d 实际上是保守估计。\n\n**R9-W5** Llama-2 base in-distribution text bias → **[RESOLVED]**\n- Discussion §5 Limitations: \"Llama-2's 9/32 pretrained instruction heads may partly reflect text bias; the +15-head delta isolates fine-tuning effects.\"\n- 简洁有效: 承认替代解释，用 delta (+15 heads from fine-tuning) 作为 deconfounding argument。\n\n**R9-W6** Specificity control 效果有限 → **[PARTIALLY RESOLVED]**\n- Appendix §A.17 扩展为 **4 条件 matched-size ablation** (instruction-dominant d=0.650, random d=0.601±0.021, image-dominant d=0.580, bottom-24 d=0.565)。比上轮仅有 top/bottom 两条件改善明显。\n- Discussion §5 第 1 段: d ratio 更新为 1.08× (从 1.15×)，并新增 \"distributed, attention-graded routing rather than a dedicated subset\"。\n- 这实际上是更诚实的 framing: 不声称 sharp specificity，而是 graded routing。\n- 但 gap 确实小 (d=0.650 vs random 0.601, 仅 8%)，论文的讨论已经到位。\n\n**R9-W7** N=63,228 有效独立单元数 → **[PARTIALLY RESOLVED]**\n- §4.1: \"RSA uses task-level blocking (N_eff=10) and probes use demo-level train/test splits.\"\n- RSA 的 N_eff 现在显式标注 ✓\n- Probe 的有效独立单元数（demo-level aggregation 后约 N=500）仍未在主文中显式给出。\n\n---\n\n### Info\n\n**R9-I1** 缺 Octo 引用 → **[RESOLVED]**\n- references.bib 新增 ghosh2024_octo。Discussion §5 predictions 段引用。\n\n**R9-I3** Table 1 caption + nostalgebraist accessed date → **[PARTIALLY RESOLVED]**\n- Table 1 caption 重写，现在自包含且清晰: \"Image_mean remains at chance (10%) in all conditions; trained readout reaches 100% at L1 and holds; untrained readout decays from L1 to L31.\"\n- nostalgebraist2020 的 note 仍有 \"Accessed: 2026-05-19\"（从 05-18 更新为 05-19）。极小问题。\n\n---\n\n## 修订引入的新变化（正面）\n\n1. **Abstract/Introduction 重构**: C1 (sanity check) 从 Abstract 的第一个 finding 降级为末尾一句话；Introduction 中 C2 (routing) 提升为 \"First\"，C1 降为 \"\\S4.2 framework sanity check\"。Contribution 列表重排: (i) routing evidence, (ii) vision representation, (iii) framework。**大幅改善了叙事权重**，呼应了上轮 R2-W1。\n\n2. **Per-token attention normalization** (Appendix §A.15 新增段): 38.2× text-to-image per-token ratio 在 trained instruction-dominant heads，vs 1.5× in untrained (25.5× increase from training)。定量化了 token-count imbalance 后的真实注意力偏好。\n\n3. **Matched-size ablation 扩展** (Appendix §A.17): 从 2 条件扩展到 4 条件 (instruction, random, image-dominant, bottom-24)，plus MSE baseline。\n\n4. **Task complexity leave-one-out** (Appendix §A.19 新增段): \"All leave-one-out p-values remain ≤0.083, with no single task removal causing a qualitative reversal.\"\n\n5. **Conclusion 精简**: 从独立 section 改为 paragraph，节省页面预算。\n\n6. **无新问题引入**: 修订在改善问题的同时未创造新的方法论问题。\n\n---\n\n## 更新后的维度打分\n\n| 维度 | 上轮 | 本轮 | 变化原因 |\n|------|------|------|----------|\n| Originality | 3/5 | 3/5 | 无变化 |\n| Quality (Soundness) | 2/5 | 3/5 | \"Interventional\" 替代 \"Causal\"；MSE ground-truth analysis；Jaccard counterfactual analysis；trajectory-level d；matched-size ablation 扩展 |\n| Clarity | 4/5 | 4.5/5 | C1 权重修正；Table 1 caption 改善；counterfactual framing 更精确 |\n| Significance | 2/5 | 2.5/5 | 仍为单模型 + 无闭环；但 information-computation dissociation framing 和 task-dependent routing 提升了理论价值 |\n| Relevance | 3/5 | 3/5 | 无变化 |\n| Limitations | 4/5 | 4.5/5 | Llama-2 text bias 承认；N_eff=10 标注；open-loop 明确 |\n\n---\n\n## Strengths（更新）\n\n1. **响应性修订**: 几乎所有可在修订周期内解决的问题都得到了实质回应，非 superficial 修改。\n2. **信息-计算分离框架** (Hewitt & Liang 2019 anchoring): 为 R² ↑ + trajectory divergence + MSE 不变的三角关系提供了principled 解释，比上轮的 \"structured noise\" 大幅改善。\n3. **Counterfactual 重分析**: Jaccard + token novelty + ρ=1.0 是一流的修改——不仅修正了 semantic distance 的 overclaim，还将 anomaly 转化为正面发现（token identity > positional sensitivity 的层级结构）。\n4. **Trajectory-level d**: 证明 token-level d 是保守估计，彻底消除了 independence 假设的担忧方向。\n5. 上轮所有 Strengths 保持不变。\n\n## Weaknesses（更新）\n\n1. **[residual, scope]** 单模型单 benchmark 范围——理解为 scope 限制，但仍是对 generalizability claim 的真实约束。\n2. **[residual, scope]** 无闭环验证——pruning target (56%) 和 deployment monitoring claim 仍缺乏支撑。\n3. **[minor]** Random-subset ablation 的 R² 差异 (random +0.077 > dominant +0.042) 在 information-computation dissociation 框架下仍需更好的解释。当前 \"structured noise\" 措辞可以改为更精确的表述。\n4. **[minor]** N=10 power limitation 应在主文 §4.4 中显式提及，而非仅在 Appendix 中隐含。\n\n## Questions（更新）\n\nQ1: 基于新增的 MSE 分析——如果 instruction-head ablation 不改变 ground-truth MSE，但改变了 72.3% 的 action tokens 和 trajectory direction (d=0.65)，这是否意味着多数 action token 的变化发生在对 MSE 影响不大的 low-precision dimensions（如 gripper 的 binary shift）？Table A.5 的 per-dimension 数据似乎支持这一点（gripper shift 0.291 >> 其他维度），但主文未明确连接。\n\nQ2: Matched-size ablation 中 instruction-dominant (d=0.650) vs random (d=0.601) 的差异仅 8%。在什么 effect size threshold 下你们会认为 specificity claim 不成立？当前 8% 的解释是 \"graded routing\"，但如果 random 和 dominant 的效果几乎相同，alternative 解释是 L1 中**所有** heads 都有类似功能贡献，instruction-attention fraction 只是一个弱 predictor。\n\n---\n\n## Overall Assessment\n\n**更新评分: 6/10 — Marginally above acceptance threshold**\n\n修订显著改善了方法严谨性: \"Causal\" overclaim 已修正；counterfactual ordering anomaly 已通过 Jaccard analysis 彻底解决并转化为正面发现；trajectory-level d 消除了 independence 担忧；MSE ground-truth 分析为 ablation 解读提供了新的理论锚点；N=10 在主文中显式标注。\n\n上调 1 分的主要依据: (1) 多个 methodological 问题被实质性修复而非回避；(2) information-computation dissociation framing 为整个 ablation 叙事提供了更 principled 的理论基础；(3) counterfactual 的 token novelty 分析是一个 example of turning a weakness into a finding。\n\n不上调至 7 的原因: (1) 单模型 + 无闭环仍是核心 scope 限制；(2) specificity control 的 modest gap 和 random-subset R² 反转仍未完全消解；(3) 对 CoRL 社区的 actionable value 仍主要停留在 analytical insights 层面。\n\n**评分上调条件**: 如果在 camera-ready 中加入至少一个 task 的 closed-loop ablation 结果（哪怕是 preliminary），或在一个额外 VLA 上验证 attention profile prediction，可考虑 7/10。\n",
  "reviewer_id": "1",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 — Round 10 修订评估\n\n**论文**: \"Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\"\n**上轮评分**: 5/10 (marginally below)\n**Confidence**: 4/5\n\n---\n\n## Open Issues 逐条核查\n\n### Critical\n\n**R9-N1** 单模型(OpenVLA-7B)单基准(LIBERO) → **[STILL_OPEN]**\n- 未新增任何额外 VLA 架构的实验。Discussion §5 的预测列表新增了 Octo 引用 (ghosh2024_octo)，但三条预测仍均为未验证推测。\n- 理解这属于 scope 限制，不太可能在修订周期内解决。降级为 **residual weakness** 而非 blocker。\n\n**R9-N2** 完全缺失 closed-loop 验证 → **[STILL_OPEN]**\n- Discussion §5 末段: \"All analyses are open-loop; combining routing with activation steering and closed-loop evaluation are natural extensions.\" 措辞未变。\n- 同上，属 scope 限制。但论文保留了 pruning target (56% 参数) 的 claim（Discussion §5 第 3 段）却未做任何验证，这依然是 overclaim。降级为 **residual weakness**。\n\n---\n\n### Warning\n\n**R9-N3** \"Causal\" 标签 → **[RESOLVED]**\n- Discussion §5 第 1 段: 原 \"Causal:\" 已改为 **\"Interventional:\"**。全文搜索确认无残留的 \"causal\" 用于描述本文证据。\n- §4.3 段标题从 \"Ablation confirms routing function\" 改为 **\"Open-loop functional sensitivity\"**，claim 力度恰当降低。\n\n**R9-N4** Ablation R² 与 routing 叙事张力 → **[PARTIALLY RESOLVED]**\n- **新增内容**:\n  - Appendix §A.8 新增 \"Ground-truth action error\" 段: ablation 后 MSE 不变（原 0.498 → instruction-head ablation 0.497, Δ=-0.001, Wilcoxon p=0.52 n.s.; bottom-24 heads 0.506, Δ=+0.008）。这是关键新数据。\n  - Discussion §5 第 2 段引入 **information-computation dissociation** 框架 (cite Hewitt & Liang 2019): \"routing controls direction rather than precision.\" 理论锚点清晰。\n- **改善了什么**: R² ↑ + trajectory divergence + MSE 不变 的三角关系现在可以自洽解释——instruction heads 控制\"做什么\"(direction)，不控制\"做得多准\"(precision)。ablation 改变了行动方向但未降低精度。\n- **仍然存在的张力**: random-subset ablation (R² +0.077) > instruction-dominant ablation (R² +0.042) 仍未充分解释。主文 §4.3 仍保留 \"structured noise for the probe\" 措辞但无独立验证。如果 direction-selection 是 routing heads 的功能，那么移除 routing heads 应该产生**更大的**方向偏移（进而更大的 R² 变化），但实际上 random 的效果更大。MSE 数据虽然帮助了主叙事，但未直接回答这个 specificity 问题。\n- 降级为 minor weakness（从 critical 降至 warning）。\n\n**R9-N5** Counterfactual ordering anomaly → **[RESOLVED]**\n- §4.3 counterfactual 段重写: \"Token novelty (1−Jaccard) perfectly predicts the divergence ordering (ρ=1.0; Table~6): paraphrased (Jaccard 0.533) exceeds shuffled (Jaccard 1.0), consistent with **token identity as the primary driver**, though the shuffled d=0.625 with identical tokens reveals additional positional sensitivity.\"\n- Table 6 新增 Jaccard 列，定量数据充分。\n- \"semantic distance\" 措辞已完全移除，替换为 \"token novelty\"。\n- 额外正面: 承认了 shuffled d=0.625 揭示 positional sensitivity，比上轮更细致。\n\n**R9-N6** N=10 统计功效 → **[PARTIALLY RESOLVED]**\n- §4.4 第 3 段: \"Best-vs-best RSA gain is non-significant on LIBERO-Goal (Δρ=0.017, 3%, **N=10 tasks**; Appendix Table), though LIBERO-Spatial yields a significant geometric gain (Δ=+0.023, p<0.001; Appendix).\"\n  - N=10 现在显式标注 ✓\n  - LIBERO-Spatial 显著结果引入主文 ✓\n  - 段标题从 \"Training enhances decodability, not geometry\" 改为 **\"Training primarily enhances readout decodability\"** — \"primarily\" 比 \"not\" 更审慎 ✓\n- **仍缺**: 主文中没有明确的 power limitation 声明（仅 Appendix §A.10 隐含提及）。\"non-significant on LIBERO-Goal\" 仍可能被误读为 \"evidence of no effect\"。一句话如 \"the non-significant result on LIBERO-Goal may reflect limited statistical power (N=10 tasks)\" 在主文中会更完善。\n\n**R9-W4** Cohen's d 独立性假设 → **[RESOLVED]**\n- Appendix §A.8 新增 \"Trajectory-level aggregation\" 段: trajectory d=2.943 (CI [2.469, 3.707])，约为 token-level 的 4×。\n- Discussion §5 第 2 段: \"Trajectory-level aggregation yields d=2.1–3.8 (~4× token-level; Appendix).\"\n- 报告了 trajectory-level d 和 CI，token-level d 实际上是保守估计。\n\n**R9-W5** Llama-2 base in-distribution text bias → **[RESOLVED]**\n- Discussion §5 Limitations: \"Llama-2's 9/32 pretrained instruction heads may partly reflect text bias; the +15-head delta isolates fine-tuning effects.\"\n- 简洁有效: 承认替代解释，用 delta (+15 heads from fine-tuning) 作为 deconfounding argument。\n\n**R9-W6** Specificity control 效果有限 → **[PARTIALLY RESOLVED]**\n- Appendix §A.17 扩展为 **4 条件 matched-size ablation** (instruction-dominant d=0.650, random d=0.601±0.021, image-dominant d=0.580, bottom-24 d=0.565)。比上轮仅有 top/bottom 两条件改善明显。\n- Discussion §5 第 1 段: d ratio 更新为 1.08× (从 1.15×)，并新增 \"distributed, attention-graded routing rather than a dedicated subset\"。\n- 这实际上是更诚实的 framing: 不声称 sharp specificity，而是 graded routing。\n- 但 gap 确实小 (d=0.650 vs random 0.601, 仅 8%)，论文的讨论已经到位。\n\n**R9-W7** N=63,228 有效独立单元数 → **[PARTIALLY RESOLVED]**\n- §4.1: \"RSA uses task-level blocking (N_eff=10) and probes use demo-level train/test splits.\"\n- RSA 的 N_eff 现在显式标注 ✓\n- Probe 的有效独立单元数（demo-level aggregation 后约 N=500）仍未在主文中显式给出。\n\n---\n\n### Info\n\n**R9-I1** 缺 Octo 引用 → **[RESOLVED]**\n- references.bib 新增 ghosh2024_octo。Discussion §5 predictions 段引用。\n\n**R9-I3** Table 1 caption + nostalgebraist accessed date → **[PARTIALLY RESOLVED]**\n- Table 1 caption 重写，现在自包含且清晰: \"Image_mean remains at chance (10%) in all conditions; trained readout reaches 100% at L1 and holds; untrained readout decays from L1 to L31.\"\n- nostalgebraist2020 的 note 仍有 \"Accessed: 2026-05-19\"（从 05-18 更新为 05-19）。极小问题。\n\n---\n\n## 修订引入的新变化（正面）\n\n1. **Abstract/Introduction 重构**: C1 (sanity check) 从 Abstract 的第一个 finding 降级为末尾一句话；Introduction 中 C2 (routing) 提升为 \"First\"，C1 降为 \"\\S4.2 framework sanity check\"。Contribution 列表重排: (i) routing evidence, (ii) vision representation, (iii) framework。**大幅改善了叙事权重**，呼应了上轮 R2-W1。\n\n2. **Per-token attention normalization** (Appendix §A.15 新增段): 38.2× text-to-image per-token ratio 在 trained instruction-dominant heads，vs 1.5× in untrained (25.5× increase from training)。定量化了 token-count imbalance 后的真实注意力偏好。\n\n3. **Matched-size ablation 扩展** (Appendix §A.17): 从 2 条件扩展到 4 条件 (instruction, random, image-dominant, bottom-24)，plus MSE baseline。\n\n4. **Task complexity leave-one-out** (Appendix §A.19 新增段): \"All leave-one-out p-values remain ≤0.083, with no single task removal causing a qualitative reversal.\"\n\n5. **Conclusion 精简**: 从独立 section 改为 paragraph，节省页面预算。\n\n6. **无新问题引入**: 修订在改善问题的同时未创造新的方法论问题。\n\n---\n\n## 更新后的维度打分\n\n| 维度 | 上轮 | 本轮 | 变化原因 |\n|------|------|------|----------|\n| Originality | 3/5 | 3/5 | 无变化 |\n| Quality (Soundness) | 2/5 | 3/5 | \"Interventional\" 替代 \"Causal\"；MSE ground-truth analysis；Jaccard counterfactual analysis；trajectory-level d；matched-size ablation 扩展 |\n| Clarity | 4/5 | 4.5/5 | C1 权重修正；Table 1 caption 改善；counterfactual framing 更精确 |\n| Significance | 2/5 | 2.5/5 | 仍为单模型 + 无闭环；但 information-computation dissociation framing 和 task-dependent routing 提升了理论价值 |\n| Relevance | 3/5 | 3/5 | 无变化 |\n| Limitations | 4/5 | 4.5/5 | Llama-2 text bias 承认；N_eff=10 标注；open-loop 明确 |\n\n---\n\n## Strengths（更新）\n\n1. **响应性修订**: 几乎所有可在修订周期内解决的问题都得到了实质回应，非 superficial 修改。\n2. **信息-计算分离框架** (Hewitt & Liang 2019 anchoring): 为 R² ↑ + trajectory divergence + MSE 不变的三角关系提供了principled 解释，比上轮的 \"structured noise\" 大幅改善。\n3. **Counterfactual 重分析**: Jaccard + token novelty + ρ=1.0 是一流的修改——不仅修正了 semantic distance 的 overclaim，还将 anomaly 转化为正面发现（token identity > positional sensitivity 的层级结构）。\n4. **Trajectory-level d**: 证明 token-level d 是保守估计，彻底消除了 independence 假设的担忧方向。\n5. 上轮所有 Strengths 保持不变。\n\n## Weaknesses（更新）\n\n1. **[residual, scope]** 单模型单 benchmark 范围——理解为 scope 限制，但仍是对 generalizability claim 的真实约束。\n2. **[residual, scope]** 无闭环验证——pruning target (56%) 和 deployment monitoring claim 仍缺乏支撑。\n3. **[minor]** Random-subset ablation 的 R² 差异 (random +0.077 > dominant +0.042) 在 information-computation dissociation 框架下仍需更好的解释。当前 \"structured noise\" 措辞可以改为更精确的表述。\n4. **[minor]** N=10 power limitation 应在主文 §4.4 中显式提及，而非仅在 Appendix 中隐含。\n\n## Questions（更新）\n\nQ1: 基于新增的 MSE 分析——如果 instruction-head ablation 不改变 ground-truth MSE，但改变了 72.3% 的 action tokens 和 trajectory direction (d=0.65)，这是否意味着多数 action token 的变化发生在对 MSE 影响不大的 low-precision dimensions（如 gripper 的 binary shift）？Table A.5 的 per-dimension 数据似乎支持这一点（gripper shift 0.291 >> 其他维度），但主文未明确连接。\n\nQ2: Matched-size ablation 中 instruction-dominant (d=0.650) vs random (d=0.601) 的差异仅 8%。在什么 effect size threshold 下你们会认为 specificity claim 不成立？当前 8% 的解释是 \"graded routing\"，但如果 random 和 dominant 的效果几乎相同，alternative 解释是 L1 中**所有** heads 都有类似功能贡献，instruction-attention fraction 只是一个弱 predictor。\n\n---\n\n## Overall Assessment\n\n**更新评分: 6/10 — Marginally above acceptance threshold**\n\n修订显著改善了方法严谨性: \"Causal\" overclaim 已修正；counterfactual ordering anomaly 已通过 Jaccard analysis 彻底解决并转化为正面发现；trajectory-level d 消除了 independence 担忧；MSE ground-truth 分析为 ablation 解读提供了新的理论锚点；N=10 在主文中显式标注。\n\n上调 1 分的主要依据: (1) 多个 methodological 问题被实质性修复而非回避；(2) information-computation dissociation framing 为整个 ablation 叙事提供了更 principled 的理论基础；(3) counterfactual 的 token novelty 分析是一个 example of turning a weakness into a finding。\n\n不上调至 7 的原因: (1) 单模型 + 无闭环仍是核心 scope 限制；(2) specificity control 的 modest gap 和 random-subset R² 反转仍未完全消解；(3) 对 CoRL 社区的 actionable value 仍主要停留在 analytical insights 层面。\n\n**评分上调条件**: 如果在 camera-ready 中加入至少一个 task 的 closed-loop ablation 结果（哪怕是 preliminary），或在一个额外 VLA 上验证 attention profile prediction，可考虑 7/10。\n",
    "reviewer_id": "1",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 333 · 2026-05-19T05:56:18.265979+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5932
}
```

</details>

---


### Assistant

_source line 334 · 2026-05-19T05:56:25.994673+00:00_

评估报告已提交。

**总结**: 评分从 5/10 上调至 **6/10** (marginally above)。修订实质性地解决了多数方法论问题——"Causal" 改为 "Interventional"、counterfactual 的 Jaccard 分析、trajectory-level d、MSE ground-truth 分析。核心 scope 限制（单模型、无闭环）仍在，但已非修订周期可解决的问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1"
}
```

</details>

---


## Round 18

## Round 18

4 recorded events


### User

_source line 335 · 2026-05-19T06:01:52.760578+00:00_

[Round 2 审稿请求]:
# 交叉分享：Reviewer 2 的 Round 2 修订评估

请逐条回应 Reviewer 2 的评估，标注 [AGREE] 或 [REBUT]。重点关注你们评估有分歧的地方。

## Reviewer 2 Round 2 核心评估（6/10）

### Issue 状态评估
- R9-N1 单模型: STILL_OPEN（同你）
- R9-N2 无闭环: STILL_OPEN（同你）
- R9-W1 CoRL scope: PARTIALLY_RESOLVED（"边界但有连接"）
- R9-W2 C1 占比: RESOLVED
- R9-W3 Vision framing: RESOLVED
- R9-N3 Causal→Interventional: RESOLVED
- R9-N4 Ablation R² 解释: PARTIALLY_RESOLVED（MSE 证据显著降低 severity，但 "为什么移除有用信号反而让 probe 更准" 未完全解释）
- R9-N5 Counterfactual: RESOLVED（"从 problematic claim 转变为 empirically grounded observation"）
- R9-N6 N=10 hedging: RESOLVED
- R9-I1 Octo: RESOLVED
- R9-I2 Häon et al.: PARTIALLY_RESOLVED（"未深入讨论 sparse semantic directions 与 L1 attention routing 的互补/冲突关系"）

### Reviewer 2 的 Questions
Q1: 消融后 MSE 不变但 d=0.65——能否提供 per-task MSE breakdown 确认不是平均效应？
Q2: Specificity control d ratio 仅 1.08×——是否意味着 any 24 heads at L1 都在做类似的事？

### Reviewer 2 识别的新问题
1. Conclusion 被压缩为一段（3行），过于简短
2. Specificity d ratio 1.08× 削弱了 "instruction-dominant heads are special" 叙事

### Reviewer 2 评分理由
- Quality 5→8, Clarity 5→8, 但 Significance 和 Relevance 均维持 5/10
- 阻止更高评分的根本原因：单模型 + 无闭环

请逐条 [AGREE] 或 [REBUT]，特别是：
1. R9-N4 你认为 MSE 证据是否充分解决了 ablation R² paradox？
2. 你是否同意 Conclusion 过于简短是新问题？
3. 对 Specificity d ratio 1.08× 的解读你是否一致？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 336 · 2026-05-19T06:03:01.414350+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 对 Reviewer 2 Round 2 评估的交叉回应\n\n---\n\n## Issue 状态评估——逐条回应\n\n**[AGREE] R9-N1 单模型: STILL_OPEN**\n一致。无分歧。\n\n**[AGREE] R9-N2 无闭环: STILL_OPEN**\n一致。无分歧。\n\n**[AGREE] R9-W1 CoRL scope: PARTIALLY_RESOLVED**\n同意 \"边界但有连接\"。修订后 Discussion §5 对 deployment monitoring (L1 routing probes for instruction-discriminative tasks) 和 activation steering (cite Häon et al.) 的讨论使 robotics 连接更具体，但仍停留在 speculative 层面。\n\n**[AGREE] R9-W2 C1 占比: RESOLVED**\n一致。Abstract/Introduction 的重构有效解决了这个问题。\n\n**[AGREE] R9-W3 Vision framing: RESOLVED**\n一致。\n\n**[AGREE] R9-N3 Causal→Interventional: RESOLVED**\n一致。\n\n**[AGREE] R9-N4 Ablation R² 解释: PARTIALLY_RESOLVED**\n同意 MSE 证据显著降低了 severity，但 paradox 未完全消解。具体评估：\n\nMSE 证据解决了什么：它建立了 R² ↑ + trajectory change + MSE 不变 的三角关系，使 \"information-computation dissociation\" 框架站得住脚。routing heads 控制方向选择（哪个 action）而非精度（action 的准确度），这是一个 principled 且可检验的 claim。\n\nMSE 证据未解决什么：为什么 **random** 24 heads 的 ablation 产生比 instruction-dominant 24 heads **更大**的 R² 增加（+0.077 vs +0.042）。information-computation dissociation 解释了为什么 ablation *可以*增加 R²（移除了 probe 不需要的 routing signal），但没有解释为什么 random heads 的 \"噪声\" 比 structured routing signal 对 probe 的干扰更大。\n\n直觉上的问题：如果 instruction-dominant heads 携带 \"structured\" signal（所以对 probe 干扰较小），而 random heads 携带 \"unstructured\" noise（所以对 probe 干扰更大），这意味着 structured 和 unstructured 的区别在于对 probe 的干扰程度，而非对 task 的功能贡献。这能自洽，但需要论文更明确地说：\"dominant heads 的 signal 更 structured 意味着 probe 可以更容易地 learn around 它\"。当前 \"structured noise for the probe\" 的措辞暗示 routing signal 本身是 noise，这与论文的核心叙事（routing signal 是功能性的）存在语义张力。\n\n**结论**: PARTIALLY_RESOLVED 是正确的判断。severity 从 critical 降至 minor。\n\n**[AGREE] R9-N5 Counterfactual: RESOLVED**\n一致。\"从 problematic claim 转变为 empirically grounded observation\" 是准确的总结。\n\n**[REBUT] R9-N6 N=10 hedging: 我标 PARTIALLY_RESOLVED，R2 标 RESOLVED**\n分歧：R2 认为 hedging 已足够。我认为 §4.4 主文中缺少一句明确的 power limitation 声明。当前写法 \"non-significant on LIBERO-Goal (Δρ=0.017, 3%, N=10 tasks)\" 对 robotics 背景的读者而言，\"non-significant\" 可能被直接理解为 \"no effect\"。LIBERO-Spatial 的显著结果 (p<0.001) 已经暗示 LIBERO-Goal 的 n.s. 是 power 问题，但这个推论应由论文明确表述，而非让读者自行推断。\n\n这是一个小分歧。如果主文加一句 \"the non-significant result on LIBERO-Goal likely reflects the limited statistical power of N=10 tasks rather than a true null, given the significant effect on LIBERO-Spatial\" 就完全解决。不影响整体评分。\n\n**[AGREE] R9-I1 Octo: RESOLVED**\n一致。\n\n**[AGREE] R9-I2 Häon et al.: PARTIALLY_RESOLVED**\n同意。Related Work §2 第 3 段提到 Häon et al. 但仅一句话描述 (\"identified sparse semantic directions in VLA residual streams linked to action selection\")。Discussion §5 Limitations 提到 \"combining routing with activation steering [Häon et al.]\"。但两者之间的互补/冲突关系未讨论——L1 attention routing (head-level, attention weights) 和 sparse semantic directions (feature-level, residual stream) 是否捕捉同一机制的不同投影？这对理解 VLA 内部机制的完整图景是有价值的讨论点。\n\n---\n\n## Director 特别要求的三个问题\n\n### 1. R9-N4: MSE 证据是否充分解决了 ablation R² paradox？\n\n**部分解决，但非完全。** 上面已详细分析。总结：\n- MSE 证据 + information-computation dissociation 框架**解决了** \"为什么 ablation 可以同时增加 R² 和改变 trajectory\"。\n- **未解决** \"为什么 random ablation 的 R² 增加更大\"——这需要更精确的理论解释（structured signal 更容易被 probe learn around），而非 \"structured noise\"。\n- Severity 已从 critical 降至 minor。不再阻止接收。\n\n### 2. Conclusion 过于简短是否为新问题？\n\n**[REBUT] 不同意这是一个 problem。**\n\n理由：\n1. CoRL 8 页正文限制下，Conclusion 的核心功能是简洁总结，不是重复 Discussion。当前 3 行 Conclusion（\"token-level analysis framework... fine-tuning reorganizes instruction routing to entry-exit layers; seven complementary analyses identify L1 as the primary hub. Code and representations will be released upon acceptance.\"）完成了这个功能。\n2. 论文已有独立的 Discussion §5，包含 Synthesis、Mechanistic interpretation、Functional stages、Task-dependent routing、Limitations 五个段落。Discussion 承担了通常 Conclusion 的大部分职责。\n3. 将 Conclusion 压缩为 \\paragraph 而非独立 \\section 是合理的页面预算决策——释放空间给更有实质内容的分析。\n4. CoRL reviewer guidelines 未要求 Conclusion 必须为独立 section 或达到特定长度。\n\n这不应算作 weakness。\n\n### 3. Specificity d ratio 1.08× 的解读\n\n**[AGREE] 与 R2 基本一致，但 framing 不同。**\n\nR2 的解读：\"1.08× 削弱了 instruction-dominant heads are special 叙事\"。\n我的解读：1.08× 是对论文 **有利**的——论文在修订后已经将叙事从 \"dedicated instruction heads\" 转向 \"distributed, attention-graded routing\" (Discussion §5 第 2 段)。在这个新叙事下，modest specificity 是 **consistent with the claim** 而非 contradictory。\n\n论文现在的 claim 不是 \"这 24 个 heads 是特殊的 instruction routing 专用 heads\"，而是 \"L1 的所有 heads 都参与 routing，instruction-attention fraction 是一个连续的 graded predictor (dose-response curve 支持), 而非 binary 分类\"。d ratio 1.08× 和 dose-response 的 plateau beyond 20 heads 都与 distributed routing 一致。\n\n唯一的风险是：如果 **any** 24 heads 都产生类似效果 (d≈0.6)，那么 instruction-attention fraction 作为 predictor 的 value 降低——可能不是 attention-to-instruction 驱动了效果，而是 L1 的通用计算负载。但 Table A.18 的排序 (instruction 0.650 > random 0.601 > image-dominant 0.580 > bottom-24 0.565) 和 KL ratio 1.56× 仍然支持 attention-fraction 作为 weak but real predictor。\n\n这是论文的 honest boundary——用 8% gap 声称 graded specificity 是合理的，但不能声称 strong specificity。论文当前措辞 \"modest gap indicates distributed, attention-graded routing rather than a dedicated subset\" 恰到好处。\n\n---\n\n## 对 Reviewer 2 的 Questions 的评估\n\n**R2-Q1 (per-task MSE breakdown)**\n合理问题。Appendix Table A.11 有 per-task Cohen's d，但 per-task MSE 未报告。如果 MSE 不变是某些 task 增加 + 某些减少的平均效应（cancellation），则 \"MSE 不变\" 的 claim 会被削弱。这是一个 minor but valid follow-up。\n\n**R2-Q2 (any 24 heads 做类似的事？)**\n上面第 3 点已回应。简短回答：不完全是——排序存在且 monotonic，但 gap 小。distributed routing 是正确的 framing。\n\n---\n\n## 对 R2 新问题的总结\n\n| R2 新问题 | 我的判断 |\n|-----------|----------|\n| Conclusion 过短 | 不同意——CoRL 8 页限制下 Discussion 已承担 Conclusion 职能 |\n| Specificity 1.08× | 同意存在 limitation，但论文的 \"distributed routing\" framing 恰当处理了它 |\n\n---\n\n## 评分一致性\n\nR2: 6/10。我: 6/10。\n\n评分完全一致。我们的 \"阻止更高评分\" 原因也一致：单模型 + 无闭环。\nQuality 方面我给 3/5（vs R2 的 8/10 ≈ 4/5）——略低，因为我对 random-subset R² 反转的 residual concern 更重。\n\n如果 Director 需要 consensus statement：这是一篇方法论扎实、修订响应性强的分析论文，被单模型范围和缺乏闭环验证限制在 borderline above。\n",
  "reviewer_id": "1",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 对 Reviewer 2 Round 2 评估的交叉回应\n\n---\n\n## Issue 状态评估——逐条回应\n\n**[AGREE] R9-N1 单模型: STILL_OPEN**\n一致。无分歧。\n\n**[AGREE] R9-N2 无闭环: STILL_OPEN**\n一致。无分歧。\n\n**[AGREE] R9-W1 CoRL scope: PARTIALLY_RESOLVED**\n同意 \"边界但有连接\"。修订后 Discussion §5 对 deployment monitoring (L1 routing probes for instruction-discriminative tasks) 和 activation steering (cite Häon et al.) 的讨论使 robotics 连接更具体，但仍停留在 speculative 层面。\n\n**[AGREE] R9-W2 C1 占比: RESOLVED**\n一致。Abstract/Introduction 的重构有效解决了这个问题。\n\n**[AGREE] R9-W3 Vision framing: RESOLVED**\n一致。\n\n**[AGREE] R9-N3 Causal→Interventional: RESOLVED**\n一致。\n\n**[AGREE] R9-N4 Ablation R² 解释: PARTIALLY_RESOLVED**\n同意 MSE 证据显著降低了 severity，但 paradox 未完全消解。具体评估：\n\nMSE 证据解决了什么：它建立了 R² ↑ + trajectory change + MSE 不变 的三角关系，使 \"information-computation dissociation\" 框架站得住脚。routing heads 控制方向选择（哪个 action）而非精度（action 的准确度），这是一个 principled 且可检验的 claim。\n\nMSE 证据未解决什么：为什么 **random** 24 heads 的 ablation 产生比 instruction-dominant 24 heads **更大**的 R² 增加（+0.077 vs +0.042）。information-computation dissociation 解释了为什么 ablation *可以*增加 R²（移除了 probe 不需要的 routing signal），但没有解释为什么 random heads 的 \"噪声\" 比 structured routing signal 对 probe 的干扰更大。\n\n直觉上的问题：如果 instruction-dominant heads 携带 \"structured\" signal（所以对 probe 干扰较小），而 random heads 携带 \"unstructured\" noise（所以对 probe 干扰更大），这意味着 structured 和 unstructured 的区别在于对 probe 的干扰程度，而非对 task 的功能贡献。这能自洽，但需要论文更明确地说：\"dominant heads 的 signal 更 structured 意味着 probe 可以更容易地 learn around 它\"。当前 \"structured noise for the probe\" 的措辞暗示 routing signal 本身是 noise，这与论文的核心叙事（routing signal 是功能性的）存在语义张力。\n\n**结论**: PARTIALLY_RESOLVED 是正确的判断。severity 从 critical 降至 minor。\n\n**[AGREE] R9-N5 Counterfactual: RESOLVED**\n一致。\"从 problematic claim 转变为 empirically grounded observation\" 是准确的总结。\n\n**[REBUT] R9-N6 N=10 hedging: 我标 PARTIALLY_RESOLVED，R2 标 RESOLVED**\n分歧：R2 认为 hedging 已足够。我认为 §4.4 主文中缺少一句明确的 power limitation 声明。当前写法 \"non-significant on LIBERO-Goal (Δρ=0.017, 3%, N=10 tasks)\" 对 robotics 背景的读者而言，\"non-significant\" 可能被直接理解为 \"no effect\"。LIBERO-Spatial 的显著结果 (p<0.001) 已经暗示 LIBERO-Goal 的 n.s. 是 power 问题，但这个推论应由论文明确表述，而非让读者自行推断。\n\n这是一个小分歧。如果主文加一句 \"the non-significant result on LIBERO-Goal likely reflects the limited statistical power of N=10 tasks rather than a true null, given the significant effect on LIBERO-Spatial\" 就完全解决。不影响整体评分。\n\n**[AGREE] R9-I1 Octo: RESOLVED**\n一致。\n\n**[AGREE] R9-I2 Häon et al.: PARTIALLY_RESOLVED**\n同意。Related Work §2 第 3 段提到 Häon et al. 但仅一句话描述 (\"identified sparse semantic directions in VLA residual streams linked to action selection\")。Discussion §5 Limitations 提到 \"combining routing with activation steering [Häon et al.]\"。但两者之间的互补/冲突关系未讨论——L1 attention routing (head-level, attention weights) 和 sparse semantic directions (feature-level, residual stream) 是否捕捉同一机制的不同投影？这对理解 VLA 内部机制的完整图景是有价值的讨论点。\n\n---\n\n## Director 特别要求的三个问题\n\n### 1. R9-N4: MSE 证据是否充分解决了 ablation R² paradox？\n\n**部分解决，但非完全。** 上面已详细分析。总结：\n- MSE 证据 + information-computation dissociation 框架**解决了** \"为什么 ablation 可以同时增加 R² 和改变 trajectory\"。\n- **未解决** \"为什么 random ablation 的 R² 增加更大\"——这需要更精确的理论解释（structured signal 更容易被 probe learn around），而非 \"structured noise\"。\n- Severity 已从 critical 降至 minor。不再阻止接收。\n\n### 2. Conclusion 过于简短是否为新问题？\n\n**[REBUT] 不同意这是一个 problem。**\n\n理由：\n1. CoRL 8 页正文限制下，Conclusion 的核心功能是简洁总结，不是重复 Discussion。当前 3 行 Conclusion（\"token-level analysis framework... fine-tuning reorganizes instruction routing to entry-exit layers; seven complementary analyses identify L1 as the primary hub. Code and representations will be released upon acceptance.\"）完成了这个功能。\n2. 论文已有独立的 Discussion §5，包含 Synthesis、Mechanistic interpretation、Functional stages、Task-dependent routing、Limitations 五个段落。Discussion 承担了通常 Conclusion 的大部分职责。\n3. 将 Conclusion 压缩为 \\paragraph 而非独立 \\section 是合理的页面预算决策——释放空间给更有实质内容的分析。\n4. CoRL reviewer guidelines 未要求 Conclusion 必须为独立 section 或达到特定长度。\n\n这不应算作 weakness。\n\n### 3. Specificity d ratio 1.08× 的解读\n\n**[AGREE] 与 R2 基本一致，但 framing 不同。**\n\nR2 的解读：\"1.08× 削弱了 instruction-dominant heads are special 叙事\"。\n我的解读：1.08× 是对论文 **有利**的——论文在修订后已经将叙事从 \"dedicated instruction heads\" 转向 \"distributed, attention-graded routing\" (Discussion §5 第 2 段)。在这个新叙事下，modest specificity 是 **consistent with the claim** 而非 contradictory。\n\n论文现在的 claim 不是 \"这 24 个 heads 是特殊的 instruction routing 专用 heads\"，而是 \"L1 的所有 heads 都参与 routing，instruction-attention fraction 是一个连续的 graded predictor (dose-response curve 支持), 而非 binary 分类\"。d ratio 1.08× 和 dose-response 的 plateau beyond 20 heads 都与 distributed routing 一致。\n\n唯一的风险是：如果 **any** 24 heads 都产生类似效果 (d≈0.6)，那么 instruction-attention fraction 作为 predictor 的 value 降低——可能不是 attention-to-instruction 驱动了效果，而是 L1 的通用计算负载。但 Table A.18 的排序 (instruction 0.650 > random 0.601 > image-dominant 0.580 > bottom-24 0.565) 和 KL ratio 1.56× 仍然支持 attention-fraction 作为 weak but real predictor。\n\n这是论文的 honest boundary——用 8% gap 声称 graded specificity 是合理的，但不能声称 strong specificity。论文当前措辞 \"modest gap indicates distributed, attention-graded routing rather than a dedicated subset\" 恰到好处。\n\n---\n\n## 对 Reviewer 2 的 Questions 的评估\n\n**R2-Q1 (per-task MSE breakdown)**\n合理问题。Appendix Table A.11 有 per-task Cohen's d，但 per-task MSE 未报告。如果 MSE 不变是某些 task 增加 + 某些减少的平均效应（cancellation），则 \"MSE 不变\" 的 claim 会被削弱。这是一个 minor but valid follow-up。\n\n**R2-Q2 (any 24 heads 做类似的事？)**\n上面第 3 点已回应。简短回答：不完全是——排序存在且 monotonic，但 gap 小。distributed routing 是正确的 framing。\n\n---\n\n## 对 R2 新问题的总结\n\n| R2 新问题 | 我的判断 |\n|-----------|----------|\n| Conclusion 过短 | 不同意——CoRL 8 页限制下 Discussion 已承担 Conclusion 职能 |\n| Specificity 1.08× | 同意存在 limitation，但论文的 \"distributed routing\" framing 恰当处理了它 |\n\n---\n\n## 评分一致性\n\nR2: 6/10。我: 6/10。\n\n评分完全一致。我们的 \"阻止更高评分\" 原因也一致：单模型 + 无闭环。\nQuality 方面我给 3/5（vs R2 的 8/10 ≈ 4/5）——略低，因为我对 random-subset R² 反转的 residual concern 更重。\n\n如果 Director 需要 consensus statement：这是一篇方法论扎实、修订响应性强的分析论文，被单模型范围和缺乏闭环验证限制在 borderline above。\n",
    "reviewer_id": "1",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 337 · 2026-05-19T06:03:06.725102+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5310
}
```

</details>

---


### Assistant

_source line 338 · 2026-05-19T06:03:13.077274+00:00_

交叉回应已提交。

与 R2 的主要共识：6/10 评分一致；单模型+无闭环是根本限制；MSE 证据显著改善但未完全消解 ablation paradox。

两处分歧：(1) N=10 power limitation 我认为仍需主文中一句明确声明（R2 判 RESOLVED，我判 PARTIALLY_RESOLVED）；(2) Conclusion 过短——我不认为这是问题，CoRL 8 页限制下 Discussion 已承担该职能。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1"
}
```

</details>

---


## Round 19

## Round 19

12 recorded events


### User

_source line 339 · 2026-05-19T06:27:30.449184+00:00_

[Round 3 审稿请求]:
# Reviewer 1 — Round 11 增量评估

## 任务
论文根据 Round 10 审稿报告中 5 个 in_progress issues 进行了针对性修改（句子级）。请逐条评估修复状态。

**论文路径**: `projects/vla-ssd/docs/paper/main.tex`
**目标 venue**: CoRL 2026（8 页正文，双盲）

## 本轮修改清单（对比 Round 10）

### 1. R9-N4: Random R² > instruction R² 解释
**Discussion line 14 新增末句**: "and random ablation yields a larger $R^2$ gain ($+0.077$ vs. $+0.042$) because unstructured perturbation releases probe capacity without disrupting organized computation."
- Round 10 状态: PARTIALLY_RESOLVED (minor)
- 要求: 解释为什么 random heads ablation 的 R² 增加大于 instruction-dominant heads

### 2. R9-N6: Power limitation 显式声明
**Experiments §4.4 line 122 新增**: "The $N = 10$ instruction set limits statistical power for detecting small effects; non-significant differences should not be interpreted as evidence of absence."
- Round 10 状态: R1 判 PARTIALLY_RESOLVED，R2 判 RESOLVED
- 要求: R1 要求主文一句明确的 power limitation 声明

### 3. R9-W1: L1 entropy runtime monitor
**Discussion line 23 新增末句**: "and L1 attention entropy could monitor cases where the model under-attends to instructions at runtime."
- Round 10 状态: PARTIALLY_RESOLVED
- 要求: 增加具体 deployment implication

### 4. R9-I2: Häon et al. where/what 互补
**Discussion line 28 重写**: "Our routing analysis (\emph{where}) complements Häon et al.'s (\emph{what} is encoded); closed-loop evaluation combining both is a natural extension."
- Round 10 状态: PARTIALLY_RESOLVED
- 要求: 1-2 句连接 L1 routing 和 sparse semantic directions 的互补关系

### 5. R10-Q1: Per-task MSE breakdown
**Appendix line 123 新增**: "Per-task breakdown shows all $|\Delta\text{MSE}| < 3\%$ of baseline with all $p > 0.27$; the near-zero aggregate $\Delta$ reflects uniformly small per-task effects rather than cancellation across tasks."
- Round 10 状态: in_progress (rebuttal question)
- 要求: 提供 per-task MSE 证据排除 cancellation

### 6. 其他小改
- Conclusion line 2: 轻微重写（"with L1 as the primary hub, supported by seven complementary analyses"）
- Discussion line 18: "potential pruning targets" → "suggesting pruning potential"
- Discussion line 19: Predictions 格式简化

## 评估要求

对每个 in_progress issue 标注：
- **[RESOLVED]** 修改充分解决了问题 + 理由
- **[STILL_OPEN]** 仍有未解决的 concern + 具体说明
- **[REGRESSED]** 修改引入了新问题

关注：
1. 新增句子是否 scientifically accurate、internally consistent
2. 是否引入新的 overclaim 或逻辑矛盾
3. 整体评分是否需要调整（上轮共识 6/10）

本轮是微调级修改，评估应简洁聚焦。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 340 · 2026-05-19T06:27:39.074444+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 341 · 2026-05-19T06:27:39.376082+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Synthesis.}
5	VLA fine-tuning primarily reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\Delta \leq 1.7\%$).
6	This explains the visual dominance of Grant et al.~\cite{grant2026}: DINOv2 has the highest geometric alignment ($\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\ $0.634$).
7	Seven complementary analyses support instruction-conditioned action generation through distributed L1 routing, where instruction-attention fraction predicts per-head contribution magnitude.
8	\emph{Interventional}: (1)~dose-response (8 conditions, $d = 0.48 \to 0.64$; Figure~\ref{fig:dose_response}); (2)~counterfactual analysis (4 perturbations, $d = 0.63$--$0.97$; Table~\ref{tab:counterfactual}).
9	\emph{Supporting}: (3)~attention gradient ($0 \to 9 \to 24$ heads); (4)~$R^2$ ablation gradient ($+0.059$ at L1, $\approx 0$ at L13); (5)~trajectory divergence ($d = 0.65$, $72.3\%$ tokens).
10	\emph{Constraining}: (6)~per-head bootstrap CIs ($d$: individual $0.027$ vs.\ $0.051$; collective $0.65$ vs.\ $0.41$; $p = 0.0018$); (7)~specificity control ($1.08\times$; Table~\ref{tab:specificity_control}).
11	
12	\paragraph{Mechanistic interpretation.}
13	Matched-size ablation ($d$: instruction $0.65$, random $0.60$, image $0.58$; Table~\ref{tab:specificity_control}) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed routing; counterfactual ordering follows token novelty ($\rho = 1.0$; \S\ref{sec:learned_routing}).
14	That ablation raises $R^2$ yet alters trajectories ($d = 0.65$) without increasing ground-truth error ($\Delta\text{MSE} \approx 0$; Appendix~\ref{sec:action_trajectory}) reflects an information-computation dissociation~\cite{hewitt2019control}: routing controls direction rather than precision, and random ablation yields a larger $R^2$ gain ($+0
…[truncated 2092 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 342 · 2026-05-19T06:27:39.828400+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
  "offset": "118",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
    "offset": "118",
    "limit": "10"
  }
}
```

</details>

---


### Tool result

_source line 343 · 2026-05-19T06:27:40.330904+00:00_

118	Under linear CKA, this pattern disappears (monotonic increase; Appendix~\ref{sec:cka_appendix}); the non-monotonic trajectory characterizes rank-order geometry specifically, not global covariance structure.
119	
120	\paragraph{Training primarily enhances readout decodability.}
121	Best-vs-best RSA gain is non-significant on LIBERO-Goal ($\Delta\rho = 0.017$, $3\%$, $N{=}10$ tasks; Appendix Table~\ref{tab:training_effects}), though LIBERO-Spatial yields a significant geometric gain ($\Delta = +0.023$, $p < 0.001$; Appendix~\ref{sec:cross_benchmark_appendix}).
122	The $N = 10$ instruction set limits statistical power for detecting small effects; non-significant differences should not be interpreted as evidence of absence.
123	Functional improvements are larger: readout $R^2$ $\Delta = +0.069$ ($p < 0.0001$, 95\% CI $[0.047, 0.090]$), image\_mean $\Delta = +0.015$ ($p = 0.006$), surviving FDR correction at 29--30/33 layers.
124	
125	\begin{table}[t]
126	\centering
127	\caption{RSA $\rho$ and probe $R^2$ alignment with actions. DINOv2 achieves highest RSA ($0.692$); ordering is metric-dependent (Appendix~\ref{sec:cka_appendix}). VLA rows: peak values. \textbf{Bold}: best; \underline{underline}: second.}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 344 · 2026-05-19T06:27:40.783082+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "offset": "113",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "offset": "113",
    "limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 345 · 2026-05-19T06:27:41.084843+00:00_

113	\paragraph{Trajectory-level aggregation.}
114	Aggregating per-demo mean actions to the trajectory level reveals that token-level $d$ values are conservative: within-trajectory averaging reduces noise, yielding ${\sim}4\times$ larger effect sizes (mean token-to-trajectory ratio $0.245$).
115	Instruction-head ablation ($N = 50$: 5 tasks $\times$ 10 demos) yields trajectory $d = 2.943$ (95\% CI $[2.469, 3.707]$); bottom-24 non-instruction heads ($N = 30$) yield $d = 2.347$ (CI $[1.854, 3.221]$).
116	All 14 conditions produce trajectory $d > 2.0$ with CI lower bounds $> 1.7$.
117	Counterfactual trajectory-level $d$: empty $3.438$ (CI $[2.921, 4.448]$), wrong $3.798$ ($[3.194, 4.938]$), paraphrased $2.131$ ($[1.740, 2.819]$), shuffled $2.595$ ($[2.028, 3.791]$).
118	Fine-grained ordering is not reliably distinguished at trajectory level ($N = 30$); token-level comparisons ($N {\sim} 1{,}500$) provide higher resolution for ordering claims.
119	
120	\paragraph{Ground-truth action error.}
121	Ablation redirects model outputs ($d = 0.65$) but does not systematically increase error relative to expert demonstrations: original MSE $= 0.498$; top-24 instruction-head ablation MSE $= 0.497$ ($\Delta = -0.001$, Wilcoxon $p = 0.52$, n.s.); bottom-24 non-instruction heads MSE $= 0.506$ ($\Delta = +0.008$).
122	Changes concentrate on the gripper dimension; translation and rotation dimensions are negligibly affected.
123	Per-task breakdown shows all $|\Delta\text{MSE}| < 3\%$ of baseline with all $p > 0.27$; the near-zero aggregate $\Delta$ reflects uniformly small per-task effects rather than cancellation across tasks.
124	This is consistent with the information-computation dissociation: routing heads control instruction-specific direction selection rather than action precision.
125	
126	Table~\ref{tab:perhead_bootstrap} reports per-head bootstrap CIs ($10{,}000$ resamples).
127	Individual control heads produce ${\sim}1.9\times$ stronger effects ($d = 0.051$) than instruction head
…[truncated 454 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 346 · 2026-05-19T06:27:41.085278+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 347 · 2026-05-19T06:27:41.185974+00:00_

1	\paragraph{Conclusion.}
2	We find that VLA fine-tuning reorganizes instruction routing to entry-exit layers with L1 as the primary hub, supported by seven complementary analyses.
3	Code and data will be released upon acceptance.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 348 · 2026-05-19T06:28:46.882484+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 — Round 11 增量评估\n\n---\n\n## 逐条评估\n\n### 1. R9-N4: Random R² > instruction R² 解释 → **[RESOLVED]**\n\nDiscussion line 14 新增: \"and random ablation yields a larger R² gain (+0.077 vs. +0.042) because unstructured perturbation releases probe capacity without disrupting organized computation.\"\n\n评估:\n- **Scientific accuracy**: 合理。逻辑链完整: instruction-dominant heads 携带 organized routing signal → probe 可以 learn around structured signal（干扰小）→ ablation 后 R² 增幅较小。Random heads 携带 unstructured 贡献 → probe 需要更多 capacity 来 ignore → ablation 后释放 capacity → R² 增幅更大。\n- **与 information-computation dissociation 框架一致**: 是。该句直接延伸了同段前半部分的 Hewitt & Liang 引用。\n- **Overclaim 风险**: 低。\"releases probe capacity\" 是对 probe 行为的合理推断，虽非直接验证（理想情况下应测量 ablation 前后 probe 的 effective dimensionality），但作为 interpretive text 在分析论文中是标准做法。\n- **综合**: 结合 MSE 不变 + information-computation dissociation + 此句对 random > dominant 的解释，整个 ablation 叙事现在形成闭环。从 Round 1 的 critical issue 到现在 fully resolved，经历了三轮迭代。\n\n### 2. R9-N6: Power limitation 声明 → **[RESOLVED]**\n\nExperiments §4.4 line 122: \"The N=10 instruction set limits statistical power for detecting small effects; non-significant differences should not be interpreted as evidence of absence.\"\n\n评估:\n- 这正是我在 Round 10 和交叉回应中明确要求的句子。\n- 位置恰当（紧跟 LIBERO-Goal n.s. 结果和 LIBERO-Spatial 显著结果之后）。\n- 措辞精确（\"should not be interpreted as evidence of absence\" 是标准统计学表述）。\n- 无 overclaim，无逻辑矛盾。\n\n### 3. R9-W1: L1 entropy runtime monitor → **[RESOLVED]**\n\nDiscussion line 23 新增: \"and L1 attention entropy could monitor cases where the model under-attends to instructions at runtime.\"\n\n评估:\n- \"could\" 恰当 hedging，未声称已验证。\n- 从 finding (L1 has 24/32 instruction-dominant heads) 到 implication (monitor attention entropy at deployment) 的逻辑跳跃合理且具体。\n- 比上轮泛泛的 \"L1 routing probes can flag instruction-discriminative tasks\" 更 actionable（指定了具体信号: attention entropy）。\n- 未引入新的 overclaim。\n\n### 4. R9-I2: Häon et al. where/what 互补 → **[RESOLVED]**\n\nDiscussion line 28: \"Our routing analysis (where) complements Häon et al.'s (what is encoded); closed-loop evaluation combining both is a natural extension.\"\n\n评估:\n- Where/what 是简洁有效的 framing: 本文研究 attention routing mechanism（信息通过哪些 heads 传递），Häon et al. 研究 residual stream 中的 sparse semantic directions（传递了什么语义内容）。两个视角正交且互补。\n- 嵌入 Limitations 段落中，长度恰当（不是 Related Work 级别的深入对比，而是 scope-aware 的 positioning）。\n- 以 \"closed-loop evaluation combining both\" 收尾，指向具体的 future work 方向。\n\n### 5. R10-Q1: Per-task MSE breakdown → **[RESOLVED]**\n\nAppendix line 123: \"Per-task breakdown shows all |ΔMSE| < 3% of baseline with all p > 0.27; the near-zero aggregate Δ reflects uniformly small per-task effects rather than cancellation across tasks.\"\n\n评估:\n- 直接回答了 R2 的 Q1（是否存在 cancellation）。\n- 定量证据充分: |ΔMSE| < 3% + all p > 0.27 排除了 \"某些 task 增大 + 某些减小\" 的 cancellation scenario。\n- 理想情况下附一个 per-task MSE table，但 summary statistics 足以支撑 claim。在 appendix 中这个详细程度合适。\n\n### 6. 其他小改 → **无问题**\n\n- Conclusion line 2: \"with L1 as the primary hub, supported by seven complementary analyses\" — 信息密度略增，同时保持简洁。不构成 R2 指出的 \"过短\" 问题（我上轮已 rebut 过该 concern）。\n- Discussion line 18: \"potential pruning targets\" → \"suggesting pruning potential\" — 更 hedged，减少 overclaim。正确方向。\n- Discussion line 19: Predictions 格式简化 — 纯 editorial，无 substantive 变化。\n\n---\n\n## 新问题检查\n\n**未发现任何新问题。** 所有修改为句子级 additions/edits，与现有内容一致，未引入逻辑矛盾或新的 overclaim。\n\n---\n\n## 总结\n\n| Issue | Round 10 状态 | Round 11 状态 | 备注 |\n|-------|-------------|-------------|------|\n| R9-N4 Random R² 解释 | PARTIALLY_RESOLVED (minor) | **RESOLVED** | information-computation dissociation 闭环 |\n| R9-N6 Power limitation | PARTIALLY_RESOLVED | **RESOLVED** | 主文显式声明 |\n| R9-W1 Deployment implication | PARTIALLY_RESOLVED | **RESOLVED** | L1 entropy monitor |\n| R9-I2 Häon et al. | PARTIALLY_RESOLVED | **RESOLVED** | where/what framing |\n| R10-Q1 Per-task MSE | in_progress | **RESOLVED** | 排除 cancellation |\n\n**所有 5 个 in_progress issues 均已 RESOLVED。本轮无 regression。**\n\n---\n\n## 评分\n\n**维持 6/10 (marginally above acceptance threshold)**。\n\n理由: 这些微调修复了所有 warning-level 和 info-level 的残留问题，论文在方法严谨性维度已无 open issues。但阻止更高评分的两个 scope 限制（单模型 OpenVLA-7B、无闭环验证）不是句子级修改能解决的。\n\n当前论文状态: 在其 scope 内（单模型 representational analysis），方法论 sound、统计报告 honest、修订 responsive。对 CoRL 而言，borderline above 是合理定位。\n",
  "reviewer_id": "1",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 — Round 11 增量评估\n\n---\n\n## 逐条评估\n\n### 1. R9-N4: Random R² > instruction R² 解释 → **[RESOLVED]**\n\nDiscussion line 14 新增: \"and random ablation yields a larger R² gain (+0.077 vs. +0.042) because unstructured perturbation releases probe capacity without disrupting organized computation.\"\n\n评估:\n- **Scientific accuracy**: 合理。逻辑链完整: instruction-dominant heads 携带 organized routing signal → probe 可以 learn around structured signal（干扰小）→ ablation 后 R² 增幅较小。Random heads 携带 unstructured 贡献 → probe 需要更多 capacity 来 ignore → ablation 后释放 capacity → R² 增幅更大。\n- **与 information-computation dissociation 框架一致**: 是。该句直接延伸了同段前半部分的 Hewitt & Liang 引用。\n- **Overclaim 风险**: 低。\"releases probe capacity\" 是对 probe 行为的合理推断，虽非直接验证（理想情况下应测量 ablation 前后 probe 的 effective dimensionality），但作为 interpretive text 在分析论文中是标准做法。\n- **综合**: 结合 MSE 不变 + information-computation dissociation + 此句对 random > dominant 的解释，整个 ablation 叙事现在形成闭环。从 Round 1 的 critical issue 到现在 fully resolved，经历了三轮迭代。\n\n### 2. R9-N6: Power limitation 声明 → **[RESOLVED]**\n\nExperiments §4.4 line 122: \"The N=10 instruction set limits statistical power for detecting small effects; non-significant differences should not be interpreted as evidence of absence.\"\n\n评估:\n- 这正是我在 Round 10 和交叉回应中明确要求的句子。\n- 位置恰当（紧跟 LIBERO-Goal n.s. 结果和 LIBERO-Spatial 显著结果之后）。\n- 措辞精确（\"should not be interpreted as evidence of absence\" 是标准统计学表述）。\n- 无 overclaim，无逻辑矛盾。\n\n### 3. R9-W1: L1 entropy runtime monitor → **[RESOLVED]**\n\nDiscussion line 23 新增: \"and L1 attention entropy could monitor cases where the model under-attends to instructions at runtime.\"\n\n评估:\n- \"could\" 恰当 hedging，未声称已验证。\n- 从 finding (L1 has 24/32 instruction-dominant heads) 到 implication (monitor attention entropy at deployment) 的逻辑跳跃合理且具体。\n- 比上轮泛泛的 \"L1 routing probes can flag instruction-discriminative tasks\" 更 actionable（指定了具体信号: attention entropy）。\n- 未引入新的 overclaim。\n\n### 4. R9-I2: Häon et al. where/what 互补 → **[RESOLVED]**\n\nDiscussion line 28: \"Our routing analysis (where) complements Häon et al.'s (what is encoded); closed-loop evaluation combining both is a natural extension.\"\n\n评估:\n- Where/what 是简洁有效的 framing: 本文研究 attention routing mechanism（信息通过哪些 heads 传递），Häon et al. 研究 residual stream 中的 sparse semantic directions（传递了什么语义内容）。两个视角正交且互补。\n- 嵌入 Limitations 段落中，长度恰当（不是 Related Work 级别的深入对比，而是 scope-aware 的 positioning）。\n- 以 \"closed-loop evaluation combining both\" 收尾，指向具体的 future work 方向。\n\n### 5. R10-Q1: Per-task MSE breakdown → **[RESOLVED]**\n\nAppendix line 123: \"Per-task breakdown shows all |ΔMSE| < 3% of baseline with all p > 0.27; the near-zero aggregate Δ reflects uniformly small per-task effects rather than cancellation across tasks.\"\n\n评估:\n- 直接回答了 R2 的 Q1（是否存在 cancellation）。\n- 定量证据充分: |ΔMSE| < 3% + all p > 0.27 排除了 \"某些 task 增大 + 某些减小\" 的 cancellation scenario。\n- 理想情况下附一个 per-task MSE table，但 summary statistics 足以支撑 claim。在 appendix 中这个详细程度合适。\n\n### 6. 其他小改 → **无问题**\n\n- Conclusion line 2: \"with L1 as the primary hub, supported by seven complementary analyses\" — 信息密度略增，同时保持简洁。不构成 R2 指出的 \"过短\" 问题（我上轮已 rebut 过该 concern）。\n- Discussion line 18: \"potential pruning targets\" → \"suggesting pruning potential\" — 更 hedged，减少 overclaim。正确方向。\n- Discussion line 19: Predictions 格式简化 — 纯 editorial，无 substantive 变化。\n\n---\n\n## 新问题检查\n\n**未发现任何新问题。** 所有修改为句子级 additions/edits，与现有内容一致，未引入逻辑矛盾或新的 overclaim。\n\n---\n\n## 总结\n\n| Issue | Round 10 状态 | Round 11 状态 | 备注 |\n|-------|-------------|-------------|------|\n| R9-N4 Random R² 解释 | PARTIALLY_RESOLVED (minor) | **RESOLVED** | information-computation dissociation 闭环 |\n| R9-N6 Power limitation | PARTIALLY_RESOLVED | **RESOLVED** | 主文显式声明 |\n| R9-W1 Deployment implication | PARTIALLY_RESOLVED | **RESOLVED** | L1 entropy monitor |\n| R9-I2 Häon et al. | PARTIALLY_RESOLVED | **RESOLVED** | where/what framing |\n| R10-Q1 Per-task MSE | in_progress | **RESOLVED** | 排除 cancellation |\n\n**所有 5 个 in_progress issues 均已 RESOLVED。本轮无 regression。**\n\n---\n\n## 评分\n\n**维持 6/10 (marginally above acceptance threshold)**。\n\n理由: 这些微调修复了所有 warning-level 和 info-level 的残留问题，论文在方法严谨性维度已无 open issues。但阻止更高评分的两个 scope 限制（单模型 OpenVLA-7B、无闭环验证）不是句子级修改能解决的。\n\n当前论文状态: 在其 scope 内（单模型 representational analysis），方法论 sound、统计报告 honest、修订 responsive。对 CoRL 而言，borderline above 是合理定位。\n",
    "reviewer_id": "1",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 349 · 2026-05-19T06:28:51.047834+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4165
}
```

</details>

---


### Assistant

_source line 350 · 2026-05-19T06:28:54.846964+00:00_

报告已提交。

所有 5 个 in_progress issues 均标注 **[RESOLVED]**。评分维持 **6/10**——方法严谨性维度已无 open issues，剩余限制（单模型、无闭环）属 scope 层面，无法通过句子级修改解决。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1"
}
```

</details>

---


## Round 20

## Round 20

116 recorded events


### User

_source line 351 · 2026-05-20T11:37:23.930685+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责 **方法严谨性 + 实验有效性**。

## Venue 信息
- **目标会议**: CoRL 2026 (Conference on Robot Learning)
- **截止日期**: 2026-05-29
- **页数限制**: 8 页正文（参考文献、附录不计）
- **模板**: `\usepackage{corl_2026}`
- **匿名规则**: Double-blind
- **附录**: 允许，可参与审稿
- **特殊要求**: 必须包含 Limitations section；鼓励 real-robot experiments 或 simulation-to-real transferability 证据

## 论文文件
- LaTeX: `docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.pdf`

## 你的审查侧重

**核心任务：评估实验设计和统计方法的严谨性。**

请重点审查以下方面：

1. **实验设计与控制变量**
   - 2×2 factorial design（trained/untrained × instruction present/absent）是否充分？
   - 三条件对比（VLA-trained, Llama-2 base, untrained）是否能有效隔离 fine-tuning 效果？
   - 外部 baseline（DINOv2, CLIP）的选择是否合理？

2. **统计方法有效性**
   - Bootstrap CI（10,000 resamples）的使用是否恰当？task-level blocking 是否充分处理了层级依赖？
   - Cohen's d 独立性假设是否在 token-level 分析中成立？
   - N_eff（有效样本量）的处理是否透明？
   - FDR 多重比较校正是否正确应用？

3. **Probe 方法论**
   - MLP probe（2层, 256 hidden）是否 capacity 过大导致 overfitting？linear probe 是否作为充分对照？
   - Demo-level train/test split 是否有效防止时间泄漏？
   - Cross-instruction probe 的 LOOCV 设计是否能排除记忆效应？

4. **因果推断逻辑**
   - Attention ablation → R² 变化的因果推断链是否成立？
   - Ablation 使 R² 增加的 paradox 解释（information-computation dissociation）是否令人信服？
   - "Instruction routing" 从 observational evidence 到 mechanistic claim 的推断强度是否合适？

5. **跨架构泛化**
   - TracVLA (Phi-3-V) 的验证是否充分？（仅 5 个 LIBERO-Goal tasks, pre-VLA baseline 不同）
   - 从 2 个架构推广到 "VLA fine-tuning" 的一般性声称是否过强？

6. **遗漏的关键实验**
   - 是否缺少必要的控制实验？
   - 对 CoRL 来说，纯 open-loop representational analysis（无 closed-loop 机器人评估）是否构成关键缺陷？

请以标准审稿格式输出：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（含评分和置信度）。对每个 Weakness 标注严重程度（critical/warning/info）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 352 · 2026-05-20T11:37:30.180762+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 353 · 2026-05-20T11:37:30.181446+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/sessions/review_reviewer_1_458aa27f.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 354 · 2026-05-20T11:37:33.648236+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15"
  }
}
```

</details>

---


### Tool result

_source line 355 · 2026-05-20T11:37:33.698790+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 356 · 2026-05-20T11:37:36.158480+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/skills/**/*review*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/skills/**/*review*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15"
  }
}
```

</details>

---


### Tool result

_source line 357 · 2026-05-20T11:37:36.209365+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 358 · 2026-05-20T11:37:38.920072+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/skills/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/skills/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15"
  }
}
```

</details>

---


### Tool result

_source line 359 · 2026-05-20T11:37:38.920514+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 360 · 2026-05-20T11:37:43.048463+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 361 · 2026-05-20T11:37:43.099405+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 362 · 2026-05-20T11:37:47.621170+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 363 · 2026-05-20T11:37:49.428968+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.pdf",
  "project": "vla-ssd",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.pdf",
    "project": "vla-ssd",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 364 · 2026-05-20T11:37:50.182102+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 365 · 2026-05-20T11:37:54.148858+00:00_

Web search results for query: "CoRL 2026 reviewer guidelines review form criteria"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"2026 Reviewer Guidelines","url":"https://neurips.cc/Conferences/2026/ReviewerGuidelines"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CVPR 2026 Reviewer Guidelines","url":"https://cvpr.thecvf.com/Conferences/2026/ReviewerGuidelinesq"},{"title":"Which Coauthor Should I Nominate in My 99 ICLR Submissions? A Mathematical Analysis of the ICLR 2026 Reciprocal Reviewer Nomination Policy","url":"https://arxiv.org/pdf/2512.17950"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"}]

Based on the search results, I found information related to CoRL 2026, though I should note that the most specific reviewer guidelines information in the results is from CoRL 2024. Here's what I found:

## CoRL 2026 Reviewer Requirements

All submissions must include at least one author who agrees to serve as a CoRL reviewer, and they are qualified if they have at least one accepted publication at a previous robotics (CoRL/ICRA/IROS/RSS) or learning conference (ICLR/NeurIPS/ICML) or equivalent journal.

## Review Criteria (from CoRL 2024)

While I couldn't find the specific CoRL 2026 review form criteria in these results, the 2024 guidance indicates that submissions are evaluated based on the significance and novelty of the results, either theoretical or empirical.

Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Additionally, all submissions should include a Limitations section, explicitly describing limiting assumptions, failure modes, and other limitations of 
…[truncated 402 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6527
}
```

</details>

---


### Tool result

_source line 366 · 2026-05-20T11:37:55.256093+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images/main_p1.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 311.4}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images/main_p2.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 399.3}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images/main_p3.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 363.9}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images/main_p4.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 346.3}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images/main_p5.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 338.3}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images/main_p6.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 379.4}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images/main_p7.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 324.5}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images/main_p8.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 272.7}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images/main_p9.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 361.4}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images/main_p10.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 365.4}], \"total_pages\": 31, \"rendered_pages\": 10, \"dpi\": 150, \"output_dir\": \"/home
…[truncated 124 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 5827
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-20T11:37:55.256743+00:00_

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
16	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
17	\setlength{\intextsep}{8pt plus 2pt minus 2pt}
18	\setlength{\floatsep}{8pt plus 2pt minus 4pt}
19	\setlength{\abovecaptionskip}{4pt}
20	\setlength{\belowcaptionskip}{0pt}
21	
22	\title{Vision Encodes, Language Routes:\\ Token-Level Functional Specialization in a Vision-Language-Action Model}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	
28	\maketitle
29	
30	\begin{abstract}
31	\input{abstract}
32	\end{abstract}
33	
34	\input{introduction}
35	\input{related_work}
36	\input{method}
37	\input{experiments}
38	\input{discussion}
39	\input{conclusion}
40	
41	\bibliography{references}
42	
43	\input{appendix}
44	
45	\end{document}
46	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 5074
}
```

</details>

---


### Tool call

_source line 368 · 2026-05-20T11:38:01.250304+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 369 · 2026-05-20T11:38:01.753066+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 370 · 2026-05-20T11:38:02.709770+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1459
}
```

</details>

---


### Tool result

_source line 371 · 2026-05-20T11:38:02.711021+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-20T11:38:02.711369+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 373 · 2026-05-20T11:38:03.169716+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 458
}
```

</details>

---


### Tool call

_source line 374 · 2026-05-20T11:38:03.221278+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---
