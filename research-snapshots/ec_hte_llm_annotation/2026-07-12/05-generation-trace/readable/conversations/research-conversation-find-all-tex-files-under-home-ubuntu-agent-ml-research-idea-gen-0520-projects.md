# Research conversation: Find all .tex files under /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/ and l

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 10
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-abc0a35aad20707c6.jsonl`
- **Structured JSON:** [`0751412b1fd376798434.json`](../../sessions/07/0751412b1fd376798434.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

10 recorded events

### User

_source line 1 · 2026-05-21T05:01:55.061Z_

Find all .tex files under /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/ and list them. Then read theory.tex and experiments.tex (or whatever the experiment section file is called) to extract: (1) all notation definitions (δ_s, Δτ, π̄, C_s, M_s, etc.), (2) all \label{} definitions, (3) proposition/corollary names and labels, (4) method name conventions used (e.g. "HB EC-HTE", "Strat. MLE", etc.), (5) any assumptions labeled (A1)-(A4). Report all of these in a structured format.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "bea3db89-b6ab-4557-9575-e64604389d66",
  "agentId": "abc0a35aad20707c6",
  "type": "user",
  "uuid": "5657d44a-8bbe-4f41-b399-b3210f6eca59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "069df309-e1d5-4181-acb0-1338e109ee71",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-21T05:01:56.648Z_

I'll help you find and analyze the .tex files in the paper directory. Let me start by locating all .tex files and then reading the relevant sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5657d44a-8bbe-4f41-b399-b3210f6eca59",
  "isSidechain": true,
  "agentId": "abc0a35aad20707c6",
  "requestId": "req_011CbF8KgxvzdtedvurKN4ve",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "884d3044-2ef4-429f-8287-1439c388f4c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "069df309-e1d5-4181-acb0-1338e109ee71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01USMsWbddEYTS7RzW4ZwQs3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27785,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27785,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 3 · 2026-05-21T05:01:56.761Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01WgtgqDgbV3GAf9GNeVnEG3`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "884d3044-2ef4-429f-8287-1439c388f4c2",
  "isSidechain": true,
  "agentId": "abc0a35aad20707c6",
  "requestId": "req_011CbF8KgxvzdtedvurKN4ve",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9b800133-3860-4aea-8bdb-535af7ff6b1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "069df309-e1d5-4181-acb0-1338e109ee71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01USMsWbddEYTS7RzW4ZwQs3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27785,
      "cache_read_input_tokens": 0,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 27785
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 121,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 27785,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 27785,
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

_source line 4 · 2026-05-21T05:01:56.781Z_

<details><summary>↩ Tool result · `toolu_01WgtgqDgbV3GAf9GNeVnEG3`</summary>

