# Director coordination — Part 7 of 8

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Conversation logs

[← Part 6](part-006.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 8 →](part-008.md) · [Structured JSON](../../../sessions/e0/e0d2e26e51128e828a96.json)

## Round 176

### Tool call

_source line 2048 · 2026-05-23T01:26:50.001800+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline ARR commitment"
  }
}
```

</details>

---


### Tool call

_source line 2049 · 2026-05-23T01:26:50.503607+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review May 2026 deadline submission date aclrollingreview.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review May 2026 deadline submission date aclrollingreview.org"
  }
}
```

</details>

---


### Tool call

_source line 2050 · 2026-05-23T01:26:52.461035+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2051 · 2026-05-23T01:26:52.812961+00:00_

1	Learned sparsity predictors for SwiGLU LLMs predominantly use binary cross-entropy (BCE), training each neuron independently, yet inference allocates budgets globally via top-$k$ ranking.
2	We train lightweight predictors ($<$1\% of base parameters) with forward KL divergence, coupling all mask decisions through the output distribution.
3	On LLaMA-3.1-8B at 30\% sparsity, the KL predictor reduces perplexity by 14.5\% over TEAL at matched sparsity, with commonsense gains but knowledge-intensive decline; post-hoc compensation (+67.2M params) becomes redundant.
4	Output-distribution optimization yields masks that diverge 46--68\% from magnitude-based targets; a target-swap ablation suggests these discovered patterns carry most of the quality information: BCE trained on KL-derived targets approaches KL-level PPL (gap $\leq$0.65pp; 3-seed, 30\%).
5	Signal type (output-distribution vs.\ intermediate loss) accounts for the majority of the PPL gap at moderate sparsity (30\%) (upper bound; not fully orthogonal with coupling scope).
6	On downstream tasks, cross-layer coupling contributes substantially for commonsense reasoning but minimally for mathematical reasoning (3-seed $K{=}4$-corrected decomposition).
7	Cross-architecture evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms PPL generalization with scale-dependent downstream effects.
8	This is primarily an empirical study; wall-clock speedup requires sparse kernel support not addressed here.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 2052 · 2026-05-23T01:26:52.813368+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2053 · 2026-05-23T01:26:53.766447+00:00_

1	\section{Introduction}
2	
3	How the training objective shapes learned sparsity prediction quality is an open question for SwiGLU LLMs~\cite{shazeer2020glu}. SwiGLU FFN blocks exhibit high contextual sparsity, but their gated activation makes importance prediction challenging: neuron importance depends on both gate and up-projection values, a target that magnitude-based methods handle suboptimally.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they predominantly rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: the TEAL (training-free activation sparsity;~\citealp{liu2025teal}) top-$k$ mechanism ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	Unlike MaskLLM~\cite{fang2024maskllm}, which applies KL to static N:M weight masks, we address contextual activation sparsity where masks must generalize to unseen inputs, vary per token, and coordinate across layers through global allocation.
8	
9	Gradient analysis reveals a structural asymmetry: BCE's gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$ depends only on neuron $j$, while under KL divergence, the gradient couples each neuron to all others through the downstream Jacobian (\S\ref{sec:method:gradient}).
10	KL's coupled gradients discover neuron importance patterns that diverge 68\% from magnitude-based masks (per-layer Jaccard 32\%).
11	A target-swap ablation shows KL-discovered mask targets carry most of the quality information: BCE retrained on KL-derived targets approaches KL PPL ($\leq$0.65pp gap, 3-seed), while magnitude-trained BCE yields 28.13$\pm$0.20. Coupling contributes marginally to PPL but m
…[truncated 3030 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 2054 · 2026-05-23T01:26:53.917342+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool call

_source line 2055 · 2026-05-23T01:26:53.917777+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2056 · 2026-05-23T01:26:53.968448+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models (Figure~\ref{fig:overview}).
5	The method replaces per-neuron binary classification (BCE) with an output-distribution alignment objective that couples all pruning decisions through the model's forward pass and achieves competitive performance without auxiliary error compensation networks at inference.
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
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{x}^{(\ell)}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuro
…[truncated 9731 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 2057 · 2026-05-23T01:26:53.969128+00:00_

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
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4 on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB), using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $1 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), GSM8K (8-shot), HellaSwag (10-shot), and PIQA (0-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly\footnote{TEAL is deterministic; single-run evaluation suffices. KL/BCE predictors require multi-seed evaluation due to random initialization.}; (2) \textbf{BCE predictor} (Deja
…[truncated 17327 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 2058 · 2026-05-23T01:26:55.022157+00:00_

Web search results for query: "ACL Rolling Review May 2026 deadline submission date aclrollingreview.org"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the search results, I found information about ACL Rolling Review deadlines. However, the search results primarily contain information about January 2026 submission deadlines for ACL 2026, not specifically a May 2026 deadline.

The ACL Rolling Review submission deadline is always the 15th of the month, so the May 2026 deadline would be May 15, 2026.

For additional context, after submission, all
…[truncated 511 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 4518
}
```

</details>

---


### Tool result

_source line 2059 · 2026-05-23T01:26:55.625339+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline ARR commitment"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"}]

Based on the web search results, here's the information about EMNLP 2026's call for papers submission deadline and ARR commitment:

## ARR Sub
…[truncated 1153 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 5623
}
```

</details>

---


### Tool call

_source line 2060 · 2026-05-23T01:27:00.309540+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2061 · 2026-05-23T01:27:00.711639+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} and GRASP~\cite{shin2025grasp} predict activation sparsity patterns without additional training.
6	LaRoSA~\cite{huang2025larosa} applies layerwise orthogonal rotations for structured activation sparsity with wall-clock speedup on SiLU models.
7	Wang et al.~\cite{wang2025dynamicsparse}, AWQ~\cite{lin2024awq}, and Outlier Suppression+~\cite{wei2023outlier} address sparsity--quantization interactions and activation-aware quantization.
8	Dhar et al.~\cite{dhar2024activation} characterize activation sparsity opportunities across architectures, showing that SwiGLU models exhibit lower natural sparsity than ReLU counterparts.
9	OWL~\cite{yin2024owl} determines per-layer sparsity ratios from outlier distributions for weight pruning.
10	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
11	
12	\paragraph{Predictor-Based Contextual Sparsity.}
13	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
14	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
15	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
16	SVD-CSP~\cite{serbin2026svdcsp} compre
…[truncated 5041 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 2062 · 2026-05-23T01:27:00.862410+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2063 · 2026-05-23T01:27:01.714865+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Output-distribution alignment is the primary design dimension for PPL at moderate sparsity (30\%; signal type accounts for the majority of the gap; upper bound); cross-layer coupling contributes task-dependently---substantially for commonsense, marginally for reasoning (3-seed $K{=}4$-corrected; Appendices~\ref{app:k4_downstream},~\ref{app:constraint}).
5	A predictor ($<$1\% of base) reduces TEAL's PPL by 14.5\% via masks 46--68\% divergent from magnitude, with commonsense gains but knowledge-task regression across scales.
6	Limitations: MMLU/GSM8K decline, no wall-clock speedup, evaluation bounded at 7--14B.
7	Code and trained predictors will be released upon acceptance.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 852
}
```

</details>

---


### Tool call

_source line 2064 · 2026-05-23T01:27:01.715233+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 2065 · 2026-05-23T01:27:02.166607+00:00_

1	\section*{Limitations}
2	
3	Our findings are bounded by three key limitations.
4	\textbf{Sparsity sweet spot.} 30\% appears to be the lowest-degradation level for downstream fidelity; at 40\%, MMLU drops to 35.5\% (vs.\ 40.7\% at 30\%), and at 50\%, all methods collapse to near-random on reasoning tasks. A separate predictor must be retrained per target.
5	\textbf{Knowledge-intensive regression.} KL consistently underperforms magnitude-based methods on MMLU and GSM8K across scales (8B: $-$5.2pp MMLU; 14B: $-$20pp GSM8K), suggesting distribution-matching objectives systematically sacrifice reasoning-critical pathways.
6	\textbf{Training data homogeneity.} All predictors are trained on WikiText-103 (English Wikipedia). OOD evaluation on C4 shows preserved KL advantage but $31\times$ higher cross-seed variance (CV=6.3\% vs.\ 0.2\% in-domain), indicating domain sensitivity. Batched inference, where sparsity patterns must be intersected across sequences, may reduce effective sparsity and is not evaluated. All experiments use sequence length 2048; behavior at longer contexts (e.g., 8K--128K) is untested. Our evaluation focuses on perplexity and multiple-choice benchmarks; open-ended generation quality (e.g., MT-Bench) remains untested and may exhibit different sparsity sensitivity. The aggravation from 8B to 14B (GSM8K regression deepening from $-$1.3pp to $-$20.1pp) raises concern about scaling to 70B+; wall-clock speedup via sparse kernels also remains future work.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 2066 · 2026-05-23T01:27:02.167095+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 2067 · 2026-05-23T01:27:02.668600+00:00_

1	\section*{Ethics Statement}
2	
3	This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3, Qwen-2.5-14B~\cite{qwen2024qwen25}) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, HellaSwag, PIQA, MMLU, GSM8K).
4	No new data collection, annotation, or human subjects are involved.
5	The method does not alter model outputs beyond the sparsity-induced degradation we analyze; it introduces no new generation capabilities or safety risks beyond those inherent in the base models.
6	Compute requirements are modest (1000 training steps, $\sim$45 minutes on a single GPU for KL training), presenting minimal environmental concern relative to the pretrained models we evaluate on.
7	We release no model weights or user-facing systems; our contribution is analytical (understanding KL distillation for sparsity) rather than deployment-oriented.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 2068 · 2026-05-23T01:27:02.668935+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool call

_source line 2069 · 2026-05-23T01:27:02.970006+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 2070 · 2026-05-23T01:27:03.021028+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB; batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
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
33	The pipeline adds $\sim$6.4\% overhead
…[truncated 36747 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool result

_source line 2071 · 2026-05-23T01:27:03.021605+00:00_

1	% =============================================================================
2	% Additional references (R20 review response)
3	% =============================================================================
4	
5	@article{huang2025larosa,
6	  title={La{R}o{SA}: Accelerating Large Language Model Inference with Layerwise Rotated Sparse Activation},
7	  author={Huang, Fangcheng and others},
8	  journal={arXiv preprint arXiv:2507.01299},
9	  year={2025}
10	}
11	
12	@inproceedings{geva2023dissecting,
13	  title = {Dissecting Recall of Factual Associations in Auto-Regressive Language Models},
14	  author = {Geva, Mor and Bastings, Jasmijn and Filippova, Katja and Globerson, Amir},
15	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
16	  pages = {12216--12235},
17	  year = {2023},
18	}
19	
20	@article{fu2024lazyllm,
21	  title = {{LazyLLM}: Dynamic Token Pruning for Efficient Long Context {LLM} Inference},
22	  author = {Qichen Fu and Minsik Cho and Thomas Merth and Sachin Mehta and Mohammad Rastegari and Mahyar Najibi},
23	  year = {2024},
24	  journal = {arXiv preprint arXiv:2407.14057},
25	}
26	
27	@article{zhang2025cots,
28	  title = {{COTS}: Connected Sparse Activation for Efficient {LLM} Inference},
29	  author = {Yilong Zhang and Junyuan Shang and Huanqi Cao and Shiyao Li and Shuguang Jiang and Lingxiao Ma and Shun Zheng and Cheng Li and Jiang Bian},
30	  year = {2025},
31	  journal = {arXiv preprint arXiv:2502.14475},
32	}
33	
34	@inproceedings{alizadeh2024llmflash,
35	  title = {{LLM} in a Flash: Efficient Large Language Model Inference with Limited Memory},
36	  author = {Keivan Alizadeh and Iman Mirzadeh and Dmitry Belenko and Karen Khatamifard and Minsik Cho and Carlo C Del Mundo and Mohammad Rastegari and Mehrdad Farajtabar},
37	  year = {2024},
38	  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
39	}
40	
41	@article{wei2023outlier,
4
…[truncated 24334 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2072 · 2026-05-23T01:27:11.900768+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "file": "artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2073 · 2026-05-23T01:27:12.051791+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2074 · 2026-05-23T01:27:12.052207+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 2075 · 2026-05-23T01:27:12.956964+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (379 个)\n\n- **eval_spon_supp_retry**: DONE (failed) — \n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-23T01:05:43Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 378 个实验 — DEPLOYED 1, DONE 377\n**DONE 分布**: failed 35, killed 82, negative 24, success 236\n\n### 💾 磁盘余量\n- **westd-34887**:\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\n  - `/init`: 150M/150M 可用（已用 1%）\n  - `/usr/bin/nvidia-smi`: 817G/879G 可用（已用 3%）\n\n### 🏃 RUNNING\n_（无）_\n\n### 📌 最近完成 (top 5)\n- `c4_kl30_s42` [failed] — 2026-05-23T01:05:38 — CUDA OOM: CUDA out of memory. Tried to allocate 224.00 MiB. GPU 0 has a total ca\n- `spon_2048_s42` [killed] — 2026-05-23T00:11:36 — 启动后崩溃，日志仅9行，停在 Setting up data loader... 待诊断\n- `bce_isocompute_v2_s42` [killed] — 2026-05-23T00:11:35\n- `kl_sparsity70_s42_v2` [killed] — 2026-05-23T00:11:33\n- `jsd_50pct_s42` [killed] — 2026-05-23T00:11:32\n\n### 🔴 最近失败原因 (top 3)\n- `c4_kl30_s42`: CUDA OOM: CUDA out of memory. Tried to allocate 224.00 MiB. GPU 0 has a total capacity of 94.97 GiB of which 188.56 MiB is free. Process 94893 has 65.98 GiB memory in use. Including non-PyTorch memory\n- `spon_2048_s42`: 启动后崩溃，日志仅9行，停在 Setting up data loader... 待诊断\n- `bce_isocompute_v2_s42`: _(no failure_reason — pre-2026-04-24 entry)_\n\n&lt;!-- AUTO-FACTS-END -->\n\n---\n\n# Hando
…[truncated 1810 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 2076 · 2026-05-23T01:27:18.984221+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check review issues tracker file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check review issues tracker file"
  }
}
```

</details>

---


### Tool result

_source line 2077 · 2026-05-23T01:27:19.840241+00:00_

issues:
  # ============================================================
  # Round 25 (Fresh Review) — Active issues
  # ============================================================

  - id: "R20-W1"
    summary: "Per-layer KL decomposition 的 train-inference mismatch confound 未解决"
    category: method
    severity: critical
    status: in_progress
    first_raised_round: 20
    last_seen_round: 25
    mentions:
      - {round: 21, reviewers: [1, 2], note: "R21 Critical。K=4 single-seed。"}
      - {round: 22, reviewers: [1, 2], note: "R22 N2。97.5% 精确数字不可靠。"}
      - {round: 24, reviewers: [1, 2], note: "R24 C1。K=1 有 32× train-inference mismatch；K=4 在 50% 反常差于 K=1 (44.23 vs 34.85) 缺乏机制解释；仅两个 K 值不足以支撑 29-97% 精确分解。定性结论（signal type matters）由 Table 4 五种 loss 对比和梯度分析独立支撑。"}
      - {round: 25, reviewers: [1, 2], note: "R25 N1/N2。K=4 at 50% 反常（PPL 44.23 > K=1 34.85）仍仅有 gradient interference speculation 无实验证据。MMLU K=4 > E2E anomaly 暴露 allocation confound（K=4 near-uniform std=0.003 vs E2E non-uniform），decomposition 的两个维度不正交。Abstract/Conclusion 仍基于 30% 结果做 general claim 但 50% 下框架失效。两位 reviewer 一致认为这是核心可信度问题。"}
    action_items:
      - {round: 21, action: "K=4 3-seed (s42/s123/s456)", assigned_to: "main_agent", status: done}
      - {round: 22, action: "97.5% → 定性 'majority of PPL gap'", assigned_to: "paper_agent", status: done}
      - {round: 22, action: "K=4 50% s42 PPL-only 实验", assigned_to: "main_agent", status: done}
      - {round: 24, action: "Abstract/Conclusion 的 decomposition claim 删除精确百分比改为定性描述", assigned_to: "paper_agent", status: done}
      - {round: 24, action: "K=4 50% 反常结果补假设性解释（gradient interference at high sparsity）", assigned_to: "paper_agent", status: done}
      - {round: 25, action: "Abstract/Conclusion 中限定 decomposition 结论适用范围为 moderate sparsity (30%)", assigned_to: "paper_agent", status: done}
      - {round: 25, action: "正文 §4.5 明确讨论 allocation confound（K=4 改变 allocation pattern 导致无法独立归因 coupling）", assigned_to: "paper_agent", status: done}
      - {r
…[truncated 19374 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 2078 · 2026-05-23T01:27:19.893174+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/constraints.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/constraints.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 2079 · 2026-05-23T01:27:20.012991+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 119
}
```

</details>

---


### Tool call

_source line 2080 · 2026-05-23T01:27:56.103486+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
  }
}
```

</details>

---


### Tool result

_source line 2081 · 2026-05-23T01:28:19.147190+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 23043
}
```

</details>

---


### Tool call

_source line 2082 · 2026-05-23T01:28:19.298266+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验有效性**的审查。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle\n- **截止日期**：2026-05-25\n- **正文页数限制**：8 页（ACL 模板）\n- **匿名规则**：Double-blind\n- **附录**：允许，审稿人可选择性参考\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/submitted.pdf`\n\n## 审查侧重\n\n请重点审查以下方面，对每个方面给出具体发现：\n\n### 1. 方法论严谨性\n- §3.6 梯度分析（BCE vs KL gradient 对比）的论证是否充分？SNR 分析结论是否自洽？\n- §3.3 Gumbel-Sigmoid relaxation 的使用和论证\n- §3.5 Geometric penalty schedule 的收敛性论证\n- KL distillation 的 forward vs reverse 选择是否有充分实验支撑？\n\n### 2. 实验设计与统计可靠性\n- 3-seed 评估是否足以支撑核心声明？高方差指标（ARC-c σ=3.6, MMLU 30% global σ=9.5）的统计力\n- Table 2（主表）中不同方法间的比较是否公平？注意 allocation strategy 差异\n- Table 3 C1 ablation 的实验设计是否能支撑其声明？s42 oracle provenance 问题\n- Table 4 ablation 中哪些行是 3-seed、哪些是 single-seed？结论可靠性\n\n### 3. Per-layer KL decomposition (§4.5)\n- K=1 和 K=4 两个控制点能否支撑 signal type vs coupling scope 的分解？\n- K=4 在 50% 下反常（PPL 44.23 > K=1 34.85）的假设性解释是否充分？\n- 两个维度的正交性问题（K=4 改变 allocation pattern → allocation confound）\n\n### 4. Cross-architecture 和 Scale 结果\n- Mistral 和 Qwen-14B 的评估覆盖度\n- MMLU/GSM8K 跨规模退步的机制分析是否充分？\n- 6.4% latency overhead 的实际影响\n\n### 5. 实验覆盖度空白\n- 缺失的对比实验或 baseline\n- 未评估的重要场景\n\n请给出结构化审稿意见：Strengths（逐条）、Weaknesses（逐条，标注 Must-Fix / Should-Fix / Minor）、Questions、Missing References。最后给出 Overall Assessment 评分（使用 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）和置信度。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验有效性**的审查。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle\n- **截止日期**：2026-05-25\n- **正文页数限制**：8 页（ACL 模板）\n- **匿名规则**：Double-blind\n- **附录**：允许，审稿人可选择性参考\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/submitted.pdf`\n\n## 审查侧重\n\n请重点审查以下方面，对每个方面给出具体发现：\n\n### 1. 方法论严谨性\n- §3.6 梯度分析（BCE vs KL gradient 对比）的论证是否充分？SNR 分析结论是否自洽？\n- §3.3 Gumbel-Sigmoid relaxation 的使用和论证\n- §3.5 Geometric penalty schedule 的收敛性论证\n- KL distillation 的 forward vs reverse 选择是否有充分实验支撑？\n\n### 2. 实验设计与统计可靠性\n- 3-seed 评估是否足以支撑核心声明？高方差指标（ARC-c σ=3.6, MMLU 30% global σ=9.5）的统计力\n- Table 2（主表）中不同方法间的比较是否公平？注意 allocation strategy 差异\n- Table 3 C1 ablation 的实验设计是否能支撑其声明？s42 oracle provenance 问题\n- Table 4 ablation 中哪些行是 3-seed、哪些是 single-seed？结论可靠性\n\n### 3. Per-layer KL decomposition (§4.5)\n- K=1 和 K=4 两个控制点能否支撑 signal type vs coupling scope 的分解？\n- K=4 在 50% 下反常（PPL 44.23 > K=1 34.85）的假设性解释是否充分？\n- 两个维度的正交性问题（K=4 改变 allocation pattern → allocation confound）\n\n### 4. Cross-architecture 和 Scale 结果\n- Mistral 和 Qwen-14B 的评估覆盖度\n- MMLU/GSM8K 跨规模退步的机制分析是否充分？\n- 6.4% latency overhead 的实际影响\n\n### 5. 实验覆盖度空白\n- 缺失的对比实验或 baseline\n- 未评估的重要场景\n\n请给出结构化审稿意见：Strengths（逐条）、Weaknesses（逐条，标注 Must-Fix / Should-Fix / Minor）、Questions、Missing References。最后给出 Overall Assessment 评分（使用 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）和置信度。"
  }
}
```

</details>

---


### Tool result

_source line 2083 · 2026-05-23T01:28:38.333455+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19035
}
```

</details>

---


### Tool call

_source line 2084 · 2026-05-23T01:28:38.485231+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性**的审查。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle\n- **截止日期**：2026-05-25\n- **正文页数限制**：8 页（ACL 模板）\n- **匿名规则**：Double-blind\n- **附录**：允许，审稿人可选择性参考\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/submitted.pdf`\n\n## 审查侧重\n\n请重点审查以下方面，对每个方面给出具体发现：\n\n### 1. 新颖性与贡献边界\n- 核心组件（KL divergence + Gumbel-Sigmoid + predictor MLP）均为成熟技术——论文是否充分承认了这一点？\n- 与 MaskLLM（同样使用 KL + Gumbel + frozen weights + learnable masks）的区分是否有说服力？\n- 论文自定位为 \"empirical study\"——其 empirical 贡献（C1 ablation, signal-type/coupling decomposition）的新颖性是否足以达到 EMNLP 录取标准？\n- Contribution list 的排序和措辞是否准确反映实际贡献？\n\n### 2. 叙事框架与声明范围\n- Abstract/Introduction/Conclusion 中的核心声明是否有充分实验支撑？特别是关于 \"primary design dimension\" 的声明\n- signal type vs coupling scope 的分解声明是否限定在了适用范围内（30% moderate sparsity）？\n- MMLU/GSM8K 退步在正文中的讨论是否到位？是否被轻描淡写？\n- 论文的 framing 是否会给读者造成误导性印象（如暗示方法可用于实际加速）？\n\n### 3. Related Work 覆盖与定位\n- 是否遗漏了 2025-2026 年的重要相关工作？\n- Taxonomy（Table 1）的分类框架是否合理？是否有应纳入但缺失的方法？\n- 与 DejaVu, FastForward, ShadowLLM, D2D-MoE 的比较讨论是否公平？\n- 引用格式和完整性\n\n### 4. 写作质量与术语一致性\n- 术语使用是否一致（output-distribution alignment / KL distillation / output-distribution objective）？\n- 数值准确性（如 Introduction 中的百分比是否与实验数据一致）\n- 表格标注是否清晰（Table 2 的 †, ‡, * 等）\n- 论文整体可读性和叙事流畅度\n\n### 5. 格式与合规性\n- 8 页限制是否满足？\n- 匿名性是否完整（无自引泄露）？\n- Limitations 和 Ethics 章节是否符合 EMNLP 2026 要求？\n- 参考文献格式是否一致（ACL natbib）？\n\n请给出结构化审稿意见：Strengths（逐条）、Weaknesses（逐条，标注 Must-Fix / Should-Fix / Minor）、Questions、Missing References。最后给出 Overall Assessment 评分（使用 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）和置信度。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性**的审查。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle\n- **截止日期**：2026-05-25\n- **正文页数限制**：8 页（ACL 模板）\n- **匿名规则**：Double-blind\n- **附录**：允许，审稿人可选择性参考\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/submitted.pdf`\n\n## 审查侧重\n\n请重点审查以下方面，对每个方面给出具体发现：\n\n### 1. 新颖性与贡献边界\n- 核心组件（KL divergence + Gumbel-Sigmoid + predictor MLP）均为成熟技术——论文是否充分承认了这一点？\n- 与 MaskLLM（同样使用 KL + Gumbel + frozen weights + learnable masks）的区分是否有说服力？\n- 论文自定位为 \"empirical study\"——其 empirical 贡献（C1 ablation, signal-type/coupling decomposition）的新颖性是否足以达到 EMNLP 录取标准？\n- Contribution list 的排序和措辞是否准确反映实际贡献？\n\n### 2. 叙事框架与声明范围\n- Abstract/Introduction/Conclusion 中的核心声明是否有充分实验支撑？特别是关于 \"primary design dimension\" 的声明\n- signal type vs coupling scope 的分解声明是否限定在了适用范围内（30% moderate sparsity）？\n- MMLU/GSM8K 退步在正文中的讨论是否到位？是否被轻描淡写？\n- 论文的 framing 是否会给读者造成误导性印象（如暗示方法可用于实际加速）？\n\n### 3. Related Work 覆盖与定位\n- 是否遗漏了 2025-2026 年的重要相关工作？\n- Taxonomy（Table 1）的分类框架是否合理？是否有应纳入但缺失的方法？\n- 与 DejaVu, FastForward, ShadowLLM, D2D-MoE 的比较讨论是否公平？\n- 引用格式和完整性\n\n### 4. 写作质量与术语一致性\n- 术语使用是否一致（output-distribution alignment / KL distillation / output-distribution objective）？\n- 数值准确性（如 Introduction 中的百分比是否与实验数据一致）\n- 表格标注是否清晰（Table 2 的 †, ‡, * 等）\n- 论文整体可读性和叙事流畅度\n\n### 5. 格式与合规性\n- 8 页限制是否满足？\n- 匿名性是否完整（无自引泄露）？\n- Limitations 和 Ethics 章节是否符合 EMNLP 2026 要求？\n- 参考文献格式是否一致（ACL natbib）？\n\n请给出结构化审稿意见：Strengths（逐条）、Weaknesses（逐条，标注 Must-Fix / Should-Fix / Minor）、Questions、Missing References。最后给出 Overall Assessment 评分（使用 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）和置信度。"
  }
}
```

</details>

---


### Tool result

_source line 2085 · 2026-05-23T01:28:39.853204+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1367
}
```

</details>

---


### Assistant

_source line 2086 · 2026-05-23T01:28:59.093762+00:00_

Round 1 已启动：
- **Reviewer 1**（方法严谨性 + 实验有效性）：已派发
- **Reviewer 2**（新颖性 + 完整性）：已派发
- **视觉审查 Agent**：已启动（fire-and-forget，不阻塞审稿）

等待两位 Reviewer 提交初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 177

## Round 177

2 recorded events


### User

_source line 2087 · 2026-05-23T01:34:29.565112+00:00_

[Reviewer 1 审稿意见]:
## 总体评分
**Overall**: 3.5 / 5 — Borderline Conference
**Confidence**: 4 / 5 — Quite sure; I read the paper very carefully and am familiar with related work.
**一句话总结**: 论文提出用 forward KL 替代 BCE 训练稀疏预测器，PPL 改善显著且实验设计诚实透明，但知识类任务系统性退化（随 scale 恶化）、缺乏实际加速、以及核心分解分析在 50% 稀疏度下失效，限制了贡献的深度和实用性。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 核心方法论合理，C1 ablation 设计精巧；但 per-layer KL decomposition 在 50% 处崩溃（K=4 比 K=1 更差），signal type vs coupling scope 两个维度存在 allocation confound，downstream claims 的统计力不足（3-seed MMLU σ=9.5） |
| Excitement | 3.0/5 | KL > BCE 用于稀疏预测是有趣的实证发现，target-swap ablation 有新意；但缺乏实际推理加速（+6.4% overhead），且核心负面结果（知识任务退化随 scale 恶化）削弱了实用前景 |
| Reproducibility | 4.0/5 | 实验细节充分（种子、步数、超参），附录完整（19页），承诺 release 代码；但部分关键行是 single-seed（Table 4 BCE 变体、MSE 50%），且 C1 s42 oracle 来自不同训练 run |
| Clarity | 4.0/5 | 写作清晰，对局限性的披露非常诚实（罕见地在 abstract 里承认无加速、在正文持续标注 upper bound/confound）；但 Table 2 的 allocation 混用（BCE 30% 用 TEAL global，KL 用 uniform）需要读者仔细看脚注才能理解 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 知识类任务系统性退化随 scale 恶化，机制分析不充分
- 具体位置：§4.2 Table 2, §4.6 Table 13 (Appendix K), Limitations
- 问题：KL 在所有测试规模上一致地在 MMLU/GSM8K 上低于 TEAL——8B: MMLU -5.2pp, GSM8K -1.3pp (30%)；14B: MMLU -2.8pp, GSM8K **-20.1pp** (σ=5.2)。退化幅度从 8B 到 14B 恶化（GSM8K 从 -1.3pp 到 -20.1pp），暗示这不是可忽略的噪声而是系统性缺陷。论文提出两个假设（训练数据同质性、forward KL mode-covering 稀释稀有激活），但仅用 constraint experiment（remove valley, MMLU +3.4pp）部分验证了第一个因素，对第二个因素（mode-covering 导致 factual neuron 保护不足）没有任何实验支撑。
- 为什么影响接收：一个声称改善稀疏预测质量的方法，如果在推理和知识任务上系统性退化且随规模恶化，其实用价值存疑。对于 EMNLP 会议级别的论文，应该至少有一个初步的消融来验证第二个假设（例如用 mixed domain 数据训练，或 probe knowledge neurons 的保留率），或者明确限定方法的适用场景。
- 建议修改方向：(1) 在 WikiText-103 + 少量数学/代码数据上重新训练 predictor，测试 GSM8K 是否恢复；(2) 分析 KL vs magnitude masks 对已知 factual neurons（如 Meng et al., 2022 定位的）的保留率差异；(3) 如果无法修复，应将适用范围明确限定为"以 PPL 和 commonsense 为目标的场景"。

**N2** [critical] Per-layer KL 分解在 50% 稀疏度下失效，削弱核心贡献之一
- 具体位置：§4.5 (Per-Layer KL), Table 4
- 问题：论文的核心贡献之一是将稀疏预测训练分解为 signal type（输出分布 vs 中间层）和 coupling scope（端到端 vs 逐层）。然而，在 50% 稀疏度下，K=4 per-layer KL（PPL 44.23）**比 K=1**（PPL 34.85）**更差**，而 E2E KL 为 11.84。论文对此的解释是"partial coupling amplifies gradient interference"，但这是纯粹假设性的，没有任何实验证据。此外，在 30% 处 K=4 的 MMLU 异常（42.7±1.4 > E2E 40.7±1.3）暴露了 allocation confound：K=4 产生 near-uniform allocation (std=0.003)，恰好匹配 uniform inference protocol，而 E2E KL 学到非均匀 allocation（protection valley）。这意味着 K=4 同时改变了两个维度（coupling 和 allocation），signal type 和 coupling scope **并非正交**。
- 为什么影响接收：论文声称"signal type accounts for the majority of the PPL gap"（abstract, §4.5, conclusion），但这个 claim 标注为 upper bound，且仅在 30% 处可解释。如果这个分解是论文的核心分析贡献，它需要在关键操作点（50%）也成立，或者论文需要大幅降低这个 claim 的强度。
- 建议修改方向：(1) 在 50% 处增加更多 K 值（K=2, K=8, K=16）以建立连续曲线，而非仅两个控制点；(2) 在 K=4 控制中强制使用与 E2E 相同的 allocation pattern（而非让 K=4 自行收敛到 near-uniform），消除 allocation confound；(3) 如果无法解决，将分解框架限定为"30% moderate sparsity regime"，并在 abstract/conclusion 中明确这一限制。

**N3** [critical] 缺乏实际推理加速，实用贡献为零
- 具体位置：§1 Introduction (最后一段), Appendix A (Table 5), Limitations
- 问题：Predictor 增加 6.4% latency overhead（126.78 vs 119.11 ms/fwd），即使在 50% 稀疏度下也没有任何速度提升。论文使用的是 unstructured element-wise masks，不支持 sparse kernel 加速。论文坦诚地承认了这一点（"This is primarily an empirical study; wall-clock speedup requires sparse kernel support not addressed here"），但这意味着方法在当前形态下没有实用价值——它比 dense inference 更慢。
- 为什么影响接收：对于一个稀疏预测方法，不能带来任何推理加速是一个严重的实用性缺陷。虽然论文定位为"empirical study characterizing how the training objective shapes sparsity prediction quality"，但 reviewer 和 AC 可能期望至少有 proof-of-concept 的加速实验。Related work 中的 LaRoSA、PowerInfer 等方法已经实现了 wall-clock speedup，没有与这些方法的对比使得贡献的 positioning 不够 convincing。
- 建议修改方向：(1) 至少在一个 sparse kernel backend（Triton block-sparse / cuSPARSE）上展示 proof-of-concept 加速；(2) 如果不可行，增加与已有加速方法（LaRoSA 等）在 mask 质量层面的对比，证明 KL masks 在质量上的优势可以转化为更好的 quality-speedup tradeoff；(3) 讨论将 unstructured masks 转化为 structured（N:M / block-sparse）的路径和预期退化。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Downstream task 统计力不足：3 seeds 无法支撑细粒度比较
- 具体位置：Table 2, §4.2
- 问题：核心下游评估使用 3 seeds。对于 PPL（σ=0.02, CV=0.2%），3 seeds 完全足够。但对于下游任务，方差极高：MMLU 30% global σ=9.5（3-seed 95% CI 约 ±23.5pp），ARC-c 30% σ=3.6，Mistral ARC-c σ=6.4。论文正确指出"95% confidence intervals for individual downstream tasks overlap"，但仍在 abstract 和 conclusion 中做出下游比较的 claims（"commonsense gains but knowledge-intensive decline"）。这些 claims 的统计基础薄弱。
- 建议：(1) 将下游比较的 claims 进一步弱化为"directional trends"而非 established findings；(2) 在有方差报告的指标上计算并报告 paired t-test 或 bootstrap p-value，让读者判断显著性；(3) 如果条件允许，增加到 5-10 seeds 以改善统计力。

**W2** [warning] Table 2 Baseline 比较条件不统一
- 具体位置：Table 2, 脚注 †
- 问题：(1) BCE 30% 使用 TEAL global allocation（脚注说明 uniform 下 PPL=15.71），而 KL 30% 同时报告了 global 和 uniform——但 TEAL baseline 用的是 uniform。这使得横向比较需要在多个 allocation 间跳转。(2) BCE 50% 使用 2700 steps（2.71× KL 预算），而 KL 用 1000 steps。虽然 §4.3 解释了 iso-compute 动机，但这也意味着 Table 2 的 BCE 50% 结果对 BCE 是**有利**的（额外训练），KL 仍然大幅领先说明差距是本质的。(3) MSE 50% 只有 s42（s123 catastrophic PPL=15,789），单种子结果可靠性弱。
- 建议：在 Table 2 中统一报告 KL/BCE/TEAL 在同一 allocation 下的结果，或者增加一个清晰的"controlled comparison"子表。当前的注释系统虽然信息完整但增加了阅读难度。

**W3** [warning] C1 ablation 的 soft-vs-hard confound 未被完全解决
- 具体位置：§4.4 "Soft-vs-Hard Confound" 段落
- 问题：C1 把 KL predictor 的 soft logits 通过阈值（>0）二值化为 hard masks，然后用 BCE 训练新 predictor。但这改变了两件事：(1) 训练目标（KL→BCE），和 (2) mask 表示（soft ranking→binary）。论文承认了这个 confound 并报告了 BCE+Gumbel (32.22) vs standard BCE (27.97)，指出"softness alone does not explain KL's advantage"。但反过来说，C1 的 near-zero delta（≤0.79pp）可能部分来自于 KL masks 的 binary pattern 本身就足够好，而不是因为 BCE *training* on these targets 等价于 KL training。一个更干净的控制是：用 KL 训练但在推理时用 magnitude-based allocation（测试 KL 的 ranking 信息 vs pattern 信息）。
- 建议：增加讨论这个 confound 的含义，或增加一个实验控制（例如冻结 KL predictor 的 binary mask patterns 但重新训练 ranking scores）。

**W4** [warning] Qwen-14B 评估不完整
- 具体位置：§4.6, Appendix K (Table 13)
- 问题：Qwen-14B 的评估仅在 30% sparsity 下进行，且 GSM8K 在 uniform allocation 下只有 3-seed 均值（32.0±5.2），方差极高。没有 50% 的结果，没有 per-layer allocation 分析，也没有 C1 ablation。作为 cross-scale 证据，这不够有力——只有 PPL generalization 的 claim 是可靠的；downstream 的退化模式（GSM8K -20pp）需要更深入的分析。
- 建议：至少增加 50% sparsity 的 PPL 结果以验证 scaling pattern；讨论 14B 上 GSM8K 退化加剧的可能机制（超越 §4.2 对 8B 的假设）。

**W5** [warning] Forward KL vs Reverse KL 的实验论证依赖 30% 处的微小差距
- 具体位置：Table 4, §4.5 "Relaxation, Divergence, and SPON"
- 问题：在 30% 处，Forward KL (8.81) vs JSD (8.90) 差距仅 0.09 PPL（1.0%），Forward KL vs Reverse KL (9.26) 差距 0.45 PPL（5.1%）。论文引用 mode-covering 理论解释 forward KL 的优越性，但在这个差距水平下，理论叙事的支撑力度有限。只有在 50% 处差距才变得明显（+6.4% JSD, +8.6% RKL）。论文的叙事将 forward KL 选择呈现为一个重要的设计决策，但数据表明它更接近于 implementation detail（30% 差距小到可能被超参调整抹平）。
- 建议：弱化 forward KL 选择的叙事权重；或增加在更多 sparsity levels 的 ablation 以建立更稳健的趋势。

---

## 小问题（不影响接收）

- §3.4 Eq. 5：$\mathcal{L}_{\text{KL}}$ 的求和是 over vocabulary $v$，但没有说明是否 applied at every token position 还是某种平均方式。附录 G 才提到"summed over the vocabulary $v$ and averaged over sequence positions"——这应该在正文中明确。
- Table 2 脚注 ‡："Actual sparsity: KL 28.5% vs. TEAL 29.3% at 30%"——由于 KL 的 Lagrangian 控制器使实际稀疏度偏离目标 5%（Appendix C），所有与 TEAL 的 PPL 比较都存在 0.8pp 的稀疏度差异。虽然 Appendix D 表明这个差异的 PPL 影响小（0.67），但正文应更明确地说明 matched-sparsity 比较。
- Figure 1 (overview) 画得比较简单，没有展示训练阶段的 Gumbel relaxation 和 Lagrangian controller 的位置，对方法理解的帮助有限。
- §2 Related Work：SPON 的讨论在 §2 和 §4.5 各出现一次，建议合并。
- Appendix P "Oracle Mask Provenance"：s42 oracle 来自 earlier checkpoint 的问题应在正文 Table 3 caption 中更显著地标注（当前只有 † 号），因为这直接影响 C1 ablation 的可信度。

---

## 主要优势

1. **Target-swap ablation (C1) 设计精巧**：将 KL-derived mask patterns 迁移到 BCE 训练，clean 地分离了 mask pattern quality 和 training objective coupling 的贡献。这是一个有创意且有信息量的控制实验。

2. **对局限性的诚实披露极为罕见**：论文在 abstract 中就承认无加速、在正文中持续标注 "upper bound"/"confound"/"not fully orthogonal"、在 Limitations 中坦承所有负面发现。这种透明度在投稿论文中很少见，值得肯定。

3. **PPL 改善显著且一致**：14.5% at 30%、50% at 50%，跨架构一致（LLaMA、Mistral、Qwen），且 3-seed PPL 的方差极低（CV=0.2%），说明 KL 训练方式确实学到了更好的 mask patterns。

4. **实验覆盖面广**：5 种 loss 排名、3 个架构、6 个 sparsity levels、allocation 策略分析、sensitivity sweeps、OOD 评估、compensation redundancy——附录极为充分。

5. **2D taxonomy (signal type × coupling scope) 为理解稀疏预测方法提供了有用框架**：即使分解不完美，这个分析视角对后续工作有价值。

6. **训练成本极低**：1000 步、单 GPU、~45 分钟——方法的实用门槛非常低。

---

## Questions to Authors

Q1: 是否尝试过在多样化数据（WikiText + 少量数学/代码文本）上训练 predictor？这是验证知识任务退化是否可修复的最直接实验。

Q2: 在 K=4 控制中，如果强制使用 E2E KL 学到的非均匀 allocation（而非让 K=4 自行收敛到 near-uniform），MMLU 异常是否消失？这能直接测试 allocation confound 假设。

Q3: Table 4 中 BCE+Gumbel+Penalty (38.02) 比 BCE+Gumbel-no-penalty (32.22) 更差——为什么添加 sparsity penalty 会让 BCE 表现恶化？这与 KL 方向上 penalty 的帮助形成反差。

Q4: 论文报告 KL predictor 在 L14-L18 形成 protection valley（14-18% sparsity）。这个 pattern 在 Mistral 和 Qwen 上是否也出现？如果是，这可能揭示 SwiGLU 架构的通用属性。

Q5: 考虑到 C1 ablation 显示 mask patterns 携带了大部分质量信息，一个自然的后续是：能否用 KL 训练一个 "teacher predictor"，然后用 BCE 训练一个更高效的 "student predictor" on KL-derived targets？这可能兼得 KL 的 mask quality 和 BCE 的 training stability。

---

## Missing References

- **CATS** (Lee et al., 2024): §2 提到但 Table 2 未作为 baseline——考虑到 CATS 也是 per-layer adaptive threshold 方法且有 wall-clock speedup 数据，应该在实验中对比或至少讨论为何排除。
- **MaskLLM** (Fang et al., 2024): §1 和 §2 讨论了与 MaskLLM 的区别（static N:M vs contextual），但没有实验对比——即使 setting 不同，PPL 层面的数字对比可以帮助读者校准结果。
- **Mixture-of-Depths** (Raposo et al., 2024): §2 引用了但未讨论与 token-level sparsity prediction 的对比——本文的 per-token mask prediction 在概念上与 MoD 的 token routing 有对偶关系。

Sources:
- [ACL Rolling Review Form](https://aclrollingreview.org/reviewform)
- [ARR Reviewer Guidelines](https://aclrollingreview.org/reviewerguidelines)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2088 · 2026-05-23T01:34:37.591335+00:00_

Reviewer 1 审稿意见已收到（3.5 Borderline Conference）。等待 Reviewer 2 提交后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 178

## Round 178

2 recorded events


### User

_source line 2089 · 2026-05-23T01:34:43.710585+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审稿总结**：Overall 3.5（Borderline Conference），置信度 4/5。

核心发现：
- **3 个 Must-Fix**：(1) 知识任务退化随 scale 恶化（14B GSM8K -20pp），机制分析不足；(2) per-layer KL 分解在 50% 稀疏度失效（K=4 比 K=1 更差），signal type vs coupling scope 不正交；(3) 无实际推理加速（+6.4% overhead）
- **5 个 Should-Fix**：downstream 统计力不足（3-seed MMLU σ=9.5）、Table 2 baseline 条件不统一、C1 soft-vs-hard confound、Qwen-14B 评估不完整、forward vs reverse KL 差距在 30% 处微小
- **主要优势**：C1 target-swap ablation 设计精巧、PPL 改善显著一致（14.5%/50%）、对局限性的诚实披露极罕见、实验覆盖面广

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2090 · 2026-05-23T01:34:48.230775+00:00_

Reviewer 1 意见已收到。等待 Reviewer 2 完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 179

## Round 179

6 recorded events


### User

_source line 2091 · 2026-05-23T01:34:49.736771+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**Confidence**: 4 (Quite sure; important points checked, familiar with activation sparsity and KL distillation literature)
**一句话总结**: 扎实的实证研究，将 KL distillation 首次系统应用于 contextual activation sparsity prediction，实验覆盖面广且诚实，但核心贡献（signal type vs coupling scope 分解）存在不可忽视的方法论混淆，加上缺乏实际加速和知识任务系统退步，限制了影响力。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 主体实验设计合理，多 seed 评估值得肯定；但 signal type vs coupling scope 分解的 K=1 control 存在 train-inference mismatch 混淆，K=4 在 50% 失效；C1 ablation 有 soft-vs-hard confound |
| Excitement | 2.5/5 | 将成熟组件（KL、Gumbel-Sigmoid、MLP predictor）应用于新场景，empirical findings 有参考价值但缺乏方法论创新或实际效率提升 |
| Reproducibility | 4/5 | 训练细节充分（超参、硬件、seed），exp_id 标注便于追溯，承诺 release code/predictors；唯一不足是 oracle mask 提取的 trajectory 依赖性 |
| Overall Assessment | 3.5/5 | Borderline Conference——实验深度足够 Findings，但核心分解 claim 的方法论问题和有限新颖性使 Conference 门槛有风险 |

---

## 主要优势（Strengths）

**S1. 系统且诚实的实证框架。** 论文从五种 loss 函数的对比出发，覆盖三种架构（LLaMA-3.1-8B、Mistral-7B-v0.3、Qwen-2.5-14B）、多个 sparsity 级别（25%–70%）和两种 allocation 策略。全程 3-seed 评估（PPL σ=0.02）、OOD 测试（C4）、cross-seed mask 一致性分析，实验可信度高。对 wall-clock speedup 缺失、MMLU/GSM8K 退步等 limitation 的主动披露体现了学术诚信（Abstract line 8, Limitations section）。

**S2. C1 Target-Swap Ablation 设计巧妙。** 将 KL 发现的 mask pattern 提取后用标准 BCE 重新训练（Table 3），在 30% (≤1.70pp) 和 50% (≤0.79pp) 均接近 KL 性能，有力地证明了 mask target quality 而非 gradient coupling 是推理时质量的主要驱动力。这是一个有意义的实验设计。

**S3. PPL 改进显著且跨架构一致。** KL predictor 在 30% sparsity 下 PPL 降低 14.5%（matched actual sparsity），50% 降低约 50%。该优势在 Mistral-7B 上一致复现（−17.3%, 3-seed, Table 16），PPL 层面的改进令人信服。

**S4. Compensation 冗余性发现实用。** 证明 FastForward 风格的 67.2M 补偿网络在 KL predictor 下完全冗余（Appendix J），可省去推理开销和额外参数，对实际部署有价值。

**S5. 写作质量整体较高。** 叙事从问题定义到方法到实验的逻辑链清晰，Section 3.6 的 gradient analysis 提供了直觉，Related Work 的二维 taxonomy（Table 1）提供了有用的文献整理框架。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Signal type vs coupling scope 分解存在不可消除的混淆变量

- 具体位置：Section 4.4 (¶Per-Layer KL), Table 4, Abstract, Conclusion
- 问题：分解的核心 claim 是"signal type accounts for the majority of the PPL gap"（Abstract line 5, Conclusion line 1）。但 K=1 per-layer KL 的 control 设计同时改变了两个变量：(1) 移除 cross-layer gradient coupling, (2) 引入严重的 train-inference mismatch（训练时仅 mask 1/32 layers，推理时 mask 全部 32 layers）。论文承认这是"upper bound"（Section 4.4 footnote 5），但仍然在 Abstract 和 Conclusion 中将其作为核心结论陈述。K=4 control 仅部分缓解：在 50% sparsity 下 K=4 (44.23) 反而比 K=1 (34.85) 差，论文自身也承认该分解"unreliable under the current design"（Section 4.4 最后一段）。一个在 50% 失效的分解不应在 Abstract 中以不加限定的方式呈现。
- 为什么影响接收：这是论文的第一条 contribution（Section 1, bullet 1）。如果分解本身不可靠，该 contribution 的价值大幅缩水。
- 建议修改方向：(1) 在 Abstract 和 Conclusion 中明确限定为"at 30% moderate sparsity, subject to train-inference mismatch confound"；(2) 考虑设计更干净的 deconfounding 实验，例如训练时 mask 全部 32 layers 但每 layer 独立优化（不传播 cross-layer gradient），或使用 stop-gradient 阻断 cross-layer 梯度流。

**N2** [critical] 知识任务系统性退步的讨论深度不够，与"primary design dimension"的强 claim 矛盾

- 具体位置：Section 4.2 (¶Knowledge-Task Regression), Table 2, Section 5, Abstract
- 问题：KL predictor 在所有测试规模上知识密集型任务系统退步——8B MMLU −5.2pp, 14B GSM8K −20.1pp (σ=5.2pp), Mistral GSM8K −7.3pp (8.6 vs 15.9)。Abstract 仅说"commonsense gains but knowledge-intensive decline"，没有量化 decline 幅度。Conclusion 将其归入一句"Limitations"。但 Section 4.2 的 hypothesis（训练数据偏倚 + forward KL mode-covering 稀释 rare activations）仅是推测，没有实验验证。Constraint experiment（Appendix T）只部分验证了 allocation 因素（MMLU +3.4pp），loss-level contribution"awaits knowledge-neuron probing"。
- 为什么影响接收：如果方法在知识/推理任务上系统性变差，称 output-distribution alignment 为"primary design dimension"就有误导性——它只是 PPL 和 commonsense 的 primary dimension，对 knowledge-intensive 任务则是 inferior。
- 建议修改方向：(1) Abstract 应量化 MMLU/GSM8K 退步幅度；(2) 将"primary design dimension"限定为"for perplexity and commonsense tasks at moderate sparsity"；(3) 在 main text 中更深入讨论知识退步的原因（而非只在 hypothesis 段推测）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 与 MaskLLM 的区分需要加强，Taxonomy Table 1 中遗漏 MaskLLM

- 具体位置：Section 2 (¶Predictor-Based Contextual Sparsity), Table 1
- 问题：MaskLLM（NeurIPS 2024）与本文共享核心 recipe：frozen weights + learnable masks + KL divergence training + Gumbel sampling。论文列出三点区分（contextual vs static masks, cross-layer allocation, distribution shift robustness），这些区分是合理的，但论文没有做任何实验来验证这些区分的影响（例如，在 activation sparsity 场景下直接对比 MaskLLM 的 static mask 方案）。更值得注意的是，Table 1 的 taxonomy 中 Static × Coupled 仅列了 SPON，而 MaskLLM 也属于此格（static per-weight masks + KL coupled training），应被纳入。
- 建议：(1) 在 Table 1 的 Static × Coupled 格中加入 MaskLLM；(2) 增加一段讨论明确说明为什么 contextual adaptation 是 activation sparsity 场景中关键的额外需求。

**W2** [warning] 14.5% PPL improvement 的引用基准在 Abstract/Introduction 与 Main Table 不一致，可能误导读者

- 具体位置：Abstract line 3, Introduction ¶14, Table 2
- 问题：Abstract 和 Introduction 声称"reduces perplexity by 14.5% over TEAL at matched sparsity (8.81 vs. 10.30, both at 28.5%)"。但 10.30 这个数字来自 Appendix D（matched actual sparsity comparison），不在 main text 的 Table 2 中。Table 2 中 TEAL uniform 30% 的 PPL 是 10.82。按 Table 2 的对比，KL 的改进是 (10.82−8.81)/10.82 = 18.6%，而非 14.5%。论文选择更保守的 14.5% 是可以理解的，但一级读者会去 Table 2 验证，发现数字对不上。
- 建议：在 Abstract 中用 Table 2 的数字（或同时报告两个基准），或在 Table 2 中增加 matched actual sparsity 的对比行。

**W3** [warning] 缺少重要近期相关工作：ActTail (March 2026)

- 具体位置：Section 2
- 问题：ActTail (arXiv:2603.12272, March 2026) 提出基于 Heavy-Tailed Self-Regularization 理论的全局 activation sparsity allocation 方法，直接针对"uniform sparsity across projections ignores heterogeneous statistical properties"的问题。该工作与本文的 global top-k allocation 和 per-layer sparsity distribution 分析（Section 4.6, Appendix E）高度相关，应当讨论。
- 建议：在 Related Work 的 Training-Free Activation Sparsity 段中加入 ActTail 的讨论。

**W4** [warning] 论文实际未展示任何推理加速，但 title 和 framing 可能产生效率方面的误导

- 具体位置：Title, Section 1, Appendix A
- 问题：标题"Output-Distribution Distillation for Contextual Sparsity Prediction"暗示了对推理效率的贡献。但实际上方法增加 6.4% latency overhead（Appendix A, Table 5），且明确表示"wall-clock speedup requires sparse kernel support not addressed here"（Abstract, Section 1）。虽然论文诚实地披露了这一点，但 framing 仍可能给匆忙的读者留下效率改进的印象。
- 建议：在 Abstract 和 Introduction 更早的位置明确声明"this work focuses on prediction quality, not inference speedup"，或在 Limitations 中更突出这一点。

**W5** [warning] C1 Ablation 的 Soft-vs-Hard Confound 未完全解决

- 具体位置：Section 4.3 (¶Soft-vs-Hard Confound)
- 问题：C1 ablation 在提取 oracle masks 时将 KL predictor 的连续 logits 二值化（logits > 0），因此 C1 同时改变了 target source 和 mask representation。论文注意到了这一点并报告了 BCE+Gumbel (32.22) vs standard BCE (27.97) 的对比，但这个对比本身不足以排除 confound——因为 BCE+Gumbel 使用的是 magnitude-based targets 而非 KL-derived targets。完全的 deconfounding 需要将 KL 的连续 soft scores（而非二值化版本）传递给 BCE predictor 作为 regression targets。
- 建议：在讨论中明确承认这一 confound 无法完全排除，或增加一个使用 soft regression targets 的实验。

---

## 小问题（不影响接收）

**M1.** Introduction ¶14 中"forward KL outperforms reverse KL by 8.6% and JSD by 6.4%"（Section 1）未标注 sparsity level。这些数字来自 50% (Table 4)，在 30% 时差距小得多（KL 8.81 vs JSD 8.90 vs RevKL 9.26）。应明确标注。

**M2.** 术语在全文中不完全一致："output-distribution alignment"（Method/Conclusion）、"output-distribution objective"（Introduction）、"output-distribution-coupled objective"（Related Work）、"KL distillation"（多处）指代同一概念。建议在首次出现时定义统一术语并一致使用。

**M3.** Table 2 的注脚标记较密集（†, ‡, *, ±），读者需要反复参照 caption 才能理解每行的确切设置。特别是 BCE 30% 的 † 标注说"TEAL global"但 main text 并未在显著位置解释为什么 BCE 用 global 而 KL 的主要报告用 uniform。建议简化或在正文中简述。

**M4.** Section 4.2 中 "MMLU 40.7±1.3%" 在正文和 Table 2 中一致，但 Introduction ¶14 表述为"stable downstream (MMLU 40.7±1.3%, 3-seed)"——相对于 dense 65.27% 而言，MMLU 降低了 24.5pp，称之为"stable"是否准确？这里指的是跨 seed 的稳定性，而非绝对性能的稳定性，应当澄清措辞。

**M5.** 页数合规性：Conclusion（Section 5）文本似乎延伸至第 9 页开头（约 1-2 行溢出）。EMNLP 2026 的 8 页正文限制是硬约束。建议检查 LaTeX 编译结果，确保 Section 5 完全在第 8 页内结束。如果确实溢出，需要压缩正文。

**M6.** Introduction 中"KL's coupled gradients discover neuron importance patterns that diverge 68% from magnitude-based masks (per-layer Jaccard 32%)"——68% divergence 和 32% Jaccard 是同一个度量的两种表述（Jaccard distance = 1 − IoU），但同一句中同时给出两个数字容易混淆。

**M7.** Qwen-2.5-14B 的 GSM8K 退步从 8B 的 −1.3pp 剧增至 14B 的 −20.1pp，但论文未深入分析原因。Limitations 仅提及"aggravation from 8B to 14B"。如果方法在 scale up 时退步加剧，这对 scalability claim 是重大挑战。

---

## 缺失引用（Missing References）

1. **ActTail** (arXiv:2603.12272, March 2026)——基于 HT-SR 理论的全局 activation sparsity allocation，与本文的 per-layer allocation 分析直接相关。
2. 论文已引用的 MaskLLM 讨论充分，但应在 Table 1 taxonomy 中体现其位置。

---

## Questions to Authors

1. 对于 N1：是否有可能设计一个 stop-gradient 实验，在保持 output-distribution KL loss 的同时阻断 cross-layer gradient propagation？这将比 per-layer KL 更干净地隔离 coupling scope。

2. 对于 N2：在 14B scale 上 GSM8K 退步 −20.1pp（σ=5.2pp），你们是否验证过这不是由于 Qwen-2.5-14B 的 SwiGLU 架构差异（d_ff = 18944 vs LLaMA 的 14336）导致的 predictor 架构不匹配？

3. 关于 W2：为什么选择在 Abstract 中报告 Appendix 的 matched-sparsity 数字（10.30）而非 main table 的 nominal-sparsity 数字（10.82）？如果 actual sparsity 不同，比较 PPL 的意义何在——是否应该先解决 sparsity controller 的精度问题？

4. Table 4 中 Per-layer KL K=4 在 50% 时 PPL=44.23，比 K=1 的 34.85 差很多。你们的 hypothesis（partial coupling 在 tight capacity 下 amplifies gradient interference）有没有进一步的实验支持？

---

## 总结

本文提出将 output-distribution KL distillation 应用于 SwiGLU LLM 的 contextual activation sparsity prediction，是该方向上首个系统性实证研究。PPL 层面的改进显著且跨架构一致，C1 target-swap ablation 设计有新意，compensation 冗余性发现有实用价值。

主要顾虑集中在两点：(1) signal type vs coupling scope 分解——论文的核心 empirical contribution——的方法论可靠性不足，confound 在 50% 下完全无法消除；(2) 知识密集型任务的系统性退步与"primary design dimension"的强 claim 之间存在张力。此外，方法目前未展示实际推理加速，新颖性主要来自成熟组件在新场景的应用。

这些问题不影响论文在 Findings 的合理性（solid empirical work），但要达到 Conference 门槛，核心 claim 的精确性和分解实验的严谨性需要提升。

**推荐**：3.5 (Borderline Conference)——如果作者能在 rebuttal 中 (1) 限定分解 claim 的适用范围并提供更干净的 deconfounding 证据，(2) 在 Abstract/Conclusion 中平衡 PPL 优势与知识任务退步的叙述，有机会升至 Conference。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2092 · 2026-05-23T01:35:35.700834+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix/Should-Fix/Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供具体证据（引用论文中的 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n### Overall: 3.5 / 5 — Borderline Conference, Confidence 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] 知识类任务系统性退化随 scale 恶化，机制分析不充分\n- KL 在所有测试规模上 MMLU/GSM8K 低于 TEAL——8B: MMLU -5.2pp, GSM8K -1.3pp (30%)；14B: GSM8K -20.1pp (σ=5.2)。退化从 8B 到 14B 恶化。论文提出两个假设（训练数据同质性、forward KL mode-covering），仅用 constraint experiment（remove valley, MMLU +3.4pp）部分验证第一个因素，第二个因素无实验支撑。建议至少做 mixed domain 训练或 knowledge neuron probe。\n\n**N2** [critical] Per-layer KL 分解在 50% 稀疏度下失效\n- K=4 per-layer KL (PPL 44.23) 比 K=1 (34.85) 更差，E2E KL 为 11.84。50% 下分解完全失效。K=4 MMLU 异常（42.7±1.4 > E2E 40.7±1.3）暴露 allocation confound：K=4 产生 near-uniform allocation (std=0.003)，signal type 和 coupling scope 并非正交。建议增加更多 K 值或强制 K=4 使用 E2E allocation pattern。\n\n**N3** [critical] 缺乏实际推理加速，实用贡献为零\n- 6.4% latency overhead，unstructured masks 无 sparse kernel 加速。方法比 dense inference 更慢。建议至少做 proof-of-concept sparse kernel 加速，或与 LaRoSA 等已有加速方法在 mask quality 层面对比。\n\n### Should-Fix 问题\n\n**W1** [warning] 3 seeds 下游统计力不足（MMLU 30% global σ=9.5，95% CI 约 ±23.5pp）\n**W2** [warning] Table 2 baseline 比较条件不统一（BCE 30% 用 global，KL 用 uniform+global；BCE 50% 用 2700 steps）\n**W3** [warning] C1 ablation soft-vs-hard confound（二值化丢失 ranking 信息）\n**W4** [warning] Qwen-14B 仅 30% sparsity，无 50% 结果，评估不完整\n**W5** [warning] Forward KL vs Reverse KL 在 30% 处差距微小（8.81 vs 9.26）\n\n### 小问题\n- Eq. 5 求和方式正文未明确（附录才说明 average over positions）\n- Table 2 脚注 ‡ matched sparsity 对比应更显著\n- Figure 1 过于简略\n- SPON 讨论在 §2 和 §4.5 重复\n- C1 s42 oracle provenance 应在 Table 3 caption 更显著标注\n\n### 主要优势\n1. C1 target-swap ablation 设计精巧\n2. 对局限性的诚实披露极罕见\n3. PPL 改善显著且一致（14.5%/50%/82%）\n4. 实验覆盖面广（5 种 loss、3 架构、6 sparsity levels）\n5. 2D taxonomy 有用\n6. 训练成本极低（单 GPU ~45 min）\n\n### Questions\nQ1: 多样化数据训练是否能修复知识任务退化？\nQ2: K=4 强制使用 E2E allocation 时 MMLU 异常是否消失？\nQ3: BCE+Gumbel+Penalty (38.02) 为何比无 penalty (32.22) 更差？\nQ4: L14-L18 protection valley 在 Mistral/Qwen 上是否也出现？\nQ5: KL teacher + BCE student 两阶段训练是否可行？\n\n### Missing References\n- CATS 应作为 baseline 对比或解释排除原因\n- MaskLLM 应有 PPL 层面数字对比\n- Mixture-of-Depths 与 per-token mask prediction 的对偶关系\n\n---\n\n请逐条回应以上所有 Must-Fix、Should-Fix 和主要 Questions。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix/Should-Fix/Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供具体证据（引用论文中的 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n### Overall: 3.5 / 5 — Borderline Conference, Confidence 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] 知识类任务系统性退化随 scale 恶化，机制分析不充分\n- KL 在所有测试规模上 MMLU/GSM8K 低于 TEAL——8B: MMLU -5.2pp, GSM8K -1.3pp (30%)；14B: GSM8K -20.1pp (σ=5.2)。退化从 8B 到 14B 恶化。论文提出两个假设（训练数据同质性、forward KL mode-covering），仅用 constraint experiment（remove valley, MMLU +3.4pp）部分验证第一个因素，第二个因素无实验支撑。建议至少做 mixed domain 训练或 knowledge neuron probe。\n\n**N2** [critical] Per-layer KL 分解在 50% 稀疏度下失效\n- K=4 per-layer KL (PPL 44.23) 比 K=1 (34.85) 更差，E2E KL 为 11.84。50% 下分解完全失效。K=4 MMLU 异常（42.7±1.4 > E2E 40.7±1.3）暴露 allocation confound：K=4 产生 near-uniform allocation (std=0.003)，signal type 和 coupling scope 并非正交。建议增加更多 K 值或强制 K=4 使用 E2E allocation pattern。\n\n**N3** [critical] 缺乏实际推理加速，实用贡献为零\n- 6.4% latency overhead，unstructured masks 无 sparse kernel 加速。方法比 dense inference 更慢。建议至少做 proof-of-concept sparse kernel 加速，或与 LaRoSA 等已有加速方法在 mask quality 层面对比。\n\n### Should-Fix 问题\n\n**W1** [warning] 3 seeds 下游统计力不足（MMLU 30% global σ=9.5，95% CI 约 ±23.5pp）\n**W2** [warning] Table 2 baseline 比较条件不统一（BCE 30% 用 global，KL 用 uniform+global；BCE 50% 用 2700 steps）\n**W3** [warning] C1 ablation soft-vs-hard confound（二值化丢失 ranking 信息）\n**W4** [warning] Qwen-14B 仅 30% sparsity，无 50% 结果，评估不完整\n**W5** [warning] Forward KL vs Reverse KL 在 30% 处差距微小（8.81 vs 9.26）\n\n### 小问题\n- Eq. 5 求和方式正文未明确（附录才说明 average over positions）\n- Table 2 脚注 ‡ matched sparsity 对比应更显著\n- Figure 1 过于简略\n- SPON 讨论在 §2 和 §4.5 重复\n- C1 s42 oracle provenance 应在 Table 3 caption 更显著标注\n\n### 主要优势\n1. C1 target-swap ablation 设计精巧\n2. 对局限性的诚实披露极罕见\n3. PPL 改善显著且一致（14.5%/50%/82%）\n4. 实验覆盖面广（5 种 loss、3 架构、6 sparsity levels）\n5. 2D taxonomy 有用\n6. 训练成本极低（单 GPU ~45 min）\n\n### Questions\nQ1: 多样化数据训练是否能修复知识任务退化？\nQ2: K=4 强制使用 E2E allocation 时 MMLU 异常是否消失？\nQ3: BCE+Gumbel+Penalty (38.02) 为何比无 penalty (32.22) 更差？\nQ4: L14-L18 protection valley 在 Mistral/Qwen 上是否也出现？\nQ5: KL teacher + BCE student 两阶段训练是否可行？\n\n### Missing References\n- CATS 应作为 baseline 对比或解释排除原因\n- MaskLLM 应有 PPL 层面数字对比\n- Mixture-of-Depths 与 per-token mask prediction 的对偶关系\n\n---\n\n请逐条回应以上所有 Must-Fix、Should-Fix 和主要 Questions。"
  }
}
```

</details>

---


### Tool result

_source line 2093 · 2026-05-23T01:36:10.394943+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 34694
}
```

</details>

---


### Tool call

_source line 2094 · 2026-05-23T01:36:10.846859+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix/Should-Fix/Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供具体证据（引用论文中的 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n### Overall: 3.5 (Borderline Conference), Confidence 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] Signal type vs coupling scope 分解存在不可消除的混淆变量\n- K=1 per-layer KL 同时改变：(1) 移除 cross-layer gradient coupling, (2) 引入 train-inference mismatch（训练 1/32 layers，推理全部 32）。K=4 仅部分缓解，在 50% 下 K=4 (44.23) 比 K=1 (34.85) 更差，论文自身承认分解\"unreliable under the current design\"。但 Abstract 和 Conclusion 仍将此作为核心结论。建议限定为\"at 30% moderate sparsity, subject to train-inference mismatch confound\"，或设计 stop-gradient 实验更干净地隔离 coupling。\n\n**N2** [critical] 知识任务系统性退步与\"primary design dimension\"强 claim 矛盾\n- 8B MMLU −5.2pp, 14B GSM8K −20.1pp, Mistral GSM8K −7.3pp。Abstract 仅说\"commonsense gains but knowledge-intensive decline\"未量化。Conclusion 归入一句 Limitations。§4.2 的两个假设仅推测无实验验证。\"primary design dimension\" 只对 PPL 和 commonsense 成立，对知识任务是 inferior。建议限定适用范围并在 Abstract 量化退步幅度。\n\n### Should-Fix 问题\n\n**W1** [warning] 与 MaskLLM 区分需加强，Table 1 遗漏 MaskLLM\n- MaskLLM（NeurIPS 2024）共享 frozen weights + learnable masks + KL + Gumbel recipe。三点区分合理但无实验验证。Table 1 Static × Coupled 格仅列 SPON，应纳入 MaskLLM。\n\n**W2** [warning] 14.5% PPL improvement 的引用基准不一致\n- Abstract 用 matched sparsity 数字（8.81 vs 10.30, 来自 Appendix），Table 2 中 TEAL uniform 30% 是 10.82。按 Table 2 改进是 18.6%。一级读者验证 Table 2 会发现数字对不上。\n\n**W3** [warning] 缺少 ActTail (arXiv:2603.12272, March 2026)\n- 基于 HT-SR 理论的全局 activation sparsity allocation，与本文 per-layer allocation 分析直接相关。\n\n**W4** [warning] 标题/framing 可能产生效率误导\n- 标题暗示推理效率贡献，但方法增加 6.4% overhead。论文诚实披露但 framing 可能误导匆忙读者。\n\n**W5** [warning] C1 ablation soft-vs-hard confound 未完全解决\n- 二值化 KL logits (>0) 同时改变 target source 和 mask representation。BCE+Gumbel (32.22) vs standard BCE (27.97) 不足以排除 confound（它们用的是 magnitude targets 而非 KL targets）。\n\n### 小问题\n- M1: Intro 中 8.6%/6.4% 未标注 sparsity level（来自 50%，30% 差距小得多）\n- M2: 术语不一致（output-distribution alignment/objective/coupled objective/KL distillation）\n- M3: Table 2 注脚标记过密\n- M4: \"stable downstream (MMLU 40.7±1.3%)\" 相对 dense 65.27% 降 24.5pp，\"stable\" 指跨 seed 稳定性应澄清\n- M5: 页数合规性——Conclusion 可能溢出第 8 页\n- M6: 68% divergence 和 32% Jaccard 同句出现易混淆\n- M7: 14B GSM8K 退步剧增（-1.3pp → -20.1pp）未深入分析\n\n### 主要优势\n1. 系统且诚实的实证框架（5 种 loss, 3 架构, 多 sparsity, 3-seed, OOD, cross-seed consistency）\n2. C1 target-swap ablation 设计巧妙\n3. PPL 改进显著且跨架构一致\n4. Compensation 冗余性发现实用\n5. 写作质量整体高，2D taxonomy 有用\n\n### Questions\nQ1: stop-gradient 实验能否更干净地隔离 coupling scope？\nQ2: Qwen-2.5-14B d_ff=18944 vs LLaMA 14336 的架构差异是否导致 predictor 不匹配？\nQ3: 为何 Abstract 用 Appendix matched-sparsity 数字而非 main table？\nQ4: K=4 50% PPL=44.23 反常的 gradient interference hypothesis 有无进一步实验支持？\n\n### Missing References\n- ActTail (arXiv:2603.12272, March 2026)\n- MaskLLM 应在 Table 1 taxonomy 中体现位置\n\n---\n\n请逐条回应以上所有 Must-Fix、Should-Fix 和主要 Questions。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix/Should-Fix/Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供具体证据（引用论文中的 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n### Overall: 3.5 (Borderline Conference), Confidence 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] Signal type vs coupling scope 分解存在不可消除的混淆变量\n- K=1 per-layer KL 同时改变：(1) 移除 cross-layer gradient coupling, (2) 引入 train-inference mismatch（训练 1/32 layers，推理全部 32）。K=4 仅部分缓解，在 50% 下 K=4 (44.23) 比 K=1 (34.85) 更差，论文自身承认分解\"unreliable under the current design\"。但 Abstract 和 Conclusion 仍将此作为核心结论。建议限定为\"at 30% moderate sparsity, subject to train-inference mismatch confound\"，或设计 stop-gradient 实验更干净地隔离 coupling。\n\n**N2** [critical] 知识任务系统性退步与\"primary design dimension\"强 claim 矛盾\n- 8B MMLU −5.2pp, 14B GSM8K −20.1pp, Mistral GSM8K −7.3pp。Abstract 仅说\"commonsense gains but knowledge-intensive decline\"未量化。Conclusion 归入一句 Limitations。§4.2 的两个假设仅推测无实验验证。\"primary design dimension\" 只对 PPL 和 commonsense 成立，对知识任务是 inferior。建议限定适用范围并在 Abstract 量化退步幅度。\n\n### Should-Fix 问题\n\n**W1** [warning] 与 MaskLLM 区分需加强，Table 1 遗漏 MaskLLM\n- MaskLLM（NeurIPS 2024）共享 frozen weights + learnable masks + KL + Gumbel recipe。三点区分合理但无实验验证。Table 1 Static × Coupled 格仅列 SPON，应纳入 MaskLLM。\n\n**W2** [warning] 14.5% PPL improvement 的引用基准不一致\n- Abstract 用 matched sparsity 数字（8.81 vs 10.30, 来自 Appendix），Table 2 中 TEAL uniform 30% 是 10.82。按 Table 2 改进是 18.6%。一级读者验证 Table 2 会发现数字对不上。\n\n**W3** [warning] 缺少 ActTail (arXiv:2603.12272, March 2026)\n- 基于 HT-SR 理论的全局 activation sparsity allocation，与本文 per-layer allocation 分析直接相关。\n\n**W4** [warning] 标题/framing 可能产生效率误导\n- 标题暗示推理效率贡献，但方法增加 6.4% overhead。论文诚实披露但 framing 可能误导匆忙读者。\n\n**W5** [warning] C1 ablation soft-vs-hard confound 未完全解决\n- 二值化 KL logits (>0) 同时改变 target source 和 mask representation。BCE+Gumbel (32.22) vs standard BCE (27.97) 不足以排除 confound（它们用的是 magnitude targets 而非 KL targets）。\n\n### 小问题\n- M1: Intro 中 8.6%/6.4% 未标注 sparsity level（来自 50%，30% 差距小得多）\n- M2: 术语不一致（output-distribution alignment/objective/coupled objective/KL distillation）\n- M3: Table 2 注脚标记过密\n- M4: \"stable downstream (MMLU 40.7±1.3%)\" 相对 dense 65.27% 降 24.5pp，\"stable\" 指跨 seed 稳定性应澄清\n- M5: 页数合规性——Conclusion 可能溢出第 8 页\n- M6: 68% divergence 和 32% Jaccard 同句出现易混淆\n- M7: 14B GSM8K 退步剧增（-1.3pp → -20.1pp）未深入分析\n\n### 主要优势\n1. 系统且诚实的实证框架（5 种 loss, 3 架构, 多 sparsity, 3-seed, OOD, cross-seed consistency）\n2. C1 target-swap ablation 设计巧妙\n3. PPL 改进显著且跨架构一致\n4. Compensation 冗余性发现实用\n5. 写作质量整体高，2D taxonomy 有用\n\n### Questions\nQ1: stop-gradient 实验能否更干净地隔离 coupling scope？\nQ2: Qwen-2.5-14B d_ff=18944 vs LLaMA 14336 的架构差异是否导致 predictor 不匹配？\nQ3: 为何 Abstract 用 Appendix matched-sparsity 数字而非 main table？\nQ4: K=4 50% PPL=44.23 反常的 gradient interference hypothesis 有无进一步实验支持？\n\n### Missing References\n- ActTail (arXiv:2603.12272, March 2026)\n- MaskLLM 应在 Table 1 taxonomy 中体现位置\n\n---\n\n请逐条回应以上所有 Must-Fix、Should-Fix 和主要 Questions。"
  }
}
```

</details>

---


### Tool result

_source line 2095 · 2026-05-23T01:36:12.211789+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1364
}
```

</details>

---


### Assistant

_source line 2096 · 2026-05-23T01:36:15.463346+00:00_

交叉分享已发出。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 180

## Round 180

2 recorded events


### User

_source line 2097 · 2026-05-23T01:36:18.018737+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

总结：

- **Overall: 3.5 (Borderline Conference)**，Confidence 4/5
- **2 个 Must-Fix**：(1) signal type vs coupling scope 分解的 train-inference mismatch confound 在 50% 完全失效，但 Abstract/Conclusion 以不加限定的方式陈述；(2) 知识任务系统退步与"primary design dimension"强 claim 矛盾，Abstract 未量化 decline
- **5 个 Should-Fix**：MaskLLM 在 taxonomy 中缺位、14.5% 基准数字在 Abstract 与 Table 2 不一致、缺少 ActTail 引用、无实际加速但 framing 可能误导、C1 soft-vs-hard confound 未解决
- **7 个 Minor**：术语一致性、页数可能溢出、MMLU"stable"措辞、Qwen-14B GSM8K 退步缺乏分析等

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2098 · 2026-05-23T01:36:22.285410+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 181

## Round 181

2 recorded events


### User

_source line 2099 · 2026-05-23T01:37:54.803653+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 的逐条交叉回应

## Must-Fix

**[AGREE] R1-N1: 知识类任务系统性退化随 scale 恶化，机制分析不充分**

同意。与我的 N2 完全一致。补充证据：Mistral-7B GSM8K 也出现反转（KL 8.6±2.2 vs TEAL 15.9, Table 16），退化跨架构一致。Constraint experiment（Appendix T）最多解释约 65% 的 MMLU 退步（+3.4pp / −5.2pp），剩余归因于 loss function 本身的 mode-covering 特性（Section 4.2 最后一句），无实验支撑。Mixed-domain training 是 rebuttal 中最直接的验证手段。

**[AGREE] R1-N2: Per-layer KL 分解在 50% 下失效**

同意，与我的 N1 高度重叠。额外补充：K=4 MMLU 异常（42.7 > E2E 40.7, Appendix S）不仅是 allocation confound，更暴露 signal type 与 coupling scope 维度的非正交性——K=4 的 near-uniform allocation (std=0.003) 等价于移除 valley pattern（Appendix T: remove-valley → MMLU=44.0）。论文在 Section 4.4 最后一段承认 50% 下分解"unreliable"，但 Abstract 和 Conclusion 中的 claim 无此限定。

**[REBUT] R1-N3: 缺乏实际推理加速，实用贡献为零**

部分反驳。"实用贡献为零"过于绝对。(1) 论文明确自定位为 empirical study（Abstract line 8），贡献在于理解训练目标对 mask quality 的影响；(2) Compensation 冗余性发现（Section 4.4, Appendix J, Table 5）实际减少推理开销从 +9.1% 降至 +6.4% 并节省 67.2M 参数；(3) C1 ablation 证明 KL-derived targets 可迁移到更简单的 BCE predictor（Table 3），这对实际部署有工程价值。但同意应增加与 LaRoSA 等已有加速方法的 mask quality 对比。建议将 N3 从 critical 降级为 warning。

## Should-Fix

**[AGREE] R1-W1**: 3 seeds 统计力不足，MMLU 30% global σ=9.5 使结论可信度极低。论文的处理（PPL 为 primary metric，下游仅作 directional evidence，Section 4.2）是诚实的，但 key comparisons 应增加 seeds。

**[AGREE] R1-W2**: Table 2 条件不统一。BCE 30% 用 global（脚注 †），KL 主报告用 uniform；BCE 50% 用 2700 steps。建议 Table 2 增加条件标注列，或将 BCE 30% uniform (PPL 15.71, Table 4) 纳入正表。

**[AGREE] R1-W3**: C1 soft-vs-hard confound 与我的 W5 一致。BCE+Gumbel (32.22) vs standard BCE (27.97) 不足以排除 confound（两者均用 magnitude targets）。需 soft KL-derived targets → regression 的实验。

**[AGREE] R1-W4**: Qwen-14B 缺 50% 结果，scaling 分析不完整。论文声称 cross-scale evidence 为 contribution（Section 1 bullet 2），但 14B 仅覆盖单一 sparsity level。

**[REBUT] R1-W5**: Forward KL vs RevKL 30% 差距小（0.45pp）恰恰支持论文结论——三种 output-distribution losses（KL/RevKL/JSD）之间差距远小于它们与 BCE (15.71) / MSE (18.52) 的差距（Table 4），说明 output-distribution alignment 是 primary factor。50% 处差距扩大至 +8.6% 符合理论预期（Section 3.4, false negatives cascade under global allocation）。但同意 Introduction 中"8.6%/6.4%"应标注 sparsity level。

## Questions

**Q1**: 合理，论文仅测试推理时 domain shift（Appendix D），未测试训练数据多样性影响。应在 rebuttal 提供。

**Q2**: 极好的实验建议。强制 K=4 使用 E2E 的 non-uniform allocation 可直接验证 allocation vs coupling 的因果关系。论文有 constraint framework（Appendix T）可支持。

**Q3**: 论文未解释。推测：BCE 无 cross-neuron coupling，penalty 强制 sparsity 但 BCE 的 loss 无法指导 global context 下的 neuron 选择，导致 penalty-driven masks 更差。与论文核心论点一致但应明确讨论。

**Q4**: 论文仅报告 LLaMA 的 per-layer distribution（Appendix U）。如果 valley pattern 非通用，cross-architecture claim 需限定。

**Q5**: 本质即 C1 ablation。Table 3 已证明可行（gap ≤1.70pp at 30%）。用 soft regression targets 替代二值化可进一步改进。

## 两位 Reviewer 的共识总结

R1 和 R2 在以下 critical issues 上完全一致：
1. **Signal type/coupling 分解的方法论可靠性**（R1-N2 ≈ R2-N1）：50% 下失效，Abstract/Conclusion 的 claim 需限定
2. **知识任务系统性退步**（R1-N1 ≈ R2-N2）：机制分析不足，"primary design dimension" claim 有误导性
3. **C1 soft-vs-hard confound**（R1-W3 ≈ R2-W5）：未完全解决

唯一分歧在 R1-N3（实际加速缺失）：R1 定性为 critical，R2 认为应降级为 warning——论文的自定位和 compensation 冗余性发现提供了一定实用价值。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2100 · 2026-05-23T01:38:00.289385+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 182

## Round 182

2 recorded events


### User

_source line 2101 · 2026-05-23T01:38:02.878563+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

两位 Reviewer 在三个核心问题上达成共识：(1) signal type/coupling 分解在 50% 下失效但 claim 未限定；(2) 知识任务退步机制分析不足；(3) C1 soft-vs-hard confound 未解决。唯一分歧是实际加速缺失的严重程度——我认为论文作为 empirical study 的自定位和 compensation 冗余性发现使其不应被定性为 critical。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2102 · 2026-05-23T01:38:10.266377+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 183

## Round 183

8 recorded events


### User

_source line 2103 · 2026-05-23T01:39:44.394648+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R2-N1: Signal type vs coupling scope 分解存在不可消除的混淆变量**

同意这是论文的核心弱点之一（与我的 N2 一致）。具体证据：

1. §4.5 脚注明确承认 K=1 的 confound："the K=1 control conflates coupling removal with train-inference mismatch (training 1/32 layers; inference all 32)"。
2. K=4 在 50% 下 PPL=44.23 比 K=1 的 34.85 更差（Table 4），论文自己说"the signal-type/coupling decomposition unreliable under the current design"（§4.5 最后一句）。
3. K=4 在 30% 的 MMLU 异常（42.7±1.4 > E2E 40.7±1.3）被论文归因为 allocation confound（Appendix T），进一步证实两个维度不正交。

但我注意到 Abstract 已加了 qualifier："(upper bound; not fully orthogonal with coupling scope)"，Conclusion 也标注了"upper bound"。问题是这些 qualifiers 是否足够——"accounts for the majority"仍然是一个较强的表述。

**R2 建议的 stop-gradient 实验**（在 KL 反传时对 downstream Jacobian 做 stop-gradient，保留 output-distribution 目标但切断跨层梯度耦合）比 K=1/K=4 设计更干净，我赞同这是一个有建设性的修改方向。不过这需要对训练代码做 non-trivial 的修改，作为 revision 任务的合理性需评估。

---

**[AGREE] R2-N2: 知识任务系统性退步与"primary design dimension"强 claim 矛盾**

同意（与我的 N1 一致）。补充 R2 未详细展开的证据：

1. 退步的**跨 scale 恶化趋势**：8B GSM8K -1.3pp → 14B GSM8K -20.1pp（Table 2 vs Table 13, Appendix K），退步幅度增长 15 倍，这不是噪声可解释的。
2. Abstract 的表述"commonsense gains but knowledge-intensive decline"确实过于轻描淡写——未量化，读者无法从 abstract 判断退步程度。对比：Introduction 第 17 行明确给出了 14B 数字"GSM8K −20.1pp, σ=5.2pp; MMLU −2.8pp"，但 abstract 回避了这些。
3. "primary design dimension"这个 claim 严格来说对 PPL 是成立的（PPL 改善一致、跨架构、3-seed 方差极低）。但论文将此 claim 作为标题级别的主要结论呈现，而在 PPL 之外的维度上方法是 inferior，这构成 overclaim。

R2 建议"限定适用范围并在 Abstract 量化退步幅度"是合理且可操作的。

---

### Should-Fix 问题

**[AGREE] R2-W1: 与 MaskLLM 区分需加强，Table 1 遗漏 MaskLLM**

同意。Table 1（taxonomy, §3.7）的 Static × Coupled 格中仅列 SPON，但 MaskLLM 也属于此格（static N:M masks + KL training）。§2 Related Work 虽然讨论了 MaskLLM 并给出三点区分（static vs contextual, N:M vs unstructured, input-independent vs input-dependent），但这些区分均无实验验证。将 MaskLLM 纳入 Table 1 是一个简单且应该做的修正。

不过我补充一点：MaskLLM 的 setting 差异（static weight masks vs contextual activation masks）确实足够大，不要求在 Table 2 中做 baseline 对比。两者的核心区别在于 MaskLLM 的 mask 不随输入变化，这在 contextual sparsity 场景下是根本性不同。Table 1 加注即可。

---

**[AGREE] R2-W2: 14.5% PPL improvement 的引用基准不一致**

同意，这是一个呈现清晰度问题。

- Abstract 使用 matched-sparsity 对比：8.81 vs 10.30（both at 28.5%），数字来自 Appendix D 和 Figure 2 caption。
- Table 2 中 TEAL uniform 30% = 10.82（名义 30% 稀疏度），按此计算改进是 18.6%。
- Introduction 第 14 行也用 matched-sparsity 数字："reduces TEAL's perplexity by 14.5% at matched sparsity (8.81 vs. 10.30, both at 28.5%)"。

论文选择 matched-sparsity 对比在方法论上是合理的（KL 实际稀疏度 28.5% ≠ 名义 30%，Appendix C Table 9），但 **primary claim 引用 appendix 而非 main table 的数字确实容易让读者困惑**。一级读者查 Table 2 找不到 10.30 这个数字。建议在 Table 2 caption 或正文中明确标注 matched-sparsity 对比的来源。

---

**[REBUT] R2-W3: 缺少 ActTail (arXiv:2603.12272, March 2026)**

我无法验证这篇论文的存在性和内容。arXiv ID 2603.12272 的格式对应 2026 年 3 月，距投稿仅 2 个月。如果这篇论文确实提出了基于 HT-SR 理论的全局 activation sparsity allocation，它与本文的 per-layer allocation 分析（§4.6, Appendix L）相关，应在 Related Work §2 "Training-Free Activation Sparsity" 段落中引用。

但我认为这不应作为 Should-Fix——遗漏一篇 2 个月前的 arXiv 预印本（非 peer-reviewed）不构成重大缺陷。降为 Minor 更合适。

---

**[AGREE] R2-W4: 标题/framing 可能产生效率误导**

部分同意。标题"Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs"本身不直接承诺效率，但"Sparsity Prediction"在 LLM 语境下强烈暗示推理加速。论文在 Introduction 最后一段和 Appendix A 中诚实地披露了 +6.4% overhead（这一点我在自己的审稿中也肯定了），但标题和 abstract 确实可能误导快速浏览的读者。

不过，我认为这更接近 framing 调整而非 substantive 问题。论文的核心贡献是 analytical（理解训练目标如何影响稀疏预测质量），而非 practical efficiency。如果论文更明确地在 abstract 开头就定位为 analytical study（类似 Introduction 第 18 行"This paper is primarily an empirical study..."），这个 concern 就会消解。

---

**[AGREE] R2-W5: C1 ablation soft-vs-hard confound 未完全解决**

同意（与我的 W3 一致）。R2 正确指出 BCE+Gumbel (32.22) vs standard BCE (27.97) 的对比使用的是 **magnitude targets**，而非 KL targets。这意味着该控制实验测试的是"softness 对 magnitude-based masks 有无帮助"，而非"softness 对 KL-derived masks 有无帮助"。要完整控制 soft-vs-hard confound，需要的是：BCE+Gumbel **on KL-derived targets** vs BCE hard **on KL-derived targets**。

但我补充：C1 的核心 claim 是"KL-discovered mask patterns transfer to simpler training"（§4.4），而非"training objective doesn't matter"。即使存在 soft-vs-hard confound，C1 的 ≤0.79pp gap（Table 3, 50% s42）已经建立了 mask pattern transferability 的强证据。confound 影响的是对 *why* transfer works 的解释，而非 transfer *whether* works 的结论。

---

### 小问题

**[AGREE] R2-M1: §3.4 中 8.6%/6.4% 未标注 sparsity level**

同意。§3.4 第 81 行："forward KL outperforms reverse KL by 8.6% and JSD by 6.4% (Table 4)"——这些数字来自 Table 4 的 50% 列（11.79 vs 12.80=8.6%, 11.79 vs 12.54=6.4%）。在 30%，Forward KL vs JSD 差距仅 1.0%（8.81 vs 8.90），vs RKL 仅 5.1%（8.81 vs 9.26）。不标注 sparsity level 会让读者高估 forward KL 在 moderate sparsity 下的优势。

小修正：R2 定位为"Intro 中"，实际出现在 §3.4 Method 中。但实质性观点正确。

---

**[AGREE] R2-M2: 术语不一致**

同意。论文交替使用 output-distribution alignment / output-distribution objective / coupled objective / KL distillation / end-to-end KL 指代同一概念，增加了阅读认知负担。建议统一为 "output-distribution KL" 或 "end-to-end KL distillation"。

---

**[AGREE] R2-M3: Table 2 注脚标记过密**

同意。Table 2 有 †, ‡, ±, * 四种标注加上 caption 中大量说明文字，视觉负担重。但信息本身是必要的——问题在于呈现方式而非内容。

---

**[AGREE] R2-M4: "stable downstream" 用词模糊**

同意。Introduction 第 14 行"stable downstream (MMLU 40.7±1.3%)"——MMLU 相对 dense 65.27% 下降了 24.5pp，这里的"stable"指跨 seed 稳定性（σ=1.3），不是指性能保持。应改为"reproducible across seeds"或"low cross-seed variance"以避免误读。

---

**[REBUT] R2-M5: 页数合规性——Conclusion 可能溢出第 8 页**

查看 PDF：第 8 页底部是 §5 Conclusion 的开头，第 9 页顶部有 Conclusion 最后 1-2 行溢出，随后是 Limitations。按 EMNLP 2026 规则，main text（含 Conclusion）限 8 页，Limitations 不计入。如果 Conclusion 确实溢出到第 9 页，这是**格式违规**，需要修复。

但我将此定级为 Minor 而非 Should-Fix——这是一个通过微调排版即可修复的问题（压缩 Table 2 间距或缩短 Conclusion 即可）。不影响内容评判。

实际上仔细看 PDF 第 8 页，Conclusion 部分占了大约 6 行正文，第 9 页顶部可能有约 1-2 行溢出。这确实是违规的，但属于 camera-ready 级别的修复。R2 的 concern 有效，但不改变评分。

---

**[AGREE] R2-M6: 68% divergence 和 32% Jaccard 同句出现易混淆**

同意。Introduction 第 10 行："patterns that diverge 68% from magnitude-based masks (per-layer Jaccard 32%)"——68% = Jaccard distance, 32% = Jaccard similarity = 1 - 0.68。同一句用两种互补度量确实造成混淆。建议统一使用 Jaccard distance 或明确注明"Jaccard similarity 32% (distance 68%)"。

---

**[AGREE] R2-M7: 14B GSM8K 退步剧增未深入分析**

同意（与我的 W4 一致）。§4.6 对 14B 退步的讨论仅一句："suggests a systematic property of distribution-matching"。8B→14B GSM8K 退步从 -1.3pp 飙升到 -20.1pp，这个 15 倍的恶化缺乏任何机制分析。可能的因素包括：(1) 14B 的 d_ff=18944（vs 8B 的 14336）导致 predictor 瓶颈 d_b=128 的压缩比更大；(2) 14B 上数学推理能力更强，被稀疏化破坏的绝对量更大。论文应至少讨论这些可能性。

---

### Questions 回应

**R2-Q1 (stop-gradient 实验)**: 同意这是一个比 K=1/K=4 更干净的隔离方案。具体实现：在 KL loss 反传时，对 $\partial \mathbf{z}_{\text{sparse}} / \partial \tilde{m}_j^{(\ell)}$ 中来自 $\ell' > \ell$ 层的梯度做 detach，保留本层 mask→output 的梯度路径但切断跨层耦合。这保持了 output-distribution 目标（signal type 不变）同时移除 coupling。

**R2-Q2 (Qwen d_ff=18944 vs LLaMA 14336)**: 这是一个有效的 concern。Predictor 结构 Linear(4096→128→d_ff) 中，d_ff=18944 时第二层参数量增加 32%（128×18944=2.42M vs 128×14336=1.84M per layer）。论文 Appendix K 的 Table 13 caption 没有说明是否调整了 d_b。如果使用相同的 d_b=128，压缩比从 4096:128:14336 变为 5120:128:18944（假设 Qwen 的 d_model=5120），bottleneck 压力更大。这可能部分解释 14B 上的退化。

**R2-Q3 (Abstract 用 Appendix 数字)**: 同意 R2 的 concern，如我在 W2 回应中所述。

**R2-Q4 (K=4 50% gradient interference hypothesis)**: 论文没有提供任何实验支持（我在自己的 N2 中也指出了这一点）。这是一个纯粹假设性的解释。要验证需要：(1) 在训练过程中测量 K=4 vs E2E 的 layer-wise gradient conflict（例如 cosine similarity between layer groups 的梯度），(2) 尝试 K=8, K=16 看是否有单调趋势。

---

### 总结

R2 与我的审稿在核心问题上高度一致：**per-layer KL 分解的 confound（R2-N1 ≈ 我的 N2）**和**知识任务退步（R2-N2 ≈ 我的 N1）**是两个最重要的 Must-Fix。R2 额外指出的 **baseline 引用不一致（W2）**和 **MaskLLM taxonomy 遗漏（W1）**是合理的 Should-Fix。我对 R2 的 W3（ActTail 引用）持保留意见——2 个月前的 arXiv 预印本不应作为 Should-Fix。

两份审稿的核心分歧不大，但侧重点不同：我更强调缺乏实际加速（我的 N3），R2 更关注分解框架的 claim 强度和呈现一致性。综合来看，论文需要：(1) 弱化 signal type/coupling decomposition 的 claim 强度，(2) 量化知识任务退步并限定方法适用范围，(3) 修复 baseline 引用和 taxonomy 遗漏。如果这些修改完成，Findings 级别接收是合理的。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2104 · 2026-05-23T01:40:05.813665+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 2105 · 2026-05-23T01:40:05.865319+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T01:28:00.173590+00:00\", \"completed_at\": \"2026-05-23T01:31:41.570892+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点（纯 Abstract + Intro 文本）。第一个 display item（Figure 1 方法概览图）出现在 page 2 右栏。对于 ACL 双栏格式这很常见，但如果能将 Figure 1 提前到 page 1（如用 figure* 跨栏置于页顶），可显著增强审稿人第一印象。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1（方法概览图）为单栏宽度，架构图内部文字偏小（接近可读下限）。该图是论文核心 message 的视觉锚点，建议考虑 figure* 全宽版本以提升清晰度。当前尺寸下文字仍可辨认，不构成阻碍。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 caption 自包含性良好——说明了方法概览、KL divergence 与 Gumbel-Sigmoid relaxation 的作用，审稿人不看正文也能理解核心 idea。\"}, {\"severity\": \"info\", \"dimension\": \"pages 3-4\", \"message\": \"Page 3 为纯文本（Related Work 尾段），page 4 为方法公式推导（4 个 display equations）。公式密集段属于合理例外，但 page 3 整页纯文本在视觉上略显单调。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1（方法分类 taxonomy）使用 booktabs 风格，结构清晰。空单元格在 caption 中明确标注为 \\\"unexplored combinations\\\"，处理得当。\"}, {\"severity\": \"warning\", \"dimension\": \"page 6\", \"message\": \"实验设置（Section 4.1-4.2 开头）整页纯文字，无任何 display item。位于 Table 1（page 5）和 Tables 2-3（page 7）之间，视觉节奏中断。建议：将部分实验设置信息整合为简表，或调整 float 位置使 Table 2 提前。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 2（主结果表）和 Table 3（target-swap ablation）同页堆叠，页面以表格为主（>60% 面积）。两表均使用 booktabs 风格，最优结果加粗，小数精度一致。Table 2 字号偏小但仍可读。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Table 4（ablation）+ Figure 2（sparsity scaling 折线图）+ Conclusion 三元素在同一页，布局紧凑但不拥挤，视觉节奏好。Figure 2 轴标签清晰，使用不同 marker + line style 区分方法，色盲友好。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Section 5 Conclusion 在 page 8 底部开始，未出现 heading 孤悬——heading 下方有至少 4-5 行正文，排版合理。\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 段简洁（~3 个要点），Ethics Statement 简短，References 在同页下半部分开始。符合 EM
…[truncated 1616 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2106 · 2026-05-23T01:43:10.446404+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 26 (Fresh Review) — Active issues\n  # ============================================================\n\n  - id: \"R20-W1\"\n    summary: \"Per-layer KL decomposition 的 train-inference mismatch confound 未解决\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 26\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Critical。K=4 single-seed。\"}\n      - {round: 22, reviewers: [1, 2], note: \"R22 N2。97.5% 精确数字不可靠。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 C1。K=1 有 32× train-inference mismatch；K=4 在 50% 反常差于 K=1；仅两个 K 值不足支撑分解。\"}\n      - {round: 25, reviewers: [1, 2], note: \"R25 N1/N2。K=4 at 50% 反常仍仅 speculation。MMLU K=4 > E2E anomaly 暴露 allocation confound。\"}\n      - {round: 26, reviewers: [1, 2], note: \"R26 R1-N2/R2-N1 完全共识。核心问题不变：(1) K=1 同时改变 coupling 和 train-inference mismatch (1/32 vs 32/32)；(2) K=4 在 50% PPL=44.23 > K=1 34.85，论文自承 unreliable；(3) K=4 MMLU anomaly (42.7>40.7) 暴露 allocation confound (near-uniform std=0.003 ≈ remove-valley)。Abstract 已加 'upper bound; not fully orthogonal' qualifier 但 'accounts for the majority' 仍为较强表述。两位 reviewer 建议 stop-gradient 实验或增加更多 K 值。\"}\n    action_items:\n      - {round: 21, action: \"K=4 3-seed (s42/s123/s456)\", assigned_to: \"main_agent\", status: done}\n      - {round: 22, action: \"97.5% → 定性 'majority of PPL gap'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 22, action: \"K=4 50% s42 PPL-only 实验\", assigned_to: \"main_agent\", status: done}\n      - {round: 24, action: \"Abstract/Conclusion 删除精确百分比改为定性\", assigned_to: \"paper_agent\", status: done}\n      - {round: 24, action: \"K=4 50% 反常结果补假设性解释\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"限定 decomposition 结论适用范围为 moderate sparsity (30%)\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"正文 §4.5 明确讨论 allocation confound\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"考虑 K=2/K=8/K=16 实验或限制 decomposition 仅 30% 有效\", assigned_to: \"main_agent\", status: open}\n      - {round: 26, action: \"设计 stop-gradient 实验：KL loss 反传时 detach downstream Jacobian 的跨层梯度，保留 output-distribution 目标但切断 coupling\", assigned_to: \"main_agent\", status: open}\n      - {round: 26, action: \"Abstract 中 'accounts for the majority' 进一步弱化或加条件限定\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-N2\"\n    summary: \"MMLU/GSM8K 跨架构系统性退步缺乏机制分析\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 18\n    last_seen_round: 26\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Critical。Protection valley 分析仅 correlational。\"}\n      - {round: 22, reviewers: [1, 2], note: \"R22 N3。要求追踪 Remove Valley + task-aware allocation。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 C2。Remove valley 方向正确但不够。8B MMLU -5.2pp, 14B GSM8K -20pp。\"}\n      - {round: 25, reviewers: [1, 2], note: \"R25 最高优先级。两个假设仍仅 speculation。\"}\n      - {round: 26, reviewers: [1, 2], note: \"R26 R1-N1/R2-N2 完全共识。问题未改善：(1) 退步跨架构一致（Mistral GSM8K 8.6 vs TEAL 15.9）；(2) 跨 scale 恶化 15 倍（8B GSM8K -1.3pp → 14B -20.1pp）；(3) Constraint experiment 最多解释 ~65% MMLU 退步 (+3.4/5.2)，剩余归因于 mode-covering 无实验验证；(4) Abstract 未量化退步幅度；(5) 'primary design dimension' claim 仅对 PPL+commonsense 成立，对知识任务是 inferior。两位 reviewer 建议 mixed-domain training 或 knowledge neuron probe。\"}\n    action_items:\n      - {round: 21, action: \"Constraint 实验\", assigned_to: \"main_agent\", status: done}\n      - {round: 22, action: \"§4.2 深化\", assigned_to: \"paper_agent\", status: done}\n      - {round: 24, action: \"§4.2 补机制假设段\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"Appendix T 结论提升到正文\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"C4 控制实验验证数据偏差假设\", assigned_to: \"main_agent\", status: wont_fix}\n      - {round: 26, action: \"Abstract 量化知识任务退步幅度（至少包含 MMLU -5.2pp 或 GSM8K decline）\", assigned_to: \"paper_agent\", status: open}\n      - {round: 26, action: \"'primary design dimension' 限定为 'for PPL and commonsense tasks at moderate sparsity'\", assigned_to: \"paper_agent\", status: open}\n      - {round: 26, action: \"Mixed-domain training（WikiText + 数学/代码数据）验证数据偏差假设\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R25-N1\"\n    summary: \"方法新颖性边界需更清晰论证\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - {round: 25, reviewers: [2], note: \"核心组件均成熟技术。MaskLLM 已用 KL+Gumbel 训练 mask。\"}\n      - {round: 26, reviewers: [2], note: \"R26 R2 Excitement 2.5/5。MaskLLM 共享核心 recipe (frozen weights + learnable masks + KL + Gumbel)。三点区分合理但无实验验证。Table 1 Static×Coupled 仅列 SPON 应纳入 MaskLLM。R1 交叉同意 Table 1 修正但认为 setting 差异足够大不需 Table 2 baseline 对比。\"}\n    action_items:\n      - {round: 25, action: \"Intro contribution list 重排\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"Intro 更早承认组件非新颖性\", assigned_to: \"paper_agent\", status: done}\n      - {round: 26, action: \"Table 1 Static×Coupled 格加入 MaskLLM\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W2\"\n    summary: \"高方差下游指标统计可靠性不足\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 24\n    last_seen_round: 26\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"ARC-c 95% CI ≈ ±8.9pp，差异不显著。PPL primary metric 方差极低。\"}\n      - {round: 25, reviewers: [1, 2], note: \"Qwen-14B GSM8K std=5.2pp (CV=16.3%)。\"}\n      - {round: 26, reviewers: [1, 2], note: \"R26 R1-W1/R2 共识。MMLU 30% global σ=9.5 (95% CI ≈ ±23.5pp)。论文正确将 PPL 作为 primary metric 且下游仅作 directional evidence，但 abstract/conclusion 中的下游 claims 应进一步弱化。\"}\n    action_items:\n      - {round: 24, action: \"正文对高方差指标加 CI overlap caveat\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"§4.6 引用 Qwen-14B GSM8K 时使用完整 mean±std\", assigned_to: \"paper_agent\", status: open}\n      - {round: 26, action: \"在有方差报告的指标上考虑增加 paired t-test 或 bootstrap p-value\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W3\"\n    summary: \"C1 ablation soft→hard mask representation 残余 confound\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 24\n    last_seen_round: 26\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"Oracle 二值化丢失排序信息。定性结论稳健。\"}\n      - {round: 25, reviewers: [1, 2], note: \"s42 oracle 来自 earlier checkpoint。\"}\n      - {round: 26, reviewers: [1, 2], note: \"R26 R1-W3/R2-W5 共识。BCE+Gumbel (32.22) vs BCE (27.97) 用 magnitude targets 不足以排除 confound。需 BCE+Gumbel on KL-derived targets vs BCE hard on KL-derived targets。R1 补充：confound 影响对 why transfer works 的解释，不影响 whether transfer works 的结论（≤0.79pp gap 已建立 transferability 证据）。\"}\n    action_items:\n      - {round: 24, action: \"讨论 oracle 信息损失可能性\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"正文添加 binarization confound caveat\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"s42 补训 matched oracle 或优先展示 s123/s456\", assigned_to: \"paper_agent\", status: open}\n      - {round: 26, action: \"增加 BCE+Gumbel on KL-derived targets 实验以隔离 softness confound\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R25-W1\"\n    summary: \"BCE 30% 缺少 uniform allocation 对比，Table 2 比较不对称\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - {round: 25, reviewers: [1, 2], note: \"Table 2 中 BCE 30% 仅有 global。\"}\n      - {round: 26, reviewers: [1, 2], note: \"R26 R1-W2 再次确认。BCE 30% 用 global (†)，KL 有 global+uniform。BCE 50% 用 2700 steps (2.71× KL budget)。建议统一 allocation 或增加 controlled comparison 子表。R2 交叉同意。\"}\n    action_items:\n      - {round: 25, action: \"补充 BCE 30% uniform 数据或解释缺失\", assigned_to: \"paper_agent\", status: open}\n      - {round: 26, action: \"Table 2 增加条件标注列或将 BCE 30% uniform PPL=15.71 (Table 4) 纳入正表\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R26-W1\"\n    summary: \"14.5% PPL improvement 引用基准在 Abstract 与 Table 2 不一致\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 26\n    mentions:\n      - {round: 26, reviewers: [1, 2], note: \"R2-W2，R1 交叉同意。Abstract 用 matched-sparsity (8.81 vs 10.30, Appendix D)，但 Table 2 TEAL uniform 30%=10.82（改进 18.6%）。一级读者查 Table 2 找不到 10.30。方法论上 matched-sparsity 合理但呈现方式导致困惑。\"}\n    action_items:\n      - {round: 26, action: \"在 Table 2 caption 或正文中标注 matched-sparsity 对比来源，或在 Table 2 增加 matched-sparsity 行\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R25-W3\"\n    summary: \"Introduction '19%' PPL 减少已修正为 14.5% matched-sparsity\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - {round: 25, reviewers: [1, 2], note: \"19% 计算不符。\"}\n      - {round: 26, reviewers: [1, 2], note: \"R26 论文已使用 14.5% matched-sparsity 数字，数值本身正确。但引用基准问题升级为独立 issue R26-W1。\"}\n    resolution: \"数值已修正为 14.5% matched-sparsity。基准一致性问题转入 R26-W1。\"\n    resolution_round: 26\n\n  - id: \"R25-M1\"\n    summary: \"术语不一致：output-distribution alignment/distillation/objective 交替使用\"\n    category: writing\n    severity: minor\n    status: open\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - {round: 25, reviewers: [2], note: \"全文交替使用多种术语。\"}\n      - {round: 26, reviewers: [1, 2], note: \"R26 R2-M2 再次提出，R1 交叉同意。建议统一为 'output-distribution KL' 或 'end-to-end KL distillation'。\"}\n    action_items:\n      - {round: 25, action: \"全文统一术语\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R26-M1\"\n    summary: \"Introduction 中 8.6%/6.4% 未标注 sparsity level\"\n    category: writing\n    severity: minor\n    status: open\n    first_raised_round: 26\n    last_seen_round: 26\n    mentions:\n      - {round: 26, reviewers: [1, 2], note: \"R2-M1，R1 交叉同意。§3.4 line 81 数字来自 50% (Table 4)，30% 差距小得多 (KL vs JSD 仅 1.0%)。不标注 sparsity level 会高估 forward KL 在 moderate sparsity 下的优势。\"}\n    action_items:\n      - {round: 26, action: \"§3.4 标注 '(at 50% sparsity)'\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R26-M2\"\n    summary: \"'stable downstream' 措辞指跨 seed 稳定性但易误读为性能保持\"\n    category: writing\n    severity: minor\n    status: open\n    first_raised_round: 26\n    last_seen_round: 26\n    mentions:\n      - {round: 26, reviewers: [1, 2], note: \"R2-M4，R1 同意。'MMLU 40.7±1.3%' 相对 dense 65.27% 降 24.5pp，'stable' 指跨 seed 而非绝对性能。应改为 'reproducible across seeds' 或 'low cross-seed variance'。\"}\n    action_items:\n      - {round: 26, action: \"Introduction 中 'stable downstream' → 'low cross-seed variance' 或 'reproducible'\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R26-M3\"\n    summary: \"68% divergence 和 32% Jaccard 同句出现易混淆\"\n    category: writing\n    severity: minor\n    status: open\n    first_raised_round: 26\n    last_seen_round: 26\n    mentions:\n      - {round: 26, reviewers: [1, 2], note: \"R2-M6，R1 同意。Introduction 同句用互补度量（Jaccard distance 68% = 1 - similarity 32%）造成混淆。建议统一。\"}\n    action_items:\n      - {round: 26, action: \"Introduction 统一使用 Jaccard distance 或明确标注\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 26 — 无实际加速 (Reviewer 分歧项)\n  # ============================================================\n\n  - id: \"R19-N3\"\n    summary: \"无实际 wall-clock 加速: +6.4% overhead, unstructured masks 无 speedup\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 26\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Critical。Intro framing 已修改为 empirical study。\"}\n      - {round: 22, reviewers: [1, 2], note: \"降为 Warning。论文已定位为 analysis work。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 W1。仍为 Warning。\"}\n      - {round: 25, reviewers: [1, 2], note: \"R25 Should-Fix。论文诚实披露。\"}\n      - {round: 26, reviewers: [1, 2], note: \"R26 唯一分歧点。R1 定为 critical (N3)，R2 rebut 降为 warning——论文自定位 empirical study，compensation 冗余性发现减少推理开销并节省 67.2M 参数，C1 证明 KL targets 可迁移到 BCE 有工程价值。Director 裁定：降为 warning，论文 framing 已充分。\"}\n    action_items:\n      - {round: 21, action: \"Abstract 加 empirical study + §1 disclaimer\", assigned_to: \"paper_agent\", status: done}\n      - {round: 22, action: \"§1 加 speedup 条件 + 6.4% overhead\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"结构性限制。论文已充分 framed 为 empirical study。R26 R1 升级为 critical 但 R2 rebut 有效，维持 warning。\"\n    resolution_round: 23\n\n  # ============================================================\n  # Round 26 — Resolved / Carried forward\n  # ============================================================\n\n  - id: \"R24-W1\"\n    summary: \"评估覆盖度关键空白：无生成任务、固定 seq_len=2048、无 batched inference\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 26\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"无 MT-Bench 等生成任务。\"}\n      - {round: 25, reviewers: [2], note: \"Base model 不适用 MT-Bench (需 instruction-tuned)。\"}\n      - {round: 26, reviewers: [], note: \"R26 未单独提出。Limitations 已覆盖。\"}\n    resolution: \"Limitations 已覆盖。Base model 不适用生成评估。\"\n    resolution_round: 25\n\n  - id: \"R24-W4\"\n    summary: \"'Primary design dimension' 声明需资格限定\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 26\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"建议软化为 'substantially outperforms'。\"}\n      - {round: 25, reviewers: [1, 2], note: \"已改为 'primary design dimension'，限定 30%。\"}\n      - {round: 26, reviewers: [1, 2], note: \"R26 与 R20-N2 重叠。'primary design dimension' 需进一步限定为 PPL+commonsense 而非 general。追踪合并入 R20-N2。\"}\n    resolution: \"追踪合并入 R20-N2。\"\n    resolution_round: 26\n\n  - id: \"R25-W2\"\n    summary: \"MSE 50% baseline 仅 seed 42 有效\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - {round: 25, reviewers: [1, 2], note: \"MSE 50% s123 catastrophic PPL=15789。\"}\n      - {round: 26, reviewers: [1, 2], note: \"R26 R1-W2 提及。Table 4 MSE 50% 标注 § 但正文 §3.7 使用时未注 single-seed caveat。\"}\n    action_items:\n      - {round: 25, action: \"正文使用 MSE 50% 时注明 single-seed caveat\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W6\"\n    summary: \"Figure 2 仅展示 global allocation 但推荐 uniform\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 26\n    mentions:\n      - {round: 22, reviewers: [1, 2], note: \"正文 Figure 之一，framing 效果强。\"}\n      - {round: 26, reviewers: [], note: \"R26 未单独提出。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R25-M2\"\n    summary: \"Eq. 4 s_j 缺少层标 ℓ 上标\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 25\n    last_seen_round: 25\n    resolution: \"Eq. 4 已补充 ℓ 上标。\"\n    resolution_round: 25\n\n  - id: \"R19-W1\"\n    summary: \"与 MaskLLM 新颖性区分\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 26\n    mentions:\n      - {round: 26, reviewers: [1, 2], note: \"R26 合并进 R25-N1。MaskLLM 三点区分已落地，Table 1 遗漏作为 R25-N1 子项追踪。\"}\n    resolution: \"合并进 R25-N1。\"\n    resolution_round: 25\n\n  - id: \"R20-W4\"\n    summary: \"WikiText 同分布评估 + C4 OOD variance\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 26\n    mentions:\n      - {round: 26, reviewers: [], note: \"R26 未提出。Appendix D OOD 证据充分。\"}\n    resolution: \"Appendix D OOD 证据充分。\"\n    resolution_round: 25\n\n  - id: \"R22-W3\"\n    summary: \"Table 2 actual sparsity mismatch ‡ 脚注不够显著\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 26\n    mentions:\n      - {round: 26, reviewers: [1], note: \"R1 minor：Lagrangian 在 30% 饱和 λ=5000 导致 actual 28.5%。Appendix C 有 matched 对比。\"}\n    resolution: \"§4.1 matched 14.5% 独立句。‡ 脚注存在。\"\n    resolution_round: 23\n\n  - id: \"R22-W5\"\n    summary: \"规模泛化仅 7-14B\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 26\n    mentions:\n      - {round: 26, reviewers: [1, 2], note: \"R26 与 R20-N2 M7 重叠。14B GSM8K -20pp 恶化的机制分析不足。Limitations 已含 'evaluation bounded at 7-14B'。\"}\n    resolution: \"Limitations 已包含 scale limitation 讨论。\"\n    resolution_round: 25\n\n  - id: \"R19-N2\"\n    summary: \"C1 target-swap ablation 因果声明\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 24\n    resolution: \"C1 claim 已降级为 transferability。\"\n    resolution_round: 23\n\n  - id: \"R22-W7\"\n    summary: \"Abstract 第5句信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"已拆分。\"\n    resolution_round: 23\n\n  - id: \"R22-W8\"\n    summary: \"Conclusion 引用 BoolQ (高 variance, 仅 Appendix)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"BoolQ → HellaSwag/PIQA。\"\n    resolution_round: 23\n\n  - id: \"R19-W7\"\n    summary: \"30% sparsity sweet spot 限制实际影响\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 26\n    resolution: \"Limitations 已覆盖。连续多轮未被 reviewer 提出。\"\n    resolution_round: 25\n\n  - id: \"R15-N3\"\n    summary: \"MaskLLM 新颖性边界\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 26\n    resolution: \"§2 三点本质差异。合并进 R25-N1。\"\n    resolution_round: 23"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 26 (Fresh Review) — Active issues\n  # ============================================================\n\n  - id: \"R20-W1\"\n    summary: \"Per-layer KL decomposition 的 train-inference mismatch confound 未解决\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 26\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Critical。K=4 single-seed。\"}\n      - {round: 22, reviewers: [1, 2], note: \"R22 N2。97.5% 精确数字不可靠。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 C1。K=1 有 32× train-inference mismatch；K=4 在 50% 反常差于 K=1；仅两个 K 值不足支撑分解。\"}\n      - {round: 25, reviewers: [1, 2], note: \"R25 N1/N2。K=4 at 50% 反常仍仅 speculation。MMLU K=4 > E2E anomaly 暴露 allocation confound。\"}\n      - {round: 26, reviewers: [1, 2], note: \"R26 R1-N2/R2-N1 完全共识。核心问题不变：(1) K=1 同时改变 coupling 和 train-inference mismatch (1/32 vs 32/32)；(2) K=4 在 50% PPL=44.23 > K=1 34.85，论文自承 unreliable；(3) K=4 MMLU anomaly (42.7>40.7) 暴露 allocation confound (near-uniform std=0.003 ≈ remove-valley)。Abstract 已加 'upper bound; not fully orthogonal' qualifier 但 'accounts for the majority' 仍为较强表述。两位 reviewer 建议 stop-gradient 实验或增加更多 K 值。\"}\n    action_items:\n      - {round: 21, action: \"K=4 3-seed (s42/s123/s456)\", assigned_to: \"main_agent\", status: done}\n      - {round: 22, action: \"97.5% → 定性 'majority of PPL gap'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 22, action: \"K=4 50% s42 PPL-only 实验\", assigned_to: \"main_agent\", status: done}\n      - {round: 24, action: \"Abstract/Conclusion 删除精确百分比改为定性\", assigned_to: \"paper_agent\", status: done}\n      - {round: 24, action: \"K=4 50% 反常结果补假设性解释\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"限定 decomposition 结论适用范围为 moderate sparsity (30%)\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"正文 §4.5 明确讨论 allocation confound\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"考虑 K=2/K=8/K=16 实验或限制 decomposition 仅 30% 有效\", assigned_to: \"main_agent\", status: open}\n      - {round: 26, action: \"设计 stop-gradient 实验：KL loss 反传时 detach downstream Jacobian 的跨层梯度，保留 output-distribution 目标但切断 coupling\", assigned_to: \"main_agent\", status: open}\n      - {round: 26, action: \"Abstract 中 'accounts for the majority' 进一步弱化或加条件限定\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-N2\"\n    summary: \"MMLU/GSM8K 跨架构系统性退步缺乏机制分析\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 18\n    last_seen_round: 26\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Critical。Protection valley 分析仅 correlational。\"}\n      - {round: 22, reviewers: [1, 2], note: \"R22 N3。要求追踪 Remove Valley + task-aware allocation。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 C2。Remove valley 方向正确但不够。8B MMLU -5.2pp, 14B GSM8K -20pp。\"}\n      - {round: 25, reviewers: [1, 2], note: \"R25 最高优先级。两个假设仍仅 speculation。\"}\n      - {round: 26, reviewers: [1, 2], note: \"R26 R1-N1/R2-N2 完全共识。问题未改善：(1) 退步跨架构一致（Mistral GSM8K 8.6 vs TEAL 15.9）；(2) 跨 scale 恶化 15 倍（8B GSM8K -1.3pp → 14B -20.1pp）；(3) Constraint experiment 最多解释 ~65% MMLU 退步 (+3.4/5.2)，剩余归因于 mode-covering 无实验验证；(4) Abstract 未量化退步幅度；(5) 'primary design dimension' claim 仅对 PPL+commonsense 成立，对知识任务是 inferior。两位 reviewer 建议 mixed-domain training 或 knowledge neuron probe。\"}\n    action_items:\n      - {round: 21, action: \"Constraint 实验\", assigned_to: \"main_agent\", status: done}\n      - {round: 22, action: \"§4.2 深化\", assigned_to: \"paper_agent\", status: done}\n      - {round: 24, action: \"§4.2 补机制假设段\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"Appendix T 结论提升到正文\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"C4 控制实验验证数据偏差假设\", assigned_to: \"main_agent\", status: wont_fix}\n      - {round: 26, action: \"Abstract 量化知识任务退步幅度（至少包含 MMLU -5.2pp 或 GSM8K decline）\", assigned_to: \"paper_agent\", status: open}\n      - {round: 26, action: \"'primary design dimension' 限定为 'for PPL and commonsense tasks at moderate sparsity'\", assigned_to: \"paper_agent\", status: open}\n      - {round: 26, action: \"Mixed-domain training（WikiText + 数学/代码数据）验证数据偏差假设\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R25-N1\"\n    summary: \"方法新颖性边界需更清晰论证\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - {round: 25, reviewers: [2], note: \"核心组件均成熟技术。MaskLLM 已用 KL+Gumbel 训练 mask。\"}\n      - {round: 26, reviewers: [2], note: \"R26 R2 Excitement 2.5/5。MaskLLM 共享核心 recipe (frozen weights + learnable masks + KL + Gumbel)。三点区分合理但无实验验证。Table 1 Static×Coupled 仅列 SPON 应纳入 MaskLLM。R1 交叉同意 Table 1 修正但认为 setting 差异足够大不需 Table 2 baseline 对比。\"}\n    action_items:\n      - {round: 25, action: \"Intro contribution list 重排\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"Intro 更早承认组件非新颖性\", assigned_to: \"paper_agent\", status: done}\n      - {round: 26, action: \"Table 1 Static×Coupled 格加入 MaskLLM\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W2\"\n    summary: \"高方差下游指标统计可靠性不足\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 24\n    last_seen_round: 26\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"ARC-c 95% CI ≈ ±8.9pp，差异不显著。PPL primary metric 方差极低。\"}\n      - {round: 25, reviewers: [1, 2], note: \"Qwen-14B GSM8K std=5.2pp (CV=16.3%)。\"}\n      - {round: 26, reviewers: [1, 2], note: \"R26 R1-W1/R2 共识。MMLU 30% global σ=9.5 (95% CI ≈ ±23.5pp)。论文正确将 PPL 作为 primary metric 且下游仅作 directional evidence，但 abstract/conclusion 中的下游 claims 应进一步弱化。\"}\n    action_items:\n      - {round: 24, action: \"正文对高方差指标加 CI overlap caveat\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"§4.6 引用 Qwen-14B GSM8K 时使用完整 mean±std\", assigned_to: \"paper_agent\", status: open}\n      - {round: 26, action: \"在有方差报告的指标上考虑增加 paired t-test 或 bootstrap p-value\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W3\"\n    summary: \"C1 ablation soft→hard mask representation 残余 confound\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 24\n    last_seen_round: 26\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"Oracle 二值化丢失排序信息。定性结论稳健。\"}\n      - {round: 25, reviewers: [1, 2], note: \"s42 oracle 来自 earlier checkpoint。\"}\n      - {round: 26, reviewers: [1, 2], note: \"R26 R1-W3/R2-W5 共识。BCE+Gumbel (32.22) vs BCE (27.97) 用 magnitude targets 不足以排除 confound。需 BCE+Gumbel on KL-derived targets vs BCE hard on KL-derived targets。R1 补充：confound 影响对 why transfer works 的解释，不影响 whether transfer works 的结论（≤0.79pp gap 已建立 transferability 证据）。\"}\n    action_items:\n      - {round: 24, action: \"讨论 oracle 信息损失可能性\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"正文添加 binarization confound caveat\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"s42 补训 matched oracle 或优先展示 s123/s456\", assigned_to: \"paper_agent\", status: open}\n      - {round: 26, action: \"增加 BCE+Gumbel on KL-derived targets 实验以隔离 softness confound\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R25-W1\"\n    summary: \"BCE 30% 缺少 uniform allocation 对比，Table 2 比较不对称\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - {round: 25, reviewers: [1, 2], note: \"Table 2 中 BCE 30% 仅有 global。\"}\n      - {round: 26, reviewers: [1, 2], note: \"R26 R1-W2 再次确认。BCE 30% 用 global (†)，KL 有 global+uniform。BCE 50% 用 2700 steps (2.71× KL budget)。建议统一 allocation 或增加 controlled comparison 子表。R2 交叉同意。\"}\n    action_items:\n      - {round: 25, action: \"补充 BCE 30% uniform 数据或解释缺失\", assigned_to: \"paper_agent\", status: open}\n      - {round: 26, action: \"Table 2 增加条件标注列或将 BCE 30% uniform PPL=15.71 (Table 4) 纳入正表\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R26-W1\"\n    summary: \"14.5% PPL improvement 引用基准在 Abstract 与 Table 2 不一致\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 26\n    mentions:\n      - {round: 26, reviewers: [1, 2], note: \"R2-W2，R1 交叉同意。Abstract 用 matched-sparsity (8.81 vs 10.30, Appendix D)，但 Table 2 TEAL uniform 30%=10.82（改进 18.6%）。一级读者查 Table 2 找不到 10.30。方法论上 matched-sparsity 合理但呈现方式导致困惑。\"}\n    action_items:\n      - {round: 26, action: \"在 Table 2 caption 或正文中标注 matched-sparsity 对比来源，或在 Table 2 增加 matched-sparsity 行\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R25-W3\"\n    summary: \"Introduction '19%' PPL 减少已修正为 14.5% matched-sparsity\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - {round: 25, reviewers: [1, 2], note: \"19% 计算不符。\"}\n      - {round: 26, reviewers: [1, 2], note: \"R26 论文已使用 14.5% matched-sparsity 数字，数值本身正确。但引用基准问题升级为独立 issue R26-W1。\"}\n    resolution: \"数值已修正为 14.5% matched-sparsity。基准一致性问题转入 R26-W1。\"\n    resolution_round: 26\n\n  - id: \"R25-M1\"\n    summary: \"术语不一致：output-distribution alignment/distillation/objective 交替使用\"\n    category: writing\n    severity: minor\n    status: open\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - {round: 25, reviewers: [2], note: \"全文交替使用多种术语。\"}\n      - {round: 26, reviewers: [1, 2], note: \"R26 R2-M2 再次提出，R1 交叉同意。建议统一为 'output-distribution KL' 或 'end-to-end KL distillation'。\"}\n    action_items:\n      - {round: 25, action: \"全文统一术语\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R26-M1\"\n    summary: \"Introduction 中 8.6%/6.4% 未标注 sparsity level\"\n    category: writing\n    severity: minor\n    status: open\n    first_raised_round: 26\n    last_seen_round: 26\n    mentions:\n      - {round: 26, reviewers: [1, 2], note: \"R2-M1，R1 交叉同意。§3.4 line 81 数字来自 50% (Table 4)，30% 差距小得多 (KL vs JSD 仅 1.0%)。不标注 sparsity level 会高估 forward KL 在 moderate sparsity 下的优势。\"}\n    action_items:\n      - {round: 26, action: \"§3.4 标注 '(at 50% sparsity)'\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R26-M2\"\n    summary: \"'stable downstream' 措辞指跨 seed 稳定性但易误读为性能保持\"\n    category: writing\n    severity: minor\n    status: open\n    first_raised_round: 26\n    last_seen_round: 26\n    mentions:\n      - {round: 26, reviewers: [1, 2], note: \"R2-M4，R1 同意。'MMLU 40.7±1.3%' 相对 dense 65.27% 降 24.5pp，'stable' 指跨 seed 而非绝对性能。应改为 'reproducible across seeds' 或 'low cross-seed variance'。\"}\n    action_items:\n      - {round: 26, action: \"Introduction 中 'stable downstream' → 'low cross-seed variance' 或 'reproducible'\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R26-M3\"\n    summary: \"68% divergence 和 32% Jaccard 同句出现易混淆\"\n    category: writing\n    severity: minor\n    status: open\n    first_raised_round: 26\n    last_seen_round: 26\n    mentions:\n      - {round: 26, reviewers: [1, 2], note: \"R2-M6，R1 同意。Introduction 同句用互补度量（Jaccard distance 68% = 1 - similarity 32%）造成混淆。建议统一。\"}\n    action_items:\n      - {round: 26, action: \"Introduction 统一使用 Jaccard distance 或明确标注\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 26 — 无实际加速 (Reviewer 分歧项)\n  # ============================================================\n\n  - id: \"R19-N3\"\n    summary: \"无实际 wall-clock 加速: +6.4% overhead, unstructured masks 无 speedup\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 26\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Critical。Intro framing 已修改为 empirical study。\"}\n      - {round: 22, reviewers: [1, 2], note: \"降为 Warning。论文已定位为 analysis work。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 W1。仍为 Warning。\"}\n      - {round: 25, reviewers: [1, 2], note: \"R25 Should-Fix。论文诚实披露。\"}\n      - {round: 26, reviewers: [1, 2], note: \"R26 唯一分歧点。R1 定为 critical (N3)，R2 rebut 降为 warning——论文自定位 empirical study，compensation 冗余性发现减少推理开销并节省 67.2M 参数，C1 证明 KL targets 可迁移到 BCE 有工程价值。Director 裁定：降为 warning，论文 framing 已充分。\"}\n    action_items:\n      - {round: 21, action: \"Abstract 加 empirical study + §1 disclaimer\", assigned_to: \"paper_agent\", status: done}\n      - {round: 22, action: \"§1 加 speedup 条件 + 6.4% overhead\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"结构性限制。论文已充分 framed 为 empirical study。R26 R1 升级为 critical 但 R2 rebut 有效，维持 warning。\"\n    resolution_round: 23\n\n  # ============================================================\n  # Round 26 — Resolved / Carried forward\n  # ============================================================\n\n  - id: \"R24-W1\"\n    summary: \"评估覆盖度关键空白：无生成任务、固定 seq_len=2048、无 batched inference\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 26\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"无 MT-Bench 等生成任务。\"}\n      - {round: 25, reviewers: [2], note: \"Base model 不适用 MT-Bench (需 instruction-tuned)。\"}\n      - {round: 26, reviewers: [], note: \"R26 未单独提出。Limitations 已覆盖。\"}\n    resolution: \"Limitations 已覆盖。Base model 不适用生成评估。\"\n    resolution_round: 25\n\n  - id: \"R24-W4\"\n    summary: \"'Primary design dimension' 声明需资格限定\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 26\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"建议软化为 'substantially outperforms'。\"}\n      - {round: 25, reviewers: [1, 2], note: \"已改为 'primary design dimension'，限定 30%。\"}\n      - {round: 26, reviewers: [1, 2], note: \"R26 与 R20-N2 重叠。'primary design dimension' 需进一步限定为 PPL+commonsense 而非 general。追踪合并入 R20-N2。\"}\n    resolution: \"追踪合并入 R20-N2。\"\n    resolution_round: 26\n\n  - id: \"R25-W2\"\n    summary: \"MSE 50% baseline 仅 seed 42 有效\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - {round: 25, reviewers: [1, 2], note: \"MSE 50% s123 catastrophic PPL=15789。\"}\n      - {round: 26, reviewers: [1, 2], note: \"R26 R1-W2 提及。Table 4 MSE 50% 标注 § 但正文 §3.7 使用时未注 single-seed caveat。\"}\n    action_items:\n      - {round: 25, action: \"正文使用 MSE 50% 时注明 single-seed caveat\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W6\"\n    summary: \"Figure 2 仅展示 global allocation 但推荐 uniform\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 26\n    mentions:\n      - {round: 22, reviewers: [1, 2], note: \"正文 Figure 之一，framing 效果强。\"}\n      - {round: 26, reviewers: [], note: \"R26 未单独提出。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R25-M2\"\n    summary: \"Eq. 4 s_j 缺少层标 ℓ 上标\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 25\n    last_seen_round: 25\n    resolution: \"Eq. 4 已补充 ℓ 上标。\"\n    resolution_round: 25\n\n  - id: \"R19-W1\"\n    summary: \"与 MaskLLM 新颖性区分\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 26\n    mentions:\n      - {round: 26, reviewers: [1, 2], note: \"R26 合并进 R25-N1。MaskLLM 三点区分已落地，Table 1 遗漏作为 R25-N1 子项追踪。\"}\n    resolution: \"合并进 R25-N1。\"\n    resolution_round: 25\n\n  - id: \"R20-W4\"\n    summary: \"WikiText 同分布评估 + C4 OOD variance\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 26\n    mentions:\n      - {round: 26, reviewers: [], note: \"R26 未提出。Appendix D OOD 证据充分。\"}\n    resolution: \"Appendix D OOD 证据充分。\"\n    resolution_round: 25\n\n  - id: \"R22-W3\"\n    summary: \"Table 2 actual sparsity mismatch ‡ 脚注不够显著\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 26\n    mentions:\n      - {round: 26, reviewers: [1], note: \"R1 minor：Lagrangian 在 30% 饱和 λ=5000 导致 actual 28.5%。Appendix C 有 matched 对比。\"}\n    resolution: \"§4.1 matched 14.5% 独立句。‡ 脚注存在。\"\n    resolution_round: 23\n\n  - id: \"R22-W5\"\n    summary: \"规模泛化仅 7-14B\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 26\n    mentions:\n      - {round: 26, reviewers: [1, 2], note: \"R26 与 R20-N2 M7 重叠。14B GSM8K -20pp 恶化的机制分析不足。Limitations 已含 'evaluation bounded at 7-14B'。\"}\n    resolution: \"Limitations 已包含 scale limitation 讨论。\"\n    resolution_round: 25\n\n  - id: \"R19-N2\"\n    summary: \"C1 target-swap ablation 因果声明\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 24\n    resolution: \"C1 claim 已降级为 transferability。\"\n    resolution_round: 23\n\n  - id: \"R22-W7\"\n    summary: \"Abstract 第5句信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"已拆分。\"\n    resolution_round: 23\n\n  - id: \"R22-W8\"\n    summary: \"Conclusion 引用 BoolQ (高 variance, 仅 Appendix)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"BoolQ → HellaSwag/PIQA。\"\n    resolution_round: 23\n\n  - id: \"R19-W7\"\n    summary: \"30% sparsity sweet spot 限制实际影响\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 26\n    resolution: \"Limitations 已覆盖。连续多轮未被 reviewer 提出。\"\n    resolution_round: 25\n\n  - id: \"R15-N3\"\n    summary: \"MaskLLM 新颖性边界\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 26\n    resolution: \"§2 三点本质差异。合并进 R25-N1。\"\n    resolution_round: 23"
  }
}
```

</details>

---


### Tool result

_source line 2107 · 2026-05-23T01:43:10.549177+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml\", \"bytes\": 17970}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 2108 · 2026-05-23T01:45:59.354177+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
  "cross_response_reviewer_ids": "[\"1\", \"2\"]",
  "overall_score": "3.5",
  "report": "# 审稿报告：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n**目标 Venue**: EMNLP 2026 via ARR May 2026  \n**审稿轮次**: Round 26 (Fresh Review)  \n**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验有效性; R2: 新颖性 + 完整性）  \n**交叉分享**: 已完成，1 轮收敛  \n\n---\n\n## Summary\n\n论文提出用 forward KL divergence 替代传统 BCE 训练 SwiGLU LLM 的上下文稀疏预测器（75.9M params, <1% base model），通过 Gumbel-Sigmoid relaxation 实现可微 mask 生成。在 LLaMA-3.1-8B 上 30% sparsity 下 PPL 降低 14.5%（matched sparsity），50% 下降 50%，跨架构（Mistral-7B、Qwen-2.5-14B）一致。论文同时贡献了 signal type vs coupling scope 的二维分解分析和 C1 target-swap ablation。自定位为 empirical study，不涉及推理加速。\n\n---\n\n## Strengths\n\n1. **PPL 改善显著且跨架构一致**：14.5% at 30%, 50% at 50%, 82% at 70%，在 LLaMA/Mistral/Qwen 三架构上均成立。3-seed PPL 方差极低（σ=0.02, CV=0.2%），改进可信度高。[R1 S3, R2 S3, 共识]\n\n2. **C1 Target-Swap Ablation 设计精巧**：将 KL-derived mask patterns 提取后用 BCE 重训练，在 30% (≤1.70pp gap) 和 50% (≤0.79pp gap) 均接近 KL 性能，有力证明 mask target quality 而非 gradient coupling 驱动推理质量。实验设计有新意且有信息量。[R1 S1, R2 S2, 共识]\n\n3. **对局限性的诚实披露极为罕见**：Abstract 中即承认无加速，正文持续标注 \"upper bound\" / \"confound\" / \"not fully orthogonal\"，Limitations 坦承所有负面发现。这种透明度在投稿论文中极少见。[R1 S2, R2 S1, 共识]\n\n4. **实验覆盖面广**：5 种 loss 排名、3 个架构（7B–14B）、6 个 sparsity levels（25%–70%）、2 种 allocation 策略、sensitivity sweeps（bottleneck/temperature/steps）、OOD 评估（C4）、cross-seed mask consistency 分析。附录约 11 页，极为充分。[R1 S4, R2 S1, 共识]\n\n5. **Compensation 冗余性发现有实用价值**：证明 FastForward 风格 67.2M 补偿网络在 KL predictor 下完全冗余（Appendix J），推理开销从 +9.1% 降至 +6.4% 并节省 67.2M 参数。[R2 S4]\n\n6. **2D Taxonomy (signal type × coupling scope) 提供有用分析框架**：即使分解不完美，该视角对理解稀疏预测方法空间有价值。[R1 S5, R2 S5]\n\n7. **训练成本极低**：1000 步、单 GPU、~45 分钟，实用门槛非常低。[R1 S6]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1. [Critical] Signal type vs coupling scope 分解在 50% 稀疏度下失效，但 Abstract/Conclusion 的 claim 限定不足**\n- R1-N2, R2-N1, 完全共识\n- 核心问题：(1) K=1 per-layer KL 同时改变 coupling 和 train-inference mismatch (训练 1/32 layers, 推理全部 32)，论文承认为 \"upper bound\" 但仍以较强措辞陈述；(2) K=4 在 50% 下 PPL=44.23 > K=1 的 34.85，论文自身承认分解 \"unreliable under the current design\"（§4.5 最后一段）；(3) K=4 MMLU 异常（42.7±1.4 > E2E 40.7±1.3）暴露 allocation confound：K=4 near-uniform allocation (std=0.003) 等价于移除 protection valley（Appendix T: remove-valley → MMLU=44.0），signal type 与 coupling scope 并非正交。\n- Abstract 已加 \"(upper bound; not fully orthogonal with coupling scope)\" qualifier，但 \"accounts for the majority\" 仍较强。Conclusion 标注 \"upper bound\" 但适用范围限定不够显著。\n- 建议：(1) 将分解 claim 限定为 \"at 30% moderate sparsity, subject to train-inference mismatch confound\"；(2) 设计 stop-gradient 实验（detach downstream Jacobian 的跨层梯度，保留 output-distribution 目标但切断 coupling）作为更干净的 deconfounding；(3) 在 Abstract/Conclusion 中明确此分解不适用于 50%。\n\n**C2. [Critical] 知识任务系统性退步缺乏机制分析，与 \"primary design dimension\" claim 矛盾**\n- R1-N1, R2-N2, 完全共识\n- 核心问题：KL 在所有规模和架构上 MMLU/GSM8K 低于 TEAL——8B: MMLU −5.2pp, GSM8K −1.3pp；Mistral: GSM8K −7.3pp；14B: GSM8K **−20.1pp** (σ=5.2pp)。退步跨 scale 恶化 15 倍（8B→14B GSM8K），不可归于噪声。\n- §4.2 提出两个假设（训练数据同质性 + forward KL mode-covering 稀释 rare activations），仅 constraint experiment 部分验证第一个（remove valley → MMLU +3.4pp，解释约 65% 退步），第二个假设无任何实验支撑。\n- Abstract 仅说 \"commonsense gains but knowledge-intensive decline\" 未量化幅度，有轻描淡写之嫌。\"primary design dimension\" claim 仅对 PPL 和 commonsense 成立，对知识任务 KL 是 inferior。\n- 建议：(1) Abstract 量化退步幅度；(2) 将 \"primary design dimension\" 限定为 \"for PPL and commonsense tasks at moderate sparsity\"；(3) 做 mixed-domain training（WikiText + 数学/代码数据）或 knowledge neuron probe 验证机制假设。\n\n### Should-Fix（影响评分但不一票否决）\n\n**S1. [Warning] Downstream 统计力不足**\n- R1-W1, R2 同意\n- MMLU 30% global σ=9.5（95% CI ≈ ±23.5pp），ARC-c σ=3.6, Mistral ARC-c σ=6.4, Qwen GSM8K σ=5.2。PPL 作为 primary metric 完全可靠（σ=0.02），但 abstract/conclusion 中的下游 claims 统计基础薄弱。\n- 建议：下游比较进一步弱化为 \"directional trends\"；考虑 paired t-test 或增加 seeds。\n\n**S2. [Warning] Table 2 baseline 比较条件不统一**\n- R1-W2, R2-M3, 共识\n- BCE 30% 用 TEAL global (†)，KL 有 global + uniform；BCE 50% 用 2700 steps。横向比较需跳转 allocation 和 compute budget，读者负担重。\n- 建议：增加 controlled comparison 子表或将 BCE 30% uniform (PPL=15.71, Table 4) 纳入正表。\n\n**S3. [Warning] C1 ablation 的 soft-vs-hard confound 未解决**\n- R1-W3, R2-W5, 共识\n- C1 二值化 KL logits (>0) 同时改变 target source 和 mask representation。BCE+Gumbel (32.22) vs BCE (27.97) 使用 magnitude targets，不足以排除 confound。R1 补充：confound 影响的是 *why* transfer works，不影响 *whether* works（≤0.79pp gap 已建立 transferability）。\n- 建议：增加 BCE+Gumbel on KL-derived targets 实验；正文加强 confound 讨论。\n\n**S4. [Warning] MaskLLM 在 Taxonomy Table 1 中缺位**\n- R2-W1, R1 同意\n- Table 1 Static × Coupled 格仅列 SPON，MaskLLM (static N:M + KL) 也属此格。三点区分合理但无实验验证。\n- R1 补充：setting 差异足够大，不需 Table 2 baseline 对比，Table 1 加注即可。\n\n**S5. [Warning] 14.5% PPL improvement 引用基准不一致**\n- R2-W2, R1 同意\n- Abstract 用 matched-sparsity (8.81 vs 10.30, Appendix D)，Table 2 TEAL uniform 30%=10.82（改进 18.6%）。一级读者查 Table 2 找不到 10.30。\n- 建议：在 Table 2 中增加 matched-sparsity 行，或在 caption 中标注来源。\n\n**S6. [Warning] Qwen-14B 评估不完整**\n- R1-W4, R2-M7, 共识\n- 仅 30% sparsity，无 50% 结果，无 per-layer allocation 分析。GSM8K −20.1pp (σ=5.2pp) 的机制未分析（可能原因：d_ff=18944 vs LLaMA 14336 导致 d_b=128 压缩比更大；14B 数学能力更强被破坏量更大）。\n- 建议：至少增加 50% PPL；讨论 14B 退化加剧的可能机制。\n\n**S7. [Warning] 无实际推理加速**\n- R1-N3 (critical), R2 REBUT → warning. Director 裁定：**降为 warning**\n- 理由：(1) 论文自定位 empirical study，贡献在于理解训练目标对 mask quality 的影响；(2) compensation 冗余性发现减少推理开销从 +9.1% 到 +6.4% 并节省 67.2M 参数；(3) C1 证明 KL targets 可迁移到 BCE 有工程价值。\n- R1 建议的 proof-of-concept sparse kernel 实验或与 LaRoSA 等方法在 mask quality 层面对比仍然有价值。\n\n### Minor（不影响接收）\n\n- **M1**: §3.4 中 forward KL vs RevKL 8.6%/6.4% 未标注 sparsity level（来自 50%，30% 差距小得多）[R2-M1, R1 同意]\n- **M2**: 术语不一致——output-distribution alignment / KL distillation / coupled objective 交替使用 [R2-M2, R1 同意]\n- **M3**: \"stable downstream (MMLU 40.7±1.3%)\" 指跨 seed 稳定性而非性能保持（vs dense 65.27%），措辞易误读 [R2-M4, R1 同意]\n- **M4**: Introduction 中 68% divergence 和 32% Jaccard 同句出现，为互补度量易混淆 [R2-M6, R1 同意]\n- **M5**: Eq. 5 求和方式正文未明确（附录才说 average over positions）[R1]\n- **M6**: Figure 1 过于简略，未展示 Gumbel relaxation 和 Lagrangian controller [R1]\n- **M7**: C1 s42 oracle 来自 earlier checkpoint（Table 3 † 标注不够显著）[R1, R2]\n- **M8**: 页数合规性——Conclusion 可能溢出第 8 页 1-2 行 [R2-M5, R1 确认违规但可通过排版修复]\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer **完全共识**（均标注 [AGREE]）：\n\n1. **Signal type/coupling 分解的方法论可靠性**（C1）：50% 下失效，Abstract/Conclusion 的 claim 限定不足，K=4 MMLU 异常暴露 allocation confound，两维度不正交\n2. **知识任务系统性退步**（C2）：机制分析不足，\"primary design dimension\" 对知识任务不成立，Abstract 未量化退步\n3. **C1 soft-vs-hard confound**（S3）：BCE+Gumbel vs BCE 的控制用 magnitude targets 不足以排除 confound\n4. **Table 2 baseline 不统一**（S2）：读者需跨 allocation 和 compute budget 跳转理解比较\n5. **Qwen-14B 评估不完整**（S6）：GSM8K 退步 15 倍恶化缺乏机制分析\n6. **所有 Minor 问题**（M1-M8）：均达成一致\n\n## Reviewer Divergence\n\n唯一分歧点：**无实际推理加速的严重程度**\n- R1：定为 critical（N3）——稀疏预测方法不能加速，实用贡献存疑\n- R2：REBUT，认为应降为 warning——论文自定位 empirical study，compensation 冗余性和 C1 target transfer 提供间接工程价值\n- **Director 裁定**：采纳 R2 的 rebut，降为 warning（S7）。论文的核心贡献是分析性的，framing 已充分，但 R1 建议的 proof-of-concept 加速或与 LaRoSA 的 mask quality 对比仍有价值。\n\n---\n\n## Questions\n\n1. 是否尝试过 mixed-domain 训练数据（WikiText + 数学/代码文本）？这是验证知识任务退化是否数据依赖的最直接实验。\n2. 在 K=4 控制中强制使用 E2E 的非均匀 allocation（而非 K=4 自行收敛到 near-uniform），MMLU 异常是否消失？\n3. Stop-gradient 实验（KL loss 反传时 detach downstream Jacobian 的跨层梯度）是否可行？这比 K=1/K=4 更干净地隔离 coupling scope。\n4. L14-L18 protection valley pattern 在 Mistral 和 Qwen 上是否也出现？\n5. Table 4 中 BCE+Gumbel+Penalty (38.02) 比无 penalty (32.22) 更差——为什么 sparsity penalty 让 BCE 恶化？\n6. Qwen-2.5-14B 的 d_ff=18944 vs LLaMA 14336——predictor bottleneck d_b=128 是否应随 scale 调整？\n\n---\n\n## Missing References\n\n1. **MaskLLM** (Fang et al., NeurIPS 2024): 已引用讨论但应在 Table 1 taxonomy 中体现位置（Static × Coupled 格）。[R1, R2 共识]\n2. **ActTail** (arXiv:2603.12272, March 2026): 基于 HT-SR 理论的全局 activation sparsity allocation，与 per-layer allocation 分析相关。[R2 提出，R1 认为 2 个月前 arXiv 预印本不应作为 Should-Fix，降为 info]\n3. **CATS** (Lee et al., 2024): §2 提到但 Table 2 未作为 baseline。[R1 提出]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未启用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**done**（耗时 ~3.5 分钟）\n\n### 发现摘要\n- **Critical**: 0\n- **Warning**: 1 — Page 6（§4.1-4.2 开头）整页纯文字，无任何 display item，位于 Table 1 和 Tables 2-3 之间，视觉节奏中断。建议调整 float 位置使 Table 2 提前。\n- **Info**: 18 — 整体排版质量良好；Figure 1 架构图字号偏小但可读；Table 2 字号偏小但可读；Appendix page 17 密度最高但作为附录可接受；Figure 2 轴标签清晰且色盲友好；Section 5 heading 未孤悬；Limitations 简洁符合 EMNLP 要求。\n- **页数合规**: 视觉审查 Agent 确认 Limitations/Ethics/References 在第 9 页开始，主文约 8 页。但 R2 指出 Conclusion 可能有 1-2 行溢出到第 9 页，需核实 LaTeX 编译结果。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 / 5 — Borderline Conference  \n**置信度**: 4 / 5\n\n### 评分理由\n\n**会议门槛因素（积极）**：\n- PPL 改善显著（14.5%–82%）、跨架构一致、3-seed 高置信度——这是一个 robust 的实证发现\n- C1 target-swap ablation 是一个有创意且有信息量的实验设计\n- 实验覆盖面在该方向上属于最全面之列\n- 论文对局限性的主动披露体现了学术诚信\n- Compensation 冗余性发现有实际工程价值\n\n**会议门槛因素（消极）**：\n- 核心分析贡献（signal type vs coupling scope 分解）在 50% 下完全失效，方法论可靠性不足以支撑 Abstract/Conclusion 中的 claim 强度\n- 知识任务系统性退步（跨规模恶化 15 倍）与 \"primary design dimension\" 的强 claim 之间存在根本张力，机制分析停留在假设层面\n- 方法新颖性有限——核心组件（KL、Gumbel-Sigmoid、MLP predictor）均为成熟技术，主要贡献是成熟组件在新场景的应用\n- 无实际推理加速（+6.4% overhead），限制实用影响\n\n### 改进路径\n\n**达到 Conference（4.0）所需**：\n1. 分解 claim 限定为 30% + 更干净的 deconfounding（stop-gradient 或更多 K 值）\n2. Abstract/Conclusion 量化知识任务退步并限定 \"primary design dimension\" 适用范围\n3. Mixed-domain training 验证数据偏差假设，或 knowledge neuron probe 验证 mode-covering 假设\n\n**当前适合 Findings（3.0-3.5）**：\n论文作为 empirical study 的价值在 Findings 层面是明确的——它是该方向首个系统性实证研究，实验可信度高，负面发现（知识退步、分解失效）本身也有信息量。核心 claim 的过度表述和分解实验的方法论问题是阻碍 Conference 的主要因素。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Line 18: \"This paper is primarily an empirical study\" 定位准确，但应更早出现（当前在 contribution list 之后）\n- \"stable downstream (MMLU 40.7±1.3%)\" 易误读——应改为 \"low cross-seed variance\"\n- 68% divergence 和 32% Jaccard 同句出现为互补度量，建议统一\n\n### §3 Method\n- §3.4 \"forward KL outperforms reverse KL by 8.6% and JSD by 6.4%\"：来自 50%，应标注 sparsity level\n- §3.6 Gradient analysis 提供良好直觉，SNR 分析结论自洽（KL SNR 更低但 mask 更好）\n- §3.7 Taxonomy Table 1: Static × Coupled 应纳入 MaskLLM\n\n### §4 Experiments\n- §4.2 Knowledge-Task Regression 两个假设均为推测——至少需一个控制实验（mixed-domain 或 neuron probe）\n- §4.4 C1 ablation 核心结论（mask patterns transfer）稳健；soft-vs-hard confound 影响 why 而非 whether\n- §4.5 Per-layer KL decomposition 在 30% 可解释，50% 失效应更显著标注\n- Table 2 条件不统一增加阅读负担\n- Table 4 Forward KL vs JSD 在 30% 仅 0.09pp，divergence 选择在 moderate sparsity 下更接近 implementation detail\n\n### §5 Conclusion\n- 可能溢出第 8 页 1-2 行——需核实并修复\n\n### Limitations\n- 覆盖全面（sparsity sweet spot, knowledge regression, training data homogeneity, seq length, batched inference, generation evaluation）\n- R26 新增建议：讨论 14B regression 加剧对 70B+ scalability 的影响（已包含）\n\n### Appendix\n- 约 11 页，覆盖极为充分\n- Appendix P (Oracle Provenance): s42 oracle 来自 earlier checkpoint 应在正文 Table 3 更显著标注"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
    "cross_response_reviewer_ids": "[\"1\", \"2\"]",
    "overall_score": "3.5",
    "report": "# 审稿报告：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n**目标 Venue**: EMNLP 2026 via ARR May 2026  \n**审稿轮次**: Round 26 (Fresh Review)  \n**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验有效性; R2: 新颖性 + 完整性）  \n**交叉分享**: 已完成，1 轮收敛  \n\n---\n\n## Summary\n\n论文提出用 forward KL divergence 替代传统 BCE 训练 SwiGLU LLM 的上下文稀疏预测器（75.9M params, <1% base model），通过 Gumbel-Sigmoid relaxation 实现可微 mask 生成。在 LLaMA-3.1-8B 上 30% sparsity 下 PPL 降低 14.5%（matched sparsity），50% 下降 50%，跨架构（Mistral-7B、Qwen-2.5-14B）一致。论文同时贡献了 signal type vs coupling scope 的二维分解分析和 C1 target-swap ablation。自定位为 empirical study，不涉及推理加速。\n\n---\n\n## Strengths\n\n1. **PPL 改善显著且跨架构一致**：14.5% at 30%, 50% at 50%, 82% at 70%，在 LLaMA/Mistral/Qwen 三架构上均成立。3-seed PPL 方差极低（σ=0.02, CV=0.2%），改进可信度高。[R1 S3, R2 S3, 共识]\n\n2. **C1 Target-Swap Ablation 设计精巧**：将 KL-derived mask patterns 提取后用 BCE 重训练，在 30% (≤1.70pp gap) 和 50% (≤0.79pp gap) 均接近 KL 性能，有力证明 mask target quality 而非 gradient coupling 驱动推理质量。实验设计有新意且有信息量。[R1 S1, R2 S2, 共识]\n\n3. **对局限性的诚实披露极为罕见**：Abstract 中即承认无加速，正文持续标注 \"upper bound\" / \"confound\" / \"not fully orthogonal\"，Limitations 坦承所有负面发现。这种透明度在投稿论文中极少见。[R1 S2, R2 S1, 共识]\n\n4. **实验覆盖面广**：5 种 loss 排名、3 个架构（7B–14B）、6 个 sparsity levels（25%–70%）、2 种 allocation 策略、sensitivity sweeps（bottleneck/temperature/steps）、OOD 评估（C4）、cross-seed mask consistency 分析。附录约 11 页，极为充分。[R1 S4, R2 S1, 共识]\n\n5. **Compensation 冗余性发现有实用价值**：证明 FastForward 风格 67.2M 补偿网络在 KL predictor 下完全冗余（Appendix J），推理开销从 +9.1% 降至 +6.4% 并节省 67.2M 参数。[R2 S4]\n\n6. **2D Taxonomy (signal type × coupling scope) 提供有用分析框架**：即使分解不完美，该视角对理解稀疏预测方法空间有价值。[R1 S5, R2 S5]\n\n7. **训练成本极低**：1000 步、单 GPU、~45 分钟，实用门槛非常低。[R1 S6]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1. [Critical] Signal type vs coupling scope 分解在 50% 稀疏度下失效，但 Abstract/Conclusion 的 claim 限定不足**\n- R1-N2, R2-N1, 完全共识\n- 核心问题：(1) K=1 per-layer KL 同时改变 coupling 和 train-inference mismatch (训练 1/32 layers, 推理全部 32)，论文承认为 \"upper bound\" 但仍以较强措辞陈述；(2) K=4 在 50% 下 PPL=44.23 > K=1 的 34.85，论文自身承认分解 \"unreliable under the current design\"（§4.5 最后一段）；(3) K=4 MMLU 异常（42.7±1.4 > E2E 40.7±1.3）暴露 allocation confound：K=4 near-uniform allocation (std=0.003) 等价于移除 protection valley（Appendix T: remove-valley → MMLU=44.0），signal type 与 coupling scope 并非正交。\n- Abstract 已加 \"(upper bound; not fully orthogonal with coupling scope)\" qualifier，但 \"accounts for the majority\" 仍较强。Conclusion 标注 \"upper bound\" 但适用范围限定不够显著。\n- 建议：(1) 将分解 claim 限定为 \"at 30% moderate sparsity, subject to train-inference mismatch confound\"；(2) 设计 stop-gradient 实验（detach downstream Jacobian 的跨层梯度，保留 output-distribution 目标但切断 coupling）作为更干净的 deconfounding；(3) 在 Abstract/Conclusion 中明确此分解不适用于 50%。\n\n**C2. [Critical] 知识任务系统性退步缺乏机制分析，与 \"primary design dimension\" claim 矛盾**\n- R1-N1, R2-N2, 完全共识\n- 核心问题：KL 在所有规模和架构上 MMLU/GSM8K 低于 TEAL——8B: MMLU −5.2pp, GSM8K −1.3pp；Mistral: GSM8K −7.3pp；14B: GSM8K **−20.1pp** (σ=5.2pp)。退步跨 scale 恶化 15 倍（8B→14B GSM8K），不可归于噪声。\n- §4.2 提出两个假设（训练数据同质性 + forward KL mode-covering 稀释 rare activations），仅 constraint experiment 部分验证第一个（remove valley → MMLU +3.4pp，解释约 65% 退步），第二个假设无任何实验支撑。\n- Abstract 仅说 \"commonsense gains but knowledge-intensive decline\" 未量化幅度，有轻描淡写之嫌。\"primary design dimension\" claim 仅对 PPL 和 commonsense 成立，对知识任务 KL 是 inferior。\n- 建议：(1) Abstract 量化退步幅度；(2) 将 \"primary design dimension\" 限定为 \"for PPL and commonsense tasks at moderate sparsity\"；(3) 做 mixed-domain training（WikiText + 数学/代码数据）或 knowledge neuron probe 验证机制假设。\n\n### Should-Fix（影响评分但不一票否决）\n\n**S1. [Warning] Downstream 统计力不足**\n- R1-W1, R2 同意\n- MMLU 30% global σ=9.5（95% CI ≈ ±23.5pp），ARC-c σ=3.6, Mistral ARC-c σ=6.4, Qwen GSM8K σ=5.2。PPL 作为 primary metric 完全可靠（σ=0.02），但 abstract/conclusion 中的下游 claims 统计基础薄弱。\n- 建议：下游比较进一步弱化为 \"directional trends\"；考虑 paired t-test 或增加 seeds。\n\n**S2. [Warning] Table 2 baseline 比较条件不统一**\n- R1-W2, R2-M3, 共识\n- BCE 30% 用 TEAL global (†)，KL 有 global + uniform；BCE 50% 用 2700 steps。横向比较需跳转 allocation 和 compute budget，读者负担重。\n- 建议：增加 controlled comparison 子表或将 BCE 30% uniform (PPL=15.71, Table 4) 纳入正表。\n\n**S3. [Warning] C1 ablation 的 soft-vs-hard confound 未解决**\n- R1-W3, R2-W5, 共识\n- C1 二值化 KL logits (>0) 同时改变 target source 和 mask representation。BCE+Gumbel (32.22) vs BCE (27.97) 使用 magnitude targets，不足以排除 confound。R1 补充：confound 影响的是 *why* transfer works，不影响 *whether* works（≤0.79pp gap 已建立 transferability）。\n- 建议：增加 BCE+Gumbel on KL-derived targets 实验；正文加强 confound 讨论。\n\n**S4. [Warning] MaskLLM 在 Taxonomy Table 1 中缺位**\n- R2-W1, R1 同意\n- Table 1 Static × Coupled 格仅列 SPON，MaskLLM (static N:M + KL) 也属此格。三点区分合理但无实验验证。\n- R1 补充：setting 差异足够大，不需 Table 2 baseline 对比，Table 1 加注即可。\n\n**S5. [Warning] 14.5% PPL improvement 引用基准不一致**\n- R2-W2, R1 同意\n- Abstract 用 matched-sparsity (8.81 vs 10.30, Appendix D)，Table 2 TEAL uniform 30%=10.82（改进 18.6%）。一级读者查 Table 2 找不到 10.30。\n- 建议：在 Table 2 中增加 matched-sparsity 行，或在 caption 中标注来源。\n\n**S6. [Warning] Qwen-14B 评估不完整**\n- R1-W4, R2-M7, 共识\n- 仅 30% sparsity，无 50% 结果，无 per-layer allocation 分析。GSM8K −20.1pp (σ=5.2pp) 的机制未分析（可能原因：d_ff=18944 vs LLaMA 14336 导致 d_b=128 压缩比更大；14B 数学能力更强被破坏量更大）。\n- 建议：至少增加 50% PPL；讨论 14B 退化加剧的可能机制。\n\n**S7. [Warning] 无实际推理加速**\n- R1-N3 (critical), R2 REBUT → warning. Director 裁定：**降为 warning**\n- 理由：(1) 论文自定位 empirical study，贡献在于理解训练目标对 mask quality 的影响；(2) compensation 冗余性发现减少推理开销从 +9.1% 到 +6.4% 并节省 67.2M 参数；(3) C1 证明 KL targets 可迁移到 BCE 有工程价值。\n- R1 建议的 proof-of-concept sparse kernel 实验或与 LaRoSA 等方法在 mask quality 层面对比仍然有价值。\n\n### Minor（不影响接收）\n\n- **M1**: §3.4 中 forward KL vs RevKL 8.6%/6.4% 未标注 sparsity level（来自 50%，30% 差距小得多）[R2-M1, R1 同意]\n- **M2**: 术语不一致——output-distribution alignment / KL distillation / coupled objective 交替使用 [R2-M2, R1 同意]\n- **M3**: \"stable downstream (MMLU 40.7±1.3%)\" 指跨 seed 稳定性而非性能保持（vs dense 65.27%），措辞易误读 [R2-M4, R1 同意]\n- **M4**: Introduction 中 68% divergence 和 32% Jaccard 同句出现，为互补度量易混淆 [R2-M6, R1 同意]\n- **M5**: Eq. 5 求和方式正文未明确（附录才说 average over positions）[R1]\n- **M6**: Figure 1 过于简略，未展示 Gumbel relaxation 和 Lagrangian controller [R1]\n- **M7**: C1 s42 oracle 来自 earlier checkpoint（Table 3 † 标注不够显著）[R1, R2]\n- **M8**: 页数合规性——Conclusion 可能溢出第 8 页 1-2 行 [R2-M5, R1 确认违规但可通过排版修复]\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer **完全共识**（均标注 [AGREE]）：\n\n1. **Signal type/coupling 分解的方法论可靠性**（C1）：50% 下失效，Abstract/Conclusion 的 claim 限定不足，K=4 MMLU 异常暴露 allocation confound，两维度不正交\n2. **知识任务系统性退步**（C2）：机制分析不足，\"primary design dimension\" 对知识任务不成立，Abstract 未量化退步\n3. **C1 soft-vs-hard confound**（S3）：BCE+Gumbel vs BCE 的控制用 magnitude targets 不足以排除 confound\n4. **Table 2 baseline 不统一**（S2）：读者需跨 allocation 和 compute budget 跳转理解比较\n5. **Qwen-14B 评估不完整**（S6）：GSM8K 退步 15 倍恶化缺乏机制分析\n6. **所有 Minor 问题**（M1-M8）：均达成一致\n\n## Reviewer Divergence\n\n唯一分歧点：**无实际推理加速的严重程度**\n- R1：定为 critical（N3）——稀疏预测方法不能加速，实用贡献存疑\n- R2：REBUT，认为应降为 warning——论文自定位 empirical study，compensation 冗余性和 C1 target transfer 提供间接工程价值\n- **Director 裁定**：采纳 R2 的 rebut，降为 warning（S7）。论文的核心贡献是分析性的，framing 已充分，但 R1 建议的 proof-of-concept 加速或与 LaRoSA 的 mask quality 对比仍有价值。\n\n---\n\n## Questions\n\n1. 是否尝试过 mixed-domain 训练数据（WikiText + 数学/代码文本）？这是验证知识任务退化是否数据依赖的最直接实验。\n2. 在 K=4 控制中强制使用 E2E 的非均匀 allocation（而非 K=4 自行收敛到 near-uniform），MMLU 异常是否消失？\n3. Stop-gradient 实验（KL loss 反传时 detach downstream Jacobian 的跨层梯度）是否可行？这比 K=1/K=4 更干净地隔离 coupling scope。\n4. L14-L18 protection valley pattern 在 Mistral 和 Qwen 上是否也出现？\n5. Table 4 中 BCE+Gumbel+Penalty (38.02) 比无 penalty (32.22) 更差——为什么 sparsity penalty 让 BCE 恶化？\n6. Qwen-2.5-14B 的 d_ff=18944 vs LLaMA 14336——predictor bottleneck d_b=128 是否应随 scale 调整？\n\n---\n\n## Missing References\n\n1. **MaskLLM** (Fang et al., NeurIPS 2024): 已引用讨论但应在 Table 1 taxonomy 中体现位置（Static × Coupled 格）。[R1, R2 共识]\n2. **ActTail** (arXiv:2603.12272, March 2026): 基于 HT-SR 理论的全局 activation sparsity allocation，与 per-layer allocation 分析相关。[R2 提出，R1 认为 2 个月前 arXiv 预印本不应作为 Should-Fix，降为 info]\n3. **CATS** (Lee et al., 2024): §2 提到但 Table 2 未作为 baseline。[R1 提出]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未启用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**done**（耗时 ~3.5 分钟）\n\n### 发现摘要\n- **Critical**: 0\n- **Warning**: 1 — Page 6（§4.1-4.2 开头）整页纯文字，无任何 display item，位于 Table 1 和 Tables 2-3 之间，视觉节奏中断。建议调整 float 位置使 Table 2 提前。\n- **Info**: 18 — 整体排版质量良好；Figure 1 架构图字号偏小但可读；Table 2 字号偏小但可读；Appendix page 17 密度最高但作为附录可接受；Figure 2 轴标签清晰且色盲友好；Section 5 heading 未孤悬；Limitations 简洁符合 EMNLP 要求。\n- **页数合规**: 视觉审查 Agent 确认 Limitations/Ethics/References 在第 9 页开始，主文约 8 页。但 R2 指出 Conclusion 可能有 1-2 行溢出到第 9 页，需核实 LaTeX 编译结果。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 / 5 — Borderline Conference  \n**置信度**: 4 / 5\n\n### 评分理由\n\n**会议门槛因素（积极）**：\n- PPL 改善显著（14.5%–82%）、跨架构一致、3-seed 高置信度——这是一个 robust 的实证发现\n- C1 target-swap ablation 是一个有创意且有信息量的实验设计\n- 实验覆盖面在该方向上属于最全面之列\n- 论文对局限性的主动披露体现了学术诚信\n- Compensation 冗余性发现有实际工程价值\n\n**会议门槛因素（消极）**：\n- 核心分析贡献（signal type vs coupling scope 分解）在 50% 下完全失效，方法论可靠性不足以支撑 Abstract/Conclusion 中的 claim 强度\n- 知识任务系统性退步（跨规模恶化 15 倍）与 \"primary design dimension\" 的强 claim 之间存在根本张力，机制分析停留在假设层面\n- 方法新颖性有限——核心组件（KL、Gumbel-Sigmoid、MLP predictor）均为成熟技术，主要贡献是成熟组件在新场景的应用\n- 无实际推理加速（+6.4% overhead），限制实用影响\n\n### 改进路径\n\n**达到 Conference（4.0）所需**：\n1. 分解 claim 限定为 30% + 更干净的 deconfounding（stop-gradient 或更多 K 值）\n2. Abstract/Conclusion 量化知识任务退步并限定 \"primary design dimension\" 适用范围\n3. Mixed-domain training 验证数据偏差假设，或 knowledge neuron probe 验证 mode-covering 假设\n\n**当前适合 Findings（3.0-3.5）**：\n论文作为 empirical study 的价值在 Findings 层面是明确的——它是该方向首个系统性实证研究，实验可信度高，负面发现（知识退步、分解失效）本身也有信息量。核心 claim 的过度表述和分解实验的方法论问题是阻碍 Conference 的主要因素。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Line 18: \"This paper is primarily an empirical study\" 定位准确，但应更早出现（当前在 contribution list 之后）\n- \"stable downstream (MMLU 40.7±1.3%)\" 易误读——应改为 \"low cross-seed variance\"\n- 68% divergence 和 32% Jaccard 同句出现为互补度量，建议统一\n\n### §3 Method\n- §3.4 \"forward KL outperforms reverse KL by 8.6% and JSD by 6.4%\"：来自 50%，应标注 sparsity level\n- §3.6 Gradient analysis 提供良好直觉，SNR 分析结论自洽（KL SNR 更低但 mask 更好）\n- §3.7 Taxonomy Table 1: Static × Coupled 应纳入 MaskLLM\n\n### §4 Experiments\n- §4.2 Knowledge-Task Regression 两个假设均为推测——至少需一个控制实验（mixed-domain 或 neuron probe）\n- §4.4 C1 ablation 核心结论（mask patterns transfer）稳健；soft-vs-hard confound 影响 why 而非 whether\n- §4.5 Per-layer KL decomposition 在 30% 可解释，50% 失效应更显著标注\n- Table 2 条件不统一增加阅读负担\n- Table 4 Forward KL vs JSD 在 30% 仅 0.09pp，divergence 选择在 moderate sparsity 下更接近 implementation detail\n\n### §5 Conclusion\n- 可能溢出第 8 页 1-2 行——需核实并修复\n\n### Limitations\n- 覆盖全面（sparsity sweet spot, knowledge regression, training data homogeneity, seq length, batched inference, generation evaluation）\n- R26 新增建议：讨论 14B regression 加剧对 70B+ scalability 的影响（已包含）\n\n### Appendix\n- 约 11 页，覆盖极为充分\n- Appendix P (Oracle Provenance): s42 oracle 来自 earlier checkpoint 应在正文 Table 3 更显著标注"
  }
}
```

</details>

---


### Tool result

_source line 2109 · 2026-05-23T01:46:03.471211+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbbf8d2c695f1e79e11713aebc107790:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4117
}
```

</details>

---


### Assistant

_source line 2110 · 2026-05-23T01:46:14.746996+00:00_

审稿报告已投递至 Research Director。

**Round 26 审稿完成总结：**

- **Overall**: 3.5 / 5 (Borderline Conference)
- **2 个 Critical Must-Fix**（两位 Reviewer 完全共识）：
  1. Signal type/coupling 分解在 50% 下失效，Abstract/Conclusion claim 限定不足
  2. 知识任务退步（14B GSM8K −20pp）机制分析不足，"primary design dimension" overclaim
- **7 个 Should-Fix**：downstream 统计力、Table 2 条件不统一、C1 soft-vs-hard confound、MaskLLM taxonomy 遗漏、14.5% 基准不一致、Qwen-14B 不完整、无实际加速（R1/R2 分歧后裁定为 warning）
- **8 个 Minor**：术语一致性、措辞、页数合规等
- **视觉审查**：已完成，0 critical / 1 warning / 18 info
- **Issue Tracker**：已同步更新（review_issues.yaml）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 184

## Round 184

2 recorded events


### User

_source line 2111 · 2026-05-23T01:46:17.359530+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

要点概括：
- R2 的两个 Must-Fix（N1 分解 confound、N2 知识任务退步）与我的 N2、N1 高度一致，均标注 [AGREE]
- 5 个 Should-Fix 中 4 个 [AGREE]（MaskLLM taxonomy、baseline 引用不一致、标题 framing、C1 soft-hard confound），1 个 [REBUT]（ActTail 引用——2 个月前的 arXiv 预印本不应作为 Should-Fix）
- 7 个 Minor 中 6 个 [AGREE]，1 个 [REBUT]（M5 页数溢出实质上是格式微调问题，不影响评分）
- 两份审稿核心判断一致：论文 PPL 贡献扎实，但 decomposition claim 需弱化、知识退步需量化限定、Findings 级别接收合理

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2112 · 2026-05-23T01:46:34.996376+00:00_

审稿报告已投递至 Research Director。

**Round 26 审稿完成。** 最终评分 **3.5 / 5 — Borderline Conference**，两位 Reviewer 评分一致（均 3.5），置信度 4/5。

**核心发现：**
- **2 个 Critical Must-Fix（完全共识）**：(1) signal type/coupling 分解在 50% 失效但 claim 限定不足；(2) 知识任务系统退步（14B GSM8K −20pp）机制分析不足，与 "primary design dimension" claim 矛盾
- **7 个 Should-Fix**：downstream 统计力不足、Table 2 条件不统一、C1 soft-vs-hard confound、MaskLLM taxonomy 缺位、14.5% 基准不一致、Qwen-14B 评估不完整、无实际加速（R1 升为 critical → R2 rebut → Director 裁定维持 warning）
- **8 个 Minor**：术语不一致、页数可能溢出、措辞精确性等

**改进建议**：达到 Conference（4.0）需 (1) stop-gradient 或更多 K 值的 deconfounding 实验，(2) Abstract/Conclusion 量化知识退步并限定 claim 范围，(3) mixed-domain training 验证数据偏差假设。当前质量适合 Findings。

Issue Tracker 已同步更新（`artifacts/review_issues.yaml`）。视觉审查已完成（0 critical, 1 warning）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 185

## Round 185

50 recorded events


### User

_source line 2113 · 2026-05-23T07:17:00.207355+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: distill_sparse_swiglu
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR May 2026)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2114 · 2026-05-23T07:17:05.388276+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2115 · 2026-05-23T07:17:05.439293+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2116 · 2026-05-23T07:17:13.341218+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,WebSearch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2117 · 2026-05-23T07:17:13.391756+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2118 · 2026-05-23T07:17:15.750814+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2119 · 2026-05-23T07:17:15.801395+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2120 · 2026-05-23T07:17:23.075867+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2121 · 2026-05-23T07:17:23.126581+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2122 · 2026-05-23T07:17:28.130530+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 2123 · 2026-05-23T07:17:29.535853+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (392 个)\n\n- **eval_spon_supp_retry**: DONE (failed) — \n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| perlayer_kl_k2_s42_train | K=2 per-layer KL at 30% sparsity: training with 2 random layers per step. Part of K-curve. K=2 tests minimal cross-layer interaction vs pure per-layer (K=1). | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **perlayer_kl_k2_s42_eval** (success): K=2 predictor eval at 30% TEAL uniform: part of K-curve. Uses Reviewer-verified nohup command pattern. ← 基于 perlayer_kl_k2_s42\n- **perlayer_kl_k16_eval_final2** (success): K=16 eval final attempt using Reviewer-verified command. Exact nohup command with all offline env vars and HF_HOME. ← 基于 perlayer_kl_k16_s42_v3\n- **perlayer_kl_k2_s42** (success): K=2 per-layer KL training masks 2/32 layers per step. Tests whether minimal per-step layer coverage (K=2) still learns effective sparse predictors via cumulative exposure across steps.\n\n## 趋势\n成功 245 / 负向 24 / 失败 39 / 共 390\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-34887: 无 GPU 信息\n\n## 告警\n- mvp_kl_s123: 已被终止 — unknown\n- mvp_kl_s456: 已被终止 — unknown\n- kl_lagrangian_v2: 已被终止 — unknown\n- kl_normalized_quicktest: 训练失败 — unknown\n- mvp_kl_norm_s42: 训练失败 — unknown\n- mvp_kl_norm_s123:
…[truncated 1803 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 2124 · 2026-05-23T07:17:29.536266+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 2125 · 2026-05-23T07:17:30.590340+00:00_

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
16	\usepackage{subcaption}
17	
18	\setlength{\textfloatsep}{8pt plus 2pt minus 2pt}
19	\setlength{\floatsep}{8pt plus 2pt minus 2pt}
20	\setlength{\intextsep}{8pt plus 2pt minus 2pt}
21	
22	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\begin{abstract}
30	\input{abstract}
31	\end{abstract}
32	
33	\input{introduction}
34	\input{related_work}
35	\input{method}
36	\input{experiments}
37	\input{conclusion}
38	\input{limitations}
39	\input{ethics}
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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool call

_source line 2126 · 2026-05-23T07:17:30.590663+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR May 2026"
  }
}
```

</details>

---


### Tool call

_source line 2127 · 2026-05-23T07:17:31.494195+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 2128 · 2026-05-23T07:17:31.645524+00:00_

issues:
  # ============================================================
  # Round 26 (Fresh Review) — Active issues
  # ============================================================

  - id: "R20-W1"
    summary: "Per-layer KL decomposition 的 train-inference mismatch confound 未解决"
    category: method
    severity: critical
    status: in_progress
    first_raised_round: 20
    last_seen_round: 26
    mentions:
      - {round: 21, reviewers: [1, 2], note: "R21 Critical。K=4 single-seed。"}
      - {round: 22, reviewers: [1, 2], note: "R22 N2。97.5% 精确数字不可靠。"}
      - {round: 24, reviewers: [1, 2], note: "R24 C1。K=1 有 32× train-inference mismatch；K=4 在 50% 反常差于 K=1；仅两个 K 值不足支撑分解。"}
      - {round: 25, reviewers: [1, 2], note: "R25 N1/N2。K=4 at 50% 反常仍仅 speculation。MMLU K=4 > E2E anomaly 暴露 allocation confound。"}
      - {round: 26, reviewers: [1, 2], note: "R26 R1-N2/R2-N1 完全共识。核心问题不变：(1) K=1 同时改变 coupling 和 train-inference mismatch (1/32 vs 32/32)；(2) K=4 在 50% PPL=44.23 > K=1 34.85，论文自承 unreliable；(3) K=4 MMLU anomaly (42.7>40.7) 暴露 allocation confound (near-uniform std=0.003 ≈ remove-valley)。Abstract 已加 'upper bound; not fully orthogonal' qualifier 但 'accounts for the majority' 仍为较强表述。两位 reviewer 建议 stop-gradient 实验或增加更多 K 值。"}
    action_items:
      - {round: 21, action: "K=4 3-seed (s42/s123/s456)", assigned_to: "main_agent", status: done}
      - {round: 22, action: "97.5% → 定性 'majority of PPL gap'", assigned_to: "paper_agent", status: done}
      - {round: 22, action: "K=4 50% s42 PPL-only 实验", assigned_to: "main_agent", status: done}
      - {round: 24, action: "Abstract/Conclusion 删除精确百分比改为定性", assigned_to: "paper_agent", status: done}
      - {round: 24, action: "K=4 50% 反常结果补假设性解释", assigned_to: "paper_agent", status: done}
      - {round: 25, action: "限定 decomposition 结论适用范围为 moderate sparsity (30%)", assigned_to: "paper_agent", status: done}
      - {round: 25, action: "正文 §4.5 明确讨论 allocation confound", assigned_to: "paper_agent", status: done}
      - {
…[truncated 16299 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool result

_source line 2129 · 2026-05-23T07:17:37.271145+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR May 2026"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting"}]

I've found comprehensive information about EMNLP 2026 call for papers submission guidelines related to the ARR May 2026 cycle. Here are the key details:

## Key Submission Guidelines

EMNLP 2026 invites the submission 
…[truncated 1357 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 6680
}
```

</details>

---


### Tool call

_source line 2130 · 2026-05-23T07:18:03.466840+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2131 · 2026-05-23T07:18:04.420691+00:00_

1	Learned sparsity predictors for SwiGLU LLMs predominantly use binary cross-entropy (BCE), training each neuron independently, yet inference allocates budgets globally via top-$k$ ranking.
2	We train lightweight predictors ($<$1\% of base parameters) with forward KL divergence, coupling all mask decisions through the output distribution.
3	On LLaMA-3.1-8B at 30\% sparsity, the KL predictor reduces perplexity by 14.5\% over TEAL at matched sparsity, with commonsense gains but knowledge-intensive regression (MMLU $-$5.2pp on 8B; GSM8K $-$20.1pp on 14B); post-hoc compensation (+67.2M params) becomes redundant.
4	Output-distribution optimization yields masks that diverge 46--68\% from magnitude-based targets; a target-swap ablation suggests these discovered patterns carry most of the quality information: BCE trained on KL-derived targets approaches KL-level PPL (PPL gap $\leq$0.65pp; 3-seed, 30\%).
5	Signal type (output-distribution vs.\ intermediate loss) accounts for the majority of the PPL gap at moderate sparsity (30\%) (upper bound; \S\ref{sec:perlayer}).
6	On downstream tasks, cross-layer coupling contributes substantially for commonsense reasoning but minimally for mathematical reasoning (3-seed $K{=}4$-corrected decomposition).
7	Cross-architecture evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms PPL generalization with scale-dependent downstream effects.
8	This is primarily an empirical study; wall-clock speedup requires sparse kernel support not addressed here.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 2132 · 2026-05-23T07:18:04.421134+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2133 · 2026-05-23T07:18:04.923229+00:00_

1	\section{Introduction}
2	
3	How the training objective shapes learned sparsity prediction quality is an open question for SwiGLU LLMs~\cite{shazeer2020glu}. SwiGLU FFN blocks exhibit high contextual sparsity, but their gated activation makes importance prediction challenging: neuron importance depends on both gate and up-projection values, a target that magnitude-based methods handle suboptimally.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they predominantly rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: the TEAL (training-free activation sparsity;~\citealp{liu2025teal}) top-$k$ mechanism ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	Unlike MaskLLM~\cite{fang2024maskllm}, which applies KL to static N:M weight masks, we address contextual activation sparsity where masks must generalize to unseen inputs, vary per token, and coordinate across layers through global allocation.
8	
9	Gradient analysis reveals a structural asymmetry: BCE's gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$ depends only on neuron $j$, while under KL divergence, the gradient couples each neuron to all others through the downstream Jacobian (\S\ref{sec:method:gradient}).
10	KL's coupled gradients discover neuron importance patterns that diverge 68\% from magnitude-based masks (per-layer Jaccard 32\%).
11	A target-swap ablation shows KL-discovered mask targets carry most of the quality information: BCE retrained on KL-derived targets approaches KL PPL ($\leq$0.65pp gap, 3-seed), while magnitude-trained BCE yields 28.13$\pm$0.20. Coupling contributes marginally to PPL but m
…[truncated 3023 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2134 · 2026-05-23T07:18:04.923583+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2135 · 2026-05-23T07:18:05.375434+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models (Figure~\ref{fig:overview}).
5	The method replaces per-neuron binary classification (BCE) with an output-distribution alignment objective that couples all pruning decisions through the model's forward pass and achieves competitive performance without auxiliary error compensation networks at inference.
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
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{x}^{(\ell)}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuro
…[truncated 9816 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 2136 · 2026-05-23T07:18:05.375767+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2137 · 2026-05-23T07:18:05.985433+00:00_

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
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4 on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB), using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $1 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), GSM8K (8-shot), HellaSwag (10-shot), and PIQA (0-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly\footnote{TEAL is deterministic; single-run evaluation suffices. KL/BCE predictors require multi-seed evaluation due to random initialization.}; (2) \textbf{BCE predictor} (Deja
…[truncated 17617 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 609
}
```

</details>

---


### Tool call

_source line 2138 · 2026-05-23T07:18:06.326108+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2139 · 2026-05-23T07:18:06.326513+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} and GRASP~\cite{shin2025grasp} predict activation sparsity patterns without additional training.
6	LaRoSA~\cite{huang2025larosa} applies layerwise orthogonal rotations for structured activation sparsity with wall-clock speedup on SiLU models.
7	Wang et al.~\cite{wang2025dynamicsparse}, AWQ~\cite{lin2024awq}, and Outlier Suppression+~\cite{wei2023outlier} address sparsity--quantization interactions and activation-aware quantization.
8	Dhar et al.~\cite{dhar2024activation} characterize activation sparsity opportunities across architectures, showing that SwiGLU models exhibit lower natural sparsity than ReLU counterparts.
9	OWL~\cite{yin2024owl} determines per-layer sparsity ratios from outlier distributions for weight pruning.
10	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
11	
12	\paragraph{Predictor-Based Contextual Sparsity.}
13	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
14	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
15	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
16	SVD-CSP~\cite{serbin2026svdcsp} compre
…[truncated 5041 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2140 · 2026-05-23T07:18:06.376932+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2141 · 2026-05-23T07:18:06.828935+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Output-distribution alignment is the primary design dimension at moderate sparsity: signal type accounts for most of the PPL gap (upper bound), with coupling contributing task-dependently (Appendices~\ref{app:k4_downstream},~\ref{app:constraint}).
5	A $<$1\% predictor reduces TEAL's PPL by 14.5\% via masks 46--68\% divergent from magnitude; commonsense gains but knowledge regression persist across 7--14B scales.
6	Code and trained predictors will be released upon acceptance.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2142 · 2026-05-23T07:18:06.829292+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 2143 · 2026-05-23T07:18:07.281279+00:00_

1	\section*{Limitations}
2	
3	Our findings are bounded by three key limitations.
4	\textbf{Sparsity sweet spot.} 30\% appears to be the lowest-degradation level for downstream fidelity; at 40\%, MMLU drops to 35.5\% (vs.\ 40.7\% at 30\%), and at 50\%, all methods collapse to near-random on reasoning tasks. A separate predictor must be retrained per target.
5	\textbf{Knowledge-intensive regression.} KL consistently underperforms magnitude-based methods on MMLU and GSM8K across scales (8B: $-$5.2pp MMLU; 14B: $-$20pp GSM8K), suggesting distribution-matching objectives systematically sacrifice reasoning-critical pathways.
6	\textbf{Training data homogeneity.} All predictors are trained on WikiText-103 (English Wikipedia). OOD evaluation on C4 shows preserved KL advantage but $31\times$ higher cross-seed variance (CV=6.3\% vs.\ 0.2\% in-domain), indicating domain sensitivity. Batched inference, where sparsity patterns must be intersected across sequences, may reduce effective sparsity and is not evaluated. All experiments use sequence length 2048; behavior at longer contexts (e.g., 8K--128K) is untested. Our evaluation focuses on perplexity and multiple-choice benchmarks; open-ended generation quality (e.g., MT-Bench) remains untested and may exhibit different sparsity sensitivity. The aggravation from 8B to 14B (GSM8K regression deepening from $-$1.3pp to $-$20.1pp) raises concern about scaling to 70B+; wall-clock speedup via sparse kernels also remains future work.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 2144 · 2026-05-23T07:18:07.281598+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 2145 · 2026-05-23T07:18:08.636926+00:00_

1	\section*{Ethics Statement}
2	
3	This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3, Qwen-2.5-14B~\cite{qwen2024qwen25}) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, HellaSwag, PIQA, MMLU, GSM8K).
4	No new data collection, annotation, or human subjects are involved.
5	The method does not alter model outputs beyond the sparsity-induced degradation we analyze; it introduces no new generation capabilities or safety risks beyond those inherent in the base models.
6	Compute requirements are modest (1000 training steps, $\sim$45 minutes on a single GPU for KL training), presenting minimal environmental concern relative to the pretrained models we evaluate on.
7	We release no model weights or user-facing systems; our contribution is analytical (understanding KL distillation for sparsity) rather than deployment-oriented.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 1355
}
```

</details>

---


### Tool call

_source line 2146 · 2026-05-23T07:18:08.637405+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 2147 · 2026-05-23T07:18:09.190826+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB; batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
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
33	The pipeline adds $\sim$6.4\% overhead
…[truncated 40197 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 2148 · 2026-05-23T07:18:09.191292+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 2149 · 2026-05-23T07:18:10.195923+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (392 个)\n\n- **eval_spon_supp_retry**: DONE (failed) — \n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| perlayer_kl_k2_s42_train | K=2 per-layer KL at 30% sparsity: training with 2 random layers per step. Part of K-curve. K=2 tests minimal cross-layer interaction vs pure per-layer (K=1). | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **perlayer_kl_k2_s42_eval** (success): K=2 predictor eval at 30% TEAL uniform: part of K-curve. Uses Reviewer-verified nohup command pattern. ← 基于 perlayer_kl_k2_s42\n- **perlayer_kl_k16_eval_final2** (success): K=16 eval final attempt using Reviewer-verified command. Exact nohup command with all offline env vars and HF_HOME. ← 基于 perlayer_kl_k16_s42_v3\n- **perlayer_kl_k2_s42** (success): K=2 per-layer KL training masks 2/32 layers per step. Tests whether minimal per-step layer coverage (K=2) still learns effective sparse predictors via cumulative exposure across steps.\n\n## 趋势\n成功 245 / 负向 24 / 失败 39 / 共 390\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-34887: 无 GPU 信息\n\n## 告警\n- mvp_kl_s123: 已被终止 — unknown\n- mvp_kl_s456: 已被终止 — unknown\n- kl_lagrangian_v2: 已被终止 — unknown\n- kl_normalized_quicktest: 训练失败 — unknown\n- mvp_kl_norm_s42: 训练失败 — unknown\n- mvp_kl_norm_s123:
…[truncated 1803 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 2150 · 2026-05-23T07:18:10.447845+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 2151 · 2026-05-23T07:18:10.548572+00:00_

-rw-r--r-- 1 ubuntu ubuntu 545948 May 23 07:15 /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2152 · 2026-05-23T07:19:10.191711+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "distill_sparse_swiglu",
  "text": "你是 Reviewer 1，负责审查论文的 **方法严谨性 + 实验设计**。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR May 2026 提交）\n- **截止日期**: 2026-05-25\n- **格式要求**: ACL 模板，Long Paper 正文上限 8 页（不含 references 和 limitations/ethics）\n- **匿名规则**: Double-blind\n- **评分标准**: ARR Overall Assessment (1-5 scale)，其中 4 = Conference（可被主会议接收），3 = Findings\n\n## 论文文件\n- LaTeX 源文件: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/submitted.pdf`\n- 图表目录: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/figures/paper/`\n\n## 你的审查侧重\n\n**核心关注点**：\n1. **Per-layer KL 分解的实验有效性**：K=1 的 train-inference mismatch (1/32 vs 32/32) 是否污染了 \"signal type accounts for majority\" 的结论？K=4 correction 是否充分？K-curve 数据（多数 single-seed）的统计可靠性。\n2. **C1 target-swap ablation 的 confound 控制**：soft→hard mask binarization 是否引入 representation confound？s42 oracle 来自 earlier checkpoint 的影响。BCE+Gumbel(32.22) vs BCE(27.97) 的解释是否充分？\n3. **统计严谨性**：3-seed 下游指标的置信区间是否足以支撑方向性结论（MMLU 30% global σ=9.5）？PPL 作为 primary metric 的合理性论证。\n4. **Table 2 对比公平性**：BCE 30% uniform vs KL 的对比条件是否充分控制（steps、allocation）？BCE 50% 用 2700 steps 的 iso-compute 论证。\n5. **Knowledge-task regression 的机制分析**：跨架构/跨 scale 一致退步（8B MMLU -5.2pp, 14B GSM8K -20pp）的解释是否充分？C4 控制实验的结论是否 over-interpreted？\n6. **实验覆盖度**：缺少生成任务评估、seq_len 固定 2048、无 batched inference。Limitations 覆盖是否充分？\n\n**输出格式**：\n- Strengths（逐条，带证据）\n- Weaknesses（逐条，按 Must-Fix / Should-Fix / Minor 分级，引用具体 Section/Table/Figure）\n- Questions（需要作者回答的问题）\n- Missing References（如有）\n- Overall Assessment（1-5 ARR scale + 简短理由）\n- Confidence（1-5）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "distill_sparse_swiglu",
    "text": "你是 Reviewer 1，负责审查论文的 **方法严谨性 + 实验设计**。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR May 2026 提交）\n- **截止日期**: 2026-05-25\n- **格式要求**: ACL 模板，Long Paper 正文上限 8 页（不含 references 和 limitations/ethics）\n- **匿名规则**: Double-blind\n- **评分标准**: ARR Overall Assessment (1-5 scale)，其中 4 = Conference（可被主会议接收），3 = Findings\n\n## 论文文件\n- LaTeX 源文件: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/submitted.pdf`\n- 图表目录: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/figures/paper/`\n\n## 你的审查侧重\n\n**核心关注点**：\n1. **Per-layer KL 分解的实验有效性**：K=1 的 train-inference mismatch (1/32 vs 32/32) 是否污染了 \"signal type accounts for majority\" 的结论？K=4 correction 是否充分？K-curve 数据（多数 single-seed）的统计可靠性。\n2. **C1 target-swap ablation 的 confound 控制**：soft→hard mask binarization 是否引入 representation confound？s42 oracle 来自 earlier checkpoint 的影响。BCE+Gumbel(32.22) vs BCE(27.97) 的解释是否充分？\n3. **统计严谨性**：3-seed 下游指标的置信区间是否足以支撑方向性结论（MMLU 30% global σ=9.5）？PPL 作为 primary metric 的合理性论证。\n4. **Table 2 对比公平性**：BCE 30% uniform vs KL 的对比条件是否充分控制（steps、allocation）？BCE 50% 用 2700 steps 的 iso-compute 论证。\n5. **Knowledge-task regression 的机制分析**：跨架构/跨 scale 一致退步（8B MMLU -5.2pp, 14B GSM8K -20pp）的解释是否充分？C4 控制实验的结论是否 over-interpreted？\n6. **实验覆盖度**：缺少生成任务评估、seq_len 固定 2048、无 batched inference。Limitations 覆盖是否充分？\n\n**输出格式**：\n- Strengths（逐条，带证据）\n- Weaknesses（逐条，按 Must-Fix / Should-Fix / Minor 分级，引用具体 Section/Table/Figure）\n- Questions（需要作者回答的问题）\n- Missing References（如有）\n- Overall Assessment（1-5 ARR scale + 简短理由）\n- Confidence（1-5）"
  }
}
```

</details>

---


### Tool result

_source line 2153 · 2026-05-23T07:19:25.468986+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15277
}
```

</details>

---


### Tool call

_source line 2154 · 2026-05-23T07:19:25.619870+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "distill_sparse_swiglu",
  "text": "你是 Reviewer 2，负责审查论文的 **新颖性 + 完整性 + 写作质量**。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR May 2026 提交）\n- **截止日期**: 2026-05-25\n- **格式要求**: ACL 模板，Long Paper 正文上限 8 页（不含 references 和 limitations/ethics）\n- **匿名规则**: Double-blind\n- **评分标准**: ARR Overall Assessment (1-5 scale)，其中 4 = Conference（可被主会议接收），3 = Findings\n\n## 论文文件\n- LaTeX 源文件: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/submitted.pdf`\n- 图表目录: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/figures/paper/`\n\n## 你的审查侧重\n\n**核心关注点**：\n1. **新颖性边界**：与 MaskLLM 共享核心 recipe (frozen weights + learnable masks + KL + Gumbel)。三点区分（contextual vs static, global allocation, distribution shift robustness）是否足够？Table 1 taxonomy 分类是否准确（Static×Coupled 仅列 SPON 和 MaskLLM 是否遗漏）？\n2. **Contribution framing**：自称 \"empirical study\"，但 contribution list 包含方法创新暗示（output-distribution alignment ranking, target-swap ablation）。定位是否一致？\"primary design dimension\" claim 的适用范围是否充分限定？\n3. **写作质量**：\n   - 术语一致性：output-distribution alignment / distillation / objective 是否交替使用？\n   - Abstract 信息密度：是否过度压缩导致误读？14.5% PPL 的引用基准是否清晰？\n   - 数字呈现：68% divergence vs 32% Jaccard 是否同句混淆？\n   - \"stable downstream\" 等措辞是否可能误导？\n4. **Related Work 完整性**：是否遗漏重要 2025-2026 近期工作？尤其是：\n   - Contextual sparsity prediction 领域的新方法\n   - KL distillation 在 structured pruning 中的应用\n   - 与本文高度相关但未引用的工作\n5. **格式合规**：8 页正文限制、ACL 模板、匿名性、References 格式、Appendix 规范\n6. **Limitations 和 Ethics 覆盖度**：是否充分讨论了方法的局限性？\n\n**输出格式**：\n- Strengths（逐条，带证据）\n- Weaknesses（逐条，按 Must-Fix / Should-Fix / Minor 分级，引用具体 Section/Table/Figure）\n- Questions（需要作者回答的问题）\n- Missing References（如有，搜索 2025-2026 相关工作）\n- Excitement（1-5 scale + 简短理由）\n- Overall Assessment（1-5 ARR scale + 简短理由）\n- Confidence（1-5）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "distill_sparse_swiglu",
    "text": "你是 Reviewer 2，负责审查论文的 **新颖性 + 完整性 + 写作质量**。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR May 2026 提交）\n- **截止日期**: 2026-05-25\n- **格式要求**: ACL 模板，Long Paper 正文上限 8 页（不含 references 和 limitations/ethics）\n- **匿名规则**: Double-blind\n- **评分标准**: ARR Overall Assessment (1-5 scale)，其中 4 = Conference（可被主会议接收），3 = Findings\n\n## 论文文件\n- LaTeX 源文件: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/submitted.pdf`\n- 图表目录: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/figures/paper/`\n\n## 你的审查侧重\n\n**核心关注点**：\n1. **新颖性边界**：与 MaskLLM 共享核心 recipe (frozen weights + learnable masks + KL + Gumbel)。三点区分（contextual vs static, global allocation, distribution shift robustness）是否足够？Table 1 taxonomy 分类是否准确（Static×Coupled 仅列 SPON 和 MaskLLM 是否遗漏）？\n2. **Contribution framing**：自称 \"empirical study\"，但 contribution list 包含方法创新暗示（output-distribution alignment ranking, target-swap ablation）。定位是否一致？\"primary design dimension\" claim 的适用范围是否充分限定？\n3. **写作质量**：\n   - 术语一致性：output-distribution alignment / distillation / objective 是否交替使用？\n   - Abstract 信息密度：是否过度压缩导致误读？14.5% PPL 的引用基准是否清晰？\n   - 数字呈现：68% divergence vs 32% Jaccard 是否同句混淆？\n   - \"stable downstream\" 等措辞是否可能误导？\n4. **Related Work 完整性**：是否遗漏重要 2025-2026 近期工作？尤其是：\n   - Contextual sparsity prediction 领域的新方法\n   - KL distillation 在 structured pruning 中的应用\n   - 与本文高度相关但未引用的工作\n5. **格式合规**：8 页正文限制、ACL 模板、匿名性、References 格式、Appendix 规范\n6. **Limitations 和 Ethics 覆盖度**：是否充分讨论了方法的局限性？\n\n**输出格式**：\n- Strengths（逐条，带证据）\n- Weaknesses（逐条，按 Must-Fix / Should-Fix / Minor 分级，引用具体 Section/Table/Figure）\n- Questions（需要作者回答的问题）\n- Missing References（如有，搜索 2025-2026 相关工作）\n- Excitement（1-5 scale + 简短理由）\n- Overall Assessment（1-5 ARR scale + 简短理由）\n- Confidence（1-5）"
  }
}
```

</details>

---


### Tool result

_source line 2155 · 2026-05-23T07:19:27.437166+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1817
}
```

</details>

---


### Tool call

_source line 2156 · 2026-05-23T07:19:27.437538+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
  }
}
```

</details>

---


### Tool call

_source line 2157 · 2026-05-23T07:19:27.638745+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 2158 · 2026-05-23T07:19:29.051810+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 1614
}
```

</details>

---


### Tool result

_source line 2159 · 2026-05-23T07:19:29.054236+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1415
}
```

</details>

---


### Tool call

_source line 2160 · 2026-05-23T07:19:42.226436+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 2161 · 2026-05-23T07:19:42.277122+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/decisions.yaml\", \"content\": \"_next_id: 108\\ndecisions:\\n- id: D001\\n  date: 2026-05-15 10:07 UTC\\n  summary: 'MVP 设计: KL vs BCE predictor 在 50% sparsity 下的 perplexity 对比'\\n  rationale: '核心假设是 KL 训练通过端到端梯度捕获联合神经元交互，优于 BCE 的逐神经元独立目标。MVP 聚焦最基础的 A/B 对比（KL vs\\n    BCE），不涉及 SPON 组合或 compensation network，以最小成本验证核心假设是否成立。Pass criteria: KL ppl <\\n    BCE ppl 差距 ≥ 0.3。评审笔记中的 novelty ceiling 和 effect size 风险恰好需要 MVP 先确认效果量级。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-15 12:08 UTC\\n  summary: 校准数据从 SlimPajama-627B 改为 WikiText-103 train split\\n  rationale: SlimPajama-627B 在 AutoDL 代理环境下 HF datasets API 无法访问（DatasetNotFoundError）。WikiText-103\\n    (~100M tokens) 满足 MVP 1K steps 需求，KL/BCE 用同一数据保证公平性。偏离 IDEA_BRIEF 原始方案，full paper\\n    实验阶段可能需要切回更多样的校准数据。\\n  related_experiments:\\n  - exp_id: mvp_kl_s42\\n    role: affected\\n    result: FAILED due to SlimPajama access\\n  - exp_id: mvp_bce_s42\\n    role: affected\\n    result: FAILED due to SlimPajama access\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-15 13:16 UTC\\n  summary: KL 训练稀疏性坍塌至 0%，改用 Lagrangian multiplier 替代固定 reg_weight\\n  rationale: mvp_kl_s42 的 sparsity 从 0.328 单调降至 0.000。KL loss 天然在 0% sparsity 处最小，固定\\n    reg_weight=0.1 被 KL loss（66 倍量级差）完全压制。Lagrangian multiplier 通过 dual gradient ascent\\n    自动调整约束强度，是约束优化的标准方案。暂停 KL s123/s456 直到修复验证通过。\\n  related_experiments:\\n  - exp_id: mvp_kl_s42\\n    role: evidence\\n    result: sparsity collapsed to 0%, KL=3.3 vs reg=0.05\\n  depends_on:\\n  - D001\\n- id: D004\\n  date: 2026-05-15 13:34 UTC\\n  summary: KL 稀疏性坍塌修复：选方案 C（KL loss 归一化 + 激进 Lagrangian），保持纯 KL 端到端训练\\n  rationale: Lagrangian quicktest 确认 lambda 爬升追不上 KL loss 量级（KL~418 vs constraint~1.2）。根因是\\n    KL 用 sum reduction 导致绝对值过大。归一化到 per-token per-dim 后 KL 应降至 ~0.003，与 constraint\\n    可比。选 C 而非 A（BCE warm-start）因为 
…[truncated 1457 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 2162 · 2026-05-23T07:19:56.784362+00:00_

外部审稿未配置，跳过。

**当前状态汇总**：
- Reviewer 1（方法严谨性 + 实验设计）：审稿进行中
- Reviewer 2（新颖性 + 完整性 + 写作）：审稿进行中
- 视觉审查 Agent：已启动，与 Reviewer 并行
- 外部审稿：未配置，不执行

等待两位 Reviewer 返回 Round 1 独立审稿意见后，进入 Step 2 交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 186

## Round 186

2 recorded events


### User

_source line 2163 · 2026-05-23T07:26:30.440260+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见（Round 1）

**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
**审查侧重**: 新颖性 + 完整性 + 写作质量

---

## 总体评分
**Overall**: 3.0 / 5 (Findings)
**一句话总结**: 扎实的实证研究，提供了 KL > BCE 用于稀疏预测训练的有用发现和精心设计的消融实验，但新颖性主要是已知组件的新组合，知识任务上的系统性退化未获充分解释，且缺乏实际加速验证。

---

## 官方维度打分（ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 (Acceptable) | 主要 claim 有实验支持，但 "primary design dimension" 泛化性不足（主要基于 LLaMA-3.1-8B 30%），知识退化机制仅有假说无因果证据 |
| Excitement | 3/5 (Interesting) | Target-swap ablation 设计巧妙，signal type vs. coupling scope 分解有参考价值，但核心方法是已知技术的直接组合（KL + Gumbel-Sigmoid），实践价值受限于无 wall-clock 加速 |
| Reproducibility | 4/5 | 实验设置详细（超参数、硬件、seed），承诺开源代码，附录含大量补充实验；部分消融仅 single-seed 略有扣分 |
| Confidence | 4/5 | 熟悉 activation sparsity prediction 文献，仔细阅读了全文及全部附录 |

---

## 主要优势

**S1. 精心设计的消融框架**
Target-swap ablation（C1, Table 3）是本文最突出的实验设计贡献：通过在 BCE 上训练 KL 发现的 oracle masks，成功分离了"mask 质量"与"训练机制"的贡献。结果令人信服——C1 在 50% 稀疏度下与 KL 仅差 ≤0.79pp（Section 4.4, Table 3），说明 KL 的优势主要来自发现了更好的 mask patterns。

**S2. Signal type vs. coupling scope 分解**
Per-layer KL 控制实验（K=1, K=4; Section 4.5, Table 4）提供了有价值的分析框架。K=1 per-layer KL 达到 9.05±0.02，仅比 E2E KL（8.81±0.02）差 2.7%，而 per-layer MSE 退化至 18.52±1.68，有力支持了 signal type 是主要因素的论点。

**S3. 诚实的局限性报告**
论文坦诚报告了 KL 在知识密集任务上的系统性退化（MMLU −5.2pp on 8B; GSM8K −20.1pp on 14B; Section 4.2, Limitations），没有选择性报告。下游指标的统计不确定性（3 seeds, CIs overlap）也被明确说明（Section 4.2: "we therefore treat PPL as the primary metric and downstream differences as directional evidence"）。

**S4. 全面的 Related Work**
引用覆盖了 2024-2026 的主要相关工作，包括 SVD-CSP (Serbin et al., 2026)、SparseInfer、ProSparse、SparseLoRA 等近期工作。与 MaskLLM 的区分讨论具体且技术性强（Section 2, three respects a-c）。

**S5. 丰富的附录**
20 页中有 ~8 页附录（Appendix A-W），涵盖推理延迟、训练收敛、温度敏感性、OOD 评估、mask 可视化等，体现了实验严谨性。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] "Primary design dimension" claim 泛化性不足
- 具体位置：Section 5 (Conclusion), Abstract line 5, Section 4.5
- 问题：结论称 "Output-distribution alignment is the primary design dimension at moderate sparsity"，但主要证据来自 LLaMA-3.1-8B 在 30% 稀疏度下的实验。跨架构验证信号混合：Mistral-7B 确认 PPL 优势但 MMLU 持平（Section 4.6: "PPL generalizes but MMLU/GSM8K decline"）；Qwen-2.5-14B 出现严重 GSM8K 退化（−20.1pp）。在论文自己报告的范围内，这个 claim 在知识密集任务上是不成立的——magnitude-based TEAL 在 MMLU/GSM8K 上始终优于 KL predictor（Table 2）。
- 为什么影响接收："primary design dimension" 是本文的核心结论，如果仅在 PPL + commonsense 维度上成立，需要明确限定适用范围。
- 建议修改方向：改为 "primary design dimension *for perplexity and commonsense tasks* at moderate sparsity"，或更保守地 "a dominant factor for PPL" 并讨论为何在知识任务上不成立。

**N2** [critical] 知识任务退化机制缺乏因果解释
- 具体位置：Section 4.2 "Knowledge-Task Regression: Hypothesis", Limitations
- 问题：论文提出两个假说（训练数据偏差、mode-covering 稀释稀有激活），但 C4 控制实验否定了第一个（Section 4.2: "confirming the deficit is structural to distribution-matching"）。第二个假说（mode-covering 稀释 factual knowledge neurons）仅是推测。Constraint experiments（Appendix, remove valley → MMLU +3.4pp）暗示 allocation 而非 loss function 本身是原因，但论文未对此深入追踪。
- 为什么影响接收：对于自称 "empirical study characterizing how the training objective shapes sparsity prediction quality" 的论文，无法解释核心发现中的系统性失败模式是显著的完整性缺陷。
- 建议修改方向：设计针对性实验区分"KL loss 本身导致退化"vs."KL 学到的 allocation 分布导致退化"——例如强制 KL predictor 使用 uniform allocation 并与 constrained allocation 对比 MMLU。（注意：uniform allocation 结果已有，40.7 vs. TEAL 45.86，但未充分分析为何 uniform KL 仍然差 5pp。）

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Contribution framing 存在张力
- 具体位置：Abstract line 8, Introduction line 18 vs. Contribution list (Introduction lines 21-27)
- 问题：论文反复声明 "primarily an empirical study"，但贡献列表包含方法性暗示："output-distribution alignment ranking"（暗示一种新的 ranking 方法）、"target-swap ablation"（一种新的实验范式）。更关键的是，论文实际上引入了一个具体的方法（KL predictor + Gumbel-Sigmoid for contextual sparsity），这不仅仅是"比较现有方法"。
- 建议：要么承认方法贡献（"we introduce a KL-based training framework and conduct the first systematic empirical comparison..."），要么将贡献列表措辞调整为更明确的实证发现（"We find that..."而非 "An output-distribution alignment ranking..."）。

**W2** [warning] 术语一致性问题
- 具体位置：全文
- 问题：核心概念至少有 5 种表述——"output-distribution distillation"（标题）、"output-distribution alignment"（Abstract, Conclusion）、"output-distribution optimization"（Abstract line 4）、"KL distillation"（Section 3 et passim）、"distribution-matching"（Limitations）。这些是否指同一概念？如果是，应统一为一个首选术语。
- 建议：选定一个主术语（建议 "output-distribution alignment" 或 "KL distillation"），在首次出现时定义并一致使用。

**W3** [warning] Abstract/Introduction 中的数字混淆
- 具体位置：Introduction line 10
- 问题："KL's coupled gradients discover neuron importance patterns that diverge 68% from magnitude-based masks (per-layer Jaccard 32%)"。68% 和 32% 是同一指标的互补面（Jaccard distance vs. Jaccard similarity），在同一句中出现两个数字造成不必要的混淆。
- 建议：统一使用一种表述，例如 "with per-layer Jaccard similarity of only 32%"。

**W4** [warning] MSE baseline 在 50% 稀疏度下不可靠
- 具体位置：Table 4, Section 4.5
- 问题：MSE 50% 报告 PPL 229.26，但脚注 §标注 s123 catastrophic (PPL=15,789)。以此作为 MSE inferiority 的证据（"$2.05\times$ worse"在 30%）是可以的，但 50% 的数字基本不可用。Ablation table 标注了 single-seed，但正文讨论中容易被误解为 robust finding。
- 建议：在正文讨论 MSE 50% 时明确标注单种子，考虑从主 ablation narrative 中降权或移至附录。

**W5** [warning] 3 seeds 下声称 "commonsense gains" 的统计依据不足
- 具体位置：Abstract line 3 ("commonsense gains"), Conclusion line 5, Section 4.2
- 问题：论文在 Section 4.2 中诚实地指出 "95% confidence intervals for individual downstream tasks overlap" 并将下游指标视为 "directional evidence"。但 Abstract 和 Conclusion 中 "commonsense gains" 的措辞没有这一限定，可能误导读者认为这是统计显著的发现。
- 建议：Abstract/Conclusion 中加 qualifier，如 "directional commonsense improvements" 或 "commonsense gains (directional; CIs overlap with 3 seeds)"。

**W6** [warning] Wall-clock speedup 的缺失削弱实际影响力
- 具体位置：Abstract line 8, Introduction line 18, Appendix A, Limitations
- 问题：论文坦承 wall-clock speedup 未测量，predictor 本身增加 6.4% latency（Appendix A）。对于一篇关于"高效推理"sparsity prediction 的论文，这意味着当前方法 *增加* 而非减少延迟。虽然论文正确地 frame 为 analytical contribution，但 reviewer 和读者期望至少有一个 end-to-end 加速的 feasibility 估算。
- 建议：即使没有 sparse kernel 实现，也可以基于已有文献（如 TEAL 的 speedup 数据 × KL 的稀疏度优势）给出理论加速估算。

---

## 小问题（不影响接收）

- **M1**: Table 2 caption 信息过载（3 个脚注标记 *, †, ‡ + 多个解释条款），建议拆分为 caption 和 table note。
- **M2**: Figure 2 caption 中 "82% at 70%" 这个数据点在正文中几乎未讨论，作为 caption 中的信息显得孤立。
- **M3**: Section 3.5 (Geometric Penalty Schedule) 中的 deadzone margin ε=0.02 的选择缺乏 justification（仅在附录中有 sensitivity analysis）。
- **M4**: Introduction line 14 "with downstream (MMLU 40.7±1.3%, 3-seed)" 没有 dense baseline 对比（dense MMLU 65.27%），孤立的数字不传达退化幅度。

---

## Questions（需要作者回答）

**Q1**: 在 50% 稀疏度下，K=4 per-layer KL（44.23）为何 *worse* than K=1（34.85）？论文假说 "partial coupling amplifies gradient interference"，但这与 30% 下 coupling 有益的叙事矛盾。是否存在某个 sparsity threshold 使 coupling 从有益变为有害？

**Q2**: K=4 在 MMLU 上超越 E2E KL（42.7 vs. 40.7, Section 4.5）——这是否意味着对知识任务而言，per-layer 训练反而更优？如果是，这对 "output-distribution alignment is the primary design dimension" 的结论意味着什么？

**Q3**: Uniform allocation 下 KL predictor MMLU = 40.7% vs. TEAL uniform MMLU = 45.86%（Table 2, 30%）。二者都是 uniform allocation，所以 allocation 策略相同。这 5pp 的差距是否完全归因于 KL loss 本身？如果是，这与 "allocation contributes" 的解释（Constraint experiments）矛盾。

**Q4**: Target-swap ablation (C1) 中 s42 oracle 来自 earlier training run (not seed-matched)，而 s123/s456 使用 seed-matched oracles。s42 的 gap (0.65pp) 与 s123/s456 的 gap (≤0.03pp) 差异显著。如何确认 s42 结果不是 oracle provenance artifact？

**Q5**: 论文未测试 reverse KL + Gumbel 在 30% 下的表现（Table 4 标注 "---"）。Forward vs. Reverse KL 在 30% 下的差异（8.81 vs. 9.26）是否有统计显著性？考虑到 JSD≈Forward KL (8.90 vs. 8.81)，30% 下 divergence measure 的选择似乎影响不大。

---

## Missing References

Related Work 覆盖全面，未发现 2025-2026 年的重大遗漏。以下可考虑补充但非必须：

- 无重大遗漏。SVD-CSP (Serbin et al., 2026)、SparseInfer、ProSparse、SparseLoRA、COTS、LaRoSA 等近期工作均已引用。

---

## Novelty 边界评估（Director 指定关注点）

**与 MaskLLM 的区分**：
论文在 Section 2 中清晰区分了三点（a-c: contextual vs static, global allocation, distribution shift robustness），这些是技术上 valid 的区分。Table 1 taxonomy 中 Static×Coupled 仅列 SPON 和 MaskLLM，经查未发现显著遗漏。

**核心问题**：论文的新颖性不在于 KL + Gumbel-Sigmoid 这一 recipe（与 MaskLLM 共享核心组件），而在于 (1) 将其应用于 contextual activation sparsity 这一新领域，以及 (2) 通过 target-swap ablation 和 per-layer KL 控制提供的分析框架。这是 "empirical + analytical" 层面的贡献，而非 "methodological" 层面的突破。对于 Findings track 足够，但对 Main Conference 可能偏弱。

---

## 评分总结

| 指标 | 分数 |
|------|------|
| Overall Assessment | 3.0 (Findings) |
| Soundness | 3/5 |
| Excitement | 3/5 |
| Reproducibility | 4/5 |
| Confidence | 4/5 |

**推荐 Findings 的理由**：论文提供了有价值的实证发现（KL > BCE for sparsity prediction, signal type 是 primary factor），实验设计严谨（target-swap ablation 尤为出色），但新颖性局限于已知组件的新应用，核心 claim 的泛化性不足（仅 PPL + commonsense, 非 knowledge tasks），且缺乏实际加速验证。这些发现对 activation sparsity 社区有参考价值，适合 Findings track。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2164 · 2026-05-23T07:26:46.747275+00:00_

Reviewer 2 审稿意见已收到。评分 3.0（Findings），核心问题集中在 "primary design dimension" 泛化性不足和知识任务退化机制缺乏因果解释。

等待 Reviewer 1 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 187

## Round 187

2 recorded events


### User

_source line 2165 · 2026-05-23T07:26:49.321616+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论**: Overall 3.0 (Findings level)

核心判断：
- **优点**：Target-swap ablation 设计精巧，signal type vs. coupling scope 分解有价值，实验诚实全面
- **主要问题**：(1) "primary design dimension" claim 泛化性不足——知识任务上 TEAL 始终优于 KL predictor；(2) 知识退化的因果机制未解释；(3) 核心方法是已知组件（KL + Gumbel-Sigmoid）的新组合而非方法论突破
- **次要问题**：术语不一致（5 种表述指同一概念）、3 seeds 下 "commonsense gains" 措辞过强、MSE 50% 单种子不可靠、无 wall-clock 加速验证
- **格式合规**：8 页正文限制 ✓，ACL 模板 ✓，匿名性 ✓，Limitations/Ethics ✓

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2166 · 2026-05-23T07:26:59.145175+00:00_

Reviewer 2 审稿已收到（Overall 3.0 / Findings）。等待 Reviewer 1 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 188

## Round 188

6 recorded events


### User

_source line 2167 · 2026-05-23T07:29:13.140940+00:00_

[Reviewer 1 审稿意见]:
## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 用 KL 散度替代 BCE 训练稀疏性预测器是一个实用的贡献，PPL 改进在多架构上一致且显著（30% sparsity 下 14.5% over TEAL），但核心分析性贡献（signal type vs coupling scope 分解）受严重实验混淆因素制约，下游任务的统计功效不足以支撑方向性结论，且 knowledge-task regression 未得到充分解释。

## 官方维度打分（来自 ACL ARR review form）
| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 核心 PPL 实验（Table 2）设计合理且结果一致，但 K=1 分解和 C1 ablation 存在未充分控制的混淆变量；3-seed 下游指标统计功效不足以支撑方向性声明 |
| Excitement | 3/5 | 用输出分布蒸馏做稀疏性预测是有意义的方向，ablation 设计深度罕见，但本质上是在已有框架中替换损失函数，增量性较强 |
| Reproducibility | 4/5 | 超参数、训练细节、seed 变异均有详尽报告（Appendices B-G），可复现性高 |
| Confidence | 4/5 | 仔细阅读全文及全部 20 个附录，核验了关键数值声明 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] K=1 per-layer 分解的 train-inference mismatch 严重污染 "signal type accounts for majority" 结论

- 具体位置：Section 4.5, Appendix R/S/W (Tables 18–19, pages 18–20)
- 问题：K=1 训练时仅 1/32 层被 mask，推理时 32/32 层全部 mask。这造成严重的 train-inference distribution shift——训练时模型几乎看到完整的 dense forward pass，推理时却面对 32 层全部被稀疏化的场景。论文用 K=4 修正（Appendix S, Table 19），但 K=4 仍仅 mask 4/32 层（12.5% vs 推理时 100%），gap 无法闭合。更严重的是：
  - K=4 的 MMLU **系统性超过** E2E（Table 19），说明 mismatch 引入了不可预测的 artifact——如果分解是可靠的，K=4 不应优于 E2E。
  - K-curve 中 K=1,2,8,16,32 的数据点均为 **single-seed (s42)**（Appendix W 第 1427–1429 行明确承认 "All results except K=4 are single-seed (s42) and should be treated as preliminary"），无法排除随机波动。
  - 论文将 K=1 结果标注为 "upper bound"（Abstract），但 upper bound 的严格性取决于 mismatch 的方向——如果 mismatch 恰好高估了 signal type 贡献（因为 K=1 predictor 在近 dense 条件下训练更容易），那么 "upper bound" 实际上可能是一个系统性偏高的估计。
- 为什么影响接收：signal type vs coupling scope 分解是论文超越 "换 loss function" 的核心分析贡献。如果该分解不可靠，论文的理论洞察价值大幅缩水。Abstract 第 5–6 行和 Conclusion 第 1–2 段均将此分解作为主要 contribution 之一呈现。
- 建议修改方向：(1) 对 K=1,2,4,8,16,32 全部做 3-seed 实验（计算开销不大，每个 K 仅需 1000 steps × 3 seeds）；(2) 设计 progressive K-scheduling（训练中逐步增加 K 到 32）以消除 mismatch；(3) 至少将当前结论从 "decomposition" 降级为 "exploratory observation"，并在 Abstract/Conclusion 中相应调整措辞。

**N2** [critical] 3-seed 下游指标的统计功效不足以支撑方向性结论

- 具体位置：Table 2 (page 7), Table 14 (page 16), Appendix F (page 14)
- 问题：
  - **Table 14** 显示 50% Global 分配下 MMLU = 35.7 ± 9.5（σ = 9.5pp！），在 3 个 seed 下这意味着 individual seed 可能在 ~26% 到 ~45% 之间波动，任何基于该条件的方向性结论都不可靠。
  - Table 2 的下游指标仅报告 3-seed mean ± std，无 confidence interval、无 significance test。以 30% uniform 为例，MMLU σ ≈ 1.3pp，在 n=3 下 95% CI 为 ±2.9pp（使用 t 分布 t_{0.025,2}=4.303），这意味着 KL vs BCE 的 MMLU 差异（~1–2pp）完全落在置信区间内，无法判定方向。
  - GSM8K 在 30% uniform 下约 7.5%，接近 open-ended 数学任务的 floor，微小差异无统计意义。
  - 按照 ARR guidelines (R5)："Error bars, confidence intervals, significance tests, and effect sizes for main results" 是 statistical rigor 的基本要求，论文未满足。
- 为什么影响接收：论文在 Abstract（"consistent gains but knowledge-intensive regression"）和 Conclusion 中做出关于下游任务的方向性声明，但 3-seed 的统计功效不足以支撑。
- 建议修改方向：(1) 关键对比（Table 2 中 KL vs BCE vs TEAL）增加到至少 5 个 seed；(2) 报告 bootstrap 或 t-test 置信区间；(3) 对 Abstract/Conclusion 中的下游声明加入显式统计限定语（如 "PPL improvements are significant (p<0.01), but downstream differences are within noise margins"）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] C1 target-swap ablation 存在未隔离的混淆变量

- 具体位置：Section 4.4, Table 3 (page 7), Appendix P (page 18)
- 问题：C1 将 KL 发现的 mask 通过 soft→hard 二值化（logits > 0, 即 τ > 0.5）后作为 BCE 的训练目标。这个设计同时改变了两个因素：(a) mask 来源（KL-discovered vs magnitude-based）和 (b) mask 表示（hard binary vs soft Gumbel probability）。论文承认 "binarizing oracle soft logits into hard masks discards ranking information"（Section 4.4），但未定量评估表示变化的贡献。
  - BCE+Gumbel PPL = 32.22 vs 标准 BCE PPL = 27.97（Table 3 脚注区域），差异达 15%，说明 Gumbel 表示本身带来了显著影响。
  - Appendix P 承认 "does not rule out trajectory-dependent confounds"，但实验设计未尝试控制这些 confounds。
- 建议：增加控制实验：(a) 将 magnitude-based masks 同样二值化后用 BCE 训练，测量 "表示形式变化" 的贡献；(b) 或用 soft KL logits（未二值化）作为 BCE regression target，隔离 "mask 来源" vs "mask 表示" 的效应。

**W2** [warning] Knowledge-task regression 的机制分析不充分

- 具体位置：Section 4.2 (page 6), Appendix T/V (pages 19)
- 问题：
  - C4 控制实验（Appendix V, Table 22）仅用 **1 个 seed (s42)**，不足以支撑 "the deficit is structural to distribution-matching rather than training data composition" 的结论。n=1 无法排除 seed-specific artifact。
  - "forward KL's mode-covering property distributes mass across high-frequency patterns, potentially diluting rare activations encoding factual knowledge"（Section 4.2）是推测性解释，缺乏直接证据。例如，未分析被 KL vs magnitude 差异性 prune 掉的 neuron 是否确实对应 knowledge neurons（Meng et al., 2022 提供了此类分析的方法论）。
  - 跨 scale 一致退步（8B MMLU −5.2pp, 14B GSM8K −20pp per Appendix K Table 13）暗示这是方法的根本限制，但论文未提供缓解路径或讨论在什么条件下可能克服。
- 建议：(1) C4 实验增至 3+ seed；(2) 用 knowledge neuron 分析方法检验被差异性 prune 的 neuron 的功能角色；(3) 在 Limitations 中明确将 knowledge regression 定性为 open problem 并讨论可能的缓解方向（如 knowledge-aware sparsity constraint）。

**W3** [warning] 实验覆盖度存在显著缺口，且 Limitations 未覆盖

- 具体位置：Section 4.1 (page 6), Limitations (page 9)
- 问题：
  - **无生成任务评估**：所有下游评估均为 discriminative（ARC-c, WinoGrande, MMLU, GSM8K, HellaSwag, PIQA）或 PPL。但稀疏化对 generation quality 的影响可能截然不同——自回归 decoding 中每步的 mask 误差会累积，而 discriminative 任务仅需正确的 next-token ranking。
  - **seq_len 固定 2048**：LLaMA-3.1 支持 128K context，更长序列的 activation pattern 和 sparsity distribution 可能显著不同（long-range dependency 可能需要更多 neuron 参与）。
  - **无 batched inference 评估**：Appendix A (Table 5) 仅报告 batch_size=1, seq_len=2048 的推理延迟。实际部署通常 batch>1，predictor overhead 的相对占比在 batched setting 下可能更大（predictor 计算不受 batch 大小的稀疏加速影响）。
  - Limitations 部分（page 9）提及了 sparsity sweet spot、knowledge regression、training data homogeneity，但**未提及上述三个缺口中的任何一个**。
- 建议：(1) 至少增加一个 open-ended generation 评估（如 AlpacaEval 或 MT-Bench）；(2) 报告 seq_len=4096 或 8192 的 PPL；(3) 在 Limitations 中明确承认这些覆盖缺口。

**W4** [warning] Table 14 MMLU 数值与正文描述存在明显不一致

- 具体位置：Table 14 (page 16) vs Appendix F 正文 (page 14)
- 问题：Table 14 报告 50% Global 分配下 MMLU = 35.7 ± 9.5，但 page 14 Appendix F 正文描述 "Under global allocation at 50%, MMLU is 28.3 ± 0.7%"。同一条件下均值差 7.4pp、标准差差一个数量级（9.5 vs 0.7），不可能来自同一组数据。这要么是写作错误（例如混淆了不同 sparsity level 或不同 allocation 的数据），要么是引用了不同实验条件的数据但未标注。无论原因，在涉及高方差指标的关键数值上出现不一致，严重影响论文整体数据可信度。
- 建议：核实并统一所有 MMLU 数值，确保每个数字的实验条件（sparsity level, allocation strategy, seed set, model）完全标注。

---

## 小问题（不影响接收）

- **Gradient SNR 叙事张力**：Section 3.6 的梯度分析论证 KL 通过 cross-layer coupling 传播信号，但 Appendix H (Figure 5) 显示 BCE 的 gradient SNR **一致高于** KL。论文解释为 "noisier gradients as exploration mechanism"（Appendix H），但如果 coupling 真的有效地传递了有用信号，SNR 应该提高而非降低。更精确的表述应区分 "coupling introduces noise but also introduces cross-layer correlation structure"。

- **措辞审慎性**：Abstract 和 Section 2 中 "the first decomposition of signal type vs. coupling scope"（Section 2 最后一段附近）的 "first" 声明，考虑到该分解实验的可靠性问题（N1），措辞应更审慎（如 "an initial attempt" 或 "a preliminary decomposition"）。

- **Table 1 Taxonomy 新颖性定位**：Table 1 中 "Coupled KL" 占据 "unexplored combinations" 的位置，这暗示方法新颖性主要来自组合已有技术（KL distillation + per-neuron prediction），而非原理创新。建议在定位时更多强调实证发现（如 mask pattern divergence、signal type 观察），减少对方法新颖性的强调。

- **MSE baseline cherry-pick 风险**：Appendix G 中 MSE baseline 的 seed 123 出现 catastrophic failure (PPL=15,789)，论文仅报告 s42 结果。虽然这种 catastrophic failure 本身是有信息量的，但单独报告 s42 可能给读者留下 cherry-pick 的印象。建议在 Table 4 的 MSE 行添加脚注说明其他 seed 结果。

---

## Questions（需要作者回答）

**Q1**: K=4 实验中 MMLU 系统性超过 E2E（Table 19）的机制解释是什么？论文将其归因于 "K=4 near-uniform per-layer sparsity matching eval-time constraint"（Appendix S），但如果 K=4 的优势来自 sparsity distribution artifact 而非 coupling 效应，这是否反而削弱了 signal type decomposition 的结论？

**Q2**: Compensation network（Appendix J）不提供质量提升的原因是什么？如果 KL predictor 已充分学习输出分布，compensation 有冗余可以理解；但既然存在 knowledge-task regression，compensation 为什么不能恢复部分 knowledge-intensive 性能？这两个观察的共存是否暗示 knowledge regression 的根源不在 mask quality 而在 sparsity 本身？

**Q3**: 在 30% sparsity 下，包含 predictor + sparse FFN 的端到端推理延迟（wall-clock latency, batch_size ∈ {1, 4, 16, 32}）相比 dense 模型的实际加速比是多少？Table 5 仅报告 predictor overhead，未给出 sparse kernel 的实际加速。

**Q4**: 如果将 Table 14 中导致 MMLU σ=9.5 的 outlier seed 排除，Global allocation 的主要结论（"late-layer starvation causes knowledge regression"）是否仍然成立？

**Q5**: 是否考虑过 token-level adaptive sparsity（不同 token 不同 sparsity rate）作为缓解 knowledge regression 的手段？Knowledge-intensive token 可能需要更低的 sparsity。

---

## Missing References

未发现对接收决定有影响的关键遗漏。Related Work 覆盖了 TEAL、DejaVu、MaskLLM、CATS、R-Sparse、FastForward、SVD-CSP 等主要工作。以下可供参考：
- PowerInfer (Song et al., 2024) 在 heterogeneous CPU-GPU 推理中利用 activation sparsity 的工作，与本文的推理场景相关但技术路线不同。

---

## 主要优势

1. **实用且一致的 PPL 改进**：KL predictor 在 30% sparsity 下实现 14.5% PPL 改进（Table 2: 8.81 vs 10.30），且在 LLaMA-3.1-8B、Mistral-7B-v0.3（Appendix N, Table 16: −17.3%）、Qwen-2.5-14B（Appendix K, Table 13）上一致，跨架构泛化能力强。

2. **罕见的 ablation 深度**：20+ 个附录部分系统性消融几乎每个设计维度（relaxation method、divergence measure、coupling scope K、allocation strategy、temperature schedule、compensation network、training data domain、per-layer constraint 等），在同类工作中极为罕见，体现了严谨的实验方法论。

3. **诚实的负面结果报告**：论文坦率报告了 knowledge-task regression（MMLU −5.2pp）、compensation network 无效（Appendix J）、MSE catastrophic seed（Appendix G, PPL=15,789）、MMLU 高方差（Table 14, σ=9.5），未隐藏不利结果。

4. **有用的概念框架**：Table 1 的 Prediction Target × Training Signal Coupling taxonomy 和 Section 3.6 的 BCE vs KL gradient structure 分析，为后续工作提供了清晰的思考框架。

5. **充分的可复现性信息**：训练配置（Section 4.1, Appendix B）、seed 信息、评估 protocol（Section 4.1）、Lagrangian 收敛行为（Appendix C）均有完整记录。

---

**总结**：论文在 "KL distillation for sparsity prediction" 这一实用贡献上表现扎实（PPL 改进一致、ablation 深入、报告诚实），但在分析性贡献（signal type decomposition）上受 K=1 mismatch 和 single-seed 限制的严重制约，下游评估的统计功效不足以支撑 abstract/conclusion 中的方向性声明。如果作者能 (1) 补充 K-curve 的多 seed 实验以巩固分解结论，(2) 增强下游指标的统计严谨性，(3) 修复 Table 14 数值不一致问题，论文有潜力达到 Conference (4.0) 水平。当前状态下，practical contribution 足够进入 Findings，但 analytical claims 的可靠性问题使 Conference acceptance 处于边界。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2168 · 2026-05-23T07:30:03.290210+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "distill_sparse_swiglu",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（Round 1）\n\n**Overall**: 3.0 / 5 (Findings)\n\n### 官方维度打分\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3/5 |\n| Excitement | 3/5 |\n| Reproducibility | 4/5 |\n| Confidence | 4/5 |\n\n### 主要优势\n**S1.** Target-swap ablation（C1, Table 3）是本文最突出的实验设计贡献：通过在 BCE 上训练 KL 发现的 oracle masks，成功分离了\"mask 质量\"与\"训练机制\"的贡献。结果令人信服——C1 在 50% 稀疏度下与 KL 仅差 ≤0.79pp。\n**S2.** Per-layer KL 控制实验（K=1, K=4; Section 4.5）提供了有价值的分析框架。K=1 per-layer KL 达到 9.05±0.02，仅比 E2E KL 差 2.7%，而 per-layer MSE 退化至 18.52±1.68。\n**S3.** 诚实的局限性报告——知识任务退化、统计不确定性均坦承。\n**S4.** Related Work 覆盖全面，包括 2024-2026 近期工作。\n**S5.** 丰富的附录（~8 页），涵盖推理延迟、训练收敛、温度敏感性等。\n\n### Must-Fix 问题\n**N1** [critical] \"Primary design dimension\" claim 泛化性不足。结论称 \"Output-distribution alignment is the primary design dimension at moderate sparsity\"，但主要证据来自 LLaMA-3.1-8B 在 30% 稀疏度。跨架构验证信号混合（Mistral MMLU 持平；Qwen-14B GSM8K −20.1pp）。在知识密集任务上 magnitude-based TEAL 始终优于 KL predictor（Table 2）。建议限定为 \"primary design dimension *for perplexity and commonsense tasks*\"。\n\n**N2** [critical] 知识任务退化机制缺乏因果解释。C4 控制实验否定了训练数据偏差假说，mode-covering 稀释假说仅是推测。Constraint experiments（remove valley → MMLU +3.4pp）暗示 allocation 而非 loss function 是原因，但未深入追踪。Uniform KL MMLU 40.7 vs TEAL uniform 45.86 差 5pp 的原因未分析。\n\n### Should-Fix 问题\n**W1** [warning] Contribution framing 存在张力——反复声明 \"empirical study\" 但贡献列表包含方法性暗示。\n**W2** [warning] 术语一致性——核心概念至少有 5 种表述。\n**W3** [warning] Introduction 中 68% divergence 和 32% Jaccard 同句出现混淆。\n**W4** [warning] MSE 50% 单种子不可靠（s123 PPL=15,789）。\n**W5** [warning] Abstract/Conclusion 中 \"commonsense gains\" 措辞过强，3 seeds 不足支撑。\n**W6** [warning] Wall-clock speedup 缺失削弱实际影响力。\n\n### 小问题\n**M1**: Table 2 caption 信息过载。\n**M2**: Figure 2 caption \"82% at 70%\" 孤立。\n**M3**: Geometric Penalty ε=0.02 缺乏 justification。\n**M4**: Introduction 中 MMLU 40.7±1.3% 无 dense baseline 对比。\n\n### Questions\n**Q1**: K=4 在 50% 下 worse than K=1 的机制？\n**Q2**: K=4 MMLU 超越 E2E——是否意味对知识任务 per-layer 训练更优？\n**Q3**: Uniform allocation 下 KL MMLU 40.7 vs TEAL 45.86，二者都是 uniform，这 5pp 差距是否完全归因于 KL loss？与 \"allocation contributes\" 的解释矛盾。\n**Q4**: C1 中 s42 oracle provenance 对结果的影响？\n**Q5**: Forward vs Reverse KL 在 30% 下差异（8.81 vs 9.26）有统计显著性吗？\n\n### Novelty 边界评估\n新颖性不在 KL + Gumbel-Sigmoid recipe（与 MaskLLM 共享），而在 (1) 应用于 contextual activation sparsity 新领域，(2) target-swap ablation 和 per-layer KL 控制的分析框架。\"empirical + analytical\" 层面贡献，非 \"methodological\" 突破。Findings 足够，Main Conference 偏弱。\n\n---\n\n请逐条回应上述所有 Strengths、Must-Fix、Should-Fix、Minor、Questions 和 Novelty 评估。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "distill_sparse_swiglu",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（Round 1）\n\n**Overall**: 3.0 / 5 (Findings)\n\n### 官方维度打分\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3/5 |\n| Excitement | 3/5 |\n| Reproducibility | 4/5 |\n| Confidence | 4/5 |\n\n### 主要优势\n**S1.** Target-swap ablation（C1, Table 3）是本文最突出的实验设计贡献：通过在 BCE 上训练 KL 发现的 oracle masks，成功分离了\"mask 质量\"与\"训练机制\"的贡献。结果令人信服——C1 在 50% 稀疏度下与 KL 仅差 ≤0.79pp。\n**S2.** Per-layer KL 控制实验（K=1, K=4; Section 4.5）提供了有价值的分析框架。K=1 per-layer KL 达到 9.05±0.02，仅比 E2E KL 差 2.7%，而 per-layer MSE 退化至 18.52±1.68。\n**S3.** 诚实的局限性报告——知识任务退化、统计不确定性均坦承。\n**S4.** Related Work 覆盖全面，包括 2024-2026 近期工作。\n**S5.** 丰富的附录（~8 页），涵盖推理延迟、训练收敛、温度敏感性等。\n\n### Must-Fix 问题\n**N1** [critical] \"Primary design dimension\" claim 泛化性不足。结论称 \"Output-distribution alignment is the primary design dimension at moderate sparsity\"，但主要证据来自 LLaMA-3.1-8B 在 30% 稀疏度。跨架构验证信号混合（Mistral MMLU 持平；Qwen-14B GSM8K −20.1pp）。在知识密集任务上 magnitude-based TEAL 始终优于 KL predictor（Table 2）。建议限定为 \"primary design dimension *for perplexity and commonsense tasks*\"。\n\n**N2** [critical] 知识任务退化机制缺乏因果解释。C4 控制实验否定了训练数据偏差假说，mode-covering 稀释假说仅是推测。Constraint experiments（remove valley → MMLU +3.4pp）暗示 allocation 而非 loss function 是原因，但未深入追踪。Uniform KL MMLU 40.7 vs TEAL uniform 45.86 差 5pp 的原因未分析。\n\n### Should-Fix 问题\n**W1** [warning] Contribution framing 存在张力——反复声明 \"empirical study\" 但贡献列表包含方法性暗示。\n**W2** [warning] 术语一致性——核心概念至少有 5 种表述。\n**W3** [warning] Introduction 中 68% divergence 和 32% Jaccard 同句出现混淆。\n**W4** [warning] MSE 50% 单种子不可靠（s123 PPL=15,789）。\n**W5** [warning] Abstract/Conclusion 中 \"commonsense gains\" 措辞过强，3 seeds 不足支撑。\n**W6** [warning] Wall-clock speedup 缺失削弱实际影响力。\n\n### 小问题\n**M1**: Table 2 caption 信息过载。\n**M2**: Figure 2 caption \"82% at 70%\" 孤立。\n**M3**: Geometric Penalty ε=0.02 缺乏 justification。\n**M4**: Introduction 中 MMLU 40.7±1.3% 无 dense baseline 对比。\n\n### Questions\n**Q1**: K=4 在 50% 下 worse than K=1 的机制？\n**Q2**: K=4 MMLU 超越 E2E——是否意味对知识任务 per-layer 训练更优？\n**Q3**: Uniform allocation 下 KL MMLU 40.7 vs TEAL 45.86，二者都是 uniform，这 5pp 差距是否完全归因于 KL loss？与 \"allocation contributes\" 的解释矛盾。\n**Q4**: C1 中 s42 oracle provenance 对结果的影响？\n**Q5**: Forward vs Reverse KL 在 30% 下差异（8.81 vs 9.26）有统计显著性吗？\n\n### Novelty 边界评估\n新颖性不在 KL + Gumbel-Sigmoid recipe（与 MaskLLM 共享），而在 (1) 应用于 contextual activation sparsity 新领域，(2) target-swap ablation 和 per-layer KL 控制的分析框架。\"empirical + analytical\" 层面贡献，非 \"methodological\" 突破。Findings 足够，Main Conference 偏弱。\n\n---\n\n请逐条回应上述所有 Strengths、Must-Fix、Should-Fix、Minor、Questions 和 Novelty 评估。"
  }
}
```

</details>

---


### Tool result

_source line 2169 · 2026-05-23T07:30:34.479571+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 31189
}
```

</details>

---


### Tool call

_source line 2170 · 2026-05-23T07:30:34.530214+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "distill_sparse_swiglu",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（Round 1）\n\n**Overall**: 3.5 (Borderline Conference)\n\n### 官方维度打分\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3/5 |\n| Excitement | 3/5 |\n| Reproducibility | 4/5 |\n| Confidence | 4/5 |\n\n### Must-Fix 问题\n**N1** [critical] K=1 per-layer 分解的 train-inference mismatch 严重污染 \"signal type accounts for majority\" 结论。K=1 训练时仅 1/32 层被 mask，推理时 32/32 层全部 mask。K=4 修正不充分（仍仅 12.5%）。K=4 MMLU 系统性超过 E2E 说明 mismatch 引入不可预测 artifact。K-curve 中 K=1,2,8,16,32 均为 single-seed (s42)。建议：(1) K-curve 全部 3-seed；(2) progressive K-scheduling；(3) 将结论降级为 \"exploratory observation\"。\n\n**N2** [critical] 3-seed 下游指标统计功效不足。Table 14 显示 50% Global MMLU=35.7±9.5（σ=9.5pp）。30% uniform MMLU σ≈1.3pp 在 n=3 下 95% CI 为 ±2.9pp，KL vs BCE 差异完全落在 CI 内。GSM8K 7.5% 接近 floor。按 ARR guidelines R5 要求 error bars/significance tests，论文未满足。建议：(1) 至少 5 seeds；(2) bootstrap/t-test CI；(3) 下游声明加统计限定语。\n\n### Should-Fix 问题\n**W1** [warning] C1 target-swap ablation 存在未隔离混淆变量——soft→hard 二值化同时改变了 mask 来源和 mask 表示。BCE+Gumbel (32.22) vs 标准 BCE (27.97) 差 15% 说明 Gumbel 表示本身有显著影响。\n\n**W2** [warning] Knowledge-task regression 机制分析不充分。C4 控制仅 1 seed。\"mode-covering dilutes rare activations\" 是推测。跨 scale 退步（8B MMLU −5.2pp, 14B GSM8K −20pp）暗示根本限制但未提供缓解路径。\n\n**W3** [warning] 实验覆盖度缺口且 Limitations 未覆盖：(1) 无生成任务评估；(2) seq_len 固定 2048；(3) 无 batched inference 评估。\n\n**W4** [warning] Table 14 MMLU 数值不一致：Table 14 报告 50% Global MMLU=35.7±9.5，但 Appendix F 正文描述 50% Global MMLU=28.3±0.7。同一条件下均值差 7.4pp、标准差差一个数量级。\n\n### 小问题\n- Gradient SNR 叙事张力：coupling 应提高 SNR 但实际降低。\n- \"the first decomposition\" 措辞应更审慎。\n- Table 1 Taxonomy 暗示方法新颖性来自组合已有技术。\n- MSE baseline cherry-pick 风险（仅报告 s42）。\n\n### 主要优势\n1. 实用且一致的 PPL 改进（14.5% over TEAL, 跨架构一致）。\n2. 罕见的 ablation 深度（20+ 附录部分）。\n3. 诚实的负面结果报告。\n4. 有用的概念框架（Table 1 taxonomy + gradient analysis）。\n5. 充分的可复现性信息。\n\n### Questions\n**Q1**: K=4 MMLU 超过 E2E 的机制？如果来自 sparsity distribution artifact，是否削弱 decomposition 结论？\n**Q2**: Compensation network 不提升质量的原因？为何不能恢复 knowledge-intensive 性能？\n**Q3**: 包含 predictor + sparse FFN 的端到端 wall-clock latency（batch_size ∈ {1,4,16,32}）？\n**Q4**: 排除 MMLU σ=9.5 的 outlier seed 后，Global allocation 结论是否仍成立？\n**Q5**: 是否考虑 token-level adaptive sparsity 缓解 knowledge regression？\n\n### Missing References\n未发现重大遗漏。PowerInfer 可供参考但非必须。\n\n---\n\n请逐条回应上述所有 Must-Fix、Should-Fix、Minor、Strengths、Questions。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "distill_sparse_swiglu",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（Round 1）\n\n**Overall**: 3.5 (Borderline Conference)\n\n### 官方维度打分\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3/5 |\n| Excitement | 3/5 |\n| Reproducibility | 4/5 |\n| Confidence | 4/5 |\n\n### Must-Fix 问题\n**N1** [critical] K=1 per-layer 分解的 train-inference mismatch 严重污染 \"signal type accounts for majority\" 结论。K=1 训练时仅 1/32 层被 mask，推理时 32/32 层全部 mask。K=4 修正不充分（仍仅 12.5%）。K=4 MMLU 系统性超过 E2E 说明 mismatch 引入不可预测 artifact。K-curve 中 K=1,2,8,16,32 均为 single-seed (s42)。建议：(1) K-curve 全部 3-seed；(2) progressive K-scheduling；(3) 将结论降级为 \"exploratory observation\"。\n\n**N2** [critical] 3-seed 下游指标统计功效不足。Table 14 显示 50% Global MMLU=35.7±9.5（σ=9.5pp）。30% uniform MMLU σ≈1.3pp 在 n=3 下 95% CI 为 ±2.9pp，KL vs BCE 差异完全落在 CI 内。GSM8K 7.5% 接近 floor。按 ARR guidelines R5 要求 error bars/significance tests，论文未满足。建议：(1) 至少 5 seeds；(2) bootstrap/t-test CI；(3) 下游声明加统计限定语。\n\n### Should-Fix 问题\n**W1** [warning] C1 target-swap ablation 存在未隔离混淆变量——soft→hard 二值化同时改变了 mask 来源和 mask 表示。BCE+Gumbel (32.22) vs 标准 BCE (27.97) 差 15% 说明 Gumbel 表示本身有显著影响。\n\n**W2** [warning] Knowledge-task regression 机制分析不充分。C4 控制仅 1 seed。\"mode-covering dilutes rare activations\" 是推测。跨 scale 退步（8B MMLU −5.2pp, 14B GSM8K −20pp）暗示根本限制但未提供缓解路径。\n\n**W3** [warning] 实验覆盖度缺口且 Limitations 未覆盖：(1) 无生成任务评估；(2) seq_len 固定 2048；(3) 无 batched inference 评估。\n\n**W4** [warning] Table 14 MMLU 数值不一致：Table 14 报告 50% Global MMLU=35.7±9.5，但 Appendix F 正文描述 50% Global MMLU=28.3±0.7。同一条件下均值差 7.4pp、标准差差一个数量级。\n\n### 小问题\n- Gradient SNR 叙事张力：coupling 应提高 SNR 但实际降低。\n- \"the first decomposition\" 措辞应更审慎。\n- Table 1 Taxonomy 暗示方法新颖性来自组合已有技术。\n- MSE baseline cherry-pick 风险（仅报告 s42）。\n\n### 主要优势\n1. 实用且一致的 PPL 改进（14.5% over TEAL, 跨架构一致）。\n2. 罕见的 ablation 深度（20+ 附录部分）。\n3. 诚实的负面结果报告。\n4. 有用的概念框架（Table 1 taxonomy + gradient analysis）。\n5. 充分的可复现性信息。\n\n### Questions\n**Q1**: K=4 MMLU 超过 E2E 的机制？如果来自 sparsity distribution artifact，是否削弱 decomposition 结论？\n**Q2**: Compensation network 不提升质量的原因？为何不能恢复 knowledge-intensive 性能？\n**Q3**: 包含 predictor + sparse FFN 的端到端 wall-clock latency（batch_size ∈ {1,4,16,32}）？\n**Q4**: 排除 MMLU σ=9.5 的 outlier seed 后，Global allocation 结论是否仍成立？\n**Q5**: 是否考虑 token-level adaptive sparsity 缓解 knowledge regression？\n\n### Missing References\n未发现重大遗漏。PowerInfer 可供参考但非必须。\n\n---\n\n请逐条回应上述所有 Must-Fix、Should-Fix、Minor、Strengths、Questions。"
  }
}
```

</details>

---


### Tool result

_source line 2171 · 2026-05-23T07:30:35.898239+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1368
}
```

</details>

---


### Assistant

_source line 2172 · 2026-05-23T07:30:38.854267+00:00_

交叉分享已派发：
- Reviewer 1 收到 Reviewer 2 的完整审稿，需逐条回应
- Reviewer 2 收到 Reviewer 1 的完整审稿，需逐条回应

等待两位 Reviewer 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 189

## Round 189

2 recorded events


### User

_source line 2173 · 2026-05-23T07:30:41.398228+00:00_

[Reviewer 1 审稿结果]:
审稿完成。已向 Review Director 提交完整审稿意见，评分 **Overall 3.5 (Borderline Conference)**。

核心判断：
- **实用贡献扎实**：KL predictor 在 30% sparsity 下 PPL 改进 14.5%，跨 3 个架构一致，ablation 深度罕见
- **两个 critical 问题**：(1) K=1 signal type 分解受 train-inference mismatch 严重污染且多数数据点为 single-seed；(2) 3-seed 下游指标统计功效不足（MMLU σ=9.5 at 50% Global）
- **四个 should-fix**：C1 ablation 混淆变量未隔离、knowledge regression 机制分析不充分、缺少生成任务/长序列/batched inference 评估、Table 14 数值不一致

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2174 · 2026-05-23T07:30:57.391218+00:00_

交叉分享任务已派发给两位 Reviewer，等待交叉回应返回。

当前进度：
- **Step 1** ✅ 两位 Reviewer 独立初审完成（R1: 3.5, R2: 3.0）
- **Step 2** ⏳ 交叉分享已派发，等待逐条 [AGREE]/[REBUT] 回应
- **Step 3** 待定（收敛判断）
- **Step 4** 待定（汇总报告 + Issue Tracker 更新 + 投递）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 190

## Round 190

2 recorded events


### User

_source line 2175 · 2026-05-23T07:34:35.462879+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Strengths 回应

[AGREE] R1-S1（PPL 改进一致性）: 同意。KL predictor 在 LLaMA-3.1-8B（14.5%）、Mistral-7B（17.3%）、Qwen-2.5-14B 上均展示一致的 PPL 优势（Table 2, Table 16/Appendix N, Table 13/Appendix K），这是本文最 robust 的发现。

[AGREE] R1-S2（罕见的 ablation 深度）: 同意。20 页附录含 Appendix A-W，覆盖推理延迟、bottleneck 敏感性、温度调度、OOD、mask 可视化、cross-seed consistency 等，远超同类工作的通常标准。

[AGREE] R1-S3（诚实的负面结果）: 同意。这是本文的一个显著优点。MMLU −5.2pp (8B)、GSM8K −20.1pp (14B) 均在 Abstract、Section 4.2、Limitations 中明确报告，没有选择性汇报。

[AGREE] R1-S4（概念框架）: 同意。Table 1 taxonomy（signal type × coupling scope）和 Section 3.6 的 gradient analysis 提供了有用的分析框架。但需注意 taxonomy 本身主要是对现有方法的分类整理，而非方法论创新。

[AGREE] R1-S5（可复现性）: 同意。超参数、硬件配置（RTX PRO 6000 Blackwell, 96GB）、训练步数、seed 选择均有明确记录。承诺开源进一步增强可复现性。

---

### Must-Fix 问题回应

[AGREE] R1-N1（K=1 per-layer 分解的 train-inference mismatch）:
同意这是本文 signal type decomposition 的核心方法论弱点。具体证据：

1. **K=1 confound 论文已承认**：Section 4.5 明确说 "an upper bound, as the K=1 control conflates coupling removal with train-inference mismatch (training 1/32 layers; inference all 32)"。
2. **K=4 修正不充分**：R1 指出 K=4 仍仅 12.5% 层被 mask，这个批评是合理的。论文的 K=4 3-seed 结果（8.89±0.01）接近 E2E（8.81±0.02），PPL gap 为 67% closure，但这并不能完全消除 mismatch confound。
3. **MMLU anomaly 削弱分解可靠性**：K=4 MMLU（42.7±1.4）系统性超过 E2E（40.7±1.3）across all 3 seeds（Section 4.5），论文将其归因于 "K=4's near-uniform allocation matching uniform inference"。如果分解本身产生 artifact（MMLU 反超），那么其他维度的分解结果同样可能受 artifact 影响。
4. **K-curve single-seed**：Appendix W 的 K-curve（K=1,2,8,16,32）均为 s42 单种子，non-monotonic pattern（K=16 PPL 8.67 < E2E 8.81）可能是 seed-specific artifact。

**补充意见**：我在自己的审稿中（N1）也指出了 "primary design dimension" 的泛化性不足。R1 建议 "(3) 将结论降级为 exploratory observation" 是合理的最小修改。更理想的修改是在论文中明确标注 K=1 结果为 upper bound，K=4 为 partial deconfounding，并承认在无 K=32（即 E2E，已有）到 K=1 之间的完整 multi-seed K-curve 之前，signal type vs. coupling 的精确分解仍是 tentative。

---

[AGREE] R1-N2（3-seed 下游指标统计功效不足）:
同意。具体证据：

1. **σ=9.5pp on n=3**：Table 2 中 30% KL global MMLU = 35.7±9.5，意味着 95% CI ≈ ±23.6pp（t-distribution, df=2），基本没有统计信息量。
2. **KL vs. TEAL 差异在 CI 内**：30% uniform MMLU: KL 40.7±1.3 vs. TEAL 45.86。差异 5.16pp，n=3 下 95% CI for KL ≈ [37.5, 43.9]，不包含 45.86。但这仅是单侧比较（TEAL 是确定性的单次运行，无方差估计），严格来说 p-value 无法计算。
3. **论文内部承认但外部声明不一致**：Section 4.2 诚实地说 "directional evidence"，但 Abstract（"commonsense gains"）和 Conclusion（"commonsense gains"）未带此限定。

**补充意见**：我在自己的审稿中（W5）也提出了相同关切。R1 的建议 "(3) 下游声明加统计限定语" 是必要的。关于 "(1) 至少 5 seeds"，这是理想方案但可能受限于计算资源，至少应增加 bootstrap CI 的报告。

---

### Should-Fix 问题回应

[AGREE] R1-W1（C1 target-swap ablation 的 soft→hard 混淆变量）:
部分同意。论文在 Section 4.4 确实承认了这一 confound："binarizing oracle soft logits (>0) into hard masks discards ranking information, so the near-zero delta reflects transferability of binary mask patterns rather than full predictor knowledge." BCE+Gumbel（32.22）vs 标准 BCE（27.97）的 15% 差距说明 Gumbel 表示本身有影响。

但 C1 的核心发现仍然成立：即使存在 representation confound，KL-derived hard masks + simple BCE 训练（C1）仍然远优于 magnitude-derived hard masks + BCE（15.71 at 30%），说明 mask 质量（哪些 neuron 被选中）是关键因素。Gumbel 的 representation 效应只部分解释了 KL 优势，不能完全解释。

**建议**：作者应增加一个 "KL-derived masks + BCE without Gumbel" 的 ablation 以完全隔离 mask 质量 vs. mask 表示。或者更明确地限定 C1 结论的适用范围。

---

[AGREE] R1-W2（Knowledge-task regression 分析不充分）:
强烈同意，这与我的 N2 高度一致。C4 控制实验仅 1 seed（Section 4.2: "MMLU 40.0%, GSM8K 4.1%"），排除训练数据假说的证据不充分。"mode-covering dilutes rare activations" 仍是推测。

关键数据点：KL uniform MMLU = 40.7 vs. TEAL uniform MMLU = 45.86（Table 2, 30%），二者使用相同的 uniform allocation 策略。这 5pp 差距不能用 allocation 解释，必须归因于 KL loss 本身的某种属性。论文未对此进行因果分析。

---

[REBUT] R1-W3（实验覆盖度缺口且 Limitations 未覆盖）:
R1 声称 "(1) 无生成任务评估；(2) seq_len 固定 2048；(3) 无 batched inference 评估" 未被 Limitations 覆盖。这与事实不符。

Limitations 段落（page 9）明确写道：
- "open-ended generation quality (e.g., MT-Bench) remains untested and may exhibit different sparsity sensitivity"（覆盖第 1 点）
- "All experiments use sequence length 2048; behavior at longer contexts (e.g., 8K-128K) is untested"（覆盖第 2 点）
- "Batched inference, where sparsity patterns must be intersected across sequences, may reduce effective sparsity and is not evaluated"（覆盖第 3 点）

三个实验覆盖度缺口均已在 Limitations 中明确承认。R1 的批评在 "这些是缺口" 方面是正确的，但 "Limitations 未覆盖" 的判断有误。

---

[REBUT] R1-W4（Table 14 MMLU 数值不一致）:
R1 称 "Table 14 报告 50% Global MMLU=35.7±9.5，但 Appendix F 正文描述 50% Global MMLU=28.3±0.7"。

经我核实 LaTeX 源文件（appendix.tex lines 336-354），Table 14（tab:phase）的实际内容是：
- **30% Global**: MMLU = 35.7±9.5*
- **30% Uniform**: MMLU = 40.7±1.3
- **50% Global**: MMLU = 28.3±0.7
- **50% Uniform**: MMLU = 28.0±0.6

**35.7±9.5 是 30% Global 的数值，不是 50% Global。** R1 误读了表格行标签。Table 14 中 50% Global MMLU = 28.3±0.7，与 Appendix F（Training Stability, appendix.tex line 221: "Under global allocation at 50%, MMLU is 28.3±0.7%"）以及 Table 2 主表完全一致。不存在数据不一致。

---

### 小问题回应

[REBUT] R1-Minor-1（Gradient SNR 叙事张力：coupling 应提高 SNR 但实际降低）:
R1 说 "coupling 应提高 SNR"，但论文并未做此预测。Section 3.6 明确写道："BCE maintains consistently higher SNR than KL throughout training (2.3× at convergence), indicating that KL's quality advantage does not arise from cleaner gradient signals. Rather, KL's end-to-end coupled gradient serves as a search mechanism." Figure 5（Appendix H）显示这是 consistent pattern，不是 anomaly。论文的叙事是 "KL 胜出 despite 更低 SNR"，而非 "KL 因更高 SNR 而胜出"。这是论文的一个 deliberate finding，不是张力。

[AGREE] R1-Minor-2（"the first decomposition" 措辞应更审慎）:
同意。Section 2 写 "to our knowledge, the first decomposition of signal type vs. coupling scope"。虽然有 "to our knowledge" 限定，但 "first" 仍然是强 claim。建议改为 "a systematic decomposition" 或 "we provide what we believe is the first..."

[AGREE] R1-Minor-3（Table 1 Taxonomy 暗示新颖性来自组合已有技术）:
同意。这与我的 novelty 边界评估一致。Table 1 诚实地展示了本文方法的位置（Per-token × Coupled），而每个维度上的技术（per-token prediction, KL distillation, Gumbel-Sigmoid）均非新发明。新颖性在于 combination + empirical characterization，这是 Findings 级别的贡献。

[AGREE] R1-Minor-4（MSE baseline cherry-pick 风险）:
部分同意。MSE 50% 仅报告 s42（PPL 229.26），s123 catastrophic（PPL=15,789, Appendix G, appendix.tex line 244）。论文通过脚注标注了这一点（Table 4: "§MSE 50%: s42 only; s123 catastrophic"），保持了透明度。但 30% MSE 3-seed mean 18.52±1.68（s42=20.43, s123=17.73, s456=17.39）是合理的 baseline。风险在于读者可能忽略脚注，误以为 MSE 50% 是 robust result。

---

### Questions 回应

[AGREE] R1-Q1（K=4 MMLU 超过 E2E 的机制）:
这是我在 Q2 中提出的相同问题。论文归因于 "K=4's near-uniform allocation matching uniform inference"（Section 4.5）。如果正确，这意味着 E2E KL 学到的 non-uniform allocation 实际上 *伤害* MMLU，而 per-layer 训练偶然产生了更好的 allocation。这确实削弱了 "output-distribution alignment is the primary design dimension" 的全面性——至少对 knowledge tasks，allocation 可能比 signal type 更重要。

[AGREE] R1-Q2（Compensation network 为何无效）:
有效问题。论文仅说 "provides no benefit"（Section 4.5, Appendix J），但未解释 *为什么*。可能的原因：(1) KL predictor 已经优化了 output distribution，compensation network 没有剩余误差可修正；(2) compensation 的 per-layer MSE 目标与 KL 的 output-distribution 目标不兼容。作者应至少讨论机制。

[AGREE] R1-Q3（端到端 wall-clock latency）:
同意需要更多 batch size 的延迟数据。Appendix A（Table 5）仅报告 batch=1 的结果。对于实际部署，batch>1 的延迟特征可能完全不同（predictor overhead 可能被摊薄，但 mask intersection 成本可能增加）。

[AGREE] R1-Q4（排除 MMLU σ=9.5 的 outlier seed 后 Global allocation 结论是否成立）:
有效问题。Table 15（Appendix L, tab:phase_full）显示 30% Global MMLU seeds span 25.3--43.5%。如果 25.3% 是 outlier，排除后 mean 会显著上升。但 n=3 下排除 1 个 seed（变成 n=2）更不可靠。这再次印证 R1-N2 的 seed 不足问题。

[AGREE] R1-Q5（token-level adaptive sparsity 缓解 knowledge regression）:
有趣的方向。当前方法使用 model-level fixed sparsity target。Token-level adaptive sparsity（对 knowledge-intensive tokens 降低 sparsity）可能缓解 MMLU 退化。论文未讨论此方向，可列为 future work。

---

### 总体评价

R1 给出 3.5（Borderline Conference），我给出 3.0（Findings）。差异主要在于：
1. R1 对 PPL 改进的实用价值评价略高，我认为缺乏 wall-clock speedup 显著削弱实际影响力。
2. 我对 "primary design dimension" claim 的泛化性更为怀疑，尤其是在 knowledge tasks 上的系统性退化。

两位 reviewer 的核心共识：
- PPL 改进 robust 且一致（共识优势）
- K=1 decomposition 存在 train-inference mismatch confound（共识弱点）
- 3 seeds 不足以支持下游 claims（共识弱点）
- Knowledge regression 缺乏因果解释（共识弱点）
- Table 1 taxonomy 的新颖性在于组合而非原创技术（共识判断）
- 适合 Findings track（3.0-3.5 区间）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2176 · 2026-05-23T07:34:48.958137+00:00_

Reviewer 2 交叉回应已收到。等待 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 191

## Round 191

10 recorded events


### User

_source line 2177 · 2026-05-23T07:34:51.513992+00:00_

[Reviewer 2 审稿结果]:
已向 Review Director 提交逐条回应。

**要点总结**：
- R1 的 5 个 Strengths 全部 **[AGREE]**
- **Must-Fix N1**（K=1 mismatch）: [AGREE]，与我的 N1 高度一致
- **Must-Fix N2**（3-seed 统计功效）: [AGREE]，与我的 W5 一致
- **Should-Fix W1**（C1 soft→hard confound）: [AGREE]，但指出核心发现仍成立
- **Should-Fix W2**（Knowledge regression）: [AGREE]，与我的 N2 一致
- **Should-Fix W3**（Limitations 未覆盖）: **[REBUT]** — Limitations 段落明确覆盖了 R1 提到的全部三个缺口（generation tasks, seq_len, batched inference）
- **Should-Fix W4**（Table 14 数值不一致）: **[REBUT]** — R1 误读了表格行标签，35.7±9.5 是 30% Global 而非 50% Global，数据完全一致
- **Minor 1**（SNR 张力）: **[REBUT]** — 论文叙事是 "KL despite lower SNR"，不是 "KL because of higher SNR"
- 其余 Minor 和 Questions 均 [AGREE]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2178 · 2026-05-23T07:36:08.658280+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 2179 · 2026-05-23T07:36:08.709103+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T07:19:28.634279+00:00\", \"completed_at\": \"2026-05-23T07:23:07.265962+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页仅有 Title/Abstract/Introduction 纯文字，无视觉锚点。Figure 1 出现在第 2 页——位置可接受，审稿人翻一页即可看到方法概览图\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1（Method overview / Training Signal Coupling）作为首个 display item，能传达核心 idea（output-distribution distillation + 跨层梯度耦合）。Caption 自包含，包含推理流程说明。单栏宽度偏小，若改为 figure*（全宽）可提升视觉冲击力，但当前尺寸文字仍可读\"}, {\"severity\": \"info\", \"dimension\": \"pages 3-4\", \"message\": \"连续 2 页无 figure/table（Related Work → Method 3.1-3.4）。Page 4 有多个公式提供视觉节奏，不算严格的\\\"纯文本页\\\"，但 page 3 整页为密集散文。对于 method-heavy 论文可接受\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1（Taxonomy）位置恰当，在 Method 章节内穿插，打破了前两页的纯文本节奏。表格使用 booktabs 风格，格式规范\"}, {\"severity\": \"warning\", \"dimension\": \"page 6\", \"message\": \"整页纯文本（Experiments 4.1-4.2 实验设置描述），位于 Table 1（p5）和 Tables 2-4（p7）之间。建议将部分实验设置移至 Appendix 以腾出空间，或在此页穿插一个小型 setup 示意图\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"单页包含 3 个表格（Table 2 主结果 + Table 3 目标交换消融 + Table 4 设计选择消融），视觉非常密集。虽然内容均为核心结果，但审稿人阅读体验较拥挤。考虑将 Table 3 或 Table 4 之一移至下一页或 Appendix\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Tables 2-4 均使用 booktabs 风格、最优值加粗、精度一致——表格规范良好\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 2（PPL Scaling with Sparsity）右栏位置合理，与 §4.6 Sparsity Scaling 分析段落紧邻。图表清晰，轴标签可读，线条可区分。Conclusion 从左栏底部开始\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"主正文（§1-5）在第 8 页内结束，符合 EMNLP/ACL 8 页限制\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 段落简短（~3 个要点），Ethics Statement 简洁，References 紧随其后。Limitations 不占正文页数，合规\"}, {\"severity\": \"info\", \"dimension\": \"pages 9-11\", \"message\": \"References 跨约 2.5 页，格式统一，未见 [?]
…[truncated 1287 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2180 · 2026-05-23T07:36:08.809819+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 2181 · 2026-05-23T07:36:08.860479+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2182 · 2026-05-23T07:44:22.620382+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 27 (Fresh Review) — Active issues\n  # ============================================================\n\n  - id: \"R20-W1\"\n    summary: \"Per-layer KL decomposition 的 train-inference mismatch confound 未解决\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 27\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Critical。K=4 single-seed。\"}\n      - {round: 22, reviewers: [1, 2], note: \"R22 N2。97.5% 精确数字不可靠。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 C1。K=1 有 32× train-inference mismatch。\"}\n      - {round: 25, reviewers: [1, 2], note: \"R25 N1/N2。K=4 at 50% 反常仍仅 speculation。\"}\n      - {round: 26, reviewers: [1, 2], note: \"R26 完全共识。核心问题不变。\"}\n      - {round: 27, reviewers: [1, 2], note: \"R27 完全共识 Critical。(1) K=1 仅 1/32 层被 mask，推理 32/32；(2) K=4 修正仅 12.5%，MMLU 42.7>40.7 超过 E2E 说明 artifact；(3) K-curve 除 K=4 外均 single-seed(s42)，论文自承 preliminary；(4) K=16 PPL 8.67 < E2E 8.81 non-monotonic 可能 seed-specific；(5) upper bound 可能系统性高估 signal type。建议降级为 exploratory observation 或补充 K-curve full 3-seed。\"}\n    action_items:\n      - {round: 21, action: \"K=4 3-seed\", assigned_to: \"main_agent\", status: done}\n      - {round: 22, action: \"97.5% → 定性表述\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"K=2/K=8/K=16 实验扩展 K-curve\", assigned_to: \"main_agent\", status: done}\n      - {round: 26, action: \"Abstract 'accounts for the majority' 弱化\", assigned_to: \"paper_agent\", status: open}\n      - {round: 27, action: \"K-curve 全部 K 值做 3-seed 实验\", assigned_to: \"main_agent\", status: open}\n      - {round: 27, action: \"§4.5 分解结论降级为 exploratory analysis with acknowledged confounds\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-N2\"\n    summary: \"MMLU/GSM8K 跨架构系统性退步缺乏因果机制分析\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 18\n    last_seen_round: 27\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Critical。Protection valley 分析仅 correlational。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 C2。Remove valley 不够。8B MMLU -5.2pp, 14B GSM8K -20pp。\"}\n      - {round: 25, reviewers: [1, 2], note: \"R25 最高优先级。两个假设仍仅 speculation。\"}\n      - {round: 26, reviewers: [1, 2], note: \"R26 完全共识。退步跨架构一致。\"}\n      - {round: 27, reviewers: [1, 2], note: \"R27 完全共识 Critical。(1) C4 控制仅 1 seed，证据不充分；(2) mode-covering 假说缺乏直接证据（未分析被差异性 prune 的 neuron 功能角色）；(3) KL uniform MMLU 40.7 vs TEAL uniform 45.86，同 allocation 差 5pp 不能用 allocation 解释；(4) 跨 scale 退步 8B→14B GSM8K -1.3→-20.1pp 暗示根本限制。\"}\n    action_items:\n      - {round: 25, action: \"C4 控制实验\", assigned_to: \"main_agent\", status: done}\n      - {round: 26, action: \"Abstract 量化知识退步\", assigned_to: \"paper_agent\", status: done}\n      - {round: 26, action: \"Conclusion 限定为 PPL+commonsense\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"C4 控制实验增至 3+ seed\", assigned_to: \"main_agent\", status: open}\n      - {round: 27, action: \"Knowledge neuron 分析检验被差异性 prune 的 neuron 功能角色\", assigned_to: \"main_agent\", status: open}\n      - {round: 27, action: \"分析 KL uniform vs TEAL uniform MMLU 5pp 差距的具体归因\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R25-N1\"\n    summary: \"方法新颖性边界需更清晰论证\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - {round: 25, reviewers: [2], note: \"核心组件均成熟技术。MaskLLM 已用 KL+Gumbel。\"}\n      - {round: 26, reviewers: [2], note: \"Table 1 需纳入 MaskLLM。\"}\n      - {round: 27, reviewers: [1, 2], note: \"R27 共识。KL+Gumbel recipe 与 MaskLLM 共享。三点区分 valid。新颖性在于 contextual activation sparsity 应用 + 分析框架。'empirical+analytical' 层面，非 methodological 突破。Findings 足够，Main Conference 偏弱。\"}\n    action_items:\n      - {round: 26, action: \"Table 1 加入 MaskLLM\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W2\"\n    summary: \"高方差下游指标统计可靠性不足\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 24\n    last_seen_round: 27\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"ARC-c 95% CI ≈ ±8.9pp。PPL 方差极低。\"}\n      - {round: 25, reviewers: [1, 2], note: \"Qwen-14B GSM8K std=5.2pp。\"}\n      - {round: 26, reviewers: [1, 2], note: \"MMLU 30% global σ=9.5。\"}\n      - {round: 27, reviewers: [1, 2], note: \"R27 R1 升级为 Critical(N2)，R2 维持 Warning 但同意。30% Global MMLU σ=9.5：n=3 95% CI ≈ ±23.6pp 基本无信息量。Abstract/Conclusion 'commonsense gains' 无 'directional' 限定。ARR R5 要求未充分满足。\"}\n    action_items:\n      - {round: 24, action: \"高方差指标加 CI overlap caveat\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"关键对比增加到 5+ seeds 或报告 bootstrap CI\", assigned_to: \"main_agent\", status: open}\n      - {round: 27, action: \"Abstract/Conclusion 'commonsense gains' 加 'directional' 限定\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W3\"\n    summary: \"C1 ablation soft→hard mask representation 残余 confound\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 24\n    last_seen_round: 27\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"Oracle 二值化丢失排序信息。\"}\n      - {round: 26, reviewers: [1, 2], note: \"BCE+Gumbel vs BCE 不足以排除 confound。\"}\n      - {round: 27, reviewers: [1, 2], note: \"R27 共识 Warning。soft→hard 同时改变 mask 来源和表示。BCE+Gumbel(32.22) vs BCE(27.97) 差 15%。R2 指出核心发现仍成立（KL-derived+BCE 远优于 magnitude+BCE 15.71）。建议增加控制实验隔离 mask 来源 vs 表示。s42 gap(0.65pp) vs s123/s456(≤0.03pp) 可能为 provenance artifact。\"}\n    action_items:\n      - {round: 25, action: \"binarization confound caveat\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"增加 magnitude masks 二值化+BCE 控制实验隔离 mask 来源 vs 表示\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R25-M1\"\n    summary: \"术语不一致：至少 5 种表述交替使用\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - {round: 25, reviewers: [2], note: \"全文交替使用多种术语。\"}\n      - {round: 26, reviewers: [1, 2], note: \"再次提出。\"}\n      - {round: 27, reviewers: [1, 2], note: \"R27 R2-W2 提出 5 种表述：distillation/alignment/optimization/KL distillation/distribution-matching。R1 交叉同意。\"}\n    action_items:\n      - {round: 25, action: \"全文统一术语\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R26-M3\"\n    summary: \"68% divergence 和 32% Jaccard 同句出现易混淆\"\n    category: writing\n    severity: minor\n    status: open\n    first_raised_round: 26\n    last_seen_round: 27\n    mentions:\n      - {round: 26, reviewers: [1, 2], note: \"Introduction 互补度量同句混淆。\"}\n      - {round: 27, reviewers: [2], note: \"R27 R2-W3 再次提出。\"}\n    action_items:\n      - {round: 26, action: \"统一使用一种表述\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R26-W1\"\n    summary: \"14.5% PPL improvement 引用基准在 Abstract 与 Table 2 不一致\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 26\n    last_seen_round: 27\n    mentions:\n      - {round: 26, reviewers: [1, 2], note: \"Abstract 用 matched-sparsity，Table 2 用 TEAL uniform。\"}\n      - {round: 27, reviewers: [2], note: \"R27 仍可能困惑读者。Table 2 caption 已标注但不够突出。\"}\n    action_items:\n      - {round: 26, action: \"Table 2 caption 标注来源\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 27 — New issues\n  # ============================================================\n\n  - id: \"R27-W1\"\n    summary: \"Abstract/Conclusion 'commonsense gains' 措辞过强缺乏统计限定\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - {round: 27, reviewers: [1, 2], note: \"Section 4.2 说 'directional evidence'，但 Abstract/Conclusion 'commonsense gains' 无此限定。3 seeds 不足支撑。\"}\n    action_items:\n      - {round: 27, action: \"'commonsense gains' 改为 'directional commonsense improvements' 或加统计限定\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R27-W2\"\n    summary: \"Contribution framing 张力：'empirical study' vs 方法性贡献列表\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - {round: 27, reviewers: [2], note: \"反复声明 'empirical study' 但贡献列表含方法性暗示。实际引入了具体方法（KL predictor + Gumbel-Sigmoid for contextual sparsity）。建议承认方法贡献或调整贡献列表措辞。\"}\n    action_items:\n      - {round: 27, action: \"贡献列表措辞统一为实证发现或承认方法贡献\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Previously open, not raised in R27\n  # ============================================================\n\n  - id: \"R25-W1\"\n    summary: \"BCE 30% 缺少 uniform allocation 对比\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - {round: 25, reviewers: [1, 2], note: \"Table 2 中 BCE 30% 仅有 global。\"}\n      - {round: 26, reviewers: [1, 2], note: \"R26 确认。\"}\n      - {round: 27, reviewers: [], note: \"R27 未提出。BCE 30% uniform 已加入 Table 2，可能已修复。\"}\n    action_items:\n      - {round: 26, action: \"Table 2 增加 BCE 30% uniform 行\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R25-W2\"\n    summary: \"MSE 50% baseline 仅 seed 42 有效\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - {round: 25, reviewers: [1, 2], note: \"MSE 50% s123 catastrophic。\"}\n      - {round: 27, reviewers: [1], note: \"R27 R1 minor 提及 cherry-pick 风险。Table 4 有脚注但正文易误解。\"}\n    action_items:\n      - {round: 25, action: \"正文使用 MSE 50% 注明 single-seed\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W6\"\n    summary: \"Figure 2 仅展示 global allocation 但推荐 uniform\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 26\n    mentions:\n      - {round: 22, reviewers: [1, 2], note: \"Figure framing 效果强。\"}\n      - {round: 27, reviewers: [], note: \"R27 未提出。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Resolved issues\n  # ============================================================\n\n  - id: \"R19-N3\"\n    summary: \"无实际 wall-clock 加速\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 27\n    mentions:\n      - {round: 22, reviewers: [1, 2], note: \"降为 Warning。\"}\n      - {round: 27, reviewers: [2], note: \"R27 R2-W6 提及但认可 framing。维持 resolved。\"}\n    resolution: \"论文已充分 framed 为 empirical study。\"\n    resolution_round: 23\n\n  - id: \"R24-W1\"\n    summary: \"评估覆盖度空白\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 27\n    mentions:\n      - {round: 27, reviewers: [1], note: \"R1-W3 提出但 R2 [REBUT] 正确——Limitations 已覆盖。\"}\n    resolution: \"Limitations 已明确覆盖全部三个缺口。\"\n    resolution_round: 25\n\n  - id: \"R24-W4\"\n    summary: \"'Primary design dimension' 声明需限定\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 27\n    resolution: \"合并入 R20-N2。Conclusion 已限定。\"\n    resolution_round: 26\n\n  - id: \"R25-W3\"\n    summary: \"19% → 14.5% PPL 数值修正\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 25\n    last_seen_round: 26\n    resolution: \"已修正。基准问题转入 R26-W1。\"\n    resolution_round: 26\n\n  - id: \"R26-M1\"\n    summary: \"8.6%/6.4% 未标注 sparsity level\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 26\n    last_seen_round: 26\n    resolution: \"已加标注。\"\n    resolution_round: 26\n\n  - id: \"R26-M2\"\n    summary: \"'stable downstream' 措辞误导\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 26\n    last_seen_round: 26\n    resolution: \"已删除 'stable'。\"\n    resolution_round: 26\n\n  - id: \"R25-M2\"\n    summary: \"Eq. 4 s_j 缺层标\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 25\n    last_seen_round: 25\n    resolution: \"已补充。\"\n    resolution_round: 25\n\n  - id: \"R19-W1\"\n    summary: \"与 MaskLLM 新颖性区分\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 26\n    resolution: \"合并进 R25-N1。\"\n    resolution_round: 25\n\n  - id: \"R20-W4\"\n    summary: \"WikiText 同分布评估 + C4 OOD\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 26\n    resolution: \"Appendix D OOD 证据充分。\"\n    resolution_round: 25\n\n  - id: \"R22-W3\"\n    summary: \"Table 2 actual sparsity mismatch 脚注\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 26\n    resolution: \"脚注存在。\"\n    resolution_round: 23\n\n  - id: \"R22-W5\"\n    summary: \"规模泛化仅 7-14B\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 26\n    resolution: \"Limitations 已含。\"\n    resolution_round: 25\n\n  - id: \"R19-N2\"\n    summary: \"C1 因果声明\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 24\n    resolution: \"已降级为 transferability。\"\n    resolution_round: 23\n\n  - id: \"R22-W7\"\n    summary: \"Abstract 信息密度\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"已拆分。\"\n    resolution_round: 23\n\n  - id: \"R22-W8\"\n    summary: \"Conclusion 引用 BoolQ\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"改为 HellaSwag/PIQA。\"\n    resolution_round: 23\n\n  - id: \"R19-W7\"\n    summary: \"30% sweet spot 限制\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 26\n    resolution: \"Limitations 已覆盖。\"\n    resolution_round: 25\n\n  - id: \"R15-N3\"\n    summary: \"MaskLLM 新颖性边界\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 26\n    resolution: \"合并进 R25-N1。\"\n    resolution_round: 23"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 27 (Fresh Review) — Active issues\n  # ============================================================\n\n  - id: \"R20-W1\"\n    summary: \"Per-layer KL decomposition 的 train-inference mismatch confound 未解决\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 27\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Critical。K=4 single-seed。\"}\n      - {round: 22, reviewers: [1, 2], note: \"R22 N2。97.5% 精确数字不可靠。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 C1。K=1 有 32× train-inference mismatch。\"}\n      - {round: 25, reviewers: [1, 2], note: \"R25 N1/N2。K=4 at 50% 反常仍仅 speculation。\"}\n      - {round: 26, reviewers: [1, 2], note: \"R26 完全共识。核心问题不变。\"}\n      - {round: 27, reviewers: [1, 2], note: \"R27 完全共识 Critical。(1) K=1 仅 1/32 层被 mask，推理 32/32；(2) K=4 修正仅 12.5%，MMLU 42.7>40.7 超过 E2E 说明 artifact；(3) K-curve 除 K=4 外均 single-seed(s42)，论文自承 preliminary；(4) K=16 PPL 8.67 < E2E 8.81 non-monotonic 可能 seed-specific；(5) upper bound 可能系统性高估 signal type。建议降级为 exploratory observation 或补充 K-curve full 3-seed。\"}\n    action_items:\n      - {round: 21, action: \"K=4 3-seed\", assigned_to: \"main_agent\", status: done}\n      - {round: 22, action: \"97.5% → 定性表述\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"K=2/K=8/K=16 实验扩展 K-curve\", assigned_to: \"main_agent\", status: done}\n      - {round: 26, action: \"Abstract 'accounts for the majority' 弱化\", assigned_to: \"paper_agent\", status: open}\n      - {round: 27, action: \"K-curve 全部 K 值做 3-seed 实验\", assigned_to: \"main_agent\", status: open}\n      - {round: 27, action: \"§4.5 分解结论降级为 exploratory analysis with acknowledged confounds\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-N2\"\n    summary: \"MMLU/GSM8K 跨架构系统性退步缺乏因果机制分析\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 18\n    last_seen_round: 27\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Critical。Protection valley 分析仅 correlational。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 C2。Remove valley 不够。8B MMLU -5.2pp, 14B GSM8K -20pp。\"}\n      - {round: 25, reviewers: [1, 2], note: \"R25 最高优先级。两个假设仍仅 speculation。\"}\n      - {round: 26, reviewers: [1, 2], note: \"R26 完全共识。退步跨架构一致。\"}\n      - {round: 27, reviewers: [1, 2], note: \"R27 完全共识 Critical。(1) C4 控制仅 1 seed，证据不充分；(2) mode-covering 假说缺乏直接证据（未分析被差异性 prune 的 neuron 功能角色）；(3) KL uniform MMLU 40.7 vs TEAL uniform 45.86，同 allocation 差 5pp 不能用 allocation 解释；(4) 跨 scale 退步 8B→14B GSM8K -1.3→-20.1pp 暗示根本限制。\"}\n    action_items:\n      - {round: 25, action: \"C4 控制实验\", assigned_to: \"main_agent\", status: done}\n      - {round: 26, action: \"Abstract 量化知识退步\", assigned_to: \"paper_agent\", status: done}\n      - {round: 26, action: \"Conclusion 限定为 PPL+commonsense\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"C4 控制实验增至 3+ seed\", assigned_to: \"main_agent\", status: open}\n      - {round: 27, action: \"Knowledge neuron 分析检验被差异性 prune 的 neuron 功能角色\", assigned_to: \"main_agent\", status: open}\n      - {round: 27, action: \"分析 KL uniform vs TEAL uniform MMLU 5pp 差距的具体归因\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R25-N1\"\n    summary: \"方法新颖性边界需更清晰论证\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - {round: 25, reviewers: [2], note: \"核心组件均成熟技术。MaskLLM 已用 KL+Gumbel。\"}\n      - {round: 26, reviewers: [2], note: \"Table 1 需纳入 MaskLLM。\"}\n      - {round: 27, reviewers: [1, 2], note: \"R27 共识。KL+Gumbel recipe 与 MaskLLM 共享。三点区分 valid。新颖性在于 contextual activation sparsity 应用 + 分析框架。'empirical+analytical' 层面，非 methodological 突破。Findings 足够，Main Conference 偏弱。\"}\n    action_items:\n      - {round: 26, action: \"Table 1 加入 MaskLLM\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W2\"\n    summary: \"高方差下游指标统计可靠性不足\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 24\n    last_seen_round: 27\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"ARC-c 95% CI ≈ ±8.9pp。PPL 方差极低。\"}\n      - {round: 25, reviewers: [1, 2], note: \"Qwen-14B GSM8K std=5.2pp。\"}\n      - {round: 26, reviewers: [1, 2], note: \"MMLU 30% global σ=9.5。\"}\n      - {round: 27, reviewers: [1, 2], note: \"R27 R1 升级为 Critical(N2)，R2 维持 Warning 但同意。30% Global MMLU σ=9.5：n=3 95% CI ≈ ±23.6pp 基本无信息量。Abstract/Conclusion 'commonsense gains' 无 'directional' 限定。ARR R5 要求未充分满足。\"}\n    action_items:\n      - {round: 24, action: \"高方差指标加 CI overlap caveat\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"关键对比增加到 5+ seeds 或报告 bootstrap CI\", assigned_to: \"main_agent\", status: open}\n      - {round: 27, action: \"Abstract/Conclusion 'commonsense gains' 加 'directional' 限定\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W3\"\n    summary: \"C1 ablation soft→hard mask representation 残余 confound\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 24\n    last_seen_round: 27\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"Oracle 二值化丢失排序信息。\"}\n      - {round: 26, reviewers: [1, 2], note: \"BCE+Gumbel vs BCE 不足以排除 confound。\"}\n      - {round: 27, reviewers: [1, 2], note: \"R27 共识 Warning。soft→hard 同时改变 mask 来源和表示。BCE+Gumbel(32.22) vs BCE(27.97) 差 15%。R2 指出核心发现仍成立（KL-derived+BCE 远优于 magnitude+BCE 15.71）。建议增加控制实验隔离 mask 来源 vs 表示。s42 gap(0.65pp) vs s123/s456(≤0.03pp) 可能为 provenance artifact。\"}\n    action_items:\n      - {round: 25, action: \"binarization confound caveat\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"增加 magnitude masks 二值化+BCE 控制实验隔离 mask 来源 vs 表示\", assigned_to: \"main_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R25-M1\"\n    summary: \"术语不一致：至少 5 种表述交替使用\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - {round: 25, reviewers: [2], note: \"全文交替使用多种术语。\"}\n      - {round: 26, reviewers: [1, 2], note: \"再次提出。\"}\n      - {round: 27, reviewers: [1, 2], note: \"R27 R2-W2 提出 5 种表述：distillation/alignment/optimization/KL distillation/distribution-matching。R1 交叉同意。\"}\n    action_items:\n      - {round: 25, action: \"全文统一术语\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R26-M3\"\n    summary: \"68% divergence 和 32% Jaccard 同句出现易混淆\"\n    category: writing\n    severity: minor\n    status: open\n    first_raised_round: 26\n    last_seen_round: 27\n    mentions:\n      - {round: 26, reviewers: [1, 2], note: \"Introduction 互补度量同句混淆。\"}\n      - {round: 27, reviewers: [2], note: \"R27 R2-W3 再次提出。\"}\n    action_items:\n      - {round: 26, action: \"统一使用一种表述\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R26-W1\"\n    summary: \"14.5% PPL improvement 引用基准在 Abstract 与 Table 2 不一致\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 26\n    last_seen_round: 27\n    mentions:\n      - {round: 26, reviewers: [1, 2], note: \"Abstract 用 matched-sparsity，Table 2 用 TEAL uniform。\"}\n      - {round: 27, reviewers: [2], note: \"R27 仍可能困惑读者。Table 2 caption 已标注但不够突出。\"}\n    action_items:\n      - {round: 26, action: \"Table 2 caption 标注来源\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 27 — New issues\n  # ============================================================\n\n  - id: \"R27-W1\"\n    summary: \"Abstract/Conclusion 'commonsense gains' 措辞过强缺乏统计限定\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - {round: 27, reviewers: [1, 2], note: \"Section 4.2 说 'directional evidence'，但 Abstract/Conclusion 'commonsense gains' 无此限定。3 seeds 不足支撑。\"}\n    action_items:\n      - {round: 27, action: \"'commonsense gains' 改为 'directional commonsense improvements' 或加统计限定\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R27-W2\"\n    summary: \"Contribution framing 张力：'empirical study' vs 方法性贡献列表\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 27\n    last_seen_round: 27\n    mentions:\n      - {round: 27, reviewers: [2], note: \"反复声明 'empirical study' 但贡献列表含方法性暗示。实际引入了具体方法（KL predictor + Gumbel-Sigmoid for contextual sparsity）。建议承认方法贡献或调整贡献列表措辞。\"}\n    action_items:\n      - {round: 27, action: \"贡献列表措辞统一为实证发现或承认方法贡献\", assigned_to: \"paper_agent\", status: open}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Previously open, not raised in R27\n  # ============================================================\n\n  - id: \"R25-W1\"\n    summary: \"BCE 30% 缺少 uniform allocation 对比\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - {round: 25, reviewers: [1, 2], note: \"Table 2 中 BCE 30% 仅有 global。\"}\n      - {round: 26, reviewers: [1, 2], note: \"R26 确认。\"}\n      - {round: 27, reviewers: [], note: \"R27 未提出。BCE 30% uniform 已加入 Table 2，可能已修复。\"}\n    action_items:\n      - {round: 26, action: \"Table 2 增加 BCE 30% uniform 行\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R25-W2\"\n    summary: \"MSE 50% baseline 仅 seed 42 有效\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 27\n    mentions:\n      - {round: 25, reviewers: [1, 2], note: \"MSE 50% s123 catastrophic。\"}\n      - {round: 27, reviewers: [1], note: \"R27 R1 minor 提及 cherry-pick 风险。Table 4 有脚注但正文易误解。\"}\n    action_items:\n      - {round: 25, action: \"正文使用 MSE 50% 注明 single-seed\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W6\"\n    summary: \"Figure 2 仅展示 global allocation 但推荐 uniform\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 26\n    mentions:\n      - {round: 22, reviewers: [1, 2], note: \"Figure framing 效果强。\"}\n      - {round: 27, reviewers: [], note: \"R27 未提出。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Resolved issues\n  # ============================================================\n\n  - id: \"R19-N3\"\n    summary: \"无实际 wall-clock 加速\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 27\n    mentions:\n      - {round: 22, reviewers: [1, 2], note: \"降为 Warning。\"}\n      - {round: 27, reviewers: [2], note: \"R27 R2-W6 提及但认可 framing。维持 resolved。\"}\n    resolution: \"论文已充分 framed 为 empirical study。\"\n    resolution_round: 23\n\n  - id: \"R24-W1\"\n    summary: \"评估覆盖度空白\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 27\n    mentions:\n      - {round: 27, reviewers: [1], note: \"R1-W3 提出但 R2 [REBUT] 正确——Limitations 已覆盖。\"}\n    resolution: \"Limitations 已明确覆盖全部三个缺口。\"\n    resolution_round: 25\n\n  - id: \"R24-W4\"\n    summary: \"'Primary design dimension' 声明需限定\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 27\n    resolution: \"合并入 R20-N2。Conclusion 已限定。\"\n    resolution_round: 26\n\n  - id: \"R25-W3\"\n    summary: \"19% → 14.5% PPL 数值修正\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 25\n    last_seen_round: 26\n    resolution: \"已修正。基准问题转入 R26-W1。\"\n    resolution_round: 26\n\n  - id: \"R26-M1\"\n    summary: \"8.6%/6.4% 未标注 sparsity level\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 26\n    last_seen_round: 26\n    resolution: \"已加标注。\"\n    resolution_round: 26\n\n  - id: \"R26-M2\"\n    summary: \"'stable downstream' 措辞误导\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 26\n    last_seen_round: 26\n    resolution: \"已删除 'stable'。\"\n    resolution_round: 26\n\n  - id: \"R25-M2\"\n    summary: \"Eq. 4 s_j 缺层标\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 25\n    last_seen_round: 25\n    resolution: \"已补充。\"\n    resolution_round: 25\n\n  - id: \"R19-W1\"\n    summary: \"与 MaskLLM 新颖性区分\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 26\n    resolution: \"合并进 R25-N1。\"\n    resolution_round: 25\n\n  - id: \"R20-W4\"\n    summary: \"WikiText 同分布评估 + C4 OOD\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 26\n    resolution: \"Appendix D OOD 证据充分。\"\n    resolution_round: 25\n\n  - id: \"R22-W3\"\n    summary: \"Table 2 actual sparsity mismatch 脚注\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 26\n    resolution: \"脚注存在。\"\n    resolution_round: 23\n\n  - id: \"R22-W5\"\n    summary: \"规模泛化仅 7-14B\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 26\n    resolution: \"Limitations 已含。\"\n    resolution_round: 25\n\n  - id: \"R19-N2\"\n    summary: \"C1 因果声明\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 24\n    resolution: \"已降级为 transferability。\"\n    resolution_round: 23\n\n  - id: \"R22-W7\"\n    summary: \"Abstract 信息密度\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"已拆分。\"\n    resolution_round: 23\n\n  - id: \"R22-W8\"\n    summary: \"Conclusion 引用 BoolQ\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"改为 HellaSwag/PIQA。\"\n    resolution_round: 23\n\n  - id: \"R19-W7\"\n    summary: \"30% sweet spot 限制\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 26\n    resolution: \"Limitations 已覆盖。\"\n    resolution_round: 25\n\n  - id: \"R15-N3\"\n    summary: \"MaskLLM 新颖性边界\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 26\n    resolution: \"合并进 R25-N1。\"\n    resolution_round: 23"
  }
}
```

</details>

---


### Tool result

_source line 2183 · 2026-05-23T07:44:22.722201+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml\", \"bytes\": 14576}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2184 · 2026-05-23T07:46:36.696967+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 27 审稿报告 (Fresh Review)\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**Venue**: EMNLP 2026 (ARR May 2026), Long Paper\n**Reviewer 编排**: 2 人（R1 方法严谨性+实验设计, R2 新颖性+完整性+写作）\n**交叉分享**: 完成（R2 提交完整 [AGREE]/[REBUT] 回应；R1 提交摘要回应）\n\n---\n\n## Summary\n\n本文提出用前向 KL 散度替代传统 BCE 训练 SwiGLU LLM 的上下文稀疏性预测器（<1% 参数开销）。在 LLaMA-3.1-8B 上 30% 稀疏度下，KL predictor 实现 14.5% PPL 改进（matched sparsity），跨 Mistral-7B 和 Qwen-2.5-14B 一致泛化。论文通过 target-swap ablation（C1）和 per-layer KL 控制（K=1/K=4）尝试分解 signal type vs coupling scope 的贡献，但该分解受 train-inference mismatch 严重 confound。知识密集任务出现系统性退化（MMLU −5.2pp/8B, GSM8K −20.1pp/14B），机制未获因果解释。\n\n---\n\n## Strengths\n\n**S1. 跨架构一致的 PPL 改进** [R1/R2 共识]\nKL predictor 在 LLaMA-3.1-8B（14.5%）、Mistral-7B（17.3%）、Qwen-2.5-14B 上均展示一致的 PPL 优势，在多稀疏度（30-70%）和 OOD（C4）条件下均成立。这是本文最 robust 的发现。\n\n**S2. 罕见的消融深度** [R1/R2 共识]\n20+ 页附录（Appendix A-W）系统性消融几乎每个设计维度，在同类工作中极为罕见，体现严谨的实验方法论。\n\n**S3. Target-swap ablation (C1) 设计巧妙** [R1/R2 共识]\n通过在 BCE 上训练 KL 发现的 oracle masks，分离 \"mask 质量\" 与 \"训练机制\" 的贡献。C1 在 50% 下与 KL 仅差 ≤0.79pp，在 30% 3-seed 下 ≤1.70pp，说明 KL 的优势主要来自发现了更好的 mask patterns。\n\n**S4. 诚实的负面结果报告** [R1/R2 共识]\nMMLU −5.2pp、GSM8K −20.1pp、MSE catastrophic seed（PPL=15,789）、MMLU 高方差（σ=9.5）等不利结果在 Abstract、正文和 Limitations 中坦承报告。\n\n**S5. 有用的概念框架** [R1/R2 共识]\nTable 1 的 Prediction Target × Training Signal Coupling taxonomy 为后续工作提供清晰的分析框架。\n\n**S6. 高可复现性** [R1/R2 共识]\n训练配置、硬件规格、seed 信息、评估协议均有完整记录，承诺开源。Reproducibility 4/5。\n\n---\n\n## Weaknesses\n\n### Critical\n\n**C1. K=1 signal type 分解受 train-inference mismatch 严重 confound** [R1-N1, R2-N1 完全共识]\nK=1 训练时仅 1/32 层被 mask，推理时 32/32 层全部 mask，造成严重 distribution shift。K=4 修正不充分（仍仅 12.5%），且 K=4 MMLU 系统性超过 E2E（42.7±1.4 vs 40.7±1.3 across all 3 seeds），说明 mismatch 引入不可预测 artifact。K-curve（K=1,2,8,16,32）中除 K=4 外均为 single-seed (s42)，论文自承 \"should be treated as preliminary\"。K=16 PPL（8.67）优于 E2E（8.81）的 non-monotonic pattern 可能是 seed-specific artifact。论文标注 \"upper bound\" 但 mismatch 方向可能系统性高估 signal type 贡献（K=1 在近 dense 条件下训练更容易）。Signal type vs coupling scope 分解是论文超越 \"换 loss function\" 的核心分析贡献；如果不可靠，理论洞察价值大幅缩水。\n\n**C2. \"Primary design dimension\" claim 泛化性不足** [R2-N1, R1 共识]\n结论称 \"Output-distribution alignment is the primary design dimension at moderate sparsity\"，但在知识密集任务上 magnitude-based TEAL 始终优于 KL predictor：MMLU（45.86 vs 40.7, −5.2pp）、GSM8K（8.79 vs 7.5）。跨架构信号混合：Mistral MMLU 持平；Qwen-14B GSM8K −20.1pp。Claim 仅在 PPL + commonsense 维度成立。\n\n**C3. Knowledge-task regression 缺乏因果解释** [R1-W2, R2-N2 完全共识]\nC4 控制实验否定了训练数据偏差假说但仅 1 seed。\"Mode-covering dilutes rare activations\" 仅是推测，缺乏直接证据。关键数据点：KL uniform MMLU 40.7 vs TEAL uniform 45.86（同为 uniform allocation），5pp 差距不能用 allocation 解释，必须归因于 KL loss 本身。跨 scale 退步（8B→14B GSM8K 从 −1.3pp 到 −20.1pp）暗示方法根本限制但未提供缓解路径。\n\n### Warning\n\n**W1. 3-seed 下游指标统计功效不足** [R1-N2, R2-W5 共识]\n30% Global MMLU σ=9.5pp：n=3 下 95% CI ≈ ±23.6pp（t-distribution, df=2），基本无统计信息量。Abstract/Conclusion 中 \"commonsense gains\" 措辞未带 Section 4.2 中的 \"directional evidence\" 限定。按 ARR guidelines R5 要求 error bars / significance tests，论文未充分满足。\n\n**W2. C1 target-swap ablation 存在未隔离混淆变量** [R1-W1, R2 部分同意]\nSoft→hard 二值化同时改变 mask 来源和 mask 表示。BCE+Gumbel（32.22）vs 标准 BCE（27.97）差 15% 说明 Gumbel 表示本身有显著影响。但 R2 指出核心发现仍成立：KL-derived hard masks + BCE 仍远优于 magnitude-derived masks + BCE（15.71 at 30%），mask 质量是关键因素。缺少控制实验隔离 mask 来源 vs mask 表示。\n\n**W3. 术语一致性问题** [R2-W2, R1 交叉同意]\n核心概念至少 5 种表述：output-distribution distillation / alignment / optimization / KL distillation / distribution-matching。应统一为一个主术语。\n\n**W4. Contribution framing 存在张力** [R2-W1]\n反复声明 \"primarily an empirical study\" 但贡献列表包含方法性暗示。实际引入了具体方法（KL predictor + Gumbel-Sigmoid for contextual sparsity），不仅仅是比较现有方法。\n\n**W5. Wall-clock speedup 缺失** [R2-W6]\nPredictor 增加 6.4% latency，当前方法增加而非减少延迟。论文已正确 frame 为 analytical contribution，但缺乏理论加速估算。\n\n### Minor\n\n- **M1**: Introduction 中 68% divergence 和 32% Jaccard 同句出现混淆\n- **M2**: \"the first decomposition\" 措辞应更审慎\n- **M3**: Table 2 caption 信息过载（3 个脚注标记 + 多个解释条款）\n- **M4**: Introduction MMLU 40.7±1.3% 无 dense baseline 对比（dense 65.27%）\n- **M5**: MSE 50% 仅报告 s42，s123 catastrophic（PPL=15,789），正文讨论容易误解为 robust finding\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键判断上完全一致：\n1. **PPL 改进 robust 且一致**——跨 3 架构、多稀疏度、OOD\n2. **K=1 signal type 分解存在 train-inference mismatch confound**——K=4 修正不充分，K-curve 多数 single-seed\n3. **3-seed 不足以支撑下游 claims**——Abstract/Conclusion 措辞需加统计限定\n4. **Knowledge regression 缺乏因果解释**——C4 控制 1 seed 不够，mode-covering 假说未验证\n5. **新颖性为组合级别**——KL + Gumbel-Sigmoid recipe 与 MaskLLM 共享，新颖性在于 contextual activation sparsity 应用 + 分析框架\n6. **Findings 级别贡献**（3.0–3.5 区间）\n\n## Reviewer Divergence [已解决]\n\n| 争议点 | R1 | R2 | 裁定 |\n|--------|----|----|------|\n| R1-W3: Limitations 是否覆盖实验缺口 | 未覆盖 | [REBUT] 已覆盖（generation, seq_len, batch） | R2 正确——Limitations page 9 明确含三点 |\n| R1-W4: Table 14 数值不一致 | 50% Global MMLU=35.7±9.5 vs 28.3±0.7 | [REBUT] R1 误读行标签，35.7±9.5 是 30% Global | R2 正确——经核实数据一致 |\n| R1-Minor-1: SNR 叙事张力 | coupling 应提高 SNR | [REBUT] 论文叙事是 \"despite lower SNR\" | R2 正确——Section 3.6 明确 |\n\n---\n\n## Questions\n\n1. K=4 MMLU 超过 E2E 的机制？如果来自 allocation artifact，意味对知识任务 allocation 可能比 signal type 更重要，这对 \"primary design dimension\" 结论意味什么？\n2. KL uniform MMLU 40.7 vs TEAL uniform 45.86（同 allocation），5pp 差距是否完全归因于 KL loss 本身？与 \"allocation contributes\" 的解释矛盾。\n3. Compensation network 为何不能恢复 knowledge-intensive 性能？\n4. C1 中 s42 oracle provenance 对结果的影响（s42 gap 0.65pp vs s123/s456 ≤0.03pp）？\n5. Forward vs Reverse KL 在 30% 下差异（8.81 vs 9.26）有统计显著性吗？JSD≈Forward KL (8.90 vs 8.81) 暗示 divergence 选择影响不大。\n\n## Missing References\n\n两位 Reviewer 均未发现重大遗漏。Related Work 覆盖了 TEAL、DejaVu、MaskLLM、CATS、R-Sparse、FastForward、SVD-CSP、LaRoSA、COTS、SparseInfer、ProSparse、SparseLoRA 等 2024-2026 主要工作。\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求。\n\n## Visual Layout Check（非评分项）\n\n状态：**已完成** (3 warnings, 16 info, 0 critical)\n\n- **[warning] Page 6**: 整页纯文本（Experiments 设置），建议将部分移至 Appendix 或穿插示意图\n- **[warning] Page 7**: 单页 3 个表格（Table 2/3/4），视觉密集拥挤，考虑将其中一个移至下页\n- **[warning] Page 20**: 末页仅 ~13 行（<15% 利用率），大量空白\n- 正文在第 8 页内结束，符合 EMNLP/ACL 8 页限制 ✓\n- Tables 使用 booktabs 风格，格式规范 ✓\n- References 格式统一，无未解析引用 ✓\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Overall | 3.5 | 3.0 | 3.0 |\n| Soundness | 3/5 | 3/5 | 3/5 |\n| Excitement | 3/5 | 3/5 | 3/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**理由**：论文提供了有价值的实证发现——KL distillation 一致且显著地优于 BCE 用于稀疏性预测（PPL 层面），实验设计深度罕见，负面结果报告诚实。但三个 critical 问题限制了接收级别：(1) signal type 分解（论文的核心分析贡献）受 K=1 train-inference mismatch 严重 confound，K-curve 多数 single-seed，结论可靠性不足；(2) \"primary design dimension\" claim 在知识任务上不成立（TEAL 始终优于 KL），泛化性不足；(3) knowledge regression 跨架构/跨 scale 一致但缺乏因果解释。新颖性为组合级别（已知组件的新应用），非方法论突破。实用贡献（KL > BCE for PPL）足以进入 Findings，但分析性 claims 的可靠性问题阻止 Conference 接收。\n\n**提升至 Conference (3.5–4.0) 的路径**：\n1. K-curve 全部 K 值做 3-seed（计算开销低，每个 K 仅需 1000 steps × 3 seeds）\n2. 将 \"primary design dimension\" 明确限定为 \"for PPL and commonsense at moderate sparsity\"\n3. Knowledge regression 增加因果分析（knowledge neuron probe 或 mixed-domain training）\n4. Abstract/Conclusion 下游声明加统计限定语（\"directional\"）\n5. C4 控制实验增至 3+ seed\n\n---\n\n## Detailed Comments\n\n**Abstract**: 信息密度高，两个问题：(1) \"commonsense gains\" 未带 \"directional\" 限定；(2) 14.5% PPL 引用基准（matched-sparsity, Appendix D）在 Table 2 中找不到（Table 2 TEAL uniform 30%=10.82 对应 18.6%），呈现方式可能困惑读者。\n\n**Introduction**: (1) \"diverge 68%... (per-layer Jaccard 32%)\" 是互补度量同句混淆；(2) \"MMLU 40.7±1.3%\" 无 dense baseline 不传达退化幅度；(3) \"the first decomposition\" 应改为 \"a systematic decomposition\"。\n\n**Method (Section 3)**: 技术叙述清晰，公式正确。Gradient analysis 提供有用直觉但 KL 的优势不来自更清晰的梯度信号（SNR 一致低于 BCE）。\n\n**Experiments (Section 4)**: 核心 PPL 实验设计合理。Section 4.5 per-layer KL 分解是最重要也最有争议的部分——需降级为 \"exploratory analysis with acknowledged confounds\"。Section 4.2 knowledge regression 讨论诚实但不充分——KL uniform vs TEAL uniform 在 MMLU 上 5pp 差距的归因未分析。\n\n**Related Work (Section 2)**: 覆盖全面，与 MaskLLM 的三点区分具体且技术性强。\n\n**Conclusion**: \"primary design dimension\" 应限定适用范围为 PPL + commonsense。\n\n**Limitations**: 覆盖充分（sparsity sweet spot, knowledge regression, training data, generation tasks, seq_len, batched inference），简洁有效。\n\n**Appendix**: 极为丰富（A-W），体现实验严谨性。K-curve（Appendix W）多数 single-seed 限制了分解结论的可靠性。",
  "project": "distill_sparse_swiglu",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 27 审稿报告 (Fresh Review)\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**Venue**: EMNLP 2026 (ARR May 2026), Long Paper\n**Reviewer 编排**: 2 人（R1 方法严谨性+实验设计, R2 新颖性+完整性+写作）\n**交叉分享**: 完成（R2 提交完整 [AGREE]/[REBUT] 回应；R1 提交摘要回应）\n\n---\n\n## Summary\n\n本文提出用前向 KL 散度替代传统 BCE 训练 SwiGLU LLM 的上下文稀疏性预测器（<1% 参数开销）。在 LLaMA-3.1-8B 上 30% 稀疏度下，KL predictor 实现 14.5% PPL 改进（matched sparsity），跨 Mistral-7B 和 Qwen-2.5-14B 一致泛化。论文通过 target-swap ablation（C1）和 per-layer KL 控制（K=1/K=4）尝试分解 signal type vs coupling scope 的贡献，但该分解受 train-inference mismatch 严重 confound。知识密集任务出现系统性退化（MMLU −5.2pp/8B, GSM8K −20.1pp/14B），机制未获因果解释。\n\n---\n\n## Strengths\n\n**S1. 跨架构一致的 PPL 改进** [R1/R2 共识]\nKL predictor 在 LLaMA-3.1-8B（14.5%）、Mistral-7B（17.3%）、Qwen-2.5-14B 上均展示一致的 PPL 优势，在多稀疏度（30-70%）和 OOD（C4）条件下均成立。这是本文最 robust 的发现。\n\n**S2. 罕见的消融深度** [R1/R2 共识]\n20+ 页附录（Appendix A-W）系统性消融几乎每个设计维度，在同类工作中极为罕见，体现严谨的实验方法论。\n\n**S3. Target-swap ablation (C1) 设计巧妙** [R1/R2 共识]\n通过在 BCE 上训练 KL 发现的 oracle masks，分离 \"mask 质量\" 与 \"训练机制\" 的贡献。C1 在 50% 下与 KL 仅差 ≤0.79pp，在 30% 3-seed 下 ≤1.70pp，说明 KL 的优势主要来自发现了更好的 mask patterns。\n\n**S4. 诚实的负面结果报告** [R1/R2 共识]\nMMLU −5.2pp、GSM8K −20.1pp、MSE catastrophic seed（PPL=15,789）、MMLU 高方差（σ=9.5）等不利结果在 Abstract、正文和 Limitations 中坦承报告。\n\n**S5. 有用的概念框架** [R1/R2 共识]\nTable 1 的 Prediction Target × Training Signal Coupling taxonomy 为后续工作提供清晰的分析框架。\n\n**S6. 高可复现性** [R1/R2 共识]\n训练配置、硬件规格、seed 信息、评估协议均有完整记录，承诺开源。Reproducibility 4/5。\n\n---\n\n## Weaknesses\n\n### Critical\n\n**C1. K=1 signal type 分解受 train-inference mismatch 严重 confound** [R1-N1, R2-N1 完全共识]\nK=1 训练时仅 1/32 层被 mask，推理时 32/32 层全部 mask，造成严重 distribution shift。K=4 修正不充分（仍仅 12.5%），且 K=4 MMLU 系统性超过 E2E（42.7±1.4 vs 40.7±1.3 across all 3 seeds），说明 mismatch 引入不可预测 artifact。K-curve（K=1,2,8,16,32）中除 K=4 外均为 single-seed (s42)，论文自承 \"should be treated as preliminary\"。K=16 PPL（8.67）优于 E2E（8.81）的 non-monotonic pattern 可能是 seed-specific artifact。论文标注 \"upper bound\" 但 mismatch 方向可能系统性高估 signal type 贡献（K=1 在近 dense 条件下训练更容易）。Signal type vs coupling scope 分解是论文超越 \"换 loss function\" 的核心分析贡献；如果不可靠，理论洞察价值大幅缩水。\n\n**C2. \"Primary design dimension\" claim 泛化性不足** [R2-N1, R1 共识]\n结论称 \"Output-distribution alignment is the primary design dimension at moderate sparsity\"，但在知识密集任务上 magnitude-based TEAL 始终优于 KL predictor：MMLU（45.86 vs 40.7, −5.2pp）、GSM8K（8.79 vs 7.5）。跨架构信号混合：Mistral MMLU 持平；Qwen-14B GSM8K −20.1pp。Claim 仅在 PPL + commonsense 维度成立。\n\n**C3. Knowledge-task regression 缺乏因果解释** [R1-W2, R2-N2 完全共识]\nC4 控制实验否定了训练数据偏差假说但仅 1 seed。\"Mode-covering dilutes rare activations\" 仅是推测，缺乏直接证据。关键数据点：KL uniform MMLU 40.7 vs TEAL uniform 45.86（同为 uniform allocation），5pp 差距不能用 allocation 解释，必须归因于 KL loss 本身。跨 scale 退步（8B→14B GSM8K 从 −1.3pp 到 −20.1pp）暗示方法根本限制但未提供缓解路径。\n\n### Warning\n\n**W1. 3-seed 下游指标统计功效不足** [R1-N2, R2-W5 共识]\n30% Global MMLU σ=9.5pp：n=3 下 95% CI ≈ ±23.6pp（t-distribution, df=2），基本无统计信息量。Abstract/Conclusion 中 \"commonsense gains\" 措辞未带 Section 4.2 中的 \"directional evidence\" 限定。按 ARR guidelines R5 要求 error bars / significance tests，论文未充分满足。\n\n**W2. C1 target-swap ablation 存在未隔离混淆变量** [R1-W1, R2 部分同意]\nSoft→hard 二值化同时改变 mask 来源和 mask 表示。BCE+Gumbel（32.22）vs 标准 BCE（27.97）差 15% 说明 Gumbel 表示本身有显著影响。但 R2 指出核心发现仍成立：KL-derived hard masks + BCE 仍远优于 magnitude-derived masks + BCE（15.71 at 30%），mask 质量是关键因素。缺少控制实验隔离 mask 来源 vs mask 表示。\n\n**W3. 术语一致性问题** [R2-W2, R1 交叉同意]\n核心概念至少 5 种表述：output-distribution distillation / alignment / optimization / KL distillation / distribution-matching。应统一为一个主术语。\n\n**W4. Contribution framing 存在张力** [R2-W1]\n反复声明 \"primarily an empirical study\" 但贡献列表包含方法性暗示。实际引入了具体方法（KL predictor + Gumbel-Sigmoid for contextual sparsity），不仅仅是比较现有方法。\n\n**W5. Wall-clock speedup 缺失** [R2-W6]\nPredictor 增加 6.4% latency，当前方法增加而非减少延迟。论文已正确 frame 为 analytical contribution，但缺乏理论加速估算。\n\n### Minor\n\n- **M1**: Introduction 中 68% divergence 和 32% Jaccard 同句出现混淆\n- **M2**: \"the first decomposition\" 措辞应更审慎\n- **M3**: Table 2 caption 信息过载（3 个脚注标记 + 多个解释条款）\n- **M4**: Introduction MMLU 40.7±1.3% 无 dense baseline 对比（dense 65.27%）\n- **M5**: MSE 50% 仅报告 s42，s123 catastrophic（PPL=15,789），正文讨论容易误解为 robust finding\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键判断上完全一致：\n1. **PPL 改进 robust 且一致**——跨 3 架构、多稀疏度、OOD\n2. **K=1 signal type 分解存在 train-inference mismatch confound**——K=4 修正不充分，K-curve 多数 single-seed\n3. **3-seed 不足以支撑下游 claims**——Abstract/Conclusion 措辞需加统计限定\n4. **Knowledge regression 缺乏因果解释**——C4 控制 1 seed 不够，mode-covering 假说未验证\n5. **新颖性为组合级别**——KL + Gumbel-Sigmoid recipe 与 MaskLLM 共享，新颖性在于 contextual activation sparsity 应用 + 分析框架\n6. **Findings 级别贡献**（3.0–3.5 区间）\n\n## Reviewer Divergence [已解决]\n\n| 争议点 | R1 | R2 | 裁定 |\n|--------|----|----|------|\n| R1-W3: Limitations 是否覆盖实验缺口 | 未覆盖 | [REBUT] 已覆盖（generation, seq_len, batch） | R2 正确——Limitations page 9 明确含三点 |\n| R1-W4: Table 14 数值不一致 | 50% Global MMLU=35.7±9.5 vs 28.3±0.7 | [REBUT] R1 误读行标签，35.7±9.5 是 30% Global | R2 正确——经核实数据一致 |\n| R1-Minor-1: SNR 叙事张力 | coupling 应提高 SNR | [REBUT] 论文叙事是 \"despite lower SNR\" | R2 正确——Section 3.6 明确 |\n\n---\n\n## Questions\n\n1. K=4 MMLU 超过 E2E 的机制？如果来自 allocation artifact，意味对知识任务 allocation 可能比 signal type 更重要，这对 \"primary design dimension\" 结论意味什么？\n2. KL uniform MMLU 40.7 vs TEAL uniform 45.86（同 allocation），5pp 差距是否完全归因于 KL loss 本身？与 \"allocation contributes\" 的解释矛盾。\n3. Compensation network 为何不能恢复 knowledge-intensive 性能？\n4. C1 中 s42 oracle provenance 对结果的影响（s42 gap 0.65pp vs s123/s456 ≤0.03pp）？\n5. Forward vs Reverse KL 在 30% 下差异（8.81 vs 9.26）有统计显著性吗？JSD≈Forward KL (8.90 vs 8.81) 暗示 divergence 选择影响不大。\n\n## Missing References\n\n两位 Reviewer 均未发现重大遗漏。Related Work 覆盖了 TEAL、DejaVu、MaskLLM、CATS、R-Sparse、FastForward、SVD-CSP、LaRoSA、COTS、SparseInfer、ProSparse、SparseLoRA 等 2024-2026 主要工作。\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求。\n\n## Visual Layout Check（非评分项）\n\n状态：**已完成** (3 warnings, 16 info, 0 critical)\n\n- **[warning] Page 6**: 整页纯文本（Experiments 设置），建议将部分移至 Appendix 或穿插示意图\n- **[warning] Page 7**: 单页 3 个表格（Table 2/3/4），视觉密集拥挤，考虑将其中一个移至下页\n- **[warning] Page 20**: 末页仅 ~13 行（<15% 利用率），大量空白\n- 正文在第 8 页内结束，符合 EMNLP/ACL 8 页限制 ✓\n- Tables 使用 booktabs 风格，格式规范 ✓\n- References 格式统一，无未解析引用 ✓\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Overall | 3.5 | 3.0 | 3.0 |\n| Soundness | 3/5 | 3/5 | 3/5 |\n| Excitement | 3/5 | 3/5 | 3/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**理由**：论文提供了有价值的实证发现——KL distillation 一致且显著地优于 BCE 用于稀疏性预测（PPL 层面），实验设计深度罕见，负面结果报告诚实。但三个 critical 问题限制了接收级别：(1) signal type 分解（论文的核心分析贡献）受 K=1 train-inference mismatch 严重 confound，K-curve 多数 single-seed，结论可靠性不足；(2) \"primary design dimension\" claim 在知识任务上不成立（TEAL 始终优于 KL），泛化性不足；(3) knowledge regression 跨架构/跨 scale 一致但缺乏因果解释。新颖性为组合级别（已知组件的新应用），非方法论突破。实用贡献（KL > BCE for PPL）足以进入 Findings，但分析性 claims 的可靠性问题阻止 Conference 接收。\n\n**提升至 Conference (3.5–4.0) 的路径**：\n1. K-curve 全部 K 值做 3-seed（计算开销低，每个 K 仅需 1000 steps × 3 seeds）\n2. 将 \"primary design dimension\" 明确限定为 \"for PPL and commonsense at moderate sparsity\"\n3. Knowledge regression 增加因果分析（knowledge neuron probe 或 mixed-domain training）\n4. Abstract/Conclusion 下游声明加统计限定语（\"directional\"）\n5. C4 控制实验增至 3+ seed\n\n---\n\n## Detailed Comments\n\n**Abstract**: 信息密度高，两个问题：(1) \"commonsense gains\" 未带 \"directional\" 限定；(2) 14.5% PPL 引用基准（matched-sparsity, Appendix D）在 Table 2 中找不到（Table 2 TEAL uniform 30%=10.82 对应 18.6%），呈现方式可能困惑读者。\n\n**Introduction**: (1) \"diverge 68%... (per-layer Jaccard 32%)\" 是互补度量同句混淆；(2) \"MMLU 40.7±1.3%\" 无 dense baseline 不传达退化幅度；(3) \"the first decomposition\" 应改为 \"a systematic decomposition\"。\n\n**Method (Section 3)**: 技术叙述清晰，公式正确。Gradient analysis 提供有用直觉但 KL 的优势不来自更清晰的梯度信号（SNR 一致低于 BCE）。\n\n**Experiments (Section 4)**: 核心 PPL 实验设计合理。Section 4.5 per-layer KL 分解是最重要也最有争议的部分——需降级为 \"exploratory analysis with acknowledged confounds\"。Section 4.2 knowledge regression 讨论诚实但不充分——KL uniform vs TEAL uniform 在 MMLU 上 5pp 差距的归因未分析。\n\n**Related Work (Section 2)**: 覆盖全面，与 MaskLLM 的三点区分具体且技术性强。\n\n**Conclusion**: \"primary design dimension\" 应限定适用范围为 PPL + commonsense。\n\n**Limitations**: 覆盖充分（sparsity sweet spot, knowledge regression, training data, generation tasks, seq_len, batched inference），简洁有效。\n\n**Appendix**: 极为丰富（A-W），体现实验严谨性。K-curve（Appendix W）多数 single-seed 限制了分解结论的可靠性。",
    "project": "distill_sparse_swiglu",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
  }
}
```

</details>

---


### Tool result

_source line 2185 · 2026-05-23T07:46:40.716548+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbbf8d2c695f1e79e11713aebc107790:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4019
}
```

</details>

---


### Assistant

_source line 2186 · 2026-05-23T07:46:51.851221+00:00_

审稿报告已投递至 Research Director。

**Round 27 审稿完成。**

- **Overall Score: 3.0 (Findings)**
- **Reviewer 1**: 3.5 (Borderline Conference) | **Reviewer 2**: 3.0 (Findings)
- **交叉分享**: 完成，3 个 REBUT 均已解决（R2 方均正确）
- **关键共识**：
  - PPL 改进 robust 且跨架构一致（最强优点）
  - K=1 signal type 分解受 train-inference mismatch 严重 confound（最关键弱点）
  - Knowledge regression 跨架构一致但缺乏因果解释
  - 3-seed 不足以支撑下游方向性声明
  - 新颖性为组合级别，Findings 足够但 Conference 偏弱
- **Issue Tracker**: 已更新（12 个活跃 issue，2 个新增，14 个已解决）
- **视觉审查**: 3 warnings（page 6 纯文本、page 7 三表拥挤、page 20 空白过多）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 192

## Round 192

2 recorded events


### User

_source line 2187 · 2026-05-23T07:46:51.856520+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Strengths 回应

**[AGREE] R2-S1**: C1 target-swap ablation 确实是本文最巧妙的实验设计。50% 下 ≤0.79pp 的 gap 有说服力（Table 3, 3-seed）。但我补充一个 caveat：C1 存在 soft→hard binarization confound（我的 W1），BCE+Gumbel PPL=32.22 vs 标准 BCE PPL=27.97（Table 3 脚注区域）显示表示形式本身有 ~15% 的影响，C1 并未干净隔离 "mask 质量" 与 "mask 表示"。不过作为 upper bound 证据仍然有价值。

**[AGREE] R2-S2**: K=1 per-layer KL 的数字准确（9.05±0.02 vs MSE 18.52±1.68, Appendix R Table 18）。但我与 R2 的保留程度不同——这组数字受 train-inference mismatch 严重影响（我的 N1），作为 "分析框架" 有启发性，但作为 "分解结果" 不可靠。

**[AGREE] R2-S3**: 与我的 Strength 3 一致。论文报告负面结果（knowledge regression, MSE catastrophic seed, MMLU 高方差）的坦率态度在同类工作中突出。

**[AGREE] R2-S4**: Related Work 覆盖了 2024-2026 的主要工作（TEAL, DejaVu, MaskLLM, CATS, R-Sparse, FastForward, SVD-CSP 等），无明显遗漏。

**[AGREE] R2-S5**: 附录实际约 9 页（pages 12-20），覆盖 23 个子节（A-W），在同类工作中罕见。

---

### Must-Fix 回应

**[AGREE] R2-N1**: "Primary design dimension" claim 泛化性不足

R2 的批评准确且与我的审查一致。具体证据：

1. **Conclusion 原文**（page 8, Section 5）："Output-distribution alignment is the primary design dimension at moderate sparsity: signal type accounts for most of the PPL gap (upper bound), with coupling contributing task-dependently"——此表述未限定 task 类型，暗示对所有任务成立。

2. **跨架构信号混合**：
   - Mistral-7B-v0.3（Appendix N, Table 16）：PPL 优势 −17.3% 确认，但 R2 指出 MMLU 持平，说明 PPL 改进不迁移到 knowledge tasks
   - Qwen-2.5-14B（Appendix K, Table 13）：GSM8K −20.1pp 的退步更为严重

3. **Table 2 中 TEAL MMLU > KL MMLU**：在同为 30% uniform allocation 的条件下，TEAL 的 MMLU 显著优于 KL predictor（R2 引用 45.86 vs 40.7），说明 magnitude-based 方法在 knowledge tasks 上系统性优于 output-distribution alignment。

建议修改 Conclusion 为："Output-distribution alignment is the primary design dimension **for perplexity and commonsense reasoning** at moderate sparsity"，并在 Abstract 中做对应限定。

**[AGREE] R2-N2**: 知识任务退化缺乏因果解释——我升级我自己的评估

R2 的分析比我的 W2 更尖锐，我升级对此问题的评估：

1. **R2-Q3 提出的 uniform-vs-uniform 对比是关键论据**：KL MMLU 40.7 vs TEAL MMLU ~45.86，两者都用 uniform allocation。如果 allocation 相同，5pp 的 gap 只能归因于 KL objective 本身选择了不同的 neuron 被 prune。这直接反驳了论文 Section 4.2 的 "Constraint experiments (Appendix T) confirm allocation contributes" 叙事——allocation 可能有贡献，但不是主因。

2. **C4 控制实验（Appendix V）仅 1-seed (s42)** 不足以排除 seed artifact。论文的 "the deficit is structural to distribution-matching" 结论缺乏统计基础。

3. **缺乏直接机制证据**："forward KL's mode-covering property dilutes rare activations" 是合理的假说，但论文未做 knowledge neuron 分析（Meng et al., 2022 的方法论可以直接应用）来验证。与 magnitude-based masks 的 46-69% Jaccard 距离（Section 4.4）进一步支持"KL 选择了不同的 neuron"，但哪些 neuron 被差异性 prune 了、它们是否编码知识，这一步关键分析缺失。

综合来看，我同意 R2 将此列为 Must-Fix。

---

### Should-Fix 回应

**[AGREE] R2-W1**: Contribution framing 张力

Section 2 末尾列出四点贡献，第一点 "An output-distribution alignment ranking across five losses" 读起来像方法贡献，而 Limitations（page 9）明确说 "This is primarily an empirical study"。两处定位不一致。建议统一为 "empirical study with analytical contributions"。

**[AGREE] R2-W2**: 术语一致性问题

我在阅读中也注意到核心概念至少有以下表述："output-distribution distillation"（Title）、"output-distribution alignment"（Section 5）、"KL distillation"（Abstract）、"forward KL"（Section 3.6）、"coupled KL"（Table 1）。对同一概念使用 5 种措辞增加了阅读认知负担。建议选定一个 primary term 并在首次出现时明确其他为同义。

**[AGREE] R2-W3**: Introduction 中 divergence/Jaccard 数值表述可改进

Section 4.4（page 7）中 "per-layer Jaccard distance averages 68% at 50% ... with cross-seed variation (36.3%)" 确实可能让读者混淆——68% 是 KL-vs-magnitude 的 inter-method distance，36.3% 是 KL masks 自身的 intra-method variation（cross-seed）。两个不同维度的百分比在同一句中出现，需要更清晰地区分。

**[AGREE] R2-W4**: MSE 50% 单种子不可靠

与我的 minor point 一致。s123 catastrophic failure (PPL=15,789) 本身有信息价值（说明 MSE 训练不稳定），但 Table 4 仅报告 s42 结果容易被解读为 cherry-pick。建议在 Table 4 的 MSE 行添加脚注说明其他 seed 结果和失败原因分析。

**[AGREE] R2-W5**: "commonsense gains" 措辞过强

与我的 N2 一致。3-seed 下游指标在 n=3 时统计功效不足。以 ARC-c 为例（Table 2 中 KL 30% uniform 约 40.6 vs BCE ~38?），即使方向正确，3-seed 的 95% CI 宽度（~±2.9pp with t_{0.025,2}=4.303）使得差异不显著。"consistent commonsense gains" 应改为 "commonsense metrics show a positive trend, though statistical significance cannot be established with three seeds"。

**[AGREE] R2-W6**: Wall-clock speedup 缺失

与我的 W3/Q3 一致。Appendix A (Table 5) 仅报告 predictor overhead 和 batch_size=1 的推理延迟，未报告 sparse FFN kernel 的实际加速。对于一篇关于稀疏推理加速的论文，缺少端到端 wall-clock speedup 数据是明显短板。

---

### Minor 回应

**[AGREE] R2-M1**: Table 2 caption 确实信息密度过高（sparsity 说明、seed 信息、对比说明、appendix 引用都压缩在 caption 中）。建议将 footnote 信息移至正文或 table notes。

**[AGREE] R2-M2**: Figure 2 caption 中 "82% at 70%" 作为单个数据点引用，没有上下文说明其意义（是 performance retention？relative to dense？）。应补充说明。

**[REBUT] R2-M3**: Geometric penalty ε=0.02 有部分 justification

Section 3.5（page 5, Eq. 7）明确定义了 ε=0.02 的功能："a deadzone margin that suppresses oscillation near the target"。Appendix C（Table 9）显示 actual sparsity 在所有测试 target 下均在 target ± 2% 以内，间接验证了 ε 选择的合理性。此外 Appendix B.1 显示温度 schedule 对 PPL 影响 <1.8（Table 7），表明方法对超参不敏感。不过我同意一个 ε sensitivity sweep（如 ε ∈ {0.01, 0.02, 0.05}）会更完整。

**[AGREE] R2-M4**: Introduction 中 "MMLU 40.7±1.3%" 确实缺少 dense baseline 对比。读者需要知道 dense MMLU ≈ 45.9%（从 Table 2 推断）才能理解 −5.2pp 的退步幅度。建议改为 "MMLU 40.7±1.3% (dense: 45.9%, −5.2pp)"。

---

### Questions 回应

**[REBUT partially] R2-Q1**: K=4 在 50% 下 worse than K=1 的机制

R2 的问题有道理，但我认为这可以从论文已有信息中合理解释。K=4 在 50% 下 mask 4/32 层，比 K=1 的 1/32 层更多。但 K=4 的 mismatch（4/32 训练 vs 32/32 推理）仍然很大，且 K=4 在训练中引入更多 sparsity 噪声——每步同时优化 4 层的 mask 可能导致梯度信号更嘈杂。此外 Appendix S（Table 19）显示 K=4 的 actual sparsity 为 s≈0.001（接近 uniform），与 K=1 的分布不同，这种 sparsity distribution 差异本身就是 confound。不过这进一步说明 K-decomposition 的可靠性有限（我的 N1），R2 的质疑是合理的。

**[AGREE] R2-Q2**: K=4 MMLU 超越 E2E 是关键 artifact 证据

这与我的 N1 一致。如果 K=4 per-layer 训练在 MMLU 上优于 E2E KL（Table 19），那么 signal type decomposition 的前提——E2E 严格优于 per-layer——在知识任务上不成立。论文将此归因于 "K=4 near-uniform per-layer sparsity matching eval-time constraint"（Appendix S），但这恰恰说明 sparsity **distribution** artifact（而非 signal type vs coupling）主导了 MMLU 变化，进一步削弱分解的可靠性。

**[AGREE] R2-Q3**: Uniform KL MMLU 40.7 vs TEAL 45.86 是最有力的论据

这是 R2 整份审稿意见中最尖锐的观察。两者都用 uniform allocation、都在 30% sparsity，唯一区别是 mask selection 机制（KL-learned vs magnitude-based）。5pp 的 MMLU gap 直接表明：

1. KL objective 本身选择了对知识编码不利的 neuron pattern
2. 论文的 "allocation contributes"（Section 4.2）叙事在 uniform 条件下不适用——allocation 相同时 gap 仍然存在
3. Mode-covering 假说获得间接支持（KL 优化整体分布质量，可能牺牲稀疏但高价值的知识 neuron），但缺乏直接验证

建议作者在 revision 中专门分析 uniform KL vs uniform TEAL 的 per-layer mask 差异，定位导致 MMLU 退步的具体 layer 和 neuron pattern。

**[AGREE] R2-Q4**: C1 s42 oracle provenance 是合理关切

Appendix P（page 18）承认 oracle masks "reflect one specific training trajectory (optimizer state, data order, Gumbel noise)" 且 "does not rule out trajectory-dependent confounds"。s42/s123/s456 的 consistency（<1.7pp, Table 3）提供部分 robustness 证据，但 3 seeds 仍不足以排除系统性 trajectory bias。这强化了我的 W1（C1 confound control 不足）。

**[AGREE] R2-Q5**: Forward vs Reverse KL 显著性需验证

Table 4 显示 30% 下 forward KL PPL=8.81 vs reverse KL=9.26，差异 0.45。从 KL predictor 的 PPL variance（±0.02 from Table 2）推断可能显著，但：(a) reverse KL 的 variance 未报告，(b) Table 4 未标注 reverse KL 是否为 3-seed，(c) 0.45 的差异虽然绝对值不大但相对于 baseline PPL（~8.81）约 5%，需要正式的 significance test。建议作者提供 t-test p-value 或 bootstrap CI。

---

### Novelty 边界评估回应

**[AGREE with nuance]**: R2 对新颖性边界的判断基本准确，但我补充两点：

1. **MaskLLM 的区分**：R2 正确指出 KL + Gumbel-Sigmoid recipe 与 MaskLLM (Fang et al., 2024) 共享，但关键区别在于 MaskLLM 学习 **static** weight masks（一次性），而本文学习 **dynamic** per-token activation sparsity masks（每 token 不同）。Dynamic setting 中 gradient coupling 的语义与 static setting 根本不同——每个 token 的 mask 都受到当前 hidden state 和所有下游 token 的影响，这不是简单的 "应用到新领域"。

2. **分析框架的价值受限**：R2 将 target-swap ablation 和 per-layer KL 控制列为新颖贡献，我同意这些设计有创意，但如前文所述（我的 N1, R2-Q2），per-layer KL 分解受 train-inference mismatch 严重制约，C1 ablation 有未隔离的 confound（我的 W1）。因此分析框架的实际贡献值低于其设计意图。

**综合判断**：我同意 R2 的 "Findings 足够，Main Conference 偏弱" 定位。核心实用贡献（KL predictor 稳定改进 PPL）可靠，但分析贡献（decomposition）可靠性不足，knowledge regression 未解决，且增量性较强（known techniques in new setting）。我的 Overall 3.5 和 R2 的 3.0 的差距主要在于：我对 ablation 深度（20+ appendix sections）和负面结果的诚实报告给予略多 credit，认为这体现了值得鼓励的实验方法论。但如果分解实验的可靠性问题不修复，3.0-3.5 范围内的任何评分都可以辩护。

---

[Reviewer 1 审稿结果]:
交叉回应已提交。核心判断：

- **R2 的 26 条意见中我同意 23 条**（含 2 条 Must-Fix 全部同意），仅对 M3（ε=0.02 justification）和 Q1（K=4 机制）部分反驳
- **最关键的新发现**：R2-Q3 提出的 uniform KL MMLU 40.7 vs TEAL 45.86 对比——在 allocation 完全相同的条件下，5pp 差距只能归因于 KL objective 本身，直接反驳了论文的 "allocation contributes" 叙事。这促使我将 knowledge regression 从 Should-Fix 升级为 Must-Fix
- **综合评估**：我维持 Overall 3.5（R2 给 3.0），差异在于我对 ablation 深度和诚实报告给予更多 credit，但两份审稿在核心问题上高度一致

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2188 · 2026-05-23T07:47:18.016292+00:00_

Reviewer 1 的完整交叉回应已收到。审稿报告已于此前提交。

**R1 交叉回应与已提交报告的一致性检查**：

R1 同意 R2 的 23/26 条意见，仅对 M3（ε=0.02 有部分 justification）和 Q1（K=4 机制部分可解释）有限度反驳。核心发现：
- R1 将 knowledge regression **从 Should-Fix 升级为 Must-Fix**，与报告中 C3 (Critical) 定级一致
- R1 特别强调 R2-Q3（uniform KL MMLU 40.7 vs TEAL 45.86）为最有力论据，报告中已作为 Question 2 和 C3 分析的核心数据点纳入
- R1 维持 3.5 但认可 3.0–3.5 均可辩护

**结论**：R1 完整交叉回应与已提交报告完全一致，无需修订。报告评分 3.0 (Findings) 反映了两位 Reviewer 的共识区间下限，三个 Critical 问题（K=1 confound、claim 泛化性、knowledge regression 机制）是阻止 Conference 接收的主要因素。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 193

## Round 193

56 recorded events


### User

_source line 2189 · 2026-05-24T02:54:11.493087+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: distill_sparse_swiglu
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2190 · 2026-05-24T02:54:29.911273+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2191 · 2026-05-24T02:54:30.062926+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2192 · 2026-05-24T02:54:38.192208+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2193 · 2026-05-24T02:54:38.192692+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2194 · 2026-05-24T02:54:42.558983+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2195 · 2026-05-24T02:54:42.559469+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2196 · 2026-05-24T02:54:47.277306+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 2197 · 2026-05-24T02:54:48.734365+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (408 个)\n\n- **eval_spon_supp_retry**: DONE (failed) — \n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- qwen14b_kl30_s123_gsm8k_v4: Rerun s123 GSM8K eval (v3 failed: HF network unreachable). Added source /etc/network_turbo + HF_DATASETS_OFFLINE fallback.（准备中）\n- qwen14b_kl30_s123_gsm8k_v3: Rerun s123 GSM8K eval (v2 failed: python not found, conda not activated). Checkpoint on westd-34887.（准备中）\n- qwen14b_kl30_s123_gsm8k_v2: Rerun s123 GSM8K eval to confirm data completeness — original run (qwen14b_kl30_s123_gsm8k) was killed after ~2.5h on unreachable westd-41718, cannot verify sample_len=1319. Checkpoint available on westd-34887.（准备中）\n\n## 近期结论\n- **perlayer_kl_k4_s42** (success): Per-layer KL distillation with K=4 active layers per step and adaptive lambda scheduling can train the sparsity predictor to achieve avg KL < 0.05 while maintaining ~28% sparsity across all 32 layers.\n- **mse30_s123_downstream** (success): MSE-trained predictor at 30% sparsity (seed 123) preserves downstream task performance comparable to dense baseline because MSE distillation captures sufficient activation magnitude information to maintain task-relevant features in the sparse SwiGLU network.\n\n## 趋势\n成功 258 / 负向 24 / 失败 40 / 共 404\narc_challenge_acc_norm: 0.3737 ↓（近 3 次 success）\ngsm8k_e
…[truncated 1797 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1457
}
```

</details>

---


### Tool call

_source line 2198 · 2026-05-24T02:54:48.734751+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 2199 · 2026-05-24T02:54:50.240067+00:00_

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
16	\usepackage{subcaption}
17	
18	\setlength{\textfloatsep}{8pt plus 2pt minus 2pt}
19	\setlength{\floatsep}{8pt plus 2pt minus 2pt}
20	\setlength{\intextsep}{8pt plus 2pt minus 2pt}
21	
22	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\begin{abstract}
30	\input{abstract}
31	\end{abstract}
32	
33	\input{introduction}
34	\input{related_work}
35	\input{method}
36	\input{experiments}
37	\input{conclusion}
38	\input{limitations}
39	% \input{ethics}  % removed per submission guidelines
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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 1505
}
```

</details>

---


### Tool call

_source line 2200 · 2026-05-24T02:54:50.691953+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 2201 · 2026-05-24T02:54:51.043608+00:00_

-rw-r--r-- 1 ubuntu ubuntu 559416 May 24 02:32 /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 2202 · 2026-05-24T02:54:51.043950+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
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

_source line 2203 · 2026-05-24T02:54:51.144634+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2204 · 2026-05-24T02:54:56.591164+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR",
  "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool call

_source line 2205 · 2026-05-24T02:54:57.043001+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2206 · 2026-05-24T02:54:57.494824+00:00_

1	Learned sparsity predictors for SwiGLU LLMs predominantly use binary cross-entropy (BCE), training each neuron independently, yet inference allocates budgets globally via top-$k$ ranking.
2	We train lightweight predictors ($<$1\% of base parameters) with forward KL divergence, coupling all mask decisions through the output distribution.
3	On LLaMA-3.1-8B at 30\% sparsity, the KL predictor reduces perplexity by 14.5\% over TEAL at matched sparsity, with directional commonsense gains ($n{=}3$) but knowledge-intensive regression (MMLU $-$5.2pp on 8B; GSM8K $-$20.1pp on 14B); post-hoc compensation (+67.2M params) becomes redundant.
4	Output-distribution optimization yields masks that diverge 46--68\% from magnitude-based targets; a target-swap ablation suggests these discovered patterns carry most of the quality information: BCE trained on KL-derived targets approaches KL-level PPL (PPL gap $\leq$0.65pp; 3-seed, 30\%).
5	Signal type (output-distribution vs.\ intermediate loss) may account for a substantial portion of the PPL gap at moderate sparsity (30\%) (upper bound; \S\ref{sec:perlayer}).
6	On downstream tasks, cross-layer coupling contributes substantially for commonsense reasoning but minimally for mathematical reasoning (3-seed $K{=}4$-corrected decomposition).
7	Cross-architecture evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms PPL generalization with scale-dependent downstream effects.
8	This is primarily an empirical study; wall-clock speedup requires sparse kernel support not addressed here.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 2207 · 2026-05-24T02:54:57.495220+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2208 · 2026-05-24T02:54:58.699374+00:00_

1	\section{Introduction}
2	
3	How the training objective shapes learned sparsity prediction quality is an open question for SwiGLU LLMs~\cite{shazeer2020glu}. SwiGLU FFN blocks exhibit high contextual sparsity, but their gated activation makes importance prediction challenging: neuron importance depends on both gate and up-projection values, a target that magnitude-based methods handle suboptimally.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they predominantly rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: the TEAL (training-free activation sparsity;~\citealp{liu2025teal}) top-$k$ mechanism ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	Unlike MaskLLM~\cite{fang2024maskllm}, which applies KL to static N:M weight masks, we address contextual activation sparsity where masks must generalize to unseen inputs, vary per token, and coordinate across layers through global allocation.
8	
9	Gradient analysis reveals a structural asymmetry: BCE's gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$ depends only on neuron $j$, while under KL divergence, the gradient couples each neuron to all others through the downstream Jacobian (\S\ref{sec:method:gradient}).
10	KL's coupled gradients discover neuron importance patterns that diverge 68\% from magnitude-based masks (mean per-layer Jaccard distance).
11	A target-swap ablation shows KL-discovered mask targets carry most of the quality information: BCE retrained on KL-derived targets approaches KL PPL ($\leq$0.65pp gap, 3-seed), while magnitude-trained BCE yields 28.13$\pm$0.20. Coupling contributes marginally to 
…[truncated 3012 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 1204
}
```

</details>

---


### Tool call

_source line 2209 · 2026-05-24T02:54:58.800080+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2210 · 2026-05-24T02:54:59.001303+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present an output-distribution KL framework for training contextual sparsity predictors in SwiGLU-based language models (Figure~\ref{fig:overview}).
5	The method replaces per-neuron binary classification (BCE) with an output-distribution alignment objective that couples all pruning decisions through the model's forward pass and achieves competitive performance without auxiliary error compensation networks at inference.
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
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{x}^{(\ell)}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces p
…[truncated 9831 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 2211 · 2026-05-24T02:54:59.001691+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2212 · 2026-05-24T02:54:59.504091+00:00_

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
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4 on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB), using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $1 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), GSM8K (8-shot), HellaSwag (10-shot), and PIQA (0-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly\footnote{TEAL is deterministic; single-run evaluation suffices. KL/BCE predictors require multi-seed evaluation due to random initialization.}; (2) \textbf{BCE predictor} (Deja
…[truncated 17382 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2213 · 2026-05-24T02:54:59.504655+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2214 · 2026-05-24T02:55:00.006890+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} and GRASP~\cite{shin2025grasp} predict activation sparsity patterns without additional training.
6	LaRoSA~\cite{huang2025larosa} applies layerwise orthogonal rotations for structured activation sparsity with wall-clock speedup on SiLU models.
7	Wang et al.~\cite{wang2025dynamicsparse}, AWQ~\cite{lin2024awq}, and Outlier Suppression+~\cite{wei2023outlier} address sparsity--quantization interactions and activation-aware quantization.
8	Dhar et al.~\cite{dhar2024activation} characterize activation sparsity opportunities across architectures, showing that SwiGLU models exhibit lower natural sparsity than ReLU counterparts.
9	OWL~\cite{yin2024owl} determines per-layer sparsity ratios from outlier distributions for weight pruning.
10	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
11	
12	\paragraph{Predictor-Based Contextual Sparsity.}
13	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
14	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
15	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
16	SVD-CSP~\cite{serbin2026svdcsp} compre
…[truncated 5026 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2215 · 2026-05-24T02:55:00.057546+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2216 · 2026-05-24T02:55:00.057864+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	At moderate sparsity (30\%), output-distribution alignment is the primary design dimension: signal type may account for most of the PPL gap (upper bound; Appendices~\ref{app:k4_downstream},~\ref{app:constraint}).
5	A $<$1\% predictor reduces TEAL's PPL by 14.5\% via divergent masks; directional downstream gains but knowledge regression persist across scales.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2217 · 2026-05-24T02:55:00.559677+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 2218 · 2026-05-24T02:55:01.362876+00:00_

1	\section*{Limitations}
2	
3	Our findings are bounded by three limitations.
4	\textbf{Sparsity sweet spot.} 30\% is the lowest-degradation level; at 50\%, all methods collapse to near-random on reasoning tasks, and a separate predictor must be retrained per target.
5	\textbf{Knowledge-intensive regression.} KL consistently underperforms on MMLU and GSM8K across scales (8B: $-$5.2pp MMLU; 14B: $-$20pp GSM8K), suggesting output-distribution objectives systematically sacrifice reasoning-critical pathways.
6	\textbf{Evaluation scope.} All predictors train on WikiText-103; C4 evaluation shows preserved KL advantage but $31\times$ higher cross-seed variance. Open-ended generation (e.g., MT-Bench) and contexts beyond 2048 tokens remain untested.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 2219 · 2026-05-24T02:55:01.363285+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 2220 · 2026-05-24T02:55:01.715176+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB; batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
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
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); output-distribution KL thus provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% o
…[truncated 41611 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 2221 · 2026-05-24T02:55:01.715556+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 2222 · 2026-05-24T02:55:02.368341+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on the search results, here are the key submission guidelines for EMNLP 2026 regarding ARR:

## EMNLP 2026 Call for Papers Overview

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

## ARR Policy

For the ARR 2026 May cycle aligned with EMNLP, authors must explicitly declare which conference they intend to commit to at submission time, and this choice is binding for EMNLP 2026—ARR 2026 May submissions that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026.

## General Requirements

Following the ACL and ARR policies, there is no anonymity period requirement.

All accepted papers must be presented at the conference to app
…[truncated 364 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 5777
}
```

</details>

---


### Tool result

_source line 2223 · 2026-05-24T02:55:03.321928+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (408 个)\n\n- **eval_spon_supp_retry**: DONE (failed) — \n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- qwen14b_kl30_s123_gsm8k_v4: Rerun s123 GSM8K eval (v3 failed: HF network unreachable). Added source /etc/network_turbo + HF_DATASETS_OFFLINE fallback.（准备中）\n- qwen14b_kl30_s123_gsm8k_v3: Rerun s123 GSM8K eval (v2 failed: python not found, conda not activated). Checkpoint on westd-34887.（准备中）\n- qwen14b_kl30_s123_gsm8k_v2: Rerun s123 GSM8K eval to confirm data completeness — original run (qwen14b_kl30_s123_gsm8k) was killed after ~2.5h on unreachable westd-41718, cannot verify sample_len=1319. Checkpoint available on westd-34887.（准备中）\n\n## 近期结论\n- **perlayer_kl_k4_s42** (success): Per-layer KL distillation with K=4 active layers per step and adaptive lambda scheduling can train the sparsity predictor to achieve avg KL < 0.05 while maintaining ~28% sparsity across all 32 layers.\n- **mse30_s123_downstream** (success): MSE-trained predictor at 30% sparsity (seed 123) preserves downstream task performance comparable to dense baseline because MSE distillation captures sufficient activation magnitude information to maintain task-relevant features in the sparse SwiGLU network.\n\n## 趋势\n成功 258 / 负向 24 / 失败 40 / 共 404\narc_challenge_acc_norm: 0.3737 ↓（近 3 次 success）\ngsm8k_e
…[truncated 1797 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1606
}
```

</details>

---


### Tool call

_source line 2224 · 2026-05-24T02:55:20.696269+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 2225 · 2026-05-24T02:55:21.148517+00:00_

1	% =============================================================================
2	% Additional references (R20 review response)
3	% =============================================================================
4	
5	@article{huang2025larosa,
6	  title={La{R}o{SA}: Accelerating Large Language Model Inference with Layerwise Rotated Sparse Activation},
7	  author={Huang, Fangcheng and others},
8	  journal={arXiv preprint arXiv:2507.01299},
9	  year={2025}
10	}
11	
12	@inproceedings{geva2023dissecting,
13	  title = {Dissecting Recall of Factual Associations in Auto-Regressive Language Models},
14	  author = {Geva, Mor and Bastings, Jasmijn and Filippova, Katja and Globerson, Amir},
15	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
16	  pages = {12216--12235},
17	  year = {2023},
18	}
19	
20	@article{fu2024lazyllm,
21	  title = {{LazyLLM}: Dynamic Token Pruning for Efficient Long Context {LLM} Inference},
22	  author = {Qichen Fu and Minsik Cho and Thomas Merth and Sachin Mehta and Mohammad Rastegari and Mahyar Najibi},
23	  year = {2024},
24	  journal = {arXiv preprint arXiv:2407.14057},
25	}
26	
27	@article{zhang2025cots,
28	  title = {{COTS}: Connected Sparse Activation for Efficient {LLM} Inference},
29	  author = {Yilong Zhang and Junyuan Shang and Huanqi Cao and Shiyao Li and Shuguang Jiang and Lingxiao Ma and Shun Zheng and Cheng Li and Jiang Bian},
30	  year = {2025},
31	  journal = {arXiv preprint arXiv:2502.14475},
32	}
33	
34	@inproceedings{alizadeh2024llmflash,
35	  title = {{LLM} in a Flash: Efficient Large Language Model Inference with Limited Memory},
36	  author = {Keivan Alizadeh and Iman Mirzadeh and Dmitry Belenko and Karen Khatamifard and Minsik Cho and Carlo C Del Mundo and Mohammad Rastegari and Mehrdad Farajtabar},
37	  year = {2024},
38	  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
39	}
40	
41	@article{wei2023outlier,
4
…[truncated 24334 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2226 · 2026-05-24T02:55:21.148873+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 2227 · 2026-05-24T02:55:23.102133+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (1). The file has 1 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 1953
}
```

</details>

---


### Tool call

_source line 2228 · 2026-05-24T02:55:23.102635+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper && pdfinfo ../artifacts/review_round_25/submitted.pdf 2>/dev/null | grep Pages || echo \"NO_PDFINFO\"",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper && pdfinfo ../artifacts/review_round_25/submitted.pdf 2>/dev/null | grep Pages || echo \"NO_PDFINFO\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 2229 · 2026-05-24T02:55:23.905815+00:00_

Pages:           19
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_director_e331551e

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 2230 · 2026-05-24T02:55:24.056837+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
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

_source line 2231 · 2026-05-24T02:55:24.157553+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2232 · 2026-05-24T02:55:33.241204+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 2233 · 2026-05-24T02:55:34.195598+00:00_

issues:
  # ============================================================
  # Round 27 — Active issues
  # ============================================================

  - id: "R20-W1"
    summary: "Per-layer KL decomposition 的 train-inference mismatch confound 未解决"
    category: method
    severity: critical
    status: in_progress
    first_raised_round: 20
    last_seen_round: 27
    mentions:
      - {round: 21, reviewers: [1, 2], note: "R21 Critical。K=4 single-seed。"}
      - {round: 22, reviewers: [1, 2], note: "R22 N2。97.5% 精确数字不可靠。"}
      - {round: 24, reviewers: [1, 2], note: "R24 C1。K=1 有 32× train-inference mismatch。"}
      - {round: 25, reviewers: [1, 2], note: "R25 N1/N2。"}
      - {round: 26, reviewers: [1, 2], note: "R26 R1-N2/R2-N1。建议 stop-gradient 或更多 K 值。"}
      - {round: 27, reviewers: [1, 2], note: "R27 C1。K-curve 6 点中除 K=4 外均 single-seed。K=16 PPL 优势可能 seed-specific。per-layer update count confound 未解决。"}
    action_items:
      - {round: 21, action: "K=4 3-seed", assigned_to: "main_agent", status: done}
      - {round: 22, action: "定性 'majority of PPL gap'", assigned_to: "paper_agent", status: done}
      - {round: 25, action: "限定 decomposition 为 moderate sparsity", assigned_to: "paper_agent", status: done}
      - {round: 25, action: "K=2/K=8/K=16 实验扩展 K-curve", assigned_to: "main_agent", status: done}
      - {round: 27, action: "§4.5 降级为 Exploratory Decomposition + may account for a substantial portion", assigned_to: "paper_agent", status: done}
      - {round: 27, action: "experiments L161 'primary design lever' → 'major factor for PPL'", assigned_to: "paper_agent", status: done}
      - {round: 27, action: "appendix L647 加 'for PPL at this sparsity level (preliminary)'", assigned_to: "paper_agent", status: done}
      - {round: 27, action: "K=2/8/16 各补 s123/s456 3-seed", assigned_to: "main_agent", status: in_progress}
    resolution: ""
    resolution_round: null

  - id: "R20-N2"
    summary: "MMLU/GSM8K 跨架构系统性退步缺乏机制分析"
    category: exp
…[truncated 12190 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 2234 · 2026-05-24T02:55:34.246367+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/agent/project_config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review configuration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/agent/project_config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review configuration"
  }
}
```

</details>

---


### Tool result

_source line 2235 · 2026-05-24T02:55:35.149889+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 2236 · 2026-05-24T02:55:35.251211+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/submitted.pdf",
  "pages": "1-9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/submitted.pdf",
    "pages": "1-9"
  }
}
```

</details>

---


### Tool result

_source line 2237 · 2026-05-24T02:55:35.856384+00:00_

PDF pages extracted: 9 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/submitted.pdf (546.3KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 605
}
```

</details>

---


### Tool call

_source line 2238 · 2026-05-24T02:56:24.593711+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
  }
}
```

</details>

---


### Tool result

_source line 2239 · 2026-05-24T02:56:55.263625+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 30669
}
```

</details>

---


### Tool call

_source line 2240 · 2026-05-24T02:56:55.314283+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "distill_sparse_swiglu",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **类别**: Long Paper（正文 8 页限制，References 不限，Limitations 不计入页数）\n- **模板**: ACL review format（double-blind）\n- **Deadline**: 2026-05-25\n- **Overall Assessment 评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/submitted.pdf`\n\n## 论文概述\n本文研究 SwiGLU LLM 中上下文稀疏性预测器的训练目标选择。核心方法：用 forward KL divergence（输出分布对齐）替代传统 BCE（逐神经元分类），训练轻量级预测器（<1% 参数），通过 Gumbel-Sigmoid 松弛实现可微 mask 采样。在 LLaMA-3.1-8B 上 30% 稀疏度下，KL 预测器 PPL 比 TEAL 低 14.5%，但 MMLU/GSM8K 下降。target-swap ablation（C1）显示 KL 发现的 mask 模式可迁移到 BCE。per-layer KL 分解尝试分离 signal type 和 coupling scope 的贡献。\n\n## 你的审查侧重\n\n### 1. KL 训练框架有效性\n- Forward KL vs Reverse KL vs JSD 的实验对比是否充分？30% 和 50% 两个点是否足够支撑结论？\n- Gumbel-Sigmoid 松弛的必要性论证（vs STE）是否 convincing？\n- Geometric penalty schedule 的设计是否合理？deadzone margin ε=0.02 是否有 sensitivity analysis？\n\n### 2. Ablation 设计严谨性\n- **C1 target-swap ablation**: oracle mask 的二值化（soft logit → hard mask）是否引入了无法忽略的 confound？BCE+Gumbel vs BCE 的差异（32.22 vs 27.97）如何解释？\n- **Per-layer KL 分解**: K=1 的 train-inference mismatch（1/32 vs 32/32 layers masked）是否使 \"signal type accounts for most of PPL gap\" 的声明站不住脚？K-curve 中 K=2/8/16 是否有 3-seed 数据？\n- 50% sparsity 下 per-layer KL (K=4: 44.23) 比 K=1 (34.85) 更差——这是否说明 decomposition 方法在高稀疏度下不可信？\n\n### 3. 统计可靠性\n- 3-seed 是否足够？95% CI 宽度是多少？downstream metrics 的 CI 是否 overlap？\n- Global allocation 下 MMLU σ=9.5pp（n=3），这个方差下任何 downstream comparison 是否有意义？\n- Qwen-14B GSM8K std=5.2pp，结论是否过度声称？\n\n### 4. 实验完整性\n- 为什么只评估 WikiText-2 PPL？C4 OOD 评估覆盖是否充分（30% 仅 2-seed）？\n- MSE 50% baseline 仅 s42 有效（s123 catastrophic PPL=15,789）——这是否削弱了 MSE 作为 baseline 的可信度？\n- BCE isocompute (2700 steps) 仅在 50% 下有 3-seed——30% 下是否缺失？\n\n### 5. 可复现性\n- 训练细节是否充分（lr schedule, warmup, gradient clipping）？\n- 代码/checkpoint 是否承诺开源？\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（含评分和置信度）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "distill_sparse_swiglu",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **类别**: Long Paper（正文 8 页限制，References 不限，Limitations 不计入页数）\n- **模板**: ACL review format（double-blind）\n- **Deadline**: 2026-05-25\n- **Overall Assessment 评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/submitted.pdf`\n\n## 论文概述\n本文研究 SwiGLU LLM 中上下文稀疏性预测器的训练目标选择。核心方法：用 forward KL divergence（输出分布对齐）替代传统 BCE（逐神经元分类），训练轻量级预测器（<1% 参数），通过 Gumbel-Sigmoid 松弛实现可微 mask 采样。在 LLaMA-3.1-8B 上 30% 稀疏度下，KL 预测器 PPL 比 TEAL 低 14.5%，但 MMLU/GSM8K 下降。target-swap ablation（C1）显示 KL 发现的 mask 模式可迁移到 BCE。per-layer KL 分解尝试分离 signal type 和 coupling scope 的贡献。\n\n## 你的审查侧重\n\n### 1. KL 训练框架有效性\n- Forward KL vs Reverse KL vs JSD 的实验对比是否充分？30% 和 50% 两个点是否足够支撑结论？\n- Gumbel-Sigmoid 松弛的必要性论证（vs STE）是否 convincing？\n- Geometric penalty schedule 的设计是否合理？deadzone margin ε=0.02 是否有 sensitivity analysis？\n\n### 2. Ablation 设计严谨性\n- **C1 target-swap ablation**: oracle mask 的二值化（soft logit → hard mask）是否引入了无法忽略的 confound？BCE+Gumbel vs BCE 的差异（32.22 vs 27.97）如何解释？\n- **Per-layer KL 分解**: K=1 的 train-inference mismatch（1/32 vs 32/32 layers masked）是否使 \"signal type accounts for most of PPL gap\" 的声明站不住脚？K-curve 中 K=2/8/16 是否有 3-seed 数据？\n- 50% sparsity 下 per-layer KL (K=4: 44.23) 比 K=1 (34.85) 更差——这是否说明 decomposition 方法在高稀疏度下不可信？\n\n### 3. 统计可靠性\n- 3-seed 是否足够？95% CI 宽度是多少？downstream metrics 的 CI 是否 overlap？\n- Global allocation 下 MMLU σ=9.5pp（n=3），这个方差下任何 downstream comparison 是否有意义？\n- Qwen-14B GSM8K std=5.2pp，结论是否过度声称？\n\n### 4. 实验完整性\n- 为什么只评估 WikiText-2 PPL？C4 OOD 评估覆盖是否充分（30% 仅 2-seed）？\n- MSE 50% baseline 仅 s42 有效（s123 catastrophic PPL=15,789）——这是否削弱了 MSE 作为 baseline 的可信度？\n- BCE isocompute (2700 steps) 仅在 50% 下有 3-seed——30% 下是否缺失？\n\n### 5. 可复现性\n- 训练细节是否充分（lr schedule, warmup, gradient clipping）？\n- 代码/checkpoint 是否承诺开源？\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（含评分和置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 2241 · 2026-05-24T02:57:25.026475+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 29712
}
```

</details>

---


### Tool call

_source line 2242 · 2026-05-24T02:57:25.077298+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "distill_sparse_swiglu",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **类别**: Long Paper（正文 8 页限制，References 不限，Limitations 不计入页数）\n- **模板**: ACL review format（double-blind）\n- **Deadline**: 2026-05-25\n- **Overall Assessment 评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/submitted.pdf`\n\n## 论文概述\n本文是一项实证研究，系统对比了 SwiGLU LLM 上下文稀疏性预测器的不同训练目标（KL/BCE/MSE/JSD/Reverse KL）。核心发现：output-distribution KL 在 PPL 上显著优于 per-neuron BCE 和 per-layer MSE；KL 发现的 mask 模式与 magnitude-based 目标有 46-68% 的 Jaccard distance 偏离；target-swap ablation 显示这些模式可迁移。跨架构（Mistral-7B, Qwen-2.5-14B）验证了 PPL 优势。但知识密集型任务（MMLU, GSM8K）出现系统性退步。\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- 核心组件（KL distillation, Gumbel-Sigmoid, lightweight predictor）均为已有技术。MaskLLM 已将 frozen weights + learnable masks + KL 用于稀疏性。本文的 novelty 边界在哪里？\"组合新颖性 + 系统性实证分析\" 是否满足 EMNLP 的 novelty bar？\n- Table 1 taxonomy 是否有真正的分析价值，还是仅仅是 organizational？空格子是否暗示了未验证的假设？\n- \"empirical study\" 的定位是否 consistent？contribution list 中有 4 条，前 2 条标 Empirical，后 2 条标 Practical——Practical 贡献是否足够 substantial？\n\n### 2. 相关工作完整性\n- 是否遗漏了重要的相关工作？特别是：\n  - 2025-2026 年发表的 activation sparsity 新工作\n  - KL distillation 用于结构化/非结构化稀疏性的其他工作\n  - Hardware-aware sparsity（如 Triton block-sparse 实现）\n- MaskLLM 的区分是否充分？论文列了 3 点区别（static vs contextual, no cross-layer, input-independent），但是否有实验证据支持这些区别的重要性？\n\n### 3. 写作质量与叙事一致性\n- Abstract 信息密度是否过高？是否在 200 words 以内？\n- \"primarily an empirical study\" 但 §3 有 7 个 subsection 的方法描述——这是否造成读者预期错位？\n- Conclusion 仅 2 句话是否过于简略？是否遗漏了 broader impact 或 future work？\n- Introduction 中数字过多（14.5%, 46-68%, 0.65pp, 28.13±0.20, 68%, 33.8%）是否影响可读性？\n- 术语一致性：是否全文统一使用 \"output-distribution KL\"？\n\n### 4. 格式合规性（EMNLP 2026 / ACL template）\n- 正文是否恰好 8 页？Limitations 是否在正文而非 appendix？\n- 匿名性：是否有 deanonymization 风险（代码链接、GPU 型号、specific experimental details）？\n- 引用格式是否符合 ACL natbib 要求？`\\citealp` vs `\\cite` 使用是否正确？\n- Appendix 是否过长（可能超出审稿人耐心）？有多少个 appendix section？\n\n### 5. Limitations 覆盖度\n- 3 个限制是否充分？是否遗漏了：\n  - 仅 SwiGLU 架构（不适用于 ReLU/GeLU）\n  - 训练数据量极小（1000 steps, WikiText-103）\n  - 无实际部署验证\n  - Predictor 增加 6.4% latency 但无 wall-clock 加速\n\n### 6. 知识退步的 framing\n- MMLU -5.2pp（8B）和 GSM8K -20.1pp（14B）是否被充分 acknowledged？\n- \"directional commonsense gains\" 的措辞是否 understate 了 knowledge regression 的严重性？\n- 在 downstream 全面退步的情况下，PPL improvement 作为主要贡献是否足够有说服力？\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（含评分和置信度）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "distill_sparse_swiglu",
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **类别**: Long Paper（正文 8 页限制，References 不限，Limitations 不计入页数）\n- **模板**: ACL review format（double-blind）\n- **Deadline**: 2026-05-25\n- **Overall Assessment 评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/submitted.pdf`\n\n## 论文概述\n本文是一项实证研究，系统对比了 SwiGLU LLM 上下文稀疏性预测器的不同训练目标（KL/BCE/MSE/JSD/Reverse KL）。核心发现：output-distribution KL 在 PPL 上显著优于 per-neuron BCE 和 per-layer MSE；KL 发现的 mask 模式与 magnitude-based 目标有 46-68% 的 Jaccard distance 偏离；target-swap ablation 显示这些模式可迁移。跨架构（Mistral-7B, Qwen-2.5-14B）验证了 PPL 优势。但知识密集型任务（MMLU, GSM8K）出现系统性退步。\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- 核心组件（KL distillation, Gumbel-Sigmoid, lightweight predictor）均为已有技术。MaskLLM 已将 frozen weights + learnable masks + KL 用于稀疏性。本文的 novelty 边界在哪里？\"组合新颖性 + 系统性实证分析\" 是否满足 EMNLP 的 novelty bar？\n- Table 1 taxonomy 是否有真正的分析价值，还是仅仅是 organizational？空格子是否暗示了未验证的假设？\n- \"empirical study\" 的定位是否 consistent？contribution list 中有 4 条，前 2 条标 Empirical，后 2 条标 Practical——Practical 贡献是否足够 substantial？\n\n### 2. 相关工作完整性\n- 是否遗漏了重要的相关工作？特别是：\n  - 2025-2026 年发表的 activation sparsity 新工作\n  - KL distillation 用于结构化/非结构化稀疏性的其他工作\n  - Hardware-aware sparsity（如 Triton block-sparse 实现）\n- MaskLLM 的区分是否充分？论文列了 3 点区别（static vs contextual, no cross-layer, input-independent），但是否有实验证据支持这些区别的重要性？\n\n### 3. 写作质量与叙事一致性\n- Abstract 信息密度是否过高？是否在 200 words 以内？\n- \"primarily an empirical study\" 但 §3 有 7 个 subsection 的方法描述——这是否造成读者预期错位？\n- Conclusion 仅 2 句话是否过于简略？是否遗漏了 broader impact 或 future work？\n- Introduction 中数字过多（14.5%, 46-68%, 0.65pp, 28.13±0.20, 68%, 33.8%）是否影响可读性？\n- 术语一致性：是否全文统一使用 \"output-distribution KL\"？\n\n### 4. 格式合规性（EMNLP 2026 / ACL template）\n- 正文是否恰好 8 页？Limitations 是否在正文而非 appendix？\n- 匿名性：是否有 deanonymization 风险（代码链接、GPU 型号、specific experimental details）？\n- 引用格式是否符合 ACL natbib 要求？`\\citealp` vs `\\cite` 使用是否正确？\n- Appendix 是否过长（可能超出审稿人耐心）？有多少个 appendix section？\n\n### 5. Limitations 覆盖度\n- 3 个限制是否充分？是否遗漏了：\n  - 仅 SwiGLU 架构（不适用于 ReLU/GeLU）\n  - 训练数据量极小（1000 steps, WikiText-103）\n  - 无实际部署验证\n  - Predictor 增加 6.4% latency 但无 wall-clock 加速\n\n### 6. 知识退步的 framing\n- MMLU -5.2pp（8B）和 GSM8K -20.1pp（14B）是否被充分 acknowledged？\n- \"directional commonsense gains\" 的措辞是否 understate 了 knowledge regression 的严重性？\n- 在 downstream 全面退步的情况下，PPL improvement 作为主要贡献是否足够有说服力？\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（含评分和置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 2243 · 2026-05-24T02:57:26.450207+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1372
}
```

</details>

---


### Assistant

_source line 2244 · 2026-05-24T02:57:37.748669+00:00_

Round 1 审稿已启动：

- **视觉审查 Agent**：已派发（fire-and-forget，不阻塞）
- **Reviewer 1**（方法严谨性 + 实验设计）：已分配
- **Reviewer 2**（新颖性 + 完整性 + 写作质量）：已分配

等待两位 Reviewer 提交独立初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 194

## Round 194

2 recorded events


### User

_source line 2245 · 2026-05-24T03:04:25.840186+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见（方法严谨性 + 实验设计）

---

## Summary

本文研究 SwiGLU LLM 中上下文稀疏性预测器的训练目标选择。核心提议是用 forward KL divergence（基于输出分布对齐）替代传统 BCE（逐神经元分类），通过 Gumbel-Sigmoid 松弛实现可微 mask 采样，训练轻量级预测器（<1% 参数）。在 LLaMA-3.1-8B 上，30% 稀疏度下 KL 预测器 PPL 比 TEAL 低 14.5%（8.81 vs 10.30），但 MMLU/GSM8K 出现系统性回退。论文通过 C1 target-swap ablation 表明 KL 发现的 mask 模式可迁移到 BCE，并尝试用 per-layer KL 分解来分离 signal type 和 coupling scope 的贡献。跨架构验证（Mistral-7B, Qwen-14B）确认 PPL 优势可泛化。

---

## 总体评分

**Overall**: 3.0 — Findings

**一句话总结**: PPL 改善显著但下游知识任务系统性回退、per-layer 分解方法学局限、以及 n=3 下统计功效不足，使本文更适合 Findings 而非主会议。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 核心方法合理且有充分实验支撑；但 per-layer KL 分解存在根本性 train-inference mismatch，下游 metric 统计功效不足 |
| Excitement | 3/5 | 输出分布对齐训练稀疏预测器是有趣的方向；但方法本身是 KL 蒸馏 + Gumbel-Sigmoid 的组合，新颖性有限；下游回退限制实用价值 |
| Reproducibility | 4/5 | 训练细节充分（lr, schedule, GPU, steps），承诺开源代码和 checkpoint；多 seed 实验增加可信度 |
| Confidence | 4/5 | 对稀疏性/效率文献熟悉，仔细核查了实验设置和数值 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Per-layer KL 分解的 train-inference mismatch 使核心 decomposition claim 站不住脚

- 具体位置：§4.5 (Per-Layer KL), Table 4, Figure 2
- 问题：K=1 per-layer KL 训练时每步只 mask 1/32 层，但推理时 32 层同时被 mask。这意味着训练阶段每个预测器几乎在 dense 条件下学习（31/32 层保持完整），而推理时面临全面的跨层交互——这是根本性的 train-inference mismatch。论文基于 K=1 (PPL 9.05) vs E2E (8.81) 只有 2.7% 的 gap 来声称 "signal type accounts for a substantial portion of the PPL gap"（abstract 第5句、§4.5），但这个小 gap 恰恰是因为 K=1 条件下任务极其简单（近似 dense evaluation）。
- 关键证据：
  - 50% 稀疏度下 K=1 PPL=34.85 vs E2E PPL=11.84（2.94×），说明 mismatch 在高稀疏度下灾难性放大
  - K=4 在 50% 时更差（44.23），论文自己承认 "the decomposition is interpretable only at 30%"（§4.5 最后一句）
  - K-curve 非单调（Figure 2, K=2 最差 10.75），说明层间交互存在复杂非线性效应，简单的 K 扫描无法干净地分离 signal type 和 coupling scope
- 为什么影响接收：这个 decomposition 是论文的核心分析贡献（区别于纯 "KL > BCE" 的实验比较）。如果 decomposition 方法学上有缺陷，论文就退化为一个 "KL 训练在 PPL 上更好但下游更差" 的实验报告，贡献不足以支撑主会议。
- 建议修改方向：(1) 明确将 K=1 结果标注为 "upper bound only"，避免 abstract/conclusion 中使用 "accounts for a substantial portion" 这类暗示因果关系的措辞；(2) 报告 K=4 在 30% 的 downstream metrics 的完整 CI（当前只在 Appendix S 部分提供）；(3) 讨论为什么 decomposition 在 50% 失效——是否说明 signal type 和 coupling scope 本质上不可分？

**N2** [critical] 下游知识任务系统性回退缺乏机制性解释

- 具体位置：Table 2, §4.2 (Task-Type Split, Knowledge-Task Regression), §4.6 (Cross-Architecture)
- 问题：KL 在所有评估的模型/规模上系统性地损害 MMLU 和 GSM8K：
  - LLaMA-8B 30%: MMLU 40.7±1.3 vs TEAL 45.86 (−5.2pp)
  - Qwen-14B 30%: GSM8K 32.0±5.2 vs 52.1 (−20.1pp)
  - Mistral-7B: MMLU/GSM8K 也下降
  论文提出了两个假设：(a) 训练数据偏差（WikiText-103 数学内容少）；(b) forward KL 的 mode-covering 稀释了编码事实知识的稀有激活。但 C4 控制实验排除了 (a)，而 (b) 只是猜测，没有直接验证（如分析 KL mask 是否确实 prune 了 factual neurons）。
- 为什么影响接收：对于一个声称改进稀疏预测质量的方法论文，在核心下游任务上系统性退步是根本性矛盾。如果方法只优化 PPL 而牺牲下游能力，实用价值大打折扣。审稿人会质疑：PPL 改善在多大程度上反映了真正的模型质量提升？
- 建议修改方向：(1) 分析 KL 和 magnitude-based mask 在 "factual neurons"（如 Geva et al. 2023 识别的 knowledge neurons）上的保留率差异，提供 (b) 假设的直接证据；(2) 讨论是否可以通过 hybrid loss（KL + factual neuron protection）缓解回退；(3) 或者明确重新框定贡献为 "PPL-optimal but not task-universal"，调低 claim。

**N3** [critical] 下游 metric 统计功效严重不足，多数比较不具统计意义

- 具体位置：Table 2, §4.2, §4.6
- 问题：
  - KL global 30% MMLU: 35.7±9.5pp (n=3)。95% CI ≈ 35.7 ± 2.48×9.5/√3 ≈ 35.7 ± 13.6pp → [22.1, 49.3]。这个区间覆盖了 dense model (65.27) 到 random chance (25%) 之间的大部分范围，任何基于此的比较完全没有统计意义。
  - Qwen-14B GSM8K: 32.0±5.2pp (n=3)。95% CI ≈ ±7.4pp。论文 abstract 报告 "−20.1pp" 但真实 gap 可能在 [12.7, 27.5]pp 之间。
  - 即使 uniform allocation 的 MMLU (40.7±1.3) 看起来更稳定，与 TEAL (45.86, 单次) 的比较也缺乏 TEAL 的方差信息。
  - 论文在 §4.2 承认 "95% confidence intervals for individual downstream tasks overlap"，但仍在 abstract 和 conclusion 中报告具体的 downstream gap 数值作为结论。
- 为什么影响接收：n=3 对于 variance 如此大的 downstream metric 是不够的。论文的多个核心 claim 建立在统计不显著的差异上。
- 建议修改方向：(1) 增加 seed 数到至少 5 个；(2) 对 TEAL baseline 也跑多次初始化确认其方差；(3) 所有 downstream 比较都报告 CI 并标注是否 overlap；(4) 对于 CI overlap 的比较，修改 claim 为 "directional" 而非 definitive。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] C1 target-swap ablation 的 confound 未充分控制

- 具体位置：Table 3, §4.4, Appendix P
- 问题：C1 ablation 将 KL predictor 的 soft logits binarize（>0 → 1）为 hard oracle mask 供 BCE 训练。这个 binarization 步骤丢弃了 ranking 信息（论文在 §4.4 末尾确实承认了这一点）。更重要的是：
  - s42 的 oracle 来自 "earlier training run (not seed-matched)"（Table 3 footnote），s123/s456 才是 seed-matched。这意味着 s42 的 C1 gap (0.65pp) 和 s123/s456 的 gap (≤0.03pp) 之间的差异可能部分来自 oracle provenance 不同。
  - BCE+Gumbel (32.22) vs BCE (27.97) 在 Table 4 显示 Gumbel 本身对 BCE 是有害的 (+4.25pp)。这意味着 C1 对照的是 "BCE without Gumbel on KL targets" vs "KL with Gumbel"，两者的训练 mechanism 完全不同，无法干净地分离 target quality 和 training mechanism。
- 建议：(1) 所有 seed 统一使用 seed-matched oracle，消除 provenance confound；(2) 增加 "BCE+Gumbel on KL targets" 条件作为更公平的 C1 对照。

**W2** [warning] MSE baseline 在 50% 下几乎不可信

- 具体位置：Table 4 footnote §, Appendix G
- 问题：MSE 50% 仅 s42 有效（229.26），s123 catastrophic (PPL=15,789)。论文标注了这一点，但仍在 Table 4 中报告 MSE 50% 的单 seed 数据作为 baseline。2/3 的 seed 失败说明 MSE 在 50% 下不是一个稳定的 baseline，将其列在 comparison 中有误导性。
- 建议：将 MSE 50% 从主 Table 移至 Appendix 并标注为 "unstable baseline"；或仅在 30% 使用 MSE 对比。

**W3** [warning] 30% 下缺少 BCE isocompute 对比

- 具体位置：Table 2, §4.3
- 问题：BCE isocompute (2700 steps) 仅在 50% 下有 3-seed 数据（28.13±0.20）。30% 下 BCE 的 1000-step 结果 (BCE uniform 15.09±0.13) 和 BCE global (11.25, single seed) 都远弱于 KL，但没有 2700-step BCE 在 30% 的数据。如果 BCE 在 30% 的更多训练步数下也能大幅改善，KL 的优势会缩小。
- 建议：补充 30% 下 BCE 2700-step 的 3-seed 结果。

**W4** [warning] ε=0.02 deadzone margin 缺乏 sensitivity analysis

- 具体位置：§3.5 (Eq. 7), Appendix C
- 问题：方法文本称 "sensitivity in Appendix C"，但 Appendix C 只展示了收敛动态（Figure 4, Table 9），没有 ε={0.01, 0.02, 0.05} 的 PPL 比较。ε 直接影响 sparsity 控制精度和训练稳定性，应该提供消融。
- 建议：补充 ε 的 2-3 个值的 PPL 消融。

**W5** [warning] 主评估指标单一（仅 WikiText-2 PPL）

- 具体位置：§4.1, Appendix D
- 问题：所有主要比较基于 WikiText-2 perplexity。C4 OOD 评估仅在 Appendix D，且 30% 下只有 seed 42 的数据（Table 10 注释："30% KL reports 2-seed mean±std; other entries use seed 42"）。对于声称 "KL 改善 PPL" 的论文，多数据集 PPL 评估是必要的。
- 建议：将 C4 PPL 提升到主 table 或至少确保 3-seed 覆盖。

---

## 小问题（不影响接收）

- Table 2 中 TEAL 是 deterministic single-run（footnote 1），但 KL/BCE 是 3-seed。直接比较 TEAL 点估计和 KL 的 CI 在方法论上不对等——TEAL 的数值没有不确定性估计。
- Figure 3 (PPL scaling with sparsity) 只展示了 global allocation 的曲线，但主 Table 显示 uniform allocation 在 ≤30% 更好。建议同时展示 uniform 曲线。
- §3.6 Gradient Analysis 是 "suggestive" analysis（论文自己的措辞），但在 introduction 中被作为核心贡献列出（"Our contributions: Empirical: Output-distribution alignment ranking across five losses..."）。建议明确区分 verified empirical findings 和 suggestive analysis。
- Limitations 部分提到 "wall-clock speedup requires sparse kernel support not addressed here" 但没有讨论 Gumbel-Sigmoid 松弛在推理时是否完全被替换为 hard threshold——如果是，应明确说明推理时无额外开销来自松弛。

---

## 主要优势

1. **PPL 改善显著且一致**：14.5%（30%）到 50%（50%）的 PPL 改善在多架构上复现，这是一个实质性的经验发现。
2. **实验覆盖面广**：3 seeds、5 种 loss variants（forward KL/reverse KL/JSD/BCE/MSE）、3 种架构、2 种稀疏度、多种 allocation 策略。对于一篇 empirical study 来说，这个覆盖面高于大多数同类工作。
3. **C1 target-swap ablation 设计有创意**：虽然有 confound，但这个实验设计展示了 "训练出更好的 mask" 和 "更好的训练过程" 可以分离研究，这个思路对后续工作有启发。
4. **诚实报告负面结果**：论文明确报告了 MMLU/GSM8K 回退，没有试图隐藏或淡化；对 per-layer 分解的局限性也有坦率讨论。
5. **Taxonomy 有组织价值**：Table 1 的二维分类法（correction granularity × training signal coupling）为该领域提供了清晰的文献组织框架。
6. **可复现性好**：训练细节充分（lr, schedule, GPU, batch size, steps），承诺代码开源。

---

## 缺失引用

- Mirzadeh et al. (2024), "ReLU Strikes Back" 已引用。
- Sun et al. (2024), "Wanda" 已引用。
- 建议补充：Song et al. (2024), "ProSparse: Introducing and enhancing intrinsic activation sparsity within large language models" — 该工作同样研究 SwiGLU 的激活稀疏性但从训练阶段介入（已引用，确认在 references 中）。
- 建议补充：Zhang et al. (2024), "LoRAShear" — 研究 structured pruning with knowledge recovery，与本文的 knowledge regression 问题相关，可在 §4.2 讨论 knowledge-task regression 时引用。
- 未见引用 Kurtic et al. (2024), "ZipLM" — 关于 structured pruning 的 data-aware 方法，可补充。

---

## Overall Assessment

**评分：3.0 (Findings)**

**置信度：4/5**

**理由**：

本文做出了一个有意义的经验贡献——证明 output-distribution KL 可以显著改善稀疏预测器的 PPL 表现。实验覆盖面广，诚实报告了正负结果。然而三个 critical 问题阻止了主会议推荐：

(1) 论文的核心分析贡献（per-layer KL decomposition）存在根本性的 train-inference mismatch，使 "signal type vs coupling scope" 的 decomposition 不可靠——该分析仅在 30% 稀疏度下 "interpretable"，且即便在 30% 也只是 upper bound。

(2) 下游知识任务（MMLU, GSM8K）的系统性回退在所有模型/规模上复现，但缺乏机制性解释。对于声称改进稀疏预测质量的论文，这构成了方法有效性的根本质疑。

(3) n=3 seeds 下 downstream metrics 方差过大（MMLU σ=9.5pp, GSM8K σ=5.2pp），多数下游比较不具统计意义，但论文仍在 abstract 和 conclusion 中以确定性措辞报告 gap 数值。

如果作者能 (a) 将 decomposition 的 claim 弱化为 exploratory upper bound 而非核心结论，(b) 增加 downstream 的 seed 数或控制 MMLU 方差，(c) 对 knowledge regression 提供更强的机制性证据，本文有望在下一轮达到 conference 水平。

当前贡献——"KL 训练在 PPL 上更好但在知识任务上更差" + "mask 模式可迁移"——符合 Findings 的接收标准（soundness + reproducibility），但 excitement 和 impact 不足以推荐主会议。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2246 · 2026-05-24T03:04:36.974155+00:00_

Reviewer 1 审稿意见已收到。评分 3.0（Findings），3 个 Critical issue，5 个 Warning。等待 Reviewer 2 审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 195

## Round 195

2 recorded events


### User

_source line 2247 · 2026-05-24T03:04:39.542988+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：给出 **Overall 3.0 (Findings)** 评分，识别了 3 个 critical 问题：
1. Per-layer KL 分解存在根本性 train-inference mismatch，K=1 下 1/32 层 mask 使 decomposition claim 站不住脚
2. 下游知识任务（MMLU/GSM8K）系统性回退缺乏机制性解释，与 "改善稀疏预测质量" 的核心 claim 矛盾
3. n=3 seeds 下 downstream metrics 方差过大（MMLU σ=9.5pp），多数比较不具统计意义

另有 5 个 should-fix（C1 confound、MSE 50% 不稳定、缺 30% BCE isocompute、ε 无 sensitivity analysis、评估指标单一）。肯定了 PPL 改善的显著性、实验覆盖面和诚实报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2248 · 2026-05-24T03:04:44.542367+00:00_

Reviewer 1 意见已收到。等待 Reviewer 2 返回后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 196

## Round 196

6 recorded events


### User

_source line 2249 · 2026-05-24T03:05:30.951567+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs

### 总体评分

**Overall**: 3.0 (Findings)
**Confidence**: 4/5
**一句话总结**: 方法论上扎实的实证研究揭示了 KL 对 BCE 在稀疏性预测上的 PPL 优势，但新颖性增量有限、无 wall-clock 加速、且知识密集型任务的系统性退步严重削弱了实际价值。

### 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计扎实（3-seed, 多架构, 多消融）；但 1000 步 WikiText-103 训练规模极小，per-layer KL 分解自认有混淆因素（"upper bound"），实际稀疏率不完全匹配（28.5% vs 29.3%）虽有补偿分析但增加解读复杂度 |
| Excitement | 2.5/5 | 核心发现（KL > BCE for sparsity prediction）符合信息论直觉，非高度意外；实际部署场景下无任何加速（+6.4% latency），知识任务全面退步，限制了研究的启发性 |
| Reproducibility | 4/5 | 超参数完整，exp_id 标注清晰，3-seed 评估，承诺开源代码；但训练数据处理细节（tokenization, 数据划分）不够明确 |
| Overall | 3.0/5 | 实证贡献达到 Findings 水平但不足以进入主会议：novelty 增量有限、无实际加速、知识退步未解决 |

### Must-Fix 问题（影响接收决定）

**N1** [critical] 知识密集型任务的系统性退步被严重低估（Framing 问题）

- 具体位置：Abstract ("directional commonsense gains")、Section 4.2 Knowledge-Task Regression、Conclusion（仅 2 句话）
- 问题：MMLU 在 8B 上从 65.3% 降至 40.7%（-24.6pp，降幅 37.7%），在 14B 上 GSM8K 从 87.6% 降至 32.0±5.2%（-55.6pp，降幅 63.5%）。Abstract 用 "directional commonsense gains (n=3) but knowledge-intensive regression" 的并列结构暗示两者是同量级的 trade-off，但实际上退步幅度远大于提升幅度。Conclusion 仅 2 句话完全没有讨论这个问题的影响和未来研究方向。
- 为什么影响接收：PPL improvement 虽然显著（14.5%），但 PPL 只是语言模型能力的代理指标。在下游任务（deployment-relevant metrics）上全面退步的方法，其实用性需要更审慎的讨论。
- 建议修改方向：(1) Abstract 中明确量化退步幅度而非用 "directional" 模糊处理；(2) Conclusion 需要扩展到至少一段话，讨论 knowledge regression 的 implications 和 future directions；(3) 在 Section 4.2 中明确区分 PPL improvement 和 downstream improvement 的不同 implications

**N2** [critical] 新颖性边界模糊——与 MaskLLM 的区分不充分

- 具体位置：Section 2 Related Work（MaskLLM 段落）、Section 3.7 Table 1
- 问题：MaskLLM (Fang et al., 2024) 已经使用 frozen weights + learnable masks + KL divergence 训练稀疏性。论文列出 3 点区别（static vs contextual, no cross-layer, input-independent），但这些区别的重要性缺乏实验验证。论文自己也承认 "shares the recipe-level principle"（page 3）。对于一篇定位为 "primarily an empirical study" 的论文，如果核心方法的每个组件都已被提出过，且 recipe-level 原则与 MaskLLM 共享，那么 "组合新颖性" 的 bar 需要由极强的实证发现来支撑——但知识退步削弱了这一支撑。
- 为什么影响接收：EMNLP 对 novelty 的要求不仅是技术组件的新颖性，也包括 insight 的新颖性。"KL 优于 BCE" 在给定足够 output-level 信息的情况下符合直觉预期（end-to-end optimization over proxy optimization），不够 surprising。
- 建议修改方向：(1) 加入与 MaskLLM 的直接实验对比；(2) 更清晰地阐述为什么 contextual activation sparsity 下的 KL 行为与 static N:M weight sparsity 下 qualitatively 不同；(3) 讨论 MaskLLM 的 "学习时动态、推理时静态" 中间态

**N3** [critical] 无 wall-clock 加速 + predictor 增加 6.4% latency = 实际减速

- 具体位置：Appendix A (Table 5)、Section 1 (最后一段)、Limitations
- 问题：当前方法在任何设置下都不提供推理加速。Predictor 增加 6.4% latency，但由于缺乏 sparse kernel 支持，稀疏 FFN 的计算量并未减少。4 条 contributions 中有 2 条标记为 "Practical"，但在无法提供任何加速的情况下，"Practical" 的标签有误导性。
- 为什么影响接收：审稿人会合理质疑：如果方法不能提供加速，又在知识任务上退步，那么 "better sparsity predictor" 的价值何在？
- 建议修改方向：(1) 将 contribution C3/C4 改为 "Analytical" 而非 "Practical"；(2) 在 Introduction 更早、更显著地声明无加速的现状

### Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Table 1 taxonomy 缺乏分析深度——空格子无分析，本质上只是 literature organization tool

**W2** [warning] 训练规模极小（1000 步, ~8.2M tokens），无法确认更大规模下 KL vs BCE 的相对优势是否保持

**W3** [warning] Per-layer KL 分解（§4.5）的 confound 未充分消除——K=1 混淆 coupling removal 与 train-inference mismatch，K=4 的 MMLU 异常说明分配模式本身就是 confound。"May account for a substantial portion" 的 claim 对于 admittedly exploratory 的分析过强

**W4** [warning] Introduction 包含近 20 个数字，信息过载。建议只保留 3-5 个核心数字，其余推到 Section 4

**W5** [warning] Conclusion 仅 2 句话——无 broader impact、future work、或 knowledge regression 解决方向的讨论

**W6** [warning] 附录 25 个 section（A-Y, 9 页），审稿人认知负担大。部分关键数据（HellaSwag/PIQA downstream）本应在主文 Table 2 中

### 小问题

- Abstract ~190 words，合规但信息密度极高
- Section 3 有 7 个 subsection（~2.5 页），对 "primarily empirical study" 而言 method section 偏重
- Limitations 未显式提及仅验证了 SwiGLU 架构
- Appendix Y 披露 Claude 用于 "summarizing related papers"——建议确认所有引用已人工验证

### 格式合规性

- 正文 8 页：合规
- Limitations 在正文（page 9）：合规
- 匿名性：合规（"Anonymous ACL submission"，无代码链接）
- 引用格式：acl_natbib.bst，合规

### 可能遗漏的相关工作

- ActTail (2026, arXiv:2603.12272)：基于 Heavy-Tailed Self-Regularization 的全局激活稀疏性分配
- WiSparse (2026, arXiv:2602.14452)：Weight-Aware Mixed Activation Sparsity
- 总体 related work 覆盖面良好

### 主要优势

- 实验方法论扎实：3-seed 评估、exp_id 标注、cross-architecture 验证（3 个模型）、多层消融
- Target-swap ablation (C1) 有独立的 insight 价值——证明 mask patterns 而非 gradient coupling 是 KL 优势的主要来源
- 诚实的 limitation acknowledgment，比多数论文更透明
- 补偿网络冗余性发现有工程简化价值
- K-curve 分析揭示 coupling breadth 的非单调效应

### Questions to Authors

1. TEAL uniform 在 30% 时 MMLU 达到 45.86%（Table 2），显著高于 KL 的 40.7±1.3%。对于实际部署，TEAL 在 knowledge tasks 上是否是更好的选择？
2. C4 训练控制实验显示 C4-trained predictor PPL 反而更差（11.55 vs 8.82），是否说明 KL predictor 在 overfitting WikiText-103 的 activation patterns？
3. 能否提供 20-25% sparsity 下的详细 downstream 对比，展示 KL 在 practical regime 中的优势？
4. Table 1 中 ShadowLLM 被归入 "Per-token × Intermediate (MSE)"，但其使用 attention-based routing——分类是否准确？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2250 · 2026-05-24T03:06:44.549984+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "distill_sparse_swiglu",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n### 总体评分\n\n**Overall**: 3.0 (Findings)\n**Confidence**: 4/5\n**一句话总结**: 方法论上扎实的实证研究揭示了 KL 对 BCE 在稀疏性预测上的 PPL 优势，但新颖性增量有限、无 wall-clock 加速、且知识密集型任务的系统性退步严重削弱了实际价值。\n\n### 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计扎实（3-seed, 多架构, 多消融）；但 1000 步 WikiText-103 训练规模极小，per-layer KL 分解自认有混淆因素（\"upper bound\"），实际稀疏率不完全匹配（28.5% vs 29.3%）虽有补偿分析但增加解读复杂度 |\n| Excitement | 2.5/5 | 核心发现（KL > BCE for sparsity prediction）符合信息论直觉，非高度意外；实际部署场景下无任何加速（+6.4% latency），知识任务全面退步，限制了研究的启发性 |\n| Reproducibility | 4/5 | 超参数完整，exp_id 标注清晰，3-seed 评估，承诺开源代码；但训练数据处理细节（tokenization, 数据划分）不够明确 |\n| Overall | 3.0/5 | 实证贡献达到 Findings 水平但不足以进入主会议：novelty 增量有限、无实际加速、知识退步未解决 |\n\n### Must-Fix 问题\n\n**N1** [critical] 知识密集型任务的系统性退步被严重低估（Framing 问题）\n\n- 具体位置：Abstract (\"directional commonsense gains\")、Section 4.2 Knowledge-Task Regression、Conclusion（仅 2 句话）\n- 问题：MMLU 在 8B 上从 65.3% 降至 40.7%（-24.6pp，降幅 37.7%），在 14B 上 GSM8K 从 87.6% 降至 32.0±5.2%（-55.6pp，降幅 63.5%）。Abstract 用 \"directional commonsense gains (n=3) but knowledge-intensive regression\" 的并列结构暗示两者是同量级的 trade-off，但实际上退步幅度远大于提升幅度。Conclusion 仅 2 句话完全没有讨论这个问题的影响和未来研究方向。\n- 为什么影响接收：PPL improvement 虽然显著（14.5%），但 PPL 只是语言模型能力的代理指标。在下游任务（deployment-relevant metrics）上全面退步的方法，其实用性需要更审慎的讨论。\n- 建议修改方向：(1) Abstract 中明确量化退步幅度而非用 \"directional\" 模糊处理；(2) Conclusion 需要扩展到至少一段话，讨论 knowledge regression 的 implications 和 future directions；(3) 在 Section 4.2 中明确区分 PPL improvement 和 downstream improvement 的不同 implications\n\n**N2** [critical] 新颖性边界模糊——与 MaskLLM 的区分不充分\n\n- 具体位置：Section 2 Related Work（MaskLLM 段落）、Section 3.7 Table 1\n- 问题：MaskLLM (Fang et al., 2024) 已经使用 frozen weights + learnable masks + KL divergence 训练稀疏性。论文列出 3 点区别（static vs contextual, no cross-layer, input-independent），但这些区别的重要性缺乏实验验证。论文自己也承认 \"shares the recipe-level principle\"（page 3）。对于一篇定位为 \"primarily an empirical study\" 的论文，如果核心方法的每个组件都已被提出过，且 recipe-level 原则与 MaskLLM 共享，那么 \"组合新颖性\" 的 bar 需要由极强的实证发现来支撑——但知识退步削弱了这一支撑。\n- 为什么影响接收：EMNLP 对 novelty 的要求不仅是技术组件的新颖性，也包括 insight 的新颖性。\"KL 优于 BCE\" 在给定足够 output-level 信息的情况下符合直觉预期（end-to-end optimization over proxy optimization），不够 surprising。\n- 建议修改方向：(1) 加入与 MaskLLM 的直接实验对比；(2) 更清晰地阐述为什么 contextual activation sparsity 下的 KL 行为与 static N:M weight sparsity 下 qualitatively 不同；(3) 讨论 MaskLLM 的 \"学习时动态、推理时静态\" 中间态\n\n**N3** [critical] 无 wall-clock 加速 + predictor 增加 6.4% latency = 实际减速\n\n- 具体位置：Appendix A (Table 5)、Section 1 (最后一段)、Limitations\n- 问题：当前方法在任何设置下都不提供推理加速。Predictor 增加 6.4% latency，但由于缺乏 sparse kernel 支持，稀疏 FFN 的计算量并未减少。4 条 contributions 中有 2 条标记为 \"Practical\"，但在无法提供任何加速的情况下，\"Practical\" 的标签有误导性。\n- 为什么影响接收：审稿人会合理质疑：如果方法不能提供加速，又在知识任务上退步，那么 \"better sparsity predictor\" 的价值何在？\n- 建议修改方向：(1) 将 contribution C3/C4 改为 \"Analytical\" 而非 \"Practical\"；(2) 在 Introduction 更早、更显著地声明无加速的现状\n\n### Should-Fix 问题\n\n**W1** [warning] Table 1 taxonomy 缺乏分析深度——空格子无分析，本质上只是 literature organization tool\n\n**W2** [warning] 训练规模极小（1000 步, ~8.2M tokens），无法确认更大规模下 KL vs BCE 的相对优势是否保持\n\n**W3** [warning] Per-layer KL 分解（§4.5）的 confound 未充分消除——K=1 混淆 coupling removal 与 train-inference mismatch，K=4 的 MMLU 异常说明分配模式本身就是 confound。\"May account for a substantial portion\" 的 claim 对于 admittedly exploratory 的分析过强\n\n**W4** [warning] Introduction 包含近 20 个数字，信息过载。建议只保留 3-5 个核心数字，其余推到 Section 4\n\n**W5** [warning] Conclusion 仅 2 句话——无 broader impact、future work、或 knowledge regression 解决方向的讨论\n\n**W6** [warning] 附录 25 个 section（A-Y, 9 页），审稿人认知负担大。部分关键数据（HellaSwag/PIQA downstream）本应在主文 Table 2 中\n\n### 小问题\n\n- Abstract ~190 words，合规但信息密度极高\n- Section 3 有 7 个 subsection（~2.5 页），对 \"primarily empirical study\" 而言 method section 偏重\n- Limitations 未显式提及仅验证了 SwiGLU 架构\n- Appendix Y 披露 Claude 用于 \"summarizing related papers\"——建议确认所有引用已人工验证\n\n### 格式合规性\n\n- 正文 8 页：合规\n- Limitations 在正文（page 9）：合规\n- 匿名性：合规\n- 引用格式：合规\n\n### 可能遗漏的相关工作\n\n- ActTail (2026, arXiv:2603.12272)\n- WiSparse (2026, arXiv:2602.14452)\n\n### 主要优势\n\n- 实验方法论扎实：3-seed 评估、exp_id 标注、cross-architecture 验证（3 个模型）、多层消融\n- Target-swap ablation (C1) 有独立的 insight 价值\n- 诚实的 limitation acknowledgment\n- 补偿网络冗余性发现有工程简化价值\n- K-curve 分析揭示 coupling breadth 的非单调效应\n\n### Questions to Authors\n\n1. TEAL uniform 在 30% 时 MMLU 达到 45.86%，显著高于 KL 的 40.7±1.3%。对于实际部署，TEAL 在 knowledge tasks 上是否是更好的选择？\n2. C4 训练控制实验显示 C4-trained predictor PPL 反而更差（11.55 vs 8.82），是否说明 KL predictor 在 overfitting WikiText-103 的 activation patterns？\n3. 能否提供 20-25% sparsity 下的详细 downstream 对比？\n4. Table 1 中 ShadowLLM 被归入 \"Per-token × Intermediate (MSE)\"，但其使用 attention-based routing——分类是否准确？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "distill_sparse_swiglu",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n### 总体评分\n\n**Overall**: 3.0 (Findings)\n**Confidence**: 4/5\n**一句话总结**: 方法论上扎实的实证研究揭示了 KL 对 BCE 在稀疏性预测上的 PPL 优势，但新颖性增量有限、无 wall-clock 加速、且知识密集型任务的系统性退步严重削弱了实际价值。\n\n### 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计扎实（3-seed, 多架构, 多消融）；但 1000 步 WikiText-103 训练规模极小，per-layer KL 分解自认有混淆因素（\"upper bound\"），实际稀疏率不完全匹配（28.5% vs 29.3%）虽有补偿分析但增加解读复杂度 |\n| Excitement | 2.5/5 | 核心发现（KL > BCE for sparsity prediction）符合信息论直觉，非高度意外；实际部署场景下无任何加速（+6.4% latency），知识任务全面退步，限制了研究的启发性 |\n| Reproducibility | 4/5 | 超参数完整，exp_id 标注清晰，3-seed 评估，承诺开源代码；但训练数据处理细节（tokenization, 数据划分）不够明确 |\n| Overall | 3.0/5 | 实证贡献达到 Findings 水平但不足以进入主会议：novelty 增量有限、无实际加速、知识退步未解决 |\n\n### Must-Fix 问题\n\n**N1** [critical] 知识密集型任务的系统性退步被严重低估（Framing 问题）\n\n- 具体位置：Abstract (\"directional commonsense gains\")、Section 4.2 Knowledge-Task Regression、Conclusion（仅 2 句话）\n- 问题：MMLU 在 8B 上从 65.3% 降至 40.7%（-24.6pp，降幅 37.7%），在 14B 上 GSM8K 从 87.6% 降至 32.0±5.2%（-55.6pp，降幅 63.5%）。Abstract 用 \"directional commonsense gains (n=3) but knowledge-intensive regression\" 的并列结构暗示两者是同量级的 trade-off，但实际上退步幅度远大于提升幅度。Conclusion 仅 2 句话完全没有讨论这个问题的影响和未来研究方向。\n- 为什么影响接收：PPL improvement 虽然显著（14.5%），但 PPL 只是语言模型能力的代理指标。在下游任务（deployment-relevant metrics）上全面退步的方法，其实用性需要更审慎的讨论。\n- 建议修改方向：(1) Abstract 中明确量化退步幅度而非用 \"directional\" 模糊处理；(2) Conclusion 需要扩展到至少一段话，讨论 knowledge regression 的 implications 和 future directions；(3) 在 Section 4.2 中明确区分 PPL improvement 和 downstream improvement 的不同 implications\n\n**N2** [critical] 新颖性边界模糊——与 MaskLLM 的区分不充分\n\n- 具体位置：Section 2 Related Work（MaskLLM 段落）、Section 3.7 Table 1\n- 问题：MaskLLM (Fang et al., 2024) 已经使用 frozen weights + learnable masks + KL divergence 训练稀疏性。论文列出 3 点区别（static vs contextual, no cross-layer, input-independent），但这些区别的重要性缺乏实验验证。论文自己也承认 \"shares the recipe-level principle\"（page 3）。对于一篇定位为 \"primarily an empirical study\" 的论文，如果核心方法的每个组件都已被提出过，且 recipe-level 原则与 MaskLLM 共享，那么 \"组合新颖性\" 的 bar 需要由极强的实证发现来支撑——但知识退步削弱了这一支撑。\n- 为什么影响接收：EMNLP 对 novelty 的要求不仅是技术组件的新颖性，也包括 insight 的新颖性。\"KL 优于 BCE\" 在给定足够 output-level 信息的情况下符合直觉预期（end-to-end optimization over proxy optimization），不够 surprising。\n- 建议修改方向：(1) 加入与 MaskLLM 的直接实验对比；(2) 更清晰地阐述为什么 contextual activation sparsity 下的 KL 行为与 static N:M weight sparsity 下 qualitatively 不同；(3) 讨论 MaskLLM 的 \"学习时动态、推理时静态\" 中间态\n\n**N3** [critical] 无 wall-clock 加速 + predictor 增加 6.4% latency = 实际减速\n\n- 具体位置：Appendix A (Table 5)、Section 1 (最后一段)、Limitations\n- 问题：当前方法在任何设置下都不提供推理加速。Predictor 增加 6.4% latency，但由于缺乏 sparse kernel 支持，稀疏 FFN 的计算量并未减少。4 条 contributions 中有 2 条标记为 \"Practical\"，但在无法提供任何加速的情况下，\"Practical\" 的标签有误导性。\n- 为什么影响接收：审稿人会合理质疑：如果方法不能提供加速，又在知识任务上退步，那么 \"better sparsity predictor\" 的价值何在？\n- 建议修改方向：(1) 将 contribution C3/C4 改为 \"Analytical\" 而非 \"Practical\"；(2) 在 Introduction 更早、更显著地声明无加速的现状\n\n### Should-Fix 问题\n\n**W1** [warning] Table 1 taxonomy 缺乏分析深度——空格子无分析，本质上只是 literature organization tool\n\n**W2** [warning] 训练规模极小（1000 步, ~8.2M tokens），无法确认更大规模下 KL vs BCE 的相对优势是否保持\n\n**W3** [warning] Per-layer KL 分解（§4.5）的 confound 未充分消除——K=1 混淆 coupling removal 与 train-inference mismatch，K=4 的 MMLU 异常说明分配模式本身就是 confound。\"May account for a substantial portion\" 的 claim 对于 admittedly exploratory 的分析过强\n\n**W4** [warning] Introduction 包含近 20 个数字，信息过载。建议只保留 3-5 个核心数字，其余推到 Section 4\n\n**W5** [warning] Conclusion 仅 2 句话——无 broader impact、future work、或 knowledge regression 解决方向的讨论\n\n**W6** [warning] 附录 25 个 section（A-Y, 9 页），审稿人认知负担大。部分关键数据（HellaSwag/PIQA downstream）本应在主文 Table 2 中\n\n### 小问题\n\n- Abstract ~190 words，合规但信息密度极高\n- Section 3 有 7 个 subsection（~2.5 页），对 \"primarily empirical study\" 而言 method section 偏重\n- Limitations 未显式提及仅验证了 SwiGLU 架构\n- Appendix Y 披露 Claude 用于 \"summarizing related papers\"——建议确认所有引用已人工验证\n\n### 格式合规性\n\n- 正文 8 页：合规\n- Limitations 在正文（page 9）：合规\n- 匿名性：合规\n- 引用格式：合规\n\n### 可能遗漏的相关工作\n\n- ActTail (2026, arXiv:2603.12272)\n- WiSparse (2026, arXiv:2602.14452)\n\n### 主要优势\n\n- 实验方法论扎实：3-seed 评估、exp_id 标注、cross-architecture 验证（3 个模型）、多层消融\n- Target-swap ablation (C1) 有独立的 insight 价值\n- 诚实的 limitation acknowledgment\n- 补偿网络冗余性发现有工程简化价值\n- K-curve 分析揭示 coupling breadth 的非单调效应\n\n### Questions to Authors\n\n1. TEAL uniform 在 30% 时 MMLU 达到 45.86%，显著高于 KL 的 40.7±1.3%。对于实际部署，TEAL 在 knowledge tasks 上是否是更好的选择？\n2. C4 训练控制实验显示 C4-trained predictor PPL 反而更差（11.55 vs 8.82），是否说明 KL predictor 在 overfitting WikiText-103 的 activation patterns？\n3. 能否提供 20-25% sparsity 下的详细 downstream 对比？\n4. Table 1 中 ShadowLLM 被归入 \"Per-token × Intermediate (MSE)\"，但其使用 attention-based routing——分类是否准确？"
  }
}
```

</details>

---


### Tool result

_source line 2251 · 2026-05-24T03:07:27.774514+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 43224
}
```

</details>

---


### Tool call

_source line 2252 · 2026-05-24T03:07:27.976445+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "distill_sparse_swiglu",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性 + 实验设计）\n\n### Summary\n\n本文研究 SwiGLU LLM 中上下文稀疏性预测器的训练目标选择。核心提议是用 forward KL divergence 替代传统 BCE，通过 Gumbel-Sigmoid 松弛实现可微 mask 采样，训练轻量级预测器（<1% 参数）。在 LLaMA-3.1-8B 上，30% 稀疏度下 KL 预测器 PPL 比 TEAL 低 14.5%（8.81 vs 10.30），但 MMLU/GSM8K 出现系统性回退。C1 target-swap ablation 表明 KL 发现的 mask 模式可迁移到 BCE。per-layer KL 分解尝试分离 signal type 和 coupling scope 的贡献。跨架构验证确认 PPL 优势可泛化。\n\n### 总体评分\n\n**Overall**: 3.0 — Findings\n**置信度**: 4/5\n\n### 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心方法合理；但 per-layer KL 分解存在根本性 train-inference mismatch，下游 metric 统计功效不足 |\n| Excitement | 3/5 | 输出分布对齐训练稀疏预测器是有趣的方向；但方法本身是 KL 蒸馏 + Gumbel-Sigmoid 的组合，新颖性有限；下游回退限制实用价值 |\n| Reproducibility | 4/5 | 训练细节充分，承诺开源代码和 checkpoint；多 seed 实验增加可信度 |\n\n### Must-Fix 问题\n\n**N1** [critical] Per-layer KL 分解的 train-inference mismatch 使核心 decomposition claim 站不住脚\n\n- §4.5, Table 4, Figure 2\n- K=1 per-layer KL 训练时每步只 mask 1/32 层，推理时 32 层同时被 mask——根本性 train-inference mismatch。K=1 (PPL 9.05) vs E2E (8.81) 只有 2.7% gap 是因为 K=1 近似 dense evaluation。\n- 关键证据：50% 下 K=1 PPL=34.85 vs E2E=11.84（2.94×）；K=4 在 50% 更差（44.23）；K-curve 非单调（K=2 最差 10.75）\n- 建议：(1) 将 K=1 结果标注为 \"upper bound only\"；(2) 报告 K=4 在 30% 的完整 downstream CI；(3) 讨论为什么 decomposition 在 50% 失效\n\n**N2** [critical] 下游知识任务系统性回退缺乏机制性解释\n\n- Table 2, §4.2, §4.6\n- KL 在所有模型/规模上系统性损害 MMLU 和 GSM8K（8B: -5.2pp MMLU, 14B: -20.1pp GSM8K）\n- C4 控制排除了训练数据偏差，但 forward KL mode-covering 假设没有直接验证（如分析是否 prune 了 factual neurons）\n- 建议：(1) 分析 KL mask 对 factual neurons 的保留率；(2) 讨论 hybrid loss 可能性；(3) 重新框定为 \"PPL-optimal but not task-universal\"\n\n**N3** [critical] 下游 metric 统计功效严重不足\n\n- Table 2, §4.2, §4.6\n- KL global 30% MMLU: 35.7±9.5pp (n=3)，95% CI ≈ [22.1, 49.3]\n- Qwen-14B GSM8K: 32.0±5.2pp (n=3)，95% CI ≈ ±7.4pp\n- 论文承认 \"95% CI overlap\" 但仍在 abstract/conclusion 以确定性措辞报告 gap\n- 建议：(1) 增加 seed 到 ≥5；(2) 对 TEAL 也跑多次；(3) 所有比较报告 CI 和 overlap 标注\n\n### Should-Fix 问题\n\n**W1** [warning] C1 target-swap ablation 的 confound 未充分控制\n- s42 oracle 来自 non-seed-matched earlier training run\n- BCE+Gumbel (32.22) vs BCE (27.97) 显示 Gumbel 对 BCE 有害，confound 未消除\n- 建议统一 seed-matched oracle + 增加 \"BCE+Gumbel on KL targets\" 条件\n\n**W2** [warning] MSE baseline 在 50% 下几乎不可信\n- s123 catastrophic (PPL=15,789)，2/3 seed 失败\n- 建议移至 Appendix 或仅在 30% 使用\n\n**W3** [warning] 30% 下缺少 BCE isocompute 对比\n\n**W4** [warning] ε=0.02 deadzone margin 缺乏 sensitivity analysis\n\n**W5** [warning] 主评估指标单一（仅 WikiText-2 PPL）\n\n### 小问题\n\n- TEAL 是 deterministic single-run vs KL 3-seed 比较不对等\n- Figure 3 只展示 global allocation\n- §3.6 Gradient Analysis 是 \"suggestive\" 但在 introduction 被列为核心贡献\n- 推理时 Gumbel-Sigmoid 是否被 hard threshold 替换应明确说明\n\n### 主要优势\n\n1. PPL 改善显著且一致（14.5%-50%）\n2. 实验覆盖面广（3 seeds, 5 losses, 3 architectures, 2 sparsity levels）\n3. C1 target-swap ablation 设计有创意\n4. 诚实报告负面结果\n5. Taxonomy 有组织价值\n6. 可复现性好\n\n### 缺失引用\n\n- 建议补充 LoRAShear（structured pruning + knowledge recovery）\n- 建议补充 ZipLM（data-aware structured pruning）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "distill_sparse_swiglu",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性 + 实验设计）\n\n### Summary\n\n本文研究 SwiGLU LLM 中上下文稀疏性预测器的训练目标选择。核心提议是用 forward KL divergence 替代传统 BCE，通过 Gumbel-Sigmoid 松弛实现可微 mask 采样，训练轻量级预测器（<1% 参数）。在 LLaMA-3.1-8B 上，30% 稀疏度下 KL 预测器 PPL 比 TEAL 低 14.5%（8.81 vs 10.30），但 MMLU/GSM8K 出现系统性回退。C1 target-swap ablation 表明 KL 发现的 mask 模式可迁移到 BCE。per-layer KL 分解尝试分离 signal type 和 coupling scope 的贡献。跨架构验证确认 PPL 优势可泛化。\n\n### 总体评分\n\n**Overall**: 3.0 — Findings\n**置信度**: 4/5\n\n### 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心方法合理；但 per-layer KL 分解存在根本性 train-inference mismatch，下游 metric 统计功效不足 |\n| Excitement | 3/5 | 输出分布对齐训练稀疏预测器是有趣的方向；但方法本身是 KL 蒸馏 + Gumbel-Sigmoid 的组合，新颖性有限；下游回退限制实用价值 |\n| Reproducibility | 4/5 | 训练细节充分，承诺开源代码和 checkpoint；多 seed 实验增加可信度 |\n\n### Must-Fix 问题\n\n**N1** [critical] Per-layer KL 分解的 train-inference mismatch 使核心 decomposition claim 站不住脚\n\n- §4.5, Table 4, Figure 2\n- K=1 per-layer KL 训练时每步只 mask 1/32 层，推理时 32 层同时被 mask——根本性 train-inference mismatch。K=1 (PPL 9.05) vs E2E (8.81) 只有 2.7% gap 是因为 K=1 近似 dense evaluation。\n- 关键证据：50% 下 K=1 PPL=34.85 vs E2E=11.84（2.94×）；K=4 在 50% 更差（44.23）；K-curve 非单调（K=2 最差 10.75）\n- 建议：(1) 将 K=1 结果标注为 \"upper bound only\"；(2) 报告 K=4 在 30% 的完整 downstream CI；(3) 讨论为什么 decomposition 在 50% 失效\n\n**N2** [critical] 下游知识任务系统性回退缺乏机制性解释\n\n- Table 2, §4.2, §4.6\n- KL 在所有模型/规模上系统性损害 MMLU 和 GSM8K（8B: -5.2pp MMLU, 14B: -20.1pp GSM8K）\n- C4 控制排除了训练数据偏差，但 forward KL mode-covering 假设没有直接验证（如分析是否 prune 了 factual neurons）\n- 建议：(1) 分析 KL mask 对 factual neurons 的保留率；(2) 讨论 hybrid loss 可能性；(3) 重新框定为 \"PPL-optimal but not task-universal\"\n\n**N3** [critical] 下游 metric 统计功效严重不足\n\n- Table 2, §4.2, §4.6\n- KL global 30% MMLU: 35.7±9.5pp (n=3)，95% CI ≈ [22.1, 49.3]\n- Qwen-14B GSM8K: 32.0±5.2pp (n=3)，95% CI ≈ ±7.4pp\n- 论文承认 \"95% CI overlap\" 但仍在 abstract/conclusion 以确定性措辞报告 gap\n- 建议：(1) 增加 seed 到 ≥5；(2) 对 TEAL 也跑多次；(3) 所有比较报告 CI 和 overlap 标注\n\n### Should-Fix 问题\n\n**W1** [warning] C1 target-swap ablation 的 confound 未充分控制\n- s42 oracle 来自 non-seed-matched earlier training run\n- BCE+Gumbel (32.22) vs BCE (27.97) 显示 Gumbel 对 BCE 有害，confound 未消除\n- 建议统一 seed-matched oracle + 增加 \"BCE+Gumbel on KL targets\" 条件\n\n**W2** [warning] MSE baseline 在 50% 下几乎不可信\n- s123 catastrophic (PPL=15,789)，2/3 seed 失败\n- 建议移至 Appendix 或仅在 30% 使用\n\n**W3** [warning] 30% 下缺少 BCE isocompute 对比\n\n**W4** [warning] ε=0.02 deadzone margin 缺乏 sensitivity analysis\n\n**W5** [warning] 主评估指标单一（仅 WikiText-2 PPL）\n\n### 小问题\n\n- TEAL 是 deterministic single-run vs KL 3-seed 比较不对等\n- Figure 3 只展示 global allocation\n- §3.6 Gradient Analysis 是 \"suggestive\" 但在 introduction 被列为核心贡献\n- 推理时 Gumbel-Sigmoid 是否被 hard threshold 替换应明确说明\n\n### 主要优势\n\n1. PPL 改善显著且一致（14.5%-50%）\n2. 实验覆盖面广（3 seeds, 5 losses, 3 architectures, 2 sparsity levels）\n3. C1 target-swap ablation 设计有创意\n4. 诚实报告负面结果\n5. Taxonomy 有组织价值\n6. 可复现性好\n\n### 缺失引用\n\n- 建议补充 LoRAShear（structured pruning + knowledge recovery）\n- 建议补充 ZipLM（data-aware structured pruning）"
  }
}
```

</details>

---


### Tool result

_source line 2253 · 2026-05-24T03:07:29.333188+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1356
}
```

</details>

---


### Assistant

_source line 2254 · 2026-05-24T03:07:32.787228+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 197

## Round 197

2 recorded events


### User

_source line 2255 · 2026-05-24T03:07:35.313913+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

总结：

- **Overall 3.0 (Findings)**，Soundness 3.5, Excitement 2.5, Confidence 4/5
- **3 个 Must-Fix**：(1) 知识退步被 framing 低估（MMLU -24.6pp 却用 "directional" 模糊处理）；(2) 与 MaskLLM 的 novelty 区分不充分（共享 recipe-level 原则）；(3) 无 wall-clock 加速却标注 "Practical" contributions
- **6 个 Should-Fix**：taxonomy 浅、训练规模极小、per-layer KL 分解有 confounds、Introduction 数字过载、Conclusion 仅 2 句、附录 25 节过长
- **主要优势**：实验方法论扎实（3-seed, 3 架构）、target-swap ablation 有 insight 价值、透明的 limitation disclosure

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2256 · 2026-05-24T03:07:42.380424+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 198

## Round 198

2 recorded events


### User

_source line 2257 · 2026-05-24T03:09:25.763412+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### R2-N1: 知识密集型任务系统性退步被严重低估（Framing 问题）

[REBUT] R2 的数值论证存在关键性错误。

R2 声称 "MMLU 在 8B 上从 65.3% 降至 40.7%（-24.6pp，降幅 37.7%），在 14B 上 GSM8K 从 87.6% 降至 32.0±5.2%（-55.6pp，降幅 63.5%）"——但 65.3% 和 87.6% 是 **dense model（0% sparsity）**的性能，不是 baseline sparsity method 的性能。将 KL 30% 与 dense 0% 对比来论证 KL 的 "退步" 是错误的基准选择：**所有** 30% 稀疏方法都会大幅降低 MMLU/GSM8K。

正确的比较是 KL vs TEAL **在同一稀疏度下**：
- LLaMA-8B MMLU: KL uniform 40.7±1.3 vs TEAL uniform 45.86 → gap = **−5.2pp**（Table 2）
- Qwen-14B GSM8K: KL 32.0±5.2 vs TEAL 52.1 → gap = **−20.1pp**（§4.6）

论文 abstract 明确量化了这些 vs-TEAL gap："knowledge-intensive regression (MMLU −5.2pp on 8B; GSM8K −20.1pp on 14B)"（abstract 第3句），并非 R2 所称的 "用 directional 模糊处理"——"directional" 修饰的是 commonsense gains（因 CI overlap），而 knowledge regression 有明确数字。

**部分同意**：Conclusion 确实只有 2 句话过于简短（§5），应扩展讨论 knowledge regression 的 implications 和 future directions。但 R2 对退步幅度的描述放大了约 5 倍（-24.6pp vs 实际 -5.2pp），这本身就是 framing 问题。

---

### R2-N2: 新颖性边界模糊——与 MaskLLM 的区分不充分

[REBUT] 要求与 MaskLLM 直接实验对比不合理，因为两者处于**根本不同的稀疏范式**。

MaskLLM（Fang et al., 2024）训练 **static N:M structured sparsity masks**（如 2:4 pattern），mask 在推理时 **固定不变**，不依赖输入。本文训练 **contextual unstructured sparsity predictors**，mask 在推理时 **per-token 动态生成**。这不是同一任务：
- N:M sparsity 有硬件加速支持（Tensor Cores）但不能 per-token 适应
- Contextual sparsity 利用 activation patterns 的输入依赖性但目前缺乏硬件支持

直接在同一 benchmark 上比较不 meaningful——sparsity pattern type（N:M vs unstructured）、allocation strategy（static vs dynamic）、inference protocol 完全不同。论文在 §2 和 Table 1 中已明确定位两者的区别（static row vs per-token row）。

**部分同意**：论文可以更清晰地阐述为什么 contextual activation sparsity 下 KL 的行为可能与 static N:M 下 qualitatively 不同——例如，contextual sparsity 的 mask 空间是 exponentially larger（每个 token 一个 mask vs 全局一个 mask），KL 的 mode-covering 特性在这个搜索空间中可能更有价值。

---

### R2-N3: 无 wall-clock 加速 + predictor 增加 6.4% latency = 实际减速

[AGREE] R2-N3: 关于 "Practical" 标签的质疑合理。

论文在 §1 最后一段和 Limitations 中已明确声明 "wall-clock speedup requires sparse kernel support not addressed here"，且 abstract 最后一句也说 "This is primarily an empirical study"。论文的自我定位是清楚的。

但 R2 指出 contribution C3/C4 使用 "Practical" 标签确实有误导风险（§1, contributions list）。C3 "target-swap ablation suggests KL-discovered mask patterns transfer to BCE" 和 C4 "compensation redundancy" 更准确地说是 **analytical findings with practical implications**，而非直接提供实际加速。将标签改为 "Analytical" 或 "Empirical" 更准确。

但我不同意 R2 将此列为 **critical/must-fix**：论文已在多处坦率声明无加速，这不构成 desk-reject 或 critical flaw。作为一篇 primarily empirical study of training objectives，无需提供 systems-level contribution。降级为 should-fix 更合适。

---

### R2-W1: Table 1 taxonomy 缺乏分析深度

[AGREE] R2-W1: Table 1 的空格子（如 Static×Decomposed）没有讨论为什么为空或是否值得探索，降低了 taxonomy 的学术价值。

但不同意 R2 说它"本质上只是 literature organization tool"——taxonomy 确实帮助定位了本文的贡献在方法空间中的位置（Per-token × Coupled），且论文在 Appendix O 中有更详细的 taxonomy discussion。作为一个 organizational framework 它是有用的，但主文中应至少提一句为什么某些格子为空。

---

### R2-W2: 训练规模极小（1000 步, ~8.2M tokens）

[AGREE] R2-W2: 这是合理的 concern。

但需要指出两个 mitigating factor：
1. Appendix B.2 (Table 8) 显示训练在 step 600 后 converge（95% quality gap closed），step 800-1000 性能趋于饱和。所以 1000 步对当前 setup 是 sufficient 的。
2. §4.3 isocompute 分析（Table 2）在 50% 下给了 BCE 2.71× 计算量（2700 步）但 KL 仍然 2.39× better，说明差距不是因为 BCE 训练不足。

但 R2 的核心 concern——更大规模训练（如 10K 步、更大数据集）下相对优势是否保持——确实没有回答。这是一个 valid limitation，但对于一篇声称 "primarily empirical study" 的论文来说，要求大规模训练验证似乎超出了合理范围。

---

### R2-W3: Per-layer KL 分解的 confound

[AGREE] R2-W3: 与我的 N1 完全一致。

K=1 混淆了 coupling removal 和 train-inference mismatch。论文自己承认这是 "upper bound"（§4.5, abstract 第5句），但 "may account for a substantial portion" 的措辞对于 admittedly exploratory 的分析来说过强。K=4 的 MMLU 异常（42.7±1.4 vs E2E 40.7±1.3, 超过 E2E）进一步说明 allocation pattern 本身就是 confound——K=4 近似 uniform allocation，而 E2E 是非 uniform 的，所以 MMLU 差异可能主要来自 allocation 而非 signal type/coupling。

---

### R2-W4: Introduction 数字过多

[REBUT] R2-W4: 这是主观的风格偏好。

Introduction 包含具体数字是为了满足 busy reviewer 快速获取核心发现的需求。ACL/EMNLP 的许多高引论文（如 TEAL, DejaVu）也在 introduction 中密集引用数字。数字过少反而会让 claim 显得 vague。这不是 soundness 或 excitement 问题。

---

### R2-W5: Conclusion 仅 2 句话

[AGREE] R2-W5: Conclusion（§5）确实过于简短。

一篇涉及复杂 trade-off（PPL vs downstream, signal type vs coupling）的论文需要在 conclusion 中总结 key takeaways、discuss broader implications、identify clear future directions。当前 2 句话没有做到任何一点。这在我的审稿中也有间接提及（建议讨论 knowledge regression 的 implications）。

---

### R2-W6: 附录 25 个 section（A-Y）认知负担大

[REBUT] R2-W6: 附录多是因为实验覆盖面广。

论文在主文中保持了 8 页正文合规，将补充材料放入附录是正确的做法。HellaSwag/PIQA 在主 Table 2 中确实缺失，但 Table 2 已有 6 列（PPL + 4 downstream），加入更多列会导致排版问题。Appendix I (Table 12) 提供了完整 downstream 数据，且在 §4.2 中通过文字描述了 HellaSwag/PIQA 的趋势（"4/4 wins at 30% uniform"）。

建议作者在 Table 2 中加入 HellaSwag 一列作为 commonsense reasoning 的代表，但这不影响论文的 soundness。

---

### R2 小问题回应

**Abstract ~190 words 信息密度高**：[AGREE] 确实密集，但在 200 word 限制内尽可能传递信息是合理的。

**Method section 偏重（7 subsections, ~2.5 pages）**：[REBUT] 对于引入 Gumbel-Sigmoid relaxation + geometric penalty schedule + KL training objective 的论文，方法描述需要足够详细以保证 reproducibility。

**Limitations 未提及仅验证 SwiGLU**：[AGREE] 这是一个合理的遗漏。论文标题包含 "SwiGLU"，但 Limitations 应明确说明未在 GeGLU 或其他 gated architecture 上验证。

**Appendix Y Claude 使用披露**：[AGREE] 重要提醒。论文应确认所有引用已人工验证，尤其是鉴于 LLM 可能产生幻觉引用。

---

### R2 Questions 回应

**Q1 (TEAL vs KL for deployment)**：合理问题。对于 knowledge-critical deployment，当前数据确实支持 TEAL 是更安全的选择（MMLU 45.86 vs 40.7）。但对于 PPL-sensitive 应用（如 generation quality），KL 可能更优。论文应更明确地讨论 use-case dependent recommendation。

**Q2 (C4 training control, overfitting)**：好问题。C4-trained predictor PPL 更差（11.55 vs 8.82, Table 22/§4.2）但 downstream 基本不变（MMLU 40.0% vs 40.7%），这不太像 overfitting——如果是 overfitting WikiText-103 patterns，我们会预期 C4-trained 的 downstream 更好。更可能的解释是 WikiText-103 的文本更干净/一致，有助于学习更好的稀疏 patterns。但这值得更深入的讨论。

**Q3 (20-25% sparsity downstream)**：[AGREE] 这是合理的实验请求。Figure 3 显示 20-25% 区间 PPL gap 较小，downstream 差异可能也更小，这对实际部署有重要参考价值。

**Q4 (ShadowLLM 分类)**：[AGREE] ShadowLLM 使用 attention-based routing，将其简单归入 "Intermediate (MSE)" 确实忽略了 routing mechanism 的区别。Table 1 的分类轴是 correction granularity × training signal coupling，但 ShadowLLM 的 attention-based routing 可能构成第三个轴的变化。

---

### R2 遗漏引用

**ActTail (2026, arXiv:2603.12272)** 和 **WiSparse (2026, arXiv:2602.14452)**：无法确认这些引用的存在性和相关性。如果它们确实存在且相关，应补充引用。

---

### 总结：与 R2 的评分分歧

我与 R2 在 **Overall 3.0 (Findings)** 上一致。

但在 Soundness 上我给 3/5 而 R2 给 3.5/5——我认为 per-layer KL 分解的方法学问题比 R2 评估的更严重（R2 将其放在 W3 should-fix，我放在 N1 must-fix）。

在 Excitement 上我给 3/5 而 R2 给 2.5/5——我认为 R2 低估了 C1 target-swap ablation 的 insight 价值和实验覆盖面的广度。同时 R2 的 N1（knowledge regression framing）使用了与 dense 比较的错误基准数字，夸大了退步程度。

R2 的 N2（MaskLLM novelty boundary）和 N3（无加速）有一定道理但不应是 critical/must-fix：N2 要求跨范式直接对比不合理，N3 论文已充分 disclaimer。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2258 · 2026-05-24T03:09:31.392494+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 199

## Round 199

2 recorded events


### User

_source line 2259 · 2026-05-24T03:09:41.295341+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 的逐条交叉回应。核心分歧点：

1. **R2-N1 [REBUT]**：R2 将 KL 与 dense model 比较（-24.6pp MMLU）是错误基准，正确比较是 KL vs TEAL at same sparsity（-5.2pp）。但同意 conclusion 过短。
2. **R2-N2 [REBUT]**：MaskLLM 是 static N:M sparsity，与 contextual unstructured sparsity 是不同范式，要求直接对比不合理。
3. **R2-N3 [AGREE]**："Practical" 标签有误导性，但不应是 critical issue（论文已多处声明无加速）。
4. **R2-W3 [AGREE]**：与我的 N1 一致，per-layer KL 分解 confound 是核心问题。
5. **Overall 3.0 一致**，但 Soundness/Excitement 维度评分有分歧。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2260 · 2026-05-24T03:09:48.061336+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 200

## Round 200

10 recorded events


### User

_source line 2261 · 2026-05-24T03:09:49.566001+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的交叉回应

### Must-Fix

[AGREE] R1-N1: Per-layer KL decomposition train-inference mismatch。完全同意。50% 下 K=1 PPL=34.85 vs E2E=11.84（Table 4）提供 decisive evidence——mismatch 加剧时 K=1 的"信号类型优势"完全瓦解。K=4 在 50% 反而更差（44.23 vs 34.85），论文自己承认 "the decomposition is interpretable only at 30%"（§4.5）。一个仅在 30% 有效且有未消除 confound 的 exploratory analysis 不应作为核心 contribution 呈现。我在自己的审稿中将此列为 W3，但认同 R1 将其提升至 critical 的判断。

[AGREE] R1-N2: 下游知识任务回退缺乏机制性解释。与我的 N1 呼应。补充：Appendix T 的 constraint analysis（remove valley → MMLU +3.4pp）说明的是 allocation pattern 影响而非 mode-covering 机制。C4 控制实验排除训练数据偏差后反而强化了"问题是 structural"的结论，但论文没有进一步追问 *为什么* 是 structural。R1 建议的 hybrid loss 方向是论文完全缺失的 future direction。

[AGREE] R1-N3: 下游 metric 统计功效不足。KL global 30% MMLU 35.7±9.5（n=3）差异极大。补充：Qwen-14B GSM8K 32.0±5.2（Table 13）CV=16.3%，不足以在 p<0.05 下确认与 TEAL（52.1%）的差异方向。不过 ≥5 seeds 在 14B 上可能有计算预算限制——至少应做 upfront disclosure。

### Should-Fix

[AGREE] R1-W1: C1 confounds。两个问题叠加：s42 non-seed-matched + BCE+Gumbel (32.22) 比 BCE (27.97) 更差说明 Gumbel 对 BCE 有害。不过 s123/s456 seed-matched oracles gap ≤1.18pp 部分缓解了 concern。

[AGREE] R1-W2: MSE 50% 不可信。s123 只达 5.1% sparsity（PPL=15,789），50% MSE 实际是单 seed 结果。

[AGREE] R1-W3: 30% 缺 BCE isocompute。

[REBUT] R1-W4: ε deadzone sensitivity。Appendix C（Table 9, Figure 4）间接展示了 ε=0.02 的稳定收敛。ε 是 auxiliary mechanism，重要性不高。Low-effort improvement 可以做但非 must-fix。

[AGREE] R1-W5: 主指标单一。部分同意——WikiText-2 与 WikiText-103 同源，C4 OOD evaluation（Appendix D）缓解但 cross-seed variance 显著更高（CV=6.3% vs 0.2%）。建议 C4 PPL 纳入主表。

### 小问题

[AGREE] TEAL deterministic vs KL 3-seed 不对等
[AGREE] Figure 3 只展示 global allocation
[AGREE] §3.6 Gradient Analysis "suggestive" vs 核心贡献的 caveat 不一致
[REBUT] 推理时 Gumbel→hard threshold 已在 §3.1 和 §3.3 明确说明

### 缺失引用

[REBUT] LoRAShear/ZipLM：两者是 weight pruning 方法，非 activation sparsity prediction。Section 2 已有 Wanda/SparseGPT/SliceGPT 覆盖此类。更相关的遗漏是 ActTail (2026) 和 WiSparse (2026)。

### 与 R1 的分歧

1. R1 未将 novelty/MaskLLM 区分列为 critical——我认为这是核心 weakness（我的 N2）
2. R1 未将无 wall-clock 加速列为 critical——我认为 "Practical" 标签在 +6.4% latency 下 misleading（我的 N3）
3. Excitement：R1 给 3/5，我给 2.5/5——"KL > BCE" 是 information-theoretically expected

### 共识：Overall 3.0 (Findings)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2262 · 2026-05-24T03:10:17.203568+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 2263 · 2026-05-24T03:10:17.305257+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-24T02:56:27.967182+00:00\", \"completed_at\": \"2026-05-24T03:00:24.578172+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1\", \"message\": \"Abstract 视觉长度偏长——目测可能接近或超过 200 words 上限（EMNLP 2026 硬约束），建议用工具精确计数确认\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无 display item，第一个视觉锚点 Figure 1 出现在 page 2 右栏——ACL 双栏格式下属正常，Figure 1 是方法概览图，能有效传达核心 idea\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 方法概览图整体清晰，但图内文字（箭头标注、模块名称）偏小，约为正文字号的 60-65%，在打印或低分辨率屏幕上可能不够清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"纯文本页（Related Work 后半段 + Method 开头），无 figure/table/equation；但 page 4 有大量公式，不构成连续纯文本页问题\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1（Taxonomy）设计整洁，使用 booktabs 风格，空 cell 用 dash 标注，结构清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"纯文本页（Experimental Setup），无 display item，介于 Table 1（page 5）和 Tables 2-4（page 7）之间；setup 页纯文本属于常见做法，不影响阅读\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"三张表格（Table 2/3/4）集中在同一页，视觉密度偏高；Tables 之间的文字段落很短，审稿人可能感到拥挤。建议考虑将 Table 4 下移或缩减 Table 3 行数\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Tables 2-4 均使用 booktabs 风格、最优值加粗、±标注不确定性，表格规范良好\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 2 和 Figure 3 分列左右栏，图表清晰可读，使用 orange/blue 双色方案（色盲友好），marker 形状有区分\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 2/3 的 axis tick label 字号偏小但仍可读；caption 包含足够解释信息，基本自包含\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Section 5 \\\"Conclusion\\\" 起始于页面底部约 1/4 处，后跟约 8-10 行正文，不构成孤悬 heading\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 简洁（~3 个点），符合 EMNLP 要求；References 紧接其后，页面填充率 >90%\"}, {\"severity\": \"info\", \"dimension\": \"pages 9-11\", \"message\": \"R
…[truncated 1660 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2264 · 2026-05-24T03:10:17.305776+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 2265 · 2026-05-24T03:10:17.306092+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2266 · 2026-05-24T03:12:49.235170+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 28 — Active issues\n  # ============================================================\n\n  - id: \"R20-W1\"\n    summary: \"Per-layer KL decomposition 的 train-inference mismatch confound 未解决\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 20\n    last_seen_round: 28\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Critical。K=4 single-seed。\"}\n      - {round: 22, reviewers: [1, 2], note: \"R22 N2。97.5% 精确数字不可靠。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 C1。K=1 有 32× train-inference mismatch。\"}\n      - {round: 25, reviewers: [1, 2], note: \"R25 N1/N2。\"}\n      - {round: 26, reviewers: [1, 2], note: \"R26 R1-N2/R2-N1。建议 stop-gradient 或更多 K 值。\"}\n      - {round: 27, reviewers: [1, 2], note: \"R27 C1。K-curve 6 点中除 K=4 外均 single-seed。K=16 PPL 优势可能 seed-specific。per-layer update count confound 未解决。\"}\n      - {round: 28, reviewers: [1, 2], note: \"R28 双方 AGREE critical。50% 下 K=1 PPL=34.85 vs E2E=11.84（2.94×）是 decisive evidence。K=4 在 50% 更差（44.23）。论文已有 'upper bound' 和 'exploratory' 标注，但 'may account for a substantial portion' 仍被认为对 exploratory analysis 过强。K=2/8/16 3-seed 数据已补充但 per-layer update count confound 仍未解决。\"}\n    action_items:\n      - {round: 21, action: \"K=4 3-seed\", assigned_to: \"main_agent\", status: done}\n      - {round: 22, action: \"定性 'majority of PPL gap'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"限定 decomposition 为 moderate sparsity\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"K=2/K=8/K=16 实验扩展 K-curve\", assigned_to: \"main_agent\", status: done}\n      - {round: 27, action: \"§4.5 降级为 Exploratory Decomposition + may account for a substantial portion\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"experiments L161 'primary design lever' → 'major factor for PPL'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"appendix L647 加 'for PPL at this sparsity level (preliminary)'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"K=2/8/16 各补 s123/s456 3-seed\", assigned_to: \"main_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-N2\"\n    summary: \"MMLU/GSM8K 跨架构系统性退步缺乏机制分析\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 18\n    last_seen_round: 28\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Critical。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 C2。\"}\n      - {round: 25, reviewers: [1, 2], note: \"R25 最高优先级。\"}\n      - {round: 26, reviewers: [1, 2], note: \"R26 R1-N1/R2-N2。\"}\n      - {round: 27, reviewers: [1, 2], note: \"R27 C3。C4 控制 1 seed 不够。KL uniform vs TEAL uniform MMLU 差 5pp（同 allocation）归因未分析。跨 scale 退步暗示根本限制但无缓解路径。\"}\n      - {round: 28, reviewers: [1, 2], note: \"R28 双方 AGREE critical。C4 控制排除训练数据偏差但 mode-covering 假设无直接验证。Constraint analysis（remove valley → MMLU +3.4pp）说明 allocation pattern 影响而非 mode-covering 机制。论文未追问为何退步是 structural。缺 hybrid loss 等缓解方向讨论。\"}\n    action_items:\n      - {round: 21, action: \"Constraint 实验\", assigned_to: \"main_agent\", status: done}\n      - {round: 25, action: \"C4 控制实验\", assigned_to: \"main_agent\", status: done}\n      - {round: 26, action: \"C4 结果写入 §4.2 + Appendix U\", assigned_to: \"paper_agent\", status: done}\n      - {round: 26, action: \"Conclusion 'primary design dimension' 限定\", assigned_to: \"paper_agent\", status: done}\n      - {round: 26, action: \"Abstract 量化知识退步\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W2\"\n    summary: \"高方差下游指标统计可靠性不足\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 24\n    last_seen_round: 28\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"ARC-c 95% CI ≈ ±8.9pp。\"}\n      - {round: 25, reviewers: [1, 2], note: \"Qwen-14B GSM8K std=5.2pp。\"}\n      - {round: 27, reviewers: [1, 2], note: \"R27 W1。30% Global MMLU σ=9.5pp，n=3 CI ≈ ±23.6pp。Abstract/Conclusion 措辞未带 directional 限定。\"}\n      - {round: 28, reviewers: [1, 2], note: \"R28 双方 AGREE critical。Abstract 已改 'directional commonsense gains (n=3)'，但 KL global MMLU 35.7±9.5 的 95% CI ≈ [22.1, 49.3]，任何基于此的比较无统计意义。Qwen-14B GSM8K CV=16.3%。论文在 §4.2 承认 CI overlap 但 abstract/conclusion 仍报告具体 gap 数值。R2 指出 ≥5 seeds 在 14B 有计算限制，应 upfront disclosure。\"}\n    action_items:\n      - {round: 24, action: \"正文加 CI overlap caveat\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"Qwen GSM8K 用 mean±std\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"Abstract 'directional commonsense gains (n=3)'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"Conclusion 'directional downstream gains'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"Introduction 'robust' → 'directional'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"experiments 'outperforms' → 'directional improvements'\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R27-C2\"\n    summary: \"'Primary design dimension' claim 在知识任务不成立\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 24\n    last_seen_round: 28\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"建议软化。\"}\n      - {round: 26, reviewers: [1, 2], note: \"限定为 PPL+commonsense。\"}\n      - {round: 27, reviewers: [1, 2], note: \"R27 C2。TEAL MMLU 45.86 vs KL 40.7 同 uniform allocation。claim 仅在 PPL+commonsense 成立。\"}\n      - {round: 28, reviewers: [1, 2], note: \"R28 本轮未作为独立 issue 提出。Conclusion 已限定 scope。但 R2 指出 Conclusion 仅 2 句话未充分讨论 scope limitation。\"}\n    action_items:\n      - {round: 27, action: \"Conclusion 加 'for perplexity and commonsense at moderate sparsity'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"experiments L161 限定 scope\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"appendix L647 限定 scope\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W3\"\n    summary: \"C1 ablation soft→hard mask representation 残余 confound\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 24\n    last_seen_round: 28\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"Oracle 二值化丢失排序信息。\"}\n      - {round: 27, reviewers: [1, 2], note: \"R27 W2。BCE+Gumbel vs BCE 差 15%。但 R2 指出核心发现仍成立。\"}\n      - {round: 28, reviewers: [1, 2], note: \"R28 双方 AGREE。s42 non-seed-matched + BCE+Gumbel (32.22) 比 BCE (27.97) 更差说明 Gumbel 对 BCE 有害。s123/s456 seed-matched ≤1.18pp 部分缓解。\"}\n    action_items:\n      - {round: 24, action: \"讨论 oracle 信息损失\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"正文 binarization confound caveat\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R25-N1\"\n    summary: \"方法新颖性边界需更清晰论证\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 28\n    mentions:\n      - {round: 25, reviewers: [2], note: \"核心组件均成熟技术。\"}\n      - {round: 26, reviewers: [2], note: \"MaskLLM 共享核心 recipe。\"}\n      - {round: 27, reviewers: [1, 2], note: \"R27 共识：新颖性为组合级别。\"}\n      - {round: 28, reviewers: [2], note: \"R28 R2 维持 critical（MaskLLM 共享 recipe-level 原则，contextual vs static 区别缺实验验证）。R1 REBUT（不同范式，直接对比不合理）。分歧未解决。\"}\n    action_items:\n      - {round: 25, action: \"Intro contribution list 重排\", assigned_to: \"paper_agent\", status: done}\n      - {round: 26, action: \"Table 1 加入 MaskLLM\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"Contribution items 加 Empirical/Practical 标签\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R28-W1\"\n    summary: \"Conclusion 仅 2 句话，缺 broader impact 和 future directions\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 28\n    last_seen_round: 28\n    mentions:\n      - {round: 28, reviewers: [1, 2], note: \"R28 双方 AGREE。2 句话未讨论 knowledge regression implications、future directions（如 hybrid loss）、broader impact。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R28-W2\"\n    summary: \"Contribution C3/C4 标注 'Practical' 在无 wall-clock 加速下有误导性\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 28\n    last_seen_round: 28\n    mentions:\n      - {round: 28, reviewers: [1, 2], note: \"R28 R2 列为 critical，R1 AGREE 但认为 should-fix。Predictor +6.4% latency，无 sparse kernel 支持。论文已多处声明无加速，但 contribution 标签 misleading。建议改为 Analytical/Empirical。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R26-W1\"\n    summary: \"14.5% PPL improvement 引用基准在 Abstract 与 Table 2 不一致\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 26\n    last_seen_round: 28\n    mentions:\n      - {round: 26, reviewers: [1, 2], note: \"Abstract 用 matched-sparsity，Table 2 找不到 10.30。\"}\n      - {round: 27, reviewers: [1, 2], note: \"R27 Detailed Comments: 14.5% 引用基准在 Table 2 中找不到。\"}\n      - {round: 28, reviewers: [], note: \"R28 本轮未被任何 Reviewer 提及，可能已通过 Table 2 caption 的 ‡ 标注解决，待 Research Director 确认。\"}\n    action_items:\n      - {round: 26, action: \"Table 2 caption 标注 matched-sparsity 来源\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 28 — New should-fix issues\n  # ============================================================\n\n  - id: \"R28-W3\"\n    summary: \"MSE 50% baseline 仅 s42 有效（s123 catastrophic PPL=15,789），作为 baseline 不可信\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 28\n    last_seen_round: 28\n    mentions:\n      - {round: 28, reviewers: [1, 2], note: \"R28 双方 AGREE。2/3 seed 失败说明 MSE 在 50% 下不稳定。Table 4 已有 § 标注但仍在主表中。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R28-W4\"\n    summary: \"30% 下缺少 BCE isocompute (2700 steps) 对比\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 28\n    last_seen_round: 28\n    mentions:\n      - {round: 28, reviewers: [1, 2], note: \"R28 双方 AGREE。BCE isocompute 仅在 50% 下有 3-seed。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R28-W5\"\n    summary: \"主评估指标单一（WikiText-2 PPL），C4 OOD 不充分\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 28\n    last_seen_round: 28\n    mentions:\n      - {round: 28, reviewers: [1, 2], note: \"R28 R1 列为 W5，R2 AGREE。WikiText-2 与 WikiText-103 同源。C4 OOD 30% 仅 2-seed。Uniform 3-seed CV=6.3% vs in-domain 0.2%。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Resolved (older rounds, carried forward)\n  # ============================================================\n\n  - id: \"R25-W1\"\n    summary: \"BCE 30% uniform 对比已补充\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 25\n    last_seen_round: 26\n    resolution: \"Table 2 已加 BCE 30% uniform (PPL=15.09±0.13, 3-seed)。\"\n    resolution_round: 27\n\n  - id: \"R25-M1\"\n    summary: \"术语不一致\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 25\n    last_seen_round: 27\n    resolution: \"全文统一为 output-distribution KL。Reviewer 验证 PASS。\"\n    resolution_round: 27\n\n  - id: \"R27-W4\"\n    summary: \"Contribution framing 存在 empirical study vs method 张力\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 27\n    last_seen_round: 27\n    resolution: \"4 个 contribution items 加 Empirical/Practical 标签。Reviewer 验证 PASS。\"\n    resolution_round: 27\n\n  - id: \"R27-W5\"\n    summary: \"Wall-clock speedup 缺失\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 28\n    mentions:\n      - {round: 28, reviewers: [1, 2], note: \"R28 R2 将其与 'Practical' 标签合并为新 issue R28-W2。论文已充分 framed 为 empirical study。\"}\n    resolution: \"结构性限制。论文已充分 framed 为 empirical study。多轮维持 resolved。\"\n    resolution_round: 23\n\n  - id: \"R25-W2\"\n    summary: \"MSE 50% baseline 仅 seed 42 有效\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 25\n    last_seen_round: 28\n    mentions:\n      - {round: 28, reviewers: [1, 2], note: \"R28 升级为新 issue R28-W3（不可信 baseline）。\"}\n    resolution: \"Table 3 caption 有 § 标注，method.tex 有 '(50%: s42 only)'。但 R28 认为不够，升级为 R28-W3。\"\n    resolution_round: 27\n\n  - id: \"R26-M3\"\n    summary: \"68% divergence 和 32% Jaccard 同句混淆\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 26\n    last_seen_round: 27\n    resolution: \"Introduction 统一使用 Jaccard distance。Reviewer 验证 PASS。\"\n    resolution_round: 27\n\n  - id: \"R19-N3\"\n    summary: \"无实际 wall-clock 加速\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 27\n    resolution: \"论文已充分 framed 为 empirical study。\"\n    resolution_round: 23\n\n  - id: \"R24-W1\"\n    summary: \"评估覆盖度关键空白\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 26\n    resolution: \"Limitations 已覆盖。Base model 不适用生成评估。\"\n    resolution_round: 25\n\n  - id: \"R24-W4\"\n    summary: \"'Primary design dimension' 需限定\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 27\n    resolution: \"合并入 R27-C2。Conclusion 已限定为 'for perplexity and commonsense at moderate sparsity'。\"\n    resolution_round: 27\n\n  - id: \"R22-W6\"\n    summary: \"Figure 2 仅展示 global allocation\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 26\n    resolution: \"R26/R27 未再提出。\"\n    resolution_round: 27\n\n  - id: \"R19-W1\"\n    summary: \"与 MaskLLM 新颖性区分\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 26\n    resolution: \"合并进 R25-N1。\"\n    resolution_round: 25\n\n  - id: \"R20-W4\"\n    summary: \"WikiText 同分布评估 + C4 OOD\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 26\n    resolution: \"Appendix D OOD 证据充分。\"\n    resolution_round: 25\n\n  - id: \"R22-W3\"\n    summary: \"Table 2 sparsity mismatch 脚注\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 26\n    resolution: \"§4.1 matched 14.5% 独立句。\"\n    resolution_round: 23\n\n  - id: \"R22-W5\"\n    summary: \"规模泛化仅 7-14B\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 27\n    resolution: \"Limitations 已覆盖。\"\n    resolution_round: 25\n\n  - id: \"R25-W3\"\n    summary: \"Introduction 19% 已修正为 14.5%\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 25\n    last_seen_round: 26\n    resolution: \"数值已修正。\"\n    resolution_round: 26\n\n  - id: \"R25-M2\"\n    summary: \"Eq. 4 s_j 缺层标\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 25\n    last_seen_round: 25\n    resolution: \"已补充。\"\n    resolution_round: 25\n\n  - id: \"R19-N2\"\n    summary: \"C1 target-swap 因果声明\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 24\n    resolution: \"C1 claim 已降级为 transferability。\"\n    resolution_round: 23\n\n  - id: \"R22-W7\"\n    summary: \"Abstract 信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"已拆分。\"\n    resolution_round: 23\n\n  - id: \"R22-W8\"\n    summary: \"Conclusion 引用 BoolQ\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"BoolQ → HellaSwag/PIQA。\"\n    resolution_round: 23\n\n  - id: \"R19-W7\"\n    summary: \"30% sparsity sweet spot\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 26\n    resolution: \"Limitations 已覆盖。\"\n    resolution_round: 25\n\n  - id: \"R15-N3\"\n    summary: \"MaskLLM 新颖性边界\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 26\n    resolution: \"合并进 R25-N1。\"\n    resolution_round: 23\n\n  - id: \"R26-M1\"\n    summary: \"Introduction 中 8.6%/6.4% 未标注 sparsity level\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 26\n    last_seen_round: 26\n    resolution: \"§4.3 已加 sparsity level 标注。\"\n    resolution_round: 26\n\n  - id: \"R26-M2\"\n    summary: \"'stable downstream' 措辞\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 26\n    last_seen_round: 26\n    resolution: \"Introduction 已删除 'stable'。\"\n    resolution_round: 26"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 28 — Active issues\n  # ============================================================\n\n  - id: \"R20-W1\"\n    summary: \"Per-layer KL decomposition 的 train-inference mismatch confound 未解决\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 20\n    last_seen_round: 28\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Critical。K=4 single-seed。\"}\n      - {round: 22, reviewers: [1, 2], note: \"R22 N2。97.5% 精确数字不可靠。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 C1。K=1 有 32× train-inference mismatch。\"}\n      - {round: 25, reviewers: [1, 2], note: \"R25 N1/N2。\"}\n      - {round: 26, reviewers: [1, 2], note: \"R26 R1-N2/R2-N1。建议 stop-gradient 或更多 K 值。\"}\n      - {round: 27, reviewers: [1, 2], note: \"R27 C1。K-curve 6 点中除 K=4 外均 single-seed。K=16 PPL 优势可能 seed-specific。per-layer update count confound 未解决。\"}\n      - {round: 28, reviewers: [1, 2], note: \"R28 双方 AGREE critical。50% 下 K=1 PPL=34.85 vs E2E=11.84（2.94×）是 decisive evidence。K=4 在 50% 更差（44.23）。论文已有 'upper bound' 和 'exploratory' 标注，但 'may account for a substantial portion' 仍被认为对 exploratory analysis 过强。K=2/8/16 3-seed 数据已补充但 per-layer update count confound 仍未解决。\"}\n    action_items:\n      - {round: 21, action: \"K=4 3-seed\", assigned_to: \"main_agent\", status: done}\n      - {round: 22, action: \"定性 'majority of PPL gap'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"限定 decomposition 为 moderate sparsity\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"K=2/K=8/K=16 实验扩展 K-curve\", assigned_to: \"main_agent\", status: done}\n      - {round: 27, action: \"§4.5 降级为 Exploratory Decomposition + may account for a substantial portion\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"experiments L161 'primary design lever' → 'major factor for PPL'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"appendix L647 加 'for PPL at this sparsity level (preliminary)'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"K=2/8/16 各补 s123/s456 3-seed\", assigned_to: \"main_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-N2\"\n    summary: \"MMLU/GSM8K 跨架构系统性退步缺乏机制分析\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 18\n    last_seen_round: 28\n    mentions:\n      - {round: 21, reviewers: [1, 2], note: \"R21 Critical。\"}\n      - {round: 24, reviewers: [1, 2], note: \"R24 C2。\"}\n      - {round: 25, reviewers: [1, 2], note: \"R25 最高优先级。\"}\n      - {round: 26, reviewers: [1, 2], note: \"R26 R1-N1/R2-N2。\"}\n      - {round: 27, reviewers: [1, 2], note: \"R27 C3。C4 控制 1 seed 不够。KL uniform vs TEAL uniform MMLU 差 5pp（同 allocation）归因未分析。跨 scale 退步暗示根本限制但无缓解路径。\"}\n      - {round: 28, reviewers: [1, 2], note: \"R28 双方 AGREE critical。C4 控制排除训练数据偏差但 mode-covering 假设无直接验证。Constraint analysis（remove valley → MMLU +3.4pp）说明 allocation pattern 影响而非 mode-covering 机制。论文未追问为何退步是 structural。缺 hybrid loss 等缓解方向讨论。\"}\n    action_items:\n      - {round: 21, action: \"Constraint 实验\", assigned_to: \"main_agent\", status: done}\n      - {round: 25, action: \"C4 控制实验\", assigned_to: \"main_agent\", status: done}\n      - {round: 26, action: \"C4 结果写入 §4.2 + Appendix U\", assigned_to: \"paper_agent\", status: done}\n      - {round: 26, action: \"Conclusion 'primary design dimension' 限定\", assigned_to: \"paper_agent\", status: done}\n      - {round: 26, action: \"Abstract 量化知识退步\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W2\"\n    summary: \"高方差下游指标统计可靠性不足\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 24\n    last_seen_round: 28\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"ARC-c 95% CI ≈ ±8.9pp。\"}\n      - {round: 25, reviewers: [1, 2], note: \"Qwen-14B GSM8K std=5.2pp。\"}\n      - {round: 27, reviewers: [1, 2], note: \"R27 W1。30% Global MMLU σ=9.5pp，n=3 CI ≈ ±23.6pp。Abstract/Conclusion 措辞未带 directional 限定。\"}\n      - {round: 28, reviewers: [1, 2], note: \"R28 双方 AGREE critical。Abstract 已改 'directional commonsense gains (n=3)'，但 KL global MMLU 35.7±9.5 的 95% CI ≈ [22.1, 49.3]，任何基于此的比较无统计意义。Qwen-14B GSM8K CV=16.3%。论文在 §4.2 承认 CI overlap 但 abstract/conclusion 仍报告具体 gap 数值。R2 指出 ≥5 seeds 在 14B 有计算限制，应 upfront disclosure。\"}\n    action_items:\n      - {round: 24, action: \"正文加 CI overlap caveat\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"Qwen GSM8K 用 mean±std\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"Abstract 'directional commonsense gains (n=3)'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"Conclusion 'directional downstream gains'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"Introduction 'robust' → 'directional'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"experiments 'outperforms' → 'directional improvements'\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R27-C2\"\n    summary: \"'Primary design dimension' claim 在知识任务不成立\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 24\n    last_seen_round: 28\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"建议软化。\"}\n      - {round: 26, reviewers: [1, 2], note: \"限定为 PPL+commonsense。\"}\n      - {round: 27, reviewers: [1, 2], note: \"R27 C2。TEAL MMLU 45.86 vs KL 40.7 同 uniform allocation。claim 仅在 PPL+commonsense 成立。\"}\n      - {round: 28, reviewers: [1, 2], note: \"R28 本轮未作为独立 issue 提出。Conclusion 已限定 scope。但 R2 指出 Conclusion 仅 2 句话未充分讨论 scope limitation。\"}\n    action_items:\n      - {round: 27, action: \"Conclusion 加 'for perplexity and commonsense at moderate sparsity'\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"experiments L161 限定 scope\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"appendix L647 限定 scope\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W3\"\n    summary: \"C1 ablation soft→hard mask representation 残余 confound\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 24\n    last_seen_round: 28\n    mentions:\n      - {round: 24, reviewers: [1, 2], note: \"Oracle 二值化丢失排序信息。\"}\n      - {round: 27, reviewers: [1, 2], note: \"R27 W2。BCE+Gumbel vs BCE 差 15%。但 R2 指出核心发现仍成立。\"}\n      - {round: 28, reviewers: [1, 2], note: \"R28 双方 AGREE。s42 non-seed-matched + BCE+Gumbel (32.22) 比 BCE (27.97) 更差说明 Gumbel 对 BCE 有害。s123/s456 seed-matched ≤1.18pp 部分缓解。\"}\n    action_items:\n      - {round: 24, action: \"讨论 oracle 信息损失\", assigned_to: \"paper_agent\", status: done}\n      - {round: 25, action: \"正文 binarization confound caveat\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R25-N1\"\n    summary: \"方法新颖性边界需更清晰论证\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 28\n    mentions:\n      - {round: 25, reviewers: [2], note: \"核心组件均成熟技术。\"}\n      - {round: 26, reviewers: [2], note: \"MaskLLM 共享核心 recipe。\"}\n      - {round: 27, reviewers: [1, 2], note: \"R27 共识：新颖性为组合级别。\"}\n      - {round: 28, reviewers: [2], note: \"R28 R2 维持 critical（MaskLLM 共享 recipe-level 原则，contextual vs static 区别缺实验验证）。R1 REBUT（不同范式，直接对比不合理）。分歧未解决。\"}\n    action_items:\n      - {round: 25, action: \"Intro contribution list 重排\", assigned_to: \"paper_agent\", status: done}\n      - {round: 26, action: \"Table 1 加入 MaskLLM\", assigned_to: \"paper_agent\", status: done}\n      - {round: 27, action: \"Contribution items 加 Empirical/Practical 标签\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R28-W1\"\n    summary: \"Conclusion 仅 2 句话，缺 broader impact 和 future directions\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 28\n    last_seen_round: 28\n    mentions:\n      - {round: 28, reviewers: [1, 2], note: \"R28 双方 AGREE。2 句话未讨论 knowledge regression implications、future directions（如 hybrid loss）、broader impact。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R28-W2\"\n    summary: \"Contribution C3/C4 标注 'Practical' 在无 wall-clock 加速下有误导性\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 28\n    last_seen_round: 28\n    mentions:\n      - {round: 28, reviewers: [1, 2], note: \"R28 R2 列为 critical，R1 AGREE 但认为 should-fix。Predictor +6.4% latency，无 sparse kernel 支持。论文已多处声明无加速，但 contribution 标签 misleading。建议改为 Analytical/Empirical。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R26-W1\"\n    summary: \"14.5% PPL improvement 引用基准在 Abstract 与 Table 2 不一致\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 26\n    last_seen_round: 28\n    mentions:\n      - {round: 26, reviewers: [1, 2], note: \"Abstract 用 matched-sparsity，Table 2 找不到 10.30。\"}\n      - {round: 27, reviewers: [1, 2], note: \"R27 Detailed Comments: 14.5% 引用基准在 Table 2 中找不到。\"}\n      - {round: 28, reviewers: [], note: \"R28 本轮未被任何 Reviewer 提及，可能已通过 Table 2 caption 的 ‡ 标注解决，待 Research Director 确认。\"}\n    action_items:\n      - {round: 26, action: \"Table 2 caption 标注 matched-sparsity 来源\", assigned_to: \"paper_agent\", status: done}\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 28 — New should-fix issues\n  # ============================================================\n\n  - id: \"R28-W3\"\n    summary: \"MSE 50% baseline 仅 s42 有效（s123 catastrophic PPL=15,789），作为 baseline 不可信\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 28\n    last_seen_round: 28\n    mentions:\n      - {round: 28, reviewers: [1, 2], note: \"R28 双方 AGREE。2/3 seed 失败说明 MSE 在 50% 下不稳定。Table 4 已有 § 标注但仍在主表中。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R28-W4\"\n    summary: \"30% 下缺少 BCE isocompute (2700 steps) 对比\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 28\n    last_seen_round: 28\n    mentions:\n      - {round: 28, reviewers: [1, 2], note: \"R28 双方 AGREE。BCE isocompute 仅在 50% 下有 3-seed。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R28-W5\"\n    summary: \"主评估指标单一（WikiText-2 PPL），C4 OOD 不充分\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 28\n    last_seen_round: 28\n    mentions:\n      - {round: 28, reviewers: [1, 2], note: \"R28 R1 列为 W5，R2 AGREE。WikiText-2 与 WikiText-103 同源。C4 OOD 30% 仅 2-seed。Uniform 3-seed CV=6.3% vs in-domain 0.2%。\"}\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Resolved (older rounds, carried forward)\n  # ============================================================\n\n  - id: \"R25-W1\"\n    summary: \"BCE 30% uniform 对比已补充\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 25\n    last_seen_round: 26\n    resolution: \"Table 2 已加 BCE 30% uniform (PPL=15.09±0.13, 3-seed)。\"\n    resolution_round: 27\n\n  - id: \"R25-M1\"\n    summary: \"术语不一致\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 25\n    last_seen_round: 27\n    resolution: \"全文统一为 output-distribution KL。Reviewer 验证 PASS。\"\n    resolution_round: 27\n\n  - id: \"R27-W4\"\n    summary: \"Contribution framing 存在 empirical study vs method 张力\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 27\n    last_seen_round: 27\n    resolution: \"4 个 contribution items 加 Empirical/Practical 标签。Reviewer 验证 PASS。\"\n    resolution_round: 27\n\n  - id: \"R27-W5\"\n    summary: \"Wall-clock speedup 缺失\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 28\n    mentions:\n      - {round: 28, reviewers: [1, 2], note: \"R28 R2 将其与 'Practical' 标签合并为新 issue R28-W2。论文已充分 framed 为 empirical study。\"}\n    resolution: \"结构性限制。论文已充分 framed 为 empirical study。多轮维持 resolved。\"\n    resolution_round: 23\n\n  - id: \"R25-W2\"\n    summary: \"MSE 50% baseline 仅 seed 42 有效\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 25\n    last_seen_round: 28\n    mentions:\n      - {round: 28, reviewers: [1, 2], note: \"R28 升级为新 issue R28-W3（不可信 baseline）。\"}\n    resolution: \"Table 3 caption 有 § 标注，method.tex 有 '(50%: s42 only)'。但 R28 认为不够，升级为 R28-W3。\"\n    resolution_round: 27\n\n  - id: \"R26-M3\"\n    summary: \"68% divergence 和 32% Jaccard 同句混淆\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 26\n    last_seen_round: 27\n    resolution: \"Introduction 统一使用 Jaccard distance。Reviewer 验证 PASS。\"\n    resolution_round: 27\n\n  - id: \"R19-N3\"\n    summary: \"无实际 wall-clock 加速\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 27\n    resolution: \"论文已充分 framed 为 empirical study。\"\n    resolution_round: 23\n\n  - id: \"R24-W1\"\n    summary: \"评估覆盖度关键空白\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 26\n    resolution: \"Limitations 已覆盖。Base model 不适用生成评估。\"\n    resolution_round: 25\n\n  - id: \"R24-W4\"\n    summary: \"'Primary design dimension' 需限定\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 27\n    resolution: \"合并入 R27-C2。Conclusion 已限定为 'for perplexity and commonsense at moderate sparsity'。\"\n    resolution_round: 27\n\n  - id: \"R22-W6\"\n    summary: \"Figure 2 仅展示 global allocation\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 26\n    resolution: \"R26/R27 未再提出。\"\n    resolution_round: 27\n\n  - id: \"R19-W1\"\n    summary: \"与 MaskLLM 新颖性区分\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 26\n    resolution: \"合并进 R25-N1。\"\n    resolution_round: 25\n\n  - id: \"R20-W4\"\n    summary: \"WikiText 同分布评估 + C4 OOD\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 26\n    resolution: \"Appendix D OOD 证据充分。\"\n    resolution_round: 25\n\n  - id: \"R22-W3\"\n    summary: \"Table 2 sparsity mismatch 脚注\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 26\n    resolution: \"§4.1 matched 14.5% 独立句。\"\n    resolution_round: 23\n\n  - id: \"R22-W5\"\n    summary: \"规模泛化仅 7-14B\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 27\n    resolution: \"Limitations 已覆盖。\"\n    resolution_round: 25\n\n  - id: \"R25-W3\"\n    summary: \"Introduction 19% 已修正为 14.5%\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 25\n    last_seen_round: 26\n    resolution: \"数值已修正。\"\n    resolution_round: 26\n\n  - id: \"R25-M2\"\n    summary: \"Eq. 4 s_j 缺层标\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 25\n    last_seen_round: 25\n    resolution: \"已补充。\"\n    resolution_round: 25\n\n  - id: \"R19-N2\"\n    summary: \"C1 target-swap 因果声明\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 24\n    resolution: \"C1 claim 已降级为 transferability。\"\n    resolution_round: 23\n\n  - id: \"R22-W7\"\n    summary: \"Abstract 信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"已拆分。\"\n    resolution_round: 23\n\n  - id: \"R22-W8\"\n    summary: \"Conclusion 引用 BoolQ\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    resolution: \"BoolQ → HellaSwag/PIQA。\"\n    resolution_round: 23\n\n  - id: \"R19-W7\"\n    summary: \"30% sparsity sweet spot\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 26\n    resolution: \"Limitations 已覆盖。\"\n    resolution_round: 25\n\n  - id: \"R15-N3\"\n    summary: \"MaskLLM 新颖性边界\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 26\n    resolution: \"合并进 R25-N1。\"\n    resolution_round: 23\n\n  - id: \"R26-M1\"\n    summary: \"Introduction 中 8.6%/6.4% 未标注 sparsity level\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 26\n    last_seen_round: 26\n    resolution: \"§4.3 已加 sparsity level 标注。\"\n    resolution_round: 26\n\n  - id: \"R26-M2\"\n    summary: \"'stable downstream' 措辞\"\n    category: writing\n    severity: minor\n    status: resolved\n    first_raised_round: 26\n    last_seen_round: 26\n    resolution: \"Introduction 已删除 'stable'。\"\n    resolution_round: 26"
  }
}
```

</details>

---


### Tool result

_source line 2267 · 2026-05-24T03:12:49.336851+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml\", \"bytes\": 16896}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2268 · 2026-05-24T03:15:35.926916+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 - Findings",
  "report": "# 审稿报告：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n**Target Venue**: EMNLP 2026 (ARR May cycle)  \n**Category**: Long Paper  \n**Review Round**: 28 (fresh)  \n**Reviewers**: R1（方法严谨性 + 实验设计）、R2（新颖性 + 完整性 + 写作质量）\n\n---\n\n## Summary\n\n本文系统对比了 SwiGLU LLM 上下文稀疏性预测器的训练目标。核心方法：用 forward KL divergence 替代传统 BCE，通过 Gumbel-Sigmoid 松弛训练轻量级预测器（75.9M, <1% 参数量）。在 LLaMA-3.1-8B 上 30% 稀疏度下，KL 预测器 PPL 比 TEAL 低 14.5%（8.81±0.02 vs 10.30，matched sparsity），跨架构验证（Mistral-7B -17.3%, Qwen-14B）确认泛化性。target-swap ablation (C1) 显示 KL 发现的 mask 模式可迁移到 BCE（PPL gap ≤0.79pp）。per-layer KL 分解尝试分离 signal type 和 coupling scope 的贡献。但知识密集型任务出现系统性退步（MMLU -5.2pp on 8B, GSM8K -20.1pp on 14B vs TEAL at same sparsity）。论文定位为 empirical study，不提供 wall-clock 加速。\n\n---\n\n## Strengths\n\n**S1** [双方共识] **PPL 改善显著且跨架构一致**。14.5%（30%）到 50%（50%）的 PPL 改善在 LLaMA-8B、Mistral-7B、Qwen-14B 上复现，是一个实质性的经验发现。C4 OOD 评估进一步确认泛化性。\n\n**S2** [双方共识] **实验覆盖面广**。3-seed 评估、5 种 loss variants（forward KL/reverse KL/JSD/BCE/MSE）、3 种架构（7B-14B）、2 种稀疏度、多种 allocation 策略、isocompute 对比。对于 empirical study 来说覆盖面高于多数同类工作。\n\n**S3** [双方共识] **C1 target-swap ablation 有独立 insight 价值**。证明 KL 发现的 mask patterns（而非 gradient coupling 本身）是 PPL 优势的主要来源，为后续工作提供了 \"先用 KL 找 mask，再用 BCE 训练\" 的实用路径。\n\n**S4** [双方共识] **诚实报告负面结果**。MMLU/GSM8K 回退、per-layer 分解的局限性、MSE 50% 的 catastrophic failure 等均如实报告。对 claim 的 hedging（\"directional\", \"upper bound\", \"exploratory\"）比多数论文更透明。\n\n**S5** [双方共识] **可复现性良好**。训练细节充分（lr, schedule, GPU, batch size, steps, exp_id），承诺代码开源。Taxonomy（Table 1）提供了该领域的清晰组织框架。\n\n**S6** [R1] **补偿网络冗余性发现有工程简化价值**。KL 预测器在两个稀疏度下均使 FastForward-style compensation (+67.2M) 冗余，减少推理开销。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1** [双方共识, critical] **Per-layer KL 分解存在根本性 train-inference mismatch，核心 decomposition claim 站不住脚**\n\nK=1 per-layer KL 训练时每步只 mask 1/32 层，推理时 32 层同时 mask——这是无法通过实验设计消除的根本性 mismatch。K=1 (PPL 9.05) 与 E2E (8.81) 的 2.7% gap 被论文解读为 \"signal type accounts for a substantial portion of PPL gap\"，但此 gap 之所以小是因为 K=1 训练条件近似 dense（31/32 层完整）。\n\n决定性证据：50% 下 K=1 PPL=34.85 vs E2E=11.84（2.94×），mismatch 灾难性放大；K=4 在 50% 更差（44.23 vs K=1 的 34.85），论文自己承认 \"the decomposition is interpretable only at 30%\"（§4.5）。K-curve 非单调（K=2 最差 10.75, K=16 最优 8.67），说明层间交互有复杂非线性效应。\n\n论文已做了多项改进（标注 \"upper bound\"、\"exploratory\"、补充 K=2/8/16 3-seed K-curve），但 \"may account for a substantial portion\" 的措辞对于 admittedly exploratory 且仅在 30% 有效的分析仍然过强。per-layer update count confound（K=2 ~62 updates/layer vs K=8 ~250）也未解决。\n\n*[跨轮追踪: R20-W1, 连续 9 轮被标记]*\n\n**C2** [双方共识, critical] **下游知识任务（MMLU/GSM8K）系统性退步缺乏机制性解释**\n\nKL 在所有模型/规模上系统性损害 MMLU 和 GSM8K：\n- LLaMA-8B 30%: MMLU 40.7±1.3 vs TEAL 45.86（同 uniform allocation, -5.2pp）\n- Qwen-14B 30%: GSM8K 32.0±5.2 vs TEAL 52.1（-20.1pp）\n- Mistral-7B: MMLU tied, GSM8K reverses\n\n论文排除了训练数据偏差（C4 控制），提出 forward KL mode-covering 稀释稀有激活假设，但无直接验证（如分析 KL mask 是否 prune 了 factual neurons）。Constraint analysis（remove valley → MMLU +3.4pp）说明 allocation pattern 有影响但非 mechanism 解释。跨 scale 退步暗示 structural limitation 但论文未追问 *why*。\n\n对于声称改善稀疏预测质量的论文，PPL 改善与 downstream 退步的矛盾是核心张力。缺乏缓解方向讨论（如 hybrid loss、task-aware allocation）。\n\n*[跨轮追踪: R20-N2, 连续 11 轮被标记]*\n\n**C3** [双方共识, critical] **n=3 下 downstream metrics 统计功效严重不足**\n\n- KL global 30% MMLU: 35.7±9.5pp (n=3)，95% CI ≈ [22.1, 49.3]——覆盖从 random chance 到 dense 的大部分范围\n- Qwen-14B GSM8K: 32.0±5.2pp (n=3)，CV=16.3%\n- TEAL 是 deterministic single-run，无方差信息，与 KL 的 CI 直接对比不对等\n\n论文在 §4.2 承认 \"95% CI for individual downstream tasks overlap\"，在 abstract 已改用 \"directional commonsense gains (n=3)\"，但 conclusion 和 abstract 中仍报告具体的 gap 数值（-5.2pp, -20.1pp）作为确定性结论。增加 seed 数至 ≥5（或至少 upfront disclosure 14B 的计算预算限制）是必要的。\n\n*[跨轮追踪: R24-W2, 连续 5 轮被标记]*\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [双方共识] **C1 target-swap ablation confound 未充分控制**。s42 oracle 来自 non-seed-matched earlier training run；BCE+Gumbel (32.22) vs BCE (27.97) 显示 Gumbel 对 BCE 有害，使 C1 的 \"target quality vs gradient coupling\" 分离不够干净。s123/s456 seed-matched ≤1.18pp 部分缓解。\n\n**W2** [双方共识] **MSE 50% baseline 不可信**。s123 仅达 5.1% sparsity（PPL=15,789），2/3 seed 失败。Table 4 虽有 § 标注但仍在主表中，有误导性。\n\n**W3** [双方共识] **30% 下缺少 BCE isocompute (2700 steps) 对比**。BCE isocompute 仅在 50% 有 3-seed，无法确认 30% 下 KL 对 BCE 的优势在更多训练步数后是否缩小。\n\n**W4** [双方共识] **主评估指标单一**。所有主要比较基于 WikiText-2 PPL（与训练数据 WikiText-103 同源）。C4 OOD 30% 仅 2-seed，uniform 3-seed CV=6.3% vs in-domain 0.2%。\n\n**W5** [双方共识] **Conclusion 仅 2 句话**。对于涉及复杂 trade-off（PPL vs downstream, signal type vs coupling, commonsense vs knowledge）的论文，缺乏 broader implications、future directions、knowledge regression 解决方向的讨论。\n\n**W6** [R2, R1 partial agree] **Contribution C3/C4 标注 \"Practical\" 在无 wall-clock 加速下有误导性**。Predictor +6.4% latency，无 sparse kernel 支持。论文已多处声明无加速，但 contribution 标签应改为 \"Analytical\" 或 \"Empirical\"。\n\n**W7** [R2, R1 partial agree] **训练规模极小（1000 步, ~8.2M tokens）**。虽然 convergence analysis 显示 step 800 后饱和、isocompute 分析支持 KL 优势非因训练不足，但更大规模下相对优势是否保持未验证。\n\n---\n\n## Reviewer Consensus\n\n以下问题双方达成完全共识（标注 [AGREE]）：\n\n1. [AGREE] Per-layer KL 分解的 train-inference mismatch 是根本性问题，仅在 30% 下 \"interpretable\"，50% 下完全失效\n2. [AGREE] 知识任务退步是系统性的且缺乏机制性解释，C4 控制排除数据偏差后问题更 structural\n3. [AGREE] n=3 统计功效不足，高方差下游指标的 CI overlap 使多数比较无统计意义\n4. [AGREE] PPL 改善显著且一致，是论文的核心实质性贡献\n5. [AGREE] C1 target-swap ablation 有 insight 价值但存在残余 confound（soft→hard binarization, non-seed-matched oracle）\n6. [AGREE] Conclusion 过短，缺 future directions\n7. [AGREE] Overall 3.0 (Findings)\n\n---\n\n## Reviewer Divergence\n\n以下问题存在分歧（均为严重程度分歧，非方向性分歧）：\n\n1. **MaskLLM novelty 区分**\n   - R2: Critical。MaskLLM 共享 recipe-level principle，contextual vs static 区别缺实验验证，\"KL > BCE\" 符合信息论直觉不够 surprising\n   - R1: Not critical。MaskLLM 是 static N:M sparsity，与 contextual unstructured 是不同范式，要求跨范式直接对比不合理\n   - **Director 判断**: Should-fix。R1 关于不同范式的论点成立——直接实验对比不可行。但 R2 关于 insight novelty 的质疑也合理——论文应更清晰地阐述为什么 contextual 下的 KL 行为可能与 static 下 qualitatively 不同\n\n2. **无 wall-clock 加速的严重程度**\n   - R2: Critical。+6.4% latency 且 \"Practical\" 标签 misleading\n   - R1: Should-fix。论文已充分 disclaimer，这是 empirical study 不是 systems paper\n   - **Director 判断**: Should-fix。论文的 self-positioning 已足够清晰，但 \"Practical\" 标签确实应修改\n\n3. **Excitement 评分**\n   - R1: 3/5（C1 ablation 和广覆盖面有价值）\n   - R2: 2.5/5（核心发现 expected，无实际加速，退步限制启发性）\n   - **Director 判断**: 2.5-3/5。PPL 改善本身 expected，但 mask divergence pattern 和 C1 transferability 有 non-trivial insight\n\n---\n\n## Questions\n\n1. TEAL uniform 30% MMLU 45.86 显著高于 KL 40.7±1.3。对实际部署，TEAL 在 knowledge-critical 场景是否更优？论文应明确 use-case dependent recommendation。\n2. C4-trained predictor PPL 更差（11.55 vs 8.82）但 downstream 基本不变（MMLU 40.0% vs 40.7%）——这是否表明 WikiText-103 的文本特性有助于学习更好的稀疏 pattern？\n3. 20-25% sparsity 下 downstream gap 是否更小？Figure 3 显示此区间 PPL gap 收窄。\n4. ShadowLLM 在 Table 1 归入 \"Per-token × Intermediate (MSE)\" 但其使用 attention-based routing——分类是否准确？\n5. Per-layer KL 的 per-layer update count confound（K=2 ~62/layer vs K=8 ~250/layer）是否可以通过 epoch-normalized training 控制？\n\n---\n\n## Missing References\n\n**双方共识遗漏**：\n- ActTail (2026, arXiv:2603.12272)：基于 Heavy-Tailed Self-Regularization 的全局激活稀疏性分配\n- WiSparse (2026, arXiv:2602.14452)：Weight-Aware Mixed Activation Sparsity\n\n**R1 建议、R2 反驳**（weight pruning 方法，与 activation sparsity prediction 相关性有限）：\n- LoRAShear, ZipLM\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置，不适用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 2 warning, 22 info）。\n\n**Warnings**：\n1. Abstract 视觉长度偏长，可能接近 200 words 上限（实测 ~190 words，合规）\n2. Page 7 三张表格（Table 2/3/4）集中在同一页，视觉密度偏高\n\n**格式合规**：\n- 正文 8 页 ✓\n- Limitations 在正文（page 9）✓\n- 匿名（\"Anonymous ACL submission\"）✓\n- 引用格式 ACL natbib ✓\n- 无 margin 溢出 ✓\n- Display items 密度 0.88/页，正常 ✓\n\n---\n\n## Overall Assessment\n\n**Overall**: 3.0 (Findings)\n\n**置信度**: 4/5（双方 Reviewer 均 4/5，核心问题高度共识）\n\n### 维度汇总\n\n| 维度 | R1 | R2 | 合议 |\n|------|-----|-----|------|\n| Soundness | 3/5 | 3.5/5 | 3/5 |\n| Excitement | 3/5 | 2.5/5 | 2.5/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Overall | 3.0 | 3.0 | 3.0 |\n\n### 理由\n\n本文做出了一个有价值的经验贡献：系统证明 output-distribution KL 在稀疏预测器的 PPL 表现上显著优于 BCE/MSE，且 KL 发现的 mask 模式可迁移（C1）。实验覆盖面广，报告透明诚实。\n\n三个 critical 问题阻止主会议推荐：\n\n**(1) 核心分析贡献（per-layer KL decomposition）方法学缺陷**。该分解存在无法消除的 train-inference mismatch（1/32 vs 32/32 layers masked），仅在 30% 有效且是 upper bound。如果去掉这个 decomposition contribution，论文退化为 \"KL 在 PPL 上更好但 downstream 更差\" 的实验报告。\n\n**(2) 知识任务系统性退步未解决**。MMLU/GSM8K 在所有模型/规模上退步，C4 控制排除了数据偏差但 mode-covering 假设无直接验证。对于声称改善稀疏预测质量的论文，这构成核心方法有效性的质疑——PPL 改善未转化为 deployment-relevant metrics 的提升。\n\n**(3) 统计功效不足**。n=3 下高方差 downstream metrics（MMLU σ=9.5pp）的 95% CI 覆盖从 random chance 到 near-dense 的范围，多数下游比较不具统计意义。\n\n当前贡献——\"KL 训练在 PPL 上更好但知识任务更差\" + \"mask 模式可迁移\" + \"补偿网络冗余\"——达到 Findings 的接收标准（soundness sufficient, reproducible, some insight value），但 excitement 和 impact 不足以推荐主会议。如果作者能 (a) 对 knowledge regression 提供机制性证据或缓解方案，(b) 将 decomposition claim 进一步弱化或提供新的控制实验，(c) 增加 downstream seed 数，论文在下一轮有望达到 conference 水平。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- ~190 words 合规，但信息密度极高\n- \"directional commonsense gains (n=3)\" 适当 hedged\n- \"MMLU −5.2pp on 8B; GSM8K −20.1pp on 14B\" 量化了退步，但在 n=3 高方差下这些数字的确定性被高估\n- \"may account for a substantial portion\" 对 exploratory analysis 仍偏强\n\n### Introduction\n- 数字过多（~20 个），信息过载（R2 W4，R1 disagree as style preference）\n- Gradient analysis (§3.6) 自称 \"suggestive\" 但在 contributions list 中被隐含列为核心贡献——应区分 verified empirical findings 和 suggestive analysis\n- Contributions list 中 \"Practical\" 标签在 +6.4% latency 下应改为 \"Analytical\"\n\n### Method (§3)\n- 7 个 subsection (~2.5 页) 对 empirical study 定位稍重，但保证了 reproducibility\n- Gumbel-Sigmoid vs STE 对比 convincing（PPL 15.77 → 11.79, 33.8% improvement）\n- Geometric penalty schedule: ε=0.02 缺 sensitivity analysis（R1 W4，R2 认为低优先级）\n- Forward KL vs reverse KL 的理论动机（mode-covering for false negatives）清晰\n\n### Experiments (§4)\n- Table 2: 6 列数据充实，但 HellaSwag/PIQA 仅在 Appendix（R2 W6）\n- Table 2 中 TEAL 是 deterministic single-run vs KL 3-seed 对比不对等\n- §4.2 Knowledge-Task Regression: C4 控制和 constraint analysis 是好的尝试，但未达到 mechanism-level 解释\n- §4.3 Isocompute: BCE 2700 steps 仅在 50%，30% 缺失\n- §4.4 C1 ablation: s42 non-seed-matched oracle 是历史遗留问题\n- §4.5 Per-layer KL: \"Exploratory Decomposition\" 的标注是诚实的，但 \"may account for a substantial portion\" 仍过强\n- §4.6 Cross-Architecture: PPL 泛化确认，但 Qwen-14B downstream std=5.2pp\n\n### Conclusion (§5)\n- 仅 2 句话严重不足\n- 缺：knowledge regression implications、future directions（hybrid loss, task-aware allocation）、method limitations summary、broader impact\n\n### Limitations\n- 3 个点覆盖合理（sparsity sweet spot, knowledge regression, evaluation scope）\n- 缺：仅验证 SwiGLU 架构、训练规模极小、无实际部署验证\n\n### Appendix\n- 25 个 section (A-Y, ~11 页)，认知负担大但内容充实\n- 关键数据（HellaSwag/PIQA downstream, K=4 full downstream）适合部分提升到主文\n- AI usage disclosure (Appendix Y) 合规"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 - Findings",
    "report": "# 审稿报告：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n**Target Venue**: EMNLP 2026 (ARR May cycle)  \n**Category**: Long Paper  \n**Review Round**: 28 (fresh)  \n**Reviewers**: R1（方法严谨性 + 实验设计）、R2（新颖性 + 完整性 + 写作质量）\n\n---\n\n## Summary\n\n本文系统对比了 SwiGLU LLM 上下文稀疏性预测器的训练目标。核心方法：用 forward KL divergence 替代传统 BCE，通过 Gumbel-Sigmoid 松弛训练轻量级预测器（75.9M, <1% 参数量）。在 LLaMA-3.1-8B 上 30% 稀疏度下，KL 预测器 PPL 比 TEAL 低 14.5%（8.81±0.02 vs 10.30，matched sparsity），跨架构验证（Mistral-7B -17.3%, Qwen-14B）确认泛化性。target-swap ablation (C1) 显示 KL 发现的 mask 模式可迁移到 BCE（PPL gap ≤0.79pp）。per-layer KL 分解尝试分离 signal type 和 coupling scope 的贡献。但知识密集型任务出现系统性退步（MMLU -5.2pp on 8B, GSM8K -20.1pp on 14B vs TEAL at same sparsity）。论文定位为 empirical study，不提供 wall-clock 加速。\n\n---\n\n## Strengths\n\n**S1** [双方共识] **PPL 改善显著且跨架构一致**。14.5%（30%）到 50%（50%）的 PPL 改善在 LLaMA-8B、Mistral-7B、Qwen-14B 上复现，是一个实质性的经验发现。C4 OOD 评估进一步确认泛化性。\n\n**S2** [双方共识] **实验覆盖面广**。3-seed 评估、5 种 loss variants（forward KL/reverse KL/JSD/BCE/MSE）、3 种架构（7B-14B）、2 种稀疏度、多种 allocation 策略、isocompute 对比。对于 empirical study 来说覆盖面高于多数同类工作。\n\n**S3** [双方共识] **C1 target-swap ablation 有独立 insight 价值**。证明 KL 发现的 mask patterns（而非 gradient coupling 本身）是 PPL 优势的主要来源，为后续工作提供了 \"先用 KL 找 mask，再用 BCE 训练\" 的实用路径。\n\n**S4** [双方共识] **诚实报告负面结果**。MMLU/GSM8K 回退、per-layer 分解的局限性、MSE 50% 的 catastrophic failure 等均如实报告。对 claim 的 hedging（\"directional\", \"upper bound\", \"exploratory\"）比多数论文更透明。\n\n**S5** [双方共识] **可复现性良好**。训练细节充分（lr, schedule, GPU, batch size, steps, exp_id），承诺代码开源。Taxonomy（Table 1）提供了该领域的清晰组织框架。\n\n**S6** [R1] **补偿网络冗余性发现有工程简化价值**。KL 预测器在两个稀疏度下均使 FastForward-style compensation (+67.2M) 冗余，减少推理开销。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1** [双方共识, critical] **Per-layer KL 分解存在根本性 train-inference mismatch，核心 decomposition claim 站不住脚**\n\nK=1 per-layer KL 训练时每步只 mask 1/32 层，推理时 32 层同时 mask——这是无法通过实验设计消除的根本性 mismatch。K=1 (PPL 9.05) 与 E2E (8.81) 的 2.7% gap 被论文解读为 \"signal type accounts for a substantial portion of PPL gap\"，但此 gap 之所以小是因为 K=1 训练条件近似 dense（31/32 层完整）。\n\n决定性证据：50% 下 K=1 PPL=34.85 vs E2E=11.84（2.94×），mismatch 灾难性放大；K=4 在 50% 更差（44.23 vs K=1 的 34.85），论文自己承认 \"the decomposition is interpretable only at 30%\"（§4.5）。K-curve 非单调（K=2 最差 10.75, K=16 最优 8.67），说明层间交互有复杂非线性效应。\n\n论文已做了多项改进（标注 \"upper bound\"、\"exploratory\"、补充 K=2/8/16 3-seed K-curve），但 \"may account for a substantial portion\" 的措辞对于 admittedly exploratory 且仅在 30% 有效的分析仍然过强。per-layer update count confound（K=2 ~62 updates/layer vs K=8 ~250）也未解决。\n\n*[跨轮追踪: R20-W1, 连续 9 轮被标记]*\n\n**C2** [双方共识, critical] **下游知识任务（MMLU/GSM8K）系统性退步缺乏机制性解释**\n\nKL 在所有模型/规模上系统性损害 MMLU 和 GSM8K：\n- LLaMA-8B 30%: MMLU 40.7±1.3 vs TEAL 45.86（同 uniform allocation, -5.2pp）\n- Qwen-14B 30%: GSM8K 32.0±5.2 vs TEAL 52.1（-20.1pp）\n- Mistral-7B: MMLU tied, GSM8K reverses\n\n论文排除了训练数据偏差（C4 控制），提出 forward KL mode-covering 稀释稀有激活假设，但无直接验证（如分析 KL mask 是否 prune 了 factual neurons）。Constraint analysis（remove valley → MMLU +3.4pp）说明 allocation pattern 有影响但非 mechanism 解释。跨 scale 退步暗示 structural limitation 但论文未追问 *why*。\n\n对于声称改善稀疏预测质量的论文，PPL 改善与 downstream 退步的矛盾是核心张力。缺乏缓解方向讨论（如 hybrid loss、task-aware allocation）。\n\n*[跨轮追踪: R20-N2, 连续 11 轮被标记]*\n\n**C3** [双方共识, critical] **n=3 下 downstream metrics 统计功效严重不足**\n\n- KL global 30% MMLU: 35.7±9.5pp (n=3)，95% CI ≈ [22.1, 49.3]——覆盖从 random chance 到 dense 的大部分范围\n- Qwen-14B GSM8K: 32.0±5.2pp (n=3)，CV=16.3%\n- TEAL 是 deterministic single-run，无方差信息，与 KL 的 CI 直接对比不对等\n\n论文在 §4.2 承认 \"95% CI for individual downstream tasks overlap\"，在 abstract 已改用 \"directional commonsense gains (n=3)\"，但 conclusion 和 abstract 中仍报告具体的 gap 数值（-5.2pp, -20.1pp）作为确定性结论。增加 seed 数至 ≥5（或至少 upfront disclosure 14B 的计算预算限制）是必要的。\n\n*[跨轮追踪: R24-W2, 连续 5 轮被标记]*\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [双方共识] **C1 target-swap ablation confound 未充分控制**。s42 oracle 来自 non-seed-matched earlier training run；BCE+Gumbel (32.22) vs BCE (27.97) 显示 Gumbel 对 BCE 有害，使 C1 的 \"target quality vs gradient coupling\" 分离不够干净。s123/s456 seed-matched ≤1.18pp 部分缓解。\n\n**W2** [双方共识] **MSE 50% baseline 不可信**。s123 仅达 5.1% sparsity（PPL=15,789），2/3 seed 失败。Table 4 虽有 § 标注但仍在主表中，有误导性。\n\n**W3** [双方共识] **30% 下缺少 BCE isocompute (2700 steps) 对比**。BCE isocompute 仅在 50% 有 3-seed，无法确认 30% 下 KL 对 BCE 的优势在更多训练步数后是否缩小。\n\n**W4** [双方共识] **主评估指标单一**。所有主要比较基于 WikiText-2 PPL（与训练数据 WikiText-103 同源）。C4 OOD 30% 仅 2-seed，uniform 3-seed CV=6.3% vs in-domain 0.2%。\n\n**W5** [双方共识] **Conclusion 仅 2 句话**。对于涉及复杂 trade-off（PPL vs downstream, signal type vs coupling, commonsense vs knowledge）的论文，缺乏 broader implications、future directions、knowledge regression 解决方向的讨论。\n\n**W6** [R2, R1 partial agree] **Contribution C3/C4 标注 \"Practical\" 在无 wall-clock 加速下有误导性**。Predictor +6.4% latency，无 sparse kernel 支持。论文已多处声明无加速，但 contribution 标签应改为 \"Analytical\" 或 \"Empirical\"。\n\n**W7** [R2, R1 partial agree] **训练规模极小（1000 步, ~8.2M tokens）**。虽然 convergence analysis 显示 step 800 后饱和、isocompute 分析支持 KL 优势非因训练不足，但更大规模下相对优势是否保持未验证。\n\n---\n\n## Reviewer Consensus\n\n以下问题双方达成完全共识（标注 [AGREE]）：\n\n1. [AGREE] Per-layer KL 分解的 train-inference mismatch 是根本性问题，仅在 30% 下 \"interpretable\"，50% 下完全失效\n2. [AGREE] 知识任务退步是系统性的且缺乏机制性解释，C4 控制排除数据偏差后问题更 structural\n3. [AGREE] n=3 统计功效不足，高方差下游指标的 CI overlap 使多数比较无统计意义\n4. [AGREE] PPL 改善显著且一致，是论文的核心实质性贡献\n5. [AGREE] C1 target-swap ablation 有 insight 价值但存在残余 confound（soft→hard binarization, non-seed-matched oracle）\n6. [AGREE] Conclusion 过短，缺 future directions\n7. [AGREE] Overall 3.0 (Findings)\n\n---\n\n## Reviewer Divergence\n\n以下问题存在分歧（均为严重程度分歧，非方向性分歧）：\n\n1. **MaskLLM novelty 区分**\n   - R2: Critical。MaskLLM 共享 recipe-level principle，contextual vs static 区别缺实验验证，\"KL > BCE\" 符合信息论直觉不够 surprising\n   - R1: Not critical。MaskLLM 是 static N:M sparsity，与 contextual unstructured 是不同范式，要求跨范式直接对比不合理\n   - **Director 判断**: Should-fix。R1 关于不同范式的论点成立——直接实验对比不可行。但 R2 关于 insight novelty 的质疑也合理——论文应更清晰地阐述为什么 contextual 下的 KL 行为可能与 static 下 qualitatively 不同\n\n2. **无 wall-clock 加速的严重程度**\n   - R2: Critical。+6.4% latency 且 \"Practical\" 标签 misleading\n   - R1: Should-fix。论文已充分 disclaimer，这是 empirical study 不是 systems paper\n   - **Director 判断**: Should-fix。论文的 self-positioning 已足够清晰，但 \"Practical\" 标签确实应修改\n\n3. **Excitement 评分**\n   - R1: 3/5（C1 ablation 和广覆盖面有价值）\n   - R2: 2.5/5（核心发现 expected，无实际加速，退步限制启发性）\n   - **Director 判断**: 2.5-3/5。PPL 改善本身 expected，但 mask divergence pattern 和 C1 transferability 有 non-trivial insight\n\n---\n\n## Questions\n\n1. TEAL uniform 30% MMLU 45.86 显著高于 KL 40.7±1.3。对实际部署，TEAL 在 knowledge-critical 场景是否更优？论文应明确 use-case dependent recommendation。\n2. C4-trained predictor PPL 更差（11.55 vs 8.82）但 downstream 基本不变（MMLU 40.0% vs 40.7%）——这是否表明 WikiText-103 的文本特性有助于学习更好的稀疏 pattern？\n3. 20-25% sparsity 下 downstream gap 是否更小？Figure 3 显示此区间 PPL gap 收窄。\n4. ShadowLLM 在 Table 1 归入 \"Per-token × Intermediate (MSE)\" 但其使用 attention-based routing——分类是否准确？\n5. Per-layer KL 的 per-layer update count confound（K=2 ~62/layer vs K=8 ~250/layer）是否可以通过 epoch-normalized training 控制？\n\n---\n\n## Missing References\n\n**双方共识遗漏**：\n- ActTail (2026, arXiv:2603.12272)：基于 Heavy-Tailed Self-Regularization 的全局激活稀疏性分配\n- WiSparse (2026, arXiv:2602.14452)：Weight-Aware Mixed Activation Sparsity\n\n**R1 建议、R2 反驳**（weight pruning 方法，与 activation sparsity prediction 相关性有限）：\n- LoRAShear, ZipLM\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置，不适用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 2 warning, 22 info）。\n\n**Warnings**：\n1. Abstract 视觉长度偏长，可能接近 200 words 上限（实测 ~190 words，合规）\n2. Page 7 三张表格（Table 2/3/4）集中在同一页，视觉密度偏高\n\n**格式合规**：\n- 正文 8 页 ✓\n- Limitations 在正文（page 9）✓\n- 匿名（\"Anonymous ACL submission\"）✓\n- 引用格式 ACL natbib ✓\n- 无 margin 溢出 ✓\n- Display items 密度 0.88/页，正常 ✓\n\n---\n\n## Overall Assessment\n\n**Overall**: 3.0 (Findings)\n\n**置信度**: 4/5（双方 Reviewer 均 4/5，核心问题高度共识）\n\n### 维度汇总\n\n| 维度 | R1 | R2 | 合议 |\n|------|-----|-----|------|\n| Soundness | 3/5 | 3.5/5 | 3/5 |\n| Excitement | 3/5 | 2.5/5 | 2.5/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Overall | 3.0 | 3.0 | 3.0 |\n\n### 理由\n\n本文做出了一个有价值的经验贡献：系统证明 output-distribution KL 在稀疏预测器的 PPL 表现上显著优于 BCE/MSE，且 KL 发现的 mask 模式可迁移（C1）。实验覆盖面广，报告透明诚实。\n\n三个 critical 问题阻止主会议推荐：\n\n**(1) 核心分析贡献（per-layer KL decomposition）方法学缺陷**。该分解存在无法消除的 train-inference mismatch（1/32 vs 32/32 layers masked），仅在 30% 有效且是 upper bound。如果去掉这个 decomposition contribution，论文退化为 \"KL 在 PPL 上更好但 downstream 更差\" 的实验报告。\n\n**(2) 知识任务系统性退步未解决**。MMLU/GSM8K 在所有模型/规模上退步，C4 控制排除了数据偏差但 mode-covering 假设无直接验证。对于声称改善稀疏预测质量的论文，这构成核心方法有效性的质疑——PPL 改善未转化为 deployment-relevant metrics 的提升。\n\n**(3) 统计功效不足**。n=3 下高方差 downstream metrics（MMLU σ=9.5pp）的 95% CI 覆盖从 random chance 到 near-dense 的范围，多数下游比较不具统计意义。\n\n当前贡献——\"KL 训练在 PPL 上更好但知识任务更差\" + \"mask 模式可迁移\" + \"补偿网络冗余\"——达到 Findings 的接收标准（soundness sufficient, reproducible, some insight value），但 excitement 和 impact 不足以推荐主会议。如果作者能 (a) 对 knowledge regression 提供机制性证据或缓解方案，(b) 将 decomposition claim 进一步弱化或提供新的控制实验，(c) 增加 downstream seed 数，论文在下一轮有望达到 conference 水平。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- ~190 words 合规，但信息密度极高\n- \"directional commonsense gains (n=3)\" 适当 hedged\n- \"MMLU −5.2pp on 8B; GSM8K −20.1pp on 14B\" 量化了退步，但在 n=3 高方差下这些数字的确定性被高估\n- \"may account for a substantial portion\" 对 exploratory analysis 仍偏强\n\n### Introduction\n- 数字过多（~20 个），信息过载（R2 W4，R1 disagree as style preference）\n- Gradient analysis (§3.6) 自称 \"suggestive\" 但在 contributions list 中被隐含列为核心贡献——应区分 verified empirical findings 和 suggestive analysis\n- Contributions list 中 \"Practical\" 标签在 +6.4% latency 下应改为 \"Analytical\"\n\n### Method (§3)\n- 7 个 subsection (~2.5 页) 对 empirical study 定位稍重，但保证了 reproducibility\n- Gumbel-Sigmoid vs STE 对比 convincing（PPL 15.77 → 11.79, 33.8% improvement）\n- Geometric penalty schedule: ε=0.02 缺 sensitivity analysis（R1 W4，R2 认为低优先级）\n- Forward KL vs reverse KL 的理论动机（mode-covering for false negatives）清晰\n\n### Experiments (§4)\n- Table 2: 6 列数据充实，但 HellaSwag/PIQA 仅在 Appendix（R2 W6）\n- Table 2 中 TEAL 是 deterministic single-run vs KL 3-seed 对比不对等\n- §4.2 Knowledge-Task Regression: C4 控制和 constraint analysis 是好的尝试，但未达到 mechanism-level 解释\n- §4.3 Isocompute: BCE 2700 steps 仅在 50%，30% 缺失\n- §4.4 C1 ablation: s42 non-seed-matched oracle 是历史遗留问题\n- §4.5 Per-layer KL: \"Exploratory Decomposition\" 的标注是诚实的，但 \"may account for a substantial portion\" 仍过强\n- §4.6 Cross-Architecture: PPL 泛化确认，但 Qwen-14B downstream std=5.2pp\n\n### Conclusion (§5)\n- 仅 2 句话严重不足\n- 缺：knowledge regression implications、future directions（hybrid loss, task-aware allocation）、method limitations summary、broader impact\n\n### Limitations\n- 3 个点覆盖合理（sparsity sweet spot, knowledge regression, evaluation scope）\n- 缺：仅验证 SwiGLU 架构、训练规模极小、无实际部署验证\n\n### Appendix\n- 25 个 section (A-Y, ~11 页)，认知负担大但内容充实\n- 关键数据（HellaSwag/PIQA downstream, K=4 full downstream）适合部分提升到主文\n- AI usage disclosure (Appendix Y) 合规"
  }
}
```

</details>

---


### Tool result

_source line 2269 · 2026-05-24T03:15:39.941470+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbbf8d2c695f1e79e11713aebc107790:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4014
}
```

</details>

---


### Assistant

_source line 2270 · 2026-05-24T03:15:51.627056+00:00_

审稿报告已投递。

**本轮审稿结论**：

- **Overall: 3.0 (Findings)**，双方 Reviewer 完全一致
- **3 个 Critical 共识**：(1) per-layer KL 分解的 train-inference mismatch 使核心 decomposition claim 站不住脚（连续 9 轮）；(2) 知识任务系统性退步缺乏机制性解释（连续 11 轮）；(3) n=3 统计功效不足
- **7 个 Should-Fix 共识**：C1 confound、MSE 50% 不可信、缺 30% BCE isocompute、评估指标单一、Conclusion 过短、"Practical" 标签 misleading、训练规模极小
- **2 个残余分歧**（严重程度而非方向）：MaskLLM novelty 区分（R2 critical vs R1 not critical）、无 wall-clock 加速（R2 critical vs R1 should-fix）
- **升级路径**：(a) knowledge regression 机制性证据或缓解方案；(b) decomposition claim 进一步弱化或新控制实验；(c) 增加 downstream seed 数

Issue tracker 已同步更新至 Round 28。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 201

## Round 201

2 recorded events


### User

_source line 2271 · 2026-05-24T03:15:54.217442+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

总结：R1 的 7 个问题中我同意 6 个（N1-N3, W1-W3, W5）、部分反驳 1 个（W4 ε sensitivity 重要性较低）。小问题中反驳了推理时 Gumbel 替换的说明（已在 §3.1/3.3 明确）和缺失引用建议（LoRAShear/ZipLM 是 weight pruning 而非 activation sparsity）。两位 reviewer 在 Overall 3.0 (Findings)、知识退步 framing、统计功效、per-layer decomposition confounds 上形成共识。主要分歧在于我额外将 novelty/MaskLLM 区分和无 wall-clock 加速列为 critical issues。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2272 · 2026-05-24T03:16:06.245197+00:00_

审稿报告已投递。

**汇总**：两位 Reviewer 均给出 **Overall 3.0 (Findings)**，核心问题高度收敛：

1. **Per-layer KL decomposition 方法学缺陷**（连续 9 轮标记）——train-inference mismatch 使 signal type vs coupling scope 分解不可靠
2. **知识任务系统性退步未解决**（连续 11 轮标记）——MMLU/GSM8K 跨架构退步缺乏机制性解释
3. **n=3 统计功效不足**（连续 5 轮标记）——高方差下游指标的比较无统计意义

残余分歧（MaskLLM novelty 严重程度、无 wall-clock 加速是否 critical）均为程度分歧而非方向分歧。

Issue tracker 已同步更新（3 critical open, 8 warning open/in_progress, 16 resolved）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 202

## Round 202

54 recorded events


### User

_source line 2273 · 2026-05-24T04:20:52.716194+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: distill_sparse_swiglu
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2274 · 2026-05-24T04:20:58.134098+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2275 · 2026-05-24T04:20:58.184904+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2276 · 2026-05-24T04:21:12.355180+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch,WebFetch",
  "max_results": "11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch,WebFetch",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 2277 · 2026-05-24T04:21:12.405774+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2278 · 2026-05-24T04:21:29.466766+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 2279 · 2026-05-24T04:21:30.924618+00:00_

{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (408 个)\n\n- **eval_spon_supp_retry**: DONE (failed) — \n- **lm_eval_dense_test**: DONE (failed) — \n- **lm_eval_mistral_downstream**: DONE (failed) — \n- **mvp_kl_s123**: DONE (killed) — \n- **mvp_kl_s456**: DONE (killed) — \n- **kl_sparsity70_s42**: DONE (killed) — \n- **kl_sparsity30_s42**: DONE (killed) — \n- **ste_baseline_s42**: DONE (success) — \n- **spon_supp_eval_retry**: DONE (failed) — \n- **bce_isocompute_s42**: DONE (failed) — \n- **ste_kl_s42**: DONE (killed) — \n- **spon_training_seq2048**: DONE (killed) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- qwen14b_kl30_s123_gsm8k_v4: Rerun s123 GSM8K eval (v3 failed: HF network unreachable). Added source /etc/network_turbo + HF_DATASETS_OFFLINE fallback.（准备中）\n- qwen14b_kl30_s123_gsm8k_v3: Rerun s123 GSM8K eval (v2 failed: python not found, conda not activated). Checkpoint on westd-34887.（准备中）\n- qwen14b_kl30_s123_gsm8k_v2: Rerun s123 GSM8K eval to confirm data completeness — original run (qwen14b_kl30_s123_gsm8k) was killed after ~2.5h on unreachable westd-41718, cannot verify sample_len=1319. Checkpoint available on westd-34887.（准备中）\n\n## 近期结论\n- **perlayer_kl_k4_s42** (success): Per-layer KL distillation with K=4 active layers per step and adaptive lambda scheduling can train the sparsity predictor to achieve avg KL < 0.05 while maintaining ~28% sparsity across all 32 layers.\n- **mse30_s123_downstream** (success): MSE-trained predictor at 30% sparsity (seed 123) preserves downstream task performance comparable to dense baseline because MSE distillation captures sufficient activation magnitude information to maintain task-relevant features in the sparse SwiGLU network.\n\n## 趋势\n成功 258 / 负向 24 / 失败 40 / 共 404\narc_challenge_acc_norm: 0.3737 ↓（近 3 次 success）\ngsm8k_e
…[truncated 1797 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1457
}
```

</details>

---


### Tool call

_source line 2280 · 2026-05-24T04:21:30.924972+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 2281 · 2026-05-24T04:21:31.778198+00:00_

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
16	\usepackage{subcaption}
17	
18	\setlength{\textfloatsep}{8pt plus 2pt minus 2pt}
19	\setlength{\floatsep}{8pt plus 2pt minus 2pt}
20	\setlength{\intextsep}{8pt plus 2pt minus 2pt}
21	
22	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\begin{abstract}
30	\input{abstract}
31	\end{abstract}
32	
33	\input{introduction}
34	\input{related_work}
35	\input{method}
36	\input{experiments}
37	\input{conclusion}
38	\input{limitations}
39	% \input{ethics}  % removed per submission guidelines
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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 2282 · 2026-05-24T04:21:31.828780+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 2283 · 2026-05-24T04:21:38.852898+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"}]

I found several results related to EM
…[truncated 1772 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 7024
}
```

</details>

---


### Tool call

_source line 2284 · 2026-05-24T04:21:43.073838+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements"
  }
}
```

</details>

---


### Tool call

_source line 2285 · 2026-05-24T04:21:43.475651+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers commitment deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers commitment deadline"
  }
}
```

</details>

---


### Tool call

_source line 2286 · 2026-05-24T04:21:45.331955+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract the full submission guidelines for ARR: page limits for long and short papers, formatting requirements, anonymity rules, template requirements, appendix rules, citation format, and any other submission requirements. Also find the upcoming submission deadlines for 2026."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/cfp",
    "prompt": "Extract the full submission guidelines for ARR: page limits for long and short papers, formatting requirements, anonymity rules, template requirements, appendix rules, citation format, and any other submission requirements. Also find the upcoming submission deadlines for 2026."
  }
}
```

</details>

---


### Tool result

_source line 2287 · 2026-05-24T04:21:47.740666+00:00_

Web search results for query: "EMNLP 2026 call for papers commitment deadline"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"}]

Based on the search results, here is the information about the EMNLP 2026 cal
…[truncated 589 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 4265
}
```

</details>

---


### Tool result

_source line 2288 · 2026-05-24T04:21:49.296373+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here are the ACL Rolling Review 2026 submission guidelines regarding page limits and format requirements:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Review versions of short papers may have up to four (4) pages of content, plus unlimited pages for references.

Upon acceptance, final versions of long papers will be given o
…[truncated 1121 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebSearch",
  "elapsed_ms": 6222
}
```

</details>

---


### Tool result

_source line 2289 · 2026-05-24T04:21:55.568896+00:00_

# ACL Rolling Review (ARR) Submission Guidelines

## Page Limits

**Long Papers:**
- Up to 8 pages of content
- Unlimited space for limitations section and optional ethical considerations
- Unlimited reference pages

**Short Papers:**
- Up to 4 pages of content
- Unlimited space for limitations section and optional ethical considerations
- Unlimited reference pages

Papers exceeding length requirements or lacking a limitations section face desk rejection.

## Formatting Requirements

Submissions must use the official ACL style template available on GitHub. All text should be "addressed exclusively to the human readers and be clearly visible to them." Papers not conforming to required styles—including page size, margins, and font size—are rejected without review.

## Anonymity Rules

Papers must exclude author names and affiliations. Authors should avoid self-references like "We previously showed..." Instead, use third-person citations: "Smith previously showed..." Supplementary materials and repository links must also be anonymized. File-sharing services tracking downloads (Dropbox, Google Drive) are prohibited.

## Appendix Guidelines

Appendices follow the double-column format (with stated exceptions) and appear after references without counting toward page limits. Reviewers are not obligated to review appendices. Critical content for assessing novelty or technical accuracy belongs in the main paper, not appendices.

## Citation Requirements

Authors must cite all relevant refereed publications. Papers appearing fewer than 3 months before submission are considered contemporaneous and don't require detailed comparisons. When preprints have been superseded by refereed versions, cite the refereed publication instead or additionally.

## Upcoming 2026 Deadlines

The document does not specify 2026 submission deadlines. It references cycles with "every two months" frequency but provides no concrete dates for the coming year.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebFetch",
  "elapsed_ms": 10236
}
```

</details>

---


### Tool call

_source line 2290 · 2026-05-24T04:22:01.317071+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract all submission requirements: page limits, formatting, anonymity rules, deadline dates, commitment deadline, topics, and any special instructions for EMNLP 2026. Include all important dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract all submission requirements: page limits, formatting, anonymity rules, deadline dates, commitment deadline, topics, and any special instructions for EMNLP 2026. Include all important dates."
  }
}
```

</details>

---


### Tool call

_source line 2291 · 2026-05-24T04:22:01.317399+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2292 · 2026-05-24T04:22:01.317564+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 2293 · 2026-05-24T04:22:07.288234+00:00_

# EMNLP 2026 Submission Requirements Summary

## Page Limits
- **Long Papers:** 8 pages (9 pages in camera-ready version)
- **Short Papers:** 4 pages (5 pages in camera-ready version)

## Important Dates
| Event | Date |
|-------|------|
| ARR Submission Deadline | May 25, 2026 |
| Reviewer Registration Deadline | May 27, 2026 |
| Author Response Period | July 7-13, 2026 |
| Meta Review Released | July 30, 2026 |
| EMNLP Commitment Deadline | August 2, 2026 |
| Acceptance Notification | August 20, 2026 |
| Camera-Ready Due | September 20, 2026 |
| Main Conference | October 24-29, 2026 |

*All deadlines are 11:59PM UTC-12:00*

## Anonymity & Review Process
The conference employs "double-blind" review where "reviewers will not see authors, nor will authors see reviewers." However, there is "no anonymity period requirement" following ACL policies.

## Submission Topics
Accepted areas span traditional NLP research including machine translation, dialogue systems, information extraction, language modeling, and ethics/bias. A special theme addresses "New Missions for NLP Research," emphasizing evaluation methodologies, system-level research, scientific understanding of language, data governance, and LLMs as research instruments.

## Special Requirements
- Authors must declare conference commitment at ARR submission time
- Dual submissions prohibited
- Mandatory reviewing participation expected
- Author lists cannot be modified during commitment phase
- All accepted papers require in-person or virtual conference presentation

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "WebFetch",
  "elapsed_ms": 5971
}
```

</details>

---


### Tool call

_source line 2294 · 2026-05-24T04:22:15.005333+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper"
  }
}
```

</details>

---


### Tool result

_source line 2295 · 2026-05-24T04:22:15.256524+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 2296 · 2026-05-24T04:22:15.256818+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "file": "artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2297 · 2026-05-24T04:22:15.307932+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2298 · 2026-05-24T04:22:22.483526+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2299 · 2026-05-24T04:22:22.985748+00:00_

1	Learned sparsity predictors for SwiGLU LLMs predominantly use binary cross-entropy (BCE), training each neuron independently, yet inference allocates budgets globally via top-$k$ ranking.
2	We train lightweight predictors ($<$1\% of base parameters) with forward KL divergence, coupling all mask decisions through the output distribution.
3	On LLaMA-3.1-8B at 30\% sparsity, the KL predictor reduces perplexity by 14.5\% over TEAL at matched sparsity, with directional commonsense gains ($n{=}3$) but knowledge-intensive regression (8B MMLU $-$5.2pp, CIs overlap; 14B GSM8K $-$19.9pp, $n{=}3$); post-hoc compensation (+67.2M params) becomes redundant.
4	Output-distribution optimization yields masks that diverge 46--68\% from magnitude-based targets; a target-swap ablation suggests these discovered patterns carry most of the quality information: BCE trained on KL-derived targets approaches KL-level PPL (PPL gap $\leq$0.65pp; 3-seed, 30\%).
5	Per-layer controls show the signal type gap (9.47 PPL) exceeds the coupling breadth range (2.08 PPL) at 30\%, though the decomposition is confounded by train--inference mismatch; a $K{=}4$ control suggests task-dependent coupling effects (\S\ref{sec:perlayer}).
6	Cross-architecture evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms PPL generalization with scale-dependent downstream effects.
7	This is primarily an empirical study; wall-clock speedup requires sparse kernel support not addressed here.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2300 · 2026-05-24T04:22:22.986145+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2301 · 2026-05-24T04:22:23.889785+00:00_

1	\section{Introduction}
2	
3	How the training objective shapes learned sparsity prediction quality is an open question for SwiGLU LLMs~\cite{shazeer2020glu}. SwiGLU FFN blocks exhibit high contextual sparsity, but their gated activation makes importance prediction challenging: neuron importance depends on both gate and up-projection values, a target that magnitude-based methods handle suboptimally.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they predominantly rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: the TEAL (training-free activation sparsity;~\citealp{liu2025teal}) top-$k$ mechanism ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	Unlike MaskLLM~\cite{fang2024maskllm}, which applies KL to static N:M weight masks, we address contextual activation sparsity where masks must generalize to unseen inputs, vary per token, and coordinate across layers through global allocation.
8	
9	Gradient analysis reveals a structural asymmetry: BCE's gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$ depends only on neuron $j$, while under KL divergence, the gradient couples each neuron to all others through the downstream Jacobian (\S\ref{sec:method:gradient}).
10	KL's coupled gradients discover neuron importance patterns that diverge 68\% from magnitude-based masks (mean per-layer Jaccard distance).
11	A target-swap ablation shows KL-discovered mask targets carry most of the quality information: BCE retrained on KL-derived targets approaches KL PPL ($\leq$0.65pp gap, 3-seed), while magnitude-trained BCE yields 28.13$\pm$0.20. Per-layer controls suggest coupling
…[truncated 3122 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 2302 · 2026-05-24T04:22:23.890153+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2303 · 2026-05-24T04:22:24.392417+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present an output-distribution KL framework for training contextual sparsity predictors in SwiGLU-based language models (Figure~\ref{fig:overview}).
5	The method replaces per-neuron binary classification (BCE) with an output-distribution alignment objective that couples all pruning decisions through the model's forward pass and achieves competitive performance without auxiliary error compensation networks at inference.
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
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{x}^{(\ell)}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces p
…[truncated 9831 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2304 · 2026-05-24T04:22:24.392871+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2305 · 2026-05-24T04:22:24.895234+00:00_

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
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4 on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB), using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $1 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), GSM8K (8-shot), HellaSwag (10-shot), and PIQA (0-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly\footnote{TEAL is deterministic; single-run evaluation suffices. KL/BCE predictors require multi-seed evaluation due to random initialization.}; (2) \textbf{BCE predictor} (Deja
…[truncated 16817 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2306 · 2026-05-24T04:22:24.895585+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2307 · 2026-05-24T04:22:25.297401+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} and GRASP~\cite{shin2025grasp} predict activation sparsity patterns without additional training.
6	LaRoSA~\cite{huang2025larosa} applies layerwise orthogonal rotations for structured activation sparsity with wall-clock speedup on SiLU models.
7	Wang et al.~\cite{wang2025dynamicsparse}, AWQ~\cite{lin2024awq}, and Outlier Suppression+~\cite{wei2023outlier} address sparsity--quantization interactions and activation-aware quantization.
8	Dhar et al.~\cite{dhar2024activation} characterize activation sparsity opportunities across architectures, showing that SwiGLU models exhibit lower natural sparsity than ReLU counterparts.
9	OWL~\cite{yin2024owl} determines per-layer sparsity ratios from outlier distributions for weight pruning.
10	ActTail~\cite{zheng2026acttail} applies heavy-tailed self-regularization for global activation sparsity allocation; WiSparse~\cite{yang2026wisparse} proposes weight-aware mixed activation sparsity.
11	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
12	
13	\paragraph{Predictor-Based Contextual Sparsity.}
14	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
15	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gr
…[truncated 5227 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 2308 · 2026-05-24T04:22:25.348142+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2309 · 2026-05-24T04:22:27.205552+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Output-distribution alignment is the primary design dimension for learned sparsity prediction, outperforming BCE and MSE across five losses.
5	The KL predictor reduces PPL by 14.5\% over TEAL at 30\%, confirmed on Mistral-7B ($-$17.3\%) and Qwen-2.5-14B.
6	Gains are task-type dependent: KL improves commonsense reasoning but degrades knowledge-intensive tasks (C4 control confirms structural to KL), suggesting KL for commonsense/PPL and TEAL for knowledge tasks.
7	The signal type gap (9.47 PPL) exceeds the coupling breadth range (2.08 PPL), though the decomposition is confounded by train--inference mismatch (\S\ref{sec:perlayer}); disentangling these factors remains an open question.
8	Downstream differences are directional ($n{=}3$, CIs overlap). Code released upon acceptance.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 1857
}
```

</details>

---


### Tool call

_source line 2310 · 2026-05-24T04:22:27.506991+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 2311 · 2026-05-24T04:22:27.507423+00:00_

1	\section*{Limitations}
2	
3	Our findings are bounded by four limitations.
4	\textbf{Sparsity sweet spot.} 30\% is the lowest-degradation level; at 50\%, all methods collapse on reasoning tasks, and a separate predictor must be retrained per target.
5	\textbf{Knowledge-intensive regression.} KL consistently underperforms on MMLU and GSM8K across scales (8B: $-$5.2pp MMLU; 14B: $-$19.9pp GSM8K), suggesting output-distribution objectives systematically sacrifice reasoning-critical pathways.
6	\textbf{Evaluation scope.} Open-ended generation (e.g., MT-Bench) and contexts beyond 2048 tokens remain untested.
7	\textbf{Baseline coverage.} The 30\% isocompute comparison lacks a BCE 2700-step baseline; WikiText-2 evaluation shares provenance with the training corpus (WikiText-103), partially mitigated by C4 OOD results (Appendix~\ref{app:ood}).
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2312 · 2026-05-24T04:22:27.557874+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 2313 · 2026-05-24T04:22:33.113352+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB; batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
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
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); output-distribution KL thus provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% o
…[truncated 41692 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 5555
}
```

</details>

---


### Tool call

_source line 2314 · 2026-05-24T04:22:33.114369+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 2315 · 2026-05-24T04:22:33.266717+00:00_

issues:
  # ============================================================
  # Round 28 — Active issues
  # ============================================================

  - id: "R20-W1"
    summary: "Per-layer KL decomposition 的 train-inference mismatch confound 未解决"
    category: method
    severity: critical
    status: in_progress
    first_raised_round: 20
    last_seen_round: 28
    mentions:
      - {round: 21, reviewers: [1, 2], note: "R21 Critical。K=4 single-seed。"}
      - {round: 22, reviewers: [1, 2], note: "R22 N2。97.5% 精确数字不可靠。"}
      - {round: 24, reviewers: [1, 2], note: "R24 C1。K=1 有 32× train-inference mismatch。"}
      - {round: 25, reviewers: [1, 2], note: "R25 N1/N2。"}
      - {round: 26, reviewers: [1, 2], note: "R26 R1-N2/R2-N1。建议 stop-gradient 或更多 K 值。"}
      - {round: 27, reviewers: [1, 2], note: "R27 C1。K-curve 6 点中除 K=4 外均 single-seed。K=16 PPL 优势可能 seed-specific。per-layer update count confound 未解决。"}
      - {round: 28, reviewers: [1, 2], note: "R28 双方 AGREE critical。50% 下 K=1 PPL=34.85 vs E2E=11.84（2.94×）是 decisive evidence。K=4 在 50% 更差（44.23）。论文已有 'upper bound' 和 'exploratory' 标注，但 'may account for a substantial portion' 仍被认为对 exploratory analysis 过强。K=2/8/16 3-seed 数据已补充但 per-layer update count confound 仍未解决。"}
    action_items:
      - {round: 21, action: "K=4 3-seed", assigned_to: "main_agent", status: done}
      - {round: 22, action: "定性 'majority of PPL gap'", assigned_to: "paper_agent", status: done}
      - {round: 25, action: "限定 decomposition 为 moderate sparsity", assigned_to: "paper_agent", status: done}
      - {round: 25, action: "K=2/K=8/K=16 实验扩展 K-curve", assigned_to: "main_agent", status: done}
      - {round: 27, action: "§4.5 降级为 Exploratory Decomposition + may account for a substantial portion", assigned_to: "paper_agent", status: done}
      - {round: 27, action: "experiments L161 'primary design lever' → 'major factor for PPL'", assigned_to: "paper_agent", status: done}
      - {round: 27, action: "appendix L647 加 '
…[truncated 16274 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 2316 · 2026-05-24T04:23:09.678034+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_CONFIG_FOUND\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_CONFIG_FOUND\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 2317 · 2026-05-24T04:23:10.130337+00:00_

NO_CONFIG_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2318 · 2026-05-24T04:23:10.181183+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 2319 · 2026-05-24T04:23:10.282795+00:00_

1	% =============================================================================
2	% Additional references (R20 review response)
3	% =============================================================================
4	
5	@article{zheng2026acttail,
6	  title={{ActTail}: Heavy-Tailed Self-Regularization for Activation Sparsity in Large Language Models},
7	  author={Zheng, Haocheng and others},
8	  journal={arXiv preprint arXiv:2603.12272},
9	  year={2026}
10	}
11	
12	@article{yang2026wisparse,
13	  title={{WiSparse}: Weight-Aware Mixed Activation Sparsity for Large Language Models},
14	  author={Yang, others},
15	  journal={arXiv preprint arXiv:2602.14452},
16	  year={2026}
17	}
18	
19	@article{huang2025larosa,
20	  title={La{R}o{SA}: Accelerating Large Language Model Inference with Layerwise Rotated Sparse Activation},
21	  author={Huang, Fangcheng and others},
22	  journal={arXiv preprint arXiv:2507.01299},
23	  year={2025}
24	}
25	
26	@inproceedings{geva2023dissecting,
27	  title = {Dissecting Recall of Factual Associations in Auto-Regressive Language Models},
28	  author = {Geva, Mor and Bastings, Jasmijn and Filippova, Katja and Globerson, Amir},
29	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
30	  pages = {12216--12235},
31	  year = {2023},
32	}
33	
34	@article{fu2024lazyllm,
35	  title = {{LazyLLM}: Dynamic Token Pruning for Efficient Long Context {LLM} Inference},
36	  author = {Qichen Fu and Minsik Cho and Thomas Merth and Sachin Mehta and Mohammad Rastegari and Mahyar Najibi},
37	  year = {2024},
38	  journal = {arXiv preprint arXiv:2407.14057},
39	}
40	
41	@article{zhang2025cots,
42	  title = {{COTS}: Connected Sparse Activation for Efficient {LLM} Inference},
43	  author = {Yilong Zhang and Junyuan Shang and Huanqi Cao and Shiyao Li and Shuguang Jiang and Lingxiao Ma and Shun Zheng and Cheng Li and Jiang Bian},
44	  year = {2025},
45	  journal = {arXiv preprint arXiv:2502.14475
…[truncated 24824 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2320 · 2026-05-24T04:23:34.601090+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "review_chat_id": "oc_ddde40053945c09c17d4aaa8ca8e5b93"
  }
}
```

</details>

---


### Tool result

_source line 2321 · 2026-05-24T04:23:54.029012+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 19427
}
```

</details>

---


### Tool call

_source line 2322 · 2026-05-24T04:23:54.081207+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计**。\n\n## 论文信息\n- **标题**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n- **路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/submitted.pdf\n\n## Venue 要求\n- **EMNLP 2026** via ACL Rolling Review (ARR)\n- **Deadline**: 2026-05-25\n- **页数限制**: Long paper 8 页正文 + unlimited references + Limitations 不计入页数\n- **模板**: ACL template with `[review]` option\n- **匿名**: Double-blind（不出现作者信息、避免自引）\n- **附录**: 在 references 之后，不计入页数，reviewer 不保证会读\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **方法严谨性**\n   - KL vs BCE 梯度分析（§3.6）的理论推导是否正确，结论是否 over-claimed\n   - Gumbel-Sigmoid relaxation 的数学正确性和与 STE 对比的公平性\n   - Geometric penalty schedule 的收敛保证\n   - Forward KL vs reverse KL 选择的论证是否充分\n\n2. **实验设计**\n   - 统计方法：n=3 seeds 是否足够支撑 claims，CI overlap 下是否有 over-claiming\n   - Ablation 设计：C1 target-swap 是否有残余 confound（soft→hard binarization、oracle provenance）\n   - Per-layer KL decomposition（§4.5）的 train-inference mismatch confound\n   - Baseline 公平性：BCE/MSE 是否在最优配置下对比\n   - WikiText-2 evaluation 与 WikiText-103 training 的同源性问题\n\n3. **Cross-architecture 证据**\n   - Mistral 3-seed vs LLaMA 对比的充分性\n   - Qwen-14B 结果中 GSM8K σ=5.3pp 的可靠性\n\n4. **格式合规**\n   - 8 页限制\n   - Limitations 节完整性\n   - 匿名性\n\n请以 ACL/EMNLP 审稿标准产出结构化审稿意见：Summary, Strengths (S1-Sn), Weaknesses (W1-Wn), Questions (Q1-Qn), Missing References, Minor Issues, Overall Assessment (1-5 scale per EMNLP 2026 ARR rubric)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计**。\n\n## 论文信息\n- **标题**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n- **路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/submitted.pdf\n\n## Venue 要求\n- **EMNLP 2026** via ACL Rolling Review (ARR)\n- **Deadline**: 2026-05-25\n- **页数限制**: Long paper 8 页正文 + unlimited references + Limitations 不计入页数\n- **模板**: ACL template with `[review]` option\n- **匿名**: Double-blind（不出现作者信息、避免自引）\n- **附录**: 在 references 之后，不计入页数，reviewer 不保证会读\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **方法严谨性**\n   - KL vs BCE 梯度分析（§3.6）的理论推导是否正确，结论是否 over-claimed\n   - Gumbel-Sigmoid relaxation 的数学正确性和与 STE 对比的公平性\n   - Geometric penalty schedule 的收敛保证\n   - Forward KL vs reverse KL 选择的论证是否充分\n\n2. **实验设计**\n   - 统计方法：n=3 seeds 是否足够支撑 claims，CI overlap 下是否有 over-claiming\n   - Ablation 设计：C1 target-swap 是否有残余 confound（soft→hard binarization、oracle provenance）\n   - Per-layer KL decomposition（§4.5）的 train-inference mismatch confound\n   - Baseline 公平性：BCE/MSE 是否在最优配置下对比\n   - WikiText-2 evaluation 与 WikiText-103 training 的同源性问题\n\n3. **Cross-architecture 证据**\n   - Mistral 3-seed vs LLaMA 对比的充分性\n   - Qwen-14B 结果中 GSM8K σ=5.3pp 的可靠性\n\n4. **格式合规**\n   - 8 页限制\n   - Limitations 节完整性\n   - 匿名性\n\n请以 ACL/EMNLP 审稿标准产出结构化审稿意见：Summary, Strengths (S1-Sn), Weaknesses (W1-Wn), Questions (Q1-Qn), Missing References, Minor Issues, Overall Assessment (1-5 scale per EMNLP 2026 ARR rubric)。"
  }
}
```

</details>

---


### Tool result

_source line 2323 · 2026-05-24T04:24:07.077503+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 12996
}
```

</details>

---


### Tool call

_source line 2324 · 2026-05-24T04:24:07.178449+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查 **新颖性 + 完整性 + 写作质量**。\n\n## 论文信息\n- **标题**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n- **路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/submitted.pdf\n\n## Venue 要求\n- **EMNLP 2026** via ACL Rolling Review (ARR)\n- **Deadline**: 2026-05-25\n- **页数限制**: Long paper 8 页正文 + unlimited references + Limitations 不计入页数\n- **模板**: ACL template with `[review]` option\n- **匿名**: Double-blind（不出现作者信息、避免自引）\n- **附录**: 在 references 之后，不计入页数，reviewer 不保证会读\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **新颖性评估**\n   - 核心 recipe（frozen model + learnable mask + KL + Gumbel relaxation）与 MaskLLM 共享程度——contextual vs static 的区别是否构成足够新颖性\n   - 各组件（KL distillation、Gumbel-Sigmoid、top-k allocation）均为 established techniques，组合新颖性是否达到 EMNLP 标准\n   - Taxonomy（Table 1）的 positioning 是否准确，是否遗漏重要相关工作\n\n2. **Claim 与证据匹配**\n   - Abstract/Introduction 中的 claim 是否被实验充分支撑\n   - \"Primary design dimension\" claim 的 scope 是否合理限定\n   - 知识任务退步（MMLU/GSM8K）的讨论是否充分\n   - Contribution list 中 \"Empirical\" vs \"Analytical\" 标注是否准确\n\n3. **写作质量**\n   - 论文结构和叙事流畅度\n   - 信息密度是否合适（是否过度压缩或冗余）\n   - Conclusion 是否充分讨论 implications 和 future directions\n   - 术语一致性\n   - Figure/Table 质量和信息量\n\n4. **完整性**\n   - Related Work 覆盖度（是否遗漏 2025-2026 重要工作）\n   - Limitations 节是否充分\n   - 评估基准覆盖度\n   - 可复现性信息是否充足\n\n请以 ACL/EMNLP 审稿标准产出结构化审稿意见：Summary, Strengths (S1-Sn), Weaknesses (W1-Wn), Questions (Q1-Qn), Missing References, Minor Issues, Overall Assessment (1-5 scale per EMNLP 2026 ARR rubric)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责审查 **新颖性 + 完整性 + 写作质量**。\n\n## 论文信息\n- **标题**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n- **路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/submitted.pdf\n\n## Venue 要求\n- **EMNLP 2026** via ACL Rolling Review (ARR)\n- **Deadline**: 2026-05-25\n- **页数限制**: Long paper 8 页正文 + unlimited references + Limitations 不计入页数\n- **模板**: ACL template with `[review]` option\n- **匿名**: Double-blind（不出现作者信息、避免自引）\n- **附录**: 在 references 之后，不计入页数，reviewer 不保证会读\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **新颖性评估**\n   - 核心 recipe（frozen model + learnable mask + KL + Gumbel relaxation）与 MaskLLM 共享程度——contextual vs static 的区别是否构成足够新颖性\n   - 各组件（KL distillation、Gumbel-Sigmoid、top-k allocation）均为 established techniques，组合新颖性是否达到 EMNLP 标准\n   - Taxonomy（Table 1）的 positioning 是否准确，是否遗漏重要相关工作\n\n2. **Claim 与证据匹配**\n   - Abstract/Introduction 中的 claim 是否被实验充分支撑\n   - \"Primary design dimension\" claim 的 scope 是否合理限定\n   - 知识任务退步（MMLU/GSM8K）的讨论是否充分\n   - Contribution list 中 \"Empirical\" vs \"Analytical\" 标注是否准确\n\n3. **写作质量**\n   - 论文结构和叙事流畅度\n   - 信息密度是否合适（是否过度压缩或冗余）\n   - Conclusion 是否充分讨论 implications 和 future directions\n   - 术语一致性\n   - Figure/Table 质量和信息量\n\n4. **完整性**\n   - Related Work 覆盖度（是否遗漏 2025-2026 重要工作）\n   - Limitations 节是否充分\n   - 评估基准覆盖度\n   - 可复现性信息是否充足\n\n请以 ACL/EMNLP 审稿标准产出结构化审稿意见：Summary, Strengths (S1-Sn), Weaknesses (W1-Wn), Questions (Q1-Qn), Missing References, Minor Issues, Overall Assessment (1-5 scale per EMNLP 2026 ARR rubric)。"
  }
}
```

</details>

---


### Tool result

_source line 2325 · 2026-05-24T04:24:08.686330+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1507
}
```

</details>

---


### Assistant

_source line 2326 · 2026-05-24T04:24:25.247761+00:00_

已派发：
- ✅ Reviewer 1（方法严谨性 + 实验设计）— Round 1
- ✅ Reviewer 2（新颖性 + 完整性 + 写作）— Round 1
- ✅ 视觉审查 Agent — 已启动

等待两位 Reviewer 完成独立审稿。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 203

## Round 203

2 recorded events


### User

_source line 2327 · 2026-05-24T04:29:35.609945+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 审稿意见 — 方法严谨性 + 实验设计

**论文:** Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
**Venue:** EMNLP 2026 via ACL Rolling Review

---

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: PPL 维度的改进令人信服（14.5% over TEAL, 3-seed, CI 不重叠），但知识类任务系统性退化（MMLU −5.2pp）、缺乏实际加速、以及 §4.5 信号类型 vs. 耦合范围的分解被 train-inference mismatch 严重混淆，共同削弱了贡献的实际影响力。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 核心方法（KL+Gumbel-Sigmoid）数学正确；梯度分析（§3.6）定性合理但未形式化；per-layer 分解（§4.5）被承认有 confound 但仍从中下结论；C1 ablation 有残余混淆变量 |
| Excitement | 3/5 | 研究问题（训练目标如何影响 sparsity predictor 质量）有价值，但实际贡献局限于"PPL 更好但 MMLU/GSM8K 更差"的 trade-off，且无实际加速 |
| Reproducibility | 4/5 | 实验细节充分（超参数、seed、exp_id 注释），承诺开源代码；OOD 验证和多 seed 评估增强了可重复性 |
| Clarity | 4/5 | 写作清晰坦诚，limitations 主动披露；notation 一致；但 §4.5 的嵌套 confound 讨论较难跟进 |
| Reviewer Confidence | 4/5 | 熟悉 activation sparsity、KD、Gumbel relaxation 相关文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] §4.5 Per-Layer KL 分解的 claim 超出证据支撑
- 具体位置：§4.5 (experiments.tex L155-160)、Conclusion (conclusion.tex L7)、Abstract (abstract.tex L5)
- 问题：论文在 Abstract、§4.5、Conclusion 中反复强调 "signal type gap (9.47 PPL) exceeds coupling breadth range (2.08 PPL)"，将此作为核心贡献之一。然而论文自身承认这一分解被 **train-inference mismatch** 严重混淆：K=1 训练时 1/32 层带 mask，推理时 32/32 层带 mask；K=4 控制实验虽部分缓解但自身也有 confound。更严重的是，在 50% sparsity 下 K=1 (34.85) 反而优于 K=4 (44.23)（Table 5 / experiments.tex L159），这一反常结果直接否定了该分解在高 sparsity 下的有效性。
- 为什么影响接收：这是论文的第一条 contribution（Introduction L23-24），如果分解不可靠，contribution list 需要实质性修改。论文虽然在 §4.5 内有诚实的 caveat，但 Abstract 和 Conclusion 中的表述没有相应降级，给读者留下了过于确定的印象。
- 建议修改方向：(1) 在 Abstract/Conclusion 中明确标注 "confounded by train-inference mismatch" 限定语；(2) 将 9.47 vs 2.08 的对比从 claim 降级为 observation；(3) 考虑设计一个无 mismatch 的控制实验（如 K=1 训练但推理也只 mask 1 层）以真正隔离 signal type 效应。

**N2** [critical] 知识任务系统性退化未充分分析因果机制
- 具体位置：§4.2 (experiments.tex L32-37)、Conclusion (conclusion.tex L6)、Limitations (limitations.tex L5)
- 问题：MMLU 退化（30%: 40.7 vs TEAL 45.86, −5.2pp）和 GSM8K 退化（14B: 32.2±5.3 vs 52.1, −19.9pp）是论文最显著的负面结果。论文将其归因于 "forward KL's mode-covering property" 结构性地牺牲 rare reasoning-critical activations，并用 C4 control（Appendix V, Table 22）排除了训练数据成分的因素。然而：
  (a) C4 control 是 **单 seed**（s42），不足以排除 seed-dependent 效应；
  (b) "mode-covering sacrifices rare activations" 的因果论证停留在直觉层面，没有进一步的实证支持（如分析哪些特定 neuron 被错误剪枝、或者在 MMLU 的具体样本上做 case study）；
  (c) Constraint 实验（Appendix T, Table 20）显示 remove valley → MMLU +3.4pp，说明 allocation 是部分原因，但这与 "KL structural property" 的解释存在张力——如果只是 allocation 问题，那用 task-aware allocation 就能修复，不应该是 KL 的固有缺陷。
- 为什么影响接收：对于声称改进 sparsity prediction 的论文，在核心下游任务上系统性退化而无法解释因果机制，会严重限制方法的可推荐性。
- 建议修改方向：(1) C4 control 增加到 3-seed；(2) 对 MMLU/GSM8K 退化做 neuron-level 的归因分析（如检查 KL 和 TEAL 在 MMLU 相关 layer 上的具体剪枝差异）；(3) 更清晰地区分 "allocation-induced regression"（可修复）和 "loss-inherent regression"（结构性）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] C1 Target-Swap Ablation 残余 confound 未充分讨论
- 具体位置：§4.4 (experiments.tex L86-116)、Table 3
- 问题：C1 ablation 试图分离 "mask target quality" 和 "gradient coupling"，但存在至少三个残余 confound：
  (1) **Soft→hard binarization**：KL oracle 通过 logits>0 硬阈值化，丢弃了 ranking information（论文已承认）；
  (2) **Oracle provenance 不一致**：s42 oracle 来自 earlier non-seed-matched checkpoint（gap 0.65pp），s123/s456 用 seed-matched oracles（gap ≤0.03pp）。这导致 s42 的 C1 PPL (9.45) 显著劣于 s123 (8.84) 和 s456 (8.82)，而这个差异可能来自 oracle provenance 而非 seed 本身；
  (3) **BCE+Gumbel 表现反常**：BCE+Gumbel (32.22) 劣于 standard BCE (27.97)（Table 5），论文称之为 "trajectory-dependent confounds"，但这意味着 Gumbel relaxation 对 BCE 是有害的，而它对 KL 是核心组件——这一 asymmetry 需要更多讨论。
- 建议：(1) 将 s42 的 oracle provenance 差异在 Table 3 caption 中更显著标注；(2) 讨论为什么 Gumbel 对 BCE 有害（BCE 的固定 oracle target 不需要 soft exploration？）；(3) 明确承认 C1 无法完全隔离 target quality vs gradient coupling。

**W2** [warning] MSE baseline 可能未在最优配置下评估
- 具体位置：§4.4 (Table 5)、Appendix G (appendix.tex L236-246)
- 问题：MSE 在 50% 时 2/3 seeds 崩溃（只达 5.1% sparsity），只有 s42 的 229.26 PPL 可用。这说明 MSE+Gumbel+Lagrangian 的组合在高 sparsity 下不稳定。论文用 "same hyperparameters" 作为控制变量，但如果 MSE 需要不同的 λ_max 或 temperature schedule 才能工作，那么 "identical setup" 反而 unfairly disadvantages MSE。
- 建议：(1) 为 MSE 做一轮 λ_max 的小搜索（如 2000, 5000），报告是否能避免崩溃；(2) 如果 MSE 在合理超参下仍然显著劣于 KL，这个 claim 就更强了。目前 MSE 50% 数据点本质上是 anecdotal（单 seed）。

**W3** [warning] n=3 seeds 对部分 claim 支撑不足
- 具体位置：Table 2 (experiments.tex L41-68)、§4.6 (experiments.tex L193)
- 问题：
  (a) MMLU 在 30% global allocation 下 σ=9.5pp（35.7±9.5），3-seed 的 95% CI 约为 [11.9, 59.5]——这个区间跨越了 TEAL (45.86) 的值，因此 "KL 在 MMLU 上退化" 在 global allocation 下不能被统计确认；
  (b) Qwen-14B GSM8K σ=5.3pp (32.2±5.3)，虽然均值差 19.9pp 在统计上显著（~3.7σ），但绝对方差仍然大到令人担忧；
  (c) Mistral ARC-c σ=6.4pp（Table 16），使该 metric 的比较无意义。
- 论文在 §4.2 中正确地将 PPL 作为 primary metric（σ=0.02, non-overlapping），但仍然在多处对方差极大的下游指标做了 directional claims。
- 建议：在 Table 2 和相关讨论中，对 CI 重叠的 downstream 比较加上 "statistically indeterminate" 标注；或增加到 5 seeds。

**W4** [warning] WikiText-2 eval / WikiText-103 training 同源性
- 具体位置：Limitations (limitations.tex L7)、Appendix D (appendix.tex L151-201)
- 问题：WikiText-2 和 WikiText-103 来自同一 Wikipedia 语料，虽然 split 不重叠，但 domain 和 style 完全一致，PPL 评估可能 inflate KL predictor 的优势（predictor 过拟合 Wikipedia 文体的 activation pattern）。C4 OOD 验证（Appendix D, Table 10）部分缓解了这个问题，但：
  (a) C4 30% 只有 2-seed（不是 3-seed）；
  (b) C4 30% uniform 的 cross-seed CV=6.3%，远高于 WikiText-2 的 0.2%，暗示 predictor 对 domain 有敏感性；
  (c) C4 30% 的 TEAL baseline 未报告，无法在 C4 上确认 KL vs TEAL 的优势。
- 建议：(1) C4 评估补充 TEAL baseline 和 3-seed 评估；(2) 在主文 Table 2 中加入 C4 PPL 列或交叉引用 Appendix 结果。

---

## 小问题（不影响接收）

- **格式合规**: 正文 8 页 ✓；Limitations 在 references 前 ✓；[review] 选项 ✓；"Anonymous ACL submission" ✓；未发现明显 de-anonymization。
- **Eq. 4 (Gumbel-Sigmoid)**: ε₁ − ε₂ 其中 ε₁, ε₂ ∼ Gumbel(0,1) 等价于 Logistic(0,1) 噪声，数学正确。可考虑加一句说明这一等价性，减少读者困惑。
- **Table 5 (Ablation)**: STE 行的 30% 列标注 "---‡" 并在脚注解释 STE 实际 sparsity 为 20.8% 而非 30%，这个处理合理但容易被忽视。建议在 STE 行直接标注实际 sparsity。
- **§3.5 Geometric Penalty Schedule**: Eq. 7 中 clamp 的 min=0 参数在 LaTeX 中渲染不太清晰。
- **Abstract 字数**: 约 173 词，在 200 词限制内 ✓。
- **Appendix Y (AI Assistants)**: 披露了 Claude 的使用，符合 ARR 要求。

---

## 主要优势

- **S1**: 实验设计总体上很严谨——C1 target-swap ablation、C4 training control、per-layer K-curve 分解、MSE 控制变量实验——形成了一个多角度的分析框架，即使每个控制实验单独来看都有 confound，组合起来仍然提供了有说服力的证据。
- **S2**: 论文异常坦诚地报告负面结果和 confounds：MMLU/GSM8K 退化在 abstract 中就提到；§4.5 明确承认 train-inference mismatch；Limitations 列出 isocompute 缺失、同源性问题。这种透明度在同行评审中值得肯定。
- **S3**: PPL 改进在统计上令人信服（8.81±0.02 vs 10.30, non-overlapping CIs, 3-seed），且跨架构泛化（Mistral −17.3%, Qwen-14B −12.6%）。
- **S4**: 方法简洁——lightweight predictor (<1% params)、无需 compensation network、训练仅需 1000 步——降低了 practical barrier，即使目前没有加速也为后续 sparse kernel work 提供了基础。
- **S5**: Taxonomy（Table 1, §3.7）提供了一个有用的概念框架（correction granularity × training signal coupling），有助于组织文献并定位贡献。

---

## Missing References

无重大遗漏。Related work 覆盖全面，包括最新的 ActTail (2026)、WiSparse (2026)、SVD-CSP (2026) 等。可考虑补充：
- Mirzadeh et al., 2024 ("ReLU Strikes Back") 已引用 ✓
- 近期 structured sparsity 加速工作（如 Triton-based sparse kernels）可在 Future Work 中提及。

---

## Questions for Authors

**Q1**: §4.5 中 K=1 在 50% 反而优于 K=4 (34.85 vs 44.23)，作者如何解释这一反常结果？这是否暗示 train-inference mismatch 在高 sparsity 下主导了 performance，使得整个 K-curve 分析在 50% 下失效？

**Q2**: C1 ablation 中 BCE+Gumbel (32.22) 劣于 standard BCE (27.97)——作者认为 Gumbel relaxation 对 BCE 有害的根本原因是什么？如果 Gumbel 对 KL 有益但对 BCE 有害，这是否说明 Gumbel 的作用不仅是 relaxation，还与 KL loss landscape 有特定的协同效应？

**Q3**: 知识任务退化（MMLU −5.2pp）和 commonsense 改进是否可以通过简单的 task-aware allocation（如 constraint experiment 中的 remove-valley）在推理时无额外训练成本地修复？如果可以，是否应该将 "KL predictor + task-aware allocation" 作为推荐配置？

**Q4**: Table 5 中 STE 在 30% 的实际 sparsity 只有 20.8%——如果将 STE 的 target 提高到补偿 undershoot（如设置 target 40% 以达到实际 30%），STE 的 PPL 是否仍然显著劣于 Gumbel？


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2328 · 2026-05-24T04:29:55.388404+00:00_

Reviewer 1 审稿意见已收到。评分 3.5（Borderline Conference）。

核心发现：
- **N1 [critical]**：§4.5 signal type vs coupling scope 分解被 train-inference mismatch 混淆，claim 超出证据
- **N2 [critical]**：MMLU/GSM8K 系统性退化缺乏因果机制分析
- **W1-W4**：C1 ablation 残余 confound、MSE baseline 公平性、n=3 统计力度不足、WikiText 同源性

等待 Reviewer 2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 204

## Round 204

2 recorded events


### User

_source line 2329 · 2026-05-24T04:29:57.916191+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**总结**：Overall 3.5（Borderline Conference）。

核心发现：
- **PPL 改进令人信服**（14.5%, 3-seed, CI 不重叠），跨架构泛化
- **两个 critical 问题**：(1) §4.5 signal type vs coupling scope 分解被 train-inference mismatch 混淆，但 Abstract/Conclusion 中的表述未相应降级；(2) MMLU/GSM8K 系统性退化缺乏因果分析
- **四个 warning 问题**：C1 ablation 残余 confound、MSE baseline 可能未最优配置、n=3 对高方差指标不足、WikiText 同源性
- **主要优势**：实验框架多角度严谨、论文异常坦诚、方法简洁实用、taxonomy 有概念价值

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2330 · 2026-05-24T04:30:05.814333+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 提交后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 205

## Round 205

6 recorded events


### User

_source line 2331 · 2026-05-24T04:31:53.141900+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 审稿意见：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs

---

## Paper Summary

本文提出使用输出分布蒸馏（forward KL divergence）替代传统 per-neuron BCE 来训练 SwiGLU LLM 的上下文稀疏性预测器。核心方法包括：冻结基模型 + 每层独立 2-layer MLP 预测器 + Gumbel-Sigmoid 松弛 + 几何惩罚调度实现目标稀疏度。在 LLaMA-3.1-8B 上，KL 预测器在 30% 稀疏度下相比 TEAL 降低 14.5% PPL。论文还提出了一个二维分类法（correction granularity × training signal coupling），分析 KL 相对 BCE 的梯度耦合机制，并通过大量消融实验研究了设计空间。

---

## Strengths

**S1. 系统性的实验设计与消融分析**
论文的实验设计非常扎实：3-seed means with standard deviations, target-swap ablation (Table 3), per-layer coupling breadth sweep (Figure 2), compensation冗余性分析 (Table 4), OOD评估 (Appendix D), 以及跨架构验证 (Mistral-7B, Qwen-2.5-14B)。每个 claim 都有对应的 controlled experiment 支撑。附录包含约 20 个补充实验（Appendix A–W），展示了极为彻底的验证工作。

**S2. 有价值的梯度分析（§3.6）**
§3.6 对比了 BCE 和 KL 的梯度结构：BCE 梯度仅依赖单个 neuron $j$，而 KL 通过下游 Jacobian $\partial \hat{p}_v / \partial g^{(l)}_j$ 将每个 neuron 的 mask 决策与所有其他 neuron 的输出效应耦合。这一分析为"为什么 KL 能发现更好的 mask"提供了直觉上的解释，虽然不是严格的理论结果，但对读者理解方法差异很有帮助。

**S3. 实用的二维分类法（Table 1）**
将已有学习型稀疏方法沿 correction granularity（per-token vs. per-corpus）和 training signal coupling（decomposed/local/coupled）两个维度组织，清晰定位了本文方法的位置，并指出设计空间中未被探索的组合。这对社区有参考价值。

**S4. 诚实的局限性讨论**
论文坦诚报告了知识任务退化（MMLU -12.7pp, GSM8K 几乎崩塌）、50% 稀疏度下所有方法均失效、以及 wall-clock speedup 未测量等问题。这种透明度值得肯定。

**S5. Target-swap ablation 设计精巧（Table 3）**
通过让 BCE 预测器使用 KL 发现的 oracle mask 进行训练，巧妙地分离了"mask 质量"和"训练目标"的贡献。结果表明 KL 发现的 mask targets 可以迁移到 BCE，PPL 从 13.13 降至 11.79，证实了 mask 质量本身是关键因素。

---

## Weaknesses

**W1. [Major] 与 MaskLLM 的新颖性区分不够充分**

核心 recipe（frozen model + learnable mask + forward KL + Gumbel relaxation）与 MaskLLM (Fang et al., 2024) 高度重合。论文在 §2 中承认了这一点：*"Unlike MaskLLM...which applies KL to static N:M weight masks, we address contextual activation sparsity."* 但"contextual vs. static"的区分未被充分论证为足够的独立贡献：

- MaskLLM 的 KL + Gumbel 训练框架是否可以直接扩展到 contextual 设置，只需将 static mask parameters 替换为 input-dependent predictor？如果是，方法学贡献主要是 engineering 而非 research。
- §3.6 的梯度分析是 contextual 设置特有的（因为 mask 是 hidden state 的函数），但该分析是基于 chain rule 的直接推导，理论深度有限。
- 论文未讨论从 static 到 contextual 的扩展中遇到了哪些 non-trivial 的技术挑战。

建议：明确列出 contextual setting 引入的 unique challenges（如泛化到 unseen inputs、cross-layer coordination 的动态性、predictor 容量与表达力的 trade-off），并讨论 MaskLLM 框架无法直接处理这些挑战的原因。

**W2. [Major] 知识任务退化严重但分析不足**

Table 2 显示 30% 稀疏度下：
- MMLU: 40.7 (dense) → 28.0 (KL uniform)，降幅 31%
- GSM8K: 19.9 → 0.2，几乎完全崩塌

这是非常严重的实际问题。论文给出的解释主要有两个：
1. 训练数据组成（§4.3, Appendix V）：C4-trained predictor achieves comparable MMLU (40.6%) but worse GSM8K (4.1% vs. 7.4%)——说明训练数据不是唯一原因。
2. Task-dependent coupling effects（§4.5）：per-layer controls 显示 commonsense 和 knowledge 任务对 coupling 的敏感度不同。

但论文未回答关键问题：**为什么 output-distribution alignment（KL）这个似乎更优的目标反而导致知识任务严重退化？** 如果 KL 发现了更好的 mask（PPL 更低），为什么这些 mask 不能保留知识能力？这暗示 KL 优化的 PPL 与下游 knowledge task 之间存在根本性的 misalignment，但论文未深入分析。

**W3. [Major] "Primary design dimension" overclaimed**

论文在 §4.5 和 abstract/contributions 中声称 training signal coupling 是 "the primary design dimension"。但证据只比较了 Table 1 taxonomy 中的两个维度（correction granularity × signal coupling）。其他潜在重要的设计维度未被系统比较：
- Predictor capacity（bottleneck dimension d_b, 目前固定为 128）
- Training data selection（仅在 Appendix V 中简短探索）
- Training duration（Appendix B.2 显示 convergence，但未探索 over-training effects）
- Sparsity allocation strategy（global top-k vs. per-layer budgets）

"Primary" 这个断言隐含了对所有设计维度的 exhaustive comparison，但实际上只比较了两个。建议改为 "a key design dimension" 或限定 scope 为 "among the two dimensions in our taxonomy"。

此外，§4.5 自身也承认了 confounding：per-layer KL 实验中 train-inference mismatch（K=1 masks 1/32 layers during training vs. all 32 at inference）、per-layer update count disparity 都可能混淆结论。在 confounding 未完全解决的情况下做出"primary"断言不够审慎。

**W4. [Moderate] 无 wall-clock 推理加速结果**

对于以推理效率为动机的论文，完全缺少 wall-clock 测量是显著缺陷。Appendix A 报告了 throughput overhead（KL-sparse pipeline 增加 6.4% 开销），但这是预测器本身的开销，不是最终的端到端加速。论文明确承认 *"wall-clock speedup requires sparse kernel support not addressed here"*（page 8），但这使得读者无法评估方法的实际影响力。

与之对比，TEAL 等 training-free 方法虽然质量更差但可以直接在现有 sparse kernels 上运行。一个自然的问题是：KL 预测器发现的 mask patterns（非结构化 top-k）是否与现有 sparse compute primitives 兼容？

**W5. [Moderate] Contribution labels "Analytical" 用法非标准**

C3 和 C4 被标注为 "Analytical"，但其内容分别是 target-swap ablation 和 compensation redundancy 实验——这些是实验性发现，不是形式化分析/理论推导。在 ACL/EMNLP 社区，"Analytical contribution" 通常指数学推导、理论 bounds 或 formal analysis。建议改为 "Empirical" 或 "Ablation-based"，避免误导读者期待理论结果。

**W6. [Moderate] 单模型主实验，跨架构泛化不足**

所有主要实验（Tables 2-4, Figures 2-3）仅在 LLaMA-3.1-8B 上完成。跨架构验证仅有：
- Mistral-7B-v0.3: 简短提及 (§4.2)，PPL advantage 确认但 MMLU 下降
- Qwen-2.5-14B: "preliminary evaluation" (§4.2)，PPL 改善但 reasoning decline (GSM8K -19.9pp)

对于声称 *"characterizing how the training objective shapes sparsity prediction quality across architectures"* 的论文，需要更系统的跨架构评估。至少应在主实验表格中包含一个完整的第二模型结果。

---

## Questions

**Q1.** KL predictor 发现的 mask patterns 是否与现有 semi-structured sparsity formats (如 2:4 N:M sparsity) 兼容？如果不兼容，实际部署需要什么样的 kernel 支持？

**Q2.** Gumbel temperature τ 的 annealing schedule (1.0 → 0.1 over 1000 steps, Appendix C) 看起来相对 aggressive。作者是否尝试过更慢的退火方案？Figure 4 显示 final ~100 steps 有 mild loss increase，这是否表明退火过快？

**Q3.** 论文提到 predictor 参数量是基模型的 <1%（75.9M vs. 8B）。但在 30% 稀疏度下，predictor 推理需要一次完整 dense forward pass 加上 predictor inference。这是否意味着首次 token 的延迟实际上会增加？

**Q4.** Table 3 (target-swap ablation) 中 KL predictor trained on KL-derived targets 的 PPL (11.79) 和 BCE predictor trained on KL-derived targets 的 PPL (13.13) 之间的差距如何解释？如果 mask targets 相同，为什么训练目标仍然重要？这似乎暗示 KL 的优势不仅来自发现更好的 masks，还来自训练动态本身。

**Q5.** Abstract 中 "n=3" 标注的含义是 3 random seeds。但 3 seeds 对于报告 downstream task variance（尤其是 GSM8K 这种高方差任务）是否足够？Tables 中的 standard deviations 有时相当大。

---

## Missing References

论文的引用覆盖面较广，涵盖了 TEAL, CATS, MaskLLM, SPON, FastForward, DejaVu, ShadowLLM, D2DMoE, ReLU Strikes Back 等主要工作。建议补充考虑：

1. **ProSparse** (Song et al., 2024, EMNLP Findings) — 通过 progressive sparsification 在 SwiGLU 模型上激活稀疏性，与本文方法互补
2. 若有 2025-2026 年发表的 contextual sparsity + KL distillation 相关工作，应检查是否遗漏

---

## Minor Issues

- **M1.** Table 1 中存在多个 "empty" 单元格标注为未探索组合。虽然诚实，但读者可能会质疑 taxonomy 的完整性。建议简要讨论为什么这些组合未被尝试（技术上不可行？或仅是未来工作？）。

- **M2.** Figures 2 和 3 在双栏格式下较小，部分文字标签在打印时可能难以辨认。Figure 3 的 y 轴 "Wallclock Perplexity Gap" 标签建议改为更直观的名称。

- **M3.** 脚注使用较多（至少 4 个可见），部分信息（如 TEAL is deterministic, sparsity notation 等）可以整合到正文中，减少阅读碎片化。

- **M4.** §3.5 Geometric Penalty Schedule 中引入了多个超参数（ε, λ, geometric doubling），但主文未提供 sensitivity analysis。虽然 Appendix C 有详细讨论，但主文中应至少提及 robustness。

- **M5.** Conclusion 中 *"the signal type gap (0.47 PPL)"*（如果确实是此数值）与 §4.5 中报告的 9.47 PPL gap 不一致。请核实。如果是排版问题，应在camera-ready中修正。[注：此处数字可能是我从 PDF 渲染中误读，但建议作者确认。]

- **M6.** 论文在 §Y 声明使用了 Claude (Anthropic) 进行代码起草和写作辅助。这符合 ARR 2026 政策，但建议确认是否需要在 Responsible NLP Checklist 中额外声明。

---

## 格式合规性检查

- **页数限制**: 主文 8 页 (pp.1-8) ✓；Limitations 在 page 9，不计入页数 ✓；References 和 Appendix 在 page 9 之后 ✓
- **匿名性**: 标题页显示 "Anonymous ACL submission" ✓；未发现明显的自引暴露
- **Limitations 节**: 存在 ✓，覆盖 4 个要点（sparsity sweet spot, knowledge regression, evaluation scope, baseline coverage）✓
- **Abstract 长度**: 约 190-200 words，接近 200-word 限制，需确认未超限

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 实验方法论扎实，3-seed means + controlled ablations；但 "primary dimension" overclaimed 且 per-layer KL 分析存在未完全解决的 confounding |
| **Excitement** | 2.5/5 | 核心 recipe 与 MaskLLM 重叠度高，contextual 扩展属 incremental innovation；梯度分析有价值但理论深度有限；知识任务退化限制了实际影响力 |
| **Reproducibility** | 4/5 | 详细的超参数、训练设置、模型描述；代码承诺在接收后开源；Appendix 提供充分的实验细节 |
| **Confidence** | 4/5 | 熟悉稀疏性/剪枝文献及本文使用的具体方法 |

---

## Overall Assessment

**Overall: 3.0 — Findings**

**一句话总结**: 扎实的实证研究，系统地证明了 KL 蒸馏在上下文稀疏性预测中优于 BCE，但方法新颖性受限于与 MaskLLM 的高度重叠，且知识任务的严重退化未得到充分解释。

**详细判断依据**:

本文的核心贡献是 empirical 的——通过系统实验证明 output-distribution alignment (KL) 优于 per-neuron classification (BCE) 作为 contextual sparsity predictor 的训练目标。实验设计严谨，消融全面，这些都是 Findings 级别工作的优势。

然而，几个因素阻碍了 main conference 接收：
1. **方法新颖性有限**: 核心技术栈（KL + Gumbel + frozen model）直接来自 MaskLLM，contextual 扩展虽有意义但属增量创新。
2. **实际影响力受限**: 无 wall-clock 加速、知识任务严重退化、单模型主实验共同削弱了实际价值论证。
3. **部分 claims overclaimed**: "primary design dimension" 在 confounding 未完全解决的情况下使用过于绝对化的表述。

如果作者能补充 (a) 对知识任务退化的机制分析、(b) 至少一个模型的 wall-clock 结果、(c) 更准确的 contribution scope 限定，本文可能提升至 3.5 (Borderline Conference)。

---

Sources (Step 0 搜索):
- [ARR Review Form](https://aclrollingreview.org/reviewform)
- [ARR Reviewer Guidelines](https://aclrollingreview.org/reviewerguidelines)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2332 · 2026-05-24T04:32:38.128233+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的 Weaknesses:\n\n**W1. [Major] 与 MaskLLM 的新颖性区分不够充分**\n核心 recipe（frozen model + learnable mask + forward KL + Gumbel relaxation）与 MaskLLM 高度重合。\"contextual vs. static\"的区分未被充分论证为足够的独立贡献。MaskLLM 的 KL + Gumbel 框架是否可以直接扩展到 contextual 设置？§3.6 梯度分析理论深度有限。论文未讨论从 static 到 contextual 的 non-trivial 技术挑战。\n\n**W2. [Major] 知识任务退化严重但分析不足**\nMMLU: 40.7→28.0 (降幅31%), GSM8K 几乎完全崩塌。为什么 output-distribution alignment 这个看似更优的目标反而导致知识任务严重退化？如果 KL 发现了更好的 mask（PPL 更低），为什么不能保留知识能力？暗示 PPL 与 knowledge task 之间存在根本性 misalignment。\n\n**W3. [Major] \"Primary design dimension\" overclaimed**\n证据只比较了 taxonomy 中两个维度，其他设计维度（predictor capacity, training data, duration, allocation strategy）未系统比较。\"Primary\" 隐含 exhaustive comparison。§4.5 自身承认 confounding。\n\n**W4. [Moderate] 无 wall-clock 推理加速结果**\n预测器增加 6.4% 开销，无最终端到端加速。KL mask patterns 是否与现有 sparse compute primitives 兼容？\n\n**W5. [Moderate] Contribution labels \"Analytical\" 用法非标准**\nC3/C4 内容是实验性发现，不是形式化分析。\"Analytical\" 在 ACL/EMNLP 通常指数学推导/理论 bounds。\n\n**W6. [Moderate] 单模型主实验，跨架构泛化不足**\n主要实验仅在 LLaMA-3.1-8B 上完成，Mistral 和 Qwen 验证不够系统。\n\n## Reviewer 2 的 Questions:\n\n**Q1.** KL mask patterns 是否与 2:4 N:M sparsity 兼容？实际部署需要什么 kernel 支持？\n\n**Q2.** Gumbel τ annealing (1.0→0.1) 是否过快？Final ~100 steps 的 mild loss increase 是否表明退火过快？\n\n**Q3.** 30% 稀疏度下首次 token 延迟是否增加（需完整 dense forward + predictor inference）？\n\n**Q4.** Table 3 中 KL predictor (11.79) vs BCE on KL targets (13.13) 的差距如何解释？如果 mask targets 相同，为什么训练目标仍然重要？\n\n**Q5.** n=3 seeds 对高方差下游任务是否足够？\n\n## Reviewer 2 的 Overall Assessment:\n3.0 (Findings)。方法新颖性受限于 MaskLLM 重叠，知识任务退化未充分解释，无 wall-clock 加速。\n\n---\n\n请逐条回应上述 Weaknesses 和 Questions。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的 Weaknesses:\n\n**W1. [Major] 与 MaskLLM 的新颖性区分不够充分**\n核心 recipe（frozen model + learnable mask + forward KL + Gumbel relaxation）与 MaskLLM 高度重合。\"contextual vs. static\"的区分未被充分论证为足够的独立贡献。MaskLLM 的 KL + Gumbel 框架是否可以直接扩展到 contextual 设置？§3.6 梯度分析理论深度有限。论文未讨论从 static 到 contextual 的 non-trivial 技术挑战。\n\n**W2. [Major] 知识任务退化严重但分析不足**\nMMLU: 40.7→28.0 (降幅31%), GSM8K 几乎完全崩塌。为什么 output-distribution alignment 这个看似更优的目标反而导致知识任务严重退化？如果 KL 发现了更好的 mask（PPL 更低），为什么不能保留知识能力？暗示 PPL 与 knowledge task 之间存在根本性 misalignment。\n\n**W3. [Major] \"Primary design dimension\" overclaimed**\n证据只比较了 taxonomy 中两个维度，其他设计维度（predictor capacity, training data, duration, allocation strategy）未系统比较。\"Primary\" 隐含 exhaustive comparison。§4.5 自身承认 confounding。\n\n**W4. [Moderate] 无 wall-clock 推理加速结果**\n预测器增加 6.4% 开销，无最终端到端加速。KL mask patterns 是否与现有 sparse compute primitives 兼容？\n\n**W5. [Moderate] Contribution labels \"Analytical\" 用法非标准**\nC3/C4 内容是实验性发现，不是形式化分析。\"Analytical\" 在 ACL/EMNLP 通常指数学推导/理论 bounds。\n\n**W6. [Moderate] 单模型主实验，跨架构泛化不足**\n主要实验仅在 LLaMA-3.1-8B 上完成，Mistral 和 Qwen 验证不够系统。\n\n## Reviewer 2 的 Questions:\n\n**Q1.** KL mask patterns 是否与 2:4 N:M sparsity 兼容？实际部署需要什么 kernel 支持？\n\n**Q2.** Gumbel τ annealing (1.0→0.1) 是否过快？Final ~100 steps 的 mild loss increase 是否表明退火过快？\n\n**Q3.** 30% 稀疏度下首次 token 延迟是否增加（需完整 dense forward + predictor inference）？\n\n**Q4.** Table 3 中 KL predictor (11.79) vs BCE on KL targets (13.13) 的差距如何解释？如果 mask targets 相同，为什么训练目标仍然重要？\n\n**Q5.** n=3 seeds 对高方差下游任务是否足够？\n\n## Reviewer 2 的 Overall Assessment:\n3.0 (Findings)。方法新颖性受限于 MaskLLM 重叠，知识任务退化未充分解释，无 wall-clock 加速。\n\n---\n\n请逐条回应上述 Weaknesses 和 Questions。"
  }
}
```

</details>

---


### Tool result

_source line 2333 · 2026-05-24T04:33:18.159921+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 40031
}
```

</details>

---


### Tool call

_source line 2334 · 2026-05-24T04:33:18.311241+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的 Must-Fix 问题:\n\n**N1** [critical] §4.5 Per-Layer KL 分解的 claim 超出证据支撑\n- Abstract/§4.5/Conclusion 反复强调 \"signal type gap (9.47 PPL) exceeds coupling breadth range (2.08 PPL)\"。但 train-inference mismatch 严重混淆（K=1 训练 1/32 层 mask vs 推理 32/32 层）。50% 下 K=1 (34.85) 优于 K=4 (44.23) 直接否定了分解在高 sparsity 下的有效性。这是第一条 contribution，但 Abstract/Conclusion 表述未降级。\n- 建议：Abstract/Conclusion 加 \"confounded by train-inference mismatch\" 限定；将 9.47 vs 2.08 从 claim 降级为 observation；设计无 mismatch 控制实验。\n\n**N2** [critical] 知识任务系统性退化未充分分析因果机制\n- MMLU −5.2pp、14B GSM8K −19.9pp。归因于 \"forward KL mode-covering\" 但：\n  (a) C4 control 单 seed；\n  (b) \"mode-covering sacrifices rare activations\" 停留在直觉，无实证；\n  (c) Constraint 实验显示 remove valley → MMLU +3.4pp，说明 allocation 是部分原因，与 \"KL structural property\" 解释有张力。\n- 建议：C4 control 增至 3-seed；neuron-level 归因分析；区分 allocation-induced vs loss-inherent regression。\n\n## Reviewer 1 的 Should-Fix 问题:\n\n**W1** [warning] C1 Target-Swap Ablation 残余 confound\n- Soft→hard binarization 丢失 ranking info；s42 oracle 来自 non-seed-matched checkpoint（gap 0.65pp vs s123/s456 ≤0.03pp）；BCE+Gumbel (32.22) 劣于 BCE (27.97) 暗示 Gumbel 对 BCE 有害但对 KL 有益。\n\n**W2** [warning] MSE baseline 可能未在最优配置下评估\n- MSE 50% 2/3 seeds 崩溃。\"Same hyperparameters\" 可能 unfairly disadvantage MSE。建议为 MSE 做 λ_max 小搜索。\n\n**W3** [warning] n=3 seeds 对部分 claim 支撑不足\n- MMLU 30% global σ=9.5pp, 95% CI ≈ [11.9, 59.5]；Qwen-14B GSM8K σ=5.3pp；Mistral ARC-c σ=6.4pp。\n\n**W4** [warning] WikiText-2 eval / WikiText-103 training 同源性\n- C4 OOD 30% 仅 2-seed；C4 uniform CV=6.3% vs in-domain 0.2%；C4 缺 TEAL baseline。\n\n## Reviewer 1 的 Questions:\n\n**Q1**: K=1 在 50% 优于 K=4 如何解释？K-curve 在 50% 下是否失效？\n**Q2**: BCE+Gumbel (32.22) 劣于 BCE (27.97) 的根本原因？Gumbel 与 KL 有特定协同效应？\n**Q3**: 知识退化是否可通过 task-aware allocation（remove-valley）在推理时修复？\n**Q4**: STE 若补偿 undershoot（target 40% 以达实际 30%），PPL 是否仍劣于 Gumbel？\n\n## Reviewer 1 的 Overall Assessment:\n3.5 (Borderline Conference)。PPL 改进令人信服，但知识退化和 §4.5 confound 削弱贡献。\n\n---\n\n请逐条回应上述 Must-Fix、Should-Fix 问题和 Questions。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的 Must-Fix 问题:\n\n**N1** [critical] §4.5 Per-Layer KL 分解的 claim 超出证据支撑\n- Abstract/§4.5/Conclusion 反复强调 \"signal type gap (9.47 PPL) exceeds coupling breadth range (2.08 PPL)\"。但 train-inference mismatch 严重混淆（K=1 训练 1/32 层 mask vs 推理 32/32 层）。50% 下 K=1 (34.85) 优于 K=4 (44.23) 直接否定了分解在高 sparsity 下的有效性。这是第一条 contribution，但 Abstract/Conclusion 表述未降级。\n- 建议：Abstract/Conclusion 加 \"confounded by train-inference mismatch\" 限定；将 9.47 vs 2.08 从 claim 降级为 observation；设计无 mismatch 控制实验。\n\n**N2** [critical] 知识任务系统性退化未充分分析因果机制\n- MMLU −5.2pp、14B GSM8K −19.9pp。归因于 \"forward KL mode-covering\" 但：\n  (a) C4 control 单 seed；\n  (b) \"mode-covering sacrifices rare activations\" 停留在直觉，无实证；\n  (c) Constraint 实验显示 remove valley → MMLU +3.4pp，说明 allocation 是部分原因，与 \"KL structural property\" 解释有张力。\n- 建议：C4 control 增至 3-seed；neuron-level 归因分析；区分 allocation-induced vs loss-inherent regression。\n\n## Reviewer 1 的 Should-Fix 问题:\n\n**W1** [warning] C1 Target-Swap Ablation 残余 confound\n- Soft→hard binarization 丢失 ranking info；s42 oracle 来自 non-seed-matched checkpoint（gap 0.65pp vs s123/s456 ≤0.03pp）；BCE+Gumbel (32.22) 劣于 BCE (27.97) 暗示 Gumbel 对 BCE 有害但对 KL 有益。\n\n**W2** [warning] MSE baseline 可能未在最优配置下评估\n- MSE 50% 2/3 seeds 崩溃。\"Same hyperparameters\" 可能 unfairly disadvantage MSE。建议为 MSE 做 λ_max 小搜索。\n\n**W3** [warning] n=3 seeds 对部分 claim 支撑不足\n- MMLU 30% global σ=9.5pp, 95% CI ≈ [11.9, 59.5]；Qwen-14B GSM8K σ=5.3pp；Mistral ARC-c σ=6.4pp。\n\n**W4** [warning] WikiText-2 eval / WikiText-103 training 同源性\n- C4 OOD 30% 仅 2-seed；C4 uniform CV=6.3% vs in-domain 0.2%；C4 缺 TEAL baseline。\n\n## Reviewer 1 的 Questions:\n\n**Q1**: K=1 在 50% 优于 K=4 如何解释？K-curve 在 50% 下是否失效？\n**Q2**: BCE+Gumbel (32.22) 劣于 BCE (27.97) 的根本原因？Gumbel 与 KL 有特定协同效应？\n**Q3**: 知识退化是否可通过 task-aware allocation（remove-valley）在推理时修复？\n**Q4**: STE 若补偿 undershoot（target 40% 以达实际 30%），PPL 是否仍劣于 Gumbel？\n\n## Reviewer 1 的 Overall Assessment:\n3.5 (Borderline Conference)。PPL 改进令人信服，但知识退化和 §4.5 confound 削弱贡献。\n\n---\n\n请逐条回应上述 Must-Fix、Should-Fix 问题和 Questions。"
  }
}
```

</details>

---


### Tool result

_source line 2335 · 2026-05-24T04:33:19.669196+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1357
}
```

</details>

---


### Assistant

_source line 2336 · 2026-05-24T04:33:24.071177+00:00_

交叉分享已派发。两位 Reviewer 正在互相审阅对方的意见并逐条回应，等待结果返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 206

## Round 206

2 recorded events


### User

_source line 2337 · 2026-05-24T04:33:26.631820+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论：Overall 3.0 (Findings)**

核心评价：
- **Soundness 3.5/5** — 实验设计扎实（3-seed, controlled ablations），但 "primary design dimension" overclaimed 且存在未解决的 confounding
- **Excitement 2.5/5** — 核心 recipe 与 MaskLLM 高度重叠（KL + Gumbel + frozen model），contextual 扩展属增量创新
- **Overall 3.0/5** — 适合 Findings

**三个 Major Weaknesses**：
1. 与 MaskLLM 新颖性区分不足（共享 frozen model + KL + Gumbel recipe，contextual vs. static 的技术挑战未充分论证）
2. 知识任务严重退化（MMLU -31%, GSM8K 几乎崩塌）缺乏机制解释
3. "Primary design dimension" 在 confounding 未解决的前提下 overclaimed

**两个 Moderate Weaknesses**：无 wall-clock 加速结果、单模型主实验限制泛化性论证

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2338 · 2026-05-24T04:33:31.097368+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 207

## Round 207

2 recorded events


### User

_source line 2339 · 2026-05-24T04:34:49.912636+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 意见的逐条回应

---

### Weaknesses 回应

**[AGREE] R2-W1: 与 MaskLLM 的新颖性区分不够充分**
部分同意。论文在 §2 (related_work.tex L21-23) 列出了三个区别：(a) per-token vs static masks, (b) cross-layer allocation interaction, (c) distribution shift robustness。但 R2 指出的核心问题是对的——论文没有讨论从 static 到 contextual 的 **技术挑战**。MaskLLM 的 Gumbel-Softmax 在 static 设置中直接优化固定的 mask 参数，而本文需要训练一个 predictor network 来泛化到 unseen inputs，这在优化景观上是不同的（predictor 的泛化误差 vs. 直接优化的 oracle masks）。但论文确实没有形式化这一区别。不过我要补充一点：MaskLLM 处理的是 N:M weight sparsity（结构化、静态），而本文处理的是 contextual activation sparsity（非结构化、动态），这是两个不同的子领域，目标读者群体不完全重叠，因此 "recipe 重合" 的严重性应适度评估。论文的真正贡献在于 empirical characterization（5 个 loss 的系统比较 + C1 ablation + K-curve 分解），这一点不依赖于与 MaskLLM 的区分。

**[AGREE] R2-W2: 知识任务退化严重但分析不足**
完全同意。这与我的 N2 一致。论文的解释（"forward KL mode-covering sacrifices rare reasoning-critical activations"）停留在直觉层面。特别值得注意的是：
- §4.2 Task-Type Split 报告 MMLU 40.7±1.3 (uniform) vs TEAL 45.86 (−5.2pp)
- 但 Appendix T (Table 20) 的 constraint experiment 显示 remove-valley → MMLU 44.0 (+3.4pp)，几乎恢复到 TEAL 水平
- 这说明退化可能主要是 **allocation pattern** 的问题而非 KL loss 的固有缺陷

R2 提出的追问很尖锐："如果 KL 发现了更好的 mask（PPL 更低），为什么不能保留知识能力？" 这暗示 PPL 改进和知识任务之间可能存在 Pareto trade-off，而不是 PPL 的绝对改进。论文应该正面讨论这个可能性。

不过我认为 R2 引用的 "MMLU: 40.7→28.0 (降幅31%)" 有误导性——40.7 是 30% sparsity, 28.0 是 50% sparsity，这是跨 sparsity level 的比较，不是同一条件下的退化。在同一条件（30% uniform）下，KL MMLU 40.7 vs TEAL 45.86 的退化幅度是 −5.2pp（11.3%），而非 31%。

**[REBUT] R2-W3: "Primary design dimension" overclaimed**
部分反驳。论文的 claim "Output-distribution alignment is the primary design dimension" 确实有 overclaim 的嫌疑，这与我的 N1 观点一致。但 R2 说 "证据只比较了 taxonomy 中两个维度" 不完全准确：
- Table 5 (§4.4) 系统比较了 **5 个 loss function**（Forward KL, Reverse KL, JSD, BCE, MSE），不仅是两个维度
- Appendix B (Table 6) 测试了 predictor capacity（d_b = 64/128/256/512）
- Appendix B.2 (Table 8) 测试了 training duration（200-1000 steps）
- §4.2 比较了 allocation strategy（global vs uniform）
- Appendix B.1 (Table 7) 测试了 temperature schedule 变体

所以论文确实 systematically varied 了多个设计维度，只是 "primary" 这个词暗示了穷尽性比较。我建议将 "primary" 改为 "a critical" 或 "among the most important"。但证据基础比 R2 描述的更宽。

**[AGREE] R2-W4: 无 wall-clock 推理加速结果**
同意这是一个实际局限。但我认为论文已经诚实地处理了这一点：Abstract 末尾（"wall-clock speedup requires sparse kernel support not addressed here"）、Introduction (L18)、Appendix A、和 Limitations 都明确说明了。对于一篇定位为 "empirical study characterizing how the training objective shapes sparsity prediction quality" 的论文（Introduction L18），不提供加速结果是可以接受的——前提是论文不 claim 加速。论文确实没有。

**[AGREE] R2-W5: "Analytical" contribution labels 非标准**
同意。Introduction L25-27 将 C3（target-swap ablation）和 C4（compensation redundancy）标记为 "Analytical"，但这些都是实验发现而非数学分析。在 ACL/EMNLP 语境下，"Analytical" 通常指理论推导、complexity bounds 等。建议改为 "Empirical-analytical" 或直接用 "Empirical"。这是一个 presentation issue，不影响贡献本身的实质。

**[REBUT] R2-W6: 单模型主实验，跨架构泛化不足**
部分反驳。R2 说 "Mistral 和 Qwen 验证不够系统"，但：
- Mistral-7B-v0.3 有 **3-seed 完整评估**（PPL + 6 个 downstream tasks, Table 16/Appendix N），PPL 泛化 −17.3%，commonsense 改进（WG +6.7pp），知识任务 tied（MMLU 43.3 vs 43.5）
- Qwen-2.5-14B 有 3-seed GSM8K + 单 seed 其他指标（Table 13/Appendix K）
- 三个架构覆盖了 GQA (LLaMA), GQA+sliding window (Mistral), 不同 d_ff 维度 (Qwen-14B 5120→18944)

对于一篇 8 页限制的论文，3 个架构（7B-14B 范围）的验证是合理的。Qwen 的评估确实可以更系统（增加更多 seed），但现有证据已经覆盖了主要的架构变体。真正缺失的是 **更大规模**（如 70B）的验证，这一点 R2 没有提到。

---

### Questions 回应

**[REBUT] R2-Q1: KL mask patterns 是否与 2:4 N:M sparsity 兼容？**
R2 的问题合理但超出了论文的 scope。论文处理的是 unstructured activation sparsity（与 TEAL 相同），而 2:4 N:M 是 structured weight sparsity pattern。这是两个不同的问题设定。MaskLLM 处理 N:M weight masks，本文处理 contextual activation masks——不应期望 activation mask 直接满足 N:M 结构约束。实际部署需要的是 block-sparse kernel（如 Triton block-sparse）而非 2:4 N:M，因为 activation mask 是 input-dependent、layer-varying 的。论文在 Appendix A (appendix.tex L32-33) 提到了这一点。

**[REBUT] R2-Q2: τ annealing 是否过快？**
论文在 Appendix B.1 (Table 7) 已经回答了这个问题：fixed τ=0.5 (PPL 11.861) 实际上 **略优于** linear 1.0→0.1 (PPL 11.963)，而 fixed τ=0.1 (PPL 12.072) 最差。整体变化范围 <1.8%，说明温度策略对最终结果影响很小。Final ~100 steps 的 mild loss increase（Appendix C, appendix.tex L144-145）被解释为 masks 趋向 binary 时 discrete rounding noise 的正常表现，而非退火过快的症状。如果退火过快，我们预期会看到更大的 loss spike，但实际观察到的只是 mild increase。

**[AGREE] R2-Q3: 首次 token 延迟**
合理的工程问题。论文的 predictor 在每一层取 x^(ℓ)（attention 后的 hidden state）作为输入，然后预测该层的 mask，因此可以与 base model 的 layer-by-layer forward pass 并行或串行执行。但论文的 latency 测量（Appendix A, Table 5）只报告了 steady-state throughput（100 forward passes 的平均），没有单独报告 first-token latency。对于 autoregressive generation 的 prefill 阶段，predictor 在每个 token 位置独立运行，所以 first-token 不应有额外开销（相对于后续 token）。但这一点论文确实没有明确说明。

**[REBUT] R2-Q4: Table 3 中数字引用有误**
R2 引用 "KL predictor (11.79) vs BCE on KL targets (13.13)"，但这些数字与论文 Table 3 不匹配：
- 50% s42: C1 PPL = **11.96**, KL PPL = **11.96**（几乎完全匹配，gap ≤0.79pp across all metrics）
- 30% s42: C1 PPL = 9.45, KL PPL = 8.82（gap 0.63pp，但 s42 oracle 来自 non-seed-matched earlier checkpoint）
- 30% s123/s456（seed-matched oracles）: C1 PPL 8.84/8.82, KL PPL 8.83/8.79（gap ≤0.03pp）

论文中 **不存在 13.13** 这个数值。11.79 出现在 Table 5 (ablation) 作为 50% 的 forward KL PPL，不在 Table 3 (C1 ablation) 中。R2 可能混淆了不同 table 的数字。实际上 C1 ablation 的结论是 mask patterns **高度可迁移**——在 seed-matched 条件下 gap ≤0.03pp，这恰恰支持了论文的 claim，而非质疑它。

**[AGREE] R2-Q5: n=3 seeds 对高方差 downstream tasks 是否足够**
完全同意，与我的 W3 一致。PPL 的 σ=0.02 (CV=0.2%) 使 3 seeds 完全足够。但 MMLU 在 30% global 下 σ=9.5pp (CV=26.6%)、Qwen GSM8K σ=5.3pp (CV=16.5%)、Mistral ARC-c σ=6.4pp (CV=14.3%) 意味着 3 seeds 无法产生有意义的置信区间。论文在 §4.2 中正确地将 PPL 作为 primary metric，但在多处对高方差 downstream 指标做了 directional claims，应加上 "statistically indeterminate" 限定语。

---

### 综合评价

R2 的整体打分 3.0 (Findings) 在我看来偏低。R2 最有力的论点是 W2（知识任务退化分析不足）和 W5（contribution labeling），但 W1（MaskLLM 重叠）和 W6（跨架构泛化不足）被过度强调：

- W1 忽视了论文真正的贡献是 **empirical characterization**（5 loss 比较 + ablation framework），不是 method novelty
- W6 低估了 3 个架构、7-14B 范围、含 3-seed Mistral 评估的充分性
- Q4 引用了论文中不存在的数字 (13.13)，这降低了该 question 的可信度

我维持 3.5 (Borderline Conference) 的评分。论文的 PPL 改进真实可信，实验框架设计有价值，坦诚度高于平均水平。主要扣分在于 §4.5 的 confounded decomposition 被 overclaim（我的 N1）和知识任务退化缺乏深入分析（我的 N2 / R2-W2）。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2340 · 2026-05-24T04:35:23.569688+00:00_

收到 Reviewer 1 的交叉回应。

R1 对 R2 的 6 个 Weakness 中：3 个 [AGREE]（W2/W4/W5）、3 个 [REBUT]（W1 部分/W3 部分/W6 部分）。R1 维持 3.5 分，认为 R2 的 3.0 偏低——主要理由是 R2 在 W1 和 W6 上过度强调，且 Q4 引用了不存在的数字。

等待 Reviewer 2 对 Reviewer 1 意见的交叉回应。收齐后评估收敛性，决定是否进入 Round 2 或直接合成报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 208

## Round 208

2 recorded events


### User

_source line 2341 · 2026-05-24T04:35:26.120428+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 意见的逐条回应。核心判断：

- R2-W2（知识任务退化）和 R2-W5（contribution labeling）完全同意
- R2-W3（overclaim）部分同意但指出论文实际比较了更多维度
- R2-W1（MaskLLM 重叠）和 R2-W6（跨架构不足）认为被过度强调
- R2-Q4 引用了论文中不存在的数字 (13.13)，标注了这一事实性错误
- 维持 3.5 评分，认为 R2 的 3.0 偏低

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2342 · 2026-05-24T04:36:07.207298+00:00_

Reviewer 1 交叉回应已收到。记录关键共识/分歧点：

| 议题 | R1 立场 | 状态 |
|------|---------|------|
| R2-W2 知识任务退化 | 完全同意 | **共识** |
| R2-W5 Analytical 标签 | 完全同意 | **共识** |
| R2-W3 overclaim | 部分同意，补充更多证据 | **部分分歧** |
| R2-W1 MaskLLM 区分 | 认为过度强调 | **分歧** |
| R2-W6 跨架构泛化 | 认为过度强调 | **分歧** |
| R2-Q4 数字引用 | 指出事实性错误 (13.13 不存在) | **R2 需回应** |
| 评分 | R1: 3.5 vs R2: 3.0 | **差 0.5** |

等待 Reviewer 2 的交叉回应。收到后进行收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director"
}
```

</details>

---


## Round 209

## Round 209

16 recorded events


### User

_source line 2343 · 2026-05-24T04:39:54.730802+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

---

**[AGREE] R1-N1: §4.5 Per-Layer KL 分解 claim 超出证据支撑**

完全同意。这也是我在自己审稿中提出的核心问题之一（我的 W3）。R1 的分析比我更为精确，补充几个要点：

1. **50% 异常是最强反证。** R1 指出 50% 下 K=1 (34.85) 优于 K=4 (44.23)，这直接否定了 "coupling breadth 单调有益" 的叙事。如果更多 coupling 在 30% 有利但在 50% 有害，那么 "signal type is the primary dimension" 的结论是 sparsity-conditional 的，不能一般化。论文在 §4.5 承认了 "the 50% failure where TEAL K=1 (14.85) outperforms K=∞ (14.42)"，但这一承认埋在行文中，未在 Abstract/Conclusion 中体现。

2. **Confounding 比论文承认的更严重。** K=1 训练时每步仅更新 1/32 层的 predictor，而推理时所有 32 层同时激活。这不仅是 train-inference mismatch，还涉及 update frequency 差异（K=1 每个 predictor 仅看到 ~31 updates vs E2E 的 1000 updates）。Appendix S 的 K=4 控制实验部分缓解了这一问题，但 K=4 本身仍有 4/32 vs 32/32 的 mismatch。**要真正分离 signal type 和 coupling scope，需要一个无 mismatch 的实验：例如训练所有 32 层的 predictor 但 loss 仅回传到 K 层。**

3. **数值疑似不一致。** 我在第一轮审稿中已标记（M5）：Conclusion 中 "signal type gap (0.47 PPL)" 与 §4.5 中的 "K=1 KL 9.05 vs. MSE 18.52: 9.47 PPL" 可能存在排版错误（0.47 vs 9.47）。如果确实是 0.47，则 "exceeds coupling breadth range (2.08 PPL)" 的断言在数学上不成立。

**建议与 R1 一致**：Abstract/Conclusion 必须加 "confounded by train-inference mismatch" 限定；将结论降级为 observation；设计无 mismatch 的控制实验。

---

**[AGREE] R1-N2: 知识任务退化未充分分析因果机制**

完全同意，并补充 R1 未提及的一个发现：

1. **R1 的三个具体论点均成立。** (a) C4 control 单 seed 不足以支撑因果推断；(b) "mode-covering sacrifices rare activations" 仅为直觉猜测；(c) remove-valley → MMLU +3.4pp 说明 allocation pattern 是部分原因。

2. **补充证据：Appendix S 的 K=4 MMLU 异常进一步支持 R1 的判断。** 论文在 Appendix S (Table 19) 中报告 K=4 的 MMLU 系统性超过 E2E ("MMLU: K=4 systematically exceeds E2E across all 3 seeds")。论文自身在 Appendix T 中将此归因于 K=4 产生近均匀的 per-layer sparsity (std=0.001)，从而 "inherently removes the valley, producing MMLU≈43.5 comparable to the remove-valley condition (44.0)"。**这直接说明知识任务退化的很大一部分原因是 allocation pattern（valley 结构），而非 KL loss 的固有属性。** 论文的两个解释（"KL mode-covering" vs "allocation-induced"）之间存在未解决的张力。

3. **Seed variance 使分析更加困难。** 从 Table 20 (Appendix T) 可以看到 s42 baseline MMLU = 40.6，而 Table 2 的 3-seed mean 为 ~28.5。这意味着 s42 是一个高 MMLU 异常种子，其他种子的 MMLU 可能低至 ~22。在如此极端的 seed variance 下，任何基于单 seed (s42) 的因果分析都不可靠。

**建议与 R1 一致**：C4 control 增至 3-seed；明确区分 allocation-induced vs loss-inherent regression；neuron-level 归因分析（哪些 neuron 在 KL vs BCE 下被保留/丢弃，这些 neuron 与知识存储的关系）。

---

### Should-Fix 问题

---

**[AGREE] R1-W1: Target-Swap Ablation 残余 confound（部分同意）**

同意 R1 提出的三个 confound 中的两个，对第一个持保留意见：

1. **Soft→hard binarization（部分保留）。** R1 认为 binarization 丢失 ranking info。但推理时 mask 最终都是 hard binary（top-k），所以 binarized oracle 是 inference-relevant 的评估标准。连续 importance scores 的 ranking info 仅在 training 中对梯度有影响，不影响最终 mask 质量评估。不过，如果连续 scores 中包含"接近 threshold 的 neuron 有歧义"的信息，那么 binarization 确实丢失了这部分信号。此 confound 存在但可能影响较小。

2. **s42 oracle provenance（同意）。** s42 oracle 来自非 seed-matched checkpoint，gap 0.65pp vs seed-matched ≤0.03pp。论文在 Table 3 脚注中承认了这一问题，但未量化其对结论的影响。建议在 seed-matched 条件下重做 s42 实验。

3. **BCE+Gumbel (32.22) 劣于 BCE (27.97)（同意，且认为重要）。** 这一观察暗示 Gumbel relaxation 与 KL 之间存在特定协同效应，而非 Gumbel 本身的普遍优势。在 BCE 的 decomposed 梯度结构下，Gumbel 引入的随机扰动只增加噪声（每个 neuron 的梯度独立，无法利用邻居的探索信号）；但在 KL 的 coupled 梯度结构下，Gumbel 的探索使得模型能发现组合上更优的 mask patterns。**这个 Gumbel-KL 协同效应本身值得在论文中讨论，因为它实际上是对 §3.6 梯度分析的一个有力补充证据。** 当前论文完全没有讨论这一现象。

---

**[AGREE] R1-W2: MSE baseline 可能未在最优配置下评估**

同意。Appendix G 描述了 MSE baseline 使用与 KL 完全相同的超参数配置。但 MSE 的梯度 magnitude 比 KL 大约 5 倍（Appendix G/H），这意味着 MSE 可能需要更小的学习率。当 2/3 seeds 在 50% 下崩溃时（Appendix F 提及），这更像是超参数不匹配而非 MSE 方法本身的缺陷。

不过，我认为这不影响核心结论的方向性：即使 MSE 在最优超参数下表现更好，KL 的 coupled gradient 结构（§3.6）仍然是理论上更优的选择。但 **PPL 差距的量化（18.52 vs 9.05）可能被高估**，建议为 MSE 至少做一个学习率 sweep。

---

**[AGREE] R1-W3: n=3 seeds 对部分 claim 支撑不足**

完全同意。我在第一轮审稿 Q5 中也提出了相同 concern。R1 提供的具体数字更有说服力：

- MMLU 30% global σ=9.5pp → 95% CI ≈ [11.9, 59.5]（使用 t-distribution, df=2）
- 这意味着 MMLU 的 seed-level 变异远大于方法间差异

**关键区分：PPL claims 稳健，downstream claims 不稳健。** PPL σ 通常在 0.02-0.15 范围，3 seeds 足以支撑 PPL 结论。但 MMLU/GSM8K 的 σ 高达 5-10pp，3 seeds 不足以对这些 metrics 做可靠推断。论文应当明确标注哪些 claims 是 PPL-based（统计可靠）、哪些是 downstream-based（需更多 seeds）。

---

**[AGREE] R1-W4: WikiText-2 eval / WikiText-103 training 同源性（部分同意）**

同意这是一个 valid concern，但认为严重程度低于 R1 的评估：

1. **同源性是社区标准做法。** TEAL、CATS、MaskLLM 等多数对比工作也使用 WikiText 系列做 train/eval。在公平比较的意义上，使用相同 evaluation 是合理的。

2. **C4 OOD 评估存在但不充分。** Appendix D 报告了 C4 OOD 结果（PPL 16.03±0.01），确认了优势持续。但 R1 正确指出：(a) 仅 2-seed；(b) CV=6.3% 远高于 in-domain 0.2%；(c) **最关键的缺失是 C4 上缺少 TEAL baseline**，无法判断 KL 的 OOD 优势是否依然存在。

---

### Questions

---

**[AGREE] R1-Q1: K=1 在 50% 优于 K=4 如何解释？**

R1 提出了正确的问题。这一异常是 §4.5 分析的最大威胁。结合 Appendix S/T 的信息，我的推测：

在 50% 下，每层丢弃一半 neuron，cross-layer error propagation 被 KL 的 coupled gradients 放大（因为 Jacobian 乘以的 activation 有一半为零）。K=1 通过切断 cross-layer coupling 避免了这种 error cascading。但 30% 下丢弃比例较低，coupling 的信息增益超过 error propagation 的代价。

**如果此推测成立，那么 coupling 的有益性是 sparsity-conditional 的，"primary design dimension" 的 claim 需要限定为 "at moderate sparsity levels"。**

---

**[AGREE] R1-Q2: BCE+Gumbel 劣于 BCE 的根因？**

如上 W1 第 3 点所述，我认为这揭示了 Gumbel-KL 协同效应：
- **BCE+Gumbel**：Gumbel 噪声扰动每个 neuron 的独立 sigmoid 决策，但 BCE 的 per-neuron 梯度无法利用这种组合探索——噪声只是噪声。
- **KL+Gumbel**：Gumbel 噪声改变了 mask 的组合状态，KL 的 coupled gradients（通过 Jacobian）可以感知这些组合变化对输出分布的影响，从而利用噪声进行有意义的 mask space exploration。

**这是一个 R1 发现的重要观察，值得在论文中作为 §3.6 梯度分析的实证佐证加以讨论。**

---

**[AGREE] R1-Q3: 知识退化是否可通过 task-aware allocation 修复？**

Appendix T 的数据表明部分可以：remove-valley → MMLU +3.4pp, GSM8K +1.6pp。但相对 dense baseline 仍有显著差距。此外，Appendix S 显示 K=4 MMLU≈43.5 接近 dense (40.7)，甚至更高——这暗示在适当的 allocation 下知识退化可以被大幅缓解。

但这引出了一个更深层的问题：**如果 allocation 调整就能修复知识退化，那退化的原因就不是 KL loss 的固有属性，而是 E2E KL training 学到的特定 allocation pattern（valley）的副作用。** 论文需要明确区分这两种因果路径。

---

**[AGREE] R1-Q4: STE 若补偿 undershoot，PPL 是否仍劣于 Gumbel？**

同意这是一个必要的控制实验。§3.3 报告 Gumbel 比 STE 改善 33.8%（PPL 15.77→11.79 at 50%），但如果 STE 的实际 sparsity 与目标不匹配（undershoot），则部分 PPL 差距可能来自 sparsity level 差异而非 gradient quality。

论文的 §3.3 理论论证（STE 的 discontinuous gradient signals 导致 oscillation）是合理的，但需要实证支撑：**在 matched actual sparsity 下比较 STE vs Gumbel。** 如果 STE 调整 target 后仍显著劣于 Gumbel，则 gradient quality 论证成立；如果差距大幅缩小，则当前论文高估了 Gumbel 的独立贡献。

---

## 综合判断

R1 的审稿极为细致，大多数 concerns 与我的独立评估一致或互补。关键共识：

1. **§4.5 per-layer KL 分析是论文最大的方法论弱点**——两位 reviewer 均认为 confounding 未解决且 claim overclaimed。
2. **知识任务退化是第二大问题**——两位 reviewer 均认为因果分析不足，且 allocation vs loss-inherent 未分离。
3. **n=3 seeds 对高方差 metrics 不足**——PPL claims 稳健但 downstream claims 需更多 seeds。

R1 比我更准确地识别了 BCE+Gumbel anomaly 和 STE undershoot confound——这些在我的第一轮审稿中未涉及。

**我维持 Overall 3.0 (Findings) 的评分。** R1 给出 3.5 (Borderline Conference) 较我乐观半档。区别可能在于：我认为与 MaskLLM 的 novelty overlap（我的 W1）进一步限制了方法贡献，而 R1 似乎未重点关注 novelty 问题。如果仅考虑 R1 评审的维度（claim strength + experimental soundness），3.5 也是合理的。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2344 · 2026-05-24T04:40:13.382759+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 2345 · 2026-05-24T04:40:13.383258+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2346 · 2026-05-24T04:40:25.997475+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 2347 · 2026-05-24T04:40:26.148503+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2348 · 2026-05-24T04:40:26.148945+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 2349 · 2026-05-24T04:40:26.199537+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-24T04:23:37.977984+00:00\", \"completed_at\": \"2026-05-24T04:26:47.467919+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 20\", \"message\": \"最后一页仅有 3 行内容（AI Assistants 声明续），约 95% 空白。建议将 Section Y 内容上移至 page 19 末尾合并，避免审稿人翻到近乎空白页\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无 display item，第一个视觉锚点（Figure 1）出现在 page 2。虽非硬性要求，但若 Figure 1 能上移至 page 1 底部可加强第一印象\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"三个 table（Table 2/3/4）集中在同一页，视觉密度较高。Tables 本身格式良好（booktabs 风格、最优值加粗），但审稿人可能感到信息过载\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Related Work 全页纯文字，无任何 display item 或公式穿插。Related Work 段落常见此情况，但可考虑在相关处嵌入简要对比表\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Experimental Setup 全页纯文字。实验设置段落常见此情况，影响有限\"}, {\"severity\": \"info\", \"dimension\": \"page 16\", \"message\": \"Figure 7（KL vs. magnitude importance scores 热力图）尺寸偏小，mask pattern 细节在打印时可能难以辨认\"}, {\"severity\": \"info\", \"dimension\": \"page 17\", \"message\": \"Figure 8（Per-layer Jaccard distance）尺寸较小，但 bar chart pattern 仍可辨识\"}, {\"severity\": \"info\", \"dimension\": \"page 18\", \"message\": \"Figure 9（Binary mask comparison 4-panel 热力图）单 panel 尺寸较小，neuron-level 细节在低分辨率打印下可能损失。Caption 较长但信息充分\"}], \"counts\": {\"critical\": 0, \"warning\": 1, \"info\": 7}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2350 · 2026-05-24T04:40:35.132408+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 2351 · 2026-05-24T04:40:35.183094+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2352 · 2026-05-24T04:40:37.433311+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2353 · 2026-05-24T04:40:37.484384+00:00_

1	issues:
2	  # ============================================================
3	  # Round 28 — Active issues
4	  # ============================================================
5	
6	  - id: "R20-W1"
7	    summary: "Per-layer KL decomposition 的 train-inference mismatch confound 未解决"
8	    category: method
9	    severity: critical
10	    status: in_progress
11	    first_raised_round: 20
12	    last_seen_round: 28
13	    mentions:
14	      - {round: 21, reviewers: [1, 2], note: "R21 Critical。K=4 single-seed。"}
15	      - {round: 22, reviewers: [1, 2], note: "R22 N2。97.5% 精确数字不可靠。"}
16	      - {round: 24, reviewers: [1, 2], note: "R24 C1。K=1 有 32× train-inference mismatch。"}
17	      - {round: 25, reviewers: [1, 2], note: "R25 N1/N2。"}
18	      - {round: 26, reviewers: [1, 2], note: "R26 R1-N2/R2-N1。建议 stop-gradient 或更多 K 值。"}
19	      - {round: 27, reviewers: [1, 2], note: "R27 C1。K-curve 6 点中除 K=4 外均 single-seed。K=16 PPL 优势可能 seed-specific。per-layer update count confound 未解决。"}
20	      - {round: 28, reviewers: [1, 2], note: "R28 双方 AGREE critical。50% 下 K=1 PPL=34.85 vs E2E=11.84（2.94×）是 decisive evidence。K=4 在 50% 更差（44.23）。论文已有 'upper bound' 和 'exploratory' 标注，但 'may account for a substantial portion' 仍被认为对 exploratory analysis 过强。K=2/8/16 3-seed 数据已补充但 per-layer update count confound 仍未解决。"}
21	    action_items:
22	      - {round: 21, action: "K=4 3-seed", assigned_to: "main_agent", status: done}
23	      - {round: 22, action: "定性 'majority of PPL gap'", assigned_to: "paper_agent", status: done}
24	      - {round: 25, action: "限定 decomposition 为 moderate sparsity", assigned_to: "paper_agent", status: done}
25	      - {round: 25, action: "K=2/K=8/K=16 实验扩展 K-curve", assigned_to: "main_agent", status: done}
26	      - {round: 27, action: "§4.5 降级为 Exploratory Decomposition + may account for a substantial portion", assigned_to: "paper_agent", status: done}
27	      - {round: 27, action: "experiments L161 'primary design lever' → 'major factor for PPL'", assigned_to: "pa
…[truncated 18010 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---
