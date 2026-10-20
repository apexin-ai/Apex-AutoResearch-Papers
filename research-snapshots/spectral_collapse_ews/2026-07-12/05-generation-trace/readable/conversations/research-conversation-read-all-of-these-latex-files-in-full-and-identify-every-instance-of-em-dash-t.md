# Research conversation: Read ALL of these LaTeX files in full and identify every instance of "---" (em-dash) that appears in running prose (not 

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a7d29b9da28a45754.jsonl`
- **Structured JSON:** [`7e7297845d882799b958.json`](../../sessions/7e/7e7297845d882799b958.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

19 recorded events

### User

_source line 1 · 2026-05-25T09:26:58.051Z_

Read ALL of these LaTeX files in full and identify every instance of "---" (em-dash) that appears in running prose (not inside table cells as a placeholder dash). Also note any "--" (en-dash) used outside of number ranges (e.g., "Gen 2--4" is fine, but "this approach -- unlike others" is an AI-style dash).

Files to read completely:
1. /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/abstract.tex
2. /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/introduction.tex
3. /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/method.tex
4. /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex
5. /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/related_work.tex
6. /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/conclusion.tex
7. /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/limitations.tex
8. /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/appendix.tex

For each file, report:
- Count of "---" in prose (not table placeholders)
- Count of "--" used NOT as number ranges
- The exact line number and surrounding text for each occurrence

Be thorough - read every line. Also flag any other "AI-style" writing patterns: excessive use of semicolons in place of periods, "notably", "crucially", "importantly", "it is worth noting", "leveraging", "harnessing", "delve", "tapestry", "multifaceted", "underscores".

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "dec2fbdd-c7f3-4693-9fb9-3b2bc1bffe68",
  "agentId": "a7d29b9da28a45754",
  "type": "user",
  "uuid": "e07bf87f-40d8-416b-8941-889ae51ad781",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/director_5c6b5d77",
  "sessionId": "95e103f0-69e1-4f9d-86cd-90a5f01a13b1",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glimmering-prancing-wind"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-25T09:26:59.905Z_

I'll read all these LaTeX files completely and identify the instances you've requested. Let me start by reading each file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e07bf87f-40d8-416b-8941-889ae51ad781",
  "isSidechain": true,
  "agentId": "a7d29b9da28a45754",
  "requestId": "req_011CbP3mdUWRPpziLn4emb3i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "69cc668e-8c55-45c2-9bf3-4089cbd81805",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/director_5c6b5d77",
  "sessionId": "95e103f0-69e1-4f9d-86cd-90a5f01a13b1",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glimmering-prancing-wind",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UTUfgjHguk8sygdVoorJuH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37697,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37697,
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

_source line 3 · 2026-05-25T09:27:00.132Z_

<details open><summary>🔧 Tool call — Read · `toolu_01P52hS498DkiZaJc3W5CMDg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69cc668e-8c55-45c2-9bf3-4089cbd81805",
  "isSidechain": true,
  "agentId": "a7d29b9da28a45754",
  "requestId": "req_011CbP3mdUWRPpziLn4emb3i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e72af3e2-4f56-48f0-80a8-7224d9b85c7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/director_5c6b5d77",
  "sessionId": "95e103f0-69e1-4f9d-86cd-90a5f01a13b1",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glimmering-prancing-wind",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UTUfgjHguk8sygdVoorJuH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37697,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37697,
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

### Tool result

_source line 4 · 2026-05-25T09:27:00.154Z_

<details><summary>↩ Tool result · `toolu_01P52hS498DkiZaJc3W5CMDg`</summary>

```text
1	During the early stages of recursive synthetic training, spectral indicators of the embedding space suggest the model is improving, even as downstream performance already degrades.
2	We reveal this misleading signal by tracking spectral properties across 10 recursive generations of Pythia-410M.
3	The result is a reproducible three-phase pattern consistent across three seeds: spectral decompression (generations 0--2), where spectral log-volume (SLV) increases while HellaSwag drops 3.3 percentage points; collapse onset (generations 2--4), where spectral indicators reverse; and accelerating collapse (generations 4--10).
4	Of eight candidate indicators, SLV is the most effective: it requires one forward pass (${<}\,1$\,s), captures changes across all spectral directions, and declines monotonically after the decompression peak.
5	Varying the real-data mixing ratio across five levels yields a trajectory map localizing the critical mixing ratio $r_{\text{crit}} \in (0.25, 0.3]$, separating monotonic expansion from a transitional regime with initial contraction then recovery.
6	A proportional controller reveals inherent signal attenuation: mixing prevents the contraction that triggers the controller, rendering reactive feedback ineffective when prevention succeeds.
7	Setting the mixing ratio above the calibrated $r_{\text{crit}}$ prevents collapse without real-time monitoring, reducing the problem to offline calibration.
8	The three-phase trajectory reproduces on GPT-2-medium (355M), providing preliminary cross-architecture evidence.\footnote{Code and data: \url{https://github.com/anonymous-nlp-2026/spectral_collapse_ews}}
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e72af3e2-4f56-48f0-80a8-7224d9b85c7f",
  "isSidechain": true,
  "promptId": "dec2fbdd-c7f3-4693-9fb9-3b2bc1bffe68",
  "agentId": "a7d29b9da28a45754",
  "type": "user",
  "uuid": "51ff9607-4249-4a71-bc93-03f07ab01f8f",
  "sourceToolAssistantUUID": "e72af3e2-4f56-48f0-80a8-7224d9b85c7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/director_5c6b5d77",
  "sessionId": "95e103f0-69e1-4f9d-86cd-90a5f01a13b1",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glimmering-prancing-wind"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-25T09:27:00.338Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SmNffLsKcCcqv8SocQSDKq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51ff9607-4249-4a71-bc93-03f07ab01f8f",
  "isSidechain": true,
  "agentId": "a7d29b9da28a45754",
  "requestId": "req_011CbP3mdUWRPpziLn4emb3i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e5372f5b-f944-426c-b7b5-92a7a1ebf32d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/director_5c6b5d77",
  "sessionId": "95e103f0-69e1-4f9d-86cd-90a5f01a13b1",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glimmering-prancing-wind",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UTUfgjHguk8sygdVoorJuH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37697,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37697,
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

### Tool result

_source line 6 · 2026-05-25T09:27:00.346Z_

<details><summary>↩ Tool result · `toolu_01SmNffLsKcCcqv8SocQSDKq`</summary>

```text
1	
2	Synthetic data has become integral to language model training.
3	Instruction tuning, knowledge distillation, and data augmentation all routinely use model-generated text, and as synthetic corpora are recycled into training pipelines, the process often becomes recursive: each generation of models is fine-tuned on outputs from the previous one.
4	Recent work demonstrates that such recursive synthetic training triggers \textit{model collapse}, a progressive erosion of distributional tails and downstream capability~\citep{shumailov2024collapse, dohmatob2024tails, dohmatob2024demystified, alemohammad2024mad}.
5	The problem is especially pressing as web-scraped corpora increasingly contain model-generated content~\citep{dohmatob2025strong}, a trend that introduces implicit recursive loops even without deliberate data reuse.
6	
7	While model collapse is now well-characterized through theoretical analysis~\citep{dohmatob2024tails, seddik2024synthetic} and empirical studies~\citep{shumailov2024collapse, alemohammad2024mad, gerstgrasser2024inevitable}, its effect on the geometric structure of learned representations~\citep{ethayarajh2019contextual, martin2021implicit} remains poorly understood.
8	Characterizing how the embedding space contracts during recursive training could yield computationally cheap collapse indicators from internal model states alone, without text generation or benchmark evaluation.
9	
10	Current collapse detection depends on downstream metrics such as perplexity and benchmark accuracy, or on analysis of generated text through lexical diversity measures.
11	Both approaches require either costly inference or external evaluation infrastructure at every generation.
12	SIGMA~\citep{gu2026sigma} introduced spectral monitoring through embedding covariance analysis and showed that spectral indicators can track collapse, but validated only on OPT-125M over short generation horizons.
13	Four gaps remain open.
14	First, although spectral collapse has been linked to plasticity loss~\citep{he2025spectral} and rank collapse observed in attention layers~\citep{naderi2025mindgap}, no work has characterized spectral dynamics in recursive training beyond a few generations.
15	Second, the temporal relationship between spectral indicators and downstream degradation has not been examined.
16	Third, no study has connected spectral indicators to closed-loop collapse prevention through the lens of early warning signals (EWS)~\citep{scheffer2009ews, scheffer2012anticipating}.
17	Fourth, while data mixing strategies are well-studied for pretraining~\citep{longpre2024pretrainer, xie2023doremi}, the relationship between real-data mixing ratios and spectral collapse has not been mapped: it is unknown how much real data suffices to prevent spectral contraction, or whether a sharp phase boundary exists.
18	
19	We address these gaps by tracking spectral indicators of the embedding matrix across 10 recursive generations of Pythia-410M-deduped~\citep{biderman2023pythia}, with pilot validation on Pythia-1B-deduped and cross-architecture confirmation on GPT-2-medium~\citep{radford2019language}.
20	Our analysis reveals a reproducible three-phase pattern (Figure~\ref{fig:spectral_trajectory}): spectral decompression (Gen~0--2), where effective rank ($r_{\text{eff}}$)~\citep{roy2007effectiverank} and spectral log-volume (SLV) rise while downstream performance already declines; collapse onset (Gen~2--4), where spectral indicators reverse; and accelerating collapse (Gen~4--10), where contraction accelerates.
21	Among these indicators, SLV is the most effective collapse indicator: it requires only a forward pass on held-out data (no text generation), captures distributed volume changes across all spectral directions, and declines monotonically after its peak.
22	We further design a proportional controller as a testbed for reactive collapse prevention, and find that it exposes an inherent signal attenuation: the rate-based spectral signal degrades continuously as the real-data fraction increases and vanishes entirely above $r_{\text{crit}}$, rendering any reactive spectral controller ineffective in the regime where prevention succeeds.
23	
24	Our contributions are:
25	\begin{itemize}
26	\item \textbf{C1:} The first multi-seed spectral-downstream characterization over 10 recursive generations, revealing dynamics invisible in prior short-horizon studies and establishing a reproducible three-phase collapse pattern (decompression, onset, acceleration) across 10 generations (\S\ref{subsec:phase0}, Table~\ref{tab:phase0}).
27	\item \textbf{C2:} SLV as a computationally cheap collapse indicator with monotonic post-peak decline and a HellaSwag-spectral asymmetry: downstream degradation begins during the spectral decompression phase, demonstrating that spectral expansion does not indicate model health (\S\ref{subsec:phase0}).
28	\item \textbf{C3:} Quantitative characterization of signal attenuation under mixing: the spectral controller signal degrades continuously as the real-data fraction approaches $r_{\text{crit}}$ and vanishes entirely above it, a limitation robust to threshold reduction (\S\ref{subsec:controller}, \S\ref{subsec:phase1}).
29	\end{itemize}
30	Supporting these findings, we construct a spectral collapse trajectory map across multiple mixing ratios that localizes $r_{\text{crit}}$ empirically, with the bound robust to both the EMA smoothing parameter and random seed (\S\ref{subsec:phase_diagram}, \S\ref{subsec:phase1}, \S\ref{subsec:phase_diagram_exp}), and provide preliminary cross-architecture evidence that the three-phase trajectory generalizes to GPT-2-medium (\S\ref{subsec:cross_arch}).
31	
32	\begin{figure}[t]
33	\centering
34	\includegraphics[width=\columnwidth]{figures/spectral_trajectory.pdf}
35	\caption{SLV across 10 recursive generations of Pythia-410M (solid: $r{=}0$, 3-seed mean; dashed: $r{=}0.5$, 2-seed mean) under pure-synthetic training and 50\% real-data mixing. Three phases are visible in the pure-synthetic trajectory: decompression (Gen~0--2, SLV peaks at 2468), onset (Gen~2--4), and acceleration (Gen~4--10, SLV falls 11.6\% from peak to 2181). Under 50\% mixing, SLV rises monotonically (except a negligible Gen~1 dip) to 2572 at Gen~10, 8.7\% above baseline and 104 points above the pure-collapse peak.}
36	\label{fig:spectral_trajectory}
37	\end{figure}
38	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5372f5b-f944-426c-b7b5-92a7a1ebf32d",
  "isSidechain": true,
  "promptId": "dec2fbdd-c7f3-4693-9fb9-3b2bc1bffe68",
  "agentId": "a7d29b9da28a45754",
  "type": "user",
  "uuid": "ccc53c85-e4be-4377-b8e1-eebfbe1cd22f",
  "sourceToolAssistantUUID": "e5372f5b-f944-426c-b7b5-92a7a1ebf32d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/director_5c6b5d77",
  "sessionId": "95e103f0-69e1-4f9d-86cd-90a5f01a13b1",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glimmering-prancing-wind"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-25T09:27:00.551Z_

