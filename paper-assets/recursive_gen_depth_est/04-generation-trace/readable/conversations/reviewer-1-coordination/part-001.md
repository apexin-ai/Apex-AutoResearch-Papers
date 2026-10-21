# Reviewer 1 coordination — Part 1 of 3

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Conversation logs

[Transcript overview](../reviewer-1-coordination.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/b5/b5a69f660c93ec0a662f.json)

## Round 1

## Round 1

46 recorded events


### User

_source line 1 · 2026-05-15T10:41:46.978180+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验完整性）

### Venue 信息
- **目标**: EMNLP 2026 Main Conference (ARR May cycle)
- **Deadline**: 2026-05-25 23:59 AoE
- **格式**: ACL 模板, double-blind, long paper ≤8 页（不含 Limitations/References）
- **匿名规则**: double-blind（正文不得包含作者身份信息）
- **Limitations section**: 必须包含，不计入页数

### 论文路径
`projects/recursive_gen_depth_est/docs/paper/main.tex`
（子文件: abstract.tex, introduction.tex, related_work.tex, method.tex, atlas.tex, generalization.tex, discussion.tex, conclusion.tex, section_appendix.tex）
引用文件: `references.bib`

### 你的审查侧重

**方法严谨性**：
1. 任务形式化（Section 2）：recursive generation chain 定义是否严密？ordinal classification formalization 是否合理？与已有 formalization 的区别是否清晰？
2. Benchmark 构建：3 model × 3 strategy × 4 depth 设计是否覆盖足够？5000 samples/cell 是否充分？Wikipedia seed text 是否引入 domain bias？LoRA finetuning 参数选择是否有 justification？
3. Feature design（19 features）：feature 设计是否有理论依据？feature 之间的冗余度（如 perplexity percentiles 与 surprisal statistics）是否讨论？reference model 选择（GPT-2 base 124M）的 circularity 问题
4. EDD 定义（Eq. 1）：公式是否正确？threshold T=0.75 选择是否 justified？binary pairwise RF 的 500 trees 是否有 convergence justification？
5. 分类器选择：RF 200 trees 是否有超参搜索？5-fold CV 是否充分？随机种子是否报告？

**实验完整性**：
6. 主实验（Table 1, 3×3 matrix）：accuracy 报告是否包含标准差/CI？是否报告了 per-class metrics？
7. Baseline 比较（Table 2）：baseline 选择是否充分？zero-shot LLM baseline 仅 200 samples 是否可信？DivEye 使用相同 19 features 是否公平对比？
8. Cross-model/cross-strategy transfer（Tables 3-4）：LOO 设计是否合理？per-class recall 数据的解读是否诚实？
9. DCOL negative result（Section 5.4）：6 配置中 5 个失败是否足以下结论？hyperparameter search 是否充分？与 CLOC 的关系是否交代？
10. 统计显著性：全文是否有 significance tests？CI 报告是否一致？bootstrap CI 方法是否说明？
11. 数据泄漏风险：train/test split 是否在 passage 级别？同一 model-strategy cell 内不同 depth 的 passages 是否来自相同 seed？
12. Reproducibility：代码/数据是否计划公开？实验细节是否足以复现？

请对每个维度给出具体评价（引用论文中的 Section/Table/Figure/公式编号），最后给出 summary + strengths + weaknesses + questions + overall score。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-15T10:41:53.413369+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3 · 2026-05-15T10:41:53.414127+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-15T10:41:55.773793+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2"
  }
}
```

</details>

---


### Tool result

_source line 5 · 2026-05-15T10:41:55.824471+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-15T10:41:58.035476+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2"
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-15T10:41:58.086055+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-15T10:42:01.105243+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-15T10:42:01.155980+00:00_

1	% How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
2	% Target: EMNLP 2026 (ARR May cycle)
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{amsmath}
10	\usepackage{amssymb}
11	\usepackage{multirow}
12	\usepackage{xcolor}
13	\usepackage{subcaption}
14	\usepackage[T1]{fontenc}
15	\usepackage[utf8]{inputenc}
16	\usepackage{microtype}
17	
18	\title{How Deep Is Your Data? Estimating Recursive Generation Depth\\via Statistical Fingerprints}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\input{abstract}
26	
27	\input{introduction}
28	
29	\input{related_work}
30	
31	\input{method}
32	
33	\input{atlas}
34	
35	\input{generalization}
36	
37	\input{discussion}
38	
39	\input{conclusion}
40	
41	\bibliography{references}
42	
43	\appendix
44	\input{section_appendix}
45	
46	\end{document}
47	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-15T10:42:04.270408+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-15T10:42:04.723065+00:00_

1	\begin{abstract}
2	As large language models increasingly train on web text containing their own outputs, a recursive model$\to$data$\to$model loop arises---yet no method estimates how many such iterations a text has undergone.
3	We formalize \emph{recursive generation depth estimation} as ordinal classification and construct a benchmark of 180K passages spanning 3 model families, 3 decoding strategies, and 4 generation depths.
4	From each passage we extract 19 statistical features---perplexity percentiles, surprisal moments, and lexical diversity measures---computed against a fixed reference model (GPT-2 base, 124M).
5	A Random Forest classifier achieves 70--85\% four-class accuracy (chance = 25\%; a zero-shot LLM baseline reaches only 40\%), with 90th-percentile perplexity and surprisal variance emerging as universal depth markers (top-2 importance in 9/9 and 7/9 model--strategy cells, respectively; mean Spearman $\rho{=}0.868$).
6	Our \emph{Depth Degradation Atlas} reveals that decoding strategy reshapes degradation trajectories rather than merely attenuating them, and we define the \emph{Effective Discriminable Depth} (EDD) metric, finding $\mathrm{EDD}_{0.75}{=}4$ for extended recursion chains.
7	Cross-model transfer reaches 66.4\% and cross-strategy transfer 59.1\%, though temperature sampling induces a d1/d2 AUC inversion that z-score normalization cannot resolve.
8	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-15T10:42:04.723490+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-15T10:42:05.179169+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	The text on which large language models are trained increasingly contains their own outputs.
5	As synthetic content proliferates across the web, a recursive loop emerges: models trained on web corpora ingest text generated by earlier models, and their outputs feed into the next generation's training data \cite{shumailov2024_nature,alemohammad2024_mad}.
6	This model$\to$data$\to$model cycle is no longer hypothetical---it is already occurring in the wild---yet we lack the ability to determine how many recursive iterations a given text has undergone, a distinction that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \cite{dohmatob2024_tale_of_tails}.
7	
8	Existing tools address adjacent but distinct problems.
9	Binary detectors such as Binoculars \cite{binoculars2024}, Fast-DetectGPT \cite{fast_detectgpt2024}, and DivEye \cite{diveye2026} classify text as human-written or machine-generated, collapsing all generation depths $d \geq 1$ into a single category.
10	Watermarking schemes \cite{kirchenbauer2023_watermark} require proactive embedding and cannot be applied retroactively to existing corpora.
11	The model collapse literature \cite{shumailov2024_nature,dohmatob2024_tale_of_tails} characterizes how recursive training degrades model quality but assumes the generation depth is known a priori---the very quantity we seek to estimate.
12	\citet{drayson2025_detection_prevents_collapse} show that filtering synthetic data from training corpora can prevent collapse, yet their approach relies on binary detection and does not distinguish among recursive depths.
13	EditLens \cite{editlens2026} estimates the extent of single-pass editing applied to a text but does not address multi-step recursive generation.
14	No existing method estimates the ordinal recursive depth of a text passage from its 
…[truncated 3622 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 14 · 2026-05-15T10:42:05.179627+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-15T10:42:05.681761+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Model Collapse Theory.}
5	\citet{shumailov2024_nature} demonstrate that recursively training language models on their own outputs erodes distributional tails, eventually collapsing the output distribution to a narrow mode.
6	\citet{dohmatob2024_tale_of_tails} formalize this phenomenon through scaling laws that distinguish tail \emph{narrowing} (reduced variance) from tail \emph{cutting} (lost support), showing both accelerate with recursion depth.
7	The MAD framework \cite{alemohammad2024_mad} extends this analysis to self-consuming generative models and quantifies the precision--recall tradeoff as synthetic data accumulates across generations.
8	\citet{gerstgrasser2024_accumulate} show that retaining real data alongside synthetic data across generations mitigates collapse, while \citet{drayson2025_detection_prevents_collapse} demonstrate that filtering synthetic samples via binary detection can preserve model quality.
9	Recent work further refines the theoretical picture: \citet{bakshi2026_collapse_improvement} identify non-monotonic dynamics where early recursion can temporarily \emph{improve} model quality before eventual degradation; \citet{marchi2024_heat_death} characterize convergence to a fixed-point ``heat death'' distribution; and \citet{wang2026_contamination} derive contamination guarantees bounding how much synthetic data a corpus can absorb.
10	Additional lines of work address curated synthetic pipelines \cite{falahati2026_curated}, knowledge collapse in factual recall \cite{knowledge_collapse2025}, spectral signatures of model-generated text \cite{sigma2026_spectral}, and the ``synthetic eggs'' problem in self-improving loops \cite{synthetic_eggs2026}.
11	These works characterize degradation patterns but assume the generation depth is known a priori; our work addresses the inverse problem of estimating depth from text alone.
12	
13	\paragraph{AI Text Detection.}
14	DetectGPT \cite{mitchell
…[truncated 3325 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-15T10:42:05.682246+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-15T10:42:06.134336+00:00_

1	\section{Task Formulation}
2	\label{sec:method}
3	
4	\subsection{Problem Definition}
5	\label{sec:method:problem}
6	
7	Let $f_\theta$ denote a language model and $\mathcal{D}_0$ a corpus of human-written seed text.
8	We define a \emph{recursive generation chain} of depth $K$ as the sequence $\mathcal{D}_0, \mathcal{D}_1, \dots, \mathcal{D}_K$, where each $\mathcal{D}_k$ ($k \geq 1$) is produced by finetuning $f_\theta$ on $\mathcal{D}_{k-1}$ and sampling from the resulting model.
9	Depth $d{=}0$ denotes human-written text; depth $d{=}k$ ($k \geq 1$) denotes text generated by a model trained on depth-$(k{-}1)$ data.
10	
11	Given a text passage $x$, the task is to estimate its recursive generation depth $d \in \{0, 1, \dots, K\}$.
12	This is an ordinal classification problem: depths carry a natural ordering, and $d{=}1$ is structurally closer to $d{=}0$ than $d{=}3$ is, since each generation step compounds distributional drift.
13	
14	\subsection{Multi-Generational Benchmark Construction}
15	\label{sec:method:benchmark}
16	
17	We construct a benchmark spanning three axes: model family, decoding strategy, and generation depth.
18	
19	\paragraph{Model families.}
20	We select three 1--1.5B-parameter models with diverse pretraining corpora and architectures: Pythia-1.4B (EleutherAI), OLMo-1B (AI2), and GPT-2~XL (OpenAI, 1.5B).
21	Restricting to a narrow parameter range isolates the effect of architecture and training data from scale.
22	
23	\paragraph{Decoding strategies.}
24	Each model is paired with three sampling methods: nucleus sampling ($p{=}0.95$) \cite{holtzman2020_nucleus}, temperature sampling ($\tau{=}0.9$), and top-$k$ sampling ($k{=}50$).
25	These span the dominant modes of open-ended generation and induce qualitatively different entropy profiles.
26	
27	\paragraph{Depth and scale.}
28	The primary benchmark covers depths d0--d3 across all $3 \times 3 = 9$ model--strategy cells, with 5{,}000 samples per depth per cell (180K samples total).
29	For depth exten
…[truncated 5419 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-15T10:42:06.134844+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-15T10:42:06.586915+00:00_

1	\section{The Depth Degradation Atlas}
2	\label{sec:atlas}
3	
4	We systematically characterize how recursive generation reshapes the statistical profile of text across a grid of 3 model families $\times$ 3 decoding strategies $\times$ 4 generation depths (d0--d3), yielding 9 experimental configurations each spanning 4 depths.
5	For each cell we train a Random Forest (RF) classifier on the 19 statistical features defined in \S\ref{sec:method} and examine (i)~in-distribution depth classification accuracy, (ii)~which features carry depth signal, (iii)~how far into the recursion chain depth remains discriminable, and (iv)~how decoding strategy modulates the degradation trajectory.
6	
7	\subsection{In-Distribution Performance}
8	\label{sec:atlas:indist}
9	
10	Table~\ref{tab:main_matrix} reports 4-class depth estimation accuracy under 5-fold cross-validation.
11	All 9 cells exceed chance (25\%) by a wide margin, with accuracy ranging from 69.6\% to 85.4\%.
12	Both model family and decoding strategy influence accuracy, though model choice accounts for larger variation (15.8pp range across models vs.\ 8.6pp across strategies), with consistent ordering (GPT-2~XL $>$ OLMo $>$ Pythia) across all strategies.
13	Among strategies, temperature sampling ($\tau{=}0.9$) yields the best accuracy in 2 of 3 model families, while top-$k$ ($k{=}50$) trails by 6--9 percentage points.
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\caption{In-distribution 4-class depth estimation accuracy (\%) across 3 model families $\times$ 3 decoding strategies. RF classifier with 19 statistical features, 5-fold CV. Chance = 25\%.}
19	\label{tab:main_matrix}
20	\begin{tabular}{lccc}
21	\toprule
22	Model & Nucleus & Temp & Top-$k$ \\
23	 & $p{=}0.95$ & $\tau{=}0.9$ & $k{=}50$ \\
24	\midrule
25	Pythia-1.4B & 78.2 & 76.3 & 69.6 \\
26	OLMo-1B & 78.8 & 82.0 & 74.2 \\
27	GPT-2 XL & 83.3 & \textbf{85.4} & 76.6 \\
28	\bottomrule
29	\end{tabular}
30	\end{table}
31	
32	Because the human-written seed text (d0)
…[truncated 8330 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-15T10:42:06.587294+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
  }
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-15T10:42:07.491518+00:00_

1	\section{Generalization and Robustness}
2	\label{sec:generalization}
3	
4	The atlas (\S\ref{sec:atlas}) established in-distribution accuracy of 69.6--85.4\%.
5	We now test whether these results reflect genuine statistical regularities or artifacts of specific training conditions, evaluating four axes: classifier choice (\S\ref{sec:gen:baselines}), cross-model transfer (\S\ref{sec:gen:crossmodel}), cross-strategy transfer (\S\ref{sec:gen:crossstrategy}), and end-to-end learned representations (\S\ref{sec:gen:dcol}).
6	
7	\subsection{Baseline Comparison}
8	\label{sec:gen:baselines}
9	
10	Table~\ref{tab:baselines} compares classification methods on the Pythia-1.4B nucleus setting.
11	Three feature-based methods---Random Forest (RF), CORAL ordinal regression \cite{coral2020}, and DivEye \cite{diveye2026}---all operate on the same 19 statistical features and achieve near-identical accuracy (78.1--78.2\%).
12	A cross-entropy MLP and logistic regression trail by $\sim$3 percentage points.
13	Single-feature regression on mean perplexity performs at chance (25.1\%), confirming that depth estimation requires the multi-dimensional feature representation defined in \S\ref{sec:method}.
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\caption{Comparison of classification methods on Pythia-1.4B nucleus. RF, CORAL, and DivEye use the same 19 statistical features. Chance = 25\%.}
19	\label{tab:baselines}
20	\begin{tabular}{lc}
21	\toprule
22	Method & 4-class Acc (\%) \\
23	\midrule
24	RF (19 features) & \textbf{78.2} \\
25	CORAL & 78.1 \\
26	DivEye & 78.2 \\
27	CE-MLP & 74.9 \\
28	LR & 75.0 \\
29	DeepSeek V3.2 (zero-shot)\footnotemark & 40.0 \\
30	ppl-regression (single feature) & 25.1 \\
31	\bottomrule
32	\end{tabular}
33	\footnotetext{Evaluated on 200 samples (50 per class) from the Pythia-1.4B nucleus cell only, due to API cost; 95\% CI: $\pm$6.8pp. All other methods use the full 20{,}000-sample set.}
34	\end{table}
35	
36	RF and CORAL achieve near-identical accuracy (gap $<
…[truncated 5234 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-15T10:42:07.542142+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-15T10:42:07.994331+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Implications}
5	\label{sec:discussion:implications}
6	
7	\paragraph{Depth-graduated data curation.}
8	Binary synthetic-data filters discard all machine-generated text indiscriminately, yet first-generation outputs may be beneficial for training \cite{drayson2025_detection_prevents_collapse}.
9	Predicted depth can serve as a continuous quality proxy for importance weighting in curation pipelines \cite{dsir2023,qurating2024}, retaining shallow-generation text while down-weighting deeply recursive samples.
10	
11	\paragraph{Feature evolution tracks tail erosion.}
12	Feature importance shifts with depth: \textsc{var\_surprisal} dominates at shallow recursions while \textsc{p90\_ppl} and kurtosis assume greater importance at deeper depths, aligning with the tail erosion theory of \citet{shumailov2024_nature}.
13	
14	\paragraph{Cross-strategy deployment.}
15	The temperature-induced d1/d2 AUC inversion (\S\ref{sec:gen:crossstrategy}) means that deploying a depth estimator without knowing the target decoding strategy risks systematic prediction reversals; strategy-conditioned classifiers are needed but strategy identification from text remains open.
16	
17	\subsection{Limitations}
18	\label{sec:discussion:limitations}
19	
20	\paragraph{Controlled setting and reference model.}
21	All experiments use Wikipedia seed text, LoRA finetuning, and 1--1.5B parameter models; transfer to mixed-domain text, instruction-tuned models, and larger scales (7B+) remains open.
22	Features are computed relative to GPT-2 base (124M), introducing partial overlap when GPT-2~XL is held out, though GPT-2~XL holdout accuracy (67.6\%) does not exceed the unrelated OLMo (69.2\%).
23	
24	\paragraph{Feature fragility and assumptions.}
25	Detection features degrade under domain shift \cite{pudasaini2026_detection_fails}; our depth features are likely susceptible.
26	Additionally, \citet{bakshi2026_collapse_improvement} find that early recur
…[truncated 235 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-15T10:42:08.045083+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-15T10:42:08.497731+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced recursive generation depth estimation and demonstrated that 19 lightweight statistical features suffice for 70--85\% four-class accuracy (chance = 25\%).
5	The Depth Degradation Atlas reveals universal depth markers (p90 perplexity, surprisal variance) alongside strategy-dependent trajectories, with $\mathrm{EDD}_{0.75}{=}4$.
6	Cross-model transfer reaches 66.4\% and cross-strategy transfer 59.1\%; the temperature-induced d1/d2 inversion and DCOL's failure (best 64.5\% vs.\ RF 78.2\%) underscore both the problem's difficulty and the effectiveness of explicit statistical features.
7	Future work should address wild-data transfer, larger model scales, strategy-conditioned classifiers, and empirical validation of depth-graduated data curation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-15T10:42:08.498148+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-15T10:42:08.749278+00:00_

1	\section{Additional Results}
2	\label{app:additional}
3	
4	\subsection{Top-$k$ Feature Trajectories}
5	\label{app:topk_trajectories}
6	
7	Figure~\ref{fig:feature_trajectory} in the main text shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\tau{=}0.9$) sampling.
8	Top-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \S\ref{sec:atlas:trajectories}.
9	Concretely, the d0$\to$d1 drop in \textsc{p90\_ppl} under top-$k$ is 78\% (vs.\ 87\% for nucleus), and the d2$\to$d3 reduction is 31\% (vs.\ 39\% for nucleus).
10	Despite the magnitude reduction, feature rank ordering across depths is preserved, which explains why ordinal classifiers maintain directionality even under top-$k$ conditions.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-15T10:42:08.749765+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-15T10:42:08.800400+00:00_

1	@article{shumailov2024_nature,
2	  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
3	  title     = {{AI models collapse when trained on recursively generated data}},
4	  journal   = {Nature},
5	  year      = {2024},
6	  doi       = {10.1038/s41586-024-07566-y},
7	}
8	
9	@inproceedings{marchi2024_heat_death,
10	  author    = {Marchi, Matteo and Soatto, Stefano and Chaudhari, Pratik and Tabuada, Paulo},
11	  title     = {{Heat Death of Generative Models in Closed-Loop Learning}},
12	  booktitle = {Proceedings of ICASSP},
13	  year      = {2024},
14	  note      = {arXiv:2404.02325},
15	  url       = {https://arxiv.org/abs/2404.02325},
16	}
17	
18	@inproceedings{dohmatob2024_tale_of_tails,
19	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia},
20	  title     = {{A Tale of Tails: Model Collapse as a Change of Scaling Laws}},
21	  booktitle = {Proceedings of ICML},
22	  year      = {2024},
23	  note      = {arXiv:2402.07043},
24	  url       = {https://arxiv.org/abs/2402.07043},
25	}
26	
27	@inproceedings{dohmatob2024_strong_collapse,
28	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
29	  title     = {{Strong Model Collapse}},
30	  booktitle = {Proceedings of ICLR},
31	  year      = {2024},
32	  note      = {arXiv:2410.04840},
33	  url       = {https://arxiv.org/abs/2410.04840},
34	}
35	
36	@inproceedings{dohmatob2024_demystified,
37	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia},
38	  title     = {{Model Collapse Demystified: The Case of Regression}},
39	  booktitle = {Proceedings of NeurIPS},
40	  year      = {2024},
41	  note      = {arXiv:2402.07712},
42	  url       = {https://arxiv.org/abs/2402.07712},
43	}
44	
45	@inproceedings{alemohammad2024_mad,
46	  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and others},
47	  title     = {{Self-Consuming Ge
…[truncated 12012 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-15T10:42:14.381178+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
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

_source line 31 · 2026-05-15T10:42:14.482066+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-15T10:42:17.999539+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form criteria 2025 2026 reviewer guidelines scoring dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form criteria 2025 2026 reviewer guidelines scoring dimensions"
  }
}
```

</details>

---


### Tool call

_source line 33 · 2026-05-15T10:42:18.150474+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR reviewer guidelines review form dimensions scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR reviewer guidelines review form dimensions scoring"
  }
}
```

</details>

---


### Tool result

_source line 34 · 2026-05-15T10:42:25.335547+00:00_

Web search results for query: "ACL ARR review form criteria 2025 2026 reviewer guidelines scoring dimensions"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"}]

Based on the search results, here is information about ACL ARR review form criteria, reviewer guidelines, and scoring dimensions for 2025-2026:

## Scoring Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundne
…[truncated 1296 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7336
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-15T10:42:26.089774+00:00_

Web search results for query: "EMNLP 2026 ARR reviewer guidelines review form dimensions scoring"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl?lang=en"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"}]

Based on the search results, here's information about the ARR reviewer guidelines and scoring dimensions for EMNLP 2026:

## ARR Review Form Scoring Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Three Scoring Dimensions:

1. **Soundness**: The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to
…[truncated 1151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7939
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-15T10:42:29.759223+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
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

_source line 37 · 2026-05-15T10:42:29.860091+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-15T10:42:33.774250+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5 or other), and the description of each score level. I need the exact scale definitions for Soundness, Excitement, and Overall Recommendation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5 or other), and the description of each score level. I need the exact scale definitions for Soundness, Excitement, and Overall Recommendation."
  }
}
```

</details>

---


### Tool call

_source line 39 · 2026-05-15T10:42:35.134793+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the full reviewer guidelines, especially: what dimensions reviewers must score, the scale for each dimension, what counts as a strength vs weakness, reproducibility requirements, and any specific instructions about how to evaluate soundness, excitement, and overall recommendation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the full reviewer guidelines, especially: what dimensions reviewers must score, the scale for each dimension, what counts as a strength vs weakness, reproducibility requirements, and any specific instructions about how to evaluate soundness, excitement, and overall recommendation."
  }
}
```

</details>

---


### Tool result

_source line 40 · 2026-05-15T10:42:38.699920+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Soundness Scale (1-5)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## Excitement Scale (1-5)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would."

## Overall Assessment Scale (1-5)
- **5**: Consider for Award (top 2.5% papers)
- **4**: Conference acceptance recommendation
- **3**: Findings track acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit

Additional dimensions include Reviewer Confidence, Reproducibility, Datasets, and Software (all using similar 1-5 scales).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 4925
}
```

</details>

---


### Tool result

_source line 41 · 2026-05-15T10:42:42.120735+00:00_

# ARR Reviewer Guidelines: Scoring Dimensions and Evaluation Criteria

## Scoring Dimensions

ARR reviewers provide **three scores**:

1. **Soundness** - Technical quality and validity of the research
2. **Excitement** - Personal interest level (subjective, orthogonal to soundness)
3. **Overall Recommendation** - Composite assessment for venue suitability

The guidelines note that "soundness scores must be justified by the text of the review" and low scores without sufficient justification indicate your review lacks consistency.

## Scale Information

The document does not explicitly specify numerical scales for each dimension. However, it mentions a "confidence score" and references an ARR review form with specific fields, suggesting OpenReview's interface determines the actual scale.

## Strengths vs. Weaknesses

**What counts as legitimate weaknesses:**
- Technical unsoundness, missing proofs, or incorrect assumptions
- Insufficient evidence for claims made
- Undisclosed methodological issues in data/experiments
- Unclear research questions or contributions

**What does NOT constitute weaknesses:**
The guidelines identify 17 problematic review heuristics (H1-H17), including:
- Dismissing results as "unsurprising" or contradicting expectations
- Requiring SOTA results unnecessarily
- Criticizing simplicity of methods
- Demanding extra experiments beyond supporting the stated claim

## Reproducibility Requirements

Papers must provide:
- Sufficient detail for experiment reproduction, including hyperparameters
- Clear disclosure about code/data availability
- Justification if materials won't be released

Reviewers assess reproducibility but aren't obligated to run code.

## Evaluating Each Dimension

**Soundness:** "Must be justified by the text" - identify specific technical flaws, methodology concerns, or logical gaps.

**Excitement:** "Reflects our personal taste" and doesn't require explicit justification; acknowledges subjectivity.

**Overall Recommendation:** 
…[truncated 143 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6985
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-15T10:44:48.030819+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
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

_source line 43 · 2026-05-15T10:44:48.031277+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-15T10:46:28.125066+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 1 审稿报告 — Reviewer 1（方法严谨性 + 实验完整性）\n\n## 总体评分\n**Overall**: 3/5（Findings track acceptance）\n**一句话总结**: 提出了一个新颖且有价值的任务（recursive generation depth estimation），实验设计系统性强，但核心指标 EDD 存在公式与报告值不一致的 off-by-one 错误，主实验缺乏统计显著性报告，DCOL negative result 证据不足以支撑其结论。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心指标 EDD 公式有 off-by-one 错误；主实验无 std/CI；feature importance 分析受 correlated features 影响；DCOL 负面结论证据薄弱 |\n| Excitement | 3/5 | 任务定义新颖，depth estimation 是真正的未填补空白；但方法偏传统（RF + handcrafted features），scope 受限于 1–1.5B 模型和 Wikipedia |\n| Overall | 3/5 | 问题有价值，atlas 分析系统性强，但方法论缺陷需修复后方可接收 |\n| Confidence | 4/5 | 我仔细阅读了全文并逐一验证了公式和数值 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] EDD 定义存在系统性 off-by-one 错误\n- 具体位置：Eq. 1 (Section 2.4) vs. Section 4.3 / Table 3 / Abstract / Figure 2 caption\n- 问题：Eq. 1 定义 $\\mathrm{EDD}_T = \\max\\{d^* : \\mathrm{AUC}(d^*, d^*{+}1) \\geq T\\}$，其中 $d^* \\in \\{0,\\dots,K{-}1\\}$。以 Pythia nucleus d0–d5 为例，AUC(3,4)=0.784≥0.75 而 AUC(4,5)=0.683<0.75，按公式 $\\mathrm{EDD}_{0.75}=\\max\\{0,1,2,3\\}=3$。但全文（Abstract、Section 4.3、Table 3、Conclusion）均报告 $\\mathrm{EDD}_{0.75}=4$。对 Table 3 所有行验证发现报告值均比公式计算值大 1：$T=0.65$ 时报告 5（公式得 4），$T=0.80$ 时报告 3（公式得 2）。要么公式需修正为 $\\mathrm{EDD}_T = \\max\\{d^*{+}1 : \\mathrm{AUC}(d^*, d^*{+}1) \\geq T\\}$（即计数可区分的 depth transitions 数量），要么全文数值需下调 1。\n- 为什么影响接收：EDD 是论文四项贡献之一，Abstract/Conclusion 均以 $\\mathrm{EDD}_{0.75}=4$ 作为关键结论。公式与数值不一致直接损害论文的技术可信度。\n- 建议修改方向：明确 EDD 的语义（\"最大可区分深度索引\" vs. \"可区分 transitions 数量\"），修正 Eq. 1 或修正全文报告值，使两者一致。\n\n**N2** [critical] 主实验结果缺乏不确定性量化\n- 具体位置：Table 1 (Section 4.1)、Table 2 (Section 5.1)\n- 问题：Table 1 报告 9 个 cell 的 4-class accuracy，但没有任何一个数值附带标准差或置信区间。论文使用 5-fold CV，完全可以报告 fold-level 标准差。Table 2 的 baseline 比较同样仅报告点估计。唯一有 CI 的是 Figure 2 的 AUC 和 LLM baseline 的 ±6.8pp。\n- 为什么影响接收：ACL ARR reviewer guidelines 明确要求 reproducibility 和 sufficient evidence for claims。在 accuracy 差异仅 0.1pp（RF 78.2% vs. DivEye 78.2%）或几个 pp（RF vs. MLP）时，无法判断差异是否显著。全文无任何 significance test。\n- 建议修改方向：(1) Table 1/2 报告 5-fold CV 的 mean ± std；(2) 对关键比较（RF vs. baselines、cross-transfer 条件间）进行 paired t-test 或 bootstrap significance test；(3) 多次随机种子运行并报告 variance。\n\n**N3** [critical] DCOL 负面结论证据不足\n- 具体位置：Section 5.4\n- 问题：论文称 \"end-to-end models struggle to extract [depth-relevant information] from raw text\"，但仅测试了 1 个架构（RoBERTa-large）、1 个方法框架（DCOL）、6 个配置（其中 5 个因 embedding collapse/OOM/NaN 失败）。6 个配置的具体超参设置未报告。5/6 的失败可能是实现/调参问题而非方法论本身的局限。此外，references.bib 中包含 CLOC (cloc2025) 条目但正文从未引用或讨论为何选择 DCOL 而非 CLOC。\n- 为什么影响接收：这是论文第四项贡献（\"end-to-end learning as negative result\"），但 negative result 需要比 positive result 更强的证据——需要充分的超参搜索、多架构验证，才能排除 \"没调好\" 的解释。当前证据水平不足以支撑 \"统计特征优于端到端学习\" 的结论。\n- 建议修改方向：(1) 报告 6 个配置的完整超参；(2) 至少增加一个额外架构（如 DeBERTa-v3）或方法（如 CLOC）；(3) 弱化结论为 \"初步证据\" 而非确定性断言；(4) 讨论 CLOC 为何未被采用。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Feature importance 分析受 correlated features 影响\n- 具体位置：Section 4.2, Figure 1\n- 问题：19 个特征中，9 个 perplexity statistics 和 3 个 surprisal statistics 存在数学上的强相关（surprisal = -log p，perplexity = exp(mean surprisal)）。Gini importance 会在相关特征间分散，导致单个特征的重要性被低估。论文在 Section 2.3（method.tex line 73）简要承认相关性但称 \"not redundant\"，却未提供定量证据（如相关矩阵、VIF、ablation）。论文的核心发现之一——p90_ppl 和 var_surprisal 的 \"universality\"——直接依赖 Gini importance ranking，而该 ranking 在存在高度相关特征时不可靠。\n- 建议：(1) 提供 19 特征的相关矩阵或 VIF 分析；(2) 使用 permutation importance（对相关特征更鲁棒）替代或补充 Gini importance；(3) 做 feature group ablation（如移除全部 surprisal features 看 accuracy 变化）。\n\n**W2** [warning] Wikipedia seed text 引入的 domain bias 未被量化\n- 具体位置：Section 2.2, Table 1\n- 问题：所有 d0 来自 Wikipedia，而 d1+ 由模型生成。d0 recall >99%（Table 3）可能部分反映 Wikipedia 的文体特征（百科全书式写作、引用密集）而非 \"human vs. machine\" 的深度信号。如果用不同 domain（如新闻、Reddit、学术摘要）作为 seed text，d0 的可分离性和整体 accuracy 可能显著变化。Section 6.1 承认了限制但未做任何定量分析。\n- 建议：至少用 1 个非 Wikipedia domain（如 OpenWebText subset）做 pilot experiment 验证结论的 domain 鲁棒性。\n\n**W3** [warning] LoRA finetuning 参数缺乏 justification\n- 具体位置：Section 2.2（method.tex line 32）\n- 问题：LoRA rank=16, α=32, lr=2e-4, batch=8, epochs=3——这些参数直接决定每轮 finetuning 对模型的修改幅度，进而决定 depth signal 的强度。不同的 LoRA rank 或 learning rate 可能产生完全不同的 degradation trajectory。但论文未提供选择依据，也未做 LoRA 参数的 sensitivity analysis。\n- 建议：至少对 LoRA rank（如 r∈{4, 16, 64}）做 ablation，验证深度信号对 finetuning 强度的敏感性。\n\n**W4** [warning] Zero-shot LLM baseline 的评估样本量严重不足\n- 具体位置：Table 2 脚注（generalization.tex line 33）\n- 问题：DeepSeek V3.2 仅在 200 samples 上评估（50/class），95% CI 为 ±6.8pp（即 33.2%–46.8%），置信区间跨越了 \"接近 chance\" 到 \"明显高于 chance\" 的边界。正文称其 \"reaches only 40%\"，但 CI 下界 33.2% 离 25% chance 并不远。同时，其他方法用 20,000 samples 评估，这种非对称比较使读者难以公平解读。\n- 建议：如果 API cost 是限制，至少增加到 500–1000 samples 使 CI 缩窄到 ±3–4pp；或明确标注这是 preliminary estimate，不宜与其他方法直接比较。\n\n**W5** [warning] 潜在数据泄漏风险未讨论\n- 具体位置：Section 2.2 / Section 4\n- 问题：Generation pipeline 中，$\\mathcal{D}_0$ 是 d1 模型的 training data，$\\mathcal{D}_1$ 是 d2 模型的 training data。5-fold CV 的 split 是在 passage 级别，但未说明是否确保同一 \"generation lineage\"（同一 seed text 及其衍生 passages across depths）全部落在同一 fold。如果某个 d0 passage 在 train fold，而由同一 seed 衍生的 d1 passage 在 test fold，特征可能因内容相似性（而非深度信号）产生关联，导致 accuracy 乐观偏估。\n- 建议：(1) 明确说明 CV split 策略是否考虑了 passage lineage；(2) 如果未考虑，补充 grouped CV（按 seed text 分组）结果以排除泄漏。\n\n**W6** [warning] Cross-strategy transfer 未报告 per-class recall\n- 具体位置：Table 4 (Section 5.3)\n- 问题：Cross-model transfer（Table 3）报告了 per-class recall，揭示了 d2 recall 低至 26.8% 的关键问题。但 cross-strategy transfer（Table 4）仅报告 overall accuracy，无 per-class 信息。考虑到 temperature-induced d1/d2 inversion，cross-strategy 的 per-class recall 分析尤为重要——很可能存在比 cross-model 更严重的 class-level 失败。\n- 建议：补充 Table 4 的 per-class recall，特别是 temperature holdout 条件下。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Section 2.3 称 surprisal variance \"captures second-order structure...that is not redundant with perplexity moments\"，但 perplexity statistics 中已包含 variance。如果指的是 token-level surprisal 分布的方差与 token-level perplexity 分布的方差在数学上不同，应明确说明。\n- **M2**: RF 200 trees 和 binary RF 500 trees 的选择均无 convergence analysis 支撑。一句 \"increased from 200 to 500 trees to ensure convergence\" 不等于 justification——应展示 OOB error vs. n_estimators 曲线或类似证据。\n- **M3**: Section 5.4 提到 DCOL \"v6\" 配置名称，暗示存在 v1–v5，但正文未解释命名或区别。建议系统性报告所有配置。\n- **M4**: Appendix 较薄——仅有 top-k trajectories 一段。建议将 confusion matrices 的完整版（9 cells）、feature correlation matrix、extended depth AUC 原始数据等放入 appendix。\n- **M5**: 全文未提及代码/数据/模型开放计划。ACL ARR review form 包含 reproducibility 评分维度，缺少此信息会直接影响该维度评分。\n- **M6**: references.bib 中 `cloc2025` 条目存在但正文未引用。如果 DCOL 实验参考了 CLOC，应引用并讨论；如果无关，应清理 bib。\n\n---\n\n## 主要优势\n\n- **S1**: 问题定义新颖且有价值。Recursive generation depth estimation 是一个真正的未填补空白——现有工作只做 binary detection 或假设 depth 已知。任务形式化（ordinal classification）合理且清晰。\n- **S2**: 实验设计的系统性。3 model × 3 strategy × 4 depth 的 atlas 结构提供了多维度的 controlled comparison，这比 \"单模型单策略\" 的实验设计强得多。\n- **S3**: Temperature-induced d1/d2 AUC inversion 的发现及其对 cross-strategy deployment 的讨论（Section 5.3, Section 6.1）是实质性的 insight，对实际部署有直接指导价值。\n- **S4**: 对 EDD 的 threshold sensitivity analysis（Table 3）和 granularity ablation 展示了负责任的实验报告态度。\n- **S5**: 论文在 Limitations section（Section 6.2）坦诚地讨论了多项限制（domain bias、reference model overlap、feature fragility、monotonicity assumption violation），这种透明度值得肯定。\n\n---\n\n## Questions for Authors\n\nQ1: Eq. 1 中 EDD 的公式与全文报告值存在系统性 +1 偏差（见 N1）。请确认是公式需修正还是报告值需修正。\n\nQ2: 5-fold CV 的 split 是否考虑了 passage lineage（即同一 seed text 的 d0 passage 及其衍生 d1/d2/d3 passages 是否总在同一 fold）？如果未考虑，是否能补充 grouped CV 结果？\n\nQ3: DCOL 6 个配置的具体超参是什么？为何选择 DCOL 而非 CLOC (Pitawela et al., 2025)？\n\nQ4: 能否提供 19 特征的 Pearson/Spearman 相关矩阵？特别是 perplexity percentiles 与 surprisal statistics 之间的相关系数。\n\nQ5: 是否计划公开代码、数据和训练好的分类器？",
  "reviewer_id": "1",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 1 审稿报告 — Reviewer 1（方法严谨性 + 实验完整性）\n\n## 总体评分\n**Overall**: 3/5（Findings track acceptance）\n**一句话总结**: 提出了一个新颖且有价值的任务（recursive generation depth estimation），实验设计系统性强，但核心指标 EDD 存在公式与报告值不一致的 off-by-one 错误，主实验缺乏统计显著性报告，DCOL negative result 证据不足以支撑其结论。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心指标 EDD 公式有 off-by-one 错误；主实验无 std/CI；feature importance 分析受 correlated features 影响；DCOL 负面结论证据薄弱 |\n| Excitement | 3/5 | 任务定义新颖，depth estimation 是真正的未填补空白；但方法偏传统（RF + handcrafted features），scope 受限于 1–1.5B 模型和 Wikipedia |\n| Overall | 3/5 | 问题有价值，atlas 分析系统性强，但方法论缺陷需修复后方可接收 |\n| Confidence | 4/5 | 我仔细阅读了全文并逐一验证了公式和数值 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] EDD 定义存在系统性 off-by-one 错误\n- 具体位置：Eq. 1 (Section 2.4) vs. Section 4.3 / Table 3 / Abstract / Figure 2 caption\n- 问题：Eq. 1 定义 $\\mathrm{EDD}_T = \\max\\{d^* : \\mathrm{AUC}(d^*, d^*{+}1) \\geq T\\}$，其中 $d^* \\in \\{0,\\dots,K{-}1\\}$。以 Pythia nucleus d0–d5 为例，AUC(3,4)=0.784≥0.75 而 AUC(4,5)=0.683<0.75，按公式 $\\mathrm{EDD}_{0.75}=\\max\\{0,1,2,3\\}=3$。但全文（Abstract、Section 4.3、Table 3、Conclusion）均报告 $\\mathrm{EDD}_{0.75}=4$。对 Table 3 所有行验证发现报告值均比公式计算值大 1：$T=0.65$ 时报告 5（公式得 4），$T=0.80$ 时报告 3（公式得 2）。要么公式需修正为 $\\mathrm{EDD}_T = \\max\\{d^*{+}1 : \\mathrm{AUC}(d^*, d^*{+}1) \\geq T\\}$（即计数可区分的 depth transitions 数量），要么全文数值需下调 1。\n- 为什么影响接收：EDD 是论文四项贡献之一，Abstract/Conclusion 均以 $\\mathrm{EDD}_{0.75}=4$ 作为关键结论。公式与数值不一致直接损害论文的技术可信度。\n- 建议修改方向：明确 EDD 的语义（\"最大可区分深度索引\" vs. \"可区分 transitions 数量\"），修正 Eq. 1 或修正全文报告值，使两者一致。\n\n**N2** [critical] 主实验结果缺乏不确定性量化\n- 具体位置：Table 1 (Section 4.1)、Table 2 (Section 5.1)\n- 问题：Table 1 报告 9 个 cell 的 4-class accuracy，但没有任何一个数值附带标准差或置信区间。论文使用 5-fold CV，完全可以报告 fold-level 标准差。Table 2 的 baseline 比较同样仅报告点估计。唯一有 CI 的是 Figure 2 的 AUC 和 LLM baseline 的 ±6.8pp。\n- 为什么影响接收：ACL ARR reviewer guidelines 明确要求 reproducibility 和 sufficient evidence for claims。在 accuracy 差异仅 0.1pp（RF 78.2% vs. DivEye 78.2%）或几个 pp（RF vs. MLP）时，无法判断差异是否显著。全文无任何 significance test。\n- 建议修改方向：(1) Table 1/2 报告 5-fold CV 的 mean ± std；(2) 对关键比较（RF vs. baselines、cross-transfer 条件间）进行 paired t-test 或 bootstrap significance test；(3) 多次随机种子运行并报告 variance。\n\n**N3** [critical] DCOL 负面结论证据不足\n- 具体位置：Section 5.4\n- 问题：论文称 \"end-to-end models struggle to extract [depth-relevant information] from raw text\"，但仅测试了 1 个架构（RoBERTa-large）、1 个方法框架（DCOL）、6 个配置（其中 5 个因 embedding collapse/OOM/NaN 失败）。6 个配置的具体超参设置未报告。5/6 的失败可能是实现/调参问题而非方法论本身的局限。此外，references.bib 中包含 CLOC (cloc2025) 条目但正文从未引用或讨论为何选择 DCOL 而非 CLOC。\n- 为什么影响接收：这是论文第四项贡献（\"end-to-end learning as negative result\"），但 negative result 需要比 positive result 更强的证据——需要充分的超参搜索、多架构验证，才能排除 \"没调好\" 的解释。当前证据水平不足以支撑 \"统计特征优于端到端学习\" 的结论。\n- 建议修改方向：(1) 报告 6 个配置的完整超参；(2) 至少增加一个额外架构（如 DeBERTa-v3）或方法（如 CLOC）；(3) 弱化结论为 \"初步证据\" 而非确定性断言；(4) 讨论 CLOC 为何未被采用。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Feature importance 分析受 correlated features 影响\n- 具体位置：Section 4.2, Figure 1\n- 问题：19 个特征中，9 个 perplexity statistics 和 3 个 surprisal statistics 存在数学上的强相关（surprisal = -log p，perplexity = exp(mean surprisal)）。Gini importance 会在相关特征间分散，导致单个特征的重要性被低估。论文在 Section 2.3（method.tex line 73）简要承认相关性但称 \"not redundant\"，却未提供定量证据（如相关矩阵、VIF、ablation）。论文的核心发现之一——p90_ppl 和 var_surprisal 的 \"universality\"——直接依赖 Gini importance ranking，而该 ranking 在存在高度相关特征时不可靠。\n- 建议：(1) 提供 19 特征的相关矩阵或 VIF 分析；(2) 使用 permutation importance（对相关特征更鲁棒）替代或补充 Gini importance；(3) 做 feature group ablation（如移除全部 surprisal features 看 accuracy 变化）。\n\n**W2** [warning] Wikipedia seed text 引入的 domain bias 未被量化\n- 具体位置：Section 2.2, Table 1\n- 问题：所有 d0 来自 Wikipedia，而 d1+ 由模型生成。d0 recall >99%（Table 3）可能部分反映 Wikipedia 的文体特征（百科全书式写作、引用密集）而非 \"human vs. machine\" 的深度信号。如果用不同 domain（如新闻、Reddit、学术摘要）作为 seed text，d0 的可分离性和整体 accuracy 可能显著变化。Section 6.1 承认了限制但未做任何定量分析。\n- 建议：至少用 1 个非 Wikipedia domain（如 OpenWebText subset）做 pilot experiment 验证结论的 domain 鲁棒性。\n\n**W3** [warning] LoRA finetuning 参数缺乏 justification\n- 具体位置：Section 2.2（method.tex line 32）\n- 问题：LoRA rank=16, α=32, lr=2e-4, batch=8, epochs=3——这些参数直接决定每轮 finetuning 对模型的修改幅度，进而决定 depth signal 的强度。不同的 LoRA rank 或 learning rate 可能产生完全不同的 degradation trajectory。但论文未提供选择依据，也未做 LoRA 参数的 sensitivity analysis。\n- 建议：至少对 LoRA rank（如 r∈{4, 16, 64}）做 ablation，验证深度信号对 finetuning 强度的敏感性。\n\n**W4** [warning] Zero-shot LLM baseline 的评估样本量严重不足\n- 具体位置：Table 2 脚注（generalization.tex line 33）\n- 问题：DeepSeek V3.2 仅在 200 samples 上评估（50/class），95% CI 为 ±6.8pp（即 33.2%–46.8%），置信区间跨越了 \"接近 chance\" 到 \"明显高于 chance\" 的边界。正文称其 \"reaches only 40%\"，但 CI 下界 33.2% 离 25% chance 并不远。同时，其他方法用 20,000 samples 评估，这种非对称比较使读者难以公平解读。\n- 建议：如果 API cost 是限制，至少增加到 500–1000 samples 使 CI 缩窄到 ±3–4pp；或明确标注这是 preliminary estimate，不宜与其他方法直接比较。\n\n**W5** [warning] 潜在数据泄漏风险未讨论\n- 具体位置：Section 2.2 / Section 4\n- 问题：Generation pipeline 中，$\\mathcal{D}_0$ 是 d1 模型的 training data，$\\mathcal{D}_1$ 是 d2 模型的 training data。5-fold CV 的 split 是在 passage 级别，但未说明是否确保同一 \"generation lineage\"（同一 seed text 及其衍生 passages across depths）全部落在同一 fold。如果某个 d0 passage 在 train fold，而由同一 seed 衍生的 d1 passage 在 test fold，特征可能因内容相似性（而非深度信号）产生关联，导致 accuracy 乐观偏估。\n- 建议：(1) 明确说明 CV split 策略是否考虑了 passage lineage；(2) 如果未考虑，补充 grouped CV（按 seed text 分组）结果以排除泄漏。\n\n**W6** [warning] Cross-strategy transfer 未报告 per-class recall\n- 具体位置：Table 4 (Section 5.3)\n- 问题：Cross-model transfer（Table 3）报告了 per-class recall，揭示了 d2 recall 低至 26.8% 的关键问题。但 cross-strategy transfer（Table 4）仅报告 overall accuracy，无 per-class 信息。考虑到 temperature-induced d1/d2 inversion，cross-strategy 的 per-class recall 分析尤为重要——很可能存在比 cross-model 更严重的 class-level 失败。\n- 建议：补充 Table 4 的 per-class recall，特别是 temperature holdout 条件下。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Section 2.3 称 surprisal variance \"captures second-order structure...that is not redundant with perplexity moments\"，但 perplexity statistics 中已包含 variance。如果指的是 token-level surprisal 分布的方差与 token-level perplexity 分布的方差在数学上不同，应明确说明。\n- **M2**: RF 200 trees 和 binary RF 500 trees 的选择均无 convergence analysis 支撑。一句 \"increased from 200 to 500 trees to ensure convergence\" 不等于 justification——应展示 OOB error vs. n_estimators 曲线或类似证据。\n- **M3**: Section 5.4 提到 DCOL \"v6\" 配置名称，暗示存在 v1–v5，但正文未解释命名或区别。建议系统性报告所有配置。\n- **M4**: Appendix 较薄——仅有 top-k trajectories 一段。建议将 confusion matrices 的完整版（9 cells）、feature correlation matrix、extended depth AUC 原始数据等放入 appendix。\n- **M5**: 全文未提及代码/数据/模型开放计划。ACL ARR review form 包含 reproducibility 评分维度，缺少此信息会直接影响该维度评分。\n- **M6**: references.bib 中 `cloc2025` 条目存在但正文未引用。如果 DCOL 实验参考了 CLOC，应引用并讨论；如果无关，应清理 bib。\n\n---\n\n## 主要优势\n\n- **S1**: 问题定义新颖且有价值。Recursive generation depth estimation 是一个真正的未填补空白——现有工作只做 binary detection 或假设 depth 已知。任务形式化（ordinal classification）合理且清晰。\n- **S2**: 实验设计的系统性。3 model × 3 strategy × 4 depth 的 atlas 结构提供了多维度的 controlled comparison，这比 \"单模型单策略\" 的实验设计强得多。\n- **S3**: Temperature-induced d1/d2 AUC inversion 的发现及其对 cross-strategy deployment 的讨论（Section 5.3, Section 6.1）是实质性的 insight，对实际部署有直接指导价值。\n- **S4**: 对 EDD 的 threshold sensitivity analysis（Table 3）和 granularity ablation 展示了负责任的实验报告态度。\n- **S5**: 论文在 Limitations section（Section 6.2）坦诚地讨论了多项限制（domain bias、reference model overlap、feature fragility、monotonicity assumption violation），这种透明度值得肯定。\n\n---\n\n## Questions for Authors\n\nQ1: Eq. 1 中 EDD 的公式与全文报告值存在系统性 +1 偏差（见 N1）。请确认是公式需修正还是报告值需修正。\n\nQ2: 5-fold CV 的 split 是否考虑了 passage lineage（即同一 seed text 的 d0 passage 及其衍生 d1/d2/d3 passages 是否总在同一 fold）？如果未考虑，是否能补充 grouped CV 结果？\n\nQ3: DCOL 6 个配置的具体超参是什么？为何选择 DCOL 而非 CLOC (Pitawela et al., 2025)？\n\nQ4: 能否提供 19 特征的 Pearson/Spearman 相关矩阵？特别是 perplexity percentiles 与 surprisal statistics 之间的相关系数。\n\nQ5: 是否计划公开代码、数据和训练好的分类器？",
    "reviewer_id": "1",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-15T10:46:32.092752+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3967
}
```

</details>

---


### Assistant

_source line 46 · 2026-05-15T10:46:40.170162+00:00_

Round 1 审稿报告已提交给 Review Director。

核心发现：

1. **EDD 公式 off-by-one 错误**（N1, critical）：Eq. 1 定义与全文报告值系统性差 1，论文四项贡献之一的核心数值不可信
2. **主实验无不确定性量化**（N2, critical）：Table 1/2 无 std/CI，无 significance test，无法判断方法间差异是否显著
3. **DCOL 负面结论证据不足**（N3, critical）：仅 1 架构 6 配置（5 个失败），不足以得出 "端到端学习不如特征工程" 的结论

另有 6 个 should-fix 问题（feature correlation、domain bias、LoRA 参数 justification、LLM baseline 样本量、数据泄漏风险、cross-strategy per-class recall 缺失）和 6 个小问题。

Overall 评分 3/5，建议 Findings track。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1"
}
```

</details>

---


## Round 2

## Round 2

4 recorded events


### User

_source line 47 · 2026-05-15T10:51:09.070336+00:00_

[Round 1 审稿请求]:
## Step 2 — 交叉分享：请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整 Round 1 审稿原文。请对每个 Must-Fix (N1-N2)、Should-Fix (W1-W6) 和关键 Questions 逐条回应：
- **[AGREE]**：同意该观点，并简要说明理由
- **[REBUT]**：反驳该观点，并提供具体证据（引用论文中的 Section/Table/Figure/公式编号）

---

## Reviewer 2 的 Must-Fix 问题

**R2-N1** [critical] DCOL negative result论证严重不足，不能支撑"end-to-end models struggle to extract depth info"的claim
- 仅测试了一个method family（DCOL with RoBERTa-large），6个配置中5个因工程问题失败
- 没有测试更简单的end-to-end baseline（直接finetune RoBERTa做4-class分类等）
- Zero-shot LLM baseline仅200样本
- 结论从一个方法的一次成功run外推到所有end-to-end models，overclaim严重
- 建议至少补充2-3个简单end-to-end baseline，或弱化结论

**R2-N2** [critical] Mohamed et al. (ACL 2025) "LLM as a Broken Telephone" 高度相关但未讨论
- 该论文研究LLM迭代生成中的信息失真，概念上直接相关
- 引用已存在于references.bib (key: mohamed2025_broken_telephone) 但正文从未引用
- 建议在Related Work "Adjacent Tasks"中讨论

## Reviewer 2 的 Should-Fix 问题

**R2-W1** DivEye引用venue错误：bib标注ICLR 2026，实际已从ICLR撤回，发表在TMLR 2026
**R2-W2** 术语不一致：var_surprisal vs var_surp，在不同section使用不同缩写
**R2-W3** Temperature-induced d1/d2 AUC inversion缺乏因果验证——仅测试τ=0.9一个值，无multi-τ ablation
**R2-W4** Limitations section位置不符合ACL模板惯例——应在Conclusion之后作为独立unnumbered section
**R2-W5** 多个bib entry标题被截短（bakshi2026, wang2026, falahati2026）
**R2-W6** 4个orphan bib entries未被引用（cloc2025, dohmatob2024_demystified, dohmatob2024_strong_collapse, mohamed2025_broken_telephone）

## Reviewer 2 的关键 Questions

Q1: 为什么ppl-regression baseline表现为chance level (25.1%)？mean perplexity也应有monotonic trend。
Q2: 是否尝试过更简单的end-to-end approach（如直接finetune RoBERTa-base做4-class classification）？
Q3: "strategy-conditioned classifier"是否有初步实验？
Q4: Mohamed et al. (ACL 2025)为什么在bib中但未被讨论？
Q5: Feature universality是否可能是reference model的artifact？

## Reviewer 2 的新颖性评估要点（供你参考/回应）

- 问题formalization genuinely novel，binary detection和model collapse theory之间的gap被填补
- Atlas "partially" 超越了 grid search — EDD有独立价值，但分析工具（Gini importance, Spearman）都是标准方法
- Feature universality科学价值"中等"——理论上可预期（Shumailov/Dohmatob已预测tail erosion）
- DCOL negative result价值"弱"
- 整体定位为 task formalization + empirical study paper，贡献量处于 Main/Findings borderline

请逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-15T10:52:24.169128+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 交叉回应 — 逐条回应 Reviewer 2 Round 1\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: DCOL negative result 论证严重不足**\n\n完全同意，这与我的 N3 一致。补充几点：\n\n1. R2 指出缺少\"简单 end-to-end baseline（直接 finetune RoBERTa 做 4-class 分类）\"——这一点非常关键。DCOL 是一个 contrastive ordinal learning 框架，本身就比标准 finetune 复杂得多。5/6 的失败（embedding collapse, OOM, NaN）更可能是 DCOL 框架本身的工程复杂性导致，而非 end-to-end learning 的根本局限。如果连最简单的 finetune-RoBERTa-base 都没试过，就下\"end-to-end models struggle\"的结论，逻辑链断裂。\n\n2. 我在 N3 中还指出了 references.bib 包含 `cloc2025` 但正文未讨论的问题。CLOC 是 DCOL 的同类方法（contrastive ordinal learning），也发表在 CVPR 2025，却未被测试或比较，进一步削弱了 negative result 的说服力。\n\n3. 论文 Section 5.4 称 DCOL \"v6\" 达到 64.5%，但 RF 在相同数据上 78.2%。即使 v6 的 64.5% 是真实的，13.7pp 的差距也可能通过更好的超参、更简单的架构、或数据增强来缩小。没有排除这些可能性就下定论是 overclaim。\n\n**[AGREE] R2-N2: Mohamed et al. (ACL 2025) 高度相关但未讨论**\n\n同意。我验证了 `references.bib` 确实包含 `mohamed2025_broken_telephone` 条目（\"LLM as a Broken Telephone: Iterative Generation Distorts Information\", ACL 2025），但正文无任何引用。该论文研究 LLM 迭代生成中的信息失真，与本文的 recursive generation chain 概念直接对应。应在 Related Work 的 \"Adjacent Tasks\" 或 \"Model Collapse Theory\" 段落中讨论，特别是对比其 \"information distortion\" 视角与本文 \"statistical fingerprints\" 视角的异同。\n\n此外，这也反映了一个更广泛的问题：bib 中存在 4 个 orphan entries（R2-W6 指出），说明论文可能经历了较大幅度的修改但未清理引用。\n\n---\n\n### Should-Fix 问题\n\n**[REBUT] R2-W1: DivEye 引用 venue 错误**\n\n我无法独立验证 DivEye 的最终发表 venue。references.bib 中标注为 `booktitle = {Proceedings of ICLR}, year = {2026}`，arXiv ID 为 2509.18880。R2 称其\"已从 ICLR 撤回，发表在 TMLR 2026\"，但我未找到支持此说法的证据。建议 Director 要求 R2 提供来源，或要求作者自行核实。如果确实 venue 有误，这是一个应修复的事实错误，但属于 minor bibliographic issue，不影响论文的技术贡献。\n\n**[AGREE] R2-W2: 术语不一致 var_surprisal vs var_surp**\n\n同意。Section 4.2（atlas.tex line 42）使用 `\\textsc{var\\_surp}`，而 Abstract、Section 1（introduction.tex line 17）、Section 2.3 使用 `\\textsc{var\\_surprisal}`。术语不一致影响可读性，应统一为一个缩写并在首次出现时定义。\n\n**[AGREE] R2-W3: Temperature inversion 缺乏因果验证，仅测试 τ=0.9**\n\n同意。论文对 temperature-induced d1/d2 AUC inversion 的因果解释（\"uniform logit scaling accelerates convergence toward low-entropy attractor\", Section 4.4）虽然理论上合理，但仅在 τ=0.9 一个值上观察到。如果 inversion 是 temperature sampling 的结构性属性，那么在 τ=0.7 或 τ=1.1 上也应该观察到（可能程度不同）。multi-τ ablation（如 τ ∈ {0.7, 0.9, 1.1}）能显著加强因果论证。不过我认为这更接近\"值得做但非必须\"——即使没有 multi-τ ablation，在单一 τ 下的发现仍有报告价值，只需弱化因果表述为 observational finding。\n\n**[AGREE] R2-W4: Limitations section 位置不符合 ACL 模板惯例**\n\n同意。当前 Limitations 作为 Section 6.2 嵌套在 Discussion（Section 6）内。ACL 2023+ 模板要求 Limitations 作为独立 unnumbered section 出现在 Conclusion 之后、References 之前。main.tex 的结构确认了这一点：`\\input{discussion}` 在 `\\input{conclusion}` 之前，而 Limitations 在 discussion.tex 的 Section 6.2 中。这是格式合规问题，应修复。\n\n**[REBUT] R2-W5: 多个 bib entry 标题被截短**\n\n我检查了 references.bib 中 R2 提到的三个条目：\n- `bakshi2026_collapse_improvement`: \"From Collapse to Improvement: Statistical Perspectives on Iterative Training\" — 看起来是完整标题\n- `wang2026_contamination`: \"Can Generative AI Survive Data Contamination? Theoretical Guarantees\" — 看起来是完整标题\n- `falahati2026_curated`: \"Curated Synthetic Data Doesn't Have to Collapse\" — 看起来是完整标题\n\n这些标题与 arXiv 页面的格式一致（通常较短）。我不认为这些是被\"截短\"的。如果 R2 能指出具体哪些标题缺少了哪些内容，可以进一步核实。但基于我的检查，这不构成问题。\n\n**[AGREE] R2-W6: 4 个 orphan bib entries 未被引用**\n\n同意。我在 N3 中已独立发现 `cloc2025` 未被引用的问题。R2 补充了另外 3 个：`dohmatob2024_demystified`、`dohmatob2024_strong_collapse`、`mohamed2025_broken_telephone`。这 4 个 orphan entries 应当被清理或整合到正文中。其中 `mohamed2025_broken_telephone` 应在 Related Work 中讨论（同 R2-N2），`cloc2025` 应在 DCOL 讨论中引用（同我的 N3），`dohmatob2024_demystified` 和 `dohmatob2024_strong_collapse` 如果与现有引用的 Dohmatob 工作不同，也应在 Model Collapse Theory 段落中引用。\n\n---\n\n### 关键 Questions 回应\n\n**R2-Q1: 为什么 ppl-regression baseline 表现为 chance level (25.1%)?**\n\n好问题。Section 4.4（atlas.tex line 116-117）显示 p90_ppl 从 d0 (483.7) → d1 (61.4) → d2 (29.7) → d3 (18.2) 单调递减，说明 mean perplexity 也应有 monotonic trend。但 Table 2 报告 ppl-regression（single feature: mean perplexity）仅 25.1%。可能的解释：(1) mean perplexity 的 inter-class overlap 非常大，即使均值单调递减，分布的重叠使得线性回归无法有效分类——但这需要展示 per-depth distribution plots 来验证；(2) 可能是 mean perplexity 而非 p90_ppl，而 Section 4.2 的 feature importance 分析恰好表明 mean perplexity 的 importance 远低于 p90_ppl。无论如何，论文应该解释这个 counter-intuitive 结果。我同意 R2 认为这需要作者澄清。\n\n**R2-Q2: 是否尝试过更简单的 end-to-end approach?**\n\n同 R2-N1 的立场，我同意这是必须回答的问题。直接 finetune RoBERTa-base 做 4-class classification 是最基本的 end-to-end baseline，成本极低，不尝试就下 negative conclusion 不合理。\n\n**R2-Q3: strategy-conditioned classifier 是否有初步实验?**\n\nSection 6.1 提出 \"strategy-conditioned classifiers are needed\" 但称 \"strategy identification from text remains open\"。如果已经知道 strategy（oracle setting），构建 strategy-conditioned classifier 只是把 Table 1 的 9 个 cell-specific RF 合起来。这实际上就是 Table 1 已经展示的 in-distribution setting（每个 cell 独立训练）。论文可以更明确地把这个 connection 点出来：Table 1 本身就是 oracle strategy-conditioned 的上界。\n\n**R2-Q4: Mohamed et al. 为什么在 bib 中但未被讨论?**\n\n同 R2-N2，已表达同意。\n\n**R2-Q5: Feature universality 是否可能是 reference model 的 artifact?**\n\n这是一个深刻的问题。所有 19 个特征都通过 GPT-2 base (124M) 计算。如果换用完全不同的 reference model（如 Llama-3-1B），feature importance ranking 是否仍然一致？论文 Section 2.2（method.tex line 36-38）承认了 GPT-2 base 与 GPT-2 XL 的 partial architectural overlap，但没有用另一个 reference model 做 robustness check。feature universality 的 \"universal\" 只是 across generation models（Pythia, OLMo, GPT-2 XL），不是 across reference models。这是一个重要区分，论文应明确声明。我在自己的 W1 中从 correlated features 角度质疑了 importance ranking 的可靠性；R2 从 reference model artifact 角度提出了互补的质疑。两个质疑共同削弱了 \"universal depth markers\" 这一 claim 的强度。\n\n---\n\n### 新颖性评估回应\n\n- **问题 formalization genuinely novel**: [AGREE] 这是论文最强的贡献。Binary detection → depth estimation 的升级是实质性的概念进步。\n- **Atlas \"partially\" 超越 grid search**: [AGREE] Atlas 的系统性值得肯定，但分析工具确实是标准方法。EDD 有独立价值，但其公式有 off-by-one 错误（我的 N1），修复后价值仍在。\n- **Feature universality 科学价值\"中等\"**: [AGREE] tail erosion 已被理论预测，实证确认有价值但不 surprising。加上 reference model artifact 的质疑（R2-Q5），\"universal\" 的强度应降级。\n- **DCOL negative result 价值\"弱\"**: [AGREE] 证据不足（我的 N3 = R2-N1），如果补充更多 end-to-end baselines 并仍然失败，价值会显著提升。\n- **整体 Main/Findings borderline**: [AGREE] 我的 Overall 评分 3/5 对应 Findings track acceptance，与 R2 的 borderline 判断一致。如果 N1（EDD 错误）、N2（统计显著性）、N3（DCOL 证据）均修复，有望升至 Main conference level。",
  "reviewer_id": "1",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 交叉回应 — 逐条回应 Reviewer 2 Round 1\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: DCOL negative result 论证严重不足**\n\n完全同意，这与我的 N3 一致。补充几点：\n\n1. R2 指出缺少\"简单 end-to-end baseline（直接 finetune RoBERTa 做 4-class 分类）\"——这一点非常关键。DCOL 是一个 contrastive ordinal learning 框架，本身就比标准 finetune 复杂得多。5/6 的失败（embedding collapse, OOM, NaN）更可能是 DCOL 框架本身的工程复杂性导致，而非 end-to-end learning 的根本局限。如果连最简单的 finetune-RoBERTa-base 都没试过，就下\"end-to-end models struggle\"的结论，逻辑链断裂。\n\n2. 我在 N3 中还指出了 references.bib 包含 `cloc2025` 但正文未讨论的问题。CLOC 是 DCOL 的同类方法（contrastive ordinal learning），也发表在 CVPR 2025，却未被测试或比较，进一步削弱了 negative result 的说服力。\n\n3. 论文 Section 5.4 称 DCOL \"v6\" 达到 64.5%，但 RF 在相同数据上 78.2%。即使 v6 的 64.5% 是真实的，13.7pp 的差距也可能通过更好的超参、更简单的架构、或数据增强来缩小。没有排除这些可能性就下定论是 overclaim。\n\n**[AGREE] R2-N2: Mohamed et al. (ACL 2025) 高度相关但未讨论**\n\n同意。我验证了 `references.bib` 确实包含 `mohamed2025_broken_telephone` 条目（\"LLM as a Broken Telephone: Iterative Generation Distorts Information\", ACL 2025），但正文无任何引用。该论文研究 LLM 迭代生成中的信息失真，与本文的 recursive generation chain 概念直接对应。应在 Related Work 的 \"Adjacent Tasks\" 或 \"Model Collapse Theory\" 段落中讨论，特别是对比其 \"information distortion\" 视角与本文 \"statistical fingerprints\" 视角的异同。\n\n此外，这也反映了一个更广泛的问题：bib 中存在 4 个 orphan entries（R2-W6 指出），说明论文可能经历了较大幅度的修改但未清理引用。\n\n---\n\n### Should-Fix 问题\n\n**[REBUT] R2-W1: DivEye 引用 venue 错误**\n\n我无法独立验证 DivEye 的最终发表 venue。references.bib 中标注为 `booktitle = {Proceedings of ICLR}, year = {2026}`，arXiv ID 为 2509.18880。R2 称其\"已从 ICLR 撤回，发表在 TMLR 2026\"，但我未找到支持此说法的证据。建议 Director 要求 R2 提供来源，或要求作者自行核实。如果确实 venue 有误，这是一个应修复的事实错误，但属于 minor bibliographic issue，不影响论文的技术贡献。\n\n**[AGREE] R2-W2: 术语不一致 var_surprisal vs var_surp**\n\n同意。Section 4.2（atlas.tex line 42）使用 `\\textsc{var\\_surp}`，而 Abstract、Section 1（introduction.tex line 17）、Section 2.3 使用 `\\textsc{var\\_surprisal}`。术语不一致影响可读性，应统一为一个缩写并在首次出现时定义。\n\n**[AGREE] R2-W3: Temperature inversion 缺乏因果验证，仅测试 τ=0.9**\n\n同意。论文对 temperature-induced d1/d2 AUC inversion 的因果解释（\"uniform logit scaling accelerates convergence toward low-entropy attractor\", Section 4.4）虽然理论上合理，但仅在 τ=0.9 一个值上观察到。如果 inversion 是 temperature sampling 的结构性属性，那么在 τ=0.7 或 τ=1.1 上也应该观察到（可能程度不同）。multi-τ ablation（如 τ ∈ {0.7, 0.9, 1.1}）能显著加强因果论证。不过我认为这更接近\"值得做但非必须\"——即使没有 multi-τ ablation，在单一 τ 下的发现仍有报告价值，只需弱化因果表述为 observational finding。\n\n**[AGREE] R2-W4: Limitations section 位置不符合 ACL 模板惯例**\n\n同意。当前 Limitations 作为 Section 6.2 嵌套在 Discussion（Section 6）内。ACL 2023+ 模板要求 Limitations 作为独立 unnumbered section 出现在 Conclusion 之后、References 之前。main.tex 的结构确认了这一点：`\\input{discussion}` 在 `\\input{conclusion}` 之前，而 Limitations 在 discussion.tex 的 Section 6.2 中。这是格式合规问题，应修复。\n\n**[REBUT] R2-W5: 多个 bib entry 标题被截短**\n\n我检查了 references.bib 中 R2 提到的三个条目：\n- `bakshi2026_collapse_improvement`: \"From Collapse to Improvement: Statistical Perspectives on Iterative Training\" — 看起来是完整标题\n- `wang2026_contamination`: \"Can Generative AI Survive Data Contamination? Theoretical Guarantees\" — 看起来是完整标题\n- `falahati2026_curated`: \"Curated Synthetic Data Doesn't Have to Collapse\" — 看起来是完整标题\n\n这些标题与 arXiv 页面的格式一致（通常较短）。我不认为这些是被\"截短\"的。如果 R2 能指出具体哪些标题缺少了哪些内容，可以进一步核实。但基于我的检查，这不构成问题。\n\n**[AGREE] R2-W6: 4 个 orphan bib entries 未被引用**\n\n同意。我在 N3 中已独立发现 `cloc2025` 未被引用的问题。R2 补充了另外 3 个：`dohmatob2024_demystified`、`dohmatob2024_strong_collapse`、`mohamed2025_broken_telephone`。这 4 个 orphan entries 应当被清理或整合到正文中。其中 `mohamed2025_broken_telephone` 应在 Related Work 中讨论（同 R2-N2），`cloc2025` 应在 DCOL 讨论中引用（同我的 N3），`dohmatob2024_demystified` 和 `dohmatob2024_strong_collapse` 如果与现有引用的 Dohmatob 工作不同，也应在 Model Collapse Theory 段落中引用。\n\n---\n\n### 关键 Questions 回应\n\n**R2-Q1: 为什么 ppl-regression baseline 表现为 chance level (25.1%)?**\n\n好问题。Section 4.4（atlas.tex line 116-117）显示 p90_ppl 从 d0 (483.7) → d1 (61.4) → d2 (29.7) → d3 (18.2) 单调递减，说明 mean perplexity 也应有 monotonic trend。但 Table 2 报告 ppl-regression（single feature: mean perplexity）仅 25.1%。可能的解释：(1) mean perplexity 的 inter-class overlap 非常大，即使均值单调递减，分布的重叠使得线性回归无法有效分类——但这需要展示 per-depth distribution plots 来验证；(2) 可能是 mean perplexity 而非 p90_ppl，而 Section 4.2 的 feature importance 分析恰好表明 mean perplexity 的 importance 远低于 p90_ppl。无论如何，论文应该解释这个 counter-intuitive 结果。我同意 R2 认为这需要作者澄清。\n\n**R2-Q2: 是否尝试过更简单的 end-to-end approach?**\n\n同 R2-N1 的立场，我同意这是必须回答的问题。直接 finetune RoBERTa-base 做 4-class classification 是最基本的 end-to-end baseline，成本极低，不尝试就下 negative conclusion 不合理。\n\n**R2-Q3: strategy-conditioned classifier 是否有初步实验?**\n\nSection 6.1 提出 \"strategy-conditioned classifiers are needed\" 但称 \"strategy identification from text remains open\"。如果已经知道 strategy（oracle setting），构建 strategy-conditioned classifier 只是把 Table 1 的 9 个 cell-specific RF 合起来。这实际上就是 Table 1 已经展示的 in-distribution setting（每个 cell 独立训练）。论文可以更明确地把这个 connection 点出来：Table 1 本身就是 oracle strategy-conditioned 的上界。\n\n**R2-Q4: Mohamed et al. 为什么在 bib 中但未被讨论?**\n\n同 R2-N2，已表达同意。\n\n**R2-Q5: Feature universality 是否可能是 reference model 的 artifact?**\n\n这是一个深刻的问题。所有 19 个特征都通过 GPT-2 base (124M) 计算。如果换用完全不同的 reference model（如 Llama-3-1B），feature importance ranking 是否仍然一致？论文 Section 2.2（method.tex line 36-38）承认了 GPT-2 base 与 GPT-2 XL 的 partial architectural overlap，但没有用另一个 reference model 做 robustness check。feature universality 的 \"universal\" 只是 across generation models（Pythia, OLMo, GPT-2 XL），不是 across reference models。这是一个重要区分，论文应明确声明。我在自己的 W1 中从 correlated features 角度质疑了 importance ranking 的可靠性；R2 从 reference model artifact 角度提出了互补的质疑。两个质疑共同削弱了 \"universal depth markers\" 这一 claim 的强度。\n\n---\n\n### 新颖性评估回应\n\n- **问题 formalization genuinely novel**: [AGREE] 这是论文最强的贡献。Binary detection → depth estimation 的升级是实质性的概念进步。\n- **Atlas \"partially\" 超越 grid search**: [AGREE] Atlas 的系统性值得肯定，但分析工具确实是标准方法。EDD 有独立价值，但其公式有 off-by-one 错误（我的 N1），修复后价值仍在。\n- **Feature universality 科学价值\"中等\"**: [AGREE] tail erosion 已被理论预测，实证确认有价值但不 surprising。加上 reference model artifact 的质疑（R2-Q5），\"universal\" 的强度应降级。\n- **DCOL negative result 价值\"弱\"**: [AGREE] 证据不足（我的 N3 = R2-N1），如果补充更多 end-to-end baselines 并仍然失败，价值会显著提升。\n- **整体 Main/Findings borderline**: [AGREE] 我的 Overall 评分 3/5 对应 Findings track acceptance，与 R2 的 borderline 判断一致。如果 N1（EDD 错误）、N2（统计显著性）、N3（DCOL 证据）均修复，有望升至 Main conference level。",
    "reviewer_id": "1",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-15T10:52:28.113090+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3943
}
```

</details>

---


### Assistant

_source line 50 · 2026-05-15T10:52:36.582973+00:00_

交叉回应已提交给 Review Director。总结：

- **Must-Fix**: 两条均 [AGREE]。R2-N1（DCOL 证据不足）与我的 N3 高度一致，R2-N2（Mohamed et al. orphan citation）我独立确认了 bib 中存在但正文未引用的事实。
- **Should-Fix**: 4 条 [AGREE]（W2 术语不一致、W3 缺少 multi-τ ablation、W4 Limitations 位置、W6 orphan bib entries），2 条 [REBUT]（W1 DivEye venue 变更缺乏证据、W5 标题截短我未复现）。
- **Questions**: 均认为合理，特别是 Q1（ppl-regression chance-level 反直觉）和 Q5（feature universality 可能是 reference model artifact）值得作者回应。
- **新颖性定位**: 同意 Main/Findings borderline 的判断，修复关键问题后有望升级。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1"
}
```

</details>

---


## Round 3

## Round 3

48 recorded events


### User

_source line 51 · 2026-05-15T16:06:14.069284+00:00_

[Round 1 审稿请求]:
## 审稿任务分配 — Reviewer 1（Round 1）

### Venue 信息
- **目标会议**：EMNLP 2026 Main Conference（ARR May cycle）
- **截止日期**：2026-05-25
- **页数限制**：Long paper ≤ 8 页正文（参考文献不计页数）
- **模板**：ACL 模板（双栏，11pt）
- **匿名规则**：Double-blind
- **Limitations**：必须在 Conclusion 之后作为 unnumbered section

### 论文文件
- 主文件：`projects/recursive_gen_depth_est/docs/paper/main.tex`
- 子文件：abstract.tex, introduction.tex, related_work.tex, method.tex, atlas.tex, generalization.tex, discussion.tex, conclusion.tex, section_appendix.tex
- 参考文献：references.bib

### 你的审查侧重：方法严谨性 + 实验设计

请重点审查以下方面：

1. **任务形式化**（§2）：recursive generation depth estimation 的定义是否严谨？ordinal classification 框架是否合理？是否有数学错误？
2. **特征设计**（§2.3）：19 维特征的选择是否有充分理由？特征之间是否存在冗余/共线性？是否遗漏了重要特征？
3. **EDD 指标**（§2.4, Eq.1）：定义是否正确？threshold 选择是否合理？sensitivity analysis 是否充分？
4. **Benchmark 构建**（§2.2）：实验设计是否存在混淆变量？数据泄漏风险？样本量是否充足？
5. **统计检验**：所有 claim 是否有充分统计支持（CI、p-value、effect size）？是否有 cherry-picking 嫌疑？
6. **实验方法论**：5-fold CV 是否合理？Random Forest 参数选择依据？baseline 比较是否公平？
7. **Cross-model/strategy transfer**（§5）：实验设计是否能支撑 generalization claim？d1/d2 AUC inversion 的解释是否站得住？
8. **End-to-end learning negative result**（§5.4）：DeBERTa/RoBERTa 结果是否足以支撑"feature-based > end-to-end"结论？feature overlap analysis 方法是否合理？

请以 EMNLP 最严格审稿标准评估，输出完整审稿报告（Summary / Strengths / Weaknesses / Questions / Missing References / Score / Confidence）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 52 · 2026-05-15T16:06:20.867253+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-15T16:06:20.918021+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_1_37084335.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 54 · 2026-05-15T16:06:23.559027+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2"
  }
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-15T16:06:23.609822+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 56 · 2026-05-15T16:06:26.323870+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2"
  }
}
```

</details>

---


### Tool result

_source line 57 · 2026-05-15T16:06:26.429033+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 105
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-15T16:06:31.509520+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
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

_source line 59 · 2026-05-15T16:06:31.560011+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 60 · 2026-05-15T16:06:35.131017+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form criteria 2025 2026 reviewer guidelines scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form criteria 2025 2026 reviewer guidelines scoring"
  }
}
```

</details>

---


### Tool call

_source line 61 · 2026-05-15T16:06:35.986375+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 62 · 2026-05-15T16:06:36.187591+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 63 · 2026-05-15T16:06:36.238408+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 64 · 2026-05-15T16:06:36.289131+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 65 · 2026-05-15T16:06:42.017299+00:00_

Web search results for query: "ACL ARR review form criteria 2025 2026 reviewer guidelines scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"}]

I've found comprehensive information about the ACL Rolling Review (ARR) form criteria and reviewer guidelines for 2025-2026. Here's what I found:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness s
…[truncated 1114 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6886
}
```

</details>

---


### Tool call

_source line 66 · 2026-05-15T16:06:49.054092+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
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

_source line 67 · 2026-05-15T16:06:49.104799+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 68 · 2026-05-15T16:06:49.207050+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 69 · 2026-05-15T16:06:49.207533+00:00_

1	% How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
2	% Target: EMNLP 2026 (ARR May cycle)
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{amsmath}
10	\usepackage{amssymb}
11	\usepackage{multirow}
12	\usepackage{xcolor}
13	\usepackage{subcaption}
14	\usepackage[T1]{fontenc}
15	\usepackage[utf8]{inputenc}
16	\usepackage{microtype}
17	
18	\title{How Deep Is Your Data? Estimating Recursive Generation Depth\\via Statistical Fingerprints}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\input{abstract}
26	
27	\input{introduction}
28	
29	\input{related_work}
30	
31	\input{method}
32	
33	\input{atlas}
34	
35	\input{generalization}
36	
37	\input{discussion}
38	
39	\input{conclusion}
40	
41	\bibliography{references}
42	
43	\appendix
44	\input{section_appendix}
45	
46	\end{document}
47	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 70 · 2026-05-15T16:06:49.308240+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 71 · 2026-05-15T16:06:49.308978+00:00_

1	\begin{abstract}
2	As large language models increasingly train on web text containing their own outputs, a recursive model$\to$data$\to$model loop arises---yet no method estimates how many such iterations a text has undergone.
3	We formalize \emph{recursive generation depth estimation} as ordinal classification and construct a benchmark of 180K passages spanning 3 model families, 3 decoding strategies, and 4 generation depths.
4	From each passage we extract 19 statistical features---perplexity percentiles, surprisal moments, and lexical diversity measures---computed against a fixed reference model (GPT-2 base, 124M).
5	A Random Forest classifier achieves 70--85\% four-class accuracy (chance = 25\%; a zero-shot LLM baseline reaches only 40\%), with 90th-percentile perplexity and surprisal variance emerging as universal depth markers (top-2 importance in 9/9 and 7/9 model--strategy cells, respectively; mean Spearman $\rho{=}0.868$).
6	Our \emph{Depth Degradation Atlas} reveals that decoding strategy reshapes degradation trajectories rather than merely attenuating them, and we define the \emph{Effective Discriminable Depth} (EDD) metric, finding $\mathrm{EDD}_{0.75}{=}4$ for extended recursion chains.
7	Cross-model transfer reaches 66.4\% and cross-strategy transfer 59.1\%, though temperature sampling induces a d1/d2 AUC inversion that z-score normalization cannot resolve.
8	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 72 · 2026-05-15T16:06:49.359532+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 73 · 2026-05-15T16:06:49.360065+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	The text on which large language models are trained increasingly contains their own outputs.
5	As synthetic content proliferates across the web, a recursive loop emerges: models trained on web corpora ingest text generated by earlier models, and their outputs feed into the next generation's training data \cite{shumailov2024_nature,alemohammad2024_mad}.
6	This model$\to$data$\to$model cycle is no longer hypothetical---it is already occurring in the wild---yet we lack the ability to determine how many recursive iterations a given text has undergone, a distinction that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \cite{dohmatob2024_tale_of_tails}.
7	
8	Existing tools address adjacent but distinct problems.
9	Binary detectors such as Binoculars \cite{binoculars2024}, Fast-DetectGPT \cite{fast_detectgpt2024}, and DivEye \cite{diveye2026} classify text as human-written or machine-generated, collapsing all depths $d \geq 1$ into a single category.
10	Watermarking \cite{kirchenbauer2023_watermark} requires proactive embedding and cannot be applied retroactively.
11	The model collapse literature \cite{shumailov2024_nature,dohmatob2024_tale_of_tails} assumes depth is known a priori; \citet{drayson2025_detection_prevents_collapse} filter synthetic data via binary detection without distinguishing depths.
12	No existing method estimates the ordinal recursive generation depth of a text passage from its content alone.
13	
14	Our key insight is that recursive generation leaves quantifiable statistical fingerprints in text, and these fingerprints exhibit universal stability across model families and decoding strategies.
15	Specifically, perplexity tail statistics---the 90th-percentile perplexity (\textsc{p90\_ppl}) and surprisal variance (\textsc{var\_surprisal})---emerge as dominant depth indic
…[truncated 2953 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 74 · 2026-05-15T16:06:49.360384+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 75 · 2026-05-15T16:06:49.360698+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Model Collapse Theory.}
5	\citet{shumailov2024_nature} demonstrate that recursively training language models on their own outputs erodes distributional tails, eventually collapsing the output distribution to a narrow mode.
6	\citet{dohmatob2024_tale_of_tails} formalize this phenomenon through scaling laws that distinguish tail \emph{narrowing} (reduced variance) from tail \emph{cutting} (lost support), showing both accelerate with generation depth; \citet{dohmatob2024_strong_collapse} establish strong collapse guarantees, and \citet{dohmatob2024_demystified} analyze the regression case.
7	The MAD framework \cite{alemohammad2024_mad} extends this analysis to self-consuming generative models and quantifies the precision--recall tradeoff as synthetic data accumulates across generations.
8	Mitigation strategies include retaining real data \cite{gerstgrasser2024_accumulate} and filtering synthetic samples via detection \cite{drayson2025_detection_prevents_collapse}.
9	Recent work identifies non-monotonic dynamics \cite{bakshi2026_collapse_improvement}, fixed-point convergence \cite{marchi2024_heat_death}, contamination bounds \cite{wang2026_contamination}, curated pipelines \cite{falahati2026_curated}, knowledge collapse \cite{knowledge_collapse2025}, spectral signatures \cite{sigma2026_spectral}, and self-improving loops \cite{synthetic_eggs2026}.
10	These works characterize degradation patterns but assume the generation depth is known a priori; our work addresses the inverse problem of estimating depth from text alone.
11	
12	\paragraph{AI Text Detection.}
13	DetectGPT \cite{mitchell2023_detectgpt} introduced probability curvature---the tendency of model-generated text to occupy local maxima of the log-probability surface---as a zero-shot detection signal.
14	\citet{fast_detectgpt2024} improve computational efficiency by replacing random perturbations with conditional probability curvature from a surrogate 
…[truncated 3207 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 76 · 2026-05-15T16:06:49.461355+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 77 · 2026-05-15T16:06:49.662691+00:00_

1	\section{Task Formulation}
2	\label{sec:method}
3	
4	\subsection{Problem Definition}
5	\label{sec:method:problem}
6	
7	Let $f_\theta$ denote a language model and $\mathcal{D}_0$ a corpus of human-written seed text.
8	We define a \emph{recursive generation chain} of depth $K$ as the sequence $\mathcal{D}_0, \mathcal{D}_1, \dots, \mathcal{D}_K$, where each $\mathcal{D}_k$ ($k \geq 1$) is produced by finetuning $f_\theta$ on $\mathcal{D}_{k-1}$ and sampling from the resulting model.
9	Depth $d{=}0$ denotes human-written text; depth $d{=}k$ ($k \geq 1$) denotes text generated by a model trained on depth-$(k{-}1)$ data.
10	
11	Given a text passage $x$, the task is to estimate its recursive generation depth $d \in \{0, 1, \dots, K\}$.
12	This is an ordinal classification problem: depths carry a natural ordering, and $d{=}1$ is structurally closer to $d{=}0$ than $d{=}3$ is, since each generation step compounds distributional drift.
13	
14	\subsection{Multi-Generational Benchmark Construction}
15	\label{sec:method:benchmark}
16	
17	We construct a benchmark spanning three axes: model family, decoding strategy, and generation depth.
18	
19	\paragraph{Model families.}
20	We select three 1--1.5B-parameter models with diverse pretraining corpora and architectures: Pythia-1.4B (EleutherAI), OLMo-1B (AI2), and GPT-2~XL (OpenAI, 1.5B).
21	Restricting to a narrow parameter range isolates the effect of architecture and training data from scale.
22	
23	\paragraph{Decoding strategies.}
24	Each model is paired with three decoding strategies: nucleus sampling ($p{=}0.95$) \cite{holtzman2020_nucleus}, temperature sampling ($\tau{=}0.9$), and top-$k$ sampling ($k{=}50$).
25	These span the dominant modes of open-ended generation and induce qualitatively different entropy profiles.
26	
27	\paragraph{Depth and scale.}
28	The primary benchmark covers depths d0--d3 across all $3 \times 3 = 9$ model--strategy cells, with 5{,}000 samples per depth per cell (180K samples total).
29	For depth ex
…[truncated 5766 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 78 · 2026-05-15T16:06:49.663233+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
  }
}
```

</details>

---


### Tool result

_source line 79 · 2026-05-15T16:06:50.115288+00:00_

1	\section{The Depth Degradation Atlas}
2	\label{sec:atlas}
3	
4	We systematically characterize how recursive generation reshapes the statistical profile of text across a grid of 3 model families $\times$ 3 decoding strategies $\times$ 4 generation depths (d0--d3), yielding 9 experimental configurations each spanning 4 depths.
5	For each cell we train a Random Forest (RF) classifier on the 19 statistical features defined in \S\ref{sec:method} and examine (i)~in-distribution depth classification accuracy, (ii)~which features carry depth signal, (iii)~how far into the recursion chain depth remains discriminable, and (iv)~how decoding strategy modulates the degradation trajectory.
6	
7	\subsection{In-Distribution Performance}
8	\label{sec:atlas:indist}
9	
10	Table~\ref{tab:main_matrix} reports 4-class depth estimation accuracy under 5-fold cross-validation.
11	All 9 cells exceed chance (25\%) by a wide margin, with accuracy ranging from 69.6\% to 85.4\%.
12	Both model family and decoding strategy influence accuracy, with model ordering GPT-2~XL $>$ OLMo $>$ Pythia holding across all strategies.
13	Top-$k$ ($k{=}50$) trails by 6--9 percentage points, while temperature and nucleus sampling alternate for the lead depending on model family.
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\caption{In-distribution 4-class depth estimation accuracy (\%) across 3 model families $\times$ 3 decoding strategies. RF classifier with 19 statistical features, 5-fold CV (std 0.2--0.9pp across all cells). Chance = 25\%.}
19	\label{tab:main_matrix}
20	\begin{tabular}{lccc}
21	\toprule
22	Model & Nucleus & Temp & Top-$k$ \\
23	 & $p{=}0.95$ & $\tau{=}0.9$ & $k{=}50$ \\
24	\midrule
25	Pythia-1.4B & 78.2 & 76.3 & 69.6 \\
26	OLMo-1B & 78.8 & 82.0 & 74.2 \\
27	GPT-2 XL & 83.3 & \textbf{85.4} & 76.6 \\
28	\bottomrule
29	\end{tabular}
30	\end{table}
31	
32	Because the human-written seed text (d0) is often trivially separable from any machine-generated depth, we also evaluate 3-class accurac
…[truncated 11678 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 80 · 2026-05-15T16:06:50.115833+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
  }
}
```

</details>

---


### Tool result

_source line 81 · 2026-05-15T16:06:50.619757+00:00_

1	\section{Generalization and Robustness}
2	\label{sec:generalization}
3	
4	We test whether the atlas results (69.6--85.4\%) reflect genuine statistical regularities or training artifacts, evaluating four axes: classifier choice (\S\ref{sec:gen:baselines}), cross-model transfer (\S\ref{sec:gen:crossmodel}), cross-strategy transfer (\S\ref{sec:gen:crossstrategy}), and end-to-end learning (\S\ref{sec:gen:dcol}).
5	
6	\subsection{Baseline Comparison}
7	\label{sec:gen:baselines}
8	
9	Table~\ref{tab:baselines} compares classification methods on the Pythia-1.4B nucleus setting.
10	Three feature-based methods---Random Forest (RF), CORAL ordinal regression \cite{coral2020}, and DivEye \cite{diveye2026}---all operate on the same 19 statistical features and achieve statistically indistinguishable accuracy (78.1--78.2\%; pairwise bootstrap $p>0.05$ after Bonferroni correction, 95\% CI within $\pm$1.1pp).
11	These three significantly outperform CE-MLP ($p<0.001$, $+$3.8pp), which in turn trails logistic regression by $\sim$0.1pp.
12	Single-feature regression on mean perplexity performs at chance (25.1\%), confirming that depth estimation requires the multi-dimensional feature representation defined in \S\ref{sec:method}.
13	
14	\begin{table}[t]
15	\centering
16	\small
17	\caption{Comparison of classification methods on Pythia-1.4B nucleus. RF, CORAL, and DivEye use the same 19 statistical features and are statistically indistinguishable (bootstrap $p>0.05$, Bonferroni-corrected). Chance = 25\%. 5-fold CV std: 0.2--0.9pp across all methods.}
18	\label{tab:baselines}
19	\begin{tabular}{lc}
20	\toprule
21	Method & 4-class Acc (\%) \\
22	\midrule
23	RF (19 features) & 78.2 \\
24	CORAL & 78.1 \\
25	DivEye & 78.2 \\
26	CE-MLP & 74.9 \\
27	LR & 75.0 \\
28	DeepSeek V3.2 (zero-shot)\footnotemark & 40.0 \\
29	ppl-regression (single feature) & 25.1 \\
30	\bottomrule
31	\end{tabular}
32	\footnotetext{Evaluated on 200 samples (approximately 50 per class) from the Pythia-1.4B nucleus cell on
…[truncated 5299 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 82 · 2026-05-15T16:06:50.720544+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 83 · 2026-05-15T16:06:51.072214+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Depth-graduated data curation.}
5	Predicted depth can serve as a continuous quality proxy for importance weighting in curation pipelines \cite{dsir2023,qurating2024}, retaining shallow-generation text while down-weighting deeply recursive samples that binary filters \cite{drayson2025_detection_prevents_collapse} would indiscriminately discard.
6	
7	\paragraph{Deployment considerations.}
8	The temperature-induced d1/d2 AUC inversion (\S\ref{sec:gen:crossstrategy}) means deploying without knowing the target decoding strategy risks systematic prediction reversals; strategy-conditioned classifiers or automatic strategy identification are needed.
9	
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 84 · 2026-05-15T16:06:51.072562+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 85 · 2026-05-15T16:06:51.976320+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced recursive generation depth estimation and showed that 19 lightweight statistical features---with p90 perplexity and surprisal variance as universal markers---achieve 70--85\% four-class accuracy (chance = 25\%) with $\mathrm{EDD}_{0.75}{=}4$.
5	Cross-model transfer reaches 66.4\% and cross-strategy 59.1\%, though the temperature-induced d1/d2 inversion and PLMs' ${\sim}$59\% ceiling underscore remaining challenges; future work should address wild-data transfer, larger scales, and strategy-conditioned classifiers.
6	Code and data will be released upon acceptance.
7	
8	\section*{Limitations}
9	\label{sec:limitations}
10	
11	\paragraph{Cross-strategy deployment constraint.}
12	Deploying depth estimators across decoding strategies requires knowing the target strategy type a priori.
13	Without this knowledge, d1/d2 predictions may systematically invert: cross-strategy holdout d1v2 AUC drops to 0.129 (GPT-2~XL) and 0.253 (OLMo) when temperature-sampled text is classified by a model trained on nucleus and top-$k$ (\S\ref{sec:gen:crossstrategy}).
14	Strategy-conditioned classifiers or automatic strategy identification are needed before deployment.
15	
16	\paragraph{d0 inflation of headline metrics.}
17	Depth~0 (human-written text) is near-perfectly separable (recall $>$98\% across all settings), inflating headline accuracy.
18	Cross-model transfer accuracy of 66.4\% is substantially driven by d0; d2 recall drops to 26.8\% in the worst case (Pythia holdout).
19	
20	\paragraph{Controlled vs.\ ecological setting.}
21	All experiments use Wikipedia seed text with controlled recursive generation (LoRA fine-tuning, 1--1.5B parameter models).
22	Transfer to mixed-domain corpora, instruction-tuned models, and larger scales (7B+) remains open.
23	Wild-data calibration is probed only indirectly; ecological transfer is future work.
24	
25	\paragraph{EDD threshold sensitivity.}
26	The Effective Discriminable Depth depend
…[truncated 1107 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 86 · 2026-05-15T16:06:52.077047+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-15T16:06:52.127869+00:00_

1	\section{Additional Results}
2	\label{app:additional}
3	
4	\subsection{Top-$k$ Feature Trajectories}
5	\label{app:topk_trajectories}
6	
7	Figure~\ref{fig:feature_trajectory} in the main text shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\tau{=}0.9$) sampling.
8	Top-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \S\ref{sec:atlas:trajectories}.
9	Concretely, the d0$\to$d1 drop in \textsc{p90\_ppl} under top-$k$ is 78\% (vs.\ 87\% for nucleus), and the d2$\to$d3 reduction is 31\% (vs.\ 39\% for nucleus).
10	Despite the magnitude reduction, feature rank ordering across depths is preserved, which explains why ordinal classifiers maintain directionality even under top-$k$ conditions.
11	
12	\subsection{Permutation Importance}
13	\label{app:permutation}
14	
15	To verify that the Gini-based importance rankings in \S\ref{sec:atlas:features} are not an artifact of the impurity measure, we compute permutation importance (5-fold CV, 10 repeats) for all 9 atlas cells.
16	Results are highly consistent: \textsc{p90\_ppl} ranks in the top 2 in 9/9 cells under both measures, and \textsc{var\_surprisal} in 8/9 (vs.\ 7/9 for Gini, with the additional cell being OLMo top-$k$).
17	The mean Spearman rank correlation between Gini and permutation importance vectors across all 9 cells is $\rho{=}0.94$, confirming that the reported feature universality is robust to the choice of importance measure.
18	
19	\subsection{DCOL Iteration Details}
20	\label{app:dcol_iterations}
21	
22	Table~\ref{tab:dcol_iterations} summarizes all six DCOL iterations.
23	DeBERTa-v3-large exhibited systematic numerical instability across five configurations; RoBERTa-large resolved stability but could not close the accuracy gap with feature-based methods.
24	
25	\begin{table}[h]
26	\centering
27	\small
28	\caption{DCOL iteration summary. All experim
…[truncated 1689 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 88 · 2026-05-15T16:06:52.128286+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 89 · 2026-05-15T16:06:52.178907+00:00_

1	% ============================================================
2	% Model Collapse Theory
3	% ============================================================
4	
5	@article{shumailov2024_nature,
6	  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
7	  title     = {{AI models collapse when trained on recursively generated data}},
8	  journal   = {Nature},
9	  volume    = {631},
10	  pages     = {755--759},
11	  year      = {2024},
12	  doi       = {10.1038/s41586-024-07566-y},
13	}
14	
15	@inproceedings{dohmatob2024_tale_of_tails,
16	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia},
17	  title     = {{A Tale of Tails: Model Collapse as a Change of Scaling Laws}},
18	  booktitle = {Proceedings of ICML},
19	  year      = {2024},
20	  note      = {arXiv:2402.07043},
21	  url       = {https://arxiv.org/abs/2402.07043},
22	}
23	
24	@inproceedings{dohmatob2024_strong_collapse,
25	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
26	  title     = {{Strong Model Collapse}},
27	  booktitle = {Proceedings of ICLR},
28	  year      = {2024},
29	  note      = {arXiv:2410.04840},
30	  url       = {https://arxiv.org/abs/2410.04840},
31	}
32	
33	@inproceedings{dohmatob2024_demystified,
34	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia},
35	  title     = {{Model Collapse Demystified: The Case of Regression}},
36	  booktitle = {Proceedings of NeurIPS},
37	  year      = {2024},
38	  note      = {arXiv:2402.07712},
39	  url       = {https://arxiv.org/abs/2402.07712},
40	}
41	
42	@inproceedings{alemohammad2024_mad,
43	  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Hossain, Hossein and Romero, Oscar and Ramanarayanan, Sriram and Baraniuk, Richard G.},
44	  title     = {{Self-Consuming Generative Models Go MAD}},
45	  booktitle = {Proceedings of I
…[truncated 14605 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 90 · 2026-05-15T16:07:00.625855+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scale ranges, and descriptions. Include soundness, excitement, overall recommendation, confidence, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scale ranges, and descriptions. Include soundness, excitement, overall recommendation, confidence, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 91 · 2026-05-15T16:07:01.882006+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the key reviewer guidelines: what reviewers should focus on, how to evaluate papers, any specific criteria for soundness, novelty, experiments, reproducibility. Include any scoring rubrics or decision criteria."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the key reviewer guidelines: what reviewers should focus on, how to evaluate papers, any specific criteria for soundness, novelty, experiments, reproducibility. Include any scoring rubrics or decision criteria."
  }
}
```

</details>

---


### Tool result

_source line 92 · 2026-05-15T16:07:08.307230+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- 5: Positive evaluation is correct; careful reading and familiar with related work
- 4: Quite sure; important points checked carefully
- 3: Pretty sure; good area familiarity but didn't carefully check details
- 2: Can defend evaluation but likely missed details or novelty unclear
- 1: Outside expertise area or paper very difficult to understand

## 2. **Soundness**
Scale: 1-5 (with .5 increments)
- 5: Most thorough study of its type
- 4: Sufficient support for claims; extra experiments optional
- 3: Adequate support for main claims; minor details need work
- 2: Main claims lack support; major technical/methodological problems
- 1: Insufficient rigor for publication or not ACL-relevant

## 3. **Excitement**
Scale: 1-5 (with .5 increments)
- 5: Highly Exciting; would recommend to others
- 4: Exciting; would mention to others
- 3: Interesting; might mention points or attend presentation
- 2: Potentially Interesting; doesn't resonate personally
- 1: Not Exciting; lacks community resonance or linguistic relevance

## 4. **Overall Assessment**
Scale: 1-5 (with .5 increments)
- 5: Award consideration (top 2.5%)
- 4: Conference acceptance
- 3: Findings acceptance
- 2: Substantial revisions needed by next cycle
- 1.5: Major revisions required beyond next cycle
- 1: Reject or non-relevant

## 5. **Reproducibility**
Scale: 1-5
- 5: Results easily reproducible
- 4: Mostly reproducible with minor variations
- 3: Reproducible with difficulty; underspecified parameters
- 2: Very difficult; unavailable data or insufficient details
- 1: Impossible to reproduce

## 6. **Datasets Value**
Scale: 1-5
- 5: Enabling; affects research direction choices
- 4: Useful; recommended for ongoing work
- 3: Potentially useful for some research
- 2: Documentary; useful for replication primarily
- 1: No usable datasets submitted

## 7. **Software Value**
Scale: 1-5 (same ratings as Datasets)

## 8. **A
…[truncated 245 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7681
}
```

</details>

---


### Tool result

_source line 93 · 2026-05-15T16:07:12.782270+00:00_

# ARR Reviewer Guidelines: Key Focus Areas

## Core Reviewing Tasks

Reviewers should complete four main tasks:
1. **Allocate time** for both reviewing and discussion periods
2. **Check assignments** for expertise fit and conflicts of interest
3. **Write strong reviews** following structured guidance
4. **Update assessments** based on author responses and peer discussion

## Evaluation Framework

### Reading Strategy
Reviewers must read papers twice: first for skimming to understand research questions and methodology scope, then for in-depth technical evaluation. This prevents confirmation bias and hindsight bias from distorting judgment.

### Three-Part Scoring System (as of February 2025)
- **Soundness**: Technical correctness and validity
- **Excitement**: Personal interest (orthogonal to soundness)
- **Overall Recommendation**: Composite assessment reflecting soundness, excitement, novelty, and impact

### Specificity Requirement
Reviews must provide concrete details rather than vague criticism. For example: "The paper misses references X, Y, Z" rather than "missing relevant references."

## Common Problematic Review Patterns (H-Series)

Reviewers should scrutinize whether they're making these mistakes:

- **H1-H4**: Dismissing findings as obvious, contradicting expectations, or lacking precedent
- **H5**: Rejecting papers without SOTA results (not required for scientific contribution)
- **H6**: Penalizing negative results (valuable for combating publication bias)
- **H7-H8**: Demanding unnecessary complexity or specific methodologies
- **H13**: Requiring extra experiments beyond what supports stated claims

## NLP-Specific Paper Issues to Flag

**Methodology (M-series)**:
- M1: LLM evaluators lack validation for their context
- M2: Insufficient reproducibility details or code availability
- M3: Undisclosed data quality problems
- M4: Unmotivated model/benchmark selection
- M5: Incomplete proof assumptions

**Results (R-series)**:
- R1: Statistical issues or p-h
…[truncated 1163 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 10900
}
```

</details>

---


### Tool call

_source line 94 · 2026-05-15T16:08:46.493030+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 95 · 2026-05-15T16:09:15.497029+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 38, \"total_citations\": 59, \"unique_cited_keys\": 38, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 33, \"online_not_found\": 3, \"online_mismatch\": 2}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"shumailov2024_nature\", \"type\": \"article\", \"title\": \"AI models collapse when trained on recursively generated data\", \"authors\": \"Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and ...\", \"year\": \"2024\", \"venue\": \"Nature\"}, {\"key\": \"dohmatob2024_tale_of_tails\", \"type\": \"inproceedings\", \"title\": \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, ...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICML\"}, {\"key\": \"dohmatob2024_strong_collapse\", \"type\": \"inproceedings\", \"title\": \"Strong Model Collapse\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\", \"year\": \"2024\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"dohmatob2024_demystified\", \"type\": \"inproceedings\", \"title\": \"Model Collapse Demystified: The Case of Regression\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia\", \"year\": \"2024\", \"venue\": \"Proceedings of NeurIPS\"}, {\"key\": \"alemohammad2024_mad\", \"type\": \"inproceedings\", \"title\": \"Self-Consuming Generative Models Go MAD\", \"authors\": \"Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahme...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"gerstgrasser2024_accumulate\", \"type\": \"misc\", \"title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"authors\": \"Gerstgrasser, Matt
…[truncated 28829 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 29003
}
```

</details>

---


### Tool call

_source line 96 · 2026-05-15T16:11:37.535152+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — Round 1 完整审稿报告\n\n### 审查侧重：方法严谨性 + 实验设计\n\n---\n\n## 总体评分\n**Overall**: 3 / 5（Findings acceptance）\n**一句话总结**: 任务形式化有价值、实验系统性强，但 EDD 定义存在数学缺陷、特征共线性分析缺失、end-to-end 对比方法论有硬伤，距主会接收尚有距离。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3 / 5 | 核心管线合理但 EDD 定义有数学漏洞；特征冗余未量化；end-to-end 对比依赖不可靠的 attention-importance 相关性 |\n| Excitement | 3.5 / 5 | 新任务定义填补了 binary detection 与 model collapse 之间的空白；Depth Degradation Atlas 设计系统；但受限于 controlled setting，实际部署价值待验证 |\n| Reproducibility | 4 / 5 | 模型、超参、数据规模均有详细说明；LoRA target 按架构区分；代码承诺 upon acceptance 发布 |\n| Datasets Value | 4 / 5 | 180K 样本 × 9 cells 的 benchmark 对后续研究有较高价值 |\n| Software Value | 2 / 5 | 未提交代码 |\n| Confidence | 4 / 5 | 熟悉 model collapse、AI text detection 和 ordinal classification 文献；仔细核验了统计检验和 EDD 定义 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] EDD 定义存在数学缺陷——max 算子不要求连续可判别性\n- 具体位置：§2.4, Eq. 1\n- 问题：当前定义 EDD_T = max{d*+1 : AUC(d*, d*+1) >= T} 取满足阈值的最大 d*，但不要求所有 d' <= d* 的 pair 都满足阈值。如果 AUC(d1,d2) < T 而 AUC(d3,d4) >= T，EDD 会报告误导性的高值。论文实验中 AUC 恰好单调衰减所以没暴露问题，但 §4.3 跨策略 transfer 的 d1/d2 AUC inversion（GPT-2 XL: 0.129）说明非单调情况在这个任务中确实存在。正确定义应为 EDD_T = max{d*+1 : ∀ d' <= d*, AUC(d', d'+1) >= T}。\n- 为什么影响接收：EDD 是论文的核心 contribution 之一，定义缺陷直接影响 metric 的可信度和可复用性。\n- 建议修改方向：修改 Eq. 1 为连续版本；在 Limitations 讨论 cross-strategy 场景下 EDD 的适用边界。\n\n**N2** [critical] 19 维特征的共线性未量化，\"19 features are needed\" 的 claim 缺乏消融支持\n- 具体位置：§2.3 (Table 1), §4.1 (Table 3)\n- 问题：12/19 特征（9 perplexity + 3 surprisal）来自同一 reference model 的 token-level 分布，必然高度相关。论文承认 \"surprisal variance captures second-order structure...not redundant with perplexity moments\"（§2.3），但没提供任何量化证据（VIF、相关矩阵、条件数）。唯一的消融是 single-feature regression（mean_ppl → 25.1%, Table 3），但直接跳到全部 19 特征。缺少中间消融：仅用 top-2 特征（p90_ppl + var_surprisal）能达到多少？仅用 4 类 category 之一的特征呢？这一消融对 \"19 features are needed\"（§4.1）和 \"multi-dimensional feature representation\" 的 claim 至关重要。\n- 为什么影响接收：无法判断信号到底来自几个独立维度，feature universality 的论述因此缺乏坚实基础。\n- 建议修改方向：报告特征相关矩阵；做 top-2 / top-5 / per-category 消融；如果 2-3 个特征即可接近 78%，则需调整 contribution 表述。\n\n**N3** [critical] End-to-end 对比中 attention-importance 相关性方法论有缺陷\n- 具体位置：§4.4, Appendix D\n- 问题：论文用 DeBERTa/RoBERTa 的 attention weight 与 RF permutation importance 做 Spearman 相关（ρ = −0.484 / −0.456），得出 \"complementary representations\" 结论。但 attention weight 不是模型使用某信息的可靠指标——这一点在 attention interpretation 文献中已被广泛讨论（Jain & Wallace, NAACL 2019; Wiegreffe & Pinter, EMNLP 2019 等）。attention 和 feature importance 度量的对象本质不同（token-level attention vs. feature-level importance），负相关可能是 scale mismatch 的 artifact。此外，end-to-end 实验仅在 Pythia nucleus 一个 pipeline 上做，DeBERTa std = ±4.7% 很大，DCOL 6 次迭代中 5 次失败。\n- 为什么影响接收：这是 Contribution 4 的核心证据。如果 attention-importance 相关性不可靠，\"feature-based > end-to-end\" 的机制解释就站不住。\n- 建议修改方向：改用 probing classifier、SHAP/integrated gradients 等更可靠的方法分析 PLM 表征；至少在 2-3 个 pipeline 上复现 end-to-end 结果；单独报告 DCOL 失败原因分析。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] d0 recall >98% 严重膨胀 headline accuracy，应以 d1–d3 accuracy 为主指标\n- 具体位置：§3.1 (Table 2), §4.2 (Table 4), Limitations\n- 问题：d0 是 Wikipedia 原文，与 model-generated text 的分离本质上是 domain classification 而非 depth estimation。论文在 Limitations 中承认了 \"d0 inflation\"，也在 §3.1 报告了 3-class accuracy（排除 d0），但 abstract 和 Introduction 仍以 \"70–85% four-class accuracy\" 为 headline。Cross-model transfer 66.4% 中 d0 recall 为 99.3%，而 d2 recall 最低只有 26.8%（Table 4, Pythia holdout）。\n- 建议：将 d1–d3 3-class accuracy 提升为主指标（或至少并列报告），在 abstract 中明确说明 d0 包含/不包含的区别。\n\n**W2** [warning] \"geometry-level shift\" overclaim——仅凭 z-score normalization 失败\n- 具体位置：§4.3\n- 问题：论文称 z-score normalization 不能解决 d1/d2 inversion，因此确认 \"genuine geometry-level shift rather than a correctable scale difference\"。但 z-score 是最简单的 domain adaptation 方法。论文引用了 Sugiyama et al. (2007) 的 importance weighting，却没尝试。没测试 more sophisticated methods（CORAL domain adaptation、moment matching、adversarial alignment）就下结论，推理跳步太大。\n- 建议：要么至少测试 2-3 种 domain adaptation 方法，要么将结论弱化为 \"z-score normalization is insufficient\"。\n\n**W3** [warning] Table 4, 5 中暴露 experiment ID 可能违反 double-blind\n- 具体位置：Table 4 caption, Table 5 caption\n- 问题：Experiment tracking ID（如 depth_extension_binary_pairwise_002、depth_extension_gpt2xl_d4d5_001）出现在表格 caption 中，暗示使用了特定实验管理系统。这在 double-blind review 中不常见，可能帮助追踪到作者团队的实验基础设施。\n- 建议：删除 experiment ID 或移至匿名化的 supplementary material。\n\n**W4** [warning] DeepSeek V3.2 zero-shot baseline 统计力度不足\n- 具体位置：§4.1 (Table 3, footnote)\n- 问题：仅 200 样本（~50/class），95% CI ±6.8pp，真实值可能在 33.2%–46.8% 范围内。这个 baseline 在 abstract 中被突出使用，但置信区间跨度太大。\n- 建议：增加到至少 1000 样本使 CI 收窄到 ±3pp 以内，或在 abstract 中改为 \"approximately 40% (±6.8pp)\"。\n\n**W5** [warning] 缺少 gradient boosting baseline\n- 具体位置：§4.1 (Table 3)\n- 问题：在 tabular/feature-based classification 中，XGBoost/LightGBM 通常是最强 baseline，但论文缺少此类比较。\n- 建议：加入 XGBoost/LightGBM；如果精度与 RF 一致，则进一步强化 \"signal in features\" 的论点。\n\n---\n\n## 小问题（不影响接收）\n\n- §2.2 \"standard LoRA hyperparameters\" 表述不严谨，建议改为 \"commonly used\"\n- Table 2 caption 报告 \"std 0.2–0.9pp across all cells\" 但没给每个 cell 的具体 CI\n- 引用：knowledge_collapse2025 和 falahati2026_curated 在 OpenAlex 中未找到（可能是索引延迟），alemohammad2024_mad 的 first author 与 API 记录不一致\n- Discussion（§5）仅 2 段，过于简短，缺少 calibration 讨论\n\n---\n\n## 主要优势\n\n- **新任务定义填补真实空白**：在 binary detection 和 model collapse theory 之间建立了 ordinal depth estimation 这一中间层，动机清晰且有实际意义\n- **系统性 Atlas 实验设计**：3 × 3 grid 覆盖 model family 和 decoding strategy 两个轴，每个 cell 报告完整指标\n- **诚实的 Limitations 讨论**：d0 inflation、cross-strategy weakness、EDD threshold sensitivity、reference model dependency 均有明确承认\n- **统计实践总体良好**：bootstrap CI、permutation test、Bonferroni correction、独立 binary classifier 避免 boundary dilution\n- **Feature universality 发现有启发性**：p90_ppl 在 9/9 cells top-2、mean Spearman ρ=0.868",
  "reviewer_id": "1",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — Round 1 完整审稿报告\n\n### 审查侧重：方法严谨性 + 实验设计\n\n---\n\n## 总体评分\n**Overall**: 3 / 5（Findings acceptance）\n**一句话总结**: 任务形式化有价值、实验系统性强，但 EDD 定义存在数学缺陷、特征共线性分析缺失、end-to-end 对比方法论有硬伤，距主会接收尚有距离。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3 / 5 | 核心管线合理但 EDD 定义有数学漏洞；特征冗余未量化；end-to-end 对比依赖不可靠的 attention-importance 相关性 |\n| Excitement | 3.5 / 5 | 新任务定义填补了 binary detection 与 model collapse 之间的空白；Depth Degradation Atlas 设计系统；但受限于 controlled setting，实际部署价值待验证 |\n| Reproducibility | 4 / 5 | 模型、超参、数据规模均有详细说明；LoRA target 按架构区分；代码承诺 upon acceptance 发布 |\n| Datasets Value | 4 / 5 | 180K 样本 × 9 cells 的 benchmark 对后续研究有较高价值 |\n| Software Value | 2 / 5 | 未提交代码 |\n| Confidence | 4 / 5 | 熟悉 model collapse、AI text detection 和 ordinal classification 文献；仔细核验了统计检验和 EDD 定义 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] EDD 定义存在数学缺陷——max 算子不要求连续可判别性\n- 具体位置：§2.4, Eq. 1\n- 问题：当前定义 EDD_T = max{d*+1 : AUC(d*, d*+1) >= T} 取满足阈值的最大 d*，但不要求所有 d' <= d* 的 pair 都满足阈值。如果 AUC(d1,d2) < T 而 AUC(d3,d4) >= T，EDD 会报告误导性的高值。论文实验中 AUC 恰好单调衰减所以没暴露问题，但 §4.3 跨策略 transfer 的 d1/d2 AUC inversion（GPT-2 XL: 0.129）说明非单调情况在这个任务中确实存在。正确定义应为 EDD_T = max{d*+1 : ∀ d' <= d*, AUC(d', d'+1) >= T}。\n- 为什么影响接收：EDD 是论文的核心 contribution 之一，定义缺陷直接影响 metric 的可信度和可复用性。\n- 建议修改方向：修改 Eq. 1 为连续版本；在 Limitations 讨论 cross-strategy 场景下 EDD 的适用边界。\n\n**N2** [critical] 19 维特征的共线性未量化，\"19 features are needed\" 的 claim 缺乏消融支持\n- 具体位置：§2.3 (Table 1), §4.1 (Table 3)\n- 问题：12/19 特征（9 perplexity + 3 surprisal）来自同一 reference model 的 token-level 分布，必然高度相关。论文承认 \"surprisal variance captures second-order structure...not redundant with perplexity moments\"（§2.3），但没提供任何量化证据（VIF、相关矩阵、条件数）。唯一的消融是 single-feature regression（mean_ppl → 25.1%, Table 3），但直接跳到全部 19 特征。缺少中间消融：仅用 top-2 特征（p90_ppl + var_surprisal）能达到多少？仅用 4 类 category 之一的特征呢？这一消融对 \"19 features are needed\"（§4.1）和 \"multi-dimensional feature representation\" 的 claim 至关重要。\n- 为什么影响接收：无法判断信号到底来自几个独立维度，feature universality 的论述因此缺乏坚实基础。\n- 建议修改方向：报告特征相关矩阵；做 top-2 / top-5 / per-category 消融；如果 2-3 个特征即可接近 78%，则需调整 contribution 表述。\n\n**N3** [critical] End-to-end 对比中 attention-importance 相关性方法论有缺陷\n- 具体位置：§4.4, Appendix D\n- 问题：论文用 DeBERTa/RoBERTa 的 attention weight 与 RF permutation importance 做 Spearman 相关（ρ = −0.484 / −0.456），得出 \"complementary representations\" 结论。但 attention weight 不是模型使用某信息的可靠指标——这一点在 attention interpretation 文献中已被广泛讨论（Jain & Wallace, NAACL 2019; Wiegreffe & Pinter, EMNLP 2019 等）。attention 和 feature importance 度量的对象本质不同（token-level attention vs. feature-level importance），负相关可能是 scale mismatch 的 artifact。此外，end-to-end 实验仅在 Pythia nucleus 一个 pipeline 上做，DeBERTa std = ±4.7% 很大，DCOL 6 次迭代中 5 次失败。\n- 为什么影响接收：这是 Contribution 4 的核心证据。如果 attention-importance 相关性不可靠，\"feature-based > end-to-end\" 的机制解释就站不住。\n- 建议修改方向：改用 probing classifier、SHAP/integrated gradients 等更可靠的方法分析 PLM 表征；至少在 2-3 个 pipeline 上复现 end-to-end 结果；单独报告 DCOL 失败原因分析。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] d0 recall >98% 严重膨胀 headline accuracy，应以 d1–d3 accuracy 为主指标\n- 具体位置：§3.1 (Table 2), §4.2 (Table 4), Limitations\n- 问题：d0 是 Wikipedia 原文，与 model-generated text 的分离本质上是 domain classification 而非 depth estimation。论文在 Limitations 中承认了 \"d0 inflation\"，也在 §3.1 报告了 3-class accuracy（排除 d0），但 abstract 和 Introduction 仍以 \"70–85% four-class accuracy\" 为 headline。Cross-model transfer 66.4% 中 d0 recall 为 99.3%，而 d2 recall 最低只有 26.8%（Table 4, Pythia holdout）。\n- 建议：将 d1–d3 3-class accuracy 提升为主指标（或至少并列报告），在 abstract 中明确说明 d0 包含/不包含的区别。\n\n**W2** [warning] \"geometry-level shift\" overclaim——仅凭 z-score normalization 失败\n- 具体位置：§4.3\n- 问题：论文称 z-score normalization 不能解决 d1/d2 inversion，因此确认 \"genuine geometry-level shift rather than a correctable scale difference\"。但 z-score 是最简单的 domain adaptation 方法。论文引用了 Sugiyama et al. (2007) 的 importance weighting，却没尝试。没测试 more sophisticated methods（CORAL domain adaptation、moment matching、adversarial alignment）就下结论，推理跳步太大。\n- 建议：要么至少测试 2-3 种 domain adaptation 方法，要么将结论弱化为 \"z-score normalization is insufficient\"。\n\n**W3** [warning] Table 4, 5 中暴露 experiment ID 可能违反 double-blind\n- 具体位置：Table 4 caption, Table 5 caption\n- 问题：Experiment tracking ID（如 depth_extension_binary_pairwise_002、depth_extension_gpt2xl_d4d5_001）出现在表格 caption 中，暗示使用了特定实验管理系统。这在 double-blind review 中不常见，可能帮助追踪到作者团队的实验基础设施。\n- 建议：删除 experiment ID 或移至匿名化的 supplementary material。\n\n**W4** [warning] DeepSeek V3.2 zero-shot baseline 统计力度不足\n- 具体位置：§4.1 (Table 3, footnote)\n- 问题：仅 200 样本（~50/class），95% CI ±6.8pp，真实值可能在 33.2%–46.8% 范围内。这个 baseline 在 abstract 中被突出使用，但置信区间跨度太大。\n- 建议：增加到至少 1000 样本使 CI 收窄到 ±3pp 以内，或在 abstract 中改为 \"approximately 40% (±6.8pp)\"。\n\n**W5** [warning] 缺少 gradient boosting baseline\n- 具体位置：§4.1 (Table 3)\n- 问题：在 tabular/feature-based classification 中，XGBoost/LightGBM 通常是最强 baseline，但论文缺少此类比较。\n- 建议：加入 XGBoost/LightGBM；如果精度与 RF 一致，则进一步强化 \"signal in features\" 的论点。\n\n---\n\n## 小问题（不影响接收）\n\n- §2.2 \"standard LoRA hyperparameters\" 表述不严谨，建议改为 \"commonly used\"\n- Table 2 caption 报告 \"std 0.2–0.9pp across all cells\" 但没给每个 cell 的具体 CI\n- 引用：knowledge_collapse2025 和 falahati2026_curated 在 OpenAlex 中未找到（可能是索引延迟），alemohammad2024_mad 的 first author 与 API 记录不一致\n- Discussion（§5）仅 2 段，过于简短，缺少 calibration 讨论\n\n---\n\n## 主要优势\n\n- **新任务定义填补真实空白**：在 binary detection 和 model collapse theory 之间建立了 ordinal depth estimation 这一中间层，动机清晰且有实际意义\n- **系统性 Atlas 实验设计**：3 × 3 grid 覆盖 model family 和 decoding strategy 两个轴，每个 cell 报告完整指标\n- **诚实的 Limitations 讨论**：d0 inflation、cross-strategy weakness、EDD threshold sensitivity、reference model dependency 均有明确承认\n- **统计实践总体良好**：bootstrap CI、permutation test、Bonferroni correction、独立 binary classifier 避免 boundary dilution\n- **Feature universality 发现有启发性**：p90_ppl 在 9/9 cells top-2、mean Spearman ρ=0.868",
    "reviewer_id": "1",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-15T16:11:41.458542+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3923
}
```

</details>

---


### Assistant

_source line 98 · 2026-05-15T16:11:46.636787+00:00_

审稿报告已提交给 Review Director。

总结：Overall 3/5（Findings 档），3 个 Must-Fix（EDD 定义数学缺陷、特征共线性消融缺失、end-to-end attention-importance 对比方法论问题），5 个 Should-Fix（d0 inflation、geometry-level shift overclaim、experiment ID 匿名性、DeepSeek baseline 样本量、缺少 GBDT baseline）。论文任务新颖、Atlas 设计系统、统计实践良好，但方法论硬伤需修复后方可接收至主会。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1"
}
```

</details>

---


## Round 4

## Round 4

4 recorded events


### User

_source line 99 · 2026-05-15T16:15:27.663185+00:00_

[Round 1 审稿请求]:
## 交叉分享 — Reviewer 2 的完整审稿意见

请逐条回应 Reviewer 2 的每个 Must-Fix 和 Should-Fix 问题：对每条用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

以下是 Reviewer 2 的完整审稿报告：

### Must-Fix 问题

**N1** [critical] 递归生成的定义与野外场景严重脱节
- 具体位置：§3.2 (method.tex:8-9), §3.4 第32行
- 问题：论文将"递归生成"定义为每一深度都重新 LoRA 微调然后采样（"finetuning $f_\theta$ on $\mathcal{D}_{k-1}$ and sampling from the resulting model"）。但现实中的递归污染机制至少有三种不同形态：(a) 同一模型对自身输出进行 prompt-based 再生成（无重训练），(b) 不同模型之间的跨代污染（Model A 的输出进入 Model B 的训练集），(c) 指令微调模型通过 RLHF 管线间接吸收合成数据。论文的定义只覆盖了一种极其受控的场景（同一 1-1.5B 模型，同一 LoRA 设定，同一 Wikipedia 种子文本）。在这种条件下发现的"统计指纹"能否迁移到野外场景是完全开放的问题，但论文在 Abstract 和 Conclusion 中的 claim 措辞暗示了较广的适用性（如"universal stability across model families and decoding strategies"）。
- 为什么影响接收：这不仅是 Limitations 里的一句话能覆盖的——它影响整篇论文 contribution 的外部效度。如果指纹在野外失效，整个方法论框架的价值将大打折扣。
- 建议修改方向：(1) 在 Introduction 或 Method 中明确界定本文所研究的递归生成机制与野外机制的区别，降低 claim 的普适性语气；(2) 至少提供一个小规模 pilot experiment 测试跨域/跨机制迁移（如用 instruction-tuned 模型或不同种子文本）；(3) 将"universal"这样的用词限定为"universal across the model-strategy grid studied"。

**N2** [critical] 跨策略 d1/d2 AUC 反转从根本上限制部署可行性
- 具体位置：§5.3 (generalization.tex:96-98)
- 问题：当训练集不含温度采样数据时，GPT-2 XL 的 d1/d2 AUC 降至 0.129，OLMo 降至 0.253——不仅低于随机（0.5），而是**反转**了决策边界。z-score 归一化不仅无法修复，反而使情况恶化（0.50→0.24, 0.50→0.19）。论文在 Discussion §6 中提到需要"strategy-conditioned classifiers or automatic strategy identification"，但未提供任何解决方案或 feasibility 分析。在实际部署中，文本的解码策略几乎从不可知，这意味着论文提出的第一个应用场景（§6 depth-graduated data curation）在当前形态下无法实现。
- 为什么影响接收：论文的核心动机是用深度估计来改善数据筛选（§6 第一段），但这个应用场景在当前方法下不可行。这在 motivation 和实际能力之间产生了严重脱节。
- 建议修改方向：(1) 诚实降低 Discussion 中关于数据筛选应用的期望；(2) 分析自动策略识别的可行性——即使只是一个简单的 baseline（如用统计特征先分类策略再分类深度），也能大大加强论文；(3) 考虑是否存在 strategy-agnostic 特征子集能部分避免反转。

**N3** [critical] Discussion 部分严重不足
- 具体位置：§6 (discussion.tex)，全文仅 2 段约 80 词
- 问题：对于提出一个**全新任务**的论文，Discussion 只有两段话是远远不够的。论文提出了一个有趣的问题但几乎没有讨论其更广泛的含义。缺失的关键讨论包括：(a) 混合深度语料库的处理——真实网络文本是不同深度文本的混合体；(b) 深度估计与数据溯源（data provenance）研究的联系；(c) 对抗攻击对深度估计器的影响——Sadasivan et al. (2023) 已证明释义攻击可将二元检测准确率降至随机水平，深度估计器是否同样脆弱？(d) 超过 1.5B 参数模型的扩展性预测。
- 为什么影响接收：ARR reviewer guidelines 明确要求论文应当自成一体地讨论 implications。当前 Discussion 的深度与论文其他部分的质量严重不匹配。
- 建议修改方向：将 Discussion 扩展至至少 1 栏（约 300-400 词），覆盖上述至少 2-3 个方向。

### Should-Fix 问题

**W1** [warning] d0 膨胀效应未在主结果表中充分呈现
- 具体位置：Table 2 (atlas.tex:15-30), Table 5 (generalization.tex:55-67), Table 6 (generalization.tex:77-91)
- 问题：论文在 Limitations 中承认 d0 recall >98% 严重膨胀了 headline accuracy，且在 §4.1 报告了排除 d0 的 3-class 准确率。但主结果 Table 2 只报告了含 d0 的 4-class 准确率，Table 5 和 Table 6 同理。读者必须自行脑补"真正有挑战的 d1-d3 部分表现如何"。交叉模型迁移中 d2 recall 低至 26.8%（Pythia holdout），这个数字如果不在 Table 5 的逐类 recall 中呈现，headline 66.4% 就具有误导性。
- 建议：在 Table 2 中增加一行 d1-d3 准确率（或单独报告 macro-F1 排除 d0），在 Tables 5-6 中增加排除 d0 的 mean accuracy。

**W2** [warning] 实验追踪 ID 可能违反双盲匿名
- 具体位置：Table 3 caption (atlas.tex:87), Table 4 caption (atlas.tex:114), §4.3 dilution paragraph (atlas.tex:131)
- 问题：表格标题中包含实验 ID 如 `depth_extension_binary_pairwise_002`、`depth_extension_gpt2xl_d4d5_001`、`granularity_ablation_rf_001`。如果这些 ID 来自公开实验追踪平台（如 W&B），可能使审稿人或他人通过搜索 ID 反推作者身份，违反 double-blind 要求。
- 建议：删除所有实验 ID，或在审稿期间替换为匿名标识。

**W3** [warning] Zero-shot LLM baseline 证据力弱
- 具体位置：Table 7 (generalization.tex:29, 32-33)
- 问题：DeepSeek V3.2 baseline 仅在 200 个样本上评估，95% CI 为 ±6.8pp，且只测试了 Pythia-1.4B nucleus 一个 cell。40% 的结果在 [33.2%, 46.8%] 范围内，上界接近一些弱 classifier 的表现。此外只测试了一个 LLM baseline（为什么不用 GPT-4o 或 Claude？），且 prompt 设计未报告。
- 建议：至少将样本量增加到 1000+（将 CI 收窄到 ±3pp），或明确声明这只是 anecdotal evidence 而非正式 baseline。

**W4** [warning] 19 特征的冗余性未分析
- 具体位置：§3.3 (method.tex:43-79), Table 1 (method.tex:48-69)
- 问题：19 个特征中存在明显的高相关对：p10/p25/p50/p75/p90 是同一分布的不同分位数；mean_surprisal 与 mean_ppl 数学上直接相关（surprisal = log(ppl)）。论文未报告特征间相关矩阵或进行特征选择分析（如 LASSO、逐步剔除）。RF 对高相关特征有一定鲁棒性，但三种 classifiers（RF/CORAL/DivEye）达到相同准确率可能部分是因为冗余特征使得任何合理方法都能提取相同信号。
- 建议：在附录中提供特征相关矩阵和一个消融实验（如用 top-5 特征 vs. 全 19 特征的准确率对比）。

**W5** [warning] End-to-end learning 比较可能不公平
- 具体位置：§5.4 (generalization.tex:101-109)
- 问题：DeBERTa 和 RoBERTa 仅在一个 cell（Pythia nucleus, 20K 样本）上微调 3 epochs。论文据此得出"depth estimation requires explicit distributional statistics rather than learned text representations"的强结论（generalization.tex:109）。但 20K 样本对于预训练模型微调可能不足；未探索数据量效应；超参数搜索范围未报告；DCOL 的 6 次迭代中有 5 次 DeBERTa 崩溃可能反映实现问题而非方法局限。
- 建议：软化结论措辞（从"requires"改为"benefits from"），或增加一个数据量消融实验。

**W6** [warning] 缺少混合深度语料库的讨论和实验
- 具体位置：全文
- 问题：所有实验假设每个 passage 来自已知的单一深度。现实中，一个网页或文档可能包含不同深度的段落混合。论文未讨论段落级 vs 文档级深度估计，也未测试当训练/测试集包含混合深度文本时的性能。
- 建议：至少在 Discussion 或 Limitations 中讨论此问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 100 · 2026-05-15T16:17:06.018661+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 交叉回应 Reviewer 2（Round 1）\n\n### Must-Fix\n\n**[AGREE] R2-N1: 递归生成定义与野外场景脱节**\n同意核心判断但建议降半级至 should-fix。论文 §3.2 的 \"universality\" 实际限定在 9 个 atlas cells 内（Spearman ρ=0.868），Abstract 的 \"universal stability across model families and decoding strategies\" 范围界定准确。问题在于读者容易过度泛化——需要更显式的 scope 声明，但不构成 claim 错误。R2 建议的 pilot experiment（换种子语料或用 instruction-tuned 模型）非常有建设性。\n\n**[AGREE] R2-N2: d1/d2 AUC 反转限制部署**\n与我的 W2 一致。进一步补充：论文仅试了 z-score normalization 一种方法就得出 \"geometry-level shift\" 结论（§4.3），推理链太短。R2 建议的 two-stage pipeline（先分类策略再分类深度）是低成本高价值实验。但核心 contribution 是任务定义和特征发现，不是 deployment-ready 系统，建议定位为 should-fix。\n\n**[REBUT] R2-N3: Discussion 不足 → 应为 should-fix**\n不同意 critical 定位。Limitations section（conclusion.tex:9-35）有 6 段详细讨论，覆盖了 cross-strategy 限制、d0 inflation、ecological transfer、EDD threshold sensitivity 等。Discussion 偏短是写作问题，不影响 Soundness。ARR H13 提醒不应要求超出 stated claims 的分析。建议降级为 W。\n\n### Should-Fix\n\n**[AGREE] R2-W1**: d0 膨胀。与我的 W1 一致。\n**[AGREE] R2-W2**: 实验 ID 匿名性。与我的 W3 一致。\n**[AGREE] R2-W3**: LLM baseline 弱。与我的 W4 一致。R2 补充了 prompt 未报告的问题。\n**[AGREE] R2-W4**: 特征冗余 → 但我认为应升级为 critical。与我的 N2 一致。mean_surprisal 和 mean_ppl 数学直接相关，缺少 top-2 / top-5 消融无法判断 \"19 features are needed\" 是否成立。\n**[AGREE] R2-W5**: End-to-end 比较 → 应升级。与我的 N3 一致。\"requires\" → \"benefits from\" 是最低限度修改。\n**[AGREE] R2-W6**: 混合深度语料库讨论缺失。好的补充视角，我 Round 1 未覆盖。\n\n### 总结\n5/9 issue 完全一致。主要分歧：R2-N3 我认为应降级；R2-W4、W5 我认为应升级。两份 review 的合集覆盖了方法严谨性（我的侧重）和外部效度/部署可行性（R2 的侧重）。",
  "reviewer_id": "1",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 交叉回应 Reviewer 2（Round 1）\n\n### Must-Fix\n\n**[AGREE] R2-N1: 递归生成定义与野外场景脱节**\n同意核心判断但建议降半级至 should-fix。论文 §3.2 的 \"universality\" 实际限定在 9 个 atlas cells 内（Spearman ρ=0.868），Abstract 的 \"universal stability across model families and decoding strategies\" 范围界定准确。问题在于读者容易过度泛化——需要更显式的 scope 声明，但不构成 claim 错误。R2 建议的 pilot experiment（换种子语料或用 instruction-tuned 模型）非常有建设性。\n\n**[AGREE] R2-N2: d1/d2 AUC 反转限制部署**\n与我的 W2 一致。进一步补充：论文仅试了 z-score normalization 一种方法就得出 \"geometry-level shift\" 结论（§4.3），推理链太短。R2 建议的 two-stage pipeline（先分类策略再分类深度）是低成本高价值实验。但核心 contribution 是任务定义和特征发现，不是 deployment-ready 系统，建议定位为 should-fix。\n\n**[REBUT] R2-N3: Discussion 不足 → 应为 should-fix**\n不同意 critical 定位。Limitations section（conclusion.tex:9-35）有 6 段详细讨论，覆盖了 cross-strategy 限制、d0 inflation、ecological transfer、EDD threshold sensitivity 等。Discussion 偏短是写作问题，不影响 Soundness。ARR H13 提醒不应要求超出 stated claims 的分析。建议降级为 W。\n\n### Should-Fix\n\n**[AGREE] R2-W1**: d0 膨胀。与我的 W1 一致。\n**[AGREE] R2-W2**: 实验 ID 匿名性。与我的 W3 一致。\n**[AGREE] R2-W3**: LLM baseline 弱。与我的 W4 一致。R2 补充了 prompt 未报告的问题。\n**[AGREE] R2-W4**: 特征冗余 → 但我认为应升级为 critical。与我的 N2 一致。mean_surprisal 和 mean_ppl 数学直接相关，缺少 top-2 / top-5 消融无法判断 \"19 features are needed\" 是否成立。\n**[AGREE] R2-W5**: End-to-end 比较 → 应升级。与我的 N3 一致。\"requires\" → \"benefits from\" 是最低限度修改。\n**[AGREE] R2-W6**: 混合深度语料库讨论缺失。好的补充视角，我 Round 1 未覆盖。\n\n### 总结\n5/9 issue 完全一致。主要分歧：R2-N3 我认为应降级；R2-W4、W5 我认为应升级。两份 review 的合集覆盖了方法严谨性（我的侧重）和外部效度/部署可行性（R2 的侧重）。",
    "reviewer_id": "1",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-15T16:17:10.290024+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4271
}
```

</details>

---


### Assistant

_source line 102 · 2026-05-15T16:17:13.833893+00:00_

交叉回应已提交。与 Reviewer 2 在 5/9 个 issue 上完全一致，主要分歧在 Discussion 长度的严重程度定位（我认为 should-fix）和特征冗余 / end-to-end 对比的严重程度（我认为应升级为 critical）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1"
}
```

</details>

---


## Round 5

## Round 5

38 recorded events


### User

_source line 103 · 2026-05-16T12:05:09.009422+00:00_

[Round 1 审稿请求]:
## 审稿任务分配 — Reviewer 1（方法严谨性 + 实验设计）

### Venue 信息
- **目标会议**: EMNLP 2026（ACL Rolling Review May cycle）
- **截止日期**: 2026-05-25
- **格式**: 长文 8 页正文 + 无限引用 + 附录，ACL 模板，double-blind
- **匿名规则**: Double-blind（无匿名期要求）
- **附录**: 允许，不保证审稿人阅读

### 论文路径
`projects/recursive_gen_depth_est/docs/paper/main.tex`
（含 abstract.tex, introduction.tex, related_work.tex, method.tex, atlas.tex, generalization.tex, discussion.tex, conclusion.tex, section_appendix.tex）

### 你的审查侧重
你负责评估论文的**方法严谨性**和**实验设计**，重点关注：

1. **EDD metric 的数学严谨性**：Eq.1 定义（∀ formulation）是否正确？与全文数值是否一致？threshold sensitivity 是否充分？
2. **特征设计的合理性**：19 维特征中 14-16 个 VIF>10 的高共线性是否影响结论？top-5 = 97.6% 的消融是否充分排除冗余？forward selection 结果是否一致？
3. **统计方法论**：5-fold CV 的实验设计是否恰当？bootstrap CI 是否正确使用？classifier convergence（RF/XGB/LGBM ≤0.4pp spread）的结论是否过强？
4. **实验控制变量**：LoRA fine-tuning pipeline（r=16, α=32）是否引入 confound？BOS-seeded 无条件生成是否充分模拟递归污染？Wiki seed → recursive generation 是否有 domain leakage？
5. **Cross-scale 实验设计**：7B 模型仅 500 samples/depth（vs 1.4B 的 5000）——统计功效是否足够？QLoRA 4-bit 引入量化噪声是否 confound？仅 2 个 7B 模型能否支撑 scale generalization claim？
6. **Zero-shot LLM baseline**：500 samples、无 in-context examples、单一 prompt template——是否是公平对比？是否 strawman？
7. **Wild-data calibration**：C4 FPR 4.7%-22.4% 的 model gap 是否有统计检验？WikiText vs C4 的对比是否 fair（editorial vs web crawl）？
8. **Curation PoC**：5 seeds 的效力是否足以支撑 significance claims？rf vs random 的配对检验是否恰当？

以 EMNLP 顶级审稿标准评审。输出标准审稿格式：Summary → Strengths → Weaknesses（分 Must-Fix / Should-Fix / Nice-to-Have）→ Questions → Missing References → Overall Score (1-5) + Confidence。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-16T12:05:30.552564+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
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

_source line 105 · 2026-05-16T12:05:30.603188+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 106 · 2026-05-16T12:05:34.421658+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 107 · 2026-05-16T12:05:35.987037+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 108 · 2026-05-16T12:05:35.987494+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 109 · 2026-05-16T12:05:44.032031+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"}]

Based on the search results, here's information about the ACL Rolling Review 2026 reviewer guidelines, review form, and evaluation criteria:

## Reviewer Guidelines

ARR reviewers are instructed to write a review as if the paper were being considered for the ACL conference. Thus low scores may indicate the submission is not a good fit for ACL, even
…[truncated 1987 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 9610
}
```

</details>

---


### Tool call

_source line 110 · 2026-05-16T12:05:48.102830+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review review form scoring rubric soundness excitement novelty 1-5 scale"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review review form scoring rubric soundness excitement novelty 1-5 scale"
  }
}
```

</details>

---


### Tool call

_source line 111 · 2026-05-16T12:05:48.103294+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 112 · 2026-05-16T12:05:48.153899+00:00_

1	% How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
2	% Target: EMNLP 2026 (ARR May cycle)
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{amsmath}
10	\usepackage{amssymb}
11	\usepackage{multirow}
12	\usepackage{xcolor}
13	\usepackage{subcaption}
14	\usepackage[T1]{fontenc}
15	\usepackage[utf8]{inputenc}
16	\usepackage{microtype}
17	\usepackage{amsthm}
18	
19	\theoremstyle{definition}
20	\newtheorem{definition}{Definition}
21	
22	\title{How Deep Is Your Data? Estimating Recursive Generation Depth\\via Statistical Fingerprints}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\input{abstract}
30	
31	\input{introduction}
32	
33	\input{related_work}
34	
35	\input{method}
36	
37	\input{atlas}
38	
39	\input{generalization}
40	
41	\input{discussion}
42	
43	\input{conclusion}
44	
45	\bibliography{references}
46	
47	\appendix
48	\input{section_appendix}
49	
50	\end{document}
51	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 113 · 2026-05-16T12:05:54.082080+00:00_

Web search results for query: "ACL Rolling Review review form scoring rubric soundness excitement novelty 1-5 scale"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"},{"title":"ACL’23 Peer Review Form - ACL 2023","url":"https://2023.aclweb.org/blog/review-form/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Program Chairs’ Report on Peer Review at ACL 2023 Anna Rogers}","url":"https://aclanthology.org/2023.acl-long.report.pdf"},{"title":"ACL’23 Peer Review Policies - ACL 2023","url":"https://2023.aclweb.org/blog/review-acl23/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Program Chairs' Report on Peer Review at ACL 2023","url":"http://www.cs.umd.edu/~jbg/docs/2023_acl_peer_review_report.pdf"},{"title":"ACL 2026 on X: \"Checkout the blog post on the soundness/excitement scores https://t.co/AKSO9DjiYP . It clarifies the reasoning behind the separation of overall scores and how it might make the reviewer recommendation more robust. #ACL2023Toronto #ACL2023NLP #NLProc\" / X","url":"https://x.com/aclmeeting/status/1637827267173953540"}]

Based on the search results, I found detailed information about the ACL Rolling Review's scoring rubric. Here's what the review form includes:

## Soundness Score

The soundness scale ranges from 5 (Excellent: one of the most thorough studies) to 1 (Poor: not s
…[truncated 1127 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 5979
}
```

</details>

---


### Tool call

_source line 114 · 2026-05-16T12:05:57.446065+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "aclrollingreview.org/reviewform review form fields 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "aclrollingreview.org/reviewform review form fields 2024 2025"
  }
}
```

</details>

---


### Tool call

_source line 115 · 2026-05-16T12:05:57.949057+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 116 · 2026-05-16T12:05:58.401542+00:00_

1	\begin{abstract}
2	As large language models increasingly train on web text containing their own outputs, a recursive model$\to$data$\to$model loop arises---yet no method estimates how many such iterations a text has undergone.
3	We formalize \emph{recursive generation depth estimation} as ordinal classification and construct a benchmark of 180K passages spanning 3 model families, 3 decoding strategies, and 4 generation depths.
4	From each passage we extract a compact statistical fingerprint---19 candidate features dominated by perplexity tail statistics, with the top 5 achieving 97.6\% of full-set performance---computed against a fixed reference model (Pythia-1.4B).
5	A Random Forest classifier achieves 70--85\% four-class accuracy (chance = 25\%; 58.8--82.6\% when excluding the near-perfectly separable d0 class; a zero-shot LLM baseline reaches only 36.2\%), with 90th-percentile perplexity and surprisal variance emerging as consistent depth markers across the studied $3 \times 3$ grid (top-2 importance in 9/9 and 8/9 cells, respectively).
6	Our \emph{Depth Degradation Atlas} reveals that decoding strategy reshapes degradation trajectories rather than merely attenuating them, and we define the \emph{Effective Discriminable Depth} (EDD) metric, finding $\mathrm{EDD}_{0.75}{=}4$ for extended recursion chains.
7	Cross-model transfer reaches 66.4\% and cross-strategy transfer 59.1\%; temperature sampling induces a d1/d2 AUC inversion that we decompose into a correctable scale component and a residual structural component.
8	Notably, cross-model recursive chains---where each depth is generated by a different architecture---achieve 84.75\% accuracy, demonstrating that the depth signal is a property of the recursive process itself rather than of any individual generator.
9	Extending to two 7B-scale generators yields 70.2\% accuracy with monotonic AUC decay ($\mathrm{EDD}{=}4$), while a second 7B architecture exhibits $\mathrm{EDD}{>}5$ with a non-monotonic trajectory pos
…[truncated 329 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 117 · 2026-05-16T12:05:58.402050+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 118 · 2026-05-16T12:05:59.004226+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	The text on which large language models are trained increasingly contains their own outputs.
5	As synthetic content proliferates across the web, a recursive loop emerges: models trained on web corpora ingest text generated by earlier models, and their outputs feed into the next generation's training data \cite{shumailov2024_nature,alemohammad2024_mad}.
6	This model$\to$data$\to$model cycle is no longer hypothetical---it is already occurring in the wild---yet we lack the ability to determine how many recursive iterations a given text has undergone, a distinction that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \cite{dohmatob2024_tale_of_tails}.
7	
8	Existing tools address adjacent but distinct problems.
9	Binary detectors such as Binoculars \cite{binoculars2024}, Fast-DetectGPT \cite{fast_detectgpt2024}, and DivEye \cite{diveye2026} classify text as human-written or machine-generated, collapsing all depths $d \geq 1$ into a single category.
10	Watermarking \cite{kirchenbauer2023_watermark} requires proactive embedding and cannot be applied retroactively.
11	The model collapse literature \cite{shumailov2024_nature,dohmatob2024_tale_of_tails} assumes depth is known a priori; \citet{drayson2025_detection_prevents_collapse} filter synthetic data via binary detection without distinguishing depths.
12	No existing method estimates the ordinal recursive generation depth of a text passage from its content alone.
13	
14	Our key insight is that recursive generation leaves quantifiable statistical fingerprints in text, and these fingerprints are \textbf{universal and scale-variant} across the three model families and three decoding strategies studied.
15	Specifically, perplexity tail statistics---the 90th-percentile perplexity (\textsc{p90\_ppl}) and surprisal variance (\textsc{var\_surpris
…[truncated 3116 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 119 · 2026-05-16T12:05:59.004695+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 120 · 2026-05-16T12:05:59.055283+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Definition}
5	\label{sec:method:problem}
6	
7	Let $f_\theta$ denote a language model and $\mathcal{D}_0$ a corpus of human-written seed text.
8	We define a \emph{recursive generation chain} of depth $K$ as the sequence $\mathcal{D}_0, \mathcal{D}_1, \dots, \mathcal{D}_K$, where each $\mathcal{D}_k$ ($k \geq 1$) is produced by finetuning $f_\theta$ on $\mathcal{D}_{k-1}$ and sampling from the resulting model.
9	Depth $d{=}0$ denotes human-written text; depth $d{=}k$ ($k \geq 1$) denotes text generated by a model trained on depth-$(k{-}1)$ data.
10	
11	Given a text passage $x$, the task is to estimate its recursive generation depth $d \in \{0, 1, \dots, K\}$.
12	This is an ordinal classification problem: depths carry a natural ordering, and $d{=}1$ is structurally closer to $d{=}0$ than $d{=}3$ is, since each generation step compounds distributional drift.
13	
14	\subsection{Multi-Generational Benchmark Construction}
15	\label{sec:method:benchmark}
16	
17	We construct a benchmark spanning three axes: model family, decoding strategy, and generation depth.
18	
19	\paragraph{Model families.}
20	We select three 1--1.5B-parameter models with diverse pretraining corpora and architectures: Pythia-1.4B (EleutherAI), OLMo-1B (AI2), and GPT-2~XL (OpenAI, 1.5B).
21	Restricting to a narrow parameter range isolates the effect of architecture and training data from scale.
22	
23	\paragraph{Decoding strategies.}
24	Each model is paired with three decoding strategies: nucleus sampling ($p{=}0.95$) \cite{holtzman2020_nucleus}, temperature sampling ($\tau{=}0.9$), and top-$k$ sampling ($k{=}50$).
25	These span the dominant modes of open-ended generation and induce qualitatively different entropy profiles.
26	Our findings on feature importance and discriminability are limited to this grid; transfer to untested models, scales, or strategies is not established.
27	
28	\paragraph{Depth and scale.}
29	The primary benchmark cov
…[truncated 6993 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 121 · 2026-05-16T12:06:02.489186+00:00_

Web search results for query: "aclrollingreview.org/reviewform review form fields 2024 2025"

Links: [{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Forms","url":"https://aclrollingreview.org/reviewforms/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"}]

Based on the search results, I found information about the ACL Rolling Review (ARR) system and related forms for 2024-2025, though the specific detailed review form fields from the direct URL weren't fully displayed in the search results.

Here's what I found:

## Review Form and Submission Information

The review form is part of a peer review platform for the Association for Computational Linguistics.

## Related Forms and Requirements

The ARR system includes several
…[truncated 902 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 5043
}
```

</details>

---


### Tool call

_source line 122 · 2026-05-16T12:06:12.051399+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
  }
}
```

</details>

---


### Tool result

_source line 123 · 2026-05-16T12:06:13.107084+00:00_

1	\section{The Depth Degradation Atlas}
2	\label{sec:atlas}
3	
4	We present the Depth Degradation Atlas: a systematic empirical map of how statistical fingerprints evolve across recursive generation depths, models, and decoding strategies.
5	The atlas spans $3 \times 3 = 9$ model--strategy cells evaluated at depths $d \in \{0, 1, 2, 3\}$, with depth extensions to $d{=}5$ for cross-model EDD validation (\S\ref{sec:atlas:edd}).
6	
7	%% ----------------------------------------------------------------
8	\subsection{In-Distribution Performance}
9	\label{sec:atlas:id}
10	
11	Table~\ref{tab:main_matrix} reports four-class Random Forest accuracy (5-fold CV, 200 trees) across all nine cells.
12	Accuracy ranges from 69.6\% (Pythia, top-$k$) to 85.4\% (GPT-2~XL, temperature), all exceeding the 25\% chance baseline by a wide margin.
13	Two axis effects emerge.
14	GPT-2~XL achieves the highest accuracy under every strategy (76.6--85.4\%), followed by OLMo (74.2--82.0\%) and Pythia (69.6--78.2\%).
15	Top-$k$ sampling yields the lowest accuracy in every model.
16	The mean within-model strategy gap is 8.4~pp, comparable to the 7.1~pp mean within-strategy model gap---decoding strategy and model family contribute roughly equally to performance variance.
17	
18	\begin{table}[t]
19	\centering
20	\small
21	\caption{Four-class RF accuracy (\%) across the $3 \times 3$ atlas, with d1--d3 three-class accuracy in parentheses (chance = 25\% / 33\%). Depth-0 recall exceeds 98\% in all cells.}
22	\label{tab:main_matrix}
23	\begin{tabular}{@{}lccc@{}}
24	\toprule
25	& Nucleus & Temp.\ $\tau{=}0.9$ & Top-$k$ \\
26	\midrule
27	Pythia-1.4B  & 78.2\,(71.2) & 76.3\,(70.6) & 69.6\,(58.8) \\
28	OLMo-1B     & 78.8\,(75.0) & 82.0\,(76.3) & 74.2\,(66.1) \\
29	GPT-2~XL    & 83.3\,(79.0) & 85.4\,(82.6) & 76.6\,(69.5) \\
30	\bottomrule
31	\end{tabular}
32	\end{table}
33	
34	\paragraph{Per-class recall distribution.}
35	Depth-0 recall exceeds 98\% in all 9 cells, confirming that human-written text is triviall
…[truncated 11665 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1055
}
```

</details>

---


### Tool call

_source line 124 · 2026-05-16T12:06:13.107554+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
  }
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-16T12:06:13.209217+00:00_

1	\section{Generalization and Robustness}
2	\label{sec:generalization}
3	
4	We test whether the atlas results (69.6--85.4\%) reflect genuine statistical regularities or training artifacts, evaluating generalization along seven axes: four in detail below---classifier choice (\S\ref{sec:gen:baselines}), cross-model transfer (\S\ref{sec:gen:crossmodel}), cross-strategy transfer (\S\ref{sec:gen:crossstrategy}), and cross-scale generalization (\S\ref{sec:gen:crossscale})---and three in the Appendix (end-to-end learning, temperature robustness, and cross-boundary transfer).
5	
6	\subsection{Baseline Comparison}
7	\label{sec:gen:baselines}
8	
9	Table~\ref{tab:baselines} evaluates three classifier families---bagging (RF), gradient boosting (XGBoost, LightGBM)---on the same 19 features across three atlas cells spanning the full accuracy range.
10	Per-cell spread is $\leq$0.4pp, establishing a feature-determined ceiling independent of the learning algorithm.
11	On Pythia nucleus, CORAL ordinal regression \cite{coral2020} (78.1\%) and DivEye \cite{diveye2026} (78.2\%) match the within-cell RF of Table~\ref{tab:main_matrix} within 0.1\,pp (bootstrap $p>0.05$, Bonferroni-corrected); all feature-based methods significantly outperform CE-MLP (74.9\%, $p<0.001$) and logistic regression (75.0\%).
12	Single-feature regression on mean perplexity performs at chance (25.1\%); two zero-shot LLMs---DeepSeek V3.2 (36.2\%, 95\% CI $[32.0, 40.4]$) and Qwen2.5-7B-Instruct (30.4\%, $[26.5, 34.6]$; each 500 samples, prompt template in Appendix~\ref{app:zeroshot_prompt})---both fail to distinguish recursive depth, performing near chance (25\%).
13	The accuracy gap between RF (78.2\%) and both LLMs exceeds 42\,pp---an order of magnitude above the CI half-width (${\approx}$4\,pp)---ensuring this finding is robust at $n{=}500$.
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\caption{Classifier convergence: 4-class accuracy (\%) across three atlas cells. RF (bagging), XGBoost and LightGBM (gradi
…[truncated 9434 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 126 · 2026-05-16T12:06:13.259989+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-16T12:06:13.310721+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	We formalized recursive generation depth estimation and showed that a compact feature set dominated by perplexity tail statistics achieves 70--85\% four-class accuracy ($\mathrm{EDD}_{0.75}{=}4$ across models; \S\ref{sec:atlas:edd}), with five features sufficing for 97.6\% of full performance and classifier-agnostic convergence within $\leq$0.4pp.
5	The dominant pair (\texttt{p90\_ppl} top-2 in 9/9 cells, \texttt{var\_surprisal} in 8/9 under SHAP) generalizes across the three studied model families without retraining, making depth estimation a candidate early-warning signal for model collapse~\cite{shumailov2024_nature} within this experimental scope.
6	Recent work corroborates this connection, identifying entropy decline as a measurable signal of recursive degradation that parallels the tail erosion our features capture~\cite{shi2025_closer_look}.
7	Zero-shot LLM baselines reinforce this view: DeepSeek V3.2 (36.2\%) and Qwen2.5-7B (30.4\%) exhibit complementary failure modes---the former predicts nearly all samples as d0 while the latter is biased toward d1---yet both perform near chance, confirming that depth discrimination requires the targeted statistical features our pipeline extracts rather than general language understanding.
8	
9	Cross-strategy transfer remains the primary bottleneck (59.1\% vs.\ 66.4\% cross-model), with the temperature-induced d1/d2 AUC inversion making single-classifier deployment across unknown decoding strategies infeasible.
10	A multi-temperature ablation ($\tau \in [0.5, 1.1]$, Pythia-1.4B; Appendix~\ref{app:multi_tau}) reinforces this: within-$\tau$ depth discrimination is robust for $\tau \leq 0.9$ (d1v2 AUC $>0.80$), but cross-$\tau$ transfer (mean 46.7\%) is harder than cross-strategy transfer (59.1\%), confirming that strategy-conditioned classifiers are necessary.
11	A two-stage pipeline---first identifying the decoding strategy, then applying a strategy-conditi
…[truncated 3538 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 128 · 2026-05-16T12:06:18.531190+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-16T12:06:18.933594+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Model Collapse Theory.}
5	\citet{shumailov2024_nature} demonstrate that recursive training on model outputs erodes distributional tails, collapsing the output distribution.
6	\citet{dohmatob2024_tale_of_tails} formalize this via scaling laws distinguishing tail \emph{narrowing} from \emph{cutting}; \citet{dohmatob2025_strong_collapse} establish strong collapse guarantees, and \citet{dohmatob2024_demystified} analyze the regression case.
7	The MAD framework \cite{alemohammad2024_mad} extends this to self-consuming models and quantifies the precision--recall tradeoff.
8	Mitigation strategies include retaining real data \cite{gerstgrasser2024_accumulate} and filtering via detection \cite{drayson2025_detection_prevents_collapse}.
9	Recent work identifies non-monotonic dynamics \cite{bakshi2026_collapse_improvement}, fixed-point convergence \cite{marchi2024_heat_death}, contamination bounds \cite{wang2026_contamination}, curated pipelines \cite{falahati2026_curated}, knowledge collapse \cite{knowledge_collapse2025}, spectral signatures \cite{sigma2026_spectral}, and self-improving loops \cite{synthetic_eggs2026}.
10	These works characterize degradation but assume depth is known a priori; we address the inverse problem of estimating depth from text alone.
11	
12	\paragraph{AI Text Detection.}
13	The detection literature, recently surveyed by \citet{wu2025_detection_survey}, spans statistical, model-based, and watermarking paradigms.
14	DetectGPT \cite{mitchell2023_detectgpt} introduced probability curvature as a zero-shot detection signal; Fast-DetectGPT \cite{fast_detectgpt2024} improves efficiency via surrogate-model conditional curvature.
15	Binoculars \cite{binoculars2024} exploits perplexity ratios between related models, DivEye \cite{diveye2026} leverages surprisal diversity, and GLTR \cite{gehrmann2019_gltr} visualizes per-token likelihood ranks.
16	Fundamental limits exist: paraphrasing reduces detecti
…[truncated 2601 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 130 · 2026-05-16T12:06:18.933998+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 131 · 2026-05-16T12:06:19.335562+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Cross-strategy deployment constraint.}
5	Cross-strategy transfer induces a d1/d2 boundary inversion under temperature sampling.
6	Per-strategy z-score normalization partially corrects the inversion under logistic regression (GPT-2~XL d1v2 AUC $0.24{\to}0.56$, OLMo $0.19{\to}0.70$) but yields negligible improvement for the Random Forest classifier used throughout the main experiments ($\Delta < 0.02$\,pp), and even in the best case (logistic regression) leaves a residual gap relative to within-strategy performance (${\sim}0.83$), indicating that a two-stage pipeline (strategy identification + strategy-conditioned classification) is needed for reliable cross-strategy deployment.
7	
8	\paragraph{d0 inflation of headline metrics.}
9	Depth~0 (human-written text) is near-perfectly separable (recall $>$98\% across all nine model--strategy settings), inflating headline accuracy.
10	Cross-model transfer accuracy of 66.4\% is substantially driven by d0; d2 recall drops to 26.8\% in the worst case (Pythia holdout).
11	
12	\paragraph{Controlled vs.\ ecological setting.}
13	The primary benchmark uses Wikipedia seed text with controlled recursive generation (LoRA fine-tuning, 1--1.5B parameter models); cross-scale experiments extend to 7--8B instruction-tuned models (\S\ref{sec:gen:crossscale}).
14	This protocol isolates the recursive depth variable but diverges from wild recursive contamination, where models are pretrained on mixed corpora containing prior-generation outputs at unknown proportions; the fingerprints we identify may attenuate or shift under such diffuse exposure.
15	Depth signal is the dominant classification factor (5-fold CV 59--82\%, up to 2.5$\times$ chance): LOGO accuracy (72.1\%) matches standard CV (72.0\%), and seed-group prediction is at chance (10.2\% vs.\ 10\%; Appendix~\ref{app:domain_bias}).
16	The 7--8B experiments use instruction-tuned models only; whether base models at this scale e
…[truncated 4054 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 132 · 2026-05-16T12:06:19.335987+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 133 · 2026-05-16T12:06:19.387144+00:00_

1	\section{Additional Results}
2	\label{app:additional}
3	
4	\subsection{Top-$k$ Feature Trajectories}
5	\label{app:topk_trajectories}
6	
7	Figure~\ref{fig:feature_trajectory} in the main text shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\tau{=}0.9$) sampling.
8	Top-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \S\ref{sec:atlas:strategy}.
9	Concretely, the d0$\to$d1 drop in \textsc{p90\_ppl} under top-$k$ is 78\% (vs.\ 87\% for nucleus), and the d2$\to$d3 reduction is 31\% (vs.\ 39\% for nucleus).
10	Despite the magnitude reduction, feature rank ordering across depths is preserved, which explains why ordinal classifiers maintain directionality even under top-$k$ conditions.
11	
12	\subsection{Permutation Importance}
13	\label{app:permutation}
14	
15	To verify that the Gini-based importance rankings in \S\ref{sec:atlas:features} are not an artifact of the impurity measure, we compute permutation importance (5-fold CV, 10 repeats) for all 9 atlas cells.
16	The top-2 features are stable across measures: \textsc{p90\_ppl} ranks in the top 2 in 9/9 cells under both Gini and permutation importance, and \textsc{var\_surprisal} in 8/9 (vs.\ 7/9 for Gini, with the additional cell being OLMo top-$k$; the single SHAP exception is GPT-2~XL top-$k$, where \textsc{p75\_ppl} displaces \textsc{var\_surprisal} to rank 3).
17	Kendall's $W{=}0.90$ across all three methods (Gini, permutation, SHAP) indicates strong concordance ($p{<}0.005$).
18	Pairwise Spearman correlations are: SHAP--Gini $\rho{=}0.93$, SHAP--permutation $\rho{=}0.84$, Gini--permutation $\rho{=}0.76$.
19	Per-cell top-5 overlap between SHAP and permutation importance is 3--4 out of 5 features; the aggregated (mean-across-cells) top-5 sets are identical, confirming that the top features are robust to the choice of importance measure at the aggregate l
…[truncated 23370 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 134 · 2026-05-16T12:07:17.400325+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
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

_source line 135 · 2026-05-16T12:07:17.400789+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 136 · 2026-05-16T12:07:23.425362+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form fields, especially: 1) All scoring dimensions and their scales (1-5 etc), 2) The exact descriptions for each score level (what does 1 mean, 2, 3, 4, 5), 3) Any other required fields like \"confidence\". Return the full rubric."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form fields, especially: 1) All scoring dimensions and their scales (1-5 etc), 2) The exact descriptions for each score level (what does 1 mean, 2, 3, 4, 5), 3) Any other required fields like \"confidence\". Return the full rubric."
  }
}
```

</details>

---


### Tool result

_source line 137 · 2026-05-16T12:07:31.412049+00:00_

# ACL Rolling Review Form - Complete Rubric

## Scoring Dimensions

### 1. **Reviewer Confidence** (1-5 scale)
- **5:** "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4:** "Quite sure. I tried to check the important points carefully."
- **3:** "Pretty sure, but there's a chance I missed something."
- **2:** "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1:** "Not my area, or paper is very hard to understand."

### 2. **Soundness** (1-5 scale with half-point increments)
- **5:** "Excellent: This study is one of the most thorough I have seen."
- **4:** "Strong: This study provides sufficient support for all claims."
- **3:** "Acceptable: Study provides sufficient support for main claims."
- **2:** "Poor: Some main claims are not sufficiently supported."
- **1:** "Major Issues: Not sufficiently thorough to warrant publication."

### 3. **Excitement** (1-5 scale with half-point increments)
- **5:** "Highly Exciting: I would recommend this paper to others."
- **4:** "Exciting: I would mention this paper to others."
- **3:** "Interesting: I might mention some points."
- **2:** "Potentially Interesting: Does not resonate with me personally."
- **1:** "Not Exciting: Lacks community resonance."

### 4. **Overall Assessment** (1-5 scale with half-point increments)
- **5:** Consider for Award (top 2.5%)
- **4:** Conference acceptance
- **3:** Findings track acceptance
- **2:** Resubmit next cycle
- **1:** Do not resubmit

### 5. **Reproducibility** (1-5 scale)
- **5:** Easily reproducible
- **4:** Mostly reproducible
- **3:** Reproducible with difficulty
- **2:** Very difficult to reproduce
- **1:** Impossible to reproduce

### 6. **Datasets Value** (1-5 scale)
- **5:** Enabling
- **4:** Useful
- **3:** Potentially useful
- **2:** Documentary
- **1:** No usable datasets

### 7. **Software Value** (1-5 scale)
- **5:** Enabling
- **4:** Useful
- **3:** Potentially useful
…[truncated 522 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7986
}
```

</details>

---


### Tool call

_source line 138 · 2026-05-16T12:09:39.855539+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿报告 — 方法严谨性 + 实验设计\n\n**论文**: \"How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\"\n**Venue**: EMNLP 2026 (ACL ARR May cycle)\n\n---\n\n## Paper Summary\n\n本文形式化了\"递归生成深度估计\"任务（ordinal classification），构建了 180K 样本的 3×3 benchmark（3 model families × 3 decoding strategies × 4 depths），提取 19 维统计特征（以 perplexity tail statistics 为主导），用 Random Forest 达到 70-85% 四分类准确率。引入 EDD metric 量化可区分深度前沿，发现 EDD₀.₇₅=4。进一步测试了 cross-model transfer、cross-strategy transfer、7B-scale 泛化等。\n\n---\n\n## 总体评分\n\n**Overall**: 3.5/5（介于 Findings track acceptance 和 Conference acceptance 之间）\n**一句话总结**: 任务新颖且系统性强，但几个关键 claim 的统计支撑不足（EDD₀.₇₅=4 的统计显著性、cross-scale N=2 的泛化声明、LLM baseline 的公平性），修订后可达 acceptance 水平。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 主要 claim 有支撑但部分 claim 统计证据不足（EDD、cross-scale） |\n| Excitement | 4/5 | 任务定义新颖且实用，与 model collapse 文献形成良好互补 |\n| Reproducibility | 4/5 | 特征定义、超参数、pipeline 描述充分；代码未公开但承诺 release |\n| Confidence | 4/5 | 熟悉统计方法论和 ML 实验设计，仔细核查了数值 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] EDD₀.₇₅=4 在 abstract 中作为通用结论呈现，但 GPT-2 XL 的统计证据不支持\n\n- 具体位置：Abstract line 6; §4.4 (\"bootstrap testing... p=0.505 for GPT-2 XL (non-significant)\")\n- 问题：Abstract 声称 \"finding EDD₀.₇₅=4 for extended recursion chains\"，但 §4.4 明确报告 GPT-2 XL 的 d3-vs-d4 AUC=0.750（恰好在阈值边界），bootstrap 检验 p=0.505（non-significant）。三个模型中只有 Pythia (p=0.001) 统计显著，OLMo (p=0.091) marginal，GPT-2 XL 不显著。用 \"graded confidence\" 修饰并不改变 abstract 中无条件陈述的问题。\n- 为什么影响接收：EDD 是本文核心创新指标之一，abstract 中的表述暗示这是一个 robust finding，但 1/3 模型不达显著性。\n- 建议修改方向：Abstract 改为 \"EDD₀.₇₅=4 for Pythia-1.4B (p=0.001); consistent direction across models but with graded statistical support (GPT-2 XL: p=0.505)\" 或使用更保守的 T=0.70（所有模型均>0.70 at d3v4）。\n\n**N2** [critical] Zero-shot LLM baseline 是结构性不公平对比（strawman）\n\n- 具体位置：§5.1 (Table 3), Appendix D (prompt template)\n- 问题：LLM 无法从原始文本计算 perplexity statistics——这不是 LLM \"能力不足\"，而是 LLM 根本没有接触到 feature space。对比的本质是 \"能否从 surface text patterns 判断 depth\" vs \"能否从 perplexity distribution 判断 depth\"，这是两个不同的任务。Prompt 中给的 depth 描述（\"Rich vocabulary\"、\"Noticeable repetition\"）是人类可观察的 surface cues，但论文自己证明这些 lexical/repetition features 的 importance 远低于 perplexity tails。\n- 补充：(a) 0-shot、无 in-context examples；(b) 单一 prompt template 无 prompt engineering；(c) 仅 500 samples（CI width ≈ 4pp，尚可接受）。\n- 为什么影响接收：论文用 \"42pp gap\" 作为 RF vs LLM 的主要对比论据（Discussion 第一段），但这个对比在方法论上不成立。EMNLP 审稿标准要求 baseline 的公平性。\n- 建议修改方向：(a) 将 LLM baseline 重新定位为 \"surface-level feature upper bound\" 而非 \"baseline comparison\"——论证是 \"raw text alone 不含 depth signal，必须经过 reference model 映射\"；(b) 或给 LLM 提供 perplexity features 作为 context（tool-use / few-shot with features）；(c) 或加入 Ghostbuster-style feature-based binary detector 扩展为 ordinal 的 baseline。\n\n**N3** [critical] Cross-scale \"泛化\" 声明基于 N=2 个 confound-stacked 模型\n\n- 具体位置：§5.4, Table 6-7\n- 问题：仅 2 个 7B 模型，且一个 monotonic（Llama）一个 non-monotonic（Qwen），完全矛盾的行为模式。Confounds 叠加：(1) 4-bit NF4 QLoRA 量化噪声（1.4B 实验无量化）；(2) 均为 instruction-tuned（1.4B 实验为 base models）；(3) 仅 500 samples/depth（1.4B 用 5000）；(4) 仅 nucleus sampling（未测其他 strategy）。\n- 为什么影响接收：Contribution bullet 3 将 \"cross-scale to two 7B architectures\" 列为泛化贡献，但两个相互矛盾的 data points + 多重 confounds 无法支撑 \"scale generalization\"。\n- 建议修改方向：(a) 降级为 \"preliminary cross-scale observation\" 而非 \"generalization\"；(b) 明确列出 confound 清单并讨论每个可能的影响；(c) 至少加一个 base model at 7B scale（即使只有 500 samples）来解耦 instruction-tuning confound。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Feature importance \"universal marker\" claim 在极端多重共线性下可信度降低\n\n- 具体位置：§4.2, Table 2\n- 问题：VIF>10 for 14-16/19 features（§3.3）。在如此极端的共线性下，Gini importance 在相关特征间的分配是不稳定的——同组特征可能因 random split 而互换排名。论文用三种 importance method（Gini/SHAP/Permutation）的 concordance (Kendall's W=0.90) 作为证据，但这三种方法在高共线性下都有相似的 instability pattern，concordance 不能证明稳定性。\n- Forward selection（p90_ppl first in 6/9 cells）是更可信的证据，但不是 9/9。\n- 建议：(a) 在 feature group level 报告 importance（perplexity quantiles as group vs surprisal vs lexical vs repetition）；(b) 报告 conditional permutation importance（控制共线性后的重要性）；(c) 或弱化 \"universal marker\" 语言为 \"perplexity tail statistics group is universally dominant\"。\n\n**W2** [warning] Curation PoC 的统计检验不支持文中 claim\n\n- 具体位置：Appendix H, Table 9-10\n- 问题：rf_soft vs unfiltered: p=0.407; rf_moderate: p=0.492; rf_strict: p=0.607。所有 rf vs unfiltered 对比均不显著。Discussion 中 claim \"RF depth-based filtering matches unfiltered performance with 44% of the data\"——这是一个 null result（未能检测到差异），不是 positive finding。5 seeds 的 paired t-test 统计功效极低（df=4）。\n- 显著的 rf vs random 对比（p<0.05）可能仅反映 \"优先保留 d0/d1 = 保留更好的文本\"，而非 depth-specific 信息的独特价值。\n- 建议：(a) 增加 seeds 到 ≥20 以获得合理统计功效；(b) 加入 \"oracle d0+d1 only\" vs \"rf-predicted d0+d1\" 对比来解耦深度信息 vs 简单的 quality filtering；(c) 或降级为 \"inconclusive pilot\" 而非 \"proof-of-concept\"。\n\n**W3** [warning] C4 FPR 的 model gap (4.7% vs 22.4%) 缺乏统计检验\n\n- 具体位置：Appendix G, Table 8\n- 问题：OLMo (4.7%) vs GPT-2 XL (22.4%) 差异约 5×，但未报告任何统计检验（confidence interval, χ² test, 或 bootstrap comparison）。Training data composition 的解释是 post-hoc narrative，非 tested hypothesis。\n- WikiText vs C4 对比也缺乏可比性：editorial text vs web crawl 本身特征分布就不同，这不是 \"domain shift\" 的公平测试。\n- 建议：(a) 报告 FPR 的 95% CI（n=5000，Wilson interval）；(b) 对 model gap 做 McNemar's test 或 bootstrap comparison；(c) 对 C4 误分类 passages 做更系统的 error analysis（beyond \"template/SEO content\"）。\n\n**W4** [warning] BOS-seeded 无条件生成的生态效度问题\n\n- 具体位置：§3.2 (\"BOS-seeded, no prompt conditioning\")\n- 问题：真实的递归污染场景中，text 是 prompt-conditioned generation。无条件 BOS-seeded generation 产生的文本统计特性（更高 repetition、更低 coherence）可能人为放大了 depth signal。论文在 Limitations 中讨论了 \"controlled vs ecological setting\" 但未直接 address prompting。\n- 建议：至少讨论 BOS-seeded vs prompt-conditioned generation 可能如何影响 feature distribution，或加一个小规模 prompt-conditioned 对照实验。\n\n**W5** [warning] d0 inflates headline accuracy；abstract 中无足够 qualification\n\n- 具体位置：Abstract, §5.2 Table 4\n- 问题：Cross-model transfer \"66.4%\" 中 d0 recall=99.3%。排除 d0 后，d1-d3 balanced accuracy = 55.4%（chance=33.3%），仅 1.66× chance。Abstract 报告 \"cross-model transfer reaches 66.4%\" 未加 qualification。\n- 建议：Abstract 中加入 d1-d3 only metric（如 \"66.4% overall; 55.4% on generated-text depths, 1.7× chance\"）。\n\n---\n\n## 小问题（不影响接收）\n\n- §4.4 footnote: \"Our AUC profiles are empirically monotonically decreasing\" 但 Qwen2.5-7B 和 cross-strategy transfer 均违反此假设——footnote 应更新。\n- \"Classifier convergence ≤0.4pp\" (§5.1) 仅在 3/9 cells 验证，能否确认其余 6 cells？\n- Table 3 caption 说 \"RF values differ from Table 1 by ≤0.7pp due to matched-fold evaluation\"——建议用相同 fold split 统一两表。\n- §3.2: LoRA 的 architecture-specific targets 未详述（只说 \"architecture-specific targets\"）——对 reproducibility 重要。\n- EDD 定义中 $d^*+1$ 的 +1 offset 在首次阅读时容易混淆（EDD=4 意味着 depths 0-4 可区分，但 d*=3），建议加一个 worked example。\n\n---\n\n## Questions to Authors\n\n1. EDD₀.₇₅=4：如果只有 Pythia 达到统计显著性，是否应该用更保守的 threshold 或改为 \"EDD₀.₇₀=4 (all models significant)\"？\n2. 是否考虑过在 7B experiments 中使用 full fine-tuning（而非 QLoRA）来隔离量化 confound？或至少测试 8-bit vs 4-bit 的影响？\n3. Cross-model recursive chain (84.75%) 的 sample size 是多少？CI [81.0, 88.25] 的 width 暗示 n 较小。\n4. Forward selection 中 p90_ppl 仅在 6/9 cells 被首选——另外 3 cells 首选什么？这是否削弱 \"universal\" 的 claim？\n5. Curation PoC 中 oracle_strict 的 PPL 反而 worse than unfiltered ($\\Delta$=-0.103)——这是否意味着即使知道真实 depth，单纯过滤也不 work？\n\n---\n\n## Missing References\n\n- Guo et al., \"Curious Decline of Linguistic Diversity\" (2024) — 研究 LLM 输出的 lexical diversity 下降，与 depth-dependent diversity erosion 直接相关\n- Padmakumar & He, \"Does Writing with Language Models Reduce Content Diversity?\" (2024) — human-AI collaborative writing 的 diversity 分析\n- Briesch et al., \"Large Language Models Suffer From Their Own Output\" (2024) — 直接研究 model-on-model-output training\n\n---\n\n## 主要优势\n\n- **任务定义新颖**：从 binary detection 到 ordinal depth estimation 是一个有意义的 research direction，与 model collapse 文献形成自然互补\n- **系统性 atlas 设计**：3×3 grid 的实验设计允许分离 model effect 和 strategy effect\n- **Cross-model chain experiment**：84.75% accuracy 在 heterogeneous chain 上是强有力的 universality 证据\n- **诚实的 Limitations section**：主动报告 d0 inflation、cross-strategy inversion、ecological validity gap，显示学术诚信\n- **Domain bias analysis**（Appendix I）：发现并修正了 seed-group confound（报告了 bug fix 前后的数字），透明度高\n- **Feature hierarchy shift with depth**（§4.2 最后一段）：浅层 var_surprisal dominates、深层 p90_ppl takes over 的发现有理论意义\n\n---\n\n## Overall Assessment: 3.5/5\n\n核心贡献（task formalization + atlas + feature analysis）solid，但三个 critical issues（EDD 统计支撑、LLM baseline 公平性、cross-scale claim）需要在 revision 中 address。如果作者能 (1) 弱化/qualify EDD₀.₇₅=4 的 claim，(2) 重新定位 LLM baseline，(3) 降级 cross-scale 为 preliminary，本文可达到 EMNLP main conference 水平。当前状态更适合 Findings track。",
  "reviewer_id": "1",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿报告 — 方法严谨性 + 实验设计\n\n**论文**: \"How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\"\n**Venue**: EMNLP 2026 (ACL ARR May cycle)\n\n---\n\n## Paper Summary\n\n本文形式化了\"递归生成深度估计\"任务（ordinal classification），构建了 180K 样本的 3×3 benchmark（3 model families × 3 decoding strategies × 4 depths），提取 19 维统计特征（以 perplexity tail statistics 为主导），用 Random Forest 达到 70-85% 四分类准确率。引入 EDD metric 量化可区分深度前沿，发现 EDD₀.₇₅=4。进一步测试了 cross-model transfer、cross-strategy transfer、7B-scale 泛化等。\n\n---\n\n## 总体评分\n\n**Overall**: 3.5/5（介于 Findings track acceptance 和 Conference acceptance 之间）\n**一句话总结**: 任务新颖且系统性强，但几个关键 claim 的统计支撑不足（EDD₀.₇₅=4 的统计显著性、cross-scale N=2 的泛化声明、LLM baseline 的公平性），修订后可达 acceptance 水平。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 主要 claim 有支撑但部分 claim 统计证据不足（EDD、cross-scale） |\n| Excitement | 4/5 | 任务定义新颖且实用，与 model collapse 文献形成良好互补 |\n| Reproducibility | 4/5 | 特征定义、超参数、pipeline 描述充分；代码未公开但承诺 release |\n| Confidence | 4/5 | 熟悉统计方法论和 ML 实验设计，仔细核查了数值 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] EDD₀.₇₅=4 在 abstract 中作为通用结论呈现，但 GPT-2 XL 的统计证据不支持\n\n- 具体位置：Abstract line 6; §4.4 (\"bootstrap testing... p=0.505 for GPT-2 XL (non-significant)\")\n- 问题：Abstract 声称 \"finding EDD₀.₇₅=4 for extended recursion chains\"，但 §4.4 明确报告 GPT-2 XL 的 d3-vs-d4 AUC=0.750（恰好在阈值边界），bootstrap 检验 p=0.505（non-significant）。三个模型中只有 Pythia (p=0.001) 统计显著，OLMo (p=0.091) marginal，GPT-2 XL 不显著。用 \"graded confidence\" 修饰并不改变 abstract 中无条件陈述的问题。\n- 为什么影响接收：EDD 是本文核心创新指标之一，abstract 中的表述暗示这是一个 robust finding，但 1/3 模型不达显著性。\n- 建议修改方向：Abstract 改为 \"EDD₀.₇₅=4 for Pythia-1.4B (p=0.001); consistent direction across models but with graded statistical support (GPT-2 XL: p=0.505)\" 或使用更保守的 T=0.70（所有模型均>0.70 at d3v4）。\n\n**N2** [critical] Zero-shot LLM baseline 是结构性不公平对比（strawman）\n\n- 具体位置：§5.1 (Table 3), Appendix D (prompt template)\n- 问题：LLM 无法从原始文本计算 perplexity statistics——这不是 LLM \"能力不足\"，而是 LLM 根本没有接触到 feature space。对比的本质是 \"能否从 surface text patterns 判断 depth\" vs \"能否从 perplexity distribution 判断 depth\"，这是两个不同的任务。Prompt 中给的 depth 描述（\"Rich vocabulary\"、\"Noticeable repetition\"）是人类可观察的 surface cues，但论文自己证明这些 lexical/repetition features 的 importance 远低于 perplexity tails。\n- 补充：(a) 0-shot、无 in-context examples；(b) 单一 prompt template 无 prompt engineering；(c) 仅 500 samples（CI width ≈ 4pp，尚可接受）。\n- 为什么影响接收：论文用 \"42pp gap\" 作为 RF vs LLM 的主要对比论据（Discussion 第一段），但这个对比在方法论上不成立。EMNLP 审稿标准要求 baseline 的公平性。\n- 建议修改方向：(a) 将 LLM baseline 重新定位为 \"surface-level feature upper bound\" 而非 \"baseline comparison\"——论证是 \"raw text alone 不含 depth signal，必须经过 reference model 映射\"；(b) 或给 LLM 提供 perplexity features 作为 context（tool-use / few-shot with features）；(c) 或加入 Ghostbuster-style feature-based binary detector 扩展为 ordinal 的 baseline。\n\n**N3** [critical] Cross-scale \"泛化\" 声明基于 N=2 个 confound-stacked 模型\n\n- 具体位置：§5.4, Table 6-7\n- 问题：仅 2 个 7B 模型，且一个 monotonic（Llama）一个 non-monotonic（Qwen），完全矛盾的行为模式。Confounds 叠加：(1) 4-bit NF4 QLoRA 量化噪声（1.4B 实验无量化）；(2) 均为 instruction-tuned（1.4B 实验为 base models）；(3) 仅 500 samples/depth（1.4B 用 5000）；(4) 仅 nucleus sampling（未测其他 strategy）。\n- 为什么影响接收：Contribution bullet 3 将 \"cross-scale to two 7B architectures\" 列为泛化贡献，但两个相互矛盾的 data points + 多重 confounds 无法支撑 \"scale generalization\"。\n- 建议修改方向：(a) 降级为 \"preliminary cross-scale observation\" 而非 \"generalization\"；(b) 明确列出 confound 清单并讨论每个可能的影响；(c) 至少加一个 base model at 7B scale（即使只有 500 samples）来解耦 instruction-tuning confound。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Feature importance \"universal marker\" claim 在极端多重共线性下可信度降低\n\n- 具体位置：§4.2, Table 2\n- 问题：VIF>10 for 14-16/19 features（§3.3）。在如此极端的共线性下，Gini importance 在相关特征间的分配是不稳定的——同组特征可能因 random split 而互换排名。论文用三种 importance method（Gini/SHAP/Permutation）的 concordance (Kendall's W=0.90) 作为证据，但这三种方法在高共线性下都有相似的 instability pattern，concordance 不能证明稳定性。\n- Forward selection（p90_ppl first in 6/9 cells）是更可信的证据，但不是 9/9。\n- 建议：(a) 在 feature group level 报告 importance（perplexity quantiles as group vs surprisal vs lexical vs repetition）；(b) 报告 conditional permutation importance（控制共线性后的重要性）；(c) 或弱化 \"universal marker\" 语言为 \"perplexity tail statistics group is universally dominant\"。\n\n**W2** [warning] Curation PoC 的统计检验不支持文中 claim\n\n- 具体位置：Appendix H, Table 9-10\n- 问题：rf_soft vs unfiltered: p=0.407; rf_moderate: p=0.492; rf_strict: p=0.607。所有 rf vs unfiltered 对比均不显著。Discussion 中 claim \"RF depth-based filtering matches unfiltered performance with 44% of the data\"——这是一个 null result（未能检测到差异），不是 positive finding。5 seeds 的 paired t-test 统计功效极低（df=4）。\n- 显著的 rf vs random 对比（p<0.05）可能仅反映 \"优先保留 d0/d1 = 保留更好的文本\"，而非 depth-specific 信息的独特价值。\n- 建议：(a) 增加 seeds 到 ≥20 以获得合理统计功效；(b) 加入 \"oracle d0+d1 only\" vs \"rf-predicted d0+d1\" 对比来解耦深度信息 vs 简单的 quality filtering；(c) 或降级为 \"inconclusive pilot\" 而非 \"proof-of-concept\"。\n\n**W3** [warning] C4 FPR 的 model gap (4.7% vs 22.4%) 缺乏统计检验\n\n- 具体位置：Appendix G, Table 8\n- 问题：OLMo (4.7%) vs GPT-2 XL (22.4%) 差异约 5×，但未报告任何统计检验（confidence interval, χ² test, 或 bootstrap comparison）。Training data composition 的解释是 post-hoc narrative，非 tested hypothesis。\n- WikiText vs C4 对比也缺乏可比性：editorial text vs web crawl 本身特征分布就不同，这不是 \"domain shift\" 的公平测试。\n- 建议：(a) 报告 FPR 的 95% CI（n=5000，Wilson interval）；(b) 对 model gap 做 McNemar's test 或 bootstrap comparison；(c) 对 C4 误分类 passages 做更系统的 error analysis（beyond \"template/SEO content\"）。\n\n**W4** [warning] BOS-seeded 无条件生成的生态效度问题\n\n- 具体位置：§3.2 (\"BOS-seeded, no prompt conditioning\")\n- 问题：真实的递归污染场景中，text 是 prompt-conditioned generation。无条件 BOS-seeded generation 产生的文本统计特性（更高 repetition、更低 coherence）可能人为放大了 depth signal。论文在 Limitations 中讨论了 \"controlled vs ecological setting\" 但未直接 address prompting。\n- 建议：至少讨论 BOS-seeded vs prompt-conditioned generation 可能如何影响 feature distribution，或加一个小规模 prompt-conditioned 对照实验。\n\n**W5** [warning] d0 inflates headline accuracy；abstract 中无足够 qualification\n\n- 具体位置：Abstract, §5.2 Table 4\n- 问题：Cross-model transfer \"66.4%\" 中 d0 recall=99.3%。排除 d0 后，d1-d3 balanced accuracy = 55.4%（chance=33.3%），仅 1.66× chance。Abstract 报告 \"cross-model transfer reaches 66.4%\" 未加 qualification。\n- 建议：Abstract 中加入 d1-d3 only metric（如 \"66.4% overall; 55.4% on generated-text depths, 1.7× chance\"）。\n\n---\n\n## 小问题（不影响接收）\n\n- §4.4 footnote: \"Our AUC profiles are empirically monotonically decreasing\" 但 Qwen2.5-7B 和 cross-strategy transfer 均违反此假设——footnote 应更新。\n- \"Classifier convergence ≤0.4pp\" (§5.1) 仅在 3/9 cells 验证，能否确认其余 6 cells？\n- Table 3 caption 说 \"RF values differ from Table 1 by ≤0.7pp due to matched-fold evaluation\"——建议用相同 fold split 统一两表。\n- §3.2: LoRA 的 architecture-specific targets 未详述（只说 \"architecture-specific targets\"）——对 reproducibility 重要。\n- EDD 定义中 $d^*+1$ 的 +1 offset 在首次阅读时容易混淆（EDD=4 意味着 depths 0-4 可区分，但 d*=3），建议加一个 worked example。\n\n---\n\n## Questions to Authors\n\n1. EDD₀.₇₅=4：如果只有 Pythia 达到统计显著性，是否应该用更保守的 threshold 或改为 \"EDD₀.₇₀=4 (all models significant)\"？\n2. 是否考虑过在 7B experiments 中使用 full fine-tuning（而非 QLoRA）来隔离量化 confound？或至少测试 8-bit vs 4-bit 的影响？\n3. Cross-model recursive chain (84.75%) 的 sample size 是多少？CI [81.0, 88.25] 的 width 暗示 n 较小。\n4. Forward selection 中 p90_ppl 仅在 6/9 cells 被首选——另外 3 cells 首选什么？这是否削弱 \"universal\" 的 claim？\n5. Curation PoC 中 oracle_strict 的 PPL 反而 worse than unfiltered ($\\Delta$=-0.103)——这是否意味着即使知道真实 depth，单纯过滤也不 work？\n\n---\n\n## Missing References\n\n- Guo et al., \"Curious Decline of Linguistic Diversity\" (2024) — 研究 LLM 输出的 lexical diversity 下降，与 depth-dependent diversity erosion 直接相关\n- Padmakumar & He, \"Does Writing with Language Models Reduce Content Diversity?\" (2024) — human-AI collaborative writing 的 diversity 分析\n- Briesch et al., \"Large Language Models Suffer From Their Own Output\" (2024) — 直接研究 model-on-model-output training\n\n---\n\n## 主要优势\n\n- **任务定义新颖**：从 binary detection 到 ordinal depth estimation 是一个有意义的 research direction，与 model collapse 文献形成自然互补\n- **系统性 atlas 设计**：3×3 grid 的实验设计允许分离 model effect 和 strategy effect\n- **Cross-model chain experiment**：84.75% accuracy 在 heterogeneous chain 上是强有力的 universality 证据\n- **诚实的 Limitations section**：主动报告 d0 inflation、cross-strategy inversion、ecological validity gap，显示学术诚信\n- **Domain bias analysis**（Appendix I）：发现并修正了 seed-group confound（报告了 bug fix 前后的数字），透明度高\n- **Feature hierarchy shift with depth**（§4.2 最后一段）：浅层 var_surprisal dominates、深层 p90_ppl takes over 的发现有理论意义\n\n---\n\n## Overall Assessment: 3.5/5\n\n核心贡献（task formalization + atlas + feature analysis）solid，但三个 critical issues（EDD 统计支撑、LLM baseline 公平性、cross-scale claim）需要在 revision 中 address。如果作者能 (1) 弱化/qualify EDD₀.₇₅=4 的 claim，(2) 重新定位 LLM baseline，(3) 降级 cross-scale 为 preliminary，本文可达到 EMNLP main conference 水平。当前状态更适合 Findings track。",
    "reviewer_id": "1",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 139 · 2026-05-16T12:09:43.669910+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3814
}
```

</details>

---


### Assistant

_source line 140 · 2026-05-16T12:09:50.945419+00:00_

审稿报告已提交给 Review Director。

总结：评分 Overall 3.5/5（Findings track / borderline main conference）。识别出 3 个 Must-Fix 问题：(1) EDD₀.₇₅=4 的 abstract claim 在 GPT-2 XL 上 p=0.505 不显著；(2) Zero-shot LLM baseline 是结构性不公平对比（LLM 无法访问 perplexity feature space）；(3) Cross-scale "泛化" 仅基于 2 个 confound-stacked 的 instruction-tuned 7B 模型。另有 5 个 Should-Fix：feature importance 在极端共线性下的稳定性、Curation PoC 全部 non-significant、C4 FPR gap 无统计检验、BOS-seeded 生态效度、d0 inflation 未在 abstract 充分 qualify。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1"
}
```

</details>

---


## Round 6

## Round 6

4 recorded events


### User

_source line 141 · 2026-05-16T12:14:43.754411+00:00_

[Round 1 审稿请求]:
## 交叉分享 — Reviewer 2 的完整审稿意见

以下是 Reviewer 2 的完整审稿报告。请逐条回应每个 Must-Fix 和 Should-Fix：
- **[AGREE]** — 同意该观点并说明理由
- **[REBUT]** — 反驳并提供具体证据（cite 论文中的 Section/Table/Figure）

---

## Reviewer 2 审稿意见：新颖性 + 完整性 + 写作质量

**Overall**: 3.0 / 5（Findings acceptance）
**一句话总结**: 定义了一个有实际意义的新任务并进行了系统实验，但核心方法论新颖性有限（标准特征+标准分类器），且最强 claims 与最难实验设置的结果存在显著落差。

### Must-Fix 问题

**N1** [critical] Abstract headline number (70.30%) 来源不清
- Abstract 宣称 "A Random Forest classifier achieves 70.30% four-class accuracy"，但 Table 2 中 9 个 cell 范围为 69.6%–85.4%。70.30% 不对应任何单个 cell 也不是简单平均。

**N2** [critical] 新颖性不足以支撑长文接收
- 核心方法是 "从 reference model 提取 19 个标准统计特征 → Random Forest 分类"。无新算法、模型或理论框架。"Depth Degradation Atlas" 本质是参数网格评估，"EDD" 是 pairwise AUC threshold cutoff。

**N3** [critical] Claims 与 Evidence 存在系统性落差
- "universal" 仅在 3+2 个模型上验证
- Cross-strategy 59.1% 被框架为 "generalization" 但接近 2× chance
- Cross-model d2 recall 最低 26.8% 说明中间 depth 判别能力极弱
- Qwen2.5-7B 60.1% 远低于 1-1.5B 的 70-85%

### Should-Fix 问题

**W1** Abstract 与正文数值不一致（cross-model chains 84.72% vs 84.75% vs 84.7%；cross-model transfer 66.8% vs 66.4%；feature dominance P90 vs P50 混淆）

**W2** d0 inflation 未在 abstract 充分体现（三分类 58.8%-82.6%，cross-model d2 recall 低至 26.8%）

**W3** Cross-model recursive chains (84.75%) 的"泛化"解读有误导性——heterogeneous chains 天然比 homogeneous chains 更容易分类（architecture difference + depth difference 叠加）

**W4** Curation PoC 证据不足（无 DSIR/QuRating 对比，无多任务验证，无 threshold 消融）

**W5** 生态效度不足——benchmark 使用 Wikipedia seed + controlled LoRA，但 framing 暗示 deployment readiness

### 缺失引用
1. Self-play / iterative self-improvement 文献（SPIN 等）
2. Seddik et al. 2025 "How Bad is Training on Synthetic Data?"

### 小问题
- Abstract 信息密度过高（15+ 数字）
- "Depth Degradation Atlas" 命名过于 marketing
- Table 3 Pythia top-k 60.9% vs Table 2 同 cell 69.6% 差异
- `falahati2026_curated` 引用真实性存疑
- 与 Mohamed et al. (2025) "Broken Telephone" 区别仅一句——建议扩展

---

请对以上每个 Must-Fix (N1-N3) 和 Should-Fix (W1-W5) 逐条给出 [AGREE] 或 [REBUT]，附理由。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 142 · 2026-05-16T12:16:44.220302+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 意见的交叉回应\n\n---\n\n### Must-Fix 逐条回应\n\n**[REBUT] R2-N1: Abstract headline number \"70.30%\" 来源不清**\n\nAbstract 原文为 \"achieves 70--85\\% four-class accuracy\"（即范围表示），对应 Table 2 的 69.6%–85.4%（四舍五入）。Abstract 中并无 \"70.30%\" 这一数字。R2 可能将 LaTeX 中的 en-dash \"70--85\" 误读为 \"70.30\"，或将 §5.4 中 Llama-3.1-8B 的 \"70.2%\" 与主实验结果混淆。\n\n但 R2 的底层关切有一定道理：abstract 中数字密度过高（15+ 数字），增加了误读风险。建议作者精简 abstract 中的数值，但这属于 presentation issue 而非 factual error——不构成 critical 级问题。\n\n**[AGREE] R2-N2: 新颖性有限**\n\n同意 R2 的核心观察：方法层面是 \"标准特征 + 标准分类器\"，无新算法或理论框架。然而我对严重程度的评估与 R2 有分歧：\n\nEMNLP 历来接收 \"novel task + systematic empirical contribution\" 型论文（例如 SemEval shared tasks, dataset papers, empirical analysis papers）。本文的新颖性主要在于：(1) task formalization（将 binary detection 扩展为 ordinal depth estimation）；(2) 系统性发现（feature hierarchy shift across depths, strategy-dependent trajectories）；(3) EDD metric 虽简单但填补了量化空白。\n\n关键在于 findings 是否 non-trivial。我认为以下发现确实非 obvious：\n- Decoding strategy 对 degradation trajectory 的 qualitative reshaping（§4.5: temperature accelerates, top-k attenuates）\n- Feature hierarchy 随 depth 转换（shallow: var_surprisal dominates → deep: p90_ppl takes over, §4.2）\n- Cross-model chain 84.75% 证明 signal 是 process property\n\n**结论**：新颖性确实不足以作为 algorithmic contribution 论文，但作为 empirical/task-definition contribution 论文可以成立。不构成 reject 理由，但降低了 excitement score（我给 4/5 可能偏高，3.5/5 更合理）。\n\n**[AGREE] R2-N3: Claims 与 Evidence 的系统性落差**\n\n完全同意。我在自己的审稿中也独立提出了相同问题：\n\n1. **\"universal\"**: 仅 3 个 1.4B base models + 2 个 7B instruction-tuned models，且 7B 结果相互矛盾（Llama monotonic vs Qwen non-monotonic）。\"Universal\" 一词使用过度——应改为 \"consistent across the studied models\" 或 \"within our experimental scope\"。\n\n2. **Cross-strategy 59.1%**: 同意 R2 的评估。排除 d0 后 d1-d3 accuracy = 45.9%（chance=33.3%），仅 1.38× chance。论文将此框架为 \"generalization\" 但实际效果很弱，且 §6 Discussion 明确承认 \"cross-strategy transfer remains the primary bottleneck\" 和 \"single-classifier deployment across unknown decoding strategies infeasible\"——这与 Introduction 的 framing 存在张力。\n\n3. **Cross-model d2 recall 26.8%**: Pythia holdout (Table 4) 确实显示 d2 recall 仅 26.8%。加上 cross-strategy temperature holdout 的 d2 recall 低至 3.7%（§5.3），中间 depth 的判别能力在 transfer 设定下接近 random。\n\n4. **Qwen 60.1%**: CI lower bound 58.0% 距离 chance (25%) 仍有实质差距，但距离 \"useful system\" 同样遥远。\n\n补充我自己的观察：Introduction (§1) bullet 3 将 7 axes of generalization 作为贡献，但其中多数 axis 的 performance 远低于 in-distribution，framing 与 evidence 确实存在落差。\n\n---\n\n### Should-Fix 逐条回应\n\n**[REBUT] R2-W1: 数值不一致（84.72% vs 84.75% vs 84.7%；66.8% vs 66.4%）**\n\n在我阅读的版本中：\n- Cross-model chains: Abstract 和 Appendix K 均为 \"84.75%\"（CI [81.0, 88.25]）。未找到 \"84.72%\" 或 \"84.7%\" 出处。\n- Cross-model transfer: Table 4 mean = 66.4%, Abstract = \"66.4%\"。未找到 \"66.8%\"。\n- P90 vs P50 混淆：Table 2 明确 p90_ppl top-2 in 9/9（Gini）。未观察到与 P50 的混淆。\n\n可能 R2 基于早期版本审稿，或编译渲染导致误读。建议作者确认 final version 的数值一致性，但基于我所读版本，这些不一致 **不成立**。不过 R2 提到的 Table 3 Pythia top-k \"60.9%\" vs Table 2 同 cell \"69.6%\" 差异——我在 Table 3 (tab:baselines) 中看到 Pythia top-k = 68.9%（非 60.9%）。R2 可能有笔误。\n\n**[AGREE] R2-W2: d0 inflation 未在 abstract 充分体现**\n\n完全同意，与我的 W5 一致。Abstract 括号中确实给出了 d1-d3 三分类范围（58.8-82.6%），这是部分 disclosure，但 cross-model/cross-strategy 的 headline numbers 仍受 d0 inflation 影响且未加 qualification。建议 abstract 对所有 transfer 结果加注 \"(d1-d3 only: X%)\"。\n\n**[AGREE] R2-W3: Cross-model recursive chains 84.75% 的 \"泛化\" 解读有误导**\n\n这是我审稿时**未充分考虑**的角度。R2 指出 heterogeneous chain（d1=Pythia, d2=OLMo, d3=GPT-2 XL）中，分类器可能部分依赖 architecture-specific perplexity fingerprints（不同模型的 baseline perplexity distribution 天然不同），而非纯粹的 depth signal。\n\n具体分析：Features 是 Pythia-1.4B reference model 对各 depth text 计算的 perplexity statistics。OLMo-generated text (d2) 和 GPT-2-XL-generated text (d3) 在 Pythia reference 下的 perplexity profile 可能本身就有 architecture-dependent 差异，与 depth 无关。这是一个 confound——84.75% 可能反映 \"depth + architecture identity\" 的联合信号，而非 pure depth signal。\n\n论文的论证逻辑是 \"if depth signal were model-specific, it wouldn't persist across model boundaries\"，但实验设计恰好将 model identity 与 depth 完全 confound（d1 永远是 Pythia, d2 永远是 OLMo...）。要真正证明 \"depth signal is process-level\"，需要 **randomize** which model generates which depth，或比较同一 architecture 单模型 chain vs 异构 chain 的 AUC profiles。\n\n**建议**：这一点显著削弱了论文 Contribution bullet 3 的 claim force。应在正文中加入此 confound 的讨论。\n\n**[AGREE] R2-W4: Curation PoC 证据不足**\n\n同意，与我的 W2 一致。补充：\n- 无 DSIR/QuRating 对比确实是缺陷——这些是 data curation 的 standard baselines\n- rf vs unfiltered 全部 non-significant（p>0.4），claim 本质是 null result\n- 5 seeds 的统计功效不足以检测 ~0.04 PPL 的微小效应\n- 缺 threshold 消融（只测了 strict/moderate/soft 三个点）\n\n**[AGREE] R2-W5: 生态效度不足**\n\n同意，与我的 W4（BOS-seeded generation）一致。论文在 Limitations 中有 partial acknowledgment，但 Introduction 和 Discussion 的 framing（\"early-warning signal for model collapse\"、\"provenance toolkit\"、\"depth-graduated curation\"）暗示了远超实验支撑的 deployment readiness。建议弱化 deployment-oriented framing 或加入更多 caveats。\n\n---\n\n### 对 R2 小问题的简评\n\n- **Abstract 信息密度过高**: 同意。15+ 数字确实 overloads reader。\n- **\"Depth Degradation Atlas\" 命名**: 不同意这是问题。学术论文命名概念性框架是常见做法（\"Scaling Laws\"、\"Chinchilla\"、\"Constitutional AI\"），不构成 marketing。\n- **Table 3 差异**: R2 说 \"60.9%\"，我在 Table 3 中看到的是 68.9%。R2 可能有笔误或版本差异。\n- **falahati2026_curated 引用真实性**: 我未验证此引用，建议 Director 可用 verify_references 工具检查。\n- **Mohamed et al. (2025) 区别**: 同意应扩展讨论——\"Broken Telephone\" 研究 forward degradation measurement，本文做 inverse estimation，一句话不够。\n\n---\n\n### 综合判断\n\nR2 的三个 Must-Fix 中：\n- N1 基于对 abstract 的误读（REBUT）\n- N2 关于新颖性的判断 partially valid 但不构成 reject（AGREE with caveats）\n- N3 关于 claims/evidence gap 是正确且重要的（AGREE）\n\nR2 的 Should-Fix 中 W3（cross-model chain confound）是我审稿时遗漏的有价值观点，我更新对此 issue 的评估：应提升为 Should-Fix（影响 Contribution bullet 3 的 claim）。\n\n我维持 Overall 3.5/5 不变——R2 的意见 reinforce 了我对 claim calibration 的担忧，但未暴露新的 fatal flaw。",
  "reviewer_id": "1",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 意见的交叉回应\n\n---\n\n### Must-Fix 逐条回应\n\n**[REBUT] R2-N1: Abstract headline number \"70.30%\" 来源不清**\n\nAbstract 原文为 \"achieves 70--85\\% four-class accuracy\"（即范围表示），对应 Table 2 的 69.6%–85.4%（四舍五入）。Abstract 中并无 \"70.30%\" 这一数字。R2 可能将 LaTeX 中的 en-dash \"70--85\" 误读为 \"70.30\"，或将 §5.4 中 Llama-3.1-8B 的 \"70.2%\" 与主实验结果混淆。\n\n但 R2 的底层关切有一定道理：abstract 中数字密度过高（15+ 数字），增加了误读风险。建议作者精简 abstract 中的数值，但这属于 presentation issue 而非 factual error——不构成 critical 级问题。\n\n**[AGREE] R2-N2: 新颖性有限**\n\n同意 R2 的核心观察：方法层面是 \"标准特征 + 标准分类器\"，无新算法或理论框架。然而我对严重程度的评估与 R2 有分歧：\n\nEMNLP 历来接收 \"novel task + systematic empirical contribution\" 型论文（例如 SemEval shared tasks, dataset papers, empirical analysis papers）。本文的新颖性主要在于：(1) task formalization（将 binary detection 扩展为 ordinal depth estimation）；(2) 系统性发现（feature hierarchy shift across depths, strategy-dependent trajectories）；(3) EDD metric 虽简单但填补了量化空白。\n\n关键在于 findings 是否 non-trivial。我认为以下发现确实非 obvious：\n- Decoding strategy 对 degradation trajectory 的 qualitative reshaping（§4.5: temperature accelerates, top-k attenuates）\n- Feature hierarchy 随 depth 转换（shallow: var_surprisal dominates → deep: p90_ppl takes over, §4.2）\n- Cross-model chain 84.75% 证明 signal 是 process property\n\n**结论**：新颖性确实不足以作为 algorithmic contribution 论文，但作为 empirical/task-definition contribution 论文可以成立。不构成 reject 理由，但降低了 excitement score（我给 4/5 可能偏高，3.5/5 更合理）。\n\n**[AGREE] R2-N3: Claims 与 Evidence 的系统性落差**\n\n完全同意。我在自己的审稿中也独立提出了相同问题：\n\n1. **\"universal\"**: 仅 3 个 1.4B base models + 2 个 7B instruction-tuned models，且 7B 结果相互矛盾（Llama monotonic vs Qwen non-monotonic）。\"Universal\" 一词使用过度——应改为 \"consistent across the studied models\" 或 \"within our experimental scope\"。\n\n2. **Cross-strategy 59.1%**: 同意 R2 的评估。排除 d0 后 d1-d3 accuracy = 45.9%（chance=33.3%），仅 1.38× chance。论文将此框架为 \"generalization\" 但实际效果很弱，且 §6 Discussion 明确承认 \"cross-strategy transfer remains the primary bottleneck\" 和 \"single-classifier deployment across unknown decoding strategies infeasible\"——这与 Introduction 的 framing 存在张力。\n\n3. **Cross-model d2 recall 26.8%**: Pythia holdout (Table 4) 确实显示 d2 recall 仅 26.8%。加上 cross-strategy temperature holdout 的 d2 recall 低至 3.7%（§5.3），中间 depth 的判别能力在 transfer 设定下接近 random。\n\n4. **Qwen 60.1%**: CI lower bound 58.0% 距离 chance (25%) 仍有实质差距，但距离 \"useful system\" 同样遥远。\n\n补充我自己的观察：Introduction (§1) bullet 3 将 7 axes of generalization 作为贡献，但其中多数 axis 的 performance 远低于 in-distribution，framing 与 evidence 确实存在落差。\n\n---\n\n### Should-Fix 逐条回应\n\n**[REBUT] R2-W1: 数值不一致（84.72% vs 84.75% vs 84.7%；66.8% vs 66.4%）**\n\n在我阅读的版本中：\n- Cross-model chains: Abstract 和 Appendix K 均为 \"84.75%\"（CI [81.0, 88.25]）。未找到 \"84.72%\" 或 \"84.7%\" 出处。\n- Cross-model transfer: Table 4 mean = 66.4%, Abstract = \"66.4%\"。未找到 \"66.8%\"。\n- P90 vs P50 混淆：Table 2 明确 p90_ppl top-2 in 9/9（Gini）。未观察到与 P50 的混淆。\n\n可能 R2 基于早期版本审稿，或编译渲染导致误读。建议作者确认 final version 的数值一致性，但基于我所读版本，这些不一致 **不成立**。不过 R2 提到的 Table 3 Pythia top-k \"60.9%\" vs Table 2 同 cell \"69.6%\" 差异——我在 Table 3 (tab:baselines) 中看到 Pythia top-k = 68.9%（非 60.9%）。R2 可能有笔误。\n\n**[AGREE] R2-W2: d0 inflation 未在 abstract 充分体现**\n\n完全同意，与我的 W5 一致。Abstract 括号中确实给出了 d1-d3 三分类范围（58.8-82.6%），这是部分 disclosure，但 cross-model/cross-strategy 的 headline numbers 仍受 d0 inflation 影响且未加 qualification。建议 abstract 对所有 transfer 结果加注 \"(d1-d3 only: X%)\"。\n\n**[AGREE] R2-W3: Cross-model recursive chains 84.75% 的 \"泛化\" 解读有误导**\n\n这是我审稿时**未充分考虑**的角度。R2 指出 heterogeneous chain（d1=Pythia, d2=OLMo, d3=GPT-2 XL）中，分类器可能部分依赖 architecture-specific perplexity fingerprints（不同模型的 baseline perplexity distribution 天然不同），而非纯粹的 depth signal。\n\n具体分析：Features 是 Pythia-1.4B reference model 对各 depth text 计算的 perplexity statistics。OLMo-generated text (d2) 和 GPT-2-XL-generated text (d3) 在 Pythia reference 下的 perplexity profile 可能本身就有 architecture-dependent 差异，与 depth 无关。这是一个 confound——84.75% 可能反映 \"depth + architecture identity\" 的联合信号，而非 pure depth signal。\n\n论文的论证逻辑是 \"if depth signal were model-specific, it wouldn't persist across model boundaries\"，但实验设计恰好将 model identity 与 depth 完全 confound（d1 永远是 Pythia, d2 永远是 OLMo...）。要真正证明 \"depth signal is process-level\"，需要 **randomize** which model generates which depth，或比较同一 architecture 单模型 chain vs 异构 chain 的 AUC profiles。\n\n**建议**：这一点显著削弱了论文 Contribution bullet 3 的 claim force。应在正文中加入此 confound 的讨论。\n\n**[AGREE] R2-W4: Curation PoC 证据不足**\n\n同意，与我的 W2 一致。补充：\n- 无 DSIR/QuRating 对比确实是缺陷——这些是 data curation 的 standard baselines\n- rf vs unfiltered 全部 non-significant（p>0.4），claim 本质是 null result\n- 5 seeds 的统计功效不足以检测 ~0.04 PPL 的微小效应\n- 缺 threshold 消融（只测了 strict/moderate/soft 三个点）\n\n**[AGREE] R2-W5: 生态效度不足**\n\n同意，与我的 W4（BOS-seeded generation）一致。论文在 Limitations 中有 partial acknowledgment，但 Introduction 和 Discussion 的 framing（\"early-warning signal for model collapse\"、\"provenance toolkit\"、\"depth-graduated curation\"）暗示了远超实验支撑的 deployment readiness。建议弱化 deployment-oriented framing 或加入更多 caveats。\n\n---\n\n### 对 R2 小问题的简评\n\n- **Abstract 信息密度过高**: 同意。15+ 数字确实 overloads reader。\n- **\"Depth Degradation Atlas\" 命名**: 不同意这是问题。学术论文命名概念性框架是常见做法（\"Scaling Laws\"、\"Chinchilla\"、\"Constitutional AI\"），不构成 marketing。\n- **Table 3 差异**: R2 说 \"60.9%\"，我在 Table 3 中看到的是 68.9%。R2 可能有笔误或版本差异。\n- **falahati2026_curated 引用真实性**: 我未验证此引用，建议 Director 可用 verify_references 工具检查。\n- **Mohamed et al. (2025) 区别**: 同意应扩展讨论——\"Broken Telephone\" 研究 forward degradation measurement，本文做 inverse estimation，一句话不够。\n\n---\n\n### 综合判断\n\nR2 的三个 Must-Fix 中：\n- N1 基于对 abstract 的误读（REBUT）\n- N2 关于新颖性的判断 partially valid 但不构成 reject（AGREE with caveats）\n- N3 关于 claims/evidence gap 是正确且重要的（AGREE）\n\nR2 的 Should-Fix 中 W3（cross-model chain confound）是我审稿时遗漏的有价值观点，我更新对此 issue 的评估：应提升为 Should-Fix（影响 Contribution bullet 3 的 claim）。\n\n我维持 Overall 3.5/5 不变——R2 的意见 reinforce 了我对 claim calibration 的担忧，但未暴露新的 fatal flaw。",
    "reviewer_id": "1",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 143 · 2026-05-16T12:16:48.183444+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3963
}
```

</details>

---


### Assistant

_source line 144 · 2026-05-16T12:16:56.565868+00:00_

已提交交叉回应。总结：

- **N1 (70.30% 来源不清)**: REBUT — abstract 原文是 "70--85%" 范围表示，R2 可能误读
- **N2 (新颖性不足)**: AGREE with caveats — 方法层面确实标准，但 task+empirical contribution 在 EMNLP 可以成立
- **N3 (Claims/Evidence 落差)**: AGREE — 与我独立提出的 N3 (cross-scale) 和 W5 (d0 inflation) 一致
- **W1 (数值不一致)**: REBUT — 在我所读版本中未发现 R2 所列的不一致
- **W2 (d0 inflation)**: AGREE
- **W3 (cross-model chain confound)**: AGREE — R2 指出了我遗漏的重要 confound (architecture identity confounded with depth)
- **W4 (Curation PoC)**: AGREE
- **W5 (生态效度)**: AGREE

维持 Overall 3.5/5 不变。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1"
}
```

</details>

---


## Round 7

## Round 7

68 recorded events


### User

_source line 145 · 2026-05-16T17:16:03.689324+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）

**论文**：How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
**路径**：projects/recursive_gen_depth_est/docs/paper/main.tex
**Venue**���EMNLP 2026 Main Conference (ARR May cycle)
**格式要求**：ACL 模板，8页正文 + unlimited references，Limitations 不计入页数，double-blind
**Deadline**：2026-05-25

### 你的审查侧重

1. **形式化定义的严谨性**：
   - EDD 定义（Definition 1）是否数学上无歧义？边界条件是否完备？
   - Recursive generation chain 的形式化是否准确覆盖了实际的 model collapse 场景？
   - Ordinal classification 的 problem setup 是否自洽？

2. **Benchmark 构造**：
   - 180K 样本的生成协议是否有信息泄露风险？
   - LoRA finetuning 参数选择（r=16, α=32, 3 epochs）是否合理？是否会引入confound？
   - Reference model 选择（Pythia-1.4B 既是 generator 又是 reference）的 circularity 问题

3. **统计检验与实验方法**：
   - Bootstrap testing 的 sample size 和 resample count 是否足够？
   - 5-fold CV 是否适合这种数据结构？是否存在 temporal/group leakage？
   - Cross-model/cross-strategy transfer 实验是否有系统性偏差？
   - Pairwise AUC 用独立 binary classifier 的合理性

4. **消融实验**：
   - Feature ablation 是否充分（top-2/top-5 vs full-19）？
   - VIF 分析揭示 14-16/19 特征高度共线性——这对模型解释性有何影响？
   - Classifier comparison (RF vs XGB vs LGBM ≤0.4pp) 是否意味着 feature ceiling？

5. **Cross-scale 实验的局限性**：
   - 500 samples vs 5000 samples 的 statistical power 差异
   - 4-bit QLoRA 量化对 perplexity distribution 的潜在影响
   - 仅两个 7B 模型能否支撑 cross-scale 结论？

请按 ACL reviewer 标准给出：Summary → Strengths → Weaknesses → Questions → Minor Issues → Overall Score (1-5)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 146 · 2026-05-16T17:16:26.847198+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
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

_source line 147 · 2026-05-16T17:16:26.897910+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 148 · 2026-05-16T17:16:27.249630+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
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

_source line 149 · 2026-05-16T17:16:27.300195+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 150 · 2026-05-16T17:16:33.634471+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 151 · 2026-05-16T17:16:35.042023+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 152 · 2026-05-16T17:16:35.092716+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 153 · 2026-05-16T17:16:41.827983+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

I've found comprehensive information about ACL ARR reviewer guidelines and review form criteria for 2025-2026. Here are the key findings:

## Reviewer Scoring (Updated February 2025)

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores mus
…[truncated 1402 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8193
}
```

</details>

---


### Tool call

_source line 154 · 2026-05-16T17:16:48.810246+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5 etc.), and descriptions for each score level. I need the exact scoring rubric for soundness, excitement, overall recommendation, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5 etc.), and descriptions for each score level. I need the exact scoring rubric for soundness, excitement, overall recommendation, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 155 · 2026-05-16T17:16:49.515789+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
  "pages": "1-5",
  "dpi": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
    "pages": "1-5",
    "dpi": "200"
  }
}
```

</details>

---


### Tool result

_source line 156 · 2026-05-16T17:16:55.753216+00:00_

# ACL Rolling Review Form - Complete Scoring Rubric

## Reviewer Confidence
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## Soundness
Scale: 1-5 (with .5 increments)
- **5**: "Excellent: This study is one of the most thorough I have seen."
- **4**: "Strong: This study provides sufficient support for all claims."
- **3**: "Acceptable: This study provides sufficient support for main claims."
- **2**: "Poor: Some main claims are not sufficiently supported."
- **1**: "Major Issues: Not sufficiently thorough to warrant publication."

## Excitement
Scale: 1-5 (with .5 increments)
- **5**: "Highly Exciting: I would recommend this paper to others."
- **4**: "Exciting: I would mention this paper to others."
- **3**: "Interesting: I might mention some points to others."
- **2**: "Potentially Interesting: does not resonate with me."
- **1**: "Not Exciting: does not resonate with me or the community."

## Overall Assessment
Scale: 1-5 (with .5 increments)
- **5**: "Consider for Award: could be outstanding (top 2.5%)"
- **4**: "Conference: could be accepted"
- **3**: "Findings: could be accepted to Findings"
- **2**: "Resubmit next cycle: needs substantial revisions"
- **1**: "Do not resubmit: must be fully redone"

## Reproducibility
Scale: 1-5
- **5**: "They could easily reproduce the results."
- **4**: "They could mostly reproduce results."
- **3**: "They could reproduce with some difficulty."
- **2**: "They would be hard pressed to reproduce."
- **1**: "They would not be able to reproduce."

## Datasets & Software
Scale: 1-5 (identical for both)
- **5**: "Enabling: should affect others' research choices
…[truncated 201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6942
}
```

</details>

---


### Tool result

_source line 157 · 2026-05-16T17:16:58.149523+00:00_

Error: result (4,518,979 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/b8e5b5cf-ef3b-4d99-826e-9cb76f03f4d4/tool-results/mcp-agent-ml-research-pdf_to_images-1778951817906.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/b8e5b5cf-ef3b-4d99-826e-9cb76f03f4d4/tool-results/mcp-agent-ml-research-pdf_to_images-1778951817906.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/b8e5b5cf-ef3b-4d99-826e-9cb76f03f4d4/tool-results/mcp-agent-ml-research-pdf_to_images-1778951817906.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 8633
}
```

</details>

---


### Tool call

_source line 158 · 2026-05-16T17:17:11.527056+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
  "pages": "1",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
    "pages": "1",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 159 · 2026-05-16T17:17:11.984850+00:00_

Error: result (627,343 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/b8e5b5cf-ef3b-4d99-826e-9cb76f03f4d4/tool-results/mcp-agent-ml-research-pdf_to_images-1778951831921.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/b8e5b5cf-ef3b-4d99-826e-9cb76f03f4d4/tool-results/mcp-agent-ml-research-pdf_to_images-1778951831921.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/b8e5b5cf-ef3b-4d99-826e-9cb76f03f4d4/tool-results/mcp-agent-ml-research-pdf_to_images-1778951831921.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 457
}
```

</details>

---


### Tool call

_source line 160 · 2026-05-16T17:17:12.487152+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
  "pages": "2",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
    "pages": "2",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 161 · 2026-05-16T17:17:12.838926+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
  "pages": "3",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
    "pages": "3",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 162 · 2026-05-16T17:17:13.047740+00:00_

Error: result (749,435 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/b8e5b5cf-ef3b-4d99-826e-9cb76f03f4d4/tool-results/mcp-agent-ml-research-pdf_to_images-1778951832982.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/b8e5b5cf-ef3b-4d99-826e-9cb76f03f4d4/tool-results/mcp-agent-ml-research-pdf_to_images-1778951832982.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/b8e5b5cf-ef3b-4d99-826e-9cb76f03f4d4/tool-results/mcp-agent-ml-research-pdf_to_images-1778951832982.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 560
}
```

</details>

---


### Tool result

_source line 163 · 2026-05-16T17:17:13.558718+00:00_

Error: result (715,815 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/b8e5b5cf-ef3b-4d99-826e-9cb76f03f4d4/tool-results/mcp-agent-ml-research-pdf_to_images-1778951833515.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/b8e5b5cf-ef3b-4d99-826e-9cb76f03f4d4/tool-results/mcp-agent-ml-research-pdf_to_images-1778951833515.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/b8e5b5cf-ef3b-4d99-826e-9cb76f03f4d4/tool-results/mcp-agent-ml-research-pdf_to_images-1778951833515.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 719
}
```

</details>

---


### Tool call

_source line 164 · 2026-05-16T17:17:25.908761+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nf = '/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/b8e5b5cf-ef3b-4d99-826e-9cb76f03f4d4/tool-results/mcp-agent-ml-research-pdf_to_images-1778951817906.txt'\nwith open(f) as fh:\n    data = json.load(fh)\nresult = json.loads(data['result'])\nif isinstance(result, dict):\n    print(list(result.keys())[:10])\nelif isinstance(result, list):\n    for item in result[:5]:\n        if isinstance(item, dict):\n            print({k: v[:80] if isinstance(v, str) and len(v) > 80 else v for k, v in item.items()})\n        else:\n            print(str(item)[:200])\n\" 2>&1 | head -20\n",
  "description": "Extract structure of PDF rendering output"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nf = '/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/b8e5b5cf-ef3b-4d99-826e-9cb76f03f4d4/tool-results/mcp-agent-ml-research-pdf_to_images-1778951817906.txt'\nwith open(f) as fh:\n    data = json.load(fh)\nresult = json.loads(data['result'])\nif isinstance(result, dict):\n    print(list(result.keys())[:10])\nelif isinstance(result, list):\n    for item in result[:5]:\n        if isinstance(item, dict):\n            print({k: v[:80] if isinstance(v, str) and len(v) > 80 else v for k, v in item.items()})\n        else:\n            print(str(item)[:200])\n\" 2>&1 | head -20\n",
    "description": "Extract structure of PDF rendering output"
  }
}
```

</details>

---


### Tool result

_source line 165 · 2026-05-16T17:17:26.171395+00:00_

['success', 'data', 'error', 'metadata']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 262
}
```

</details>

---


### Tool call

_source line 166 · 2026-05-16T17:17:33.865062+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nf = '/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/b8e5b5cf-ef3b-4d99-826e-9cb76f03f4d4/tool-results/mcp-agent-ml-research-pdf_to_images-1778951817906.txt'\nwith open(f) as fh:\n    data = json.load(fh)\nresult = json.loads(data['result'])\nprint('Keys:', list(result.keys()))\nprint('Metadata:', result.get('metadata'))\nif 'data' in result:\n    d = result['data']\n    if isinstance(d, list):\n        print(f'Data is list of {len(d)} items')\n        for item in d[:2]:\n            if isinstance(item, dict):\n                print('  Item keys:', list(item.keys()))\n                for k,v in item.items():\n                    if k != 'base64':\n                        print(f'    {k}: {str(v)[:100]}')\n                    else:\n                        print(f'    base64: [{len(v)} chars]')\n    elif isinstance(d, dict):\n        print('Data keys:', list(d.keys())[:10])\n\" 2>&1\n",
  "description": "Get PDF image file paths from rendered output"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nf = '/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/b8e5b5cf-ef3b-4d99-826e-9cb76f03f4d4/tool-results/mcp-agent-ml-research-pdf_to_images-1778951817906.txt'\nwith open(f) as fh:\n    data = json.load(fh)\nresult = json.loads(data['result'])\nprint('Keys:', list(result.keys()))\nprint('Metadata:', result.get('metadata'))\nif 'data' in result:\n    d = result['data']\n    if isinstance(d, list):\n        print(f'Data is list of {len(d)} items')\n        for item in d[:2]:\n            if isinstance(item, dict):\n                print('  Item keys:', list(item.keys()))\n                for k,v in item.items():\n                    if k != 'base64':\n                        print(f'    {k}: {str(v)[:100]}')\n                    else:\n                        print(f'    base64: [{len(v)} chars]')\n    elif isinstance(d, dict):\n        print('Data keys:', list(d.keys())[:10])\n\" 2>&1\n",
    "description": "Get PDF image file paths from rendered output"
  }
}
```

</details>

---


### Tool result

_source line 167 · 2026-05-16T17:17:33.965947+00:00_

Keys: ['success', 'data', 'error', 'metadata']
Metadata: {}
Data keys: ['images', 'total_pages', 'rendered_pages', 'dpi', 'output_dir']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 168 · 2026-05-16T17:17:40.592668+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nf = '/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/b8e5b5cf-ef3b-4d99-826e-9cb76f03f4d4/tool-results/mcp-agent-ml-research-pdf_to_images-1778951817906.txt'\nwith open(f) as fh:\n    data = json.load(fh)\nresult = json.loads(data['result'])\nd = result['data']\nprint('total_pages:', d['total_pages'])\nprint('rendered_pages:', d['rendered_pages'])\nprint('output_dir:', d['output_dir'])\nprint('dpi:', d['dpi'])\nimgs = d['images']\nprint(f'images: list of {len(imgs)} items')\nfor img in imgs:\n    print(f'  page={img.get(\\\"page\\\")}, path={img.get(\\\"path\\\", img.get(\\\"file_path\\\",\\\"?\\\"))}')\n\" 2>&1\n",
  "description": "Get image file paths and page info"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nf = '/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/b8e5b5cf-ef3b-4d99-826e-9cb76f03f4d4/tool-results/mcp-agent-ml-research-pdf_to_images-1778951817906.txt'\nwith open(f) as fh:\n    data = json.load(fh)\nresult = json.loads(data['result'])\nd = result['data']\nprint('total_pages:', d['total_pages'])\nprint('rendered_pages:', d['rendered_pages'])\nprint('output_dir:', d['output_dir'])\nprint('dpi:', d['dpi'])\nimgs = d['images']\nprint(f'images: list of {len(imgs)} items')\nfor img in imgs:\n    print(f'  page={img.get(\\\"page\\\")}, path={img.get(\\\"path\\\", img.get(\\\"file_path\\\",\\\"?\\\"))}')\n\" 2>&1\n",
    "description": "Get image file paths and page info"
  }
}
```

</details>

---


### Tool result

_source line 169 · 2026-05-16T17:17:40.743945+00:00_

total_pages: 16
rendered_pages: 5
output_dir: /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images
dpi: 200
images: list of 5 items
  page=1, path=/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p1.png
  page=2, path=/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p2.png
  page=3, path=/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p3.png
  page=4, path=/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p4.png
  page=5, path=/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p5.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 170 · 2026-05-16T17:17:46.919193+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
  "pages": "6-16",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
    "pages": "6-16",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 171 · 2026-05-16T17:17:47.323069+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 172 · 2026-05-16T17:17:47.878307+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 173 · 2026-05-16T17:17:50.335293+00:00_

Error: result (6,958,823 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/b8e5b5cf-ef3b-4d99-826e-9cb76f03f4d4/tool-results/mcp-agent-ml-research-pdf_to_images-1778951869746.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/b8e5b5cf-ef3b-4d99-826e-9cb76f03f4d4/tool-results/mcp-agent-ml-research-pdf_to_images-1778951869746.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/b8e5b5cf-ef3b-4d99-826e-9cb76f03f4d4/tool-results/mcp-agent-ml-research-pdf_to_images-1778951869746.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 3416
}
```

</details>

---


### Tool result

_source line 174 · 2026-05-16T17:17:51.140905+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3817
}
```

</details>

---


### Tool result

_source line 175 · 2026-05-16T17:17:51.292149+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3413
}
```

</details>

---


### Tool call

_source line 176 · 2026-05-16T17:17:56.272061+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 177 · 2026-05-16T17:17:56.774032+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 178 · 2026-05-16T17:17:57.855911+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1583
}
```

</details>

---


### Tool call

_source line 179 · 2026-05-16T17:17:57.856317+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 180 · 2026-05-16T17:17:59.213910+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2439
}
```

</details>

---


### Tool call

_source line 181 · 2026-05-16T17:17:59.515832+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nf = '/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/b8e5b5cf-ef3b-4d99-826e-9cb76f03f4d4/tool-results/mcp-agent-ml-research-pdf_to_images-1778951869746.txt'\nwith open(f) as fh:\n    data = json.load(fh)\nresult = json.loads(data['result'])\nd = result['data']\nfor img in d['images']:\n    print(img.get('path'))\n\" 2>&1\n",
  "description": "Get file paths for pages 6-16"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nf = '/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/b8e5b5cf-ef3b-4d99-826e-9cb76f03f4d4/tool-results/mcp-agent-ml-research-pdf_to_images-1778951869746.txt'\nwith open(f) as fh:\n    data = json.load(fh)\nresult = json.loads(data['result'])\nd = result['data']\nfor img in d['images']:\n    print(img.get('path'))\n\" 2>&1\n",
    "description": "Get file paths for pages 6-16"
  }
}
```

</details>

---


### Tool result

_source line 182 · 2026-05-16T17:17:59.668987+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1812
}
```

</details>

---


### Tool result

_source line 183 · 2026-05-16T17:17:59.770083+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p6.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p7.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p8.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p9.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p10.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p11.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p12.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p13.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p14.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p15.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p16.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 254
}
```

</details>

---


### Tool call

_source line 184 · 2026-05-16T17:18:31.036062+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 185 · 2026-05-16T17:18:31.239060+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-16T17:18:31.239506+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 187 · 2026-05-16T17:18:31.392091+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 188 · 2026-05-16T17:18:32.300827+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1264
}
```

</details>

---


### Tool result

_source line 189 · 2026-05-16T17:18:32.955189+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1715
}
```

</details>

---


### Tool result

_source line 190 · 2026-05-16T17:18:33.157488+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1918
}
```

</details>

---


### Tool result

_source line 191 · 2026-05-16T17:18:33.259372+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1867
}
```

</details>

---


### Tool call

_source line 192 · 2026-05-16T17:18:37.578055+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 193 · 2026-05-16T17:18:38.482702+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 194 · 2026-05-16T17:18:38.483318+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 195 · 2026-05-16T17:18:38.987416+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 196 · 2026-05-16T17:18:39.291500+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 808
}
```

</details>

---


### Tool call

_source line 197 · 2026-05-16T17:18:39.291922+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 198 · 2026-05-16T17:18:39.946397+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool result

_source line 199 · 2026-05-16T17:18:40.199225+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 200 · 2026-05-16T17:18:43.914412+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 201 · 2026-05-16T17:18:44.417501+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 202 · 2026-05-16T17:18:44.871139+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 203 · 2026-05-16T17:18:44.921785+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 204 · 2026-05-16T17:18:44.973197+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 205 · 2026-05-16T17:18:45.074400+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 656
}
```

</details>

---


### Tool call

_source line 206 · 2026-05-16T17:20:11.636215+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool call

_source line 207 · 2026-05-16T17:20:12.389557+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 review form soundness excitement scoring detailed rubric criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 review form soundness excitement scoring detailed rubric criteria"
  }
}
```

</details>

---


### Tool result

_source line 208 · 2026-05-16T17:20:59.855235+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 49, \"total_citations\": 77, \"unique_cited_keys\": 49, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 40, \"online_not_found\": 5, \"online_mismatch\": 4}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"shumailov2024_nature\", \"type\": \"article\", \"title\": \"AI models collapse when trained on recursively generated data\", \"authors\": \"Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and ...\", \"year\": \"2024\", \"venue\": \"Nature\"}, {\"key\": \"dohmatob2024_tale_of_tails\", \"type\": \"inproceedings\", \"title\": \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, ...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICML\"}, {\"key\": \"dohmatob2025_strong_collapse\", \"type\": \"inproceedings\", \"title\": \"Strong Model Collapse\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\", \"year\": \"2025\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"dohmatob2024_demystified\", \"type\": \"inproceedings\", \"title\": \"Model Collapse Demystified: The Case of Regression\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia\", \"year\": \"2024\", \"venue\": \"Proceedings of NeurIPS\"}, {\"key\": \"alemohammad2024_mad\", \"type\": \"inproceedings\", \"title\": \"Self-Consuming Generative Models Go MAD\", \"authors\": \"Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahme...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"gerstgrasser2024_accumulate\", \"type\": \"misc\", \"title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"authors\": \"Gerstgrasser, Matt
…[truncated 38138 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 48219
}
```

</details>

---


### Tool result

_source line 209 · 2026-05-16T17:21:08.427215+00:00_

Web search results for query: "ACL ARR 2025 review form soundness excitement scoring detailed rubric criteria"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"aclrollingreview/acguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/acguidelines.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Conference Decisions · GitHub","url":"https://gist.github.com/antonisa/2158dee79179c7c49304ef353887bfa0"},{"title":"🎪 ACL 2025 Reviews Are Out: To Rebut or Flee? The Harsh Reality of NLP’s \"Publish or Perish\" Circus | CSPaper Forum","url":"https://forum.cspaper.org/topic/27/acl-2025-reviews-are-out-to-rebut-or-flee-the-harsh-reality-of-nlp-s-publish-or-perish-circus"},{"title":"Program Chairs’ Report on Peer Review at ACL 2023 Anna Rogers}","url":"https://aclanthology.org/2023.acl-long.report.pdf"}]

Based on the search results, here's information about the ACL ARR 2025 review form's soundness and excitement scoring rubrics:

## Soundness Scoring

For soundness, reviewers evaluate
…[truncated 1866 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 56037
}
```

</details>

---


### Tool call

_source line 210 · 2026-05-16T17:24:05.265200+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — Round 1 审稿报告\n\n**论文**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n**审查侧重**: 方法严谨性 + 实验设计\n**Reviewer Confidence**: 4/5 (Quite sure. I tried to check the important points carefully.)\n\n---\n\n## 总体评分\n\n**Overall**: 3/5 (Findings: could be accepted to Findings)\n**一句话总结**: 问题定义新颖且有实际价值，特征分析扎实，但交叉验证中样本非独立性、reference model 循环依赖、cross-scale 实验混淆变量等方法论问题削弱了泛化性声明的可信度。\n\n## 官方维度打分（来自 ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心实验流程可靠，但 CV 中样本非独立性、EDD 的 classifier-dependence、cross-scale 混淆变量等方法论缺陷需要修复 |\n| Excitement | 4/5 | 从二分类 AI 文本检测到有序深度估计是有意义的概念跳跃，对数据 curation 有实际影响 |\n| Reproducibility | 3.5/5 | 多数实验细节已给出，但 LoRA 训练细节（warmup、scheduler、batch size）和 Wikipedia 预处理不够精确 |\n| Overall Assessment | 3/5 | 新颖问题 + 扎实初步探索，但泛化性声明（尤其 cross-scale、cross-strategy）的支撑力度不足以达到主会议标准 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **EDD 定义的 classifier-dependence 和单调性假设**\n- 具体位置：Section 3.4, Definition 1; Limitations (p.7)\n- 问题：EDD_T 依赖于独立训练的逐对二分类 RF classifiers（500 trees, √|F| features/split），使其成为 classifier+features 的性质而非数据的内在属性。不同分类器可能产生不同的 EDD 值。同时，Definition 1 要求 AUC 单调递减（\"longest contiguous discriminable prefix\"），但论文自己在 Limitations 中引用 Bakshi & Chakraborty (2026) 指出递归生成可能暂时改善质量，产生非单调 AUC 曲线（如 d1d2 处下降后 d3d5 恢复）。当前定义对此场景无法处理，论文未提出替代方案。\n- 为什么影响接收：EDD 是论文声称的核心贡献之一（§1 bullet 4），如果该度量既依赖于分类器选择又不能处理非单调情况，其作为通用度量标准的价值存疑。\n- 建议修改方向：(a) 报告 EDD 对不同分类器（SVM、LR、XGB）的敏感性分析；(b) 定义 non-contiguous 版本的 EDD（如允许一个 gap）以应对非单调场景；(c) 在论文中明确 EDD 是给定 classifier+feature 组合下的操作性定义，而非数据内在性质。\n\n**N2** [critical] **Reference Model 循环依赖**\n- 具体位置：Section 3.3; Appendix A.12 Table 15\n- 问题：Pythia-1.4B 同时作为生成器（generator）和参考模型（reference model）。所有 19 个统计特征均相对于 Pythia-1.4B 计算（p90_ppl、var_surprisal 等）。对于 Pythia cells，这意味着 reference model 对自己生成文本的分布有直接先验知识——相当于用一个人评判自己写的文章。Appendix A.12 显示 self-reference (Pythia→Pythia) 准确率 78.6%，cross-reference (OLMo-1B→Pythia text) 下降到 74.5%，4.1pp gap。但论文未测试更远架构（如 GPT-2→OLMo text）是否会进一步恶化，也未讨论在 generator 未知的部署场景下 reference model 选择的系统性影响。\n- 为什么影响接收：如果方法的有效性在很大程度上依赖于知道 generator identity 来选择 matching reference model，则其实用性被大幅削弱——这与传统 AI 文本检测的核心挑战（generator-agnostic detection）相矛盾。\n- 建议修改方向：(a) 测试所有 3×3 reference-generator 组合（3 个 reference × 3 个 generator family）的完整矩阵；(b) 测试一个完全独立的 reference model（如未在 benchmark 中出现的 Phi-2 或 TinyLlama）；(c) 如果 cross-reference 确实显著下降，在 claims 中明确 scope 限制。\n\n**N3** [critical] **5-Fold CV 中样本非独立性**\n- 具体位置：Section 3.3 (\"5-fold stratified CV\"); Section 4 全部结果\n- 问题：每个 depth d 的所有样本来自同一个 LoRA finetuned model 实例。深度 d=2 的 5000 个样本全部由同一个 LoRA 模型生成——它们共享相同的模型参数和训练轨迹。5-fold stratified CV 将这些样本视为 i.i.d.，但实际上它们来自同一分布实例化（same distribution instantiation）。这违反了独立性假设。类比：如果你用同一个人写的 5000 篇文章训练/测试 authorship classifier，CV 准确率会虚高，因为模型学的是那个人的风格而非 authorship 的通用信号。\n- 为什么影响接收：主实验结果（Table 2 的 70-85% accuracy）可能因此偏乐观。论文的 cross-model 和 cross-strategy transfer 实验部分缓解了这个问题，但主要结果表仍受影响。\n- 建议修改方向：(a) 使用多个独立 LoRA seeds（如 5 个不同 random seed）生成每个 depth 的数据，报告 seed-level 方差；(b) 或使用 group-aware CV（grouped k-fold，同一 generation run 的样本不分散到不同 fold）；(c) 至少在 Discussion 中明确讨论这个 limitation 并量化其影响。\n\n**N4** [critical] **Cross-Scale 实验存在严重混淆变量**\n- 具体位置：Section 5.4; Table 6\n- 问题：Cross-scale 实验（7B 模型）同时引入三个混淆变量：(a) 模型规模（1.4B→7B），(b) 量化方法（standard LoRA→4-bit QLoRA），(c) 样本量（5000→500 per depth）。4-bit 量化会显著影响 perplexity distribution——QLoRA 模型的 token-level perplexity 分布与 full-precision LoRA 不同，这直接影响论文的核心特征（p90_ppl 等）。500 vs 5000 样本的 statistical power 差异也使置信区间不可比。仅两个 7B 模型（Llama-3.1-8B, Qwen2.5-7B）无法支撑 \"cross-scale\" 的泛化性声明。\n- 为什么影响接收：论文在 §1 contributions 中声称 \"extending to two 7B-scale generators yields 70.29% accuracy\"，但该数字的可靠性因混淆变量而不确定。\n- 建议修改方向：(a) 对同一模型分别测试 full-precision LoRA 和 QLoRA 以隔离量化效应；(b) 增加 7B 样本量到至少 2000 per depth；(c) 如资源有限，降低 claim 强度——改为 \"preliminary cross-scale evidence\" 而非 \"cross-scale generalization\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **LoRA 超参数敏感性完全未探索**\n- 具体位置：Section 3.2 (\"LoRA finetuning: r=16, α=32, 3 epochs, lr=2e-5\")\n- 问题：整个 benchmark 使用单一 LoRA 配置，无任何消融。不同 LoRA rank（r=4 vs r=64）可能导致截然不同的退化动态——低 rank 可能加速 collapse（信息瓶颈更严格），高 rank 可能更好保持分布特性。不同训练 epoch 数（1 vs 10）也可能改变 depth fingerprint 的形态。论文的 \"statistical fingerprint\" 概念的通用性在没有 LoRA 配置消融的情况下无法确立。\n- 建议：至少在一个 model-strategy cell 上测试 r ∈ {4, 16, 64} 和 epochs ∈ {1, 3, 10}。\n\n**W2** [warning] **VIF 分析揭示的多重共线性对特征重要性分析的影响被忽视**\n- 具体位置：Section 3.3; Table 16 (Appendix A.15); Figure 4\n- 问题：14–16/19 特征 VIF > 10，有效维度仅 4–5，但论文多处强调 \"19 candidate features\"。更严重的是，高度共线特征下 SHAP 和 Gini importance 是不稳定的——排列一个共线特征的值会将重要性重新分配到其他共线特征。Appendix A.15 的 \"SHAP-Gini ρ=0.93\" concordance 在共线环境下可能是 artifact。论文声称 p90_ppl 和 var_surprisal 是 \"universal depth markers\"，但这两个特征本身高度相关（都捕获尾部 perplexity 信息），其 \"dominance\" 可能仅因为它们恰好在 RF 的 tree-building 过程中被优先选中。\n- 建议：(a) 报告剔除共线特征后（如仅保留 VIF < 5 的特征子集）的 SHAP ranking；(b) 使用 conditional SHAP（SHAP with grouped features）或 permutation importance with grouped correlated features。\n\n**W3** [warning] **逐对 AUC 的独立分类器缺乏序关系一致性**\n- 具体位置：Section 3.4; Section 4.3\n- 问题：每对 (d, d+1) 由独立训练的二分类 RF 判别。这些分类器之间没有一致性约束——d1-vs-d2 classifier 判为 d=2 的样本，d2-vs-d3 classifier 可能判为 d=2 而非 d=3。论文未验证这些独立 classifier 的预测是否构成一致的序关系。对于 EDD 的 \"contiguous discriminability\" 概念，如果各对之间的分类边界不兼容，EDD 的语义就不清晰。\n- 建议：在 test set 上运行所有 pairwise classifiers，检查序关系一致性（如一个 d=2 样本是否同时被 d1-vs-d2 判为 d2、被 d2-vs-d3 判为 d2）。\n\n**W4** [warning] **Wild Data FPR 过高，削弱实用性声明**\n- 具体位置：Table 12; Section A.10; Discussion §6\n- 问题：C4 web-crawl 数据上 FPR 从 4.7%（Pythia-1.4B/WikiText）到 22.4%（GPT-2 XL）。22.4% 集中在 \"template/SEO content\"——但这恰好是真实 web crawl 中的主要内容类型。论文在 Discussion（§6）中声称 depth estimation 可用于 \"depth-graduated data curation\"，但 22% 的误报率在实际数据筛选流程中不可接受。\n- 建议：(a) 分析 FPR 的分布——是否有简单的后处理规则（如文本长度阈值、repetition ratio 阈值）能降低 FPR？(b) 至少在 Discussion 中量化 FPR 对 curation quality 的影响。\n\n**W5** [warning] **Cross-Strategy Transfer 的下降暗示方法依赖先验知识**\n- 具体位置：Section 5.3; Table 5; Limitations (p.7)\n- 问题：Cross-strategy transfer 从 ~70%（within-strategy）下降到 59.1%（leave-one-out）。Limitations 承认需要 \"strategy-conditioned classification\"——这意味着方法的有效部署需要预先知道解码策略，大幅限制实用性。temperature 采样尤其造成边界反转（d1d2 boundary inversion under temperature, p.7），说明不同策略产生质性不同的退化轨迹。论文未提供任何策略检测模块或策略不变的特征设计。\n- 建议：(a) 设计一个简单的 decoding strategy detector（基于 entropy distribution）作为 pre-stage；(b) 或至少分析哪些特征在策略间最稳定。\n\n---\n\n## 小问题（不影响接收）\n\n- Table 2 主表未报告置信区间；CI 仅出现在 Appendix Table 14。建议在主表至少报告标准差。\n- \"Depth Degradation Atlas\"（§4 标题）对一个 3×3 accuracy grid 而言命名过于宏大。\n- Definition 1 的排版可更清晰——\"if AUC(0,1) ≥ T\" 的条件语句读起来有歧义，建议用标准数学符号重写为：$\\mathrm{EDD}_T = \\max\\{d^* \\in \\{0,\\ldots,N{-}1\\} : \\forall\\, i < d^*,\\; \\mathrm{AUC}(i,i{+}1) \\geq T\\}$。\n- 引用元数据：`he2021_deberta_v3` 标注为 2023 但实际发表于 2021（ICLR 2021 preprint, 2023 proceedings）。\n- 引用元数据：`alemohammad2024_mad` 第一作者与 OpenAlex 记录不一致（bib=Alemohammad vs api=Casco-Rodriguez）。\n- Wikipedia seed corpus 的具体子集选择和预处理流程不够详细，影响精确复现。\n- §5.4 报告 \"500 samples/depth\" 但未说明这是 total 还是 per model-strategy cell。\n\n---\n\n## 主要优势\n\n1. **问题定义新颖且有实际价值**：从 binary AI 文本检测到 ordinal depth estimation 是概念性突破。递归生成链形式化（§3.1）简洁且有理论根基（model collapse literature）。这个问题在数据 curation 和 AI 安全领域有明确需求。\n\n2. **系统性 benchmark 设计**：3 model families × 3 decoding strategies × 4+ depths 的 180K 样本覆盖面广。扩展到 d5 和 7B 模型的意图正确（尽管执行上有混淆变量）。\n\n3. **特征分析扎实且有启发性**：p90_ppl 和 var_surprisal 作为跨模型跨策略的 universal depth markers 的发现（§4.2, Figure 4, Table 16）令人信服。Gini importance 和 SHAP concordance (ρ=0.93) 的交叉验证增加了可信度。这一发现对 model collapse 研究社区有独立价值。\n\n4. **诚实的 Limitations section**：论文坦诚讨论了非单调性、reference model 依赖、strategy-conditioned limits、FPR 问题。这在投稿论文中不常见且值得肯定。\n\n5. **全面的评估维度**：七个泛化轴（§5）——cross-model、cross-strategy、cross-scale、temperature robustness、wild-data、end-to-end PLM、domain bias——展现了对新问题领域难得的探索广度。\n\n6. **Downstream 应用验证**（Appendix A.11）：PoC 实验证明 depth estimation 可改善 downstream curation quality（seed-group production 从 20.8% 提升到 64.09% LOGO accuracy），增强了实用价值论证。\n\n---\n\n## Questions for Authors\n\nQ1: 如果使用多个独立 LoRA random seeds 生成同一 depth 的数据（如 5 seeds × 1000 samples per seed），然后进行 seed-grouped CV，预期准确率会下降多少？\n\nQ2: 对于 cross-scale 实验，是否可以在一个较小模型（如 Pythia-1.4B）上同时运行 standard LoRA 和 4-bit QLoRA 来隔离量化效应？\n\nQ3: EDD 在不同分类器（LR, SVM, XGB）下的值差异有多大？如果差异超过 ±1，如何为 T=0.75 的选择辩护？\n\nQ4: Table 12 中 GPT-2 XL 在 C4 上 22.4% FPR——这些 false positive 集中在哪些文本类型？是否有可提取的 rejection criteria（如 repetition ratio > X）来降低 FPR？\n\nQ5: 论文是否考虑过将问题建模为 ordinal regression（如 CORAL, Cao et al. 2020）而非独立 pairwise classification + 多类 RF？这可能自然保证序关系一致性。",
  "reviewer_id": "1",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — Round 1 审稿报告\n\n**论文**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n**审查侧重**: 方法严谨性 + 实验设计\n**Reviewer Confidence**: 4/5 (Quite sure. I tried to check the important points carefully.)\n\n---\n\n## 总体评分\n\n**Overall**: 3/5 (Findings: could be accepted to Findings)\n**一句话总结**: 问题定义新颖且有实际价值，特征分析扎实，但交叉验证中样本非独立性、reference model 循环依赖、cross-scale 实验混淆变量等方法论问题削弱了泛化性声明的可信度。\n\n## 官方维度打分（来自 ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心实验流程可靠，但 CV 中样本非独立性、EDD 的 classifier-dependence、cross-scale 混淆变量等方法论缺陷需要修复 |\n| Excitement | 4/5 | 从二分类 AI 文本检测到有序深度估计是有意义的概念跳跃，对数据 curation 有实际影响 |\n| Reproducibility | 3.5/5 | 多数实验细节已给出，但 LoRA 训练细节（warmup、scheduler、batch size）和 Wikipedia 预处理不够精确 |\n| Overall Assessment | 3/5 | 新颖问题 + 扎实初步探索，但泛化性声明（尤其 cross-scale、cross-strategy）的支撑力度不足以达到主会议标准 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **EDD 定义的 classifier-dependence 和单调性假设**\n- 具体位置：Section 3.4, Definition 1; Limitations (p.7)\n- 问题：EDD_T 依赖于独立训练的逐对二分类 RF classifiers（500 trees, √|F| features/split），使其成为 classifier+features 的性质而非数据的内在属性。不同分类器可能产生不同的 EDD 值。同时，Definition 1 要求 AUC 单调递减（\"longest contiguous discriminable prefix\"），但论文自己在 Limitations 中引用 Bakshi & Chakraborty (2026) 指出递归生成可能暂时改善质量，产生非单调 AUC 曲线（如 d1d2 处下降后 d3d5 恢复）。当前定义对此场景无法处理，论文未提出替代方案。\n- 为什么影响接收：EDD 是论文声称的核心贡献之一（§1 bullet 4），如果该度量既依赖于分类器选择又不能处理非单调情况，其作为通用度量标准的价值存疑。\n- 建议修改方向：(a) 报告 EDD 对不同分类器（SVM、LR、XGB）的敏感性分析；(b) 定义 non-contiguous 版本的 EDD（如允许一个 gap）以应对非单调场景；(c) 在论文中明确 EDD 是给定 classifier+feature 组合下的操作性定义，而非数据内在性质。\n\n**N2** [critical] **Reference Model 循环依赖**\n- 具体位置：Section 3.3; Appendix A.12 Table 15\n- 问题：Pythia-1.4B 同时作为生成器（generator）和参考模型（reference model）。所有 19 个统计特征均相对于 Pythia-1.4B 计算（p90_ppl、var_surprisal 等）。对于 Pythia cells，这意味着 reference model 对自己生成文本的分布有直接先验知识——相当于用一个人评判自己写的文章。Appendix A.12 显示 self-reference (Pythia→Pythia) 准确率 78.6%，cross-reference (OLMo-1B→Pythia text) 下降到 74.5%，4.1pp gap。但论文未测试更远架构（如 GPT-2→OLMo text）是否会进一步恶化，也未讨论在 generator 未知的部署场景下 reference model 选择的系统性影响。\n- 为什么影响接收：如果方法的有效性在很大程度上依赖于知道 generator identity 来选择 matching reference model，则其实用性被大幅削弱——这与传统 AI 文本检测的核心挑战（generator-agnostic detection）相矛盾。\n- 建议修改方向：(a) 测试所有 3×3 reference-generator 组合（3 个 reference × 3 个 generator family）的完整矩阵；(b) 测试一个完全独立的 reference model（如未在 benchmark 中出现的 Phi-2 或 TinyLlama）；(c) 如果 cross-reference 确实显著下降，在 claims 中明确 scope 限制。\n\n**N3** [critical] **5-Fold CV 中样本非独立性**\n- 具体位置：Section 3.3 (\"5-fold stratified CV\"); Section 4 全部结果\n- 问题：每个 depth d 的所有样本来自同一个 LoRA finetuned model 实例。深度 d=2 的 5000 个样本全部由同一个 LoRA 模型生成——它们共享相同的模型参数和训练轨迹。5-fold stratified CV 将这些样本视为 i.i.d.，但实际上它们来自同一分布实例化（same distribution instantiation）。这违反了独立性假设。类比：如果你用同一个人写的 5000 篇文章训练/测试 authorship classifier，CV 准确率会虚高，因为模型学的是那个人的风格而非 authorship 的通用信号。\n- 为什么影响接收：主实验结果（Table 2 的 70-85% accuracy）可能因此偏乐观。论文的 cross-model 和 cross-strategy transfer 实验部分缓解了这个问题，但主要结果表仍受影响。\n- 建议修改方向：(a) 使用多个独立 LoRA seeds（如 5 个不同 random seed）生成每个 depth 的数据，报告 seed-level 方差；(b) 或使用 group-aware CV（grouped k-fold，同一 generation run 的样本不分散到不同 fold）；(c) 至少在 Discussion 中明确讨论这个 limitation 并量化其影响。\n\n**N4** [critical] **Cross-Scale 实验存在严重混淆变量**\n- 具体位置：Section 5.4; Table 6\n- 问题：Cross-scale 实验（7B 模型）同时引入三个混淆变量：(a) 模型规模（1.4B→7B），(b) 量化方法（standard LoRA→4-bit QLoRA），(c) 样本量（5000→500 per depth）。4-bit 量化会显著影响 perplexity distribution——QLoRA 模型的 token-level perplexity 分布与 full-precision LoRA 不同，这直接影响论文的核心特征（p90_ppl 等）。500 vs 5000 样本的 statistical power 差异也使置信区间不可比。仅两个 7B 模型（Llama-3.1-8B, Qwen2.5-7B）无法支撑 \"cross-scale\" 的泛化性声明。\n- 为什么影响接收：论文在 §1 contributions 中声称 \"extending to two 7B-scale generators yields 70.29% accuracy\"，但该数字的可靠性因混淆变量而不确定。\n- 建议修改方向：(a) 对同一模型分别测试 full-precision LoRA 和 QLoRA 以隔离量化效应；(b) 增加 7B 样本量到至少 2000 per depth；(c) 如资源有限，降低 claim 强度——改为 \"preliminary cross-scale evidence\" 而非 \"cross-scale generalization\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **LoRA 超参数敏感性完全未探索**\n- 具体位置：Section 3.2 (\"LoRA finetuning: r=16, α=32, 3 epochs, lr=2e-5\")\n- 问题：整个 benchmark 使用单一 LoRA 配置，无任何消融。不同 LoRA rank（r=4 vs r=64）可能导致截然不同的退化动态——低 rank 可能加速 collapse（信息瓶颈更严格），高 rank 可能更好保持分布特性。不同训练 epoch 数（1 vs 10）也可能改变 depth fingerprint 的形态。论文的 \"statistical fingerprint\" 概念的通用性在没有 LoRA 配置消融的情况下无法确立。\n- 建议：至少在一个 model-strategy cell 上测试 r ∈ {4, 16, 64} 和 epochs ∈ {1, 3, 10}。\n\n**W2** [warning] **VIF 分析揭示的多重共线性对特征重要性分析的影响被忽视**\n- 具体位置：Section 3.3; Table 16 (Appendix A.15); Figure 4\n- 问题：14–16/19 特征 VIF > 10，有效维度仅 4–5，但论文多处强调 \"19 candidate features\"。更严重的是，高度共线特征下 SHAP 和 Gini importance 是不稳定的——排列一个共线特征的值会将重要性重新分配到其他共线特征。Appendix A.15 的 \"SHAP-Gini ρ=0.93\" concordance 在共线环境下可能是 artifact。论文声称 p90_ppl 和 var_surprisal 是 \"universal depth markers\"，但这两个特征本身高度相关（都捕获尾部 perplexity 信息），其 \"dominance\" 可能仅因为它们恰好在 RF 的 tree-building 过程中被优先选中。\n- 建议：(a) 报告剔除共线特征后（如仅保留 VIF < 5 的特征子集）的 SHAP ranking；(b) 使用 conditional SHAP（SHAP with grouped features）或 permutation importance with grouped correlated features。\n\n**W3** [warning] **逐对 AUC 的独立分类器缺乏序关系一致性**\n- 具体位置：Section 3.4; Section 4.3\n- 问题：每对 (d, d+1) 由独立训练的二分类 RF 判别。这些分类器之间没有一致性约束——d1-vs-d2 classifier 判为 d=2 的样本，d2-vs-d3 classifier 可能判为 d=2 而非 d=3。论文未验证这些独立 classifier 的预测是否构成一致的序关系。对于 EDD 的 \"contiguous discriminability\" 概念，如果各对之间的分类边界不兼容，EDD 的语义就不清晰。\n- 建议：在 test set 上运行所有 pairwise classifiers，检查序关系一致性（如一个 d=2 样本是否同时被 d1-vs-d2 判为 d2、被 d2-vs-d3 判为 d2）。\n\n**W4** [warning] **Wild Data FPR 过高，削弱实用性声明**\n- 具体位置：Table 12; Section A.10; Discussion §6\n- 问题：C4 web-crawl 数据上 FPR 从 4.7%（Pythia-1.4B/WikiText）到 22.4%（GPT-2 XL）。22.4% 集中在 \"template/SEO content\"——但这恰好是真实 web crawl 中的主要内容类型。论文在 Discussion（§6）中声称 depth estimation 可用于 \"depth-graduated data curation\"，但 22% 的误报率在实际数据筛选流程中不可接受。\n- 建议：(a) 分析 FPR 的分布——是否有简单的后处理规则（如文本长度阈值、repetition ratio 阈值）能降低 FPR？(b) 至少在 Discussion 中量化 FPR 对 curation quality 的影响。\n\n**W5** [warning] **Cross-Strategy Transfer 的下降暗示方法依赖先验知识**\n- 具体位置：Section 5.3; Table 5; Limitations (p.7)\n- 问题：Cross-strategy transfer 从 ~70%（within-strategy）下降到 59.1%（leave-one-out）。Limitations 承认需要 \"strategy-conditioned classification\"——这意味着方法的有效部署需要预先知道解码策略，大幅限制实用性。temperature 采样尤其造成边界反转（d1d2 boundary inversion under temperature, p.7），说明不同策略产生质性不同的退化轨迹。论文未提供任何策略检测模块或策略不变的特征设计。\n- 建议：(a) 设计一个简单的 decoding strategy detector（基于 entropy distribution）作为 pre-stage；(b) 或至少分析哪些特征在策略间最稳定。\n\n---\n\n## 小问题（不影响接收）\n\n- Table 2 主表未报告置信区间；CI 仅出现在 Appendix Table 14。建议在主表至少报告标准差。\n- \"Depth Degradation Atlas\"（§4 标题）对一个 3×3 accuracy grid 而言命名过于宏大。\n- Definition 1 的排版可更清晰——\"if AUC(0,1) ≥ T\" 的条件语句读起来有歧义，建议用标准数学符号重写为：$\\mathrm{EDD}_T = \\max\\{d^* \\in \\{0,\\ldots,N{-}1\\} : \\forall\\, i < d^*,\\; \\mathrm{AUC}(i,i{+}1) \\geq T\\}$。\n- 引用元数据：`he2021_deberta_v3` 标注为 2023 但实际发表于 2021（ICLR 2021 preprint, 2023 proceedings）。\n- 引用元数据：`alemohammad2024_mad` 第一作者与 OpenAlex 记录不一致（bib=Alemohammad vs api=Casco-Rodriguez）。\n- Wikipedia seed corpus 的具体子集选择和预处理流程不够详细，影响精确复现。\n- §5.4 报告 \"500 samples/depth\" 但未说明这是 total 还是 per model-strategy cell。\n\n---\n\n## 主要优势\n\n1. **问题定义新颖且有实际价值**：从 binary AI 文本检测到 ordinal depth estimation 是概念性突破。递归生成链形式化（§3.1）简洁且有理论根基（model collapse literature）。这个问题在数据 curation 和 AI 安全领域有明确需求。\n\n2. **系统性 benchmark 设计**：3 model families × 3 decoding strategies × 4+ depths 的 180K 样本覆盖面广。扩展到 d5 和 7B 模型的意图正确（尽管执行上有混淆变量）。\n\n3. **特征分析扎实且有启发性**：p90_ppl 和 var_surprisal 作为跨模型跨策略的 universal depth markers 的发现（§4.2, Figure 4, Table 16）令人信服。Gini importance 和 SHAP concordance (ρ=0.93) 的交叉验证增加了可信度。这一发现对 model collapse 研究社区有独立价值。\n\n4. **诚实的 Limitations section**：论文坦诚讨论了非单调性、reference model 依赖、strategy-conditioned limits、FPR 问题。这在投稿论文中不常见且值得肯定。\n\n5. **全面的评估维度**：七个泛化轴（§5）——cross-model、cross-strategy、cross-scale、temperature robustness、wild-data、end-to-end PLM、domain bias——展现了对新问题领域难得的探索广度。\n\n6. **Downstream 应用验证**（Appendix A.11）：PoC 实验证明 depth estimation 可改善 downstream curation quality（seed-group production 从 20.8% 提升到 64.09% LOGO accuracy），增强了实用价值论证。\n\n---\n\n## Questions for Authors\n\nQ1: 如果使用多个独立 LoRA random seeds 生成同一 depth 的数据（如 5 seeds × 1000 samples per seed），然后进行 seed-grouped CV，预期准确率会下降多少？\n\nQ2: 对于 cross-scale 实验，是否可以在一个较小模型（如 Pythia-1.4B）上同时运行 standard LoRA 和 4-bit QLoRA 来隔离量化效应？\n\nQ3: EDD 在不同分类器（LR, SVM, XGB）下的值差异有多大？如果差异超过 ±1，如何为 T=0.75 的选择辩护？\n\nQ4: Table 12 中 GPT-2 XL 在 C4 上 22.4% FPR——这些 false positive 集中在哪些文本类型？是否有可提取的 rejection criteria（如 repetition ratio > X）来降低 FPR？\n\nQ5: 论文是否考虑过将问题建模为 ordinal regression（如 CORAL, Cao et al. 2020）而非独立 pairwise classification + 多类 RF？这可能自然保证序关系一致性。",
    "reviewer_id": "1",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 211 · 2026-05-16T17:24:08.878589+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3613
}
```

</details>

---


### Assistant

_source line 212 · 2026-05-16T17:24:18.305870+00:00_

审稿报告已提交给 Review Director。

总结：

- **Overall: 3/5 (Findings)**，Soundness 3.5，Excitement 4
- 4 个 Must-Fix 问题：EDD 的 classifier-dependence 和单调性假设、reference model 循环依赖、5-fold CV 样本非独立性、cross-scale 混淆变量
- 5 个 Should-Fix 问题：LoRA 超参数未消融、VIF 共线性对 SHAP 的影响、pairwise classifier 序关系不一致、wild data FPR 过高、cross-strategy 下降暗示需要策略先验
- 核心判断：问题定义新颖且重要，特征分析有价值，但泛化性声明的实验支撑存在方法论缺陷，当前版本更适合 Findings 而非主会议

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1"
}
```

</details>

---


## Round 8

## Round 8

18 recorded events


### User

_source line 213 · 2026-05-16T17:24:59.297182+00:00_

[Round 1 审稿请求]:
## Step 2 — 交叉分享：Reviewer 2 的完整审稿意见

请逐条回应以下 Reviewer 2 的意见。对每个观点标注：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

特别注意与你自己审稿意见的异同——如有分歧请详细论证。

---

以下是 Reviewer 2 的完整原文：

## Reviewer 2 — Round 1 审稿报告

**Overall**: 3.5/5 (Borderline Conference / Findings)

### Must-Fix 问题

**N1** [critical] "Universal" claim证据不足
- Introduction §1 ("universal and scale-variant across the three model families and three decoding strategies studied"), Abstract line 6-7
- 论文用 "universal" 描述depth signal，但实验仅覆盖3个1-1.5B autoregressive models + 2个7B instruction-tuned models，全部为decoder-only transformer。Cross-model transfer（Table 4）d1-d3 balanced accuracy仅55.4%（chance=33%，即1.67×chance）。
- 建议：将 "universal" 替换为 "consistent across the three model families studied"。

**N2** [critical] Curation PoC作为contribution列出，但结果统计不显著
- RF-filtered vs unfiltered的所有三个对比均不显著（p=0.407/0.492/0.607）。论文仍将 "depth-graduated curation" 列为enabling application。RF vs random subsampling显著（p<0.001-0.02），但这只证明depth-informed selection优于随机丢弃。
- 建议：将curation从contribution降级为 "preliminary exploration"。

**N3** [critical] Perplexity tail statistics dominance的novelty受限
- Dohmatob et al. (2024) "A Tale of Tails" 的核心结论就是recursive training erodes distributional tails。论文的发现几乎是这些理论结果的直接empirical corollary。
- 建议：明确区分 "theory predicts tails erode" vs "our contribution shows this erosion is monotonic, quantifiable, and classifiable at specific depth boundaries"。

### Should-Fix 问题

**W1** Abstract对transfer结果的representation不平衡
- 70-85%是in-distribution performance。Cross-model transfer只有66.4%（d1-d3: 55.4%）。Abstract没有关于transfer degradation的信息。

**W2** Cross-model recursive chain (84.75%) 的architecture confound未完全解决
- 仅两条chain（forward + reverse）不足以fully eliminate confound。需要多个permutation。

**W3** 7B cross-scale实验的confounds过多
- base vs instruct对比（"instruction-tuning regularizes"）可能被quantization artifacts drive。因果推断过于confident。

**W4** 方法论贡献轻量
- 方法是 "19 perplexity-based features + RF"，EDD是AUC threshold的简单包装。对于EMNLP main conference方法论深度不足。

### 小问题
1. Table 1和Table 2的accuracy微小不一致（78.2% vs 78.8%）
2. 脚注提到Qwen2.5-7B的U-shaped pattern "possibly reflecting instruction-tuning effects"——但base model control显示base model也non-monotonic。tension未讨论。
3. Ordinal Classification只引了CORAL和CLOC，missing经典工作如Frank & Hall (2001)。
4. Zero-shot LLM ablation prompt给了oracle information about depth patterns。
5. Cross-domain仅arXiv 500 samples on single pipeline。

### Related Work 建议补充
1. Schaeffer et al. (2025) "Position: Model Collapse Does Not Mean What You Think"
2. "A Closer Look at Model Collapse" (2025) — memorization perspective
3. C2PA/Content Credentials framework
4. Mohamed et al. "Broken Telephone" 需更深入讨论

### Venue Fit
建议投稿target：Findings of EMNLP 或修改后resubmit Main Conference。

---

请对以上每个 Must-Fix (N1-N3)、Should-Fix (W1-W4)、和小问题逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 214 · 2026-05-16T17:25:38.739661+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 215 · 2026-05-16T17:25:39.091537+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 216 · 2026-05-16T17:25:39.746681+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1007
}
```

</details>

---


### Tool result

_source line 217 · 2026-05-16T17:25:40.802567+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1711
}
```

</details>

---


### Tool call

_source line 218 · 2026-05-16T17:25:46.927267+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 219 · 2026-05-16T17:25:47.128809+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 220 · 2026-05-16T17:25:47.783715+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 221 · 2026-05-16T17:25:47.784182+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 222 · 2026-05-16T17:25:48.338164+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1209
}
```

</details>

---


### Tool result

_source line 223 · 2026-05-16T17:25:48.642076+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool call

_source line 224 · 2026-05-16T17:25:53.160256+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 225 · 2026-05-16T17:25:53.361370+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 226 · 2026-05-16T17:25:54.216353+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1056
}
```

</details>

---


### Tool result

_source line 227 · 2026-05-16T17:25:54.519951+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1158
}
```

</details>

---


### Tool call

_source line 228 · 2026-05-16T17:28:36.373172+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 意见的逐条交叉回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: \"Universal\" claim 证据不足**\n\n同意 R2 的核心判断。虽然 Abstract 确实加了限定语 \"across the three model families and three decoding strategies studied\"（p.1），但 \"universal\" 一词仍然过强。关键证据：\n\n1. Table 4 (p.6) 的 cross-model transfer mean accuracy 为 66.4%，但观察 per-holdout 结果，OLMo holdout 的 d1 recall 仅约 17.5%，Pythia holdout 的 d2 recall 约 24.8%——这说明跨模型泛化在中间深度极不稳定。\n2. 所有模型均为 decoder-only transformer、参数规模 1–1.5B，架构同质性高。encoder-decoder（T5/BART）、mixture-of-experts 等架构完全未覆盖。\n3. \"Universal\" 在 NLP 社区有明确含义（如 Universal Sentence Encoder、Universal Dependencies），暗示广泛适用性，与当前证据不匹配。\n\nR2 建议的 \"consistent across the three model families studied\" 措辞更准确。我进一步建议在 Discussion 中添加一段明确列出 \"universal\" 成立所需的额外验证（encoder-decoder、MoE、>13B scale）。\n\n**与我自己审稿的关系**：我的 N4（cross-scale 混淆变量）从实验设计角度指出了同类问题——证据基础太窄无法支撑强泛化声明。R2 从语言层面切入，二者互补。\n\n---\n\n**[AGREE] R2-N2: Curation PoC 统计不显著**\n\n同意。从 Appendix A.11 Table 13–14 (p.14) 的数据看：\n\n1. **关键对比不显著**：RF-filtered vs unfiltered（即\"过滤了是否比不过滤好？\"）的 p 值均 >0.4。这意味着在统计意义上，depth-based 过滤后训练的模型并不比用全部数据训练的模型更好。\n2. **显著对比的含金量低**：RF vs random subsampling 显著（p<0.02），但这只证明 \"有信息的选择优于随机丢弃\"——一个很低的 bar。任何合理的数据质量指标（如 perplexity 阈值）都可能超过随机丢弃。\n3. **统计功效不足**：仅 5 个 seed 的 paired t-test，检测中等 effect size 的 power 很低。但这不能作为维持 contribution claim 的理由——如果 effect size 小到 5 seeds 检测不到，其实际价值也有限。\n\nR2 建议将 curation 从 contribution 降级为 \"preliminary exploration\" 是合理的。论文 §1 的 contribution list 第 4 条应相应修改。\n\n**补充**：我在 Round 1 中将 curation PoC 列为优势（\"Downstream 应用验证\"），现在在 R2 的指出下修正——PoC 的方向正确，但统计证据不足以作为 contribution 列出。\n\n---\n\n**[AGREE，但需要补充 nuance] R2-N3: Perplexity tail statistics 的 novelty 受限**\n\n部分同意 R2 的判断，但认为 novelty 不是零。\n\n**同意的部分**：\n- Dohmatob et al. (2024) \"A Tale of Tails\" 确实已建立 \"recursive training erodes distributional tails\" 的理论框架。论文的 p90_ppl 和 var_surprisal 作为 dominant features 的发现在概念上是这一理论的 empirical realization。\n- 论文当前的 framing（§4.2, §6）未充分 acknowledge 这一理论先驱，读起来像是独立发现了 tail erosion。\n\n**需要 nuance 的部分**：\n- 从 \"theory predicts tails erode\" 到 \"tail erosion is monotonic across 4+ depths, quantifiable via specific percentile statistics, and classifiable with >70% ordinal accuracy\" 之间存在 non-trivial gap。理论预测了定性方向，论文提供了定量操作化。\n- EDD 框架将 tail erosion 的 \"何时变得不可区分\" 量化为具体 threshold 下的 depth boundary（§4.3, Table 17, Appendix A.16），这超出了 Dohmatob 的理论范围。\n- Feature ranking 的发现（top-2 features 达到 full-set 91.1% accuracy, §4.2）为实际部署提供了 actionable guidance。\n\n**结论**：R2 的建议完全正确——论文需要在 Related Work 和 Introduction 中明确区分 \"theory predicts tails erode\"（Dohmatob 的贡献）与 \"we operationalize this into a classifiable, quantifiable, ordinal depth estimation framework\"（本文贡献）。这不是降低 novelty，而是更诚实地定位贡献。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Abstract 对 transfer 结果的呈现不平衡**\n\n完全同意。Abstract (p.1) 报告 \"Cross-model transfer reaches 66.8%\"，但未提及：\n- d1-d3 子集的大幅下降（从 Table 4 可见，去掉几乎 100% 的 d0 后，实际深度区分能力显著弱化）\n- Cross-strategy 仅 59.1%（§5.3, Table 5）\n- Cross-scale 仅 60.1%–70.2%（§5.4, Table 6）\n\nAbstract 应至少用一句话 acknowledge transfer gap，例如 \"though transfer accuracy degrades substantially for intermediate depths, ranging from 55–67% across model and strategy holdouts.\"\n\n**与我自己审稿的关系**：我的 W4（wild data FPR）和 W5（cross-strategy 下降）从不同角度指出了同样的 overstatement 模式。\n\n---\n\n**[AGREE] R2-W2: Cross-model recursive chain 的 architecture confound**\n\n同意。Appendix A.13 (p.14) 的 cross-model recursive chain 实验仅测试了两条 chain（forward: Pythia→OLMo→GPT-2 和 reverse）。3 个模型有 3!=6 种排列，仅测 2 种不足以消除 architecture ordering confound。\n\n补充证据：从 p.14 可见 forward chain 达到 84.75%——但如果 reverse chain 准确率显著不同（论文未明确报告 reverse chain 的单独准确率），则 ordering effect 可能不可忽略。\n\n---\n\n**[AGREE] R2-W3: 7B cross-scale confounds**\n\n完全同意，这与我自己的 N4 高度重合。R2 进一步指出了 base vs instruct 对比中的混淆——论文 §5.4 提到 \"instruction-tuning regularizes\"（p.6），但 base model 也展现 non-monotonic pattern，说明 instruction-tuning 不是唯一因素。这个因果推断确实过于 confident。\n\n---\n\n**[REBUT] R2-W4: 方法论贡献轻量**\n\n不完全同意。R2 认为 \"19 perplexity features + RF\" 对 EMNLP main 方法论深度不足，我认为这低估了本文的贡献类型。\n\n**反驳理由**：\n\n1. **贡献类型是 problem formulation + benchmark + systematic analysis，不是 algorithmic novelty**。*ACL 有大量高影响力的此类论文——GLUE (Wang et al., 2018)、BIG-Bench (Srivastava et al., 2023)、各种 BERTology 分析论文——方法都不复杂，贡献在于问题定义和系统性评估。本文开辟了 \"recursive generation depth estimation\" 这一新 task，构建了 180K 的 benchmark，定义了 EDD 度量，这些是实质性贡献。\n\n2. **方法的简洁性本身有价值**。Table 3 (p.6) 显示 RF/XGB/LGBM 差异 ≤0.4pp，说明这不是一个需要复杂模型的问题——feature 设计才是关键。论文的 end-to-end PLM baseline (§5.5, Appendix A.8) 显示 DeBERTa/RoBERTa 仅达 ~59%，远低于手工特征的 78%+，这证明 domain knowledge-driven features 优于暴力 representation learning，是有信息量的 negative result。\n\n3. **EDD 不是 \"AUC threshold 的简单包装\"**。它提供了一个可比较的、跨配置的标准化度量。虽然定义简单，但其 utility 在于为 model collapse 研究建立了 quantifiable depth boundary 的概念框架。\n\n**但我承认 R2 的隐含观点有道理**：论文如果能在方法上多走一步（如 ordinal regression 替代 RF、learned features 替代手工特征的 hybrid approach），会更有说服力。当前版本确实在 Findings 和 Main 之间。\n\n---\n\n### 小问题\n\n**[AGREE] R2-小问题-1: Table 1 vs Table 2 accuracy 不一致（78.2% vs 78.8%）**\n如属实，这是排版/数据搬运错误，需要在 camera-ready 修正。我未在自己的审查中注意到此细节。\n\n**[AGREE] R2-小问题-2: Qwen2.5-7B U-shaped pattern 与 base model 的 tension**\n同意。论文脚注将 U-shaped pattern 归因于 instruction-tuning effects，但如果 base model 也是 non-monotonic，这个归因就不成立。这与 Limitations (p.7) 承认的 non-monotonicity 问题直接相关，也强化了我对 EDD 单调性假设的批评（我的 N1）。\n\n**[AGREE] R2-小问题-3: Ordinal classification 引用不足**\nFrank & Hall (2001) 是 ordinal classification 的经典工作，论文只引了 CORAL (Cao et al., 2020) 和 CLOC (Chen et al., 2025)。至少应该引 Frank & Hall，以及 Rennie & Srebro (2005) 的 loss functions for ordinal regression。这也呼应了我在 Questions Q5 中提出的建议——论文应更认真考虑 ordinal regression 方法。\n\n**[AGREE] R2-小问题-4: Zero-shot LLM ablation 给了 oracle information**\n好的观察。Appendix A.5 (p.11) 的 zero-shot LLM prompt 告诉模型 \"recursive generation depth\" 的概念和各深度的预期 pattern——这不是 zero-shot，而是 informed few-shot without examples。一个真正的 zero-shot baseline 不应包含关于 depth degradation patterns 的先验知识。这使 LLM baseline 的 36.29% 显得虚高而非虚低。\n\n**[AGREE] R2-小问题-5: Cross-domain 仅 arXiv 500 samples**\n同意。Appendix A.9 的 cross-domain 实验使用 arXiv 500 samples 在 single pipeline 上测试，样本量和 domain 覆盖都太有限。至少应加一个明显不同的 domain（如 code、dialogue、medical text）。\n\n---\n\n### Related Work 补充建议\n\n**[AGREE] Schaeffer et al. (2025) \"Position: Model Collapse Does Not Mean What You Think\"**\n高度相关。该论文对 model collapse 的常见叙事提出挑战，如果其论点成立，本文的基础假设（递归生成导致可检测的系统性退化）需要更谨慎的限定条件。必须引用并讨论。\n\n**[AGREE] \"A Closer Look at Model Collapse\" (2025) — memorization perspective**\n论文 Related Work (p.2) 已引用了类似工作（\"data retention\", Georgiou et al., 2025），但 memorization perspective 确实未充分讨论。\n\n**[AGREE，但影响有限] C2PA/Content Credentials framework**\nDiscussion §6 提到 watermarking 和 source attribution (Kirchenbauer et al., 2023; Uchendu et al., 2020)，但未提及 C2PA 这一工业标准框架。作为 provenance toolkit 讨论的一部分，应该提及。不过对论文核心论点影响不大。\n\n**[REBUT] Mohamed et al. \"Broken Telephone\" 需更深入讨论**\n论文 Related Work (p.2) 已经引用了 Mohamed et al. (2025) \"LLM as a Broken Telephone: Iterative Generation Distorts Information\"。R2 要求 \"更深入讨论\"，但这篇论文关注的是 information distortion（语义漂移），而本文关注的是 statistical fingerprints（分布特征）。两者的 angle 不同，当前引用深度已足够。当然，如果能用 1-2 句话明确区分二者的关注点会更好。\n\n---\n\n### 综合评估：与我自己审稿意见的异同\n\n**高度一致的领域**：\n- Cross-scale 混淆变量（我的 N4 ≈ R2 的 W3）\n- Abstract/claims 的 overstatement（我的 W4/W5 ≈ R2 的 N1/W1）\n- Reference model 问题（我的 N2 和 R2 的 §8 讨论都涉及）\n\n**R2 发现而我遗漏的**：\n- Curation PoC 统计不显著（R2-N2）：重要遗漏，我错误地将 PoC 列为优势\n- Zero-shot LLM prompt 含 oracle information（R2-小问题-4）\n- Table 1 vs Table 2 数据不一致（R2-小问题-1）\n\n**我发现而 R2 未强调的**：\n- 5-fold CV 样本非独立性（我的 N3）：R2 未提及这个方法论问题\n- EDD 定义的 classifier-dependence 和序关系不一致性（我的 N1, W3）\n- VIF 对 SHAP 稳定性的影响（我的 W2）\n\n**核心分歧**：\n- **方法论深度**（R2-W4）：R2 认为方法过于轻量，我认为 benchmark/problem-formulation 型贡献在 *ACL 是合法的贡献类型。这是主要分歧点。\n\n**总体**：两份审稿互补性强。R2 侧重 novelty framing 和 claim 校准，我侧重统计方法论和实验设计。综合看，论文的核心贡献（问题定义 + 特征发现）有价值，但 claims 需要显著 tone down，多个实验环节需要加固。我维持 **3/5 (Findings)** 的评分。",
  "reviewer_id": "1",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 意见的逐条交叉回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: \"Universal\" claim 证据不足**\n\n同意 R2 的核心判断。虽然 Abstract 确实加了限定语 \"across the three model families and three decoding strategies studied\"（p.1），但 \"universal\" 一词仍然过强。关键证据：\n\n1. Table 4 (p.6) 的 cross-model transfer mean accuracy 为 66.4%，但观察 per-holdout 结果，OLMo holdout 的 d1 recall 仅约 17.5%，Pythia holdout 的 d2 recall 约 24.8%——这说明跨模型泛化在中间深度极不稳定。\n2. 所有模型均为 decoder-only transformer、参数规模 1–1.5B，架构同质性高。encoder-decoder（T5/BART）、mixture-of-experts 等架构完全未覆盖。\n3. \"Universal\" 在 NLP 社区有明确含义（如 Universal Sentence Encoder、Universal Dependencies），暗示广泛适用性，与当前证据不匹配。\n\nR2 建议的 \"consistent across the three model families studied\" 措辞更准确。我进一步建议在 Discussion 中添加一段明确列出 \"universal\" 成立所需的额外验证（encoder-decoder、MoE、>13B scale）。\n\n**与我自己审稿的关系**：我的 N4（cross-scale 混淆变量）从实验设计角度指出了同类问题——证据基础太窄无法支撑强泛化声明。R2 从语言层面切入，二者互补。\n\n---\n\n**[AGREE] R2-N2: Curation PoC 统计不显著**\n\n同意。从 Appendix A.11 Table 13–14 (p.14) 的数据看：\n\n1. **关键对比不显著**：RF-filtered vs unfiltered（即\"过滤了是否比不过滤好？\"）的 p 值均 >0.4。这意味着在统计意义上，depth-based 过滤后训练的模型并不比用全部数据训练的模型更好。\n2. **显著对比的含金量低**：RF vs random subsampling 显著（p<0.02），但这只证明 \"有信息的选择优于随机丢弃\"——一个很低的 bar。任何合理的数据质量指标（如 perplexity 阈值）都可能超过随机丢弃。\n3. **统计功效不足**：仅 5 个 seed 的 paired t-test，检测中等 effect size 的 power 很低。但这不能作为维持 contribution claim 的理由——如果 effect size 小到 5 seeds 检测不到，其实际价值也有限。\n\nR2 建议将 curation 从 contribution 降级为 \"preliminary exploration\" 是合理的。论文 §1 的 contribution list 第 4 条应相应修改。\n\n**补充**：我在 Round 1 中将 curation PoC 列为优势（\"Downstream 应用验证\"），现在在 R2 的指出下修正——PoC 的方向正确，但统计证据不足以作为 contribution 列出。\n\n---\n\n**[AGREE，但需要补充 nuance] R2-N3: Perplexity tail statistics 的 novelty 受限**\n\n部分同意 R2 的判断，但认为 novelty 不是零。\n\n**同意的部分**：\n- Dohmatob et al. (2024) \"A Tale of Tails\" 确实已建立 \"recursive training erodes distributional tails\" 的理论框架。论文的 p90_ppl 和 var_surprisal 作为 dominant features 的发现在概念上是这一理论的 empirical realization。\n- 论文当前的 framing（§4.2, §6）未充分 acknowledge 这一理论先驱，读起来像是独立发现了 tail erosion。\n\n**需要 nuance 的部分**：\n- 从 \"theory predicts tails erode\" 到 \"tail erosion is monotonic across 4+ depths, quantifiable via specific percentile statistics, and classifiable with >70% ordinal accuracy\" 之间存在 non-trivial gap。理论预测了定性方向，论文提供了定量操作化。\n- EDD 框架将 tail erosion 的 \"何时变得不可区分\" 量化为具体 threshold 下的 depth boundary（§4.3, Table 17, Appendix A.16），这超出了 Dohmatob 的理论范围。\n- Feature ranking 的发现（top-2 features 达到 full-set 91.1% accuracy, §4.2）为实际部署提供了 actionable guidance。\n\n**结论**：R2 的建议完全正确——论文需要在 Related Work 和 Introduction 中明确区分 \"theory predicts tails erode\"（Dohmatob 的贡献）与 \"we operationalize this into a classifiable, quantifiable, ordinal depth estimation framework\"（本文贡献）。这不是降低 novelty，而是更诚实地定位贡献。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Abstract 对 transfer 结果的呈现不平衡**\n\n完全同意。Abstract (p.1) 报告 \"Cross-model transfer reaches 66.8%\"，但未提及：\n- d1-d3 子集的大幅下降（从 Table 4 可见，去掉几乎 100% 的 d0 后，实际深度区分能力显著弱化）\n- Cross-strategy 仅 59.1%（§5.3, Table 5）\n- Cross-scale 仅 60.1%–70.2%（§5.4, Table 6）\n\nAbstract 应至少用一句话 acknowledge transfer gap，例如 \"though transfer accuracy degrades substantially for intermediate depths, ranging from 55–67% across model and strategy holdouts.\"\n\n**与我自己审稿的关系**：我的 W4（wild data FPR）和 W5（cross-strategy 下降）从不同角度指出了同样的 overstatement 模式。\n\n---\n\n**[AGREE] R2-W2: Cross-model recursive chain 的 architecture confound**\n\n同意。Appendix A.13 (p.14) 的 cross-model recursive chain 实验仅测试了两条 chain（forward: Pythia→OLMo→GPT-2 和 reverse）。3 个模型有 3!=6 种排列，仅测 2 种不足以消除 architecture ordering confound。\n\n补充证据：从 p.14 可见 forward chain 达到 84.75%——但如果 reverse chain 准确率显著不同（论文未明确报告 reverse chain 的单独准确率），则 ordering effect 可能不可忽略。\n\n---\n\n**[AGREE] R2-W3: 7B cross-scale confounds**\n\n完全同意，这与我自己的 N4 高度重合。R2 进一步指出了 base vs instruct 对比中的混淆——论文 §5.4 提到 \"instruction-tuning regularizes\"（p.6），但 base model 也展现 non-monotonic pattern，说明 instruction-tuning 不是唯一因素。这个因果推断确实过于 confident。\n\n---\n\n**[REBUT] R2-W4: 方法论贡献轻量**\n\n不完全同意。R2 认为 \"19 perplexity features + RF\" 对 EMNLP main 方法论深度不足，我认为这低估了本文的贡献类型。\n\n**反驳理由**：\n\n1. **贡献类型是 problem formulation + benchmark + systematic analysis，不是 algorithmic novelty**。*ACL 有大量高影响力的此类论文——GLUE (Wang et al., 2018)、BIG-Bench (Srivastava et al., 2023)、各种 BERTology 分析论文——方法都不复杂，贡献在于问题定义和系统性评估。本文开辟了 \"recursive generation depth estimation\" 这一新 task，构建了 180K 的 benchmark，定义了 EDD 度量，这些是实质性贡献。\n\n2. **方法的简洁性本身有价值**。Table 3 (p.6) 显示 RF/XGB/LGBM 差异 ≤0.4pp，说明这不是一个需要复杂模型的问题——feature 设计才是关键。论文的 end-to-end PLM baseline (§5.5, Appendix A.8) 显示 DeBERTa/RoBERTa 仅达 ~59%，远低于手工特征的 78%+，这证明 domain knowledge-driven features 优于暴力 representation learning，是有信息量的 negative result。\n\n3. **EDD 不是 \"AUC threshold 的简单包装\"**。它提供了一个可比较的、跨配置的标准化度量。虽然定义简单，但其 utility 在于为 model collapse 研究建立了 quantifiable depth boundary 的概念框架。\n\n**但我承认 R2 的隐含观点有道理**：论文如果能在方法上多走一步（如 ordinal regression 替代 RF、learned features 替代手工特征的 hybrid approach），会更有说服力。当前版本确实在 Findings 和 Main 之间。\n\n---\n\n### 小问题\n\n**[AGREE] R2-小问题-1: Table 1 vs Table 2 accuracy 不一致（78.2% vs 78.8%）**\n如属实，这是排版/数据搬运错误，需要在 camera-ready 修正。我未在自己的审查中注意到此细节。\n\n**[AGREE] R2-小问题-2: Qwen2.5-7B U-shaped pattern 与 base model 的 tension**\n同意。论文脚注将 U-shaped pattern 归因于 instruction-tuning effects，但如果 base model 也是 non-monotonic，这个归因就不成立。这与 Limitations (p.7) 承认的 non-monotonicity 问题直接相关，也强化了我对 EDD 单调性假设的批评（我的 N1）。\n\n**[AGREE] R2-小问题-3: Ordinal classification 引用不足**\nFrank & Hall (2001) 是 ordinal classification 的经典工作，论文只引了 CORAL (Cao et al., 2020) 和 CLOC (Chen et al., 2025)。至少应该引 Frank & Hall，以及 Rennie & Srebro (2005) 的 loss functions for ordinal regression。这也呼应了我在 Questions Q5 中提出的建议——论文应更认真考虑 ordinal regression 方法。\n\n**[AGREE] R2-小问题-4: Zero-shot LLM ablation 给了 oracle information**\n好的观察。Appendix A.5 (p.11) 的 zero-shot LLM prompt 告诉模型 \"recursive generation depth\" 的概念和各深度的预期 pattern——这不是 zero-shot，而是 informed few-shot without examples。一个真正的 zero-shot baseline 不应包含关于 depth degradation patterns 的先验知识。这使 LLM baseline 的 36.29% 显得虚高而非虚低。\n\n**[AGREE] R2-小问题-5: Cross-domain 仅 arXiv 500 samples**\n同意。Appendix A.9 的 cross-domain 实验使用 arXiv 500 samples 在 single pipeline 上测试，样本量和 domain 覆盖都太有限。至少应加一个明显不同的 domain（如 code、dialogue、medical text）。\n\n---\n\n### Related Work 补充建议\n\n**[AGREE] Schaeffer et al. (2025) \"Position: Model Collapse Does Not Mean What You Think\"**\n高度相关。该论文对 model collapse 的常见叙事提出挑战，如果其论点成立，本文的基础假设（递归生成导致可检测的系统性退化）需要更谨慎的限定条件。必须引用并讨论。\n\n**[AGREE] \"A Closer Look at Model Collapse\" (2025) — memorization perspective**\n论文 Related Work (p.2) 已引用了类似工作（\"data retention\", Georgiou et al., 2025），但 memorization perspective 确实未充分讨论。\n\n**[AGREE，但影响有限] C2PA/Content Credentials framework**\nDiscussion §6 提到 watermarking 和 source attribution (Kirchenbauer et al., 2023; Uchendu et al., 2020)，但未提及 C2PA 这一工业标准框架。作为 provenance toolkit 讨论的一部分，应该提及。不过对论文核心论点影响不大。\n\n**[REBUT] Mohamed et al. \"Broken Telephone\" 需更深入讨论**\n论文 Related Work (p.2) 已经引用了 Mohamed et al. (2025) \"LLM as a Broken Telephone: Iterative Generation Distorts Information\"。R2 要求 \"更深入讨论\"，但这篇论文关注的是 information distortion（语义漂移），而本文关注的是 statistical fingerprints（分布特征）。两者的 angle 不同，当前引用深度已足够。当然，如果能用 1-2 句话明确区分二者的关注点会更好。\n\n---\n\n### 综合评估：与我自己审稿意见的异同\n\n**高度一致的领域**：\n- Cross-scale 混淆变量（我的 N4 ≈ R2 的 W3）\n- Abstract/claims 的 overstatement（我的 W4/W5 ≈ R2 的 N1/W1）\n- Reference model 问题（我的 N2 和 R2 的 §8 讨论都涉及）\n\n**R2 发现而我遗漏的**：\n- Curation PoC 统计不显著（R2-N2）：重要遗漏，我错误地将 PoC 列为优势\n- Zero-shot LLM prompt 含 oracle information（R2-小问题-4）\n- Table 1 vs Table 2 数据不一致（R2-小问题-1）\n\n**我发现而 R2 未强调的**：\n- 5-fold CV 样本非独立性（我的 N3）：R2 未提及这个方法论问题\n- EDD 定义的 classifier-dependence 和序关系不一致性（我的 N1, W3）\n- VIF 对 SHAP 稳定性的影响（我的 W2）\n\n**核心分歧**：\n- **方法论深度**（R2-W4）：R2 认为方法过于轻量，我认为 benchmark/problem-formulation 型贡献在 *ACL 是合法的贡献类型。这是主要分歧点。\n\n**总体**：两份审稿互补性强。R2 侧重 novelty framing 和 claim 校准，我侧重统计方法论和实验设计。综合看，论文的核心贡献（问题定义 + 特征发现）有价值，但 claims 需要显著 tone down，多个实验环节需要加固。我维持 **3/5 (Findings)** 的评分。",
    "reviewer_id": "1",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 229 · 2026-05-16T17:28:40.038347+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3665
}
```

</details>

---


### Assistant

_source line 230 · 2026-05-16T17:28:48.860047+00:00_

交叉回应已提交。

总结：
- 对 R2 的 3 个 Must-Fix 全部 **[AGREE]**（N1 universal 措辞、N2 curation PoC 不显著、N3 novelty positioning），其中 N3 补充了 nuance
- 对 4 个 Should-Fix 中 3 个 **[AGREE]**（W1 abstract 不平衡、W2 chain permutation 不足、W3 cross-scale confounds），1 个 **[REBUT]**（W4 方法论轻量——benchmark/problem-formulation 型贡献在 *ACL 是合法的）
- 5 个小问题全部 **[AGREE]**，related work 建议 3 个 AGREE + 1 个 REBUT（Broken Telephone 已引用且角度不同）
- 修正了自己 Round 1 的一个判断：curation PoC 从"优势"降级
- 指出 R2 未覆盖的问题：CV 样本非独立性、EDD classifier-dependence、VIF-SHAP 稳定性
- 维持 **3/5 (Findings)** 评分

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1"
}
```

</details>

---


## Round 9

## Round 9

64 recorded events


### User

_source line 231 · 2026-05-16T19:30:52.012935+00:00_

[Round 6 审稿请求]:
## Round 6 审稿任务 — Reviewer 1（方法严谨性 + 实验有效性）

### Venue 信息
- **目标**: EMNLP 2026 Main Conference (ARR May cycle)
- **Deadline**: 2026-05-25
- **格式**: ACL 模板，8 页正文 + 无限参考文献，double-blind
- **论文路径**: projects/recursive_gen_depth_est/docs/paper/main.tex

### 你的审查侧重
方法严谨性、统计证据充分性、实验设计合理性、confound 控制。

### 上轮（Round 5）你的主要发现中仍 open/in_progress 的问题

请逐条检查以下问题在当前论文版本中是否已充分解决：

1. **R1-W1** (in_progress): Feature importance multicollinearity——论文已有 VIF 分析和三种 importance measure concordance (W=0.90)，但需确认是否已将 claim 从 individual feature level 调整到 feature GROUP level。
2. **R1-W3** (in_progress): LoRA rank sensitivity analysis——要求至少一个 cell 测试 rank ∈ {4, 16, 64}。检查是否已补充。
3. **R4-N2** (in_progress): Zero-shot LLM baseline 结构性不公平——应重新定位为 "surface-text ablation" 而非 baseline comparison。检查 §6 Discussion 是否仍含 superiority framing。
4. **R4-N3** (in_progress): Cross-scale 声明基于 N=2 confound-stacked 7B 模型——abstract/introduction 是否已加 "preliminary" qualification？
5. **R5-N2** (open): Reference model 循环依赖——Pythia 同时为 generator 和 reference，仅测试 2 个同族 1B reference。是否补充了 architecturally distinct reference 或明确 Limitations 讨论？
6. **R5-W1** (open): Single LoRA instance per depth——5-Fold CV 样本非独立性。是否在 Discussion/Limitations 讨论？
7. **R5-W2** (open): 方法部署需预知 decoding strategy——是否讨论了 strategy detection 作为 prerequisite？
8. **R5-W3** (open): Wild data FPR (GPT-2 XL C4: 22.4%) 削弱实用性声明。
9. **R5-W5** (open): EDD 定义的 classifier-dependence——是否明确为 operational measure 而非 intrinsic data property？

### 评审标准
- 对每个问题判断：[RESOLVED] / [PARTIALLY ADDRESSED] / [NOT ADDRESSED] / [REGRESSED]
- 识别本轮修改是否引入新问题
- 特别关注：统计声明是否有充分证据支撑，experimental claims 是否 properly qualified

### 输出格式
```
## 遗留问题评估
[逐条评估]

## 新发现
[如有]

## Strengths（本版本）
## Weaknesses（Must-Fix / Should-Fix / Minor）
## Questions for Authors
## Overall Assessment
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 232 · 2026-05-16T19:31:10.962534+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
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

_source line 233 · 2026-05-16T19:31:10.963072+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 234 · 2026-05-16T19:31:11.917942+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 235 · 2026-05-16T19:31:11.968748+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 236 · 2026-05-16T19:31:17.953852+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
  "pages": "1-8",
  "dpi": "180"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
    "pages": "1-8",
    "dpi": "180"
  }
}
```

</details>

---


### Tool call

_source line 237 · 2026-05-16T19:31:18.256362+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
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

_source line 238 · 2026-05-16T19:31:21.581045+00:00_

Error: result (6,453,272 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/f5009a54-ac13-49a4-83d8-13bbafebaca9/tool-results/mcp-agent-ml-research-pdf_to_images-1778959881147.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/f5009a54-ac13-49a4-83d8-13bbafebaca9/tool-results/mcp-agent-ml-research-pdf_to_images-1778959881147.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/f5009a54-ac13-49a4-83d8-13bbafebaca9/tool-results/mcp-agent-ml-research-pdf_to_images-1778959881147.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 3627
}
```

</details>

---


### Tool result

_source line 239 · 2026-05-16T19:31:21.581416+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 3325
}
```

</details>

---


### Tool call

_source line 240 · 2026-05-16T19:31:33.729742+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
  "pages": "1-2",
  "dpi": "160"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
    "pages": "1-2",
    "dpi": "160"
  }
}
```

</details>

---


### Tool call

_source line 241 · 2026-05-16T19:31:33.882055+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer form criteria scoring guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer form criteria scoring guidelines"
  }
}
```

</details>

---


### Tool result

_source line 242 · 2026-05-16T19:31:34.552322+00:00_

Error: result (1,410,114 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/f5009a54-ac13-49a4-83d8-13bbafebaca9/tool-results/mcp-agent-ml-research-pdf_to_images-1778959894471.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/f5009a54-ac13-49a4-83d8-13bbafebaca9/tool-results/mcp-agent-ml-research-pdf_to_images-1778959894471.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/f5009a54-ac13-49a4-83d8-13bbafebaca9/tool-results/mcp-agent-ml-research-pdf_to_images-1778959894471.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 822
}
```

</details>

---


### Tool result

_source line 243 · 2026-05-16T19:31:42.820775+00:00_

Web search results for query: "ACL ARR 2026 reviewer form criteria scoring guidelines"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

Based on the search results, here is information about the ACL ARR 2026 reviewer form criteria and scoring guidelines:

## Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall 
…[truncated 1265 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8938
}
```

</details>

---


### Tool call

_source line 244 · 2026-05-16T19:31:51.813007+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
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

_source line 245 · 2026-05-16T19:31:51.813361+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 246 · 2026-05-16T19:31:52.216037+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/_pdf_images/*.png",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/_pdf_images/*.png",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 247 · 2026-05-16T19:31:52.266620+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p9.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p10.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p11.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p12.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p13.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p14.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p15.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p16.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p3.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p4.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p5.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p6.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p7.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p8.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p1.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p2.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 248 · 2026-05-16T19:32:14.209141+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read paper pages 1-4",
  "prompt": "Read the following PNG images of a research paper and extract ALL text content verbatim (especially section titles, claims, equations, and table/figure captions). Focus on: title, abstract, introduction, and beginning of methodology.\n\nRead these files in order:\n1. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p1.png\n2. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p2.png\n3. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p3.png\n4. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p4.png\n\nFor each page, report:\n- All section/subsection headings\n- Key claims and qualifications (especially in abstract/intro - look for words like \"preliminary\", \"initial\", \"limited\")\n- Any mention of cross-scale generalization, LoRA rank, feature importance, multicollinearity, VIF\n- Table/figure content if present\n- Footnotes\n\nReturn the FULL extracted text, preserving structure. Do not summarize.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Agent",
  "tool_args": {
    "description": "Read paper pages 1-4",
    "prompt": "Read the following PNG images of a research paper and extract ALL text content verbatim (especially section titles, claims, equations, and table/figure captions). Focus on: title, abstract, introduction, and beginning of methodology.\n\nRead these files in order:\n1. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p1.png\n2. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p2.png\n3. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p3.png\n4. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p4.png\n\nFor each page, report:\n- All section/subsection headings\n- Key claims and qualifications (especially in abstract/intro - look for words like \"preliminary\", \"initial\", \"limited\")\n- Any mention of cross-scale generalization, LoRA rank, feature importance, multicollinearity, VIF\n- Table/figure content if present\n- Footnotes\n\nReturn the FULL extracted text, preserving structure. Do not summarize.",
    "subagent_type": "general-purpose"
  }
}
```

</details>

---


### Tool call

_source line 249 · 2026-05-16T19:32:20.440109+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 250 · 2026-05-16T19:32:20.440543+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 251 · 2026-05-16T19:32:20.441159+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 252 · 2026-05-16T19:32:20.441416+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 253 · 2026-05-16T19:32:20.444070+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3
}
```

</details>

---


### Tool call

_source line 254 · 2026-05-16T19:32:20.444451+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 255 · 2026-05-16T19:32:20.444810+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read paper pages 5-8",
  "prompt": "Read the following PNG images of a research paper and extract ALL text content verbatim (especially section titles, experimental details, tables, and figures). Focus on: experiments section, results, ablations, and any discussion of LoRA rank sensitivity, feature groups, zero-shot LLM baselines.\n\nRead these files in order:\n1. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p5.png\n2. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p6.png\n3. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p7.png\n4. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p8.png\n\nFor each page, report:\n- All section/subsection headings\n- Experimental setup details (models used, datasets, metrics)\n- Table content (reproduce tables as markdown if possible)\n- Discussion of: LoRA rank experiments, zero-shot LLM as \"surface-text ablation\" vs baseline, wild data FPR results, cross-scale claims and qualifications\n- Any Limitations or Discussion section content\n- Figure captions and descriptions\n\nReturn the FULL extracted text, preserving structure. Do not summarize.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Agent",
  "tool_args": {
    "description": "Read paper pages 5-8",
    "prompt": "Read the following PNG images of a research paper and extract ALL text content verbatim (especially section titles, experimental details, tables, and figures). Focus on: experiments section, results, ablations, and any discussion of LoRA rank sensitivity, feature groups, zero-shot LLM baselines.\n\nRead these files in order:\n1. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p5.png\n2. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p6.png\n3. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p7.png\n4. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p8.png\n\nFor each page, report:\n- All section/subsection headings\n- Experimental setup details (models used, datasets, metrics)\n- Table content (reproduce tables as markdown if possible)\n- Discussion of: LoRA rank experiments, zero-shot LLM as \"surface-text ablation\" vs baseline, wild data FPR results, cross-scale claims and qualifications\n- Any Limitations or Discussion section content\n- Figure captions and descriptions\n\nReturn the FULL extracted text, preserving structure. Do not summarize.",
    "subagent_type": "general-purpose"
  }
}
```

</details>

---


### Tool result

_source line 256 · 2026-05-16T19:32:26.676534+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 6235
}
```

</details>

---


### Tool result

_source line 257 · 2026-05-16T19:32:26.677361+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 6232
}
```

</details>

---


### Tool call

_source line 258 · 2026-05-16T19:32:26.677713+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 259 · 2026-05-16T19:32:26.682221+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 260 · 2026-05-16T19:32:26.682628+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 261 · 2026-05-16T19:32:26.682908+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 262 · 2026-05-16T19:32:26.683549+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 5
}
```

</details>

---


### Tool result

_source line 263 · 2026-05-16T19:32:26.688344+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 6
}
```

</details>

---


### Tool call

_source line 264 · 2026-05-16T19:32:26.688800+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read paper pages 9-12",
  "prompt": "Read the following PNG images of a research paper and extract ALL text content verbatim. Focus on: discussion, limitations, conclusion, and beginning of appendix. Pay special attention to:\n- Any discussion of reference model circular dependency / architecturally distinct references\n- Discussion of single LoRA instance per depth / 5-Fold CV sample non-independence\n- Discussion of deployment requiring pre-known decoding strategy / strategy detection\n- Wild data FPR discussion and practical deployment claims\n- EDD definition discussion (classifier-dependence vs intrinsic property)\n- Any \"Limitations\" section content\n\nRead these files in order:\n1. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p9.png\n2. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p10.png\n3. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p11.png\n4. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p12.png\n\nReturn the FULL extracted text, preserving structure. Do not summarize.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Agent",
  "tool_args": {
    "description": "Read paper pages 9-12",
    "prompt": "Read the following PNG images of a research paper and extract ALL text content verbatim. Focus on: discussion, limitations, conclusion, and beginning of appendix. Pay special attention to:\n- Any discussion of reference model circular dependency / architecturally distinct references\n- Discussion of single LoRA instance per depth / 5-Fold CV sample non-independence\n- Discussion of deployment requiring pre-known decoding strategy / strategy detection\n- Wild data FPR discussion and practical deployment claims\n- EDD definition discussion (classifier-dependence vs intrinsic property)\n- Any \"Limitations\" section content\n\nRead these files in order:\n1. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p9.png\n2. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p10.png\n3. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p11.png\n4. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p12.png\n\nReturn the FULL extracted text, preserving structure. Do not summarize.",
    "subagent_type": "general-purpose"
  }
}
```

</details>

---


### Tool result

_source line 265 · 2026-05-16T19:32:30.806046+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4123
}
```

</details>

---


### Tool result

_source line 266 · 2026-05-16T19:32:30.806654+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4123
}
```

</details>

---


### Tool call

_source line 267 · 2026-05-16T19:32:30.806844+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 268 · 2026-05-16T19:32:30.807030+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 269 · 2026-05-16T19:32:30.957713+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read paper pages 13-16",
  "prompt": "Read the following PNG images of a research paper and extract ALL text content verbatim. These are likely appendix/supplementary pages. Focus on:\n- LoRA rank sensitivity analysis (rank 4, 16, 64 experiments)\n- VIF analysis / multicollinearity discussion\n- Feature importance concordance (Kendall's W)\n- Any additional ablation results\n- Cross-architecture reference model experiments\n- Any additional tables/figures\n\nRead these files in order:\n1. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p13.png\n2. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p14.png\n3. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p15.png\n4. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p16.png\n\nReturn the FULL extracted text, preserving structure. Do not summarize.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Agent",
  "tool_args": {
    "description": "Read paper pages 13-16",
    "prompt": "Read the following PNG images of a research paper and extract ALL text content verbatim. These are likely appendix/supplementary pages. Focus on:\n- LoRA rank sensitivity analysis (rank 4, 16, 64 experiments)\n- VIF analysis / multicollinearity discussion\n- Feature importance concordance (Kendall's W)\n- Any additional ablation results\n- Cross-architecture reference model experiments\n- Any additional tables/figures\n\nRead these files in order:\n1. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p13.png\n2. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p14.png\n3. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p15.png\n4. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p16.png\n\nReturn the FULL extracted text, preserving structure. Do not summarize.",
    "subagent_type": "general-purpose"
  }
}
```

</details>

---


### Tool result

_source line 270 · 2026-05-16T19:32:31.261424+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool result

_source line 271 · 2026-05-16T19:32:31.262205+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 272 · 2026-05-16T19:32:31.262542+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 273 · 2026-05-16T19:32:31.262808+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 274 · 2026-05-16T19:32:32.472446+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1209
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-16T19:32:32.473144+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1210
}
```

</details>

---


### Tool call

_source line 276 · 2026-05-16T19:32:32.523559+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with ALL scoring criteria, their scales, descriptions, and any guidance for reviewers. Include all fields like soundness, excitement, overall assessment, confidence, etc. Return the full structured content."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with ALL scoring criteria, their scales, descriptions, and any guidance for reviewers. Include all fields like soundness, excitement, overall assessment, confidence, etc. Return the full structured content."
  }
}
```

</details>

---


### Tool call

_source line 277 · 2026-05-16T19:32:33.879331+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 278 · 2026-05-16T19:32:34.383097+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 279 · 2026-05-16T19:32:35.287727+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1408
}
```

</details>

---


### Tool result

_source line 280 · 2026-05-16T19:32:35.288582+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 281 · 2026-05-16T19:32:35.288913+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 282 · 2026-05-16T19:32:35.489902+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 283 · 2026-05-16T19:32:35.490756+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 284 · 2026-05-16T19:32:35.893777+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---


### Tool result

_source line 285 · 2026-05-16T19:32:40.362024+00:00_

# ACL Rolling Review Form - Complete Structure

## Core Review Sections

**Paper Summary**: Describe paper topic to aid understanding by editors and area chairs.

**Summary of Strengths**: "major reasons to publish this paper at a selective *ACL venue" including methodology, empirical results, theoretical analysis, or literature organization.

**Summary of Weaknesses**: Numbered concerns about correctness, impact, clarity, or other publication barriers.

**Comments/Suggestions/Typos**: Additional improvement suggestions beyond addressing weaknesses.

## Scoring Criteria

### Reviewer Confidence (1-5 scale)
- 5: "Positive that my evaluation is correct"
- 4: Quite sure; unlikely to miss critical points
- 3: Pretty sure; may lack detailed verification
- 2: "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- 1: Outside expertise or incomprehensible paper

### Soundness (1-5 scale with half-points)
- 5: "one of the most thorough I have seen"
- 4: Strong support for claims
- 3: Adequate support; minor gaps acceptable
- 2: Major technical/methodological problems
- 1: Insufficient rigor or relevance to ACL

### Excitement (1-5 scale with half-points)
- 5: "Highly Exciting: I would recommend this paper to others"
- 4: Would mention to colleagues
- 3: Might mention or attend presentation
- 2: Potentially interesting to others
- 1: "Not Exciting" and unlikely community interest

### Overall Assessment (1-5 scale with half-points)
- 5: Consider for Award (top 2.5% papers)
- 4: Conference acceptance recommended
- 3: Findings track consideration
- 2: Substantial revisions needed
- 1: Do not resubmit or lacks relevance

## Additional Evaluation Areas

**Limitations and Societal Impact**: Assess author discussion of constraints, potential harms, excluded groups, and dual-use concerns.

**Ethical Concerns**: Review against ACL Code of Ethics; flag papers requiring specialized ethics committee review.

**Reproducibility** (1-5 scale): From easily r
…[truncated 330 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7838
}
```

</details>

---


### Tool result

_source line 286 · 2026-05-16T19:34:39.630950+00:00_



## Page 1 — Full Extracted Text

---

**Title:** How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints

**Authors:** Anonymous ACL submission

---

### Abstract

As large language models increasingly train on web text containing their own outputs, a recursive model→data→model loop arises— yet no method estimates how many such iterations a text has undergone. We formalize recursive generation depth estimation as an ordinal classification and construct a benchmark of 180K passages spanning 3 model families, 3 decoding strategies, and 4 generation depths. From each passage we extract a compact statistical fingerprint—19 candidate features dominated by perplexity tail statistics, with the top 5 achieving 97.6% of full-set performance—compared against a fixed reference model (Pythia-1.4B). A Random Forest classifier achieves 70.8% four-class accuracy (chance = 25%; 58.8–82.6% when excluding the most perfectly separable d0 class), a zero-shot LLM baseline reaches only 36.2%, with 90th-percentile perplexity and surprisal variance emerging as consistent depth markers across the studied 3 × 3 grid (key 3 importance in 9/9 and 8/9 cells, respectively). Our Depth Degradation Atlas reveals that decoding strategy reshapes degradation trajectories more than merely attenuating them, and we define the *Effective Discriminable Depth* (EDD&lt;sub>T&lt;/sub>=1 for extended recursive finding, EDD&lt;sub>T&lt;/sub>=1 for extended recursive chains. Cross-model transfer reaches 66.4% and cross-strategy transfer 59.1%; temperature sampling induces a d0↔2 AUC inversion that we decompose into a *perceptual* scale component and a residual structural component. Cross-model recursive chains—where each depth is generated by a different architecture— achieve 84.75%, and extending to two 7B-scale generators yields 70.2% accuracy with monotonic AUC decay (EDD=4), while a second 7B architecture exhibits EDD≥5 with a non-monotonic trajectory possibly linked to instruction-tu
…[truncated 16571 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Agent",
  "elapsed_ms": 145421
}
```

</details>

---


### Tool result

_source line 287 · 2026-05-16T19:34:40.635078+00:00_



Here is the full extracted text from all four pages:

---

## Page 13

while RF achieves 0.596 d2 recall, a >2× advantage at the hardest depth class.

Table 11: Per-class performance for end-to-end PLM classifiers vs. RF baseline (Pythia-1.4B nucleus). PLM columns report F1; RF d2 column reports recall at depth class with the largest PLM–RF gap). Both PLM backbones share the same failure pattern: collapsed d1/d2 distinctions despite adequate d0/d3.

| Model | d0 CV | d1 | d2 | d3 |
|-------|-------|----|----|----|
| DeBERTa-v3 | 58.3 ± 4.7 | .947 | .378 | .247 | .655 |
| RoBERTa-lg | 59.5 ± 2.2 | .938 | .416 | .261 | .647 |
| RF (11 feat) | | | | .596* |

*Recall; shown for the depth class with the largest PLM–RF gap.

**Feature space divergence.** SHAP TreeExplainer analysis confirms that perplexity and surprisal features account for 68.8% of RF's total contribution. Three independent importance measures—SHAP, Gini, and permutation—show strong concordance (Kendall's W = 0.90, p<0.005; pairwise Spearman ρ: SHAP–Gini 0.83, SHAP–permutation 0.81; see Table 16). Gini importance assigns p_82.4% with p_95.0 appearing in the SHAP top-2 in 9/9 cells and var_surprisal in 8/9.

Linear probing of PLM [CLS] representations yields negative Δr for both var_surprisal and p90_p10 (§A.7), indicating that pretrained representations lack the linear structure needed to recover perplexity tail statistics—a systematic representational gap rather than a bag-of-hyperparameters artifact.

ECOL (Plawiak et al., 2023) reached 64.5% (§A.4); all end-to-end approaches (58–65%) underperform feature-based methods, suggesting depth estimation benefits from targeted statistical features that capture distributional tail properties absent from PLM representations. This comparison is bounded by backbone scale (<125M parameters); whether larger PLMs (e.g., 7B+) can close the gap via richer internal representations remains an open question.

**A.9 Domain Bias Analysis**

To assess whether the classifi
…[truncated 12913 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Agent",
  "elapsed_ms": 129677
}
```

</details>

---


### Tool result

_source line 288 · 2026-05-16T19:35:20.783652+00:00_



Here is the full extracted text from all four pages:

---

## PAGE 5 (main_p5.png)

**[Figure 1]** (top of page, left side)

A line chart titled with axis labels "Perplexity AUC" (y-axis) and "Depth d" (x-axis, values d0 through d4). Three lines are plotted:
- Pythia 1.4B (blue circles)
- GPT-2 XL (orange triangles)
- OLMo 1B (green squares)

Horizontal dashed lines mark τ = {0.65, 0.70, 0.75, 0.80}. All three curves converge below 0.70 at d4–d5. Shaded bands: bootstrap 95% CIs.

**Caption:** Figure 1: Binary pairwise AUC decay curves for three models (nucleus sampling, depth 0–5). VIF and var\_surprise reveals 14 to 18 features with VIF≤10, placing effective dimensionality at 4–5; forward selection confirms the dominant pair (p90\_ppl first in 69 cells, var\_surprisal in 39). The bivariate shifts with depth—var\_surprisal dominates at shallow boundaries while tail perplexity statistics take over deeper, consistent with model-collapse dynamics (Shumailov et al., 2024) (§5) (temperature heatmap in Figure 4, Appendix A.5).

---

of full accuracy; top-5 achieve 97.6%. VIF analysis reveals 14 to 18 features with VIF≤10, placing effective dimensionality at 4–5; forward selection confirms the dominant pair (p90\_ppl first in 69 cells, var\_surprisal in 39). The bivariate shifts with depth—var\_surprisal dominates at shallow boundaries while tail perplexity statistics take over deeper, consistent with model-collapse dynamics (Shumailov et al., 2024) (§5) (temperature heatmap in Figure 4, Appendix A.5).

### 4.3 Monotonicity and EDD Analysis

Depth features exhibit strong monotonic trends: perplexity tail statistics decrease with depth (Spearman ρ = −1 across cell-level medians) while repetition features increase (trajectories in Figure 3, Appendix A.1). Inter-depth distances are monotonically uniform (d0-vs-d1 AUC exceeds 0.99 in all cells, whereas d2-vs-d3 ranges from 0.69 to 0.89.

We extend to depth d=5 for all three models under nucleus sampling, training dedicated b
…[truncated 18358 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Agent",
  "elapsed_ms": 180338
}
```

</details>

---


### Tool result

_source line 289 · 2026-05-16T19:35:21.939546+00:00_



Here is the full extracted text from the four pages:

---

## Page 9 (References page, continued)

Neural Networks with Application to Age Estimation. *Pattern Recognition Letters*, 140:325–331. arXiv:1901.07884.

Elvis Dohmatob, Yunzhen Feng, and Julia Kempe. 2024a. Model Collapse Demystified: The Case of Regression. In *Proceedings of NeurIPS*. arXiv:2402.07712.

Elvis Dohmatob, Yunzhen Feng, Arjan Suhbatmaniam, and Julia Kempe. 2025. Strong Model Collapse. In *Proceedings of ICLR*. arXiv:2410.04840.

Elvis Dohmatob, Yunzhen Feng, Pu Yang, Francois Charton, and Julia Kempe. 2024b. A Tale of Tails: Model Collapse as a Change of Scaling Laws. In *Proceedings of ICML*. arXiv:2402.07043(78).

George Drayson, Emile Thinane, and Vasileios Lampos. 2025. Machine-generated text detection prevents language model collapse. In *Findings of EMNLP*. arXiv:2502.15654.

Ali Falahati, Mohammad Mohammad Amiri, Kate Larson, and Lukasz Golab. 2026. Curated Synthetic Data Doesn't Have to Destroy a Language Model: A Closer Study of Generative Retraining with Pluralistic Preferences. arXiv:2605.07724.

Matthew Finlayson, John Hewitt, Alexander Koller, Swabha Swayamdipta, and Ashish Sabharwal. 2024. Closing the Curious Case of Neural Text Degeneration. In *Proceedings of ICLR*. arXiv:2310.01693v2.

Esteban Garces Arias, Meimingwei Li, Christian Heumann, and Matthias Assenmacher. 2025. Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation. In *Proceedings of COLING*. arXiv:2410.06097.

Sebastian Gehrmann, Hendrik Strobelt, and Alexander M. Rush. 2019. GLTR: Statistical Detection and Visualization of Generated Text. In *Proceedings of ACL: System Demonstrations*. 199:606610.

Matthias Gerstgrasser, Rylan Schaeffer, Apratim Dey, Rafael Rafailov, Henry Sleight, John Hughes, Tomasz Korbak, Rajashree Agrawal, Dhruv Pai, Andrey Gromov, Daniel A. Roberts, Diyi Yang, David L. Donoho, and Sanmi Koyejo. 2024. Is Model Collapse Inevitable? Breaking the Curse of Recur
…[truncated 17406 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Agent",
  "elapsed_ms": 175250
}
```

</details>

---


### Tool call

_source line 290 · 2026-05-16T19:37:32.834082+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the key guidance about what reviewers should focus on, how to calibrate scores, what constitutes a \"must fix\" vs minor issue, and any specific guidance about statistical methodology papers or experimental papers. Return the full relevant text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the key guidance about what reviewers should focus on, how to calibrate scores, what constitutes a \"must fix\" vs minor issue, and any specific guidance about statistical methodology papers or experimental papers. Return the full relevant text."
  }
}
```

</details>

---


### Tool result

_source line 291 · 2026-05-16T19:37:44.612717+00:00_

# ARR Reviewer Guidelines: Key Guidance Summary

## What Reviewers Should Focus On

The guidelines emphasize a two-pass reading strategy: first skim to assess research question and methodology appropriateness, then conduct in-depth technical evaluation. Reviewers should "read the paper at least twice: skimming and in-depth reading" to avoid knee-jerk reactions.

Critical focus areas include:
- **Specificity**: Avoid vague critiques. Instead of "missing relevant references," specify which ones and why they matter.
- **Methodology validity**: Check for sound argumentation, proof validity, and technical correctness appropriate to the paper type.
- **Scope alignment**: Ensure claims match the evidence presented, avoiding overclaiming.

## Calibrating Scores

Starting February 2025, reviewers provide three distinct scores:

1. **Soundness**: "must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation."

2. **Excitement**: A separate, subjective measure reflecting personal interest—explicitly orthogonal to soundness assessment.

3. **Overall Assessment**: A composite recommendation reflecting soundness, excitement, novelty, and potential impact.

The guidance clarifies: papers can be technically sound but personally uninteresting, or vice versa. "All papers recommended for Findings and main conferences are expected to be sufficiently sound and reproducible."

## "Must Fix" vs. Minor Issues

The guidelines identify common problematic review patterns (H1-H17) that often aren't genuine weaknesses:

**Not grounds for rejection:**
- Results seeming obvious in retrospect (confirmation bias)
- Simplicity of methods ("goal is to solve the problem, not in a complex way")
- Negative results (actually valuable for field)
- Non-SOTA performance (neither necessary nor sufficient for contribution)
- Papers on non-English languages or niche topics
- Ackn
…[truncated 1511 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 11778
}
```

</details>

---


### Tool call

_source line 292 · 2026-05-16T19:40:13.101229+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 6 Review — Reviewer 1（方法严谨性 + 实验有效性）\n\n**Paper**: \"How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\"\n**Venue**: EMNLP 2026 Main Conference (ACL ARR May cycle)\n**审查侧重**: 方法严谨性、统计证据充分性、实验设计合理性、confound 控制\n\n---\n\n## 遗留问题评估\n\n### R1-W1: Feature importance multicollinearity [PARTIALLY ADDRESSED]\n\n**改进**: §4.2 现在明确报告 VIF>10 对 14-16 个 features (p3: \"variance inflation analysis reveals VIF>10 for 14–16 features, placing the effective independent dimensionality at 4–5\")，三种 importance measure 的 Kendall's W=0.90 concordance (Appendix A.2)，以及 \"dominant pair\" 的 forward selection 验证。\n\n**残余问题**: 论文仍然对单个 feature 做精确排名声明 — \"P90_PPL ranks top-2 by Gini importance in all 9 cells; VAR_SURPRISAL ranks in 8/9\" — 但当 VIF>10 意味着特征间共线性极高时，个体特征的 importance 归属在统计上不可靠。论文在 feature GROUP 层面（perplexity tail statistics 作为一组）和 individual feature 层面的声明之间切换，没有明确说明 \"在 VIF>10 条件下，个体排名的稳定性本身受限于共线性\"。\n\n**判定**: W=0.90 concordance 和 4-5 effective dimensions 的承认已经显著改善了论述严谨性，但需要在 §4.2 加一句明确说明 individual-feature attribution 在高 VIF 条件下的 inherent instability。这是 minor 而非 critical。\n\n---\n\n### R1-W3: LoRA rank sensitivity analysis [NOT ADDRESSED]\n\n**现状**: 论文全篇仅使用 r=16。§3.2 (p3): \"LoRA finetuning (r=16, α=32)\"；cross-scale 使用 4-bit NF4 QLoRA；downstream PoC 使用 \"Pythia-410M with LoRA (r=16, α=32)\"。\n\n**无任何 rank sensitivity ablation (r ∈ {4, 16, 64})**。这在 Appendix A.1-A.17 中都未出现。\n\n**影响**: LoRA rank 直接控制 finetuning 的表达能力和过拟合程度——如果 r=4 时 depth signal 显著减弱或消失，则说明 signal 部分来自 LoRA 的 capacity artifact 而非 recursive generation 本身的 distributional shift。这影响核心 claim 的 robustness。\n\n**判定**: 仍为 Should-Fix。至少需要在一个 cell 上测试 r∈{4, 64} 并报告 accuracy 变化。\n\n---\n\n### R4-N2: Zero-shot LLM \"baseline\" framing [PARTIALLY ADDRESSED]\n\n**改进**: §6 Discussion 中将 LLM 结果定位为 \"confirming that depth discrimination requires computed statistical features rather than general language understanding\"，这更接近 ablation 解读。\n\n**残余问题**: §5.1 标题仍为 \"Baseline Comparison\"，正文称 \"zero-shot LLM baseline\" 并报告 \"accuracy gap exceeding 42 pp vs. RF\"。这是结构性不公平对比——LLM 没有 reference model perplexity features 的 access，不可能在相同信息条件下竞争。正确的 framing 应为 \"surface-text ablation: can general language understanding alone discriminate depth?\"\n\n**判定**: §6 的解读已改善，但 §5.1 的标题和竞争性语言仍在。从 \"Baseline Comparison\" 改为 \"Ablation: General Language Understanding\" 或在正文中加一句承认信息不对称即可解决。Minor → Should-Fix（因为审稿人容易误读为不公平 baseline）。\n\n---\n\n### R4-N3: Cross-scale claims qualification [PARTIALLY ADDRESSED]\n\n**改进**: §5.4 (p6) 加了 \"though further architectures are needed\"；Limitations (p7) 加了 \"The 7–8B experiments use instruction-tuned models only; whether base models at this scale exhibit the same signal profile remains open\"。Appendix A.13 使用 \"providing preliminary evidence\"。\n\n**残余问题**: Abstract 仍然以完整声明形式陈述 cross-scale 结果 — \"extending to two 7B-scale generators yields 70.2% accuracy with monotonic AUC decay (EDD=4)\" — 没有任何 \"preliminary\" 或 \"initial\" 限定词。读者首先接触的 abstract 给出的印象是 cross-scale generalization 已经建立，而实际上仅基于 N=2 instruction-tuned 7B 模型（confound-stacked: scale + instruction-tuning + QLoRA）。\n\n**判定**: 在 abstract 中加 \"preliminary cross-scale evidence\" 或类似限定词。Should-Fix。\n\n---\n\n### R5-N2: Reference model circular dependency [PARTIALLY ADDRESSED]\n\n**改进**: Limitations (p8) 现在明确讨论: \"An ablation with OLMo-1B as reference model shows 2-4pp (±2.3), suggesting moderate robustness; however, both reference models share similar scale (~1B) and autoregressive architecture, so validation with architecturally distinct references (e.g., encoder-only or larger-scale models) remains open.\" Table 15 (A.12) 提供了数据。\n\n**残余问题**: 仅测试了 2 个同族 (~1B autoregressive) reference model。没有测试 architecturally distinct reference (如 encoder-only 或 3B+ model)。但 Limitations 的措辞已经充分承认了这一局限。\n\n**判定**: Given the scope constraint (实验成本), Limitations 的明确承认是合理的。从 \"open\" → \"acceptable with current Limitations discussion\"。RESOLVED (via Limitations acknowledgment)。\n\n---\n\n### R5-W1: Single LoRA instance per depth — 5-Fold CV non-independence [NOT ADDRESSED]\n\n**现状**: 论文仅在 §3.2 说 \"no per-passage lineage across depths, ensuring cross-validation splits do not introduce leakage\"，A.9 的 LOGO 分析证明 seed-article 不构成 confound。\n\n**但核心问题不同**: 每个 depth 只有一个 LoRA-finetuned generator instance。5-Fold CV 的所有 folds 的 depth-d 样本都来自同一个 generator，violating the assumption that test samples are drawn from the \"population of depth-d generators\"。论文测量的是 \"this specific Pythia-LoRA-r16 at depth d 的 discriminability\"，而非 \"depth-d generation process in general 的 discriminability\"。\n\n**没有在 Limitations 中讨论。** LOGO 评估证明 seed-article 无 confound，但未 address single-generator non-independence。这对 generalization claim 有影响——如果用不同 random seed 的 LoRA 或不同 LoRA rank 产生 depth-d 数据，signal 是否 persist？\n\n**判定**: Should-Fix。至少需要在 Limitations 中明确承认 \"all depth-d samples at a given cell originate from a single generator instance; repeating with different LoRA seeds/configurations could yield different signal profiles\"。\n\n---\n\n### R5-W2: Deployment requires pre-known decoding strategy [PARTIALLY ADDRESSED]\n\n**改进**: §6 Discussion (p7) 明确讨论: \"strategy-conditioned classifiers—preceded by automatic strategy identification exploiting distinguishable perplexity signatures—offer a practical path, particularly since single-platform deployment typically knows the decoding strategy a priori.\" Limitations (p7): \"a two-stage pipeline (strategy identification → strategy-conditioned classification) is needed for reliable cross-strategy deployment.\"\n\n**残余问题**: \"automatic strategy identification exploiting distinguishable perplexity signatures\" 没有任何实验验证。这是一个 unsupported feasibility claim。论文 propose 了一个 two-stage pipeline 作为解决方案，但 stage-1 的可行性未被证明。\n\n**判定**: Discussion 的承认是合理的（明确标记为 \"practical path\" 而非已验证）。加 \"this remains to be validated\" 即可完善。Minor issue。RESOLVED (with minor wording suggestion)。\n\n---\n\n### R5-W3: Wild data FPR undermines practical claims [PARTIALLY ADDRESSED + NEW ISSUE]\n\n**改进**: Limitations (p7-8) 明确讨论 FPR 问题: \"FPR ranges from 4.7% (OLMo) to 22.4% (GPT-2 XL)... Deployment on heterogeneous web corpora requires model- and domain-specific calibration.\" A.10 提供 detailed calibration data (Table 12)。\n\n**新发现 — 数据报告不一致 (critical)**:\n- Abstract 声明: \"false positive rates range from 4.7% to 22.4%\"\n- Limitations 声明: \"FPR ranges from 4.7% (OLMo) to 22.4% (GPT-2 XL)\"\n- **但 Table 12 显示**: Pythia-1.4B C4 d0 accuracy = 70.8% → **FPR = 29.2%**\n\n论文在 abstract 和 Limitations 中报告 FPR 范围为 4.7%-22.4%，**但实际三个 classifier 中最差的 FPR 是 Pythia 的 29.2%**，而非 GPT-2 XL 的 22.4%。这是选择性报告——排除了最差结果而没有给出排除理由。\n\n可能的解释：Pythia 是 self-reference model 所以被排除？但 (a) 论文没有说明这一排除，(b) 论文声称 \"self-model configuration does not confer a systematic advantage\"。如果 self-reference 在 wild data 上表现最差（29.2% vs 22.4%），这恰恰说明 self-reference 有 systematic disadvantage，与论文声称矛盾。\n\n**判定**: Must-Fix。Abstract 和 Limitations 的 FPR 范围必须包含所有三个 classifier，或明确说明排除 Pythia 的原因。\n\n---\n\n### R5-W5: EDD classifier-dependence [NOT ADDRESSED]\n\n**现状**: §3.4 (p4) 定义 EDD 时使用 \"dedicated binary Random Forest (500 trees, |√19| features/split, 5-fold stratified CV)\" 作为 pairwise discriminability 的操作化手段。§4.3 提到 \"EDD uses binary-pair classifiers to avoid decision boundary dilution\"。\n\n**但论文从未明确说明 EDD 是一个 classifier-dependent operational measure**。它被呈现为一种描述 recursive generation process 本身的 metric — 仿佛 EDD 是 data 的固有属性。然而：\n- 换用不同 classifier (如 SVM 或 neural) 可能得到不同 EDD\n- 换用不同 feature set 可能得到不同 EDD\n- EDD 反映的是 \"给定此 detection pipeline 的可分辨性\"，而非 \"generation process 的内在可分辨深度\"\n\n§5.1 (Table 3) 显示 RF/XGB/LGBM 在同一 feature set 上 spread <0.4pp，这间接支持 EDD 对 classifier choice 的 robustness，但没有被 explicitly connected 到 EDD 的 classifier-independence discussion。\n\n**判定**: Should-Fix。在 §3.4 Definition 1 后加一段说明 EDD 是 \"operational measure conditioned on the feature set and classifier family\" 并引用 Table 3 的 classifier convergence 作为 approximate classifier-independence 的 evidence。\n\n---\n\n## 新发现\n\n### N1 [critical]: FPR 范围选择性报告\n\n如 R5-W3 评估中详述：Abstract 和 Limitations 报告 \"4.7% to 22.4%\"，但 Table 12 显示 Pythia C4 FPR = 29.2%。这构成选择性数据报告，无论是否有合理解释，都必须在文本中透明化。\n\n### N2 [warning]: Abstract 中 EDD 表述混淆\n\nAbstract: \"EDD_T=1 for extended recursive finding, EDD_T=1 for extended recursive chains\" — 这段文字看起来像是排版错误或 placeholder text 残留。后文和 Table 6 表明实际结果应为 EDD=4。如果 abstract 中确实存在这段 garbled text，这是严重的排版问题。\n\n注：这可能是 PDF 渲染/OCR 误读，建议作者核实 abstract 最终段的 EDD 表述。\n\n### N3 [minor]: Table 12 内部一致性\n\nTable 12 中 OLMo 的 C4 false positive 分布: \"d1 (2.9%), d2 (0.9%), d1 (3.1%)\" — \"d1\" 出现两次，第二个应为 \"d3\"。\n\n---\n\n## Strengths（本版本）\n\n1. **Comprehensive Limitations section** (p7-8): 覆盖 7+ 个明确局限性，包括 reference model dependency、domain FPR、adversarial robustness 等，展现了作者的诚实态度\n2. **Domain bias analysis** (A.9): LOGO 评估 + negative control + 自纠正（发现 bug 并修正）展现了严谨实验方法论\n3. **Three-method importance concordance** (W=0.90): VIF 分析 + forward selection + 三种 importance measure 对 feature validity 提供了多角度验证\n4. **Cross-boundary generalization** (A.13): heterogeneous chain 84.75% 提供了 depth signal 跨模型边界持续存在的有力证据\n5. **Temperature robustness analysis** (A.6): 多温度实验揭示了 \"memorization as prerequisite\" 的有洞察力的机制分析\n\n---\n\n## Weaknesses\n\n### Must-Fix\n\n**MF1** [critical]: FPR 选择性报告\n- 位置: Abstract, §7 Limitations, vs. Table 12 (A.10)\n- 问题: Abstract/Limitations 声称 \"FPR ranges from 4.7% to 22.4%\" 但 Table 12 的 Pythia C4 FPR = 29.2% 被排除而无说明\n- 影响: 双重问题 — (1) 数据报告不完整; (2) 若排除原因是 Pythia=reference model，则与 §3.2 \"self-model configuration does not confer a systematic advantage\" 的声称矛盾\n- 建议: 报告完整范围 (4.7%-29.2%) 或明确说明排除逻辑\n\n### Should-Fix\n\n**SF1**: LoRA rank sensitivity ablation 缺失（R1-W3 遗留）\n- 位置: §3.2 / Appendix\n- 问题: r=16 是唯一测试值。若 r=4 时 signal 消失，则 depth signal 可能部分来自 LoRA capacity artifact\n- 建议: 在一个 cell 上测试 r∈{4, 64}，报告 accuracy 和 top-feature 稳定性\n\n**SF2**: Single-generator non-independence 未讨论（R5-W1 遗留）\n- 位置: Limitations section\n- 问题: 5-Fold CV 的所有样本来自同一 LoRA instance per depth——测量的是 generator-specific 而非 process-general 的 discriminability\n- 建议: 在 Limitations 加 1-2 句承认 single-instance limitation 和 potential variation across LoRA seeds\n\n**SF3**: EDD 未定义为 operational measure（R5-W5 遗留）\n- 位置: §3.4 Definition 1\n- 问题: EDD 被呈现为 data property 而非 pipeline-conditioned operational measure\n- 建议: 在定义后说明 \"EDD is an operational measure conditioned on the feature representation and classification family\" 并引用 Table 3 作为 approximate independence evidence\n\n**SF4**: Abstract 缺少 cross-scale \"preliminary\" 限定（R4-N3 遗留）\n- 位置: Abstract\n- 问题: N=2 instruction-tuned 7B models 的结果在 abstract 中无任何 tentative language，而 body 已有 qualifications\n- 建议: \"preliminary cross-scale evidence from two 7B architectures...\"\n\n**SF5**: §5.1 \"Baseline Comparison\" 标题仍为竞争性 framing（R4-N2 遗留）\n- 位置: §5.1 标题 + 正文\n- 问题: Zero-shot LLM 无 reference-model feature access，不应以 baseline 形式对比\n- 建议: 改标题为 \"Classifier and Ablation Analysis\" 或加一句说明信息不对称\n\n---\n\n## Minor Issues\n\n- R1-W1: 建议在 §4.2 加一句: \"Individual feature attributions should be interpreted cautiously given VIF>10; the stable signal unit is the feature group (perplexity tail statistics) rather than individual features\"\n- N2: 核实 abstract 末尾的 EDD 表述是否有排版错误\n- N3: Table 12 commentary 中 \"d1 (2.9%), d2 (0.9%), d1 (3.1%)\" 第二个 d1 应为 d3\n- §5.2 \"2.7× chance\" — 66.4/25 = 2.656，四舍五入为 2.7× 可以接受但建议用 \"~2.7×\"\n\n---\n\n## Questions for Authors\n\n1. Table 12 中 Pythia C4 FPR=29.2% 为何在 abstract/Limitations 的范围声明中被排除？是 self-reference confound 还是其他原因？\n2. 是否考虑过用不同 LoRA random seed 重复生成某个 depth 来验证 signal 的 generator-instance independence？\n3. EDD 在 Table 3 的三种 classifier 上 converge（<0.4pp），但是否测试过在完全不同的 feature set 下（如仅用 lexical features）EDD 会如何变化？\n\n---\n\n## Overall Assessment\n\n**Soundness**: 3.5/5 — 核心方法论合理且实验设计整体 solid，但存在一个 critical data reporting inconsistency (FPR 选择性报告) 和若干未 addressed 的 validity concerns (LoRA rank, single-generator, EDD classifier-dependence)。\n\n**Excitement**: 3.5/5 — 问题定义新颖且有实际意义（recursive depth estimation as ordinal task），Depth Degradation Atlas 的系统性分析有价值，但 practical deployment 仍受限于 strategy-dependence 和 high FPR。\n\n**Overall**: 3.0/5 — Borderline，倾向 Findings。\n\n**一句话总结**: 论文在 Limitations 讨论上有显著进步，但 FPR 选择性报告是一个新 critical issue，加上 LoRA rank sensitivity 和 single-generator non-independence 两个 open concerns 仍未回应，阻碍 main conference 推荐。如果能 (1) 修正 FPR 报告, (2) 补一个 LoRA rank ablation, (3) 在 Limitations 承认 single-generator 和 EDD operational nature，则可升至 3.5 (Findings recommendation)。\n\n---\n\n**变化追踪总结**:\n| Issue | 状态 | 影响 |\n|-------|------|------|\n| R1-W1 multicollinearity | PARTIALLY ADDRESSED | Minor remaining |\n| R1-W3 LoRA rank | NOT ADDRESSED | Should-Fix |\n| R4-N2 LLM framing | PARTIALLY ADDRESSED | Should-Fix |\n| R4-N3 cross-scale qualification | PARTIALLY ADDRESSED | Should-Fix |\n| R5-N2 reference dependency | RESOLVED (via Limitations) | — |\n| R5-W1 single-generator | NOT ADDRESSED | Should-Fix |\n| R5-W2 strategy detection | RESOLVED (minor wording) | — |\n| R5-W3 FPR + NEW discrepancy | PARTIALLY + REGRESSED | Must-Fix |\n| R5-W5 EDD classifier-dep | NOT ADDRESSED | Should-Fix |\n\n新问题: FPR 数据选择性报告 (critical), abstract EDD typo (minor), Table 12 typo (minor)",
  "reviewer_id": "1",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 6 Review — Reviewer 1（方法严谨性 + 实验有效性）\n\n**Paper**: \"How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\"\n**Venue**: EMNLP 2026 Main Conference (ACL ARR May cycle)\n**审查侧重**: 方法严谨性、统计证据充分性、实验设计合理性、confound 控制\n\n---\n\n## 遗留问题评估\n\n### R1-W1: Feature importance multicollinearity [PARTIALLY ADDRESSED]\n\n**改进**: §4.2 现在明确报告 VIF>10 对 14-16 个 features (p3: \"variance inflation analysis reveals VIF>10 for 14–16 features, placing the effective independent dimensionality at 4–5\")，三种 importance measure 的 Kendall's W=0.90 concordance (Appendix A.2)，以及 \"dominant pair\" 的 forward selection 验证。\n\n**残余问题**: 论文仍然对单个 feature 做精确排名声明 — \"P90_PPL ranks top-2 by Gini importance in all 9 cells; VAR_SURPRISAL ranks in 8/9\" — 但当 VIF>10 意味着特征间共线性极高时，个体特征的 importance 归属在统计上不可靠。论文在 feature GROUP 层面（perplexity tail statistics 作为一组）和 individual feature 层面的声明之间切换，没有明确说明 \"在 VIF>10 条件下，个体排名的稳定性本身受限于共线性\"。\n\n**判定**: W=0.90 concordance 和 4-5 effective dimensions 的承认已经显著改善了论述严谨性，但需要在 §4.2 加一句明确说明 individual-feature attribution 在高 VIF 条件下的 inherent instability。这是 minor 而非 critical。\n\n---\n\n### R1-W3: LoRA rank sensitivity analysis [NOT ADDRESSED]\n\n**现状**: 论文全篇仅使用 r=16。§3.2 (p3): \"LoRA finetuning (r=16, α=32)\"；cross-scale 使用 4-bit NF4 QLoRA；downstream PoC 使用 \"Pythia-410M with LoRA (r=16, α=32)\"。\n\n**无任何 rank sensitivity ablation (r ∈ {4, 16, 64})**。这在 Appendix A.1-A.17 中都未出现。\n\n**影响**: LoRA rank 直接控制 finetuning 的表达能力和过拟合程度——如果 r=4 时 depth signal 显著减弱或消失，则说明 signal 部分来自 LoRA 的 capacity artifact 而非 recursive generation 本身的 distributional shift。这影响核心 claim 的 robustness。\n\n**判定**: 仍为 Should-Fix。至少需要在一个 cell 上测试 r∈{4, 64} 并报告 accuracy 变化。\n\n---\n\n### R4-N2: Zero-shot LLM \"baseline\" framing [PARTIALLY ADDRESSED]\n\n**改进**: §6 Discussion 中将 LLM 结果定位为 \"confirming that depth discrimination requires computed statistical features rather than general language understanding\"，这更接近 ablation 解读。\n\n**残余问题**: §5.1 标题仍为 \"Baseline Comparison\"，正文称 \"zero-shot LLM baseline\" 并报告 \"accuracy gap exceeding 42 pp vs. RF\"。这是结构性不公平对比——LLM 没有 reference model perplexity features 的 access，不可能在相同信息条件下竞争。正确的 framing 应为 \"surface-text ablation: can general language understanding alone discriminate depth?\"\n\n**判定**: §6 的解读已改善，但 §5.1 的标题和竞争性语言仍在。从 \"Baseline Comparison\" 改为 \"Ablation: General Language Understanding\" 或在正文中加一句承认信息不对称即可解决。Minor → Should-Fix（因为审稿人容易误读为不公平 baseline）。\n\n---\n\n### R4-N3: Cross-scale claims qualification [PARTIALLY ADDRESSED]\n\n**改进**: §5.4 (p6) 加了 \"though further architectures are needed\"；Limitations (p7) 加了 \"The 7–8B experiments use instruction-tuned models only; whether base models at this scale exhibit the same signal profile remains open\"。Appendix A.13 使用 \"providing preliminary evidence\"。\n\n**残余问题**: Abstract 仍然以完整声明形式陈述 cross-scale 结果 — \"extending to two 7B-scale generators yields 70.2% accuracy with monotonic AUC decay (EDD=4)\" — 没有任何 \"preliminary\" 或 \"initial\" 限定词。读者首先接触的 abstract 给出的印象是 cross-scale generalization 已经建立，而实际上仅基于 N=2 instruction-tuned 7B 模型（confound-stacked: scale + instruction-tuning + QLoRA）。\n\n**判定**: 在 abstract 中加 \"preliminary cross-scale evidence\" 或类似限定词。Should-Fix。\n\n---\n\n### R5-N2: Reference model circular dependency [PARTIALLY ADDRESSED]\n\n**改进**: Limitations (p8) 现在明确讨论: \"An ablation with OLMo-1B as reference model shows 2-4pp (±2.3), suggesting moderate robustness; however, both reference models share similar scale (~1B) and autoregressive architecture, so validation with architecturally distinct references (e.g., encoder-only or larger-scale models) remains open.\" Table 15 (A.12) 提供了数据。\n\n**残余问题**: 仅测试了 2 个同族 (~1B autoregressive) reference model。没有测试 architecturally distinct reference (如 encoder-only 或 3B+ model)。但 Limitations 的措辞已经充分承认了这一局限。\n\n**判定**: Given the scope constraint (实验成本), Limitations 的明确承认是合理的。从 \"open\" → \"acceptable with current Limitations discussion\"。RESOLVED (via Limitations acknowledgment)。\n\n---\n\n### R5-W1: Single LoRA instance per depth — 5-Fold CV non-independence [NOT ADDRESSED]\n\n**现状**: 论文仅在 §3.2 说 \"no per-passage lineage across depths, ensuring cross-validation splits do not introduce leakage\"，A.9 的 LOGO 分析证明 seed-article 不构成 confound。\n\n**但核心问题不同**: 每个 depth 只有一个 LoRA-finetuned generator instance。5-Fold CV 的所有 folds 的 depth-d 样本都来自同一个 generator，violating the assumption that test samples are drawn from the \"population of depth-d generators\"。论文测量的是 \"this specific Pythia-LoRA-r16 at depth d 的 discriminability\"，而非 \"depth-d generation process in general 的 discriminability\"。\n\n**没有在 Limitations 中讨论。** LOGO 评估证明 seed-article 无 confound，但未 address single-generator non-independence。这对 generalization claim 有影响——如果用不同 random seed 的 LoRA 或不同 LoRA rank 产生 depth-d 数据，signal 是否 persist？\n\n**判定**: Should-Fix。至少需要在 Limitations 中明确承认 \"all depth-d samples at a given cell originate from a single generator instance; repeating with different LoRA seeds/configurations could yield different signal profiles\"。\n\n---\n\n### R5-W2: Deployment requires pre-known decoding strategy [PARTIALLY ADDRESSED]\n\n**改进**: §6 Discussion (p7) 明确讨论: \"strategy-conditioned classifiers—preceded by automatic strategy identification exploiting distinguishable perplexity signatures—offer a practical path, particularly since single-platform deployment typically knows the decoding strategy a priori.\" Limitations (p7): \"a two-stage pipeline (strategy identification → strategy-conditioned classification) is needed for reliable cross-strategy deployment.\"\n\n**残余问题**: \"automatic strategy identification exploiting distinguishable perplexity signatures\" 没有任何实验验证。这是一个 unsupported feasibility claim。论文 propose 了一个 two-stage pipeline 作为解决方案，但 stage-1 的可行性未被证明。\n\n**判定**: Discussion 的承认是合理的（明确标记为 \"practical path\" 而非已验证）。加 \"this remains to be validated\" 即可完善。Minor issue。RESOLVED (with minor wording suggestion)。\n\n---\n\n### R5-W3: Wild data FPR undermines practical claims [PARTIALLY ADDRESSED + NEW ISSUE]\n\n**改进**: Limitations (p7-8) 明确讨论 FPR 问题: \"FPR ranges from 4.7% (OLMo) to 22.4% (GPT-2 XL)... Deployment on heterogeneous web corpora requires model- and domain-specific calibration.\" A.10 提供 detailed calibration data (Table 12)。\n\n**新发现 — 数据报告不一致 (critical)**:\n- Abstract 声明: \"false positive rates range from 4.7% to 22.4%\"\n- Limitations 声明: \"FPR ranges from 4.7% (OLMo) to 22.4% (GPT-2 XL)\"\n- **但 Table 12 显示**: Pythia-1.4B C4 d0 accuracy = 70.8% → **FPR = 29.2%**\n\n论文在 abstract 和 Limitations 中报告 FPR 范围为 4.7%-22.4%，**但实际三个 classifier 中最差的 FPR 是 Pythia 的 29.2%**，而非 GPT-2 XL 的 22.4%。这是选择性报告——排除了最差结果而没有给出排除理由。\n\n可能的解释：Pythia 是 self-reference model 所以被排除？但 (a) 论文没有说明这一排除，(b) 论文声称 \"self-model configuration does not confer a systematic advantage\"。如果 self-reference 在 wild data 上表现最差（29.2% vs 22.4%），这恰恰说明 self-reference 有 systematic disadvantage，与论文声称矛盾。\n\n**判定**: Must-Fix。Abstract 和 Limitations 的 FPR 范围必须包含所有三个 classifier，或明确说明排除 Pythia 的原因。\n\n---\n\n### R5-W5: EDD classifier-dependence [NOT ADDRESSED]\n\n**现状**: §3.4 (p4) 定义 EDD 时使用 \"dedicated binary Random Forest (500 trees, |√19| features/split, 5-fold stratified CV)\" 作为 pairwise discriminability 的操作化手段。§4.3 提到 \"EDD uses binary-pair classifiers to avoid decision boundary dilution\"。\n\n**但论文从未明确说明 EDD 是一个 classifier-dependent operational measure**。它被呈现为一种描述 recursive generation process 本身的 metric — 仿佛 EDD 是 data 的固有属性。然而：\n- 换用不同 classifier (如 SVM 或 neural) 可能得到不同 EDD\n- 换用不同 feature set 可能得到不同 EDD\n- EDD 反映的是 \"给定此 detection pipeline 的可分辨性\"，而非 \"generation process 的内在可分辨深度\"\n\n§5.1 (Table 3) 显示 RF/XGB/LGBM 在同一 feature set 上 spread <0.4pp，这间接支持 EDD 对 classifier choice 的 robustness，但没有被 explicitly connected 到 EDD 的 classifier-independence discussion。\n\n**判定**: Should-Fix。在 §3.4 Definition 1 后加一段说明 EDD 是 \"operational measure conditioned on the feature set and classifier family\" 并引用 Table 3 的 classifier convergence 作为 approximate classifier-independence 的 evidence。\n\n---\n\n## 新发现\n\n### N1 [critical]: FPR 范围选择性报告\n\n如 R5-W3 评估中详述：Abstract 和 Limitations 报告 \"4.7% to 22.4%\"，但 Table 12 显示 Pythia C4 FPR = 29.2%。这构成选择性数据报告，无论是否有合理解释，都必须在文本中透明化。\n\n### N2 [warning]: Abstract 中 EDD 表述混淆\n\nAbstract: \"EDD_T=1 for extended recursive finding, EDD_T=1 for extended recursive chains\" — 这段文字看起来像是排版错误或 placeholder text 残留。后文和 Table 6 表明实际结果应为 EDD=4。如果 abstract 中确实存在这段 garbled text，这是严重的排版问题。\n\n注：这可能是 PDF 渲染/OCR 误读，建议作者核实 abstract 最终段的 EDD 表述。\n\n### N3 [minor]: Table 12 内部一致性\n\nTable 12 中 OLMo 的 C4 false positive 分布: \"d1 (2.9%), d2 (0.9%), d1 (3.1%)\" — \"d1\" 出现两次，第二个应为 \"d3\"。\n\n---\n\n## Strengths（本版本）\n\n1. **Comprehensive Limitations section** (p7-8): 覆盖 7+ 个明确局限性，包括 reference model dependency、domain FPR、adversarial robustness 等，展现了作者的诚实态度\n2. **Domain bias analysis** (A.9): LOGO 评估 + negative control + 自纠正（发现 bug 并修正）展现了严谨实验方法论\n3. **Three-method importance concordance** (W=0.90): VIF 分析 + forward selection + 三种 importance measure 对 feature validity 提供了多角度验证\n4. **Cross-boundary generalization** (A.13): heterogeneous chain 84.75% 提供了 depth signal 跨模型边界持续存在的有力证据\n5. **Temperature robustness analysis** (A.6): 多温度实验揭示了 \"memorization as prerequisite\" 的有洞察力的机制分析\n\n---\n\n## Weaknesses\n\n### Must-Fix\n\n**MF1** [critical]: FPR 选择性报告\n- 位置: Abstract, §7 Limitations, vs. Table 12 (A.10)\n- 问题: Abstract/Limitations 声称 \"FPR ranges from 4.7% to 22.4%\" 但 Table 12 的 Pythia C4 FPR = 29.2% 被排除而无说明\n- 影响: 双重问题 — (1) 数据报告不完整; (2) 若排除原因是 Pythia=reference model，则与 §3.2 \"self-model configuration does not confer a systematic advantage\" 的声称矛盾\n- 建议: 报告完整范围 (4.7%-29.2%) 或明确说明排除逻辑\n\n### Should-Fix\n\n**SF1**: LoRA rank sensitivity ablation 缺失（R1-W3 遗留）\n- 位置: §3.2 / Appendix\n- 问题: r=16 是唯一测试值。若 r=4 时 signal 消失，则 depth signal 可能部分来自 LoRA capacity artifact\n- 建议: 在一个 cell 上测试 r∈{4, 64}，报告 accuracy 和 top-feature 稳定性\n\n**SF2**: Single-generator non-independence 未讨论（R5-W1 遗留）\n- 位置: Limitations section\n- 问题: 5-Fold CV 的所有样本来自同一 LoRA instance per depth——测量的是 generator-specific 而非 process-general 的 discriminability\n- 建议: 在 Limitations 加 1-2 句承认 single-instance limitation 和 potential variation across LoRA seeds\n\n**SF3**: EDD 未定义为 operational measure（R5-W5 遗留）\n- 位置: §3.4 Definition 1\n- 问题: EDD 被呈现为 data property 而非 pipeline-conditioned operational measure\n- 建议: 在定义后说明 \"EDD is an operational measure conditioned on the feature representation and classification family\" 并引用 Table 3 作为 approximate independence evidence\n\n**SF4**: Abstract 缺少 cross-scale \"preliminary\" 限定（R4-N3 遗留）\n- 位置: Abstract\n- 问题: N=2 instruction-tuned 7B models 的结果在 abstract 中无任何 tentative language，而 body 已有 qualifications\n- 建议: \"preliminary cross-scale evidence from two 7B architectures...\"\n\n**SF5**: §5.1 \"Baseline Comparison\" 标题仍为竞争性 framing（R4-N2 遗留）\n- 位置: §5.1 标题 + 正文\n- 问题: Zero-shot LLM 无 reference-model feature access，不应以 baseline 形式对比\n- 建议: 改标题为 \"Classifier and Ablation Analysis\" 或加一句说明信息不对称\n\n---\n\n## Minor Issues\n\n- R1-W1: 建议在 §4.2 加一句: \"Individual feature attributions should be interpreted cautiously given VIF>10; the stable signal unit is the feature group (perplexity tail statistics) rather than individual features\"\n- N2: 核实 abstract 末尾的 EDD 表述是否有排版错误\n- N3: Table 12 commentary 中 \"d1 (2.9%), d2 (0.9%), d1 (3.1%)\" 第二个 d1 应为 d3\n- §5.2 \"2.7× chance\" — 66.4/25 = 2.656，四舍五入为 2.7× 可以接受但建议用 \"~2.7×\"\n\n---\n\n## Questions for Authors\n\n1. Table 12 中 Pythia C4 FPR=29.2% 为何在 abstract/Limitations 的范围声明中被排除？是 self-reference confound 还是其他原因？\n2. 是否考虑过用不同 LoRA random seed 重复生成某个 depth 来验证 signal 的 generator-instance independence？\n3. EDD 在 Table 3 的三种 classifier 上 converge（<0.4pp），但是否测试过在完全不同的 feature set 下（如仅用 lexical features）EDD 会如何变化？\n\n---\n\n## Overall Assessment\n\n**Soundness**: 3.5/5 — 核心方法论合理且实验设计整体 solid，但存在一个 critical data reporting inconsistency (FPR 选择性报告) 和若干未 addressed 的 validity concerns (LoRA rank, single-generator, EDD classifier-dependence)。\n\n**Excitement**: 3.5/5 — 问题定义新颖且有实际意义（recursive depth estimation as ordinal task），Depth Degradation Atlas 的系统性分析有价值，但 practical deployment 仍受限于 strategy-dependence 和 high FPR。\n\n**Overall**: 3.0/5 — Borderline，倾向 Findings。\n\n**一句话总结**: 论文在 Limitations 讨论上有显著进步，但 FPR 选择性报告是一个新 critical issue，加上 LoRA rank sensitivity 和 single-generator non-independence 两个 open concerns 仍未回应，阻碍 main conference 推荐。如果能 (1) 修正 FPR 报告, (2) 补一个 LoRA rank ablation, (3) 在 Limitations 承认 single-generator 和 EDD operational nature，则可升至 3.5 (Findings recommendation)。\n\n---\n\n**变化追踪总结**:\n| Issue | 状态 | 影响 |\n|-------|------|------|\n| R1-W1 multicollinearity | PARTIALLY ADDRESSED | Minor remaining |\n| R1-W3 LoRA rank | NOT ADDRESSED | Should-Fix |\n| R4-N2 LLM framing | PARTIALLY ADDRESSED | Should-Fix |\n| R4-N3 cross-scale qualification | PARTIALLY ADDRESSED | Should-Fix |\n| R5-N2 reference dependency | RESOLVED (via Limitations) | — |\n| R5-W1 single-generator | NOT ADDRESSED | Should-Fix |\n| R5-W2 strategy detection | RESOLVED (minor wording) | — |\n| R5-W3 FPR + NEW discrepancy | PARTIALLY + REGRESSED | Must-Fix |\n| R5-W5 EDD classifier-dep | NOT ADDRESSED | Should-Fix |\n\n新问题: FPR 数据选择性报告 (critical), abstract EDD typo (minor), Table 12 typo (minor)",
    "reviewer_id": "1",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 293 · 2026-05-16T19:40:16.918950+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3817
}
```

</details>

---


### Assistant

_source line 294 · 2026-05-16T19:40:24.307716+00:00_

Round 6 审稿已完成并提交给 Review Director。

**核心判定**: Overall 3.0/5 (Borderline, 倾向 Findings)。

**关键发现**:
- 1 个新 critical issue：FPR 选择性报告（Abstract/Limitations 声称 4.7%-22.4%，但 Table 12 显示 Pythia 为 29.2%）
- 2 个遗留 open 问题仍未回应：LoRA rank sensitivity、single-generator non-independence
- 2 个问题通过 Limitations 讨论已 resolved：reference model dependency、strategy detection prerequisite
- 4 个问题 partially addressed 但仍有 minor 残余

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1"
}
```

</details>

---


## Round 10

## Round 10

2 recorded events


### User

_source line 295 · 2026-05-16T19:41:01.570272+00:00_

[Round 6 审稿请求]:
## 交叉分享 — Reviewer 2 的完整审稿意见

请逐条回应以下 Reviewer 2 的审稿意见。对每个观点用 **[AGREE]** 或 **[REBUT]** 标记，并提供 1-2 句理由（引用具体 Section/Table/Figure 作为证据）。

---

以下是 Reviewer 2 的完整审稿原文：

### 遗留问题评估

**1. R3-N4 'Universal' overclaim [PARTIALLY ADDRESSED]**
Introduction (line 14) 现在写 "universal and scale-variant across the three model families and three decoding strategies studied"——"universal" 仍在，但紧跟范围限定语。但 generalization.tex line 110 仍有未限定的 "signal universality"。建议替换为 "signal consistency across all tested configurations"。

**2. R1-W2 d0 inflation [RESOLVED]**
Abstract 明确标注 d1-d3 balanced accuracy: 55.4%。充分解决。

**3. R4-W1 Curation PoC [PARTIALLY ADDRESSED]**
已从 contribution list 删除。但 Discussion.tex 正文仍以应用方向口吻提及 "depth-graduated data curation" 而未标注 inconclusive。

**4. R4-W3 方法论新颖性 [PARTIALLY ADDRESSED]**
§4.2 有 post-hoc 对齐式叙述连接 model-collapse dynamics，但没有形式化理论分析。对 EMNLP 不一定 must-fix，但限制 excitement。

**5. R5-N1 Novelty vs Dohmatob (2024) [PARTIALLY ADDRESSED]**
Related Work 建立了任务层面区分 ("inverse problem")，但 perplexity tail 使用的具体区分不够 explicit。需要 2-3 句明确 bridge: "tail erosion is a theoretical prediction; our contribution is demonstrating it as sufficient and dominant practical signal for ordinal depth classification"。

**6. R5-W4 Related Work 遗漏 [NOT ADDRESSED]**
三篇均未出现：Schaeffer et al. (2025) "Model Collapse Does Not Mean What You Think"、Frank & Hall (2001)、Rennie & Srebro (2005)。

**7. R3-M1 引用元数据 [PARTIALLY ADDRESSED]**
alemohammad2024_mad 作者仍错误："Romero, Oscar" → "Leong, Oscar"，"Ramanarayanan, Sriram" → "Rangamani, Akshay"。

**8. R4-W5 Abstract 信息密度 [NOT ADDRESSED]**
Abstract 含 20+ 数字，含不应在 abstract 中出现的 "§4.4" 引用。

### Weaknesses

**Must-Fix:**
- MF1: alemohammad2024_mad 作者错误（引用诚信）
- MF2: Related Work 遗漏 Schaeffer et al. (2025)

**Should-Fix:**
- SF1: Abstract 数字过载
- SF2: "universal/universality" 仍残留
- SF3: Discussion curation 未标注 inconclusive
- SF4: Novelty vs Dohmatob 区分不够 explicit
- SF5: Ordinal Classification 缺经典工作

**Minor:**
- Contribution bullet 3 过载
- Abstract "§4.4" 不规范
- "universal and scale-variant" 用词矛盾

### New Findings:
- N1: Contribution bullet 3 在一个列表项中堆叠 7 axes + 6 数字
- N2: "consistent across all three families" 的 statistical support 不均 (p=0.001/0.091/0.505)
- N3: Discussion 缺失对 Schaeffer 反论点的讨论

### Overall: 3/5 (Findings-level)

---

请逐条 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 296 · 2026-05-16T19:42:02.801450+00:00_

## 交叉回应 — Reviewer 1 对 Reviewer 2 意见的逐条回应

---

### 遗留问题评估

**[AGREE] R2-Issue-1 (R3-N4 'Universal' overclaim)**
同意。即使 Introduction 加了范围限定语，"universal" 一词在学术写作中暗示超出测试范围的普适性。3 model families × 3 strategies = 9 cells 是系统性实验，但远不足以支撑 "universal"。"consistent across all tested configurations" 更准确。补充：我在 Round 6 中也注意到 cross-scale 仅 N=2 models 的 qualification 问题（R4-N3），"universal" 与此构成叠加 overclaim。

---

**[AGREE] R2-Issue-2 (R1-W2 d0 inflation)**
同意 RESOLVED。Abstract 明确报告 "d1–d3 balanced accuracy 55.4%"，把 d0 膨胀效应透明化了。

---

**[AGREE] R2-Issue-3 (R4-W1 Curation PoC)**
同意。§6 Discussion 和 A.14 仍以 "depth-graduated data curation" 作为应用方向讨论，且 A.14 的 downstream PoC (Pythia-410M perplexity 差异 0.3pp, p=0.41) 实际上 inconclusive — 结果不显著但论文未明确标注。Discussion 应加 "preliminary and statistically inconclusive" qualifier。我在 Round 6 中未专门 flag 此问题，但同意 Reviewer 2 的判断。

---

**[REBUT] R2-Issue-4 (R4-W3 方法论新颖性)**
部分不同意其严重性评估。论文的核心新颖性在于 problem formulation (recursive depth as ordinal classification) + empirical contribution (systematic atlas + EDD metric)，而非 formal theory。§4.4 的 "signal attenuation" 分析虽为 post-hoc，但提供了 mechanistic insight (memorization prerequisite, A.6 Table 9 τ=1.1 collapse)。对 EMNLP empirical track 而言，formal theory 不是必要条件——但我同意这限制 excitement score，不影响 soundness。

---

**[AGREE] R2-Issue-5 (R5-N1 Novelty vs Dohmatob 2024)**
同意需要更 explicit 的 bridge statement。Dohmatob et al. (2024a,b) 从理论预测 tail erosion/scaling law change；本文将 tail statistics 作为 classification feature——但 "from theoretical prediction to practical sufficient signal" 的逻辑链在 Related Work 中确实不够清晰。2-3 句的 bridge 是合理且低成本的要求。

---

**[AGREE] R2-Issue-6 (R5-W4 Related Work 遗漏)**
部分同意。
- **Schaeffer et al. (2025) "Model Collapse Does Not Mean What You Think"**: 强烈同意必须引用。此文 challenge "model collapse" narrative 本身——如果本文不讨论此反论点，reviewer 会质疑作者是否了解 field 的争论。这是 Must-Fix。
- **Frank & Hall (2001), Rennie & Srebro (2005)**: 作为 ordinal classification 经典方法论文，应在 §3.1 提及以 contextualize threshold-based ordinal 方法选择。但影响程度为 Should-Fix 而非 Must-Fix，因为论文使用的 RF + ordinal wrapper 是标准做法，不 claim 方法论创新。

---

**[AGREE] R2-Issue-7 (R3-M1 引用元数据)**
同意这是 Must-Fix。引用作者名错误属于引用诚信问题，无论是否影响技术内容都必须修正。我未在 Round 6 中独立检查 bib 元数据，接受 Reviewer 2 的发现。

---

**[AGREE] R2-Issue-8 (R4-W5 Abstract 信息密度)**
同意。Abstract 含 20+ 数字 + "§4.4" section 引用确实不符合 ACL 规范。学术 abstract 应传达核心 claim 和主要结论，而非堆砌精确数字。特别是 "§4.4" 这类内部引用在 abstract 中属于格式错误。Should-Fix。

---

### Weaknesses 回应

**[AGREE] MF1: alemohammad2024_mad 作者错误**
引用诚信 issue，必须修正。

**[AGREE] MF2: Related Work 遗漏 Schaeffer et al. (2025)**
同意 Must-Fix 级别。该文直接挑战 "model collapse" 的定义和严重性——本文以 model collapse detection 为应用动机，不讨论 counterargument 是严重遗漏。

**[AGREE] SF1: Abstract 数字过载**
同意。建议保留 3-5 个关键数字（overall accuracy、d1-d3 balanced acc、EDD、cross-model accuracy），其余移入正文。

**[AGREE] SF2: "universal/universality" 残留**
与我的 cross-scale qualification 关注一致。

**[AGREE] SF3: Discussion curation 未标注 inconclusive**
A.14 的 p=0.41 明确 insignificant。

**[AGREE] SF4: Novelty vs Dohmatob 区分**
如上述，2-3 句 bridge 是合理要求。

**[AGREE] SF5: Ordinal Classification 缺经典工作**
同意 Should-Fix。Frank & Hall (2001) 是 ordinal classification 的 seminal work，Rennie & Srebro (2005) 提出 threshold loss——至少需要一句 contextualization 说明为何选择 threshold-based RF wrapper。

---

### New Findings 回应

**[AGREE] N1: Contribution bullet 3 过载**
7 axes + 6 数字在一个 bullet 中确实损害可读性。建议拆分为 2 个 sub-bullets。

**[REBUT] N2: "consistent across all three families" 统计 support 不均 (p=0.001/0.091/0.505)**
部分不同意。需看具体上下文——如果指的是某个 specific metric 的 per-family significance test，p 值不均并不否定 overall pattern consistency。Consistency claim 可能基于 direction (所有 family 都呈 monotonic decrease) 而非 per-family magnitude significance。但如果论文使用 "statistically consistent" 而非 "directionally consistent"，则 Reviewer 2 的批评成立。**需要确认具体位置和 exact claim wording** 才能完全判断。倾向 partial agree — 建议作者将此 claim 从 "consistent" 改为 "directionally consistent across families, with varying effect sizes"。

**[AGREE] N3: Discussion 缺失对 Schaeffer 反论点的讨论**
与 MF2 一致。如果引用 Schaeffer et al.，还需在 Discussion 加 1-2 句讨论：即使 "model collapse" 的严重性存在争议，recursive depth estimation 本身仍有独立价值（作为 provenance signal）。

---

### Overall Assessment 回应

**[AGREE]** 3/5 Findings-level 与我的评估一致（我给 3.0/5）。Reviewer 2 侧重 presentation/framing/citation 问题，我侧重 methodology/statistics 问题——两者互补，共同指向 "solid empirical work with presentation and methodological gaps that place it at Findings level rather than Main"。

---

**综合判断**: Reviewer 2 的 8 个遗留问题评估和 3 个新发现中，我在 7/8 + 2/3 上 AGREE。唯一 REBUT 是 R4-W3 的严重性（formal theory 对 EMNLP empirical track 非必要）和 N2 的 partial rebut（需确认 exact claim context）。两份审稿意见的 convergence 强化了论文处于 Findings 而非 Main conference 水平的判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1"
}
```

</details>

---


## Round 11

## Round 11

52 recorded events


### User

_source line 297 · 2026-05-16T20:06:14.042276+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1

**你的审查侧重：方法严谨性 + 实验设计 + 统计分析**

### Venue 信息
- **目标会议**: EMNLP 2026 Main Conference (via ARR May 2026 cycle)
- **Deadline**: 2026-05-25
- **页数限制**: Long paper, 8 pages (不含 Limitations/Ethics/References)
- **模板**: ACL format (`\usepackage[review]{acl}`)
- **匿名规则**: Double-blind，禁止自引暴露身份
- **Limitations section**: 必须存在，位于 Conclusion 后，不计入页数

### 论文路径
`projects/recursive_gen_depth_est/docs/paper/main.tex`
（含 `abstract.tex`, `introduction.tex`, `related_work.tex`, `method.tex`, `atlas.tex`, `generalization.tex`, `discussion.tex`, `conclusion.tex`, `section_appendix.tex`）

### 你的审查重点

1. **方法定义严谨性**：
   - EDD 定义（Eq.1）是否严格、无歧义
   - Problem formulation 是否完整（ordinal classification）
   - 统计检验是否恰当（bootstrap, significance levels）

2. **实验设计**：
   - 基准实验是否公平（classifier comparison, surface-text ablation）
   - 交叉验证方案是否有泄漏风险
   - Cross-model / cross-strategy / cross-scale 实验的 confounds 是否充分讨论
   - 样本量是否充分（180K primary, 500/depth cross-scale）

3. **统计分析**：
   - 报告的 CI/std 是否充分
   - EDD₀.₇₅=4 的 p-value 分层（Pythia p=0.001, OLMo p=0.091, GPT-2 XL p=0.505）是否被如实反映
   - d0 inflation 对 headline metrics 的影响是否被充分 qualify

4. **可复现性**：
   - LoRA 参数是否有选择依据
   - Reference model 选择是否有 circularity 问题
   - Feature extraction pipeline 是否可复现

请按 Strengths / Weaknesses (Must-Fix / Should-Fix / Minor) / Questions / Missing References 结构输出审稿意见。对每个 Weakness 标注严重程度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 298 · 2026-05-16T20:06:40.599955+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,WebSearch,mcp__agent-ml-research__verify_references,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,WebSearch,mcp__agent-ml-research__verify_references,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 299 · 2026-05-16T20:06:40.600303+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 300 · 2026-05-16T20:06:41.605099+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 301 · 2026-05-16T20:06:41.605425+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 302 · 2026-05-16T20:06:46.857172+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 303 · 2026-05-16T20:06:47.510222+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
  "pages": "1-5",
  "dpi": "180"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.pdf",
    "pages": "1-5",
    "dpi": "180"
  }
}
```

</details>

---


### Tool result

_source line 304 · 2026-05-16T20:06:55.243174+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

I found comprehensive information about ACL ARR 2026 reviewer guidelines and the review form criteria. Here's what I found:

## Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, 
…[truncated 1804 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8386
}
```

</details>

---


### Tool result

_source line 305 · 2026-05-16T20:06:57.290553+00:00_

Error: result (4,013,515 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/973a2203-6cf6-480c-b9ee-466b00682204/tool-results/mcp-agent-ml-research-pdf_to_images-1778962017093.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/973a2203-6cf6-480c-b9ee-466b00682204/tool-results/mcp-agent-ml-research-pdf_to_images-1778962017093.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-review-reviewer-1-37084335/973a2203-6cf6-480c-b9ee-466b00682204/tool-results/mcp-agent-ml-research-pdf_to_images-1778962017093.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 9780
}
```

</details>

---


### Tool call

_source line 306 · 2026-05-16T20:07:05.176202+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*_pdf_images/**/*.png",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*_pdf_images/**/*.png",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 307 · 2026-05-16T20:07:05.628517+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p9.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p10.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p11.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p12.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p13.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p14.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p15.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p16.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p6.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p7.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p8.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p1.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p2.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p3.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p4.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p5.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 308 · 2026-05-16T20:07:05.729371+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
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

_source line 309 · 2026-05-16T20:07:05.779979+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 310 · 2026-05-16T20:07:13.576427+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5 or whatever), and the description of each score level. I need the exact criteria for: soundness, excitement, overall assessment, confidence, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5 or whatever), and the description of each score level. I need the exact criteria for: soundness, excitement, overall assessment, confidence, and any other scored dimensions."
  }
}
```

</details>

---


### Tool call

_source line 311 · 2026-05-16T20:07:13.978595+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 312 · 2026-05-16T20:07:14.332088+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 313 · 2026-05-16T20:07:16.241594+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2263
}
```

</details>

---


### Tool result

_source line 314 · 2026-05-16T20:07:16.342917+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2010
}
```

</details>

---


### Tool result

_source line 315 · 2026-05-16T20:07:20.308021+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Reviewer Confidence
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: Quite confident; unlikely but possible to have missed something affecting ratings
- **3**: Reasonably assured, though details may have been overlooked
- **2**: Can defend evaluation, but likely missed important details or novelty assessment
- **1**: "Not my area, or paper is very hard to understand"

## Soundness
Scale: 1-5 (with .5 increments)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: "Strong: This study provides sufficient support for all of its claims"
- **3**: "Acceptable: This study provides sufficient support for its main claims"
- **2**: "Poor: Some of the main claims are not sufficiently supported"
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement
Scale: 1-5 (with .5 increments)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation"
- **4**: "Exciting: I would mention this paper to others"
- **3**: "Interesting: I might mention some points of this paper to others"
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others"
- **1**: "Not Exciting: this paper does not resonate with me"

## Overall Assessment
Scale: 1-5 (with .5 increments)
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance
- **3**: Findings acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit

## Additional Scored Dimensions

**Reproducibility** (1-5): Ease of reproducing results

**Datasets** (1-5): Value of released datasets to other researchers

**Software** (1-5): Value of released software to other researchers

**Author Identity Knowledge** (1-5): Reviewer's awareness of authorship

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6731
}
```

</details>

---


### Tool call

_source line 316 · 2026-05-16T20:07:27.186070+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 317 · 2026-05-16T20:07:27.788830+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 318 · 2026-05-16T20:07:28.694587+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 319 · 2026-05-16T20:07:28.947941+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1761
}
```

</details>

---


### Tool call

_source line 320 · 2026-05-16T20:07:28.948380+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 321 · 2026-05-16T20:07:30.611302+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2822
}
```

</details>

---


### Tool result

_source line 322 · 2026-05-16T20:07:31.567712+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2873
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-16T20:07:31.568802+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2620
}
```

</details>

---


### Tool call

_source line 324 · 2026-05-16T20:07:36.843060+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 325 · 2026-05-16T20:07:37.747151+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 326 · 2026-05-16T20:07:38.300061+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 327 · 2026-05-16T20:07:38.402141+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1559
}
```

</details>

---


### Tool call

_source line 328 · 2026-05-16T20:07:38.604452+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 329 · 2026-05-16T20:07:39.920945+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1620
}
```

</details>

---


### Tool result

_source line 330 · 2026-05-16T20:07:39.972334+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2225
}
```

</details>

---


### Tool result

_source line 331 · 2026-05-16T20:07:40.173843+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1569
}
```

</details>

---


### Tool call

_source line 332 · 2026-05-16T20:07:45.862943+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 333 · 2026-05-16T20:07:46.653505+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 790
}
```

</details>

---


### Tool call

_source line 334 · 2026-05-16T20:07:46.704189+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 335 · 2026-05-16T20:07:47.306710+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 336 · 2026-05-16T20:07:47.960232+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1256
}
```

</details>

---


### Tool result

_source line 337 · 2026-05-16T20:07:47.961420+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 654
}
```

</details>

---


### Tool call

_source line 338 · 2026-05-16T20:07:48.113061+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 339 · 2026-05-16T20:07:48.163773+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 340 · 2026-05-16T20:07:48.717444+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 341 · 2026-05-16T20:07:48.919226+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool result

_source line 342 · 2026-05-16T20:07:49.070979+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool result

_source line 343 · 2026-05-16T20:07:49.272579+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1108
}
```

</details>

---


### Tool call

_source line 344 · 2026-05-16T20:10:28.857053+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 345 · 2026-05-16T20:11:21.073602+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 49, \"total_citations\": 77, \"unique_cited_keys\": 49, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 40, \"online_not_found\": 5, \"online_mismatch\": 4}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"shumailov2024_nature\", \"type\": \"article\", \"title\": \"AI models collapse when trained on recursively generated data\", \"authors\": \"Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and ...\", \"year\": \"2024\", \"venue\": \"Nature\"}, {\"key\": \"dohmatob2024_tale_of_tails\", \"type\": \"inproceedings\", \"title\": \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, ...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICML\"}, {\"key\": \"dohmatob2025_strong_collapse\", \"type\": \"inproceedings\", \"title\": \"Strong Model Collapse\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\", \"year\": \"2025\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"dohmatob2024_demystified\", \"type\": \"inproceedings\", \"title\": \"Model Collapse Demystified: The Case of Regression\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia\", \"year\": \"2024\", \"venue\": \"Proceedings of NeurIPS\"}, {\"key\": \"alemohammad2024_mad\", \"type\": \"inproceedings\", \"title\": \"Self-Consuming Generative Models Go MAD\", \"authors\": \"Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahme...\", \"year\": \"2024\", \"venue\": \"Proceedings of ICLR\"}, {\"key\": \"gerstgrasser2024_accumulate\", \"type\": \"misc\", \"title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"authors\": \"Gerstgrasser, Matt
…[truncated 38138 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 52216
}
```

</details>

---


### Tool call

_source line 346 · 2026-05-16T20:14:07.432717+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 — Round 1 审稿意见\n\n**论文**: \"How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\"\n**审稿侧重**: 方法严谨性 + 实验设计 + 统计分析\n**对照标准**: ACL ARR Review Form (2025 版, soundness/excitement/overall 三维度制)\n\n---\n\n## 总体评分\n**Overall**: 3.0 / 5（Findings 水平）\n**一句话总结**: 问题定义新颖、atlas 构建系统，但核心指标 EDD₀.₇₅=4 的统计支撑在模型间差异悬殊且未被如实反映，d0 inflation 使 headline 数字产生误导，削弱了方法论声称的严谨性。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2.5/5 | 核心 EDD₀.₇₅=4 claim 的统计支撑不均匀（GPT-2 XL 在 d3-vs-d4 边界无显著性），d0 inflation 未充分 qualify，reference model circularity 未被有效排除 |\n| Excitement | 3.5/5 | 将递归生成深度估计形式化为 ordinal classification 是新颖的切入角度，Depth Degradation Atlas 有独立参考价值 |\n| Overall | 3.0/5 | 问题重要、方向有趣，但实验-声明之间的 gap 需要修补才能达到 conference 接收标准 |\n| Reproducibility | 3/5 | 特征提取管线可复现，但 LoRA 参数无选择依据，DCOL 迭代细节分散 |\n| Confidence | 4/5 | 仔细阅读全文含附录，熟悉 model collapse 和 AI-text detection 两个领域 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] EDD₀.₇₅=4 的 claim 在 abstract 中被过度概括\n\n- 具体位置：Abstract 第 7-8 行（\"finding EDD₀.₇₅=4 for extended recursive generation depth estimation\"）；§4.3 第 2 段\n- 问题：Abstract 将 EDD₀.₇₅=4 作为通用结论呈现，但 §4.3 明确写道\"At T=0.75, 7/9 atlas cells maintain EDD ≥ 3 on the primary benchmark\"——即 2/9 的 atlas cell 在 T=0.75 时连 EDD≥3 都不满足。更关键的是，d3-vs-d4 边界的 pairwise AUC 在三个模型族间的统计显著性差异悬殊：根据 Figure 1 中 bootstrap 95% CI，Pythia d3-vs-d4 AUC 的 CI 下界明显高于 0.75，但 GPT-2 XL 的 CI 跨越 0.75 阈值。论文未报告各 model-strategy cell 在 d3-vs-d4 边界的 bootstrap p-value，读者无法判断 EDD₀.₇₅=4 在每个 cell 中是否有统计显著支撑。\n- 为什么影响接收：EDD₀.₇₅=4 是全文的 headline finding。如果这一结论仅在部分配置中统计显著，而在其他配置中不显著（或边际显著），则 abstract 的表述构成 overclaiming，违反 ARR soundness 要求。\n- 建议修改方向：(1) 在 abstract 中改为条件性表述（如\"EDD₀.₇₅ reaches 4 for nucleus sampling across all three model families; under temperature and top-k, 7/9 cells achieve EDD ≥ 3\"）；(2) Table 17 (Appendix A.16) 或主文中增加每个 cell 在 d3-vs-d4 边界的 bootstrap p-value 和 CI；(3) 如果某些 cell 的 d3-vs-d4 AUC 在 0.75 附近无显著性，必须明确标注。\n\n**N2** [critical] 关键结果表（Table 2, 4, 5）缺乏不确定性度量\n\n- 具体位置：Table 2（4-class RF accuracy, 9 cells）；Table 4（cross-model transfer）；Table 5（cross-strategy transfer）\n- 问题：Table 2 报告 9 个 cell 的 4-class accuracy，无标准差、无置信区间、无 bootstrap CI。Figure 1 使用了 bootstrap 95% CI（shaded bands），说明作者有计算 CI 的能力和数据，但未将这一实践推广到核心数字。Table 4/5 同样缺乏 CI。对于 5-fold stratified CV，至少应报告 fold 间的 mean ± std。\n- 为什么影响接收：ACL ARR soundness 标准要求 claims 有充分统计支撑。没有 CI 的 accuracy 数字无法判断 cell 间差异是否显著、transfer 是否真正有效。\n- 建议修改方向：所有准确率表格增加 5-fold CV 的 mean ± std 或 bootstrap 95% CI。\n\n**N3** [critical] d0 inflation 对 headline metrics 的影响未在主文中充分 qualify\n\n- 具体位置：Table 2（主文 p4）vs Table 7（Appendix A.3 per-class recall）\n- 问题：Table 2 中 4-class accuracy 最高达 85.4%（GPT-2 XL, temp），但 Table 7 显示 d2 在每个 cell 中都是 recall 最低的类别（最低仅 46% 在 Pythia holdout 下）。d0 recall 则在所有 cell 中 >98%。这意味着 4-class accuracy 被 d0 的近完美分类大幅拉高。主文 §4.1 仅用一句话提到\"Depth-0 recall exceeds 98% in all 9 cells\"，但未报告 d2 recall 的困难程度，也未讨论 class imbalance 的影响。\n- 为什么影响接收：如果方法对 d2 的区分能力弱到只有 46% recall，那么\"depth estimation\"的实际效用大打折扣。reviewer 需要看到 macro-F1 或 balanced accuracy 来评估真实性能。\n- 建议修改方向：(1) 主文 Table 2 增加 macro-F1 或 balanced accuracy 列；(2) 在 §4.1 中明确讨论 d2 的困难性及原因（d2 是中间深度，特征可能与 d1/d3 重叠）；(3) Figure 2（confusion matrix）中标注 per-class recall 数字。\n\n**N4** [major] Reference model 选择存在 circularity 且 ablation 不充分\n\n- 具体位置：§3.3（feature extraction pipeline）；§8 Limitations（\"Reference model dependency\"）；Appendix A.12\n- 问题：所有 19 个统计特征均基于 Pythia-1.4B 作为 reference model 计算。当分类 Pythia 生成的文本时，reference model 即 generator（或同系列近亲），构成 self-model feature extraction（§3.2 也承认了这一点）。Appendix A.12 用 OLMo-1B 替换 Pythia-1.4B 做 reference，结果准确率下降 2-40pp，但 OLMo-1B 与 Pythia-1.4B 共享相似的 scale (~1B) 和 autoregressive 架构——这不是一个有力的 ablation。如果 reference model 的选择如此敏感，那么方法的通用性声称就需要更多支撑。\n- 为什么影响接收：如果 Pythia 作为 reference model 给 Pythia-generated text 带来了系统性优势，那么整个 atlas 的结论可能存在偏差。\n- 建议修改方向：(1) 至少用一个不同 scale 或架构的 reference model（如 GPT-2 XL 或 7-8B 模型）做完整 ablation；(2) 在主文中明确量化 self-model vs cross-model feature extraction 的性能差距；(3) 讨论理想的 reference model 选择标准。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] LoRA 训练配置缺乏选择依据\n\n- 具体位置：§3.2（generation pipeline）；Table 8（DCOL iterations, Appendix A.4）\n- 问题：§3.2 提到使用 LoRA 微调生成模型（每一代递归），但未说明 rank、alpha、target modules 的选择理由。Table 8 列出 6 个 DCOL 迭代中的不同配置（DeBERTa FT vs LoRA, 不同学习率），但这些是 DCOL 过程的记录，不是系统性的超参数 ablation。LoRA rank 直接影响模型在递归训练中的 capacity，进而影响 collapse 速度和特征分布——这是一个核心 confound。\n- 建议：增加 LoRA rank ablation（如 rank=4,8,16,32），或说明选择依据（如 follow 某篇先前工作的设定）。\n\n**W2** [warning] Cross-strategy transfer 弱（59.1%）但主文对其实际影响的讨论不够突出\n\n- 具体位置：§5.3（Table 5）；§6 Discussion\n- 问题：3-class cross-strategy accuracy 为 59.1%（chance=33%），意味着在不知道解码策略的实际场景中，方法的深度估计能力有限。§6 的 Discussion 段提到需要\"strategy-conditioned classifiers\"，但这一重大局限被放在一个长段落中而非作为独立的 limitation 讨论。\n- 建议：在 Limitations 中单独一段讨论策略依赖性，并量化在\"策略未知\"场景下方法的预期性能下界。\n\n**W3** [warning] Negative control 暴露的历史 confound 未充分透明\n\n- 具体位置：Appendix A.9 Sub-C（Negative control）\n- 问题：Sub-C 报告 seed-group prediction accuracy 在\"修复前\"为 20.8%，修复后降到 10.2%（接近 10-class chance）。这表明实验设计曾存在 depth-group confound——seed 分组与 depth 之间有泄漏。论文未解释这个 confound 的具体性质和修复方法。\n- 建议：明确描述原始 confound 的来源（是 seed 分配不均还是 data pipeline bug？）和修复措施，让 reviewer 评估修复是否充分。\n\n**W4** [warning] EDD 定义依赖 classifier capacity，非分布内禀属性\n\n- 具体位置：Definition 1（§3.4）\n- 问题：EDD 通过 binary RF classifier 的 pairwise AUC 定义。这意味着 EDD 不仅反映深度间的内禀可区分性，还反映所选 classifier 的能力上限。一个更强的 classifier（如 neural model）可能会得到更高的 EDD。论文在 §8 中提到\"this comparison is bounded by backbone scale\"但未系统讨论 classifier choice 对 EDD 的影响。\n- 建议：(1) 讨论 EDD 是 method-dependent 的 operational metric 而非 distribution-intrinsic 的性质；(2) 或在 §3.4 用至少两种不同 classifier 报告 EDD 来展示稳定性（RF 在 §3.4 已选，Appendix 可加 LightGBM 或 logistic regression 的 EDD 对比）。\n\n---\n\n## 小问题（不影响接收）\n\n- **引用年份不一致**：`he2021_deberta_v3` bib 条目标记 year=2023，OpenAlex 匹配结果为 2021；`alemohammad2024_mad` 第一作者与 OpenAlex 不一致（bib=Alemohammad vs API=Casco-Rodriguez）。建议核对。\n- **knowledge_collapse2025** 和 **falahati2026_curated** 在 OpenAlex 上未找到记录，可能是极新的 preprint。如果引用这些作为支撑论点，需确保这些论文确实存在且已公开。\n- Table 1 的 19 个特征在不同类别中的分配描述可以更清晰（Perplexity: 9, Surprisal: 3, Lexical: 4, Repetition: 3，但正文和表格的编号跳跃容易混淆）。\n- Figure 4（feature importance heatmap）色标的可读性较低，建议使用离散色标或增大字体。\n- Abstract 中\"with the top 5 achieving 97.6% of full-scale performance\"这一表述容易被误读为\"97.6% accuracy\"，建议改为\"retaining 97.6% of the 19-feature accuracy\"以消除歧义。\n\n---\n\n## Questions to Authors\n\n**Q1**: EDD₀.₇₅=4 是否在所有 9 个 atlas cell 中都有 bootstrap 显著性支撑？请报告每个 cell 在 d3-vs-d4 边界的 bootstrap p-value。\n\n**Q2**: 如果用 GPT-2 XL（而非 Pythia-1.4B）作为 reference model，Table 2 中各 cell 的 accuracy 变化如何？是否会改变 EDD 的结论？\n\n**Q3**: Appendix A.9 Sub-C 中提到 seed-group confound 的\"fix\"——具体修复了什么？修复前后的 per-depth accuracy 是否有变化？\n\n**Q4**: 有没有考虑用 distribution-free 的方法（如 MMD 或 permutation test）直接衡量深度间的分布距离，而非通过 classifier AUC 间接衡量？这可以提供一个不依赖 classifier capacity 的 EDD 变体。\n\n**Q5**: 主文报告的 4-class accuracy（Table 2）是否已用 balanced/stratified sampling 确保 class balance？如果 d0 样本多于 d3，accuracy 会被 d0 自然拉高。\n\n---\n\n## Missing References（建议补充）\n\n- **Podolskiy et al. (2021)** \"Revisiting the Calibration of Modern Neural Networks\"——与 depth-conditional calibration 相关，且论文涉及 ordinal classification 的 calibration 问题但未引用校准领域的工作。\n- **Ordinal regression in NLP** 相关工作：论文引用的 CORAL/CLOC 均为 CV 领域，NLP 中的 ordinal regression 方法（如 sentiment intensity, essay scoring）可作为 methodology 参考。\n\n---\n\n## 主要优势\n\n- **问题定义新颖且重要**：将递归生成深度估计形式化为 ordinal classification 是一个 well-motivated 且此前未被探索的方向，填补了 binary detection 和 model collapse 理论之间的空白。\n- **Atlas 构建系统、覆盖面广**：3 model families × 3 decoding strategies × 4+ depths 的网格设计比同领域大多数工作更系统。\n- **特征分析扎实**：SHAP + Gini + Spearman 三重验证，permutation importance 排序在 Table 16 中跨 cell 一致，说明 p90_ppl 和 var_surprisal 确实是 robust 的 depth signal。\n- **附录充实**：18 个 appendix section 覆盖了 temperature robustness、domain bias、downstream curation PoC、cross-boundary generalization 等多个方向，展现了较好的 thoroughness。\n- **EDD 指标有独立价值**：即使具体数值因 classifier/reference model 而变，EDD 作为刻画\"可区分深度边界\"的 operational metric 对后续研究有参考意义。\n",
  "reviewer_id": "1",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 — Round 1 审稿意见\n\n**论文**: \"How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\"\n**审稿侧重**: 方法严谨性 + 实验设计 + 统计分析\n**对照标准**: ACL ARR Review Form (2025 版, soundness/excitement/overall 三维度制)\n\n---\n\n## 总体评分\n**Overall**: 3.0 / 5（Findings 水平）\n**一句话总结**: 问题定义新颖、atlas 构建系统，但核心指标 EDD₀.₇₅=4 的统计支撑在模型间差异悬殊且未被如实反映，d0 inflation 使 headline 数字产生误导，削弱了方法论声称的严谨性。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2.5/5 | 核心 EDD₀.₇₅=4 claim 的统计支撑不均匀（GPT-2 XL 在 d3-vs-d4 边界无显著性），d0 inflation 未充分 qualify，reference model circularity 未被有效排除 |\n| Excitement | 3.5/5 | 将递归生成深度估计形式化为 ordinal classification 是新颖的切入角度，Depth Degradation Atlas 有独立参考价值 |\n| Overall | 3.0/5 | 问题重要、方向有趣，但实验-声明之间的 gap 需要修补才能达到 conference 接收标准 |\n| Reproducibility | 3/5 | 特征提取管线可复现，但 LoRA 参数无选择依据，DCOL 迭代细节分散 |\n| Confidence | 4/5 | 仔细阅读全文含附录，熟悉 model collapse 和 AI-text detection 两个领域 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] EDD₀.₇₅=4 的 claim 在 abstract 中被过度概括\n\n- 具体位置：Abstract 第 7-8 行（\"finding EDD₀.₇₅=4 for extended recursive generation depth estimation\"）；§4.3 第 2 段\n- 问题：Abstract 将 EDD₀.₇₅=4 作为通用结论呈现，但 §4.3 明确写道\"At T=0.75, 7/9 atlas cells maintain EDD ≥ 3 on the primary benchmark\"——即 2/9 的 atlas cell 在 T=0.75 时连 EDD≥3 都不满足。更关键的是，d3-vs-d4 边界的 pairwise AUC 在三个模型族间的统计显著性差异悬殊：根据 Figure 1 中 bootstrap 95% CI，Pythia d3-vs-d4 AUC 的 CI 下界明显高于 0.75，但 GPT-2 XL 的 CI 跨越 0.75 阈值。论文未报告各 model-strategy cell 在 d3-vs-d4 边界的 bootstrap p-value，读者无法判断 EDD₀.₇₅=4 在每个 cell 中是否有统计显著支撑。\n- 为什么影响接收：EDD₀.₇₅=4 是全文的 headline finding。如果这一结论仅在部分配置中统计显著，而在其他配置中不显著（或边际显著），则 abstract 的表述构成 overclaiming，违反 ARR soundness 要求。\n- 建议修改方向：(1) 在 abstract 中改为条件性表述（如\"EDD₀.₇₅ reaches 4 for nucleus sampling across all three model families; under temperature and top-k, 7/9 cells achieve EDD ≥ 3\"）；(2) Table 17 (Appendix A.16) 或主文中增加每个 cell 在 d3-vs-d4 边界的 bootstrap p-value 和 CI；(3) 如果某些 cell 的 d3-vs-d4 AUC 在 0.75 附近无显著性，必须明确标注。\n\n**N2** [critical] 关键结果表（Table 2, 4, 5）缺乏不确定性度量\n\n- 具体位置：Table 2（4-class RF accuracy, 9 cells）；Table 4（cross-model transfer）；Table 5（cross-strategy transfer）\n- 问题：Table 2 报告 9 个 cell 的 4-class accuracy，无标准差、无置信区间、无 bootstrap CI。Figure 1 使用了 bootstrap 95% CI（shaded bands），说明作者有计算 CI 的能力和数据，但未将这一实践推广到核心数字。Table 4/5 同样缺乏 CI。对于 5-fold stratified CV，至少应报告 fold 间的 mean ± std。\n- 为什么影响接收：ACL ARR soundness 标准要求 claims 有充分统计支撑。没有 CI 的 accuracy 数字无法判断 cell 间差异是否显著、transfer 是否真正有效。\n- 建议修改方向：所有准确率表格增加 5-fold CV 的 mean ± std 或 bootstrap 95% CI。\n\n**N3** [critical] d0 inflation 对 headline metrics 的影响未在主文中充分 qualify\n\n- 具体位置：Table 2（主文 p4）vs Table 7（Appendix A.3 per-class recall）\n- 问题：Table 2 中 4-class accuracy 最高达 85.4%（GPT-2 XL, temp），但 Table 7 显示 d2 在每个 cell 中都是 recall 最低的类别（最低仅 46% 在 Pythia holdout 下）。d0 recall 则在所有 cell 中 >98%。这意味着 4-class accuracy 被 d0 的近完美分类大幅拉高。主文 §4.1 仅用一句话提到\"Depth-0 recall exceeds 98% in all 9 cells\"，但未报告 d2 recall 的困难程度，也未讨论 class imbalance 的影响。\n- 为什么影响接收：如果方法对 d2 的区分能力弱到只有 46% recall，那么\"depth estimation\"的实际效用大打折扣。reviewer 需要看到 macro-F1 或 balanced accuracy 来评估真实性能。\n- 建议修改方向：(1) 主文 Table 2 增加 macro-F1 或 balanced accuracy 列；(2) 在 §4.1 中明确讨论 d2 的困难性及原因（d2 是中间深度，特征可能与 d1/d3 重叠）；(3) Figure 2（confusion matrix）中标注 per-class recall 数字。\n\n**N4** [major] Reference model 选择存在 circularity 且 ablation 不充分\n\n- 具体位置：§3.3（feature extraction pipeline）；§8 Limitations（\"Reference model dependency\"）；Appendix A.12\n- 问题：所有 19 个统计特征均基于 Pythia-1.4B 作为 reference model 计算。当分类 Pythia 生成的文本时，reference model 即 generator（或同系列近亲），构成 self-model feature extraction（§3.2 也承认了这一点）。Appendix A.12 用 OLMo-1B 替换 Pythia-1.4B 做 reference，结果准确率下降 2-40pp，但 OLMo-1B 与 Pythia-1.4B 共享相似的 scale (~1B) 和 autoregressive 架构——这不是一个有力的 ablation。如果 reference model 的选择如此敏感，那么方法的通用性声称就需要更多支撑。\n- 为什么影响接收：如果 Pythia 作为 reference model 给 Pythia-generated text 带来了系统性优势，那么整个 atlas 的结论可能存在偏差。\n- 建议修改方向：(1) 至少用一个不同 scale 或架构的 reference model（如 GPT-2 XL 或 7-8B 模型）做完整 ablation；(2) 在主文中明确量化 self-model vs cross-model feature extraction 的性能差距；(3) 讨论理想的 reference model 选择标准。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] LoRA 训练配置缺乏选择依据\n\n- 具体位置：§3.2（generation pipeline）；Table 8（DCOL iterations, Appendix A.4）\n- 问题：§3.2 提到使用 LoRA 微调生成模型（每一代递归），但未说明 rank、alpha、target modules 的选择理由。Table 8 列出 6 个 DCOL 迭代中的不同配置（DeBERTa FT vs LoRA, 不同学习率），但这些是 DCOL 过程的记录，不是系统性的超参数 ablation。LoRA rank 直接影响模型在递归训练中的 capacity，进而影响 collapse 速度和特征分布——这是一个核心 confound。\n- 建议：增加 LoRA rank ablation（如 rank=4,8,16,32），或说明选择依据（如 follow 某篇先前工作的设定）。\n\n**W2** [warning] Cross-strategy transfer 弱（59.1%）但主文对其实际影响的讨论不够突出\n\n- 具体位置：§5.3（Table 5）；§6 Discussion\n- 问题：3-class cross-strategy accuracy 为 59.1%（chance=33%），意味着在不知道解码策略的实际场景中，方法的深度估计能力有限。§6 的 Discussion 段提到需要\"strategy-conditioned classifiers\"，但这一重大局限被放在一个长段落中而非作为独立的 limitation 讨论。\n- 建议：在 Limitations 中单独一段讨论策略依赖性，并量化在\"策略未知\"场景下方法的预期性能下界。\n\n**W3** [warning] Negative control 暴露的历史 confound 未充分透明\n\n- 具体位置：Appendix A.9 Sub-C（Negative control）\n- 问题：Sub-C 报告 seed-group prediction accuracy 在\"修复前\"为 20.8%，修复后降到 10.2%（接近 10-class chance）。这表明实验设计曾存在 depth-group confound——seed 分组与 depth 之间有泄漏。论文未解释这个 confound 的具体性质和修复方法。\n- 建议：明确描述原始 confound 的来源（是 seed 分配不均还是 data pipeline bug？）和修复措施，让 reviewer 评估修复是否充分。\n\n**W4** [warning] EDD 定义依赖 classifier capacity，非分布内禀属性\n\n- 具体位置：Definition 1（§3.4）\n- 问题：EDD 通过 binary RF classifier 的 pairwise AUC 定义。这意味着 EDD 不仅反映深度间的内禀可区分性，还反映所选 classifier 的能力上限。一个更强的 classifier（如 neural model）可能会得到更高的 EDD。论文在 §8 中提到\"this comparison is bounded by backbone scale\"但未系统讨论 classifier choice 对 EDD 的影响。\n- 建议：(1) 讨论 EDD 是 method-dependent 的 operational metric 而非 distribution-intrinsic 的性质；(2) 或在 §3.4 用至少两种不同 classifier 报告 EDD 来展示稳定性（RF 在 §3.4 已选，Appendix 可加 LightGBM 或 logistic regression 的 EDD 对比）。\n\n---\n\n## 小问题（不影响接收）\n\n- **引用年份不一致**：`he2021_deberta_v3` bib 条目标记 year=2023，OpenAlex 匹配结果为 2021；`alemohammad2024_mad` 第一作者与 OpenAlex 不一致（bib=Alemohammad vs API=Casco-Rodriguez）。建议核对。\n- **knowledge_collapse2025** 和 **falahati2026_curated** 在 OpenAlex 上未找到记录，可能是极新的 preprint。如果引用这些作为支撑论点，需确保这些论文确实存在且已公开。\n- Table 1 的 19 个特征在不同类别中的分配描述可以更清晰（Perplexity: 9, Surprisal: 3, Lexical: 4, Repetition: 3，但正文和表格的编号跳跃容易混淆）。\n- Figure 4（feature importance heatmap）色标的可读性较低，建议使用离散色标或增大字体。\n- Abstract 中\"with the top 5 achieving 97.6% of full-scale performance\"这一表述容易被误读为\"97.6% accuracy\"，建议改为\"retaining 97.6% of the 19-feature accuracy\"以消除歧义。\n\n---\n\n## Questions to Authors\n\n**Q1**: EDD₀.₇₅=4 是否在所有 9 个 atlas cell 中都有 bootstrap 显著性支撑？请报告每个 cell 在 d3-vs-d4 边界的 bootstrap p-value。\n\n**Q2**: 如果用 GPT-2 XL（而非 Pythia-1.4B）作为 reference model，Table 2 中各 cell 的 accuracy 变化如何？是否会改变 EDD 的结论？\n\n**Q3**: Appendix A.9 Sub-C 中提到 seed-group confound 的\"fix\"——具体修复了什么？修复前后的 per-depth accuracy 是否有变化？\n\n**Q4**: 有没有考虑用 distribution-free 的方法（如 MMD 或 permutation test）直接衡量深度间的分布距离，而非通过 classifier AUC 间接衡量？这可以提供一个不依赖 classifier capacity 的 EDD 变体。\n\n**Q5**: 主文报告的 4-class accuracy（Table 2）是否已用 balanced/stratified sampling 确保 class balance？如果 d0 样本多于 d3，accuracy 会被 d0 自然拉高。\n\n---\n\n## Missing References（建议补充）\n\n- **Podolskiy et al. (2021)** \"Revisiting the Calibration of Modern Neural Networks\"——与 depth-conditional calibration 相关，且论文涉及 ordinal classification 的 calibration 问题但未引用校准领域的工作。\n- **Ordinal regression in NLP** 相关工作：论文引用的 CORAL/CLOC 均为 CV 领域，NLP 中的 ordinal regression 方法（如 sentiment intensity, essay scoring）可作为 methodology 参考。\n\n---\n\n## 主要优势\n\n- **问题定义新颖且重要**：将递归生成深度估计形式化为 ordinal classification 是一个 well-motivated 且此前未被探索的方向，填补了 binary detection 和 model collapse 理论之间的空白。\n- **Atlas 构建系统、覆盖面广**：3 model families × 3 decoding strategies × 4+ depths 的网格设计比同领域大多数工作更系统。\n- **特征分析扎实**：SHAP + Gini + Spearman 三重验证，permutation importance 排序在 Table 16 中跨 cell 一致，说明 p90_ppl 和 var_surprisal 确实是 robust 的 depth signal。\n- **附录充实**：18 个 appendix section 覆盖了 temperature robustness、domain bias、downstream curation PoC、cross-boundary generalization 等多个方向，展现了较好的 thoroughness。\n- **EDD 指标有独立价值**：即使具体数值因 classifier/reference model 而变，EDD 作为刻画\"可区分深度边界\"的 operational metric 对后续研究有参考意义。\n",
    "reviewer_id": "1",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 347 · 2026-05-16T20:14:11.347395+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3914
}
```

</details>

---


### Assistant

_source line 348 · 2026-05-16T20:14:30.598606+00:00_

Round 1 审稿意见已提交。

总结：给出 Overall 3.0/5（Findings 水平），识别了 4 个 Must-Fix 和 4 个 Should-Fix 问题。核心关切是：

1. **EDD₀.₇₅=4 overclaiming**：abstract 呈现为通用结论，但 2/9 atlas cell 在 T=0.75 时连 EDD≥3 都不满足，且各模型族在 d3-vs-d4 边界的统计显著性差异悬殊
2. **关键表格无不确定性度量**：Table 2/4/5 均缺乏 CI 或 std，与论文"统计指纹"的方法论定位不一致
3. **d0 inflation 使 headline accuracy 误导**：d0 recall >98% 大幅拉高 4-class accuracy，但 d2 recall 最低仅 46%
4. **Reference model circularity**：Pythia-1.4B 同时作为 reference model 和 generator 之一，ablation 不充分

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1"
}
```

</details>

---


## Round 12

## Round 12

16 recorded events


### User

_source line 349 · 2026-05-16T20:14:59.729255+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix 问题：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

## Reviewer 2 完整审稿意见

**Overall**: 3/5 (Findings)

### Must-Fix 问题

**N1** [critical] Related Work 遗漏关键 position paper：Schaeffer et al. 2025 "Position: Model Collapse Does Not Mean What You Think" (arXiv:2503.03150, ICML 2025)

- 该文指出 model collapse 文献存在 8 种相互冲突的定义，且多数"collapse"预测依赖不现实假设（纯合成数据替代训练）。本文的 benchmark 构建恰好采用了 Schaeffer et al. 批评的极端设定（每一代完全用上一代合成数据 fine-tune，Section 3.2），却未讨论这一已发表的批评。这直接影响论文 ecological validity 的论证。
- 为什么影响接收：如果 reviewer 或 AC 熟悉 Schaeffer 2025，会认为 framing 不够诚实——论文声称解决"wild"中的递归污染（Introduction L4-6），但 benchmark 使用的 100% synthetic replacement 设定正是 Schaeffer 等人认为不现实的。

**N2** [critical] 方法论新颖性不足：核心方法为"19 个统计特征 + Random Forest"，无 learned representation、无新 loss、无新架构

- 19 个 candidate features 中，perplexity 统计量和 lexical diversity 是 text quality / AI detection 文献中的标准特征。Random Forest 是 off-the-shelf 分类器。Section 5.1 证明 5 种 classifier 结果一致（≤0.4pp），恰恰说明方法层面没有贡献——signal 完全在 feature 中，而 feature 选择本身也是常见的。

**N3** [critical] Downstream curation PoC 无法支撑 practical utility claim

- Discussion 声称 "depth estimation enables depth-graduated data curation"，但 Appendix D.7 的 curation PoC 显示 rf_soft vs unfiltered 仅有 +0.043 PPL 差异（p=0.407，不显著），rf_strict 甚至比 unfiltered 更差。唯一显著的结果是 RF-filtered vs random subsampling（p<0.001），但这只证明"非随机选择比随机好"。

### Should-Fix 问题

**W1** EDD metric 的增量价值 vs Dohmatob 2024 "A Tale of Tails" 的 scaling law — EDD 是将 Dohmatob 的 insight 操作化为 threshold-based metric，但未讨论增量信息是什么。

**W2** Cross-strategy transfer 的 practical implication 被弱化 — d1-d3 balanced accuracy 仅 45.9%（chance = 33%），部署时策略未知则系统接近 chance。

**W3** d0 inflation 使 headline accuracy 具有误导性 — Abstract 报告 "70-85% four-class accuracy" 被 d0 near-perfect recall 大幅拉高。

**W4** Ordinal classification related work 过于单薄 — 仅引用 CORAL 和 CLOC，缺 McCullagh 1980, Rennie & Srebro 2005 等经典文献。

**W5** 引用完整性问题 — alemohammad2024_mad 作者不一致，knowledge_collapse2025 和 falahati2026_curated 在 OpenAlex 未找到。

### Questions to Authors

Q1: 如果直接用 p90_ppl 单特征做 threshold-based depth filtering，curation 效果是否等价于 RF-based filtering？
Q2: 如果训练数据中只有 10%-50% 来自上一代合成输出，depth fingerprint 是否仍可检测？
Q3: Cross-model recursive chain 的 reverse control 是否排除了 "data quality degradation fingerprint"（signal 来自质量下降而非递归深度本身）？

---

请逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 350 · 2026-05-16T20:16:04.096198+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 351 · 2026-05-16T20:16:05.050482+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 352 · 2026-05-16T20:16:05.655213+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 353 · 2026-05-16T20:16:05.656396+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1560
}
```

</details>

---


### Tool result

_source line 354 · 2026-05-16T20:16:06.964574+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1309
}
```

</details>

---


### Tool result

_source line 355 · 2026-05-16T20:16:06.965407+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1914
}
```

</details>

---


### Tool call

_source line 356 · 2026-05-16T20:16:14.813816+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 357 · 2026-05-16T20:16:15.870414+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 358 · 2026-05-16T20:16:16.324897+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1511
}
```

</details>

---


### Tool call

_source line 359 · 2026-05-16T20:16:16.325338+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 360 · 2026-05-16T20:16:17.532056+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1206
}
```

</details>

---


### Tool result

_source line 361 · 2026-05-16T20:16:17.633326+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1762
}
```

</details>

---


### Tool call

_source line 362 · 2026-05-16T20:18:43.230160+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: 遗漏 Schaeffer et al. 2025 position paper**\n\n同意这是一个重要遗漏。论文的 benchmark 确实采用 100% synthetic replacement 设定（§3.2: \"each depth is produced by a model trained on prior-depth data\"），且 Introduction L4-6 将问题框定为与 wild web-crawled corpora 相关——这与 Schaeffer et al. 的核心批评直接相关。\n\n但需补充：论文在 §6 Discussion 中已有部分自我限定：\"This protocol isolates the recursive depth variable but diverges from wild recursive contamination, where models are pretrained on mixed corpora containing post-generation outputs as unknown proportions\"。§8 Limitations 也提到 \"EDD monotonicity assumption\" 可能因 Bakshi & Chakraborty (2026) 所示的 early-recursion improvement 而不成立。因此问题的严重程度是\"引用缺失 + framing 可改善\"，而非\"完全未意识到该限制\"。\n\n**建议**：引用 Schaeffer et al. 2025，并在 §2 Related Work 或 §6 Discussion 中明确讨论 100% replacement 设定与实际 partial mixing 场景的差距。这也应与 R2-Q2（10-50% mixing 场景下 fingerprint 是否仍可检测）联动讨论。\n\n---\n\n**[REBUT] R2-N2: 方法论新颖性不足**\n\n不同意将此标记为 critical/must-fix。理由：\n\n1. **贡献类型判断**：这是一篇 *empirical study + problem formulation* 论文，不是 methods 论文。核心贡献是：(a) 将递归深度估计形式化为 ordinal classification——这在此前文献中未被提出；(b) 系统性构建 3×3 Depth Degradation Atlas（180K 样本）；(c) 提出 EDD metric 来量化可区分深度边界。这三项均非\"standard features + RF\"能概括的。\n\n2. **§5.1 的 classifier invariance 是 strength 而非 weakness**：Table 3 显示 RF、XGBoost、LightGBM 在相同 19 个特征上的准确率差异 ≤0.4pp（Pythia: 78.8/79.0/78.8; GPT-2 XL: 85.9/86.2/86.5）。这恰恰说明 signal 是 feature-intrinsic 的、不依赖特定 classifier capacity——这是一个 *positive finding*，证明 depth fingerprint 是 robust 的 distributional signal，而非 classifier overfitting 的产物。\n\n3. **ACL/EMNLP 的 contribution scope**：许多有影响力的 *ACL 论文使用标准方法解决新问题（如 Ghostbuster [Verma et al., 2024] 用 trigram features + logistic regression，仍被 NAACL 接收）。EMNLP 评审标准不要求每篇论文都提出 new architecture。\n\n4. **不过**，我同意论文可以在 §3.3 中更明确地讨论为什么 *不* 用 learned representations：Appendix A.7 和 A.8 已展示 end-to-end PLM (DeBERTa, RoBERTa) 的性能反而更低（58-65% vs RF 的 70-85%），且 PLM \"fail to capture perplexity distribution statistics\"（A.7）。这个 negative result 应被提升到主文，作为支撑\"statistical features 优于 learned features\"的论据。\n\n---\n\n**[AGREE] R2-N3: Downstream curation PoC 统计支撑不足**\n\n同意 PoC 的证据力度偏弱。但需要纠正 R2 对 claim 的定性：\n\n1. **论文的实际 claim 是 \"matching, not improving\"**：Appendix A.14 (Extended Discussion) 的原文是\"RF-filtered subsets match unfiltered quality with 44% of the data\"。§6 Discussion 说\"depth estimation enables depth-graduated data curation\"——这是一个 *possibility* claim，不是一个 *improvement* claim。因此 PoC 的标准应该是\"能否用更少数据达到相当质量\"，而非\"能否超过 unfiltered\"。\n\n2. **但 R2 指出的统计问题确实存在**：Table 14 中 rf_soft vs unfiltered 的 p 值未达 0.05 水平，rf_strict 表现更差——这说明在当前 PoC 规模（5 seeds, Pythia-410M）下，depth-based filtering 的价值未被充分证明。即使是\"matching with less data\"的 claim，也需要 non-inferiority test 或等价性检验来支撑，而非仅靠 paired t-test 的 non-significance。\n\n3. **RF-filtered vs random subsampling 显著（p<0.001）** 确实只说明\"非随机选择优于随机\"，这一结论的增量信息有限。\n\n**建议**：(a) 将 curation PoC 的表述从\"enables curation\"降级为\"provides preliminary evidence that depth-aware filtering can maintain quality with reduced data volume\"；(b) 增加 PoC 规模（更多 seeds 或更大 base model）以获得足够 statistical power；(c) 或者直接将 curation 定位为 future work 而非 contribution。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: EDD vs Dohmatob 2024 scaling law 的增量讨论**\n\n同意。§2 Related Work 引用了 Dohmatob et al. (2024) \"formalize tail narrowing vs. cutting\"，但未讨论 EDD 与 scaling law 框架的关系。EDD 可被视为 Dohmatob 理论预测的 *empirical operationalization*——理论预测 tail 收缩会随递归加深而恶化，EDD 则量化了这一恶化的实证边界。论文应在 §3.4 或 §6 中明确阐述这一关系，而非让读者自行推断。\n\n补充我自己的相关发现（R1-W4）：EDD 作为 classifier-dependent metric 而非 distribution-intrinsic measure，其与 Dohmatob 的 distribution-level scaling law 之间存在一个 gap。论文应讨论 EDD 是否随 classifier capacity 增强而单调增加，以及这对 metric 的可解释性意味着什么。\n\n---\n\n**[AGREE] R2-W2: Cross-strategy transfer 的实际影响**\n\n完全同意。这与我的 R1-W2 一致。Table 5 显示 cross-strategy transfer 的整体准确率仅 59.1%（4-class），而 R2 指出 d1-d3 balanced accuracy 进一步降至 45.9%（排除 d0 后更接近 chance）。这意味着在不知道解码策略的实际场景中，系统基本无法有效工作。\n\n我补充一个 R2 未提到的细节：§5.3 中 \"per-strategy z-score normalization partially corrects the d1/d2 boundary inversion under temperature sampling\" 说明策略效应不仅降低准确率，还导致 depth ordering 反转——这比 accuracy 下降更严重，因为它破坏了 ordinal structure。\n\n---\n\n**[AGREE] R2-W3: d0 inflation**\n\n完全同意。这与我的 R1-N3 一致。我将此标记为 must-fix 级别（R1-N3），R2 标记为 should-fix——我认为 must-fix 更合适，因为 headline accuracy 是读者对论文的第一印象，如果这些数字被 d0 严重拉高且未在主文中充分 qualify，构成 misleading presentation。\n\n具体数字：Table 2 中 GPT-2 XL temperature 的 4-class accuracy 为 85.4%，但 Table 7 显示同一 cell 的 d2 recall 仅约 66.1%。这 ~19pp 的 gap 应在主文中明确呈现。\n\n---\n\n**[AGREE] R2-W4: Ordinal classification related work 过于单薄**\n\n同意 McCullagh (1980) 的 proportional odds model 是 ordinal regression 的开创性工作，作为一篇将 depth estimation 定义为 ordinal classification 的论文，不引用它是一个明显遗漏。但我将此视为 minor 而非 should-fix：论文不以 ordinal classification 方法论为贡献，CORAL 和 CLOC 的引用足以说明作者了解该领域，缺少 McCullagh 1980 更多是 scholarly completeness 问题而非 soundness 问题。\n\n---\n\n**[AGREE] R2-W5: 引用完整性**\n\n同意。我在 R1 minor issues 中也指出了相同问题（alemohammad2024_mad 作者不一致，knowledge_collapse2025 和 falahati2026_curated 在 OpenAlex 未找到，he2021_deberta_v3 年份不一致）。这些应在 camera-ready 前修正。\n\n---\n\n### 对 R2 Questions 的补充意见\n\n**R2-Q1**（p90_ppl 单特征 threshold vs RF）：好问题。Table 16（Appendix A.15）和 Figure 4 均显示 p90_ppl 是跨 cell 最一致的 top-1 feature。如果单特征 threshold 效果接近 RF，则进一步支撑了 R2-N2 的论点（method 层面无增量贡献）。但也进一步支撑了论文的 *finding* 贡献（depth signal 是 distributional 的、可通过简单统计量捕获）。\n\n**R2-Q2**（10-50% partial mixing）：这是最关键的 ecological validity 问题，直接关联 R2-N1。论文目前完全没有在 partial mixing 设定下的实验。Appendix A.10 (Wild-Data Calibration) 测试了 out-of-distribution human text（WikiText-103, C4），但测试的是 *分类器对 human text 的鲁棒性*，不是 partial mixing 下的 depth fingerprint 存活性。这是一个重要的实验空白。\n\n**R2-Q3**（cross-model chain 的 quality degradation confound）：这与我的理解一致。Appendix A.13 的 cross-model recursive chain 实验表明\"depth signal is a property of the recursive process itself rather than of any individual generator\"（p14），但未设计 *matched-quality control*——即深度不同但文本质量相当的样本对，以排除 quality degradation 作为 confound 的可能性。Appendix A.9 Sub-C 的 negative control（seed-group prediction）排除了 seed-specific 信号，但未排除 quality-correlated 信号。\n\n---\n\n### R1 与 R2 的共识总结\n\n| 问题 | R1 | R2 | 共识 |\n|------|----|----|------|\n| EDD₀.₇₅=4 overclaiming | N1 (critical) | — | R1 独有，R2 未涉及 |\n| 关键表格缺 CI | N2 (critical) | — | R1 独有 |\n| d0 inflation | N3 (critical) | W3 (warning) | 共识，R1 严重程度更高 |\n| Reference model circularity | N4 (major) | — | R1 独有 |\n| 缺 Schaeffer 2025 | — | N1 (critical) | R2 独有，R1 同意 |\n| 方法新颖性不足 | — | N2 (critical) | R2 独有，R1 反驳 |\n| Curation PoC 弱 | — | N3 (critical) | R2 独有，R1 同意（降级为 should-fix） |\n| Cross-strategy 实际影响 | W2 (warning) | W2 (warning) | 完全共识 |\n| LoRA 配置无依据 | W1 (warning) | — | R1 独有 |\n| EDD 定义 classifier-dependent | W4 (warning) | W1 (warning) | 共识，角度互补 |\n| Ordinal classification refs 单薄 | — | W4 (warning) | R2 独有，R1 同意降级为 minor |\n",
  "reviewer_id": "1",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: 遗漏 Schaeffer et al. 2025 position paper**\n\n同意这是一个重要遗漏。论文的 benchmark 确实采用 100% synthetic replacement 设定（§3.2: \"each depth is produced by a model trained on prior-depth data\"），且 Introduction L4-6 将问题框定为与 wild web-crawled corpora 相关——这与 Schaeffer et al. 的核心批评直接相关。\n\n但需补充：论文在 §6 Discussion 中已有部分自我限定：\"This protocol isolates the recursive depth variable but diverges from wild recursive contamination, where models are pretrained on mixed corpora containing post-generation outputs as unknown proportions\"。§8 Limitations 也提到 \"EDD monotonicity assumption\" 可能因 Bakshi & Chakraborty (2026) 所示的 early-recursion improvement 而不成立。因此问题的严重程度是\"引用缺失 + framing 可改善\"，而非\"完全未意识到该限制\"。\n\n**建议**：引用 Schaeffer et al. 2025，并在 §2 Related Work 或 §6 Discussion 中明确讨论 100% replacement 设定与实际 partial mixing 场景的差距。这也应与 R2-Q2（10-50% mixing 场景下 fingerprint 是否仍可检测）联动讨论。\n\n---\n\n**[REBUT] R2-N2: 方法论新颖性不足**\n\n不同意将此标记为 critical/must-fix。理由：\n\n1. **贡献类型判断**：这是一篇 *empirical study + problem formulation* 论文，不是 methods 论文。核心贡献是：(a) 将递归深度估计形式化为 ordinal classification——这在此前文献中未被提出；(b) 系统性构建 3×3 Depth Degradation Atlas（180K 样本）；(c) 提出 EDD metric 来量化可区分深度边界。这三项均非\"standard features + RF\"能概括的。\n\n2. **§5.1 的 classifier invariance 是 strength 而非 weakness**：Table 3 显示 RF、XGBoost、LightGBM 在相同 19 个特征上的准确率差异 ≤0.4pp（Pythia: 78.8/79.0/78.8; GPT-2 XL: 85.9/86.2/86.5）。这恰恰说明 signal 是 feature-intrinsic 的、不依赖特定 classifier capacity——这是一个 *positive finding*，证明 depth fingerprint 是 robust 的 distributional signal，而非 classifier overfitting 的产物。\n\n3. **ACL/EMNLP 的 contribution scope**：许多有影响力的 *ACL 论文使用标准方法解决新问题（如 Ghostbuster [Verma et al., 2024] 用 trigram features + logistic regression，仍被 NAACL 接收）。EMNLP 评审标准不要求每篇论文都提出 new architecture。\n\n4. **不过**，我同意论文可以在 §3.3 中更明确地讨论为什么 *不* 用 learned representations：Appendix A.7 和 A.8 已展示 end-to-end PLM (DeBERTa, RoBERTa) 的性能反而更低（58-65% vs RF 的 70-85%），且 PLM \"fail to capture perplexity distribution statistics\"（A.7）。这个 negative result 应被提升到主文，作为支撑\"statistical features 优于 learned features\"的论据。\n\n---\n\n**[AGREE] R2-N3: Downstream curation PoC 统计支撑不足**\n\n同意 PoC 的证据力度偏弱。但需要纠正 R2 对 claim 的定性：\n\n1. **论文的实际 claim 是 \"matching, not improving\"**：Appendix A.14 (Extended Discussion) 的原文是\"RF-filtered subsets match unfiltered quality with 44% of the data\"。§6 Discussion 说\"depth estimation enables depth-graduated data curation\"——这是一个 *possibility* claim，不是一个 *improvement* claim。因此 PoC 的标准应该是\"能否用更少数据达到相当质量\"，而非\"能否超过 unfiltered\"。\n\n2. **但 R2 指出的统计问题确实存在**：Table 14 中 rf_soft vs unfiltered 的 p 值未达 0.05 水平，rf_strict 表现更差——这说明在当前 PoC 规模（5 seeds, Pythia-410M）下，depth-based filtering 的价值未被充分证明。即使是\"matching with less data\"的 claim，也需要 non-inferiority test 或等价性检验来支撑，而非仅靠 paired t-test 的 non-significance。\n\n3. **RF-filtered vs random subsampling 显著（p<0.001）** 确实只说明\"非随机选择优于随机\"，这一结论的增量信息有限。\n\n**建议**：(a) 将 curation PoC 的表述从\"enables curation\"降级为\"provides preliminary evidence that depth-aware filtering can maintain quality with reduced data volume\"；(b) 增加 PoC 规模（更多 seeds 或更大 base model）以获得足够 statistical power；(c) 或者直接将 curation 定位为 future work 而非 contribution。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: EDD vs Dohmatob 2024 scaling law 的增量讨论**\n\n同意。§2 Related Work 引用了 Dohmatob et al. (2024) \"formalize tail narrowing vs. cutting\"，但未讨论 EDD 与 scaling law 框架的关系。EDD 可被视为 Dohmatob 理论预测的 *empirical operationalization*——理论预测 tail 收缩会随递归加深而恶化，EDD 则量化了这一恶化的实证边界。论文应在 §3.4 或 §6 中明确阐述这一关系，而非让读者自行推断。\n\n补充我自己的相关发现（R1-W4）：EDD 作为 classifier-dependent metric 而非 distribution-intrinsic measure，其与 Dohmatob 的 distribution-level scaling law 之间存在一个 gap。论文应讨论 EDD 是否随 classifier capacity 增强而单调增加，以及这对 metric 的可解释性意味着什么。\n\n---\n\n**[AGREE] R2-W2: Cross-strategy transfer 的实际影响**\n\n完全同意。这与我的 R1-W2 一致。Table 5 显示 cross-strategy transfer 的整体准确率仅 59.1%（4-class），而 R2 指出 d1-d3 balanced accuracy 进一步降至 45.9%（排除 d0 后更接近 chance）。这意味着在不知道解码策略的实际场景中，系统基本无法有效工作。\n\n我补充一个 R2 未提到的细节：§5.3 中 \"per-strategy z-score normalization partially corrects the d1/d2 boundary inversion under temperature sampling\" 说明策略效应不仅降低准确率，还导致 depth ordering 反转——这比 accuracy 下降更严重，因为它破坏了 ordinal structure。\n\n---\n\n**[AGREE] R2-W3: d0 inflation**\n\n完全同意。这与我的 R1-N3 一致。我将此标记为 must-fix 级别（R1-N3），R2 标记为 should-fix——我认为 must-fix 更合适，因为 headline accuracy 是读者对论文的第一印象，如果这些数字被 d0 严重拉高且未在主文中充分 qualify，构成 misleading presentation。\n\n具体数字：Table 2 中 GPT-2 XL temperature 的 4-class accuracy 为 85.4%，但 Table 7 显示同一 cell 的 d2 recall 仅约 66.1%。这 ~19pp 的 gap 应在主文中明确呈现。\n\n---\n\n**[AGREE] R2-W4: Ordinal classification related work 过于单薄**\n\n同意 McCullagh (1980) 的 proportional odds model 是 ordinal regression 的开创性工作，作为一篇将 depth estimation 定义为 ordinal classification 的论文，不引用它是一个明显遗漏。但我将此视为 minor 而非 should-fix：论文不以 ordinal classification 方法论为贡献，CORAL 和 CLOC 的引用足以说明作者了解该领域，缺少 McCullagh 1980 更多是 scholarly completeness 问题而非 soundness 问题。\n\n---\n\n**[AGREE] R2-W5: 引用完整性**\n\n同意。我在 R1 minor issues 中也指出了相同问题（alemohammad2024_mad 作者不一致，knowledge_collapse2025 和 falahati2026_curated 在 OpenAlex 未找到，he2021_deberta_v3 年份不一致）。这些应在 camera-ready 前修正。\n\n---\n\n### 对 R2 Questions 的补充意见\n\n**R2-Q1**（p90_ppl 单特征 threshold vs RF）：好问题。Table 16（Appendix A.15）和 Figure 4 均显示 p90_ppl 是跨 cell 最一致的 top-1 feature。如果单特征 threshold 效果接近 RF，则进一步支撑了 R2-N2 的论点（method 层面无增量贡献）。但也进一步支撑了论文的 *finding* 贡献（depth signal 是 distributional 的、可通过简单统计量捕获）。\n\n**R2-Q2**（10-50% partial mixing）：这是最关键的 ecological validity 问题，直接关联 R2-N1。论文目前完全没有在 partial mixing 设定下的实验。Appendix A.10 (Wild-Data Calibration) 测试了 out-of-distribution human text（WikiText-103, C4），但测试的是 *分类器对 human text 的鲁棒性*，不是 partial mixing 下的 depth fingerprint 存活性。这是一个重要的实验空白。\n\n**R2-Q3**（cross-model chain 的 quality degradation confound）：这与我的理解一致。Appendix A.13 的 cross-model recursive chain 实验表明\"depth signal is a property of the recursive process itself rather than of any individual generator\"（p14），但未设计 *matched-quality control*——即深度不同但文本质量相当的样本对，以排除 quality degradation 作为 confound 的可能性。Appendix A.9 Sub-C 的 negative control（seed-group prediction）排除了 seed-specific 信号，但未排除 quality-correlated 信号。\n\n---\n\n### R1 与 R2 的共识总结\n\n| 问题 | R1 | R2 | 共识 |\n|------|----|----|------|\n| EDD₀.₇₅=4 overclaiming | N1 (critical) | — | R1 独有，R2 未涉及 |\n| 关键表格缺 CI | N2 (critical) | — | R1 独有 |\n| d0 inflation | N3 (critical) | W3 (warning) | 共识，R1 严重程度更高 |\n| Reference model circularity | N4 (major) | — | R1 独有 |\n| 缺 Schaeffer 2025 | — | N1 (critical) | R2 独有，R1 同意 |\n| 方法新颖性不足 | — | N2 (critical) | R2 独有，R1 反驳 |\n| Curation PoC 弱 | — | N3 (critical) | R2 独有，R1 同意（降级为 should-fix） |\n| Cross-strategy 实际影响 | W2 (warning) | W2 (warning) | 完全共识 |\n| LoRA 配置无依据 | W1 (warning) | — | R1 独有 |\n| EDD 定义 classifier-dependent | W4 (warning) | W1 (warning) | 共识，角度互补 |\n| Ordinal classification refs 单薄 | — | W4 (warning) | R2 独有，R1 同意降级为 minor |\n",
    "reviewer_id": "1",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 363 · 2026-05-16T20:18:46.894581+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3664
}
```

</details>

---


### Assistant

_source line 364 · 2026-05-16T20:18:54.621806+00:00_

交叉回应已提交给 Review Director。总结：

- **3 项 AGREE**（N1 缺 Schaeffer 2025、N3 curation PoC 弱、W1-W5 全部同意）
- **1 项 REBUT**（N2 方法新颖性——论文是 empirical study + problem formulation 贡献，classifier invariance 是 strength 不是 weakness，且 PLM baselines 在 A.7/A.8 中表现更差）
- 共识总结表整理了 R1 与 R2 在 11 个问题上的严重程度对比

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1"
}
```

</details>

---


## Round 13

## Round 13

44 recorded events


### User

_source line 365 · 2026-05-17T06:20:48.339974+00:00_

[Round 8 审稿请求]:
## Round 8 审稿任务 — Reviewer 1（方法严谨性 + 实验有效性）

### 论文信息
- **标题**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
- **路径**: `projects/recursive_gen_depth_est/docs/paper/main.tex`（多文件结构：abstract.tex, introduction.tex, related_work.tex, method.tex, atlas.tex, generalization.tex, discussion.tex, conclusion.tex, section_appendix.tex）
- **目标 Venue**: EMNLP 2026 (Findings)，ARR May 2026 cycle
- **格式**: ACL template, long paper (8pp + refs + appendix), double-blind, `\usepackage[review]{acl}`
- **Deadline**: 2026-05-25

### 你的审查侧重
1. **统计方法论**：EDD 定义的数学正确性、统计检验充分性、confidence interval 报告
2. **实验设计**：confound 控制、数据泄漏风险、生态效度
3. **核心数值声明**：所有百分比、AUC、p-value 是否 internally consistent

### 历史遗留 open/in_progress issues（你需要逐条验证当前论文版本是否已修复）

**Critical/Must-Fix 级**：
- **R1-N2**: Table 2/4/5 仍无 std/CI/significance test。Figure 4 有 bootstrap CI 说明有计算能力但未推广。
- **R1-W2**: d0 inflation 问题——主文缺 macro-F1 或 d1-d3 balanced accuracy 列；d2 recall 困难性未讨论
- **R4-N1**: Abstract 中 EDD₀.₇₅=4 的统计限定——仅 Pythia p=0.001 显著，OLMo marginal (p=0.091), GPT-2 XL non-significant (p=0.505)。'consistent direction' 语义模糊。
- **R5-W4**: Related Work 遗漏 Schaeffer et al. 2025（直接挑战 benchmark ecological validity）、ordinal classics (McCullagh 1980, Rennie & Srebro 2005)、CCNet (Wenzek et al. 2020)

**Should-Fix/Warning 级**：
- **R1-W3**: LoRA rank sensitivity analysis 从未补充（rank ∈ {4, 16, 64}）
- **R5-N2**: Reference model 循环依赖——Pythia 同时为 generator 和 reference。Limitations 已讨论但建议增加 architecturally distinct reference ablation。
- **R5-W1**: Single LoRA instance per depth 的 non-independence 问题——Limitations 未明确讨论
- **R5-W5**: EDD 定义的 classifier-dependence 未明确声明为 operational measure
- **R7-W3**: Partial mixing (accumulation) 场景下 depth fingerprint 存活性完全未验证
- **R7-W4**: Depth estimation 可能本质为 text quality estimation 重新包装——缺 matched-quality control

### 评审要求
- 按 EMNLP Findings 标准严格评审
- 对每个历史 issue，明确判断：✅ RESOLVED / ⚠️ PARTIALLY ADDRESSED / ❌ NOT ADDRESSED
- 发现新问题按 Must-Fix / Should-Fix / Minor 分级
- 输出结构：Summary → Strengths → Weaknesses (编号) → Questions → Overall Assessment (score + confidence)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 366 · 2026-05-17T06:21:02.307063+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find paper tex files",
  "prompt": "Find all .tex files under projects/recursive_gen_depth_est/docs/paper/ and list them. Also check for .bib files. Use Glob with pattern \"projects/recursive_gen_depth_est/docs/paper/**/*.tex\" and \"projects/recursive_gen_depth_est/docs/paper/**/*.bib\" from /home/ubuntu/.agent-ml-research-idea_gen_0513_2/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Find paper tex files",
    "prompt": "Find all .tex files under projects/recursive_gen_depth_est/docs/paper/ and list them. Also check for .bib files. Use Glob with pattern \"projects/recursive_gen_depth_est/docs/paper/**/*.tex\" and \"projects/recursive_gen_depth_est/docs/paper/**/*.bib\" from /home/ubuntu/.agent-ml-research-idea_gen_0513_2/"
  }
}
```

</details>

---


### Tool call

_source line 367 · 2026-05-17T06:21:03.814090+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/recursive_gen_depth_est/docs/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/recursive_gen_depth_est/docs/paper/**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2"
  }
}
```

</details>

---


### Tool call

_source line 368 · 2026-05-17T06:21:03.965088+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
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

_source line 369 · 2026-05-17T06:21:04.066003+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 370 · 2026-05-17T06:21:04.066413+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/recursive_gen_depth_est/docs/paper/**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/recursive_gen_depth_est/docs/paper/**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2"
  }
}
```

</details>

---


### Tool result

_source line 371 · 2026-05-17T06:21:04.066610+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 372 · 2026-05-17T06:21:04.066749+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 373 · 2026-05-17T06:21:06.024797+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs -type f \\( -name \"*.tex\" -o -name \"*.bib\" \\) 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs -type f \\( -name \"*.tex\" -o -name \"*.bib\" \\) 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool call

_source line 374 · 2026-05-17T06:21:06.025251+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/ 2>/dev/null || echo \"Directory does not exist\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/ 2>/dev/null || echo \"Directory does not exist\""
  }
}
```

</details>

---


### Tool result

_source line 375 · 2026-05-17T06:21:06.177212+00:00_

total 48
drwxr-xr-x  4 ubuntu ubuntu  4096 May 15 05:24 .
drwxr-xr-x 12 ubuntu ubuntu  4096 May 17 06:19 ..
-rw-r--r--  1 ubuntu ubuntu 29226 May 14 14:03 IDEA_BRIEF.md
drwxr-xr-x  3 ubuntu ubuntu  4096 May 17 06:06 paper
drwxr-xr-x  3 ubuntu ubuntu  4096 May 15 05:24 results

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool result

_source line 376 · 2026-05-17T06:21:06.177644+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 152
}
```

</details>

---


### Tool result

_source line 377 · 2026-05-17T06:21:09.149074+00:00_

Perfect! I found the files. Here's a summary of all .tex and .bib files in the paper directory:

## .tex Files Found:
1. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex
2. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex
3. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex
4. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex
5. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex
6. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex
7. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex
8. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex
9. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex
10. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex

## .bib Files Found:
1. /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib

**Total: 10 .tex files and 1 .bib file**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Agent",
  "elapsed_ms": 6842
}
```

</details>

---


### Tool call

_source line 378 · 2026-05-17T06:21:14.275199+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 379 · 2026-05-17T06:21:14.576832+00:00_

1	% How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
2	% Target: EMNLP 2026 (ARR May cycle)
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{amsmath}
10	\usepackage{amssymb}
11	\usepackage{multirow}
12	\usepackage{xcolor}
13	\usepackage{subcaption}
14	\usepackage[T1]{fontenc}
15	\usepackage[utf8]{inputenc}
16	\usepackage{microtype}
17	\usepackage{amsthm}
18	
19	\theoremstyle{definition}
20	\newtheorem{definition}{Definition}
21	
22	\title{How Deep Is Your Data? Estimating Recursive Generation Depth\\via Statistical Fingerprints}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\input{abstract}
30	
31	\input{introduction}
32	
33	\input{related_work}
34	
35	\input{method}
36	
37	\input{atlas}
38	
39	\input{generalization}
40	
41	\input{discussion}
42	
43	\input{conclusion}
44	
45	\bibliography{references}
46	
47	\appendix
48	\input{section_appendix}
49	
50	\end{document}
51	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 380 · 2026-05-17T06:21:14.577237+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 381 · 2026-05-17T06:21:15.029669+00:00_

1	\begin{abstract}
2	As large language models increasingly train on web text containing their own outputs, a recursive model$\to$data$\to$model loop arises---yet no method estimates how many such iterations a text has undergone.
3	We formalize \emph{recursive generation depth estimation} as ordinal classification and construct a benchmark of 180K passages spanning 3 model families, 3 decoding strategies, and 4 generation depths.
4	From each passage we extract a compact statistical fingerprint---19 candidate features dominated by perplexity tail statistics---computed against a fixed reference model.
5	A Random Forest classifier achieves 70--85\% four-class accuracy (chance = 25\%), with perplexity tail statistics emerging as consistent depth markers across all studied configurations.
6	Our \emph{Depth Degradation Atlas} reveals that decoding strategy reshapes degradation trajectories rather than merely attenuating them, and we define the \emph{Effective Discriminable Depth} (EDD) metric, finding $\mathrm{EDD}_{0.75}{=}4$ for the best-characterized model family (Pythia, $p{=}0.001$; consistent direction across all three families with graded statistical support; \S4.4).
7	Cross-model transfer reaches 66.4\% (d1--d3 balanced accuracy: 55.4\%, $1.7\times$ chance); bidirectional cross-model recursive chains achieve equivalent accuracy under forward (84.75\%) and reverse (85.75\%) orderings, providing evidence for a process-level depth signal.
8	Preliminary cross-scale observations on two 7B-scale generators yield 70.2\% accuracy ($\mathrm{EDD}{=}4$) and 60.1\%; a base-model control reveals that instruction-tuning regularizes AUC decay (monotonic vs.\ non-monotonic), with weaker overall depth signal in the base variant (59.9\% vs.\ 70.2\%).
9	Applied to WikiText-103 and C4 web-crawl text, the classifiers maintain high d0 accuracy on editorial text while revealing model-dependent false positive rates on heterogeneous web content.
10	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 382 · 2026-05-17T06:21:15.030198+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 383 · 2026-05-17T06:21:15.532359+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	The text on which large language models are trained increasingly contains their own outputs.
5	As synthetic content proliferates across the web, a recursive loop emerges: models trained on web corpora ingest text generated by earlier models, and their outputs feed into the next generation's training data \cite{shumailov2024_nature,alemohammad2024_mad}.
6	This model$\to$data$\to$model cycle is no longer hypothetical---it is already occurring in the wild---yet we lack the ability to determine how many recursive iterations a given text has undergone, a distinction that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \cite{dohmatob2024_tale_of_tails}.
7	
8	Existing tools address adjacent but distinct problems.
9	Binary detectors such as Binoculars \cite{binoculars2024}, Fast-DetectGPT \cite{fast_detectgpt2024}, and DivEye \cite{diveye2026} classify text as human-written or machine-generated, collapsing all depths $d \geq 1$ into a single category.
10	Watermarking \cite{kirchenbauer2023_watermark} requires proactive embedding and cannot be applied retroactively.
11	The model collapse literature \cite{shumailov2024_nature,dohmatob2024_tale_of_tails} assumes depth is known a priori; \citet{drayson2025_detection_prevents_collapse} filter synthetic data via binary detection without distinguishing depths.
12	No existing method estimates the ordinal recursive generation depth of a text passage from its content alone.
13	
14	Our key insight is that recursive generation leaves quantifiable statistical fingerprints in text, and these fingerprints are \textbf{universal and scale-variant} across the three model families and three decoding strategies studied.
15	Specifically, perplexity tail statistics---the 90th-percentile perplexity (\textsc{p90\_ppl}) and surprisal variance (\textsc{var\_surpris
…[truncated 2350 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 384 · 2026-05-17T06:21:15.532732+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 385 · 2026-05-17T06:21:15.984704+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Definition}
5	\label{sec:method:problem}
6	
7	Let $f_\theta$ denote a language model and $\mathcal{D}_0$ a corpus of human-written seed text.
8	We define a \emph{recursive generation chain} of depth $K$ as the sequence $\mathcal{D}_0, \mathcal{D}_1, \dots, \mathcal{D}_K$, where each $\mathcal{D}_k$ ($k \geq 1$) is produced by finetuning $f_\theta$ on $\mathcal{D}_{k-1}$ and sampling from the resulting model.
9	Depth $d{=}0$ denotes human-written text; depth $d{=}k$ ($k \geq 1$) denotes text generated by a model trained on depth-$(k{-}1)$ data.
10	
11	Given a text passage $x$, the task is to estimate its recursive generation depth $d \in \{0, 1, \dots, K\}$.
12	This is an ordinal classification problem: depths carry a natural ordering, and $d{=}1$ is structurally closer to $d{=}0$ than $d{=}3$ is, since each generation step compounds distributional drift.
13	
14	\subsection{Multi-Generational Benchmark Construction}
15	\label{sec:method:benchmark}
16	
17	We construct a benchmark spanning three axes: model family, decoding strategy, and generation depth.
18	
19	\paragraph{Model families.}
20	We select three 1--1.5B-parameter models with diverse pretraining corpora and architectures: Pythia-1.4B (EleutherAI), OLMo-1B (AI2), and GPT-2~XL (OpenAI, 1.5B).
21	Restricting to a narrow parameter range isolates the effect of architecture and training data from scale.
22	
23	\paragraph{Decoding strategies.}
24	Each model is paired with three decoding strategies: nucleus sampling ($p{=}0.95$) \cite{holtzman2020_nucleus}, temperature sampling ($\tau{=}0.9$), and top-$k$ sampling ($k{=}50$).
25	These span the dominant modes of open-ended generation and induce qualitatively different entropy profiles.
26	Our findings on feature importance and discriminability are limited to this grid; transfer to untested models, scales, or strategies is not established.
27	
28	\paragraph{Depth and scale.}
29	The primary benchmark cov
…[truncated 6565 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 386 · 2026-05-17T06:21:16.035354+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
  }
}
```

</details>

---


### Tool result

_source line 387 · 2026-05-17T06:21:16.537741+00:00_

1	\section{The Depth Degradation Atlas}
2	\label{sec:atlas}
3	
4	We present the Depth Degradation Atlas: a systematic empirical map of how statistical fingerprints evolve across recursive generation depths, models, and decoding strategies.
5	The atlas spans $3 \times 3 = 9$ model--strategy cells evaluated at depths $d \in \{0, 1, 2, 3\}$, with depth extensions to $d{=}5$ for cross-model EDD validation (\S\ref{sec:atlas:edd}).
6	
7	%% ----------------------------------------------------------------
8	\subsection{In-Distribution Performance}
9	\label{sec:atlas:id}
10	
11	Table~\ref{tab:main_matrix} reports four-class Random Forest accuracy (5-fold CV, 200 trees) across all nine cells.
12	Accuracy ranges from 69.6\% (Pythia, top-$k$) to 85.4\% (GPT-2~XL, temperature), all exceeding the 25\% chance baseline by a wide margin.
13	Two axis effects emerge.
14	GPT-2~XL achieves the highest accuracy under every strategy (76.6--85.4\%), followed by OLMo (74.2--82.0\%) and Pythia (69.6--78.2\%).
15	Top-$k$ sampling yields the lowest accuracy in every model.
16	The mean within-model strategy gap is 8.4~pp, comparable to the 7.1~pp mean within-strategy model gap---decoding strategy and model family contribute roughly equally to performance variance.
17	
18	\begin{table}[t]
19	\centering
20	\small
21	\caption{Four-class RF accuracy (\%) across the $3 \times 3$ atlas, with d1--d3 three-class accuracy in parentheses (chance = 25\% / 33\%). Depth-0 recall exceeds 98\% in all cells.}
22	\label{tab:main_matrix}
23	\begin{tabular}{@{}lccc@{}}
24	\toprule
25	& Nucleus & Temp.\ $\tau{=}0.9$ & Top-$k$ \\
26	\midrule
27	Pythia-1.4B  & 78.2\,(71.2) & 76.3\,(70.6) & 69.6\,(58.8) \\
28	OLMo-1B     & 78.8\,(75.0) & 82.0\,(76.3) & 74.2\,(66.1) \\
29	GPT-2~XL    & 83.3\,(79.0) & 85.4\,(82.6) & 76.6\,(69.5) \\
30	\bottomrule
31	\end{tabular}
32	\end{table}
33	
34	\paragraph{Per-class recall distribution.}
35	Depth-0 recall exceeds 98\% in all 9 cells, confirming that human-written text is triviall
…[truncated 11973 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 388 · 2026-05-17T06:21:16.538465+00:00_

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
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool result

_source line 389 · 2026-05-17T06:21:26.481532+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

Based on the search results, here are the key details about ACL ARR 2025-2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scoring (Starting February 2025)

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must b
…[truncated 1418 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 9943
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-17T06:21:35.216224+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
  }
}
```

</details>

---


### Tool result

_source line 391 · 2026-05-17T06:21:35.668663+00:00_

1	\section{Generalization and Robustness}
2	\label{sec:generalization}
3	
4	We test whether the atlas results (69.6--85.4\%) reflect genuine statistical regularities or training artifacts, evaluating generalization along seven axes: four in detail below---classifier choice (\S\ref{sec:gen:baselines}), cross-model transfer (\S\ref{sec:gen:crossmodel}), cross-strategy transfer (\S\ref{sec:gen:crossstrategy}), and preliminary cross-scale observations (\S\ref{sec:gen:crossscale})---and three in the Appendix (end-to-end learning, temperature robustness, and cross-boundary transfer).
5	
6	\subsection{Classifier Comparison and Surface-Text Ablation}
7	\label{sec:gen:baselines}
8	
9	Table~\ref{tab:baselines} evaluates three classifier families---bagging (RF), gradient boosting (XGBoost, LightGBM)---on the same 19 features across three atlas cells spanning the full accuracy range.
10	Per-cell spread is $\leq$0.4pp, establishing a feature-determined ceiling independent of the learning algorithm.
11	On Pythia nucleus, CORAL ordinal regression \cite{coral2020} (78.1\%) and DivEye \cite{diveye2026} (78.2\%) match the within-cell RF of Table~\ref{tab:main_matrix} within 0.1\,pp (bootstrap $p>0.05$, Bonferroni-corrected); all feature-based methods significantly outperform CE-MLP (74.9\%, $p<0.001$) and logistic regression (75.0\%).
12	
13	\paragraph{Surface-text ablation.}
14	Single-feature regression on mean perplexity performs at chance (25.1\%); two zero-shot LLMs---DeepSeek V3.2 (36.2\%) and Qwen2.5-7B-Instruct (30.4\%; each 500 samples, prompt in Appendix~\ref{app:zeroshot_prompt})---also fail, confirming that the depth signal resides in distributional statistics inaccessible from surface text alone (42\,pp gap vs.\ RF at 78.2\%).
15	
16	\begin{table}[t]
17	\centering
18	\small
19	\caption{Classifier convergence: 4-class accuracy (\%) across three atlas cells. RF (bagging), XGBoost and LightGBM (gradient boosting) operate on the same 19 features; $\Delta_{\max}$: largest per-
…[truncated 6072 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 392 · 2026-05-17T06:21:35.719353+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 393 · 2026-05-17T06:21:35.719759+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Model Collapse Theory.}
5	\citet{shumailov2024_nature} demonstrate that recursive training on model outputs erodes distributional tails; \citet{dohmatob2024_tale_of_tails} formalize this via scaling laws, \citet{dohmatob2025_strong_collapse} establish strong collapse guarantees, and the MAD framework \cite{alemohammad2024_mad} extends the analysis to self-consuming models.
6	Subsequent work addresses mitigation \cite{gerstgrasser2024_accumulate,drayson2025_detection_prevents_collapse,yi2026_escaping_collapse,falahati2026_curated}, non-monotonic dynamics \cite{bakshi2026_collapse_improvement}, convergence \cite{marchi2024_heat_death,wang2026_contamination}, and related phenomena \cite{knowledge_collapse2025,sigma2026_spectral,synthetic_eggs2026,dohmatob2024_demystified}.
7	These works characterize degradation but assume depth is known a priori; we address the inverse problem of estimating depth from text alone.
8	
9	\paragraph{AI Text Detection.}
10	The detection literature \cite{wu2025_detection_survey} spans statistical methods---DetectGPT \cite{mitchell2023_detectgpt}, Fast-DetectGPT \cite{fast_detectgpt2024}, Binoculars \cite{binoculars2024}, DivEye \cite{diveye2026}, GLTR \cite{gehrmann2019_gltr}, Ghostbuster \cite{verma2024_ghostbuster}, DNA-GPT \cite{yang2024_dnagpt}---and watermarking \cite{kirchenbauer2023_watermark}, with known limits from paraphrasing \cite{sadasivan2023_paraphrase}, distribution shift \cite{pudasaini2026_detection_fails}, and generator barriers \cite{pu2026_generator_barrier}.
11	M4-SemEval \cite{wang2024_m4_semeval} benchmarks multilingual detection.
12	All these methods perform binary classification, discarding ordinal depth information; our approach outputs ordinal depth labels, complementing rather than replacing binary detection.
13	
14	\paragraph{Adjacent Tasks.}
15	EditLens \cite{editlens2026} estimates editing extent but does not model recursive chains; \citet{uchendu2
…[truncated 1412 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 394 · 2026-05-17T06:21:36.171923+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 395 · 2026-05-17T06:21:37.125856+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	We formalized recursive generation depth estimation and showed that a compact feature set dominated by perplexity tail statistics achieves 70--85\% four-class accuracy ($\mathrm{EDD}_{0.75}{=}4$; \S\ref{sec:atlas:edd}), with five features sufficing for 97.6\% of full performance and classifier-agnostic convergence within $\leq$0.4pp.
5	The dominant feature group---perplexity tail statistics (\texttt{p90\_ppl} top-2 in 9/9 cells, \texttt{var\_surprisal} in 8/9)---generalizes across all three model families without retraining, making depth estimation a candidate early-warning signal for model collapse~\cite{shumailov2024_nature,shi2025_closer_look}; a surface-text ablation (zero-shot LLMs at 30--36\%, 42\,pp below RF; \S\ref{sec:gen:baselines}) confirms the signal resides in distributional statistics inaccessible from surface text alone.
6	Cross-strategy transfer remains the primary bottleneck (59.1\% vs.\ 66.4\% cross-model; Appendix~\ref{app:multi_tau}), confirming strategy-conditioned classifiers are necessary.
7	Depth estimation enables depth-graduated data curation---retaining d1 while filtering d3+---complementing binary detection~\cite{dsir2023,qurating2024} (Appendix~\ref{app:curation_poc}) and watermarking~\cite{kirchenbauer2023_watermark} as a provenance signal~\cite{bevendorff2025_two_paradigms}; extensions to adversarial robustness and larger generators remain open (Appendix~\ref{app:cross_scale_full}).
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 396 · 2026-05-17T06:21:37.126214+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 397 · 2026-05-17T06:21:37.628558+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Cross-strategy deployment constraint.}
5	Cross-strategy transfer induces a d1/d2 boundary inversion under temperature sampling.
6	Per-strategy z-score normalization partially corrects the inversion under logistic regression (GPT-2~XL d1v2 AUC $0.24{\to}0.56$, OLMo $0.19{\to}0.70$) but yields negligible improvement for the Random Forest classifier used throughout the main experiments ($\Delta < 0.02$\,pp), and even in the best case (logistic regression) leaves a residual gap relative to within-strategy performance (${\sim}0.83$), indicating that a two-stage pipeline (strategy identification + strategy-conditioned classification) is needed for reliable cross-strategy deployment.
7	
8	\paragraph{d0 inflation of headline metrics.}
9	Depth~0 (human-written text) is near-perfectly separable (recall $>$98\% across all nine model--strategy settings), inflating headline accuracy.
10	Cross-model transfer accuracy of 66.4\% is substantially driven by d0; d2 recall drops to 26.8\% in the worst case (Pythia holdout).
11	
12	\paragraph{Controlled vs.\ ecological setting.}
13	The primary benchmark uses Wikipedia seed text with controlled recursive generation (LoRA fine-tuning, 1--1.5B parameter models); cross-scale experiments extend to 7--8B instruction-tuned models (\S\ref{sec:gen:crossscale}).
14	This protocol isolates the recursive depth variable but diverges from wild recursive contamination, where models are pretrained on mixed corpora containing prior-generation outputs at unknown proportions; the fingerprints we identify may attenuate or shift under such diffuse exposure.
15	Depth signal is the dominant classification factor (5-fold CV 59--82\%, up to 2.5$\times$ chance): LOGO accuracy (72.1\%) matches standard CV (72.0\%), and seed-group prediction is at chance (10.2\% vs.\ 10\%; Appendix~\ref{app:domain_bias}).
16	Cross-scale experiments include both instruction-tuned and base variants; the base model sho
…[truncated 5119 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 398 · 2026-05-17T06:21:37.628990+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 399 · 2026-05-17T06:21:38.081195+00:00_

1	\section{Additional Results}
2	\label{app:additional}
3	
4	\subsection{Top-$k$ Feature Trajectories}
5	\label{app:topk_trajectories}
6	
7	Figure~\ref{fig:feature_trajectory} in the main text shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\tau{=}0.9$) sampling.
8	Top-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \S\ref{sec:atlas:strategy}.
9	Concretely, the d0$\to$d1 drop in \textsc{p90\_ppl} under top-$k$ is 78\% (vs.\ 87\% for nucleus), and the d2$\to$d3 reduction is 31\% (vs.\ 39\% for nucleus).
10	Despite the magnitude reduction, feature rank ordering across depths is preserved, which explains why ordinal classifiers maintain directionality even under top-$k$ conditions.
11	
12	\subsection{Permutation Importance}
13	\label{app:permutation}
14	
15	To verify that the Gini-based importance rankings in \S\ref{sec:atlas:features} are not an artifact of the impurity measure, we compute permutation importance (5-fold CV, 10 repeats) for all 9 atlas cells.
16	The top-2 features are stable across measures: \textsc{p90\_ppl} ranks in the top 2 in 9/9 cells under both Gini and permutation importance, and \textsc{var\_surprisal} in 8/9 (vs.\ 7/9 for Gini, with the additional cell being OLMo top-$k$; the single SHAP exception is GPT-2~XL top-$k$, where \textsc{p75\_ppl} displaces \textsc{var\_surprisal} to rank 3).
17	Kendall's $W{=}0.90$ across all three methods (Gini, permutation, SHAP) indicates strong concordance ($p{<}0.005$).
18	Pairwise Spearman correlations are: SHAP--Gini $\rho{=}0.93$, SHAP--permutation $\rho{=}0.84$, Gini--permutation $\rho{=}0.76$.
19	Per-cell top-5 overlap between SHAP and permutation importance is 3--4 out of 5 features; the aggregated (mean-across-cells) top-5 sets are identical, confirming that the top features are robust to the choice of importance measure at the aggregate l
…[truncated 34218 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 400 · 2026-05-17T06:21:38.081535+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review review form soundness excitement scoring scale 1-5 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review review form soundness excitement scoring scale 1-5 2025"
  }
}
```

</details>

---


### Tool result

_source line 401 · 2026-05-17T06:21:45.653505+00:00_

Web search results for query: "ACL Rolling Review review form soundness excitement scoring scale 1-5 2025"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/acguidelines.md at main · yoshitomo-matsubara/aclrollingreview","url":"https://github.com/yoshitomo-matsubara/aclrollingreview/blob/main/acguidelines.md"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL 2026 on X: \"Checkout the blog post on the soundness/excitement scores https://t.co/AKSO9DjiYP . It clarifies the reasoning behind the separation of overall scores and how it might make the reviewer recommendation more robust. #ACL2023Toronto #ACL2023NLP #NLProc\" / X","url":"https://x.com/aclmeeting/status/1637827267173953540"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"🎪 ACL 2025 Reviews Are Out: To Rebut or Flee? The Harsh Reality of NLP’s \"Publish or Perish\" Circus | CSPaper Forum","url":"https://forum.cspaper.org/topic/27/acl-2025-reviews-are-out-to-rebut-or-flee-the
…[truncated 1694 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7571
}
```

</details>

---


### Tool call

_source line 402 · 2026-05-17T06:23:22.474986+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 403 · 2026-05-17T06:23:23.178806+00:00_

1	% ============================================================
2	% Model Collapse Theory
3	% ============================================================
4	
5	@article{shumailov2024_nature,
6	  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
7	  title     = {{AI models collapse when trained on recursively generated data}},
8	  journal   = {Nature},
9	  volume    = {631},
10	  pages     = {755--759},
11	  year      = {2024},
12	  doi       = {10.1038/s41586-024-07566-y},
13	}
14	
15	@inproceedings{dohmatob2024_tale_of_tails,
16	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia},
17	  title     = {{A Tale of Tails: Model Collapse as a Change of Scaling Laws}},
18	  booktitle = {Proceedings of ICML},
19	  year      = {2024},
20	  note      = {arXiv:2402.07043},
21	  url       = {https://arxiv.org/abs/2402.07043},
22	}
23	
24	@inproceedings{dohmatob2025_strong_collapse,
25	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
26	  title     = {{Strong Model Collapse}},
27	  booktitle = {Proceedings of ICLR},
28	  year      = {2025},
29	  note      = {arXiv:2410.04840},
30	  url       = {https://arxiv.org/abs/2410.04840},
31	}
32	
33	@inproceedings{dohmatob2024_demystified,
34	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia},
35	  title     = {{Model Collapse Demystified: The Case of Regression}},
36	  booktitle = {Proceedings of NeurIPS},
37	  year      = {2024},
38	  note      = {arXiv:2402.07712},
39	  url       = {https://arxiv.org/abs/2402.07712},
40	}
41	
42	@inproceedings{alemohammad2024_mad,
43	  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Hossain, Hossein and Romero, Oscar and Ramanarayanan, Sriram and Baraniuk, Richard G.},
44	  title     = {{Self-Consuming Generative Models Go MAD}},
45	  booktitle = {Proceedings of I
…[truncated 19537 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 404 · 2026-05-17T06:23:23.179241+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARR review form 2025 soundness score rubric \"5\" \"4\" \"3\" \"2\" \"1\" definition criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ARR review form 2025 soundness score rubric \"5\" \"4\" \"3\" \"2\" \"1\" definition criteria"
  }
}
```

</details>

---


### Tool result

_source line 405 · 2026-05-17T06:23:29.954496+00:00_

Web search results for query: "ARR review form 2025 soundness score rubric "5" "4" "3" "2" "1" definition criteria"

Links: [{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"Program Chairs’ Report on Peer Review at ACL 2023 Anna Rogers}","url":"https://aclanthology.org/2023.acl-long.report.pdf"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Surviving ARR May Meta-Review & Deciding on EMNLP 2025: A Tactical and Honest Guide | CSPaper Forum","url":"https://forum.cspaper.org/topic/113/surviving-arr-may-meta-review-deciding-on-emnlp-2025-a-tactical-and-honest-guide"},{"title":"ACL’23 Peer Review Policies - ACL 2023","url":"https://2023.aclweb.org/blog/review-acl23/"},{"title":"ACL ARR 2025 July | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2025%2FJuly"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"}]

Based on the search results, I found the ARR soundness score rubric definitions. Here are the specific criteria for each score level:

## ARR 2025 Soundness Score Rubric

**5 = Excellent:** "This study is one of the most thorough I have seen, given its type."

**4 = Strong:** "This study provides sufficient support for all of its claims. Some extra experiments could be nice, but not essential."

**3 = Acceptable:** "This study provides sufficient supp
…[truncated 792 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6775
}
```

</details>

---


### Tool call

_source line 406 · 2026-05-17T06:26:10.321000+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 8 审稿报告 — Reviewer 1（方法严谨性 + 实验有效性）\n\n**论文**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n**Venue**: EMNLP 2026 Findings (ARR May 2026 cycle)\n\n---\n\n## 总体评分\n\n**Overall Recommendation**: 3.0 (Resubmit next cycle — needs targeted revisions achievable in one cycle)\n**一句话总结**: 核心方法新颖且实验覆盖面宽，但主表格缺统计不确定性度量、EDD 跨模型统计支撑不均、以及 accumulation/quality-control 实验缺失等问题需在 camera-ready 前解决。\n\n---\n\n## 官方维度打分（ACL ARR Review Form, Feb 2025+）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 (Acceptable) | 主 claims 有支撑但 key tables 缺 CI/significance；EDD=4 的跨模型泛化声明统计基础不均（1/3 显著） |\n| Excitement | 3.5/5 | 问题定义新颖（ordinal depth estimation 是真空白），atlas 设计系统性好，但实用性论证（curation PoC p=0.407）偏弱 |\n| Reproducibility | 4/5 | Pipeline 描述清晰（LoRA hyperparams, feature extraction, CV splits），承诺代码公开；cross-seed replication 加分 |\n| Clarity | 4/5 | 结构清晰，limitations 诚实透明；abstract 偏长且数字密集 |\n\n---\n\n## 历史遗留 Issue 逐条验证\n\n### ✅ RESOLVED\n\n**R1-W2** (d0 inflation): Table 2 现在括号内报告 d1-d3 三类 accuracy（chance=33%），Limitations 段明确讨论 d0 inflation，Abstract 也报告 \"d1-d3 balanced accuracy: 55.4%, 1.7× chance\"。\n\n**R5-W1** (Single LoRA non-independence): Appendix §A.10 提供 cross-seed replication（seed=43, Δ=-1.05pp, 95% CI [76.4, 78.15]）和 cross-seed transfer（76.76%），top-5 feature importance 跨 seed 一致。充分证明 depth signal 不是特定 LoRA 权重的 artifact。\n\n### ⚠️ PARTIALLY ADDRESSED\n\n**R1-N2** (Tables 缺 std/CI/significance):\n- Figure 4 有 bootstrap 95% CI shaded bands ✓\n- Cross-scale Table (Appendix §A.7) 有 95% CI brackets ✓\n- Cross-seed Table (Appendix §A.10) 有 95% CI ✓\n- **但 Table 2（核心 9-cell matrix）和 Table 5（classifier comparison）仍无任何 variance 指标**。Table 5 有 Δ_max 列（≤0.4pp）替代，但这不等于正式的 CI 或 std。5-fold CV 天然产生 fold-level variance，不报告是遗憾。\n- 状态：主文核心表格仍缺，附录/图中有。建议至少在 Table 2 加 ±std 或 95% CI。\n\n**R4-N1** (EDD₀.₇₅=4 统计限定):\n- Abstract 现在写 \"for the best-characterized model family (Pythia, p=0.001; consistent direction across all three families with graded statistical support; §4.4)\" ✓ 范围已限定到 Pythia\n- §4.4 正文完整报告三个 p-values：Pythia 0.001, OLMo 0.091, GPT-2 XL 0.505 ✓\n- 问题：Abstract 中 \"consistent direction... with graded statistical support\" 仍是 euphemism——GPT-2 XL p=0.505 意味着其 AUC 点估计 0.750 完全无法排除随机波动（H₀: AUC≤0.75 无法拒绝）。\"Graded statistical support\" 在统计学中无标准含义，可能误导读者以为三个模型都显示了有意义的证据。建议改为 \"Pythia significant (p=0.001), OLMo marginal (p=0.091), GPT-2 XL non-significant\" 的精确表述，或至少在 abstract 内明示仅 Pythia 具备充分统计支撑。\n\n**R5-N2** (Reference model 循环依赖):\n- Limitations 段充分讨论了 self-model 测量问题 ✓\n- OLMo-1B 作为 alternative reference 的 ablation（Δ=4.0pp）存在 ✓\n- 明确指出 \"architecturally distinct references (e.g., encoder-only or larger-scale models) remains open\" ✓\n- 但建议的 architecturally distinct reference ablation 未执行。考虑到两个 reference 都是 ~1B autoregressive models，无法排除这一架构族系的 bias。\n\n**R5-W5** (EDD classifier-dependence):\n- §5.1 Table 5 展示 RF/XGBoost/LightGBM 在同一特征上的 convergence（Δ≤0.4pp）✓ 间接表明 EDD 对 classifier 不敏感\n- 但 EDD 定义（Definition 1）仍未显式声明 \"EDD is an operational measure conditioned on the specified classifier and feature set\"。当前写法可能让读者误以为 EDD 是 text 的 intrinsic property。建议在 Definition 1 后加一句 methodological caveat。\n\n### ❌ NOT ADDRESSED\n\n**R5-W4** (Related Work 引用遗漏):\n- **McCullagh 1980** (proportional odds model): ordinal classification 的奠基论文，当前 §2 \"Ordinal Classification\" 段只引 CORAL (2020) 和 CLOC (2025)，缺少经典基础。\n- **Rennie & Srebro 2005** (loss design for ordinal regression): 同上。\n- **CCNet / Wenzek et al. 2020**: 未引。CCNet 是 Common Crawl 数据清洗 pipeline，与本文讨论的 web-crawl calibration（C4）高度相关。\n- **Schaeffer et al. 2025**: 直接挑战 benchmark ecological validity 的论文未引（注意 Gerstgrasser et al. 2024 中 Schaeffer 是共同作者，但那是不同论文）。\n- 状态：references.bib 中无上述四项。建议至少补充 McCullagh 和 Schaeffer。\n\n**R1-W3** (LoRA rank sensitivity analysis):\n- 论文始终使用 r=16, α=32。Cross-seed replication（§A.10）使用相同 rank。\n- 未报告 rank ∈ {4, 16, 64} 的 sensitivity analysis。\n- 这是重要的方法学缺失：如果 depth signal 因 rank 改变而显著变化，则当前结论的适用范围受限。至少需要一组 rank ablation 数据。\n\n**R7-W3** (Partial mixing/accumulation 场景):\n- Limitations 提到 \"wild recursive contamination, where models are pretrained on mixed corpora containing prior-generation outputs at unknown proportions\" 并承认 \"fingerprints we identify may attenuate or shift under such diffuse exposure\"。\n- Appendix §A.9 (Mixed-Depth Corpus) 测试的是 evaluation set 中 class 比例变化对分类器的影响（macro-recall Δ=-1.62pp），**不是**训练数据本身为混合深度的情况。\n- 真正的 accumulation 场景（如 Gerstgrasser et al. 2024 的 accumulate 设定：训练集 = 70% d0 + 30% d1，从此混合数据 finetune 后生成）完全未测试。这是 ecological validity 的核心缺口。\n\n**R7-W4** (Depth estimation vs. text quality estimation):\n- 无 matched-quality control 实验。论文未测试：在控制 text quality（如 perplexity level、coherence score）的条件下，depth 是否仍可区分。\n- 间接证据存在：τ=1.1 时 signal 消失说明不纯粹是 quality；cross-model chains 排除了单一模型的 quality gradient。但缺少直接的 confound-control 实验。\n- 这是一个 conceptual concern：如果 depth 与 quality 强相关且无法解耦，则 \"depth estimation\" 可能只是 \"quality estimation\" 的重包装。\n\n---\n\n## 新发现问题\n\n### Must-Fix（影响接收决定）\n\n**N1** [critical] Abstract 数值精度问题\n- 位置：Abstract line 1-2, §1\n- 问题：Abstract 写 \"70--85% four-class accuracy\"，但 Table 2 实际范围为 69.6%--85.4%。下界 69.6% 被向上取整至 70%。虽然差异仅 0.4pp，但在 blind review 中审稿人可能质疑数据 cherry-picking。\n- 建议：改为 \"approximately 70--85%\" 或 \"69.6--85.4%\"。\n\n**N2** [critical] Curation PoC 与 narrative 不一致\n- 位置：§6 Discussion, Appendix §A.6\n- 问题：Discussion 将 depth-graduated curation 作为核心 motivation 之一，但 Appendix Table 9 显示 RF-filtered vs. unfiltered 无统计显著差异（p=0.407, 0.492, 0.607）。仅 RF vs. random subsampling 显著（p<0.001--0.02）。这意味着 depth-aware filtering 相比 simply keeping all data 无可证明的益处——只是优于随机丢弃数据。\n- 为什么影响接收：核心 application narrative（\"enables depth-graduated data curation\"）缺乏实验支撑。如果 curation 是 motivation 之一，inconclusive 结果需要在主文而非仅附录中诚实呈现。\n- 建议：(1) 在 Discussion 中明确说明 curation PoC 目前 inconclusive，或 (2) 降低 narrative 中对 curation 的强调，将其定位为 future work 而非 established benefit。\n\n### Should-Fix（影响评分）\n\n**W1** [warning] EDD 在 GPT-2 XL 上的 boundary case\n- 位置：§4.4, Abstract\n- 问题：GPT-2 XL d3-vs-d4 AUC = 0.750，恰好等于 threshold T=0.75。定义上 EDD≥4（因为 ≥），但 bootstrap test p=0.505 说明这个点估计完全无法区分于 random fluctuation。论文将此纳入 \"consistent direction\" 表述中，但数学上 AUC=0.750 at T=0.75 with p=0.505 是一个 null result。\n- 建议：在 §4.4 中明确指出 GPT-2 XL 的 EDD=4 结论在统计上是 trivial 的（AUC 恰好等于阈值且无显著性），避免读者误解三个模型都 robustly 支持 EDD=4。\n\n**W2** [warning] Cross-strategy transfer failure 与 \"universal fingerprint\" narrative 的张力\n- 位置：§5.3, §1（Introduction \"universal and scale-variant\"）\n- 问题：Introduction 声称 fingerprints 是 \"universal and scale-variant\"，但 cross-strategy transfer（§5.3）仅 59.1% mean accuracy，d1-d3 仅 45.9%（chance=33%，1.38×），temperature holdout d1v2 AUC 可低至 0.129（GPT-2 XL）。这不是 \"universal\" 的表现——strategy-conditioned classifiers 是必需的。\n- 建议：将 Introduction 的 \"universal\" 修饰为 \"universal within-strategy\" 或限定 universality 的范围。当前措辞对读者产生过度乐观的印象。\n\n**W3** [warning] 95% CI 未报告在 primary result tables\n- 位置：Table 2, Table 5\n- 问题：5-fold CV 本身产生 5 个 fold-level accuracy，可直接报告 mean±std。Table 2 和 Table 5 是论文最核心的 result tables，却是唯二没有 variance measure 的主要表格。Figure 4 有 bootstrap CI，cross-scale table 有 95% CI——说明作者有计算能力但选择性地省略了。\n- 建议：Table 2 加 ±std 列（或 95% CI），Table 5 的 Δ_max 列改为标准 std 报告。\n\n### Minor（不影响接收）\n\n- Abstract 过度压缩（~250 words，数字密集），建议删减 cross-model chain 的具体百分比（84.75%/85.75%）以提高可读性。\n- §3.4 EDD 定义的 footnote 1 解释了 non-monotonic 情况，但正文未在 Definition 后 explicitly state \"EDD is defined relative to the classifier and feature set specified above\"。\n- Table 2 caption 说 \"Depth-0 recall exceeds 98% in all cells\" 但 Table 8 (Appendix) 显示 GPT-2 XL top-k 为 98.5%——consistent，只是 \"exceeds 98%\" 与 98.5% 的 margin 很小。\n- §1 \"our key insight is that recursive generation leaves quantifiable statistical fingerprints... universal and scale-variant\"：前半句是 post-hoc conclusion 而非 a priori insight；建议改为 hypothesis-driven 表述。\n\n---\n\n## 主要优势\n\n1. **问题新颖性**：Ordinal depth estimation 确实是文献空白。从 binary detection 到 ordinal classification 的推进有明确的科学价值。\n2. **系统性实验设计**：3×3 atlas 设计优雅，覆盖了 model family 和 decoding strategy 两个维度的交叉效应。\n3. **诚实的 Limitations**：8 段 Limitations 覆盖了大部分可预见的批评，这在 submission 中罕见。Cross-seed replication、domain bias analysis、base-model control 都体现了方法学严谨性。\n4. **特征可解释性**：p90_ppl + var_surprisal 作为 dominant features 的一致性（9/9 + 8/9，三种 importance measures concordance W=0.90）令人信服。\n5. **Ablation 充分性**：feature ablation、classifier convergence、passage length、reference model、cross-seed——覆盖面广。\n\n---\n\n## 总结判断\n\n论文定义了一个有价值的新任务，实验覆盖系统性好，但三个核心方法学问题阻碍接收：(1) 主表格缺 CI 降低了 reproducibility claim 的可信度；(2) EDD=4 的跨模型泛化统计支撑不均匀且 abstract 表述 euphemistic；(3) accumulation 场景和 matched-quality control 两个关键生态效度实验完全缺失。这些问题中 (1)(2) 可在一个 cycle 内修复，(3) 需要额外实验但技术上可行。建议 resubmit next cycle。\n\n**Confidence**: 4/5 (I am confident but not certain about my assessment)",
  "reviewer_id": "1",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 8 审稿报告 — Reviewer 1（方法严谨性 + 实验有效性）\n\n**论文**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n**Venue**: EMNLP 2026 Findings (ARR May 2026 cycle)\n\n---\n\n## 总体评分\n\n**Overall Recommendation**: 3.0 (Resubmit next cycle — needs targeted revisions achievable in one cycle)\n**一句话总结**: 核心方法新颖且实验覆盖面宽，但主表格缺统计不确定性度量、EDD 跨模型统计支撑不均、以及 accumulation/quality-control 实验缺失等问题需在 camera-ready 前解决。\n\n---\n\n## 官方维度打分（ACL ARR Review Form, Feb 2025+）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 (Acceptable) | 主 claims 有支撑但 key tables 缺 CI/significance；EDD=4 的跨模型泛化声明统计基础不均（1/3 显著） |\n| Excitement | 3.5/5 | 问题定义新颖（ordinal depth estimation 是真空白），atlas 设计系统性好，但实用性论证（curation PoC p=0.407）偏弱 |\n| Reproducibility | 4/5 | Pipeline 描述清晰（LoRA hyperparams, feature extraction, CV splits），承诺代码公开；cross-seed replication 加分 |\n| Clarity | 4/5 | 结构清晰，limitations 诚实透明；abstract 偏长且数字密集 |\n\n---\n\n## 历史遗留 Issue 逐条验证\n\n### ✅ RESOLVED\n\n**R1-W2** (d0 inflation): Table 2 现在括号内报告 d1-d3 三类 accuracy（chance=33%），Limitations 段明确讨论 d0 inflation，Abstract 也报告 \"d1-d3 balanced accuracy: 55.4%, 1.7× chance\"。\n\n**R5-W1** (Single LoRA non-independence): Appendix §A.10 提供 cross-seed replication（seed=43, Δ=-1.05pp, 95% CI [76.4, 78.15]）和 cross-seed transfer（76.76%），top-5 feature importance 跨 seed 一致。充分证明 depth signal 不是特定 LoRA 权重的 artifact。\n\n### ⚠️ PARTIALLY ADDRESSED\n\n**R1-N2** (Tables 缺 std/CI/significance):\n- Figure 4 有 bootstrap 95% CI shaded bands ✓\n- Cross-scale Table (Appendix §A.7) 有 95% CI brackets ✓\n- Cross-seed Table (Appendix §A.10) 有 95% CI ✓\n- **但 Table 2（核心 9-cell matrix）和 Table 5（classifier comparison）仍无任何 variance 指标**。Table 5 有 Δ_max 列（≤0.4pp）替代，但这不等于正式的 CI 或 std。5-fold CV 天然产生 fold-level variance，不报告是遗憾。\n- 状态：主文核心表格仍缺，附录/图中有。建议至少在 Table 2 加 ±std 或 95% CI。\n\n**R4-N1** (EDD₀.₇₅=4 统计限定):\n- Abstract 现在写 \"for the best-characterized model family (Pythia, p=0.001; consistent direction across all three families with graded statistical support; §4.4)\" ✓ 范围已限定到 Pythia\n- §4.4 正文完整报告三个 p-values：Pythia 0.001, OLMo 0.091, GPT-2 XL 0.505 ✓\n- 问题：Abstract 中 \"consistent direction... with graded statistical support\" 仍是 euphemism——GPT-2 XL p=0.505 意味着其 AUC 点估计 0.750 完全无法排除随机波动（H₀: AUC≤0.75 无法拒绝）。\"Graded statistical support\" 在统计学中无标准含义，可能误导读者以为三个模型都显示了有意义的证据。建议改为 \"Pythia significant (p=0.001), OLMo marginal (p=0.091), GPT-2 XL non-significant\" 的精确表述，或至少在 abstract 内明示仅 Pythia 具备充分统计支撑。\n\n**R5-N2** (Reference model 循环依赖):\n- Limitations 段充分讨论了 self-model 测量问题 ✓\n- OLMo-1B 作为 alternative reference 的 ablation（Δ=4.0pp）存在 ✓\n- 明确指出 \"architecturally distinct references (e.g., encoder-only or larger-scale models) remains open\" ✓\n- 但建议的 architecturally distinct reference ablation 未执行。考虑到两个 reference 都是 ~1B autoregressive models，无法排除这一架构族系的 bias。\n\n**R5-W5** (EDD classifier-dependence):\n- §5.1 Table 5 展示 RF/XGBoost/LightGBM 在同一特征上的 convergence（Δ≤0.4pp）✓ 间接表明 EDD 对 classifier 不敏感\n- 但 EDD 定义（Definition 1）仍未显式声明 \"EDD is an operational measure conditioned on the specified classifier and feature set\"。当前写法可能让读者误以为 EDD 是 text 的 intrinsic property。建议在 Definition 1 后加一句 methodological caveat。\n\n### ❌ NOT ADDRESSED\n\n**R5-W4** (Related Work 引用遗漏):\n- **McCullagh 1980** (proportional odds model): ordinal classification 的奠基论文，当前 §2 \"Ordinal Classification\" 段只引 CORAL (2020) 和 CLOC (2025)，缺少经典基础。\n- **Rennie & Srebro 2005** (loss design for ordinal regression): 同上。\n- **CCNet / Wenzek et al. 2020**: 未引。CCNet 是 Common Crawl 数据清洗 pipeline，与本文讨论的 web-crawl calibration（C4）高度相关。\n- **Schaeffer et al. 2025**: 直接挑战 benchmark ecological validity 的论文未引（注意 Gerstgrasser et al. 2024 中 Schaeffer 是共同作者，但那是不同论文）。\n- 状态：references.bib 中无上述四项。建议至少补充 McCullagh 和 Schaeffer。\n\n**R1-W3** (LoRA rank sensitivity analysis):\n- 论文始终使用 r=16, α=32。Cross-seed replication（§A.10）使用相同 rank。\n- 未报告 rank ∈ {4, 16, 64} 的 sensitivity analysis。\n- 这是重要的方法学缺失：如果 depth signal 因 rank 改变而显著变化，则当前结论的适用范围受限。至少需要一组 rank ablation 数据。\n\n**R7-W3** (Partial mixing/accumulation 场景):\n- Limitations 提到 \"wild recursive contamination, where models are pretrained on mixed corpora containing prior-generation outputs at unknown proportions\" 并承认 \"fingerprints we identify may attenuate or shift under such diffuse exposure\"。\n- Appendix §A.9 (Mixed-Depth Corpus) 测试的是 evaluation set 中 class 比例变化对分类器的影响（macro-recall Δ=-1.62pp），**不是**训练数据本身为混合深度的情况。\n- 真正的 accumulation 场景（如 Gerstgrasser et al. 2024 的 accumulate 设定：训练集 = 70% d0 + 30% d1，从此混合数据 finetune 后生成）完全未测试。这是 ecological validity 的核心缺口。\n\n**R7-W4** (Depth estimation vs. text quality estimation):\n- 无 matched-quality control 实验。论文未测试：在控制 text quality（如 perplexity level、coherence score）的条件下，depth 是否仍可区分。\n- 间接证据存在：τ=1.1 时 signal 消失说明不纯粹是 quality；cross-model chains 排除了单一模型的 quality gradient。但缺少直接的 confound-control 实验。\n- 这是一个 conceptual concern：如果 depth 与 quality 强相关且无法解耦，则 \"depth estimation\" 可能只是 \"quality estimation\" 的重包装。\n\n---\n\n## 新发现问题\n\n### Must-Fix（影响接收决定）\n\n**N1** [critical] Abstract 数值精度问题\n- 位置：Abstract line 1-2, §1\n- 问题：Abstract 写 \"70--85% four-class accuracy\"，但 Table 2 实际范围为 69.6%--85.4%。下界 69.6% 被向上取整至 70%。虽然差异仅 0.4pp，但在 blind review 中审稿人可能质疑数据 cherry-picking。\n- 建议：改为 \"approximately 70--85%\" 或 \"69.6--85.4%\"。\n\n**N2** [critical] Curation PoC 与 narrative 不一致\n- 位置：§6 Discussion, Appendix §A.6\n- 问题：Discussion 将 depth-graduated curation 作为核心 motivation 之一，但 Appendix Table 9 显示 RF-filtered vs. unfiltered 无统计显著差异（p=0.407, 0.492, 0.607）。仅 RF vs. random subsampling 显著（p<0.001--0.02）。这意味着 depth-aware filtering 相比 simply keeping all data 无可证明的益处——只是优于随机丢弃数据。\n- 为什么影响接收：核心 application narrative（\"enables depth-graduated data curation\"）缺乏实验支撑。如果 curation 是 motivation 之一，inconclusive 结果需要在主文而非仅附录中诚实呈现。\n- 建议：(1) 在 Discussion 中明确说明 curation PoC 目前 inconclusive，或 (2) 降低 narrative 中对 curation 的强调，将其定位为 future work 而非 established benefit。\n\n### Should-Fix（影响评分）\n\n**W1** [warning] EDD 在 GPT-2 XL 上的 boundary case\n- 位置：§4.4, Abstract\n- 问题：GPT-2 XL d3-vs-d4 AUC = 0.750，恰好等于 threshold T=0.75。定义上 EDD≥4（因为 ≥），但 bootstrap test p=0.505 说明这个点估计完全无法区分于 random fluctuation。论文将此纳入 \"consistent direction\" 表述中，但数学上 AUC=0.750 at T=0.75 with p=0.505 是一个 null result。\n- 建议：在 §4.4 中明确指出 GPT-2 XL 的 EDD=4 结论在统计上是 trivial 的（AUC 恰好等于阈值且无显著性），避免读者误解三个模型都 robustly 支持 EDD=4。\n\n**W2** [warning] Cross-strategy transfer failure 与 \"universal fingerprint\" narrative 的张力\n- 位置：§5.3, §1（Introduction \"universal and scale-variant\"）\n- 问题：Introduction 声称 fingerprints 是 \"universal and scale-variant\"，但 cross-strategy transfer（§5.3）仅 59.1% mean accuracy，d1-d3 仅 45.9%（chance=33%，1.38×），temperature holdout d1v2 AUC 可低至 0.129（GPT-2 XL）。这不是 \"universal\" 的表现——strategy-conditioned classifiers 是必需的。\n- 建议：将 Introduction 的 \"universal\" 修饰为 \"universal within-strategy\" 或限定 universality 的范围。当前措辞对读者产生过度乐观的印象。\n\n**W3** [warning] 95% CI 未报告在 primary result tables\n- 位置：Table 2, Table 5\n- 问题：5-fold CV 本身产生 5 个 fold-level accuracy，可直接报告 mean±std。Table 2 和 Table 5 是论文最核心的 result tables，却是唯二没有 variance measure 的主要表格。Figure 4 有 bootstrap CI，cross-scale table 有 95% CI——说明作者有计算能力但选择性地省略了。\n- 建议：Table 2 加 ±std 列（或 95% CI），Table 5 的 Δ_max 列改为标准 std 报告。\n\n### Minor（不影响接收）\n\n- Abstract 过度压缩（~250 words，数字密集），建议删减 cross-model chain 的具体百分比（84.75%/85.75%）以提高可读性。\n- §3.4 EDD 定义的 footnote 1 解释了 non-monotonic 情况，但正文未在 Definition 后 explicitly state \"EDD is defined relative to the classifier and feature set specified above\"。\n- Table 2 caption 说 \"Depth-0 recall exceeds 98% in all cells\" 但 Table 8 (Appendix) 显示 GPT-2 XL top-k 为 98.5%——consistent，只是 \"exceeds 98%\" 与 98.5% 的 margin 很小。\n- §1 \"our key insight is that recursive generation leaves quantifiable statistical fingerprints... universal and scale-variant\"：前半句是 post-hoc conclusion 而非 a priori insight；建议改为 hypothesis-driven 表述。\n\n---\n\n## 主要优势\n\n1. **问题新颖性**：Ordinal depth estimation 确实是文献空白。从 binary detection 到 ordinal classification 的推进有明确的科学价值。\n2. **系统性实验设计**：3×3 atlas 设计优雅，覆盖了 model family 和 decoding strategy 两个维度的交叉效应。\n3. **诚实的 Limitations**：8 段 Limitations 覆盖了大部分可预见的批评，这在 submission 中罕见。Cross-seed replication、domain bias analysis、base-model control 都体现了方法学严谨性。\n4. **特征可解释性**：p90_ppl + var_surprisal 作为 dominant features 的一致性（9/9 + 8/9，三种 importance measures concordance W=0.90）令人信服。\n5. **Ablation 充分性**：feature ablation、classifier convergence、passage length、reference model、cross-seed——覆盖面广。\n\n---\n\n## 总结判断\n\n论文定义了一个有价值的新任务，实验覆盖系统性好，但三个核心方法学问题阻碍接收：(1) 主表格缺 CI 降低了 reproducibility claim 的可信度；(2) EDD=4 的跨模型泛化统计支撑不均匀且 abstract 表述 euphemistic；(3) accumulation 场景和 matched-quality control 两个关键生态效度实验完全缺失。这些问题中 (1)(2) 可在一个 cycle 内修复，(3) 需要额外实验但技术上可行。建议 resubmit next cycle。\n\n**Confidence**: 4/5 (I am confident but not certain about my assessment)",
    "reviewer_id": "1",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 407 · 2026-05-17T06:26:14.109254+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3788
}
```

</details>

---


### Assistant

_source line 408 · 2026-05-17T06:26:23.489629+00:00_

审稿报告已提交给 Review Director。

**本轮审查核心发现**：

- 10 个历史 issues：2 个 ✅ RESOLVED（d0 inflation、single LoRA），4 个 ⚠️ PARTIALLY ADDRESSED（CI 报告、EDD 统计限定、reference 循环依赖、classifier-dependence 声明），4 个 ❌ NOT ADDRESSED（Related Work 引用遗漏、LoRA rank sensitivity、accumulation 场景验证、matched-quality control）
- 2 个新 Must-Fix（Abstract 数值取整、curation PoC 与 narrative 不一致）
- 3 个新 Should-Fix（GPT-2 XL EDD boundary case、universal fingerprint 表述过强、主表格缺 CI）
- 总体评分：Overall 3.0，Soundness 3/5，建议 resubmit next cycle

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1"
}
```

</details>

---


## Round 14

## Round 14

4 recorded events


### User

_source line 409 · 2026-05-17T06:26:54.268328+00:00_

[Round 8 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿原文。请逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

## Reviewer 2 审稿报告

**Overall**: 3.5/5
**一句话总结**: 任务定义有价值且实验全面，但新颖性定位仍不清晰（perplexity tail 是 Dohmatob 2024 的已知推论），Abstract 信息过载，且遗漏直接挑战其叙事前提的关键文献。

### Must-Fix

**N1** [critical] Related Work 遗漏直接挑战论文前提的文献
- Schaeffer et al. 2025 ("Position: Model Collapse Does Not Mean What You Think", arXiv:2503.03150) 论证 model collapse 在实际条件下并非必然发生，直接质疑本文 Introduction 核心前提。
- 建议在 Related Work 引用并回应。

**N2** [critical] 核心发现的增量贡献定位不清
- perplexity tail statistics 主导 depth discrimination 本质上是 Dohmatob 2024 "A Tale of Tails" 的 direct empirical validation。
- 建议明确 positioning：theory → practice gap + strategy-dependent insight。

**N3** [critical] Abstract 内有 §4.4 内部引用 + 数字过载
- Abstract 包含 20+ 数字和 §4.4 section 引用，违反 Abstract 独立阅读原则。
- 建议精简至 ≤8 个关键数字，删除内部引用。

### Should-Fix

**W1** Introduction "universal and scale-variant" 矛盾措辞
**W2** Discussion "enables" vs PoC "inconclusive" 张力
**W3** generalization.tex "signal universality" overclaim
**W4** Contribution bullet 3 信息过载
**W5** 遗漏 CCNet (Wenzek et al. 2020) 等 perplexity-based curation 文��
**W6** Ordinal classification 引用基础薄弱（缺 McCullagh 1980）

### Minor
- 6+ 处 em-dash AI 写作痕迹
- -ing phrase ending
- DivEye year 可能应为 2025
- conclusion.tex 命名混淆

### 优势
1. 任务定义有真实贡献
2. 实验设计系统全面
3. Limitations 诚实充分
4. 统计纪律良好

---

请对以上每个 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 410 · 2026-05-17T06:28:25.602063+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 8 交叉回应 — Reviewer 1 对 Reviewer 2 审稿意见\n\n---\n\n### Must-Fix 逐条回应\n\n**[AGREE] R2-N1: Related Work 遗漏 Schaeffer et al. 2025**\n\n同意。我在独立审稿中也将此标记为 R5-W4 未解决项。Schaeffer et al. 2025 (\"Position: Model Collapse Does Not Mean What You Think\") 直接质疑 model collapse 在实际混合数据条件下的必然性，而本文 Introduction §1 第一段以 \"a recursive loop emerges... it is already occurring in the wild\" 作为核心前提。不引用并回应最直接的反对声音是 Related Work 的显著缺陷。\n\n补充：Gerstgrasser et al. 2024（已在 references.bib 中，Schaeffer 为共同作者）讨论了 accumulation 设定下 collapse 可避免，但那是一篇独立的论文，不能替代 Schaeffer et al. 2025 的 position paper 所提出的更根本的质疑。\n\n---\n\n**[AGREE] R2-N2: 核心发现增量贡献定位不清**\n\n部分同意，但认为严重程度应从 critical 降为 should-fix。\n\n理由：\n- R2 正确指出 \"perplexity tail statistics dominate depth discrimination\" 本质上是 Dohmatob 2024 tail-erosion theory 的 empirical consequence。如果论文仅发现此点，novelty 确实不足。\n- 但论文的实际增量不仅在于 feature-level observation，还包括：(1) task formalization as ordinal classification (§3.1)；(2) EDD metric + contiguous discriminability 概念 (§3.4)；(3) strategy-dependent trajectory 差异——temperature accelerates convergence, top-k attenuates signal (§4.5)——这些是 Dohmatob 理论未预测的 empirical findings；(4) benchmark construction enabling future work。\n- **但 R2 的建议完全正确**：论文应在 Introduction 中明确 position 自己为 \"theory → practice bridge\"，承认 feature-level finding 的 theoretical prior（Dohmatob），并将 novelty claim 集中在 strategy-dependent dynamics、EDD formalization 和 cross-model generalization 上。当前写法（§1 \"Our key insight is that recursive generation leaves quantifiable statistical fingerprints\"）暗示这是全新发现，但 Dohmatob 2024 已经从理论上预测了这一点。\n\n建议：将 critical 改为 should-fix，因为增量贡献存在但 positioning 需调整。\n\n---\n\n**[AGREE] R2-N3: Abstract §4.4 引用 + 数字过载**\n\n完全同意。我在审稿 Minor 中也注意到 abstract 数字密集。\n\n具体问题：\n1. \"§4.4\" 出现在 Abstract (abstract.tex line 6) 是明确的 format violation——Abstract 必须是自包含阅读单元。\n2. 我计数 Abstract 中的数值：180K, 3, 3, 4, 19, 70--85%, 25%, 9/9, 8/9, EDD₀.₇₅=4, p=0.001, 66.4%, 55.4%, 1.7×, 84.75%, 85.75%, 70.2%, EDD=4, 60.1%, 59.9%, 70.2%, 98.5%... 超过 20 个数字。这远超正常 NLP 论文 abstract 密度。\n3. 审稿人在 30 秒内无法从这种密度中提取核心 message。\n\n但我将此标为 should-fix 而非 critical——这是写作质量问题而非方法学缺陷，不应单独影响接收决定。技术内容有效前提下，abstract 可以在 camera-ready 时修订。\n\n---\n\n### Should-Fix 逐条回应\n\n**[AGREE] R2-W1: \"universal and scale-variant\" 矛盾措辞**\n\n完全同意。我在独立审稿中也标记了此问题（我的 W2）。Introduction §1 写 fingerprints are \"universal and scale-variant\"，但 cross-strategy transfer 仅 59.1%（d1-d3: 45.9%, 1.38× chance），temperature holdout d1v2 AUC 低至 0.129 (§5.3 GPT-2 XL)。Strategy-conditioned classifiers 是必需的——这不是 \"universal\" 的定义。\n\n---\n\n**[AGREE] R2-W2: Discussion \"enables\" vs PoC \"inconclusive\" 张力**\n\n完全同意。我在独立审稿中将此标为 N2 (critical)。Discussion §6 写 \"Depth estimation enables depth-graduated data curation\"，但 Appendix Table 9 显示 RF-filtered vs. unfiltered p=0.407/0.492/0.607——全部 non-significant。仅 RF vs. random subsampling 显著。论文主文不应用 \"enables\" 描述一个 inconclusive 的 PoC。\n\n---\n\n**[AGREE] R2-W3: \"signal universality\" overclaim**\n\n同意。generalization.tex 最后一句 (line 110): \"Cross-model recursive chains (84.75%)... further confirm signal universality.\" 但：\n- Cross-strategy transfer 仅 59.1%（§5.3）\n- Cross-τ transfer 仅 46.7%（Appendix §A.4）\n- Cross-model transfer d2 recall 低至 26.8%（Table 6, Pythia holdout）\n\n\"Signal universality\" 在这些数据下是 overclaim。更准确的描述是 \"signal persists across model boundaries under matched strategy conditions\"。\n\n---\n\n**[AGREE] R2-W4: Contribution bullet 3 信息过载**\n\n同意。Introduction contribution list 第三条（introduction.tex lines 28-29）在一个 bullet 中堆砌了 7 个数字和 5 个 generalization axes，读起来像 results summary 而非 contribution statement。Contribution bullets 应陈述 what was achieved，具体数字放在相应 section。\n\n---\n\n**[AGREE] R2-W5: 遗漏 CCNet (Wenzek et al. 2020)**\n\n同意。我在独立审稿中也标记了此遗漏。CCNet 是 perplexity-based web data filtering 的 foundational work，与本文使用 perplexity features 进行 depth-based filtering 有直接方法论关联。Appendix §A.5 讨论 C4 calibration 时不引 CCNet 是明显缺失。\n\n---\n\n**[AGREE] R2-W6: Ordinal classification 引用基础薄弱**\n\n同意。我在独立审稿中也标记了此点。McCullagh 1980 (proportional odds model) 是 ordinal regression 的奠基论文。当前 §2 Ordinal Classification 段仅引 CORAL (2020) 和 CLOC (2025)，缺少理论基础。补充 McCullagh 1980 和 Rennie & Srebro 2005 不需要额外实验，仅需 1-2 句话和 bib entries。\n\n---\n\n### Minor 逐条回应\n\n**[AGREE] em-dash 和 -ing phrases**: Abstract line 1 已有 \"arises---yet\"，虽然技术上是 LaTeX 的三连 hyphen 生成的 em-dash，但仍是 AI 写作的典型标志。同意需要全文清理。\n\n**[REBUT] DivEye year**: references.bib 中 DivEye 标注为 TMLR 2026（diveye2026 entry, line 206-212），arXiv ID 2509.18880 (Sep 2025 submission, 2026 publication)。R2 认为应为 2025，但 publication venue year 标注 2026 是合理的——投稿于 2025 但 published in TMLR 2026。两种标注方式都有合理性，建议作者与 TMLR 官方 publication date 对齐即可。非实质问题。\n\n**[AGREE] conclusion.tex 命名混淆**: 文件名为 conclusion.tex 但实际包含的是 Limitations + Ethics Statement，而 Discussion and Conclusion 的内容在 discussion.tex 中。这确实容易让读者（或 collaborator）混淆。\n\n---\n\n### 总结\n\n我与 R2 的 9 条 Must-Fix/Should-Fix 中有 **9/9 方向一致**，但在严重程度上有 2 处分歧：\n1. R2-N2 我认为应从 critical 降为 should-fix（增量贡献存在，只是 positioning 需调整）\n2. R2-N3 我认为应从 critical 降为 should-fix（写作问题非方法学缺陷）\n\n我的独立审稿中标记的几个问题 R2 未覆盖：\n- 主表格 (Table 2, 5) 缺 std/CI（我的 R1-N2 续，R2 未提及）\n- LoRA rank sensitivity 缺失（我的 R1-W3 续，R2 未提及）\n- Accumulation 场景未验证（我的 R7-W3 续，R2 未提及）\n- Matched-quality control 缺失（我的 R7-W4 续，R2 未提及）\n\n这些方法学问题可能比 R2 关注的 framing/positioning 问题对接收决定影响更大。",
  "reviewer_id": "1",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 8 交叉回应 — Reviewer 1 对 Reviewer 2 审稿意见\n\n---\n\n### Must-Fix 逐条回应\n\n**[AGREE] R2-N1: Related Work 遗漏 Schaeffer et al. 2025**\n\n同意。我在独立审稿中也将此标记为 R5-W4 未解决项。Schaeffer et al. 2025 (\"Position: Model Collapse Does Not Mean What You Think\") 直接质疑 model collapse 在实际混合数据条件下的必然性，而本文 Introduction §1 第一段以 \"a recursive loop emerges... it is already occurring in the wild\" 作为核心前提。不引用并回应最直接的反对声音是 Related Work 的显著缺陷。\n\n补充：Gerstgrasser et al. 2024（已在 references.bib 中，Schaeffer 为共同作者）讨论了 accumulation 设定下 collapse 可避免，但那是一篇独立的论文，不能替代 Schaeffer et al. 2025 的 position paper 所提出的更根本的质疑。\n\n---\n\n**[AGREE] R2-N2: 核心发现增量贡献定位不清**\n\n部分同意，但认为严重程度应从 critical 降为 should-fix。\n\n理由：\n- R2 正确指出 \"perplexity tail statistics dominate depth discrimination\" 本质上是 Dohmatob 2024 tail-erosion theory 的 empirical consequence。如果论文仅发现此点，novelty 确实不足。\n- 但论文的实际增量不仅在于 feature-level observation，还包括：(1) task formalization as ordinal classification (§3.1)；(2) EDD metric + contiguous discriminability 概念 (§3.4)；(3) strategy-dependent trajectory 差异——temperature accelerates convergence, top-k attenuates signal (§4.5)——这些是 Dohmatob 理论未预测的 empirical findings；(4) benchmark construction enabling future work。\n- **但 R2 的建议完全正确**：论文应在 Introduction 中明确 position 自己为 \"theory → practice bridge\"，承认 feature-level finding 的 theoretical prior（Dohmatob），并将 novelty claim 集中在 strategy-dependent dynamics、EDD formalization 和 cross-model generalization 上。当前写法（§1 \"Our key insight is that recursive generation leaves quantifiable statistical fingerprints\"）暗示这是全新发现，但 Dohmatob 2024 已经从理论上预测了这一点。\n\n建议：将 critical 改为 should-fix，因为增量贡献存在但 positioning 需调整。\n\n---\n\n**[AGREE] R2-N3: Abstract §4.4 引用 + 数字过载**\n\n完全同意。我在审稿 Minor 中也注意到 abstract 数字密集。\n\n具体问题：\n1. \"§4.4\" 出现在 Abstract (abstract.tex line 6) 是明确的 format violation——Abstract 必须是自包含阅读单元。\n2. 我计数 Abstract 中的数值：180K, 3, 3, 4, 19, 70--85%, 25%, 9/9, 8/9, EDD₀.₇₅=4, p=0.001, 66.4%, 55.4%, 1.7×, 84.75%, 85.75%, 70.2%, EDD=4, 60.1%, 59.9%, 70.2%, 98.5%... 超过 20 个数字。这远超正常 NLP 论文 abstract 密度。\n3. 审稿人在 30 秒内无法从这种密度中提取核心 message。\n\n但我将此标为 should-fix 而非 critical——这是写作质量问题而非方法学缺陷，不应单独影响接收决定。技术内容有效前提下，abstract 可以在 camera-ready 时修订。\n\n---\n\n### Should-Fix 逐条回应\n\n**[AGREE] R2-W1: \"universal and scale-variant\" 矛盾措辞**\n\n完全同意。我在独立审稿中也标记了此问题（我的 W2）。Introduction §1 写 fingerprints are \"universal and scale-variant\"，但 cross-strategy transfer 仅 59.1%（d1-d3: 45.9%, 1.38× chance），temperature holdout d1v2 AUC 低至 0.129 (§5.3 GPT-2 XL)。Strategy-conditioned classifiers 是必需的——这不是 \"universal\" 的定义。\n\n---\n\n**[AGREE] R2-W2: Discussion \"enables\" vs PoC \"inconclusive\" 张力**\n\n完全同意。我在独立审稿中将此标为 N2 (critical)。Discussion §6 写 \"Depth estimation enables depth-graduated data curation\"，但 Appendix Table 9 显示 RF-filtered vs. unfiltered p=0.407/0.492/0.607——全部 non-significant。仅 RF vs. random subsampling 显著。论文主文不应用 \"enables\" 描述一个 inconclusive 的 PoC。\n\n---\n\n**[AGREE] R2-W3: \"signal universality\" overclaim**\n\n同意。generalization.tex 最后一句 (line 110): \"Cross-model recursive chains (84.75%)... further confirm signal universality.\" 但：\n- Cross-strategy transfer 仅 59.1%（§5.3）\n- Cross-τ transfer 仅 46.7%（Appendix §A.4）\n- Cross-model transfer d2 recall 低至 26.8%（Table 6, Pythia holdout）\n\n\"Signal universality\" 在这些数据下是 overclaim。更准确的描述是 \"signal persists across model boundaries under matched strategy conditions\"。\n\n---\n\n**[AGREE] R2-W4: Contribution bullet 3 信息过载**\n\n同意。Introduction contribution list 第三条（introduction.tex lines 28-29）在一个 bullet 中堆砌了 7 个数字和 5 个 generalization axes，读起来像 results summary 而非 contribution statement。Contribution bullets 应陈述 what was achieved，具体数字放在相应 section。\n\n---\n\n**[AGREE] R2-W5: 遗漏 CCNet (Wenzek et al. 2020)**\n\n同意。我在独立审稿中也标记了此遗漏。CCNet 是 perplexity-based web data filtering 的 foundational work，与本文使用 perplexity features 进行 depth-based filtering 有直接方法论关联。Appendix §A.5 讨论 C4 calibration 时不引 CCNet 是明显缺失。\n\n---\n\n**[AGREE] R2-W6: Ordinal classification 引用基础薄弱**\n\n同意。我在独立审稿中也标记了此点。McCullagh 1980 (proportional odds model) 是 ordinal regression 的奠基论文。当前 §2 Ordinal Classification 段仅引 CORAL (2020) 和 CLOC (2025)，缺少理论基础。补充 McCullagh 1980 和 Rennie & Srebro 2005 不需要额外实验，仅需 1-2 句话和 bib entries。\n\n---\n\n### Minor 逐条回应\n\n**[AGREE] em-dash 和 -ing phrases**: Abstract line 1 已有 \"arises---yet\"，虽然技术上是 LaTeX 的三连 hyphen 生成的 em-dash，但仍是 AI 写作的典型标志。同意需要全文清理。\n\n**[REBUT] DivEye year**: references.bib 中 DivEye 标注为 TMLR 2026（diveye2026 entry, line 206-212），arXiv ID 2509.18880 (Sep 2025 submission, 2026 publication)。R2 认为应为 2025，但 publication venue year 标注 2026 是合理的——投稿于 2025 但 published in TMLR 2026。两种标注方式都有合理性，建议作者与 TMLR 官方 publication date 对齐即可。非实质问题。\n\n**[AGREE] conclusion.tex 命名混淆**: 文件名为 conclusion.tex 但实际包含的是 Limitations + Ethics Statement，而 Discussion and Conclusion 的内容在 discussion.tex 中。这确实容易让读者（或 collaborator）混淆。\n\n---\n\n### 总结\n\n我与 R2 的 9 条 Must-Fix/Should-Fix 中有 **9/9 方向一致**，但在严重程度上有 2 处分歧：\n1. R2-N2 我认为应从 critical 降为 should-fix（增量贡献存在，只是 positioning 需调整）\n2. R2-N3 我认为应从 critical 降为 should-fix（写作问题非方法学缺陷）\n\n我的独立审稿中标记的几个问题 R2 未覆盖：\n- 主表格 (Table 2, 5) 缺 std/CI（我的 R1-N2 续，R2 未提及）\n- LoRA rank sensitivity 缺失（我的 R1-W3 续，R2 未提及）\n- Accumulation 场景未验证（我的 R7-W3 续，R2 未提及）\n- Matched-quality control 缺失（我的 R7-W4 续，R2 未提及）\n\n这些方法学问题可能比 R2 关注的 framing/positioning 问题对接收决定影响更大。",
    "reviewer_id": "1",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 411 · 2026-05-17T06:28:30.172119+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4570
}
```

</details>

---


### Assistant

_source line 412 · 2026-05-17T06:28:37.470346+00:00_

交叉回应已提交。总结：

- R2 的 9 条 Must-Fix/Should-Fix 全部方向一致 (9/9 AGREE)
- 2 处严重程度分歧：R2-N2 和 R2-N3 我认为应从 critical 降为 should-fix
- 补充了 R2 未覆盖的 4 个方法学问题（主表格缺 CI、LoRA rank sensitivity、accumulation 场景、matched-quality control）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1"
}
```

</details>

---


## Round 15

## Round 15

26 recorded events


### User

_source line 413 · 2026-05-17T08:46:26.317372+00:00_

[Round 1 审稿请求]:
## Review Assignment: R1 — Method & Experiments

**Venue:** EMNLP 2026 Main (via ACL Rolling Review)
**Paper:** "Ordinal Depth Estimation for Recursive Language Model Generations: A Depth Degradation Atlas Across Scales and Strategies"

**Scoring system (ARR 2025+):** Three scores on 1–5 scale: Soundness, Excitement, Overall Assessment.
- 5 = Top ~2%, exceptional
- 4 = Strong, warrants acceptance at a top *ACL venue
- 3 = Good, could be published but may not be top-tier
- 2 = Borderline, has merit but significant flaws
- 1 = Poor, significant flaws

**Your focus:** Method soundness, experimental rigor, statistical validity, reproducibility.

### Paper Summary
The paper formalizes "ordinal generation depth estimation": predicting how many recursive generation cycles (d ∈ {0,1,2,3}) a text passage has undergone, where depth 0 is human-written. The authors:
1. Construct a 3-model × 3-strategy × 4-depth benchmark (Pythia-1.4B, OLMo-1B, GPT-2 XL; nucleus/temperature/top-k; LoRA fine-tuning at each depth)
2. Extract 19 statistical features from a fixed reference model (Pythia-1.4B) and train RF/LR classifiers achieving 70–85% four-class accuracy (chance=25%)
3. Build a "Depth Degradation Atlas" revealing: universal depth markers (p90_ppl, var_surprisal), monotonic AUC decay, and strategy-dependent feature trajectory reversal under temperature sampling
4. Extend to 14B scale (Qwen2.5-14B, FP16, 76.2% accuracy) and prompted generation (92.8% retention vs BOS)
5. Propose a two-stage pipeline (strategy identification → conditioned depth classification) achieving 75.2%, +3.2pp over naive pooling
6. Apply classifiers to wild web data (RedPajama-v2, Dolma) showing consistent FPR gradients and temporal signal

### Evaluate These Dimensions

**A. Task Formalization (Section 3.1)**
- Is the problem definition (Eq. 1-2) clean and well-motivated?
- Is the EDD metric (Eq. 2) a meaningful contribution?

**B. Benchmark Construction (Section 3.2)**
- Is the 3×3×4 design sufficient? What's missing?
- Is LoRA-only fine-tuning a significant limitation?
- Sample sizes per configuration — are they reported clearly?

**C. Feature Extraction (Section 3.3)**
- Are 19 features well-chosen? Any obvious omissions?
- Is the fixed reference model (Pythia-1.4B) design sound?
- Is there a circularity concern when classifying Pythia-generated text?

**D. Classification (Section 3.4)**
- RF + LR only — should neural baselines be included?
- Is 5-fold stratified CV appropriate? Should there be held-out test sets?
- Are confidence intervals and significance tests adequate?

**E. Scale & Ecological Validity (Sections 5.2-5.3)**
- Does one 14B experiment suffice for "scale robustness" claims?
- Is the prompted generation experiment convincing for ecological validity?
- KS test for feature distribution comparison — appropriate?

**F. Two-Stage Pipeline (Section 5.4)**
- Is the v1→v2 improvement well-motivated?
- Oracle vs predicted gap analysis — is this analysis sound?
- Is 75.2% vs 72.0% (+3.2pp) a meaningful improvement?

**G. Wild-Data Calibration (Section 5.5)**
- Without ground-truth, how interpretable are these results?
- Is the temporal analysis (pre/post 2023) well-caveated?
- FPR estimation methodology — is it justified?

**H. Reproducibility**
- Are all hyperparameters specified?
- Is the experimental pipeline reproducible?
- Is code/data availability mentioned?

Provide: (1) numbered strengths, (2) numbered weaknesses, (3) questions for authors, (4) preliminary scores (Soundness, Excitement, Overall) with justification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 414 · 2026-05-17T08:46:42.818089+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 415 · 2026-05-17T08:46:43.169620+00:00_

1	% How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
2	% Target: EMNLP 2026 (ARR May cycle)
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{amsmath}
10	\usepackage{amssymb}
11	\usepackage{multirow}
12	\usepackage{xcolor}
13	\usepackage{subcaption}
14	\usepackage[T1]{fontenc}
15	\usepackage[utf8]{inputenc}
16	\usepackage{microtype}
17	\usepackage{amsthm}
18	
19	\theoremstyle{definition}
20	\newtheorem{definition}{Definition}
21	
22	\title{How Deep Is Your Data? Estimating Recursive Generation Depth\\via Statistical Fingerprints}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\input{abstract}
30	
31	\input{introduction}
32	
33	\input{related_work}
34	
35	\input{method}
36	
37	\input{atlas}
38	
39	\input{generalization}
40	
41	\input{discussion}
42	
43	\input{conclusion}
44	
45	\bibliography{references}
46	
47	\appendix
48	\input{section_appendix}
49	
50	\end{document}
51	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 416 · 2026-05-17T08:46:43.220750+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 417 · 2026-05-17T08:46:43.274921+00:00_

1	\begin{abstract}
2	As large language models increasingly train on web text containing their own outputs, a recursive model$\to$data$\to$model loop arises, yet no method estimates how many such iterations a text has undergone.
3	We formalize \emph{recursive generation depth estimation} as ordinal classification and construct a benchmark of 180K passages spanning 3 model families, 3 decoding strategies, and 4 generation depths.
4	A Random Forest over 19 perplexity-based features achieves 70--85\% four-class accuracy (chance = 25\%), with perplexity tail statistics emerging as consistent depth markers; a parsimonious subset of 5 features retains 97.6\% of full performance.
5	We define the \emph{Effective Discriminable Depth} (EDD) metric, finding $\mathrm{EDD}_{0.75}{=}4$ for the best-characterized family, and show that cross-model transfer reaches 66.4\% (2.7$\times$ chance).
6	Systematic generalization across seven axes (including cross-scale with 7B models at 70.2\%, cross-domain, and LoRA-rank ablation) confirms that depth signal is robust and resides in distributional statistics inaccessible from surface text (zero-shot LLMs: 30--36\%, 42\,pp below RF).
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 54
}
```

</details>

---


### Tool call

_source line 418 · 2026-05-17T08:46:43.677061+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 419 · 2026-05-17T08:46:44.631427+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	The text on which large language models are trained increasingly contains their own outputs.
5	As synthetic content proliferates across the web, a recursive loop emerges: models trained on web corpora ingest text generated by earlier models, and their outputs feed into the next generation's training data \cite{shumailov2024_nature,alemohammad2024_mad}.
6	This model$\to$data$\to$model cycle is no longer hypothetical; it is already occurring in the wild. Yet we lack the ability to determine how many recursive iterations a given text has undergone, a distinction that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \cite{dohmatob2024_tale_of_tails}.
7	
8	Existing tools address adjacent but distinct problems.
9	Binary detectors such as Binoculars \cite{binoculars2024}, Fast-DetectGPT \cite{fast_detectgpt2024}, and DivEye \cite{diveye2026} classify text as human-written or machine-generated, collapsing all depths $d \geq 1$ into a single category.
10	Watermarking \cite{kirchenbauer2023_watermark} requires proactive embedding and cannot be applied retroactively.
11	The model collapse literature \cite{shumailov2024_nature,dohmatob2024_tale_of_tails} assumes depth is known a priori; \citet{drayson2025_detection_prevents_collapse} filter synthetic data via binary detection without distinguishing depths.
12	No existing method estimates the ordinal recursive generation depth of a text passage from its content alone.
13	
14	We find that recursive generation leaves quantifiable statistical fingerprints in text, and these fingerprints are \textbf{consistent in direction but scale-dependent in magnitude} across the three model families and three decoding strategies studied.
15	Specifically, perplexity tail statistics (the 90th-percentile perplexity, \textsc{p90\_ppl}, and surprisal variance, \text
…[truncated 2445 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 420 · 2026-05-17T08:46:44.631895+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 421 · 2026-05-17T08:46:44.785080+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Definition}
5	\label{sec:method:problem}
6	
7	Let $f_\theta$ denote a language model and $\mathcal{D}_0$ a corpus of human-written seed text.
8	We define a \emph{recursive generation chain} of depth $K$ as the sequence $\mathcal{D}_0, \mathcal{D}_1, \dots, \mathcal{D}_K$, where each $\mathcal{D}_k$ ($k \geq 1$) is produced by finetuning $f_\theta$ on $\mathcal{D}_{k-1}$ and sampling from the resulting model.
9	Depth $d{=}0$ denotes human-written text; depth $d{=}k$ ($k \geq 1$) denotes text generated by a model trained on depth-$(k{-}1)$ data.
10	
11	Given a text passage $x$, the task is to estimate its recursive generation depth $d \in \{0, 1, \dots, K\}$.
12	This is an ordinal classification problem: depths carry a natural ordering, and $d{=}1$ is structurally closer to $d{=}0$ than $d{=}3$ is, since each generation step compounds distributional drift.
13	
14	\subsection{Multi-Generational Benchmark Construction}
15	\label{sec:method:benchmark}
16	
17	We construct a benchmark spanning three axes: model family, decoding strategy, and generation depth.
18	
19	\paragraph{Model families.}
20	We select three 1--1.5B-parameter models with diverse pretraining corpora and architectures: Pythia-1.4B (EleutherAI), OLMo-1B (AI2), and GPT-2~XL (OpenAI, 1.5B).
21	Restricting to a narrow parameter range isolates the effect of architecture and training data from scale.
22	
23	\paragraph{Decoding strategies.}
24	Each model is paired with three decoding strategies: nucleus sampling ($p{=}0.95$) \cite{holtzman2020_nucleus}, temperature sampling ($\tau{=}0.9$), and top-$k$ sampling ($k{=}50$).
25	These span the dominant modes of open-ended generation and induce qualitatively different entropy profiles.
26	Our findings on feature importance and discriminability are limited to this grid; transfer to untested models, scales, or strategies is not established.
27	
28	\paragraph{Depth and scale.}
29	The primary benchmark cov
…[truncated 6665 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 153
}
```

</details>

---


### Tool call

_source line 422 · 2026-05-17T08:46:44.785555+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
  }
}
```

</details>

---


### Tool result

_source line 423 · 2026-05-17T08:46:44.836307+00:00_

1	\section{The Depth Degradation Atlas}
2	\label{sec:atlas}
3	
4	We present the Depth Degradation Atlas: a systematic empirical map of how statistical fingerprints evolve across recursive generation depths, models, and decoding strategies.
5	The atlas spans $3 \times 3 = 9$ model--strategy cells evaluated at depths $d \in \{0, 1, 2, 3\}$, with depth extensions to $d{=}5$ for cross-model EDD validation (\S\ref{sec:atlas:edd}).
6	
7	%% ----------------------------------------------------------------
8	\subsection{In-Distribution Performance}
9	\label{sec:atlas:id}
10	
11	Table~\ref{tab:main_matrix} reports four-class Random Forest accuracy (5-fold CV, 200 trees) across all nine cells.
12	Accuracy ranges from 69.6\% (Pythia, top-$k$) to 85.4\% (GPT-2~XL, temperature), all exceeding the 25\% chance baseline by a wide margin.
13	Two axis effects emerge.
14	GPT-2~XL achieves the highest accuracy under every strategy (76.6--85.4\%), followed by OLMo (74.2--82.0\%) and Pythia (69.6--78.2\%).
15	Top-$k$ sampling yields the lowest accuracy in every model.
16	The mean within-model strategy gap is 8.4~pp, comparable to the 7.1~pp mean within-strategy model gap; decoding strategy and model family contribute roughly equally to performance variance.
17	
18	\begin{table}[t]
19	\centering
20	\small
21	\caption{Four-class RF accuracy (\%) across the $3 \times 3$ atlas, with d1--d3 three-class accuracy in parentheses (chance = 25\% / 33\%). Depth-0 recall exceeds 98\% in all cells.}
22	\label{tab:main_matrix}
23	\begin{tabular}{@{}lccc@{}}
24	\toprule
25	& Nucleus & Temp.\ $\tau{=}0.9$ & Top-$k$ \\
26	\midrule
27	Pythia-1.4B  & 78.2\,(71.2) & 76.3\,(70.6) & 69.6\,(58.8) \\
28	OLMo-1B     & 78.8\,(75.0) & 82.0\,(76.3) & 74.2\,(66.1) \\
29	GPT-2~XL    & 83.3\,(79.0) & 85.4\,(82.6) & 76.6\,(69.5) \\
30	\bottomrule
31	\end{tabular}
32	\end{table}
33	
34	\paragraph{Per-class recall distribution.}
35	Depth-0 recall exceeds 98\% in all 9 cells, confirming that human-written text is trivially
…[truncated 11971 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 424 · 2026-05-17T08:47:02.065830+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
  }
}
```

</details>

---


### Tool result

_source line 425 · 2026-05-17T08:47:02.618195+00:00_

1	\section{Generalization and Robustness}
2	\label{sec:generalization}
3	
4	We test whether atlas accuracy (69.6--85.4\%) reflects genuine statistical regularities, evaluating along seven axes: four below (\S\ref{sec:gen:baselines}--\S\ref{sec:gen:crossscale}) and three in the Appendix (end-to-end learning, temperature robustness, cross-boundary transfer).
5	
6	\subsection{Classifier Comparison and Surface-Text Ablation}
7	\label{sec:gen:baselines}
8	
9	Table~\ref{tab:baselines} evaluates bagging (RF) and gradient boosting (XGBoost, LightGBM) on the same 19 features; per-cell spread is $\leq$0.4pp, establishing a feature-determined ceiling.
10	On Pythia nucleus, CORAL ordinal regression \cite{coral2020} (78.1\%) and DivEye \cite{diveye2026} (78.2\%) match the within-cell RF of Table~\ref{tab:main_matrix} within 0.1\,pp (bootstrap $p>0.05$, Bonferroni-corrected); all feature-based methods significantly outperform CE-MLP (74.9\%, $p<0.001$) and logistic regression (75.0\%).
11	
12	\paragraph{Surface-text ablation.}
13	Single-feature regression on mean perplexity performs at chance (25.1\%); two zero-shot LLMs (DeepSeek V3.2, 36.2\%; Qwen2.5-7B-Instruct, 30.4\%; each 500 samples, prompt in Appendix~\ref{app:zeroshot_prompt}) also fail, confirming that the depth signal resides in distributional statistics inaccessible from surface text alone (42\,pp gap vs.\ RF at 78.2\%).
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\caption{Classifier convergence: 4-class accuracy (\%) across three atlas cells. RF (bagging), XGBoost and LightGBM (gradient boosting) operate on the same 19 features; $\Delta_{\max}$: largest per-cell spread. Chance = 25\%. RF values differ from Table~\ref{tab:main_matrix} by $\leq$0.7pp due to matched-fold evaluation.}
19	\label{tab:baselines}
20	\begin{tabular}{@{}lcccc@{}}
21	\toprule
22	Cell & RF & XGB & LGBM & $\Delta_{\max}$ \\
23	\midrule
24	Pythia, nuc. & 78.8 & 79.0 & 78.9 & 0.2 \\
25	GPT-2~XL, $\tau$ & 85.8 & 86.2 & 86.2 & 0.4 \\
26	Pythia
…[truncated 5423 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 426 · 2026-05-17T08:47:02.618709+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 427 · 2026-05-17T08:47:03.120957+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	We formalized recursive generation depth estimation and showed that perplexity tail statistics achieve 70--85\% four-class accuracy ($\mathrm{EDD}_{0.75}{=}4$), with five features sufficing for 97.6\% of full performance and classifier-agnostic convergence within $\leq$0.4pp.
5	These features generalize across model families without retraining, positioning depth estimation as an early-warning signal for model collapse~\cite{shumailov2024_nature,shi2025_closer_look}; zero-shot LLMs at 30--36\% (\S\ref{sec:gen:baselines}) confirm the signal is inaccessible from surface text alone.
6	Cross-strategy transfer remains the primary bottleneck; see Limitations for detailed analysis.
7	Depth-graduated curation complements binary detection~\cite{dsir2023,qurating2024} and watermarking~\cite{kirchenbauer2023_watermark} as a provenance signal~\cite{bevendorff2025_two_paradigms}; pilot results are inconclusive (Appendix~\ref{app:curation_poc}) and adversarial robustness remains untested.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 428 · 2026-05-17T08:47:03.121334+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 429 · 2026-05-17T08:47:03.676446+00:00_

1	\section{Additional Results}
2	\label{app:additional}
3	
4	\subsection{Top-$k$ Feature Trajectories}
5	\label{app:topk_trajectories}
6	
7	Figure~\ref{fig:feature_trajectory} in the main text shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\tau{=}0.9$) sampling.
8	Top-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \S\ref{sec:atlas:strategy}.
9	Concretely, the d0$\to$d1 drop in \textsc{p90\_ppl} under top-$k$ is 78\% (vs.\ 87\% for nucleus), and the d2$\to$d3 reduction is 31\% (vs.\ 39\% for nucleus).
10	Despite the magnitude reduction, feature rank ordering across depths is preserved, which explains why ordinal classifiers maintain directionality even under top-$k$ conditions.
11	
12	\subsection{Permutation Importance}
13	\label{app:permutation}
14	
15	To verify that the Gini-based importance rankings in \S\ref{sec:atlas:features} are not an artifact of the impurity measure, we compute permutation importance (5-fold CV, 10 repeats) for all 9 atlas cells.
16	The top-2 features are stable across measures: \textsc{p90\_ppl} ranks in the top 2 in 9/9 cells under both Gini and permutation importance, and \textsc{var\_surprisal} in 8/9 (vs.\ 7/9 for Gini, with the additional cell being OLMo top-$k$; the single SHAP exception is GPT-2~XL top-$k$, where \textsc{p75\_ppl} displaces \textsc{var\_surprisal} to rank 3).
17	Kendall's $W{=}0.90$ across all three methods (Gini, permutation, SHAP) indicates strong concordance ($p{<}0.005$).
18	Pairwise Spearman correlations are: SHAP--Gini $\rho{=}0.93$, SHAP--permutation $\rho{=}0.84$, Gini--permutation $\rho{=}0.76$.
19	Per-cell top-5 overlap between SHAP and permutation importance is 3--4 out of 5 features; the aggregated (mean-across-cells) top-5 sets are identical, confirming that the top features are robust to the choice of importance measure at the aggregate l
…[truncated 34507 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 555
}
```

</details>

---


### Tool call

_source line 430 · 2026-05-17T08:47:03.676820+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 431 · 2026-05-17T08:47:03.677149+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Cross-strategy deployment constraint.}
5	Cross-strategy transfer induces a d1/d2 boundary inversion under temperature sampling.
6	Per-strategy z-score normalization partially corrects the inversion under logistic regression (GPT-2~XL d1v2 AUC $0.24{\to}0.56$, OLMo $0.19{\to}0.70$) but yields negligible improvement for the Random Forest classifier used throughout the main experiments ($\Delta < 0.02$\,pp), and even in the best case (logistic regression) leaves a residual gap relative to within-strategy performance (${\sim}0.83$), indicating that a two-stage pipeline (strategy identification + strategy-conditioned classification) is needed for reliable cross-strategy deployment.
7	
8	\paragraph{d0 inflation of headline metrics.}
9	Depth~0 (human-written text) is near-perfectly separable (recall $>$98\% across all nine model--strategy settings), inflating headline accuracy.
10	Cross-model transfer accuracy of 66.4\% is substantially driven by d0; d2 recall drops to 26.8\% in the worst case (Pythia holdout).
11	
12	\paragraph{Controlled vs.\ ecological setting.}
13	The primary benchmark uses Wikipedia seed text with controlled recursive generation (LoRA fine-tuning, 1--1.5B parameter models); cross-scale experiments extend to 7--8B instruction-tuned models (\S\ref{sec:gen:crossscale}).
14	This protocol isolates the recursive depth variable but diverges from wild recursive contamination, where models are pretrained on mixed corpora containing prior-generation outputs at unknown proportions; the fingerprints we identify may attenuate or shift under such diffuse exposure.
15	Depth signal is the dominant classification factor (5-fold CV 59--82\%, up to 2.5$\times$ chance): LOGO accuracy (72.1\%) matches standard CV (72.0\%), and seed-group prediction is at chance (10.2\% vs.\ 10\%; Appendix~\ref{app:domain_bias}).
16	Cross-scale experiments include both instruction-tuned and base variants; the base model sho
…[truncated 5260 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 432 · 2026-05-17T08:47:04.625184+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 433 · 2026-05-17T08:47:04.776109+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Model Collapse Theory.}
5	\citet{shumailov2024_nature} demonstrate that recursive training on model outputs erodes distributional tails; \citet{dohmatob2024_tale_of_tails} formalize this via scaling laws \cite{seddik2024synthetic}, \citet{dohmatob2025_strong_collapse} establish strong collapse guarantees, and the MAD framework \cite{alemohammad2024_mad} extends the analysis to self-consuming models.
6	Subsequent work addresses mitigation \cite{gerstgrasser2024_accumulate,drayson2025_detection_prevents_collapse,yi2026_escaping_collapse,falahati2026_curated,wenzek2020_ccnet}, non-monotonic dynamics \cite{bakshi2026_collapse_improvement}, convergence \cite{marchi2024_heat_death,wang2026_contamination,knowledge_collapse2025,dohmatob2024_demystified}, and diversity decline \cite{guo2024curious,briesch2024selfconsuming,padmakumar2024diversity,sigma2026_spectral,synthetic_eggs2026}.
7	\citet{schaeffer2025} argue that ``model collapse'' conflates multiple distinct phenomena, underscoring the need for operationally precise metrics.
8	Dohmatob et al.\ predict that recursive training erodes distributional tails as a theoretical scaling law \citep{dohmatob2024_tale_of_tails}; we operationalize this prediction into a deployable ordinal classifier, revealing strategy-dependent trajectories and non-monotonic 7B behavior that the theory does not predict.
9	All assume depth is known a priori; we address the inverse problem of estimating depth from text alone.
10	
11	\paragraph{AI Text Detection.}
12	The detection literature \cite{wu2025_detection_survey} spans statistical methods (DetectGPT \cite{mitchell2023_detectgpt}, Fast-DetectGPT \cite{fast_detectgpt2024}, Binoculars \cite{binoculars2024}, DivEye \cite{diveye2026}, GLTR \cite{gehrmann2019_gltr}, Ghostbuster \cite{verma2024_ghostbuster}, DNA-GPT \cite{yang2024_dnagpt}) and watermarking \cite{kirchenbauer2023_watermark}, with known limits from paraphrasing \cite{sada
…[truncated 2177 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 434 · 2026-05-17T08:47:04.827019+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 435 · 2026-05-17T08:47:04.877954+00:00_

1	% ============================================================
2	% Model Collapse Theory
3	% ============================================================
4	
5	@article{shumailov2024_nature,
6	  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
7	  title     = {{AI models collapse when trained on recursively generated data}},
8	  journal   = {Nature},
9	  volume    = {631},
10	  pages     = {755--759},
11	  year      = {2024},
12	  doi       = {10.1038/s41586-024-07566-y},
13	}
14	
15	@inproceedings{dohmatob2024_tale_of_tails,
16	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia},
17	  title     = {{A Tale of Tails: Model Collapse as a Change of Scaling Laws}},
18	  booktitle = {Proceedings of ICML},
19	  year      = {2024},
20	  note      = {arXiv:2402.07043},
21	  url       = {https://arxiv.org/abs/2402.07043},
22	}
23	
24	@inproceedings{dohmatob2025_strong_collapse,
25	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
26	  title     = {{Strong Model Collapse}},
27	  booktitle = {Proceedings of ICLR},
28	  year      = {2025},
29	  note      = {arXiv:2410.04840},
30	  url       = {https://arxiv.org/abs/2410.04840},
31	}
32	
33	@inproceedings{dohmatob2024_demystified,
34	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia},
35	  title     = {{Model Collapse Demystified: The Case of Regression}},
36	  booktitle = {Proceedings of NeurIPS},
37	  year      = {2024},
38	  note      = {arXiv:2402.07712},
39	  url       = {https://arxiv.org/abs/2402.07712},
40	}
41	
42	@inproceedings{alemohammad2024_mad,
43	  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},
44	  title     = {{Self-Consuming Generative Models Go MAD}},
45	  booktitle = {Proceedings of ICLR},

…[truncated 23683 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 436 · 2026-05-17T08:49:52.072281+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 1 审稿报告 — Reviewer 1（Method & Experiments）\n\n**Paper**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n**Venue**: EMNLP 2026 Main (ARR May 2026 cycle)\n\n---\n\n### ⚠️ 重要说明：Paper Summary 与实际论文不一致\n\nDirector 的 paper summary 描述了以下内容，但当前 tex 文件中 **不存在**：\n- **14B 实验** (Qwen2.5-14B, FP16, 76.2%)：实际论文仅有 7B（Qwen2.5-7B: 60.1%, Llama-3.1-8B: 70.2%）\n- **Prompted generation** (92.8% retention)：论文未包含此实验，BOS-seeded 生成被标注为 limitation\n- **Two-stage pipeline** (§5.4, 75.2%)：论文中 §5.4 是 \"Preliminary Cross-Scale Observations\"，无 two-stage pipeline\n- **Wild-data calibration on RedPajama-v2/Dolma**：论文使用 WikiText-103 和 C4，在 Appendix §A.5 中\n- **论文标题**：实际为 \"How Deep Is Your Data?\"，而非 Director summary 中的 \"Ordinal Depth Estimation...\"\n\n以下审稿基于 **实际 tex 文件内容**。如果 Director 描述的是计划中的修改，请确认后我可以对新版重新审稿。\n\n---\n\n## (1) Strengths\n\n**S1. 问题定义清晰且有真实空白。** Recursive depth estimation as ordinal classification（§3.1）是 binary detection 的自然且重要的扩展。Definition 1 (EDD) 数学上严谨：contiguous discriminability prefix + threshold sensitivity 是 well-motivated 的设计选择。\n\n**S2. Atlas 设计系统性优秀。** 3×3 grid + depth extension to d5 + EDD threshold sensitivity at T ∈ {0.65, 0.70, 0.75, 0.80}（Table 4）提供了全面的 landscape view。Strategy-dependent trajectory 发现（temperature 加速 convergence、top-k 衰减信号；§4.5）超越了 Dohmatob 2024 的理论预测。\n\n**S3. 多轮修订后 Related Work 显著改善。** 现在引用 Schaeffer et al. 2025（反驳 collapse 必然性）、McCullagh 1980（ordinal 经典）、Frank 2001、Rennie & Srebro 2005、CCNet（Wenzek et al. 2020）。Dohmatob 定位清晰：\"we operationalize this prediction into a deployable ordinal classifier\"（related_work.tex line 8）。\n\n**S4. Feature importance 一致性令人信服。** p90_ppl top-2 in 9/9 cells（Gini）、var_surprisal 8/9（SHAP），三种 importance measures concordance W=0.90 (p<0.005)。Top-5 features 达到 97.6% full accuracy。VIF 分析 + forward selection 提供了独立验证。\n\n**S5. 诚实的 Limitations。** 8 段 Limitations 覆盖 cross-strategy failure、d0 inflation、ecological gap、FPR variability、adversarial robustness、EDD monotonicity、reference dependency、single LoRA。Discussion 现在明确说 curation pilot \"inconclusive\"（discussion.tex line 7）。\n\n**S6. LoRA rank ablation 新增。** generalization.tex line 110-111 报告 rank 4-64 accuracy spread 4.65pp，解决了此前遗留的方法学缺失。\n\n**S7. 三个 reference model ablation。** 从单一 OLMo ablation 扩展到三个 reference architectures（67-79% range），conclusion.tex line 35-39 详细讨论。\n\n---\n\n## (2) Weaknesses\n\n### 按维度组织\n\n#### A. Task Formalization (§3.1)\n\n**W1** [minor] EDD 仍未显式声明为 operational measure。Definition 1 指定了具体的 classifier（RF 500 trees, ⌊√19⌋ features per split），但文本未明确说 \"EDD is conditioned on the classifier and feature set; a different classifier may yield different EDD values.\" §5.1 的 classifier convergence（≤0.4pp）间接表明 classifier 依赖性小，但应 explicit。\n\n#### B. Benchmark Construction (§3.2)\n\n**W2** [moderate] BOS-seeded generation 是显著生态效度限制。论文承认 \"BOS-seeded generation may amplify depth signal relative to prompted settings\"（method.tex line 35）但未提供任何 prompted generation 数据点。这对读者评估 real-world applicability 至关重要——prompted text 通常有更高的 coherence 和更低的 repetition，可能大幅衰减 depth signal。Director summary 提到 92.8% retention 实验但论文中不存在。\n\n**W3** [minor] 全量 fine-tuning 未对比。LoRA rank ablation (4-64) 是好的补充，但 LoRA 与 full fine-tuning 的 depth signal 差异未测试。在 wild 中，recursive contamination 更可能通过 full pretraining 而非 LoRA 发生。\n\n#### C. Feature Extraction (§3.3)\n\n**W4** [minor] Reference model circularity 已充分讨论但未完全解决。三个 reference models 都是 ~1-1.5B autoregressive decoder-only。Limitations 提到 \"architecturally distinct references... remains open\"，这是合理的 scope limitation。Reference-free surface features 53.7%（confirming partial signal without reference model）是有价值的 baseline。\n\n#### D. Classification (§3.4 / §5.1)\n\n**W5** [moderate] Table 2 和 Table 5 仍缺 std/CI。这是多轮审稿以来的 persistent issue。5-fold CV 天然产生 fold-level variance；Figure 4 有 bootstrap CI，cross-scale table 有 95% CI brackets，Table 9 (Appendix curation) 有 std——但两个最核心的 main-text tables 仍然只报告点估计。至少应在 Table 2 加 ±std 列。\n\n**W6** [minor] DeBERTa/RoBERTa end-to-end baselines 仅使用 base-size (~125M)。论文承认 \"whether larger PLMs (e.g., 7B+) can close the gap... remains an open question\"（section_appendix.tex line 188），但 ~125M 的 neural baseline 对 \"depth signal is inaccessible to PLM representations\" 的 claim 支撑不够强。\n\n#### E. Scale & Ecological Validity (§5.4)\n\n**W7** [moderate] Cross-scale 仅有两个 7B 模型，且均为 4-bit QLoRA。Director summary 描述了 14B FP16 实验但不在论文中。当前仅有 Qwen2.5-7B (60.1%) 和 Llama-3.1-8B (70.2%)：\n- 60.1% 的 lower CI bound (58.0%) 仅 marginally above chance at d1-d3 level\n- 两个模型 divergent AUC trajectories（monotonic vs U-shaped）无法判断哪个是 dominant pattern\n- Quantization confound 无法与 vocabulary mismatch 解耦\n- 论文正确标注为 \"Preliminary\"——这是诚实的，但削弱了 scale robustness claim\n\n**W8** [moderate] Wild-data calibration 缺乏 ground truth。Appendix §A.5 的 C4 FPR 分析假设所有 C4 passages 为 human-written (d0)，但 2023+ web crawl 数据可能已包含 LLM-generated text，使 \"false positive\" rate 成为 upper bound estimate。论文未讨论这一 caveat。\n\n#### F. Two-Stage Pipeline\n\n**W9** [info] 论文中不存在。Limitations 提到 \"a two-stage pipeline (strategy identification + strategy-conditioned classification) is needed for reliable cross-strategy deployment\"（conclusion.tex line 6）但未实现。\n\n#### G. Wild-Data Analysis\n\n**W10** [minor] Wild-data 结果仅在 Appendix，且无时间维度分析。论文使用 WikiText-103 和 C4 而非 Director summary 中的 RedPajama-v2/Dolma。GPT-2 XL 的 22.4% C4 FPR 是 deployment-critical 的数字但仅在 Appendix 中报告。\n\n#### H. Reproducibility\n\n**W11** [minor] Code/data \"will be released upon acceptance\"（conclusion.tex line 58）。当前版本无法验证 pipeline 可复现性。LoRA hyperparameters 完整（r=16, α=32, lr=2e-4, batch=8, 3 epochs, dropout=0.05），RF params 完整（200/500 trees, 5-fold CV）。总体 specification level 良好。\n\n### 独立于维度的问题\n\n**W12** [moderate] Accumulation/mixing 场景完全未测试。Appendix §A.9 \"Mixed-Depth Corpus\" 仅测试 evaluation set class balance 变化的影响（macro-recall Δ=-1.62pp），不是真正的 accumulation 场景（如 Gerstgrasser et al. 2024 的 D_k = α·D_0 + (1-α)·D_{k-1}）。Limitations 承认 \"wild recursive contamination, where models are pretrained on mixed corpora... the fingerprints we identify may attenuate or shift\"——但缺少任何实验验证。这是 ecological validity 的核心缺口。\n\n**W13** [moderate] Depth estimation vs quality estimation confound 未控制。论文未测试：在匹配 text quality（如按 perplexity bin 分层）的条件下，depth 是否仍可区分。间接证据存在（τ=1.1 signal collapse 说明不纯粹是 quality；cross-model chains 排除单一模型的 quality gradient），但无直接 confound-control 实验。\n\n**W14** [minor] Abstract \"70-85%\" 仍然将 69.6% 向上取整为 70%（Table 2 实际 lower bound）。\n\n---\n\n## (3) Questions for Authors\n\nQ1. LoRA rank ablation（§5.4 末尾）仅提到 \"accuracy spread 4.65pp\"。能否提供 per-rank accuracy 数据（r=4, 16, 64）和对应的 feature importance rankings？rank 对 EDD 有影响吗？\n\nQ2. Cross-scale 中 Qwen2.5-7B 的 U-shaped AUC 恢复（d2v3=0.709 → d3v4=0.732 → d4v5=0.772）是否可能反映 instruction-tuning data 在 d3+ 深度引入了训练数据中已有的 pattern？base Qwen2.5-7B 的 AUC trajectory 是否也是 U-shaped？\n\nQ3. GPT-2 XL 的 d3v4 AUC 恰好等于 threshold 0.750（p=0.505）。如果使用 one-sided test H₀: AUC ≤ 0.75，这是 null result。你们是否考虑过在 EDD 定义中引入 statistical significance 要求（如 AUC > T AND p < α）？\n\nQ4. C4 FPR 分析假设所有 passages 为 human-written。考虑到 C4 的时间范围，这一假设在 2023+ 数据上是否仍然合理？是否有子集分析（如按 document date 分层）？\n\nQ5. Curation PoC（Appendix §A.6）中 RF-filtered vs unfiltered 无显著差异（p=0.407）。这是否因为 Pythia-1.4B 在 depth 0-3 数据上的 depth signal 本身太弱以至于过滤不产生质量差异？还是因为 downstream task（perplexity evaluation on Pythia-410M）对 training data quality 不够敏感？\n\n---\n\n## (4) Preliminary Scores\n\n| Dimension | Score | Justification |\n|-----------|-------|---------------|\n| **Soundness** | 3.5/5 | 核心方法论正确：EDD 定义严谨、feature importance 通过三种 measures 验证、domain bias control 充分。但 Table 2/5 缺 CI（persistent issue）、accumulation 和 quality-control 实验缺失削弱 ecological validity claims。GPT-2 XL EDD=4 at p=0.505 是统计 boundary case。 |\n| **Excitement** | 3.5/5 | Ordinal depth estimation 是真正的文献空白。Strategy-dependent trajectories 和 \"memorization as prerequisite\" insight（Appendix §A.4: τ=1.1 collapse）是有趣的 empirical finding。但 practical applicability 受限于 (a) strategy-conditioned 需求未实现、(b) curation PoC inconclusive、(c) wild-data FPR 高达 22.4%。 |\n| **Overall** | 3.5/5 | 论文相比前轮有实质性改善：Related Work 补全、LoRA rank ablation 新增、Introduction 措辞修正、Discussion curation narrative 诚实化、Abstract 精简。核心贡献（task formalization + atlas + EDD）solid for Findings。主要残余问题：(1) Tables 2/5 缺 CI 是 long-standing gap；(2) accumulation scenario 是 ecological validity 的 hard gap；(3) cross-scale 仅两个 7B+QLoRA 模型（Director summary 描述的 14B FP16 实验不在当前稿件中）。若 Director summary 中的计划内容（14B、prompted、two-stage pipeline、RedPajama/Dolma）能实际纳入论文，Overall 可升至 4.0。 |\n\n**Confidence**: 4/5 — 对 method/experiments 维度有高置信度；对 Director summary 中描述但不在 tex 中的内容无法评判。\n\n---\n\n### 相比 Round 8 的变化追踪\n\n| Issue | Round 8 状态 | 当前状态 | 变化 |\n|-------|-------------|---------|------|\n| R5-W4 (Related Work 遗漏) | ❌ NOT ADDRESSED | ✅ RESOLVED | 全部补齐 |\n| R1-W3 (LoRA rank) | ❌ NOT ADDRESSED | ✅ RESOLVED | rank 4-64 ablation |\n| R2-N2 (novelty positioning) | ⚠️ | ✅ RESOLVED | Dohmatob explicit positioning |\n| R2-N3 (Abstract overload) | ⚠️ | ✅ RESOLVED | 精简，无内部引用 |\n| R2-W1 (universal overclaim) | ⚠️ | ✅ RESOLVED | 改为 \"consistent in direction but scale-dependent\" |\n| R2-W2 (curation \"enables\") | ⚠️ | ✅ RESOLVED | 改为 \"inconclusive\" |\n| R1-N2 (Table CI) | ⚠️ PARTIAL | ⚠️ STILL PARTIAL | Table 2/5 仍缺 |\n| R4-N1 (EDD stat qualification) | ⚠️ PARTIAL | ✅ IMPROVED | Abstract 更简洁，详情在正文 |\n| R7-W3 (accumulation) | ❌ NOT ADDRESSED | ❌ STILL MISSING | |\n| R7-W4 (quality control) | ❌ NOT ADDRESSED | ❌ STILL MISSING | |\n| R5-W5 (EDD operational) | ⚠️ PARTIAL | ⚠️ STILL PARTIAL | |\n\n**总结**：论文在 Related Work、novelty positioning、Abstract 质量、LoRA ablation、reference model ablation、Discussion 诚实性上有实质进步。核心残余：(1) Tables 缺 CI；(2) accumulation + quality-control experiments；(3) Director 描述的 14B/prompted/two-stage/RedPajama 内容未落地到 tex 文件。",
  "reviewer_id": "1",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 1 审稿报告 — Reviewer 1（Method & Experiments）\n\n**Paper**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n**Venue**: EMNLP 2026 Main (ARR May 2026 cycle)\n\n---\n\n### ⚠️ 重要说明：Paper Summary 与实际论文不一致\n\nDirector 的 paper summary 描述了以下内容，但当前 tex 文件中 **不存在**：\n- **14B 实验** (Qwen2.5-14B, FP16, 76.2%)：实际论文仅有 7B（Qwen2.5-7B: 60.1%, Llama-3.1-8B: 70.2%）\n- **Prompted generation** (92.8% retention)：论文未包含此实验，BOS-seeded 生成被标注为 limitation\n- **Two-stage pipeline** (§5.4, 75.2%)：论文中 §5.4 是 \"Preliminary Cross-Scale Observations\"，无 two-stage pipeline\n- **Wild-data calibration on RedPajama-v2/Dolma**：论文使用 WikiText-103 和 C4，在 Appendix §A.5 中\n- **论文标题**：实际为 \"How Deep Is Your Data?\"，而非 Director summary 中的 \"Ordinal Depth Estimation...\"\n\n以下审稿基于 **实际 tex 文件内容**。如果 Director 描述的是计划中的修改，请确认后我可以对新版重新审稿。\n\n---\n\n## (1) Strengths\n\n**S1. 问题定义清晰且有真实空白。** Recursive depth estimation as ordinal classification（§3.1）是 binary detection 的自然且重要的扩展。Definition 1 (EDD) 数学上严谨：contiguous discriminability prefix + threshold sensitivity 是 well-motivated 的设计选择。\n\n**S2. Atlas 设计系统性优秀。** 3×3 grid + depth extension to d5 + EDD threshold sensitivity at T ∈ {0.65, 0.70, 0.75, 0.80}（Table 4）提供了全面的 landscape view。Strategy-dependent trajectory 发现（temperature 加速 convergence、top-k 衰减信号；§4.5）超越了 Dohmatob 2024 的理论预测。\n\n**S3. 多轮修订后 Related Work 显著改善。** 现在引用 Schaeffer et al. 2025（反驳 collapse 必然性）、McCullagh 1980（ordinal 经典）、Frank 2001、Rennie & Srebro 2005、CCNet（Wenzek et al. 2020）。Dohmatob 定位清晰：\"we operationalize this prediction into a deployable ordinal classifier\"（related_work.tex line 8）。\n\n**S4. Feature importance 一致性令人信服。** p90_ppl top-2 in 9/9 cells（Gini）、var_surprisal 8/9（SHAP），三种 importance measures concordance W=0.90 (p<0.005)。Top-5 features 达到 97.6% full accuracy。VIF 分析 + forward selection 提供了独立验证。\n\n**S5. 诚实的 Limitations。** 8 段 Limitations 覆盖 cross-strategy failure、d0 inflation、ecological gap、FPR variability、adversarial robustness、EDD monotonicity、reference dependency、single LoRA。Discussion 现在明确说 curation pilot \"inconclusive\"（discussion.tex line 7）。\n\n**S6. LoRA rank ablation 新增。** generalization.tex line 110-111 报告 rank 4-64 accuracy spread 4.65pp，解决了此前遗留的方法学缺失。\n\n**S7. 三个 reference model ablation。** 从单一 OLMo ablation 扩展到三个 reference architectures（67-79% range），conclusion.tex line 35-39 详细讨论。\n\n---\n\n## (2) Weaknesses\n\n### 按维度组织\n\n#### A. Task Formalization (§3.1)\n\n**W1** [minor] EDD 仍未显式声明为 operational measure。Definition 1 指定了具体的 classifier（RF 500 trees, ⌊√19⌋ features per split），但文本未明确说 \"EDD is conditioned on the classifier and feature set; a different classifier may yield different EDD values.\" §5.1 的 classifier convergence（≤0.4pp）间接表明 classifier 依赖性小，但应 explicit。\n\n#### B. Benchmark Construction (§3.2)\n\n**W2** [moderate] BOS-seeded generation 是显著生态效度限制。论文承认 \"BOS-seeded generation may amplify depth signal relative to prompted settings\"（method.tex line 35）但未提供任何 prompted generation 数据点。这对读者评估 real-world applicability 至关重要——prompted text 通常有更高的 coherence 和更低的 repetition，可能大幅衰减 depth signal。Director summary 提到 92.8% retention 实验但论文中不存在。\n\n**W3** [minor] 全量 fine-tuning 未对比。LoRA rank ablation (4-64) 是好的补充，但 LoRA 与 full fine-tuning 的 depth signal 差异未测试。在 wild 中，recursive contamination 更可能通过 full pretraining 而非 LoRA 发生。\n\n#### C. Feature Extraction (§3.3)\n\n**W4** [minor] Reference model circularity 已充分讨论但未完全解决。三个 reference models 都是 ~1-1.5B autoregressive decoder-only。Limitations 提到 \"architecturally distinct references... remains open\"，这是合理的 scope limitation。Reference-free surface features 53.7%（confirming partial signal without reference model）是有价值的 baseline。\n\n#### D. Classification (§3.4 / §5.1)\n\n**W5** [moderate] Table 2 和 Table 5 仍缺 std/CI。这是多轮审稿以来的 persistent issue。5-fold CV 天然产生 fold-level variance；Figure 4 有 bootstrap CI，cross-scale table 有 95% CI brackets，Table 9 (Appendix curation) 有 std——但两个最核心的 main-text tables 仍然只报告点估计。至少应在 Table 2 加 ±std 列。\n\n**W6** [minor] DeBERTa/RoBERTa end-to-end baselines 仅使用 base-size (~125M)。论文承认 \"whether larger PLMs (e.g., 7B+) can close the gap... remains an open question\"（section_appendix.tex line 188），但 ~125M 的 neural baseline 对 \"depth signal is inaccessible to PLM representations\" 的 claim 支撑不够强。\n\n#### E. Scale & Ecological Validity (§5.4)\n\n**W7** [moderate] Cross-scale 仅有两个 7B 模型，且均为 4-bit QLoRA。Director summary 描述了 14B FP16 实验但不在论文中。当前仅有 Qwen2.5-7B (60.1%) 和 Llama-3.1-8B (70.2%)：\n- 60.1% 的 lower CI bound (58.0%) 仅 marginally above chance at d1-d3 level\n- 两个模型 divergent AUC trajectories（monotonic vs U-shaped）无法判断哪个是 dominant pattern\n- Quantization confound 无法与 vocabulary mismatch 解耦\n- 论文正确标注为 \"Preliminary\"——这是诚实的，但削弱了 scale robustness claim\n\n**W8** [moderate] Wild-data calibration 缺乏 ground truth。Appendix §A.5 的 C4 FPR 分析假设所有 C4 passages 为 human-written (d0)，但 2023+ web crawl 数据可能已包含 LLM-generated text，使 \"false positive\" rate 成为 upper bound estimate。论文未讨论这一 caveat。\n\n#### F. Two-Stage Pipeline\n\n**W9** [info] 论文中不存在。Limitations 提到 \"a two-stage pipeline (strategy identification + strategy-conditioned classification) is needed for reliable cross-strategy deployment\"（conclusion.tex line 6）但未实现。\n\n#### G. Wild-Data Analysis\n\n**W10** [minor] Wild-data 结果仅在 Appendix，且无时间维度分析。论文使用 WikiText-103 和 C4 而非 Director summary 中的 RedPajama-v2/Dolma。GPT-2 XL 的 22.4% C4 FPR 是 deployment-critical 的数字但仅在 Appendix 中报告。\n\n#### H. Reproducibility\n\n**W11** [minor] Code/data \"will be released upon acceptance\"（conclusion.tex line 58）。当前版本无法验证 pipeline 可复现性。LoRA hyperparameters 完整（r=16, α=32, lr=2e-4, batch=8, 3 epochs, dropout=0.05），RF params 完整（200/500 trees, 5-fold CV）。总体 specification level 良好。\n\n### 独立于维度的问题\n\n**W12** [moderate] Accumulation/mixing 场景完全未测试。Appendix §A.9 \"Mixed-Depth Corpus\" 仅测试 evaluation set class balance 变化的影响（macro-recall Δ=-1.62pp），不是真正的 accumulation 场景（如 Gerstgrasser et al. 2024 的 D_k = α·D_0 + (1-α)·D_{k-1}）。Limitations 承认 \"wild recursive contamination, where models are pretrained on mixed corpora... the fingerprints we identify may attenuate or shift\"——但缺少任何实验验证。这是 ecological validity 的核心缺口。\n\n**W13** [moderate] Depth estimation vs quality estimation confound 未控制。论文未测试：在匹配 text quality（如按 perplexity bin 分层）的条件下，depth 是否仍可区分。间接证据存在（τ=1.1 signal collapse 说明不纯粹是 quality；cross-model chains 排除单一模型的 quality gradient），但无直接 confound-control 实验。\n\n**W14** [minor] Abstract \"70-85%\" 仍然将 69.6% 向上取整为 70%（Table 2 实际 lower bound）。\n\n---\n\n## (3) Questions for Authors\n\nQ1. LoRA rank ablation（§5.4 末尾）仅提到 \"accuracy spread 4.65pp\"。能否提供 per-rank accuracy 数据（r=4, 16, 64）和对应的 feature importance rankings？rank 对 EDD 有影响吗？\n\nQ2. Cross-scale 中 Qwen2.5-7B 的 U-shaped AUC 恢复（d2v3=0.709 → d3v4=0.732 → d4v5=0.772）是否可能反映 instruction-tuning data 在 d3+ 深度引入了训练数据中已有的 pattern？base Qwen2.5-7B 的 AUC trajectory 是否也是 U-shaped？\n\nQ3. GPT-2 XL 的 d3v4 AUC 恰好等于 threshold 0.750（p=0.505）。如果使用 one-sided test H₀: AUC ≤ 0.75，这是 null result。你们是否考虑过在 EDD 定义中引入 statistical significance 要求（如 AUC > T AND p < α）？\n\nQ4. C4 FPR 分析假设所有 passages 为 human-written。考虑到 C4 的时间范围，这一假设在 2023+ 数据上是否仍然合理？是否有子集分析（如按 document date 分层）？\n\nQ5. Curation PoC（Appendix §A.6）中 RF-filtered vs unfiltered 无显著差异（p=0.407）。这是否因为 Pythia-1.4B 在 depth 0-3 数据上的 depth signal 本身太弱以至于过滤不产生质量差异？还是因为 downstream task（perplexity evaluation on Pythia-410M）对 training data quality 不够敏感？\n\n---\n\n## (4) Preliminary Scores\n\n| Dimension | Score | Justification |\n|-----------|-------|---------------|\n| **Soundness** | 3.5/5 | 核心方法论正确：EDD 定义严谨、feature importance 通过三种 measures 验证、domain bias control 充分。但 Table 2/5 缺 CI（persistent issue）、accumulation 和 quality-control 实验缺失削弱 ecological validity claims。GPT-2 XL EDD=4 at p=0.505 是统计 boundary case。 |\n| **Excitement** | 3.5/5 | Ordinal depth estimation 是真正的文献空白。Strategy-dependent trajectories 和 \"memorization as prerequisite\" insight（Appendix §A.4: τ=1.1 collapse）是有趣的 empirical finding。但 practical applicability 受限于 (a) strategy-conditioned 需求未实现、(b) curation PoC inconclusive、(c) wild-data FPR 高达 22.4%。 |\n| **Overall** | 3.5/5 | 论文相比前轮有实质性改善：Related Work 补全、LoRA rank ablation 新增、Introduction 措辞修正、Discussion curation narrative 诚实化、Abstract 精简。核心贡献（task formalization + atlas + EDD）solid for Findings。主要残余问题：(1) Tables 2/5 缺 CI 是 long-standing gap；(2) accumulation scenario 是 ecological validity 的 hard gap；(3) cross-scale 仅两个 7B+QLoRA 模型（Director summary 描述的 14B FP16 实验不在当前稿件中）。若 Director summary 中的计划内容（14B、prompted、two-stage pipeline、RedPajama/Dolma）能实际纳入论文，Overall 可升至 4.0。 |\n\n**Confidence**: 4/5 — 对 method/experiments 维度有高置信度；对 Director summary 中描述但不在 tex 中的内容无法评判。\n\n---\n\n### 相比 Round 8 的变化追踪\n\n| Issue | Round 8 状态 | 当前状态 | 变化 |\n|-------|-------------|---------|------|\n| R5-W4 (Related Work 遗漏) | ❌ NOT ADDRESSED | ✅ RESOLVED | 全部补齐 |\n| R1-W3 (LoRA rank) | ❌ NOT ADDRESSED | ✅ RESOLVED | rank 4-64 ablation |\n| R2-N2 (novelty positioning) | ⚠️ | ✅ RESOLVED | Dohmatob explicit positioning |\n| R2-N3 (Abstract overload) | ⚠️ | ✅ RESOLVED | 精简，无内部引用 |\n| R2-W1 (universal overclaim) | ⚠️ | ✅ RESOLVED | 改为 \"consistent in direction but scale-dependent\" |\n| R2-W2 (curation \"enables\") | ⚠️ | ✅ RESOLVED | 改为 \"inconclusive\" |\n| R1-N2 (Table CI) | ⚠️ PARTIAL | ⚠️ STILL PARTIAL | Table 2/5 仍缺 |\n| R4-N1 (EDD stat qualification) | ⚠️ PARTIAL | ✅ IMPROVED | Abstract 更简洁，详情在正文 |\n| R7-W3 (accumulation) | ❌ NOT ADDRESSED | ❌ STILL MISSING | |\n| R7-W4 (quality control) | ❌ NOT ADDRESSED | ❌ STILL MISSING | |\n| R5-W5 (EDD operational) | ⚠️ PARTIAL | ⚠️ STILL PARTIAL | |\n\n**总结**：论文在 Related Work、novelty positioning、Abstract 质量、LoRA ablation、reference model ablation、Discussion 诚实性上有实质进步。核心残余：(1) Tables 缺 CI；(2) accumulation + quality-control experiments；(3) Director 描述的 14B/prompted/two-stage/RedPajama 内容未落地到 tex 文件。",
    "reviewer_id": "1",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 437 · 2026-05-17T08:49:56.346556+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4274
}
```

</details>

---


### Assistant

_source line 438 · 2026-05-17T08:50:02.521700+00:00_

审稿报告已提交。

核心发现：
1. 论文相比 Round 8 有实质改善（Related Work 补全、LoRA rank ablation、Abstract 精简、novelty positioning 修正）
2. **主要不一致**：Director 的 paper summary 描述了不在当前 tex 文件中的内容（14B 实验、prompted generation、two-stage pipeline、RedPajama-v2/Dolma 分析、不同标题）
3. 残余问题：Tables 2/5 仍缺 CI、accumulation 和 matched-quality control 实验缺失
4. 评分：Soundness 3.5, Excitement 3.5, Overall 3.5——若 Director 描述的计划内容能落地，可升至 4.0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1"
}
```

</details>

---


## Round 16

## Round 16

14 recorded events


### User

_source line 439 · 2026-05-17T08:54:59.995310+00:00_

[Round 9 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 的修订版审稿意见

以下是 Reviewer 2 对修订版论文的完整审稿。请逐条回应 Must-Fix 和 Should-Fix：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

## Reviewer 2 报告摘要

**Overall**: 3.5/5 (Borderline accept, leaning accept for Findings)

### Must-Fix

**N1** [critical] Reference model 消融表格与正文 claim 不一致
- method.tex line 41 和 conclusion.tex line 39 均声称 "67-79% across three reference architectures"
- 但 Table 16 (Appendix §C.5) 仅有 2 行数据（Pythia-1.4B: 78.6%, OLMo-1B: 74.5%），GPT-2 XL reference 结果完全缺失
- 构成 claim 与 evidence 的直接矛盾

### Should-Fix

**W1** "signal universality" overclaim 仍在 generalization.tex line 108
**W2** Abstract "70-85%" 向上取整（实际下界 69.6%）
**W3** Contribution bullet 3 信息过载（7+ axes + 数字堆叠）
**W4** 跨策略迁移实用性瓶颈讨论不足（d1-d3 仅 45.9%，two-stage pipeline 仅 mentioned 未实现）
**W5** 2 个 orphan bib 条目（c2pa2024, chen2024spin）

### 新发现

- RAID benchmark（Dugan et al., ACL 2024）未引用
- Abstract 括号内列举不完整（只列 3/7 axes）
- Curation PoC threshold sensitivity 缺失

### R2 对修订版的评价

- Related Work 显著改善（Schaeffer, McCullagh, CCNet 等补全）✅
- Novelty positioning 准确（Dohmatob "operationalize" framing）✅
- Discussion curation 叙事诚实化 ✅
- Em-dash 全部清除 ✅
- "universal and scale-variant" 矛盾修正 ✅

---

请特别关注 N1（Table 16 数据缺失）是否构成 blocking issue，以及你对 W4（cross-strategy 实用性）的判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 440 · 2026-05-17T08:55:09.546362+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "67.*79|three reference|ref_ablation|GPT-2.*reference|reference.*GPT",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "67.*79|three reference|ref_ablation|GPT-2.*reference|reference.*GPT",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 441 · 2026-05-17T08:55:09.949682+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:296:\label{app:ref_ablation}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:301:\label{tab:ref_ablation}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.fdb_latexmk:41:  "/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmex10.tfm" 1136768653 992 662f679a0b3d2d53c1b94050fdaa3f50 ""
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.fdb_latexmk:49:  "/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr6.tfm" 1136768653 1300 b62933e007d01cfd073f79b963c01526 ""
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.fdb_latexmk:55:  "/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmsy9.tfm" 1136768653 1116 25a7bf822c58caf309a702ef79f4afbb ""
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.fdb_latexmk:59:  "/usr/share/texlive/texmf-dist/fonts/tfm/public/latex-fonts/lasy7.tfm" 1136768653 520 a74c6ed8cb48679fdc3ea874d9d34a7e ""
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.fdb_latexmk:81:  "/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb" 1136849748 44729 811d6c62865936705a31c797a1d5dada ""
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.fdb_latexmk:146:  "/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg" 1279039959 678 4792914a8f45be57bb98413425e4c7af ""
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.fdb_latexmk:155:  "/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty" 1731446765 6696 886c9f3087d0b973ed2c19aa79cb3023 ""
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.
…[truncated 1499 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 442 · 2026-05-17T08:55:10.401963+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "signal universality",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "signal universality",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 443 · 2026-05-17T08:55:10.452688+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex:108:Cross-model recursive chains (84.75\%), validated by a reverse-chain control (85.75\%; Appendix~\ref{app:cross_boundary}), and cross-domain transfer (arXiv 74.1\%) further confirm signal universality.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 444 · 2026-05-17T08:55:11.055389+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "c2pa2024|chen2024spin",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "c2pa2024|chen2024spin",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 445 · 2026-05-17T08:55:11.106286+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib:495:@misc{c2pa2024,
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib:549:@inproceedings{chen2024spin,

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 446 · 2026-05-17T08:55:21.916734+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "c2pa|chen2024spin|spin",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "c2pa|chen2024spin|spin",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 447 · 2026-05-17T08:55:22.325215+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 408
}
```

</details>

---


### Tool call

_source line 448 · 2026-05-17T08:55:22.376115+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
  "offset": "295",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
    "offset": "295",
    "limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 449 · 2026-05-17T08:55:22.426804+00:00_

295	\subsection{Reference Model Ablation}
296	\label{app:ref_ablation}
297	
298	\begin{table}[h]
299	\centering
300	\caption{Reference model ablation. Classification accuracy (5-fold CV) on Pythia-1.4B generated text (nucleus, d0--d3) using different reference models for feature extraction.}
301	\label{tab:ref_ablation}
302	\begin{tabular}{lcc}
303	\toprule
304	Reference Model & Architecture & Accuracy (\%) \\
305	\midrule
306	Pythia-1.4B (self) & GPT-NeoX & 78.6 $\pm$ 0.6 \\
307	OLMo-1B (cross) & OLMo & 74.5 $\pm$ 0.7 \\
308	\bottomrule
309	\end{tabular}
310	\end{table}
311	
312	\subsection{Cross-Scale Full Results}
313	\label{app:cross_scale_full}
314	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 450 · 2026-05-17T08:56:21.975256+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 9 交叉回应 — Reviewer 1 对 Reviewer 2 修订版审稿\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-N1: Reference model 消融表格与正文 claim 不一致**\n\n完全同意，这是 blocking issue。我独立验证了以下事实：\n\n1. **method.tex line 41**: \"Ablations with OLMo-1B **and GPT-2 XL** as alternative references yield **67--79%** accuracy\"\n2. **conclusion.tex line 39**: \"accuracy ranging from **67--79%** across **three** reference architectures\"\n3. **Table 16 (tab:ref_ablation, section_appendix.tex lines 298-310)**: 仅有 **2 行**数据——Pythia-1.4B (78.6±0.6%) 和 OLMo-1B (74.5±0.7%)。**GPT-2 XL 作为 reference model 的数据完全缺失。**\n\n这是直接的 claim-evidence 矛盾：\n- \"67%\" 的下界必须来自 GPT-2 XL reference 数据，但该数据不在表中\n- \"three reference architectures\" 与表中 2 行数据不符\n- Introduction contribution bullet 3 也提到 \"reference model robustness (67--79% accuracy across three reference models)\"\n\n这不是措辞问题而是 **数据缺失**。可能的情况：(a) GPT-2 XL reference 实验已完成但结果遗漏入表；(b) 实验未完成但文字 claim 先行写入。无论哪种，作为审稿人我无法验证 \"67%\" 这一数字的真实性。\n\n**建议**：必须在 Table 16 补入 GPT-2 XL reference 数据行，或将所有正文 claim 修改为仅覆盖现有两个 reference models。这应在提交前立即修复。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: \"signal universality\" overclaim 仍在 generalization.tex line 108**\n\n确认。原文：\"Cross-model recursive chains (84.75%)... further confirm signal universality.\" 这是从 Round 8 以来的遗留问题。虽然 Introduction 已将 \"universal\" 修正为 \"consistent in direction but scale-dependent in magnitude\"，但 generalization.tex 中此处遗漏了同步修改。\n\nCross-strategy transfer 仅 59.1%（d1-d3: 45.9%），cross-τ 仅 46.7%。\"Signal universality\" 在这些数据下仍是 overclaim。建议改为 \"signal robustness across model boundaries\" 或 \"cross-model signal persistence\"。\n\n---\n\n**[AGREE] R2-W2: Abstract \"70-85%\" 向上取整**\n\n同意。我在 Round 8 也标记了此问题（当时的 N1）。Table 2 实际范围 69.6%--85.4%，将 69.6% 取整为 70% 仍未修复。建议改为 \"approximately 70--85%\" 或 \"69.6--85.4%\"。问题不大但容易修复。\n\n---\n\n**[AGREE] R2-W3: Contribution bullet 3 信息过载**\n\n同意。Introduction contribution bullet 3（introduction.tex lines 28-29）在一个 bullet 中堆叠 7 个 generalization axes + 对应数字，读起来像 results summary。这是从 Round 8 R2-W4 以来的遗留问题。建议拆分为 (a) 列出 axes 名称，(b) 将数字移至正文各节。\n\n---\n\n**[AGREE] R2-W4: 跨策略迁移实用性瓶颈讨论不足**\n\n同意，并认为这是比 R2 评估更重要的问题。\n\n核心数据：\n- Cross-strategy d1-d3 accuracy: 45.9%（chance=33%, 仅 1.38×）\n- Temperature holdout d1v2 AUC 低至 0.129（GPT-2 XL, §5.3 Table 7）\n- Cross-τ LOO transfer: 46.7%（Appendix §A.4）\n\nLimitations 仅提到 \"a two-stage pipeline... is needed\" 但未实现。这是论文声称的核心应用场景（\"depth-graduated data curation\"）的实际部署瓶颈：在真实 web data 中，decoding strategy 通常未知。如果不知道 strategy，分类器可能产生 inverted depth predictions（d1v2 AUC < 0.5），这比不做分类更糟糕。\n\n我在 Round 1 审稿中也标记了此问题（W9: two-stage pipeline 不存在于论文中）。建议至少在 Limitations 中更强调这一实际部署障碍，或实现一个 minimal two-stage pipeline proof-of-concept。\n\n---\n\n**[AGREE] R2-W5: 2 个 orphan bib 条目**\n\n确认。我独立验证：\n- `c2pa2024` (C2PA Technical Specification): 在 references.bib line 495 但未在任何 .tex 文件中被 `\\cite`\n- `chen2024spin` (Self-Play Fine-Tuning): 在 references.bib line 549 但未在任何 .tex 文件中被 `\\cite`\n\n两者均为 orphan entries。可能是修订过程中加入 bib 但未完成正文引用。如果打算引用（如 C2PA 用于 provenance toolkit 讨论），需在正文添加 `\\cite`；否则从 .bib 删除以避免 ACL camera-ready 检查工具报错。\n\n---\n\n### R2 新发现\n\n**[AGREE] RAID benchmark 未引用**\n\n同意。Dugan et al. 2024 \"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors\" (ACL 2024) 是 AI text detection 的主要 benchmark。论文 Related Work §2 \"AI Text Detection\" 段引用了 M4-SemEval 和 LOKI 作为 benchmark，但遗漏了 RAID。考虑到 RAID 的影响力，应补充引用。\n\n**[AGREE] Abstract 括号内列举不完整**\n\n同意。Abstract line 6 写 \"including cross-scale with 7B models at 70.2%, cross-domain, and LoRA-rank ablation\"，仅列举 3/7 axes。建议要么列出所有 7 个 axis 名称（不带数字），要么改为 \"including cross-model, cross-scale, and cross-domain transfer\"（选最重要的 3 个即可，但当前选择的 3 个不是最具代表性的——cross-model transfer 比 LoRA-rank ablation 更重要但未列出）。\n\n**[REBUT] Curation PoC threshold sensitivity 缺失**\n\n部分反驳。R2 指出 curation PoC 缺 threshold sensitivity 分析。但考虑到 (a) PoC 本身已报告为 inconclusive（Discussion line 7），(b) RF-filtered vs unfiltered p=0.407 已是 null result，在一个已经 inconclusive 的 PoC 上要求 threshold sensitivity 分析投入产出比不高。如果作者选择扩展 curation 实验（如使用更大 downstream model 或更敏感的 downstream task），那么 threshold sensitivity 会变得有意义。但在当前 null-result 状态下，额外分析不会改变结论。\n\n---\n\n### 总结\n\nR2 的 5 条 Should-Fix 和 1 条 Must-Fix 中，我 **5/6 完全同意**，1 条（Curation threshold sensitivity）部分反驳。\n\n**R2-N1 是 blocking issue**——这是数据与 claim 的直接矛盾，不是措辞问题。Table 16 必须补入 GPT-2 XL reference 数据或修改所有 \"three reference architectures\" / \"67-79%\" 的正文声明。\n\n我在 Round 1 审稿中标记的 W12（accumulation scenario）和 W13（quality-control confound）是 R2 未覆盖的独立方法学问题，仍然有效。",
  "reviewer_id": "1",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 9 交叉回应 — Reviewer 1 对 Reviewer 2 修订版审稿\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-N1: Reference model 消融表格与正文 claim 不一致**\n\n完全同意，这是 blocking issue。我独立验证了以下事实：\n\n1. **method.tex line 41**: \"Ablations with OLMo-1B **and GPT-2 XL** as alternative references yield **67--79%** accuracy\"\n2. **conclusion.tex line 39**: \"accuracy ranging from **67--79%** across **three** reference architectures\"\n3. **Table 16 (tab:ref_ablation, section_appendix.tex lines 298-310)**: 仅有 **2 行**数据——Pythia-1.4B (78.6±0.6%) 和 OLMo-1B (74.5±0.7%)。**GPT-2 XL 作为 reference model 的数据完全缺失。**\n\n这是直接的 claim-evidence 矛盾：\n- \"67%\" 的下界必须来自 GPT-2 XL reference 数据，但该数据不在表中\n- \"three reference architectures\" 与表中 2 行数据不符\n- Introduction contribution bullet 3 也提到 \"reference model robustness (67--79% accuracy across three reference models)\"\n\n这不是措辞问题而是 **数据缺失**。可能的情况：(a) GPT-2 XL reference 实验已完成但结果遗漏入表；(b) 实验未完成但文字 claim 先行写入。无论哪种，作为审稿人我无法验证 \"67%\" 这一数字的真实性。\n\n**建议**：必须在 Table 16 补入 GPT-2 XL reference 数据行，或将所有正文 claim 修改为仅覆盖现有两个 reference models。这应在提交前立即修复。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: \"signal universality\" overclaim 仍在 generalization.tex line 108**\n\n确认。原文：\"Cross-model recursive chains (84.75%)... further confirm signal universality.\" 这是从 Round 8 以来的遗留问题。虽然 Introduction 已将 \"universal\" 修正为 \"consistent in direction but scale-dependent in magnitude\"，但 generalization.tex 中此处遗漏了同步修改。\n\nCross-strategy transfer 仅 59.1%（d1-d3: 45.9%），cross-τ 仅 46.7%。\"Signal universality\" 在这些数据下仍是 overclaim。建议改为 \"signal robustness across model boundaries\" 或 \"cross-model signal persistence\"。\n\n---\n\n**[AGREE] R2-W2: Abstract \"70-85%\" 向上取整**\n\n同意。我在 Round 8 也标记了此问题（当时的 N1）。Table 2 实际范围 69.6%--85.4%，将 69.6% 取整为 70% 仍未修复。建议改为 \"approximately 70--85%\" 或 \"69.6--85.4%\"。问题不大但容易修复。\n\n---\n\n**[AGREE] R2-W3: Contribution bullet 3 信息过载**\n\n同意。Introduction contribution bullet 3（introduction.tex lines 28-29）在一个 bullet 中堆叠 7 个 generalization axes + 对应数字，读起来像 results summary。这是从 Round 8 R2-W4 以来的遗留问题。建议拆分为 (a) 列出 axes 名称，(b) 将数字移至正文各节。\n\n---\n\n**[AGREE] R2-W4: 跨策略迁移实用性瓶颈讨论不足**\n\n同意，并认为这是比 R2 评估更重要的问题。\n\n核心数据：\n- Cross-strategy d1-d3 accuracy: 45.9%（chance=33%, 仅 1.38×）\n- Temperature holdout d1v2 AUC 低至 0.129（GPT-2 XL, §5.3 Table 7）\n- Cross-τ LOO transfer: 46.7%（Appendix §A.4）\n\nLimitations 仅提到 \"a two-stage pipeline... is needed\" 但未实现。这是论文声称的核心应用场景（\"depth-graduated data curation\"）的实际部署瓶颈：在真实 web data 中，decoding strategy 通常未知。如果不知道 strategy，分类器可能产生 inverted depth predictions（d1v2 AUC < 0.5），这比不做分类更糟糕。\n\n我在 Round 1 审稿中也标记了此问题（W9: two-stage pipeline 不存在于论文中）。建议至少在 Limitations 中更强调这一实际部署障碍，或实现一个 minimal two-stage pipeline proof-of-concept。\n\n---\n\n**[AGREE] R2-W5: 2 个 orphan bib 条目**\n\n确认。我独立验证：\n- `c2pa2024` (C2PA Technical Specification): 在 references.bib line 495 但未在任何 .tex 文件中被 `\\cite`\n- `chen2024spin` (Self-Play Fine-Tuning): 在 references.bib line 549 但未在任何 .tex 文件中被 `\\cite`\n\n两者均为 orphan entries。可能是修订过程中加入 bib 但未完成正文引用。如果打算引用（如 C2PA 用于 provenance toolkit 讨论），需在正文添加 `\\cite`；否则从 .bib 删除以避免 ACL camera-ready 检查工具报错。\n\n---\n\n### R2 新发现\n\n**[AGREE] RAID benchmark 未引用**\n\n同意。Dugan et al. 2024 \"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors\" (ACL 2024) 是 AI text detection 的主要 benchmark。论文 Related Work §2 \"AI Text Detection\" 段引用了 M4-SemEval 和 LOKI 作为 benchmark，但遗漏了 RAID。考虑到 RAID 的影响力，应补充引用。\n\n**[AGREE] Abstract 括号内列举不完整**\n\n同意。Abstract line 6 写 \"including cross-scale with 7B models at 70.2%, cross-domain, and LoRA-rank ablation\"，仅列举 3/7 axes。建议要么列出所有 7 个 axis 名称（不带数字），要么改为 \"including cross-model, cross-scale, and cross-domain transfer\"（选最重要的 3 个即可，但当前选择的 3 个不是最具代表性的——cross-model transfer 比 LoRA-rank ablation 更重要但未列出）。\n\n**[REBUT] Curation PoC threshold sensitivity 缺失**\n\n部分反驳。R2 指出 curation PoC 缺 threshold sensitivity 分析。但考虑到 (a) PoC 本身已报告为 inconclusive（Discussion line 7），(b) RF-filtered vs unfiltered p=0.407 已是 null result，在一个已经 inconclusive 的 PoC 上要求 threshold sensitivity 分析投入产出比不高。如果作者选择扩展 curation 实验（如使用更大 downstream model 或更敏感的 downstream task），那么 threshold sensitivity 会变得有意义。但在当前 null-result 状态下，额外分析不会改变结论。\n\n---\n\n### 总结\n\nR2 的 5 条 Should-Fix 和 1 条 Must-Fix 中，我 **5/6 完全同意**，1 条（Curation threshold sensitivity）部分反驳。\n\n**R2-N1 是 blocking issue**——这是数据与 claim 的直接矛盾，不是措辞问题。Table 16 必须补入 GPT-2 XL reference 数据或修改所有 \"three reference architectures\" / \"67-79%\" 的正文声明。\n\n我在 Round 1 审稿中标记的 W12（accumulation scenario）和 W13（quality-control confound）是 R2 未覆盖的独立方法学问题，仍然有效。",
    "reviewer_id": "1",
    "project": "recursive_gen_depth_est"
  }
}
```

</details>

---


### Tool result

_source line 451 · 2026-05-17T08:56:25.692003+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3716
}
```

</details>

---


### Assistant

_source line 452 · 2026-05-17T08:56:33.773373+00:00_

审稿意见已提交。

核心发现：R2-N1 confirmed as blocking issue——Table 16 仅 2 行数据（Pythia, OLMo）但正文在 3 处声称 "three reference architectures" 和 "67-79%"。GPT-2 XL 作为 reference 的数据完全缺失。其余 5 条 Should-Fix 中 4 条完全同意，1 条（curation threshold sensitivity）部分反驳。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1"
}
```

</details>

---


## Round 17

## Round 17

46 recorded events


### User

_source line 453 · 2026-05-18T14:10:05.974600+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1

**你的审查侧重：方法严谨性 + 实验设计**

### 论文信息
- **标题**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
- **路径**: `projects/recursive_gen_depth_est/docs/paper/main.tex`（主文件在 `docs/paper/` 目录，含 abstract.tex, introduction.tex, related_work.tex, method.tex, atlas.tex, generalization.tex, discussion.tex, conclusion.tex, section_appendix.tex）
- **目标 Venue**: EMNLP 2026（ARR May 2026 cycle）
- **截止日期**: 2026-05-25

### Venue 格式要求
- Long paper: 8 页正文 + 无限 references
- 模板: ACL LaTeX, `\usepackage[review]{acl}`
- 匿名: double-blind
- 附录: 必须 double-column format
- Overall Assessment 评分: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

### 你的审查重点

请从以下维度严格评审：

1. **问题定义与形式化**
   - Recursive generation depth estimation 作为 ordinal classification 的形式化是否严谨？
   - EDD (Effective Discriminable Depth) 定义（Eq. 1）是否数学上完备、无歧义？
   - 是否有边界情况未处理？

2. **实验设计**
   - Benchmark 构建（3 models × 3 strategies × 4 depths, 180K samples）是否充分？
   - LoRA fine-tuning pipeline 是否合理？参数选择是否有充分依据？
   - 5-fold stratified CV 是否存在信息泄漏风险？
   - Cross-validation 分组策略是否正确？

3. **统计严谨性**
   - 主实验结果是否有适当的统计量（CI、显著性检验）？
   - EDD 的 bootstrap testing 是否方法合理、报告完整？
   - Feature importance 方法（Gini vs SHAP vs permutation）的一致性检验是否充分？
   - 多重比较问题是否被处理？

4. **消融实验完整性**
   - Feature ablation 是否系统？
   - Reference model ablation 是否充分？
   - 是否存在应做但未做的关键 ablation？

5. **泛化实验**
   - Cross-model/cross-strategy/cross-scale 实验设计是否有方法论问题？
   - Cross-scale (7-8B) 实验的 confounds 是否被充分讨论？
   - Prompted generation 验证是否充分？

6. **可复现性**
   - 实验细节是否足够复现？
   - 代码/数据是否承诺发布？

### 输出格式

请按以下结构输出审稿意见：

```
## Summary（2-3 句）

## Strengths（逐条）

## Weaknesses（逐条，按严重程度排序：Must-Fix / Should-Fix / Minor）

## Questions（需要作者回答的问题）

## Missing References（如有）

## Overall Assessment
- 评分（使用 ARR 5 分制）
- 置信度（1-5）
- 简要理由
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 454 · 2026-05-18T14:10:14.798823+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---