```text
docs/paper/theory.tex
docs/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b800133-3860-4aea-8bdb-535af7ff6b1a",
  "isSidechain": true,
  "promptId": "bea3db89-b6ab-4557-9575-e64604389d66",
  "agentId": "abc0a35aad20707c6",
  "type": "user",
  "uuid": "8647f2c0-8016-4ae9-8131-b5c5f26725ac",
  "sourceToolAssistantUUID": "9b800133-3860-4aea-8bdb-535af7ff6b1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "069df309-e1d5-4181-acb0-1338e109ee71",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-21T05:01:58.440Z_

Great! I found 2 .tex files. Now let me read both theory.tex and experiments.tex to extract the requested information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8647f2c0-8016-4ae9-8131-b5c5f26725ac",
  "isSidechain": true,
  "agentId": "abc0a35aad20707c6",
  "requestId": "req_011CbF8KpGifWNTg6t5dVx5J",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7ab522b8-dae6-4b42-83b4-d7e9cd3a422d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "069df309-e1d5-4181-acb0-1338e109ee71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NXnapAASi15E6viYKMrGyj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 983,
      "cache_read_input_tokens": 27785,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 983,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 6 · 2026-05-21T05:01:58.669Z_

<details open><summary>🔧 Tool call — Read · `toolu_01R4iLhTnE4YkE7TrKSZeEza`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ab522b8-dae6-4b42-83b4-d7e9cd3a422d",
  "isSidechain": true,
  "agentId": "abc0a35aad20707c6",
  "requestId": "req_011CbF8KpGifWNTg6t5dVx5J",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4ca08ab7-71d6-48ea-883e-91a76bcc52c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "069df309-e1d5-4181-acb0-1338e109ee71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NXnapAASi15E6viYKMrGyj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 983,
      "cache_read_input_tokens": 27785,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 983,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 7 · 2026-05-21T05:01:58.717Z_

<details><summary>↩ Tool result · `toolu_01R4iLhTnE4YkE7TrKSZeEza`</summary>

```text
1	% Requires preamble: \usepackage{amsthm,amsmath,amssymb}
2	% and: \newtheorem{proposition}{Proposition}
3	
4	\section{Bias Decomposition: When Debiasing Hurts}
5	\label{sec:theory}
6	
7	We formalize the bias that global misclassification correction introduces when subgroup error rates are heterogeneous.
8	Consider estimating the conditional average treatment effect (CATE) $\tau(z) = \mathbb{E}[Y(1) - Y(0) \mid Z = z]$, where $Z \in \{0, 1\}$ is a binary effect modifier observed only through a noisy annotation $\hat{Z}$.
9	The population consists of $K$ subgroups $S \in \{1, \ldots, K\}$ with weights $w_s = P(S{=}s)$, each characterized by a $2 \times 2$ confusion matrix $C_s$ with symmetric error rate $\pi_s = P(\hat{Z} \neq Z \mid S{=}s)$.
10	Standard practice estimates a single confusion matrix $\bar{C} = \sum_s w_s C_s$ from expert annotations and applies its inverse uniformly to all observations, with pooled error rate $\bar{\pi} = \sum_s w_s \pi_s$.
11	We show that when error rates vary across subgroups, this global procedure introduces a bias with an exact product form.
12	
13	We state four assumptions maintained throughout.
14	%
15	\begin{itemize}
16	\item[\textbf{(A1)}] \textit{Conditional independence:} misclassification depends only on the true label $Z$ and subgroup $S$, not on potential outcomes $Y(0), Y(1)$.
17	\item[\textbf{(A2)}] \textit{Symmetric misclassification:} $P(\hat{Z}{=}1 \mid Z{=}0, S{=}s) = P(\hat{Z}{=}0 \mid Z{=}1, S{=}s) = \pi_s$ for all $s$.
18	\item[\textbf{(A3)}] \textit{Balanced effect modifier:} $P(Z{=}0) = P(Z{=}1) = 0.5$. This simplifies the exposition; we discuss relaxation below.
19	\item[\textbf{(A4)}] \textit{Non-degeneracy:} $\pi_s \neq 0.5$ for all $s$, ensuring each $C_s$ is invertible.
20	\end{itemize}
21	
22	Under (A2)--(A3), the Bayesian mixing matrix $M_s$ (entries $M_s[\hat{z}, z] = P(Z{=}z \mid \hat{Z}{=}\hat{z}, S{=}s)$) coincides with $C_s$.
23	The global mixing matrix is $M_{\text{global}} = \sum_s w_s M_s$.
24	
25	\begin{proposition}[Bias Decomposition Identity]
26	\label{prop:bias_identity}
27	Under \textnormal{(A1)--(A4)}, the bias of global correction in subgroup $s$ at effect-modifier level $z$ is
28	\begin{align}
29	\mathrm{bias}_{\mathrm{global}}(z{=}0, s) &= +\frac{\delta_s \cdot \Delta\tau}{1 - 2\bar{\pi}}, \label{eq:bias_z0} \\
30	\mathrm{bias}_{\mathrm{global}}(z{=}1, s) &= -\frac{\delta_s \cdot \Delta\tau}{1 - 2\bar{\pi}}, \label{eq:bias_z1}
31	\end{align}
32	where $\delta_s = \pi_s - \bar{\pi}$ is the subgroup deviation from the pooled error rate and $\Delta\tau = \tau(1) - \tau(0)$ is the CATE heterogeneity.
33	\end{proposition}
34	
35	Equations~\eqref{eq:bias_z0}--\eqref{eq:bias_z1} constitute an exact identity at the population level, not a bound.
36	The bias factors into three interpretable components: $\delta_s$ captures how much subgroup $s$ deviates from the average misclassification rate, $\Delta\tau$ captures treatment effect heterogeneity across levels of $Z$, and $1/(1 - 2\bar{\pi})$ is an amplification factor from matrix inversion.
37	Bias vanishes when either source of variation is absent ($\delta_s = 0$ or $\Delta\tau = 0$), and arises only through their interaction.
38	Proposition~\ref{prop:bias_identity} implies that global correction trades one source of confounding for another: it removes attenuation from label noise but introduces a new bias from error-rate heterogeneity.
39	
40	\paragraph{Proof sketch.}
41	Global correction applies $M_{\text{global}}^{-1}$ to the subgroup-specific observed CATE $\tau_{\text{obs}}(\cdot, s) = M_s \cdot \tau_{\text{true}}$, yielding bias $(M_{\text{global}}^{-1} M_s - I) \cdot \tau_{\text{true}}$.
42	Direct computation shows $M_{\text{global}}^{-1} M_s - I = \frac{\delta_s}{1-2\bar{\pi}} \bigl[\begin{smallmatrix} -1 & 1 \\ 1 & -1 \end{smallmatrix}\bigr]$.
43	Applying this matrix to $[\tau(0),\, \tau(1)]^\top$ produces the product form.
44	The full derivation appears in Appendix~\ref{app:derivation}.
45	
46	\begin{corollary}[Multi-class Extension]
47	\label{cor:multiclass}
48	For $K > 2$ subgroups with $J$ effect-modifier levels, the subgroup bias of global correction generalizes to
49	\begin{equation}
50	\mathrm{bias}_{\mathrm{global}}(z, s) = \sum_{j=1}^{J} \bigl(\bar{\pi}_j - \pi_{s,j}\bigr) \cdot \bigl(\tau(j) - \bar{\tau}\bigr) \cdot g(\bar{\pi}),
51	\label{eq:multiclass}
52	\end{equation}
53	where $g(\bar{\pi})$ collects the matrix-inversion amplification terms.
54	The essential structure, $\sum_s w_s (\bar{\pi}_j - \pi_{s,j}) = 0$, ensures that bias redistributes across subgroups rather than vanishing in aggregate.
55	\end{corollary}
56	
57	Assumption~(A3) ensures $M_s = C_s$; when $P(Z{=}1) \neq 0.5$, the mixing matrices acquire asymmetric entries, but the product structure persists with modified coefficients (Appendix~\ref{app:derivation}).
58	Empirical verification (Section~\ref{sec:bias_mechanism}) yields $R^2 = 0.994$ for $K{=}2$ and $R^2 = 0.974$ for $K{=}4$; the residual variance reflects finite-sample Monte Carlo noise, not model misspecification.
59	
60	\paragraph{Finite-sample remainder.}
61	Proposition~\ref{prop:bias_identity} is an exact population identity.
62	In practice, confusion matrices are estimated from $n_{\text{expert}}$ expert labels, introducing an estimation error $\hat{C}_s = C_s + E_s$ where $\|E_s\| = O_p(n_{\text{expert}}^{-1/2})$.
63	The resulting remainder term in the corrected CATE is $R_n = O_p(n_{\text{expert}}^{-1/2} \cdot \kappa(C_s))$, where $\kappa(C_s)$ is the condition number of the subgroup confusion matrix.
64	This dependence on both sample size and matrix conditioning motivates the singularity guard ($\kappa > 100 \to$ fallback) described in Section~\ref{sec:method}.
65	
66	\begin{proposition}[Debiasing Can Increase Bias]
67	\label{prop:debiasing_hurts}
68	Under \textnormal{(A1)--(A4)}, global correction produces larger absolute bias than the naive estimator ($|\mathrm{bias}_{\mathrm{global}}| > |\mathrm{bias}_{\mathrm{naive}}|$) in subgroup $s$ if and only if
69	\begin{equation}
70	\frac{|\delta_s|}{(1 - 2\bar{\pi}) \cdot \pi_s} > 1.
71	\label{eq:hurts_condition}
72	\end{equation}
73	\end{proposition}
74	
75	Equation~\eqref{eq:hurts_condition} partitions subgroups into two regimes.
76	For high-error subgroups ($\pi_s > \bar{\pi}$), the condition reduces to $\pi_s > 0.5$, which is excluded by~(A4); global correction always reduces bias in these subgroups.
77	For low-error subgroups ($\pi_s < \bar{\pi}$), the condition holds whenever $\pi_s < \bar{\pi} / (2(1 - \bar{\pi}))$.
78	This threshold is easily satisfied in practice: when $\bar{\pi} = 0.15$, any subgroup with $\pi_s < 0.088$ experiences increased bias from global correction.
79	The mechanism is that global correction inverts the pooled confusion matrix, applying a correction calibrated for the average error rate; high-error subgroups are under-corrected (bias reduced but not eliminated), while low-error subgroups are over-corrected (the correction overshoots and reverses the sign of bias).
80	For subgroups with near-zero misclassification ($\pi_s \approx 0$), the naive estimator is nearly unbiased, yet global correction creates substantial bias where none existed.
81	This is the most consequential implication of Proposition~\ref{prop:bias_identity}: debiasing can be worse than doing nothing.
82	
83	In our experiments (Section~\ref{sec:bias_mechanism}), global correction increases bias in 50\% of parameter configurations (260 of 520, excluding cases where $\Delta_c{=}0$).
84	Maximum amplification reaches $2.86\times$ for $K{=}2$ and $5.9\times$ for $K{=}4$ with a CausalForest estimator; the phenomenon intensifies with more subgroups as the range of $\delta_s$ values widens.
85	Figure~\ref{fig:heatmap} visualizes the amplification across the full $\Delta\pi \times \Delta\tau$ parameter grid.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ca08ab7-71d6-48ea-883e-91a76bcc52c4",
  "isSidechain": true,
  "promptId": "bea3db89-b6ab-4557-9575-e64604389d66",
  "agentId": "abc0a35aad20707c6",
  "type": "user",
  "uuid": "18c5c32c-8e87-4b14-9f81-bcabd01b84d6",
  "sourceToolAssistantUUID": "4ca08ab7-71d6-48ea-883e-91a76bcc52c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "069df309-e1d5-4181-acb0-1338e109ee71",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T05:01:58.830Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QpJAR9yhKP59kbGz3MoBZk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18c5c32c-8e87-4b14-9f81-bcabd01b84d6",
  "isSidechain": true,
  "agentId": "abc0a35aad20707c6",
  "requestId": "req_011CbF8KpGifWNTg6t5dVx5J",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "edbf324b-294c-4c53-b547-1f9121f1d813",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "069df309-e1d5-4181-acb0-1338e109ee71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NXnapAASi15E6viYKMrGyj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 983,
      "cache_read_input_tokens": 27785,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 983
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 191,
          "cache_read_input_tokens": 27785,
          "cache_creation_input_tokens": 983,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 983,
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

