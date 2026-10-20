# Research conversation: I need to check all figure environments in the paper's LaTeX source to see which ones use `figure*` vs `figure`, and wha

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-aa7d450a33c4a6692.jsonl`
- **Structured JSON:** [`eec144d31aebcd7ed64b.json`](../../sessions/ee/eec144d31aebcd7ed64b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

23 recorded events

### User

_source line 1 · 2026-05-25T04:45:35.442Z_

I need to check all figure environments in the paper's LaTeX source to see which ones use `figure*` vs `figure`, and what width they specify (e.g., `\textwidth` vs `\columnwidth`). The figures were recently converted from horizontal to vertical layout, making them taller and narrower — some that were full-width (`figure*`) may now fit in a single column (`figure`).

Search these files for figure/includegraphics patterns:
- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex

For each figure, report:
1. The file and line number
2. Whether it uses `figure` or `figure*`
3. The includegraphics width parameter
4. The figure filename
5. Whether it's a main text figure or appendix figure

Report in a compact table format.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "52ff2238-2bff-43fb-88da-a3f0a815c702",
  "agentId": "aa7d450a33c4a6692",
  "type": "user",
  "uuid": "8523014e-ff8c-49be-9562-046271867415",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-25T04:45:36.935Z_

I'll search through all the specified LaTeX files to find figure environments and their configurations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8523014e-ff8c-49be-9562-046271867415",
  "isSidechain": true,
  "agentId": "aa7d450a33c4a6692",
  "requestId": "req_011CbNgK9hzNmxPTro6HfRSr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e47492b4-7a28-43e6-8995-354494d8057d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XA1kDJXgdNpGBD8FeLYn9Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39933,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39933,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-25T04:45:37.361Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WQgoJaSySGkPBdfwCVf92V`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e47492b4-7a28-43e6-8995-354494d8057d",
  "isSidechain": true,
  "agentId": "aa7d450a33c4a6692",
  "requestId": "req_011CbNgK9hzNmxPTro6HfRSr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "86018783-3d52-420e-a222-f572d34941e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XA1kDJXgdNpGBD8FeLYn9Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39933,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39933,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-25T04:45:37.369Z_