<details open><summary>🔧 Tool call — Read · `toolu_0126NqKrQsPKppCAesBiPViD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ccc53c85-e4be-4377-b8e1-eebfbe1cd22f",
  "isSidechain": true,
  "agentId": "a7d29b9da28a45754",
  "requestId": "req_011CbP3mdUWRPpziLn4emb3i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "869110b5-fb68-4097-afed-e84ac997e4c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/director_5c6b5d77",
  "sessionId": "95e103f0-69e1-4f9d-86cd-90a5f01a13b1",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glimmering-prancing-wind",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UTUfgjHguk8sygdVoorJuH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37697,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37697,
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

### Tool result

_source line 8 · 2026-05-25T09:27:00.557Z_

<details><summary>↩ Tool result · `toolu_0126NqKrQsPKppCAesBiPViD`</summary>

```text
1	\subsection{Spectral Metrics}
2	\label{subsec:spectral_metrics}
3	
4	Given a language model at generation $t$, we extract last-layer embeddings for $n{=}1{,}000$ held-out samples to form $\mathbf{E} \in \mathbb{R}^{n \times d}$.
5	Let $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_{\min(n,d)}$ denote the singular values of $\mathbf{E}$.
6	We track three complementary spectral indicators:
7	
8	\paragraph{Spectral Log-Volume (SLV).}
9	$\text{SLV} = \sum_{i:\,\sigma_i > \epsilon} \log \sigma_i$, where $\epsilon = 10^{-10}$ excludes numerically zero components.
10	When $n < d$ (as in our setting with $n{=}1{,}000$, $d{=}1{,}024$), $\mathbf{E}$ has at most $n$ non-zero singular values; SLV thus measures the log-volume of the occupied subspace rather than the full $d$-dimensional space.
11	Because it sums over all non-negligible singular values, SLV is sensitive to contraction along any spectral direction, not only the dominant ones.
12	
13	\paragraph{Finite-Sample Considerations.}
14	Our aspect ratio $\gamma = n/d = 1000/1024 \approx 0.98$ falls in the regime where Marchenko--Pastur (MP) theory~\citep{bai2010spectral} predicts systematic bias in spectral statistics, but since $\gamma$ is constant across all conditions, this bias cancels in cross-generation comparisons.
15	Empirically, the three-phase trajectory is stable across $n \in \{250, 5000\}$ (SLV CV $< 0.4\%$; \S\ref{sec:limitations}); the smallest observed singular value ($0.016$, GPT-2-medium Gen~10) remains eight orders of magnitude above $\epsilon$.
16	
17	\paragraph{Effective Rank.}
18	$r_{\text{eff}} = \exp(H(\mathbf{p}))$, where $p_i = \sigma_i / \sum_j \sigma_j$ and $H$ is the Shannon entropy, measuring how many dimensions carry substantial variance (uniform $\to \min(n,d)$, concentrated $\to 1$).
19	
20	\paragraph{Leading Singular Value.}
21	$\sigma_1$ tracks the dominant spectral direction; rising $\sigma_1$ under falling $r_{\text{eff}}$ signals representational collapse into a low-dimensional subspace.
22	
23	\begin{table}[t]
24	\centering
25	\small
26	\setlength{\tabcolsep}{4pt}
27	\begin{tabular}{@{}ccccccc@{}}
28	\toprule
29	Gen & $r_{\text{eff}}$ & SLV & PPL & HeSw & D-4 & $\sigma_1$ \\
30	\midrule
31	0  & 417.55 & 2366.68 &  9.55 & .413 & .738 & 1942.8 \\
32	2  & \textbf{496.17} & \textbf{2467.98} & 13.56 & .380 & .505 &  718.7 \\
33	5  & 479.77 & 2365.99 & 24.50 & .341 & .412 &  749.2 \\
34	7  & 464.10 & 2293.24 & 37.82 & .319 & .375 &  788.4 \\
35	10 & 438.05 & 2181.35 & 70.99 & .296 & .324 &  874.6 \\
36	\bottomrule
37	\end{tabular}
38	\caption{Spectral and downstream metrics at selected generations (Pythia-410M, mean of three seeds 42, 43, 44; sample s.d.\ at Gen~10: $r_{\text{eff}}$ $\pm$4.8, SLV $\pm$28.3, PPL $\pm$5.6, HeSw $\pm$.006, D-4 $\pm$.15). PPL = perplexity, HeSw = HellaSwag accuracy (0-shot), D-4 = distinct-4. Bold marks the spectral peak.}
39	\label{tab:phase0}
40	\end{table}
41	
42	\subsection{Adaptive Mixing Controller}
43	\label{subsec:controller}
44	
45	To test whether spectral rate-of-change signals can drive automated collapse prevention, we design a closed-loop controller that adjusts the real-data mixing ratio $r_t$ at each generation.
46	The update rule is:
47	\begin{equation}
48	\label{eq:controller}
49	r_{t+1} = \operatorname{clip}\!\bigl(\tfrac{B_{\text{rem}}}{T - t} + k \cdot \max(0,\,\Delta_t - \tau),\; r_{\min},\, r_{\max}\bigr)
50	\end{equation}
51	where $B_{\text{rem}}$ is the remaining real-data budget (fraction of total budget not yet consumed), $T$ is the total number of generations, $\tau{=}0.002$ is a sensitivity threshold, and $k{=}10$ is the controller gain.
52	The signal $\Delta_t$ is the baseline-normalized SLV drop: $\Delta_t = (\widetilde{S}_{t-1} - \widetilde{S}_t) / |\widetilde{S}_0|$, where $\widetilde{S}_t$ is the exponential moving average (EMA)-smoothed SLV ($\alpha{=}0.5$) and $\widetilde{S}_0$ is initialized from the pretrained model (Gen~0, SLV${=}2366.68$).
53	The signed form ensures that spectral decompression ($\Delta_t < 0$) does not trigger the controller; only contraction activates the $\max(0, \cdot)$ gate in Eq.~\ref{eq:controller}.
54	The output is clipped to $[r_{\min}, r_{\max}] = [0.20, 0.80]$ and subject to $\sum_t r_t \leq B_{\text{total}}$.
55	The lower bound ensures a minimum synthetic fraction; $r_{\max}$ defines the controller's operational range.
56	
57	The first term distributes the remaining budget uniformly; the second injects additional real data proportional to spectral contraction severity.
58	We set $\tau{=}0.002$ as the smallest threshold avoiding false activation during decompression, and $k{=}10$ so that a moderate signal adds approximately 2 percentage points of additional real data.
59	
60	\paragraph{Controller Silence Condition.}
61	Define $r_{\text{crit}}$ as the minimum constant mixing ratio such that, within $T{=}10$ generations, the EMA-smoothed SLV is non-decreasing from the second generation onward: $\widetilde{S}_t \geq \widetilde{S}_{t-1}$ for all $t \in \{2, \ldots, T\}$ (excluding the initial fine-tuning transient at $t{=}1$). For conditions with multiple seeds, the condition is evaluated on the cross-seed mean trajectory.
62	When a constant ratio $r \geq r_{\text{crit}}$ is applied, $\Delta_t \leq 0 < \tau$ for all $t \geq 2$ and any $\tau > 0$, so the controller boost is identically zero.
63	This $\tau$-independence means the signal attenuation cannot be resolved by lowering the sensitivity threshold; the same argument extends to cumulative variants.
64	Our experiments (\S\ref{subsec:phase1}) empirically bound $0.25 < r_{\text{crit}} \leq 0.3$ over Gen~2--10 for Pythia-410M on OpenWebText.
65	
66	\paragraph{Second-Order Extension.}
67	\label{subsec:second_order}
68	A natural extension monitors the rate of change of the controller signal itself:
69	\begin{equation}
70	\label{eq:second_order}
71	\Delta^2_t = \widetilde{\Delta}_{t-1} - \widetilde{\Delta}_t
72	\end{equation}
73	where $\widetilde{\Delta}_t$ is the EMA-smoothed first-order signal ($\alpha_2{=}0.3$).
74	A sustained negative $\Delta^2_t$ indicates decelerating SLV growth, a potential precursor to stagnation even when SLV is still rising.
75	We evaluate this indicator in \S\ref{subsec:phase_diagram_exp}.
76	
77	\subsection{Collapse Trajectory Classification}
78	\label{subsec:phase_diagram}
79	
80	We define the \emph{collapse trajectory map} as the mapping from constant mixing ratio $r$ to the SLV trajectory over $T$ generations, classifying outcomes as \emph{collapse} (monotonic post-decompression decline), \emph{stable} (non-decreasing), or \emph{transitional} (non-monotonic after Gen~2).
81	We estimate $r_{\text{crit}}$ by identifying the lowest $r$ for which $\widetilde{S}_t \geq \widetilde{S}_{t-1}$ holds for all $t \in \{2, \ldots, T\}$.
82	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "869110b5-fb68-4097-afed-e84ac997e4c2",
  "isSidechain": true,
  "promptId": "dec2fbdd-c7f3-4693-9fb9-3b2bc1bffe68",
  "agentId": "a7d29b9da28a45754",
  "type": "user",
  "uuid": "f9435d8b-287e-41a9-81ad-536ba13e9f69",
  "sourceToolAssistantUUID": "869110b5-fb68-4097-afed-e84ac997e4c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/director_5c6b5d77",
  "sessionId": "95e103f0-69e1-4f9d-86cd-90a5f01a13b1",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glimmering-prancing-wind"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T09:27:00.979Z_

