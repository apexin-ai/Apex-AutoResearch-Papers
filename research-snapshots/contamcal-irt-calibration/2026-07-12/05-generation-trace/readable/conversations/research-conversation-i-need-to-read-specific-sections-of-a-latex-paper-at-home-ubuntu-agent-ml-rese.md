# Research conversation: I need to read specific sections of a LaTeX paper at /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a567180dd5dedd4dc.jsonl`
- **Structured JSON:** [`72fbc528ef1a742c2e6e.json`](../../sessions/72/72fbc528ef1a742c2e6e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

49 recorded events

### User

_source line 1 · 2026-05-21T17:22:14.557Z_

I need to read specific sections of a LaTeX paper at /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/

Find and read the following content:
1. The IRT model formulation (likely in method.tex) - specifically the 2PL+γ equation, what J represents, and the prior specifications
2. Appendix K (prior sensitivity analysis) - the exact text about "95% CI excludes zero" and the lower/upper bounds
3. Appendix F (identifiability simulation) - the claims about J≥50 vs J=16
4. The AUGMENT mode description in experimental_setup.tex - what happens to total training size at each dosage
5. Section 5.5 (calibration quality) - what J=16 refers to exactly

Report the exact text verbatim for each section. Search breadth: medium.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "27fa6281-7801-4dec-a217-a595ec352dff",
  "agentId": "a567180dd5dedd4dc",
  "type": "user",
  "uuid": "ac394d6e-ad8c-4112-873d-c91ff853f852",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-21T17:22:16.089Z_

I'll help you find and read these specific sections from the LaTeX paper. Let me start by exploring the directory structure and locating the relevant files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac394d6e-ad8c-4112-873d-c91ff853f852",
  "isSidechain": true,
  "agentId": "a567180dd5dedd4dc",
  "requestId": "req_011CbG6n3KHSHouQz9DJdMQH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a99df318-1e36-4f33-9b4f-5e5603871b2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DiGCY5ACqUzxkdDHX3zVeJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18452,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18452,
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

_source line 3 · 2026-05-21T17:22:16.255Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01HBzf8TzmfDuZLoCy8texew`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper -type f -name \"*.tex\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a99df318-1e36-4f33-9b4f-5e5603871b2c",
  "isSidechain": true,
  "agentId": "a567180dd5dedd4dc",
  "requestId": "req_011CbG6n3KHSHouQz9DJdMQH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c129f33c-e2b0-4818-8dab-04edc096377a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DiGCY5ACqUzxkdDHX3zVeJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18452,
      "cache_read_input_tokens": 0,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18452
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 132,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 18452,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18452,
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

_source line 4 · 2026-05-21T17:22:16.424Z_

<details><summary>↩ Tool result · `toolu_01HBzf8TzmfDuZLoCy8texew`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c129f33c-e2b0-4818-8dab-04edc096377a",
  "isSidechain": true,
  "promptId": "27fa6281-7801-4dec-a217-a595ec352dff",
  "agentId": "a567180dd5dedd4dc",
  "type": "user",
  "uuid": "bda41d52-d8e5-4887-b3b3-15a64781f3e9",
  "sourceToolAssistantUUID": "c129f33c-e2b0-4818-8dab-04edc096377a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-21T17:22:18.690Z_

Good! Now let me read the method.tex file for the IRT model formulation, and start searching for the specific sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bda41d52-d8e5-4887-b3b3-15a64781f3e9",
  "isSidechain": true,
  "agentId": "a567180dd5dedd4dc",
  "requestId": "req_011CbG6nBF2jHXfvMiWykCus",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9c13d9f9-972a-48c5-bc5a-018b51b9b44a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015xwgdF6Dp2X8vyfkK8AZ89",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1422,
      "cache_read_input_tokens": 18452,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1422,
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

_source line 6 · 2026-05-21T17:22:18.818Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QXD5YGZLSiTefpRQBsMmk2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c13d9f9-972a-48c5-bc5a-018b51b9b44a",
  "isSidechain": true,
  "agentId": "a567180dd5dedd4dc",
  "requestId": "req_011CbG6nBF2jHXfvMiWykCus",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bfaf71e7-fae4-43f3-89e4-738f9ee8a21d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015xwgdF6Dp2X8vyfkK8AZ89",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1422,
      "cache_read_input_tokens": 18452,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1422
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 119,
          "cache_read_input_tokens": 18452,
          "cache_creation_input_tokens": 1422,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1422,
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

_source line 7 · 2026-05-21T17:22:18.823Z_

<details><summary>↩ Tool result · `toolu_01QXD5YGZLSiTefpRQBsMmk2`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	ContamCal operates in two stages: Stage~1 estimates per-item contamination exposure from multiple detection signals via training-free fusion; Stage~2 embeds these scores in a contamination-augmented IRT model to produce calibrated ability estimates with credible intervals.
5	
6	\subsection{Problem Formulation}
7	\label{sec:formulation}
8	
9	Let $y_{ijk} \in \{0,1\}$ denote the binary response of model~$j$ ($j=1,\ldots,J$) to item~$i$ ($i=1,\ldots,I_k$) on benchmark~$k$. Standard IRT assumes $P(y_{ijk}=1) = f(\theta_j, \boldsymbol{\xi}_i)$ where $\theta_j$ is latent ability and $\boldsymbol{\xi}_i$ collects item parameters. When training corpora contain benchmark items, the observed ability $\hat{\theta}_j$ confounds genuine capability with memorization.
10	
11	Our goal is to estimate $\theta_j^{\text{clean}}$, the ability each model would exhibit absent contamination, and to diagnose contamination effects at domain granularity. We adapt item compromise IRT \citep{eckerly_2017_item_compromise,sinharay_2017_preknowledge} and explanatory IRT \citep{deboeck_2004_explanatory_irt} for LLM evaluation: replacing binary leakage indicators with continuous exposure scores $e_{ij} \in [0,1]$, fitting per-benchmark models to handle the shared item pool \citep{sanmartin_2009_irt}, and recovering clean ability via counterfactual inference (setting $e_{ij}=0$).
12	
13	\subsection{Stage 1: Multi-Signal Exposure Mapping}
14	\label{sec:stage1}
15	
16	For each model~$j$ and item~$i$, we consider four candidate detection signals. \textbf{S1}~(Embedding similarity): cosine similarity between the item embedding and its nearest neighbor in the SFT training corpus. \textbf{S2}~(Min-K\%++): a membership inference statistic based on token-level surprisal \citep{zhang_2024_minkpp}. \textbf{S3}~(ConStat): the accuracy gap between original and paraphrased item variants \citep{dekoninck2024constat}. \textbf{S4}~(Self-Critique): negative entropy of model self-evaluation distributions, inspired by the finding that LLMs can assess their own knowledge \citep{kadavath2022}; concurrent work by \citet{tao2025detecting} uses a related but mechanistically distinct entropy collapse approach targeting RL-trained models. S3 requires paired paraphrased items as reference and is therefore limited to benchmarks with existing paraphrase sets. Our primary pipeline uses the remaining three signals ($\mathcal{S} = \{\text{S1, S2, S4}\}$) and is applicable to any benchmark without auxiliary data requirements. S2 and S4 exhibit known failure modes under RL post-training, which we characterize in \S\ref{sec:signal_failure}. Item-level classification performance of the exposure scores is reported in Appendix~\ref{sec:sij_classification}.
17	
18	We aggregate signals via Reciprocal Rank Fusion \citep[RRF;][]{cormack_2009_rrf}:
19	\begin{equation}
20	\label{eq:rrf}
21	    e_{ij} = \sum_{s \in \mathcal{S}} \frac{1}{\kappa + r_{s}(i)},
22	\end{equation}
23	where $r_s(i)$ is the rank of item~$i$ under signal~$s$ (rank~1 = most suspicious), $\kappa=60$ is the standard smoothing constant, and $|\mathcal{S}|=3$ in our primary configuration. Raw scores are min-max normalized per model to obtain $e_{ij} \in [0,1]$. The resulting distribution is highly right-skewed (mean 0.041, median 0.016, max 0.879), with most model-item pairs receiving near-zero exposure.
24	
25	\subsection{Stage 2: Contamination-Augmented IRT}
26	\label{sec:stage2}
27	
28	\paragraph{Primary model: 2PL+$\gamma$.}
29	Our primary specification augments the two-parameter logistic (2PL) model \citep{lord_1980_irt,hambleton_1991_irt} with a contamination covariate. We fit independent IRT models per benchmark~$k$, each with its own contamination effect $\gamma_k$. Per-benchmark fitting avoids cross-benchmark item parameter borrowing while permitting heterogeneous contamination effects. For benchmark~$k$, the response probability is:
30	\begin{equation}
31	\label{eq:2pl_gamma}
32	    P(y_{ijk} = 1) = \sigma\!\bigl(a_i(\theta_j - b_i) + \gamma_k \cdot e_{ij}\bigr),
33	\end{equation}
34	where $\sigma(\cdot)$ is the logistic function, $a_i > 0$ is item discrimination, $b_i \in \mathbb{R}$ is item difficulty, $\theta_j$ is model ability, and $\gamma_k$ is the scalar contamination effect for benchmark~$k$. Each benchmark is fitted independently; when finer-grained diagnosis is needed, we replace $\gamma_k$ with per-domain effects $\gamma_d$ ($d=1,\ldots,D$), fitting Eq.~\eqref{eq:2pl_gamma} separately for each cognitive domain within a benchmark (\S\ref{sec:domain_differential}).
35	
36	The additive structure admits a natural interpretation: contamination shifts the effective difficulty of item~$i$ by $\gamma_k \cdot e_{ij} / a_i$ units on the ability scale (this holds exactly under linearization of the logistic function; the true shift is nonlinear and probability-dependent).
37	
38	For MC-format benchmarks, a 4PL extension adds guessing and ceiling asymptotes (Appendix~\ref{sec:4pl_details}); this requires $J \geq 16$ and is not used in domain-level analyses ($J = 13$).
39	
40	\paragraph{Inference.}
41	We perform Bayesian inference via NUTS \citep{hoffman2014} in Stan \citep{carpenter2017} with four chains and target acceptance 0.95. Priors: $\theta_j \sim \mathcal{N}(0,1)$, $a_i \sim \text{LogNormal}(0, 0.5)$, $b_i \sim \mathcal{N}(0,1)$, $\gamma_k \sim \mathcal{N}(0,1)$. Convergence requires split-$\hat{R} < 1.01$ and bulk ESS~$> 400$ for all parameters. Model fit is assessed via the posterior predictive $p$-value (PPP), where values near 0.5 indicate adequate fit.
42	
43	\paragraph{Calibrated score.}
44	The decontaminated accuracy for model~$j$ on benchmark~$k$ is the posterior expectation under zero exposure:
45	\begin{equation}
46	\label{eq:calibrated}
47	    \text{Acc}_{j}^{\text{cal}} = \frac{1}{I_k} \sum_{i=1}^{I_k}\, \mathbb{E}_{\boldsymbol{\psi} \sim p(\boldsymbol{\psi} \mid \mathbf{y})} \!\left[\sigma\!\bigl(a_i(\theta_j - b_i)\bigr)\right],
48	\end{equation}
49	with credible intervals from posterior quantiles. In practice, we average $\sigma(a_i(\theta_j - b_i))$ over posterior draws with $e_{ij}=0$; the spread of draws yields the credible interval. Models with noisier exposure signals receive wider intervals by construction.
50	
51	\paragraph{Identifiability.}
52	\label{sec:fisher}
53	\label{sec:value_decomposition}
54	The reliability of $\gamma$ depends on signal AUC and ensemble size $J$; simulation validates that recovery requires AUC$\geq$0.55 with $J \geq 50$ (Appendix~\ref{sec:identifiability_appendix}). Eq.~\eqref{eq:calibrated} depends on $\theta_j$, not $\gamma$ directly, predicting that vanilla 2PL ($\gamma\!=\!0$) achieves comparable calibration to 2PL+$\gamma$, with $\gamma_k$ serving diagnosis rather than calibration (\S\ref{sec:calibration_results}).
55	
56	\subsection{Dose-Response Profile Classification}
57	\label{sec:classification}
58	
59	Independent of the IRT calibration pipeline, we formalize how each model's accuracy trajectory across dosage levels is classified into a canonical dose-response pattern, drawing on the dose-response modeling tradition in pharmacology \citep{hill1910aggregation,ritz2015dose}. Algorithm~\ref{alg:profile-classification} defines a deterministic decision tree over the accuracy vector $\mathbf{a} = (a_0, a_5, a_{25}, a_{50}, a_{100})$, parameterized by a noise threshold $\tau$, severity threshold $\sigma$, saturation ratio $\rho$, and late-gain floor $\lambda$. The three-way top-level split (immune/harm/benefit) is governed by the sign and magnitude of $\Delta = a_{100} - a_0$ relative to $\tau$; within-branch refinements distinguish Collapse from V-recovery (via mid-dosage trough detection); within the benefit branch, gain trajectory shape (monotonic vs.\ saturating) is logged but both map to a single Benefit pattern. A mid-trajectory volatility check ($v^*$) within the immune branch distinguishes true immunity (Phi-4: $v^* = 0.34$pp $\le \tau$) from V-recovery with full endpoint recovery (Qwen-7B seed$=$123: $\Delta \approx 0$ but $v^* = 3.22$pp $> \tau$); recovery extent varies by seed (partial at seed$=$42, full at seed$=$123). All thresholds are explicit and adjustable; a 30-combination grid sweep confirms all families are stable across all $(\tau, \sigma)$ combinations (180/180 model--seed--threshold pairs; Appendix~\ref{sec:classification_sensitivity}).
60	
61	\begin{algorithm}[H]
62	\caption{Dose-Response Profile Classification}
63	\label{alg:profile-classification}
64	\begin{algorithmic}[1]
65	\Require Accuracy vector $\mathbf{a} = (a_{0}, a_{5}, a_{25}, a_{50}, a_{100})$ at dosages $d \in \{0, 5, 25, 50, 100\}\%$
66	\Require Noise threshold $\tau = 2$ pp, severity threshold $\sigma = 5$ pp
67	\Require Saturation ratio $\rho = 0.3$, late-gain floor $\lambda = 0.5$ pp
68	\Ensure Pattern $p \in \{\textsc{Immune}, \textsc{Collapse}, \textsc{V-recovery}, \textsc{Benefit}\}$
69	\State $\Delta \gets a_{100} - a_{0}$ \Comment{end-to-end accuracy shift}
70	\State $m^* \gets \min(a_{5},\, a_{25},\, a_{50})$ \Comment{mid-dosage minimum}
71	\State $v^* \gets \max_{i \in \{5,25,50\}} |a_i - a_0|$ \Comment{max mid-trajectory deviation}
72	\If{$|\Delta| \le \tau$}
73	    \If{$v^* \le \tau$}
74	        \State \Return \textsc{Immune} \Comment{fluctuation within noise band}
75	    \ElsIf{$m^* < a_{0}$ \textbf{and} $m^* < a_{100}$}
76	        \State \Return \textsc{V-recovery} \Comment{V-dip with full endpoint recovery}
77	    \Else
78	        \State \Return \textsc{Immune} \Comment{non-V volatility, endpoint stable}
79	    \EndIf
80	\ElsIf{$\Delta < -\tau$}
81	    \If{$\Delta \le -\sigma$}
82	        \State \Return \textsc{Collapse} \Comment{severe monotonic degradation}
83	    \ElsIf{$m^* < a_{0}$ \textbf{and} $m^* < a_{100}$}
84	        \State \Return \textsc{V-recovery} \Comment{mid-dosage trough with partial recovery}
85	    \Else
86	        \State \Return \textsc{Collapse} \Comment{moderate decline, no V-shape}
87	    \EndIf
88	\Else \Comment{$\Delta > \tau$}
89	    \State $g_1 \gets a_{25} - a_{0}$ \Comment{first-half gain}
90	    \State $g_2 \gets a_{100} - a_{25}$ \Comment{second-half gain}
91	    \State $\ell \gets a_{100} - a_{50}$ \Comment{late gain}
92	    \If{$(g_1 > 0$ \textbf{and} $g_2 < \rho \cdot g_1)$ \textbf{or} $\ell < \lambda$}
93	        \State \Return \textsc{Benefit} \Comment{saturating gain}
94	    \Else
95	        \State \Return \textsc{Benefit} \Comment{sustained gain}
96	    \EndIf
97	\EndIf
98	\end{algorithmic}
99	\end{algorithm}
100	
101	\paragraph{Family-level aggregation.}
102	Algorithm~\ref{alg:profile-classification} classifies individual seed trajectories. Because per-seed shape classification is more seed-sensitive than endpoint direction (\S\ref{sec:cross_seed}), family-level classification uses \emph{direction} as the primary criterion. A family is classified as Immune if (i)~the bootstrap 95\% CI of the cross-seed mean $\Delta$(d100) includes zero \emph{and} (ii)~$|\text{mean}~\Delta| < \tau$ (1\,pp); families where the CI includes zero but $|\text{mean}~\Delta| \geq \tau$ are classified as Borderline, reflecting insufficient evidence for either clear benefit or clear harm. Otherwise, the sign of the mean determines Harm vs.\ Benefit, and the majority per-seed shape classification provides supplementary characterization. For Immune families, sign disagreement across seeds is expected and does not constitute directional inconsistency. This two-level aggregation avoids sensitivity to the per-seed noise threshold $\tau$ and ensures that families with small, sign-inconsistent effects are not assigned a directional pattern. Parametric model selection (Appendix~\ref{sec:parametric_dr}) confirms Algorithm~\ref{alg:profile-classification}'s classifications for extreme effects but lacks power to resolve moderate patterns at $n\!=\!3$ seeds, motivating the per-seed rule-based approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bfaf71e7-fae4-43f3-89e4-738f9ee8a21d",
  "isSidechain": true,
  "promptId": "27fa6281-7801-4dec-a217-a595ec352dff",
  "agentId": "a567180dd5dedd4dc",
  "type": "user",
  "uuid": "e22f9432-d9c7-409a-9025-f9f9b8e39025",
  "sourceToolAssistantUUID": "bfaf71e7-fae4-43f3-89e4-738f9ee8a21d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-21T17:22:20.451Z_

Now let me read the appendix to find Appendix K (prior sensitivity analysis) and Appendix F (identifiability simulation):

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e22f9432-d9c7-409a-9025-f9f9b8e39025",
  "isSidechain": true,
  "agentId": "a567180dd5dedd4dc",
  "requestId": "req_011CbG6nMdrnHuz9RtQTMBhW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "baa571e8-d580-4751-937b-291974f69ac9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CthaPGCCd113RzTzvnZPjP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 4122,
      "cache_read_input_tokens": 19874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4122,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 9 · 2026-05-21T17:22:21.318Z_

<details open><summary>🔧 Tool call — Read · `toolu_0199xQqAtu49xPdd3Ca1mbZU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "baa571e8-d580-4751-937b-291974f69ac9",
  "isSidechain": true,
  "agentId": "a567180dd5dedd4dc",
  "requestId": "req_011CbG6nMdrnHuz9RtQTMBhW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b8fee0b4-8103-49c4-8f8f-c719ccb26fe8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CthaPGCCd113RzTzvnZPjP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 4122,
      "cache_read_input_tokens": 19874,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4122
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 122,
          "cache_read_input_tokens": 19874,
          "cache_creation_input_tokens": 4122,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4122,
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

_source line 10 · 2026-05-21T17:22:22.107Z_

<details><summary>↩ Tool result · `toolu_0199xQqAtu49xPdd3Ca1mbZU`</summary>

```text
1	\appendix
2	
3	\section{Cross-Benchmark Transfer Details}
4	\label{sec:cross_benchmark_details}
5	
6	\begin{table}[h]
7	\centering
8	\caption{Cross-benchmark transfer: MMLU vs.\ GSM8K accuracy change at d100. LLaMA-3.1 shows the strongest asymmetric transfer ($+$16.4pp GSM8K despite MMLU immunity). Gemma-2 excluded due to CoT collapse under MC-format SFT.}
9	\label{tab:gsm8k_transfer}
10	\footnotesize
11	\begin{tabular}{lcccl}
12	\toprule
13	Model & MMLU $\Delta$ & GSM8K $\Delta$ & Range & Transfer \\
14	\midrule
15	Phi-4 14.7B & $\pm$0.5pp & $-$0.5pp & --- & Null \\
16	OLMo-2 7B & $+$3.2pp & $+$2.1pp$^{\S}$ & --- & Consistent \\
17	Qwen-7B & $-$1.8pp & $+$10.1pp & $\pm$0.9 & Reversal \\
18	Qwen-14B & $-$9.4pp & $+$13.1pp & $\pm$7.4 & Reversal$^{\dagger}$ \\
19	LLaMA-3.1 8B & $-$0.7pp & $+$16.4pp$^{\ddagger}$ & --- & Asymmetric \\
20	\bottomrule
21	\multicolumn{5}{l}{\scriptsize $^{\dagger}$d000 baseline seed-sensitive (s42$=$60.8\% vs.\ s123$=$76.7\%); d100 stable ($82\pm0.5$\%).} \\
22	\multicolumn{5}{l}{\scriptsize $^{\S}$Seed$=$42; OLMo-2 GSM8K effect is seed-sensitive (s42: $+$2.1pp vs.\ s0: $+$9.2pp).} \\
23	\multicolumn{5}{l}{\scriptsize $^{\ddagger}$Single seed (s0); MMLU Immune but strongest GSM8K transfer across all families.}
24	\end{tabular}
25	\end{table}
26	
27	\section{ARC-Challenge Cross-Benchmark Analysis}
28	\label{sec:arc_cross_benchmark}
29	
30	ARC-Challenge (25-shot, 1{,}172 items) patterns under s42 are directionally consistent with MMLU for four of five models: OLMo-2 benefits ($+$3.9pp), Qwen-7B ($-$2.9pp) and Qwen-14B ($-$3.4pp) are harmed, Phi-4 remains immune ($+$0.6pp). Gemma-2 achieves $n\!=\!3$ on ARC: s42 exhibits a 16pp oscillation artifact (endpoint $-$1.20pp), s0 shows harm ($-$1.97pp), and s123 shows benefit ($+$2.73pp). The $n\!=\!3$ ARC mean is $-$0.15pp (SD$=$2.41pp; BCa 95\% CI [$-$1.97, $+$1.42]), with cross-seed direction inconsistent ($-$/$-$/$+$). This contrasts with MMLU, where all three seeds show benefit (mean $+$2.38pp, CI [$+$1.49, $+$3.14] excludes zero), making Gemma-2 the clearest example of benchmark-conditional contamination effects. Bootstrap stability is substantially lower than MMLU (OLMo-2: 53.3\%, Gemma-2: 62.7\%) due to the smaller item pool (1{,}172 vs.\ 14{,}042).
31	
32	\paragraph{Cross-seed ARC consistency.}
33	Phi-4 is the strongest anchor with $n\!=\!3$ on both benchmarks: ARC mean $\Delta = +0.66$pp (SD$=$0.18pp; s0 $+$0.51, s42 $+$0.60, s123 $+$0.86; BCa 95\% CI [$+$0.51, $+$0.77]), MMLU mean $\Delta = +0.73$pp---cross-benchmark agreement within 0.07pp. While statistically detectable on ARC (CI excludes zero, unlike MMLU CI [$-$0.17, $+$1.39]), the effect ($+$0.66pp) is too small to meaningfully inflate benchmark scores, consistent with the Immune classification. Qwen-7B achieves $n\!=\!3$ on ARC: mean $\Delta = -2.42$pp (SD$=$0.51pp; s0 $-$1.88, s42 $-$2.90, s123 $-$2.47; BCa 95\% CI [$-$2.90, $-$2.08]), confirming persistent harm. The d005 V-dip severity is seed-dependent ($-$1.8pp vs.\ $-$4.7pp). Qwen-14B achieves $n\!=\!3$ on both benchmarks: MMLU mean $\Delta = -15.7$pp (BCa CI [$-$24.99, $-$10.49]; s0 most extreme at $-$25.0pp due to position bias amplification); ARC mean $\Delta = -5.03$pp (BCa CI [$-$9.38, $-$2.76]). Both CIs exclude zero, confirming Collapse. OLMo-2 achieves $n\!=\!3$ on ARC: mean $\Delta = +3.44$pp (SD$=$0.52pp; s0 $+$3.50, s42 $+$3.92, s123 $+$2.90). Despite being the most seed-sensitive family on MMLU (SD$=$1.9pp), OLMo-2 is remarkably stable on ARC (SD$=$0.52pp)---seed sensitivity is itself benchmark-dependent, likely modulated by item count and difficulty distribution. Using multi-seed MMLU means ($+$1.4pp), direction is consistently positive on both benchmarks, illustrating why cross-benchmark comparisons require multi-seed aggregation (\S\ref{sec:cross_seed}). ARC dose-response trajectories (s123): Qwen-14B 90.4$\to$91.5$\to$89.8$\to$88.7$\to$87.3 (d005 transient spike then monotonic decline, consistent with MMLU s123 shape); Qwen-7B 87.1$\to$82.4$\to$85.2$\to$85.1$\to$84.7 (d005 sharp drop then partial recovery); OLMo-2 76.9$\to$77.2$\to$76.6$\to$79.2$\to$79.8 (monotonic rise).
34	
35	Cross-seed direction on ARC is consistent for 4/5 families: Phi-4 and OLMo-2 positive across three seeds each, Qwen-7B and Qwen-14B negative across three seeds each. Gemma-2 is the exception ($-$/$-$/$+$ across seeds; mean $-$0.15pp). This contrasts with MMLU, where only 2/5 families achieve strict sign consistency (\S\ref{sec:cross_seed}). ARC yields tighter confidence intervals and higher cross-seed consistency than MMLU, likely because its smaller item pool (1{,}172 vs.\ 14{,}042) amplifies the contamination signal---suggesting that benchmark size modulates not only effect magnitude but also statistical detectability.
36	
37	Cross-benchmark direction (MMLU vs.\ ARC) is consistent for 3/5 families (\S\ref{sec:gsm8k_transfer}): Qwen-14B (Harm), Phi-4 (Immune), and OLMo-2 (Benefit). Two families show benchmark-conditional effects: Gemma-2 benefits on MMLU ($+$2.38pp, CI excludes zero) but shows no significant ARC effect ($-$0.15pp, CI crosses zero); Qwen-7B shows harm on both benchmarks, but recovery to baseline occurs only on MMLU---on ARC, contamination produces a persistent deficit ($-$2.4pp mean across three seeds). Effect magnitudes remain benchmark-specific: Qwen-14B suffers $-$5.0pp on ARC compared to $-$15.7pp on MMLU (3.1$\times$ attenuation), implying that while direction transfers, magnitude does not. GSM8K cross-benchmark transfer is also seed-stable for Qwen-7B: under s0, accuracy rises from 73.3\% to 81.2\% ($+$7.9pp, monotonic), consistent with the directional reversal observed under s42 ($+$10.1pp; Table~\ref{tab:gsm8k_transfer}).
38	
39	\begin{figure}[h]
40	\centering
41	\includegraphics[width=\columnwidth]{figures/fig_arc_dose_response.pdf}
42	\caption{ARC-Challenge accuracy vs.\ contamination dosage (25-shot). Patterns are directionally consistent with MMLU (Figure~\ref{fig:dose_response}) for 4/5 models.}
43	\label{fig:dose_response_arc}
44	\end{figure}
45	
46	\section{GSM8K Dose-Response Transfer}
47	\label{sec:gsm8k_dose_response}
48	
49	Table~\ref{tab:gsm8k_dose} reports GSM8K accuracy across contamination dosages for all six families (single seed, s0). All five non-excluded families show positive within-family dose-response transfer ($+$1 to $+$16pp), including families that suffer MMLU Collapse (Qwen-14B: $-$9.4pp MMLU, $+$7.4pp GSM8K) or are MMLU-Immune (LLaMA-3.1: $-$0.7pp MMLU, $+$16.4pp GSM8K---the strongest transfer effect). This directional reversal---MMLU-targeted contamination improving an unrelated open-ended math benchmark---strengthens the global capability modulation interpretation. Within-family dose-response patterns (direction and relative magnitude of $\Delta$) are the primary finding, as all dosage levels for each family use identical evaluation settings.
50	
51	\begin{table}[h]
52	\centering
53	\caption{GSM8K accuracy (\%) across MMLU contamination dosages (seed$=$0). All five non-excluded families show positive within-family transfer ($+$1 to $+$16pp). Gemma-2 excluded due to CoT collapse under MC-format SFT (d000 baseline 17.8\%).}
54	\label{tab:gsm8k_dose}
55	\footnotesize
56	\begin{tabular}{lcccccc}
57	\toprule
58	Family & d000 & d005 & d025 & d050 & d100 & $\Delta$ \\
59	\midrule
60	Phi-4 14.7B & 84.46 & --- & --- & --- & 85.60 & $+$1.14 \\
61	Qwen2.5-14B & 74.98 & 71.19 & 79.30 & 81.05 & 82.41 & $+$7.43 \\
62	Qwen2.5-7B & 73.31 & 78.32 & 78.24 & 79.38 & 81.20 & $+$7.89 \\
63	OLMo-2 7B & 60.58 & --- & --- & --- & 69.75 & $+$9.17$^{\ddagger}$ \\
64	LLaMA-3.1 8B & 38.74 & --- & 52.16 & --- & 55.12 & $+$16.38 \\
65	Gemma-2 9B & 17.82$^{\dagger}$ & --- & --- & --- & --- & --- \\
66	\bottomrule
67	\multicolumn{7}{l}{\scriptsize $^{\dagger}$CoT collapse under MC-format SFT; excluded from analysis.} \\
68	\multicolumn{7}{l}{\scriptsize $^{\ddagger}$Seed-sensitive: s0 $+$9.17pp vs.\ s42 $+$2.1pp (Table~\ref{tab:gsm8k_transfer}).}
69	\end{tabular}
70	\end{table}
71	
72	GSM8K evaluations use \texttt{max\_new\_tokens=256}, which may truncate chain-of-thought reasoning for some models. Absolute accuracy is therefore a lower bound; cross-family comparisons of absolute values should be interpreted with caution. Within-family dose-response patterns (direction and relative magnitude of $\Delta$) are the primary finding, as all dosage levels for each family use identical evaluation settings.
73	
74	\section{Signal Reliability Across Scales}
75	\label{sec:signal_reliability_appendix}
76	
77	\begin{figure}[h]
78	\centering
79	\includegraphics[width=\columnwidth]{figures/fig_signal_heatmap.pdf}
80	\caption{Detection signal AUC across scale, dosage, and signal type. S1 achieves AUC $>0.95$ at all scales; S2 (Min-K\%++) reverses at 0.5B; S4 is near-random below 1.5B.}
81	\label{fig:signal_heatmap}
82	\end{figure}
83	
84	\section{RRF Signal Ablation}
85	\label{sec:rrf_ablation}
86	
87	\paragraph{Signal orthogonality.}
88	Table~\ref{tab:signal_correlation} reports pairwise Spearman rank correlations between detection signals at the item level, averaged across 31 models. All pairwise $|\rho| < 0.06$, confirming that S1, S2, and S4 capture orthogonal aspects of contamination exposure.
89	
90	\begin{table}[h]
91	\centering
92	\caption{Pairwise Spearman $\rho$ between detection signals (item-level, averaged across 31 models). All $|\rho| < 0.06$.}
93	\label{tab:signal_correlation}
94	\footnotesize
95	\begin{tabular}{lccc}
96	\toprule
97	Signal Pair & MMLU & ARC & GSM8K \\
98	\midrule
99	S1--S2 & $-$0.044 & $-$0.019 & $-$0.022 \\
100	S1--S4 & $+$0.038 & $+$0.009 & $+$0.053 \\
101	S2--S4 & $-$0.001 & $+$0.012 & $+$0.007 \\
102	\bottomrule
103	\end{tabular}
104	\end{table}
105	
106	\paragraph{Leave-one-out ablation.}
107	Table~\ref{tab:rrf_ablation} reports the effect of removing each signal from the RRF ensemble. $\rho_{\text{dose}}$ is the model-level Spearman correlation between mean exposure score and true dosage; $\Delta$MAE is the change in model-level exposure--dosage MAE vs.\ the full configuration; item~$\rho$ is the rank correlation of item-level exposure scores vs.\ the full configuration.
108	
109	\begin{table}[h]
110	\centering
111	\caption{Leave-one-signal-out RRF ablation (31 models, $\kappa\!=\!60$).}
112	\label{tab:rrf_ablation}
113	\footnotesize
114	\begin{tabular}{lccc}
115	\toprule
116	Configuration & $\rho_{\text{dose}}$ & $\Delta$MAE & Item $\rho$ \\
117	\midrule
118	\multicolumn{4}{l}{\textit{MMLU}} \\
119	Full (S1+S2+S4) & 0.049 & --- & --- \\
120	Drop S1 & 0.045 & $+$0.066 & 0.782 \\
121	Drop S2 & \textbf{0.471} & $+$0.045 & 0.773 \\
122	Drop S4 & 0.084 & $+$0.079 & 0.786 \\
123	\midrule
124	\multicolumn{4}{l}{\textit{ARC-Challenge}} \\
125	Full (S1+S2+S4) & $-$0.003 & --- & --- \\
126	Drop S1 & $-$0.006 & $-$0.054 & 0.784 \\
127	Drop S2 & 0.029 & $-$0.079 & 0.786 \\
128	Drop S4 & 0.001 & $-$0.004 & 0.784 \\
129	\bottomrule
130	\end{tabular}
131	\end{table}
132	
133	Dropping S2 (Min-K\%++) causes $\rho_{\text{dose}}$ to jump from 0.049 to 0.471 on MMLU, revealing that S2 actively suppresses model-level dosage discrimination. This is consistent with the directional reversal at small scales (\S\ref{sec:signal_failure}): S2 assigns higher scores to clean items in some models, counteracting S1 and S4. Despite this model-level harm, S2 provides unique item-level information (item~$\rho = 0.773$, i.e., ${\sim}$23\% of item rankings change upon removal). Signal importance by $\Delta$MAE ranks S4 $>$ S1 $>$ S2 on MMLU; this ordering holds across benchmarks. The near-zero $\rho_{\text{dose}}$ (0.049 on MMLU, $-$0.003 on ARC) confirms that RRF exposure is an item-level tool: it identifies which items within a model are most likely contaminated, but cannot distinguish dosage levels across models.
134	
135	\section{Identifiability Simulation}
136	\label{sec:identifiability_appendix}
137	
138	\begin{figure}[h]
139	\centering
140	\includegraphics[width=\columnwidth]{figures/fig_identifiability_heatmap.pdf}
141	\caption{$\gamma$ recovery as a function of signal AUC and ensemble size $J$. Bias $<0.05$ and 95\% CI coverage $\geq90\%$ require $J\geq50$ at AUC$=$0.55, but only $J\geq16$ at AUC$\geq$0.90.}
142	\label{fig:identifiability_heatmap}
143	\end{figure}
144	
145	Fisher information $\mathcal{I}(\gamma) \propto \text{Var}(e_{\cdot i})$ collapses when signal AUC is low. At AUC$=$0.55, bias $< 0.05$ and 95\% CI coverage $\geq 90\%$ require $J \geq 50$; at AUC$\geq$0.90 (as S1 achieves in practice), $J = 16$ suffices. CI width scales as $J^{-0.48}$, above current practice ($J = 8$--$30$; \citealp{habba_2025_growing_pains,lalor_2024_irt_nlp,schroeders_2025_irt_sample_size}).
146	
147	\section{4PL Extension}
148	\label{sec:4pl_details}
149	
150	For MC-format benchmarks where guessing and ceiling effects are non-negligible, we extend to:
151	\begin{equation}
152	    P(y_{ijk} = 1) = c_i + (d_i - c_i)\,\sigma\!\bigl(a_i(\theta_j - b_i) + \gamma_k \cdot e_{ij}\bigr),
153	\end{equation}
154	with $c_i \sim \text{Beta}(5,20)$ and $d_i \sim \text{Beta}(20,5)$. This requires $J \geq 16$ to avoid overparameterization; at $J=5$, 4PL+$\gamma$ yields PPP$=$0.000 and MAE degradation from 0.004 to 0.068. Our domain-level analyses use 2PL+$\gamma$ at $J=13$; pooled calibration uses $J=16$.
155	
156	\section{S4 Self-Critique Signal Details}
157	\label{sec:s4_details}
158	
159	S4 prompts the model with ``Is the following answer correct?'' followed by the question and candidate answer. We extract YES/NO logits to compute $P(\text{YES})$, then score each item as the negative entropy of this distribution: $\text{S4}_i = -[-p\log p - (1-p)\log(1-p)]$ where $p = P(\text{YES})$. Scores near zero indicate high confidence (potentially contaminated); large negative values indicate uncertainty.
160	
161	\section{Training Convergence}
162	\label{sec:training_convergence}
163	
164	All SFT configurations converged. Final training loss increases monotonically with dosage (d000: 1.08, d005: 1.08, d025: 1.14, d100: 1.17 averaged across seeds), consistent with distribution shift from benchmark item injection.
165	
166	\section{Model Exclusion Details}
167	\label{sec:exclusion_details}
168	
169	Of the 16 models remaining after 0.5B exclusion, three 3B checkpoints were removed: two had mismatched naming conventions between evaluation and signal extraction stages, and one lacked evaluation results under the unified hyperparameter setting ($\alpha=32$). Additionally, 3B d000 (clean control) checkpoints were excluded because the standardized protocol (LoRA $\alpha=32$, lr$=5\times10^{-5}$) was applied only to dosages d005--d100 at the 3B scale; earlier d000 checkpoints used inconsistent hyperparameters across retraining iterations.
170	
171	\paragraph{Model sets across analyses.}
172	Table~\ref{tab:model_sets} summarizes model compositions. Model sets vary because domain-level runs preceded the 3B retraining (\S\ref{sec:injection}). Core findings ($\gamma$ non-significance, raw accuracy dominance) replicate across $J=13$ and $J=16$ configurations.
173	
174	\begin{table}[h]
175	\centering
176	\caption{Model set composition across analyses.}
177	\label{tab:model_sets}
178	\footnotesize
179	\begin{tabular}{lcll}
180	\toprule
181	Analysis & $J$ & Model Set & Section \\
182	\midrule
183	Pooled baselines & 16 & 8$\times$Qwen-1.5B + 8$\times$Qwen-3B & \S\ref{sec:calibration_results} \\
184	Domain $\gamma$ & 13 & 8$\times$Qwen-1.5B + 5$\times$Qwen-3B & \S\ref{sec:domain_differential} \\
185	Cross-family & 16--28 & varies by benchmark & \S\ref{sec:taxonomy} \\
186	Oracle ablation & 13 & domain whitelist & \S\ref{sec:calibration_results} \\
187	\bottomrule
188	\end{tabular}
189	\end{table}
190	
191	\section{Prior Sensitivity Analysis}
192	\label{sec:prior_sensitivity}
193	
194	To assess the influence of the $\gamma$ prior, we refit the pooled MMLU model ($J=16$, 300 RRF items) under three specifications: $\gamma \sim \mathcal{N}(0, 0.5)$, $\mathcal{N}(0, 1)$ (default), and $\mathcal{N}(0, 2)$. The posterior mean shifts from 0.34 to 0.89 across priors, while the 95\% CI includes zero in all cases (lower bound stable at $\approx -0.4$; upper bound ranges from 1.11 to 2.20). All fits converge ($\hat{R} < 1.01$, ESS $> 3800$, PPP $\in [0.16, 0.25]$). The prior sensitivity confirms that $J=16$ provides insufficient data to override the prior, which reinforces the exploratory status of $\gamma$-based conclusions at current ensemble sizes.
195	
196	For the Social Sciences domain ($J=16$, 2000 items), the directional conclusion is data-dominated rather than prior-dominated:
197	
198	\begin{table}[h]
199	\centering
200	\caption{Social Sciences $\gamma$ prior sensitivity ($J$=16).}
201	\label{tab:socsci_prior}
202	\footnotesize
203	\begin{tabular}{lcccc}
204	\toprule
205	Prior & $\hat{\gamma}$ & 95\% CI & $P(\gamma\!<\!0)$ & PPP \\
206	\midrule
207	$\mathcal{N}(0, 0.5)$ & $-$0.428 & [$-$0.825, $-$0.017] & 97.95\% & 0.242 \\
208	$\mathcal{N}(0, 1)$ & $-$0.497 & [$-$0.943, $-$0.055] & 98.48\% & 0.282 \\
209	$\mathcal{N}(0, 2)$ & $-$0.507 & [$-$0.957, $-$0.077] & 98.92\% & 0.282 \\
210	\bottomrule
211	\end{tabular}
212	\end{table}
213	
214	In contrast to the pooled analysis where $\hat{\gamma}$ shifts 2.6$\times$ across priors, Social Sciences $\hat{\gamma}$ varies only 1.2$\times$ ($-$0.43 to $-$0.51), with $P(\gamma<0) \geq 97.95\%$ in all cases.
215	
216	\section{IRT Ability Separation by Scale}
217	\label{sec:theta_separation}
218	
219	Table~\ref{tab:theta_separation} reports the mean posterior $\theta$ estimates for 1.5B and 3B model groups across all MMLU domains and the pooled analysis. The ability gap $\Delta\theta = \bar{\theta}_{3\text{B}} - \bar{\theta}_{1.5\text{B}}$ is positive and significant (95\% CI excludes zero) for all nine comparisons, which confirms that the IRT model recovers the expected scale-ability ordering.
220	
221	\begin{table}[h]
222	\centering
223	\caption{IRT ability estimates by model scale ($J=13$ Qwen2.5). $\Delta\theta$ is positive and significant (95\% CI excludes zero) across all domains.}
224	\label{tab:theta_separation}
225	\footnotesize
226	\begin{tabular}{lccc}
227	\toprule
228	Domain & $\bar{\theta}_{1.5\text{B}}$ & $\bar{\theta}_{3\text{B}}$ & $\Delta\theta$ [95\% CI] \\
229	\midrule
230	Math & $-$0.532 & 0.119 & 0.651 [0.570, 0.731] \\
231	Science & 0.321 & 0.780 & 0.459 [0.370, 0.546] \\
232	CS/Eng & 0.372 & 0.542 & 0.169 [0.030, 0.304] \\
233	Medical & 0.521 & 1.053 & 0.531 [0.452, 0.609] \\
234	Humanities & 0.228 & 0.496 & 0.268 [0.202, 0.337] \\
235	Social Sci & 0.940 & 1.540 & 0.599 [0.523, 0.675] \\
236	Business/Law & 0.083 & 0.417 & 0.334 [0.261, 0.410] \\
237	Other & 0.817 & 1.565 & 0.748 [0.647, 0.846] \\
238	\midrule
239	Pooled & 0.311 & 0.811 & 0.500 [0.431, 0.568] \\
240	\bottomrule
241	\end{tabular}
242	\end{table}
243	
244	\section{DiD Across Dosage Levels}
245	\label{sec:did_dosage}
246	
247	\begin{figure}[h]
248	\centering
249	\includegraphics[width=\columnwidth]{figures/fig_did_dose_response.pdf}
250	\caption{Difference-in-differences (treated vs.\ untreated items) across contamination dosage levels. DiD remains non-significant at all dosages for all model families, confirming that the global capability modulation mechanism (\S\ref{sec:memorization_test}) is consistent across the full dosage range.}
251	\label{fig:did_dose_response}
252	\end{figure}
253	
254	\section{Post-hoc Power Analysis (MDES)}
255	\label{sec:mdes}
256	
257	Table~\ref{tab:mdes_mmlu} and Table~\ref{tab:mdes_arc} report the minimum detectable effect size (MDES) for the treated vs.\ untreated DiD comparison at d025 (80\% power, $\alpha=0.05$, two-sided). MDES is computed as the effect size detectable given each model's observed variance, the treated/untreated split sizes, and a two-sample $t$-test power calculation. At d100, all benchmark items are treated ($n_{\text{untreated}}=0$), precluding DiD analysis; d025 is reported as the primary dosage level.
258	
259	\begin{table}[h]
260	\centering
261	\caption{Post-hoc MDES for MMLU DiD ($n_{\text{treated}}=3{,}540$, $n_{\text{untreated}}=10{,}502$).}
262	\label{tab:mdes_mmlu}
263	\footnotesize
264	\begin{tabular}{lcc}
265	\toprule
266	Model & DiD (pp) & MDES (pp) \\
267	\midrule
268	Phi-4 14.7B & $-$0.27 & 1.25 \\
269	OLMo-2 7B & $-$1.07 & 1.59 \\
270	Gemma-2 9B & $+$0.55 & 1.74 \\
271	Qwen2.5-7B & $-$0.84 & 2.02 \\
272	Qwen2.5-14B & $+$0.69 & 2.05 \\
273	\bottomrule
274	\end{tabular}
275	\end{table}
276	
277	\begin{table}[h]
278	\centering
279	\caption{Post-hoc MDES for ARC-Challenge DiD ($n_{\text{treated}}=257$, $n_{\text{untreated}}=915$).}
280	\label{tab:mdes_arc}
281	\footnotesize
282	\begin{tabular}{lcc}
283	\toprule
284	Model & DiD (pp) & MDES (pp) \\
285	\midrule
286	Phi-4 14.7B & $-$0.83 & 2.28 \\
287	Qwen2.5-14B & $-$0.26 & 3.47 \\
288	OLMo-2 7B & $-$1.13 & 4.19 \\
289	Gemma-2 9B & $-$0.25 & 4.66 \\
290	Qwen2.5-7B & $+$2.43 & 5.57 \\
291	\bottomrule
292	\end{tabular}
293	\end{table}
294	
295	On MMLU, all observed DiD values are well below their respective MDES, confirming that the null results are consistent with absence of item-specific effects $>$2pp. On ARC, the smaller treated sample ($n=257$) yields substantially higher MDES; in particular, Qwen-7B's MDES of 5.57pp means that even moderate item-specific effects cannot be excluded for this model on ARC. ARC DiD results should therefore be interpreted as inconclusive rather than as evidence against memorization.
296	
297	\section{Dose-Response Details}
298	\label{sec:dose_response_details}
299	
300	The dose-response patterns reported in \S\ref{sec:taxonomy} are measured at the 7B--14.7B scale. Within the Qwen2.5 family at $\leq$3B, effects are considerably smaller: at 1.5B and 3B, MMLU accuracy increases with contamination dosage by ${\sim}$0.6--0.7pp, with diminishing returns above d025. At 0.5B, however, aggregate MMLU accuracy \textit{decreases} with dosage (0.41 at d000 $\to$ 0.27 at d100), consistent with the position bias confound documented in \S\ref{sec:injection}: SFT injection at this scale disrupts the model's general capability, and the resulting A-option bias (up to 98\%) overwhelms any memorization benefit.
301	
302	\section{Sensitivity of Profile Classification}
303	\label{sec:classification_sensitivity}
304	
305	We assess the robustness of Algorithm~\ref{alg:profile-classification} to threshold selection via a grid sweep over 134 $(\tau, \sigma)$ combinations. Table~\ref{tab:sensitivity} reports family-level stability across both a reasonable parameter range ($\tau \in [0.5, 2.0]$~pp $\times$ $\sigma \in [3.0, 7.0]$~pp; 30 combinations) and the full 134-combination sweep, along with the nearest parameter value at which the classification transitions.
306	
307	\begin{table}[h]
308	\centering
309	\caption{Profile classification stability across threshold parameter ranges. All families achieve 100\% stability within the reasonable range; transitions occur only at extreme parameter values ($\geq$3$\times$ default).}
310	\label{tab:sensitivity}
311	\footnotesize
312	\begin{tabular}{lcccc}
313	\toprule
314	Family & Pattern & Reasonable & Full & Nearest transition \\
315	\midrule
316	Qwen2.5-14B & Collapse & 100\% & 100\% & $\tau = 9.4$ \\
317	Gemma-2 9B & Benefit & 100\% & 89\% & $\tau = 3.8$ \\
318	Phi-4 14.7B & Immune & 100\% & 82\% & $\tau < 0.35$ \\
319	OLMo-2 7B & Benefit & 100\% & 82\% & $\tau = 3.25$ \\
320	Qwen2.5-7B & V-recovery & 100\% & 72\% & $\tau = 3.0$ \\
321	\bottomrule
322	\end{tabular}
323	\end{table}
324	
325	Within the reasonable parameter range, all five families achieve 100\% classification stability (150/150 family--parameter combinations). Transitions occur only at extreme $\tau$ values well beyond the default ($\tau\!=\!2$): Qwen-14B requires $\tau\!=\!9.4$ (4.7$\times$ default) to reclassify, reflecting the large separation between its $\Delta\text{acc}$ ($-$9.4pp) and any plausible noise threshold. Qwen-7B is the least robust at $\tau\!=\!3.0$ (1.5$\times$ default), but this is still above any defensible noise threshold for MMLU. The high intrinsic effect-size separation---Phi-4 fluctuates $<$0.4pp while Qwen-14B declines by 9.4pp---means that classification stability is driven by the data rather than by parameter choice.
326	
327	\section{Cross-Family Domain Decomposition}
328	\label{sec:domain_decomposition}
329	
330	We decompose MMLU accuracy changes into four constituent domains (STEM, Humanities, Social Sciences, Other) across all model families at each contamination dosage.
331	
332	Two patterns emerge. First, the direction of accuracy change is governed by the dose-response pattern, not by domain. At d100, Collapse (Qwen-14B) produces negative $\Delta\text{acc}$ in all four domains (STEM $-6.8$pp, Humanities $-10.1$pp, Social Sciences $-11.2$pp, Other $-9.4$pp), while Benefit (Gemma-2) produces positive $\Delta\text{acc}$ throughout ($+2.7$, $+3.9$, $+5.0$, $+3.4$pp). Immune (Phi-4) remains within $\pm 1.0$pp across all domains. No pattern produces a crossover exceeding the noise band ($|\Delta| > 1$pp); the single exception is V-recovery Humanities ($+0.28$pp, well within sampling noise). This consistency holds at intermediate dosages as well.
333	
334	Second, domains differ in sensitivity. STEM is the most resilient (mean $|\Delta\text{acc}| = 2.8$pp across all families at d100). Social Sciences is the most sensitive at $5.1$pp---$1.8\times$ the STEM magnitude. The ordering is stable across patterns: in Collapse, STEM shows the smallest decline; in Benefit, STEM shows the smallest gain.
335	
336	These results reinforce the global capability modulation interpretation (\S\ref{sec:memorization_test}): contamination direction is determined by the model's dose-response pattern rather than domain-specific memorization. The differential domain sensitivity more likely reflects variation in item difficulty distributions than differential memorization rates.
337	
338	\section{Baseline Ability vs.\ Contamination Effect}
339	\label{sec:baseline_vs_effect}
340	
341	\begin{figure}[h]
342	\centering
343	\includegraphics[width=\columnwidth]{figures/fig_baseline_vs_effect.pdf}
344	\caption{Baseline MMLU accuracy (d000) vs.\ maximum accuracy change ($\Delta$acc) under contamination. A threshold between 61.9\% (Gemma-2) and 66.1\% (Qwen-7B) separates models that benefit from contamination (below) from those that are harmed or immune (above). Estimated from models spanning four independent families.}
345	\label{fig:baseline_vs_effect}
346	\end{figure}
347	
348	\section{Per-Domain $\gamma$ Estimates}
349	\label{sec:domain_gamma_table}
350	
351	\begin{figure}[h]
352	\centering
353	\includegraphics[width=\columnwidth]{figures/fig_domain_gamma.pdf}
354	\caption{Per-domain $\gamma_d$ estimates with 95\% CIs ($J$=13 Qwen2.5). STEM domains show positive $\gamma_d$; Social Sciences is negative and survives Bonferroni correction at $J$=16.}
355	\label{fig:domain_gamma}
356	\end{figure}
357	
358	\begin{table}[h]
359	\centering
360	\caption{Per-domain $\gamma$ estimates (2PL+$\gamma$, Qwen2.5) at $J$=13 and $J$=16. All $J$=16 fits converge ($\hat{R} < 1.01$). Social Sciences $P(\gamma\!<\!0)$ strengthens from 99.1\% to 99.7\% at $J$=16, crossing the Bonferroni-corrected threshold of 99.375\% for eight tests. Results remain exploratory at these ensemble sizes \citep{gelman2012why}. ARC-Challenge is excluded (PPP $<$ 0.05 at all $J$).}
361	\label{tab:domain_gamma}
362	\footnotesize
363	\resizebox{\columnwidth}{!}{%
364	\begin{tabular}{lcccccc}
365	\toprule
366	 & \multicolumn{2}{c}{$J$=13} & \multicolumn{4}{c}{$J$=16} \\
367	\cmidrule(lr){2-3} \cmidrule(lr){4-7}
368	Domain & $\gamma$ & $P(\gamma\!<\!0)$ & $\gamma$ & $P(\gamma\!<\!0)$ & PPP & $\hat{R}$ \\
369	\midrule
370	MMLU: Math & +0.50 & 8.1\% & +0.60 & 3.8\% & 0.305 & 1.007 \\
371	MMLU: Science & +0.50 & 7.8\% & +0.57 & 4.3\% & 0.197 & 1.007 \\
372	MMLU: CS/Eng & +0.50 & 14.8\% & +0.32 & 24.0\% & 0.503 & 1.006 \\
373	MMLU: Medical & +0.24 & 24.0\% & +0.05 & 43.6\% & 0.268 & 1.008 \\
374	MMLU: Other & +0.13 & 35.7\% & +0.32 & 20.4\% & 0.072$^\dagger$ & 1.008 \\
375	MMLU: Business/Law & +0.04 & 44.1\% & +0.08 & 37.8\% & 0.395 & 1.007 \\
376	MMLU: Humanities & $-$0.31 & 85.4\% & $-$0.14 & 69.7\% & 0.416 & 1.007 \\
377	MMLU: Social Sci & $-$0.57 & \textbf{99.1\%} & $-$0.63 & \textbf{99.7\%} & 0.722 & 1.006 \\
378	\bottomrule
379	\end{tabular}}
380	
381	\vspace{2pt}
382	{\scriptsize $^\dagger$PPP below acceptable threshold (0.1); $\gamma$ estimate for this domain should be interpreted with caution.}
383	\end{table}
384	
385	\section{DGP Robustness Analysis}
386	\label{sec:threshold_dgp}
387	
388	We evaluate 2PL+$\gamma$ robustness under data-generating process (DGP) misspecification via 400 simulation runs (2 DGPs $\times$ 4 ensemble sizes $\times$ 5 true $\gamma$ values $\times$ 10 seeds).
389	
390	\paragraph{Design.} The \emph{Linear DGP} (control) generates responses from the correctly specified additive model (Eq.~\ref{eq:2pl_gamma}). The \emph{Threshold DGP} (misspecified) applies a step-function contamination effect: items with exposure above a threshold receive the full effect; items below receive zero. Ensemble sizes sweep $J \in \{16, 50, 100, 500\}$; true $\gamma \in \{0.5, 1.0, 1.5, 2.0, 3.0\}$.
391	
392	\paragraph{Point estimates.} Under the Linear DGP, $\hat{\gamma}/\gamma_{\text{true}} = 0.84$--$1.07$ across all conditions (unbiased within sampling noise). Under the Threshold DGP, $\hat{\gamma}/\gamma_{\text{true}} = 0.94$--$1.24$ (mild overestimation, not attenuation). PPP remains in the acceptable range (0.50--0.56) under both DGPs, confirming that posterior predictive checks cannot detect this form of misspecification.
393	
394	\paragraph{CI coverage.} Under the Linear DGP, 95\% CI coverage is nominal ($\geq$0.93) at all $J$. Under the Threshold DGP, coverage degrades with ensemble size (Table~\ref{tab:dgp_coverage}). The intervals become overconfident as $J$ increases because the model converges to a biased point estimate.
395	
396	\begin{table}[h]
397	\centering
398	\caption{95\% CI coverage under Threshold DGP (range across $\gamma$ values).}
399	\label{tab:dgp_coverage}
400	\footnotesize
401	\begin{tabular}{lc}
402	\toprule
403	$J$ & 95\% CI coverage \\
404	\midrule
405	50 & 1.00 \\
406	100 & 0.90--1.00 \\
407	200 & 0.80--1.00 \\
408	500 & 0.70--1.00 \\
409	\bottomrule
410	\end{tabular}
411	\end{table}
412	
413	\paragraph{Implications.} The reasoning chain is: (i)~Threshold DGP + linear model yields $\hat{\gamma}/\gamma_{\text{true}} \geq 0.94$ (overestimation, not attenuation); (ii)~therefore, if a true threshold effect exists, the linear model will not fail to detect it; (iii)~an empirical $\gamma \approx 0$ is a genuine null, not a misspecification artifact. Coverage degradation affects the \emph{precision} of effect size estimates (how narrow the CI is), not the \emph{detection} of whether an effect exists. At the ensemble sizes in our empirical analyses ($J\!=\!13$--$16$), coverage remains near-nominal even under misspecification. Real RRF exposure is right-skewed (mean$=$0.041); the simulation uses uniform exposure, so quantitative magnitudes may differ, but the qualitative pattern (overestimation direction, coverage degradation at large $J$) is robust.
414	
415	\section{ARC IRT Results}
416	\label{sec:arc_irt}
417	
418	ARC-Challenge IRT results are reported separately due to marginal model fit (PPP$=$0.003 at $J=16$). The smaller item pool (1,172 vs.\ 14,042 for MMLU) and more homogeneous difficulty distribution contribute to structural misfit: the 2PL+$\gamma$ model cannot adequately capture the item response patterns. Under this caveat, the ARC baseline comparison ($J=16$, 300 RRF items) yields: B0-Raw MAE$=$0.007, B3-Vanilla2PL MAE$=$0.015, B4-LinearRegression MAE$=$0.012 ($\tau = 0.731$, best rank correlation), B6-DCR MAE$=$0.314 (systematic overcorrection), ContamCal MAE$=$0.020. The pattern mirrors MMLU: raw accuracy dominates on MAE because the aggregate contamination effect (${\sim}$0.7pp) is smaller than correction noise. Domain-level $\gamma$ estimation on ARC is unreliable at all tested configurations ($J=8$, 13, 16; PPP $< 0.05$ in all cases).
419	
420	\section{Full Baseline Comparison}
421	\label{sec:full_baselines}
422	
423	Table~\ref{tab:baselines} (main text) reports B0, B3, and ContamCal under the Qwen2.5 pooled configuration ($J=16$ for MMLU/ARC, $J=24$ for GSM8K which retains 0.5B). Table~\ref{tab:full_baselines_arc} presents the complete seven-baseline comparison on ARC under a pooled 0.5B+1.5B configuration ($J=8$, S1-only exposure). This configuration differs from the main analysis ($J=16$, RRF exposure): the smaller ensemble and single-signal exposure limit comparability with MMLU results; these results are included for completeness. Table~\ref{tab:full_baselines_gsm8k} presents GSM8K baselines at 0.5B scale.
424	
425	B6-DCR \citep{xu2025dcr} produces the highest MAE on both benchmarks, consistent with its fuzzy inference approach, which overcorrects scores without a measurement-theoretic anchor. B4-LinearRegression performs competitively on ARC (MAE$=$0.056) but lacks the uncertainty quantification and domain-level diagnosis that IRT provides. B1-Remove\&Rescore and B5-Emperor do not improve over raw scores, which confirms that item removal and mitigation strategies are insufficient for calibration.
426	
427	\begin{table}[h]
428	\centering
429	\caption{Full baseline comparison on ARC-Challenge (pooled 0.5B+1.5B, $J=8$, S1-only exposure). MAE$\downarrow$.}
430	\label{tab:full_baselines_arc}
431	\footnotesize
432	\begin{tabular}{lc}
433	\toprule
434	Method & ARC MAE \\
435	\midrule
436	B0-Raw & 0.059 \\
437	B1-Remove\&Rescore & 0.059 \\
438	B2-Single2PL+$\gamma$ & 0.064 \\
439	B3-Vanilla4PL & 0.071 \\
440	B4-LinearRegression & 0.056 \\
441	B5-Emperor & 0.059 \\
442	B6-DCR & --- \\
443	\midrule
444	ContamCal (4PL+$\gamma$) & \textbf{0.035} \\
445	\bottomrule
446	\end{tabular}
447	\end{table}
448	
449	\begin{table}[h]
450	\centering
451	\caption{Baseline comparison on GSM8K (0.5B scale, delta exposure). MAE$\downarrow$.}
452	\label{tab:full_baselines_gsm8k}
453	\footnotesize
454	\begin{tabular}{lc}
455	\toprule
456	Method & GSM8K MAE \\
457	\midrule
458	B0-Raw & 0.003 \\
459	B2-Single2PL+$\gamma$ & 0.320 \\
460	B3-Vanilla4PL & 0.012 \\
461	B4-LinearRegression & \textbf{0.003} \\
462	B6-DCR & --- \\
463	\midrule
464	ContamCal (4PL+$\gamma$) & 0.020 \\
465	\bottomrule
466	\end{tabular}
467	\end{table}
468	
469	\section{Parametric Dose-Response Model Comparison}
470	\label{sec:parametric_dr}
471	
472	We fit four parametric dose-response models---Constant (intercept-only), Linear, Quadratic, and four-parameter Hill \citep{hill1910aggregation,ritz2015dose}---to pooled multi-seed MMLU accuracy trajectories for each family. Table~\ref{tab:aicc_dr} reports AICc and Akaike weights.
473	
474	\begin{table}[h]
475	\centering
476	\caption{AICc model selection for dose-response trajectories (pooled multi-seed MMLU). Bold indicates best-fitting model per family; $w$ is the Akaike weight of the best model.}
477	\label{tab:aicc_dr}
478	\footnotesize
479	\begin{tabular}{lccccc}
480	\toprule
481	Family & Constant & Linear & Quadratic & Hill & Best ($w$) \\
482	\midrule
483	Phi-4 14.7B & $-$71.42 & $-$72.08 & $-$70.06 & $\mathbf{-73.14}$ & Hill (0.58) \\
484	Qwen2.5-14B & 49.54 & 23.40 & 21.22 & $\mathbf{18.28}$ & Hill (0.55) \\
485	Qwen2.5-7B & $-$12.38 & $-$20.53 & $-$14.52 & $\mathbf{-24.97}$ & Hill (0.77) \\
486	Gemma-2 9B & $\mathbf{17.35}$ & 18.89 & 20.01 & 18.96 & Constant (0.39) \\
487	OLMo-2 7B & $\mathbf{25.82}$ & 26.66 & 27.54 & 26.47 & Constant (0.62) \\
488	\bottomrule
489	\end{tabular}
490	\end{table}
491	
492	Parametric model selection with pooled multi-seed data recovers only the most extreme pattern (Collapse, Qwen-14B; Hill $E_{\max} = -43$pp). Two families classified as Benefit by Algorithm~\ref{alg:profile-classification} (Gemma-2, OLMo-2) are indistinguishable from Constant under AICc---consistent with their cross-seed CIs crossing zero (Table~\ref{tab:cross_seed}). Qwen-7B's V-recovery is structurally inaccessible to monotonic Hill/sigmoid models; Quadratic captures the V-shape but is penalized by AICc ($\Delta$AICc$=$6.4). Phi-4's Immune classification is reclassified as weak Benefit (Hill $E_{\max} = +2.43$pp, CI [$-$2.01, $+$6.88] crossing zero). These discrepancies reflect insufficient statistical power at $n\!=\!3$ seeds rather than contradictions: Algorithm~\ref{alg:profile-classification} resolves per-seed patterns below the detection threshold of pooled parametric methods, motivating its use for taxonomy construction.
493	
494	\section{Exposure Score Item-Level Classification}
495	\label{sec:sij_classification}
496	
497	Under controlled injection where ground-truth contamination labels are available, we evaluate item-level classification performance of each detection signal and the RRF fusion (\S\ref{sec:stage1}). S1 (embedding similarity) achieves near-perfect discrimination (ROC-AUC 0.93--0.99 across benchmarks and dosage levels), confirming that cosine similarity to the training corpus reliably identifies injected items. RRF fusion achieves ROC-AUC 0.73--0.93, reduced relative to S1 because S2 (Min-K\%++, AUC $\approx$ 0.48--0.50) and S4 (Self-Critique, AUC $\approx$ 0.47--0.51) contribute near-random item-level signal. However, RRF is designed for the realistic setting where ground truth is unavailable: S1 requires an explicit training corpus reference, which practitioners typically lack, while RRF's multi-signal approach provides robustness across detection scenarios where no single signal dominates (\S\ref{sec:rrf_ablation}).
498	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b8fee0b4-8103-49c4-8f8f-c719ccb26fe8",
  "isSidechain": true,
  "promptId": "27fa6281-7801-4dec-a217-a595ec352dff",
  "agentId": "a567180dd5dedd4dc",
  "type": "user",
  "uuid": "015ea7f5-1c53-41d9-9c45-5c62d44cc03e",
  "sourceToolAssistantUUID": "b8fee0b4-8103-49c4-8f8f-c719ccb26fe8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-21T17:22:24.389Z_

Great! I found several sections. Now let me search for the experimental_setup.tex file to find the AUGMENT mode description, and let me also look for Section 5.5 (calibration quality) which might be in results.tex:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "015ea7f5-1c53-41d9-9c45-5c62d44cc03e",
  "isSidechain": true,
  "agentId": "a567180dd5dedd4dc",
  "requestId": "req_011CbG6nbYXTQzHgsK1zpF8G",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d56f5352-9866-44ce-82f1-a61a57fc3550",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VC5rBBsbF4gfyrUH6BPVmB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 14831,
      "cache_read_input_tokens": 23996,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14831,
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

_source line 12 · 2026-05-21T17:22:25.423Z_

<details open><summary>🔧 Tool call — Read · `toolu_012DU6h7hnqFyNAjF8t8C8XE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d56f5352-9866-44ce-82f1-a61a57fc3550",
  "isSidechain": true,
  "agentId": "a567180dd5dedd4dc",
  "requestId": "req_011CbG6nbYXTQzHgsK1zpF8G",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ebaa0dc8-13d2-449e-a380-4004a1d5baf4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VC5rBBsbF4gfyrUH6BPVmB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 14831,
      "cache_read_input_tokens": 23996,
      "output_tokens": 221,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14831
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 221,
          "cache_read_input_tokens": 23996,
          "cache_creation_input_tokens": 14831,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14831,
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

### Tool call

_source line 13 · 2026-05-21T17:22:25.427Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PuoQvm1RPfEVXkyYzv2rCX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebaa0dc8-13d2-449e-a380-4004a1d5baf4",
  "isSidechain": true,
  "agentId": "a567180dd5dedd4dc",
  "requestId": "req_011CbG6nbYXTQzHgsK1zpF8G",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2db65cda-8135-4e55-9641-7c0854a3b2f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VC5rBBsbF4gfyrUH6BPVmB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 14831,
      "cache_read_input_tokens": 23996,
      "output_tokens": 221,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14831
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 221,
          "cache_read_input_tokens": 23996,
          "cache_creation_input_tokens": 14831,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14831,
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

_source line 14 · 2026-05-21T17:22:25.440Z_

<details><summary>↩ Tool result · `toolu_01PuoQvm1RPfEVXkyYzv2rCX`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	Cross-family results (\S\ref{sec:taxonomy}) use seed$=$42 data across five models from four independent families. Within-family IRT analyses (\S\ref{sec:calibration_results}--\ref{sec:domain_differential}) use $J=16$ Qwen2.5 models (8$\times$1.5B + 8$\times$3B); domain-level contamination estimates $\gamma_d$ (\S\ref{sec:domain_differential}) are reported at $J=16$ in the text and $J=13$ in Figure~\ref{fig:domain_gamma}.
5	
6	\subsection{Dose-Response Patterns}
7	\label{sec:taxonomy}
8	
9	\begin{table}[t]
10	\centering
11	\caption{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\Delta$acc: d000$\to$d100 change (95\% CI from item-level paired bootstrap, $B=10{,}000$). Stab.: bootstrap classification stability. Classifications are robust to threshold hyperparameter choice (5/5 families at 100\% stability across 30 reasonable $(\tau,\sigma)$ combinations; Appendix~\ref{sec:classification_sensitivity}).}
12	\label{tab:taxonomy}
13	\footnotesize
14	\begin{tabular}{llccccc}
15	\toprule
16	Pattern & Model & Baseline & $\Delta$acc & 95\% CI & Peak & Stab. \\
17	\midrule
18	Immune & Phi-4 14.7B & 76.4\% & $\pm$0.5pp & [$-$0.60, $+$0.26] & negl. & 100\% \\
19	Collapse & Qwen-14B & 69.4\% & $-$9.4 to $-$12.7pp & [$-$12.74, $-$9.0] & --- & 100\% \\
20	V-recovery & Qwen-7B & 66.1\% & $-$1.8pp & [$-$2.36, $-$1.22] & $-$3.1\textsuperscript{d025} & 99.6\% \\
21	Benefit & Gemma-2 9B & 61.9\% & $+$3.8pp & [$+$3.18, $+$4.33] & mono. & 76.6\% \\
22	Benefit & OLMo-2 7B & 53.8\% & $+$3.2pp\textsuperscript{$\dagger$} & [$+$2.73, $+$3.71] & sat.\textsuperscript{d050} & 100\% \\
23	\bottomrule
24	\multicolumn{7}{l}{\scriptsize $^{\dagger}$Seed-sensitive: s42 $+$3.2pp, s123 $-$0.6pp, s0 $+$1.4pp; cross-seed CI crosses zero. See \S\ref{sec:cross_seed}.}
25	\end{tabular}
26	\end{table}
27	
28	Applying Algorithm~\ref{alg:profile-classification} to seed$=$42 accuracy trajectories yields qualitatively different dose-response patterns (Table~\ref{tab:taxonomy}, Figure~\ref{fig:dose_response}), not a uniform inflation effect. This empirical taxonomy is preliminary at $N\!=\!5$ families.
29	
30	\paragraph{Baseline ability gradient.}
31	In our five-family sample, contamination vulnerability concentrates in the 65--70\% MMLU baseline band; models at extreme baselines show limited sensitivity. Below 62\%, OLMo-2 (53.8\%) gains $+$3.2pp (saturating at d050) and Gemma-2 (61.9\%) gains $+$3.8pp monotonically. In the vulnerable band, Qwen-7B (66.1\%) shows V-shaped harm-then-recovery across seeds (trough at d025 for seed$=$42, d005 for seed$=$123; recovery extent varies from partial to full), and Qwen-14B (69.4\%) collapses by $-$9.4 to $-$25.0pp across seeds (mean $-$15.7pp; s0 most extreme due to position bias amplification)---3$\times$ more fragile than 7B despite higher baseline. Above 76\%, Phi-4 (76.4\%) is immune. ARC-Challenge direction is consistent for 3/5 families; full results in Appendix~\ref{sec:arc_cross_benchmark}. STEM is the most resilient domain across all families (Appendix~\ref{sec:domain_decomposition}).
32	
33	\paragraph{Out-of-sample validation.}
34	To assess whether the taxonomy generalizes beyond the four construction families, we evaluate LLaMA-3.1-8B (Meta) at three dosage levels (d000, d025, d100). LLaMA-3.1-8B exhibits Immune on both MMLU (53.50\%$\to$52.75\%$\to$52.81\%, $\Delta$$=$$-$0.69pp) and ARC (72.61\%$\to$72.01\%$\to$72.70\%, $\Delta$$=$$+$0.09pp). Algorithm~\ref{alg:profile-classification} assigns Immune, consistent with Phi-4. Notably, LLaMA-3.1's MMLU baseline (53.5\%) nearly matches OLMo-2 (53.8\%), yet OLMo-2 is Benefit---demonstrating that family-level factors beyond baseline ability modulate contamination vulnerability. Two of four patterns (Immune, Benefit) are attested in $\geq$2 independent families; Collapse and V-recovery are each observed in one family across all three seeds, and require additional family-level replication. On GSM8K, LLaMA-3.1 shows the strongest positive transfer across all families ($+$16.4pp; Appendix~\ref{sec:gsm8k_dose_response}), demonstrating that target-benchmark immunity does not imply transfer immunity.
35	
36	\subsection{Cross-Benchmark Transfer}
37	\label{sec:gsm8k_transfer}
38	
39	We evaluate contaminated checkpoints on GSM8K \citep{cobbe2021gsm8k} (1{,}319 open-ended math problems) and ARC-Challenge. Table~\ref{tab:gsm8k_transfer} (Appendix) reveals three GSM8K transfer patterns: \textbf{directional reversal}---Qwen-7B loses $-$1.8pp on MMLU but gains $+$10.1pp on GSM8K (stable across seeds, range 1.9pp), demonstrating benchmark-conditional effects; \textbf{null transfer} (Phi-4, $-$0.5pp), confirming immunity generalizes across formats; and \textbf{consistent positive} transfer (OLMo-2, $+$2.1pp). Gemma-2 is excluded due to CoT collapse (d000 baseline 17.8\%; \S\ref{sec:benchmarks}). All five non-excluded families show positive GSM8K transfer ($+$1 to $+$16pp; Appendix~\ref{sec:gsm8k_dose_response}), even those suffering MMLU Collapse (Qwen-14B: $-$9.4pp MMLU but $+$7.4pp GSM8K), though absolute magnitudes should be interpreted cautiously due to evaluation configuration differences (\S\ref{sec:gsm8k_dose_response}). Volume confounds (${\sim}$33\% more steps at d100) are mitigated by three observations: d005 ($+$1.5\% data) already yields substantial Qwen-7B gains; Phi-4 shows zero transfer despite identical volume; OLMo-2's gain is seed-sensitive ($+$2.1pp at s42; $+$9.2pp at s0). Using multi-seed means, cross-benchmark direction (MMLU vs.\ ARC) is consistent for 3/5 families; two show benchmark-conditional effects (Appendix~\ref{sec:arc_cross_benchmark}).
40	
41	\subsection{Cross-Seed Stability}
42	\label{sec:cross_seed}
43	
44	With $n\!=\!3$ seeds per family, cross-seed CIs have limited precision (widths 1.5--14.5pp). Classification therefore relies on direction consistency, cross-benchmark replication, and shape stability; CIs are reported for transparency. Table~\ref{tab:cross_seed} reports per-seed $\Delta\text{acc}$(d100).
45	
46	\begin{table}[t]
47	\centering
48	\caption{Cross-seed $\Delta$acc (d000$\to$d100). Strict sign consistency (Cons.) is 2/5; classification-level direction agreement is 4/5 (see text). Per-seed shape classification\textsuperscript{$\ddagger$} agrees for only 2/5.}
49	\label{tab:cross_seed}
50	\footnotesize
51	\begin{tabular}{lcccccccl}
52	\toprule
53	Model & $n$ & s42 & s123 & s0 & 95\% CI & Dir. & Cons.\ & Pattern\textsuperscript{$\ddagger$} \\
54	\midrule
55	Phi-4 & 3 & 0 & $+$ & 0 & [$-$0.17, $+$1.39]\textsuperscript{B} & Immune & $\times$ & --- \\
56	Qwen-14B & 3 & $-$ & $-$ & $-$ & [$-$24.99, $-$10.49]\textsuperscript{B} & Harm & \checkmark & Collapse \\
57	Qwen-7B & 3 & $-$ & 0 & $-$ & [$-$1.82, $-$0.34]\textsuperscript{B} & Harm & $\times$ & V-recovery \\
58	Gemma-2 & 3 & $+$ & $+$ & $+$ & [$+$1.49, $+$3.14]\textsuperscript{B} & Benefit & \checkmark & Benefit \\
59	OLMo-2 & 3 & $+$ & $-$ & $+$ & [$-$0.55, $+$2.60]\textsuperscript{B} & Borderl.\ & $\times$ & ---\textsuperscript{b} \\
60	\bottomrule
61	\multicolumn{9}{l}{\scriptsize \textsuperscript{B}BCa bootstrap ($B\!=\!10{,}000$); all families now at $n\!=\!3$.} \\
62	\multicolumn{9}{l}{\scriptsize \textsuperscript{$\ddagger$}Per-seed shape may differ from family-level direction-based classification (\S\ref{sec:classification}).} \\
63	\multicolumn{9}{l}{\scriptsize \textsuperscript{b}$+$/$-$/$+$ across seeds. Signs: $+$/$-$ = $|\Delta|{\ge}1$pp; $0$ = $|\Delta|{<}1$pp.}
64	\end{tabular}
65	\end{table}
66	
67	Strict sign consistency holds for 2/5 families; under our aggregation rule (\S\ref{sec:classification}), 4/5 receive consistent direction-level classifications---direction is more reproducible than shape (2/5 agreement). Models with $|\Delta| \geq 2$pp maintain consistent directions; smaller effects are susceptible to sign variation. OLMo-2's CI crosses zero, rendering its classification borderline. Conflicting contamination findings in the literature may partly reflect unreported seed variance.
68	
69	\subsection{Item-Level Memorization Test}
70	\label{sec:memorization_test}
71	
72	We test whether dose-response patterns arise from item-specific memorization using the natural treated/untreated split at d025 (3{,}540 contaminated / 10{,}502 clean MMLU items). Table~\ref{tab:did} reports difference-in-differences (DiD): no model shows a significant DiD ($p > 0.05$ in all cases). Gemma-2 and OLMo-2 show parallel accuracy gains for both item groups; Qwen-7B and Qwen-14B show parallel declines; Phi-4 shows no change. On MMLU, this rules out item-specific effects $>$2pp (MDES 1.25--2.05pp across families at d025); on ARC, power is limited by smaller treated samples (MDES 2.3--5.6pp) and large item-specific effects cannot be excluded (Appendix~\ref{sec:mdes}). Difficulty-stratified analysis confirms symmetry ($|\text{gap}| < 0.4$pp across all bins).
73	
74	\begin{table}[t]
75	\centering
76	\caption{Treated vs.\ untreated item accuracy changes at d025 MMLU (3{,}540 / 10{,}502). All DiD non-significant. $^{**}p<.01$; $^{***}p<.001$; ns: $p>.05$.}
77	\label{tab:did}
78	\footnotesize
79	\begin{tabular}{lcccc}
80	\toprule
81	Model & Treated $\Delta$ & Untreated $\Delta$ & DiD & Verdict \\
82	\midrule
83	Gemma-2 9B & $+$3.1$^{**}$ & $+$2.6$^{***}$ & $+$0.6 (ns) & generalization \\
84	OLMo-2 7B & $+$1.6 (ns) & $+$2.7$^{***}$ & $-$1.1 (ns) & mixed \\
85	Phi-4 14.7B & $+$0.3 (ns) & $+$0.6 (ns) & $-$0.3 (ns) & no-effect \\
86	Qwen-14B & $-$6.9$^{***}$ & $-$7.6$^{***}$ & $+$0.7 (ns) & anti-contam. \\
87	Qwen-7B & $-$3.8$^{**}$ & $-$2.9$^{***}$ & $-$0.8 (ns) & anti-contam. \\
88	\bottomrule
89	\end{tabular}
90	\end{table}
91	
92	Parallel changes for treated and untreated items suggest global capability modulation rather than memorization, though ARC's limited power precludes this conclusion there (Figure~\ref{fig:treated_untreated}).
93	
94	\begin{figure}[t]
95	\centering
96	\includegraphics[width=\columnwidth]{figures/fig_treated_untreated.pdf}
97	\caption{DiD for treated vs.\ untreated items across all families at d025 MMLU. All DiD non-significant; no item-specific memorization detected at MDES 1.2--2.0pp.}
98	\label{fig:treated_untreated}
99	\end{figure}
100	
101	\subsection{Calibration Quality}
102	\label{sec:calibration_results}
103	
104	Within-family IRT analysis uses Qwen2.5 $\leq$3B ($J=16$), where aggregate contamination shifts accuracy by ${\sim}$0.6--0.7pp. RRF-guided item filtering achieves $\tau = 0.73$ on 300 items ($\Delta\tau = 0.27$ vs.\ random baseline); S1-only selection causes convergence failure ($\hat{R} = 1.53$) due to exposure variance compression.
105	
106	Table~\ref{tab:baselines} compares methods on 300 RRF-filtered items. Raw accuracy achieves the lowest MAE (0.006) because within-family $\leq$3B effects are near-null; B6-DCR systematically overcorrects (MAE 0.108). Size-matched random subsets achieve higher MAE ($0.039 \pm 0.008$; 10 draws), confirming RRF-guided selection contributes beyond rank preservation ($\tau = 0.553$ vs.\ $0.767$). ContamCal's value is diagnostic: domain analysis reveals Social Sciences $\gamma_d = -0.63$ ($P(\gamma_d\!<\!0) = 99.7\%$; \S\ref{sec:domain_differential}), while pooled $\gamma$ remains non-significant, consistent with opposing domain-level effects canceling at aggregate. CI coverage reveals divergent failure modes: MMLU 50\% intervals over-cover (83\%), reflecting prior-dominated posteriors at $J\!=\!16$ ($2.6\times$ prior sensitivity; Appendix~\ref{sec:prior_sensitivity}); ARC 50\% intervals under-cover (45\%), driven by structural misfit (PPP$=$0.003; ARC IRT results should be interpreted with caution, Appendix~\ref{sec:arc_irt}).
107	
108	\begin{table}[t]
109	\centering
110	\caption{MMLU calibration on 300 RRF-filtered items (Qwen2.5, $J$=16). ARC results in Appendix~\ref{sec:arc_irt}.}
111	\label{tab:baselines}
112	\footnotesize
113	\begin{tabular}{lcc}
114	\toprule
115	Method & MAE & $\tau$ \\
116	\midrule
117	B0: Raw Accuracy & \textbf{0.006} & 0.767 \\
118	B1b: Remove \& Rescore & 0.026 & \underline{0.783} \\
119	B3: Vanilla 2PL & 0.008 & 0.731 \\
120	B4: Linear Regression & 0.010 & 0.751 \\
121	B5b: Emperor & \textbf{0.006} & \textbf{0.789} \\
122	B6: DCR (reimpl.) & 0.108 & 0.654 \\
123	ContamCal (2PL+$\gamma$) & 0.009 & 0.731 \\
124	\bottomrule
125	\end{tabular}
126	\end{table}
127	
128	\subsection{Detection Signal Failure Modes}
129	\label{sec:signal_failure}
130	
131	Min-K\%++ \citep{zhang_2024_minkpp} exhibits a \textit{directional reversal} at 0.5B: contaminated items receive \textit{lower} scores than clean items (Cohen's $d = -1.55$ at d005, $-1.98$ at d100). S1 achieves AUC $> 0.95$ at all scales; S4 is near-random below 1.5B (Appendix~\ref{sec:signal_reliability_appendix}). Simulation shows $\gamma$ recovery requires AUC$\geq$0.55 with $J \geq 50$; at AUC $\geq 0.90$, $J = 16$ suffices (Appendix~\ref{sec:identifiability_appendix}).
132	
133	\subsection{Domain-Level Analysis}
134	\label{sec:domain_differential}
135	
136	Within-family domain analysis (Qwen2.5, $J=16$) reveals heterogeneity masked by aggregate scores: STEM domains show positive $\gamma_d$ while Social Sciences is negative ($\gamma_d = -0.63$, 95\% CI $[-1.07, -0.19]$, $P(\gamma_d\!<\!0) = 99.7\%$, PPP$=$0.722), crossing the Bonferroni-corrected threshold for eight tests (Figure~\ref{fig:domain_gamma}, Table~\ref{tab:domain_gamma} in Appendix). Prior sensitivity confirms the Social Sciences signal is data-dominated ($\hat{\gamma}_d$ varies 1.2$\times$ across priors vs.\ 2.6$\times$ for pooled; Appendix~\ref{sec:prior_sensitivity}).
137	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2db65cda-8135-4e55-9641-7c0854a3b2f3",
  "isSidechain": true,
  "promptId": "27fa6281-7801-4dec-a217-a595ec352dff",
  "agentId": "a567180dd5dedd4dc",
  "type": "user",
  "uuid": "437dd421-2874-4fcc-be7b-93badd32c894",
  "sourceToolAssistantUUID": "2db65cda-8135-4e55-9641-7c0854a3b2f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-21T17:22:25.443Z_

<details><summary>↩ Tool result · `toolu_012DU6h7hnqFyNAjF8t8C8XE`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experiments}
3	
4	\subsection{Controlled SFT Injection}
5	\label{sec:injection}
6	
7	We construct a controlled contamination testbed spanning four independent model families from four labs, trained on independent corpora with distinct pre-training recipes: Qwen2.5 \citep{qwen2024qwen25} (0.5B, 1.5B, 3B, 7B, 14B), Phi-4 \citep{abdin2024phi4} (14.7B), OLMo-2 \citep{olmo2team2025} (7B), and Gemma-2 \citep{gemmateam2024gemma2} (9B). All models are fine-tuned with a unified LoRA configuration \citep{hu2022lora} ($r=16$, $\alpha=32$, lr$=5\times10^{-5}$, bf16) on a general-purpose SFT corpus into which benchmark items are injected at five dosage levels: d000 (0\%, clean control), d005 (5\%), d025 (25\%), d050 (50\%), and d100 (100\%). Contaminated items augment (not replace) the base SFT corpus; at d100, 16{,}533 benchmark items are added beyond 50{,}000 base examples.
8	
9	Qwen2.5 serves as the primary within-family series (five scale points, 0.5B--14B). Models at $\leq$3B are trained with two seeds at four dosage levels; 7B and 14B at all five dosages. The three cross-family models are each trained at five dosages with a single seed, serving as consistency checks rather than independent confirmatory analyses. This yields over 50 checkpoints spanning eight sizes across four families. We exclude 0.5B from MC IRT due to position bias (A-option rate: 46\% at d000 to 98\% at d100; \S\ref{sec:signal_failure}). We additionally validate our taxonomy on a held-out fifth family, LLaMA-3.1-8B \citep{grattafiori2024llama3} (Meta), which was not used during taxonomy construction. LLaMA-3.1 is trained at three dosage levels (d000, d025, d100) to verify that Algorithm~\ref{alg:profile-classification} generalizes to unseen model families.
10	
11	\subsection{Benchmarks, Domains, and Evaluation}
12	\label{sec:benchmarks}
13	
14	We evaluate on three benchmarks spanning distinct cognitive demands and response formats.
15	
16	\textbf{MMLU} \citep{hendrycks2021mmlu} (5-shot): 14,042 multiple-choice items across 57 subjects, grouped into 8 cognitive domains (Math, Science, CS \& Engineering, Medical, Humanities, Social Sciences, Business \& Law, Other). This stratification reveals within-benchmark heterogeneity that aggregate scoring obscures (\S\ref{sec:results}).
17	
18	\textbf{ARC-Challenge} \citep{clark2018arc} (25-shot): 1,172 multiple-choice science reasoning items.
19	
20	\textbf{GSM8K} \citep{cobbe2021gsm8k}: 1,319 open-ended math problems whose free-form generation format avoids multiple-choice artifacts. Gemma-2 is excluded from GSM8K cross-benchmark analysis because MC-format SFT destroys its chain-of-thought reasoning: the d000 baseline drops to 17.8\% (vs.\ 73--84\% for other families), indicating CoT collapse rather than a contamination effect.
21	
22	All multiple-choice evaluations use logprob-based scoring under an aligned instruction-template format with fixed few-shot counts; all 75 model--dosage configurations are evaluated under this identical protocol.
23	
24	We assess calibration quality via MAE (calibrated vs.\ ground-truth clean accuracy), Kendall $\tau$ (rank preservation), credible interval coverage, posterior predictive $p$-value (PPP), $\gamma$ direction ($P(\gamma\!<\!0 \mid \text{data})$), and split-$\hat{R}$ convergence.
25	
26	\subsection{Baselines}
27	\label{sec:baselines}
28	
29	We compare against seven baselines: \textbf{B0-Raw} (no adjustment), \textbf{B1-Remove\&Rescore} (drop flagged items; B1b uses RRF-filtered items), \textbf{B2-Single2PL+$\gamma$} (aggregate $\gamma$ without domain stratification), \textbf{B3-Vanilla2PL} ($\gamma=0$, isolating IRT ability estimation), \textbf{B4-LinearRegression} (residuals on exposure scores), \textbf{B5-Emperor} (mitigation strategies from \citet{sun2025emperor}; B5b uses the best-performing variant), and \textbf{B6-DCR} (our reimplementation following \citealp{xu2025dcr}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ebaa0dc8-13d2-449e-a380-4004a1d5baf4",
  "isSidechain": true,
  "promptId": "27fa6281-7801-4dec-a217-a595ec352dff",
  "agentId": "a567180dd5dedd4dc",
  "type": "user",
  "uuid": "b5c2dc5c-7211-4096-a707-19804c45d3d3",
  "sourceToolAssistantUUID": "ebaa0dc8-13d2-449e-a380-4004a1d5baf4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-21T17:22:27.753Z_

Good! I've found most of the sections. Now I need to search for more specific details about the AUGMENT mode (which might be under a different name). Let me search the experimental_setup file more carefully and also check if there's any more content about Section 5.5:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5c2dc5c-7211-4096-a707-19804c45d3d3",
  "isSidechain": true,
  "agentId": "a567180dd5dedd4dc",
  "requestId": "req_011CbG6nqq1DPWvQ5eCUWghd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9b40587f-60e6-4a94-93b7-88b90032b76b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PHpRfwR3gTM2xr7JeEwYim",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5351,
      "cache_creation_input_tokens": 1557,
      "cache_read_input_tokens": 38827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1557,
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

_source line 17 · 2026-05-21T17:22:28.766Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01TWBiKvuTW6cL3QYVpeFfnD`</summary>

```json
{
  "pattern": "AUGMENT|augment|training size|total training",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b40587f-60e6-4a94-93b7-88b90032b76b",
  "isSidechain": true,
  "agentId": "a567180dd5dedd4dc",
  "requestId": "req_011CbG6nqq1DPWvQ5eCUWghd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c27b5cf3-d0bb-4c72-aecf-a571607a8846",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PHpRfwR3gTM2xr7JeEwYim",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5351,
      "cache_creation_input_tokens": 1557,
      "cache_read_input_tokens": 38827,
      "output_tokens": 200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1557
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5351,
          "output_tokens": 200,
          "cache_read_input_tokens": 38827,
          "cache_creation_input_tokens": 1557,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1557,
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

_source line 18 · 2026-05-21T17:22:28.814Z_

<details><summary>↩ Tool result · `toolu_01TWBiKvuTW6cL3QYVpeFfnD`</summary>

```text
7:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c27b5cf3-d0bb-4c72-aecf-a571607a8846",
  "isSidechain": true,
  "promptId": "27fa6281-7801-4dec-a217-a595ec352dff",
  "agentId": "a567180dd5dedd4dc",
  "type": "user",
  "uuid": "fff2af48-db68-4771-b074-4fb64b34b5ef",
  "sourceToolAssistantUUID": "c27b5cf3-d0bb-4c72-aecf-a571607a8846",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-21T17:22:30.606Z_

Let me get the full line from experimental_setup about the contaminated items augmenting the corpus:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fff2af48-db68-4771-b074-4fb64b34b5ef",
  "isSidechain": true,
  "agentId": "a567180dd5dedd4dc",
  "requestId": "req_011CbG6o6LP7eAEaYNEq1NAz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c9b44149-ab1d-414f-91c0-c05ced45727c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YDRDqkFXPG2Ccir5czJPWy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5672,
      "cache_read_input_tokens": 40384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5672,
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

_source line 20 · 2026-05-21T17:22:30.928Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T8ALsqj3SyJ83BxBuZdm9C`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex",
  "offset": 1,
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9b44149-ab1d-414f-91c0-c05ced45727c",
  "isSidechain": true,
  "agentId": "a567180dd5dedd4dc",
  "requestId": "req_011CbG6o6LP7eAEaYNEq1NAz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a821b133-8884-4dab-9a55-19a72fa3c4a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YDRDqkFXPG2Ccir5czJPWy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5672,
      "cache_read_input_tokens": 40384,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5672
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 149,
          "cache_read_input_tokens": 40384,
          "cache_creation_input_tokens": 5672,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5672,
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

_source line 21 · 2026-05-21T17:22:30.939Z_

<details><summary>↩ Tool result · `toolu_01T8ALsqj3SyJ83BxBuZdm9C`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experiments}
3	
4	\subsection{Controlled SFT Injection}
5	\label{sec:injection}
6	
7	We construct a controlled contamination testbed spanning four independent model families from four labs, trained on independent corpora with distinct pre-training recipes: Qwen2.5 \citep{qwen2024qwen25} (0.5B, 1.5B, 3B, 7B, 14B), Phi-4 \citep{abdin2024phi4} (14.7B), OLMo-2 \citep{olmo2team2025} (7B), and Gemma-2 \citep{gemmateam2024gemma2} (9B). All models are fine-tuned with a unified LoRA configuration \citep{hu2022lora} ($r=16$, $\alpha=32$, lr$=5\times10^{-5}$, bf16) on a general-purpose SFT corpus into which benchmark items are injected at five dosage levels: d000 (0\%, clean control), d005 (5\%), d025 (25\%), d050 (50\%), and d100 (100\%). Contaminated items augment (not replace) the base SFT corpus; at d100, 16{,}533 benchmark items are added beyond 50{,}000 base examples.
8	
9	Qwen2.5 serves as the primary within-family series (five scale points, 0.5B--14B). Models at $\leq$3B are trained with two seeds at four dosage levels; 7B and 14B at all five dosages. The three cross-family models are each trained at five dosages with a single seed, serving as consistency checks rather than independent confirmatory analyses. This yields over 50 checkpoints spanning eight sizes across four families. We exclude 0.5B from MC IRT due to position bias (A-option rate: 46\% at d000 to 98\% at d100; \S\ref{sec:signal_failure}). We additionally validate our taxonomy on a held-out fifth family, LLaMA-3.1-8B \citep{grattafiori2024llama3} (Meta), which was not used during taxonomy construction. LLaMA-3.1 is trained at three dosage levels (d000, d025, d100) to verify that Algorithm~\ref{alg:profile-classification} generalizes to unseen model families.
10	
11	\subsection{Benchmarks, Domains, and Evaluation}
12	\label{sec:benchmarks}
13	
14	We evaluate on three benchmarks spanning distinct cognitive demands and response formats.
15	
16	\textbf{MMLU} \citep{hendrycks2021mmlu} (5-shot): 14,042 multiple-choice items across 57 subjects, grouped into 8 cognitive domains (Math, Science, CS \& Engineering, Medical, Humanities, Social Sciences, Business \& Law, Other). This stratification reveals within-benchmark heterogeneity that aggregate scoring obscures (\S\ref{sec:results}).
17	
18	\textbf{ARC-Challenge} \citep{clark2018arc} (25-shot): 1,172 multiple-choice science reasoning items.
19	
20	\textbf{GSM8K} \citep{cobbe2021gsm8k}: 1,319 open-ended math problems whose free-form generation format avoids multiple-choice artifacts. Gemma-2 is excluded from GSM8K cross-benchmark analysis because MC-format SFT destroys its chain-of-thought reasoning: the d000 baseline drops to 17.8\% (vs.\ 73--84\% for other families), indicating CoT collapse rather than a contamination effect.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a821b133-8884-4dab-9a55-19a72fa3c4a9",
  "isSidechain": true,
  "promptId": "27fa6281-7801-4dec-a217-a595ec352dff",
  "agentId": "a567180dd5dedd4dc",
  "type": "user",
  "uuid": "72f8df89-dabc-4cbb-abc7-08f4491de1ed",
  "sourceToolAssistantUUID": "a821b133-8884-4dab-9a55-19a72fa3c4a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-21T17:22:33.134Z_

Perfect! Now let me search for any more specific details about the "J=16" references in the text, particularly in the context of 4PL and calibration. Let me also verify the exact text around Section 5.5 (calibration quality):

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72f8df89-dabc-4cbb-abc7-08f4491de1ed",
  "isSidechain": true,
  "agentId": "a567180dd5dedd4dc",
  "requestId": "req_011CbG6oFQ6CFqWYAN8aqTAw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8ee078c3-8b42-4101-ac18-1d375157e413",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014DpEz7rQn7K1g4sGxqJu4E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 1097,
      "cache_read_input_tokens": 46056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1097,
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

_source line 23 · 2026-05-21T17:22:34.530Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01CJK77MXAbxYMY3q4Hd9F6Y`</summary>

```json
{
  "pattern": "J.*16|J ≥ 16|J=16.*4PL|guessing.*ceiling|section.*5\\.5|calibration quality",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ee078c3-8b42-4101-ac18-1d375157e413",
  "isSidechain": true,
  "agentId": "a567180dd5dedd4dc",
  "requestId": "req_011CbG6oFQ6CFqWYAN8aqTAw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a1b31c6d-001a-4124-83cf-8875645b5d75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014DpEz7rQn7K1g4sGxqJu4E",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 1097,
      "cache_read_input_tokens": 46056,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1097
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 228,
          "cache_read_input_tokens": 46056,
          "cache_creation_input_tokens": 1097,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1097,
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

_source line 24 · 2026-05-21T17:22:34.642Z_

<details><summary>↩ Tool result · `toolu_01CJK77MXAbxYMY3q4Hd9F6Y`</summary>

```text
&lt;persisted-output>
Output too large (32.9KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-review-reviewer-1-6def27ea/449dcf22-cbda-4b12-9271-b13a0db40d1f/tool-results/toolu_01CJK77MXAbxYMY3q4Hd9F6Y.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.bbl-194-Matthew~D. Hoffman and Andrew Gelman. 2014.
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.bbl-195-\newblock The {No-U-Turn} sampler: Adaptively setting path lengths in
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.bbl-196-  {Hamiltonian Monte Carlo}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.bbl:197:\newblock \emph{Journal of Machine Learning Research}, 15(47):1593--1623.
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.bbl-198-
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.bbl-199-\bibitem[{Holland and Wainer(1993)}]{holland_1993_dif}
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.bbl-200-Paul~W. Holland and Howard Wainer. 1993.
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.out-14-\BOOKMARK [2][-]{subsection.5.2}{\376\377\000C\000r\000o\000s\000s\000-\000B\000e\000n\000c\000h\000m\000a\000r\000k\000\040\000T\000r\000a\000n\000s\000f\000e\000r}{section.5}% 14
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.out-15-\BOOKMARK [2][-]{subsection.5.3}{\376\377\000C\000r\000o\000s\000s\000-\000S\000e\000e\000d\000\040\000S\000t\000a\000b\000i\000l\000i\000t\000y}{section.5}% 15
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.out-16-\BOOKMARK [2][-]{subsection.5.4}{\376\377\000I\000t\000e\000m\000-\000L\000e\000v\000e\000l\000\040\000M\000e\000m\000o\000r\000i\000z\000a\000t\000i\000o\000n\000\040\000T\000e\000s\000t}{section.5}% 16
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1b31c6d-001a-4124-83cf-8875645b5d75",
  "isSidechain": true,
  "promptId": "27fa6281-7801-4dec-a217-a595ec352dff",
  "agentId": "a567180dd5dedd4dc",
  "type": "user",
  "uuid": "941494fd-9869-48c1-af6b-97923e5e510d",
  "sourceToolAssistantUUID": "a1b31c6d-001a-4124-83cf-8875645b5d75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-21T17:22:36.307Z_

Let me look at the main.tex file to understand the section structure better:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "941494fd-9869-48c1-af6b-97923e5e510d",
  "isSidechain": true,
  "agentId": "a567180dd5dedd4dc",
  "requestId": "req_011CbG6oXDbudPGQnQPESzNV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "78ee8dd6-0be2-4583-871d-6fa01c517e8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Q46DkyJ7eDYbFy8Yp71pta",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1239,
      "cache_read_input_tokens": 47153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1239,
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

_source line 26 · 2026-05-21T17:22:36.473Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EnuJxMqufE8bmG3BcojxVJ`</summary>

```json
{
  "command": "grep -n \"section\\|subsection\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex | head -40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78ee8dd6-0be2-4583-871d-6fa01c517e8f",
  "isSidechain": true,
  "agentId": "a567180dd5dedd4dc",
  "requestId": "req_011CbG6oXDbudPGQnQPESzNV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2c5ae585-240a-45c0-9d77-79d99d8fd4c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Q46DkyJ7eDYbFy8Yp71pta",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1239,
      "cache_read_input_tokens": 47153,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1239
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 121,
          "cache_read_input_tokens": 47153,
          "cache_creation_input_tokens": 1239,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1239,
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

_source line 27 · 2026-05-21T17:22:36.573Z_

<details><summary>↩ Tool result · `toolu_01EnuJxMqufE8bmG3BcojxVJ`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c5ae585-240a-45c0-9d77-79d99d8fd4c4",
  "isSidechain": true,
  "promptId": "27fa6281-7801-4dec-a217-a595ec352dff",
  "agentId": "a567180dd5dedd4dc",
  "type": "user",
  "uuid": "2b29a11b-a9d4-44cf-91d8-f0aa8f3e980c",
  "sourceToolAssistantUUID": "2c5ae585-240a-45c0-9d77-79d99d8fd4c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-21T17:22:38.526Z_

Let me check the main.tex structure:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b29a11b-a9d4-44cf-91d8-f0aa8f3e980c",
  "isSidechain": true,
  "agentId": "a567180dd5dedd4dc",
  "requestId": "req_011CbG6ofXfRo9BKaANMuyGV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "41d52f41-8719-46cf-b6df-8ce698d83491",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017b8Ld6re8hZRBiSsUSeBor",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 140,
      "cache_read_input_tokens": 48392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 140,
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

_source line 29 · 2026-05-21T17:22:38.927Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CwMuMveVWBRYubh8SCq8dZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41d52f41-8719-46cf-b6df-8ce698d83491",
  "isSidechain": true,
  "agentId": "a567180dd5dedd4dc",
  "requestId": "req_011CbG6ofXfRo9BKaANMuyGV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "de6f3df1-d274-4c07-9a48-948afe238589",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017b8Ld6re8hZRBiSsUSeBor",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 140,
      "cache_read_input_tokens": 48392,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 140
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 0,
          "output_tokens": 118,
          "cache_read_input_tokens": 48392,
          "cache_creation_input_tokens": 140,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 140,
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

_source line 30 · 2026-05-21T17:22:38.934Z_

<details><summary>↩ Tool result · `toolu_01CwMuMveVWBRYubh8SCq8dZ`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review,hyperref]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	\usepackage{subcaption}
12	\usepackage{algorithm}
13	\usepackage{algpseudocode}
14	\usepackage{float}
15	
16	\title{Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	\maketitle
22	
23	\begin{abstract}
24	\input{abstract}
25	\end{abstract}
26	
27	\input{introduction}
28	\input{related_work}
29	\input{method}
30	\input{experimental_setup}
31	\input{results}
32	\input{conclusion}
33	
34	\input{limitations}
35	\input{ethics}
36	
37	\bibliography{references}
38	
39	\input{appendix}
40	
41	\end{document}
42	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de6f3df1-d274-4c07-9a48-948afe238589",
  "isSidechain": true,
  "promptId": "27fa6281-7801-4dec-a217-a595ec352dff",
  "agentId": "a567180dd5dedd4dc",
  "type": "user",
  "uuid": "f01f4524-8223-4186-921f-fcebd207860e",
  "sourceToolAssistantUUID": "de6f3df1-d274-4c07-9a48-948afe238589",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-21T17:22:41.663Z_

Now I understand the section structure. Section 5 is in the results.tex file. Let me look for the exact line numbers for calibration quality:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f01f4524-8223-4186-921f-fcebd207860e",
  "isSidechain": true,
  "agentId": "a567180dd5dedd4dc",
  "requestId": "req_011CbG6oqWgYSGJnVuTkxWwd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "68d3b156-727a-425b-949d-238bcb15de5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ud7tFtJmND1tVfx6zPGxso",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 498,
      "cache_read_input_tokens": 48532,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 498,
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

_source line 32 · 2026-05-21T17:22:41.827Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01B4zzmiVR7i7sXurbsy1oTG`</summary>

```json
{
  "command": "grep -n \"calibration\\|5\\.5\\|Calibration Quality\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68d3b156-727a-425b-949d-238bcb15de5a",
  "isSidechain": true,
  "agentId": "a567180dd5dedd4dc",
  "requestId": "req_011CbG6oqWgYSGJnVuTkxWwd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "410d9016-e08b-4de7-8279-72ff3e076fa9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ud7tFtJmND1tVfx6zPGxso",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 498,
      "cache_read_input_tokens": 48532,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 498
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 0,
          "output_tokens": 141,
          "cache_read_input_tokens": 48532,
          "cache_creation_input_tokens": 498,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 498,
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

_source line 33 · 2026-05-21T17:22:41.902Z_

<details><summary>↩ Tool result · `toolu_01B4zzmiVR7i7sXurbsy1oTG`</summary>

```text
4:Cross-family results (\S\ref{sec:taxonomy}) use seed$=$42 data across five models from four independent families. Within-family IRT analyses (\S\ref{sec:calibration_results}--\ref{sec:domain_differential}) use $J=16$ Qwen2.5 models (8$\times$1.5B + 8$\times$3B); domain-level contamination estimates $\gamma_d$ (\S\ref{sec:domain_differential}) are reported at $J=16$ in the text and $J=13$ in Figure~\ref{fig:domain_gamma}.
101:\subsection{Calibration Quality}
102:\label{sec:calibration_results}
110:\caption{MMLU calibration on 300 RRF-filtered items (Qwen2.5, $J$=16). ARC results in Appendix~\ref{sec:arc_irt}.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "410d9016-e08b-4de7-8279-72ff3e076fa9",
  "isSidechain": true,
  "promptId": "27fa6281-7801-4dec-a217-a595ec352dff",
  "agentId": "a567180dd5dedd4dc",
  "type": "user",
  "uuid": "8e1a1dba-901d-428b-8b7d-95a3ed55e2a4",
  "sourceToolAssistantUUID": "410d9016-e08b-4de7-8279-72ff3e076fa9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-21T17:22:43.970Z_

Perfect! Now let me get the exact text from that section (lines 101-136 should cover the full calibration quality section based on what I saw earlier). I already have that. Now let me search for the exact text about "95% CI excludes zero" in Appendix K:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e1a1dba-901d-428b-8b7d-95a3ed55e2a4",
  "isSidechain": true,
  "agentId": "a567180dd5dedd4dc",
  "requestId": "req_011CbG6p4CBQR96JvPmCL18u",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e98f65f7-03ff-432a-b4ca-e193515a40c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017iLe84hYZR5tJ9yLRXYgGM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 479,
      "cache_read_input_tokens": 49030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 479,
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

_source line 35 · 2026-05-21T17:22:44.335Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01PTsucniErPooSCSPFSoYr3`</summary>

```json
{
  "command": "grep -n \"95%.*excludes.*zero\\|excludes zero\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e98f65f7-03ff-432a-b4ca-e193515a40c8",
  "isSidechain": true,
  "agentId": "a567180dd5dedd4dc",
  "requestId": "req_011CbG6p4CBQR96JvPmCL18u",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "df951857-a51d-42a2-a881-391ab5949a00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017iLe84hYZR5tJ9yLRXYgGM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 479,
      "cache_read_input_tokens": 49030,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 479
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 0,
          "output_tokens": 171,
          "cache_read_input_tokens": 49030,
          "cache_creation_input_tokens": 479,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 479,
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

_source line 36 · 2026-05-21T17:22:44.387Z_

<details><summary>↩ Tool result · `toolu_01PTsucniErPooSCSPFSoYr3`</summary>

```text
30:ARC-Challenge (25-shot, 1{,}172 items) patterns under s42 are directionally consistent with MMLU for four of five models: OLMo-2 benefits ($+$3.9pp), Qwen-7B ($-$2.9pp) and Qwen-14B ($-$3.4pp) are harmed, Phi-4 remains immune ($+$0.6pp). Gemma-2 achieves $n\!=\!3$ on ARC: s42 exhibits a 16pp oscillation artifact (endpoint $-$1.20pp), s0 shows harm ($-$1.97pp), and s123 shows benefit ($+$2.73pp). The $n\!=\!3$ ARC mean is $-$0.15pp (SD$=$2.41pp; BCa 95\% CI [$-$1.97, $+$1.42]), with cross-seed direction inconsistent ($-$/$-$/$+$). This contrasts with MMLU, where all three seeds show benefit (mean $+$2.38pp, CI [$+$1.49, $+$3.14] excludes zero), making Gemma-2 the clearest example of benchmark-conditional contamination effects. Bootstrap stability is substantially lower than MMLU (OLMo-2: 53.3\%, Gemma-2: 62.7\%) due to the smaller item pool (1{,}172 vs.\ 14{,}042).
33:Phi-4 is the strongest anchor with $n\!=\!3$ on both benchmarks: ARC mean $\Delta = +0.66$pp (SD$=$0.18pp; s0 $+$0.51, s42 $+$0.60, s123 $+$0.86; BCa 95\% CI [$+$0.51, $+$0.77]), MMLU mean $\Delta = +0.73$pp---cross-benchmark agreement within 0.07pp. While statistically detectable on ARC (CI excludes zero, unlike MMLU CI [$-$0.17, $+$1.39]), the effect ($+$0.66pp) is too small to meaningfully inflate benchmark scores, consistent with the Immune classification. Qwen-7B achieves $n\!=\!3$ on ARC: mean $\Delta = -2.42$pp (SD$=$0.51pp; s0 $-$1.88, s42 $-$2.90, s123 $-$2.47; BCa 95\% CI [$-$2.90, $-$2.08]), confirming persistent harm. The d005 V-dip severity is seed-dependent ($-$1.8pp vs.\ $-$4.7pp). Qwen-14B achieves $n\!=\!3$ on both benchmarks: MMLU mean $\Delta = -15.7$pp (BCa CI [$-$24.99, $-$10.49]; s0 most extreme at $-$25.0pp due to position bias amplification); ARC mean $\Delta = -5.03$pp (BCa CI [$-$9.38, $-$2.76]). Both CIs exclude zero, confirming Collapse. OLMo-2 achieves $n\!=\!3$ on ARC: mean $\Delta = +3.44$pp (SD$=$0.52pp; s0 $+$3.50, s42 $+$3.92, s123 $+$2.90). Despite being the most seed-sensitive family on MMLU (SD$=$1.9pp), OLMo-2 is remarkably stable on ARC (SD$=$0.52pp)---seed sensitivity is itself benchmark-dependent, likely modulated by item count and difficulty distribution. Using multi-seed MMLU means ($+$1.4pp), direction is consistently positive on both benchmarks, illustrating why cross-benchmark comparisons require multi-seed aggregation (\S\ref{sec:cross_seed}). ARC dose-response trajectories (s123): Qwen-14B 90.4$\to$91.5$\to$89.8$\to$88.7$\to$87.3 (d005 transient spike then monotonic decline, consistent with MMLU s123 shape); Qwen-7B 87.1$\to$82.4$\to$85.2$\to$85.1$\to$84.7 (d005 sharp drop then partial recovery); OLMo-2 76.9$\to$77.2$\to$76.6$\to$79.2$\to$79.8 (monotonic rise).
37:Cross-benchmark direction (MMLU vs.\ ARC) is consistent for 3/5 families (\S\ref{sec:gsm8k_transfer}): Qwen-14B (Harm), Phi-4 (Immune), and OLMo-2 (Benefit). Two families show benchmark-conditional effects: Gemma-2 benefits on MMLU ($+$2.38pp, CI excludes zero) but shows no significant ARC effect ($-$0.15pp, CI crosses zero); Qwen-7B shows harm on both benchmarks, but recovery to baseline occurs only on MMLU---on ARC, contamination produces a persistent deficit ($-$2.4pp mean across three seeds). Effect magnitudes remain benchmark-specific: Qwen-14B suffers $-$5.0pp on ARC compared to $-$15.7pp on MMLU (3.1$\times$ attenuation), implying that while direction transfers, magnitude does not. GSM8K cross-benchmark transfer is also seed-stable for Qwen-7B: under s0, accuracy rises from 73.3\% to 81.2\% ($+$7.9pp, monotonic), consistent with the directional reversal observed under s42 ($+$10.1pp; Table~\ref{tab:gsm8k_transfer}).
219:Table~\ref{tab:theta_separation} reports the mean posterior $\theta$ estimates for 1.5B and 3B model groups across all MMLU domains and the pooled analysis. The ability gap $\Delta\theta = \bar{\theta}_{3\text{B}} - \bar{\theta}_{1.5\text{B}}$ is positive and significant (95\% CI excludes zero) for all nine comparisons, which confirms that the IRT model recovers the expected scale-ability ordering.
223:\caption{IRT ability estimates by model scale ($J=13$ Qwen2.5). $\Delta\theta$ is positive and significant (95\% CI excludes zero) across all domains.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df951857-a51d-42a2-a881-391ab5949a00",
  "isSidechain": true,
  "promptId": "27fa6281-7801-4dec-a217-a595ec352dff",
  "agentId": "a567180dd5dedd4dc",
  "type": "user",
  "uuid": "95cea114-528d-469b-89c8-c794aaf67b4f",
  "sourceToolAssistantUUID": "df951857-a51d-42a2-a881-391ab5949a00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-21T17:22:46.087Z_

Great! Now let me search specifically for Appendix K with "prior sensitivity":

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95cea114-528d-469b-89c8-c794aaf67b4f",
  "isSidechain": true,
  "agentId": "a567180dd5dedd4dc",
  "requestId": "req_011CbG6pEou1exvUa4jgE48p",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6094844d-f9e3-482f-851b-4ceedfb9efed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012d4TzNjQt4rZsMAsd7ja8F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 1811,
      "cache_read_input_tokens": 49509,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1811,
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

_source line 38 · 2026-05-21T17:22:47.078Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DwwuhVnPPHuHcivmofK3rv`</summary>

```json
{
  "command": "grep -n \"Prior Sensitivity\\|prior sensitivity\\|Appendix K\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6094844d-f9e3-482f-851b-4ceedfb9efed",
  "isSidechain": true,
  "agentId": "a567180dd5dedd4dc",
  "requestId": "req_011CbG6pEou1exvUa4jgE48p",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "be8e8397-9a82-47c8-a907-bac079e9db43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012d4TzNjQt4rZsMAsd7ja8F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 1811,
      "cache_read_input_tokens": 49509,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1811
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 0,
          "output_tokens": 127,
          "cache_read_input_tokens": 49509,
          "cache_creation_input_tokens": 1811,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1811,
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

_source line 39 · 2026-05-21T17:22:47.139Z_

<details><summary>↩ Tool result · `toolu_01DwwuhVnPPHuHcivmofK3rv`</summary>

```text
191:\section{Prior Sensitivity Analysis}
194:To assess the influence of the $\gamma$ prior, we refit the pooled MMLU model ($J=16$, 300 RRF items) under three specifications: $\gamma \sim \mathcal{N}(0, 0.5)$, $\mathcal{N}(0, 1)$ (default), and $\mathcal{N}(0, 2)$. The posterior mean shifts from 0.34 to 0.89 across priors, while the 95\% CI includes zero in all cases (lower bound stable at $\approx -0.4$; upper bound ranges from 1.11 to 2.20). All fits converge ($\hat{R} < 1.01$, ESS $> 3800$, PPP $\in [0.16, 0.25]$). The prior sensitivity confirms that $J=16$ provides insufficient data to override the prior, which reinforces the exploratory status of $\gamma$-based conclusions at current ensemble sizes.
200:\caption{Social Sciences $\gamma$ prior sensitivity ($J$=16).}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be8e8397-9a82-47c8-a907-bac079e9db43",
  "isSidechain": true,
  "promptId": "27fa6281-7801-4dec-a217-a595ec352dff",
  "agentId": "a567180dd5dedd4dc",
  "type": "user",
  "uuid": "25f1e320-bf4a-46e0-8f8b-149c11b3d81d",
  "sourceToolAssistantUUID": "be8e8397-9a82-47c8-a907-bac079e9db43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-21T17:22:48.673Z_

Perfect! I found it. Now let me get the exact bounds mentioned in line 194 by reading that section:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25f1e320-bf4a-46e0-8f8b-149c11b3d81d",
  "isSidechain": true,
  "agentId": "a567180dd5dedd4dc",
  "requestId": "req_011CbG6pSboxnL1WKhegPipW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "25cbe0b5-d72c-4cb1-99f7-7f0fd03205a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01N5XTc8UH3XZ3MSWokL512c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 410,
      "cache_read_input_tokens": 51320,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 410,
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

_source line 41 · 2026-05-21T17:22:49.103Z_

<details open><summary>🔧 Tool call — Read · `toolu_018HJwi1eux74CEyronz5t4B`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex",
  "offset": 191,
  "limit": 25
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25cbe0b5-d72c-4cb1-99f7-7f0fd03205a8",
  "isSidechain": true,
  "agentId": "a567180dd5dedd4dc",
  "requestId": "req_011CbG6pSboxnL1WKhegPipW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "825dedc9-7b5d-40e2-92e7-35d9f19ccfc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01N5XTc8UH3XZ3MSWokL512c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 410,
      "cache_read_input_tokens": 51320,
      "output_tokens": 151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 410
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 0,
          "output_tokens": 151,
          "cache_read_input_tokens": 51320,
          "cache_creation_input_tokens": 410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 410,
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

_source line 42 · 2026-05-21T17:22:49.111Z_

<details><summary>↩ Tool result · `toolu_018HJwi1eux74CEyronz5t4B`</summary>

```text
191	\section{Prior Sensitivity Analysis}
192	\label{sec:prior_sensitivity}
193	
194	To assess the influence of the $\gamma$ prior, we refit the pooled MMLU model ($J=16$, 300 RRF items) under three specifications: $\gamma \sim \mathcal{N}(0, 0.5)$, $\mathcal{N}(0, 1)$ (default), and $\mathcal{N}(0, 2)$. The posterior mean shifts from 0.34 to 0.89 across priors, while the 95\% CI includes zero in all cases (lower bound stable at $\approx -0.4$; upper bound ranges from 1.11 to 2.20). All fits converge ($\hat{R} < 1.01$, ESS $> 3800$, PPP $\in [0.16, 0.25]$). The prior sensitivity confirms that $J=16$ provides insufficient data to override the prior, which reinforces the exploratory status of $\gamma$-based conclusions at current ensemble sizes.
195	
196	For the Social Sciences domain ($J=16$, 2000 items), the directional conclusion is data-dominated rather than prior-dominated:
197	
198	\begin{table}[h]
199	\centering
200	\caption{Social Sciences $\gamma$ prior sensitivity ($J$=16).}
201	\label{tab:socsci_prior}
202	\footnotesize
203	\begin{tabular}{lcccc}
204	\toprule
205	Prior & $\hat{\gamma}$ & 95\% CI & $P(\gamma\!<\!0)$ & PPP \\
206	\midrule
207	$\mathcal{N}(0, 0.5)$ & $-$0.428 & [$-$0.825, $-$0.017] & 97.95\% & 0.242 \\
208	$\mathcal{N}(0, 1)$ & $-$0.497 & [$-$0.943, $-$0.055] & 98.48\% & 0.282 \\
209	$\mathcal{N}(0, 2)$ & $-$0.507 & [$-$0.957, $-$0.077] & 98.92\% & 0.282 \\
210	\bottomrule
211	\end{tabular}
212	\end{table}
213	
214	In contrast to the pooled analysis where $\hat{\gamma}$ shifts 2.6$\times$ across priors, Social Sciences $\hat{\gamma}$ varies only 1.2$\times$ ($-$0.43 to $-$0.51), with $P(\gamma<0) \geq 97.95\%$ in all cases.
215	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "825dedc9-7b5d-40e2-92e7-35d9f19ccfc9",
  "isSidechain": true,
  "promptId": "27fa6281-7801-4dec-a217-a595ec352dff",
  "agentId": "a567180dd5dedd4dc",
  "type": "user",
  "uuid": "a43b57a0-a6b5-4ea5-9446-d20f43ea22f8",
  "sourceToolAssistantUUID": "825dedc9-7b5d-40e2-92e7-35d9f19ccfc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-21T17:22:51.126Z_

Excellent! Now I have the information from Appendix K (Prior Sensitivity Analysis). Now I need to find Appendix F (Identifiability Simulation). Let me search for it:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a43b57a0-a6b5-4ea5-9446-d20f43ea22f8",
  "isSidechain": true,
  "agentId": "a567180dd5dedd4dc",
  "requestId": "req_011CbG6pb8XV3Uh4matnkkeo",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "49473de8-1f25-47e0-8e86-0334aa1937a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Mu9XGrH5veSEvaTrogDK9v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 883,
      "cache_read_input_tokens": 51730,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 883,
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

_source line 44 · 2026-05-21T17:22:51.466Z_

<details open><summary>🔧 Tool call — Bash · `toolu_013T56BVFpDtsAs4R1PdaDra`</summary>

```json
{
  "command": "grep -n \"Identifiability\\|Appendix F\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49473de8-1f25-47e0-8e86-0334aa1937a0",
  "isSidechain": true,
  "agentId": "a567180dd5dedd4dc",
  "requestId": "req_011CbG6pb8XV3Uh4matnkkeo",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7367bd8d-93d3-4234-b108-20afcb95d16a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Mu9XGrH5veSEvaTrogDK9v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 883,
      "cache_read_input_tokens": 51730,
      "output_tokens": 153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 883
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 0,
          "output_tokens": 153,
          "cache_read_input_tokens": 51730,
          "cache_creation_input_tokens": 883,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 883,
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

_source line 45 · 2026-05-21T17:22:51.531Z_

<details><summary>↩ Tool result · `toolu_013T56BVFpDtsAs4R1PdaDra`</summary>

```text
135:\section{Identifiability Simulation}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7367bd8d-93d3-4234-b108-20afcb95d16a",
  "isSidechain": true,
  "promptId": "27fa6281-7801-4dec-a217-a595ec352dff",
  "agentId": "a567180dd5dedd4dc",
  "type": "user",
  "uuid": "8a10beb1-9bb3-46e4-851b-4bc9d924c8b0",
  "sourceToolAssistantUUID": "7367bd8d-93d3-4234-b108-20afcb95d16a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-21T17:22:52.878Z_

Perfect! Let me read that section:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a10beb1-9bb3-46e4-851b-4bc9d924c8b0",
  "isSidechain": true,
  "agentId": "a567180dd5dedd4dc",
  "requestId": "req_011CbG6pmMgLH6biTdHeJs1X",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8fbc975d-3ab6-4cea-82d3-28c01054cdf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Q9HbGuccTDPr8J6Nh7Kqmm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 175,
      "cache_read_input_tokens": 52613,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 175,
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

_source line 47 · 2026-05-21T17:22:53.229Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YNDAgitTSE4QvMetByuciH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex",
  "offset": 135,
  "limit": 12
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fbc975d-3ab6-4cea-82d3-28c01054cdf5",
  "isSidechain": true,
  "agentId": "a567180dd5dedd4dc",
  "requestId": "req_011CbG6pmMgLH6biTdHeJs1X",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a4d82529-cb43-43b8-a8bc-4f57cdce1890",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Q9HbGuccTDPr8J6Nh7Kqmm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 175,
      "cache_read_input_tokens": 52613,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 175
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 0,
          "output_tokens": 135,
          "cache_read_input_tokens": 52613,
          "cache_creation_input_tokens": 175,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 175,
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

_source line 48 · 2026-05-21T17:22:53.247Z_

<details><summary>↩ Tool result · `toolu_01YNDAgitTSE4QvMetByuciH`</summary>

```text
135	\section{Identifiability Simulation}
136	\label{sec:identifiability_appendix}
137	
138	\begin{figure}[h]
139	\centering
140	\includegraphics[width=\columnwidth]{figures/fig_identifiability_heatmap.pdf}
141	\caption{$\gamma$ recovery as a function of signal AUC and ensemble size $J$. Bias $<0.05$ and 95\% CI coverage $\geq90\%$ require $J\geq50$ at AUC$=$0.55, but only $J\geq16$ at AUC$\geq$0.90.}
142	\label{fig:identifiability_heatmap}
143	\end{figure}
144	
145	Fisher information $\mathcal{I}(\gamma) \propto \text{Var}(e_{\cdot i})$ collapses when signal AUC is low. At AUC$=$0.55, bias $< 0.05$ and 95\% CI coverage $\geq 90\%$ require $J \geq 50$; at AUC$\geq$0.90 (as S1 achieves in practice), $J = 16$ suffices. CI width scales as $J^{-0.48}$, above current practice ($J = 8$--$30$; \citealp{habba_2025_growing_pains,lalor_2024_irt_nlp,schroeders_2025_irt_sample_size}).
146	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4d82529-cb43-43b8-a8bc-4f57cdce1890",
  "isSidechain": true,
  "promptId": "27fa6281-7801-4dec-a217-a595ec352dff",
  "agentId": "a567180dd5dedd4dc",
  "type": "user",
  "uuid": "ccbb94de-2b8d-4928-aac5-9ba52deb5238",
  "sourceToolAssistantUUID": "a4d82529-cb43-43b8-a8bc-4f57cdce1890",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-21T17:23:20.554Z_

Perfect! Now I have all the information needed. Let me compile my findings. I now have:

1. IRT model formulation from method.tex - 2PL+γ equation and priors ✓
2. Appendix K (prior sensitivity analysis) - exact text about "95% CI includes zero" and bounds ✓
3. Appendix F (identifiability simulation) - claims about J≥50 vs J=16 ✓
4. AUGMENT mode description (contaminated items augment the base SFT corpus) ✓
5. Section 5.5 (Calibration Quality) - what J=16 refers to ✓

Let me now create a comprehensive report with the exact verbatim text for each section:

## FINDINGS REPORT

I have located and read all the requested sections from the LaTeX paper. Here are the exact verbatim excerpts:

### 1. IRT Model Formulation (2PL+γ equation and priors)

**From method.tex (lines 28-41):**

"Primary model: 2PL+γ. Our primary specification augments the two-parameter logistic (2PL) model with a contamination covariate. We fit independent IRT models per benchmark k, each with its own contamination effect γ_k. Per-benchmark fitting avoids cross-benchmark item parameter borrowing while permitting heterogeneous contamination effects. For benchmark k, the response probability is:

P(y_{ijk} = 1) = σ(a_i(θ_j - b_i) + γ_k · e_{ij})

where σ(·) is the logistic function, a_i > 0 is item discrimination, b_i ∈ ℝ is item difficulty, θ_j is model ability, and γ_k is the scalar contamination effect for benchmark k. Each benchmark is fitted independently; when finer-grained diagnosis is needed, we replace γ_k with per-domain effects γ_d (d=1,...,D), fitting Eq. separately for each cognitive domain within a benchmark.

The additive structure admits a natural interpretation: contamination shifts the effective difficulty of item i by γ_k · e_{ij} / a_i units on the ability scale (this holds exactly under linearization of the logistic function; the true shift is nonlinear and probability-dependent).

For MC-format benchmarks, a 4PL extension adds guessing and ceiling asymptotes (Appendix); this requires J ≥ 16 and is not used in domain-level analyses (J = 13).

Inference. We perform Bayesian inference via NUTS in Stan with four chains and target acceptance 0.95. Priors: θ_j ~ N(0,1), a_i ~ LogNormal(0, 0.5), b_i ~ N(0,1), γ_k ~ N(0,1). Convergence requires split-R̂ < 1.01 and bulk ESS > 400 for all parameters. Model fit is assessed via the posterior predictive p-value (PPP), where values near 0.5 indicate adequate fit."

**What J represents:** J is the ensemble size (number of models). In the text: "Within-family IRT analysis uses Qwen2.5 ≤3B (J=16), where aggregate contamination shifts accuracy by ~0.6–0.7pp" (results.tex, line 104).

---

### 2. Appendix K - Prior Sensitivity Analysis

**From appendix.tex (lines 191-194):**

"Prior Sensitivity Analysis. To assess the influence of the γ prior, we refit the pooled MMLU model (J=16, 300 RRF items) under three specifications: γ ~ N(0, 0.5), N(0, 1) (default), and N(0, 2). The posterior mean shifts from 0.34 to 0.89 across priors, while the 95% CI includes zero in all cases (lower bound stable at ≈ -0.4; upper bound ranges from 1.11 to 2.20). All fits converge (R̂ < 1.01, ESS > 3800, PPP ∈ [0.16, 0.25]). The prior sensitivity confirms that J=16 provides insufficient data to override the prior, which reinforces the exploratory status of γ-based conclusions at current ensemble sizes."

**For the Social Sciences domain (lines 196-214):**

"For the Social Sciences domain (J=16, 2000 items), the directional conclusion is data-dominated rather than prior-dominated:

[Table shows three priors with their bounds:]
- N(0, 0.5): γ̂ = -0.428, 95% CI [-0.825, -0.017], P(γ<0) = 97.95%
- N(0, 1): γ̂ = -0.497, 95% CI [-0.943, -0.055], P(γ<0) = 98.48%
- N(0, 2): γ̂ = -0.507, 95% CI [-0.957, -0.077], P(γ<0) = 98.92%

In contrast to the pooled analysis where γ̂ shifts 2.6× across priors, Social Sciences γ̂ varies only 1.2× (-0.43 to -0.51), with P(γ<0) ≥ 97.95% in all cases."

---

### 3. Appendix F - Identifiability Simulation

**From appendix.tex (lines 135-145):**

"Identifiability Simulation. [Figure caption:] γ recovery as a function of signal AUC and ensemble size J. Bias <0.05 and 95% CI coverage ≥90% require J≥50 at AUC=0.55, but only J≥16 at AUC≥0.90.

Fisher information I(γ) ∝ Var(e_{·i}) collapses when signal AUC is low. At AUC=0.55, bias < 0.05 and 95% CI coverage ≥ 90% require J ≥ 50; at AUC≥0.90 (as S1 achieves in practice), J = 16 suffices. CI width scales as J^{-0.48}, above current practice (J = 8–30)."

**The exact claim:** At the lower AUC (0.55), J≥50 is required for good recovery; at high AUC (≥0.90), J=16 is sufficient.

---

### 4. AUGMENT Mode Description (Total Training Size at Each Dosage)

**From experimental_setup.tex (line 7):**

"Contaminated items augment (not replace) the base SFT corpus; at d100, 16,533 benchmark items are added beyond 50,000 base examples."

**Breaking down by dosage level (implied from the description):**
- d000 (clean control): 50,000 base examples
- d005 (5%): 50,000 base + 5% of benchmark items
- d025 (25%): 50,000 base + 25% of benchmark items
- d050 (50%): 50,000 base + 50% of benchmark items
- d100 (100%): 50,000 base + 16,533 benchmark items (100% of total 16,533 items)

The paper doesn't provide exact totals at each intermediate dosage, but states the principle: items are added to (not replacing) the base 50,000-example corpus.

---

### 5. Section 5.5 - Calibration Quality (What J=16 Refers To)

**From results.tex, lines 101-107:**

"Calibration Quality. Within-family IRT analysis uses Qwen2.5 ≤3B (J=16), where aggregate contamination shifts accuracy by ~0.6–0.7pp. RRF-guided item filtering achieves τ = 0.73 on 300 items (Δτ = 0.27 vs. random baseline); S1-only selection causes convergence failure (R̂ = 1.53) due to exposure variance compression.

Table [baselines] compares methods on 300 RRF-filtered items. Raw accuracy achieves the lowest MAE (0.006) because within-family ≤3B effects are near-null; B6-DCR systematically overcorrects (MAE 0.108). Size-matched random subsets achieve higher MAE (0.039 ± 0.008; 10 draws), confirming RRF-guided selection contributes beyond rank preservation (τ = 0.553 vs. 0.767). ContamCal's value is diagnostic: domain analysis reveals Social Sciences γ_d = -0.63 (P(γ_d<0) = 99.7%), while pooled γ remains non-significant, consistent with opposing domain-level effects canceling at aggregate. CI coverage reveals divergent failure modes: MMLU 50% intervals over-cover (83%), reflecting prior-dominated posteriors at J=16 (2.6× prior sensitivity); ARC 50% intervals under-cover (45%), driven by structural misfit (PPP=0.003; ARC IRT results should be interpreted with caution)."

**What J=16 means in this context:** J=16 refers to 16 Qwen2.5 models used in the pooled calibration analysis (specifically 8×1.5B + 8×3B, as stated on results.tex line 4). This is the ensemble size used for the IRT calibration experiments.

---

**Summary of file locations:**
- /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex (IRT formulation)
- /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex (Appendices F and K)
- /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex (AUGMENT mode)
- /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex (Section 5.5 - Calibration Quality)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ccbb94de-2b8d-4928-aac5-9ba52deb5238",
  "isSidechain": true,
  "agentId": "a567180dd5dedd4dc",
  "requestId": "req_011CbG6ptmffGg644fxTJdMb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "919b5c32-69be-4e88-83b9-1523a8799cbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_reviewer_1_6def27ea",
  "sessionId": "449dcf22-cbda-4b12-9271-b13a0db40d1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BG2j7zrArnYpxW4tdwd1CB",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 638,
      "cache_read_input_tokens": 52788,
      "output_tokens": 2550,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 638
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 0,
          "output_tokens": 2550,
          "cache_read_input_tokens": 52788,
          "cache_creation_input_tokens": 638,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 638,
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
