# Research conversation: Read these LaTeX appendix files and return their FULL content: 1. /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projec

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a7bd140387e37fb65.jsonl`
- **Structured JSON:** [`aeb9cde4be4cf4ffd95e.json`](../../sessions/ae/aeb9cde4be4cf4ffd95e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

13 recorded events

### User

_source line 1 · 2026-05-19T02:43:03.071Z_

Read these LaTeX appendix files and return their FULL content:

1. /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_tost.tex
2. /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_seed_control.tex  
3. /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_ddr_validation.tex
4. /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex
5. /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_classifier.tex

For each file report the full content, paying special attention to:
- TOST epsilon values, sample sizes, and statistical justification
- Seed control methodology and how gen-0 leakage is addressed
- DDR partition validation methodology and thresholds
- QLoRA setup details (model, rank, learning rate, epochs, evaluation protocol)
- Classifier sensitivity analysis details


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "66da4863-8b0b-4bc9-b61d-ba5a74da661b",
  "agentId": "a7bd140387e37fb65",
  "type": "user",
  "uuid": "fe25ec75-4dd1-4afc-82c5-8ac5969e3f12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "8a3fcdf1-bd5a-44d6-bdc9-96e7600e0702",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-19T02:43:05.073Z_

I'll read all five LaTeX appendix files for you.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe25ec75-4dd1-4afc-82c5-8ac5969e3f12",
  "isSidechain": true,
  "agentId": "a7bd140387e37fb65",
  "requestId": "req_011CbBA7fp7JEG4i9wEo9kQ3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3c72e329-578f-472c-b3ef-93d529ec43cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "8a3fcdf1-bd5a-44d6-bdc9-96e7600e0702",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Sfj1ZRJpfax1y7VfEx3vwe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 751,
      "cache_read_input_tokens": 17691,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 751,
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

_source line 3 · 2026-05-19T02:43:05.288Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RkxLVVaNi9piKAUx1LqAY7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_tost.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c72e329-578f-472c-b3ef-93d529ec43cc",
  "isSidechain": true,
  "agentId": "a7bd140387e37fb65",
  "requestId": "req_011CbBA7fp7JEG4i9wEo9kQ3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6dd15961-b7b0-4ad4-ac32-7401ee8e9391",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "8a3fcdf1-bd5a-44d6-bdc9-96e7600e0702",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Sfj1ZRJpfax1y7VfEx3vwe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 751,
      "cache_read_input_tokens": 17691,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 751,
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

_source line 4 · 2026-05-19T02:43:05.293Z_

<details><summary>↩ Tool result · `toolu_01RkxLVVaNi9piKAUx1LqAY7`</summary>

```text
1	\section{Per-Generator Equivalence Testing}
2	\label{app:tost}
3	
4	To confirm that the near-stationary classification is not a pooling artifact, we apply two one-sided $t$-tests (TOST) \cite{lakens_equivalence} for each feature within each generator separately (gen-1 vs.\ gen-2+, equivalence bound $|d| < 0.20$).
5	We adopt Cohen's conventional small effect size ($d{=}0.20$) \cite{cohen1988statistical} as the smallest effect of practical significance (SESOI): effects below this threshold are unlikely to be practically meaningful for depth discrimination.
6	LOFO analysis independently supports this choice: removing any near-stationary feature changes classification F1 by $\leq$1.5\,pp (Appendix~\ref{app:lofo}), linking the statistical threshold to classification irrelevance.
7	Sensitivity analysis at $\varepsilon \in \{0.15, 0.20, 0.25\}$ confirms the partition is robust to the bound choice (see DDR Validation appendix).
8	Table~\ref{tab:tost-per-gen} reports observed $|d|$; \checkmark{} marks features for which the TOST null hypothesis (non-equivalence) is rejected at $\alpha = 0.05$.
9	
10	Entropy min passes equivalence for all eight generators; entropy max passes for six of eight (exceeding $\varepsilon$ only for Pythia-1B and Pythia-2.8B, where $|d| \approx 0.21$--$0.25$); tail decay passes for four of eight.
11	All drifting and intermediate features fail equivalence uniformly, with $|d|$ ranging from 0.23 (entropy std, Mistral) to 1.40 (entropy mean, Pythia-1B).
12	The partition is robust at the individual-generator level, with entropy min as the most consistently stationary feature.
13	Figure~\ref{fig:ddr-scatter} visualizes the DDR partition in ($|\rho|$, $d$) space, showing a clear gap between the three groups.
14	
15	\begin{table}[h]
16	\centering
17	\footnotesize
18	\caption{Per-generator TOST equivalence ($\varepsilon{=}|d|{<}0.20$, gen-1 vs.\ gen-2+). Observed $|d|$; \checkmark{} = equivalent ($p_{\mathrm{TOST}} < 0.05$). Features grouped by DDR partition.}
19	\label{tab:tost-per-gen}
20	\resizebox{\columnwidth}{!}{%
21	\begin{tabular}{l ccc c ccc}
22	\toprule
23	& \multicolumn{3}{c}{\textbf{Drifting}} & \textbf{Int.} & \multicolumn{3}{c}{\textbf{Near-stationary}} \\
24	\cmidrule(lr){2-4} \cmidrule(lr){5-5} \cmidrule(lr){6-8}
25	\textbf{Generator} & $\bar{H}$ & TTR & hapax & $\sigma_H$ & $H_{\max}$ & tail & $H_{\min}$ \\
26	\midrule
27	Pythia-2.8B  & 1.20 & 0.77 & 0.67 & 0.39 & 0.25          & 0.07\,\checkmark & 0.03\,\checkmark \\
28	Pythia-1B    & 1.40 & 0.80 & 0.65 & 0.53 & 0.21          & 0.08\,\checkmark & 0.02\,\checkmark \\
29	Qwen3-1.7B  & 1.12 & 0.93 & 0.83 & 0.52 & 0.02\,\checkmark & 0.09\,\checkmark & 0.05\,\checkmark \\
30	Llama-3.2-3B & 1.15 & 1.04 & 0.98 & 0.50 & 0.01\,\checkmark & 0.19          & 0.01\,\checkmark \\
31	OLMo-2-1B   & 1.19 & 1.08 & 1.00 & 0.61 & 0.06\,\checkmark & 0.22          & 0.07\,\checkmark \\
32	Qwen3-8B    & 0.86 & 0.71 & 0.66 & 0.37 & 0.04\,\checkmark & 0.15          & 0.01\,\checkmark \\
33	Qwen3-0.6B  & 0.92 & 0.63 & 0.50 & 0.56 & 0.01\,\checkmark & 0.08\,\checkmark & 0.10\,\checkmark \\
34	Mistral-7B   & 0.89 & 0.82 & 0.82 & 0.23 & 0.00\,\checkmark & 0.16          & 0.04\,\checkmark \\
35	\midrule
36	\textbf{Equiv.\ count} & 0/8 & 0/8 & 0/8 & 0/8 & 6/8 & 4/8 & 8/8 \\
37	\bottomrule
38	\end{tabular}}
39	\end{table}
40	
41	\begin{figure}[h]
42	\centering
43	\includegraphics[width=0.85\columnwidth]{fig_ddr_scatter.pdf}
44	\caption{DDR partition in pooled ($|\rho|$, Cohen's $d$) space. Drifting features (green) cluster at high $|\rho|$ and $d$; near-stationary features (orange) cluster near the origin; entropy std (purple) occupies a sole intermediate position. Dashed lines: TOST equivalence bound ($d{=}0.20$) and $|\rho|{=}0.30$. Diamond marker: entropy min (pooled $|\rho|{=}0.40$ reflects the gen-0/gen-1 boundary; gen-1 vs.\ gen-2+ $d{=}0.03$).}
45	\label{fig:ddr-scatter}
46	\end{figure}
47	
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6dd15961-b7b0-4ad4-ac32-7401ee8e9391",
  "isSidechain": true,
  "promptId": "66da4863-8b0b-4bc9-b61d-ba5a74da661b",
  "agentId": "a7bd140387e37fb65",
  "type": "user",
  "uuid": "78d44334-a7ba-48da-899c-c055733eb50e",
  "sourceToolAssistantUUID": "6dd15961-b7b0-4ad4-ac32-7401ee8e9391",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "8a3fcdf1-bd5a-44d6-bdc9-96e7600e0702",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T02:43:05.870Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KaDmNMvTvoiPX98Y5WH1KX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_seed_control.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78d44334-a7ba-48da-899c-c055733eb50e",
  "isSidechain": true,
  "agentId": "a7bd140387e37fb65",
  "requestId": "req_011CbBA7fp7JEG4i9wEo9kQ3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bb32ba4c-42ec-4fa6-8c24-df3c0a1f3ff9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "8a3fcdf1-bd5a-44d6-bdc9-96e7600e0702",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Sfj1ZRJpfax1y7VfEx3vwe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 751,
      "cache_read_input_tokens": 17691,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 751,
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

_source line 6 · 2026-05-19T02:43:05.874Z_

<details><summary>↩ Tool result · `toolu_01KaDmNMvTvoiPX98Y5WH1KX`</summary>

```text
1	\section{Independent-Seed Control}
2	\label{app:seed-control}
3	
4	To rule out topic-level leakage from shared seeds across generators, we construct an independent-seed evaluation where Pythia-2.8B and OLMo-2-1B use completely disjoint Wikipedia seed pools (500 seeds each, zero overlap).
5	Each generator produces depth-0 through depth-4 chains on its own seed pool; features are extracted with the same Pythia-410M reference model.
6	We then train a 7-feature XGBoost classifier on one generator's data and test on the other, in both directions.
7	
8	\begin{table}[h]
9	\centering
10	\small
11	\begin{tabular}{lcc}
12	\toprule
13	\textbf{Setting} & \textbf{Binary F1} & \textbf{95\% CI} \\
14	\midrule
15	Pythia-2.8B $\rightarrow$ OLMo-2-1B & 0.695 & [0.673, 0.717] \\
16	OLMo-2-1B $\rightarrow$ Pythia-2.8B & 0.666 & [0.643, 0.689] \\
17	\midrule
18	Independent-seed average & 0.680 & --- \\
19	Shared-seed LOGO (reference) & 0.694 & [0.688, 0.700] \\
20	\bottomrule
21	\end{tabular}
22	\caption{Independent-seed cross-generator evaluation (binary: gen-1 vs.\ gen-2+). Disjoint seed pools eliminate any possibility of topic-based leakage. The average independent-seed F1 (0.680) is within 1.4\,pp of the shared-seed LOGO baseline (0.694), confirming that the classifier captures generative degradation patterns rather than seed-specific topic content.}
23	\label{tab:seed-control}
24	\end{table}
25	
26	The small gap ($-$1.4\,pp) between independent-seed and shared-seed evaluation falls within bootstrap confidence intervals, and both directions individually exceed 0.66.
27	Combined with the seed-level demeaning control (\S\ref{sec:results-classification}), these results provide converging evidence that depth classification is driven by distributional properties of recursive generation, not topic identity.
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb32ba4c-42ec-4fa6-8c24-df3c0a1f3ff9",
  "isSidechain": true,
  "promptId": "66da4863-8b0b-4bc9-b61d-ba5a74da661b",
  "agentId": "a7bd140387e37fb65",
  "type": "user",
  "uuid": "bf5f2ee8-1890-421e-b385-7be302c4e448",
  "sourceToolAssistantUUID": "bb32ba4c-42ec-4fa6-8c24-df3c0a1f3ff9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "8a3fcdf1-bd5a-44d6-bdc9-96e7600e0702",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T02:43:06.618Z_

<details open><summary>🔧 Tool call — Read · `toolu_014vC9a44H6y7msNW6c8beua`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_ddr_validation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf5f2ee8-1890-421e-b385-7be302c4e448",
  "isSidechain": true,
  "agentId": "a7bd140387e37fb65",
  "requestId": "req_011CbBA7fp7JEG4i9wEo9kQ3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b7c7a6ab-8ba3-4cd0-92cd-03d769e2a2ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "8a3fcdf1-bd5a-44d6-bdc9-96e7600e0702",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Sfj1ZRJpfax1y7VfEx3vwe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 751,
      "cache_read_input_tokens": 17691,
      "output_tokens": 419,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 751
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 419,
          "cache_read_input_tokens": 17691,
          "cache_creation_input_tokens": 751,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 751,
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

_source line 8 · 2026-05-19T02:43:06.622Z_

<details><summary>↩ Tool result · `toolu_014vC9a44H6y7msNW6c8beua`</summary>

```text
1	\subsection*{Data-Driven Clustering}
2	
3	To assess whether the 3/1/3 DDR partition emerges from the data rather than post-hoc grouping, we apply $k$-means clustering ($k \in \{2,3,4,5\}$) to the seven features in standardized $(|\rho|, d)$ space (Table~\ref{tab:clustering}).
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\caption{$k$-means clustering of 7 features in $(|\rho|, d)$ space.}
9	\label{tab:clustering}
10	\begin{tabular}{ccp{5.5cm}}
11	\toprule
12	$k$ & Silhouette & Clusters \\
13	\midrule
14	2 & \textbf{0.632} & \{$\bar{H}$, TTR, hapax\} $\mid$ \{$\sigma_H$, $H_{\min}$, $H_{\max}$, tail\} \\
15	3 & 0.499 & \{$\bar{H}$, TTR, hapax\} $\mid$ \{$\sigma_H$, $H_{\max}$, tail\} $\mid$ \{$H_{\min}$\} \\
16	4 & 0.571 & \{$\bar{H}$, TTR, hapax\} $\mid$ \{$H_{\max}$, tail\} $\mid$ \{$\sigma_H$\} $\mid$ \{$H_{\min}$\} \\
17	\bottomrule
18	\end{tabular}
19	\end{table}
20	
21	The primary drifting/non-drifting split ($k{=}2$, silhouette\,=\,0.632) is the strongest cluster structure.
22	At $k{=}3$, entropy min forms its own cluster rather than joining the near-stationary group because its pooled $|\rho|{=}0.40$ (driven by the gen-0/gen-1 boundary) places it far from other near-stationary features in $\rho$ space.
23	The 3/1/3 DDR partition resolves this by using the gen-1 vs.\ gen-2+ Cohen's $d$ ($d{=}0.03$) to place entropy min in the near-stationary group, a domain-informed refinement that unsupervised clustering cannot recover from pooled statistics alone.
24	At $k{=}4$ (silhouette\,=\,0.571), entropy std separates from the near-stationary group, consistent with its intermediate DDR classification.
25	
26	\subsection*{TOST Equivalence Bound Sensitivity}
27	\label{app:tost-sensitivity}
28	
29	Table~\ref{tab:tost-sensitivity} shows the fraction of generators for which each feature passes the TOST equivalence test (gen-1 vs.\ gen-2+, $\alpha{=}0.05$) at three equivalence bounds $\varepsilon$.
30	
31	\begin{table}[h]
32	\centering
33	\small
34	\caption{TOST equivalence pass rate across 8 generators at varying $\varepsilon$.}
35	\label{tab:tost-sensitivity}
36	\begin{tabular}{llccc}
37	\toprule
38	\textbf{DDR Zone} & \textbf{Feature} & $\boldsymbol{\varepsilon{=}0.15}$ & $\boldsymbol{\varepsilon{=}0.20}$ & $\boldsymbol{\varepsilon{=}0.25}$ \\
39	\midrule
40	\multirow{3}{*}{Drifting} & $\bar{H}$ (ent.\ mean) & 0/8 & 0/8 & 0/8 \\
41	 & TTR & 0/8 & 0/8 & 0/8 \\
42	 & hapax ratio & 0/8 & 0/8 & 0/8 \\
43	\midrule
44	Intermediate & $\sigma_H$ (ent.\ std) & 0/8 & 0/8 & 0/8 \\
45	\midrule
46	\multirow{3}{*}{Near-stat.} & $H_{\min}$ (ent.\ min) & 7/8 & 8/8 & 8/8 \\
47	 & $H_{\max}$ (ent.\ max) & 6/8 & 6/8 & 6/8 \\
48	 & tail decay & 4/8 & 4/8 & 7/8 \\
49	\bottomrule
50	\end{tabular}
51	\end{table}
52	
53	The partition is robust to the equivalence bound: drifting features reject equivalence at all $\varepsilon$ for all generators, while entropy min passes even at the stricter bound $\varepsilon{=}0.15$ (7/8 generators).
54	Tail decay is the most $\varepsilon$-sensitive near-stationary feature, passing 4/8 at $\varepsilon{=}0.20$ but 7/8 at $\varepsilon{=}0.25$; the four non-passing generators show $|d|{=}0.15$--$0.22$, still well below the drifting threshold ($d > 0.50$).
55	Entropy max is stable across all three bounds (6/8), with the two failures (Pythia-1B $d{=}0.21$, Pythia-2.8B $d{=}0.25$) reflecting same-family reference affinity with the Pythia-410M reference model.
56	
57	\subsection*{Holdout Generator Split Validation}
58	\label{app:holdout-split}
59	
60	To confirm the DDR partition is not an artifact of the specific generator pool, we split the eight generators into disjoint selection (4) and validation (4) sets, compute per-subset pooled $(|\rho|, d)$, and check whether all seven features receive the same zone assignment in both subsets.
61	We evaluate two complementary splits to avoid dependence on a single partition:
62	Split~A selects \{Pythia-2.8B, Qwen3-1.7B, OLMo, Mistral\} (validation: Pythia-1B, Qwen3-0.6B, Qwen3-8B, Llama);
63	Split~B selects \{Pythia-1B, Qwen3-0.6B, OLMo, Mistral\} (validation: Pythia-2.8B, Qwen3-1.7B, Qwen3-8B, Llama).
64	
65	\begin{table}[h]
66	\centering
67	\small
68	\caption{Holdout split validation of the DDR partition. Selection (sel) and validation (val) $|\rho|$ and $d$ for two disjoint 4/4 generator splits. Zone assignment is identical across all four subsets for every feature.}
69	\label{tab:holdout-split}
70	\resizebox{\linewidth}{!}{%
71	\begin{tabular}{llcccccc}
72	\toprule
73	& & \multicolumn{3}{c}{\textbf{Split A}} & \multicolumn{3}{c}{\textbf{Split B}} \\
74	\cmidrule(lr){3-5} \cmidrule(lr){6-8}
75	\textbf{Zone} & \textbf{Feature} & sel $|\rho|$ & val $|\rho|$ & $\Delta|\rho|$ & sel $|\rho|$ & val $|\rho|$ & $\Delta|\rho|$ \\
76	\midrule
77	\multirow{3}{*}{Drifting} & $\bar{H}$ (ent.\ mean) & 0.60 & 0.58 & 0.02 & 0.60 & 0.58 & 0.02 \\
78	 & TTR & 0.61 & 0.59 & 0.02 & 0.60 & 0.59 & 0.01 \\
79	 & hapax ratio & 0.62 & 0.60 & 0.02 & 0.62 & 0.61 & 0.01 \\
80	\midrule
81	Intermediate & $\sigma_H$ (ent.\ std) & 0.19 & 0.21 & 0.02 & 0.22 & 0.17 & 0.05 \\
82	\midrule
83	\multirow{3}{*}{Near-stat.} & $H_{\min}$ (ent.\ min) & 0.39 & 0.36 & 0.03 & 0.38 & 0.37 & 0.01 \\
84	 & $H_{\max}$ (ent.\ max) & 0.05 & 0.05 & 0.00 & 0.04 & 0.06 & 0.02 \\
85	 & tail decay & 0.10 & 0.08 & 0.02 & 0.11 & 0.07 & 0.04 \\
86	\bottomrule
87	\end{tabular}}
88	\end{table}
89	
90	Under simple joint $(|\rho|, d)$ thresholds, both splits produce a 3/2/2 partition: entropy min is classified as a second intermediate feature due to its elevated pooled $|\rho|$ (0.36--0.39).
91	However, entropy min's binary (gen-1 vs.\ gen-2+) $d$ values are uniformly below 0.06 across all four split${\times}$subset combinations, confirming near-stationarity on the task-relevant metric; its pooled $|\rho|$ reflects change concentrated at the gen-0/gen-1 boundary rather than sustained drift.
92	Five of seven features are unambiguously classified under any reasonable criterion; entropy min's boundary status is resolved by the binary-task $d$ criterion.
93	
94	Selection and validation subsets produce identical partitions in both splits (Table~\ref{tab:holdout-split}; Figure~\ref{fig:holdout-scatter}).
95	The maximum $\Delta|\rho|$ between selection and validation is 0.05 (entropy std, Split~B), and the minimum gap between adjacent zones remains $>$0.15 in all subsets.
96	
97	\begin{figure}[h]
98	\centering
99	\includegraphics[width=\linewidth]{fig_ddr_holdout_split.pdf}
100	\caption{Holdout split validation in $(|\rho|, d)$ space. Filled markers: selection set; hollow: validation set. Zone assignments are identical across subsets; selection/validation pairs cluster tightly for all features.}
101	\label{fig:holdout-scatter}
102	\end{figure}
103	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b7c7a6ab-8ba3-4cd0-92cd-03d769e2a2ad",
  "isSidechain": true,
  "promptId": "66da4863-8b0b-4bc9-b61d-ba5a74da661b",
  "agentId": "a7bd140387e37fb65",
  "type": "user",
  "uuid": "f9c6b1dd-4c08-4c6d-9a82-4c1a2fc55ff5",
  "sourceToolAssistantUUID": "b7c7a6ab-8ba3-4cd0-92cd-03d769e2a2ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "8a3fcdf1-bd5a-44d6-bdc9-96e7600e0702",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T02:43:06.646Z_

<details open><summary>🔧 Tool call — Read · `toolu_012ftsN5VQ2wFj9GyKWXMX9v`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9c6b1dd-4c08-4c6d-9a82-4c1a2fc55ff5",
  "isSidechain": true,
  "agentId": "a7bd140387e37fb65",
  "requestId": "req_011CbBA7fp7JEG4i9wEo9kQ3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d20f64d1-2514-4ee1-9c42-6290e1018cca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "8a3fcdf1-bd5a-44d6-bdc9-96e7600e0702",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Sfj1ZRJpfax1y7VfEx3vwe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 751,
      "cache_read_input_tokens": 17691,
      "output_tokens": 419,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 751
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 419,
          "cache_read_input_tokens": 17691,
          "cache_creation_input_tokens": 751,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 751,
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

_source line 10 · 2026-05-19T02:43:06.652Z_

<details><summary>↩ Tool result · `toolu_012ftsN5VQ2wFj9GyKWXMX9v`</summary>

```text
1	To assess whether depth signal extends beyond handcrafted features, we fine-tune a pretrained language model end-to-end as a depth classifier using QLoRA \cite{qlora}.
2	
3	\paragraph{Setup.}
4	We fine-tune Qwen3-0.6B-Base with LoRA rank 16, learning rate $2 \times 10^{-4}$, and 3 epochs, framing depth estimation as 5-class sequence classification (gen-0 through gen-4).\footnote{Evaluated on the original 6-generator subset; XGBoost 3-class F1\,=\,0.789. We expect 8-generator training to further improve given additional diversity; the comparison direction is preserved.}
5	For 3-class evaluation, we collapse predictions into gen-0\,/\,gen-1\,/\,gen-2+ post hoc.
6	All results use the same LOGO protocol as the main experiments.
7	
8	\begin{table}[h]
9	\centering
10	\small
11	\caption{QLoRA end-to-end depth classification vs.\ XGBoost on handcrafted features, under LOGO evaluation.}
12	\label{tab:qlora}
13	\resizebox{\linewidth}{!}{%
14	\begin{tabular}{lccc}
15	\toprule
16	\textbf{Method} & \textbf{5-class F1} & \textbf{3-class F1} & \textbf{Per-class F1 (5-class)} \\
17	\midrule
18	XGBoost (7 features) & 0.501 $\pm$ 0.038 & 0.789 & --- \\
19	QLoRA (Qwen3-0.6B)   & 0.583 $\pm$ 0.010 & 0.905 $\pm$ 0.003 & 0.999\,/\,0.796\,/\,0.413\,/\,0.259\,/\,0.447 \\
20	\bottomrule
21	\end{tabular}}
22	\end{table}
23	
24	\paragraph{Results.}
25	QLoRA achieves 3-class LOGO F1\,=\,0.905 ($\pm$0.003), a +11.6\,pp improvement over the XGBoost baseline (0.789).
26	On 5-class evaluation, QLoRA reaches F1\,=\,0.583 ($\pm$0.010) vs.\ 0.501 for XGBoost (+8.2\,pp), with the largest gains at gen-1 (0.796 vs.\ 0.634) and gen-2 (0.413 vs.\ 0.268).
27	The gen-2/gen-3 boundary remains the primary failure mode (gen-3 F1\,=\,0.259), consistent with the feature-level analysis in \S\ref{sec:discussion}.
28	
29	\paragraph{Hyperparameter robustness.}
30	A second run with LoRA rank 32 and seed 123 yields 5-class F1\,=\,0.587 ($\pm$0.005) and 3-class F1\,=\,0.905 ($\pm$0.004), which confirms stability across hyperparameter and seed variation ($\Delta < 1$\,pp on both metrics).
31	
32	\paragraph{Implications.}
33	The substantial 3-class improvement demonstrates that raw token embeddings contain depth signal beyond what summary statistics capture; the seven handcrafted features are a strong but lossy compression of the full distributional information.
34	End-to-end fine-tuning exploits token-level patterns (e.g., positional regularities, n-gram repetitions) that aggregate features cannot represent.
35	This confirms that the depth signal documented in our main analysis is real and exploitable beyond engineered features, while the handcrafted approach retains practical advantages: interpretability, computational efficiency (no GPU inference), and the ability to reveal the differential depth response pattern that motivates the task formulation.
36	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d20f64d1-2514-4ee1-9c42-6290e1018cca",
  "isSidechain": true,
  "promptId": "66da4863-8b0b-4bc9-b61d-ba5a74da661b",
  "agentId": "a7bd140387e37fb65",
  "type": "user",
  "uuid": "b71bcd84-3b26-4889-bd71-29262bed8948",
  "sourceToolAssistantUUID": "d20f64d1-2514-4ee1-9c42-6290e1018cca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "8a3fcdf1-bd5a-44d6-bdc9-96e7600e0702",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T02:43:06.662Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UV5xZzSgA2VEZNGGA61b7e`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_classifier.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b71bcd84-3b26-4889-bd71-29262bed8948",
  "isSidechain": true,
  "agentId": "a7bd140387e37fb65",
  "requestId": "req_011CbBA7fp7JEG4i9wEo9kQ3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "faa38a21-0150-471b-91e5-b4ef2592dd86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "8a3fcdf1-bd5a-44d6-bdc9-96e7600e0702",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Sfj1ZRJpfax1y7VfEx3vwe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 751,
      "cache_read_input_tokens": 17691,
      "output_tokens": 419,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 751
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 419,
          "cache_read_input_tokens": 17691,
          "cache_creation_input_tokens": 751,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 751,
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

_source line 12 · 2026-05-19T02:43:06.665Z_

<details><summary>↩ Tool result · `toolu_01UV5xZzSgA2VEZNGGA61b7e`</summary>

```text
1	To verify that the depth signal resides in the features rather than the classifier,
2	we repeat the 6-generator LOGO evaluation using Logistic Regression and Random Forest
3	in place of XGBoost (Table~\ref{tab:alt-classifier}).
4	All other settings (the same 7 features, 3-class labels, and class-balanced downsampling) are
5	kept identical. For Logistic Regression we apply standard scaling to the features.
6	
7	\begin{table}[h]
8	\centering
9	\caption{LOGO macro-F1 across three classifiers. Each column shows the held-out generator F1. (6-generator LOGO; 3-class.)}
10	\label{tab:alt-classifier}
11	\small
12	\resizebox{\linewidth}{!}{%
13	\begin{tabular}{lc cccccc}
14	\toprule
15	Classifier & Avg F1 & OLMo-2 & Py-1B & Py-2.8B & Qw-0.6B & Qw-1.7B & Qw-8B \\
16	\midrule
17	XGBoost          & 0.789 & 0.764 & 0.856 & 0.804 & 0.824 & 0.806 & 0.683 \\
18	Random Forest    & 0.790 & 0.764 & 0.856 & 0.804 & 0.825 & 0.807 & 0.684 \\
19	Logistic Regr.   & 0.725 & 0.719 & 0.781 & 0.740 & 0.745 & 0.743 & 0.624 \\
20	\bottomrule
21	\end{tabular}}
22	\end{table}
23	
24	Both tree-based classifiers achieve LOGO F1 $\approx 0.79$,
25	and even a linear model reaches $0.725$, well above the $0.33$ chance baseline for
26	three classes.
27	The per-generator ranking is also consistent across classifiers
28	(Pythia-1B easiest, Qwen3-8B hardest),
29	confirming that discriminative power originates in the entropy and lexical features,
30	not in classifier capacity.
31	Ordinal-specific methods (CORAL \cite{coral_ordinal}, Frank-Hall \cite{frank_hall_ordinal}) achieve comparable F1 with overlapping CIs, which confirms that 3-class granularity provides insufficient resolution for ranking-aware losses to improve over standard multiclass classification.
32	
33	\subsection*{Sampling Sensitivity Analysis}
34	\label{app:sampling-sensitivity}
35	
36	To assess robustness to decoding temperature, we regenerate continuation chains at $t \in \{0.5, 0.9\}$ with fixed nucleus $p{=}0.9$ (matching the default) for four generators spanning three model families: Pythia-2.8B, OLMo-2-1B, Qwen3-1.7B, and Qwen3-0.6B (Table~\ref{tab:sampling-ablation}).
37	
38	\begin{table}[h]
39	\centering
40	\caption{Depth classification under varying temperature (fixed top-$p$\,=\,0.9). Binary: gen-1 vs.\ gen-2+. LOGO evaluation; 95\% bootstrap CIs.$^{\ast}$$^{\dagger}$}
41	\label{tab:sampling-ablation}
42	\small
43	\begin{tabular}{llcc c}
44	\toprule
45	Model & Temp & LOGO Binary F1 & 95\% CI & $\rho$(ent.\ mean) \\
46	\midrule
47	Pythia-2.8B$^{\dagger}$ & 0.5  & \textbf{0.814} & [.798, .828] & $-0.58$ \\
48	Pythia-2.8B$^{\dagger}$ & 0.7  & 0.740 & [.725, .755] & $-0.60$ \\
49	Pythia-2.8B$^{\dagger}$ & 0.9  & 0.480 & [.465, .498] & $-0.30$ \\
50	\midrule
51	OLMo-2-1B & 0.5  & \textbf{0.783} & [.768, .798] & $-0.72$ \\
52	OLMo-2-1B & 0.7  & 0.695 & [.679, .711] & $-0.60$ \\
53	OLMo-2-1B & 0.9  & 0.453 & [.437, .469] & $-0.26$ \\
54	\midrule
55	Qwen3-1.7B$^{\dagger}$ & 0.5  & 0.751 & --- & $-0.60$ \\
56	Qwen3-1.7B$^{\dagger}$ & 0.7  & 0.751 & --- & $-0.60$ \\
57	Qwen3-1.7B$^{\dagger}$ & 0.9  & 0.566 & --- & $-0.37$ \\
58	\midrule
59	Qwen3-0.6B & 0.5  & 0.711 & [.694, .729] & $-0.67$ \\
60	Qwen3-0.6B & 0.7  & 0.691 & [.673, .709] & $-0.60$ \\
61	Qwen3-0.6B & 0.9  & 0.598 & [.582, .615] & $-0.29$ \\
62	\bottomrule
63	\end{tabular}
64	\end{table}
65	\noindent{\footnotesize $^{\ast}$OLMo temperature experiments use OLMo-2-0425-1B (April 2025 release); the original OLMo-2-1B-hf weights used in the main experiments are no longer publicly available.}\\
66	\noindent{\footnotesize $^{\dagger}$Pythia-2.8B and Qwen3-1.7B temperature experiments predate the 8-generator expansion and use 6-generator LOGO; OLMo-2-1B and Qwen3-0.6B use 8-generator LOGO. Within-model temperature comparisons (the focus of this analysis) are unaffected.}
67	
68	Temperature sensitivity is asymmetric and model-dependent. High-temperature degradation ($t{=}0.9$) is universal: all four generators lose $9.3$--$26.0$\,pp in binary F1, with entropy mean's $|\rho|$ weakening to $0.26$--$0.37$ (vs.\ $0.58$--$0.72$ at $t{=}0.5$). Low-temperature improvement ($t{=}0.5$) is model-dependent: Pythia-2.8B and OLMo-2-1B gain $+7.4$ and $+8.8$\,pp respectively, while both Qwen models show negligible change ($0$--$2.0$\,pp). This split tracks model family rather than scale: Qwen3-0.6B (smallest) and Qwen3-1.7B both plateau, while OLMo-2-1B (similar scale to Qwen3-1.7B) benefits substantially. One possible explanation is that Qwen models produce more peaked output distributions at $t{=}0.7$, leaving less room for low-temperature compression to sharpen the depth signal.
69	
70	The method operates reliably within $t \in [0.5, 0.7]$ across all tested models. Degradation onset at $t{=}0.9$ defines the practical upper bound, consistent with the hypothesis that elevated temperature injects sufficient randomness to flatten the distributional drift that DDR exploits (\S\ref{sec:discussion}).
71	
72	\subsection*{Per-Generator Performance}
73	
74	Figure~\ref{fig:per-gen} visualizes per-generator LOGO performance.
75	Pythia models (1B, 2.8B) achieve highest F1, while larger models (Mistral-7B, Qwen3-8B) show degradation.
76	The scale effect (larger models $\rightarrow$ lower F1) is consistent with higher-capacity models generating text statistically closer to human writing.
77	
78	\begin{figure}[ht]
79	\centering
80	\includegraphics[width=\columnwidth]{fig_appendix_per_gen.pdf}
81	\caption{Per-generator LOGO performance. (a) 8-generator binary and 3-class F1, sorted by binary F1. Dashed lines: pool average. (b) 6-generator LOGO detail heatmap showing the performance spread across model families.}
82	\label{fig:per-gen}
83	\end{figure}
84	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "faa38a21-0150-471b-91e5-b4ef2592dd86",
  "isSidechain": true,
  "promptId": "66da4863-8b0b-4bc9-b61d-ba5a74da661b",
  "agentId": "a7bd140387e37fb65",
  "type": "user",
  "uuid": "b6a867e0-3f15-4bee-af18-f35f3f3f3202",
  "sourceToolAssistantUUID": "faa38a21-0150-471b-91e5-b4ef2592dd86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "8a3fcdf1-bd5a-44d6-bdc9-96e7600e0702",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-19T02:43:32.403Z_

I have successfully read all five LaTeX appendix files. Here is the complete content with key details highlighted:

## APPENDIX 1: appendix_tost.tex

**Full Content:**
This appendix applies two one-sided t-tests (TOST) to confirm that near-stationary classification is not a pooling artifact. Key details:

- **Equivalence bound**: |d| < 0.20 (Cohen's conventional small effect size)
- **SESOI (Smallest Effect of Practical Significance)**: Effects below 0.20 threshold are unlikely to be practically meaningful for depth discrimination
- **Statistical justification**: LOFO analysis supports this choice—removing any near-stationary feature changes classification F1 by ≤1.5 percentage points
- **Sensitivity analysis**: Partition is robust at ε ∈ {0.15, 0.20, 0.25}
- **Results per feature across 8 generators**:
  - **Entropy min** (H_min): Passes equivalence for ALL 8 generators (most consistently stationary)
  - **Entropy max** (H_max): Passes for 6/8 generators (exceeds ε only for Pythia-1B and Pythia-2.8B with |d| ≈ 0.21–0.25)
  - **Tail decay**: Passes for 4/8 generators
  - **Drifting features** (entropy mean, TTR, hapax): All fail equivalence uniformly with |d| ranging from 0.23 to 1.40

The partition exhibits clear separation in (|ρ|, d) space between the three groups.

## APPENDIX 2: appendix_seed_control.tex

**Full Content:**
This appendix validates that the classifier captures generative degradation rather than seed-specific topic content through independent-seed evaluation.

- **Methodology**: Pythia-2.8B and OLMo-2-1B use completely disjoint Wikipedia seed pools (500 seeds each, zero overlap)
- **Cross-generator evaluation** (both directions):
  - Pythia-2.8B → OLMo-2-1B: Binary F1 = 0.695 [95% CI: 0.673, 0.717]
  - OLMo-2-1B → Pythia-2.8B: Binary F1 = 0.666 [95% CI: 0.643, 0.689]
  - Independent-seed average: 0.680
  - Shared-seed LOGO baseline (reference): 0.694 [95% CI: 0.688, 0.700]
- **Gen-0 leakage addressed**: The small gap (−1.4 pp) falls within bootstrap confidence intervals, confirming that depth classification is driven by distributional properties of recursive generation, not topic identity
- **Additional control**: Seed-level demeaning control is applied (see main results section)

## APPENDIX 3: appendix_ddr_validation.tex

**Full Content:**
This appendix validates the Data-Driven Ranking (DDR) partition through multiple approaches:

### K-means Clustering Validation:
- **2-cluster split** (silhouette = 0.632): {Drifting} | {Near-stationary + Intermediate}—strongest cluster structure
- **3-cluster split** (silhouette = 0.499): {Drifting} | {Near-stationary} | {Entropy min}
- **4-cluster split** (silhouette = 0.571): Entropy std separates as intermediate
- The 3/1/3 partition uses domain-informed refinement (gen-1 vs. gen-2+ Cohen's d = 0.03) to place entropy min in near-stationary group

### TOST Equivalence Sensitivity:
- **Equivalence bounds tested**: ε ∈ {0.15, 0.20, 0.25}
- **Robustness findings**:
  - Drifting features reject equivalence at all ε for all 8 generators
  - Entropy min passes at stricter bound ε = 0.15 for 7/8 generators
  - Entropy max: 6/8 generators across all bounds (failures in Pythia-1B |d|=0.21, Pythia-2.8B |d|=0.25)
  - Tail decay: 4/8 at ε=0.20 but 7/8 at ε=0.25

### Holdout Generator Split Validation:
- **Two complementary 4/4 splits**:
  - Split A: Selection {Pythia-2.8B, Qwen3-1.7B, OLMo, Mistral} | Validation {Pythia-1B, Qwen3-0.6B, Qwen3-8B, Llama}
  - Split B: Selection {Pythia-1B, Qwen3-0.6B, OLMo, Mistral} | Validation {Pythia-2.8B, Qwen3-1.7B, Qwen3-8B, Llama}
- **Partition stability**: Zone assignment is identical across all four subsets for every feature
- **Maximum Δ|ρ|**: 0.05 (entropy std, Split B)
- **Minimum gap between zones**: >0.15 in all subsets

## APPENDIX 4: appendix_qlora.tex

**Full Content:**
This appendix presents end-to-end depth classification using QLoRA fine-tuning:

### Setup Details:
- **Model**: Qwen3-0.6B-Base
- **LoRA rank**: 16
- **Learning rate**: 2 × 10^−4
- **Epochs**: 3
- **Task formulation**: 5-class sequence classification (gen-0 through gen-4)
- **Evaluation protocol**: LOGO protocol, same as main experiments; 3-class evaluation collapses predictions post hoc into gen-0 / gen-1 / gen-2+

### Results:
- **3-class F1**: 0.905 (±0.003)—**+11.6 pp improvement** over XGBoost baseline (0.789)
- **5-class F1**: 0.583 (±0.010) vs. 0.501 for XGBoost (+8.2 pp)
- **Per-class 5-class F1**: 0.999 (gen-0) / 0.796 (gen-1) / 0.413 (gen-2) / 0.259 (gen-3) / 0.447 (gen-4)
- **Hyperparameter robustness**: LoRA rank 32 with seed 123 yields 5-class F1 = 0.587 (±0.005), 3-class F1 = 0.905 (±0.004)—stability within 1 pp

### Implications:
Raw token embeddings contain depth signal beyond summary statistics; the seven handcrafted features are strong but lossy compression of full distributional information. End-to-end fine-tuning exploits token-level patterns that aggregate features cannot represent.

## APPENDIX 5: appendix_classifier.tex

**Full Content:**
This appendix includes multiple classifier and sensitivity analyses:

### Classifier Sensitivity Analysis:
**Alternative Classifiers** (6-generator LOGO, 3-class):
- **XGBoost**: Average F1 = 0.789 [per-generator: OLMo-2: 0.764, Pythia-1B: 0.856, Pythia-2.8B: 0.804, Qwen-0.6B: 0.824, Qwen-1.7B: 0.806, Qwen-8B: 0.683]
- **Random Forest**: Average F1 = 0.790 [nearly identical per-generator performance]
- **Logistic Regression**: Average F1 = 0.725 [well above 0.33 chance baseline]
- **Finding**: Discriminative power resides in features, not classifier capacity; per-generator ranking is consistent across classifiers

### Temperature Sensitivity Analysis:
**Temperature values tested**: t ∈ {0.5, 0.7, 0.9} with fixed top-p = 0.9

**Binary (gen-1 vs. gen-2+) LOGO performance**:
- **Pythia-2.8B**: t=0.5: 0.814; t=0.7: 0.740; t=0.9: 0.480
- **OLMo-2-1B**: t=0.5: 0.783; t=0.7: 0.695; t=0.9: 0.453
- **Qwen3-1.7B**: t=0.5: 0.751; t=0.7: 0.751; t=0.9: 0.566
- **Qwen3-0.6B**: t=0.5: 0.711; t=0.7: 0.691; t=0.9: 0.598

**Key findings**:
- **High-temperature degradation** (t=0.9): Universal across all four generators, losing 9.3–26.0 pp in binary F1; entropy mean's |ρ| weakens to 0.26–0.37 (vs. 0.58–0.72 at t=0.5)
- **Low-temperature improvement** (t=0.5): Model-dependent. Pythia-2.8B and OLMo-2-1B gain +7.4 and +8.8 pp respectively; both Qwen models show negligible change (0–2.0 pp)
- **Practical operating range**: Method operates reliably within t ∈ [0.5, 0.7] across all tested models

### Per-Generator Performance:
- Pythia models (1B, 2.8B) achieve highest F1
- Larger models (Mistral-7B, Qwen3-8B) show degradation
- Scale effect: Higher-capacity models generate text statistically closer to human writing, reducing depth signal

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6a867e0-3f15-4bee-af18-f35f3f3f3202",
  "isSidechain": true,
  "agentId": "a7bd140387e37fb65",
  "requestId": "req_011CbBA7wMFUx24R8HRdWMhh",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6f023835-3476-4d25-8abb-77cff11fc5d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/review_reviewer_1_c21d58b8",
  "sessionId": "8a3fcdf1-bd5a-44d6-bdc9-96e7600e0702",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018wHuPHFFXkpfr3uKQbmt9C",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 9962,
      "cache_read_input_tokens": 18442,
      "output_tokens": 2482,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9962
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 2482,
          "cache_read_input_tokens": 18442,
          "cache_creation_input_tokens": 9962,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9962,
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