_source line 9 · 2026-05-21T05:01:58.855Z_

<details><summary>↩ Tool result · `toolu_01QpJAR9yhKP59kbGz3MoBZk`</summary>

```text
1	\section{Experiments}
2	
3	\subsection{Experimental Setup and Data Generation}
4	
5	\subsubsection{Synthetic DGP}
6	
7	We generate data from a controlled data-generating process (DGP) that separates the effect of subgroup-level misclassification heterogeneity from other confounders.
8	For each observation $i$, the potential outcome under treatment $t$ is
9	\begin{equation}
10	Y_i(t) = \alpha + \tau(Z_i) \cdot t + \beta X_i + \varepsilon_i, \quad \varepsilon_i \sim \mathcal{N}(0,1),
11	\end{equation}
12	where $T_i \sim \text{Bernoulli}(0.5)$ simulates a randomized controlled trial, and $Z_i \in \{0, \ldots, K{-}1\}$ is the true effect modifier with $K \in \{2, 4\}$ subgroups.
13	The conditional average treatment effect (CATE) $\tau(Z{=}z)$ varies across subgroups with controlled heterogeneity $\Delta\tau = \max_z \tau(z) - \min_z \tau(z)$.
14	Misclassification is injected through subgroup-specific symmetric confusion matrices $C_s$: the observed label $\hat{Z}_i$ is drawn as $\hat{Z}_i \sim \text{Multinomial}(C_{S_i})$, where each subgroup $s$ has error rate $\pi_s$ and $\Delta\pi = \max_s \pi_s - \min_s \pi_s$ controls heterogeneity.
15	We fix $N{=}5000$ observations and vary $n_{\text{expert}} \in \{50, 100, 250, 500, 1000, 2000\}$ (the number of expert-labeled observations used to estimate confusion matrices).
16	Each configuration is repeated for 100 Monte Carlo runs.
17	
18	\subsubsection{Semi-synthetic DGP (TweetEval)}
19	
20	To test EC-HTE under realistic conditions, we construct a semi-synthetic DGP from the TweetEval sentiment corpus~\cite{barbieri2020tweeteval}, sampling $N{=}5000$ tweets per run from a pool of 57{,}899.
21	Four subgroups are defined by crossing two binary text features: presence of hashtags (\texttt{has\_hashtag}) and text length relative to the median (\texttt{text\_length\_bin}).
22	This yields unbalanced subgroup proportions (S0: 39\%, S1: 38\%, S2: 12\%, S3: 11\%).
23	The effect modifier is $Z{=}1$ if the true sentiment is positive ($P(Z{=}1) \approx 35\%$), and $Z{=}0$ otherwise.
24	We set subgroup-specific misclassification rates $\pi_{S0}{=}0.05$, $\pi_{S1}{=}0.10$, $\pi_{S2}{=}0.15$, $\pi_{S3}{=}0.25$ in the extreme regime, reflecting empirical evidence that hashtag-heavy text degrades LLM classifier accuracy~\cite{ashwin2025bias}.
25	The outcome model is
26	\begin{equation}
27	Y_i = 1.0 + \tau(Z_i, S_i) \cdot T_i + 0.3 \cdot \text{len}_i + 0.2 \cdot \text{mention}_i + \varepsilon_i,
28	\end{equation}
29	where $\tau(Z{=}1, S) \in \{0.5, 0.4, 0.3, 0.2\}$ for S0--S3 and $\tau(Z{=}0) = 0.1$ is the baseline effect.
30	
31	\paragraph{Baselines and metrics.}
32	We compare: (1) \textit{Naive} (no correction), (2) \textit{Global} (pooled confusion matrix), (3) \textit{Stratified MLE} (per-subgroup MLE without pooling), (4) \textit{HB EC-HTE} (our hierarchical Bayes estimator), (5) \textit{PPCI}~\cite{sui2026ppci}, and (6) \textit{EC-HTE+PPCI} (our combined method).
33	For the CausalForest estimator~\cite{wager2018causal}, we also compare naive, global, and EC-HTE variants.
34	Primary metrics are absolute bias $|\text{bias}|$, root mean squared error (RMSE), and 95\% confidence interval coverage, all averaged across subgroups and 100 MC runs.
35	
36	\subsection{Bias Mechanism Verification}
37	\label{sec:bias_mechanism}
38	
39	The bias decomposition identity (Theorem~1) predicts that global correction introduces bias proportional to $\Delta\pi \times \Delta\tau$ at the subgroup level.
40	We verify this identity empirically across 520 configurations spanning $K \in \{2,4\}$, two misclassification regimes, and six expert budget levels.
41	Regressing observed subgroup bias on the predicted $\Delta\pi \times \Delta\tau$ product yields $R^2 = 0.994$ for $K{=}2$ and $R^2 = 0.974$ for $K{=}4$; the residual variance reflects MC sampling noise rather than model misspecification, since Theorem~1 is an exact identity at the population level.
42	In 50\% of configurations (260/520, excluding $\Delta_c{=}0$ rows where bias is zero by construction), global correction produces larger absolute bias than the naive estimator.
43	The damage concentrates in low-$\pi$ subgroups: among subgroups where $\pi_s < \bar{\pi}$, global correction increases bias in 84.6\% of cases.
44	Maximum observed amplification reaches 2.86$\times$ (K=2) and 2.41$\times$ (K=4) relative to the naive estimator.
45	Figure~\ref{fig:heatmap} visualizes the $\Delta\pi \times \Delta\tau$ amplification surface across the parameter grid.
46	
47	\subsection{EC-HTE Evaluation}
48	\label{sec:ec_hte_eval}
49	
50	Table~\ref{tab:main_results} presents the main results across representative configurations.
51	In the synthetic DGP with $K{=}2$ subgroups and extreme misclassification heterogeneity, HB EC-HTE reduces $|\text{bias}|$ from 0.059 (global) to 0.011 (a 5.4$\times$ reduction) while maintaining nominal coverage (0.95) and comparable RMSE (0.093 vs.\ 0.099).
52	The advantage persists at $K{=}4$: EC-HTE achieves $|\text{bias}|{=}0.009$ versus 0.056 for global (6.2$\times$ reduction), though with a small RMSE penalty (0.127 vs.\ 0.125).
53	Under moderate heterogeneity ($K{=}2$), global correction already achieves low bias (0.009), and EC-HTE provides negligible improvement (0.005) at the cost of slightly higher RMSE (0.075 vs.\ 0.074).
54	This illustrates the conditional nature of EC-HTE's advantage: when $\Delta\pi$ is small, the variance cost of stratification is not offset by bias reduction.
55	
56	In the semi-synthetic TweetEval experiment, the pattern shifts.
57	Global correction achieves the lowest $|\text{bias}|$ (0.023) among non-oracle methods, while HB EC-HTE attains 0.027 with substantially higher RMSE (0.225 vs.\ 0.124).
58	This is consistent with moderate $\Delta\pi{=}0.20$ and the high-error subgroups (S2, S3) comprising only 23\% of data: the bias reduction from stratification is marginal while the variance cost of four per-subgroup confusion matrices is substantial.
59	HB EC-HTE does improve over stratified MLE (RMSE 0.225 vs.\ 0.248), confirming that partial pooling helps, but the improvement is insufficient to overcome the structural variance from unbalanced subgroup sizes.
60	At $n_{\text{expert}} \geq 250$, HB and MLE converge to within 5\% on all metrics.
61	
62	\paragraph{CausalForest K-dependence.}
63	When the downstream estimator is a CausalForest~\cite{wager2018causal} rather than difference-in-means, the bias mechanism operates with amplified magnitude.
64	At $K{=}4$/extreme/$n{=}500$, EC-HTE Forest reduces $|\text{bias}|$ from 0.191 (global) to 0.040, a 4.8$\times$ improvement with lower RMSE (0.224 vs.\ 0.244) and dramatically better coverage (0.91 vs.\ 0.58).
65	The debiasing-hurts phenomenon intensifies: global correction amplifies naive bias by up to 5.9$\times$ in the worst subgroup (compared to 2.41$\times$ for difference-in-means), because the forest's sensitivity to covariate noise magnifies the effect of label errors.
66	At $K{=}2$/$n{=}500$, EC-HTE Forest achieves near-zero bias (0.004--0.013 across subgroups) versus 0.033--0.109 for global, with coverage of 0.91 compared to 0.58 for the global variant.
67	At $K{=}4$, the per-subgroup range widens to 0.002--0.068 while coverage remains above 0.80.
68	However, this comes at a variance cost: at $K{=}4$/$n{=}100$, EC-HTE Forest RMSE reaches 1.43 (3.5$\times$ naive), underscoring the budget guidelines in Section~\ref{sec:budget}.
69	
70	\begin{table*}[t]
71	\centering
72	\caption{Main results across synthetic (difference-in-means and CausalForest) and semi-synthetic configurations. $|\text{Bias}|$ and RMSE are averaged over subgroups, $z$-levels, and 100 MC runs. Bold marks lowest $|\text{bias}|$ per block. $^\dagger$RMSE exceeds Global in this configuration, reflecting the variance cost of stratification.}
73	\label{tab:main_results}
74	\small
75	\begin{tabular}{ll ccc}
76	\toprule
77	Configuration & Method & $|\text{Bias}| \downarrow$ & RMSE $\downarrow$ & Coverage \\
78	\midrule
79	\multirow{4}{*}{\shortstack[l]{Synthetic DIM\\$K{=}2$, extreme, $n{=}250$}}
80	 & Naive & 0.058 & 0.090 & 0.82 \\
81	 & Global & 0.059 & 0.099 & 0.87 \\
82	 & Strat.\ MLE & 0.012 & 0.094 & 0.95 \\
83	 & HB EC-HTE & \textbf{0.011} & 0.093 & 0.95 \\
84	\midrule
85	\multirow{4}{*}{\shortstack[l]{Synthetic DIM\\$K{=}2$, moderate, $n{=}250$}}
86	 & Naive & 0.018 & 0.064 & 0.95 \\
87	 & Global & 0.009 & 0.074 & 0.96 \\
88	 & Strat.\ MLE & \textbf{0.005} & 0.075$^\dagger$ & 0.97 \\
89	 & HB EC-HTE & \textbf{0.005} & 0.075$^\dagger$ & 0.97 \\
90	\midrule
91	\multirow{4}{*}{\shortstack[l]{Synthetic DIM\\$K{=}4$, extreme, $n{=}500$}}
92	 & Naive & 0.062 & 0.113 & 0.88 \\
93	 & Global & 0.056 & 0.125 & 0.91 \\
94	 & Strat.\ MLE & 0.010 & 0.127$^\dagger$ & 0.95 \\
95	 & HB EC-HTE & \textbf{0.009} & 0.127$^\dagger$ & 0.95 \\
96	\midrule
97	\multirow{3}{*}{\shortstack[l]{Synthetic CausalForest\\$K{=}4$, extreme, $n{=}500$}}
98	 & Naive & 0.208 & 0.231 & 0.44 \\
99	 & Global & 0.191 & 0.244 & 0.58 \\
100	 & EC-HTE Forest & \textbf{0.040} & 0.224 & 0.91 \\
101	\midrule
102	\multirow{4}{*}{\shortstack[l]{Semi-synthetic\\TweetEval, extreme, $n{=}250$}}
103	 & Naive & 0.027 & 0.103 & 0.93 \\
104	 & Global & \textbf{0.023} & 0.124 & 0.92 \\
105	 & Strat.\ MLE & 0.032 & 0.248$^\dagger$ & 0.91 \\
106	 & HB EC-HTE & 0.027 & 0.225$^\dagger$ & 0.91 \\
107	\bottomrule
108	\end{tabular}
109	\end{table*}
110	
111	\subsection{Diagnostic Criterion}
112	\label{sec:diagnostic}
113	
114	As a practical corollary of Theorem~1, the $\Delta\pi \times \Delta\tau$ product provides a computable diagnostic for predicting when global correction will fail.
115	Using leave-one-out cross-validation at the subgroup level, a threshold classifier on $|\Delta\pi \times \Delta\tau|$ achieves AUC = 0.833 for predicting whether global correction increases bias relative to the naive estimator.
116	The Pearson correlation between the signed product and the observed bias ratio is $r = 0.86$.
117	At the setting level (averaging across subgroups within a configuration), the diagnostic has AUC = 0.49, which is no better than random.
118	This asymmetry arises because global correction redistributes bias across subgroups (benefiting high-$\pi$ subgroups at the expense of low-$\pi$ ones) rather than increasing total bias uniformly.
119	In practice, the diagnostic enables researchers to identify vulnerable subgroups before committing to a correction strategy: if any subgroup has $\pi_s \ll \bar{\pi}$ and $\tau(z)$ varies across $z$-levels, global correction should be avoided.
120	Figure~\ref{fig:roc} shows the ROC curve and the correlation scatter plot.
121	
122	\subsection{Expert Budget Analysis}
123	\label{sec:budget}
124	
125	The crossover point at which EC-HTE achieves lower RMSE than global correction depends on $K$ and $\Delta\pi$.
126	For $K{=}2$/extreme, the crossover occurs at $n_{\text{expert}} = 250$: below this threshold, the variance cost of estimating per-subgroup confusion matrices exceeds the bias reduction.
127	For $K{=}4$/extreme, the crossover shifts to $n_{\text{expert}} = 1000$ because four subgroups require more expert labels to achieve precise confusion matrix estimates.
128	Under moderate heterogeneity ($K{=}2$), EC-HTE never achieves lower RMSE than global at any budget, because global correction already produces low bias ($|\text{bias}|{<}0.01$) in this regime.
129	Within the EC-HTE family, HB partial pooling improves over stratified MLE in 21 of 24 budget-regime configurations overall, with the largest gains at small $n_{\text{expert}}$ in $K{=}4$ settings (+42.4\% RMSE improvement for the hardest subgroup).
130	The two estimators converge by $n_{\text{expert}} \geq 1000$ ($<$0.5\% difference).
131	Figure~\ref{fig:budget} shows the crossover curves across the full budget range.
132	
133	\subsection{PPCI Complementarity}
134	\label{sec:ppci}
135	
136	EC-HTE corrects structured covariate misclassification by inverting estimated confusion matrices, but cannot address treatment-differential outcome measurement error.
137	Prediction-Powered Conditional Inference~\cite{sui2026ppci} (PPCI) correct outcome-level prediction error using a small gold-standard sample but assume correct covariate labels.
138	We test their combination across four DGP variants: (A) covariate error only ($\sigma_{\text{outcome}}{=}0$), (B) outcome error only ($\sigma_{\text{outcome}}{=}0.5$), (C) both errors ($\sigma_{\text{outcome}}{=}0.5$), and (D) no error ($\sigma_{\text{outcome}}{=}0$).
139	Table~\ref{tab:ppci} reports results for $K{=}2$, $n_{\text{expert}}{=}250$, extreme misclassification.
140	
141	Under DGP~C (both errors), EC-HTE+PPCI reduces $|\text{bias}|$ to 0.007/0.008 (z=0/z=1), compared to 0.179/0.216 for EC-HTE alone, representing a 25--27$\times$ improvement.
142	PPCI alone achieves comparable bias (0.017/0.007) but at higher RMSE (0.241 vs.\ 0.209 for z=0).
143	Under DGP~A (covariate error only), EC-HTE+PPCI produces identical results to EC-HTE, confirming that PPCI adds no correction when outcome labels are unbiased.
144	Under DGP~D (no error), all methods perform similarly, with naive and PPCI equivalent as expected.
145	The two corrections are complementary rather than redundant: EC-HTE handles the structured $M^{-1}$ inversion for covariate error, while PPCI handles residual outcome-level bias through its debiasing estimator~\cite{sui2026ppci}.
146	
147	\begin{table*}[t]
148	\centering
149	\caption{PPCI complementarity experiment ($K{=}2$, extreme, $n_{\text{expert}}{=}250$). DGP~A: covariate error only; B: outcome error only ($\sigma{=}0.5$); C: both errors; D: no error. Values are $|\text{bias}|$ and RMSE averaged over two subgroups. $^\star$EC-HTE+PPCI achieves near-zero bias when both error types are present.}
150	\label{tab:ppci}
151	\small
152	\begin{tabular}{ll cccc}
153	\toprule
154	DGP & Method & $|\text{Bias}|_{z=0}$ & $|\text{Bias}|_{z=1}$ & RMSE$_{z=0}$ & RMSE$_{z=1}$ \\
155	\midrule
156	\multirow{5}{*}{A: Covariate}
157	 & Naive & 0.053 & 0.063 & 0.087 & 0.093 \\
158	 & Global & 0.063 & 0.055 & 0.101 & 0.102 \\
159	 & EC-HTE & 0.017 & \textbf{0.013} & 0.097 & 0.108 \\
160	 & PPCI & \textbf{0.015} & 0.020 & 0.162 & 0.168 \\
161	 & EC-HTE+PPCI & 0.017 & \textbf{0.013} & 0.097 & 0.108 \\
162	\midrule
163	\multirow{5}{*}{B: Outcome}
164	 & Naive & 0.189 & 0.197 & 0.206 & 0.212 \\
165	 & Global & 0.185 & 0.208 & 0.204 & 0.228 \\
166	 & EC-HTE & 0.181 & 0.215 & 0.202 & 0.237 \\
167	 & PPCI & 0.015 & \textbf{0.020} & 0.171 & 0.176 \\
168	 & EC-HTE+PPCI & \textbf{0.012} & 0.023 & 0.171 & 0.186 \\
169	\midrule
170	\multirow{5}{*}{C: Both}
171	 & Naive & 0.251 & 0.135 & 0.267 & 0.155 \\
172	 & Global & 0.182 & 0.209 & 0.233 & 0.235 \\
173	 & EC-HTE & 0.179 & 0.216 & 0.224 & 0.262 \\
174	 & PPCI & 0.017 & 0.007 & 0.241 & 0.232 \\
175	 & EC-HTE+PPCI$^\star$ & \textbf{0.007} & \textbf{0.008} & 0.209 & 0.223 \\
176	\midrule
177	\multirow{5}{*}{D: None}
178	 & Naive & \textbf{0.007} & 0.003 & 0.060 & 0.065 \\
179	 & Global & 0.010 & \textbf{0.002} & 0.061 & 0.071 \\
180	 & EC-HTE & 0.013 & 0.007 & 0.062 & 0.079 \\
181	 & PPCI & \textbf{0.007} & \textbf{0.003} & 0.060 & 0.065 \\
182	 & EC-HTE+PPCI & 0.013 & 0.007 & 0.062 & 0.079 \\
183	\bottomrule
184	\end{tabular}
185	\end{table*}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "edbf324b-294c-4c53-b547-1f9121f1d813",
  "isSidechain": true,
  "promptId": "bea3db89-b6ab-4557-9575-e64604389d66",
  "agentId": "abc0a35aad20707c6",
  "type": "user",
  "uuid": "d53a837d-db04-438f-b2c4-98dd8e10d231",
  "sourceToolAssistantUUID": "edbf324b-294c-4c53-b547-1f9121f1d813",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "069df309-e1d5-4181-acb0-1338e109ee71",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-21T05:02:22.974Z_

Perfect! I have extracted all the requested information from the theory.tex and experiments.tex files. Let me compile a comprehensive structured report.

## .tex Files Found

The paper directory contains:
- `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex`

---

## STRUCTURED EXTRACTION REPORT

### 1. NOTATION DEFINITIONS

| Symbol | Definition | First Appearance | Context |
|--------|------------|------------------|---------|
| τ(z) | Conditional average treatment effect (CATE) | Line 8 | Core effect measure |
| Z | Binary effect modifier (Z ∈ {0,1}) | Line 8 | True label |
| Ẑ | Noisy annotation of Z | Line 8 | Observed/corrupted label |
| S | Subgroup indicator (S ∈ {1,...,K}) | Line 9 | Population subgroups |
| w_s | Weight of subgroup s: P(S=s) | Line 9 | Subgroup proportions |
| C_s | 2×2 confusion matrix for subgroup s | Line 9 | Misclassification structure |
| π_s | Symmetric error rate P(Ẑ ≠ Z \| S=s) | Line 9 | Per-subgroup error rate |
| C̄ | Pooled confusion matrix: Σ_s w_s C_s | Line 10 | Global aggregated matrix |
| π̄ | Pooled error rate: Σ_s w_s π_s | Line 10 | Average error rate |
| δ_s | Subgroup deviation: π_s - π̄ | Line 32 | Relative error heterogeneity |
| Δτ | CATE heterogeneity: τ(1) - τ(0) | Line 32 | Treatment effect variation |
| M_s | Bayesian mixing matrix for subgroup s | Line 22 | Posterior probability structure |
| M_global | Global mixing matrix: Σ_s w_s M_s | Line 23 | Pooled posterior structure |
| n_expert | Number of expert-labeled observations | Line 15 | Sample size for confusion matrix estimation |
| Δπ | Misclassification heterogeneity: max_s π_s - min_s π_s | Line 14 | Range of error rates |
| K | Number of subgroups | Line 12 | Population partition size |
| Y_i(t) | Potential outcome under treatment t | Line 10 (Exp.) | Counterfactual outcome |
| T_i | Treatment indicator (Bernoulli(0.5)) | Line 12 (Exp.) | Binary treatment |
| X_i | Covariates | Line 10 (Exp.) | Feature variables |
| ε_i | Noise term (N(0,1)) | Line 10 (Exp.) | Error distribution |
| κ(C_s) | Condition number of confusion matrix C_s | Line 63 (Theory) | Matrix conditioning |
| bias_global(z,s) | Bias of global correction in subgroup s at level z | Line 27 | Primary quantity of interest |
| bias_naive | Bias of naive (uncorrected) estimator | Line 68 | Baseline comparator |

---

### 2. \label{} DEFINITIONS

**Theory Section:**
- `\label{sec:theory}` (Line 5) - Main theory section
- `\label{prop:bias_identity}` (Line 26) - Proposition on bias decomposition
- `\label{eq:bias_z0}` (Line 29) - Equation: bias at Z=0
- `\label{eq:bias_z1}` (Line 30) - Equation: bias at Z=1
- `\label{fig:heatmap}` (Line 85) - Figure reference (cited, not defined in theory.tex)
- `\label{cor:multiclass}` (Line 47) - Corollary: multi-class extension
- `\label{eq:multiclass}` (Line 51) - Equation: multi-class bias formula
- `\label{app:derivation}` (Lines 44, 57) - Appendix reference (cited)
- `\label{sec:bias_mechanism}` (Line 37) - Bias mechanism verification section
- `\label{sec:method}` (Line 64) - Method section reference (cited)
- `\label{prop:debiasing_hurts}` (Line 67) - Proposition: when debiasing increases bias
- `\label{eq:hurts_condition}` (Line 71) - Equation: condition for debiasing harm

**Experiments Section:**
- `\label{sec:bias_mechanism}` (Line 37) - Bias mechanism verification subsection
- `\label{sec:ec_hte_eval}` (Line 48) - EC-HTE evaluation subsection
- `\label{tab:main_results}` (Line 73) - Table: main results
- `\label{sec:budget}` (Line 123) - Expert budget analysis subsection
- `\label{sec:diagnostic}` (Line 112) - Diagnostic criterion subsection
- `\label{sec:ppci}` (Line 134) - PPCI complementarity subsection
- `\label{tab:ppci}` (Line 150) - Table: PPCI complementarity results
- `\label{fig:budget}` (Line 131) - Figure reference (cited)
- `\label{fig:roc}` (Line 120) - Figure reference (cited)

---

### 3. PROPOSITIONS AND COROLLARIES WITH LABELS

| Entity | Label | Location | Title |
|--------|-------|----------|-------|
| Proposition | `prop:bias_identity` | Lines 25-33 | Bias Decomposition Identity |
| Corollary | `cor:multiclass` | Lines 46-55 | Multi-class Extension |
| Proposition | `prop:debiasing_hurts` | Lines 66-73 | Debiasing Can Increase Bias |

---

### 4. METHOD NAME CONVENTIONS

Methods referenced in the paper:

| Method Name | Abbreviation | Description | First Mention |
|------------|--------------|-------------|-----------------|
| Naive | - | No correction applied | Line 32 (Exp.) |
| Global | - | Pooled confusion matrix correction | Line 32 (Exp.) |
| Stratified MLE | Strat. MLE | Per-subgroup MLE without pooling | Line 32 (Exp.) |
| Hierarchical Bayes EC-HTE | HB EC-HTE | Hierarchical Bayes estimator (main method) | Line 32 (Exp.) |
| PPCI | PPCI | Prediction-Powered Conditional Inference | Line 32 (Exp.) |
| EC-HTE+PPCI | EC-HTE+PPCI | Combined method: EC-HTE and PPCI | Line 32 (Exp.) |
| CausalForest | - | Causal forest estimator (downstream) | Line 33 (Exp.) |
| EC-HTE Forest | - | EC-HTE with CausalForest | Line 33 (Exp.) |
| Difference-in-Means | DIM | Standard difference-in-means estimator | Line 79 (Exp.) |

**Method presentation in tables:**
- Table 1 (Line 73): "Synthetic DIM K=2, extreme, n=250" → Methods: Naive, Global, Strat. MLE, HB EC-HTE
- Uses consistent abbreviation: "Strat. MLE" in tables (Line 82, 88, 94, 105)
- "HB EC-HTE" for hierarchical Bayes variant
- "EC-HTE Forest" for CausalForest version

---

### 5. ASSUMPTIONS (A1)-(A4)

All four assumptions are formally stated in Theory section (Lines 15-20):

| Assumption | Code | Label Type | Full Statement |
|-----------|------|-----------|-----------------|
| Conditional Independence | **(A1)** | Bullet point | "Misclassification depends only on the true label Z and subgroup S, not on potential outcomes Y(0), Y(1)." |
| Symmetric Misclassification | **(A2)** | Bullet point | "P(Ẑ=1 \| Z=0, S=s) = P(Ẑ=0 \| Z=1, S=s) = π_s for all s." |
| Balanced Effect Modifier | **(A3)** | Bullet point | "P(Z=0) = P(Z=1) = 0.5. This simplifies exposition; relaxation discussed below." |
| Non-degeneracy | **(A4)** | Bullet point | "π_s ≠ 0.5 for all s, ensuring each C_s is invertible." |

**Key implications:**
- (A2)-(A3) together ensure mixing matrix M_s equals confusion matrix C_s (Line 22)
- (A1)-(A4) are the full set of conditions for Propositions 1, 2 (Lines 27, 68)
- (A3) allows simplification; discussed as relaxable (Line 57, Appendix A)
- (A4) prevents singular matrices; motivates condition number guard κ > 100 (Line 64)

---

### ADDITIONAL KEY REFERENCES

**Equations cited for notation:**
- `eq:bias_z0` / `eq:bias_z1` (Lines 29-30): Main bias decomposition formulas
- `eq:hurts_condition` (Line 71): Threshold criterion for when debiasing increases bias
- `eq:multiclass` (Line 51): Generalization to K>2 subgroups, J effect-modifier levels

**Experimental configurations:**
- Synthetic DGP: K ∈ {2, 4}, n_expert ∈ {50, 100, 250, 500, 1000, 2000}
- Semi-synthetic TweetEval: N=5000, 4 subgroups (S0-S3)
- Primary metrics: |Bias|, RMSE, 95% CI coverage

---

This extraction provides a complete reference for all notation, labels, propositions, method conventions, and assumptions used throughout the theory and experimental sections of the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d53a837d-db04-438f-b2c4-98dd8e10d231",
  "isSidechain": true,
  "agentId": "abc0a35aad20707c6",
  "requestId": "req_011CbF8KydHh2FR4wFZxGpfq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "df891c36-f934-4a19-a6b7-35212023edc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "069df309-e1d5-4181-acb0-1338e109ee71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SwmKvFEbqbiE51QGsbatUC",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 9068,
      "cache_read_input_tokens": 28768,
      "output_tokens": 2622,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9068
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 2622,
          "cache_read_input_tokens": 28768,
          "cache_creation_input_tokens": 9068,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9068,
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
