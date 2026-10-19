# Reviewer 1 coordination — Part 1 of 4

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Conversation logs

[Transcript overview](../reviewer-1-coordination.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/4b/4bf7b0cbf90edc59b291.json)

## Round 1

## Round 1

30 recorded events


### User

_source line 1 · 2026-05-16T18:55:32.659455+00:00_

[Round 1 审稿请求]:
## 审稿任务分配 — Reviewer 1

**论文**: "Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs"
**目标 Venue**: EMNLP 2026 (Main Conference, Efficient Methods for NLP track)
**ARR 提交截止**: 2026-05-25
**格式**: Long paper, ≤8 页正文 + 无限参考文献, ACL 模板, double-blind
**匿名规则**: 严格 double-blind, 禁止自引暴露身份

**论文路径**: `projects/distill_sparse_swiglu/paper/main.tex`
（子文件: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex）

---

### 你的审查侧重：方法严谨性 + 实验设计

请重点审查以下方面：

1. **方法论正确性**
   - §3.5 梯度分析（BCE vs KL）的数学推导是否正确？链式法则展开是否准确？
   - Gumbel-Sigmoid relaxation 的使用是否恰当？温度退火策略的理论依据？
   - Lagrangian 约束的对偶更新公式是否有收敛保证？

2. **实验设计严谨性**
   - 训练 setup（1000 steps, WikiText-103, batch=4）是否充分？是否存在过拟合 WikiText-2 评估集的风险？
   - Iso-compute 对比（BCE 2700 steps vs KL 1000 steps）是否公平？BCE 的超参是否经过充分调优？
   - Multi-seed 稳定性（3 seeds, std=0.07）的种子数是否足够？
   - "Relative advantage" 的计算方式是否合理（(TEAL-KL)/TEAL × 100%）？

3. **统计声明与数值一致性**
   - 论文中多处重复出现的数字（11.79, 23.31, 27.97 等）在不同 section 间是否一致？
   - "18% at 30%, 49% at 50%, 82% at 70%" — 验证这些百分比计算
   - SPON 贡献 "2.4% relative improvement (12.08→11.79)" — 验证 (12.08-11.79)/12.08
   - Appendix latency 数字与正文 claims 是否一致（6.4% overhead, 2.7% predictor）

4. **消融实验充分性**
   - 缺少哪些关键消融？（例如：bottleneck 维度 d_b 的敏感性？温度退火 schedule 的影响？训练步数的影响曲线？）
   - Gumbel vs STE 的对比是否充分？是否有其他 relaxation 方法应该对比？

5. **Claim 强度 vs 证据**
   - "eliminates the need for error compensation" — 证据是否足够支撑？
   - "structural failure, not computational" — BCE 是否给了公平的超参搜索？
   - Cross-architecture 声明只有 Mistral 一个额外模型，是否过度泛化？

请输出完整审稿报告，包含 Strengths、Weaknesses (逐条编号)、Questions、Overall Assessment。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-16T18:55:42.928462+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
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

_source line 3 · 2026-05-16T18:55:42.979045+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-16T18:55:46.391707+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 5 · 2026-05-16T18:55:47.295369+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 6 · 2026-05-16T18:55:47.295723+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	
17	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
18	
19	\author{Anonymous}
20	
21	\begin{document}
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
32	\input{conclusion}
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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 7 · 2026-05-16T18:55:48.316199+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 8 · 2026-05-16T18:55:48.367059+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models.
5	The method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass, eliminating the need for auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{h}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importance scores from the pre-FFN hidden state $\mathbf{h}$.
26
…[truncated 12973 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 9 · 2026-05-16T18:55:48.367498+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 10 · 2026-05-16T18:55:48.419570+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4, using AdamW with learning rate $1 \times 10^{-3}$ and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly; (2) \textbf{BCE predictor}, trained with per-neuron binary cross-entropy loss for 1000 and 2700 steps; (3) \textbf{Uniform allocation}, which distributes the sparsity budget equally across layers; and (4) \textbf{WINA}~\cite{liu2025teal}, an importance-weighted variant.
23	
24	
25	\subsection{Main Results}
26	
27	Table~\ref{tab:main} presen
…[truncated 11401 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-16T18:55:53.399336+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

I found comprehensive information about ACL ARR 2026 reviewer guidelines. Here are the key details:

## Review Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recom
…[truncated 1153 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7007
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-16T18:55:57.605122+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-16T18:55:58.057142+00:00_

1	Activation sparsity can accelerate SwiGLU-based LLMs by pruning FFN neurons at inference, but existing learned predictors trained with binary cross-entropy (BCE) require error compensation networks due to a structural mismatch: BCE decomposes per neuron while inference uses global top-$k$ allocation across all layers.
2	We train lightweight predictors (2.37M parameters per layer, 75.9M total, $<$1\% of the base model) with KL divergence, which couples all neurons through the output distribution via Gumbel-Sigmoid relaxation, eliminating the need for compensation.
3	On LLaMA-3.1-8B (WikiText-2), our KL-trained predictor achieves perplexity 11.79 at 50\% sparsity without compensation, compared to 23.31 for vanilla TEAL and 27.97 for BCE trained at 2.71$\times$ the compute budget, whose loss saturates, confirming a structural rather than computational failure.
4	Three-seed evaluation confirms training stability (PPL $11.92 \pm 0.07$, CV${<}$1\% under uniform allocation).
5	The KL advantage grows disproportionately with sparsity: 18\% relative improvement at 30\%, 49\% at 50\%, and 82\% at 70\%.
6	Cross-architecture evaluation on Mistral-7B-v0.3 yields +63\% degradation from dense, compared to +93\% on LLaMA.
7	SPON's static bias correction proves near-orthogonal to the predictor (cosine similarity 0.196), providing only 2.4\% relative PPL improvement (12.08$\to$11.79 under \texttt{evaluate.py}).
8	We propose a two-dimensional taxonomy over correction granularity $\times$ training signal coupling that unifies prior methods and identify three distinct sparsity regimes---budget-surplus, budget-constrained, and capacity-limited---that govern the quality-sparsity tradeoff.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 14 · 2026-05-16T18:55:58.107822+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-16T18:55:58.559833+00:00_

1	\section{Introduction}
2	
3	SwiGLU feed-forward networks~\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.
4	Exploiting this sparsity can in principle yield substantial inference speedup by pruning 50\% of FFN neurons per token---without modifying the pretrained weights---once structured sparse kernels are available.
5	Yet the gap between potential and practice remains wide.
6	Training-free methods such as TEAL~\cite{liu2025teal} select neurons by activation magnitude alone, degrading perplexity from 6.12 (dense) to 23.31 at 50\% sparsity on LLaMA-3.1-8B~\cite{grattafiori2024llama3}---a 281\% increase.
7	Learned predictors~\cite{liu2023dejavu,gautam2026fastforward} close part of this gap by training small auxiliary networks to anticipate which neurons will be important, but they rely on error compensation modules (output rescaling networks or additive correction layers) that add 67.2M parameters and $\sim$2.7\% additional latency overhead at inference.
8	The question is whether a predictor can be trained so that compensation becomes unnecessary.
9	
10	The answer depends on the training objective.
11	Current learned predictors use binary cross-entropy (BCE) loss: each neuron is independently classified as ``keep'' or ``prune'' against an oracle mask derived from the dense model's activations.
12	The gradient of BCE with respect to neuron $j$'s score is $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$---a function of neuron $j$ alone, independent of every other neuron in the network.
13	But at inference, no neuron is evaluated in isolation.
14	TEAL's global top-$k$ mechanism~\cite{liu2025teal} ranks all neurons across all layers and retains only those above a model-wide threshold.
15	Whether neuron $j$ survives depends not on its own score but on how that score compares to the scores of all $L \times d_{\text{ff}}$ neurons.
16	This cr
…[truncated 4950 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-16T18:55:58.560245+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-16T18:55:59.012790+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude, achieving 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking.
6	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
7	
8	\paragraph{Predictor-Based Contextual Sparsity.}
9	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
10	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with MSE supervision but retains per-neuron decomposition.
11	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction---adding inference latency.
12	PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.
13	All use decomposed (BCE) or intermediate (MSE) objectives where each neuron's gradient is independent of other mask states.
14	Our \emph{coupled} KL objective propagates gradients through all downstream layers, optimizing for global allocation quality without compensation.
15	
16	\paragraph{Static Bias Correction.}
17	SPON~\cite{xu2026spon} learns input-independent bias vectors via KL divergence, absorbed into parameters at zero inference cost.
18	However, static correction cannot adapt to token-specific patterns.
19	We show SPON's vectors are near-orthogonal to our predictor (cosine similarity 0.196), providing only 2.4\% relative PPL improvement (12.08$\to$11.79)---confirming the KL predictor captures most recoverable signal.
20	
21	\paragraph{Activation
…[truncated 623 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-16T18:55:59.013341+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-16T18:55:59.063887+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We have shown that training sparsity predictors with KL divergence eliminates the need for error compensation networks in activation sparsity for LLMs.
5	The mechanism is structural: BCE's per-neuron gradient is independent of other neurons' mask states, creating a mismatch with global top-$k$ inference allocation that no amount of additional training resolves.
6	KL divergence couples all neurons through the output distribution, aligning the training objective with the inference mechanism.
7	The resulting predictor---a two-layer MLP with 2.37M parameters per layer (75.9M total, $<$1\% of the base model)---achieves PPL 11.79 at 50\% sparsity on LLaMA-3.1-8B under TEAL's global allocation, compared to 23.31 for vanilla TEAL and 27.97 for BCE.
8	Three-seed evaluation under uniform allocation confirms training stability (PPL $11.92 \pm 0.07$, CV${<}$1\%).
9	Our two-dimensional taxonomy (correction granularity $\times$ training signal coupling) situates this result within the broader landscape of activation sparsity methods and identifies the previously unexplored cell of per-token contextual prediction with coupled training signals.
10	
11	Several empirical findings deserve emphasis.
12	The KL advantage grows disproportionately with sparsity---18\% relative improvement at 30\%, 49\% at 50\%, and 82\% at 70\%---indicating that distributional coupling becomes increasingly important as more neurons are pruned.
13	The non-monotonic allocation preference reveals three distinct regimes: budget-surplus ($\leq$30\%), where uniform allocation suffices and even outperforms global allocation on MMLU; budget-constrained ($\sim$40\%), where global allocation provides measurable gains; and capacity-limited ($\geq$50\%), where both strategies fail to preserve downstream reasoning.
14	SPON's static bias correction achieves only cosine similarity 0.196 with the predictor's effect and provides only 2.4\% relative PPL improvement (12.08
…[truncated 1817 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-16T18:55:59.465898+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-16T18:55:59.516613+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling), confirming that KL distillation provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The full pipeline adds $\sim$6.4\% 
…[truncated 723 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-16T18:56:05.288542+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review review form 2025 2026 soundness excitement overall score scale 1-5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review review form 2025 2026 soundness excitement overall score scale 1-5"
  }
}
```

</details>

---


### Tool call

_source line 23 · 2026-05-16T18:56:05.590107+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
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

_source line 24 · 2026-05-16T18:56:05.640688+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-16T18:56:11.215107+00:00_

Web search results for query: "ACL Rolling Review review form 2025 2026 soundness excitement overall score scale 1-5"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL 2026 on X: \"Checkout the blog post on the soundness/excitement scores https://t.co/AKSO9DjiYP . It clarifies the reasoning behind the separation of overall scores and how it might make the reviewer recommendation more robust. #ACL2023Toronto #ACL2023NLP #NLProc\" / X","url":"https://x.com/aclmeeting/status/1637827267173953540"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"🎪 ACL 2025 Reviews Are Out: To Rebut or Flee? The Harsh Reality of NLP’s \"Publish or Perish\" Circus | CSPaper Forum","url":"https://forum.cspaper.org/topic/27/acl-2025-reviews-are-out-to-rebut-or-flee-the-harsh-reality-of-nlp-s-publish-or-perish-circus"},{"title":"Conference Decisions · GitHub","url":"https://gist.github.com/antonisa/2158dee79179c7c49304ef353887bfa0"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Ba
…[truncated 1409 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 5926
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-16T18:56:15.533275+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete scoring scales for: 1) Soundness (all levels 1-5 with descriptions), 2) Excitement (all levels 1-5 with descriptions), 3) Overall recommendation (all levels with descriptions). Also extract any other scored dimensions like reproducibility, confidence, etc."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete scoring scales for: 1) Soundness (all levels 1-5 with descriptions), 2) Excitement (all levels 1-5 with descriptions), 3) Overall recommendation (all levels with descriptions). Also extract any other scored dimensions like reproducibility, confidence, etc."
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-16T18:56:27.529894+00:00_

# ACL Rolling Review Scoring Scales

## 1) Soundness
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 2) Excitement
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

## 3) Overall Assessment
- **5**: Consider for Award (top 2.5% papers)
- **4**: Conference acceptance recommended
- **3**: Findings track acceptance recommended
- **2**: Resubmit next cycle with substantial revisions
- **1.5**: Resubmit after next cycle (major revisions needed)
- **1**: Do not resubmit (fundamentally flawed or off-topic)

## Additional Scored Dimensions
- **Reviewer Confidence** (1-5 scale)
- **Reproducibility** (1-5 scale)
- **Datasets** (1-5 scale, if applicable)
- **Software** (1-5 scale, if applicable)
- **Author Identity Knowledge** (1-5 scale)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 11996
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-16T18:59:05.079064+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿报告\n\n**论文**: \"Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\"\n**Venue**: EMNLP 2026 Main Conference (Efficient Methods for NLP track)\n\n---\n\n## 总体评分\n\n**Overall**: 3 (Findings track acceptance recommended)\n**一句话总结**: 核心 idea（用 KL 替代 BCE 训练 sparsity predictor）合理且有实验支撑，但实验规模过小、关键消融缺失、\"structural failure\"声明证据不足，且论文未实现任何实际加速。\n\n---\n\n## 官方维度打分（ACL ARR Review Form, 2025-2026）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心 claim 有基本实验支撑，但\"structural failure\"断言缺少充分 hyperparameter search 证据；梯度分析是 informal argument 而非 formal proof；Lagrangian 无收敛分析 |\n| Excitement | 3/5 | KL+Gumbel-Sigmoid 用于 sparsity predictor 训练是 reasonable contribution，但实际未实现 wall-clock 加速，限制了实践影响力 |\n| Reproducibility | 4/5 | 训练 setup 清晰（1000 steps, WikiText-103, batch=4, AdamW），代码细节足够复现，但缺少关键超参（η_λ, Gumbel noise scale） |\n| Confidence | 4/5 | 本 reviewer 熟悉 activation sparsity、知识蒸馏和 Gumbel relaxation 文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 训练/评估数据同源，存在过拟合风险\n\n- 具体位置：§4.1 Training & Evaluation\n- 问题：训练数据为 WikiText-103，评估指标为 WikiText-2 perplexity。两者来自同一 Wikipedia 数据源，共享领域分布和文本风格。在仅 1000 steps（~8M tokens）的极少训练量下，predictor 可能学到 WikiText 特有的 neuron importance pattern 而非通用 pattern。论文的 primary metric（PPL 11.79 vs 23.31）完全依赖此评估，但未提供任何 out-of-domain 评估（如 C4、The Pile test set）来排除过拟合。\n- 为什么影响接收：如果 PPL improvement 主要来自 domain overfitting，核心 contribution 不成立。\n- 建议修改方向：至少补充一个 out-of-domain PPL 评估（C4 或 Pile test），或在不同训练数据上训练后评估 WikiText-2。\n\n**N2** [critical] \"Structural failure, not computational\" 声明缺少充分证据\n\n- 具体位置：§4.2 (Iso-Compute Analysis), §3.5 最后一段\n- 问题：论文断言 BCE 的失败是\"structural\"而非\"computational\"，证据是：(a) 2700 steps 后仍不如 KL 1000 steps; (b) BCE loss 在 500-2700 steps 间仅下降 0.006。但这不排除以下可能性：\n  1. BCE 需要不同的 learning rate / schedule（论文未报告 BCE 的 LR 是否做过搜索）\n  2. BCE 需要更大的 predictor architecture（也许 d_b=256 或 512 对 BCE 更关键）\n  3. BCE loss 饱和可能仅说明当前 LR 太小或处于 local minimum\n  4. \"Loss saturation\"不等于\"structural limitation\"——任何已收敛的模型都有 loss saturation\n\n  论文只试了**一个** BCE configuration 就做出\"structural\"断言。对比之下，KL 用了 Gumbel relaxation + Lagrangian constraint + temperature annealing 等多个 tricks。\n- 为什么影响接收：这是论文的核心 narrative，如果证据不足，贡献被严重削弱。\n- 建议修改方向：(1) 对 BCE 做基本的 hyperparameter search（至少 LR grid + architecture size），报告所有结果；(2) 或弱化 claim 为\"under our setting, KL is significantly more effective\"而非绝对的\"structural failure\"。\n\n**N3** [critical] 消融实验严重不足\n\n- 具体位置：Table 3 (§4.3)\n- 问题：消融表只有 4 行，对一个有多个 design choice 的方法论文远远不够。关键缺失：\n  1. **Bottleneck 维度 d_b 的敏感性**：论文选 d_b=128 无任何理由，不知 64/256/512 的效果如何\n  2. **温度退火 schedule**：cosine 从 1.0→0.1 完全无 justification，无 linear/exponential/fixed 对比\n  3. **训练步数的影响曲线**：1000 steps 是否足够？learning curve 是什么样？\n  4. **Lagrangian learning rate η_λ**：这是关键超参，完全未报告\n  5. **训练数据 domain 的影响**：换 C4 训练会怎样？\n- 为什么影响接收：读者无法判断 method 的鲁棒性和 sensitivity，也无法在自己的场景中 tune。\n- 建议修改方向：至少补充 d_b sensitivity（3-4 个值）和 training steps curve。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 论文实际增加了推理延迟，未实现任何 wall-clock 加速\n\n- 具体位置：§4 最后一段 \"Inference Efficiency\" + Appendix A\n- 问题：论文整体 motivation 是\"accelerate SwiGLU-based LLMs\"（Abstract, §1），但实验表明 pipeline 增加 6.4% latency overhead。Appendix 明确承认\"unstructured element-wise masks...do not translate to wall-clock speedup without sparse kernel support\"。这意味着方法**当前不能加速推理**，只能在假设未来有 sparse kernel 的情况下才有价值。\n- 建议：在 Abstract/Introduction 中更诚实地 frame 贡献为\"prediction quality\"研究而非\"acceleration\"研究，或提供至少一个 sparse kernel 的 PoC。\n\n**W2** [warning] Cross-architecture 验证仅一个模型，泛化 claim 过强\n\n- 具体位置：§4 \"Cross-Architecture Validation\" 段\n- 问题：仅额外评估 Mistral-7B-v0.3 一个模型，就称\"cross-architecture validation\"和\"transferability to other SwiGLU architectures\"。LLaMA-3.1-8B 和 Mistral-7B 都是 ~7-8B SwiGLU decoder-only transformers，极其相似。真正的 cross-architecture 应包括不同 FFN 类型（如 GeGLU）、不同规模（13B/70B）、或不同家族（Qwen、Gemma）。\n- 建议：弱化措辞为\"preliminary evaluation on one additional model\"，或补充一个更不同的架构。\n\n**W3** [warning] 三 seed 稳定性评估 (n=3) 统计效力不足\n\n- 具体位置：§4 \"Training Stability\", Appendix B\n- 问题：3 个 seed（42, 123, 456）得到 std=0.07 是不够的。n=3 时标准误差的估计本身就极不可靠——95% CI for σ 在 n=3 时的宽度约为 [0.45σ, 3.2σ]。无法从 3 个点得出\"training is stable\"的可靠结论。\n- 建议：扩展到至少 5-10 seeds，或明确标注这是 preliminary evidence。\n\n**W4** [warning] 梯度分析（§3.5）是 informal argument，非 formal proof\n\n- 具体位置：§3.5\n- 问题：链式法则展开本身正确，但论文从\"KL gradient depends on all neurons\"跳到\"KL is better\"缺少严格推理。Coupled gradient 也可能带来劣势：(a) gradient variance 更高导致优化困难；(b) high-dimensional Jacobian 的 condition number 可能很差；(c) Gumbel noise 进一步增加 variance。论文没有讨论这些 trade-offs，也没有 formal characterization（如 gradient SNR 对比）。\n- 建议：要么提供 gradient variance/SNR 的实证对比，要么明确标注§3.5为\"intuitive motivation\"而非\"theoretical contribution\"。\n\n**W5** [warning] Lagrangian 对偶更新无收敛保证\n\n- 具体位置：§3.4, Eq. 9-10\n- 问题：对于非凸目标（neural network + Gumbel relaxation），Lagrangian dual ascent 不保证收敛到可行解。论文完全没讨论：(a) λ 是否实际收敛？(b) sparsity constraint 最终是否被满足？(c) 是否有 oscillation？这些在实践中可能不是问题（多数 DL 论文忽略这点），但既然论文把 Lagrangian 作为方法 contribution 之一，应该至少实证展示 λ 和 sparsity ratio 的训练曲线。\n- 建议：Appendix 中补充 λ 和实际 sparsity ratio over training steps 的图。\n\n---\n\n## 小问题（不影响接收）\n\n- \"2.71×\" (§4.2) 应为 2.70× (2700/1000=2.7)，微小数值错误\n- \"saves ~2.7% latency\" (§4 Inference Efficiency): 在 50% sparsity 下实际为 2.46% ((129.71-126.78)/119.11)，2.7% 对应 30% sparsity 的数据。文本未说明使用哪个 sparsity level 的数据\n- Table 1 caption 称\"Multi-seed variance (3 seeds, 50% uniform): PPL std=0.07\"，但 main text 报的 PPL 11.79 是 global allocation (seed=42)。multi-seed 用 uniform allocation 得到 11.92±0.07——这两个数字的区别（11.79 vs 11.92）应该更清楚地解释（footnote 已有但容易混淆）\n- \"Relative advantage\" 定义为 (TEAL-KL)/TEAL，这是一种对方法有利的 metric 选择。相比之下，(TEAL-KL)/(TEAL-Dense) 即\"recovery of degradation\"在某些情况下更有信息量\n\n---\n\n## 主要优势\n\n- **Clear central insight**：BCE per-neuron decomposition vs global top-k inference 的 mismatch 观察敏锐且 well-articulated\n- **Solid core result**：PPL 11.79 vs 23.31 (TEAL) / 27.97 (BCE) 的差距显著且consistent across sparsity levels\n- **Well-structured paper**：2D taxonomy 有效地 situate 了 contribution；三个 sparsity regime 的分析有 insight\n- **Honest limitations section**：论文坦诚承认无 wall-clock speedup、单一规模、PPL 作为 proxy 的局限\n- **Reproducibility**：训练 setup 详细，17 min on A6000，practical for reproduction\n- **Gumbel vs STE ablation**：+3.98 PPL gap 证明 relaxation choice matters\n\n---\n\n## Questions to Authors (for rebuttal)\n\n1. BCE 实验中使用的 learning rate 和 schedule 是什么？是否做过 LR search？\n2. d_b=128 是如何选择的？是否有 preliminary 实验？\n3. 能否提供 C4 test set 或其他 OOD 数据上的 PPL，以排除 WikiText 过拟合？\n4. Lagrangian multiplier λ 在训练过程中的轨迹如何？实际 sparsity ratio 是否精确达到 target？\n5. 如果给 BCE 同样的 Gumbel-Sigmoid + Lagrangian 框架（仅把 KL loss 换成对应的 BCE target），性能如何？这能更 cleanly 隔离 loss function 的贡献 vs 训练框架的贡献。",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿报告\n\n**论文**: \"Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\"\n**Venue**: EMNLP 2026 Main Conference (Efficient Methods for NLP track)\n\n---\n\n## 总体评分\n\n**Overall**: 3 (Findings track acceptance recommended)\n**一句话总结**: 核心 idea（用 KL 替代 BCE 训练 sparsity predictor）合理且有实验支撑，但实验规模过小、关键消融缺失、\"structural failure\"声明证据不足，且论文未实现任何实际加速。\n\n---\n\n## 官方维度打分（ACL ARR Review Form, 2025-2026）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心 claim 有基本实验支撑，但\"structural failure\"断言缺少充分 hyperparameter search 证据；梯度分析是 informal argument 而非 formal proof；Lagrangian 无收敛分析 |\n| Excitement | 3/5 | KL+Gumbel-Sigmoid 用于 sparsity predictor 训练是 reasonable contribution，但实际未实现 wall-clock 加速，限制了实践影响力 |\n| Reproducibility | 4/5 | 训练 setup 清晰（1000 steps, WikiText-103, batch=4, AdamW），代码细节足够复现，但缺少关键超参（η_λ, Gumbel noise scale） |\n| Confidence | 4/5 | 本 reviewer 熟悉 activation sparsity、知识蒸馏和 Gumbel relaxation 文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 训练/评估数据同源，存在过拟合风险\n\n- 具体位置：§4.1 Training & Evaluation\n- 问题：训练数据为 WikiText-103，评估指标为 WikiText-2 perplexity。两者来自同一 Wikipedia 数据源，共享领域分布和文本风格。在仅 1000 steps（~8M tokens）的极少训练量下，predictor 可能学到 WikiText 特有的 neuron importance pattern 而非通用 pattern。论文的 primary metric（PPL 11.79 vs 23.31）完全依赖此评估，但未提供任何 out-of-domain 评估（如 C4、The Pile test set）来排除过拟合。\n- 为什么影响接收：如果 PPL improvement 主要来自 domain overfitting，核心 contribution 不成立。\n- 建议修改方向：至少补充一个 out-of-domain PPL 评估（C4 或 Pile test），或在不同训练数据上训练后评估 WikiText-2。\n\n**N2** [critical] \"Structural failure, not computational\" 声明缺少充分证据\n\n- 具体位置：§4.2 (Iso-Compute Analysis), §3.5 最后一段\n- 问题：论文断言 BCE 的失败是\"structural\"而非\"computational\"，证据是：(a) 2700 steps 后仍不如 KL 1000 steps; (b) BCE loss 在 500-2700 steps 间仅下降 0.006。但这不排除以下可能性：\n  1. BCE 需要不同的 learning rate / schedule（论文未报告 BCE 的 LR 是否做过搜索）\n  2. BCE 需要更大的 predictor architecture（也许 d_b=256 或 512 对 BCE 更关键）\n  3. BCE loss 饱和可能仅说明当前 LR 太小或处于 local minimum\n  4. \"Loss saturation\"不等于\"structural limitation\"——任何已收敛的模型都有 loss saturation\n\n  论文只试了**一个** BCE configuration 就做出\"structural\"断言。对比之下，KL 用了 Gumbel relaxation + Lagrangian constraint + temperature annealing 等多个 tricks。\n- 为什么影响接收：这是论文的核心 narrative，如果证据不足，贡献被严重削弱。\n- 建议修改方向：(1) 对 BCE 做基本的 hyperparameter search（至少 LR grid + architecture size），报告所有结果；(2) 或弱化 claim 为\"under our setting, KL is significantly more effective\"而非绝对的\"structural failure\"。\n\n**N3** [critical] 消融实验严重不足\n\n- 具体位置：Table 3 (§4.3)\n- 问题：消融表只有 4 行，对一个有多个 design choice 的方法论文远远不够。关键缺失：\n  1. **Bottleneck 维度 d_b 的敏感性**：论文选 d_b=128 无任何理由，不知 64/256/512 的效果如何\n  2. **温度退火 schedule**：cosine 从 1.0→0.1 完全无 justification，无 linear/exponential/fixed 对比\n  3. **训练步数的影响曲线**：1000 steps 是否足够？learning curve 是什么样？\n  4. **Lagrangian learning rate η_λ**：这是关键超参，完全未报告\n  5. **训练数据 domain 的影响**：换 C4 训练会怎样？\n- 为什么影响接收：读者无法判断 method 的鲁棒性和 sensitivity，也无法在自己的场景中 tune。\n- 建议修改方向：至少补充 d_b sensitivity（3-4 个值）和 training steps curve。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 论文实际增加了推理延迟，未实现任何 wall-clock 加速\n\n- 具体位置：§4 最后一段 \"Inference Efficiency\" + Appendix A\n- 问题：论文整体 motivation 是\"accelerate SwiGLU-based LLMs\"（Abstract, §1），但实验表明 pipeline 增加 6.4% latency overhead。Appendix 明确承认\"unstructured element-wise masks...do not translate to wall-clock speedup without sparse kernel support\"。这意味着方法**当前不能加速推理**，只能在假设未来有 sparse kernel 的情况下才有价值。\n- 建议：在 Abstract/Introduction 中更诚实地 frame 贡献为\"prediction quality\"研究而非\"acceleration\"研究，或提供至少一个 sparse kernel 的 PoC。\n\n**W2** [warning] Cross-architecture 验证仅一个模型，泛化 claim 过强\n\n- 具体位置：§4 \"Cross-Architecture Validation\" 段\n- 问题：仅额外评估 Mistral-7B-v0.3 一个模型，就称\"cross-architecture validation\"和\"transferability to other SwiGLU architectures\"。LLaMA-3.1-8B 和 Mistral-7B 都是 ~7-8B SwiGLU decoder-only transformers，极其相似。真正的 cross-architecture 应包括不同 FFN 类型（如 GeGLU）、不同规模（13B/70B）、或不同家族（Qwen、Gemma）。\n- 建议：弱化措辞为\"preliminary evaluation on one additional model\"，或补充一个更不同的架构。\n\n**W3** [warning] 三 seed 稳定性评估 (n=3) 统计效力不足\n\n- 具体位置：§4 \"Training Stability\", Appendix B\n- 问题：3 个 seed（42, 123, 456）得到 std=0.07 是不够的。n=3 时标准误差的估计本身就极不可靠——95% CI for σ 在 n=3 时的宽度约为 [0.45σ, 3.2σ]。无法从 3 个点得出\"training is stable\"的可靠结论。\n- 建议：扩展到至少 5-10 seeds，或明确标注这是 preliminary evidence。\n\n**W4** [warning] 梯度分析（§3.5）是 informal argument，非 formal proof\n\n- 具体位置：§3.5\n- 问题：链式法则展开本身正确，但论文从\"KL gradient depends on all neurons\"跳到\"KL is better\"缺少严格推理。Coupled gradient 也可能带来劣势：(a) gradient variance 更高导致优化困难；(b) high-dimensional Jacobian 的 condition number 可能很差；(c) Gumbel noise 进一步增加 variance。论文没有讨论这些 trade-offs，也没有 formal characterization（如 gradient SNR 对比）。\n- 建议：要么提供 gradient variance/SNR 的实证对比，要么明确标注§3.5为\"intuitive motivation\"而非\"theoretical contribution\"。\n\n**W5** [warning] Lagrangian 对偶更新无收敛保证\n\n- 具体位置：§3.4, Eq. 9-10\n- 问题：对于非凸目标（neural network + Gumbel relaxation），Lagrangian dual ascent 不保证收敛到可行解。论文完全没讨论：(a) λ 是否实际收敛？(b) sparsity constraint 最终是否被满足？(c) 是否有 oscillation？这些在实践中可能不是问题（多数 DL 论文忽略这点），但既然论文把 Lagrangian 作为方法 contribution 之一，应该至少实证展示 λ 和 sparsity ratio 的训练曲线。\n- 建议：Appendix 中补充 λ 和实际 sparsity ratio over training steps 的图。\n\n---\n\n## 小问题（不影响接收）\n\n- \"2.71×\" (§4.2) 应为 2.70× (2700/1000=2.7)，微小数值错误\n- \"saves ~2.7% latency\" (§4 Inference Efficiency): 在 50% sparsity 下实际为 2.46% ((129.71-126.78)/119.11)，2.7% 对应 30% sparsity 的数据。文本未说明使用哪个 sparsity level 的数据\n- Table 1 caption 称\"Multi-seed variance (3 seeds, 50% uniform): PPL std=0.07\"，但 main text 报的 PPL 11.79 是 global allocation (seed=42)。multi-seed 用 uniform allocation 得到 11.92±0.07——这两个数字的区别（11.79 vs 11.92）应该更清楚地解释（footnote 已有但容易混淆）\n- \"Relative advantage\" 定义为 (TEAL-KL)/TEAL，这是一种对方法有利的 metric 选择。相比之下，(TEAL-KL)/(TEAL-Dense) 即\"recovery of degradation\"在某些情况下更有信息量\n\n---\n\n## 主要优势\n\n- **Clear central insight**：BCE per-neuron decomposition vs global top-k inference 的 mismatch 观察敏锐且 well-articulated\n- **Solid core result**：PPL 11.79 vs 23.31 (TEAL) / 27.97 (BCE) 的差距显著且consistent across sparsity levels\n- **Well-structured paper**：2D taxonomy 有效地 situate 了 contribution；三个 sparsity regime 的分析有 insight\n- **Honest limitations section**：论文坦诚承认无 wall-clock speedup、单一规模、PPL 作为 proxy 的局限\n- **Reproducibility**：训练 setup 详细，17 min on A6000，practical for reproduction\n- **Gumbel vs STE ablation**：+3.98 PPL gap 证明 relaxation choice matters\n\n---\n\n## Questions to Authors (for rebuttal)\n\n1. BCE 实验中使用的 learning rate 和 schedule 是什么？是否做过 LR search？\n2. d_b=128 是如何选择的？是否有 preliminary 实验？\n3. 能否提供 C4 test set 或其他 OOD 数据上的 PPL，以排除 WikiText 过拟合？\n4. Lagrangian multiplier λ 在训练过程中的轨迹如何？实际 sparsity ratio 是否精确达到 target？\n5. 如果给 BCE 同样的 Gumbel-Sigmoid + Lagrangian 框架（仅把 KL loss 换成对应的 BCE target），性能如何？这能更 cleanly 隔离 loss function 的贡献 vs 训练框架的贡献。",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-16T18:59:08.849878+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3770
}
```

</details>

---


### Assistant

_source line 30 · 2026-05-16T18:59:15.374130+00:00_

审稿报告已提交给 Review Director。

总结：评分 Overall 3/5（Findings track），Soundness 3/5，Excitement 3/5。主要问题：(1) 训练/评估同源（WikiText-103→WikiText-2）有过拟合风险且无 OOD 验证；(2) "structural failure"断言仅基于一个 BCE configuration，缺少 hyperparameter search；(3) 消融实验仅 4 行，缺 d_b sensitivity、温度 schedule 对比、training curve 等关键消融。次要问题包括未实现实际加速、cross-architecture 验证不足（仅 1 个额外模型）、3-seed 统计效力弱。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1"
}
```

</details>

---


## Round 2

## Round 2

4 recorded events


### User

_source line 31 · 2026-05-16T19:01:19.159484+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix 问题：
- **[AGREE]**：同意该问题存在，并简述理由
- **[REBUT]**：反驳该问题，并提供证据（cite 具体 Section/Table/Figure）

---

### Reviewer 2 报告摘要

**Overall**: 3.0/5 (Findings)
**Soundness**: 3/5 | **Excitement**: 3/5 | **Reproducibility**: 4/5

---

### Must-Fix 问题

**N1** [critical] Limitations section 格式不合规
- 当前为 conclusion 内 `\paragraph{Limitations.}`
- ARR 要求独立 `\section*{Limitations}`（conclusion 之后、references 之前、不计页数）
- 这是 desk-reject 条件之一

**N2** [critical] 页数超限
- Conclusion 含 Limitations 和 Future work 延伸至第 9 页顶部
- ACL long paper 正文限制 ≤8 页
- 即使拆出 Limitations 后可能刚好 8 页，当前状态超限

**N3** [critical] 新颖性有限——与 SPON 的区分度不充分
- SPON 已使用 KL divergence 训练 sparsity correction
- 本文差异仅在于 per-token contextual mask + Gumbel-Sigmoid
- 更像 SPON 的自然延伸而非根本性创新
- SPON orthogonality analysis 反过来说明 SPON 的 KL training 已覆盖大部分信号

---

### Should-Fix 问题

**W1** 遗漏重要相关工作：MaskLLM (NeurIPS 2024 Spotlight) — 使用 Gumbel Softmax 学 N:M sparsity mask
**W2** MoE 与 contextual sparsity 的关联未讨论
**W3** "Structural mismatch" 论述过度——"proxy loss vs end-to-end loss" 是 ML 基本认知
**W4** BCE baseline 不充分——仅 vanilla BCE，缺 weighted BCE / BCE+ranking loss / soft targets 对比
**W5** 三个 regime 的发现仅单模型验证，缺乏普适性
**W6** 2D taxonomy 学术贡献有限——post-hoc 分类，无预测性
**W7** 无实际 wall-clock speedup 展示

---

### 遗漏引用
1. MaskLLM (Fang et al., NeurIPS 2024 Spotlight)
2. MoE routing 相关工作 (Switch Transformer, GShard)
3. LLM-specific KD (MiniLLM, GKD)

### 小问题
- S1: SPON year mismatch (bib=2026 ICML, OpenAlex=2025)
- S2: 两个 evaluation protocol 差异未充分解释
- S3: FastForward 67.2M/2.7% 数字来源不明
- S4: Mistral PPL 8.98 = LLaMA 30% PPL 8.98 巧合易混淆
- S5: WikiText train/eval leakage 风险
- S6: 缺 Ethics Statement
- S7: 匿名性检查通过

---

请逐条回应以上所有问题（Must-Fix N1-N3, Should-Fix W1-W7, 遗漏引用, 小问题 S1-S7）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-16T19:02:49.627786+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 交叉回应 — 逐条回应 Reviewer 2\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: Limitations section 格式不合规**\n\n同意。我确认 `conclusion.tex` 中使用的是 `\\paragraph{Limitations.}` 嵌在 Conclusion 内，而非独立的 `\\section*{Limitations}`。ARR Author Guidelines 明确要求 Limitations 为独立 section（conclusion 之后、references 之前、不占页数）。这确实是 desk-reject 条件。我在自己的审稿中未将此列为单独问题（我的审查侧重在方法/实验），但 R2 的判断完全正确。\n\n**[AGREE] R2-N2: 页数超限**\n\n同意这是一个需要确认的 formatting risk。当前 Conclusion 包含 Limitations + Future work 共约 25 行正文（conclusion.tex），加上 Method 和 Experiments 的密度（多个 table 和 figure），很可能超 8 页。不过我无法 100% 确认——需要编译 PDF 实测。如果拆出 Limitations 并 tighten future work，可能刚好 8 页。我建议作者编译确认并必要时压缩。\n\n**[REBUT] R2-N3: 新颖性有限——与 SPON 的区分度不充分**\n\nR2 的核心论点是\"本文仅是 SPON 的自然延伸\"，我不同意这个判断。理由：\n\n1. **方法差异是 fundamental 的，不是 incremental 的**：SPON 学习的是 input-independent per-layer bias vector（§2 Related Work: \"learns input-independent bias vectors via KL divergence, absorbed into parameters at zero inference cost\"）。本文学习的是 input-dependent per-token contextual mask（2.37M 参数/层的 MLP predictor）。这是\"static correction\"与\"dynamic prediction\"的根本区别——一个是加法偏置，一个是乘法 gating。\n\n2. **SPON orthogonality analysis 的正确解读**：R2 称\"SPON 的 KL training 已覆盖大部分信号\"，但§4.4 的数据说的恰恰相反——cosine similarity 0.196 意味着 SPON 的修正方向与 predictor 几乎正交，SPON 只贡献 2.4% relative improvement (12.08→11.79)。这证明 **SPON 未能捕获 predictor 捕获的信号**，而非\"SPON 已覆盖大部分\"。Predictor 的 L2 norm 为 482.65，SPON 为 76.2（仅 15.8%）——信号主体在 predictor 而非 SPON。\n\n3. **技术框架完全不同**：SPON 不需要 Gumbel relaxation（因为它不做 discrete mask decision），不需要 Lagrangian constraint（因为它不控制 sparsity ratio），不需要 end-to-end differentiable forward pass through masks。本文的技术贡献在于如何让 KL training work for discrete mask decisions——这是 SPON 完全没有解决的问题。\n\n不过，我承认论文可以更好地 articulate 这一区别。当前写法（§2, §4.4）分散在多处，reader 需要自行拼合。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: 遗漏 MaskLLM (NeurIPS 2024 Spotlight)**\n\n强烈同意。MaskLLM 使用 Gumbel-Softmax 学习 N:M sparsity masks，与本文在技术手法（Gumbel relaxation for discrete mask learning）和问题设置（learned sparsity prediction for LLMs）上高度相关。遗漏此引用是一个明显的疏忽。论文应在 Related Work 中讨论 MaskLLM 并明确区分（MaskLLM 针对 N:M structured pattern，本文针对 unstructured contextual sparsity with global top-k allocation）。\n\n**[AGREE] R2-W2: MoE 与 contextual sparsity 的关联未讨论**\n\n部分同意。Contextual sparsity prediction 确实与 MoE routing 有 conceptual similarity（both 做 input-dependent computation selection）。一两句讨论 MoE routing literature 和本文 setting 的区别（MoE 选 expert = coarse-grained block selection；本文选 neurons = fine-grained element selection）会 strengthen related work。但我不认为这是 critical omission——问题域和粒度差异足够大。\n\n**[AGREE] R2-W3: \"Structural mismatch\" 论述过度**\n\n同意。我在自己的 W4 中也提出了类似观点。\"Per-neuron proxy loss vs end-to-end loss performs worse\" 确实是 ML 的 common wisdom（distillation > classification in many settings）。论文将此 frame 为\"structural insight\"并用一整个 §3.5 展开梯度分析有些 overselling。核心贡献应定位在 **empirical demonstration + practical recipe**（Gumbel + Lagrangian + temperature annealing 使其 work）而非 theoretical novelty。\n\n**[AGREE] R2-W4: BCE baseline 不充分**\n\n强烈同意。这与我的 N2 (Must-Fix) 完全一致。论文只试了 vanilla BCE 一个配置就宣称\"structural failure\"，缺少 weighted BCE、BCE + ranking loss、soft-target BCE、不同 LR/architecture 的对比。这严重削弱了核心 narrative。\n\n**[AGREE] R2-W5: 三个 regime 仅单模型验证**\n\n同意。Budget-surplus / budget-constrained / capacity-limited 的 regime 划分是有 insight 的观察，但基于单模型（LLaMA-3.1-8B）。这些 boundary 是否在不同 model sizes 下 shift？在 13B 上 50% sparsity 是否仍是 capacity-limited？缺乏验证使这个 finding 的 generalizability 存疑。\n\n**[REBUT] R2-W6: 2D taxonomy 学术贡献有限**\n\n部分反驳。我同意 taxonomy 是 post-hoc classification 而非有预测性的理论框架。但我认为它仍有 organizational value：\n1. 它清晰地 identify 了本文 contribution 相对于 prior work 的位置（Table 1, §3.6）\n2. 它帮助 reader 快速理解方法空间的 landscape\n3. \"Post-hoc\"不等于\"无价值\"——periodic table 也是 post-hoc classification\n\n不过 R2 的批评对于将 taxonomy 作为 \"contribution\" 列在 bullet points 中是合理的——它更适合作为 presentation device 而非 standalone contribution。\n\n**[AGREE] R2-W7: 无实际 wall-clock speedup 展示**\n\n完全同意。我在自己的 W1 中提出了同样的问题。Appendix A 明确承认当前实现增加 6.4% overhead 且 unstructured masks 不产生实际加速。论文应更诚实地 frame 为 prediction quality 研究。\n\n---\n\n### 遗漏引用\n\n**[AGREE] MaskLLM (Fang et al., NeurIPS 2024)**：直接相关，必须引用。\n\n**[AGREE partially] MoE routing (Switch Transformer, GShard)**：值得在 Related Work 中简短提及以 discuss connection/distinction，但非 critical omission。\n\n**[AGREE partially] LLM-specific KD (MiniLLM, GKD)**：与本文的 KL distillation 有方法论 overlap，值得引用。不过本文的 distillation 目标是 mask predictor（不改变 base model weights），与 MiniLLM/GKD 的 model distillation 有 fundamental 区别。\n\n---\n\n### 小问题\n\n**[AGREE] S1: SPON year mismatch**：如果 bib 标注 2026 ICML 但实际发表于 2025，这是 citation accuracy 问题，应修正。\n\n**[AGREE] S2: 两个 evaluation protocol 差异未充分解释**：我在自己的小问题中也指出了这点。Table 1 footnote 尝试解释但不够清晰。两个 protocol 下 PPL=11.79 的\"coincidental equality\"增加了混淆。\n\n**[AGREE] S3: FastForward 67.2M/2.7% 数字来源不明**：论文多次引用\"67.2M parameters and ~2.7% additional latency\"作为 compensation network 的 cost，但这些数字是否来自 FastForward 原文、作者自己的 reimplementation、还是估算？应标注来源。\n\n**[AGREE] S4: Mistral PPL 8.98 = LLaMA 30% PPL 8.98 巧合**：确实容易让 reader 混淆。建议加一句 clarification 或在 Table 中并排呈现时加注。\n\n**[AGREE] S5: WikiText train/eval leakage 风险**：这与我的 N1 (Must-Fix) 一致。WikiText-103 训练 + WikiText-2 评估存在 domain overlap 风险。\n\n**[AGREE] S6: 缺 Ethics Statement**：ARR 要求 Ethics Statement section。如果确实缺失，与 N1 (Limitations) 同属格式合规问题。\n\n**[AGREE] S7: 匿名性检查通过**：确认。\n\n---\n\n### 总结\n\nR2 的审稿与我的审稿高度互补。我们在以下关键问题上达成共识：\n1. BCE baseline 给的不公平（我的 N2 = R2 的 W4）\n2. 无 wall-clock speedup（我的 W1 = R2 的 W7）\n3. WikiText leakage 风险（我的 N1 = R2 的 S5）\n4. \"Structural failure\" claim 过强（我的 N2 ≈ R2 的 W3）\n\n我与 R2 的主要分歧在 **N3 (novelty vs SPON)**：我认为本文与 SPON 的技术差异是 fundamental 的（static bias vs dynamic contextual mask, 完全不同的训练框架），SPON orthogonality 数据支持本文而非削弱本文。",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 交叉回应 — 逐条回应 Reviewer 2\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: Limitations section 格式不合规**\n\n同意。我确认 `conclusion.tex` 中使用的是 `\\paragraph{Limitations.}` 嵌在 Conclusion 内，而非独立的 `\\section*{Limitations}`。ARR Author Guidelines 明确要求 Limitations 为独立 section（conclusion 之后、references 之前、不占页数）。这确实是 desk-reject 条件。我在自己的审稿中未将此列为单独问题（我的审查侧重在方法/实验），但 R2 的判断完全正确。\n\n**[AGREE] R2-N2: 页数超限**\n\n同意这是一个需要确认的 formatting risk。当前 Conclusion 包含 Limitations + Future work 共约 25 行正文（conclusion.tex），加上 Method 和 Experiments 的密度（多个 table 和 figure），很可能超 8 页。不过我无法 100% 确认——需要编译 PDF 实测。如果拆出 Limitations 并 tighten future work，可能刚好 8 页。我建议作者编译确认并必要时压缩。\n\n**[REBUT] R2-N3: 新颖性有限——与 SPON 的区分度不充分**\n\nR2 的核心论点是\"本文仅是 SPON 的自然延伸\"，我不同意这个判断。理由：\n\n1. **方法差异是 fundamental 的，不是 incremental 的**：SPON 学习的是 input-independent per-layer bias vector（§2 Related Work: \"learns input-independent bias vectors via KL divergence, absorbed into parameters at zero inference cost\"）。本文学习的是 input-dependent per-token contextual mask（2.37M 参数/层的 MLP predictor）。这是\"static correction\"与\"dynamic prediction\"的根本区别——一个是加法偏置，一个是乘法 gating。\n\n2. **SPON orthogonality analysis 的正确解读**：R2 称\"SPON 的 KL training 已覆盖大部分信号\"，但§4.4 的数据说的恰恰相反——cosine similarity 0.196 意味着 SPON 的修正方向与 predictor 几乎正交，SPON 只贡献 2.4% relative improvement (12.08→11.79)。这证明 **SPON 未能捕获 predictor 捕获的信号**，而非\"SPON 已覆盖大部分\"。Predictor 的 L2 norm 为 482.65，SPON 为 76.2（仅 15.8%）——信号主体在 predictor 而非 SPON。\n\n3. **技术框架完全不同**：SPON 不需要 Gumbel relaxation（因为它不做 discrete mask decision），不需要 Lagrangian constraint（因为它不控制 sparsity ratio），不需要 end-to-end differentiable forward pass through masks。本文的技术贡献在于如何让 KL training work for discrete mask decisions——这是 SPON 完全没有解决的问题。\n\n不过，我承认论文可以更好地 articulate 这一区别。当前写法（§2, §4.4）分散在多处，reader 需要自行拼合。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: 遗漏 MaskLLM (NeurIPS 2024 Spotlight)**\n\n强烈同意。MaskLLM 使用 Gumbel-Softmax 学习 N:M sparsity masks，与本文在技术手法（Gumbel relaxation for discrete mask learning）和问题设置（learned sparsity prediction for LLMs）上高度相关。遗漏此引用是一个明显的疏忽。论文应在 Related Work 中讨论 MaskLLM 并明确区分（MaskLLM 针对 N:M structured pattern，本文针对 unstructured contextual sparsity with global top-k allocation）。\n\n**[AGREE] R2-W2: MoE 与 contextual sparsity 的关联未讨论**\n\n部分同意。Contextual sparsity prediction 确实与 MoE routing 有 conceptual similarity（both 做 input-dependent computation selection）。一两句讨论 MoE routing literature 和本文 setting 的区别（MoE 选 expert = coarse-grained block selection；本文选 neurons = fine-grained element selection）会 strengthen related work。但我不认为这是 critical omission——问题域和粒度差异足够大。\n\n**[AGREE] R2-W3: \"Structural mismatch\" 论述过度**\n\n同意。我在自己的 W4 中也提出了类似观点。\"Per-neuron proxy loss vs end-to-end loss performs worse\" 确实是 ML 的 common wisdom（distillation > classification in many settings）。论文将此 frame 为\"structural insight\"并用一整个 §3.5 展开梯度分析有些 overselling。核心贡献应定位在 **empirical demonstration + practical recipe**（Gumbel + Lagrangian + temperature annealing 使其 work）而非 theoretical novelty。\n\n**[AGREE] R2-W4: BCE baseline 不充分**\n\n强烈同意。这与我的 N2 (Must-Fix) 完全一致。论文只试了 vanilla BCE 一个配置就宣称\"structural failure\"，缺少 weighted BCE、BCE + ranking loss、soft-target BCE、不同 LR/architecture 的对比。这严重削弱了核心 narrative。\n\n**[AGREE] R2-W5: 三个 regime 仅单模型验证**\n\n同意。Budget-surplus / budget-constrained / capacity-limited 的 regime 划分是有 insight 的观察，但基于单模型（LLaMA-3.1-8B）。这些 boundary 是否在不同 model sizes 下 shift？在 13B 上 50% sparsity 是否仍是 capacity-limited？缺乏验证使这个 finding 的 generalizability 存疑。\n\n**[REBUT] R2-W6: 2D taxonomy 学术贡献有限**\n\n部分反驳。我同意 taxonomy 是 post-hoc classification 而非有预测性的理论框架。但我认为它仍有 organizational value：\n1. 它清晰地 identify 了本文 contribution 相对于 prior work 的位置（Table 1, §3.6）\n2. 它帮助 reader 快速理解方法空间的 landscape\n3. \"Post-hoc\"不等于\"无价值\"——periodic table 也是 post-hoc classification\n\n不过 R2 的批评对于将 taxonomy 作为 \"contribution\" 列在 bullet points 中是合理的——它更适合作为 presentation device 而非 standalone contribution。\n\n**[AGREE] R2-W7: 无实际 wall-clock speedup 展示**\n\n完全同意。我在自己的 W1 中提出了同样的问题。Appendix A 明确承认当前实现增加 6.4% overhead 且 unstructured masks 不产生实际加速。论文应更诚实地 frame 为 prediction quality 研究。\n\n---\n\n### 遗漏引用\n\n**[AGREE] MaskLLM (Fang et al., NeurIPS 2024)**：直接相关，必须引用。\n\n**[AGREE partially] MoE routing (Switch Transformer, GShard)**：值得在 Related Work 中简短提及以 discuss connection/distinction，但非 critical omission。\n\n**[AGREE partially] LLM-specific KD (MiniLLM, GKD)**：与本文的 KL distillation 有方法论 overlap，值得引用。不过本文的 distillation 目标是 mask predictor（不改变 base model weights），与 MiniLLM/GKD 的 model distillation 有 fundamental 区别。\n\n---\n\n### 小问题\n\n**[AGREE] S1: SPON year mismatch**：如果 bib 标注 2026 ICML 但实际发表于 2025，这是 citation accuracy 问题，应修正。\n\n**[AGREE] S2: 两个 evaluation protocol 差异未充分解释**：我在自己的小问题中也指出了这点。Table 1 footnote 尝试解释但不够清晰。两个 protocol 下 PPL=11.79 的\"coincidental equality\"增加了混淆。\n\n**[AGREE] S3: FastForward 67.2M/2.7% 数字来源不明**：论文多次引用\"67.2M parameters and ~2.7% additional latency\"作为 compensation network 的 cost，但这些数字是否来自 FastForward 原文、作者自己的 reimplementation、还是估算？应标注来源。\n\n**[AGREE] S4: Mistral PPL 8.98 = LLaMA 30% PPL 8.98 巧合**：确实容易让 reader 混淆。建议加一句 clarification 或在 Table 中并排呈现时加注。\n\n**[AGREE] S5: WikiText train/eval leakage 风险**：这与我的 N1 (Must-Fix) 一致。WikiText-103 训练 + WikiText-2 评估存在 domain overlap 风险。\n\n**[AGREE] S6: 缺 Ethics Statement**：ARR 要求 Ethics Statement section。如果确实缺失，与 N1 (Limitations) 同属格式合规问题。\n\n**[AGREE] S7: 匿名性检查通过**：确认。\n\n---\n\n### 总结\n\nR2 的审稿与我的审稿高度互补。我们在以下关键问题上达成共识：\n1. BCE baseline 给的不公平（我的 N2 = R2 的 W4）\n2. 无 wall-clock speedup（我的 W1 = R2 的 W7）\n3. WikiText leakage 风险（我的 N1 = R2 的 S5）\n4. \"Structural failure\" claim 过强（我的 N2 ≈ R2 的 W3）\n\n我与 R2 的主要分歧在 **N3 (novelty vs SPON)**：我认为本文与 SPON 的技术差异是 fundamental 的（static bias vs dynamic contextual mask, 完全不同的训练框架），SPON orthogonality 数据支持本文而非削弱本文。",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-16T19:02:54.616694+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4988
}
```

</details>

---


### Assistant

_source line 34 · 2026-05-16T19:03:00.755525+00:00_

交叉回应已提交给 Review Director。我逐条回应了 R2 的所有问题：
- Must-Fix: N1 [AGREE], N2 [AGREE], N3 [REBUT]（与 SPON 的差异是 fundamental 的）
- Should-Fix: W1-W5, W7 [AGREE]; W6 [部分 REBUT]（taxonomy 有 organizational value）
- 遗漏引用和小问题基本同意

与 R2 的主要分歧在 novelty 判断——我认为 per-token contextual mask + Gumbel-Sigmoid + Lagrangian 框架与 SPON 的 static bias vector 有根本性区别，orthogonality 数据支持本文的 claim。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1"
}
```

</details>

---


## Round 3

## Round 3

36 recorded events


### User

_source line 35 · 2026-05-17T02:29:26.618416+00:00_

[Round 1 审稿请求]:
## 审稿任务分配 — Reviewer 1（方法严谨性 + 实验方法论）

### Venue 信息
- **目标会议**: EMNLP 2026 (via ACL Rolling Review May cycle)
- **Deadline**: 2026-05-25
- **页数限制**: Long paper, 8 页正文 + unlimited references
- **模板**: ACL style (`\usepackage[review]{acl}`)
- **匿名规则**: Double-blind
- **Limitations**: 必须独立 `\section*{Limitations}`（不计入页数）
- **Appendix**: 不计入页数，审稿人不强制阅读但可参考

### 论文路径
`projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, appendix.tex）

### 你的审查侧重

**核心任务**：评估方法的技术严谨性和实验的可靠性。

重点审查维度：
1. **KL distillation 框架**：Gumbel-Sigmoid relaxation 的数学正确性、与 inference 的 gap（soft mask training vs hard mask inference）、forward KL 选择的合理性
2. **梯度分析（§3.5）**：BCE vs KL 的 structural mismatch argument 是否 rigorous、是否存在 logical gap
3. **Lagrangian sparsity constraint**：multiplicative dual variable controller 的收敛性、deadzone 设计、是否有更好的替代方案
4. **实验设计**：
   - Iso-compute 对比是否公平（KL 1000 steps vs BCE 2700 steps，但 KL 需要 full forward pass 梯度）
   - 消融实验的完整性（d_b sensitivity、τ schedule、training convergence）
   - 统计可靠性（3 seeds, CV<1%）
   - OOD 评估（WikiText-103 训练 → WikiText-2 评估 → C4 验证）
5. **Inference 实际收益**：6.4% overhead claim、compensation 消除的实际影响
6. **可复现性**：训练细节是否充分（lr, batch size, hardware, time）

### 已知 open issues（来自 Issue Tracker）
- R1-N3 (in_progress): 消融实验维度——d_b sensitivity、温度 schedule、training curve 是否已补充到 Appendix
- R1-W5 (in_progress): Lagrangian 收敛分析——λ 轨迹和 sparsity ratio 曲线是否已加入
- R1-W3 (open): 三 seed (n=3) 统计效力

### 输出格式
请按以下结构输出审稿意见：
1. Summary（2-3 句）
2. Strengths（逐条，标号 S1, S2, ...）
3. Weaknesses（逐条，标号 W1, W2, ...，标注 severity: critical/warning/info）
4. Questions（需要作者澄清的技术问题）
5. Missing References（如有）
6. Overall Assessment（score + confidence + 1-2 句总评）

评分标准：strong reject / weak reject / borderline / weak accept / strong accept
置信度：1-5（5=expert）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-17T02:29:34.938742+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
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

_source line 37 · 2026-05-17T02:29:34.989407+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-17T02:29:37.701504+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 39 · 2026-05-17T02:29:39.057600+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 40 · 2026-05-17T02:29:39.108274+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	
17	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
18	
19	\author{Anonymous}
20	
21	\begin{document}
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
32	\input{conclusion}
33	\input{limitations}
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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 41 · 2026-05-17T02:29:47.319459+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"}]

Based on the search results, here's information about ACL Rolling Review 2026 reviewer guidelines and review criteria:

## Reviewer Guidelines

ARR reviewers are instructed to write a review as if the paper were being considered for the ACL conference. Thus low scores may indicate the submission is not a good fit for ACL, even if it may be a good fit for other/mo
…[truncated 1709 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 9617
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-17T02:29:50.987885+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
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

_source line 43 · 2026-05-17T02:29:50.988260+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-17T02:29:51.593696+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-17T02:29:51.644447+00:00_

1	Activation sparsity reduces the effective computation in SwiGLU-based LLMs by pruning FFN neurons at inference, but existing learned predictors trained with binary cross-entropy (BCE) require error compensation networks due to a structural mismatch: BCE decomposes per neuron while inference uses global top-$k$ allocation across all layers.
2	We train lightweight predictors (2.37M parameters per layer, 75.9M total, $<$1\% of the base model) with KL divergence, which couples all neurons through the output distribution via Gumbel-Sigmoid relaxation, eliminating the need for compensation.
3	On LLaMA-3.1-8B (WikiText-2), our KL-trained predictor achieves perplexity 11.79 at 50\% sparsity without compensation, compared to 23.31 for vanilla TEAL and 27.97 for BCE trained at 2.71$\times$ the compute budget, whose loss saturates, confirming a structural rather than computational failure.
4	Three-seed evaluation confirms training stability (PPL $11.92 \pm 0.07$, CV${<}$1\% under uniform allocation).
5	The KL advantage grows disproportionately with sparsity: 18\% relative improvement at 30\%, 49\% at 50\%, and 82\% at 70\%.
6	Cross-architecture evaluation on Mistral-7B-v0.3 confirms the advantage transfers across SwiGLU architectures of similar scale, with consistent KL-over-TEAL ratios (within 7\% at $\leq$50\% sparsity).
7	SPON's static bias correction proves near-orthogonal to the predictor (cosine similarity 0.196), providing only 2.4\% relative PPL improvement (12.08$\to$11.79 under \texttt{evaluate.py}).
8	We propose a two-dimensional taxonomy over correction granularity $\times$ training signal coupling that unifies prior methods and identify three distinct sparsity regimes---budget-surplus, budget-constrained, and capacity-limited---that govern the quality-sparsity tradeoff.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-17T02:29:52.197240+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 47 · 2026-05-17T02:29:52.197798+00:00_

1	\section{Introduction}
2	
3	SwiGLU feed-forward networks~\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.
4	Exploiting this sparsity can simplify inference by pruning 50\% of FFN neurons per token---without modifying the pretrained weights---eliminating the need for auxiliary compensation networks.
5	Yet the gap between potential and practice remains wide.
6	Training-free methods such as TEAL~\cite{liu2025teal} select neurons by activation magnitude alone, degrading perplexity from 6.12 (dense) to 23.31 at 50\% sparsity on LLaMA-3.1-8B~\cite{grattafiori2024llama3}---a 281\% increase.
7	Learned predictors~\cite{liu2023dejavu,gautam2026fastforward} close part of this gap by training small auxiliary networks to anticipate which neurons will be important, but they rely on error compensation modules (output rescaling networks or additive correction layers) that add 67.2M parameters and $\sim$2.7\% additional latency overhead at inference.
8	The question is whether a predictor can be trained so that compensation becomes unnecessary.
9	
10	The answer depends on the training objective.
11	Current learned predictors use binary cross-entropy (BCE) loss: each neuron is independently classified as ``keep'' or ``prune'' against an oracle mask derived from the dense model's activations.
12	The gradient of BCE with respect to neuron $j$'s score is $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$---a function of neuron $j$ alone, independent of every other neuron in the network.
13	But at inference, no neuron is evaluated in isolation.
14	TEAL's global top-$k$ mechanism~\cite{liu2025teal} ranks all neurons across all layers and retains only those above a model-wide threshold.
15	Whether neuron $j$ survives depends not on its own score but on how that score compares to the scores of all $L \times d_{\text{ff}}$ neurons.
16	This creates a structural
…[truncated 4994 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-17T02:29:52.399046+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-17T02:29:52.451430+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models.
5	The method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass, eliminating the need for auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{h}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importance scores from the pre-FFN hidden state $\mathbf{h}$.
26
…[truncated 13338 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-17T02:29:58.489548+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form criteria, scoring dimensions, and their scales (e.g., soundness 1-5, excitement 1-5, etc.). List all dimensions that reviewers must score on and any specific instructions for each dimension."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form criteria, scoring dimensions, and their scales (e.g., soundness 1-5, excitement 1-5, etc.). List all dimensions that reviewers must score on and any specific instructions for each dimension."
  }
}
```

</details>

---


### Tool call

_source line 51 · 2026-05-17T02:30:00.349884+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 52 · 2026-05-17T02:30:00.803011+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4, using AdamW with learning rate $1 \times 10^{-3}$ and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly; (2) \textbf{BCE predictor}, trained with per-neuron binary cross-entropy loss for 1000 and 2700 steps; (3) \textbf{Uniform allocation}, which distributes the sparsity budget equally across layers; and (4) \textbf{WINA}~\cite{liu2025teal}, an importance-weighted variant.
23	
24	
25	\subsection{Main Results}
26	
27	Table~\ref{tab:main} presen
…[truncated 12486 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 53 · 2026-05-17T02:30:00.803514+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 54 · 2026-05-17T02:30:00.904268+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude, achieving 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking.
6	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
7	
8	\paragraph{Predictor-Based Contextual Sparsity.}
9	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
10	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with MSE supervision but retains per-neuron decomposition.
11	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction---adding inference latency.
12	PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.
13	MaskLLM~\cite{fang2024maskllm} also employs learnable masks with Gumbel relaxation and frozen weights, but targets N:M semi-structured \emph{weight} sparsity (2:4 patterns) via Gumbel-Softmax, producing fixed masks independent of input tokens.
14	In contrast, our method learns \emph{activation} masks that are contextual (per-token), unstructured (budget-constrained global top-$k$), and trained with Gumbel-Sigmoid to minimize output-distribution divergence.
15	All prior predictor-based methods use decomposed (BCE) or intermediate (MSE) objectives where each neuron's gradient is independent of other mask states.
16	Our \emph{coupled} KL objective propagates gradients through all downstream layers, optimizing for global allocation quality without compensation
…[truncated 1589 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-17T02:30:03.665477+00:00_

# ARR Review Form Scoring Dimensions

Based on the provided guidelines, the review form includes the following scoring dimensions:

## Primary Scoring Dimensions

**1. Soundness**
Reviewers assess the technical quality and validity of the work. The guidelines state that "soundness scores must be justified by the text of the review." Low soundness scores require explicit justification in the written content; otherwise, the review lacks consistency.

**2. Excitement**
This reflects personal interest and subjective appeal, described as "orthogonal to the assessment of the soundness of the paper." The guidelines clarify that excitement captures individual preferences separate from technical merit.

**3. Overall Assessment/Recommendation**
A composite score providing an explicit recommendation for paper acceptance. This integrates soundness, excitement, novelty, and potential impact considerations.

## Additional Scoring Elements

**Confidence/Confidence Scores**
Reviewers can indicate their confidence level in their assessment, particularly relevant when expertise doesn't cover all submission aspects.

**Reproducibility Score**
While not extensively detailed, the guidelines reference reproducibility scoring, noting that "low reproducibility scores should be justified" similar to soundness scores.

## Important Note

The document states these guidelines are "a work-in-progress" and notes that "starting with February 2025, ARR reviewers are asked to provide" the three primary scores mentioned above. The specific numerical scales (e.g., 1-5) are not explicitly detailed in the provided text.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5175
}
```

</details>

---


### Tool call

_source line 56 · 2026-05-17T02:30:07.833074+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 57 · 2026-05-17T02:30:08.285155+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Training sparsity predictors with KL divergence eliminates error compensation networks by coupling all neurons through the output distribution, resolving BCE's structural mismatch with global top-$k$ allocation.
5	The resulting predictor (75.9M params, $<$1\% of base) achieves PPL 11.79 at 50\% sparsity vs.\ 23.31 for TEAL, transfers across SwiGLU architectures of similar scale (within 7\% ratio consistency), and reveals three sparsity regimes governing the quality-allocation tradeoff.
6	
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-17T02:30:08.285503+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 59 · 2026-05-17T02:30:08.587267+00:00_

1	\section*{Limitations}
2	
3	Our primary evaluation uses WikiText-2 perplexity, and downstream benchmarks reveal that perplexity is a poor proxy for reasoning ability at moderate sparsity: 40\% sparsity achieves PPL 8.36 but MMLU already degrades, motivating 30\% as the recommended operating point for downstream fidelity.
4	Training requires 1000 steps on WikiText-103 ($\sim$17 minutes on A6000), but a separate predictor must be trained for each sparsity target.
5	All experiments use 7--8B parameter models (LLaMA-3.1-8B, Mistral-7B-v0.3); scaling behavior to 13B or 70B models remains untested.
6	While we motivate our work with inference speedup potential, actual wall-clock acceleration depends on sparse kernel implementations (e.g., Triton, cuSPARSE) and hardware-specific memory access patterns; this work focuses on prediction quality rather than systems optimization.
7	Future directions include N:M structured sparsity for hardware-native acceleration, scaling to 13B+ models, and training a single predictor that serves multiple sparsity targets simultaneously.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 60 · 2026-05-17T02:30:08.587608+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 61 · 2026-05-17T02:30:08.638176+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling), confirming that KL distillation provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overh
…[truncated 7564 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 62 · 2026-05-17T02:30:13.922486+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form 2025 2026 scoring scale soundness excitement overall assessment 1-5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form 2025 2026 scoring scale soundness excitement overall assessment 1-5"
  }
}
```

</details>

---


### Tool call

_source line 63 · 2026-05-17T02:30:15.430206+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 64 · 2026-05-17T02:30:15.430908+00:00_

1	% =============================================================================
2	% Direction 1: KL distillation for structured/activation sparsity
3	% =============================================================================
4	
5	@inproceedings{fang2024maskllm,
6	  title = {MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models},
7	  author = {Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff Pool and Jan Kautz and Pavlo Molchanov and Xinchao Wang},
8	  year = {2024},
9	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
10	  url = {https://arxiv.org/abs/2409.17481},
11	}
12	
13	@inproceedings{xu2026spon,
14	  title = {Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models},
15	  author = {Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma},
16	  year = {2026},
17	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
18	  url = {https://arxiv.org/abs/2512.12744},
19	}
20	
21	@inproceedings{muralidharan2024minitron,
22	  title = {Compact Language Models via Pruning and Knowledge Distillation},
23	  author = {Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marcin Chochowski and Mostofa Patwary and Mohammad Shoeybi and Bryan Catanzaro and Jan Kautz and Pavlo Molchanov},
24	  year = {2024},
25	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
26	  url = {https://arxiv.org/abs/2407.14679},
27	}
28	
29	
30	% =============================================================================
31	% Direction 3: SPON and learnable bias correction for sparsity
32	% =============================================================================
33	
34	@article{gautam2026fastforward,
35	  title = {Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity},
36	  author = {Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott and Naras
…[truncated 8151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 65 · 2026-05-17T02:30:21.217890+00:00_

Web search results for query: "ACL ARR review form 2025 2026 scoring scale soundness excitement overall assessment 1-5"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Statistics","url":"https://stats.aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL ARR 2025 May | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2025%2FMay"},{"title":"ACL Rolling Review Data Collection (ARR-DC) - ARR Data Collection","url":"https://arr-data.aclweb.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

Based on the search results, I found information about the ACL ARR review form scoring scale for 2025-2026:

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

Regarding the overall recommendation/assessment scoring scale, the options are: 5 = Consider for Award (up to top 2.5% papers), with lower options including 2 = Resubmit next cycle, 1.5 = Re
…[truncated 654 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7295
}
```

</details>

---


### Tool call

_source line 66 · 2026-05-17T02:30:26.138219+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with ALL scoring dimensions, their numerical scales (e.g., 1-5), and the description of each score level. I need the exact scale for: soundness, excitement/novelty, overall assessment/recommendation, confidence, reproducibility, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with ALL scoring dimensions, their numerical scales (e.g., 1-5), and the description of each score level. I need the exact scale for: soundness, excitement/novelty, overall assessment/recommendation, confidence, reproducibility, and any other scored dimensions."
  }
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-17T02:30:32.034294+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Reviewer Confidence
**Scale: 1-5**
- 5: "Positive that my evaluation is correct. I read the paper very carefully"
- 4: "Quite sure" with unlikely but conceivable errors
- 3: "Pretty sure, but there's a chance I missed something"
- 2: "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- 1: "Not my area, or paper is very hard to understand"

## Soundness
**Scale: 1-5 (with half-point increments)**
- 5: "Excellent: This study is one of the most thorough I have seen"
- 4: "Strong: This study provides sufficient support for all of its claims"
- 3: "Acceptable: This study provides sufficient support for its main claims"
- 2: "Poor: Some of the main claims are not sufficiently supported"
- 1: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement
**Scale: 1-5 (with half-point increments)**
- 5: "Highly Exciting: I would recommend this paper to others"
- 4: "Exciting: I would mention this paper to others"
- 3: "Interesting: I might mention some points of this paper to others"
- 2: "Potentially Interesting: this paper does not resonate with me"
- 1: "Not Exciting: this paper does not resonate with me"

## Overall Assessment
**Scale: 1-5 (with half-point increments)**
- 5: Consider for Award (top 2.5%)
- 4: Conference acceptance
- 3: Findings acceptance
- 2: Resubmit next cycle
- 1: Do not resubmit

## Reproducibility
**Scale: 1-5**
- 5: "They could easily reproduce the results"
- 4: "They could mostly reproduce the results"
- 3: "They could reproduce the results with some difficulty"
- 2: "They would be hard pressed to reproduce the results"
- 1: "They would not be able to reproduce the results"

## Datasets & Software
**Scale: 1-5** (identical scales)
- 5: Enabling impact on research choices
- 4: Useful for researchers/developers
- 3: Potentially useful
- 2: Documentary value only
- 1: No usable materials submitted

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5896
}
```

</details>

---


### Tool call

_source line 68 · 2026-05-17T02:31:39.705600+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
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

_source line 69 · 2026-05-17T02:31:39.756313+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 70 · 2026-05-17T02:32:26.651205+00:00_

I have now read the full paper including abstract, introduction, related work, method, experiments, conclusion, limitations, and appendix. I also have the ACL ARR review form scoring dimensions. Let me compile my review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1"
}
```

</details>

---


## Round 4

## Round 4

34 recorded events


### User

_source line 71 · 2026-05-17T04:47:32.907088+00:00_

[Round 2 审稿请求]:
## Round 2 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）

### Venue 信息
- **目标**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle
- **Deadline**: 2026-05-25
- **页数限制**: 正文 8 页 + unlimited references; Limitations 不计页数
- **模板**: ACL template with `[review]` option
- **匿名规则**: Double-blind

### 论文路径
`projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, appendix.tex）

### 你的审查侧重
1. **方法严谨性**：KL distillation framework 的理论支撑、Gumbel-Sigmoid 采样、Lagrangian 对偶约束的正确性
2. **实验设计**：baseline 对比公平性、统计显著性、消融实验完整性
3. **重点验证 Round 1 遗留 in_progress issues**：
   - **R1-W4** (in_progress): §3.5 梯度分析从 "theoretical contribution" 弱化为 "gradient-based motivation"，且需添加实证 gradient SNR 数据 (KL/BCE=5.76×)。检查是否已完成、数据是否可信、framing 是否合理。
   - **R1-W5** (in_progress): Lagrangian 对偶更新缺收敛分析。Appendix C 已有 convergence table (4 targets × final λ + actual sparsity)，还需 λ/sparsity 时序曲线。检查 Appendix C 是否充分。
   - **R1-W3** (open/info): 三 seed (n=3) 统计效力——检查是否有改善或 adequate justification。

### 输出格式
请按以下结构输出审稿意见：
1. Summary (2-3 sentences)
2. Strengths (bullet points)
3. Weaknesses (bullet points, 标注 severity: critical/warning/info)
4. Round 1 Issue Status (逐条确认 R1-W4, R1-W5, R1-W3 是否已修复)
5. Questions for authors
6. Missing references
7. Overall score (strong reject / weak reject / borderline / weak accept / strong accept) + confidence (1-5)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 72 · 2026-05-17T04:47:42.549598+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
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

_source line 73 · 2026-05-17T04:47:42.550043+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 74 · 2026-05-17T04:47:46.424192+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 75 · 2026-05-17T04:47:46.977239+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 76 · 2026-05-17T04:47:46.977594+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	
17	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
18	
19	\author{Anonymous}
20	
21	\begin{document}
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
32	\input{conclusion}
33	\input{limitations}
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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 77 · 2026-05-17T04:47:58.646810+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

I found comprehensive information about ACL Rolling Review 2026 reviewer guidelines, review form criteria, and related documents. Here's what the search revealed:

## Reviewer Guidelines

Reviewers for *ACL conferences and TACL should not actively try to discover the identity o
…[truncated 1809 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 12222
}
```

</details>

---


### Tool call

_source line 78 · 2026-05-17T04:48:02.781173+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5 etc.), and descriptions. I need the exact criteria names, score ranges, and what each score level means."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5 etc.), and descriptions. I need the exact criteria names, score ranges, and what each score level means."
  }
}
```

</details>

---


### Tool call

_source line 79 · 2026-05-17T04:48:03.437428+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 80 · 2026-05-17T04:48:03.489501+00:00_

1	Activation sparsity reduces the effective computation in SwiGLU-based LLMs by pruning FFN neurons at inference, but existing learned predictors trained with binary cross-entropy (BCE) require error compensation networks due to a structural mismatch: BCE decomposes per neuron while inference uses global top-$k$ allocation across all layers.
2	We train lightweight predictors (2.37M parameters per layer, 75.9M total, $<$1\% of the base model) with KL divergence, which couples all neurons through the output distribution via Gumbel-Sigmoid relaxation, eliminating the need for compensation.
3	On LLaMA-3.1-8B (WikiText-2), our KL-trained predictor achieves perplexity 11.79 at 50\% sparsity without compensation, compared to 23.31 for vanilla TEAL and 27.97 for BCE trained at 2.71$\times$ the compute budget, whose loss saturates, confirming a structural rather than computational failure.
4	Three-seed evaluation confirms training stability (PPL $11.92 \pm 0.07$, CV${<}$1\% under uniform allocation).
5	The KL advantage grows disproportionately with sparsity: 18\% relative improvement at 30\%, 49\% at 50\%, and 82\% at 70\%.
6	Cross-architecture evaluation on Mistral-7B-v0.3 confirms the advantage transfers across SwiGLU architectures of similar scale, with consistent KL-over-TEAL ratios (within 7\% at $\leq$50\% sparsity).
7	SPON's static bias correction proves near-orthogonal to the predictor (cosine similarity 0.196), providing only 2.4\% relative PPL improvement (12.08$\to$11.79 under \texttt{evaluate.py}).
8	We propose a two-dimensional taxonomy over correction granularity $\times$ training signal coupling that unifies prior methods and identify three distinct sparsity regimes---budget-surplus, budget-constrained, and capacity-limited---that govern the quality-sparsity tradeoff.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 81 · 2026-05-17T04:48:04.599428+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 82 · 2026-05-17T04:48:04.700844+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models.
5	The method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass, eliminating the need for auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{h}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importance scores from the pre-FFN hidden state $\mathbf{h}$.
26
…[truncated 13643 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 83 · 2026-05-17T04:48:07.529802+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. **Reviewer Confidence** (1-5 scale)
- **5**: "Positive that my evaluation is correct"
- **4**: "Quite sure" with unlikely but possible errors
- **3**: "Pretty sure" but chance of missing details
- **2**: "Willing to defend" but likely gaps in understanding
- **1**: "Not my area" or highly unclear paper

## 2. **Soundness** (1-5 scale with .5 increments)
- **5**: Exceptionally thorough research for its type
- **4**: Adequate support for claims; extra experiments optional
- **3**: Main claims sufficiently supported with minor gaps
- **2**: Insufficient support; major technical problems
- **1**: Insufficient rigor or not relevant to ACL

## 3. **Excitement** (1-5 scale with .5 increments)
- **5**: "Highly Exciting" - would recommend widely
- **4**: "Exciting" - would mention to others
- **3**: "Interesting" - might discuss selectively
- **2**: "Potentially Interesting" - limited personal resonance
- **1**: "Not Exciting" - lacks community relevance

## 4. **Overall Assessment** (1-5 scale with .5 increments)
- **5**: Consider for award consideration
- **4**: Conference acceptance
- **3**: Findings track acceptance
- **2**: Needs revision by next cycle
- **1**: Reject or not ACL-relevant

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 4748
}
```

</details>

---


### Tool call

_source line 84 · 2026-05-17T04:48:11.843429+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 85 · 2026-05-17T04:48:12.298437+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4, using AdamW with learning rate $1 \times 10^{-3}$ and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly; (2) \textbf{BCE predictor}, trained with per-neuron binary cross-entropy loss for 1000 and 2700 steps; (3) \textbf{Uniform allocation}, which distributes the sparsity budget equally across layers; and (4) \textbf{WINA}~\cite{liu2025teal}, an importance-weighted variant.
23	
24	
25	\subsection{Main Results}
26	
27	Table~\ref{tab:main} presen
…[truncated 12302 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 86 · 2026-05-17T04:48:12.298905+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-17T04:48:12.350754+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling), confirming that KL distillation provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overh
…[truncated 7564 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 88 · 2026-05-17T04:48:16.950059+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 89 · 2026-05-17T04:48:17.352216+00:00_

1	\section{Introduction}
2	
3	SwiGLU feed-forward networks~\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.
4	Exploiting this sparsity can simplify inference by pruning 50\% of FFN neurons per token---without modifying the pretrained weights---eliminating the need for auxiliary compensation networks.
5	Yet the gap between potential and practice remains wide.
6	Training-free methods such as TEAL~\cite{liu2025teal} select neurons by activation magnitude alone, degrading perplexity from 6.12 (dense) to 23.31 at 50\% sparsity on LLaMA-3.1-8B~\cite{grattafiori2024llama3}---a 281\% increase.
7	Learned predictors~\cite{liu2023dejavu,gautam2026fastforward} close part of this gap by training small auxiliary networks to anticipate which neurons will be important, but they rely on error compensation modules (output rescaling networks or additive correction layers) that add 67.2M parameters and $\sim$2.7\% additional latency overhead at inference.
8	The question is whether a predictor can be trained so that compensation becomes unnecessary.
9	
10	The answer depends on the training objective.
11	Current learned predictors use binary cross-entropy (BCE) loss: each neuron is independently classified as ``keep'' or ``prune'' against an oracle mask derived from the dense model's activations.
12	The gradient of BCE with respect to neuron $j$'s score is $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$---a function of neuron $j$ alone, independent of every other neuron in the network.
13	But at inference, no neuron is evaluated in isolation.
14	TEAL's global top-$k$ mechanism~\cite{liu2025teal} ranks all neurons across all layers and retains only those above a model-wide threshold.
15	Whether neuron $j$ survives depends not on its own score but on how that score compares to the scores of all $L \times d_{\text{ff}}$ neurons.
16	This creates a structural
…[truncated 4994 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 90 · 2026-05-17T04:48:17.352661+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 91 · 2026-05-17T04:48:17.554160+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude, achieving 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking.
6	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
7	
8	\paragraph{Predictor-Based Contextual Sparsity.}
9	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
10	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with MSE supervision but retains per-neuron decomposition.
11	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction---adding inference latency.
12	PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.
13	MaskLLM~\cite{fang2024maskllm} also employs learnable masks with Gumbel relaxation and frozen weights, but targets N:M semi-structured \emph{weight} sparsity (2:4 patterns) via Gumbel-Softmax, producing fixed masks independent of input tokens.
14	In contrast, our method learns \emph{activation} masks that are contextual (per-token), unstructured (budget-constrained global top-$k$), and trained with Gumbel-Sigmoid to minimize output-distribution divergence.
15	All prior predictor-based methods use decomposed (BCE) or intermediate (MSE) objectives where each neuron's gradient is independent of other mask states.
16	Our \emph{coupled} KL objective propagates gradients through all downstream layers, optimizing for global allocation quality without compensation
…[truncated 1155 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 92 · 2026-05-17T04:48:17.605520+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 93 · 2026-05-17T04:48:17.656398+00:00_

1	\section*{Limitations}
2	
3	Our primary evaluation uses WikiText-2 perplexity, and downstream benchmarks reveal that perplexity is a poor proxy for reasoning ability at moderate sparsity: 40\% sparsity achieves PPL 8.36 but MMLU already degrades, motivating 30\% as the recommended operating point for downstream fidelity.
4	Training requires 1000 steps on WikiText-103 ($\sim$17 minutes on A6000), but a separate predictor must be trained for each sparsity target.
5	All experiments use 7--8B parameter models (LLaMA-3.1-8B, Mistral-7B-v0.3); scaling behavior to 13B or 70B models remains untested.
6	While we motivate our work with inference speedup potential, actual wall-clock acceleration depends on sparse kernel implementations (e.g., Triton, cuSPARSE) and hardware-specific memory access patterns; this work focuses on prediction quality rather than systems optimization.
7	Future directions include N:M structured sparsity for hardware-native acceleration, scaling to 13B+ models, and training a single predictor that serves multiple sparsity targets simultaneously.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 94 · 2026-05-17T04:48:20.518621+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 95 · 2026-05-17T04:48:20.770051+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Training sparsity predictors with KL divergence eliminates error compensation networks by coupling all neurons through the output distribution, resolving BCE's structural mismatch with global top-$k$ allocation.
5	The resulting predictor (75.9M params, $<$1\% of base) achieves PPL 11.79 at 50\% sparsity vs.\ 23.31 for TEAL, transfers across SwiGLU architectures of similar scale (within 7\% ratio consistency), and reveals three sparsity regimes governing the quality-allocation tradeoff.
6	
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 96 · 2026-05-17T04:48:20.870806+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-17T04:48:20.871344+00:00_

1	% =============================================================================
2	% Direction 1: KL distillation for structured/activation sparsity
3	% =============================================================================
4	
5	@inproceedings{fang2024maskllm,
6	  title = {MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models},
7	  author = {Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff Pool and Jan Kautz and Pavlo Molchanov and Xinchao Wang},
8	  year = {2024},
9	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
10	  url = {https://arxiv.org/abs/2409.17481},
11	}
12	
13	@inproceedings{xu2026spon,
14	  title = {Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models},
15	  author = {Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma},
16	  year = {2026},
17	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
18	  url = {https://arxiv.org/abs/2512.12744},
19	}
20	
21	@inproceedings{muralidharan2024minitron,
22	  title = {Compact Language Models via Pruning and Knowledge Distillation},
23	  author = {Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marcin Chochowski and Mostofa Patwary and Mohammad Shoeybi and Bryan Catanzaro and Jan Kautz and Pavlo Molchanov},
24	  year = {2024},
25	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
26	  url = {https://arxiv.org/abs/2407.14679},
27	}
28	
29	
30	% =============================================================================
31	% Direction 3: SPON and learnable bias correction for sparsity
32	% =============================================================================
33	
34	@article{gautam2026fastforward,
35	  title = {Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity},
36	  author = {Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott and Naras
…[truncated 8151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 98 · 2026-05-17T04:49:09.601453+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the COMPLETE review form with ALL fields, scoring dimensions, their exact scales, and the complete description of each score level. Include all fields such as soundness, excitement, overall assessment, confidence, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the COMPLETE review form with ALL fields, scoring dimensions, their exact scales, and the complete description of each score level. Include all fields such as soundness, excitement, overall assessment, confidence, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 99 · 2026-05-17T04:49:10.605901+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the key reviewer guidelines: what aspects should reviewers focus on, what counts as major/minor weaknesses, guidance on soundness evaluation, and what makes a good review."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the key reviewer guidelines: what aspects should reviewers focus on, what counts as major/minor weaknesses, guidance on soundness evaluation, and what makes a good review."
  }
}
```

</details>

---


### Tool result

_source line 100 · 2026-05-17T04:49:16.328601+00:00_

# Key ARR Reviewer Guidelines Summary

## Core Review Focus Areas

Reviewers should concentrate on four main tasks:

1. **Assignment validation** – Confirm expertise match and absence of conflicts of interest
2. **Technical soundness** – Evaluate methodology, proofs, and experimental rigor
3. **Clarity and specificity** – Identify vague claims and missing details
4. **Constructive feedback** – Provide actionable suggestions in professional tone

## Major vs. Minor Weaknesses

**Major weaknesses** include:
- Fundamental methodological flaws or incomplete proofs
- Missing critical comparisons directly relevant to core claims
- Anonymity violations or ethics violations
- Hallucinated references or plagiarism

**Minor weaknesses** (suggestions, not rejection grounds):
- Missing recent preprints or concurrent work
- Potential additional experiments beyond the paper's scope
- Writing improvements or clarity enhancements
- Acknowledged limitations already disclosed by authors

## Soundness Evaluation Guidance

The guidelines emphasize that "soundness scores must be justified by the review text." Key principles include:

- Distinguish between technical validity and personal interest (reflected separately in excitement scores)
- Specify exactly what aspects were checked versus unchecked
- Justify confidence levels through concrete evidence
- Avoid conflating limitations with fundamental flaws

## Hallmarks of Strong Reviews

Effective reviews demonstrate:

- **Specificity**: Reference concrete line numbers, methods, or results rather than vague complaints
- **Evidence-based critique**: Support claims with citations or reasoning
- **Professional tone**: Constructive feedback written as colleague-to-colleague
- **Calibrated expectations**: Assess papers against their stated contributions, not personal preferences
- **Good faith engagement**: Acknowledge author responses and update assessments accordingly

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5722
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-17T04:49:17.882075+00:00_

# ACL Rolling Review Form - Complete Structure

## Primary Evaluation Dimensions

### 1. **Reviewer Confidence** (5-point scale)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

### 2. **Soundness** (1-5 scale with half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

### 3. **Excitement** (1-5 scale with half-point increments)
- **5**: "Highly Exciting: I would recommend this paper to others."
- **4**: "Exciting: I would mention this paper to others."
- **3**: "Interesting: I might mention some points of this paper."
- **2**: "Potentially Interesting: this paper does not resonate with me."
- **1**: "Not Exciting: this paper does not resonate with me."

### 4. **Overall Assessment** (1-5 scale with half-point increments)
- **5**: "Consider for Award: up to top 2.5% papers"
- **4.5**: "Borderline Award"
- **4**: "Conference: I think this paper could be accepted."
- **3.5**: "Borderline Conference"
- **3**: "Findings: I think this paper could be accepted to the Findings of the ACL."
- **2.5**: "Borderline Findings"
- **2**: "Resubmit next cycle: substantial revisions needed"
- **1.5**: "Resubmit after next cycle: substantial revisions cannot be completed soon"
- **1**: "Do not resubmit"

## Additional Assessment Fields

### 5. **Reproducibility
…[truncated 1695 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8280
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-17T04:51:08.357743+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 2 Review — Reviewer 1（方法严谨性 + 实验设计）\n\n### 1. Summary\n\n本文提出用 KL 散度替代 BCE 训练 SwiGLU LLM 的上下文稀疏预测器，通过 Gumbel-Sigmoid 松弛和自适应惩罚系数实现端到端可微训练。方法在 LLaMA-3.1-8B 上 50% 稀疏度达到 PPL 11.79（对比 TEAL 23.31），并在 Mistral-7B 上验证跨架构一致性。论文还提出了二维分类法和三种稀疏 regime 的分析框架。\n\n---\n\n### 2. Strengths\n\n- **核心贡献清晰且可验证**：KL vs BCE 的结构性差异论证（§3.6 梯度分析）逻辑自洽，且有实证 SNR 数据支撑（5.76×）。\n- **消融设计良好**：Table 3 系统隔离了 loss function（ΔP=26.23）vs relaxation method（ΔP=3.98），明确了 KL 是主要贡献因素。BCE+Gumbel+Lagrangian 实验（PPL 38.02）特别有说服力，排除了 Gumbel 本身带来改进的假设。\n- **Iso-compute 分析**（§4.3）：BCE 2700 步 loss 饱和（Δ=-0.006）证明了结构性失败而非计算不足。\n- **Cross-architecture 验证**：两个不同架构（LLaMA/Mistral）上 advantage ratio 的一致性（≤50% 时 within 7%）增强了泛化性 claim 的可信度。\n- **Regime 分析有实用价值**：budget-surplus/constrained/capacity-limited 三分法对实践者选择稀疏度有指导意义。\n- **Limitations 诚实**：明确承认无实际加速、仅 7-8B 模型、per-target 训练的限制。\n\n---\n\n### 3. Weaknesses\n\n**W1 [critical] \"Lagrangian\" 术语不准确，非标准对偶方法**\n- 具体位置：§3.5, Eq. 9-10\n- 问题：Eq. 9 是带 deadzone 的二次惩罚项 λ·clamp(|s̄-(1-ρ)|-ε, min=0)²，Eq. 10 的更新规则是几何倍增/减半（×2/×0.5），这既不是标准 augmented Lagrangian（需 λ ← λ + η·violation），也不是对偶上升法。将其称为 \"Lagrangian\" 和 \"dual variable\" 存在术语误导。这是一个带自适应权重的惩罚方法（penalty method with adaptive coefficient）。\n- 影响：审稿人可能质疑作者对优化理论的理解深度；更重要的是，penalty method 不保证满足 KKT 条件，论文也未讨论这一局限。\n- 建议：(1) 改称 \"adaptive penalty controller\" 或明确说明这是对 Lagrangian 的工程化简化；(2) 讨论为何不使用标准对偶上升以及当前方案的收敛保证。\n\n**W2 [critical] Appendix C 缺少 λ/sparsity 时序曲线（R1-W5 未完全修复）**\n- 具体位置：Appendix C (§C, Table 7)\n- 问题：Table 7 仅报告最终状态（final λ + actual sparsity + deviation），满足\"是否收敛\"的验证。但缺少训练过程中 λ 和 actual sparsity 随 step 变化的时序曲线。Director 明确要求 \"还需 λ/sparsity 时序曲线\"。\n- 为什么重要：(1) 30% 和 70% target 的 λ 均 hit cap（5000 和 1000），表明系统可能在 cap boundary 震荡而非真正收敛；(2) 文中提到 \"最后 ~100 步 loss 轻微上升\"（Appendix C 末段），时序曲线可以展示这是否与 λ 动态相关；(3) 无曲线无法验证 \"~10 步达到稳态\" 的 claim。\n- 建议：补充 Figure 展示至少 30%/50%/70% 三个 target 的 (step, λ) 和 (step, actual_sparsity) 曲线。\n\n**W3 [warning] 梯度 SNR 定义不明确且样本量小**\n- 具体位置：§3.6, \"Empirical verification\" 段落\n- 问题：(1) \"gradient SNR\" 未给出数学定义——是 mean(|grad|)/std(|grad|) over steps? over neurons? over layers? 读者无法 verify 或 reproduce 这个数字。(2) 仅 80 步的测量，对于 SNR 估计（尤其是分层报告 early/late layers）样本量偏小。(3) 数值 5.77×10⁻⁵ vs 1.00×10⁻⁵ 的 ratio 是 5.77×，但文中写 \"5.76×\"——小数点精度不一致。\n- 建议：(1) 明确 SNR 的数学公式；(2) 增加到至少 200+ steps 或报告 bootstrap CI；(3) 修正 5.77/1.00=5.77 vs claim 5.76 的不一致。\n\n**W4 [warning] n=3 seeds 统计效力不足（R1-W3 未改善）**\n- 具体位置：§4.7, Appendix E\n- 问题：论文仍使用 3 seeds，仅以 CV<1% 作为 justification。CV<1% 说明方法 variance 小，但不等于效力足够检测方法间差异。对于主表中 KL global (11.79) vs KL uniform (11.96) 之差（0.17），以 std=0.07 计算，即使 paired t-test 也仅有 n=3 自由度=2，无法确信 p<0.05。\n- 此外，cross-arch claim \"within 7%\" 完全基于点估计（无 CI），无法区分真实差异与噪声。\n- 建议：(1) 至少补充 5 seeds，或明确声明 \"global vs uniform 差异不显著\"；(2) 对 cross-arch ratio 报告 bootstrap CI。\n\n**W5 [warning] 无实际推理加速，且 overhead 表述可能误导读者**\n- 具体位置：Appendix A, Table 5\n- 问题：论文动机强调 \"reduces effective computation\"（Abstract 第一句），但实测增加 6.4% latency overhead。虽然 Limitations 中诚实说明了这一点，但 Abstract/Introduction 的 framing 可能让读者期望实际加速。\"Eliminating compensation network\" 节省的 2.7% latency 被 predictor 自身的 6.4% overhead 抵消，net effect 是变慢。\n- 建议：Abstract 首句明确 \"prediction quality\" 而非暗示 \"reduces computation\"；或在 Experiments 主文中简要说明当前无加速。\n\n**W6 [info] 30% 稀疏度 MMLU 异常未充分解释**\n- 具体位置：Table 2, §4.5\n- 问题：KL global 在 30% 稀疏度的 MMLU 仅 25.27%（接近随机），而 KL uniform 达 40.61%。这是 15pp 差异，暗示全局分配在低稀疏度时 actively harmful for knowledge tasks。论文将此归因于 \"global top-k starves knowledge-critical layers\"，但缺乏进一步分析：具体哪些 layers 被 starved？layer-wise allocation 分布是什么样？\n- 建议：补充 30% 稀疏度下 global top-k 的 per-layer 实际保留率分布，验证 \"starve\" 假设。\n\n---\n\n### 4. Round 1 Issue Status\n\n| Issue | Status | 评估 |\n|-------|--------|------|\n| **R1-W4** (gradient motivation reframing + SNR data) | ✅ 基本完成 | §3.6 标题改为 \"Gradient-Based Motivation\"，framing 合理。SNR 5.76× 数据已添加且与 layer-depth 理论一致。但 SNR 定义不明确（see W3 above）。 |\n| **R1-W5** (Lagrangian convergence) | ⚠️ 部分完成 | Table 7 提供了 4 targets 的最终收敛状态，满足基本验证。但缺少 λ/sparsity 时序曲线（see W2 above），且两个 target hit cap 的情况未充分讨论。 |\n| **R1-W3** (n=3 statistical power) | ❌ 未改善 | 仍为 3 seeds，仅增加了 downstream metric 的 std 报告。未增加 seed 数量，也未提供 adequate justification（如 power analysis 或 paired comparison CI）。 |\n\n---\n\n### 5. Questions for Authors\n\n1. Eq. 10 的几何倍增如何保证收敛？当 λ hit cap 时（30%: λ=5000, 70%: λ=1000），是否意味着约束无法被精确满足？30% 的 5% deviation 是否可接受？\n2. Gradient SNR 的精确定义是什么？是 E[grad²] / Var[grad] 还是 |E[grad]| / std(grad)？over what dimensions (neurons? steps? sequences)?\n3. 如果将 KL global 在 30% 稀疏度的 MMLU 25.27% 与 dense 的 65.27% 比较，这是 40pp 的退化。论文推荐的实际使用方案是什么——30% uniform？还是 50% global？\n4. BCE+Gumbel+Lagrangian (PPL 38.02) 比 vanilla BCE (27.97) 更差，作者解释为 \"Lagrangian 干扰 per-neuron optimization\"。但这是否也说明 Gumbel-Sigmoid 本身引入了噪声？如果去掉 Lagrangian 只用 BCE+Gumbel 结果如何？\n5. 论文 claim SPON cosine similarity 0.196 为 \"near-orthogonal\"，但 0.196 并不特别接近 0。在 14336 维空间中，随机向量的 expected cosine similarity ≈ 0。0.196 是否实际上表示 moderate positive correlation？\n\n---\n\n### 6. Missing References\n\n- **Wanda (Sun et al., 2024)**: 结构化/非结构化剪枝的重要 baseline，尤其在讨论 neuron importance 时应对比。\n- **SparseGPT (Frantar & Alistarh, 2023)**: one-shot pruning 的代表方法，作为 broader pruning landscape 的参照。\n- **Mixture-of-Experts (Fedus et al., 2022)**: conditional computation 的另一范式，Related Work 中应 acknowledge。\n- 缺少对 Gumbel-Sigmoid 变体的直接引用——Jang et al. 2017 是 Gumbel-Softmax (categorical)，Gumbel-Sigmoid (binary) 的标准引用应为 Maddison et al. 2017 (Concrete distribution) 或 Louizos et al. 2018 (L0 regularization)。\n\n---\n\n### 7. Overall Assessment\n\n**Soundness**: 3.5/5\n核心 KL vs BCE 的结构性论证正确且实验支撑充分。但 \"Lagrangian\" 术语误用、SNR 定义缺失、n=3 统计效力不足降低了 rigor。消融实验设计良好。\n\n**Excitement**: 3.5/5\n贡献有实用价值（消除 compensation network、regime 分析），但 scope 限于 7-8B 模型 + WikiText，且无实际加速演示，限制了 impact。\n\n**Reproducibility**: 4/5\n超参数详尽，实验 protocol 清晰。缺少代码发布承诺和 SNR 测量的精确定义。\n\n**Overall**: 3.5 (Borderline Conference)\n论文有一个清晰的核心贡献（KL training for sparsity prediction），消融充分，跨架构验证有说服力。但 Lagrangian 术语问题（W1）和缺少收敛曲线（W2）是方法严谨性的硬伤；n=3 统计效力（W4）和 SNR 定义缺失（W3）进一步削弱可信度。如果 W1+W2 能在 revision 中修复（改称 penalty method + 补充曲线），且 W3 的 SNR 给出明确定义，可升至 weak accept。\n\n**Confidence**: 4/5\n\"Quite sure. I tried to check the important points carefully.\" 对优化理论和稀疏推理均有经验，仔细检查了梯度推导和实验设计。",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 2 Review — Reviewer 1（方法严谨性 + 实验设计）\n\n### 1. Summary\n\n本文提出用 KL 散度替代 BCE 训练 SwiGLU LLM 的上下文稀疏预测器，通过 Gumbel-Sigmoid 松弛和自适应惩罚系数实现端到端可微训练。方法在 LLaMA-3.1-8B 上 50% 稀疏度达到 PPL 11.79（对比 TEAL 23.31），并在 Mistral-7B 上验证跨架构一致性。论文还提出了二维分类法和三种稀疏 regime 的分析框架。\n\n---\n\n### 2. Strengths\n\n- **核心贡献清晰且可验证**：KL vs BCE 的结构性差异论证（§3.6 梯度分析）逻辑自洽，且有实证 SNR 数据支撑（5.76×）。\n- **消融设计良好**：Table 3 系统隔离了 loss function（ΔP=26.23）vs relaxation method（ΔP=3.98），明确了 KL 是主要贡献因素。BCE+Gumbel+Lagrangian 实验（PPL 38.02）特别有说服力，排除了 Gumbel 本身带来改进的假设。\n- **Iso-compute 分析**（§4.3）：BCE 2700 步 loss 饱和（Δ=-0.006）证明了结构性失败而非计算不足。\n- **Cross-architecture 验证**：两个不同架构（LLaMA/Mistral）上 advantage ratio 的一致性（≤50% 时 within 7%）增强了泛化性 claim 的可信度。\n- **Regime 分析有实用价值**：budget-surplus/constrained/capacity-limited 三分法对实践者选择稀疏度有指导意义。\n- **Limitations 诚实**：明确承认无实际加速、仅 7-8B 模型、per-target 训练的限制。\n\n---\n\n### 3. Weaknesses\n\n**W1 [critical] \"Lagrangian\" 术语不准确，非标准对偶方法**\n- 具体位置：§3.5, Eq. 9-10\n- 问题：Eq. 9 是带 deadzone 的二次惩罚项 λ·clamp(|s̄-(1-ρ)|-ε, min=0)²，Eq. 10 的更新规则是几何倍增/减半（×2/×0.5），这既不是标准 augmented Lagrangian（需 λ ← λ + η·violation），也不是对偶上升法。将其称为 \"Lagrangian\" 和 \"dual variable\" 存在术语误导。这是一个带自适应权重的惩罚方法（penalty method with adaptive coefficient）。\n- 影响：审稿人可能质疑作者对优化理论的理解深度；更重要的是，penalty method 不保证满足 KKT 条件，论文也未讨论这一局限。\n- 建议：(1) 改称 \"adaptive penalty controller\" 或明确说明这是对 Lagrangian 的工程化简化；(2) 讨论为何不使用标准对偶上升以及当前方案的收敛保证。\n\n**W2 [critical] Appendix C 缺少 λ/sparsity 时序曲线（R1-W5 未完全修复）**\n- 具体位置：Appendix C (§C, Table 7)\n- 问题：Table 7 仅报告最终状态（final λ + actual sparsity + deviation），满足\"是否收敛\"的验证。但缺少训练过程中 λ 和 actual sparsity 随 step 变化的时序曲线。Director 明确要求 \"还需 λ/sparsity 时序曲线\"。\n- 为什么重要：(1) 30% 和 70% target 的 λ 均 hit cap（5000 和 1000），表明系统可能在 cap boundary 震荡而非真正收敛；(2) 文中提到 \"最后 ~100 步 loss 轻微上升\"（Appendix C 末段），时序曲线可以展示这是否与 λ 动态相关；(3) 无曲线无法验证 \"~10 步达到稳态\" 的 claim。\n- 建议：补充 Figure 展示至少 30%/50%/70% 三个 target 的 (step, λ) 和 (step, actual_sparsity) 曲线。\n\n**W3 [warning] 梯度 SNR 定义不明确且样本量小**\n- 具体位置：§3.6, \"Empirical verification\" 段落\n- 问题：(1) \"gradient SNR\" 未给出数学定义——是 mean(|grad|)/std(|grad|) over steps? over neurons? over layers? 读者无法 verify 或 reproduce 这个数字。(2) 仅 80 步的测量，对于 SNR 估计（尤其是分层报告 early/late layers）样本量偏小。(3) 数值 5.77×10⁻⁵ vs 1.00×10⁻⁵ 的 ratio 是 5.77×，但文中写 \"5.76×\"——小数点精度不一致。\n- 建议：(1) 明确 SNR 的数学公式；(2) 增加到至少 200+ steps 或报告 bootstrap CI；(3) 修正 5.77/1.00=5.77 vs claim 5.76 的不一致。\n\n**W4 [warning] n=3 seeds 统计效力不足（R1-W3 未改善）**\n- 具体位置：§4.7, Appendix E\n- 问题：论文仍使用 3 seeds，仅以 CV<1% 作为 justification。CV<1% 说明方法 variance 小，但不等于效力足够检测方法间差异。对于主表中 KL global (11.79) vs KL uniform (11.96) 之差（0.17），以 std=0.07 计算，即使 paired t-test 也仅有 n=3 自由度=2，无法确信 p<0.05。\n- 此外，cross-arch claim \"within 7%\" 完全基于点估计（无 CI），无法区分真实差异与噪声。\n- 建议：(1) 至少补充 5 seeds，或明确声明 \"global vs uniform 差异不显著\"；(2) 对 cross-arch ratio 报告 bootstrap CI。\n\n**W5 [warning] 无实际推理加速，且 overhead 表述可能误导读者**\n- 具体位置：Appendix A, Table 5\n- 问题：论文动机强调 \"reduces effective computation\"（Abstract 第一句），但实测增加 6.4% latency overhead。虽然 Limitations 中诚实说明了这一点，但 Abstract/Introduction 的 framing 可能让读者期望实际加速。\"Eliminating compensation network\" 节省的 2.7% latency 被 predictor 自身的 6.4% overhead 抵消，net effect 是变慢。\n- 建议：Abstract 首句明确 \"prediction quality\" 而非暗示 \"reduces computation\"；或在 Experiments 主文中简要说明当前无加速。\n\n**W6 [info] 30% 稀疏度 MMLU 异常未充分解释**\n- 具体位置：Table 2, §4.5\n- 问题：KL global 在 30% 稀疏度的 MMLU 仅 25.27%（接近随机），而 KL uniform 达 40.61%。这是 15pp 差异，暗示全局分配在低稀疏度时 actively harmful for knowledge tasks。论文将此归因于 \"global top-k starves knowledge-critical layers\"，但缺乏进一步分析：具体哪些 layers 被 starved？layer-wise allocation 分布是什么样？\n- 建议：补充 30% 稀疏度下 global top-k 的 per-layer 实际保留率分布，验证 \"starve\" 假设。\n\n---\n\n### 4. Round 1 Issue Status\n\n| Issue | Status | 评估 |\n|-------|--------|------|\n| **R1-W4** (gradient motivation reframing + SNR data) | ✅ 基本完成 | §3.6 标题改为 \"Gradient-Based Motivation\"，framing 合理。SNR 5.76× 数据已添加且与 layer-depth 理论一致。但 SNR 定义不明确（see W3 above）。 |\n| **R1-W5** (Lagrangian convergence) | ⚠️ 部分完成 | Table 7 提供了 4 targets 的最终收敛状态，满足基本验证。但缺少 λ/sparsity 时序曲线（see W2 above），且两个 target hit cap 的情况未充分讨论。 |\n| **R1-W3** (n=3 statistical power) | ❌ 未改善 | 仍为 3 seeds，仅增加了 downstream metric 的 std 报告。未增加 seed 数量，也未提供 adequate justification（如 power analysis 或 paired comparison CI）。 |\n\n---\n\n### 5. Questions for Authors\n\n1. Eq. 10 的几何倍增如何保证收敛？当 λ hit cap 时（30%: λ=5000, 70%: λ=1000），是否意味着约束无法被精确满足？30% 的 5% deviation 是否可接受？\n2. Gradient SNR 的精确定义是什么？是 E[grad²] / Var[grad] 还是 |E[grad]| / std(grad)？over what dimensions (neurons? steps? sequences)?\n3. 如果将 KL global 在 30% 稀疏度的 MMLU 25.27% 与 dense 的 65.27% 比较，这是 40pp 的退化。论文推荐的实际使用方案是什么——30% uniform？还是 50% global？\n4. BCE+Gumbel+Lagrangian (PPL 38.02) 比 vanilla BCE (27.97) 更差，作者解释为 \"Lagrangian 干扰 per-neuron optimization\"。但这是否也说明 Gumbel-Sigmoid 本身引入了噪声？如果去掉 Lagrangian 只用 BCE+Gumbel 结果如何？\n5. 论文 claim SPON cosine similarity 0.196 为 \"near-orthogonal\"，但 0.196 并不特别接近 0。在 14336 维空间中，随机向量的 expected cosine similarity ≈ 0。0.196 是否实际上表示 moderate positive correlation？\n\n---\n\n### 6. Missing References\n\n- **Wanda (Sun et al., 2024)**: 结构化/非结构化剪枝的重要 baseline，尤其在讨论 neuron importance 时应对比。\n- **SparseGPT (Frantar & Alistarh, 2023)**: one-shot pruning 的代表方法，作为 broader pruning landscape 的参照。\n- **Mixture-of-Experts (Fedus et al., 2022)**: conditional computation 的另一范式，Related Work 中应 acknowledge。\n- 缺少对 Gumbel-Sigmoid 变体的直接引用——Jang et al. 2017 是 Gumbel-Softmax (categorical)，Gumbel-Sigmoid (binary) 的标准引用应为 Maddison et al. 2017 (Concrete distribution) 或 Louizos et al. 2018 (L0 regularization)。\n\n---\n\n### 7. Overall Assessment\n\n**Soundness**: 3.5/5\n核心 KL vs BCE 的结构性论证正确且实验支撑充分。但 \"Lagrangian\" 术语误用、SNR 定义缺失、n=3 统计效力不足降低了 rigor。消融实验设计良好。\n\n**Excitement**: 3.5/5\n贡献有实用价值（消除 compensation network、regime 分析），但 scope 限于 7-8B 模型 + WikiText，且无实际加速演示，限制了 impact。\n\n**Reproducibility**: 4/5\n超参数详尽，实验 protocol 清晰。缺少代码发布承诺和 SNR 测量的精确定义。\n\n**Overall**: 3.5 (Borderline Conference)\n论文有一个清晰的核心贡献（KL training for sparsity prediction），消融充分，跨架构验证有说服力。但 Lagrangian 术语问题（W1）和缺少收敛曲线（W2）是方法严谨性的硬伤；n=3 统计效力（W4）和 SNR 定义缺失（W3）进一步削弱可信度。如果 W1+W2 能在 revision 中修复（改称 penalty method + 补充曲线），且 W3 的 SNR 给出明确定义，可升至 weak accept。\n\n**Confidence**: 4/5\n\"Quite sure. I tried to check the important points carefully.\" 对优化理论和稀疏推理均有经验，仔细检查了梯度推导和实验设计。",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 103 · 2026-05-17T04:51:12.677740+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4319
}
```

</details>

---


### Assistant

_source line 104 · 2026-05-17T04:51:18.739743+00:00_

审稿意见已提交给 Review Director。

总结：整体评分 **3.5/5 (Borderline Conference)**。核心贡献（KL 替代 BCE 训练稀疏预测器）有效且消融充分，但存在三个需修复的问题：(1) "Lagrangian" 术语实际是 penalty method，需正名；(2) Appendix C 缺 λ/sparsity 时序曲线（R1-W5 未完全关闭）；(3) gradient SNR 定义缺失。R1-W3（n=3 统计效力）未改善，仍是减分项但非 deal-breaker。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1"
}
```

</details>

---


## Round 5

## Round 5

4 recorded events


### User

_source line 105 · 2026-05-17T04:52:10.995353+00:00_

[Round 2 审稿请求]:
## 交叉分享 — Reviewer 2 的完整审稿意见

请逐条回应 Reviewer 2 的每个 Weakness：对每一条标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

以下是 Reviewer 2 的完整审稿意见：

### Summary
This paper proposes training lightweight MLP sparsity predictors with KL divergence (instead of BCE) combined with Gumbel-Sigmoid relaxation to predict which FFN neurons to prune at inference in SwiGLU-based LLMs. The key argument is that KL couples all neurons through the output distribution, resolving BCE's structural mismatch with global top-k allocation. Experiments on LLaMA-3.1-8B and Mistral-7B show substantial PPL improvements over TEAL baselines, with analysis of sparsity regimes and a 2D taxonomy positioning the contribution.

### Strengths
- Clear structural argument: The BCE vs. KL gradient analysis (§3.5) is well-motivated and the formal derivation (Eq. 7-8) makes the "coupling through downstream Jacobian" argument concrete and verifiable.
- Thorough ablation design: The loss-function isolation experiment (BCE + Gumbel + Lagrangian → PPL 38.02) cleanly demonstrates that the KL objective, not the relaxation mechanism, is the decisive factor.
- Honest limitations: The paper explicitly acknowledges that 6.4% overhead does NOT translate to speedup without sparse kernels, and that PPL is a poor proxy for reasoning (§4.4). The regime analysis (budget-surplus vs. capacity-limited) is a genuinely useful framework.
- Reproducibility: Training details are sufficient (1000 steps, WikiText-103, batch=4, AdamW, lr=1e-3, cosine decay). Three-seed variance reported.
- SPON orthogonality analysis is convincing: Cosine similarity 0.196 with quantitative PPL decomposition clearly separates the two methods' contributions.

### Weaknesses

**W1 [critical] — Novelty is incremental: known components in a predictable configuration**
The paper combines: (1) KL distillation (standard in model compression since Hinton 2015), (2) Gumbel-Sigmoid relaxation (Jang et al. 2017), (3) lightweight MLP predictor (DejaVu 2023). The 2D taxonomy frames this as "filling an unexplored cell," but the combination is the obvious next step once you observe that SPON uses KL (static) and FastForward uses per-token (BCE). A reviewer could ask: why hadn't anyone done this already? If the answer is "it's straightforward to combine," the novelty bar for a main conference paper may not be met.

**W2 [critical] — The "relative advantage grows with sparsity" claim is partially an artifact of baseline collapse**
The paper's central scaling narrative (18% → 49% → 82% advantage) measures (TEAL - KL) / TEAL. When TEAL collapses from 23.31 to 100.11, any reasonable method will show a growing "relative advantage." It would be more informative to report KL/Dense ratio across sparsity levels: 1.47× at 30%, 1.93× at 50%, 2.93× at 70%.

**W3 [warning] — Scale limitation undermines generality claims**
Only two models tested (LLaMA-3.1-8B and Mistral-7B-v0.3), both 7-8B parameters with SwiGLU. No experiments on 13B, 70B, or non-SwiGLU architectures. Introduction/Abstract still frame it as if it's a general structural property.

**W4 [warning] — Downstream task collapse at 50% sparsity raises practical concerns**
At 50% sparsity, all methods collapse on MMLU (27.89% ≈ random) and GSM8K (<2.2%). At 30%, KL-global hurts MMLU (25.27% vs. TEAL 38.61%). The practical operating point is ≤30%, where PPL advantage is modest (8.98 vs. 10.97).

**W5 [warning] — Em-dash usage signals AI-generated text**
12+ instances of explanatory em-dashes (---) in running text across introduction.tex, method.tex, abstract.tex, related_work.tex.

**W6 [warning] — "Lagrangian" formulation is misleading terminology**
Eq. 7-8 describe a squared penalty with deadzone and multiplicative weight update, not a true Lagrangian relaxation. "Adaptive penalty method" would be more accurate.

**W7 [info] — Reference count is low for EMNLP**
22 unique references is below typical EMNLP papers (30-50). Missing: MoE, Wanda, SparseGPT, sequence-level KD, Triton.

### Questions for Authors
1. Have you measured per-neuron prediction accuracy of the KL predictor against the oracle top-k mask?
2. What happens when you train a single predictor on multiple sparsity targets?
3. The gradient SNR analysis reports absolute values of ~10⁻⁵. Is this measured on the raw gradient or after optimizer adaptation?
4. At 30% sparsity, KL-global MMLU (25.27%) is significantly worse than both TEAL (38.61%) and KL-uniform (40.61%). Can you explain why?

### Overall Score
3/5 (Findings) — Solid execution of a logical idea with clear experimental validation, but novelty is incremental and scale is limited. Suitable for Findings of EMNLP rather than the main conference.
Confidence: 4/5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 106 · 2026-05-17T04:53:21.354270+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## 交叉回应 — Reviewer 1 对 Reviewer 2 意见的逐条回应\n\n---\n\n**[REBUT] R2-W1: Novelty is incremental**\n\n不完全同意 \"predictable combination\" 的判断。关键证据是 Table 3 的 BCE+Gumbel+Lagrangian 实验（PPL 38.02）：如果组合是 \"obvious\"，那为什么将 Gumbel-Sigmoid 和 Lagrangian 直接应用于 BCE 反而比 vanilla BCE（27.97）更差？这说明 Gumbel 松弛与 loss function 之间存在非平凡的交互——Lagrangian penalty 在 BCE 下会干扰 per-neuron optimization（§4.4 第三段明确讨论）。仅仅 \"填表格\" 不足以构成贡献，但论文的核心洞察不是 \"KL 比 BCE 好\" 这个 general statement，而是具体机制：BCE 梯度 factorize per-neuron（Eq. 8）导致无法学到 global top-k 所需的 inter-neuron coupling。这个 mismatch 的诊断（§3.6 gradient analysis）+ 实证验证（iso-compute saturation）超越了简单 component combination。\n\n但 R2 的质疑并非无理：论文 2D taxonomy 的 framing 确实有 \"填空\" 嫌疑，且 KL distillation 本身不新。如果这篇论文去掉 gradient analysis 和 regime analysis，只剩 \"KL 比 BCE 好\"，那确实 incremental。目前版本的 contribution 在 borderline。\n\n---\n\n**[AGREE] R2-W2: Relative advantage 部分是 baseline collapse 的 artifact**\n\n完全同意。(TEAL-KL)/TEAL 作为 metric 在 TEAL 崩溃时会 inflate。Table 4 数据：\n- 30%: KL/Dense = 8.98/6.12 = 1.47×\n- 50%: KL/Dense = 11.79/6.12 = 1.93×\n- 70%: KL/Dense = 17.91/6.12 = 2.93×\n\n这个 framing 更诚实地反映了 KL predictor 自身的质量退化曲线。论文 Abstract 第 5 行 \"18% at 30%, 49% at 50%, and 82% at 70%\" 的叙事过度依赖于 TEAL 的失败来 inflate 自己的优势。建议作者至少同时报告 KL/Dense ratio。\n\n不过补充一点：即使 reframe 为 KL/Dense，从 1.47× 到 2.93× 的增长仍然表明 KL predictor 在高稀疏度下也显著退化（dense 到 2.93× 的 gap 并不小）。这更凸显了 capacity-limited regime（§4.5）的诚实性。\n\n---\n\n**[AGREE] R2-W3: Scale limitation undermines generality claims**\n\n同意。两个 7-8B SwiGLU 模型不足以支撑 \"structural property of SwiGLU networks\"（§4.6 末句）的泛化 claim。尤其是：\n- 13B/70B 模型的 layer 数和 d_ff 不同，Jacobian chain（factor (b) in Eq. 12）的 depth 效应可能质变\n- Limitations 中承认了这一点，但 Introduction 和 Abstract 的 framing 仍然偏 general\n\n不过严格来说，论文使用的措辞是 \"transfers across SwiGLU architectures of similar scale\"（Abstract 第 6 行），加了 \"of similar scale\" 的限定词，这在 Round 1 后已有改进。问题在于 §4.6 最后一句 \"evidence that the method exploits a structural property of SwiGLU networks\" 仍然过强——应加 \"at 7-8B scale\" 限定。\n\n---\n\n**[AGREE] R2-W4: Downstream collapse raises practical concerns**\n\n同意这是一个重要的实践限制。数据支撑：\n- 50% sparsity: MMLU 27.89% ≈ random（Table 2）\n- 30% KL-global: MMLU 25.27%，甚至比 TEAL 的 38.61% 更差（Table 2）\n- 实际推荐操作点仅为 30% uniform（MMLU 40.61%），PPL 优势仅 8.82 vs 10.97\n\n论文的 regime 分析（§4.5）诚实地展示了这些数据，并且 Limitations 中推荐 30% 为 \"recommended operating point for downstream fidelity\"。但 R2 的批评是合理的：如果实际有用的区间只有 ≤30%，那 50%/70% 的大幅 PPL 优势在实践中意义有限（downstream 都崩了）。\n\n论文核心贡献仍然成立（方法论 + 分析框架），但 impact 确实被这一限制约束。\n\n---\n\n**[REBUT] R2-W5: Em-dash usage signals AI-generated text**\n\n部分不同意将此列为 [warning] 级别问题。\n\n首先事实确认：LaTeX 中 `---` 产生 em-dash，论文中确实有多处使用（如 Abstract 第 8 行 \"three distinct sparsity regimes---budget-surplus, budget-constrained, and capacity-limited---\"；Introduction 中也有类似用法）。\n\n但作为审稿意见，这属于 stylistic preference 而非学术质量问题。Em-dash 在英文学术写作中是合法标点（Chicago Manual of Style 认可），许多人类作者也使用。将 em-dash 等同于 \"AI-generated\" 是一种 heuristic，不是 evidence。这个问题最多属于 [info] 级别的 minor suggestion，不应影响接收决定。\n\n如果真要修，建议作者减少使用频率即可（改为逗号或拆分句子），但这不应是审稿意见中的 warning。\n\n---\n\n**[AGREE] R2-W6: \"Lagrangian\" formulation is misleading terminology**\n\n完全同意，这与我 Round 2 review 中的 W1 是同一问题。Eq. 9 是二次惩罚 + deadzone，Eq. 10 是几何倍增/减半——这不是 Lagrangian dual ascent。\"Adaptive penalty controller\" 更准确。两位 reviewer 独立指出同一问题，增强了这个 concern 的权重。\n\n---\n\n**[AGREE] R2-W7: Reference count is low**\n\n同意。我在自己的 review 中也指出缺少 Wanda、SparseGPT、MoE、Louizos et al. 2018 (L0/Concrete distribution) 等引用。22 refs 对 EMNLP main 偏少，30-40 是更合理的密度。尤其是 pruning 领域的经典工作（Wanda, SparseGPT）和 conditional computation（MoE）应该在 Related Work 中有所 acknowledge。\n\n---\n\n### 总结\n\n与 Reviewer 2 的主要分歧点：\n1. **W1 (novelty)**: 我认为论文的 gradient mismatch 诊断 + iso-compute verification + regime analysis 超越了简单 component combination，但同意 2D taxonomy framing 有填空嫌疑。Overall novelty borderline。\n2. **W5 (em-dash)**: 不应作为 warning 级别问题。\n\n与 Reviewer 2 的一致点：\n- W2 (relative advantage inflation)、W3 (scale)、W4 (downstream collapse)、W6 (Lagrangian 术语)、W7 (reference count) 均为有效批评。\n\n我的 overall 评价维持 3.5 (Borderline Conference)，略高于 R2 的 3.0 (Findings)。分歧在于对 novelty 和 analytical contribution 的权重：如果重视方法论洞察（gradient coupling mechanism + regime analysis），主会可接受；如果要求 novel algorithm 或 scaling evidence，Findings 更合适。",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## 交叉回应 — Reviewer 1 对 Reviewer 2 意见的逐条回应\n\n---\n\n**[REBUT] R2-W1: Novelty is incremental**\n\n不完全同意 \"predictable combination\" 的判断。关键证据是 Table 3 的 BCE+Gumbel+Lagrangian 实验（PPL 38.02）：如果组合是 \"obvious\"，那为什么将 Gumbel-Sigmoid 和 Lagrangian 直接应用于 BCE 反而比 vanilla BCE（27.97）更差？这说明 Gumbel 松弛与 loss function 之间存在非平凡的交互——Lagrangian penalty 在 BCE 下会干扰 per-neuron optimization（§4.4 第三段明确讨论）。仅仅 \"填表格\" 不足以构成贡献，但论文的核心洞察不是 \"KL 比 BCE 好\" 这个 general statement，而是具体机制：BCE 梯度 factorize per-neuron（Eq. 8）导致无法学到 global top-k 所需的 inter-neuron coupling。这个 mismatch 的诊断（§3.6 gradient analysis）+ 实证验证（iso-compute saturation）超越了简单 component combination。\n\n但 R2 的质疑并非无理：论文 2D taxonomy 的 framing 确实有 \"填空\" 嫌疑，且 KL distillation 本身不新。如果这篇论文去掉 gradient analysis 和 regime analysis，只剩 \"KL 比 BCE 好\"，那确实 incremental。目前版本的 contribution 在 borderline。\n\n---\n\n**[AGREE] R2-W2: Relative advantage 部分是 baseline collapse 的 artifact**\n\n完全同意。(TEAL-KL)/TEAL 作为 metric 在 TEAL 崩溃时会 inflate。Table 4 数据：\n- 30%: KL/Dense = 8.98/6.12 = 1.47×\n- 50%: KL/Dense = 11.79/6.12 = 1.93×\n- 70%: KL/Dense = 17.91/6.12 = 2.93×\n\n这个 framing 更诚实地反映了 KL predictor 自身的质量退化曲线。论文 Abstract 第 5 行 \"18% at 30%, 49% at 50%, and 82% at 70%\" 的叙事过度依赖于 TEAL 的失败来 inflate 自己的优势。建议作者至少同时报告 KL/Dense ratio。\n\n不过补充一点：即使 reframe 为 KL/Dense，从 1.47× 到 2.93× 的增长仍然表明 KL predictor 在高稀疏度下也显著退化（dense 到 2.93× 的 gap 并不小）。这更凸显了 capacity-limited regime（§4.5）的诚实性。\n\n---\n\n**[AGREE] R2-W3: Scale limitation undermines generality claims**\n\n同意。两个 7-8B SwiGLU 模型不足以支撑 \"structural property of SwiGLU networks\"（§4.6 末句）的泛化 claim。尤其是：\n- 13B/70B 模型的 layer 数和 d_ff 不同，Jacobian chain（factor (b) in Eq. 12）的 depth 效应可能质变\n- Limitations 中承认了这一点，但 Introduction 和 Abstract 的 framing 仍然偏 general\n\n不过严格来说，论文使用的措辞是 \"transfers across SwiGLU architectures of similar scale\"（Abstract 第 6 行），加了 \"of similar scale\" 的限定词，这在 Round 1 后已有改进。问题在于 §4.6 最后一句 \"evidence that the method exploits a structural property of SwiGLU networks\" 仍然过强——应加 \"at 7-8B scale\" 限定。\n\n---\n\n**[AGREE] R2-W4: Downstream collapse raises practical concerns**\n\n同意这是一个重要的实践限制。数据支撑：\n- 50% sparsity: MMLU 27.89% ≈ random（Table 2）\n- 30% KL-global: MMLU 25.27%，甚至比 TEAL 的 38.61% 更差（Table 2）\n- 实际推荐操作点仅为 30% uniform（MMLU 40.61%），PPL 优势仅 8.82 vs 10.97\n\n论文的 regime 分析（§4.5）诚实地展示了这些数据，并且 Limitations 中推荐 30% 为 \"recommended operating point for downstream fidelity\"。但 R2 的批评是合理的：如果实际有用的区间只有 ≤30%，那 50%/70% 的大幅 PPL 优势在实践中意义有限（downstream 都崩了）。\n\n论文核心贡献仍然成立（方法论 + 分析框架），但 impact 确实被这一限制约束。\n\n---\n\n**[REBUT] R2-W5: Em-dash usage signals AI-generated text**\n\n部分不同意将此列为 [warning] 级别问题。\n\n首先事实确认：LaTeX 中 `---` 产生 em-dash，论文中确实有多处使用（如 Abstract 第 8 行 \"three distinct sparsity regimes---budget-surplus, budget-constrained, and capacity-limited---\"；Introduction 中也有类似用法）。\n\n但作为审稿意见，这属于 stylistic preference 而非学术质量问题。Em-dash 在英文学术写作中是合法标点（Chicago Manual of Style 认可），许多人类作者也使用。将 em-dash 等同于 \"AI-generated\" 是一种 heuristic，不是 evidence。这个问题最多属于 [info] 级别的 minor suggestion，不应影响接收决定。\n\n如果真要修，建议作者减少使用频率即可（改为逗号或拆分句子），但这不应是审稿意见中的 warning。\n\n---\n\n**[AGREE] R2-W6: \"Lagrangian\" formulation is misleading terminology**\n\n完全同意，这与我 Round 2 review 中的 W1 是同一问题。Eq. 9 是二次惩罚 + deadzone，Eq. 10 是几何倍增/减半——这不是 Lagrangian dual ascent。\"Adaptive penalty controller\" 更准确。两位 reviewer 独立指出同一问题，增强了这个 concern 的权重。\n\n---\n\n**[AGREE] R2-W7: Reference count is low**\n\n同意。我在自己的 review 中也指出缺少 Wanda、SparseGPT、MoE、Louizos et al. 2018 (L0/Concrete distribution) 等引用。22 refs 对 EMNLP main 偏少，30-40 是更合理的密度。尤其是 pruning 领域的经典工作（Wanda, SparseGPT）和 conditional computation（MoE）应该在 Related Work 中有所 acknowledge。\n\n---\n\n### 总结\n\n与 Reviewer 2 的主要分歧点：\n1. **W1 (novelty)**: 我认为论文的 gradient mismatch 诊断 + iso-compute verification + regime analysis 超越了简单 component combination，但同意 2D taxonomy framing 有填空嫌疑。Overall novelty borderline。\n2. **W5 (em-dash)**: 不应作为 warning 级别问题。\n\n与 Reviewer 2 的一致点：\n- W2 (relative advantage inflation)、W3 (scale)、W4 (downstream collapse)、W6 (Lagrangian 术语)、W7 (reference count) 均为有效批评。\n\n我的 overall 评价维持 3.5 (Borderline Conference)，略高于 R2 的 3.0 (Findings)。分歧在于对 novelty 和 analytical contribution 的权重：如果重视方法论洞察（gradient coupling mechanism + regime analysis），主会可接受；如果要求 novel algorithm 或 scaling evidence，Findings 更合适。",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 107 · 2026-05-17T04:53:25.021623+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3667
}
```

</details>

---


### Assistant

_source line 108 · 2026-05-17T04:53:30.635513+00:00_

已提交交叉回应。总结：

- **REBUT**: W1 (novelty) — BCE+Gumbel+Lagrangian 实验 (PPL 38.02 > vanilla BCE 27.97) 证明组合并非 trivial；W5 (em-dash) — stylistic preference 不应为 warning 级别
- **AGREE**: W2 (relative advantage inflation)、W3 (scale)、W4 (downstream collapse)、W6 (Lagrangian 术语)、W7 (reference count)

两位 reviewer 在 Lagrangian 术语误用和 reference 不足上完全一致；主要分歧在 novelty 评估和 overall score（我 3.5 vs R2 3.0）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1"
}
```

</details>

---


## Round 6

## Round 6

42 recorded events


### User

_source line 109 · 2026-05-17T08:10:53.279663+00:00_

[Round 1 审稿请求]:
你负责**方法严谨性 + 实验有效性**的审查。

## Venue 信息
- **目标会议**: EMNLP 2026 (via ACL Rolling Review, May cycle)
- **截止日期**: 2026-05-25
- **页数限制**: Long paper ≤8 页正文 + unlimited references + appendix
- **模板**: ACL format with `[review]` option
- **匿名规则**: Double-blind
- **附录规则**: 允许，reviewer 可选择性阅读

## 论文路径
`projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, appendix.tex）

## 你的审查侧重

1. **方法正确性**：
   - KL 梯度分析（Eq. 7-8）是否数学上严格？factor (a)-(d) 的分解是否完整？
   - Gumbel-Sigmoid relaxation 的使用是否正确？与标准 Concrete distribution 的关系是否清晰？
   - Adaptive penalty controller (Eq. 5-6) 的收敛保证——论文称其为 "adaptive penalty controller" 而非 Lagrangian，这个表述是否准确？multiplicative schedule 是否有理论支撑？
   - BCE vs KL structural mismatch argument 是否有逻辑漏洞？

2. **实验有效性**：
   - 主实验对比是否公平？KL 和 BCE 的计算量对比（1000 vs 2700 steps）是否充分说明 structural failure？
   - 消融实验是否覆盖所有关键设计选择？是否有遗漏的 confounding factors？
   - 三 seed 统计（PPL 11.92±0.07）——3 seeds 的统计效力是否足够？
   - Cross-architecture evaluation (Mistral-7B) 是否充分验证 generalization？仅两个 7-8B 模型是否足够？
   - OOD evaluation (C4) 是否足够？训练和评估都在 WikiText 系列上是否存在 data leakage concern？
   - Downstream task collapse（MMLU/GSM8K 在 50% 时 ≈ random）——这是否 undermines the practical value？

3. **可重复性**：
   - 超参数是否充分报告？
   - 训练细节（WikiText-103, 1000 steps, batch=4, seq=2048）是否足够 reproduce？
   - Inference protocol（predictor-TEAL）是否描述清晰？

4. **Latency claim**：
   - 论文声称 6.4% overhead 但目前没有 wall-clock speedup——这对一篇 efficiency-motivated paper 意味着什么？
   - "eliminates compensation network" 节省 2.7% latency，但 predictor 本身加 6.4%——净效果是增加 overhead，这与 paper framing 是否矛盾？

请按 ARR review form 格式输出：Summary → Strengths → Weaknesses → Questions → Soundness (1-5) → Overall (1-5)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 110 · 2026-05-17T08:11:08.595629+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
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

_source line 111 · 2026-05-17T08:11:08.646350+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 112 · 2026-05-17T08:11:11.608506+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 113 · 2026-05-17T08:11:12.272408+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
  "pages": "1-10",
  "dpi": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
    "pages": "1-10",
    "dpi": "200"
  }
}
```

</details>

---


### Tool result

_source line 114 · 2026-05-17T08:11:26.210318+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

I've found comprehensive information about the ACL Rolling Review 2026 reviewer guidelines, review form, and criteria. Here are the key findings:

## Reviewer Guidelines

When you accept a reviewing request for an ARR cycle, you'll receive a kick-off email from OpenReview listi
…[truncated 2344 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 14601
}
```

</details>

---


### Tool result

_source line 115 · 2026-05-17T08:11:31.334610+00:00_

Error: result (9,085,867 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/fd7408d6-e7e0-4bb4-8dde-4202758b928d/tool-results/mcp-agent-ml-research-pdf_to_images-1779005490929.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/fd7408d6-e7e0-4bb4-8dde-4202758b928d/tool-results/mcp-agent-ml-research-pdf_to_images-1779005490929.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 19062
}
```

</details>

---


### Tool call

_source line 116 · 2026-05-17T08:11:36.806370+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scale (1-5 etc), and descriptions for each score level. Include all fields reviewers must fill in."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scale (1-5 etc), and descriptions for each score level. Include all fields reviewers must fill in."
  }
}
```

</details>

---


### Tool call

_source line 117 · 2026-05-17T08:11:37.158503+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper"
  }
}
```

</details>

---


### Tool result

_source line 118 · 2026-05-17T08:11:37.209375+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 119 · 2026-05-17T08:11:43.533854+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## Core Evaluation Dimensions

**Reviewer Confidence** (1-5 scale)
- 5: "Positive that my evaluation is correct. I read the paper very carefully"
- 4: Quite sure; unlikely to have missed important points
- 3: Pretty sure; may have missed some details
- 2: Willing to defend evaluation; fairly likely missed some details
- 1: "Not my area, or paper is very hard to understand"

**Soundness** (1-5 scale, with half-points)
- 5: "Excellent: This study is one of the most thorough I have seen"
- 4: Strong; sufficient support with minor additions optional
- 3: Acceptable; main claims supported with minor gaps
- 2: Poor; main claims lack sufficient support
- 1: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

**Excitement** (1-5 scale, with half-points)
- 5: "Highly Exciting: I would recommend this paper to others"
- 4: Exciting; would mention to others or attend presentation
- 3: Interesting; might mention points or attend if time permits
- 2: Potentially interesting; doesn't resonate personally
- 1: "Not Exciting: this paper does not resonate with me"

**Overall Assessment** (1-5 scale, with half-points)
- 5: Consider for Award (top 2.5% papers)
- 4: Conference acceptance
- 3: Findings acceptance
- 2: Resubmit next cycle
- 1: Do not resubmit

## Additional Evaluation Dimensions

**Reproducibility** (1-5 scale): Assesses whether readers can reproduce results

**Datasets** (1-5 scale): Evaluates released dataset value to community

**Software** (1-5 scale): Assesses released software utility

**Author Identity Knowledge** (1-5 scale): Tracks blind review integrity

**Required Fields:**
- Paper Summary
- Summary of Strengths
- Summary of Weaknesses
- Comments/Suggestions/Typos
- Limitations and Societal Impact
- Ethical Concerns
- Ethics Review Recommendation
- Best Paper Justification (conditional)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6727
}
```

</details>

---


### Tool call

_source line 120 · 2026-05-17T08:11:47.837588+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 121 · 2026-05-17T08:11:48.289290+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	
17	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
18	
19	\author{Anonymous}
20	
21	\begin{document}
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
32	\input{conclusion}
33	\input{limitations}
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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 122 · 2026-05-17T08:11:48.339816+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 123 · 2026-05-17T08:11:48.741565+00:00_

1	Activation sparsity reduces the effective computation in SwiGLU-based LLMs by pruning FFN neurons at inference, but existing learned predictors trained with binary cross-entropy (BCE) require error compensation networks due to a structural mismatch: BCE decomposes per neuron while inference uses global top-$k$ allocation across all layers.
2	We train lightweight predictors (2.37M parameters per layer, 75.9M total, $<$1\% of the base model) with KL divergence, which couples all neurons through the output distribution via Gumbel-Sigmoid relaxation, eliminating the need for compensation.
3	On LLaMA-3.1-8B (WikiText-2), our KL-trained predictor achieves perplexity 11.79 at 50\% sparsity without compensation, compared to 23.31 for vanilla TEAL and 27.97 for BCE trained at 2.71$\times$ the compute budget, whose loss saturates, confirming a structural rather than computational failure.
4	Three-seed evaluation confirms training stability (PPL $11.92 \pm 0.07$, CV${<}$1\% under uniform allocation).
5	The KL advantage grows disproportionately with sparsity: 18\% relative improvement at 30\%, 49\% at 50\%, and 82\% at 70\% (PPL 17.91 vs.\ 100.11); KL itself incurs $2.93\times$ the dense baseline, demonstrating substantial output fidelity even at extreme sparsity.
6	Cross-architecture evaluation on Mistral-7B-v0.3 confirms the advantage transfers across SwiGLU architectures at the 7--8B parameter scale, with consistent KL-over-TEAL ratios (within 7\% at $\leq$50\% sparsity).
7	SPON's static bias correction proves near-orthogonal to the predictor (cosine similarity 0.196), providing only 2.4\% relative PPL improvement (12.08$\to$11.79 under \texttt{evaluate.py}).
8	We propose a two-dimensional taxonomy over correction granularity $\times$ training signal coupling that unifies prior methods and identify three distinct sparsity regimes (budget-surplus, budget-constrained, and capacity-limited) that govern the quality-sparsity tradeoff.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 124 · 2026-05-17T08:11:48.792216+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-17T08:11:49.244421+00:00_

1	\section{Introduction}
2	
3	SwiGLU feed-forward networks~\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.
4	Exploiting this sparsity can simplify inference by pruning 50\% of FFN neurons per token (without modifying the pretrained weights), eliminating the need for auxiliary compensation networks.
5	Yet the gap between potential and practice remains wide.
6	Training-free methods such as TEAL~\cite{liu2025teal} select neurons by activation magnitude alone, degrading perplexity from 6.12 (dense) to 23.31 at 50\% sparsity on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, a 281\% increase.
7	Learned predictors~\cite{liu2023dejavu,gautam2026fastforward} close part of this gap by training small auxiliary networks to anticipate which neurons will be important, but they rely on error compensation modules (output rescaling networks or additive correction layers) that add 67.2M parameters and $\sim$2.7\% additional latency overhead at inference.
8	The question is whether a predictor can be trained so that compensation becomes unnecessary.
9	
10	The answer depends on the training objective.
11	Current learned predictors use binary cross-entropy (BCE) loss: each neuron is independently classified as ``keep'' or ``prune'' against an oracle mask derived from the dense model's activations.
12	The gradient of BCE with respect to neuron $j$'s score is $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$, a function of neuron $j$ alone, independent of every other neuron in the network.
13	But at inference, no neuron is evaluated in isolation.
14	TEAL's global top-$k$ mechanism~\cite{liu2025teal} ranks all neurons across all layers and retains only those above a model-wide threshold.
15	Whether neuron $j$ survives depends not on its own score but on how that score compares to the scores of all $L \times d_{\text{ff}}$ neurons.
16	This creates a structural mi
…[truncated 4883 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 126 · 2026-05-17T08:11:49.245094+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-17T08:11:49.697153+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models.
5	The method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass, eliminating the need for auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{h}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importance scores from the pre-FFN hidden state $\mathbf{h}$.
26
…[truncated 13358 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 128 · 2026-05-17T08:11:49.697513+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-17T08:11:50.149452+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4, using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$ and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly; (2) \textbf{BCE predictor}, trained with per-neuron binary cross-entropy loss for 1000 and 2700 steps; (3) \textbf{Uniform allocation}, which distributes the sparsity budget equally across layers; and (4) \textbf{WINA}~\cite{liu2025teal}, an importance-weighted variant.
23	
24	
25	\subsection{Main Results}
26	
27	
…[truncated 12662 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 130 · 2026-05-17T08:11:50.149927+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 131 · 2026-05-17T08:11:51.103978+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude, achieving 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking.
6	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
7	
8	\paragraph{Predictor-Based Contextual Sparsity.}
9	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
10	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with MSE supervision but retains per-neuron decomposition.
11	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
12	PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.
13	MaskLLM~\cite{fang2024maskllm} also employs learnable masks with Gumbel relaxation and frozen weights, but targets N:M semi-structured \emph{weight} sparsity (2:4 patterns) via Gumbel-Softmax, producing fixed masks independent of input tokens.
14	In contrast, our method learns \emph{activation} masks that are contextual (per-token), unstructured (budget-constrained global top-$k$), and trained with Gumbel-Sigmoid to minimize output-distribution divergence.
15	All prior predictor-based methods use decomposed (BCE) or intermediate (MSE) objectives where each neuron's gradient is independent of other mask states.
16	Our \emph{coupled} KL objective propagates gradients through all downstream layers, optimizing for global allocation quality without compensation.
…[truncated 2049 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 132 · 2026-05-17T08:11:51.104373+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 133 · 2026-05-17T08:11:51.606621+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Training sparsity predictors with KL divergence eliminates error compensation networks by coupling all neurons through the output distribution, resolving BCE's structural mismatch with global top-$k$ allocation.
5	The resulting predictor (75.9M params, $<$1\% of base) achieves PPL 11.79 at 50\% sparsity vs.\ 23.31 for TEAL, transfers across SwiGLU architectures at the 7--8B parameter scale (within 7\% ratio consistency), and reveals three sparsity regimes governing the quality-allocation tradeoff.
6	
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 134 · 2026-05-17T08:11:51.607053+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 135 · 2026-05-17T08:11:51.707854+00:00_

1	\section*{Limitations}
2	
3	Our primary evaluation uses WikiText-2 perplexity, and downstream benchmarks reveal that perplexity is a poor proxy for reasoning ability at moderate sparsity: 40\% sparsity achieves PPL 8.36 but MMLU already degrades, motivating 30\% as the recommended operating point for downstream fidelity.
4	Training requires 1000 steps on WikiText-103 ($\sim$17 minutes on A6000), but a separate predictor must be trained for each sparsity target.
5	All experiments use 7--8B parameter models (LLaMA-3.1-8B, Mistral-7B-v0.3); scaling behavior to 13B or 70B models remains untested.
6	While we motivate our work with inference speedup potential, actual wall-clock acceleration depends on sparse kernel implementations (e.g., Triton, cuSPARSE) and hardware-specific memory access patterns; this work focuses on prediction quality rather than systems optimization.
7	Future directions include N:M structured sparsity for hardware-native acceleration, scaling to 13B+ models, and training a single predictor that serves multiple sparsity targets simultaneously.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 136 · 2026-05-17T08:11:51.708305+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 137 · 2026-05-17T08:11:51.758997+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling), confirming that KL distillation provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overh
…[truncated 8907 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 138 · 2026-05-17T08:11:57.583478+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
  "offset": "192"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
    "offset": "192"
  }
}
```

</details>

---


### Tool result

_source line 139 · 2026-05-17T08:11:57.985947+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (192). The file has 192 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 140 · 2026-05-17T08:11:57.986326+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper"
  }
}
```

</details>

---


### Tool result

_source line 141 · 2026-05-17T08:11:58.036731+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 142 · 2026-05-17T08:12:01.051256+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 143 · 2026-05-17T08:12:01.102179+00:00_

1	% =============================================================================
2	% Direction 1: KL distillation for structured/activation sparsity
3	% =============================================================================
4	
5	@inproceedings{fang2024maskllm,
6	  title = {MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models},
7	  author = {Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff Pool and Jan Kautz and Pavlo Molchanov and Xinchao Wang},
8	  year = {2024},
9	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
10	  url = {https://arxiv.org/abs/2409.17481},
11	}
12	
13	@inproceedings{xu2026spon,
14	  title = {Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models},
15	  author = {Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma},
16	  year = {2026},
17	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
18	  url = {https://arxiv.org/abs/2512.12744},
19	}
20	
21	@inproceedings{muralidharan2024minitron,
22	  title = {Compact Language Models via Pruning and Knowledge Distillation},
23	  author = {Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marcin Chochowski and Mostofa Patwary and Mohammad Shoeybi and Bryan Catanzaro and Jan Kautz and Pavlo Molchanov},
24	  year = {2024},
25	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
26	  url = {https://arxiv.org/abs/2407.14679},
27	}
28	
29	
30	% =============================================================================
31	% Direction 3: SPON and learnable bias correction for sparsity
32	% =============================================================================
33	
34	@article{gautam2026fastforward,
35	  title = {Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity},
36	  author = {Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott and Naras
…[truncated 12159 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 144 · 2026-05-17T08:14:16.018890+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool call

_source line 145 · 2026-05-17T08:14:18.489743+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the detailed reviewer guidelines: what should reviewers focus on, what dimensions matter most, any specific instructions about experimental evaluation, reproducibility, claims vs evidence. Include scoring rubric details if any."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the detailed reviewer guidelines: what should reviewers focus on, what dimensions matter most, any specific instructions about experimental evaluation, reproducibility, claims vs evidence. Include scoring rubric details if any."
  }
}
```

</details>

---


### Tool result

_source line 146 · 2026-05-17T08:14:45.674164+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 31, \"total_citations\": 58, \"unique_cited_keys\": 31, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 29, \"online_not_found\": 0, \"online_mismatch\": 2}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"fang2024maskllm\", \"type\": \"inproceedings\", \"title\": \"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models\", \"authors\": \"Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff P...\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"xu2026spon\", \"type\": \"inproceedings\", \"title\": \"Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models\", \"authors\": \"Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma\", \"year\": \"2026\", \"venue\": \"Proceedings of the International Conference on Machine Learning (ICML)\"}, {\"key\": \"muralidharan2024minitron\", \"type\": \"inproceedings\", \"title\": \"Compact Language Models via Pruning and Knowledge Distillation\", \"authors\": \"Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marci...\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"gautam2026fastforward\", \"type\": \"article\", \"title\": \"Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity\", \"authors\": \"Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott ...\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2602.00397\"}, {\"key\": \"liu2025teal\", \"type\": \"inproceedings\", \"title\": \"Training-Free Activation Sparsity in Large Language Models\", \"authors\": \"James Liu and Pragaash Ponnusamy and Tianle Cai and Han Guo and Yoon Kim and Ben...\", \"year
…[truncated 24190 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 29655
}
```

</details>

---


### Tool result

_source line 147 · 2026-05-17T08:15:00.815858+00:00_

# ARR Reviewer Guidelines: Key Focus Areas

## Core Reviewing Tasks

Reviewers should complete **four main tasks**:
1. Calendar allocation for reviewing and discussion periods
2. Assignment verification (expertise, conflicts of interest, desk-rejection criteria)
3. Writing substantive reviews
4. Updating assessments post-author response

## Primary Review Dimensions

**Soundness Assessment**: Technical validity must justify low scores. The guidance warns against scoring poorly without identifying specific faults, as this signals unconscious bias rather than legitimate concerns.

**Excitement Score**: Separate from soundness, this captures personal interest level—orthogonal to paper quality assessment.

**Overall Recommendation**: Composite judgment reflecting soundness, novelty, impact, and potential contribution to the field, regardless of personal enthusiasm.

## Critical Review Focus Areas

### Reading Strategy
Reviewers must read papers twice: initial skim-reading to adjust expectations without confirmation bias, then in-depth evaluation. The guidance emphasizes "postpone such searches until after they have read the paper completely" regarding related work verification.

### Specificity Requirement
Generic criticism is forbidden. Instead of stating "X is not clear," reviewers must specify "Y and Z are missing from X's description." Citations of missing references require exact identification.

### Common Problematic Heuristics to Avoid

The guidelines list 17 bias patterns (H1-H17), including:
- Dismissing findings as "obvious in retrospect"
- Requiring SOTA results when incremental progress suffices
- Penalizing negative results
- Criticizing methodological simplicity
- Demanding unnecessary additional experiments

## NLP-Specific Problem Areas

Reviewers should flag common issues with codes (M1-M5, T1-T2, R1-R5, G1-G5):

**Methodology issues** include LLM-only evaluation without validation, reproducibility gaps, undisclosed data quality problems, and incomplet
…[truncated 1250 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 42326
}
```

</details>

---


### Tool call

_source line 148 · 2026-05-17T08:17:57.747647+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 审稿意见：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n## Paper Summary\n\n本文提出用 KL divergence 替代 BCE 训练 SwiGLU LLM 的 activation sparsity predictor。核心论点是 BCE 梯度按 neuron 分解（Eq. 7: ∂L/∂s_j = σ(s_j) − m_j*），与推理时 TEAL 的 global top-k allocation 存在\"结构性不匹配\"；KL 梯度通过下游 Jacobian（factor (b)）耦合所有 neuron。方法使用 Gumbel-Sigmoid relaxation 实现可微训练，adaptive penalty controller 控制稀疏度。在 LLaMA-3.1-8B 上 50% sparsity 下 PPL 11.79 vs TEAL 的 23.31（无 compensation network）。跨架构验证于 Mistral-7B-v0.3。提出 correction granularity × training signal coupling 的 2D taxonomy，识别三种 sparsity regime。\n\n---\n\n## Summary of Strengths\n\n**S1. 清晰的理论洞察与形式化。** §3.5 的梯度分析是本文最强贡献。Factor (a)-(d) 分解清楚说明了 KL 和 BCE 的结构性差异：factor (b) 的 Jacobian ∂z/∂h^(ℓ) 使 KL 梯度依赖所有下游层的 mask 状态，而 BCE 的 Eq. 7 只依赖 neuron j 自身。这个观察数学上严格，且有直接的实证支撑。\n\n**S2. Oracle F1 分析揭示 proxy mismatch 的深度（§4.2）。** BCE 达到 F1=0.613（比 KL 的 0.540 高 +13pp）但 PPL 差 91%；KL 的 near-random precision (0.51) 表明它学到的 mask 与 magnitude oracle 完全不同，优化的是 distributional fidelity 而非 magnitude matching。这是全文最有说服力的实验证据，直接支撑了\"正确目标 > 高精度代理\"的核心论点。\n\n**S3. 消融设计覆盖关键设计选择。** Table 3 系统覆盖：loss direction（Forward KL vs JSD vs Reverse KL）、relaxation（Gumbel vs STE, Δ=3.98）、compensation 效果、以及关键的 isolation 实验（BCE + Gumbel + Penalty = 38.02，证明 penalty 框架本身不提供增益）。Loss effect (ΔPPL=26.23) 是 relaxation effect (ΔPPL=3.98) 的 6.6×，清晰分离了各组件贡献。\n\n**S4. 2D taxonomy 和 regime 分析有组织价值。** Table 1 的 correction granularity × training signal coupling 分类法简洁有效地定位了本文在文献中的位置。三 regime 分析（budget-surplus / budget-constrained / capacity-limited）发现 allocation preference 的非单调性（30% 偏好 uniform，40% 偏好 global，50% 无差异）是有意义的实证发现。\n\n**S5. SPON 正交性分析（§4.5）。** Cosine similarity 0.196 + 仅 2.4% PPL 改善的定量分解说明 KL predictor 已捕获大部分可恢复信号，static correction 与 learned prediction 接近正交，这对未来工作有指导意义。\n\n---\n\n## Summary of Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**N1 [critical] 论文以 efficiency 为动机，但实际无 wall-clock speedup，且 framing 产生误导。**\n- 具体位置：§1 (\"simplify inference by pruning 50% of FFN neurons\"), §4.6 (\"eliminates the compensation network, −2.7% latency\"), Appendix A (Table 6)\n- 问题：Table 6 (Appendix A) 显示 KL predictor-only 在 50% sparsity 下为 126.78ms（dense 119.11ms），overhead = +6.4%。消除 compensation 节省 2.7%，但 predictor 本身加 6.4%。与 compensation-based 方法相比净效果是 +6.4% vs +8.9%——仅节省 2.5pp overhead，且两者都比 dense 慢。更关键的是，unstructured element-wise mask 不产生任何 sparse computation speedup，论文自己在 Appendix A 和 Limitations 中承认 \"net acceleration requires kernel-level sparse computation optimizations\"。\n- 为什么影响接收：论文 Introduction 的 framing 暗示 \"simplify inference\" 和 \"eliminating compensation\" 带来效率增益。但实际效果是：(1) 比 dense 慢 6.4%；(2) 比有 compensation 的方案快 2.5pp 但仍然更慢。一篇以 sparsity prediction 为核心的论文，在没有任何实际加速的情况下，需要将 framing 从 \"efficiency\" 调整为 \"prediction quality / understanding\"。\n- 建议修改方向：重新定位论文贡献为\"理解 loss function 对 sparsity prediction 的影响\"和\"elimination of compensation as architectural simplification\"。在 Introduction 和 Abstract 中明确说明当前无 wall-clock speedup，将加速留作 future work with structured sparsity。\n\n**N2 [critical] 下游任务在实用稀疏度下崩溃，严重削弱 practical value。**\n- 具体位置：Table 2 (30% KL global: MMLU 25.27%, 50%: MMLU 27.89% ≈ random), Table 4\n- 问题：Dense MMLU = 65.27%。30% sparsity + global TEAL: MMLU = 25.27%（−40pp，接近 random 25%）；uniform 恢复到 40.61% 但仍损失 24.7pp。50% 时所有方法 MMLU ≈ 28%，GSM8K < 2.2%。PPL 的大幅改善（11.79 vs 23.31）未转化为 reasoning 能力保持。论文在 §4.3 提到 \"PPL is a poor proxy for reasoning\"，但这个结论在 Limitations 中才被充分讨论，而非贯穿全文。\n- 为什么影响接收：论文的核心评价指标（PPL）与实际应用关注的指标（downstream task performance）之间存在严重脱节。如果 50% sparsity 下模型在所有知识/推理任务上退化到 random，这意味着论文展示的\"最引人注目\"的改善点（49% PPL reduction at 50%）在实践中可能不相关。审稿人需要知道：在什么稀疏度下，该方法能同时保持合理的 PPL 和 downstream performance？\n- 建议修改方向：(1) 在主实验中更突出讨论 PPL-downstream disconnect；(2) 将 30% 的 downstream 结果提升到与 50% PPL 同等重要的位置；(3) 考虑补充 10-20% sparsity 下的 downstream 评估，找到 practical sweet spot。\n\n**N3 [critical] 训练-推理 mask 不匹配未被分析，且残差退化来源不明。**\n- 具体位置：§3.3 (Gumbel-Sigmoid, τ annealed to 0.1), §4.1 (predictor-TEAL inference), Appendix B Table 5\n- 问题：训练使用 soft Gumbel-Sigmoid mask（即使 τ=0.1 也非完全 binary），推理使用 TEAL 的 hard top-k allocation。Table 5 (Appendix B) 揭示了关键数据：d_b=128 在 per-token 评估下 PPL=9.218，在 TEAL global 下 PPL=11.963——差距约 30%。这意味着从 dense (6.12) 到 KL-TEAL (11.79) 的全部退化（Δ=5.67）中，有相当一部分可能来自 soft→hard mismatch 和 TEAL global allocation 的信息丢失，而非 sparsity 本身的 capacity loss。论文从未正式分析这一 gap 的来源。\n- 为什么影响接收：不分析这个 gap，读者无法判断剩余退化是方法可以改进的（通过 better allocation 或 better train-test alignment）还是 fundamental limit。这直接关系到方法的 ceiling 和 future improvement 空间。\n- 建议修改方向：添加分解分析，例如：(1) per-token hard mask evaluation（控制 allocation）；(2) per-token soft mask evaluation（Table 5 已有）；(3) global hard mask with oracle scores。分离 mask quality loss、discretization loss 和 allocation loss。\n\n---\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1 [warning] BCE 对比的公平性问题：系统差异超过 loss function。**\n- 具体位置：Table 3 ablation\n- 问题：KL 系统 = Forward KL + Gumbel-Sigmoid + penalty controller；BCE 系统 = BCE + hard mask + compensation。消融中 \"BCE + Gumbel + Penalty\" 达到 38.02（比 vanilla BCE 的 27.97 更差），说明 penalty 框架与 BCE 不兼容。这意味着 Table 2 中的 KL vs BCE 对比不仅是 loss function 的差异，而是整个 training pipeline 的差异。KL+STE (15.77) 提供了更接近的对比，但 STE 本身的 gradient bias 也是 confound。\n- 建议：明确说明 KL 的优势来自 loss function + compatible training infrastructure 的组合，而非单独的 loss function。或提供一个更直接的 fair comparison（例如 MSE on output logits + Gumbel，控制 training infrastructure 的同时对比 loss）。\n\n**W2 [warning] \"Parameter-free\" penalty controller 表述不准确。**\n- 具体位置：§3.4, footnote (\"parameter-free, no step-size tuning\"), Table 7\n- 问题：λ_max 在不同 sparsity target 下取不同值（30% 和 70% 用 5000，50% 用 1000），这本身就是 hyperparameter。Table 7 显示 30% target 时 λ 达到 cap (5000)，actual sparsity = 0.285（偏差 5%）。Controller 无法在所有 target 下精确收敛。\n- 建议：去掉 \"parameter-free\" 措辞；讨论 λ_max 选择对结果的影响；说明 30% 时 5% deviation 对 PPL 的影响。\n\n**W3 [warning] 统计效力不足。**\n- 具体位置：Appendix F (3 seeds, 50% uniform only)\n- 问题：(1) 3 seeds 的 95% CI（≈ [11.73, 12.11]，t-distribution）较宽，对 Table 3 中差异 <1 的 ablation 结果（如 Forward KL 11.79 vs JSD 12.54），无法判断统计显著性。(2) Multi-seed 仅在 50% uniform 下做，主结果（50% global TEAL, PPL 11.79）无方差估计。(3) Downstream metrics 更 noisy（ARC-c 33.8±1.2%），3 seeds 不足以支撑 downstream 的 regime 分析结论。\n- 建议：至少在 primary configuration (50% global TEAL) 也报告 multi-seed；考虑增加到 5 seeds。\n\n**W4 [warning] 实验规模受限。**\n- 具体位置：§4.1, §4.6, Limitations\n- 问题：仅 7-8B 模型（LLaMA-3.1-8B, Mistral-7B-v0.3），同一参数量级，同为 SwiGLU。论文多处使用 \"transfers across SwiGLU architectures\" 但实际上 (a) 仅测试了一个 scale，(b) 两个模型的 d_ff / d_model ratio 相同（14336/4096），(c) Mistral 的主要差异是 GQA + sliding window attention，这些差异与 FFN sparsity prediction 关系不大。\n- 建议：弱化 generalization claims，改为 \"verified on two 7-8B SwiGLU models\"。如果可能，增加 13B 或更大模型的验证。\n\n**W5 [warning] Gradient SNR 测量与训练设置不一致。**\n- 具体位置：§3.5 empirical verification\n- 问题：SNR 在 C4 数据上测量（\"80 steps on LLaMA-3.1-8B (C4 data)\"），但训练使用 WikiText-103。不同数据分布可能影响 SNR，使该测量不能直接代表训练过程中的实际 gradient quality。\n- 建议：在 WikiText-103 上重复 SNR 测量，或解释为何选择 C4 及其对结论的影响。\n\n**W6 [warning] 训练数据集过小且与评估数据同源。**\n- 具体位置：§4.1 (\"trained for 1000 steps on WikiText-103 with batch size 4\")\n- 问题：1000 steps × batch 4 × seq 2048 = ~8M tokens，仅为 WikiText-103 全集的一小部分。评估在 WikiText-2 上——与 WikiText-103 同源（都是 Wikipedia）。虽然 Appendix D 的 C4 OOD 评估有所缓解，但仅有一个 sparsity level (50%) 和一个 metric (PPL)。\n- 建议：在 C4 上补充 30% 和 70% 的评估；如果条件允许，考虑在非 Wikipedia 数据上训练一版 predictor 验证泛化性。\n\n---\n\n### 小问题（不影响接收）\n\n- **M1**: AdamW 的 weight decay 值未报告（§4.1）。\n- **M2**: BCE 的 oracle mask 生成方式（per-layer top-k 还是 global top-k？）未明确说明（§3.5 \"oracle masks m_j* = 1[|g_j| ≥ top-k threshold]\"，但 threshold 的作用域不清楚）。\n- **M3**: Table 1 将 ShadowLLM 归为 \"Per-layer\"，但 ShadowLLM 使用 attention-based routing，可能更接近 per-token。需核实分类准确性。\n- **M4**: loshchilov2019adamw 引用年份为 2019，OpenAlex 匹配到的原始 arXiv 年份为 2017。会议发表年份与 arXiv 年份不一致，建议统一。\n- **M5**: Appendix A 的 latency 测量在 RTX PRO 6000 Blackwell 上，但训练在 A6000 上（Limitations 提到 \"~17 minutes on A6000\"）。两个 GPU 架构差异较大，latency 数据的可迁移性不明。\n\n---\n\n## Questions to Authors\n\n**Q1.** Table 5 (Appendix B) 显示 d_b=128 per-token PPL = 9.218, TEAL global PPL = 11.963。这 ~30% 的 gap 中，有多少来自 soft→hard discretization，多少来自 TEAL global 的 budget allocation 策略？能否提供 per-token hard mask evaluation 来分离这两个因素？\n\n**Q2.** BCE 对比中，BCE 的 learning rate 和 optimizer 设置是否与 KL 完全一致？如果不一致，BCE 是否经过独立的 hyperparameter tuning？\n\n**Q3.** 论文称 \"KL's near-random precision (0.51)\"——这是否意味着 KL predictor 学到的 mask 与 magnitude-based oracle 几乎无相关性？如果是，KL predictor 到底保留了哪些 neuron——是否有 per-layer 的分析可以说明 KL mask 与 oracle mask 的差异模式？\n\n**Q4.** 30% sparsity 下 penalty controller 达到 λ cap (5000) 且 actual sparsity = 28.5%。如果 λ_max 设为更大的值（如 10000），sparsity 能否达到 30%？如果能，PPL 会如何变化？\n\n**Q5.** 是否尝试过在训练中使用 hard top-k (with STE) 替代 Gumbel-Sigmoid 来缩小 train-test gap？Table 3 已有 KL+STE 但未说明其是否使用 top-k selection。\n\n---\n\n## 官方维度打分（ACL Rolling Review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心梯度分析数学正确，factor (a)-(d) 分解完整。Gumbel-Sigmoid 使用正确。但 BCE 对比的公平性有 confound (W1)；train-test mask mismatch 未分析 (N3)；penalty controller 在边界情况下表现不佳 (W2)。 |\n| Excitement | 2.5/5 | \"正确 loss > 高精度 proxy\" 的洞察有价值，oracle F1 分析令人信服。2D taxonomy 有组织贡献。但无实际 speedup (N1) 和 downstream collapse (N2) 严重限制了实际影响力。 |\n| Reproducibility | 3.5/5 | 训练设置报告较全（model, data, steps, LR, optimizer, τ schedule）。缺少 weight decay、gradient clipping、evaluation batch size。未提及代码是否会开源。Appendix 的超参数 sensitivity 分析有利于复现。 |\n| Overall | 3/5 | Findings 边界。理论洞察清晰且有实证支撑，但 practical impact 受限于 (1) 无 wall-clock speedup, (2) downstream collapse, (3) limited scale。 |\n| Confidence | 4/5 | 对 activation sparsity 和 knowledge distillation 领域较熟悉，仔细阅读了全文和附录。 |\n\n---\n\n## 总体评分\n\n**Overall**: 3/5 (Findings acceptance)\n\n**一句话总结**: 论文提供了有价值的理论洞察（KL 梯度耦合解决 BCE 的结构性不匹配），实验设计合理但存在 BCE 对比公平性和 train-test mismatch 未分析的问题；无实际推理加速和下游任务崩溃严重限制了实用价值，适合 Findings 而非主会议。\n\n---\n\n## 主要优势\n\n- 梯度分析形式化清晰，factor (a)-(d) 分解为理解 loss function 设计提供了有用的分析框架\n- Oracle F1 分析（BCE F1=0.613 > KL F1=0.540，但 PPL 差 91%）是全文最有说服力的实验，直接 falsify 了 \"per-neuron accuracy = output quality\" 的隐含假设\n- 消融设计系统全面，loss isolation 实验（BCE + Gumbel + Penalty = 38.02）有效分离了 loss function 和 training infrastructure 的贡献\n- 三 regime 分析发现了 allocation preference 的非单调性，对部署决策有实用指导价值\n- 写作质量好，结构清晰，主线统一\n",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 审稿意见：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n## Paper Summary\n\n本文提出用 KL divergence 替代 BCE 训练 SwiGLU LLM 的 activation sparsity predictor。核心论点是 BCE 梯度按 neuron 分解（Eq. 7: ∂L/∂s_j = σ(s_j) − m_j*），与推理时 TEAL 的 global top-k allocation 存在\"结构性不匹配\"；KL 梯度通过下游 Jacobian（factor (b)）耦合所有 neuron。方法使用 Gumbel-Sigmoid relaxation 实现可微训练，adaptive penalty controller 控制稀疏度。在 LLaMA-3.1-8B 上 50% sparsity 下 PPL 11.79 vs TEAL 的 23.31（无 compensation network）。跨架构验证于 Mistral-7B-v0.3。提出 correction granularity × training signal coupling 的 2D taxonomy，识别三种 sparsity regime。\n\n---\n\n## Summary of Strengths\n\n**S1. 清晰的理论洞察与形式化。** §3.5 的梯度分析是本文最强贡献。Factor (a)-(d) 分解清楚说明了 KL 和 BCE 的结构性差异：factor (b) 的 Jacobian ∂z/∂h^(ℓ) 使 KL 梯度依赖所有下游层的 mask 状态，而 BCE 的 Eq. 7 只依赖 neuron j 自身。这个观察数学上严格，且有直接的实证支撑。\n\n**S2. Oracle F1 分析揭示 proxy mismatch 的深度（§4.2）。** BCE 达到 F1=0.613（比 KL 的 0.540 高 +13pp）但 PPL 差 91%；KL 的 near-random precision (0.51) 表明它学到的 mask 与 magnitude oracle 完全不同，优化的是 distributional fidelity 而非 magnitude matching。这是全文最有说服力的实验证据，直接支撑了\"正确目标 > 高精度代理\"的核心论点。\n\n**S3. 消融设计覆盖关键设计选择。** Table 3 系统覆盖：loss direction（Forward KL vs JSD vs Reverse KL）、relaxation（Gumbel vs STE, Δ=3.98）、compensation 效果、以及关键的 isolation 实验（BCE + Gumbel + Penalty = 38.02，证明 penalty 框架本身不提供增益）。Loss effect (ΔPPL=26.23) 是 relaxation effect (ΔPPL=3.98) 的 6.6×，清晰分离了各组件贡献。\n\n**S4. 2D taxonomy 和 regime 分析有组织价值。** Table 1 的 correction granularity × training signal coupling 分类法简洁有效地定位了本文在文献中的位置。三 regime 分析（budget-surplus / budget-constrained / capacity-limited）发现 allocation preference 的非单调性（30% 偏好 uniform，40% 偏好 global，50% 无差异）是有意义的实证发现。\n\n**S5. SPON 正交性分析（§4.5）。** Cosine similarity 0.196 + 仅 2.4% PPL 改善的定量分解说明 KL predictor 已捕获大部分可恢复信号，static correction 与 learned prediction 接近正交，这对未来工作有指导意义。\n\n---\n\n## Summary of Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**N1 [critical] 论文以 efficiency 为动机，但实际无 wall-clock speedup，且 framing 产生误导。**\n- 具体位置：§1 (\"simplify inference by pruning 50% of FFN neurons\"), §4.6 (\"eliminates the compensation network, −2.7% latency\"), Appendix A (Table 6)\n- 问题：Table 6 (Appendix A) 显示 KL predictor-only 在 50% sparsity 下为 126.78ms（dense 119.11ms），overhead = +6.4%。消除 compensation 节省 2.7%，但 predictor 本身加 6.4%。与 compensation-based 方法相比净效果是 +6.4% vs +8.9%——仅节省 2.5pp overhead，且两者都比 dense 慢。更关键的是，unstructured element-wise mask 不产生任何 sparse computation speedup，论文自己在 Appendix A 和 Limitations 中承认 \"net acceleration requires kernel-level sparse computation optimizations\"。\n- 为什么影响接收：论文 Introduction 的 framing 暗示 \"simplify inference\" 和 \"eliminating compensation\" 带来效率增益。但实际效果是：(1) 比 dense 慢 6.4%；(2) 比有 compensation 的方案快 2.5pp 但仍然更慢。一篇以 sparsity prediction 为核心的论文，在没有任何实际加速的情况下，需要将 framing 从 \"efficiency\" 调整为 \"prediction quality / understanding\"。\n- 建议修改方向：重新定位论文贡献为\"理解 loss function 对 sparsity prediction 的影响\"和\"elimination of compensation as architectural simplification\"。在 Introduction 和 Abstract 中明确说明当前无 wall-clock speedup，将加速留作 future work with structured sparsity。\n\n**N2 [critical] 下游任务在实用稀疏度下崩溃，严重削弱 practical value。**\n- 具体位置：Table 2 (30% KL global: MMLU 25.27%, 50%: MMLU 27.89% ≈ random), Table 4\n- 问题：Dense MMLU = 65.27%。30% sparsity + global TEAL: MMLU = 25.27%（−40pp，接近 random 25%）；uniform 恢复到 40.61% 但仍损失 24.7pp。50% 时所有方法 MMLU ≈ 28%，GSM8K < 2.2%。PPL 的大幅改善（11.79 vs 23.31）未转化为 reasoning 能力保持。论文在 §4.3 提到 \"PPL is a poor proxy for reasoning\"，但这个结论在 Limitations 中才被充分讨论，而非贯穿全文。\n- 为什么影响接收：论文的核心评价指标（PPL）与实际应用关注的指标（downstream task performance）之间存在严重脱节。如果 50% sparsity 下模型在所有知识/推理任务上退化到 random，这意味着论文展示的\"最引人注目\"的改善点（49% PPL reduction at 50%）在实践中可能不相关。审稿人需要知道：在什么稀疏度下，该方法能同时保持合理的 PPL 和 downstream performance？\n- 建议修改方向：(1) 在主实验中更突出讨论 PPL-downstream disconnect；(2) 将 30% 的 downstream 结果提升到与 50% PPL 同等重要的位置；(3) 考虑补充 10-20% sparsity 下的 downstream 评估，找到 practical sweet spot。\n\n**N3 [critical] 训练-推理 mask 不匹配未被分析，且残差退化来源不明。**\n- 具体位置：§3.3 (Gumbel-Sigmoid, τ annealed to 0.1), §4.1 (predictor-TEAL inference), Appendix B Table 5\n- 问题：训练使用 soft Gumbel-Sigmoid mask（即使 τ=0.1 也非完全 binary），推理使用 TEAL 的 hard top-k allocation。Table 5 (Appendix B) 揭示了关键数据：d_b=128 在 per-token 评估下 PPL=9.218，在 TEAL global 下 PPL=11.963——差距约 30%。这意味着从 dense (6.12) 到 KL-TEAL (11.79) 的全部退化（Δ=5.67）中，有相当一部分可能来自 soft→hard mismatch 和 TEAL global allocation 的信息丢失，而非 sparsity 本身的 capacity loss。论文从未正式分析这一 gap 的来源。\n- 为什么影响接收：不分析这个 gap，读者无法判断剩余退化是方法可以改进的（通过 better allocation 或 better train-test alignment）还是 fundamental limit。这直接关系到方法的 ceiling 和 future improvement 空间。\n- 建议修改方向：添加分解分析，例如：(1) per-token hard mask evaluation（控制 allocation）；(2) per-token soft mask evaluation（Table 5 已有）；(3) global hard mask with oracle scores。分离 mask quality loss、discretization loss 和 allocation loss。\n\n---\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1 [warning] BCE 对比的公平性问题：系统差异超过 loss function。**\n- 具体位置：Table 3 ablation\n- 问题：KL 系统 = Forward KL + Gumbel-Sigmoid + penalty controller；BCE 系统 = BCE + hard mask + compensation。消融中 \"BCE + Gumbel + Penalty\" 达到 38.02（比 vanilla BCE 的 27.97 更差），说明 penalty 框架与 BCE 不兼容。这意味着 Table 2 中的 KL vs BCE 对比不仅是 loss function 的差异，而是整个 training pipeline 的差异。KL+STE (15.77) 提供了更接近的对比，但 STE 本身的 gradient bias 也是 confound。\n- 建议：明确说明 KL 的优势来自 loss function + compatible training infrastructure 的组合，而非单独的 loss function。或提供一个更直接的 fair comparison（例如 MSE on output logits + Gumbel，控制 training infrastructure 的同时对比 loss）。\n\n**W2 [warning] \"Parameter-free\" penalty controller 表述不准确。**\n- 具体位置：§3.4, footnote (\"parameter-free, no step-size tuning\"), Table 7\n- 问题：λ_max 在不同 sparsity target 下取不同值（30% 和 70% 用 5000，50% 用 1000），这本身就是 hyperparameter。Table 7 显示 30% target 时 λ 达到 cap (5000)，actual sparsity = 0.285（偏差 5%）。Controller 无法在所有 target 下精确收敛。\n- 建议：去掉 \"parameter-free\" 措辞；讨论 λ_max 选择对结果的影响；说明 30% 时 5% deviation 对 PPL 的影响。\n\n**W3 [warning] 统计效力不足。**\n- 具体位置：Appendix F (3 seeds, 50% uniform only)\n- 问题：(1) 3 seeds 的 95% CI（≈ [11.73, 12.11]，t-distribution）较宽，对 Table 3 中差异 <1 的 ablation 结果（如 Forward KL 11.79 vs JSD 12.54），无法判断统计显著性。(2) Multi-seed 仅在 50% uniform 下做，主结果（50% global TEAL, PPL 11.79）无方差估计。(3) Downstream metrics 更 noisy（ARC-c 33.8±1.2%），3 seeds 不足以支撑 downstream 的 regime 分析结论。\n- 建议：至少在 primary configuration (50% global TEAL) 也报告 multi-seed；考虑增加到 5 seeds。\n\n**W4 [warning] 实验规模受限。**\n- 具体位置：§4.1, §4.6, Limitations\n- 问题：仅 7-8B 模型（LLaMA-3.1-8B, Mistral-7B-v0.3），同一参数量级，同为 SwiGLU。论文多处使用 \"transfers across SwiGLU architectures\" 但实际上 (a) 仅测试了一个 scale，(b) 两个模型的 d_ff / d_model ratio 相同（14336/4096），(c) Mistral 的主要差异是 GQA + sliding window attention，这些差异与 FFN sparsity prediction 关系不大。\n- 建议：弱化 generalization claims，改为 \"verified on two 7-8B SwiGLU models\"。如果可能，增加 13B 或更大模型的验证。\n\n**W5 [warning] Gradient SNR 测量与训练设置不一致。**\n- 具体位置：§3.5 empirical verification\n- 问题：SNR 在 C4 数据上测量（\"80 steps on LLaMA-3.1-8B (C4 data)\"），但训练使用 WikiText-103。不同数据分布可能影响 SNR，使该测量不能直接代表训练过程中的实际 gradient quality。\n- 建议：在 WikiText-103 上重复 SNR 测量，或解释为何选择 C4 及其对结论的影响。\n\n**W6 [warning] 训练数据集过小且与评估数据同源。**\n- 具体位置：§4.1 (\"trained for 1000 steps on WikiText-103 with batch size 4\")\n- 问题：1000 steps × batch 4 × seq 2048 = ~8M tokens，仅为 WikiText-103 全集的一小部分。评估在 WikiText-2 上——与 WikiText-103 同源（都是 Wikipedia）。虽然 Appendix D 的 C4 OOD 评估有所缓解，但仅有一个 sparsity level (50%) 和一个 metric (PPL)。\n- 建议：在 C4 上补充 30% 和 70% 的评估；如果条件允许，考虑在非 Wikipedia 数据上训练一版 predictor 验证泛化性。\n\n---\n\n### 小问题（不影响接收）\n\n- **M1**: AdamW 的 weight decay 值未报告（§4.1）。\n- **M2**: BCE 的 oracle mask 生成方式（per-layer top-k 还是 global top-k？）未明确说明（§3.5 \"oracle masks m_j* = 1[|g_j| ≥ top-k threshold]\"，但 threshold 的作用域不清楚）。\n- **M3**: Table 1 将 ShadowLLM 归为 \"Per-layer\"，但 ShadowLLM 使用 attention-based routing，可能更接近 per-token。需核实分类准确性。\n- **M4**: loshchilov2019adamw 引用年份为 2019，OpenAlex 匹配到的原始 arXiv 年份为 2017。会议发表年份与 arXiv 年份不一致，建议统一。\n- **M5**: Appendix A 的 latency 测量在 RTX PRO 6000 Blackwell 上，但训练在 A6000 上（Limitations 提到 \"~17 minutes on A6000\"）。两个 GPU 架构差异较大，latency 数据的可迁移性不明。\n\n---\n\n## Questions to Authors\n\n**Q1.** Table 5 (Appendix B) 显示 d_b=128 per-token PPL = 9.218, TEAL global PPL = 11.963。这 ~30% 的 gap 中，有多少来自 soft→hard discretization，多少来自 TEAL global 的 budget allocation 策略？能否提供 per-token hard mask evaluation 来分离这两个因素？\n\n**Q2.** BCE 对比中，BCE 的 learning rate 和 optimizer 设置是否与 KL 完全一致？如果不一致，BCE 是否经过独立的 hyperparameter tuning？\n\n**Q3.** 论文称 \"KL's near-random precision (0.51)\"——这是否意味着 KL predictor 学到的 mask 与 magnitude-based oracle 几乎无相关性？如果是，KL predictor 到底保留了哪些 neuron——是否有 per-layer 的分析可以说明 KL mask 与 oracle mask 的差异模式？\n\n**Q4.** 30% sparsity 下 penalty controller 达到 λ cap (5000) 且 actual sparsity = 28.5%。如果 λ_max 设为更大的值（如 10000），sparsity 能否达到 30%？如果能，PPL 会如何变化？\n\n**Q5.** 是否尝试过在训练中使用 hard top-k (with STE) 替代 Gumbel-Sigmoid 来缩小 train-test gap？Table 3 已有 KL+STE 但未说明其是否使用 top-k selection。\n\n---\n\n## 官方维度打分（ACL Rolling Review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心梯度分析数学正确，factor (a)-(d) 分解完整。Gumbel-Sigmoid 使用正确。但 BCE 对比的公平性有 confound (W1)；train-test mask mismatch 未分析 (N3)；penalty controller 在边界情况下表现不佳 (W2)。 |\n| Excitement | 2.5/5 | \"正确 loss > 高精度 proxy\" 的洞察有价值，oracle F1 分析令人信服。2D taxonomy 有组织贡献。但无实际 speedup (N1) 和 downstream collapse (N2) 严重限制了实际影响力。 |\n| Reproducibility | 3.5/5 | 训练设置报告较全（model, data, steps, LR, optimizer, τ schedule）。缺少 weight decay、gradient clipping、evaluation batch size。未提及代码是否会开源。Appendix 的超参数 sensitivity 分析有利于复现。 |\n| Overall | 3/5 | Findings 边界。理论洞察清晰且有实证支撑，但 practical impact 受限于 (1) 无 wall-clock speedup, (2) downstream collapse, (3) limited scale。 |\n| Confidence | 4/5 | 对 activation sparsity 和 knowledge distillation 领域较熟悉，仔细阅读了全文和附录。 |\n\n---\n\n## 总体评分\n\n**Overall**: 3/5 (Findings acceptance)\n\n**一句话总结**: 论文提供了有价值的理论洞察（KL 梯度耦合解决 BCE 的结构性不匹配），实验设计合理但存在 BCE 对比公平性和 train-test mismatch 未分析的问题；无实际推理加速和下游任务崩溃严重限制了实用价值，适合 Findings 而非主会议。\n\n---\n\n## 主要优势\n\n- 梯度分析形式化清晰，factor (a)-(d) 分解为理解 loss function 设计提供了有用的分析框架\n- Oracle F1 分析（BCE F1=0.613 > KL F1=0.540，但 PPL 差 91%）是全文最有说服力的实验，直接 falsify 了 \"per-neuron accuracy = output quality\" 的隐含假设\n- 消融设计系统全面，loss isolation 实验（BCE + Gumbel + Penalty = 38.02）有效分离了 loss function 和 training infrastructure 的贡献\n- 三 regime 分析发现了 allocation preference 的非单调性，对部署决策有实用指导价值\n- 写作质量好，结构清晰，主线统一\n",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 149 · 2026-05-17T08:18:01.814613+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4066
}
```

</details>

---


### Assistant

_source line 150 · 2026-05-17T08:18:09.122193+00:00_

审稿意见已提交给 Review Director。

总结：

- **Overall 3/5 (Findings 边界)**
- **3 个 critical 问题**：(1) 无 wall-clock speedup 与 efficiency framing 矛盾；(2) 下游任务在 50% sparsity 崩溃至 random，PPL 改善不转化为 reasoning 保持；(3) 训练时 soft Gumbel mask vs 推理时 hard top-k 的 mismatch（~30% PPL gap）未被分析
- **6 个 warning 问题**：BCE 对比公平性、"parameter-free" 表述不准确、3-seed 统计效力不足、仅 7-8B 规模、SNR 测量数据不一致、训练评估数据同源
- **主要优势**：梯度分析形式化清晰，oracle F1 分析令人信服，消融覆盖全面，regime 分析有实用价值

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1"
}
```

</details>

---


## Round 7

## Round 7

8 recorded events


### User

_source line 151 · 2026-05-17T08:19:46.958593+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix / Should-Fix / 小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 — Round 1 审稿意见（新颖性 + 完整性）

### 总体评分
**Overall**: 3.0 / 5 (Findings)
**一句话总结**: 核心方法是已有技术（KL distillation + Gumbel relaxation）在新场景（per-token activation sparsity）的组合应用，执行质量扎实但新颖性有限；downstream metrics 与 PPL 叙事存在系统性矛盾，削弱了核心 claim 的说服力。

### Must-Fix 问题

**N1** [critical] Responsible NLP Research Checklist 缺失，desk rejection 风险
- ARR 自 2024-12 起强制要求此 checklist，缺失可直接 desk reject。论文无 checklist 也无 Ethics Statement。
- 建议：参照 aclrollingreview.org/responsibleNLPresearch/ 逐项填写。

**N2** [critical] Downstream metrics 与 PPL-centric 叙事系统性矛盾
- Table 1: 30% sparsity KL global MMLU = 25.27%，比 TEAL vanilla (38.61%) 低 13.3pp。50% sparsity MMLU 全部 ≈28%（近随机），KL (27.89%) vs TEAL (28.32%) 无差异。GSM8K 50% KL (1.29%) 比 TEAL (1.97%) 更差。
- 论文核心叙事围绕 PPL 改善（11.79 vs 23.31），但 downstream 讲了不同的故事。如果 PPL 改善不转化为 downstream 收益，"eliminates compensation networks" 的实际价值需重新评估。
- Limitations 承认 PPL is poor proxy for reasoning，但 Abstract/Introduction 仍以 PPL 为核心 framing，自相矛盾。
- 建议：Abstract/Introduction 诚实呈现 downstream mixed results；讨论 KL 训练为何恶化 MMLU（可能过度偏向 PPL-dominant layers）。

**N3** [critical] 与 MaskLLM 核心技术重叠未充分辨析
- MaskLLM (NeurIPS 2024) 同样用 frozen weights + learnable masks + Gumbel relaxation + KL divergence。Related Work 仅以 "weight vs activation, static vs contextual" 区分，但这是应用场景差异而非方法论差异。核心 pipeline（KL + Gumbel mask learning with frozen weights）相同。
- 论文未讨论：(1) Gumbel-Softmax (MaskLLM) vs Gumbel-Sigmoid (本文) 的技术原因；(2) MaskLLM 是否已隐含解决 structural mismatch；(3) 如果 MaskLLM 的 mask 改为 input-dependent 是否等价于本文方法。
- 建议：明确讨论方法论层面的区别和联系。

### Should-Fix 问题

**W1** [warning] 三 regime 分析证据不足以支撑 claim 强度
- 三 regime 定义来自 2 个模型 × 3 个 sparsity levels = 6 数据点。具体边界阈值（≤30%, ~40%, ≥50%）的跨规模/跨架构泛化性完全未验证，但论文作为 Contribution 之一呈现。

**W2** [warning] D2DMoE (NeurIPS 2024) 遗漏
- Dense-to-Dynamic-k MoE 训练 router 用 ℓ2-norm regression 预测 expert 贡献，实现 per-token activation sparsity。其 training signal 既非 BCE 也非 KL，应位于 taxonomy 的 Per-token × Intermediate cell。遗漏使 taxonomy 不完整。

**W3** [warning] Abstract 数据堆砌（18+ 个数字），审稿人 30 秒内无法消化

**W4** [warning] 无实际 wall-clock speedup（+6.4% overhead），但 framing 暗示 efficiency gain

**W5** [warning] Taxonomy 可能 post-hoc rationalization
- 3×3 中仅 4 cell 填充，5 cell 空。两个轴恰好让本文独占一 cell。DejaVu 被归类为 Per-token × Decomposed 但 Table 2 中缺失。

**W6** [warning] WAS (EMNLP 2025 main) 可能遗漏

### 小问题
- Abstract 中 "-ing" 分词短语有轻微 AI 写作痕迹
- xu2026spon bib year=2026 vs OpenAlex=2025
- Table 2 缺 DejaVu
- Figure 1 label "fig:taxonomy" 但内容是 method overview
- Conclusion 仅 3 行过短

### 主要优势
1. Gradient analysis 清晰有力，SNR 验证
2. Ablation 系统全面，loss isolation 有力
3. Cross-architecture Mistral 验证一致
4. F1 oracle analysis 优雅
5. 训练成本低

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 152 · 2026-05-17T08:20:35.058321+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 153 · 2026-05-17T08:20:35.360223+00:00_

1	Activation sparsity reduces the effective computation in SwiGLU-based LLMs by pruning FFN neurons at inference, but existing learned predictors trained with binary cross-entropy (BCE) require error compensation networks due to a structural mismatch: BCE decomposes per neuron while inference uses global top-$k$ allocation across all layers.
2	We train lightweight predictors (2.37M parameters per layer, 75.9M total, $<$1\% of the base model) with KL divergence, which couples all neurons through the output distribution via Gumbel-Sigmoid relaxation, eliminating the need for compensation.
3	On LLaMA-3.1-8B (WikiText-2), our KL-trained predictor achieves perplexity 11.79 at 50\% sparsity without compensation, compared to 23.31 for vanilla TEAL and 27.97 for BCE trained at 2.71$\times$ the compute budget, whose loss saturates, confirming a structural rather than computational failure.
4	Three-seed evaluation confirms training stability (PPL $11.92 \pm 0.07$, CV${<}$1\% under uniform allocation).
5	The KL advantage grows disproportionately with sparsity: 18\% relative improvement at 30\%, 49\% at 50\%, and 82\% at 70\% (PPL 17.91 vs.\ 100.11); KL itself incurs $2.93\times$ the dense baseline, demonstrating substantial output fidelity even at extreme sparsity.
6	Cross-architecture evaluation on Mistral-7B-v0.3 confirms the advantage transfers across SwiGLU architectures at the 7--8B parameter scale, with consistent KL-over-TEAL ratios (within 7\% at $\leq$50\% sparsity).
7	SPON's static bias correction proves near-orthogonal to the predictor (cosine similarity 0.196), providing only 2.4\% relative PPL improvement (12.08$\to$11.79 under \texttt{evaluate.py}).
8	We propose a two-dimensional taxonomy over correction granularity $\times$ training signal coupling that unifies prior methods and identify three distinct sparsity regimes (budget-surplus, budget-constrained, and capacity-limited) that govern the quality-sparsity tradeoff.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 154 · 2026-05-17T08:20:35.412284+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 155 · 2026-05-17T08:20:35.463127+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude, achieving 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking.
6	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
7	
8	\paragraph{Predictor-Based Contextual Sparsity.}
9	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
10	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with MSE supervision but retains per-neuron decomposition.
11	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
12	PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.
13	MaskLLM~\cite{fang2024maskllm} also employs learnable masks with Gumbel relaxation and frozen weights, but targets N:M semi-structured \emph{weight} sparsity (2:4 patterns) via Gumbel-Softmax, producing fixed masks independent of input tokens.
14	In contrast, our method learns \emph{activation} masks that are contextual (per-token), unstructured (budget-constrained global top-$k$), and trained with Gumbel-Sigmoid to minimize output-distribution divergence.
15	All prior predictor-based methods use decomposed (BCE) or intermediate (MSE) objectives where each neuron's gradient is independent of other mask states.
16	Our \emph{coupled} KL objective propagates gradients through all downstream layers, optimizing for global allocation quality without compensation.
…[truncated 2049 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 156 · 2026-05-17T08:22:21.868188+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 对 Reviewer 2 Round 1 意见的交叉回应\n\n---\n\n## Must-Fix 问题\n\n### [AGREE] R2-N1: Responsible NLP Research Checklist 缺失\n\n同意。我在 Round 1 审稿中遗漏了这一检查。main.tex 中确无 checklist 或 Ethics Statement。ARR 自 2024-12 起强制要求，缺失确实构成 desk rejection 风险。这是纯粹的格式合规问题，作者应立即补充。\n\n---\n\n### [AGREE] R2-N2: Downstream metrics 与 PPL-centric 叙事系统性矛盾\n\n强烈同意，这与我自己的 N2 一致。R2 进一步指出了一个我未充分强调的关键数据点：**30% sparsity 下 KL global 的 MMLU (25.27%) 比 TEAL vanilla (38.61%) 低 13.3pp**（Table 2）。这意味着 KL predictor 在 PPL 维度改善的同时，MMLU 反而显著恶化，KL 训练可能过度优化 token prediction 分布而牺牲了知识保留。\n\n补充我的观察：Table 4 (§4.4) 显示 KL uniform 在 30% 时恢复 MMLU 到 40.61%（+15.3pp over global），说明问题可能不在 KL 训练本身，而在 global top-k allocation 对 late layers（logit-forming layers）的 starvation 效应。§4.4 提到 \"L31 retention 28.4%\"，知识密集层被剥夺 budget 是 MMLU 崩溃的直接原因。但论文对此的讨论仅限于 regime analysis（§4.4），未反映到 Abstract/Introduction 的核心叙事中——R2 的 \"自相矛盾\" 判断准确。\n\n---\n\n### [REBUT] R2-N3: 与 MaskLLM 核心技术重叠\n\n**部分同意论文讨论不足，但不同意\"核心技术重叠\"的判断。**\n\nR2 正确指出 Related Work (§5 第2段) 对 MaskLLM 的区分过于简略——仅以 \"weight vs activation, static vs contextual\" 一笔带过。论文确实应更深入讨论方法论层面的联系。但 R2 将两者描述为 \"核心 pipeline 相同\" 忽略了关键的结构差异：\n\n1. **优化问题本质不同。** MaskLLM 学习 static masks（每个 N:M group 内选哪些 weight 保留），优化空间是 $\\binom{M}{N}$ 的 categorical distribution per group。本文学习 per-token contextual masks（每个 input position 独立决定哪些 neurons 保留），优化空间是 $\\{0,1\\}^{L \\times d_{ff}}$ 的 combinatorial space，受 global budget constraint。MaskLLM 没有 \"structural mismatch\" 问题——它的 masks 在训练和推理中都是 group-local 的，不存在 per-element 训练 vs. global allocation 推理的矛盾。\n\n2. **本文的核心贡献不是 \"KL + Gumbel\" pipeline 本身，而是 §3.5 的梯度分析。** Factor (a)-(d) 分解证明了 per-neuron BCE 和 end-to-end KL 在 contextual prediction + global top-k 设定下的结构性差异（factor (b) 的 downstream Jacobian 耦合）。这个分析对 MaskLLM 不适用——MaskLLM 的 masks 是 input-independent 的，不涉及 contextual prediction 的 gradient flow。\n\n3. **R2 的第三个问题 \"如果 MaskLLM 改为 input-dependent 是否等价\" 值得讨论**，但答案是否定的：(a) MaskLLM 用 Gumbel-Softmax 在 N:M group 内做 categorical selection，本文用 Gumbel-Sigmoid 做 binary per-neuron decisions + global budget constraint——relaxation 机制不同；(b) MaskLLM 的 allocation 是 per-group structured (2:4)，本文是 unstructured global top-k——inference protocol 不同；(c) 即使改为 input-dependent，MaskLLM 的 per-group 结构不产生 global coupling 问题。\n\n**结论：同意论文应更充分讨论 MaskLLM（especially 技术原因 for Gumbel-Softmax vs Sigmoid），但 \"核心技术重叠\" 的判断不成立。本文的核心新颖性在于 structural mismatch 的识别和梯度分析（§3.5），这在 MaskLLM 的设定中不存在。** 建议作者添加一段专门的 MaskLLM 技术对比。\n\n---\n\n## Should-Fix 问题\n\n### [AGREE] R2-W1: 三 regime 分析证据不足\n\n同意。2 models × 3 sparsity levels = 6 个数据点。具体 regime 边界（≤30%, ~40%, ≥50%）的泛化性完全未验证。这与我的 W4（实验规模受限）一致。作为 Contribution 之一呈现，claim 强度应降低为 \"empirical observation on 7-8B models\" 而非 general framework。补充：regime 边界可能与模型规模、架构、预训练数据量密切相关，论文未讨论这些 confounds。\n\n---\n\n### [AGREE] R2-W2: D2DMoE 遗漏\n\n同意。如果 D2DMoE (NeurIPS 2024) 使用 ℓ2-norm regression（intermediate objective）进行 per-token router training，它应填入 Table 1 的 Per-token × Intermediate cell（当前为空）。这不仅是引用遗漏，还影响 taxonomy 的完整性——本文 claim \"no prior work has combined per-token contextual prediction with a coupled training signal\"（§3.6 末段），但 taxonomy 中应先确认所有 cell 的 occupancy 状态。\n\n---\n\n### [AGREE] R2-W3: Abstract 数据堆砌\n\n同意。我统计 Abstract 中至少有 **25 个数字/百分比**（2.37M, 75.9M, <1%, 11.79, 50%, 23.31, 27.97, 2.71×, 11.92±0.07, CV<1%, 18%, 30%, 49%, 50%, 82%, 70%, 17.91, 100.11, 2.93×, 7-8B, 7%, ≤50%, 0.196, 2.4%, 12.08→11.79）。审稿人在 30 秒内无法从中提取核心信息。按照 ACL 论文写作规范，Abstract 应以叙事为主、最多引用 2-3 个关键数字。当前 Abstract 更像 Results 的压缩版，不是独立的故事。\n\n---\n\n### [AGREE] R2-W4: 无实际 wall-clock speedup\n\n同意，与我的 N1 一致。Appendix A Table 6 明确显示 +6.4% overhead。\n\n---\n\n### [AGREE] R2-W5: Taxonomy 可能 post-hoc rationalization\n\n部分同意。5/9 cells 空的确引发 post-hoc 质疑，尤其是两个轴恰好让本文独占一 cell。但我认为两个轴本身有独立的组织价值（correction granularity 和 training signal coupling 是文献中可辨认的真实维度），因此判断为 \"presentation concern\" 而非 \"validity concern\"。\n\n补充：R2 指出 DejaVu 在 Table 1 中被归类但 Table 2 中缺失——这确实是一个重要遗漏。如果 DejaVu 是 Per-token × Decomposed 的代表方法，它应该作为 baseline 出现在实验对比中。当前 Table 2 的 BCE baseline 未说明是否等同于 DejaVu 的实现。\n\n---\n\n### [REBUT] R2-W6: WAS (EMNLP 2025) 可能遗漏\n\n无法确认。R2 未提供 WAS 的完整标题、作者或链接。如果 R2 能提供具体引用信息，我可以评估其与本文的相关性。仅凭缩写无法判断是否确实是重要遗漏。\n\n---\n\n## 小问题\n\n**[AGREE]** Abstract -ing 分词短语。Abstract 确有多处 -ing 结尾：\"eliminating the need for compensation\", \"confirming a structural rather than computational failure\", \"confirming training stability\", \"demonstrating substantial output fidelity\"。这是典型的 AI 写作标志，应改写。\n\n**[AGREE]** xu2026spon bib year 不一致。references.bib 中 `year = {2026}`，如果 OpenAlex 显示 2025，应核实论文实际发表/接收年份。\n\n**[AGREE]** Table 2 缺 DejaVu。如 W5 中所述，taxonomy 中提到的方法应尽可能出现在实验对比中。\n\n**[AGREE]** Figure 1 label 为 `fig:taxonomy` 但内容是 method overview。§3.6 最后一段 \"Figure~\\ref{fig:taxonomy}\" 引用的是 Figure 1（method overview），但 taxonomy 实际在 Table 1。标签应改为 `fig:overview` 或类似。\n\n**[AGREE]** Conclusion 仅 3 行过短。§6 只有一段（conclusion.tex 仅 6 行 LaTeX），没有 future work discussion、没有 broader implications。对于一篇 long paper 这不符合预期。\n\n---\n\n## 对 R2 总体判断的评价\n\nR2 给出 Overall 3.0/5 (Findings)，与我的判断一致。R2 的新颖性质疑（R2-N3 MaskLLM overlap）是本次评审的核心分歧点。我的立场是：方法论工具确实不新（KL + Gumbel），但 structural mismatch 的识别和梯度分析（§3.5）是本文真正的贡献所在，这在 MaskLLM 的设定中不存在。论文应通过更充分的 MaskLLM 对比来突出这一点。\n\nR2 的 checklist 缺失（R2-N1）和 D2DMoE 遗漏（R2-W2）是我 Round 1 遗漏的有价值发现。Abstract 数据堆砌（R2-W3）的具体量化（18+ 数字）也比我更到位。\n\n两位 Reviewer 一致认为的核心问题：(1) downstream collapse vs PPL framing 矛盾，(2) 无 wall-clock speedup，(3) 实验规模有限。这三点是决定接收/拒绝的关键。\n",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 对 Reviewer 2 Round 1 意见的交叉回应\n\n---\n\n## Must-Fix 问题\n\n### [AGREE] R2-N1: Responsible NLP Research Checklist 缺失\n\n同意。我在 Round 1 审稿中遗漏了这一检查。main.tex 中确无 checklist 或 Ethics Statement。ARR 自 2024-12 起强制要求，缺失确实构成 desk rejection 风险。这是纯粹的格式合规问题，作者应立即补充。\n\n---\n\n### [AGREE] R2-N2: Downstream metrics 与 PPL-centric 叙事系统性矛盾\n\n强烈同意，这与我自己的 N2 一致。R2 进一步指出了一个我未充分强调的关键数据点：**30% sparsity 下 KL global 的 MMLU (25.27%) 比 TEAL vanilla (38.61%) 低 13.3pp**（Table 2）。这意味着 KL predictor 在 PPL 维度改善的同时，MMLU 反而显著恶化，KL 训练可能过度优化 token prediction 分布而牺牲了知识保留。\n\n补充我的观察：Table 4 (§4.4) 显示 KL uniform 在 30% 时恢复 MMLU 到 40.61%（+15.3pp over global），说明问题可能不在 KL 训练本身，而在 global top-k allocation 对 late layers（logit-forming layers）的 starvation 效应。§4.4 提到 \"L31 retention 28.4%\"，知识密集层被剥夺 budget 是 MMLU 崩溃的直接原因。但论文对此的讨论仅限于 regime analysis（§4.4），未反映到 Abstract/Introduction 的核心叙事中——R2 的 \"自相矛盾\" 判断准确。\n\n---\n\n### [REBUT] R2-N3: 与 MaskLLM 核心技术重叠\n\n**部分同意论文讨论不足，但不同意\"核心技术重叠\"的判断。**\n\nR2 正确指出 Related Work (§5 第2段) 对 MaskLLM 的区分过于简略——仅以 \"weight vs activation, static vs contextual\" 一笔带过。论文确实应更深入讨论方法论层面的联系。但 R2 将两者描述为 \"核心 pipeline 相同\" 忽略了关键的结构差异：\n\n1. **优化问题本质不同。** MaskLLM 学习 static masks（每个 N:M group 内选哪些 weight 保留），优化空间是 $\\binom{M}{N}$ 的 categorical distribution per group。本文学习 per-token contextual masks（每个 input position 独立决定哪些 neurons 保留），优化空间是 $\\{0,1\\}^{L \\times d_{ff}}$ 的 combinatorial space，受 global budget constraint。MaskLLM 没有 \"structural mismatch\" 问题——它的 masks 在训练和推理中都是 group-local 的，不存在 per-element 训练 vs. global allocation 推理的矛盾。\n\n2. **本文的核心贡献不是 \"KL + Gumbel\" pipeline 本身，而是 §3.5 的梯度分析。** Factor (a)-(d) 分解证明了 per-neuron BCE 和 end-to-end KL 在 contextual prediction + global top-k 设定下的结构性差异（factor (b) 的 downstream Jacobian 耦合）。这个分析对 MaskLLM 不适用——MaskLLM 的 masks 是 input-independent 的，不涉及 contextual prediction 的 gradient flow。\n\n3. **R2 的第三个问题 \"如果 MaskLLM 改为 input-dependent 是否等价\" 值得讨论**，但答案是否定的：(a) MaskLLM 用 Gumbel-Softmax 在 N:M group 内做 categorical selection，本文用 Gumbel-Sigmoid 做 binary per-neuron decisions + global budget constraint——relaxation 机制不同；(b) MaskLLM 的 allocation 是 per-group structured (2:4)，本文是 unstructured global top-k——inference protocol 不同；(c) 即使改为 input-dependent，MaskLLM 的 per-group 结构不产生 global coupling 问题。\n\n**结论：同意论文应更充分讨论 MaskLLM（especially 技术原因 for Gumbel-Softmax vs Sigmoid），但 \"核心技术重叠\" 的判断不成立。本文的核心新颖性在于 structural mismatch 的识别和梯度分析（§3.5），这在 MaskLLM 的设定中不存在。** 建议作者添加一段专门的 MaskLLM 技术对比。\n\n---\n\n## Should-Fix 问题\n\n### [AGREE] R2-W1: 三 regime 分析证据不足\n\n同意。2 models × 3 sparsity levels = 6 个数据点。具体 regime 边界（≤30%, ~40%, ≥50%）的泛化性完全未验证。这与我的 W4（实验规模受限）一致。作为 Contribution 之一呈现，claim 强度应降低为 \"empirical observation on 7-8B models\" 而非 general framework。补充：regime 边界可能与模型规模、架构、预训练数据量密切相关，论文未讨论这些 confounds。\n\n---\n\n### [AGREE] R2-W2: D2DMoE 遗漏\n\n同意。如果 D2DMoE (NeurIPS 2024) 使用 ℓ2-norm regression（intermediate objective）进行 per-token router training，它应填入 Table 1 的 Per-token × Intermediate cell（当前为空）。这不仅是引用遗漏，还影响 taxonomy 的完整性——本文 claim \"no prior work has combined per-token contextual prediction with a coupled training signal\"（§3.6 末段），但 taxonomy 中应先确认所有 cell 的 occupancy 状态。\n\n---\n\n### [AGREE] R2-W3: Abstract 数据堆砌\n\n同意。我统计 Abstract 中至少有 **25 个数字/百分比**（2.37M, 75.9M, <1%, 11.79, 50%, 23.31, 27.97, 2.71×, 11.92±0.07, CV<1%, 18%, 30%, 49%, 50%, 82%, 70%, 17.91, 100.11, 2.93×, 7-8B, 7%, ≤50%, 0.196, 2.4%, 12.08→11.79）。审稿人在 30 秒内无法从中提取核心信息。按照 ACL 论文写作规范，Abstract 应以叙事为主、最多引用 2-3 个关键数字。当前 Abstract 更像 Results 的压缩版，不是独立的故事。\n\n---\n\n### [AGREE] R2-W4: 无实际 wall-clock speedup\n\n同意，与我的 N1 一致。Appendix A Table 6 明确显示 +6.4% overhead。\n\n---\n\n### [AGREE] R2-W5: Taxonomy 可能 post-hoc rationalization\n\n部分同意。5/9 cells 空的确引发 post-hoc 质疑，尤其是两个轴恰好让本文独占一 cell。但我认为两个轴本身有独立的组织价值（correction granularity 和 training signal coupling 是文献中可辨认的真实维度），因此判断为 \"presentation concern\" 而非 \"validity concern\"。\n\n补充：R2 指出 DejaVu 在 Table 1 中被归类但 Table 2 中缺失——这确实是一个重要遗漏。如果 DejaVu 是 Per-token × Decomposed 的代表方法，它应该作为 baseline 出现在实验对比中。当前 Table 2 的 BCE baseline 未说明是否等同于 DejaVu 的实现。\n\n---\n\n### [REBUT] R2-W6: WAS (EMNLP 2025) 可能遗漏\n\n无法确认。R2 未提供 WAS 的完整标题、作者或链接。如果 R2 能提供具体引用信息，我可以评估其与本文的相关性。仅凭缩写无法判断是否确实是重要遗漏。\n\n---\n\n## 小问题\n\n**[AGREE]** Abstract -ing 分词短语。Abstract 确有多处 -ing 结尾：\"eliminating the need for compensation\", \"confirming a structural rather than computational failure\", \"confirming training stability\", \"demonstrating substantial output fidelity\"。这是典型的 AI 写作标志，应改写。\n\n**[AGREE]** xu2026spon bib year 不一致。references.bib 中 `year = {2026}`，如果 OpenAlex 显示 2025，应核实论文实际发表/接收年份。\n\n**[AGREE]** Table 2 缺 DejaVu。如 W5 中所述，taxonomy 中提到的方法应尽可能出现在实验对比中。\n\n**[AGREE]** Figure 1 label 为 `fig:taxonomy` 但内容是 method overview。§3.6 最后一段 \"Figure~\\ref{fig:taxonomy}\" 引用的是 Figure 1（method overview），但 taxonomy 实际在 Table 1。标签应改为 `fig:overview` 或类似。\n\n**[AGREE]** Conclusion 仅 3 行过短。§6 只有一段（conclusion.tex 仅 6 行 LaTeX），没有 future work discussion、没有 broader implications。对于一篇 long paper 这不符合预期。\n\n---\n\n## 对 R2 总体判断的评价\n\nR2 给出 Overall 3.0/5 (Findings)，与我的判断一致。R2 的新颖性质疑（R2-N3 MaskLLM overlap）是本次评审的核心分歧点。我的立场是：方法论工具确实不新（KL + Gumbel），但 structural mismatch 的识别和梯度分析（§3.5）是本文真正的贡献所在，这在 MaskLLM 的设定中不存在。论文应通过更充分的 MaskLLM 对比来突出这一点。\n\nR2 的 checklist 缺失（R2-N1）和 D2DMoE 遗漏（R2-W2）是我 Round 1 遗漏的有价值发现。Abstract 数据堆砌（R2-W3）的具体量化（18+ 数字）也比我更到位。\n\n两位 Reviewer 一致认为的核心问题：(1) downstream collapse vs PPL framing 矛盾，(2) 无 wall-clock speedup，(3) 实验规模有限。这三点是决定接收/拒绝的关键。\n",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 157 · 2026-05-17T08:22:25.731398+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3863
}
```

</details>

---


### Assistant

_source line 158 · 2026-05-17T08:22:32.554052+00:00_

交叉回应已提交。

要点总结：
- **R2-N1 (Checklist)**: [AGREE]，我 Round 1 遗漏的有效发现，desk reject 风险
- **R2-N2 (Downstream)**: [AGREE]，与我的 N2 一致，R2 补充了 MMLU 在 KL global 下比 TEAL 更差的关键数据点
- **R2-N3 (MaskLLM overlap)**: [REBUT]，同意讨论不足但不同意"核心技术重叠"——本文的核心贡献是 §3.5 structural mismatch 梯度分析，这在 MaskLLM 的 static N:M 设定中不存在
- **R2-W1~W5**: 全部 [AGREE]，其中 D2DMoE 遗漏和 Abstract 数据堆砌是我 Round 1 未充分覆盖的
- **R2-W6 (WAS)**: [REBUT]，信息不足无法判断

两位 Reviewer 一致的三个核心问题：downstream collapse vs PPL framing、无 wall-clock speedup、实验规模有限。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1"
}
```

</details>

---


## Round 8

## Round 8

88 recorded events


### User

_source line 159 · 2026-05-17T09:05:18.512251+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。

## Venue 信息
- **目标**: EMNLP 2026（ARR May 2026 cycle）
- **截止日期**: 2026-05-25
- **格式**: ACL 模板 `[review]`，Long paper 8 页正文 + 无限引用页
- **匿名**: Double-blind
- **Limitations**: 必须有，不计页数，位于 conclusion 之后 references 之前
- **Responsible NLP Checklist**: 必填，错误/遗漏可 desk reject
- **附录**: 允许，在 references 之后，双栏

## 论文路径
`projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex, related_work.tex）

## 你的审查侧重

### 1. 方法论严谨性
- §3.5 梯度分析（BCE vs KL gradient structure）的数学正确性——chain rule 推导、因子分解是否严谨
- §3.4 Adaptive Penalty Controller 的收敛保证——multiplicative schedule 的理论依据、与 formal Lagrangian 的区别是否充分说明
- Gumbel-Sigmoid relaxation 在 train-inference mismatch 下的影响分析是否充分
- "structural mismatch" claim 的证据链是否完整（gradient analysis → oracle F1 → PPL gap）

### 2. 实验设计与公平性
- KL vs BCE 对比的公平性：是否存在 pipeline 差异（loss 以外的变量未控制）
- Iso-compute analysis 是否充分（2700 steps BCE vs 1000 steps KL）
- 统计效力：3-seed 评估的充分性，报告的 std=0.07 是否覆盖关键结论
- Cross-architecture validation（仅 LLaMA-8B + Mistral-7B）的范围是否支撑 claim
- Downstream evaluation：MMLU 25.27% 与 PPL 改善的 disconnect 是否充分解释

### 3. 消融完整性
- Table 3 ablation：是否所有关键设计选择都被隔离
- Regime analysis（3 regimes, 6 data points）：证据是否支撑 "regime" 级别的 claim
- Gap decomposition（53% predictor error vs 47% allocation loss）的方法论

### 4. 技术细节
- Training setup（WikiText-103, 1000 steps, seq_len=2048, batch=4）是否 standard/sufficient
- Inference protocol：predictor-TEAL 与 vanilla TEAL 的精确对应关系
- Appendix 数据与正文 claim 的一致性

请按 ACL reviewer guidelines 格式输出完整审稿报告：Summary, Strengths, Weaknesses (逐条编号，标注 severity: critical/warning/info), Questions, Missing References, Overall Assessment (score + confidence)。

**审查标准**：像顶会最严格的审稿人一样评估。不留情面。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 160 · 2026-05-17T09:05:27.199150+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 161 · 2026-05-17T09:05:28.004650+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 805
}
```

</details>

---


### Tool call

_source line 162 · 2026-05-17T09:05:28.155749+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebFetch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 163 · 2026-05-17T09:05:28.156202+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 164 · 2026-05-17T09:05:33.528272+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 165 · 2026-05-17T09:05:35.035158+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ -name \"*.tex\" -o -name \"*.bib\" | sort",
  "description": "List all tex and bib files in paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ -name \"*.tex\" -o -name \"*.bib\" | sort",
    "description": "List all tex and bib files in paper directory"
  }
}
```

</details>

---


### Tool result

_source line 166 · 2026-05-17T09:05:35.286391+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 167 · 2026-05-17T09:05:35.286813+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/main.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/main.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 168 · 2026-05-17T09:05:35.337328+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 169 · 2026-05-17T09:05:42.178309+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

I found comprehensive information about the ACL ARR 2026 reviewer guidelines, review form criteria, and scoring. Here's what I found:

## Three-Point Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: s
…[truncated 1705 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8650
}
```

</details>

---


### Tool call

_source line 170 · 2026-05-17T09:05:46.846183+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the COMPLETE review form with all scoring dimensions, their scales, descriptions, and any guidelines. I need: (1) all scoring fields and their numeric scales, (2) what each score level means, (3) all free-text fields reviewers must fill, (4) any special instructions about soundness vs excitement vs overall."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the COMPLETE review form with all scoring dimensions, their scales, descriptions, and any guidelines. I need: (1) all scoring fields and their numeric scales, (2) what each score level means, (3) all free-text fields reviewers must fill, (4) any special instructions about soundness vs excitement vs overall."
  }
}
```

</details>

---


### Tool call

_source line 171 · 2026-05-17T09:05:47.751111+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
  "pages": "1-10",
  "dpi": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
    "pages": "1-10",
    "dpi": "200"
  }
}
```

</details>

---


### Tool result

_source line 172 · 2026-05-17T09:06:01.309719+00:00_

# ACL Rolling Review Form - Complete Structure

## Scoring Dimensions

### 1. **Reviewer Confidence** (1-5 scale)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar"
- **4**: Quite sure with minimal likelihood of missing impactful details
- **3**: Pretty sure but acknowledges possible oversights in technical verification
- **2**: Willing to defend evaluation despite fairly likely missed details
- **1**: Outside expertise area or paper highly difficult to understand

### 2. **Soundness** (1-5 scale with half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type"
- **4**: Strong with sufficient support; optional extra experiments
- **3**: Acceptable with adequate main claim support; minor details may need development
- **2**: Poor; main claims lack sufficient support with major technical issues
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

### 3. **Excitement** (1-5 scale with half-point increments)
Evaluates subjective appeal including conceptual breakthroughs, community impact, and personal relevance:
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation"
- **4**: Exciting; would mention to others or prioritize attending
- **3**: Interesting; might mention points or attend if available
- **2**: Potentially interesting to some despite limited personal resonance
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others"

### 4. **Overall Assessment** (1-5 scale with half-point increments)
- **5**: "Consider for Award: I think this paper could be considered for an outstanding paper award"
- **4.5**: Borderline Award consideration
- **4**: Conference acceptance recommendation
- **3.5**: Borderline Conference
- **3**: Suitable for Findings track
- **2.5**: Borderline Findings
- **2**: Requires substantial revisions for next cycle resubmission

…[truncated 2601 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 14463
}
```

</details>

---


### Tool result

_source line 173 · 2026-05-17T09:06:07.577145+00:00_

Error: result (9,005,051 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/13c46f03-a32a-4aeb-a35a-1ae28706eae8/tool-results/mcp-agent-ml-research-pdf_to_images-1779008766646.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/13c46f03-a32a-4aeb-a35a-1ae28706eae8/tool-results/mcp-agent-ml-research-pdf_to_images-1779008766646.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 19826
}
```

</details>

---


### Tool call

_source line 174 · 2026-05-17T09:06:11.293269+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 175 · 2026-05-17T09:06:11.745176+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	
17	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
18	
19	\author{Anonymous}
20	
21	\begin{document}
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
32	\input{conclusion}
33	\input{limitations}
34	\input{ethics}
35	
36	\bibliography{references}
37	
38	\input{appendix}
39	
40	\end{document}
41	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 176 · 2026-05-17T09:06:11.745692+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 177 · 2026-05-17T09:06:12.248435+00:00_

1	We study whether end-to-end KL distillation can replace per-neuron classification for activation sparsity prediction in SwiGLU LLMs.
2	Existing predictors trained with binary cross-entropy (BCE) optimize each neuron independently, but inference allocates sparsity budgets via global top-$k$ across all layers.
3	We show this creates a structural mismatch: BCE achieves higher oracle F1 (0.613 vs.\ 0.540) yet produces 91\% worse perplexity, because per-neuron accuracy is a misaligned proxy for output-distribution preservation.
4	A lightweight predictor (75.9M params, $<$1\% of the base model) trained with forward KL divergence and Gumbel-Sigmoid relaxation resolves this mismatch by coupling all neurons through the output distribution.
5	On LLaMA-3.1-8B at 50\% sparsity, the KL predictor achieves PPL 11.79 vs.\ 23.31 for magnitude-based TEAL (49\% reduction), with consistent improvements on Mistral-7B-v0.3 at the 7--8B scale.
6	However, perplexity gains do not uniformly transfer to downstream tasks: global allocation starves late layers (L31 retention 28.4\%), degrading MMLU to 25.27\%, while uniform allocation recovers it to 40.61\%, comparable to TEAL's 38.61\%.
7	We identify three sparsity regimes (budget-surplus, budget-constrained, capacity-limited) that govern this allocation-quality tradeoff on 7--8B models and provide gradient coupling analysis explaining why distributional objectives outperform decomposed per-neuron losses for global budget allocation.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 178 · 2026-05-17T09:06:12.248801+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 179 · 2026-05-17T09:06:12.700543+00:00_

1	\section{Introduction}
2	
3	SwiGLU feed-forward networks~\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they universally rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: TEAL's top-$k$ mechanism~\cite{liu2025teal} ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	
8	We provide this analysis.
9	The gradient of BCE with respect to neuron $j$'s score is $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$, a function of $j$ alone, independent of every other neuron.
10	Under KL divergence, the gradient for neuron $j$ in layer $\ell$ factors as:
11	\begin{equation*}
12	\frac{\partial \mathcal{L}_{\text{KL}}}{\partial s_j^{(\ell)}} = \frac{\partial \mathcal{L}_{\text{KL}}}{\partial \mathbf{z}} \cdot \frac{\partial \mathbf{z}}{\partial \mathbf{h}^{(\ell)}} \cdot \frac{\partial \mathbf{h}^{(\ell)}}{\partial \tilde{m}_j^{(\ell)}} \cdot \frac{\partial \tilde{m}_j^{(\ell)}}{\partial s_j^{(\ell)}},
13	\end{equation*}
14	where the Jacobian $\partial \mathbf{z} / \partial \mathbf{h}^{(\ell)}$ propagates through all downstream layers, coupling each neuron's gradient to every other neuron's mask state.
15	This structural difference predicts that KL should outperform BCE specifically under global allocation, and the prediction is confirmed empirically: BCE achieves higher oracle F1 (0.613 vs.\ 0.540) yet produces 91\% worse perplexity, because per-neuron magnitude accuracy is a misaligned proxy for output-distribution preserv
…[truncated 2412 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 180 · 2026-05-17T09:06:12.701158+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-17T09:06:13.203070+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models.
5	The method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass, eliminating the need for auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{h}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importance scores from the pre-FFN hidden state $\mathbf{h}$.
26
…[truncated 14119 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 182 · 2026-05-17T09:06:13.203449+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 183 · 2026-05-17T09:06:13.605247+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4, using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $5 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly; (2) \textbf{BCE predictor}, trained with per-neuron binary cross-entropy loss for 1000 and 2700 steps; (3) \textbf{Uniform allocation}, which distributes the sparsity budget equally across layers; and (4) \textbf{WINA}~\cite{liu2025teal}, an importance-weighted variant.
23	
24	
25
…[truncated 14147 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 184 · 2026-05-17T09:06:13.605633+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 185 · 2026-05-17T09:06:14.610779+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude, achieving 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking.
6	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
7	
8	\paragraph{Predictor-Based Contextual Sparsity.}
9	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
10	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision, providing intermediate coupling within each layer but no end-to-end gradient signal.
11	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
12	PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.
13	MaskLLM~\cite{fang2024maskllm} also employs learnable masks with Gumbel relaxation and frozen weights, but targets N:M semi-structured \emph{weight} sparsity (2:4 patterns) via per-group categorical selection (Gumbel-Softmax), producing fixed masks independent of input tokens.
14	Both share the principle of frozen weights + learnable masks + KL training, but solve distinct optimization problems: MaskLLM finds optimal static N:M patterns within fixed groups, while we predict dynamic per-token masks under a global budget constraint.
15	The structural mismatch we identify (per-neuron gradient decomposition vs.\ global top-$k$) does not arise in MaskLLM's per-group categorical setting, where N:M patterns
…[truncated 2398 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-17T09:06:14.611199+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 187 · 2026-05-17T09:06:15.063884+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that KL distillation resolves the structural mismatch between per-neuron BCE training and global top-$k$ inference allocation in SwiGLU sparsity prediction.
5	The coupled gradient signal enables a lightweight predictor (75.9M params, $<$1\% of base) to achieve PPL 11.79 at 50\% sparsity vs.\ 23.31 for TEAL, with consistent improvements on both LLaMA-3.1-8B and Mistral-7B-v0.3 (within 7\% ratio consistency at $\leq$50\% sparsity).
6	Regime analysis reveals that allocation strategy, not predictor quality, is the primary bottleneck for downstream tasks: global top-$k$ starves late layers, degrading MMLU, while uniform allocation recovers performance comparable to TEAL.
7	
8	Two directions remain open.
9	First, allocation-aware training (jointly optimizing the predictor and per-layer budgets) could address late-layer starvation without sacrificing the perplexity advantages of global selection.
10	Second, evaluating at larger scales (13B--70B) and with structured sparsity patterns that enable wall-clock speedup would determine the practical deployment value of distributional training for sparsity prediction.
11	
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 188 · 2026-05-17T09:06:15.064244+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 189 · 2026-05-17T09:06:15.516619+00:00_

1	\section*{Limitations}
2	
3	Our primary evaluation uses WikiText-2 perplexity, and downstream benchmarks reveal that perplexity is a poor proxy for reasoning ability at moderate sparsity: 40\% sparsity achieves PPL 8.36 but MMLU already degrades, motivating 30\% as the recommended operating point for downstream fidelity.
4	Training requires 1000 steps on WikiText-103 ($\sim$17 minutes on A6000), but a separate predictor must be trained for each sparsity target.
5	All experiments use 7--8B parameter models (LLaMA-3.1-8B, Mistral-7B-v0.3); scaling behavior to 13B or 70B models remains untested.
6	While we motivate our work with inference speedup potential, actual wall-clock acceleration depends on sparse kernel implementations (e.g., Triton, cuSPARSE) and hardware-specific memory access patterns; this work focuses on prediction quality rather than systems optimization.
7	Future directions include N:M structured sparsity for hardware-native acceleration, scaling to 13B+ models, and training a single predictor that serves multiple sparsity targets simultaneously.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 190 · 2026-05-17T09:06:15.567462+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 191 · 2026-05-17T09:06:15.768481+00:00_

1	\section*{Ethics Statement}
2	
3	This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, MMLU, GSM8K).
4	No new data collection, annotation, or human subjects are involved.
5	The method does not alter model outputs beyond the sparsity-induced degradation we analyze; it introduces no new generation capabilities or safety risks beyond those inherent in the base models.
6	Compute requirements are modest (1000 training steps, $\sim$17 minutes on a single GPU), presenting minimal environmental concern relative to the pretrained models we evaluate on.
7	We release no model weights or user-facing systems; our contribution is analytical (understanding KL distillation for sparsity) rather than deployment-oriented.
8	
9	\section*{Responsible NLP Research Checklist}
10	
11	\paragraph{A. Limitations and Risks.}
12	\begin{itemize}[nosep,leftmargin=*]
13	\item[\textbf{A1.}] Limitations are discussed in the Limitations section. Key limitations: evaluation limited to 7--8B models; perplexity is an imperfect proxy for downstream quality; wall-clock speedup requires sparse kernel support not implemented here.
14	\item[\textbf{A2.}] No foreseeable risks specific to this work beyond those inherent in the base language models. The method does not enable new capabilities or applications.
15	\end{itemize}
16	
17	\paragraph{B. Scientific Artifacts.}
18	\begin{itemize}[nosep,leftmargin=*]
19	\item[\textbf{B1.}] Yes. All models (LLaMA-3.1-8B~\cite{grattafiori2024llama3}, Mistral-7B-v0.3~\cite{jiang2023mistral}), datasets (WikiText~\cite{merity2017pointer}, C4~\cite{raffel2020c4}), and methods (TEAL~\cite{liu2025teal}, SPON~\cite{xu2026spon}) are cited with original references.
20	\item[\textbf{B2.}] LLaMA-3.1 is released under the Llama 3.1 Community License; Mistral-7B under Apache 2.0. WikiText and C4 are public
…[truncated 1802 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 192 · 2026-05-17T09:06:15.769082+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 193 · 2026-05-17T09:06:15.819752+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling), confirming that KL distillation provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overh
…[truncated 8907 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 194 · 2026-05-17T09:06:21.799826+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
  "offset": "192"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
    "offset": "192"
  }
}
```

</details>

---


### Tool result

_source line 195 · 2026-05-17T09:06:22.251661+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (192). The file has 192 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 196 · 2026-05-17T09:06:22.352437+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 197 · 2026-05-17T09:06:22.754171+00:00_

1	% =============================================================================
2	% Direction 1: KL distillation for structured/activation sparsity
3	% =============================================================================
4	
5	@inproceedings{fang2024maskllm,
6	  title = {MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models},
7	  author = {Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff Pool and Jan Kautz and Pavlo Molchanov and Xinchao Wang},
8	  year = {2024},
9	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
10	  url = {https://arxiv.org/abs/2409.17481},
11	}
12	
13	@inproceedings{xu2026spon,
14	  title = {Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models},
15	  author = {Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma},
16	  year = {2025},
17	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
18	  url = {https://arxiv.org/abs/2512.12744},
19	}
20	
21	@inproceedings{muralidharan2024minitron,
22	  title = {Compact Language Models via Pruning and Knowledge Distillation},
23	  author = {Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marcin Chochowski and Mostofa Patwary and Mohammad Shoeybi and Bryan Catanzaro and Jan Kautz and Pavlo Molchanov},
24	  year = {2024},
25	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
26	  url = {https://arxiv.org/abs/2407.14679},
27	}
28	
29	
30	% =============================================================================
31	% Direction 3: SPON and learnable bias correction for sparsity
32	% =============================================================================
33	
34	@article{gautam2026fastforward,
35	  title = {Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity},
36	  author = {Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott and Naras
…[truncated 12601 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 198 · 2026-05-17T09:06:24.509868+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract ALL specific guidance for reviewers: what to look for in soundness, what counts as exciting, how to calibrate scores, what are common pitfalls. Include any specific criteria for experimental papers, reproducibility requirements, and how novelty should be assessed."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract ALL specific guidance for reviewers: what to look for in soundness, what counts as exciting, how to calibrate scores, what are common pitfalls. Include any specific criteria for experimental papers, reproducibility requirements, and how novelty should be assessed."
  }
}
```

</details>

---


### Tool result

_source line 199 · 2026-05-17T09:06:33.997540+00:00_

# ARR Reviewer Guidance: Soundness, Excitement, and Scoring

## Soundness Assessment

**What to evaluate:**
- Technical correctness and validity of methodology
- Appropriateness of research design for answering the stated question
- Clarity of assumptions and completeness of proofs
- Sound argumentation throughout the paper

Reviewers must justify low soundness scores with specific textual evidence. "If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation."

## Excitement (Subjective Interest)

Excitement reflects personal taste and interest independent of soundness. A paper can be technically sound but less personally exciting to a reviewer. Conversely, a reviewer may find work exciting while acknowledging limitations.

## Common Pitfalls to Avoid

**Cognitive Biases (Heuristics H1-H17):**

- **H1-H2:** Avoid dismissing findings as "obvious" or rejecting results contradicting expectations
- **H3:** Novelty requires evidence; provide references if claiming prior work exists
- **H5:** SOTA results aren't necessary—evaluate contributions holistically (efficiency, fairness, interpretability)
- **H6:** Negative results deserve publication to counter publication bias
- **H7:** Simpler solutions are preferable when solving the problem
- **H13:** Only require experiments that directly support the authors' claims
- **H14:** Closed-source model comparisons unnecessary unless they directly address research questions
- **H16:** Acknowledge limitations without treating them as rejection grounds

## Reproducibility Requirements

Papers must provide sufficient detail for replication: hyperparameters, methodological steps, code availability plans. The review should assess whether enough information exists for someone to reproduce experiments, though reviewers aren't obligated to run code.

## Experimental Paper Criteria

**Critical checks (codes M1-R5):**
- **M2:** Reproducibility details present?
- **R1:** Stat
…[truncated 601 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 9487
}
```

</details>

---


### Tool call

_source line 200 · 2026-05-17T09:08:15.447886+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool call

_source line 201 · 2026-05-17T09:08:16.403267+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
  "pages": "1-3",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
    "pages": "1-3",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 202 · 2026-05-17T09:19:56.098869+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 32, \"total_citations\": 67, \"unique_cited_keys\": 32, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 22, \"online_not_found\": 0, \"online_mismatch\": 1}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"fang2024maskllm\", \"type\": \"inproceedings\", \"title\": \"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models\", \"authors\": \"Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff P...\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"xu2026spon\", \"type\": \"inproceedings\", \"title\": \"Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models\", \"authors\": \"Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Machine Learning (ICML)\"}, {\"key\": \"muralidharan2024minitron\", \"type\": \"inproceedings\", \"title\": \"Compact Language Models via Pruning and Knowledge Distillation\", \"authors\": \"Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marci...\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"gautam2026fastforward\", \"type\": \"article\", \"title\": \"Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity\", \"authors\": \"Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott ...\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2602.00397\"}, {\"key\": \"liu2025teal\", \"type\": \"inproceedings\", \"title\": \"Training-Free Activation Sparsity in Large Language Models\", \"authors\": \"James Liu and Pragaash Ponnusamy and Tianle Cai and Han Guo and Yoon Kim and Ben...\", \"year
…[truncated 25344 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 700650
}
```

</details>

---


### Tool result

_source line 203 · 2026-05-17T09:19:57.119867+00:00_

Error: result (2,040,577 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/13c46f03-a32a-4aeb-a35a-1ae28706eae8/tool-results/mcp-agent-ml-research-pdf_to_images-1779009597040.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/13c46f03-a32a-4aeb-a35a-1ae28706eae8/tool-results/mcp-agent-ml-research-pdf_to_images-1779009597040.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 700716
}
```

</details>

---


### Tool call

_source line 204 · 2026-05-17T09:20:07.617229+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/13c46f03-a32a-4aeb-a35a-1ae28706eae8/tool-results/mcp-agent-ml-research-pdf_to_images-1779009597040.txt | python3 -c \"import json,sys; d=json.loads(sys.stdin.read()); r=json.loads(d['result']); print(len(r.get('pages',r.get('images',[]))),'pages'); [print(p.get('page','?'), len(p.get('base64','')[:10])) for p in r.get('pages',r.get('images',[]))]\" 2>/dev/null || echo \"trying alternate parse\"; cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/13c46f03-a32a-4aeb-a35a-1ae28706eae8/tool-results/mcp-agent-ml-research-pdf_to_images-1779009597040.txt | python3 -c \"import json,sys; d=json.loads(sys.stdin.read()); print(type(d)); print(list(d.keys())[:5] if isinstance(d,dict) else 'not dict')\" 2>/dev/null",
  "description": "Parse PDF images output structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/13c46f03-a32a-4aeb-a35a-1ae28706eae8/tool-results/mcp-agent-ml-research-pdf_to_images-1779009597040.txt | python3 -c \"import json,sys; d=json.loads(sys.stdin.read()); r=json.loads(d['result']); print(len(r.get('pages',r.get('images',[]))),'pages'); [print(p.get('page','?'), len(p.get('base64','')[:10])) for p in r.get('pages',r.get('images',[]))]\" 2>/dev/null || echo \"trying alternate parse\"; cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/13c46f03-a32a-4aeb-a35a-1ae28706eae8/tool-results/mcp-agent-ml-research-pdf_to_images-1779009597040.txt | python3 -c \"import json,sys; d=json.loads(sys.stdin.read()); print(type(d)); print(list(d.keys())[:5] if isinstance(d,dict) else 'not dict')\" 2>/dev/null",
    "description": "Parse PDF images output structure"
  }
}
```

</details>

---


### Tool result

_source line 205 · 2026-05-17T09:20:07.819349+00:00_

0 pages
&lt;class 'dict'>
['result']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 206 · 2026-05-17T09:20:14.198058+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/13c46f03-a32a-4aeb-a35a-1ae28706eae8/tool-results/mcp-agent-ml-research-pdf_to_images-1779009597040.txt') as f:\n    d = json.load(f)\nr = d['result']\nif isinstance(r, str):\n    r2 = json.loads(r)\n    print(type(r2), list(r2.keys())[:10] if isinstance(r2, dict) else 'not dict')\n    if 'pages' in r2:\n        for p in r2['pages']:\n            print('Page', p.get('page_number','?'), 'file:', p.get('file_path','N/A')[:80])\n    elif 'images' in r2:\n        for p in r2['images']:\n            print('Image', p.get('page','?'), 'file:', p.get('path','N/A')[:80])\n\"\n",
  "description": "Parse PDF images paths"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/13c46f03-a32a-4aeb-a35a-1ae28706eae8/tool-results/mcp-agent-ml-research-pdf_to_images-1779009597040.txt') as f:\n    d = json.load(f)\nr = d['result']\nif isinstance(r, str):\n    r2 = json.loads(r)\n    print(type(r2), list(r2.keys())[:10] if isinstance(r2, dict) else 'not dict')\n    if 'pages' in r2:\n        for p in r2['pages']:\n            print('Page', p.get('page_number','?'), 'file:', p.get('file_path','N/A')[:80])\n    elif 'images' in r2:\n        for p in r2['images']:\n            print('Image', p.get('page','?'), 'file:', p.get('path','N/A')[:80])\n\"\n",
    "description": "Parse PDF images paths"
  }
}
```

</details>

---


### Tool result

_source line 207 · 2026-05-17T09:20:14.298894+00:00_

&lt;class 'dict'> ['success', 'data', 'error', 'metadata']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 208 · 2026-05-17T09:20:20.272224+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/13c46f03-a32a-4aeb-a35a-1ae28706eae8/tool-results/mcp-agent-ml-research-pdf_to_images-1779009597040.txt') as f:\n    d = json.load(f)\nr = json.loads(d['result'])\ndata = r['data']\nprint(type(data), list(data.keys())[:10] if isinstance(data, dict) else len(data))\nif isinstance(data, list):\n    for item in data:\n        print(item.get('page_number','?'), item.get('file_path','N/A')[:100])\nelif isinstance(data, dict):\n    for k,v in data.items():\n        if isinstance(v, list):\n            print(k, len(v))\n            for item in v[:3]:\n                if isinstance(item, dict):\n                    print('  ', {kk:str(vv)[:60] for kk,vv in item.items() if kk != 'base64'})\n        else:\n            print(k, str(v)[:100])\n\"\n",
  "description": "Parse PDF image data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/13c46f03-a32a-4aeb-a35a-1ae28706eae8/tool-results/mcp-agent-ml-research-pdf_to_images-1779009597040.txt') as f:\n    d = json.load(f)\nr = json.loads(d['result'])\ndata = r['data']\nprint(type(data), list(data.keys())[:10] if isinstance(data, dict) else len(data))\nif isinstance(data, list):\n    for item in data:\n        print(item.get('page_number','?'), item.get('file_path','N/A')[:100])\nelif isinstance(data, dict):\n    for k,v in data.items():\n        if isinstance(v, list):\n            print(k, len(v))\n            for item in v[:3]:\n                if isinstance(item, dict):\n                    print('  ', {kk:str(vv)[:60] for kk,vv in item.items() if kk != 'base64'})\n        else:\n            print(k, str(v)[:100])\n\"\n",
    "description": "Parse PDF image data structure"
  }
}
```

</details>

---


### Tool result

_source line 209 · 2026-05-17T09:20:20.373193+00:00_

&lt;class 'dict'> ['images', 'total_pages', 'rendered_pages', 'dpi', 'output_dir']
images 3
   {'page': '1', 'path': '/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/di', 'width': '1241', 'height': '1754', 'size_kb': '449.6'}
   {'page': '2', 'path': '/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/di', 'width': '1241', 'height': '1754', 'size_kb': '556.3'}
   {'page': '3', 'path': '/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/di', 'width': '1241', 'height': '1754', 'size_kb': '488.0'}
total_pages 13
rendered_pages 3
dpi 150
output_dir /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 210 · 2026-05-17T09:20:23.184481+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/page_001.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/page_001.png"
  }
}
```

</details>

---


### Tool result

_source line 211 · 2026-05-17T09:20:23.285382+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 212 · 2026-05-17T09:20:23.486547+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/page_002.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/page_002.png"
  }
}
```

</details>

---


### Tool result

_source line 213 · 2026-05-17T09:20:23.988882+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 214 · 2026-05-17T09:20:24.240562+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/page_003.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/page_003.png"
  }
}
```

</details>

---


### Tool result

_source line 215 · 2026-05-17T09:20:24.291161+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 216 · 2026-05-17T09:20:27.353513+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/",
  "description": "List PDF image files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/",
    "description": "List PDF image files"
  }
}
```

</details>

---


### Tool result

_source line 217 · 2026-05-17T09:20:27.404219+00:00_

main_p1.png
main_p10.png
main_p11.png
main_p12.png
main_p2.png
main_p3.png
main_p4.png
main_p5.png
main_p6.png
main_p7.png
main_p8.png
main_p9.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 218 · 2026-05-17T09:20:30.467891+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 219 · 2026-05-17T09:20:30.821201+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 220 · 2026-05-17T09:20:31.377212+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 221 · 2026-05-17T09:20:32.385083+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1917
}
```

</details>

---


### Tool call

_source line 222 · 2026-05-17T09:20:32.387512+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 223 · 2026-05-17T09:20:32.438176+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 224 · 2026-05-17T09:20:34.301536+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3480
}
```

</details>

---


### Tool result

_source line 225 · 2026-05-17T09:20:35.613366+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4236
}
```

</details>

---


### Tool result

_source line 226 · 2026-05-17T09:20:36.468116+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4080
}
```

</details>

---


### Tool result

_source line 227 · 2026-05-17T09:20:36.519339+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4081
}
```

</details>

---


### Tool call

_source line 228 · 2026-05-17T09:20:40.790094+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 229 · 2026-05-17T09:20:41.192127+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 230 · 2026-05-17T09:20:42.096854+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 231 · 2026-05-17T09:20:42.900886+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 232 · 2026-05-17T09:20:42.901438+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 233 · 2026-05-17T09:20:44.213962+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3423
}
```

</details>

---


### Tool result

_source line 234 · 2026-05-17T09:20:45.836600+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4644
}
```

</details>

---


### Tool result

_source line 235 · 2026-05-17T09:20:47.399920+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 5303
}
```

</details>

---


### Tool result

_source line 236 · 2026-05-17T09:20:47.402127+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4501
}
```

</details>

---


### Tool result

_source line 237 · 2026-05-17T09:20:47.403244+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4501
}
```

</details>

---


### Tool call

_source line 238 · 2026-05-17T09:20:51.633228+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/ | sort -V",
  "description": "List all PDF pages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/ | sort -V",
    "description": "List all PDF pages"
  }
}
```

</details>

---


### Tool result

_source line 239 · 2026-05-17T09:20:51.734113+00:00_

main_p1.png
main_p2.png
main_p3.png
main_p4.png
main_p5.png
main_p6.png
main_p7.png
main_p8.png
main_p9.png
main_p10.png
main_p11.png
main_p12.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 240 · 2026-05-17T09:20:58.061730+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "22\\.51",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "22\\.51",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 241 · 2026-05-17T09:20:58.564209+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex:66:The failure is structural, not due to architectural or compute differences: both predictors use identical architectures and TEAL allocation, yet BCE achieves +13pp oracle F1 (0.613 vs.\ 0.540) with 91\% worse PPL (22.51 vs.\ 11.79). KL's near-random precision (0.51) confirms it learns a mask optimized for distributional fidelity rather than magnitude matching. % exp_id: f1_oracle_analysis, bce_isocompute_s42

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 242 · 2026-05-17T09:20:58.715109+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "91\\\\%",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "91\\\\%",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 243 · 2026-05-17T09:20:58.765682+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex:66:The failure is structural, not due to architectural or compute differences: both predictors use identical architectures and TEAL allocation, yet BCE achieves +13pp oracle F1 (0.613 vs.\ 0.540) with 91\% worse PPL (22.51 vs.\ 11.79). KL's near-random precision (0.51) confirms it learns a mask optimized for distributional fidelity rather than magnitude matching. % exp_id: f1_oracle_analysis, bce_isocompute_s42
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex:3:We show this creates a structural mismatch: BCE achieves higher oracle F1 (0.613 vs.\ 0.540) yet produces 91\% worse perplexity, because per-neuron accuracy is a misaligned proxy for output-distribution preservation.
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex:15:This structural difference predicts that KL should outperform BCE specifically under global allocation, and the prediction is confirmed empirically: BCE achieves higher oracle F1 (0.613 vs.\ 0.540) yet produces 91\% worse perplexity, because per-neuron magnitude accuracy is a misaligned proxy for output-distribution preservation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 244 · 2026-05-17T09:23:49.491944+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 审稿报告：方法严谨性 + 实验设计\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审稿标准**: ACL Rolling Review official review form (2025 updated, three-point scoring)\n\n---\n\n## Paper Summary\n\n本文研究用 forward KL divergence 替代 binary cross-entropy (BCE) 训练 SwiGLU LLM 的 contextual sparsity predictor。核心观察是 BCE 梯度按 neuron 独立分解，与 TEAL 推理时 global top-k 分配机制存在结构性不匹配。作者训练一个轻量 predictor (75.9M params)，通过 Gumbel-Sigmoid relaxation 实现端到端 KL 蒸馏，在 LLaMA-3.1-8B 50% sparsity 下 PPL 11.79 vs TEAL 23.31 (49% 改善)。论文同时分析了 global vs uniform allocation 在不同 sparsity 水平下的 downstream 表现，提出了 three-regime 框架，并给出 2D taxonomy 分类先前方法。\n\n---\n\n## 总体评分\n\n**Overall**: 2.5 / 5 (Borderline Findings)\n**一句话总结**: 问题定义清晰，梯度分析有启发性，但关键数据不一致、实验对比存在 pipeline 混淆变量、headline method 在最重要的 downstream task 上退化至随机水平，整体证据链不足以支撑 claims 的强度。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2.5 / 5 | 梯度分析数学正确但属 chain rule 的标准应用；BCE vs KL 对比存在严重 pipeline 混淆；22.51 PPL 幽灵数据；regime claim 证据密度不足 |\n| Excitement | 2.5 / 5 | 问题本身有意义（per-neuron vs global allocation mismatch），但实际结果令人失望：无 wall-clock 加速、MMLU 退化至 random、仅 7-8B scale |\n| Overall | 2.5 / 5 | 分析贡献有价值但实验缺陷削弱了可信度；需要修复数据一致性、补充 controlled comparison、调低 claim 强度 |\n| Reproducibility | 3.5 / 5 | 大部分超参和实验细节已报告；但主表结果为单 seed、22.51 数字不可追溯 |\n| Reviewer Confidence | 4 / 5 | 熟悉 activation sparsity、KD、Gumbel relaxation 领域 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **数据完整性：PPL 22.51 幽灵数字**\n- 具体位置：§4.3 (experiments.tex:66), Abstract, Introduction\n- 问题：§4.3 写到 \"BCE achieves +13pp oracle F1 (0.613 vs. 0.540) with 91% worse PPL (22.51 vs. 11.79)\"。然而 22.51 这个数字**不出现在论文任何表格中**。Table 2 中 BCE (2700 steps) = 27.97, BCE+Compensation = 25.44。如果 22.51 是 1000-step BCE 的结果，它需要在 Table 2 或 Table 3 中显示。数学验证：22.51/11.79 = 1.909 ≈ \"91% worse\"，但如果用 Table 2 的 27.97，则是 137% worse。Abstract 和 Introduction 反复使用 \"91% worse perplexity\" 这个数字作为核心 claim，但该 claim 所依赖的 baseline 数据无法从论文本身验证。\n- 为什么影响接收：论文最核心的 quantitative claim 之一不可追溯。审稿人无法从提交材料中 verify 该数字的来源。这不是 typo，是 **数据溯源链断裂**。\n- 建议：在 Table 2 或 Table 3 中补充 BCE 1000-step 的 PPL 数据行，或者用 Table 中已有的数字（27.97）重新计算百分比。\n\n---\n\n**N2** [critical] **Headline method 在最重要 downstream task 上退化至随机水平**\n- 具体位置：Table 2, Table 5, §4.5\n- 问题：论文主推方法 \"KL global (Ours)\" 在 30% sparsity 下 MMLU = 25.27%，而 4-choice random baseline = 25%。同一设定下 TEAL vanilla = 38.61%。即论文的核心方法在最广泛使用的知识评测上**比 baseline 差 13.3pp**，且约等于随机。论文的解释是 global top-k allocation 导致 late-layer starvation（L31 retention 28.4%），并提出 uniform allocation 作为修复（恢复至 40.61%）。但这实质上承认：**论文提出的 KL + TEAL global 组合在 downstream tasks 上不可用**，实际可用配置是 KL + uniform allocation——但 uniform allocation 本身消除了 global top-k 的概念，也就是说论文花大量篇幅分析的 \"global allocation quality\" 在实践中需要被绕过。\n- 为什么影响接收：论文的 framing 围绕 \"KL optimizes for global allocation quality\" (Abstract, §1, §3.5)，但实验结论表明 global allocation 在实践中损害 downstream performance。这是一个 **narrative vs evidence 的根本矛盾**。\n- 建议：(1) 重新定位主推方法为 KL + uniform，将 global 作为分析对象而非推荐配置；(2) 在 Table 2 中将 KL uniform 标为 Ours (recommended)；(3) 调整 Abstract/Introduction 的 framing，诚实反映 \"global allocation reveals a quality advantage in PPL but not downstream tasks\"。\n\n---\n\n**N3** [critical] **BCE vs KL 对比存在严重的 pipeline 混淆变量**\n- 具体位置：§4.3, §4.4, Table 3\n- 问题：KL 和 BCE 使用了完全不同的训练 pipeline：\n  - KL: Gumbel-Sigmoid soft masks + adaptive penalty controller + forward KL loss\n  - BCE: hard masks + compensation network (optional) + per-neuron BCE loss\n  \n  论文 claim \"the failure is structural, not due to architectural or compute differences\" (§4.3)，但这个 claim 无法从现有实验中得出，因为 loss function 和 relaxation method 是 **jointly varied** 的。Table 3 的 isolation 实验 \"BCE + Gumbel + Penalty (no KL)\" = 38.02（比 vanilla BCE 的 27.97 更差）恰好说明了这个问题：Gumbel + penalty 机制与 BCE loss 互不兼容，无法简单分离。\n\n  更公平的对比需要：(a) BCE + Gumbel + KL-style global objective (e.g., MSE on hidden states) 作为中间点；(b) KL + hard masks (STE) + no penalty 作为对照。Table 3 中 \"Forward KL + STE\" = 15.77 提供了部分信息，但仍然混杂了 relaxation 和 penalty 两个变量。\n\n  论文称 \"loss effect (ΔPPL=26.23) is 6.6× the relaxation effect (ΔPPL=3.98)\"，但 loss effect 的计算用了 BCE+Gumbel+Penalty=38.02 vs KL+Gumbel=11.79，而不是 controlled comparison。BCE+Gumbel+Penalty 之所以差，可能是因为 penalty controller 破坏了 BCE 的 per-neuron convergence（论文自己也指出 \"the penalty interferes with per-neuron optimization\"），而非 KL 本身有多好。\n- 为什么影响接收：无法从实验中 cleanly 区分 \"KL loss 的贡献\" vs \"Gumbel relaxation + penalty controller 对 KL 恰好有效的贡献\"。核心 claim \"distributional objectives outperform decomposed per-neuron losses\" 在 controlled experiment 意义上未被证明。\n- 建议：(1) 补充 MSE (intermediate coupling) ablation，对应 taxonomy 中的 intermediate 列；(2) 补充 per-layer KL (解耦 cross-layer coupling) 作为 controlled variant；(3) 明确 claim 是关于 \"KL+Gumbel+Penalty 组合\" 而非单独的 loss function。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **\"Three regimes\" 从 3 个数据点归纳——证据密度不足**\n- 具体位置：§4.5, Table 5\n- 问题：论文定义了 budget-surplus (≤30%), budget-constrained (~40%), capacity-limited (≥50%) 三个 regime。但整个分析基于 3 个 sparsity level（30%, 40%, 50%）× 2 个 allocation = 6 个数据点。每个 \"regime\" 实际上只有 1 个数据点。regime boundary 的精确位置（30%→40% 之间、40%→50% 之间）完全没有被定位。论文说 \"this boundary is consistent on both 7-8B models\"，但 Mistral 上没有 regime analysis 数据（Table 6 只有 PPL，无 downstream）。\n- 建议：(1) 补充 35%, 45% 的数据以定位 regime transition；(2) 降低 claim 强度为 \"we observe non-monotonic behavior suggestive of distinct operating regimes\"；(3) 在 Mistral 上补充 downstream 数据。\n\n**W2** [warning] **无 wall-clock 加速——6.4% overhead**\n- 具体位置：Appendix A, Table 7\n- 问题：在 50% sparsity 下，KL predictor 的推理延迟为 126.78ms vs dense 的 119.11ms，即 **增加** 6.4% 延迟。论文在 Limitations 中承认需要 sparse kernel support，但 title (\"Contextual Sparsity Prediction\") 和 motivation (§1 第一段) 暗示了推理效率提升。一个增加延迟的 \"sparsity\" 方法在实用性上存在根本性问题。\n- 建议：在 Abstract 中明确这是一个 prediction quality 研究，而非推理加速工作。\n\n**W3** [warning] **Train-inference mismatch 未量化**\n- 具体位置：§3.3, Appendix B.1\n- 问题：训练使用 Gumbel-Sigmoid soft masks（τ=0.1 时仍是 soft），推理使用 hard top-k binary masks。这两者之间的 gap 从未被直接量化。Appendix B.1 的 temperature sensitivity 实验只测了不同 τ schedule 下的 TEAL global PPL，但没有报告 \"soft mask at τ=0.1 PPL\" vs \"hard mask PPL\"。Appendix B (Table 8) 的 per-token evaluation (9.218) 与 TEAL global (11.963) 的差距混合了 train-inference mismatch 和 allocation loss，无法分离。\n- 建议：报告训练末期 soft mask (τ=0.1) 下的 PPL 与 hard mask 下的 PPL 对比。\n\n**W4** [warning] **主表结果为单 seed**\n- 具体位置：Table 2 caption, Appendix E\n- 问题：Table 2 的所有关键对比（KL global 11.79, TEAL 23.31 等）都是 **单 seed** 结果。三 seed 评估仅在 50% uniform 配置下进行（11.92±0.07），且仅报告 PPL。核心 claim \"49% PPL reduction\" 基于单 seed。30% sparsity 下 KL global MMLU=25.27% 如果有 ±2pp 的方差就可能与 random baseline 无显著差异。Downstream metrics 的多 seed 数据仅在 Appendix E 简要提及一行。\n- 建议：至少对 Table 2 的关键行（KL global 30%、50%，TEAL 30%、50%）做 3-seed 评估。\n\n**W5** [warning] **模型规模局限**\n- 具体位置：§4 全文, Limitations\n- 问题：仅在 LLaMA-3.1-8B 和 Mistral-7B-v0.3 上测试。Title 说 \"SwiGLU LLMs\" 暗示广泛适用性。两个同规模（7-8B）模型不能代表 13B、70B 或更大模型上的表现。论文的 \"structural mismatch\" 是关于 SwiGLU 架构的一般性 claim，但实验范围不支撑。\n- 建议：在 Title 中限定为 \"7-8B SwiGLU LLMs\"，或补充至少一个 13B 模型的实验。\n\n**W6** [warning] **Adaptive Penalty Controller 无收敛保证**\n- 具体位置：§3.4, Appendix C (Table 11)\n- 问题：multiplicative schedule 是一个 heuristic，论文已在脚注中承认 \"不保证 KKT 满足\"。Appendix Table 11 显示 30% target 的 λ saturate at cap (5000) 且 deviation = 5.0%，意味着 controller 在该操作点 **没有收敛** 而是 **hit ceiling**。70% target 同样 saturate at cap (1000)。只有 40% 和 50% 真正收敛。这与正文 \"converges within 40-110 steps across all targets\" (§3.4) 的 claim 矛盾——hit cap 不等于 convergence。\n- 建议：(1) 修正 §3.4 的 convergence claim，区分 \"convergence\" 和 \"saturation at cap\"；(2) 讨论 cap saturation 对训练质量的潜在影响。\n\n---\n\n## 小问题（不影响接收）\n\n- §4.4 SPON analysis 脚注提到 \"SPON analysis uses evaluate.py; main results use the unified benchmark\"——这意味着 SPON 的 2.4% improvement (12.08→11.79) 可能是在不同 evaluation protocol 下比较的数字，不够严谨。\n- Table 5 的 40% KL uniform PPL=8.36 footnote 标注该 predictor \"uses a predictor trained at the respective sparsity target\"，但 exp_id 标注为 \"d030_kl40_uniform\"（d030 暗示 predictor 在 30% 下训练，评估在 40% 下），需要澄清。\n- Abstract 中 \"7-8B scale\" 的 claim 实际基于两个具体模型（LLaMA-8B, Mistral-7B），措辞给人更广泛验证的错觉。\n- Table 1 (taxonomy) 的 \"Static × Decomposed\" 和 \"Static × Intermediate\" 两个 cell 标为 \"---\"，但 magnitude pruning (TEAL itself) 可被视为 static × decomposed，应讨论。\n- 引用 xu2026spon 的 bib key 写成 2026 但论文年份为 2025 (ICML 2025)，虽是小问题但可能导致误解。\n\n---\n\n## 主要优势\n\n1. **问题定义清晰、有启发性**：per-neuron BCE 与 global top-k 之间的 structural mismatch 是一个真实问题，gradient analysis 虽然本质上是 chain rule 的标准应用，但将其 formalize 并与 oracle F1 / SNR 实验联系起来的分析框架有价值。\n2. **消融设计合理**：Table 3 覆盖了 divergence direction (forward/reverse/JSD)、relaxation (Gumbel/STE)、BCE variants (±compensation, +Gumbel)，多维度隔离了设计选择。\n3. **诚实的 failure analysis**：论文没有隐瞒 MMLU 退化、无 wall-clock 加速等问题，而是将其作为分析对象（regime analysis, late-layer starvation），这是值得赞赏的。\n4. **2D Taxonomy 有组织价值**：correction granularity × training signal coupling 的分类框架是理解 sparsity prediction 文献的有用工具。\n5. **OOD 泛化评估**：C4 validation 上 52.5% advantage 的 OOD 实验（Appendix D）部分回应了 WikiText 训练/评估同源的担忧。\n6. **Reproducibility 细节充分**：hyperparameter 全量报告、training convergence curve、bottleneck sensitivity sweep，大部分实验可复现。\n\n---\n\n## Missing References\n\n- **MSE-based distillation for sparsity**: 论文 taxonomy 定义了 \"Intermediate (MSE)\" 这一列，cite 了 ShadowLLM 和 D2DMoE，但 **没有实验对比 MSE baseline**。如果要声称 KL (coupled) 优于 MSE (intermediate)，需要实验支撑。\n- **Larger-scale activation sparsity**: 论文应讨论 Griffin (De et al., 2024) 或 Mixture-of-Depths (Raposo et al., 2024) 等涉及 dynamic compute allocation 的工作，因为它们从不同角度解决了 conditional computation 的 allocation 问题。\n\n---\n\n## Questions for Authors\n\n1. §4.3 中 BCE PPL=22.51 对应哪个具体实验配置？为什么不在任何表格中？是 1000-step BCE 还是另一个 variant？\n2. 是否尝试过 MSE on hidden states 作为中间 coupling 水平的 ablation？这对验证 \"coupling 程度越强越好\" 的 claim 很关键。\n3. Table 5 中 40% KL uniform (exp_id: d030_kl40_uniform) 是否使用了在 30% 下训练的 predictor？如果是，这意味着不同行使用了不同的 predictor，影响 regime 分析的公平性。\n4. 是否测量过训练结束时 soft mask (τ=0.1) 与 hard mask 之间的 PPL gap？\n5. Appendix C (Table 11) 中 30% target λ=5000 (cap) with 5% deviation：如果 λ_max 设为更大值（如 10000），deviation 是否进一步降低？当前的 cap saturation 是否影响了 30% 的训练质量？\n\n---\n\n## Overall Assessment\n\n本文提出了一个有意义的问题（per-neuron BCE 与 global allocation 的 mismatch），gradient analysis 提供了清晰的 motivation。但实验执行存在几个关键缺陷：(1) 核心数字 22.51 无法追溯，(2) headline method 在 MMLU 上严重退化与论文叙事矛盾，(3) BCE vs KL 对比被 pipeline 差异混淆。这些问题共同削弱了论文的核心 contribution claim 的可信度。\n\n如果作者能 (a) 修复数据一致性、(b) 补充 controlled ablation（特别是 MSE baseline 和 per-layer KL）、(c) 重新 framing 以诚实反映 method 的实际适用范围，本文可以成为 Findings 级别的扎实 analytical contribution。当前状态需要 substantial revision。\n\n**推荐**: Resubmit next cycle (2 / 5)，修复后有 Findings 潜力。\n",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 审稿报告：方法严谨性 + 实验设计\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审稿标准**: ACL Rolling Review official review form (2025 updated, three-point scoring)\n\n---\n\n## Paper Summary\n\n本文研究用 forward KL divergence 替代 binary cross-entropy (BCE) 训练 SwiGLU LLM 的 contextual sparsity predictor。核心观察是 BCE 梯度按 neuron 独立分解，与 TEAL 推理时 global top-k 分配机制存在结构性不匹配。作者训练一个轻量 predictor (75.9M params)，通过 Gumbel-Sigmoid relaxation 实现端到端 KL 蒸馏，在 LLaMA-3.1-8B 50% sparsity 下 PPL 11.79 vs TEAL 23.31 (49% 改善)。论文同时分析了 global vs uniform allocation 在不同 sparsity 水平下的 downstream 表现，提出了 three-regime 框架，并给出 2D taxonomy 分类先前方法。\n\n---\n\n## 总体评分\n\n**Overall**: 2.5 / 5 (Borderline Findings)\n**一句话总结**: 问题定义清晰，梯度分析有启发性，但关键数据不一致、实验对比存在 pipeline 混淆变量、headline method 在最重要的 downstream task 上退化至随机水平，整体证据链不足以支撑 claims 的强度。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2.5 / 5 | 梯度分析数学正确但属 chain rule 的标准应用；BCE vs KL 对比存在严重 pipeline 混淆；22.51 PPL 幽灵数据；regime claim 证据密度不足 |\n| Excitement | 2.5 / 5 | 问题本身有意义（per-neuron vs global allocation mismatch），但实际结果令人失望：无 wall-clock 加速、MMLU 退化至 random、仅 7-8B scale |\n| Overall | 2.5 / 5 | 分析贡献有价值但实验缺陷削弱了可信度；需要修复数据一致性、补充 controlled comparison、调低 claim 强度 |\n| Reproducibility | 3.5 / 5 | 大部分超参和实验细节已报告；但主表结果为单 seed、22.51 数字不可追溯 |\n| Reviewer Confidence | 4 / 5 | 熟悉 activation sparsity、KD、Gumbel relaxation 领域 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **数据完整性：PPL 22.51 幽灵数字**\n- 具体位置：§4.3 (experiments.tex:66), Abstract, Introduction\n- 问题：§4.3 写到 \"BCE achieves +13pp oracle F1 (0.613 vs. 0.540) with 91% worse PPL (22.51 vs. 11.79)\"。然而 22.51 这个数字**不出现在论文任何表格中**。Table 2 中 BCE (2700 steps) = 27.97, BCE+Compensation = 25.44。如果 22.51 是 1000-step BCE 的结果，它需要在 Table 2 或 Table 3 中显示。数学验证：22.51/11.79 = 1.909 ≈ \"91% worse\"，但如果用 Table 2 的 27.97，则是 137% worse。Abstract 和 Introduction 反复使用 \"91% worse perplexity\" 这个数字作为核心 claim，但该 claim 所依赖的 baseline 数据无法从论文本身验证。\n- 为什么影响接收：论文最核心的 quantitative claim 之一不可追溯。审稿人无法从提交材料中 verify 该数字的来源。这不是 typo，是 **数据溯源链断裂**。\n- 建议：在 Table 2 或 Table 3 中补充 BCE 1000-step 的 PPL 数据行，或者用 Table 中已有的数字（27.97）重新计算百分比。\n\n---\n\n**N2** [critical] **Headline method 在最重要 downstream task 上退化至随机水平**\n- 具体位置：Table 2, Table 5, §4.5\n- 问题：论文主推方法 \"KL global (Ours)\" 在 30% sparsity 下 MMLU = 25.27%，而 4-choice random baseline = 25%。同一设定下 TEAL vanilla = 38.61%。即论文的核心方法在最广泛使用的知识评测上**比 baseline 差 13.3pp**，且约等于随机。论文的解释是 global top-k allocation 导致 late-layer starvation（L31 retention 28.4%），并提出 uniform allocation 作为修复（恢复至 40.61%）。但这实质上承认：**论文提出的 KL + TEAL global 组合在 downstream tasks 上不可用**，实际可用配置是 KL + uniform allocation——但 uniform allocation 本身消除了 global top-k 的概念，也就是说论文花大量篇幅分析的 \"global allocation quality\" 在实践中需要被绕过。\n- 为什么影响接收：论文的 framing 围绕 \"KL optimizes for global allocation quality\" (Abstract, §1, §3.5)，但实验结论表明 global allocation 在实践中损害 downstream performance。这是一个 **narrative vs evidence 的根本矛盾**。\n- 建议：(1) 重新定位主推方法为 KL + uniform，将 global 作为分析对象而非推荐配置；(2) 在 Table 2 中将 KL uniform 标为 Ours (recommended)；(3) 调整 Abstract/Introduction 的 framing，诚实反映 \"global allocation reveals a quality advantage in PPL but not downstream tasks\"。\n\n---\n\n**N3** [critical] **BCE vs KL 对比存在严重的 pipeline 混淆变量**\n- 具体位置：§4.3, §4.4, Table 3\n- 问题：KL 和 BCE 使用了完全不同的训练 pipeline：\n  - KL: Gumbel-Sigmoid soft masks + adaptive penalty controller + forward KL loss\n  - BCE: hard masks + compensation network (optional) + per-neuron BCE loss\n  \n  论文 claim \"the failure is structural, not due to architectural or compute differences\" (§4.3)，但这个 claim 无法从现有实验中得出，因为 loss function 和 relaxation method 是 **jointly varied** 的。Table 3 的 isolation 实验 \"BCE + Gumbel + Penalty (no KL)\" = 38.02（比 vanilla BCE 的 27.97 更差）恰好说明了这个问题：Gumbel + penalty 机制与 BCE loss 互不兼容，无法简单分离。\n\n  更公平的对比需要：(a) BCE + Gumbel + KL-style global objective (e.g., MSE on hidden states) 作为中间点；(b) KL + hard masks (STE) + no penalty 作为对照。Table 3 中 \"Forward KL + STE\" = 15.77 提供了部分信息，但仍然混杂了 relaxation 和 penalty 两个变量。\n\n  论文称 \"loss effect (ΔPPL=26.23) is 6.6× the relaxation effect (ΔPPL=3.98)\"，但 loss effect 的计算用了 BCE+Gumbel+Penalty=38.02 vs KL+Gumbel=11.79，而不是 controlled comparison。BCE+Gumbel+Penalty 之所以差，可能是因为 penalty controller 破坏了 BCE 的 per-neuron convergence（论文自己也指出 \"the penalty interferes with per-neuron optimization\"），而非 KL 本身有多好。\n- 为什么影响接收：无法从实验中 cleanly 区分 \"KL loss 的贡献\" vs \"Gumbel relaxation + penalty controller 对 KL 恰好有效的贡献\"。核心 claim \"distributional objectives outperform decomposed per-neuron losses\" 在 controlled experiment 意义上未被证明。\n- 建议：(1) 补充 MSE (intermediate coupling) ablation，对应 taxonomy 中的 intermediate 列；(2) 补充 per-layer KL (解耦 cross-layer coupling) 作为 controlled variant；(3) 明确 claim 是关于 \"KL+Gumbel+Penalty 组合\" 而非单独的 loss function。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **\"Three regimes\" 从 3 个数据点归纳——证据密度不足**\n- 具体位置：§4.5, Table 5\n- 问题：论文定义了 budget-surplus (≤30%), budget-constrained (~40%), capacity-limited (≥50%) 三个 regime。但整个分析基于 3 个 sparsity level（30%, 40%, 50%）× 2 个 allocation = 6 个数据点。每个 \"regime\" 实际上只有 1 个数据点。regime boundary 的精确位置（30%→40% 之间、40%→50% 之间）完全没有被定位。论文说 \"this boundary is consistent on both 7-8B models\"，但 Mistral 上没有 regime analysis 数据（Table 6 只有 PPL，无 downstream）。\n- 建议：(1) 补充 35%, 45% 的数据以定位 regime transition；(2) 降低 claim 强度为 \"we observe non-monotonic behavior suggestive of distinct operating regimes\"；(3) 在 Mistral 上补充 downstream 数据。\n\n**W2** [warning] **无 wall-clock 加速——6.4% overhead**\n- 具体位置：Appendix A, Table 7\n- 问题：在 50% sparsity 下，KL predictor 的推理延迟为 126.78ms vs dense 的 119.11ms，即 **增加** 6.4% 延迟。论文在 Limitations 中承认需要 sparse kernel support，但 title (\"Contextual Sparsity Prediction\") 和 motivation (§1 第一段) 暗示了推理效率提升。一个增加延迟的 \"sparsity\" 方法在实用性上存在根本性问题。\n- 建议：在 Abstract 中明确这是一个 prediction quality 研究，而非推理加速工作。\n\n**W3** [warning] **Train-inference mismatch 未量化**\n- 具体位置：§3.3, Appendix B.1\n- 问题：训练使用 Gumbel-Sigmoid soft masks（τ=0.1 时仍是 soft），推理使用 hard top-k binary masks。这两者之间的 gap 从未被直接量化。Appendix B.1 的 temperature sensitivity 实验只测了不同 τ schedule 下的 TEAL global PPL，但没有报告 \"soft mask at τ=0.1 PPL\" vs \"hard mask PPL\"。Appendix B (Table 8) 的 per-token evaluation (9.218) 与 TEAL global (11.963) 的差距混合了 train-inference mismatch 和 allocation loss，无法分离。\n- 建议：报告训练末期 soft mask (τ=0.1) 下的 PPL 与 hard mask 下的 PPL 对比。\n\n**W4** [warning] **主表结果为单 seed**\n- 具体位置：Table 2 caption, Appendix E\n- 问题：Table 2 的所有关键对比（KL global 11.79, TEAL 23.31 等）都是 **单 seed** 结果。三 seed 评估仅在 50% uniform 配置下进行（11.92±0.07），且仅报告 PPL。核心 claim \"49% PPL reduction\" 基于单 seed。30% sparsity 下 KL global MMLU=25.27% 如果有 ±2pp 的方差就可能与 random baseline 无显著差异。Downstream metrics 的多 seed 数据仅在 Appendix E 简要提及一行。\n- 建议：至少对 Table 2 的关键行（KL global 30%、50%，TEAL 30%、50%）做 3-seed 评估。\n\n**W5** [warning] **模型规模局限**\n- 具体位置：§4 全文, Limitations\n- 问题：仅在 LLaMA-3.1-8B 和 Mistral-7B-v0.3 上测试。Title 说 \"SwiGLU LLMs\" 暗示广泛适用性。两个同规模（7-8B）模型不能代表 13B、70B 或更大模型上的表现。论文的 \"structural mismatch\" 是关于 SwiGLU 架构的一般性 claim，但实验范围不支撑。\n- 建议：在 Title 中限定为 \"7-8B SwiGLU LLMs\"，或补充至少一个 13B 模型的实验。\n\n**W6** [warning] **Adaptive Penalty Controller 无收敛保证**\n- 具体位置：§3.4, Appendix C (Table 11)\n- 问题：multiplicative schedule 是一个 heuristic，论文已在脚注中承认 \"不保证 KKT 满足\"。Appendix Table 11 显示 30% target 的 λ saturate at cap (5000) 且 deviation = 5.0%，意味着 controller 在该操作点 **没有收敛** 而是 **hit ceiling**。70% target 同样 saturate at cap (1000)。只有 40% 和 50% 真正收敛。这与正文 \"converges within 40-110 steps across all targets\" (§3.4) 的 claim 矛盾——hit cap 不等于 convergence。\n- 建议：(1) 修正 §3.4 的 convergence claim，区分 \"convergence\" 和 \"saturation at cap\"；(2) 讨论 cap saturation 对训练质量的潜在影响。\n\n---\n\n## 小问题（不影响接收）\n\n- §4.4 SPON analysis 脚注提到 \"SPON analysis uses evaluate.py; main results use the unified benchmark\"——这意味着 SPON 的 2.4% improvement (12.08→11.79) 可能是在不同 evaluation protocol 下比较的数字，不够严谨。\n- Table 5 的 40% KL uniform PPL=8.36 footnote 标注该 predictor \"uses a predictor trained at the respective sparsity target\"，但 exp_id 标注为 \"d030_kl40_uniform\"（d030 暗示 predictor 在 30% 下训练，评估在 40% 下），需要澄清。\n- Abstract 中 \"7-8B scale\" 的 claim 实际基于两个具体模型（LLaMA-8B, Mistral-7B），措辞给人更广泛验证的错觉。\n- Table 1 (taxonomy) 的 \"Static × Decomposed\" 和 \"Static × Intermediate\" 两个 cell 标为 \"---\"，但 magnitude pruning (TEAL itself) 可被视为 static × decomposed，应讨论。\n- 引用 xu2026spon 的 bib key 写成 2026 但论文年份为 2025 (ICML 2025)，虽是小问题但可能导致误解。\n\n---\n\n## 主要优势\n\n1. **问题定义清晰、有启发性**：per-neuron BCE 与 global top-k 之间的 structural mismatch 是一个真实问题，gradient analysis 虽然本质上是 chain rule 的标准应用，但将其 formalize 并与 oracle F1 / SNR 实验联系起来的分析框架有价值。\n2. **消融设计合理**：Table 3 覆盖了 divergence direction (forward/reverse/JSD)、relaxation (Gumbel/STE)、BCE variants (±compensation, +Gumbel)，多维度隔离了设计选择。\n3. **诚实的 failure analysis**：论文没有隐瞒 MMLU 退化、无 wall-clock 加速等问题，而是将其作为分析对象（regime analysis, late-layer starvation），这是值得赞赏的。\n4. **2D Taxonomy 有组织价值**：correction granularity × training signal coupling 的分类框架是理解 sparsity prediction 文献的有用工具。\n5. **OOD 泛化评估**：C4 validation 上 52.5% advantage 的 OOD 实验（Appendix D）部分回应了 WikiText 训练/评估同源的担忧。\n6. **Reproducibility 细节充分**：hyperparameter 全量报告、training convergence curve、bottleneck sensitivity sweep，大部分实验可复现。\n\n---\n\n## Missing References\n\n- **MSE-based distillation for sparsity**: 论文 taxonomy 定义了 \"Intermediate (MSE)\" 这一列，cite 了 ShadowLLM 和 D2DMoE，但 **没有实验对比 MSE baseline**。如果要声称 KL (coupled) 优于 MSE (intermediate)，需要实验支撑。\n- **Larger-scale activation sparsity**: 论文应讨论 Griffin (De et al., 2024) 或 Mixture-of-Depths (Raposo et al., 2024) 等涉及 dynamic compute allocation 的工作，因为它们从不同角度解决了 conditional computation 的 allocation 问题。\n\n---\n\n## Questions for Authors\n\n1. §4.3 中 BCE PPL=22.51 对应哪个具体实验配置？为什么不在任何表格中？是 1000-step BCE 还是另一个 variant？\n2. 是否尝试过 MSE on hidden states 作为中间 coupling 水平的 ablation？这对验证 \"coupling 程度越强越好\" 的 claim 很关键。\n3. Table 5 中 40% KL uniform (exp_id: d030_kl40_uniform) 是否使用了在 30% 下训练的 predictor？如果是，这意味着不同行使用了不同的 predictor，影响 regime 分析的公平性。\n4. 是否测量过训练结束时 soft mask (τ=0.1) 与 hard mask 之间的 PPL gap？\n5. Appendix C (Table 11) 中 30% target λ=5000 (cap) with 5% deviation：如果 λ_max 设为更大值（如 10000），deviation 是否进一步降低？当前的 cap saturation 是否影响了 30% 的训练质量？\n\n---\n\n## Overall Assessment\n\n本文提出了一个有意义的问题（per-neuron BCE 与 global allocation 的 mismatch），gradient analysis 提供了清晰的 motivation。但实验执行存在几个关键缺陷：(1) 核心数字 22.51 无法追溯，(2) headline method 在 MMLU 上严重退化与论文叙事矛盾，(3) BCE vs KL 对比被 pipeline 差异混淆。这些问题共同削弱了论文的核心 contribution claim 的可信度。\n\n如果作者能 (a) 修复数据一致性、(b) 补充 controlled ablation（特别是 MSE baseline 和 per-layer KL）、(c) 重新 framing 以诚实反映 method 的实际适用范围，本文可以成为 Findings 级别的扎实 analytical contribution。当前状态需要 substantial revision。\n\n**推荐**: Resubmit next cycle (2 / 5)，修复后有 Findings 潜力。\n",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 245 · 2026-05-17T09:23:53.416195+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3924
}
```

</details>

---


### Assistant

_source line 246 · 2026-05-17T09:24:03.227452+00:00_

审稿报告已提交给 Review Director。

**审查总结**：

核心发现 3 个 critical 问题 + 6 个 warning 问题：

**Critical**:
1. **数据完整性**：§4.3 中 BCE PPL=22.51 不存在于任何表格中，但 "91% worse PPL" 这个核心 claim（出现在 Abstract、Introduction、Experiments）依赖此数字
2. **Headline method MMLU 退化**：KL global 在 30% sparsity 下 MMLU=25.27%（≈random），比 TEAL 差 13pp，与论文 "optimizes for global allocation quality" 的叙事矛盾
3. **Pipeline 混淆变量**：KL 和 BCE 使用完全不同的训练 pipeline（Gumbel vs hard mask, penalty vs none），无法 cleanly 隔离 loss function 的贡献

**评分**: Overall 2.5/5 (Borderline Findings), Soundness 2.5/5, Excitement 2.5/5。修复数据一致性、补充 controlled ablation、调整 framing 后有 Findings 潜力。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1"
}
```

</details>

---


## Round 9

## Round 9

4 recorded events


### User

_source line 247 · 2026-05-17T09:24:51.838785+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix (N1-N3)、Should-Fix (W1-W7)、小问题 (P1-P5) 和 Questions (Q1-Q5)，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

# Reviewer 2 完整审稿报告

## Must-Fix 问题

**N1** [critical] 核心新颖性不足：与 MaskLLM 的区分过于薄弱
- MaskLLM (Fang et al., NeurIPS 2024) 的高层框架与本文几乎完全一致：frozen base model weights + learnable masks + Gumbel relaxation + KL divergence training。论文在 §2 声称区别在于 "weight vs activation sparsity" 和 "static N:M vs dynamic per-token"。但这本质上是将一个已被验证有效的训练范式应用到一个不同的 sparsity type，属于 application-level 的迁移而非方法论创新。
- 论文声称 "The structural mismatch we identify does not arise in MaskLLM's per-group categorical setting"，但这恰恰说明 structural mismatch 分析是 task-specific 的适配，而非通用性洞察。

**N2** [critical] 实际推理无加速，效率动机不成立
- Table 8 明确显示 pipeline 增加 6.4% overhead。unstructured element-wise masks 无法利用硬件稀疏加速。Abstract 的 "49% reduction" PPL 结果容易让读者误认为有速度提升。

**N3** [critical] PPL-centric 叙事掩盖 downstream collapse 的严重性
- 30% sparsity, KL global: MMLU 25.27%（dense 65.27%，降 40pp，近乎随机）
- 50% sparsity: MMLU 27.89%, GSM8K 1.29%（完全失效）
- KL global 是论文的 primary inference protocol，而 KL global 在所有设置下 MMLU 都很差
- 论文试图将问题归因于 allocation strategy，但 global allocation 是论文自己的 primary protocol

## Should-Fix 问题

**W1** [warning] "Structural mismatch" 洞察的新颖性可质疑
- end-to-end 目标优于 decomposed per-component 目标是深度学习的基本原则。论文将 BCE 独立梯度 vs KL Jacobian 耦合包装为 novel insight，但本质上是 "end-to-end loss 能捕获组件间交互" 的直接推论。

**W2** [warning] Taxonomy (Table 1) 贡献价值有限
- 2D taxonomy 是 post-hoc organization，没有做出可验证的预测。"Static × Decomposed" 和 "Static × Intermediate" 是空的但未讨论原因。

**W3** [warning] 三 regime 分析数据点过少
- 3 个 sparsity level × 2 个模型 = 6 个数据点，每个 regime 只有 1 个数据点。regime boundary 精确位置未被定位。

**W4** [warning] Related work 遗漏重要引用
- MiniLLM (forward vs reverse KL for LLM distillation, ICLR 2024)
- SVD Contextual Sparsity Predictors (arxiv 2603.14110)
- SparseLoRA (ICML 2025)
- Broader LLM distillation literature
- 32 篇引用对 EMNLP long paper 偏少（typical: 40-60）

**W5** [warning] D2DMoE taxonomy positioning 需更细致
- D2DMoE 的训练包含 router training 和 expert conversion，不仅仅是 MSE on hidden states。

**W6** [warning] Training/evaluation domain overlap
- WikiText-103 训练, WikiText-2 评测。C4 OOD PPL 18.40 比 WikiText-2 的 11.79 高 56%。

**W7** [warning] Framing 不一致：mechanistic understanding vs efficiency
- Conclusion 提到 wall-clock speedup 和 practical deployment value 作为 future directions，与 understanding framing 矛盾。

## 小问题 P1-P5
- P1: SPON eval protocol 不一致
- P2: 早 saturation 可作 efficiency 优势
- P3: BCE 不同 inference pipeline 的公平性说明不够显眼
- P4: bib xu2026spon key vs year 不一致
- P5: 75.9M "lightweight" 标准不明确

## Questions Q1-Q5
- Q1: MaskLLM 直接迁移到 activation sparsity 的效果？
- Q2: KL predictor 与 TEAL global top-k 是否根本性不兼容？
- Q3: Forward vs reverse KL 与 MiniLLM 结论矛盾？
- Q4: 什么条件下 unstructured sparsity 能实现实际加速？
- Q5: 三 regime 的精确边界？

---

请逐条用 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 248 · 2026-05-17T09:27:21.746360+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n**[AGREE] R2-N1: 与 MaskLLM 的区分薄弱**\n\n同意 R2 的判断。论文 §2 Related Work 已承认两者共享 \"frozen weights + learnable masks + KL training\" 范式，区别仅在 sparsity type（weight N:M vs activation per-token）和 mask generation（static categorical vs dynamic per-neuron）。论文的辩护是 \"structural mismatch does not arise in MaskLLM's per-group categorical setting\"（§2 第二段），但正如 R2 所指出，这恰好说明论文的核心 \"insight\" 是 MaskLLM 范式在新 setting 下的 task-specific 适配，而非通用性方法论贡献。\n\n**补充证据**：论文的方法部分（§3.1-§3.4）除了 Adaptive Penalty Controller（§3.4）外，每个组件都有直接对应的已有工作：Gumbel-Sigmoid relaxation → MaskLLM/Concrete distribution，KL distillation → MaskLLM/standard KD，per-layer MLP predictor → DejaVu/FastForward。唯一的方法论新增是 multiplicative penalty schedule，但这只是 augmented Lagrangian 的一个简化 heuristic（§3.4 脚注自承）。\n\n如果论文重新定位为 **empirical analysis paper**（\"我们验证了 KL 范式在 activation sparsity + global allocation 设定下的表现，发现了 structural mismatch 现象\"），novelty 问题会缓解。但当前 framing 混合了 method contribution 和 analytical contribution，导致 novelty expectation 被拉高。\n\n---\n\n**[AGREE] R2-N2: 无 wall-clock 加速**\n\n完全同意。Table 8（Appendix A）显示 KL predictor 在 50% sparsity 下 latency 126.78ms vs dense 119.11ms，即 **增加 6.4% 延迟**。论文在 Limitations 中承认 \"actual wall-clock acceleration depends on sparse kernel implementations\"，但 Abstract 和 Introduction 的 motivation 从 \"contextual sparsity\" 的 inference efficiency 角度切入，给读者建立了效率提升的预期。\n\n**补充**：我在自己的审稿中将此列为 W2 (warning) 而非 critical。R2 升级为 critical 有其道理——如果论文的 motivation 是 efficiency 但实际结果是 overhead，这是一个叙事诚信问题。但论文 Limitations 的坦诚报告和 Conclusion 的 \"prediction quality rather than systems optimization\" 定位部分缓解了这一点。我倾向于 **介于 critical 和 warning 之间**：不至一票否决，但需要在 Abstract 中明确 \"本文研究 prediction quality，不提供 wall-clock 加速\"。\n\n---\n\n**[AGREE] R2-N3: PPL-centric 叙事掩盖 downstream collapse**\n\n强烈同意。这与我自己的 N2 (critical) 完全一致。数据清晰：\n\n- Table 2：30% KL global MMLU = 25.27%（≈ 4-choice random），TEAL vanilla = 38.61%\n- Table 2：50% KL global MMLU = 27.89%，GSM8K = 1.29%\n- Table 5：即使是 \"best case\" 的 30% KL uniform = 40.61%，也比 dense 65.27% 低 24.7pp\n\n论文的 primary inference protocol \"KL + TEAL global\" 在所有设定下 MMLU 都不可用。论文试图用 regime analysis（§4.5）和 \"allocation strategy vs predictor quality\" 的归因来化解，但实际效果是：读者读完论文后不清楚这个方法在什么条件下 **真正可用**。\n\nR2 和我对此问题的 severity 评估完全一致：critical。\n\n---\n\n## Should-Fix 问题\n\n**[AGREE] R2-W1: \"Structural mismatch\" insight 新颖性可质疑**\n\n部分同意，有补充。R2 说 \"end-to-end 目标优于 decomposed 目标是基本原则\"，这个判断是对的。§3.5 的梯度分析本质上是对 chain rule 的展开——factor (b) 的 Jacobian 耦合是任何 end-to-end loss 的固有性质，不是 KL 特有的。\n\n**但有一个有价值的 empirical 观察**：BCE F1=0.613 > KL F1=0.540，但 KL PPL 远优（§4.3）。这个 \"高 accuracy 反而差 performance\" 的现象不是先验显然的——直觉上 per-neuron 更准确应该更好。论文将此解释为 proxy misalignment，这个 empirical finding 本身有贡献。但把它包装成 \"formal gradient analysis\" 级别的理论贡献确实过度了。\n\n---\n\n**[REBUT] R2-W2: Taxonomy 贡献有限**\n\n部分不同意。Taxonomy（Table 1）虽然是 post-hoc 的描述性分类，但在 activation sparsity prediction 领域没有先前工作做过这种系统化整理。2D 框架（correction granularity × training signal coupling）确实帮助定位了方法空间中的空白（Per-token × Coupled cell），并为 reader 提供了快速理解方法关系的入口。\n\n但我同意 R2 的两个具体批评：(1) 空 cell（Static × Decomposed, Static × Intermediate）未讨论原因——TEAL 可以被视为 Static × Decomposed，这个遗漏需要修正；(2) taxonomy 不做可验证预测，限制了其科学贡献。\n\n**结论**：taxonomy 有 organizational utility，但不应作为 contribution 列表中的独立条目。它更适合作为 Related Work 的组织框架。\n\n---\n\n**[AGREE] R2-W3: 三 regime 分析数据点不足**\n\n完全同意，这与我自己的 W1 一致。3 个 sparsity level × 2 allocation = 6 data points，每个 \"regime\" 仅 1 个观测。regime boundary 的位置（30%→40% 之间 surplus→constrained 转变、40%→50% 之间 constrained→limited 转变）完全没有被细粒度定位。论文说 \"this boundary is consistent on both 7-8B models\"（§4.5），但 Mistral 上根本没有 downstream regime 数据（Table 6 只有 PPL）。\n\n---\n\n**[AGREE] R2-W4: Missing references**\n\n同意引用不足。32 篇对 EMNLP long paper 偏少（R2 给出的 typical range 40-60 是合理的）。具体遗漏：\n\n- **MiniLLM (Gu et al., ICLR 2024)**：直接相关——研究 forward vs reverse KL 在 LLM distillation 中的差异，论文 §4.4 ablation 测了 forward vs reverse KL 但未讨论 MiniLLM 的结论。这对 Q3 尤其重要。\n- **Broader LLM distillation 文献**：论文 cite 了 Hinton (2015)、DistilBERT、Sequence-KD，但缺少近年 LLM-specific distillation 工作（GKD, MiniLLM 等）。\n\nR2 提到的 SVD Contextual Sparsity Predictors (arxiv 2603.14110) 我无法确认是否已公开（arXiv 2603 prefix 暗示 2026年3月），如果在 submission deadline 之前公开则应引用。\n\n---\n\n**[AGREE] R2-W5: D2DMoE taxonomy positioning 简化**\n\n同意。论文将 D2DMoE 归类为 \"Intermediate (MSE)\" coupling，但 D2DMoE 的训练流程包含 expert conversion（将 dense FFN 重组为 MoE）+ router training + fine-tuning，远比单纯 MSE 监督复杂。§2 的描述 \"converts dense FFNs to dynamic-k experts with MSE supervision on hidden states\" 遗漏了 expert conversion 的结构性变化。这影响了 taxonomy 中 D2DMoE 的准确定位。\n\n---\n\n**[REBUT] R2-W6: Training/evaluation domain overlap**\n\n部分不同意。WikiText-103 训练 / WikiText-2 评测的同源性确实是一个 concern，但论文在 Appendix D 提供了 C4 OOD 评估。R2 指出 \"C4 PPL 18.40 比 WikiText-2 的 11.79 高 56%\"，但这个 gap 主要反映 domain shift 对 absolute PPL 的影响（dense 模型本身也从 6.12 升至 9.21，即 50.5% increase）。更重要的指标是 **relative advantage**：WikiText-2 上 KL vs TEAL = 49% improvement，C4 上 = 52.5% improvement。Relative advantage 在 OOD 数据上 **保持甚至略增**，说明 predictor 学到了可迁移的 neuron importance patterns。\n\n**但**：OOD 评估仅在 50% sparsity 下进行，缺少 30% 和 40% 的 OOD 数据。鉴于 30% 的 downstream 表现（MMLU 25.27%）是论文最薄弱的环节，OOD 下 30% 的表现尤为关键。这一点上 R2 的 concern 有道理。\n\n---\n\n**[AGREE] R2-W7: Framing 不一致**\n\n同意。Introduction 的 reframing 侧重 \"mechanistic understanding\"（梯度分析、structural mismatch、regime taxonomy），但 Conclusion 最后一段直接提到 \"wall-clock speedup\" 和 \"practical deployment value\" 作为 future directions（§5 最后一句）。如果论文定位是 analytical/mechanistic contribution，Conclusion 不应将效率作为核心 future direction，否则暗示当前工作的 motivation 仍然是效率。应改为以 allocation-aware training、scale validation 等分析方向收尾。\n\n---\n\n## 小问题 P1-P5\n\n**[AGREE] R2-P1: SPON eval protocol 不一致**\n同意。§4.4 脚注说明 SPON 用 evaluate.py 而 main results 用 unified benchmark，2.4% improvement (12.08→11.79) 可能在不同 evaluation 下不可比。我在自己的 review 中也标记了此问题。\n\n**[AGREE] R2-P2: 早 saturation 可作 efficiency 优势**\n同意。Appendix B.3 Table 10 显示 800 步即饱和（PPL 11.907 vs 1000步 11.906），可以节省 20% 训练时间。论文未将此作为 efficiency advantage 强调，是一个轻度遗漏。\n\n**[AGREE] R2-P3: BCE inference pipeline 差异说明不够显眼**\n同意。Table 2 caption 有脚注 \"BCE uses a different inference protocol\"，但正文 §4.3 的 iso-compute 对比直接比较 27.97 vs 11.79 而未在对比句中重申 pipeline 差异。\n\n**[AGREE] R2-P4: bib key xu2026spon vs actual year**\n同意，与我自己的小问题一致。\n\n**[REBUT] R2-P5: 75.9M \"lightweight\" 标准不明确**\n不同意这是一个问题。论文 §3.2 明确给出了比较基准：\"less than 1% of the 8B base model\"。在 8B 模型上下文中，75.9M 占比 <1% 在 predictor-based sparsity 文献中属于标准量级（DejaVu 和 FastForward 的 predictor 规模相当）。\"Lightweight\" 的含义在上下文中是清晰的。\n\n---\n\n## Questions Q1-Q5\n\n**Q1: MaskLLM 直接迁移到 activation sparsity 的效果？**\n这是一个好问题，但超出了作者当前实验范围。MaskLLM 使用 Gumbel-Softmax 进行 per-group N:M categorical selection，直接迁移到 unstructured per-token activation sparsity 需要重新设计 mask generation 机制（从 categorical → binary）。但如果作者能展示 \"MaskLLM-style baseline\" 的表现，会大大增强 novelty 论证。建议作者在 revision 中补充此对比。\n\n**Q2: KL predictor 与 TEAL global top-k 是否根本不兼容？**\n[AGREE] 这是一个关键问题。Table 2 和 Table 5 的数据显示：在所有 sparsity 水平下，KL global 的 MMLU 都严重退化（30%: 25.27%, 40%: 38.06%, 50%: 27.89%）。如果 KL + global 在 downstream 上始终不可用，论文的 \"optimize for global allocation quality\" narrative 就存在根本矛盾。这个问题与我的 N2 和 R2 的 N3 直接相关。\n\n**Q3: Forward vs reverse KL 与 MiniLLM 结论矛盾？**\n[AGREE] 这是一个需要讨论的重要点。MiniLLM (Gu et al., ICLR 2024) 发现 reverse KL（避免 mode-averaging）在 LLM distillation 中更好，但本文 Table 3 显示 forward KL (11.79) > reverse KL (12.80)。两者的 context 不同（model distillation vs mask training），但论文应该讨论为什么结论相反——可能是因为 mask training 的 mode structure 与 model output distribution 不同，forward KL 的 mean-seeking 性质在 mask 优化中更有利（§3.4 简要提了一句 \"preserve the dense model's primary predictions\" 但未深入）。\n\n**Q4: 什么条件下 unstructured sparsity 能实现实际加速？**\n这是一个合理但超出论文范围的问题。论文 Limitations 已指出需要 \"Triton block-sparse, cuSPARSE\" 支持。当前 unstructured sparsity 在 GPU 上几乎无法加速是领域共识。\n\n**Q5: 三 regime 的精确边界？**\n[AGREE] 与我的 W1 和 R2 的 W3 一致。需要更细粒度的 sparsity sweep（35%, 45% 等）来定位 transition points。\n\n---\n\n## 总结\n\nR2 的审稿意见整体准确且有深度。在 13 个具体 issue 中，我 **同意 10 项**、**部分反驳 3 项**（W2 taxonomy、W6 domain overlap、P5 lightweight 标准）。\n\nR2 与我的审稿最大的共识在于：\n1. **Downstream collapse 是核心问题**（R2-N3 = 我的 N2）\n2. **Regime analysis 数据不足**（R2-W3 = 我的 W1）\n3. **实际效率缺失**（R2-N2 = 我的 W2）\n\nR2 提出而我未覆盖的最有价值的新观点是 **N1（与 MaskLLM 的 novelty 区分）** 和 **W4（missing references，特别是 MiniLLM）**。这两点我完全同意，会影响整体评分。\n\n结合 R2 的意见，我维持 **Overall 2.5/5 (Resubmit next cycle)** 的评分，可能下调至 2.0。核心障碍是 downstream 失效 + 数据不一致 + novelty 有限的组合。\n",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n**[AGREE] R2-N1: 与 MaskLLM 的区分薄弱**\n\n同意 R2 的判断。论文 §2 Related Work 已承认两者共享 \"frozen weights + learnable masks + KL training\" 范式，区别仅在 sparsity type（weight N:M vs activation per-token）和 mask generation（static categorical vs dynamic per-neuron）。论文的辩护是 \"structural mismatch does not arise in MaskLLM's per-group categorical setting\"（§2 第二段），但正如 R2 所指出，这恰好说明论文的核心 \"insight\" 是 MaskLLM 范式在新 setting 下的 task-specific 适配，而非通用性方法论贡献。\n\n**补充证据**：论文的方法部分（§3.1-§3.4）除了 Adaptive Penalty Controller（§3.4）外，每个组件都有直接对应的已有工作：Gumbel-Sigmoid relaxation → MaskLLM/Concrete distribution，KL distillation → MaskLLM/standard KD，per-layer MLP predictor → DejaVu/FastForward。唯一的方法论新增是 multiplicative penalty schedule，但这只是 augmented Lagrangian 的一个简化 heuristic（§3.4 脚注自承）。\n\n如果论文重新定位为 **empirical analysis paper**（\"我们验证了 KL 范式在 activation sparsity + global allocation 设定下的表现，发现了 structural mismatch 现象\"），novelty 问题会缓解。但当前 framing 混合了 method contribution 和 analytical contribution，导致 novelty expectation 被拉高。\n\n---\n\n**[AGREE] R2-N2: 无 wall-clock 加速**\n\n完全同意。Table 8（Appendix A）显示 KL predictor 在 50% sparsity 下 latency 126.78ms vs dense 119.11ms，即 **增加 6.4% 延迟**。论文在 Limitations 中承认 \"actual wall-clock acceleration depends on sparse kernel implementations\"，但 Abstract 和 Introduction 的 motivation 从 \"contextual sparsity\" 的 inference efficiency 角度切入，给读者建立了效率提升的预期。\n\n**补充**：我在自己的审稿中将此列为 W2 (warning) 而非 critical。R2 升级为 critical 有其道理——如果论文的 motivation 是 efficiency 但实际结果是 overhead，这是一个叙事诚信问题。但论文 Limitations 的坦诚报告和 Conclusion 的 \"prediction quality rather than systems optimization\" 定位部分缓解了这一点。我倾向于 **介于 critical 和 warning 之间**：不至一票否决，但需要在 Abstract 中明确 \"本文研究 prediction quality，不提供 wall-clock 加速\"。\n\n---\n\n**[AGREE] R2-N3: PPL-centric 叙事掩盖 downstream collapse**\n\n强烈同意。这与我自己的 N2 (critical) 完全一致。数据清晰：\n\n- Table 2：30% KL global MMLU = 25.27%（≈ 4-choice random），TEAL vanilla = 38.61%\n- Table 2：50% KL global MMLU = 27.89%，GSM8K = 1.29%\n- Table 5：即使是 \"best case\" 的 30% KL uniform = 40.61%，也比 dense 65.27% 低 24.7pp\n\n论文的 primary inference protocol \"KL + TEAL global\" 在所有设定下 MMLU 都不可用。论文试图用 regime analysis（§4.5）和 \"allocation strategy vs predictor quality\" 的归因来化解，但实际效果是：读者读完论文后不清楚这个方法在什么条件下 **真正可用**。\n\nR2 和我对此问题的 severity 评估完全一致：critical。\n\n---\n\n## Should-Fix 问题\n\n**[AGREE] R2-W1: \"Structural mismatch\" insight 新颖性可质疑**\n\n部分同意，有补充。R2 说 \"end-to-end 目标优于 decomposed 目标是基本原则\"，这个判断是对的。§3.5 的梯度分析本质上是对 chain rule 的展开——factor (b) 的 Jacobian 耦合是任何 end-to-end loss 的固有性质，不是 KL 特有的。\n\n**但有一个有价值的 empirical 观察**：BCE F1=0.613 > KL F1=0.540，但 KL PPL 远优（§4.3）。这个 \"高 accuracy 反而差 performance\" 的现象不是先验显然的——直觉上 per-neuron 更准确应该更好。论文将此解释为 proxy misalignment，这个 empirical finding 本身有贡献。但把它包装成 \"formal gradient analysis\" 级别的理论贡献确实过度了。\n\n---\n\n**[REBUT] R2-W2: Taxonomy 贡献有限**\n\n部分不同意。Taxonomy（Table 1）虽然是 post-hoc 的描述性分类，但在 activation sparsity prediction 领域没有先前工作做过这种系统化整理。2D 框架（correction granularity × training signal coupling）确实帮助定位了方法空间中的空白（Per-token × Coupled cell），并为 reader 提供了快速理解方法关系的入口。\n\n但我同意 R2 的两个具体批评：(1) 空 cell（Static × Decomposed, Static × Intermediate）未讨论原因——TEAL 可以被视为 Static × Decomposed，这个遗漏需要修正；(2) taxonomy 不做可验证预测，限制了其科学贡献。\n\n**结论**：taxonomy 有 organizational utility，但不应作为 contribution 列表中的独立条目。它更适合作为 Related Work 的组织框架。\n\n---\n\n**[AGREE] R2-W3: 三 regime 分析数据点不足**\n\n完全同意，这与我自己的 W1 一致。3 个 sparsity level × 2 allocation = 6 data points，每个 \"regime\" 仅 1 个观测。regime boundary 的位置（30%→40% 之间 surplus→constrained 转变、40%→50% 之间 constrained→limited 转变）完全没有被细粒度定位。论文说 \"this boundary is consistent on both 7-8B models\"（§4.5），但 Mistral 上根本没有 downstream regime 数据（Table 6 只有 PPL）。\n\n---\n\n**[AGREE] R2-W4: Missing references**\n\n同意引用不足。32 篇对 EMNLP long paper 偏少（R2 给出的 typical range 40-60 是合理的）。具体遗漏：\n\n- **MiniLLM (Gu et al., ICLR 2024)**：直接相关——研究 forward vs reverse KL 在 LLM distillation 中的差异，论文 §4.4 ablation 测了 forward vs reverse KL 但未讨论 MiniLLM 的结论。这对 Q3 尤其重要。\n- **Broader LLM distillation 文献**：论文 cite 了 Hinton (2015)、DistilBERT、Sequence-KD，但缺少近年 LLM-specific distillation 工作（GKD, MiniLLM 等）。\n\nR2 提到的 SVD Contextual Sparsity Predictors (arxiv 2603.14110) 我无法确认是否已公开（arXiv 2603 prefix 暗示 2026年3月），如果在 submission deadline 之前公开则应引用。\n\n---\n\n**[AGREE] R2-W5: D2DMoE taxonomy positioning 简化**\n\n同意。论文将 D2DMoE 归类为 \"Intermediate (MSE)\" coupling，但 D2DMoE 的训练流程包含 expert conversion（将 dense FFN 重组为 MoE）+ router training + fine-tuning，远比单纯 MSE 监督复杂。§2 的描述 \"converts dense FFNs to dynamic-k experts with MSE supervision on hidden states\" 遗漏了 expert conversion 的结构性变化。这影响了 taxonomy 中 D2DMoE 的准确定位。\n\n---\n\n**[REBUT] R2-W6: Training/evaluation domain overlap**\n\n部分不同意。WikiText-103 训练 / WikiText-2 评测的同源性确实是一个 concern，但论文在 Appendix D 提供了 C4 OOD 评估。R2 指出 \"C4 PPL 18.40 比 WikiText-2 的 11.79 高 56%\"，但这个 gap 主要反映 domain shift 对 absolute PPL 的影响（dense 模型本身也从 6.12 升至 9.21，即 50.5% increase）。更重要的指标是 **relative advantage**：WikiText-2 上 KL vs TEAL = 49% improvement，C4 上 = 52.5% improvement。Relative advantage 在 OOD 数据上 **保持甚至略增**，说明 predictor 学到了可迁移的 neuron importance patterns。\n\n**但**：OOD 评估仅在 50% sparsity 下进行，缺少 30% 和 40% 的 OOD 数据。鉴于 30% 的 downstream 表现（MMLU 25.27%）是论文最薄弱的环节，OOD 下 30% 的表现尤为关键。这一点上 R2 的 concern 有道理。\n\n---\n\n**[AGREE] R2-W7: Framing 不一致**\n\n同意。Introduction 的 reframing 侧重 \"mechanistic understanding\"（梯度分析、structural mismatch、regime taxonomy），但 Conclusion 最后一段直接提到 \"wall-clock speedup\" 和 \"practical deployment value\" 作为 future directions（§5 最后一句）。如果论文定位是 analytical/mechanistic contribution，Conclusion 不应将效率作为核心 future direction，否则暗示当前工作的 motivation 仍然是效率。应改为以 allocation-aware training、scale validation 等分析方向收尾。\n\n---\n\n## 小问题 P1-P5\n\n**[AGREE] R2-P1: SPON eval protocol 不一致**\n同意。§4.4 脚注说明 SPON 用 evaluate.py 而 main results 用 unified benchmark，2.4% improvement (12.08→11.79) 可能在不同 evaluation 下不可比。我在自己的 review 中也标记了此问题。\n\n**[AGREE] R2-P2: 早 saturation 可作 efficiency 优势**\n同意。Appendix B.3 Table 10 显示 800 步即饱和（PPL 11.907 vs 1000步 11.906），可以节省 20% 训练时间。论文未将此作为 efficiency advantage 强调，是一个轻度遗漏。\n\n**[AGREE] R2-P3: BCE inference pipeline 差异说明不够显眼**\n同意。Table 2 caption 有脚注 \"BCE uses a different inference protocol\"，但正文 §4.3 的 iso-compute 对比直接比较 27.97 vs 11.79 而未在对比句中重申 pipeline 差异。\n\n**[AGREE] R2-P4: bib key xu2026spon vs actual year**\n同意，与我自己的小问题一致。\n\n**[REBUT] R2-P5: 75.9M \"lightweight\" 标准不明确**\n不同意这是一个问题。论文 §3.2 明确给出了比较基准：\"less than 1% of the 8B base model\"。在 8B 模型上下文中，75.9M 占比 <1% 在 predictor-based sparsity 文献中属于标准量级（DejaVu 和 FastForward 的 predictor 规模相当）。\"Lightweight\" 的含义在上下文中是清晰的。\n\n---\n\n## Questions Q1-Q5\n\n**Q1: MaskLLM 直接迁移到 activation sparsity 的效果？**\n这是一个好问题，但超出了作者当前实验范围。MaskLLM 使用 Gumbel-Softmax 进行 per-group N:M categorical selection，直接迁移到 unstructured per-token activation sparsity 需要重新设计 mask generation 机制（从 categorical → binary）。但如果作者能展示 \"MaskLLM-style baseline\" 的表现，会大大增强 novelty 论证。建议作者在 revision 中补充此对比。\n\n**Q2: KL predictor 与 TEAL global top-k 是否根本不兼容？**\n[AGREE] 这是一个关键问题。Table 2 和 Table 5 的数据显示：在所有 sparsity 水平下，KL global 的 MMLU 都严重退化（30%: 25.27%, 40%: 38.06%, 50%: 27.89%）。如果 KL + global 在 downstream 上始终不可用，论文的 \"optimize for global allocation quality\" narrative 就存在根本矛盾。这个问题与我的 N2 和 R2 的 N3 直接相关。\n\n**Q3: Forward vs reverse KL 与 MiniLLM 结论矛盾？**\n[AGREE] 这是一个需要讨论的重要点。MiniLLM (Gu et al., ICLR 2024) 发现 reverse KL（避免 mode-averaging）在 LLM distillation 中更好，但本文 Table 3 显示 forward KL (11.79) > reverse KL (12.80)。两者的 context 不同（model distillation vs mask training），但论文应该讨论为什么结论相反——可能是因为 mask training 的 mode structure 与 model output distribution 不同，forward KL 的 mean-seeking 性质在 mask 优化中更有利（§3.4 简要提了一句 \"preserve the dense model's primary predictions\" 但未深入）。\n\n**Q4: 什么条件下 unstructured sparsity 能实现实际加速？**\n这是一个合理但超出论文范围的问题。论文 Limitations 已指出需要 \"Triton block-sparse, cuSPARSE\" 支持。当前 unstructured sparsity 在 GPU 上几乎无法加速是领域共识。\n\n**Q5: 三 regime 的精确边界？**\n[AGREE] 与我的 W1 和 R2 的 W3 一致。需要更细粒度的 sparsity sweep（35%, 45% 等）来定位 transition points。\n\n---\n\n## 总结\n\nR2 的审稿意见整体准确且有深度。在 13 个具体 issue 中，我 **同意 10 项**、**部分反驳 3 项**（W2 taxonomy、W6 domain overlap、P5 lightweight 标准）。\n\nR2 与我的审稿最大的共识在于：\n1. **Downstream collapse 是核心问题**（R2-N3 = 我的 N2）\n2. **Regime analysis 数据不足**（R2-W3 = 我的 W1）\n3. **实际效率缺失**（R2-N2 = 我的 W2）\n\nR2 提出而我未覆盖的最有价值的新观点是 **N1（与 MaskLLM 的 novelty 区分）** 和 **W4（missing references，特别是 MiniLLM）**。这两点我完全同意，会影响整体评分。\n\n结合 R2 的意见，我维持 **Overall 2.5/5 (Resubmit next cycle)** 的评分，可能下调至 2.0。核心障碍是 downstream 失效 + 数据不一致 + novelty 有限的组合。\n",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 249 · 2026-05-17T09:27:25.666568+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3920
}
```

</details>

---


### Assistant

_source line 250 · 2026-05-17T09:27:32.636344+00:00_

已提交对 Reviewer 2 全部意见的逐条回应。

总结：在 R2 的 13 个具体 issue 中，我同意 10 项（含 3 个 critical 全部同意），部分反驳 3 项（taxonomy 有组织价值、OOD relative advantage 保持、75.9M 在上下文中属 lightweight）。R2 提出的 MaskLLM novelty 问题和 MiniLLM missing reference 是我自己审稿未充分覆盖的重要新观点。维持 Overall 2.5/5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1"
}
```

</details>

---


## Round 10

## Round 10

38 recorded events


### User

_source line 251 · 2026-05-17T10:32:12.680875+00:00_

[Round 1 审稿请求]:
## 审稿任务 — Reviewer 1（方法严谨性 + 实验有效性）

### Venue 信息
- **目标**: EMNLP 2026 Main (ARR May 2026 cycle)
- **截止日期**: 2026-05-25
- **页数限制**: 长文 8 页正文（不含 limitations/ethics/references/appendix）
- **模板**: ACL 两栏 11pt (`\usepackage[review]{acl}`)
- **匿名规则**: Double-blind，论文中不得出现作者信息，自引不得暴露身份
- **附录规则**: 附录在 references 后，不计入页数，但审稿人可选择是否审阅

### 论文文件
- 主文件: `projects/distill_sparse_swiglu/paper/main.tex`
- 各章节: abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex
- 参考文献: references.bib
- PDF: `projects/distill_sparse_swiglu/paper/main.pdf`

### 你的审查侧重

**核心职责**: 评估方法的技术严谨性和实验的可信度。

请重点审查以下方面：

1. **梯度分析的严谨性**（§3.6 / §3.5）
   - BCE vs KL 梯度结构分析是否数学正确？
   - "structural mismatch" 的论证是否充分？是否存在 overclaim？
   - Gradient SNR 实验（80 steps, C4 data）的设置是否充分？统计显著性如何？

2. **KL vs BCE 对比的公平性**
   - BCE 使用 oracle masks (magnitude-based)，KL 使用 Gumbel-Sigmoid relaxation——训练目标和推理协议是否一致？
   - "137% worse PPL" 的 claim：BCE 和 KL 是否在完全相同条件下对比（架构、步数、数据、推理协议）？
   - Iso-compute analysis (§4.2): BCE 2700 steps vs KL 1000 steps 的对比是否足够公平？

3. **实验设置的可信度**
   - 仅使用 LLaMA-3.1-8B + Mistral-7B-v0.3（7-8B 规模）——泛化性声明是否过度？
   - 训练数据 WikiText-103 (1000 steps) 是否太小？
   - 单种子 vs 三种子：哪些结果是单种子的？variance 报告是否充分？
   - Downstream benchmarks（ARC-c, WG, MMLU, GSM8K）在 50% 稀疏度下全部崩溃——这是否削弱了核心 claim？

4. **消融实验的完整性**
   - Table 3 消融是否覆盖所有关键设计选择？
   - Gumbel vs STE 的对比是否孤立了正确的变量？
   - SPON orthogonality analysis 的 cosine similarity 0.196 是否充分支持 "near-orthogonal" claim？

5. **Adaptive Penalty Controller**
   - 数学表述是否正确？与标准 augmented Lagrangian 的区别是否说清？
   - 30% 和 70% 目标偏差 5%/1.7% 是否太大？对结果影响如何？

6. **数据一致性**
   - 表格间数据是否一致（同一实验在不同表格/文字中引用时数值是否一致）？
   - PPL 数据的小数精度是否统一？

### 输出格式

请按以下结构输出你的审稿意见：

```
## Summary
（2-3 句论文概述）

## Strengths
S1. ...
S2. ...

## Weaknesses
W1. [Must-Fix] ...
W2. [Should-Fix] ...
W3. [Minor] ...

## Questions
Q1. ...

## Missing References
（如有）

## Overall Assessment
评分: strong reject / weak reject / borderline / weak accept / strong accept
置信度: low / medium / high
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 252 · 2026-05-17T10:32:22.022686+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 253 · 2026-05-17T10:32:23.328191+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1305
}
```

</details>

---


### Tool call

_source line 254 · 2026-05-17T10:32:23.433823+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
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

_source line 255 · 2026-05-17T10:32:23.434344+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 256 · 2026-05-17T10:32:27.762236+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 257 · 2026-05-17T10:32:28.566103+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
  "pages": "1-5",
  "dpi": "180"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
    "pages": "1-5",
    "dpi": "180"
  }
}
```

</details>

---


### Tool result

_source line 258 · 2026-05-17T10:32:40.176291+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, exci
…[truncated 1347 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 12414
}
```

</details>

---


### Tool result

_source line 259 · 2026-05-17T10:32:42.759208+00:00_

Error: result (3,860,247 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/6c69ffa5-9f54-450f-85f8-c3341af2bbc4/tool-results/mcp-agent-ml-research-pdf_to_images-1779013962592.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/6c69ffa5-9f54-450f-85f8-c3341af2bbc4/tool-results/mcp-agent-ml-research-pdf_to_images-1779013962592.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 14193
}
```

</details>

---


### Tool call

_source line 260 · 2026-05-17T10:32:51.306245+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5), and descriptions for each score level. Include soundness, excitement, overall recommendation, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5), and descriptions for each score level. Include soundness, excitement, overall recommendation, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 261 · 2026-05-17T10:32:51.708223+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 262 · 2026-05-17T10:32:52.161631+00:00_

1	We study whether end-to-end KL distillation can replace per-neuron classification for activation sparsity prediction in SwiGLU LLMs.
2	Existing predictors trained with binary cross-entropy (BCE) optimize each neuron independently, but inference allocates sparsity budgets via global top-$k$ across all layers.
3	Gradient coupling analysis reveals a structural mismatch: BCE's per-neuron gradient is blind to cross-neuron interactions, achieving higher oracle F1 (0.613 vs.\ 0.540) yet 137\% worse perplexity.
4	A lightweight predictor (75.9M params, $<$1\% of base) trained with forward KL and Gumbel-Sigmoid relaxation resolves this mismatch by coupling all neurons through the output distribution.
5	On LLaMA-3.1-8B at 50\% sparsity with uniform per-layer allocation, the KL predictor achieves PPL 11.96 with MMLU 27.77\%, improving over magnitude-based TEAL (PPL 23.31); under global allocation, PPL drops further to 11.79 but late-layer starvation (L31 retention 28.4\%) degrades downstream tasks.
6	We identify three operating regions at the 7--8B scale (budget-surplus, budget-constrained, capacity-limited) that govern allocation-quality tradeoffs, with consistent KL-over-TEAL improvements on Mistral-7B-v0.3 (within 8\% ratio at $\leq$50\% sparsity).
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 263 · 2026-05-17T10:32:52.162127+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 264 · 2026-05-17T10:32:52.212740+00:00_

1	\section{Introduction}
2	
3	SwiGLU feed-forward networks~\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they universally rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: TEAL's top-$k$ mechanism~\cite{liu2025teal} ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	
8	We provide this analysis.
9	The gradient of BCE with respect to neuron $j$'s score is $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$, a function of $j$ alone, independent of every other neuron.
10	Under KL divergence, the gradient for neuron $j$ in layer $\ell$ factors as:
11	\begin{equation*}
12	\frac{\partial \mathcal{L}_{\text{KL}}}{\partial s_j^{(\ell)}} = \frac{\partial \mathcal{L}_{\text{KL}}}{\partial \mathbf{z}} \cdot \frac{\partial \mathbf{z}}{\partial \mathbf{h}^{(\ell)}} \cdot \frac{\partial \mathbf{h}^{(\ell)}}{\partial \tilde{m}_j^{(\ell)}} \cdot \frac{\partial \tilde{m}_j^{(\ell)}}{\partial s_j^{(\ell)}},
13	\end{equation*}
14	where the Jacobian $\partial \mathbf{z} / \partial \mathbf{h}^{(\ell)}$ propagates through all downstream layers, coupling each neuron's gradient to every other neuron's mask state.
15	This structural difference predicts that KL should outperform BCE specifically under global allocation, and the prediction is confirmed empirically: BCE achieves higher oracle F1 (0.613 vs.\ 0.540) yet produces 137\% worse perplexity, because per-neuron magnitude accuracy is a misaligned proxy for output-distribution preser
…[truncated 1998 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 265 · 2026-05-17T10:33:00.204414+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully"
- **4**: "Quite sure. I tried to check the important points carefully"
- **3**: "Pretty sure, but there's a chance I missed something"
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- **1**: "Not my area, or paper is very hard to understand"

## 2. **Soundness**
Scale: 1-5 (with half-point options)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: "Strong: This study provides sufficient support for all claims"
- **3**: "Acceptable: This study provides sufficient support for main claims"
- **2**: "Poor: Some main claims are not sufficiently supported"
- **1**: "Major Issues: This study is not yet sufficiently thorough"

## 3. **Excitement**
Scale: 1-5 (with half-point options)
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: "Exciting: I would mention this paper to others"
- **3**: "Interesting: I might mention some points of this paper"
- **2**: "Potentially Interesting: does not resonate with me"
- **1**: "Not Exciting: does not resonate with me"

## 4. **Overall Assessment**
Scale: 1-5 (with half-point options)
- **5**: Consider for Award (top 2.5% papers)
- **4**: Conference acceptance recommendation
- **3**: Findings track acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit

## 5. **Reproducibility**
Scale: 1-5
- **5**: "They could easily reproduce the results"
- **3**: "They could reproduce the results with some difficulty"
- **1**: "They would not be able to reproduce the results"

## 6. **Datasets & Software**
Each: Scale 1-5
- **5**: "Enabling" impact on research choices
- **4**: "Useful" for ongoing work
- **3**: "Potentially useful"
- **1**: No usable materials submitted

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8898
}
```

</details>

---


### Tool call

_source line 266 · 2026-05-17T10:33:04.179136+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 267 · 2026-05-17T10:33:04.330462+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models.
5	The method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass, eliminating the need for auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{h}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importance scores from the pre-FFN hidden state $\mathbf{h}$.
26
…[truncated 14269 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 268 · 2026-05-17T10:33:04.381491+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 269 · 2026-05-17T10:33:04.432336+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4, using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $5 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly; (2) \textbf{BCE predictor}, trained with per-neuron binary cross-entropy loss for 1000 and 2700 steps; (3) \textbf{Uniform allocation}, which distributes the sparsity budget equally across layers; and (4) \textbf{WINA}~\cite{liu2025teal}, an importance-weighted variant.
23	
24	
25
…[truncated 14326 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 270 · 2026-05-17T10:33:09.957566+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 271 · 2026-05-17T10:33:10.914912+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude, achieving 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking.
6	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
7	
8	\paragraph{Predictor-Based Contextual Sparsity.}
9	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
10	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision, providing intermediate coupling within each layer but no end-to-end gradient signal.
11	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
12	PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.
13	MaskLLM~\cite{fang2024maskllm} also employs learnable masks with Gumbel relaxation and frozen weights, but targets N:M semi-structured \emph{weight} sparsity (2:4 patterns) via per-group categorical selection (Gumbel-Softmax), producing fixed masks independent of input tokens.
14	Both share the principle of frozen weights + learnable masks + KL training, but solve distinct optimization problems: MaskLLM finds optimal static N:M patterns within fixed groups, while we predict dynamic per-token masks under a global budget constraint.
15	The structural mismatch we identify (per-neuron gradient decomposition vs.\ global top-$k$) does not arise in MaskLLM's per-group categorical setting, where N:M patterns
…[truncated 2689 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 272 · 2026-05-17T10:33:10.965603+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 273 · 2026-05-17T10:33:11.016225+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that KL distillation resolves the structural mismatch between per-neuron BCE training and global top-$k$ inference allocation in SwiGLU sparsity prediction.
5	The coupled gradient signal enables a lightweight predictor (75.9M params, $<$1\% of base) to achieve PPL 11.79 at 50\% sparsity vs.\ 23.31 for TEAL, with consistent improvements on both LLaMA-3.1-8B and Mistral-7B-v0.3 (within 8\% ratio consistency at $\leq$50\% sparsity).
6	Analysis of allocation strategies reveals that global top-$k$ starves late layers, degrading downstream tasks, while uniform allocation recovers performance comparable to TEAL, confirming that allocation strategy rather than predictor quality is the primary bottleneck.
7	
8	Open directions include scaling to 13B--70B models to test generality beyond 7--8B, adaptive per-layer allocation that bridges the global-PPL and uniform-downstream gap, and downstream-aware training objectives that directly optimize task accuracy rather than output-distribution fidelity.
9	
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 274 · 2026-05-17T10:33:11.016568+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-17T10:33:11.117729+00:00_

1	\section*{Limitations}
2	
3	Our primary evaluation uses WikiText-2 perplexity, and downstream benchmarks reveal that perplexity is a poor proxy for reasoning ability at moderate sparsity: 40\% sparsity achieves PPL 8.36 but MMLU already degrades, motivating 30\% as the recommended operating point for downstream fidelity.
4	Training requires 1000 steps on WikiText-103 ($\sim$45 minutes on RTX PRO 6000 for KL, $\sim$17 minutes for BCE), but a separate predictor must be trained for each sparsity target.
5	All experiments use 7--8B parameter models (LLaMA-3.1-8B, Mistral-7B-v0.3); scaling behavior to 13B or 70B models remains untested.
6	Out-of-distribution evaluation (Appendix~\ref{app:ood}) covers only 50\% sparsity on C4; extending to 30\% and 70\% is left to future work.
7	While we motivate our work with inference speedup potential, actual wall-clock acceleration depends on sparse kernel implementations (e.g., Triton, cuSPARSE) and hardware-specific memory access patterns; this work focuses on prediction quality rather than systems optimization.
8	Future directions include N:M structured sparsity for hardware-native acceleration, scaling to 13B+ models, and training a single predictor that serves multiple sparsity targets simultaneously.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 276 · 2026-05-17T10:33:14.130273+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 277 · 2026-05-17T10:33:14.181298+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling), confirming that KL distillation provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overh
…[truncated 8907 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 278 · 2026-05-17T10:33:18.399785+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 279 · 2026-05-17T10:33:18.751832+00:00_

1	\section*{Ethics Statement}
2	
3	This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, MMLU, GSM8K).
4	No new data collection, annotation, or human subjects are involved.
5	The method does not alter model outputs beyond the sparsity-induced degradation we analyze; it introduces no new generation capabilities or safety risks beyond those inherent in the base models.
6	Compute requirements are modest (1000 training steps, $\sim$45 minutes on a single GPU for KL training), presenting minimal environmental concern relative to the pretrained models we evaluate on.
7	We release no model weights or user-facing systems; our contribution is analytical (understanding KL distillation for sparsity) rather than deployment-oriented.
8	
9	\section*{Responsible NLP Research Checklist}
10	
11	\paragraph{A. Limitations and Risks.}
12	\begin{itemize}[nosep,leftmargin=*]
13	\item[\textbf{A1.}] Limitations are discussed in the Limitations section. Key limitations: evaluation limited to 7--8B models; perplexity is an imperfect proxy for downstream quality; wall-clock speedup requires sparse kernel support not implemented here.
14	\item[\textbf{A2.}] No foreseeable risks specific to this work beyond those inherent in the base language models. The method does not enable new capabilities or applications.
15	\end{itemize}
16	
17	\paragraph{B. Scientific Artifacts.}
18	\begin{itemize}[nosep,leftmargin=*]
19	\item[\textbf{B1.}] Yes. All models (LLaMA-3.1-8B~\cite{grattafiori2024llama3}, Mistral-7B-v0.3~\cite{jiang2023mistral}), datasets (WikiText~\cite{merity2017pointer}, C4~\cite{raffel2020c4}), and methods (TEAL~\cite{liu2025teal}, SPON~\cite{xu2026spon}) are cited with original references.
20	\item[\textbf{B2.}] LLaMA-3.1 is released under the Llama 3.1 Community License; Mistral-7B under Apache 2.0. WikiText a
…[truncated 1816 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 280 · 2026-05-17T10:33:18.802558+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 281 · 2026-05-17T10:33:18.853895+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	
17	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
18	
19	\author{Anonymous}
20	
21	\begin{document}
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
32	\input{conclusion}
33	\input{limitations}
34	\input{ethics}
35	
36	\bibliography{references}
37	
38	\input{appendix}
39	
40	\end{document}
41	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 282 · 2026-05-17T10:34:12.578661+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the detailed reviewer guidelines including: what makes a good/poor review, scoring guidance for soundness and excitement, what counts as a weakness vs strength, how to evaluate reproducibility, and any guidance on experimental rigor expectations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the detailed reviewer guidelines including: what makes a good/poor review, scoring guidance for soundness and excitement, what counts as a weakness vs strength, how to evaluate reproducibility, and any guidance on experimental rigor expectations."
  }
}
```

</details>

---


### Tool call

_source line 283 · 2026-05-17T10:34:12.880536+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 284 · 2026-05-17T10:34:13.082818+00:00_

1	% =============================================================================
2	% Direction 1: KL distillation for structured/activation sparsity
3	% =============================================================================
4	
5	@inproceedings{fang2024maskllm,
6	  title = {MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models},
7	  author = {Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff Pool and Jan Kautz and Pavlo Molchanov and Xinchao Wang},
8	  year = {2024},
9	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
10	  url = {https://arxiv.org/abs/2409.17481},
11	}
12	
13	@inproceedings{xu2026spon,
14	  title = {Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models},
15	  author = {Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma},
16	  year = {2025},
17	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
18	  url = {https://arxiv.org/abs/2512.12744},
19	}
20	
21	@inproceedings{muralidharan2024minitron,
22	  title = {Compact Language Models via Pruning and Knowledge Distillation},
23	  author = {Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marcin Chochowski and Mostofa Patwary and Mohammad Shoeybi and Bryan Catanzaro and Jan Kautz and Pavlo Molchanov},
24	  year = {2024},
25	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
26	  url = {https://arxiv.org/abs/2407.14679},
27	}
28	
29	
30	% =============================================================================
31	% Direction 3: SPON and learnable bias correction for sparsity
32	% =============================================================================
33	
34	@article{gautam2026fastforward,
35	  title = {Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity},
36	  author = {Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott and Naras
…[truncated 14316 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 202
}
```

</details>

---


### Tool result

_source line 285 · 2026-05-17T10:34:24.734050+00:00_

# ARR Reviewer Guidelines: Standards for Quality Reviews

## What Makes a Good Review

**Specificity and Clarity**: Reviews must be concrete rather than vague. Instead of "The paper is missing relevant references," specify "The paper is missing references X, Y, and Z." This enables area chairs to understand concerns without reading the full paper.

**Professional Tone**: "Write the review you would like to get yourself." Reviews should be helpful and kind, recognizing that authors may be early-career researchers facing stress. Sarcasm and dismissiveness undermine the collaborative spirit of peer review.

**Justified Scores**: "If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation."

## Scoring Guidance

**Soundness**: Technical correctness and methodological validity. This score must align directly with identified flaws in your review text.

**Excitement**: Personal interest in the topic—orthogonal to soundness. A technically sound paper addressing a niche topic may receive low excitement while maintaining high soundness.

**Overall Assessment**: A composite judgment reflecting soundness, excitement, novelty, and potential impact. Papers need sufficient soundness for acceptance, but personal excitement isn't required.

## Common Review Problems to Avoid

The guidelines identify 17 heuristics that sound like weaknesses but often reflect reviewer bias:

- **H1-H4**: Dismissing results as "obvious" or "lacking precedent"
- **H5**: Criticizing lack of SOTA when authors don't claim SOTA
- **H6**: Unfair bias against negative results
- **H7-H8**: Preferring complexity or specific methodologies unnecessarily
- **H9-H10**: Dismissing niche topics or non-English work
- **H13**: Demanding experiments beyond what claims require

## Weakness vs. Strength Distinctions

**Not Weaknesses**:
- Authors choosing a different methodology than you would prefer
- Acknowledged limitations (unles
…[truncated 1626 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 12155
}
```

</details>

---


### Tool call

_source line 286 · 2026-05-17T10:36:59.759783+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Summary\n\n本文分析了 SwiGLU LLM 中 per-neuron BCE 训练与 global top-k 推理之间的结构性不匹配，提出用 forward KL 蒸馏 + Gumbel-Sigmoid 松弛训练轻量级稀疏预测器。在 LLaMA-3.1-8B 和 Mistral-7B-v0.3 上验证了 KL 在 PPL 指标上优于 TEAL 和 BCE baseline，并分析了分配策略如何影响下游任务表现。\n\n---\n\n## Strengths\n\n**S1. 梯度结构分析提供了有价值的理论洞察（§3.6）**\nBCE 梯度 per-neuron 独立、KL 梯度通过 Jacobian 耦合所有 neuron 的分析在数学上是正确的，chain rule 分解清晰。这为选择 KL 目标提供了原则性动机，而非仅靠经验对比。\n\n**S2. 实验设计系统且消融充分（§4.3, Table 3）**\n消融覆盖了 divergence 方向（forward/reverse KL/JSD）、松弛方式（Gumbel vs STE）、loss function 隔离（BCE+Gumbel+Penalty），每个 design choice 的贡献量化清晰。Loss effect (6.6×) vs relaxation effect 的分解有信息量。\n\n**S3. 三操作区域分析具有实用价值（§4.4, Table 4）**\nBudget-surplus/constrained/capacity-limited 的区分为实际部署提供了指导，且在两个模型上验证了一致性。global vs uniform allocation 的 non-monotonic preference 是一个非 trivial 的发现。\n\n**S4. 论文诚实报告了负面结果**\n50% sparsity 下游崩溃、penalty controller 的偏差、PPL 与下游任务的脱节——这些局限性被坦诚讨论，增加了结果可信度。\n\n**S5. 方法简洁，无 compensation network**\n消除了 FastForward 式的补偿网络，predictor 参数 <1% base model，推理流程简化。\n\n---\n\n## Weaknesses\n\n**W1. [Must-Fix] Iso-compute 对比存在严重不公平（§4.2）**\n\n论文声称 BCE 2700 steps 与 KL 1000 steps 是 \"iso-compute\" 对比（2.71×），但完全忽略了 per-step 计算成本的巨大差异：\n- KL 训练每步需要：dense forward pass（获取 target logits）+ sparse forward pass（经过 Gumbel masks 的完整前向）+ backward through the entire base model（虽然 frozen，但梯度需流经所有下游层以计算 mask 梯度 factor (b)）\n- BCE 训练每步仅需：一次 forward pass 获取 oracle masks + predictor forward + backward through predictor only\n\nKL 每步的实际 FLOP 远高于 BCE（至少 3-5×，因为需要 full backward through 8B model）。真正的 iso-compute 应该让 BCE 训练 8000-13000 steps。当前 2700 steps 的 \"iso-compute\" 表述是误导性的。\n\n建议：(1) 明确报告两种训练的 wall-clock time 和 GPU memory（Limitations 提到 KL 45min vs BCE 17min，即 2.65× per-step cost，这意味着 iso-compute 应让 BCE 运行约 7000 steps）；(2) 或修改措辞为 \"extended training\" 而非 \"iso-compute\"。\n\n**W2. [Must-Fix] BCE baseline 的 oracle 选择使对比不公平，coupling 论证存在混淆（§3.6, §4.2）**\n\n核心论证存在一个未讨论的混淆因素：\n\n- BCE 训练的 oracle masks 来自 activation magnitude (m_j* = 1[|g_j| >= global threshold])\n- KL 直接优化 output distribution preservation\n\n论文将 KL 的优势归因于 \"gradient coupling\"（factor (b)），但存在另一个完全不同的解释：magnitude-based oracle 本身就是 output preservation 的 poor proxy。即使 BCE 有完美的 \"coupling\"，如果 oracle 本身与 PPL 不对齐，也不会得到好的 PPL。\n\n具体证据：BCE oracle F1 = 0.613（即完美匹配 magnitude oracle），但 PPL 仍然差。这说明问题可能不在于 \"gradient coupling\" 而在于 oracle 质量本身——用 magnitude 定义的 \"重要\" 与用 output distribution 定义的 \"重要\" 是不同的东西。\n\n要真正证明 \"coupling\" 是关键因素，需要一个 ablation：用 KL-optimal masks 作为 BCE oracle（而非 magnitude-based masks），看 BCE 在该 oracle 下能否缩小与 KL 的差距。如果 BCE + better oracle 仍然差很多，才能证明 coupling 是核心因素。\n\n**W3. [Must-Fix] 50% sparsity 下游完全崩溃，削弱核心实用性主张（Table 1, §4.1）**\n\n50% sparsity（论文展示最大 PPL 优势的区间）：\n- MMLU: 27.89% (global) / 27.77% (uniform) ≈ 随机（25%）\n- GSM8K: <2.2% 所有方法\n\n这意味着 KL predictor 在 50% sparsity 虽然 PPL 好很多（11.79 vs 23.31），但模型的实际能力已完全丧失。PPL 的改善没有转化为任何有意义的下游能力保持。\n\n在唯一有意义下游表现的 30% sparsity：\n- KL uniform PPL 8.82 vs TEAL 10.97（19% improvement，不是 dramatic）\n- MMLU: 40.61% vs TEAL 38.61%（仅 +2pp）\n\n这意味着论文的核心卖点（\"49% PPL reduction\"）发生在一个实际无用的区间。论文承认了这一点但仍以 50% 结果为主要展示。Introduction 和 Abstract 应更突出 30% 为推荐操作点以及该操作点下相对温和的改善幅度。\n\n**W4. [Should-Fix] Gradient SNR 实验统计力度不足（§3.6）**\n\n- 仅 80 steps，无 error bars，无统计显著性检验\n- SNR 绝对值极低（5.77×10⁻⁵ vs 1.00×10⁻⁵），两者都接近零——质疑这些梯度信号是否实际有用\n- \"Early-layer BCE SNR collapses to ~10⁻⁸ after step 10\"——这是一个重大声明但缺乏验证：为什么 collapse？是 vanishing gradient 还是 convergence？如果 BCE 已经在 10 步内拟合了 oracle masks，SNR 应该下降（因为 loss 已很小）\n- 建议：报告 95% CI 或 bootstrap intervals，增加到至少 200-500 steps 覆盖不同训练阶段\n\n**W5. [Should-Fix] 大部分结果为 single-seed，稳定性评估不充分（Table 1 note, Appendix E）**\n\n- 仅 50% uniform 有 3-seed 评估（PPL 11.92±0.07）\n- 30%、70%、cross-arch、iso-compute 等核心结果全部 single-seed\n- Gumbel sampling 的随机性可能导致不同 seed 下显著差异，尤其在极端 sparsity（70%）下\n- 这在 ARR 标准下属于 reproducibility 扣分项\n\n**W6. [Should-Fix] \"Near-orthogonal\" 声称缺乏依据（§4.5）**\n\nCosine similarity = 0.196 被描述为 \"near-orthogonal\"。在数学上，orthogonal 意味着 cosine = 0。0.196 表示约 11° 偏离正交（arccos(0.196) ≈ 79°，正交为 90°）。这不是 \"near-orthogonal\"，这是 \"低相关但非正交\"。\n\n高维空间中随机向量的 expected cosine similarity 约为 0（stddev ≈ 1/√d），所以 0.196 在高维中其实是 statistically significant 的非零相关。建议改为 \"weakly correlated\" 或提供随机 baseline 的 cosine distribution 作对比。\n\n**W7. [Should-Fix] Adaptive penalty 30% target 偏差 5% 未讨论对实验结果的影响（Appendix B, Table 7）**\n\n30% target 实际达到 28.5%（偏差 5%）。TEAL vanilla 在 30% 报告 PPL 10.97——那在 28.5% sparsity 下 TEAL 的 PPL 是多少？如果 TEAL 在 28.5% 也明显更好，则 KL 的优势被高估（因为它实际上在更低的 sparsity 下运行）。\n\n建议：报告 TEAL 在实际达成的 sparsity level（28.5%）下的 PPL，或说明影响可忽略。\n\n**W8. [Should-Fix] Training/evaluation 数据同源性（§4.1）**\n\nWikiText-103 训练 → WikiText-2 评估。这两个数据集来自同一来源（Wikipedia），vocabulary 和 domain 高度重叠。OOD 评估（Appendix D）仅覆盖 50% sparsity 下的 C4，未覆盖 30%（推荐操作点）。建议在 30% sparsity 下也报告 C4 PPL。\n\n**W9. [Minor] Table 1 中 BCE 行标注 \"different inference protocol\" 但解释不充分**\n\n注释说 \"BCE uses a different inference protocol (hard mask + compensation network)\"，但正文 §4.2 的 iso-compute 比较中 BCE 使用的是 TEAL allocation（无 compensation），而 Table 1 row \"BCE (2700 steps)\" 标了 asterisk 说用了不同协议。这导致混淆：iso-compute 分析中 BCE 的 PPL 27.97 是 with compensation 还是 without？从 Table 3 看，\"BCE (no compensation)\" = 27.97, \"BCE + Compensation\" = 25.44——Table 1 的 27.97 应该是 no compensation 版本但标注说 \"different protocol\"，不一致。\n\n**W10. [Minor] Scale 限制的 generalization claims 需要更谨慎措辞**\n\n论文多处使用 \"at the 7-8B scale\" 作为 qualifier，这很好。但 conclusion 中 \"open directions include scaling to 13B-70B\" 暗示当前发现可能 generalize。考虑到 SwiGLU activation distribution 随 model size 变化（cf. Sparsing Law），当前结论严格限于 7-8B。\n\n**W11. [Minor] Forward KL 方向选择的理由偏弱（§3.4）**\n\n\"The goal is to preserve the dense model's primary predictions rather than explore alternative modes\" 是正确的直觉，但实验中 forward KL 仅优于 reverse KL 1.01 PPL（8.6%），优于 JSD 0.75 PPL（6.4%）——这些差异在缺乏 error bars 的情况下是否可靠？\n\n---\n\n## Questions\n\n**Q1.** KL 每步的实际 GPU wall-clock time 和 peak memory 是多少？BCE 每步的对应数据是多少？Limitations 提到 KL 45min vs BCE 17min for 1000 steps——这意味着 KL 每步成本约 2.65× BCE，若给 BCE 同等 wall-clock (2650 steps)，PPL 能降到多少？\n\n**Q2.** 如果用 KL-trained predictor 的 hard masks 作为 BCE 的 oracle target（而非 magnitude-based masks），BCE 能否缩小差距？这能分离 \"coupling\" 效应和 \"oracle quality\" 效应。\n\n**Q3.** Table 3 中 \"BCE + Gumbel + Penalty\" (PPL 38.02) 比 vanilla BCE (27.97) 还差——这意味着 Gumbel+Penalty 框架不是通用的改进而是 KL-specific 的。请解释为什么 Gumbel 帮助了 KL 却伤害了 BCE？这是否暗示优势来自 loss function 与 relaxation 的 interaction 而非纯粹的 coupling？\n\n**Q4.** 30% sparsity 下 penalty 达到 λ_max=5000 且偏差 5%——这是否意味着 SwiGLU 的 natural activation density 与 30% target 不兼容，训练实际上在对抗网络的内在分布？\n\n**Q5.** Gradient SNR 中 \"BCE early-layer SNR collapses to ~10⁻⁸ after step 10\"——这是否因为 BCE 在 10 步内已对 oracle masks 过拟合（loss 接近 0 → gradient 接近 0）？如果是，这不是缺陷而是收敛。\n\n---\n\n## Missing References\n\n- **ThunderKittens / FlashInfer** — sparse kernel implementations，与 wall-clock speedup 讨论相关\n- **Deja Vu++ / Brain-inspired Sparse Training** — 更近期的 predictor-based sparsity 工作（如果存在）\n- 当前引用覆盖度尚可（26篇），但缺少 hardware-aware pruning 方向的引用（如 nm-sparsity 的 Nvidia 工作）\n\n---\n\n## Overall Assessment\n\n**Soundness: 3/5 (Acceptable)**\n梯度分析数学正确但论证存在混淆（W2）；iso-compute claim 有误导性（W1）；核心实验单 seed（W5）。主要 claims 有支撑但关键对比的 fairness 存在问题。\n\n**Excitement: 3/5 (Interesting)**\n问题定义有价值（BCE vs KL for sparsity prediction 是实际存在的设计选择），三操作区域分析有实用意义。但 50% 下游崩溃和 30% 下温和改善限制了实际影响力。\n\n**Reproducibility: 3.5/5**\n超参完整报告，架构细节充分，但大部分结果单 seed 且缺少代码承诺。\n\n**Overall: 2.5 (Borderline: between Resubmit and Findings)**\n\n核心问题：(1) iso-compute claim 不公平需要修正或重新措辞；(2) coupling vs oracle-quality 的因果分离不足，核心叙事 \"structural mismatch → KL solves it via coupling\" 可能是 overclaim；(3) 实际可用区间（30%）的改善幅度温和（PPL 19%, MMLU +2pp）。\n\n如果作者能够：修正 iso-compute 表述、增加 oracle-quality ablation、在 30% 补充 multi-seed + OOD 评估，论文有望达到 Findings 水平。当前版本的 overclaim 和实验 gaps 使其处于 borderline 状态。\n\n**置信度: High (4/5)**\n我仔细检查了梯度推导、数值计算和实验逻辑。对 sparsity prediction 和 KL distillation 文献有较好了解。",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Summary\n\n本文分析了 SwiGLU LLM 中 per-neuron BCE 训练与 global top-k 推理之间的结构性不匹配，提出用 forward KL 蒸馏 + Gumbel-Sigmoid 松弛训练轻量级稀疏预测器。在 LLaMA-3.1-8B 和 Mistral-7B-v0.3 上验证了 KL 在 PPL 指标上优于 TEAL 和 BCE baseline，并分析了分配策略如何影响下游任务表现。\n\n---\n\n## Strengths\n\n**S1. 梯度结构分析提供了有价值的理论洞察（§3.6）**\nBCE 梯度 per-neuron 独立、KL 梯度通过 Jacobian 耦合所有 neuron 的分析在数学上是正确的，chain rule 分解清晰。这为选择 KL 目标提供了原则性动机，而非仅靠经验对比。\n\n**S2. 实验设计系统且消融充分（§4.3, Table 3）**\n消融覆盖了 divergence 方向（forward/reverse KL/JSD）、松弛方式（Gumbel vs STE）、loss function 隔离（BCE+Gumbel+Penalty），每个 design choice 的贡献量化清晰。Loss effect (6.6×) vs relaxation effect 的分解有信息量。\n\n**S3. 三操作区域分析具有实用价值（§4.4, Table 4）**\nBudget-surplus/constrained/capacity-limited 的区分为实际部署提供了指导，且在两个模型上验证了一致性。global vs uniform allocation 的 non-monotonic preference 是一个非 trivial 的发现。\n\n**S4. 论文诚实报告了负面结果**\n50% sparsity 下游崩溃、penalty controller 的偏差、PPL 与下游任务的脱节——这些局限性被坦诚讨论，增加了结果可信度。\n\n**S5. 方法简洁，无 compensation network**\n消除了 FastForward 式的补偿网络，predictor 参数 <1% base model，推理流程简化。\n\n---\n\n## Weaknesses\n\n**W1. [Must-Fix] Iso-compute 对比存在严重不公平（§4.2）**\n\n论文声称 BCE 2700 steps 与 KL 1000 steps 是 \"iso-compute\" 对比（2.71×），但完全忽略了 per-step 计算成本的巨大差异：\n- KL 训练每步需要：dense forward pass（获取 target logits）+ sparse forward pass（经过 Gumbel masks 的完整前向）+ backward through the entire base model（虽然 frozen，但梯度需流经所有下游层以计算 mask 梯度 factor (b)）\n- BCE 训练每步仅需：一次 forward pass 获取 oracle masks + predictor forward + backward through predictor only\n\nKL 每步的实际 FLOP 远高于 BCE（至少 3-5×，因为需要 full backward through 8B model）。真正的 iso-compute 应该让 BCE 训练 8000-13000 steps。当前 2700 steps 的 \"iso-compute\" 表述是误导性的。\n\n建议：(1) 明确报告两种训练的 wall-clock time 和 GPU memory（Limitations 提到 KL 45min vs BCE 17min，即 2.65× per-step cost，这意味着 iso-compute 应让 BCE 运行约 7000 steps）；(2) 或修改措辞为 \"extended training\" 而非 \"iso-compute\"。\n\n**W2. [Must-Fix] BCE baseline 的 oracle 选择使对比不公平，coupling 论证存在混淆（§3.6, §4.2）**\n\n核心论证存在一个未讨论的混淆因素：\n\n- BCE 训练的 oracle masks 来自 activation magnitude (m_j* = 1[|g_j| >= global threshold])\n- KL 直接优化 output distribution preservation\n\n论文将 KL 的优势归因于 \"gradient coupling\"（factor (b)），但存在另一个完全不同的解释：magnitude-based oracle 本身就是 output preservation 的 poor proxy。即使 BCE 有完美的 \"coupling\"，如果 oracle 本身与 PPL 不对齐，也不会得到好的 PPL。\n\n具体证据：BCE oracle F1 = 0.613（即完美匹配 magnitude oracle），但 PPL 仍然差。这说明问题可能不在于 \"gradient coupling\" 而在于 oracle 质量本身——用 magnitude 定义的 \"重要\" 与用 output distribution 定义的 \"重要\" 是不同的东西。\n\n要真正证明 \"coupling\" 是关键因素，需要一个 ablation：用 KL-optimal masks 作为 BCE oracle（而非 magnitude-based masks），看 BCE 在该 oracle 下能否缩小与 KL 的差距。如果 BCE + better oracle 仍然差很多，才能证明 coupling 是核心因素。\n\n**W3. [Must-Fix] 50% sparsity 下游完全崩溃，削弱核心实用性主张（Table 1, §4.1）**\n\n50% sparsity（论文展示最大 PPL 优势的区间）：\n- MMLU: 27.89% (global) / 27.77% (uniform) ≈ 随机（25%）\n- GSM8K: <2.2% 所有方法\n\n这意味着 KL predictor 在 50% sparsity 虽然 PPL 好很多（11.79 vs 23.31），但模型的实际能力已完全丧失。PPL 的改善没有转化为任何有意义的下游能力保持。\n\n在唯一有意义下游表现的 30% sparsity：\n- KL uniform PPL 8.82 vs TEAL 10.97（19% improvement，不是 dramatic）\n- MMLU: 40.61% vs TEAL 38.61%（仅 +2pp）\n\n这意味着论文的核心卖点（\"49% PPL reduction\"）发生在一个实际无用的区间。论文承认了这一点但仍以 50% 结果为主要展示。Introduction 和 Abstract 应更突出 30% 为推荐操作点以及该操作点下相对温和的改善幅度。\n\n**W4. [Should-Fix] Gradient SNR 实验统计力度不足（§3.6）**\n\n- 仅 80 steps，无 error bars，无统计显著性检验\n- SNR 绝对值极低（5.77×10⁻⁵ vs 1.00×10⁻⁵），两者都接近零——质疑这些梯度信号是否实际有用\n- \"Early-layer BCE SNR collapses to ~10⁻⁸ after step 10\"——这是一个重大声明但缺乏验证：为什么 collapse？是 vanishing gradient 还是 convergence？如果 BCE 已经在 10 步内拟合了 oracle masks，SNR 应该下降（因为 loss 已很小）\n- 建议：报告 95% CI 或 bootstrap intervals，增加到至少 200-500 steps 覆盖不同训练阶段\n\n**W5. [Should-Fix] 大部分结果为 single-seed，稳定性评估不充分（Table 1 note, Appendix E）**\n\n- 仅 50% uniform 有 3-seed 评估（PPL 11.92±0.07）\n- 30%、70%、cross-arch、iso-compute 等核心结果全部 single-seed\n- Gumbel sampling 的随机性可能导致不同 seed 下显著差异，尤其在极端 sparsity（70%）下\n- 这在 ARR 标准下属于 reproducibility 扣分项\n\n**W6. [Should-Fix] \"Near-orthogonal\" 声称缺乏依据（§4.5）**\n\nCosine similarity = 0.196 被描述为 \"near-orthogonal\"。在数学上，orthogonal 意味着 cosine = 0。0.196 表示约 11° 偏离正交（arccos(0.196) ≈ 79°，正交为 90°）。这不是 \"near-orthogonal\"，这是 \"低相关但非正交\"。\n\n高维空间中随机向量的 expected cosine similarity 约为 0（stddev ≈ 1/√d），所以 0.196 在高维中其实是 statistically significant 的非零相关。建议改为 \"weakly correlated\" 或提供随机 baseline 的 cosine distribution 作对比。\n\n**W7. [Should-Fix] Adaptive penalty 30% target 偏差 5% 未讨论对实验结果的影响（Appendix B, Table 7）**\n\n30% target 实际达到 28.5%（偏差 5%）。TEAL vanilla 在 30% 报告 PPL 10.97——那在 28.5% sparsity 下 TEAL 的 PPL 是多少？如果 TEAL 在 28.5% 也明显更好，则 KL 的优势被高估（因为它实际上在更低的 sparsity 下运行）。\n\n建议：报告 TEAL 在实际达成的 sparsity level（28.5%）下的 PPL，或说明影响可忽略。\n\n**W8. [Should-Fix] Training/evaluation 数据同源性（§4.1）**\n\nWikiText-103 训练 → WikiText-2 评估。这两个数据集来自同一来源（Wikipedia），vocabulary 和 domain 高度重叠。OOD 评估（Appendix D）仅覆盖 50% sparsity 下的 C4，未覆盖 30%（推荐操作点）。建议在 30% sparsity 下也报告 C4 PPL。\n\n**W9. [Minor] Table 1 中 BCE 行标注 \"different inference protocol\" 但解释不充分**\n\n注释说 \"BCE uses a different inference protocol (hard mask + compensation network)\"，但正文 §4.2 的 iso-compute 比较中 BCE 使用的是 TEAL allocation（无 compensation），而 Table 1 row \"BCE (2700 steps)\" 标了 asterisk 说用了不同协议。这导致混淆：iso-compute 分析中 BCE 的 PPL 27.97 是 with compensation 还是 without？从 Table 3 看，\"BCE (no compensation)\" = 27.97, \"BCE + Compensation\" = 25.44——Table 1 的 27.97 应该是 no compensation 版本但标注说 \"different protocol\"，不一致。\n\n**W10. [Minor] Scale 限制的 generalization claims 需要更谨慎措辞**\n\n论文多处使用 \"at the 7-8B scale\" 作为 qualifier，这很好。但 conclusion 中 \"open directions include scaling to 13B-70B\" 暗示当前发现可能 generalize。考虑到 SwiGLU activation distribution 随 model size 变化（cf. Sparsing Law），当前结论严格限于 7-8B。\n\n**W11. [Minor] Forward KL 方向选择的理由偏弱（§3.4）**\n\n\"The goal is to preserve the dense model's primary predictions rather than explore alternative modes\" 是正确的直觉，但实验中 forward KL 仅优于 reverse KL 1.01 PPL（8.6%），优于 JSD 0.75 PPL（6.4%）——这些差异在缺乏 error bars 的情况下是否可靠？\n\n---\n\n## Questions\n\n**Q1.** KL 每步的实际 GPU wall-clock time 和 peak memory 是多少？BCE 每步的对应数据是多少？Limitations 提到 KL 45min vs BCE 17min for 1000 steps——这意味着 KL 每步成本约 2.65× BCE，若给 BCE 同等 wall-clock (2650 steps)，PPL 能降到多少？\n\n**Q2.** 如果用 KL-trained predictor 的 hard masks 作为 BCE 的 oracle target（而非 magnitude-based masks），BCE 能否缩小差距？这能分离 \"coupling\" 效应和 \"oracle quality\" 效应。\n\n**Q3.** Table 3 中 \"BCE + Gumbel + Penalty\" (PPL 38.02) 比 vanilla BCE (27.97) 还差——这意味着 Gumbel+Penalty 框架不是通用的改进而是 KL-specific 的。请解释为什么 Gumbel 帮助了 KL 却伤害了 BCE？这是否暗示优势来自 loss function 与 relaxation 的 interaction 而非纯粹的 coupling？\n\n**Q4.** 30% sparsity 下 penalty 达到 λ_max=5000 且偏差 5%——这是否意味着 SwiGLU 的 natural activation density 与 30% target 不兼容，训练实际上在对抗网络的内在分布？\n\n**Q5.** Gradient SNR 中 \"BCE early-layer SNR collapses to ~10⁻⁸ after step 10\"——这是否因为 BCE 在 10 步内已对 oracle masks 过拟合（loss 接近 0 → gradient 接近 0）？如果是，这不是缺陷而是收敛。\n\n---\n\n## Missing References\n\n- **ThunderKittens / FlashInfer** — sparse kernel implementations，与 wall-clock speedup 讨论相关\n- **Deja Vu++ / Brain-inspired Sparse Training** — 更近期的 predictor-based sparsity 工作（如果存在）\n- 当前引用覆盖度尚可（26篇），但缺少 hardware-aware pruning 方向的引用（如 nm-sparsity 的 Nvidia 工作）\n\n---\n\n## Overall Assessment\n\n**Soundness: 3/5 (Acceptable)**\n梯度分析数学正确但论证存在混淆（W2）；iso-compute claim 有误导性（W1）；核心实验单 seed（W5）。主要 claims 有支撑但关键对比的 fairness 存在问题。\n\n**Excitement: 3/5 (Interesting)**\n问题定义有价值（BCE vs KL for sparsity prediction 是实际存在的设计选择），三操作区域分析有实用意义。但 50% 下游崩溃和 30% 下温和改善限制了实际影响力。\n\n**Reproducibility: 3.5/5**\n超参完整报告，架构细节充分，但大部分结果单 seed 且缺少代码承诺。\n\n**Overall: 2.5 (Borderline: between Resubmit and Findings)**\n\n核心问题：(1) iso-compute claim 不公平需要修正或重新措辞；(2) coupling vs oracle-quality 的因果分离不足，核心叙事 \"structural mismatch → KL solves it via coupling\" 可能是 overclaim；(3) 实际可用区间（30%）的改善幅度温和（PPL 19%, MMLU +2pp）。\n\n如果作者能够：修正 iso-compute 表述、增加 oracle-quality ablation、在 30% 补充 multi-seed + OOD 评估，论文有望达到 Findings 水平。当前版本的 overclaim 和实验 gaps 使其处于 borderline 状态。\n\n**置信度: High (4/5)**\n我仔细检查了梯度推导、数值计算和实验逻辑。对 sparsity prediction 和 KL distillation 文献有较好了解。",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 287 · 2026-05-17T10:37:04.479266+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4719
}
```

</details>

---


### Assistant

_source line 288 · 2026-05-17T10:37:13.502400+00:00_

审稿意见已提交给 Review Director。

总结：论文在梯度结构分析和消融实验设计上有值得肯定之处，但存在三个核心问题：(1) iso-compute 对比忽略了 KL 每步 2.65× 的成本差异，表述有误导性；(2) coupling vs oracle-quality 的因果归因未被分离，"structural mismatch" 可能是 overclaim；(3) 方法的实际价值集中在 30% sparsity（PPL 19% improvement, MMLU +2pp），而论文主推的 50% 区间下游任务完全崩溃。评分 borderline (2.5/5)，建议修正后可达 Findings 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1"
}
```

</details>

---


## Round 11

## Round 11

4 recorded events


### User

_source line 289 · 2026-05-17T10:40:08.510597+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿意见。请逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

# Reviewer 2 — Round 1 审稿意见

## Summary
本文提出用 forward KL distillation + Gumbel-Sigmoid relaxation 训练 SwiGLU LLM 的 contextual sparsity predictor，替代标准 BCE 训练。核心论点是 BCE 的 per-neuron 独立梯度结构与 global top-k 推理分配不匹配，而 KL 的耦合梯度信号通过所有下游层传播，能更好地优化输出分布保真度。在 LLaMA-3.1-8B 上 50% sparsity 下 PPL 从 23.31 降至 11.79，并在 Mistral-7B-v0.3 上验证了跨架构一致性。

## 总体评分
**Overall**: 2.5 / 5（Borderline Findings）
**一句话总结**: 实验扎实但新颖性有限——核心贡献是将已有技术（KL distillation + Gumbel relaxation + Lagrangian penalty）组合应用于 sparsity prediction，梯度分析形式化了一个从计算图即可推导的显然性质。

## Strengths
S1. 梯度分析提供清晰的动机框架
S2. 消融实验设计全面
S3. 三区域发现具有实证价值
S4. 跨架构验证
S5. 二维 taxonomy 有用
S6. 写作质量整体良好

## Must-Fix 问题

**N1** [critical] 新颖性有限：核心贡献是已有技术的直接组合
- 论文的核心方法是将三个已有技术组合应用于 sparsity prediction：(1) Forward KL distillation（Hinton 2015），(2) Gumbel-Sigmoid relaxation（Jang 2017），(3) Lagrangian/adaptive penalty。论文自身承认 MaskLLM 也使用 "frozen weights + learnable masks + KL training"。
- EMNLP main conference 期望方法论或理论层面的新贡献，而非已有组件的新组合。
- 建议：重新定位为 empirical analysis 论文，或提出新的技术机制。

**N2** [critical] 梯度分析形式化了一个显然的性质
- §3.6 的核心观察是 KL loss 的梯度通过 Jacobian 耦合所有 neuron，而 BCE 是 per-neuron 独立的。但这是 backpropagation 通过复合函数的基本性质——任何 end-to-end loss 都会产生这种耦合。
- 如果论文的主要理论贡献仅是形式化一个 trivial property，则理论深度不足。
- 建议：深化分析，推导 KL 梯度退化为 BCE 等效的条件，或 per-layer 消融验证 Jacobian chain length 的预测。

**N3** [critical] "eliminates the need for error compensation" 的 claim 未经验证
- 论文从未测试 KL + compensation 的组合。如果 KL+compensation 能改善到 10.x，则 "eliminates the need" 是错误的。
- 建议：补充 KL+compensation 实验，或弱化 claim。

## Should-Fix 问题

**W1** 推荐配置下下游任务退化严重（MMLU 65→40%，GSM8K 48→7%）
**W2** 单 seed 主结果
**W3** 三区域发现仅 3 个采样点
**W4** 遗漏相关工作：SparseInfer (Shin et al., DATE 2025), SVD Contextual Sparsity Predictors (Serbin et al., 2026)
**W5** "consistent improvements on Mistral" 基于仅 1 个额外架构的 3 个 PPL 数据点，无下游结果
**W6** 训练/评估域内同质性

## 小问题
M1. Abstract 数字密度过高
M2. 术语不一致（predictor-TEAL / KL predictor / KL global）
M3. 40% MMLU 反转无 error bars
M4. 无 wall-clock speedup
M5. Table 2 中 BCE 行标注的比较公平性

## Questions
Q1. KL + compensation 效果如何？
Q2. MSE on output logits 是否测试过？
Q3. Per-layer PPL 贡献是否与 SNR pattern 一致？
Q4. KL 优势只在 PPL 而非 downstream——distributional fidelity 和 task-relevant preservation 是否存在 gap？

## Missing References
1. SparseInfer (Shin et al., DATE 2025, arXiv:2411.12692)
2. SVD Contextual Sparsity Predictors (Serbin et al., 2026, arXiv:2603.14110)

---

请对以上每条 Must-Fix (N1-N3)、Should-Fix (W1-W6)、Questions (Q1-Q4) 和 Missing References 逐条给出 [AGREE] 或 [REBUT]，并说明理由。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 290 · 2026-05-17T10:41:38.550663+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## 交叉回应 — Reviewer 1 对 Reviewer 2 意见的逐条评价\n\n---\n\n### Must-Fix 问题\n\n**[AGREE with nuance] R2-N1: 新颖性有限，已有技术的直接组合**\n\n同意核心判断：KL distillation (Hinton 2015) + Gumbel-Sigmoid (Jang 2017) + adaptive penalty 确实都是已有技术。论文 Related Work 自身承认与 MaskLLM 共享 \"frozen weights + learnable masks + KL training\" 原则（§5, Related Work paragraph 2）。\n\n但需要注意的细微差异：(1) MaskLLM 解决 static N:M weight sparsity（per-group categorical，无跨组预算竞争），而本文解决 dynamic per-token activation sparsity under global budget constraint——优化问题本质不同；(2) 此前确实无人将 KL 应用于 per-token activation predictor 的训练，Table 2 的 \"Per-token × Coupled\" cell 确实是空的。\n\n因此，技术新颖性确实有限，但 **问题新颖性** 存在——将其定位为 empirical analysis + mechanistic understanding 论文（如 \"understanding when and why KL outperforms BCE\"）可能更准确。对于 EMNLP Findings 而非 Main 可能更合适。\n\n**[REBUT] R2-N2: 梯度分析形式化了一个显然的性质**\n\n部分反驳。Reviewer 2 的论点——\"任何 end-to-end loss 都会产生 Jacobian 耦合\"——在数学上是正确的，但忽略了论文的实际贡献点：\n\n1. **形式化本身有价值**：尽管 backprop coupling 是 \"基本性质\"，但此前文献（DejaVu, FastForward, ShadowLLM）从未讨论过这个性质对 **global top-k allocation** 的具体影响。将显然性质 formalize 并指出其在特定场景下的后果是合法的贡献——类似于 batch normalization 论文形式化了 internal covariate shift 这个 \"显然\" 的现象。\n\n2. **实证验证非 trivial**：§3.6 的 SNR 测量、early-layer collapse 模式、以及 layer-depth vs advantage ratio 的 pattern（early layers 34-156×, late layers 1.7-3.8×）确实验证了 Jacobian chain length 的预测（layer 越靠前→chain 越长→coupling 优势越大）。这回应了 Reviewer 2 建议的 \"per-layer 消融验证 Jacobian chain length 的预测\"——论文已经做了这个分析。\n\n3. **但我在自己的审稿中指出**：该分析存在 confound——论文未分离 \"coupling effect\" 和 \"oracle quality effect\"（我的 W2）。所以梯度分析虽然数学正确且非完全 trivial，但其因果解释力确实被高估了。\n\n综合评价：N2 作为 \"critical\" 过于严厉。梯度分析的 formalization 和验证有增量贡献，但不是 groundbreaking 理论。降级为 Should-Fix 更合理。\n\n**[AGREE] R2-N3: \"eliminates the need for error compensation\" 未验证**\n\n完全同意。Table 3 有 \"BCE + Compensation\" (25.44) 但没有 \"KL + Compensation\"。论文声称 KL \"eliminates\" compensation need，但未验证 KL+compensation 是否能进一步改善到 e.g., PPL 10.x。这是一个简单的实验 gap。\n\n从现有数据推测：SPON 分析（§4.5）显示 SPON bias correction 对 KL 仅贡献 2.4% improvement（12.08→11.79），暗示 \"low-hanging fruit\" 已被 KL 捕获。但 SPON 不等于 compensation network——后者可能捕获不同类型的残差。\n\n建议作者：跑 KL+compensation 实验，或将 claim 弱化为 \"reduces the need for\" 而非 \"eliminates\"。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: 推荐配置下下游任务退化严重**\n\n同意，与我的 W3 一致。30% sparsity（推荐操作点）：MMLU 65→40%（-25pp），GSM8K 48→7%（-41pp）。这是巨大的退化。论文的 recommended configuration 仍然会让模型在 reasoning 任务上基本不可用。\n\n**[AGREE] R2-W2: 单 seed 主结果**\n\n同意，与我的 W5 一致。\n\n**[AGREE with nuance] R2-W3: 三区域发现仅 3 个采样点**\n\n同意这是一个弱点，但论文 §4.4 自身承认 \"Denser sampling (e.g., 35% sparsity) would be needed to precisely locate region boundaries\"。三区域的定性观察（non-monotonic allocation preference）从 30/40/50% 三个点可以建立，但精确边界需要更多数据。作为 exploratory finding 而非 definitive claim，3 个点是可接受的最低限度。但如果论文将此作为 core contribution（Introduction contribution list 第 3 条），则确实需要更多支撑。\n\n**[PARTIALLY AGREE] R2-W4: 遗漏相关工作**\n\n- SparseInfer (Shin et al., DATE 2025, arXiv:2411.12692)：如果确实是 hardware-aware sparse inference 方法，属于 \"Training-Free\" 类别，应在 §5 第一段提及。\n- SVD Contextual Sparsity Predictors (Serbin et al., 2026, arXiv:2603.14110)：如果是 predictor-based contextual sparsity 方法，则与本文直接相关，必须讨论。\n\n但需注意：我无法独立验证这两篇论文的真实性和内容。如果 Reviewer 2 能确认这些是真实发表/预印本且内容直接相关，则同意应引用。建议作者用 verify_references 工具核实。\n\n**[AGREE] R2-W5: 跨架构 claim 基于有限数据**\n\n同意。Mistral-7B 仅报告 PPL（Table 5），无下游 benchmarks。\"consistent improvements\" 的 claim 仅基于 3 个 PPL 数据点（30/50/70% sparsity）在 1 个额外架构上。这不足以支撑 \"cross-architecture\" 泛化的强结论。\n\n**[AGREE] R2-W6: 训练/评估域内同质性**\n\n同意，与我的 W8 一致。WikiText-103→WikiText-2 几乎是同分布。OOD 评估仅覆盖 50% 下的 C4。\n\n---\n\n### Questions\n\n**[AGREE - valid question] R2-Q1: KL + compensation 效果如何？**\n\n同上 N3 分析。这是论文应回答的关键问题。\n\n**[AGREE - valid question] R2-Q2: MSE on output logits 是否测试过？**\n\n好问题。论文 Table 2 taxonomy 列出了 \"Intermediate (MSE)\" 作为 ShadowLLM/D2DMoE 使用的 coupling level，但未在自己的 ablation 中测试 MSE on final logits（比 per-layer MSE 更强的 coupling）。这是一个有价值的 ablation：MSE on logits 也会产生 Jacobian coupling（因为 end-to-end），但优化的是 L2 距离而非 distributional distance。如果 MSE-on-logits 也大幅优于 BCE，则优势可能不是 KL-specific 而是 end-to-end-specific。\n\n论文 §4.2 末尾确实提到 \"Future work could further isolate coupling effects through MSE on hidden states and per-layer KL ablations\"——承认了这个 gap 但未执行。\n\n**[AGREE - insightful] R2-Q3: Per-layer PPL 贡献是否与 SNR pattern 一致？**\n\n非常好的问题。如果 KL 的优势主要来自 early-layer 的更好 SNR（§3.6: early layers 34-156× advantage），那么 per-layer PPL 分解应显示 KL 的 early-layer masks 质量显著高于 BCE。这可以通过 per-layer mask ablation 验证（每次只用一层的 KL mask，其余用 BCE mask）。论文未做此分析。\n\n**[AGREE - important] R2-Q4: KL 优势只在 PPL 而非 downstream**\n\n这是我在 W3 中强调的核心问题的另一种表述。50% sparsity 下 KL PPL >>> TEAL 但 MMLU/GSM8K 均崩溃。30% 下 PPL 改善 19% 但 MMLU 仅 +2pp（40.61 vs 38.61, Table 4）。distributional fidelity (PPL) 和 task-relevant preservation (downstream) 之间确实存在 gap。这挑战了论文 \"output-distribution preservation is the right objective\" 的核心前提。\n\n---\n\n### Missing References\n\n**[PARTIALLY AGREE] R2-Missing References**\n\n1. SparseInfer (Shin et al., DATE 2025)：如果真实存在且是 activation sparsity 相关，应引用于 Training-Free 段落。\n2. SVD Contextual Sparsity Predictors (Serbin et al., 2026)：如果真实存在且是 predictor-based 方法，应引用于 Predictor-Based 段落。\n\n但在我的审稿中也注意到引用覆盖的其他 gap：hardware-aware pruning direction（如 nm-sparsity 相关的 Nvidia 工作）也应提及。\n\n---\n\n### 总结评价\n\nReviewer 2 的审稿意见整体中肯。主要分歧在 N2（梯度分析的 trivialness）：\n- R2 认为这完全 trivial → \"critical\"\n- 我认为 formalization + empirical verification 有增量价值，但确实不构成 strong theoretical contribution → 更适合 \"Should-Fix\" 级别\n\n其余问题我大致同意，尤其是 N1（novelty）、N3（compensation claim）、W1-W6 的方向判断与我自己的审稿结论一致。\n\n**我的 overall 评分 (2.5) 与 Reviewer 2 (2.5) 一致**，论文处于 Borderline Findings 水平。核心问题是：技术新颖性有限 + 实用价值（下游任务保持）不够 convincing + 关键对比的公平性存疑。",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## 交叉回应 — Reviewer 1 对 Reviewer 2 意见的逐条评价\n\n---\n\n### Must-Fix 问题\n\n**[AGREE with nuance] R2-N1: 新颖性有限，已有技术的直接组合**\n\n同意核心判断：KL distillation (Hinton 2015) + Gumbel-Sigmoid (Jang 2017) + adaptive penalty 确实都是已有技术。论文 Related Work 自身承认与 MaskLLM 共享 \"frozen weights + learnable masks + KL training\" 原则（§5, Related Work paragraph 2）。\n\n但需要注意的细微差异：(1) MaskLLM 解决 static N:M weight sparsity（per-group categorical，无跨组预算竞争），而本文解决 dynamic per-token activation sparsity under global budget constraint——优化问题本质不同；(2) 此前确实无人将 KL 应用于 per-token activation predictor 的训练，Table 2 的 \"Per-token × Coupled\" cell 确实是空的。\n\n因此，技术新颖性确实有限，但 **问题新颖性** 存在——将其定位为 empirical analysis + mechanistic understanding 论文（如 \"understanding when and why KL outperforms BCE\"）可能更准确。对于 EMNLP Findings 而非 Main 可能更合适。\n\n**[REBUT] R2-N2: 梯度分析形式化了一个显然的性质**\n\n部分反驳。Reviewer 2 的论点——\"任何 end-to-end loss 都会产生 Jacobian 耦合\"——在数学上是正确的，但忽略了论文的实际贡献点：\n\n1. **形式化本身有价值**：尽管 backprop coupling 是 \"基本性质\"，但此前文献（DejaVu, FastForward, ShadowLLM）从未讨论过这个性质对 **global top-k allocation** 的具体影响。将显然性质 formalize 并指出其在特定场景下的后果是合法的贡献——类似于 batch normalization 论文形式化了 internal covariate shift 这个 \"显然\" 的现象。\n\n2. **实证验证非 trivial**：§3.6 的 SNR 测量、early-layer collapse 模式、以及 layer-depth vs advantage ratio 的 pattern（early layers 34-156×, late layers 1.7-3.8×）确实验证了 Jacobian chain length 的预测（layer 越靠前→chain 越长→coupling 优势越大）。这回应了 Reviewer 2 建议的 \"per-layer 消融验证 Jacobian chain length 的预测\"——论文已经做了这个分析。\n\n3. **但我在自己的审稿中指出**：该分析存在 confound——论文未分离 \"coupling effect\" 和 \"oracle quality effect\"（我的 W2）。所以梯度分析虽然数学正确且非完全 trivial，但其因果解释力确实被高估了。\n\n综合评价：N2 作为 \"critical\" 过于严厉。梯度分析的 formalization 和验证有增量贡献，但不是 groundbreaking 理论。降级为 Should-Fix 更合理。\n\n**[AGREE] R2-N3: \"eliminates the need for error compensation\" 未验证**\n\n完全同意。Table 3 有 \"BCE + Compensation\" (25.44) 但没有 \"KL + Compensation\"。论文声称 KL \"eliminates\" compensation need，但未验证 KL+compensation 是否能进一步改善到 e.g., PPL 10.x。这是一个简单的实验 gap。\n\n从现有数据推测：SPON 分析（§4.5）显示 SPON bias correction 对 KL 仅贡献 2.4% improvement（12.08→11.79），暗示 \"low-hanging fruit\" 已被 KL 捕获。但 SPON 不等于 compensation network——后者可能捕获不同类型的残差。\n\n建议作者：跑 KL+compensation 实验，或将 claim 弱化为 \"reduces the need for\" 而非 \"eliminates\"。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: 推荐配置下下游任务退化严重**\n\n同意，与我的 W3 一致。30% sparsity（推荐操作点）：MMLU 65→40%（-25pp），GSM8K 48→7%（-41pp）。这是巨大的退化。论文的 recommended configuration 仍然会让模型在 reasoning 任务上基本不可用。\n\n**[AGREE] R2-W2: 单 seed 主结果**\n\n同意，与我的 W5 一致。\n\n**[AGREE with nuance] R2-W3: 三区域发现仅 3 个采样点**\n\n同意这是一个弱点，但论文 §4.4 自身承认 \"Denser sampling (e.g., 35% sparsity) would be needed to precisely locate region boundaries\"。三区域的定性观察（non-monotonic allocation preference）从 30/40/50% 三个点可以建立，但精确边界需要更多数据。作为 exploratory finding 而非 definitive claim，3 个点是可接受的最低限度。但如果论文将此作为 core contribution（Introduction contribution list 第 3 条），则确实需要更多支撑。\n\n**[PARTIALLY AGREE] R2-W4: 遗漏相关工作**\n\n- SparseInfer (Shin et al., DATE 2025, arXiv:2411.12692)：如果确实是 hardware-aware sparse inference 方法，属于 \"Training-Free\" 类别，应在 §5 第一段提及。\n- SVD Contextual Sparsity Predictors (Serbin et al., 2026, arXiv:2603.14110)：如果是 predictor-based contextual sparsity 方法，则与本文直接相关，必须讨论。\n\n但需注意：我无法独立验证这两篇论文的真实性和内容。如果 Reviewer 2 能确认这些是真实发表/预印本且内容直接相关，则同意应引用。建议作者用 verify_references 工具核实。\n\n**[AGREE] R2-W5: 跨架构 claim 基于有限数据**\n\n同意。Mistral-7B 仅报告 PPL（Table 5），无下游 benchmarks。\"consistent improvements\" 的 claim 仅基于 3 个 PPL 数据点（30/50/70% sparsity）在 1 个额外架构上。这不足以支撑 \"cross-architecture\" 泛化的强结论。\n\n**[AGREE] R2-W6: 训练/评估域内同质性**\n\n同意，与我的 W8 一致。WikiText-103→WikiText-2 几乎是同分布。OOD 评估仅覆盖 50% 下的 C4。\n\n---\n\n### Questions\n\n**[AGREE - valid question] R2-Q1: KL + compensation 效果如何？**\n\n同上 N3 分析。这是论文应回答的关键问题。\n\n**[AGREE - valid question] R2-Q2: MSE on output logits 是否测试过？**\n\n好问题。论文 Table 2 taxonomy 列出了 \"Intermediate (MSE)\" 作为 ShadowLLM/D2DMoE 使用的 coupling level，但未在自己的 ablation 中测试 MSE on final logits（比 per-layer MSE 更强的 coupling）。这是一个有价值的 ablation：MSE on logits 也会产生 Jacobian coupling（因为 end-to-end），但优化的是 L2 距离而非 distributional distance。如果 MSE-on-logits 也大幅优于 BCE，则优势可能不是 KL-specific 而是 end-to-end-specific。\n\n论文 §4.2 末尾确实提到 \"Future work could further isolate coupling effects through MSE on hidden states and per-layer KL ablations\"——承认了这个 gap 但未执行。\n\n**[AGREE - insightful] R2-Q3: Per-layer PPL 贡献是否与 SNR pattern 一致？**\n\n非常好的问题。如果 KL 的优势主要来自 early-layer 的更好 SNR（§3.6: early layers 34-156× advantage），那么 per-layer PPL 分解应显示 KL 的 early-layer masks 质量显著高于 BCE。这可以通过 per-layer mask ablation 验证（每次只用一层的 KL mask，其余用 BCE mask）。论文未做此分析。\n\n**[AGREE - important] R2-Q4: KL 优势只在 PPL 而非 downstream**\n\n这是我在 W3 中强调的核心问题的另一种表述。50% sparsity 下 KL PPL >>> TEAL 但 MMLU/GSM8K 均崩溃。30% 下 PPL 改善 19% 但 MMLU 仅 +2pp（40.61 vs 38.61, Table 4）。distributional fidelity (PPL) 和 task-relevant preservation (downstream) 之间确实存在 gap。这挑战了论文 \"output-distribution preservation is the right objective\" 的核心前提。\n\n---\n\n### Missing References\n\n**[PARTIALLY AGREE] R2-Missing References**\n\n1. SparseInfer (Shin et al., DATE 2025)：如果真实存在且是 activation sparsity 相关，应引用于 Training-Free 段落。\n2. SVD Contextual Sparsity Predictors (Serbin et al., 2026)：如果真实存在且是 predictor-based 方法，应引用于 Predictor-Based 段落。\n\n但在我的审稿中也注意到引用覆盖的其他 gap：hardware-aware pruning direction（如 nm-sparsity 相关的 Nvidia 工作）也应提及。\n\n---\n\n### 总结评价\n\nReviewer 2 的审稿意见整体中肯。主要分歧在 N2（梯度分析的 trivialness）：\n- R2 认为这完全 trivial → \"critical\"\n- 我认为 formalization + empirical verification 有增量价值，但确实不构成 strong theoretical contribution → 更适合 \"Should-Fix\" 级别\n\n其余问题我大致同意，尤其是 N1（novelty）、N3（compensation claim）、W1-W6 的方向判断与我自己的审稿结论一致。\n\n**我的 overall 评分 (2.5) 与 Reviewer 2 (2.5) 一致**，论文处于 Borderline Findings 水平。核心问题是：技术新颖性有限 + 实用价值（下游任务保持）不够 convincing + 关键对比的公平性存疑。",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 291 · 2026-05-17T10:41:42.317562+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3766
}
```

</details>

---


### Assistant

_source line 292 · 2026-05-17T10:41:47.283366+00:00_

交叉回应已提交。核心结论：与 Reviewer 2 在大方向上一致（overall 2.5），主要分歧在 N2 的严重程度（我认为 Should-Fix 而非 Critical，因为 formalization + SNR 验证有增量价值）。两位 reviewer 共同识别的最关键问题是：iso-compute 不公平、下游任务退化严重、单 seed 结果、compensation claim 未验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1"
}
```

</details>

---


## Round 12

## Round 12

38 recorded events


### User

_source line 293 · 2026-05-18T12:24:23.521852+00:00_

[Round 1 审稿请求]:
你是 Round 7 Reviewer 1，负责 **方法严谨性 + 实验充分性**。

## Venue 信息
- **目标**: EMNLP 2026 (ARR May 2026 cycle)
- **截止日期**: 2026-05-25
- **格式**: ACL style, Long paper ≤8 页正文, double-blind
- **评分标准**: 5=Award(前2.5%), 4=Conference(主会议), 3=Findings, 2=Resubmit, 1=Do not resubmit

## 论文路径
`projects/distill_sparse_swiglu/paper/main.tex`
（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）

## 论文概要
提出用 forward KL 蒸馏（替代 BCE）训练 SwiGLU LLM 的激活稀疏性预测器。核心论点：BCE 的 per-neuron 梯度与 TEAL 的 global top-k 推理分配存在结构性错配；KL 通过端到端梯度耦合解决此问题。在 LLaMA-3.1-8B 上，KL predictor (<1% params) 在 30% 稀疏度下 PPL 降低 18%，在 50% 下降低 49%，且 compensation network 冗余。跨架构验证涵盖 Mistral-7B 和 Qwen-2.5-14B。

## 你的审查重点

### 方法严谨性
1. **梯度分析 (§3.5)**: BCE vs KL 梯度结构分析是否严谨？"structural mismatch" 论证是否过度包装了一个基本原理（end-to-end > decomposed）？SNR 测量的统计力度（步数、CI、替代解释）。
2. **Gumbel-Sigmoid 松弛 (§3.3)**: 训练（soft mask）和推理（hard mask via TEAL top-k）之间的 gap 是否被充分量化？
3. **自适应惩罚控制器 (§3.5)**: 30% 目标偏差 5%（实际 28.5%），对 TEAL 对比的影响是否讨论清楚？术语是否准确？
4. **BCE 对比公平性 (§4.2-4.3)**: KL 与 BCE 的差异是 loss function 差异还是 pipeline 差异（oracle 来源、Gumbel vs hard mask、penalty vs threshold）？confound 是否被承认？

### 实验充分性
5. **统计效力**: 主表中多少结果有 multi-seed？单 seed 结果的可靠性？Gumbel 随机性是否被充分考虑？
6. **OOD 评估**: 训练用 WikiText-103、评测用 WikiText-2（同源）。C4 OOD 覆盖哪些 sparsity levels？
7. **跨架构/跨规模**: Mistral 仅 PPL 无 downstream？Qwen-14B 的 MMLU gap 是否被充分分析？
8. **Regime 分析 (Table 4)**: 3 个采样点（30/40/50%）是否足够支撑 "three operating regions" 的结论？
9. **Compensation 冗余 claim**: KL+compensation 控制实验是否存在？数据是否充分？

请按 ACL 审稿标准输出完整审稿报告：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (评分+置信度)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 294 · 2026-05-18T12:24:32.721946+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
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

_source line 295 · 2026-05-18T12:24:32.722443+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 296 · 2026-05-18T12:24:35.936639+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 297 · 2026-05-18T12:24:37.794269+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/distill_sparse_swiglu/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/distill_sparse_swiglu/paper/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14"
  }
}
```

</details>

---


### Tool result

_source line 298 · 2026-05-18T12:24:37.844969+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 299 · 2026-05-18T12:24:44.127515+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

Based on the search results, here is information about ACL ARR 2025-2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by 
…[truncated 1571 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8190
}
```

</details>

---


### Tool call

_source line 300 · 2026-05-18T12:24:48.606093+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ACL ARR review form: all scoring dimensions (soundness, excitement, overall assessment, confidence, etc.), their scales, and descriptions. Include all questions reviewers must answer."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete ACL ARR review form: all scoring dimensions (soundness, excitement, overall assessment, confidence, etc.), their scales, and descriptions. Include all questions reviewers must answer."
  }
}
```

</details>

---


### Tool call

_source line 301 · 2026-05-18T12:24:49.359766+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper"
  }
}
```

</details>

---


### Tool result

_source line 302 · 2026-05-18T12:24:49.410384+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 303 · 2026-05-18T12:24:53.929832+00:00_

# ACL ARR Review Form: Scoring Dimensions and Questions

## Primary Scoring Dimensions

**Reviewer Confidence** (1-5 scale)
- 5: "Positive that my evaluation is correct"
- 4: "Quite sure"
- 3: "Pretty sure, but there's a chance I missed something"
- 2: "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- 1: "Not my area, or paper is very hard to understand"

**Soundness** (1-5 scale with half-point increments)
- 5: Excellent thoroughness for paper type
- 4: Provides sufficient support for claims
- 3: Adequate support for main claims
- 2: Major technical/methodological problems
- 1: Insufficient rigor for publication

**Excitement** (1-5 scale with half-point increments)
- 5: "I would recommend this paper to others"
- 4: "I would mention this paper to others"
- 3: "I might mention some points"
- 2: "Does not resonate with me"
- 1: "Not Exciting"

**Overall Assessment** (1-5 scale with half-point increments)
- 5: Award consideration
- 4: Conference acceptance
- 3: Findings acceptance
- 2: Resubmit next cycle
- 1: Do not resubmit

## Required Written Sections

- Paper Summary
- Summary of Strengths
- Summary of Weaknesses
- Comments/Suggestions/Typos
- Best paper justification (if applicable)
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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5323
}
```

</details>

---


### Tool call

_source line 304 · 2026-05-18T12:24:57.897158+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 305 · 2026-05-18T12:24:58.348863+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	
17	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
18	
19	\author{Anonymous}
20	
21	\begin{document}
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
32	\input{conclusion}
33	\input{limitations}
34	\input{ethics}
35	
36	\bibliography{references}
37	
38	\input{appendix}
39	
40	\end{document}
41	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 306 · 2026-05-18T12:24:58.349445+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 307 · 2026-05-18T12:24:58.852294+00:00_

1	We study whether end-to-end KL distillation can replace per-neuron classification for activation sparsity prediction in SwiGLU LLMs.
2	Existing predictors trained with binary cross-entropy (BCE) optimize each neuron independently, but inference allocates sparsity budgets via global top-$k$ across all layers.
3	Gradient analysis reveals a structural mismatch: BCE's per-neuron gradient is blind to cross-neuron interactions and achieves higher oracle F1 yet 139\% worse perplexity than a KL-trained predictor.
4	A lightweight predictor ($<$1\% of base parameters) trained with forward KL and Gumbel-Sigmoid relaxation resolves this mismatch by coupling all neurons through the output distribution, rendering post-hoc compensation (+67.2M params) redundant at both 30\% and 50\% sparsity.
5	On LLaMA-3.1-8B at the recommended 30\% sparsity, KL reduces PPL degradation 18\% over TEAL; uniform allocation provides $7.5\times$ smaller cross-seed downstream $\sigma$, eliminating seed-dependent instability.
6	At 50\% sparsity, the PPL advantage widens to 49\% but downstream tasks degrade regardless of allocation, revealing allocation-dependent operating regions at 7--8B scale.
7	Evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms the PPL advantage across 7--14B, though 14B reveals a scale-dependent MMLU gap not resolved by allocation strategy.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 308 · 2026-05-18T12:24:58.852660+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 309 · 2026-05-18T12:24:59.304693+00:00_

1	\section{Introduction}
2	
3	SwiGLU feed-forward networks~\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they universally rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: TEAL's top-$k$ mechanism~\cite{liu2025teal} ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	
8	We provide this analysis.
9	The gradient of BCE with respect to neuron $j$'s score is $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$, a function of $j$ alone, independent of every other neuron.
10	Under KL divergence, the gradient for neuron $j$ in layer $\ell$ factors as:
11	\begin{equation*}
12	\frac{\partial \mathcal{L}_{\text{KL}}}{\partial s_j^{(\ell)}} = \frac{\partial \mathcal{L}_{\text{KL}}}{\partial \mathbf{z}} \cdot \frac{\partial \mathbf{z}}{\partial \mathbf{h}^{(\ell)}} \cdot \frac{\partial \mathbf{h}^{(\ell)}}{\partial \tilde{m}_j^{(\ell)}} \cdot \frac{\partial \tilde{m}_j^{(\ell)}}{\partial s_j^{(\ell)}},
13	\end{equation*}
14	where the Jacobian $\partial \mathbf{z} / \partial \mathbf{h}^{(\ell)}$ propagates through all downstream layers, coupling each neuron's gradient to every other neuron's mask state.
15	This structural difference predicts that KL should outperform BCE specifically under global allocation, and the prediction is confirmed empirically: BCE achieves higher oracle F1 (0.613 vs.\ 0.540) yet produces 139\% worse perplexity, because per-neuron magnitude accuracy is a misaligned proxy for output-distribution preser
…[truncated 1574 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 310 · 2026-05-18T12:24:59.305231+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 311 · 2026-05-18T12:24:59.809253+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models.
5	The method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass and achieves competitive performance without auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{h}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importance scores from the pre-FFN hidden sta
…[truncated 14198 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 312 · 2026-05-18T12:24:59.809776+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 313 · 2026-05-18T12:25:00.251286+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4, using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $5 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly; (2) \textbf{BCE predictor} (DejaVu-style~\cite{liu2023dejavu}), trained with per-neuron binary cross-entropy on magnitude-based oracle masks for 1000 and 2700 steps; (3) \textbf{Uniform allocation}, which distributes the sparsity budget equally across layers; and (4) \textbf{WINA}
…[truncated 16769 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 441
}
```

</details>

---


### Tool call

_source line 314 · 2026-05-18T12:25:00.251823+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 315 · 2026-05-18T12:25:00.436547+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} predicts activation sparsity patterns from attention outputs without additional training.
6	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
7	
8	\paragraph{Predictor-Based Contextual Sparsity.}
9	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
10	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
11	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
12	SVD-CSP~\cite{serbin2026svdcsp} compresses sparsity predictors via SVD decomposition for reduced predictor overhead.
13	PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.
14	MaskLLM~\cite{fang2024maskllm} also employs learnable masks with Gumbel relaxation and frozen weights, but targets N:M semi-structured \emph{weight} sparsity (2:4 patterns) via per-group categorical selection (Gumbel-Softmax), producing fixed masks independent of input tokens.
15	Both share the principle of frozen weights + learnable masks + KL training, but solve distinct optimization problems: MaskLLM finds optimal static N:M patterns within fixed groups
…[truncated 2535 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 184
}
```

</details>

---


### Tool call

_source line 316 · 2026-05-18T12:25:00.741725+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 317 · 2026-05-18T12:25:01.193576+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	\vspace{-2pt}
4	
5	A $<$1\% predictor with KL distillation halves TEAL's PPL across 7--14B; uniform allocation cuts cross-seed $\sigma$ $7.5\times$.
6	
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 318 · 2026-05-18T12:25:01.194045+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 319 · 2026-05-18T12:25:02.149712+00:00_

1	\section*{Limitations}
2	
3	Our primary evaluation uses WikiText-2 perplexity, and downstream benchmarks reveal that perplexity is a poor proxy for reasoning ability at moderate sparsity: 40\% sparsity achieves PPL 8.36 but MMLU already degrades, motivating 30\% as the recommended operating point for downstream fidelity.
4	Training requires 1000 steps on WikiText-103 ($\sim$45 minutes on RTX PRO 6000 for KL, $\sim$17 minutes for BCE), but a separate predictor must be trained for each sparsity target.
5	Our recommended operating point (30\% sparsity, uniform allocation) is validated at 7--8B scale; at 14B (Qwen-2.5-14B), KL's PPL advantage persists but the MMLU gap relative to TEAL/BCE is not resolved by uniform allocation (+0.8pp vs.\ +5.0pp at 8B), suggesting that KL's output-preservation objective may underweight task-specific features at higher knowledge densities. Scaling to 70B remains untested.
6	Out-of-distribution evaluation (Appendix~\ref{app:ood}) covers 30\% and 50\% sparsity on C4; extending to 70\% is left to future work.
7	Our attribution of KL's advantage to gradient coupling (\S\ref{sec:method:gradient}) is supported by SNR measurements and the BCE isolation ablation, but does not fully disentangle coupling from oracle quality: BCE uses magnitude-based oracles while KL directly optimizes output preservation, and an ablation using KL-derived masks as BCE targets would more precisely isolate the coupling effect.
8	At 30\% sparsity, global allocation exhibits 9.5pp cross-seed MMLU standard deviation (3-seed); allocation strategy interacts with predictor initialization in task-specific ways. This variance is MMLU-specific, as ARC, WinoGrande, and GSM8K show stable performance across seeds under both allocation strategies.
9	While we motivate our work with inference speedup potential, actual wall-clock acceleration depends on sparse kernel implementations (e.g., Triton, cuSPARSE) and hardware-specific memory access patterns; this work focuses on predict
…[truncated 246 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 320 · 2026-05-18T12:25:02.150276+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 321 · 2026-05-18T12:25:02.301826+00:00_

1	\section*{Ethics Statement}
2	
3	This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, MMLU, GSM8K).
4	No new data collection, annotation, or human subjects are involved.
5	The method does not alter model outputs beyond the sparsity-induced degradation we analyze; it introduces no new generation capabilities or safety risks beyond those inherent in the base models.
6	Compute requirements are modest (1000 training steps, $\sim$45 minutes on a single GPU for KL training), presenting minimal environmental concern relative to the pretrained models we evaluate on.
7	We release no model weights or user-facing systems; our contribution is analytical (understanding KL distillation for sparsity) rather than deployment-oriented.
8	
9	\section*{Responsible NLP Research Checklist}
10	
11	\paragraph{A. Limitations and Risks.}
12	\begin{itemize}[nosep,leftmargin=*]
13	\item[\textbf{A1.}] Limitations are discussed in the Limitations section. Key limitations: evaluation limited to 7--8B models; perplexity is an imperfect proxy for downstream quality; wall-clock speedup requires sparse kernel support not implemented here.
14	\item[\textbf{A2.}] No foreseeable risks specific to this work beyond those inherent in the base language models. The method does not enable new capabilities or applications.
15	\end{itemize}
16	
17	\paragraph{B. Scientific Artifacts.}
18	\begin{itemize}[nosep,leftmargin=*]
19	\item[\textbf{B1.}] Yes. All models (LLaMA-3.1-8B~\cite{grattafiori2024llama3}, Mistral-7B-v0.3~\cite{jiang2023mistral}), datasets (WikiText~\cite{merity2017pointer}, C4~\cite{raffel2020c4}), and methods (TEAL~\cite{liu2025teal}, SPON~\cite{xu2026spon}) are cited with original references.
20	\item[\textbf{B2.}] LLaMA-3.1 is released under the Llama 3.1 Community License; Mistral-7B under Apache 2.0. WikiText a
…[truncated 1816 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 322 · 2026-05-18T12:25:02.302375+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-18T12:25:02.404350+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); KL distillation thus provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overhead; net ac
…[truncated 12466 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 324 · 2026-05-18T12:25:08.628391+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool call

_source line 325 · 2026-05-18T12:25:10.988089+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines: what reviewers should evaluate, how to score soundness and excitement, what counts as a strength vs weakness, guidance on experimental rigor, and any specific instructions about claims vs evidence."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines: what reviewers should evaluate, how to score soundness and excitement, what counts as a strength vs weakness, guidance on experimental rigor, and any specific instructions about claims vs evidence."
  }
}
```

</details>

---


### Tool result

_source line 326 · 2026-05-18T12:25:42.641329+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 39, \"total_citations\": 76, \"unique_cited_keys\": 39, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 35, \"online_not_found\": 0, \"online_mismatch\": 4}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"fang2024maskllm\", \"type\": \"inproceedings\", \"title\": \"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models\", \"authors\": \"Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff P...\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"xu2026spon\", \"type\": \"inproceedings\", \"title\": \"Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models\", \"authors\": \"Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Machine Learning (ICML)\"}, {\"key\": \"muralidharan2024minitron\", \"type\": \"inproceedings\", \"title\": \"Compact Language Models via Pruning and Knowledge Distillation\", \"authors\": \"Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marci...\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"gautam2026fastforward\", \"type\": \"article\", \"title\": \"Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity\", \"authors\": \"Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott ...\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2602.00397\"}, {\"key\": \"liu2025teal\", \"type\": \"inproceedings\", \"title\": \"Training-Free Activation Sparsity in Large Language Models\", \"authors\": \"James Liu and Pragaash Ponnusamy and Tianle Cai and Han Guo and Yoon Kim and Ben...\", \"year
…[truncated 31237 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 34012
}
```

</details>

---


### Tool result

_source line 327 · 2026-05-18T12:25:54.273683+00:00_

# ARR Reviewer Guidelines: Key Evaluation Principles

## What Reviewers Should Evaluate

Reviewers assess papers across multiple dimensions. The core evaluation focuses on **technical soundness, novelty, clarity, and contribution to the field**. Papers must be "sufficiently sound and reproducible" for acceptance at main venues.

Key assessment areas include:
- Research question clarity and appropriateness
- Methodological validity and completeness
- Evidence quality supporting claims
- Novelty relative to prior work
- Reproducibility and implementation details

## Scoring: Soundness and Excitement

ARR uses three scores (as of February 2025):

**Soundness**: "must be justified by the text of the review." Low soundness scores require explicit explanation of technical flaws. Reviewers should identify specific methodological problems, incomplete proofs, or invalid assumptions.

**Excitement**: Orthogonal to soundness, reflecting "personal taste" about topic interest. A paper can be technically sound but personally unexciting, or vice versa.

**Overall Assessment**: A composite recommendation balancing soundness, excitement, novelty, and potential impact—not solely dependent on any single factor.

## Strengths vs. Weaknesses: Critical Distinctions

The guidelines identify **common review mistakes** that mischaracterize papers:

| Problematic | Why It's Flawed |
|---|---|
| "Results seem obvious" | Findings often appear intuitive retrospectively but lack prior empirical validation |
| "Method too simple" | Simplicity is preferable; complexity doesn't equal quality |
| "No SOTA results" | SOTA isn't necessary for scientific contribution |
| "Negative results" | Publishing negatives combats publication bias |
| "Paper lacks experiment X" | Only required if X is essential to the core claim |

**Legitimate weaknesses** include: incomplete assumptions, invalid proofs, unfair baseline comparisons, undisclosed data quality issues, or claims unsupported by presented evidence.

#
…[truncated 1631 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 43285
}
```

</details>

---


### Tool call

_source line 328 · 2026-05-18T12:30:57.856707+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 7 Reviewer 1 审稿报告：方法严谨性 + 实验充分性\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**Confidence**: 4/5 (Quite sure)\n**一句话总结**: 实用的 KL 蒸馏方案替代 BCE 训练稀疏预测器，但核心 \"structural mismatch\" 叙事的因果证据不足——KL 与 BCE 的比较被多重流水线差异混淆，且缺少中间耦合度方法 (ShadowLLM/D2DMoE) 的关键 baseline。\n\n---\n\n## 官方维度打分（ACL ARR Review Form, Feb 2025+）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0/5 | 核心方法可行，但 BCE vs KL 比较存在未解混淆变量（oracle 来源、mask 类型、sparsity 控制方式同时不同）；\"structural mismatch\" 论证在严格意义上是循环论证 |\n| Excitement | 3.0/5 | 问题实际相关，compensation 冗余发现实用，但贡献偏 incremental（替换一个 loss），Qwen-14B 的 MMLU 负结果削弱泛化故事 |\n| Reproducibility | 4.0/5 | 超参数完整，训练/评估协议清晰，缺少代码但提供了充足细节 |\n| Overall Assessment | 3.0 | Findings 水平——有扎实的实验工作和诚实的局限性讨论，但因果证据的缺口和缺失的 intermediate baseline 使核心 claim 证据不充分 |\n\n---\n\n## 主要优势\n\n1. **问题定义清晰且实际相关**：per-neuron training 与 global inference allocation 之间的不匹配是真实工程问题。\n\n2. **Ablation 设计系统全面**：Table 3 逐一隔离 divergence direction、Gumbel vs STE、compensation 效果。\n\n3. **诚实的局限性讨论**：主动承认 confound 未完全 disentangle、Qwen-14B MMLU gap、single-seed 局限。\n\n4. **Compensation 冗余的实用价值**：KL predictor 使 67.2M 参数 compensation network 冗余，减少 2.7% inference latency。\n\n5. **Training 效率极高**：1000 步/45 分钟训练达到饱和。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] BCE 与 KL 比较存在多重混淆变量，不能支撑 \"structural mismatch\" 因果 claim\n\n- 具体位置：§3.6、§4.3、Table 3\n- 问题：KL 与 BCE 的比较存在至少四个同时变化的因素：(1) loss function；(2) oracle 来源（output distribution vs magnitude-based threshold）；(3) mask 类型（Gumbel-Sigmoid 连续 vs hard threshold）；(4) sparsity 控制（adaptive penalty vs oracle 内建 threshold）。论文的 \"loss isolation\" ablation（BCE + Gumbel + Penalty = PPL 38.02）并未清楚隔离 loss 效果——adaptive penalty 对 BCE per-neuron 目标产生干扰。关键缺失实验：(a) BCE trained on KL-derived oracle masks，或 (b) KL with magnitude-based oracle constraints。论文在 §4.3 和 Limitations 中承认此问题但未执行。\n- 影响：论文核心叙事建立在 \"structural mismatch → KL coupling resolves it\" 的因果链上。当前证据无法区分 \"梯度耦合本身有益\" 和 \"直接优化正确指标有益\" 两种解释。\n- 建议：执行 oracle-swap ablation；或将 \"structural mismatch\" 从因果 claim 降级为 motivating hypothesis。\n\n**N2** [critical] 缺少 intermediate coupling (MSE) baseline 比较\n\n- 具体位置：Table 1、§2 Related Work\n- 问题：Taxonomy 将方法分为 Decomposed/Intermediate/Coupled 三级，但实验只比较两个极端。ShadowLLM 和 D2DMoE（MSE, intermediate）从未作为 baseline。如果 intermediate coupling 已获得大部分优势，full end-to-end KL 的额外复杂性失去正当性。\n- 建议：实现 MSE hidden-state loss baseline；如资源不足，明确讨论此缺失。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] \"Three operating regions\" 结论基于 3 个数据点\n\n- 具体位置：§4.5、Table 4\n- 30/40/50% 三点拟合三类 regime，自由度为零。40% 全部 single seed。\n- 建议：补充中间 sparsity 点或降级为 \"preliminary observation\"。\n\n**W2** [warning] 40% uniform PPL (8.36) 低于 30% uniform PPL (8.82) 的反直觉结果未讨论\n\n- 具体位置：Table 4\n- 更高稀疏度应导致更高 PPL。可能与 30% target penalty controller 饱和（λ→5000）导致 predictor 质量下降有关。\n- 建议：分析 30% vs 40% predictor 的纯 KL loss 分量。\n\n**W3** [warning] 训练-推理 gap（soft → hard mask）未被量化讨论\n\n- 具体位置：§3.3、Appendix B\n- Per-token evaluation PPL 9.218 vs TEAL global PPL 11.963——30% gap 未讨论。\n- 建议：正式讨论此 gap，量化 soft vs hard mask 的分离效应。\n\n**W4** [warning] Qwen-14B MMLU 降幅对论文 framing 影响不足\n\n- 具体位置：§4.5、Table 5、Abstract\n- KL MMLU 63.7% vs TEAL/BCE >71%。Abstract 以 \"PPL advantage\" 领衔，低估了实用场景中 MMLU 的重要性。\n- 建议：在 Abstract 中更对等呈现；讨论 KL output-preservation 与 task-specific feature preservation 的 trade-off 机制。\n\n**W5** [warning] Mistral-7B 仅 PPL 无 downstream\n\n- 论文反复强调 \"PPL is a poor proxy for reasoning\"，但 Mistral 跨架构验证仅有 PPL。\n- 建议：至少报告 Mistral 30% 的 MMLU 和 ARC-c。\n\n**W6** [warning] SNR 分析仅覆盖前 300/1000 步\n\n- 非单调性（BCE 在 step 100-250 超过 KL）意味着 KL SNR 优势是 late-training 现象，可能与收敛动态有关而非结构性质。\n- 建议：扩展至 1000 步完整 trajectory。\n\n---\n\n## 小问题\n\n- Conclusion 仅一句话\n- WikiText-103→WikiText-2 非真正 OOD；C4 仅覆盖 30/50%\n- 40% uniform exp_id `d030_kl40_uniform` 前缀暗示可能使用 30% predictor，与 caption 矛盾\n- Table 5 Qwen uniform 行缺少 GSM8K 数据未解释\n- 引用整体可靠（35/39 verified），4 个 minor mismatch 为作者姓格式差异\n\n---\n\n## Questions to Authors\n\n1. Table 4 中 40% uniform PPL (8.36) 低于 30% uniform PPL (8.82)，请解释。exp_id d030 是否意味着使用了 30% predictor？\n2. 是否计划执行 oracle-swap ablation？\n3. Qwen-14B MMLU gap 是否在其他 knowledge-intensive task 上也存在？\n4. Per-token PPL (9.218) 与 TEAL global PPL (11.963) 的 30% gap 中，soft→hard 和 per-token→global 各贡献多少？",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 7 Reviewer 1 审稿报告：方法严谨性 + 实验充分性\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**Confidence**: 4/5 (Quite sure)\n**一句话总结**: 实用的 KL 蒸馏方案替代 BCE 训练稀疏预测器，但核心 \"structural mismatch\" 叙事的因果证据不足——KL 与 BCE 的比较被多重流水线差异混淆，且缺少中间耦合度方法 (ShadowLLM/D2DMoE) 的关键 baseline。\n\n---\n\n## 官方维度打分（ACL ARR Review Form, Feb 2025+）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0/5 | 核心方法可行，但 BCE vs KL 比较存在未解混淆变量（oracle 来源、mask 类型、sparsity 控制方式同时不同）；\"structural mismatch\" 论证在严格意义上是循环论证 |\n| Excitement | 3.0/5 | 问题实际相关，compensation 冗余发现实用，但贡献偏 incremental（替换一个 loss），Qwen-14B 的 MMLU 负结果削弱泛化故事 |\n| Reproducibility | 4.0/5 | 超参数完整，训练/评估协议清晰，缺少代码但提供了充足细节 |\n| Overall Assessment | 3.0 | Findings 水平——有扎实的实验工作和诚实的局限性讨论，但因果证据的缺口和缺失的 intermediate baseline 使核心 claim 证据不充分 |\n\n---\n\n## 主要优势\n\n1. **问题定义清晰且实际相关**：per-neuron training 与 global inference allocation 之间的不匹配是真实工程问题。\n\n2. **Ablation 设计系统全面**：Table 3 逐一隔离 divergence direction、Gumbel vs STE、compensation 效果。\n\n3. **诚实的局限性讨论**：主动承认 confound 未完全 disentangle、Qwen-14B MMLU gap、single-seed 局限。\n\n4. **Compensation 冗余的实用价值**：KL predictor 使 67.2M 参数 compensation network 冗余，减少 2.7% inference latency。\n\n5. **Training 效率极高**：1000 步/45 分钟训练达到饱和。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] BCE 与 KL 比较存在多重混淆变量，不能支撑 \"structural mismatch\" 因果 claim\n\n- 具体位置：§3.6、§4.3、Table 3\n- 问题：KL 与 BCE 的比较存在至少四个同时变化的因素：(1) loss function；(2) oracle 来源（output distribution vs magnitude-based threshold）；(3) mask 类型（Gumbel-Sigmoid 连续 vs hard threshold）；(4) sparsity 控制（adaptive penalty vs oracle 内建 threshold）。论文的 \"loss isolation\" ablation（BCE + Gumbel + Penalty = PPL 38.02）并未清楚隔离 loss 效果——adaptive penalty 对 BCE per-neuron 目标产生干扰。关键缺失实验：(a) BCE trained on KL-derived oracle masks，或 (b) KL with magnitude-based oracle constraints。论文在 §4.3 和 Limitations 中承认此问题但未执行。\n- 影响：论文核心叙事建立在 \"structural mismatch → KL coupling resolves it\" 的因果链上。当前证据无法区分 \"梯度耦合本身有益\" 和 \"直接优化正确指标有益\" 两种解释。\n- 建议：执行 oracle-swap ablation；或将 \"structural mismatch\" 从因果 claim 降级为 motivating hypothesis。\n\n**N2** [critical] 缺少 intermediate coupling (MSE) baseline 比较\n\n- 具体位置：Table 1、§2 Related Work\n- 问题：Taxonomy 将方法分为 Decomposed/Intermediate/Coupled 三级，但实验只比较两个极端。ShadowLLM 和 D2DMoE（MSE, intermediate）从未作为 baseline。如果 intermediate coupling 已获得大部分优势，full end-to-end KL 的额外复杂性失去正当性。\n- 建议：实现 MSE hidden-state loss baseline；如资源不足，明确讨论此缺失。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] \"Three operating regions\" 结论基于 3 个数据点\n\n- 具体位置：§4.5、Table 4\n- 30/40/50% 三点拟合三类 regime，自由度为零。40% 全部 single seed。\n- 建议：补充中间 sparsity 点或降级为 \"preliminary observation\"。\n\n**W2** [warning] 40% uniform PPL (8.36) 低于 30% uniform PPL (8.82) 的反直觉结果未讨论\n\n- 具体位置：Table 4\n- 更高稀疏度应导致更高 PPL。可能与 30% target penalty controller 饱和（λ→5000）导致 predictor 质量下降有关。\n- 建议：分析 30% vs 40% predictor 的纯 KL loss 分量。\n\n**W3** [warning] 训练-推理 gap（soft → hard mask）未被量化讨论\n\n- 具体位置：§3.3、Appendix B\n- Per-token evaluation PPL 9.218 vs TEAL global PPL 11.963——30% gap 未讨论。\n- 建议：正式讨论此 gap，量化 soft vs hard mask 的分离效应。\n\n**W4** [warning] Qwen-14B MMLU 降幅对论文 framing 影响不足\n\n- 具体位置：§4.5、Table 5、Abstract\n- KL MMLU 63.7% vs TEAL/BCE >71%。Abstract 以 \"PPL advantage\" 领衔，低估了实用场景中 MMLU 的重要性。\n- 建议：在 Abstract 中更对等呈现；讨论 KL output-preservation 与 task-specific feature preservation 的 trade-off 机制。\n\n**W5** [warning] Mistral-7B 仅 PPL 无 downstream\n\n- 论文反复强调 \"PPL is a poor proxy for reasoning\"，但 Mistral 跨架构验证仅有 PPL。\n- 建议：至少报告 Mistral 30% 的 MMLU 和 ARC-c。\n\n**W6** [warning] SNR 分析仅覆盖前 300/1000 步\n\n- 非单调性（BCE 在 step 100-250 超过 KL）意味着 KL SNR 优势是 late-training 现象，可能与收敛动态有关而非结构性质。\n- 建议：扩展至 1000 步完整 trajectory。\n\n---\n\n## 小问题\n\n- Conclusion 仅一句话\n- WikiText-103→WikiText-2 非真正 OOD；C4 仅覆盖 30/50%\n- 40% uniform exp_id `d030_kl40_uniform` 前缀暗示可能使用 30% predictor，与 caption 矛盾\n- Table 5 Qwen uniform 行缺少 GSM8K 数据未解释\n- 引用整体可靠（35/39 verified），4 个 minor mismatch 为作者姓格式差异\n\n---\n\n## Questions to Authors\n\n1. Table 4 中 40% uniform PPL (8.36) 低于 30% uniform PPL (8.82)，请解释。exp_id d030 是否意味着使用了 30% predictor？\n2. 是否计划执行 oracle-swap ablation？\n3. Qwen-14B MMLU gap 是否在其他 knowledge-intensive task 上也存在？\n4. Per-token PPL (9.218) 与 TEAL global PPL (11.963) 的 30% gap 中，soft→hard 和 per-token→global 各贡献多少？",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 329 · 2026-05-18T12:31:02.933362+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5076
}
```

</details>

---


### Assistant

_source line 330 · 2026-05-18T12:31:11.009699+00:00_

审稿报告已提交给 Review Director。

**审稿结论：Overall 3.0 (Findings)**

核心发现：
- 2 个 Must-Fix：(1) BCE vs KL 比较被 4 个混淆变量污染，无法支撑因果 claim；(2) 缺少 intermediate coupling (MSE) baseline，taxonomy 自建框架未被实验覆盖
- 6 个 Should-Fix：regime analysis 数据点不足、40% PPL 反直觉异常、soft→hard mask gap 未量化、Qwen-14B MMLU framing 不对等、Mistral 无 downstream、SNR 仅 30% 训练步数
- 优势：问题实际相关、ablation 系统、诚实的局限性讨论、compensation 冗余发现有实用价值

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1"
}
```

</details>

---


## Round 13

## Round 13

40 recorded events


### User

_source line 331 · 2026-05-18T12:32:00.006339+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 完整审稿原文

**Overall**: 3.0 (Findings), Confidence 4/5

### 主要优势
S1. 诚实透明的实验报告（负面结果坦诚呈现）
S2. 系统性消融设计（Table 3 逐一隔离各因素）
S3. 多种子统计和方差报告
S4. 写作质量（无 AI 写作痕迹）
S5. Gradient 分析提供清晰直觉

### Must-Fix 问题

**N1** [critical] 技术新颖性有限：已有组件的新问题组合
- 核心技术组件（frozen weights + learnable masks + KL training + Gumbel relaxation）全部来自 MaskLLM。区分点是 N:M static weight sparsity vs dynamic per-token activation sparsity——problem formulation 层面的不同而非方法层面的创新。Table 1 taxonomy（2×3, 5/6 cells filled）填充空 cell 的新颖性论证较弱。论文自身定位 "primarily empirical"。

**N2** [critical] Headline 数字与推荐操作点之间的叙事张力
- 50% sparsity 的 "49% PPL reduction" 是 headline，但该 regime 下 downstream 全面崩溃。推荐操作点 30% 改善为 PPL 18%, MMLU +2.1pp，且 ARC-c (40.78 vs 42.32) 和 GSM8K (7.35 vs 7.88) 实际劣于 TEAL vanilla。Conclusion 仅一句以 "halves PPL" 为卖点——overclaiming。

**N3** [critical] 14B 结果实质性削弱泛化 claim
- Qwen-14B MMLU 比 TEAL 低 8.1pp，比 BCE 低 7.95pp。Uniform 仅恢复 +0.8pp。Abstract 称 "confirms the PPL advantage" 将严重退化轻描淡写。

### Should-Fix 问题

**W1** BCE 对比存在混淆变量（oracle 质量 vs 训练目标）
**W2** 无实际推理加速（+6.4% overhead, unstructured masks）
**W3** Conclusion 过于简短（一句话）
**W4** `\enlargethispage{8\baselineskip}` 页面操纵（≈1.3 inches expansion）
**W5** "Structural mismatch" 洞察本质是标准链式法则应用

### 小问题
M1: Table 2/4 高度重叠
M2: 39 篇引用处于下限
M3: 术语不一致
M4: "We provide this analysis." 突兀
M5: exp_id 注释未清除

### Questions
Q1: 30% uniform 在 ARC-c/GSM8K 劣于 TEAL，为何仍推荐？
Q2: 14B MMLU 退化能否通过 temperature 调整或混合 loss 缓解？
Q3: MaskLLM Gumbel-Softmax vs 本文 Gumbel-Sigmoid 在优化 landscape 上有什么实质区别？
Q4: KL-derived masks 作 BCE targets 的 ablation 是否有初步结果？

### Missing References
1. Quantization + Sparsity（AWQ, SqueezeLLM）
2. Dynamic inference 综述（Schuster et al., Han et al.）
3. FLAP（fluctuation-based activation pruning）
4. LLM-Pruner（structured pruning with gradient）

---

请对以上每个 Must-Fix (N1, N2, N3)、Should-Fix (W1-W5)、小问题 (M1-M5)、Questions (Q1-Q4)、和 Missing References 逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 332 · 2026-05-18T12:33:45.767483+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 333 · 2026-05-18T12:33:45.818252+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 334 · 2026-05-18T12:33:46.370949+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
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

_source line 335 · 2026-05-18T12:33:46.371328+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 336 · 2026-05-18T12:33:46.672664+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
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

_source line 337 · 2026-05-18T12:33:46.773575+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 338 · 2026-05-18T12:33:52.196098+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
  "pages": "1-8",
  "dpi": "180"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
    "pages": "1-8",
    "dpi": "180"
  }
}
```

</details>

---


### Tool call

_source line 339 · 2026-05-18T12:33:53.151626+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
  "pages": "9-16",
  "dpi": "180"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
    "pages": "9-16",
    "dpi": "180"
  }
}
```

</details>

---


### Tool call

_source line 340 · 2026-05-18T12:33:53.555001+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring rubric"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring rubric"
  }
}
```

</details>

---


### Tool result

_source line 341 · 2026-05-18T12:33:55.181181+00:00_

Error: result (6,300,606 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/9f1d1d19-64e8-4613-9864-3e1bb48676c6/tool-results/mcp-agent-ml-research-pdf_to_images-1779107634924.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/9f1d1d19-64e8-4613-9864-3e1bb48676c6/tool-results/mcp-agent-ml-research-pdf_to_images-1779107634924.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2985
}
```

</details>

---


### Tool result

_source line 342 · 2026-05-18T12:33:55.181565+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"页码超出范围 (共 14 页): 9-16\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2029
}
```

</details>

---


### Tool result

_source line 343 · 2026-05-18T12:34:04.218230+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring rubric"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the web search results, I found comprehensive information about ACL ARR 2025-2026 reviewer guidelines and review form criteria. Here's what I found:

## Reviewer Scoring and Guidelines

Starting with February 
…[truncated 1651 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 10663
}
```

</details>

---


### Tool call

_source line 344 · 2026-05-18T12:34:07.582007+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. I need the exact criteria names and scoring rubrics."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. I need the exact criteria names and scoring rubrics."
  }
}
```

</details>

---


### Tool result

_source line 345 · 2026-05-18T12:34:15.114622+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## Primary Evaluation Dimensions

**1. Reviewer Confidence**
- Scale: 1-5
- "5 = Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- Level 4: High confidence with minor gaps possible
- Level 3: Adequate familiarity but incomplete detail review
- Level 2: Defense possible despite significant uncertainty
- "1 = Not my area, or paper is very hard to understand"

**2. Soundness**
- Scale: 1-5 (with .5 increments)
- "5 = Excellent: This study is one of the most thorough I have seen"
- "4 = Strong: This study provides sufficient support for all of its claims"
- "3 = Acceptable: This study provides sufficient support for its main claims"
- "2 = Poor: Some of the main claims are not sufficiently supported"
- "1 = Major Issues: This study is not yet sufficiently thorough to warrant publication"

**3. Excitement**
- Scale: 1-5 (with .5 increments)
- "5 = Highly Exciting: I would recommend this paper to others"
- "4 = Exciting: I would mention this paper to others"
- "3 = Interesting: I might mention some points of this paper"
- "2 = Potentially Interesting: does not resonate with me"
- "1 = Not Exciting: does not resonate with me"

**4. Overall Assessment**
- Scale: 1-5 (with .5 increments)
- "5 = Consider for Award: up to top 2.5% papers"
- "4 = Conference: could be accepted"
- "3 = Findings: could be accepted to Findings"
- "2 = Resubmit next cycle: needs substantial revisions"
- "1 = Do not resubmit"

**5. Reproducibility**
- Scale: 1-5
- "5 = They could easily reproduce the results"
- "4 = They could mostly reproduce the results"
- "3 = They could reproduce with some difficulty"
- "2 = They would be hard pressed to reproduce"
- "1 = They would not be able to reproduce"

**6. Datasets Value**
- Scale: 1-5
- "5 = Enabling: should affect research choices"
- "4 = Useful: would recommend to researchers"
- "3 = Potentially useful: Someone might find useful"
- "2 = 
…[truncated 287 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7532
}
```

</details>

---


### Tool call

_source line 346 · 2026-05-18T12:34:24.300717+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/9f1d1d19-64e8-4613-9864-3e1bb48676c6/tool-results/mcp-agent-ml-research-pdf_to_images-1779107634924.txt | python3 -c \"import sys,json; d=json.load(sys.stdin); r=json.loads(d['result']); print('success:', r['success']); print('pages:', list(r['data'].keys()))\"",
  "description": "Check structure of PDF rendering output"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/9f1d1d19-64e8-4613-9864-3e1bb48676c6/tool-results/mcp-agent-ml-research-pdf_to_images-1779107634924.txt | python3 -c \"import sys,json; d=json.load(sys.stdin); r=json.loads(d['result']); print('success:', r['success']); print('pages:', list(r['data'].keys()))\"",
    "description": "Check structure of PDF rendering output"
  }
}
```

</details>

---


### Tool result

_source line 347 · 2026-05-18T12:34:24.552064+00:00_

success: True
pages: ['images', 'total_pages', 'rendered_pages', 'dpi', 'output_dir']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 348 · 2026-05-18T12:34:33.437770+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/9f1d1d19-64e8-4613-9864-3e1bb48676c6/tool-results/mcp-agent-ml-research-pdf_to_images-1779107634924.txt | python3 -c \"import sys,json; d=json.load(sys.stdin); r=json.loads(d['result']); imgs=r['data']['images']; print('total_pages:', r['data']['total_pages']); print('rendered:', r['data']['rendered_pages']); print('output_dir:', r['data']['output_dir']); [print(f'  page {i[\\\"page\\\"]}: {i[\\\"path\\\"]}') for i in imgs]\"",
  "description": "List rendered page image paths"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/9f1d1d19-64e8-4613-9864-3e1bb48676c6/tool-results/mcp-agent-ml-research-pdf_to_images-1779107634924.txt | python3 -c \"import sys,json; d=json.load(sys.stdin); r=json.loads(d['result']); imgs=r['data']['images']; print('total_pages:', r['data']['total_pages']); print('rendered:', r['data']['rendered_pages']); print('output_dir:', r['data']['output_dir']); [print(f'  page {i[\\\"page\\\"]}: {i[\\\"path\\\"]}') for i in imgs]\"",
    "description": "List rendered page image paths"
  }
}
```

</details>

---


### Tool result

_source line 349 · 2026-05-18T12:34:33.592503+00:00_

total_pages: 14
rendered: 8
output_dir: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images
  page 1: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p1.png
  page 2: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p2.png
  page 3: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p3.png
  page 4: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p4.png
  page 5: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p5.png
  page 6: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p6.png
  page 7: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p7.png
  page 8: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p8.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 154
}
```

</details>

---


### Tool call

_source line 350 · 2026-05-18T12:34:36.905746+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 351 · 2026-05-18T12:34:37.509831+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 352 · 2026-05-18T12:34:37.714212+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 353 · 2026-05-18T12:34:38.418198+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 354 · 2026-05-18T12:34:39.475889+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2570
}
```

</details>

---


### Tool result

_source line 355 · 2026-05-18T12:34:40.938661+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3428
}
```

</details>

---


### Tool result

_source line 356 · 2026-05-18T12:34:41.040115+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3325
}
```

</details>

---


### Tool result

_source line 357 · 2026-05-18T12:34:41.192742+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2774
}
```

</details>

---


### Tool call

_source line 358 · 2026-05-18T12:34:44.707535+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 359 · 2026-05-18T12:34:45.314206+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 360 · 2026-05-18T12:34:45.766443+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 361 · 2026-05-18T12:34:46.220215+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 362 · 2026-05-18T12:34:47.081696+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2374
}
```

</details>

---


### Tool result

_source line 363 · 2026-05-18T12:34:48.594105+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3279
}
```

</details>

---


### Tool result

_source line 364 · 2026-05-18T12:34:49.046478+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3280
}
```

</details>

---


### Tool result

_source line 365 · 2026-05-18T12:34:49.047251+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2827
}
```

</details>

---


### Tool call

_source line 366 · 2026-05-18T12:34:53.464862+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
  "pages": "9-14",
  "dpi": "180"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
    "pages": "9-14",
    "dpi": "180"
  }
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-18T12:34:55.401632+00:00_

Error: result (4,654,914 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/9f1d1d19-64e8-4613-9864-3e1bb48676c6/tool-results/mcp-agent-ml-research-pdf_to_images-1779107695247.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/9f1d1d19-64e8-4613-9864-3e1bb48676c6/tool-results/mcp-agent-ml-research-pdf_to_images-1779107695247.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1936
}
```

</details>

---


### Tool call

_source line 368 · 2026-05-18T12:35:00.120352+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/9f1d1d19-64e8-4613-9864-3e1bb48676c6/tool-results/mcp-agent-ml-research-pdf_to_images-1779107695247.txt | python3 -c \"import sys,json; d=json.load(sys.stdin); r=json.loads(d['result']); imgs=r['data']['images']; [print(f'page {i[\\\"page\\\"]}: {i[\\\"path\\\"]}') for i in imgs]\"",
  "description": "List appendix page paths"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/9f1d1d19-64e8-4613-9864-3e1bb48676c6/tool-results/mcp-agent-ml-research-pdf_to_images-1779107695247.txt | python3 -c \"import sys,json; d=json.load(sys.stdin); r=json.loads(d['result']); imgs=r['data']['images']; [print(f'page {i[\\\"page\\\"]}: {i[\\\"path\\\"]}') for i in imgs]\"",
    "description": "List appendix page paths"
  }
}
```

</details>

---


### Tool result

_source line 369 · 2026-05-18T12:35:00.321561+00:00_

page 9: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p9.png
page 10: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p10.png
page 11: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p11.png
page 12: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p12.png
page 13: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p13.png
page 14: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p14.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 370 · 2026-05-18T12:35:03.384082+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


## Round 14

## Round 14

80 recorded events


### User

_source line 371 · 2026-05-18T14:11:31.019796+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1

**你的侧重：方法严谨性 + 实验有效性**

### 投稿信息
- 论文路径：`projects/distill_sparse_swiglu/paper/main.tex`（多文件结构，各章节为独立 .tex）
- 目标 venue：**EMNLP 2026**（ACL Rolling Review May 2026 cycle）
- 截止日期：2026-05-25
- 页数限制：Long paper 8 页正文 + 无限引用/Limitations/Ethics
- 模板：ACL 官方模板，`\usepackage[review]{acl}`
- 双盲评审
- 强制 Limitations section + Responsible NLP Research Checklist

### 论文概要
标题："Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs"
核心贡献：用 KL 散度（而非 BCE）训练 SwiGLU LLM 的稀疏性预测器，消除补偿网络需求。在 LLaMA-3.1-8B 上验证，跨架构到 Mistral-7B 和 Qwen-2.5-14B。

### 你需要重点审查的方面

1. **技术正确性**
   - 梯度分析（§3.6 BCE vs KL gradient structure）是否数学正确？推导是否 rigorous？
   - Gumbel-Sigmoid relaxation 的使用是否合理？温度退火策略是否有理论依据？
   - Adaptive penalty controller（§3.5）的收敛保证？30% 目标偏差 5% 是否影响结论？

2. **实验设计与统计**
   - 主要 claim 的统计支撑是否充分？哪些关键对比有 multi-seed，哪些只有单 seed？
   - Iso-compute 对比（§4.2）是否公平？BCE 2700 步 vs KL 1000 步的 wall-clock 对齐是否合理？
   - Oracle F1 分析（F1 高但 PPL 差）的论证是否 sound？是否存在 confound？
   - OOD 评估（C4）的覆盖是否充分？

3. **消融完整性**
   - Table 3 的消融是否覆盖所有关键设计选择？
   - BCE+Gumbel+Penalty 消融是否公平隔离了 loss function 的贡献？
   - 是否存在遗漏的关键消融（如 KL-derived masks 作为 BCE targets）？

4. **可复现性**
   - 超参数是否完整报告？
   - 训练/评估 protocol 是否清晰可复现？
   - GPU 硬件信息是否充分？

5. **Claims 与 Evidence 对齐**
   - "renders compensation redundant" 的 claim 是否有充分实验支撑？
   - 三 regime 分析（30%/40%/50%）每个 regime 仅一个数据点，claim 强度是否匹配？
   - 14B 结果（KL PPL 好但 MMLU 差 8pp）与整体叙事是否一致？

请按 ARR reviewer guidelines 格式输出完整审稿意见：Summary → Strengths → Weaknesses (Critical/Major/Minor) → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）→ Detailed Comments。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-18T14:11:40.308209+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 373 · 2026-05-18T14:11:40.409312+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 374 · 2026-05-18T14:11:45.479540+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14"
  }
}
```

</details>

---


### Tool result

_source line 375 · 2026-05-18T14:11:45.531114+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 376 · 2026-05-18T14:11:48.342729+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14"
  }
}
```

</details>

---


### Tool result

_source line 377 · 2026-05-18T14:11:48.393457+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 378 · 2026-05-18T14:11:57.312909+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
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

_source line 379 · 2026-05-18T14:11:57.363651+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 380 · 2026-05-18T14:12:01.181581+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 381 · 2026-05-18T14:12:01.683741+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "paper/**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 382 · 2026-05-18T14:12:02.085806+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 383 · 2026-05-18T14:12:02.137217+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "paper/**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "paper/**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 384 · 2026-05-18T14:12:02.187921+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 385 · 2026-05-18T14:12:11.679481+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

I found comprehensive information about ACL Rolling Review 2026 reviewer guidelines and review form criteria. Here's what I found:

## Reviewer Guidelines

When accepting a reviewing request for an ARR cycle, reviewers receive a kick-off email from OpenReview listing important
…[truncated 1720 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 10497
}
```

</details>

---


### Tool call

_source line 386 · 2026-05-18T14:12:16.450270+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 387 · 2026-05-18T14:12:16.701677+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 388 · 2026-05-18T14:12:18.257941+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all fields, scoring dimensions, score ranges, and descriptions. I need the exact scoring criteria for each dimension (e.g., soundness, overall assessment, confidence, etc.) with their numeric scales and what each number means."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all fields, scoring dimensions, score ranges, and descriptions. I need the exact scoring criteria for each dimension (e.g., soundness, overall assessment, confidence, etc.) with their numeric scales and what each number means."
  }
}
```

</details>

---


### Tool result

_source line 389 · 2026-05-18T14:12:25.037218+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## 2. **Soundness**
Scale: 1-5 (with half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. **Excitement**
Scale: 1-5 (with half-point increments)
- **5**: "Highly Exciting: I would recommend this paper to others."
- **4**: "Exciting: I would mention this paper to others."
- **3**: "Interesting: I might mention some points to others."
- **2**: "Potentially Interesting: does not resonate with me, but might with others."
- **1**: "Not Exciting: does not resonate with me, and I don't think it would with others."

## 4. **Overall Assessment**
Scale: 1-5 (with half-point increments)
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance
- **3**: Findings acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit

## 5. **Reproducibility**
Scale: 1-5
- **5**: "They could easily reproduce the results."
- **4**: "They could mostly reproduce the results."
- **3**: "They could reproduce the results with some difficulty."
- **2**: "They would be hard pressed to reproduce the results."
- **1**: "They would not be able to reproduce the results."

## 6. **Datasets & Software Value**
Scale: 1-5 (
…[truncated 292 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6779
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-18T14:12:27.807626+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 391 · 2026-05-18T14:12:27.858355+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	
17	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
18	
19	\author{Anonymous}
20	
21	\begin{document}
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
32	\input{conclusion}
33	\input{limitations}
34	\input{ethics}
35	
36	\bibliography{references}
37	
38	\input{appendix}
39	
40	\end{document}
41	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 392 · 2026-05-18T14:12:31.322074+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "paper/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 393 · 2026-05-18T14:12:31.372764+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 394 · 2026-05-18T14:12:35.500232+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/",
  "description": "List paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/",
    "description": "List paper directory contents"
  }
}
```

</details>

---


### Tool result

_source line 395 · 2026-05-18T14:12:35.651302+00:00_

_pdf_images
abstract.tex
acl.sty
acl_natbib.bst
appendix.tex
conclusion.tex
ethics.tex
experiments.tex
introduction.tex
limitations.tex
main.aux
main.bbl
main.blg
main.fdb_latexmk
main.fls
main.log
main.out
main.pdf
main.tex
method.tex
references.bib
related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 396 · 2026-05-18T14:12:38.763141+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 397 · 2026-05-18T14:12:39.266621+00:00_

1	We study whether end-to-end KL distillation can replace per-neuron classification for activation sparsity prediction in SwiGLU LLMs.
2	Existing predictors trained with binary cross-entropy (BCE) optimize each neuron independently, but inference allocates sparsity budgets via global top-$k$ across all layers.
3	Gradient analysis reveals a structural mismatch: BCE's per-neuron gradient is blind to cross-neuron interactions and achieves higher oracle F1 yet 139\% worse perplexity than a KL-trained predictor.
4	A lightweight predictor ($<$1\% of base parameters) trained with forward KL and Gumbel-Sigmoid relaxation resolves this mismatch by coupling all neurons through the output distribution, rendering post-hoc compensation (+67.2M params) redundant at both 30\% and 50\% sparsity.
5	On LLaMA-3.1-8B at the recommended 30\% sparsity, KL reduces PPL degradation 18\% over TEAL; uniform allocation provides $7.5\times$ smaller cross-seed downstream $\sigma$, eliminating seed-dependent instability.
6	At 50\% sparsity, the PPL advantage widens to 49\% but downstream tasks degrade regardless of allocation, revealing allocation-dependent operating regions at 7--8B scale.
7	Evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms the PPL advantage across 7--14B, though 14B reveals a scale-dependent MMLU gap not resolved by allocation strategy.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 398 · 2026-05-18T14:12:39.267112+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 399 · 2026-05-18T14:12:40.120585+00:00_

1	\section{Introduction}
2	
3	SwiGLU feed-forward networks~\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they universally rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: TEAL's top-$k$ mechanism~\cite{liu2025teal} ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	
8	We provide this analysis.
9	The gradient of BCE with respect to neuron $j$'s score is $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$, a function of $j$ alone, independent of every other neuron.
10	Under KL divergence, the gradient for neuron $j$ in layer $\ell$ factors as:
11	\begin{equation*}
12	\frac{\partial \mathcal{L}_{\text{KL}}}{\partial s_j^{(\ell)}} = \frac{\partial \mathcal{L}_{\text{KL}}}{\partial \mathbf{z}} \cdot \frac{\partial \mathbf{z}}{\partial \mathbf{h}^{(\ell)}} \cdot \frac{\partial \mathbf{h}^{(\ell)}}{\partial \tilde{m}_j^{(\ell)}} \cdot \frac{\partial \tilde{m}_j^{(\ell)}}{\partial s_j^{(\ell)}},
13	\end{equation*}
14	where the Jacobian $\partial \mathbf{z} / \partial \mathbf{h}^{(\ell)}$ propagates through all downstream layers, coupling each neuron's gradient to every other neuron's mask state.
15	This structural difference predicts that KL should outperform BCE specifically under global allocation, and the prediction is confirmed empirically: BCE achieves higher oracle F1 (0.613 vs.\ 0.540) yet produces 139\% worse perplexity, because per-neuron magnitude accuracy is a misaligned proxy for output-distribution preser
…[truncated 1574 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 400 · 2026-05-18T14:12:40.171295+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 401 · 2026-05-18T14:12:40.673066+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} predicts activation sparsity patterns from attention outputs without additional training.
6	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
7	
8	\paragraph{Predictor-Based Contextual Sparsity.}
9	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
10	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
11	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
12	SVD-CSP~\cite{serbin2026svdcsp} compresses sparsity predictors via SVD decomposition for reduced predictor overhead.
13	PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.
14	MaskLLM~\cite{fang2024maskllm} also employs learnable masks with Gumbel relaxation and frozen weights, but targets N:M semi-structured \emph{weight} sparsity (2:4 patterns) via per-group categorical selection (Gumbel-Softmax), producing fixed masks independent of input tokens.
15	Both share the principle of frozen weights + learnable masks + KL training, but solve distinct optimization problems: MaskLLM finds optimal static N:M patterns within fixed groups
…[truncated 2535 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 402 · 2026-05-18T14:12:40.824138+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 403 · 2026-05-18T14:12:40.824758+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models.
5	The method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass and achieves competitive performance without auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{h}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importance scores from the pre-FFN hidden sta
…[truncated 14198 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 404 · 2026-05-18T14:12:41.125785+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 405 · 2026-05-18T14:12:41.577583+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4, using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $5 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly; (2) \textbf{BCE predictor} (DejaVu-style~\cite{liu2023dejavu}), trained with per-neuron binary cross-entropy on magnitude-based oracle masks for 1000 and 2700 steps; (3) \textbf{Uniform allocation}, which distributes the sparsity budget equally across layers; and (4) \textbf{WINA}
…[truncated 16396 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 406 · 2026-05-18T14:12:41.577948+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 407 · 2026-05-18T14:12:42.029401+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	\vspace{-4pt}
4	
5	KL distillation replaces per-neuron BCE with output-distribution coupling: a predictor ($<$1\% of base) halves TEAL's perplexity across 7--14B, with compensation (+67.2M params) redundant at both tested sparsity levels.
6	At 30\%, uniform allocation delivers $7.5\times$ smaller cross-seed $\sigma$; allocation-aware evaluation is essential since perplexity alone is a poor downstream proxy.
7	At 14B, the PPL advantage persists but an MMLU gap emerges, a scale-dependent tradeoff warranting further investigation.
8	
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 408 · 2026-05-18T14:12:42.029903+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 409 · 2026-05-18T14:12:42.481225+00:00_

1	\section*{Limitations}
2	
3	Our primary evaluation uses WikiText-2 perplexity, and downstream benchmarks reveal that perplexity is a poor proxy for reasoning ability at moderate sparsity: 40\% sparsity achieves PPL 8.36 but MMLU already degrades, motivating 30\% as the recommended operating point for downstream fidelity.
4	Training requires 1000 steps on WikiText-103 ($\sim$45 minutes on RTX PRO 6000 for KL, $\sim$17 minutes for BCE), but a separate predictor must be trained for each sparsity target.
5	Our recommended operating point (30\% sparsity, uniform allocation) is validated at 7--8B scale; at 14B, the MMLU gap persists regardless of allocation strategy (\S\ref{sec:14b}). Scaling to 70B remains untested.
6	Out-of-distribution evaluation (Appendix~\ref{app:ood}) covers 30\% and 50\% sparsity on C4; extending to 70\% is left to future work.
7	Our attribution of KL's advantage to gradient coupling (\S\ref{sec:method:gradient}) is supported by SNR measurements and the BCE isolation ablation, but does not fully disentangle coupling from oracle quality: BCE uses magnitude-based oracles while KL directly optimizes output preservation, and an ablation using KL-derived masks as BCE targets would more precisely isolate the coupling effect.
8	At 30\% sparsity, global allocation exhibits 9.5pp cross-seed MMLU standard deviation (3-seed); allocation strategy interacts with predictor initialization in task-specific ways. This variance is MMLU-specific, as ARC, WinoGrande, and GSM8K show stable performance across seeds under both allocation strategies.
9	While we motivate our work with inference speedup potential, actual wall-clock acceleration depends on sparse kernel implementations (e.g., Triton, cuSPARSE) and hardware-specific memory access patterns; this work focuses on prediction quality rather than systems optimization.
10	Future directions include N:M structured sparsity for hardware-native acceleration, scaling to 13B+ models, and training a single predictor that
…[truncated 53 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 410 · 2026-05-18T14:12:42.531775+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 411 · 2026-05-18T14:12:43.033829+00:00_

1	\section*{Ethics Statement}
2	
3	This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, MMLU, GSM8K).
4	No new data collection, annotation, or human subjects are involved.
5	The method does not alter model outputs beyond the sparsity-induced degradation we analyze; it introduces no new generation capabilities or safety risks beyond those inherent in the base models.
6	Compute requirements are modest (1000 training steps, $\sim$45 minutes on a single GPU for KL training), presenting minimal environmental concern relative to the pretrained models we evaluate on.
7	We release no model weights or user-facing systems; our contribution is analytical (understanding KL distillation for sparsity) rather than deployment-oriented.
8	
9	\section*{Responsible NLP Research Checklist}
10	
11	\paragraph{A. Limitations and Risks.}
12	\begin{itemize}[nosep,leftmargin=*]
13	\item[\textbf{A1.}] Limitations are discussed in the Limitations section. Key limitations: evaluation limited to 7--8B models; perplexity is an imperfect proxy for downstream quality; wall-clock speedup requires sparse kernel support not implemented here.
14	\item[\textbf{A2.}] No foreseeable risks specific to this work beyond those inherent in the base language models. The method does not enable new capabilities or applications.
15	\end{itemize}
16	
17	\paragraph{B. Scientific Artifacts.}
18	\begin{itemize}[nosep,leftmargin=*]
19	\item[\textbf{B1.}] Yes. All models (LLaMA-3.1-8B~\cite{grattafiori2024llama3}, Mistral-7B-v0.3~\cite{jiang2023mistral}), datasets (WikiText~\cite{merity2017pointer}, C4~\cite{raffel2020c4}), and methods (TEAL~\cite{liu2025teal}, SPON~\cite{xu2026spon}) are cited with original references.
20	\item[\textbf{B2.}] LLaMA-3.1 is released under the Llama 3.1 Community License; Mistral-7B under Apache 2.0. WikiText a
…[truncated 1816 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 412 · 2026-05-18T14:12:43.034250+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 413 · 2026-05-18T14:12:43.486258+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); KL distillation thus provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overhead; net ac
…[truncated 12466 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 414 · 2026-05-18T14:12:43.486765+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 415 · 2026-05-18T14:12:43.539757+00:00_

1	% =============================================================================
2	% Direction 1: KL distillation for structured/activation sparsity
3	% =============================================================================
4	
5	@inproceedings{fang2024maskllm,
6	  title = {MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models},
7	  author = {Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff Pool and Jan Kautz and Pavlo Molchanov and Xinchao Wang},
8	  year = {2024},
9	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
10	  url = {https://arxiv.org/abs/2409.17481},
11	}
12	
13	@inproceedings{xu2026spon,
14	  title = {Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models},
15	  author = {Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma},
16	  year = {2025},
17	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
18	  url = {https://arxiv.org/abs/2512.12744},
19	}
20	
21	@inproceedings{muralidharan2024minitron,
22	  title = {Compact Language Models via Pruning and Knowledge Distillation},
23	  author = {Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marcin Chochowski and Mostofa Patwary and Mohammad Shoeybi and Bryan Catanzaro and Jan Kautz and Pavlo Molchanov},
24	  year = {2024},
25	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
26	  url = {https://arxiv.org/abs/2407.14679},
27	}
28	
29	
30	% =============================================================================
31	% Direction 3: SPON and learnable bias correction for sparsity
32	% =============================================================================
33	
34	@article{gautam2026fastforward,
35	  title = {Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity},
36	  author = {Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott and Naras
…[truncated 15271 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 416 · 2026-05-18T14:12:51.873198+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool call

_source line 417 · 2026-05-18T14:12:52.475637+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
  "pages": "1-12",
  "dpi": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
    "pages": "1-12",
    "dpi": "200"
  }
}
```

</details>

---


### Tool result

_source line 418 · 2026-05-18T14:13:22.955299+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 39, \"total_citations\": 76, \"unique_cited_keys\": 39, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 35, \"online_not_found\": 0, \"online_mismatch\": 4}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"fang2024maskllm\", \"type\": \"inproceedings\", \"title\": \"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models\", \"authors\": \"Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff P...\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"xu2026spon\", \"type\": \"inproceedings\", \"title\": \"Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models\", \"authors\": \"Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Machine Learning (ICML)\"}, {\"key\": \"muralidharan2024minitron\", \"type\": \"inproceedings\", \"title\": \"Compact Language Models via Pruning and Knowledge Distillation\", \"authors\": \"Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marci...\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"gautam2026fastforward\", \"type\": \"article\", \"title\": \"Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity\", \"authors\": \"Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott ...\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2602.00397\"}, {\"key\": \"liu2025teal\", \"type\": \"inproceedings\", \"title\": \"Training-Free Activation Sparsity in Large Language Models\", \"authors\": \"James Liu and Pragaash Ponnusamy and Tianle Cai and Han Guo and Yoon Kim and Ben...\", \"year
…[truncated 31237 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 31082
}
```

</details>

---


### Tool result

_source line 419 · 2026-05-18T14:13:33.692277+00:00_

Error: result (10,899,577 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/6ed52efa-b8bb-4cfe-a5af-66eca733a642/tool-results/mcp-agent-ml-research-pdf_to_images-1779113613127.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/6ed52efa-b8bb-4cfe-a5af-66eca733a642/tool-results/mcp-agent-ml-research-pdf_to_images-1779113613127.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 41216
}
```

</details>

---


### Tool call

_source line 420 · 2026-05-18T14:13:39.369618+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
  "pages": "1",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
    "pages": "1",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 421 · 2026-05-18T14:13:39.924364+00:00_

Error: result (599,387 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/6ed52efa-b8bb-4cfe-a5af-66eca733a642/tool-results/mcp-agent-ml-research-pdf_to_images-1779113619875.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-review-reviewer-1-772f066c/6ed52efa-b8bb-4cfe-a5af-66eca733a642/tool-results/mcp-agent-ml-research-pdf_to_images-1779113619875.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 554
}
```

</details>

---


### Tool call

_source line 422 · 2026-05-18T14:13:43.739254+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/",
  "description": "List PDF image files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/",
    "description": "List PDF image files"
  }
}
```

</details>

---


### Tool result

_source line 423 · 2026-05-18T14:13:43.840164+00:00_

total 8776
drwxr-xr-x 2 ubuntu ubuntu   4096 May 18 14:13 .
drwxr-xr-x 3 ubuntu ubuntu   4096 May 18 13:58 ..
-rw-r--r-- 1 ubuntu ubuntu 449176 May 18 14:13 main_p1.png
-rw-r--r-- 1 ubuntu ubuntu 761848 May 18 14:13 main_p10.png
-rw-r--r-- 1 ubuntu ubuntu 783960 May 18 14:13 main_p11.png
-rw-r--r-- 1 ubuntu ubuntu 591664 May 18 14:13 main_p12.png
-rw-r--r-- 1 ubuntu ubuntu 485894 May 18 12:34 main_p13.png
-rw-r--r-- 1 ubuntu ubuntu 442042 May 18 12:34 main_p14.png
-rw-r--r-- 1 ubuntu ubuntu 755945 May 18 14:13 main_p2.png
-rw-r--r-- 1 ubuntu ubuntu 662790 May 18 14:13 main_p3.png
-rw-r--r-- 1 ubuntu ubuntu 576460 May 18 14:13 main_p4.png
-rw-r--r-- 1 ubuntu ubuntu 700975 May 18 14:13 main_p5.png
-rw-r--r-- 1 ubuntu ubuntu 697312 May 18 14:13 main_p6.png
-rw-r--r-- 1 ubuntu ubuntu 630928 May 18 14:13 main_p7.png
-rw-r--r-- 1 ubuntu ubuntu 690066 May 18 14:13 main_p8.png
-rw-r--r-- 1 ubuntu ubuntu 722066 May 18 14:13 main_p9.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 424 · 2026-05-18T14:13:47.104207+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 425 · 2026-05-18T14:13:47.607200+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 426 · 2026-05-18T14:13:48.060871+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 427 · 2026-05-18T14:13:48.062337+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 428 · 2026-05-18T14:13:49.119205+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 429 · 2026-05-18T14:13:49.373214+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 430 · 2026-05-18T14:13:51.237830+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3630
}
```

</details>

---


### Tool result

_source line 431 · 2026-05-18T14:13:51.641036+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3578
}
```

</details>

---


### Tool result

_source line 432 · 2026-05-18T14:13:52.847854+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3728
}
```

</details>

---


### Tool result

_source line 433 · 2026-05-18T14:13:52.848997+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3475
}
```

</details>

---


### Tool call

_source line 434 · 2026-05-18T14:13:59.596910+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 435 · 2026-05-18T14:14:03.416383+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3819
}
```

</details>

---


### Tool call

_source line 436 · 2026-05-18T14:14:03.768036+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 437 · 2026-05-18T14:14:04.323131+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 438 · 2026-05-18T14:14:04.380669+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 439 · 2026-05-18T14:14:04.437241+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 440 · 2026-05-18T14:14:04.945292+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 441 · 2026-05-18T14:14:04.945878+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 442 · 2026-05-18T14:14:12.443577+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 8675
}
```

</details>

---


### Tool result

_source line 443 · 2026-05-18T14:14:12.596789+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 8273
}
```

</details>

---


### Tool result

_source line 444 · 2026-05-18T14:14:12.799542+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 8418
}
```

</details>

---


### Tool result

_source line 445 · 2026-05-18T14:14:13.101772+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 8155
}
```

</details>

---


### Tool result

_source line 446 · 2026-05-18T14:14:13.102918+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 8665
}
```

</details>

---


### Tool result

_source line 447 · 2026-05-18T14:14:13.104728+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 8159
}
```

</details>

---


### Tool call

_source line 448 · 2026-05-18T14:17:41.335728+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 — Round 1 审稿意见\n\n**论文**: \"Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\"\n**Venue**: EMNLP 2026 (ACL Rolling Review May 2026 cycle)\n\n---\n\n## 总体评分\n**Overall**: 3.0 / 5 — Findings\n**一句话总结**: 观察到 KL 蒸馏优于 BCE 用于稀疏性预测是有价值的实证贡献，但核心因果 claim 存在未解的混淆变量（oracle target quality vs. gradient coupling），14B 结果与主叙事矛盾，且无实际推理加速演示。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3 / 5 | 梯度分析结构正确，但 BCE vs KL 对比存在已知混淆变量（论文自身承认），regime 分析每个 regime 仅 1 个数据点 |\n| Excitement | 3 / 5 | KL > BCE 的观察有用且可能启发后续工作，但无实际加速且 14B 结果限制了 claim 的普适性 |\n| Reproducibility | 4 / 5 | 超参数报告完整，硬件明确，关键结果有 multi-seed；但 SNR 计算细节缺失 |\n| Confidence | 4 / 5 | 熟悉稀疏性预测和蒸馏文献，仔细阅读了全文 |\n\n---\n\n## Summary\n\n本文研究用 forward KL 蒸馏替代 per-neuron BCE 训练 SwiGLU LLM 的稀疏性预测器。核心观察是：BCE 的梯度对每个 neuron 独立，而 KL 的梯度通过下游层的 Jacobian 耦合所有 neuron，更适合 TEAL 的 global top-k 推理分配。在 LLaMA-3.1-8B 上，KL 预测器（75.9M 参数）在 30% 和 50% 稀疏度下均优于 TEAL，并使补偿网络（+67.2M 参数）成为冗余。跨架构验证覆盖 Mistral-7B 和 Qwen-2.5-14B。论文还分析了三个\"operating regions\"并报告了 allocation-dependent 行为。\n\n---\n\n## 主要优势\n\n1. **梯度分析清晰且有启发性**（§3.6）：BCE gradient $\\partial \\mathcal{L}/\\partial s_j = \\sigma(s_j) - m_j^*$ 仅依赖 neuron $j$，而 KL gradient 通过 Jacobian factor (b) 耦合所有 neuron。这是一个简洁有力的 structural observation，即使论文未能完全证明它是性能差异的唯一来源。\n\n2. **诚实报告负面结果**：14B MMLU gap（63.7% vs 71.8%，Table 7）、无 wall-clock speedup、30% 下 global allocation 的 seed 不稳定性（MMLU σ=9.5pp）——这些对论文叙事不利的结果都被如实报告并讨论，这是值得称赞的。\n\n3. **消融设计较完整**（Table 3）：覆盖 divergence direction（forward/reverse/JSD）、relaxation method（Gumbel vs STE）、loss function isolation（BCE+Gumbel+Penalty）、compensation redundancy。每个消融隔离了一个设计选择。\n\n4. **跨架构验证**（Table 6）：LLaMA-8B、Mistral-7B、Qwen-14B 三个架构的 PPL 优势一致（30%: 1.22-1.24×, 50%: 1.98-2.12×），增强了方法的普适性 claim。\n\n5. **Taxonomy（Table 1）**将 prior work 按 correction granularity × training signal coupling 组织，定位清晰。\n\n6. **写作质量高**：结构紧凑，数学符号一致，表格信息密度高。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 核心因果 claim 存在未隔离的混淆变量\n- 具体位置：§4.3（第 7 页）、Limitations（第 9 页）\n- 问题：论文的核心叙事是\"梯度耦合（gradient coupling）使 KL 优于 BCE\"。但 BCE 使用 magnitude-based oracle masks 作为 target，而 KL 直接优化输出分布——这是两个同时变化的变量（training objective 和 implicit target quality）。论文自身在 §4.3 明确承认：\"an ablation using KL-derived masks as BCE targets would isolate the effect\"，但未执行该消融。\n- 现有证据的局限：Oracle F1 分析（BCE 0.613 vs KL 0.540，但 KL PPL 好 139%）说明 per-neuron accuracy 不等于 output preservation，但无法区分这是因为（a）KL 的梯度耦合更好，还是（b）magnitude-based oracle masks 本身就是次优 target。如果 BCE 使用 KL-derived masks（即\"正确的\" target），表现是否仍差？这是一个可执行的消融。\n- 为什么影响接收：这是 contribution 1 和 2 的根基。如果改善主要来自 target quality 而非 gradient coupling，论文的主要叙事（structural mismatch → coupled gradient → better allocation）就需要重新 frame。\n- 建议修改方向：执行 KL-derived masks as BCE targets 消融（论文自己提出了这个实验）。即使 KL 仍胜出，结果也会更 conclusive；即使 BCE 缩小差距，也是有价值的发现，可以修改 framing 为\"both target quality and coupling matter\"。\n\n**N2** [critical] \"Three Operating Regions\" 分析证据不足\n- 具体位置：§4.5（Table 5），第 8 页\n- 问题：论文声称存在三个 qualitatively distinct 的 operating regions（budget-surplus ≤30%、budget-constrained ~40%、capacity-limited ≥50%），但每个 regime 只有 **一个数据点**（30%、40%、50%），且 40% 仅单 seed。论文承认\"Denser sampling (e.g., 35% sparsity) would be needed to precisely locate region boundaries\"，但仍然在正文中强调\"三个 regions\"作为核心发现之一。\n- 具体缺陷：\n  - 40% regime：global MMLU 38.06% vs uniform 30.68%（+7.4pp），但这是**单 seed**结果。考虑到 30% global MMLU 的 σ=9.5pp，40% 的 7.4pp 差异可能在 seed variance 之内。\n  - 边界不确定：30% 和 40% 之间的行为（35%? 37%?）完全未知，40% 和 50% 之间同理。\n  - 30% 的 regime 标签\"budget-surplus\"暗示 30% 是\"容易的\"，但 30% 的 PPL 已比 dense 恶化 47%（8.96/6.12），downstream 显著退化。\n- 为什么影响接收：这是 contribution 3 的主体。以 3 个点声称\"三个 qualitative phases\"在统计上不严格。\n- 建议修改方向：（1）在 25%、35%、45% 补充至少 2-seed 实验以确认 regime boundaries；或（2）将 framing 弱化为\"preliminary observations suggesting allocation-dependent behavior\"而非 distinct operating regions。\n\n**N3** [critical] 14B 结果与核心 claim 显著矛盾，解释不充分\n- 具体位置：§4.6（Table 7），第 8 页\n- 问题：在 Qwen-2.5-14B 30% 稀疏度下，KL PPL 最优（7.62 vs TEAL 8.73），但 MMLU 低 8.1pp（63.72% vs 71.83%），GSM8K 低 4.3pp（48.82% vs 53.07%），ARC-c 也略低。在 uniform allocation 下，MMLU 差距仍存在（64.49 vs 66.34）。论文的核心 claim 是\"output-distribution preservation is better than per-neuron classification\"，但 14B 的 downstream 结果表明，PPL 优化不等于 task 保持，且在更大模型上 BCE/TEAL 的 downstream 表现反而更好。\n- 论文的解释（\"Higher knowledge density at 14B may cause KL's output-preservation objective to sacrifice task-specific pathways\"）是推测性的，没有实证支撑。\n- 为什么影响接收：如果方法在 scale up 到 14B 时核心优势反转（PPL 好但 downstream 差），那么\"output-distribution distillation is better\"的 claim 的 generalization scope 需要严格限定。\n- 建议修改方向：（1）在 14B 上测试更多稀疏度（40%, 50%）以确认是否 consistent；（2）分析 14B per-layer retention patterns 与 8B 的差异；（3）修改 claim scope 为明确限定在 7-8B。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] `\\enlargethispage{10\\baselineskip}` 格式操纵\n- 具体位置：experiments.tex 第 253 行\n- 问题：使用 `\\enlargethispage{10\\baselineskip}` 人为扩展第 8 页以容纳更多内容。从 PDF 第 8 页可看到，该页内容密度明显高于其他页（包含 Table 5、Table 6、Table 7、三个 operating regions 分析、SPON 分析、cross-architecture validation、14B 结果、inference efficiency、完整 conclusion）。\n- 为什么重要：ACL 模板明确规定不得修改 margin 和 page layout。虽然技术上不算 desk reject，但审稿人和 AC 经常注意到这类操纵。\n- 建议：将部分实验内容（如 SPON 详细分析）移至 appendix。\n\n**W2** [warning] BCE baseline 比较不完全公平\n- 具体位置：§4.2-4.3（Table 2, Table 3）\n- 问题：\n  - BCE 在 30% 稀疏度下的结果**未在 Table 2 中报告**。既然 30% 是 recommended operating point，这是一个关键缺失。仅在 50% 展示 BCE（PPL 28.13）放大了 KL 的优势。\n  - BCE 和 KL 的 target 不同（magnitude oracle vs output distribution），这不仅是 loss function 的差异，还是 supervision signal 的差异（与 N1 相关但这里聚焦 fairness）。\n  - Isolation ablation（BCE+Gumbel+Penalty = 38.02）比 vanilla BCE（27.97）更差，说明 Gumbel+Penalty 框架与 BCE 不兼容，而非 BCE 在该框架下效果不好。\n- 建议：（1）补充 BCE 30% 结果；（2）测试 BCE with output-based targets 或 BCE without TEAL allocation（用 BCE 自身的 per-layer top-k）。\n\n**W3** [warning] 训练/评估数据同族问题\n- 具体位置：§4.1、Appendix D\n- 问题：训练用 WikiText-103，主要评估用 WikiText-2（同一 WikiText 语料族）。C4 OOD 结果（Appendix D）在 30% 时 PPL 退化为 1.74× dense（vs WikiText-2 的 1.47×），退化更严重。C4 30% 仅 2-seed（vs 主结果 3-seed），且无 C4 downstream 评估。\n- 建议：（1）C4 补充到 3-seed 以匹配主结果的 rigor；（2）报告 C4 上的 downstream benchmarks 或解释为什么 WikiText-2 的 downstream 结果可以 generalize。\n\n**W4** [warning] SNR 分析覆盖不足\n- 具体位置：§3.6（第 5 页），Appendix F\n- 问题：\n  - SNR 仅测量到 step 300，但训练跑 1000 步。Step 300-1000 的 SNR 演化未知。\n  - \"5.14× higher SNR at convergence (step 300)\" ——但 step 300 不是真正的 convergence（Appendix B.2 显示 training converges by step 800）。\n  - SNR 计算的 mini-batch 数量未报告，bootstrap CI 的样本量未报告。\n  - 因果 claim（\"KL's gradient coupling becoming effective only after the predictor learns a coarse mask structure\"）是 post-hoc 解释，未经验证。\n- 建议：（1）将 SNR 测量延伸到 1000 步；（2）报告 mini-batch 数量和 bootstrap 参数；（3）弱化因果 claim 为 correlation observation。\n\n**W5** [warning] Adaptive penalty controller 在 30% 处不收敛\n- 具体位置：Appendix C（Table 12），第 12 页\n- 问题：在 recommended 30% operating point，$\\lambda$ 达到 cap（5000），actual sparsity 28.5%（deviation 5.0%）。论文辩称 TEAL 在 28.5% 的 PPL ≈ 10.7 vs 30% 的 10.97，差异可忽略。但这意味着 KL predictor 实际运行在比标称更低的稀疏度上，给 KL 带来了不公平的 ~1.5% sparsity 优势。Table 2 报告\"30% sparsity\"但实际是 28.5%。\n- 建议：（1）在 Table 2 的 caption 或正文中明确注明 actual sparsity；（2）与 TEAL at 28.5% 做 fair comparison。\n\n**W6** [warning] 无实际推理加速\n- 具体位置：Appendix A（Table 8），第 11-12 页\n- 问题：Pipeline 增加 6.4% overhead（126.78 vs 119.11 ms/fwd）。在 30% recommended sparsity 下，预测器增加 6.3% latency 但未从稀疏性获得任何 speedup（unstructured masks 无法被硬件加速）。论文的 motivation 是推理效率，但实际贡献是 prediction quality 而非 efficiency。\n- 建议：论文诚实地在 Limitations 中讨论了这一点，但建议在 Introduction 中更早 set expectations，避免读者产生效率提升的预期。\n\n---\n\n## 小问题（不影响接收）\n\n1. Figure 1（method overview）出现在第 6 页（实验部分之后才开始的位置），位置偏晚。建议移到 Method section 正文中更早的位置。\n2. \"renders post-hoc compensation redundant\" claim 仅测试了一种 compensation 架构（FastForward-style）。措辞可改为\"renders FastForward-style compensation redundant\"。\n3. Abstract 中 \"7-14B\" 范围暗示 PPL 优势跨 scale 一致，但 14B downstream 结果与此暗示矛盾。\n4. Table 2 caption 注脚说明\"50% uniform PPL is 3-seed (11.92 ± 0.07; Appendix E)\"，但正文 Table 2 中 50% KL uniform 显示为 11.96，不一致。\n5. Downstream benchmark 选择标准未解释——为什么 ARC-c, WG, MMLU, GSM8K 在主表而 HellaSwag, PIQA, BoolQ 在 appendix？\n6. Appendix 引用完整性：正文提到 Appendix H (app:downstream) 但编号可能需要检查（appendix 使用字母编号 A-F）。\n\n---\n\n## Missing References\n\n引用验证结果：39 条 bib entries 全部被引用，无 orphan/missing。OpenAlex 验证 35 条通过，4 条 minor mismatch（author name formatting）。\n\n建议补充考虑的参考文献：\n- **Griffin (De Vries et al., 2024)** 或其他 gated linear unit variant 的稀疏性工作\n- **Mixture-of-Experts 稀疏性与 activation sparsity 的交叉文献**（如 Expert Choice routing）——Table 1 taxonomy 可能遗漏了 MoE-based 方法作为\"coupled + per-token\"的另一个 cell\n\n---\n\n## Detailed Comments\n\n### 技术正确性\n\n1. **梯度分析（§3.6）数学正确**：BCE gradient 分解（Eq. 9-10）和 KL gradient chain rule（Eq. 11）的结构分析是正确的。Factor (b) $\\partial \\mathbf{z}/\\partial \\mathbf{h}^{(\\ell)}$ 确实通过下游层耦合所有 neuron。\n\n2. **Gumbel-Sigmoid relaxation（§3.3）使用合理**：温度退火 1.0→0.1 是标准做法（Jang et al. 2017; Maddison et al. 2017）。STE 对比（PPL 15.77 vs 11.79）有效展示了 smooth relaxation 的价值。但温度 schedule sensitivity（Appendix B.1）显示 fixed τ=0.5 实际上略好于 default schedule（PPL 11.861 vs 11.963），这与正文描述的 annealing 动机（\"从 exploration 到 exploitation\"）矛盾。\n\n3. **Adaptive penalty controller（§3.5）收敛保证**：论文明确在 footnote 中说明这不是 formal dual method，不保证 KKT satisfaction。这是诚实的。但 30% 处 5% deviation（28.5% actual）不可忽略——在 PPL scale 上 1.5% sparsity 差异约 0.3 PPL，而 KL vs TEAL 差异为 2.0 PPL，所以影响有限但应注明。\n\n### 实验设计\n\n4. **Iso-compute 对比（§4.3）基本公平**：BCE 2700 步 ≈ 46min vs KL 1000 步 ≈ 45min。Wall-clock 时间匹配合理（KL 需要 dense forward pass + sparse forward pass per step，计算量更大）。但 BCE 2700 步是否收敛？论文说 PPL 28.13±0.20，没有报告 training loss curve 是否已 plateau。如果 BCE training loss 仍在下降，更多步数可能进一步缩小差距。\n\n5. **Oracle F1 分析（§4.3）论证基本 sound**：F1 高但 PPL 差确实说明 per-neuron accuracy 是 misaligned proxy。但 confound 是：BCE 的 oracle masks 来自 magnitude ranking（TEAL's protocol），而不是\"最优 output-preserving masks\"——所以 BCE 的低 PPL 可能部分来自 target 质量差而非 gradient 不耦合。\n\n6. **OOD 评估覆盖**：C4 evaluation 仅覆盖 30%/50%（Appendix D），无 70%。30% 为 2-seed，50% 为 single seed。考虑到 C4 退化更严重（1.74× vs 1.47×），更多的 OOD 评估会增强说服力。\n\n---\n\n## 格式合规\n\n- [✓] `\\usepackage[review]{acl}` — 双盲 review 模式\n- [✓] Anonymous 作者\n- [⚠️] `\\enlargethispage{10\\baselineskip}` — 格式操纵（W1）\n- [✓] Limitations section 存在且实质性\n- [✓] Ethics Statement 存在\n- [✓] Responsible NLP Research Checklist 逐项填写\n- [✓] 页数：正文 8 页（但第 8 页被人为扩展）\n- [✓] 行号开启\n",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 — Round 1 审稿意见\n\n**论文**: \"Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\"\n**Venue**: EMNLP 2026 (ACL Rolling Review May 2026 cycle)\n\n---\n\n## 总体评分\n**Overall**: 3.0 / 5 — Findings\n**一句话总结**: 观察到 KL 蒸馏优于 BCE 用于稀疏性预测是有价值的实证贡献，但核心因果 claim 存在未解的混淆变量（oracle target quality vs. gradient coupling），14B 结果与主叙事矛盾，且无实际推理加速演示。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3 / 5 | 梯度分析结构正确，但 BCE vs KL 对比存在已知混淆变量（论文自身承认），regime 分析每个 regime 仅 1 个数据点 |\n| Excitement | 3 / 5 | KL > BCE 的观察有用且可能启发后续工作，但无实际加速且 14B 结果限制了 claim 的普适性 |\n| Reproducibility | 4 / 5 | 超参数报告完整，硬件明确，关键结果有 multi-seed；但 SNR 计算细节缺失 |\n| Confidence | 4 / 5 | 熟悉稀疏性预测和蒸馏文献，仔细阅读了全文 |\n\n---\n\n## Summary\n\n本文研究用 forward KL 蒸馏替代 per-neuron BCE 训练 SwiGLU LLM 的稀疏性预测器。核心观察是：BCE 的梯度对每个 neuron 独立，而 KL 的梯度通过下游层的 Jacobian 耦合所有 neuron，更适合 TEAL 的 global top-k 推理分配。在 LLaMA-3.1-8B 上，KL 预测器（75.9M 参数）在 30% 和 50% 稀疏度下均优于 TEAL，并使补偿网络（+67.2M 参数）成为冗余。跨架构验证覆盖 Mistral-7B 和 Qwen-2.5-14B。论文还分析了三个\"operating regions\"并报告了 allocation-dependent 行为。\n\n---\n\n## 主要优势\n\n1. **梯度分析清晰且有启发性**（§3.6）：BCE gradient $\\partial \\mathcal{L}/\\partial s_j = \\sigma(s_j) - m_j^*$ 仅依赖 neuron $j$，而 KL gradient 通过 Jacobian factor (b) 耦合所有 neuron。这是一个简洁有力的 structural observation，即使论文未能完全证明它是性能差异的唯一来源。\n\n2. **诚实报告负面结果**：14B MMLU gap（63.7% vs 71.8%，Table 7）、无 wall-clock speedup、30% 下 global allocation 的 seed 不稳定性（MMLU σ=9.5pp）——这些对论文叙事不利的结果都被如实报告并讨论，这是值得称赞的。\n\n3. **消融设计较完整**（Table 3）：覆盖 divergence direction（forward/reverse/JSD）、relaxation method（Gumbel vs STE）、loss function isolation（BCE+Gumbel+Penalty）、compensation redundancy。每个消融隔离了一个设计选择。\n\n4. **跨架构验证**（Table 6）：LLaMA-8B、Mistral-7B、Qwen-14B 三个架构的 PPL 优势一致（30%: 1.22-1.24×, 50%: 1.98-2.12×），增强了方法的普适性 claim。\n\n5. **Taxonomy（Table 1）**将 prior work 按 correction granularity × training signal coupling 组织，定位清晰。\n\n6. **写作质量高**：结构紧凑，数学符号一致，表格信息密度高。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 核心因果 claim 存在未隔离的混淆变量\n- 具体位置：§4.3（第 7 页）、Limitations（第 9 页）\n- 问题：论文的核心叙事是\"梯度耦合（gradient coupling）使 KL 优于 BCE\"。但 BCE 使用 magnitude-based oracle masks 作为 target，而 KL 直接优化输出分布——这是两个同时变化的变量（training objective 和 implicit target quality）。论文自身在 §4.3 明确承认：\"an ablation using KL-derived masks as BCE targets would isolate the effect\"，但未执行该消融。\n- 现有证据的局限：Oracle F1 分析（BCE 0.613 vs KL 0.540，但 KL PPL 好 139%）说明 per-neuron accuracy 不等于 output preservation，但无法区分这是因为（a）KL 的梯度耦合更好，还是（b）magnitude-based oracle masks 本身就是次优 target。如果 BCE 使用 KL-derived masks（即\"正确的\" target），表现是否仍差？这是一个可执行的消融。\n- 为什么影响接收：这是 contribution 1 和 2 的根基。如果改善主要来自 target quality 而非 gradient coupling，论文的主要叙事（structural mismatch → coupled gradient → better allocation）就需要重新 frame。\n- 建议修改方向：执行 KL-derived masks as BCE targets 消融（论文自己提出了这个实验）。即使 KL 仍胜出，结果也会更 conclusive；即使 BCE 缩小差距，也是有价值的发现，可以修改 framing 为\"both target quality and coupling matter\"。\n\n**N2** [critical] \"Three Operating Regions\" 分析证据不足\n- 具体位置：§4.5（Table 5），第 8 页\n- 问题：论文声称存在三个 qualitatively distinct 的 operating regions（budget-surplus ≤30%、budget-constrained ~40%、capacity-limited ≥50%），但每个 regime 只有 **一个数据点**（30%、40%、50%），且 40% 仅单 seed。论文承认\"Denser sampling (e.g., 35% sparsity) would be needed to precisely locate region boundaries\"，但仍然在正文中强调\"三个 regions\"作为核心发现之一。\n- 具体缺陷：\n  - 40% regime：global MMLU 38.06% vs uniform 30.68%（+7.4pp），但这是**单 seed**结果。考虑到 30% global MMLU 的 σ=9.5pp，40% 的 7.4pp 差异可能在 seed variance 之内。\n  - 边界不确定：30% 和 40% 之间的行为（35%? 37%?）完全未知，40% 和 50% 之间同理。\n  - 30% 的 regime 标签\"budget-surplus\"暗示 30% 是\"容易的\"，但 30% 的 PPL 已比 dense 恶化 47%（8.96/6.12），downstream 显著退化。\n- 为什么影响接收：这是 contribution 3 的主体。以 3 个点声称\"三个 qualitative phases\"在统计上不严格。\n- 建议修改方向：（1）在 25%、35%、45% 补充至少 2-seed 实验以确认 regime boundaries；或（2）将 framing 弱化为\"preliminary observations suggesting allocation-dependent behavior\"而非 distinct operating regions。\n\n**N3** [critical] 14B 结果与核心 claim 显著矛盾，解释不充分\n- 具体位置：§4.6（Table 7），第 8 页\n- 问题：在 Qwen-2.5-14B 30% 稀疏度下，KL PPL 最优（7.62 vs TEAL 8.73），但 MMLU 低 8.1pp（63.72% vs 71.83%），GSM8K 低 4.3pp（48.82% vs 53.07%），ARC-c 也略低。在 uniform allocation 下，MMLU 差距仍存在（64.49 vs 66.34）。论文的核心 claim 是\"output-distribution preservation is better than per-neuron classification\"，但 14B 的 downstream 结果表明，PPL 优化不等于 task 保持，且在更大模型上 BCE/TEAL 的 downstream 表现反而更好。\n- 论文的解释（\"Higher knowledge density at 14B may cause KL's output-preservation objective to sacrifice task-specific pathways\"）是推测性的，没有实证支撑。\n- 为什么影响接收：如果方法在 scale up 到 14B 时核心优势反转（PPL 好但 downstream 差），那么\"output-distribution distillation is better\"的 claim 的 generalization scope 需要严格限定。\n- 建议修改方向：（1）在 14B 上测试更多稀疏度（40%, 50%）以确认是否 consistent；（2）分析 14B per-layer retention patterns 与 8B 的差异；（3）修改 claim scope 为明确限定在 7-8B。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] `\\enlargethispage{10\\baselineskip}` 格式操纵\n- 具体位置：experiments.tex 第 253 行\n- 问题：使用 `\\enlargethispage{10\\baselineskip}` 人为扩展第 8 页以容纳更多内容。从 PDF 第 8 页可看到，该页内容密度明显高于其他页（包含 Table 5、Table 6、Table 7、三个 operating regions 分析、SPON 分析、cross-architecture validation、14B 结果、inference efficiency、完整 conclusion）。\n- 为什么重要：ACL 模板明确规定不得修改 margin 和 page layout。虽然技术上不算 desk reject，但审稿人和 AC 经常注意到这类操纵。\n- 建议：将部分实验内容（如 SPON 详细分析）移至 appendix。\n\n**W2** [warning] BCE baseline 比较不完全公平\n- 具体位置：§4.2-4.3（Table 2, Table 3）\n- 问题：\n  - BCE 在 30% 稀疏度下的结果**未在 Table 2 中报告**。既然 30% 是 recommended operating point，这是一个关键缺失。仅在 50% 展示 BCE（PPL 28.13）放大了 KL 的优势。\n  - BCE 和 KL 的 target 不同（magnitude oracle vs output distribution），这不仅是 loss function 的差异，还是 supervision signal 的差异（与 N1 相关但这里聚焦 fairness）。\n  - Isolation ablation（BCE+Gumbel+Penalty = 38.02）比 vanilla BCE（27.97）更差，说明 Gumbel+Penalty 框架与 BCE 不兼容，而非 BCE 在该框架下效果不好。\n- 建议：（1）补充 BCE 30% 结果；（2）测试 BCE with output-based targets 或 BCE without TEAL allocation（用 BCE 自身的 per-layer top-k）。\n\n**W3** [warning] 训练/评估数据同族问题\n- 具体位置：§4.1、Appendix D\n- 问题：训练用 WikiText-103，主要评估用 WikiText-2（同一 WikiText 语料族）。C4 OOD 结果（Appendix D）在 30% 时 PPL 退化为 1.74× dense（vs WikiText-2 的 1.47×），退化更严重。C4 30% 仅 2-seed（vs 主结果 3-seed），且无 C4 downstream 评估。\n- 建议：（1）C4 补充到 3-seed 以匹配主结果的 rigor；（2）报告 C4 上的 downstream benchmarks 或解释为什么 WikiText-2 的 downstream 结果可以 generalize。\n\n**W4** [warning] SNR 分析覆盖不足\n- 具体位置：§3.6（第 5 页），Appendix F\n- 问题：\n  - SNR 仅测量到 step 300，但训练跑 1000 步。Step 300-1000 的 SNR 演化未知。\n  - \"5.14× higher SNR at convergence (step 300)\" ——但 step 300 不是真正的 convergence（Appendix B.2 显示 training converges by step 800）。\n  - SNR 计算的 mini-batch 数量未报告，bootstrap CI 的样本量未报告。\n  - 因果 claim（\"KL's gradient coupling becoming effective only after the predictor learns a coarse mask structure\"）是 post-hoc 解释，未经验证。\n- 建议：（1）将 SNR 测量延伸到 1000 步；（2）报告 mini-batch 数量和 bootstrap 参数；（3）弱化因果 claim 为 correlation observation。\n\n**W5** [warning] Adaptive penalty controller 在 30% 处不收敛\n- 具体位置：Appendix C（Table 12），第 12 页\n- 问题：在 recommended 30% operating point，$\\lambda$ 达到 cap（5000），actual sparsity 28.5%（deviation 5.0%）。论文辩称 TEAL 在 28.5% 的 PPL ≈ 10.7 vs 30% 的 10.97，差异可忽略。但这意味着 KL predictor 实际运行在比标称更低的稀疏度上，给 KL 带来了不公平的 ~1.5% sparsity 优势。Table 2 报告\"30% sparsity\"但实际是 28.5%。\n- 建议：（1）在 Table 2 的 caption 或正文中明确注明 actual sparsity；（2）与 TEAL at 28.5% 做 fair comparison。\n\n**W6** [warning] 无实际推理加速\n- 具体位置：Appendix A（Table 8），第 11-12 页\n- 问题：Pipeline 增加 6.4% overhead（126.78 vs 119.11 ms/fwd）。在 30% recommended sparsity 下，预测器增加 6.3% latency 但未从稀疏性获得任何 speedup（unstructured masks 无法被硬件加速）。论文的 motivation 是推理效率，但实际贡献是 prediction quality 而非 efficiency。\n- 建议：论文诚实地在 Limitations 中讨论了这一点，但建议在 Introduction 中更早 set expectations，避免读者产生效率提升的预期。\n\n---\n\n## 小问题（不影响接收）\n\n1. Figure 1（method overview）出现在第 6 页（实验部分之后才开始的位置），位置偏晚。建议移到 Method section 正文中更早的位置。\n2. \"renders post-hoc compensation redundant\" claim 仅测试了一种 compensation 架构（FastForward-style）。措辞可改为\"renders FastForward-style compensation redundant\"。\n3. Abstract 中 \"7-14B\" 范围暗示 PPL 优势跨 scale 一致，但 14B downstream 结果与此暗示矛盾。\n4. Table 2 caption 注脚说明\"50% uniform PPL is 3-seed (11.92 ± 0.07; Appendix E)\"，但正文 Table 2 中 50% KL uniform 显示为 11.96，不一致。\n5. Downstream benchmark 选择标准未解释——为什么 ARC-c, WG, MMLU, GSM8K 在主表而 HellaSwag, PIQA, BoolQ 在 appendix？\n6. Appendix 引用完整性：正文提到 Appendix H (app:downstream) 但编号可能需要检查（appendix 使用字母编号 A-F）。\n\n---\n\n## Missing References\n\n引用验证结果：39 条 bib entries 全部被引用，无 orphan/missing。OpenAlex 验证 35 条通过，4 条 minor mismatch（author name formatting）。\n\n建议补充考虑的参考文献：\n- **Griffin (De Vries et al., 2024)** 或其他 gated linear unit variant 的稀疏性工作\n- **Mixture-of-Experts 稀疏性与 activation sparsity 的交叉文献**（如 Expert Choice routing）——Table 1 taxonomy 可能遗漏了 MoE-based 方法作为\"coupled + per-token\"的另一个 cell\n\n---\n\n## Detailed Comments\n\n### 技术正确性\n\n1. **梯度分析（§3.6）数学正确**：BCE gradient 分解（Eq. 9-10）和 KL gradient chain rule（Eq. 11）的结构分析是正确的。Factor (b) $\\partial \\mathbf{z}/\\partial \\mathbf{h}^{(\\ell)}$ 确实通过下游层耦合所有 neuron。\n\n2. **Gumbel-Sigmoid relaxation（§3.3）使用合理**：温度退火 1.0→0.1 是标准做法（Jang et al. 2017; Maddison et al. 2017）。STE 对比（PPL 15.77 vs 11.79）有效展示了 smooth relaxation 的价值。但温度 schedule sensitivity（Appendix B.1）显示 fixed τ=0.5 实际上略好于 default schedule（PPL 11.861 vs 11.963），这与正文描述的 annealing 动机（\"从 exploration 到 exploitation\"）矛盾。\n\n3. **Adaptive penalty controller（§3.5）收敛保证**：论文明确在 footnote 中说明这不是 formal dual method，不保证 KKT satisfaction。这是诚实的。但 30% 处 5% deviation（28.5% actual）不可忽略——在 PPL scale 上 1.5% sparsity 差异约 0.3 PPL，而 KL vs TEAL 差异为 2.0 PPL，所以影响有限但应注明。\n\n### 实验设计\n\n4. **Iso-compute 对比（§4.3）基本公平**：BCE 2700 步 ≈ 46min vs KL 1000 步 ≈ 45min。Wall-clock 时间匹配合理（KL 需要 dense forward pass + sparse forward pass per step，计算量更大）。但 BCE 2700 步是否收敛？论文说 PPL 28.13±0.20，没有报告 training loss curve 是否已 plateau。如果 BCE training loss 仍在下降，更多步数可能进一步缩小差距。\n\n5. **Oracle F1 分析（§4.3）论证基本 sound**：F1 高但 PPL 差确实说明 per-neuron accuracy 是 misaligned proxy。但 confound 是：BCE 的 oracle masks 来自 magnitude ranking（TEAL's protocol），而不是\"最优 output-preserving masks\"——所以 BCE 的低 PPL 可能部分来自 target 质量差而非 gradient 不耦合。\n\n6. **OOD 评估覆盖**：C4 evaluation 仅覆盖 30%/50%（Appendix D），无 70%。30% 为 2-seed，50% 为 single seed。考虑到 C4 退化更严重（1.74× vs 1.47×），更多的 OOD 评估会增强说服力。\n\n---\n\n## 格式合规\n\n- [✓] `\\usepackage[review]{acl}` — 双盲 review 模式\n- [✓] Anonymous 作者\n- [⚠️] `\\enlargethispage{10\\baselineskip}` — 格式操纵（W1）\n- [✓] Limitations section 存在且实质性\n- [✓] Ethics Statement 存在\n- [✓] Responsible NLP Research Checklist 逐项填写\n- [✓] 页数：正文 8 页（但第 8 页被人为扩展）\n- [✓] 行号开启\n",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 449 · 2026-05-18T14:17:45.150625+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3814
}
```

</details>

---


### Assistant

_source line 450 · 2026-05-18T14:17:56.104773+00:00_

审稿意见已提交给 Review Director。

**审稿完成摘要**：

- **Overall: 3.0 (Findings)**
- **3 个 Critical 问题**：(N1) KL vs BCE 的核心因果 claim 存在未隔离的混淆变量——论文自身承认需要"KL-derived masks as BCE targets"消融但未执行；(N2) "三个 operating regions" 每个 regime 仅 1 个数据点，40% 为单 seed；(N3) 14B 的 MMLU 比 TEAL 低 8pp，与核心叙事矛盾
- **6 个 Warning 问题**：格式操纵 (`\enlargethispage`)、BCE 30% 未报告、训练/评估数据同族、SNR 分析覆盖不足、penalty controller 在 30% 不收敛（实际 28.5%）、无实际加速
- **主要优势**：梯度分析清晰、消融完整、负面结果诚实报告、跨架构验证、写作质量高

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1"
}
```

</details>

---


## Round 15

## Round 15

18 recorded events


### User

_source line 451 · 2026-05-18T14:20:21.392977+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并引用具体 Section/Table/Figure 作为证据。

---

### Reviewer 2 评分：3.0 (Findings)

**Must-Fix:**

**N1** [critical] 方法论新颖性不足以支撑 Main Conference
- Forward KL distillation、Gumbel-Sigmoid、adaptive penalty 均为成熟技术。MaskLLM 已将 frozen weights + learnable masks + KL + Gumbel relaxation 用于 LLM sparsity，技术栈高度重叠。§3.5 gradient 分析是 end-to-end > decomposed 这一公知原则的直接实例化。Table 1 taxonomy 是循环论证式新颖性声明。

**N2** [critical] 14B 结果与核心叙事矛盾
- Qwen-2.5-14B at 30%: KL PPL 7.62 vs TEAL 8.73（优势），但 MMLU 63.7 vs 71.8（落后 8pp）。核心叙事"output-distribution preservation beats per-neuron classification"与此矛盾。"Knowledge density"解释为未验证推测。

**N3** [critical] `\enlargethispage{10\baselineskip}` 页面操控
- 第 8 页增加约 10 行额外内容，底部 margin 被显著压缩。ACL 模板禁止修改 margins，可能 desk reject。

**Should-Fix:**

**W1** 50% downstream collapse 与叙事 framing 不一致（Abstract 突出 49% PPL advantage 但 MMLU ≈ random）
**W2** 训练-评估域重叠（WikiText-103 训练 / WikiText-2 评估，OOD 仅 PPL 无 downstream）
**W3** 39 篇引用偏少；遗漏若干相关工作
**W4** 无实际推理加速（+6.4% overhead）
**W5** Gradient coupling vs oracle quality 未 disentangle（论文自己提出的 ablation 未执行）

**小问题:**
- Appendix C Figure 3 可能有 placeholder
- bib key `xu2026spon` year 标 2026 实为 ICML 2025
- Abstract 数字密度偏高
- §4.5 的 `\label{sec:14b}` 位置可能导致引用问题

---

请对每个 N 和 W 逐条回应 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 452 · 2026-05-18T14:20:53.171819+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
  "offset": "195",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
    "offset": "195",
    "limit": "15"
  }
}
```

</details>

---


### Tool result

_source line 453 · 2026-05-18T14:20:53.624552+00:00_

195	\subsection{SPON Orthogonality Analysis}
196	\label{sec:spon}
197	
198	At 50\% sparsity, the predictor's hidden-state perturbation (L2=482.65) and SPON's additive correction (L2=76.2, cosine similarity 0.196) are weakly correlated ($R^2$=0.038); SPON yields only 2.4\% PPL improvement (12.08$\to$11.79); the KL predictor already captures most recoverable signal. % exp_id: spon_decomposition, spon_2048_s42, mvp_kl_norm_v2_s42
199	
200	\paragraph{Cross-Architecture Validation.}
201	\label{sec:cross_arch}
202	Table~\ref{tab:cross_arch} evaluates on Mistral-7B-v0.3~\cite{jiang2023mistral} (GQA + sliding window, dense PPL 5.52).
203	
204	\begin{table}[t]
205	\centering
206	\caption{Cross-architecture comparison (WikiText-2 PPL$\downarrow$). Adv = TEAL\,/\,KL ratio. LLaMA uses global top-$k$; Mistral uses uniform allocation (matched within each architecture).}
207	\label{tab:cross_arch}
208	\small
209	\begin{tabular}{l@{\hspace{4pt}}cc@{\hspace{3pt}}c@{\hspace{6pt}}|@{\hspace{6pt}}cc@{\hspace{3pt}}c}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 454 · 2026-05-18T14:20:53.976302+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex",
  "offset": "13",
  "limit": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex",
    "offset": "13",
    "limit": "6"
  }
}
```

</details>

---


### Tool result

_source line 455 · 2026-05-18T14:20:54.028192+00:00_

13	PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.
14	MaskLLM~\cite{fang2024maskllm} also employs learnable masks with Gumbel relaxation and frozen weights, but targets N:M semi-structured \emph{weight} sparsity (2:4 patterns) via per-group categorical selection (Gumbel-Softmax), producing fixed masks independent of input tokens.
15	Both share the principle of frozen weights + learnable masks + KL training, but solve distinct optimization problems: MaskLLM finds optimal static N:M patterns within fixed groups, while we predict dynamic per-token masks under a global budget constraint.
16	The structural mismatch we characterize (per-neuron gradient decomposition vs.\ global top-$k$) does not arise in MaskLLM's per-group categorical setting, where N:M patterns eliminate cross-group budget competition.
17	All prior predictor-based methods use decomposed (BCE) or intermediate (MSE) objectives where each neuron's gradient is independent of other mask states.
18	Our contribution is primarily empirical: we observe that a coupled KL objective propagates gradients through all downstream layers and quantify when this matters for global allocation quality.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 456 · 2026-05-18T14:20:58.901077+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 457 · 2026-05-18T14:20:59.253233+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 458 · 2026-05-18T14:20:59.304002+00:00_

1	We study whether end-to-end KL distillation can replace per-neuron classification for activation sparsity prediction in SwiGLU LLMs.
2	Existing predictors trained with binary cross-entropy (BCE) optimize each neuron independently, but inference allocates sparsity budgets via global top-$k$ across all layers.
3	Gradient analysis reveals a structural mismatch: BCE's per-neuron gradient is blind to cross-neuron interactions and achieves higher oracle F1 yet 139\% worse perplexity than a KL-trained predictor.
4	A lightweight predictor ($<$1\% of base parameters) trained with forward KL and Gumbel-Sigmoid relaxation resolves this mismatch by coupling all neurons through the output distribution, rendering post-hoc compensation (+67.2M params) redundant at both 30\% and 50\% sparsity.
5	On LLaMA-3.1-8B at the recommended 30\% sparsity, KL reduces PPL degradation 18\% over TEAL; uniform allocation provides $7.5\times$ smaller cross-seed downstream $\sigma$, eliminating seed-dependent instability.
6	At 50\% sparsity, the PPL advantage widens to 49\% but downstream tasks degrade regardless of allocation, revealing allocation-dependent operating regions at 7--8B scale.
7	Evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms the PPL advantage across 7--14B, though 14B reveals a scale-dependent MMLU gap not resolved by allocation strategy.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 459 · 2026-05-18T14:21:00.263453+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1362
}
```

</details>

---


### Tool call

_source line 460 · 2026-05-18T14:21:05.137802+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 461 · 2026-05-18T14:21:05.842272+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\label\\{sec:14b\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\label\\{sec:14b\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 462 · 2026-05-18T14:21:05.893073+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex:224:\label{sec:14b}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 463 · 2026-05-18T14:21:06.446538+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1308
}
```

</details>

---


### Tool call

_source line 464 · 2026-05-18T14:21:10.161302+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
  "offset": "220",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
    "offset": "220",
    "limit": "10"
  }
}
```

</details>

---


### Tool result

_source line 465 · 2026-05-18T14:21:10.262406+00:00_

220	
221	The KL advantage ratio is consistent across architectures (within 8\% at $\leq$50\% sparsity).
222	
223	\paragraph{Scale Generalization: Qwen-2.5-14B.}
224	\label{sec:14b}
225	Table~\ref{tab:14b} evaluates Qwen-2.5-14B~\cite{qwen2024qwen25} at 30\%: KL's PPL advantage generalizes ($1.47\times$ dense), but MMLU falls below TEAL/BCE (63.7 vs.\ 71.8\%), and uniform recovers only +0.8pp. The gap appears intrinsic to KL's output-preservation objective rather than allocation-induced.
226	Higher knowledge density at 14B may cause KL's output-preservation objective to sacrifice task-specific pathways that 8B retains at 30\%; whether this generalizes requires further study.
227	BCE collapses to 6.4\% native sparsity (\S\ref{sec:method:gradient}); Table~\ref{tab:14b} uses forced global top-$k$. % exp_id: qwen14b_kl30_s42, qwen14b_bce30_s42, qwen14b_bce30_s42_v2, qwen14b_teal30_eval, qwen14b_kl30_uniform, qwen14b_teal30_uniform
228	
229	\begin{table}[t]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 466 · 2026-05-18T14:23:06.138325+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 交叉回应 Reviewer 2 意见\n\n---\n\n### Must-Fix 逐条回应\n\n**[AGREE with nuance] R2-N1: 方法论新颖性不足**\n\n同意 novelty concern 对 Main Conference 是合理的，但 MaskLLM 重叠程度被高估。\n\n同意的部分：\n- Forward KL、Gumbel-Sigmoid、adaptive penalty 确实都是成熟技术，论文本身也承认 \"Our contribution is primarily empirical\"（Related Work, line 18）。\n- Table 1 taxonomy 的\"循环论证\"批评有道理：定义两个轴使自己恰好填充空白 cell，这是 positioning 技巧而非独立贡献。\n- §3.6 的梯度分析结构上是 \"end-to-end gradient couples neurons\" 这一公知原则的直接实例化，analytical novelty 有限。\n\n反驳的部分：\n- MaskLLM 解决的是 **static N:M weight sparsity**（per-group Gumbel-Softmax，固定 mask 不随 input 变化），本文是 **dynamic per-token activation sparsity under global budget constraint**。论文在 Related Work 第 14-16 行明确区分：\"MaskLLM finds optimal static N:M patterns within fixed groups, while we predict dynamic per-token masks under a global budget constraint. The structural mismatch we characterize (per-neuron gradient decomposition vs. global top-k) does not arise in MaskLLM's per-group categorical setting.\" 这不是同一个优化问题，技术栈的重叠是表面层面的（都用 KL + Gumbel + frozen weights），而 problem formulation 是不同的。\n- 真正的 novelty 不在于单个组件，而在于将 KL distillation 应用于 contextual sparsity prediction 这个 **specific combination**，并用实证量化了什么时候 coupling matters。这是 empirical contribution 而非 methodological contribution，论文定位基本准确。\n\n**综合判断**：R2 的 novelty concern 对 Main 合理，但 MaskLLM 的类比不足以构成 \"已有工作\"——两者解决不同问题。论文作为 empirical contribution 适合 Findings。\n\n---\n\n**[AGREE] R2-N2: 14B 结果与核心叙事矛盾**\n\n完全同意，与我的 R1-N3 一致。\n\n补充证据：\n- Table 7：KL PPL 7.62（最优）但 MMLU 63.72（vs TEAL 71.83，落后 8.1pp），GSM8K 48.82（vs BCE 53.07，落后 4.3pp）。\n- Uniform allocation 仅恢复 +0.8pp MMLU（64.49 vs 63.72），说明差距不是 allocation-induced。\n- §4.6 的解释 \"Higher knowledge density at 14B may cause KL's output-preservation objective to sacrifice task-specific pathways\" 是推测性的、无实证支撑的 post-hoc rationalization。\n- 这直接削弱了 Abstract 第 7 行的 claim \"confirms the PPL advantage across 7-14B\"——PPL advantage 确实 confirmed，但 downstream 方向相反，而 downstream 才是最终衡量标准。\n\n建议作者在 Abstract 和 Introduction 中将 scope 明确限定为 7-8B，14B 作为 scale-dependent limitation 而非 confirmation。\n\n---\n\n**[AGREE with downgrade] R2-N3: `\\enlargethispage{10\\baselineskip}` 页面操控**\n\n同意这是问题（与我的 R1-W1 一致），但对严重性判断略有不同。\n\n同意：\n- `\\enlargethispage{10\\baselineskip}`（experiments.tex line 253）确实人为扩展了第 8 页。从 PDF 第 8 页可观察到该页内容密度远超其他页面（包含 Tables 5-7、三个 regime 分析、SPON、cross-architecture、14B、inference efficiency、完整 Conclusion）。\n- ACL 模板确实要求不修改 margins/layout。\n\n轻微反驳 \"desk reject\" 判断：\n- `\\enlargethispage` 是 LaTeX 的标准命令，不同于直接修改 `\\geometry` 或 sty 文件中的 margin 值。许多已发表论文使用过此命令。ARR desk reject 通常针对 **margin/font-size 修改** 而非 per-page stretching。\n- 风险确实存在，但更可能的结果是 AC 要求修改而非直接 desk reject。\n\n**建议分级**：Should-Fix (high priority) 而非 Critical。作者应立即移除该命令，将 SPON 详细分析或部分 Table 移至 appendix。\n\n---\n\n### Should-Fix 逐条回应\n\n**[AGREE] R2-W1: 50% downstream collapse 与叙事 framing 不一致**\n\n同意。Abstract 第 6 行突出 \"the PPL advantage widens to 49%\"，但 Table 2 显示 50% MMLU ≈ 28%（≈random for 4-choice）、GSM8K < 2.2%。Abstract 后半句 \"but downstream tasks degrade regardless of allocation\" 做了 hedge，但读者首先记住的是 \"49% advantage\"。\n\n论文在 §4.5 正确将此分析为 \"capacity-limited regime\"（MMLU 28.1±0.2% vs 28.0±0.6%，差异不显著），但 Abstract 的 emphasis 与此不匹配。建议 Abstract 更明确传达：50% sparsity 下 PPL 改善虽大但 downstream 已 collapse，实际推荐 30%。\n\n---\n\n**[AGREE] R2-W2: 训练-评估域重叠**\n\n同意，与我的 R1-W3 一致。补充：C4 OOD 评估（Appendix D）在 30% 处 PPL 退化为 1.74× dense（vs WikiText-2 的 1.47×），退化显著更大。C4 30% 仅 2-seed（vs 主结果 3-seed），且完全没有 C4 downstream benchmarks。如果 predictor 对 WikiText 族有分布偏好，PPL 优势可能部分来自 distribution overlap 而非 method superiority。\n\n---\n\n**[REBUT] R2-W3: 39 篇引用偏少**\n\n不同意引用数量不足。\n\n- 39 篇引用对于一篇聚焦于 **specific technique (KL for sparsity prediction)** 的 empirical paper 是合理的。论文不是 survey 性质的综述。\n- 引用覆盖了所有关键类别：activation sparsity methods（TEAL, CATS, R-Sparse, DIP, SparseInfer, DejaVu, ShadowLLM, FastForward, SVD-CSP, PowerInfer, MaskLLM）、activation function engineering（ReLU Strikes Back, TurboSparse, ProSparse, Sparsing Law, MiniTron）、weight pruning（Wanda, SparseGPT）、KL distillation（Kim & Rush 2016, DistilBERT, MiniLLM, GKD）、conditional computation（Switch Transformers, MoD, D2DMoE）、relaxation methods（Gumbel-Softmax, Concrete, L0）、SPON。\n- 我在 R1 审稿中建议补充 Expert Choice routing 等 MoE 稀疏性文献，但这是 \"nice to have\" 而非 coverage gap。\n- EMNLP 录用论文引用量中位数约 40-50，39 在正常范围内。\n\n---\n\n**[AGREE] R2-W4: 无实际推理加速**\n\n同意，与我的 R1-W6 一致。Appendix A Table 8 显示 +6.4% overhead without any demonstrated speedup from sparsity（unstructured masks 无硬件加速支持）。论文在 Limitations 中诚实讨论了这一点，但 Introduction 的 motivation framing 可以更清楚地 set expectations。\n\n---\n\n**[AGREE] R2-W5: Gradient coupling vs oracle quality 未 disentangle**\n\n完全同意，这与我的 R1-N1 是同一问题（我将其列为 Critical）。\n\n补充分析：\n- 论文 §4.3 明确写道 \"an ablation using KL-derived masks as BCE targets would isolate the effect\"——这证明作者意识到了这个 confound。\n- BCE isolation ablation（Table 3, BCE+Gumbel+Penalty = PPL 38.02）并不能隔离 loss function 的贡献，因为 penalty controller 是为 KL 设计的，与 BCE 不兼容（结果比 vanilla BCE 更差：38.02 vs 27.97）。\n- 缺失的消融是：**用 KL-trained predictor 产生的 masks 作为 BCE 的 oracle targets**，保持其他一切不变。如果 BCE 在\"正确 targets\"下仍差，则 coupling 是关键因素；如果 BCE 显著缩小差距，则 target quality 是主因。这是一个可在数小时内完成的实验。\n\n我认为这应该是 Must-Fix 而非 Should-Fix——它是核心 claim 的关键 confound。R2 将其放在 W5 可能低估了它的影响。\n\n---\n\n### 小问题回应\n\n**[AGREE] Appendix C Figure 3 placeholder**\n确认。PDF 第 13 页 Figure 3 显示 \"[Placeholder: lagrangian_dynamics.pdf]\" 而非实际图表。appendix.tex line 139 引用 `lagrangian_dynamics.pdf`，但该文件似乎缺失或为占位符。这是提交前必须修复的问题。\n\n**[REBUT with nuance] bib key `xu2026spon` year**\nBib key 名称 `xu2026spon` 中的 \"2026\" 仅是 key identifier，不影响渲染。references.bib 中该条目的 `year = {2025}` 和 `booktitle = {ICML}` 是正确的。渲染输出显示 \"(Xu et al., 2025)\"。这是 bib key 命名不规范但不影响论文输出的 cosmetic issue。\n\n**[AGREE] Abstract 数字密度偏高**\nAbstract 包含：139%、<1%、67.2M、30%、50%、18%、7.5×、49%、7-14B、MMLU gap 等大量数字。每个句子都有 1-2 个数字，读起来像 results summary 而非 story。建议减少到关键的 3-4 个数字。\n\n**[AGREE] `\\label{sec:14b}` 位置问题**\n确认。`\\label{sec:14b}` 位于 `\\paragraph{Scale Generalization: Qwen-2.5-14B.}` 之后（experiments.tex line 224），但 `\\paragraph` 在 ACL style 中没有独立 counter。`\\ref{sec:14b}` 会解析为父级 section 编号（§4.6 = SPON Orthogonality Analysis），导致 Limitations 中 `\\S\\ref{sec:14b}` 指向错误 section。应改用 `\\S4.6` 硬编码或将 14B 提升为独立 `\\subsection`。\n\n---\n\n### 总体评估与 R2 的一致性\n\nR2 和我的 Overall 评分一致：**3.0 (Findings)**。\n\n两位 reviewer 共识的核心问题：\n1. KL vs BCE 的因果 claim 存在未隔离的 confound（R1-N1 = R2-W5）\n2. 14B 结果与核心叙事矛盾（R1-N3 = R2-N2）\n3. 无实际推理加速（R1-W6 = R2-W4）\n4. 训练/评估域重叠（R1-W3 = R2-W2）\n\nR1 额外强调的问题：\n- Three Operating Regions 分析证据不足（R1-N2）——R2 未提及，但我认为这是独立的 critical issue\n- Adaptive penalty 在 30% 处不收敛导致 unfair comparison（R1-W5）\n\nR2 额外强调的问题：\n- Novelty 不足（R2-N1）——我部分同意，但认为 MaskLLM 类比被高估\n- 格式操纵严重性（R2-N3 = R1-W1）——R2 评为 critical，我评为 high-priority warning\n\n论文作为 empirical contribution 有价值（KL > BCE for sparsity prediction 的观察可能启发后续工作），但核心 claim 的因果归因需要更严格的 ablation 支撑，且 generalization scope 需要从 \"7-14B\" 收紧到 \"7-8B\"。Findings 级别合适。\n",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 交叉回应 Reviewer 2 意见\n\n---\n\n### Must-Fix 逐条回应\n\n**[AGREE with nuance] R2-N1: 方法论新颖性不足**\n\n同意 novelty concern 对 Main Conference 是合理的，但 MaskLLM 重叠程度被高估。\n\n同意的部分：\n- Forward KL、Gumbel-Sigmoid、adaptive penalty 确实都是成熟技术，论文本身也承认 \"Our contribution is primarily empirical\"（Related Work, line 18）。\n- Table 1 taxonomy 的\"循环论证\"批评有道理：定义两个轴使自己恰好填充空白 cell，这是 positioning 技巧而非独立贡献。\n- §3.6 的梯度分析结构上是 \"end-to-end gradient couples neurons\" 这一公知原则的直接实例化，analytical novelty 有限。\n\n反驳的部分：\n- MaskLLM 解决的是 **static N:M weight sparsity**（per-group Gumbel-Softmax，固定 mask 不随 input 变化），本文是 **dynamic per-token activation sparsity under global budget constraint**。论文在 Related Work 第 14-16 行明确区分：\"MaskLLM finds optimal static N:M patterns within fixed groups, while we predict dynamic per-token masks under a global budget constraint. The structural mismatch we characterize (per-neuron gradient decomposition vs. global top-k) does not arise in MaskLLM's per-group categorical setting.\" 这不是同一个优化问题，技术栈的重叠是表面层面的（都用 KL + Gumbel + frozen weights），而 problem formulation 是不同的。\n- 真正的 novelty 不在于单个组件，而在于将 KL distillation 应用于 contextual sparsity prediction 这个 **specific combination**，并用实证量化了什么时候 coupling matters。这是 empirical contribution 而非 methodological contribution，论文定位基本准确。\n\n**综合判断**：R2 的 novelty concern 对 Main 合理，但 MaskLLM 的类比不足以构成 \"已有工作\"——两者解决不同问题。论文作为 empirical contribution 适合 Findings。\n\n---\n\n**[AGREE] R2-N2: 14B 结果与核心叙事矛盾**\n\n完全同意，与我的 R1-N3 一致。\n\n补充证据：\n- Table 7：KL PPL 7.62（最优）但 MMLU 63.72（vs TEAL 71.83，落后 8.1pp），GSM8K 48.82（vs BCE 53.07，落后 4.3pp）。\n- Uniform allocation 仅恢复 +0.8pp MMLU（64.49 vs 63.72），说明差距不是 allocation-induced。\n- §4.6 的解释 \"Higher knowledge density at 14B may cause KL's output-preservation objective to sacrifice task-specific pathways\" 是推测性的、无实证支撑的 post-hoc rationalization。\n- 这直接削弱了 Abstract 第 7 行的 claim \"confirms the PPL advantage across 7-14B\"——PPL advantage 确实 confirmed，但 downstream 方向相反，而 downstream 才是最终衡量标准。\n\n建议作者在 Abstract 和 Introduction 中将 scope 明确限定为 7-8B，14B 作为 scale-dependent limitation 而非 confirmation。\n\n---\n\n**[AGREE with downgrade] R2-N3: `\\enlargethispage{10\\baselineskip}` 页面操控**\n\n同意这是问题（与我的 R1-W1 一致），但对严重性判断略有不同。\n\n同意：\n- `\\enlargethispage{10\\baselineskip}`（experiments.tex line 253）确实人为扩展了第 8 页。从 PDF 第 8 页可观察到该页内容密度远超其他页面（包含 Tables 5-7、三个 regime 分析、SPON、cross-architecture、14B、inference efficiency、完整 Conclusion）。\n- ACL 模板确实要求不修改 margins/layout。\n\n轻微反驳 \"desk reject\" 判断：\n- `\\enlargethispage` 是 LaTeX 的标准命令，不同于直接修改 `\\geometry` 或 sty 文件中的 margin 值。许多已发表论文使用过此命令。ARR desk reject 通常针对 **margin/font-size 修改** 而非 per-page stretching。\n- 风险确实存在，但更可能的结果是 AC 要求修改而非直接 desk reject。\n\n**建议分级**：Should-Fix (high priority) 而非 Critical。作者应立即移除该命令，将 SPON 详细分析或部分 Table 移至 appendix。\n\n---\n\n### Should-Fix 逐条回应\n\n**[AGREE] R2-W1: 50% downstream collapse 与叙事 framing 不一致**\n\n同意。Abstract 第 6 行突出 \"the PPL advantage widens to 49%\"，但 Table 2 显示 50% MMLU ≈ 28%（≈random for 4-choice）、GSM8K < 2.2%。Abstract 后半句 \"but downstream tasks degrade regardless of allocation\" 做了 hedge，但读者首先记住的是 \"49% advantage\"。\n\n论文在 §4.5 正确将此分析为 \"capacity-limited regime\"（MMLU 28.1±0.2% vs 28.0±0.6%，差异不显著），但 Abstract 的 emphasis 与此不匹配。建议 Abstract 更明确传达：50% sparsity 下 PPL 改善虽大但 downstream 已 collapse，实际推荐 30%。\n\n---\n\n**[AGREE] R2-W2: 训练-评估域重叠**\n\n同意，与我的 R1-W3 一致。补充：C4 OOD 评估（Appendix D）在 30% 处 PPL 退化为 1.74× dense（vs WikiText-2 的 1.47×），退化显著更大。C4 30% 仅 2-seed（vs 主结果 3-seed），且完全没有 C4 downstream benchmarks。如果 predictor 对 WikiText 族有分布偏好，PPL 优势可能部分来自 distribution overlap 而非 method superiority。\n\n---\n\n**[REBUT] R2-W3: 39 篇引用偏少**\n\n不同意引用数量不足。\n\n- 39 篇引用对于一篇聚焦于 **specific technique (KL for sparsity prediction)** 的 empirical paper 是合理的。论文不是 survey 性质的综述。\n- 引用覆盖了所有关键类别：activation sparsity methods（TEAL, CATS, R-Sparse, DIP, SparseInfer, DejaVu, ShadowLLM, FastForward, SVD-CSP, PowerInfer, MaskLLM）、activation function engineering（ReLU Strikes Back, TurboSparse, ProSparse, Sparsing Law, MiniTron）、weight pruning（Wanda, SparseGPT）、KL distillation（Kim & Rush 2016, DistilBERT, MiniLLM, GKD）、conditional computation（Switch Transformers, MoD, D2DMoE）、relaxation methods（Gumbel-Softmax, Concrete, L0）、SPON。\n- 我在 R1 审稿中建议补充 Expert Choice routing 等 MoE 稀疏性文献，但这是 \"nice to have\" 而非 coverage gap。\n- EMNLP 录用论文引用量中位数约 40-50，39 在正常范围内。\n\n---\n\n**[AGREE] R2-W4: 无实际推理加速**\n\n同意，与我的 R1-W6 一致。Appendix A Table 8 显示 +6.4% overhead without any demonstrated speedup from sparsity（unstructured masks 无硬件加速支持）。论文在 Limitations 中诚实讨论了这一点，但 Introduction 的 motivation framing 可以更清楚地 set expectations。\n\n---\n\n**[AGREE] R2-W5: Gradient coupling vs oracle quality 未 disentangle**\n\n完全同意，这与我的 R1-N1 是同一问题（我将其列为 Critical）。\n\n补充分析：\n- 论文 §4.3 明确写道 \"an ablation using KL-derived masks as BCE targets would isolate the effect\"——这证明作者意识到了这个 confound。\n- BCE isolation ablation（Table 3, BCE+Gumbel+Penalty = PPL 38.02）并不能隔离 loss function 的贡献，因为 penalty controller 是为 KL 设计的，与 BCE 不兼容（结果比 vanilla BCE 更差：38.02 vs 27.97）。\n- 缺失的消融是：**用 KL-trained predictor 产生的 masks 作为 BCE 的 oracle targets**，保持其他一切不变。如果 BCE 在\"正确 targets\"下仍差，则 coupling 是关键因素；如果 BCE 显著缩小差距，则 target quality 是主因。这是一个可在数小时内完成的实验。\n\n我认为这应该是 Must-Fix 而非 Should-Fix——它是核心 claim 的关键 confound。R2 将其放在 W5 可能低估了它的影响。\n\n---\n\n### 小问题回应\n\n**[AGREE] Appendix C Figure 3 placeholder**\n确认。PDF 第 13 页 Figure 3 显示 \"[Placeholder: lagrangian_dynamics.pdf]\" 而非实际图表。appendix.tex line 139 引用 `lagrangian_dynamics.pdf`，但该文件似乎缺失或为占位符。这是提交前必须修复的问题。\n\n**[REBUT with nuance] bib key `xu2026spon` year**\nBib key 名称 `xu2026spon` 中的 \"2026\" 仅是 key identifier，不影响渲染。references.bib 中该条目的 `year = {2025}` 和 `booktitle = {ICML}` 是正确的。渲染输出显示 \"(Xu et al., 2025)\"。这是 bib key 命名不规范但不影响论文输出的 cosmetic issue。\n\n**[AGREE] Abstract 数字密度偏高**\nAbstract 包含：139%、<1%、67.2M、30%、50%、18%、7.5×、49%、7-14B、MMLU gap 等大量数字。每个句子都有 1-2 个数字，读起来像 results summary 而非 story。建议减少到关键的 3-4 个数字。\n\n**[AGREE] `\\label{sec:14b}` 位置问题**\n确认。`\\label{sec:14b}` 位于 `\\paragraph{Scale Generalization: Qwen-2.5-14B.}` 之后（experiments.tex line 224），但 `\\paragraph` 在 ACL style 中没有独立 counter。`\\ref{sec:14b}` 会解析为父级 section 编号（§4.6 = SPON Orthogonality Analysis），导致 Limitations 中 `\\S\\ref{sec:14b}` 指向错误 section。应改用 `\\S4.6` 硬编码或将 14B 提升为独立 `\\subsection`。\n\n---\n\n### 总体评估与 R2 的一致性\n\nR2 和我的 Overall 评分一致：**3.0 (Findings)**。\n\n两位 reviewer 共识的核心问题：\n1. KL vs BCE 的因果 claim 存在未隔离的 confound（R1-N1 = R2-W5）\n2. 14B 结果与核心叙事矛盾（R1-N3 = R2-N2）\n3. 无实际推理加速（R1-W6 = R2-W4）\n4. 训练/评估域重叠（R1-W3 = R2-W2）\n\nR1 额外强调的问题：\n- Three Operating Regions 分析证据不足（R1-N2）——R2 未提及，但我认为这是独立的 critical issue\n- Adaptive penalty 在 30% 处不收敛导致 unfair comparison（R1-W5）\n\nR2 额外强调的问题：\n- Novelty 不足（R2-N1）——我部分同意，但认为 MaskLLM 类比被高估\n- 格式操纵严重性（R2-N3 = R1-W1）——R2 评为 critical，我评为 high-priority warning\n\n论文作为 empirical contribution 有价值（KL > BCE for sparsity prediction 的观察可能启发后续工作），但核心 claim 的因果归因需要更严格的 ablation 支撑，且 generalization scope 需要从 \"7-14B\" 收紧到 \"7-8B\"。Findings 级别合适。\n",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 467 · 2026-05-18T14:23:09.754076+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3615
}
```

</details>

---


### Assistant

_source line 468 · 2026-05-18T14:23:23.234765+00:00_

交叉回应已提交。

核心结论：R2 和我在 Overall 3.0 (Findings) 上一致。5 个问题达成共识（因果 confound、14B 矛盾、无加速、域重叠、格式操纵），分歧点在于 MaskLLM novelty 类比的严重性和格式操纵的分级。我在 R2-W5（gradient coupling vs oracle quality）上认为应升级为 Must-Fix，在 R2-N3（formatting）上认为应降级为 high-priority Should-Fix。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1"
}
```

</details>

---


## Round 16

## Round 16

66 recorded events


### User

_source line 469 · 2026-05-19T01:37:05.938720+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性 + 实验设计**审查。

## 投稿信息
- **论文**: "Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs"
- **Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
- **截止**: 2026-05-25
- **格式要求**: ACL 模板, Long paper (8 页正文, unlimited references/limitations/ethics), double-blind
- **论文路径**: `projects/distill_sparse_swiglu/paper/main.tex` (含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex)

## 你的审查侧重

### 1. 方法正确性
- KL divergence objective (Eq. 4-5) 的数学推导是否正确？Forward KL 的选择是否有充分理由？
- Gumbel-Sigmoid relaxation (Eq. 3) 的应用是否标准？与 Gumbel-Softmax/Concrete distribution 的关系是否正确？
- Adaptive penalty controller (Eq. 6-7) 是否有理论保证？与 augmented Lagrangian 的区别是否准确？
- §3.6 gradient analysis: BCE vs KL 的梯度结构对比是否正确？"downstream Jacobian" 的论述是否准确？

### 2. 实验设计严谨性
- **Causal ablation (C1, Table 3)**: BCE trained on KL-derived targets 的设计是否能真正 disentangle target quality vs gradient coupling？有无混淆变量？2-seed 统计效力是否足够？
- **Baseline 公平性**: BCE baseline 训练 2700 steps vs KL 1000 steps (iso-compute claim), 是否真正公平？"approximately equal wall-clock time" 是否可信？
- **Main results (Table 1)**: 30% 和 50% 的 BCE baseline 设置不同（30% 用 TEAL global, 50% 用 compensation 无 TEAL），是否 confounded？
- **Statistical power**: 哪些数字是 3-seed，哪些是单 seed？Table 1 的 annotation 是否清晰？
- **Cross-architecture (Mistral, Qwen-14B)**: 只报 PPL + 部分 downstream，实验是否充分？14B MMLU reversal 的讨论是否足够？

### 3. Ablation 完整性
- Table 4 ablation 是否覆盖所有关键 design choices？
- 缺失的 ablation: 不同训练数据？不同 predictor 架构？不同 allocation 策略与 loss 的交互？
- SPON 贡献只有 2.4%，是否应该从 method 中移除？

### 4. 数值一致性
- 检查 Table 1-4 数字是否内部一致（cross-reference between tables）
- Abstract/Intro 中引用的数字是否与 tables 匹配
- Appendix 数据与正文数据是否一致

### 5. 评分标准 (EMNLP 2026 ARR)
5 = Consider for Award, 4 = Conference, 3.5 = Borderline Conference, 3 = Findings, 2.5 = Borderline Findings, 2 = Resubmit next cycle, 1.5 = Resubmit after next cycle, 1 = Do not resubmit

请按 **Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Overall Assessment (含评分和置信度)** 格式输出。Weaknesses 部分需要详细、具体、引用论文中的具体 Section/Table/Figure，不要含糊。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 470 · 2026-05-19T01:37:19.072204+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Search ARR review form",
  "prompt": "Search the web for \"ACL ARR review form 2025 2026 reviewer guidelines criteria\" and \"EMNLP 2026 reviewer guidelines review form\". I need to find the official ACL Rolling Review (ARR) review form dimensions and scoring criteria. Look for:\n1. The official review form dimensions (soundness, excitement/novelty, clarity, etc.)\n2. The scoring scale for each dimension\n3. Any specific guidelines for reviewers\n\nUse WebSearch and WebFetch to find this information. Report the complete review form structure with all dimensions and their scales."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Search ARR review form",
    "prompt": "Search the web for \"ACL ARR review form 2025 2026 reviewer guidelines criteria\" and \"EMNLP 2026 reviewer guidelines review form\". I need to find the official ACL Rolling Review (ARR) review form dimensions and scoring criteria. Look for:\n1. The official review form dimensions (soundness, excitement/novelty, clarity, etc.)\n2. The scoring scale for each dimension\n3. Any specific guidelines for reviewers\n\nUse WebSearch and WebFetch to find this information. Report the complete review form structure with all dimensions and their scales."
  }
}
```

</details>

---


### Tool call

_source line 471 · 2026-05-19T01:37:20.881573+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
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

_source line 472 · 2026-05-19T01:37:20.882053+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 473 · 2026-05-19T01:37:20.982865+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form 2025 2026 reviewer guidelines criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form 2025 2026 reviewer guidelines criteria"
  }
}
```

</details>

---


### Tool call

_source line 474 · 2026-05-19T01:37:21.485669+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 reviewer guidelines review form"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 reviewer guidelines review form"
  }
}
```

</details>

---


### Tool call

_source line 475 · 2026-05-19T01:37:21.486071+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review official review form dimensions scoring scale"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review official review form dimensions scoring scale"
  }
}
```

</details>

---