<details><summary>↩ Tool result · `toolu_01WQgoJaSySGkPBdfwCVf92V`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Multi-turn dialogue is central to how large language models are deployed, yet a persistent failure accompanies even the most fluent generation: as conversations grow longer, models pay progressively less attention to the system-prompt goals that define their task. \citet{dongre2026attention} measured 27--48\% Goal Accessibility Ratio (GAR) decline across 12 models over 50 turns, even as residual stream probes confirm that goal representations persist (AUC\,=\,0.98). This is not just a measurement artifact---it degrades instruction compliance by up to 24 percentage points on content-constrained tasks (\S\ref{sec:discussion}).
4	
5	Existing remedies address this decay at inference time. Split-softmax \citep{li2024measuring} separates instruction from conversation tokens; StreamingLLM \citep{xiao2024streaming} retains anchor tokens; Gated Attention \citep{qiu2025gated} applies per-head sigmoid gates within a single forward pass. None of these intervenes during training. A natural alternative is to optimize goal attention directly through auxiliary attention losses trained alongside next-token prediction (NTP). Yet this strategy rests on an untested assumption: that attention patterns learned under teacher forcing transfer to autoregressive generation. Classical exposure bias research \citep{bengio2015scheduled,lamb2016professor} has shown that teacher forcing creates a training--inference mismatch for RNN sequence models, but whether this mismatch extends to auxiliary attention objectives in multi-turn transformers remains unknown.
6	
7	We test this assumption. We introduce ThreadGate, per-layer content-and-turn-conditioned gates on the residual stream ($x_{l+1} = x_l + g_l \cdot f_l(x_l)$), designed not as a solution but as a controlled testbed for isolating failure mechanisms. A five-way comparison (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Base) forms a causal exclusion chain (\S\ref{sec:comparison-design}): each adjacent pair rules out one alternative hypothesis---turn conditioning, gating mechanism, gradient conflict---tracing the failure to its root cause.
8	
9	\begin{figure*}[t]
10	  \centering
11	  \includegraphics[width=\textwidth]{fig1_headline.pdf}
12	  \caption{Exposure bias destroys auxiliary attention losses. \textbf{(a)}~Goal attention decays 85--90\% across turns under AR generation on both Qwen-2.5-7B and Llama-3.1-8B. \textbf{(b)}~Under TF evaluation all variants reach GAR$\approx$0.50, but AR generation collapses GAR by 8--17$\times$ (log scale). \textbf{(c)}~Scheduled sampling compresses the TF--AR gap from 7.8$\times$ to 1.3$\times$ (Qwen) and 12.0$\times$ to 2.9$\times$ (Llama).}
13	  \label{fig:headline}
14	\end{figure*}
15	
16	The result is clear: training succeeds but inference fails. All variants converge to TF GAR\,=\,0.50, yet under autoregressive generation GAR collapses to 0.019--0.064, an 8--17$\times$ gap on Qwen-2.5-7B and 27$\times$ on Llama-3.1-8B (Figure~\ref{fig:headline}). The causal exclusion chain identifies exposure bias as the sole surviving explanation: PCGrad removes gradient conflict yet \emph{worsens} AR GAR ($p$\,=\,0.002), ruling it out by \emph{modus tollens}; gating provides no benefit over LoRA-only. Crucially, inference-time steering ($\beta$\,=\,5) recovers GAR to 0.727, confirming that the collapse reflects attention misallocation rather than representation degradation. Scheduled sampling compresses the TF--AR gap to ${\sim}$1.3$\times$ on Qwen and ${\sim}$2.9$\times$ on Llama with no perplexity cost---the first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers.
17	
18	Our contributions: (1)~the first empirical characterization of exposure bias on auxiliary attention losses (8--27$\times$ TF--AR gap across two architectures); (2)~PCGrad-based causal exclusion of gradient conflict ($p$\,=\,0.002, effect reverses); (3)~inference-time $\beta$-steering recovers GAR to 0.727, confirming attention misallocation as the proximal cause; (4)~scheduled sampling compresses the TF--AR gap from 8--27$\times$ to 1.3--2.9$\times$ ($0.401\pm0.047$, three seeds on Qwen), generalizing across architectures. Code and data are available at \url{https://anonymous.4open.science/r/turn-residual-gating}.
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86018783-3d52-420e-a222-f572d34941e5",
  "isSidechain": true,
  "promptId": "52ff2238-2bff-43fb-88da-a3f0a815c702",
  "agentId": "aa7d450a33c4a6692",
  "type": "user",
  "uuid": "6a81120b-c693-4a2f-aff9-8e1614f2bd87",
  "sourceToolAssistantUUID": "86018783-3d52-420e-a222-f572d34941e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-25T04:45:37.579Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VGBotERCazUaT2jUrAnAZ9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a81120b-c693-4a2f-aff9-8e1614f2bd87",
  "isSidechain": true,
  "agentId": "aa7d450a33c4a6692",
  "requestId": "req_011CbNgK9hzNmxPTro6HfRSr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7ac45bfd-ef9e-4e5c-a48f-1a944f0356dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XA1kDJXgdNpGBD8FeLYn9Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39933,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39933,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-25T04:45:37.586Z_

<details><summary>↩ Tool result · `toolu_01VGBotERCazUaT2jUrAnAZ9`</summary>

```text
1	\section{Method}\label{sec:method}
2	
3	\subsection{Preliminaries}\label{sec:background}
4	
5	\paragraph{Goal Accessibility Ratio.}
6	Standard metrics such as perplexity and attention entropy capture generation quality but not \emph{what} the model attends to. In multi-turn dialogue, a model may generate fluent text while progressively ignoring task specifications in the system prompt. We need a metric that directly measures whether goal-relevant context receives attention. We denote the task specification tokens in the system prompt as \emph{goal tokens} $\mathcal{G}$. In the standard transformer attention mechanism \citep{vaswani2017attention}, \citet{dongre2026attention} defined the Goal Accessibility Ratio (GAR) for a model with $L$ layers and $H$ heads at turn $\tau$ as
7	\begin{equation}\label{eq:gar}
8	  \text{GAR}(\tau) = \frac{1}{L \cdot H \cdot |\mathcal{R}_\tau|} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{i \in \mathcal{R}_\tau} \sum_{j \in \mathcal{G}} A_{i,j}^{(\ell,h)},
9	\end{equation}
10	where $\mathcal{R}_\tau$ is the set of response tokens at turn $\tau$ and $A_{i,j}^{(\ell,h)}$ is the attention weight from token $i$ to token $j$ at layer $\ell$, head $h$.
11	
12	\paragraph{Two GAR variants.}
13	\textbf{GAR-Dongre} is the original definition (Eq.~\ref{eq:gar}), averaging over all response tokens. However, averaging dilutes the signal with intermediate positions that may legitimately attend to local context rather than the system prompt. The last token of each assistant turn is where the model aggregates information for the next continuation---attention at this position most directly reflects the model's awareness of task specifications. \textbf{GAR-ours} restricts the measurement accordingly:
14	\begin{equation}\label{eq:gar-ours}
15	  \text{GAR\text{-}ours}(\tau) = \frac{1}{L \cdot H} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{j \in \mathcal{G}} A_{t_\tau,\, j}^{(\ell,h)},
16	\end{equation}
17	where $t_\tau$ is the last token index at turn $\tau$. Attention at this position reflects the information drawn upon for continuation; we use GAR-ours as the optimization target for $\mathcal{L}_\text{GAR}$ (\S\ref{sec:loss}).
18	
19	\subsection{ThreadGate Architecture}
20	
21	Different transformer layers serve different roles: early layers capture local syntax while later layers integrate long-range context \citep{gromov2024unreasonable}. A global intervention would uniformly scale all layers, but goal attention decay is layer-dependent: some layers contribute more to cross-turn information routing than others. ThreadGate therefore adds a \emph{per-layer} gating mechanism to the residual stream, allowing the model to learn which layers to modulate. At each layer $l$, the residual update is scaled by a scalar gate:
22	\begin{equation}
23	  x_{l+1} = x_l + g_l \cdot f_l(x_l),
24	\end{equation}
25	where $f_l$ denotes the sublayer computation (self-attention or feed-forward network, FFN). From the perspective that residual networks function as ensembles of shallow paths \citep{veit2016residual}, per-layer gating selectively modulates individual paths. This resembles ReZero \citep{bachlechner2021rezero}, which initializes a single trainable scalar at zero to stabilize deep network training. ThreadGate differs in three ways: (i)~gates are \emph{content-conditioned}, a function of the hidden state rather than a fixed scalar; (ii)~gates are \emph{turn-conditioned}, incorporating conversation-position features; (iii)~gates are initialized near identity ($\sigma(1.5) \approx 0.82$) rather than zero, preserving the pretrained model's computation.
26	
27	\paragraph{Gate network.} A fixed scalar per layer (as in ReZero) cannot adapt to varying inputs; the gate must be \emph{content-conditioned} so that different conversations or turns can receive different modulation. Adding \emph{turn conditioning} allows the gate to distinguish early turns (where GAR is naturally high) from late turns (where intervention is most needed). Each gate $g_l$ is thus produced by a two-layer MLP that takes both content and turn features as input:
28	\begin{align}\label{eq:gate}
29	  g_l = \sigma\bigl(W_2\,\text{ReLU}(&W_1\,[\text{proj}(x_l);\;\text{emb}(t_d, t_i)] \notag\\
30	  &+ b_1) + b_2\bigr),
31	\end{align}
32	where $\text{proj}(\cdot)$ reduces the hidden dimension to 16, and $\text{emb}(t_d, t_i)$ provides a 16-dimensional turn embedding. The 32-dimensional input passes through a 64-unit hidden layer to a scalar gate in $(0, 1)$ via sigmoid. For Qwen-2.5-7B ($L\!=\!28$), this adds ${\sim}$57K parameters ($<$0.001\% of 7B).
33	
34	\paragraph{Turn embedding.} The embedding $\text{emb}(t_d, t_i)$ encodes turn distance $t_d$ (turns since system prompt) and turn index $t_i$ via learned lookup tables, allowing gates to distinguish conversation positions. The \textbf{Uniform Gate} ablation replaces $\text{emb}(\cdot)$ with a learnable constant, removing turn awareness.
35	
36	\paragraph{Initialization.} Gate biases are set to 1.5 (${\sim}$82\% pass-through), contrasting ReZero's zero initialization that would suppress pretrained capabilities. Gate parameters receive a $10\times$ learning rate multiplier.
37	
38	\begin{figure}[t]
39	  \centering
40	  \includegraphics[width=\columnwidth]{fig4_attention_heatmap.pdf}
41	  \caption{Per-turn GAR-ours under AR generation ($N$\,=\,5 conversations, 10 turns). All fine-tuned variants cluster together (77--81\% decay; $\Delta$\,=\,3.3\,pp between ThreadGate and LoRA-only); Base decays 87.5\%. Gating adds zero incremental effect.}
42	  \label{fig:attention-heatmap}
43	\end{figure}
44	
45	\subsection{Training Objective}\label{sec:loss}
46	
47	Next-token prediction alone provides no gradient signal for attention allocation; a model can achieve low perplexity while distributing attention arbitrarily. The auxiliary GAR loss provides explicit pressure to maintain goal-token attention, while a diversity regularizer prevents gate collapse. The training objective combines three terms:
48	\begin{equation}
49	  \mathcal{L} = \mathcal{L}_\text{NTP} + \lambda_\text{GAR}\,\mathcal{L}_\text{GAR} + \lambda_\text{div}\,\mathcal{L}_\text{div}.
50	\end{equation}
51	$\mathcal{L}_\text{NTP}$ is the standard next-token prediction loss. We use mean squared error (MSE) rather than cross-entropy for $\mathcal{L}_\text{GAR}$ because GAR is a continuous ratio, not a probability, and MSE provides \emph{bidirectional} pressure, penalizing both under-attention (GAR\,$<$\,$\tau$) and over-attention (GAR\,$>$\,$\tau$). This symmetry is critical: a unidirectional maximize objective drives gates toward identity (Appendix~\ref{sec:appendix-loss}). The GAR loss is:
52	\begin{equation}
53	  \mathcal{L}_\text{GAR} = \text{MSE}(\text{GAR\text{-}ours}, \tau),
54	\end{equation}
55	where $\tau = 0.5$ targets allocating half of the last token's attention capacity to goal tokens. GAR is measured at the last token of each assistant turn (GAR-ours, \S\ref{sec:background}). Without explicit diversity pressure, all gates converge to the same value (typically near 1.0), eliminating the layer-specific modulation that is the design intent. The gate diversity loss prevents this collapse:
56	\begin{equation}
57	  \mathcal{L}_\text{div} = \text{ReLU}(\sigma_\text{min} - \text{std}(\mathbf{g})),
58	\end{equation}
59	where $\mathbf{g} = [g_1, \ldots, g_L]$ and $\sigma_\text{min}$ is a minimum standard deviation threshold. Both $\lambda_\text{GAR} = \lambda_\text{div} = 1.0$.
60	
61	\paragraph{Loss design evolution.} The MSE formulation was selected from seven iterations spanning four loss families (Appendix~\ref{sec:appendix-loss}): cumulative (v1--v2) and maximize (v3--v6) objectives either starve gate gradients at equilibrium or drive gates toward identity. Only MSE provides bidirectional pressure, penalizing both over- and under-attention, preventing identity collapse.
62	
63	\subsection{Controlled Comparison Design}\label{sec:comparison-design}
64	
65	We design a five-way comparison where each adjacent pair isolates one factor: \textbf{ThreadGate (TG) vs.\ Uniform Gate (UG)} (turn conditioning), \textbf{TG vs.\ LoRA-only} (gating mechanism), \textbf{ThreadGate vs.\ +PCGrad} (gradient conflict via gradient surgery \citep{yu2020pcgrad}), and \textbf{Fine-tuned vs.\ Base} (LoRA adaptation). All fine-tuned variants share training data, LoRA configuration, optimizer, and seed (Appendix~\ref{sec:appendix-hyper}).
66	
67	\begin{figure}[t]
68	  \centering
69	  \includegraphics[width=\columnwidth]{fig5_attention_steering.pdf}
70	  \caption{Inference-time $\beta$-steering recovers GAR from 0.064 to 0.727, confirming attention misallocation as the proximal cause (9\% PPL cost at $\beta$\,=\,3; phase transition at $\beta \in [2, 3]$).}
71	  \label{fig:steering-recovery}
72	\end{figure}
73	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ac45bfd-ef9e-4e5c-a48f-1a944f0356dc",
  "isSidechain": true,
  "promptId": "52ff2238-2bff-43fb-88da-a3f0a815c702",
  "agentId": "aa7d450a33c4a6692",
  "type": "user",
  "uuid": "3cf9485d-62e9-47e5-9369-3a075ade1a0b",
  "sourceToolAssistantUUID": "7ac45bfd-ef9e-4e5c-a48f-1a944f0356dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-25T04:45:37.791Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MHMpfKQEvuqtCPA27rAUuf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3cf9485d-62e9-47e5-9369-3a075ade1a0b",
  "isSidechain": true,
  "agentId": "aa7d450a33c4a6692",
  "requestId": "req_011CbNgK9hzNmxPTro6HfRSr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "54619264-c3af-4a47-a842-4928916e25b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XA1kDJXgdNpGBD8FeLYn9Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39933,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39933,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-25T04:45:37.797Z_

<details><summary>↩ Tool result · `toolu_01MHMpfKQEvuqtCPA27rAUuf`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	
6	We fine-tune Qwen-2.5-7B-Instruct with LoRA \citep{hu2022lora,dettmers2023qlora} on 8K multi-turn conversations from the UltraChat \citep{ding2023ultrachat} training split. Training uses 3 epochs with AdamW (lr $= 2 \times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB; training costs in Appendix~\ref{sec:appendix-cost}). Full hyperparameters are in Appendix~\ref{sec:appendix-hyper}; dataset statistics in Appendix~\ref{sec:appendix-data}; the controlled comparison design is described in \S\ref{sec:comparison-design}. We evaluate under \emph{IID} (same-distribution UltraChat text) and \emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours, GAR-Dongre \citep{dongre2026attention}, and perplexity (PPL).
7	
8	\subsection{Main Results}
9	
10	Table~\ref{tab:four-way} presents the five-way comparison. Under TF evaluation, all fine-tuned variants converge: GAR-ours spans 0.49--0.51 ($\leq$2\,pp), PPL is 2.78 for all. IID and held-out protocols produce identical rankings (held-out GAR-ours differs by $\leq$1\,pp), ruling out data overlap as a confound. GAR-Dongre remains low (0.01--0.02) with no TF-AR gap, confirming that only concentrated last-token attention is vulnerable to distribution shift; scheduled sampling breaks this pattern (\S\ref{subsec:ss}).
11	
12	Under AR generation ($N$\,=\,50), GAR-ours drops to 0.019--0.064, an 8--17$\times$ gap (Figure~\ref{fig:headline}). The ordering (ThreadGate 0.064 $>$ LoRA-only 0.037 $>$ Uniform Gate 0.033 $>$ PCGrad 0.030 $>$ Base 0.019) shows ThreadGate vs.\ LoRA-only is significant ($p$\,=\,0.004; Appendix~\ref{sec:appendix-stats}), yet the gap remains 7.8$\times$. A second seed confirms TF stability ($0.504\pm0.001$). MMLU 5-shot accuracy remains within 0.8\,pp across all variants (Appendix~\ref{sec:appendix-mmlu}). We analyze this distribution shift in \S\ref{sec:analysis}.
13	
14	\subsection{Inference-Time Attention Steering}\label{subsec:steering}
15	
16	All training-time interventions leave the exposure bias gap intact. If the collapse is caused by attention misallocation rather than representation degradation, then directly correcting attention should recover GAR. We test this by adding a constant bias $\beta$ to pre-softmax attention logits for goal-token positions during generation:
17	\begin{equation}
18	  \tilde{A}_{i,j}^{(\ell,h)} = A_{i,j}^{(\ell,h)} + \beta \cdot \mathbf{1}[j \in \mathcal{G}],
19	\end{equation}
20	where $\tilde{A}$ denotes the modified logits before softmax. The additive form operates in log-probability space, providing uniform boost even when baseline attention is near zero. The response is sharply nonlinear: $\beta \in [0, 2]$ yields marginal improvement, then $\beta = 3$ triggers a phase transition to GAR\,=\,0.556 (9\% PPL cost). At $\beta$\,=\,5, GAR reaches 0.727$\pm$0.061 (PPL 1.77); the operating region $\beta \in [3, 5]$ exceeds the TF baseline while PPL remains below 1.8 (Figure~\ref{fig:steering-recovery}; full results in Appendix~\ref{sec:appendix-steering}; per-$\beta$ turn-level profiles in Appendix~\ref{sec:appendix-steering-viz}).
21	
22	This closes the causal loop: if the collapse were due to representation drift in hidden states, no amount of attention reweighting could recover GAR. The recovery confirms attention misallocation, not representation degradation, as the proximal cause (qualitative examples in Appendix~\ref{sec:appendix-examples}).
23	
24	\subsection{Scheduled Sampling Compresses the TF--AR Gap}\label{subsec:ss}
25	
26	Scheduled sampling (SS; \citealp{bengio2015scheduled}), which mixes model-generated tokens into training prefixes with linearly increasing probability (implementation details in Appendix~\ref{sec:appendix-ss}), directly targets the training-inference mismatch identified in \S\ref{subsec:dist-shift}. Across three seeds, AR GAR-ours rises from 0.064 to $0.401\pm0.047$ (seeds: 0.347 / 0.423 / 0.433; per-seed details in Appendix~\ref{sec:appendix-perseed}), compressing the gap from 7.8$\times$ to ${\sim}$1.3$\times$ (per-seed gaps: 1.45$\times$, 1.17$\times$, 1.15$\times$; TF GAR $0.498\pm0.004$) with no PPL cost ($1.441\pm0.001$; Figure~\ref{fig:ss-gap}). Steering on SS models is remarkably stable ($\beta$\,=\,5: $0.717\pm0.001$): the training-time seed variance (std\,=\,0.047 at $\beta$\,=\,0) is nearly eliminated (Figure~\ref{fig:ss-multiseed}), suggesting $\beta$-steering converges to a seed-independent attention equilibrium. The improvement generalizes across GAR definitions: SS raises mid-turn GAR above 0.36 under all four alternative token-position variants (Appendix~\ref{sec:appendix-gar-robust}), while ThreadGate only improves last-token GAR (0.325 vs.\ all-token 0.025): SS builds a broad goal-attention pattern, not position-specific overfitting. GAR-Dongre also rises substantially under SS ($N$\,=\,5 pilot; see Appendix~\ref{sec:appendix-n5}), the only intervention that moves both metrics. The benefit generalizes across architectures: on Llama-3.1-8B, SS compresses the gap from ${\sim}$12$\times$ to 2.9$\times$ (AR GAR 0.166, TF GAR 0.477), weaker than Qwen's ${\sim}$1.3$\times$ likely due to fewer training epochs (2 vs.\ 3; \S\ref{subsec:cross-model}). The benefit diminishes in longer dialogues (Appendix~\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.
27	
28	\begin{figure}[t]
29	  \centering
30	  \includegraphics[width=\columnwidth]{fig_ss_gap_compression.pdf}
31	  \caption{Scheduled sampling compresses the TF-AR gap from 7.8$\times$ to ${\sim}$1.3$\times$, the only variant approaching parity across five training conditions.}
32	  \label{fig:ss-gap}
33	\end{figure}
34	
35	
36	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54619264-c3af-4a47-a842-4928916e25b4",
  "isSidechain": true,
  "promptId": "52ff2238-2bff-43fb-88da-a3f0a815c702",
  "agentId": "aa7d450a33c4a6692",
  "type": "user",
  "uuid": "989f0da1-9ca6-4275-b155-9f5ccff10eb9",
  "sourceToolAssistantUUID": "54619264-c3af-4a47-a842-4928916e25b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T04:45:38.006Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SMtLwK3xqpfejPVhL6bBeG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "989f0da1-9ca6-4275-b155-9f5ccff10eb9",
  "isSidechain": true,
  "agentId": "aa7d450a33c4a6692",
  "requestId": "req_011CbNgK9hzNmxPTro6HfRSr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ae66c28b-9a1d-4b73-8d67-91f21cd0bf93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XA1kDJXgdNpGBD8FeLYn9Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39933,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39933,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-25T04:45:38.016Z_

<details><summary>↩ Tool result · `toolu_01SMtLwK3xqpfejPVhL6bBeG`</summary>

```text
1	\section{Analysis}\label{sec:analysis}
2	
3	The five-way comparison (\S\ref{sec:experiments}) yields a paradox: training succeeds but inference fails, and no single architectural factor explains the gap. This section resolves it through a causal exclusion chain; each subsection kills one alternative hypothesis: \S\ref{subsec:gate-conditioning} kills ``turn conditioning rescues late-turn attention''; \S\ref{subsec:pcgrad} kills ``gradient conflict prevents GAR convergence''; \S\ref{subsec:dist-shift} identifies exposure bias as the surviving explanation. \S\ref{subsec:mechanism-specificity} confirms selectivity via an orthogonal metric, and \S\ref{subsec:cross-model} confirms generalization across architectures.
4	
5	\subsection{Gate Turn Conditioning}\label{subsec:gate-conditioning}
6	
7	We compare gate values at turn~1 (early) and turn~21 (late) across all 28 layers. The gates invert the design intent: in 27/28 layers, gate values are \emph{lower} at turn~1 than turn~21 (Wilcoxon $p = 3.73 \times 10^{-8}$, $r = 0.975$); e.g., layer~23 shifts from 0.769 to 0.979. NTP pressure pushes gates toward 1.0, a convergence pattern reminiscent of attention collapse in deep transformers \citep{dong2021attention}, yielding inference-time values of 0.93--0.98 (2--7\% attenuation; Table~\ref{tab:four-way}; full gate profiles in Appendix~\ref{sec:appendix-gate-profile}). The Uniform Gate learns comparable per-layer variation (L3\,=\,0.777, L27\,=\,1.000) despite lacking turn conditioning, confirming the structure arises from LoRA$+$GAR pressure (Figure~\ref{fig:gate-shift}a). Does the NTP-GAR gradient conflict prevent the intended behavior?
8	
9	\subsection{PCGrad Gradient Conflict Exclusion}\label{subsec:pcgrad}
10	
11	NTP and GAR gradients oppose in 68--79\% of layers (cosine similarity $-$0.089$\to$$-$0.042 across epochs), with NTP magnitude dominance growing from 7.5$\times$ to 14.7$\times$ (full gradient statistics in Appendix~\ref{sec:appendix-gradient}). If this conflict prevents GAR convergence, eliminating it via PCGrad \citep{yu2020pcgrad}, which projects conflicting gradients onto the other's normal plane, should prevent the collapse. To our knowledge, this is the first application of PCGrad as a \emph{diagnostic} tool rather than an optimization method.
12	
13	PCGrad shifts cosine similarity to oscillate around zero, yet TF metrics are unchanged. AR GAR \emph{worsens}: 0.064$\to$0.030 ($p$\,=\,0.002; Figure~\ref{fig:training-pcgrad}b in Appendix~\ref{sec:appendix-gradient}). By \emph{modus tollens}: removing gradient conflict does not prevent collapse; therefore it is not the cause. The 7.5--14.7$\times$ magnitude dominance renders gradient conflict inconsequential. Cross-model analysis confirms this pattern: Llama-3.1-8B gradients are near-orthogonal (cos\,=\,+0.005) with 25.7$\times$ NTP dominance (Table~\ref{tab:gradient-crossmodel}).
14	
15	\begin{figure}[t]
16	  \centering
17	  \includegraphics[width=\columnwidth]{fig_ss_multiseed.pdf}
18	  \caption{Multi-seed AR GAR under scheduled sampling ($\beta$\,=\,0 and $\beta$\,=\,5, three seeds). Steering nearly eliminates seed variance (std: 0.047$\to$0.001).}
19	  \label{fig:ss-multiseed}
20	\end{figure}
21	
22	\subsection{Distribution Shift Analysis}\label{subsec:dist-shift}
23	
24	The TF-AR GAR gap persists across all variants (Table~\ref{tab:four-way}). GAR-Dongre provides a control: it remains uniformly low (0.01--0.02) with no distribution gap, so the shift selectively destroys concentrated last-token attention while leaving diffuse attention unaffected. The mechanism is exposure bias \citep{bengio2015scheduled,zhang2019bridging,arora2022exposure}: during training the model conditions on ground-truth prefixes; at inference, on its own outputs. NTP self-recovers \citep{he2019exposure} because prediction is the same task at both regimes; GAR optimizes a distributional property with no autoregressive counterpart. Unlike token-level predictions, attention flow through layers \citep{abnar2020quantifying} over model-generated tokens has no training-time analogue, explaining why TF GAR-ours remains near $\tau$\,=\,0.5 while AR GAR collapses (77--87\% per-turn decay; Figure~\ref{fig:attention-heatmap}; scaling analysis in Appendix~\ref{sec:appendix-eb-scaling}; per-turn dynamics in Appendices~\ref{sec:appendix-ar-gar-dynamics} and~\ref{sec:appendix-perturn-detail}).
25	
26	\begin{figure}[t]
27	  \centering
28	  \includegraphics[width=\columnwidth]{fig3_gate_shift.pdf}
29	  \caption{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \times 10^{-8}$). (b)~Distribution shift ($N$\,=\,5 pilot): the TF-AR GAR gap persists across all five variants. Pilot gaps (20--34$\times$) exceed final $N$\,=\,50 estimates (8--17$\times$; Table~\ref{tab:four-way}) due to smaller sample size.}
30	  \label{fig:gate-shift}
31	\end{figure}
32	
33	\subsection{Mechanism Specificity}\label{subsec:mechanism-specificity}
34	
35	We test specificity with Turn-level Residual Coherence (TRC), the cosine similarity between adjacent-turn hidden states. TF/AR TRC is 0.334/0.332 for ThreadGate (gap $+$0.002) and 0.349/0.411 for LoRA-only (gap $-$0.062, reversed), confirming exposure bias disrupts a specific routing behavior while leaving representations intact. Cross-model evaluation confirms: GAR-Dongre shows negligible shift on both Llama (1.002$\times$) and Qwen (1.28$\times$) vs.\ the order-of-magnitude GAR-ours collapse.
36	
37	\subsection{Cross-Model Replication}\label{subsec:cross-model}
38	
39	We replicate on Llama-3.1-8B-Instruct \citep{grattafiori2024llama3} (Base, ThreadGate, LoRA-only; $N$\,=\,20, 4 turns). TF GAR-ours is 0.484 (TG) / 0.481 (LoRA-only); gating contributes zero benefit. The AR distribution is heavy-tailed (coefficient of variation, CoV\,$>$\,100\%); we report medians: 0.018 (TG and LoRA-only), 0.009 (Base), yielding gaps of 27$\times$ and 26$\times$ (Figure~\ref{fig:crossmodel}a in Appendix~\ref{sec:appendix-llama}). Gate profiles differ qualitatively (Figure~\ref{fig:crossmodel}b): Qwen attenuates early layers (L1\,=\,0.793) while Llama dips at late layers (L25\,=\,0.719), an architecture-dependent pattern, but convergence toward identity is universal (Appendix~\ref{sec:appendix-viz}). The gap is substantial on both architectures (8--17$\times$ on Qwen, 27$\times$ on Llama), consistent with exposure bias as architecture-independent.
40	
41	Scheduled sampling confirms cross-model generalization: Llama SS compresses the gap from ${\sim}$12$\times$ to 2.9$\times$ (TF GAR 0.477, AR GAR 0.166), weaker than Qwen's ${\sim}$1.3$\times$ likely due to fewer training epochs (2 vs.\ 3). The phase transition is architecture-dependent: $\beta$\,=\,3 triggers recovery on Qwen (0.556) but not Llama (0.173); Llama requires $\beta$\,=\,5 (GAR 0.791, exceeding Qwen SS 0.717), suggesting deeper architectures need higher steering thresholds but ultimately provide more surface for attention reweighting (full results in Appendix~\ref{sec:appendix-llama}).
42	
43	Cross-scale validation on Qwen-2.5-1.5B confirms the same pattern: 79.8\% GAR decay and $\beta$-steering recovery to 0.715 (Appendix~\ref{sec:appendix-1.5b}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae66c28b-9a1d-4b73-8d67-91f21cd0bf93",
  "isSidechain": true,
  "promptId": "52ff2238-2bff-43fb-88da-a3f0a815c702",
  "agentId": "aa7d450a33c4a6692",
  "type": "user",
  "uuid": "2aaacab1-6791-4ae0-a791-fef3ae4e9b2c",
  "sourceToolAssistantUUID": "ae66c28b-9a1d-4b73-8d67-91f21cd0bf93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-25T04:45:38.214Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Wcfk8DsTxRUHjbG9VNxKT3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2aaacab1-6791-4ae0-a791-fef3ae4e9b2c",
  "isSidechain": true,
  "agentId": "aa7d450a33c4a6692",
  "requestId": "req_011CbNgK9hzNmxPTro6HfRSr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9812515a-897c-4f68-be5c-c01a1c723bb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XA1kDJXgdNpGBD8FeLYn9Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39933,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39933,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-25T04:45:38.233Z_

<details><summary>↩ Tool result · `toolu_01Wcfk8DsTxRUHjbG9VNxKT3`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	The failure traces to an incompatibility between teacher-forcing and GAR-family auxiliary losses, not to the gating architecture. Any auxiliary attention objective paired with teacher forcing should face the same exposure bias barrier when targeting distributional properties of the attention pattern rather than the prediction itself.
4	
5	\paragraph{Why NTP self-recovers but GAR does not.} NTP self-recovers because the task (predict one token from a prefix) is identical at training and inference \citep{he2019exposure}. GAR optimizes a \emph{global property of the prefix}---attention allocation to goal tokens---that has no autoregressive counterpart: the model receives no feedback on attention distributions during generation. Per-head analysis confirms this selectivity: heads with higher TF GAR shift most under AR generation ($r$\,=\,0.743; Appendix~\ref{sec:appendix-kl}).
6	
7	\paragraph{Downstream effects.} Instruction retention ($\beta$\,=\,3) shows late-turn compliance rising from 75.9\% to 87.0\% (+11.1\,pp, $p$\,=\,0.077). Content constraints benefit most (+23.8\,pp), consistent with GAR targeting cross-turn semantic coherence rather than locally-verifiable procedural rules (Appendix~\ref{sec:appendix-ir}).
8	
9	\paragraph{SS and steering as substitutes.} SS provides training-time mitigation with no inference cost; steering provides inference-time recovery with PPL cost. At high $\beta$ the two converge ($\beta$\,=\,5: SS GAR\,=\,$0.717\pm0.001$ vs.\ TG\,=\,0.727), making them substitutes. SS is preferable when inference budgets are tight, steering when retraining is infeasible.
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9812515a-897c-4f68-be5c-c01a1c723bb4",
  "isSidechain": true,
  "promptId": "52ff2238-2bff-43fb-88da-a3f0a815c702",
  "agentId": "aa7d450a33c4a6692",
  "type": "user",
  "uuid": "0d46c3eb-dcc6-4e10-9112-ec4b90115467",
  "sourceToolAssistantUUID": "9812515a-897c-4f68-be5c-c01a1c723bb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-25T04:45:38.371Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DrHWPWiQp4gzunZNfzuzpd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d46c3eb-dcc6-4e10-9112-ec4b90115467",
  "isSidechain": true,
  "agentId": "aa7d450a33c4a6692",
  "requestId": "req_011CbNgK9hzNmxPTro6HfRSr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f569ae28-edae-4eb5-a4df-043cf5c9b8fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XA1kDJXgdNpGBD8FeLYn9Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39933,
      "cache_read_input_tokens": 0,
      "output_tokens": 469,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 39933
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 469,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 39933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 39933,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-25T04:45:38.636Z_

<details><summary>↩ Tool result · reported error · `toolu_01DrHWPWiQp4gzunZNfzuzpd`</summary>

```text
File content (26074 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f569ae28-edae-4eb5-a4df-043cf5c9b8fe",
  "isSidechain": true,
  "promptId": "52ff2238-2bff-43fb-88da-a3f0a815c702",
  "agentId": "aa7d450a33c4a6692",
  "type": "user",
  "uuid": "ec17176e-55f4-4b33-aeba-96f9f47364e5",
  "toolUseResult": "Error: File content (26074 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "f569ae28-edae-4eb5-a4df-043cf5c9b8fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-25T04:45:39.925Z_

Let me read the appendix file in chunks since it's quite large:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec17176e-55f4-4b33-aeba-96f9f47364e5",
  "isSidechain": true,
  "agentId": "aa7d450a33c4a6692",
  "requestId": "req_011CbNgKNhq9Gc9KWFrJtWjq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ad4c4848-d2e6-4199-b74b-cc50ecb8107e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0149AWjUS8pkiHb4kUfW7MHC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 10525,
      "cache_read_input_tokens": 39933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10525,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-25T04:45:40.698Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WKSF3DLRLF6TuQKj98JS5s`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "offset": 1,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad4c4848-d2e6-4199-b74b-cc50ecb8107e",
  "isSidechain": true,
  "agentId": "aa7d450a33c4a6692",
  "requestId": "req_011CbNgKNhq9Gc9KWFrJtWjq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "332e64ca-404e-47f8-a99c-deb2bd5ccc26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0149AWjUS8pkiHb4kUfW7MHC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 10525,
      "cache_read_input_tokens": 39933,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10525
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 140,
          "cache_read_input_tokens": 39933,
          "cache_creation_input_tokens": 10525,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10525,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-25T04:45:40.952Z_

<details><summary>↩ Tool result · `toolu_01WKSF3DLRLF6TuQKj98JS5s`</summary>

```text
1	\section{Training Configuration}\label{sec:appendix-hyper}
2	
3	Table~\ref{tab:hyperparams} lists the full training configuration shared across all fine-tuned variants. ThreadGate gate parameters receive a $10\times$ learning rate multiplier and are initialized with bias 1.5 ($\sigma(1.5) \approx 0.82$); the gate MLP adds ${\sim}$57K parameters per variant ($<$0.001\% of 7B). The scheduled sampling variant (v8b) linearly increases the model-generated context ratio from 0 to 0.5 over 3 epochs (29.7--37.1\% effective usage due to per-sample Bernoulli sampling). All experiments were conducted on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB VRAM), requiring 6--8 hours per variant.
4	
5	\begin{table}[h]
6	\centering\small
7	\caption{Training hyperparameters for all fine-tuned variants. Entries marked $\dagger$ apply only to ThreadGate and its ablations.}
8	\label{tab:hyperparams}
9	\begin{tabular}{l@{\hspace{8pt}}l}
10	\toprule
11	\textbf{Parameter} & \textbf{Value} \\
12	\midrule
13	Base model & Qwen-2.5-7B-Instruct \\
14	LoRA rank / $\alpha$ & 16 / 32 \\
15	LoRA targets & \texttt{q\_proj}, \texttt{v\_proj} \\
16	Optimizer & AdamW ($\beta_1$\!=\!0.9, $\beta_2$\!=\!0.999) \\
17	Learning rate & $2 \times 10^{-4}$ \\
18	Gate LR mult.$^\dagger$ & $10\times$ \\
19	Batch / grad accum & 1 / 8 (eff.\ 8) \\
20	Epochs & 3 \\
21	Max seq length & 2048 \\
22	Training data & 8K UltraChat convs \\
23	Seed & 42 (+123 for TG, SS) \\
24	$\lambda_\text{GAR}$/$\lambda_\text{div}$ & 1.0 / 1.0 \\
25	GAR target $\tau$ & 0.5 \\
26	Gate init bias$^\dagger$ & 1.5 ($\sigma\!\approx\!0.82$) \\
27	Gate hidden dim$^\dagger$ & 64 \\
28	Turn embed dim$^\dagger$ & 16 \\
29	GPU & RTX PRO 6000 (96\,GB) \\
30	Training time & 6--8 h / variant \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	\section{Loss Formulation Search}\label{sec:appendix-loss}
36	
37	The final MSE + gate diversity loss (\S\ref{sec:loss}) emerged from seven iterations spanning four loss families. Table~\ref{tab:loss-iterations} summarizes the progression. The search was motivated by a consistent failure mode: naive formulations either collapse to trivial solutions (cumulative losses) or drive gates toward identity (maximize-family losses). We describe each family below.
38	
39	\paragraph{Cumulative losses (v1--v2).} These losses accumulate GAR contributions across layers, rewarding monotonically increasing attention. v1 collapsed because once the cumulative GAR exceeded the threshold, the loss gradient vanished and gates froze. v2 added an $\varepsilon$-stabilization term to the cumulative product, but numerical instability from the product of 28 per-layer terms dominated, and training followed the same trajectory.
40	
41	\paragraph{Maximize losses (v3--v5).} These losses directly maximize mean GAR ($-\text{mean}(\text{GAR})$). The unbounded objective rewards full pass-through ($g \to 1.0$), collapsing gate diversity (std $<$ 0.025). At $\lambda$=2 (v3), gates froze within 100 steps; at $\lambda$=10 (v3b), convergence to identity accelerated; at $\lambda$=1 (v5), rebalancing delayed but did not prevent the same degenerate solution.
42	
43	\paragraph{Smooth saturation (v6).} This bounded the reward using a saturating function, intended to prevent the unbounded growth of maximize losses. In practice, the loss landscape remained monotonic in $g$, and training followed the same terminal trajectory as the maximize family, only more slowly.
44	
45	\paragraph{MSE + gate diversity (v7).} The MSE formulation provides bidirectional pressure: GAR above $\tau$ incurs the same penalty as GAR below $\tau$, preventing the runaway optimization of maximize losses. The gate diversity regularizer ($\mathcal{L}_\text{div}$) enforces a minimum standard deviation across per-layer gate values, preventing all gates from collapsing to a uniform value. This combination is the only one that achieved stable convergence (GAR-ours = 0.50, PPL = 2.78).
46	
47	\begin{table*}[t]
48	\centering\footnotesize
49	\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration (v7).}
50	\label{tab:loss-iterations}
51	\begin{tabular}{l l l p{5.8cm} c c}
52	\toprule
53	 & \textbf{Loss Family} & \textbf{Status} & \textbf{Failure Mechanism} & \textbf{GAR} & \textbf{PPL} \\
54	\midrule
55	v1  & Cumulative            & \texttimes~GAR loss $\to$ 0     & GAR loss collapses to zero once threshold is reached; gate gradients vanish at equilibrium & ---  & ---  \\
56	v2  & Cumulative + $\varepsilon$ & \texttimes~same trajectory & Numerical instability from cumulative product; $\varepsilon$-stabilization insufficient & ---  & ---  \\
57	v3  & Maximize ($\lambda$=2)  & \texttimes~gate frozen        & Unbounded reward drives gates toward identity (all-pass); no layer selectivity & ---  & ---  \\
58	v3b & Maximize ($\lambda$=10) & \texttimes~identity collapse   & Higher $\lambda$ accelerates convergence to same degenerate identity solution & ---  & ---  \\
59	v5  & Maximize ($\lambda$=1)  & \texttimes~identity collapse   & Rebalancing delays but does not prevent identity collapse & ---  & ---  \\
60	v6  & Smooth saturation       & \texttimes~identity collapse   & Monotonic reward identical to maximize in practice; boundedness slows but does not alter terminal trajectory & ---  & ---  \\
61	v7  & MSE + gate div          & \checkmark~\textbf{converged}  & \textbf{Bidirectional penalty prevents identity collapse; gate diversity regularizer enforces layer selectivity} & 0.50 & 2.78 \\
62	\bottomrule
63	\end{tabular}
64	\end{table*}
65	
66	\section{Instruction Retention Details}\label{sec:appendix-ir}
67	
68	To evaluate whether GAR improvements translate to downstream task performance, we test instruction retention across 18 system-prompt constraint types using the ThreadGate checkpoint with $\beta$\,=\,3 steering on $N$\,=\,200 held-out conversations. Each constraint type requires the model to follow a specific instruction embedded in the system prompt (e.g., ``always respond in bullet points'', ``never use the word X'', ``include a summary at the end''). This evaluation bridges the gap between our attention-level metric (GAR) and observable model behavior.
69	
70	\paragraph{Evaluation protocol.} For each conversation, we inject a constraint into the system prompt and evaluate compliance across all assistant turns. A turn is compliant if it satisfies the constraint according to rule-based checkers (for format, count, and position constraints) or GPT-4-based evaluation (for content constraints, which require semantic judgment). We use the same 18 constraint types across all conversations, yielding $N$\,=\,54 paired evaluations (18 types $\times$ 3 conversations per type) for the McNemar analysis.
71	
72	\paragraph{Per-category results.} Table~\ref{tab:ir-results} reports per-category compliance rates. Content constraints---which require attending to and recalling specific system-prompt instructions across turns---show the largest improvement (+23.8\,pp), consistent with GAR measuring attention to goal tokens. This category includes constraints like ``mention X in every response'' and ``always reference the original topic,'' which require sustained attention to the system prompt. Position constraints (e.g., ``start each response with Y'') show a modest improvement (+6.7\,pp), as they partially depend on goal-token attention. Format (e.g., ``use bullet points'') and count constraints (e.g., ``exactly 3 sentences'') show no change, consistent with these being procedural patterns that are cached in the model's generation routine rather than requiring ongoing attention to the system prompt.
73	
74	\paragraph{Correlation analysis.} The GAR-compliance correlation ($r$\,=\,0.200, $p$\,=\,0.007) is statistically significant but modest, suggesting that attention to goal tokens is one of several factors in instruction compliance. Other factors likely include the model's procedural memory for format constraints, the specificity of the constraint (vague constraints are harder regardless of attention), and the interaction between constraint type and conversation topic. McNemar's test ($p$\,=\,0.077) is marginally significant for the overall compliance improvement, reflecting the small sample size (18 constraint types). These results are exploratory and pending multi-model confirmation.
75	
76	Figure~\ref{fig:ir-bar} visualizes the per-category breakdown.
77	
78	\begin{figure}[h]
79	  \centering
80	  \includegraphics[width=\columnwidth]{fig_instruction_retention.pdf}
81	  \caption{Instruction retention by constraint category under $\beta$\,=\,3 steering. Content constraints benefit most (+23.8\,pp); format and count constraints are unaffected.}
82	  \label{fig:ir-bar}
83	\end{figure}
84	
85	\begin{table}[h]
86	\centering\small
87	\caption{Instruction retention by constraint category ($\beta$\,=\,3 steering on ThreadGate checkpoint). Content constraints benefit most from increased goal attention.}
88	\label{tab:ir-results}
89	\begin{tabular}{lccc}
90	\toprule
91	\textbf{Category} & $\beta$\,=\,0 & $\beta$\,=\,3 & $\Delta$ \\
92	\midrule
93	Content    & 61.9\% & 85.7\% & +23.8\,pp \\
94	Position   & 66.7\% & 73.3\% & +6.7\,pp \\
95	Count      & 100\%  & 100\%  & 0 \\
96	Format     & 100\%  & 100\%  & 0 \\
97	\midrule
98	\textbf{Overall} & 75.9\% & 87.0\% & +11.1\,pp \\
99	\bottomrule
100	\end{tabular}
101	\end{table}
102	
103	\section{Long-Conversation AR Evaluation}\label{sec:appendix-n5}
104	
105	The main results (Table~\ref{tab:four-way}) report AR GAR from $N$\,=\,50 held-out conversations with a mean of 3.6 user turns. Table~\ref{tab:n5-ar} presents complementary results on $N$\,=\,5 conversations with 10 turns each, testing whether the observed patterns generalize beyond the training distribution's conversation length.
106	
107	\paragraph{Gating advantage vanishes at length.} In these longer dialogues, the gating advantage observed in shorter conversations vanishes: all fine-tuned variants collapse to AR GAR-ours of 0.015--0.025, compared to 0.030--0.064 in the shorter evaluation. ThreadGate's advantage over LoRA-only shrinks from 1.7$\times$ (0.064 vs.\ 0.037 in the $N$\,=\,50 evaluation) to 0.64$\times$ (0.016 vs.\ 0.025), actually reversing the ordering. This reversal is not statistically robust given the small sample ($N$\,=\,5) but directionally suggests that architectural modifications provide diminishing returns as conversation length increases and exposure bias accumulates.
108	
109	\paragraph{Convergence to base.} By turn~10, all fine-tuned variants converge to within 2$\times$ of the base model's GAR, compared to 3.4$\times$ at turn~1 in the shorter evaluation. This convergence is consistent with exposure bias compounding multiplicatively over turns: each model-generated turn introduces additional distributional drift from the teacher-forced training regime, and by turn~10 the accumulated drift overwhelms any gating or LoRA signal, leaving only the base model's intrinsic attention patterns.
110	
111	\paragraph{Caveats.} The $N$\,=\,5 sample size limits statistical power, and the 10-turn conversations may differ systematically from the 3--5 turn training distribution in ways beyond length (e.g., topic complexity, user engagement patterns). We present these results as directional evidence rather than definitive conclusions.
112	
113	\begin{table}[h]
114	\centering\small
115	\caption{AR GAR-ours on $N$\,=\,5 ten-turn conversations. The gating advantage observed in Table~\ref{tab:four-way} ($N$\,=\,50, mean 3.6 turns) diminishes with conversation length.}
116	\label{tab:n5-ar}
117	\begin{tabular}{lcc}
118	\toprule
119	\textbf{Configuration} & \textbf{AR GAR-O} & \textbf{$\Delta$ vs.\ Table~\ref{tab:four-way}} \\
120	\midrule
121	Base & 0.012 & $-$0.007 \\
122	\midrule
123	ThreadGate & 0.016 & $-$0.048 \\
124	\;+\,PCGrad & 0.015 & $-$0.015 \\
125	Uniform Gate & 0.015 & $-$0.018 \\
126	LoRA-only & 0.025 & $-$0.012 \\
127	\bottomrule
128	\end{tabular}
129	\end{table}
130	
131	\section{Statistical Test Details}\label{sec:appendix-stats}
132	
133	All statistical tests reported in the main text use non-parametric methods due to the non-normal, heavy-tailed distribution of per-conversation GAR values. Table~\ref{tab:stat-tests} consolidates the full results.
134	
135	\paragraph{Wilcoxon signed-rank tests.} We use paired Wilcoxon signed-rank tests for all pairwise configuration comparisons under AR evaluation, treating each conversation as a paired observation. The TG vs.\ LoRA-only comparison ($p$\,=\,0.004, $r$\,=\,0.454) confirms that turn-conditioned gating provides a statistically significant but modest improvement. The TG vs.\ +PCGrad comparison ($p$\,=\,0.002) shows that resolving gradient conflict is actively harmful. Gate turn conditioning uses an unpaired Wilcoxon test across 28 layers.
136	
137	\paragraph{Bootstrap confidence intervals.} The 95\% CIs in Table~\ref{tab:four-way} are computed via 10,000 bootstrap resamples of per-conversation mid-turn GAR averages (turns 2--$T$), using the percentile method.
138	
139	\paragraph{Effect sizes.} We report rank-biserial correlation $r = Z / \sqrt{N}$ as the effect size for Wilcoxon tests, where $Z$ is the standardized test statistic and $N$ is the number of observations. By standard conventions: $r < 0.3$ is small, $0.3 \leq r < 0.5$ is medium, and $r \geq 0.5$ is large. The TG vs.\ LoRA-only effect ($r$\,=\,0.454) is medium, and TG vs.\ Base ($r$\,=\,0.802) is large.
140	
141	\paragraph{Multiple comparisons.} We report uncorrected $p$-values throughout, as our comparisons are hypothesis-driven (each tests a specific causal exclusion) rather than exploratory. Applying Bonferroni correction to the 4 primary AR comparisons would adjust the significance threshold to 0.0125; all reported significant results ($p \leq 0.004$) survive this correction.
142	
143	\begin{table}[h]
144	\centering\small
145	\caption{Consolidated statistical tests. All AR comparisons use $N$\,=\,50 conversations (39 with $\geq$3 turns); gate conditioning uses 28 layers.}
146	\label{tab:stat-tests}
147	\begin{tabular}{llcc}
148	\toprule
149	\textbf{Comparison} & \textbf{Test} & $p$ & $r$ \\
150	\midrule
151	\multicolumn{4}{l}{\emph{AR GAR-ours ($\beta$\,=\,0)}} \\
152	TG vs.\ Base & Wilcoxon & $<$0.001 & 0.802 \\
153	TG vs.\ LoRA-only & Wilcoxon & 0.004 & 0.454 \\
154	TG vs.\ +PCGrad & Wilcoxon & 0.002 & --- \\
155	SS vs.\ TG & Wilcoxon & $<$0.001 & 0.869 \\
156	\midrule
157	\multicolumn{4}{l}{\emph{Gate conditioning (28 layers)}} \\
158	Turn 1 vs.\ Turn 21 & Wilcoxon & $3.7\!\times\!10^{-8}$ & 0.975 \\
159	\midrule
160	\multicolumn{4}{l}{\emph{Instruction retention}} \\
161	$\beta$\,=\,0 vs.\ $\beta$\,=\,3 & McNemar & 0.077 & --- \\
162	GAR--compliance & Pearson & 0.007 & 0.200 \\
163	\bottomrule
164	\end{tabular}
165	\end{table}
166	
167	\section{Llama-3.1-8B Complete Results}\label{sec:appendix-llama}
168	
169	Table~\ref{tab:llama-full} presents the complete Llama-3.1-8B-Instruct results, complementing the summary in \S\ref{subsec:cross-model}. Three configurations were trained (Base, ThreadGate, LoRA-only) using the same training pipeline as Qwen-2.5-7B (8K UltraChat, 3 epochs, LoRA rank 16). Training required 7.0--7.3 hours per variant on the same GPU.
170	
171	\paragraph{Teacher-forced evaluation.} TF GAR-ours is 0.484 (TG) and 0.481 (LoRA-only), confirming that gating provides zero benefit under teacher forcing on Llama, consistent with the Qwen results (0.50 vs.\ 0.50).
172	
173	\paragraph{Autoregressive evaluation.} AR evaluation uses $N$\,=\,20 mid-turn conversations (turns 3--$T$, excluding the first two turns to avoid initialization effects). The AR GAR distribution is heavy-tailed: the coefficient of variation exceeds 100\% for ThreadGate (mean 0.043, std 0.100), and 5\% of turn-level measurements exhibit sporadic attention spikes (GAR $\geq$ 0.4). We therefore report both mean and median.
174	
175	\paragraph{Gate profile.} Llama's gate profile differs qualitatively from Qwen's: Qwen shows minimum attenuation at early layers (L1\,=\,0.793, L5\,=\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719, L24\,=\,0.809). Despite this architectural difference, both models converge toward identity under NTP pressure, and the TF-AR gap is comparable (27$\times$ by median for Llama vs.\ 8--17$\times$ for Qwen).
176	
177	\begin{table}[h]
178	\centering\small
179	\caption{Llama-3.1-8B-Instruct complete results. TF: teacher-forced ($N$\,=\,50); AR: autoregressive ($N$\,=\,20 for Base/TG/LoRA-only, $N$\,=\,50 for SS). Median is more representative due to heavy-tailed AR distributions (SS uses mean only).}
180	\label{tab:llama-full}
181	\resizebox{\columnwidth}{!}{%
182	\begin{tabular}{lcccc}
183	\toprule
184	& \multicolumn{2}{c}{\textbf{TF}} & \multicolumn{2}{c}{\textbf{AR}} \\
185	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
186	& GAR-O & PPL & GAR-O (mean) & GAR-O (med) \\
187	\midrule
188	Base & 0.017 & 3.45 & 0.009 & 0.009 \\
189	ThreadGate & 0.484 & 2.57 & 0.043 & 0.018 \\
190	LoRA-only & 0.481 & 2.60 & 0.028 & 0.018 \\
191	\textbf{SS} & 0.477 & 2.82 & \textbf{0.166} & --- \\
192	\bottomrule
193	\end{tabular}}
194	\end{table}
195	
196	\begin{figure}[t]
197	  \centering
198	  \includegraphics[width=\columnwidth]{fig_crossmodel.pdf}
199	  \caption{Cross-architecture validation. (a)~The TF-AR gap persists on Llama-3.1-8B (27$\times$ by median), exceeding Qwen's 8$\times$. (b)~Gate profiles on normalized depth: Qwen dips at early layers, Llama at late layers; architecture-dependent patterns, but both converge toward identity.}
200	  \label{fig:crossmodel}
201	\end{figure}
202	
203	\paragraph{Cross-model summary.} Table~\ref{tab:crossmodel-detail} consolidates the cross-model comparison, showing TF GAR, AR GAR, PPL, and gap ratios side by side for both architectures. The consistent pattern---TF GAR $\approx$ 0.5, AR GAR $\ll$ 0.1, gap $\geq$ 7.9$\times$---across two architectures with different layer counts, attention head configurations, and pre-training corpora provides strong evidence that exposure bias is architecture-independent. Notably, Llama's larger gaps (11.2--17.2$\times$ vs.\ 7.9--13.5$\times$) may reflect its deeper architecture (32 vs.\ 28 layers), which allows more layers for distributional drift to compound through.
204	
205	\input{../artifacts/appendix_expansion/tab_crossmodel_detail.tex}
206	
207	\paragraph{GAR-Dongre cross-model comparison.} GAR-Dongre shows negligible distribution shift on Llama (AR/TF ratio 1.002$\times$), compared to 1.28$\times$ on Qwen. This confirms the mechanism specificity finding: exposure bias selectively disrupts the concentrated last-token attention pattern (GAR-ours) while leaving the diffuse all-token attention (GAR-Dongre) unaffected across both architectures.
208	
209	\paragraph{Training details.} Llama variants used the same pipeline as Qwen: 8K UltraChat conversations, LoRA rank 16 targeting $q$/$v$ projections, 3 epochs. Training loss converged to 0.929 (LoRA-only) and 0.934 (ThreadGate); the slight difference is attributable to the additional GAR loss component. Wall-clock time was 7.0h (LoRA-only) and 7.3h (ThreadGate), approximately 17\% longer than Qwen due to Llama's larger layer count (32 vs.\ 28 layers).
210	
211	\paragraph{Phase 1 diagnostics.} Before fine-tuning, we confirmed that Llama exhibits the same goal attention decay as Qwen. Base model GAR decays from 0.026 (turn 1) to 0.003 (turn 10), a 90\% decline. This is steeper than Qwen's 70.8\% decline, suggesting that attention decay may be more severe in Llama's architecture despite its larger head count (32 vs.\ 28 KV heads).
212	
213	\paragraph{Cross-model gradient analysis.} Table~\ref{tab:gradient-crossmodel} compares NTP--GAR gradient interaction between the two architectures. Both models exhibit near-orthogonal gradients (cosine similarity $\approx$\,0), not systematic conflict: Qwen shows a slight negative mean ($-$0.042) while Llama is marginally positive (+0.005). NTP gradients dominate GAR by 14.7$\times$ on Qwen and 25.7$\times$ on Llama, indicating that the auxiliary signal is overwhelmed by magnitude rather than opposed by direction. The cross-model consistency---near-zero cosine similarity and order-of-magnitude NTP dominance on both architectures---reinforces the \emph{modus tollens} argument (\S\ref{subsec:pcgrad}): gradient conflict is not the root cause of the TF-AR gap.
214	
215	\begin{table}[h]
216	\centering\small
217	\caption{Cross-model NTP--GAR gradient interaction. Gradients are near-orthogonal on both architectures; NTP magnitude dominates GAR by 15--26$\times$.}
218	\label{tab:gradient-crossmodel}
219	\begin{tabular}{lcc}
220	\toprule
221	\textbf{Metric} & \textbf{Qwen-7B} & \textbf{Llama-8B} \\
222	\midrule
223	Mean cos sim & $-$0.042 & +0.005 \\
224	Neg-layer \% & 67.9\% & 53.1\% \\
225	NTP/GAR mag ratio & 14.7$\times$ & 25.7$\times$ \\
226	\bottomrule
227	\end{tabular}
228	\end{table}
229	
230	\section{Additional Visualizations}\label{sec:appendix-viz}
231	
232	This section presents extended visualizations referenced in the main text. Each figure examines a different aspect of the gating behavior and its failure under autoregressive generation.
233	
234	\subsection{Gate Profile Heatmap}
235	
236	Figure~\ref{fig:gate-heatmap} shows the per-layer gate values across all training configurations for both Qwen-2.5-7B (28 layers) and Llama-3.1-8B (32 layers). The key observation is that early layers consistently receive the lowest gate values across all conditions, suggesting that these layers contribute more dispensable computations for the NTP objective. The pattern is remarkably consistent across ThreadGate, Uniform Gate, and PCGrad variants, indicating that gate-value allocation is driven primarily by the NTP loss landscape rather than the GAR auxiliary objective.
237	
238	\begin{figure*}[h]
239	\centering
240	\includegraphics[width=0.95\textwidth]{fig_gate_profile_heatmap.pdf}
241	\caption{Per-layer gate values across training for Qwen-2.5-7B (28 layers $\times$ 5 conditions) and Llama-3.1-8B (32 layers $\times$ 1 condition). Early layers (L1, L4--5) consistently receive the lowest gate values across conditions.}
242	\label{fig:gate-heatmap}
243	\end{figure*}
244	
245	\subsection{Cross-Model Gate Profile Comparison}
246	
247	Figure~\ref{fig:gate-crossmodel} compares gate profiles between the two architectures. Qwen-2.5-7B shows minimum gate values at early layers (L1\,=\,0.793, L5\,=\,0.797), suggesting these layers are most amenable to attenuation without disrupting NTP. Llama-3.1-8B instead shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719), indicating that architecturally distinct models learn different layer-importance hierarchies. Both profiles converge toward identity at their respective final layers, consistent with NTP gradient pressure dominating gate optimization at output-adjacent layers.
248	
249	\begin{figure*}[h]
250	\centering
251	\includegraphics[width=0.95\textwidth]{fig_gate_profile_crossmodel.pdf}
252	\caption{Side-by-side gate profiles for Qwen-2.5-7B and Llama-3.1-8B. Qwen dips at early layers (L1\,=\,0.793, L5\,=\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719). Both models learn layer-selective gating but with architecture-dependent patterns.}
253	\label{fig:gate-crossmodel}
254	\end{figure*}
255	
256	\subsection{Per-Turn AR GAR Decay}
257	
258	Figure~\ref{fig:ar-gar-perturn} visualizes the monotonic decay of GAR across conversation turns under autoregressive generation. Qwen base drops 85\% from turn 1 to turn 10; Llama base drops 90\%. The ThreadGate-trained model shows slight elevation in absolute GAR values but follows the same decay pattern, confirming that training-time GAR optimization does not alter the fundamental decay dynamic during generation. This per-turn view complements the aggregate TF-AR gap reported in Table~\ref{tab:four-way}: the gap is not a fixed offset but grows with conversation length, consistent with cumulative exposure bias.
259	
260	\begin{figure}[h]
261	\centering
262	\includegraphics[width=\columnwidth]{fig_ar_gar_perturn.pdf}
263	\caption{GAR decays monotonically across turns under autoregressive generation. Qwen base drops 85\% (turn 1$\to$10), Llama base drops 90\%. The ThreadGate-trained model (AR) shows slight elevation but the same decay pattern, confirming that training-time GAR optimization does not transfer to generation.}
264	\label{fig:ar-gar-perturn}
265	\end{figure}
266	
267	\subsection{Bootstrap Confidence Intervals}
268	
269	Figure~\ref{fig:bootstrap-ci} shows the bootstrap resampling distributions underlying the 95\% CIs reported in Table~\ref{tab:four-way}.
270	
271	\begin{figure}[h]
272	  \centering
273	  \includegraphics[width=\columnwidth]{fig_bootstrap_ci.pdf}
274	  \caption{Bootstrap CI distributions for AR GAR-ours (ThreadGate vs.\ LoRA-only, $N$\,=\,50, 10K resamples). Distributions overlap substantially, consistent with the modest effect size ($r$\,=\,0.454).}
275	  \label{fig:bootstrap-ci}
276	\end{figure}
277	
278	\subsection{Gate Value Distributions}
279	
280	Figure~\ref{fig:gate-distribution} shows the full distribution of per-layer gate values for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\sim$0.94--0.96, concentrated between 0.9 and 1.0), confirming that the gating mechanism provides minimal modulation regardless of the specific variant. The distributions are right-skewed with a sharp cutoff at 1.0, reflecting NTP pressure pushing gates toward identity.
281	
282	\begin{figure}[h]
283	\centering
284	\includegraphics[width=\columnwidth]{fig_gate_distribution.pdf}
285	\caption{Per-layer gate value distributions for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\sim$0.94--0.96), confirming minimal modulation from the gating mechanism.}
286	\label{fig:gate-distribution}
287	\end{figure}
288	
289	\subsection{Training Loss Curves}
290	
291	Figure~\ref{fig:training-loss} shows the NTP, GAR, and total loss trajectories during training. GAR loss collapses to near-zero within the first epoch across all variants, indicating rapid convergence of the auxiliary objective under teacher forcing. NTP loss converges normally to ${\sim}$0.93 by epoch 3. The fast GAR convergence is not itself pathological---it indicates successful optimization under the training distribution. The pathology emerges only at the transition to autoregressive generation, where the learned attention patterns fail to transfer.
292	
293	\begin{figure*}[h]
294	\centering
295	\includegraphics[width=0.95\textwidth]{fig_training_loss_curves.pdf}
296	\caption{NTP, GAR, and total loss trajectories. GAR loss collapses to near-zero within the first epoch across all variants, while NTP loss converges normally.}
297	\label{fig:training-loss}
298	\end{figure*}
299	
300	\subsection{Full Attention Steering Results}\label{sec:appendix-steering}
301	
302	\begin{table*}[t]
303	\centering\small
304	\caption{Full attention steering results across evaluation settings.
305	\textbf{Bold} indicates the operating point cited in the main text ($\beta$\,=\,5).
306	A visual gap separates the phase-transition boundary: GAR jumps sharply between $\beta$\,=\,2 and $\beta$\,=\,3 across all settings.}
307	\label{tab:steering-full}
308	\begin{tabular}{r cc cc cc}
309	\toprule
310	 & \multicolumn{2}{c}{\textbf{$N$\,=\,5, Gen}} & \multicolumn{2}{c}{\textbf{$N$\,=\,50, Gen}} & \multicolumn{2}{c}{\textbf{$N$\,=\,200, TF}} \\
311	\cmidrule(lr){2-3} \cmidrule(lr){4-5} \cmidrule(lr){6-7}
312	$\beta$ & GAR & PPL & GAR & PPL & GAR & PPL \\
313	\midrule
314	0   & .028 & 1.41 & $.064 \pm .081$ & $1.43 \pm .10$ & .535 & 2.62 \\
315	0.5 & .029 & 1.39 & ---             & ---             & ---  & ---  \\
316	1   & .035 & 1.36 & ---             & ---             & ---  & ---  \\
317	2   & .062 & 1.41 & $.128 \pm .110$ & $1.48 \pm .14$ & .611 & 2.69 \\
318	\addlinespace[3pt]
319	3   & ---  & ---  & $.556 \pm .060$ & $1.56 \pm .17$ & .788 & 2.93 \\
320	4   & ---  & ---  & $.644 \pm .061$ & $1.67 \pm .22$ & .817 & 3.49 \\
321	\textbf{5}  & \textbf{.680} & \textbf{1.91} & $\mathbf{.727 \pm .061}$ & $\mathbf{1.77 \pm .27}$ & \textbf{.833} & \textbf{6.15} \\
322	10  & .959 & 4.22 & $.961 \pm .015$ & $3.45 \pm 1.78$ & .977 & 505.2 \\
323	\bottomrule
324	\end{tabular}
325	\end{table*}
326	
327	\begin{figure}[h]
328	  \centering
329	  \includegraphics[width=\columnwidth]{fig_steering_standalone.pdf}
330	  \caption{Detailed $\beta$-steering trade-off ($N$\,=\,50). GAR-ours (top) increases monotonically with $\beta$; PPL (bottom) remains stable below $\beta$\,=\,3 (9\% cost), then rises sharply. The $\beta$\,=\,3 operating point (circled) achieves 8.7$\times$ GAR recovery while crossing the TF baseline, representing the optimal trade-off.}
331	  \label{fig:steering-standalone}
332	\end{figure}
333	
334	\section{Per-Layer Gate Profile}\label{sec:appendix-gate-profile}
335	
336	Table~\ref{tab:gate-profile} reports the final per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct (28 layers). Gate values are averaged across all tokens in the evaluation set. Layers 1 and 5 show the lowest gate values (0.793 and 0.797), indicating these layers are most amenable to attenuation without disrupting NTP. Layers 26--27 converge to $\geq$0.988, consistent with NTP gradient pressure dominating at output-adjacent layers. The mean across all layers is 0.947 ($\sigma$\,=\,0.051).
337	
338	\begin{table}[h]
339	\centering\small
340	\caption{Per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct. Min values (L1, L5) in bold.}
341	\label{tab:gate-profile}
342	\resizebox{\columnwidth}{!}{%
343	\begin{tabular}{cccccccc}
344	\toprule
345	L0 & L1 & L2 & L3 & L4 & L5 & L6 & L7 \\
346	.883 & \textbf{.793} & .996 & .988 & .984 & \textbf{.797} & .961 & .918 \\
347	\midrule
348	L8 & L9 & L10 & L11 & L12 & L13 & L14 & L15 \\
349	.965 & .934 & .969 & .918 & .926 & .941 & .930 & .965 \\
350	\midrule
351	L16 & L17 & L18 & L19 & L20 & L21 & L22 & L23 \\
352	.941 & .910 & .961 & .965 & .973 & .988 & .969 & .980 \\
353	\midrule
354	L24 & L25 & L26 & L27 & \multicolumn{4}{c}{Summary} \\
355	.980 & .984 & .988 & 1.00 & \multicolumn{4}{c}{$\bar{g}$\,=\,.947, $\sigma$\,=\,.051} \\
356	\bottomrule
357	\end{tabular}}
358	\end{table}
359	
360	The gate profile exhibits two notable patterns: (1)~a bimodal dip at L1 and L5, suggesting two distinct ``dispensable'' layer clusters in Qwen's architecture; (2)~monotonic increase from L17 to L27, indicating output-adjacent layers are progressively more critical for NTP. Seed 42 produces a similar profile (mean 0.934, min at L3--L5), confirming the pattern is not seed-dependent.
361	
362	\paragraph{Cross-model comparison.} See \S\ref{sec:appendix-viz} for the full cross-model gate profile comparison (Figure~\ref{fig:gate-crossmodel}). Llama-3.1-8B shows a qualitatively different profile---a V-shaped valley at mid-to-late layers rather than early-layer dips---suggesting architecture-dependent layer importance hierarchies.
363	
364	\section{Scheduled Sampling Implementation}\label{sec:appendix-ss}
365	
366	Our scheduled sampling implementation follows \citet{bengio2015scheduled} with modifications for multi-turn transformer training:
367	
368	\paragraph{Sampling schedule.} The model-generated context ratio $\rho$ increases linearly from 0 to 0.3 over 3 epochs. At each training step, a Bernoulli trial with probability $\rho$ determines whether the input prefix is replaced with model-generated tokens. The effective usage rate (29.7--37.1\%) is lower than the nominal schedule due to per-sample Bernoulli variance.
369	
370	\paragraph{Context generation.} When model-generated context is selected, the model autoregressively generates the assistant turns from the conversation prefix up to the current training position. The generated tokens replace the ground-truth assistant tokens in the input, while user turns remain unchanged. This preserves the multi-turn structure while introducing distributional diversity in the conditioning context.
371	
372	\paragraph{Training dynamics.} The scheduled sampling variant converges to similar final loss (NTP 0.932 vs.\ 0.930 for standard ThreadGate) but with higher variance in early epochs due to the stochastic context mixing (Figure~\ref{fig:ss-dynamics}). Gate profiles remain similar (mean 0.953 vs.\ 0.947, min at L4 vs.\ L1), indicating that scheduled sampling does not fundamentally alter gate optimization but rather improves the robustness of the learned attention patterns to distributional shift. Training time increases by 8--80\% across seeds (seed-dependent; dominated by GAR forward pass overhead): 6.5h (seed 42), 10.8h (seed 123), and 6.5h (seed 456) vs.\ 6.0h for standard ThreadGate on Qwen. Seed 456 exhibits consistent training dynamics with seeds 42 and 123.
373	
374	\begin{figure}[h]
375	  \centering
376	  \includegraphics[width=\columnwidth]{fig_ss_training_dynamics.pdf}
377	  \caption{Scheduled sampling training dynamics: sampling ratio $\rho$ ramps linearly from 0 to 0.3 (left axis); GAR loss (right axis) shows higher early-epoch variance due to stochastic context mixing.}
378	  \label{fig:ss-dynamics}
379	\end{figure}
380	
381	\section{Computational Cost Analysis}\label{sec:appendix-cost}
382	
383	\begin{table}[h]
384	\centering\small
385	\caption{Computational cost across training configurations. All experiments use a single NVIDIA RTX PRO 6000 (96\,GB VRAM).}
386	\label{tab:cost}
387	\resizebox{\columnwidth}{!}{%
388	\begin{tabular}{lcccc}
389	\toprule
390	\textbf{Config} & \textbf{Params} & \textbf{Time (h)} & \textbf{VRAM} & \textbf{Overhead} \\
391	\midrule
392	\multicolumn{5}{l}{\emph{Qwen-2.5-7B-Instruct}} \\
393	LoRA-only & 4.2M & 6.0 & 42\,GB & baseline \\
394	ThreadGate & 4.3M & 6.0 & 43\,GB & $+$57K \\
395	\;+\,PCGrad & 4.3M & 8.0 & 43\,GB & $+$33\% \\
396	Uniform Gate & 4.3M & 6.0 & 43\,GB & $+$57K \\
397	SS (s42) & 4.3M & 6.5 & 43\,GB & $+$8\% \\
398	SS (s123) & 4.3M & 10.8 & 43\,GB & $+$80\% \\
399	SS (s456) & 4.3M & 6.5 & 43\,GB & $+$8\% \\
400	\midrule
401	\multicolumn{5}{l}{\emph{Llama-3.1-8B-Instruct}} \\
402	LoRA-only & 4.2M & 7.0 & 45\,GB & baseline \\
403	ThreadGate & 4.3M & 7.3 & 46\,GB & $+$65K \\
404	\bottomrule
405	\end{tabular}}
406	\end{table}
407	
408	\paragraph{Parameter overhead.} ThreadGate adds ${\sim}$57K gate parameters for Qwen-2.5-7B (28 layers $\times$ 2K per gate MLP) and ${\sim}$65K for Llama-3.1-8B (32 layers), representing $<$0.001\% of the base model. LoRA adapters (rank 16, targeting $q$/$v$ projections) contribute 4.2M parameters across both architectures.
409	
410	\paragraph{Training time.} Standard variants (ThreadGate, Uniform Gate, LoRA-only) train in 6.0--7.3 hours. PCGrad adds ${\sim}$33\% overhead due to the per-step gradient projection computation. Scheduled sampling overhead varies: seed 42 adds only 8\% (6.5h) due to efficient batched generation, while seed 123 adds 80\% (10.8h) because of a longer generation schedule. The difference is due to the extended AR generation schedule in the seed 123 variant.
411	
412	\paragraph{Inference overhead.} Gate computation at inference time is negligible: a single 32$\to$64$\to$1 MLP forward pass per layer adds $<$0.1\% latency. $\beta$-steering requires identifying goal tokens (a one-time operation per conversation) and adding a constant bias to attention logits, with zero additional parameters.
413	
414	\section{Qualitative Steering Examples}\label{sec:appendix-examples}
415	
416	Table~\ref{tab:examples} illustrates the effect of $\beta$-steering on model behavior in a 4-turn conversation where the system prompt instructs ``Always respond in exactly three bullet points.''
417	
418	\begin{table*}[h]
419	\centering\small
420	\caption{Qualitative effect of $\beta$-steering on instruction following across conversation turns. System prompt: ``Always respond in exactly three bullet points.'' ThreadGate checkpoint, 4-turn conversation.}
421	\label{tab:examples}
422	\begin{tabular}{c p{5.5cm} p{5.5cm}}
423	\toprule
424	\textbf{Turn} & \textbf{$\beta$\,=\,0 (unsteered)} & \textbf{$\beta$\,=\,3 (steered)} \\
425	\midrule
426	1 & \checkmark~Three bullet points, on-topic & \checkmark~Three bullet points, on-topic \\
427	2 & \checkmark~Three bullet points, relevant & \checkmark~Three bullet points, relevant \\
428	3 & $\sim$~Four bullet points, partially on-topic & \checkmark~Three bullet points, on-topic \\
429	4 & \texttimes~Free-form paragraph, no bullets & \checkmark~Three bullet points, on-topic \\
430	\bottomrule
431	\end{tabular}
432	\end{table*}
433	
434	The pattern is consistent with the GAR decay analysis (\S\ref{sec:analysis}): unsteered models progressively lose attention to the system-prompt constraint, leading to format violations at later turns. Steering maintains goal-token attention, preserving instruction compliance. The per-category breakdown in Table~\ref{tab:ir-results} shows that content constraints benefit most from this effect.
435	
436	\section{Gradient Conflict Analysis}\label{sec:appendix-gradient}
437	
438	\begin{figure}[t]
439	  \centering
440	  \includegraphics[width=\columnwidth,height=0.42\textheight,keepaspectratio]{fig2_training_pcgrad.pdf}
441	  \caption{(a)~Training GAR convergence to target ($\tau$\,=\,0.5). (b)~PCGrad removes gradient conflict but $\mathcal{L}_\text{GAR}$ still collapses, confirming that gradient conflict is not the cause (\S\ref{subsec:pcgrad}).}
442	  \label{fig:training-pcgrad}
443	\end{figure}
444	
445	This section provides extended gradient interaction analysis supporting the PCGrad exclusion argument in \S\ref{subsec:pcgrad}. We measure per-layer cosine similarity between NTP and GAR gradients, gradient magnitude ratios, and the effect of PCGrad projection on these quantities.
446	
447	\paragraph{Gradient direction analysis.} Figure~\ref{fig:gradient-heatmap} visualizes the per-layer cosine similarity between NTP and GAR gradients across training epochs for both standard ThreadGate (v7) and PCGrad (v9) training. Under standard training, 79\% of layers show negative cosine similarity (gradient conflict) at epoch~0, declining to 68\% by epoch~2 as GAR loss converges to near-zero. This decline reflects diminishing GAR gradient magnitude rather than alignment improvement---as GAR loss approaches zero, the GAR gradient shrinks proportionally, making cosine similarity measurements less reliable (small gradients produce noisy direction estimates). Under PCGrad training, the conflict percentage decreases more slowly (79\%$\to$71\%), consistent with PCGrad projecting conflicting gradients onto the other's normal plane but not eliminating the underlying gradient conflict.
448	
449	\paragraph{Spatial patterns.} The early layers (L0--L5) and output-adjacent layers (L24--L27) show the strongest conflict, corresponding to the layers where gate values deviate most from identity (Figure~\ref{fig:gate-heatmap}). This spatial correlation is not causal: removing gradient conflict via PCGrad does not improve AR GAR, and gates at high-conflict layers are not systematically different from gates at low-conflict layers (Spearman $\rho$\,=\,$-$0.12, $p$\,=\,0.54 between gate value and conflict magnitude).
450	
451	\paragraph{Magnitude dominance.} NTP gradient magnitude dominates GAR by 7.5$\times$ at epoch~0 and 14.7$\times$ by epoch~2, as GAR loss converges while NTP loss remains at $\sim$0.93. This growing dominance means that even when directions oppose, the effective update direction is determined almost entirely by NTP. PCGrad addresses gradient conflict but not magnitude dominance---it projects conflicting gradients onto the other's normal plane (changing direction) but preserves relative magnitudes. The 7.5--14.7$\times$ magnitude ratio means that even after PCGrad projection, GAR contributes $<$7\% of the effective update magnitude, explaining why PCGrad is ineffective.
452	
453	\paragraph{Cross-model consistency.} Table~\ref{tab:gradient-crossmodel} confirms the pattern on Llama-3.1-8B: gradients are near-orthogonal (mean cosine $+$0.005, essentially zero) rather than systematically conflicting, with 25.7$\times$ NTP dominance. The Llama result is particularly informative because it shows that even without systematic gradient conflict (53\% negative layers, near chance), the same TF-AR gap persists. This cross-model evidence strengthens the \textit{modus tollens} argument: if gradient conflict were the cause, it should be present on both architectures; it is absent on Llama, yet the gap persists; therefore gradient conflict is not the cause.
454	
455	\begin{figure*}[h]
456	\centering
457	\includegraphics[width=0.95\textwidth]{fig_gradient_conflict_heatmap.pdf}
458	\caption{Per-layer cosine similarity between NTP and GAR gradients across training epochs. (a)~Standard training: conflict decreases from 79\% to 68\% of layers as GAR loss vanishes. (b)~PCGrad training: projection reduces conflict more slowly (79\%$\to$71\%) but does not improve AR GAR, ruling out gradient conflict as the cause (\S\ref{subsec:pcgrad}).}
459	\label{fig:gradient-heatmap}
460	\end{figure*}
461	
462	\section{Training Data Characteristics}\label{sec:appendix-data}
463	
464	All experiments use 8,000 multi-turn conversations sampled from the UltraChat \citep{ding2023ultrachat} training split. Table~\ref{tab:data-stats} summarizes the dataset characteristics. Conversations are truncated to 2,048 tokens; conversations shorter than 3 user turns are excluded to ensure sufficient multi-turn structure for GAR computation. The held-out evaluation sets use separate non-overlapping samples: $N$\,=\,50 conversations (mean 3.6 user turns) for the primary AR evaluation and $N$\,=\,5 conversations (10 turns each) for the long-conversation analysis (Appendix~\ref{sec:appendix-n5}).
465	
466	\begin{table}[h]
467	\centering\small
468	\caption{Training and evaluation data characteristics. All data from UltraChat \citep{ding2023ultrachat}.}
469	\label{tab:data-stats}
470	\begin{tabular}{lcc}
471	\toprule
472	\textbf{Property} & \textbf{Train} & \textbf{Eval (primary)} \\
473	\midrule
474	Conversations & 8,000 & 50 \\
475	Min user turns & 3 & 3 \\
476	Max sequence length & 2,048 & 2,048 \\
477	Source & UltraChat train & UltraChat train \\
478	Overlap & --- & non-overlapping \\
479	\bottomrule
480	\end{tabular}
481	\end{table}
482	
483	\section{Exposure Bias Scaling}\label{sec:appendix-eb-scaling}
484	
485	Figure~\ref{fig:eb-scaling} quantifies two scaling dimensions of the exposure bias phenomenon: cross-variant gap ratios (panel~a) and length-dependent gap compounding (panel~b).
486	
487	\paragraph{Cross-variant gaps.} On Qwen, ThreadGate achieves the smallest gap among standard variants (7.8$\times$) while PCGrad shows the largest (16.7$\times$, consistent with its counterproductive effect on AR GAR). Scheduled sampling reduces the gap to ${\sim}$1.3$\times$, the only variant approaching parity. The ordering of gap ratios (SS $\ll$ TG $<$ LoRA $<$ UG $<$ PCGrad) differs from the ordering of TF GAR (all $\approx$ 0.50), confirming that training-time optimization success does not predict inference-time robustness. On Llama, both ThreadGate and LoRA-only show $\sim$27$\times$ gaps (by median), larger than any Qwen variant. The consistently larger Llama gaps may reflect its deeper architecture (32 vs.\ 28 layers), which provides more layers for distributional drift to compound through.
488	
489	\paragraph{Length-dependent compounding.} Panel~(b) shows that the gap compounds with conversation length: at 3.6 mean turns ($N$\,=\,50), ThreadGate's gap is 8$\times$; at 10 turns ($N$\,=\,5), it widens to 31$\times$. The relationship is approximately linear in the number of turns on a log scale, suggesting that the per-turn drift contribution is roughly multiplicative. Extrapolating this trend suggests that at 20 turns the gap would exceed 100$\times$, making any training-time attention signal essentially undetectable. This length dependence is consistent with cumulative distributional drift---each model-generated turn introduces additional divergence from the teacher-forced training distribution, and by turn~10 the accumulated drift overwhelms any gating signal.
490	
491	\paragraph{Implications for deployment.} These scaling results have practical implications: (1)~for applications requiring sustained attention over many turns (e.g., long-form tutoring, multi-step reasoning), architectural modifications alone are insufficient---distributional robustification or inference-time intervention is necessary; (2)~the near-parity of scheduled sampling (${\sim}$1.3$\times$ gap) suggests that bridging the training-inference distribution gap is both necessary and sufficient for maintaining attention; (3)~the $\beta$-steering approach provides a complementary inference-time solution, but its effectiveness also depends on conversation length (Appendix~\ref{sec:appendix-steering-viz}).
492	
493	\begin{figure*}[h]
494	\centering
495	\includegraphics[width=0.95\textwidth]{fig_eb_scaling.pdf}
496	\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\sim}$1.3$\times$) is the only variant near parity. Llama gaps ($\sim$27$\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\times$ (3.6 turns) to 31$\times$ (10 turns).}
497	\label{fig:eb-scaling}
498	\end{figure*}
499	
500	\section{Per-Turn AR GAR Dynamics}\label{sec:appendix-ar-gar-dynamics}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "332e64ca-404e-47f8-a99c-deb2bd5ccc26",
  "isSidechain": true,
  "promptId": "52ff2238-2bff-43fb-88da-a3f0a815c702",
  "agentId": "aa7d450a33c4a6692",
  "type": "user",
  "uuid": "9046bf19-49b7-4ab6-8cb5-d1b3277d3e84",
  "sourceToolAssistantUUID": "332e64ca-404e-47f8-a99c-deb2bd5ccc26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-25T04:45:43.093Z_

Let me search for figure environments more systematically using grep:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9046bf19-49b7-4ab6-8cb5-d1b3277d3e84",
  "isSidechain": true,
  "agentId": "aa7d450a33c4a6692",
  "requestId": "req_011CbNgKYaQaiMD2MMrsXEC6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1d8dc5c6-9d64-4e1c-a96b-3389184682a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01L7iYgVsnXoVy9EHSEVUnmK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 15368,
      "cache_read_input_tokens": 50458,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15368,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-25T04:45:44.172Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01EAwJZzazQBnWajPVL3btqj`</summary>

```json
{
  "pattern": "\\\\begin\\{figure\\*?\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d8dc5c6-9d64-4e1c-a96b-3389184682a8",
  "isSidechain": true,
  "agentId": "aa7d450a33c4a6692",
  "requestId": "req_011CbNgKYaQaiMD2MMrsXEC6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "64e8b347-7f41-4b0a-9cf9-738125fdd9b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01L7iYgVsnXoVy9EHSEVUnmK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 15368,
      "cache_read_input_tokens": 50458,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15368,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-25T04:45:44.189Z_

<details><summary>↩ Tool result · `toolu_01EAwJZzazQBnWajPVL3btqj`</summary>

```text
&lt;persisted-output>
Output too large (32.2KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating--claude-sessions-director-e14ea3a0/4300e384-65b8-49ff-9336-5b8eeb6dbb5d/tool-results/toolu_01EAwJZzazQBnWajPVL3btqj.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex-12-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex-13-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex-14-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex:15:\begin{figure}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex-16-  \centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex-17-  \includegraphics[width=\columnwidth]{fig_ss_multiseed.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex-18-  \caption{Multi-seed AR GAR under scheduled sampling ($\beta$\,=\,0 and $\beta$\,=\,5, three seeds). Steering nearly eliminates seed variance (std: 0.047$\to$0.001).}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex-23-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex-24-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex-25-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex:26:\begin{figure}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex-27-  \centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex-28-  \includegraphics[width=\columnwidth]{fig3_gate_shift.pdf}
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "64e8b347-7f41-4b0a-9cf9-738125fdd9b8",
  "isSidechain": true,
  "promptId": "52ff2238-2bff-43fb-88da-a3f0a815c702",
  "agentId": "aa7d450a33c4a6692",
  "type": "user",
  "uuid": "a0d6cde3-9d43-4d40-bd55-274209652cad",
  "sourceToolAssistantUUID": "64e8b347-7f41-4b0a-9cf9-738125fdd9b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-25T04:45:44.581Z_

<details open><summary>🔧 Tool call — Grep · `toolu_019Pax5qeqz9736zNtQzXvu3`</summary>

```json
{
  "pattern": "\\\\includegraphics\\[width=",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections",
  "output_mode": "content",
  "context": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0d6cde3-9d43-4d40-bd55-274209652cad",
  "isSidechain": true,
  "agentId": "aa7d450a33c4a6692",
  "requestId": "req_011CbNgKYaQaiMD2MMrsXEC6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "742961a6-9e6c-41cb-87ae-cd138e691fc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01L7iYgVsnXoVy9EHSEVUnmK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 15368,
      "cache_read_input_tokens": 50458,
      "output_tokens": 285,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15368
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 285,
          "cache_read_input_tokens": 50458,
          "cache_creation_input_tokens": 15368,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15368,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-25T04:45:44.600Z_

<details><summary>↩ Tool result · `toolu_019Pax5qeqz9736zNtQzXvu3`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex-16-  \centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex:17:  \includegraphics[width=\columnwidth]{fig_ss_multiseed.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex-18-  \caption{Multi-seed AR GAR under scheduled sampling ($\beta$\,=\,0 and $\beta$\,=\,5, three seeds). Steering nearly eliminates seed variance (std: 0.047$\to$0.001).}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex-27-  \centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex:28:  \includegraphics[width=\columnwidth]{fig3_gate_shift.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex-29-  \caption{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \times 10^{-8}$). (b)~Distribution shift ($N$\,=\,5 pilot): the TF-AR GAR gap persists across all five variants. Pilot gaps (20--34$\times$) exceed final $N$\,=\,50 estimates (8--17$\times$; Table~\ref{tab:four-way}) due to smaller sample size.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex-29-  \centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex:30:  \includegraphics[width=\columnwidth]{fig_ss_gap_compression.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex-31-  \caption{Scheduled sampling compresses the TF-AR gap from 7.8$\times$ to ${\sim}$1.3$\times$, the only variant approaching parity across five training conditions.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex-39-  \centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex:40:  \includegraphics[width=\columnwidth]{fig4_attention_heatmap.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex-41-  \caption{Per-turn GAR-ours under AR generation ($N$\,=\,5 conversations, 10 turns). All fine-tuned variants cluster together (77--81\% decay; $\Delta$\,=\,3.3\,pp between ThreadGate and LoRA-only); Base decays 87.5\%. Gating adds zero incremental effect.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex-68-  \centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex:69:  \includegraphics[width=\columnwidth]{fig5_attention_steering.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex-70-  \caption{Inference-time $\beta$-steering recovers GAR from 0.064 to 0.727, confirming attention misallocation as the proximal cause (9\% PPL cost at $\beta$\,=\,3; phase transition at $\beta \in [2, 3]$).}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-79-  \centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:80:  \includegraphics[width=\columnwidth]{fig_instruction_retention.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-81-  \caption{Instruction retention by constraint category under $\beta$\,=\,3 steering. Content constraints benefit most (+23.8\,pp); format and count constraints are unaffected.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-197-  \centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:198:  \includegraphics[width=\columnwidth]{fig_crossmodel.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-199-  \caption{Cross-architecture validation. (a)~The TF-AR gap persists on Llama-3.1-8B (27$\times$ by median), exceeding Qwen's 8$\times$. (b)~Gate profiles on normalized depth: Qwen dips at early layers, Llama at late layers; architecture-dependent patterns, but both converge toward identity.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-239-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:240:\includegraphics[width=0.95\textwidth]{fig_gate_profile_heatmap.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-241-\caption{Per-layer gate values across training for Qwen-2.5-7B (28 layers $\times$ 5 conditions) and Llama-3.1-8B (32 layers $\times$ 1 condition). Early layers (L1, L4--5) consistently receive the lowest gate values across conditions.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-250-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:251:\includegraphics[width=0.95\textwidth]{fig_gate_profile_crossmodel.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-252-\caption{Side-by-side gate profiles for Qwen-2.5-7B and Llama-3.1-8B. Qwen dips at early layers (L1\,=\,0.793, L5\,=\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719). Both models learn layer-selective gating but with architecture-dependent patterns.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-261-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:262:\includegraphics[width=\columnwidth]{fig_ar_gar_perturn.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-263-\caption{GAR decays monotonically across turns under autoregressive generation. Qwen base drops 85\% (turn 1$\to$10), Llama base drops 90\%. The ThreadGate-trained model (AR) shows slight elevation but the same decay pattern, confirming that training-time GAR optimization does not transfer to generation.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-272-  \centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:273:  \includegraphics[width=\columnwidth]{fig_bootstrap_ci.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-274-  \caption{Bootstrap CI distributions for AR GAR-ours (ThreadGate vs.\ LoRA-only, $N$\,=\,50, 10K resamples). Distributions overlap substantially, consistent with the modest effect size ($r$\,=\,0.454).}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-283-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:284:\includegraphics[width=\columnwidth]{fig_gate_distribution.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-285-\caption{Per-layer gate value distributions for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\sim$0.94--0.96), confirming minimal modulation from the gating mechanism.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-294-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:295:\includegraphics[width=0.95\textwidth]{fig_training_loss_curves.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-296-\caption{NTP, GAR, and total loss trajectories. GAR loss collapses to near-zero within the first epoch across all variants, while NTP loss converges normally.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-328-  \centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:329:  \includegraphics[width=\columnwidth]{fig_steering_standalone.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-330-  \caption{Detailed $\beta$-steering trade-off ($N$\,=\,50). GAR-ours (top) increases monotonically with $\beta$; PPL (bottom) remains stable below $\beta$\,=\,3 (9\% cost), then rises sharply. The $\beta$\,=\,3 operating point (circled) achieves 8.7$\times$ GAR recovery while crossing the TF baseline, representing the optimal trade-off.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-375-  \centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:376:  \includegraphics[width=\columnwidth]{fig_ss_training_dynamics.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-377-  \caption{Scheduled sampling training dynamics: sampling ratio $\rho$ ramps linearly from 0 to 0.3 (left axis); GAR loss (right axis) shows higher early-epoch variance due to stochastic context mixing.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-439-  \centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:440:  \includegraphics[width=\columnwidth,height=0.42\textheight,keepaspectratio]{fig2_training_pcgrad.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-441-  \caption{(a)~Training GAR convergence to target ($\tau$\,=\,0.5). (b)~PCGrad removes gradient conflict but $\mathcal{L}_\text{GAR}$ still collapses, confirming that gradient conflict is not the cause (\S\ref{subsec:pcgrad}).}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-456-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:457:\includegraphics[width=0.95\textwidth]{fig_gradient_conflict_heatmap.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-458-\caption{Per-layer cosine similarity between NTP and GAR gradients across training epochs. (a)~Standard training: conflict decreases from 79\% to 68\% of layers as GAR loss vanishes. (b)~PCGrad training: projection reduces conflict more slowly (79\%$\to$71\%) but does not improve AR GAR, ruling out gradient conflict as the cause (\S\ref{subsec:pcgrad}).}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-494-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:495:\includegraphics[width=0.95\textwidth]{fig_eb_scaling.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-496-\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\sim}$1.3$\times$) is the only variant near parity. Llama gaps ($\sim$27$\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\times$ (3.6 turns) to 31$\times$ (10 turns).}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-507-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:508:\includegraphics[width=\columnwidth]{fig_kl_ar_gar_curves.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-509-\caption{Per-turn AR GAR trajectories for six Qwen-2.5-7B configurations (turns 1--5). All models show monotonic decay; Scheduled Sampling retains far higher GAR throughout (0.53$\to$0.39), while the remaining five variants cluster below 0.13 and decay rapidly.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-514-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:515:\includegraphics[width=\columnwidth]{fig_kl_ar_gar_bar.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-516-\caption{Mid-turn AR GAR comparison across six training configurations. Ranking from highest to lowest: Scheduled Sampling (0.423), ThreadGate (0.064), LoRA-only (0.037), Uniform Gate (0.033), PCGrad (0.030), Base (0.019).}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-654-  \centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:655:  \includegraphics[width=\columnwidth]{fig_perturn_qwen_detail.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-656-  \caption{Per-turn AR GAR-ours across six Qwen-2.5-7B configurations. Scheduled sampling (green) retains far higher GAR than all other variants, which cluster below 0.13 and decay rapidly.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-663-  \centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:664:  \includegraphics[width=0.95\textwidth]{fig_perturn_llama_detail.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-665-  \caption{Per-turn AR GAR decay on Llama-3.1-8B. (a)~Three-way comparison (Base, TG, LoRA-only; $N$\,=\,20, 4 turns). (b)~Extended Base decay profile ($N$\,=\,5, 10 turns), showing 90\% decline.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-692-  \centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:693:  \includegraphics[width=\columnwidth]{fig_gar_robustness_grouped.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-694-  \caption{Mid-turn GAR across four token-position definitions. SS raises all four above 0.36; TG only improves last-token and goal-only.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-711-  \centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:712:  \includegraphics[width=\columnwidth]{fig_mmlu_comparison.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-713-  \caption{MMLU 5-shot accuracy by category across training configurations. All variants remain within 1.2\,pp of the LoRA-only baseline across all categories.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-758-  \centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:759:  \includegraphics[width=0.95\textwidth]{fig_training_curves_6panel.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-760-  \caption{Training loss curves for all five Qwen conditions. NTP loss (left) converges to ${\sim}$0.93 across variants; GAR loss (center) collapses within epoch~1; total loss (right) is NTP-dominated. Training-time behavior is indistinguishable; the failure emerges only at inference.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-779-  \centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:780:  \includegraphics[width=0.95\textwidth]{fig_steering_perturn_4panel.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex-781-  \caption{Per-turn GAR under four $\beta$-steering strengths. At $\beta$\,=\,0, monotonic decay; at $\beta$\,=\,3, partial recovery with residual decay; at $\beta$\,=\,5, sustained high GAR; at $\beta$\,=\,10, saturation with catastrophic PPL.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex-10-  \centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex:11:  \includegraphics[width=\textwidth]{fig1_headline.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex-12-  \caption{Exposure bias destroys auxiliary attention losses. \textbf{(a)}~Goal attention decays 85--90\% across turns under AR generation on both Qwen-2.5-7B and Llama-3.1-8B. \textbf{(b)}~Under TF evaluation all variants reach GAR$\approx$0.50, but AR generation collapses GAR by 8--17$\times$ (log scale). \textbf{(c)}~Scheduled sampling compresses the TF--AR gap from 7.8$\times$ to 1.3$\times$ (Qwen) and 12.0$\times$ to 2.9$\times$ (Llama).}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "742961a6-9e6c-41cb-87ae-cd138e691fc7",
  "isSidechain": true,
  "promptId": "52ff2238-2bff-43fb-88da-a3f0a815c702",
  "agentId": "aa7d450a33c4a6692",
  "type": "user",
  "uuid": "b6f96254-d80f-4788-bd5e-e0974f01d1a9",
  "sourceToolAssistantUUID": "742961a6-9e6c-41cb-87ae-cd138e691fc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-25T04:45:54.849Z_

Perfect! Now I have comprehensive data. Let me compile the full figure inventory in a compact table format.

## Figure Environment Analysis - LaTeX Source

Based on my search of all specified section files, here's the complete inventory of figure environments:

| File | Line | Environment | Width | Figure File | Section Type |
|------|------|-------------|-------|-------------|--------------|
| introduction.tex | 9 | `figure*` | `\textwidth` | fig1_headline.pdf | Main Text |
| method.tex | 38 | `figure` | `\columnwidth` | fig4_attention_heatmap.pdf | Main Text |
| method.tex | 67 | `figure` | `\columnwidth` | fig5_attention_steering.pdf | Main Text |
| experiments.tex | 28 | `figure` | `\columnwidth` | fig_ss_gap_compression.pdf | Main Text |
| analysis.tex | 15 | `figure` | `\columnwidth` | fig_ss_multiseed.pdf | Main Text |
| analysis.tex | 26 | `figure` | `\columnwidth` | fig3_gate_shift.pdf | Main Text |
| appendix.tex | 78 | `figure` | `\columnwidth` | fig_instruction_retention.pdf | Appendix |
| appendix.tex | 196 | `figure` | `\columnwidth` | fig_crossmodel.pdf | Appendix |
| appendix.tex | 238 | `figure*` | `0.95\textwidth` | fig_gate_profile_heatmap.pdf | Appendix |
| appendix.tex | 249 | `figure*` | `0.95\textwidth` | fig_gate_profile_crossmodel.pdf | Appendix |
| appendix.tex | 260 | `figure` | `\columnwidth` | fig_ar_gar_perturn.pdf | Appendix |
| appendix.tex | 271 | `figure` | `\columnwidth` | fig_bootstrap_ci.pdf | Appendix |
| appendix.tex | 283 | `figure` | `\columnwidth` | fig_gate_distribution.pdf | Appendix |
| appendix.tex | 293 | `figure*` | `0.95\textwidth` | fig_training_loss_curves.pdf | Appendix |
| appendix.tex | 327 | `figure` | `\columnwidth` | fig_steering_standalone.pdf | Appendix |
| appendix.tex | 374 | `figure` | `\columnwidth` | fig_ss_training_dynamics.pdf | Appendix |
| appendix.tex | 438 | `figure` | `\columnwidth` (with height constraint) | fig2_training_pcgrad.pdf | Appendix |
| appendix.tex | 455 | `figure*` | `0.95\textwidth` | fig_gradient_conflict_heatmap.pdf | Appendix |
| appendix.tex | 493 | `figure*` | `0.95\textwidth` | fig_eb_scaling.pdf | Appendix |
| appendix.tex | 507 | `figure` | `\columnwidth` | fig_kl_ar_gar_curves.pdf | Appendix |
| appendix.tex | 514 | `figure` | `\columnwidth` | fig_kl_ar_gar_bar.pdf | Appendix |
| appendix.tex | 654 | `figure` | `\columnwidth` | fig_perturn_qwen_detail.pdf | Appendix |
| appendix.tex | 664 | `figure` | `0.95\textwidth` | fig_perturn_llama_detail.pdf | Appendix |
| appendix.tex | 692 | `figure` | `\columnwidth` | fig_gar_robustness_grouped.pdf | Appendix |
| appendix.tex | 712 | `figure` | `\columnwidth` | fig_mmlu_comparison.pdf | Appendix |
| appendix.tex | 759 | `figure*` | `0.95\textwidth` | fig_training_curves_6panel.pdf | Appendix |
| appendix.tex | 780 | `figure*` | `0.95\textwidth` | fig_steering_perturn_4panel.pdf | Appendix |

## Summary & Observations

**Main Text (6 figures):**
- 1 full-width (`figure*`, `\textwidth`): fig1_headline.pdf (introduction)
- 5 single-column (`figure`, `\columnwidth`): method (2), experiments (1), analysis (2)

**Appendix (21 figures):**
- 6 full-width (`figure*`): 2 at 0.95\textwidth, 4 at 0.95\textwidth
- 15 single-column (`figure`): mostly `\columnwidth`, 1 with `0.95\textwidth` (fig_perturn_llama_detail)

**Width Analysis:**
- **Single-column** (`\columnwidth`): 18 figures - suitable for vertical/narrow layouts
- **Multi-column** (`\textwidth` or `0.95\textwidth`): 9 figures - primarily supporting complex comparisons

**Conversion Potential:**
The main text figure (fig1_headline) at `\textwidth` could potentially be reviewed for conversion to `figure` + `\columnwidth` if the vertical conversion has made it tall enough. All main-text single-column figures are already optimized for narrow layouts. In the appendix, the `0.95\textwidth` figures (gate heatmaps, training curves, scaling analysis) are the candidates for evaluation—they were likely designed for side-by-side comparisons that the vertical layout may have already addressed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6f96254-d80f-4788-bd5e-e0974f01d1a9",
  "isSidechain": true,
  "agentId": "aa7d450a33c4a6692",
  "requestId": "req_011CbNgKpEVbJt4Z4dsKtVye",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ebfc0d10-709f-40e1-87c9-adb32dd71752",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/director_e14ea3a0",
  "sessionId": "4300e384-65b8-49ff-9336-5b8eeb6dbb5d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "temporal-foraging-pizza",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TXy2ABZFJ2Ugv9aVjbBN5m",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 7670,
      "cache_read_input_tokens": 65826,
      "output_tokens": 1402,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7670
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 1402,
          "cache_read_input_tokens": 65826,
          "cache_creation_input_tokens": 7670,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7670,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