<details open><summary>🔧 Tool call — Read · `toolu_016DGKi3mBDqAzQCCoAWuGvD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9435d8b-287e-41a9-81ad-536ba13e9f69",
  "isSidechain": true,
  "agentId": "a7d29b9da28a45754",
  "requestId": "req_011CbP3mdUWRPpziLn4emb3i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ae0b2ba6-0ec7-4f85-a420-a0ab26377041",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/director_5c6b5d77",
  "sessionId": "95e103f0-69e1-4f9d-86cd-90a5f01a13b1",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glimmering-prancing-wind",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UTUfgjHguk8sygdVoorJuH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37697,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37697,
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

### Tool result

_source line 10 · 2026-05-25T09:27:00.985Z_

<details><summary>↩ Tool result · `toolu_016DGKi3mBDqAzQCCoAWuGvD`</summary>

```text
1	
2	\subsection{Experimental Setup}
3	\label{subsec:setup}
4	
5	We use the publicly released final Pythia-410M-deduped checkpoint \citep{biderman2023pythia} as our base model and fine-tune on a 50K-subset of OpenWebText.
6	Starting from the pretrained checkpoint (generation~0), each subsequent generation fine-tunes on synthetic text produced by the previous generation, for a total of 10 recursive generations.
7	At each generation we compute the spectral indicators from \S\ref{subsec:spectral_metrics} on 1K held-out last-layer embeddings, paired with three downstream metrics: perplexity, HellaSwag accuracy (0-shot), and distinct-4.
8	These three metrics (language modeling capability, natural language understanding, and generation diversity) cover the primary evaluation dimensions accessible to a 410M-parameter model.
9	Training hyperparameters and compute details are in Appendix~\ref{app:training_details}.
10	
11	For the mixing comparison (\S\ref{subsec:phase1}), we evaluate three strategies:
12	(1)~\textbf{pure collapse} ($r_t{=}0$),
13	(2)~\textbf{fixed mix} ($r_t{=}0.50$), and
14	(3)~\textbf{adaptive} ($k{=}10$, Eq.~\ref{eq:controller}).
15	To construct the collapse trajectory map (\S\ref{subsec:phase_diagram_exp}), we additionally evaluate fixed mixing at $r \in \{0.2, 0.25, 0.3\}$.
16	
17	\subsection{Spectral Collapse Characterization}
18	\label{subsec:phase0}
19	
20	Table~\ref{tab:phase0} reports spectral and downstream metrics across 10 recursive generations, which reveal a three-phase structure.
21	
22	\paragraph{Phase I: Spectral Decompression (Gen~0--2).}
23	$r_{\text{eff}}$ rises from 417.55 to 496.2 (+18.8\%) and SLV from 2366.7 to 2468.0 (+4.3\%), while $\sigma_1$ drops from 1942.8 to 718.7.
24	The peak at Gen~2 is consistent across all three seeds (Figure~\ref{fig:seed_variability}; SLV coefficient of variation (CV) $< 1.3\%$ at all generations; full per-generation statistics in Appendix Table~\ref{tab:pergen_variance}).
25	Crucially, this decompression does not indicate improved model quality: HellaSwag drops 8.0\% and distinct-4 falls 31.6\% during the same interval (Figure~\ref{fig:slv_ppl_decoupling}), and SLV computation takes ${<}\,1$\,s vs.\ ${\sim}$70\,min for benchmarks.
26	
27	\begin{figure}[t]
28	\centering
29	\includegraphics[width=\columnwidth]{figures/seed_variability.pdf}
30	\caption{Cross-seed reproducibility of SLV under pure-synthetic training ($r{=}0$). Thin lines: individual seeds (42, 43, 44); thick line: 3-seed mean; shaded band: $\pm$1 s.d. The coefficient of variation remains below 1.3\% at all generations, confirming that spectral collapse follows a deterministic trajectory.}
31	\label{fig:seed_variability}
32	\end{figure}
33	
34	\begin{figure}[t]
35	\centering
36	\includegraphics[width=\columnwidth]{figures/slv_ppl_decoupling.pdf}
37	\caption{SLV (top) and perplexity (bottom) across 10 recursive generations ($r{=}0$, 3-seed mean). In Phase~I (Gen~0--2), both metrics rise simultaneously. The SLV increase reflects distributional broadening, not model health. From Phase~III onward (Gen~4--10), the two metrics diverge: SLV declines monotonically while perplexity accelerates, which confirms that post-decompression SLV faithfully tracks structural collapse.}
38	\label{fig:slv_ppl_decoupling}
39	\end{figure}
40	
41	\paragraph{Phase II: Collapse Onset (Gen~2--4).}
42	Both $r_{\text{eff}}$ and SLV reverse after Gen~2 ($r_{\text{eff}}$: 496.2$\to$493.6, SLV: 2468$\to$2440), marking the transition from decompression to collapse while perplexity continues its monotonic rise.
43	SLV's post-peak decline is sharper than $r_{\text{eff}}$'s ($-$1.1\% vs.\ $-$0.5\% in the first post-peak generation), reflecting its sensitivity to distributed contraction across all spectral directions rather than the dominant ones alone.
44	At 1B scale, this sensitivity gap widens to a timing difference: SLV peaks one generation earlier than $r_{\text{eff}}$ (see Cross-Scale Pilot below).
45	
46	\paragraph{Phase III: Accelerating Collapse (Gen~4--10).}
47	SLV contraction accelerates: the per-generation decline averages $-$31.0 during onset (Gen~2--4) vs.\ $-$37.4 during acceleration (Gen~4--10), with 78\% of the total peak-to-final decline occurring in Phase~III (Table~\ref{tab:pergen_variance}).
48	By Gen~10, $r_{\text{eff}}$ falls to 438.1 ($-$11.7\% from peak), SLV to 2181.4 ($-$11.6\% from peak), and perplexity reaches 71.0 ($+$643\%).
49	Concurrently, $\sigma_1$ traces a U-shaped trajectory: after dropping from 1942.8 to 718.7 during decompression, it rises to 874.6 by Gen~10 (Figure~\ref{fig:spectral_trajectory}).
50	This simultaneous $\sigma_1$ recovery and $r_{\text{eff}}$ decline is a geometric signature of mode collapse: representations concentrate along fewer dominant directions while the overall occupied volume shrinks.
51	
52	\paragraph{Cross-Scale Pilot.}
53	Repeating the protocol on Pythia-1B-deduped (Gen~0--3) reproduces the decompression-onset structure: SLV rises from 2835 to 2906 at Gen~1 ($+$2.5\%) before declining to 2865 at Gen~3, while $r_{\text{eff}}$ peaks one generation later at Gen~2 (580.9 vs.\ 570.8 at Gen~1).
54	This one-generation SLV lead over $r_{\text{eff}}$ (absent at 410M, where both peak simultaneously) suggests that SLV sensitivity increases with model scale.
55	Perplexity rises monotonically throughout (8.1$\to$13.4, $+$66\%), confirming the downstream-spectral asymmetry at a second scale.
56	Full 10-generation characterization at 1B remains future work.
57	
58	\subsection{Adaptive Mixing Comparison}
59	\label{subsec:phase1}
60	
61	We evaluate the controller retrospectively by computing its signal on pre-existing fixed-ratio trajectories rather than deploying it in a closed loop; the goal is to characterize signal attenuation, not to propose operational deployment.
62	Under pure synthetic training, SLV peaks at Gen~2 (2468) and declines monotonically; with 50\% mixing, SLV rises to 2572 at Gen~10, with only a negligible Gen~1 dip ($\Delta_1 \approx 0.0005$, well below $\tau$).
63	The adaptive controller ($k{=}10$) remains silent through all ten generations.
64	Figure~\ref{fig:controller_signal} quantifies the signal attenuation: the maximum controller signal magnitude drops from 40.4 at $r{=}0$ to 3.8 at $r{=}0.2$ and reaches exactly zero at $r \geq 0.3$, confirming that even moderate mixing suffices to suppress the rate-based signal~\citep{scheffer2009ews}.
65	
66	\begin{figure}[t]
67	\centering
68	\includegraphics[width=0.85\columnwidth]{figures/controller_signal.pdf}
69	\caption{Maximum controller signal magnitude ($\max|\Delta\tilde{S}_t|$, $t \geq 2$) across mixing ratios. The signal drops $10\times$ from $r{=}0$ to $r{=}0.2$ and is exactly zero for $r \geq 0.3$ (``silent''), rendering rate-based controllers ineffective.}
70	\label{fig:controller_signal}
71	\end{figure}
72	
73	Despite sustained spectral expansion at $r{=}0.5$, downstream metrics degrade: perplexity increases 58\% and distinct-4 falls to .152 (below even pure collapse), reinforcing that spectral health does not guarantee model health.
74	
75	\subsection{Alternative EWS Comparison}
76	\label{subsec:alt_ews}
77	
78	We compare SLV against seven alternative collapse indicators from three signal sources: embedding geometry (RankMe, isotropy), attention weights (stable rank, spectral norm), and output distributions (token entropy, raw perplexity, perplexity growth rate).
79	
80	Table~\ref{tab:ews_main} summarizes the comparison under pure-synthetic training ($r{=}0$); full tabular data appear in Appendix Table~\ref{tab:ews_comparison}.
81	Only SLV and RankMe~\citep{rankme2023} exhibit a decompression peak at Gen~2 followed by monotonic decline; all other indicators change monotonically from Gen~0 and cannot distinguish collapse onset from the initial fine-tuning transient.
82	SLV's signal-to-noise ratio is 2.5$\times$ that of RankMe (11.8\% vs.\ 4.7\% relative change).
83	
84	\begin{table}[t]
85	\centering
86	\small
87	\setlength{\tabcolsep}{4pt}
88	\begin{tabular}{@{}llcc@{}}
89	\toprule
90	Indicator & Direction ($r{=}0$) & Rel $\Delta$ & Rev. \\
91	\midrule
92	SLV         & Peak G2, mono.\ $\downarrow$ & 11.8\% & \checkmark \\
93	RankMe      & Peak G2, mono.\ $\downarrow$ &  4.7\% & \checkmark \\
94	Token ent.  & Mono.\ $\downarrow$           &  9.6\% & \checkmark \\
95	Stable rank & Mono.\ $\downarrow$           & 14.0\% & \checkmark \\
96	Spec.\ norm & Mono.\ $\uparrow$            &  8.0\% & \checkmark \\
97	Isotropy    & Non-mono.\ (6 rev.)           & 75\%   & \checkmark \\
98	Raw PPL     & Mono.\ $\uparrow$            & 704\%  & $\times$ \\
99	PPL growth  & ${\sim}$Mono.\ $\downarrow$   &  ---   & \checkmark \\
100	\bottomrule
101	\end{tabular}
102	\caption{Eight EWS indicators under pure-synthetic training ($r{=}0$, Pythia-410M). \textbf{Direction}: trajectory shape (Peak G$n$ = decompression peak at generation $n$; mono.\ = monotonic post-peak or throughout). \textbf{Rel $\Delta$}: total relative change. \textbf{Rev.}: whether the indicator reverses under $r{=}0.5$ mixing. Seven of eight reverse; raw PPL is the sole exception. Full data in Appendix Table~\ref{tab:ews_comparison}.}
103	\label{tab:ews_main}
104	\end{table}
105	Seven of eight indicators reverse direction under mixing (Table~\ref{tab:ews_main}, last column); raw perplexity is the sole exception.
106	This near-universality confirms that signal attenuation is not specific to SLV: any rate-based controller will fall silent when mixing exceeds $r_{\text{crit}}$.
107	SLV is the only indicator that combines decompression-phase sensitivity, post-peak monotonicity, and sub-second computation cost; it shares a metric foundation with SIGMA's $\log\det G$ ($= 2 \times \text{SLV}$; \S\ref{sec:related}).
108	
109	\subsection{Collapse Trajectory Classification}
110	\label{subsec:phase_diagram_exp}
111	
112	We now map SLV trajectories across mixing ratios to construct the collapse trajectory map defined in \S\ref{subsec:phase_diagram}.
113	Figure~\ref{fig:phase_diagram} plots SLV across 10 recursive generations for five mixing ratios; three qualitatively distinct trajectory types emerge:
114	
115	\begin{figure}[t]
116	\centering
117	\includegraphics[width=0.92\columnwidth]{figures/phase_diagram.pdf}
118	\caption{SLV trajectories across mixing ratios (Pythia-410M; $r{=}0$, $r{=}0.2$, $r{=}0.25$, $r{=}0.3$: 3-seed mean, solid lines; $r{=}0.5$: 2-seed mean, dashed line). Type~I ($r{=}0$): decompression then monotonic collapse. Type~II ($r{=}0.2$, $r{=}0.25$): transient dip followed by recovery. Type~III ($r{=}0.3$, $r{=}0.5$): monotonic expansion from Gen~2 onward. The shaded band marks the critical threshold $r_{\text{crit}} \in (0.25, 0.3]$. The dashed horizontal line indicates the Gen~0 baseline.}
119	\label{fig:phase_diagram}
120	\end{figure}
121	
122	\paragraph{Type~I: Pure Collapse ($r{=}0$).}
123	SLV exhibits large decompression ($+$96 points at Gen~1, peaking at Gen~2) followed by accelerating contraction (\S\ref{subsec:phase0}).
124	
125	\paragraph{Type~II: Near-critical Mixing ($r{=}0.2$, $r{=}0.25$).}
126	At $r{=}0.2$, SLV dips $-7.3$ points at Gen~2 before recovering to 2467.2 at Gen~10 ($+4.3\%$ above baseline; full per-generation data in Appendix Table~\ref{tab:pergen_variance_r02}).
127	The EMA-smoothed SLV violates non-decreasing at Gen~2, placing $r{=}0.2$ below $r_{\text{crit}}$, yet the smoothed signal ($\max \Delta_t = 0.0016$, below $\tau{=}0.002$) fails to trigger the controller.
128	At $r{=}0.25$, the same pattern holds with a weaker dip ($-2.1$) and ${\sim}3\times$ weaker signal.
129	As Figure~\ref{fig:rankme_trajectories} shows, $r_{\text{eff}}$ rises monotonically for all $r \geq 0.2$, yielding only a 2-type classification (collapse vs.\ non-collapse); SLV's transient dip uniquely identifies the transitional regime.
130	
131	\begin{figure}[t]
132	\centering
133	\includegraphics[width=0.92\columnwidth]{figures/rankme_trajectories.pdf}
134	\caption{Effective rank ($r_{\mathrm{eff}}$) trajectories across mixing ratios. Unlike SLV (Figure~\ref{fig:phase_diagram}), $r_{\mathrm{eff}}$ rises monotonically for all $r \geq 0.2$, providing only a 2-type classification and failing to identify the Type~II transitional regime.}
135	\label{fig:rankme_trajectories}
136	\end{figure}
137	
138	\paragraph{Type~III: Super-critical Mixing ($r \geq 0.3$).}
139	SLV rises monotonically from Gen~2 onward.
140	At $r{=}0.3$, SLV reaches 2508.2 at Gen~10 ($+$6.0\% above baseline); at $r{=}0.5$, 2572 ($+$8.7\%).
141	The critical threshold is robust to EMA smoothing ($\alpha \in \{0.3, 0.5, 0.7\}$ all yield $r_{\text{crit}} \in (0.25, 0.3]$; Appendix Table~\ref{tab:alpha_robustness}), and the maximum SLV departure below baseline (multi-seed mean) shrinks continuously with $r$ ($-7.3$ at $r{=}0.2$, $-3.3$ at $r{=}0.25$, $-1.5$ at $r{=}0.3$), consistent with a continuous crossover.
142	$r_{\text{crit}}$ thus marks a transition in trajectory shape, not in final outcome: Type~II trajectories recover spectrally but exhibit an initial contraction transient that Type~III trajectories lack.
143	
144	\paragraph{Output Diversity Divergence.}
145	D-4 does not increase monotonically with $r$: it remains highest around $r \in \{0.2, 0.25\}$ (mean $.324$--$.342$, with high cross-seed variance s.d.\ $\approx 0.17$) before dropping to .152 at $r{=}0.5$, indicating that spectral expansion does not guarantee diversity.
146	D-4 also shows substantially higher cross-seed variance than SLV (CV $= 3.9\%$ vs.\ $0.12\%$ at $r{=}0.25$), confirming that the two metrics capture orthogonal aspects of model behavior.
147	
148	Table~\ref{tab:phase_summary} consolidates the final-generation metrics across all five mixing ratios.
149	
150	\begin{table}[t]
151	\centering
152	\small
153	\setlength{\tabcolsep}{4pt}
154	\begin{tabular}{@{}cccccccc@{}}
155	\toprule
156	$r$ & Type & SLV & $r_{\text{eff}}$ & PPL & D-4 & $\max\Delta_t$ & Gen. \\
157	\midrule
158	0    & I   & 2181.4 & 438.1 & 71.0\phantom{0} & .324 & ---   & 10 \\
159	0.20 & II  & 2467.2 & 508.1 & 13.54 & .324 & .0016 & 10 \\
160	0.25 & II  & 2488.1 & 513.8 & 13.41 & .342 & .0005 & 10 \\
161	0.30 & III & 2508.2 & 521.1 & 13.34 & .295 & 0     & 10 \\
162	0.50 & III & 2571.6 & 553.5 & 15.11 & .152 & 0     & 10 \\
163	\bottomrule
164	\end{tabular}
165	\caption{Final-generation spectral and downstream metrics across mixing ratios (all runs to Gen~10). PPL = perplexity, D-4 = distinct-4. $\max\Delta_t$ computed for $t \geq 2$, excluding the initial fine-tuning transient. Type classification follows \S\ref{subsec:phase_diagram}. $r{=}0$ reports the mean of three seeds (42, 43, 44); $r{=}0.3$ the mean of three seeds (42, 43, 44); $r{=}0.2$ the mean of three seeds (42, 43, 44); $r{=}0.5$ the mean of two seeds (42, 43); $r{=}0.25$ the mean of three seeds (42, 43, 44). D-4 exhibits high cross-seed variance at $r{=}0$ (s.d.\ $= 0.15$) and $r{=}0.3$ (s.d.\ $= 0.155$).}
166	\label{tab:phase_summary}
167	\end{table}
168	
169	\paragraph{Practical Implications.}
170	Neither second-order acceleration ($\Delta^2_t$, Eq.~\ref{eq:second_order}) nor level-based triggers resolve the attenuation problem: $\Delta^2_t$ is negative in late generations regardless of $r$, and level-based triggers fail under Type~III.
171	The trajectory map provides a direct prescription: setting $r > 0.3$ prevents spectral collapse without per-generation monitoring.
172	
173	\subsection{Cross-Architecture Validation}
174	\label{subsec:cross_arch}
175	
176	To test whether the three-phase trajectory generalizes beyond Pythia, we repeat the recursive pipeline on GPT-2-medium~\citep{radford2019language} (355M parameters, different pretraining corpus and tokenizer) under four conditions: pure synthetic ($r{=}0$, 9 generations), intermediate mixing ($r{=}0.25$ and $r{=}0.3$, 3 generations each), and a real-data control ($r{=}1.0$, 3 generations).
177	
178	\begin{table}[t]
179	\centering
180	\small
181	\setlength{\tabcolsep}{4pt}
182	\begin{tabular}{@{}cccccc@{}}
183	\toprule
184	$r$ & Type & SLV$_0$ & SLV$_{\text{end}}$ & $\Delta$SLV & Match \\
185	\midrule
186	0    & I    & 689  & 415\,(G9)  & $-$39.8\% & \checkmark \\
187	0.25 & ---  & 689  & 738\,(G3)  & $+$7.0\%  & $\dagger$ \\
188	0.30 & III  & 689  & 737\,(G3)  & $+$6.9\%  & \checkmark \\
189	1.0  & Ctrl & 689  & 813\,(G3)  & $+$17.9\% & \checkmark \\
190	\bottomrule
191	\end{tabular}
192	\caption{Cross-architecture validation on GPT-2-medium (355M, seed~42). \textbf{Match}: whether the trajectory type matches the corresponding Pythia-410M classification. $\dagger$\,Three-generation horizon does not resolve the Type~II/III distinction at this ratio.}
193	\label{tab:cross_arch}
194	\end{table}
195	
196	Under pure synthetic training, GPT-2-medium reproduces the three-phase pattern (Table~\ref{tab:cross_arch}): SLV peaks at Gen~2 (924, $+$34.1\% from baseline) and declines to 415 by Gen~9 ($-$55.1\% from peak), while perplexity rises from 15.5 to 329 ($+$2028\%).
197	The $\sigma_1$ trajectory follows the same U-shape (6598$\to$1191 during decompression, rising to ${\sim}$1570 by Gen~9), confirming that dominant-direction reconcentration under falling effective rank is architecture-independent.
198	The collapse magnitude is substantially larger than Pythia's ($-$55.1\% vs.\ $-$11.6\% SLV decline), reflecting GPT-2-medium's more anisotropic initial spectrum ($r_{\text{eff}}{=}23$ vs.\ Pythia's 418).
199	
200	The real-data control ($r{=}1.0$) shows monotonic expansion with perplexity \emph{decreasing} ($-$27.4\%), which confirms that collapse is specific to recursive synthetic training.
201	
202	At intermediate ratios ($r{=}0.25$, $r{=}0.3$), both conditions reproduce the decompression phase (Gen~0$\to$1: SLV $+$7.5--8.5\%, $r_{\text{eff}}$ from 23 to 136--142, $\sigma_1$ $-$80--82\%) and stabilize through Gen~3, with EMA-smoothed SLV monotonically non-decreasing.
203	At $r{=}0.3$ this matches Pythia's Type~III classification.
204	At $r{=}0.25$, the three-generation window does not resolve the Type~II/III distinction, since Pythia's characteristic EMA dip appears only at Gen~5+; the trajectory is consistent with the Pythia-410M phase boundary but does not independently confirm $r_{\text{crit}}$ for this architecture.
205	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae0b2ba6-0ec7-4f85-a420-a0ab26377041",
  "isSidechain": true,
  "promptId": "dec2fbdd-c7f3-4693-9fb9-3b2bc1bffe68",
  "agentId": "a7d29b9da28a45754",
  "type": "user",
  "uuid": "4cea6048-2b4c-4a97-899b-9be1d5223b4c",
  "sourceToolAssistantUUID": "ae0b2ba6-0ec7-4f85-a420-a0ab26377041",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/director_5c6b5d77",
  "sessionId": "95e103f0-69e1-4f9d-86cd-90a5f01a13b1",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glimmering-prancing-wind"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-25T09:27:01.182Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AxoWHP7iR1PMSG5QQD3Cxr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cea6048-2b4c-4a97-899b-9be1d5223b4c",
  "isSidechain": true,
  "agentId": "a7d29b9da28a45754",
  "requestId": "req_011CbP3mdUWRPpziLn4emb3i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "92b5d7b1-dc20-4e29-baf0-de219677e41e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/director_5c6b5d77",
  "sessionId": "95e103f0-69e1-4f9d-86cd-90a5f01a13b1",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glimmering-prancing-wind",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UTUfgjHguk8sygdVoorJuH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37697,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37697,
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

### Tool result

_source line 12 · 2026-05-25T09:27:01.188Z_

<details><summary>↩ Tool result · `toolu_01AxoWHP7iR1PMSG5QQD3Cxr`</summary>

```text
1	\begin{figure}[t]
2	\centering
3	\includegraphics[width=\columnwidth]{figures/pipeline_overview.pdf}
4	\caption{Experimental pipeline. Each generation fine-tunes on synthetic text mixed with real data at ratio $r_t$. Spectral monitoring extracts last-layer embeddings from held-out data, computes SVD, and derives SLV, $r_{\text{eff}}$, and $\sigma_1$. A proportional controller (dashed) can adjust $r_{t+1}$ based on the SLV rate of change. The three phases---decompression (I), onset (II), and acceleration (III)---are annotated along the generation axis.}
5	\label{fig:pipeline}
6	\end{figure}
7	
8	\paragraph{Model Collapse.}
9	\citet{shumailov2024collapse} showed that recursive training on model-generated data progressively erodes distributional tails (\emph{model collapse}).
10	Scaling laws predict tail erosion as a function of recursive depth~\citep{dohmatob2024tails, dohmatob2024demystified, seddik2024synthetic}; the self-consuming loop accelerates collapse even under data accumulation~\citep{alemohammad2024mad}, with as little as 1\% synthetic contamination sufficing~\citep{dohmatob2025strong}, though preserving all prior data can delay it~\citep{gerstgrasser2024inevitable}; mitigations include self-verification~\citep{fu2025selfverification} and weak non-synthetic data~\citep{amin2025escaping}.
11	We complement these output-based diagnoses by tracking collapse through the spectral geometry of internal representations.
12	
13	\paragraph{Spectral Analysis of Representations.}
14	Random matrix theory reveals implicit regularization in neural network eigenspectra~\citep{martin2021implicit}; effective rank~\citep{roy2007effectiverank} and RankMe~\citep{rankme2023} quantify representational dimensionality.
15	\citet{he2025spectral} linked spectral collapse to plasticity loss in continual learning, and \citet{naderi2025mindgap} identified rank collapse in attention matrices.
16	Most directly relevant, \citet{gu2026sigma} proposed SIGMA, tracking singular-value distributions during recursive training on OPT-125M over three generations.
17	Our SLV equals half of SIGMA's $\log\det G$; we extend SIGMA in \emph{scale} (Pythia-410M/1B, 3--8$\times$ larger), \emph{temporal depth} (10 vs.\ 3 generations), and \emph{methodology} (SLV-based mixing control).
18	Table~\ref{tab:related_comparison} summarizes the positioning.
19	
20	\begin{table}[t]
21	\centering
22	\small
23	\setlength{\tabcolsep}{3pt}
24	\begin{tabular}{@{}lccc@{}}
25	\toprule
26	& \textbf{SIGMA} & \textbf{He+ '25} & \textbf{This work} \\
27	\midrule
28	Setting & Recursive & Continual & Recursive \\
29	Scale & 125M & Various & 355M--1B \\
30	Generations & 3 & --- & 10 \\
31	Spectral metric & $\log\det G$ & spec.\ norm & SLV \\
32	Phase typology & --- & --- & \checkmark \\
33	Mixing / $r_{\text{crit}}$ & --- & --- & \checkmark \\
34	Controller & --- & --- & \checkmark \\
35	\bottomrule
36	\end{tabular}
37	\caption{Positioning relative to recent spectral-collapse studies. SLV $\equiv \tfrac{1}{2}\log\det G$. SIGMA: \citet{gu2026sigma}; He+: \citet{he2025spectral}.}
38	\label{tab:related_comparison}
39	\end{table}
40	
41	\paragraph{Early Warning Signals and Critical Transitions.}
42	EWS for critical transitions originate in ecology, where rising autocorrelation and variance precede regime shifts~\citep{scheffer2009ews, scheffer2012anticipating}, with methods from statistical tests~\citep{dakos2012methods} to deep learning~\citep{bury2021deeplearning}.
43	A central tension is that stabilization interventions suppress the precursors they rely on~\citep{scheffer2009ews}; we encounter a stronger form where real-data mixing reverses the spectral trajectory entirely (\S\ref{subsec:controller}).
44	
45	\paragraph{Data Mixing for LLM Training.}
46	Data composition significantly affects LM quality~\citep{longpre2024pretrainer, muennighoff2023scaling}, and several methods optimize domain mixtures~\citep{xie2023doremi, ye2025mixinglaws, chen2025aioli}, but evaluate mixing through loss or benchmarks.
47	Our work reveals that real-vs-synthetic mixing reshapes the spectral geometry of representations, producing a trajectory map that loss-based metrics do not capture.
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92b5d7b1-dc20-4e29-baf0-de219677e41e",
  "isSidechain": true,
  "promptId": "dec2fbdd-c7f3-4693-9fb9-3b2bc1bffe68",
  "agentId": "a7d29b9da28a45754",
  "type": "user",
  "uuid": "937686d0-aa96-4fc2-8480-2e8c3994e59d",
  "sourceToolAssistantUUID": "92b5d7b1-dc20-4e29-baf0-de219677e41e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/director_5c6b5d77",
  "sessionId": "95e103f0-69e1-4f9d-86cd-90a5f01a13b1",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glimmering-prancing-wind"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-25T09:27:01.393Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Thace1qvdjFJZmZ8sn9XJk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "937686d0-aa96-4fc2-8480-2e8c3994e59d",
  "isSidechain": true,
  "agentId": "a7d29b9da28a45754",
  "requestId": "req_011CbP3mdUWRPpziLn4emb3i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "eeec41e2-80b0-49ed-888d-a92129699c2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/director_5c6b5d77",
  "sessionId": "95e103f0-69e1-4f9d-86cd-90a5f01a13b1",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glimmering-prancing-wind",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UTUfgjHguk8sygdVoorJuH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37697,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37697,
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

### Tool result

_source line 14 · 2026-05-25T09:27:01.400Z_

<details><summary>↩ Tool result · `toolu_01Thace1qvdjFJZmZ8sn9XJk`</summary>

```text
1	
2	The spectral decompression phase reflects fine-tuning's redistribution of variance: early recursive training compresses the dominant singular direction while inflating subordinate ones, resembling isotropy regularization~\citep{ethayarajh2019contextual} reversed by recursive amplification.
3	That downstream performance degrades during this expansion confirms these indicators are collapse detectors, not quality measures.
4	SLV and perplexity are complementary: perplexity rises monotonically from Gen~0; SLV provides mechanistic diagnosis by distinguishing volume contraction from distributional broadening.
5	
6	A key finding is the prevention--detectability tradeoff: real-data mixing reverses the spectral trajectory entirely, and the controller signal drops $10\times$ from $r{=}0$ to $r{=}0.2$ and vanishes at $r \geq 0.3$, leaving no regime where prevention and detection coexist.
7	Our analysis identifies SLV as a cheap spectral indicator, reveals a reproducible three-phase collapse trajectory, and exposes the signal attenuation that limits reactive controllers.
8	The trajectory map localizes $r_{\text{crit}} \in (0.25, 0.3]$; setting $r > r_{\text{crit}}$ prevents collapse without per-generation monitoring, with cross-architecture support from GPT-2-medium and preliminary scale evidence from Pythia-1B.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eeec41e2-80b0-49ed-888d-a92129699c2b",
  "isSidechain": true,
  "promptId": "dec2fbdd-c7f3-4693-9fb9-3b2bc1bffe68",
  "agentId": "a7d29b9da28a45754",
  "type": "user",
  "uuid": "7bb62c37-e301-49e9-a2ff-1575cd925fdd",
  "sourceToolAssistantUUID": "eeec41e2-80b0-49ed-888d-a92129699c2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/director_5c6b5d77",
  "sessionId": "95e103f0-69e1-4f9d-86cd-90a5f01a13b1",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glimmering-prancing-wind"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-25T09:27:01.605Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KSiDeAve8dowHLC4dKFWM6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bb62c37-e301-49e9-a2ff-1575cd925fdd",
  "isSidechain": true,
  "agentId": "a7d29b9da28a45754",
  "requestId": "req_011CbP3mdUWRPpziLn4emb3i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a1af40ee-7cf7-4239-ab11-2613128df3f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/director_5c6b5d77",
  "sessionId": "95e103f0-69e1-4f9d-86cd-90a5f01a13b1",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glimmering-prancing-wind",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UTUfgjHguk8sygdVoorJuH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37697,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37697,
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

### Tool result

_source line 16 · 2026-05-25T09:27:01.615Z_

<details><summary>↩ Tool result · `toolu_01KSiDeAve8dowHLC4dKFWM6`</summary>

```text
1	\section{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Scale and Scope.}
5	We validate at two model scales (Pythia-410M and a 1B pilot through Gen~3) with all spectral metrics computed from last-layer embeddings only; intermediate layers may exhibit different dynamics.
6	The 1B pilot confirms the decompression peak but is insufficient to characterize full acceleration or estimate $r_{\text{crit}}$ at that scale.
7	All fine-tuning uses a single domain (OpenWebText, English web text); spectral collapse dynamics may differ for code, multilingual, or domain-specific corpora.
8	
9	\paragraph{Temporal Horizon.}
10	Ten recursive generations may be shorter than production pipelines.
11	Type~II (transitional) trajectories may eventually revert to collapse at longer horizons, which would shift $r_{\text{crit}}$ upward.
12	The proportional controller uses a single gain $k$ without integral or derivative terms; a more sophisticated design might partially mitigate signal attenuation.
13	
14	\paragraph{Generalization.}
15	Signal attenuation may extend to implicit-loop settings where web corpora contain model-generated content, but validating this requires controlled experiments with web-scale data.
16	Our use of AI coding and writing assistants is disclosed in Appendix~\ref{app:ai-assistants}.
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1af40ee-7cf7-4239-ab11-2613128df3f8",
  "isSidechain": true,
  "promptId": "dec2fbdd-c7f3-4693-9fb9-3b2bc1bffe68",
  "agentId": "a7d29b9da28a45754",
  "type": "user",
  "uuid": "0e139eba-2ea8-4878-8579-f8971cd52e5c",
  "sourceToolAssistantUUID": "a1af40ee-7cf7-4239-ab11-2613128df3f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/director_5c6b5d77",
  "sessionId": "95e103f0-69e1-4f9d-86cd-90a5f01a13b1",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glimmering-prancing-wind"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-25T09:27:01.764Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Y2gUu9obfyY76bV9xXLZCB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e139eba-2ea8-4878-8579-f8971cd52e5c",
  "isSidechain": true,
  "agentId": "a7d29b9da28a45754",
  "requestId": "req_011CbP3mdUWRPpziLn4emb3i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ddddc9ea-4b65-46f5-8d03-976cc7874066",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/director_5c6b5d77",
  "sessionId": "95e103f0-69e1-4f9d-86cd-90a5f01a13b1",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glimmering-prancing-wind",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UTUfgjHguk8sygdVoorJuH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37697,
      "cache_read_input_tokens": 0,
      "output_tokens": 622,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 37697
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 622,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 37697,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 37697,
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

_source line 18 · 2026-05-25T09:27:01.774Z_

<details><summary>↩ Tool result · `toolu_01Y2gUu9obfyY76bV9xXLZCB`</summary>

```text
1	
2	\section{Alternative EWS Indicator Details}
3	\label{app:ews_details}
4	
5	Table~\ref{tab:ews_comparison} provides full tabular data for the eight alternative early warning indicators compared in \S\ref{subsec:alt_ews}.
6	
7	\begin{table}[H]
8	\centering
9	\small
10	\setlength{\tabcolsep}{4pt}
11	\begin{tabular}{@{}llcccc@{}}
12	\toprule
13	Indicator & Source & Peak & Mono. & Rel $\Delta$ & Rev. \\
14	\midrule
15	SLV         & emb-SVD   & Gen 2 & \checkmark & 11.8\% & \checkmark \\
16	RankMe      & emb-SVD   & Gen 2 & \checkmark &  4.7\% & \checkmark \\
17	Token ent.  & logit     & ---   & \checkmark &  9.6\% & \checkmark \\
18	Stable rank & attn wt.  & ---   & \checkmark & 14.0\% & \checkmark \\
19	Spec.\ norm & attn wt.  & ---   & \checkmark &  8.0\% & \checkmark \\
20	Isotropy    & emb       & ---   & $\times$\,(6) & 75\%   & \checkmark \\
21	Raw PPL     & eval      & ---   & \checkmark & 704\%  & $\times$ \\
22	PPL growth  & ppl       & ---   & $\sim$\,(1) &  ---   & \checkmark \\
23	\bottomrule
24	\end{tabular}
25	\caption{Alternative early warning indicators under pure-synthetic training ($r{=}0$, seed 42, Pythia-410M, 10 gen). \textbf{Peak}: generation at which the indicator reverses (--- = monotonic from Gen~0). \textbf{Mono.}: post-peak monotonicity (\checkmark\ = yes; number = violations). \textbf{Rel $\Delta$}: magnitude of total relative change; for peaked indicators (SLV, RankMe), computed as $|v_{10} - v_{\text{peak}}|/|v_{\text{peak}}|$; for monotonic indicators, $|v_{10} - v_0|/|v_0|$. \textbf{Rev.}: direction reversal under $r{=}0.5$ mixing (\checkmark\ = reversed). Note: Raw PPL Rel~$\Delta$ is 704\% for seed~42; the main text reports 643\% (3-seed mean).}
26	\label{tab:ews_comparison}
27	\end{table}
28	
29	\section{Per-Generation Cross-Seed Variance}
30	\label{app:pergen_variance}
31	
32	Table~\ref{tab:pergen_variance} reports all six metrics at every generation under pure-synthetic training ($r{=}0$), with mean and sample standard deviation across three seeds (42, 43, 44).
33	Spectral metrics ($r_{\text{eff}}$, SLV, $\sigma_1$) exhibit low cross-seed variance throughout the trajectory (SLV coefficient of variation $< 1.3\%$ at all generations), confirming that spectral collapse follows a deterministic geometric trajectory.
34	In contrast, D-4 variance increases sharply after Gen~5, reaching a coefficient of variation of 46\% at Gen~10, consistent with the stochastic nature of n-gram diversity under progressive mode collapse.
35	
36	\begin{table*}[!htb]
37	\centering
38	\small
39	\caption{Per-generation metrics under pure-synthetic training ($r{=}0$, Pythia-410M, mean$_{\pm\text{s.d.}}$ across seeds 42, 43, 44). Gen~0 shares a single pretrained checkpoint; D-4 variance at Gen~0 reflects generation sampling. Bold marks the spectral peak.}
40	\label{tab:pergen_variance}
41	\setlength{\tabcolsep}{4pt}
42	\begin{tabular}{@{}ccccccc@{}}
43	\toprule
44	Gen & $r_{\text{eff}}$ & SLV & PPL & HeSw & D-4 & $\sigma_1$ \\
45	\midrule
46	 0 & 417.5$_{\pm0.0}$ & 2366.7$_{\pm0.0}$ & 9.55$_{\pm0.00}$ & .413$_{\pm.000}$ & .738$_{\pm.006}$ & 1942.8$_{\pm0.0}$ \\
47	 1 & 491.1$_{\pm0.6}$ & 2462.3$_{\pm2.7}$ & 11.37$_{\pm0.01}$ & .390$_{\pm.001}$ & .609$_{\pm.014}$ & 808.9$_{\pm5.4}$ \\
48	 2 & \textbf{496.2}$_{\pm0.3}$ & \textbf{2468.0}$_{\pm1.7}$ & 13.56$_{\pm0.02}$ & .380$_{\pm.004}$ & .505$_{\pm.011}$ & 718.7$_{\pm7.0}$ \\
49	 3 & 493.6$_{\pm0.4}$ & 2440.4$_{\pm2.0}$ & 16.23$_{\pm0.02}$ & .367$_{\pm.005}$ & .465$_{\pm.033}$ & 708.7$_{\pm7.5}$ \\
50	 4 & 487.8$_{\pm1.9}$ & 2406.0$_{\pm2.0}$ & 19.90$_{\pm0.09}$ & .354$_{\pm.003}$ & .419$_{\pm.047}$ & 722.9$_{\pm6.9}$ \\
51	 5 & 479.8$_{\pm0.5}$ & 2366.0$_{\pm3.8}$ & 24.50$_{\pm0.17}$ & .341$_{\pm.003}$ & .412$_{\pm.053}$ & 749.2$_{\pm7.1}$ \\
52	 6 & 472.4$_{\pm0.6}$ & 2326.1$_{\pm8.6}$ & 30.40$_{\pm0.45}$ & .329$_{\pm.004}$ & .402$_{\pm.067}$ & 764.6$_{\pm5.7}$ \\
53	 7 & 464.1$_{\pm0.2}$ & 2293.2$_{\pm10.2}$ & 37.82$_{\pm0.94}$ & .319$_{\pm.000}$ & .375$_{\pm.082}$ & 788.4$_{\pm4.0}$ \\
54	 8 & 455.8$_{\pm1.1}$ & 2246.1$_{\pm7.4}$ & 46.90$_{\pm2.41}$ & .311$_{\pm.005}$ & .337$_{\pm.137}$ & 806.4$_{\pm8.0}$ \\
55	 9 & 446.6$_{\pm2.1}$ & 2210.4$_{\pm23.1}$ & 58.56$_{\pm4.52}$ & .301$_{\pm.003}$ & .316$_{\pm.148}$ & 841.1$_{\pm23.6}$ \\
56	10 & 438.1$_{\pm4.8}$ & 2181.4$_{\pm28.3}$ & 70.99$_{\pm5.56}$ & .296$_{\pm.006}$ & .324$_{\pm.150}$ & 874.6$_{\pm44.2}$ \\
57	\bottomrule
58	\end{tabular}
59	\end{table*}
60	
61	Table~\ref{tab:pergen_variance_r02} provides the same breakdown under transitional mixing ($r{=}0.2$), where D-4 variance is the dominant source of cross-seed disagreement.
62	
63	\begin{table*}[!htb]
64	\centering
65	\small
66	\caption{Per-generation metrics under transitional mixing ($r{=}0.2$, Pythia-410M, mean$_{\pm\text{s.d.}}$ across seeds 42, 43, 44). Gen~0 shares a single pretrained checkpoint; D-4 variance at Gen~0 reflects generation sampling. HellaSwag was not evaluated for mixing experiments.}
67	\label{tab:pergen_variance_r02}
68	\setlength{\tabcolsep}{5pt}
69	\begin{tabular}{@{}cccccc@{}}
70	\toprule
71	Gen & $r_{\text{eff}}$ & SLV & PPL & D-4 & $\sigma_1$ \\
72	\midrule
73	 0 & 417.5$_{\pm0.0}$ & 2366.7$_{\pm0.0}$ & 9.55$_{\pm0.00}$ & .738$_{\pm.006}$ & 1942.8$_{\pm0.0}$ \\
74	 1 & 476.2$_{\pm0.8}$ & 2367.4$_{\pm2.1}$ & 10.28$_{\pm0.00}$ & .671$_{\pm.015}$ & 961.8$_{\pm1.1}$ \\
75	 2 & 481.7$_{\pm1.4}$ & 2359.4$_{\pm1.5}$ & 10.74$_{\pm0.01}$ & .519$_{\pm.037}$ & 879.2$_{\pm10.3}$ \\
76	 3 & 486.7$_{\pm0.3}$ & 2364.6$_{\pm1.8}$ & 11.14$_{\pm0.01}$ & .471$_{\pm.006}$ & 811.9$_{\pm9.6}$ \\
77	 4 & 489.6$_{\pm0.6}$ & 2377.9$_{\pm1.2}$ & 11.49$_{\pm0.00}$ & .429$_{\pm.026}$ & 779.2$_{\pm9.2}$ \\
78	 5 & 492.6$_{\pm0.5}$ & 2396.8$_{\pm1.8}$ & 11.83$_{\pm0.00}$ & .420$_{\pm.037}$ & 748.8$_{\pm9.3}$ \\
79	 6 & 495.5$_{\pm1.2}$ & 2417.7$_{\pm10.5}$ & 12.17$_{\pm0.02}$ & .413$_{\pm.070}$ & 749.7$_{\pm22.5}$ \\
80	 7 & 496.7$_{\pm1.2}$ & 2429.0$_{\pm6.4}$ & 12.49$_{\pm0.05}$ & .379$_{\pm.096}$ & 750.9$_{\pm30.6}$ \\
81	 8 & 499.8$_{\pm2.3}$ & 2442.4$_{\pm10.3}$ & 12.82$_{\pm0.12}$ & .365$_{\pm.119}$ & 753.9$_{\pm23.4}$ \\
82	 9 & 503.8$_{\pm1.2}$ & 2456.0$_{\pm6.3}$ & 13.18$_{\pm0.18}$ & .349$_{\pm.143}$ & 738.1$_{\pm37.6}$ \\
83	10 & 508.1$_{\pm2.8}$ & 2467.2$_{\pm12.0}$ & 13.54$_{\pm0.25}$ & .324$_{\pm.171}$ & 722.7$_{\pm26.6}$ \\
84	\bottomrule
85	\end{tabular}
86	\end{table*}
87	
88	\section{Controller Signal Sensitivity to EMA Smoothing Parameter}
89	\label{app:alpha_robustness}
90	
91	\begin{table}[H]
92	\centering
93	\small
94	\setlength{\tabcolsep}{5pt}
95	\begin{tabular}{@{}cccccc@{}}
96	\toprule
97	$\alpha$ & $r{=}0$ & $r{=}0.2$ & $r{=}0.25$ & $r{=}0.3$ & $r{=}0.5$ \\
98	\midrule
99	0.3 & .0141 & .0009 & .0003 & 0 & 0 \\
100	0.5 & .0171 & .0016 & .0005 & 0 & 0 \\
101	0.7 & .0183 & .0023 & .0005 & 0 & 0 \\
102	\bottomrule
103	\end{tabular}
104	\caption{Normalized maximum controller signal magnitude ($\max|\Delta\tilde{S}_t| / \tilde{S}_t$, $t \geq 2$) across mixing ratios and EMA smoothing parameters. The critical threshold $r_{\text{crit}} \in (0.25, 0.3]$ is invariant to $\alpha$: signal is exactly zero for $r \geq 0.3$ at all three smoothing values, confirming that the phase boundary is a structural property of the trajectory rather than an artifact of smoothing.}
105	\label{tab:alpha_robustness}
106	\end{table}
107	
108	\section{Training and Compute Details}
109	\label{app:training_details}
110	
111	Fine-tuning uses AdamW (lr $5 \times 10^{-5}$, weight decay 0.01, linear warmup 5\%, effective batch size 32) for one epoch per generation, with gradient clipping at max norm 1.0.
112	Synthetic text is generated with temperature 1.0, top-$k{=}50$, max length 512.
113	All experiments run on NVIDIA RTX PRO 6000 GPUs (96\,GB); each 10-generation pipeline requires 15--26 single-GPU hours depending on the mixing ratio, totaling approximately 220 GPU-hours across all reported experiments.
114	
115	\section{Use of AI Assistants}
116	\label{app:ai-assistants}
117	
118	We used Claude (Anthropic) as an AI coding and writing assistant
119	throughout this work. Specifically:
120	\begin{itemize}
121	    \item \textbf{Code:} drafting experiment scripts, data-processing
122	    pipelines, and analysis utilities; debugging and refactoring.
123	    \item \textbf{Writing:} drafting and revising paper sections,
124	    polishing prose, and reformatting \LaTeX{}.
125	    \item \textbf{Literature:} summarizing related papers to inform
126	    the related-work section.
127	\end{itemize}
128	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ddddc9ea-4b65-46f5-8d03-976cc7874066",
  "isSidechain": true,
  "promptId": "dec2fbdd-c7f3-4693-9fb9-3b2bc1bffe68",
  "agentId": "a7d29b9da28a45754",
  "type": "user",
  "uuid": "2d9a7307-51dc-4d77-bc81-ee618e0ae8c7",
  "sourceToolAssistantUUID": "ddddc9ea-4b65-46f5-8d03-976cc7874066",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/director_5c6b5d77",
  "sessionId": "95e103f0-69e1-4f9d-86cd-90a5f01a13b1",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glimmering-prancing-wind"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-25T09:27:20.193Z_

Now I'll analyze all the files I've read for em-dashes (---), en-dashes (--) outside number ranges, and AI-style writing patterns.

## COMPREHENSIVE ANALYSIS OF LaTeX FILES

### 1. **abstract.tex**
**Em-dashes (---) in prose:** 0
**En-dashes (--) outside ranges:** 0
**Prose dashes found:** None

### 2. **introduction.tex**
**Em-dashes (---) in prose:** 0
**En-dashes (--) outside ranges:** 1

**Line 4:** `"~\citep{shumailov2024collapse, dohmatob2024tails, dohmatob2024demystified, alemohammad2024mad}."`
- This line contains no improper dashes in prose.

Actual finding:
**Line 20:** `"collapse pattern (Figure~\ref{fig:spectral_trajectory}): spectral decompression (Gen~0--2), where effective rank...and accelerating collapse (Gen~4--10)."`
- Two en-dashes here: `0--2` and `4--10` are NUMBER RANGES (acceptable use)

**AI-style patterns found:**
- Line 20: "revealing dynamics invisible in prior short-horizon studies" (somewhat verbose phrasing)
- Line 22: "the rate-based spectral signal degrades continuously" (repeated "signal" usage)

### 3. **method.tex**
**Em-dashes (---) in prose:** 0
**En-dashes (--) outside ranges:** 0

**All dashes checked:**
- Line 14: `0.98` (not a dash)
- Line 22: "rising $\sigma_1$ under falling" (not a dash)
- Line 64: `Gen~2--10` is a NUMBER RANGE (acceptable)
- Line 81: "identify the lowest $r$" (not a dash)

### 4. **experiments.tex**
**Em-dashes (---) in prose:** 1

**LINE 99, Table tab:ews_main:**
```
PPL growth  & ${\sim}$Mono.\ $\downarrow$   &  ---   & \checkmark \\
```
The `---` here appears in a TABLE CELL as a placeholder for empty data, NOT in running prose. This is acceptable.

**En-dashes (--) outside ranges:** 3 PROBLEMATIC INSTANCES

**LINE 22:** `"Phase~I: Spectral Decompression (Gen~0--2)."`
- `0--2` = NUMBER RANGE (acceptable)

**LINE 25:** `"Crucially, this decompression does not indicate improved model quality: HellaSwag drops 8.0\% and distinct-4 falls 31.6\% during the same interval (Figure~\ref{fig:slv_ppl_decoupling}), and SLV computation takes ${<}\,1$\,s vs.\ ${\sim}$70\,min for benchmarks."`
- No improper dashes here

**LINE 37:** `"In Phase~I (Gen~0--2), both metrics rise simultaneously. The SLV increase reflects distributional broadening, not model health. From Phase~III onward (Gen~4--10), the two metrics diverge: SLV declines monotonically while perplexity accelerates, which confirms that post-decompression SLV faithfully tracks structural collapse."`
- `0--2` and `4--10` are NUMBER RANGES (acceptable)

**LINE 41:** `"Phase~II: Collapse Onset (Gen~2--4)."`
- `2--4` is NUMBER RANGE (acceptable)

**LINE 64:** `"Gen~2--10 for Pythia-410M on OpenWebText."`
- NUMBER RANGE (acceptable)

**AI-style patterns found:**
- Line 25: "Crucially, this decompression does not indicate" - Use of "Crucially" (flagged term)
- Line 47: "SLV contraction accelerates" (acceptable technical language)

### 5. **related_work.tex**
**Em-dashes (---) in prose:** 0
**En-dashes (--) outside ranges:** 0

**AI-style patterns found:**
- Line 16: "Most directly relevant, \citet{gu2026sigma} proposed SIGMA" (acceptable)
- Line 17: "Our SLV equals half of SIGMA's...we extend SIGMA in \emph{scale}" (acceptable technical language)

### 6. **conclusion.tex**
**Em-dashes (---) in prose:** 0
**En-dashes (--) outside ranges:** 1 PROBLEMATIC

**LINE 6:** `"A key finding is the prevention--detectability tradeoff: real-data mixing reverses the spectral trajectory entirely..."`
- HERE: `prevention--detectability` - This is an en-dash `--` used to separate two compound terms in prose (AI-style hyphen usage). Should be either a hyphen `-` for a compound adjective or proper em-dash spacing.

### 7. **limitations.tex**
**Em-dashes (---) in prose:** 0
**En-dashes (--) outside ranges:** 0

No problematic dashes found.

### 8. **appendix.tex**
**Em-dashes (---) in prose:** 0
**En-dashes (--) outside ranges:** 0

All dashes are either in table cells as placeholders or in acceptable number ranges.

---

## SUMMARY REPORT

### Critical Findings:

**Em-dashes (---) in running prose:** 0 instances found across all files. ✓

**Problematic en-dashes (--) outside number ranges:** 1 instance found
1. **conclusion.tex, Line 6:** `"prevention--detectability tradeoff"` - en-dash between compound terms should use a proper hyphen or em-dash

**AI-style writing patterns detected:**

| Pattern | Location | Count |
|---------|----------|-------|
| "Crucially" | experiments.tex, Line 25 | 1 |
| Excessive compound phrases | Various | Minimal |
| "Most directly relevant" | related_work.tex | Acceptable phrasing |
| Semicolons in prose | Minimal usage | Acceptable |

### Overall Assessment:
The paper is generally well-formatted with proper LaTeX dash usage. The files contain minimal AI-writing artifacts. The one problematic en-dash usage in conclusion.tex (`prevention--detectability`) should be corrected to either `prevention-detectability` (hyphen for compound adjective) or reformatted with proper em-dash syntax. The single instance of "Crucially" is a minor concern but acceptable in academic prose.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d9a7307-51dc-4d77-bc81-ee618e0ae8c7",
  "isSidechain": true,
  "agentId": "a7d29b9da28a45754",
  "requestId": "req_011CbP3muasfKH7dvHBq1LuB",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d2ec713a-9dc6-4ec8-896e-fbe02f5e9c5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/.claude/sessions/director_5c6b5d77",
  "sessionId": "95e103f0-69e1-4f9d-86cd-90a5f01a13b1",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glimmering-prancing-wind",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018EBvzpiETNeijfBriX5jKy",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 18956,
      "cache_read_input_tokens": 37697,
      "output_tokens": 1614,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18956
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1614,
          "cache_read_input_tokens": 37697,
          "cache_creation_input_tokens": 18956,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18956,
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
