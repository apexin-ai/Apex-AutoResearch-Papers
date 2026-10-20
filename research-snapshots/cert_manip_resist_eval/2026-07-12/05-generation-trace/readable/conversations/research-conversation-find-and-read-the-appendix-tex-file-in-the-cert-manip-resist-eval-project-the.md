# Research conversation: Find and read the appendix.tex file in the cert_manip_resist_eval project. The project is located at /home/ubuntu/.agent

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 10
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a2bfd38fb2f2154cb.jsonl`
- **Structured JSON:** [`594239d0be59b4f350c8.json`](../../sessions/59/594239d0be59b4f350c8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

10 recorded events

### User

_source line 1 · 2026-05-24T10:36:17.269Z_

Find and read the appendix.tex file in the cert_manip_resist_eval project. The project is located at /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/. Look in artifacts/ or any paper-related subdirectory. Show me the full content of the file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "4f56398c-daec-492b-b598-2d686c53cd24",
  "agentId": "a2bfd38fb2f2154cb",
  "type": "user",
  "uuid": "c22503ce-99f1-4000-af98-d4223939d5aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/director_a20165af",
  "sessionId": "c9dbaca8-1cd1-415f-aa7b-2e5963ce8650",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-24T10:36:19.487Z_

I'll help you find and read the appendix.tex file in the cert_manip_resist_eval project. Let me search for it first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c22503ce-99f1-4000-af98-d4223939d5aa",
  "isSidechain": true,
  "agentId": "a2bfd38fb2f2154cb",
  "requestId": "req_011CbMFFJw6B2EAxusUHKovg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "919f552f-7213-430a-af53-e22e449d31ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/director_a20165af",
  "sessionId": "c9dbaca8-1cd1-415f-aa7b-2e5963ce8650",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014UmVF66yauN7cYDAXVS5fg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39607,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39607,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 3 · 2026-05-24T10:36:20.018Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01HjzGR4qutJhT2d4aUWGBTD`</summary>

```json
{
  "pattern": "**/appendix.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "919f552f-7213-430a-af53-e22e449d31ab",
  "isSidechain": true,
  "agentId": "a2bfd38fb2f2154cb",
  "requestId": "req_011CbMFFJw6B2EAxusUHKovg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e2e26ba5-7fd9-47ad-b7f0-d90c1ed7fc09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/director_a20165af",
  "sessionId": "c9dbaca8-1cd1-415f-aa7b-2e5963ce8650",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014UmVF66yauN7cYDAXVS5fg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39607,
      "cache_read_input_tokens": 0,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 39607
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 39607,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 39607,
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

_source line 4 · 2026-05-24T10:36:20.071Z_

<details><summary>↩ Tool result · `toolu_01HjzGR4qutJhT2d4aUWGBTD`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e2e26ba5-7fd9-47ad-b7f0-d90c1ed7fc09",
  "isSidechain": true,
  "promptId": "4f56398c-daec-492b-b598-2d686c53cd24",
  "agentId": "a2bfd38fb2f2154cb",
  "type": "user",
  "uuid": "6e0ccc09-6120-477d-8b25-c99d8551b4fa",
  "sourceToolAssistantUUID": "e2e26ba5-7fd9-47ad-b7f0-d90c1ed7fc09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/director_a20165af",
  "sessionId": "c9dbaca8-1cd1-415f-aa7b-2e5963ce8650",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-24T10:36:20.081Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DUx57ykyL1puERkT6U6jQN`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval -name \"appendix.tex\" -type f 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e0ccc09-6120-477d-8b25-c99d8551b4fa",
  "isSidechain": true,
  "agentId": "a2bfd38fb2f2154cb",
  "requestId": "req_011CbMFFJw6B2EAxusUHKovg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "29abf326-99b2-4612-b2c2-3fcef9a257c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/director_a20165af",
  "sessionId": "c9dbaca8-1cd1-415f-aa7b-2e5963ce8650",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014UmVF66yauN7cYDAXVS5fg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39607,
      "cache_read_input_tokens": 0,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 39607
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 39607,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 39607,
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

_source line 6 · 2026-05-24T10:36:20.282Z_

<details><summary>↩ Tool result · `toolu_01DUx57ykyL1puERkT6U6jQN`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29abf326-99b2-4612-b2c2-3fcef9a257c2",
  "isSidechain": true,
  "promptId": "4f56398c-daec-492b-b598-2d686c53cd24",
  "agentId": "a2bfd38fb2f2154cb",
  "type": "user",
  "uuid": "44f004d1-d63b-4627-8df7-0a9c56d39b3c",
  "sourceToolAssistantUUID": "29abf326-99b2-4612-b2c2-3fcef9a257c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/director_a20165af",
  "sessionId": "c9dbaca8-1cd1-415f-aa7b-2e5963ce8650",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-24T10:36:22.588Z_

Perfect! I found the file at `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex`. Let me read it now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44f004d1-d63b-4627-8df7-0a9c56d39b3c",
  "isSidechain": true,
  "agentId": "a2bfd38fb2f2154cb",
  "requestId": "req_011CbMFFXc6Ldv6UFFvdHVq3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8fc56fb3-9221-4160-b94c-74e330f7809a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/director_a20165af",
  "sessionId": "c9dbaca8-1cd1-415f-aa7b-2e5963ce8650",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Fchhx4D5zdWASe9ejh6TrJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1188,
      "cache_read_input_tokens": 39607,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1188,
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

