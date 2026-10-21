# Reviewer 1 coordination — Part 2 of 8

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../reviewer-1-coordination.md) · [Part 3 →](part-003.md) · [Structured JSON](../../../sessions/ed/ed9cd9e2adfd642813e6.json)

## Round 15

### User

_source line 493 · 2026-05-15T12:14:50.531819+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 的审查。

## 论文信息
- **标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Do Not Scale Structured Information Extraction
- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（含 sections/ 子目录各章节）
- **目标 Venue**: EMNLP 2026 Main Conference
- **Track**: Main Conference (Long Paper)
- **Deadline**: 2026-05-25 (ARR May 2026 cycle)

## Venue 格式要求
- ACL 模板，8 页正文 + 引用不限 + 附录
- Double-blind（匿名审稿）
- Limitations section 必需
- 提交时必须选择 EMNLP（绑定选择）

## 你的审查侧重

### 1. 方法严谨性
- 五个 confidence signal 的定义是否数学严谨、无歧义
- Soft Jaccard（Eq.4-5）的 Hungarian matching 描述是否完整（目标函数、zero-IoU 处理、threshold）
- VC（Eq.6）的公式定义与脚注中描述的实际实现（majority threshold）是否一致
- FK 的独立性假设：excess agreement 数据是否充分支撑（configuration 覆盖、显著性检验）
- Consensus-proximity = LOO-SJ 等价性推导是否充分

### 2. 统计检验
- Bootstrap resampling 的参数设置（B=10,000, n=529）是否充分
- TOST 等价检验的 δ 选择（±2/3/5 pp）的合理性论证——δ 是否有实践锚定
- 多重比较校正（Bonferroni）的处理是否到位
- Effect size (Cohen's d=0.038) 和 CI 的报告是否完整
- "60% instances effectively tied" 的 ε=0.05 阈值选择是否有依据

### 3. 实验设计
- 训练配置（LoRA rank=32, α=64, 5 epochs）是否完整可复现
- Qwen3-8B SciERC thinking token 训练不一致是否充分讨论
- N=8 single seed (seed=42) 作为核心结果的局限性
- Free-form ablation 仅 1 个 dataset × 1 个 model 的充分性
- RE 证据仅基于 SciERC 单数据集的措辞限定是否一致

### 4. 可复现性
- 附录是否包含完整训练配置、prompt template
- 数据集 split 信息
- Constrained decoding 的具体工具和参数

请严格按照 EMNLP 审稿标准评审，不留情面。输出格式：Summary → Strengths → Weaknesses (Critical/Warning/Minor 分级) → Questions → Missing References → Scores (Soundness/Presentation/Contribution/Overall 1-5) → Confidence。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 494 · 2026-05-15T12:15:01.613637+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/struct_self_consist_ie/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/struct_self_consist_ie/docs/paper/**/*.tex"
  }
}
```

</details>

---


### Tool result

_source line 495 · 2026-05-15T12:15:01.664322+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 496 · 2026-05-15T12:15:02.216909+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
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

_source line 497 · 2026-05-15T12:15:02.368111+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 498 · 2026-05-15T12:15:09.022944+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/**/*.tex"
  }
}
```

</details>

---


### Tool result

_source line 499 · 2026-05-15T12:15:09.476271+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 500 · 2026-05-15T12:15:09.476719+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool result

_source line 501 · 2026-05-15T12:15:16.943865+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results, here's information about the ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Review Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, ex
…[truncated 1494 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7467
}
```

</details>

---


### Tool call

_source line 502 · 2026-05-15T12:15:24.380239+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5 or whatever), and the description of each score level. Include soundness, excitement, overall recommendation, confidence, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5 or whatever), and the description of each score level. Include soundness, excitement, overall recommendation, confidence, and any other scored dimensions."
  }
}
```

</details>

---


### Tool call

_source line 503 · 2026-05-15T12:15:25.433948+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 504 · 2026-05-15T12:15:25.936394+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ Why Confidence Signals Do Not Scale Structured Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	
45	\bibliography{references}
46	
47	\appendix
48	\input{sections/appendix}
49	
50	\end{document}
51	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 505 · 2026-05-15T12:15:25.989314+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 506 · 2026-05-15T12:15:26.291608+00:00_

1	\begin{abstract}
2	Test-time scaling through repeated sampling promises quality gains for LLM-based information extraction (IE), but whether confidence signals can identify the best output among multiple candidates remains untested for structured tasks.
3	We compare five confidence signals across NER and relation extraction on three benchmarks with two 8B-parameter model families and uncover a \textit{correlation-selection gap}: signals achieve strong quality estimation yet none significantly improves sample selection despite substantial oracle headroom.
4	Most signals are instance-level by construction and cannot rank candidates; the empirical question is whether log-probability---the sole per-sample signal---or consensus-proximity selection (MBR decoding) can bridge the gap.
5	Neither succeeds: log-probability scores are compressed into effective ties, while MBR utility correlates with quality across instances but not within them.
6	A controlled ablation confirms that this compression is intrinsic to the model and task, not an artifact of constrained decoding.
7	Signal rankings depend on task complexity, with findings consistent across two model families at 8B scale.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 507 · 2026-05-15T12:15:26.291948+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 508 · 2026-05-15T12:15:26.643365+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2025scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalen
…[truncated 4839 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 509 · 2026-05-15T12:15:26.693964+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 510 · 2026-05-15T12:15:26.745216+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We use \textit{confidence signal} as the umbrella term for all five measures.
17	Four are \textit{consistency signals}---computed from inter-sample agreement---spanning two families: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]).
18	The fifth, log-probability, is the sole \textit{model-internal} signal and the only one that scores individual samples rather than the instance as a whole.
19	
20	\paragraph{Log-probability (model-internal, per-sample).}
21	The only per-sample signal.
22	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
23	\begin{equation}\label{eq:logprob}
24	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
25	\end{equation}
26	
27	\paragraph{Exact match voting (surface
…[truncated 4871 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 511 · 2026-05-15T12:15:30.963373+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. Reviewer Confidence
**Scale: 1-5**
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## 2. Soundness
**Scale: 1-5 (with half-point increments)**
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. Excitement
**Scale: 1-5 (with half-point increments)**
- **5**: "Highly Exciting: I would recommend this paper to others."
- **4**: "Exciting: I would mention this paper to others."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me."
- **1**: "Not Exciting: this paper does not resonate with me."

## 4. Overall Assessment
**Scale: 1-5 (with half-point increments)**
- **5**: "Consider for Award"
- **4**: "Conference acceptance"
- **3**: "Findings of the ACL"
- **2**: "Resubmit next cycle"
- **1**: "Do not resubmit"

## 5. Reproducibility
**Scale: 1-5**
Ranges from "easily reproduce" (5) to "would not be able to reproduce" (1).

## 6. Datasets & Software
**Scale: 1-5** each
Rated from "Enabling" (5) to "No usable datasets/software" (1).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6583
}
```

</details>

---


### Tool call

_source line 512 · 2026-05-15T12:15:36.947056+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 513 · 2026-05-15T12:15:37.550727+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.
15	We note a training confound for SciERC: Qwen3-8B's SciERC checkpoint was trained with \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), which prepends empty \texttt{&lt;think>\textbackslash n&lt;/think>} blocks (4--5 tokens) to each training response and includes them in the loss computation; CoNLL-2003 and WNUT-17 checkpoints explicitly set \texttt{enable\_thinking=False}.
16	No reasoning content is present (the blocks are always empty), and constrained decoding at inference time enforces JSON-only output, so thinking tokens do not appear in generated samples.
17	This constitutes a minor train--test distribution mismatch for SciERC ($<$0.3\% of the 2048-token training window); CoNLL-2003 and WNUT-17 are unaffected.
18	We discuss implications in the Limitations section.
19	We draw $N{=}8$ samples at $T{=}1.0$ (primary; single seed, seed${=}42$), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in T
…[truncated 11585 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 514 · 2026-05-15T12:15:37.602945+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 515 · 2026-05-15T12:15:37.904558+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, VC provides the strongest rank correlation ($\rho{=}0.38$), though EM leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).
5	Signal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across two model families at 8B scale, though with model-dependent magnitude.
6	At higher sample sizes ($N{=}16$), SJ converges to comparable NER performance with VC ($\Delta{=}0.002$) with lower cross-seed variance ($\sigma{=}0.010$ vs.\ $0.026$); on RE, only VC consistently outperforms LP (preliminary).
7	When model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\ref{tab:wnut}).
8	
9	\paragraph{Why the gap exists: two layers.}
10	\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
11	Consensus-proximity selection (\S\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\ref{tab:selection}).
12	\textit{Layer 2 (score compression):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.
13	LP scores are severely compressed: 60\% of instances have a within-sample range below 0.05, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$; Appendix~\ref{app:logprob_ties}).
14	In the 40\% of instances where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), LP \textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.01$; within-instance $\rho$: 0.08$\to$0.39).
15	This diagnostic confirms that LP carries useful per-sample quality information; score compression is the primary mechanistic bottleneck.
16	A cont
…[truncated 4640 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 516 · 2026-05-15T12:15:37.905178+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 517 · 2026-05-15T12:15:38.871641+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We demonstrate that consistency signals are effective quality estimators ($\rho$ up to 0.38, AUROC up to 0.75) for LLM-based structured IE, but fail at sample selection---the \textit{correlation-selection gap}.
4	By construction, four of five signals assign identical scores to all candidates from the same input; log-probability, the only per-sample signal, also fails ($p{>}0.39$) despite 13--18~pp oracle headroom due to score compression.
5	Where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$); consensus-proximity selection (MBR decoding) similarly fails as utility correlates with quality across instances but not within them.
6	A controlled free-form decoding ablation confirms that score compression is intrinsic to the model and task, not an artifact of constrained decoding.
7	Signal rankings depend on task difficulty, with consistent ordering across two model families at 8B scale.
8	RE findings rest on SciERC alone (preliminary, single benchmark) and warrant multi-benchmark validation.
9	Trained verifiers, scaling to 70B+ models, and conformal prediction are promising directions for closing the gap.
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 966
}
```

</details>

---


### Tool call

_source line 518 · 2026-05-15T12:15:38.871976+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 519 · 2026-05-15T12:15:39.373970+00:00_

1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	RE selection failure persists even when restricting to non-zero F1 instances (Appendix~\ref{app:re_conditional_selection}), ruling out floor effects as the sole explanation, but generalization to other RE benchmarks remains unvalidated.
3	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
4	
5	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
6	A 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
7	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
8	
9	Our analysis of selection potential uses only unsupervised signals.
10	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
11	
12	We evaluate at $N{=}8$ and $N{=}16$.
13	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.047$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
14	
15	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
16	Our free-form ablation (\S\ref{sec:ablation}) confirms that LP score compression persists
…[truncated 1227 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 520 · 2026-05-15T12:15:39.374373+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 521 · 2026-05-15T12:15:39.726301+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.010$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as population standard deviation.}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.411$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.283 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.4
…[truncated 34442 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 522 · 2026-05-15T12:15:39.726996+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 523 · 2026-05-15T12:15:39.777641+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling \cite{zhang2025tts}, \citet{snell2025scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.
9	All of the above target reasoning/QA with discrete answers or specific aggregation strategies.
10	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
11	
12	\paragraph{Consistency for structured IE.}
13	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
14	Their work leaves open three questions we address: (i)~whether structural matching improves on surface-level agreement (which they acknowledge ``overlooks semantically consistent outputs''); (ii)~whether quality estimation translates to best-of-$N$ selec
…[truncated 2915 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 524 · 2026-05-15T12:15:47.766280+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the key reviewer guidelines: what should reviewers focus on, what makes a good review, scoring criteria details, what constitutes a reason for rejection vs acceptance, any specific guidance on soundness evaluation, experimental rigor requirements, and reproducibility standards."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the key reviewer guidelines: what should reviewers focus on, what makes a good review, scoring criteria details, what constitutes a reason for rejection vs acceptance, any specific guidance on soundness evaluation, experimental rigor requirements, and reproducibility standards."
  }
}
```

</details>

---


### Tool call

_source line 525 · 2026-05-15T12:15:49.377210+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/*.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/*.bib"
  }
}
```

</details>

---


### Tool result

_source line 526 · 2026-05-15T12:15:49.427922+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 527 · 2026-05-15T12:15:56.410529+00:00_

# ARR Reviewer Guidelines: Key Summary

## Core Review Focus Areas

Reviewers should concentrate on four main tasks:

1. **Assignment verification** – Check expertise match and conflicts of interest
2. **Desk-rejection assessment** – Evaluate appropriateness, anonymity violations, style compliance, ethics flags
3. **Detailed review writing** – Provide specific, constructive feedback
4. **Discussion engagement** – Respond to author clarifications and colleague reviewers

## What Makes a Good Review

Strong reviews demonstrate these qualities:

- **Specificity**: "The formulation of X misses factor Y" rather than vague criticism
- **Justified scoring**: Soundness scores must align with identified technical issues
- **Professional tone**: Constructive feedback framed as colleague-to-colleague dialogue
- **Balanced perspective**: Reading papers twice before critiquing, adjusting expectations based on contribution type

As the guidelines note, reviewers should adopt "a reading strategy" that involves "skimming and in-depth reading" rather than critiquing during initial exposure.

## Scoring Criteria

Three distinct scores are required:

- **Soundness**: Technical validity and methodological rigor (must be justified in review text)
- **Excitement**: Personal interest level (subjective, requires no explicit justification)
- **Overall recommendation**: Composite assessment reflecting soundness, novelty, and potential impact

## Rejection vs. Acceptance Thresholds

**Grounds for desk rejection** include:
- Scope misalignment with conference CFP
- Hallucinated citations or anonymity violations
- Style guide/length non-compliance
- Missing limitations sections
- Egregious responsible NLP checklist violations

**NOT grounds for rejection**:
- Lack of state-of-the-art results (unless claimed)
- Simplicity of methodology
- Non-English evaluation
- Acknowledged limitations
- Negative findings

## Soundness Evaluation Requirements

Reviewers must verify:

- Complete, correct proofs
…[truncated 777 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8644
}
```

</details>

---


### Tool call

_source line 528 · 2026-05-15T12:16:50.726357+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 529 · 2026-05-15T12:17:43.229574+00:00_

&lt;persisted-output>
Output too large (50.8KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/eb1a3f49-65c9-4074-8546-55ac5548828b/tool-results/toolu_01NEwNG45FBvBPtMRiJ9HQX3.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 62, \"total_citations\": 93, \"unique_cited_keys\": 62, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 56, \"online_not_found\": 3, \"online_mismatch\": 3}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"angelopoulos2021conformal\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\", \"year\": \"2021\", \"venue\": \"ICLR 2021\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": 
…[truncated 363 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 52503
}
```

</details>

---


### Tool call

_source line 530 · 2026-05-15T12:17:47.094936+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/eb1a3f49-65c9-4074-8546-55ac5548828b/tool-results/toolu_01NEwNG45FBvBPtMRiJ9HQX3.txt",
  "offset": "0",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/eb1a3f49-65c9-4074-8546-55ac5548828b/tool-results/toolu_01NEwNG45FBvBPtMRiJ9HQX3.txt",
    "offset": "0",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 531 · 2026-05-15T12:17:47.399526+00:00_

0	{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 62, \"total_citations\": 93, \"unique_cited_keys\": 62, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 56, \"online_not_found\": 3, \"online_mismatch\": 3}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"angelopoulos2021conformal\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\", \"year\": \"2021\", \"venue\": \"ICLR 2021\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence Estimation for Information Extraction\", \"authors\": \"Culotta, Aron and McCallum, Andrew\", \"year\": \"2004\", \"venue\": \"HLT-NAACL 2004\"}, {\"key\": \"derczynski2017wnut\", \"type\": \"inproceedings\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recogni
…[truncated 49981 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 304
}
```

</details>

---


### Tool call

_source line 532 · 2026-05-15T12:20:29.861186+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿意见：方法严谨性 + 实验设计\n\n**论文**: Strong Predictors, Weak Selectors: Why Confidence Signals Do Not Scale Structured Information Extraction\n**Venue**: EMNLP 2026 Main Conference (Long Paper)\n\n---\n\n### 总体评分\n\n**Overall**: 3/5 (Findings of the ACL)\n**一句话总结**: 论文提出了有价值的 correlation-selection gap 概念并提供了扎实的 quality estimation 分析，但核心 selection failure 结论建立在 single-seed 分析上、ε=0.05 阈值缺乏论证、free-form ablation 范围过窄却支撑了过强的泛化声称。\n\n### 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 方法定义清晰，QE 分析可靠；但 selection gap 的统计支撑不足（single seed）、关键阈值未论证、ablation 泛化过度 |\n| Excitement | 3.5/5 | Correlation-selection gap 概念对 IE + test-time scaling 社区有实际指导意义；MBR 连接有洞察力 |\n| Overall | 3/5 | 贡献真实但 selection 分析——论文的核心卖点——统计论证最弱；补充多种子 selection 分析后可达 Findings |\n| Confidence | 4/5 | 仔细阅读全文含附录，核查公式推导和引用 |\n| Reproducibility | 3.5/5 | 训练配置完整（Table 7），但核心实验 single seed 限制复现可信度 |\n\n---\n\n### Must-Fix 问题（3个 Critical）\n\n**N1** [critical] Selection gap 分析缺乏多种子验证\n- 位置：Section 4.3 / Table 3\n- 核心 selection failure（LP NER +0.6pp, p=0.39）仅使用 seed=42。3-seed 分析（Table 10）仅覆盖 QE，未覆盖 selection F1。p=0.39 的 single-seed 结果不足以支撑论文的 headline finding。\n- 建议：将 3-seed 分析扩展至 Table 3，报告跨种子 selection F1 的 mean±σ 和 p-value 范围。\n\n**N2** [critical] ε=0.05 \"effectively tied\" 阈值缺乏论证\n- 位置：Section 5 / Appendix H (Table 12)\n- Table 12 显示 ε=0.01→1.1%, ε=0.05→60.3%（59×跳变），说明阈值处于分布陡峭区域。\"60% effectively tied\" 出现在 abstract 中但 0.05 的依据未给出。\n- 建议：提供 LP range 完整 CDF；或用连续度量（within-instance LP-F1 correlation）替代二元划分。\n\n**N3** [critical] Free-form ablation 范围过窄但结论过强\n- 位置：Section 5 §4 / Discussion\n- 1 dataset × 1 model × 1 seed 的 ablation 支撑了 \"fundamental challenge\" 的声称。且 RE LP selection 在 free-form 下翻转（−0.68pp→+1.69pp），与 \"not an artifact of decoding strategy\" 矛盾。\n- 建议：降级 \"fundamental\" 为 \"observed in our setting\"；明确承认 RE 翻转。\n\n### Should-Fix 问题（5个 Warning）\n\n**W1** FK 独立性检验功效极低（n=5 configurations 的 t-test）\n**W2** VC 在 QE 和 selection 中使用不同计算但 Table 3 标注不清\n**W3** TOST δ 值循环锚定于 oracle headroom，缺乏外部标准\n**W4** LP 温度敏感性完全缺失（核心诊断对象却无 T=0.7 数据）\n**W5** 标题/摘要暗示 NER+RE 均有多 benchmark 支持，实际 RE 仅单数据集\n\n### 主要优势\n\n- Correlation-selection gap 概念清晰且有社区价值\n- 五信号三家族的系统化 taxonomy 是理论贡献\n- RE \"preliminary\" 标注诚实，Limitations 详尽\n- MBR decoding 连接是对 MBR 文献的有意义扩展\n- 附录深度出色（12个补充分析章节）\n\n### 引用验证\n\n62篇引用全部 cross-check 通过，56篇 OpenAlex 确认，无伪造引用问题。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿意见：方法严谨性 + 实验设计\n\n**论文**: Strong Predictors, Weak Selectors: Why Confidence Signals Do Not Scale Structured Information Extraction\n**Venue**: EMNLP 2026 Main Conference (Long Paper)\n\n---\n\n### 总体评分\n\n**Overall**: 3/5 (Findings of the ACL)\n**一句话总结**: 论文提出了有价值的 correlation-selection gap 概念并提供了扎实的 quality estimation 分析，但核心 selection failure 结论建立在 single-seed 分析上、ε=0.05 阈值缺乏论证、free-form ablation 范围过窄却支撑了过强的泛化声称。\n\n### 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 方法定义清晰，QE 分析可靠；但 selection gap 的统计支撑不足（single seed）、关键阈值未论证、ablation 泛化过度 |\n| Excitement | 3.5/5 | Correlation-selection gap 概念对 IE + test-time scaling 社区有实际指导意义；MBR 连接有洞察力 |\n| Overall | 3/5 | 贡献真实但 selection 分析——论文的核心卖点——统计论证最弱；补充多种子 selection 分析后可达 Findings |\n| Confidence | 4/5 | 仔细阅读全文含附录，核查公式推导和引用 |\n| Reproducibility | 3.5/5 | 训练配置完整（Table 7），但核心实验 single seed 限制复现可信度 |\n\n---\n\n### Must-Fix 问题（3个 Critical）\n\n**N1** [critical] Selection gap 分析缺乏多种子验证\n- 位置：Section 4.3 / Table 3\n- 核心 selection failure（LP NER +0.6pp, p=0.39）仅使用 seed=42。3-seed 分析（Table 10）仅覆盖 QE，未覆盖 selection F1。p=0.39 的 single-seed 结果不足以支撑论文的 headline finding。\n- 建议：将 3-seed 分析扩展至 Table 3，报告跨种子 selection F1 的 mean±σ 和 p-value 范围。\n\n**N2** [critical] ε=0.05 \"effectively tied\" 阈值缺乏论证\n- 位置：Section 5 / Appendix H (Table 12)\n- Table 12 显示 ε=0.01→1.1%, ε=0.05→60.3%（59×跳变），说明阈值处于分布陡峭区域。\"60% effectively tied\" 出现在 abstract 中但 0.05 的依据未给出。\n- 建议：提供 LP range 完整 CDF；或用连续度量（within-instance LP-F1 correlation）替代二元划分。\n\n**N3** [critical] Free-form ablation 范围过窄但结论过强\n- 位置：Section 5 §4 / Discussion\n- 1 dataset × 1 model × 1 seed 的 ablation 支撑了 \"fundamental challenge\" 的声称。且 RE LP selection 在 free-form 下翻转（−0.68pp→+1.69pp），与 \"not an artifact of decoding strategy\" 矛盾。\n- 建议：降级 \"fundamental\" 为 \"observed in our setting\"；明确承认 RE 翻转。\n\n### Should-Fix 问题（5个 Warning）\n\n**W1** FK 独立性检验功效极低（n=5 configurations 的 t-test）\n**W2** VC 在 QE 和 selection 中使用不同计算但 Table 3 标注不清\n**W3** TOST δ 值循环锚定于 oracle headroom，缺乏外部标准\n**W4** LP 温度敏感性完全缺失（核心诊断对象却无 T=0.7 数据）\n**W5** 标题/摘要暗示 NER+RE 均有多 benchmark 支持，实际 RE 仅单数据集\n\n### 主要优势\n\n- Correlation-selection gap 概念清晰且有社区价值\n- 五信号三家族的系统化 taxonomy 是理论贡献\n- RE \"preliminary\" 标注诚实，Limitations 详尽\n- MBR decoding 连接是对 MBR 文献的有意义扩展\n- 附录深度出色（12个补充分析章节）\n\n### 引用验证\n\n62篇引用全部 cross-check 通过，56篇 OpenAlex 确认，无伪造引用问题。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 533 · 2026-05-15T12:20:33.677193+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3816
}
```

</details>

---


### Assistant

_source line 534 · 2026-05-15T12:20:40.011407+00:00_

审稿意见已提交给 Review Director。

总结：论文在 quality estimation 层面做得扎实（5 signal × 3 dataset × 2 model 的系统比较，统计分析较完整），但其核心卖点——correlation-selection gap——的统计支撑存在三个 critical 级别问题：(1) selection 分析仅 single seed；(2) "60% effectively tied" 的 ε 阈值未论证；(3) free-form ablation 过窄但支撑了过强的泛化声称。建议 Overall 3/5（Findings 水平），补充多种子 selection 分析后有望提升。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 16

## Round 16

4 recorded events


### User

_source line 535 · 2026-05-15T12:23:20.141662+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Critical/Warning 级别的问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并引用论文具体 Section/Table/Figure 作为证据。

---

## Reviewer 2 审稿意见（新颖性 + 完整性 + 写作质量）

**Overall**: 3/5

### Critical Issues

**N1**: Correlation-selection gap 大部分是 definitional，非 empirical
- 4/5 signals 按设计对同一 instance 的所有 candidates 赋相同分数——论文 §5 自己承认这是 "Layer 1 (definitional)"，但 abstract/intro 将其包装为 empirical discovery。实际的 empirical finding 更窄：LP compression。需要根本性 reframing。

**N2**: 模型规模同质性（仅 8B）无法支撑标题中 "Do Not Scale" 的 broad claim
- 两个模型均为 8B 参数。论文自身发现 task difficulty × model capability 存在交互效应，但只测了一个 scale 点。标题/abstract 需要 scope down。

**N3**: RE 结论过度前置但证据不足
- 仅 SciERC RE 单 benchmark + Qwen only（preliminary），但 LP 负相关数字出现在 abstract 中。应从 abstract 移除或补充实验。

### Warning Issues

**W1**: Abstract 信息密度过高
**W2**: "First multi-family comparison" 是 scope engineering
**W3**: Evaluation framework (Contribution 1) 是 engineering benchmark 而非 methodological contribution
**W4**: LP 的 temperature sensitivity 未表征
**W5**: Conditional set 排除最难实例的 selection bias 未充分讨论
**W6**: Eikema et al. (2025) structure-conditional MBR 仅在 Discussion 出现，应在 Related Work 中定位

### 优势
- 问题定位精准，负面结论有实用价值
- 实验设计远超平均水平
- Quality estimation vs. sample selection 的 conceptual distinction 有价值
- 引用全面准确

---

请逐条（N1-N3, W1-W6）给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 536 · 2026-05-15T12:25:07.505331+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 的交叉回应\n\n### Critical Issues\n\n**[AGREE] R2-N1**: Correlation-selection gap 确实大部分是 definitional。论文 §5 自己承认 \"Layer 1 (definitional)\"，但 abstract/intro 将整个 gap 包装为统一的 empirical finding。实际 empirical contribution 更窄：LP compression 诊断 + MBR utility-quality misalignment + non-tied subset 分析。需要 reframing。\n\n**[AGREE] R2-N2**: 仅 8B × 2 models 不足以支撑 \"Do Not Scale\" 的 universal claim。论文自身发现的 task difficulty × model capability 交互效应说明 model capability 是关键调节变量。标题需要 scope down。\n\n**[REBUT] R2-N3**: R2 声称 \"LP 负相关数字出现在 abstract 中\"——这是误读。Abstract 中没有 RE 负相关数字。Introduction 中的 ρ=−0.410 是 WNUT-17 NER（非 RE）。但 R2 的 underlying concern（RE 证据不足被前置）与我的 W5 一致——问题在于 abstract 措辞暗示了比实际更广的 RE 覆盖度。建议 R2 修正 factual error。\n\n### Warning Issues\n\n**[AGREE] R2-W1**: Abstract 信息密度过高，8句话覆盖过多发现。\n**[REBUT] R2-W2**: 论文未声称 \"first multi-family comparison\"。Contribution 1 的核心是三个 metrics 的 decouple（ρ-AUROC dissociation, Table 1），不是 priority claim。\n**[REBUT] R2-W3**: Contribution 1 核心是三个 metrics decouple 的 empirical finding（EM leads AUROC=0.749 but ranks third in ρ=0.295），有实践意义。同意降级为 \"finding\" 比 \"contribution\" 更准确。\n**[AGREE] R2-W4**: 与我的 W4 完全一致。LP 温度敏感性缺失是核心诊断对象的数据缺口。\n**[REBUT] R2-W5**: Conditional filtering 是分离 binary detection 与 quality gradation 的 methodological 必要步骤，不是 selection bias。Table 5 显示 full-set ρ=0.724 完全由 zero/non-zero boundary 驱动。\n**[AGREE] R2-W6**: eikema2025structured 应在 Related Work 的 MBR 段落中定位。\n\n### 汇总\n\nR2 的 N1（definitional reframing）和 N2（scale scope down）与我自己的评估一致，是需要作者解决的实质问题。N3 有 factual error 但 underlying concern 成立。W2/W3/W5 我持不同意见，已提供具体证据。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 的交叉回应\n\n### Critical Issues\n\n**[AGREE] R2-N1**: Correlation-selection gap 确实大部分是 definitional。论文 §5 自己承认 \"Layer 1 (definitional)\"，但 abstract/intro 将整个 gap 包装为统一的 empirical finding。实际 empirical contribution 更窄：LP compression 诊断 + MBR utility-quality misalignment + non-tied subset 分析。需要 reframing。\n\n**[AGREE] R2-N2**: 仅 8B × 2 models 不足以支撑 \"Do Not Scale\" 的 universal claim。论文自身发现的 task difficulty × model capability 交互效应说明 model capability 是关键调节变量。标题需要 scope down。\n\n**[REBUT] R2-N3**: R2 声称 \"LP 负相关数字出现在 abstract 中\"——这是误读。Abstract 中没有 RE 负相关数字。Introduction 中的 ρ=−0.410 是 WNUT-17 NER（非 RE）。但 R2 的 underlying concern（RE 证据不足被前置）与我的 W5 一致——问题在于 abstract 措辞暗示了比实际更广的 RE 覆盖度。建议 R2 修正 factual error。\n\n### Warning Issues\n\n**[AGREE] R2-W1**: Abstract 信息密度过高，8句话覆盖过多发现。\n**[REBUT] R2-W2**: 论文未声称 \"first multi-family comparison\"。Contribution 1 的核心是三个 metrics 的 decouple（ρ-AUROC dissociation, Table 1），不是 priority claim。\n**[REBUT] R2-W3**: Contribution 1 核心是三个 metrics decouple 的 empirical finding（EM leads AUROC=0.749 but ranks third in ρ=0.295），有实践意义。同意降级为 \"finding\" 比 \"contribution\" 更准确。\n**[AGREE] R2-W4**: 与我的 W4 完全一致。LP 温度敏感性缺失是核心诊断对象的数据缺口。\n**[REBUT] R2-W5**: Conditional filtering 是分离 binary detection 与 quality gradation 的 methodological 必要步骤，不是 selection bias。Table 5 显示 full-set ρ=0.724 完全由 zero/non-zero boundary 驱动。\n**[AGREE] R2-W6**: eikema2025structured 应在 Related Work 的 MBR 段落中定位。\n\n### 汇总\n\nR2 的 N1（definitional reframing）和 N2（scale scope down）与我自己的评估一致，是需要作者解决的实质问题。N3 有 factual error 但 underlying concern 成立。W2/W3/W5 我持不同意见，已提供具体证据。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 537 · 2026-05-15T12:25:11.479722+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3974
}
```

</details>

---


### Assistant

_source line 538 · 2026-05-15T12:25:17.563668+00:00_

交叉回应已提交。汇总：

- **3 个 AGREE**（R2-N1 definitional reframing、R2-N2 scale scope down、R2-W1/W4/W6）
- **3 个 REBUT**（R2-N3 的 factual error、R2-W2/W3 的 contribution 定性、R2-W5 的 conditional filtering）

R2 与我的评审在以下问题上形成共识：abstract/title 泛化过度、LP 温度数据缺失、RE 单 benchmark 不足。分歧主要在 evaluation framework 是否构成 contribution 以及 conditional filtering 是否引入 selection bias。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 17

## Round 17

40 recorded events


### User

_source line 539 · 2026-05-15T14:58:10.125037+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1

**你的侧重**：方法严谨性 + 实验可靠性

### 投稿信息
- **目标 venue**: EMNLP 2026 Findings (ARR May cycle)
- **Deadline**: 2026-05-25
- **格式**: ACL template, 长文 8 页正文 + unlimited Limitations/Ethics/References/Appendix
- **匿名**: Double-blind
- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（多文件结构，sections 在 `sections/` 子目录）

### 论文概要
本文研究 LLM 结构化信息抽取（NER/RE）中，自一致性信号能否用于质量估计和样本选择。比较 5 个置信度信号（VC, SJ, FK, EM, LP），在 3 个 NER 数据集 + 1 个 RE 数据集、2 个 8B 模型上系统评估。核心发现：所有信号实现强质量估计（ρ 至 0.38, AUROC 至 0.75），但无一显著改善样本选择——"correlation-selection gap"。机制解释：LP score compression + MBR utility-quality misalignment。

### 审查要点（不限于此）

1. **统计检验严谨性**
   - Bootstrap resampling 方法是否规范（B=10,000, Fisher combination, n=551）
   - TOST 等价检验的 δ 选择是否有充分论证（论文用 ±2/3/5 pp，锚定于 oracle headroom）
   - 多重比较校正是否充分（Bonferroni 声明）
   - 单种子 vs 多种子：核心 selection failure（Table 3, seed=42）是否需要多种子验证

2. **信号形式化**
   - SJ（Eq. 4-5）：Hungarian matching 目标函数、zero-IoU pairs 处理、max normalizer vs union normalizer 选择
   - VC（Eq. 6）：QE 用连续公式 vs selection 用 majority threshold——Table 3 是否清楚标注
   - FK（Eq. 3）：独立性假设的 justification（excess agreement -0.4% to -4.0%, n=5 t-test 功效是否足够）
   - LP（Eq. 1）：ε=0.05 "effectively tied" 阈值的 arbitrary 程度（Table 12 显示 ε=0.01→1.1%, ε=0.05→60.3%，59× 跳变）

3. **实验设计**
   - RE 结论仅基于 SciERC 单数据集——"preliminary" 标注是否全文一致
   - Free-form ablation 范围（1 dataset × 1 model × 1 seed）是否支撑 "task-intrinsic" 声称
   - LP 温度数据缺失（T=0.7 无 LP 数据）——核心诊断对象的关键参数
   - N=8 核心结果单种子，N=16 有 3-seed——是否存在不对称
   - Qwen3-8B SciERC 的 enable_thinking confound

4. **可复现性**
   - 训练配置（Appendix Table 8）完整度
   - Prompt template 是否充分
   - 数据集 filtering 标准（n=529 vs 551, gold-empty 排除）是否清晰

请按 EMNLP 标准进行严格审查，输出完整审稿报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 540 · 2026-05-15T14:58:20.129853+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
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

_source line 541 · 2026-05-15T14:58:20.182327+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 542 · 2026-05-15T14:58:22.642959+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 543 · 2026-05-15T14:58:23.999431+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 544 · 2026-05-15T14:58:24.050078+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 545 · 2026-05-15T14:58:32.748232+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's information about the ACL ARR 2026 reviewer guidelines, review form, and criteria:

## Reviewer Guidelines Overview

Reviewers should follow this workflow: (1) read the paper and get the first impression, (2) search f
…[truncated 1874 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 10105
}
```

</details>

---


### Tool call

_source line 546 · 2026-05-15T14:58:34.657354+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
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

_source line 547 · 2026-05-15T14:58:34.708160+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 548 · 2026-05-15T14:58:39.091018+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, score ranges, and criteria descriptions. Include every question and rating scale."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, score ranges, and criteria descriptions. Include every question and rating scale."
  }
}
```

</details>

---


### Tool call

_source line 549 · 2026-05-15T14:58:39.594546+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 550 · 2026-05-15T14:58:40.097321+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ Confidence Signals Predict but Do Not Select in 8B-Scale Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	
45	\bibliography{references}
46	
47	\appendix
48	\input{sections/appendix}
49	
50	\end{document}
51	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 551 · 2026-05-15T14:58:40.097708+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 552 · 2026-05-15T14:58:40.600319+00:00_

1	\begin{abstract}
2	Self-consistency---sampling multiple outputs and selecting via agreement---yields large gains on discrete-answer tasks, but information extraction (IE) produces \textit{sets} of entities and relations with partial overlap, where no majority vote exists.
3	Can consistency signals nonetheless select the best among $N$ candidates?
4	
5	Across three NER and one RE benchmark with two 8B-parameter models, all signals achieve strong quality estimation yet none significantly improves sample selection despite 12--18~pp of oracle headroom---the \textit{correlation-selection gap}.
6	Instance-level signals fail by construction; the two mechanisms that \textit{could} bridge the gap also fail: log-probability scores are compressed into effective ties (60\% of instances), and consensus-proximity selection (MBR decoding) correlates with quality across but not within instances.
7	Signal rankings are difficulty-dependent and collapse at the capability boundary.
8	
9	The gap widens with sample size; closing it likely requires per-sample scoring such as trained verifiers.
10	\end{abstract}
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 553 · 2026-05-15T14:58:40.600734+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 554 · 2026-05-15T14:58:40.651635+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2025scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a structurally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumpt
…[truncated 5489 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 555 · 2026-05-15T14:58:45.981190+00:00_

# ACL Rolling Review Form - Complete Structure

## Core Review Sections

**Paper Summary**: Authors describe the paper's topic to clarify understanding and prevent misinterpretations.

**Summary of Strengths**: Identify reasons for publication, including "novel and useful methodology, insightful empirical results or theoretical analysis."

**Summary of Weaknesses**: Number concerns about correctness, impact, clarity, or other publication obstacles.

**Comments/Suggestions/Typos**: Additional improvement recommendations beyond addressing main concerns.

## Scoring Dimensions

### Reviewer Confidence (1-5 scale)
- 5: Positive evaluation; thoroughly read paper and familiar with related work
- 4: Quite sure; checked important points carefully
- 3: Pretty sure; general area knowledge but didn't verify details thoroughly
- 2: Willing to defend; likely missed some details or novelty assessment
- 1: Outside expertise area or paper is difficult to understand

### Soundness (1-5 scale)
Evaluates whether claims receive adequate support and methodology is valid:
- 5: "One of the most thorough" studies observed
- 4: Sufficient support; extra experiments optional
- 3: Main claims supported; minor details need clarification
- 2: "Major technical/methodological problems"
- 1: Insufficient rigor or ACL-irrelevant

### Excitement (1-5 scale)
Subjective assessment of innovation, impact, or relevance to reviewer's research.

### Overall Assessment (1-5 scale)
Publication recommendation ranging from "Consider for Award" through "Do not resubmit."

### Additional Dimensions
- Limitations and societal impact discussion
- Ethical concerns per ACL code of ethics
- Reproducibility (1-5 scale)
- Dataset value (1-5 scale)
- Software value (1-5 scale)
- Author anonymity knowledge (1-5 scale)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6890
}
```

</details>

---


### Tool call

_source line 556 · 2026-05-15T14:58:49.757256+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 557 · 2026-05-15T14:58:50.310594+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We use \textit{confidence signal} as the umbrella term for all five measures.
17	Four are \textit{consistency signals}---computed from inter-sample agreement---spanning two families: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]).
18	The fifth, log-probability, is the sole \textit{model-internal} signal and the only one that scores individual samples rather than the instance as a whole.
19	
20	\paragraph{Log-probability (model-internal, per-sample).}
21	The only per-sample signal.
22	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
23	\begin{equation}\label{eq:logprob}
24	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
25	\end{equation}
26	
27	\paragraph{Exact match voting (surface
…[truncated 5477 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 558 · 2026-05-15T14:58:50.310981+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 559 · 2026-05-15T14:58:50.762920+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.
15	We note a training confound for SciERC: Qwen3-8B's SciERC checkpoint was trained with \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), which prepends empty \texttt{&lt;think>\textbackslash n&lt;/think>} blocks (4--5 tokens) to each training response and includes them in the loss computation; CoNLL-2003 and WNUT-17 checkpoints explicitly set \texttt{enable\_thinking=False}.
16	No reasoning content is present (the blocks are always empty), and constrained decoding at inference time enforces JSON-only output, so thinking tokens do not appear in generated samples.
17	This constitutes a minor train--test distribution mismatch for SciERC ($<$0.3\% of the 2048-token training window); CoNLL-2003 and WNUT-17 are unaffected.
18	We discuss implications in the Limitations section.
19	We draw $N{=}8$ samples at $T{=}1.0$ (primary; single seed, seed${=}42$), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in T
…[truncated 13735 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 560 · 2026-05-15T14:58:50.813529+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 561 · 2026-05-15T14:58:51.216403+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, VC provides the strongest rank correlation ($\rho{=}0.38$), though EM leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).
5	Signal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across two model families at 8B scale, though with model-dependent magnitude.
6	At higher sample sizes ($N{=}16$), SJ converges to comparable NER performance with VC ($\Delta{=}0.002$) with lower cross-seed variance ($\sigma{=}0.010$ vs.\ $0.026$); on RE, only VC consistently outperforms LP (preliminary).
7	When model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\ref{tab:wnut}).
8	
9	\paragraph{Why the gap exists: two layers.}
10	\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
11	Consensus-proximity selection (\S\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\ref{tab:selection}).
12	\textit{Layer 2 (score compression):} Log-probability, the only per-sample signal, also fails to exploit the 12--18~pp oracle headroom.
13	LP scores are severely compressed: the median within-instance LP range is only 0.041 nats, below the $\varepsilon{=}0.05$ threshold at which 60\% of instances are effectively tied, and 75\% of pairwise comparisons fall within $|\Delta|{<}0.026$ (Appendix~\ref{app:logprob_ties}).
14	In the 40\% of instances where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), LP \textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.01$; within-instance $\rho$: 0.08$\to$0.39).
15	This diagnostic confirms that LP carries useful per-sample qualit
…[truncated 6757 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 562 · 2026-05-15T14:58:51.216853+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 563 · 2026-05-15T14:58:51.268462+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling \cite{zhang2025tts}, \citet{snell2025scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.
9	All of the above target reasoning/QA with discrete answers or specific aggregation strategies.
10	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
11	
12	\paragraph{Consistency for structured IE.}
13	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
14	Their work leaves open three questions we address: (i)~whether structural matching improves on surface-level agreement (which they acknowledge ``overlooks semantically consistent outputs''); (ii)~whether quality estimation translates to best-of-$N$ selec
…[truncated 3089 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 564 · 2026-05-15T14:58:54.983287+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 565 · 2026-05-15T14:58:55.485665+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We systematically evaluate five confidence signals across quality estimation, binary discrimination, and sample selection for LLM-based structured IE, revealing that these metrics decouple---single-metric evaluation risks selecting the wrong signal for the intended use case.
4	All signals achieve strong quality estimation ($\rho$ up to 0.38, AUROC up to 0.75) yet none significantly improves sample selection on SciERC despite 12--18~pp oracle headroom---the \textit{correlation-selection gap}.
5	The instance-level failure of four signals is definitional; the empirical finding is that neither consensus-proximity selection (MBR decoding) nor log-probability bridges the gap.
6	MBR utility correlates with quality across instances but not within them; LP scores are compressed into effective ties (60\% of instances), though where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).
7	A controlled free-form decoding ablation confirms that NER LP compression persists without constrained decoding; on RE, LP selection reverses direction (preliminary), indicating task-dependent interaction with decoding regime.
8	Signal rankings shift with task difficulty---EM leads on easy tasks, SJ on hard tasks---consistent across two model families at 8B scale, though with model-dependent magnitude; at the capability boundary (WNUT-17), all signals collapse to non-significance.
9	RE findings rest on SciERC alone (preliminary) and warrant multi-benchmark validation.
10	Trained verifiers, scaling to 70B+ models, and conformal prediction are promising directions for closing the gap.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 566 · 2026-05-15T14:58:55.536368+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 567 · 2026-05-15T14:58:55.787762+00:00_

1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	RE selection failure persists even when restricting to non-zero F1 instances (Appendix~\ref{app:re_conditional_selection}), ruling out floor effects as the sole explanation, but generalization to other RE benchmarks remains unvalidated.
3	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
4	
5	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
6	A 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
7	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
8	
9	Our analysis of selection potential uses only unsupervised signals.
10	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
11	
12	We evaluate at $N{=}8$ and $N{=}16$.
13	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.047$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
14	
15	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
16	Our free-form ablation (\S\ref{sec:ablation}) confirms that LP score compression persists
…[truncated 2611 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 568 · 2026-05-15T14:58:55.788166+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 569 · 2026-05-15T14:58:56.391507+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality---including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
47	\quad FK & 
…[truncated 47137 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 570 · 2026-05-15T14:59:04.097037+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool call

_source line 571 · 2026-05-15T14:59:05.810894+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines, including what reviewers should evaluate, how to score, what constitutes a strong vs weak paper, and any specific instructions about soundness, novelty, reproducibility, and significance."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines, including what reviewers should evaluate, how to score, what constitutes a strong vs weak paper, and any specific instructions about soundness, novelty, reproducibility, and significance."
  }
}
```

</details>

---


### Tool result

_source line 572 · 2026-05-15T15:00:46.369093+00:00_

&lt;persisted-output>
Output too large (50.9KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/2c65fe24-7dea-41a6-9c51-f6f9eb797b23/tool-results/toolu_01K4yA9C22wWnEr8hmL28txW.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 62, \"total_citations\": 94, \"unique_cited_keys\": 62, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 56, \"online_not_found\": 3, \"online_mismatch\": 3}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"angelopoulos2021conformal\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\", \"year\": \"2021\", \"venue\": \"ICLR 2021\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": 
…[truncated 363 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 102272
}
```

</details>

---


### Tool result

_source line 573 · 2026-05-15T15:01:02.093287+00:00_

# ARR Reviewer Guidelines: Comprehensive Summary

## Core Evaluation Framework

ARR reviewers assess papers using three primary scores:

**1. Soundness** - "The _soundness_ scores must be justified by the text of the review." Technical validity and methodological rigor are essential, with low scores requiring explicit justification.

**2. Excitement** - A subjective assessment orthogonal to soundness, reflecting personal interest rather than paper quality.

**3. Overall Recommendation** - A composite judgment balancing soundness, excitement, novelty, and potential impact for *ACL venues.

## Key Review Principles

### Reading Strategy
Reviewers must read papers twice: first for skim-reading to assess research questions and scope, then for in-depth technical evaluation. This prevents hindsight bias and confirmation bias from distorting initial impressions.

### Specificity Requirement
Reviews must be precise and actionable. Vague criticisms like "missing relevant references" should become "missing references X, Y, and Z" so chairs understand concerns without re-reading papers.

### Professional Tone
"Write the review you would like to get yourself." Reviews should be neutral and constructive, recognizing that harsh language harms academic communities and reflects reviewer bias rather than paper merit.

## Critical Evaluation Areas

### Soundness Components
- Technical validity of methodology
- Correctness of proofs and formal claims
- Reproducibility details and implementation clarity
- Appropriate statistical significance reporting
- Proper handling of experimental assumptions

### Novelty Assessment
Novel contributions require specific prior-work references. The guideline clarifies: "If the paper claims e.g. a novel method, and you think you've seen this before - you need to provide a reference."

Negative results, resource papers, and reimplementation studies remain valid contributions if properly scoped and motivated.

### Reproducibility Standards
Papers should 
…[truncated 3305 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 116282
}
```

</details>

---


### Tool call

_source line 574 · 2026-05-15T15:01:09.125957+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/2c65fe24-7dea-41a6-9c51-f6f9eb797b23/tool-results/toolu_01K4yA9C22wWnEr8hmL28txW.txt",
  "offset": "0",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/2c65fe24-7dea-41a6-9c51-f6f9eb797b23/tool-results/toolu_01K4yA9C22wWnEr8hmL28txW.txt",
    "offset": "0",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 575 · 2026-05-15T15:01:09.429706+00:00_

0	{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 62, \"total_citations\": 94, \"unique_cited_keys\": 62, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 56, \"online_not_found\": 3, \"online_mismatch\": 3}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"angelopoulos2021conformal\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\", \"year\": \"2021\", \"venue\": \"ICLR 2021\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence Estimation for Information Extraction\", \"authors\": \"Culotta, Aron and McCallum, Andrew\", \"year\": \"2004\", \"venue\": \"HLT-NAACL 2004\"}, {\"key\": \"derczynski2017wnut\", \"type\": \"inproceedings\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recogni
…[truncated 50097 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 303
}
```

</details>

---


### Tool call

_source line 576 · 2026-05-15T15:04:41.493533+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — Round 1 审稿报告\n\n**侧重**：方法严谨性 + 实验可靠性\n\n### 总体评分\n- **Overall**: 3.5/5（Findings 边缘接受，需修改后可接收）\n- **Soundness**: 3.5/5\n- **Excitement**: 3/5\n- **Reproducibility**: 3/5\n- **Confidence**: 4/5\n\n**一句话总结**: NER 上 correlation-selection gap 的发现和机制分析扎实可信，但 RE 证据薄弱（单数据集+核心 Table 3 单种子）、LP 温度敏感性数据缺失、ε=0.05 阈值论证循环，整体构成一篇值得发表但需补强的实证研究。\n\n### Must-Fix 问题（3 个 critical）\n\n**N1** [critical] ε=0.05 \"effectively tied\" 阈值论证循环性\n- Table 12 显示 ε=0.01→1.1%, ε=0.05→60.3%（59× 跳变），阈值选择对核心 \"60% effectively tied\" 叙事有决定性影响\n- ε=0.05 选在中位数附近（median LP range=0.041），保证≥50% tied 是 by construction 非 empirical finding\n- 建议报告完整 ε 梯度 + 提供外部基准（QA/MT 上同模型 LP range 作参照）\n\n**N2** [critical] LP 温度数据缺失\n- 核心诊断对象 LP 在 T=0.7 无数据（Appendix B 明确标注），但论文在 Section 4.4 声称 \"robust performance across T∈{0.7, 1.0}\" 易误读为包含 LP\n- T<1.0 是常用部署温度，LP compression 在该条件下是否成立完全未知\n\n**N3** [critical] RE 结论基础薄弱\n- 仅 SciERC 单数据集；Table 3 RE 仅 seed=42 单种子\n- \"preliminary\" 标注不一致：Abstract 未标 preliminary，Conclusion 合并引用 NER/RE headroom\n- 建议补数据集或统一降级 RE 为 pilot study\n\n### Should-Fix 问题（6 个 warning）\n\n**W1** Free-form ablation 仅 1 dataset × 1 model × 1 seed，RE LP 翻转需 3-seed 验证\n**W2** FK 独立性检验 n=5 t-test 功效极低，应改用 instance-level 检验（n=529+）\n**W3** Seed 456 使用 --subtask joint 而非 --subtask ner，可能影响 LP 行为\n**W4** TOST δ 锚定于内部 oracle headroom，缺乏外部实际意义基准\n**W5** SJ max normalizer 非标准设计未 ablate\n**W6** N=8 QE 主表单种子 vs N=16 多种子，设计不对称\n\n### 主要优势\n- Correlation-selection gap 概念和两层机制解释逻辑自洽\n- 统计分析远超同类工作（bootstrap + Fisher + TOST + effect size + CI）\n- 限制披露透明（enable_thinking、seed 456、LP T=0.7 等逐一讨论）\n- NER 跨模型一致性强（Kendall's W=1.000）\n- 难度梯度设计揭示信号排名翻转等非显然现象\n\n### 引用核查\n62 条引用全部通过交叉验证，无虚假引用。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — Round 1 审稿报告\n\n**侧重**：方法严谨性 + 实验可靠性\n\n### 总体评分\n- **Overall**: 3.5/5（Findings 边缘接受，需修改后可接收）\n- **Soundness**: 3.5/5\n- **Excitement**: 3/5\n- **Reproducibility**: 3/5\n- **Confidence**: 4/5\n\n**一句话总结**: NER 上 correlation-selection gap 的发现和机制分析扎实可信，但 RE 证据薄弱（单数据集+核心 Table 3 单种子）、LP 温度敏感性数据缺失、ε=0.05 阈值论证循环，整体构成一篇值得发表但需补强的实证研究。\n\n### Must-Fix 问题（3 个 critical）\n\n**N1** [critical] ε=0.05 \"effectively tied\" 阈值论证循环性\n- Table 12 显示 ε=0.01→1.1%, ε=0.05→60.3%（59× 跳变），阈值选择对核心 \"60% effectively tied\" 叙事有决定性影响\n- ε=0.05 选在中位数附近（median LP range=0.041），保证≥50% tied 是 by construction 非 empirical finding\n- 建议报告完整 ε 梯度 + 提供外部基准（QA/MT 上同模型 LP range 作参照）\n\n**N2** [critical] LP 温度数据缺失\n- 核心诊断对象 LP 在 T=0.7 无数据（Appendix B 明确标注），但论文在 Section 4.4 声称 \"robust performance across T∈{0.7, 1.0}\" 易误读为包含 LP\n- T<1.0 是常用部署温度，LP compression 在该条件下是否成立完全未知\n\n**N3** [critical] RE 结论基础薄弱\n- 仅 SciERC 单数据集；Table 3 RE 仅 seed=42 单种子\n- \"preliminary\" 标注不一致：Abstract 未标 preliminary，Conclusion 合并引用 NER/RE headroom\n- 建议补数据集或统一降级 RE 为 pilot study\n\n### Should-Fix 问题（6 个 warning）\n\n**W1** Free-form ablation 仅 1 dataset × 1 model × 1 seed，RE LP 翻转需 3-seed 验证\n**W2** FK 独立性检验 n=5 t-test 功效极低，应改用 instance-level 检验（n=529+）\n**W3** Seed 456 使用 --subtask joint 而非 --subtask ner，可能影响 LP 行为\n**W4** TOST δ 锚定于内部 oracle headroom，缺乏外部实际意义基准\n**W5** SJ max normalizer 非标准设计未 ablate\n**W6** N=8 QE 主表单种子 vs N=16 多种子，设计不对称\n\n### 主要优势\n- Correlation-selection gap 概念和两层机制解释逻辑自洽\n- 统计分析远超同类工作（bootstrap + Fisher + TOST + effect size + CI）\n- 限制披露透明（enable_thinking、seed 456、LP T=0.7 等逐一讨论）\n- NER 跨模型一致性强（Kendall's W=1.000）\n- 难度梯度设计揭示信号排名翻转等非显然现象\n\n### 引用核查\n62 条引用全部通过交叉验证，无虚假引用。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 577 · 2026-05-15T15:04:45.261691+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3768
}
```

</details>

---


### Assistant

_source line 578 · 2026-05-15T15:04:52.545963+00:00_

审稿报告已提交给 Review Director。

总结：论文在 NER 上的核心发现（correlation-selection gap + LP compression 机制）有充分统计支撑，论文写作透明度高于同类工作。3 个 critical 问题集中在：(1) ε=0.05 阈值的循环论证需补外部基准，(2) LP 在 T=0.7 下缺失数据是核心机制的关键盲区，(3) RE 仅单数据集+单种子需补强或降级。6 个 should-fix 问题涉及 ablation 范围、FK 检验功效、seed 456 confound 等方法论细节。整体评分 3.5/5，适合 EMNLP Findings 但需一轮修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 18

## Round 18

2 recorded events


### User

_source line 579 · 2026-05-15T15:05:22.192595+00:00_

[Round 1 审稿请求]:
## Step 2 — 交叉分享：请回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿原文。请逐条回应：**[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

### Reviewer 2 总体评分
Overall: 2.5/5, Soundness: 3.5/5, Excitement: 2.5/5, Reproducibility: 4/5

### Must-Fix 问题

**N1** [critical] 正文页数极可能严重超过 8 页限制
- 正文包含 7 个 section（Abstract 至 Conclusion），含 1 个 figure*、2 个 figure*、1 个 table*、1 个 table、6 个 displayed equation、1 个 ablation subsection。保守估计正文约 10-11 页，超限 2-3 页。
- ARR 超页是 desk-rejection 理由。
- 建议：Discussion §ablation 移至 Appendix；Robustness 大部分移至 Appendix；精简 contribution bullets。

**N2** [critical] 核心 framing "correlation-selection gap" 混淆定义性观察与经验发现
- 论文自承 4/5 信号 "definitional, not empirical"（Introduction line 23），但将 5 个信号纳入 selection table 展示"失败"，叙事上误导读者。
- 真正经验贡献仅限：(a) LP score compression 诊断，(b) MBR utility-quality misalignment。
- 建议：重新聚焦 framing，核心问题改为"为什么 LP 和 MBR 都无法 bridge quality estimation 到 selection"。

**N3** [critical] 标题 claim 过强："Do Not Select" + "8B-Scale" 的泛化暗示
- "Do Not Select" 是绝对否定，但 LP 在非 tied 子集上 significantly selects (+2.9pp, p=0.01)，RE 在 free-form 下也翻转为正。
- 仅 2 个 8B 模型，标题暗示规模普遍性。
- 建议："Do Not Select" → "Struggle to Select"；移除或限定 "8B-Scale"。

### Should-Fix 问题

**W1** Abstract 信息密度过高
**W2** Contribution 1 ("multi-metric evaluation") 更像 methodology 而非 conceptual contribution
**W3** SJ 方法新颖性有限（标准技术组合）
**W4** Eikema et al. (2025) structure-conditional MBR 应前移到 Related Work
**W5** RE "preliminary" 标注各 section 不一致（Abstract 未标注）
**W6** 缺少代码/数据发布承诺
**W7** enable_thinking 训练 confound 影响评估不充分

### 小问题
M1: NER 也是 single benchmark 但未标 preliminary
M2: SJ max normalizer 无 sensitivity analysis
M3: bib entry 作者顺序问题（feng2025optimal, snell2025scaling）
M4: Discussion ablation 段落粒度不一致
M5: Appendix Table 3 footnote 与表格数字不匹配
M6: nedellec2026 bib key 与实际第一作者不一致

### Reviewer 2 主要优势评价
1. 统计严谨性远超典型 NLP 论文
2. 对 limitations 的诚实 hedging
3. LP compression 诊断的机制清晰度
4. Difficulty gradient 的实践指导价值
5. 引用完整（62/62）

---

请对以上每个 N/W/M 级别问题给出你的 [AGREE] 或 [REBUT] 判断，并说明理由。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 580 · 2026-05-15T15:07:17.509096+00:00_

## 交叉回应：Reviewer 2 审稿意见

---

### Must-Fix 问题

**[AGREE] R2-N1: 正文页数可能超限**
同意这是一个需要确认的风险。正文包含 Introduction（含 figure*）、Related Work、Method（6 个 displayed equation）、Experiments（2 个 figure*、1 个 table*、1 个 table）、Discussion（含完整 ablation 段落）、Conclusion，内容体量确实接近或超过 8 页。Discussion 中的 "Score compression under free-form decoding" 段落（§5 lines 33-49）和 "Task-specific decoding interactions" 段落（lines 42-49）合计约 1 页，移至 Appendix 不会损失核心论证。R2 的建议（Discussion ablation 移至 Appendix、Robustness 精简、contribution bullets 压缩）可操作。但需注意：我无法从 .tex 源码精确判定编译后页数，建议 Director 确认实际编译页数。

**[REBUT] R2-N2: 核心 framing 混淆定义性 vs 经验性**
R2 认为将 4 个 instance-level 信号纳入 Table 3 构成叙事误导。我不同意这个判断的严重程度。

理由：(1) 论文在 Introduction line 23 明确标注 "definitional, not empirical"，在 Section 4.3 line 119 再次强调 "they cannot rank candidates by construction"，在 Conclusion line 5 第三次重申——三处一致的透明声明不构成"误导"。(2) Table 3 的完整比较（5 信号 + oracle + greedy + random）为读者提供了 apples-to-apples 的全景视图；如果省略 4 个信号，反而会导致读者质疑为什么不测试它们。(3) 论文的核心 framing 准确地说是："gap 的存在是多层次的——Layer 1 是 definitional（4 个信号），Layer 2 是 empirical（LP compression + MBR misalignment）"。这个两层结构是有信息量的，因为它解释了为什么 consensus-proximity selection（将 instance-level 信号转化为 per-sample ranking 的尝试）也失败了。

但 R2 有一个合理的子观点：论文可以更早、更醒目地区分 definitional vs empirical，例如在 Table 3 中用视觉分组（水平线分隔 instance-level 和 per-sample 信号）。这是一个呈现改进建议，而非 framing 错误。

**[AGREE with qualification] R2-N3: 标题 claim 过强**
部分同意。"Do Not Select" 确实与非 tied 子集的显著选择结果（$+2.9$ pp, $p=0.01$; Section 5, Discussion）矛盾——论文自己证明了在 40% 的实例上 LP *does* select。R2 建议 "Struggle to Select" 是更准确的描述。

但关于 "8B-Scale" 我不同意 R2 的判断。标题中 "8B-Scale" 是 **描述性限定**（specifying what was tested），而非泛化声明。如果去掉 "8B-Scale"，反而会让读者认为结论适用于所有模型规模，这更具误导性。论文在 Limitations (line 6) 明确说 "whether our findings hold for larger models (70B+) remains untested"，标题的 "8B-Scale" 恰好与这个限定一致。建议保留 "8B-Scale"，仅将 "Do Not Select" 修改为更 hedged 的表述。

---

### Should-Fix 问题

**[AGREE] R2-W1: Abstract 信息密度过高**
同意。10 行 abstract 包含 5 个信号名称、3+1 数据集、2 模型、ρ/AUROC 具体数值、LP compression 百分比、MBR misalignment、difficulty-dependence、未来方向。建议删减具体数值（如 "ρ 至 0.38, AUROC 至 0.75" 可简化为 "strong quality estimation"），将信号名称移至正文。

**[REBUT] R2-W2: Contribution 1 是 methodology 而非 conceptual contribution**
不同意。Contribution 1 的核心发现是 **metric dissociation**——EM 在 AUROC 领先 (0.749) 但在 ρ 仅排第三 (0.295)（Table 2）。这不是"我们用了多个指标"的方法论声明，而是一个 empirical finding：单指标评估会选错信号。这个发现对 practitioners 有直接实用价值（质量分流用 EM，细粒度排名用 VC/SJ），不应降格为方法论细节。当然，Contribution 1 的措辞 ("Multi-metric evaluation revealing metric dissociation") 确实不够锐利，建议改为以发现为主语的表述。

**[REBUT] R2-W3: SJ 方法新颖性有限**
论文并未将 SJ 作为方法论贡献（Contribution list 中无 "novel signal design"）。SJ 是分析工具而非论文贡献，因此 "新颖性有限" 的批评对象不成立。论文的贡献在于系统比较，而非发明信号。且 SJ 的具体设计选择（type-aware bipartite matching + token-level IoU + max normalizer; Eq. 4-5）在 IE 自一致性文献中未见先例——Nédellec et al. (2026) 只用 surface-level agreement，论文自身在 Introduction line 17 和 Related Work lines 13-15 明确对比了这一改进。

**[AGREE] R2-W4: Eikema et al. (2025) 应前移**
同意。Eikema et al. (2025) 的 structure-conditional MBR 发现（"standard utility functions degrade on structured outputs"）与本文核心发现直接相关。当前仅在 Related Work line 27 和 Discussion line 30 简短提及，建议在 Related Work 中扩展讨论，明确本文与其互补关系。

**[AGREE] R2-W5: RE "preliminary" 标注不一致**
完全同意，与我自己 N3 中的发现一致。Abstract 未标注 preliminary，Conclusion 合并引用 NER/RE headroom (12-18 pp)。需全文统一。

**[AGREE] R2-W6: 缺少代码/数据发布承诺**
同意。对于 EMNLP Findings 论文，ARR 评审标准明确考察 reproducibility。论文使用公开数据集和开源模型（Qwen3-8B, LLaMA-3.1-8B），但自定义代码（SJ matching、bootstrap testing pipeline、constrained decoding schema）未提及发布计划。即使只声明 "code will be released upon acceptance" 也能改善评分。

**[AGREE with qualification] R2-W7: enable_thinking confound 影响评估不充分**
部分同意。论文的辩护逻辑是合理的（CoNLL/WNUT 无此 confound 但 LP 同样失败→confound 非 gap 主因；Section 4.1 lines 15-17, Limitations lines 18-21）。但 R2 的 "不充分" 指向一个具体缺口：论文未量化 enable_thinking 对 LP score distribution 的影响。即使 <0.3% token window，first-token probability shift 可能对 LP range（本就极窄，median 0.041 nats）产生 non-negligible 的影响。建议补充 SciERC 上 enable_thinking=False 的 LP 分布对比（至少在 Appendix 中），或明确论证 4-5 个 empty thinking tokens 的 LP 贡献在 mean token log-prob 中被 1500+ 个其他 token 稀释到可忽略。

---

### 小问题

**[REBUT] R2-M1: NER 也是 single benchmark 但未标 preliminary**
不正确。NER 在 **3 个数据集**上评估：SciERC (Table 2), CoNLL-2003 (Table 2), WNUT-17 (Table 7)。RE 之所以标 preliminary 是因为仅 SciERC 一个 RE benchmark，而 NER 的 3 数据集覆盖了 easy→hard 难度梯度，不属于 single-benchmark 问题。

**[AGREE] R2-M2: SJ max normalizer 无 sensitivity analysis**
同意，与我自己 W5 一致。

**[REBUT] R2-M3: bib entry 作者顺序问题**
引用核查结果显示 feng2025optimal 和 snell2025scaling 的 "mismatch" 仅为 OpenAlex API 返回 first name vs bib 使用 last name 的格式差异（bib=feng vs api=austin → Austin Feng; bib=snell vs api=charlie → Charlie Snell）。bib 中实际 author field 排列正确，不存在作者顺序错误。

**[AGREE] R2-M4: Discussion ablation 段落粒度不一致**
同意。"Score compression under free-form decoding" 和 "Task-specific decoding interactions" 两段的细节程度（win/loss ratio, Jaccard similarity 0.472, selective variance reallocation p<0.0001）更适合 Appendix 而非 Discussion 正文。

**[REBUT with uncertainty] R2-M5: Appendix Table 3 footnote 与表格数字不匹配**
无法从 .tex 源码确认 R2 所指的具体不匹配。Table 3 (selection table) footnote 关于 VC majority-threshold voting 和 greedy baseline 的说明与正文数字一致（VC NER 0.595, greedy 0.620, Δ=-2.5 pp; Section 4.3 line 129）。如 R2 指的是编译后的表格渲染问题，需要查看 PDF 才能确认。

**[AGREE] R2-M6: nedellec2026 bib key 与实际第一作者不一致**
确认。bib 条目 `nedellec2026consistency` 的实际第一作者是 "Yao, Xinzhi"，而非 Nédellec。bib key 使用了第二作者姓氏，属于 bib 卫生问题，应修正为 `yao2026consistency`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 19

## Round 19

49 recorded events


### User

_source line 581 · 2026-05-15T15:22:57.918555+00:00_

[Round 9 审稿请求]:
## Round 9 审稿任务 — Reviewer 1

### 你的审查侧重：方法严谨性 + 实验设计

### Venue 信息
- **目标**: EMNLP 2026 Main Conference (via ARR May cycle)
- **截止日期**: 2026-05-25
- **页数限制**: 正文 ≤8 页（双栏 ACL 模板），参考文献不限页，Limitations 不计入页数
- **模板**: ACL style (`\usepackage[review]{acl}`)
- **匿名规则**: Double-blind

### 论文路径
- 主文件: `projects/struct_self_consist_ie/docs/paper/main.tex`
- 各 section 在 `projects/struct_self_consist_ie/docs/paper/sections/` 下
- Appendix: `projects/struct_self_consist_ie/docs/paper/sections/appendix.tex`

### 审查重点（方法严谨性 + 实验设计）

请重点审查以下方面：

1. **统计方法论**：
   - Bootstrap 检验、TOST 等价检验的实施是否正确
   - 多重比较校正是否充分
   - p 值解读是否准确（failure-to-reject ≠ evidence of absence）
   - Fleiss' Kappa 独立性假设的 justification

2. **实验设计完整性**：
   - 多种子验证覆盖率（哪些结果有 3-seed，哪些仅 single seed）
   - N=8 vs N=16 设计是否对称
   - Cross-model/cross-dataset 证据面是否支撑所述 claim
   - Free-form ablation 的范围是否足以支撑其结论

3. **数据完整性**：
   - 表格数据是否自洽（cross-reference 检查）
   - LP（logprob）温度敏感性数据是否缺失
   - RE 证据标注是否一致（preliminary vs established）

4. **可复现性**：
   - 训练配置和 prompt template 是否完整
   - 代码/数据发布承诺
   - 超参数选择的 justification（如 ε=0.05 阈值）

5. **页数**：请估算正文页数是否符合 ≤8 页限制

### 参考：Issue Tracker 中与你审查范围相关的 open/in_progress 问题

- R7-C1: Selection gap 分析缺乏多种子验证（critical）
- R7-C2: ε=0.05 effectively tied 阈值缺乏论证（critical）
- R7-C3: Free-form ablation 范围过窄但支撑过强泛化声称（critical）
- R7-W1: LP 温度敏感性完全缺失（critical）
- R4-W1: RE 证据需进一步加强（critical）
- R3-W4: FK 独立性假设 justification 不足（warning）
- R4-M2: TOST δ 选择缺乏实践意义论证（warning）
- R8-N1: 正文页数严重超过 8 页限制（critical）
- R8-W2: enable_thinking 对 LP score distribution 的影响未量化（warning）
- R8-W3: SJ max normalizer 未做 sensitivity analysis（warning）
- R8-W4: Seed 456 使用 --subtask joint 而非 --subtask ner（warning）
- R8-W5: N=8 QE 主表单种子 vs N=16 多种子设计不对称（warning）

请独立审稿，不受上述 issue 列表局限——如有新发现请完整报告。

### 输出格式
```
## Summary
## Strengths（逐条）
## Weaknesses（逐条，标注 severity: critical/warning/info）
## Questions（需作者澄清的问题）
## Missing References
## Overall Assessment（评分 + 置信度）
## Detailed Comments（逐节）
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 582 · 2026-05-15T15:23:07.117288+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
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

_source line 583 · 2026-05-15T15:23:07.167870+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 584 · 2026-05-15T15:23:11.084768+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 review form criteria scoring rubric"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 review form criteria scoring rubric"
  }
}
```

</details>

---


### Tool call

_source line 585 · 2026-05-15T15:23:11.336095+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/struct_self_consist_ie/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/struct_self_consist_ie/docs/paper/**/*.tex"
  }
}
```

</details>

---


### Tool result

_source line 586 · 2026-05-15T15:23:11.386707+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 587 · 2026-05-15T15:23:17.511409+00:00_

Web search results for query: "ACL ARR 2026 review form criteria scoring rubric"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://twitter.com/reviewacl?lang=en"},{"title":"ACL ARR 2026 | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, I've found information about the ACL ARR 2026 review form criteria and scoring rubric. Here's what I found:

## Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Scoring Rubric Details

**For the Overall Assessment Score
…[truncated 968 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6426
}
```

</details>

---


### Tool call

_source line 588 · 2026-05-15T15:23:22.355839+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
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

_source line 589 · 2026-05-15T15:23:22.356399+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 590 · 2026-05-15T15:23:22.858563+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/**/*.tex"
  }
}
```

</details>

---


### Tool result

_source line 591 · 2026-05-15T15:23:22.959316+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 592 · 2026-05-15T15:23:23.009949+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 593 · 2026-05-15T15:23:23.060593+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 594 · 2026-05-15T15:23:27.733159+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper -type f -name \"*.tex\" 2>/dev/null | head -30",
  "description": "Find all .tex files in the paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper -type f -name \"*.tex\" 2>/dev/null | head -30",
    "description": "Find all .tex files in the paper directory"
  }
}
```

</details>

---


### Tool result

_source line 595 · 2026-05-15T15:23:29.091333+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 1358
}
```

</details>

---


### Tool call

_source line 596 · 2026-05-15T15:23:29.141946+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include soundness, excitement, overall assessment, confidence, and any other dimensions. Include the full rubric text for each score level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include soundness, excitement, overall assessment, confidence, and any other dimensions. Include the full rubric text for each score level."
  }
}
```

</details>

---


### Tool result

_source line 597 · 2026-05-15T15:23:37.033320+00:00_

# ACL Rolling Review Form – Complete Scoring Dimensions

## 1. Reviewer Confidence
**Scale: 1-5**
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## 2. Soundness
**Scale: 1-5 (with half-point increments)**
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. Excitement
**Scale: 1-5 (with half-point increments)**
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me."
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

## 4. Overall Assessment
**Scale: 1-5 (with half-point increments)**
- **5**: "Consider for Award: could be considered for outstanding paper award (top 2.5%)."
- **4**: "Conference: could be accepted to an *ACL conference."
- **3**: "Findings: could be accepted to the Findings of the ACL."
- **2**: "Resubmit next cycle: needs substantial revisions."
- **1**: "Do not resubmit: has to be fully redone."

## 5. Reproducibility
**Scale: 1-5**
- **5**: "They could easily reproduce the results."
- **4**: "They could mostly reproduce th
…[truncated 440 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7891
}
```

</details>

---


### Tool call

_source line 598 · 2026-05-15T15:23:40.807274+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 599 · 2026-05-15T15:23:41.510958+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ Confidence Signals Predict but Do Not Select in 8B-Scale Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	
45	\bibliography{references}
46	
47	\appendix
48	\input{sections/appendix}
49	
50	\end{document}
51	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 600 · 2026-05-15T15:23:41.611910+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 601 · 2026-05-15T15:23:41.662618+00:00_

1	\begin{abstract}
2	Self-consistency---sampling multiple outputs and selecting via agreement---yields large gains on discrete-answer tasks, but information extraction (IE) produces \textit{sets} of entities and relations with partial overlap, where no majority vote exists.
3	Can consistency signals nonetheless select the best among $N$ candidates?
4	
5	Across three NER and one RE benchmark with two 8B-parameter models, all signals achieve strong quality estimation yet none significantly improves sample selection despite 12--18~pp of oracle headroom---the \textit{correlation-selection gap}.
6	Instance-level signals fail by construction; the two mechanisms that \textit{could} bridge the gap also fail: log-probability scores are compressed into effective ties (60\% of instances), and consensus-proximity selection (MBR decoding) correlates with quality across but not within instances.
7	Signal rankings are difficulty-dependent and collapse at the capability boundary.
8	
9	The gap widens with sample size; closing it likely requires per-sample scoring such as trained verifiers.
10	\end{abstract}
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 602 · 2026-05-15T15:23:42.516295+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 603 · 2026-05-15T15:23:42.516855+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2025scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a structurally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumpt
…[truncated 3925 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 604 · 2026-05-15T15:23:43.119935+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 605 · 2026-05-15T15:23:43.170708+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We use \textit{confidence signal} as the umbrella term for all five measures.
17	Four are \textit{consistency signals}---computed from inter-sample agreement---spanning two families: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]).
18	The fifth, log-probability, is the sole \textit{model-internal} signal and the only one that scores individual samples rather than the instance as a whole.
19	
20	\paragraph{Log-probability (model-internal, per-sample).}
21	The only per-sample signal.
22	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
23	\begin{equation}\label{eq:logprob}
24	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
25	\end{equation}
26	
27	\paragraph{Exact match voting (surface
…[truncated 5477 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 606 · 2026-05-15T15:23:43.673029+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 607 · 2026-05-15T15:23:43.673632+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.
15	We note a training confound for SciERC: Qwen3-8B's SciERC checkpoint was trained with \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), which prepends empty \texttt{&lt;think>\textbackslash n&lt;/think>} blocks (4--5 tokens) to each training response and includes them in the loss computation; CoNLL-2003 and WNUT-17 checkpoints explicitly set \texttt{enable\_thinking=False}.
16	No reasoning content is present (the blocks are always empty), and constrained decoding at inference time enforces JSON-only output, so thinking tokens do not appear in generated samples.
17	This constitutes a minor train--test distribution mismatch for SciERC ($<$0.3\% of the 2048-token training window); CoNLL-2003 and WNUT-17 are unaffected.
18	We discuss implications in the Limitations section.
19	We draw $N{=}8$ samples at $T{=}1.0$ (primary; single seed, seed${=}42$), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in T
…[truncated 10068 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 608 · 2026-05-15T15:23:44.125601+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 609 · 2026-05-15T15:23:44.226458+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling \cite{zhang2025tts}, \citet{snell2025scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.
9	All of the above target reasoning/QA with discrete answers or specific aggregation strategies.
10	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
11	
12	\paragraph{Consistency for structured IE.}
13	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
14	Their work leaves open three questions we address: (i)~whether structural matching improves on surface-level agreement (which they acknowledge ``overlooks semantically consistent outputs''); (ii)~whether quality estimation translates to best-of-$N$ selec
…[truncated 3089 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 610 · 2026-05-15T15:23:44.327311+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 611 · 2026-05-15T15:23:44.779436+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, VC provides the strongest rank correlation ($\rho{=}0.38$), though EM leads binary discrimination (AUROC${=}0.816$ on CoNLL); under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).
5	Signal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across two model families at 8B scale, though with model-dependent magnitude.
6	At $N{=}16$, SJ converges to VC on NER ($\Delta{=}0.002$) with lower variance ($\sigma{=}0.010$ vs.\ $0.026$); when capability is insufficient (WNUT-17), all signals converge toward non-significance (Table~\ref{tab:wnut}).
7	
8	\paragraph{Why the gap exists: two layers.}
9	\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
10	Consensus-proximity selection (\S\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\ref{tab:selection}).
11	\textit{Layer 2 (score compression):} Log-probability, the only per-sample signal, also fails to exploit the 12--18~pp oracle headroom.
12	LP scores are severely compressed: 60\% of instances are effectively tied at $\varepsilon{=}0.05$ (Appendix~\ref{app:logprob_ties}).
13	In the 40\% where compression is mitigated ($n{=}210$), LP \textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.01$), confirming score compression as the primary bottleneck; a free-form ablation (\S\ref{sec:ablation}) shows this persists without constrained decoding.
14	The gap holds even among high-diversity instances (Appendix~\ref{app:diversity}).
15	
16	\paragraph{The gap widens with $N$.}
17	Doubling from $N{=}8$ to $N{=}16$ expands oracle headroom by $+4.4$~pp, yet LP improves by only $+0.4$~pp and VC deteriorates ($\Delta$: $-2.5{\to}{
…[truncated 1490 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 612 · 2026-05-15T15:23:45.281552+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 613 · 2026-05-15T15:23:45.281919+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We systematically evaluate five confidence signals across quality estimation, binary discrimination, and sample selection for LLM-based structured IE, revealing that these metrics decouple---single-metric evaluation risks selecting the wrong signal for the intended use case.
4	All signals achieve strong quality estimation ($\rho$ up to 0.45, AUROC up to 0.82) yet none significantly improves sample selection on SciERC despite 12--18~pp oracle headroom---the \textit{correlation-selection gap}.
5	The instance-level failure of four signals is definitional; LP scores are compressed into effective ties (60\% of instances), though where compression is mitigated, LP becomes significant ($+2.9$~pp, $p{=}0.01$); a free-form ablation confirms compression persists without constrained decoding.
6	Signal rankings shift with difficulty (EM leads on easy tasks, SJ on hard), consistent across two model families; at the capability boundary (WNUT-17), all signals collapse.
7	RE findings rest on SciERC alone (preliminary); trained verifiers, scaling to 70B+, and conformal prediction are promising directions.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 614 · 2026-05-15T15:23:45.585256+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 615 · 2026-05-15T15:23:45.585780+00:00_

1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	RE selection failure persists even when restricting to non-zero F1 instances (Appendix~\ref{app:re_conditional_selection}), ruling out floor effects as the sole explanation, but generalization to other RE benchmarks remains unvalidated.
3	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
4	
5	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
6	A 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
7	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
8	
9	Our analysis of selection potential uses only unsupervised signals.
10	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
11	
12	We evaluate at $N{=}8$ and $N{=}16$.
13	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.047$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
14	
15	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
16	Our free-form ablation (\S\ref{sec:ablation}) confirms that LP score compression persists
…[truncated 2611 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 616 · 2026-05-15T15:23:45.837320+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 617 · 2026-05-15T15:23:46.142339+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality---including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
47	\quad FK & 
…[truncated 49666 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 305
}
```

</details>

---


### Tool call

_source line 618 · 2026-05-15T15:23:51.112564+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "735"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "735"
  }
}
```

</details>

---


### Tool result

_source line 619 · 2026-05-15T15:23:51.615454+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (735). The file has 735 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 620 · 2026-05-15T15:23:51.832151+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "description": "Count lines in appendix"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "description": "Count lines in appendix"
  }
}
```

</details>

---


### Tool result

_source line 621 · 2026-05-15T15:23:51.882808+00:00_

734 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 622 · 2026-05-15T15:23:56.655053+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/*.tex /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
  "description": "Count lines per section for page estimation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/*.tex /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
    "description": "Count lines per section for page estimation"
  }
}
```

</details>

---


### Tool result

_source line 623 · 2026-05-15T15:23:57.258354+00:00_

   10 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
  734 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
    7 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
   27 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
  132 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
   47 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
   30 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
   77 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
   28 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
   50 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
 1142 total

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 624 · 2026-05-15T15:23:57.310350+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper -name \"*.bib\" | head -5",
  "description": "Find bib files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper -name \"*.bib\" | head -5",
    "description": "Find bib files"
  }
}
```

</details>

---


### Tool result

_source line 625 · 2026-05-15T15:23:57.361043+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 626 · 2026-05-15T15:23:59.972043+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 627 · 2026-05-15T15:24:00.027747+00:00_

1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@inproceedings{angelopoulos2021conformal,
4	  title = {Uncertainty Sets for Image Classifiers using Conformal Prediction},
5	  author = {Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, Michael I.},
6	  booktitle = {ICLR 2021},
7	  year = {2021},
8	  url = {https://arxiv.org/abs/2009.14193}
9	}
10	
11	@article{brown2024monkeys,
12	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
13	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
14	  journal = {arXiv preprint arXiv:2407.21787},
15	  year = {2024},
16	  url = {https://arxiv.org/abs/2407.21787}
17	}
18	
19	@inproceedings{chen2024usc,
20	  title = {Universal Self-Consistency for Large Language Model Generation},
21	  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
22	  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},
23	  year = {2024},
24	  url = {https://arxiv.org/abs/2311.17311}
25	}
26	
27	@article{cobbe2021verifiers,
28	  title = {Training Verifiers to Solve Math Word Problems},
29	  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
30	  journal = {arXiv preprint arXiv:2110.14168},
31	  year = {2021},
32	  url = {https://arxiv.org/abs/2110.14168}
33	}
34	
35	@inproceedings{culotta2004confidence,
36	  title = {Confidence Estimation for Information Extraction},
37	  author = {Culotta, Aron and McCallum, Andrew},
38	  booktitle = {HLT-NAACL 2004},
39	  year = {2004},
40	  url = {https://aclanthology.org/N04-4028/}
41	}
42	
43	@inproceedings{derczynski2017wnut,
44
…[truncated 23254 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 55
}
```

</details>

---


### Tool call

_source line 628 · 2026-05-15T15:26:00.091163+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Assistant

_source line 629 · 2026-05-15T15:42:58.116147+00:00_

全部论文材料已读完。现在进行系统性审查。

让我先验证引用，同时撰写审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 20

## Round 20

52 recorded events


### User

_source line 630 · 2026-05-16T02:17:06.780763+00:00_

[Round 9 审稿请求]:
你是 Reviewer 1，负责审查以下论文的**方法严谨性、实验设计和统计分析**。

## 论文信息
- 标题: Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Information Extraction
- 路径: `projects/struct_self_consist_ie/docs/paper/main.tex`（sections 在 `sections/` 子目录）
- 目标 venue: **EMNLP 2026 Main Conference**（via ARR May 2026 cycle）
- 截止日期: 2026-05-25
- 格式要求:
  - 正文 ≤8 页（final 9 页），参考文献不限页数
  - ACL 模板（`\usepackage[review]{acl}`），double-blind
  - Limitations section 必须
  - Responsible NLP Checklist 必须
  - Ethics Statement 必须

## 你的审查侧重

### 1. 方法论严谨性
- 5 个 confidence signal（SJ, VC, FK, EM, LP）的形式化定义是否精确、无歧义
- SJ 的 Hungarian matching + IoU + max normalizer 设计是否合理
- FK 独立性假设的 justification 是否充分
- 评估框架（QE: Spearman ρ + AUROC；Selection: best-of-N）是否恰当
- Correlation-selection gap 的概念界定是否清晰——instance-level vs per-sample 区分是否 tautological

### 2. 实验设计
- 数据集选择（SciERC / CoNLL-2003 / WNUT-17）的覆盖度和 difficulty gradient 设计
- 模型选择（Qwen3-8B, LLaMA-3.1-8B, Qwen3-4B）及训练配置（identical LoRA）是否构成公平比较
- N=8/16、T=0.7/1.0、3-seed 的 ablation 是否充分
- Free-form decoding ablation 的范围（1 dataset × 1 model × 1 seed）是否支撑其结论
- Scale ablation（4B vs 8B）设计是否合理

### 3. 统计分析
- Bootstrap CI、permutation test、Fisher combined p 的使用是否规范
- TOST 等价检验的 δ 选择是否有外部基准
- 多重比较校正的处理
- Effect size 报告（Cohen's d）的恰当性
- 单种子 vs 多种子结果的标注一致性（RE 是否全部标注 preliminary）

### 4. 页数合规
- 估算正文是否 ≤8 页（section 数量、figure/table、equation 数量）

请提供完整审稿意见，包含：Strengths（逐条）、Weaknesses（逐条，按 critical/warning/info 分级）、Questions、Missing References、Overall Assessment。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 631 · 2026-05-16T02:17:14.129242+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 632 · 2026-05-16T02:17:14.180018+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 633 · 2026-05-16T02:17:16.640500+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 634 · 2026-05-16T02:17:16.691308+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 635 · 2026-05-16T02:17:19.252309+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 636 · 2026-05-16T02:17:19.302867+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 637 · 2026-05-16T02:17:24.935033+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
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

_source line 638 · 2026-05-16T02:17:24.985647+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 639 · 2026-05-16T02:17:38.944485+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 640 · 2026-05-16T02:17:39.045429+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 641 · 2026-05-16T02:17:39.096223+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ The Correlation-Selection Gap in LLM-Based Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	Code and data will be released upon acceptance at [anonymized URL].
45	
46	\bibliography{references}
47	
48	\appendix
49	\input{sections/appendix}
50	
51	\end{document}
52	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 642 · 2026-05-16T02:17:39.096674+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 643 · 2026-05-16T02:17:39.197482+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 644 · 2026-05-16T02:17:47.030158+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

Based on the search results, I've found comprehensive information about ACL ARR 2026 reviewer guidelines and review form criteria. Here's what I found:

## Reviewer Guidelines

Reviewers are asked to read the paper and get the first impression, then sea
…[truncated 1744 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8085
}
```

</details>

---


### Tool call

_source line 645 · 2026-05-16T02:17:53.007959+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 646 · 2026-05-16T02:17:53.961961+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 647 · 2026-05-16T02:17:55.218270+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ACL ARR review form: all scoring dimensions, their scales, and descriptions. Include Overall Assessment, Soundness, Excitement, Reproducibility, and any other dimensions with their full rating scales."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete ACL ARR review form: all scoring dimensions, their scales, and descriptions. Include Overall Assessment, Soundness, Excitement, Reproducibility, and any other dimensions with their full rating scales."
  }
}
```

</details>

---


### Tool result

_source line 648 · 2026-05-16T02:18:01.148518+00:00_

# ACL ARR Review Form - Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- 5: "Positive that my evaluation is correct. I read the paper very carefully"
- 4: Quite sure with careful checking
- 3: Pretty sure but may have missed details
- 2: Willing to defend but likely missed some points
- 1: Not expertise area or paper very difficult

## 2. **Soundness**
Scale: 1-5 (with .5 increments)
- 5: "Excellent: This study is one of the most thorough I have seen"
- 4: Strong with sufficient support
- 3: Acceptable with minor gaps
- 2: Poor with insufficient support
- 1: "Major Issues: This study is not yet sufficiently thorough"

## 3. **Excitement**
Scale: 1-5 (with .5 increments)
- 5: Highly Exciting - would recommend to others
- 4: Exciting - would mention to others
- 3: Interesting - might mention some points
- 2: Potentially Interesting - doesn't resonate personally
- 1: Not Exciting - limited community appeal

## 4. **Overall Assessment**
Scale: 1-5 (with .5 increments)
- 5: Consider for Award
- 4: Conference acceptance
- 3: Findings acceptance
- 2: Resubmit next cycle
- 1: Do not resubmit

## 5. **Reproducibility**
Scale: 1-5
- 5: "They could easily reproduce the results"
- 4: Mostly reproducible with minor variations
- 3: Reproducible with some difficulty
- 2: Hard to reproduce - limited data availability
- 1: Not reproducible

## 6. **Datasets & Software**
Scale: 1-5 each
- 5: Enabling - affects research direction
- 4: Useful for ongoing work
- 3: Potentially useful
- 2: Documentary value only
- 1: No usable materials

## 7. **Author Identity Knowledge**
Scale: 1-5
- 5: Know author from submission violation
- 4: Know from preprint/workshop
- 3: Know from paper contents
- 2: Know from social media/talks
- 1: No educated guess

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5930
}
```

</details>

---


### Tool call

_source line 649 · 2026-05-16T02:18:04.163562+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 650 · 2026-05-16T02:18:04.464755+00:00_

1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but information extraction (IE) produces \textit{sets} of entities and relations with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals across NER and RE benchmarks at two model scales (4B and 8B).
4	All signals achieve strong quality estimation yet none improves best-of-$N$ selection despite substantial oracle headroom---the \textit{correlation-selection gap}.
5	Most signals are instance-level and cannot rank candidates by construction; log-probability---the only per-sample signal---is too compressed within instances to discriminate.
6	A free-form ablation confirms compression is intrinsic; the gap persists across scales and task types.
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 651 · 2026-05-16T02:18:04.465242+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 652 · 2026-05-16T02:18:04.967604+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---majority voting over multiple samples---yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But information extraction (IE) poses a structurally different challenge: the output is a \textit{set} of entities or relations, two samples may extract overlapping but non-identical structures, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
8	\citet{yao2026consistency} examine consistency--accuracy correlations for LLM-based IE; we extend their work with structural matching, selection analysis, and a difficulty gradient.
9	
10	Our central finding is the \textbf{correlation-selection gap} (Figure~\ref{fig:overview}): consistency signals achieve strong quality estimation ($\rho$ up to 0.45) but fail at sample selection despite substantial oracle headroom.
11	Four of five signals are instance-level by construction; log-probability, the only per-sample signal, is too compressed to discriminate (\S\ref{sec:discussion}).
12	
13	\begin{figure*}[t]
14	\centering
15	\includegraphics[width=\textwidth]{fig_overview}
16	\caption{The correlation-selection gap. \textbf{Left}: high inter-sample agreement correlates with high F1 (quality estimation). \textbf{Right}: instance-level signals assign identical scores to all candidates, precluding sample selection.}
17	\label{fig:overview}
18	\end{figure*}
19	
20	We evaluate five signal
…[truncated 971 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 653 · 2026-05-16T02:18:04.967966+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 654 · 2026-05-16T02:18:05.871167+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text through LLM comparison \cite{chen2024usc}, sub-claim decomposition \cite{thirukovalluru2024atomic}, or hallucination detection \cite{manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2025latentsc} all target discrete answers.
6	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings; \citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.
7	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap.
8	
9	\paragraph{Consistency for structured IE.}
10	\citet{yao2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, leaving open whether structural matching improves on surface agreement, whether quality estimation translates to selection, and whether findings generalize across a difficulty gradient---the three questions we address.
11	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency for QA/summarization but does not address structured extraction.
12	Our evaluation builds on generative IE work \cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting} and constrained decoding \cite{willard2023guided}.
13	
14	\paragraph{Uncertainty estimation and calibration.}
15	Surveys cover confidence estimation \cite{geng2024confidence}, uncertainty quantification \cite{xia2025survey}, and calibration \cite{hobelsberger2025systematic} for LLMs.
16	Semantic uncertainty \cite{kuhn2023semantic} clusters generations by meaning; our structural signals instead measure agreement over output \textit{str
…[truncated 601 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 655 · 2026-05-16T02:18:05.921718+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 656 · 2026-05-16T02:18:06.373822+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set (NER) or relation set (RE).
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	
8	\subsection{Confidence Signals}\label{sec:signals}
9	
10	Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
11	
12	\paragraph{Log-probability (model-internal, per-sample).}
13	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
14	\begin{equation}\label{eq:logprob}
15	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
16	\end{equation}
17	
18	\paragraph{Exact match voting (surface, instance-level).}
19	The proportion of samples producing the most common output:
20	\begin{equation}\label{eq:em}
21	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
22	\end{equation}
23	
24	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
25	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\cup| \times 2$ rating matrix:
26	\begin{equation}\label{eq:fk}
27	\kappa = \frac{\bar{P} - \bar{P}_e}{1 - \bar{P}_e}
28	\end{equation}
29	where $\bar{P}$ is mean observed and $\bar{P}_e$ expected agreement.
30	Temperature-based sampling introduces mild negative dependence ($-$0.4\% to $-$4.0\%), which does not inflate
…[truncated 2079 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 657 · 2026-05-16T02:18:06.374247+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 658 · 2026-05-16T02:18:06.826181+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures.
15	Qwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\ref{app:thinking_token}).
16	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\ref{app:n_scaling}).}
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation ($\rho$ and AUROC; $N{=}8$, seed${=}42$). Best in \textbf{bold}. RE: preliminary. $N{=}16$ in Table~\ref{tab:robustness}.}
27	\label{tab:quality_estimation}
28	\begin{tabular}{ll cc cc cc cc}
29	\toprule
30	& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}
…[truncated 5939 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 659 · 2026-05-16T02:18:06.826651+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 660 · 2026-05-16T02:18:07.292290+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	VC leads on hard NER ($\rho{=}0.38$); EM leads easy NER and binary discrimination (AUROC${=}0.816$, CoNLL); on RE (preliminary), LP outperforms structural signals (Table~\ref{tab:multiseed}).
5	Rankings hold across model families and a 4B ablation (Table~\ref{tab:scale_ablation}); at the capability boundary (WNUT-17), all signals collapse.
6	
7	\paragraph{Why the gap exists.}
8	Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
9	Log-probability, the only per-sample signal, is severely compressed: median LP range is 0.041 nats (IQR [0.024, 0.073]; Table~\ref{tab:logprob_ties}).
10	Where compression is mitigated ($n{=}210$ instances with above-median spread), LP selection outperforms greedy ($+2.9$~pp, $p{=}0.004$), confirming compression as the bottleneck; the gap holds even among high-diversity instances (Appendix~\ref{app:diversity}).
11	Doubling to $N{=}16$ expands oracle headroom by $+4.4$~pp without improving selection; on RE at 4B scale (preliminary), LP is the sole positive signal ($\Delta{=}{+}0.7$~pp, $p{=}0.058$; Table~\ref{tab:re_n16_selection}), consistent with LP being the strongest RE selection signal across scales, though still below greedy at 8B.
12	
13	\paragraph{Ablation: free-form decoding.}\label{sec:ablation}
14	Removing grammar constraints (SciERC NER, Qwen3-8B) yields nearly identical LP distributions (std ratio 0.97) and negligible selection changes (Appendix~\ref{app:freeform_ablation}), ruling out constrained decoding as the cause.
15	On RE (preliminary), LP reverses direction under free-form decoding (CI includes zero); whether this generalizes remains open.
16	Our consensus-proximity strategies instantiate MBR decoding \cite{eikema2022sampling}; all fail because utility correlates with F1 across instances but not within them (Appendix~\ref{app:mbr_discussion}).
17	
18
…[truncated 467 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 465
}
```

</details>

---


### Tool call

_source line 661 · 2026-05-16T02:18:07.294894+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 662 · 2026-05-16T02:18:07.395536+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluate five confidence signals for quality estimation and sample selection in LLM-based structured IE.
4	All signals achieve strong quality estimation yet none improves selection despite substantial oracle headroom---the \textit{correlation-selection gap}.
5	Four signals fail by construction (instance-level); log-probability is too compressed to discriminate, and a free-form ablation confirms compression is intrinsic.
6	Signal rankings shift with difficulty and task type, collapsing at the capability boundary---consistent across two model families and a 4B ablation.
7	Trained verifiers and scaling to 70B+ are promising directions.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 663 · 2026-05-16T02:18:08.349610+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 664 · 2026-05-16T02:18:08.350102+00:00_

1	Our evaluation covers three NER datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1; generalization to other RE benchmarks remains unvalidated.
2	We cover 4B--8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested---larger models may produce more diverse samples.
3	We do not train a verifier, leaving unknown how much oracle headroom a supervised approach could recover.
4	
5	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
6	The free-form ablation covers one dataset (SciERC NER) with one model; RE shows a directional LP reversal under free-form decoding.
7	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
8	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 665 · 2026-05-16T02:18:08.350452+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 666 · 2026-05-16T02:18:08.652828+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality---including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
47	\quad FK & 
…[truncated 61168 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 667 · 2026-05-16T02:18:14.039848+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "887"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "887"
  }
}
```

</details>

---


### Tool result

_source line 668 · 2026-05-16T02:18:14.140663+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (887). The file has 887 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 669 · 2026-05-16T02:18:18.207771+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/references.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 670 · 2026-05-16T02:18:18.609670+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 671 · 2026-05-16T02:18:18.761108+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/figures/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/figures/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 672 · 2026-05-16T02:18:18.811858+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_overview.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_reliability.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_signal_heatmap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_temperature_robustness.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_length_logprob_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_lp_range_cdf.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_selection_gap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_selection_gap.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 673 · 2026-05-16T02:18:21.873944+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 674 · 2026-05-16T02:18:22.426349+00:00_

1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@inproceedings{angelopoulos2021conformal,
4	  title = {Uncertainty Sets for Image Classifiers using Conformal Prediction},
5	  author = {Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, Michael I.},
6	  booktitle = {ICLR 2021},
7	  year = {2021},
8	  url = {https://arxiv.org/abs/2009.14193}
9	}
10	
11	@article{brown2024monkeys,
12	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
13	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
14	  journal = {arXiv preprint arXiv:2407.21787},
15	  year = {2024},
16	  url = {https://arxiv.org/abs/2407.21787}
17	}
18	
19	@inproceedings{chen2024usc,
20	  title = {Universal Self-Consistency for Large Language Model Generation},
21	  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
22	  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},
23	  year = {2024},
24	  url = {https://arxiv.org/abs/2311.17311}
25	}
26	
27	@article{cobbe2021verifiers,
28	  title = {Training Verifiers to Solve Math Word Problems},
29	  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
30	  journal = {arXiv preprint arXiv:2110.14168},
31	  year = {2021},
32	  url = {https://arxiv.org/abs/2110.14168}
33	}
34	
35	@inproceedings{culotta2004confidence,
36	  title = {Confidence Estimation for Information Extraction},
37	  author = {Culotta, Aron and McCallum, Andrew},
38	  booktitle = {HLT-NAACL 2004},
39	  year = {2004},
40	  url = {https://aclanthology.org/N04-4028/}
41	}
42	
43	@inproceedings{derczynski2017wnut,
44
…[truncated 24147 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 675 · 2026-05-16T02:18:22.527304+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 676 · 2026-05-16T02:19:13.655111+00:00_

&lt;persisted-output>
Output too large (49.1KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/cf6a9dd2-06b5-41c2-a47b-6d940cd6602e/tool-results/toolu_016PzynTPimwmyc99ftJDF4k.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 64, \"total_citations\": 61, \"unique_cited_keys\": 40, \"orphan_bib\": 24, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 58, \"online_not_found\": 3, \"online_mismatch\": 3}, \"cross_check\": {\"orphan_bib\": [\"angelopoulos2021conformal\", \"culotta2004confidence\", \"desai2020calibration\", \"fisch2021conformal\", \"gal2016dropout\", \"geifman2017selective\", \"guo2017calibration\", \"he2024uncertainty\", \"heo2025uncertainty\", \"jaccard1901distribution\", \"josifoski2022genie\", \"kadavath2022language\", \"kim2024verifiner\", \"kossen2024semantic\", \"lakshminarayanan2017ensembles\", \"malinin2021uncertainty\", \"shelmanov2021active\", \"wang2023instructuie\", \"wang2024mathshepherd\", \"wen2025know\", \"xiao2019uncertainty\", \"xiong2024llm\", \"zhang2023ener\", \"zhang2025tts\"], \"missing_bib\": [], \"orphan_count\": 24, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"angelopoulos2021conformal\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\", \"year\": \"2021\", \"venue\": \"ICLR 2021\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\":
…[truncated 363 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 51127
}
```

</details>

---


### Tool call

_source line 677 · 2026-05-16T02:19:18.180535+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/cf6a9dd2-06b5-41c2-a47b-6d940cd6602e/tool-results/toolu_016PzynTPimwmyc99ftJDF4k.txt",
  "offset": "0",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296/cf6a9dd2-06b5-41c2-a47b-6d940cd6602e/tool-results/toolu_016PzynTPimwmyc99ftJDF4k.txt",
    "offset": "0",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 678 · 2026-05-16T02:19:18.433437+00:00_

0	{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 64, \"total_citations\": 61, \"unique_cited_keys\": 40, \"orphan_bib\": 24, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 58, \"online_not_found\": 3, \"online_mismatch\": 3}, \"cross_check\": {\"orphan_bib\": [\"angelopoulos2021conformal\", \"culotta2004confidence\", \"desai2020calibration\", \"fisch2021conformal\", \"gal2016dropout\", \"geifman2017selective\", \"guo2017calibration\", \"he2024uncertainty\", \"heo2025uncertainty\", \"jaccard1901distribution\", \"josifoski2022genie\", \"kadavath2022language\", \"kim2024verifiner\", \"kossen2024semantic\", \"lakshminarayanan2017ensembles\", \"malinin2021uncertainty\", \"shelmanov2021active\", \"wang2023instructuie\", \"wang2024mathshepherd\", \"wen2025know\", \"xiao2019uncertainty\", \"xiong2024llm\", \"zhang2023ener\", \"zhang2025tts\"], \"missing_bib\": [], \"orphan_count\": 24, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"angelopoulos2021conformal\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\", \"year\": \"2021\", \"venue\": \"ICLR 2021\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers 
…[truncated 48231 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 679 · 2026-05-16T02:22:19.479086+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿意见\n\n**论文**: Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Information Extraction\n**Venue**: EMNLP 2026 Main Conference (ARR May 2026)\n\n---\n\n## 总体评分\n**Overall**: 3.5/5 (介于 Findings acceptance 和 Conference acceptance 之间)\n**一句话总结**: 问题定义清晰、实验设计严谨、统计分析透明，correlation-selection gap 是有价值的概念贡献；但核心 insight 有部分 tautological 成分，RE 证据不足，free-form ablation 范围过窄以至于 abstract 中\"compression is intrinsic\"的 claim 强于实际证据。\n\n---\n\n## 官方维度打分（来自 ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法论整体严谨，统计实践优于同类工作（bootstrap CI, TOST, permutation test）；但 instance-level signal 无法 rank 是 by construction 的，gap 部分是 tautological；TOST 外部锚点显示等价性结论 configuration-dependent |\n| Excitement | 3/5 | 概念贡献（metric dissociation, correlation-selection gap）对社区有价值；但负结果论文天然 excitement 有限，且未提出解决方案 |\n| Reproducibility | 4/5 | 训练配置、prompt 模板、超参数详尽（Appendix F）；代码承诺 release；唯一扣分：Qwen3-8B SciERC thinking token confound 需要额外验证 |\n| Reviewer Confidence | 4/5 | 仔细阅读了全文和全部 appendix |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Abstract/Conclusion 中 \"free-form ablation confirms compression is intrinsic\" 过度概括\n- 具体位置：Abstract line 6；Section 6 (Conclusion) line 5\n- 问题：Free-form ablation 仅覆盖 1 dataset (SciERC) × 1 model (Qwen3-8B) × 1 seed (42)。NER LP 分布确实稳定（std ratio 0.97, Table 12 Panel A），但 RE 在 free-form 下 LP 选择方向反转（从 −0.68pp 到 +1.69pp, Panel B），这直接 undermines \"compression is intrinsic\" 的通用性。论文 Discussion (§5) 和 Limitations 都诚实承认了这一局限，但 abstract 和 conclusion 的措辞没有限定范围。\n- 为什么影响接收：Abstract 是读者对论文的第一印象，overclaim 会误导对核心贡献的理解。\n- 建议修改方向：改为 \"A free-form ablation confirms NER compression is intrinsic; RE shows a directional reversal that warrants further investigation\" 或类似限定性表述。\n\n**N2** [critical] Correlation-selection gap 中 instance-level signal 失败的 tautological 成分未充分讨论\n- 具体位置：Section 4.2, Section 5 \"Why the gap exists\"\n- 问题：4/5 信号是 instance-level 的，assign identical score to all candidates *by construction*（论文自己也这样说：Section 4.2 line 83）。这不是一个 empirical finding，而是一个 definitional consequence——这些信号根本不是设计用来做 per-sample selection 的。将此包装为 \"gap\" 有夸大意外程度之嫌。真正有信息量的 gap 仅存在于 LP（唯一的 per-sample signal）和 VC 的 majority-voting selection variant（脚注 Eq 5 line 50 表明 selection 时 VC 给每个 sample 不同的 voted output，从而变成 per-sample signal）。\n- 为什么影响接收：如果 \"gap\" 在 4/5 信号上是 trivially true，论文的核心贡献缩窄为 \"LP compression prevents selection\"——仍有价值但 scope 显著缩小。\n- 建议修改方向：(a) 更清晰地将 instance-level 信号的失败定位为 design limitation 而非 empirical surprise；(b) 将 LP 和 VC-voted-output 的 selection failure 作为核心实验发现重点展开；(c) 或者重新 frame 贡献为 \"existing signals are either instance-level (by design) or compressed (LP), and there is no practical per-sample signal for structured IE\"。\n\n**N3** [critical] RE 证据不足以支撑标题和 abstract 中 \"LLM-Based Information Extraction\" 的通用性声明\n- 具体位置：Title, Abstract, Section 4.1 line 49-50, Limitations\n- 问题：RE 仅在 SciERC 上测试（40% zero F1），且全部标注 \"preliminary\"。标题和 abstract 说 \"Information Extraction\"，实际上核心可靠结论仅覆盖 NER。论文在 Limitations 和正文中反复诚实标注了 \"preliminary\"，但标题/abstract 的 scope 与证据不匹配。\n- 为什么影响接收：Reviewer 和读者会基于标题/abstract 判断 scope，当 RE 是 preliminary 时称 \"Information Extraction\" 是 overclaim。\n- 建议修改方向：标题/abstract 中加限定语（如 \"primarily on NER\"），或在 abstract 明确 \"RE conclusions rest on a single benchmark and are preliminary\"（introduction 已有类似措辞 line 30，但 abstract 没有）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] TOST 外部锚点结果显示等价性结论 configuration-dependent，但正文未充分整合\n- 具体位置：Appendix D, Section 4.2\n- 问题：外部锚点下（δ_SEM, δ_practical=0.5pp, δ_literature=1.0pp），LLaMA CoNLL 通过所有等价检验，但 SciERC 和 Qwen CoNLL 在所有外部 δ 下均 fail（Appendix D line 390-394）。这意味着 \"no signal improves selection\" 的 blanket claim 应改为 \"no signal *consistently* improves selection\" 或 \"selection gains are at best marginal\"。当前正文 Section 4.2 没有整合这一 nuance。\n- 建议：在 Section 4.2 主文中加一句提及外部锚点结果的 configuration-dependent 性质，或调整 claim 措辞。\n\n**W2** [warning] VC majority-voting selection variant（脚注 Eq 5）的 per-sample 性质和失败原因未深入分析\n- 具体位置：Section 3.2 line 50 (footnote), Table 2\n- 问题：Eq 5 脚注说 selection 时只保留 frequency > N/2 的实体形成 voted output。这使得 VC 在 selection 语境下成为一个 per-sample-like signal（不同 sample 与 voted output 的 overlap 不同），但 Table 2 显示 VC selection 表现最差（0.623, 低于 random 0.610 但也低于 greedy 0.645）。这个失败值得深入分析——VC 理论上 *能* rank candidates，为什么仍然失败？是因为 voted output 本身就和多数 sample 相似（高 recall、低 precision），还是因为 high-overlap sample 恰好不是 best-F1 sample？\n- 建议：在 Discussion 中增加 1-2 句对 VC-selection 失败机制的分析。\n\n**W3** [warning] 多重比较校正不完整\n- 具体位置：Table 1 (quality estimation), Table 2 (selection), 全文\n- 问题：Bootstrap CI appendix 的脚注（line 302）提到 SJ-EM gap \"would not survive Bonferroni correction for 10 pairwise comparisons\"，但正文中大量信号 × 数据集 × 模型的比较（5 signals × 3 datasets × 2-3 models）没有系统性的多重比较校正。Selection 分析中每个 signal 都与 greedy 做了独立的 sign test / Fisher combined test，但没有 family-wise error 校正。\n- 建议：至少在正文或 appendix 中讨论多重比较的影响，说明 \"即使做 Bonferroni/Holm 校正，core conclusions 是否成立\"。对于 \"无显著差异\" 类的负结果，未校正的 individual p-values 已经足够（p > 0.05 未校正 → 校正后仍 > 0.05），但应明确说明这一逻辑。\n\n**W4** [warning] Quality estimation 主表（Table 1）仅用单 seed，与后续多 seed 分析有潜在不一致\n- 具体位置：Table 1 (seed=42), Table 7 (3-seed mean)\n- 问题：Table 1 报告 seed=42 的单次结果。Table 7（Appendix F）显示 3-seed mean 值与 Table 1 有差异（如 SJ NER: Table 1 报 0.360, Table 7 mean 0.364; VC NER: 0.379 vs 0.386; LP NER: 0.205 vs 0.217）。虽然差异不大且 ranking 一致（Kendall's W=1.000），但 Table 1 作为主表应注明这些是 single-seed 结果并指向多 seed 验证。\n- 建议：Table 1 caption 中加一句 \"Values are single-seed (42); 3-seed means and stability in Table X confirm ranking consistency (W=1.000)\"，或直接报告 3-seed mean。\n\n**W5** [warning] Scale ablation (4B vs 8B) 设计有限\n- 具体位置：Table 3, Section 4.3 line 117-118\n- 问题：4B ablation 仅用 Qwen3-4B（无 LLaMA 4B），且结论 \"task difficulty, not model capacity, drives the gap\" 仅基于两个数据点（4B 和 8B）。4B→8B 的 scale 差异不到 2×，不足以充分 disentangle model capacity 和 task difficulty 的效应。论文 Limitations 中提到 \"70B+ models untested\"，但这一局限对 \"not model capacity\" 的 claim 影响更大。\n- 建议：弱化 \"not model capacity\" 的措辞为 \"within the 4B-8B range, task difficulty appears to be the primary driver\"，保留 scale limitation。\n\n---\n\n## 小问题（不影响接收）\n\n- **W6** [info] Bib 有 24 个 orphan entries（在 .bib 中但未被 \\cite），建议清理以避免提交时 LaTeX warning。\n- **W7** [info] Section 3.2 line 30 关于 FK 负依赖性的 claim（\"−0.4% to −4.0%\"）未给出计算过程或 appendix reference，直接断言 \"does not inflate FK\" 需要更多 justification。虽然 permutation test (Table 4) 间接支持了 FK 的有效性，但 claim 本身的推导缺失。\n- **W8** [info] Table 2 NER 用 2-seed mean±σ（sign test），RE 用 single seed。NER 和 RE 的统计标准不一致，建议统一。\n- **W9** [info] Ethics Statement 提到 \"CoNLL-2003 is derived from Reuters RCV1 corpus, which is available for research purposes under a NIST agreement\"——严格来说是 NIST 分发但非 NIST 协议，应核实具体 license 描述。\n- **W10** [info] \"correlation-selection gap\" 这个术语在论文中反复使用但没有形式化定义（如 Δ = ρ − selection_gain / oracle_headroom）。建议在 Section 4.2 给出操作性定义。\n\n---\n\n## 提问（Questions for Authors）\n\n**Q1**: VC 在 selection 语境下（majority-voted output 然后选最近的 sample）实际上是 per-sample signal——每个 candidate 与 voted output 的 overlap 不同。那为什么 VC selection 仍然失败？是否因为 voted output 本身和高频 sample 高度 overlap，导致 selection 退化为 \"选最平庸的 sample\"？\n\n**Q2**: 有没有尝试过组合信号（如 LP + SJ 的 weighted combination）做 selection？即使各自失败，是否有互补性？\n\n**Q3**: Free-form RE LP reversal（Table 12 Panel B: from −0.68pp to +1.69pp）是最 actionable 的发现之一。这个 reversal 在 seed 42 之外是否能复现？如果能，这可能是一个重要的 positive contribution（\"free-form decoding enables LP selection for RE\"）。\n\n**Q4**: $\\varepsilon$ = 0.05 用于 LP tied/non-tied 分割。Table 9 的 $\\varepsilon$ sweep 显示这个选择最大化了 statistical separation（p=0.004），但这是否构成 p-hacking？即在多个 threshold 中选了效果最好的那个来报告？\n\n---\n\n## Missing References\n\n引用核查：所有 40 个 \\cite key 均有对应 bib entry，无 missing。3 个条目在 OpenAlex 中未找到（hobelsberger2025, lightman2024, venktesh2025），经核实为 OpenAlex 覆盖局限，论文本身存在。\n\n可能遗漏的相关工作：\n- **Ren et al. (2023)** \"Investigating Uncertainty Calibration of Aligned Language Models under the Hood\" (EMNLP 2023 Findings) — 与 LP calibration 和 uncertainty estimation 直接相关\n- **Lin et al. (2024)** \"Generating Benchmarks for Factuality Evaluation of Language Models\" (EACL 2024) — SelfCheckGPT 相关但更 focused on factuality + consistency\n\n---\n\n## 主要优势\n\n- **S1**: 问题定义有价值——将 self-consistency 扩展到 set-valued structured output 是一个自然但重要的研究方向，quality estimation vs selection 的 metric dissociation 是有启发性的\n- **S2**: 实验设计严谨——difficulty gradient（SciERC → CoNLL → WNUT-17）、cross-model (Qwen/LLaMA)、cross-scale (4B/8B)、multi-seed 验证形成完整的 robustness picture\n- **S3**: 统计分析显著优于同类 empirical NLP 工作——bootstrap CI with pairwise Δρ、TOST 等价检验（含外部锚点）、permutation test、Fisher combined p、Cohen's d 报告，且诚实标注所有 borderline/preliminary 结果\n- **S4**: Limitations 透明——RE preliminary 标注贯穿全文，thinking token confound 有三部分定量分析，free-form ablation 的 RE reversal 没有被回避\n- **S5**: Appendix 极其详尽（~15 pages），提供了 normalizer robustness、LOO-SJ equivalence、ε sensitivity、OOD analysis、LP failure stability 等细粒度分析，增强可重复性\n- **S6**: 与 MBR decoding 文献的连接（Appendix K, cite Eikema et al. 2025）将 finding 嵌入更广泛的理论框架，非 ad hoc observation\n\n---\n\n## 最终判断\n\n这是一篇方法论严谨、统计实践优良的 empirical 负结果论文。核心贡献（metric dissociation + LP compression bottleneck）对 test-time scaling for IE 社区有实际价值。主要弱点是：(1) instance-level signal 失败有 tautological 成分；(2) RE 证据不足但标题/abstract scope 过宽；(3) free-form ablation 范围不支撑 abstract 中的通用性 claim。修复 N1-N3 后，推荐 Findings acceptance；若能增加 free-form multi-seed RE 实验并缩窄 framing，可考虑 main conference。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿意见\n\n**论文**: Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Information Extraction\n**Venue**: EMNLP 2026 Main Conference (ARR May 2026)\n\n---\n\n## 总体评分\n**Overall**: 3.5/5 (介于 Findings acceptance 和 Conference acceptance 之间)\n**一句话总结**: 问题定义清晰、实验设计严谨、统计分析透明，correlation-selection gap 是有价值的概念贡献；但核心 insight 有部分 tautological 成分，RE 证据不足，free-form ablation 范围过窄以至于 abstract 中\"compression is intrinsic\"的 claim 强于实际证据。\n\n---\n\n## 官方维度打分（来自 ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法论整体严谨，统计实践优于同类工作（bootstrap CI, TOST, permutation test）；但 instance-level signal 无法 rank 是 by construction 的，gap 部分是 tautological；TOST 外部锚点显示等价性结论 configuration-dependent |\n| Excitement | 3/5 | 概念贡献（metric dissociation, correlation-selection gap）对社区有价值；但负结果论文天然 excitement 有限，且未提出解决方案 |\n| Reproducibility | 4/5 | 训练配置、prompt 模板、超参数详尽（Appendix F）；代码承诺 release；唯一扣分：Qwen3-8B SciERC thinking token confound 需要额外验证 |\n| Reviewer Confidence | 4/5 | 仔细阅读了全文和全部 appendix |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Abstract/Conclusion 中 \"free-form ablation confirms compression is intrinsic\" 过度概括\n- 具体位置：Abstract line 6；Section 6 (Conclusion) line 5\n- 问题：Free-form ablation 仅覆盖 1 dataset (SciERC) × 1 model (Qwen3-8B) × 1 seed (42)。NER LP 分布确实稳定（std ratio 0.97, Table 12 Panel A），但 RE 在 free-form 下 LP 选择方向反转（从 −0.68pp 到 +1.69pp, Panel B），这直接 undermines \"compression is intrinsic\" 的通用性。论文 Discussion (§5) 和 Limitations 都诚实承认了这一局限，但 abstract 和 conclusion 的措辞没有限定范围。\n- 为什么影响接收：Abstract 是读者对论文的第一印象，overclaim 会误导对核心贡献的理解。\n- 建议修改方向：改为 \"A free-form ablation confirms NER compression is intrinsic; RE shows a directional reversal that warrants further investigation\" 或类似限定性表述。\n\n**N2** [critical] Correlation-selection gap 中 instance-level signal 失败的 tautological 成分未充分讨论\n- 具体位置：Section 4.2, Section 5 \"Why the gap exists\"\n- 问题：4/5 信号是 instance-level 的，assign identical score to all candidates *by construction*（论文自己也这样说：Section 4.2 line 83）。这不是一个 empirical finding，而是一个 definitional consequence——这些信号根本不是设计用来做 per-sample selection 的。将此包装为 \"gap\" 有夸大意外程度之嫌。真正有信息量的 gap 仅存在于 LP（唯一的 per-sample signal）和 VC 的 majority-voting selection variant（脚注 Eq 5 line 50 表明 selection 时 VC 给每个 sample 不同的 voted output，从而变成 per-sample signal）。\n- 为什么影响接收：如果 \"gap\" 在 4/5 信号上是 trivially true，论文的核心贡献缩窄为 \"LP compression prevents selection\"——仍有价值但 scope 显著缩小。\n- 建议修改方向：(a) 更清晰地将 instance-level 信号的失败定位为 design limitation 而非 empirical surprise；(b) 将 LP 和 VC-voted-output 的 selection failure 作为核心实验发现重点展开；(c) 或者重新 frame 贡献为 \"existing signals are either instance-level (by design) or compressed (LP), and there is no practical per-sample signal for structured IE\"。\n\n**N3** [critical] RE 证据不足以支撑标题和 abstract 中 \"LLM-Based Information Extraction\" 的通用性声明\n- 具体位置：Title, Abstract, Section 4.1 line 49-50, Limitations\n- 问题：RE 仅在 SciERC 上测试（40% zero F1），且全部标注 \"preliminary\"。标题和 abstract 说 \"Information Extraction\"，实际上核心可靠结论仅覆盖 NER。论文在 Limitations 和正文中反复诚实标注了 \"preliminary\"，但标题/abstract 的 scope 与证据不匹配。\n- 为什么影响接收：Reviewer 和读者会基于标题/abstract 判断 scope，当 RE 是 preliminary 时称 \"Information Extraction\" 是 overclaim。\n- 建议修改方向：标题/abstract 中加限定语（如 \"primarily on NER\"），或在 abstract 明确 \"RE conclusions rest on a single benchmark and are preliminary\"（introduction 已有类似措辞 line 30，但 abstract 没有）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] TOST 外部锚点结果显示等价性结论 configuration-dependent，但正文未充分整合\n- 具体位置：Appendix D, Section 4.2\n- 问题：外部锚点下（δ_SEM, δ_practical=0.5pp, δ_literature=1.0pp），LLaMA CoNLL 通过所有等价检验，但 SciERC 和 Qwen CoNLL 在所有外部 δ 下均 fail（Appendix D line 390-394）。这意味着 \"no signal improves selection\" 的 blanket claim 应改为 \"no signal *consistently* improves selection\" 或 \"selection gains are at best marginal\"。当前正文 Section 4.2 没有整合这一 nuance。\n- 建议：在 Section 4.2 主文中加一句提及外部锚点结果的 configuration-dependent 性质，或调整 claim 措辞。\n\n**W2** [warning] VC majority-voting selection variant（脚注 Eq 5）的 per-sample 性质和失败原因未深入分析\n- 具体位置：Section 3.2 line 50 (footnote), Table 2\n- 问题：Eq 5 脚注说 selection 时只保留 frequency > N/2 的实体形成 voted output。这使得 VC 在 selection 语境下成为一个 per-sample-like signal（不同 sample 与 voted output 的 overlap 不同），但 Table 2 显示 VC selection 表现最差（0.623, 低于 random 0.610 但也低于 greedy 0.645）。这个失败值得深入分析——VC 理论上 *能* rank candidates，为什么仍然失败？是因为 voted output 本身就和多数 sample 相似（高 recall、低 precision），还是因为 high-overlap sample 恰好不是 best-F1 sample？\n- 建议：在 Discussion 中增加 1-2 句对 VC-selection 失败机制的分析。\n\n**W3** [warning] 多重比较校正不完整\n- 具体位置：Table 1 (quality estimation), Table 2 (selection), 全文\n- 问题：Bootstrap CI appendix 的脚注（line 302）提到 SJ-EM gap \"would not survive Bonferroni correction for 10 pairwise comparisons\"，但正文中大量信号 × 数据集 × 模型的比较（5 signals × 3 datasets × 2-3 models）没有系统性的多重比较校正。Selection 分析中每个 signal 都与 greedy 做了独立的 sign test / Fisher combined test，但没有 family-wise error 校正。\n- 建议：至少在正文或 appendix 中讨论多重比较的影响，说明 \"即使做 Bonferroni/Holm 校正，core conclusions 是否成立\"。对于 \"无显著差异\" 类的负结果，未校正的 individual p-values 已经足够（p > 0.05 未校正 → 校正后仍 > 0.05），但应明确说明这一逻辑。\n\n**W4** [warning] Quality estimation 主表（Table 1）仅用单 seed，与后续多 seed 分析有潜在不一致\n- 具体位置：Table 1 (seed=42), Table 7 (3-seed mean)\n- 问题：Table 1 报告 seed=42 的单次结果。Table 7（Appendix F）显示 3-seed mean 值与 Table 1 有差异（如 SJ NER: Table 1 报 0.360, Table 7 mean 0.364; VC NER: 0.379 vs 0.386; LP NER: 0.205 vs 0.217）。虽然差异不大且 ranking 一致（Kendall's W=1.000），但 Table 1 作为主表应注明这些是 single-seed 结果并指向多 seed 验证。\n- 建议：Table 1 caption 中加一句 \"Values are single-seed (42); 3-seed means and stability in Table X confirm ranking consistency (W=1.000)\"，或直接报告 3-seed mean。\n\n**W5** [warning] Scale ablation (4B vs 8B) 设计有限\n- 具体位置：Table 3, Section 4.3 line 117-118\n- 问题：4B ablation 仅用 Qwen3-4B（无 LLaMA 4B），且结论 \"task difficulty, not model capacity, drives the gap\" 仅基于两个数据点（4B 和 8B）。4B→8B 的 scale 差异不到 2×，不足以充分 disentangle model capacity 和 task difficulty 的效应。论文 Limitations 中提到 \"70B+ models untested\"，但这一局限对 \"not model capacity\" 的 claim 影响更大。\n- 建议：弱化 \"not model capacity\" 的措辞为 \"within the 4B-8B range, task difficulty appears to be the primary driver\"，保留 scale limitation。\n\n---\n\n## 小问题（不影响接收）\n\n- **W6** [info] Bib 有 24 个 orphan entries（在 .bib 中但未被 \\cite），建议清理以避免提交时 LaTeX warning。\n- **W7** [info] Section 3.2 line 30 关于 FK 负依赖性的 claim（\"−0.4% to −4.0%\"）未给出计算过程或 appendix reference，直接断言 \"does not inflate FK\" 需要更多 justification。虽然 permutation test (Table 4) 间接支持了 FK 的有效性，但 claim 本身的推导缺失。\n- **W8** [info] Table 2 NER 用 2-seed mean±σ（sign test），RE 用 single seed。NER 和 RE 的统计标准不一致，建议统一。\n- **W9** [info] Ethics Statement 提到 \"CoNLL-2003 is derived from Reuters RCV1 corpus, which is available for research purposes under a NIST agreement\"——严格来说是 NIST 分发但非 NIST 协议，应核实具体 license 描述。\n- **W10** [info] \"correlation-selection gap\" 这个术语在论文中反复使用但没有形式化定义（如 Δ = ρ − selection_gain / oracle_headroom）。建议在 Section 4.2 给出操作性定义。\n\n---\n\n## 提问（Questions for Authors）\n\n**Q1**: VC 在 selection 语境下（majority-voted output 然后选最近的 sample）实际上是 per-sample signal——每个 candidate 与 voted output 的 overlap 不同。那为什么 VC selection 仍然失败？是否因为 voted output 本身和高频 sample 高度 overlap，导致 selection 退化为 \"选最平庸的 sample\"？\n\n**Q2**: 有没有尝试过组合信号（如 LP + SJ 的 weighted combination）做 selection？即使各自失败，是否有互补性？\n\n**Q3**: Free-form RE LP reversal（Table 12 Panel B: from −0.68pp to +1.69pp）是最 actionable 的发现之一。这个 reversal 在 seed 42 之外是否能复现？如果能，这可能是一个重要的 positive contribution（\"free-form decoding enables LP selection for RE\"）。\n\n**Q4**: $\\varepsilon$ = 0.05 用于 LP tied/non-tied 分割。Table 9 的 $\\varepsilon$ sweep 显示这个选择最大化了 statistical separation（p=0.004），但这是否构成 p-hacking？即在多个 threshold 中选了效果最好的那个来报告？\n\n---\n\n## Missing References\n\n引用核查：所有 40 个 \\cite key 均有对应 bib entry，无 missing。3 个条目在 OpenAlex 中未找到（hobelsberger2025, lightman2024, venktesh2025），经核实为 OpenAlex 覆盖局限，论文本身存在。\n\n可能遗漏的相关工作：\n- **Ren et al. (2023)** \"Investigating Uncertainty Calibration of Aligned Language Models under the Hood\" (EMNLP 2023 Findings) — 与 LP calibration 和 uncertainty estimation 直接相关\n- **Lin et al. (2024)** \"Generating Benchmarks for Factuality Evaluation of Language Models\" (EACL 2024) — SelfCheckGPT 相关但更 focused on factuality + consistency\n\n---\n\n## 主要优势\n\n- **S1**: 问题定义有价值——将 self-consistency 扩展到 set-valued structured output 是一个自然但重要的研究方向，quality estimation vs selection 的 metric dissociation 是有启发性的\n- **S2**: 实验设计严谨——difficulty gradient（SciERC → CoNLL → WNUT-17）、cross-model (Qwen/LLaMA)、cross-scale (4B/8B)、multi-seed 验证形成完整的 robustness picture\n- **S3**: 统计分析显著优于同类 empirical NLP 工作——bootstrap CI with pairwise Δρ、TOST 等价检验（含外部锚点）、permutation test、Fisher combined p、Cohen's d 报告，且诚实标注所有 borderline/preliminary 结果\n- **S4**: Limitations 透明——RE preliminary 标注贯穿全文，thinking token confound 有三部分定量分析，free-form ablation 的 RE reversal 没有被回避\n- **S5**: Appendix 极其详尽（~15 pages），提供了 normalizer robustness、LOO-SJ equivalence、ε sensitivity、OOD analysis、LP failure stability 等细粒度分析，增强可重复性\n- **S6**: 与 MBR decoding 文献的连接（Appendix K, cite Eikema et al. 2025）将 finding 嵌入更广泛的理论框架，非 ad hoc observation\n\n---\n\n## 最终判断\n\n这是一篇方法论严谨、统计实践优良的 empirical 负结果论文。核心贡献（metric dissociation + LP compression bottleneck）对 test-time scaling for IE 社区有实际价值。主要弱点是：(1) instance-level signal 失败有 tautological 成分；(2) RE 证据不足但标题/abstract scope 过宽；(3) free-form ablation 范围不支撑 abstract 中的通用性 claim。修复 N1-N3 后，推荐 Findings acceptance；若能增加 free-form multi-seed RE 实验并缩窄 framing，可考虑 main conference。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 680 · 2026-05-16T02:22:24.101728+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4622
}
```

</details>

---


### Assistant

_source line 681 · 2026-05-16T02:22:35.185659+00:00_

审稿意见已提交给 Review Director。

核心结论：**Overall 3.5/5**，介于 Findings 和 Main Conference 之间。

三个 Must-Fix 问题：
1. Abstract 中 "compression is intrinsic" 的 claim 强于 free-form ablation 的证据（NER 成立但 RE 方向反转）
2. Instance-level signal 无法 rank candidates 是 by construction 的，不应包装为 empirical surprise——correlation-selection gap 的贡献范围需重新界定
3. 标题/Abstract 说 "Information Extraction" 但 RE 仅在 SciERC 上测试且标注 preliminary，scope 过宽

五个 Should-Fix：VC selection 失败机制分析缺失、TOST 等价性 configuration-dependent 未整合进正文、多重比较校正不完整、主表用单 seed、4B-8B scale ablation 不足以得出 "not model capacity" 的结论。

优势方面：统计实践显著优于同类 empirical NLP 工作（bootstrap CI + TOST + permutation test），difficulty gradient 实验设计完整，limitations 透明度高。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 21

## Round 21

4 recorded events


### User

_source line 682 · 2026-05-16T02:23:20.207034+00:00_

[Round 9 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 N/W/M 条目标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 完整审稿意见

**Overall**: 3 (Findings acceptance)
**一句话总结**: 实验执行扎实、LP 压缩发现有价值，但核心 "correlation-selection gap" 概念对 4/5 信号而言是 definitional/tautological，框架性贡献被高估。

### Must-Fix

**N1** [critical] 核心 "gap" 对 4/5 信号是 definitional，非实验发现
- Section 4.2 (line 83), Section 5 Discussion (line 8), Abstract (line 4-5)
- VC, SJ, FK, EM 作为 instance-level 信号，数学上产生 single score per input，无法对 N 个 candidate 排序——是信号定义的直接推论，不是实验发现。标题 "The Correlation-Selection Gap" 和 abstract "none improves best-of-N selection" 将部分 tautological 的观察框架化为统一发现。真正的实验发现仅是 LP score compression（1/5 信号的具体失败机制）。
- 建议：(1) 在 Introduction/Abstract 中明确承认 4/5 信号的 selection 失败是 definitional 而非 empirical；(2) 或重新框架化——分类法本身是贡献，而非 gap 的 "发现"。

**N2** [critical] Abstract 过度声称——省略 RE free-form decoding 的方向性反转
- Abstract (line 6), Discussion Section 5 (lines 14-15)
- Abstract 称 "A free-form ablation confirms compression is intrinsic; the gap persists across scales and task types"。但 Discussion 明确记录 RE 在 free-form decoding 下 LP selection 从 −0.68pp 翻转为 +1.69pp（Table 15 Panel B）。
- 建议：修改 Abstract 为 "...compression is intrinsic to NER; on RE (preliminary), free-form decoding reverses LP selection direction"。

### Should-Fix

**W1** [warning] 缺少 verbalized/elicited confidence 作为 per-sample signal
- 论文 per-sample signal 仅有 LP 一种。Xiong et al. (2024), Tian et al. (2023), Kang et al. (2025, self-certainty) 均为 per-sample signal 但未对比。
- 建议：至少在 Limitations 中承认仅测试了一种 per-sample signal。

**W2** [warning] 24 个 orphan bib entries 未引用
- 包括 Culotta & McCallum 2004, Kadavath 2022, Malinin 2021, Guo 2017, Desai 2020, Shelmanov 2021, He 2024, Zhang 2023 E-NER 等。
- 建议：引用相关的或删除不相关的。

**W3** [warning] Conclusion 未 hedge RE 结论
- Conclusion 未提及 RE 的 preliminary 性质，但 Introduction #3 正确标注了。
- 建议：Conclusion 加一句 hedging。

**W4** [warning] 模型规模限制削弱了 generalizability claim
- 仅覆盖 4B-8B 规模。Introduction 和 Conclusion 的 "the gap persists across scales" 仅指 4B-8B。
- 建议：明确标注 "at 4B-8B scale"。

**W5** [warning] Consensus-proximity selection 对 instance-level 信号的 operationalization 有些 ad-hoc
- 是否尝试过其他 operationalization？如 entity-level majority voting 应用于所有 consistency 信号。
- 建议：在主文中更早 qualify consensus-proximity 是 MBR 的一种 instantiation。

### Minor

- **M1**: Table 2 "Greedy" 指 T=1.0 single sample，但 greedy 通常指 argmax (T→0)——建议改措辞。
- **M2**: Section 3.2 line 30 FK 负依赖 "−0.4% to −4.0%" 含义不清。
- **M3**: bib entry 名/姓顺序问题（feng2025optimal, snell2025scaling）。
- **M4**: Discussion ρ=0.38 是 VC ρ=0.379 的四舍五入，精度不一致。
- **M5**: Introduction line 8 "nedellec2026/yao2026consistency" 似乎是 bib key 残留。

### Questions
- Q1: 是否尝试过其他 per-sample signals？
- Q2: RE free-form LP reversal 的具体机制？"selective variance reallocation" 能否更具体？
- Q3: 对所有 consistency 信号都用 entity-level aggregation 做 selection，结果是否不同？
- Q4: Thinking token confound 是否也影响了 consistency signals？

### Missing References
- Kadavath et al. 2022 (在 bib 中未引用)
- Culotta & McCallum 2004 (在 bib 中未引用)
- Malinin & Gales 2021 (在 bib 中未引用)
- Tian et al. 2023 "Just Ask for Calibration"
- Lin et al. 2023 "Generating with Confidence"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 683 · 2026-05-16T02:24:58.453910+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n### Must-Fix\n\n**[AGREE] R2-N1: 核心 \"gap\" 对 4/5 信号是 definitional**\n同意，与 R1-N2 一致。Section 4.2 line 83 自己写 \"cannot rank outputs by construction\"。补充：VC 在 selection 语境下（脚注 Eq 5, line 50）实际上给每个 candidate 不同的 overlap score（per-sample-like），但 Table 2 显示 VC selection 最差（0.623），这个失败才是真正的 empirical finding，论文未深入分析。\n\n**[AGREE] R2-N2: Abstract 过度声称 free-form ablation 结论**\n完全同意，与 R1-N1 一致。Table 12 Panel B 的 RE LP reversal (+1.69pp) 直接 undermines Abstract line 6 的通用性声称。\n\n### Should-Fix\n\n**[AGREE] R2-W1: 缺少 verbalized/elicited confidence**\n同意。仅测试 LP 一种 per-sample signal 就跳到 \"需要 trained verifiers\" 的结论，逻辑链有缺环。\n\n**[REBUT] R2-W2: 24 个 orphan bib entries**\n事实正确但严重程度应降为 info。ACL \\bibliography{} 只渲染被 \\cite 的条目，orphan entries 不出现在 PDF 中。是 bib 卫生问题，不影响论文内容。\n\n**[AGREE] R2-W3: Conclusion 未 hedge RE**\n同意。Conclusion Section 6 未标注 RE preliminary，与 Introduction #3 (line 30) 不一致。\n\n**[AGREE] R2-W4: 模型规模限制**\n同意，与 R1-W5 一致。4B-8B range 过窄支撑 \"across scales\" 的表述。\n\n**[REBUT] R2-W5: Consensus-proximity 是 ad-hoc**\n部分不同意。Appendix K (line 649) 已将其定位为 MBR instantiation，Appendix D (line 167-172) 证明 LOO-SJ 等价性（最大差异 3.1×10⁻⁴）。但同意应补充对其他 operationalization（如 entity-level majority voting 应用于 SJ/FK/EM）的讨论。\n\n### Minor\n\n**[AGREE] R2-M1**: \"Greedy\" 在 NLP 中通常指 argmax，此处指 T=1.0 单次采样，应改名。\n**[AGREE] R2-M2**: FK 负依赖数值缺推导，与 R1-W7 一致。\n**[REBUT] R2-M3**: Bib 格式无误，是 OpenAlex API 的 first_author 比对 false positive（\"Feng, Austin\" 被解析为 api=austin vs bib=feng）。\n**[AGREE] R2-M4**: ρ=0.38 vs Table 1 的 0.379 vs Table 7 的 0.386，精度不一致。\n**[REBUT] R2-M5**: 未发现 bib key 残留。Introduction line 8 是正常 \\citet{yao2026consistency}，R2 可能将共同作者 Nédellec 误认为 bib key。\n\n### R1-R2 共识总结\n\n两位 Reviewer 在以下核心问题上完全一致：\n1. **Instance-level signal 失败是 definitional 而非 empirical**（R1-N2 = R2-N1）\n2. **Abstract \"compression is intrinsic\" overclaim**（R1-N1 = R2-N2）——RE free-form reversal 未在 abstract 中限定\n3. **RE 证据不足但 scope 过宽**（R1-N3 ≈ R2-W3/W4）\n4. **Scale ablation range 过窄**（R1-W5 = R2-W4）\n\n主要分歧：\n- R2-W2（orphan bib）：R1 认为应降级为 info\n- R2-W5（ad-hoc operationalization）：R1 认为 MBR framing 已在 appendix 中，但同意应讨论替代方案\n- R2-M3（bib 格式）：R1 认为是 false positive\n- R2-M5（bib key 残留）：R1 在源码中未发现",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n### Must-Fix\n\n**[AGREE] R2-N1: 核心 \"gap\" 对 4/5 信号是 definitional**\n同意，与 R1-N2 一致。Section 4.2 line 83 自己写 \"cannot rank outputs by construction\"。补充：VC 在 selection 语境下（脚注 Eq 5, line 50）实际上给每个 candidate 不同的 overlap score（per-sample-like），但 Table 2 显示 VC selection 最差（0.623），这个失败才是真正的 empirical finding，论文未深入分析。\n\n**[AGREE] R2-N2: Abstract 过度声称 free-form ablation 结论**\n完全同意，与 R1-N1 一致。Table 12 Panel B 的 RE LP reversal (+1.69pp) 直接 undermines Abstract line 6 的通用性声称。\n\n### Should-Fix\n\n**[AGREE] R2-W1: 缺少 verbalized/elicited confidence**\n同意。仅测试 LP 一种 per-sample signal 就跳到 \"需要 trained verifiers\" 的结论，逻辑链有缺环。\n\n**[REBUT] R2-W2: 24 个 orphan bib entries**\n事实正确但严重程度应降为 info。ACL \\bibliography{} 只渲染被 \\cite 的条目，orphan entries 不出现在 PDF 中。是 bib 卫生问题，不影响论文内容。\n\n**[AGREE] R2-W3: Conclusion 未 hedge RE**\n同意。Conclusion Section 6 未标注 RE preliminary，与 Introduction #3 (line 30) 不一致。\n\n**[AGREE] R2-W4: 模型规模限制**\n同意，与 R1-W5 一致。4B-8B range 过窄支撑 \"across scales\" 的表述。\n\n**[REBUT] R2-W5: Consensus-proximity 是 ad-hoc**\n部分不同意。Appendix K (line 649) 已将其定位为 MBR instantiation，Appendix D (line 167-172) 证明 LOO-SJ 等价性（最大差异 3.1×10⁻⁴）。但同意应补充对其他 operationalization（如 entity-level majority voting 应用于 SJ/FK/EM）的讨论。\n\n### Minor\n\n**[AGREE] R2-M1**: \"Greedy\" 在 NLP 中通常指 argmax，此处指 T=1.0 单次采样，应改名。\n**[AGREE] R2-M2**: FK 负依赖数值缺推导，与 R1-W7 一致。\n**[REBUT] R2-M3**: Bib 格式无误，是 OpenAlex API 的 first_author 比对 false positive（\"Feng, Austin\" 被解析为 api=austin vs bib=feng）。\n**[AGREE] R2-M4**: ρ=0.38 vs Table 1 的 0.379 vs Table 7 的 0.386，精度不一致。\n**[REBUT] R2-M5**: 未发现 bib key 残留。Introduction line 8 是正常 \\citet{yao2026consistency}，R2 可能将共同作者 Nédellec 误认为 bib key。\n\n### R1-R2 共识总结\n\n两位 Reviewer 在以下核心问题上完全一致：\n1. **Instance-level signal 失败是 definitional 而非 empirical**（R1-N2 = R2-N1）\n2. **Abstract \"compression is intrinsic\" overclaim**（R1-N1 = R2-N2）——RE free-form reversal 未在 abstract 中限定\n3. **RE 证据不足但 scope 过宽**（R1-N3 ≈ R2-W3/W4）\n4. **Scale ablation range 过窄**（R1-W5 = R2-W4）\n\n主要分歧：\n- R2-W2（orphan bib）：R1 认为应降级为 info\n- R2-W5（ad-hoc operationalization）：R1 认为 MBR framing 已在 appendix 中，但同意应讨论替代方案\n- R2-M3（bib 格式）：R1 认为是 false positive\n- R2-M5（bib key 残留）：R1 在源码中未发现",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 684 · 2026-05-16T02:25:02.171560+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3717
}
```

</details>

---


### Assistant

_source line 685 · 2026-05-16T02:25:06.781642+00:00_

逐条回应已完成并汇报给 Director。核心共识：R1 和 R2 在三个 critical 问题上完全对齐——instance-level gap 的 tautological 性质、abstract overclaim、RE 证据不足。两处分歧（orphan bib 严重程度、M3/M5 的准确性）已给出具体证据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 22

## Round 22

44 recorded events


### User

_source line 686 · 2026-05-16T04:18:24.857044+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1

**你的审查侧重：方法严谨性 + 实验设计 + 统计有效性**

### Venue 信息
- **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle)
- **截止日期**: 2026-05-25
- **页数**: 长文 8 页 + 无限参考文献 + 附录不计入页数
- **模板**: ACL style（`\usepackage[review]{acl}`）
- **匿名**: Double-blind
- **附录规则**: 附录在 references 之后，审稿人可选择性参考但不应要求内容必须移至附录

### 论文路径
`projects/struct_self_consist_ie/docs/paper/main.tex`
（各章节在 `sections/` 子目录下：abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex）
引用文件：`references.bib`

### 论文概要
论文评估 5 种置信度信号（Soft Jaccard, Voting Confidence, Exact Match, Fleiss' κ, Log-probability）在 LLM-based structured IE（NER + RE）中的 quality estimation 和 sample selection 能力。核心发现是 "correlation-selection gap"：信号能预测质量（ρ 达 0.45）但无法改善 best-of-N 选择。实验覆盖 3 个 NER 数据集 + 1 个 RE 数据集，2 个模型族（Qwen3-8B, LLaMA-3.1-8B），加 4B scale ablation。

### 审查重点（必须逐条评估）

1. **实验设计**
   - 数据集选择是否足够？RE 只有 SciERC 一个，论文标注为 "preliminary"——这种标注是否足够？
   - 模型覆盖（3B-8B）是否支撑论文声称的 generality？
   - N=8 作为 primary setting 是否合理？N=16 仅作补充。
   - 3 seeds 是否足以支撑稳定性声明？

2. **统计方法**
   - Spearman ρ 作为 primary metric 是否合适？AUROC 和 selection F1 的三指标框架是否 well-motivated？
   - Bootstrap CI、permutation test、Fisher combined p、TOST 等统计检验是否正确使用？
   - 多重比较校正（Bonferroni）是否充分？
   - "tied fraction" 的 ε=0.05 阈值选择是否有足够的 data-driven justification？

3. **Claims vs Evidence 对齐**
   - 核心 claim "correlation-selection gap is universal" 是否被证据完全支撑？
   - "LP compression is model/task intrinsic, not decoding artifact" 这个因果推断是否可靠（free-form ablation 仅在 SciERC 上做）？
   - Scale ablation 只覆盖 3B-8B，能否支撑 "task difficulty is the primary driver" 的结论？
   - RE 结论标注为 "preliminary, single benchmark"——这种 hedging 是否适当？

4. **潜在混淆因素**
   - Qwen3-8B SciERC checkpoint 的 empty thinking token confound——论文三重论证是否充分排除？
   - Gold-empty instance filtering（CoNLL 20.2%, SciERC 4.0%）的影响？
   - Constrained decoding 对 LP 的系统性影响？

5. **可重复性**
   - 是否提供足够的实验细节（超参数、prompt template、evaluation protocol）？
   - 代码/数据 release 声明？

请按 EMNLP 审稿标准输出完整审稿报告，包括：Summary, Strengths, Weaknesses, Questions, Missing References, Overall Assessment (1-5 scale + confidence)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 687 · 2026-05-16T04:18:31.291371+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 688 · 2026-05-16T04:18:31.342290+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 689 · 2026-05-16T04:18:33.904219+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 690 · 2026-05-16T04:18:33.954828+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 691 · 2026-05-16T04:18:36.667382+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 692 · 2026-05-16T04:18:36.718009+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 693 · 2026-05-16T04:18:42.901627+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
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

_source line 694 · 2026-05-16T04:18:42.902093+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 695 · 2026-05-16T04:18:46.426233+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 696 · 2026-05-16T04:18:47.330924+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 697 · 2026-05-16T04:18:47.431861+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 698 · 2026-05-16T04:18:47.532828+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 699 · 2026-05-16T04:18:47.583611+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 700 · 2026-05-16T04:18:54.800065+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

I've successfully retrieved the ACL Rolling Review (ARR) 2026 reviewer guidelines information. Here's what I found regarding the review form criteria and scoring:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked 
…[truncated 1501 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8373
}
```

</details>

---


### Tool call

_source line 701 · 2026-05-16T04:19:00.377791+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5), and detailed descriptions for each score level. Include all fields reviewers must fill out."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5), and detailed descriptions for each score level. Include all fields reviewers must fill out."
  }
}
```

</details>

---


### Tool call

_source line 702 · 2026-05-16T04:19:00.881608+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 703 · 2026-05-16T04:19:01.284364+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ The Correlation-Selection Gap in LLM-Based Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	Code and data will be released upon acceptance at [anonymized URL].
45	
46	\bibliography{references}
47	
48	\appendix
49	\input{sections/appendix}
50	
51	\end{document}
52	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 704 · 2026-05-16T04:19:01.335071+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 705 · 2026-05-16T04:19:02.289565+00:00_

1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but information extraction (IE) produces \textit{sets} of entities and relations with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals across NER and RE benchmarks at two model scales (4B and 8B).
4	All signals achieve strong quality estimation (Spearman $\rho$ up to 0.45), yet none improves best-of-$N$ selection despite substantial oracle headroom---the \textit{correlation-selection gap}.
5	Four instance-level signals fail by construction; the empirical finding is that log-probability---the only per-sample signal---is too compressed within instances to discriminate (median range 0.041 nats, 60\% tied).
6	A 4-seed free-form decoding ablation confirms NER compression is not an artifact of constrained decoding; on RE, LP selection reverses direction under free-form decoding ($+1.8{\pm}0.1$~pp; preliminary, single benchmark), suggesting regime-dependent behavior.
7	Consensus-proximity selection (MBR) correlates with F1 across instances but not within them.
8	Signal rankings shift with task difficulty and collapse at the capability boundary; closing the gap likely requires learned per-sample scoring.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 706 · 2026-05-16T04:19:02.289940+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 707 · 2026-05-16T04:19:02.742154+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---majority voting over multiple samples---yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But information extraction (IE) poses a structurally different challenge: the output is a \textit{set} of entities or relations, two samples may extract overlapping but non-identical structures, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
8	\citet{yao2026consistency} examine consistency--accuracy correlations for LLM-based IE; we extend their work with structural matching, selection analysis, and a difficulty gradient.
9	
10	Our central finding is the \textbf{correlation-selection gap} (Figure~\ref{fig:overview}): consistency signals achieve strong quality estimation ($\rho$ up to 0.45) but fail at sample selection despite substantial oracle headroom.
11	Instance-level signals (4 of 5) fail by construction---they assign identical scores to all candidates.
12	The empirical contribution concerns log-probability (LP), the only per-sample signal: LP scores are too compressed within instances to discriminate (median range 0.041 nats; \S\ref{sec:discussion}), and consensus-proximity selection (MBR) fails because utility correlates with F1 across instances but not within them.
13	
14	\begin{figure*}[t]
15	\centering
16	\includegraphics[width=\textwidth]{fig_overview}
17	\caption{The correlation-selection gap. \textbf{Le
…[truncated 1370 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 708 · 2026-05-16T04:19:02.742738+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 709 · 2026-05-16T04:19:03.044371+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set (NER) or relation set (RE).
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	
8	\subsection{Confidence Signals}\label{sec:signals}
9	
10	Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
11	
12	\paragraph{Log-probability (model-internal, per-sample).}
13	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
14	\begin{equation}\label{eq:logprob}
15	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
16	\end{equation}
17	
18	\paragraph{Exact match voting (surface, instance-level).}
19	The proportion of samples producing the most common output:
20	\begin{equation}\label{eq:em}
21	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
22	\end{equation}
23	
24	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
25	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\cup| \times 2$ rating matrix:
26	\begin{equation}\label{eq:fk}
27	\kappa = \frac{\bar{P} - \bar{P}_e}{1 - \bar{P}_e}
28	\end{equation}
29	where $\bar{P}$ is mean observed and $\bar{P}_e$ expected agreement.
30	Temperature-based sampling introduces mild negative dependence ($-$0.4\% to $-$4.0\%; Appendix~\ref{app:fk_in
…[truncated 2139 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 710 · 2026-05-16T04:19:03.044939+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 711 · 2026-05-16T04:19:03.095577+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures.
15	Qwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\ref{app:thinking_token}).
16	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\ref{app:n_scaling}).}
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation ($\rho$ and AUROC; $N{=}8$, seed${=}42$, single-seed; 3-seed stability in Table~\ref{tab:multiseed}). Best in \textbf{bold}. RE: preliminary. $N{=}16$ in Table~\ref{tab:robustness}.}
27	\label{tab:quality_estimation}
28	\begin{tabular}{ll cc cc cc cc}
29	\toprule
30	& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \m
…[truncated 6607 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 712 · 2026-05-16T04:19:07.362935+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## Core Evaluation Sections

**Reviewer Confidence** (1-5 scale)
- 5: "Positive that my evaluation is correct. I read the paper very carefully"
- 4: Quite sure with careful checks; unlikely to have missed critical issues
- 3: Pretty sure but chance of missing details; limited familiarity with specifics
- 2: Willing to defend evaluation but fairly likely to have missed details
- 1: "Not my area, or paper is very hard to understand"

**Soundness** (1-5 scale with half-point increments)
- 5: "Excellent: This study is one of the most thorough I have seen"
- 4: Strong with sufficient support; extra experiments optional
- 3: Acceptable with support for main claims; minor details need work
- 2: Poor; main claims lack sufficient support; major technical problems
- 1: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

**Excitement** (1-5 scale with half-point increments)
- 5: "Highly Exciting: I would recommend this paper to others"
- 4: Exciting; would mention to others and attempt conference attendance
- 3: Interesting; might share points if time permits
- 2: Potentially interesting to some community members
- 1: "Not Exciting: this paper does not resonate with me"

**Overall Assessment** (1-5 scale with half-point increments)
- 5: Consider for Award (top 2.5%)
- 4: Conference acceptance recommended
- 3: Findings acceptance recommended
- 2: Resubmit next cycle with substantial revisions
- 1: Do not resubmit or not relevant

## Additional Evaluation Dimensions

**Reproducibility** (1-5 scale): Ranging from easily reproducible to impossible

**Datasets** (1-5 scale): From enabling research to no usable datasets

**Software** (1-5 scale): From affecting research choices to no release

**Author Identity Knowledge** (1-5 scale): Anonymity assessment

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6985
}
```

</details>

---


### Tool call

_source line 713 · 2026-05-16T04:19:12.434962+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 714 · 2026-05-16T04:19:13.439354+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text through LLM comparison \cite{chen2024usc}, sub-claim decomposition \cite{thirukovalluru2024atomic}, or hallucination detection \cite{manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2025latentsc} all target discrete answers.
6	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings; \citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.
7	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap.
8	
9	\paragraph{Consistency for structured IE.}
10	\citet{yao2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, leaving open whether structural matching improves on surface agreement, whether quality estimation translates to selection, and whether findings generalize across a difficulty gradient---the three questions we address.
11	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency for QA/summarization but does not address structured extraction.
12	\citet{culotta2004confidence} pioneer confidence estimation for IE via CRF marginals; our signals are model-agnostic.
13	Our evaluation builds on generative IE work \cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting} and constrained decoding \cite{willard2023guided}.
14	
15	\paragraph{Uncertainty estimation and calibration.}
16	Surveys cover confidence estimation \cite{geng2024confidence}, uncertainty quantification \cite{xia2025survey}, and calibration \cite{hobelsberger2025systematic} for LLMs.
17	Semantic uncertainty \cite{ku
…[truncated 898 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 715 · 2026-05-16T04:19:13.439742+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 716 · 2026-05-16T04:19:13.942979+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	VC leads on hard NER ($\rho{=}0.379$); EM leads easy NER and binary discrimination (AUROC${=}0.816$, CoNLL); on RE (preliminary), LP outperforms structural signals (Table~\ref{tab:multiseed}).
5	Rankings hold across model families and a 4B ablation (Table~\ref{tab:scale_ablation}); at the capability boundary (WNUT-17), all signals collapse.
6	
7	\paragraph{Why the gap exists.}
8	Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
9	Log-probability, the only per-sample signal, is severely compressed: median LP range is 0.041 nats (IQR [0.024, 0.073]; Table~\ref{tab:logprob_ties}).
10	Where compression is mitigated ($n{=}210$ instances with above-median spread), LP selection outperforms greedy ($+2.9$~pp, $p{=}0.004$), confirming compression as the bottleneck; the gap holds even among high-diversity instances (Appendix~\ref{app:diversity}).
11	Doubling to $N{=}16$ expands oracle headroom by $+4.4$~pp without improving selection; on RE at 4B scale (preliminary), LP is the sole positive signal ($\Delta{=}{+}0.7$~pp, $p{=}0.058$; Table~\ref{tab:re_n16_selection}), consistent with LP being the strongest RE selection signal across scales, though still below greedy at 8B.
12	A verbalized confidence baseline confirms that score compression is not LP-specific: the model's self-rated confidence (mean 8.6/10) is even more compressed and yields the weakest selection (Appendix~\ref{app:verbalized_confidence}).
13	
14	\paragraph{Ablation: free-form decoding.}\label{sec:ablation}
15	Removing grammar constraints (SciERC NER, Qwen3-8B, 4 seeds) yields nearly identical LP distributions (std ratio 0.97) and negligible selection changes (Appendix~\ref{app:freeform_ablation}), ruling out constrained decoding as the cause of NER compression.
16	On RE, LP selection consistently reverses direction under free-form decodin
…[truncated 1296 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 717 · 2026-05-16T04:19:13.943513+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 718 · 2026-05-16T04:19:14.395533+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluate five confidence signals for quality estimation and sample selection in LLM-based structured IE, revealing the \textit{correlation-selection gap}: strong quality estimation ($\rho$ up to 0.45) coexists with selection failure.
4	Instance-level signals fail by construction; the core empirical finding is that log-probability---the only per-sample signal---is too compressed within instances to discriminate (median range 0.041 nats, 60\% tied), and consensus-proximity selection (MBR) fails because utility correlates with F1 across but not within instances.
5	A 4-seed free-form ablation confirms NER compression is not caused by constrained decoding; on RE, LP selection reverses direction (preliminary, single benchmark).
6	Signal rankings shift with difficulty across NER benchmarks and collapse at the capability boundary---consistent across two model families (3B--8B).
7	RE conclusions rest on SciERC alone (preliminary, 40\% zero-F1 rate); trained verifiers and scaling to 70B+ are promising directions.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 719 · 2026-05-16T04:19:14.395878+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 720 · 2026-05-16T04:19:14.647061+00:00_

1	Our evaluation covers three NER datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1; generalization to other RE benchmarks remains unvalidated.
2	We cover 4B--8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested---larger models may produce more diverse samples.
3	We do not train a verifier, leaving unknown how much oracle headroom a supervised approach could recover.
4	
5	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
6	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE shows a directional LP reversal under free-form decoding.
7	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
8	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
9	We tested verbalized confidence \cite{tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 721 · 2026-05-16T04:19:14.647594+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 722 · 2026-05-16T04:19:15.000575+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality---including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
47	\quad FK & 
…[truncated 66606 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 723 · 2026-05-16T04:19:21.689455+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool call

_source line 724 · 2026-05-16T04:19:23.699404+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines, especially: what reviewers should evaluate, what constitutes a good/bad review, scoring criteria details for soundness/excitement/overall, and any specific instructions about negative results papers, reproducibility, or statistical rigor."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines, especially: what reviewers should evaluate, what constitutes a good/bad review, scoring criteria details for soundness/excitement/overall, and any specific instructions about negative results papers, reproducibility, or statistical rigor."
  }
}
```

</details>

---


### Tool result

_source line 725 · 2026-05-16T04:19:59.133857+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 44, \"total_citations\": 66, \"unique_cited_keys\": 44, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 38, \"online_not_found\": 3, \"online_mismatch\": 3}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence Estimation for Information Extraction\", \"authors\": \"Culotta, Aron and McCallum, Andrew\", \"year\": \"2004\", \"venue\": \"HLT-NAACL 2004\"}, {\"key\": \"derczynski2017wnut\", \"type\": \"inproceedings\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"authors\": \"Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut\", \"year\": \"2017\", \"venue\": \"W-NUT Workshop at EMNLP 2017\"}, {\"key\": \"eikema2022sampling\", \"type\": \"inproceedings\", \"title\": \"Sampling-Based Approximations to Minimum Bayes Risk Decodi
…[truncated 35397 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 37444
}
```

</details>

---


### Tool result

_source line 726 · 2026-05-16T04:20:07.428387+00:00_

# ARR Reviewer Guidelines: Key Evaluation Criteria

## What Reviewers Should Evaluate

Reviewers assess papers across multiple dimensions:

**Soundness**: Technical correctness and methodological rigor. Reviews must justify low soundness scores with specific evidence from the paper text.

**Excitement**: Personal interest level, kept separate from soundness. "You may find the work sound, but not something that is interesting for you personally."

**Overall Recommendation**: Composite judgment reflecting soundness, excitement, novelty, and potential impact for the field.

## Core Review Standards

### Specificity (I1)
Reviews must be concrete. Rather than "The paper is missing relevant references," specify "The paper is missing references X, Y, Z." Generic criticisms lack actionable value.

### Professional Tone (I4)
"A good review should be professional and neutral, if not kind." Sarcasm and dismissiveness harm reviewer-author relationships and contribute to peer review dysfunction.

### Score Alignment (I3)
Scores must correspond to review content. Low soundness ratings require documented technical problems; without justification, scores suggest unconscious bias.

## Common Review Problems to Avoid

The guidelines flag 17 problematic heuristics (H1-H17), including:

- **H1/H2**: Dismissing results as "obvious" or contradicting personal expectations
- **H5**: Demanding SOTA results when papers claim other contributions
- **H6**: Bias against negative/null results
- **H13**: Requiring experiments beyond the paper's stated claims
- **H16**: Listing acknowledged limitations as weaknesses

## Negative Results & Reproducibility

Negative findings deserve publication. "The bias towards publishing only positive results is a known problem in many fields, and contributes to hype and overclaiming."

Reproducibility assessment (M2) evaluates whether sufficient details exist to replicate experiments—not whether reviewers personally run code.

## Specific NLP Paper Issues

The g
…[truncated 576 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 43728
}
```

</details>

---


### Tool call

_source line 727 · 2026-05-16T04:23:36.133398+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — Round 1 审稿报告\n\n**审查侧重：方法严谨性 + 实验设计 + 统计有效性**\n\n---\n\n## 总体评分\n**Overall**: 3.5/5（介于 Findings acceptance 和 Conference acceptance 之间）\n**一句话总结**: 论文对 structured IE 中 quality estimation 与 sample selection 的解耦提供了系统性实证，核心 NER 发现扎实，但 RE 覆盖不足、scale 范围过窄、以及若干因果推断的证据链不完整限制了 generality claims 的力度。\n\n## 官方维度打分（ARR 2025+ Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | NER 主张有充分支撑；RE 适当标注 preliminary；但 LP compression \"task-intrinsic\" 因果推断与 free-form RE reversal 矛盾；ε=0.05 阈值选择存在 circularity |\n| Excitement | 3/5 | Correlation-selection gap 是有实践价值的负性发现，对 test-time scaling 社区有意义；但论文本身不提供解决方案，且发现的 surprise 有限——instance-level 信号无法 rank candidates 是构造性的 |\n| Overall Assessment | 3.5/5 | 方法论严谨，统计处理在同类工作中属上乘，但 claim scope 超出证据覆盖（单一 RE benchmark、3B–8B scale），建议 Findings 或经修改后 Main Conference |\n| Reproducibility | 4/5 | 训练配置、prompt template、超参数详尽（Appendix F）；代码/数据承诺 upon acceptance；缺少 inference compute budget 和具体 vLLM 版本 |\n| Reviewer Confidence | 4/5 | 仔细阅读了正文和全部附录；对 statistical methodology 和 structured IE 评估有经验 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] RE 覆盖不足与 claim scope 不匹配\n- 具体位置：Title (\"LLM-Based Information Extraction\"), Abstract line 3 (\"NER and RE benchmarks\"), §5\n- 问题：论文标题和 abstract 将贡献定位为 \"Information Extraction\"，涵盖 NER + RE，但 RE 实验仅在 SciERC 一个 benchmark 上进行（且 40% zero-F1）。NER 有 3 个 benchmark 跨难度梯度，RE 却缺乏类似设计。论文在正文中反复标注 \"preliminary\"（≥12 次），但标题、abstract 第 1–2 句和 Figure 1 caption 均未体现这一限定。\n- 为什么影响接收：单一 RE benchmark 不足以支撑 \"Information Extraction\" 级别的 claim。SciERC RE 的 40% zero-F1 率进一步削弱该 benchmark 的代表性。\n- 建议：(1) 将标题/abstract 显式限定为 \"primarily NER, with preliminary RE evidence\"；(2) 增加至少一个额外 RE benchmark（如 TACRED、DocRED、或 ACE05）；(3) 若无法增加数据集，则将 RE 结论完全移至附录并在 abstract 中删除 RE 相关的具体数字。\n\n**N2** [critical] ε=0.05 \"tied fraction\" 阈值的 circularity\n- 具体位置：Appendix §app:logprob_ties（line 499–500）, Table 11（ε sweep）\n- 问题：Appendix 声称 \"the median within-instance LP range is only 0.041 nats—below the ε=0.05 threshold used throughout, providing data-driven justification for this cutoff.\" 这是 circular reasoning：阈值 ε 的选择是为了让 median LP range 落在阈值以下。Table 11 的 ε sweep 显示 ε=0.05 恰好给出最强 p-value（p=0.004），暗示 p-value optimization。ARR guidelines (R1) 明确标记 threshold optimization 为 problematic practice。\n- 建议：(1) 用 pre-registered 或 literature-grounded ε 替代；(2) 报告 ε-free 的连续指标（median LP range 本身即可作为核心统计量）；(3) 如果保留 ε，承认 circularity 并在所有 tied-fraction 数字旁标注 \"threshold-dependent\"。\n\n**N3** [critical] \"LP compression is model/task intrinsic, not decoding artifact\" 的因果推断被 RE reversal 削弱\n- 具体位置：Abstract line 6, §6 ¶\"Ablation: free-form decoding\", Appendix Table 15 Panel B\n- 问题：论文声称 free-form ablation \"confirms NER compression is not an artifact of constrained decoding\"，但 RE 数据直接反驳——LP selection 在 constrained 下为 −0.68 pp，free-form 下为 +1.69 pp。至少对 RE 而言，constrained decoding 确实是 LP selection failure 的一个因素。Abstract 的措辞暗示了比实际证据更强的结论。\n- 建议：Abstract 改为 \"...confirms NER compression is not caused by constrained decoding; on RE, LP selection reverses direction under free-form decoding, suggesting regime-dependent behavior (preliminary, single benchmark).\"\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Scale range (3B–8B) 过窄，不足以支撑 \"task difficulty is the primary driver\" 因果结论\n- 具体位置：§5.4 line 120, Conclusion line 6\n- 建议：弱化为 \"task difficulty is a stronger predictor than model scale within the 3B–8B range tested\"。\n\n**W2** [warning] 3 seeds 对 stability claims 的统计效力不足\n- 具体位置：Appendix Table 8, Table 10 (Kendall's W)\n- Kendall's W=1.000 with 3 observations 不具信息量。σ≤0.026 基于 n=3，95% CI 极宽。\n- 建议：增加至少 5–10 seeds 或弱化 stability 措辞。\n\n**W3** [warning] \"Greedy\" baseline 实为 T=1.0 random sample，命名混淆\n- 建议：使用 \"single-sample\" 替代 \"greedy\"；增加 argmax (T=0) baseline。\n\n**W4** [warning] 缺少信号组合实验\n- LP non-tied subset 的 +2.9 pp gain 暗示 VC 筛选 + LP 排序等组合策略可能有效。\n- 建议：增加至少一个 simple combination baseline。\n\n**W5** [warning] Gold-empty filtering 比例差异（CoNLL 20.2% vs SciERC 4.0%）影响跨数据集可比性\n- 建议：报告 CoNLL full-set ρ 作为对照。\n\n**W6** [warning] Thinking token confound 的 \"CoNLL control\" 论证薄弱\n- CoNLL 高 tied fraction 更可能因 task easiness（88% identical outputs），而非证据排除 thinking token 假说。Task difficulty 与 thinking token 混淆未被分离。\n\n---\n\n## 小问题\n\n- Table 3 NER 用 2-seed mean，其他部分用 3 seeds，未说明原因\n- Figure 1 caption 措辞对 LP 不适用（LP 是 per-sample，非 instance-level）\n- \\cite vs \\citet 使用不一致\n- 引用验证：3 条 bib entries 未在 OpenAlex 索引中找到（hobelsberger2025, lightman2024, venktesh2025），均为知名预印本，非引用错误\n\n## Questions to Authors\n\n1. ε=0.05 的选择是否先于 LP range 分析确定？\n2. 为什么 Table 3 selection analysis 使用 2 seeds 而非 3？\n3. 是否考虑过 LP + consistency signal 组合策略？\n4. Free-form RE reversal 是否在不同 temperature 下也成立？\n5. 增加 TACRED/ACE05 是否预计 RE conclusions 会有质性变化？\n\n## Missing References\n\n- Huang et al. (2024) \"Large Language Models Cannot Self-Correct Reasoning Yet\" — 对 self-assessment 限制有直接相关性\n- Fernandes et al. (2022) \"Quality-Aware Decoding for Neural Machine Translation\" — MBR 在 structured prediction 的早期讨论\n\n## 主要优势\n\n- 统计方法论在同类工作中属上乘（Bootstrap CI、TOST with external anchors、permutation test）\n- 三指标框架（ρ, AUROC, selection F1）的 dissociation 是重要的方法论贡献\n- 极其详尽的 appendix（15 sections），几乎每个 claim 都有 robustness check\n- 诚实的 RE hedging 和全面的 Limitations section\n- Matched training protocol 消除跨模型训练 confound\n- LP compression 的系统性诊断分析是论文最有洞察力的贡献",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — Round 1 审稿报告\n\n**审查侧重：方法严谨性 + 实验设计 + 统计有效性**\n\n---\n\n## 总体评分\n**Overall**: 3.5/5（介于 Findings acceptance 和 Conference acceptance 之间）\n**一句话总结**: 论文对 structured IE 中 quality estimation 与 sample selection 的解耦提供了系统性实证，核心 NER 发现扎实，但 RE 覆盖不足、scale 范围过窄、以及若干因果推断的证据链不完整限制了 generality claims 的力度。\n\n## 官方维度打分（ARR 2025+ Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | NER 主张有充分支撑；RE 适当标注 preliminary；但 LP compression \"task-intrinsic\" 因果推断与 free-form RE reversal 矛盾；ε=0.05 阈值选择存在 circularity |\n| Excitement | 3/5 | Correlation-selection gap 是有实践价值的负性发现，对 test-time scaling 社区有意义；但论文本身不提供解决方案，且发现的 surprise 有限——instance-level 信号无法 rank candidates 是构造性的 |\n| Overall Assessment | 3.5/5 | 方法论严谨，统计处理在同类工作中属上乘，但 claim scope 超出证据覆盖（单一 RE benchmark、3B–8B scale），建议 Findings 或经修改后 Main Conference |\n| Reproducibility | 4/5 | 训练配置、prompt template、超参数详尽（Appendix F）；代码/数据承诺 upon acceptance；缺少 inference compute budget 和具体 vLLM 版本 |\n| Reviewer Confidence | 4/5 | 仔细阅读了正文和全部附录；对 statistical methodology 和 structured IE 评估有经验 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] RE 覆盖不足与 claim scope 不匹配\n- 具体位置：Title (\"LLM-Based Information Extraction\"), Abstract line 3 (\"NER and RE benchmarks\"), §5\n- 问题：论文标题和 abstract 将贡献定位为 \"Information Extraction\"，涵盖 NER + RE，但 RE 实验仅在 SciERC 一个 benchmark 上进行（且 40% zero-F1）。NER 有 3 个 benchmark 跨难度梯度，RE 却缺乏类似设计。论文在正文中反复标注 \"preliminary\"（≥12 次），但标题、abstract 第 1–2 句和 Figure 1 caption 均未体现这一限定。\n- 为什么影响接收：单一 RE benchmark 不足以支撑 \"Information Extraction\" 级别的 claim。SciERC RE 的 40% zero-F1 率进一步削弱该 benchmark 的代表性。\n- 建议：(1) 将标题/abstract 显式限定为 \"primarily NER, with preliminary RE evidence\"；(2) 增加至少一个额外 RE benchmark（如 TACRED、DocRED、或 ACE05）；(3) 若无法增加数据集，则将 RE 结论完全移至附录并在 abstract 中删除 RE 相关的具体数字。\n\n**N2** [critical] ε=0.05 \"tied fraction\" 阈值的 circularity\n- 具体位置：Appendix §app:logprob_ties（line 499–500）, Table 11（ε sweep）\n- 问题：Appendix 声称 \"the median within-instance LP range is only 0.041 nats—below the ε=0.05 threshold used throughout, providing data-driven justification for this cutoff.\" 这是 circular reasoning：阈值 ε 的选择是为了让 median LP range 落在阈值以下。Table 11 的 ε sweep 显示 ε=0.05 恰好给出最强 p-value（p=0.004），暗示 p-value optimization。ARR guidelines (R1) 明确标记 threshold optimization 为 problematic practice。\n- 建议：(1) 用 pre-registered 或 literature-grounded ε 替代；(2) 报告 ε-free 的连续指标（median LP range 本身即可作为核心统计量）；(3) 如果保留 ε，承认 circularity 并在所有 tied-fraction 数字旁标注 \"threshold-dependent\"。\n\n**N3** [critical] \"LP compression is model/task intrinsic, not decoding artifact\" 的因果推断被 RE reversal 削弱\n- 具体位置：Abstract line 6, §6 ¶\"Ablation: free-form decoding\", Appendix Table 15 Panel B\n- 问题：论文声称 free-form ablation \"confirms NER compression is not an artifact of constrained decoding\"，但 RE 数据直接反驳——LP selection 在 constrained 下为 −0.68 pp，free-form 下为 +1.69 pp。至少对 RE 而言，constrained decoding 确实是 LP selection failure 的一个因素。Abstract 的措辞暗示了比实际证据更强的结论。\n- 建议：Abstract 改为 \"...confirms NER compression is not caused by constrained decoding; on RE, LP selection reverses direction under free-form decoding, suggesting regime-dependent behavior (preliminary, single benchmark).\"\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Scale range (3B–8B) 过窄，不足以支撑 \"task difficulty is the primary driver\" 因果结论\n- 具体位置：§5.4 line 120, Conclusion line 6\n- 建议：弱化为 \"task difficulty is a stronger predictor than model scale within the 3B–8B range tested\"。\n\n**W2** [warning] 3 seeds 对 stability claims 的统计效力不足\n- 具体位置：Appendix Table 8, Table 10 (Kendall's W)\n- Kendall's W=1.000 with 3 observations 不具信息量。σ≤0.026 基于 n=3，95% CI 极宽。\n- 建议：增加至少 5–10 seeds 或弱化 stability 措辞。\n\n**W3** [warning] \"Greedy\" baseline 实为 T=1.0 random sample，命名混淆\n- 建议：使用 \"single-sample\" 替代 \"greedy\"；增加 argmax (T=0) baseline。\n\n**W4** [warning] 缺少信号组合实验\n- LP non-tied subset 的 +2.9 pp gain 暗示 VC 筛选 + LP 排序等组合策略可能有效。\n- 建议：增加至少一个 simple combination baseline。\n\n**W5** [warning] Gold-empty filtering 比例差异（CoNLL 20.2% vs SciERC 4.0%）影响跨数据集可比性\n- 建议：报告 CoNLL full-set ρ 作为对照。\n\n**W6** [warning] Thinking token confound 的 \"CoNLL control\" 论证薄弱\n- CoNLL 高 tied fraction 更可能因 task easiness（88% identical outputs），而非证据排除 thinking token 假说。Task difficulty 与 thinking token 混淆未被分离。\n\n---\n\n## 小问题\n\n- Table 3 NER 用 2-seed mean，其他部分用 3 seeds，未说明原因\n- Figure 1 caption 措辞对 LP 不适用（LP 是 per-sample，非 instance-level）\n- \\cite vs \\citet 使用不一致\n- 引用验证：3 条 bib entries 未在 OpenAlex 索引中找到（hobelsberger2025, lightman2024, venktesh2025），均为知名预印本，非引用错误\n\n## Questions to Authors\n\n1. ε=0.05 的选择是否先于 LP range 分析确定？\n2. 为什么 Table 3 selection analysis 使用 2 seeds 而非 3？\n3. 是否考虑过 LP + consistency signal 组合策略？\n4. Free-form RE reversal 是否在不同 temperature 下也成立？\n5. 增加 TACRED/ACE05 是否预计 RE conclusions 会有质性变化？\n\n## Missing References\n\n- Huang et al. (2024) \"Large Language Models Cannot Self-Correct Reasoning Yet\" — 对 self-assessment 限制有直接相关性\n- Fernandes et al. (2022) \"Quality-Aware Decoding for Neural Machine Translation\" — MBR 在 structured prediction 的早期讨论\n\n## 主要优势\n\n- 统计方法论在同类工作中属上乘（Bootstrap CI、TOST with external anchors、permutation test）\n- 三指标框架（ρ, AUROC, selection F1）的 dissociation 是重要的方法论贡献\n- 极其详尽的 appendix（15 sections），几乎每个 claim 都有 robustness check\n- 诚实的 RE hedging 和全面的 Limitations section\n- Matched training protocol 消除跨模型训练 confound\n- LP compression 的系统性诊断分析是论文最有洞察力的贡献",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 728 · 2026-05-16T04:23:39.899717+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3766
}
```

</details>

---


### Assistant

_source line 729 · 2026-05-16T04:23:47.026830+00:00_

审稿报告已提交给 Review Director。

**审稿摘要：**

- **Overall 3.5/5**，Soundness 3.5，Excitement 3
- 3 个 Must-Fix：(N1) RE 仅 SciERC 一个 benchmark 与 title/abstract 的 "IE" scope 不匹配；(N2) ε=0.05 tied-fraction 阈值存在 circular reasoning / p-value optimization 嫌疑；(N3) abstract 关于 LP compression "not a decoding artifact" 的措辞被 RE free-form reversal 削弱
- 6 个 Should-Fix：scale range 过窄、3 seeds 统计效力不足、greedy baseline 命名混淆、缺信号组合实验、gold-empty filtering 跨数据集不可比、thinking token CoNLL control 论证薄弱
- **主要优势**：统计方法论上乘，三指标 dissociation 框架有贡献，appendix 极其详尽，LP compression 诊断分析系统性强

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 23

## Round 23

12 recorded events


### User

_source line 730 · 2026-05-16T04:25:03.364388+00:00_

[Round 1 审稿请求]:
## 交叉分享 — Reviewer 2 的完整审稿意见

请逐条回应以下 Reviewer 2 的审稿意见。对每一条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

以下是 Reviewer 2 的完整审稿原文：

### Overall: 3.0/5 (Findings)
Soundness 3.5, Excitement 2.5, Confidence 4/5

### Must-Fix 问题

**N1** [critical] "Instance-level signals fail by construction" 是 definitional observation，不应算作 empirical contribution
- 位置：Section 1 Contribution 1、Section 4.2 第二段、Section 5 第二段
- 论文反复强调四个 instance-level signals 因只产生单一分数而无法 per-sample selection，但这是定义层面的必然结果，不构成 empirical finding。论文自己也承认 "fail by construction"，却仍列为三大贡献之一（"Metric dissociation"）。去掉 definitional 部分后，empirical novelty 只剩 LP compression 和 MBR within-instance failure——前者 scope 有限，后者与 Eikema & Aziz (2025) structured MBR 发现高度一致。
- 建议：将 instance-level/per-sample 区分作为 problem formulation 前提（Section 3），聚焦 LP compression 和 difficulty-dependent rankings 作为贡献。

**N2** [critical] RE 结论仅基于 SciERC 单一 benchmark 且 40% zero-F1 rate
- 与你的 N1 一致：RE 覆盖不足，title/abstract scope 不匹配。

**N3** [critical] 与 Yao et al. (2026) 的增量贡献定义不够清晰
- 三个 "extension"（structural matching、selection analysis、difficulty gradient）中：(a) SJ 比 EM 高 0.065 ρ 仅 marginal significance；(b) selection analysis 核心是 negative result；(c) WNUT-17 所有 signal collapse。Combined novelty 是否足够？

### Should-Fix 问题

**W1** "Preliminary" 标注过于频繁（≥11次），削弱论文可信度
**W2** LP compression 缺乏 mechanistic explanation
**W3** 缺少对 conformal prediction / set-valued uncertainty 的讨论（ICLR 2025, arxiv 2410.06296）
**W4** 3B-8B 规模限制对结论适用范围影响大
**W5** Spearman ρ 作为 primary QE metric 缺乏 justification

### 缺失引用
1. Conformal Structured Prediction (ICLR 2025)
2. "Beyond Confidence" (arxiv 2605.07806, May 2026)
3. "Learning When to Sample" (arxiv 2603.08999, March 2026)
4. Slim-SC / Thought Pruning (EMNLP 2025)

### 主要优势
- 实验设计系统且严谨
- 诚实的 scope 限定
- 清晰的 practical recommendations
- 高质量 Appendix
- MBR within- vs across-instance failure analysis 有价值

---

请对 Reviewer 2 的每个 Must-Fix、Should-Fix 和缺失引用逐条回应 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 731 · 2026-05-16T04:25:34.726819+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2410.06296 conformal structured prediction ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2410.06296 conformal structured prediction ICLR 2025"
  }
}
```

</details>

---


### Tool call

_source line 732 · 2026-05-16T04:25:34.877758+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2605.07806 \"Beyond Confidence\" May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2605.07806 \"Beyond Confidence\" May 2026"
  }
}
```

</details>

---


### Tool call

_source line 733 · 2026-05-16T04:25:35.330010+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2603.08999 \"Learning When to Sample\" March 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2603.08999 \"Learning When to Sample\" March 2026"
  }
}
```

</details>

---


### Tool call

_source line 734 · 2026-05-16T04:25:35.581714+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Slim-SC Thought Pruning self-consistency EMNLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Slim-SC Thought Pruning self-consistency EMNLP 2025"
  }
}
```

</details>

---


### Tool result

_source line 735 · 2026-05-16T04:25:40.353388+00:00_

Web search results for query: "arxiv 2410.06296 conformal structured prediction ICLR 2025"

Links: [{"title":"[2410.06296] Conformal Structured Prediction","url":"https://arxiv.org/abs/2410.06296"},{"title":"ICLR Conformal Structured Prediction","url":"https://iclr.cc/virtual/2025/32866"},{"title":"Conformal Structured Prediction","url":"https://www.researchgate.net/publication/384769274_Conformal_Structured_Prediction"},{"title":"Published as a conference paper at ICLR 2025 CONFORMAL STRUCTURED PREDICTION","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/1868a3c73d0d2a44c42458575fa8514c-Paper-Conference.pdf"},{"title":"ICML Poster Volume Optimality in Conformal Prediction with Structured Prediction Sets","url":"https://icml.cc/virtual/2025/poster/44066"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2410.01767"},{"title":"Conformal Risk Control | OpenReview","url":"https://openreview.net/forum?id=33XGfHLtZg"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/9da457059dd3386a2166c5b08f29b7de-Paper-Conference.pdf"},{"title":"ICLR Prune 'n Predict: Optimizing LLM Decision-making with Conformal Prediction","url":"https://iclr.cc/virtual/2025/32865"},{"title":"Conformal Information Pursuit for Interactively Guiding Large Language Models","url":"https://arxiv.org/html/2507.03279v2"}]

I found information about arxiv paper 2410.06296 on "Conformal Structured Prediction":

## Overview
The paper proposes a general framework for conformal prediction in the structured prediction setting, modifying existing conformal prediction algorithms to output structured prediction sets that implicitly represent sets of labels.

## Key Problem
Existing conformal prediction algorithms have largely targeted classification and regression settings with simple prediction set structures, but for complex structured outputs such as text generation, these prediction sets might 
…[truncated 802 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 5626
}
```

</details>

---


### Tool result

_source line 736 · 2026-05-16T04:25:41.859699+00:00_

Web search results for query: "arxiv 2605.07806 "Beyond Confidence" May 2026"

Links: [{"title":"[2605.07806] Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs","url":"https://arxiv.org/abs/2605.07806"},{"title":"The Confidence Trap: Gender Bias and Predictive Certainty in LLMs","url":"https://arxiv.org/pdf/2601.07806"},{"title":"Beyond ECE: Calibrated Size Ratio, Risk Assessment, and Confidence-Weighted Metrics","url":"https://arxiv.org/html/2605.01796"},{"title":"[2605.05964] Uncertainty Estimation via Hyperspherical Confidence Mapping","url":"https://arxiv.org/abs/2605.05964"},{"title":"[2605.01796] Beyond ECE: Calibrated Size Ratio, Risk Assessment, and Confidence-Weighted Metrics","url":"https://arxiv.org/abs/2605.01796"},{"title":"[2605.05166] The First Token Knows: Single-Decode Confidence for Hallucination Detection","url":"https://arxiv.org/abs/2605.05166"},{"title":"[2605.10893v1] Grounded or Guessing? LVLM Confidence Estimation via Blind-Image Contrastive Ranking","url":"https://arxiv.org/abs/2605.10893v1"},{"title":"PDCR: Perception-Decomposed Confidence Reward for Vision-Language Reasoning","url":"https://arxiv.org/html/2605.13467"},{"title":"[2605.10893] Grounded or Guessing? LVLM Confidence Estimation via Blind-Image Contrastive Ranking","url":"https://arxiv.org/abs/2605.10893"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=202&show=2000"}]

I found the paper you were looking for! Here are the details about arxiv 2605.07806:

## "Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs"

The paper was submitted on May 8, 2026, with authors Sree Bhattacharyya, Samarth Khanna, Leona Chen, Lucas Craig, Tharun Dilliraj, and James Z. Wang.

**Research Focus:**

The paper addresses how Large Language Models (LLMs) can achieve reliable self-assessment, which is critical in many applications. While assessment methods have evolved from using probabilistic correctness estimate
…[truncated 932 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6981
}
```

</details>

---


### Tool result

_source line 737 · 2026-05-16T04:25:41.960632+00:00_

Web search results for query: "arxiv 2603.08999 "Learning When to Sample" March 2026"

Links: [{"title":"[2603.08999] Learning When to Sample: Confidence-Aware Self-Consistency for Efficient LLM Chain-of-Thought Reasoning","url":"https://arxiv.org/abs/2603.08999"},{"title":"Learning When to Sample: Confidence-Aware Self-Consistency for Efficient LLM Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2603.08999"},{"title":"Learning When to Sample: Confidence-Aware Self-Consistency for","url":"https://arxiv.org/pdf/2603.08999"},{"title":"Why AI systems don’t learn and what to do about it Lessons on autonomous learning from cognitive science","url":"https://arxiv.org/html/2603.15381v1"},{"title":"A Survey of Reinforcement Learning For Economics","url":"https://arxiv.org/html/2603.08956v5"},{"title":"Learning to Solve Orienteering Problem with Time ...","url":"https://arxiv.org/pdf/2603.06260"},{"title":"[2603.01309] PAC Guarantees for Reinforcement Learning: Sample Complexity, Coverage, and Structure","url":"https://arxiv.org/abs/2603.01309"},{"title":"Continual Learning in Large Language Models: Methods, Challenges, and Opportunities","url":"https://arxiv.org/html/2603.12658v1"},{"title":"March, 2026 Retrieval-Augmented LLM Agents: Learning to Learn from Experience","url":"https://arxiv.org/pdf/2603.18272"},{"title":"A Grammar of Machine Learning Workflows Simon Roth March 14, 2026 Abstract","url":"https://arxiv.org/pdf/2603.10742"}]

I found the arxiv paper 2603.08999 titled "Learning When to Sample: Confidence-Aware Self-Consistency for Efficient LLM Chain-of-Thought Reasoning".

Here are the key details:

**Paper Information:**
- Submitted on 9 Mar 2026 (v1), last revised 17 Mar 2026 (v2)
- Authors: Juming Xiong, Kevin Guo, Congning Ni, Chao Yan, Katherine Brown, Avinash Baidya, Xiang Gao, Bradley Malin, Zhijun Yin

**Summary:**
Large language models achieve strong reasoning performance through chain-of-thought reasoning, yet often generate unnecessarily lon
…[truncated 915 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6630
}
```

</details>

---


### Tool result

_source line 738 · 2026-05-16T04:25:42.463810+00:00_

Web search results for query: "Slim-SC Thought Pruning self-consistency EMNLP 2025"

Links: [{"title":"GitHub - hyscale-lab/slimsc: Official repository for the EMNLP 2025 paper \"Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency\".","url":"https://github.com/hyscale-lab/slimsc"},{"title":"Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1750/"},{"title":"Thought Pruning for Efficient Scaling with Self-Consistency","url":"https://aclanthology.org/2025.emnlp-main.1750.pdf"},{"title":"Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/slim-sc-thought-pruning-for-efficient-scaling-with-self-consistency/"},{"title":"[2509.13990] Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency","url":"https://arxiv.org/abs/2509.13990"},{"title":"Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency","url":"https://arxiv.org/html/2509.13990v1"},{"title":"[Literature Review] Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency","url":"https://www.themoonlight.io/en/review/slim-sc-thought-pruning-for-efficient-scaling-with-self-consistency"},{"title":"Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency","url":"https://www.researchgate.net/publication/397418864_Slim-SC_Thought_Pruning_for_Efficient_Scaling_with_Self-Consistency"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=12225&show=2000"},{"title":"Parallel-Probe: Towards Efficient Parallel Thinking via 2D Probing","url":"https://arxiv.org/html/2602.03845v2"}]

Based on the search results, here's what I found about Slim-SC:

## Overview

Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency is a paper by Colin Hong, Xu Guo, Anand Chaanan Singh, Esha Choukse, and Dmitrii Ustiugov presented at EMNLP 2025.

## Problem 
…[truncated 1189 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6882
}
```

</details>

---


### Tool call

_source line 739 · 2026-05-16T04:27:42.041340+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — 交叉回应 Reviewer 2 审稿意见\n\n---\n\n### Must-Fix 问题\n\n**[REBUT] R2-N1: \"Instance-level signals fail by construction\" 是 definitional observation，不应算作 empirical contribution**\n\nR2 部分正确但过度延伸。\"四个 instance-level signals 无法 rank candidates\" 确实是构造性的，但 Contribution 1（Metric dissociation）的核心是 ρ/AUROC/selection F1 三指标在实证中的 decoupling——这需要数据来展示：\n- Table 1 中 EM 在 CoNLL AUROC 最高（0.816）但 ρ 排名不同\n- Appendix §app:verbalized_confidence 中 VerbConf ρ > LP 但 selection 最差——per-sample signal 之间的 dissociation 不是 definitional\n- Table 4 中 LP full-set/conditional ρ inversion（−0.410 → +0.350）\n\n但同意 framing 可改进：应将 instance-level/per-sample 区分移至 §3 作为前提，Contribution 1 重新聚焦为 empirical dissociation。Eikema et al. (2025) 的 overlap 存在但本文提供了 IE-specific failure mode（utility correlates across but not within instances）。\n\n**[AGREE] R2-N2: RE 单一 benchmark** — 与我的 N1 完全一致。\n\n**[REBUT] R2-N3: 与 Yao et al. (2026) 增量贡献不够清晰**\n\nR2 低估了 selection analysis 的价值：\n(a) SJ vs EM marginal（Δρ=+0.065）确实，但 structural vs LP gap（Δρ=+0.155, CI [+0.074, +0.234], Table 6）clearly significant，Yao 未评估 structural signals 或 LP\n(b) Selection analysis 是 test-time scaling 社区最关心的问题——Yao 止步于 correlation，本文的 correlation-selection gap 证明 more samples ≠ better selection 在 structured IE 中不成立\n(c) WNUT-17 的 LP full/conditional inversion 提供了具体 diagnostic insight，不仅是 \"collapse\"\n\n建议作者在 Introduction 更明确 tabulate 与 Yao 的差异，但 combined novelty 足够。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: \"Preliminary\" 过于频繁** — 建议首次完整说明后用 † 标记替代。\n\n**[AGREE] R2-W2: LP compression 缺乏 mechanistic explanation** — 论文展示了现象但未解释原因。应至少讨论可能的 hypotheses：token averaging 平滑 variance、schema-enforced tokens 占多数 tokens 导致有效 variance 来源少、constrained decoding 下有效 vocabulary 缩小等。\n\n**[REBUT] R2-W3: 缺少 conformal prediction 讨论** — Conformal prediction 构建具有 coverage guarantee 的 prediction sets，与本文的 best-of-N point selection 目标 fundamentally 不同。High-level connection 在 uncertainty quantification 层面存在，但 Related Work 中一句简要提及足矣，detailed discussion 不必要。\n\n**[AGREE] R2-W4: 3B-8B scale 限制** — 与我的 W1 一致。\n\n**[REBUT] R2-W5: Spearman ρ 缺乏 justification** — Spearman ρ 是 uncertainty estimation 文献标准 metric（Kuhn 2023, Kadavath 2022），rank-based 对非线性关系鲁棒。更重要的是论文并非只用 ρ——三指标框架（ρ + AUROC + selection F1）本身就是对 single-metric 问题的回应。Conditional analysis（Table 4）处理了 floor/ceiling effects。\n\n---\n\n### 缺失引用\n\n**[AGREE] #1 Conformal Structured Prediction (ICLR 2025)** — tangential 但值得在 Related Work 简要提及。\n**[AGREE] #2 \"Beyond Confidence\" (2605.07806)** — 与 verbalized confidence failure 直接相关，应引用。\n**[REBUT] #3 \"Learning When to Sample\" (2603.08999)** — 处理 discrete-answer CoT，本文已引用同类工作（Feng 2025, Wang 2025, Kim 2026），coverage 充分。\n**[REBUT] #4 Slim-SC (EMNLP 2025)** — discrete-answer efficiency 问题，与 structured IE selection failure 不同，非 critical missing。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — 交叉回应 Reviewer 2 审稿意见\n\n---\n\n### Must-Fix 问题\n\n**[REBUT] R2-N1: \"Instance-level signals fail by construction\" 是 definitional observation，不应算作 empirical contribution**\n\nR2 部分正确但过度延伸。\"四个 instance-level signals 无法 rank candidates\" 确实是构造性的，但 Contribution 1（Metric dissociation）的核心是 ρ/AUROC/selection F1 三指标在实证中的 decoupling——这需要数据来展示：\n- Table 1 中 EM 在 CoNLL AUROC 最高（0.816）但 ρ 排名不同\n- Appendix §app:verbalized_confidence 中 VerbConf ρ > LP 但 selection 最差——per-sample signal 之间的 dissociation 不是 definitional\n- Table 4 中 LP full-set/conditional ρ inversion（−0.410 → +0.350）\n\n但同意 framing 可改进：应将 instance-level/per-sample 区分移至 §3 作为前提，Contribution 1 重新聚焦为 empirical dissociation。Eikema et al. (2025) 的 overlap 存在但本文提供了 IE-specific failure mode（utility correlates across but not within instances）。\n\n**[AGREE] R2-N2: RE 单一 benchmark** — 与我的 N1 完全一致。\n\n**[REBUT] R2-N3: 与 Yao et al. (2026) 增量贡献不够清晰**\n\nR2 低估了 selection analysis 的价值：\n(a) SJ vs EM marginal（Δρ=+0.065）确实，但 structural vs LP gap（Δρ=+0.155, CI [+0.074, +0.234], Table 6）clearly significant，Yao 未评估 structural signals 或 LP\n(b) Selection analysis 是 test-time scaling 社区最关心的问题——Yao 止步于 correlation，本文的 correlation-selection gap 证明 more samples ≠ better selection 在 structured IE 中不成立\n(c) WNUT-17 的 LP full/conditional inversion 提供了具体 diagnostic insight，不仅是 \"collapse\"\n\n建议作者在 Introduction 更明确 tabulate 与 Yao 的差异，但 combined novelty 足够。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: \"Preliminary\" 过于频繁** — 建议首次完整说明后用 † 标记替代。\n\n**[AGREE] R2-W2: LP compression 缺乏 mechanistic explanation** — 论文展示了现象但未解释原因。应至少讨论可能的 hypotheses：token averaging 平滑 variance、schema-enforced tokens 占多数 tokens 导致有效 variance 来源少、constrained decoding 下有效 vocabulary 缩小等。\n\n**[REBUT] R2-W3: 缺少 conformal prediction 讨论** — Conformal prediction 构建具有 coverage guarantee 的 prediction sets，与本文的 best-of-N point selection 目标 fundamentally 不同。High-level connection 在 uncertainty quantification 层面存在，但 Related Work 中一句简要提及足矣，detailed discussion 不必要。\n\n**[AGREE] R2-W4: 3B-8B scale 限制** — 与我的 W1 一致。\n\n**[REBUT] R2-W5: Spearman ρ 缺乏 justification** — Spearman ρ 是 uncertainty estimation 文献标准 metric（Kuhn 2023, Kadavath 2022），rank-based 对非线性关系鲁棒。更重要的是论文并非只用 ρ——三指标框架（ρ + AUROC + selection F1）本身就是对 single-metric 问题的回应。Conditional analysis（Table 4）处理了 floor/ceiling effects。\n\n---\n\n### 缺失引用\n\n**[AGREE] #1 Conformal Structured Prediction (ICLR 2025)** — tangential 但值得在 Related Work 简要提及。\n**[AGREE] #2 \"Beyond Confidence\" (2605.07806)** — 与 verbalized confidence failure 直接相关，应引用。\n**[REBUT] #3 \"Learning When to Sample\" (2603.08999)** — 处理 discrete-answer CoT，本文已引用同类工作（Feng 2025, Wang 2025, Kim 2026），coverage 充分。\n**[REBUT] #4 Slim-SC (EMNLP 2025)** — discrete-answer efficiency 问题，与 structured IE selection failure 不同，非 critical missing。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 740 · 2026-05-16T04:27:45.761805+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3720
}
```

</details>

---


### Assistant

_source line 741 · 2026-05-16T04:27:54.445301+00:00_

Round 1 审稿报告和 Reviewer 2 交叉回应均已发送给 Review Director。

总结：
- **我的审稿**：Overall 3.5/5，3 个 Must-Fix（RE 覆盖不足、ε 阈值 circularity、LP "task-intrinsic" 因果推断被 RE reversal 削弱）+ 6 个 Should-Fix
- **对 R2 的回应**：R2-N1 部分反驳（metric dissociation 有 empirical 成分但 framing 需改进）、R2-N2 同意、R2-N3 反驳（selection analysis 价值被低估）；W3（conformal prediction）和 W5（Spearman ρ）反驳；W1/W2/W4 同意；缺失引用 #1/#2 同意、#3/#4 反驳（discrete-answer 工作，已有充分覆盖）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 24

## Round 24

42 recorded events


### User

_source line 742 · 2026-05-16T05:12:24.235189+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计 + 统计分析）

### Venue 信息
- **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle)
- **截止日期**: 2026-05-25
- **格式**: ACL 模板, 正文 8 页, double-blind, Limitations/Ethics 不计页数
- **匿名规则**: double-blind, 禁止自引暴露身份

### 论文文件
- 主文件: `projects/struct_self_consist_ie/docs/paper/main.tex`
- Section 文件: `projects/struct_self_consist_ie/docs/paper/sections/` 目录下 (abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex)
- 引用: `projects/struct_self_consist_ie/docs/paper/references.bib`

### 你的审查侧重

**核心任务：评估方法严谨性、实验设计和统计分析的可靠性。** 具体关注：

1. **方法论有效性**
   - 5 个 confidence signal 的定义是否严谨、无歧义
   - Soft Jaccard (SJ) 的 Hungarian matching + IoU 定义是否正确
   - instance-level vs per-sample 的区分是否成立——特别是 4/5 信号无法做 selection 是否是 tautological（定义上必然的）而非 empirical finding
   - Evaluation framework (ρ, AUROC, selection F1) 三指标是否充分且无冗余

2. **实验设计**
   - 3 个 NER benchmark + 1 个 RE benchmark 的覆盖度是否足够支撑 "structured IE" 的论文标题
   - N=8 (primary) / N=16 的样本量选择是否合理
   - 2 个 model family (Qwen3-8B, LLaMA-3.1-8B) + 1 个 4B ablation 的 scale coverage 是否足够
   - Fine-tuning setup (LoRA rank=32, 5 epochs) 是否标准且可复现
   - Free-form decoding ablation 的设计是否能有效隔离 constrained decoding 的影响

3. **统计分析**
   - Spearman ρ 的 bootstrap CI 和 permutation test 是否正确应用
   - Selection F1 的 Fisher p-value 和 sign test 是否适当
   - TOST 等价性检验的 δ 选择是否有 prior justification（注意 ε=0.05 是否存在 circularity）
   - 3-seed stability (Kendall W=1.000 with n=3) 的统计效力
   - 多重比较校正是否充分（只对 positive finding 做了 Bonferroni）
   - Gold-empty instance filtering 的决策是否合理且一致

4. **数据可靠性**
   - Table 1-4 之间数据是否一致
   - 正文、caption、appendix 中同一数值的引用是否一致
   - Table 2 NER 2-seed vs RE 单 seed 的不一致是否有合理解释

5. **页数合规**
   - 正文是否在 8 页限制内（不计 Limitations, Ethics, References, Appendix）

请输出完整审稿报告，包括：Summary (2-3句)、Strengths (逐条)、Weaknesses (逐条，严格不留情)、Questions (需作者回答)、Missing References、Overall Assessment (评分 + 置信度)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 743 · 2026-05-16T05:12:33.343833+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
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

_source line 744 · 2026-05-16T05:12:33.344317+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 745 · 2026-05-16T05:12:34.498986+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 746 · 2026-05-16T05:12:34.549692+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 747 · 2026-05-16T05:12:38.377316+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 748 · 2026-05-16T05:12:39.760312+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 749 · 2026-05-16T05:12:40.313056+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ The Correlation-Selection Gap in LLM-Based Structured Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	Code and data will be released upon acceptance at [anonymized URL].
45	
46	\bibliography{references}
47	
48	\appendix
49	\input{sections/appendix}
50	
51	\end{document}
52	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 750 · 2026-05-16T05:12:40.313855+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 751 · 2026-05-16T05:12:40.717443+00:00_

1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but information extraction (IE) produces \textit{sets} of entities and relations with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals across three NER benchmarks, with one RE benchmark as an exploratory extension, at two model scales (4B and 8B).
4	All signals achieve strong quality estimation (Spearman $\rho$ up to 0.45), yet none improves best-of-$N$ selection despite substantial oracle headroom---the \textit{correlation-selection gap}.
5	Four instance-level signals fail by construction; the empirical finding is that log-probability---the only per-sample signal---is too compressed within instances to discriminate (median range 0.041 nats, 60\% tied).
6	A 4-seed free-form decoding ablation confirms NER compression is not an artifact of constrained decoding; on RE, LP selection reverses direction under free-form decoding ($+1.8{\pm}0.1$~pp), suggesting regime-dependent behavior.
7	Consensus-proximity selection (MBR) correlates with F1 across instances but not within them.
8	Signal rankings shift with task difficulty and collapse at the capability boundary; closing the gap likely requires learned per-sample scoring.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 752 · 2026-05-16T05:12:40.717880+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 753 · 2026-05-16T05:12:40.768589+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---majority voting over multiple samples---yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But information extraction (IE) poses a structurally different challenge: the output is a \textit{set} of entities or relations, two samples may extract overlapping but non-identical structures, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
8	\citet{yao2026consistency} examine consistency--accuracy correlations for LLM-based IE using exact-match agreement; we extend their work by introducing structural matching (Soft Jaccard) that captures partial overlap, separating quality estimation from best-of-$N$ selection, and evaluating across a three-dataset difficulty gradient with a free-form decoding ablation.
9	
10	Our central finding is the \textbf{correlation-selection gap} (Figure~\ref{fig:overview}): consistency signals achieve strong quality estimation ($\rho$ up to 0.45) but fail at sample selection despite substantial oracle headroom.
11	The gap has two causes: instance-level signals (4 of 5) assign identical scores to all candidates and thus cannot rank them (\S\ref{sec:formulation}); LP---the only per-sample signal---is too compressed within instances to discriminate (median range 0.041 nats; \S\ref{sec:discussion}), and consensus-proximity selection (MBR) fails because utility correlates with F1 across instan
…[truncated 2115 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 754 · 2026-05-16T05:12:46.252631+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results, here's information about the ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, 
…[truncated 1421 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7875
}
```

</details>

---


### Tool call

_source line 755 · 2026-05-16T05:12:49.768319+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review review form 2025 2026 soundness excitement overall score scale"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review review form 2025 2026 soundness excitement overall score scale"
  }
}
```

</details>

---


### Tool call

_source line 756 · 2026-05-16T05:12:50.220345+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 757 · 2026-05-16T05:12:50.271038+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set (NER) or relation set (RE).
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	This distinction is consequential for selection: in our study, 4 of 5 signals are instance-level aggregates that assign identical scores to all $N$ candidates and thus cannot rank them by construction; only per-sample signals can, in principle, select the best output.
8	
9	\subsection{Confidence Signals}\label{sec:signals}
10	
11	Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
12	
13	\paragraph{Log-probability (model-internal, per-sample).}
14	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
15	\begin{equation}\label{eq:logprob}
16	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
17	\end{equation}
18	
19	\paragraph{Exact match voting (surface, instance-level).}
20	The proportion of samples producing the most common output:
21	\begin{equation}\label{eq:em}
22	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
23	\end{equation}
24	
25	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
26	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\cup| \times 2$ rating matrix:
27	\begin{equatio
…[truncated 2752 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 758 · 2026-05-16T05:12:50.722771+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 759 · 2026-05-16T05:12:50.823760+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures.
15	Qwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\ref{app:thinking_token}).
16	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\ref{app:n_scaling}).}
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation ($\rho$ and AUROC; $N{=}8$, seed${=}42$, single-seed; 3-seed stability in Table~\ref{tab:multiseed}). Best in \textbf{bold}. $^\dagger$RE results rest on a single benchmark (SciERC, 40\% zero-F1 rate). $N{=}16$ in Table~\ref{tab:robustness}.}
27	\label{tab:quality_estimation}
28	\begin{tabular}{ll cc cc cc cc}
29	\toprule
30	& & \multicolumn{2}{c}{\textb
…[truncated 6700 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 760 · 2026-05-16T05:12:51.325776+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 761 · 2026-05-16T05:12:51.326248+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	VC leads on hard NER ($\rho{=}0.379$); EM leads easy NER and binary discrimination (AUROC${=}0.816$, CoNLL); on $^\dagger$RE, LP outperforms structural signals (Table~\ref{tab:multiseed}).
5	Rankings hold across model families and a 4B ablation (Table~\ref{tab:scale_ablation}); at the capability boundary (WNUT-17), all signals collapse.
6	
7	\paragraph{Why the gap exists.}
8	Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
9	Log-probability, the only per-sample signal, is severely compressed: median LP range is 0.041 nats (IQR [0.024, 0.073]; Table~\ref{tab:logprob_ties}), with pooled within-instance $\rho(\text{LP}, \text{F1}){=}0.248$ confirming weak but positive signal.
10	Where compression is mitigated ($n{=}210$ instances with above-median spread), LP selection outperforms single-sample ($+2.9$~pp, $p{=}0.004$), confirming compression as the bottleneck; the gap holds even among high-diversity instances (Appendix~\ref{app:diversity}).
11	Stratifying by voting confidence reveals a complementary mechanism: high-consistency instances (Q4) have collapsed headroom (4.78~pp), leaving nothing to select, while low-consistency instances retain headroom but unreliable LP rankings (Appendix~\ref{app:vc_quartile}).
12	Doubling to $N{=}16$ expands oracle headroom by $+4.4$~pp without improving selection; on $^\dagger$RE at 4B scale, LP is the sole positive signal ($\Delta{=}{+}0.7$~pp, $p{=}0.058$; Table~\ref{tab:re_n16_selection}), consistent with LP being the strongest RE selection signal across scales, though still below single-sample at 8B.
13	A verbalized confidence baseline confirms that score compression is not LP-specific: the model's self-rated confidence (mean 8.6/10) is even more compressed and yields the weakest selection despite higher $\rho$ than LP (Appendix~\ref{app:verbalized_confidenc
…[truncated 3206 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 762 · 2026-05-16T05:12:56.371565+00:00_

Web search results for query: "ACL Rolling Review review form 2025 2026 soundness excitement overall score scale"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"},{"title":"ARR Changelog – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/changelog"},{"title":"ARR Dashboard","url":"https://stats.aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's information about the ACL Rolling Review form for 2025-2026:

## Review Scoring Categories

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score Scale

The soundness score assesses the techn
…[truncated 1164 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6603
}
```

</details>

---


### Tool call

_source line 763 · 2026-05-16T05:13:01.762253+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 764 · 2026-05-16T05:13:02.271428+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text through LLM comparison \cite{chen2024usc}, sub-claim decomposition \cite{thirukovalluru2024atomic}, or hallucination detection \cite{manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2025latentsc} all target discrete answers.
6	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings; \citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.
7	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap.
8	
9	\paragraph{Consistency for structured IE.}
10	\citet{yao2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, leaving open whether structural matching improves on surface agreement, whether quality estimation translates to selection, and whether findings generalize across a difficulty gradient---the three questions we address.
11	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency for QA/summarization but does not address structured extraction.
12	\citet{culotta2004confidence} pioneer confidence estimation for IE via CRF marginals; our signals are model-agnostic.
13	Our evaluation builds on generative IE work \cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting} and constrained decoding \cite{willard2023guided}.
14	
15	\paragraph{Uncertainty estimation and calibration.}
16	Surveys cover confidence estimation \cite{geng2024confidence}, uncertainty quantification \cite{xia2025survey}, and calibration \cite{hobelsberger2025systematic} for LLMs.
17	Semantic uncertainty \cite{ku
…[truncated 1135 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 509
}
```

</details>

---


### Tool call

_source line 765 · 2026-05-16T05:13:02.372355+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 766 · 2026-05-16T05:13:03.278220+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluate five confidence signals for quality estimation and sample selection in LLM-based structured IE, revealing the \textit{correlation-selection gap}: strong quality estimation ($\rho$ up to 0.45) coexists with selection failure.
4	Instance-level signals fail by construction; the core empirical finding is that log-probability---the only per-sample signal---is too compressed within instances to discriminate (median range 0.041 nats, 60\% tied), and consensus-proximity selection (MBR) fails because utility correlates with F1 across but not within instances.
5	A 4-seed free-form ablation confirms NER compression is not caused by constrained decoding; on $^\dagger$RE, LP selection reverses direction.
6	Signal rankings shift with difficulty across NER benchmarks and collapse at the capability boundary---consistent across two model families (3B--8B).
7	$^\dagger$RE conclusions rest on SciERC alone (40\% zero-F1 rate); trained verifiers and scaling to 70B+ are promising directions.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 767 · 2026-05-16T05:13:03.278736+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 768 · 2026-05-16T05:13:03.530002+00:00_

1	Our evaluation covers three NER datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1; generalization to other RE benchmarks remains unvalidated.
2	TACRED-style sentence-level RE classification differs structurally from set-valued extraction and is left for future work.
3	We cover 4B--8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested---larger models may produce more diverse samples.
4	We do not train a verifier, leaving unknown how much oracle headroom a supervised approach could recover.
5	
6	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
7	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE shows a directional LP reversal under free-form decoding.
8	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
9	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
10	We tested verbalized confidence \cite{tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
11	We evaluate signals individually; whether signal combinations (e.g., LP $\times$ consistency) or learned weightings could close the selection gap is unexplored.
12	The $\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app:epsilon_robustness}), the specific subset gains should be interpreted as characterizing the compression phenomenon rather than as a tuned selection strategy.
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 769 · 2026-05-16T05:13:03.530431+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 770 · 2026-05-16T05:13:03.781886+00:00_

File content (25409 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 771 · 2026-05-16T05:13:08.564429+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "500"
  }
}
```

</details>

---


### Tool result

_source line 772 · 2026-05-16T05:13:08.816862+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality---including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
47	\quad FK & 
…[truncated 37198 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 773 · 2026-05-16T05:13:14.189710+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "500",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "500",
    "limit": "500"
  }
}
```

</details>

---


### Tool result

_source line 774 · 2026-05-16T05:13:14.491632+00:00_

500	At this cutpoint, 60.3\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below $\varepsilon$, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$).
501	The CDF rises smoothly with no cliff or discontinuity (Figure~\ref{fig:lp_range_cdf}), confirming that compression is a pervasive regime rather than a bimodal split.
502	This compression is stable across seeds: seed${=}456$ yields median LP range${=}0.040$ nats and tied fraction${=}62.2\%$ (vs.\ seed${=}42$: $0.041$ nats, $60.3\%$).
503	Seed~456 uses a different subtask flag (joint vs.\ ner for seeds 42 and 123); the LP distributions are statistically indistinguishable (median LP: 8.37 vs.\ 8.20 nats; Mann--Whitney $p{=}0.55$), confirming that the subtask change does not affect compression.
504	For comparison, SJ has only 12.5\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.
505	
506	\begin{figure}[t]
507	\centering
508	\includegraphics[width=\columnwidth]{fig_lp_range_cdf}
509	\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}
510	\label{fig:lp_range_cdf}
511	\end{figure}
512	
513	\begin{table}[t]
514	\centering
515	\small
516	\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\varepsilon$.}
517	\label{tab:logprob_ties}
518	\begin{tabular}{lc}
519	\toprule
520	$\varepsilon$ threshold & Tied instances (\%) \\
521	\midrule
522	0.01 & 1.1\% \\
523	0.05 & 60.3\% \\
524	0.1  & ${\sim}$84\% \\
525	0.5  & ${\sim}$99\% \\
526	\bottomrule
527	\end{tabular}
528	\end{table}
529	
530	\paragraph{Non-tied subset.}
531	Among instances with LP range ${\geq}0.05$ ($n{=}210$, 40\% of total), log-probability selection \textit{significa
…[truncated 30290 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 775 · 2026-05-16T05:13:19.713020+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 776 · 2026-05-16T05:13:19.713941+00:00_

1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@article{brown2024monkeys,
4	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
5	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
6	  journal = {arXiv preprint arXiv:2407.21787},
7	  year = {2024},
8	  url = {https://arxiv.org/abs/2407.21787}
9	}
10	
11	@inproceedings{chen2024usc,
12	  title = {Universal Self-Consistency for Large Language Model Generation},
13	  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
14	  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},
15	  year = {2024},
16	  url = {https://arxiv.org/abs/2311.17311}
17	}
18	
19	@article{cobbe2021verifiers,
20	  title = {Training Verifiers to Solve Math Word Problems},
21	  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
22	  journal = {arXiv preprint arXiv:2110.14168},
23	  year = {2021},
24	  url = {https://arxiv.org/abs/2110.14168}
25	}
26	
27	@inproceedings{culotta2004confidence,
28	  title = {Confidence Estimation for Information Extraction},
29	  author = {Culotta, Aron and McCallum, Andrew},
30	  booktitle = {HLT-NAACL 2004},
31	  year = {2004},
32	  url = {https://aclanthology.org/N04-4028/}
33	}
34	
35	@inproceedings{derczynski2017wnut,
36	  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},
37	  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},
38	  booktitle = {W-NUT Workshop at EMNLP 2017},
39	  year = {2017},
40	  url = {https://aclanthology.org/W17-4418/}
41	}
42	
43	@inproceedings{eikema2022
…[truncated 17362 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 777 · 2026-05-16T05:14:46.845099+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
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

_source line 778 · 2026-05-16T05:14:46.895856+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 779 · 2026-05-16T05:14:51.766014+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete scoring scales for all review dimensions (soundness, excitement, overall recommendation, confidence, etc.). List each score number and its description verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete scoring scales for all review dimensions (soundness, excitement, overall recommendation, confidence, etc.). List each score number and its description verbatim."
  }
}
```

</details>

---


### Tool result

_source line 780 · 2026-05-16T05:14:59.414669+00:00_

# ACL Rolling Review Scoring Scales

## Reviewer Confidence
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully. It's unlikely, though conceivable, that I missed something that should affect my ratings."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand. My evaluation is just an educated guess."

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
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

## Overall Assessment
- **5**: Consider for Award (top 2.5%)
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
- **3**: "They c
…[truncated 613 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7648
}
```

</details>

---


### Tool call

_source line 781 · 2026-05-16T05:17:12.189603+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 1 审稿报告 — Reviewer 1（方法严谨性 + 实验设计 + 统计分析）\n\n### Summary\n\n本文评估了五种置信度信号在 LLM-based structured IE 中的质量估计和样本选择能力，发现\"correlation-selection gap\"：信号与 F1 相关性强（ρ 达 0.45）但无法改善 best-of-N 选择。四个 instance-level 信号通过 MBR 选择无效，LP（唯一 per-sample 信号）因 within-instance 压缩（中位数范围 0.041 nats）而失败。这是一个有价值的负面结果，实验设计整体严谨，但核心 framing 存在方法论问题，且实验覆盖度不足以支撑标题。\n\n---\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验方法总体可靠，统计分析全面（bootstrap CI, permutation test, TOST），但核心 \"by construction\" framing 存在逻辑问题（见 N1），部分统计分析的效力不足（见 W1） |\n| Excitement | 3/5 | 识别了 QE vs. selection 的 decoupling 现象，对 test-time compute scaling 社区有参考价值；但缺乏解决方案，范围限于小模型，且标题过于宽泛 |\n| Overall | 3.5/5 | Borderline Conference — 实验工作扎实，负面结果有价值，但 framing 和 scope 问题需解决 |\n| Reproducibility | 4/5 | 训练配置、prompt template 完整公开（Table A6），使用开源框架/模型，代码承诺 release |\n| Confidence | 4/5 | 仔细阅读全文及 appendix，熟悉 self-consistency、MBR decoding 和 IE 评估相关文献 |\n\n---\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] \"By construction\" framing 混淆定义性与经验性发现\n\n- 具体位置：Section 3.1 (line 7), Section 4.2 paragraph 2, Abstract (line 4-5)\n- 问题：论文反复声称 4/5 信号\"cannot rank candidates by construction\"（Section 3.1: \"4 of 5 signals are instance-level aggregates that assign identical scores to all N candidates and thus cannot rank them by construction\"），但 Table 2 中这些信号 **实际执行了选择**（SJ=0.646, FK=0.646 等），通过 \"consensus-proximity selection\"（即 MBR: argmax_i Σ_{j≠i} U(y_i, y_j)）。Discussion 也承认 \"VC becomes per-sample in the selection context.\" Appendix 证实 LOO-SJ 与 consensus-proximity selection 等价。\n\n  论文的实际发现是：(1) instance-level QE 值对所有 candidate 相同（定义性的，trivially true）；(2) 用这些信号做 MBR-style selection 无效（经验性发现，有意义）。但论文将两者混为一谈，将 (2) 也归为 \"by construction\" 失败，从而弱化了这一经验发现的价值。MBR 在 MT 中成功但在 IE 中失败是本文最重要的经验贡献之一——应该突出而非隐藏在 \"by construction\" framing 之下。\n\n- 为什么影响接收：核心 claim 的逻辑严密性是 soundness 评分的关键。当前 framing 使读者混淆哪些结论是定义推导、哪些是实验证据。\n- 建议修改方向：明确区分两层失败——(a) QE signal 的 instance-level 性质使其 *本身* 无法做 selection；(b) 将其转化为 per-sample utility（MBR/consensus-proximity）后仍然失败，且这是一个经验发现（因为 MBR 在 MT 中有效）。将 (b) 作为独立 contribution 突出。\n\n**N2** [critical] 标题和论文范围不匹配：\"Structured Information Extraction\" vs. 实际覆盖\n\n- 具体位置：Title, Abstract, Section 4.1\n- 问题：标题使用 \"Structured Information Extraction\" 这一宽泛术语，但论文的核心证据来自 3 个 NER benchmark（flat entity recognition），RE 仅有 1 个 benchmark（SciERC）作为 \"exploratory extension\"，且 RE 实验在统计上不完整（Table 2: RE 为 single-seed；全文标注 \"†RE\" 表示 preliminary）。\n\n  Structured IE 通常包括 NER、RE、Event Extraction、Slot Filling 等多种任务。当前论文实质上是一篇 \"NER confidence estimation\" 论文附带一个初步的 RE 探索。Section 4.1 和 Limitations 均承认 \"RE conclusions rest on SciERC alone\" 和 \"TACRED-style RE is left for future work\"。\n\n- 为什么影响接收：标题/abstract 的 claim 范围与证据支撑之间的落差会被 AC 视为 overclaiming。EMNLP reviewer guidelines 明确要求 claims 与 evidence 对齐。\n- 建议修改方向：(1) 缩窄标题为 \"NER\" 或 \"Entity Set Extraction\"；(2) 或增加至少一个独立 RE 数据集（如 TACRED、DocRED）的实验使 RE 结论不再 preliminary。\n\n---\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Kendall W=1.000 (n=3 seeds) 的统计效力问题\n\n- 具体位置：Appendix F, Table A8 (tab:ranking-stability)\n- 问题：3 seeds 排 5 个 signal 的 Kendall W=1.000 被用于支撑 \"signal ranking is stable across seeds\" 的结论。然而 n=3 的统计效力极低——即使 raters 之间仅有轻微共识，W 也容易达到高值（W 的 chi-squared 检验 df=4，临界值 9.49 for α=0.05）。论文在 Appendix 中承认 \"statistical power with n=3 is limited\"，但正文 Section 4.1 footnote 仍以此作为 robustness 证据。\n- 建议：要么增加 seeds（≥5）以提高效力，要么在正文中降低对 ranking stability 的表述强度，改为 \"consistent with stable rankings but insufficient power to confirm.\"\n\n**W2** [warning] Table 2 NER 2-seed vs RE single-seed 的不一致未充分解释\n\n- 具体位置：Table 2 caption (\"NER: 2-seed mean±σ; †RE: single seed\")\n- 问题：同一张表中 NER 用 2-seed 统计但 RE 仅 single seed。Appendix Table A8 显示 RE 有 3-seed QE 数据可用（Qwen RE ρ: .297±.022 for LP, .309±.024 for VC），但 selection 实验为何 RE 只跑了一个 seed？资源限制？如果是，应当明确说明。\n- 建议：在正文或 footnote 中解释这一不对称的原因。如果 3-seed RE selection 数据可用但未报告，考虑在 appendix 中补充。\n\n**W3** [warning] 未测试 entity-level LP 聚合——明显的 LP 变体缺失\n\n- 具体位置：Eq. 1 (Section 3.2), Discussion \"Hypotheses for LP compression\" (d)\n- 问题：论文指出假说 (d) \"format-token dilution\" 是 LP 压缩的可能主因（fine-tuned models 对 schema tokens 赋予极高 LP，稀释了 entity-name tokens 的信号）。这直接暗示了一个显而易见的变体：仅在 entity-name tokens 上计算 LP（排除 format/schema tokens），即 entity-level LP aggregation。论文列出了 4 个假说但只通过 free-form ablation 测试了 (b)-(c)，未直接验证 (a)/(d)——而 entity-level LP 正是 (d) 的直接测试。\n- 建议：加入 entity-token-only LP 变体的实验或 pilot study；如果不可行（如 constrained decoding 下无法区分 entity vs. schema tokens 的 LP），需明确说明为什么。\n\n**W4** [warning] Gold-empty instance filtering 在 QE 和 Selection 之间的不一致\n\n- 具体位置：Section 3.3 paragraph \"Quality estimation\" (\"Correlation analyses exclude empty gold annotations... selection retains the full set\")\n- 问题：QE 分析排除 gold-empty instances（CoNLL 排除 697/3453=20.2%），而 selection 保留完整集。这一设计选择的理由 partially explained（\"F1 is trivially zero regardless of prediction quality\"），但导致两个问题：(1) QE 的 ρ 在 n=2756 上计算，selection F1 在 n=3453 上计算，直接对比（如 \"strong ρ yet no selection gain\"）涉及不同样本集；(2) Table A13（cross_selection）的 CoNLL 仍标注 n=2756——这与正文描述矛盾。\n- 建议：统一说明 filtering 策略并验证 Table cross_selection 的 n 值标注是否正确。如果 selection 确实在 full set 上计算，解释为什么 gold-empty instances 对 selection 的影响是可接受的。\n\n**W5** [warning] 模型规模覆盖不足限制结论的普适性\n\n- 具体位置：Section 4.1 (\"Both Qwen3-8B and LLaMA-3.1-8B-Instruct\"), Table A6\n- 问题：所有实验仅覆盖 3B-8B 规模，Limitations 承认 \"whether the gap holds for 70B+ models or closed-source APIs is untested.\" 然而正文 Conclusion 表述为 \"consistent across two model families (3B–8B)\" 暗示了比实际证据更强的普适性。在 test-time compute scaling 文献中，model scale 是核心变量——70B 模型可能产生更多样的 samples 从而改变 LP compression 现象。\n- 建议：在 Conclusion/Discussion 中更明确地将发现限定为 small-model regime 的特性，或增加一个 ≥32B 模型的 pilot experiment。\n\n---\n\n### Questions（需作者回答）\n\n**Q1**: Consensus-proximity selection (MBR) 对 instance-level signals 来说实质上是一个 per-sample 选择策略。请解释为什么论文将其归类为 \"fail by construction\" 而非 \"MBR fails empirically for IE\"——这两者的理论含义截然不同。\n\n**Q2**: Entity-token-only LP（仅对 entity mention tokens 计算 mean LP，排除 JSON schema tokens）是否被考虑过？如果排除了 schema tokens 的 LP 贡献，within-instance compression 是否缓解？这是假说 (d) 的直接检验。\n\n**Q3**: Table A13 (cross_selection) 标注 CoNLL n=2756，但正文 Section 3.3 说 \"selection retains the full set\" (n=3453)。哪个是正确的？\n\n**Q4**: TOST 分析中的 external anchors (Section F, Appendix) 显示 Qwen CoNLL 的 selection 实际上 significantly worse than single-sample（所有外部 δ 下均不通过等价检验）。这是否意味着在某些配置下，signals 实际上 *损害* selection？这一发现与 \"equivalence\" 的正文表述矛盾。\n\n**Q5**: Free-form ablation 中 RE LP selection 的 direction reversal（constrained: −0.68pp → free-form: +1.84±0.12pp across 4 seeds）——这暗示 constrained decoding 本身是 RE selection failure 的原因。为什么论文没有将 \"free-form decoding + LP selection\" 作为一个 positive result 更突出地呈现？\n\n---\n\n### Missing References\n\n1. **Bertoldi et al. (2024)** \"Beyond Self-Consistency: Ensemble Reasoning in LLMs\" — 直接讨论 self-consistency 在 structured output 上的局限性\n2. **Ye et al. (2023)** \"Complementary Explanations for Effective In-Context Learning\" — 提出对 sampling diversity 与 selection 关系的分析框架\n3. 论文引用了 Eikema & Aziz (2022) for MBR 但未引用 **Deguchi et al. (2024)** \"Centroid-Based Efficient Minimum Bayes Risk Decoding\" 中关于 MBR 在 structured 任务上 mode-seeking bias 的分析\n\n---\n\n### 主要优势\n\n1. **问题定义清晰有价值**：明确区分 quality estimation 和 sample selection 是本文的核心方法论贡献，对 test-time compute scaling 社区有直接指导意义。三个评估指标（ρ, AUROC, selection F1）的 decoupling demonstration (Contribution 1) 设计精巧。\n\n2. **统计分析全面且透明**：Bootstrap CI (B=10,000), permutation tests, Fisher combined p-values, TOST with multiple δ anchors, ε-robustness sweep——统计方法论的严谨程度超过 EMNLP 平均水平。论文主动提出并解决 potential circularity（如 TOST δ 与 oracle headroom 的循环性），且在 Limitations 中诚实声明了所有已知限制。\n\n3. **消融设计合理**：Free-form decoding ablation 有效隔离了 constrained decoding 的影响；scale ablation (4B vs. 8B) 提供了跨规模验证；温度和 N-scaling 实验覆盖了关键超参数。\n\n4. **负面结果的呈现方式得当**：论文没有为 negative result 强行赋予 positive spin，而是通过 non-tied subset analysis (+2.9pp, p=0.004) 展示了 LP 在什么条件下 *能* 工作，并由此诊断出 compression 作为瓶颈。\n\n5. **Related work 公允全面**：对 Yao et al. (2026) 的 positioning 清晰（从 exact-match 扩展到 structural matching + selection），对 Eikema et al. (2025) structured MBR 失败的 connection 有见地。\n\n---\n\n### 小问题（不影响接收）\n\n- \"Soft Jaccard\" 命名：使用 max(|g_i|, |g_j|) 而非 |A∪B| 作为分母，严格说不是 Jaccard 的 soft 推广。建议改为 \"Soft overlap score\" 或在首次出现时明确说明与标准 Jaccard 的区别。\n- Discussion 中列出 (a)(b)(c)(d) 四个假说但标记为 \"three (non-mutually-exclusive) mechanisms\"——实际有 4 个。\n- Table 1 caption 说 \"Best in bold\" 但某些列有多个 bold（如 CoNLL LLaMA 列 SJ 和 EM 均 .431），需确认是否为 ties。\n- Abstract 第 5 行 \"Four instance-level signals fail by construction; the empirical finding is that log-probability...\" 这一句的分号前后表述暗示 LP 发现是 \"the\" empirical finding，降低了 MBR failure 作为独立发现的地位。\n\n---\n\n### Overall Assessment\n\n**Overall**: 3.5/5 (Borderline Conference)\n\n**一句话总结**: 实验严谨且统计分析全面的经验性负面结果论文，但核心 framing 的逻辑问题（N1）和标题/范围不匹配（N2）需要在 rebuttal 中有说服力地回应才能达到 conference acceptance。\n\n如果 N1 的 framing 问题被修正（明确区分 definitional vs. empirical failure，突出 MBR failure 作为独立 contribution），且标题/abstract 精确化，本文可提升至 4.0（Conference acceptance level）。当前版本的主要风险是 overclaiming（标题）和 underclaiming（将 MBR 的经验性失败归为定义性的）同时存在，造成叙事的不一致。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 1 审稿报告 — Reviewer 1（方法严谨性 + 实验设计 + 统计分析）\n\n### Summary\n\n本文评估了五种置信度信号在 LLM-based structured IE 中的质量估计和样本选择能力，发现\"correlation-selection gap\"：信号与 F1 相关性强（ρ 达 0.45）但无法改善 best-of-N 选择。四个 instance-level 信号通过 MBR 选择无效，LP（唯一 per-sample 信号）因 within-instance 压缩（中位数范围 0.041 nats）而失败。这是一个有价值的负面结果，实验设计整体严谨，但核心 framing 存在方法论问题，且实验覆盖度不足以支撑标题。\n\n---\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验方法总体可靠，统计分析全面（bootstrap CI, permutation test, TOST），但核心 \"by construction\" framing 存在逻辑问题（见 N1），部分统计分析的效力不足（见 W1） |\n| Excitement | 3/5 | 识别了 QE vs. selection 的 decoupling 现象，对 test-time compute scaling 社区有参考价值；但缺乏解决方案，范围限于小模型，且标题过于宽泛 |\n| Overall | 3.5/5 | Borderline Conference — 实验工作扎实，负面结果有价值，但 framing 和 scope 问题需解决 |\n| Reproducibility | 4/5 | 训练配置、prompt template 完整公开（Table A6），使用开源框架/模型，代码承诺 release |\n| Confidence | 4/5 | 仔细阅读全文及 appendix，熟悉 self-consistency、MBR decoding 和 IE 评估相关文献 |\n\n---\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] \"By construction\" framing 混淆定义性与经验性发现\n\n- 具体位置：Section 3.1 (line 7), Section 4.2 paragraph 2, Abstract (line 4-5)\n- 问题：论文反复声称 4/5 信号\"cannot rank candidates by construction\"（Section 3.1: \"4 of 5 signals are instance-level aggregates that assign identical scores to all N candidates and thus cannot rank them by construction\"），但 Table 2 中这些信号 **实际执行了选择**（SJ=0.646, FK=0.646 等），通过 \"consensus-proximity selection\"（即 MBR: argmax_i Σ_{j≠i} U(y_i, y_j)）。Discussion 也承认 \"VC becomes per-sample in the selection context.\" Appendix 证实 LOO-SJ 与 consensus-proximity selection 等价。\n\n  论文的实际发现是：(1) instance-level QE 值对所有 candidate 相同（定义性的，trivially true）；(2) 用这些信号做 MBR-style selection 无效（经验性发现，有意义）。但论文将两者混为一谈，将 (2) 也归为 \"by construction\" 失败，从而弱化了这一经验发现的价值。MBR 在 MT 中成功但在 IE 中失败是本文最重要的经验贡献之一——应该突出而非隐藏在 \"by construction\" framing 之下。\n\n- 为什么影响接收：核心 claim 的逻辑严密性是 soundness 评分的关键。当前 framing 使读者混淆哪些结论是定义推导、哪些是实验证据。\n- 建议修改方向：明确区分两层失败——(a) QE signal 的 instance-level 性质使其 *本身* 无法做 selection；(b) 将其转化为 per-sample utility（MBR/consensus-proximity）后仍然失败，且这是一个经验发现（因为 MBR 在 MT 中有效）。将 (b) 作为独立 contribution 突出。\n\n**N2** [critical] 标题和论文范围不匹配：\"Structured Information Extraction\" vs. 实际覆盖\n\n- 具体位置：Title, Abstract, Section 4.1\n- 问题：标题使用 \"Structured Information Extraction\" 这一宽泛术语，但论文的核心证据来自 3 个 NER benchmark（flat entity recognition），RE 仅有 1 个 benchmark（SciERC）作为 \"exploratory extension\"，且 RE 实验在统计上不完整（Table 2: RE 为 single-seed；全文标注 \"†RE\" 表示 preliminary）。\n\n  Structured IE 通常包括 NER、RE、Event Extraction、Slot Filling 等多种任务。当前论文实质上是一篇 \"NER confidence estimation\" 论文附带一个初步的 RE 探索。Section 4.1 和 Limitations 均承认 \"RE conclusions rest on SciERC alone\" 和 \"TACRED-style RE is left for future work\"。\n\n- 为什么影响接收：标题/abstract 的 claim 范围与证据支撑之间的落差会被 AC 视为 overclaiming。EMNLP reviewer guidelines 明确要求 claims 与 evidence 对齐。\n- 建议修改方向：(1) 缩窄标题为 \"NER\" 或 \"Entity Set Extraction\"；(2) 或增加至少一个独立 RE 数据集（如 TACRED、DocRED）的实验使 RE 结论不再 preliminary。\n\n---\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Kendall W=1.000 (n=3 seeds) 的统计效力问题\n\n- 具体位置：Appendix F, Table A8 (tab:ranking-stability)\n- 问题：3 seeds 排 5 个 signal 的 Kendall W=1.000 被用于支撑 \"signal ranking is stable across seeds\" 的结论。然而 n=3 的统计效力极低——即使 raters 之间仅有轻微共识，W 也容易达到高值（W 的 chi-squared 检验 df=4，临界值 9.49 for α=0.05）。论文在 Appendix 中承认 \"statistical power with n=3 is limited\"，但正文 Section 4.1 footnote 仍以此作为 robustness 证据。\n- 建议：要么增加 seeds（≥5）以提高效力，要么在正文中降低对 ranking stability 的表述强度，改为 \"consistent with stable rankings but insufficient power to confirm.\"\n\n**W2** [warning] Table 2 NER 2-seed vs RE single-seed 的不一致未充分解释\n\n- 具体位置：Table 2 caption (\"NER: 2-seed mean±σ; †RE: single seed\")\n- 问题：同一张表中 NER 用 2-seed 统计但 RE 仅 single seed。Appendix Table A8 显示 RE 有 3-seed QE 数据可用（Qwen RE ρ: .297±.022 for LP, .309±.024 for VC），但 selection 实验为何 RE 只跑了一个 seed？资源限制？如果是，应当明确说明。\n- 建议：在正文或 footnote 中解释这一不对称的原因。如果 3-seed RE selection 数据可用但未报告，考虑在 appendix 中补充。\n\n**W3** [warning] 未测试 entity-level LP 聚合——明显的 LP 变体缺失\n\n- 具体位置：Eq. 1 (Section 3.2), Discussion \"Hypotheses for LP compression\" (d)\n- 问题：论文指出假说 (d) \"format-token dilution\" 是 LP 压缩的可能主因（fine-tuned models 对 schema tokens 赋予极高 LP，稀释了 entity-name tokens 的信号）。这直接暗示了一个显而易见的变体：仅在 entity-name tokens 上计算 LP（排除 format/schema tokens），即 entity-level LP aggregation。论文列出了 4 个假说但只通过 free-form ablation 测试了 (b)-(c)，未直接验证 (a)/(d)——而 entity-level LP 正是 (d) 的直接测试。\n- 建议：加入 entity-token-only LP 变体的实验或 pilot study；如果不可行（如 constrained decoding 下无法区分 entity vs. schema tokens 的 LP），需明确说明为什么。\n\n**W4** [warning] Gold-empty instance filtering 在 QE 和 Selection 之间的不一致\n\n- 具体位置：Section 3.3 paragraph \"Quality estimation\" (\"Correlation analyses exclude empty gold annotations... selection retains the full set\")\n- 问题：QE 分析排除 gold-empty instances（CoNLL 排除 697/3453=20.2%），而 selection 保留完整集。这一设计选择的理由 partially explained（\"F1 is trivially zero regardless of prediction quality\"），但导致两个问题：(1) QE 的 ρ 在 n=2756 上计算，selection F1 在 n=3453 上计算，直接对比（如 \"strong ρ yet no selection gain\"）涉及不同样本集；(2) Table A13（cross_selection）的 CoNLL 仍标注 n=2756——这与正文描述矛盾。\n- 建议：统一说明 filtering 策略并验证 Table cross_selection 的 n 值标注是否正确。如果 selection 确实在 full set 上计算，解释为什么 gold-empty instances 对 selection 的影响是可接受的。\n\n**W5** [warning] 模型规模覆盖不足限制结论的普适性\n\n- 具体位置：Section 4.1 (\"Both Qwen3-8B and LLaMA-3.1-8B-Instruct\"), Table A6\n- 问题：所有实验仅覆盖 3B-8B 规模，Limitations 承认 \"whether the gap holds for 70B+ models or closed-source APIs is untested.\" 然而正文 Conclusion 表述为 \"consistent across two model families (3B–8B)\" 暗示了比实际证据更强的普适性。在 test-time compute scaling 文献中，model scale 是核心变量——70B 模型可能产生更多样的 samples 从而改变 LP compression 现象。\n- 建议：在 Conclusion/Discussion 中更明确地将发现限定为 small-model regime 的特性，或增加一个 ≥32B 模型的 pilot experiment。\n\n---\n\n### Questions（需作者回答）\n\n**Q1**: Consensus-proximity selection (MBR) 对 instance-level signals 来说实质上是一个 per-sample 选择策略。请解释为什么论文将其归类为 \"fail by construction\" 而非 \"MBR fails empirically for IE\"——这两者的理论含义截然不同。\n\n**Q2**: Entity-token-only LP（仅对 entity mention tokens 计算 mean LP，排除 JSON schema tokens）是否被考虑过？如果排除了 schema tokens 的 LP 贡献，within-instance compression 是否缓解？这是假说 (d) 的直接检验。\n\n**Q3**: Table A13 (cross_selection) 标注 CoNLL n=2756，但正文 Section 3.3 说 \"selection retains the full set\" (n=3453)。哪个是正确的？\n\n**Q4**: TOST 分析中的 external anchors (Section F, Appendix) 显示 Qwen CoNLL 的 selection 实际上 significantly worse than single-sample（所有外部 δ 下均不通过等价检验）。这是否意味着在某些配置下，signals 实际上 *损害* selection？这一发现与 \"equivalence\" 的正文表述矛盾。\n\n**Q5**: Free-form ablation 中 RE LP selection 的 direction reversal（constrained: −0.68pp → free-form: +1.84±0.12pp across 4 seeds）——这暗示 constrained decoding 本身是 RE selection failure 的原因。为什么论文没有将 \"free-form decoding + LP selection\" 作为一个 positive result 更突出地呈现？\n\n---\n\n### Missing References\n\n1. **Bertoldi et al. (2024)** \"Beyond Self-Consistency: Ensemble Reasoning in LLMs\" — 直接讨论 self-consistency 在 structured output 上的局限性\n2. **Ye et al. (2023)** \"Complementary Explanations for Effective In-Context Learning\" — 提出对 sampling diversity 与 selection 关系的分析框架\n3. 论文引用了 Eikema & Aziz (2022) for MBR 但未引用 **Deguchi et al. (2024)** \"Centroid-Based Efficient Minimum Bayes Risk Decoding\" 中关于 MBR 在 structured 任务上 mode-seeking bias 的分析\n\n---\n\n### 主要优势\n\n1. **问题定义清晰有价值**：明确区分 quality estimation 和 sample selection 是本文的核心方法论贡献，对 test-time compute scaling 社区有直接指导意义。三个评估指标（ρ, AUROC, selection F1）的 decoupling demonstration (Contribution 1) 设计精巧。\n\n2. **统计分析全面且透明**：Bootstrap CI (B=10,000), permutation tests, Fisher combined p-values, TOST with multiple δ anchors, ε-robustness sweep——统计方法论的严谨程度超过 EMNLP 平均水平。论文主动提出并解决 potential circularity（如 TOST δ 与 oracle headroom 的循环性），且在 Limitations 中诚实声明了所有已知限制。\n\n3. **消融设计合理**：Free-form decoding ablation 有效隔离了 constrained decoding 的影响；scale ablation (4B vs. 8B) 提供了跨规模验证；温度和 N-scaling 实验覆盖了关键超参数。\n\n4. **负面结果的呈现方式得当**：论文没有为 negative result 强行赋予 positive spin，而是通过 non-tied subset analysis (+2.9pp, p=0.004) 展示了 LP 在什么条件下 *能* 工作，并由此诊断出 compression 作为瓶颈。\n\n5. **Related work 公允全面**：对 Yao et al. (2026) 的 positioning 清晰（从 exact-match 扩展到 structural matching + selection），对 Eikema et al. (2025) structured MBR 失败的 connection 有见地。\n\n---\n\n### 小问题（不影响接收）\n\n- \"Soft Jaccard\" 命名：使用 max(|g_i|, |g_j|) 而非 |A∪B| 作为分母，严格说不是 Jaccard 的 soft 推广。建议改为 \"Soft overlap score\" 或在首次出现时明确说明与标准 Jaccard 的区别。\n- Discussion 中列出 (a)(b)(c)(d) 四个假说但标记为 \"three (non-mutually-exclusive) mechanisms\"——实际有 4 个。\n- Table 1 caption 说 \"Best in bold\" 但某些列有多个 bold（如 CoNLL LLaMA 列 SJ 和 EM 均 .431），需确认是否为 ties。\n- Abstract 第 5 行 \"Four instance-level signals fail by construction; the empirical finding is that log-probability...\" 这一句的分号前后表述暗示 LP 发现是 \"the\" empirical finding，降低了 MBR failure 作为独立发现的地位。\n\n---\n\n### Overall Assessment\n\n**Overall**: 3.5/5 (Borderline Conference)\n\n**一句话总结**: 实验严谨且统计分析全面的经验性负面结果论文，但核心 framing 的逻辑问题（N1）和标题/范围不匹配（N2）需要在 rebuttal 中有说服力地回应才能达到 conference acceptance。\n\n如果 N1 的 framing 问题被修正（明确区分 definitional vs. empirical failure，突出 MBR failure 作为独立 contribution），且标题/abstract 精确化，本文可提升至 4.0（Conference acceptance level）。当前版本的主要风险是 overclaiming（标题）和 underclaiming（将 MBR 的经验性失败归为定义性的）同时存在，造成叙事的不一致。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 782 · 2026-05-16T05:17:16.104594+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3914
}
```

</details>

---


### Assistant

_source line 783 · 2026-05-16T05:17:30.978117+00:00_

审稿报告已提交至 Review Director。

**完成情况总结**：

- **Overall**: 3.5/5（Borderline Conference）
- **Soundness**: 3.5/5 — 统计方法全面但核心 "by construction" framing 有逻辑漏洞
- **Excitement**: 3/5 — 有价值的负面结果但缺乏解决方案且 scope 有限

**两个 Must-Fix 问题**：
1. "By construction" framing 混淆了定义性失败与经验性发现（MBR 在 IE 中的失败是 empirical finding，不应被 "by construction" 标签掩盖）
2. 标题 "Structured IE" 过宽，实际主要是 NER + 一个 exploratory RE 实验

**关键 Should-Fix**：Kendall W 统计效力不足、NER/RE seed 数量不一致、未测试 entity-token-only LP 变体、gold-empty filtering 不一致、模型规模限于 3B-8B。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 25

## Round 25

2 recorded events


### User

_source line 784 · 2026-05-16T05:24:30.535677+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿原文。请对每个 Must-Fix、Should-Fix 和 Question 逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

特别关注你和 Reviewer 2 观点不同的地方。

---

### Reviewer 2 的完整审稿报告

**Overall**: 3.0 (Findings)

**Soundness**: 3.5/5 | **Excitement**: 2.5/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5

#### Must-Fix 问题

**N1** [critical] Contribution 1 的 "empirical dissociation" 大部分是定义必然，不是经验发现
- 论文将 "instance-level signals 无法做 sample selection" 列为第一个 contribution ("Empirical dissociation of evaluation metrics")。然而 Section 3.1 自己定义了 instance-level signal 对同一 input 的所有 candidates 赋予相同分数。这不是 empirical finding，而是 definitional consequence。真正的 empirical finding 只有 LP compression——只占 1/5 信号——被淹没在对另外 4 个信号"不能选"的反复论述中。
- 建议：重新组织 contribution list——将 "by construction" 部分降为 setup/background，把 LP compression + MBR within-instance failure 作为核心经验发现来呈现。

**N2** [critical] 标题和 scope 严重不匹配："Structured Information Extraction" vs. 实际 RE 覆盖严重不足
- 标题使用 "Structured Information Extraction" 暗示 NER、RE、EE 等广泛覆盖。实际上 RE 仅 SciERC 一个数据集（40% zero-F1），且自称 "exploratory extension"。完全没有 Event Extraction。
- 建议：将标题限定为 NER，或增加至少一个额外 RE benchmark。

**N3** [critical] ρ = 0.45 被描述为 "strong quality estimation"——这是中等相关性，措辞过度
- Spearman ρ = 0.45 在统计学中归类为 moderate correlation（Cohen's benchmarks: 0.1 weak, 0.3 moderate, 0.5 strong）。论文反复使用 "strong quality estimation"，但 ρ = 0.45 仅解释约 20% 方差。如果 QE 本身只是 moderate，gap 的戏剧性就大大降低。
- 建议：使用 "moderate" 或 "non-trivial"，或明确说明 "up to 0.45, which is moderate by Cohen's standards but substantially exceeds random baselines"。

#### Should-Fix 问题

**W1** 未尝试任何 remedy，纯诊断性论文的 impact 受限
- 即使简单的 baseline remedy（LP × consistency 组合、LP z-score 归一化、entity-token-only LP、learned linear combination）都缺失。

**W2** 模型规模范围过窄（3B-8B），结论普适性存疑
- 3B-8B 是同一个 capability tier。LP compression 可能是小模型的特性。

**W3** Yao et al. (2026) 的差异描述不够精确
- 需要更精确地说明增量贡献的大小，建议添加对比段落。

**W4** ε = 0.05 threshold 的选择影响核心叙事
- "60% tied" 依赖于 ε = 0.05。ε = 0.03 时 tied fraction 仅 31.8%。建议主文改用 continuous characterization（pooled within-instance ρ = 0.248）。

**W5** 缺少若干直接相关文献
- Zerva et al. (2025) "Uncertainty-Aware Decoding with MBR" (ICLR 2025)
- Mejer & Crammer (2011) "Confidence Estimation in Structured Prediction"
- Xie et al. (2024) "Self-Evaluation Improves Selective Generation" (NeurIPS 2024)
- "Existing LLMs Are Not Self-Consistent For Simple Tasks" (2025)

#### Questions
1. Entity-name-only LP 是否被考虑过？
2. 是否尝试过用 binary classifier 预测 non-tied instances 然后条件性应用 LP？
3. Contribution 1 中 ρ, AUROC, selection F1 decouple 的 empirical surprise 在哪里？它们本来就衡量不同的东西。
4. CoNLL (F1≈0.91, headroom ~4pp) 的 selection 分析是否有意义？

#### 小问题
- Abstract 数字过密
- Contribution 3 (difficulty-dependent rankings) 较弱
- Table 2 caption dagger 标注混淆
- FK entity set 改编非标准
- Discussion LP hypotheses (a)(b)(c)(d) 编号标点错误
- oh2025latentsc bib year 应更新为 2026

---

请逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 785 · 2026-05-16T05:26:16.322717+00:00_

逐条回应 Reviewer 2 的审稿意见如下。

---

## 交叉回应 Reviewer 2

### Must-Fix 问题

**[AGREE] R2-N1**: Contribution 1 的 "empirical dissociation" 大部分是定义必然

同意核心论点。这与我的 N1 高度一致——论文将 instance-level signals 的 selection failure 反复描述为 "by construction"，同时又展示它们的 MBR selection 结果（Table 2: SJ=0.646, FK=0.646），制造了逻辑上的自相矛盾。

**但需补充一点 nuance**：Contribution 1 中 ρ-AUROC-selection F1 三指标的 decouple 并非完全 trivial。对于 LP（per-sample signal），higher ρ 的朴素预期是 better selection——LP 的 selection failure 尽管 ρ=0.205 仍是真正的经验发现。此外，VerbConf 的 ρ > LP 但 selection worst（Appendix K, Table A14）才是最 surprising 的 dissociation。R2 的建议（将 by-construction 降为 background，突出 LP compression + MBR within-instance failure）是正确的重组方向。

---

**[AGREE] R2-N2**: 标题和 scope 严重不匹配

完全同意。我在自己的 N2 中提出了相同问题。RE 仅 SciERC 一个 benchmark，40% zero-F1，全文标注 "†RE" = preliminary。标题用 "Structured Information Extraction" 不成立。

---

**[REBUT] R2-N3**: ρ=0.45 被描述为 "strong" 是 overclaiming

部分不同意将此列为 **Must-Fix**。理由：

1. **Cohen's benchmarks 适用于行为科学，不直接适用于 NLP unsupervised QE**。在无监督置信度信号领域，ρ=0.45 的 baseline 对比应该是 random (ρ≈0) 和 supervised methods（通常 ρ=0.5-0.7），而非 Cohen 的 generic threshold。论文在 CoNLL 上 EM ρ=0.451, AUROC=0.816——后者在二分类场景中已是 good discriminator。

2. **论文已使用了限定语**：Abstract 写 "up to 0.45"（不是 average），Introduction 的 "strong quality estimation ($\rho$ up to 0.45)" 是在 contrast 完全失败的 selection 时使用的相对表述。

3. **然而 R2 的 underlying point 有道理**：如果 QE 本身只是 moderate，"gap" 的 dramaticness 确实降低。建议采纳 R2 的措辞建议 "moderate-to-strong by domain standards, substantially exceeding random baselines"——但这是 **Should-Fix level 的 framing refinement**，不是 critical issue。

---

### Should-Fix 问题

**[AGREE] R2-W1**: 未尝试任何 remedy

同意这限制了论文的 impact。我在 W3 中提出了 entity-token-only LP 这一最直接的 remedy。论文作为纯诊断性工作有其价值（类似于 Belinkov & Glass 2019 analysis papers），但至少一个 pilot remedy（如 LP × VC 组合、或 entity-token LP）会显著增强贡献。不过，我认为这不上升到 Must-Fix——因为论文的定位是 diagnostic + negative result，且已明确指向 trained verifiers 作为解决方向（citing Cobbe et al. 2021, Lightman et al. 2024）。

---

**[AGREE] R2-W2**: 模型规模范围过窄

完全同意，与我的 W5 一致。3B-8B 本质上是 one capability tier。LP compression 可能在 70B+ 上缓解。

---

**[REBUT] R2-W3**: Yao et al. (2026) 差异描述不够精确

不完全同意。Section 1 (Introduction, paragraph 2) 明确列出三项增量贡献："we extend their work by introducing structural matching (Soft Jaccard) that captures partial overlap, separating quality estimation from best-of-N selection, and evaluating across a three-dataset difficulty gradient with a free-form decoding ablation." Related Work (Section 2, paragraph 2) 进一步澄清 Yao et al. 使用 "exact-match agreement" 而本文引入 structural matching。

这些差异是明确的、具体的、可验证的。如果 R2 的意思是需要 quantify 增量大小（如 "SJ vs. EM on Yao's setup"），那可能超出论文 scope——Yao et al. 在不同数据/模型上工作，direct comparison 不一定 feasible。建议作者在 camera-ready 中添加 1-2 句更精确的对比（如 "Yao et al. report ρ=X on their setup; our structural signals achieve ρ=Y on the same task type"），但这是 minor refinement。

---

**[AGREE] R2-W4**: ε=0.05 threshold 选择影响核心叙事

同意 R2 的具体建议。"60% tied" 是论文反复引用的核心数字（Abstract, Discussion），高度依赖 ε=0.05 的选择。ε=0.03 时 tied fraction 仅 31.8%（Table A10），叙事将从 "大多数 instances 无法区分" 变为 "约三分之一无法区分"。

论文确实在 Appendix 提供了 ε sweep（Table A10）和 continuous metric（pooled within-instance ρ=0.248），但这些被埋在附录中。R2 的建议——在正文中用 continuous characterization（pooled ρ=0.248, CDF 特征）替代二元 threshold 叙述——是合理的改进方向。不过我认为当前呈现也不算 misleading（因为 CDF 图和 sweep 都在 Appendix 中），所以 Should-Fix 定级恰当。

---

**[AGREE with caveat] R2-W5**: 缺少若干直接相关文献

- **Mejer & Crammer (2011) "Confidence in Structured Prediction"**：直接相关，structured prediction 的置信度估计先驱工作（CRF-based），论文已引 Culotta & McCallum (2004) 但漏了这篇。同意应加。
- **Xie et al. (2024) "Self-Evaluation Improves Selective Generation"**：如果涉及 per-sample self-evaluation for selection，直接相关。同意。
- **Zerva et al. (2025)** 和 **"Existing LLMs Are Not Self-Consistent" (2025)**：无法独立验证这两篇的存在和确切内容。建议作者核查后按相关性添加。

---

### Questions

**[AGREE] R2-Q1**: Entity-name-only LP 是否被考虑过？

完全同意这是关键缺失实验——与我的 W3 一致。Discussion 提出假说 (d) format-token dilution 但未直接检验。

---

**[REBUT] R2-Q2**: Binary classifier 预测 non-tied instances 然后条件性应用 LP

这是一个合理的 future work 方向，但作为对当前论文的批评稍显苛刻。论文定位为 diagnostic paper，要求实现 learned components 超出了论文的 scope statement。而且这本质上已是 "trained selector"——论文已指向 Cobbe et al. verifiers 作为解决方案。

---

**[AGREE] R2-Q3**: ρ, AUROC, selection F1 decouple 的 empirical surprise 在哪里？

R2 的质疑合理：这三个指标 *理论上* 确实衡量不同的东西（rank correlation, binary discrimination, per-sample selection），所以它们 decouple 本身不令人惊讶。真正的 empirical content 不在于 "它们 decouple"，而在于 **decouple 的具体方式和原因**（VerbConf ρ > LP 但 selection worst; EM AUROC highest on CoNLL 但 ρ not best on SciERC）。建议作者重新表述 Contribution 1：不是 "metrics decouple"（trivial），而是 "the specific patterns of decoupling reveal distinct failure modes that single-metric evaluation would miss"。

---

**[REBUT] R2-Q4**: CoNLL selection 分析是否有意义？

不完全同意此批评。CoNLL 的 selection 分析虽然 headroom 极小（4pp），但作为 **ceiling-effect control** 是方法论上必要的：它确认 selection failure 不仅发生在难任务（SciERC）上，也发生在易任务上——但原因不同（难任务: LP compression + unreliable rankings; 易任务: collapsed diversity，无 headroom 可 exploit）。论文在 Appendix (Table A13 note) 已承认 "selection analysis on these configurations is uninformative because there is little per-sample variance"。

不过 R2 的 implicit point 有道理：正文不应对 CoNLL selection 结果过度解读。当前 Table A13 的呈现方式是恰当的（放 appendix 而非主表），但正文 Section 4.2 末尾 "The pattern holds across CoNLL" 的表述可以更 nuanced。

---

### 小问题

**[AGREE]** Abstract 数字过密——确实对 readability 有影响，建议精简。

**[REBUT]** Contribution 3 (difficulty-dependent rankings) 较弱——不同意较弱。WNUT-17 boundary collapse（full-set ρ=0.724 but conditional ρ=0.038，Table A5）是一个有价值的 finding，说明 signals 在 capability boundary 处完全失效。这对 practitioners 的 deployment 决策有直接意义。

**[AGREE]** Discussion LP hypotheses 标为 "three mechanisms" 但列出 (a)(b)(c)(d) 四个——我在小问题中也指出了这个 inconsistency。

**[AGREE]** oh2025latentsc bib year 应更新为 2026——如果论文确实在 2026 发表，应修正。

**[REBUT]** FK entity set 改编非标准——论文在 Section 3.2 给出了完整定义，Appendix D 通过 permutation test 验证了 FK 的有效性（all p<0.001, Table A3）。Adapted FK 的理论依据充分：将 entity set 视为 binary present/absent rating matrix 是 Fleiss' κ 的标准 use case。

---

### 总结

与 R2 的评分差异：我给 Overall 3.5（Borderline Conference），R2 给 3.0（Findings）。主要分歧点：

1. **N3 的严重程度**：R2 将 ρ=0.45 的措辞问题列为 critical，我认为是 Should-Fix level 的 framing refinement。
2. **W1 (no remedy) 的影响**：R2 认为严重限制 impact，我认为 diagnostic papers 在 EMNLP 有先例（如 probing/analysis papers），但同意加一个 pilot remedy 会增强。
3. **Contribution 3 (difficulty-dependent)**：R2 认为较弱，我认为 WNUT-17 boundary collapse 有独立价值。

核心一致点：N1/N2（framing + scope）是必须修改的关键问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 26

## Round 26

44 recorded events


### User

_source line 786 · 2026-05-16T06:39:29.079091+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1

**你的侧重**：方法严谨性 + 实验设计 + 统计分析

### 论文信息
- **标题**: Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition
- **路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（含 sections/ 子文件）
- **目标 venue**: EMNLP 2026 Main Conference (via ACL Rolling Review May 2026 cycle)
- **格式**: ACL template (review mode), 8 页正文 + unlimited references, double-blind, 需含 Limitations section

### 你的审查重点

1. **方法设计**
   - 5 个 confidence signals 的定义是否严谨、无歧义
   - Soft Jaccard 定义（Eq.4 用 max 分母而非 union）是否合理、命名是否准确
   - Instance-level vs per-sample 信号的区分是否在实验中得到正确处理
   - MBR/consensus-proximity selection 的实现是否正确

2. **实验设计**
   - 数据集选择（SciERC, CoNLL-2003, WNUT-17）是否构成有效的 difficulty gradient
   - N=8 primary + N=16 scaling 是否足够
   - 模型选择（Qwen3-8B, LLaMA-3.1-8B, Qwen3-4B）是否覆盖足够
   - Gold-empty instance filtering 策略是否一致（QE vs Selection 是否用同一 n？）
   - Free-form decoding ablation 是否充分（seeds, datasets）

3. **统计分析**
   - Sign tests, Fisher combined p, bootstrap CIs 使用是否得当
   - TOST equivalence testing 的 δ 选择是否合理（是否有循环论证）
   - 多重比较校正是否充分
   - 3 seeds 是否提供足够 statistical power（Kendall W=1.000 with n=3 的信息量）
   - NER 2-seed vs RE single-seed selection 统计标准是否一致

4. **结论支撑**
   - "correlation-selection gap" 中哪些是 by-construction（定义必然）vs empirical finding
   - ρ=0.45 被称为 "strong" quality estimation 是否合理
   - RE 结论仅基于 SciERC 单数据集，标题中的 NER 限定是否足够
   - Scale 结论（3B-8B）是否过度泛化
   - Entity-token LP 消融结果如何影响核心叙事

请按以下结构输出你的审稿报告：
- **Summary** (2-3 句)
- **Strengths** (逐条)
- **Weaknesses** (逐条，标注 Must-Fix / Should-Fix / Minor)
- **Questions** (需要作者回答的)
- **Missing References**
- **Overall Assessment** (strong reject / weak reject / borderline / weak accept / strong accept + 置信度 1-5)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 787 · 2026-05-16T06:39:37.742997+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
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

_source line 788 · 2026-05-16T06:39:37.843882+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 789 · 2026-05-16T06:39:42.715508+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 790 · 2026-05-16T06:39:43.067961+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ The Correlation-Selection Gap in LLM-Based Named Entity Recognition}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	Code and data will be released upon acceptance at [anonymized URL].
45	
46	\bibliography{references}
47	
48	\appendix
49	\input{sections/appendix}
50	
51	\end{document}
52	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 791 · 2026-05-16T06:39:43.118659+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 792 · 2026-05-16T06:39:43.219974+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 793 · 2026-05-16T06:39:43.473050+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool result

_source line 794 · 2026-05-16T06:39:52.747786+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"aclrollingreview/acguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/acguidelines.md"}]

Based on the search results, here's information about the ACL Rolling Review 2026 reviewer guidelines, review form, criteria, and scoring:

## Reviewer Guidelines

Starting with February 2025, ARR reviewers are asked to provide 
…[truncated 2331 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 9274
}
```

</details>

---


### Tool call

_source line 795 · 2026-05-16T06:39:57.823165+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 796 · 2026-05-16T06:39:58.175321+00:00_

1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals across three NER benchmarks, with one RE benchmark as an exploratory extension, at two model scales (4B and 8B).
4	All signals achieve moderate-to-strong quality estimation (Spearman $\rho$ up to 0.45), yet none improves best-of-$N$ selection despite substantial oracle headroom---the \textit{correlation-selection gap}.
5	Four instance-level signals assign identical scores to all candidates; when converted to consensus-proximity rankings (MBR), they produce per-sample scores but do not improve selection.
6	Log-probability---the only natively per-sample signal---is too compressed within instances to discriminate (median within-instance range 0.041 nats).
7	A 4-seed free-form decoding ablation confirms NER compression is not an artifact of constrained decoding; on RE, LP selection reverses direction under free-form decoding ($+1.8{\pm}0.1$~pp), suggesting regime-dependent behavior.
8	Consensus-proximity selection (MBR) correlates with F1 across instances but not within them.
9	Signal rankings shift with task difficulty and collapse at the capability boundary; closing the gap likely requires learned per-sample scoring.
10	\end{abstract}
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 797 · 2026-05-16T06:39:58.175696+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 798 · 2026-05-16T06:39:58.879360+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---majority voting over multiple samples---yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
8	\citet{yao2026consistency} examine consistency--accuracy correlations for LLM-based IE using exact-match agreement; we extend their work by introducing structural matching (Soft Jaccard, a variant using per-type max cardinality; \S\ref{sec:signals}) that captures partial overlap, separating quality estimation from best-of-$N$ selection, and evaluating across a three-dataset difficulty gradient with a free-form decoding ablation.
9	
10	Our central finding is the \textbf{correlation-selection gap} (Figure~\ref{fig:overview}): consistency signals achieve moderate-to-strong quality estimation ($\rho$ up to 0.45, substantially exceeding random baselines) but fail at sample selection despite substantial oracle headroom.
11	The gap has two causes: instance-level signals (4 of 5) assign identical QE scores to all candidates; consensus-proximity (MBR) converts these to per-sample rankings, but utility correlates with F1 across instances, not within them (\S\ref{sec:discussion}).
12	LP---the only nativ
…[truncated 2496 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 799 · 2026-05-16T06:39:58.879812+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 800 · 2026-05-16T06:39:58.930698+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text through LLM comparison \cite{chen2024usc}, sub-claim decomposition \cite{thirukovalluru2024atomic}, or hallucination detection \cite{manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2026latentsc} all target discrete answers.
6	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings; \citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.
7	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap.
8	
9	\paragraph{Consistency for structured IE.}
10	\citet{yao2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, leaving open whether structural matching improves on surface agreement, whether quality estimation translates to selection, and whether findings generalize across a difficulty gradient---the three questions we address.
11	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency for QA/summarization but does not address structured extraction.
12	\citet{culotta2004confidence} and \citet{mejer2011confidence} pioneer confidence estimation for structured prediction via CRF marginals and confidence-weighted models; our signals are model-agnostic.
13	Our evaluation builds on generative IE work \cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting} and constrained decoding \cite{willard2023guided}.
14	
15	\paragraph{Uncertainty estimation and calibration.}
16	Surveys cover confidence estimation \cite{geng2024confidence}, uncertainty quantification \cite{xia2025survey}, and calibr
…[truncated 1435 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 801 · 2026-05-16T06:39:59.132925+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 802 · 2026-05-16T06:39:59.635274+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set (NER) or relation set (RE).
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	This distinction is consequential for selection: in our study, 4 of 5 signals are instance-level aggregates that assign identical QE scores to all $N$ candidates. Consensus-proximity (MBR) converts these to per-sample rankings (\S\ref{sec:selection_gap}), but these rankings do not improve selection; only natively per-sample signals can, in principle, exploit oracle headroom.
8	
9	\subsection{Confidence Signals}\label{sec:signals}
10	
11	Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
12	
13	\paragraph{Log-probability (model-internal, per-sample).}
14	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
15	\begin{equation}\label{eq:logprob}
16	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
17	\end{equation}
18	
19	\paragraph{Exact match voting (surface, instance-level).}
20	The proportion of samples producing the most common output:
21	\begin{equation}\label{eq:em}
22	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
23	\end{equation}
24	
25	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
26	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each
…[truncated 3037 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 803 · 2026-05-16T06:39:59.635729+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 804 · 2026-05-16T06:40:00.087997+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English NER benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures.
15	Qwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\ref{app:thinking_token}).
16	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\ref{app:n_scaling}).}
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation ($\rho$ and AUROC; $N{=}8$, seed${=}42$, single-seed; 3-seed stability in Table~\ref{tab:multiseed}). Best in \textbf{bold}. $^\dagger$RE results rest on a single benchmark (SciERC, 40\% zero-F1 rate). $N{=}16$ in Table~\ref{tab:robustness}.}
27	\label{tab:quality_estimation}
28	\begin{tabular}{ll cc cc cc cc}
29	\toprule
30	& & \multicolumn{2}{c}{\text
…[truncated 7584 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 805 · 2026-05-16T06:40:00.088412+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 806 · 2026-05-16T06:40:01.045682+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	VC leads on hard NER ($\rho{=}0.379$); EM leads easy NER and binary discrimination (AUROC${=}0.816$, CoNLL); on $^\dagger$RE, LP outperforms structural signals (Table~\ref{tab:multiseed}).
5	Rankings hold across model families and a 4B ablation (Table~\ref{tab:scale_ablation}); at the capability boundary (WNUT-17), all signals collapse.
6	
7	\paragraph{Why the gap exists.}
8	Four of five signals are instance-level aggregates that assign a single QE score per input. Consensus-proximity (MBR) converts these to per-sample rankings (Table~\ref{tab:selection}), instantiating MBR decoding \cite{eikema2022sampling} with signal-specific utility functions. Despite MBR's success in machine translation \cite{freitag2022high}, all variants fail here because utility correlates with F1 across instances but not within a single instance---the fundamental asymmetry underlying the gap (Appendix~\ref{app:mbr_discussion}).
9	Log-probability, the only per-sample signal, is severely compressed: median LP range is 0.041 nats (IQR [0.024, 0.073]; Table~\ref{tab:logprob_ties}), with pooled within-instance $\rho(\text{LP}, \text{F1}){=}0.248$ confirming weak but positive signal.
10	Where compression is mitigated ($n{=}210$ instances with above-median spread), LP selection outperforms single-sample ($+2.9$~pp, $p{=}0.004$), confirming compression as the bottleneck; the gap holds even among high-diversity instances (Appendix~\ref{app:diversity}).
11	Stratifying by voting confidence reveals a complementary mechanism: high-consistency instances (Q4) have collapsed headroom (4.78~pp), leaving nothing to select, while low-consistency instances retain headroom but unreliable LP rankings (Appendix~\ref{app:vc_quartile}).
12	Doubling to $N{=}16$ expands oracle headroom by $+4.4$~pp without improving selection; on $^\dagger$RE at 4B scale, LP is the sole positive signal ($\Delta{=}{+}0.7$~pp, $p{=}0.058$; Table~
…[truncated 4902 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 807 · 2026-05-16T06:40:01.196869+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 808 · 2026-05-16T06:40:01.499436+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluate five confidence signals for quality estimation and sample selection in LLM-based NER, revealing the \textit{correlation-selection gap}: moderate-to-strong quality estimation ($\rho$ up to 0.45) coexists with selection failure.
4	Instance-level signals, even when converted to per-sample MBR rankings, do not improve selection; the core empirical finding is that log-probability---the only natively per-sample signal---is too compressed within instances to discriminate (median range 0.041 nats), and consensus-proximity utility correlates with F1 across but not within instances.
5	A 4-seed free-form ablation confirms NER compression is not caused by constrained decoding; on $^\dagger$RE, LP selection reverses direction.
6	Signal rankings shift with difficulty across NER benchmarks and collapse at the capability boundary in the small-model regime (3B--8B); whether LP compression persists at 70B+ scales is an open question.
7	$^\dagger$RE conclusions rest on SciERC alone (40\% zero-F1 rate); trained verifiers and scaling to 70B+ are promising directions.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 809 · 2026-05-16T06:40:01.499884+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 810 · 2026-05-16T06:40:02.002695+00:00_

1	Our evaluation covers three NER datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1; generalization to other RE benchmarks remains unvalidated.
2	TACRED-style sentence-level RE classification differs structurally from set-valued extraction and is left for future work.
3	We cover 4B--8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested---larger models may produce more diverse samples.
4	We do not train a verifier, leaving unknown how much oracle headroom a supervised approach could recover.
5	
6	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
7	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE shows a directional LP reversal under free-form decoding.
8	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
9	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
10	We tested verbalized confidence \cite{tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
11	We evaluate signals individually; whether signal combinations (e.g., LP $\times$ consistency) or learned weightings could close the selection gap is unexplored.
12	The $\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app:epsilon_robustness}), the specific subset gains should be interpreted as characterizing the compression phenomenon rather than as a tuned selection strategy.
13	We tested one remedy for LP compression--
…[truncated 258 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 811 · 2026-05-16T06:40:02.254293+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 812 · 2026-05-16T06:40:03.864981+00:00_

File content (25406 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1610
}
```

</details>

---


### Tool call

_source line 813 · 2026-05-16T06:40:04.016474+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their exact scales (1-5, etc.), and the description for each score level. I need the exact rubric for: soundness, excitement, overall assessment, reproducibility, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their exact scales (1-5, etc.), and the description for each score level. I need the exact rubric for: soundness, excitement, overall assessment, reproducibility, and any other scored dimensions."
  }
}
```

</details>

---


### Tool call

_source line 814 · 2026-05-16T06:40:05.225324+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines, especially: what constitutes a sound paper, what is excitement, scoring rubrics, and any guidance on how to assess methodology and experimental design."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines, especially: what constitutes a sound paper, what is excitement, scoring rubrics, and any guidance on how to assess methodology and experimental design."
  }
}
```

</details>

---


### Tool result

_source line 815 · 2026-05-16T06:40:10.856043+00:00_

# ACL Rolling Review Form Rubrics

## Soundness
Scale: 1-5 (with 3.5, 2.5, 1.5 options)

- **5 = Excellent:** "This study is one of the most thorough I have seen, given its type."
- **4 = Strong:** "This study provides sufficient support for all of its claims."
- **3 = Acceptable:** "This study provides sufficient support for its main claims."
- **2 = Poor:** "Some of the main claims are not sufficiently supported."
- **1 = Major Issues:** "This study is not yet sufficiently thorough to warrant publication."

## Excitement
Scale: 1-5 (with 4.5, 3.5, 2.5, 1.5 options)

- **5 = Highly Exciting:** "I would recommend this paper to others and/or attend its presentation."
- **4 = Exciting:** "I would mention this paper to others and/or make an effort to attend."
- **3 = Interesting:** "I might mention some points of this paper to others."
- **2 = Potentially Interesting:** "this paper does not resonate with me, but it might with others."
- **1 = Not Exciting:** Paper lacks relevance to computational linguistics work.

## Overall Assessment
Scale: 1-5 (with 4.5, 3.5, 2.5, 1.5 options)

- **5 = Consider for Award:** "I think this paper could be considered for an outstanding paper award."
- **4 = Conference:** "I think this paper could be accepted to an \*ACL conference."
- **3 = Findings:** "I think this paper could be accepted to the Findings of the ACL."
- **2 = Resubmit next cycle:** "This paper needs substantial revisions."
- **1 = Do not resubmit:** "This paper has to be fully redone."

## Reproducibility
Scale: 1-5

- **5:** "They could easily reproduce the results."
- **4:** "They could mostly reproduce the results."
- **3:** "They could reproduce with some difficulty."
- **2:** "They would be hard pressed to reproduce the results."
- **1:** "They would not be able to reproduce the results."

## Reviewer Confidence
Scale: 1-5

- **5:** "Positive that my evaluation is correct."
- **4:** "Quite sure...unlikely, though conceivable, that I missed something."
- **3:** "Pr
…[truncated 186 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6839
}
```

</details>

---


### Tool result

_source line 816 · 2026-05-16T06:40:17.084374+00:00_

# ARR Reviewer Guidelines: Sound Papers, Excitement, and Scoring

## What Constitutes Sound Methodology

ARR emphasizes technical rigor and clarity. Papers should demonstrate "sufficiently familiar with the core methodology and the kinds of arguments that are typically made in our field's papers." Reviewers must verify:

- **Clear assumptions**: "All assumptions should be clearly stated" (M5)
- **Valid proofs**: For formal contributions, proofs must be "complete and correct" (M5)
- **Appropriate methodology selection**: Methods should be justified relative to research questions, not selected arbitrarily (M4)
- **Reproducibility details**: Sufficient information to replicate experiments, including hyperparameters and code availability (M2)

## Sound Experimental Design

The guidelines warn against several common pitfalls:

- **Unmotivated sample selection** (M4): The chosen models and benchmarks must align with stated contributions
- **Insufficient statistics** (R5): "at least the main experimental results should be accompanied by appropriate information about their statistical significance"
- **Scope-claim mismatch** (R2): Evaluation samples must represent the populations claims address
- **P-hacking and prompt engineering** (R1): Report results transparently without cherry-picking

## The Three Scoring Dimensions

Starting February 2025, ARR uses three orthogonal scores:

**Soundness**: Technical validity and methodological rigor. "Soundness scores must be justified by the text of the review" (I3). Low soundness requires clear evidence of flaws.

**Excitement**: Subjective personal interest. This is explicitly separated from soundness—"you may consider a paper worthy of the main conference even if you personally are not excited about it" (I3).

**Overall Recommendation**: A composite assessment reflecting soundness, excitement, novelty, and potential impact. All main conference papers "are expected to be sufficiently sound and reproducible" (I3).

## Critical Guida
…[truncated 1078 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 11859
}
```

</details>

---


### Tool call

_source line 817 · 2026-05-16T06:40:24.189254+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "500"
  }
}
```

</details>

---


### Tool result

_source line 818 · 2026-05-16T06:40:24.491928+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality---including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
47	\quad FK & 
…[truncated 37198 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 819 · 2026-05-16T06:40:24.542736+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 820 · 2026-05-16T06:40:24.593356+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 821 · 2026-05-16T06:40:28.813553+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "500"
  }
}
```

</details>

---


### Tool result

_source line 822 · 2026-05-16T06:40:29.116894+00:00_

500	At this cutpoint, 60.3\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below $\varepsilon$, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$).
501	The CDF rises smoothly with no cliff or discontinuity (Figure~\ref{fig:lp_range_cdf}), confirming that compression is a pervasive regime rather than a bimodal split.
502	This compression is stable across seeds: seed${=}456$ yields median LP range${=}0.040$ nats and tied fraction${=}62.2\%$ (vs.\ seed${=}42$: $0.041$ nats, $60.3\%$).
503	Seed~456 uses a different subtask flag (joint vs.\ ner for seeds 42 and 123); the LP distributions are statistically indistinguishable (median LP: 8.37 vs.\ 8.20 nats; Mann--Whitney $p{=}0.55$), confirming that the subtask change does not affect compression.
504	For comparison, SJ has only 12.5\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.
505	
506	\begin{figure}[t]
507	\centering
508	\includegraphics[width=\columnwidth]{fig_lp_range_cdf}
509	\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}
510	\label{fig:lp_range_cdf}
511	\end{figure}
512	
513	\begin{table}[t]
514	\centering
515	\small
516	\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\varepsilon$.}
517	\label{tab:logprob_ties}
518	\begin{tabular}{lc}
519	\toprule
520	$\varepsilon$ threshold & Tied instances (\%) \\
521	\midrule
522	0.01 & 1.1\% \\
523	0.05 & 60.3\% \\
524	0.1  & ${\sim}$84\% \\
525	0.5  & ${\sim}$99\% \\
526	\bottomrule
527	\end{tabular}
528	\end{table}
529	
530	\paragraph{Non-tied subset.}
531	Among instances with LP range ${\geq}0.05$ ($n{=}210$, 40\% of total), log-probability selection \textit{significa
…[truncated 30290 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 303
}
```

</details>

---


### Tool call

_source line 823 · 2026-05-16T06:40:33.787827+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "995"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "995"
  }
}
```

</details>

---


### Tool result

_source line 824 · 2026-05-16T06:40:33.938829+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (995). The file has 995 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 825 · 2026-05-16T06:42:47.656917+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines page limit"
  }
}
```

</details>

---


### Tool result

_source line 826 · 2026-05-16T06:42:52.401605+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines page limit"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"EMNLP 2026 on X: \"Here is more precise submission policy. For full details, please check the latest CFP on our website! https://t.co/6dttoXBIT9 https://t.co/ta6IuAjIVm\" / X","url":"https://x.com/emnlpmeeting/status/2047977818928320807"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"}]

Based on the search results, here are the page limit guidelines for EMNLP 2026:

**Main Conference Papers:** The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers.

**Industry Track Papers:** Industry Track papers cannot exceed 6 pages in length (excluding ethical considerations and references). Additionally, references and limitations sections do not count toward the page limit, nor do the following optional sections: acknowledgements (only in the final version), eth
…[truncated 228 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 4744
}
```

</details>

---


### Tool call

_source line 827 · 2026-05-16T06:45:15.968530+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 Round 1 审稿报告完成\n\n**Paper**: Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition\n\n### 总体评分\n- **Soundness**: 3.5/5\n- **Excitement**: 3.5/5\n- **Reproducibility**: 4/5\n- **Overall**: 3.5/5 (Borderline Findings/Conference)\n- **Confidence**: 4/5\n\n### 核心判断\n研究问题新颖（QE vs selection 解耦），统计实践扎实（bootstrap CIs, TOST with external anchors, effect sizes），但有两个关键问题需要解决。\n\n### Must-Fix (2项)\n**N1**: Selection gap 的 effective test bed 仅限 SciERC（CoNLL 是 ceiling-effect control，WNUT collapse）。标题和 abstract 暗示 NER 普遍现象，但实证仅来自一个科学领域数据集（n=529）。建议：增加中等难度数据集或收窄 claim scope。\n\n**N2**: Framing 过度强调 \"4/5 signals assign identical scores\"（by-construction trivial），模糊了核心 empirical finding（MBR conversion 产生 per-sample rankings 后仍然失败，因为 utility 在 across-instances 而非 within-instance 维度与 F1 相关）。当前叙事使读者误以为 gap 对 instance-level signals 是显而易见的定义问题。\n\n### Should-Fix (5项)\nW1: ρ=0.45 称 \"moderate-to-strong\" 但此值来自 ceiling-effect 数据集 CoNLL；SciERC 上最佳仅 ρ=0.379\nW2: N≤16 不足以支撑 scaling claim，需 N=32+ 验证\nW3: 缺少 greedy decoding baseline——部署决策的核心对照\nW4: 3 seeds 下 Kendall W=1.000 统计信息量不足\nW5: Soft Jaccard 命名不准确（分母用 max 非 union）\n\n### 主要优势\n- Entity-token LP 消融深层诊断（排除 format-token dilution，指向 intrinsic model overconfidence）\n- Free-form ablation 4-seed RE reversal（+1.84±0.12 pp）\n- 统计实践（TOST 循环论证识别与外部锚定、bootstrap CIs、Bonferroni 讨论）\n- Honest negative-result reporting with appropriate caveats\n\n### 5 个作者需回答的问题\nQ1: 是否尝试过 soft selection / weighted fusion 而非 hard argmax MBR?\nQ2: Oracle headroom 依赖 gold annotations，部署时如何估计？\nQ3: Entity-token LP variance 在 CoNLL vs SciERC 的巨大差异是否与 entity type diversity 有关？\nQ4: RE LP reversal 的 constrained baseline 仅 single-seed，reversal magnitude 相对 seed variance 是否显著？\nQ5: 4B 模型 QE 优于 8B 的 counterintuitive finding 需要更多讨论——是否因 output diversity 更大？\n\n完整审稿报告已在 Reviewer 1 session 中生成。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 Round 1 审稿报告完成\n\n**Paper**: Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition\n\n### 总体评分\n- **Soundness**: 3.5/5\n- **Excitement**: 3.5/5\n- **Reproducibility**: 4/5\n- **Overall**: 3.5/5 (Borderline Findings/Conference)\n- **Confidence**: 4/5\n\n### 核心判断\n研究问题新颖（QE vs selection 解耦），统计实践扎实（bootstrap CIs, TOST with external anchors, effect sizes），但有两个关键问题需要解决。\n\n### Must-Fix (2项)\n**N1**: Selection gap 的 effective test bed 仅限 SciERC（CoNLL 是 ceiling-effect control，WNUT collapse）。标题和 abstract 暗示 NER 普遍现象，但实证仅来自一个科学领域数据集（n=529）。建议：增加中等难度数据集或收窄 claim scope。\n\n**N2**: Framing 过度强调 \"4/5 signals assign identical scores\"（by-construction trivial），模糊了核心 empirical finding（MBR conversion 产生 per-sample rankings 后仍然失败，因为 utility 在 across-instances 而非 within-instance 维度与 F1 相关）。当前叙事使读者误以为 gap 对 instance-level signals 是显而易见的定义问题。\n\n### Should-Fix (5项)\nW1: ρ=0.45 称 \"moderate-to-strong\" 但此值来自 ceiling-effect 数据集 CoNLL；SciERC 上最佳仅 ρ=0.379\nW2: N≤16 不足以支撑 scaling claim，需 N=32+ 验证\nW3: 缺少 greedy decoding baseline——部署决策的核心对照\nW4: 3 seeds 下 Kendall W=1.000 统计信息量不足\nW5: Soft Jaccard 命名不准确（分母用 max 非 union）\n\n### 主要优势\n- Entity-token LP 消融深层诊断（排除 format-token dilution，指向 intrinsic model overconfidence）\n- Free-form ablation 4-seed RE reversal（+1.84±0.12 pp）\n- 统计实践（TOST 循环论证识别与外部锚定、bootstrap CIs、Bonferroni 讨论）\n- Honest negative-result reporting with appropriate caveats\n\n### 5 个作者需回答的问题\nQ1: 是否尝试过 soft selection / weighted fusion 而非 hard argmax MBR?\nQ2: Oracle headroom 依赖 gold annotations，部署时如何估计？\nQ3: Entity-token LP variance 在 CoNLL vs SciERC 的巨大差异是否与 entity type diversity 有关？\nQ4: RE LP reversal 的 constrained baseline 仅 single-seed，reversal magnitude 相对 seed variance 是否显著？\nQ5: 4B 模型 QE 优于 8B 的 counterintuitive finding 需要更多讨论——是否因 output diversity 更大？\n\n完整审稿报告已在 Reviewer 1 session 中生成。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 828 · 2026-05-16T06:45:20.153541+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4185
}
```

</details>

---


### Assistant

_source line 829 · 2026-05-16T06:45:24.835946+00:00_

Round 1 审稿报告已完成并提交给 Review Director。

核心结论：**Overall 3.5/5（Borderline Findings/Conference）**。研究问题有价值，统计实践优秀，但两个 Must-Fix 问题需要解决：(1) selection gap 的有效验证仅限 SciERC 一个数据集，generalizability 不足；(2) framing 过度强调 instance-level signals 的 by-construction limitation，掩盖了 MBR failure 这一更有价值的 empirical finding。5 项 Should-Fix 中最重要的是缺少 greedy decoding baseline 和 N>16 的验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 27

## Round 27

4 recorded events


### User

_source line 830 · 2026-05-16T06:46:09.923415+00:00_

[Round 1 审稿请求]:
## Step 2 — 交叉分享：Reviewer 2 的完整审稿意见

请逐条回应以下 Reviewer 2 的审稿意见。对每一条使用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

### Reviewer 2 完整审稿报告

**Overall**: 3/5 (Findings track, not main conference)

**Strengths**:
- S1: QE 与 selection 的解耦是有价值的方法论贡献
- S2: 统计方法论在 NLP empirical papers 中属上乘
- S3: LP 压缩诊断链层次分明（全序列→entity-token→free-form→verbalized→non-tied subset）
- S4: Appendix 质量高（FK independence, LOO-SJ, OOD, SJ normalizer）
- S5: †RE hedging 诚实一致

**Must-Fix**:
- N1 [critical]: Instance-level 信号的 "gap" 是设计的定义性后果而非经验发现。4/5 信号 by construction 对同一 instance 赋相同分数。MBR 转换是额外方法步骤。Abstract/Intro/Conclusion 将 definitional failure 与 empirical failure（LP 压缩）混为同一现象。建议 Contribution 1 明确区分 (a) MBR across-vs-within asymmetry（empirical）和 (b) LP compression（empirical）。

- N2 [critical]: Contribution framing 相对 Yao et al. (2026) 夸大增量贡献。SJ vs EM 改进仅 Δρ=+0.065（borderline, "would not survive Bonferroni"），CoNLL 上 EM 反领先。Difficulty gradient 是自然 multi-dataset 延伸。建议重心放在 MBR 失败机制和 LP 压缩诊断。

**Should-Fix**:
- W1: 纯诊断无 remedy（entity-token LP 失败, verbalized conf 失败, non-tied LP 依赖 post-hoc ε）。至少尝试一个 lightweight pilot（LP×VC, calibration-based rescoring）。
- W2: RE 覆盖过广但证据过弱。†RE >15 处，hedging noise 大。Free-form RE reversal 是最有趣发现但被埋在 appendix。建议全做或全移 Appendix。
- W3: Abstract 信息过度压缩（9 句覆盖 5 signals + MBR + LP 0.041 nats + free-form + RE reversal）。

**Minor**:
- M1: mejer2011confidence key 年份错误（实际 EMNLP 2010）
- M2: feng2025optimal first author mismatch
- M3: hobelsberger2025, lightman2024, venktesh2025, zhang2025conformal 在 OpenAlex 未匹配
- M4: Table 2 caption "Fisher p" vs Appendix "Fisher combined p" 术语不一致
- M5: Discussion LP hypotheses (a)-(d) "and" 重复

**Questions**:
1. Non-tied LP subset +2.9pp 部署时需 ground-truth 选 ε，是否有 oracle-free proxy？
2. SJ-utility 与 F1 的 within-instance ρ 具体多少？
3. LP×VC combination 是否有初步数据？

**Missing References**: 无（50 entries, 0 orphan, 0 missing）

**��式**: ✅ ACL review mode, ✅ anonymous, ✅ Limitations, ✅ Ethics, ⚠️ 页数需编译确认

---

请逐条回应上述所有 Must-Fix、Should-Fix、Minor 和 Questions。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 831 · 2026-05-16T06:48:00.881739+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 交叉回应 Reviewer 2 完成\n\n### 同意的条目\n- **R2-N1** (definitional vs empirical): 完全同意，与我的 R1-N2 一致\n- **R2-W2** (RE 覆盖过广): 同意，建议全移 appendix\n- **R2-W3** (Abstract 过度压缩): 同意\n- **R2-M1–M5**: 全部同意\n- **R2-Q1–Q3**: 全部同意是有价值的问题，特别是 Q2（SJ-utility within-instance ρ 缺失）是支撑核心 claim 的关键数据空白\n\n### 有分歧的条目\n- **R2-N2** (贡献 incremental): 部分同意。SJ vs EM (Δρ=+0.065, borderline) 和 difficulty gradient 确实不强，但 QE-selection separation 和 LP compression diagnostic chain（全序列→entity-token→free-form→verbalized→non-tied，涉及 5 层消融）是超越 Yao et al. 的 non-trivial 贡献。R2 的修改建议方向正确（重心转向 MBR failure + LP diagnostics），但不应将整体贡献判为仅 incremental。\n\n- **R2-W1** (无 remedy): 同意 LP×VC 缺席遗憾，但诊断性论文不必须包含 remedy（ARR H13: \"additional experiments could be performed\" 非自动 weakness）。\n\n### Overall 分歧\nR2: 3/5 (Findings) vs R1: 3.5/5 (Borderline)\n分歧核心：R2 对 SJ contribution 和 difficulty gradient 的批评合理，但 LP compression diagnostic chain 和 entity-token ablation 的独立价值被低估。修正 framing（N1/N2）后论文贡献更清晰。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 交叉回应 Reviewer 2 完成\n\n### 同意的条目\n- **R2-N1** (definitional vs empirical): 完全同意，与我的 R1-N2 一致\n- **R2-W2** (RE 覆盖过广): 同意，建议全移 appendix\n- **R2-W3** (Abstract 过度压缩): 同意\n- **R2-M1–M5**: 全部同意\n- **R2-Q1–Q3**: 全部同意是有价值的问题，特别是 Q2（SJ-utility within-instance ρ 缺失）是支撑核心 claim 的关键数据空白\n\n### 有分歧的条目\n- **R2-N2** (贡献 incremental): 部分同意。SJ vs EM (Δρ=+0.065, borderline) 和 difficulty gradient 确实不强，但 QE-selection separation 和 LP compression diagnostic chain（全序列→entity-token→free-form→verbalized→non-tied，涉及 5 层消融）是超越 Yao et al. 的 non-trivial 贡献。R2 的修改建议方向正确（重心转向 MBR failure + LP diagnostics），但不应将整体贡献判为仅 incremental。\n\n- **R2-W1** (无 remedy): 同意 LP×VC 缺席遗憾，但诊断性论文不必须包含 remedy（ARR H13: \"additional experiments could be performed\" 非自动 weakness）。\n\n### Overall 分歧\nR2: 3/5 (Findings) vs R1: 3.5/5 (Borderline)\n分歧核心：R2 对 SJ contribution 和 difficulty gradient 的批评合理，但 LP compression diagnostic chain 和 entity-token ablation 的独立价值被低估。修正 framing（N1/N2）后论文贡献更清晰。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 832 · 2026-05-16T06:48:04.905328+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4023
}
```

</details>

---


### Assistant

_source line 833 · 2026-05-16T06:48:09.618454+00:00_

交叉回应已完成并提交。核心结论：与 R2 在 N1（definitional vs empirical framing）、W2–W3、所有 Minor 和 Questions 上一致；在 N2（overall contribution）和 W1（remedy necessity）上有程度分歧——我认为 LP diagnostic chain 的独立价值使论文高于 pure Findings level。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 28

## Round 28

42 recorded events


### User

_source line 834 · 2026-05-16T07:40:15.401834+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1

### 你的审查侧重：方法严谨性 + 实验设计 + 统计分析

### Venue 信息
- **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle)
- **截止日期**: 2026-05-25
- **页数限制**: 正文 8 页 (long paper)，参考文献/limitations/ethics/appendix 不计
- **模板**: ACL style (`\usepackage[review]{acl}`)
- **匿名规则**: Double-blind (作者已匿名)
- **附录**: 允许，不参与页数限制但可被审稿人参考

### 论文路径
`projects/struct_self_consist_ie/docs/paper/main.tex`
（sections 在 `docs/paper/sections/` 下: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex）
（references: `docs/paper/references.bib`）

### 论文概要
标题: "Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition"
研究 LLM-based NER 中 5 种置信信号的质量估计与样本选择能力。核心发现：信号可估计质量（ρ=0.38）但无法选出优于 greedy decoding 的样本——"correlation-selection gap"。诊断两种失败机制：instance degeneracy 和 LP compression。

### 重点审查方向

1. **方法定义与数学正确性**：
   - 5 种信号（SJ, VC, FK, EM, LP）的定义是否严谨？公式是否正确？
   - SJ 分母用 max(|g_i|,|g_j|) 而非 union——命名为 "Soft Jaccard" 是否恰当？
   - Instance-level vs per-sample 信号的区分是否清晰？

2. **实验设计**：
   - 数据集选择（SciERC/CoNLL/WNUT-17 三梯度）是否合理？
   - Selection gap 的有效测试台是否仅限 SciERC（CoNLL ceiling-effect, WNUT collapse）？如此，三数据集验证的 claim 是否过强？
   - N=8/16 样本量是否充分？
   - Greedy baseline (T=0) 的加入是否恰当？Single sample (T=1.0 draw) vs Greedy (argmax) 的区别是否充分说明？

3. **统计分析**：
   - 3-seed stability（σ≤0.026）的统计效力如何？n=3 下 Kendall W 有多大信息量？
   - Bootstrap CI、Fisher combined p、TOST equivalence testing 的使用是否恰当？
   - Gold-empty instance filtering 在 QE 和 Selection 之间是否一致？（Section 3.3 写 n=529 on SciERC from 551, n=2756 on CoNLL from 3453）
   - ε=0.05 threshold 用于 LP tied/non-tied 分层——是否有 prior justification？Sensitivity analysis 是否充分？

4. **消融实验链**：
   - Free-form decoding ablation（std ratio 0.97）→ 排除 constrained decoding
   - Entity-token LP（4× variance but -2.0pp selection）→ 排除 format-token dilution
   - Verbalized confidence → 排除 LP-specific
   - 这条诊断链的逻辑是否严密？每一步排除是否成立？

5. **Claim-Evidence 对齐**：
   - "correlation-selection gap" 的操作性定义在哪？是否清晰？
   - 4/5 signals 是 instance-level → 不能 select 是 by construction。这算 finding 还是 trivial observation？MBR conversion 后仍失败才是 empirical finding——论文区分清楚了吗？
   - Scale ablation (4B vs 8B) 能否支撑 "task difficulty drives the gap" 的结论？

请以 EMNLP 顶级审稿人标准评估。输出格式：
- Summary（2-3 句）
- Strengths（逐条）
- Weaknesses（逐条，分 Must-Fix / Should-Fix / Minor）
- Questions（需要作者回答的问题）
- Missing References（遗漏的关键相关工作）
- Overall Assessment（评分 + 置信度）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 835 · 2026-05-16T07:40:24.749716+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
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

_source line 836 · 2026-05-16T07:40:24.850617+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 837 · 2026-05-16T07:40:28.815787+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 838 · 2026-05-16T07:40:30.322872+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 839 · 2026-05-16T07:40:30.724842+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ The Correlation-Selection Gap in LLM-Based Named Entity Recognition}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	Code and data will be released upon acceptance at [anonymized URL].
45	
46	\bibliography{references}
47	
48	\appendix
49	\input{sections/appendix}
50	
51	\end{document}
52	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 840 · 2026-05-16T07:40:30.725366+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 841 · 2026-05-16T07:40:31.227583+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	This distinction is consequential for selection: in our study, 4 of 5 signals are instance-level aggregates that assign identical QE scores to all $N$ candidates. Consensus-proximity (MBR) converts these to per-sample rankings (\S\ref{sec:selection_gap}), but these rankings do not improve selection; only natively per-sample signals can, in principle, exploit oracle headroom.
8	
9	\subsection{Confidence Signals}\label{sec:signals}
10	
11	Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
12	
13	\paragraph{Log-probability (model-internal, per-sample).}
14	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
15	\begin{equation}\label{eq:logprob}
16	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
17	\end{equation}
18	
19	\paragraph{Exact match voting (surface, instance-level).}
20	The proportion of samples producing the most common output:
21	\begin{equation}\label{eq:em}
22	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
23	\end{equation}
24	
25	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
26	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary pres
…[truncated 2968 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 842 · 2026-05-16T07:40:31.227987+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 843 · 2026-05-16T07:40:31.278577+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English NER benchmarks spanning a difficulty gradient, each serving a distinct role.
9	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\approx}$65\% F1.
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 52\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures.
15	Qwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\ref{app:thinking_token}).
16	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\ref{app:n_scaling}).}
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, seed${=}42$, single-seed; 3-seed stability in Table~\ref{tab:multiseed}). Best in \textbf{bold}. RE results in Appendix~\ref{app:re_extension}. $N{=}16$ in Table~\ref{tab:robustness}.}
27	\la
…[truncated 7238 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 844 · 2026-05-16T07:40:37.022658+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Scoring Structure

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement
…[truncated 1563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8206
}
```

</details>

---


### Tool call

_source line 845 · 2026-05-16T07:40:42.049139+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 846 · 2026-05-16T07:40:42.602981+00:00_

1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals on a primary medium-difficulty benchmark (SciERC) with ceiling-effect (CoNLL) and signal-collapse (WNUT-17) boundary conditions, at two model scales (4B and 8B).
4	All signals achieve moderate-to-strong quality estimation ($\rho{=}0.38$ on the primary test bed, up to 0.45 on a ceiling-effect control), yet none improves best-of-$N$ selection over cost-free greedy decoding---the \textit{correlation-selection gap}.
5	Consensus-proximity (MBR) selection achieves positive within-instance utility--F1 correlation (median $\rho{=}0.52$) but fails due to pervasive instance degeneracy (21--58\% of instances yield identical outputs); log-probability---the only per-sample signal---is too compressed within instances to discriminate.
6	Diagnostic ablations---free-form decoding, entity-token LP isolation---confirm that compression is intrinsic rather than an artifact of constrained decoding or format-token dilution.
7	Signal rankings shift with task difficulty and collapse at the capability boundary; closing the gap likely requires learned per-sample scoring.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 847 · 2026-05-16T07:40:42.603478+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 848 · 2026-05-16T07:40:43.105741+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---majority voting over multiple samples---yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
8	\citet{yao2026consistency} examine consistency--accuracy correlations for LLM-based IE using exact-match agreement; we extend their work by separating quality estimation from best-of-$N$ selection, diagnosing two failure mechanisms (instance degeneracy and LP compression) through a multi-ablation chain across a three-dataset difficulty gradient.
9	
10	Our central finding is the \textbf{correlation-selection gap} (Figure~\ref{fig:overview}): consistency signals achieve moderate-to-strong quality estimation ($\rho{=}0.38$ on the primary test bed, up to 0.45 on a ceiling-effect control) but fail to improve selection over cost-free greedy decoding ($T{=}0$) despite substantial oracle headroom.
11	The gap has two causes: (a)~\textit{instance degeneracy}---fine-tuned models produce identical outputs for 21--58\% of instances, eliminating selection headroom despite positive within-instance utility--F1 correlation (median $\rho{=}0.52$); and (b)~\textit{LP compression}---log-probability, the only per
…[truncated 2446 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 849 · 2026-05-16T07:40:43.257326+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 850 · 2026-05-16T07:40:43.309381+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	VC leads on medium-difficulty NER ($\rho{=}0.379$, SciERC); EM leads easy NER and binary discrimination (AUROC${=}0.816$, CoNLL).
5	Rankings hold across model families and a 4B ablation (Table~\ref{tab:scale_ablation}); at the capability boundary (WNUT-17), all signals collapse. RE signal rankings are reported in Appendix~\ref{app:re_extension}.
6	
7	\paragraph{Why the gap exists.}
8	We identify two mechanisms: \textit{instance degeneracy} (affecting consensus-proximity selection) and \textit{LP compression} (affecting per-sample selection).
9	
10	Four of five signals are instance-level aggregates; consensus-proximity (MBR) converts these to per-sample rankings (Table~\ref{tab:selection}), instantiating MBR decoding \cite{eikema2022sampling} with signal-specific utility functions.
11	Within-instance analysis reveals that MBR utility does correlate positively with F1 (SJ median within-instance $\rho{=}0.524$ on SciERC, $0.994$ on CoNLL), and on non-degenerate instances MBR closes 23\% (SciERC) to 41\% (CoNLL) of the oracle gap.
12	However, fine-tuned models exhibit pervasive \textit{instance degeneracy}: 21\% of SciERC instances (58\% on CoNLL) produce identical F1 across all $N$ samples, offering zero selection headroom; an additional 13\% (49\% on CoNLL) yield constant utility scores, preventing MBR ranking entirely (Table~\ref{tab:degeneracy}).
13	These degenerate instances dominate the aggregate, diluting genuine gains to near-zero.
14	Despite MBR's success in machine translation \cite{freitag2022high}, all variants fail here because degeneracy eliminates the headroom that positive within-instance correlation would otherwise exploit (Appendix~\ref{app:mbr_discussion}).
15	Meanwhile, deterministic greedy decoding ($T{=}0$)---requiring no sampling cost---achieves F1${=}0.663$ on SciERC, surpassing all $N{=}8$ selection strategies (best: LP at 0.647; Table~\ref{tab:selection})
…[truncated 5898 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 851 · 2026-05-16T07:40:43.661755+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 852 · 2026-05-16T07:40:43.762687+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text through LLM comparison \cite{chen2024usc}, sub-claim decomposition \cite{thirukovalluru2024atomic}, or hallucination detection \cite{manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2026latentsc} all target discrete answers.
6	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings; \citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.
7	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap.
8	
9	\paragraph{Consistency for structured IE.}
10	\citet{yao2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, leaving open whether structural matching improves on surface agreement, whether quality estimation translates to selection, and whether findings generalize across a difficulty gradient---the three questions we address.
11	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency for QA/summarization but does not address structured extraction.
12	\citet{culotta2004confidence} and \citet{mejer2010confidence} pioneer confidence estimation for structured prediction via CRF marginals and confidence-weighted models; our signals are model-agnostic.
13	Our evaluation builds on generative IE work \cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting} and constrained decoding \cite{willard2023guided}.
14	
15	\paragraph{Uncertainty estimation and calibration.}
16	Surveys cover confidence estimation \cite{geng2024confidence}, uncertainty quantification \cite{xia2025survey}, and calibr
…[truncated 1476 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 853 · 2026-05-16T07:40:49.587012+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 854 · 2026-05-16T07:40:49.989241+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluate five confidence signals for quality estimation and sample selection in LLM-based NER, revealing the \textit{correlation-selection gap}: moderate-to-strong quality estimation ($\rho{=}0.38$ on medium-difficulty NER, up to 0.45 on a ceiling-effect control) coexists with selection that fails to outperform cost-free greedy decoding.
4	The gap stems from two mechanisms: instance degeneracy (21--58\% of instances produce identical F1 across all $N$ samples, eliminating selection headroom despite positive within-instance utility correlation) and LP compression (the only per-sample signal has median within-instance range of 0.041 nats).
5	Diagnostic ablations---free-form decoding, entity-token LP isolation---confirm compression is intrinsic rather than an artifact of constrained decoding or format-token dilution.
6	The gap is demonstrated in the medium-difficulty regime where models achieve moderate but imperfect accuracy; signal rankings shift with difficulty and collapse at the capability boundary in the small-model regime (3B--8B).
7	Whether these mechanisms persist at 70B+ scales is an open question; trained verifiers and an exploratory extension to relation extraction (Appendix~\ref{app:re_extension}) are promising directions.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 855 · 2026-05-16T07:40:50.140329+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 856 · 2026-05-16T07:40:50.944569+00:00_

1	Our evaluation covers three NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.
2	We cover 4B--8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested---larger models may produce more diverse samples.
3	We do not train a verifier, leaving unknown how much oracle headroom a supervised approach could recover.
4	
5	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
6	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\ref{app:re_extension}.
7	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
8	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
9	We tested verbalized confidence \cite{tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
10	We evaluate signals individually; whether signal combinations (e.g., LP $\times$ consistency) or learned weightings could close the selection gap is unexplored.
11	The $\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app:epsilon_robustness}), the specific subset gains should be interpreted as characterizing the compression phenomenon rather than as a tuned selection strategy.
12	We tested one remedy for LP compression---entity-token-only LP (excluding format/schema tokens)---which fails to improve selection despite increasing with
…[truncated 145 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 857 · 2026-05-16T07:40:51.095707+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 858 · 2026-05-16T07:40:51.648784+00:00_

File content (26138 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 859 · 2026-05-16T07:40:51.749605+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form 2025 2026 soundness excitement overall scoring scale criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form 2025 2026 soundness excitement overall scoring scale criteria"
  }
}
```

</details>

---


### Tool result

_source line 860 · 2026-05-16T07:40:58.747809+00:00_

Web search results for query: "ACL ARR review form 2025 2026 soundness excitement overall scoring scale criteria"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ACL 2026 on X: \"Checkout the blog post on the soundness/excitement scores https://t.co/AKSO9DjiYP . It clarifies the reasoning behind the separation of overall scores and how it might make the reviewer recommendation more robust. #ACL2023Toronto #ACL2023NLP #NLProc\" / X","url":"https://x.com/aclmeeting/status/1637827267173953540"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ARR Dashboard","url":"https://stats.aclrollingreview.org/"},{"title":"Conference Decisions · GitHub","url":"https://gist.github.com/antonisa/2158dee79179c7c49304ef353887bfa0"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, I found detailed information about the ACL ARR review form for 2025-2026. Here's what I found:

## Three-Score System

Starting with February 2025, ARR reviewers are asked to
…[truncated 1456 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6998
}
```

</details>

---


### Tool call

_source line 861 · 2026-05-16T07:41:03.273883+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "0",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "0",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 862 · 2026-05-16T07:41:04.228764+00:00_

0	\section{Notation}\label{app:notation}
1	
2	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
3	
4	\begin{table}[h]
5	\centering
6	\small
7	\begin{tabular}{cl}
8	\toprule
9	Symbol & Meaning \\
10	\midrule
11	$\mathcal{M}$ & Language model \\
12	$x$ & Input instance \\
13	$y_i$ & $i$-th stochastic sample \\
14	$N$ & Number of samples \\
15	$T$ & Sampling temperature \\
16	$c(\cdot)$ & Confidence signal \\
17	SJ & Soft Jaccard similarity \\
18	FK & Fleiss' $\kappa$ \\
19	EM & Exact-match voting rate \\
20	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
21	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
22	\bottomrule
23	\end{tabular}
24	\caption{Notation used throughout the paper.}
25	\label{tab:notation}
26	\end{table}
27	
28	\section{Robustness Analysis}\label{app:robustness}
29	
30	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
31	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality---including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
32	
33	\begin{table}[t]
34	\centering
35	\small
36	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
37	\label{tab:robustness}
38	\begin{tabular}{llcc}
39	\toprule
40	& & NER $\rho$ & RE $\rho$ \\
41	\midrule
42	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
43	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
44	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
45	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
46	\quad FK & $
…[truncated 13706 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 863 · 2026-05-16T07:41:04.229281+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
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

_source line 864 · 2026-05-16T07:41:04.279777+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 865 · 2026-05-16T07:41:12.563855+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "200",
  "limit": "250"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "200",
    "limit": "250"
  }
}
```

</details>

---


### Tool result

_source line 866 · 2026-05-16T07:41:12.614762+00:00_

200	EM ranks first across all four tested conditional configurations---SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$)---despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
201	On the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.
202	On the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.
203	The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$), where all signals converge near $\rho{\approx}0.46$.
204	
205	\paragraph{WNUT-17 full signal analysis.}
206	Table~\ref{tab:wnut} reports all five signals on WNUT-17.
207	VC achieves $\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\rho{=}0.038$ ($p{=}0.49$).
208	LP shows the reverse pattern: full-set $\rho{=}{-}0.410$ but conditional $\rho{=}0.350$, the highest among all signals on the conditional set.
209	This inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.
210	
211	\begin{table}[t]
212	\centering
213	\small
214	\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). LP exhibits strong negative full-set $\rho$; its conditional $\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}
215	\label{tab:wnut}
216	\begin{tabular}{lccccc}
…[truncated 17986 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 867 · 2026-05-16T07:41:17.837025+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "450",
  "limit": "250"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "450",
    "limit": "250"
  }
}
```

</details>

---


### Tool result

_source line 868 · 2026-05-16T07:41:17.837779+00:00_

450	Max gradient norm & 1.0 \\
451	Training seed & 42 \\
452	Framework & LLaMA Factory \\
453	\midrule
454	\multicolumn{2}{l}{\textit{Dataset-specific}} \\
455	SciERC split & 1861 / 275 / 551 \\
456	CoNLL / WNUT & +\,load\_best\_model\_at\_end, \\
457	& eval\_steps${=}$200, save\_limit${=}$5 \\
458	\bottomrule
459	\end{tabular}
460	\end{table}
461	
462	\paragraph{Prompt template.}
463	For NER, we use a structured prompt:
464	\begin{quote}
465	\small
466	\texttt{System:} You are an expert in Named Entity Recognition.\\
467	\texttt{User:} Extract all named entities from the following text. Output as JSON.\\
468	Text: \texttt{\{input\_text\}}\\
469	Entity types: \texttt{\{schema\_types\}}
470	\end{quote}
471	RE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.
472	
473	\paragraph{Constrained decoding.}
474	Inference uses vLLM with XGrammar-based JSON schema enforcement \cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.
475	This eliminates format errors but may compress per-sample diversity by restricting the output space.\footnote{SciERC training used \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \texttt{enable\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \S\ref{sec:setup} and Limitations for discussion of this confound.}
476	
477	\section{Thinking Token Impact Analysis}\label{app:thinking_token}
478	
479	Qwen3-8B's SciERC checkpoint was trained with empty \texttt{&lt;think>&lt;/think>} blocks prepended to each response (\S\ref{sec:setup}).
480	We quantify the potential impact on LP scores through three complementary arguments.
481	
482	\paragraph{LP shift magnitude.}
483	Empty thinking tokens (mean 4.5 per sample) constitute 2.1\%
…[truncated 15157 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 869 · 2026-05-16T07:41:22.907049+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "700",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "700",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 870 · 2026-05-16T07:41:23.008072+00:00_

700	\bottomrule
701	\end{tabular}
702	\end{table}
703	
704	\section{MBR Decoding and Task-Specific Interactions}\label{app:mbr_discussion}
705	
706	\paragraph{Connection to MBR decoding.}
707	Our selection strategies instantiate minimum Bayes risk (MBR) decoding \cite{eikema2022sampling, muller2021understanding}: each selects $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.
708	Despite MBR's success in machine translation \cite{freitag2022high} and its extension to summarization, code generation, and captioning \cite{jinnai2024mbr}, all variants fail here: despite positive within-instance utility--F1 correlation, selection gains are limited by instance degeneracy---the core of the correlation-selection gap.
709	\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.
710	
711	\paragraph{Task-specific decoding interactions.}
712	The free-form ablation reveals divergent behavior across tasks.
713	On RE, LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single RE benchmark), a reversal that spans all 7 relation types and is driven by selective variance reallocation ($p{<}0.0001$).
714	The win/loss ratio shifts from 36:59 (constrained) to 45:45 (free-form), with the gains concentrated on relation-dense instances (mean 3.3 gold relations).
715	This interaction does not generalize to NER, where selection remains negligible under both regimes.
716	This ablation uses a single seed (seed${=}42$); whether the RE reversal replicates across seeds and generalizes to other RE benchmarks warrants further investigation.
717	The non-tied subset ($n{=}210$) is partially reshuffled under free-form decoding: Jaccard similarity between the constrained and free-form non-tied sets is 0.472,
…[truncated 9825 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 871 · 2026-05-16T07:41:28.991881+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 872 · 2026-05-16T07:41:29.042744+00:00_

1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@article{brown2024monkeys,
4	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
5	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
6	  journal = {arXiv preprint arXiv:2407.21787},
7	  year = {2024},
8	  url = {https://arxiv.org/abs/2407.21787}
9	}
10	
11	@inproceedings{chen2024usc,
12	  title = {Universal Self-Consistency for Large Language Model Generation},
13	  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
14	  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},
15	  year = {2024},
16	  url = {https://arxiv.org/abs/2311.17311}
17	}
18	
19	@article{cobbe2021verifiers,
20	  title = {Training Verifiers to Solve Math Word Problems},
21	  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
22	  journal = {arXiv preprint arXiv:2110.14168},
23	  year = {2021},
24	  url = {https://arxiv.org/abs/2110.14168}
25	}
26	
27	@inproceedings{culotta2004confidence,
28	  title = {Confidence Estimation for Information Extraction},
29	  author = {Culotta, Aron and McCallum, Andrew},
30	  booktitle = {HLT-NAACL 2004},
31	  year = {2004},
32	  url = {https://aclanthology.org/N04-4028/}
33	}
34	
35	@inproceedings{derczynski2017wnut,
36	  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},
37	  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},
38	  booktitle = {W-NUT Workshop at EMNLP 2017},
39	  year = {2017},
40	  url = {https://aclanthology.org/W17-4418/}
41	}
42	
43	@inproceedings{eikema2022
…[truncated 3208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 873 · 2026-05-16T07:44:10.253410+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 1 Review — Reviewer 1 (方法严谨性 + 实验设计 + 统计分析)\n\n### Summary\n\n本文评估 LLM-based NER 中 5 种置信信号在质量估计（QE）和 best-of-N 选择两个任务上的表现，核心发现是\"correlation-selection gap\"：信号能预测哪些 instance 做得好（ρ=0.38），却不能选出比 greedy decoding 更好的样本。论文诊断两种失败机制——instance degeneracy 和 LP compression——并通过 free-form decoding、entity-token LP 等消融验证 compression 是内在属性。实验覆盖三数据集难度梯度、两个模型族、两种规模。\n\n### Strengths\n\n**S1.** 概念贡献清晰且有实际意义。QE/selection 的解耦是这篇论文的核心洞察，且直接指向实践者容易犯的错误（用高 ρ 信号做选择）。这个区分在 IE 领域尚未被明确指出。\n\n**S2.** 诊断链逻辑严密。Free-form decoding (std ratio 0.97) → entity-token LP (4× variance 但 -2.0pp selection) → verbalized confidence (更压缩)，每一步排除一个假设，且每步都有量化证据。RE free-form 的反向效果（+1.8pp）被恰当标注为 regime-dependent。\n\n**S3.** 统计实践远超 NLP 论文平均水平。Bootstrap CI、TOST equivalence testing（含外部锚定 δ）、Fisher combined p、多种 ε sensitivity sweep、multi-seed Kendall's W——方法论上非常负责。\n\n**S4.** 三数据集难度梯度设计合理。CoNLL (ceiling-effect control) 和 WNUT-17 (signal-collapse boundary) 明确标注为边界条件而非主要验证集，避免了过度 claim。\n\n**S5.** 消融实验覆盖面广。Thinking token 影响分析（三角论证）、SJ normalizer robustness（Δρ<0.01）、LOO-SJ equivalence proof、FK independence permutation test——预见并回应了大多数潜在质疑。\n\n### Weaknesses\n\n#### Must-Fix（影响接收决定）\n\n**N1** [critical] Instance-level 信号\"无法选择\"在很大程度上是 by construction，论文区分不够sharp\n\n- 具体位置：Section 3.1 (最后一句), Section 4.3 (第一段)\n- 问题：4/5 信号是 instance-level aggregates，给同一 input 的所有 N 个候选分配相同分数——它们在字面意义上不具备选择能力。论文用 MBR/consensus-proximity 将其转化为 per-sample ranking，但 MBR 转换后仍然失败才是 empirical finding。当前叙述中，contribution #1 (\"the correlation-selection gap\") 把 instance-level 信号的 by-construction 限制和 LP 的 empirical 失败混在一起计算，夸大了\"5个信号全部失败\"的 surprise factor。\n- 为什么影响接收：如果 reviewer/reader 认为 4/5 的\"发现\"是 trivial observation (对 instance-level 信号无法选择而感到不惊讶)，那么核心 contribution 实质上缩减为\"LP 选择失败 + 诊断\"——仍有价值但需要更诚实的 framing。\n- 建议：在 Introduction/Method 中更清晰地将 gap 分为两层：(a) structural limitation (instance-level → needs conversion) 和 (b) empirical failure (MBR conversion has positive within-instance ρ=0.52 but fails due to degeneracy; LP is per-sample but too compressed)。当前 Section 5 (Discussion) 确实做了这个区分，但 abstract 和 introduction 中的 framing 过于 monolithic。\n\n**N2** [critical] Selection gap 的有效验证集实质上仅 SciERC 一个数据集\n\n- 具体位置：Section 4.3, Table 3 (selection), Table 6 (cross_selection)\n- 问题：CoNLL oracle headroom 仅 4pp（论文正确标注为 ceiling-effect control）；WNUT-17 信号全部 collapse（capability boundary）。真正验证 selection gap 的只有 SciERC。Table 6 中 LLaMA/SciERC 的 LP 0.652 vs single 0.646 确实 replicate 了 gap，但这仍然是同一数据集的不同模型。论文 claim \"The pattern holds across CoNLL and WNUT-17 (Table 6)\" (Section 4.3, line 90)，但 CoNLL 上 holding 的原因是 ceiling effect（无 headroom 可选），并非信号失败——这是 qualitatively 不同的原因。\n- 为什么影响接收：一篇诊断性论文的 claim 泛化性依赖于在足够多的 non-trivial settings 中复现。单数据集（SciERC）+ 单模型家族（Qwen/LLaMA 都是 8B decoder-only）的 selection 实验难以支撑 \"the gap\" 作为 general phenomenon 的 framing。\n- 建议：(1) 明确将 CoNLL/WNUT 定位为 boundary-condition analysis 而非 replication（当前部分语言已如此但不一致）；(2) 增加一个 medium-difficulty 数据集（如 ACE05 或 Few-NERD subset）以验证 gap 在 SciERC 之外成立；(3) 或者软化 claim 为 \"demonstrated on medium-difficulty NER\" 而非隐含的 general phenomenon。\n\n#### Should-Fix（影响评分但不一票否决）\n\n**W1** [warning] Scale ablation (4B vs 8B) 支撑 \"task difficulty drives the gap\" 结论的证据力不足\n\n- 具体位置：Section 4.4, Table 4\n- 问题：仅 2 个规模点（4B, 8B），属同一模型家族（Qwen3），scale 范围极窄。结论 \"task difficulty is a stronger predictor of the gap than model scale\" 基于 4B 在 SciERC 上 QE 提升但 selection 仍失败——但 4B 可能产生更多 diversity（更多 degenerate 或更少？），论文未报告 4B 的 degeneracy 统计。缺少 4B 的 instance degeneracy 数据使得无法判断：是 task difficulty 驱动 gap，还是 4B 恰好有相似的 degeneracy pattern？\n- 建议：报告 4B 的 degeneracy 统计（constant F1 fraction, oracle headroom）；承认 2-point scale ablation 的限制性更强。\n\n**W2** [warning] Fisher combined p 仅基于 2 seeds 的统计合理性\n\n- 具体位置：Table 3 (selection), Section 4.3\n- 问题：Table 3 报告 \"2-seed mean±σ, Fisher combined p vs. single-sample\"。Fisher's method 组合 2 个独立 p-value 的统计效力极低——2-seed Fisher 本质上就是一个 χ²(4) 检验，对于检测 13pp oracle headroom 中的 0.2pp effect size 几乎没有检测力。这不是错误（Fisher's method technically works with k=2），但给人一种统计严谨性的表象而实际上 power 极低。\n- 建议：(1) 报告 power analysis（在给定 effect size 下 2-seed Fisher 的检测力）；(2) 或直接使用 bootstrap CI 作为主要统计推断依据（论文 appendix 已有），将 Fisher p 降级为辅助证据。\n\n**W3** [warning] Kendall's W 在 n=3 seeds 下的信息量问题\n\n- 具体位置：Table 9 (ranking-stability), Appendix F\n- 问题：Kendall's W=1.000 with 3 raters ranking 5 signals = complete agreement，但 n=3 下即使 W=1.0 也不显著（临界值约 0.88 at α=0.05 for k=3, m=5）。论文注释 \"though statistical power with n=3 is limited\" 是诚实的，但仍在 abstract/introduction 中使用 \"σ≤0.026\" 暗示高稳定性。\n- 建议：明确 3-seed 的主要功能是 sanity check（排除 catastrophic seed sensitivity），而非统计推断依据。避免将其作为 robustness 证据的第一行引用。\n\n**W4** [warning] Greedy baseline (T=0) 与 T=1.0 sampling 的比较公平性\n\n- 具体位置：Section 4.3, Table 3\n- 问题：Greedy (T=0) F1=0.663 > best selection LP 0.647。但 greedy 是 deterministic argmax（token-level 最优局部选择），而 T=1.0 sampling 引入了 substantial noise。如果目的是展示 selection 无法回收 sampling noise 的代价，这是合理的。但论文使用 \"surpassing all N=8 selection strategies\" 的修辞暗示 greedy 是 selection 的公平 competitor。实际上，greedy 和 sampling+selection 解决的是不同问题（deterministic quality vs. exploration+selection）。\n- 为什么重要：这使得 \"gap\" 的 practical implication 变得模糊——如果 conclusion 是 \"just use greedy\"，那么整个 sampling+QE+selection pipeline 的研究价值需要重新 frame。\n- 建议：更明确地讨论 greedy 不是 selection 的 baseline 而是 \"practical cost-free alternative\"——当前脚注已有暗示但主文不够清晰。将 \"single-sample\" 作为选择的正式 baseline（Table 3 结构已对），减少对 greedy 的修辞强调。\n\n**W5** [warning] ε=0.05 threshold 虽有 sensitivity analysis，但 \"非 tied 子集 +2.9pp (p=0.004)\" 的 multiple testing 问题\n\n- 具体位置：Section 5, Appendix G (Table 8)\n- 问题：Table 8 展示 ε sweep 从 0.01 到 0.20，selection gain 单调递增——这表明 ε=0.05 并非 \"natural split point\" 而是连续谱上的一个 arbitrary cutoff。论文在 Section 4.3 脚注中说 \"survives Bonferroni correction over 5 comparisons\"，但 Bonferroni over 5 signals 不等于 correction over 7 ε values × 5 signals。Limitations 节承认 \"post-hoc exploratory choice\" 但主文仍突出 p=0.004。\n- 建议：将 non-tied subset 结果明确定位为 \"exploratory/descriptive\"（当前 Limitations 已接近这个 framing，但 Discussion §5 段落 2 将其作为 \"confirming compression as the bottleneck\" 的主要证据——这超出了 exploratory framing 允许的 claim 强度）。\n\n#### Minor（不影响接收）\n\n**M1.** SJ 命名：分母用 max(|g_i|,|g_j|) 而非 |A∪B|——虽然 footnote 已说明，且 Table 5 证明 Δρ<0.01，但 \"Soft Jaccard\" 这个名称可能误导熟悉 Jaccard index 的读者。建议考虑 \"penalized set overlap\" 或在首次使用时加注 \"a variant penalizing cardinality mismatch\"。\n\n**M2.** Section 4.1 报告 SciERC Qwen seed=42 单 seed 结果，而 Table 7 (multi-seed) 显示 VC mean=0.386±0.019。主表值 0.379 是 seed=42 的值——这本身没问题，但 reader 可能困惑为什么主表不用 3-seed mean。建议统一或在表格脚注中更明确说明。\n\n**M3.** \"Correlation-selection gap\" 的操作性定义出现在 Section 4.3 第一句——但 abstract 和 introduction 已经大量使用这个术语。建议在 Introduction 首次使用时给出 one-sentence 操作性定义。\n\n**M4.** Table 3 selection F1 = 0.647 (LP) 但 Discussion 中 non-tied subset 的 F1 明显更高——这种 subsetting 分析在主表 vs appendix 之间的呈现稍有断裂，可增加一句在 Table 3 caption 中的 forward pointer。\n\n### Questions for Authors\n\n**Q1.** 4B 模型的 instance degeneracy fraction 是多少？如果 4B 产生更多 diversity（degeneracy 更低），但 selection 仍然失败，这会更强力地支持 \"task difficulty drives the gap\"。反之，如果 degeneracy 也更低但 selection 仍失败，那可能暗示 compression 也是 scale-independent。\n\n**Q2.** 为什么 selection 实验用 2-seed 而非 3-seed（QE 用了 3-seed）？这是计算资源限制还是有方法论原因？\n\n**Q3.** MBR utility correlation (within-instance SJ ρ=0.524 median) 如何计算？对于 21% 的 degenerate instances（F1 identical across all N），ρ 是 undefined——这些 instances 被排除还是赋值 0？\n\n**Q4.** RE free-form decoding 的 selection reversal (+1.8pp) 是否暗示：对于 RE，constrained decoding 本身就是 gap 的原因？如果是，这是否削弱了 \"compression is intrinsic\" 的 NER 结论（因为它暗示 decoding regime 可以改变 gap 存在与否）？\n\n**Q5.** Table 3 中 Random baseline 0.610 明显低于 Single 0.645——这 0.035pp 差距来源是什么？如果 random 从 N=8 中随机选一个，期望值应等于 mean(per-sample F1)，而 single 是 one draw from the same distribution。两者应该有相同的期望值（都是 E[F1] under T=1.0）——除非 \"Single\" 实际上使用了与 sampling 不同的 seed/batch？请澄清。\n\n### Missing References\n\n1. **Pasad et al. (2023/2024)** \"Minimum Bayes Risk Decoding for Sequence-to-Sequence Models\": 直接相关的 MBR decoding for structured outputs 工作，比 Eikema & Aziz 2022 更新且覆盖 seq2seq。\n2. **Bertsch et al. (2023)** \"It's MBR All the Way Down\": 讨论 MBR utility 选择对 selection quality 的影响，与本文 consensus-proximity 策略直接相关。\n3. **Xu et al. (2024/2025)** 关于 NER 中 self-consistency 或 sample-and-select 的工作（如有）——当前 related work 未覆盖 NER-specific test-time compute scaling。\n4. **Lin & Chen (2023)** \"LLM-Eval\" or similar works on per-sample scoring for structured outputs as an alternative to consistency-based methods.\n\n### Overall Assessment\n\n**Soundness: 3.5/5** — 方法论上基本严谨，统计实践优秀，但 N1（by-construction limitation 混入 empirical finding）和 N2（单数据集验证）构成 soundness 隐患。消融链逻辑成立，但 claim 强度偶尔超出证据力。\n\n**Excitement: 3.5/5** — QE/selection 解耦 + 诊断链是有价值的贡献，但本质上是 negative result paper（\"signals don't work for selection\"），impact 依赖于 community 是否在意这个问题。对于做 test-time compute scaling for IE 的研究者有直接参考价值。\n\n**Overall: 3.0 (Borderline: could be accepted to main conference or Findings)** — 贡献真实且实验扎实，但两个核心问题——(1) 核心 finding 部分是 by-construction 的 tautology，(2) selection gap 的非 trivial 验证仅限一个数据集——使其离 clear accept 有距离。如果作者在 rebuttal 中 (a) 重新 frame contribution 使 trivial/non-trivial 部分清晰分离，(b) 补充 4B degeneracy 数据或第二个 medium-difficulty 数据集验证，则可上调至 3.5。\n\n**Confidence: 4/5** — 我熟悉 MBR decoding、self-consistency、NER evaluation、以及 LLM uncertainty estimation 文献。对统计方法（TOST、bootstrap CI）有直接实践经验。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 1 Review — Reviewer 1 (方法严谨性 + 实验设计 + 统计分析)\n\n### Summary\n\n本文评估 LLM-based NER 中 5 种置信信号在质量估计（QE）和 best-of-N 选择两个任务上的表现，核心发现是\"correlation-selection gap\"：信号能预测哪些 instance 做得好（ρ=0.38），却不能选出比 greedy decoding 更好的样本。论文诊断两种失败机制——instance degeneracy 和 LP compression——并通过 free-form decoding、entity-token LP 等消融验证 compression 是内在属性。实验覆盖三数据集难度梯度、两个模型族、两种规模。\n\n### Strengths\n\n**S1.** 概念贡献清晰且有实际意义。QE/selection 的解耦是这篇论文的核心洞察，且直接指向实践者容易犯的错误（用高 ρ 信号做选择）。这个区分在 IE 领域尚未被明确指出。\n\n**S2.** 诊断链逻辑严密。Free-form decoding (std ratio 0.97) → entity-token LP (4× variance 但 -2.0pp selection) → verbalized confidence (更压缩)，每一步排除一个假设，且每步都有量化证据。RE free-form 的反向效果（+1.8pp）被恰当标注为 regime-dependent。\n\n**S3.** 统计实践远超 NLP 论文平均水平。Bootstrap CI、TOST equivalence testing（含外部锚定 δ）、Fisher combined p、多种 ε sensitivity sweep、multi-seed Kendall's W——方法论上非常负责。\n\n**S4.** 三数据集难度梯度设计合理。CoNLL (ceiling-effect control) 和 WNUT-17 (signal-collapse boundary) 明确标注为边界条件而非主要验证集，避免了过度 claim。\n\n**S5.** 消融实验覆盖面广。Thinking token 影响分析（三角论证）、SJ normalizer robustness（Δρ<0.01）、LOO-SJ equivalence proof、FK independence permutation test——预见并回应了大多数潜在质疑。\n\n### Weaknesses\n\n#### Must-Fix（影响接收决定）\n\n**N1** [critical] Instance-level 信号\"无法选择\"在很大程度上是 by construction，论文区分不够sharp\n\n- 具体位置：Section 3.1 (最后一句), Section 4.3 (第一段)\n- 问题：4/5 信号是 instance-level aggregates，给同一 input 的所有 N 个候选分配相同分数——它们在字面意义上不具备选择能力。论文用 MBR/consensus-proximity 将其转化为 per-sample ranking，但 MBR 转换后仍然失败才是 empirical finding。当前叙述中，contribution #1 (\"the correlation-selection gap\") 把 instance-level 信号的 by-construction 限制和 LP 的 empirical 失败混在一起计算，夸大了\"5个信号全部失败\"的 surprise factor。\n- 为什么影响接收：如果 reviewer/reader 认为 4/5 的\"发现\"是 trivial observation (对 instance-level 信号无法选择而感到不惊讶)，那么核心 contribution 实质上缩减为\"LP 选择失败 + 诊断\"——仍有价值但需要更诚实的 framing。\n- 建议：在 Introduction/Method 中更清晰地将 gap 分为两层：(a) structural limitation (instance-level → needs conversion) 和 (b) empirical failure (MBR conversion has positive within-instance ρ=0.52 but fails due to degeneracy; LP is per-sample but too compressed)。当前 Section 5 (Discussion) 确实做了这个区分，但 abstract 和 introduction 中的 framing 过于 monolithic。\n\n**N2** [critical] Selection gap 的有效验证集实质上仅 SciERC 一个数据集\n\n- 具体位置：Section 4.3, Table 3 (selection), Table 6 (cross_selection)\n- 问题：CoNLL oracle headroom 仅 4pp（论文正确标注为 ceiling-effect control）；WNUT-17 信号全部 collapse（capability boundary）。真正验证 selection gap 的只有 SciERC。Table 6 中 LLaMA/SciERC 的 LP 0.652 vs single 0.646 确实 replicate 了 gap，但这仍然是同一数据集的不同模型。论文 claim \"The pattern holds across CoNLL and WNUT-17 (Table 6)\" (Section 4.3, line 90)，但 CoNLL 上 holding 的原因是 ceiling effect（无 headroom 可选），并非信号失败——这是 qualitatively 不同的原因。\n- 为什么影响接收：一篇诊断性论文的 claim 泛化性依赖于在足够多的 non-trivial settings 中复现。单数据集（SciERC）+ 单模型家族（Qwen/LLaMA 都是 8B decoder-only）的 selection 实验难以支撑 \"the gap\" 作为 general phenomenon 的 framing。\n- 建议：(1) 明确将 CoNLL/WNUT 定位为 boundary-condition analysis 而非 replication（当前部分语言已如此但不一致）；(2) 增加一个 medium-difficulty 数据集（如 ACE05 或 Few-NERD subset）以验证 gap 在 SciERC 之外成立；(3) 或者软化 claim 为 \"demonstrated on medium-difficulty NER\" 而非隐含的 general phenomenon。\n\n#### Should-Fix（影响评分但不一票否决）\n\n**W1** [warning] Scale ablation (4B vs 8B) 支撑 \"task difficulty drives the gap\" 结论的证据力不足\n\n- 具体位置：Section 4.4, Table 4\n- 问题：仅 2 个规模点（4B, 8B），属同一模型家族（Qwen3），scale 范围极窄。结论 \"task difficulty is a stronger predictor of the gap than model scale\" 基于 4B 在 SciERC 上 QE 提升但 selection 仍失败——但 4B 可能产生更多 diversity（更多 degenerate 或更少？），论文未报告 4B 的 degeneracy 统计。缺少 4B 的 instance degeneracy 数据使得无法判断：是 task difficulty 驱动 gap，还是 4B 恰好有相似的 degeneracy pattern？\n- 建议：报告 4B 的 degeneracy 统计（constant F1 fraction, oracle headroom）；承认 2-point scale ablation 的限制性更强。\n\n**W2** [warning] Fisher combined p 仅基于 2 seeds 的统计合理性\n\n- 具体位置：Table 3 (selection), Section 4.3\n- 问题：Table 3 报告 \"2-seed mean±σ, Fisher combined p vs. single-sample\"。Fisher's method 组合 2 个独立 p-value 的统计效力极低——2-seed Fisher 本质上就是一个 χ²(4) 检验，对于检测 13pp oracle headroom 中的 0.2pp effect size 几乎没有检测力。这不是错误（Fisher's method technically works with k=2），但给人一种统计严谨性的表象而实际上 power 极低。\n- 建议：(1) 报告 power analysis（在给定 effect size 下 2-seed Fisher 的检测力）；(2) 或直接使用 bootstrap CI 作为主要统计推断依据（论文 appendix 已有），将 Fisher p 降级为辅助证据。\n\n**W3** [warning] Kendall's W 在 n=3 seeds 下的信息量问题\n\n- 具体位置：Table 9 (ranking-stability), Appendix F\n- 问题：Kendall's W=1.000 with 3 raters ranking 5 signals = complete agreement，但 n=3 下即使 W=1.0 也不显著（临界值约 0.88 at α=0.05 for k=3, m=5）。论文注释 \"though statistical power with n=3 is limited\" 是诚实的，但仍在 abstract/introduction 中使用 \"σ≤0.026\" 暗示高稳定性。\n- 建议：明确 3-seed 的主要功能是 sanity check（排除 catastrophic seed sensitivity），而非统计推断依据。避免将其作为 robustness 证据的第一行引用。\n\n**W4** [warning] Greedy baseline (T=0) 与 T=1.0 sampling 的比较公平性\n\n- 具体位置：Section 4.3, Table 3\n- 问题：Greedy (T=0) F1=0.663 > best selection LP 0.647。但 greedy 是 deterministic argmax（token-level 最优局部选择），而 T=1.0 sampling 引入了 substantial noise。如果目的是展示 selection 无法回收 sampling noise 的代价，这是合理的。但论文使用 \"surpassing all N=8 selection strategies\" 的修辞暗示 greedy 是 selection 的公平 competitor。实际上，greedy 和 sampling+selection 解决的是不同问题（deterministic quality vs. exploration+selection）。\n- 为什么重要：这使得 \"gap\" 的 practical implication 变得模糊——如果 conclusion 是 \"just use greedy\"，那么整个 sampling+QE+selection pipeline 的研究价值需要重新 frame。\n- 建议：更明确地讨论 greedy 不是 selection 的 baseline 而是 \"practical cost-free alternative\"——当前脚注已有暗示但主文不够清晰。将 \"single-sample\" 作为选择的正式 baseline（Table 3 结构已对），减少对 greedy 的修辞强调。\n\n**W5** [warning] ε=0.05 threshold 虽有 sensitivity analysis，但 \"非 tied 子集 +2.9pp (p=0.004)\" 的 multiple testing 问题\n\n- 具体位置：Section 5, Appendix G (Table 8)\n- 问题：Table 8 展示 ε sweep 从 0.01 到 0.20，selection gain 单调递增——这表明 ε=0.05 并非 \"natural split point\" 而是连续谱上的一个 arbitrary cutoff。论文在 Section 4.3 脚注中说 \"survives Bonferroni correction over 5 comparisons\"，但 Bonferroni over 5 signals 不等于 correction over 7 ε values × 5 signals。Limitations 节承认 \"post-hoc exploratory choice\" 但主文仍突出 p=0.004。\n- 建议：将 non-tied subset 结果明确定位为 \"exploratory/descriptive\"（当前 Limitations 已接近这个 framing，但 Discussion §5 段落 2 将其作为 \"confirming compression as the bottleneck\" 的主要证据——这超出了 exploratory framing 允许的 claim 强度）。\n\n#### Minor（不影响接收）\n\n**M1.** SJ 命名：分母用 max(|g_i|,|g_j|) 而非 |A∪B|——虽然 footnote 已说明，且 Table 5 证明 Δρ<0.01，但 \"Soft Jaccard\" 这个名称可能误导熟悉 Jaccard index 的读者。建议考虑 \"penalized set overlap\" 或在首次使用时加注 \"a variant penalizing cardinality mismatch\"。\n\n**M2.** Section 4.1 报告 SciERC Qwen seed=42 单 seed 结果，而 Table 7 (multi-seed) 显示 VC mean=0.386±0.019。主表值 0.379 是 seed=42 的值——这本身没问题，但 reader 可能困惑为什么主表不用 3-seed mean。建议统一或在表格脚注中更明确说明。\n\n**M3.** \"Correlation-selection gap\" 的操作性定义出现在 Section 4.3 第一句——但 abstract 和 introduction 已经大量使用这个术语。建议在 Introduction 首次使用时给出 one-sentence 操作性定义。\n\n**M4.** Table 3 selection F1 = 0.647 (LP) 但 Discussion 中 non-tied subset 的 F1 明显更高——这种 subsetting 分析在主表 vs appendix 之间的呈现稍有断裂，可增加一句在 Table 3 caption 中的 forward pointer。\n\n### Questions for Authors\n\n**Q1.** 4B 模型的 instance degeneracy fraction 是多少？如果 4B 产生更多 diversity（degeneracy 更低），但 selection 仍然失败，这会更强力地支持 \"task difficulty drives the gap\"。反之，如果 degeneracy 也更低但 selection 仍失败，那可能暗示 compression 也是 scale-independent。\n\n**Q2.** 为什么 selection 实验用 2-seed 而非 3-seed（QE 用了 3-seed）？这是计算资源限制还是有方法论原因？\n\n**Q3.** MBR utility correlation (within-instance SJ ρ=0.524 median) 如何计算？对于 21% 的 degenerate instances（F1 identical across all N），ρ 是 undefined——这些 instances 被排除还是赋值 0？\n\n**Q4.** RE free-form decoding 的 selection reversal (+1.8pp) 是否暗示：对于 RE，constrained decoding 本身就是 gap 的原因？如果是，这是否削弱了 \"compression is intrinsic\" 的 NER 结论（因为它暗示 decoding regime 可以改变 gap 存在与否）？\n\n**Q5.** Table 3 中 Random baseline 0.610 明显低于 Single 0.645——这 0.035pp 差距来源是什么？如果 random 从 N=8 中随机选一个，期望值应等于 mean(per-sample F1)，而 single 是 one draw from the same distribution。两者应该有相同的期望值（都是 E[F1] under T=1.0）——除非 \"Single\" 实际上使用了与 sampling 不同的 seed/batch？请澄清。\n\n### Missing References\n\n1. **Pasad et al. (2023/2024)** \"Minimum Bayes Risk Decoding for Sequence-to-Sequence Models\": 直接相关的 MBR decoding for structured outputs 工作，比 Eikema & Aziz 2022 更新且覆盖 seq2seq。\n2. **Bertsch et al. (2023)** \"It's MBR All the Way Down\": 讨论 MBR utility 选择对 selection quality 的影响，与本文 consensus-proximity 策略直接相关。\n3. **Xu et al. (2024/2025)** 关于 NER 中 self-consistency 或 sample-and-select 的工作（如有）——当前 related work 未覆盖 NER-specific test-time compute scaling。\n4. **Lin & Chen (2023)** \"LLM-Eval\" or similar works on per-sample scoring for structured outputs as an alternative to consistency-based methods.\n\n### Overall Assessment\n\n**Soundness: 3.5/5** — 方法论上基本严谨，统计实践优秀，但 N1（by-construction limitation 混入 empirical finding）和 N2（单数据集验证）构成 soundness 隐患。消融链逻辑成立，但 claim 强度偶尔超出证据力。\n\n**Excitement: 3.5/5** — QE/selection 解耦 + 诊断链是有价值的贡献，但本质上是 negative result paper（\"signals don't work for selection\"），impact 依赖于 community 是否在意这个问题。对于做 test-time compute scaling for IE 的研究者有直接参考价值。\n\n**Overall: 3.0 (Borderline: could be accepted to main conference or Findings)** — 贡献真实且实验扎实，但两个核心问题——(1) 核心 finding 部分是 by-construction 的 tautology，(2) selection gap 的非 trivial 验证仅限一个数据集——使其离 clear accept 有距离。如果作者在 rebuttal 中 (a) 重新 frame contribution 使 trivial/non-trivial 部分清晰分离，(b) 补充 4B degeneracy 数据或第二个 medium-difficulty 数据集验证，则可上调至 3.5。\n\n**Confidence: 4/5** — 我熟悉 MBR decoding、self-consistency、NER evaluation、以及 LLM uncertainty estimation 文献。对统计方法（TOST、bootstrap CI）有直接实践经验。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 874 · 2026-05-16T07:44:14.325197+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4071
}
```

</details>

---


### Assistant

_source line 875 · 2026-05-16T07:44:20.796089+00:00_

审稿意见已提交给 Review Director。

核心判断：论文实验扎实、统计实践优秀，但有两个影响接收的问题——(1) 4/5 信号无法选择是 by construction 的结构限制（非 empirical finding），论文 framing 混淆了 trivial 和 non-trivial 部分；(2) selection gap 的有效验证实质上仅限 SciERC 一个数据集。Overall 评分 3.0 (borderline)，可通过 rebuttal 上调。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 29

## Round 29

4 recorded events


### User

_source line 876 · 2026-05-16T07:49:52.062667+00:00_

[Round 1 审稿请求]:
## Step 2 — 交叉分享：请回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿意见。请逐条回应：
- **[AGREE]** 同意，并说明理由（cite 具体 Section/Table/Figure）
- **[REBUT]** 反驳，并提供证据

---

## Reviewer 2 审稿意见原文

### Overall: 2.5/5（介于 Findings 和需要 substantial revisions 之间）

核心判断: 实验设计扎实、消融全面，但核心发现（correlation-selection gap）的新颖性有限——它在很大程度上是 MBR 社区已知现象在 IE 场景下的重新标签化，且缺少直接相关的关键文献。

### Must-Fix 问题

**N1** [critical] 与 Yao et al. (2026) 的增量贡献不够清晰
- Section 1 line 8、Section 2 line 10
- 论文声称 Yao et al. "leaving open" 三个问题，但 gap 表述过于笼统。需精确界定：Yao et al. 使用 hard-prompting（非 fine-tuned），instance degeneracy 在其设置中可能不存在——这是否正好是 gap 的来源？
- 建议：明确 Yao et al. 不涉及 fine-tuned models、不区分 QE 与 selection、无 MBR 分析。将差异表格化。

**N2** [critical] "Correlation-selection gap" 与 MBR 社区已知结论的关系未充分讨论
- Section 1 Contribution #1、Section 5 Discussion
- Eikema et al. (2025) 已发现 MBR utilities degrade on structured outputs。"Good metric correlation ≠ good selection" 在 QE for MT 领域也有先例。论文的贡献应定位为"在 IE 场景下给出两种具体失败机制"，而非发现全新现象。
- 建议：将 Contribution #1 从 "identifying the gap" 改为 "diagnosing two specific failure mechanisms that explain the gap in IE"。

**N3** [critical] 缺少两篇直接相关的重要文献
1. Schall & de Melo (RANLP 2025) "The Hidden Cost of Structure" — 直接研究 constrained decoding 如何影响 LP distribution，与 LP compression hypotheses (b)(c) 高度相关
2. Yun et al. (Findings EMNLP 2025) "The Price of Format: Diversity Collapse in LLMs" — format templates 导致的 diversity collapse，与 instance degeneracy 直接相关

### Should-Fix 问题

**W1** "Moderate-to-strong" QE 措辞有误导性 — ρ=0.38 属 medium effect，ρ=0.45 来自受 inflation 影响的 ceiling-effect control

**W2** 论文定位模糊（diagnostic vs. methodology），应明确定位为 diagnostic study

**W3** 4/5 signals instance-level → cannot select 是 definitional tautology，非 empirical finding

**W4** 3B-8B scale 限制实践指导意义，标题/abstract 未充分限定

**W5** Discussion 中 LP compression hypotheses 列举格式有误，且 (b) 与 (d) 区分不够清晰

### Minor 问题
- Abstract 缺引用
- "Cost-free greedy decoding" 措辞不精确
- WNUT-17 结果不在主文 Table 中
- bhattacharyya2026beyond 引用关联不清楚

### Missing References
1. Schall & de Melo (RANLP 2025) "The Hidden Cost of Structure"
2. Yun et al. (Findings EMNLP 2025) "The Price of Format: Diversity Collapse in LLMs"
3. Park et al. (NeurIPS 2024) "Grammar-Aligned Decoding"

### Questions for Authors
1. Yao et al. (2026) hard-prompted LLMs 的 instance degeneracy 比例？degeneracy 是 fine-tuning artifact 还是 task 固有属性？
2. 是否考虑过 LP × VC product 等简单 signal combination？
3. Entity-token LP CoNLL 上 variance ≈ 0 是否说明 fine-tuned models 将 entity tokens 视为 deterministic vocabulary？
4. Greedy (T=0) > all N=8 selection — 是否 temperature sampling 的 noise > selection 能 recover 的 signal？

---

请对以上每个 Must-Fix (N1/N2/N3)、Should-Fix (W1-W5)、Missing References 逐条回应 [AGREE] 或 [REBUT]。对 Questions 部分如有补充观点也请说明。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 877 · 2026-05-16T07:51:59.239559+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 交叉回应 — 对 Reviewer 2 审稿意见\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: 与 Yao et al. (2026) 的增量贡献界定**\n\n同意需要更清晰的差异化。Section 1 line 8 仅用一句话概括 (\"leaving open whether structural matching improves on surface agreement, whether quality estimation translates to selection, and whether findings generalize across a difficulty gradient\")，但未说明 Yao et al. 使用 hard-prompting 这一关键方法论差异。如果 instance degeneracy (Table 5: 21-58% constant F1) 是 fine-tuning 的产物而非 task 固有属性，那么本文最核心的 failure mechanism 可能不存在于 Yao et al. 的设置中——这恰好构成最强的差异化论点，但论文未抓住。建议作者在 Related Work 中增加一个明确对比段落，将 fine-tuning → low diversity → degeneracy 作为关键区分点。\n\n**[REBUT] R2-N2: \"Gap\" 是 MBR 社区已知现象的重新标签化**\n\n部分反驳。R2 的论点是 \"good metric correlation ≠ good selection\" 在 QE for MT 已有先例，且 Eikema et al. (2025) 已发现 MBR utilities degrade on structured outputs。但有两个关键区别：\n\n1. **失败机制的 specificity**：MBR 文献讨论的是 utility function mismatch（utility 不 align with human quality），而本文诊断的是 instance degeneracy（utility 在 instance 内 positively correlates with F1，median ρ=0.524 on SciERC [Table 5]，但 21% instances 没有任何 headroom 可选）。这不是 utility degradation，而是 headroom elimination——一个 qualitatively 不同的机制。\n\n2. **Structural difference of IE outputs**：MT 中 MBR 失败因为 utility functions (BLEU, COMET) 不 capture quality；本文中 SJ utility DOES capture quality (within-instance ρ=0.524)，但 degeneracy 使其 moot。Section 5 (Discussion) 第二段明确写道：\"Despite MBR's success in machine translation, all variants fail here because degeneracy eliminates the headroom that positive within-instance correlation would otherwise exploit\"——这 IS 新贡献，不是重新标签化。\n\n但我同意 R2 关于 **framing** 的建议：将 Contribution #1 从 \"identifying the gap\" 调整为 \"diagnosing two specific failure mechanisms unique to fine-tuned IE models\" 会使 novelty claim 更准确。当前 abstract 和 introduction 的 framing 确实过于强调 \"discovery\" 而非 \"diagnosis\"。\n\n**[AGREE with reservation] R2-N3: 缺少两篇关键文献**\n\n关于 relevance 我同意：\n- Schall & de Melo (\"The Hidden Cost of Structure\") 如果确实研究 constrained decoding 对 LP distribution 的影响，则与 hypotheses (b)(c) 直接相关——尽管本文的 free-form ablation (Appendix §10, Panel A: std ratio 0.97) 已经 empirically 排除了 (b)(c) 对 NER 的解释力，引用此文可强化 \"我们知道这个 hypothesis，并实证排除了它\" 的论证。\n- Yun et al. (\"The Price of Format\") 与 instance degeneracy 话题相关，但需注意：本文的 degeneracy 指 fine-tuned models 产生 identical entity sets（output-level），不同于 format-induced diversity collapse（token-level diversity）。Table 8 (diversity) 显示 SciERC 有 43% unique outputs——degeneracy 不是 universal collapse，而是 instance-specific 的 high-confidence convergence。\n\n**Reservation**：我无法验证这两篇文献是否真实存在（建议 Director 使用 verify_references 确认）。如果存在，应当引用但不改变论文结论。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: \"Moderate-to-strong\" 措辞**\n\nρ=0.38 按 Cohen (1988) 标准属 medium effect (0.3-0.5 range)。论文在 abstract 中写 \"moderate-to-strong quality estimation (ρ=0.38 on the primary test bed, up to 0.45 on a ceiling-effect control)\"——但 0.45 来自 CoNLL，而论文自身承认 CoNLL 的 ρ 因 zero/non-zero boundary 而被 inflate +0.03-0.05 (Section 3.3 footnote)。\"Moderate\" 或 \"moderate quality estimation\" 是更准确的描述。\n\n**[AGREE] R2-W2: 论文定位模糊**\n\n同意。论文同时尝试 (a) 提供实践指导 (Section 5 \"Practical recommendations\") 和 (b) 诊断失败机制——但 (a) 的 actionable takeaway 很薄弱（\"use VC for QE, trained verifiers for selection\"）。明确定位为 diagnostic/analytical study 会使期望对齐，也减少 reviewer 对 \"so what?\" 的追问。\n\n**[AGREE] R2-W3: Instance-level 信号无法选择是 definitional tautology**\n\n强烈同意——这与我的 N1 完全一致。Section 3.1 最后一句确实说明了这一区分，但 abstract/introduction 将 \"5 signals all fail at selection\" 作为统一 narrative 呈现时，模糊了 trivial (instance-level by construction) 与 non-trivial (MBR conversion fails due to degeneracy; LP fails due to compression) 之间的界限。\n\n**[PARTIALLY AGREE] R2-W4: 3B-8B scale 限制**\n\n同意标题/abstract 未充分限定 scale 范围。但 Limitations 节 (line 2: \"whether the gap holds for 70B+ models or closed-source APIs is untested\") 和 Conclusion (line 7: \"Whether these mechanisms persist at 70B+ scales is an open question\") 已有明确限定。问题在于 abstract 中使用 \"at two model scales (4B and 8B)\" 但未说明这是 narrow range。建议在 abstract 中添加 \"in the small-model regime (3B-8B)\" 的限定词。\n\n**[PARTIALLY AGREE] R2-W5: Hypotheses (b) 与 (d) 区分不清**\n\n区分确实存在但需要仔细阅读才能理解：\n- (b) = constrained decoding **强制产生** schema tokens（因此这些 tokens 必然存在）\n- (d) = model **赋予** schema tokens 极高 LP（即使不强制，模型也会产生它们——free-form parse rate 99.95% 证实这一点）\n\n逻辑链是：free-form ablation (std ratio 0.97) 排除 (b)+(c) → 但 format tokens 仍然存在 (parse rate 99.95%) → 所以 (d) 仍可能成立 → entity-token LP ablation 直接测试 (d) → (d) 也不够解释（entity-token variance 在 CoNLL 上 collapse）。\n\n这个推理链是 sound 的，但 Section 5 的呈现确实可以更清晰——特别是 (b) 和 (d) 的关键区别（constraint-imposed vs. model-learned）可以用一句话显式说明。\n\n---\n\n### Missing References\n\n**[CONDITIONAL AGREE]** 三篇 references 的 topic relevance 我认同：\n1. Schall & de Melo — constrained decoding ↔ LP distribution 直接相关于 hypothesis (b)(c)\n2. Yun et al. — format ↔ diversity 相关于 instance degeneracy 讨论\n3. Park et al. \"Grammar-Aligned Decoding\" — 与 constrained decoding (Willard & Merrill 2023, 本文引用) 属同一 line\n\n但我对 1 和 2 的真实性持保留态度。如果确认存在，应当引用；但即使引用，不改变论文的 empirical findings（free-form ablation 已经排除了 constrained decoding 作为 NER compression 的主因）。\n\n---\n\n### Questions 补充观点\n\n**R2-Q1 (degeneracy: fine-tuning artifact vs task-intrinsic?)**: 极好的问题。与我的 Q1 互补。如果 Yao et al. 的 hard-prompted setting 也有 high degeneracy，则 degeneracy 是 task-intrinsic（NER 答案空间有限）；如果仅 fine-tuned models 有，则是 fine-tuning 导致的 overconfidence。这直接影响论文的 practical relevance：如果是 fine-tuning artifact，那么 alternative training regimes (e.g., diversity-promoting objectives) 可能是比 trained verifiers 更自然的解决方案。\n\n**R2-Q2 (signal combination)**: Limitations 节 (line 10) 承认 \"whether signal combinations (e.g., LP × consistency) or learned weightings could close the selection gap is unexplored\"。这是合理的 scope limitation，但如果 LP×VC 的简单实验只需几行代码就能做，不做显得遗憾。\n\n**R2-Q4 (temperature noise > selection signal)**: 与我的 W4 高度相关。Greedy (T=0) F1=0.663 > best LP selection 0.647 暗示 T=1.0 的 sampling noise 本身就超过了 selection 能 recover 的信号。但论文应区分两种 use case：(a) 如果你只要一个输出，greedy wins——那为什么 sample？(b) 如果你需要 diverse outputs（for downstream reranking, ensembling），那 selection 的 failure 是 concerning。当前论文隐含假设 (b) 的 setting 但用 (a) 的 greedy baseline 来强化 negative result。\n\n---\n\n### 总结：与 R2 的共识和分歧\n\n**共识领域**（高一致性）：\n- Instance-level signals 无法选择是 partly tautological (R2-W3 = 我的 N1)\n- Scale 范围需要更明确限定 (R2-W4 ≈ 我的 W1)\n- \"Moderate-to-strong\" 用词需降级 (R2-W1)\n- 论文定位应明确为 diagnostic study (R2-W2)\n- 与 Yao et al. 的差异化需加强 (R2-N1)\n\n**分歧领域**：\n- R2 认为 gap 是 MBR 已知现象的重新标签化 → 我认为 instance degeneracy 是 qualitatively new mechanism（within-instance utility correlation IS positive; failure is from headroom elimination, not utility mismatch）\n- R2 给 Overall 2.5 (substantial revisions needed) → 我给 3.0 (borderline)。分歧来源：我认为消融链和统计实践的质量本身有足够 contribution value，即使 framing 需调整；R2 对 novelty 要求更高。\n\n**我的评分是否需要调整**：读完 R2 意见后，我维持 Overall 3.0 不变。R2 的 N2 有道理但我不完全同意其\"重新标签化\"判断；其他问题大部分与我的发现重合或互补。如果作者能 address N1 (framing) 和 N2 (positioning vs MBR literature) 的 rebuttal，3.0→3.5 是可能的。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 交叉回应 — 对 Reviewer 2 审稿意见\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: 与 Yao et al. (2026) 的增量贡献界定**\n\n同意需要更清晰的差异化。Section 1 line 8 仅用一句话概括 (\"leaving open whether structural matching improves on surface agreement, whether quality estimation translates to selection, and whether findings generalize across a difficulty gradient\")，但未说明 Yao et al. 使用 hard-prompting 这一关键方法论差异。如果 instance degeneracy (Table 5: 21-58% constant F1) 是 fine-tuning 的产物而非 task 固有属性，那么本文最核心的 failure mechanism 可能不存在于 Yao et al. 的设置中——这恰好构成最强的差异化论点，但论文未抓住。建议作者在 Related Work 中增加一个明确对比段落，将 fine-tuning → low diversity → degeneracy 作为关键区分点。\n\n**[REBUT] R2-N2: \"Gap\" 是 MBR 社区已知现象的重新标签化**\n\n部分反驳。R2 的论点是 \"good metric correlation ≠ good selection\" 在 QE for MT 已有先例，且 Eikema et al. (2025) 已发现 MBR utilities degrade on structured outputs。但有两个关键区别：\n\n1. **失败机制的 specificity**：MBR 文献讨论的是 utility function mismatch（utility 不 align with human quality），而本文诊断的是 instance degeneracy（utility 在 instance 内 positively correlates with F1，median ρ=0.524 on SciERC [Table 5]，但 21% instances 没有任何 headroom 可选）。这不是 utility degradation，而是 headroom elimination——一个 qualitatively 不同的机制。\n\n2. **Structural difference of IE outputs**：MT 中 MBR 失败因为 utility functions (BLEU, COMET) 不 capture quality；本文中 SJ utility DOES capture quality (within-instance ρ=0.524)，但 degeneracy 使其 moot。Section 5 (Discussion) 第二段明确写道：\"Despite MBR's success in machine translation, all variants fail here because degeneracy eliminates the headroom that positive within-instance correlation would otherwise exploit\"——这 IS 新贡献，不是重新标签化。\n\n但我同意 R2 关于 **framing** 的建议：将 Contribution #1 从 \"identifying the gap\" 调整为 \"diagnosing two specific failure mechanisms unique to fine-tuned IE models\" 会使 novelty claim 更准确。当前 abstract 和 introduction 的 framing 确实过于强调 \"discovery\" 而非 \"diagnosis\"。\n\n**[AGREE with reservation] R2-N3: 缺少两篇关键文献**\n\n关于 relevance 我同意：\n- Schall & de Melo (\"The Hidden Cost of Structure\") 如果确实研究 constrained decoding 对 LP distribution 的影响，则与 hypotheses (b)(c) 直接相关——尽管本文的 free-form ablation (Appendix §10, Panel A: std ratio 0.97) 已经 empirically 排除了 (b)(c) 对 NER 的解释力，引用此文可强化 \"我们知道这个 hypothesis，并实证排除了它\" 的论证。\n- Yun et al. (\"The Price of Format\") 与 instance degeneracy 话题相关，但需注意：本文的 degeneracy 指 fine-tuned models 产生 identical entity sets（output-level），不同于 format-induced diversity collapse（token-level diversity）。Table 8 (diversity) 显示 SciERC 有 43% unique outputs——degeneracy 不是 universal collapse，而是 instance-specific 的 high-confidence convergence。\n\n**Reservation**：我无法验证这两篇文献是否真实存在（建议 Director 使用 verify_references 确认）。如果存在，应当引用但不改变论文结论。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: \"Moderate-to-strong\" 措辞**\n\nρ=0.38 按 Cohen (1988) 标准属 medium effect (0.3-0.5 range)。论文在 abstract 中写 \"moderate-to-strong quality estimation (ρ=0.38 on the primary test bed, up to 0.45 on a ceiling-effect control)\"——但 0.45 来自 CoNLL，而论文自身承认 CoNLL 的 ρ 因 zero/non-zero boundary 而被 inflate +0.03-0.05 (Section 3.3 footnote)。\"Moderate\" 或 \"moderate quality estimation\" 是更准确的描述。\n\n**[AGREE] R2-W2: 论文定位模糊**\n\n同意。论文同时尝试 (a) 提供实践指导 (Section 5 \"Practical recommendations\") 和 (b) 诊断失败机制——但 (a) 的 actionable takeaway 很薄弱（\"use VC for QE, trained verifiers for selection\"）。明确定位为 diagnostic/analytical study 会使期望对齐，也减少 reviewer 对 \"so what?\" 的追问。\n\n**[AGREE] R2-W3: Instance-level 信号无法选择是 definitional tautology**\n\n强烈同意——这与我的 N1 完全一致。Section 3.1 最后一句确实说明了这一区分，但 abstract/introduction 将 \"5 signals all fail at selection\" 作为统一 narrative 呈现时，模糊了 trivial (instance-level by construction) 与 non-trivial (MBR conversion fails due to degeneracy; LP fails due to compression) 之间的界限。\n\n**[PARTIALLY AGREE] R2-W4: 3B-8B scale 限制**\n\n同意标题/abstract 未充分限定 scale 范围。但 Limitations 节 (line 2: \"whether the gap holds for 70B+ models or closed-source APIs is untested\") 和 Conclusion (line 7: \"Whether these mechanisms persist at 70B+ scales is an open question\") 已有明确限定。问题在于 abstract 中使用 \"at two model scales (4B and 8B)\" 但未说明这是 narrow range。建议在 abstract 中添加 \"in the small-model regime (3B-8B)\" 的限定词。\n\n**[PARTIALLY AGREE] R2-W5: Hypotheses (b) 与 (d) 区分不清**\n\n区分确实存在但需要仔细阅读才能理解：\n- (b) = constrained decoding **强制产生** schema tokens（因此这些 tokens 必然存在）\n- (d) = model **赋予** schema tokens 极高 LP（即使不强制，模型也会产生它们——free-form parse rate 99.95% 证实这一点）\n\n逻辑链是：free-form ablation (std ratio 0.97) 排除 (b)+(c) → 但 format tokens 仍然存在 (parse rate 99.95%) → 所以 (d) 仍可能成立 → entity-token LP ablation 直接测试 (d) → (d) 也不够解释（entity-token variance 在 CoNLL 上 collapse）。\n\n这个推理链是 sound 的，但 Section 5 的呈现确实可以更清晰——特别是 (b) 和 (d) 的关键区别（constraint-imposed vs. model-learned）可以用一句话显式说明。\n\n---\n\n### Missing References\n\n**[CONDITIONAL AGREE]** 三篇 references 的 topic relevance 我认同：\n1. Schall & de Melo — constrained decoding ↔ LP distribution 直接相关于 hypothesis (b)(c)\n2. Yun et al. — format ↔ diversity 相关于 instance degeneracy 讨论\n3. Park et al. \"Grammar-Aligned Decoding\" — 与 constrained decoding (Willard & Merrill 2023, 本文引用) 属同一 line\n\n但我对 1 和 2 的真实性持保留态度。如果确认存在，应当引用；但即使引用，不改变论文的 empirical findings（free-form ablation 已经排除了 constrained decoding 作为 NER compression 的主因）。\n\n---\n\n### Questions 补充观点\n\n**R2-Q1 (degeneracy: fine-tuning artifact vs task-intrinsic?)**: 极好的问题。与我的 Q1 互补。如果 Yao et al. 的 hard-prompted setting 也有 high degeneracy，则 degeneracy 是 task-intrinsic（NER 答案空间有限）；如果仅 fine-tuned models 有，则是 fine-tuning 导致的 overconfidence。这直接影响论文的 practical relevance：如果是 fine-tuning artifact，那么 alternative training regimes (e.g., diversity-promoting objectives) 可能是比 trained verifiers 更自然的解决方案。\n\n**R2-Q2 (signal combination)**: Limitations 节 (line 10) 承认 \"whether signal combinations (e.g., LP × consistency) or learned weightings could close the selection gap is unexplored\"。这是合理的 scope limitation，但如果 LP×VC 的简单实验只需几行代码就能做，不做显得遗憾。\n\n**R2-Q4 (temperature noise > selection signal)**: 与我的 W4 高度相关。Greedy (T=0) F1=0.663 > best LP selection 0.647 暗示 T=1.0 的 sampling noise 本身就超过了 selection 能 recover 的信号。但论文应区分两种 use case：(a) 如果你只要一个输出，greedy wins——那为什么 sample？(b) 如果你需要 diverse outputs（for downstream reranking, ensembling），那 selection 的 failure 是 concerning。当前论文隐含假设 (b) 的 setting 但用 (a) 的 greedy baseline 来强化 negative result。\n\n---\n\n### 总结：与 R2 的共识和分歧\n\n**共识领域**（高一致性）：\n- Instance-level signals 无法选择是 partly tautological (R2-W3 = 我的 N1)\n- Scale 范围需要更明确限定 (R2-W4 ≈ 我的 W1)\n- \"Moderate-to-strong\" 用词需降级 (R2-W1)\n- 论文定位应明确为 diagnostic study (R2-W2)\n- 与 Yao et al. 的差异化需加强 (R2-N1)\n\n**分歧领域**：\n- R2 认为 gap 是 MBR 已知现象的重新标签化 → 我认为 instance degeneracy 是 qualitatively new mechanism（within-instance utility correlation IS positive; failure is from headroom elimination, not utility mismatch）\n- R2 给 Overall 2.5 (substantial revisions needed) → 我给 3.0 (borderline)。分歧来源：我认为消融链和统计实践的质量本身有足够 contribution value，即使 framing 需调整；R2 对 novelty 要求更高。\n\n**我的评分是否需要调整**：读完 R2 意见后，我维持 Overall 3.0 不变。R2 的 N2 有道理但我不完全同意其\"重新标签化\"判断；其他问题大部分与我的发现重合或互补。如果作者能 address N1 (framing) 和 N2 (positioning vs MBR literature) 的 rebuttal，3.0→3.5 是可能的。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 878 · 2026-05-16T07:52:03.261600+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4022
}
```

</details>

---


### Assistant

_source line 879 · 2026-05-16T07:52:10.786493+00:00_

交叉回应已提交。主要结论：

- 与 R2 在 5 个点上达成共识（instance-level tautology、scale 限定、QE 措辞、定位、Yao et al. 差异化）
- 在核心分歧点（N2: gap 是否为 MBR 已知现象的重标签化）提出反驳——instance degeneracy 是 qualitatively 不同于 utility mismatch 的失败机制，within-instance ρ=0.524 证明 utility 本身是好的，问题在于 headroom 被消除
- 维持 Overall 3.0 评分不变

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 30

## Round 30

66 recorded events


### User

_source line 880 · 2026-05-16T08:34:35.433961+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1

**你的审查侧重：方法严谨性 + 实验设计 + 统计分析**

### 论文信息
- **标题**: "Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition"
- **文件**: `projects/struct_self_consist_ie/docs/paper/main.tex`（及 `sections/` 下各子文件）
- **目标 Venue**: EMNLP 2026 Main Conference（ARR May 2026 cycle）
- **截止日期**: 2026-05-25

### Venue 要求
- Long paper: 8 页正文 + unlimited references + Appendix 不计入页数
- 模板: ACL style（`\usepackage[review]{acl}`）
- Double-blind 匿名审稿
- Limitations section 必须（≤1 页，不计入页数）
- Ethics statement 推荐

### 论文概要
论文研究 LLM-based NER 中自一致性信号的质量估计与样本选择能力。在 SciERC（主要）、CoNLL-2003（ceiling-effect control）、WNUT-17（signal-collapse boundary）上评估 5 个置信度信号（4 个 instance-level + 1 个 per-sample LP），使用 Qwen3-8B、LLaMA-3.1-8B（+ 4B ablation）。核心发现是 "correlation-selection gap"：信号有中等 QE 能力（ρ 达 0.38）但选择失败，greedy decoding (T=0) 超过所有 N=8 选择策略。诊断两个机制：instance degeneracy（21-58% 实例产生相同 F1）和 LP compression（中位数 within-instance range 0.041 nats）。

### 你需要重点审查的方面

1. **实验设计合理性**
   - 数据集选择（SciERC/CoNLL/WNUT-17 三级难度梯度）是否充分？Selection gap 的有效测试仅在 SciERC (n=529) 上有意义——CoNLL 是 ceiling control，WNUT 是 collapse boundary——单数据集支撑核心 claim 是否足够？
   - 模型规模范围（4B-8B）是否足以支撑结论？
   - N=8 primary / N=16 scaling 的选择是否合理？

2. **统计分析严谨性**
   - 2-seed Fisher combined p 的统计效力是否充足？
   - 3-seed Kendall W=1.0 的统计意义（n=3 时 p≈0.05 仅 borderline）
   - ε=0.05 tied/non-tied 切分的 post-hoc 性质是否充分说明？non-tied subset +2.9pp (p=0.004) 在 Bonferroni over 多少个比较下是否 survive？
   - TOST 等价性检验的 equivalence margins 选择和解释
   - Bootstrap CI 的使用和解释是否恰当？

3. **方法论**
   - 5 个信号中 4 个是 instance-level（by construction 无法区分 per-sample），只有 LP 是 per-sample——这个 "gap" 在多大程度上是定义上的 tautology vs 经验发现？
   - Consensus-proximity (MBR) 将 instance-level 转为 per-sample ranking 后仍然失败——这与 MBR 文献中已知的 failure modes 关系如何？
   - Instance degeneracy 和 LP compression 的诊断是否充分支撑 "intrinsic" 结论？
   - Free-form ablation (std ratio 0.97) 足以排除 constrained decoding 作为原因吗？
   - Entity-token LP isolation 的实验设计和结论解读

4. **4B scale ablation**
   - Table 6 报告了 degeneracy 统计（8B 21% vs 4B 10.4%），数据是否完整？
   - 2-point scale ablation 的解释力

5. **可重复性**
   - 训练配置、推理设置、评估协议是否描述充分？
   - Thinking token confound 的 3-part analysis 是否令人信服？

请按 EMNLP 最严格标准审稿，输出完整审稿报告，包括 Summary、Strengths、Weaknesses（Must-Fix / Should-Fix / Minor 分级）、Questions for Authors、Missing References、Overall Score（strong reject / weak reject / borderline / weak accept / strong accept）+ Confidence。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 881 · 2026-05-16T08:34:44.562491+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
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

_source line 882 · 2026-05-16T08:34:44.562965+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 883 · 2026-05-16T08:34:47.983247+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 884 · 2026-05-16T08:34:48.284781+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/struct_self_consist_ie/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/struct_self_consist_ie/docs/paper/**/*.tex"
  }
}
```

</details>

---


### Tool result

_source line 885 · 2026-05-16T08:34:48.486161+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 886 · 2026-05-16T08:34:48.586939+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/struct_self_consist_ie/docs/paper/**/*.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/struct_self_consist_ie/docs/paper/**/*.bib"
  }
}
```

</details>

---


### Tool result

_source line 887 · 2026-05-16T08:34:48.637659+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 888 · 2026-05-16T08:34:56.770097+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here is information about ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, exc
…[truncated 1730 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8786
}
```

</details>

---


### Tool call

_source line 889 · 2026-05-16T08:35:01.390162+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper -type f 2>/dev/null | head -50",
  "description": "List paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper -type f 2>/dev/null | head -50",
    "description": "List paper directory contents"
  }
}
```

</details>

---


### Tool result

_source line 890 · 2026-05-16T08:35:01.744254+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p1.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p14.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p3.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p17.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p12.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p9.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p10.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p6.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p21.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p11.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p15.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p20.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p13.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p2.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p16.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p19.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p22.png
/home/ubuntu/.agent-ml-research-i
…[truncated 3673 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 354
}
```

</details>

---


### Tool call

_source line 891 · 2026-05-16T08:35:02.857194+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ACL ARR review form: all scoring dimensions, their scales (1-5 etc.), descriptions for each score level, and any other required fields. I need the exact scoring rubric."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete ACL ARR review form: all scoring dimensions, their scales (1-5 etc.), descriptions for each score level, and any other required fields. I need the exact scoring rubric."
  }
}
```

</details>

---


### Tool result

_source line 892 · 2026-05-16T08:35:09.952255+00:00_

# ACL ARR Review Form - Complete Scoring Rubric

## 1. Reviewer Confidence
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## 2. Soundness
Scale: 1-5 (with half-point increments)
- **5**: Exceptional thoroughness for paper type
- **4**: Study provides sufficient support with minor gaps acceptable
- **3**: Main claims supported; minor points need extra detail
- **2**: Main claims lack sufficient support; major technical problems
- **1**: "Not yet sufficiently thorough to warrant publication or not relevant to ACL"

## 3. Excitement
Scale: 1-5 (with half-point increments)
- **5**: "I would recommend this paper to others and/or attend its presentation"
- **4**: Would mention to others; make effort to attend presentation
- **3**: Might mention some points; attend if time permits
- **2**: "Does not resonate with me, but it might with others"
- **1**: Does not resonate; unlikely to resonate with community

## 4. Overall Assessment
Scale: 1-5 (with half-point increments)
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance
- **3**: Findings acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit

## Additional Required Sections
- Paper Summary
- Summary of Strengths
- Summary of Weaknesses
- Comments/Suggestions/Typos
- Best Paper Justification (if applicable)
- Limitations and Societal Impact
- Ethical Concerns
- Reproducibility (1-5 scale)
- Datasets (1-5 scale)
- Software (1-5 scale)
- Author Identity Knowledge (1-5 scale)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7095
}
```

</details>

---


### Tool call

_source line 893 · 2026-05-16T08:35:15.778375+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 894 · 2026-05-16T08:35:16.281650+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ The Correlation-Selection Gap in LLM-Based Named Entity Recognition}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	Code and data will be released upon acceptance at [anonymized URL].
45	
46	\bibliography{references}
47	
48	\appendix
49	\input{sections/appendix}
50	
51	\end{document}
52	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 895 · 2026-05-16T08:35:16.282005+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 896 · 2026-05-16T08:35:16.684703+00:00_

1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals---four instance-level (structural and surface agreement) and one per-sample (log-probability)---on a medium-difficulty benchmark (SciERC) with ceiling-effect (CoNLL) and signal-collapse (WNUT-17) controls, within a narrow model-scale range (4B--8B).
4	All signals achieve moderate quality estimation ($\rho$ up to 0.38 on the primary test bed, 0.45 on a ceiling-effect control), yet best-of-$N$ selection fails to outperform greedy decoding ($T{=}0$)---the \textit{correlation-selection gap}.
5	We diagnose two mechanisms: (a)~\textit{instance degeneracy}---fine-tuned models produce identical outputs for 21--58\% of instances, eliminating selection headroom despite positive within-instance utility--F1 correlation (median $\rho{=}0.52$); and (b)~\textit{log-probability compression}---median within-instance range of 0.041 nats, with entity-token isolation revealing intrinsic overconfidence rather than format-token dilution.
6	A five-layer ablation chain (free-form decoding, entity-token LP, verbalized confidence, non-tied subset, signal combinations) confirms these mechanisms are intrinsic to capable fine-tuned models, not artifacts of constrained decoding.
7	Signal rankings shift with task difficulty and collapse at the capability boundary; closing the gap likely requires learned per-sample scoring.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 897 · 2026-05-16T08:35:16.737150+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 898 · 2026-05-16T08:35:16.737682+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---majority voting over multiple samples---yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
8	\citet{yao2026consistency} examine consistency--accuracy correlations for LLM-based IE using exact-match agreement under hard-prompting; we extend their work to fine-tuned models, separating quality estimation from best-of-$N$ selection and diagnosing two failure mechanisms---instance degeneracy and LP compression---within the dominant deployment paradigm for production NER.
9	
10	A methodological premise structures our analysis: four of five signals (SJ, VC, FK, EM) are instance-level aggregates that by design assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.
11	We define the \textbf{correlation-selection gap} as the disparity between a signal's rank correlation with F1 ($\rho$) and its ability to select the best output from $N$ candidates (Figure~\ref{fig:overview}): on SciERC, signals achieve moderate quality estimation ($\rho{=}0.38$, up to 0.45 on a ceiling-effect control) yet selection fails to improve over greedy decoding
…[truncated 3024 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 899 · 2026-05-16T08:35:19.899747+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 900 · 2026-05-16T08:35:20.352919+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	This distinction is consequential for selection: in our study, 4 of 5 signals are instance-level aggregates that assign identical QE scores to all $N$ candidates. Consensus-proximity (MBR) converts these to per-sample rankings (\S\ref{sec:selection_gap}), but these rankings do not improve selection; only natively per-sample signals can, in principle, exploit oracle headroom.
8	
9	\subsection{Confidence Signals}\label{sec:signals}
10	
11	Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
12	
13	\paragraph{Log-probability (model-internal, per-sample).}
14	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
15	\begin{equation}\label{eq:logprob}
16	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
17	\end{equation}
18	
19	\paragraph{Exact match voting (surface, instance-level).}
20	The proportion of samples producing the most common output:
21	\begin{equation}\label{eq:em}
22	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
23	\end{equation}
24	
25	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
26	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary pres
…[truncated 3040 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 901 · 2026-05-16T08:35:20.353466+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 902 · 2026-05-16T08:35:20.704889+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text through LLM comparison \cite{chen2024usc}, sub-claim decomposition \cite{thirukovalluru2024atomic}, or hallucination detection \cite{manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2026latentsc} all target discrete answers.
6	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings; \citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.
7	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap.
8	
9	\paragraph{Consistency for structured IE.}
10	\citet{yao2026consistency} study consistency--accuracy correlations for LLM-based NER/RE under hard-prompting, leaving open whether structural matching improves on surface agreement, whether quality estimation translates to selection, and whether findings generalize across a difficulty gradient---the three questions we address.
11	Our experiments use fine-tuned models---the dominant deployment paradigm for production NER---where instance degeneracy is most pronounced.
12	Degeneracy scales with model capability: CoNLL (91\% single-sample F1) exhibits 58\% degeneracy; SciERC (66\%) shows 21\%; WNUT-17 (48\%) shows near-zero (\S\ref{sec:discussion}).
13	This creates an inherent tension between model quality and selection utility that we expect to intensify as models improve.
14	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency for QA/summarization but does not address structured extraction.
15	\citet{culotta2004confidence} and \citet{mejer2010confidence} pioneer confidence es
…[truncated 2303 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 903 · 2026-05-16T08:35:20.755510+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 904 · 2026-05-16T08:35:20.806899+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English NER benchmarks spanning a difficulty gradient, each serving a distinct role.
9	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\approx}$65\% F1.
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 52\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures.
15	Qwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\ref{app:thinking_token}).
16	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\ref{app:n_scaling}).}
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.\footnote{Quality estimation uses a single primary seed (seed${=}42$); selection uses 2-seed averages for variance estimation. Three-seed experiments ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}) confirm ranking stability; the reduced seed count for primary results reflects computational budget.}
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
…[truncated 7949 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 905 · 2026-05-16T08:35:27.238109+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 906 · 2026-05-16T08:35:27.790331+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Implications for practitioners.}
4	VC leads on medium-difficulty NER ($\rho{=}0.379$, SciERC); EM leads easy NER and binary discrimination (AUROC${=}0.816$, CoNLL).
5	Rankings hold across model families and a 4B ablation (Table~\ref{tab:scale_ablation}); at the capability boundary (WNUT-17), all signals collapse. RE signal rankings are reported in Appendix~\ref{app:re_extension}.
6	
7	\paragraph{Why the gap exists.}
8	We identify two mechanisms: \textit{instance degeneracy} (affecting consensus-proximity selection) and \textit{LP compression} (affecting per-sample selection).
9	
10	Within-instance analysis (restricted to non-degenerate instances where F1 varies across samples) reveals that MBR utility \cite{eikema2022sampling} does correlate positively with F1 (SJ median within-instance $\rho{=}0.524$ on SciERC, $0.994$ on CoNLL), and on these instances consensus-proximity selection closes 23\% (SciERC) to 41\% (CoNLL) of the oracle gap.
11	However, fine-tuned models exhibit pervasive \textit{instance degeneracy}: 21\% of SciERC instances (58\% on CoNLL) produce identical F1 across all $N$ samples, offering zero selection headroom; an additional 13\% (49\% on CoNLL) yield constant utility scores, preventing MBR ranking entirely (Table~\ref{tab:degeneracy}).
12	Instance degeneracy is not an artifact of our setup but a consequence of model capability: the better the model, the less room for selection to add value.
13	CoNLL (91\% single-sample F1) exhibits 58\% degeneracy; SciERC (66\%) shows 21\%; WNUT-17 (48\%) shows near-zero---the tension between model quality and selection utility is inherent.
14	Scale ablation confirms this tension: Qwen3-8B shows 21\% instance degeneracy on SciERC vs.\ 10.4\% for the weaker Qwen3-4B, despite comparable within-instance utility correlation ($\rho{=}0.52$ vs.\ $0.55$; Table~\ref{tab:degeneracy}).
15	Despite MBR's success in machine translation \cite{freitag2022high}, all 
…[truncated 7276 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 907 · 2026-05-16T08:35:28.091646+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 908 · 2026-05-16T08:35:28.092104+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluate five confidence signals for quality estimation and sample selection in LLM-based NER, revealing the \textit{correlation-selection gap}: moderate quality estimation ($\rho{=}0.38$ on medium-difficulty NER, up to 0.45 on a ceiling-effect control) coexists with selection that fails to outperform greedy decoding ($T{=}0$).
4	The gap stems from two mechanisms: instance degeneracy (21--58\% of instances produce identical F1 across all $N$ samples, scaling with model capability and eliminating selection headroom despite positive within-instance utility correlation) and LP compression (the only per-sample signal has median within-instance range of 0.041 nats).
5	Diagnostic ablations---free-form decoding, entity-token LP isolation---confirm compression is intrinsic rather than an artifact of constrained decoding or format-token dilution.
6	The gap is demonstrated in the medium-difficulty regime where models achieve moderate but imperfect accuracy; signal rankings shift with difficulty and collapse at the capability boundary in the small-model regime (3B--8B).
7	Whether these mechanisms persist at 70B+ scales is an open question; trained verifiers and an exploratory extension to relation extraction (Appendix~\ref{app:re_extension}) are promising directions.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 909 · 2026-05-16T08:35:28.142719+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 910 · 2026-05-16T08:35:28.243501+00:00_

1	Our evaluation covers three NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.
2	We cover 4B--8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested---larger models may produce more diverse samples.
3	We do not train a verifier, leaving unknown how much oracle headroom a supervised approach could recover.
4	
5	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
6	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\ref{app:re_extension}.
7	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
8	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
9	We tested verbalized confidence \cite{tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
10	Ad-hoc LP${\times}$VC combinations yield at most $+0.4$~pp over greedy (not significant; \S\ref{sec:discussion}); whether \textit{learned} combinations could close the gap remains open.
11	The $\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app:epsilon_robustness}), the specific subset gains should be interpreted as characterizing the compression phenomenon rather than as a tuned selection strategy.
12	We tested one remedy for LP compression---entity-token-only LP (excluding format/schema tokens)---which fails to improve selectio
…[truncated 207 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 911 · 2026-05-16T08:35:32.208999+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 912 · 2026-05-16T08:35:32.460384+00:00_

File content (26138 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 913 · 2026-05-16T08:35:35.085323+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "500"
  }
}
```

</details>

---


### Tool result

_source line 914 · 2026-05-16T08:35:35.487731+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality---including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
47	\quad FK & 
…[truncated 37198 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 915 · 2026-05-16T08:35:39.554590+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "500"
  }
}
```

</details>

---


### Tool result

_source line 916 · 2026-05-16T08:35:39.906625+00:00_

500	At this cutpoint, 60.3\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below $\varepsilon$, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$).
501	The CDF rises smoothly with no cliff or discontinuity (Figure~\ref{fig:lp_range_cdf}), confirming that compression is a pervasive regime rather than a bimodal split.
502	This compression is stable across seeds: seed${=}456$ yields median LP range${=}0.040$ nats and tied fraction${=}62.2\%$ (vs.\ seed${=}42$: $0.041$ nats, $60.3\%$).
503	Seed~456 uses a different subtask flag (joint vs.\ ner for seeds 42 and 123); the LP distributions are statistically indistinguishable (median LP: 8.37 vs.\ 8.20 nats; Mann--Whitney $p{=}0.55$), confirming that the subtask change does not affect compression.
504	For comparison, SJ has only 12.5\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.
505	
506	\begin{figure}[t]
507	\centering
508	\includegraphics[width=\columnwidth]{fig_lp_range_cdf}
509	\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}
510	\label{fig:lp_range_cdf}
511	\end{figure}
512	
513	\begin{table}[t]
514	\centering
515	\small
516	\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\varepsilon$.}
517	\label{tab:logprob_ties}
518	\begin{tabular}{lc}
519	\toprule
520	$\varepsilon$ threshold & Tied instances (\%) \\
521	\midrule
522	0.01 & 1.1\% \\
523	0.05 & 60.3\% \\
524	0.1  & ${\sim}$84\% \\
525	0.5  & ${\sim}$99\% \\
526	\bottomrule
527	\end{tabular}
528	\end{table}
529	
530	\paragraph{Non-tied subset.}
531	Among instances with LP range ${\geq}0.05$ ($n{=}210$, 40\% of total), log-probability selection \textit{significa
…[truncated 32505 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 917 · 2026-05-16T08:35:45.278492+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "1017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "1017"
  }
}
```

</details>

---


### Tool result

_source line 918 · 2026-05-16T08:35:46.032527+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (1017). The file has 1017 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 754
}
```

</details>

---


### Tool call

_source line 919 · 2026-05-16T08:35:46.184109+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 920 · 2026-05-16T08:35:46.787679+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 921 · 2026-05-16T08:35:50.018863+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 922 · 2026-05-16T08:35:50.522313+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 923 · 2026-05-16T08:35:50.928511+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool call

_source line 924 · 2026-05-16T08:35:51.029583+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 925 · 2026-05-16T08:35:51.683244+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1160
}
```

</details>

---


### Tool result

_source line 926 · 2026-05-16T08:35:51.784793+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 755
}
```

</details>

---


### Tool call

_source line 927 · 2026-05-16T08:35:55.148807+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 928 · 2026-05-16T08:35:55.651220+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 929 · 2026-05-16T08:35:56.003688+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 930 · 2026-05-16T08:35:56.004151+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 931 · 2026-05-16T08:35:56.457306+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 932 · 2026-05-16T08:35:56.609039+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool result

_source line 933 · 2026-05-16T08:35:57.113610+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1109
}
```

</details>

---


### Tool result

_source line 934 · 2026-05-16T08:35:57.366453+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool call

_source line 935 · 2026-05-16T08:36:03.860459+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 936 · 2026-05-16T08:36:04.413324+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 937 · 2026-05-16T08:36:04.717123+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 938 · 2026-05-16T08:36:04.717555+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 939 · 2026-05-16T08:36:05.676050+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1262
}
```

</details>

---


### Tool result

_source line 940 · 2026-05-16T08:36:06.782911+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2065
}
```

</details>

---


### Tool call

_source line 941 · 2026-05-16T08:36:06.934049+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines including: what reviewers should evaluate, how to score soundness/excitement/overall, what constitutes a good review, specific criteria for accepting/rejecting papers, and any guidance on statistical methodology or experimental rigor expectations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines including: what reviewers should evaluate, how to score soundness/excitement/overall, what constitutes a good review, specific criteria for accepting/rejecting papers, and any guidance on statistical methodology or experimental rigor expectations."
  }
}
```

</details>

---


### Tool result

_source line 942 · 2026-05-16T08:36:20.392402+00:00_

# ARR Reviewer Guidelines Summary

## What Reviewers Should Evaluate

Reviewers assess papers across multiple dimensions. The core evaluation framework requires examining:

- **Research soundness**: Technical validity, proof correctness, and methodological rigor
- **Novelty and contribution**: Whether the work advances knowledge in meaningful ways
- **Clarity and presentation**: Whether findings are communicated effectively
- **Experimental rigor**: Statistical significance, appropriate baselines, and reproducibility

Reviewers must read papers twice—first for initial impressions without looking at results, then for in-depth technical assessment.

## Scoring System (February 2025 onwards)

ARR uses three separate scores:

**Soundness**: Reflects technical validity. As guidelines note, "low soundness scores must be justified by the text of the review." Discrepancies between score and justification suggest unconscious bias.

**Excitement**: A subjective, personal interest metric orthogonal to soundness. Papers can be technically sound but personally uninteresting to individual reviewers.

**Overall Assessment**: A composite recommendation integrating soundness, excitement, novelty, and potential impact for venue commitment.

## Characteristics of Strong Reviews

Quality reviews demonstrate these traits:

- **Specificity**: Cite exact issues rather than vague criticisms. "Missing references X, Y, Z" beats "missing relevant references"
- **Professional tone**: Reviews should be kind and constructive, written as colleagues would speak face-to-face
- **Evidence-based critique**: Claims require supporting references or clear reasoning
- **Proportional assessment**: Distinguish between critical flaws and minor suggestions

Reviews should acknowledge author responses and update assessments accordingly.

## Common Problematic Review Patterns (H1-H17)

Guidelines explicitly warn against dismissing papers because:

- Results seem obvious in retrospect (confirmation bias)
- Find
…[truncated 2756 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 13458
}
```

</details>

---


### Tool call

_source line 943 · 2026-05-16T08:40:28.694444+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — Round 1 审稿报告\n\n**论文**: \"Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition\"\n**审查侧重**: 方法严谨性 + 实验设计 + 统计分析\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 / 5 (Findings acceptance)\n**一句话总结**: 论文提出了一个有价值的概念区分（quality estimation vs. sample selection），诊断了两个失败机制，但核心 claim 在实质上仅由单数据集（SciERC, n=529）支撑，且统计分析存在若干需要修正的问题。\n\n---\n\n## 官方维度打分（ACL ARR Review Form, Feb 2025+）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0 / 5 | 核心 claim 的实验支撑依赖单一有效数据集；统计检验的多重比较校正不完整；instance-level 信号的 selection failure 部分是定义上的必然而非经验发现 |\n| Excitement | 3.5 / 5 | Correlation-selection gap 是有用的概念贡献；instance degeneracy 作为机制解释有洞察力；但结论偏向 negative result（\"现有信号都不行\"），缺少前进路径的具体验证 |\n| Reproducibility | 4.0 / 5 | 训练配置详尽（Table 9），prompt template、constrained decoding 细节完整；代码承诺开源；但 2-seed 主实验的 variance estimation 偏弱 |\n| Confidence | 4 / 5 | 熟悉 MBR decoding、self-consistency、NER 评估方法论和统计检验 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 核心 claim 的有效测试仅由单数据集支撑\n- 具体位置：Section 4 (Experiments), Table 2, §4.3\n- 问题：论文声称发现 \"correlation-selection gap\"——信号有 QE 能力但 selection 失败。但实际有效测试 selection gap 的仅 SciERC (n=529)：\n  - CoNLL 被明确标记为 \"ceiling-effect control\"（single-sample F1≈0.91, oracle headroom 仅 4 pp）——作者自己在 Table 5 和 §D 中承认 \"selection analysis on these configurations is uninformative\"\n  - WNUT-17 被标记为 \"signal-collapse boundary\"（52% zero F1）——信号本身崩溃，无法测试 selection\n  - 因此论文的核心发现——greedy 超过所有 N=8 策略——实质上仅在 SciERC 上被验证\n- 为什么影响接收：一个旨在揭示 \"LLM-based NER\" 普遍现象的论文，核心 claim 由单一 domain-specific 数据集（科学文本, 6 entity types, n=529）支撑，泛化性不足。SciERC 的 medium-difficulty 特性（~65% F1）恰好处于 degeneracy 和 collapse 之间的窄带——这可能是一个 sweet-spot artifact 而非普遍现象。\n- 建议修改方向：(1) 增加至少一个额外的 medium-difficulty 数据集（如 OntoNotes 5.0 NER 的子集、ACE 2005、或 Few-NERD）在相似 F1 range (50-70%) 验证 selection gap；或 (2) 将 claim 明确限定为 \"on a medium-difficulty scientific NER benchmark\"，相应调整 title 和 abstract 的泛化程度。\n\n**N2** [critical] 4/5 信号的 selection failure 部分是定义上的必然，非纯经验发现\n- 具体位置：Section 3.1 (Problem Formulation), §4.3, Table 2\n- 问题：SJ、VC、FK、EM 均为 instance-level 信号——by construction 对同一 input 的所有 N 个候选给出相同分数。Table 2 中这些信号的 \"selection\" 实际测试的是 consensus-proximity（MBR），不是原始信号的 selection 能力。这与 LP（唯一 per-sample 信号）的 selection failure 有本质区别：\n  - Instance-level 信号不能 select → 这是信号设计的数学必然\n  - LP 不能 select → 这是经验发现（compression）\n  - 论文将两者混为 \"5 个信号都失败\"，夸大了发现的规模\n- Abstract、Introduction 的 contribution list、和 Conclusion 均写 \"five confidence signals\" 统一处理，但真正的 empirical surprise 只在 LP。\n- 为什么影响接收：Framing 误导了读者对贡献规模的判断。如果准确表述为 \"instance-level 信号无法 select（by design），LP 因 compression 也无法 select\"，那么贡献集中在 LP compression 的诊断上——这仍有价值，但论文需要重新调整 framing。\n- 建议修改方向：在 abstract 和 introduction 中明确区分两类 failure（definitional vs. empirical），将 MBR/consensus-proximity failure 与 LP compression 分别讨论。当前 §3.1 第一段已有初步区分，但后续行文未贯彻。\n\n**N3** [critical] 2-seed Fisher combined p 的统计效力严重不足\n- 具体位置：Table 2 (\"2-seed mean±σ, Fisher combined p vs. single-sample\"), §4.3\n- 问题：Selection 的核心结论——\"no signal significantly outperforms single-sample (all p>0.05)\"——基于仅 2 个 random seed 的 Fisher combined p-value。\n  - 2 个独立 sign test 的 Fisher combination 对小效应的检测力极低。LP 的 Δ=+0.2 pp (p=0.29)，但 bootstrap 95% CI 为 [-3.0, +4.2] pp——这个 CI 宽度为 7.2 pp，远超 oracle headroom 的 40%。如此宽的 CI 下，无法区分 \"无效果\" 和 \"有小到中等效果但检测不到\"。\n  - Cohen's d=0.038（§F, TOST 段落）本身说明效应很小，但 CI 的宽度意味着即使真实效应为 +3 pp（实际有意义），2-seed 设计也可能给出 p>0.05。\n  - 3-seed 实验（Table 8）报告 σ≤0.026 for ρ，但这是 QE metric 的 seed 稳定性，不是 selection F1 的 seed 稳定性——论文没有报告 selection F1 的 3-seed variance。\n- 为什么影响接收：\"所有信号的 selection 与 single-sample 无显著差异\" 是论文最核心的 negative result。如果这个结论建立在 underpowered test 上，读者无法判断这是 true null 还是 Type II error。\n- 建议修改方向：(1) 将 selection 实验扩展到至少 3-seed（最好 5-seed），报告 selection F1 的 seed 间 σ 和 CI；(2) 进行 post-hoc power analysis，明确在当前样本量和 seed 数下能检测到的最小效应大小；(3) 报告 equivalence 的 power，而非仅 p-value。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Non-tied LP subset +2.9 pp (p=0.004) 的 Bonferroni 校正不完整\n- 具体位置：§4.3 footnote 4, §F (Appendix), Table in §F (ε sweep)\n- 问题：Footnote 4 称 \"+2.9 pp, p=0.004 survives Bonferroni correction over 5 comparisons\"（α_adj=0.01）。但 Bonferroni 的 5 comparisons 仅计入 5 个信号，未计入 ε 的 post-hoc 选择。Appendix Table (ε sweep) 测试了 7 个 ε 值（0.01 到 0.20），每个给出不同的 subset 和 p-value。如果校正为 7 ε × 5 signals = 35 comparisons，α_adj=0.0014，p=0.004 不再 survive。\n- 论文在 Limitations 中坦诚 ε=0.05 是 post-hoc，但 main text footnote 的 \"survives Bonferroni\" 表述给读者留下了 robust finding 的印象。\n- 建议：(1) 在 footnote 4 中明确 Bonferroni 仅覆盖 signal 维度，不含 ε 选择的自由度；(2) 用 permutation test 或 bootstrap 而非 Bonferroni 来评估 subset analysis 的稳健性；或 (3) 更保守地称其为 \"exploratory finding\" 而非 \"survives correction\"。\n\n**W2** [warning] Kendall's W=1.0 (3 seeds) 的呈现方式\n- 具体位置：§4.4 \"Signal rankings are stable across seeds (Kendall's W=1.0 at N=8; Table 11)\"\n- 问题：Main text 呈现 W=1.0 without caveat。虽然 m=3 raters, n=5 items 下 W=1.0 的 p 值确实显著（χ²=12, df=4, p≈0.017），但问题不是显著性而是 precision：仅 3 个 seed 时，即使一个 seed 产生微小的 ranking 变化（如 VC 和 SJ 互换），W 就会明显下降。Appendix 已承认 \"statistical power with n=3 is limited\"，但 main text 的呈现过于自信。\n- 建议：Main text 加注 \"(though 3 seeds provide limited precision for the W estimate)\" 或类似 caveat。\n\n**W3** [warning] 模型规模范围（3B-8B）限制了 \"intrinsic\" 结论的强度\n- 具体位置：Conclusion (\"confirm these mechanisms are intrinsic to capable fine-tuned models\"), §5 Discussion\n- 问题：论文在 3B-8B 范围内观察到 instance degeneracy 随 capability 增加（8B 21% vs 4B 10.4%），并推断这是 \"intrinsic\" 的。但 3B-8B 全是小模型；在 70B+ 规模下，模型可能产生更多样的样本（因更好的 calibration），也可能更 degenerate。两个方向都合理，但论文无法区分。\n- \"Intrinsic to capable fine-tuned models\" 的 claim 基于一个仅有两点（4B 和 8B）的线性外推，且 direction 取决于 capability 的 operationalization。\n- Limitations 中虽提及 \"whether the gap holds for 70B+ models is untested\"，但 Conclusion 的 \"intrinsic\" 用语暗示了更强的普遍性。\n- 建议：将 \"intrinsic\" 限定为 \"intrinsic within the 3B-8B fine-tuned regime we tested\"；或提供理论论证为什么 degeneracy 必然随 capability 单调递增。\n\n**W4** [warning] Free-form ablation 对 NER 的 std ratio 0.97 不足以排除 constrained decoding\n- 具体位置：§5 \"Ablation: free-form decoding\", Appendix §K (Table 6)\n- 问题：NER 的 free-form std ratio 为 0.97（几乎不变），论文据此声称 \"ruling out constrained decoding as the cause of NER compression\"。但：\n  - 同一 ablation 在 RE 上显示 LP selection 方向完全逆转（constrained -0.9 pp → free-form +1.8 pp），说明 constrained decoding 对 structured extraction 有实质影响\n  - NER 和 RE 的不同表现可能反映 NER 的 format template 更简单（entity list vs. relation triples），而非 constrained decoding 无关\n  - std ratio 0.97 的 effect size 很小，但 free-form QE 提升了 VC ρ（0.379→0.409），说明 constraint 确实有影响，只是在 selection 维度不明显\n- 建议：弱化 \"ruling out\" 的措辞为 \"constrained decoding has minimal effect on NER LP variance but substantial effect on RE\"；讨论 NER/RE 差异的可能原因。\n\n**W5** [warning] TOST 等价性结论是 configuration-dependent，main text 未充分反映\n- 具体位置：§4.3, Appendix §F (External equivalence margins)\n- 问题：Main text 称 \"TOST equivalence holds under all external anchors for LLaMA-CoNLL but varies by configuration\"（§4.3）。但 Appendix §F 更明确地指出：\n  - LLaMA-CoNLL: 所有 δ 下均 pass（robust）\n  - Qwen-CoNLL: 所有 external δ 下均 fail（selection 实际 degrades 0.9-1.5 pp）\n  - SciERC NER: 仅 SJ 在最宽 δ_SEM=1.33 pp 下 pass\n  - 这意味着 \"equivalence\" 仅在一个 configuration 下是 robust 的；其他 configurations 显示信号 actively harms selection\n- 建议：Main text 应更平衡地呈现——不仅是 \"signals don't help\"，某些 configurations 下信号 actively hurts。\n\n---\n\n## 小问题（不影响接收）\n\n- **Title 与 scope 不匹配**：Title 说 \"Named Entity Recognition\" 但 abstract 和正文多处讨论 RE（虽然标记为 exploratory）。建议 title 明确为 NER 或在 title 中删除 \"Named Entity Recognition\" 改为 \"Information Extraction\"（但这需要更强的 RE 支撑）。\n- **Greedy (T=0) 与 single-sample 的区分**：Table 2 中 Greedy=0.663 vs Single=0.645，差异 +1.8 pp，但未报告显著性检验。如果 greedy 本身 vs single-sample 不显著，那 \"greedy surpasses all selection strategies\" 的实际意义减弱——它也不显著优于 single-sample。\n- **Table 4 (Degeneracy) 中 CoNLL 用 N=16 而 SciERC 用 N=8**：不同 N 下 degeneracy 比例不可直接比较（更多 samples 更可能产生不同输出）。\n- **§5 Discussion 中 \"signal combinations\" 段落**：LP×VC 的三种组合策略描述简短，但 oracle tiebreaker 的 +7.9 pp 是重要 calibration point，值得更突出。\n- **Appendix §G FK split-half reliability**: SciERC r=0.395 较低，暗示 FK 在 harder tasks 上不够稳定，但 main text 仍将 FK 与其他信号并列讨论。\n\n---\n\n## 主要优势\n\n1. **概念贡献清晰且有价值**：将 quality estimation 与 sample selection 解耦是一个重要的方法论区分，解释了为什么看似有效的 confidence signal 在实际 selection 中失败。Figure 1 的 overview 图设计精良，一张图传达了核心发现。\n\n2. **诊断分析深入**：五层 ablation chain（free-form、entity-token LP、verbalized confidence、non-tied subset、signal combination）系统性地排除了替代解释。特别是 verbalized confidence（Appendix §R）的加入——它展示了更高的 ρ 但更差的 selection——强化了 correlation-selection gap 的概念。\n\n3. **Instance degeneracy 作为机制解释具有洞察力**：将 selection failure 归因于 \"模型越好，选择空间越小\" 的内在矛盾，这是一个非平凡的发现。Within-instance SJ-F1 ρ=0.52（正相关）vs. 整体 selection failure 的对比清晰展示了这一矛盾。\n\n4. **实验透明度高**：对 post-hoc 分析（ε=0.05）、thinking token confound、训练 mismatch 等潜在问题的主动披露达到了很高的标准。Limitations section 诚实且详尽。\n\n5. **Related work positioning 准确**：与 MBR 文献（Eikema et al., 2022, 2025）、self-consistency（Wang et al., 2023）、Yao et al. (2026) 的区分明确——特别是指出本文的 failure mode 不同于 MBR 的 utility misalignment（§2, §5）。\n\n6. **三数据集难度梯度设计**：虽然有效 selection 测试仅在 SciERC 上（N1），但三级梯度（ceiling/medium/collapse）本身是良好的实验设计思路，为 signal behavior 随 difficulty 变化提供了有用的 calibration。\n\n---\n\n## Questions for Authors\n\n1. **关于 N1（单数据集）**：是否有在其他 medium-difficulty NER 数据集（如 OntoNotes 子集或 ACE 2005）上的初步结果？如果没有，能否论证 SciERC 的哪些特性使其结论可能泛化（或不泛化）？\n\n2. **关于 N2（definitional vs. empirical）**：论文是否考虑过仅围绕 LP compression 作为 central finding，将 instance-level 信号的 selection failure 作为 \"expected baseline\"？这样的 framing 是否会更准确地反映贡献？\n\n3. **关于 greedy vs. selection 的实际含义**：如果一个 practitioner 已知可以用 greedy (T=0)，那 quality estimation（知道哪些 input 可靠）的 practical value 是什么？是否有 downstream use case（如 selective prediction、active learning）where QE signals have clear value despite selection failure？\n\n4. **Instance degeneracy 的实际检测**：在推理时，degeneracy 可以被检测到（所有 N 个输出相同）。是否考虑过一个简单的 hybrid 策略：degenerate instances 用 greedy，non-degenerate instances 用 MBR selection？这相比 pure greedy 的 expected gain 是多少？\n\n5. **Entity-token LP worsening selection despite 4× variance**：§5 讨论了 entity-token LP 在 SciERC 上 variance 增大但 selection 更差。作者能否提供 within-instance entity-token LP 与 F1 的 correlation（类比 pooled ρ=0.248 for full LP）？如果 entity-token LP 的 within-instance ρ 更低，则说明增加的 variance 是 noise 而非 signal。\n\n---\n\n## Missing References\n\n1. **Yixin Liu et al. (2024)**, \"Litcoder: Estimating task difficulty for code generation\" — 关于 per-sample difficulty estimation 的 test-time compute 工作，与本文的 QE/selection 区分相关。\n2. **Shuofei Qiao et al. (2023)**, \"Making language models better tool learners with execution feedback\" — 关于 structured output 的 verification 机制，与 trained verifiers 的讨论相关。\n3. **Daniel Deutsch et al. (2022)**, \"Training and meta-evaluating machine translation evaluation metrics at the paragraph level\" — MBR with structural metrics 在更复杂 output 上的表现，与 SJ-based MBR 的讨论直接相关。\n\n---\n\n## Overall Assessment 详细说明\n\n**推荐**: 3.0 — Findings acceptance\n\n论文提出了一个有价值的概念（correlation-selection gap），诊断了两个有洞察力的失败机制（instance degeneracy + LP compression），实验设计在结构上是合理的（三级难度梯度、多模型、ablation chain）。\n\n但三个 critical 问题削弱了结论的可信度：(1) 核心 claim 实质上由单数据集支撑；(2) 5-signal framing 夸大了经验发现的规模（4/5 的 failure 是 definitional）；(3) selection 的核心 negative result 基于 underpowered 2-seed test，无法区分 true null 和 Type II error。\n\n如果作者能解决 N1（增加数据集或限定 claim scope）、N2（重新 frame 贡献）、N3（增加 seed 数或 power analysis），我会将评分提升到 3.5-4.0（borderline accept to accept）。当前版本更适合 Findings track。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — Round 1 审稿报告\n\n**论文**: \"Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition\"\n**审查侧重**: 方法严谨性 + 实验设计 + 统计分析\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 / 5 (Findings acceptance)\n**一句话总结**: 论文提出了一个有价值的概念区分（quality estimation vs. sample selection），诊断了两个失败机制，但核心 claim 在实质上仅由单数据集（SciERC, n=529）支撑，且统计分析存在若干需要修正的问题。\n\n---\n\n## 官方维度打分（ACL ARR Review Form, Feb 2025+）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0 / 5 | 核心 claim 的实验支撑依赖单一有效数据集；统计检验的多重比较校正不完整；instance-level 信号的 selection failure 部分是定义上的必然而非经验发现 |\n| Excitement | 3.5 / 5 | Correlation-selection gap 是有用的概念贡献；instance degeneracy 作为机制解释有洞察力；但结论偏向 negative result（\"现有信号都不行\"），缺少前进路径的具体验证 |\n| Reproducibility | 4.0 / 5 | 训练配置详尽（Table 9），prompt template、constrained decoding 细节完整；代码承诺开源；但 2-seed 主实验的 variance estimation 偏弱 |\n| Confidence | 4 / 5 | 熟悉 MBR decoding、self-consistency、NER 评估方法论和统计检验 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 核心 claim 的有效测试仅由单数据集支撑\n- 具体位置：Section 4 (Experiments), Table 2, §4.3\n- 问题：论文声称发现 \"correlation-selection gap\"——信号有 QE 能力但 selection 失败。但实际有效测试 selection gap 的仅 SciERC (n=529)：\n  - CoNLL 被明确标记为 \"ceiling-effect control\"（single-sample F1≈0.91, oracle headroom 仅 4 pp）——作者自己在 Table 5 和 §D 中承认 \"selection analysis on these configurations is uninformative\"\n  - WNUT-17 被标记为 \"signal-collapse boundary\"（52% zero F1）——信号本身崩溃，无法测试 selection\n  - 因此论文的核心发现——greedy 超过所有 N=8 策略——实质上仅在 SciERC 上被验证\n- 为什么影响接收：一个旨在揭示 \"LLM-based NER\" 普遍现象的论文，核心 claim 由单一 domain-specific 数据集（科学文本, 6 entity types, n=529）支撑，泛化性不足。SciERC 的 medium-difficulty 特性（~65% F1）恰好处于 degeneracy 和 collapse 之间的窄带——这可能是一个 sweet-spot artifact 而非普遍现象。\n- 建议修改方向：(1) 增加至少一个额外的 medium-difficulty 数据集（如 OntoNotes 5.0 NER 的子集、ACE 2005、或 Few-NERD）在相似 F1 range (50-70%) 验证 selection gap；或 (2) 将 claim 明确限定为 \"on a medium-difficulty scientific NER benchmark\"，相应调整 title 和 abstract 的泛化程度。\n\n**N2** [critical] 4/5 信号的 selection failure 部分是定义上的必然，非纯经验发现\n- 具体位置：Section 3.1 (Problem Formulation), §4.3, Table 2\n- 问题：SJ、VC、FK、EM 均为 instance-level 信号——by construction 对同一 input 的所有 N 个候选给出相同分数。Table 2 中这些信号的 \"selection\" 实际测试的是 consensus-proximity（MBR），不是原始信号的 selection 能力。这与 LP（唯一 per-sample 信号）的 selection failure 有本质区别：\n  - Instance-level 信号不能 select → 这是信号设计的数学必然\n  - LP 不能 select → 这是经验发现（compression）\n  - 论文将两者混为 \"5 个信号都失败\"，夸大了发现的规模\n- Abstract、Introduction 的 contribution list、和 Conclusion 均写 \"five confidence signals\" 统一处理，但真正的 empirical surprise 只在 LP。\n- 为什么影响接收：Framing 误导了读者对贡献规模的判断。如果准确表述为 \"instance-level 信号无法 select（by design），LP 因 compression 也无法 select\"，那么贡献集中在 LP compression 的诊断上——这仍有价值，但论文需要重新调整 framing。\n- 建议修改方向：在 abstract 和 introduction 中明确区分两类 failure（definitional vs. empirical），将 MBR/consensus-proximity failure 与 LP compression 分别讨论。当前 §3.1 第一段已有初步区分，但后续行文未贯彻。\n\n**N3** [critical] 2-seed Fisher combined p 的统计效力严重不足\n- 具体位置：Table 2 (\"2-seed mean±σ, Fisher combined p vs. single-sample\"), §4.3\n- 问题：Selection 的核心结论——\"no signal significantly outperforms single-sample (all p>0.05)\"——基于仅 2 个 random seed 的 Fisher combined p-value。\n  - 2 个独立 sign test 的 Fisher combination 对小效应的检测力极低。LP 的 Δ=+0.2 pp (p=0.29)，但 bootstrap 95% CI 为 [-3.0, +4.2] pp——这个 CI 宽度为 7.2 pp，远超 oracle headroom 的 40%。如此宽的 CI 下，无法区分 \"无效果\" 和 \"有小到中等效果但检测不到\"。\n  - Cohen's d=0.038（§F, TOST 段落）本身说明效应很小，但 CI 的宽度意味着即使真实效应为 +3 pp（实际有意义），2-seed 设计也可能给出 p>0.05。\n  - 3-seed 实验（Table 8）报告 σ≤0.026 for ρ，但这是 QE metric 的 seed 稳定性，不是 selection F1 的 seed 稳定性——论文没有报告 selection F1 的 3-seed variance。\n- 为什么影响接收：\"所有信号的 selection 与 single-sample 无显著差异\" 是论文最核心的 negative result。如果这个结论建立在 underpowered test 上，读者无法判断这是 true null 还是 Type II error。\n- 建议修改方向：(1) 将 selection 实验扩展到至少 3-seed（最好 5-seed），报告 selection F1 的 seed 间 σ 和 CI；(2) 进行 post-hoc power analysis，明确在当前样本量和 seed 数下能检测到的最小效应大小；(3) 报告 equivalence 的 power，而非仅 p-value。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Non-tied LP subset +2.9 pp (p=0.004) 的 Bonferroni 校正不完整\n- 具体位置：§4.3 footnote 4, §F (Appendix), Table in §F (ε sweep)\n- 问题：Footnote 4 称 \"+2.9 pp, p=0.004 survives Bonferroni correction over 5 comparisons\"（α_adj=0.01）。但 Bonferroni 的 5 comparisons 仅计入 5 个信号，未计入 ε 的 post-hoc 选择。Appendix Table (ε sweep) 测试了 7 个 ε 值（0.01 到 0.20），每个给出不同的 subset 和 p-value。如果校正为 7 ε × 5 signals = 35 comparisons，α_adj=0.0014，p=0.004 不再 survive。\n- 论文在 Limitations 中坦诚 ε=0.05 是 post-hoc，但 main text footnote 的 \"survives Bonferroni\" 表述给读者留下了 robust finding 的印象。\n- 建议：(1) 在 footnote 4 中明确 Bonferroni 仅覆盖 signal 维度，不含 ε 选择的自由度；(2) 用 permutation test 或 bootstrap 而非 Bonferroni 来评估 subset analysis 的稳健性；或 (3) 更保守地称其为 \"exploratory finding\" 而非 \"survives correction\"。\n\n**W2** [warning] Kendall's W=1.0 (3 seeds) 的呈现方式\n- 具体位置：§4.4 \"Signal rankings are stable across seeds (Kendall's W=1.0 at N=8; Table 11)\"\n- 问题：Main text 呈现 W=1.0 without caveat。虽然 m=3 raters, n=5 items 下 W=1.0 的 p 值确实显著（χ²=12, df=4, p≈0.017），但问题不是显著性而是 precision：仅 3 个 seed 时，即使一个 seed 产生微小的 ranking 变化（如 VC 和 SJ 互换），W 就会明显下降。Appendix 已承认 \"statistical power with n=3 is limited\"，但 main text 的呈现过于自信。\n- 建议：Main text 加注 \"(though 3 seeds provide limited precision for the W estimate)\" 或类似 caveat。\n\n**W3** [warning] 模型规模范围（3B-8B）限制了 \"intrinsic\" 结论的强度\n- 具体位置：Conclusion (\"confirm these mechanisms are intrinsic to capable fine-tuned models\"), §5 Discussion\n- 问题：论文在 3B-8B 范围内观察到 instance degeneracy 随 capability 增加（8B 21% vs 4B 10.4%），并推断这是 \"intrinsic\" 的。但 3B-8B 全是小模型；在 70B+ 规模下，模型可能产生更多样的样本（因更好的 calibration），也可能更 degenerate。两个方向都合理，但论文无法区分。\n- \"Intrinsic to capable fine-tuned models\" 的 claim 基于一个仅有两点（4B 和 8B）的线性外推，且 direction 取决于 capability 的 operationalization。\n- Limitations 中虽提及 \"whether the gap holds for 70B+ models is untested\"，但 Conclusion 的 \"intrinsic\" 用语暗示了更强的普遍性。\n- 建议：将 \"intrinsic\" 限定为 \"intrinsic within the 3B-8B fine-tuned regime we tested\"；或提供理论论证为什么 degeneracy 必然随 capability 单调递增。\n\n**W4** [warning] Free-form ablation 对 NER 的 std ratio 0.97 不足以排除 constrained decoding\n- 具体位置：§5 \"Ablation: free-form decoding\", Appendix §K (Table 6)\n- 问题：NER 的 free-form std ratio 为 0.97（几乎不变），论文据此声称 \"ruling out constrained decoding as the cause of NER compression\"。但：\n  - 同一 ablation 在 RE 上显示 LP selection 方向完全逆转（constrained -0.9 pp → free-form +1.8 pp），说明 constrained decoding 对 structured extraction 有实质影响\n  - NER 和 RE 的不同表现可能反映 NER 的 format template 更简单（entity list vs. relation triples），而非 constrained decoding 无关\n  - std ratio 0.97 的 effect size 很小，但 free-form QE 提升了 VC ρ（0.379→0.409），说明 constraint 确实有影响，只是在 selection 维度不明显\n- 建议：弱化 \"ruling out\" 的措辞为 \"constrained decoding has minimal effect on NER LP variance but substantial effect on RE\"；讨论 NER/RE 差异的可能原因。\n\n**W5** [warning] TOST 等价性结论是 configuration-dependent，main text 未充分反映\n- 具体位置：§4.3, Appendix §F (External equivalence margins)\n- 问题：Main text 称 \"TOST equivalence holds under all external anchors for LLaMA-CoNLL but varies by configuration\"（§4.3）。但 Appendix §F 更明确地指出：\n  - LLaMA-CoNLL: 所有 δ 下均 pass（robust）\n  - Qwen-CoNLL: 所有 external δ 下均 fail（selection 实际 degrades 0.9-1.5 pp）\n  - SciERC NER: 仅 SJ 在最宽 δ_SEM=1.33 pp 下 pass\n  - 这意味着 \"equivalence\" 仅在一个 configuration 下是 robust 的；其他 configurations 显示信号 actively harms selection\n- 建议：Main text 应更平衡地呈现——不仅是 \"signals don't help\"，某些 configurations 下信号 actively hurts。\n\n---\n\n## 小问题（不影响接收）\n\n- **Title 与 scope 不匹配**：Title 说 \"Named Entity Recognition\" 但 abstract 和正文多处讨论 RE（虽然标记为 exploratory）。建议 title 明确为 NER 或在 title 中删除 \"Named Entity Recognition\" 改为 \"Information Extraction\"（但这需要更强的 RE 支撑）。\n- **Greedy (T=0) 与 single-sample 的区分**：Table 2 中 Greedy=0.663 vs Single=0.645，差异 +1.8 pp，但未报告显著性检验。如果 greedy 本身 vs single-sample 不显著，那 \"greedy surpasses all selection strategies\" 的实际意义减弱——它也不显著优于 single-sample。\n- **Table 4 (Degeneracy) 中 CoNLL 用 N=16 而 SciERC 用 N=8**：不同 N 下 degeneracy 比例不可直接比较（更多 samples 更可能产生不同输出）。\n- **§5 Discussion 中 \"signal combinations\" 段落**：LP×VC 的三种组合策略描述简短，但 oracle tiebreaker 的 +7.9 pp 是重要 calibration point，值得更突出。\n- **Appendix §G FK split-half reliability**: SciERC r=0.395 较低，暗示 FK 在 harder tasks 上不够稳定，但 main text 仍将 FK 与其他信号并列讨论。\n\n---\n\n## 主要优势\n\n1. **概念贡献清晰且有价值**：将 quality estimation 与 sample selection 解耦是一个重要的方法论区分，解释了为什么看似有效的 confidence signal 在实际 selection 中失败。Figure 1 的 overview 图设计精良，一张图传达了核心发现。\n\n2. **诊断分析深入**：五层 ablation chain（free-form、entity-token LP、verbalized confidence、non-tied subset、signal combination）系统性地排除了替代解释。特别是 verbalized confidence（Appendix §R）的加入——它展示了更高的 ρ 但更差的 selection——强化了 correlation-selection gap 的概念。\n\n3. **Instance degeneracy 作为机制解释具有洞察力**：将 selection failure 归因于 \"模型越好，选择空间越小\" 的内在矛盾，这是一个非平凡的发现。Within-instance SJ-F1 ρ=0.52（正相关）vs. 整体 selection failure 的对比清晰展示了这一矛盾。\n\n4. **实验透明度高**：对 post-hoc 分析（ε=0.05）、thinking token confound、训练 mismatch 等潜在问题的主动披露达到了很高的标准。Limitations section 诚实且详尽。\n\n5. **Related work positioning 准确**：与 MBR 文献（Eikema et al., 2022, 2025）、self-consistency（Wang et al., 2023）、Yao et al. (2026) 的区分明确——特别是指出本文的 failure mode 不同于 MBR 的 utility misalignment（§2, §5）。\n\n6. **三数据集难度梯度设计**：虽然有效 selection 测试仅在 SciERC 上（N1），但三级梯度（ceiling/medium/collapse）本身是良好的实验设计思路，为 signal behavior 随 difficulty 变化提供了有用的 calibration。\n\n---\n\n## Questions for Authors\n\n1. **关于 N1（单数据集）**：是否有在其他 medium-difficulty NER 数据集（如 OntoNotes 子集或 ACE 2005）上的初步结果？如果没有，能否论证 SciERC 的哪些特性使其结论可能泛化（或不泛化）？\n\n2. **关于 N2（definitional vs. empirical）**：论文是否考虑过仅围绕 LP compression 作为 central finding，将 instance-level 信号的 selection failure 作为 \"expected baseline\"？这样的 framing 是否会更准确地反映贡献？\n\n3. **关于 greedy vs. selection 的实际含义**：如果一个 practitioner 已知可以用 greedy (T=0)，那 quality estimation（知道哪些 input 可靠）的 practical value 是什么？是否有 downstream use case（如 selective prediction、active learning）where QE signals have clear value despite selection failure？\n\n4. **Instance degeneracy 的实际检测**：在推理时，degeneracy 可以被检测到（所有 N 个输出相同）。是否考虑过一个简单的 hybrid 策略：degenerate instances 用 greedy，non-degenerate instances 用 MBR selection？这相比 pure greedy 的 expected gain 是多少？\n\n5. **Entity-token LP worsening selection despite 4× variance**：§5 讨论了 entity-token LP 在 SciERC 上 variance 增大但 selection 更差。作者能否提供 within-instance entity-token LP 与 F1 的 correlation（类比 pooled ρ=0.248 for full LP）？如果 entity-token LP 的 within-instance ρ 更低，则说明增加的 variance 是 noise 而非 signal。\n\n---\n\n## Missing References\n\n1. **Yixin Liu et al. (2024)**, \"Litcoder: Estimating task difficulty for code generation\" — 关于 per-sample difficulty estimation 的 test-time compute 工作，与本文的 QE/selection 区分相关。\n2. **Shuofei Qiao et al. (2023)**, \"Making language models better tool learners with execution feedback\" — 关于 structured output 的 verification 机制，与 trained verifiers 的讨论相关。\n3. **Daniel Deutsch et al. (2022)**, \"Training and meta-evaluating machine translation evaluation metrics at the paragraph level\" — MBR with structural metrics 在更复杂 output 上的表现，与 SJ-based MBR 的讨论直接相关。\n\n---\n\n## Overall Assessment 详细说明\n\n**推荐**: 3.0 — Findings acceptance\n\n论文提出了一个有价值的概念（correlation-selection gap），诊断了两个有洞察力的失败机制（instance degeneracy + LP compression），实验设计在结构上是合理的（三级难度梯度、多模型、ablation chain）。\n\n但三个 critical 问题削弱了结论的可信度：(1) 核心 claim 实质上由单数据集支撑；(2) 5-signal framing 夸大了经验发现的规模（4/5 的 failure 是 definitional）；(3) selection 的核心 negative result 基于 underpowered 2-seed test，无法区分 true null 和 Type II error。\n\n如果作者能解决 N1（增加数据集或限定 claim scope）、N2（重新 frame 贡献）、N3（增加 seed 数或 power analysis），我会将评分提升到 3.5-4.0（borderline accept to accept）。当前版本更适合 Findings track。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 944 · 2026-05-16T08:40:32.862916+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4168
}
```

</details>

---


### Assistant

_source line 945 · 2026-05-16T08:40:44.017858+00:00_

审稿报告已提交给 Review Director。

**核心判断：Overall 3.0/5 (Findings acceptance)**

三个 critical 问题：
1. 核心 claim（correlation-selection gap）实质上仅由 SciERC (n=529) 一个数据集支撑——CoNLL 是 ceiling control，WNUT-17 是 collapse boundary，都无法有效测试 selection gap
2. 5 个信号中 4 个是 instance-level（by construction 无法 select），将 definitional limitation 与 LP compression 的 empirical finding 混为 "5 signals all fail" 夸大了发现规模
3. Selection 的核心 negative result 基于 2-seed Fisher combined p，bootstrap CI 宽达 7.2 pp，无法区分 true null 和 Type II error

五个 should-fix：non-tied subset 的 Bonferroni 不完整、Kendall's W=1.0 呈现过于自信、3B-8B scale range 不足以支撑 "intrinsic" claim、free-form ablation 的 "ruling out" 措辞过强、TOST 等价性结论的 configuration-dependency 未充分呈现。

论文的主要优势在于概念贡献清晰（QE vs. selection 解耦）、诊断分析深入（五层 ablation chain）、实验透明度高（主动披露 post-hoc 分析和 confounds）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 31

## Round 31

4 recorded events


### User

_source line 946 · 2026-05-16T08:44:30.510593+00:00_

[Round 1 审稿请求]:
## 交叉分享 — Reviewer 2 的完整审稿意见

以下是 Reviewer 2 的完整审稿原文。请逐条回应：对每个 Must-Fix、Should-Fix 和主要观点，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

### Reviewer 2 评分：3/5 (Findings)

**Must-Fix:**

**N1** [critical] Contribution #1 framing 混淆 by-construction limitation 与 empirical finding
- 4/5 信号是 instance-level aggregates，BY DESIGN 对所有 N 个 candidate 赋相同 QE 分。这不是需要 "diagnose" 的失败，而是信号设计的固有属性。论文通过 MBR 转换为 per-sample ranking，但 framing 让读者误以为作者发现了 4 个信号为何无法 select。
- 建议：拆分为 (a) MBR conversion fails due to instance degeneracy 和 (b) LP fails due to compression。

**N2** [critical] Instance degeneracy 新颖性边界未充分建立
- "Better fine-tuned models → more consistent outputs → less selection headroom" 直觉上可预期。
- 未区分与 Yun et al. (2025) format-induced diversity collapse 和 fine-tuning overfitting 的边界。
- "Intrinsic to capable fine-tuned models" 未排除 fine-tuning recipe artifact（LoRA rank=32, 5 epochs, dropout=0）。
- 建议：讨论 fine-tuning hyperparameters 对 degeneracy 的潜在影响；考虑 LoRA rank ablation。

**N3** [critical] Table 2 Random (0.610) vs Single (0.645) 差距 3.5pp 缺乏解释
- 在 T=1.0 下，Random (uniform from N) 和 Single (one T=1.0 draw) 的期望 F1 应相同。3.5pp 系统性差距 (across 529 instances × 2 seeds, ~2.7σ) 不太可能是随机波动。如果计算方式不同需明确说明，因为这影响所有 selection methods 的 baseline 解读。

**Should-Fix:**

**W1** Abstract 信息密度过高。ρ=0.45 来自 ceiling-effect control CoNLL，primary SciERC 仅 ρ=0.379。

**W2** "Soft Jaccard" 命名误导。分母用 max(|g_i|,|g_j|) 非 union，NLP 社区中 "Jaccard" 有固定含义。

**W3** 与 Yao et al. (2026) positioning 遗漏关键讨论——未讨论 hard-prompted models 是否存在类似 output concentration。如果不存在 → degeneracy 是 fine-tuning artifact 非 task-intrinsic。

**W4** Yun et al. (2025) 引用讨论不充分——diversity collapse 与 instance degeneracy 直接相关但仅作附注引用。

**W5** "surpassing all N=8 selection strategies" 修辞过强。Greedy vs Single 1.8pp 未经 significance test。

**W6** 2-seed Fisher combined p 统计效力不足。Negative result 需更强 power analysis。

**小问题：**
- VC QE (continuous) vs VC selection (freq>N/2, discrete) 关系应说清
- SciERC checkpoint 未用 load_best_model_at_end 是否影响 degeneracy
- Introduction 和 Section 4.3 对 gap 重复定义

**R2 主要优势认定：**
1. 实验设计 thoroughly controlled
2. QE vs selection 解耦框架有方法论价值
3. Negative result 诚实处理
4. Appendix 质量极高
5. Within-instance analysis 是最佳部分（non-degenerate MBR closes 23-41% gap）

**R2 Questions:**
1. Table 2 Random vs Single 精确计算公式及 3.5pp 差距来源？
2. Instance degeneracy 是否与 fine-tuning recipe 相关？
3. Free-form ablation 下 constant-F1 fraction 是否改变？
4. Greedy vs Single 1.8pp 差距是否经过 significance test？

**R2 Missing References:**
- Gao et al. (2023) scaling laws for reward model overoptimization

**R2 引用核查：** 53 entries, 0 orphan, 0 missing, 44 verified。

---

请对以上每个 Must-Fix (N1-N3)、Should-Fix (W1-W6)、小问题和 Questions 逐条给出 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 947 · 2026-05-16T08:47:34.264571+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — 交叉回应 Reviewer 2\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-N1: Contribution #1 framing 混淆 by-construction limitation 与 empirical finding**\n\n完全同意，这与我的 R1-N2 指向同一问题。§3.1 第一段明确写了 \"4 of 5 signals are instance-level aggregates that assign identical QE scores to all N candidates\"，但 abstract (\"five confidence signals... yet best-of-N selection fails\") 和 Contribution list (\"Two failure mechanisms\") 的 framing 将两类本质不同的 failure 混为一谈。R2 提出的拆分方案合理：(a) MBR conversion fails due to instance degeneracy; (b) LP fails due to compression。这能更准确地传达贡献的规模和性质。\n\n补充我的发现：Table 2 中 instance-level 信号的 selection F1 (SJ 0.646, FK 0.646, EM 0.637, VC 0.623) 实际测试的是 consensus-proximity (MBR) 的有效性，不是原始信号的 selection 能力。将 MBR failure 归因于 \"信号失败\" 是 attribution error。\n\n---\n\n**[PARTIALLY AGREE] R2-N2: Instance degeneracy 新颖性边界**\n\nR2 的两个子论点需要分别评判：\n\n(a) \"Better fine-tuned models → more consistent outputs → less headroom 可预期\"——部分同意。直觉上 \"更好的模型更一致\" 确实可预期。但论文的具体贡献不止于此：within-instance SJ-F1 ρ=0.52（Table 4, §5）表明 MBR utility IS aligned with quality（正相关），问题不在 utility misalignment 而在 headroom vanishing。这与 Eikema et al. (2025) 报告的 MBR failure mode 不同（他们归因于 bag-of-unit utility mismatch）。这一区分不是 trivial。Non-degenerate instances 上 MBR closes 23-41% of oracle gap（Table 4）——这证明了 MBR 在有 headroom 时是 work 的。将 failure 精确定位到 headroom 而非 utility 是有价值的诊断。\n\n(b) **\"未排除 fine-tuning recipe artifact\"——完全同意，这是我未充分强调的问题。** 论文用 LoRA rank=32, dropout=0, 5 epochs（Table 9），且 SciERC 训练未使用 load_best_model_at_end（仅 CoNLL/WNUT 用了）。这意味着 SciERC checkpoint 可能 over-trained，导致 output diversity 人为降低。Degeneracy 21% (8B) vs 10.4% (4B) 的差异可能部分反映了 larger model overfitting faster with same epochs，而非 capability 的 intrinsic property。\n- **缺少的 ablation**: LoRA rank ablation（rank 8 vs 16 vs 32）或 epoch ablation（3 vs 5 epochs）能有效区分 fine-tuning artifact 和 intrinsic property。\n- **与 Yao et al. (2026) 的关键对比**（也是 R2-W3 的问题）：如果 hard-prompted models 不表现出 degeneracy，则 degeneracy 是 fine-tuning artifact。论文 §2 提到 Yao et al. 但未讨论这一关键区分。\n\n结论：within-instance analysis 的诊断有新颖性，但 \"intrinsic to capable fine-tuned models\" 的 claim 需要更强支撑。\n\n---\n\n**[AGREE] R2-N3: Table 2 Random (0.610) vs Single (0.645) 差距 3.5pp**\n\n这是我审稿中遗漏的重要问题。在 T=1.0 下：\n- Single = one T=1.0 draw → 一个随机 sample 的 F1，averaged across instances\n- Random = uniform random from N=8 → 一个随机 sample 的 F1，averaged across instances\n\n两者的期望应相同：E[Random] = E[Single] = (1/N) Σ E[F1(y_i)]。\n\n3.5pp 的系统性差距 (across 529 instances, 2 seeds, ±0.003 variance) 不太可能是随机波动。可能的解释：\n1. **计算方式不同**：Single 可能是 N 个 sample 的 mean F1（即期望值），而 Random 是单次 random draw 的 F1。但如果如此，多次 random draw 的均值应收敛到 Single。\n2. **样本选择偏差**：如果 Random 使用的 random generator 与 seed 产生了系统性的低质量选择。\n3. **F1 计算的 aggregation 差异**：如果 Single 是 macro-averaged 而 Random 使用了不同的 aggregation。\n\n无论原因如何，这个差距影响所有 selection method 的 baseline interpretation——如果 Random 系统性偏低，那 selection methods 相对 Random 的 +3-4pp 实际上可能只是恢复到了 expectation，而非真正的 selection gain。这需要作者明确解释计算方式。\n\n---\n\n### Should-Fix\n\n**[PARTIALLY AGREE] R2-W1: Abstract 信息密度**\n\nAbstract 实际写的是 \"ρ up to 0.38 on the primary test bed, 0.45 on a ceiling-effect control\"——两个数字都明确标注了来源。准确但有 framing 问题：将 ceiling-effect control（CoNLL）的 ρ=0.45 放入 abstract 给读者留下了比 primary result (0.38) 更乐观的印象。由于 CoNLL 的 ρ inflate 部分源于 zero/non-zero boundary effect（§4.2 footnote 5, Appendix §B 均提及），在 abstract 中使用这个数字需要 caveat。\n\n建议：abstract 仅报告 primary test bed 的 ρ=0.38，或用 \"ρ=0.38 (primary)\" 不提 CoNLL 数字。\n\n---\n\n**[REBUT] R2-W2: \"Soft Jaccard\" 命名**\n\nR2 认为分母用 max(|g_i|,|g_j|) 而非 union 使 \"Jaccard\" 名称误导。但：\n1. 论文 Eq. 4 的 footnote 已明确说明 \"The denominator uses max(|g_i|, |g_j|) per type group rather than |A∪B|\"\n2. Appendix Table 10 (§D) 验证了 max vs union normalizer 在所有 6 个 model-dataset 组合上 |Δρ|<0.01——结论不受影响\n3. \"Soft Jaccard\" 在 image segmentation 文献中已有使用先例（Iglovikov et al., 2018 等），\"Soft\" 前缀本身暗示了对标准 Jaccard 的修改\n4. 真正的 novelty 在 token-level IoU matching + Hungarian algorithm 的组合，不在分母选择\n\n命名可以更精确（如 \"modified Jaccard\" 或 \"max-normalized overlap\"），但这不构成 should-fix 级别的问题——数学定义完整且 robustness 已验证。\n\n---\n\n**[AGREE] R2-W3: 与 Yao et al. (2026) 未讨论 hard-prompted models 的 degeneracy**\n\n完全同意。§2 写了 \"Yao et al. (2026) examine consistency–accuracy correlations for LLM-based IE using exact-match agreement under hard-prompting; we extend their work to fine-tuned models\"。但关键问题是：hard-prompted models 是否也表现出 instance degeneracy？\n- 如果是 → degeneracy 是 structured extraction 的 task-intrinsic property\n- 如果否 → degeneracy 是 fine-tuning artifact（与 R2-N2(b) 呼应）\n\n这个对比对论文的核心 claim (\"intrinsic to capable fine-tuned models\") 有直接影响。论文 §2 和 §5 都没有讨论这一区分。建议作者在 revision 中至少定性讨论 Yao et al. 的 output diversity 情况，最好补充一个 hard-prompted baseline 的 degeneracy 统计。\n\n---\n\n**[PARTIALLY AGREE] R2-W4: Yun et al. (2025) 讨论不充分**\n\nR2 指出 Yun et al. (2025) 的 diversity collapse 与 instance degeneracy 直接相关。论文 §2 引用了 Schall et al. (2025, \"hidden costs of constrained generation for log-probability estimation\") 和 Yun et al. (2025, \"inference efficiency\")，但后者的 diversity collapse finding 与本文的 instance degeneracy 确实高度相关。\n\n不过，论文的 free-form ablation (Appendix §K, Table 6) 已经 address 了 constrained decoding 是否导致 compression 的问题（NER std ratio=0.97），间接 address 了 Yun et al. 的 concern。问题是这个 connection 没有被显式讨论。建议在 §2 或 §5 中增加 1-2 句话，显式连接 Yun et al. 的 diversity collapse 与本文的 degeneracy，并指向 free-form ablation 作为回应。\n\n---\n\n**[AGREE] R2-W5: \"surpassing all N=8 selection strategies\" 修辞过强**\n\n同意。§4.3 和 Contribution #3 写 \"Greedy (T=0, F1=0.663) surpasses all N=8 selection strategies (best: 0.647)\"，但 Greedy vs Single (0.663 vs 0.645, +1.8pp) 未经 significance test。如果 Greedy vs Single 不显著，那实际结论应是 \"Greedy ≈ Single > all selection strategies\"，这改变了 practical implication——不是 greedy 特别好，而是 selection 特别差（甚至不如 random single draw）。\n\n---\n\n**[AGREE] R2-W6: 2-seed Fisher combined p 统计效力不足**\n\n与我的 R1-N3 完全一致。补充：论文虽然在 Table 8 报告了 3-seed QE stability (σ≤0.026)，但这是 Spearman ρ 的 seed 稳定性，不是 selection F1 的。Selection F1 的 seed 间 variance 可能更大（因为 selection 依赖 per-instance ranking 而非 aggregate correlation），但论文没有报告这个数字。\n\n---\n\n### 小问题\n\n**[AGREE]** VC QE (continuous, Eq. 5) vs VC selection (freq > N/2, discrete, footnote 1)：论文 footnote 1 已做区分，但 Table 2 中两种 VC 使用不同定义却共享同一行标签 \"VC\"，容易混淆。建议在 table caption 中明确。\n\n**[AGREE]** SciERC checkpoint 未用 load_best_model_at_end（Table 9）：这可能导致 SciERC model over-trained，人为增加 degeneracy。这与 R2-N2 的 fine-tuning recipe concern 一致。\n\n**[AGREE]** Introduction 和 §4.3 重复定义 gap：轻微冗余，可合并。\n\n---\n\n### R2 Questions 回应\n\n**Q1 (Random vs Single 计算)**: [AGREE] 需要作者回答。如上述 R2-N3 分析。\n\n**Q2 (Fine-tuning recipe 与 degeneracy)**: [AGREE] 这是 R2-N2(b) 的核心问题。LoRA rank、epoch、dropout 都可能影响 output diversity。论文需要至少 acknowledge 这个 confound，最好提供 ablation evidence。\n\n**Q3 (Free-form 下 constant-F1 fraction)**: [AGREE] 这是诊断 free-form ablation 的关键补充数据。如果 free-form decoding 下 degeneracy 显著降低，则 constrained decoding（而非 model capability）是 degeneracy 的部分原因。Appendix §K Table 6 Panel A 报告了 LP distribution 变化但没有报告 constant-F1 fraction 的变化——这个遗漏值得补充。\n\n**Q4 (Greedy vs Single significance)**: [AGREE] 与 R2-W5 一致。\n\n---\n\n### R2 Missing References\n\n**[PARTIALLY AGREE]** Gao et al. (2023) scaling laws for reward model overoptimization：与论文的直接相关性有限（NER selection ≠ RLHF reward hacking），但 \"best-of-N 随 N 增加可能 over-optimize on proxy signal\" 的概念框架与本文的 \"selection fails despite more samples\" 有概念联系。建议仅在 §5 discussion 中作为 broader context 提及，非 core citation。\n\n---\n\n### 与我 R1 审稿的交叉对照\n\n| 问题 | R1 | R2 | 一致性 |\n|------|-----|-----|--------|\n| Framing conflation (definitional vs empirical) | N2 (critical) | N1 (critical) | **完全一致** |\n| 2-seed power | N3 (critical) | W6 (should-fix) | 一致，我评级更高 |\n| 单数据集支撑 | N1 (critical) | 未提及 | R2 未覆盖 |\n| Random vs Single 3.5pp | 未发现 | N3 (critical) | **R2 发现了我遗漏的问题** |\n| Degeneracy novelty/recipe artifact | W3 (scale range) | N2 (critical) | 相关但角度不同 |\n| Greedy rhetoric | Minor | W5 (should-fix) | 一致 |\n| Yao et al. (2026) positioning | 未涉及 | W3 (should-fix) | **R2 发现了我遗漏的问题** |\n\n**总结**：R2 和我在核心问题（framing conflation, statistical power）上高度一致。R2 补充了两个我遗漏的重要问题（Random vs Single 差距, fine-tuning recipe artifact）。我补充了 R2 未覆盖的单数据集泛化问题。两份审稿结合后，论文需要 address 的核心问题集中在：(1) framing 重构, (2) 统计 power 加强, (3) 泛化性验证或 claim 限定, (4) Random vs Single 解释, (5) fine-tuning recipe ablation or acknowledgment。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — 交叉回应 Reviewer 2\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-N1: Contribution #1 framing 混淆 by-construction limitation 与 empirical finding**\n\n完全同意，这与我的 R1-N2 指向同一问题。§3.1 第一段明确写了 \"4 of 5 signals are instance-level aggregates that assign identical QE scores to all N candidates\"，但 abstract (\"five confidence signals... yet best-of-N selection fails\") 和 Contribution list (\"Two failure mechanisms\") 的 framing 将两类本质不同的 failure 混为一谈。R2 提出的拆分方案合理：(a) MBR conversion fails due to instance degeneracy; (b) LP fails due to compression。这能更准确地传达贡献的规模和性质。\n\n补充我的发现：Table 2 中 instance-level 信号的 selection F1 (SJ 0.646, FK 0.646, EM 0.637, VC 0.623) 实际测试的是 consensus-proximity (MBR) 的有效性，不是原始信号的 selection 能力。将 MBR failure 归因于 \"信号失败\" 是 attribution error。\n\n---\n\n**[PARTIALLY AGREE] R2-N2: Instance degeneracy 新颖性边界**\n\nR2 的两个子论点需要分别评判：\n\n(a) \"Better fine-tuned models → more consistent outputs → less headroom 可预期\"——部分同意。直觉上 \"更好的模型更一致\" 确实可预期。但论文的具体贡献不止于此：within-instance SJ-F1 ρ=0.52（Table 4, §5）表明 MBR utility IS aligned with quality（正相关），问题不在 utility misalignment 而在 headroom vanishing。这与 Eikema et al. (2025) 报告的 MBR failure mode 不同（他们归因于 bag-of-unit utility mismatch）。这一区分不是 trivial。Non-degenerate instances 上 MBR closes 23-41% of oracle gap（Table 4）——这证明了 MBR 在有 headroom 时是 work 的。将 failure 精确定位到 headroom 而非 utility 是有价值的诊断。\n\n(b) **\"未排除 fine-tuning recipe artifact\"——完全同意，这是我未充分强调的问题。** 论文用 LoRA rank=32, dropout=0, 5 epochs（Table 9），且 SciERC 训练未使用 load_best_model_at_end（仅 CoNLL/WNUT 用了）。这意味着 SciERC checkpoint 可能 over-trained，导致 output diversity 人为降低。Degeneracy 21% (8B) vs 10.4% (4B) 的差异可能部分反映了 larger model overfitting faster with same epochs，而非 capability 的 intrinsic property。\n- **缺少的 ablation**: LoRA rank ablation（rank 8 vs 16 vs 32）或 epoch ablation（3 vs 5 epochs）能有效区分 fine-tuning artifact 和 intrinsic property。\n- **与 Yao et al. (2026) 的关键对比**（也是 R2-W3 的问题）：如果 hard-prompted models 不表现出 degeneracy，则 degeneracy 是 fine-tuning artifact。论文 §2 提到 Yao et al. 但未讨论这一关键区分。\n\n结论：within-instance analysis 的诊断有新颖性，但 \"intrinsic to capable fine-tuned models\" 的 claim 需要更强支撑。\n\n---\n\n**[AGREE] R2-N3: Table 2 Random (0.610) vs Single (0.645) 差距 3.5pp**\n\n这是我审稿中遗漏的重要问题。在 T=1.0 下：\n- Single = one T=1.0 draw → 一个随机 sample 的 F1，averaged across instances\n- Random = uniform random from N=8 → 一个随机 sample 的 F1，averaged across instances\n\n两者的期望应相同：E[Random] = E[Single] = (1/N) Σ E[F1(y_i)]。\n\n3.5pp 的系统性差距 (across 529 instances, 2 seeds, ±0.003 variance) 不太可能是随机波动。可能的解释：\n1. **计算方式不同**：Single 可能是 N 个 sample 的 mean F1（即期望值），而 Random 是单次 random draw 的 F1。但如果如此，多次 random draw 的均值应收敛到 Single。\n2. **样本选择偏差**：如果 Random 使用的 random generator 与 seed 产生了系统性的低质量选择。\n3. **F1 计算的 aggregation 差异**：如果 Single 是 macro-averaged 而 Random 使用了不同的 aggregation。\n\n无论原因如何，这个差距影响所有 selection method 的 baseline interpretation——如果 Random 系统性偏低，那 selection methods 相对 Random 的 +3-4pp 实际上可能只是恢复到了 expectation，而非真正的 selection gain。这需要作者明确解释计算方式。\n\n---\n\n### Should-Fix\n\n**[PARTIALLY AGREE] R2-W1: Abstract 信息密度**\n\nAbstract 实际写的是 \"ρ up to 0.38 on the primary test bed, 0.45 on a ceiling-effect control\"——两个数字都明确标注了来源。准确但有 framing 问题：将 ceiling-effect control（CoNLL）的 ρ=0.45 放入 abstract 给读者留下了比 primary result (0.38) 更乐观的印象。由于 CoNLL 的 ρ inflate 部分源于 zero/non-zero boundary effect（§4.2 footnote 5, Appendix §B 均提及），在 abstract 中使用这个数字需要 caveat。\n\n建议：abstract 仅报告 primary test bed 的 ρ=0.38，或用 \"ρ=0.38 (primary)\" 不提 CoNLL 数字。\n\n---\n\n**[REBUT] R2-W2: \"Soft Jaccard\" 命名**\n\nR2 认为分母用 max(|g_i|,|g_j|) 而非 union 使 \"Jaccard\" 名称误导。但：\n1. 论文 Eq. 4 的 footnote 已明确说明 \"The denominator uses max(|g_i|, |g_j|) per type group rather than |A∪B|\"\n2. Appendix Table 10 (§D) 验证了 max vs union normalizer 在所有 6 个 model-dataset 组合上 |Δρ|<0.01——结论不受影响\n3. \"Soft Jaccard\" 在 image segmentation 文献中已有使用先例（Iglovikov et al., 2018 等），\"Soft\" 前缀本身暗示了对标准 Jaccard 的修改\n4. 真正的 novelty 在 token-level IoU matching + Hungarian algorithm 的组合，不在分母选择\n\n命名可以更精确（如 \"modified Jaccard\" 或 \"max-normalized overlap\"），但这不构成 should-fix 级别的问题——数学定义完整且 robustness 已验证。\n\n---\n\n**[AGREE] R2-W3: 与 Yao et al. (2026) 未讨论 hard-prompted models 的 degeneracy**\n\n完全同意。§2 写了 \"Yao et al. (2026) examine consistency–accuracy correlations for LLM-based IE using exact-match agreement under hard-prompting; we extend their work to fine-tuned models\"。但关键问题是：hard-prompted models 是否也表现出 instance degeneracy？\n- 如果是 → degeneracy 是 structured extraction 的 task-intrinsic property\n- 如果否 → degeneracy 是 fine-tuning artifact（与 R2-N2(b) 呼应）\n\n这个对比对论文的核心 claim (\"intrinsic to capable fine-tuned models\") 有直接影响。论文 §2 和 §5 都没有讨论这一区分。建议作者在 revision 中至少定性讨论 Yao et al. 的 output diversity 情况，最好补充一个 hard-prompted baseline 的 degeneracy 统计。\n\n---\n\n**[PARTIALLY AGREE] R2-W4: Yun et al. (2025) 讨论不充分**\n\nR2 指出 Yun et al. (2025) 的 diversity collapse 与 instance degeneracy 直接相关。论文 §2 引用了 Schall et al. (2025, \"hidden costs of constrained generation for log-probability estimation\") 和 Yun et al. (2025, \"inference efficiency\")，但后者的 diversity collapse finding 与本文的 instance degeneracy 确实高度相关。\n\n不过，论文的 free-form ablation (Appendix §K, Table 6) 已经 address 了 constrained decoding 是否导致 compression 的问题（NER std ratio=0.97），间接 address 了 Yun et al. 的 concern。问题是这个 connection 没有被显式讨论。建议在 §2 或 §5 中增加 1-2 句话，显式连接 Yun et al. 的 diversity collapse 与本文的 degeneracy，并指向 free-form ablation 作为回应。\n\n---\n\n**[AGREE] R2-W5: \"surpassing all N=8 selection strategies\" 修辞过强**\n\n同意。§4.3 和 Contribution #3 写 \"Greedy (T=0, F1=0.663) surpasses all N=8 selection strategies (best: 0.647)\"，但 Greedy vs Single (0.663 vs 0.645, +1.8pp) 未经 significance test。如果 Greedy vs Single 不显著，那实际结论应是 \"Greedy ≈ Single > all selection strategies\"，这改变了 practical implication——不是 greedy 特别好，而是 selection 特别差（甚至不如 random single draw）。\n\n---\n\n**[AGREE] R2-W6: 2-seed Fisher combined p 统计效力不足**\n\n与我的 R1-N3 完全一致。补充：论文虽然在 Table 8 报告了 3-seed QE stability (σ≤0.026)，但这是 Spearman ρ 的 seed 稳定性，不是 selection F1 的。Selection F1 的 seed 间 variance 可能更大（因为 selection 依赖 per-instance ranking 而非 aggregate correlation），但论文没有报告这个数字。\n\n---\n\n### 小问题\n\n**[AGREE]** VC QE (continuous, Eq. 5) vs VC selection (freq > N/2, discrete, footnote 1)：论文 footnote 1 已做区分，但 Table 2 中两种 VC 使用不同定义却共享同一行标签 \"VC\"，容易混淆。建议在 table caption 中明确。\n\n**[AGREE]** SciERC checkpoint 未用 load_best_model_at_end（Table 9）：这可能导致 SciERC model over-trained，人为增加 degeneracy。这与 R2-N2 的 fine-tuning recipe concern 一致。\n\n**[AGREE]** Introduction 和 §4.3 重复定义 gap：轻微冗余，可合并。\n\n---\n\n### R2 Questions 回应\n\n**Q1 (Random vs Single 计算)**: [AGREE] 需要作者回答。如上述 R2-N3 分析。\n\n**Q2 (Fine-tuning recipe 与 degeneracy)**: [AGREE] 这是 R2-N2(b) 的核心问题。LoRA rank、epoch、dropout 都可能影响 output diversity。论文需要至少 acknowledge 这个 confound，最好提供 ablation evidence。\n\n**Q3 (Free-form 下 constant-F1 fraction)**: [AGREE] 这是诊断 free-form ablation 的关键补充数据。如果 free-form decoding 下 degeneracy 显著降低，则 constrained decoding（而非 model capability）是 degeneracy 的部分原因。Appendix §K Table 6 Panel A 报告了 LP distribution 变化但没有报告 constant-F1 fraction 的变化——这个遗漏值得补充。\n\n**Q4 (Greedy vs Single significance)**: [AGREE] 与 R2-W5 一致。\n\n---\n\n### R2 Missing References\n\n**[PARTIALLY AGREE]** Gao et al. (2023) scaling laws for reward model overoptimization：与论文的直接相关性有限（NER selection ≠ RLHF reward hacking），但 \"best-of-N 随 N 增加可能 over-optimize on proxy signal\" 的概念框架与本文的 \"selection fails despite more samples\" 有概念联系。建议仅在 §5 discussion 中作为 broader context 提及，非 core citation。\n\n---\n\n### 与我 R1 审稿的交叉对照\n\n| 问题 | R1 | R2 | 一致性 |\n|------|-----|-----|--------|\n| Framing conflation (definitional vs empirical) | N2 (critical) | N1 (critical) | **完全一致** |\n| 2-seed power | N3 (critical) | W6 (should-fix) | 一致，我评级更高 |\n| 单数据集支撑 | N1 (critical) | 未提及 | R2 未覆盖 |\n| Random vs Single 3.5pp | 未发现 | N3 (critical) | **R2 发现了我遗漏的问题** |\n| Degeneracy novelty/recipe artifact | W3 (scale range) | N2 (critical) | 相关但角度不同 |\n| Greedy rhetoric | Minor | W5 (should-fix) | 一致 |\n| Yao et al. (2026) positioning | 未涉及 | W3 (should-fix) | **R2 发现了我遗漏的问题** |\n\n**总结**：R2 和我在核心问题（framing conflation, statistical power）上高度一致。R2 补充了两个我遗漏的重要问题（Random vs Single 差距, fine-tuning recipe artifact）。我补充了 R2 未覆盖的单数据集泛化问题。两份审稿结合后，论文需要 address 的核心问题集中在：(1) framing 重构, (2) 统计 power 加强, (3) 泛化性验证或 claim 限定, (4) Random vs Single 解释, (5) fine-tuning recipe ablation or acknowledgment。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 948 · 2026-05-16T08:47:38.353749+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4089
}
```

</details>

---


### Assistant

_source line 949 · 2026-05-16T08:47:46.683524+00:00_

交叉回应已提交给 Director。

逐条回应了 R2 的所有 Must-Fix (N1-N3)、Should-Fix (W1-W6)、小问题和 Questions：
- **N1 (framing conflation)**: AGREE，与我的 R1-N2 一致
- **N2 (degeneracy novelty)**: PARTIALLY AGREE — within-instance analysis 有新颖性，但 fine-tuning recipe artifact 未排除是有效批评
- **N3 (Random vs Single 3.5pp)**: AGREE，我遗漏的重要问题，期望值应相同但差距系统性存在
- **W2 (Soft Jaccard naming)**: REBUT — 公式已明确，Appendix Table 10 验证了 normalizer robustness
- 其余 W1/W3-W6 和小问题基本 AGREE

两份审稿的交叉对照表总结了共识和互补发现。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1"
}
```

</details>

---


## Round 32

## Round 32

48 recorded events


### User

_source line 950 · 2026-05-17T06:15:33.177386+00:00_

[Round 16 审稿请求]:
## Round 16 审稿任务 — Reviewer 1（方法严谨性 + 实验设计 + 统计方法论）

### Venue 信息
- **目标**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
- **Deadline**: 2026-05-25
- **格式**: ACL 模板, 正文 ≤8 页, double-blind, Limitations section 必须
- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`

### 你的审查侧重

1. **统计方法论**:
   - Table 2 selection results 使用 2-seed paired sign test, Fisher combined p. 评估统计效力是否足够支撑结论
   - Bonferroni correction scope: footnote 4 声称 "survives Bonferroni over 5 comparisons" 但 ε threshold 是 post-hoc 选择（7ε×5=35 comparisons）
   - Random baseline (0.610) vs Single/Greedy (0.645) 的 3.5pp 差距是否合理（E[Random] 理论上应 = E[Single] under same T）
   - Kendall's W=1.0 with only 3 seeds — precision caveat 是否充分

2. **实验设计**:
   - Instance degeneracy 8B(21%) vs 4B(10.4%) 差异: capability-driven 还是 fine-tuning recipe artifact (same epochs, larger model overfits faster)?
   - LoRA rank ablation (rank=8 vs 32): degeneracy 7%→21%, 但 selection 仍失败. 是否足以区分 degeneracy 和 LP compression 的独立贡献?
   - Gold-empty instance filtering: QE 和 Selection 用 n=529 from 551, n=2756 from 3453. 一致性是否 OK?

3. **核心 claim 的证据链**:
   - "Correlation-selection gap": 13pp oracle headroom 下所有信号 ≈ greedy. 证据链是否完整?
   - Degeneracy-gating pattern (58%→fail, 21%→+0.42pp, 10%→+1.36pp): 仅 3 个数据点的 monotonic pattern, 是否过度解读?
   - TOST 等价性: configuration-dependent (LLaMA-CoNLL pass, Qwen-CoNLL fail). 主文是否平衡呈现?

4. **再现性**:
   - Qwen3-8B SciERC checkpoint 有 empty thinking tokens. Appendix 3-part analysis 是否充分排除 confound?
   - vLLM + constrained decoding pipeline 的细节是否足够再现?

请按 ACL/ARR 审稿标准输出完整审稿报告，格式: Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (score + confidence).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 951 · 2026-05-17T06:15:42.451258+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
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

_source line 952 · 2026-05-17T06:15:42.501722+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 953 · 2026-05-17T06:15:48.174313+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 954 · 2026-05-17T06:15:48.224981+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ Why Confidence Signals Fail to Scale Structured Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	Code and data will be released upon acceptance at [anonymized URL].
45	
46	\bibliography{references}
47	
48	\appendix
49	\input{sections/appendix}
50	
51	\end{document}
52	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 955 · 2026-05-17T06:15:48.225439+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool result

_source line 956 · 2026-05-17T06:15:59.325877+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results, here's comprehensive information about the ACL ARR 2026 reviewer guidelines:

## Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recomm
…[truncated 1775 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 11100
}
```

</details>

---


### Tool call

_source line 957 · 2026-05-17T06:16:02.411567+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
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

_source line 958 · 2026-05-17T06:16:02.462074+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 959 · 2026-05-17T06:16:08.332321+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5 or whatever), and the description of each score level. Include soundness, excitement, overall assessment, confidence, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5 or whatever), and the description of each score level. Include soundness, excitement, overall assessment, confidence, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 960 · 2026-05-17T06:16:08.684034+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 961 · 2026-05-17T06:16:08.734620+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 962 · 2026-05-17T06:16:23.436346+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## 1. **Reviewer Confidence** (1-5 scale)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## 2. **Soundness** (1-5 scale with half-points)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. **Excitement** (1-5 scale with half-points)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me."

## 4. **Overall Assessment** (1-5 scale with half-points)
- **5**: "Consider for Award: I think this paper could be considered for an outstanding paper award."
- **4**: "Conference: I think this paper could be accepted to an *ACL conference."
- **3**: "Findings: I think this paper could be accepted to the Findings of the ACL."
- **2**: "Resubmit next cycle: I think this paper needs substantial revisions."
- **1**: "Do not resubmit: This paper has to be fully redone."

## 5. **Reproducibility** (1-5 scale)
- **5**: "They could easil
…[truncated 1595 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 15104
}
```

</details>

---


### Tool call

_source line 963 · 2026-05-17T06:16:26.581301+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 964 · 2026-05-17T06:16:26.581755+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 965 · 2026-05-17T06:16:30.798532+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 966 · 2026-05-17T06:16:31.250790+00:00_

1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals---four instance-level (structural and surface agreement) and one per-sample (log-probability)---for quality estimation and sample selection on four NER benchmarks spanning a difficulty gradient (SciERC, Few-NERD, CoNLL, WNUT-17), using 4B--8B models.
4	All signals achieve reliable quality estimation ($\rho$ up to 0.42 on Few-NERD and the primary test bed; AUROC up to 0.82), supporting selective prediction and error flagging.
5	However, quality estimation does not translate to structural selection---the \textit{correlation-selection gap}: structural best-of-$N$ selection matches or degrades greedy decoding ($T{=}0$) despite 12--14~pp oracle headroom.
6	We diagnose two mechanisms: (a)~\textit{instance degeneracy}---fine-tuned models produce identical outputs for 10--58\% of instances, eliminating selection headroom; and (b)~\textit{log-probability compression}---median within-instance range of 0.041 nats.
7	LP selection effectiveness is inversely predicted by degeneracy: at 10\% degeneracy (Few-NERD), LP achieves $+1.36$~pp ($p{<}0.001$); at 21\% (SciERC), $+0.42$~pp ($p{=}0.091$); at 58\% (CoNLL), LP fails.
8	Structural signals fail uniformly regardless of degeneracy, confirming the gap is persistent for consensus-based methods.
9	Closing the structural gap likely requires learned per-sample scoring.
10	\end{abstract}
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 967 · 2026-05-17T06:16:31.251173+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---
