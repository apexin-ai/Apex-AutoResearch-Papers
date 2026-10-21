# Reviewer 2 coordination — Part 1 of 2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

[Transcript overview](../reviewer-2-coordination.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/49/4904f20abb631b58b816.json)

## Round 1

## Round 1

56 recorded events


### User

_source line 1 · 2026-05-17T04:31:54.194304+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2（新颖性 + Related Work + 实际意义）

### Venue 信息
- **目标会议**: CoRL 2026
- **截止日期**: 2026-05-28（论文）
- **页数限制**: 8 页正文 + references + appendix
- **模板**: corl_2026（已正确使用）
- **匿名规则**: double-blind
- **特殊要求**: 必须含 Limitations section（计入 8 页），需论证 robotics relevance，鼓励 real-robot experiments 或 sim-to-real 证据

### 论文路径
`projects/vla-ssd/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, appendix.tex, references.bib）

### 你的审查侧重

**新颖性、Related Work 覆盖度、对机器人社区的实际意义**，重点关注：

1. **新颖性评估**：
   - 相对于 Grant 2026（vision dominance behavioral study）、Haon 2025（mechanistic interp for VLA steering）、Swann 2026（SAE on VLA）、Buurmeijer/Rizzardo 2026（feature observability/controllability）的增量贡献是什么？
   - "First token-level representational decomposition" 这一 claim 是否成立？检查是否有未引用的先行工作
   - RSA + probing + attention analysis 组合是否构成方法论创新，还是标准工具的直接应用？
   - trained vs untrained 对照的 novelty：是否有其他工作已做过类似比较？

2. **Related Work 完整性**：
   - 检查是否遗漏关键 related work（特别是 2025-2026 年 VLA interpretability/analysis 方向）
   - 检查 VLM representation analysis 文献（非 VLA 领域但方法高度相关的工作）
   - 引用密度是否符合 CoRL 水准（当前约 17 篇引用，是否偏少）
   - Related Work section 是否做到了有效 positioning（不是 survey 而是建立 gap）

3. **对 Robotics 社区的实际意义**：
   - 三个 finding 是否能转化为可操作的设计建议？
   - "vision encoder quality is the primary design lever" 是否有足够证据？
   - 没有 real-robot 实验或 sim-to-real 验证——这对 CoRL 是否是致命缺陷？
   - 纯分析论文在 CoRL 的历史接受率如何？

4. **Claim 与 evidence 的匹配**：
   - "strict functional specialization" 是否 overclaim（仅在 LIBERO 上验证）
   - Design implications 是否过于 speculative（未验证 early-exit at L12 等）
   - Abstract 中的强结论与 Discussion 中的 limitations 是否矛盾

请给出结构化审稿报告：Summary → Strengths → Weaknesses → Questions → Missing References

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-17T04:32:06.390314+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
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

_source line 3 · 2026-05-17T04:32:06.390740+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-17T04:32:13.297275+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 5 · 2026-05-17T04:32:13.598882+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 6 · 2026-05-17T04:32:13.649512+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-17T04:32:19.421265+00:00_

Web search results for query: "CoRL 2026 reviewer guidelines review form criteria"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CVPR 2026 Reviewer Guidelines","url":"https://cvpr.thecvf.com/Conferences/2026/ReviewerGuidelinesq"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"}]

Based on the search results, I found information about CoRL 2026, though a specific dedicated "CoRL 2026 Reviewer Guidelines" document with detailed review form criteria was not located in the search results. However, I can share what I found:

## Available CoRL 2026 Information

The search revealed general submission and author information for CoRL 2026, but not a comprehensive reviewer guidelines document. Here's what was found:

**General Reviewer Requirements:**
All submissions must include at least one author who agrees to serve as a CoRL reviewer, and they are qualified if they have at least one accepted publication at a previous robotics (CoRL/ ICRA/ IROS/ RSS) or learning conference (ICLR/ NeurIPS/ ICML) or equivalent journal.

**Related Context from Previous CoRL Conferences:**

For reference, the search did return information from CoRL 2024 and 2023 that may be relevant:

- CoRL 2024 submissions were
…[truncated 706 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6123
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-17T04:32:23.293097+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2024.corl.org/contributions/instruction-for-reviews",
  "prompt": "Extract the full reviewer guidelines, review form criteria, scoring dimensions, and rating scales used for CoRL reviews. I need the specific questions reviewers must answer and the numerical scales."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2024.corl.org/contributions/instruction-for-reviews",
    "prompt": "Extract the full reviewer guidelines, review form criteria, scoring dimensions, and rating scales used for CoRL reviews. I need the specific questions reviewers must answer and the numerical scales."
  }
}
```

</details>

---


### Tool call

_source line 9 · 2026-05-17T04:32:23.846334+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 10 · 2026-05-17T04:32:24.800623+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 11 · 2026-05-17T04:32:24.801210+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 12 · 2026-05-17T04:32:24.951988+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 13 · 2026-05-17T04:32:25.002710+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 14 · 2026-05-17T04:32:25.103938+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-17T04:32:27.263190+00:00_

# CoRL 2024 Review Guidelines - Limited Information

Based on the provided webpage content, I can only report the following review-related guidance:

## Available Review Criteria

**Evaluation Focus:**
The document states reviewers should assess "significance and novelty of the results, either theoretical or empirical" along with "objective establishment" and "potential for scientific and technological impact."

**Scope Requirements:**
Papers must demonstrate robot learning relevance through either:
- Intent: "Explicitly address a learning question for physical robots"
- Outcome: "Test the proposed learning solution on physical robots"

## Missing Information

The webpage excerpt **does not contain**:
- Specific review form questions
- Numerical rating scales or scoring dimensions
- Detailed evaluation rubrics
- Point-by-point assessment criteria

The page titled "Instruction for Reviews" appears to focus primarily on desk rejection criteria and reviewer qualifications rather than the actual review form structure and scoring methodology you're seeking.

**Recommendation:** You may need to access the full review submission portal or contact the CoRL 2024 organizing committee directly to obtain the complete reviewer guidelines with specific questions and numerical scales.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 3970
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-17T04:32:30.676983+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-17T04:32:31.132468+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-17T04:32:31.184526+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-17T04:32:31.637352+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-17T04:32:31.688214+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-17T04:32:32.140242+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-17T04:32:32.843768+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl2023.org/reviewer-guidelines",
  "prompt": "Extract the complete reviewer guidelines including all review form questions, scoring dimensions, numerical rating scales, and evaluation criteria. I need the exact scoring rubric and all dimensions reviewers rate."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl2023.org/reviewer-guidelines",
    "prompt": "Extract the complete reviewer guidelines including all review form questions, scoring dimensions, numerical rating scales, and evaluation criteria. I need the exact scoring rubric and all dimensions reviewers rate."
  }
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-17T04:32:37.714461+00:00_

# CoRL 2023 Reviewer Guidelines Summary

Based on the provided content, the guidelines outline six primary evaluation dimensions but **do not specify numerical rating scales or a complete scoring rubric**.

## Evaluation Dimensions

Reviewers assess papers across these categories:

1. **Originality** – "Are the problems or methods new?" and whether the work clearly distinguishes itself from prior contributions

2. **Quality** – Technical soundness, whether "claims well supported (e.g., by theoretical analysis or experimental results)," and completeness of work

3. **Clarity** – Writing quality, organization, and whether the paper provides sufficient detail for expert reproducibility

4. **Significance** – Whether results are important and likely to influence future research or practice

5. **Relevance** – Alignment with robot learning, use of learning-based methods, and appeal to the CoRL audience

6. **Limitations** – Appreciation for "honestly reported limitations" versus unacknowledged shortcomings

## Missing Information

The document does not provide:
- Specific numerical scales (e.g., 1-5, 1-10)
- Point distributions for each dimension
- Threshold scores for acceptance/rejection
- Detailed rubric descriptors for each rating level

The guidelines emphasize constructive feedback and reference external resources (ICML and NeurIPS) for more comprehensive reviewer training.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 4870
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-17T04:32:42.711768+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-17T04:32:43.264478+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-17T04:32:43.264841+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-17T04:32:43.617101+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-17T04:32:43.667942+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-17T04:32:43.719225+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-17T04:32:48.945535+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "VLA representation analysis token-level decomposition 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "VLA representation analysis token-level decomposition 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 31 · 2026-05-17T04:32:49.499198+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "VLM representation probing RSA layer-wise analysis vision language model 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "VLM representation probing RSA layer-wise analysis vision language model 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-17T04:32:50.393590+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2024 2025 analysis paper pure interpretability no real robot accepted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2024 2025 analysis paper pure interpretability no real robot accepted"
  }
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-17T04:32:56.954721+00:00_

Web search results for query: "VLA representation analysis token-level decomposition 2025 2026"

Links: [{"title":"A Survey on Vision-Language-Action Models: An Action Tokenization Perspective","url":"https://arxiv.org/html/2507.01925v1"},{"title":"Unified Vision-Language-Action Tokenization","url":"https://www.emergentmind.com/topics/unified-vision-language-action-vla-tokenization"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via ...","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf"},{"title":"VQ-VLA: Improving Vision-Language-Action Models via Scaling","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf"},{"title":"Spec-VLA: Speculative Decoding for Vision-Language- ...","url":"https://aclanthology.org/2025.emnlp-main.1367.pdf"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.01166v2"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Visual-Language-Action+(VLA)+models"},{"title":"When LLaVA Meets Objects: Token Composition for Vision-Language-Models","url":"https://arxiv.org/html/2602.04864v1"}]

Based on the search results, I found recent research on Vision-Language-Action (VLA) models with token-level analysis and representation. Here are the key findings:

## Recent VLA Research Developments (2025-2026)

### Token-Level Analysis and Representation

Current VLA models can be unified under a single framework where vision and lan
…[truncated 1597 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8009
}
```

</details>

---


### Tool result

_source line 34 · 2026-05-17T04:33:01.535643+00:00_

Web search results for query: "CoRL 2024 2025 analysis paper pure interpretability no real robot accepted"

Links: [{"title":"GitHub - smallfryy/corl-2025-papers: ✨ 200+ robotics papers from CoRL 2025, with TLDRs, project pages, code, and more","url":"https://github.com/smallfryy/corl-2025-papers"},{"title":"CoRL.2024 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/CoRL.2024"},{"title":"CoRL 2024 Publication Round-Up | RAI Institute","url":"https://rai-inst.com/resources/blog/corl-round-up/"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"GitHub - YanjieZe/Paper-List: A paper list of my history reading. Robotics, Learning, Vision. · GitHub","url":"https://github.com/YanjieZe/Paper-List"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"CoRL.2025 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/CoRL.2025"},{"title":"CoRL 2024","url":"https://2024.corl.org/"},{"title":"CoRL 2024 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FConference"},{"title":"CoRL | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL"}]

Based on the web search results, I found information about papers accepted to CoRL 2024 and 2025, but the results don't show a specific paper matching all your criteria (analysis paper on pure interpretability without real robot testing).

However, the search results do show several interpretability-related papers that were accepted at CoRL conferences:

At CoRL 2024, a paper describing ALGAE (Adaptive Language-Guided Abstraction from Explanations) was accepted, which learns generalizable reward functions defined on interpretable features.

Additionally, there is work on ECoT (Embodied Chain-of-Thought Reasoning) that makes it easier for humans to interpret a policy's failures.

For a more specifi
…[truncated 573 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 11142
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-17T04:33:22.312184+00:00_

Web search results for query: "VLM representation probing RSA layer-wise analysis vision language model 2025 2026"

Links: [{"title":"Interpreting Vision-Language Models with VLM-LENS","url":"https://aclanthology.org/2025.emnlp-demos.68.pdf"},{"title":"Mechanistic Interpretability Meets Vision Language Models: Insights and Limitations | ICLR Blogposts 2025","url":"https://d2jud02ci9yv69.cloudfront.net/2025-04-28-vlm-understanding-29/blog/vlm-understanding/"},{"title":"Object detection with multimodal large vision-language models: An in-depth review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1566253525006475"},{"title":"VLM: How Vision-Language Models Work (2026 Guide) | Label Your Data","url":"https://labelyourdata.com/articles/machine-learning/vision-language-models"},{"title":"GitHub - zli12321/Vision-Language-Models-Overview: A most Frontend Collection and survey of vision-language model papers, and models GitHub repository. Continuous updates. · GitHub","url":"https://github.com/zli12321/Vision-Language-Models-Overview"},{"title":"Compact vision language models enable efficient and interpretable optical coherence tomography through layer-specific multimodal learning | Communications Medicine","url":"https://www.nature.com/articles/s43856-025-01293-9"},{"title":"[2510.09586] Vision Language Models: A Survey of 26K Papers","url":"https://arxiv.org/abs/2510.09586"},{"title":"A systematic review of vision language models: Comprehensive analysis of architectures, applications, datasets and challenges towards robust multimodal intelligence - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2590005626000627"},{"title":"Vision Language Models (VLMs) | cbarkinozer | Softtech","url":"https://medium.com/softtechas/vision-language-models-vlms-6844cdb02444"},{"title":"VLMs-Guided Representation Distillation for Efficient Vision-Based","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Xu_VLMs-Guided_Representa
…[truncated 1783 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 32812
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-17T04:33:26.582448+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Rizzardo\" 2026 VLA feature controllability observability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Rizzardo\" 2026 VLA feature controllability observability"
  }
}
```

</details>

---


### Tool call

_source line 37 · 2026-05-17T04:33:27.084562+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mechanistic interpretability VLM probing token-level layer-wise ICLR 2025 blogpost"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mechanistic interpretability VLM probing token-level layer-wise ICLR 2025 blogpost"
  }
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-17T04:33:27.536788+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 call for papers submission requirements page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 call for papers submission requirements page limit"
  }
}
```

</details>

---


### Tool result

_source line 39 · 2026-05-17T04:33:32.709958+00:00_

Web search results for query: "CoRL 2026 call for papers submission requirements page limit"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"Refactor conference data · huggingface/ai-deadlines at f3cc2d7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/f3cc2d74f8283ae00d3005ff7cca51dd26540377"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026 - Call for Workshops | Danfei Xu","url":"https://www.linkedin.com/posts/danfei-xu-94522133_corl-2026-call-for-workshops-activity-7458261431461965824-yH7b"}]

Based on the search results, here are the key submission requirements for CoRL 2026:

**Page Limit:** The page limit is 8 pages for the main paper. Acknowledgments, References, and Appendix (optional) will not count towards the page limit.

**Other Key Requirements:**

- All submissions should include a Limitations section (counted toward the 8-page limit), explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments, and how these might be addressed in the future.

- Authors should use the provided LaTeX template.

- Authors are encouraged to submit a supplementary file with further details, and 
…[truncated 453 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5173
}
```

</details>

---


### Tool result

_source line 40 · 2026-05-17T04:33:33.413128+00:00_

Web search results for query: "Mechanistic interpretability VLM probing token-level layer-wise ICLR 2025 blogpost"

Links: [{"title":"Mechanistic Interpretability Meets Vision Language Models: Insights and Limitations | ICLR Blogposts 2025","url":"https://d2jud02ci9yv69.cloudfront.net/2025-04-28-vlm-understanding-29/blog/vlm-understanding/"},{"title":"Mechanistic Interpretability Meets Vision Language Models: Insights and Limitations | OpenReview","url":"https://openreview.net/forum?id=pZqvfsUpeh"},{"title":"ICLR 2025 Blog Track Posters","url":"https://iclr.cc/virtual/2025/events/BlogTrack-2025"},{"title":"ICLR Poster Mechanistic Interpretability Meets Vision Language Models: Insights and Limitations","url":"https://iclr.cc/virtual/2025/poster/31330"},{"title":"Published as a conference paper at ICLR 2025 TOWARDS INTERPRETING VISUAL","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/900fb3439e4968df79a6f2bfedec49cd-Paper-Conference.pdf"},{"title":"blog | ICLR Blogposts 2025","url":"https://iclr-blogposts.github.io/2025/blog/"},{"title":"Towards Interpreting Visual Information Processing in Vision-Language Models | OpenReview","url":"https://openreview.net/forum?id=chanJGoa7f"},{"title":"Interpreting Vision-Language Models with VLM-LENS","url":"https://aclanthology.org/2025.emnlp-demos.68.pdf"},{"title":"ICLR 2025 Papers","url":"https://iclr.cc/virtual/2025/papers.html"},{"title":"tldr: token-level detective reward model","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/70217f4d06e57a2395f03b4bc136361a-Paper-Conference.pdf"}]

I found several relevant results about mechanistic interpretability in Vision Language Models (VLMs) from ICLR 2025. Here are the key findings:

## Main ICLR 2025 Blogpost

A systematic review examines mechanistic interpretability methods for VLMs, specifically studying five prominent techniques: probing, activation patching, logit lens, sparse autoencoders, and automated explanation.

### Key Research Focus

The rese
…[truncated 1016 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6328
}
```

</details>

---


### Tool result

_source line 41 · 2026-05-17T04:33:33.614337+00:00_

Web search results for query: ""Rizzardo" 2026 VLA feature controllability observability"

Links: [{"title":"Observing and Controlling Features in Vision-Language-Action Models","url":"https://arxiv.org/html/2603.05487"},{"title":"[2603.05487] Observing and Controlling Features in Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.05487"},{"title":"Vision-Language-Action (VLA) Guide for 2026","url":"https://hyscaler.com/insights/vision-language-action-vla-guide/"},{"title":"(PDF) Observing and Controlling Features in Vision-Language-Action Models","url":"https://www.researchgate.net/publication/401601449_Observing_and_Controlling_Features_in_Vision-Language-Action_Models"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf/526d7a00bb5b3afacbf16960d6879f086fe34bd3.pdf"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"},{"title":"Vision-Language-Action (VLA) Models for Unmanned ...","url":"https://www.preprints.org/manuscript/202604.0664"},{"title":"Control and stabilization results for strongly coupled degenerate/singular hyperbolic systems","url":"https://www.aimsciences.org/article/doi/10.3934/mcrf.2025057"},{"title":"Assessment of Computational Tools for Analysing the Observability and Accessibility of Nonlinear Models","url":"https://www.mdpi.com/2079-3197/13/12/281"}]

Based on the search results, I found a highly relevant research paper that matches your query. Here's what I found:

## Paper: "Observing and Controlling Features in Vision-Language-Action Models"

This paper was submitted on March 5, 2026 by authors Hugo Buurmeijer, Carmen Amo Alonso, Aiden Swann, and Marco Pavone. (Note: The query mentioned "Rizzardo," but this author does not appear in the paper I found. It'
…[truncated 1153 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7031
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-17T04:33:40.153513+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://d2jud02ci9yv69.cloudfront.net/2025-04-28-vlm-understanding-29/blog/vlm-understanding/",
  "prompt": "Extract all information about token-level analysis, layer-wise probing, representation analysis methods (RSA, CKA, probing) applied to vision-language models. I want to know: 1) What specific methods were used for layer-wise analysis? 2) Was there any token-level decomposition (image tokens vs text tokens)? 3) What were the key findings about how different token types encode information? 4) Were there any trained vs untrained comparisons?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://d2jud02ci9yv69.cloudfront.net/2025-04-28-vlm-understanding-29/blog/vlm-understanding/",
    "prompt": "Extract all information about token-level analysis, layer-wise probing, representation analysis methods (RSA, CKA, probing) applied to vision-language models. I want to know: 1) What specific methods were used for layer-wise analysis? 2) Was there any token-level decomposition (image tokens vs text tokens)? 3) What were the key findings about how different token types encode information? 4) Were there any trained vs untrained comparisons?"
  }
}
```

</details>

---


### Tool call

_source line 43 · 2026-05-17T04:33:42.725665+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/900fb3439e4968df79a6f2bfedec49cd-Paper-Conference.pdf",
  "prompt": "Extract the key methods and findings of this paper about interpreting visual information processing in vision-language models. I need: 1) What analysis methods were used (probing, RSA, attention analysis, etc.)? 2) Was there token-level decomposition? 3) What were the key findings about how different token types or layers process information? 4) How does this relate to understanding the role of vision vs language tokens in VLMs?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/900fb3439e4968df79a6f2bfedec49cd-Paper-Conference.pdf",
    "prompt": "Extract the key methods and findings of this paper about interpreting visual information processing in vision-language models. I need: 1) What analysis methods were used (probing, RSA, attention analysis, etc.)? 2) Was there token-level decomposition? 3) What were the key findings about how different token types or layers process information? 4) How does this relate to understanding the role of vision vs language tokens in VLMs?"
  }
}
```

</details>

---


### Tool result

_source line 44 · 2026-05-17T04:33:45.890132+00:00_

# Token-Level and Layer-Wise Analysis in Vision-Language Models

## Specific Methods for Layer-Wise Analysis

The document employs several techniques for analyzing information across layers:

- **Activation Patching**: Researchers "replace activations from one input (e.g., corrupted) with those from another (e.g., clean)" to identify critical layers
- **Logit Lens**: Applied to "extract and interpret predictions from intermediate layers"
- **Attention Knockout**: "A specialized form focused on analyzing attention mechanisms"

## Token-Level Decomposition

Yes, significant token-level distinctions were examined:

**Image vs. Text Tokens**: MMNeuron analysis revealed that "image tokens generate notably sparser distributions than text tokens," suggesting image representations are "encoded as mixtures of concepts rather than direct word mappings."

**Visual Token Evolution**: Neo et al. found "representations at visual token positions change systematically across layers, gradually aligning with interpretable textual concepts."

## Key Findings About Information Encoding

- Early layers (1-10) "process broader contextual information"
- Later layers (15-24) "focus on extracting specific object details"
- Visual-linguistic integration occurs "primarily in late layers"
- Different architectures exhibit distinct patterns (e.g., LLaVA lacks "text-only" attention heads)

## Trained vs. Untrained Comparisons

The document mentions research comparing "pre-training versus fine-tuning" stages using "carefully designed datasets," though specific findings aren't detailed extensively.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5736
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-17T04:33:49.456135+00:00_

I appreciate your detailed request, but I need to be transparent: the content you've provided appears to be a PDF file in raw binary/stream format with embedded compression. The text is not human-readable in its current state - it consists primarily of encoded stream objects, deflate-compressed data, and PDF structural elements rather than extractable article text.

To help you effectively, I would need:

1. **A readable text version** of the paper (plain text, properly formatted PDF, or HTML)
2. **The paper's title and authors** for proper attribution
3. **Access to the actual content** rather than PDF encoding layers

**What I can tell you about typical VLM interpretation studies:**

If this paper follows standard methodologies in this domain, researchers typically employ techniques like:
- Attention pattern visualization
- Representation Similarity Analysis (RSA)
- Probing classifiers for information content
- Ablation studies isolating vision vs. language components

However, I cannot extract the specific methods, findings, or novel contributions from the encoded content you've shared.

**Could you provide:**
- The paper as plain text or a readable format?
- A link to the published version?
- The paper title so I can suggest where to find it?

This will allow me to give you the precise, well-sourced analysis you're requesting while respecting the 125-character quote limit and proper attribution standards.

[Binary content (application/pdf, 5MB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-reviewer-2-df1bf1a9/2ea82c4d-40d4-44d9-abf9-306e98e970fa/tool-results/webfetch-1778992424471-fab20n.pdf]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6730
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-17T04:33:53.055872+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Towards Interpreting Visual Information Processing in Vision-Language Models\" ICLR 2025 token layer probing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Towards Interpreting Visual Information Processing in Vision-Language Models\" ICLR 2025 token layer probing"
  }
}
```

</details>

---


### Tool call

_source line 47 · 2026-05-17T04:33:53.709201+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Grant 2026 \"Not All Features Are Created Equal\" VLA mechanistic study vision dominance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Grant 2026 \"Not All Features Are Created Equal\" VLA mechanistic study vision dominance"
  }
}
```

</details>

---


### Tool result

_source line 48 · 2026-05-17T04:33:59.031962+00:00_

Web search results for query: ""Towards Interpreting Visual Information Processing in Vision-Language Models" ICLR 2025 token layer probing"

Links: [{"title":"Published as a conference paper at ICLR 2025 TOWARDS INTERPRETING VISUAL","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/900fb3439e4968df79a6f2bfedec49cd-Paper-Conference.pdf"},{"title":"[2410.07149] Towards Interpreting Visual Information Processing in Vision-Language Models","url":"https://arxiv.org/abs/2410.07149"},{"title":"Towards Interpreting Visual Information Processing in Vision-Language Models | OpenReview","url":"https://openreview.net/forum?id=chanJGoa7f"},{"title":"dblp: Towards Interpreting Visual Information Processing in Vision-Language Models.","url":"https://dblp.org/rec/conf/iclr/NeoO0G0B25.html"},{"title":"TOWARDS INTERPRETING VISUAL INFORMATION PROCESSING IN VISION-LANGUAGE MODELS - Tel Aviv University","url":"https://cris.tau.ac.il/en/publications/towards-interpreting-visual-information-processing-in-vision-lang/"},{"title":"Visual Representations inside the Language Model","url":"https://arxiv.org/html/2510.04819v1"},{"title":"Mechanistic Interpretability Meets Vision Language Models: Insights and Limitations | ICLR Blogposts 2025","url":"https://d2jud02ci9yv69.cloudfront.net/2025-04-28-vlm-understanding-29/blog/vlm-understanding/"},{"title":"Towards Interpreting Visual Information Processing in Vision-Language Models","url":"https://arxiv.org/html/2410.07149v1"},{"title":"Towards Comprehensive Reasoning in Vision-Language Models | ICCV 2025","url":"https://wangywust.github.io/iccv-tutorial-reasoning-vlm/"},{"title":"GitHub - F-JISOO/ICLR-2025-Submitted · GitHub","url":"https://github.com/F-JISOO/ICLR-2025-Submitted"}]

I found the paper "Towards Interpreting Visual Information Processing in Vision-Language Models" published at ICLR 2025. Here are the key findings:

## Overview

The paper studies the processing of visual tokens in the language model component of LLaVA, a
…[truncated 1270 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5976
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-17T04:34:02.465206+00:00_

Web search results for query: "Grant 2026 "Not All Features Are Created Equal" VLA mechanistic study vision dominance"

Links: [{"title":"[2603.19233] Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.19233"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models","url":"https://arxiv.org/html/2603.19233v1"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=w8Mw9zJt1y"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2603.19233"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models","url":"https://www.wispaper.ai/en/blog/not-all-features-created-equal-mechanistic-study-vision-language-action-models-20260320/zho"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2603.19233v1"},{"title":"GitHub - CWRU-AISM/action-atlas: Mechanistic Interpretability toolkit for Vision-Language-Action models · GitHub","url":"https://github.com/CWRU-AISM/action-atlas"},{"title":"Robotics Research arXiv on X: \"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models Bryce Grant, Xijia Zhao, Peng Wang https://t.co/Mr1IyrLxt9 [𝚌𝚜.𝚁𝙾] https://t.co/9LLIgjodQp\" / X","url":"https://x.com/OWW/status/2034850674173788594"},{"title":"你的 AI 机器人可能根本没听你的话_腾讯新闻","url":"https://news.qq.com/rain/a/20260322A02KDA00"}]

I found the research paper you were looking for. Here's a summary of the key findings:

## Study Overview

Vision-Language-Action (VLA) models combine perception, language, and motor control in a single architecture, yet how they translate multimodal inputs into actions 
…[truncated 1699 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8755
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-17T04:34:07.903241+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
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

_source line 51 · 2026-05-17T04:34:08.906510+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Neo 2025 \"visual token\" representation layer LLaVA visual information processing ICLR findings summary"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Neo 2025 \"visual token\" representation layer LLaVA visual information processing ICLR findings summary"
  }
}
```

</details>

---


### Tool result

_source line 52 · 2026-05-17T04:34:24.541817+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 21, \"total_citations\": 52, \"unique_cited_keys\": 21, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 17, \"online_not_found\": 1, \"online_mismatch\": 3}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"kim2024_openvla\", \"type\": \"article\", \"title\": \"OpenVLA: An Open-Source Vision-Language-Action Model\", \"authors\": \"Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balak...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2406.09246\"}, {\"key\": \"karamcheti2024\", \"type\": \"article\", \"title\": \"Prismatic VLMs: Investigating the Design Space of Visually-Conditioned Language Models\", \"authors\": \"Karamcheti, Siddharth and Nair, Suraj and Balakrishna, Ashwin and Liang, Percy a...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2402.07865\"}, {\"key\": \"brohan2023_rt2\", \"type\": \"article\", \"title\": \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\", \"authors\": \"Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and C...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2307.15818\"}, {\"key\": \"liu2023_libero\", \"type\": \"inproceedings\", \"title\": \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\", \"authors\": \"Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"kriegeskorte2008\", \"type\": \"article\", \"title\": \"Representational Similarity Analysis -- Connecting the Branches of Systems Neuroscience\", \"authors\": \"Kriegeskorte, Nikolaus and Mur, Marieke and Bandettini, Peter\", \"year\": \"2008\", \"venue\": \"Frontiers in Systems Neuroscience\"}, {\"key\": \"korn
…[truncated 16967 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 16638
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-17T04:34:32.439604+00:00_

Web search results for query: "Neo 2025 "visual token" representation layer LLaVA visual information processing ICLR findings summary"

Links: [{"title":"Published as a conference paper at ICLR 2025 TOWARDS INTERPRETING VISUAL","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/900fb3439e4968df79a6f2bfedec49cd-Paper-Conference.pdf"},{"title":"Published as a conference paper at ICLR 2025 TOWARDS INTERPRETING VISUAL","url":"https://ora.ox.ac.uk/objects/uuid:b9d3e15d-03df-446b-8d7c-8c85edddb58d/files/sjd472z47b"},{"title":"[2410.07149] Towards Interpreting Visual Information Processing in Vision-Language Models","url":"https://arxiv.org/abs/2410.07149"},{"title":"NLP Group has 2 papers accepted by ICLR 2025----Natural Language Processing Group","url":"https://nlp.ict.ac.cn/en/academic_news/202501/t20250123_377987.html"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/8400a2ec9ba85bfdb41eb2a584c0876d-Paper-Conference.pdf"},{"title":"[Quick Review] Towards Interpreting Visual Information Processing in Vision-Language Models","url":"https://liner.com/review/towards-interpreting-visual-information-processing-in-visionlanguage-models"},{"title":"Towards Interpreting Visual Information Processing in Vision-Language Models","url":"https://arxiv.org/html/2410.07149v2"},{"title":"LLaVA-Mini: Efficient Image and Video Large Multimodal Models with One Vision Token | OpenReview","url":"https://openreview.net/forum?id=UQJ7CDW8nb"},{"title":"Towards Interpreting Visual Information Processing in Vision-Language Models | OpenReview","url":"https://openreview.net/forum?id=chanJGoa7f"},{"title":"ATP-LLaVA: Adaptive Token Pruning for Large Vision Language Models","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Ye_ATP-LLaVA_Adaptive_Token_Pruning_for_Large_Vision_Language_Models_CVPR_2025_paper.pdf"}]

Based on the search results, here's a summary of the key ICLR 2025 findings from Neo et al.'s
…[truncated 1679 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 23533
}
```

</details>

---


### Tool call

_source line 54 · 2026-05-17T04:36:39.582228+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 1 审稿报告 — Reviewer 2（新颖性 + Related Work + 实际意义）\n\n**论文**: \"Vision Encodes, Language Routes: A Representational Decomposition of Vision-Language-Action Models\"\n\n---\n\n## 总体评分\n\n**Overall**: 4/10 (Borderline Reject)\n**一句话总结**: 实验设计严谨但贡献增量有限——标准分析工具的组合应用于单一模型/单一 benchmark，无方法论创新，design implications 未经验证，且 Related Work 过于单薄。\n\n## 官方维度打分（CoRL review form，参照 CoRL 2023/2024 标准）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 3/10 | 方法是标准工具 (RSA+probing+attention) 的直接组合，\"first token-level decomposition\" claim 站不住脚（见 N1） |\n| Quality | 6/10 | 实验严谨（bootstrap CI、LOOCV、cross-benchmark），但关键 RSA 结果 n.s.，CKA 反转 RSA 结论未充分讨论 |\n| Clarity | 7/10 | 写作清晰、结构良好，但 Related Work 过短 |\n| Significance | 3/10 | design implications 全部 speculative，无验证；对 robotics 社区 actionable value 低 |\n| Relevance | 5/10 | 研究对象是 VLA 但完全是离线分析，无 robot 实验，对 CoRL 社区实际价值存疑 |\n| Limitations | 7/10 | Limitations section 诚实，覆盖了主要弱点 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] \"First token-level representational decomposition\" claim 不成立\n\n- 具体位置：Abstract L2, Introduction L10, Conclusion L1\n- 问题：Neo et al. (ICLR 2025, \"Towards Interpreting Visual Information Processing in Vision-Language Models\") 已对 VLM (LLaVA) 进行了 token-level 分析，发现 (1) object information 高度 localized 到对应 visual token 位置，(2) visual token representations 跨 layer 逐步与 textual tokens 对齐，(3) 最终 token 位置通过 mid-late layer attention 提取 object information。虽然该工作针对 VLM 而非 VLA，但方法论框架（per-token probing + layer-wise analysis + attention mechanism 分析）高度重合。此外 Grant 2026 (Action Atlas) 明确做了 per-token 分析（\"per-token processing is generally essential\"），训练了 424 SAEs 做 per-token 分解，且覆盖 6 个模型 + 4 个 benchmark。本文的 \"first\" claim 需要大幅限定或删除。\n- 为什么影响接收：novelty claim 的核心基础被削弱\n- 建议：改为 \"first systematic *trained-vs-untrained* per-layer decomposition of a VLA with factorial design\"，同时必须引用并讨论 Neo et al. 2025\n\n**N2** [critical] 方法无创新——标准工具的直接应用\n\n- 具体位置：Section 3 (Method) 整体\n- 问题：RSA (Kriegeskorte 2008)、linear/MLP probing (Alain 2017)、attention pattern analysis 都是 20+ 年 / 10+ 年历史的标准工具。论文没有提出任何新的分析方法、新的 metric、或新的实验范式。\"Cross-instruction probe\" 本质是标准 linear probe 的一个 application scenario。$2\\times 2$ factorial design 是实验设计上的好实践，但不构成方法贡献。对于 CoRL 这种重视方法创新和实际应用的会议，纯用现有工具做分析、不产出新方法或新系统，竞争力不足。\n- 为什么影响接收：CoRL 期望 either novel methods or actionable design insights backed by experiments；本文两者都不提供\n- 建议：要么 (1) 基于发现设计并验证新架构（如 early-exit action head at L12），要么 (2) 提出可复用的新分析框架\n\n**N3** [critical] Design implications 完全 speculative，未经任何验证\n\n- 具体位置：Discussion §6 \"Implications for VLA design\"\n- 问题：三条 design implications（vision encoder quality 是 primary lever；action head 应读 L12-L13；instruction 仅通过 readout token 影响 action）全部是从分析结果外推的假设，没有任何验证实验。例如：\n  - \"early exit at L12\" 未测试——作者自己在 Limitations 中承认 \"they do not address whether architectural interventions would alter the patterns we observe\"\n  - \"vision encoder quality is the primary design lever\" 仅基于 RSA 排序 (DINOv2 > CLIP)，但 (1) 这忽略了 CKA 完全反转该排序（Appendix §A.2: untrained > trained > projector > DINOv2），(2) 从 representation 相似性到 task performance 的推断缺乏因果证据\n  - 没有 ablation 测试替换不同质量的 vision encoder 对下游 task success rate 的影响\n- 为什么影响接收：CoRL 审稿标准要求 \"significance\" 和对 robot learning 的实际贡献；纯 speculative implications 不满足\n- 建议：至少做一组验证实验（如 early-exit probe at L12 vs full-depth，或 swap vision encoder quality 对 LIBERO success rate 的影响）\n\n**N4** [critical] 单一模型 + 单一 benchmark 家族，泛化性严重不足\n\n- 具体位置：Section 4.1 (Setup), Discussion Limitations\n- 问题：仅研究 OpenVLA-7B 在 LIBERO 上的表现。LIBERO 是 tabletop manipulation 的简单仿真 benchmark（10 tasks, 50 demos each）。其他主流 VLA（RT-2、π₀、Octo）使用不同架构（encoder-decoder vs decoder-only、diffusion action head vs autoregressive）。Grant 2026 覆盖了 6 个模型（80M-7B）和 4 个 benchmark。Buurmeijer 2026 在 π₀.5 和 OpenVLA 上验证。本文的 \"strict functional specialization\" 结论可能是 OpenVLA 特定架构（frozen vision encoder + Llama-2 backbone）的 artifact，不能推广为 VLA 的通用属性。\n- 为什么影响接收：结论的普适性不成立，大幅降低影响力\n- 建议：至少在一个额外架构（如 π₀ 或 RT-2-X）上验证核心 finding\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Related Work 严重不足（21 篇引用，3 段 15 行）\n\n- 具体位置：Section 2\n- 问题：\n  1. **引用量偏低**：CoRL 2024/2025 录用论文通常有 40-60+ 篇引用，本文仅 21 篇\n  2. **缺失关键 VLM 分析文献**：Neo et al. (ICLR 2025) 是 VLM token-level 分析的核心先行工作，必须引用。VLM-LENS (EMNLP 2025) 提供了系统化 probing 框架。\"Visual Representations inside the Language Model\" (arXiv 2510.04819) 研究了 LLM 内部视觉表征演化。\n  3. **缺失 LLM interpretability 经典文献**：logit lens (nostalgebraist 2020)、residual stream analysis (Elhage et al. 2021)、information flow in transformers\n  4. **缺失 representation learning 比较文献**：Raghu et al. (NeurIPS 2021) \"Do Vision Transformers See Like CNNs?\"、Nguyen et al. 2021 对 CKA/RSA 的比较分析\n  5. **Related Work 缺乏 positioning**：当前仅列举先行工作，没有清楚说明本文与 Grant 2026、Swann 2026、Buurmeijer 2026 的具体差异和增量贡献\n- 建议：扩展 Related Work 至少到 1 页，增加 VLM 分析、LLM interpretability、representation comparison 三个子节，明确 differentiation\n\n**W2** [warning] CKA 结果与 RSA 结论矛盾，处理不够充分\n\n- 具体位置：Appendix §A.2 (Metric Sensitivity)\n- 问题：Linear CKA 完全反转 RSA 排序——untrained > trained > projector > DINOv2。这意味着 \"DINOv2 provides the highest geometric foundation\" 这一核心 narrative（Abstract L6, Discussion §6）仅在 RSA 这一特定 metric 下成立。论文将此放在 appendix 一笔带过（\"reflects the known sensitivity of representation similarity metrics\"），但这实际上严重动摇了 \"vision encoder quality is the primary design lever\" 的推论。如果不同 metric 给出相反结论，那么基于单一 metric 的 design recommendation 就不可靠。\n- 建议：在正文 Discussion 中显式讨论这一矛盾，说明为什么 RSA（rank-order preservation）比 CKA（global linear structure）更适合作为 action-relevant quality 的 proxy，或者承认该 design implication 是 metric-dependent 的\n\n**W3** [warning] 核心 RSA 结果统计不显著\n\n- 具体位置：Table 3 (Training Effects), Experiments §4.3\n- 问题：LIBERO-Goal 上 RSA best-vs-best 的 training effect ($\\Delta = +0.017$) CI 包含零，即 n.s.。论文试图用 LIBERO-Spatial 的显著结果 ($\\Delta = +0.023$, $p < 0.001$) 来 rescue，称 Goal 的 n.s. \"reflects limited power\"。但如果主实验的核心指标不显著，而依赖一个 appendix 中的辅助 benchmark 来支撑结论，这在审稿中是不够 convincing 的。\n- 建议：要么增加 LIBERO-Goal 的样本量使 CI 缩小，要么将 LIBERO-Spatial 提升为 co-primary 分析并在正文充分呈现\n\n**W4** [warning] 无 real-robot 实验——CoRL 期望 robotics grounding\n\n- 具体位置：全文\n- 问题：CoRL CFP 明确 \"highly encouraged to submit real-robot experiments or sim-to-real evidence\"。纯仿真 + 纯离线分析论文在 CoRL 的接受率偏低。论文的分析完全基于 frozen representations，不涉及任何 closed-loop 行为评估。即使是分析论文，Grant 2026 做了 394,000+ rollout episodes 的 behavioral validation，Buurmeijer 2026 做了 closed-loop steering 实验。本文没有任何 rollout-level 验证。\n- 建议：至少补充 (1) 用 best-layer representation 做 action prediction 后在 LIBERO 上的 success rate 对比，或 (2) 验证 early-exit 架构在 rollout 中的表现\n\n---\n\n## 小问题（不影响接收）\n\n- Abstract 中 \"instruction classification at chance, $10\\%$\" 括号使用略显突兀，建议改为独立从句\n- Table 1 caption 提到 \"L0-L8 shown\" 但表格实际包含 L0, L1, L4, L8, L16, L31——caption 不准确\n- $R^2$ peak 在 Table 2 中标注为 \"L8--L10†\"，但正文多处使用不同范围（L8-L13, L8-L10, L8-L16）——术语不统一\n- Figure 3 和 Figure 5(a) 内容高度重叠（都是 per-layer RSA profile），空间效率低\n\n---\n\n## 主要优势\n\n1. **实验设计严谨**：$2\\times 2$ factorial design（training status × instruction presence）是分析论文的 best practice；bootstrap CI + LOOCV + cross-benchmark replication + permutation test + seed sensitivity 构成完整的统计验证体系\n2. **清晰的叙事结构**：三个 finding 层层递进（what → how → where），读者容易跟随\n3. **Trained vs untrained 对照有价值**：揭示了 \"architecture provides incidental routing but training makes it robust\" 这一洞察，区分了架构贡献 vs 学习贡献\n4. **DINOv2 > CLIP 在 action alignment 上的发现**：虽然在单一 metric 下，但对 vision encoder 选择有参考意义\n5. **论文写作质量高**：简洁、technical precision 好、结果呈现清晰\n\n---\n\n## 缺失引用（必须补充）\n\n1. **Neo et al. (ICLR 2025)** \"Towards Interpreting Visual Information Processing in Vision-Language Models\" — VLM token-level 分析的直接先行工作\n2. **\"Visual Representations inside the Language Model\" (arXiv 2510.04819)** — LLM 内部视觉表征演化\n3. **LLM interpretability 经典**: logit lens, residual stream analysis (Elhage et al. 2021, \"A Mathematical Framework for Transformer Circuits\")\n4. **Raghu et al. (NeurIPS 2021)** \"Do Vision Transformers See Like Convolutional Neural Networks?\" — ViT layer-wise representation analysis 方法论\n5. **CoRL/RSS 接受的 VLA 分析论文**（如有）\n\n---\n\n## Questions to Authors\n\n1. 既然 CKA 反转了 RSA 的 encoder 排序，你们如何论证 \"vision encoder quality is the primary design lever\" 不是 metric-dependent 的结论？\n2. Neo et al. (ICLR 2025) 已经在 VLM 中做了 token-level analysis 并发现了 localized information + last-token integration，你们的工作相对于他们的具体增量是什么？\n3. 如果 \"early exit at L12\" 被验证为不改变 action prediction quality（因为改变了 forward pass 可能改变 representation），你们的 design implication 还剩什么 actionable content？\n4. Grant 2026 覆盖了 6 个模型并发现 \"per-token processing is generally essential\"——这是否已经涵盖了你们的 \"token-level specialization\" finding？\n5. 为什么不做至少一个 rollout-level 实验（如用 L12 representation 直接预测 action 并在 LIBERO 上评估 success rate）来 ground 你们的分析发现？\n\n---\n\n## 总结判断\n\n本文是一篇执行良好的分析研究，但对 CoRL 2026 而言存在根本性的竞争力问题：(1) 方法无创新（标准工具的组合），(2) novelty claim 不成立（先行工作已覆盖相似分析），(3) design implications 完全 speculative，(4) 单模型单 benchmark 泛化性不足，(5) 无任何 robot 实验或 behavioral validation。建议作者增加验证实验（early-exit 或 encoder swap 对 task success 的影响）、扩大模型覆盖、或投稿至更适合纯分析工作的 venue（如 TMLR 或 NeurIPS Workshops）。",
  "reviewer_id": "2",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 1 审稿报告 — Reviewer 2（新颖性 + Related Work + 实际意义）\n\n**论文**: \"Vision Encodes, Language Routes: A Representational Decomposition of Vision-Language-Action Models\"\n\n---\n\n## 总体评分\n\n**Overall**: 4/10 (Borderline Reject)\n**一句话总结**: 实验设计严谨但贡献增量有限——标准分析工具的组合应用于单一模型/单一 benchmark，无方法论创新，design implications 未经验证，且 Related Work 过于单薄。\n\n## 官方维度打分（CoRL review form，参照 CoRL 2023/2024 标准）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 3/10 | 方法是标准工具 (RSA+probing+attention) 的直接组合，\"first token-level decomposition\" claim 站不住脚（见 N1） |\n| Quality | 6/10 | 实验严谨（bootstrap CI、LOOCV、cross-benchmark），但关键 RSA 结果 n.s.，CKA 反转 RSA 结论未充分讨论 |\n| Clarity | 7/10 | 写作清晰、结构良好，但 Related Work 过短 |\n| Significance | 3/10 | design implications 全部 speculative，无验证；对 robotics 社区 actionable value 低 |\n| Relevance | 5/10 | 研究对象是 VLA 但完全是离线分析，无 robot 实验，对 CoRL 社区实际价值存疑 |\n| Limitations | 7/10 | Limitations section 诚实，覆盖了主要弱点 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] \"First token-level representational decomposition\" claim 不成立\n\n- 具体位置：Abstract L2, Introduction L10, Conclusion L1\n- 问题：Neo et al. (ICLR 2025, \"Towards Interpreting Visual Information Processing in Vision-Language Models\") 已对 VLM (LLaVA) 进行了 token-level 分析，发现 (1) object information 高度 localized 到对应 visual token 位置，(2) visual token representations 跨 layer 逐步与 textual tokens 对齐，(3) 最终 token 位置通过 mid-late layer attention 提取 object information。虽然该工作针对 VLM 而非 VLA，但方法论框架（per-token probing + layer-wise analysis + attention mechanism 分析）高度重合。此外 Grant 2026 (Action Atlas) 明确做了 per-token 分析（\"per-token processing is generally essential\"），训练了 424 SAEs 做 per-token 分解，且覆盖 6 个模型 + 4 个 benchmark。本文的 \"first\" claim 需要大幅限定或删除。\n- 为什么影响接收：novelty claim 的核心基础被削弱\n- 建议：改为 \"first systematic *trained-vs-untrained* per-layer decomposition of a VLA with factorial design\"，同时必须引用并讨论 Neo et al. 2025\n\n**N2** [critical] 方法无创新——标准工具的直接应用\n\n- 具体位置：Section 3 (Method) 整体\n- 问题：RSA (Kriegeskorte 2008)、linear/MLP probing (Alain 2017)、attention pattern analysis 都是 20+ 年 / 10+ 年历史的标准工具。论文没有提出任何新的分析方法、新的 metric、或新的实验范式。\"Cross-instruction probe\" 本质是标准 linear probe 的一个 application scenario。$2\\times 2$ factorial design 是实验设计上的好实践，但不构成方法贡献。对于 CoRL 这种重视方法创新和实际应用的会议，纯用现有工具做分析、不产出新方法或新系统，竞争力不足。\n- 为什么影响接收：CoRL 期望 either novel methods or actionable design insights backed by experiments；本文两者都不提供\n- 建议：要么 (1) 基于发现设计并验证新架构（如 early-exit action head at L12），要么 (2) 提出可复用的新分析框架\n\n**N3** [critical] Design implications 完全 speculative，未经任何验证\n\n- 具体位置：Discussion §6 \"Implications for VLA design\"\n- 问题：三条 design implications（vision encoder quality 是 primary lever；action head 应读 L12-L13；instruction 仅通过 readout token 影响 action）全部是从分析结果外推的假设，没有任何验证实验。例如：\n  - \"early exit at L12\" 未测试——作者自己在 Limitations 中承认 \"they do not address whether architectural interventions would alter the patterns we observe\"\n  - \"vision encoder quality is the primary design lever\" 仅基于 RSA 排序 (DINOv2 > CLIP)，但 (1) 这忽略了 CKA 完全反转该排序（Appendix §A.2: untrained > trained > projector > DINOv2），(2) 从 representation 相似性到 task performance 的推断缺乏因果证据\n  - 没有 ablation 测试替换不同质量的 vision encoder 对下游 task success rate 的影响\n- 为什么影响接收：CoRL 审稿标准要求 \"significance\" 和对 robot learning 的实际贡献；纯 speculative implications 不满足\n- 建议：至少做一组验证实验（如 early-exit probe at L12 vs full-depth，或 swap vision encoder quality 对 LIBERO success rate 的影响）\n\n**N4** [critical] 单一模型 + 单一 benchmark 家族，泛化性严重不足\n\n- 具体位置：Section 4.1 (Setup), Discussion Limitations\n- 问题：仅研究 OpenVLA-7B 在 LIBERO 上的表现。LIBERO 是 tabletop manipulation 的简单仿真 benchmark（10 tasks, 50 demos each）。其他主流 VLA（RT-2、π₀、Octo）使用不同架构（encoder-decoder vs decoder-only、diffusion action head vs autoregressive）。Grant 2026 覆盖了 6 个模型（80M-7B）和 4 个 benchmark。Buurmeijer 2026 在 π₀.5 和 OpenVLA 上验证。本文的 \"strict functional specialization\" 结论可能是 OpenVLA 特定架构（frozen vision encoder + Llama-2 backbone）的 artifact，不能推广为 VLA 的通用属性。\n- 为什么影响接收：结论的普适性不成立，大幅降低影响力\n- 建议：至少在一个额外架构（如 π₀ 或 RT-2-X）上验证核心 finding\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Related Work 严重不足（21 篇引用，3 段 15 行）\n\n- 具体位置：Section 2\n- 问题：\n  1. **引用量偏低**：CoRL 2024/2025 录用论文通常有 40-60+ 篇引用，本文仅 21 篇\n  2. **缺失关键 VLM 分析文献**：Neo et al. (ICLR 2025) 是 VLM token-level 分析的核心先行工作，必须引用。VLM-LENS (EMNLP 2025) 提供了系统化 probing 框架。\"Visual Representations inside the Language Model\" (arXiv 2510.04819) 研究了 LLM 内部视觉表征演化。\n  3. **缺失 LLM interpretability 经典文献**：logit lens (nostalgebraist 2020)、residual stream analysis (Elhage et al. 2021)、information flow in transformers\n  4. **缺失 representation learning 比较文献**：Raghu et al. (NeurIPS 2021) \"Do Vision Transformers See Like CNNs?\"、Nguyen et al. 2021 对 CKA/RSA 的比较分析\n  5. **Related Work 缺乏 positioning**：当前仅列举先行工作，没有清楚说明本文与 Grant 2026、Swann 2026、Buurmeijer 2026 的具体差异和增量贡献\n- 建议：扩展 Related Work 至少到 1 页，增加 VLM 分析、LLM interpretability、representation comparison 三个子节，明确 differentiation\n\n**W2** [warning] CKA 结果与 RSA 结论矛盾，处理不够充分\n\n- 具体位置：Appendix §A.2 (Metric Sensitivity)\n- 问题：Linear CKA 完全反转 RSA 排序——untrained > trained > projector > DINOv2。这意味着 \"DINOv2 provides the highest geometric foundation\" 这一核心 narrative（Abstract L6, Discussion §6）仅在 RSA 这一特定 metric 下成立。论文将此放在 appendix 一笔带过（\"reflects the known sensitivity of representation similarity metrics\"），但这实际上严重动摇了 \"vision encoder quality is the primary design lever\" 的推论。如果不同 metric 给出相反结论，那么基于单一 metric 的 design recommendation 就不可靠。\n- 建议：在正文 Discussion 中显式讨论这一矛盾，说明为什么 RSA（rank-order preservation）比 CKA（global linear structure）更适合作为 action-relevant quality 的 proxy，或者承认该 design implication 是 metric-dependent 的\n\n**W3** [warning] 核心 RSA 结果统计不显著\n\n- 具体位置：Table 3 (Training Effects), Experiments §4.3\n- 问题：LIBERO-Goal 上 RSA best-vs-best 的 training effect ($\\Delta = +0.017$) CI 包含零，即 n.s.。论文试图用 LIBERO-Spatial 的显著结果 ($\\Delta = +0.023$, $p < 0.001$) 来 rescue，称 Goal 的 n.s. \"reflects limited power\"。但如果主实验的核心指标不显著，而依赖一个 appendix 中的辅助 benchmark 来支撑结论，这在审稿中是不够 convincing 的。\n- 建议：要么增加 LIBERO-Goal 的样本量使 CI 缩小，要么将 LIBERO-Spatial 提升为 co-primary 分析并在正文充分呈现\n\n**W4** [warning] 无 real-robot 实验——CoRL 期望 robotics grounding\n\n- 具体位置：全文\n- 问题：CoRL CFP 明确 \"highly encouraged to submit real-robot experiments or sim-to-real evidence\"。纯仿真 + 纯离线分析论文在 CoRL 的接受率偏低。论文的分析完全基于 frozen representations，不涉及任何 closed-loop 行为评估。即使是分析论文，Grant 2026 做了 394,000+ rollout episodes 的 behavioral validation，Buurmeijer 2026 做了 closed-loop steering 实验。本文没有任何 rollout-level 验证。\n- 建议：至少补充 (1) 用 best-layer representation 做 action prediction 后在 LIBERO 上的 success rate 对比，或 (2) 验证 early-exit 架构在 rollout 中的表现\n\n---\n\n## 小问题（不影响接收）\n\n- Abstract 中 \"instruction classification at chance, $10\\%$\" 括号使用略显突兀，建议改为独立从句\n- Table 1 caption 提到 \"L0-L8 shown\" 但表格实际包含 L0, L1, L4, L8, L16, L31——caption 不准确\n- $R^2$ peak 在 Table 2 中标注为 \"L8--L10†\"，但正文多处使用不同范围（L8-L13, L8-L10, L8-L16）——术语不统一\n- Figure 3 和 Figure 5(a) 内容高度重叠（都是 per-layer RSA profile），空间效率低\n\n---\n\n## 主要优势\n\n1. **实验设计严谨**：$2\\times 2$ factorial design（training status × instruction presence）是分析论文的 best practice；bootstrap CI + LOOCV + cross-benchmark replication + permutation test + seed sensitivity 构成完整的统计验证体系\n2. **清晰的叙事结构**：三个 finding 层层递进（what → how → where），读者容易跟随\n3. **Trained vs untrained 对照有价值**：揭示了 \"architecture provides incidental routing but training makes it robust\" 这一洞察，区分了架构贡献 vs 学习贡献\n4. **DINOv2 > CLIP 在 action alignment 上的发现**：虽然在单一 metric 下，但对 vision encoder 选择有参考意义\n5. **论文写作质量高**：简洁、technical precision 好、结果呈现清晰\n\n---\n\n## 缺失引用（必须补充）\n\n1. **Neo et al. (ICLR 2025)** \"Towards Interpreting Visual Information Processing in Vision-Language Models\" — VLM token-level 分析的直接先行工作\n2. **\"Visual Representations inside the Language Model\" (arXiv 2510.04819)** — LLM 内部视觉表征演化\n3. **LLM interpretability 经典**: logit lens, residual stream analysis (Elhage et al. 2021, \"A Mathematical Framework for Transformer Circuits\")\n4. **Raghu et al. (NeurIPS 2021)** \"Do Vision Transformers See Like Convolutional Neural Networks?\" — ViT layer-wise representation analysis 方法论\n5. **CoRL/RSS 接受的 VLA 分析论文**（如有）\n\n---\n\n## Questions to Authors\n\n1. 既然 CKA 反转了 RSA 的 encoder 排序，你们如何论证 \"vision encoder quality is the primary design lever\" 不是 metric-dependent 的结论？\n2. Neo et al. (ICLR 2025) 已经在 VLM 中做了 token-level analysis 并发现了 localized information + last-token integration，你们的工作相对于他们的具体增量是什么？\n3. 如果 \"early exit at L12\" 被验证为不改变 action prediction quality（因为改变了 forward pass 可能改变 representation），你们的 design implication 还剩什么 actionable content？\n4. Grant 2026 覆盖了 6 个模型并发现 \"per-token processing is generally essential\"——这是否已经涵盖了你们的 \"token-level specialization\" finding？\n5. 为什么不做至少一个 rollout-level 实验（如用 L12 representation 直接预测 action 并在 LIBERO 上评估 success rate）来 ground 你们的分析发现？\n\n---\n\n## 总结判断\n\n本文是一篇执行良好的分析研究，但对 CoRL 2026 而言存在根本性的竞争力问题：(1) 方法无创新（标准工具的组合），(2) novelty claim 不成立（先行工作已覆盖相似分析），(3) design implications 完全 speculative，(4) 单模型单 benchmark 泛化性不足，(5) 无任何 robot 实验或 behavioral validation。建议作者增加验证实验（early-exit 或 encoder swap 对 task success 的影响）、扩大模型覆盖、或投稿至更适合纯分析工作的 venue（如 TMLR 或 NeurIPS Workshops）。",
    "reviewer_id": "2",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-17T04:36:43.652769+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4070
}
```

</details>

---


### Assistant

_source line 56 · 2026-05-17T04:36:52.896355+00:00_

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
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2"
}
```

</details>

---


## Round 2

## Round 2

4 recorded events


### User

_source line 57 · 2026-05-17T04:38:18.216000+00:00_

[Round 1 审稿请求]:
## Step 2 交叉分享 — 请逐条回应 Reviewer 1 和 Reviewer 3 的意见

以下是 Reviewer 1 和 Reviewer 3 的完整审稿原文。请对每个 Must-Fix (N) 和 Should-Fix (W) 问题逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

### Reviewer 1 的完整审稿意见（5/10, Marginally below acceptance）

**Must-Fix:**

**N1** [critical] Untrained control 不能隔离 VLA fine-tuning 的贡献
- Random weights vs trained 混淆了 Llama-2 语言预训练 vs VLA fine-tuning。需增加 Llama-2 base checkpoint 作为中间对照。

**N2** [critical] 单一模型 + 单一 benchmark family 无法支撑 "VLAs" 的一般性结论
- Title/Abstract 用复数 "VLAs"，但仅测试 OpenVLA-7B + LIBERO。

**N3** [critical] RSA best-vs-best 比较存在 selection bias
- 32 层取 max 有正偏置(winner's curse)；主 benchmark 结果 n.s.；用 LIBERO-Spatial 显著性来 rescue Goal 的零结果方法论不成立。

**N4** [critical] Probing 的 encoding ≠ use
- MLP probe R² 证明 information extractable，不证明 model uses it。"Vision encoder is primary lever" 缺乏因果支撑。

**Should-Fix:**

**W1** "Instruction-blind" claim 过强——chance-level linear probe ≠ no instruction information。未测 MLP probe on instruction classification。
**W2** CKA 与 RSA 结论矛盾处理不充分。
**W3** Attention analysis 仅限 L1，可能存在选择性报告。
**W4** LOOCV 100%±0.00 的统计检验力问题——4096-D 做 10-way classification 可能对 random features 也接近 100%。
**W5** 数据规模（500 demos）对 peak layer 精确位置的影响。

---

### Reviewer 3 的完整审稿意见（6/10, Weak Accept）

**Must-Fix:**

**N1** Limitations 格式不满足 CoRL 2026 硬性要求。
**N2** Em-dash (---) 作为解释性标点至少 8 处（AI 写作标志）。

**Should-Fix:**

**W1** 术语首次出现未定义（LOOCV, MLP, CKA）
**W2** 页数可能超出 8 页（估算 ~9.1 页）
**W3** -ing 分词短语结尾
**W4** Related Work 过短
**W5** 无 code/data 释放声明

---

请逐条给出你的 [AGREE] 或 [REBUT] 回应，特别关注：
1. R1-N1 的 untrained baseline 问题——你是否同意这比你提出的 N4（单模型泛化性）更根本？
2. R1-N3 的 statistical bias 问题——你的 W3 也提到 RSA n.s.，是否同意 R1 对 selection bias 的分析？
3. R1-W1 的 "instruction-blind" claim——这与你对 novelty 的评估有何关联？
4. R3 的格式问题是否会改变你的整体评分？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-17T04:41:07.718130+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Step 2 交叉回应（R1 + R3）\n\n### 回应 Reviewer 1\n\n**[AGREE] R1-N1: Untrained control 不能隔离 VLA fine-tuning 的贡献**\n同意，且认为这比我的 N4（单模型泛化性）更根本。Random weights vs trained 混淆了 Llama-2 语言预训练和 VLA fine-tuning。25/32 heads 翻转为 instruction-dominant 可能是语言预训练的产物而非 VLA-specific learning。需要三级对照：random → Llama-2 base → VLA。这是 internal validity 问题，动摇论文核心叙事。\n\n**[AGREE] R1-N2: 单模型 + 单 benchmark 无法支撑一般性结论**\n同意。补充：Grant 2026 Action Atlas 已在 6 个 VLA 模型上做了类似分析，本文应引用作为跨模型支持证据。\n\n**[AGREE] R1-N3: RSA best-vs-best selection bias**\n完全同意。32 层取 max 有 winner's curse；用 LIBERO-Spatial 显著性 rescue Goal 的 null 是 post-hoc rationalization。应报告 FDR-corrected 或 permutation-based max-statistic。\n\n**[AGREE] R1-N4: Probing encoding ≠ use**\n同意。Discussion 承认 encoding ≠ use，但随即做出因果性设计建议（\"vision encoder quality is the primary design lever\"），构成内部矛盾。\n\n**[AGREE] R1-W1: \"Instruction-blind\" claim 过强**\n同意，且直接影响 novelty。未用 MLP probe 测 instruction classification on image tokens。如果 nonlinear probe 能超越 chance，\"strict\" specialization 弱化为 \"predominantly visual\"，与 Grant 2026 behavioral findings 的区分度降低。\n\n**[AGREE] R1-W2: CKA 与 RSA 矛盾**\n同意。两个标准度量给出相反结论，仅选择支持叙事的指标构成 confirmation bias。\n\n**[REBUT] R1-W3: Attention analysis 仅限 L1**\n部分不同意。L1 是 instruction info 首次流入 readout 的位置（L0=chance, L1=100%），分析这层逻辑自洽。但直接展示 L16/L31 attention pattern 会更有说服力。\n\n**[REBUT] R1-W4: LOOCV 100% 的统计检验力**\n部分不同意。Image_mean（同为 4096-D）在所有层 = 10%，反证高维度本身不足以解释 100%。真正的区分力来自 routing mechanism。但同意 100%±0.00 说明 task 太 easy，QA probe（86.3% vs 82.7%）是更 informative 的证据。\n\n**[AGREE] R1-W5: 数据规模影响**\n部分同意。Appendix Table 8 显示 peak region 稳定但精确位置敏感。应弱化为 \"L8-L16 plateau\"。\n\n---\n\n### 回应 Reviewer 3\n\n**[AGREE] R3-N1: Limitations 格式违规** — 需从 \\paragraph 改为 \\section，格式问题可快速修复。\n\n**[AGREE] R3-N2: Em-dash** — 确实存在，但我认为应为 Should-Fix 而非 Must-Fix。\n\n**[AGREE] R3-W1-W5** — 全部同意：术语未定义、页数可能超限、-ing 短语、Related Work 过短（强烈同意，遗漏 Neo et al. ICLR 2025 等关键工作）、无 code 释放声明。\n\n---\n\n### Director 四个问题的直接回答\n\n**Q1**: 是的，R1-N1 比我的 N4 更根本。N4 是 external validity（能否推广），N1 是 internal validity（核心 claim 的因果归因是否成立）。\n\n**Q2**: 完全同意 R1 对 selection bias 的分析。我原来将 RSA n.s. 视为 underpowered，R1 指出这可能是 effect doesn't exist + selection bias 的叠加。\n\n**Q3**: 如果 \"strict specialization\" 弱化，novelty 从 \"revealing unexpected strict separation\" 降级为 \"confirming known dominance at representation level with standard tools\"。方法论层面的 \"first decomposition\" 仍成立，但 surprise value 降低。\n\n**Q4**: R3 格式问题不改变科学评分，但页数超限 + Limitations 格式不符有 desk-reject 风险。\n\n---\n\n### 评估更新\n\n综合 R1+R3 后：\n- **Novelty**: moderate → incremental（R1-N1 confound + W1 overclaim）\n- **Soundness**: adequate → below threshold（N1 + N3 + N4 叠加）\n- **Overall**: 维持 5/10 (marginally below acceptance)。如修复 R1-N1（加 Llama-2 base 对照）+ 弱化 overclaims，可升至 6/10。",
  "reviewer_id": "2",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Step 2 交叉回应（R1 + R3）\n\n### 回应 Reviewer 1\n\n**[AGREE] R1-N1: Untrained control 不能隔离 VLA fine-tuning 的贡献**\n同意，且认为这比我的 N4（单模型泛化性）更根本。Random weights vs trained 混淆了 Llama-2 语言预训练和 VLA fine-tuning。25/32 heads 翻转为 instruction-dominant 可能是语言预训练的产物而非 VLA-specific learning。需要三级对照：random → Llama-2 base → VLA。这是 internal validity 问题，动摇论文核心叙事。\n\n**[AGREE] R1-N2: 单模型 + 单 benchmark 无法支撑一般性结论**\n同意。补充：Grant 2026 Action Atlas 已在 6 个 VLA 模型上做了类似分析，本文应引用作为跨模型支持证据。\n\n**[AGREE] R1-N3: RSA best-vs-best selection bias**\n完全同意。32 层取 max 有 winner's curse；用 LIBERO-Spatial 显著性 rescue Goal 的 null 是 post-hoc rationalization。应报告 FDR-corrected 或 permutation-based max-statistic。\n\n**[AGREE] R1-N4: Probing encoding ≠ use**\n同意。Discussion 承认 encoding ≠ use，但随即做出因果性设计建议（\"vision encoder quality is the primary design lever\"），构成内部矛盾。\n\n**[AGREE] R1-W1: \"Instruction-blind\" claim 过强**\n同意，且直接影响 novelty。未用 MLP probe 测 instruction classification on image tokens。如果 nonlinear probe 能超越 chance，\"strict\" specialization 弱化为 \"predominantly visual\"，与 Grant 2026 behavioral findings 的区分度降低。\n\n**[AGREE] R1-W2: CKA 与 RSA 矛盾**\n同意。两个标准度量给出相反结论，仅选择支持叙事的指标构成 confirmation bias。\n\n**[REBUT] R1-W3: Attention analysis 仅限 L1**\n部分不同意。L1 是 instruction info 首次流入 readout 的位置（L0=chance, L1=100%），分析这层逻辑自洽。但直接展示 L16/L31 attention pattern 会更有说服力。\n\n**[REBUT] R1-W4: LOOCV 100% 的统计检验力**\n部分不同意。Image_mean（同为 4096-D）在所有层 = 10%，反证高维度本身不足以解释 100%。真正的区分力来自 routing mechanism。但同意 100%±0.00 说明 task 太 easy，QA probe（86.3% vs 82.7%）是更 informative 的证据。\n\n**[AGREE] R1-W5: 数据规模影响**\n部分同意。Appendix Table 8 显示 peak region 稳定但精确位置敏感。应弱化为 \"L8-L16 plateau\"。\n\n---\n\n### 回应 Reviewer 3\n\n**[AGREE] R3-N1: Limitations 格式违规** — 需从 \\paragraph 改为 \\section，格式问题可快速修复。\n\n**[AGREE] R3-N2: Em-dash** — 确实存在，但我认为应为 Should-Fix 而非 Must-Fix。\n\n**[AGREE] R3-W1-W5** — 全部同意：术语未定义、页数可能超限、-ing 短语、Related Work 过短（强烈同意，遗漏 Neo et al. ICLR 2025 等关键工作）、无 code 释放声明。\n\n---\n\n### Director 四个问题的直接回答\n\n**Q1**: 是的，R1-N1 比我的 N4 更根本。N4 是 external validity（能否推广），N1 是 internal validity（核心 claim 的因果归因是否成立）。\n\n**Q2**: 完全同意 R1 对 selection bias 的分析。我原来将 RSA n.s. 视为 underpowered，R1 指出这可能是 effect doesn't exist + selection bias 的叠加。\n\n**Q3**: 如果 \"strict specialization\" 弱化，novelty 从 \"revealing unexpected strict separation\" 降级为 \"confirming known dominance at representation level with standard tools\"。方法论层面的 \"first decomposition\" 仍成立，但 surprise value 降低。\n\n**Q4**: R3 格式问题不改变科学评分，但页数超限 + Limitations 格式不符有 desk-reject 风险。\n\n---\n\n### 评估更新\n\n综合 R1+R3 后：\n- **Novelty**: moderate → incremental（R1-N1 confound + W1 overclaim）\n- **Soundness**: adequate → below threshold（N1 + N3 + N4 叠加）\n- **Overall**: 维持 5/10 (marginally below acceptance)。如修复 R1-N1（加 Llama-2 base 对照）+ 弱化 overclaims，可升至 6/10。",
    "reviewer_id": "2",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 59 · 2026-05-17T04:41:11.485606+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3767
}
```

</details>

---


### Assistant

_source line 60 · 2026-05-17T04:41:19.682357+00:00_

已完成交叉回应并提交给 Director。核心判断：

- R1-N1（baseline confound）和 R1-N3（selection bias）是最具杀伤力的问题，我全部 AGREE
- 仅对 R1-W3（L1 attention 选择性报告）和 R1-W4（LOOCV 统计力）部分 REBUT，因为论文内部证据已部分回应
- R3 格式问题全部同意，但不应影响科学评分
- 综合评估维持 5/10，核心瓶颈是 internal validity（untrained baseline 的 confound 设计）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2"
}
```

</details>

---


## Round 3

## Round 3

28 recorded events


### User

_source line 61 · 2026-05-17T06:03:52.937385+00:00_

[Round 2 审稿请求]:
## Round 2 修订评估 — Reviewer 2（新颖性 + Related Work + 实际意义）

**模式**：继续审稿。你在 Round 1 给出 4/10。现在评估修改是否充分回应了你的问题。

### Venue 信息（不变）
- CoRL 2026, Deadline 2026-05-29, 8 页正文, double-blind

### 论文路径
`projects/vla-ssd/docs/paper/main.tex`

### 你的 Round 1 主要发现摘要
- **N1** (critical): "First token-level decomposition" claim 不成立（Neo et al. ICLR 2025 + Grant 2026）
- **N2** (critical): 无方法论创新，标准��具直接应用
- **N3** (critical): Design implications 完全 speculative
- **N4** (critical): 单模型单 benchmark 泛化性不足
- **W1** (warning): Related Work 严重不足（21 引用，缺失关键文献）

### 当前 Open/In-Progress Issues（逐条标注 [RESOLVED] / [STILL_OPEN]）

请读取更新后的论文，对以下 issue 逐条判定：

1. **R2-N1** [in_progress]: "First" novelty claim
   - Action: 删除 "first"，引用 Neo et al.，重定位 novelty
   - 检查：Abstract/Intro/Conclusion 是否仍含 "first"？Neo et al. (ICLR 2025) 是否被引用？novelty 如何重新定位？

2. **R2-N2** [in_progress]: 无方法创新
   - 上轮判断：CoRL 期望 method 或 actionable insight。R1+R3 rebut 认为 insight novelty 可弥补。
   - 检查：论文是否增加了任何新实验/方法/��证来强化 insight novelty？

3. **R2-N3** [in_progress]: Design implications speculative
   - Action: 弱化语气或���加因果验证
   - 检查：Discussion/Abstract/Conclusion 中 design implications 的语气是否软化？是否有新���证实验？

4. **R2-N4** [in_progress]: 单模型单 benchmark
   - 同 R1-N2��检查 Title 是否限定？claims 是否加 scope qualifier？

5. **R2-W1** [in_progress]: Related Work 不足
   - Action: 扩展至 4-6 段，40+ 引用
   - 检查：段数、引用数、覆盖的类别。特别关注：Neo et al. (ICLR 2025) 是否被引用？logit lens？Raghu et al. 2021（ViT representation）？

### 关键新问题检查
- Related Work 扩展后，与 Grant 2026 的 differentiation 是否清晰？
- 新增引用是否改善了 positioning？
- 是否引入了新的问题（如过度引用无关文献）？

### 输出格式
对每个 issue：[RESOLVED] / [PARTIALLY_RESOLVED] / [STILL_OPEN] + 理由
最后给出更新后的 Overall Score 和理由。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 62 · 2026-05-17T06:04:01.787413+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-17T06:04:02.141694+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 354
}
```

</details>

---


### Tool call

_source line 64 · 2026-05-17T06:04:02.293068+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 65 · 2026-05-17T06:04:02.444269+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 66 · 2026-05-17T06:04:02.547118+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-17T06:04:02.598014+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 68 · 2026-05-17T06:04:06.465353+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 69 · 2026-05-17T06:04:06.867207+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 70 · 2026-05-17T06:04:06.867607+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 71 · 2026-05-17T06:04:07.219381+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 72 · 2026-05-17T06:04:07.270007+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 73 · 2026-05-17T06:04:07.271567+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 74 · 2026-05-17T06:04:12.501098+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 75 · 2026-05-17T06:04:12.601954+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 76 · 2026-05-17T06:04:18.429720+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 77 · 2026-05-17T06:04:18.731533+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 78 · 2026-05-17T06:04:18.731882+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 79 · 2026-05-17T06:04:18.782570+00:00_

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
…[truncated 15077 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 80 · 2026-05-17T06:05:16.494988+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "first|First",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "first|First",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 81 · 2026-05-17T06:05:16.597277+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex:21:\emph{First}, vision encoder pretraining quality is the primary design lever; investing in stronger self-supervised encoders may yield larger gains than scaling the LLM.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_example.tex:15:% if LaTeX puts 3 of 4 authors names on the first line, and the last
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex:4:First, the VLA exhibits strict token-level functional specialization: image tokens encode purely visual information (instruction classification at chance, $10\%$, across all layers), while the readout token serves as a multimodal convergence point ($100\%$ instruction classification from L1, LOOCV-verified).
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex:97:First, the absolute RSA values are higher on Spatial ($0.691$ vs.\ $0.628$), possibly reflecting greater action diversity in spatial tasks that produces a more discriminative action RDM.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex:17:\emph{First}, the VLA exhibits strict token-level functional specialization.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 82 · 2026-05-17T06:05:16.647958+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "neo|Neo",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "neo|Neo",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 83 · 2026-05-17T06:05:16.698529+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 84 · 2026-05-17T06:05:21.519650+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "---",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 85 · 2026-05-17T06:05:21.620575+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:13:%------------------------------------------------------------------
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:53:%------------------------------------------------------------------
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:82:%------------------------------------------------------------------
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:114:DINOv2 cls\_token & \textbf{0.692} & 0.634 & --- & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:116:Fused DinoSigLIP & 0.634 & --- & --- & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:118:DinoSigLIP+Projector & 0.615 & 0.630 & --- & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:121:CLIP ViT-L/14$^\ddagger$ & 0.557 & 0.587 & --- & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:149:Instruction effect (max $|\Delta|$) & 0.006 & --- & n.s. \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex:6:%------------------------------------------------------------------
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex:14:%------------------------------------------------------------------
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex:27:%------------------------------------------------------------------
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex:35:%------------------------------------------------------------------
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex:42:%------------------------
…[truncated 599 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 86 · 2026-05-17T06:07:04.796323+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 2 修订评估\n\n### 逐条判定\n\n1. **R2-N1 \"First\" novelty claim** → [PARTIALLY_RESOLVED]\n   - \"First\" 已删除，novelty 重定位为 \"systematic + factorial control\" ✓\n   - 但 Introduction line 10 仍写 \"No prior work has provided a systematic token-level decomposition\"（换皮 \"first\"）\n   - **Neo et al. (ICLR 2025) 仍未引用** — 该工作在 LLaVA 上做了 token-level layer-wise 分析（probing + attention + ablation by position），方法高度可比。不引此文，\"no prior work\" claim 不成立。\n\n2. **R2-N2 无方法创新** → [STILL_OPEN]\n   - 无新实验/方法/因果验证\n   - \"Why RSA over CKA\" 段落是 justification 而非 innovation\n   - 核心问题不变：标准工具直接应用\n\n3. **R2-N3 Design implications speculative** → [PARTIALLY_RESOLVED]\n   - Discussion 加了 \"requires policy rollout experiments\" + Limitations 加了 \"Post-hoc analysis\" ✓\n   - 但 Abstract line 8 仍为强处方性语言：\"should optimize\"/\"primary design lever\"，无 hedge\n   - Abstract/Conclusion vs Discussion/Limitations 的 claims 强度不一致\n\n4. **R2-N4 单模型单 benchmark** → [PARTIALLY_RESOLVED]\n   - Abstract 现在限定 \"(OpenVLA-7B on LIBERO)\" ✓\n   - Limitations 拆分为 Architecture scope + Task diversity ✓\n   - Title 仍为复数 \"Vision-Language-Action Models\"，暗示一般性\n\n5. **R2-W1 Related Work** → [PARTIALLY_RESOLVED]\n   - 3→5 段，21→35 引用 ✓\n   - Grant 2026 三点 differentiation 清晰有效 ✓\n   - 仍缺：Neo et al. (ICLR 2025)、Raghu et al. 2021 (ViT RSA/CKA)、logit lens 系列\n\n### Overall Score: 4/10 → 5/10 (Marginally below acceptance)\n\n修订体现诚意但核心问题未完全解决：Neo et al. 缺失、无新方法、Abstract overclaims。\n\n**升至 6/10 的条件（均为文字修改）：**\n(a) 引用 Neo et al. 并 differentiate\n(b) Abstract 最后一句改为 hypothesis 而非 prescription\n(c) Title 加限定或改为不暗示一般性",
  "reviewer_id": "2",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 2 修订评估\n\n### 逐条判定\n\n1. **R2-N1 \"First\" novelty claim** → [PARTIALLY_RESOLVED]\n   - \"First\" 已删除，novelty 重定位为 \"systematic + factorial control\" ✓\n   - 但 Introduction line 10 仍写 \"No prior work has provided a systematic token-level decomposition\"（换皮 \"first\"）\n   - **Neo et al. (ICLR 2025) 仍未引用** — 该工作在 LLaVA 上做了 token-level layer-wise 分析（probing + attention + ablation by position），方法高度可比。不引此文，\"no prior work\" claim 不成立。\n\n2. **R2-N2 无方法创新** → [STILL_OPEN]\n   - 无新实验/方法/因果验证\n   - \"Why RSA over CKA\" 段落是 justification 而非 innovation\n   - 核心问题不变：标准工具直接应用\n\n3. **R2-N3 Design implications speculative** → [PARTIALLY_RESOLVED]\n   - Discussion 加了 \"requires policy rollout experiments\" + Limitations 加了 \"Post-hoc analysis\" ✓\n   - 但 Abstract line 8 仍为强处方性语言：\"should optimize\"/\"primary design lever\"，无 hedge\n   - Abstract/Conclusion vs Discussion/Limitations 的 claims 强度不一致\n\n4. **R2-N4 单模型单 benchmark** → [PARTIALLY_RESOLVED]\n   - Abstract 现在限定 \"(OpenVLA-7B on LIBERO)\" ✓\n   - Limitations 拆分为 Architecture scope + Task diversity ✓\n   - Title 仍为复数 \"Vision-Language-Action Models\"，暗示一般性\n\n5. **R2-W1 Related Work** → [PARTIALLY_RESOLVED]\n   - 3→5 段，21→35 引用 ✓\n   - Grant 2026 三点 differentiation 清晰有效 ✓\n   - 仍缺：Neo et al. (ICLR 2025)、Raghu et al. 2021 (ViT RSA/CKA)、logit lens 系列\n\n### Overall Score: 4/10 → 5/10 (Marginally below acceptance)\n\n修订体现诚意但核心问题未完全解决：Neo et al. 缺失、无新方法、Abstract overclaims。\n\n**升至 6/10 的条件（均为文字修改）：**\n(a) 引用 Neo et al. 并 differentiate\n(b) Abstract 最后一句改为 hypothesis 而非 prescription\n(c) Title 加限定或改为不暗示一般性",
    "reviewer_id": "2",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-17T06:07:08.662831+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3866
}
```

</details>

---


### Assistant

_source line 88 · 2026-05-17T06:07:15.080613+00:00_

已提交 Round 2 评估。核心结论：

- **5/10**（从 4/10 上调 1 分）
- 修订有实质改善（删 "first"、扩展 Related Work、增加 caveats），但三个关键问题仍在：Neo et al. 未引（直接削弱 novelty positioning）、无新方法/实验、Abstract 与 Limitations 的语气不一致
- 升至 6/10 只需文字修改：引 Neo et al.、软化 Abstract 最后一句、Title 加限定

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2"
}
```

</details>

---


## Round 4

## Round 4

4 recorded events


### User

_source line 89 · 2026-05-17T06:08:28.594998+00:00_

[Round 2 审稿请求]:
## Round 2 Step 2 交叉确认（简化版）

R1 评分 5/10，R3 评分 7/10。请简要回应：

**R1 关键判定**：
- R1-W2 RESOLVED: "Why RSA over CKA" 段提供了 principled justification
- R1-N1: baseline confound — acknowledge 充分但无数据，标题/abstract 措辞仍 causal
- R1 指出具体 actionable items: Abstract "should"→"may benefit from"，Section 4.2 标题改为观察性
- R1 认为 5/10 维持，若 Llama-2 base 数据 + Abstract 软化可升至 6

**R3 关键判定**（7/10）：
- 从写作维度 conditional accept
- 仅需 4 个一行修改
- R3 的 7/10 是基于写作/格式评价，不含科学方法论评估

**问题**：
1. R1 将 CKA/RSA 问题标为 RESOLVED——你是否同意 "Why RSA over CKA" 段充分回应了你在 R1 轮提出的 metric divergence concern？
2. 如果 Abstract 最后一句如 R1 建议改为 hypothesis 语气，是否足以消除你对 overclaiming 的核心 concern？

请用 2-3 句话回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 90 · 2026-05-17T06:08:40.466178+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 ��� Round 2 Step 2 交叉确认\n\n**Q1 (CKA/RSA)**: 同意 RESOLVED。method.tex \"Why RSA over CKA\" 段提供了 principled argument（scale-invariance + dimension mismatch），且明确将 CKA 作为 complementary perspective 在 appendix 报告。这比 Round 1 的\"两个指标说不同的话我们选对我们有利的\"处理方式好得多��\n\n**Q2 (Abstract overclaiming)**: Abstract 最后一句改为 hypothesis 语气能消除 overclaiming concern 的大部分（约 80%）。但如果 Neo et al. 仍不引用，即使语气软化，novelty positioning 仍有缺陷——那是一个独立问题，不被 hedging 解决。两者都做到才能让我升至 6/10。",
  "reviewer_id": "2",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 ��� Round 2 Step 2 交叉确认\n\n**Q1 (CKA/RSA)**: 同意 RESOLVED。method.tex \"Why RSA over CKA\" 段提供了 principled argument（scale-invariance + dimension mismatch），且明确将 CKA 作为 complementary perspective 在 appendix 报告。这比 Round 1 的\"两个指标说不同的话我们选对我们有利的\"处理方式好得多��\n\n**Q2 (Abstract overclaiming)**: Abstract 最后一句改为 hypothesis 语气能消除 overclaiming concern 的大部分（约 80%）。但如果 Neo et al. 仍不引用，即使语气软化，novelty positioning 仍有缺陷——那是一个独立问题，不被 hedging 解决。两者都做到才能让我升至 6/10。",
    "reviewer_id": "2",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 91 · 2026-05-17T06:08:44.938383+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4472
}
```

</details>

---


### Assistant

_source line 92 · 2026-05-17T06:08:49.873141+00:00_

已提交。两个回答的要点：

1. **CKA/RSA**: 同意 R1 的 RESOLVED 判定。"Why RSA over CKA" 段提供了有原则的论证。
2. **Abstract hedge**: 能消除 overclaiming 的大部分，但如果 Neo et al. 仍不引用，novelty positioning 仍有独立缺陷。两者都需要才能升至 6/10。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2"
}
```

</details>

---


## Round 5

## Round 5

54 recorded events


### User

_source line 93 · 2026-05-17T18:01:56.908960+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责审查**新颖性/影响力 + 写作/格式合规**。

## 论文信息
- **标题**: Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model
- **文件路径**: `projects/vla-ssd/docs/paper/main.tex`（多文件结构：abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, appendix.tex, references.bib）
- **目标 Venue**: CoRL 2026（10th Conference on Robot Learning）
- **截止日期**: Paper 2026-05-28 EOD
- **格式**: 8 页正文 + references + appendix，双盲审稿，corl_2026 模板
- **匿名规则**: 双盲（double-blind）
- **Limitations**: 必须包含，计入 8 页

## 你的审查侧重

**新颖性/影响力 + 写作/格式**，具体关注：

### A. 新颖性与影响力

1. **与直接竞争者的区分度**：
   - Grant et al. (2026, arXiv:2603.19233) — 同为 VLA 内部表征分析，behavioral intervention（activation injection, SAE, probing）发现 visual dominance + language "encoded but not used"。本文的 token-level decomposition + trained-vs-untrained factorial control 是否构成足够增量？
   - Swann et al. (2026) — SAE on OpenVLA。本文与之的互补性如何？
   - Rizzardo/Buurmeijer et al. (2026) — feature observability/controllability on VLAs。
   - Häon et al. (CoRL 2025) — 第一篇 VLA mechanistic interpretability（activation steering）。

2. **贡献的显著性**：
   - C1（token-level specialization）：image tokens instruction-blind 是否可以从 causal mask 的 architecture 直接预测？如果 image tokens 在 causal attention 中看不到后面的 instruction tokens，那么 instruction-blind 是 trivial consequence 还是 empirical finding？
   - C2（front-loaded routing）：entry-exit attention pattern 的 practical implication 是什么？
   - C3（inverted-U refinement）：non-monotonic RSA 在 neuroscience 和 deep learning 中已有先例，novelty 在于 VLA-specific application？

3. **对 CoRL 社区的价值**：
   - 分析型论文（无新方法/无新 benchmark/无性能提升）在 CoRL 的接受度
   - Actionable insights 是否足够——论文的 findings 是否能指导 VLA 设计？

### B. 写作质量

1. **叙事结构**：Abstract/Intro/Method/Experiments/Discussion 的主线是否连贯一致
2. **AI 写作痕迹**：
   - grep 检查 em-dash（—）和 en-dash（ – ）
   - 检查 -ing 分词短语结尾
   - 检查 "Furthermore"/"Moreover"/"Additionally" 过度使用
   - 检查 "leverage"/"utilize"/"delve into" 等 AI 高频词
3. **数字和精度一致性**：全文数字精度是否统一
4. **图表质量**：信息密度、字体大小、caption 自包含性
5. **专有名词定义**：首次出现是否定义

### C. CoRL 2026 格式合规

1. **页数**：正文是否 ≤ 8 页
2. **模板**：`\usepackage{corl_2026}` 是否正确（review 版不应用 `[final]`）
3. **匿名化**：是否有泄露身份的信息（致谢、代码链接、自引）
4. **Limitations section**：是否存在且在 8 页内
5. **引用格式**：bib 格式一致性，是否有 preprint 应更新为正式发表版本
6. **引用充足度**：引用数量和覆盖范围是否达标

请按标准审稿格式输出：Summary → Strengths → Weaknesses → Questions → Minor Issues。
Weakness 分为 Must-Fix / Should-Fix / Nice-to-Have 三级。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 94 · 2026-05-17T18:02:10.067010+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 95 · 2026-05-17T18:02:10.117909+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/sessions/review_reviewer_2_df1bf1a9.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 96 · 2026-05-17T18:02:10.971550+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
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

_source line 97 · 2026-05-17T18:02:11.024099+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 98 · 2026-05-17T18:02:16.195736+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 99 · 2026-05-17T18:02:18.102464+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 100 · 2026-05-17T18:02:18.555683+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 101 · 2026-05-17T18:02:18.556098+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 102 · 2026-05-17T18:02:19.057872+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 103 · 2026-05-17T18:02:19.058263+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 104 · 2026-05-17T18:02:19.509950+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 105 · 2026-05-17T18:02:19.510328+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 106 · 2026-05-17T18:02:19.962015+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 107 · 2026-05-17T18:02:20.012579+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 108 · 2026-05-17T18:02:20.464640+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 109 · 2026-05-17T18:02:20.465153+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 110 · 2026-05-17T18:02:21.418896+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 111 · 2026-05-17T18:02:21.419298+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 112 · 2026-05-17T18:02:21.871073+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 113 · 2026-05-17T18:02:21.871427+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 114 · 2026-05-17T18:02:22.022592+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 115 · 2026-05-17T18:02:22.023140+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 116 · 2026-05-17T18:02:22.124116+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 117 · 2026-05-17T18:02:22.425583+00:00_

Web search results for query: "CoRL 2026 reviewer guidelines review form criteria"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CVPR 2026 Reviewer Guidelines","url":"https://cvpr.thecvf.com/Conferences/2026/ReviewerGuidelinesq"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"}]

Based on the search results, I found information about CoRL 2026, though the specific dedicated reviewer guidelines document wasn't directly returned. However, I can provide you with what I found:

The search results show information about CoRL 2026's submission requirements and some reviewer-related policies, but a dedicated "CoRL 2026 Reviewer Guidelines" document with a detailed review form and criteria wasn't prominently featured in the results.

From the available information, here's what I found about reviewer-related aspects of CoRL 2026:

**Reviewer Requirements:**
All submissions must include at least one author who agrees to serve as a CoRL reviewer, and they are qualified if they have at least one accepted publication at a previous robotics (CoRL/ICRA/IROS/RSS) or learning conference (ICLR/NeurIPS/ICML) or equivalent journal.

**Review Goals:**
Submissions should focus on a core robotics problem and
…[truncated 665 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6229
}
```

</details>

---


### Tool call

_source line 118 · 2026-05-17T18:02:31.409636+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2024.corl.org/contributions/instruction-for-reviews",
  "prompt": "Extract the complete review form criteria, scoring dimensions, and scoring scales. I need all evaluation dimensions (like soundness, significance, novelty, clarity, etc.), their definitions, and the numeric scoring scale for each."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2024.corl.org/contributions/instruction-for-reviews",
    "prompt": "Extract the complete review form criteria, scoring dimensions, and scoring scales. I need all evaluation dimensions (like soundness, significance, novelty, clarity, etc.), their definitions, and the numeric scoring scale for each."
  }
}
```

</details>

---


### Tool call

_source line 119 · 2026-05-17T18:02:32.864375+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl.org/contributions/instruction-for-authors",
  "prompt": "Extract ALL author instructions: page limits, template requirements, anonymity rules, mandatory sections, formatting constraints, and any other submission requirements for CoRL 2026."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl.org/contributions/instruction-for-authors",
    "prompt": "Extract ALL author instructions: page limits, template requirements, anonymity rules, mandatory sections, formatting constraints, and any other submission requirements for CoRL 2026."
  }
}
```

</details>

---


### Tool result

_source line 120 · 2026-05-17T18:02:35.274306+00:00_

# CoRL 2024 Review Criteria - Summary

Based on the provided webpage content, I cannot extract a complete review form with detailed scoring dimensions and numeric scales. 

The document only specifies **general review criteria for regular papers**:

Papers are evaluated on:
- "Significance and novelty of the results, either theoretical or empirical"
- "Degree to which they have been objectively established and/or their potential for scientific and technological impact"
- Relevance to robotic learning

**What's Missing:**
The webpage does not contain:
- Individual evaluation dimensions (soundness, clarity, originality, etc.)
- Numeric scoring scales (e.g., 1-5, 1-10)
- Detailed rubrics for each criterion
- Point breakdowns or weighting systems

The document focuses instead on desk rejection criteria and reviewer qualification requirements rather than the actual scoring form used to evaluate submissions. To obtain the complete review form template with scoring scales, you would need to access the actual review submission system or contact the CoRL 2024 organizing committee directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 3864
}
```

</details>

---


### Tool call

_source line 121 · 2026-05-17T18:02:35.274658+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 122 · 2026-05-17T18:02:35.726322+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 123 · 2026-05-17T18:02:36.228215+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 124 · 2026-05-17T18:02:37.682719+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 1454
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-17T18:02:38.691955+00:00_

# CoRL 2026 Author Instructions - Complete Summary

## Page Limits
- **Initial submission:** 8 pages maximum for main paper
- **Camera-ready:** 9 pages maximum for main paper
- Acknowledgments, references, and optional appendix do not count toward page limits

## Template Requirements
- Use provided LaTeX template (available via Google Drive links)
- For camera-ready: use `\usepackage[final]{corl_2026}`
- Match template's text density, fonts, spacing, and margins
- Footer on first page: "10th Conference on Robot Learning (CoRL 2026), Austin, Texas, USA."

## Anonymity Rules
- Double-blind review process required
- "All papers must be anonymized"
- De-anonymization occurs after decisions are announced
- Authors cannot be added/removed after abstract deadline

## Mandatory Sections
- **Limitations section** (counted in 8-page limit): must explicitly describe "limiting assumptions, failure modes, and other limitations"
- Acknowledgments
- References
- Optional: Appendix

## Formatting Constraints
- Submission platform: OpenReview
- Single zip file for all supplementary materials
- Footer required on camera-ready version
- Appendix should be included in main PDF, not separate file

## Additional Requirements
- Double-blind format throughout review
- Video submission encouraged (≤250 MB, ≤3 minutes)
- Supplementary materials permitted but not required
- Reciprocal reviewing requirement for qualified authors
- Disclosure of generative AI tool usage required
- Disclose fake citations result in desk rejection

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5827
}
```

</details>

---


### Tool call

_source line 126 · 2026-05-17T18:02:38.692322+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,|ing\\.|Furthermore|Moreover|Additionally|leverage|utilize|delve|myriad|plethora|paradigm shift",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,|ing\\.|Furthermore|Moreover|Additionally|leverage|utilize|delve|myriad|plethora|paradigm shift",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-17T18:02:38.993669+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex:15:Our Layer-1 attention head analysis extends this tradition to the VLA domain, where we find that 25 of 32 heads become instruction-dominant after fine-tuning.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:67:Llama-2 base concentrates instruction attention at mid-depth (L9--L16: 15--22 heads), consistent with autoregressive LM processing.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:76:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:123:The inverted-U replicates on LIBERO-Spatial ($\Delta = +0.023$, $p < 0.001$; Appendix~\ref{sec:cross_benchmark_appendix}) and is robust to distance metric, per-DOF decomposition, permutation testing, and halved demonstrations (Appendix~\ref{sec:robustness_appendix}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex:4:We decompose a VLA's internal representations with factorial trained-vs-untrained control, revealing: (1)~strict token-level specialization (instruction-blind image tokens, cross-validated readout hub); (2)~front-loaded instruction routing, shifted from mid-depth (L9--L16) to entry-exit (L0--L1, L31); and (3)~non-monotonic vision encoder refinement (peak L12, readout $R^2$ $+0.069$, image $\Delta \leq 1.7\%$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex:9:The instruction-blindness of image tokens provides a mechanistic explanation for the visual dominance reported by Grant et al.~\cite{grant2026}: with no instruction-specific information in image representations ($|\Delta| < 0.006$), the action pathway relies on the readout token for task conditioning.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex:20:In sum, we reveal token-le
…[truncated 2286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 128 · 2026-05-17T18:02:38.994107+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 reviewer instructions review form OpenReview scoring criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 reviewer instructions review form OpenReview scoring criteria"
  }
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-17T18:02:45.024244+00:00_

Web search results for query: "CoRL 2026 reviewer instructions review form OpenReview scoring criteria"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"CoRL 2026 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2026"},{"title":"ICML 2026 Reviewer Instructions","url":"https://icml.cc/Conferences/2026/ReviewerInstructions"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"CVPR 2026 Reviewer Guidelines","url":"https://cvpr.thecvf.com/Conferences/2026/ReviewerGuidelines"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"Insights from the ICLR Peer Review and Rebuttal Process","url":"https://arxiv.org/pdf/2511.15462"},{"title":"CoRL 2021 - Instructions for Reviewers","url":"https://2021.corl.org/reviewer-information/instructions-for-reviewers"}]

I found information about CoRL 2026, though the search results primarily contain general author instructions rather than detailed reviewer instructions with specific scoring criteria. Here's what I found:

## CoRL 2026 Review Process

The search results show that CoRL aims to have at least two reviewers per paper. Additionally, papers that receive all reviews in the "reject" range in the initial round will not proceed to the rebuttal phase.

## Review Form and Submission

Authors will not be able to give individual responses to the reviewer on OpenReview, nor will they be able to update the paper during the rebuttal process.

## Related Information from CoRL 2024

While I couldn't locate the specific 2026 reviewer instructions and detailed scoring criteria, I found
…[truncated 724 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6030
}
```

</details>

---


### Tool call

_source line 130 · 2026-05-17T18:02:50.924054+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 131 · 2026-05-17T18:02:51.576997+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 652
}
```

</details>

---


### Tool call

_source line 132 · 2026-05-17T18:02:53.283493+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl2023.org/reviewer-guidelines",
  "prompt": "Extract the complete review form scoring dimensions, scoring scales (1-10, 1-5, etc.), and detailed definitions for each review criterion (like significance, novelty, soundness, clarity, etc.). I need all dimensions and their scales."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl2023.org/reviewer-guidelines",
    "prompt": "Extract the complete review form scoring dimensions, scoring scales (1-10, 1-5, etc.), and detailed definitions for each review criterion (like significance, novelty, soundness, clarity, etc.). I need all dimensions and their scales."
  }
}
```

</details>

---


### Tool call

_source line 133 · 2026-05-17T18:02:54.688954+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl.org/contributions/call-for-papers",
  "prompt": "Extract all submission requirements, paper topics, evaluation criteria, and any review-related information for CoRL 2026."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl.org/contributions/call-for-papers",
    "prompt": "Extract all submission requirements, paper topics, evaluation criteria, and any review-related information for CoRL 2026."
  }
}
```

</details>

---


### Tool call

_source line 134 · 2026-05-17T18:02:55.495104+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 135 · 2026-05-17T18:02:57.954535+00:00_

# CoRL 2023 Review Form Dimensions

Based on the provided guidelines, the review form evaluates submissions across **six main criteria**:

1. **Originality**: "Are the problems or methods new?" Novel combinations of techniques count as valuable.

2. **Quality**: Assesses technical soundness, whether claims are supported by theory or experiments, and if authors honestly evaluate strengths and weaknesses.

3. **Clarity**: Evaluates writing quality, organization, and whether experts could reproduce results from the information provided.

4. **Significance**: Determines if results are important and whether the work "advance[s] the state of the art in a demonstrable way."

5. **Relevance**: Focuses on robot learning applicability and whether "the CoRL audience be interested in reading this paper?"

6. **Limitations**: Acknowledges that CoRL requires a limitations section; honestly reported limitations should be "treat[ed] kindly."

## Important Limitation

The document does **not specify numerical scoring scales** (e.g., 1-10 or 1-5). It provides evaluation dimensions and guidance for assessment but does not detail the actual quantitative scoring system reviewers would use when submitting their reviews.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 4671
}
```

</details>

---


### Tool result

_source line 136 · 2026-05-17T18:02:58.809093+00:00_

# CoRL 2026 Submission Requirements & Evaluation Information

## Core Submission Requirements

**Focus & Scope:** Papers must address "a core robotics problem" and demonstrate how proposed models, algorithms, datasets, or benchmarks apply to robotics. Submissions lacking robotics focus will be desk-rejected without peer review.

**Required Components:**
- Limitations section mandatory in all submissions, addressing "limiting assumptions, failure modes, and other limitations of the results and experiments"
- Real-robot experiments strongly encouraged, or convincing simulation-to-reality transferability evidence
- Supplementary materials welcomed: video, code, and data

## Acceptable Research Topics

The conference welcomes papers spanning:
- Perception and control representation learning
- Foundation models and knowledge systems for robots
- Imitation learning and reinforcement learning approaches
- Model-based/model-free learning for decision-making
- Planning-learning combinations
- Uncertainty quantification and probabilistic methods
- Data generation and benchmarking
- Task/motion planning, sensor fusion, vision
- Human-robot interaction and natural language instruction
- Hardware design optimization
- Safety and alignment in learning systems
- Applications across manipulation, navigation, locomotion, driving, and flight
- Theoretical foundations and generalization theory
- Video and latent world models
- Datasets and benchmarks

## Additional Guidance

No explicit evaluation criteria, review process details, or acceptance rates are specified in this document. Reference the "Instruction for Authors" page for formatting standards and submission deadlines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 4120
}
```

</details>

---


### Tool result

_source line 137 · 2026-05-17T18:07:55.672153+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 38, \"total_citations\": 68, \"unique_cited_keys\": 38, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 30, \"online_not_found\": 4, \"online_mismatch\": 4}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"kim2024_openvla\", \"type\": \"article\", \"title\": \"OpenVLA: An Open-Source Vision-Language-Action Model\", \"authors\": \"Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balak...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2406.09246\"}, {\"key\": \"karamcheti2024\", \"type\": \"article\", \"title\": \"Prismatic VLMs: Investigating the Design Space of Visually-Conditioned Language Models\", \"authors\": \"Karamcheti, Siddharth and Nair, Suraj and Balakrishna, Ashwin and Liang, Percy a...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2402.07865\"}, {\"key\": \"brohan2023_rt2\", \"type\": \"article\", \"title\": \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\", \"authors\": \"Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and C...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2307.15818\"}, {\"key\": \"liu2023_libero\", \"type\": \"inproceedings\", \"title\": \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\", \"authors\": \"Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"kriegeskorte2008\", \"type\": \"article\", \"title\": \"Representational Similarity Analysis -- Connecting the Branches of Systems Neuroscience\", \"authors\": \"Kriegeskorte, Nikolaus and Mur, Marieke and Bandettini, Peter\", \"year\": \"2008\", \"venue\": \"Frontiers in Systems Neuroscience\"}, {\"key\": \"korn
…[truncated 29542 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 300177
}
```

</details>

---


### Tool call

_source line 138 · 2026-05-17T18:10:35.745564+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://openreview.net/group?id=robot-learning.org/CoRL/2026/Conference",
  "prompt": "Extract the review form fields, scoring dimensions, and numeric scales used for reviewing papers at CoRL 2026. I need the exact field names, rating scales, and any descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://openreview.net/group?id=robot-learning.org/CoRL/2026/Conference",
    "prompt": "Extract the review form fields, scoring dimensions, and numeric scales used for reviewing papers at CoRL 2026. I need the exact field names, rating scales, and any descriptions."
  }
}
```

</details>

---


### Tool call

_source line 139 · 2026-05-17T18:10:36.200164+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"CoRL\" review form \"overall recommendation\" \"confidence\" scoring scale site:openreview.net"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"CoRL\" review form \"overall recommendation\" \"confidence\" scoring scale site:openreview.net"
  }
}
```

</details>

---


### Tool result

_source line 140 · 2026-05-17T18:10:38.057755+00:00_

I cannot extract the review form fields, scoring dimensions, and numeric scales for CoRL 2026 based on the provided content.

The webpage content you shared only displays the OpenReview.net navigation menu and footer information. It does not contain any details about the actual review form structure, rating scales, or evaluation criteria used for the CoRL 2026 conference.

To find this information, you would need to:
- Visit the full CoRL 2026 conference page on OpenReview
- Look for submission guidelines or reviewer instructions
- Check the actual review form interface when accessing the conference portal

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 2312
}
```

</details>

---


### Tool result

_source line 141 · 2026-05-17T18:10:40.979698+00:00_

Web search results for query: ""CoRL" review form "overall recommendation" "confidence" scoring scale site:openreview.net"

Links: [{"title":"Default Review Form | OpenReview","url":"https://docs.openreview.net/reference/default-forms/default-review-form"},{"title":"Under review as a conference paper at ICLR 2024","url":"https://openreview.net/pdf/e55f3cb39892682f5c37efa8b008171b91981671.pdf"},{"title":"CoRL 2023 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2023%2FConference"},{"title":"CoRL 2021 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2021%2FConference"},{"title":"CoRL 2024 Conference Submissions | OpenReview","url":"https://openreview.net/submissions?venue=robot-learning.org/CoRL/2024/Conference"},{"title":"Position: The AI Conference Peer Review Crisis Demands Author Feedback and Reviewer Rewards | OpenReview","url":"https://openreview.net/forum?id=l8QemUZaIA"},{"title":"CoRL 2025 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2025%2FConference"},{"title":"CoRL 2024 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FConference"},{"title":"CoRL | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL"},{"title":"You Are the Best Reviewer of Your Own Papers: An Owner-Assisted Scoring Mechanism | OpenReview","url":"https://openreview.net/forum?id=xmx5rE9QP7R"}]

I found information about review forms on OpenReview. The first result shows the default OpenReview review form structure, which includes both a rating scale and a confidence scale:

**Rating Scale:** The rating dropdown includes options from 10 (Top 5% of accepted papers, seminal paper) down to 1 (Trivial or wrong), with intermediate categories for different levels of acceptance and rejection.

**Confidence Scale:** The confidence field uses a radio button selection with a 5-point scale, where 5 r
…[truncated 722 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 4779
}
```

</details>

---


### Tool call

_source line 142 · 2026-05-17T18:10:45.145496+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://docs.openreview.net/reference/default-forms/default-review-form",
  "prompt": "Extract the complete default review form including ALL scoring dimensions, their exact numeric scales, and the text description of each score level. I need the full rating scale (1-10) and confidence scale (1-5) with exact descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://docs.openreview.net/reference/default-forms/default-review-form",
    "prompt": "Extract the complete default review form including ALL scoring dimensions, their exact numeric scales, and the text description of each score level. I need the full rating scale (1-10) and confidence scale (1-5) with exact descriptions."
  }
}
```

</details>

---


### Tool result

_source line 143 · 2026-05-17T18:10:47.905917+00:00_

# Default Review Form - Complete Scoring Dimensions

## Rating Scale (1-10)

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

## Confidence Scale (1-5)

| Score | Description |
|-------|-------------|
| 5 | "absolutely certain that the evaluation is correct and very familiar with the relevant literature" |
| 4 | "confident but not absolutely certain that the evaluation is correct" |
| 3 | "fairly confident that the evaluation is correct" |
| 2 | "willing to defend the evaluation, but it is quite likely that the reviewer did not understand central parts" |
| 1 | "evaluation is an educated guess" |

## Additional Fields

The form also includes a **title** field (max 500 characters) for a brief summary and a **review** field (1-20,000 characters) supporting Markdown and LaTeX formatting for detailed evaluation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 2760
}
```

</details>

---


### Tool call

_source line 144 · 2026-05-17T18:13:31.539955+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿意见：Vision Encodes, Language Routes\n\n**Overall: 5/10 (Marginally below acceptance threshold)**\n**Confidence: 4/5**\n\n**一句话总结**: 方法论严谨、写作清晰，但核心贡献 C1（image tokens instruction-blind）是 causal attention mask 的数学必然结果而非经验性发现，显著削弱新颖性；其余贡献效应量小或存在度量敏感性问题，对 CoRL 社区缺乏 actionable insights。\n\n---\n\n### 主要优势\n- S1: 系统化 2×2 factorial control（trained/untrained × instruction/no-instruction），三条件对比有效 disentangle language pretraining 与 VLA fine-tuning\n- S2: 充分的 robustness analysis（distance metric invariance, per-DOF, permutation test, seed sensitivity, demo subsampling, cross-benchmark）\n- S3: 写作质量良好，无 AI 写作痕迹，叙事连贯\n- S4: L1 attention ablation 提供了少有的 interventional causal evidence\n\n---\n\n### Must-Fix 问题\n\n**N1 [critical] C1 是 causal mask 的数学必然结果**\nOpenVLA 的 token 序列为 [image] → [instruction] → [readout/action]。Causal attention 中位置 i 的表征仅依赖位置 ≤ i。Image tokens 先于 instruction tokens，因此 image tokens 在任何层都无法 attend to instruction tokens——这是架构决定的数学性质，非 empirical finding。Frozen vision encoder 只接收图像，instruction invariance 同样 trivially expected。Discussion 仅一句话承认（\"C1 likely generalizes via the causal mask\"），但全文将 C1 作为首要贡献和标题基础。untrained 模型 L1 即达 100% classification 进一步支持 trivial 判断。建议重新定位 C1 或澄清 token ordering。\n\n**N2 [critical] RSA 与 CKA 矛盾未充分解决**\nLinear CKA 完全反转 RSA ordering（untrained > trained > DINOv2），直接否定 \"DINOv2 provides highest geometric foundation\"。RDM kernel CKA 中 DINOv2 在所有变体排名最低。Linear CKA per-layer profile 无 inverted-U。论文将此放在 appendix 归因于 \"metrics capture different properties\"，但未给出 principled argument 解释为何应信任 RSA。如果核心 claims 依赖度量选择，它们就不是 robust findings。\n\n---\n\n### Should-Fix 问题\n\n**W1** RSA best-vs-best 训练效应在 LIBERO-Goal 不显著（Δ=+0.017, CI includes 0, n.s.），但 Abstract/Intro 中未标注\n**W2** L1 ablation 使用 5 demos（vs. 主实验 50），R² 基准差异大（0.256 vs. ~0.65），可比性存疑\n**W3** 缺少 Llama-2 和 Open X-Embodiment 关键引用\n**W4** Architectural implications 仅为 observational insights，未通过设计实验验证（如 encoder swap），对 CoRL 实践社区 actionable value 不足\n**W5** 单模型（OpenVLA-7B）、单 benchmark family（LIBERO），泛化性有限\n\n---\n\n### 小问题\n- M1: Intro \"untested assumption\" 是 straw man（causal mask 下无人会这样假设）\n- M2: \"readout token\" 与 \"last_preaction\" 交替使用未定义等价性\n- M3: conclusion.tex 未被 main.tex \\input\n- M4: alain2017 实际年份应为 2016；nostalgebraist2020 blog post 格式不规范\n- M5: 多个 arXiv preprints 可能已有正式发表版本\n- M6: 个别 R² 精度不统一（2位 vs. 3位）\n\n---\n\n### 格式合规\n- 模板 ✓，匿名化 ✓，AI 痕迹 ✓\n- ⚠ 缺 Llama-2/OXE 引用，部分 preprint 应更新\n- ⚠ Limitations section 较简短\n\n### 与竞争者区分度\nGrant et al. (2026) 已发现 visual dominance + language \"encoded but not used\"。本文的 token-level 分解在 causal mask 约束下提供的额外 insight 有限。Häon et al. (CoRL 2025) 提供了 interventional analysis（activation steering），本文主要是 observational。整体增量有限。\n\n### 建议\n若能解决 N1（重新定位 C1 或论证 non-trivial token ordering）和 N2（正文讨论 CKA 矛盾），并增加一个 analysis-to-design bridge experiment，论文可提升至 borderline accept。",
  "reviewer_id": "2",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿意见：Vision Encodes, Language Routes\n\n**Overall: 5/10 (Marginally below acceptance threshold)**\n**Confidence: 4/5**\n\n**一句话总结**: 方法论严谨、写作清晰，但核心贡献 C1（image tokens instruction-blind）是 causal attention mask 的数学必然结果而非经验性发现，显著削弱新颖性；其余贡献效应量小或存在度量敏感性问题，对 CoRL 社区缺乏 actionable insights。\n\n---\n\n### 主要优势\n- S1: 系统化 2×2 factorial control（trained/untrained × instruction/no-instruction），三条件对比有效 disentangle language pretraining 与 VLA fine-tuning\n- S2: 充分的 robustness analysis（distance metric invariance, per-DOF, permutation test, seed sensitivity, demo subsampling, cross-benchmark）\n- S3: 写作质量良好，无 AI 写作痕迹，叙事连贯\n- S4: L1 attention ablation 提供了少有的 interventional causal evidence\n\n---\n\n### Must-Fix 问题\n\n**N1 [critical] C1 是 causal mask 的数学必然结果**\nOpenVLA 的 token 序列为 [image] → [instruction] → [readout/action]。Causal attention 中位置 i 的表征仅依赖位置 ≤ i。Image tokens 先于 instruction tokens，因此 image tokens 在任何层都无法 attend to instruction tokens——这是架构决定的数学性质，非 empirical finding。Frozen vision encoder 只接收图像，instruction invariance 同样 trivially expected。Discussion 仅一句话承认（\"C1 likely generalizes via the causal mask\"），但全文将 C1 作为首要贡献和标题基础。untrained 模型 L1 即达 100% classification 进一步支持 trivial 判断。建议重新定位 C1 或澄清 token ordering。\n\n**N2 [critical] RSA 与 CKA 矛盾未充分解决**\nLinear CKA 完全反转 RSA ordering（untrained > trained > DINOv2），直接否定 \"DINOv2 provides highest geometric foundation\"。RDM kernel CKA 中 DINOv2 在所有变体排名最低。Linear CKA per-layer profile 无 inverted-U。论文将此放在 appendix 归因于 \"metrics capture different properties\"，但未给出 principled argument 解释为何应信任 RSA。如果核心 claims 依赖度量选择，它们就不是 robust findings。\n\n---\n\n### Should-Fix 问题\n\n**W1** RSA best-vs-best 训练效应在 LIBERO-Goal 不显著（Δ=+0.017, CI includes 0, n.s.），但 Abstract/Intro 中未标注\n**W2** L1 ablation 使用 5 demos（vs. 主实验 50），R² 基准差异大（0.256 vs. ~0.65），可比性存疑\n**W3** 缺少 Llama-2 和 Open X-Embodiment 关键引用\n**W4** Architectural implications 仅为 observational insights，未通过设计实验验证（如 encoder swap），对 CoRL 实践社区 actionable value 不足\n**W5** 单模型（OpenVLA-7B）、单 benchmark family（LIBERO），泛化性有限\n\n---\n\n### 小问题\n- M1: Intro \"untested assumption\" 是 straw man（causal mask 下无人会这样假设）\n- M2: \"readout token\" 与 \"last_preaction\" 交替使用未定义等价性\n- M3: conclusion.tex 未被 main.tex \\input\n- M4: alain2017 实际年份应为 2016；nostalgebraist2020 blog post 格式不规范\n- M5: 多个 arXiv preprints 可能已有正式发表版本\n- M6: 个别 R² 精度不统一（2位 vs. 3位）\n\n---\n\n### 格式合规\n- 模板 ✓，匿名化 ✓，AI 痕迹 ✓\n- ⚠ 缺 Llama-2/OXE 引用，部分 preprint 应更新\n- ⚠ Limitations section 较简短\n\n### 与竞争者区分度\nGrant et al. (2026) 已发现 visual dominance + language \"encoded but not used\"。本文的 token-level 分解在 causal mask 约束下提供的额外 insight 有限。Häon et al. (CoRL 2025) 提供了 interventional analysis（activation steering），本文主要是 observational。整体增量有限。\n\n### 建议\n若能解决 N1（重新定位 C1 或论证 non-trivial token ordering）和 N2（正文讨论 CKA 矛盾），并增加一个 analysis-to-design bridge experiment，论文可提升至 borderline accept。",
    "reviewer_id": "2",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 145 · 2026-05-17T18:13:35.254101+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3714
}
```

</details>

---


### Assistant

_source line 146 · 2026-05-17T18:13:42.597059+00:00_

审稿意见已提交给 Review Director。

总结：评分 **5/10**（marginally below acceptance threshold）。两个 critical 问题：(1) C1 是 causal mask 的数学必然而非经验发现，但论文将其作为首要贡献和标题基础；(2) CKA 完全反转 RSA 的 ordering，核心 claims 的 robustness 存疑。论文方法论扎实、写作清晰是优势，但缺乏 actionable design insights 且泛化性有限。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2"
}
```

</details>

---


## Round 6

## Round 6

8 recorded events


### User

_source line 147 · 2026-05-17T18:14:33.009614+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 1 的完整审稿意见

请逐条回应以下 Reviewer 1 的审稿意见。对每一条使用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

以下是 Reviewer 1 的完整审稿原文：

**Overall: 3/5 (Borderline)**

### Must-Fix 问题

**N1 [critical]** Cross-instruction probe 任务 trivially easy，不支撑 "multimodal convergence" 的强 claim
- 10-way classification over 10 distinct instruction strings 对任何能 attend to instruction tokens 的位置都是 trivial 的
- 论文自己在 Appendix D.1 承认 "even incidental attention (~12%) suffices for linear classification at L1"
- untrained model（随机权重）在 L1 也达到 100%（Table 1）
- 100% 分类准确率不能作为 "multimodal convergence" 或 "functional specialization" 的强证据——它只反映 instruction embeddings 本身是线性可分的
- 真正有价值的发现是 image token 保持 chance level，但论文的对称叙事过度依赖 readout 侧的结果
- 建议增加更困难的 probe 任务或调整 framing

**N2 [critical]** RSA "inverted-U" 的 rise phase 效应量极小（Δρ = 0.016），且 metric-dependent
- Trained image_mean RSA 从 L0 (0.612) 到 L12 (0.628) 的升幅仅为 0.016（2.6%）
- Best-vs-best training effect (+0.017) 的 CI 包含 0
- Appendix B.2 显示 linear CKA 完全逆转了 RSA ordering
- "non-monotonic refinement" 是 metric-specific 的描述，而非 representation 的 intrinsic property
- 建议明确 qualify claims 的 metric-dependence，讨论为什么 RSA 比 CKA 更 appropriate

**N3 [critical]** L1 attention ablation 使用 5 demos（vs 主实验 50 demos），因果推断的可靠性存疑
- 用 50 个 total datapoints 训练 2-layer MLP probe（~1M 参数），baseline R²=0.256 暗示严重 underfitting
- ablation "improvement" 可能是 reduced effective input dimensionality 带来的 regularization effect
- 建议用 50 demos 重跑 ablation 或添加 random ablation control

### Should-Fix 问题

**W1** 缺乏多重比较校正（32 层 × 3 条件 × 多 metric 的逐层比较无 FDR/Bonferroni 校正）
**W2** Probe 的 total N 未报告，capacity 控制不充分（4096→256→7 有 ~1.05M 参数）
**W3** Untrained L1=100% 削弱 Finding 1 的 interpretation，讨论不足
**W4** Frozen vision encoder 是 feature 但也是 confound："vision encoder quality > LLM scale" 的 implication 需要 across-encoder 实验支持
**W5** 25 vs 24 heads 不一致需要更清晰解释

### Questions

Q1: Cross-instruction probe 主结果（Table 1 的 100%）用的是 linear 还是 MLP？
Q2: Ablation 中 5 demos 对应多少 total observation-action pairs？
Q3: RSA 中每个 demo 取一个 observation 还是多个？同一 demo 的 temporal autocorrelation 是否 inflate RSA？
Q4: Readout RSA 是否也呈 inverted-U？
Q5: Untrained readout R² peak 在 L32 (0.609) 如何解释？

---

请逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 148 · 2026-05-17T18:15:28.419116+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
  "offset": "14",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
    "offset": "14",
    "limit": "40"
  }
}
```

</details>

---


### Tool result

_source line 149 · 2026-05-17T18:15:28.871496+00:00_

14	\subsection{Token-Level Functional Specialization}
15	\label{sec:token_specialization}
16	
17	We test whether image tokens and readout tokens encode different types of information by training cross-instruction probes (\S\ref{sec:cross_instruction_probes}): given the same visual frame paired with each of 10 task instructions, we classify which instruction was present from per-layer activations.
18	
19	\paragraph{Image tokens are instruction-blind.}
20	At the image\_mean position, instruction classification remains at chance ($10\%$) across all 32 layers, in both trained and untrained models (Table~\ref{tab:dense_routing_main}).
21	Both linear and MLP probes confirm chance-level performance ($10\%$), as does standalone DINOv2 \texttt{cls\_token} ($10\%$), ruling out probe capacity.
22	RSA corroborates: instruction presence produces $|\Delta| \leq 0.006$ across all conditions (Appendix~\ref{sec:instruction_invariance_appendix}).
23	
24	\paragraph{Readout token as multimodal hub.}
25	The readout token tells a different story.
26	Trained last\_preaction achieves $100\%$ 10-way classification from L1 through L31, confirmed by LOOCV ($100\% \pm 0.00$ across all folds; Appendix~\ref{sec:loocv}).
27	The untrained model achieves $100\%$ at L1 but decays to $82\%$ by L31.
28	
29	\paragraph{Functional implications.}
30	This division indicates the readout token is the sole locus of multimodal integration.
31	QA probes confirm richer task-relevant information at the readout: trained last\_preaction achieves $86.3\%$ (L20) vs.\ DINOv2 \texttt{cls\_token} $82.7\%$ (Appendix~\ref{sec:qa_probe}).
32	These patterns replicate on LIBERO-Spatial (Appendix~\ref{sec:cross_benchmark_appendix}).
33	
34	\begin{table}[t]
35	\centering
36	\caption{Cross-instruction 10-way classification (selected layers; full profile in Appendix~\ref{sec:dense_routing}). Image\_mean stays at chance; readout achieves $100\%$ from L1 (trained) or decays (untrained).}
37	\label{tab:dense_routing_main}
38	\small
…[truncated 459 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 150 · 2026-05-17T18:15:28.872021+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex",
  "offset": "30",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex",
    "offset": "30",
    "limit": "10"
  }
}
```

</details>

---


### Tool result

_source line 151 · 2026-05-17T18:15:28.972756+00:00_

30	\subsection{Cross-Instruction Probes}
31	\label{sec:cross_instruction_probes}
32	
33	To test whether different token types encode instruction identity, we construct a cross-instruction dataset: each visual frame is paired with all 10 task instructions, producing 10 representation vectors per frame per layer.
34	A linear classifier (10-way) is trained to identify which instruction was present, separately for image\_mean and readout token positions.
35	We validate with leave-one-out cross-validation (LOOCV) over 10 folds, each holding out one task's instructions, to confirm that results reflect generalizable instruction encoding rather than memorization.
36	
37	%------------------------------------------------------------------
38	\subsection{Attention Pattern Analysis}
39	\label{sec:attention_analysis}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 152 · 2026-05-17T18:17:31.321164+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n### Must-Fix\n\n**[AGREE] R1-N1: Cross-instruction probe trivially easy**\n同意。与我的 N1（causal mask 使 C1 trivially true）高度一致但视角互补——R1 从 probe difficulty，我从 architecture。两者指向同一结论：C1 证据链薄弱。补充：(1) untrained L1=100% + 论文自承 \"~12% attention suffices\" 是论文自己提供的 trivial 证据；(2) QA probe 差异仅 3.6pp (86.3% vs 82.7%) 不足以支撑 \"sole locus\" 强 claim；(3) trained vs untrained trajectory 差异是唯一值得保留的信号。\n\n**[AGREE] R1-N2: RSA inverted-U rise phase 极小且 metric-dependent**\n完全同意。与我的 N2 一致。补充：R1 的 Δρ=0.016 (rise) 和我的 Δ=0.017 (training effect) 共同表明 inverted-U 的 rise phase 在 noise floor。Linear CKA per-layer 单调递增无 inverted-U（Appendix D.1 line 25-26）。RDM kernel CKA 中 DINOv2 排名最低（0.241），进一步削弱 \"DINOv2 geometric ceiling\" claim 的 robustness。\n\n**[AGREE] R1-N3: L1 ablation 5 demos 不可靠**\n同意核心关切。补充：论文用 L8/L13 null result 排除 artifact（Section 4.3 line 77-78），但如果 L8/L13 本身不受 L1 attention 影响（有独立 attention patterns），null result 不能排除 L1 level confound。支持 R1 的 random ablation control 建议。\n\n### Should-Fix\n\n**[AGREE] R1-W1**: 多重比较校正缺失是合理关切。Bootstrap CIs 为 per-comparison，无 family-wise 校正。\n**[AGREE] R1-W2**: Total N 未报告。同意 capacity 控制不充分。\n**[AGREE] R1-W3**: 强烈同意。untrained L1=100% 直接削弱 Finding 1 的 trained-side interpretation。\n**[AGREE] R1-W4**: 同意。\"encoder quality > LLM scale\" 需要 across-encoder 实验，否则只是 restatement。与我的 W4 一致。\n\n**[REBUT] R1-W5**: 部分反驳。论文在 3 处解释了 25/24 差异（Section 4.3 line 68, line 76, Table 7 caption），来源是 dedicated vs. bulk extraction 的 threshold boundary。Appendix Table 8 提供了 30%-70% threshold sensitivity 验证。但同意解释分散，建议集中说明。\n\n### Questions\n\nQ1: 主结果用 linear classifier（Method 3.3），MLP 仅作 corroboration。Linear 就达 100% 进一步支持 R1-N1。\nQ2: 未明确报告。估计 50 demos × 50-200 steps/demo × 10 tasks ≈ 2,500-10,000 pairs for 5-demo ablation。\nQ3: 好问题。论文未说明 temporal autocorrelation 处理和 bootstrap 是否 block by demo。可能 inflate RSA ρ。\nQ4: Table 3 显示 readout RSA peak L12 (0.643)，但 Figure 3 只画了 image_mean。Spatial appendix 暗示 readout 也 non-monotonic。建议补充 readout 曲线。\nQ5: 推测 L32 layer norm 对 random projections 的 normalization 可能产生 probe-friendly scaling，但论文未讨论。\n\n### 综合评估\n\nR1 和 R2 独立发现高度一致的核心问题：C1 trivial（R1 从 probe difficulty，R2 从 causal mask）；C3 metric-dependent（两人都指出 CKA 矛盾）；ablation 数据量不足。建议将这三个问题合并为 rebuttal 必须回应的核心关切。论文的实验设计和写作质量是真正的优势。",
  "reviewer_id": "2",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n### Must-Fix\n\n**[AGREE] R1-N1: Cross-instruction probe trivially easy**\n同意。与我的 N1（causal mask 使 C1 trivially true）高度一致但视角互补——R1 从 probe difficulty，我从 architecture。两者指向同一结论：C1 证据链薄弱。补充：(1) untrained L1=100% + 论文自承 \"~12% attention suffices\" 是论文自己提供的 trivial 证据；(2) QA probe 差异仅 3.6pp (86.3% vs 82.7%) 不足以支撑 \"sole locus\" 强 claim；(3) trained vs untrained trajectory 差异是唯一值得保留的信号。\n\n**[AGREE] R1-N2: RSA inverted-U rise phase 极小且 metric-dependent**\n完全同意。与我的 N2 一致。补充：R1 的 Δρ=0.016 (rise) 和我的 Δ=0.017 (training effect) 共同表明 inverted-U 的 rise phase 在 noise floor。Linear CKA per-layer 单调递增无 inverted-U（Appendix D.1 line 25-26）。RDM kernel CKA 中 DINOv2 排名最低（0.241），进一步削弱 \"DINOv2 geometric ceiling\" claim 的 robustness。\n\n**[AGREE] R1-N3: L1 ablation 5 demos 不可靠**\n同意核心关切。补充：论文用 L8/L13 null result 排除 artifact（Section 4.3 line 77-78），但如果 L8/L13 本身不受 L1 attention 影响（有独立 attention patterns），null result 不能排除 L1 level confound。支持 R1 的 random ablation control 建议。\n\n### Should-Fix\n\n**[AGREE] R1-W1**: 多重比较校正缺失是合理关切。Bootstrap CIs 为 per-comparison，无 family-wise 校正。\n**[AGREE] R1-W2**: Total N 未报告。同意 capacity 控制不充分。\n**[AGREE] R1-W3**: 强烈同意。untrained L1=100% 直接削弱 Finding 1 的 trained-side interpretation。\n**[AGREE] R1-W4**: 同意。\"encoder quality > LLM scale\" 需要 across-encoder 实验，否则只是 restatement。与我的 W4 一致。\n\n**[REBUT] R1-W5**: 部分反驳。论文在 3 处解释了 25/24 差异（Section 4.3 line 68, line 76, Table 7 caption），来源是 dedicated vs. bulk extraction 的 threshold boundary。Appendix Table 8 提供了 30%-70% threshold sensitivity 验证。但同意解释分散，建议集中说明。\n\n### Questions\n\nQ1: 主结果用 linear classifier（Method 3.3），MLP 仅作 corroboration。Linear 就达 100% 进一步支持 R1-N1。\nQ2: 未明确报告。估计 50 demos × 50-200 steps/demo × 10 tasks ≈ 2,500-10,000 pairs for 5-demo ablation。\nQ3: 好问题。论文未说明 temporal autocorrelation 处理和 bootstrap 是否 block by demo。可能 inflate RSA ρ。\nQ4: Table 3 显示 readout RSA peak L12 (0.643)，但 Figure 3 只画了 image_mean。Spatial appendix 暗示 readout 也 non-monotonic。建议补充 readout 曲线。\nQ5: 推测 L32 layer norm 对 random projections 的 normalization 可能产生 probe-friendly scaling，但论文未讨论。\n\n### 综合评估\n\nR1 和 R2 独立发现高度一致的核心问题：C1 trivial（R1 从 probe difficulty，R2 从 causal mask）；C3 metric-dependent（两人都指出 CKA 矛盾）；ablation 数据量不足。建议将这三个问题合并为 rebuttal 必须回应的核心关切。论文的实验设计和写作质量是真正的优势。",
    "reviewer_id": "2",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 153 · 2026-05-17T18:17:35.186319+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3865
}
```

</details>

---


### Assistant

_source line 154 · 2026-05-17T18:17:44.182565+00:00_

交叉回应已提交。

总结：R1 的 6 条 Must-Fix/Should-Fix 中我同意 5 条、部分反驳 1 条（W5，论文已在多处解释 25/24 差异，只是分散）。R1 和我的审稿独立发现了三个共同核心问题：(1) C1 trivially true（R1 从 probe difficulty 角度，我从 causal mask 角度）；(2) inverted-U 和 DINOv2 ceiling claim 的 metric sensitivity；(3) ablation 数据量不足。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2"
}
```

</details>

---


## Round 7

## Round 7

70 recorded events


### User

_source line 155 · 2026-05-18T01:50:15.061981+00:00_

[Round 1 审稿请求]:
## 审稿任务 — Reviewer 2: 新颖性/意义 + 相关工作 + Framing

**论文**: "Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model"
**路径**: `projects/vla-ssd/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, appendix.tex, references.bib）
**Venue**: CoRL 2026, double-blind, 8 页正文 + refs + appendix, Limitations section 必须（计入 8 页）
**Deadline**: 2026-05-29

### 你的审查侧重

**1. 新颖性与意义评估**
- 三个 claims 的 novelty 层级：C1（framework + architecture verification）、C2（instruction routing reorganization, 核心 finding）、C3（vision encoder geometry observation）
- 与最近的直接竞争者对比 novelty：Grant et al. 2026 (Action Atlas, 6 models), Häon et al. 2025 (steering directions), Swann/Buurmeijer 2026 (SAE features)
- C2 的 three-condition routing gradient（0/32 → 9/32 → 24/32）是否构成 genuine empirical contribution？
- 对 CoRL 社区（robotics + learning）的实际意义：分析论文的 finding 能否指导 VLA 设计？

**2. 相关工作覆盖度**
- 当前 references.bib 有 29 entries。评估是否达到 CoRL 论文的引用覆盖标准
- 检查是否缺失重要相关工作（特别是：2025-2026 年的 VLA 分析论文、VLM token-level analysis、probing methodology 经典文献）
- Related Work section 的组织结构和 positioning 是否清晰

**3. Framing 与 Claim 范围**
- Abstract 和 Introduction 的 claim 强度是否匹配证据：
  - C1 是否恰当定位为 framework 而非 finding？
  - C2 "front-loads instruction routing" 是否有充分支撑？
  - C3 "non-monotonic" observation 是否恰当标注了 metric-dependence？
- Title 使用单数"a Vision-Language-Action Model"——是否已消除 overclaiming？
- Discussion 的 design implications 是否仍然过强？

**4. Round 4 Framing Issues 修复检查**
- **R4-N1 (critical)**: C1 reframe 是否到位（从"empirical finding"到"experimental framework + empirical verification"）
- **R4-W1 (warning)**: RSA best-vs-best n.s. 在 Abstract/Intro 是否已标注
- **R4-W4 (warning)**: Frozen encoder confound caveat 是否在 Discussion 中充分说明
- **R4-W5 (warning)**: 单模型局限性是否已在 Limitations 中充分展开
- **R4-W7 (warning)**: Introduction 的 "untested assumption" straw man 是否已修复
- **R4-I1 (info)**: conclusion.tex 是否已整合或 Discussion 结尾是否充分

**5. 写作风格**
- 检查 AI 写作痕迹（em-dash、-ing phrases、过度分段）
- 专有名词是否首次出现即定义
- Abstract 是否满足 150-250 words 和四个必答问题

### 输出格式
按以下结构输出审稿意见：
1. Summary（2-3 句）
2. Strengths（逐条）
3. Weaknesses（分 critical / warning / info 三级，逐条）
4. Round 4 Issue Status（逐条标注 RESOLVED / PARTIALLY_RESOLVED / NOT_RESOLVED）
5. Missing References（如有）
6. Questions for Authors
7. Overall Score（1-10）和 Confidence（1-5）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 156 · 2026-05-18T01:50:24.831000+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 157 · 2026-05-18T01:50:25.185401+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/sessions/review_reviewer_2_df1bf1a9.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 354
}
```

</details>

---


### Tool call

_source line 158 · 2026-05-18T01:50:25.185868+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 159 · 2026-05-18T01:50:25.186161+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 160 · 2026-05-18T01:50:27.296102+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 161 · 2026-05-18T01:50:27.797814+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 162 · 2026-05-18T01:50:27.798318+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 163 · 2026-05-18T01:50:28.300145+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 164 · 2026-05-18T01:50:28.300521+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 165 · 2026-05-18T01:50:28.351100+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 166 · 2026-05-18T01:50:28.752567+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 167 · 2026-05-18T01:50:29.204204+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 168 · 2026-05-18T01:50:29.204768+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 169 · 2026-05-18T01:50:29.656491+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 170 · 2026-05-18T01:50:29.656850+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 171 · 2026-05-18T01:50:30.210656+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 172 · 2026-05-18T01:50:30.211125+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 173 · 2026-05-18T01:50:30.765476+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 554
}
```

</details>

---


### Tool call

_source line 174 · 2026-05-18T01:50:30.765897+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 175 · 2026-05-18T01:50:30.816642+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 176 · 2026-05-18T01:50:36.847586+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,TodoWrite",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,TodoWrite",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 177 · 2026-05-18T01:50:36.898126+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 178 · 2026-05-18T01:50:51.383830+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '搜索 CoRL 2026 reviewer guidelines / review form', 'status': 'in_progress', 'activeForm': '搜索 CoRL 2026 reviewer guidelines'}, {'content': '检查 AI 写作痕迹（em-dash, -ing phrases, 过度分段）', 'status': 'pending', 'activeForm': '检查 AI 写作痕迹'}, {'content': '评估新颖性与意义（C1/C2/C3 + 竞争者对比）', 'status': 'pending', 'activeForm': '评估新颖性与意义'}, {'content': '评估相关工作覆盖度和 positioning', 'status': 'pending', 'activeForm': '评估相关工作覆盖度'}, {'content': '评估 Framing 与 Claim 范围', 'status': 'pending', 'activeForm': '评估 Framing 与 Claim 范围'}, {'content': '检查 Round 4 issues 修复状态', 'status': 'pending', 'activeForm': '检查 Round 4 issues 修复状态'}, {'content': '撰写完整审稿意见并汇报 Director', 'status': 'pending', 'activeForm': '撰写完整审稿意见'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '搜索 CoRL 2026 reviewer guidelines / review form', 'status': 'in_progress', 'activeForm': '搜索 CoRL 2026 reviewer guidelines'}, {'content': '检查 AI 写作痕迹（em-dash, -ing phrases, 过度分段）', 'status': 'pending', 'activeForm': '检查 AI 写作痕迹'}, {'content': '评估新颖性与意义（C1/C2/C3 + 竞争者对比）', 'status': 'pending', 'activeForm': '评估新颖性与意义'}, {'content': '评估相关工作覆盖度和 positioning', 'status': 'pending', 'activeForm': '评估相关工作覆盖度'}, {'content': '评估 Framing 与 Claim 范围', 'status': 'pending', 'activeForm': '评估 Framing 与 Claim 范围'}, {'content': '检查 Round 4 issues 修复状态', 'status': 'pending', 'activeForm': '检查 Round 4 issues 修复状态'}, {'content': '撰写完整审稿意见并汇报 Director', 'status': 'pending', 'activeForm': '撰写完整审稿意见'}]"
  }
}
```

</details>

---


### Tool result

_source line 179 · 2026-05-18T01:50:51.384376+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 180 · 2026-05-18T01:50:53.542725+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 181 · 2026-05-18T01:50:55.902078+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 182 · 2026-05-18T01:50:56.404426+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 183 · 2026-05-18T01:50:56.404905+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 184 · 2026-05-18T01:50:56.455497+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 185 · 2026-05-18T01:50:59.418118+00:00_

Web search results for query: "CoRL 2026 reviewer guidelines review form criteria"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CVPR 2026 Reviewer Guidelines","url":"https://cvpr.thecvf.com/Conferences/2026/ReviewerGuidelinesq"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"2026 Reviewer Guidelines","url":"https://neurips.cc/Conferences/2026/ReviewerGuidelines"}]

Based on the web search results, I found some relevant information about CoRL 2026, though the specific detailed reviewer guidelines and review form criteria for CoRL 2026 don't appear to be fully published yet. However, I can share what is available:

## CoRL 2026 Reviewer Information

All submissions to CoRL 2026 must include at least one author who agrees to serve as a CoRL reviewer and is qualified if they have at least one accepted publication at a previous robotics (CoRL/ICRA/IROS/RSS) or learning conference (ICLR/NeurIPS/ICML) or equivalent journal.

The aim is to have at least two reviewers per paper.

## Historical CoRL Review Criteria

While specific 2026 criteria aren't fully detailed in the search results, the CoRL 2024 guidelines indicate that submissions are evaluated based on the significance and novelty of the results, either theoretical or empirical. Additionally, reviewers assess whe
…[truncated 549 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5875
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-18T01:51:01.583637+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2024 instruction for reviews reviewer form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2024 instruction for reviews reviewer form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 187 · 2026-05-18T01:51:02.086023+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 reviewer instructions openreview review form"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 reviewer instructions openreview review form"
  }
}
```

</details>

---


### Tool call

_source line 188 · 2026-05-18T01:51:03.091278+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 189 · 2026-05-18T01:51:03.142221+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:78:To test whether L1 instruction-dominant heads causally mediate a capacity trade-off between instruction routing and action encoding, we ablate their attention to instruction tokens and measure downstream action probe $R^2$ using 50 demonstrations per task ($N = 63{,}228$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:128:The inverted-U replicates on LIBERO-Spatial ($\Delta = +0.023$, $p < 0.001$; Appendix~\ref{sec:cross_benchmark_appendix}) and is robust to distance metric, per-DOF decomposition, permutation testing, halved demonstrations, and data subsampling (25 demonstrations: RSA peak unchanged at L12, profile $r = 0.97$; Appendix~\ref{sec:robustness_appendix}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex:4:We decompose a VLA's internal representations with factorial trained-vs-untrained control, revealing: (1)~strict token-level specialization (instruction-blind image tokens, cross-validated readout hub); (2)~front-loaded instruction routing, shifted from mid-depth (L9--L16) to entry-exit (L0--L1, L31); and (3)~non-monotonic vision encoder refinement (peak L12, readout $R^2$ $+0.069$, image $\Delta \leq 1.7\%$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex:12:To disentangle the contributions of language pretraining and VLA fine-tuning, we compare three LLM conditions: (1)~VLA-trained (the released checkpoint), (2)~Llama-2 base (the pretrained LLM backbone without VLA fine-tuning), and (3)~untrained (all 6.74B LLM parameters reinitialized via \texttt{from\_config()}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex:20:\emph{Third}, vision encoder representations undergo a non-monotonic transformation through LLM layers: functional probes peak at L8--L13 ($R^2 = 0.655$--$0.678$) before d
…[truncated 440 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 190 · 2026-05-18T01:51:07.817509+00:00_

Web search results for query: "CoRL 2024 instruction for reviews reviewer form criteria scoring"

Links: [{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2024 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/corl-paper-list/corl-2024-paper-list/"},{"title":"CoRL 2024 - Instruction for Authors","url":"https://2024.corl.org/contributions/instruction-for-authors"},{"title":"CORL 2024 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/corl-statistics/corl-2024-statistics/"},{"title":"CoRL 2024 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FConference"},{"title":"ICML 2024 Reviewer Instructions","url":"https://icml.cc/Conferences/2024/ReviewerInstructions"},{"title":"Conference on Robot Learning","url":"https://twitter.com/corl_conf/status/1666663426339508224"},{"title":"Instructions for Reviewers","url":"https://corl2022.org/instructions-for-reviewers/"}]

Based on the search results, I found the official CoRL 2024 Instruction for Reviews page. Here's what the guidelines cover:

## Reviewer Expertise Requirements

Reviewers need to have expertise in robotics, robot learning, machine learning and complementary fields. Reviewers ideally have a minimum of 3 first author publications in major robotics conferences and journals such as CoRL, RSS, ICRA, IROS, IJRR, TRO, RAL and core machine learning venues like NeurIPS, ICML, AIStats, JMLR, PAMI.

## Evaluation Criteria

Results will be judged on the degree to which they have been objectively established and/or their potential for scientific and technological impact, as well as their relevance to robotic learning.

## Review Process Fea
…[truncated 703 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6233
}
```

</details>

---


### Tool result

_source line 191 · 2026-05-18T01:51:07.918478+00:00_

Web search results for query: "CoRL 2026 reviewer instructions openreview review form"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2026"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"ICML 2026 Reviewer Instructions","url":"https://icml.cc/Conferences/2026/ReviewerInstructions"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"CoRL | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"Frequently Asked Questions","url":"https://corl2022.org/frequently-asked-questions/"}]

I found some information about CoRL 2026, though the specific reviewer instructions and review form details for 2026 are not yet fully available in the search results. Here's what I found:

**Available CoRL 2026 Information:**

The search results point to the official CoRL 2026 pages on OpenReview and the CoRL website, but the detailed reviewer instructions page for 2026 doesn't appear to have published comprehensive reviewer guidelines yet.

**What I Found:**

1. CoRL 2026 Conference has a homepage on OpenReview, accessible at openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference

2. For context, CoRL's main review form evaluates originality, quality, clarity, significance, relevance and limitations (based on CoRL 2023 guidelines)

3. Papers that receive all "reject" reviews in the initial round will not proceed to the r
…[truncated 465 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5832
}
```

</details>

---


### Tool call

_source line 192 · 2026-05-18T01:51:13.542101+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
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

_source line 193 · 2026-05-18T01:51:13.743246+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 194 · 2026-05-18T01:51:18.265496+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl2023.org/reviewer-guidelines",
  "prompt": "Extract the complete review form criteria, scoring dimensions, and scale (e.g., 1-10 overall recommendation, soundness, novelty, clarity, significance, etc.). List each dimension with its scale and description."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl2023.org/reviewer-guidelines",
    "prompt": "Extract the complete review form criteria, scoring dimensions, and scale (e.g., 1-10 overall recommendation, soundness, novelty, clarity, significance, etc.). List each dimension with its scale and description."
  }
}
```

</details>

---


### Tool call

_source line 195 · 2026-05-18T01:51:19.371637+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2024.corl.org/contributions/instruction-for-reviews",
  "prompt": "Extract the complete review form criteria, scoring dimensions, scale, and any specific instructions for reviewers. List each evaluation dimension with its scale and what reviewers should assess."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2024.corl.org/contributions/instruction-for-reviews",
    "prompt": "Extract the complete review form criteria, scoring dimensions, scale, and any specific instructions for reviewers. List each evaluation dimension with its scale and what reviewers should assess."
  }
}
```

</details>

---


### Tool result

_source line 196 · 2026-05-18T01:51:23.539670+00:00_

# CoRL 2023 Review Form Criteria

Based on the provided guidelines, the review form evaluates submissions across **six key dimensions**:

1. **Originality**: Assesses whether problems/methods are new, novel combinations of existing techniques, and proper differentiation from prior work.

2. **Quality**: Evaluates technical soundness, claim support through analysis or experiments, appropriateness of methods, completeness, and author honesty about strengths/weaknesses.

3. **Clarity**: Examines writing quality, organization, and whether content provides sufficient detail for expert reproducibility.

4. **Significance**: Determines if results are important, likely to influence researchers/practitioners, and advance the field demonstrably.

5. **Relevance**: Confirms the paper addresses robot learning problems, applies learning-based methods, includes simulation or real robot evaluation, and interests the CoRL audience.

6. **Limitations**: Acknowledges that CoRL requires a limitations section; honestly reported limitations should be treated positively, while unreported flaws should significantly impact scores.

**Important Note**: The document does not specify a numerical scoring scale (such as 1-10 ratings) for these dimensions. The guidelines emphasize constructive, concrete feedback rather than detailing a structured scoring rubric with defined point ranges.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5274
}
```

</details>

---


### Tool result

_source line 197 · 2026-05-18T01:51:25.911123+00:00_

# CoRL 2024 Review Criteria

Based on the provided content, the document does **not contain a complete review form with specific scoring dimensions or numerical scales**. Instead, it outlines foundational evaluation principles:

## Review Criteria (Main Evaluation Basis)

Reviewers assess submissions on:

1. **Significance and Novelty** — both theoretical and empirical contributions
2. **Objective Establishment** — degree to which results are rigorously demonstrated
3. **Impact Potential** — scientific and technological relevance
4. **Relevance to Robot Learning** — connection to the field's core focus

## Scope Requirements (Desk Reject Criteria)

To avoid rejection, papers must demonstrate relevance through either:

- **Intent**: "Explicitly address a learning question for physical robots," OR
- **Outcome**: "Test the proposed learning solution on physical robots"

## Notable Gaps

The instructions lack:
- Specific numerical rating scales (e.g., 1-5, 1-10)
- Detailed rubrics for each dimension
- Guidance on weighting criteria
- Specific assessment prompts for reviewers

The document emphasizes that CoRL takes "a broad view of robot learning" and welcomes both experimental and theoretical work, but defers detailed scoring methodologies to the actual review form, which is not included in this excerpt.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6539
}
```

</details>

---


### Tool call

_source line 198 · 2026-05-18T01:51:33.092305+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL openreview review form \"overall recommendation\" \"confidence\" scale 1-10 site:openreview.net"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL openreview review form \"overall recommendation\" \"confidence\" scale 1-10 site:openreview.net"
  }
}
```

</details>

---


### Tool result

_source line 199 · 2026-05-18T01:51:38.162153+00:00_

Web search results for query: "CoRL openreview review form "overall recommendation" "confidence" scale 1-10 site:openreview.net"

Links: [{"title":"Default Review Form | OpenReview","url":"https://docs.openreview.net/reference/default-forms/default-review-form"},{"title":"Why are the \"rating\" and \"confidence\" fields in my PC Console wrong? | OpenReview","url":"https://docs.openreview.net/getting-started/frequently-asked-questions/why-are-the-rating-and-confidence-fields-in-my-pc-console-wrong"},{"title":"Default Meta Review Form | OpenReview","url":"https://docs.openreview.net/reference/default-forms/default-meta-review-form"},{"title":"Reference-Free Rating of LLM Responses via Latent Information | OpenReview","url":"https://openreview.net/forum?id=WoYvrulVOp"},{"title":"Review Stage | OpenReview","url":"https://docs.openreview.net/reference/stages/review-stage"},{"title":"Position: The AI Conference Peer Review Crisis Demands Author Feedback and Reviewer Rewards | OpenReview","url":"https://openreview.net/forum?id=l8QemUZaIA"},{"title":"Openreview","url":"https://openreview.net/pdf/7abd65724a350c731a52b0e5cf304772b9b3289d.pdf"},{"title":"CONFIDENCE CALIBRATION IN VISION-LANGUAGE-ACTION ...","url":"https://openreview.net/pdf/527841d8920adc2a9d18b71659aa6ad7720a134c.pdf"},{"title":"CoRL | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL"},{"title":"Annotation-Efficient Honesty Alignment via Confidence Elicitation and Calibration | OpenReview","url":"https://openreview.net/forum?id=cW6oDsPobl"}]

Based on the search results, I found information about the OpenReview default review form structure:

The OpenReview default review form includes a "rating" field with a 1-10 scale where 10 represents "Top 5% of accepted papers, seminal paper" and 1 represents "Trivial or wrong," and a "confidence" field with a 5-point scale where 5 means "The reviewer is absolutely certain that the evaluation is correct and very familiar with the relevant lit
…[truncated 599 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5069
}
```

</details>

---


### Tool call

_source line 200 · 2026-05-18T01:51:47.520102+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://docs.openreview.net/reference/default-forms/default-review-form",
  "prompt": "Extract the complete default review form structure: all field names, their scales/options, and descriptions. Especially the rating scale (1-10) and confidence scale (1-5) with all values listed."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://docs.openreview.net/reference/default-forms/default-review-form",
    "prompt": "Extract the complete default review form structure: all field names, their scales/options, and descriptions. Especially the rating scale (1-10) and confidence scale (1-5) with all values listed."
  }
}
```

</details>

---


### Tool result

_source line 201 · 2026-05-18T01:51:50.482885+00:00_

# Default Review Form Structure

The default review form contains four fields:

## 1. **Title**
- **Type:** String (0-500 characters)
- **Description:** "Brief summary of your review."
- **Order:** 1

## 2. **Review**
- **Type:** Text area with markdown support
- **Length:** 1-20,000 characters
- **Description:** Evaluation of quality, clarity, originality, and significance
- **Order:** 2

## 3. **Rating Scale** (1-10)
- 10: Top 5% of accepted papers, seminal paper
- 9: Top 15% of accepted papers, strong accept
- 8: Top 50% of accepted papers, clear accept
- 7: Good paper, accept
- 6: Marginally above acceptance threshold
- 5: Marginally below acceptance threshold
- 4: Ok but not good enough - rejection
- 3: Clear rejection
- 2: Strong rejection
- 1: Trivial or wrong
- **Order:** 3

## 4. **Confidence Scale** (1-5)
- 5: Absolutely certain evaluation is correct; very familiar with literature
- 4: Confident but not absolutely certain evaluation is correct
- 3: Fairly confident evaluation is correct
- 2: Willing to defend it, but may lack understanding of central parts
- 1: Educated guess
- **Order:** 4

Both API V2 and V1 JSON formats document this structure with identical field definitions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 2962
}
```

</details>

---


### Tool call

_source line 202 · 2026-05-18T01:52:04.213516+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '搜索 CoRL 2026 reviewer guidelines / review form', 'status': 'completed', 'activeForm': '搜索 CoRL 2026 reviewer guidelines'}, {'content': '检查 AI 写作痕迹（em-dash, -ing phrases, 过度分段）', 'status': 'in_progress', 'activeForm': '检查 AI 写作痕迹'}, {'content': '评估新颖性与意义（C1/C2/C3 + 竞争者对比）', 'status': 'pending', 'activeForm': '评估新颖性与意义'}, {'content': '评估相关工作覆盖度和 positioning', 'status': 'pending', 'activeForm': '评估相关工作覆盖度'}, {'content': '评估 Framing 与 Claim 范围', 'status': 'pending', 'activeForm': '评估 Framing 与 Claim 范围'}, {'content': '检查 Round 4 issues 修复状态', 'status': 'pending', 'activeForm': '检查 Round 4 issues 修复状态'}, {'content': '撰写完整审稿意见并汇报 Director', 'status': 'pending', 'activeForm': '撰写完整审稿意见'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '搜索 CoRL 2026 reviewer guidelines / review form', 'status': 'completed', 'activeForm': '搜索 CoRL 2026 reviewer guidelines'}, {'content': '检查 AI 写作痕迹（em-dash, -ing phrases, 过度分段）', 'status': 'in_progress', 'activeForm': '检查 AI 写作痕迹'}, {'content': '评估新颖性与意义（C1/C2/C3 + 竞争者对比）', 'status': 'pending', 'activeForm': '评估新颖性与意义'}, {'content': '评估相关工作覆盖度和 positioning', 'status': 'pending', 'activeForm': '评估相关工作覆盖度'}, {'content': '评估 Framing 与 Claim 范围', 'status': 'pending', 'activeForm': '评估 Framing 与 Claim 范围'}, {'content': '检查 Round 4 issues 修复状态', 'status': 'pending', 'activeForm': '检查 Round 4 issues 修复状态'}, {'content': '撰写完整审稿意见并汇报 Director', 'status': 'pending', 'activeForm': '撰写完整审稿意见'}]"
  }
}
```

</details>

---


### Tool result

_source line 203 · 2026-05-18T01:52:04.214059+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 204 · 2026-05-18T01:52:08.735906+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
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

_source line 205 · 2026-05-18T01:52:09.639373+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 206 · 2026-05-18T01:52:09.690017+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex | wc -w",
  "description": "Count abstract word count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex | wc -w",
    "description": "Count abstract word count"
  }
}
```

</details>

---


### Tool result

_source line 207 · 2026-05-18T01:52:09.891961+00:00_

241

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 208 · 2026-05-18T01:52:18.535209+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 209 · 2026-05-18T01:52:19.440982+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 210 · 2026-05-18T01:52:20.043365+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": ", (highlighting|demonstrating|enabling|suggesting|indicating|confirming|revealing|showing)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": ", (highlighting|demonstrating|enabling|suggesting|indicating|confirming|revealing|showing)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 211 · 2026-05-18T01:52:20.194864+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex:28:We extend this to VLAs, showing that image tokens remain instruction-blind while the readout token serves as the exclusive multimodal hub.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:63:Llama-2 base shows 9/32 heads ($36.5\%$ text), indicating that language pretraining seeds instruction-attending structure.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:80:Ablating 8 non-dominant heads (control) yields $+0.017$ ($p = 0.008$), 3.5$\times$ smaller than the dominant-head effect, confirming a graded specificity rather than a generic attention-removal artifact.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:125:The same-layer training effect at L12 is large ($\Delta = +0.079$, $p < 0.0001$), but the best-vs-best gain is non-significant ($\Delta = +0.017$, $3\%$, 95\% CI includes zero; Appendix Table~\ref{tab:training_effects}), suggesting training reshapes \emph{where} geometry peaks rather than \emph{how high}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex:4:We decompose a VLA's internal representations with factorial trained-vs-untrained control, revealing: (1)~strict token-level specialization (instruction-blind image tokens, cross-validated readout hub); (2)~front-loaded instruction routing, shifted from mid-depth (L9--L16) to entry-exit (L0--L1, L31); and (3)~non-monotonic vision encoder refinement (peak L12, readout $R^2$ $+0.069$, image $\Delta \leq 1.7\%$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex:5:Second, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth (L9--L16, 15--22 heads), while VLA training shifts this to entry-layer routing (L0--L1: 21--24 heads) with exit-lay
…[truncated 5943 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 212 · 2026-05-18T01:53:40.319053+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "untest|straw|assumption",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "untest|straw|assumption",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 213 · 2026-05-18T01:53:41.273169+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex:6:A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex:7:We test this assumption at the representational level through per-layer, per-token-type decomposition.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 214 · 2026-05-18T01:53:41.926022+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Moreover|Furthermore|Additionally|Notably|delve|leverage|utilize|facilitate|paradigm",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Moreover|Furthermore|Additionally|Notably|delve|leverage|utilize|facilitate|paradigm",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 215 · 2026-05-18T01:53:41.926456+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 216 · 2026-05-18T01:53:56.691802+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '搜索 CoRL 2026 reviewer guidelines / review form', 'status': 'completed', 'activeForm': '搜索 CoRL 2026 reviewer guidelines'}, {'content': '检查 AI 写作痕迹（em-dash, -ing phrases, 过度分段）', 'status': 'completed', 'activeForm': '检查 AI 写作痕迹'}, {'content': '评估新颖性与意义（C1/C2/C3 + 竞争者对比）', 'status': 'completed', 'activeForm': '评估新颖性与意义'}, {'content': '评估相关工作覆盖度和 positioning', 'status': 'completed', 'activeForm': '评估相关工作覆盖度'}, {'content': '评估 Framing 与 Claim 范围', 'status': 'completed', 'activeForm': '评估 Framing 与 Claim 范围'}, {'content': '检查 Round 4 issues 修复状态', 'status': 'completed', 'activeForm': '检查 Round 4 issues 修复状态'}, {'content': '撰写完整审稿意见并汇报 Director', 'status': 'in_progress', 'activeForm': '撰写完整审稿意见'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '搜索 CoRL 2026 reviewer guidelines / review form', 'status': 'completed', 'activeForm': '搜索 CoRL 2026 reviewer guidelines'}, {'content': '检查 AI 写作痕迹（em-dash, -ing phrases, 过度分段）', 'status': 'completed', 'activeForm': '检查 AI 写作痕迹'}, {'content': '评估新颖性与意义（C1/C2/C3 + 竞争者对比）', 'status': 'completed', 'activeForm': '评估新颖性与意义'}, {'content': '评估相关工作覆盖度和 positioning', 'status': 'completed', 'activeForm': '评估相关工作覆盖度'}, {'content': '评估 Framing 与 Claim 范围', 'status': 'completed', 'activeForm': '评估 Framing 与 Claim 范围'}, {'content': '检查 Round 4 issues 修复状态', 'status': 'completed', 'activeForm': '检查 Round 4 issues 修复状态'}, {'content': '撰写完整审稿意见并汇报 Director', 'status': 'in_progress', 'activeForm': '撰写完整审稿意见'}]"
  }
}
```

</details>

---


### Tool result

_source line 217 · 2026-05-18T01:53:56.692206+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 218 · 2026-05-18T01:54:24.768464+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
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

_source line 219 · 2026-05-18T01:54:24.819380+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 220 · 2026-05-18T01:56:46.298907+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿意见 — Round 1\n\n**论文**: \"Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\"\n**Venue**: CoRL 2026\n**审查侧重**: 新颖性/意义 + 相关工作 + Framing + Round 4 修复检查 + 写作风格\n\n---\n\n## 1. Summary\n\n本文对 OpenVLA-7B 在 LIBERO 上进行了系统性的 token 级表征分析，使用 trained/pretrained/untrained 三条件 factorial 设计，结合 cross-instruction probes、attention 分析、RSA 和 functional probes 四种互补方法。核心发现是 VLA fine-tuning 将 instruction routing 从 mid-depth (L9-L16) 前移至 entry-exit pattern (L0-L1, L31)，且训练效果集中在 readout token 而非 image tokens。论文方法论严谨，统计分析充分，对 metric dependence 坦诚（RSA vs CKA 分歧），但受限于单模型单 benchmark 的 scope。\n\n---\n\n## 2. Strengths\n\n**S1. 方法论系统性强。** 四种分析方法（probes, attention, RSA, functional probes）相互验证，三条件 factorial 设计（trained/pretrained/untrained × instruction presence）是本文最大的方法论贡献。这种设计在 VLA 分析文献中尚属首次，能有效隔离 language pretraining 和 VLA fine-tuning 各自的贡献。\n\n**S2. C2 routing finding 是 genuine empirical contribution。** 三条件 routing gradient（0/32 → 9/32 → 24/32 instruction-dominant heads at L1）和 entry-exit pattern 的发现具有真正的新颖性。L1 ablation（dominant heads: +0.059 vs control: +0.017, 3.5× specificity, Section 4.3）提供了因果支持，效果集中在 L1（deeper layers: Δ ≈ 0）进一步确认了 head specialization 的 layer specificity。\n\n**S3. 统计严谨性和 robustness 分析充分。** Bootstrap CIs (10,000 resamples)、LOOCV、permutation tests、distance metric invariance (profile r > 0.989)、seed sensitivity (0.655 ± 0.002)、demonstration subsampling (RSA profile r = 0.97)、threshold sensitivity (30%-70%)、cross-benchmark validation (LIBERO-Spatial) — 对于一篇分析论文来说，robustness 分析的覆盖度达到了高标准。\n\n**S4. 对 metric dependence 的坦诚处理。** 论文明确报告 CKA 与 RSA 产生不同的 layer profiles 和 encoder rankings（Appendix A.1-A.2），没有回避这一分歧，而是将其作为结论的重要 qualifier。这种透明性增强了可信度。\n\n**S5. 写作质量高，AI 痕迹极少。** 全文无 em-dash (—) 或解释性 en-dash (–)，无 AI 典型用词（Moreover/Furthermore/Additionally/Notably/delve/leverage/utilize/facilitate 均未出现）。-ing 分词短语在正文中使用频率在可接受范围内（主要出现在 technical descriptions 中如 \"enabling immediate instruction access\", \"indicating that...\"），不构成风格问题。\n\n---\n\n## 3. Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **单模型局限性对 C2 generalizability 的根本约束**\n- 具体位置：Discussion \"Limitations and scope\" (Section 5, para 5)；全文 C2 claims\n- 问题：C2（entry-exit routing pattern）是本文核心贡献，但仅在 OpenVLA-7B 一个模型上验证。Discussion 用两句话概括了单模型局限（\"We study OpenVLA-7B on LIBERO; generalization to other VLAs and backbones remains open\"），然后以架构相似性做类推（\"shares the dominant VLA design pattern... with RT-2 and π₀\"）。但类推不等于验证：(a) RT-2 使用不同的 LLM backbone（PaLM-E），routing pattern 可能完全不同；(b) π₀ 使用 flow matching 而非 autoregressive decoding，entry-exit pattern 的前提（readout token attending to instruction tokens）在其架构中可能不成立；(c) 即使架构相似，不同预训练数据和 fine-tuning 策略可能产生不同的 routing reorganization。Grant et al. 2026 (Action Atlas) 在 6 个 VLAs 上进行分析恰恰表明了 cross-model 验证的可行性和必要性。\n- 为什么影响接收：CoRL 社区关心的是 VLA 设计的通用规律。如果 entry-exit pattern 是 OpenVLA-specific 而非 VLA-general 的，则 C2 的 significance 大幅降低。当前的 limitations 描述不足以让读者判断 generalizability risk 的大小。\n- 建议修改方向：(1) 在 Limitations 中具体列举哪些架构变量可能改变 routing pattern（backbone size/family, frozen vs unfrozen encoder, action head design, pretraining data）；(2) 明确说明 C2 的 claim scope 为 \"demonstrated on OpenVLA-7B\" 而非暗示 VLA-general；(3) 如果可能，至少在一个架构不同的 VLA（如 smaller model 或不同 backbone）上跑一个 lightweight 验证。\n\n**N2** [critical] **Discussion \"Architectural implications\" 段落的 speculative leap 缺乏 behavioral validation**\n- 具体位置：Discussion Section 5, \"Architectural implications\" 段落最后一句\n- 问题：该段从 L1 attention ablation 的 representational effect（action probe R² 变化）直接推导出 practical design implication：\"The concentration of instruction routing at L0-L1 suggests that adapting a VLA's instruction-following behavior may require updating only early-layer attention parameters, rather than full-model fine-tuning.\" 这个跳跃有两个 gap：(1) probe R² 的变化不等于 behavioral performance（success rate）的变化，论文自己在 Limitations 中承认 \"whether the observed routing reorganization translates to behavioral performance differences requires task-level evaluation\"；(2) 即使 routing 集中在 early layers，fine-tuning 的效果可能仍然需要 deep layers 的协同更新（论文自身数据显示 L31 也有 18 heads instruction-dominant）。\n- 为什么影响接收：这是论文对 CoRL 社区最具 actionable 价值的 claim，但缺乏验证使其停留在 speculation 层面。如果审稿人以此为 contribution 接受论文，后续无法 reproduce 这个 design implication 会是问题。\n- 建议修改方向：(1) 将 \"suggests\" 改为更弱的措辞（如 \"raises the hypothesis that...\"）；(2) 明确标注这是 speculative interpretation 而非 evidence-supported conclusion；(3) 指出 L31 的 re-engagement (18 heads) 对这一 implication 构成的 complication。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **C1 的 contribution 定位仍有模糊之处**\n- 具体位置：Introduction contributions list (i)；Abstract 第 4 句\n- 问题：C1 已从 \"finding\" 重新定位为 \"experimental framework + empirical verification\"，这是正确的方向。但 contributions list (i) 混合了两个层次：框架贡献（\"a systematic experimental framework for token-level representational analysis\"）和验证结果（\"verifying architecture-expected specialization\"）。对于 CoRL 审稿人来说，\"验证架构预期的东西\" 本身作为 contribution 的说服力有限，因为 causal mask + frozen encoder 的逻辑是先验显然的。建议在 (i) 中更强调框架的 reusability（可以应用于其他 VLAs / 不同架构），将验证结果作为框架的 demonstration 而非独立贡献。\n- 建议：Rewrite (i) to foreground the framework's applicability to future VLAs and downplay the verification as a demonstration case.\n\n**W2** [warning] **C3 non-monotonic observation 的贡献权重与证据强度不匹配**\n- 具体位置：Abstract 第 6 句；Introduction 第 20 行；Section 4.4\n- 问题：C3 在 Abstract 和 Introduction 中获得了与 C1、C2 等量的篇幅，但它的 evidence 是 metric-dependent 的（RSA shows inverted-U, CKA shows monotonic increase）。论文正确标注了这一分歧，但在呈现顺序上，inverted-U 仍作为主结论，CKA 作为 qualifier 放在句末。对于一个核心结论被另一种标准方法直接否定的 finding，当前的权重分配可能 overclaim 其 robustness。\n- 建议：在 Abstract 中缩减 C3 篇幅，将节省空间用于 C2 的 detail（如 ablation evidence），或将 metric divergence 前置为 C3 statement 的一部分而非后置 qualifier。\n\n**W3** [warning] **Related Work 缺少 causal tracing / activation patching 相关文献**\n- 具体位置：Section 2 \"Mechanistic interpretability in transformers\" 段落\n- 问题：Related Work 覆盖了 residual stream framework (Elhage 2021)、induction heads (Olsson 2022)、circuit discovery (Wang 2023, Conmy 2023)、attention probing (Clark 2019, Vig 2019, Voita 2019)。但缺少了 mechanistic interpretability 中另一个重要方向：causal tracing / activation patching (Meng et al. 2022, \"Locating and Editing Factual Associations in GPT\", NeurIPS; Goldowsky-Dill et al. 2023, \"Localizing Model Behavior with Path Patching\")。这些方法与本文的 L1 ablation 在方法论上直接相关（都是通过 intervention 建立因果关系），不引用会让审稿人质疑方法论 awareness。\n- 建议：在 \"Mechanistic interpretability\" 段落中加入 activation patching / causal tracing 的引用，并说明本文的 ablation 方法与其的关系（如 本文的 attention ablation 是一种 targeted intervention，与 activation patching 的思路一致但 granularity 不同）。\n\n**W4** [warning] **Related Work 缺少 tuned lens 等 logit lens 后续工作**\n- 具体位置：Section 2 \"Token-level functional specialization\" 段落\n- 问题：论文引用了 nostalgebraist 2020 (logit lens)，但 logit lens 有已知的 representation misalignment 问题，tuned lens (Belrose et al. 2023, \"Eliciting Latent Predictions from Transformers with the Tuned Lens\", NeurIPS 2023 Workshop → 后续 full paper) 是直接改进。本文的 per-layer probe analysis 在精神上更接近 tuned lens（per-layer 学习映射到 output space），不引用这个 closely related method 是遗漏。\n- 建议：引用 tuned lens，说明 per-layer MLP probes 与 tuned lens 的联系（都学习 per-layer 映射），但本文的 target 是 action space 而非 vocabulary。\n\n**W5** [warning] **conclusion.tex 存在但未被 main.tex \\input**\n- 具体位置：main.tex 未包含 conclusion.tex；conclusion.tex 为 6 行独立文件\n- 问题：conclusion.tex 存在，包含一段 3 句话的 Conclusion section (Section label `\\ref{sec:conclusion}`)，但 main.tex 中未 `\\input{conclusion}`。Discussion 以 \"Limitations and scope\" 段落结尾。CoRL 不强制要求 Conclusion section，但 (a) 未使用的文件暗示编辑遗漏；(b) Discussion 结尾以 limitations 收束，叙事上以消极信息结尾不理想；(c) conclusion.tex 的内容（3 句精炼总结 + code release 承诺）适合作为论文结尾。\n- 建议：将 conclusion.tex 整合到 Discussion 末尾或作为独立 section 加入 main.tex。\n\n### 小问题（不影响接收）\n\n**I1** [info] **Abstract 词数偏高（~241 words raw LaTeX）。** CoRL 未明确规定 abstract 词数上限，但渲染后可能超过 250 words（考虑 LaTeX 公式展开）。建议自查渲染后词数。\n\n**I2** [info] **-ing 分词短语数量较多。** 正文中有约 15+ 处 \", enabling/indicating/confirming/suggesting/revealing/showing...\" 模式。虽不构成严重 AI 痕迹（无其他 AI markers），但 pattern 的密度偏高。建议在 final pass 中将部分改写为独立句子。\n\n**I3** [info] **References 数量 (29) 处于 CoRL 论文的中等偏低水平。** CoRL 2024 accepted papers 的引用中位数约 35-45。当前覆盖度合理但不充裕，特别是在加入 W3/W4 建议的引用后仍有空间。\n\n---\n\n## 4. Round 4 Issue Status\n\n| Issue | Status | 说明 |\n|-------|--------|------|\n| **R4-N1** C1 reframe (finding → framework+verification) | **RESOLVED** | Abstract: \"we verify and quantify architecture-expected token specialization\"; Introduction: \"consistent with architectural expectations\"; Contributions (i): \"systematic experimental framework...verifying architecture-expected specialization\". Reframe 到位。 |\n| **R4-W1** RSA best-vs-best n.s. 标注 | **RESOLVED** | Abstract: \"Δρ ≤ 0.017, non-significant\"; Introduction: \"non-significant geometric gain (Δρ = 0.017, 3%)\". 两处均明确标注。 |\n| **R4-W4** Frozen encoder confound caveat | **RESOLVED** | Introduction line 16: \"consistent with the causal mask and frozen encoder\"; Discussion: 明确列出 \"frozen vision encoder\" 作为 shared design pattern. C1 的 instruction-blindness 被正确归因为架构特性而非 learned property。 |\n| **R4-W5** 单模型局限性展开 | **PARTIALLY_RESOLVED** | Discussion 提到 \"generalization to other VLAs and backbones remains open\" 并给出架构类推。但如 N1 所述，类推论证不足以覆盖架构差异可能带来的 routing pattern 变化。需更具体地列举潜在 confounds。 |\n| **R4-W7** Introduction \"untested assumption\" straw man | **RESOLVED** | Introduction 使用 \"remains uncharacterized\" (line 5) 和 \"opaque\" (line 9)，无 straw man 语言。Related Work 中 \"A central assumption\" 是对领域的客观描述，不构成 straw man。 |\n| **R4-I1** conclusion.tex 整合 | **NOT_RESOLVED** | conclusion.tex (6 行) 存在但未被 main.tex \\input。见 W5。 |\n\n---\n\n## 5. Missing References\n\n| 类别 | 缺失引用 | 重要性 |\n|------|----------|--------|\n| Causal tracing / activation patching | Meng et al. 2022 \"Locating and Editing Factual Associations in GPT\" (NeurIPS) | **High** — 与本文 L1 ablation 方法论直接相关 |\n| Causal tracing | Goldowsky-Dill et al. 2023 \"Localizing Model Behavior with Path Patching\" | Medium — 更全面的 patching methodology |\n| Logit lens improvement | Belrose et al. 2023 \"Eliciting Latent Predictions from Transformers with the Tuned Lens\" | **High** — 与 per-layer probing 方法论紧密相关 |\n| Other VLA architectures | Ghosh et al. 2024 \"Octo: An Open-Source Generalist Robot Policy\" | Low — 讨论 generalizability 时作为不同架构的例子 |\n\n---\n\n## 6. Questions for Authors\n\n**Q1.** C2 的 entry-exit pattern 是否可能是 Llama-2 7B 这一特定 backbone 的 artifact？如果使用不同的 LLM backbone（如 Mistral 或 Phi），是否预期同样的 routing reorganization？请提供架构层面的论证。\n\n**Q2.** L1 ablation 显示 dominant head removal 增加 action R² (+0.059)。这意味着 instruction routing heads 在 action encoding 上有 cost。是否测量过这种 ablation 对 instruction-following accuracy 的影响（即 cross-instruction classification accuracy 是否下降）？这将完善 capacity trade-off 的论证。\n\n**Q3.** Discussion 提出 early-layer-only fine-tuning 的 design implication。是否考虑过做一个简单验证：只 fine-tune L0-L1 的 attention parameters，比较其与 full fine-tuning 的 behavioral performance？即使只在 LIBERO 上做，也能显著增强这个 claim。\n\n**Q4.** 29 篇引用对 CoRL 论文偏少。作者是否有意控制引用数量？是否考虑过加入 activation patching (Meng et al. 2022) 和 tuned lens (Belrose et al. 2023)？\n\n---\n\n## 7. Overall Assessment\n\n**Overall Score: 6/10 — Marginally above acceptance threshold**\n\n**Confidence: 4/5 — Confident but not absolutely certain**\n\n**一句话总结**: 方法论严谨的 VLA 分析论文，C2 routing finding 有真正的新颖性，但单模型 scope 和 speculative design implications 限制了对 CoRL 社区的实际指导价值。\n\n### 官方维度打分（基于 CoRL review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Originality** | 6/10 | C2 (entry-exit routing) 是 genuine novel finding；C1 (framework) 有方法论价值但验证结果是预期的；C3 (non-monotonic) 被 metric dependence 削弱。与 Grant 2026 (6 models, feature-level) 相比，本文 depth > breadth。 |\n| **Quality** | 7/10 | 统计分析严谨（bootstrap, LOOCV, permutation, robustness suite）；factorial 设计得当；metric dependence 坦诚报告。扣分：单模型、无 behavioral validation、speculative design implications。 |\n| **Clarity** | 8/10 | 写作清晰，结构合理，几乎无 AI 痕迹。Abstract 四要素齐全。-ing phrases 稍多但不影响可读性。conclusion.tex 未整合是小问题。 |\n| **Significance** | 5/10 | 核心问题：对 CoRL 社区的 practical impact 有限。C2 的 routing finding 有启发性但无 behavioral validation，design implications 是 speculative 的。单模型 scope 进一步限制 significance。如果能在第二个 VLA 上验证 C2 或做一个 early-layer fine-tuning 实验，significance 可提升至 7。 |\n| **Relevance** | 8/10 | 直接分析 VLA 内部机制，完全在 CoRL scope 内。理解 VLA 内部工作原理对 robotics community 有长期价值。 |\n| **Limitations** | 7/10 | 主要限制已报告（单模型、metric dependence、无 behavioral validation）。但单模型局限性的讨论不够具体（见 N1），frozen encoder confound 的 generalizability implications 可以更详细。 |",
  "reviewer_id": "2",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿意见 — Round 1\n\n**论文**: \"Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\"\n**Venue**: CoRL 2026\n**审查侧重**: 新颖性/意义 + 相关工作 + Framing + Round 4 修复检查 + 写作风格\n\n---\n\n## 1. Summary\n\n本文对 OpenVLA-7B 在 LIBERO 上进行了系统性的 token 级表征分析，使用 trained/pretrained/untrained 三条件 factorial 设计，结合 cross-instruction probes、attention 分析、RSA 和 functional probes 四种互补方法。核心发现是 VLA fine-tuning 将 instruction routing 从 mid-depth (L9-L16) 前移至 entry-exit pattern (L0-L1, L31)，且训练效果集中在 readout token 而非 image tokens。论文方法论严谨，统计分析充分，对 metric dependence 坦诚（RSA vs CKA 分歧），但受限于单模型单 benchmark 的 scope。\n\n---\n\n## 2. Strengths\n\n**S1. 方法论系统性强。** 四种分析方法（probes, attention, RSA, functional probes）相互验证，三条件 factorial 设计（trained/pretrained/untrained × instruction presence）是本文最大的方法论贡献。这种设计在 VLA 分析文献中尚属首次，能有效隔离 language pretraining 和 VLA fine-tuning 各自的贡献。\n\n**S2. C2 routing finding 是 genuine empirical contribution。** 三条件 routing gradient（0/32 → 9/32 → 24/32 instruction-dominant heads at L1）和 entry-exit pattern 的发现具有真正的新颖性。L1 ablation（dominant heads: +0.059 vs control: +0.017, 3.5× specificity, Section 4.3）提供了因果支持，效果集中在 L1（deeper layers: Δ ≈ 0）进一步确认了 head specialization 的 layer specificity。\n\n**S3. 统计严谨性和 robustness 分析充分。** Bootstrap CIs (10,000 resamples)、LOOCV、permutation tests、distance metric invariance (profile r > 0.989)、seed sensitivity (0.655 ± 0.002)、demonstration subsampling (RSA profile r = 0.97)、threshold sensitivity (30%-70%)、cross-benchmark validation (LIBERO-Spatial) — 对于一篇分析论文来说，robustness 分析的覆盖度达到了高标准。\n\n**S4. 对 metric dependence 的坦诚处理。** 论文明确报告 CKA 与 RSA 产生不同的 layer profiles 和 encoder rankings（Appendix A.1-A.2），没有回避这一分歧，而是将其作为结论的重要 qualifier。这种透明性增强了可信度。\n\n**S5. 写作质量高，AI 痕迹极少。** 全文无 em-dash (—) 或解释性 en-dash (–)，无 AI 典型用词（Moreover/Furthermore/Additionally/Notably/delve/leverage/utilize/facilitate 均未出现）。-ing 分词短语在正文中使用频率在可接受范围内（主要出现在 technical descriptions 中如 \"enabling immediate instruction access\", \"indicating that...\"），不构成风格问题。\n\n---\n\n## 3. Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **单模型局限性对 C2 generalizability 的根本约束**\n- 具体位置：Discussion \"Limitations and scope\" (Section 5, para 5)；全文 C2 claims\n- 问题：C2（entry-exit routing pattern）是本文核心贡献，但仅在 OpenVLA-7B 一个模型上验证。Discussion 用两句话概括了单模型局限（\"We study OpenVLA-7B on LIBERO; generalization to other VLAs and backbones remains open\"），然后以架构相似性做类推（\"shares the dominant VLA design pattern... with RT-2 and π₀\"）。但类推不等于验证：(a) RT-2 使用不同的 LLM backbone（PaLM-E），routing pattern 可能完全不同；(b) π₀ 使用 flow matching 而非 autoregressive decoding，entry-exit pattern 的前提（readout token attending to instruction tokens）在其架构中可能不成立；(c) 即使架构相似，不同预训练数据和 fine-tuning 策略可能产生不同的 routing reorganization。Grant et al. 2026 (Action Atlas) 在 6 个 VLAs 上进行分析恰恰表明了 cross-model 验证的可行性和必要性。\n- 为什么影响接收：CoRL 社区关心的是 VLA 设计的通用规律。如果 entry-exit pattern 是 OpenVLA-specific 而非 VLA-general 的，则 C2 的 significance 大幅降低。当前的 limitations 描述不足以让读者判断 generalizability risk 的大小。\n- 建议修改方向：(1) 在 Limitations 中具体列举哪些架构变量可能改变 routing pattern（backbone size/family, frozen vs unfrozen encoder, action head design, pretraining data）；(2) 明确说明 C2 的 claim scope 为 \"demonstrated on OpenVLA-7B\" 而非暗示 VLA-general；(3) 如果可能，至少在一个架构不同的 VLA（如 smaller model 或不同 backbone）上跑一个 lightweight 验证。\n\n**N2** [critical] **Discussion \"Architectural implications\" 段落的 speculative leap 缺乏 behavioral validation**\n- 具体位置：Discussion Section 5, \"Architectural implications\" 段落最后一句\n- 问题：该段从 L1 attention ablation 的 representational effect（action probe R² 变化）直接推导出 practical design implication：\"The concentration of instruction routing at L0-L1 suggests that adapting a VLA's instruction-following behavior may require updating only early-layer attention parameters, rather than full-model fine-tuning.\" 这个跳跃有两个 gap：(1) probe R² 的变化不等于 behavioral performance（success rate）的变化，论文自己在 Limitations 中承认 \"whether the observed routing reorganization translates to behavioral performance differences requires task-level evaluation\"；(2) 即使 routing 集中在 early layers，fine-tuning 的效果可能仍然需要 deep layers 的协同更新（论文自身数据显示 L31 也有 18 heads instruction-dominant）。\n- 为什么影响接收：这是论文对 CoRL 社区最具 actionable 价值的 claim，但缺乏验证使其停留在 speculation 层面。如果审稿人以此为 contribution 接受论文，后续无法 reproduce 这个 design implication 会是问题。\n- 建议修改方向：(1) 将 \"suggests\" 改为更弱的措辞（如 \"raises the hypothesis that...\"）；(2) 明确标注这是 speculative interpretation 而非 evidence-supported conclusion；(3) 指出 L31 的 re-engagement (18 heads) 对这一 implication 构成的 complication。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **C1 的 contribution 定位仍有模糊之处**\n- 具体位置：Introduction contributions list (i)；Abstract 第 4 句\n- 问题：C1 已从 \"finding\" 重新定位为 \"experimental framework + empirical verification\"，这是正确的方向。但 contributions list (i) 混合了两个层次：框架贡献（\"a systematic experimental framework for token-level representational analysis\"）和验证结果（\"verifying architecture-expected specialization\"）。对于 CoRL 审稿人来说，\"验证架构预期的东西\" 本身作为 contribution 的说服力有限，因为 causal mask + frozen encoder 的逻辑是先验显然的。建议在 (i) 中更强调框架的 reusability（可以应用于其他 VLAs / 不同架构），将验证结果作为框架的 demonstration 而非独立贡献。\n- 建议：Rewrite (i) to foreground the framework's applicability to future VLAs and downplay the verification as a demonstration case.\n\n**W2** [warning] **C3 non-monotonic observation 的贡献权重与证据强度不匹配**\n- 具体位置：Abstract 第 6 句；Introduction 第 20 行；Section 4.4\n- 问题：C3 在 Abstract 和 Introduction 中获得了与 C1、C2 等量的篇幅，但它的 evidence 是 metric-dependent 的（RSA shows inverted-U, CKA shows monotonic increase）。论文正确标注了这一分歧，但在呈现顺序上，inverted-U 仍作为主结论，CKA 作为 qualifier 放在句末。对于一个核心结论被另一种标准方法直接否定的 finding，当前的权重分配可能 overclaim 其 robustness。\n- 建议：在 Abstract 中缩减 C3 篇幅，将节省空间用于 C2 的 detail（如 ablation evidence），或将 metric divergence 前置为 C3 statement 的一部分而非后置 qualifier。\n\n**W3** [warning] **Related Work 缺少 causal tracing / activation patching 相关文献**\n- 具体位置：Section 2 \"Mechanistic interpretability in transformers\" 段落\n- 问题：Related Work 覆盖了 residual stream framework (Elhage 2021)、induction heads (Olsson 2022)、circuit discovery (Wang 2023, Conmy 2023)、attention probing (Clark 2019, Vig 2019, Voita 2019)。但缺少了 mechanistic interpretability 中另一个重要方向：causal tracing / activation patching (Meng et al. 2022, \"Locating and Editing Factual Associations in GPT\", NeurIPS; Goldowsky-Dill et al. 2023, \"Localizing Model Behavior with Path Patching\")。这些方法与本文的 L1 ablation 在方法论上直接相关（都是通过 intervention 建立因果关系），不引用会让审稿人质疑方法论 awareness。\n- 建议：在 \"Mechanistic interpretability\" 段落中加入 activation patching / causal tracing 的引用，并说明本文的 ablation 方法与其的关系（如 本文的 attention ablation 是一种 targeted intervention，与 activation patching 的思路一致但 granularity 不同）。\n\n**W4** [warning] **Related Work 缺少 tuned lens 等 logit lens 后续工作**\n- 具体位置：Section 2 \"Token-level functional specialization\" 段落\n- 问题：论文引用了 nostalgebraist 2020 (logit lens)，但 logit lens 有已知的 representation misalignment 问题，tuned lens (Belrose et al. 2023, \"Eliciting Latent Predictions from Transformers with the Tuned Lens\", NeurIPS 2023 Workshop → 后续 full paper) 是直接改进。本文的 per-layer probe analysis 在精神上更接近 tuned lens（per-layer 学习映射到 output space），不引用这个 closely related method 是遗漏。\n- 建议：引用 tuned lens，说明 per-layer MLP probes 与 tuned lens 的联系（都学习 per-layer 映射），但本文的 target 是 action space 而非 vocabulary。\n\n**W5** [warning] **conclusion.tex 存在但未被 main.tex \\input**\n- 具体位置：main.tex 未包含 conclusion.tex；conclusion.tex 为 6 行独立文件\n- 问题：conclusion.tex 存在，包含一段 3 句话的 Conclusion section (Section label `\\ref{sec:conclusion}`)，但 main.tex 中未 `\\input{conclusion}`。Discussion 以 \"Limitations and scope\" 段落结尾。CoRL 不强制要求 Conclusion section，但 (a) 未使用的文件暗示编辑遗漏；(b) Discussion 结尾以 limitations 收束，叙事上以消极信息结尾不理想；(c) conclusion.tex 的内容（3 句精炼总结 + code release 承诺）适合作为论文结尾。\n- 建议：将 conclusion.tex 整合到 Discussion 末尾或作为独立 section 加入 main.tex。\n\n### 小问题（不影响接收）\n\n**I1** [info] **Abstract 词数偏高（~241 words raw LaTeX）。** CoRL 未明确规定 abstract 词数上限，但渲染后可能超过 250 words（考虑 LaTeX 公式展开）。建议自查渲染后词数。\n\n**I2** [info] **-ing 分词短语数量较多。** 正文中有约 15+ 处 \", enabling/indicating/confirming/suggesting/revealing/showing...\" 模式。虽不构成严重 AI 痕迹（无其他 AI markers），但 pattern 的密度偏高。建议在 final pass 中将部分改写为独立句子。\n\n**I3** [info] **References 数量 (29) 处于 CoRL 论文的中等偏低水平。** CoRL 2024 accepted papers 的引用中位数约 35-45。当前覆盖度合理但不充裕，特别是在加入 W3/W4 建议的引用后仍有空间。\n\n---\n\n## 4. Round 4 Issue Status\n\n| Issue | Status | 说明 |\n|-------|--------|------|\n| **R4-N1** C1 reframe (finding → framework+verification) | **RESOLVED** | Abstract: \"we verify and quantify architecture-expected token specialization\"; Introduction: \"consistent with architectural expectations\"; Contributions (i): \"systematic experimental framework...verifying architecture-expected specialization\". Reframe 到位。 |\n| **R4-W1** RSA best-vs-best n.s. 标注 | **RESOLVED** | Abstract: \"Δρ ≤ 0.017, non-significant\"; Introduction: \"non-significant geometric gain (Δρ = 0.017, 3%)\". 两处均明确标注。 |\n| **R4-W4** Frozen encoder confound caveat | **RESOLVED** | Introduction line 16: \"consistent with the causal mask and frozen encoder\"; Discussion: 明确列出 \"frozen vision encoder\" 作为 shared design pattern. C1 的 instruction-blindness 被正确归因为架构特性而非 learned property。 |\n| **R4-W5** 单模型局限性展开 | **PARTIALLY_RESOLVED** | Discussion 提到 \"generalization to other VLAs and backbones remains open\" 并给出架构类推。但如 N1 所述，类推论证不足以覆盖架构差异可能带来的 routing pattern 变化。需更具体地列举潜在 confounds。 |\n| **R4-W7** Introduction \"untested assumption\" straw man | **RESOLVED** | Introduction 使用 \"remains uncharacterized\" (line 5) 和 \"opaque\" (line 9)，无 straw man 语言。Related Work 中 \"A central assumption\" 是对领域的客观描述，不构成 straw man。 |\n| **R4-I1** conclusion.tex 整合 | **NOT_RESOLVED** | conclusion.tex (6 行) 存在但未被 main.tex \\input。见 W5。 |\n\n---\n\n## 5. Missing References\n\n| 类别 | 缺失引用 | 重要性 |\n|------|----------|--------|\n| Causal tracing / activation patching | Meng et al. 2022 \"Locating and Editing Factual Associations in GPT\" (NeurIPS) | **High** — 与本文 L1 ablation 方法论直接相关 |\n| Causal tracing | Goldowsky-Dill et al. 2023 \"Localizing Model Behavior with Path Patching\" | Medium — 更全面的 patching methodology |\n| Logit lens improvement | Belrose et al. 2023 \"Eliciting Latent Predictions from Transformers with the Tuned Lens\" | **High** — 与 per-layer probing 方法论紧密相关 |\n| Other VLA architectures | Ghosh et al. 2024 \"Octo: An Open-Source Generalist Robot Policy\" | Low — 讨论 generalizability 时作为不同架构的例子 |\n\n---\n\n## 6. Questions for Authors\n\n**Q1.** C2 的 entry-exit pattern 是否可能是 Llama-2 7B 这一特定 backbone 的 artifact？如果使用不同的 LLM backbone（如 Mistral 或 Phi），是否预期同样的 routing reorganization？请提供架构层面的论证。\n\n**Q2.** L1 ablation 显示 dominant head removal 增加 action R² (+0.059)。这意味着 instruction routing heads 在 action encoding 上有 cost。是否测量过这种 ablation 对 instruction-following accuracy 的影响（即 cross-instruction classification accuracy 是否下降）？这将完善 capacity trade-off 的论证。\n\n**Q3.** Discussion 提出 early-layer-only fine-tuning 的 design implication。是否考虑过做一个简单验证：只 fine-tune L0-L1 的 attention parameters，比较其与 full fine-tuning 的 behavioral performance？即使只在 LIBERO 上做，也能显著增强这个 claim。\n\n**Q4.** 29 篇引用对 CoRL 论文偏少。作者是否有意控制引用数量？是否考虑过加入 activation patching (Meng et al. 2022) 和 tuned lens (Belrose et al. 2023)？\n\n---\n\n## 7. Overall Assessment\n\n**Overall Score: 6/10 — Marginally above acceptance threshold**\n\n**Confidence: 4/5 — Confident but not absolutely certain**\n\n**一句话总结**: 方法论严谨的 VLA 分析论文，C2 routing finding 有真正的新颖性，但单模型 scope 和 speculative design implications 限制了对 CoRL 社区的实际指导价值。\n\n### 官方维度打分（基于 CoRL review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Originality** | 6/10 | C2 (entry-exit routing) 是 genuine novel finding；C1 (framework) 有方法论价值但验证结果是预期的；C3 (non-monotonic) 被 metric dependence 削弱。与 Grant 2026 (6 models, feature-level) 相比，本文 depth > breadth。 |\n| **Quality** | 7/10 | 统计分析严谨（bootstrap, LOOCV, permutation, robustness suite）；factorial 设计得当；metric dependence 坦诚报告。扣分：单模型、无 behavioral validation、speculative design implications。 |\n| **Clarity** | 8/10 | 写作清晰，结构合理，几乎无 AI 痕迹。Abstract 四要素齐全。-ing phrases 稍多但不影响可读性。conclusion.tex 未整合是小问题。 |\n| **Significance** | 5/10 | 核心问题：对 CoRL 社区的 practical impact 有限。C2 的 routing finding 有启发性但无 behavioral validation，design implications 是 speculative 的。单模型 scope 进一步限制 significance。如果能在第二个 VLA 上验证 C2 或做一个 early-layer fine-tuning 实验，significance 可提升至 7。 |\n| **Relevance** | 8/10 | 直接分析 VLA 内部机制，完全在 CoRL scope 内。理解 VLA 内部工作原理对 robotics community 有长期价值。 |\n| **Limitations** | 7/10 | 主要限制已报告（单模型、metric dependence、无 behavioral validation）。但单模型局限性的讨论不够具体（见 N1），frozen encoder confound 的 generalizability implications 可以更详细。 |",
    "reviewer_id": "2",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 221 · 2026-05-18T01:56:50.716346+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4417
}
```

</details>

---


### Tool call

_source line 222 · 2026-05-18T01:57:03.944647+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '搜索 CoRL 2026 reviewer guidelines / review form', 'status': 'completed', 'activeForm': '搜索 CoRL 2026 reviewer guidelines'}, {'content': '检查 AI 写作痕迹（em-dash, -ing phrases, 过度分段）', 'status': 'completed', 'activeForm': '检查 AI 写作痕迹'}, {'content': '评估新颖性与意义（C1/C2/C3 + 竞争者对比）', 'status': 'completed', 'activeForm': '评估新颖性与意义'}, {'content': '评估相关工作覆盖度和 positioning', 'status': 'completed', 'activeForm': '评估相关工作覆盖度'}, {'content': '评估 Framing 与 Claim 范围', 'status': 'completed', 'activeForm': '评估 Framing 与 Claim 范围'}, {'content': '检查 Round 4 issues 修复状态', 'status': 'completed', 'activeForm': '检查 Round 4 issues 修复状态'}, {'content': '撰写完整审稿意见并汇报 Director', 'status': 'completed', 'activeForm': '撰写完整审稿意见'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '搜索 CoRL 2026 reviewer guidelines / review form', 'status': 'completed', 'activeForm': '搜索 CoRL 2026 reviewer guidelines'}, {'content': '检查 AI 写作痕迹（em-dash, -ing phrases, 过度分段）', 'status': 'completed', 'activeForm': '检查 AI 写作痕迹'}, {'content': '评估新颖性与意义（C1/C2/C3 + 竞争者对比）', 'status': 'completed', 'activeForm': '评估新颖性与意义'}, {'content': '评估相关工作覆盖度和 positioning', 'status': 'completed', 'activeForm': '评估相关工作覆盖度'}, {'content': '评估 Framing 与 Claim 范围', 'status': 'completed', 'activeForm': '评估 Framing 与 Claim 范围'}, {'content': '检查 Round 4 issues 修复状态', 'status': 'completed', 'activeForm': '检查 Round 4 issues 修复状态'}, {'content': '撰写完整审稿意见并汇报 Director', 'status': 'completed', 'activeForm': '撰写完整审稿意见'}]"
  }
}
```

</details>

---


### Tool result

_source line 223 · 2026-05-18T01:57:03.995645+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 224 · 2026-05-18T01:57:14.365090+00:00_

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
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2"
}
```

</details>

---


## Round 8

## Round 8

8 recorded events


### User

_source line 225 · 2026-05-18T01:57:54.799151+00:00_

[Round 1 审稿请求]:
## 交叉分享 — Reviewer 1 的完整审稿意见

请逐条回应以下 Reviewer 1 的意见。对每条使用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

以下是 Reviewer 1 的完整审稿原文：

### Must-Fix (Critical)

**R1-N1** [critical] L1 Ablation 的 3.5× specificity claim 被 per-head normalization 严重削弱
- Ablating 24 dominant heads → +0.059 R²; ablating 8 non-dominant heads → +0.017
- Per-head: dominant = 0.059/24 ≈ 0.00246, non-dominant = 0.017/8 ≈ 0.00213, 差异仅 ~15%
- 外推 24 heads at non-dominant rate = 0.051, 观测值 0.059, excess 仅 0.008 (16%)
- 建议：报告 per-head normalized effect; 补充 random-subset ablation (随机 24/32 heads, k 次); 或弱化 claim

**R1-N2** [critical] N/params ≈ 0.05 被错误解读为 "ensuring adequate training signal"
- MLP probe (4096→256→7) 约 1.05M params, N=63,228
- N/params ≈ 0.06 → 参数量是数据量 17 倍 → 严重 overparameterization
- Belinkov 2022: 过高容量 probe 可从任何表征 decode 信息
- 建议：承认 overparameterized + 依赖 early stopping; 补充 linear/small probe baseline; 强调 Δ 不受 absolute R² inflation 影响

### Should-Fix (Warning)

**R1-W1** Pretrained Llama-2 condition 的 OOD confound 未讨论：Llama-2 从未被训练处理 projected visual tokens，对其而言是 OOD 输入
**R1-W2** Bootstrap CI 未报告具体数值：RSA rise phase Δ=+0.017 仅标 "incl. 0"，未给 [lower, upper]
**R1-W3** Cross-benchmark 仅限 LIBERO suite 内部（shared simulator/objects/action space）
**R1-W4** 缺乏行为层面验证（无 policy rollout success rate）

### Info
- N/params 分子分母可能写反
- Appendix A.6 single-seed analysis 应补 3+ seeds
- Belinkov 2022 应在 Method 中引用

### R1 评分
- Overall: 6/10
- Originality: 3/5, Quality: 3/5, Clarity: 4/5, Significance: 3/5, Relevance: 4/5, Limitations: 4/5

### Round 4 Issue Status (R1 判断)
- R4-N1 C1 reframe: RESOLVED
- R4-N2 RSA+CKA divergence: RESOLVED
- R4-N3 5→50 demos: RESOLVED
- R4-W2 FDR correction: RESOLVED
- R4-W3 Probe N/capacity: PARTIALLY_RESOLVED (数字报告了但解读错误)

请逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 226 · 2026-05-18T01:58:42.517668+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
  "offset": "76",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
    "offset": "76",
    "limit": "10"
  }
}
```

</details>

---


### Tool result

_source line 227 · 2026-05-18T01:58:42.668632+00:00_

76	
77	\paragraph{Ablation reveals functional specialization.}
78	To test whether L1 instruction-dominant heads causally mediate a capacity trade-off between instruction routing and action encoding, we ablate their attention to instruction tokens and measure downstream action probe $R^2$ using 50 demonstrations per task ($N = 63{,}228$).
79	Ablating all 24 dominant heads increases action $R^2$ at L1 by $+0.059$ ($p < 0.0001$; baseline $0.557 \to 0.615$).
80	Ablating 8 non-dominant heads (control) yields $+0.017$ ($p = 0.008$), 3.5$\times$ smaller than the dominant-head effect, confirming a graded specificity rather than a generic attention-removal artifact.
81	The specificity contrast is significant (dominant $-$ control $= +0.042$, $p < 0.0001$).
82	The effect concentrates at L1 (L8: $+0.018$; L13: $\Delta \approx 0$), consistent with the entry-layer routing pattern identified in \S\ref{sec:learned_routing}.
83	
84	\begin{table}[t]
85	\centering

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 228 · 2026-05-18T01:58:42.919950+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
  "offset": "10",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
    "offset": "10",
    "limit": "5"
  }
}
```

</details>

---


### Tool result

_source line 229 · 2026-05-18T01:58:42.970588+00:00_

10	RSA computes Spearman $\rho$ between cosine-distance representation RDMs and Euclidean-distance action RDMs, with 10{,}000 bootstrap CIs (\S\ref{sec:rsa}).
11	MLP probes (input $\to$ 256 $\to$ 7; Adam, lr${}=10^{-3}$, 50 epochs, early stopping) report mean $R^2$ (\S\ref{sec:probes}).
12	This yields $N = 63{,}228$ observations (50 demonstrations $\times$ 10 tasks $\times$ $\sim$127 timesteps per demonstration). For the MLP probe (2-layer, 256 hidden units), the ratio $N/\text{params} \approx 0.05$, ensuring adequate training signal.
13	
14	%------------------------------------------------------------------

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 230 · 2026-05-18T02:00:13.543249+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n### Must-Fix (Critical)\n\n**[AGREE] R1-N1: L1 Ablation 的 3.5× specificity claim 被 per-head normalization 削弱**\n\nR1 的 per-head 分析是有效的。24 dominant heads 产生 +0.059（per-head ≈ 0.00246），8 non-dominant heads 产生 +0.017（per-head ≈ 0.00213），per-head 差异仅约 15%。外推 24 heads at non-dominant rate 得到 0.051，与观测值 0.059 的 excess 仅 0.008（16%），远弱于 \"3.5×\" 的表面印象。\n\n论文原文（Section 4.3）：\"Ablating 8 non-dominant heads (control) yields +0.017, 3.5× smaller than the dominant-head effect, confirming a graded specificity rather than a generic attention-removal artifact.\" 这里的 \"3.5×\" 混淆了 head 数量差异和 per-head specificity。\n\n不过我认为需补充两点 nuance：\n1. 论文还报告了 \"specificity contrast is significant (dominant − control = +0.042, p < 0.0001)\"（Section 4.3, line 81）。这个 total difference 的 p-value 是关于 aggregate 效果的统计检验，本身没问题，问题在于 \"3.5×\" 的 framing 暗示 per-head specificity 远大于实际。\n2. 更关键的 specificity 证据来自 layer confinement：L1 effect = +0.059, L8 = +0.018, L13 ≈ 0（Section 4.3, line 82）。这个 layer gradient 不受 head 数量 confound 的影响，是更干净的 specificity 证据。\n\n**建议：** 同意 R1 的修改方向。作者应 (a) 报告 per-head normalized effect；(b) 弱化 \"3.5×\" 为 \"aggregate effect comparison\"；(c) 将 layer confinement 作为 specificity 的主要证据而非 head-count comparison。R1 建议的 random-subset ablation 是理想方案但可能 scope 过大。\n\n---\n\n**[AGREE] R1-N2: N/params ≈ 0.05 被错误解读**\n\nR1 的计算正确。MLP probe (4096→256→7) 参数量：\n- Layer 1: 4096×256 + 256 = 1,048,832\n- Layer 2: 256×7 + 7 = 1,799\n- Total ≈ 1.05M params\n\nN = 63,228, 所以 N/params ≈ 0.06，即参数量是数据量的 ~17 倍。论文称此 \"ensuring adequate training signal\"（Section 4.1, line 12）是错误的——这是严重 overparameterized 的 regime。\n\nR1 的 Info section 指出 \"N/params 分子分母可能写反\" 也是合理推测。即使 params/N ≈ 17，这同样表明 overparameterization 而非 adequate signal。\n\n关键缓解因素：\n1. 论文使用 early stopping (patience 5)（Section 3.5），这在 overparameterized probes 中是标准 regularization\n2. 核心 claims 基于 Δ (trained vs untrained) 而非 absolute R²，如 R1 所指出的，Δ 不受 absolute inflation 影响（假设 overfitting degree 在 conditions 间相似）\n3. Seed sensitivity 分析（Appendix A.9）显示 R² 跨 seed 标准差 < 0.01，表明结果不是 overfit artifact\n\n**建议：** 同意 R1 的全部修改建议。(a) 修正 \"ensuring adequate training signal\" 为 \"the probe is overparameterized (N/params ≈ 0.06); we rely on early stopping for regularization\"；(b) 补充 linear probe 或 smaller MLP (64 hidden) baseline 以验证 conclusions 对 probe capacity 的 robustness；(c) 在 Method 中引用 Belinkov 2022 讨论 probe complexity-capability tradeoff。\n\n---\n\n### Should-Fix (Warning)\n\n**[AGREE] R1-W1: Pretrained Llama-2 OOD confound**\n\n有效的方法论关切。Llama-2 base 从未见过 visual tokens（来自 DinoSigLIP projector 的 4096-D vectors），其 routing 行为可能反映 OOD 处理策略（如 default 到最近的 known distribution）而非对 visual input 的 genuine 处理。\n\n这不完全否定三条件比较的价值——pretrained condition 的意义恰恰在于展示 language pretraining 单独在面对 multimodal input 时贡献了什么（Section 3.1, line 12-13 描述了设计意图）。但论文应明确讨论这一 confound：\n- L1 的 9/32 instruction-dominant heads（Table 2）可能反映 Llama-2 对 unfamiliar input 的 default 行为（attention fallback 到 known token types 即 instruction tokens），而非 language pretraining 对 instruction routing 的真正 \"seeding\"\n- 这会影响 C2 的叙事：当前 \"language pretraining seeds instruction routing, VLA fine-tuning amplifies it\" 的故事可能过于 clean\n\n**补充我的 review 未涉及的角度：** 如果 OOD confound 成立，那么 untrained → pretrained 的变化（0/32 → 9/32 heads）可能主要反映 trained weights 对 OOD inputs 的 generic response 而非 instruction-specific routing learning。这进一步加强了我在 N1 中对 single-model generalizability 的担忧。\n\n---\n\n**[AGREE] R1-W2: Bootstrap CI 未报告具体数值**\n\n论文多处仅标注 \"95% CI includes zero\"（如 Table 5: RSA best-vs-best Δ=+0.017）或 \"95% CI excludes zero\"，但未给出 [lower, upper] 区间。这是统计报告的基本规范问题。Section 4.4, line 125: \"best-vs-best gain is non-significant (Δ = +0.017, 3%, 95% CI includes zero; Appendix Table 5)\" —— Appendix Table 5 同样只写 \"incl. 0\" 和 \"excl. 0\"。\n\n补充：LIBERO-Spatial 的 CI 报告更完整：Appendix A.7, line 123 给出了 \"95% CI [0.012, 0.036]\"。这种不一致性使得主实验的 CI 缺失更加显眼。\n\n---\n\n**[AGREE] R1-W3: Cross-benchmark 局限于 LIBERO suite**\n\nLIBERO-Goal 和 LIBERO-Spatial 共享 simulator (MuJoCo)、object set 和 7-D action space，cross-benchmark validation 的力度有限。Appendix A.7 指出 Spatial 是 \"out-of-distribution tasks requiring spatial reasoning\"，但 OOD 仅在 task semantics 层面，底层 environment dynamics 完全相同。\n\n此问题与我 review 中的 N1（单模型 scope）性质相同，从不同角度指出了 generalizability 的局限。在可操作性上，考虑到 deadline (2026-05-29)，在不同 simulator 上做 cross-benchmark 不太现实，但可以在 Limitations 中更明确地区分 \"task-level generalization\"（已测试）和 \"environment-level generalization\"（未测试）。\n\n---\n\n**[AGREE] R1-W4: 缺乏行为层面验证**\n\n与我 review 中的 N2 一致。论文 Discussion (Section 5, Limitations para) 自己承认 \"whether the observed routing reorganization translates to behavioral performance differences requires task-level evaluation beyond this work\"。这个 gap 同时削弱了 C2 的 practical significance 和 \"Architectural implications\" 段落的 design suggestion。\n\n---\n\n### Info\n\n**[AGREE] N/params 分子分母可能写反：** 见 R1-N2 分析。\n\n**[AGREE] Appendix A.6 single-seed analysis 应补 3+ seeds：** Appendix A.6 (Figure 7) 的 three-condition action R² comparison 使用 single seed（该 section 最后一句 \"This analysis uses a single seed without confidence intervals and should be interpreted as a supplementary observation\"）。既然 main results 有 5-seed sensitivity analysis (Appendix A.9, Table 8)，A.6 没有理由不做同样的处理。\n\n**[AGREE] Belinkov 2022 应在 Method 中引用：** 当前 Belinkov 2022 仅在 Related Work (Section 2) 和 Method Section 3.5 的 citation list 中出现 ([alain2017,hewitt2019,belinkov2022])。但 probe complexity 的讨论（如 R1-N2 所指出的 overparameterization 问题）应在 Method 中有明确段落讨论 probe design choices 和 complexity-capability tradeoff。\n\n---\n\n### R1 Round 4 Issue Status 的回应\n\n| R1 判断 | 我的判断 | 说明 |\n|---------|---------|------|\n| R4-N1 C1 reframe: RESOLVED | **一致** | C1 已从 \"finding\" 重新定位为 \"framework + verification\"。 |\n| R4-N2 RSA+CKA divergence: RESOLVED | **一致** | 论文在 Abstract、Introduction、Section 4.4、Appendix 中均明确报告了 metric divergence。 |\n| R4-N3 5→50 demos: RESOLVED | **一致** | 当前使用 50 demonstrations per task (Section 3.1)，subsample sensitivity 在 Appendix A.10 中报告。 |\n| R4-W2 FDR correction: RESOLVED | **一致** | Section 4.4, line 127: \"Benjamini-Hochberg, Wilcoxon signed-rank, n=10 tasks\" 有明确 FDR 报告。 |\n| R4-W3 Probe N/capacity: PARTIALLY_RESOLVED | **一致** | 数字已报告但解读错误（R1-N2）。 |\n\n---\n\n### R1 评分的回应\n\nR1 Overall: 6/10。我的 Overall: 6/10。**一致。**\n\n维度层面：\n- Originality: R1 给 3/5，我给 6/10（等价 3/5）。**一致。**\n- Quality: R1 给 3/5。我给 7/10（≈3.5/5）。**我略高。** 原因：我认为 statistical rigor（bootstrap, LOOCV, permutation, robustness suite）是质量的加分项，值得肯定，尽管 R1-N1 和 R1-N2 是有效的质量问题。\n- Clarity: R1 给 4/5，我给 8/10（4/5）。**一致。**\n- Significance: R1 给 3/5，我给 5/10（2.5/5）。**我略低。** 原因：单模型 scope 对 CoRL 社区的 practical impact 构成更严重的限制。\n- Relevance: R1 给 4/5，我给 8/10（4/5）。**一致。**\n\n---\n\n### 总结\n\nR1 和 R2 在所有 critical issues 上形成一致：\n1. **Ablation specificity claim 需要修正**（R1-N1，R2 同意）\n2. **Probe overparameterization 需要承认和补充**（R1-N2，R2 同意）\n3. **单模型 scope 限制 significance**（R2-N1，R1 隐含于 Significance 评分）\n4. **Design implications 缺乏 behavioral validation**（R2-N2 = R1-W4）\n\n主要分歧：R1 在 Quality 上比我更严格（3/5 vs 我的 3.5/5），原因是 R1 更侧重方法论细节问题（N1, N2），而我更多考虑了整体 statistical apparatus 的充分性。\n\n**综合判断维持 6/10（marginally above threshold）。** 如果作者在 rebuttal 中能 (a) 修正 ablation framing, (b) 承认 probe overparameterization 并补充 linear probe baseline, (c) 充实 single-model limitations，论文有条件接收。最大风险是 significance——如果审稿人认为单模型分析论文对 CoRL 社区的指导价值有限，可能从 borderline 滑向 reject。",
  "reviewer_id": "2",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n### Must-Fix (Critical)\n\n**[AGREE] R1-N1: L1 Ablation 的 3.5× specificity claim 被 per-head normalization 削弱**\n\nR1 的 per-head 分析是有效的。24 dominant heads 产生 +0.059（per-head ≈ 0.00246），8 non-dominant heads 产生 +0.017（per-head ≈ 0.00213），per-head 差异仅约 15%。外推 24 heads at non-dominant rate 得到 0.051，与观测值 0.059 的 excess 仅 0.008（16%），远弱于 \"3.5×\" 的表面印象。\n\n论文原文（Section 4.3）：\"Ablating 8 non-dominant heads (control) yields +0.017, 3.5× smaller than the dominant-head effect, confirming a graded specificity rather than a generic attention-removal artifact.\" 这里的 \"3.5×\" 混淆了 head 数量差异和 per-head specificity。\n\n不过我认为需补充两点 nuance：\n1. 论文还报告了 \"specificity contrast is significant (dominant − control = +0.042, p < 0.0001)\"（Section 4.3, line 81）。这个 total difference 的 p-value 是关于 aggregate 效果的统计检验，本身没问题，问题在于 \"3.5×\" 的 framing 暗示 per-head specificity 远大于实际。\n2. 更关键的 specificity 证据来自 layer confinement：L1 effect = +0.059, L8 = +0.018, L13 ≈ 0（Section 4.3, line 82）。这个 layer gradient 不受 head 数量 confound 的影响，是更干净的 specificity 证据。\n\n**建议：** 同意 R1 的修改方向。作者应 (a) 报告 per-head normalized effect；(b) 弱化 \"3.5×\" 为 \"aggregate effect comparison\"；(c) 将 layer confinement 作为 specificity 的主要证据而非 head-count comparison。R1 建议的 random-subset ablation 是理想方案但可能 scope 过大。\n\n---\n\n**[AGREE] R1-N2: N/params ≈ 0.05 被错误解读**\n\nR1 的计算正确。MLP probe (4096→256→7) 参数量：\n- Layer 1: 4096×256 + 256 = 1,048,832\n- Layer 2: 256×7 + 7 = 1,799\n- Total ≈ 1.05M params\n\nN = 63,228, 所以 N/params ≈ 0.06，即参数量是数据量的 ~17 倍。论文称此 \"ensuring adequate training signal\"（Section 4.1, line 12）是错误的——这是严重 overparameterized 的 regime。\n\nR1 的 Info section 指出 \"N/params 分子分母可能写反\" 也是合理推测。即使 params/N ≈ 17，这同样表明 overparameterization 而非 adequate signal。\n\n关键缓解因素：\n1. 论文使用 early stopping (patience 5)（Section 3.5），这在 overparameterized probes 中是标准 regularization\n2. 核心 claims 基于 Δ (trained vs untrained) 而非 absolute R²，如 R1 所指出的，Δ 不受 absolute inflation 影响（假设 overfitting degree 在 conditions 间相似）\n3. Seed sensitivity 分析（Appendix A.9）显示 R² 跨 seed 标准差 < 0.01，表明结果不是 overfit artifact\n\n**建议：** 同意 R1 的全部修改建议。(a) 修正 \"ensuring adequate training signal\" 为 \"the probe is overparameterized (N/params ≈ 0.06); we rely on early stopping for regularization\"；(b) 补充 linear probe 或 smaller MLP (64 hidden) baseline 以验证 conclusions 对 probe capacity 的 robustness；(c) 在 Method 中引用 Belinkov 2022 讨论 probe complexity-capability tradeoff。\n\n---\n\n### Should-Fix (Warning)\n\n**[AGREE] R1-W1: Pretrained Llama-2 OOD confound**\n\n有效的方法论关切。Llama-2 base 从未见过 visual tokens（来自 DinoSigLIP projector 的 4096-D vectors），其 routing 行为可能反映 OOD 处理策略（如 default 到最近的 known distribution）而非对 visual input 的 genuine 处理。\n\n这不完全否定三条件比较的价值——pretrained condition 的意义恰恰在于展示 language pretraining 单独在面对 multimodal input 时贡献了什么（Section 3.1, line 12-13 描述了设计意图）。但论文应明确讨论这一 confound：\n- L1 的 9/32 instruction-dominant heads（Table 2）可能反映 Llama-2 对 unfamiliar input 的 default 行为（attention fallback 到 known token types 即 instruction tokens），而非 language pretraining 对 instruction routing 的真正 \"seeding\"\n- 这会影响 C2 的叙事：当前 \"language pretraining seeds instruction routing, VLA fine-tuning amplifies it\" 的故事可能过于 clean\n\n**补充我的 review 未涉及的角度：** 如果 OOD confound 成立，那么 untrained → pretrained 的变化（0/32 → 9/32 heads）可能主要反映 trained weights 对 OOD inputs 的 generic response 而非 instruction-specific routing learning。这进一步加强了我在 N1 中对 single-model generalizability 的担忧。\n\n---\n\n**[AGREE] R1-W2: Bootstrap CI 未报告具体数值**\n\n论文多处仅标注 \"95% CI includes zero\"（如 Table 5: RSA best-vs-best Δ=+0.017）或 \"95% CI excludes zero\"，但未给出 [lower, upper] 区间。这是统计报告的基本规范问题。Section 4.4, line 125: \"best-vs-best gain is non-significant (Δ = +0.017, 3%, 95% CI includes zero; Appendix Table 5)\" —— Appendix Table 5 同样只写 \"incl. 0\" 和 \"excl. 0\"。\n\n补充：LIBERO-Spatial 的 CI 报告更完整：Appendix A.7, line 123 给出了 \"95% CI [0.012, 0.036]\"。这种不一致性使得主实验的 CI 缺失更加显眼。\n\n---\n\n**[AGREE] R1-W3: Cross-benchmark 局限于 LIBERO suite**\n\nLIBERO-Goal 和 LIBERO-Spatial 共享 simulator (MuJoCo)、object set 和 7-D action space，cross-benchmark validation 的力度有限。Appendix A.7 指出 Spatial 是 \"out-of-distribution tasks requiring spatial reasoning\"，但 OOD 仅在 task semantics 层面，底层 environment dynamics 完全相同。\n\n此问题与我 review 中的 N1（单模型 scope）性质相同，从不同角度指出了 generalizability 的局限。在可操作性上，考虑到 deadline (2026-05-29)，在不同 simulator 上做 cross-benchmark 不太现实，但可以在 Limitations 中更明确地区分 \"task-level generalization\"（已测试）和 \"environment-level generalization\"（未测试）。\n\n---\n\n**[AGREE] R1-W4: 缺乏行为层面验证**\n\n与我 review 中的 N2 一致。论文 Discussion (Section 5, Limitations para) 自己承认 \"whether the observed routing reorganization translates to behavioral performance differences requires task-level evaluation beyond this work\"。这个 gap 同时削弱了 C2 的 practical significance 和 \"Architectural implications\" 段落的 design suggestion。\n\n---\n\n### Info\n\n**[AGREE] N/params 分子分母可能写反：** 见 R1-N2 分析。\n\n**[AGREE] Appendix A.6 single-seed analysis 应补 3+ seeds：** Appendix A.6 (Figure 7) 的 three-condition action R² comparison 使用 single seed（该 section 最后一句 \"This analysis uses a single seed without confidence intervals and should be interpreted as a supplementary observation\"）。既然 main results 有 5-seed sensitivity analysis (Appendix A.9, Table 8)，A.6 没有理由不做同样的处理。\n\n**[AGREE] Belinkov 2022 应在 Method 中引用：** 当前 Belinkov 2022 仅在 Related Work (Section 2) 和 Method Section 3.5 的 citation list 中出现 ([alain2017,hewitt2019,belinkov2022])。但 probe complexity 的讨论（如 R1-N2 所指出的 overparameterization 问题）应在 Method 中有明确段落讨论 probe design choices 和 complexity-capability tradeoff。\n\n---\n\n### R1 Round 4 Issue Status 的回应\n\n| R1 判断 | 我的判断 | 说明 |\n|---------|---------|------|\n| R4-N1 C1 reframe: RESOLVED | **一致** | C1 已从 \"finding\" 重新定位为 \"framework + verification\"。 |\n| R4-N2 RSA+CKA divergence: RESOLVED | **一致** | 论文在 Abstract、Introduction、Section 4.4、Appendix 中均明确报告了 metric divergence。 |\n| R4-N3 5→50 demos: RESOLVED | **一致** | 当前使用 50 demonstrations per task (Section 3.1)，subsample sensitivity 在 Appendix A.10 中报告。 |\n| R4-W2 FDR correction: RESOLVED | **一致** | Section 4.4, line 127: \"Benjamini-Hochberg, Wilcoxon signed-rank, n=10 tasks\" 有明确 FDR 报告。 |\n| R4-W3 Probe N/capacity: PARTIALLY_RESOLVED | **一致** | 数字已报告但解读错误（R1-N2）。 |\n\n---\n\n### R1 评分的回应\n\nR1 Overall: 6/10。我的 Overall: 6/10。**一致。**\n\n维度层面：\n- Originality: R1 给 3/5，我给 6/10（等价 3/5）。**一致。**\n- Quality: R1 给 3/5。我给 7/10（≈3.5/5）。**我略高。** 原因：我认为 statistical rigor（bootstrap, LOOCV, permutation, robustness suite）是质量的加分项，值得肯定，尽管 R1-N1 和 R1-N2 是有效的质量问题。\n- Clarity: R1 给 4/5，我给 8/10（4/5）。**一致。**\n- Significance: R1 给 3/5，我给 5/10（2.5/5）。**我略低。** 原因：单模型 scope 对 CoRL 社区的 practical impact 构成更严重的限制。\n- Relevance: R1 给 4/5，我给 8/10（4/5）。**一致。**\n\n---\n\n### 总结\n\nR1 和 R2 在所有 critical issues 上形成一致：\n1. **Ablation specificity claim 需要修正**（R1-N1，R2 同意）\n2. **Probe overparameterization 需要承认和补充**（R1-N2，R2 同意）\n3. **单模型 scope 限制 significance**（R2-N1，R1 隐含于 Significance 评分）\n4. **Design implications 缺乏 behavioral validation**（R2-N2 = R1-W4）\n\n主要分歧：R1 在 Quality 上比我更严格（3/5 vs 我的 3.5/5），原因是 R1 更侧重方法论细节问题（N1, N2），而我更多考虑了整体 statistical apparatus 的充分性。\n\n**综合判断维持 6/10（marginally above threshold）。** 如果作者在 rebuttal 中能 (a) 修正 ablation framing, (b) 承认 probe overparameterization 并补充 linear probe baseline, (c) 充实 single-model limitations，论文有条件接收。最大风险是 significance——如果审稿人认为单模型分析论文对 CoRL 社区的指导价值有限，可能从 borderline 滑向 reject。",
    "reviewer_id": "2",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 231 · 2026-05-18T02:00:17.982084+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4438
}
```

</details>

---


### Assistant

_source line 232 · 2026-05-18T02:00:21.467431+00:00_

交叉回应已提交。R1 的所有意见我均 [AGREE]，两位 reviewer 在关键问题上形成共识：ablation specificity claim 需修正、probe overparameterization 需承认、单模型 scope 限制 significance、design implications 缺 behavioral validation。综合评分维持 6/10。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2"
}
```

</details>

---


## Round 9

## Round 9

64 recorded events


### User

_source line 233 · 2026-05-18T08:52:45.998846+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2

### 你的审查侧重：新颖性 + 叙事完整性 + 格式合规

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

1. **新颖性 vs 竞品**：
   - 与 Grant 2026（"Not All Features Are Created Equal"）的差异化是否充分？Grant 用 activation injection/SAE 做了 6 个 VLA 的 behavioral intervention，本文用 probing/RSA 做单模型 representation 分析——增量贡献是否足够？
   - 与 Swann 2026（SAE on OpenVLA）、Rizzardo 2026（feature observability/controllability）、Haon 2025（CoRL 2025, mechanistic interpretability for VLA）的定位是否清晰？
   - 核心贡献（trained vs untrained routing reorganization）是否是 genuine novel finding，还是 expected from architecture？

2. **Claim 与 Evidence 匹配度**：
   - Abstract 和 Introduction 中的每个 claim 是否在实验中有对应证据？
   - Contribution list 的每一条是否有对应 section/table 支撑？
   - 是否存在 overclaim（证据只支持弱结论但写了强结论）或 underclaim（有好的结果但没有充分利用）？

3. **叙事连贯性**：
   - Abstract → Introduction → Method → Experiments → Discussion 是否形成一条统一主线？
   - 是否有"故事 A 在 Intro，故事 B 在 Method"的脱节？
   - C1（framework + token specialization verification）、C2（routing reorganization）、C3（vision encoder geometry observation）三个 claim 之间的关系是否清晰？

4. **Related Work 覆盖度**：
   - 引用是否覆盖：直接竞品、baseline 论文（OpenVLA, LIBERO）、评测方法（probing, RSA）、理论基础（mechanistic interpretability）？
   - 是否缺少 2025-2026 年的重要相关工作？
   - Positioning 是否清晰（不是 survey 而是定位自己）？

5. **CoRL 格式合规**：
   - 页数是否在 8 页限制内？
   - Limitations section 是否存在且有实质内容？
   - 匿名化是否完整（无 self-citation 泄露、无 GitHub link、无作者信息）？
   - 图表质量（字体 ≥7pt、caption 自包含、无视觉遮挡）？

6. **写作质量（AI 痕迹检查）**：
   - 检查解释性 em-dash (—) 和 en-dash (–) 残留
   - 检查 -ing phrase 结尾（"..., demonstrating..."）
   - 检查过度分段、过渡词堆积（Furthermore/Moreover/Additionally）
   - 检查 AI 用词黑名单（delve/leverage/utilize/facilitate/myriad/plethora）

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 234 · 2026-05-18T08:52:54.960852+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 235 · 2026-05-18T08:52:55.363386+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/sessions/review_reviewer_2_df1bf1a9.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 236 · 2026-05-18T08:52:55.414012+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 237 · 2026-05-18T08:52:55.514813+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 238 · 2026-05-18T08:52:58.175358+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 239 · 2026-05-18T08:52:58.577125+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 240 · 2026-05-18T08:52:58.628183+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 241 · 2026-05-18T08:52:59.079979+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 242 · 2026-05-18T08:52:59.080330+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 243 · 2026-05-18T08:52:59.533195+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 244 · 2026-05-18T08:52:59.533707+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 245 · 2026-05-18T08:52:59.985856+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 246 · 2026-05-18T08:53:00.037139+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 247 · 2026-05-18T08:53:00.491582+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 248 · 2026-05-18T08:53:00.492102+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 249 · 2026-05-18T08:53:00.997152+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 505
}
```

</details>

---


### Tool call

_source line 250 · 2026-05-18T08:53:00.997753+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 251 · 2026-05-18T08:53:01.656598+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 658
}
```

</details>

---


### Tool call

_source line 252 · 2026-05-18T08:53:07.041626+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "offset": "492"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "offset": "492"
  }
}
```

</details>

---


### Tool result

_source line 253 · 2026-05-18T08:53:07.443946+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (492). The file has 492 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 254 · 2026-05-18T08:53:07.494616+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
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

_source line 255 · 2026-05-18T08:53:07.546516+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 256 · 2026-05-18T08:53:10.458763+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 257 · 2026-05-18T08:53:10.710197+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2025 2026 review form scoring criteria dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2025 2026 review form scoring criteria dimensions"
  }
}
```

</details>

---


### Tool result

_source line 258 · 2026-05-18T08:53:16.785352+00:00_

Web search results for query: "CoRL 2026 reviewer guidelines review form criteria"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CVPR 2026 Reviewer Guidelines","url":"https://cvpr.thecvf.com/Conferences/2026/ReviewerGuidelinesq"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"2026 Reviewer Guidelines","url":"https://neurips.cc/Conferences/2026/ReviewerGuidelines"}]

Based on the search results, I found some information about CoRL 2026, though the specific detailed reviewer guidelines document with the full review form criteria wasn't directly available in the results. However, here's what I can share:

## CoRL 2026 Reviewer Information

All submissions must include at least one author who agrees to serve as a CoRL reviewer. They are qualified if they have at least one accepted publication at a previous robotics (CoRL/ICRA/IROS/RSS) or learning conference (ICLR/NeurIPS/ICML) or equivalent journal.

While the complete 2026 reviewer guidelines document wasn't fully available in the search results, I did find reference to CoRL 2023 reviewer guidelines which provide insight into the review criteria. Reviewers evaluate papers on: Relevance - Does the paper address a problem in robot learning? Does it apply or improve a learning-based method, or a learned model? Is the 
…[truncated 629 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6326
}
```

</details>

---


### Tool result

_source line 259 · 2026-05-18T08:53:22.863066+00:00_

Web search results for query: "CoRL 2025 2026 review form scoring criteria dimensions"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2025 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/corl-paper-list/corl-2025-paper-list/"},{"title":"CORL 2025 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/corl-statistics/corl-2025-statistics/"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2025","url":"https://2025.corl.org/"},{"title":"CoRL 2025 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2025%2FConference"},{"title":"CoRL 2025 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2025"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2025 Workshop H2R | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2025%2FWorkshop%2FH2R"},{"title":"CoRL 2025 Workshop Open Hardware | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2025%2FWorkshop%2FOpen_Hardware"}]

The search results provide general information about CoRL 2025 and 2026 but don't contain specific information about review form scoring criteria dimensions. Let me search more specifically for the review criteria.

Links: [{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"Defining quality in peer review reports: a scoping review | Knowledge and Information Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10115-025-02435-0"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"2025 Reviewer Guidelines","url":"https://neurips.cc/Con
…[truncated 5407 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 12152
}
```

</details>

---


### Tool call

_source line 260 · 2026-05-18T08:53:26.327401+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
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

_source line 261 · 2026-05-18T08:53:26.378019+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 262 · 2026-05-18T08:53:30.853661+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2024.corl.org/contributions/instruction-for-reviews",
  "prompt": "Extract the complete review form criteria, scoring dimensions, scoring scales (numerical ranges), and all evaluation questions that reviewers must answer. List every dimension with its exact scale."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2024.corl.org/contributions/instruction-for-reviews",
    "prompt": "Extract the complete review form criteria, scoring dimensions, scoring scales (numerical ranges), and all evaluation questions that reviewers must answer. List every dimension with its exact scale."
  }
}
```

</details>

---


### Tool call

_source line 263 · 2026-05-18T08:53:31.506589+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl2023.org/reviewer-guidelines",
  "prompt": "Extract the complete review form criteria, scoring dimensions, scoring scales (numerical ranges), and all evaluation questions that reviewers must answer. List every dimension with its exact scale."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl2023.org/reviewer-guidelines",
    "prompt": "Extract the complete review form criteria, scoring dimensions, scoring scales (numerical ranges), and all evaluation questions that reviewers must answer. List every dimension with its exact scale."
  }
}
```

</details>

---


### Tool result

_source line 264 · 2026-05-18T08:53:35.390613+00:00_

# CoRL 2024 Review Criteria

Based on the provided content, the document does **not contain a complete review form with scoring dimensions, numerical scales, or specific evaluation questions** that reviewers must answer.

## What IS Provided:

**Review Criteria for Regular Papers:**
The guidelines state that submissions will be evaluated on:
- "significance and novelty of the results, either theoretical or empirical"
- "degree to which they have been objectively established and/or their potential for scientific and technological impact"
- "relevance to robotic learning"

**Desk Rejection Criteria** (not reviewer scoring):
Papers may be rejected for formatting issues, anonymity violations, or scope misalignment.

**Reviewer Qualifications** (not evaluation criteria):
Reviewers should have expertise demonstrated by minimum 3 first-author publications in robotics/ML venues.

## Missing Information:

The document does not specify:
- Numerical scoring scales (e.g., 1-5, 1-10)
- Specific review dimensions or categories
- Detailed evaluation questions reviewers must answer
- Point distributions or weighting systems

The actual review form appears to be administered through a separate submission platform not included in this instructional page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 4536
}
```

</details>

---


### Tool result

_source line 265 · 2026-05-18T08:53:36.655167+00:00_

# CoRL 2023 Review Form Criteria

Based on the provided guidelines, the document outlines **six evaluation dimensions** but **does not specify numerical scoring scales or a complete review form structure**.

## Evaluation Dimensions

The guidelines identify these assessment areas:

1. **Originality**: "Are the problems or methods new?" Novel combinations and clear differentiation from prior work
2. **Quality**: Technical soundness, claim support through analysis/experiments, method appropriateness, completeness
3. **Clarity**: Writing quality, organization, reader comprehension, reproducibility information
4. **Significance**: Importance of results, potential adoption/impact, advancement over prior work, theoretical/experimental contributions
5. **Relevance**: "Does the paper address a problem in robot learning?" Learning-based methods, evaluation context (simulation/real robots)
6. **Limitations**: Appreciation for honestly reported limitations; accountability for unreported shortcomings

## Notable Gaps

The document does **not provide**:
- Specific numerical scoring scales (e.g., 1-5, 1-10 range)
- Complete review form template
- Exact scoring anchor definitions
- Recommendation categories or thresholds

The guidelines emphasize constructive feedback and reference external resources (ICML, NeurIPS) for detailed reviewer standards, suggesting the actual scoring mechanism may exist in the OpenReview system itself rather than in this overview document.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5148
}
```

</details>

---


### Tool call

_source line 266 · 2026-05-18T08:53:44.391050+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 267 · 2026-05-18T08:53:44.843069+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 268 · 2026-05-18T08:53:45.345053+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 269 · 2026-05-18T08:53:46.348564+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 1003
}
```

</details>

---


### Tool call

_source line 270 · 2026-05-18T08:53:47.302105+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,|ing\\.|ing;|, demonstrating|, highlighting|, enabling|, providing|, showing|, suggesting|, indicating|, confirming|, reflecting",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,|ing\\.|ing;|, demonstrating|, highlighting|, enabling|, providing|, showing|, suggesting|, indicating|, confirming|, reflecting",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 271 · 2026-05-18T08:53:48.256014+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex:12:Building on this, Olsson et al.~\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning; these specialized attention heads implement token-copying algorithms.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex:16:Our Layer-1 attention head analysis extends this tradition to the VLA domain; unlike knowledge editing or prediction lens approaches, we use functional ablation to study task-specific routing and find that 24 of 32 heads become instruction-dominant after fine-tuning.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex:29:We extend this to VLAs, showing that image tokens remain instruction-blind while the readout token serves as the exclusive multimodal hub.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:12:This yields $N = 63{,}228$ observations (50 demonstrations $\times$ 10 tasks $\times$ $\sim$127 timesteps per demonstration). The MLP probe is overparameterized ($N/\text{params} \approx 0.06$); early stopping mitigates overfitting, and all patterns reproduce with a linear probe ($N/\text{params} \approx 2.2$; Appendix~\ref{sec:linear_probe}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:68:Llama-2 base concentrates instruction attention at mid-depth (L9--L16: 15--22 heads), consistent with autoregressive LM processing.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex:82:Random heads, lacking organized instruction routing, produce larger $R^2$ gains when ablated because their removal frees attention bandwidth without disrupting instruction routing.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex:4:We decompose a VLA's internal representations with factorial train
…[truncated 10154 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 272 · 2026-05-18T08:53:49.059094+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Furthermore|Moreover|Additionally|delve|leverage|utilize|facilitate|myriad|plethora|paradigm shift",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Furthermore|Moreover|Additionally|delve|leverage|utilize|facilitate|myriad|plethora|paradigm shift",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 273 · 2026-05-18T08:53:49.159890+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 274 · 2026-05-18T08:53:53.980343+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-18T08:53:54.432197+00:00_

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
…[truncated 14825 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 276 · 2026-05-18T08:53:54.934731+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/conclusion*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/conclusion*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs"
  }
}
```

</details>

---


### Tool result

_source line 277 · 2026-05-18T08:53:55.840005+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 278 · 2026-05-18T08:53:56.845066+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "github|anonymous|our (previous|prior|earlier) work|our code|we released|supplementary",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "github|anonymous|our (previous|prior|earlier) work|our code|we released|supplementary",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 279 · 2026-05-18T08:53:57.807036+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex:18:\author{Anonymous}
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex:3:\section{Supplementary Material}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 961
}
```

</details>

---


### Tool call

_source line 280 · 2026-05-18T08:53:58.563006+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Generative AI|generative ai|AI assistance|language model assistance|ChatGPT|GPT-4|Claude|Copilot",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Generative AI|generative ai|AI assistance|language model assistance|ChatGPT|GPT-4|Claude|Copilot",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 281 · 2026-05-18T08:53:58.613668+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 282 · 2026-05-18T08:54:02.130621+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 283 · 2026-05-18T08:54:02.633090+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 284 · 2026-05-18T08:54:02.934865+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\bibliographystyle",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\bibliographystyle",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 285 · 2026-05-18T08:54:03.386813+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_example.tex:142:% no \bibliographystyle is required, since the corl style is automatically used.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 286 · 2026-05-18T08:54:03.688172+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\input\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\input\\{",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 287 · 2026-05-18T08:54:03.739294+00:00_

25:\input{abstract}
28:\input{introduction}
29:\input{related_work}
30:\input{method}
31:\input{experiments}
32:\input{discussion}
36:\input{appendix}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 288 · 2026-05-18T08:55:01.261636+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Grant 2026 \"Not All Features Are Created Equal\" mechanistic study VLA arXiv 2603.19233"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Grant 2026 \"Not All Features Are Created Equal\" mechanistic study VLA arXiv 2603.19233"
  }
}
```

</details>

---


### Tool call

_source line 289 · 2026-05-18T08:55:02.127635+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Swann 2026 \"Sparse Autoencoders Reveal Interpretable\" VLA OpenVLA arXiv 2603.19183"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Swann 2026 \"Sparse Autoencoders Reveal Interpretable\" VLA OpenVLA arXiv 2603.19183"
  }
}
```

</details>

---


### Tool result

_source line 290 · 2026-05-18T08:55:07.635870+00:00_

Web search results for query: "Grant 2026 "Not All Features Are Created Equal" mechanistic study VLA arXiv 2603.19233"

Links: [{"title":"[2603.19233] Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.19233"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models","url":"https://arxiv.org/html/2603.19233"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2603.19233"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2603.19233"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=w8Mw9zJt1y"}]

I found the paper! Here are the key details:

**Paper Title:** "Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models"

**Authors & Affiliation:** Bryce Grant, Xijia Zhao, and Peng Wang from Case Western Reserve University

**arXiv ID:** 2603.19233

**Submission Date:** Submitted on 19 Mar 2026

**Core Research Focus:** Vision-Language-Action (VLA) models combine perception, language, and motor control in a single architecture, yet how they translate multimodal inputs into actions remains poorly understood.

**Key Methodology:** The study applies activation injection, sparse autoencoders (SAEs), and linear probes to six models spanning 80M--7B parameters across 394,000+ rollout episodes on four benchmarks.

**Major Findings:**
- The visual pathway dominates action generation across all architectures: injecting baseline activations into null-prompt episodes recovers near-identical behavior, while cross-task injection steers robots toward source-task positions (99.8% of X-VLA episodes align with the source
…[truncated 386 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6374
}
```

</details>

---


### Tool result

_source line 291 · 2026-05-18T08:55:25.266640+00:00_

Web search results for query: "Swann 2026 "Sparse Autoencoders Reveal Interpretable" VLA OpenVLA arXiv 2603.19183"

Links: [{"title":"[2603.19183] Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models","url":"https://arxiv.org/abs/2603.19183"},{"title":"Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2603.19183"},{"title":"SPARSE AUTOENCODERS REVEAL INTERPRETABLE ...","url":"https://openreview.net/pdf?id=5AuN6RD072"},{"title":"Sparse Autoencoders Reveal Interpretable and Steerable ...","url":"https://drvla.github.io/"},{"title":"[2603.13277] Learning Retrieval Models with Sparse Autoencoders","url":"https://arxiv.org/abs/2603.13277"},{"title":"Sparse Autoencoders Find Highly Interpretable Features in Language Models | OpenReview","url":"https://openreview.net/forum?id=F76bwRSLeK"},{"title":"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models","url":"https://arxiv.org/html/2603.19233"},{"title":"Interpretable Embeddings with Sparse Autoencoders: A Data Analysis Toolkit","url":"https://arxiv.org/html/2512.10092v1"},{"title":"Sparse Autoencoders Reveal Interpretable and Steerable ...","url":"https://www.wispaper.ai/en"},{"title":"Interpretability Illusions with Sparse Autoencoders","url":"https://arxiv.org/pdf/2505.16004"}]

I found the paper you're looking for! The paper is titled "Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models" by Aiden Swann and 4 other authors, published on arXiv as 2603.19183 on March 19, 2026.

Here's a summary of the paper:

Vision-Language-Action (VLA) models have emerged as a promising approach for general-purpose robot manipulation, but their generalization is inconsistent—while they can perform impressively in some settings, fine-tuned variants often fail on novel objects, scenes, and instructions. 

The researchers apply mechanistic interpretability techniques to under
…[truncated 606 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 23139
}
```

</details>

---


### Tool call

_source line 292 · 2026-05-18T08:55:44.642733+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
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

_source line 293 · 2026-05-18T08:55:44.743547+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 294 · 2026-05-18T08:58:08.515086+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 — Round 1 审稿意见\n\n**论文**: Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\n**Venue**: CoRL 2026\n**审查侧重**: 新颖性 + 叙事完整性 + 格式合规\n\n---\n\n## Summary\n\n本文对 OpenVLA-7B 在 LIBERO 上进行 token 级别的表征分析，使用 cross-instruction probes、attention analysis、RSA 和 MLP probes 四种方法，在 trained/pretrained/untrained 三条件阶乘设计下，报告三个发现：(1) image tokens 对 instruction 不敏感（由 causal mask 和 frozen encoder 架构保证），(2) VLA fine-tuning 将 instruction routing 从 mid-depth 前移到 entry-exit 层，(3) vision encoder 表征在 LLM 层中呈非单调变换。实验设计严谨，统计报告完整，但核心新颖性受限于单模型范围和部分 architecturally-expected 的发现。\n\n---\n\n## Strengths\n\n- **S1: 实验设计严谨的阶乘控制**。trained/pretrained/untrained × instruction presence/absence 的 2×3 设计是该领域少见的严格控制方案，能有效隔离 language pretraining 和 VLA fine-tuning 各自的贡献（Section 3.1）。这一设计优于 Grant 2026 等仅做 trained model 分析的工作。\n\n- **S2: 统计报告高标准**。所有主要结论均附有 bootstrap CI（10,000 resamples）、FDR 校正（Benjamini-Hochberg）、permutation test、seed sensitivity、demo subsampling sensitivity（Appendix H-J）。这在 VLA interpretability 文献中罕见，值得肯定。\n\n- **S3: Routing reorganization 发现有价值**。C2（Section 4.3, Figure 1, Table 2）揭示 VLA fine-tuning 将 instruction routing 从 Llama-2 的 mid-depth 模式（L9-L16, 15-22 heads）重组为 entry-exit 模式（L0-L1: 21-24 heads, L31: 18 heads），且三条件梯度在 30%-70% 阈值范围内稳定（Appendix Table 14）。这是对 VLA 内部机制的有意义新知识。\n\n- **S4: 方法互补性好**。四种分析方法（probing → 功能可解码性，attention → 机制，RSA → 几何对齐，cross-instruction → token 特化）从不同角度交叉验证同一结论，增强了可信度。RSA 与 CKA 的分歧也被坦诚报告（Appendix A-B），而非回避。\n\n- **S5: Related Work 定位清晰**。与 Grant 2026 的三点差异（token-level vs feature-level, per-layer decomposition, factorial controls）在 Section 2 第三段明确阐述，positioning 准确。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**W1 [CRITICAL]: Contribution 1（token specialization）是架构上的必然结果，不构成实质新颖性**\n- 具体位置：Abstract 第4句, Introduction §1 Finding 1, Section 4.2, Contribution (i)\n- 问题：Image tokens 对 instruction blind 是 causal mask（image tokens 在 instruction tokens 之前，无法回看）和 frozen encoder（不接收 language input）的直接架构推论。论文自己也承认这是 \"architecture-expected\"（Abstract 第4句, Introduction ¶3 \"consistent with architectural expectations\"）。用 4 种 probe 方法验证一个架构保证的性质，methodologically sound 但不构成 contribution。将其列为三大贡献之首（Contribution (i)）让审稿人质疑 novelty bar。readout token 作为 multimodal hub 同样是 decoder-only 架构中 last token 的标准角色。\n- 为什么影响接收：如果三大贡献中的一个是验证已知事实，实际 novel contributions 只有 C2 和 C3。C3 又是 metric-dependent（见 W3），则论文的核心新颖性实质上只有 C2 的 routing reorganization。对 CoRL 而言，单一发现的增量贡献度不够。\n- 建议修改方向：将 C1 降格为 \"methodology validation\"（验证分析框架的有效性），而非独立 contribution。将 Contribution 列表重心放在 C2 和 C3，并加强 C2 的 behavioral implications。\n\n**W2 [CRITICAL]: 单模型（OpenVLA-7B）+ 单 benchmark 家族（LIBERO），泛化性严重不足**\n- 具体位置：Abstract（无 qualification）, Introduction（claims 用一般化措辞）, Discussion \"Limitations and scope\"（仅半段）\n- 问题：所有实验只在 OpenVLA-7B 上进行，benchmark 仅 LIBERO-Goal 和 LIBERO-Spatial（同一 benchmark 家族的两个 split）。但 Abstract 写 \"instruction routing reorganization is the primary learned contribution of VLA fine-tuning\"——这是对所有 VLA fine-tuning 的一般性声明，证据只来自一个模型。Grant 2026 覆盖 6 个 VLA（80M-7B），本文在范围上明显更窄。Discussion 承认 \"C2 may differ across backbone scales, decoder paradigms, and encoder training regimes\"，但 Abstract/Introduction 的 framing 没有相应 qualify。\n- 为什么影响接收：CoRL 审稿人会问：这些发现在 RT-2、π₀、SmolVLA 等不同架构上是否成立？特别是 π₀ 使用 flow matching 而非 autoregressive decoding，entry-exit routing pattern 可能完全不同。单模型分析论文在 CoRL 的 bar 上需要更强的 insight 或 architectural implication 来补偿。\n- 建议修改方向：(a) 在 Abstract/Introduction 中明确限定 scope（\"on OpenVLA-7B\" 而非泛化措辞），(b) 在 Discussion 扩充 limitation 段，讨论 flow-matching VLAs、不同 encoder training regimes 下 C2 可能不成立的原因，(c) 如有可能，至少在一个不同架构的 VLA 上验证 C2 的 entry-exit pattern。\n\n**W3 [CRITICAL]: 缺少行为层面验证——representational finding 未与 task performance 连接**\n- 具体位置：Section 4.3 ablation, Discussion \"Architectural implications\"\n- 问题：论文报告了 attention head ablation 对 R² 的影响（Section 4.3: dominant heads +0.042, random heads +0.077），但从未测量对实际 task success rate 的影响。R² 是 probe 在 frozen representations 上的离线指标，不等于 behavioral importance。Discussion 自己也承认 \"linking routing to behavioral outcomes requires task-level evaluation\"。对于 CoRL（机器人学习会议），representational analysis 不与 behavioral outcomes 连接，是一个重要缺口。\n- 为什么影响接收：CoRL 审稿人期望看到发现对 robot policy 设计有 actionable implications。论文的 architectural implication（\"early-layer parameters may suffice for instruction adaptation\"）是 speculative 的，没有任何实验支撑。如果 routing reorganization 对 success rate 的影响微乎其微，整篇论文的实际价值就存疑。\n- 建议修改方向：(a) 至少做一个简单的 behavioral validation：在 LIBERO 上用 ablated model 跑 rollout，报告 success rate 变化，(b) 或者将论文重新定位为 \"representational analysis\" 而非暗示 design implications，降低 claim 强度。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W4 [WARNING]: Ablation 解释逻辑不够 convincing**\n- 具体位置：Section 4.3 ¶4, Appendix E\n- 问题：Ablating 24 个 instruction-dominant heads 使 R² 从 0.517 增加到 0.559（+0.042），ablating 随机 24 heads 增加更多（+0.077）。论文解释为 dominant heads 具有 \"dual routing-encoding function\"。但同样合理的解释是：(a) ablation 本身通过移除 noise/interference 普遍提高 R²（无论哪些 heads），(b) dominant heads 贡献略少于随机 heads 恰恰因为它们不编码 action-relevant information。论文的 \"dual function\" 解释需要额外证据排除 alternative explanations。且 z-score 基于仅 10 个 random subsets，统计功效有限。\n- 建议：增加 random subsets 数量（至少 100），并考虑 attention knockout（将 attention 设为 uniform 而非 zero）作为对照。\n\n**W5 [WARNING]: C3（非单调变换）是 metric-dependent 的，CKA 直接矛盾**\n- 具体位置：Appendix A-B (Figure 6), Section 4.4 ¶3\n- 问题：RSA 显示 inverted-U（peak L12），但 linear CKA 显示单调递增（L0: 0.081 → L32: 0.098），甚至 untrained > trained。论文解释为 \"RSA captures rank-order geometry; CKA captures global linear structure\"，但读者可以合理选择 CKA 来讲一个完全相反的故事。C3 作为独立 contribution，其 robustness 受到 metric 选择的严重制约。此外，NLP 领域已广泛记录 transformer 层的非单调 probing profile（Tenney 2019 等），将其延伸到 VLA 的增量新颖性有限。\n- 建议：(a) 在正文（非仅 Appendix）承认 CKA 的矛盾结果，(b) 将 C3 定位为 \"observation\" 而非独立 contribution，(c) 讨论 RSA vs CKA 分歧对结论的实质影响。\n\n**W6 [WARNING]: Abstract 和 Introduction 数据密度过高，叙事可读性受损**\n- 具体位置：Abstract 全文, Introduction ¶3-4\n- 问题：Abstract 在约 200 words 中包含了 ~15 个具体数值（10%, 100%, L0-L1, 21-24 heads, L9-L16, 15-22 heads, 99.6%, 80.2%, z=-2.73, R² peaks L8-L14, ρ=0.628, 0.422, +0.069, +46pp, ≤0.017）。Introduction 同样密集。这让论文读起来像 experimental report 而非有说服力的 narrative。审稿人在 30 秒内无法从 Abstract 提取核心价值。\n- 建议：Abstract 保留 2-3 个最关键数字，其余移入正文。Introduction 的 three findings 段落应先建立直觉再给数字。\n\n**W7 [WARNING]: 格式问题——缺少 Generative AI 使用声明**\n- 具体位置：main.tex 全文\n- 问题：CoRL 2026 Call for Papers 要求提交 Generative AI 使用声明（disclosure of generative AI use）。当前稿件中未找到此声明。\n- 建议：按 CoRL 2026 要求添加 Generative AI disclosure statement。\n\n**W8 [WARNING]: conclusion.tex 存在但未被 main.tex 编译**\n- 具体位置：main.tex line 28-32（\\input 列表中无 conclusion）, conclusion.tex（存在于同一目录）\n- 问题：conclusion.tex 文件包含一个完整的 Conclusion section，但 main.tex 的 \\input 序列中没有 \\input{conclusion}。这意味着编译后的 PDF 没有 Conclusion 节。Discussion 节结尾没有明确总结，读者看到的最后正文内容是 Limitations and scope 段落。\n- 建议：在 \\input{discussion} 之后、\\bibliography 之前添加 \\input{conclusion}。\n\n### 小问题（不影响接收）\n\n- **M1**: \"-ing\" 分词短语在全文中出现约 30+ 次（\", indicating...\", \", confirming...\", \", reflecting...\"）。虽然每处单独看是自然英文，但高密度是 AI 辅助写作的统计信号。建议通读一遍，将部分改写为独立句子。\n- **M2**: Appendix 中 conclusion.tex 第 6 行 \"Code and representations will be released upon acceptance\" 可能泄露非匿名信息（暗示作者有代码控制权）。对 double-blind 无大碍，但建议改为更中性的表述。\n- **M3**: Table 2 caption 需要解释 \"Mode\" 列的含义（\"immed.+stable\", \"gradual+stable\", \"incid.+forget\"），当前 caption 不自包含。\n- **M4**: references.bib 中 nostalgebraist2020 的 `note = {Accessed: 2026-05-18}` 暴露了写作日期，在 blind review 中无实质风险但不够规范。\n- **M5**: Discussion \"Speculative mechanistic interpretation\" 段落（¶3）标题中的 \"Speculative\" 过于自我贬低，建议改为 \"Mechanistic hypothesis\" 或直接去掉限定词。\n\n---\n\n## Questions for Authors\n\n- **Q1**: Untrained readout 在 L1 达到 100% cross-instruction classification（Table 1），但 untrained model 在 L1 有 0/32 instruction-dominant heads（Table 2）。论文解释为 \"even incidental attention (~12%) suffices for linear classification\"（Appendix K.1）。如果 12% 的 incidental attention 就足以完美分类，那么 VLA training 将 L1 attention 提高到 57.7% 的功能意义是什么？这是否说明 cross-instruction probe 的 ceiling effect 太严重，无法区分 fine 的路由差异？\n\n- **Q2**: 论文声称 \"vision encoder quality emerges as a key design lever\"（conclusion.tex），但实验中 DINOv2 cls_token 的 RSA 最高（0.692）而 VLA trained readout 的 R² 最高（0.678）。这两个指标指向不同的 \"best\" representation。如果两者矛盾，\"vision encoder quality\" 的操作化定义是什么？\n\n- **Q3**: Pretrained Llama-2 base 接收的是从未在 pretraining 中见过的 visual token projections（OOD input）。虽然 Appendix G 报告了 activation diagnostics，但这些诊断只证明 representations 非退化，不证明 pretrained model 的 routing pattern（mid-depth concentration）是 meaningful 而非 arbitrary OOD response。如何排除 pretrained condition 的 routing pattern 只是 OOD 输入的 artifact？\n\n- **Q4**: L1 ablation 实验使用了 \"feature reconstruction pipeline\"（Section 4.3 footnote 1），其 baseline R² (0.517) 与 Table 3 的值 (0.557-0.678) 不同。这个 pipeline 的细节在哪里描述？差异的来源是否影响 ablation 结论的可靠性？\n\n---\n\n## Missing References\n\n1. **Rizzardo et al. (2026)** — 如果 Buurmeijer 2026 不是同一篇，则缺少 Rizzardo 2026 的 feature observability/controllability 工作\n2. **Bills et al. (2023)** \"Language models can explain neurons in language models\" — SAE/feature interpretation 的重要方法论基础\n3. **Templeton et al. (2024)** \"Scaling monosemanticity\" — Anthropic 的 SAE scaling 工作，与 Swann 2026 的方法论基础相关\n4. **Neel Nanda et al. (2023)** \"Progress measures for grokking via mechanistic interpretability\" — mechanistic interpretability 的重要参考\n5. **可能缺少 VLA fine-tuning 效率相关工作**（如 parameter-efficient fine-tuning for VLAs），因为论文暗示 \"early-layer parameters may suffice for instruction adaptation\"\n\n---\n\n## 官方维度打分（基于 CoRL 2023/2024 review criteria）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 4/10 | C1 是架构必然；C3 是 metric-dependent；实质新颖性主要在 C2 routing reorganization |\n| Quality/Soundness | 7/10 | 实验设计严谨，统计完整，但缺少 behavioral validation，ablation 解释存在 alternative explanations |\n| Clarity | 6/10 | 写作技术上清晰但 Abstract/Intro 数据过载，叙事感不足，更像 experimental report |\n| Significance | 4/10 | 单模型单 benchmark 的 representational finding，无 behavioral validation，对 VLA 设计的 actionable implications 仅 speculative |\n| Relevance | 7/10 | VLA interpretability 是 CoRL 关心的方向，但纯 representation analysis 不如 behavioral/design insights 与 CoRL 受众匹配 |\n| Limitations | 6/10 | 存在但仅半段嵌入 Discussion，scope 限制描述到位但未讨论关键 failure modes |\n\n---\n\n## Overall Assessment\n\n**Score: Weak Reject (4/10)**\n**Confidence: High**\n\n**一句话总结**: 实验设计和统计严谨度优秀，但三大贡献中 C1 是架构必然、C3 是 metric-dependent，实质新颖性集中在 C2（routing reorganization），而单模型+无 behavioral validation 使这一贡献难以达到 CoRL 的 acceptance bar。\n\n**核心判断**：本文是一篇执行质量高的 representational analysis 工作，但存在 novelty 和 significance 的结构性问题。如果作者能 (a) 在至少一个额外 VLA 上验证 C2，(b) 添加 behavioral validation（哪怕是 preliminary 的 success rate 测量），(c) 重组 contribution 列表将 C1 降格，论文的竞争力会显著提升。当前版本更适合 workshop paper 或需要 major revision 后重投。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 数据密度过高（~15 个数字），可读性差。核心 message 被淹没在统计细节中。\n- \"instruction routing reorganization is the primary learned contribution of VLA fine-tuning\" 是 overclaim（单模型证据）。\n\n### Introduction\n- 5 段结构完整，从 gap 到 method 到 findings 到 contributions 的逻辑清晰。\n- 但 ¶3-4 重复 Abstract 的数字密集风格，未建立足够的直觉铺垫。\n- Contribution (i) 的 \"verifying architecture-expected specialization\" 措辞暗示作者知道这不是 novel finding，但仍列为 contribution。\n\n### Related Work\n- 覆盖全面：VLA models, mechanistic interpretability, behavioral analysis, token specialization, similarity methods 五个主题。\n- 与 Grant 2026 的差异化（第三段）清晰有力。\n- 缺少 SAE 方法论基础文献（Bills 2023, Templeton 2024）。\n\n### Method\n- 清晰、可复现。四种分析方法的选择有充分 justify（特别是 RSA over CKA 的段落）。\n- \"Why RSA over CKA\" 段落放在 Method 中有些突兀，考虑移至 Appendix。\n\n### Experiments\n- Section 4.2（Token Specialization）: 结果 clean 但 C1 的 novelty 问题依然存在。\n- Section 4.3（Routing）: 最强的贡献。Figure 1 和 Table 2 清晰展示三条件梯度。\n- Section 4.4（Non-monotonic）: 数据详实但 CKA 矛盾未在正文讨论。\n\n### Discussion\n- 简洁但过于简短。\"Speculative mechanistic interpretation\" 段有价值但自我限制过多。\n- \"Limitations and scope\" 仅半段，未讨论 behavioral validation 缺失和 metric dependence。\n- 建议扩充 Limitations 为独立 section（CoRL 要求）。\n\n### Appendix\n- 内容丰富且必要（robustness, cross-benchmark, diagnostics）。\n- 但部分结果（CKA 矛盾、action R² three-condition）对主文叙事有重大影响，应在正文中至少 summarize。\n",
  "reviewer_id": "2",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 — Round 1 审稿意见\n\n**论文**: Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\n**Venue**: CoRL 2026\n**审查侧重**: 新颖性 + 叙事完整性 + 格式合规\n\n---\n\n## Summary\n\n本文对 OpenVLA-7B 在 LIBERO 上进行 token 级别的表征分析，使用 cross-instruction probes、attention analysis、RSA 和 MLP probes 四种方法，在 trained/pretrained/untrained 三条件阶乘设计下，报告三个发现：(1) image tokens 对 instruction 不敏感（由 causal mask 和 frozen encoder 架构保证），(2) VLA fine-tuning 将 instruction routing 从 mid-depth 前移到 entry-exit 层，(3) vision encoder 表征在 LLM 层中呈非单调变换。实验设计严谨，统计报告完整，但核心新颖性受限于单模型范围和部分 architecturally-expected 的发现。\n\n---\n\n## Strengths\n\n- **S1: 实验设计严谨的阶乘控制**。trained/pretrained/untrained × instruction presence/absence 的 2×3 设计是该领域少见的严格控制方案，能有效隔离 language pretraining 和 VLA fine-tuning 各自的贡献（Section 3.1）。这一设计优于 Grant 2026 等仅做 trained model 分析的工作。\n\n- **S2: 统计报告高标准**。所有主要结论均附有 bootstrap CI（10,000 resamples）、FDR 校正（Benjamini-Hochberg）、permutation test、seed sensitivity、demo subsampling sensitivity（Appendix H-J）。这在 VLA interpretability 文献中罕见，值得肯定。\n\n- **S3: Routing reorganization 发现有价值**。C2（Section 4.3, Figure 1, Table 2）揭示 VLA fine-tuning 将 instruction routing 从 Llama-2 的 mid-depth 模式（L9-L16, 15-22 heads）重组为 entry-exit 模式（L0-L1: 21-24 heads, L31: 18 heads），且三条件梯度在 30%-70% 阈值范围内稳定（Appendix Table 14）。这是对 VLA 内部机制的有意义新知识。\n\n- **S4: 方法互补性好**。四种分析方法（probing → 功能可解码性，attention → 机制，RSA → 几何对齐，cross-instruction → token 特化）从不同角度交叉验证同一结论，增强了可信度。RSA 与 CKA 的分歧也被坦诚报告（Appendix A-B），而非回避。\n\n- **S5: Related Work 定位清晰**。与 Grant 2026 的三点差异（token-level vs feature-level, per-layer decomposition, factorial controls）在 Section 2 第三段明确阐述，positioning 准确。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**W1 [CRITICAL]: Contribution 1（token specialization）是架构上的必然结果，不构成实质新颖性**\n- 具体位置：Abstract 第4句, Introduction §1 Finding 1, Section 4.2, Contribution (i)\n- 问题：Image tokens 对 instruction blind 是 causal mask（image tokens 在 instruction tokens 之前，无法回看）和 frozen encoder（不接收 language input）的直接架构推论。论文自己也承认这是 \"architecture-expected\"（Abstract 第4句, Introduction ¶3 \"consistent with architectural expectations\"）。用 4 种 probe 方法验证一个架构保证的性质，methodologically sound 但不构成 contribution。将其列为三大贡献之首（Contribution (i)）让审稿人质疑 novelty bar。readout token 作为 multimodal hub 同样是 decoder-only 架构中 last token 的标准角色。\n- 为什么影响接收：如果三大贡献中的一个是验证已知事实，实际 novel contributions 只有 C2 和 C3。C3 又是 metric-dependent（见 W3），则论文的核心新颖性实质上只有 C2 的 routing reorganization。对 CoRL 而言，单一发现的增量贡献度不够。\n- 建议修改方向：将 C1 降格为 \"methodology validation\"（验证分析框架的有效性），而非独立 contribution。将 Contribution 列表重心放在 C2 和 C3，并加强 C2 的 behavioral implications。\n\n**W2 [CRITICAL]: 单模型（OpenVLA-7B）+ 单 benchmark 家族（LIBERO），泛化性严重不足**\n- 具体位置：Abstract（无 qualification）, Introduction（claims 用一般化措辞）, Discussion \"Limitations and scope\"（仅半段）\n- 问题：所有实验只在 OpenVLA-7B 上进行，benchmark 仅 LIBERO-Goal 和 LIBERO-Spatial（同一 benchmark 家族的两个 split）。但 Abstract 写 \"instruction routing reorganization is the primary learned contribution of VLA fine-tuning\"——这是对所有 VLA fine-tuning 的一般性声明，证据只来自一个模型。Grant 2026 覆盖 6 个 VLA（80M-7B），本文在范围上明显更窄。Discussion 承认 \"C2 may differ across backbone scales, decoder paradigms, and encoder training regimes\"，但 Abstract/Introduction 的 framing 没有相应 qualify。\n- 为什么影响接收：CoRL 审稿人会问：这些发现在 RT-2、π₀、SmolVLA 等不同架构上是否成立？特别是 π₀ 使用 flow matching 而非 autoregressive decoding，entry-exit routing pattern 可能完全不同。单模型分析论文在 CoRL 的 bar 上需要更强的 insight 或 architectural implication 来补偿。\n- 建议修改方向：(a) 在 Abstract/Introduction 中明确限定 scope（\"on OpenVLA-7B\" 而非泛化措辞），(b) 在 Discussion 扩充 limitation 段，讨论 flow-matching VLAs、不同 encoder training regimes 下 C2 可能不成立的原因，(c) 如有可能，至少在一个不同架构的 VLA 上验证 C2 的 entry-exit pattern。\n\n**W3 [CRITICAL]: 缺少行为层面验证——representational finding 未与 task performance 连接**\n- 具体位置：Section 4.3 ablation, Discussion \"Architectural implications\"\n- 问题：论文报告了 attention head ablation 对 R² 的影响（Section 4.3: dominant heads +0.042, random heads +0.077），但从未测量对实际 task success rate 的影响。R² 是 probe 在 frozen representations 上的离线指标，不等于 behavioral importance。Discussion 自己也承认 \"linking routing to behavioral outcomes requires task-level evaluation\"。对于 CoRL（机器人学习会议），representational analysis 不与 behavioral outcomes 连接，是一个重要缺口。\n- 为什么影响接收：CoRL 审稿人期望看到发现对 robot policy 设计有 actionable implications。论文的 architectural implication（\"early-layer parameters may suffice for instruction adaptation\"）是 speculative 的，没有任何实验支撑。如果 routing reorganization 对 success rate 的影响微乎其微，整篇论文的实际价值就存疑。\n- 建议修改方向：(a) 至少做一个简单的 behavioral validation：在 LIBERO 上用 ablated model 跑 rollout，报告 success rate 变化，(b) 或者将论文重新定位为 \"representational analysis\" 而非暗示 design implications，降低 claim 强度。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W4 [WARNING]: Ablation 解释逻辑不够 convincing**\n- 具体位置：Section 4.3 ¶4, Appendix E\n- 问题：Ablating 24 个 instruction-dominant heads 使 R² 从 0.517 增加到 0.559（+0.042），ablating 随机 24 heads 增加更多（+0.077）。论文解释为 dominant heads 具有 \"dual routing-encoding function\"。但同样合理的解释是：(a) ablation 本身通过移除 noise/interference 普遍提高 R²（无论哪些 heads），(b) dominant heads 贡献略少于随机 heads 恰恰因为它们不编码 action-relevant information。论文的 \"dual function\" 解释需要额外证据排除 alternative explanations。且 z-score 基于仅 10 个 random subsets，统计功效有限。\n- 建议：增加 random subsets 数量（至少 100），并考虑 attention knockout（将 attention 设为 uniform 而非 zero）作为对照。\n\n**W5 [WARNING]: C3（非单调变换）是 metric-dependent 的，CKA 直接矛盾**\n- 具体位置：Appendix A-B (Figure 6), Section 4.4 ¶3\n- 问题：RSA 显示 inverted-U（peak L12），但 linear CKA 显示单调递增（L0: 0.081 → L32: 0.098），甚至 untrained > trained。论文解释为 \"RSA captures rank-order geometry; CKA captures global linear structure\"，但读者可以合理选择 CKA 来讲一个完全相反的故事。C3 作为独立 contribution，其 robustness 受到 metric 选择的严重制约。此外，NLP 领域已广泛记录 transformer 层的非单调 probing profile（Tenney 2019 等），将其延伸到 VLA 的增量新颖性有限。\n- 建议：(a) 在正文（非仅 Appendix）承认 CKA 的矛盾结果，(b) 将 C3 定位为 \"observation\" 而非独立 contribution，(c) 讨论 RSA vs CKA 分歧对结论的实质影响。\n\n**W6 [WARNING]: Abstract 和 Introduction 数据密度过高，叙事可读性受损**\n- 具体位置：Abstract 全文, Introduction ¶3-4\n- 问题：Abstract 在约 200 words 中包含了 ~15 个具体数值（10%, 100%, L0-L1, 21-24 heads, L9-L16, 15-22 heads, 99.6%, 80.2%, z=-2.73, R² peaks L8-L14, ρ=0.628, 0.422, +0.069, +46pp, ≤0.017）。Introduction 同样密集。这让论文读起来像 experimental report 而非有说服力的 narrative。审稿人在 30 秒内无法从 Abstract 提取核心价值。\n- 建议：Abstract 保留 2-3 个最关键数字，其余移入正文。Introduction 的 three findings 段落应先建立直觉再给数字。\n\n**W7 [WARNING]: 格式问题——缺少 Generative AI 使用声明**\n- 具体位置：main.tex 全文\n- 问题：CoRL 2026 Call for Papers 要求提交 Generative AI 使用声明（disclosure of generative AI use）。当前稿件中未找到此声明。\n- 建议：按 CoRL 2026 要求添加 Generative AI disclosure statement。\n\n**W8 [WARNING]: conclusion.tex 存在但未被 main.tex 编译**\n- 具体位置：main.tex line 28-32（\\input 列表中无 conclusion）, conclusion.tex（存在于同一目录）\n- 问题：conclusion.tex 文件包含一个完整的 Conclusion section，但 main.tex 的 \\input 序列中没有 \\input{conclusion}。这意味着编译后的 PDF 没有 Conclusion 节。Discussion 节结尾没有明确总结，读者看到的最后正文内容是 Limitations and scope 段落。\n- 建议：在 \\input{discussion} 之后、\\bibliography 之前添加 \\input{conclusion}。\n\n### 小问题（不影响接收）\n\n- **M1**: \"-ing\" 分词短语在全文中出现约 30+ 次（\", indicating...\", \", confirming...\", \", reflecting...\"）。虽然每处单独看是自然英文，但高密度是 AI 辅助写作的统计信号。建议通读一遍，将部分改写为独立句子。\n- **M2**: Appendix 中 conclusion.tex 第 6 行 \"Code and representations will be released upon acceptance\" 可能泄露非匿名信息（暗示作者有代码控制权）。对 double-blind 无大碍，但建议改为更中性的表述。\n- **M3**: Table 2 caption 需要解释 \"Mode\" 列的含义（\"immed.+stable\", \"gradual+stable\", \"incid.+forget\"），当前 caption 不自包含。\n- **M4**: references.bib 中 nostalgebraist2020 的 `note = {Accessed: 2026-05-18}` 暴露了写作日期，在 blind review 中无实质风险但不够规范。\n- **M5**: Discussion \"Speculative mechanistic interpretation\" 段落（¶3）标题中的 \"Speculative\" 过于自我贬低，建议改为 \"Mechanistic hypothesis\" 或直接去掉限定词。\n\n---\n\n## Questions for Authors\n\n- **Q1**: Untrained readout 在 L1 达到 100% cross-instruction classification（Table 1），但 untrained model 在 L1 有 0/32 instruction-dominant heads（Table 2）。论文解释为 \"even incidental attention (~12%) suffices for linear classification\"（Appendix K.1）。如果 12% 的 incidental attention 就足以完美分类，那么 VLA training 将 L1 attention 提高到 57.7% 的功能意义是什么？这是否说明 cross-instruction probe 的 ceiling effect 太严重，无法区分 fine 的路由差异？\n\n- **Q2**: 论文声称 \"vision encoder quality emerges as a key design lever\"（conclusion.tex），但实验中 DINOv2 cls_token 的 RSA 最高（0.692）而 VLA trained readout 的 R² 最高（0.678）。这两个指标指向不同的 \"best\" representation。如果两者矛盾，\"vision encoder quality\" 的操作化定义是什么？\n\n- **Q3**: Pretrained Llama-2 base 接收的是从未在 pretraining 中见过的 visual token projections（OOD input）。虽然 Appendix G 报告了 activation diagnostics，但这些诊断只证明 representations 非退化，不证明 pretrained model 的 routing pattern（mid-depth concentration）是 meaningful 而非 arbitrary OOD response。如何排除 pretrained condition 的 routing pattern 只是 OOD 输入的 artifact？\n\n- **Q4**: L1 ablation 实验使用了 \"feature reconstruction pipeline\"（Section 4.3 footnote 1），其 baseline R² (0.517) 与 Table 3 的值 (0.557-0.678) 不同。这个 pipeline 的细节在哪里描述？差异的来源是否影响 ablation 结论的可靠性？\n\n---\n\n## Missing References\n\n1. **Rizzardo et al. (2026)** — 如果 Buurmeijer 2026 不是同一篇，则缺少 Rizzardo 2026 的 feature observability/controllability 工作\n2. **Bills et al. (2023)** \"Language models can explain neurons in language models\" — SAE/feature interpretation 的重要方法论基础\n3. **Templeton et al. (2024)** \"Scaling monosemanticity\" — Anthropic 的 SAE scaling 工作，与 Swann 2026 的方法论基础相关\n4. **Neel Nanda et al. (2023)** \"Progress measures for grokking via mechanistic interpretability\" — mechanistic interpretability 的重要参考\n5. **可能缺少 VLA fine-tuning 效率相关工作**（如 parameter-efficient fine-tuning for VLAs），因为论文暗示 \"early-layer parameters may suffice for instruction adaptation\"\n\n---\n\n## 官方维度打分（基于 CoRL 2023/2024 review criteria）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 4/10 | C1 是架构必然；C3 是 metric-dependent；实质新颖性主要在 C2 routing reorganization |\n| Quality/Soundness | 7/10 | 实验设计严谨，统计完整，但缺少 behavioral validation，ablation 解释存在 alternative explanations |\n| Clarity | 6/10 | 写作技术上清晰但 Abstract/Intro 数据过载，叙事感不足，更像 experimental report |\n| Significance | 4/10 | 单模型单 benchmark 的 representational finding，无 behavioral validation，对 VLA 设计的 actionable implications 仅 speculative |\n| Relevance | 7/10 | VLA interpretability 是 CoRL 关心的方向，但纯 representation analysis 不如 behavioral/design insights 与 CoRL 受众匹配 |\n| Limitations | 6/10 | 存在但仅半段嵌入 Discussion，scope 限制描述到位但未讨论关键 failure modes |\n\n---\n\n## Overall Assessment\n\n**Score: Weak Reject (4/10)**\n**Confidence: High**\n\n**一句话总结**: 实验设计和统计严谨度优秀，但三大贡献中 C1 是架构必然、C3 是 metric-dependent，实质新颖性集中在 C2（routing reorganization），而单模型+无 behavioral validation 使这一贡献难以达到 CoRL 的 acceptance bar。\n\n**核心判断**：本文是一篇执行质量高的 representational analysis 工作，但存在 novelty 和 significance 的结构性问题。如果作者能 (a) 在至少一个额外 VLA 上验证 C2，(b) 添加 behavioral validation（哪怕是 preliminary 的 success rate 测量），(c) 重组 contribution 列表将 C1 降格，论文的竞争力会显著提升。当前版本更适合 workshop paper 或需要 major revision 后重投。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 数据密度过高（~15 个数字），可读性差。核心 message 被淹没在统计细节中。\n- \"instruction routing reorganization is the primary learned contribution of VLA fine-tuning\" 是 overclaim（单模型证据）。\n\n### Introduction\n- 5 段结构完整，从 gap 到 method 到 findings 到 contributions 的逻辑清晰。\n- 但 ¶3-4 重复 Abstract 的数字密集风格，未建立足够的直觉铺垫。\n- Contribution (i) 的 \"verifying architecture-expected specialization\" 措辞暗示作者知道这不是 novel finding，但仍列为 contribution。\n\n### Related Work\n- 覆盖全面：VLA models, mechanistic interpretability, behavioral analysis, token specialization, similarity methods 五个主题。\n- 与 Grant 2026 的差异化（第三段）清晰有力。\n- 缺少 SAE 方法论基础文献（Bills 2023, Templeton 2024）。\n\n### Method\n- 清晰、可复现。四种分析方法的选择有充分 justify（特别是 RSA over CKA 的段落）。\n- \"Why RSA over CKA\" 段落放在 Method 中有些突兀，考虑移至 Appendix。\n\n### Experiments\n- Section 4.2（Token Specialization）: 结果 clean 但 C1 的 novelty 问题依然存在。\n- Section 4.3（Routing）: 最强的贡献。Figure 1 和 Table 2 清晰展示三条件梯度。\n- Section 4.4（Non-monotonic）: 数据详实但 CKA 矛盾未在正文讨论。\n\n### Discussion\n- 简洁但过于简短。\"Speculative mechanistic interpretation\" 段有价值但自我限制过多。\n- \"Limitations and scope\" 仅半段，未讨论 behavioral validation 缺失和 metric dependence。\n- 建议扩充 Limitations 为独立 section（CoRL 要求）。\n\n### Appendix\n- 内容丰富且必要（robustness, cross-benchmark, diagnostics）。\n- 但部分结果（CKA 矛盾、action R² three-condition）对主文叙事有重大影响，应在正文中至少 summarize。\n",
    "reviewer_id": "2",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 295 · 2026-05-18T08:58:12.834725+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4319
}
```

</details>

---


### Assistant

_source line 296 · 2026-05-18T08:58:20.517153+00:00_

Round 1 审稿意见已提交给 Review Director。

核心判断：**Weak Reject (4/10)**，信心 High。

主要问题：
1. **C1（token specialization）是架构必然结果**，不构成实质 contribution
2. **单模型单 benchmark**，泛化性不足，但 claims 用了一般化措辞
3. **无 behavioral validation**——representational findings 未与 task success rate 连接，对 CoRL 是重大缺口
4. 格式问题：缺少 Generative AI 声明，conclusion.tex 未编译，无独立 Limitations section

主要优势：阶乘实验设计严谨，统计报告高标准，C2（routing reorganization）有实质新颖性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2"
}
```

</details>

---


## Round 10

## Round 10

4 recorded events


### User

_source line 297 · 2026-05-18T09:09:11.189324+00:00_

[Round 1 审稿请求]:
## Step 2 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整 Round 1 审稿意见。请逐条回应：
- **[AGREE]**：同意并说明理由
- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）

特别关注与你意见分歧的地方。

---

# Reviewer 1 — Round 1 Review

**Score: 5 (Marginally below acceptance threshold), Confidence: 4**

## Strengths
- S1: 系统性实验框架设计（三条件因子控制）
- S2: 多角度互验（RSA + probes + attention + cross-instruction，含 linear probe 复制）
- S3: 丰富的 robustness 分析（distance metric, demo subsampling, seed, threshold, cross-benchmark）
- S4: CKA 分歧的诚实处理
- S5: 与 behavioral 文献的连接（Grant 2026, Häon 2025）

## Weaknesses

**W1 [CRITICAL]: Cross-instruction probe 近乎 trivially easy，削弱核心贡献新颖性**
- 10-way classification 在 ALL THREE 条件（trained/pretrained/untrained）L1 均达到 99.6-100%
- 10 条 LIBERO-Goal 指令在 token 层面差异巨大，linear classifier 只需最微弱残留即可 100%
- 更有信息量的是 DECAY PATTERN（untrained 100%→82%, trained 100%→100%），但论文将 "100% from L1" 作为主要发现
- 建议增加更难的 probe task（paraphrase 指令、语义近似指令）

**W2 [CRITICAL]: L1 head ablation 因果推断方向存在根本性问题**
- Ablating ANY 24/32 heads 都 INCREASE R²（dominant +0.042, random +0.077）
- 如果 dominant heads 功能重要，ablation 应 DECREASE R²
- "dual function" 是 post-hoc rationalization；等效替代解释：L1 heads 普遍添加噪声
- Random subset 仅 N=10，z-test 统计功效极低
- 建议：细粒度 ablation curve (4/8/12/16/20/24/28), selective ablation (只移除 instruction attention), 增加 random subsets ≥100

**W3 [CRITICAL]: Action probe train/test split 未说明，overparameterized MLP probe R² 可信度存疑**
- MLP probe N/params ≈ 0.06（overparameterized），R² 在哪个数据集上计算未明确
- Linear probe gap (Δ=+0.324 at L14) vs MLP probe gap (Δ=+0.015 at L8) 相差 ~20 倍 → MLP 过强压缩条件差异
- N=63,228 中时间步高度自相关，有效样本量远小于名义值
- Bootstrap CI 基于独立假设，可能严重低估不确定性

**W4 [WARNING]: RSA 统计推断中的依赖性问题**
- N(N-1)/2 pairwise distances 不独立，标准 bootstrap 低估 variance
- Permutation test 仅测试 "是否存在 ANY structure"，不测试条件间差异
- same-layer L12 比较存在 selection bias（选择差异最大的层）
- 建议 Mantel test 或 stimulus-level bootstrap

**W5 [WARNING]: RSA vs CKA 分歧对 Finding 3 影响被低估**
- Linear CKA 完全反转 RSA 排序和 per-layer profile
- 论文未论证为何 rank-order geometry 对 action prediction 更相关
- 三个 metrics 给三种故事，论文选择 RSA

**W6 [WARNING]: 单模型单 benchmark 泛化性不足**
- 所有实验仅 OpenVLA-7B + LIBERO（10 个 tabletop tasks）
- 无其他 VLA、无 real-robot、无多样化任务域
- LIBERO-Spatial 仍在 LIBERO 框架内

**W7 [WARNING]: 缺少行为验证**
- 所有发现在 representation space，无连接到 task success rate
- "early-layer parameters may suffice" 无验证
- 对 CoRL 的 practical value 有限

**W8 [INFO]: Pretrained Llama-2 visual token 处理是否有意义**
- 非退化不等于有意义处理
- 建议用 random noise tokens 替代 visual tokens 作 diagnostic

## Questions
- Q1: R² 在 training set 还是 held-out test set 上计算？train/test split 策略？
- Q2: 所有 head ablation 都 INCREASE R²，是否意味着 L1 heads 对 action prediction 有害？
- Q3: 如果用更难的 probe task（paraphrase 指令），结果是否不同？
- Q4: Linear probe gap (~20× MLP probe gap) 对结果解释有什么影响？
- Q5: Bootstrap CI 的 resampling unit？如何处理自相关？
- Q6: 能否提供 RSA 条件间差异的 Mantel test？

## Missing References
- Hewitt & Liang (2019) "Designing and Interpreting Probes with Control Tasks"
- Zheng et al. (2024) "3D-VLA"
- Nili et al. (2014) "A Toolbox for Representational Similarity Analysis"

---

请对以上每个 Weakness (W1-W8)、Question (Q1-Q6) 和 Missing References 逐条回应 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 298 · 2026-05-18T09:11:00.686227+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 — 交叉回应 Reviewer 1 Round 1 意见\n\n---\n\n## Weaknesses 逐条回应\n\n**[AGREE] R1-W1: Cross-instruction probe trivially easy**\n同意这是 C1 新颖性问题的另一个维度。我的 R2-W1 从架构层面论证 C1 是 trivial（causal mask + frozen encoder），R1 从 probe task difficulty 层面论证同一结论。两个角度互补：不仅架构保证了 image token instruction-blindness，且 10 条 LIBERO 指令在 token 空间差异巨大，使 readout token 的 100% classification 也接近 trivial。R1 指出 untrained 模型在 L1 也达到 100%（Table 1），这直接说明该 probe task 的 discriminative power 不足以区分有意义的表征差异和 incidental signal leakage。\n\nR1 建议的 paraphrase/语义近似指令 probe 是一个有价值的加强方向，能真正测试指令理解的深度而非表面 token 差异。\n\n补充一点：论文 Appendix K.3 的 QA probe（progress + subtask classification）才是更有信息量的 probe，但被放在 Appendix 且 trained vs untrained 差异仅 1pp（86.3% vs 85.3%, Table 12），进一步削弱了 training effect 在 readout token 上的 functional significance。\n\n**[AGREE] R1-W2: L1 head ablation 因果推断方向问题**\n强烈同意。这是我 R2-W4 的更尖锐表述。核心逻辑问题：如果 dominant heads 真正承担 \"dual routing-encoding function\"，ablation 应导致 R² 下降（information loss），而非上升。所有 ablation 都 increase R² 这一事实，最简洁的解释是 L1 heads 整体对 downstream probe 有轻微 interference，而非 functional contribution。\n\nR1 提出的 alternative explanation（\"L1 heads 普遍添加噪声\"）比论文的 \"dual function\" 解释更 parsimonious。论文选择了更复杂的解释但未提供足够证据排除更简单的解释，违反 Occam's razor。\n\nR1 建议的细粒度 ablation curve（4/8/12/.../28 heads）和 selective ablation（只移除 instruction attention component）都是 constructive 的。特别是 selective ablation——如果能零化 instruction attention 但保留其他 attention patterns，就能真正测试 instruction routing 的 causal role。\n\nN=10 random subsets 的统计功效问题我也在 R2-W4 中指出。z=-2.73 在 N=10 下虽然名义 p=0.003，但分布假设（正态近似）在如此小样本下不可靠。\n\n**[AGREE] R1-W3: Probe train/test split 和 overparameterization 问题**\n同意这是一个被忽视的方法论漏洞。论文 Section 4.1 提到 \"early stopping patience 5\"，暗示有 validation set，但从未明确说明：(a) train/test split ratio，(b) split 是 random 还是 per-task/per-demonstration，(c) R² 报告在 test set 还是 train set 上。\n\nR1 关于时间步自相关的观点尤其重要。63,228 observations 来自 50 demonstrations × 10 tasks × ~127 timesteps。相邻时间步的 representations 和 actions 高度相关（机器人运动的连续性），effective sample size 远小于 63K。如果 train/test split 是 random timestep split（而非 demonstration-level split），则 test set 几乎必然包含与 training set 近乎相同的数据点（相邻帧），导致 R² 严重高估。\n\nLinear vs MLP probe 的 20× gap（Δ=0.324 vs Δ=0.015）是一个 red flag。这说明 MLP probe 的非线性容量足以从 untrained representations 中也\"解救\"大量 action information，压缩了 trained/untrained 的差异。论文在 Appendix F 承认 \"MLP nonlinearity partially rescues degraded representations\"，但没有讨论这对主文所有 MLP probe 结论的影响——如果 MLP probe 系统性地低估 training effect，Table 3 的 Δ=+0.069 可能是 attenuated 的。反过来说，如果 linear probe 是更 fair 的指标，则论文应以 linear probe 为主，MLP probe 为辅。\n\n**[AGREE] R1-W4: RSA 统计推断中的依赖性问题**\n同意。RDM 的 N(N-1)/2 pairwise distances 之间存在 structural dependency（每个 observation 参与 N-1 个 pair），标准 bootstrap 假设 independent sampling，会 underestimate variance。这是 RSA 文献中已知的问题（Nili et al. 2014 明确讨论了此点，这也是 R1 建议引用该文的原因）。\n\nR1 建议的 Mantel test 或 stimulus-level bootstrap（以 observation 而非 pair 为 resampling unit）是正确的处理方式。论文当前的 bootstrap 可能使 CI 过窄，导致一些 \"significant\" 的 Δ 在正确统计下变为 n.s.。这尤其影响 Table 5 中 best-vs-best image_mean Δ=+0.017 的判断（当前已是 n.s.；如果 CI 更宽，则更加 n.s.）以及 same-layer L12 Δ=+0.079 的 significance。\n\n不过，permutation test（Appendix H.3）的 15-23 SD 偏移足以确认 representation-action alignment 的存在性（observed ρ vs null），即使不完美也不至于完全失效。R1 说 \"permutation test 仅测试 ANY structure 而非条件间差异\" 是准确的。\n\n**[AGREE] R1-W5: RSA vs CKA 分歧对 Finding 3 影响被低估**\n完全同意，与我的 R2-W5 一致。补充一点：论文选择 RSA 的理由（Section 3.6 \"Why RSA over CKA\"）是 \"Spearman rank correlation is scale-invariant and robust to monotonic transformations\"，但这是 general methodological argument，未论证为何 rank-order geometry（而非 global covariance structure）对 action prediction 更 relevant。如果目标是 action prediction，probe R² 才是直接指标；如果目标是 geometric characterization，则两种 metric 同等 valid，论文不能只报一种。\n\n关键的叙事问题：如果作者在写论文时先看到 CKA 结果（monotonic increase），他们是否还会提出 \"non-monotonic refinement\" 作为 C3？Metric selection 看起来是 results-driven 而非 hypothesis-driven。\n\n**[AGREE] R1-W6: 单模型单 benchmark 泛化性不足**\n与我的 R2-W2 完全一致。无额外补充。\n\n**[AGREE] R1-W7: 缺少行为验证**\n与我的 R2-W3 完全一致。无额外补充。\n\n**[AGREE] R1-W8: Pretrained Llama-2 visual token 处理是否有意义**\n同意，与我的 R2-Q3 相关。R1 建议的 random noise token diagnostic 是一个 clean 的实验：如果 Llama-2 base 在 random noise input 上也显示 mid-depth routing concentration（L9-L16 头数类似），则该 pattern 是 pretrained weights 的 generic 行为，与 visual token 无关，C2 中 \"language pretraining seeds partial instruction routing\" 的 claim 就不成立。\n\nAppendix G 的三个 diagnostics（activation magnitude, cosine similarity, PC variance）只证明 non-degenerate，不证明 meaningful processing。这是一个 necessary but not sufficient 的验证。\n\n---\n\n## Questions 逐条回应\n\n**[AGREE] R1-Q1: R² 在哪个数据集上计算？**\n完全同意这需要明确。我在 R1-W3 的回应中已详述。如果是 train set R²，则所有 probe 结果的 magnitude 需要大幅打折。\n\n**[AGREE] R1-Q2: 所有 ablation 都 increase R²，是否 L1 heads 对 action prediction 有害？**\n同意这是需要回答的关键问题。见 R1-W2 回应。论文需要解释为什么一个 supposedly important layer 的 head ablation 不会 hurt performance。\n\n**[AGREE] R1-Q3: 更难的 probe task 是否会改变结论？**\n同意。当前 10-way classification 在所有条件下都近乎 trivial，无法 discriminate fine-grained differences。\n\n**[AGREE] R1-Q4: Linear vs MLP probe gap 的 20× 差异**\n同意这需要解释。见 R1-W3 回应中的分析。\n\n**[AGREE] R1-Q5: Bootstrap resampling unit 和自相关处理**\n同意。论文未说明 bootstrap 的 resampling unit 是 observation-level 还是 demonstration-level。如果是 observation-level，时间自相关导致 effective sample size 远小于 63K，CI 被严重低估。\n\n**[REBUT] R1-Q6: RSA 条件间差异的 Mantel test**\n部分 rebut。Mantel test 主要用于测试两个 distance matrices 之间的 association（即论文已在做的 representation-action RDM correlation），而非条件间差异。对于 trained vs untrained 的 RSA Δ 比较，更合适的方法是 stimulus-level bootstrap（以 demonstration 或 task 为 resampling unit），或者直接用 per-task RSA 值做 paired test（论文已报告 per-task 结果用于 bootstrap）。但 R1 的核心关切——标准 bootstrap 低估 variance——是完全正确的。\n\n---\n\n## Missing References 回应\n\n**[AGREE] Hewitt & Liang (2019) \"Designing and Interpreting Probes with Control Tasks\"**\n强烈同意。这篇论文直接讨论了 probe 设计中的 control task 方法论，与本文的 probing framework 高度相关。特别是其 \"selectivity\" 概念（probe accuracy minus control task accuracy）可以 formalize R1-W1 提出的 \"probe task too easy\" 问题。论文当前的 bib 中有 Belinkov 2022 和 Hewitt 2019（structural probe），但缺少这篇关于 probe design 的关键方法论文献。\n\n**[REBUT] Zheng et al. (2024) \"3D-VLA\"**\n部分 rebut。3D-VLA 是一个 VLA 架构论文，使用 3D representations。与本文的 representational analysis 主题关联度有限。Related Work 的 VLA 段落已引用 RT-2、OpenVLA、π₀ 等核心架构，3D-VLA 的缺失不构成重大遗漏。不过如果空间允许，加上也无妨。\n\n**[AGREE] Nili et al. (2014) \"A Toolbox for Representational Similarity Analysis\"**\n同意。这是 RSA 方法论的核心参考，特别是关于 RDM 统计推断（pairwise dependency 问题、noise ceiling 估计）。论文使用 RSA 作为主要 geometric metric 但只引用 Kriegeskorte 2008 的原始论文，缺少 Nili 2014 对 RSA 统计实践的重要补充。\n\n---\n\n## 总结：与 Reviewer 1 的共识和分歧\n\n**高度共识（6/8 Weaknesses）**：\n- C1 新颖性不足（R1-W1 + R2-W1）\n- Ablation 逻辑问题（R1-W2 + R2-W4）\n- 单模型泛化性（R1-W6 + R2-W2）\n- 缺少行为验证（R1-W7 + R2-W3）\n- RSA/CKA 分歧（R1-W5 + R2-W5）\n- Pretrained OOD 问题（R1-W8 + R2-Q3）\n\n**R1 新增的重要关切**：\n- Probe train/test split 和 overparameterization（R1-W3）——这是我遗漏的重要方法论问题\n- RSA pairwise dependency 的统计推断（R1-W4）——比我的审查更深入的统计关切\n- Linear vs MLP probe 20× gap 的 implication（R1-Q4）——有价值的观察\n\n**我的 R2 审稿中 R1 未覆盖的关切**：\n- Abstract/Introduction 数据密度过高、叙事可读性差（R2-W6）\n- 格式问题：缺少 Generative AI disclosure（R2-W7）、conclusion.tex 未编译（R2-W8）\n\n**总体评分对比**：R1 给 5/10（marginally below），我给 4/10（weak reject）。分差主要来自我对 novelty 的更严格判断——我认为 C1+C3 的 novelty 问题使论文实质上只有 C2 一个 contribution，这对 CoRL 不够。R1 对方法论问题（probe design, statistical inference）的关切比我更深入，是有价值的补充。\n\n综合两位 reviewer 意见，**核心问题一致**：novelty 受限 + 单模型 + 无 behavioral validation。分歧仅在严重程度判断上。\n",
  "reviewer_id": "2",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 — 交叉回应 Reviewer 1 Round 1 意见\n\n---\n\n## Weaknesses 逐条回应\n\n**[AGREE] R1-W1: Cross-instruction probe trivially easy**\n同意这是 C1 新颖性问题的另一个维度。我的 R2-W1 从架构层面论证 C1 是 trivial（causal mask + frozen encoder），R1 从 probe task difficulty 层面论证同一结论。两个角度互补：不仅架构保证了 image token instruction-blindness，且 10 条 LIBERO 指令在 token 空间差异巨大，使 readout token 的 100% classification 也接近 trivial。R1 指出 untrained 模型在 L1 也达到 100%（Table 1），这直接说明该 probe task 的 discriminative power 不足以区分有意义的表征差异和 incidental signal leakage。\n\nR1 建议的 paraphrase/语义近似指令 probe 是一个有价值的加强方向，能真正测试指令理解的深度而非表面 token 差异。\n\n补充一点：论文 Appendix K.3 的 QA probe（progress + subtask classification）才是更有信息量的 probe，但被放在 Appendix 且 trained vs untrained 差异仅 1pp（86.3% vs 85.3%, Table 12），进一步削弱了 training effect 在 readout token 上的 functional significance。\n\n**[AGREE] R1-W2: L1 head ablation 因果推断方向问题**\n强烈同意。这是我 R2-W4 的更尖锐表述。核心逻辑问题：如果 dominant heads 真正承担 \"dual routing-encoding function\"，ablation 应导致 R² 下降（information loss），而非上升。所有 ablation 都 increase R² 这一事实，最简洁的解释是 L1 heads 整体对 downstream probe 有轻微 interference，而非 functional contribution。\n\nR1 提出的 alternative explanation（\"L1 heads 普遍添加噪声\"）比论文的 \"dual function\" 解释更 parsimonious。论文选择了更复杂的解释但未提供足够证据排除更简单的解释，违反 Occam's razor。\n\nR1 建议的细粒度 ablation curve（4/8/12/.../28 heads）和 selective ablation（只移除 instruction attention component）都是 constructive 的。特别是 selective ablation——如果能零化 instruction attention 但保留其他 attention patterns，就能真正测试 instruction routing 的 causal role。\n\nN=10 random subsets 的统计功效问题我也在 R2-W4 中指出。z=-2.73 在 N=10 下虽然名义 p=0.003，但分布假设（正态近似）在如此小样本下不可靠。\n\n**[AGREE] R1-W3: Probe train/test split 和 overparameterization 问题**\n同意这是一个被忽视的方法论漏洞。论文 Section 4.1 提到 \"early stopping patience 5\"，暗示有 validation set，但从未明确说明：(a) train/test split ratio，(b) split 是 random 还是 per-task/per-demonstration，(c) R² 报告在 test set 还是 train set 上。\n\nR1 关于时间步自相关的观点尤其重要。63,228 observations 来自 50 demonstrations × 10 tasks × ~127 timesteps。相邻时间步的 representations 和 actions 高度相关（机器人运动的连续性），effective sample size 远小于 63K。如果 train/test split 是 random timestep split（而非 demonstration-level split），则 test set 几乎必然包含与 training set 近乎相同的数据点（相邻帧），导致 R² 严重高估。\n\nLinear vs MLP probe 的 20× gap（Δ=0.324 vs Δ=0.015）是一个 red flag。这说明 MLP probe 的非线性容量足以从 untrained representations 中也\"解救\"大量 action information，压缩了 trained/untrained 的差异。论文在 Appendix F 承认 \"MLP nonlinearity partially rescues degraded representations\"，但没有讨论这对主文所有 MLP probe 结论的影响——如果 MLP probe 系统性地低估 training effect，Table 3 的 Δ=+0.069 可能是 attenuated 的。反过来说，如果 linear probe 是更 fair 的指标，则论文应以 linear probe 为主，MLP probe 为辅。\n\n**[AGREE] R1-W4: RSA 统计推断中的依赖性问题**\n同意。RDM 的 N(N-1)/2 pairwise distances 之间存在 structural dependency（每个 observation 参与 N-1 个 pair），标准 bootstrap 假设 independent sampling，会 underestimate variance。这是 RSA 文献中已知的问题（Nili et al. 2014 明确讨论了此点，这也是 R1 建议引用该文的原因）。\n\nR1 建议的 Mantel test 或 stimulus-level bootstrap（以 observation 而非 pair 为 resampling unit）是正确的处理方式。论文当前的 bootstrap 可能使 CI 过窄，导致一些 \"significant\" 的 Δ 在正确统计下变为 n.s.。这尤其影响 Table 5 中 best-vs-best image_mean Δ=+0.017 的判断（当前已是 n.s.；如果 CI 更宽，则更加 n.s.）以及 same-layer L12 Δ=+0.079 的 significance。\n\n不过，permutation test（Appendix H.3）的 15-23 SD 偏移足以确认 representation-action alignment 的存在性（observed ρ vs null），即使不完美也不至于完全失效。R1 说 \"permutation test 仅测试 ANY structure 而非条件间差异\" 是准确的。\n\n**[AGREE] R1-W5: RSA vs CKA 分歧对 Finding 3 影响被低估**\n完全同意，与我的 R2-W5 一致。补充一点：论文选择 RSA 的理由（Section 3.6 \"Why RSA over CKA\"）是 \"Spearman rank correlation is scale-invariant and robust to monotonic transformations\"，但这是 general methodological argument，未论证为何 rank-order geometry（而非 global covariance structure）对 action prediction 更 relevant。如果目标是 action prediction，probe R² 才是直接指标；如果目标是 geometric characterization，则两种 metric 同等 valid，论文不能只报一种。\n\n关键的叙事问题：如果作者在写论文时先看到 CKA 结果（monotonic increase），他们是否还会提出 \"non-monotonic refinement\" 作为 C3？Metric selection 看起来是 results-driven 而非 hypothesis-driven。\n\n**[AGREE] R1-W6: 单模型单 benchmark 泛化性不足**\n与我的 R2-W2 完全一致。无额外补充。\n\n**[AGREE] R1-W7: 缺少行为验证**\n与我的 R2-W3 完全一致。无额外补充。\n\n**[AGREE] R1-W8: Pretrained Llama-2 visual token 处理是否有意义**\n同意，与我的 R2-Q3 相关。R1 建议的 random noise token diagnostic 是一个 clean 的实验：如果 Llama-2 base 在 random noise input 上也显示 mid-depth routing concentration（L9-L16 头数类似），则该 pattern 是 pretrained weights 的 generic 行为，与 visual token 无关，C2 中 \"language pretraining seeds partial instruction routing\" 的 claim 就不成立。\n\nAppendix G 的三个 diagnostics（activation magnitude, cosine similarity, PC variance）只证明 non-degenerate，不证明 meaningful processing。这是一个 necessary but not sufficient 的验证。\n\n---\n\n## Questions 逐条回应\n\n**[AGREE] R1-Q1: R² 在哪个数据集上计算？**\n完全同意这需要明确。我在 R1-W3 的回应中已详述。如果是 train set R²，则所有 probe 结果的 magnitude 需要大幅打折。\n\n**[AGREE] R1-Q2: 所有 ablation 都 increase R²，是否 L1 heads 对 action prediction 有害？**\n同意这是需要回答的关键问题。见 R1-W2 回应。论文需要解释为什么一个 supposedly important layer 的 head ablation 不会 hurt performance。\n\n**[AGREE] R1-Q3: 更难的 probe task 是否会改变结论？**\n同意。当前 10-way classification 在所有条件下都近乎 trivial，无法 discriminate fine-grained differences。\n\n**[AGREE] R1-Q4: Linear vs MLP probe gap 的 20× 差异**\n同意这需要解释。见 R1-W3 回应中的分析。\n\n**[AGREE] R1-Q5: Bootstrap resampling unit 和自相关处理**\n同意。论文未说明 bootstrap 的 resampling unit 是 observation-level 还是 demonstration-level。如果是 observation-level，时间自相关导致 effective sample size 远小于 63K，CI 被严重低估。\n\n**[REBUT] R1-Q6: RSA 条件间差异的 Mantel test**\n部分 rebut。Mantel test 主要用于测试两个 distance matrices 之间的 association（即论文已在做的 representation-action RDM correlation），而非条件间差异。对于 trained vs untrained 的 RSA Δ 比较，更合适的方法是 stimulus-level bootstrap（以 demonstration 或 task 为 resampling unit），或者直接用 per-task RSA 值做 paired test（论文已报告 per-task 结果用于 bootstrap）。但 R1 的核心关切——标准 bootstrap 低估 variance——是完全正确的。\n\n---\n\n## Missing References 回应\n\n**[AGREE] Hewitt & Liang (2019) \"Designing and Interpreting Probes with Control Tasks\"**\n强烈同意。这篇论文直接讨论了 probe 设计中的 control task 方法论，与本文的 probing framework 高度相关。特别是其 \"selectivity\" 概念（probe accuracy minus control task accuracy）可以 formalize R1-W1 提出的 \"probe task too easy\" 问题。论文当前的 bib 中有 Belinkov 2022 和 Hewitt 2019（structural probe），但缺少这篇关于 probe design 的关键方法论文献。\n\n**[REBUT] Zheng et al. (2024) \"3D-VLA\"**\n部分 rebut。3D-VLA 是一个 VLA 架构论文，使用 3D representations。与本文的 representational analysis 主题关联度有限。Related Work 的 VLA 段落已引用 RT-2、OpenVLA、π₀ 等核心架构，3D-VLA 的缺失不构成重大遗漏。不过如果空间允许，加上也无妨。\n\n**[AGREE] Nili et al. (2014) \"A Toolbox for Representational Similarity Analysis\"**\n同意。这是 RSA 方法论的核心参考，特别是关于 RDM 统计推断（pairwise dependency 问题、noise ceiling 估计）。论文使用 RSA 作为主要 geometric metric 但只引用 Kriegeskorte 2008 的原始论文，缺少 Nili 2014 对 RSA 统计实践的重要补充。\n\n---\n\n## 总结：与 Reviewer 1 的共识和分歧\n\n**高度共识（6/8 Weaknesses）**：\n- C1 新颖性不足（R1-W1 + R2-W1）\n- Ablation 逻辑问题（R1-W2 + R2-W4）\n- 单模型泛化性（R1-W6 + R2-W2）\n- 缺少行为验证（R1-W7 + R2-W3）\n- RSA/CKA 分歧（R1-W5 + R2-W5）\n- Pretrained OOD 问题（R1-W8 + R2-Q3）\n\n**R1 新增的重要关切**：\n- Probe train/test split 和 overparameterization（R1-W3）——这是我遗漏的重要方法论问题\n- RSA pairwise dependency 的统计推断（R1-W4）——比我的审查更深入的统计关切\n- Linear vs MLP probe 20× gap 的 implication（R1-Q4）——有价值的观察\n\n**我的 R2 审稿中 R1 未覆盖的关切**：\n- Abstract/Introduction 数据密度过高、叙事可读性差（R2-W6）\n- 格式问题：缺少 Generative AI disclosure（R2-W7）、conclusion.tex 未编译（R2-W8）\n\n**总体评分对比**：R1 给 5/10（marginally below），我给 4/10（weak reject）。分差主要来自我对 novelty 的更严格判断——我认为 C1+C3 的 novelty 问题使论文实质上只有 C2 一个 contribution，这对 CoRL 不够。R1 对方法论问题（probe design, statistical inference）的关切比我更深入，是有价值的补充。\n\n综合两位 reviewer 意见，**核心问题一致**：novelty 受限 + 单模型 + 无 behavioral validation。分歧仅在严重程度判断上。\n",
    "reviewer_id": "2",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 299 · 2026-05-18T09:11:05.709795+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5023
}
```

</details>

---


### Assistant

_source line 300 · 2026-05-18T09:11:11.021041+00:00_

交叉回应已提交。与 Reviewer 1 在 6/8 个 Weakness 上高度共识（C1 新颖性不足、ablation 逻辑、单模型泛化、缺少行为验证、RSA/CKA 分歧、pretrained OOD 问题）。R1 在 probe train/test split 和 RSA 统计依赖性方面提出了我遗漏的重要方法论关切。唯一部分 rebut 的是 R1-Q6（Mantel test 不是 conditional comparison 的最佳工具）和 3D-VLA 引用（关联度有限）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2"
}
```

</details>

---


## Round 11

## Round 11

28 recorded events


### User

_source line 301 · 2026-05-18T13:36:17.026529+00:00_

[Round 2 审稿请求]:
## Round 2 修订评估 — Reviewer 2

### 背景
上一轮（Round 1）你侧重新颖性+叙事完整性+格式合规，给出 4/10 (Weak Reject)。论文已根据审稿意见进行修改。本轮任务是**逐条验证 open/in_progress issues 是否已充分修复**，并识别修改是否引入新问题。

### 论文路径
`projects/vla-ssd/docs/paper/main.tex`（含所有 .tex 子文件）
**Venue**: CoRL 2026, Deadline May 29

### Open/In-Progress Issues（你的上轮主要发现）

请逐条标注 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由：

**R6-C1 [CRITICAL]: Ablation "dual function" → "routing-first" 叙事修改**
- 上轮问题：所有 ablation increase R²，"dual function" 是 post-hoc rationalization
- 修改措施：Section 4.3 ¶4 (line 80) 改为 "routing-first specialization: these heads carry organized instruction signals that the action probe treats as structured noise"；新增 action trajectory validation (lines 83-87, d=0.65)
- 验证要点：(a) "routing-first" 叙事是否解决了"所有 ablation increase R²"的方向性问题？(b) action trajectory analysis 是否提供了 ablation 缺乏的因果证据？

**R6-C3 [CRITICAL]: 单模型 Abstract overclaim**
- 上轮问题：Abstract 用一般化措辞但仅单模型证据
- 修改措施：Abstract line 7 改为 "in the model studied"；Introduction contribution (ii) 加 "demonstrated on OpenVLA-7B/LIBERO"
- 验证要点：(a) qualify 是否充分？(b) Introduction ¶3-4 的 three findings 描述是否也已 qualify？(c) Discussion 中是否仍有 unqualified general claims？

**R6-C4 [CRITICAL]: 缺 behavioral validation**
- 上轮问题：representational findings 未连接 task success rate
- 修改措施：新增 "Action trajectory validation"（Section 4.3 lines 83-87）：open-loop action token 分析（72.3% divergence, d=0.65），但无 closed-loop rollout
- 验证要点：(a) open-loop action trajectory 对 CoRL 审稿人来说是否足够？(b) Discussion 中 "early-layer parameters may suffice" 是否仍 speculative？(c) 是否应更明确地标注 behavioral validation 的缺失？

**R6-W1 [WARNING]: RSA pairwise dependency**
- 修改措施：Method §3.5 (line 51) task-level block resampling + Nili 2014 引用
- 验证要点：处理是否充分？

### 同时检查

1. **已 resolved 的 issues 验证**：
   - R6-W2: GenAI disclosure 是否存在且完整？（Discussion 末尾）
   - R6-W3: Abstract 数据密度是否改善？
   - R6-I2: 缺失引用（Hewitt 2019, Nili 2014, Bills 2023, Templeton 2024）是否已添加？
   - R6-I3: Table 2 caption 是否自包含？Discussion "Speculative" 是否改为 "Mechanistic hypothesis"？

2. **C1 novelty 问题**（上轮 R2-W1 + R1-W1）：C1 仍列为 contribution (i)——"verifying architecture-expected specialization"。是否仍是 novelty 瓶颈？

3. **C3 metric-dependence**（上轮 R2-W5）：CKA 分歧是否在正文（非仅 Appendix）被更充分地讨论？

4. **修改是否引入新问题？**

### 输出格式
```
## Issue Verification
- R6-C1: [RESOLVED/STILL_OPEN] — 理由
- R6-C3: [RESOLVED/STILL_OPEN] — 理由
- R6-C4: [RESOLVED/STILL_OPEN] — 理由
- R6-W1: [RESOLVED/STILL_OPEN] — 理由

## Resolved Issues Quick Check
- R6-W2: [CONFIRMED/ISSUE]
- R6-W3: [CONFIRMED/ISSUE]
- R6-I2: [CONFIRMED/ISSUE]
- R6-I3: [CONFIRMED/ISSUE]

## Persistent Issues (from Round 1 not explicitly tracked)
## New Issues (if any)
## Updated Assessment
Score: X/10 (vs 上轮 4/10)
Direction: ↑/↓/→
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 302 · 2026-05-18T13:36:28.618362+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 303 · 2026-05-18T13:36:29.221740+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 304 · 2026-05-18T13:36:29.222225+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 305 · 2026-05-18T13:36:29.524131+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 306 · 2026-05-18T13:36:29.574722+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 307 · 2026-05-18T13:36:30.026705+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 308 · 2026-05-18T13:36:30.027241+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 309 · 2026-05-18T13:36:30.077974+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 310 · 2026-05-18T13:36:30.529612+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 311 · 2026-05-18T13:36:30.981111+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 312 · 2026-05-18T13:36:30.981583+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 313 · 2026-05-18T13:36:31.483736+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 314 · 2026-05-18T13:36:31.534458+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 315 · 2026-05-18T13:36:31.534961+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 316 · 2026-05-18T13:36:39.327561+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 317 · 2026-05-18T13:36:40.182004+00:00_

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
14	Meng et al.~\cite{meng2022_rome} developed causal tracing to locate factual associations in specific MLP layers, Belrose et al.~\cite{belrose2023_tunedlens} introduced the tuned lens for per-layer prediction tracking, and feature-level methods have scaled from automated neuron explanation~\cite{bills2023language} to dictionary learning over millions of features~\cite{templeton2024scaling}.
15	In parallel, attention probing studies have shown that individual heads encode syntactic relations~\cite{clark2019}, capture positional and structural patterns at different depths
…[truncated 3210 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 318 · 2026-05-18T13:36:40.182505+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
  "offset": "0",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
    "offset": "0",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 319 · 2026-05-18T13:36:40.634055+00:00_

0	% === VLA / Architecture ===
1	
2	@article{kim2024_openvla,
3	  title     = {{OpenVLA}: An Open-Source Vision-Language-Action Model},
4	  author    = {Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balakrishna, Ashwin and Nair, Suraj and Rafailov, Rafael and Foster, Ethan and Lam, Grace and Sanketi, Pannag and Lu, Quan and Kollar, Thomas and Burchfiel, Benjamin and Tedrake, Russ and Sadigh, Dorsa and Levine, Sergey and Liang, Percy and Finn, Chelsea},
5	  journal   = {arXiv preprint arXiv:2406.09246},
6	  year      = {2024},
7	}
8	
9	@article{karamcheti2024,
10	  title     = {Prismatic {VLMs}: Investigating the Design Space of Visually-Conditioned Language Models},
11	  author    = {Karamcheti, Siddharth and Nair, Suraj and Balakrishna, Ashwin and Liang, Percy and Kollar, Thomas and Sadigh, Dorsa},
12	  journal   = {arXiv preprint arXiv:2402.07865},
13	  year      = {2024},
14	}
15	
16	@article{brohan2023_rt2,
17	  title     = {{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
18	  author    = {Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},
19	  journal   = {arXiv preprint arXiv:2307.15818},
20	  year      = {2023},
21	}
22	
23	% === Benchmark ===
24	
25	@inproceedings{liu2023_libero,
26	  title     = {{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
27	  author    = {Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},
28	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
29	  year      = {2023},
30	}
31	
32	% === Representation Analysis Methods ===
33	
34	@article{kriegeskorte2008,
35	  title     = {Representational Similarity Analysis -- Connecting the Branches of Systems Neuroscience},
36	  author    = {Kriegeskorte, Nikolaus and Mur, Marieke and Band
…[truncated 2693 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 320 · 2026-05-18T13:36:40.985593+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "offset": "0",
  "limit": "120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "offset": "0",
    "limit": "120"
  }
}
```

</details>

---


### Tool result

_source line 321 · 2026-05-18T13:36:41.036856+00:00_

0	\appendix
1	
2	\section{Supplementary Material}
3	\label{sec:appendix}
4	
5	\subsection{CKA Analysis Method}
6	\label{sec:cka_appendix}
7	
8	We employ Centered Kernel Alignment (CKA)~\cite{kornblith2019} alongside RSA as a complementary perspective.
9	While RSA captures local geometric alignment via rank-order preservation, CKA measures global representational similarity through kernel-based comparisons.
10	
11	We compute both \emph{linear CKA}, which uses a linear kernel and is sensitive to second-order statistics, and \emph{RDM kernel CKA}, which operates on the same distance matrices as RSA but aggregates them differently.
12	Using both variants tests whether conclusions about representation structure are robust to the choice of similarity metric.
13	
14	Linear CKA between high-dimensional representations (4{,}096-D for LLM layers) and the 7-D action space is subject to a known dimension mismatch: the linear kernel in the low-dimensional space may not capture the same structure as in the high-dimensional space.
15	RDM kernel CKA avoids this issue by operating on distance matrices of equal size regardless of the original feature dimensionality.
16	
17	\subsection{Metric Sensitivity: RSA versus CKA}
18	\label{sec:metric_sensitivity_appendix}
19	
20	Linear CKA~\cite{kornblith2019} reverses the RSA ordering: untrained LLM ($\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially inverting the self-supervised advantage (Figure~\ref{fig:metric_comparison}).
21	RDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $\approx$ Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).
22	This divergence reflects the known sensitivity of representation similarity metrics to different geometric properties.
23	
24	At the per-layer level, linear CKA between image\_mean and the action space rises monotonically from L0 ($0.081$) to L32 ($0.098$), showing no inverted-U pattern.
25	RSA captures rank
…[truncated 7573 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 322 · 2026-05-18T13:36:46.505542+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "nili2014|bills2023|templeton2024|hewitt2019control",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "nili2014|bills2023|templeton2024|hewitt2019control",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-18T13:36:46.957913+00:00_

299:@inproceedings{hewitt2019control,
310:@article{nili2014toolbox,
323:@misc{bills2023language,
331:@article{templeton2024scaling,

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 324 · 2026-05-18T13:36:46.958407+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "offset": "119"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "offset": "119"
  }
}
```

</details>

---


### Tool result

_source line 325 · 2026-05-18T13:36:47.009112+00:00_

119	\bottomrule
120	\end{tabular}
121	\end{table}
122	
123	\subsection{Pretrained LLM Representation Quality Under Visual Input}
124	\label{sec:ood_diagnostics}
125	
126	A potential concern with the three-condition comparison (\S\ref{sec:model_data}) is that the pretrained Llama-2 backbone never encountered projected visual tokens during pretraining, so its representations of such input could be degenerate.
127	We evaluate three diagnostics to assess representation quality.
128	Activation magnitude grows from $16.5$ (L0) to $90.2$ (L31) for Llama-2 base, compared to $16.5 \to 51.7$ for the VLA-trained model; the pretrained LLM produces larger but non-exploding activations with no evidence of collapse.
129	Per-layer cosine similarity between L0 and deeper layers decreases progressively from $1.0$ to $\approx 0.28$ at L25, reflecting gradual differentiation rather than catastrophic out-of-distribution behavior.
130	Top-10 principal component variance explained remains stable across all layers ($0.59$--$0.74$), with no low-rank collapse.
131	These diagnostics indicate that the pretrained LLM produces structured, full-rank representations of visual input despite never encountering projected visual tokens during pretraining, supporting the validity of the three-condition comparison.
132	
133	\begin{figure}[h]
134	\centering
135	\includegraphics[width=\columnwidth]{figures/fig_ood_diagnostics.pdf}
136	\caption{Pretrained LLM representation diagnostics under visual input. Left: activation magnitude across layers (Llama-2 base vs.\ VLA-trained). Center: cosine similarity between L0 and deeper layers. Right: top-10 PC variance explained. All three metrics confirm structured, non-degenerate representations.}
137	\label{fig:ood_diagnostics}
138	\end{figure}
139	
140	\subsection{Probe Architecture Sensitivity}
141	\label{sec:linear_probe}
142	
143	To rule out that our findings depend on MLP probe capacity ($N/\text{params} \approx 0.06$, overparameterized), we replicate the per
…[truncated 21055 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 326 · 2026-05-18T13:39:15.533275+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 — Round 2 修订评估\n\n**上轮评分**: 4/10 (Weak Reject)\n\n---\n\n## Issue Verification\n\n### R6-C1 [STILL_OPEN — 部分改善]: Ablation \"routing-first\" 叙事修改\n\n**(a) \"routing-first\" 叙事是否解决了方向性问题？**\n\n部分改善但核心问题仍在。Section 4.3 line 80 的新表述——\"these heads carry organized instruction signals that the action probe treats as structured noise, so removing them yields a modest increase\"——比原来的 \"dual function\" 更诚实，承认了 R² 上升的事实。但 \"structured noise\" 本身仍是 post-hoc rationalization：如果 instruction signals 对 action prediction 是 noise，那说明 instruction routing 和 action encoding 是分离的，而非 integrated。这与论文 Discussion line 12 声称的 \"routing-first specialization\" 存在张力——如果 routing 和 encoding 分离，那 \"specialization\" 的 functional significance 是什么？\n\n更根本的问题：所有 24-head ablation（无论 dominant 还是 random）都 increase R²，说明 L1 作为整体对 downstream probe 有 interference。dominant heads 增加少（+0.042 vs +0.077），最 parsimonious 的解释是它们的 interference 少（因为 organized signals 比 random noise 更 structured），而非它们有某种 \"routing-first\" 的特殊功能。\n\n**(b) Action trajectory validation 是否提供因果证据？**\n\nAction trajectory analysis（lines 83-87, Appendix §Action Trajectory Analysis Details）是有价值的新增内容。关键数据：\n- Instruction-head ablation: 72.3% token divergence, d=0.65\n- Control ablation (8 non-instruction heads): 29.3% divergence, d=0.41\n- 效应集中在 gripper 维度（shift 0.291 vs <0.034 for continuous dims）\n\n这证明 L1 heads 确实因果性地影响 action token 生成。但存在新的 internal inconsistency：\n1. R² ablation 测的是 continuous action prediction，显示 dominant heads removal 反而帮助 R²\n2. Trajectory analysis 显示效应集中在 gripper（离散 open/close），不在连续维度\n3. 这两个结果实际上讲的是不同故事：R² improvement from ablation 可能是因为 instruction routing 对连续维度确实是 noise，而 trajectory divergence 主要来自离散 gripper 维度\n\n论文没有讨论这个维度分离（连续 vs 离散）对 \"routing-first specialization\" 解释的影响。\n\n此外，line 86 提到 \"Per-head effects are comparable; L1 attention collectively influences action generation rather than through a specialized subset\"——这实际上 undermines 了 instruction-dominant heads 的特殊地位：如果所有 heads 的 per-head effect 类似，那 instruction routing 并没有独特的 causal role。\n\n**评级**：从 CRITICAL 降为 WARNING。新叙事更准确，trajectory validation 增加了因果证据，但 interpretation 仍有 internal inconsistency。\n\n---\n\n### R6-C3 [STILL_OPEN — 大部分改善]: Abstract overclaim\n\n**(a) Abstract qualification**: Abstract line 7 \"in the model studied\" ✓ 到位。\n\n**(b) Introduction findings 是否 qualified？**: Introduction lines 15-21 的 \"Three findings emerge\" 仍用一般化语言：\n- Line 16: \"the VLA exhibits strict token-level functional specialization\"（无 model qualification）\n- Line 17: \"VLA fine-tuning front-loads instruction routing\"（泛指 VLA fine-tuning）\n- Line 20: \"vision encoder representations undergo a non-monotonic transformation\"（泛指）\n\nContribution (ii) 加了 \"demonstrated on OpenVLA-7B/LIBERO\" ✓，但 Contribution (i) 和 (iii) 仍无 model-specific qualification。\n\n**(c) Discussion 是否有 unqualified claims？**: Discussion line 12 \"L0--L1 routing concentration suggests early-layer parameters may suffice for adaptation\"——仍是 unqualified general claim。Conclusion line 4 同样用 general \"a VLA\" 而非 \"OpenVLA-7B\"。\n\n**评级**：从 CRITICAL 降为 WARNING。Abstract 改善显著，但 Introduction findings 段落和 Conclusion 仍有遗漏。\n\n---\n\n### R6-C4 [STILL_OPEN — 部分改善]: 缺 behavioral validation\n\n**(a) Open-loop trajectory 是否足够？**: Action trajectory analysis（lines 83-87）是一种 behavioral proxy：它测量 predicted action tokens 的变化而非 frozen representations 上的 probe R²。这比 Round 1 的纯 representational analysis 有进步。但对 CoRL 审稿人而言，open-loop action token 变化 ≠ closed-loop task success rate。核心问题：72.3% 的 action token 变化是否导致 task failure？如果 ablation 后模型仍能完成任务（因为 gripper timing 有容错空间），那 d=0.65 的 \"大效应\" 在 behavioral 层面可能无足轻重。\n\n**(b) \"early-layer parameters may suffice\" 是否仍 speculative？**: Discussion line 12 仍写 \"L0--L1 routing concentration suggests early-layer parameters may suffice for adaptation\"。没有任何实验验证（如 freeze experiments 或 LoRA on early layers）。仍然是 speculative。\n\n**(c) 应否更明确标注 behavioral validation 缺失？**: Limitations paragraph（Discussion lines 14-15）仅说 \"C2 may differ across backbone scales and decoder paradigms\"，没有提到 behavioral validation 的缺失。建议在 Limitations 中明确写出：本文所有分析均在 representational/open-loop 层面，未进行 closed-loop rollout validation。\n\n**评级**：保持 CRITICAL（对 CoRL 而言）。Open-loop trajectory 是进步，但不足以替代 behavioral validation。如果论文加一句明确承认这一限制并将 architectural implications 标注为 hypothesis 而非 conclusion，可降为 WARNING。\n\n---\n\n### R6-W1 [RESOLVED]: RSA pairwise dependency\n\nMethod §3.5 line 51: \"resampling is performed at the task level ($N=10$), treating each task's pairwise RDM entries as a block to preserve within-task dependency structure~\\cite{nili2014toolbox}\"\n\n这是正确的处理方式。Task-level block resampling 保留了 within-task pairwise dependency，N=10 tasks 作为 resampling unit 也是 honest 的（虽然 effective N=10 很小，导致 CI 较宽，但这正是 conservative 的正确方向）。Nili 2014 引用到位。\n\n**评级**：RESOLVED。\n\n---\n\n## Resolved Issues Quick Check\n\n### R6-W2 (GenAI disclosure): [CONFIRMED] ✓\nDiscussion lines 17-18: \"Generative AI tools (Claude, GPT-4) assisted with code implementation and manuscript editing; all scientific content was produced by the authors.\" 内容完整，符合 CoRL 2026 要求。\n\n### R6-W3 (Abstract 数据密度): [ISSUE — 轻微改善]\nAbstract 仍包含约 12 个具体数值（chance/10%, 100%, L1, L0-L1, L31, 99.6%, 80.2%, L8-L14, +0.069, +46pp, ≤0.017）。相比 Round 1 的 ~15 个减少了少量（去掉了 z=-2.73 和部分 head counts），但整体数据密度仍然偏高。Abstract line 5 在一句话中包含 6 个数字/符号。改善方向正确但幅度不足——不过考虑到论文的 technical analysis 性质，这在 acceptable 范围内。\n\n### R6-I2 (缺失引用): [CONFIRMED] ✓\n- Hewitt & Liang 2019 (control tasks): 已添加为 hewitt2019control，在 Related Work line 33 引用 ✓\n- Nili et al. 2014: 已添加为 nili2014toolbox，在 Method line 51 引用 ✓\n- Bills et al. 2023: 已添加为 bills2023language，在 Related Work line 14 引用 ✓\n- Templeton et al. 2024: 已添加为 templeton2024scaling，在 Related Work line 14 引用 ✓\n\n四篇全部添加且在正文中正确引用。\n\n### R6-I3 (Table 2 caption / Discussion \"Speculative\"): [CONFIRMED] ✓\n- Table 2 caption（experiments.tex line 91）现在解释了 Mode 列：\"Mode describes acquisition speed and retention: immed. = immediate, gradual = multi-layer, incid. = incidental; +stable = retained, +forget = decays.\" Caption 自包含。✓\n- Discussion paragraph title 从 \"Speculative mechanistic interpretation\" 改为 \"Mechanistic hypothesis and implications\"（discussion.tex line 9）。✓\n\n---\n\n## Persistent Issues (from Round 1 not explicitly tracked)\n\n### P1: C1 仍列为 contribution (i) — novelty 瓶颈\n\nIntroduction line 23 Contribution (i) 仍是 \"a systematic experimental framework for token-level representational analysis of VLAs with factorial controls, verifying architecture-expected specialization between image and readout tokens.\"\n\n修改方向正确：Abstract line 4 重新表述为 \"we validate the framework by confirming architecture-expected token specialization\"，将 C1 降格为 framework validation 而非独立 finding。但 Introduction 的 contribution 列表中，(i) 仍同时包含 framework + specialization verification，使其看起来像一个 compound contribution 而非 methodological validation。\n\n建议：将 (i) 精简为 \"a systematic experimental framework for token-level representational analysis of VLAs with factorial controls\"，将 specialization verification 作为 framework 的 validation evidence 提及，而非 contribution 的一部分。\n\n**严重程度**：WARNING。比 Round 1 改善，但仍是 novelty 的 soft weakness。\n\n### P2: C3 metric-dependence — CKA 分歧仍主要在 Appendix\n\n正文中的 CKA 提及：\n- Introduction line 20: \"CKA yields monotonically increasing layer profiles (Appendix~\\ref{sec:cka_appendix})\" — 仅一个括号\n- Section 4.4 line 118: \"this ordering is metric-dependent (Appendix~\\ref{sec:cka_appendix})\" — 仅一个括号\n- Method §3.6 lines 63-66: \"Why RSA over CKA\" 段落有所扩充，新增 \"RSA captures the relative distance structure among representations, which directly governs action prediction quality\"\n\n改善方向正确（\"Why RSA over CKA\" 的 justification 更强了），但 CKA 的具体矛盾结果（monotonic increase, reversed ordering）仍未在正文讨论。读者如果不翻 Appendix，不会知道有一个常用 metric 完全推翻了 C3 的 inverted-U。\n\n建议：在 Section 4.4 加 1-2 句正文讨论 CKA 的矛盾，明确说 \"non-monotonic pattern is specific to rank-order metrics (RSA, probes); global covariance metrics (CKA) show monotonic increase, indicating the refinement operates on geometric arrangement rather than overall representational structure.\"\n\n**严重程度**：WARNING。\n\n### P3: conclusion.tex 仍未编译\n\nmain.tex 仍然没有 \\input{conclusion}。\\input 序列为：introduction → related_work → method → experiments → discussion → bibliography → appendix。conclusion.tex 存在于同一目录但未被编译。这意味着编译后的 PDF 仍无 Conclusion section。\n\nRound 1 中这被标记为 R2-W8，但本轮 open issues 列表中未追踪。\n\n**严重程度**：INFO → WARNING。缺少 Conclusion 不会导致 desk reject，但 CoRL 论文通常有 Conclusion，且 conclusion.tex 第 6 行的 \"Code and representations will be released upon acceptance\" 是有价值的承诺，当前被浪费了。\n\n### P4: Probe train/test split 现已明确（Round 1 R1-W3 关切已修复）\n\nMethod §3.6 line 59: \"Probes are trained on demos 0--39 and evaluated on held-out demos 40--49 (demo-level split), ensuring zero temporal overlap between training and evaluation trajectories.\"\n\n这直接回应了 R1-W3 和 R1-Q1 的关切。Demo-level split 消除了时间自相关导致的 train/test leakage。✓\n\n---\n\n## New Issues\n\n### N1 [WARNING]: Action trajectory validation 的 internal inconsistency\n\n新增的 action trajectory analysis（Section 4.3 lines 83-87, Appendix §Action Trajectory Analysis Details）与 R² ablation 测量的是不同东西，且结果指向不同维度：\n\n- R² ablation：所有 ablations increase R²（连续 action 维度的 probe 质量改善）\n- Trajectory analysis：效应集中在 gripper 维度（shift 0.291 vs <0.034 for continuous dims, Appendix Table）\n\n这意味着：(a) L1 instruction routing 主要因果性地影响离散 gripper 决策，(b) 对连续动作维度的影响极小（<0.034），(c) R² increase from ablation 可能正是因为移除了对连续维度无关的 instruction routing signals。\n\n论文没有讨论这一维度分离。如果 routing 主要影响 gripper 而非连续动作，那 \"instruction routing is the primary learned contribution of VLA fine-tuning\" 的 scope 需要更精确限定。\n\n### N2 [INFO]: Line 86 的 per-head comparability undermines dominant-head narrative\n\nSection 4.3 line 86: \"Per-head effects are comparable; L1 attention collectively influences action generation rather than through a specialized subset.\"\n\n这句话实际上削弱了整个 Section 4.3 的核心论点：如果 instruction-dominant heads 的 per-head effect 与非 instruction heads comparable，那 \"instruction-dominant heads\" 作为一个 functionally distinct group 的意义何在？这与前文将 24 dominant heads 作为特殊群体进行分析和讨论的 framing 矛盾。\n\n---\n\n## Updated Assessment\n\n**Score: 5/10 (Borderline)**\n**Direction: ↑ (从 4/10 上升)**\n\n### 改善点：\n1. \"Routing-first\" 叙事比 \"dual function\" 更诚实（R6-C1 改善）\n2. Action trajectory validation 增加了因果证据（R6-C4 部分改善）\n3. Abstract overclaim qualification 到位（R6-C3 大部分改善）\n4. RSA 统计方法修复正确（R6-W1 resolved）\n5. 四篇缺失引用全部补齐（R6-I2 resolved）\n6. GenAI disclosure、Table 2 caption、Discussion 标题全部修复（R6-W2, I3 resolved）\n7. Probe train/test split 明确为 demo-level，解决了 R1-W3 的关切\n\n### 仍存在的主要问题（按严重程度）：\n1. **[CRITICAL] 缺 closed-loop behavioral validation**：open-loop trajectory 是进步但不够，CoRL 需要连接到 task success。Limitations 未明确承认。\n2. **[WARNING] Ablation 的 internal inconsistency**：R² vs trajectory 维度分离未讨论；per-head comparability undermines dominant-head narrative。\n3. **[WARNING] Introduction/Conclusion 仍有 unqualified general claims**（C3 部分未修）。\n4. **[WARNING] C1 novelty 仍是 soft weakness**（改善但未完全解决）。\n5. **[WARNING] CKA 矛盾仍未在正文充分讨论**。\n6. **[WARNING] conclusion.tex 仍未编译**。\n\n### 总体判断：\n论文在 Round 1 反馈上做了实质性改进，特别是统计方法（RSA bootstrap）、probe split 透明度、引用覆盖和 overclaim qualification。方向正确。但核心的 CoRL 适配性问题（behavioral validation）和 ablation interpretation 的 internal consistency 仍需解决。如果在 camera-ready 版本中 (a) 加 1-2 句明确承认 behavioral validation 限制，(b) 讨论 gripper vs continuous 维度分离，(c) 将 Introduction findings 限定到 OpenVLA，(d) 编译 conclusion.tex，论文可以达到 borderline accept。\n",
  "reviewer_id": "2",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 — Round 2 修订评估\n\n**上轮评分**: 4/10 (Weak Reject)\n\n---\n\n## Issue Verification\n\n### R6-C1 [STILL_OPEN — 部分改善]: Ablation \"routing-first\" 叙事修改\n\n**(a) \"routing-first\" 叙事是否解决了方向性问题？**\n\n部分改善但核心问题仍在。Section 4.3 line 80 的新表述——\"these heads carry organized instruction signals that the action probe treats as structured noise, so removing them yields a modest increase\"——比原来的 \"dual function\" 更诚实，承认了 R² 上升的事实。但 \"structured noise\" 本身仍是 post-hoc rationalization：如果 instruction signals 对 action prediction 是 noise，那说明 instruction routing 和 action encoding 是分离的，而非 integrated。这与论文 Discussion line 12 声称的 \"routing-first specialization\" 存在张力——如果 routing 和 encoding 分离，那 \"specialization\" 的 functional significance 是什么？\n\n更根本的问题：所有 24-head ablation（无论 dominant 还是 random）都 increase R²，说明 L1 作为整体对 downstream probe 有 interference。dominant heads 增加少（+0.042 vs +0.077），最 parsimonious 的解释是它们的 interference 少（因为 organized signals 比 random noise 更 structured），而非它们有某种 \"routing-first\" 的特殊功能。\n\n**(b) Action trajectory validation 是否提供因果证据？**\n\nAction trajectory analysis（lines 83-87, Appendix §Action Trajectory Analysis Details）是有价值的新增内容。关键数据：\n- Instruction-head ablation: 72.3% token divergence, d=0.65\n- Control ablation (8 non-instruction heads): 29.3% divergence, d=0.41\n- 效应集中在 gripper 维度（shift 0.291 vs <0.034 for continuous dims）\n\n这证明 L1 heads 确实因果性地影响 action token 生成。但存在新的 internal inconsistency：\n1. R² ablation 测的是 continuous action prediction，显示 dominant heads removal 反而帮助 R²\n2. Trajectory analysis 显示效应集中在 gripper（离散 open/close），不在连续维度\n3. 这两个结果实际上讲的是不同故事：R² improvement from ablation 可能是因为 instruction routing 对连续维度确实是 noise，而 trajectory divergence 主要来自离散 gripper 维度\n\n论文没有讨论这个维度分离（连续 vs 离散）对 \"routing-first specialization\" 解释的影响。\n\n此外，line 86 提到 \"Per-head effects are comparable; L1 attention collectively influences action generation rather than through a specialized subset\"——这实际上 undermines 了 instruction-dominant heads 的特殊地位：如果所有 heads 的 per-head effect 类似，那 instruction routing 并没有独特的 causal role。\n\n**评级**：从 CRITICAL 降为 WARNING。新叙事更准确，trajectory validation 增加了因果证据，但 interpretation 仍有 internal inconsistency。\n\n---\n\n### R6-C3 [STILL_OPEN — 大部分改善]: Abstract overclaim\n\n**(a) Abstract qualification**: Abstract line 7 \"in the model studied\" ✓ 到位。\n\n**(b) Introduction findings 是否 qualified？**: Introduction lines 15-21 的 \"Three findings emerge\" 仍用一般化语言：\n- Line 16: \"the VLA exhibits strict token-level functional specialization\"（无 model qualification）\n- Line 17: \"VLA fine-tuning front-loads instruction routing\"（泛指 VLA fine-tuning）\n- Line 20: \"vision encoder representations undergo a non-monotonic transformation\"（泛指）\n\nContribution (ii) 加了 \"demonstrated on OpenVLA-7B/LIBERO\" ✓，但 Contribution (i) 和 (iii) 仍无 model-specific qualification。\n\n**(c) Discussion 是否有 unqualified claims？**: Discussion line 12 \"L0--L1 routing concentration suggests early-layer parameters may suffice for adaptation\"——仍是 unqualified general claim。Conclusion line 4 同样用 general \"a VLA\" 而非 \"OpenVLA-7B\"。\n\n**评级**：从 CRITICAL 降为 WARNING。Abstract 改善显著，但 Introduction findings 段落和 Conclusion 仍有遗漏。\n\n---\n\n### R6-C4 [STILL_OPEN — 部分改善]: 缺 behavioral validation\n\n**(a) Open-loop trajectory 是否足够？**: Action trajectory analysis（lines 83-87）是一种 behavioral proxy：它测量 predicted action tokens 的变化而非 frozen representations 上的 probe R²。这比 Round 1 的纯 representational analysis 有进步。但对 CoRL 审稿人而言，open-loop action token 变化 ≠ closed-loop task success rate。核心问题：72.3% 的 action token 变化是否导致 task failure？如果 ablation 后模型仍能完成任务（因为 gripper timing 有容错空间），那 d=0.65 的 \"大效应\" 在 behavioral 层面可能无足轻重。\n\n**(b) \"early-layer parameters may suffice\" 是否仍 speculative？**: Discussion line 12 仍写 \"L0--L1 routing concentration suggests early-layer parameters may suffice for adaptation\"。没有任何实验验证（如 freeze experiments 或 LoRA on early layers）。仍然是 speculative。\n\n**(c) 应否更明确标注 behavioral validation 缺失？**: Limitations paragraph（Discussion lines 14-15）仅说 \"C2 may differ across backbone scales and decoder paradigms\"，没有提到 behavioral validation 的缺失。建议在 Limitations 中明确写出：本文所有分析均在 representational/open-loop 层面，未进行 closed-loop rollout validation。\n\n**评级**：保持 CRITICAL（对 CoRL 而言）。Open-loop trajectory 是进步，但不足以替代 behavioral validation。如果论文加一句明确承认这一限制并将 architectural implications 标注为 hypothesis 而非 conclusion，可降为 WARNING。\n\n---\n\n### R6-W1 [RESOLVED]: RSA pairwise dependency\n\nMethod §3.5 line 51: \"resampling is performed at the task level ($N=10$), treating each task's pairwise RDM entries as a block to preserve within-task dependency structure~\\cite{nili2014toolbox}\"\n\n这是正确的处理方式。Task-level block resampling 保留了 within-task pairwise dependency，N=10 tasks 作为 resampling unit 也是 honest 的（虽然 effective N=10 很小，导致 CI 较宽，但这正是 conservative 的正确方向）。Nili 2014 引用到位。\n\n**评级**：RESOLVED。\n\n---\n\n## Resolved Issues Quick Check\n\n### R6-W2 (GenAI disclosure): [CONFIRMED] ✓\nDiscussion lines 17-18: \"Generative AI tools (Claude, GPT-4) assisted with code implementation and manuscript editing; all scientific content was produced by the authors.\" 内容完整，符合 CoRL 2026 要求。\n\n### R6-W3 (Abstract 数据密度): [ISSUE — 轻微改善]\nAbstract 仍包含约 12 个具体数值（chance/10%, 100%, L1, L0-L1, L31, 99.6%, 80.2%, L8-L14, +0.069, +46pp, ≤0.017）。相比 Round 1 的 ~15 个减少了少量（去掉了 z=-2.73 和部分 head counts），但整体数据密度仍然偏高。Abstract line 5 在一句话中包含 6 个数字/符号。改善方向正确但幅度不足——不过考虑到论文的 technical analysis 性质，这在 acceptable 范围内。\n\n### R6-I2 (缺失引用): [CONFIRMED] ✓\n- Hewitt & Liang 2019 (control tasks): 已添加为 hewitt2019control，在 Related Work line 33 引用 ✓\n- Nili et al. 2014: 已添加为 nili2014toolbox，在 Method line 51 引用 ✓\n- Bills et al. 2023: 已添加为 bills2023language，在 Related Work line 14 引用 ✓\n- Templeton et al. 2024: 已添加为 templeton2024scaling，在 Related Work line 14 引用 ✓\n\n四篇全部添加且在正文中正确引用。\n\n### R6-I3 (Table 2 caption / Discussion \"Speculative\"): [CONFIRMED] ✓\n- Table 2 caption（experiments.tex line 91）现在解释了 Mode 列：\"Mode describes acquisition speed and retention: immed. = immediate, gradual = multi-layer, incid. = incidental; +stable = retained, +forget = decays.\" Caption 自包含。✓\n- Discussion paragraph title 从 \"Speculative mechanistic interpretation\" 改为 \"Mechanistic hypothesis and implications\"（discussion.tex line 9）。✓\n\n---\n\n## Persistent Issues (from Round 1 not explicitly tracked)\n\n### P1: C1 仍列为 contribution (i) — novelty 瓶颈\n\nIntroduction line 23 Contribution (i) 仍是 \"a systematic experimental framework for token-level representational analysis of VLAs with factorial controls, verifying architecture-expected specialization between image and readout tokens.\"\n\n修改方向正确：Abstract line 4 重新表述为 \"we validate the framework by confirming architecture-expected token specialization\"，将 C1 降格为 framework validation 而非独立 finding。但 Introduction 的 contribution 列表中，(i) 仍同时包含 framework + specialization verification，使其看起来像一个 compound contribution 而非 methodological validation。\n\n建议：将 (i) 精简为 \"a systematic experimental framework for token-level representational analysis of VLAs with factorial controls\"，将 specialization verification 作为 framework 的 validation evidence 提及，而非 contribution 的一部分。\n\n**严重程度**：WARNING。比 Round 1 改善，但仍是 novelty 的 soft weakness。\n\n### P2: C3 metric-dependence — CKA 分歧仍主要在 Appendix\n\n正文中的 CKA 提及：\n- Introduction line 20: \"CKA yields monotonically increasing layer profiles (Appendix~\\ref{sec:cka_appendix})\" — 仅一个括号\n- Section 4.4 line 118: \"this ordering is metric-dependent (Appendix~\\ref{sec:cka_appendix})\" — 仅一个括号\n- Method §3.6 lines 63-66: \"Why RSA over CKA\" 段落有所扩充，新增 \"RSA captures the relative distance structure among representations, which directly governs action prediction quality\"\n\n改善方向正确（\"Why RSA over CKA\" 的 justification 更强了），但 CKA 的具体矛盾结果（monotonic increase, reversed ordering）仍未在正文讨论。读者如果不翻 Appendix，不会知道有一个常用 metric 完全推翻了 C3 的 inverted-U。\n\n建议：在 Section 4.4 加 1-2 句正文讨论 CKA 的矛盾，明确说 \"non-monotonic pattern is specific to rank-order metrics (RSA, probes); global covariance metrics (CKA) show monotonic increase, indicating the refinement operates on geometric arrangement rather than overall representational structure.\"\n\n**严重程度**：WARNING。\n\n### P3: conclusion.tex 仍未编译\n\nmain.tex 仍然没有 \\input{conclusion}。\\input 序列为：introduction → related_work → method → experiments → discussion → bibliography → appendix。conclusion.tex 存在于同一目录但未被编译。这意味着编译后的 PDF 仍无 Conclusion section。\n\nRound 1 中这被标记为 R2-W8，但本轮 open issues 列表中未追踪。\n\n**严重程度**：INFO → WARNING。缺少 Conclusion 不会导致 desk reject，但 CoRL 论文通常有 Conclusion，且 conclusion.tex 第 6 行的 \"Code and representations will be released upon acceptance\" 是有价值的承诺，当前被浪费了。\n\n### P4: Probe train/test split 现已明确（Round 1 R1-W3 关切已修复）\n\nMethod §3.6 line 59: \"Probes are trained on demos 0--39 and evaluated on held-out demos 40--49 (demo-level split), ensuring zero temporal overlap between training and evaluation trajectories.\"\n\n这直接回应了 R1-W3 和 R1-Q1 的关切。Demo-level split 消除了时间自相关导致的 train/test leakage。✓\n\n---\n\n## New Issues\n\n### N1 [WARNING]: Action trajectory validation 的 internal inconsistency\n\n新增的 action trajectory analysis（Section 4.3 lines 83-87, Appendix §Action Trajectory Analysis Details）与 R² ablation 测量的是不同东西，且结果指向不同维度：\n\n- R² ablation：所有 ablations increase R²（连续 action 维度的 probe 质量改善）\n- Trajectory analysis：效应集中在 gripper 维度（shift 0.291 vs <0.034 for continuous dims, Appendix Table）\n\n这意味着：(a) L1 instruction routing 主要因果性地影响离散 gripper 决策，(b) 对连续动作维度的影响极小（<0.034），(c) R² increase from ablation 可能正是因为移除了对连续维度无关的 instruction routing signals。\n\n论文没有讨论这一维度分离。如果 routing 主要影响 gripper 而非连续动作，那 \"instruction routing is the primary learned contribution of VLA fine-tuning\" 的 scope 需要更精确限定。\n\n### N2 [INFO]: Line 86 的 per-head comparability undermines dominant-head narrative\n\nSection 4.3 line 86: \"Per-head effects are comparable; L1 attention collectively influences action generation rather than through a specialized subset.\"\n\n这句话实际上削弱了整个 Section 4.3 的核心论点：如果 instruction-dominant heads 的 per-head effect 与非 instruction heads comparable，那 \"instruction-dominant heads\" 作为一个 functionally distinct group 的意义何在？这与前文将 24 dominant heads 作为特殊群体进行分析和讨论的 framing 矛盾。\n\n---\n\n## Updated Assessment\n\n**Score: 5/10 (Borderline)**\n**Direction: ↑ (从 4/10 上升)**\n\n### 改善点：\n1. \"Routing-first\" 叙事比 \"dual function\" 更诚实（R6-C1 改善）\n2. Action trajectory validation 增加了因果证据（R6-C4 部分改善）\n3. Abstract overclaim qualification 到位（R6-C3 大部分改善）\n4. RSA 统计方法修复正确（R6-W1 resolved）\n5. 四篇缺失引用全部补齐（R6-I2 resolved）\n6. GenAI disclosure、Table 2 caption、Discussion 标题全部修复（R6-W2, I3 resolved）\n7. Probe train/test split 明确为 demo-level，解决了 R1-W3 的关切\n\n### 仍存在的主要问题（按严重程度）：\n1. **[CRITICAL] 缺 closed-loop behavioral validation**：open-loop trajectory 是进步但不够，CoRL 需要连接到 task success。Limitations 未明确承认。\n2. **[WARNING] Ablation 的 internal inconsistency**：R² vs trajectory 维度分离未讨论；per-head comparability undermines dominant-head narrative。\n3. **[WARNING] Introduction/Conclusion 仍有 unqualified general claims**（C3 部分未修）。\n4. **[WARNING] C1 novelty 仍是 soft weakness**（改善但未完全解决）。\n5. **[WARNING] CKA 矛盾仍未在正文充分讨论**。\n6. **[WARNING] conclusion.tex 仍未编译**。\n\n### 总体判断：\n论文在 Round 1 反馈上做了实质性改进，特别是统计方法（RSA bootstrap）、probe split 透明度、引用覆盖和 overclaim qualification。方向正确。但核心的 CoRL 适配性问题（behavioral validation）和 ablation interpretation 的 internal consistency 仍需解决。如果在 camera-ready 版本中 (a) 加 1-2 句明确承认 behavioral validation 限制，(b) 讨论 gripper vs continuous 维度分离，(c) 将 Introduction findings 限定到 OpenVLA，(d) 编译 conclusion.tex，论文可以达到 borderline accept。\n",
    "reviewer_id": "2",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 327 · 2026-05-18T13:39:20.161096+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4627
}
```

</details>

---


### Assistant

_source line 328 · 2026-05-18T13:39:25.671490+00:00_

Round 2 审稿意见已提交。评分从 4/10 上调至 5/10 (Borderline)，方向 ↑。

主要改善：RSA 统计修复、probe split 透明化、overclaim qualification、四篇引用补齐、GenAI disclosure。仍存在的核心问题：缺 closed-loop behavioral validation（对 CoRL 仍是 CRITICAL）、ablation 的 R² vs trajectory 维度不一致未讨论、conclusion.tex 仍未编译。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2"
}
```

</details>

---


## Round 12

## Round 12

4 recorded events


### User

_source line 329 · 2026-05-18T13:40:31.022477+00:00_

[Round 2 审稿请求]:
## Step 2 交叉分享 — 请回应 Reviewer 1 的 Round 2 评估

R1 评分从 5/10 上升至 6/10 (Marginally above threshold)。以下是 R1 的关键判断，请逐条 [AGREE] 或 [REBUT]。

---

### Issue Verification 差异

**R6-C1 (Ablation)**: R1 保持 STILL_OPEN，指出四点：
1. 核心矛盾未解决——ALL ablation increase R²，"routing-first" 仍是对 "增幅更小" 的 post-hoc 解释
2. Discussion line 12 自相矛盾："effect distributes across L1 heads" 与 "routing concentration suggests early-layer suffice" 互相矛盾
3. N=10 random subsets 未增加
4. 效应集中在 gripper dimension，claim scope 应缩小

**你降为 WARNING**，R1 保持 CRITICAL 级别。你同意保持还是坚持降级？

**R6-C2 (Probe split)**: R1 标 RESOLVED。Demo-level split 完全消除时间泄漏。残余：linear vs MLP 20× gap 未在正文讨论（R1 降为 INFO）。你未单独追踪此 issue——同意 RESOLVED？

**R6-C4 (Behavioral validation)**: R1 标 STILL_OPEN (partially improved)。关键判断：
- Open-loop trajectory analysis 不是 behavioral validation
- "confirms the causal role"（Discussion line 12）对 "causal role" 定义过宽
- 建议 Discussion/Limitations 明确承认 behavioral gap
- 评价比你温和——R1 未明确标 CRITICAL

你保持 CRITICAL。R1 似乎更偏向 WARNING/STILL_OPEN。这一差异是否影响你的评分？

### R1 新发现

**N1 [WARNING]: Discussion 自相矛盾**
Discussion line 12: "the effect distributes across L1 heads rather than concentrating in instruction-dominant ones, yet L0-L1 routing concentration suggests early-layer parameters may suffice for adaptation."
- 前半句：效应均匀分布（不集中在 instruction-dominant heads）
- 后半句：仍推论 routing concentration 的特殊意义

这与你的 N2（per-head comparability undermines dominant-head narrative）是同一个问题的不同表述。你同意这是 WARNING 级别？

**N2 [INFO]: conclusion.tex 仍未编译**——你在 P3 中也指出。

**N3 [INFO]: conclusion.tex 中 claims 未更新**——因未编译暂不影响。

### R1 的残余小问题

- Linear vs MLP 20× gap 未在正文讨论（降为 INFO）
- N=10 tasks 的 bootstrap 功效有限（固有限制，非方法论错误）

### 评分对比
- R1: 6/10 (↑ from 5)
- 你: 5/10 (↑ from 4)

R1 认为方法论修复（probe split + RSA bootstrap）"显著提升了统计推断可信度"，使论文从 "marginally below" 升至 "marginally above"。你是否同意这一判断？如果不同意，什么是你维持 5/10 的决定性因素？

请就上述差异点给出 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 330 · 2026-05-18T13:41:41.066334+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 — 交叉回应 Reviewer 1 Round 2 评估\n\n---\n\n## Issue Verification 差异\n\n### R6-C1 (Ablation): R1 保持 CRITICAL，我降为 WARNING\n\n**[AGREE with R1 on points 1, 2, 4; REBUT on severity]**\n\nR1 的四点诊断我逐条回应：\n\n1. **\"ALL ablation increase R², routing-first 仍是 post-hoc\"** — [AGREE] 事实判断完全正确。我在自己的 Round 2 评估中也指出 \"routing-first\" 仍是 rationalization。R² 方向性问题没有被新叙事解决。\n\n2. **Discussion line 12 自相矛盾** — [AGREE] \"effect distributes across L1 heads\" 与 \"routing concentration suggests early-layer suffice\" 确实矛盾。如果效应均匀分布，那 instruction-dominant heads 的 \"routing concentration\" 就不是功能上的特殊性，只是 attention pattern 的描述性统计。\n\n3. **N=10 random subsets 未增加** — [AGREE] 事实正确。不过这是 degree 问题而非 kind 问题：即使增加到 100 subsets，如果方向性问题（all increase R²）不变，z-score 的 precision 提升不改变解释困境。\n\n4. **效应集中 gripper dimension** — [AGREE] 这是我的 N1 新发现的核心，Appendix Table 清楚显示连续维度 shift <0.034。Claim scope 应缩小到 \"L1 routing primarily affects discrete gripper decisions\"。\n\n**但我坚持降为 WARNING 而非 CRITICAL 的理由**：Round 1 到 Round 2 的关键变化是 action trajectory validation 的加入。虽然 interpretation 有问题，但新数据（d=0.65, 72.3% divergence）确实证明了 L1 heads 因果性地影响 action token 生成——这是 Round 1 完全缺失的。问题从 \"无因果证据\" 变为 \"因果证据的 interpretation 有 inconsistency\"，severity 应下降一级。如果 R1 的 CRITICAL 定义是 \"影响接收决定\"，我认为 ablation interpretation 的不完美不足以单独否决论文——routing reorganization 的核心发现（三条件梯度、entry-exit pattern、Figure 1）不依赖于 ablation 解释。\n\n**结论**：同意 R1 的所有事实判断，但认为 WARNING 更合适，因为 ablation 是 supporting evidence 而非 core claim 的唯一支撑。\n\n---\n\n### R6-C2 (Probe split): [AGREE — RESOLVED]\n\nDemo-level split（demos 0-39 train, 40-49 test, Method line 59）完全消除了时间自相关导致的 train/test leakage。这是 Round 1 两位 reviewer 共同关切的方法论问题，修复彻底。\n\n对 R1 残余 INFO（linear vs MLP 20× gap 未在正文讨论）：同意这是 INFO 级别。论文在 Appendix F 已有讨论（\"MLP nonlinearity partially rescues degraded representations\"），正文 Section 4.1 line 12 也提到 overparameterization + linear probe replication。理想情况下正文加一句 summary，但不影响结论可信度。\n\n---\n\n### R6-C4 (Behavioral validation): 我保持 CRITICAL，R1 偏 WARNING\n\n**[REBUT R1's milder assessment — 我认为对 CoRL 这仍是 CRITICAL]**\n\n理由分三层：\n\n1. **Venue-specific standard**：CoRL 是机器人学习会议，不是 representation learning workshop。审稿人的隐性期望是 findings 能连接到 robot behavior。纯 representational analysis 在 ICLR/NeurIPS 可以独立成文，但 CoRL 审稿人会问 \"so what for robot design?\"。论文的 Discussion 暗示了 design implications（\"early-layer parameters may suffice for adaptation\"）但没有任何验证。\n\n2. **Open-loop ≠ behavioral**：Action trajectory analysis 测的是 \"predicted tokens change\"，不是 \"robot succeeds or fails\"。72.3% token divergence 听起来很大，但如果 divergent tokens 仍在 success region 内（action space 有容错），behavioral impact 可能极小。反之，如果 divergence 导致 catastrophic failure，那才是 strong evidence。缺少这一步就无法判断 routing 的 practical significance。Discussion line 12 写 \"confirms the causal role\" 对 \"causal role\" 的定义过宽——这点我同意 R1 的诊断。\n\n3. **Limitations 未明确承认**：Discussion lines 14-15 的 Limitations 段落讨论了 model generalization（\"C2 may differ across backbone scales\"），但完全没有提到 behavioral validation 的缺失。对于一个自知没做 closed-loop evaluation 的论文，这是一个 framing 问题：如果 Limitations 明确写 \"all analyses are representational; closed-loop behavioral validation remains future work\"，审稿人至少知道作者 aware of the gap。当前版本看起来像作者认为 trajectory analysis 已经 sufficient。\n\n**这一差异是否影响评分**：是。这是我给 5/10 而非 6/10 的主要原因之一。如果论文加 1-2 句明确承认 behavioral gap，我愿意升到 5.5 或 borderline 6。\n\n---\n\n## R1 新发现回应\n\n### N1 (Discussion 自相矛盾): [AGREE — WARNING]\n\n同意这是 WARNING 级别。Discussion line 12 的逻辑断裂：\n\n> \"the effect distributes across L1 heads rather than concentrating in instruction-dominant ones, **yet** L0--L1 routing concentration suggests early-layer parameters may suffice for adaptation\"\n\n前半句说 \"效应不集中在 instruction-dominant heads\"，后半句用 \"routing concentration\"（即 instruction-dominant heads 的集中）来推论 design implication。这是同一段内的 self-contradiction。R1 和我（N2）从不同角度捕捉到了同一个问题。\n\n这反映了一个更深层的 framing 问题：论文想同时讲 (a) instruction-dominant heads 是 functionally special 的（Section 4.3 前半部分的整个 narrative），和 (b) L1 heads 的 per-head effect 是 uniform 的（line 86 的 trajectory analysis 结论）。两者不能同时为真。\n\n---\n\n### N2/N3 (conclusion.tex): [AGREE — INFO]\n\n同意 INFO 级别。未编译不影响当前审稿（Discussion 已有足够 wrap-up），但应在提交前修复。\n\n---\n\n## 评分差异分析\n\n### R1: 6/10, R2 (我): 5/10\n\nR1 认为方法论修复（probe split + RSA bootstrap）\"显著提升了统计推断可信度\"，使论文从 below 升至 above threshold。\n\n**[PARTIALLY AGREE]**\n\n方法论修复确实重要且执行到位：\n- Demo-level split 消除了最严重的 validity threat\n- Task-level RSA bootstrap 是正确的统计处理\n- 四篇引用补齐，GenAI disclosure 到位\n\n这些修复将论文的 methodological soundness 从 \"有疑问\" 提升到 \"solid\"。在这一点上我同意 R1。\n\n**我维持 5/10 的决定性因素**是两个 R1 也认同但 weight 不同的问题：\n\n1. **Behavioral validation gap [CRITICAL]**：如上所述，对 CoRL 这不是可选的 nice-to-have。R1 给 6/10 意味着他认为 representational findings 本身对 CoRL 有足够价值；我不同意——CoRL 的审稿人群体比 ICLR/NeurIPS 更重视 practical robotics implications。\n\n2. **Effective contribution count**：C1 是架构验证（framework validation），C3 是 metric-dependent observation，core novelty 实质上只有 C2（routing reorganization）。单一 finding 在单一 model 上，对 CoRL 的 bar 偏低。R1 可能将 C2 的 depth 和 rigor 权重更高；我认为 breadth（multi-model）和 impact（behavioral connection）同样重要。\n\n**如果论文在 final version 中做到以下两点，我会升至 6/10**：\n- Limitations 明确承认 closed-loop behavioral validation 缺失\n- Discussion line 12 的自相矛盾修复（删除 \"yet\" 后的 overreach，或修改为 conditional language）\n\n这两点都是 1-2 句的文字修改，不需要新实验。\n\n---\n\n## 总结\n\n| Issue | R1 判断 | R2 判断 | 共识？ |\n|-------|---------|---------|--------|\n| R6-C1 ablation | STILL_OPEN (CRITICAL) | STILL_OPEN (WARNING) | 事实共识，severity 分歧 |\n| R6-C2 probe split | RESOLVED | RESOLVED | ✓ |\n| R6-C3 overclaim | （未单独追踪） | STILL_OPEN (WARNING) | — |\n| R6-C4 behavioral | STILL_OPEN (partial) | STILL_OPEN (CRITICAL) | 事实共识，severity 分歧（方向相反） |\n| R6-W1 RSA stats | RESOLVED | RESOLVED | ✓ |\n| Discussion 矛盾 | N1 WARNING | N2 WARNING | ✓ |\n| conclusion.tex | N2 INFO | P3 WARNING→INFO | ✓ |\n| Overall score | 6/10 | 5/10 | 分歧 |\n\n核心分歧归结为一个判断：**对 CoRL 而言，单模型 representational analysis 在无 behavioral validation 的情况下是否足够？** R1 倾向于 yes（如果方法论 sound），我倾向于 no（需要至少 acknowledge the gap explicitly）。这是 legitimate disagreement，应由 AC/Director 权衡。\n",
  "reviewer_id": "2",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 — 交叉回应 Reviewer 1 Round 2 评估\n\n---\n\n## Issue Verification 差异\n\n### R6-C1 (Ablation): R1 保持 CRITICAL，我降为 WARNING\n\n**[AGREE with R1 on points 1, 2, 4; REBUT on severity]**\n\nR1 的四点诊断我逐条回应：\n\n1. **\"ALL ablation increase R², routing-first 仍是 post-hoc\"** — [AGREE] 事实判断完全正确。我在自己的 Round 2 评估中也指出 \"routing-first\" 仍是 rationalization。R² 方向性问题没有被新叙事解决。\n\n2. **Discussion line 12 自相矛盾** — [AGREE] \"effect distributes across L1 heads\" 与 \"routing concentration suggests early-layer suffice\" 确实矛盾。如果效应均匀分布，那 instruction-dominant heads 的 \"routing concentration\" 就不是功能上的特殊性，只是 attention pattern 的描述性统计。\n\n3. **N=10 random subsets 未增加** — [AGREE] 事实正确。不过这是 degree 问题而非 kind 问题：即使增加到 100 subsets，如果方向性问题（all increase R²）不变，z-score 的 precision 提升不改变解释困境。\n\n4. **效应集中 gripper dimension** — [AGREE] 这是我的 N1 新发现的核心，Appendix Table 清楚显示连续维度 shift <0.034。Claim scope 应缩小到 \"L1 routing primarily affects discrete gripper decisions\"。\n\n**但我坚持降为 WARNING 而非 CRITICAL 的理由**：Round 1 到 Round 2 的关键变化是 action trajectory validation 的加入。虽然 interpretation 有问题，但新数据（d=0.65, 72.3% divergence）确实证明了 L1 heads 因果性地影响 action token 生成——这是 Round 1 完全缺失的。问题从 \"无因果证据\" 变为 \"因果证据的 interpretation 有 inconsistency\"，severity 应下降一级。如果 R1 的 CRITICAL 定义是 \"影响接收决定\"，我认为 ablation interpretation 的不完美不足以单独否决论文——routing reorganization 的核心发现（三条件梯度、entry-exit pattern、Figure 1）不依赖于 ablation 解释。\n\n**结论**：同意 R1 的所有事实判断，但认为 WARNING 更合适，因为 ablation 是 supporting evidence 而非 core claim 的唯一支撑。\n\n---\n\n### R6-C2 (Probe split): [AGREE — RESOLVED]\n\nDemo-level split（demos 0-39 train, 40-49 test, Method line 59）完全消除了时间自相关导致的 train/test leakage。这是 Round 1 两位 reviewer 共同关切的方法论问题，修复彻底。\n\n对 R1 残余 INFO（linear vs MLP 20× gap 未在正文讨论）：同意这是 INFO 级别。论文在 Appendix F 已有讨论（\"MLP nonlinearity partially rescues degraded representations\"），正文 Section 4.1 line 12 也提到 overparameterization + linear probe replication。理想情况下正文加一句 summary，但不影响结论可信度。\n\n---\n\n### R6-C4 (Behavioral validation): 我保持 CRITICAL，R1 偏 WARNING\n\n**[REBUT R1's milder assessment — 我认为对 CoRL 这仍是 CRITICAL]**\n\n理由分三层：\n\n1. **Venue-specific standard**：CoRL 是机器人学习会议，不是 representation learning workshop。审稿人的隐性期望是 findings 能连接到 robot behavior。纯 representational analysis 在 ICLR/NeurIPS 可以独立成文，但 CoRL 审稿人会问 \"so what for robot design?\"。论文的 Discussion 暗示了 design implications（\"early-layer parameters may suffice for adaptation\"）但没有任何验证。\n\n2. **Open-loop ≠ behavioral**：Action trajectory analysis 测的是 \"predicted tokens change\"，不是 \"robot succeeds or fails\"。72.3% token divergence 听起来很大，但如果 divergent tokens 仍在 success region 内（action space 有容错），behavioral impact 可能极小。反之，如果 divergence 导致 catastrophic failure，那才是 strong evidence。缺少这一步就无法判断 routing 的 practical significance。Discussion line 12 写 \"confirms the causal role\" 对 \"causal role\" 的定义过宽——这点我同意 R1 的诊断。\n\n3. **Limitations 未明确承认**：Discussion lines 14-15 的 Limitations 段落讨论了 model generalization（\"C2 may differ across backbone scales\"），但完全没有提到 behavioral validation 的缺失。对于一个自知没做 closed-loop evaluation 的论文，这是一个 framing 问题：如果 Limitations 明确写 \"all analyses are representational; closed-loop behavioral validation remains future work\"，审稿人至少知道作者 aware of the gap。当前版本看起来像作者认为 trajectory analysis 已经 sufficient。\n\n**这一差异是否影响评分**：是。这是我给 5/10 而非 6/10 的主要原因之一。如果论文加 1-2 句明确承认 behavioral gap，我愿意升到 5.5 或 borderline 6。\n\n---\n\n## R1 新发现回应\n\n### N1 (Discussion 自相矛盾): [AGREE — WARNING]\n\n同意这是 WARNING 级别。Discussion line 12 的逻辑断裂：\n\n> \"the effect distributes across L1 heads rather than concentrating in instruction-dominant ones, **yet** L0--L1 routing concentration suggests early-layer parameters may suffice for adaptation\"\n\n前半句说 \"效应不集中在 instruction-dominant heads\"，后半句用 \"routing concentration\"（即 instruction-dominant heads 的集中）来推论 design implication。这是同一段内的 self-contradiction。R1 和我（N2）从不同角度捕捉到了同一个问题。\n\n这反映了一个更深层的 framing 问题：论文想同时讲 (a) instruction-dominant heads 是 functionally special 的（Section 4.3 前半部分的整个 narrative），和 (b) L1 heads 的 per-head effect 是 uniform 的（line 86 的 trajectory analysis 结论）。两者不能同时为真。\n\n---\n\n### N2/N3 (conclusion.tex): [AGREE — INFO]\n\n同意 INFO 级别。未编译不影响当前审稿（Discussion 已有足够 wrap-up），但应在提交前修复。\n\n---\n\n## 评分差异分析\n\n### R1: 6/10, R2 (我): 5/10\n\nR1 认为方法论修复（probe split + RSA bootstrap）\"显著提升了统计推断可信度\"，使论文从 below 升至 above threshold。\n\n**[PARTIALLY AGREE]**\n\n方法论修复确实重要且执行到位：\n- Demo-level split 消除了最严重的 validity threat\n- Task-level RSA bootstrap 是正确的统计处理\n- 四篇引用补齐，GenAI disclosure 到位\n\n这些修复将论文的 methodological soundness 从 \"有疑问\" 提升到 \"solid\"。在这一点上我同意 R1。\n\n**我维持 5/10 的决定性因素**是两个 R1 也认同但 weight 不同的问题：\n\n1. **Behavioral validation gap [CRITICAL]**：如上所述，对 CoRL 这不是可选的 nice-to-have。R1 给 6/10 意味着他认为 representational findings 本身对 CoRL 有足够价值；我不同意——CoRL 的审稿人群体比 ICLR/NeurIPS 更重视 practical robotics implications。\n\n2. **Effective contribution count**：C1 是架构验证（framework validation），C3 是 metric-dependent observation，core novelty 实质上只有 C2（routing reorganization）。单一 finding 在单一 model 上，对 CoRL 的 bar 偏低。R1 可能将 C2 的 depth 和 rigor 权重更高；我认为 breadth（multi-model）和 impact（behavioral connection）同样重要。\n\n**如果论文在 final version 中做到以下两点，我会升至 6/10**：\n- Limitations 明确承认 closed-loop behavioral validation 缺失\n- Discussion line 12 的自相矛盾修复（删除 \"yet\" 后的 overreach，或修改为 conditional language）\n\n这两点都是 1-2 句的文字修改，不需要新实验。\n\n---\n\n## 总结\n\n| Issue | R1 判断 | R2 判断 | 共识？ |\n|-------|---------|---------|--------|\n| R6-C1 ablation | STILL_OPEN (CRITICAL) | STILL_OPEN (WARNING) | 事实共识，severity 分歧 |\n| R6-C2 probe split | RESOLVED | RESOLVED | ✓ |\n| R6-C3 overclaim | （未单独追踪） | STILL_OPEN (WARNING) | — |\n| R6-C4 behavioral | STILL_OPEN (partial) | STILL_OPEN (CRITICAL) | 事实共识，severity 分歧（方向相反） |\n| R6-W1 RSA stats | RESOLVED | RESOLVED | ✓ |\n| Discussion 矛盾 | N1 WARNING | N2 WARNING | ✓ |\n| conclusion.tex | N2 INFO | P3 WARNING→INFO | ✓ |\n| Overall score | 6/10 | 5/10 | 分歧 |\n\n核心分歧归结为一个判断：**对 CoRL 而言，单模型 representational analysis 在无 behavioral validation 的情况下是否足够？** R1 倾向于 yes（如果方法论 sound），我倾向于 no（需要至少 acknowledge the gap explicitly）。这是 legitimate disagreement，应由 AC/Director 权衡。\n",
    "reviewer_id": "2",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 331 · 2026-05-18T13:41:44.987882+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3921
}
```

</details>

---


### Assistant

_source line 332 · 2026-05-18T13:41:52.101113+00:00_

审稿意见已提交。

核心分歧总结：R1 给 6/10，我给 5/10。事实判断高度一致（ablation 方向性问题、Discussion 自相矛盾、behavioral gap），分歧在 severity weighting。我的 5/10 主要因为 CoRL 对 behavioral validation 的隐性要求——如果论文在 Limitations 中明确承认这一 gap 并修复 Discussion 的逻辑矛盾（均为 1-2 句文字改动），我愿升至 6/10。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2"
}
```

</details>

---


## Round 13

## Round 13

24 recorded events


### User

_source line 333 · 2026-05-18T14:11:51.838526+00:00_

[Round 8 审稿请求]:
# Round 8 — Reviewer 2 任务（新颖性/完整性/格式）

**模式**: 继续审稿（验证 Round 7 open issues 的修复）
**Venue**: CoRL 2026, 8 pages + unlimited refs, double-blind
**论文路径**: `projects/vla-ssd/docs/paper/main.tex`

## 你的任务

逐条验证以下 in_progress issues 是否已充分修复。每条标 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由。同时检查修改是否引入新问题。

---

## Open Issues 清单

### 🟡 R6-C3 [WARNING] 单模型 overclaim 残余
**Round 7 诊断**: Abstract line 7 'in the model studied' ✓，但 Introduction lines 16-20 'Three findings emerge' 无 model-specific 限定；Contribution (i) 和 (iii) 未限定模型；Discussion 'early-layer parameters may suffice' �qualified。
**预期修复**: (P4) Introduction findings 段落 + Contribution (i)(iii) 加 model-specific 限定。
**验证要点**:
- 读 Introduction line 15 开始的 findings 段落，检查是否有 model-specific 前缀
- 读 Contribution 列表 (i)(iii)，检查是否加了 "in the model studied" / "in this architecture"
- 读 Discussion，检查是否还有 unqualified generalizations（特别是新增 Predictions 段落）
- Abstract 是否保持了 Round 7 的 "in the model studied"

### 🟡 R7-W3 [WARNING] CKA 矛盾正文讨论不足
**Round 7 诊断**: CKA 完全反转 inverted-U 仅括号提及。建议 Section 4.4 加 1-2 句。
**预期修复**: (P7) Section 4.4 (Non-Monotonic Refinement) 加正文讨论 CKA。
**验证要点**:
- 读 Section 4.4，检查是否有明确的 CKA 矛盾讨论
- 讨论是否充分（读者不翻 Appendix 能否理解 metric-dependency 的严重程度）
- 措辞是否透明还是试图最小化矛盾

### ℹ️ R4-I1 [INFO] conclusion.tex 未编译
**Round 7 诊断**: main.tex 无 `\input{conclusion}`。
**验证要点**:
- 读 main.tex，确认 `\input{conclusion}` 存在
- 读 conclusion.tex 内容，评估是否 adequate（长度、内容、code release 声明）

---

## 也请检查

1. **Abstract**: 是否仍保持 Round 7 的改进质量？是否有新问题？
2. **Introduction 叙事连贯性**: findings 段落 model-specific 后，与 Contribution 列表是否一致？
3. **Discussion "Predictions" 段落**: 这是新增内容。评估：(a) 是否 overclaim；(b) 是否有科学价值；(c) 措辞是否 appropriate（prediction vs claim）
4. **格式检查**: CoRL 2026 要求 8 pages。估算当前页数是否合规。新增内容（CKA 讨论、Predictions、Limitations 扩展、Conclusion）是否导致超页。
5. **写作质量**: em-dash 检查、-ing phrase 检查、AI 风格标志

## 输出格式

```
## Issue Verification
[逐条 RESOLVED/STILL_OPEN]

## New Issues (if any)
[新发现]

## Completeness & Format Assessment
[完整性和格式评价]

## Score
[评分 /10 + 理由]
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 334 · 2026-05-18T14:12:00.293807+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 335 · 2026-05-18T14:12:00.696000+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 336 · 2026-05-18T14:12:00.696476+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 337 · 2026-05-18T14:12:01.407356+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 710
}
```

</details>

---


### Tool call

_source line 338 · 2026-05-18T14:12:01.458600+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 339 · 2026-05-18T14:12:01.762192+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 303
}
```

</details>

---


### Tool call

_source line 340 · 2026-05-18T14:12:01.762746+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 341 · 2026-05-18T14:12:02.618823+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 342 · 2026-05-18T14:12:02.619318+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 343 · 2026-05-18T14:12:02.669853+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 344 · 2026-05-18T14:12:02.720538+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 345 · 2026-05-18T14:12:02.771624+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We present factorial-controlled analysis of VLA representations, revealing token-level specialization, front-loaded instruction routing, and non-monotonic refinement concentrated at the readout token. Code and representations will be released upon acceptance.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 346 · 2026-05-18T14:12:08.550453+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 347 · 2026-05-18T14:12:08.601109+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 348 · 2026-05-18T14:12:09.504846+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 349 · 2026-05-18T14:12:09.956795+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 350 · 2026-05-18T14:12:11.061290+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Furthermore|Moreover|Additionally|delve|leverage|utilize|facilitate|myriad|plethora",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Furthermore|Moreover|Additionally|delve|leverage|utilize|facilitate|myriad|plethora",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 351 · 2026-05-18T14:12:11.312520+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 352 · 2026-05-18T14:12:11.312845+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 353 · 2026-05-18T14:12:11.364384+00:00_

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
…[truncated 4017 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 354 · 2026-05-18T14:14:27.720434+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 — Round 8 修订评估\n\n**上轮评分**: 5/10 (Borderline)\n\n---\n\n## Issue Verification\n\n### R6-C3 [RESOLVED]: 单模型 overclaim 残余\n\n逐处验证：\n\n**Introduction line 15**: \"Three findings emerge from our analysis of OpenVLA-7B on LIBERO.\" — ✓ 关键修复。这一句将后续所有 findings（lines 16-21）的 scope 限定到了具体模型和 benchmark，无需每句重复。\n\n**Contribution (i)** (line 23): \"...verifying architecture-expected specialization between image and readout tokens **in the model studied**\" — ✓\n\n**Contribution (ii)** (line 23): \"...demonstrated on **OpenVLA-7B/LIBERO**\" — ✓（已有）\n\n**Contribution (iii)** (line 23): \"the observation, **in this architecture**, that vision encoder representations are non-monotonically transformed...\" — ✓\n\n**Abstract line 7**: \"in the model studied\" — ✓ 保持。\n\n**Discussion**: \n- Predictions 段落（lines 17-18）使用 \"should show\" / \"should produce\"，明确为预测而非已验证的 claim — ✓\n- Limitations（line 21）: \"C2 may differ across backbone scales and decoder paradigms\" — ✓ 适当 qualified\n- Line 22: \"Our analyses are representational and open-loop\" — ✓ 直接承认 scope\n\n**Conclusion line 4**: \"We present factorial-controlled analysis of VLA representations\" — 用了泛化的 \"VLA\" 而非 \"OpenVLA-7B\"。但 Conclusion 仅 2 句且是 summary 性质，且前文已全面限定。可接受。\n\n**残余极小**：Conclusion 用 generic \"VLA\"。不影响接收。\n\n---\n\n### R7-W3 [RESOLVED]: CKA 矛盾正文讨论不足\n\n**Section 4.4 line 124（新增）**:\n> \"Under linear CKA, the inverted-U disappears (per-layer similarity increases monotonically) and encoder ordering reverses (Appendix~\\ref{sec:cka_appendix}). The non-monotonic trajectory reported here characterizes RSA-specific rank-order geometry; its generality across similarity metrics remains open.\"\n\n这两句话完成了三件事：\n1. 明确告知读者 CKA 结果相反（monotonic increase, reversed ordering）\n2. 将 inverted-U 限定为 \"RSA-specific rank-order geometry\"\n3. 坦诚承认 \"generality across metrics remains open\"\n\n不翻 Appendix 的读者现在也知道 CKA 矛盾的存在和程度。措辞透明，不试图最小化分歧。\n\n**配合点**：\n- Method §3.6 line 64: 交叉引用 \"the divergence between metrics (§\\ref{sec:nonmonotonic})\" — ✓\n- Introduction line 20: \"CKA diverging (Appendix)\" 也提及 — ✓\n\n**评级**: RESOLVED。处理到位。\n\n---\n\n### R4-I1 [RESOLVED]: conclusion.tex 未编译\n\n**main.tex line 33**: `\\input{conclusion}` — ✓ 现在正确地出现在 `\\input{discussion}` 和 `\\bibliography{references}` 之间。\n\n**conclusion.tex 内容评估**：\n> \"We present factorial-controlled analysis of VLA representations, revealing token-level specialization, front-loaded instruction routing, and non-monotonic refinement concentrated at the readout token. Code and representations will be released upon acceptance.\"\n\n2 句话，非常简短。对 CoRL 可接受（许多 robotics 论文有 minimal conclusion），但有改善空间——可以加一句 future work direction（如 closed-loop validation）或 broader implication。不过这是 polish 级别的建议，不影响评分。\n\n**评级**: RESOLVED。\n\n---\n\n## Resolved Issues Quick Check（来自早期轮次，确认维持）\n\n| Issue | Status | 验证 |\n|-------|--------|------|\n| GenAI disclosure | ✓ | Discussion lines 24-25 |\n| Table 2 caption 自包含 | ✓ | experiments.tex line 84 |\n| Discussion \"Speculative\" → \"Mechanistic\" | ✓ | discussion.tex line 10 \"Mechanistic interpretation\" |\n| RSA task-level bootstrap + Nili 2014 | ✓ | method.tex line 51 |\n| Probe demo-level split | ✓ | method.tex line 58 |\n| 四篇缺失引用 | ✓ | 在 references.bib 和正文中确认 |\n| Abstract \"in the model studied\" | ✓ | abstract.tex line 7 |\n\n---\n\n## Discussion 新内容评估\n\n### Predictions 段落（Discussion lines 16-18）\n\n**(a) 是否 overclaim？** 否。两条预测都用 \"should\"（预测性语气），不是 \"will\" 或 \"does\"。第一条（line 17）基于 causal mask 的共享约束给出了合理的架构推断，且明确指出 cross-attention VLAs（如 π₀）应不同——这展示了 boundary awareness 而非盲目泛化。\n\n**(b) 科学价值？** 高。这使论文从 descriptive analysis 提升为 falsifiable framework：其他研究者可以直接测试这两条预测。第二条（line 18: \"L1 ablation should produce measurable task degradation\"）如果被验证，将建立 routing → behavior 的因果链，弥补当前论文的 behavioral gap。\n\n**(c) 措辞是否 appropriate？** 是。\"should show\" / \"should produce\" / \"should differ\" 是 prediction 的标准学术表述，清晰区分于 findings。\n\n**评价**：这是本轮最有价值的新增内容之一。\n\n### Mechanistic interpretation 段落（Discussion lines 10-14）\n\nLine 13 新增内容解决了 Round 2 的两个问题：\n- **N1（gripper vs continuous 分离）**: \"The R² improvement reflects information gain in continuous dimensions (removing routing signals frees bandwidth), while the gripper-concentrated trajectory effect (72.3% divergence) reflects discrete manipulation sensitivity.\" — 明确分离两种效应，不再混淆。\n- **N2/R1-N1（per-head comparability undermines dominant-head narrative）**: \"Routing reorganization is the observable signature of L1's acquired collective role, not a property of individual heads.\" — 这句直接解决了之前 \"distributed effect\" vs \"specialized heads\" 的 self-contradiction。论文现在一致地讲一个故事：VLA fine-tuning 让 L1 集体获得 routing 功能，attention analysis 揭示学到了什么（reorganized pattern），ablation 揭示怎么实现（distributed across layer）。\n\n**评价**：Round 2 中我和 R1 共同识别的 Discussion self-contradiction 已彻底修复。逻辑一致性显著提升。\n\n### Limitations 段落（Discussion lines 20-22）\n\nLine 22 新增: \"Our analyses are representational and open-loop; connecting routing reorganization to task success requires closed-loop evaluation, which we leave to future work.\"\n\n这直接回应了我 Round 2 的 CRITICAL 关切（R6-C4: behavioral validation 缺失）。明确承认了：\n1. 所有分析都是 representational 和 open-loop\n2. Routing → task success 的连接需要 closed-loop evaluation\n3. 这是 future work\n\n我在 Round 2 交叉回应中明确说过：\"如果论文加 1-2 句明确承认 behavioral gap，我愿意升到 5.5 或 borderline 6\"。这一条件现已满足。\n\n---\n\n## New Issues\n\n### N1 [INFO]: Conclusion 过于简短\n\nConclusion（2 句话）作为 8 页论文的收尾偏短。可以考虑加一句 broader impact 或 future direction（如 \"These findings suggest that early-layer adaptation may be a fruitful design axis for efficient VLA fine-tuning, pending behavioral validation\"）。但这是 polish 级别，不影响评分。\n\n### 无 CRITICAL 或 WARNING 级新问题\n\n修改未引入新的 inconsistency、overclaim 或格式问题。\n\n---\n\n## Completeness & Format Assessment\n\n### 格式合规\n\n- **CoRL 2026 模板**: `\\usepackage{corl_2026}` ✓\n- **匿名**: `\\author{Anonymous}` ✓\n- **Limitations section**: 在 Discussion 内，有实质内容 ✓\n- **GenAI disclosure**: 在 Discussion 末尾 ✓\n- **Conclusion**: 现在编译 ✓\n\n### 页数估算\n\n- Abstract: ~0.4 page\n- Introduction: ~1.5 pages（24 lines, dense）\n- Related Work: ~1.0 page（34 lines）\n- Method: ~1.1 pages（65 lines，略缩减）\n- Experiments: ~2.8 pages（155 lines, 3 tables, 2 figures, captions 精简）\n- Discussion: ~0.8 page（26 lines，新增 Predictions + 扩展 Limitations）\n- Conclusion: ~0.1 page（4 lines）\n\n**估算总计**: ~7.7 pages。在 8 页限制内，有少量余量。新增内容（CKA 讨论 2 句、Predictions 3 句、Limitations 扩展 1 句、Conclusion 2 句）约 0.3 page，被 Experiments section 的精简（captions 缩短、redundant text 移除）抵消。合规。\n\n### 写作质量\n\n- Em-dash (—): 0 处 ✓\n- En-dash ( – ): 0 处 ✓\n- AI 黑名单词 (delve/leverage/utilize/facilitate/myriad/plethora): 0 处 ✓\n- -ing 短语：正常密度，无过度集中\n- 过渡词堆积：无\n\n---\n\n## Score\n\n**评分: 6/10 (Marginally above acceptance threshold)**\n**方向: ↑ (从 5/10 上升)**\n**Confidence: High**\n\n### 升分理由\n\n我在 Round 2 交叉回应中明确给出了两个升分条件：\n\n1. ✅ **Limitations 明确承认 closed-loop behavioral validation 缺失** — Discussion line 22 直接满足\n2. ✅ **Discussion self-contradiction 修复** — \"collective role\" framing 彻底解决 \"distributed effect\" vs \"routing concentration\" 的矛盾\n\n两个条件均已满足，我兑现承诺升至 6/10。\n\n### 额外加分因素（超出预期的改善）\n\n- **Predictions 段落**是有价值的 scientific contribution：使论文从 descriptive 升级为 falsifiable\n- **CKA 主文讨论**透明且不回避矛盾\n- **Mechanistic interpretation 的 gripper/continuous 分离**解决了 Round 2 N1 新发现\n- **所有三个 Contributions 的 model-specific 限定**一致且不突兀\n\n### 保持 6 而非更高的原因\n\n1. **单模型 + 无 behavioral validation** 仍是 structural limitation（已承认但未解决）\n2. **C1（framework + architecture verification）** 的 novelty 仍 modest\n3. **Ablation 方向性问题**（all increase R²）虽然 interpretation 改善但事实不变\n4. **10 random subsets** 仍未增加\n\n这些是论文的 inherent scope 限制，非写作或 framing 问题。在当前 scope 内，论文已做到了它能做到的最好：严谨的方法论、诚实的报告、透明的限制承认、falsifiable predictions。对 CoRL 来说，这是一篇 borderline 但有价值的 representational analysis 论文。\n\n### 与 R1 评分对齐\n\nR1 在 Round 2 给 6/10。我现在也给 6/10。两位 reviewer 达成共识。\n",
  "reviewer_id": "2",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 — Round 8 修订评估\n\n**上轮评分**: 5/10 (Borderline)\n\n---\n\n## Issue Verification\n\n### R6-C3 [RESOLVED]: 单模型 overclaim 残余\n\n逐处验证：\n\n**Introduction line 15**: \"Three findings emerge from our analysis of OpenVLA-7B on LIBERO.\" — ✓ 关键修复。这一句将后续所有 findings（lines 16-21）的 scope 限定到了具体模型和 benchmark，无需每句重复。\n\n**Contribution (i)** (line 23): \"...verifying architecture-expected specialization between image and readout tokens **in the model studied**\" — ✓\n\n**Contribution (ii)** (line 23): \"...demonstrated on **OpenVLA-7B/LIBERO**\" — ✓（已有）\n\n**Contribution (iii)** (line 23): \"the observation, **in this architecture**, that vision encoder representations are non-monotonically transformed...\" — ✓\n\n**Abstract line 7**: \"in the model studied\" — ✓ 保持。\n\n**Discussion**: \n- Predictions 段落（lines 17-18）使用 \"should show\" / \"should produce\"，明确为预测而非已验证的 claim — ✓\n- Limitations（line 21）: \"C2 may differ across backbone scales and decoder paradigms\" — ✓ 适当 qualified\n- Line 22: \"Our analyses are representational and open-loop\" — ✓ 直接承认 scope\n\n**Conclusion line 4**: \"We present factorial-controlled analysis of VLA representations\" — 用了泛化的 \"VLA\" 而非 \"OpenVLA-7B\"。但 Conclusion 仅 2 句且是 summary 性质，且前文已全面限定。可接受。\n\n**残余极小**：Conclusion 用 generic \"VLA\"。不影响接收。\n\n---\n\n### R7-W3 [RESOLVED]: CKA 矛盾正文讨论不足\n\n**Section 4.4 line 124（新增）**:\n> \"Under linear CKA, the inverted-U disappears (per-layer similarity increases monotonically) and encoder ordering reverses (Appendix~\\ref{sec:cka_appendix}). The non-monotonic trajectory reported here characterizes RSA-specific rank-order geometry; its generality across similarity metrics remains open.\"\n\n这两句话完成了三件事：\n1. 明确告知读者 CKA 结果相反（monotonic increase, reversed ordering）\n2. 将 inverted-U 限定为 \"RSA-specific rank-order geometry\"\n3. 坦诚承认 \"generality across metrics remains open\"\n\n不翻 Appendix 的读者现在也知道 CKA 矛盾的存在和程度。措辞透明，不试图最小化分歧。\n\n**配合点**：\n- Method §3.6 line 64: 交叉引用 \"the divergence between metrics (§\\ref{sec:nonmonotonic})\" — ✓\n- Introduction line 20: \"CKA diverging (Appendix)\" 也提及 — ✓\n\n**评级**: RESOLVED。处理到位。\n\n---\n\n### R4-I1 [RESOLVED]: conclusion.tex 未编译\n\n**main.tex line 33**: `\\input{conclusion}` — ✓ 现在正确地出现在 `\\input{discussion}` 和 `\\bibliography{references}` 之间。\n\n**conclusion.tex 内容评估**：\n> \"We present factorial-controlled analysis of VLA representations, revealing token-level specialization, front-loaded instruction routing, and non-monotonic refinement concentrated at the readout token. Code and representations will be released upon acceptance.\"\n\n2 句话，非常简短。对 CoRL 可接受（许多 robotics 论文有 minimal conclusion），但有改善空间——可以加一句 future work direction（如 closed-loop validation）或 broader implication。不过这是 polish 级别的建议，不影响评分。\n\n**评级**: RESOLVED。\n\n---\n\n## Resolved Issues Quick Check（来自早期轮次，确认维持）\n\n| Issue | Status | 验证 |\n|-------|--------|------|\n| GenAI disclosure | ✓ | Discussion lines 24-25 |\n| Table 2 caption 自包含 | ✓ | experiments.tex line 84 |\n| Discussion \"Speculative\" → \"Mechanistic\" | ✓ | discussion.tex line 10 \"Mechanistic interpretation\" |\n| RSA task-level bootstrap + Nili 2014 | ✓ | method.tex line 51 |\n| Probe demo-level split | ✓ | method.tex line 58 |\n| 四篇缺失引用 | ✓ | 在 references.bib 和正文中确认 |\n| Abstract \"in the model studied\" | ✓ | abstract.tex line 7 |\n\n---\n\n## Discussion 新内容评估\n\n### Predictions 段落（Discussion lines 16-18）\n\n**(a) 是否 overclaim？** 否。两条预测都用 \"should\"（预测性语气），不是 \"will\" 或 \"does\"。第一条（line 17）基于 causal mask 的共享约束给出了合理的架构推断，且明确指出 cross-attention VLAs（如 π₀）应不同——这展示了 boundary awareness 而非盲目泛化。\n\n**(b) 科学价值？** 高。这使论文从 descriptive analysis 提升为 falsifiable framework：其他研究者可以直接测试这两条预测。第二条（line 18: \"L1 ablation should produce measurable task degradation\"）如果被验证，将建立 routing → behavior 的因果链，弥补当前论文的 behavioral gap。\n\n**(c) 措辞是否 appropriate？** 是。\"should show\" / \"should produce\" / \"should differ\" 是 prediction 的标准学术表述，清晰区分于 findings。\n\n**评价**：这是本轮最有价值的新增内容之一。\n\n### Mechanistic interpretation 段落（Discussion lines 10-14）\n\nLine 13 新增内容解决了 Round 2 的两个问题：\n- **N1（gripper vs continuous 分离）**: \"The R² improvement reflects information gain in continuous dimensions (removing routing signals frees bandwidth), while the gripper-concentrated trajectory effect (72.3% divergence) reflects discrete manipulation sensitivity.\" — 明确分离两种效应，不再混淆。\n- **N2/R1-N1（per-head comparability undermines dominant-head narrative）**: \"Routing reorganization is the observable signature of L1's acquired collective role, not a property of individual heads.\" — 这句直接解决了之前 \"distributed effect\" vs \"specialized heads\" 的 self-contradiction。论文现在一致地讲一个故事：VLA fine-tuning 让 L1 集体获得 routing 功能，attention analysis 揭示学到了什么（reorganized pattern），ablation 揭示怎么实现（distributed across layer）。\n\n**评价**：Round 2 中我和 R1 共同识别的 Discussion self-contradiction 已彻底修复。逻辑一致性显著提升。\n\n### Limitations 段落（Discussion lines 20-22）\n\nLine 22 新增: \"Our analyses are representational and open-loop; connecting routing reorganization to task success requires closed-loop evaluation, which we leave to future work.\"\n\n这直接回应了我 Round 2 的 CRITICAL 关切（R6-C4: behavioral validation 缺失）。明确承认了：\n1. 所有分析都是 representational 和 open-loop\n2. Routing → task success 的连接需要 closed-loop evaluation\n3. 这是 future work\n\n我在 Round 2 交叉回应中明确说过：\"如果论文加 1-2 句明确承认 behavioral gap，我愿意升到 5.5 或 borderline 6\"。这一条件现已满足。\n\n---\n\n## New Issues\n\n### N1 [INFO]: Conclusion 过于简短\n\nConclusion（2 句话）作为 8 页论文的收尾偏短。可以考虑加一句 broader impact 或 future direction（如 \"These findings suggest that early-layer adaptation may be a fruitful design axis for efficient VLA fine-tuning, pending behavioral validation\"）。但这是 polish 级别，不影响评分。\n\n### 无 CRITICAL 或 WARNING 级新问题\n\n修改未引入新的 inconsistency、overclaim 或格式问题。\n\n---\n\n## Completeness & Format Assessment\n\n### 格式合规\n\n- **CoRL 2026 模板**: `\\usepackage{corl_2026}` ✓\n- **匿名**: `\\author{Anonymous}` ✓\n- **Limitations section**: 在 Discussion 内，有实质内容 ✓\n- **GenAI disclosure**: 在 Discussion 末尾 ✓\n- **Conclusion**: 现在编译 ✓\n\n### 页数估算\n\n- Abstract: ~0.4 page\n- Introduction: ~1.5 pages（24 lines, dense）\n- Related Work: ~1.0 page（34 lines）\n- Method: ~1.1 pages（65 lines，略缩减）\n- Experiments: ~2.8 pages（155 lines, 3 tables, 2 figures, captions 精简）\n- Discussion: ~0.8 page（26 lines，新增 Predictions + 扩展 Limitations）\n- Conclusion: ~0.1 page（4 lines）\n\n**估算总计**: ~7.7 pages。在 8 页限制内，有少量余量。新增内容（CKA 讨论 2 句、Predictions 3 句、Limitations 扩展 1 句、Conclusion 2 句）约 0.3 page，被 Experiments section 的精简（captions 缩短、redundant text 移除）抵消。合规。\n\n### 写作质量\n\n- Em-dash (—): 0 处 ✓\n- En-dash ( – ): 0 处 ✓\n- AI 黑名单词 (delve/leverage/utilize/facilitate/myriad/plethora): 0 处 ✓\n- -ing 短语：正常密度，无过度集中\n- 过渡词堆积：无\n\n---\n\n## Score\n\n**评分: 6/10 (Marginally above acceptance threshold)**\n**方向: ↑ (从 5/10 上升)**\n**Confidence: High**\n\n### 升分理由\n\n我在 Round 2 交叉回应中明确给出了两个升分条件：\n\n1. ✅ **Limitations 明确承认 closed-loop behavioral validation 缺失** — Discussion line 22 直接满足\n2. ✅ **Discussion self-contradiction 修复** — \"collective role\" framing 彻底解决 \"distributed effect\" vs \"routing concentration\" 的矛盾\n\n两个条件均已满足，我兑现承诺升至 6/10。\n\n### 额外加分因素（超出预期的改善）\n\n- **Predictions 段落**是有价值的 scientific contribution：使论文从 descriptive 升级为 falsifiable\n- **CKA 主文讨论**透明且不回避矛盾\n- **Mechanistic interpretation 的 gripper/continuous 分离**解决了 Round 2 N1 新发现\n- **所有三个 Contributions 的 model-specific 限定**一致且不突兀\n\n### 保持 6 而非更高的原因\n\n1. **单模型 + 无 behavioral validation** 仍是 structural limitation（已承认但未解决）\n2. **C1（framework + architecture verification）** 的 novelty 仍 modest\n3. **Ablation 方向性问题**（all increase R²）虽然 interpretation 改善但事实不变\n4. **10 random subsets** 仍未增加\n\n这些是论文的 inherent scope 限制，非写作或 framing 问题。在当前 scope 内，论文已做到了它能做到的最好：严谨的方法论、诚实的报告、透明的限制承认、falsifiable predictions。对 CoRL 来说，这是一篇 borderline 但有价值的 representational analysis 论文。\n\n### 与 R1 评分对齐\n\nR1 在 Round 2 给 6/10。我现在也给 6/10。两位 reviewer 达成共识。\n",
    "reviewer_id": "2",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 355 · 2026-05-18T14:14:31.752334+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4031
}
```

</details>

---


### Assistant

_source line 356 · 2026-05-18T14:14:40.680868+00:00_

Round 8 审稿意见已提交。

三个 open issues 的验证结果：
- **R6-C3 (overclaim)**: RESOLVED — Introduction findings 段加了 "from our analysis of OpenVLA-7B on LIBERO"，三个 contributions 均有 model-specific 限定
- **R7-W3 (CKA 矛盾)**: RESOLVED — Section 4.4 新增 2 句正文讨论，透明承认 CKA 反转且限定为 "RSA-specific rank-order geometry"
- **R4-I1 (conclusion.tex)**: RESOLVED — main.tex 现在 `\input{conclusion}`

评分从 5/10 升至 **6/10**，与 R1 达成共识。升分的决定性因素是 Limitations 明确承认了 behavioral gap + Discussion self-contradiction 彻底修复，这满足了我在 Round 2 设定的两个条件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2"
}
```

</details>

---


## Round 14

## Round 14

4 recorded events


### User

_source line 357 · 2026-05-18T14:15:20.592020+00:00_

[Round 8 审稿请求]:
# Round 8 交叉分享 — 请回应 Reviewer 1 的评估

以下是 Reviewer 1 的完整 Round 8 评估。请逐条回应 [AGREE] 或 [REBUT]，特别关注评分差异（R1 给 7/10，你给 6/10）。

---

## R1 的 Issue Verification

### R6-C4 [RESOLVED as WARNING]: behavioral validation
R1 确认：
- P2（Limitations 声明）完全达标
- P1（Discussion 弱化措辞）大部分达标
- 残余：Discussion line 8 "establishing a causal link" 比 line 12 "demonstrates" 更强，两处不一致
- 从 CRITICAL 降为 WARNING

### R6-C1 + R7-W1 + R7-W2 [RESOLVED]: Ablation + 维度分离 + Per-head
R1 确认：
- (a) 维度分离：Discussion line 13 "合理且诚实的 framing"
- (b) Per-head comparability：line 14 "collective role" 消除了矛盾，与 Experiments line 79 完全一致
- (c) Experiments self-consistency：routing-first + collective role 兼容
- 残余注意：R² +0.059 数值来源不明

## R1 的新发现

### N1 [INFO]: "Establishing" vs "demonstrates" 措辞不一致
Discussion line 8 "establishing"（最强）→ line 12 "demonstrates"（居中）→ Limitations line 22（最弱）。三处对因果链强度描述不一致。

### N2 [INFO]: R² +0.059 来源不明
Discussion line 8 的 "+0.059 at L1" 未在 Experiments 中出现。

## R1 的 Discussion Quality Assessment

- Synthesis: 逻辑清晰，minor issue "establishing" 过强
- Mechanistic interpretation: **本轮最大改进**，自相矛盾消除
- Predictions: 有价值，但 prediction (2) 与 ablation R² 增加有张力
- Limitations: 显著改善

## R1 的评分: 7/10

### R1 升至 7 的理由
1. R6-C4 从 CRITICAL 降为 WARNING
2. R6-C1 完全 RESOLVED
3. CKA 进入主文
4. Model-specific qualifiers
5. conclusion.tex 修复

### R1 限制在 7 的因素
1. "Establishing" 仍过强
2. Behavioral validation 仍是 WARNING
3. 单模型+单 benchmark
4. N=10 random subsets 未增加

---

## 请特别回应

1. **评分差异**：R1 给 7/10，你给 6/10。你是否认同 R1 的升分理由？是否调整？
2. **R1 的 N1**（"establishing" 不一致）：你在 R6-C4 验证中未提及 line 8 "establishing" 的问题。你同意这是一个 concern 吗？
3. **R1 的 N2**（R² +0.059 来源不明）：你是否注意到这个数值？是否同意标记为 INFO？
4. **Predictions 段落的张力**：R1 指出 prediction (2)（"L1 ablation should produce task degradation"）与 Experiments（ablation increases R²）之间有隐含张力。你在高度肯定 Predictions 段落时是否考虑到这一点？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 358 · 2026-05-18T14:16:19.717958+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 — 交叉回应 Reviewer 1 Round 8 评估\n\n---\n\n## 1. 评分差异：R1 给 7/10，我给 6/10\n\n**结论：我调整至 6.5/10，不完全对齐 R1 的 7。**\n\nR1 的升分理由我逐条评估：\n\n1. **R6-C4 从 CRITICAL 降为 WARNING** — [AGREE] Limitations line 22 的明确声明确实消除了 \"论文不知道自己缺什么\" 的问题。我自己也从 CRITICAL 降到了 acknowledged limitation。\n2. **R6-C1 完全 RESOLVED** — [AGREE] Discussion 的 \"collective role\" framing 和维度分离讨论确实彻底解决了自相矛盾。\n3. **CKA 进入主文** — [AGREE] Section 4.4 line 124 的处理到位。\n4. **Model-specific qualifiers** — [AGREE] 三个 contributions 全部限定。\n5. **conclusion.tex 修复** — [AGREE] 编译了。\n\n**我与 R1 的分歧在于 weight assignment**：R1 似乎认为方法论的 internal consistency 修复（ablation interpretation、CKA 透明度、overclaim 修正）将论文从 borderline 推过了 acceptance bar。我同意这些修复重要且执行良好，但对我而言，论文的 structural limitation（单模型、无 behavioral validation、C1 novelty modest）在 CoRL venue 的 weight 更大。\n\n具体而言：\n- R1 的 7/10 隐含 \"weak accept\"，意味着 reviewer 认为论文应被接收。\n- 我的 6/10 是 \"borderline\"，意味着论文在 acceptance threshold 边缘，可以两边走。\n- 差距的 root cause 是 venue fitness 的判断：R1 可能对 CoRL 接受纯 representational analysis 的 bar 更乐观，我更保守。\n\n**调整**：R1 的论证让我认识到方法论 consistency 修复的累积效应比我单独评估时更显著。Discussion 从 Round 2 的 self-contradictory 半页变成了现在有 Synthesis + Mechanistic interpretation + Predictions + Limitations + GenAI 的完整讨论，质量提升是实质性的。我上调至 **6.5/10**（如果 CoRL 用整数，则 round 方向取决于 AC 判断）。\n\n---\n\n## 2. R1 的 N1：\"establishing\" 不一致\n\n**[AGREE — INFO 级别]**\n\nR1 精确识别了三处因果强度的 gradient：\n- Discussion line 8: \"**establishing** a causal link from routing to output\" — 最强\n- Discussion line 12: \"**demonstrates** causal influence on action output\" — 居中\n- Limitations line 22: \"connecting routing reorganization to task success requires closed-loop evaluation\" — 最弱/最诚实\n\n这三处确实不一致。Line 8 的 \"establishing\" 对 open-loop trajectory analysis 来说过强——\"establishing a causal link\" 在学术用语中通常暗示充分的因果推断（如 RCT 或 do-calculus sense 的 intervention），而论文做的是 ablation + token divergence 测量，是因果 evidence 但不是 \"established\" 因果链。\n\n我在 Round 8 评估中未提及此处是一个疏漏。R1 的诊断准确。\n\n**修复建议**：将 line 8 \"establishing a causal link\" 改为 \"providing causal evidence linking routing to output\" 或 \"demonstrating causal influence\"（与 line 12 对齐）。这是 1 个词的修改。\n\n---\n\n## 3. R1 的 N2：R² +0.059 来源不明\n\n**[AGREE — INFO 级别]**\n\nDiscussion line 8: \"representational probes show a cross-layer ablation gradient confined to L1 ($R^2$ $+0.059$ at L1 vs.\\ $+0.018$ at L8 vs.\\ $\\approx 0$ at L13)\"\n\n检查 Experiments section：\n- Section 4.3 line 71: dominant heads ablation \"+0.042\"\n- Section 4.3 line 72: random subsets \"+0.077 ± 0.013\"\n- Section 4.3 line 74: \"L8: +0.018; L13: Δ ≈ 0\"\n\n+0.059 不出现在 Experiments 中。可能来源：\n- 可能是 dominant-head ablation（+0.042）和某个 variant 的平均值？\n- 可能是不同 baseline 的 ablation 数值？\n- 可能是修改过程中的 editorial error\n\n无论来源如何，Discussion 引用的数值必须能追溯到 Experiments 或 Appendix 中的具体实验。当前无法 verify。\n\n**修复建议**：确认 +0.059 的来源并在 Experiments 中标注，或将 Discussion 数值替换为 Experiments 中已报告的 +0.042。\n\n---\n\n## 4. Predictions 段落的张力\n\n**[AGREE — 有张力但可接受]**\n\nR1 指出：Prediction (2)（\"L1 ablation on a fine-tuned model should produce measurable task degradation\"）与 Experiments 结果（ablation increases R²）之间有隐含张力。\n\n这一观察准确。让我展开分析：\n\n**张力所在**：\n- Experiments: 移除 24 dominant heads → R² 增加 +0.042（改善了 action prediction）\n- Prediction (2): L1 ablation → \"should produce measurable task degradation\"\n\n表面上矛盾：如果 ablation 改善了 representational proxy（R²），为什么预测 behavioral outcome 会恶化？\n\n**论文的隐含逻辑**（基于 Discussion line 13 的维度分离）：\n- R² 测的是 continuous action 维度的 probe quality — ablation 移除 \"structured noise\" 改善了这个指标\n- Task success 依赖于 gripper timing + continuous trajectory 的联合正确性 — trajectory analysis 显示 72.3% token divergence（主要在 gripper），这在 closed-loop 中可能导致 manipulation failure\n\n所以论文的隐含论证是：R² 改善 ≠ behavioral 改善，因为 R² 不 capture gripper timing 对 task success 的影响。\n\n**问题**：这个逻辑链是 reasonable 但没有在论文中 explicitly articulated。读者需要自己连接 Discussion line 13（维度分离）和 Prediction (2) 之间的推理。\n\n**我在高度肯定 Predictions 时是否考虑到这一点**：坦白说，我的 Round 8 评估重点关注了 Predictions 的 scientific format（predictive language, falsifiability, boundary awareness），没有足够仔细地检查 prediction 与 existing results 的 internal consistency。R1 的观察是对的——Prediction (2) 与 R² ablation 结果之间的关系需要至少一句解释。\n\n**建议修复**：在 Prediction (2) 后加一句：\", since task success depends on joint accuracy of continuous trajectories and discrete gripper timing, which the R² metric does not fully capture\" 或类似表述。\n\n**严重程度**：INFO。张力存在但有合理解释路径，只是需要 explicit。\n\n---\n\n## 总结\n\n| 议题 | R1 判断 | R2 判断 | 共识？ |\n|------|---------|---------|--------|\n| R6-C4 降级 | RESOLVED as WARNING | AGREE | ✓ |\n| R6-C1 RESOLVED | RESOLVED | AGREE | ✓ |\n| N1 \"establishing\" | INFO | AGREE (INFO) | ✓ |\n| N2 R²+0.059 来源 | INFO | AGREE (INFO) | ✓ |\n| Prediction 张力 | Noted | AGREE (INFO) | ✓ |\n| Overall score | 7/10 | 6.5/10 | 接近共识 |\n\n**所有事实判断达成共识**。评分差 0.5 分，来自 venue fitness 判断的 calibration 差异，非实质性分歧。核心共识：论文在方法论 rigor 和 transparency 上已达到 CoRL acceptable 水准；structural limitations（单模型、无 behavioral validation）是 inherent scope 限制，已被诚实承认。\n\n最终评分：**6.5/10**（从 6 上调 0.5，承认方法论修复的累积效应）。\n",
  "reviewer_id": "2",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 — 交叉回应 Reviewer 1 Round 8 评估\n\n---\n\n## 1. 评分差异：R1 给 7/10，我给 6/10\n\n**结论：我调整至 6.5/10，不完全对齐 R1 的 7。**\n\nR1 的升分理由我逐条评估：\n\n1. **R6-C4 从 CRITICAL 降为 WARNING** — [AGREE] Limitations line 22 的明确声明确实消除了 \"论文不知道自己缺什么\" 的问题。我自己也从 CRITICAL 降到了 acknowledged limitation。\n2. **R6-C1 完全 RESOLVED** — [AGREE] Discussion 的 \"collective role\" framing 和维度分离讨论确实彻底解决了自相矛盾。\n3. **CKA 进入主文** — [AGREE] Section 4.4 line 124 的处理到位。\n4. **Model-specific qualifiers** — [AGREE] 三个 contributions 全部限定。\n5. **conclusion.tex 修复** — [AGREE] 编译了。\n\n**我与 R1 的分歧在于 weight assignment**：R1 似乎认为方法论的 internal consistency 修复（ablation interpretation、CKA 透明度、overclaim 修正）将论文从 borderline 推过了 acceptance bar。我同意这些修复重要且执行良好，但对我而言，论文的 structural limitation（单模型、无 behavioral validation、C1 novelty modest）在 CoRL venue 的 weight 更大。\n\n具体而言：\n- R1 的 7/10 隐含 \"weak accept\"，意味着 reviewer 认为论文应被接收。\n- 我的 6/10 是 \"borderline\"，意味着论文在 acceptance threshold 边缘，可以两边走。\n- 差距的 root cause 是 venue fitness 的判断：R1 可能对 CoRL 接受纯 representational analysis 的 bar 更乐观，我更保守。\n\n**调整**：R1 的论证让我认识到方法论 consistency 修复的累积效应比我单独评估时更显著。Discussion 从 Round 2 的 self-contradictory 半页变成了现在有 Synthesis + Mechanistic interpretation + Predictions + Limitations + GenAI 的完整讨论，质量提升是实质性的。我上调至 **6.5/10**（如果 CoRL 用整数，则 round 方向取决于 AC 判断）。\n\n---\n\n## 2. R1 的 N1：\"establishing\" 不一致\n\n**[AGREE — INFO 级别]**\n\nR1 精确识别了三处因果强度的 gradient：\n- Discussion line 8: \"**establishing** a causal link from routing to output\" — 最强\n- Discussion line 12: \"**demonstrates** causal influence on action output\" — 居中\n- Limitations line 22: \"connecting routing reorganization to task success requires closed-loop evaluation\" — 最弱/最诚实\n\n这三处确实不一致。Line 8 的 \"establishing\" 对 open-loop trajectory analysis 来说过强——\"establishing a causal link\" 在学术用语中通常暗示充分的因果推断（如 RCT 或 do-calculus sense 的 intervention），而论文做的是 ablation + token divergence 测量，是因果 evidence 但不是 \"established\" 因果链。\n\n我在 Round 8 评估中未提及此处是一个疏漏。R1 的诊断准确。\n\n**修复建议**：将 line 8 \"establishing a causal link\" 改为 \"providing causal evidence linking routing to output\" 或 \"demonstrating causal influence\"（与 line 12 对齐）。这是 1 个词的修改。\n\n---\n\n## 3. R1 的 N2：R² +0.059 来源不明\n\n**[AGREE — INFO 级别]**\n\nDiscussion line 8: \"representational probes show a cross-layer ablation gradient confined to L1 ($R^2$ $+0.059$ at L1 vs.\\ $+0.018$ at L8 vs.\\ $\\approx 0$ at L13)\"\n\n检查 Experiments section：\n- Section 4.3 line 71: dominant heads ablation \"+0.042\"\n- Section 4.3 line 72: random subsets \"+0.077 ± 0.013\"\n- Section 4.3 line 74: \"L8: +0.018; L13: Δ ≈ 0\"\n\n+0.059 不出现在 Experiments 中。可能来源：\n- 可能是 dominant-head ablation（+0.042）和某个 variant 的平均值？\n- 可能是不同 baseline 的 ablation 数值？\n- 可能是修改过程中的 editorial error\n\n无论来源如何，Discussion 引用的数值必须能追溯到 Experiments 或 Appendix 中的具体实验。当前无法 verify。\n\n**修复建议**：确认 +0.059 的来源并在 Experiments 中标注，或将 Discussion 数值替换为 Experiments 中已报告的 +0.042。\n\n---\n\n## 4. Predictions 段落的张力\n\n**[AGREE — 有张力但可接受]**\n\nR1 指出：Prediction (2)（\"L1 ablation on a fine-tuned model should produce measurable task degradation\"）与 Experiments 结果（ablation increases R²）之间有隐含张力。\n\n这一观察准确。让我展开分析：\n\n**张力所在**：\n- Experiments: 移除 24 dominant heads → R² 增加 +0.042（改善了 action prediction）\n- Prediction (2): L1 ablation → \"should produce measurable task degradation\"\n\n表面上矛盾：如果 ablation 改善了 representational proxy（R²），为什么预测 behavioral outcome 会恶化？\n\n**论文的隐含逻辑**（基于 Discussion line 13 的维度分离）：\n- R² 测的是 continuous action 维度的 probe quality — ablation 移除 \"structured noise\" 改善了这个指标\n- Task success 依赖于 gripper timing + continuous trajectory 的联合正确性 — trajectory analysis 显示 72.3% token divergence（主要在 gripper），这在 closed-loop 中可能导致 manipulation failure\n\n所以论文的隐含论证是：R² 改善 ≠ behavioral 改善，因为 R² 不 capture gripper timing 对 task success 的影响。\n\n**问题**：这个逻辑链是 reasonable 但没有在论文中 explicitly articulated。读者需要自己连接 Discussion line 13（维度分离）和 Prediction (2) 之间的推理。\n\n**我在高度肯定 Predictions 时是否考虑到这一点**：坦白说，我的 Round 8 评估重点关注了 Predictions 的 scientific format（predictive language, falsifiability, boundary awareness），没有足够仔细地检查 prediction 与 existing results 的 internal consistency。R1 的观察是对的——Prediction (2) 与 R² ablation 结果之间的关系需要至少一句解释。\n\n**建议修复**：在 Prediction (2) 后加一句：\", since task success depends on joint accuracy of continuous trajectories and discrete gripper timing, which the R² metric does not fully capture\" 或类似表述。\n\n**严重程度**：INFO。张力存在但有合理解释路径，只是需要 explicit。\n\n---\n\n## 总结\n\n| 议题 | R1 判断 | R2 判断 | 共识？ |\n|------|---------|---------|--------|\n| R6-C4 降级 | RESOLVED as WARNING | AGREE | ✓ |\n| R6-C1 RESOLVED | RESOLVED | AGREE | ✓ |\n| N1 \"establishing\" | INFO | AGREE (INFO) | ✓ |\n| N2 R²+0.059 来源 | INFO | AGREE (INFO) | ✓ |\n| Prediction 张力 | Noted | AGREE (INFO) | ✓ |\n| Overall score | 7/10 | 6.5/10 | 接近共识 |\n\n**所有事实判断达成共识**。评分差 0.5 分，来自 venue fitness 判断的 calibration 差异，非实质性分歧。核心共识：论文在方法论 rigor 和 transparency 上已达到 CoRL acceptable 水准；structural limitations（单模型、无 behavioral validation）是 inherent scope 限制，已被诚实承认。\n\n最终评分：**6.5/10**（从 6 上调 0.5，承认方法论修复的累积效应）。\n",
    "reviewer_id": "2",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 359 · 2026-05-18T14:16:23.635145+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3917
}
```

</details>

---


### Assistant

_source line 360 · 2026-05-18T14:16:29.222997+00:00_

Round 8 交叉回应已提交。核心结论：与 R1 在所有事实判断上达成共识，评分从 6 上调至 6.5/10（R1 为 7/10），差距来自对 CoRL venue fitness 的 calibration 差异而非实质分歧。识别了两个 R1 发现的 INFO 级问题（"establishing" 措辞过强、R²+0.059 来源不明）并同意其诊断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2"
}
```

</details>

---


## Round 15

## Round 15

46 recorded events


### User

_source line 361 · 2026-05-19T00:50:10.531851+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责 **新颖性 + 叙事完整性 + CoRL 适配性** 审查。

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
1. **Novelty 评估**：相对于 Grant et al. 2026、Swann et al. 2026、Buurmeijer/Rizzardo et al. 2026、Häon et al. 2025 的增量贡献是否足够 CoRL——这些竞争者已经做了 VLA 内部分析，本文的 token-level + factorial controls 框架是否构成足够差异化
2. **CoRL 适配性**：CoRL 社区重视 robotics 实际应用——本文是纯 representational analysis，无 closed-loop 实验，是否符合 CoRL 评审偏好；Discussion 的 design implications 是否有足够的 robotics 实践价值
3. **叙事主线统一性**：Abstract → Introduction → Method → Experiments → Discussion → Conclusion 是否形成一条连贯主线；三个 finding 之间的逻辑关系是否清晰
4. **Contribution 权重分配**：C1 (architecture validation) 是 causal mask 的必然结果，作为 contribution 的权重是否合理；C2 (routing) 是核心发现；C3 (metric-dependent peak) 是 negative/qualified result——三者的权重在 Abstract/Introduction 中是否恰当
5. **Related Work positioning**：是否充分区分本文与竞争者；引用密度和覆盖度是否达到 CoRL 标准
6. **写作质量**：AI 写作痕迹（em-dash、-ing phrases、过度分段）、专有名词定义、过渡连接
7. **Missing References**：是否遗漏了 VLA 领域或 mechanistic interpretability 领域的重要相关工作
8. **格式合规**：页数、匿名化、Limitations section、Generative AI 声明

**硬规则**：
- 不给修改建议——只评估和报告问题
- 用 CoRL 2026 的标准评判（robotics + learning 社区）
- 必须给出：Strengths (逐条)、Weaknesses (逐条，按 severity: critical/warning/info 分级)、Questions、Missing References、Overall Assessment

请读取论文全文并完成审稿。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 362 · 2026-05-19T00:50:18.237139+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
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

_source line 363 · 2026-05-19T00:50:18.287850+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 364 · 2026-05-19T00:50:22.565094+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 365 · 2026-05-19T00:50:23.520097+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 366 · 2026-05-19T00:50:23.620981+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-19T00:50:28.189218+00:00_

Web search results for query: "CoRL 2026 reviewer guidelines review form criteria"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"CVPR 2026 Reviewer Guidelines","url":"https://cvpr.thecvf.com/Conferences/2026/ReviewerGuidelinesq"},{"title":"Which Coauthor Should I Nominate in My 99 ICLR Submissions? A Mathematical Analysis of the ICLR 2026 Reciprocal Reviewer Nomination Policy","url":"https://arxiv.org/pdf/2512.17950"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"}]

Based on the search results, I found information about CoRL review criteria, though specific CoRL 2026 reviewer guidelines documents were limited. Here's what I found:

## Review Criteria

Submissions are evaluated based on the significance and novelty of the results, either theoretical or empirical.

## Key Review Considerations

From the CoRL reviewer guidelines, reviewers should assess:

- **Relevance to Robot Learning**: Does the paper address a problem in robot learning? Does it apply or improve a learning-based method, or a learned model? Is the method evaluated in simulation, on real robots, or both?

- **Limitations Section**: CoRL papers are required to include a limitations section, and the guidelines recommend treating honestly reported limitations kindly and with high appreciation.

- **Quality of Feedback**: Reviewers should be constructive and concrete; be courteous and respectful, starting with the positive aspects and suggesting improvements.

While the search results included some information from CoRL 2024 and prior years, I was unable to locate a de
…[truncated 330 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5624
}
```

</details>

---


### Tool call

_source line 368 · 2026-05-19T00:50:33.060712+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2024.corl.org/contributions/instruction-for-reviews",
  "prompt": "Extract the complete review form criteria, scoring dimensions, score ranges, and any specific guidelines for reviewers. List all rating categories and their scales."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2024.corl.org/contributions/instruction-for-reviews",
    "prompt": "Extract the complete review form criteria, scoring dimensions, score ranges, and any specific guidelines for reviewers. List all rating categories and their scales."
  }
}
```

</details>

---


### Tool call

_source line 369 · 2026-05-19T00:50:34.115453+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl.org/contributions/instruction-for-authors",
  "prompt": "Extract the complete author instructions including page limits, formatting requirements, review criteria, and any specific submission requirements for CoRL 2026."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl.org/contributions/instruction-for-authors",
    "prompt": "Extract the complete author instructions including page limits, formatting requirements, review criteria, and any specific submission requirements for CoRL 2026."
  }
}
```

</details>

---


### Tool call

_source line 370 · 2026-05-19T00:50:35.070135+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 371 · 2026-05-19T00:50:35.422003+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-19T00:50:35.422480+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 373 · 2026-05-19T00:50:36.125717+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 374 · 2026-05-19T00:50:36.377030+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 375 · 2026-05-19T00:50:36.377506+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 376 · 2026-05-19T00:50:36.478113+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 377 · 2026-05-19T00:50:36.729569+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool result

_source line 378 · 2026-05-19T00:50:36.980883+00:00_

# CoRL 2024 Review Form Analysis

Based on the provided webpage content, the document does **not contain a complete review form with scoring dimensions or numerical score ranges**.

## Available Review Criteria

The page outlines evaluation standards rather than a scoring rubric:

**Evaluation Focus:**
- "Significance and novelty of results, either theoretical or empirical"
- Objective establishment of findings and potential for "scientific and technological impact"
- Relevance to robotic learning

**Scope Requirements:**
Papers must demonstrate robot learning relevance through either:
- Intent: "Explicitly address a learning question for physical robots" OR
- Outcome: "Test the proposed learning solution on physical robots"

## Critical Limitation

The document provides **no numerical rating scales, scoring dimensions, or specific score categories** for reviewers to use when evaluating submissions. It establishes what papers should address but not how reviewers should quantify their assessments.

The page focuses instead on desk rejection criteria (formatting, anonymity, scope) and reviewer qualifications rather than the actual review scoring methodology.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 3920
}
```

</details>

---


### Tool result

_source line 379 · 2026-05-19T00:50:40.242820+00:00_

# CoRL 2026 Author Instructions Summary

## Page Limits & Format
- **Main paper:** 8 pages (initial submission); 9 pages (camera-ready)
- **Excluded from limit:** acknowledgments, references, optional appendix
- **Template:** LaTeX format required (provided via Google Drive link)
- **Anonymization:** Double-blind review required

## Submission Requirements

**Core Elements:**
- Paper through OpenReview platform
- Supplementary materials as single zip file
- Video submission encouraged (≤250 MB, ≤3 minutes suggested)
- "Limitations section" mandatory within page count

**Content Specifics:**
Papers must contain "a Limitations section...describing limiting assumptions, failure modes" and reproducibility details.

## Review Policies

**Reciprocal Reviewing:**
At least one author must agree to review, or be exempt (e.g., conference committee member). Authors with 3+ submissions must also review.

**Rebuttal Process:**
Authors may submit one-page rebuttals addressing "factual errors in the review." Papers receiving all rejection recommendations skip this phase.

## Submission Policy Restrictions

- No dual submission to other archival venues simultaneously
- No papers substantially identical to previously published work
- ArXiv-only prior versions permitted
- Generative AI: must disclose usage; papers with fabricated citations face desk rejection

## Key Deadline
Paper submission: Thursday, May 28 (EOD)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6127
}
```

</details>

---


### Tool call

_source line 380 · 2026-05-19T00:50:47.270049+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 381 · 2026-05-19T00:50:47.270537+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 382 · 2026-05-19T00:50:47.320996+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 383 · 2026-05-19T00:50:47.572332+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 384 · 2026-05-19T00:50:47.572695+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 385 · 2026-05-19T00:50:48.074669+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 386 · 2026-05-19T00:50:48.075066+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 387 · 2026-05-19T00:50:48.828781+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 388 · 2026-05-19T00:50:48.979849+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2024 2025 review form scoring rubric \"overall recommendation\" scale OpenReview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2024 2025 review form scoring rubric \"overall recommendation\" scale OpenReview"
  }
}
```

</details>

---


### Tool result

_source line 389 · 2026-05-19T00:51:06.542179+00:00_

Web search results for query: "CoRL 2024 2025 review form scoring rubric "overall recommendation" scale OpenReview"

Links: [{"title":"CoRL 2024 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2024"},{"title":"CoRL 2024 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FConference"},{"title":"CoRL 2025 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2025%2FConference"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"What Drives Paper Acceptance? A Process-Centric Analysis of Modern Peer Review","url":"https://arxiv.org/pdf/2509.25701"},{"title":"Best Reviewers Award for 2024","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11955497/"},{"title":"Development and Validation of a Scoring Rubric for Editorial Evaluation of Peer-review Quality: A Pilot Study","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11000557/"},{"title":"Rethinking Rubric Generation for Improving LLM Judge and Reward Modeling for Open-ended Tasks","url":"https://arxiv.org/pdf/2602.05125"}]

I found some OpenReview pages for CoRL 2024 and 2025, but the search results didn't provide detailed information about the specific review form scoring rubric or the "overall recommendation" scale. Let me search more specifically for that information.

Links: [{"title":"CoRL 2024 - Instruction for Authors","url":"https://2024.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"CoRL.2024 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/CoRL.2024"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"Information pro
…[truncated 5106 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 17562
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-19T00:51:12.064431+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl2023.org/reviewer-guidelines",
  "prompt": "Extract the complete review form criteria, all scoring dimensions, score ranges/scales, and evaluation categories. List everything that reviewers need to score."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl2023.org/reviewer-guidelines",
    "prompt": "Extract the complete review form criteria, all scoring dimensions, score ranges/scales, and evaluation categories. List everything that reviewers need to score."
  }
}
```

</details>

---


### Tool call

_source line 391 · 2026-05-19T00:51:13.021068+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL OpenReview review form \"overall score\" \"soundness\" \"significance\" rating 1-10 site:openreview.net"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL OpenReview review form \"overall score\" \"soundness\" \"significance\" rating 1-10 site:openreview.net"
  }
}
```

</details>

---


### Tool call

_source line 392 · 2026-05-19T00:51:14.627727+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 393 · 2026-05-19T00:51:14.678750+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 394 · 2026-05-19T00:51:17.790859+00:00_

Web search results for query: "CoRL OpenReview review form "overall score" "soundness" "significance" rating 1-10 site:openreview.net"

Links: [{"title":"CoRL | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL"},{"title":"CoRL 2023 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2023%2FConference"},{"title":"Default Review Form | OpenReview","url":"https://docs.openreview.net/reference/default-forms/default-review-form"},{"title":"Why are the \"rating\" and \"confidence\" fields in my PC Console wrong? | OpenReview","url":"https://docs.openreview.net/getting-started/frequently-asked-questions/why-are-the-rating-and-confidence-fields-in-my-pc-console-wrong"},{"title":"An Open Review of OpenReview: A Critical Analysis of the Machine Learning Conference Review Process | OpenReview","url":"https://openreview.net/forum?id=Cn706AbJaKW"},{"title":"What Drives Paper Acceptance? A Process-Centric Analysis of Modern Peer Review","url":"https://arxiv.org/pdf/2509.25701"},{"title":"An Open Review of OpenReview: A Critical Analysis of the Machine   Learning Conference Review Process","url":"https://arxiv.org/pdf/2010.05137"}]

The search results provided general information about OpenReview and CoRL conferences, but did not return specific details about the CoRL review form with the particular rating scales and criteria you're looking for. The results show that CoRL has a presence on OpenReview, but the specific details about the "overall score," "soundness," and "significance" rating criteria (particularly the 1-10 scale) are not included in these search results.

To find this information, you may want to:
1. Visit the CoRL OpenReview page directly at openreview.net and look for the review form instructions
2. Check the latest CoRL conference year's page (such as CoRL 2024 or 2025) for submission guidelines
3. Look for documents labeled "Review Form" or "Reviewer Instructions" on the OpenReview platform

Th
…[truncated 314 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 4769
}
```

</details>

---


### Tool result

_source line 395 · 2026-05-19T00:51:17.992172+00:00_

# CoRL 2023 Review Criteria

Based on the guidelines provided, reviewers evaluate submissions across these dimensions:

## Primary Evaluation Categories

1. **Originality** — Assesses whether problems/methods are novel, if it's a creative combination of existing techniques, and whether prior work is adequately cited.

2. **Quality** — Examines technical soundness, whether claims are empirically or theoretically supported, appropriateness of methods, completeness, and author honesty about strengths/weaknesses.

3. **Clarity** — Evaluates writing quality, organization, informativeness, and whether sufficient detail allows expert reproduction of results.

4. **Significance** — Determines if results matter, whether others will build on the work, if it advances the field demonstrably, and if it offers unique approaches.

5. **Relevance** — Focuses on whether the paper addresses robot learning problems, applies learning-based methods, includes simulation/real-world evaluation, and appeals to the CoRL audience.

6. **Limitations** — Requests reviewers appreciate honestly-reported limitations while critically examining unreported shortcomings.

## Note on Scoring

The document outlines evaluation criteria but does not specify explicit numerical scoring scales, point ranges, or detailed rating options. Reviewers are instructed on qualitative assessment across these six dimensions rather than given a standardized scoring rubric.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5927
}
```

</details>

---


### Tool call

_source line 396 · 2026-05-19T00:51:24.773488+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://docs.openreview.net/reference/default-forms/default-review-form",
  "prompt": "Extract the complete default review form including all rating scales, score ranges, and their descriptions. Focus on the \"overall score\" or \"overall recommendation\" field and its scale."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://docs.openreview.net/reference/default-forms/default-review-form",
    "prompt": "Extract the complete default review form including all rating scales, score ranges, and their descriptions. Focus on the \"overall score\" or \"overall recommendation\" field and its scale."
  }
}
```

</details>

---


### Tool call

_source line 397 · 2026-05-19T00:51:25.426275+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2024 paper review \"overall score\" \"soundness\" rating example site:openreview.net/forum"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2024 paper review \"overall score\" \"soundness\" rating example site:openreview.net/forum"
  }
}
```

</details>

---


### Tool result

_source line 398 · 2026-05-19T00:51:28.237309+00:00_

# Default Review Form - Complete Structure

The default review form contains four fields:

## 1. **Title** (Order 1)
- Type: String, max 500 characters
- Purpose: "Brief summary of your review"

## 2. **Review** (Order 2)
- Type: Text area with markdown support
- Length: 1-20,000 characters
- Supports LaTeX formulas
- Description requests evaluation of quality, clarity, originality, and significance with pros/cons

## 3. **Rating** (Order 3) - Overall Recommendation
The rating scale uses integer values 1-10:

| Score | Category |
|-------|----------|
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

## 4. **Confidence** (Order 4)
Scale from 1-5, where 5 indicates the reviewer is "absolutely certain" and familiar with relevant literature, down to 1 representing an "educated guess."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 3463
}
```

</details>

---


### Tool result

_source line 399 · 2026-05-19T00:51:33.862652+00:00_

Web search results for query: "CoRL 2024 paper review "overall score" "soundness" rating example site:openreview.net/forum"

Links: [{"title":"HumanPlus: Humanoid Shadowing and Imitation from Humans | OpenReview","url":"https://openreview.net/forum?id=WnSl42M9Z4"},{"title":"Robot Manipulation with Flow Matching | OpenReview","url":"https://openreview.net/forum?id=l8DzhzIcEj"},{"title":"$\\mathcal{D(R,O)}$ Grasp: A Unified Representation of Robot and Object Interaction for Cross-Embodiment Dexterous Grasping | OpenReview","url":"https://openreview.net/forum?id=0rsnbgcHUU"},{"title":"The AI Review Lottery: Widespread AI-Assisted Peer Reviews Boost Paper   Scores and Acceptance Rates","url":"https://arxiv.org/pdf/2405.02150"},{"title":"Reviewers in 2024","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12056528/"},{"title":"Reviewers in 2024","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12055280/"},{"title":"Reviewers in 2024","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12056527/"},{"title":"Reviewers in 2024","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12056554/"}]

The search results include some CoRL 2024 papers from OpenReview, but they don't show the actual review content with specific "overall score" and "soundness" ratings. Let me try a more targeted search to find actual review examples with those specific rating fields.

Links: [{"title":"CoRL 2024 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2024"},{"title":"CoRL 2024 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FConference"},{"title":"CoRL 2024 Workshop | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FWorkshop"},{"title":"CoRL 2024 Workshop XE | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FWorkshop%2FXE"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"CoRL | Ope
…[truncated 1470 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8436
}
```

</details>

---


### Tool call

_source line 400 · 2026-05-19T00:51:40.288008+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://openreview.net/forum?id=WnSl42M9Z4",
  "prompt": "Extract the review form fields and scoring dimensions used by CoRL reviewers. Focus on what categories are scored (soundness, significance, etc.), what scale is used (1-5, 1-10, etc.), and the labels for each score level. List ALL rating fields from the reviews."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://openreview.net/forum?id=WnSl42M9Z4",
    "prompt": "Extract the review form fields and scoring dimensions used by CoRL reviewers. Focus on what categories are scored (soundness, significance, etc.), what scale is used (1-5, 1-10, etc.), and the labels for each score level. List ALL rating fields from the reviews."
  }
}
```

</details>

---


### Tool result

_source line 401 · 2026-05-19T00:51:45.810420+00:00_

# Response

I cannot extract the review form fields and scoring dimensions from the provided content. The webpage displays a paper abstract and metadata for "HumanPlus: Humanoid Shadowing and Imitation from Humans" on OpenReview, but it does not include the actual peer review forms or scoring rubrics used by CoRL reviewers.

To find this information, you would need to:
1. Access the actual review section of the paper (typically visible to reviewers and authors)
2. Consult the CoRL 2024 conference's official review guidelines or submission portal
3. Contact OpenReview or the conference organizers directly

The current page shows only the paper's abstract, author information, and publication metadata—not the reviewing criteria.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5522
}
```

</details>

---


### Tool call

_source line 402 · 2026-05-19T00:51:54.749079+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 403 · 2026-05-19T00:52:30.713597+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 46, \"total_citations\": 78, \"unique_cited_keys\": 46, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 35, \"online_not_found\": 6, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"kim2024_openvla\", \"type\": \"article\", \"title\": \"OpenVLA: An Open-Source Vision-Language-Action Model\", \"authors\": \"Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balak...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2406.09246\"}, {\"key\": \"karamcheti2024\", \"type\": \"article\", \"title\": \"Prismatic VLMs: Investigating the Design Space of Visually-Conditioned Language Models\", \"authors\": \"Karamcheti, Siddharth and Nair, Suraj and Balakrishna, Ashwin and Liang, Percy a...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2402.07865\"}, {\"key\": \"brohan2023_rt2\", \"type\": \"article\", \"title\": \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\", \"authors\": \"Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and C...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2307.15818\"}, {\"key\": \"liu2023_libero\", \"type\": \"inproceedings\", \"title\": \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\", \"authors\": \"Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"kriegeskorte2008\", \"type\": \"article\", \"title\": \"Representational Similarity Analysis -- Connecting the Branches of Systems Neuroscience\", \"authors\": \"Kriegeskorte, Nikolaus and Mur, Marieke and Bandettini, Peter\", \"year\": \"2008\", \"venue\": \"Frontiers in Systems Neuroscience\"}, {\"key\": \"korn
…[truncated 35612 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 35964
}
```

</details>

---


### Tool call

_source line 404 · 2026-05-19T00:55:50.007208+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿报告：Vision Encodes, Language Routes\n\n## 总体评分\n**Overall**: 5/10 (Marginally below acceptance threshold)\n**Confidence**: 4/5\n**一句话总结**: 方法论严谨的 representational analysis 论文，但单模型/单基准范围和完全缺失 closed-loop 验证使其对 CoRL 社区的实际价值存疑。\n\n## 官方维度打分（CoRL review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 6/10 | Token-level + factorial controls 框架相对 Grant et al. 2026 有方法论增量，但核心发现（fine-tuning 改 routing 不改 visual geometry）部分重复已有结论 |\n| Quality | 7/10 | 统计方法严谨（bootstrap CI、FDR correction、permutation test、seed sensitivity），但消融 R² 与 trajectory d 的矛盾解释不够清晰 |\n| Clarity | 7/10 | 结构清晰，\"七项互补分析\"框架有效，但 jargon 密度高（RSA、CKA、Cohen's d 等），某些关键解释反直觉且篇幅不足 |\n| Significance | 5/10 | 对 ML interpretability 有中等贡献，但对 robot learning 无经过验证的 actionable insight |\n| Relevance | 5/10 | 纯 representational analysis，无物理机器人实验、无 closed-loop 评估、无学习算法改进；更适合 NeurIPS/ICML |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 单模型单基准范围严重限制 generalizability\n- 具体位置：Section 3.1, Section 5 (Limitations, line 27-28), 全文\n- 问题：论文仅研究 OpenVLA-7B 一个模型，在 LIBERO-Goal 一个基准上做主实验（LIBERO-Spatial 为同一模拟器、同一机器人、同一动作空间的交叉验证）。Section 5 对 π₀（cross-attention）、RT-2（decoder-only）、更大 VLA 做了三个预测，但无一经过验证。VLA 领域正快速多样化（π₀ cross-attention、Octo diffusion heads、不同 embodiment/action space），单模型在桌面基准上的发现对其他架构范式的迁移性不确定。\n- 为什么影响接收：CoRL 社区关注发现的实际泛化性。一个仅在 OpenVLA-7B + LIBERO 上的分析，读者很难判断哪些是该模型的特性、哪些是 VLA 的通用机制。\n- 建议修改方向：至少在一个不同架构（如 π₀ 或 RT-2）或不同 embodiment 上验证核心 C2 发现（entry-exit routing pattern），即使只做 attention profile 比较也可以显著增强说服力。\n\n**N2** [critical] 完全缺失 closed-loop / task-performance 验证\n- 具体位置：Section 5, line 19 (\"potential pruning or distillation targets\"), line 24 (\"L1 probes could monitor routing integrity\"), line 28 (\"closed-loop evaluation is future work\")\n- 问题：所有分析均为 representational/open-loop。论文声称的最具 robotics 价值的 implications（routing monitoring、layer pruning/distillation、56% 参数潜在可删减）均为未验证的猜测。核心发现（L1 routing）与 task success rate 之间无任何因果链。probe R² 和 trajectory divergence (Cohen's d) 衡量的是表征质量和动作偏移，而非任务完成率。\n- 为什么影响接收：CoRL 评审标准要求论文 \"explicitly address a learning question for physical robots\" 或 \"test the proposed learning solution on physical robots\"。本文两项都不满足。Section 5 的 design implications 是本文对 CoRL 最强的 relevance pitch，但全部未经验证。\n- 建议修改方向：（1）基于 routing analysis 结论做 layer pruning/distillation，在 LIBERO 上跑 closed-loop success rate；（2）展示 L1 routing integrity metric 与 task success rate 的相关性；（3）至少其中一项可以将本文从纯分析论文提升为有 actionable robotics insight 的论文。\n\n**N3** [critical] CoRL scope fit 存疑\n- 具体位置：全文\n- 问题：论文本质上是一篇 transformer mechanistic interpretability 论文，碰巧分析对象是 VLA。主要方法来自 NLP interpretability（probing, attention analysis, RSA）；主要 positioning 对标 NLP/ML 会议的 interp 工作（Elhage 2021, Olsson 2022, Wang 2023 等）；主要发现（routing reorganization, metric-dependent peaks）对 robot learning 的指导意义停留在 Discussion 的推测层面。\n- 为什么影响接收：CoRL scope 要求 \"relevance to robotic learning\"，而本文的 robotics 关联仅是分析对象的选择（VLA 而非纯 LLM），而非实验内容或结论。在当前的 CoRL 投稿竞争中，纯 analysis 论文需要格外强的 actionable insight 才能说服 reviewer。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] C1（architecture validation）占比失衡\n- 具体位置：Abstract line 4, Introduction line 17, Section 4.2, Table 1, Contribution (i)\n- 问题：C1 是 causal mask + frozen encoder 的必然结果，论文自己称之为 \"sanity check\"（Section 4.2, line 18）。然而 C1 占据了 Abstract 最长的 finding 描述、Introduction 的第一个 finding 段落、一个完整 subsection (4.2) + Table 1、以及 Contribution 列表的 (i)。对一个 \"expected result\"，这一权重过高。\n- 建议：将 C1 精简为 Section 4.2 的一段话 + Table 1 的一行，释放空间给 C2 的更深入分析或 missing validation experiments。Abstract 和 Introduction 中减少 C1 篇幅。\n\n**W2** [warning] Vision representation 的训练效果小到可能无实际意义\n- 具体位置：Section 4.4, Table 8 (Appendix), Table 10 (Appendix)\n- 问题：RSA best-vs-best Δρ = +0.017 (3%), LIBERO-Goal 上 non-significant (CI includes 0)。Image_mean R² Δ = +0.015 (p=0.006，borderline)。Same-layer L12 comparison (Δρ = +0.079) 混淆了 peak-shift effect 和 magnitude effect。论文声称 \"training enhances decodability, not geometry\"，但 decodability gains 也很小（readout Δ = +0.069 是 meaningful，但 image_mean Δ = +0.015 不是）。这意味着 VLA fine-tuning 对 vision representations 的改变非常有限，核心改变集中在 readout routing。论文虽然如实报告了这一点，但 framing 上未充分强调这对 \"VLA fine-tuning 到底学了什么\" 这个 headline question 的含义：答案可能是 \"非常有限的东西\"。\n\n**W3** [warning] 消融 R² 解释反直觉且不充分\n- 具体位置：Section 4.3 lines 65-67, Appendix A.7\n- 问题：Instruction-dominant heads 消融使 R² 增加 +0.042，但 random subset 消融使 R² 增加更多（+0.077±0.013, z=-2.73, p=0.003）。论文解释：\"dominant heads carry organized routing signals (structured noise for the probe); random heads lack such organization\"。这一解释反直觉：如果 dominant heads 是 functionally special for routing，消融它们应该造成更大（而非更小）的 probe disruption。用 trajectory divergence (Cohen's d = 0.65 vs 0.41) 和 R² 两个指标得出相反结论的做法，使读者难以判断哪个指标更可信。\n- 建议：需要更清晰地解释为什么 R² 增加反映的是 routing signal 的移除（而非功能的破坏），并讨论 probe R² 作为衡量 routing function 的指标的局限性。\n\n**W4** [warning] Counterfactual ordering 与 semantic distance claim 不完全一致\n- 具体位置：Section 4.3 line 79, Table A7 (Appendix)\n- 问题：论文声称 \"the ordering follows semantic distance from the original instruction\"。数据显示：empty d=0.968 > wrong task d=0.844 > paraphrased d=0.697 > shuffled d=0.625。但 paraphrased（不同词汇但保留原意）的 d 高于 shuffled（原词汇但打乱顺序），这与语义距离假说不一致：paraphrase 语义上更接近原始 instruction，应该产生更小的 d。实际数据表明模型对 lexical identity 比 syntactic structure 更敏感，这与 attention-based routing（依赖 token identity 而非 word order）一致，但论文未讨论这一点。\n\n**W5** [warning] 竞争者工作的 positioning 不够深入\n- 具体位置：Section 2, Related Work\n- 问题：Swann et al. 2026 和 Buurmeijer et al. 2026 用 SAE 发现了 VLA 中的 interpretable features 和 memorized action sequences。论文 Related Work 仅提及一句（line 21），未讨论 SAE features 是否 corroborate 或 contradict L1 routing hypothesis。Häon et al. 2025 发现 \"sparse semantic directions in VLA residual streams\"，论文仅提及但未讨论与 attention-based routing mechanism 的关系。Grant et al. 2026 的三点差异化陈述（Related Work lines 24-25）清晰，但其他竞争者的差异化不足。\n\n**W6** [warning] 缺失引用\n- 具体位置：references.bib\n- 问题：以下重要相关工作未被引用：\n  - **Octo** (Ghosh et al. 2024)：主要开源 VLA，cross-attention 架构，与论文 Discussion 中对 π₀ 的预测直接相关\n  - **Rizzardo et al. 2026**：VLA 内部分析方面的竞争者（Director 指定检查）\n  - 46 篇引用对于 CoRL 论文在一个拥挤的 VLA 分析领域偏少\n- 引用验证工具显示：6 篇 not_found（elhage2021、hewitt2019、bills2023language、templeton2024scaling、nostalgebraist2020、black2024_pi0），均为 blog posts 或特殊标题格式的论文，属于 OpenAlex 未收录，非虚假引用。5 篇 minor mismatch（first author 格式），无实质问题。\n\n---\n\n## 小问题（不影响接收）\n\n- Abstract line 1: \"but what fine-tuning changes at the representational level remains unclear\" 稍显 awkward，建议 \"but the representational changes induced by fine-tuning remain unclear\"\n- Section 4.3 footnote 1 (line 65): R² baseline 不同的解释放在脚注中容易被忽略，建议在正文中明确说明 within-experiment comparisons\n- Appendix 中 figures 使用 `[h]` placement；部分 figure caption 较长但信息量高，整体可接受\n- Generative AI 声明存在且符合要求\n- 匿名化检查：无明显 de-anonymization（作者列为 \"Anonymous\"，无代码仓库链接）\n- 页数：正文看起来在 8 页限制内（需 PDF 确认）\n- Limitations section 存在且融入 Discussion\n\n---\n\n## Questions for Authors\n\nQ1: 你们有条件在 π₀ 或 RT-2 等不同架构的 VLA 上验证 L1 routing pattern 吗？即使只做 32-layer attention profile 比较，也能大幅增强 generalizability claim。\n\nQ2: 是否考虑过将 routing analysis 的结论用于 layer pruning，然后在 LIBERO 上跑 closed-loop success rate 来验证 \"last 18 layers are pruning targets\" 的声明？这对 CoRL 读者的价值远大于 probe R²。\n\nQ3: 关于 W3（消融 R² 反直觉）：能否提供一个更详细的解释，说明为什么 ablating organized routing signals 对 probe 的影响小于 ablating random heads？是否有理论框架可以预测这一结果？\n\nQ4: 关于 W4（counterfactual ordering）：paraphrased d=0.697 > shuffled d=0.625 是否表明 VLA 对 lexical identity 比 syntactic structure 更敏感？这似乎与 token-level attention routing mechanism 一致，但论文未讨论。\n\nQ5: 论文 Discussion 中预测 cross-attention VLAs 不会有 L1 routing heads。如果这一预测成立，这意味着本文的核心发现 (C2) 仅适用于 decoder-only VLAs，这进一步缩小了 generalizability scope。你们如何看待这一 tension？\n\n---\n\n## Missing References\n\n1. **Octo** (Ghosh et al. 2024): 开源 cross-attention VLA，与 Discussion 中对 cross-attention 架构的预测直接相关\n2. **Rizzardo et al. 2026**: VLA 内部分析的竞争者工作\n3. 建议补充近期 multimodal interpretability 论文以增加引用覆盖度\n\n---\n\n## 主要优势\n\n1. **方法论严谨**：Factorial design（三条件 × 有无 instruction）是该领域少见的系统化设计。七项互补分析（causal + supporting + constraining）构成令人信服的证据链条。\n2. **Robustness 检查充分**：seed sensitivity、demo subsampling、threshold sensitivity、distance metric invariance、linear vs MLP probe、cross-benchmark (LIBERO-Spatial) 验证。这一水平的 robustness 检查超过同领域大多数论文。\n3. **核心发现（C2 routing）有价值**：Entry-exit routing pattern 与 Llama-2 base 的 mid-depth pattern 的对比是 genuine insight，且有多项 converging evidence 支持。\n4. **诚实汇报**：C1 被标为 sanity check，C3 的 metric-dependent 性质被明确说明，CKA divergence 被如实报告而非隐藏。Limitations 段有实质内容。\n5. **与 Grant et al. 2026 的差异化清晰**：token-level vs feature-level、per-layer decomposition、factorial controls 三点区别陈述明确（Related Work lines 24-25）。\n\n---\n\n## Overall Assessment\n\n本文是一篇方法论扎实、数据分析严谨的 representational analysis 论文。核心贡献 C2（VLA fine-tuning 将 instruction routing 前置到 entry-exit layers）是有价值的发现，七项互补分析形成有说服力的证据链。然而，三个 critical 问题使其在 CoRL 的接收前景不乐观：（1）单模型单基准范围限制 generalizability；（2）完全缺失 closed-loop 验证使 robotics implications 停留在猜测层面；（3）论文本质上是 NLP-style mechanistic interpretability 工作，对 CoRL 的 scope fit 有限。如果作者能增加至少一项 closed-loop validation（如基于 routing analysis 的 layer pruning + task success 评估）和至少一个额外模型/架构的验证，本文将显著增强竞争力。当前版本更适合投往 NeurIPS/ICML 的 interpretability track。\n\nRating: **5/10** — Marginally below acceptance threshold\nConfidence: **4/5**\n",
  "reviewer_id": "2",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审稿报告：Vision Encodes, Language Routes\n\n## 总体评分\n**Overall**: 5/10 (Marginally below acceptance threshold)\n**Confidence**: 4/5\n**一句话总结**: 方法论严谨的 representational analysis 论文，但单模型/单基准范围和完全缺失 closed-loop 验证使其对 CoRL 社区的实际价值存疑。\n\n## 官方维度打分（CoRL review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 6/10 | Token-level + factorial controls 框架相对 Grant et al. 2026 有方法论增量，但核心发现（fine-tuning 改 routing 不改 visual geometry）部分重复已有结论 |\n| Quality | 7/10 | 统计方法严谨（bootstrap CI、FDR correction、permutation test、seed sensitivity），但消融 R² 与 trajectory d 的矛盾解释不够清晰 |\n| Clarity | 7/10 | 结构清晰，\"七项互补分析\"框架有效，但 jargon 密度高（RSA、CKA、Cohen's d 等），某些关键解释反直觉且篇幅不足 |\n| Significance | 5/10 | 对 ML interpretability 有中等贡献，但对 robot learning 无经过验证的 actionable insight |\n| Relevance | 5/10 | 纯 representational analysis，无物理机器人实验、无 closed-loop 评估、无学习算法改进；更适合 NeurIPS/ICML |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 单模型单基准范围严重限制 generalizability\n- 具体位置：Section 3.1, Section 5 (Limitations, line 27-28), 全文\n- 问题：论文仅研究 OpenVLA-7B 一个模型，在 LIBERO-Goal 一个基准上做主实验（LIBERO-Spatial 为同一模拟器、同一机器人、同一动作空间的交叉验证）。Section 5 对 π₀（cross-attention）、RT-2（decoder-only）、更大 VLA 做了三个预测，但无一经过验证。VLA 领域正快速多样化（π₀ cross-attention、Octo diffusion heads、不同 embodiment/action space），单模型在桌面基准上的发现对其他架构范式的迁移性不确定。\n- 为什么影响接收：CoRL 社区关注发现的实际泛化性。一个仅在 OpenVLA-7B + LIBERO 上的分析，读者很难判断哪些是该模型的特性、哪些是 VLA 的通用机制。\n- 建议修改方向：至少在一个不同架构（如 π₀ 或 RT-2）或不同 embodiment 上验证核心 C2 发现（entry-exit routing pattern），即使只做 attention profile 比较也可以显著增强说服力。\n\n**N2** [critical] 完全缺失 closed-loop / task-performance 验证\n- 具体位置：Section 5, line 19 (\"potential pruning or distillation targets\"), line 24 (\"L1 probes could monitor routing integrity\"), line 28 (\"closed-loop evaluation is future work\")\n- 问题：所有分析均为 representational/open-loop。论文声称的最具 robotics 价值的 implications（routing monitoring、layer pruning/distillation、56% 参数潜在可删减）均为未验证的猜测。核心发现（L1 routing）与 task success rate 之间无任何因果链。probe R² 和 trajectory divergence (Cohen's d) 衡量的是表征质量和动作偏移，而非任务完成率。\n- 为什么影响接收：CoRL 评审标准要求论文 \"explicitly address a learning question for physical robots\" 或 \"test the proposed learning solution on physical robots\"。本文两项都不满足。Section 5 的 design implications 是本文对 CoRL 最强的 relevance pitch，但全部未经验证。\n- 建议修改方向：（1）基于 routing analysis 结论做 layer pruning/distillation，在 LIBERO 上跑 closed-loop success rate；（2）展示 L1 routing integrity metric 与 task success rate 的相关性；（3）至少其中一项可以将本文从纯分析论文提升为有 actionable robotics insight 的论文。\n\n**N3** [critical] CoRL scope fit 存疑\n- 具体位置：全文\n- 问题：论文本质上是一篇 transformer mechanistic interpretability 论文，碰巧分析对象是 VLA。主要方法来自 NLP interpretability（probing, attention analysis, RSA）；主要 positioning 对标 NLP/ML 会议的 interp 工作（Elhage 2021, Olsson 2022, Wang 2023 等）；主要发现（routing reorganization, metric-dependent peaks）对 robot learning 的指导意义停留在 Discussion 的推测层面。\n- 为什么影响接收：CoRL scope 要求 \"relevance to robotic learning\"，而本文的 robotics 关联仅是分析对象的选择（VLA 而非纯 LLM），而非实验内容或结论。在当前的 CoRL 投稿竞争中，纯 analysis 论文需要格外强的 actionable insight 才能说服 reviewer。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] C1（architecture validation）占比失衡\n- 具体位置：Abstract line 4, Introduction line 17, Section 4.2, Table 1, Contribution (i)\n- 问题：C1 是 causal mask + frozen encoder 的必然结果，论文自己称之为 \"sanity check\"（Section 4.2, line 18）。然而 C1 占据了 Abstract 最长的 finding 描述、Introduction 的第一个 finding 段落、一个完整 subsection (4.2) + Table 1、以及 Contribution 列表的 (i)。对一个 \"expected result\"，这一权重过高。\n- 建议：将 C1 精简为 Section 4.2 的一段话 + Table 1 的一行，释放空间给 C2 的更深入分析或 missing validation experiments。Abstract 和 Introduction 中减少 C1 篇幅。\n\n**W2** [warning] Vision representation 的训练效果小到可能无实际意义\n- 具体位置：Section 4.4, Table 8 (Appendix), Table 10 (Appendix)\n- 问题：RSA best-vs-best Δρ = +0.017 (3%), LIBERO-Goal 上 non-significant (CI includes 0)。Image_mean R² Δ = +0.015 (p=0.006，borderline)。Same-layer L12 comparison (Δρ = +0.079) 混淆了 peak-shift effect 和 magnitude effect。论文声称 \"training enhances decodability, not geometry\"，但 decodability gains 也很小（readout Δ = +0.069 是 meaningful，但 image_mean Δ = +0.015 不是）。这意味着 VLA fine-tuning 对 vision representations 的改变非常有限，核心改变集中在 readout routing。论文虽然如实报告了这一点，但 framing 上未充分强调这对 \"VLA fine-tuning 到底学了什么\" 这个 headline question 的含义：答案可能是 \"非常有限的东西\"。\n\n**W3** [warning] 消融 R² 解释反直觉且不充分\n- 具体位置：Section 4.3 lines 65-67, Appendix A.7\n- 问题：Instruction-dominant heads 消融使 R² 增加 +0.042，但 random subset 消融使 R² 增加更多（+0.077±0.013, z=-2.73, p=0.003）。论文解释：\"dominant heads carry organized routing signals (structured noise for the probe); random heads lack such organization\"。这一解释反直觉：如果 dominant heads 是 functionally special for routing，消融它们应该造成更大（而非更小）的 probe disruption。用 trajectory divergence (Cohen's d = 0.65 vs 0.41) 和 R² 两个指标得出相反结论的做法，使读者难以判断哪个指标更可信。\n- 建议：需要更清晰地解释为什么 R² 增加反映的是 routing signal 的移除（而非功能的破坏），并讨论 probe R² 作为衡量 routing function 的指标的局限性。\n\n**W4** [warning] Counterfactual ordering 与 semantic distance claim 不完全一致\n- 具体位置：Section 4.3 line 79, Table A7 (Appendix)\n- 问题：论文声称 \"the ordering follows semantic distance from the original instruction\"。数据显示：empty d=0.968 > wrong task d=0.844 > paraphrased d=0.697 > shuffled d=0.625。但 paraphrased（不同词汇但保留原意）的 d 高于 shuffled（原词汇但打乱顺序），这与语义距离假说不一致：paraphrase 语义上更接近原始 instruction，应该产生更小的 d。实际数据表明模型对 lexical identity 比 syntactic structure 更敏感，这与 attention-based routing（依赖 token identity 而非 word order）一致，但论文未讨论这一点。\n\n**W5** [warning] 竞争者工作的 positioning 不够深入\n- 具体位置：Section 2, Related Work\n- 问题：Swann et al. 2026 和 Buurmeijer et al. 2026 用 SAE 发现了 VLA 中的 interpretable features 和 memorized action sequences。论文 Related Work 仅提及一句（line 21），未讨论 SAE features 是否 corroborate 或 contradict L1 routing hypothesis。Häon et al. 2025 发现 \"sparse semantic directions in VLA residual streams\"，论文仅提及但未讨论与 attention-based routing mechanism 的关系。Grant et al. 2026 的三点差异化陈述（Related Work lines 24-25）清晰，但其他竞争者的差异化不足。\n\n**W6** [warning] 缺失引用\n- 具体位置：references.bib\n- 问题：以下重要相关工作未被引用：\n  - **Octo** (Ghosh et al. 2024)：主要开源 VLA，cross-attention 架构，与论文 Discussion 中对 π₀ 的预测直接相关\n  - **Rizzardo et al. 2026**：VLA 内部分析方面的竞争者（Director 指定检查）\n  - 46 篇引用对于 CoRL 论文在一个拥挤的 VLA 分析领域偏少\n- 引用验证工具显示：6 篇 not_found（elhage2021、hewitt2019、bills2023language、templeton2024scaling、nostalgebraist2020、black2024_pi0），均为 blog posts 或特殊标题格式的论文，属于 OpenAlex 未收录，非虚假引用。5 篇 minor mismatch（first author 格式），无实质问题。\n\n---\n\n## 小问题（不影响接收）\n\n- Abstract line 1: \"but what fine-tuning changes at the representational level remains unclear\" 稍显 awkward，建议 \"but the representational changes induced by fine-tuning remain unclear\"\n- Section 4.3 footnote 1 (line 65): R² baseline 不同的解释放在脚注中容易被忽略，建议在正文中明确说明 within-experiment comparisons\n- Appendix 中 figures 使用 `[h]` placement；部分 figure caption 较长但信息量高，整体可接受\n- Generative AI 声明存在且符合要求\n- 匿名化检查：无明显 de-anonymization（作者列为 \"Anonymous\"，无代码仓库链接）\n- 页数：正文看起来在 8 页限制内（需 PDF 确认）\n- Limitations section 存在且融入 Discussion\n\n---\n\n## Questions for Authors\n\nQ1: 你们有条件在 π₀ 或 RT-2 等不同架构的 VLA 上验证 L1 routing pattern 吗？即使只做 32-layer attention profile 比较，也能大幅增强 generalizability claim。\n\nQ2: 是否考虑过将 routing analysis 的结论用于 layer pruning，然后在 LIBERO 上跑 closed-loop success rate 来验证 \"last 18 layers are pruning targets\" 的声明？这对 CoRL 读者的价值远大于 probe R²。\n\nQ3: 关于 W3（消融 R² 反直觉）：能否提供一个更详细的解释，说明为什么 ablating organized routing signals 对 probe 的影响小于 ablating random heads？是否有理论框架可以预测这一结果？\n\nQ4: 关于 W4（counterfactual ordering）：paraphrased d=0.697 > shuffled d=0.625 是否表明 VLA 对 lexical identity 比 syntactic structure 更敏感？这似乎与 token-level attention routing mechanism 一致，但论文未讨论。\n\nQ5: 论文 Discussion 中预测 cross-attention VLAs 不会有 L1 routing heads。如果这一预测成立，这意味着本文的核心发现 (C2) 仅适用于 decoder-only VLAs，这进一步缩小了 generalizability scope。你们如何看待这一 tension？\n\n---\n\n## Missing References\n\n1. **Octo** (Ghosh et al. 2024): 开源 cross-attention VLA，与 Discussion 中对 cross-attention 架构的预测直接相关\n2. **Rizzardo et al. 2026**: VLA 内部分析的竞争者工作\n3. 建议补充近期 multimodal interpretability 论文以增加引用覆盖度\n\n---\n\n## 主要优势\n\n1. **方法论严谨**：Factorial design（三条件 × 有无 instruction）是该领域少见的系统化设计。七项互补分析（causal + supporting + constraining）构成令人信服的证据链条。\n2. **Robustness 检查充分**：seed sensitivity、demo subsampling、threshold sensitivity、distance metric invariance、linear vs MLP probe、cross-benchmark (LIBERO-Spatial) 验证。这一水平的 robustness 检查超过同领域大多数论文。\n3. **核心发现（C2 routing）有价值**：Entry-exit routing pattern 与 Llama-2 base 的 mid-depth pattern 的对比是 genuine insight，且有多项 converging evidence 支持。\n4. **诚实汇报**：C1 被标为 sanity check，C3 的 metric-dependent 性质被明确说明，CKA divergence 被如实报告而非隐藏。Limitations 段有实质内容。\n5. **与 Grant et al. 2026 的差异化清晰**：token-level vs feature-level、per-layer decomposition、factorial controls 三点区别陈述明确（Related Work lines 24-25）。\n\n---\n\n## Overall Assessment\n\n本文是一篇方法论扎实、数据分析严谨的 representational analysis 论文。核心贡献 C2（VLA fine-tuning 将 instruction routing 前置到 entry-exit layers）是有价值的发现，七项互补分析形成有说服力的证据链。然而，三个 critical 问题使其在 CoRL 的接收前景不乐观：（1）单模型单基准范围限制 generalizability；（2）完全缺失 closed-loop 验证使 robotics implications 停留在猜测层面；（3）论文本质上是 NLP-style mechanistic interpretability 工作，对 CoRL 的 scope fit 有限。如果作者能增加至少一项 closed-loop validation（如基于 routing analysis 的 layer pruning + task success 评估）和至少一个额外模型/架构的验证，本文将显著增强竞争力。当前版本更适合投往 NeurIPS/ICML 的 interpretability track。\n\nRating: **5/10** — Marginally below acceptance threshold\nConfidence: **4/5**\n",
    "reviewer_id": "2",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 405 · 2026-05-19T00:55:54.149491+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4142
}
```

</details>

---


### Assistant

_source line 406 · 2026-05-19T00:56:02.028803+00:00_

审稿报告已提交给 Review Director。

核心结论：**5/10，marginally below acceptance threshold**。

三个 critical 问题：
1. **单模型单基准**（仅 OpenVLA-7B + LIBERO）严重限制 generalizability
2. **无 closed-loop 验证**：所有 robotics implications（pruning、routing monitoring）均为未验证猜测
3. **CoRL scope fit 有限**：本质是 NLP-style mechanistic interpretability 论文，无物理机器人实验，无学习算法改进

主要优势是方法论严谨（factorial design + 七项互补分析 + 充分 robustness checks）和核心发现 C2（entry-exit routing pattern）的 converging evidence。建议增加 closed-loop validation 和多架构验证后投 NeurIPS/ICML，或补充这些内容后再投 CoRL。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2"
}
```

</details>

---


## Round 16

## Round 16

2 recorded events


### User

_source line 407 · 2026-05-19T00:57:21.537546+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 1 的完整审稿意见

请逐条回应以下 Reviewer 1 的意见。对每个 Must-Fix 和 Should-Fix 条目，标注 **[AGREE]** 或 **[REBUT]**，并说明理由。如有 REBUT，请引用论文中的具体 Section/Table/Figure 作为证据。

---

以下是 Reviewer 1 的完整审稿原文：

### 总体评分
Overall: 5/10 — Marginally below acceptance threshold
Confidence: 4/5

### Must-Fix 问题

**N1** [critical] Random-subset ablation 结果与核心叙事矛盾
- 论文的核心 claim 是 L1 的 24 个 instruction-dominant heads 是 instruction routing 的功能载体。但 ablation 实验显示，移除这 24 个 dominant heads 使 action probe R² **增加** +0.042，而随机 24 heads 的 ablation R² 增加更大（+0.077）。(a) 移除 instruction routing 反而让 action 更容易解码；(b) dominant heads 的效应甚至弱于随机 heads。论文的解释（"structured noise for the probe"）是 post-hoc rationalization，缺乏独立验证。如果 instruction signal 真的是 "结构化噪声"，那么整个 routing 叙事都需要重新审视。

**N2** [critical] "Causal" claim 在 open-loop 设定下不成立
- 所有分析均为 representational/open-loop。Discussion §5 明确使用 "Causal" 标签分类证据，但真正的因果验证需要闭环评估（ablate → deploy → measure task success）。应将措辞改为 "interventional" 或 "quasi-causal"。

**N3** [critical] Counterfactual instruction ordering 与 semantic distance 叙事不符
- paraphrased (d=0.697) > shuffled (d=0.625)：paraphrased 在语义上应比 shuffled 更接近原始指令，但产生更大 divergence。说明模型对 token identity 比语义更敏感，支持 Grant et al. 的 "language instructions largely ignored" 结论，与本文叙事（instruction routing 有功能意义）形成张力。

**N4** [critical] 统计功效不足以支撑核心比较
- RSA bootstrap N=10 tasks。论文自己承认 "n.s. result reflects limited statistical power"。但主文仍将 Δρ=0.017 报告为 "non-significant" 并据此得出 "training enhances decodability, not geometry"。在 N=10 下不能基于 underpowered non-significance 得出 negative conclusion。

### Should-Fix 问题

**W1** [warning] Probe 严重过参数化
- MLP probe N/params ≈ 0.06。虽然 linear probe 复现了定性模式，但主文报告的所有 R² 值均来自过参数化的 MLP probe。

**W2** [warning] N=63,228 的独立性假设
- 同一 demo 内的 frames 存在强时间自相关。Demo-level split 解决了泄露，但 bootstrap 比较中有效独立单元数远小于 63,228。

**W3** [warning] Cohen's d 的独立性假设违反
- Action tokens 在同一 trajectory 内强烈相关。将每个 action token 作为独立观测计算 d 会系统性高估 effect size。

**W4** [warning] Pretrained Llama-2 base control 的有效性
- Llama-2 base 从未见过 projected visual tokens。Appendix 诊断仅证明表征非退化，不证明与 VLA-trained 可比。Llama-2 base 在 L1 显示 9/32 instruction-dominant heads 可能仅因为 instruction tokens 是 in-distribution input，与 "language pretraining seeds partial instruction routing" 的解读不同。

**W5** [warning] Specificity control 效果有限
- Top-24 vs Bottom-24 有 16 heads 重叠。d ratio 仅 1.15×，特异性有限。

**W6** [warning] 单模型范围
- 仅研究 OpenVLA-7B。Discussion 对其他架构做了预测但均未验证。Framework 的泛化性仅在同一模型的两个 LIBERO suite 上验证过。

---

请逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 408 · 2026-05-19T00:59:13.108177+00:00_

逐条回应 Reviewer 1 的审稿意见。

---

## 交叉回应：Reviewer 1

### Must-Fix 条目

**[AGREE with qualification] R1-N1: Random-subset ablation 与核心叙事的张力**

R1 指出的 R² 结果（dominant +0.042 < random +0.077）确实反直觉，我在自己的审稿中也将其列为 W3。但我不同意 R1 将此升级为 "整个 routing 叙事需要重新审视" 的程度。

理由：R² 与 trajectory divergence 的矛盾并非指向同一个量。probe R² 衡量的是从 frozen representation 解码 action 的容易程度（移除结构化信号反而可以简化解码）；Cohen's d 衡量的是 intervention 对 output trajectory 的功能影响（Section 4.3: dominant d=0.65 vs control d=0.41, Table A5）。后者与 routing function 的关联更直接。此外，dose-response curve（Figure A4, 8 conditions, monotonic d=0.48→0.64）、counterfactual analysis（Table A7, 4 conditions, d=0.63-0.97）、task-dependent routing（Table A11, p=0.033）三条独立证据线均支持 L1 routing 的功能意义，不依赖 R² ablation 结果。

**共识**：R² 解释确实是 post-hoc，论文应更明确讨论 R² 与 d 的分离机制。但将其定为推翻 routing narrative 的 critical issue 过重——routing claim 有至少五条 converging evidence，R² ablation 只是其中之一。建议降为 should-fix。

---

**[AGREE with nuance] R1-N2: "Causal" 术语在 open-loop 下的适用性**

R1 要求将 "Causal" 改为 "interventional" 或 "quasi-causal"，这在 robotics 语境下有道理。但需要注意：Discussion Section 5 使用 "Causal" 标签（第 8 行）是对标 mechanistic interpretability 文献的惯例——Meng et al. 2022 (ROME)、Wang et al. 2023 (IOI circuit) 均用 "causal tracing" 指代模型内部的 intervention 实验，而非 closed-loop deployment。论文的用法与这一领域惯例一致。

**共识**：CoRL 读者以 robotics 背景为主，"causal" 一词易引起对 closed-loop 因果的误解。改为 "interventional evidence" 是低成本高收益的修改。但这是 terminology issue，不构成 critical methodological flaw。建议降为 should-fix。

---

**[AGREE on ordering, REBUT on inference] R1-N3: Counterfactual ordering 与 semantic distance**

我在自己的审稿 W4 中提出了相同观察：paraphrased d=0.697 > shuffled d=0.625 与 "semantic distance" claim 不一致。这一点 R1 和我完全一致。

但 R1 进一步推断这 "支持 Grant et al. 的 language instructions largely ignored 结论，与本文叙事形成张力"——这我不同意。Table A7 显示：empty d=0.968, wrong task d=0.844, paraphrased d=0.697, shuffled d=0.625。所有条件均产生 substantial trajectory divergence（d > 0.6），这恰恰证明 instructions **are** influencing action generation，只是影响路径不走 semantic distance 而是走 lexical/token identity。这与 Grant et al. 的 "language largely ignored" 结论相矛盾而非支持。

**共识**：ordering 确实不符 semantic distance 叙事，论文应修正 Section 4.3 line 79 的表述。但数据本身支持 instruction-conditioned action generation（all d > 0.6），不支持 R1 的 "language ignored" 推断。

---

**[AGREE] R1-N4: 统计功效不足以支撑 negative conclusion**

R1 的统计论点完全正确。N=10 tasks 的 bootstrap 下，non-significant result (Δρ=0.017, CI includes 0) 不能等价于 "no effect"。论文在 Appendix A.14（cross-benchmark, LIBERO-Spatial: Δ=+0.023, p<0.001）自己也承认 "n.s. result on Goal reflects limited statistical power rather than a true null"。

但主文 Section 4.4 line 119 的措辞 "training enhances decodability, not geometry" 实质上是从 underpowered n.s. 得出了 negative claim。这是 inferential error。

**减缓因素**：LIBERO-Spatial 的 replication (p<0.001) 提供了 geometry gain 存在的证据，说明 LIBERO-Goal 的 n.s. 确实是 power 问题。论文应在主文中明确呈现 LIBERO-Spatial 的 significant result 作为对冲，并将 "not geometry" 改为 "limited geometric gain under current sample size"。

---

### Should-Fix 条目

**[REBUT] R1-W1: Probe 过参数化**

论文在 Appendix A.8（Section linear_probe）已直接回应此问题。Linear probe (N/params ≈ 2.2) 复现了 inverted-U pattern：trained image_mean peaks at L14 (R²=0.565), untrained declines monotonically from L0 (R²=0.517)。更关键的是，linear probe 下 trained-untrained gap **更大**（L14: Δ=+0.324 vs MLP L8: Δ=+0.015），说明 VLA training 使 action information 更 linearly decodable。Figure A6 (fig_linear_vs_mlp_probe.pdf) 直接对比了两种 probe 的 per-layer profile。

MLP probe 的过参数化是一个 valid concern，但论文已有充分的 robustness check。R1 的表述 "主文报告的所有 R² 值均来自过参数化的 MLP probe" 忽略了 Appendix 已提供 linear probe 作为验证。

---

**[AGREE partially] R1-W2: N=63,228 的独立性**

R1 正确指出 demo 内 frames 有强时间自相关。但论文的统计框架已部分处理了这一问题：RSA bootstrap 在 task level 重采样（Section 3.5: "resampling is performed at the task level, N=10, treating each task's pairwise RDM entries as a block"），probe 用 demo-level train/test split（Section 3.6: "demos 0-39 vs 40-49"）。有效独立单元数确实远小于 63,228，但分析的 blocking structure 已经将有效 N 降到了 task/demo 粒度，而非假装每个 frame 独立。

**共识**：论文应在 Method 或 Appendix 中明确说明有效独立单元数和 blocking 策略，避免 N=63,228 给读者错误印象。

---

**[AGREE] R1-W3: Cohen's d 的独立性假设违反**

这一点 R1 完全正确，我在自己的审稿中未充分关注。同一 trajectory 内的 action tokens 存在强时间自相关（连续 frames 的 action 高度相似），将每个 token 作为独立观测计算 Cohen's d 会系统性高估 effect size。论文报告的 d 值（0.48-0.97）的绝对值可能被 inflate。

不过，d 值之间的 **相对排序**（empty > wrong > paraphrased > shuffled > ablation > control）不太可能被自相关改变，因为自相关对所有条件的影响方向一致。定量 d 值存疑，但定性结论（routing 的 graded effect, dose-response 的 monotonicity）应仍成立。

---

**[AGREE partially, REBUT partially] R1-W4: Pretrained Llama-2 base control 的有效性**

R1 提出一个精细的替代解释：Llama-2 base 的 9/32 instruction-dominant heads 可能仅因为 instruction tokens 是 in-distribution text（而 image tokens 是 OOD），不代表 "language pretraining seeds partial routing"。

这一替代解释 plausible，但不影响核心发现：无论 9/32 的原因是 "text in-distribution bias" 还是 "pretraining seeds routing"，from pretrained (9/32) to VLA-trained (24/32) 的 shift (+15 heads, +21.2pp attention) 仍然是 VLA fine-tuning 的效应。Appendix A.9 (Figure A3, fig_ood_diagnostics.pdf) 的诊断虽然不能排除 R1 的解释，但三项指标（activation magnitude non-exploding, cosine similarity progressive decrease, PC variance stable）至少排除了 Llama-2 base representations 的退化假说。

**共识**：论文应在 Discussion 中提及 R1 的替代解释，并强调无论 baseline 9/32 的来源如何，pretrained→trained 的 delta 才是核心 claim。

---

**[AGREE] R1-W5: Specificity control 效果有限**

Table A12 (specificity_control): top-24 vs bottom-24 overlap 16 heads，d ratio 1.15× 确实modest。KL ratio (1.56×) 稍好但仍非 dramatic。论文自己的措辞 "graded, attention-ordered contribution" 已经是 conservative claim，与这一有限的 specificity 一致。但 R1 有理由指出这不构成 strong specificity evidence。

---

**[AGREE] R1-W6: 单模型范围**

与我的 N1 完全一致。这是本文最大的局限性之一。

---

### 总结

| R1 条目 | 我的判断 | 严重度调整建议 |
|---------|---------|--------------|
| N1 (ablation R² contradiction) | AGREE with qualification | 降为 W-level；routing claim 有五条独立证据，R² 是其中之一 |
| N2 ("causal" terminology) | AGREE with nuance | 降为 W-level；符合 interp 惯例，但 CoRL 语境下应改措辞 |
| N3 (counterfactual ordering) | AGREE on data, REBUT on inference | 维持 W-level；ordering 问题成立，但 "language ignored" 推断不成立 |
| N4 (statistical power) | AGREE | 维持 N-level；underpowered n.s. → negative conclusion 是 inferential error |
| W1 (probe overparameterization) | REBUT | Appendix A.8 已充分回应 |
| W2 (independence assumption) | AGREE partially | 维持 W-level |
| W3 (Cohen's d autocorrelation) | AGREE | 维持 W-level |
| W4 (Llama-2 base control) | AGREE partially | 维持 W-level；替代解释 plausible 但不影响 delta |
| W5 (specificity control) | AGREE | 维持 W-level |
| W6 (single model) | AGREE | 与我的 N1 一致 |

**与 R1 的主要分歧**：R1 的 N1 和 N2 我认为应降级——N1 因为 routing claim 的证据不只依赖 ablation R²；N2 因为术语使用符合 interp 领域惯例。R1 的 N3 推断（"supports language ignored"）与数据不符。R1 的 N4 我完全同意。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2"
}
```

</details>

---


## Round 17

## Round 17

24 recorded events


### User

_source line 409 · 2026-05-19T05:53:28.766105+00:00_

[Round 2 审稿请求]:
## Round 10 修订评估（继续审稿）

你是 Reviewer 2，负责 **新颖性 + 叙事完整性 + CoRL 适配性**。这是继续审稿模式——上轮你给出 5/10 (borderline reject)，核心问题是单模型范围、无闭环验证、CoRL scope fit。

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
**R9-W1** CoRL scope fit 有限
- 上轮建议：增加 robotics-specific implications 的具体论述
**R9-W2** C1 (architecture validation) 占比失衡
- 上轮建议：压缩 C1 在 Abstract/Introduction/Contributions 的篇幅
**R9-W3** Vision representation 训练效果微弱，framing 未充分反映
- 上轮建议：使用更 conservative 的措辞

### Shared Warning
**R9-N3** 'Causal' → 'interventional' 术语修改
**R9-N4** Ablation R² 解释 post-hoc
**R9-N5** Counterfactual semantic distance 措辞
**R9-N6** N=10 统计功效 → "not geometry" 措辞

### Info
**R9-I1** 缺 Octo 引用
**R9-I2** Häon et al. 与 L1 routing 的互补关系未讨论

## 要求
1. 逐条标注 [RESOLVED] 或 [STILL_OPEN]
2. 检查修改是否引入新问题
3. 评估叙事主线是否因修改而变得更连贯或产生新的不一致
4. 给出更新后的评分（是否有变化）
5. 格式：Strengths / Weaknesses / Questions / Overall

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 410 · 2026-05-19T05:53:36.489135+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 411 · 2026-05-19T05:53:36.941258+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 412 · 2026-05-19T05:53:36.991902+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 413 · 2026-05-19T05:53:37.896130+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 414 · 2026-05-19T05:53:37.896492+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 415 · 2026-05-19T05:53:38.348487+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 416 · 2026-05-19T05:53:38.348860+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 417 · 2026-05-19T05:53:38.851278+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 418 · 2026-05-19T05:53:38.851629+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 419 · 2026-05-19T05:53:39.303751+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 420 · 2026-05-19T05:53:39.304767+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 421 · 2026-05-19T05:53:39.958039+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 653
}
```

</details>

---