_source line 8 · 2026-05-24T10:36:22.845Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Hq2BZns7D9LyqRYApoJBan`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fc56fb3-9221-4160-b94c-74e330f7809a",
  "isSidechain": true,
  "agentId": "a2bfd38fb2f2154cb",
  "requestId": "req_011CbMFFXc6Ldv6UFFvdHVq3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3a239750-f893-4898-89b4-7fe5c023c6cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/director_a20165af",
  "sessionId": "c9dbaca8-1cd1-415f-aa7b-2e5963ce8650",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Fchhx4D5zdWASe9ejh6TrJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1188,
      "cache_read_input_tokens": 39607,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1188
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 145,
          "cache_read_input_tokens": 39607,
          "cache_creation_input_tokens": 1188,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1188,
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

_source line 9 · 2026-05-24T10:36:23.118Z_

<details><summary>↩ Tool result · `toolu_01Hq2BZns7D9LyqRYApoJBan`</summary>

```text
1	\appendix
2	
3	\section{Proof of Theorem~\ref{thm:monotonicity}}
4	\label{app:proof}
5	
6	The replaced judge $J_K'$ is \emph{pivotal} exactly when $t{-}1$ of the remaining $K{-}1$ judges have already failed. Formally, let $S = \sum_{j=1}^{K-1} X_j^a$ denote the number of failures among the shared judges. The panel fails if and only if the $K$-th judge also fails when $S = t{-}1$, or when $S \geq t$ regardless of the $K$-th judge:
7	\begin{align}
8	\mathrm{ASR}(\mathcal{P}, a) &= \Pr(S \geq t) + \Pr(S = t{-}1) \cdot \Pr(X_K^a {=} 1 \mid S = t{-}1).
9	\end{align}
10	Since $\Pr(X_{K'}^a {=} 1 \mid \mathbf{X}_{-K}^a {=} \mathbf{x}_{-K}) \geq \Pr(X_K^a {=} 1 \mid \mathbf{X}_{-K}^a {=} \mathbf{x}_{-K})$ for all attacks $a$ and realizations $\mathbf{x}_{-K}$ (by hypothesis), the second term is weakly larger for $\mathcal{P}'$ than for $\mathcal{P}$ under every attack. Taking the supremum over attacks preserves the inequality: $\mathrm{ASR}^*(\mathcal{P}') \geq \mathrm{ASR}^*(\mathcal{P})$. The result holds under arbitrary inter-judge correlations and any attack space $\mathcal{A}$.
11	
12	\section{Robustness Correction Methods}
13	\label{app:robustness_methods}
14	
15	The 455 panels are constructed combinatorially from 15 shared judges: each judge appears in $\binom{14}{2} = 91$ panels, inducing correlated residuals across panel-level observations. Standard OLS assumes independent errors, potentially inflating significance. We apply three corrections.
16	
17	\paragraph{Clustered Standard Errors.} Because each panel of $K{=}3$ judges does not map to a single cluster, we perform three separate one-way clusterings (one for each judge position in the ordered panel tuple) using CR1 bias-corrected sandwich estimators (13 clusters per position). The reported standard error for each coefficient is the maximum across the three clusterings, yielding the most conservative inference.
18	
19	\paragraph{Mixed Effects.} For each of the three judge positions, we fit a linear mixed-effects model with a random intercept for the judge occupying that position, estimating $K_{\mathrm{eff}}$ and $\eta_{\max}$ as fixed effects. The reported $p$-value for each coefficient is the maximum across the three models.
20	
21	\paragraph{Wild Cluster Bootstrap.} We perform $B{=}9{,}999$ bootstrap resamples using Rademacher weights, clustering by each of the three panel positions in turn and taking the maximum $p$-value across positions (the most conservative aggregation). This approach avoids distributional assumptions on the cluster structure.
22	
23	\section{Extended Analysis}
24	\label{app:extended_analysis}
25	
26	\subsection{BFT Reversal Mechanism: Detailed Evidence}
27	\label{app:bft_reversal}
28	
29	Under standard OLS, the regression results (Table~\ref{tab:dominance}) show $\eta_{\max}$ significant in 10 of 12 conditions and $K_{\mathrm{eff}}$ positively associated with ASR in all 12. Non-independence correction attenuates both predictors: under wild cluster bootstrap, $\eta_{\max}$ retains 3/12 and $K_{\mathrm{eff}}$ retains 4/12, with $K_{\mathrm{eff}}$ slightly ahead. The directional pattern (all $K_{\mathrm{eff}}$ point estimates positive) persists uniformly. The random-fault contrast (\S\ref{sec:rf_contrast}) sharpens this: under random faults, $K_{\mathrm{eff}}$'s positive association with panel error survives all corrections (2/2 conditions, $R^2 = 0.73$--$0.81$), indicating a genuine relationship whose statistical confidence attenuates under adaptive attack (4/12 after correction).
30	
31	\begin{figure}[h]
32	\centering
33	\includegraphics[width=\columnwidth]{figures/fig2_gam_keff_split.pdf}
34	\caption{GAM bootstrap $K_{\mathrm{eff}}$ effect direction at $K{=}3$ ($B{=}9999$). All 12 conditions show positive $K_{\mathrm{eff}}$ direction (88.9--100\% bootstrap rate). The Kruskal--Wallis test finds no significant magnitude difference between targeted and shared-bias attacks ($p{=}0.200$).}
35	\label{fig:gam_split}
36	\end{figure}
37	
38	Under corrected data (V2), all 12 $K_{\mathrm{eff}}$ OLS coefficients are positive. The previously reported negative ARC $\times$ sycophancy coefficient ($\hat{\beta}_{\mathrm{std}} = -0.192$) was an artifact of error-as-tie handling; after correction, it becomes positive ($\hat{\beta}_{\mathrm{std}} = +0.257$). GAM bootstrap confirms the uniform positive direction: 12/12 conditions at $K{=}3$ (88.9--100\% positive rate) and 12/12 at $K{=}5$ (100\%).
39	
40	\subsection{Diversity--Capability Tradeoff}
41	\label{app:diversity_capability}
42	
43	The $r = 0.70$--$0.81$ correlation between $K_{\mathrm{eff}}$ and $\eta_{\max}$ ($K{=}3$ to $K{=}5$) reflects a structural feature of the current LLM ecosystem: maximizing panel diversity requires sampling across capability tiers, which systematically introduces less capable and therefore more vulnerable judges. The structural correlation is unaffected by SE correction; it is a property of the model ecosystem, not an artifact of panel overlap. However, the high confound combined with fragile independent significance means that observational regression cannot reliably disentangle diversity's causal contribution from the capability deficit that co-occurs with it.
44	
45	\begin{figure}[h]
46	\centering
47	\includegraphics[width=\columnwidth]{figures/fig_keff_eta_scatter.pdf}
48	\caption{Panel-level correlation between $K_{\mathrm{eff}}$ and $\eta_{\max}$ at $K{=}5$ ($n{=}3{,}003$ panels). Full model pool (gray, $r{=}0.81$) exhibits strong collinearity; capability-matched Pool~A (orange diamonds, $r{=}0.50$, 126 panels) shows reduced confounding.}
49	\label{fig:keff_eta_scatter}
50	\end{figure}
51	
52	Family-level labels provide indirect evidence that capability proximity matters more than taxonomic grouping: family membership is not a significant predictor of panel vulnerability ($p = 0.179$ on MMLU, $p = 0.385$ on ARC), consistent with models from the same provider exhibiting heterogeneous vulnerability profiles that vary by capability tier rather than by shared architecture \citep{kuncheva2003measures}.
53	
54	\subsection{Aggregation Mechanism Details}
55	\label{app:aggregation_details}
56	
57	Bayesian calibration attenuates $K_{\mathrm{eff}}$ significance (5+/1$-$) and reduces overall predictability ($R^2{=}0.087$), but $\eta_{\max}$ persists (9/12 under OLS), providing partial defense. The mechanism is calibrated reliability weighting: by estimating each judge's confusion matrix on clean data, Bayesian aggregation downweights weak judges, reducing the diversity channel while the individual weakness channel remains active. Threshold voting amplifies both channels because any single dissenting judge vetoes the panel decision, making compositional factors highly predictive of attack success ($R^2{=}0.829$). Bayesian calibration requires a clean accuracy prior, and an adaptive attacker aware of this calibration could target the prior itself \citep{tambe2011security}.
58	
59	\begin{figure}[h]
60	\centering
61	\includegraphics[width=\columnwidth]{figures/fig3_aggregation_gradient.pdf}
62	\caption{Distribution of $K_{\mathrm{eff}}$ coefficients across aggregation methods. Majority and weighted voting show uniformly positive $K_{\mathrm{eff}}$ direction (12+/0$-$). Bayesian calibration reduces overall predictability ($R^2{=}0.087$) with predominantly positive direction (5+/1$-$).}
63	\label{fig:aggregation}
64	\end{figure}
65	
66	\subsection{Aggregation at \texorpdfstring{$K{=}5$}{K=5}}
67	\label{app:aggregation_k5}
68	
69	Table~\ref{tab:aggregation_k5} extends the aggregation analysis to $K{=}5$ (3{,}003 panels) under wild cluster bootstrap with 5-position max-$p$. All four aggregation methods yield identical $K_{\mathrm{eff}}$ significance (7/12), with $\eta_{\max}$ uniformly low (2--3/12). The Bayesian attenuation observed at $K{=}3$ (5+/1$-$; Table~\ref{tab:aggregation}) does not persist: $K_{\mathrm{eff}}$ reaches 7/12 regardless of aggregation rule. Predictability still varies ($\bar{R}^2$: threshold 0.408, Bayesian 0.166), but the diversity channel operates uniformly across all methods. At $K{=}7$, however, methods diverge again: Bayesian neutralization returns (0/12) while threshold voting strengthens to 10/12 (Table~\ref{tab:aggregation_k7}).
70	
71	\begin{table}[h]
72	\centering
73	\small
74	\begin{tabular}{lccc}
75	\toprule
76	\textbf{Aggregation} & $\boldsymbol{\eta_{\max}}$ \textbf{sig} & $\boldsymbol{K_{\mathrm{eff}}}$ \textbf{sig} & $\boldsymbol{\bar{R}^2}$ \\
77	\midrule
78	Majority   & 2/12  & 7/12 & 0.285 \\
79	Weighted   & 2/12  & 7/12 & 0.275 \\
80	Threshold  & 3/12  & 7/12 & 0.408 \\
81	Bayesian   & 2/12  & 7/12 & 0.166 \\
82	\bottomrule
83	\end{tabular}
84	\caption{Aggregation method comparison at $K{=}5$ (3{,}003 panels, wild cluster bootstrap with 5-position max-$p$, BH FDR $\alpha{=}0.05$). All four methods converge to $K_{\mathrm{eff}}$ 7/12, unlike the differentiated pattern at $K{=}3$ (Table~\ref{tab:aggregation}).}
85	\label{tab:aggregation_k5}
86	\end{table}
87	
88	\subsection{Aggregation at \texorpdfstring{$K{=}7$}{K=7}}
89	\label{app:aggregation_k7}
90	
91	Table~\ref{tab:aggregation_k7} extends the aggregation analysis to $K{=}7$ (6{,}435 panels) under wild cluster bootstrap with 7-position max-$p$. Unlike the uniform convergence at $K{=}5$ (all methods 7/12), aggregation methods diverge at $K{=}7$: threshold voting strengthens to 10/12 while Bayesian calibration drops to 0/12, restoring the neutralization pattern absent at $K{=}5$.
92	
93	\begin{table}[h]
94	\centering
95	\small
96	\begin{tabular}{lccc}
97	\toprule
98	\textbf{Aggregation} & $\boldsymbol{\eta_{\max}}$ \textbf{sig} & $\boldsymbol{K_{\mathrm{eff}}}$ \textbf{sig} & $\boldsymbol{\bar{R}^2}$ \\
99	\midrule
100	Majority   & 1/12  & 8/12 & 0.244 \\
101	Weighted   & 1/12  & 6/12 & 0.207 \\
102	Threshold  & 8/12  & 10/12 & 0.509 \\
103	Bayesian   & 1/12  & 0/12 & 0.105 \\
104	\bottomrule
105	\end{tabular}
106	\caption{Aggregation method comparison at $K{=}7$ (6{,}435 panels, wild cluster bootstrap with 7-position max-$p$, BH FDR $\alpha{=}0.05$). Unlike $K{=}5$ where all methods converge to 7/12, $K{=}7$ shows method divergence: threshold voting reaches 10/12 while Bayesian calibration returns to full $K_{\mathrm{eff}}$ neutralization (0/12).}
107	\label{tab:aggregation_k7}
108	\end{table}
109	
110	\subsection{Metric Robustness Under Partial Panel Information}
111	\label{app:oracle}
112	
113	The main analysis computes $\eta_{\max}$ with full knowledge of panel composition (all three judges known). In deployment, a practitioner selecting or auditing a panel may know only a subset of the constituent judges. We test whether $\eta_{\max}$ retains predictive power under such partial information by recomputing it from two of the three panel members: for each panel, we cycle through all $\binom{3}{1} = 3$ leave-one-out masks, compute $\eta_{\max}$ from the two known judges, and average the regression estimates across masking scenarios.
114	
115	Under the most conservative inference (partial information + clustered SE), $\eta_{\max}$ remains the sole significant predictor with $\hat{\beta}_{\mathrm{std}} = 0.589$, achieving significance in 12/12 conditions, stronger than the oracle baseline (4/12 under clustered SE). $K_{\mathrm{eff}}$ loses all predictive power (0/12). The averaging over masking scenarios smooths estimation noise inherent in the three-judge oracle computation, strengthening the $\eta_{\max}$ signal. This demonstrates that $\eta_{\max}$ computed from partial panel information is robust to incomplete composition knowledge and retains (indeed improves) its predictive power for panel ASR.
116	
117	\section{Panel Selection Strategy Comparison}
118	\label{app:panel_selection}
119	
120	\begin{figure}[h]
121	\centering
122	\includegraphics[width=\columnwidth]{figures/fig4_panel_design.pdf}
123	\caption{Panel attack success rate under three selection strategies. $\min(\eta_{\max})$ achieves lowest ASR in 12/12 conditions, confirming that robustness-first selection dominates diversity-maximizing strategies.}
124	\label{fig:panel_design}
125	\end{figure}
126	
127	Figure~\ref{fig:panel_design} compares three panel selection strategies: $\min(\eta_{\max})$ (select the panel minimizing weakest-judge vulnerability), random selection, and $\max(K_{\mathrm{eff}})$ (maximize diversity). The $\min(\eta_{\max})$ strategy achieves the lowest ASR in all 12 conditions, consistent with the weakest-link dominance documented in \S\ref{sec:dominance}.
128	
129	\section{Clustered Standard Error Analysis}
130	\label{app:forest_plot}
131	
132	Under clustered standard errors (clustering on the $K$ judge positions), $\eta_{\max}$ retains significance in 4/12 conditions while $K_{\mathrm{eff}}$ achieves significance in 0/12. This contrasts with OLS ($\eta_{\max}$ 10/12, $K_{\mathrm{eff}}$ 12/12) and wild cluster bootstrap ($\eta_{\max}$ 3/12, $K_{\mathrm{eff}}$ 4/12), illustrating how the choice of inference method modulates apparent significance at $K{=}3$ while coefficient direction remains uniformly positive for $K_{\mathrm{eff}}$ across all methods (Figure~\ref{fig:robustness}).
133	
134	\section{Robustness Checks: Subsampling and Specification}
135	\label{app:robustness_checks}
136	
137	Table~\ref{tab:robustness_checks} summarizes regression results across model subsets and alternative specifications at $K{=}5$, testing whether the predictor shift is robust to collinearity reduction and specification choice.
138	
139	\begin{table}[h]
140	\centering
141	\small
142	\begin{tabular}{lcccc}
143	\toprule
144	\textbf{Subset / Method} & $\boldsymbol{r}$ & $\boldsymbol{\eta_{\max}}$ & $\boldsymbol{K_{\mathrm{eff}}}$ & \textbf{Trans.} \\
145	\midrule
146	Full bootstrap       & 0.81 & 2/12 & 7/12 & \checkmark \\
147	API-only (9) clust.  & 0.85 & 8/12 & 3/12 & --- \\
148	Cap-matched A (5A+4L) & 0.50 & ---  & 9/12 & \checkmark\checkmark \\
149	Cap-matched B (6A+3L) & 0.73 & ---  & 2/12 & --- \\
150	Fractional logit     & 0.81 & 4/12 & 11/12 & \checkmark \\
151	\bottomrule
152	\end{tabular}
153	\caption{Predictor shift robustness at $K{=}5$ across model subsets and specifications. $r$: correlation between $K_{\mathrm{eff}}$ and $\eta_{\max}$. $\eta_{\max}$ and $K_{\mathrm{eff}}$ columns show FDR-significant counts out of 12 conditions. Trans.: whether $K_{\mathrm{eff}}$ dominates $\eta_{\max}$. API-only models ($r{=}0.85$, VIF${=}4.4$) show partially collinear predictors; capability-matched subsamples ($r{=}0.50$) strengthen the shift. Fractional logit \citep{papke1996econometric} confirms OLS patterns with 98.6\% directional agreement (71/72 direction matches; the single discordance is $\eta_{\max}$ at $K{=}7$ for ARC $\times$ score manipulation).}
154	\label{tab:robustness_checks}
155	\end{table}
156	
157	The API-only subset ($r{=}0.85$, VIF${=}4.4$) demonstrates that elevated collinearity between $K_{\mathrm{eff}}$ and $\eta_{\max}$ partially inflates standard errors: both predictors achieve moderate significance but neither dominates, and the predictor shift does not replicate. Breaking collinearity through capability-matched subsampling (pool~A, $r{=}0.50$) strengthens $K_{\mathrm{eff}}$'s emergence to 9/12, comparable to the full-pool 7/12. Pool~B ($r{=}0.73$) falls near the decorrelation threshold, and the shift weakens accordingly. Random 9-model subsampling (1{,}000 trials) confirms an inverted-U: $K_{\mathrm{eff}}$ dominance rate peaks when the subsample includes 3--4 local models (maximizing capability spread) and drops when the pool is too homogeneous (Appendix~\ref{app:random_subsample}).
158	
159	\section{Random Subsample Analysis}
160	\label{app:random_subsample}
161	
162	To test whether the predictor shift depends on model pool composition, we randomly sample 9 of 15 models (1{,}000 trials), construct all $\binom{9}{5}$ panels, and run the bootstrap analysis at $K{=}5$. We stratify by the number of local models ($n_{\mathrm{local}} \in \{0, \ldots, 6\}$) in each subsample.
163	
164	Under clustered standard errors, $K_{\mathrm{eff}}$ is the dominant predictor in 51.4\% of subsamples (mean significance 1.85/12), with an inverted-U as a function of $n_{\mathrm{local}}$: subsamples with 3--4 local models (maximizing capability range) achieve the highest $K_{\mathrm{eff}}$ significance rate, while all-API ($n_{\mathrm{local}}{=}0$) and heavily-local ($n_{\mathrm{local}}{\geq}5$) subsamples show reduced detection. Significance is attenuated relative to the full pool by smaller sample sizes (126 vs.\ 3{,}003 panels at $K{=}5$), but the shift direction holds in the majority of subsamples. This confirms that the shift's detectability depends on capability diversity in the model pool rather than pool size per se.
165	
166	\section{Attacked $K_{\mathrm{eff}}$ Stability}
167	\label{app:attacked_keff}
168	
169	$K_{\mathrm{eff}}$ is computed from clean (unattacked) pairwise MI (\S\ref{sec:experiments}), but used to predict vulnerability under attack. We verify this assumption by recomputing MI from judge outputs under each attack type and comparing clean vs.\ attacked $K_{\mathrm{eff}}$ via Spearman rank correlation across all panels.
170	
171	\begin{table}[h]
172	\centering
173	\small
174	\begin{tabular}{lcc}
175	\toprule
176	\textbf{Attack} & \textbf{MMLU $\rho$} & \textbf{ARC $\rho$} \\
177	\midrule
178	Score manipulation & 0.98 & 0.99 \\
179	Authority bias     & 0.95 & 0.97 \\
180	Sycophancy         & 0.91 & 0.92 \\
181	Verbosity bias     & 0.91 & 0.92 \\
182	Prompt injection   & 0.63 & 0.60 \\
183	Position bias      & 0.60 & 0.08 \\
184	\bottomrule
185	\end{tabular}
186	\caption{Spearman rank correlation between clean and attacked $K_{\mathrm{eff}}$ across 455 panels ($K{=}3$). Four attack types preserve MI structure ($\rho{\geq}0.91$); prompt injection shows moderate perturbation ($\rho{\approx}0.60$--$0.63$); position bias substantially disrupts pairwise dependencies.}
187	\label{tab:attacked_keff}
188	\end{table}
189	
190	Four attack types (score manipulation, authority bias, sycophancy, verbosity bias) preserve MI structure with $\rho{\geq}0.91$ on both benchmarks, validating the use of clean $K_{\mathrm{eff}}$ as a predictor. Prompt injection shows moderate perturbation ($\rho{\approx}0.60$--$0.63$), consistent with its mechanism of overriding evaluation instructions, which can alter pairwise agreement patterns. Position bias substantially disrupts MI structure ($\rho{=}0.08$ on ARC, $p{=}0.10$), consistent with its anomalous regression behavior in Table~\ref{tab:dominance} (sole non-significant $\eta_{\max}$ condition) and suggesting that positional reordering fundamentally changes inter-judge dependence rather than merely introducing noise.
191	
192	\section{Cinelli--Hazlett Sensitivity Analysis}
193	\label{app:sensitivity}
194	
195	We apply the Cinelli--Hazlett omitted variable bias framework to quantify how robust $K_{\mathrm{eff}}$'s coefficient is to unobserved confounders. For each of the 36 conditions ($3K \times 2$ benchmarks $\times$ $6$ attacks), we compute the robustness value (RV): the minimum strength an unobserved confounder must have, in terms of partial $R^2$ with both treatment and outcome, to reduce $K_{\mathrm{eff}}$'s coefficient to zero.
196	
197	\begin{table}[h]
198	\centering
199	\footnotesize
200	\setlength{\tabcolsep}{3pt}
201	\begin{tabular}{rcllcccc}
202	\toprule
203	$\boldsymbol{K}$ & \textbf{Data} & \textbf{Attack} & \textbf{RV} & $\boldsymbol{\eta}$ $\boldsymbol{R^2_{\mathrm{tr}}}$ & $\boldsymbol{\eta}$ $\boldsymbol{R^2_{\mathrm{out}}}$ & \textbf{Exc.} \\
204	\midrule
205	3 & MMLU & Prompt inj.    & 0.419 & 0.587 & 0.059 & -- \\
206	3 & MMLU & Sycophancy     & 0.412 & 0.347 & 0.098 & \checkmark \\
207	3 & MMLU & Score manip.   & 0.410 & 0.735 & 0.002 & -- \\
208	3 & MMLU & Verbosity      & 0.330 & 0.342 & 0.203 & -- \\
209	3 & MMLU & Position bias  & 0.291 & 0.446 & 0.043 & -- \\
210	3 & MMLU & Authority bias & 0.371 & 0.493 & 0.019 & -- \\
211	3 & ARC  & Prompt inj.    & 0.303 & 0.654 & 0.028 & -- \\
212	3 & ARC  & Sycophancy     & 0.105 & 0.629 & 0.129 & -- \\
213	3 & ARC  & Score manip.   & 0.273 & 0.838 & 0.003 & -- \\
214	3 & ARC  & Verbosity      & 0.259 & 0.658 & 0.047 & -- \\
215	3 & ARC  & Position bias  & 0.265 & 0.850 & 0.001 & -- \\
216	3 & ARC  & Authority bias & 0.224 & 0.582 & 0.056 & -- \\
217	\addlinespace
218	5 & MMLU & Prompt inj.    & 0.455 & 0.379 & 0.176 & \checkmark \\
219	5 & MMLU & Sycophancy     & 0.303 & 0.106 & 0.135 & \checkmark \\
220	5 & MMLU & Score manip.   & 0.321 & 0.597 & 0.003 & -- \\
221	5 & MMLU & Verbosity      & 0.235 & 0.120 & 0.206 & \checkmark \\
222	5 & MMLU & Position bias  & 0.131 & 0.272 & 0.090 & -- \\
223	5 & MMLU & Authority bias & 0.064 & 0.277 & 0.031 & -- \\
224	5 & ARC  & Prompt inj.    & 0.318 & 0.696 & 0.001 & -- \\
225	5 & ARC  & Sycophancy     & 0.103 & 0.555 & 0.063 & -- \\
226	5 & ARC  & Score manip.   & 0.196 & 0.800 & ${<}0.001$ & -- \\
227	5 & ARC  & Verbosity      & 0.135 & 0.642 & 0.034 & -- \\
228	5 & ARC  & Position bias  & 0.400 & 0.778 & 0.040 & -- \\
229	5 & ARC  & Authority bias & 0.181 & 0.509 & 0.012 & -- \\
230	\addlinespace
231	7 & MMLU & Prompt inj.    & 0.522 & 0.289 & 0.126 & \checkmark \\
232	7 & MMLU & Sycophancy     & 0.301 & 0.077 & 0.078 & \checkmark \\
233	7 & MMLU & Score manip.   & 0.393 & 0.515 & 0.004 & -- \\
234	7 & MMLU & Verbosity      & 0.205 & 0.078 & 0.195 & \checkmark \\
235	7 & MMLU & Position bias  & 0.207 & 0.179 & 0.073 & \checkmark \\
236	7 & MMLU & Authority bias & 0.005 & 0.200 & 0.011 & -- \\
237	7 & ARC  & Prompt inj.    & 0.355 & 0.629 & 0.004 & -- \\
238	7 & ARC  & Sycophancy     & 0.117 & 0.535 & 0.065 & -- \\
239	7 & ARC  & Score manip.   & 0.165 & 0.717 & 0.001 & -- \\
240	7 & ARC  & Verbosity      & 0.165 & 0.599 & 0.028 & -- \\
241	7 & ARC  & Position bias  & 0.422 & 0.705 & 0.046 & -- \\
242	7 & ARC  & Authority bias & 0.179 & 0.514 & 0.003 & -- \\
243	\bottomrule
244	\end{tabular}
245	\caption{Cinelli--Hazlett sensitivity analysis for $K_{\mathrm{eff}}$'s coefficient across 36 conditions. RV: robustness value (minimum partial $R^2$ an unobserved confounder must have with both $K_{\mathrm{eff}}$ and ASR to nullify the coefficient). $\eta$ $R^2_{\mathrm{tr}}$/$R^2_{\mathrm{out}}$: partial $R^2$ of $\eta_{\max}$ with $K_{\mathrm{eff}}$ (treatment) and ASR (outcome). Exc.: \checkmark\ if RV exceeds $\eta_{\max}$'s partial $R^2$ with treatment, indicating $K_{\mathrm{eff}}$'s coefficient is robust to the known capability confound. RV exceeds $\eta_{\max}$ in 11/36 conditions ($K{=}3$: 4/12, $K{=}5$: 3/12, $K{=}7$: 4/12).}
246	\label{tab:sensitivity}
247	\end{table}
248	
249	RV ranges from 0.005--0.59 across the 36 conditions (median by $K$: 0.30 at $K{=}3$, 0.22 at $K{=}5$, 0.21 at $K{=}7$), revealing heterogeneous robustness: some conditions show $K_{\mathrm{eff}}$ coefficients robust to strong confounders (e.g., $K{=}7$ MMLU prompt injection, RV${=}0.52$), while others are fragile (e.g., $K{=}7$ MMLU authority bias, RV${=}0.005$). The known $\eta_{\max}$ confound exceeds RV in 25/36 conditions ($K{=}3$: 8/12, $K{=}5$: 9/12, $K{=}7$: 8/12). RV exceeds $\eta_{\max}$ in 3--4/12 conditions across all $K$ values (4/12 at $K{=}3$, 3/12 at $K{=}5$, 4/12 at $K{=}7$), indicating that $K_{\mathrm{eff}}$'s robustness to omitted variable bias is stable rather than monotonically increasing with panel size.
250	
251	\begin{figure}[h]
252	\centering
253	\includegraphics[width=\columnwidth]{figures/fig_sensitivity_contour_K5.png}
254	\caption{Cinelli--Hazlett sensitivity contour plot at $K{=}5$ (representative). $x$-axis: confounder's partial $R^2$ with treatment ($K_{\mathrm{eff}}$); $y$-axis: confounder's partial $R^2$ with outcome (ASR). Contour lines show the adjusted $K_{\mathrm{eff}}$ coefficient under hypothetical confounders of varying strength. The diamond marks the known $\eta_{\max}$ confound benchmark; conditions where the benchmark falls inside the zero-contour indicate that the $\eta_{\max}$ confound alone could explain away $K_{\mathrm{eff}}$'s effect.}
255	\label{fig:sensitivity_contour}
256	\end{figure}
257	
258	\section{Cross-Benchmark Prediction Robustness}
259	\label{app:cross_benchmark}
260	
261	To test whether the diversity--vulnerability association reflects structural panel properties rather than benchmark-specific artifacts, we use $K_{\mathrm{eff}}$ computed from one benchmark's pairwise MI to predict panel vulnerability on the other. Under wild cluster bootstrap (FDR $\alpha{=}0.05$), MMLU-derived $K_{\mathrm{eff}}$ predicts ARC vulnerability in 17/18 conditions across $K \in \{3, 5, 7\}$ (5/6 at $K{=}3$, 6/6 at $K{\geq}5$); the sole exception is $K{=}3$ position bias, where all judges share similar ASR (${\sim}0.5$), leaving insufficient heterogeneity for $K_{\mathrm{eff}}$ to discriminate. The reverse direction (ARC$\to$MMLU) achieves 10/18, with attenuation concentrated at $K{\geq}5$ (4/12), consistent with ARC's binary format producing lower MI discriminability between judge pairs. Cross-benchmark $K_{\mathrm{eff}}$ correlations are $r{\approx}0.76$--$0.78$, indicating that $K_{\mathrm{eff}}$ primarily captures panel-level compositional structure rather than benchmark-specific judge interactions. The asymmetry between prediction directions further suggests that MI estimated from richer response distributions (MMLU's four-way choice) yields a more transferable diversity measure.
262	
263	\section{Pool A Cinelli--Hazlett Sensitivity}
264	\label{app:sensitivity_poolA}
265	
266	To test whether reducing the $K_{\mathrm{eff}}$--$\eta_{\max}$ collinearity strengthens $K_{\mathrm{eff}}$'s independent signal, we repeat the Cinelli--Hazlett analysis on the capability-matched Pool~A subsample (9 models, $r{=}0.50$, 84 panels at $K{=}3$, 126 at $K{=}5$). Table~\ref{tab:sensitivity_poolA} compares the full-pool results with Pool~A.
267	
268	\begin{table}[h]
269	\centering
270	\small
271	\begin{tabular}{lccc}
272	\toprule
273	\textbf{Pool / $K$} & \textbf{RV $>$ $\eta$} & \textbf{Median RV} & \textbf{$K_{\mathrm{eff}}$ sig} \\
274	\midrule
275	Full / $K{=}3$ & 1/12 & 0.30 & 1/12 \\
276	Full / $K{=}5$ & 3/12 & 0.22 & 7/12 \\
277	Pool A / $K{=}3$ & 2/12 & 0.25 & --- \\
278	Pool A / $K{=}5$ & 10/12 & 0.32 & 9/12 \\
279	\bottomrule
280	\end{tabular}
281	\caption{Cinelli--Hazlett sensitivity comparison: full pool vs.\ capability-matched Pool~A. RV $>$ $\eta$: conditions where $K_{\mathrm{eff}}$'s robustness value exceeds the known $\eta_{\max}$ confound benchmark. Pool~A's reduced collinearity ($r{=}0.50$ vs.\ $0.81$ at $K{=}5$) increases the fraction of robust conditions from 1/12 to 2/12 at $K{=}3$ and from 3/12 to 10/12 at $K{=}5$, with the largest gains at $K{=}5$ where both benchmarks improve equally (ARC 5/6, MMLU 5/6).}
282	\label{tab:sensitivity_poolA}
283	\end{table}
284	
285	At $K{=}5$, Pool~A RV exceeds the $\eta_{\max}$ confound in 10/12 conditions (ARC 5/6, MMLU 5/6; the two failures are both sycophancy). The improvement from full-pool 3/12 to Pool~A 10/12 demonstrates that reducing collinearity substantially separates $K_{\mathrm{eff}}$'s signal from capability variance, though full causal identification would require training-based diversity control.
286	
287	\section{Epsilon Sensitivity Analysis}
288	\label{app:epsilon}
289	
290	The log-log specification (Equation~\ref{eq:regression}) uses $\epsilon{=}10^{-6}$ to handle zero ASR values. We assess sensitivity by comparing coefficients across $\epsilon \in \{10^{-3}, 10^{-6}, 10^{-9}\}$. Zero ASR rates are low on MMLU ($<$1\% of panels across conditions) but can reach 38--40\% on ARC for authority bias and sycophancy at $K{=}7$. Coefficient magnitudes show moderate sensitivity to $\epsilon$ at $K{=}3$ (maximum $\Delta\beta_{\mathrm{std}} = 0.10$ between $\epsilon{=}10^{-6}$ and $\epsilon{=}10^{-9}$, with three conditions exhibiting $K_{\mathrm{eff}}$ sign changes), reflecting the influence of zero-ASR panels on the log transformation. At $K{=}5$, all $K_{\mathrm{eff}}$ coefficient directions are preserved across $\epsilon$ values (maximum $\Delta\beta_{\mathrm{std}} = 0.073$ between $\epsilon{=}10^{-6}$ and $\epsilon{=}10^{-9}$, all $p < 0.005$), confirming that the predictor shift finding is robust to this modeling choice. The fractional logit specification (\S\ref{sec:experiments}), which avoids the log+$\epsilon$ transformation entirely, provides 98.6\% directional concordance with the main OLS results (71/72 direction matches) (Appendix~\ref{app:robustness_checks}).
291	
292	\section{Temperature Sensitivity Pilot}
293	\label{app:temperature}
294	
295	We evaluate $K_{\mathrm{eff}}$ stability across decoding temperatures $t \in \{0.0, 0.3, 0.7, 1.0\}$ using a 3-model pilot (GPT-4.1-nano, Gemini-3.5-Flash, Claude-3-Haiku; 300 clean samples per benchmark, 3 repeats). The maximum $K_{\mathrm{eff}}$ variation across all four temperatures is $\Delta < 0.034$ (MMLU: 0.033, ARC: 0.027), confirming that decoding randomness does not meaningfully perturb pairwise MI structure. Clean $K_{\mathrm{eff}}$ computation is thus robust to temperature variation within the range used by standard API configurations.
296	
297	\section{$K_{\mathrm{eff}}$ Distribution Statistics}
298	\label{app:keff_dist}
299	
300	Table~\ref{tab:keff_dist} summarizes the distribution of $K_{\mathrm{eff}}$ across panel sizes.
301	
302	\begin{table}[h]
303	\centering
304	\small
305	\begin{tabular}{rrccc}
306	\toprule
307	$\boldsymbol{K}$ & \textbf{Panels} & \textbf{Mean (SD)} & \textbf{Range} \\
308	\midrule
309	3 & 455     & 2.18 (0.30) & [1.47, 2.80] \\
310	5 & 3{,}003 & 3.35 (0.42) & [2.16, 4.30] \\
311	7 & 6{,}435 & 4.53 (0.47) & [2.97, 5.55] \\
312	\bottomrule
313	\end{tabular}
314	\caption{$K_{\mathrm{eff}}$ distribution across panel sizes. Mean $K_{\mathrm{eff}}$ increases approximately linearly with $K$ but remains below the theoretical maximum ($K_{\mathrm{eff}} = K$ for fully independent judges), reflecting non-zero inter-judge correlations.}
315	\label{tab:keff_dist}
316	\end{table}
317	
318	$K_{\mathrm{eff}}$ exhibits sufficient variance at each $K$ for regression analysis (coefficient of variation 10--14\%), with no floor or ceiling effects that would compress the predictor range.
319	
320	\section{Power Analysis Across Panel Sizes}
321	\label{app:power_analysis}
322	
323	Table~\ref{tab:mde} reports minimum detectable effect sizes (MDE at 80\% power) under wild cluster bootstrap for each $K$. The sharp decrease in MDE from $K{=}3$ to $K{=}5$ (0.144 to 0.048) reflects both increased sample size ($455 \to 3{,}003$ panels) and more clusters per position. $K_{\mathrm{eff}}$'s partial significance at $K{=}3$ (4/12) is consistent with moderate power at this sample size; the 7/12 significance at $K{=}5$ is not type~I error inflation, as the design can detect effects as small as 0.048 SD.
324	
325	\begin{table}[h]
326	\centering
327	\small
328	\begin{tabular}{rccc}
329	\toprule
330	$\boldsymbol{K}$ & \textbf{Panels} & \textbf{MDE ($\beta_{\mathrm{std}}$)} & \textbf{$K_{\mathrm{eff}}$ sig} \\
331	\midrule
332	3 & 455     & 0.144 & 4/12 \\
333	5 & 3{,}003 & 0.048 & 7/12 \\
334	7 & 6{,}435 & 0.036 & 8/12 \\
335	\bottomrule
336	\end{tabular}
337	\caption{Minimum detectable effect size (80\% power, 1{,}000 simulations, wild cluster bootstrap) by panel size. MDE decreases approximately as $1/\sqrt{N}$, confirming that $K{=}5$/$K{=}7$ significance reflects genuine effects rather than inflated type~I error.}
338	\label{tab:mde}
339	\end{table}
340	
341	\section{Alternative Diversity Measures}
342	\label{app:alt_diversity}
343	
344	We compare $K_{\mathrm{eff}}$ against three classical ensemble diversity measures using the same OLS specification (Equation~\ref{eq:regression}) with FDR correction across 12 conditions pooled over $K$ values.
345	
346	\begin{table}[h]
347	\centering
348	\small
349	\begin{tabular}{lcccc}
350	\toprule
351	\textbf{Measure} & \textbf{Sig} & \textbf{Dir.} & \textbf{$|\bar{\beta}_{\mathrm{std}}|$} & $\boldsymbol{\rho}$ \textbf{w/} $\boldsymbol{K_{\mathrm{eff}}}$ \\
352	\midrule
353	$Q$-statistic    & 9/12  & 6+/3$-$ & 0.251 & 0.599 \\
354	Disagreement     & 11/12 & 11+/0$-$ & 0.481 & 0.934 \\
355	$\kappa$-diversity & 11/12 & 11+/0$-$ & 0.497 & 0.978 \\
356	\addlinespace
357	$K_{\mathrm{eff}}$ (ref.) & 12/12 & 12+/0$-$ & 0.430 & --- \\
358	\bottomrule
359	\end{tabular}
360	\caption{Comparison of diversity measures as predictors of panel ASR (OLS, FDR-corrected, 12 conditions pooled across $K$). Sig: FDR-significant conditions. $|\bar{\beta}_{\mathrm{std}}|$: mean absolute standardized coefficient. $\rho$: Pearson correlation with $K_{\mathrm{eff}}$.}
361	\label{tab:alt_diversity}
362	\end{table}
363	
364	$K_{\mathrm{eff}}$ and $\kappa$-diversity \citep{kuncheva2003measures} are near-equivalent ($\rho{=}0.978$), with comparable significance counts (12/12 vs.\ 11/12) and effect sizes (0.430 vs.\ 0.497). Disagreement rate achieves similar predictive power ($\rho{=}0.934$, 11/12). The $Q$-statistic is the weakest predictor (9/12, $|\bar{\beta}_{\mathrm{std}}|{=}0.251$), consistent with its known insensitivity to the type of error correlation that is associated with panel vulnerability \citep{kuncheva2003measures}. $K_{\mathrm{eff}}$'s advantage over these alternatives is not predictive power but interpretability: it quantifies the number of effective independent channels in the panel, connecting directly to the information-theoretic foundation of panel aggregation (\S\ref{sec:experiments}).
365	
366	\section{$\kappa$-Diversity Predictor Shift Comparison}
367	\label{app:kappa_regime}
368	
369	To test whether the predictor shift (\S\ref{sec:cross_k}) is specific to $K_{\mathrm{eff}}$ or a generic property of diversity measures, we repeat the wild cluster bootstrap analysis replacing $K_{\mathrm{eff}}$ with $\kappa$-diversity ($1 - \bar{\kappa}$, where $\bar{\kappa}$ is the mean pairwise Cohen's $\kappa$ on clean winner labels; $\rho{=}0.978$ with $K_{\mathrm{eff}}$).
370	
371	\begin{table}[h]
372	\centering
373	\small
374	\begin{tabular}{rcccc}
375	\toprule
376	& \multicolumn{2}{c}{\textbf{$K_{\mathrm{eff}}$}} & \multicolumn{2}{c}{\textbf{$\kappa$-diversity}} \\
377	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
378	$\boldsymbol{K}$ & \textbf{div.\ sig} & $\boldsymbol{\eta_{\max}}$ \textbf{sig} & \textbf{div.\ sig} & $\boldsymbol{\eta_{\max}}$ \textbf{sig} \\
379	\midrule
380	3 & 4/12  & 3/12 & 8/12 & 1/12 \\
381	5 & 7/12 & 2/12 & 7/12 & 4/12 \\
382	7 & 8/12  & 1/12 & 6/12 & 1/12 \\
383	\bottomrule
384	\end{tabular}
385	\caption{Predictor shift comparison: $K_{\mathrm{eff}}$ vs.\ $\kappa$-diversity across panel sizes (wild cluster bootstrap, BH FDR $\alpha{=}0.05$). $K_{\mathrm{eff}}$ exhibits a clear shift ($4 \to 7 \to 8$); $\kappa$-diversity significance decreases monotonically ($8 \to 7 \to 6$), showing no predictor shift.}
386	\label{tab:kappa_regime}
387	\end{table}
388	
389	$\kappa$-diversity is a stronger predictor than $K_{\mathrm{eff}}$ at $K{=}3$ (8/12 vs.\ 4/12), consistent with its larger mean effect size ($|\bar{\beta}_{\mathrm{std}}|{=}0.497$ vs.\ 0.430; Table~\ref{tab:alt_diversity}). However, $\kappa$-diversity shows no predictor shift: its significance \emph{decreases} from $K{=}3$ to $K{=}7$ ($8 \to 7 \to 6$), the opposite of $K_{\mathrm{eff}}$'s pattern ($4 \to 7 \to 8$). Furthermore, under $\kappa$-diversity, $\eta_{\max}$ retains significance at $K{=}5$ (4/12), whereas under $K_{\mathrm{eff}}$ it drops to 2/12. The predictor shift---co-determination at $K{=}3$ transitioning to diversity dominance at $K{\geq}5$---is thus specific to $K_{\mathrm{eff}}$'s MI-based formulation, which captures effective judge independence rather than pairwise label agreement.
390	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a239750-f893-4898-89b4-7fe5c023c6cf",
  "isSidechain": true,
  "promptId": "4f56398c-daec-492b-b598-2d686c53cd24",
  "agentId": "a2bfd38fb2f2154cb",
  "type": "user",
  "uuid": "dba705e3-e1ec-407b-9c09-28e6a8281f52",
  "sourceToolAssistantUUID": "3a239750-f893-4898-89b4-7fe5c023c6cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/director_a20165af",
  "sessionId": "c9dbaca8-1cd1-415f-aa7b-2e5963ce8650",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-24T10:36:31.582Z_

Here is the full content of the appendix.tex file:

The file contains 8 main appendix sections:

1. **Proof of Theorem (lines 3-10)**: Mathematical proof of monotonicity regarding panel failure rates when replacing a judge with a more vulnerable one.

2. **Robustness Correction Methods (lines 12-22)**: Details on three statistical corrections applied to handle correlated residuals from 455 panels constructed from 15 shared judges:
   - Clustered Standard Errors (CR1 bias-corrected sandwich estimators)
   - Mixed Effects models with random intercepts
   - Wild Cluster Bootstrap with Rademacher weights

3. **Extended Analysis - BFT Reversal Mechanism (lines 23-38)**: Detailed evidence showing how effective judge independence (K_eff) relates to panel error rates, including discussion of corrected data and GAM bootstrap results.

4. **Diversity-Capability Tradeoff (lines 40-52)**: Analysis of the 0.70-0.81 correlation between K_eff and η_max, explaining structural constraints in the current LLM ecosystem.

5. **Aggregation Mechanism Details (lines 54-108)**: Examination of different aggregation methods (majority, weighted, threshold, Bayesian) across panel sizes K=3, K=5, and K=7, with regression tables showing how these methods affect predictor significance.

6. **Panel Selection Strategy Comparison (lines 117-127)**: Comparison showing that min(η_max) selection strategy outperforms diversity-maximizing approaches.

7. **Clustered Standard Error Analysis (lines 129-132)**: Forest plot analysis of robustness across inference methods.

8. **Robustness Checks (lines 134-290)**: Extensive appendix sections including:
   - Subsampling and specification tests
   - Random subsample analysis
   - Attacked K_eff stability verification
   - Cinelli-Hazlett sensitivity analysis (with detailed tables)
   - Cross-benchmark prediction robustness
   - Pool A sensitivity analysis
   - Epsilon sensitivity analysis
   - Temperature sensitivity pilot
   - K_eff distribution statistics
   - Power analysis across panel sizes
   - Alternative diversity measures comparison
   - κ-diversity predictor shift comparison

The appendix is highly technical, containing multiple tables with regression results, sensitivity analyses, and statistical validation of the paper's main findings regarding panel vulnerability to adversarial attacks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dba705e3-e1ec-407b-9c09-28e6a8281f52",
  "isSidechain": true,
  "agentId": "a2bfd38fb2f2154cb",
  "requestId": "req_011CbMFFjrY15uACUuxvuNa7",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "efdbf47e-44f4-4813-ba7b-25bbdf93d310",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/director_a20165af",
  "sessionId": "c9dbaca8-1cd1-415f-aa7b-2e5963ce8650",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01X5fCzxZQopiy161RNQvQ26",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 13661,
      "cache_read_input_tokens": 40795,
      "output_tokens": 565,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13661
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 565,
          "cache_read_input_tokens": 40795,
          "cache_creation_input_tokens": 13661,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13661,
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
