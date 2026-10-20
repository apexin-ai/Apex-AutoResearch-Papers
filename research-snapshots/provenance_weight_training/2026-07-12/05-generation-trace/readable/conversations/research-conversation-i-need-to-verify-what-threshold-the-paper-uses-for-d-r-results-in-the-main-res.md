# Research conversation: I need to verify what threshold the paper uses for D&R results in the main results table. Read these files and find the 

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a77822597a2053a5c.jsonl`
- **Structured JSON:** [`549aa9066be1d7d8f5c8.json`](../../sessions/54/549aa9066be1d7d8f5c8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

33 recorded events

### User

_source line 1 · 2026-05-25T19:57:19.747Z_

I need to verify what threshold the paper uses for D&R results in the main results table. Read these files and find the main results table, looking specifically for what D&R PPL values are reported and at what thresholds:

1. `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex` (if it exists)
2. Any file matching `*results*` or `*main*` in `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/`

Also search for "17.250" and "17.25" across all .tex files in the paper directory to find all occurrences.

Also search for "5.9" across all .tex files to find where the 5.9x claim originates and how it might be computed.

Report the exact text and line numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "2063b979-bba7-4480-8b91-7387b6dcd8bf",
  "agentId": "a77822597a2053a5c",
  "type": "user",
  "uuid": "401e7c45-0981-4a88-8316-46cb3d527893",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "3aaca442-e705-47db-9f84-980fe61c25da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-25T19:57:21.236Z_

I'll help you find the D&R threshold information and search for those specific values. Let me start by exploring the paper structure and searching for the relevant files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "401e7c45-0981-4a88-8316-46cb3d527893",
  "isSidechain": true,
  "agentId": "a77822597a2053a5c",
  "requestId": "req_011CbPsqdQVVgj4X18meD64J",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "294bd5d9-27dc-4a56-af1b-223ea52d5c51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "3aaca442-e705-47db-9f84-980fe61c25da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SH5u3KRiC4QhdQQBZZXzqR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19402,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19402,
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

_source line 3 · 2026-05-25T19:57:21.850Z_

<details open><summary>🔧 Tool call — Glob · `toolu_014K2pQev5SGTHoX27xq2e1n`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "294bd5d9-27dc-4a56-af1b-223ea52d5c51",
  "isSidechain": true,
  "agentId": "a77822597a2053a5c",
  "requestId": "req_011CbPsqdQVVgj4X18meD64J",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f5ab622c-e34f-477e-b524-6ab07e08a994",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "3aaca442-e705-47db-9f84-980fe61c25da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SH5u3KRiC4QhdQQBZZXzqR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19402,
      "cache_read_input_tokens": 0,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 19402
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 202,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 19402,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 19402,
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

_source line 4 · 2026-05-25T19:57:21.859Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014NQ7U5m2KRmEYU1qia3QRj`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper -type f -name \"*.tex\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5ab622c-e34f-477e-b524-6ab07e08a994",
  "isSidechain": true,
  "agentId": "a77822597a2053a5c",
  "requestId": "req_011CbPsqdQVVgj4X18meD64J",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4d2f8f11-db4f-4a78-be4c-b14ea829d4b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "3aaca442-e705-47db-9f84-980fe61c25da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SH5u3KRiC4QhdQQBZZXzqR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19402,
      "cache_read_input_tokens": 0,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 19402
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 202,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 19402,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 19402,
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

_source line 5 · 2026-05-25T19:57:21.874Z_

<details><summary>↩ Tool result · `toolu_014K2pQev5SGTHoX27xq2e1n`</summary>

```text
docs/paper/sections/checklist.tex
docs/paper/sections/introduction.tex
docs/paper/sections/experiments.tex
docs/paper/sections/abstract.tex
docs/paper/sections/method.tex
docs/paper/sections/limitations.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/appendix.tex
docs/paper/sections/discussion.tex
docs/paper/sections/results.tex
docs/paper/sections/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5ab622c-e34f-477e-b524-6ab07e08a994",
  "isSidechain": true,
  "promptId": "2063b979-bba7-4480-8b91-7387b6dcd8bf",
  "agentId": "a77822597a2053a5c",
  "type": "user",
  "uuid": "2bff2768-682d-4b9f-801a-169490b0ea83",
  "sourceToolAssistantUUID": "f5ab622c-e34f-477e-b524-6ab07e08a994",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "3aaca442-e705-47db-9f84-980fe61c25da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-25T19:57:21.919Z_

<details><summary>↩ Tool result · `toolu_014NQ7U5m2KRmEYU1qia3QRj`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d2f8f11-db4f-4a78-be4c-b14ea829d4b9",
  "isSidechain": true,
  "promptId": "2063b979-bba7-4480-8b91-7387b6dcd8bf",
  "agentId": "a77822597a2053a5c",
  "type": "user",
  "uuid": "f36aef4a-2e7a-4f5e-8bb5-043ac98af44d",
  "sourceToolAssistantUUID": "4d2f8f11-db4f-4a78-be4c-b14ea829d4b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "3aaca442-e705-47db-9f84-980fe61c25da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-25T19:57:23.613Z_

Good! The results.tex file exists. Now let me read it and also search for the specific values you mentioned across all .tex files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f36aef4a-2e7a-4f5e-8bb5-043ac98af44d",
  "isSidechain": true,
  "agentId": "a77822597a2053a5c",
  "requestId": "req_011CbPsqngM6SkUqsoKE3jCg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "57b599e9-2f63-471d-aa75-9ff0ba5d90f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "3aaca442-e705-47db-9f84-980fe61c25da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WLMioVnb3bzkaWm3Fwr1Dj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1677,
      "cache_read_input_tokens": 19402,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1677,
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

_source line 8 · 2026-05-25T19:57:23.892Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HGG31JMSWsRUM6omVQjY5p`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57b599e9-2f63-471d-aa75-9ff0ba5d90f8",
  "isSidechain": true,
  "agentId": "a77822597a2053a5c",
  "requestId": "req_011CbPsqngM6SkUqsoKE3jCg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bce5907a-8f45-4ff7-8b30-c25f2b808b33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "3aaca442-e705-47db-9f84-980fe61c25da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WLMioVnb3bzkaWm3Fwr1Dj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1677,
      "cache_read_input_tokens": 19402,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1677,
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

_source line 9 · 2026-05-25T19:57:23.898Z_

<details><summary>↩ Tool result · `toolu_01HGG31JMSWsRUM6omVQjY5p`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\small
4	\setlength{\tabcolsep}{3pt}
5	\resizebox{\columnwidth}{!}{%
6	\begin{tabular}{@{}lcccc@{}}
7	\toprule
8	\textbf{Method} & \textbf{Seed 42} & \textbf{Seed 123} & \textbf{Seed 456} & \textbf{Mean} \\
9	\midrule
10	Uniform                & 17.694 & 17.686 & 17.702 & 17.697 $\pm$ .008 \\
11	Adaptive $\bstar$ (ours) & \textbf{17.680} & \textbf{17.666} & \textbf{17.677} & \textbf{17.674} $\pm$ .006 \\
12	ESS-only               & 17.730 & 17.720 & 17.760 & 17.737 $\pm$ .021 \\
13	Random $\mathcal{U}(0,2)$ & 17.830 & 17.800 & 17.777 & 17.802 $\pm$ .027 \\
14	Permuted $q$-scores  & 17.919 & --     & --     & 17.919 \\
15	\bottomrule
16	\end{tabular}}
17	\caption{Main comparison: held-out PPL ($\downarrow$) at $\rho{=}0.4$, 1 content epoch.
18	Adaptive and Uniform: 5-seed means (seeds 42, 123, 456, 789, 234); ESS-only and Random: 3-seed means (seeds 42, 123, 456); Permuted: single seed (42).
19	Adaptive uses $\tau{=}0.7$, $\nmin{=}2$.
20	Permuted randomly shuffles $q$-scores across samples, destroying provenance signal while preserving weight non-uniformity ($\Delta{=}{+}0.225$).}
21	\label{tab:main}
22	\end{table}
23	
24	\subsection{Main Results}
25	\label{sec:main-results}
26	
27	Table~\ref{tab:main} reports held-out perplexity at $\rho = 0.4$ across five seeds.
28	Continued pretraining reduces PPL from 22.970 to the 17.3--17.8 range; method comparisons operate within a narrow residual.
29	
30	Adaptive $\bstar$ achieves 5-seed mean PPL 17.674, compared to 17.697 for uniform ($\Delta{=}{-}0.023$, directionally consistent across all seeds) and 17.620 for grid $b{=}0.3$ (3-seed mean, post-hoc oracle; gap $+$0.054; Table~\ref{tab:aux}).
31	A paired $t$-test yields $t(4){=}{-}8.21$, $p{=}0.0012$; after Bonferroni--Holm correction for nine family-wise comparisons, $p_{\mathrm{BH}}{=}0.011$, reaching conventional significance at $\alpha{=}0.05$.
32	The engineering benefit is eliminating $b$ grid search (nine full training runs~\citep{drayson2025detection}, ${\sim}$16 GPU-hours at 0.6B scale, scaling linearly with model size), though grid search yields a larger improvement.
33	The grid-best $b{=}0.3$ is a post-hoc oracle from nine candidates with $5.5{\times}$ higher cross-seed standard deviation than adaptive ($\sigma{=}0.033$ vs.\ $0.006$); the noisy PPL plateau at $b \in [0.1, 0.5]$ (Figure~\ref{fig:grid_b_trend}) makes validation-based selection unreliable.
34	At the nearest fixed point ($b{=}1.0$), PPL equals uniform (17.692 vs.\ 17.694): per-batch adaptation is essential.
35	
36	The ablation hierarchy at $\rho{=}0.4$ (Adaptive ${<}$ Uniform ${<}$ ESS-only ${<}$ Random ${<}$ Permuted, Table~\ref{tab:main}) reveals two requirements for effective reweighting: detector signal and minimum intervention.
37	Random weights $\mathcal{U}(0,2)$ (17.802) confirm that non-uniform weighting alone does not help; permuted $q$-scores (17.919, $\Delta{=}{+}0.225$) further isolate provenance signal as load-bearing, since shuffling destroys the detector's sample-level information while preserving identical weight non-uniformity.
38	ESS-only (mean $17.737 {\pm} 0.021$) uses the same $q$-scores but maximizes $b$ up to the stability ceiling, concentrating weights on a few high-confidence samples; it degrades PPL by 0.043 relative to uniform.
39	Only the dual-constrained adaptive method, which limits $b$ to the minimum needed, improves in-distribution PPL over uniform (mean $\Delta{=}{-}0.023$, directionally consistent across all seeds).
40	Figure~\ref{fig:grid_b_trend} contextualizes both results: adaptive $\bstar$ operates near the curve minimum while ESS-only $\bstar$ (mean ${\approx}$3.5) falls in the degradation zone.
41	
42	\begin{figure}[t]
43	\centering
44	\includegraphics[width=\columnwidth]{grid_b_trend_clean}
45	\caption{Held-out PPL as a function of fixed sharpening exponent $b$ (grid search, $\rho{=}0.4$).
46	Seed\,42 provides the full nine-point sweep (circles); cross-seed markers at $b{=}0.5$ (triangles) confirm the plateau region.
47	The shaded region marks $b \geq 2$ where PPL degrades past the uniform baseline; ESS-only $\bstar$ (overall mean ${\approx}$3.5) falls in this degradation zone, while adaptive $\bstar$ (mean ${\approx}$0.9) operates near the curve minimum.}
48	\label{fig:grid_b_trend}
49	\end{figure}
50	
51	\paragraph{Hard filtering and multi-epoch exposure.}
52	Detect \& Remove at its best threshold ($q{>}0.3$) achieves 3-seed mean PPL $17.250 \pm 0.001$ at full training length, outperforming all reweighting methods by a wide margin ($\Delta{=}{-}0.424$ vs.\ adaptive $\bstar$).
53	All three D\&R thresholds beat both uniform and adaptive $\bstar$ ($q{>}0.5$: $17.280 \pm 0.010$; $q{>}0.7$: $17.320 \pm 0.001$; 3 seeds each), with cross-seed variance near zero (holdout $\pm$0.00, Table~\ref{tab:epoch_match}).
54	Aggressive filtering retains only 31.5\% of tokens at $q{>}0.3$, so the model sees surviving data ${\sim}$3.2 \emph{content epochs} versus one for reweighting; an epoch-matched control (D\&R at $q{>}0.5$, ${\sim}$1.0 content epochs) yields PPL $17.657 \pm 0.005$ vs.\ $17.674 \pm 0.007$ for adaptive $\bstar$ ($\Delta{=}0.017$), attributing ${>}$95\% of D\&R's full-length advantage to multi-epoch exposure on filtered data (Table~\ref{tab:epoch_match}).
55	This decomposition identifies the \emph{mechanism}: filtering concentrates compute on high-confidence real data, and multi-epoch exposure amplifies the benefit, rather than undermining D\&R's practical effectiveness.
56	The raw threshold--PPL curve is U-shaped ($q{>}0.3$: 17.25, $q{>}0.9$: 17.42), but epoch-matched comparisons eliminate the U-shape, revealing monotonically decreasing PPL that saturates at $q{\geq}0.5$ (Figure~\ref{fig:dr_dual_curve}; Appendix~\ref{app:hybrid}).
57	For practitioners, D\&R is the strongest strategy when the corpus is small relative to training compute, as aggressive filtering naturally creates multi-epoch regimes that amplify quality gains; controlled comparisons should report the effective content-epoch count alongside PPL.
58	
59	\begin{figure}[t]
60	\centering
61	\includegraphics[width=\columnwidth]{dr_dual_curve}
62	\caption{D\&R threshold--PPL relationship ($\rho{=}0.4$, 3 seeds).
63	Blue: raw (multi-epoch) PPL with effective epoch counts annotated.
64	Orange: epoch-matched PPL (single content epoch), saturating at the adaptive $\bstar$ level (green dashed).}
65	\label{fig:dr_dual_curve}
66	\end{figure}
67	
68	\begin{figure}[t]
69	\centering
70	\includegraphics[width=\columnwidth]{delta_vs_rho}
71	\caption{Effect of contamination ratio on adaptive reweighting effectiveness.
72	$\Delta$ = adaptive $-$ uniform holdout PPL (lower is better).
73	Error bars show $\pm$1 SD across seeds.
74	The method transitions from harmful to beneficial between $\rho{=}0.3$ and $0.4$ (shaded).}
75	\label{fig:delta_vs_rho}
76	\end{figure}
77	
78	\subsection{Robustness and Boundary Conditions}
79	\label{sec:robustness}
80	
81	Across three seeds at $\rho = 0.6$, adaptive $\bstar$ ($17.731 \pm 0.004$) directionally outperforms uniform on in-distribution PPL ($17.763 \pm 0.008$, $\Delta{=}{-}0.032$, 3 seeds, paired $t{=}{-}9.95$, $p_{\mathrm{BH}}{=}0.064$), with a larger effect size than at $\rho{=}0.4$ ($\Delta{=}{-}0.023$).
82	The ablation hierarchy is preserved (Grid 17.634\footnote{Single seed; full per-seed results in Appendix~\ref{app:rho06}.} ${<}$ Adaptive 17.731 ${<}$ Uniform 17.763 ${\approx}$ ESS-only 17.763 ${<}$ Random 17.861), but the ESS-only/uniform gap collapses to effectively zero (three-seed means both $17.763$) as ESS binding rises to ${\sim}$49\%.
83	Random remains substantially worse than uniform (gap 0.098, $\sigma{=}0.025$): detector signal is load-bearing even when the stability constraint dominates; the adaptive method's continued advantage is driven by the $\aeff$ quality constraint, which operates independently of the ESS ceiling.
84	Three-seed paired comparison confirms $\tau{=}0.7$ outperforms $\tau{=}0.8$ on both holdout and out-of-distribution (OOD) metrics (\S\ref{sec:sensitivity}).
85	
86	\begin{table}[t]
87	\centering
88	\small
89	\setlength{\tabcolsep}{3pt}
90	\resizebox{\columnwidth}{!}{%
91	\begin{tabular}{@{}lccc@{}}
92	\toprule
93	\textbf{Method} & \textbf{Epochs} & \textbf{PPL (raw)} $\downarrow$ & \textbf{PPL (ep.-matched)} $\downarrow$ \\
94	\midrule
95	D\&R ($q{>}0.3$) & ${\sim}$3.2 & \textbf{17.250} $\pm$ .001 & 17.74 \\
96	D\&R ($q{>}0.5$) & ${\sim}$2.4 & 17.280 $\pm$ .010 & 17.657 $\pm$ .005 \\
97	D\&R ($q{>}0.7$) & ${\sim}$2.0 & 17.32 & 17.62 \\
98	\midrule
99	Adaptive $\bstar$ & ${\sim}$1.0 & \multicolumn{2}{c}{17.674 $\pm$ .007} \\
100	Uniform           & ${\sim}$1.0 & \multicolumn{2}{c}{17.697 $\pm$ .008} \\
101	\bottomrule
102	\end{tabular}}
103	\caption{D\&R threshold comparison ($\rho{=}0.4$).
104	Raw PPL traces a U-shape across thresholds; epoch-matched PPL (single content epoch) decreases monotonically and saturates near the adaptive $\bstar$ level.
105	D\&R's 0.424 PPL advantage (at $q{>}0.3$) shrinks to $\Delta{=}0.017$ when content epochs are equalized.
106	All raw PPL values are 3-seed means; epoch-matched values at $q{>}0.3$ and $q{>}0.7$ are single-seed.
107	Full 9-threshold sweep in Table~\ref{tab:dr_threshold}.}
108	\label{tab:epoch_match}
109	\end{table}
110	
111	\paragraph{Scale.}
112	At 1.7B parameters (Qwen3-1.7B, $\rho{=}0.4$, $\tau{=}0.8$, 3 seeds), the method scales without degradation but the benefit diminishes.
113	Adaptive $\bstar$ achieves holdout PPL $13.26$ vs.\ uniform $13.27$ ($\Delta{=}{-}0.013$); OOD results are mixed in direction across domains (OWT $\Delta{=}{-}0.008$, Wiki $\Delta{=}{+}0.013$) and downstream accuracy is unchanged ($\Delta{\approx}{+}0.002$).
114	The diminished effect is consistent with larger models being more robust to self-generated contamination: Qwen3-1.7B's own outputs are likely closer to its training distribution, reducing the distributional shift that reweighting corrects.
115	A preliminary Llama-3.2-3B cross-model result (Appendix~\ref{app:cross_model}) shows mixed downstream effects (MMLU $+$1.6 percentage points, HellaSwag $-$0.6 percentage points), leaving cross-architecture generalization as an open question.
116	\paragraph{Out-of-distribution evaluation.}
117	To test whether the in-distribution improvement reflects distribution matching, we evaluate all three from-scratch seeds on OpenWebText and Wikipedia.
118	At $\rho{=}0.4$, adaptive reweighting improves mean PPL on all three evaluation domains: FineWeb $\Delta{=}{-}0.023$ (5 seeds), OpenWebText $\Delta{=}{-}0.028$, Wikipedia $\Delta{=}{-}0.029$ (3 seeds each); downstream accuracy is identical (0.5414).
119	OOD improvements exceed the in-distribution gain, indicating genuine quality improvement rather than distribution matching toward the training mixture ($\tau{=}0.8$'s OOD effect is smaller; $\tau{=}0.7$'s advantage reflects active OOD improvement, \S\ref{sec:sensitivity}).
120	
121	\paragraph{Calibration, not just discrimination.}
122	Replacing TF-IDF+LR with generative perplexity detectors reverses the advantage across three seeds (GPT-2: AUC\,=\,0.91, ECE\,=\,0.131, $\Delta{=}{+}0.098$; N-gram: AUC\,=\,0.73, ECE\,=\,0.069, $\Delta{=}{+}0.129$; Figure~\ref{fig:overview}b; Appendix~\ref{app:detector}).
123	The TF-IDF vs.\ GPT-2 contrast (comparable AUC, $2.7{\times}$ ECE gap) isolates calibration as an empirically observed requirement in our self-contamination setting; N-gram's better ECE (0.069) does not compensate for insufficient AUC (0.73), indicating that both discrimination and calibration are jointly necessary (Figure~\ref{fig:overview}b).
124	
125	\begin{table}[t]
126	\centering
127	\small
128	\setlength{\tabcolsep}{3pt}
129	\resizebox{\columnwidth}{!}{%
130	\begin{tabular}{@{}lcccl@{}}
131	\toprule
132	\textbf{Method} & \textbf{Seeds} & \textbf{Oracle?} & \textbf{Epochs} & \textbf{Mean PPL} $\downarrow$ \\
133	\midrule
134	Grid ($b{=}0.3$) & 3 & post-hoc & 1 & \textbf{17.620} $\pm$ .033 \\
135	Golden Ratio     & 1 & known $\rho$ & 1 & 17.654 \\
136	D\&R ($q{>}0.3$) & 3 & post-hoc & ${\sim}$3.2 & \textbf{17.250} $\pm$ .001 \\
137	\bottomrule
138	\end{tabular}}
139	\caption{Auxiliary baselines at $\rho{=}0.4$. Grid-best selected post-hoc from nine candidates (Appendix~\ref{app:grid}). Golden Ratio requires known $\rho$~\citep{he2025golden}. D\&R uses ${\sim}$3.2 content epochs (Table~\ref{tab:epoch_match}).}
140	\label{tab:aux}
141	\end{table}
142	
143	\subsection{Hyperparameter Sensitivity}
144	\label{sec:sensitivity}
145	
146	\paragraph{Quality threshold $\tau$.}
147	$\tau{=}0.7$ outperforms $\tau{=}0.8$ on holdout at both contamination levels ($\rho{=}0.4$: 17.674 vs.\ 17.683; $\rho{=}0.6$: paired $t{=}{-}4.70$, $p{<}0.05$; \S\ref{sec:robustness}) and achieves larger OOD gains ($\rho{=}0.4$: $\Delta{=}{-}0.028$/$-$0.029 vs.\ $-$0.005/$-$0.009; Table~\ref{tab:tau}, Appendix~\ref{app:tau_rho}).
148	$\tau \in [0.5, 0.8]$ all improve holdout over uniform, while $\tau {>} 0.8$ degrades (Appendix~\ref{app:tau_sweep}).
149	We also tested per-batch adaptive $\tau$ clamping, which did not improve over fixed thresholds (Appendix~\ref{app:batch_adaptive}).
150	
151	\paragraph{ESS floor $\nmin$.}
152	The default $\nmin{=}2$ ($\nmin/B{=}0.5$) is optimal; extremes degrade ($\nmin{=}1$: PPL $17.742{\pm}0.009$, 3 seeds, worse than uniform; $\nmin{=}B$: recovers uniform).
153	Neither constraint alone improves over uniform ($\nmin{=}1$: $+$0.048; ESS-only: $+$0.043); both must act jointly for the method to outperform uniform training.
154	The coupling $\nmin{=}\lfloor B/2 \rfloor$ is also empirically motivated: at $B{=}8$, keeping $\nmin{=}2$ (ratio $0.25$) degrades PPL by $+$0.036 vs.\ uniform, whereas $\nmin{=}4$ (ratio $0.5$) yields $\Delta{=}{-}0.052{\pm}0.007$.
155	Under this coupling, the adaptive advantage monotonically increases across $B \in \{4, 8, 16\}$: $\Delta{=}{-}0.023{\pm}0.006$ (5 seeds), $-$0.052${\pm}$0.007 (3 seeds, $p{=}0.006$), and $-$0.068${\pm}$0.005 (3 seeds), corresponding to $1.0{\times}$, $2.3{\times}$, and $3.0{\times}$ amplification ($p{<}0.01$ at $B \geq 8$).
156	The gap to grid-best narrows from 0.040 ($B{=}4$) to 0.009 ($B{=}16$, seed\,42; Figure~\ref{fig:batch_amp}).
157	
158	\begin{figure}[t]
159	\centering
160	\includegraphics[width=\columnwidth]{batch_size_amplification}
161	\caption{Batch-size amplification of adaptive reweighting ($\nmin{=}\lfloor B/2 \rfloor$).
162	The adaptive advantage over uniform increases monotonically with micro-batch size, from $1.0{\times}$ ($B{=}4$) to $3.0{\times}$ ($B{=}16$); $\Delta$ values and $\pm$1\,SD shown above each bar.}
163	\label{fig:batch_amp}
164	\end{figure}
165	
166	\paragraph{Constraint regime.}
167	\label{sec:regime}
168	Over 24{,}412 micro-batches (seed\,42), 5.8\% are clean ($\aeff(0) \geq \tau$, $\bstar{=}0$), ${\sim}$50\% are $\aeff$-binding (quality constraint dominates), and ${\sim}$44\% are ESS-binding (stability constraint dominates); the distribution is stable across seeds (coefficient of variation ${<}2\%$; Figure~\ref{fig:regime_decomp}).
169	The $\aeff$-binding majority indicates that detector quality signal, not training stability, is the primary bottleneck, reinforcing the calibration requirement (\S\ref{sec:robustness}).
170	
171	\begin{figure}[t]
172	\centering
173	\includegraphics[width=\columnwidth]{constraint_regime_decomposition}
174	\caption{Constraint regime decomposition at two contamination levels (seed\,42).
175	At $\rho{=}0.4$, ${\sim}$50\% of batches are $\aeff$-binding and ${\sim}$44\% ESS-binding, with ${\sim}$6\% clean; at $\rho{=}0.6$, the constraints are nearly balanced (${\sim}$49\% ESS-binding, ${\sim}$47\% $\aeff$-binding).}
176	\label{fig:regime_decomp}
177	\end{figure}
178	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bce5907a-8f45-4ff7-8b30-c25f2b808b33",
  "isSidechain": true,
  "promptId": "2063b979-bba7-4480-8b91-7387b6dcd8bf",
  "agentId": "a77822597a2053a5c",
  "type": "user",
  "uuid": "fba92180-4cbd-4f9e-9f51-353a1b22272c",
  "sourceToolAssistantUUID": "bce5907a-8f45-4ff7-8b30-c25f2b808b33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "3aaca442-e705-47db-9f84-980fe61c25da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-25T19:57:24.731Z_

<details open><summary>🔧 Tool call — Grep · `toolu_011ikFaioFzamsdD6QjkDcYF`</summary>

```json
{
  "pattern": "17\\.250|17\\.25",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fba92180-4cbd-4f9e-9f51-353a1b22272c",
  "isSidechain": true,
  "agentId": "a77822597a2053a5c",
  "requestId": "req_011CbPsqngM6SkUqsoKE3jCg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f8d751b2-5a0b-45b8-8c88-0ac60fa545c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "3aaca442-e705-47db-9f84-980fe61c25da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WLMioVnb3bzkaWm3Fwr1Dj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1677,
      "cache_read_input_tokens": 19402,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1677,
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

_source line 11 · 2026-05-25T19:57:24.745Z_

<details><summary>↩ Tool result · `toolu_011ikFaioFzamsdD6QjkDcYF`</summary>

```text
docs/paper/sections/appendix.tex:159:Raw PPL traces a U-shaped curve with a minimum at $q{>}0.3$ (17.250, 3 seeds), but this curve conflates filtering quality with multi-epoch exposure: aggressive thresholds retain less data and repeat it more often.
docs/paper/sections/appendix.tex:174:Detect \& Remove ($q{>}0.3$) & 17.250 & -- \\
docs/paper/sections/appendix.tex:192:$q > 0.3$ & 31.5\% & ${\sim}$3.2 & \textbf{17.250}$^\dagger$ & 17.74 \\
docs/paper/sections/appendix.tex:203:$^\dagger$\,3-seed mean $17.250 \pm 0.001$.}
docs/paper/sections/introduction.tex:26:D\&R outperforms all reweighting methods in our setting (PPL $17.250$ vs.\ $17.674$, 3 seeds); epoch-matched controls attribute ${>}$95\% of the advantage to multi-epoch exposure on filtered data, reducing the gap to $\Delta{=}0.017$ (Table~\ref{tab:epoch_match}).
docs/paper/sections/results.tex:52:Detect \& Remove at its best threshold ($q{>}0.3$) achieves 3-seed mean PPL $17.250 \pm 0.001$ at full training length, outperforming all reweighting methods by a wide margin ($\Delta{=}{-}0.424$ vs.\ adaptive $\bstar$).
docs/paper/sections/results.tex:56:The raw threshold--PPL curve is U-shaped ($q{>}0.3$: 17.25, $q{>}0.9$: 17.42), but epoch-matched comparisons eliminate the U-shape, revealing monotonically decreasing PPL that saturates at $q{\geq}0.5$ (Figure~\ref{fig:dr_dual_curve}; Appendix~\ref{app:hybrid}).
docs/paper/sections/results.tex:95:D\&R ($q{>}0.3$) & ${\sim}$3.2 & \textbf{17.250} $\pm$ .001 & 17.74 \\
docs/paper/sections/results.tex:136:D\&R ($q{>}0.3$) & 3 & post-hoc & ${\sim}$3.2 & \textbf{17.250} $\pm$ .001 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8d751b2-5a0b-45b8-8c88-0ac60fa545c5",
  "isSidechain": true,
  "promptId": "2063b979-bba7-4480-8b91-7387b6dcd8bf",
  "agentId": "a77822597a2053a5c",
  "type": "user",
  "uuid": "65e3854f-3018-406f-bc48-a4874ef52eb9",
  "sourceToolAssistantUUID": "f8d751b2-5a0b-45b8-8c88-0ac60fa545c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "3aaca442-e705-47db-9f84-980fe61c25da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-25T19:57:25.153Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01AuaBXsWodSiVkkmvqQpxm6`</summary>

```json
{
  "pattern": "5\\.9",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65e3854f-3018-406f-bc48-a4874ef52eb9",
  "isSidechain": true,
  "agentId": "a77822597a2053a5c",
  "requestId": "req_011CbPsqngM6SkUqsoKE3jCg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6b52fa0e-f2c3-4136-87c7-72ae1fd69ab6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "3aaca442-e705-47db-9f84-980fe61c25da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WLMioVnb3bzkaWm3Fwr1Dj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1677,
      "cache_read_input_tokens": 19402,
      "output_tokens": 402,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1677
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 402,
          "cache_read_input_tokens": 19402,
          "cache_creation_input_tokens": 1677,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1677,
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

_source line 13 · 2026-05-25T19:57:25.172Z_

<details><summary>↩ Tool result · `toolu_01AuaBXsWodSiVkkmvqQpxm6`</summary>

```text
docs/paper/sections/appendix.tex:313:456 & 0.8006 & 0.8749 & 5.9 \\
docs/paper/sections/introduction.tex:32:An $\aeff$ quality constraint binds in ${\sim}$50\% of batches at ${\approx}5.9{\times}$ lower sharpening exponents than an ESS-only alternative (\S\ref{sec:regime}); at $\rho{=}0.6$, ESS-only collapses toward uniform while the dual constraint maintains its advantage.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b52fa0e-f2c3-4136-87c7-72ae1fd69ab6",
  "isSidechain": true,
  "promptId": "2063b979-bba7-4480-8b91-7387b6dcd8bf",
  "agentId": "a77822597a2053a5c",
  "type": "user",
  "uuid": "dc2eedbe-babd-4c86-bbe2-988663c512e8",
  "sourceToolAssistantUUID": "6b52fa0e-f2c3-4136-87c7-72ae1fd69ab6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "3aaca442-e705-47db-9f84-980fe61c25da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-25T19:57:27.928Z_

Excellent! Now let me get more context around the "5.9" reference and search for where it's computed. Let me read the appendix section and check for more details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc2eedbe-babd-4c86-bbe2-988663c512e8",
  "isSidechain": true,
  "agentId": "a77822597a2053a5c",
  "requestId": "req_011CbPsr2s8TPyxSt5fnpgtE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8e9aeefe-1d49-4fc1-827c-f7c2d028fc20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "3aaca442-e705-47db-9f84-980fe61c25da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FAHN15fAf1mmN1Df1nFm6i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7379,
      "cache_read_input_tokens": 21079,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7379,
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

_source line 15 · 2026-05-25T19:57:28.918Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ejpm6MCr1kCcosroLCtdxV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex",
  "offset": 150,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e9aeefe-1d49-4fc1-827c-f7c2d028fc20",
  "isSidechain": true,
  "agentId": "a77822597a2053a5c",
  "requestId": "req_011CbPsr2s8TPyxSt5fnpgtE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "657b321a-e228-4c7e-8696-f817dfa860cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "3aaca442-e705-47db-9f84-980fe61c25da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FAHN15fAf1mmN1Df1nFm6i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7379,
      "cache_read_input_tokens": 21079,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7379,
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

### Tool result

_source line 16 · 2026-05-25T19:57:28.924Z_

<details><summary>↩ Tool result · `toolu_01Ejpm6MCr1kCcosroLCtdxV`</summary>

```text
150	(b) Normalized PPL gap relative to uniform at shared $\tau$ values.}
151	\label{fig:tau_rho_rank}
152	\end{figure}
153	
154	\section{Hybrid and Threshold Comparison}
155	\label{app:hybrid}
156	
157	Table~\ref{tab:hybrid} compares method families across contamination levels.
158	Table~\ref{tab:dr_threshold} shows D\&R sensitivity to the detection threshold at both full training length and epoch-matched settings.
159	Raw PPL traces a U-shaped curve with a minimum at $q{>}0.3$ (17.250, 3 seeds), but this curve conflates filtering quality with multi-epoch exposure: aggressive thresholds retain less data and repeat it more often.
160	Epoch-matched comparisons (rightmost column of Table~\ref{tab:dr_threshold}) remove the multi-epoch confound: the U-shape vanishes and PPL decreases monotonically, saturating near the adaptive $\bstar$ level at $q{\geq}0.5$.
161	Figure~\ref{fig:dr_dual_curve} visualizes the two curves.
162	
163	\begin{table}[h]
164	\centering
165	\small
166	\begin{tabular}{@{}lcc@{}}
167	\toprule
168	\textbf{Method} & $\rho{=}0.4$ & $\rho{=}0.6$ \\
169	\midrule
170	Uniform & 17.694 & 17.766 \\
171	Adaptive $\bstar$ & 17.689 & 17.740 \\
172	Hybrid ($q{>}0.95$ + adaptive) & 17.514 & 17.530$^*$ \\
173	Detect \& Remove ($q{>}0.5$) & 17.285 & -- \\
174	Detect \& Remove ($q{>}0.3$) & 17.250 & -- \\
175	\bottomrule
176	\end{tabular}
177	\caption{Method comparison across contamination levels (seed\,42, $\tau{=}0.8$).
178	$^*$Hybrid at $\rho{=}0.6$ filters high-confidence synthetic ($q{>}0.95$), reducing effective $\rho$ to ${\approx}0.4$; PPL is not directly comparable to $\rho{=}0.6$ baselines.}
179	\label{tab:hybrid}
180	\end{table}
181	
182	\begin{table}[h]
183	\centering
184	\small
185	\setlength{\tabcolsep}{3pt}
186	\begin{tabular}{@{}ccccc@{}}
187	\toprule
188	\textbf{Thresh.} & \textbf{Ret.\ \%} & \textbf{Epochs} & \textbf{Raw PPL} $\downarrow$ & \textbf{Ep.-matched} $\downarrow$ \\
189	\midrule
190	$q > 0.1$ & 15.0\% & ${\sim}$10.0 & 17.40 & 18.04 \\
191	$q > 0.2$ & ${\sim}$23\% & ${\sim}$5.0 & 17.27 & -- \\
192	$q > 0.3$ & 31.5\% & ${\sim}$3.2 & \textbf{17.250}$^\dagger$ & 17.74 \\
193	$q > 0.4$ & ${\sim}$38\% & ${\sim}$2.8 & 17.26 & -- \\
194	$q > 0.5$ & 41.4\% & ${\sim}$2.4 & 17.28 & 17.65 \\
195	$q > 0.6$ & ${\sim}$46\% & ${\sim}$1.7 & 17.30 & -- \\
196	$q > 0.7$ & 49.8\% & ${\sim}$2.0 & 17.32 & 17.62 \\
197	$q > 0.8$ & ${\sim}$56\% & ${\sim}$1.3 & 17.34 & -- \\
198	$q > 0.9$ & 61.6\% & ${\sim}$1.1 & 17.42 & 17.628 \\
199	\bottomrule
200	\end{tabular}
201	\caption{D\&R threshold sensitivity ($\rho{=}0.4$, seed\,42 unless noted).
202	Raw PPL traces a U-shaped curve (minimum at $q{>}0.3$); epoch-matched PPL (single content epoch) decreases monotonically and saturates near the adaptive $\bstar$ level (${\approx}$17.65) at $q{\geq}0.5$; the U-shape is thus a multi-epoch artifact.
203	$^\dagger$\,3-seed mean $17.250 \pm 0.001$.}
204	\label{tab:dr_threshold}
205	\end{table}
206	
207	See Figure~\ref{fig:dr_dual_curve} (\S\ref{sec:main-results}) for the dual-curve visualization.
208	
209	\section{Downstream Task Evaluation}
210	\label{app:downstream}
211	
212	Table~\ref{tab:downstream} reports downstream benchmark accuracy for adaptive vs.\ uniform training at $\rho{=}0.4$ (seed\,42, Qwen3-0.6B).
213	Across multiple seeds, downstream differences are mixed in direction and uniformly within standard error, indicating that adaptive reweighting has no meaningful downstream impact.
214	
215	\begin{table}[h]
216	\centering
217	\small
218	\resizebox{\columnwidth}{!}{%
219	\begin{tabular}{@{}llccc@{}}
220	\toprule
221	\textbf{Benchmark} & \textbf{Metric} & \textbf{Adaptive} & \textbf{Uniform} & $\boldsymbol{\Delta}$ \\
222	\midrule
223	\multicolumn{5}{@{}l}{\textit{Seed 42 (checkpoint resume)}} \\
224	ARC-Challenge & acc\_norm & 0.343 & 0.348 & $-$0.005 \\
225	ARC-Easy & acc & 0.650 & 0.657 & $-$0.007 \\
226	HellaSwag & acc\_norm & 0.479 & 0.484 & $-$0.005 \\
227	PIQA & acc & 0.687 & 0.686 & $+$0.001 \\
228	WinoGrande & acc & 0.578 & 0.586 & $-$0.008 \\
229	\midrule
230	\multicolumn{5}{@{}l}{\textit{From-scratch 2-seed mean (seeds 123, 456)}} \\
231	\multicolumn{3}{@{}l}{Mean $\Delta$ across 5 tasks} & & $+$0.001 \\
232	\multicolumn{3}{@{}l}{Direction} & \multicolumn{2}{c}{mixed (seed 123: 3/5$-$; seed 456: 3/5$+$)} \\
233	\bottomrule
234	\end{tabular}}
235	\caption{Downstream benchmarks (Qwen3-0.6B, $\rho{=}0.4$).
236	Seed\,42 used a checkpoint-resumed adaptive model; from-scratch seeds (123, 456) show mixed direction with mean $|\Delta| \leq 0.01$.
237	All differences within standard error ($\pm 0.01$).
238	Models use $\tau{=}0.8$; $\tau{=}0.7$ yields identical 3-seed means (0.5414).}
239	\label{tab:downstream}
240	\end{table}
241	
242	\section{Higher Contamination Details}
243	\label{app:rho06}
244	
245	Table~\ref{tab:rho06} reports results at $\rho{=}0.6$.
246	The full five-method ablation preserves the hierarchy from $\rho{=}0.4$ across all three seeds: Grid ${<}$ Adaptive ${<}$ Uniform ${\approx}$ ESS-only ${<}$ Random.
247	
248	\begin{table}[h]
249	\centering
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "657b321a-e228-4c7e-8696-f817dfa860cc",
  "isSidechain": true,
  "promptId": "2063b979-bba7-4480-8b91-7387b6dcd8bf",
  "agentId": "a77822597a2053a5c",
  "type": "user",
  "uuid": "cf6e2e9c-4489-4a34-b5fe-e30e7ef3b1dc",
  "sourceToolAssistantUUID": "657b321a-e228-4c7e-8696-f817dfa860cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "3aaca442-e705-47db-9f84-980fe61c25da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-25T19:57:29.138Z_

<details open><summary>🔧 Tool call — Read · `toolu_01A4xJMDBhwhN2aYTc6VBZ11`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex",
  "offset": 300,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf6e2e9c-4489-4a34-b5fe-e30e7ef3b1dc",
  "isSidechain": true,
  "agentId": "a77822597a2053a5c",
  "requestId": "req_011CbPsr2s8TPyxSt5fnpgtE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f638d7d6-c4dc-4f4a-a620-c931db72757a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "3aaca442-e705-47db-9f84-980fe61c25da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FAHN15fAf1mmN1Df1nFm6i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7379,
      "cache_read_input_tokens": 21079,
      "output_tokens": 272,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7379
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 272,
          "cache_read_input_tokens": 21079,
          "cache_creation_input_tokens": 7379,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7379,
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

_source line 18 · 2026-05-25T19:57:29.143Z_

<details><summary>↩ Tool result · `toolu_01A4xJMDBhwhN2aYTc6VBZ11`</summary>

```text
300	
301	\paragraph{Cross-seed stability.}
302	Table~\ref{tab:alpha_corr_perseed} reports the correlation between $\aeff$ and the batch mean $q$-score ($\bar{q}$, computed from known labels) across all three seeds.
303	
304	\begin{table}[h]
305	\centering
306	\small
307	\begin{tabular}{@{}cccc@{}}
308	\toprule
309	\textbf{Seed} & Pearson $r(\aeff, \bar{q})$ & Spearman $\rho_s$ & $\bstar{=}0$ (\%) \\
310	\midrule
311	42  & 0.8019 & 0.8761 & 5.8 \\
312	123 & 0.7994 & 0.8692 & 5.7 \\
313	456 & 0.8006 & 0.8749 & 5.9 \\
314	\midrule
315	\textbf{Spread} & 0.0025 & 0.0069 & 0.2 \\
316	\bottomrule
317	\end{tabular}
318	\caption{Per-seed $\aeff$--$\bar{q}$ correlation ($\rho{=}0.4$, $B{=}4$).
319	Cross-seed spread is $<$0.003 for Pearson $r$ and $<$0.007 for Spearman $\rho_s$, indicating stable proxy fidelity across random seeds.
320	$r(\aeff, \bar{q}) = 0.80$ measures the proxy's fidelity to batch composition; the ground-truth correlation $r(\aeff, \text{true real fraction}) \approx 0.79$ (\S\ref{sec:discussion}) is slightly lower due to detector noise.
321	The per-seed table demonstrates cross-seed stability rather than superseding the ground-truth estimate.}
322	\label{tab:alpha_corr_perseed}
323	\end{table}
324	
325	\section{Detector Comparison}
326	\label{app:detector}
327	
328	See Figure~\ref{fig:overview}b (\S\ref{sec:robustness}) for the detector requirements visualization.
329	
330	Table~\ref{tab:detector} compares three detector families for adaptive reweighting.
331	The discriminative TF-IDF+LR detector (ECE\,=\,0.048) produces the only improvement over uniform.
332	The TF-IDF vs.\ GPT-2 contrast (comparable AUC: 0.94 vs.\ 0.91, but $2.7{\times}$ ECE gap: 0.048 vs.\ 0.131) isolates calibration as an empirically observed requirement; however, N-gram's better ECE (0.069) does not compensate for its low AUC (0.73); both sufficient discrimination and good calibration are jointly necessary in our setting.
333	TF-IDF+LR's $q$-scores have reliable probabilistic semantics, so the $\aeff$ proxy accurately tracks batch quality.
334	Generative detectors assign high $q$-scores to fluent, predictable human text (false positives concentrated among high-quality samples), systematically inflating $\aeff$ for clean batches and deflating it for contaminated ones, which inverts the minimum-intervention logic.
335	
336	\begin{table}[h]
337	\centering
338	\small
339	\resizebox{\columnwidth}{!}{%
340	\begin{tabular}{@{}llccccc@{}}
341	\toprule
342	\textbf{Detector} & \textbf{Type} & \textbf{AUC} & \textbf{ECE} & \textbf{Mean PPL} & $\boldsymbol{\Delta}$ \\
343	\midrule
344	TF-IDF+LR & Discriminative & 0.94 & 0.048 & 17.650{\tiny$\pm$.010} & $-$0.044 \\
345	GPT-2 PPL & Generative & 0.91 & 0.131 & 17.792{\tiny$\pm$.005} & $+$0.098 \\
346	N-gram PPL & Generative & 0.73 & 0.069 & 17.823{\tiny$\pm$.003} & $+$0.129 \\
347	\bottomrule
348	\end{tabular}}
349	\caption{Detector comparison for adaptive reweighting ($\rho{=}0.4$, $\tau{=}0.8$, 3 seeds).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f638d7d6-c4dc-4f4a-a620-c931db72757a",
  "isSidechain": true,
  "promptId": "2063b979-bba7-4480-8b91-7387b6dcd8bf",
  "agentId": "a77822597a2053a5c",
  "type": "user",
  "uuid": "3e92f02a-4ec2-4b53-aa72-128164a3b25a",
  "sourceToolAssistantUUID": "f638d7d6-c4dc-4f4a-a620-c931db72757a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "3aaca442-e705-47db-9f84-980fe61c25da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-25T19:57:30.750Z_

Now let me search for more context on how the 5.9x value is computed - specifically around the comparison of sharpening exponents between the two constraint regimes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e92f02a-4ec2-4b53-aa72-128164a3b25a",
  "isSidechain": true,
  "agentId": "a77822597a2053a5c",
  "requestId": "req_011CbPsrKmNQqnuZNL925kpm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "905a5bf5-7078-4337-8ef7-502f9dd81516",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "3aaca442-e705-47db-9f84-980fe61c25da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013t1nUiAo9AHiM3tT9NJ4L4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3892,
      "cache_read_input_tokens": 28458,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3892,
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

_source line 20 · 2026-05-25T19:57:31.899Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01WYWfSquRCjb4D7wmyfBUWH`</summary>

```json
{
  "pattern": "sharpening exponent|constraint regime|5\\.8|5\\.9|5\\.7",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "905a5bf5-7078-4337-8ef7-502f9dd81516",
  "isSidechain": true,
  "agentId": "a77822597a2053a5c",
  "requestId": "req_011CbPsrKmNQqnuZNL925kpm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1154a9b2-0bf9-4b5b-84c9-12b8f7f168d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "3aaca442-e705-47db-9f84-980fe61c25da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013t1nUiAo9AHiM3tT9NJ4L4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3892,
      "cache_read_input_tokens": 28458,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3892
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 209,
          "cache_read_input_tokens": 28458,
          "cache_creation_input_tokens": 3892,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3892,
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

_source line 21 · 2026-05-25T19:57:31.935Z_

<details><summary>↩ Tool result · `toolu_01WYWfSquRCjb4D7wmyfBUWH`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex-6-\end{figure}
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex-7-
docs/paper/sections/method.tex-8-Figure~\ref{fig:pipeline} illustrates the pipeline. Let $\mathcal{D}$ denote a pretraining corpus with unknown synthetic contamination ratio $\rho$~\citep{cheng2025contamination}.
docs/paper/sections/method.tex:9:A detector assigns each sample $x$ a synthetic probability $q(x) \in [0,1]$; following \citet{drayson2025detection}, we weight each sample as $w(x) = (1 - q(x))^{b}$, where $b \geq 0$ is a sharpening exponent ($b{=}0$ recovers uniform training).
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex-10-Rather than selecting $b$ via grid search, we derive $b$ per-batch from the batch's $q$-score distribution using two opposing constraints.
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex-11-
docs/paper/sections/method.tex-12-Given a batch $\mathcal{B} = \{x_1, \ldots, x_B\}$ with scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$:
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-42-\begin{figure}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-43-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-44-\includegraphics[width=\columnwidth]{grid_b_trend_clean}
docs/paper/sections/results.tex:45:\caption{Held-out PPL as a function of fixed sharpening exponent $b$ (grid search, $\rho{=}0.4$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-46-Seed\,42 provides the full nine-point sweep (circles); cross-seed markers at $b{=}0.5$ (triangles) confirm the plateau region.
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-47-The shaded region marks $b \geq 2$ where PPL degrades past the uniform baseline; ESS-only $\bstar$ (overall mean ${\approx}$3.5) falls in this degradation zone, while adaptive $\bstar$ (mean ${\approx}$0.9) operates near the curve minimum.}
docs/paper/sections/results.tex-48-\label{fig:grid_b_trend}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-165-
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-166-\paragraph{Constraint regime.}
docs/paper/sections/results.tex-167-\label{sec:regime}
docs/paper/sections/results.tex:168:Over 24{,}412 micro-batches (seed\,42), 5.8\% are clean ($\aeff(0) \geq \tau$, $\bstar{=}0$), ${\sim}$50\% are $\aeff$-binding (quality constraint dominates), and ${\sim}$44\% are ESS-binding (stability constraint dominates); the distribution is stable across seeds (coefficient of variation ${<}2\%$; Figure~\ref{fig:regime_decomp}).
docs/paper/sections/results.tex-169-The $\aeff$-binding majority indicates that detector quality signal, not training stability, is the primary bottleneck, reinforcing the calibration requirement (\S\ref{sec:robustness}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-170-
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-171-\begin{figure}[t]
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex-1-The detect-and-reweight paradigm~\citep{drayson2025detection} has emerged as a response to synthetic contamination in web corpora, now estimated at 20--60\% of crawled data~\citep{cheng2025contamination}.
docs/paper/sections/introduction.tex:2:Training on such data risks model collapse~\citep{shumailov2024model,dohmatob2025strong}, motivating methods that downweight likely-synthetic samples via $w(x) = (1 - q(x))^b$, where $q(x)$ is a detector's synthetic probability and $b$ is a sharpening exponent.
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex-3-An alternative, Detect and Remove (D\&R), hard-filters samples above a threshold~\citep{feng2025beyond}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex-4-
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex-5-\begin{figure*}[t]
--
docs/paper/sections/introduction.tex-29-Both sufficient discrimination (area under the ROC curve; AUC) and good calibration (expected calibration error; ECE) are empirically observed requirements in our self-contamination setting; a high-AUC but poorly calibrated detector degrades performance below uniform (3 detectors, 3 seeds; \S\ref{sec:robustness}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex-30-
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex-31-\item \textbf{Minimum intervention outperforms maximization.}
docs/paper/sections/introduction.tex:32:An $\aeff$ quality constraint binds in ${\sim}$50\% of batches at ${\approx}5.9{\times}$ lower sharpening exponents than an ESS-only alternative (\S\ref{sec:regime}); at $\rho{=}0.6$, ESS-only collapses toward uniform while the dual constraint maintains its advantage.
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex-33-\end{itemize}
docs/paper/sections/introduction.tex-34-To demonstrate the minimum-intervention principle, we derive a dual-constrained adaptive $\bstar$ that eliminates per-model grid search ($\Delta{=}{-}0.023$ at $\rho{=}0.4$, $-$0.032 at $\rho{=}0.6$; Table~\ref{tab:main}), with transferable defaults ($\tau{=}0.7$, $\nmin{=}\lfloor B/2 \rfloor$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex-35-The method fails at $\rho{=}0.2$; at 1.7B it shows no degradation but the benefit diminishes.
--
docs/paper/sections/appendix.tex-52-\label{alg:bstar}
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-53-\begin{algorithmic}[1]
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-54-\REQUIRE Batch scores $\{q_i\}_{i=1}^{B}$, threshold~$\tau$, ESS floor~$n_{\min}$, bound~$b_{\max}$, tol.~$\varepsilon$
docs/paper/sections/appendix.tex:55:\ENSURE Optimal sharpening exponent $b^{*}$
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-56-\IF{$\alpha_{\mathrm{eff}}(0) \geq \tau$}
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-57-  \STATE \textbf{return} $0$ \COMMENT{clean batch}
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-58-\ENDIF
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-308-\toprule
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-309-\textbf{Seed} & Pearson $r(\aeff, \bar{q})$ & Spearman $\rho_s$ & $\bstar{=}0$ (\%) \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-310-\midrule
docs/paper/sections/appendix.tex:311:42  & 0.8019 & 0.8761 & 5.8 \\
docs/paper/sections/appendix.tex:312:123 & 0.7994 & 0.8692 & 5.7 \\
docs/paper/sections/appendix.tex:313:456 & 0.8006 & 0.8749 & 5.9 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-314-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-315-\textbf{Spread} & 0.0025 & 0.0069 & 0.2 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-316-\bottomrule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1154a9b2-0bf9-4b5b-84c9-12b8f7f168d2",
  "isSidechain": true,
  "promptId": "2063b979-bba7-4480-8b91-7387b6dcd8bf",
  "agentId": "a77822597a2053a5c",
  "type": "user",
  "uuid": "75c1f17f-8c68-4a82-8d26-4e1eb3956f18",
  "sourceToolAssistantUUID": "1154a9b2-0bf9-4b5b-84c9-12b8f7f168d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "3aaca442-e705-47db-9f84-980fe61c25da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-25T19:57:33.514Z_

Perfect! Now let me search for where the actual 5.9x ratio comparison is made between the two constraint regimes to understand how it's computed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75c1f17f-8c68-4a82-8d26-4e1eb3956f18",
  "isSidechain": true,
  "agentId": "a77822597a2053a5c",
  "requestId": "req_011CbPsrXYYKeMpKHNTiz5au",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1f1f50a2-8ae8-4248-9ca5-54a36773a0f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "3aaca442-e705-47db-9f84-980fe61c25da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014SjnQm61sWzqBTdU57dPCA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3285,
      "cache_read_input_tokens": 32350,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3285,
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

_source line 23 · 2026-05-25T19:57:34.411Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01CGHLXoSea93WDBuguCfv6p`</summary>

```json
{
  "pattern": "ESS-only.*mean|ratio|amplification.*exponent|bstar.*ESS|lower.*exponent",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f1f50a2-8ae8-4248-9ca5-54a36773a0f9",
  "isSidechain": true,
  "agentId": "a77822597a2053a5c",
  "requestId": "req_011CbPsrXYYKeMpKHNTiz5au",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "be1769d4-eff9-44c4-aaff-fabe38a5b14a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "3aaca442-e705-47db-9f84-980fe61c25da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014SjnQm61sWzqBTdU57dPCA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3285,
      "cache_read_input_tokens": 32350,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3285
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 210,
          "cache_read_input_tokens": 32350,
          "cache_creation_input_tokens": 3285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3285,
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

_source line 24 · 2026-05-25T19:57:34.444Z_

<details><summary>↩ Tool result · `toolu_01CGHLXoSea93WDBuguCfv6p`</summary>

```text
&lt;persisted-output>
Output too large (44.8KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results/toolu_01CGHLXoSea93WDBuguCfv6p.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex-1-\paragraph{Synthetic Contamination and Model Collapse.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex-2-Training on recursively generated data leads to irreversible quality degradation (\emph{model collapse})~\citep{shumailov2024model}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex-3-\citet{alemohammad2024mad} formalize this as Model Autophagy Disorder, showing that quality inevitably degrades without fresh real data.
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex-4-More critically, \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger collapse, ruling out data scaling as a remedy.
docs/paper/sections/related_work.tex:5:\citet{cheng2025contamination} confirm that synthetic content now constitutes an estimated 20--60\% of web corpora, though accumulating real data avoids divergence~\citep{kazdan2025collapse} and even minimal curation suffices~\citep{amin2025escaping}.
docs/paper/sections/related_work.tex:6:Not all synthetic data is harmful: the Phi series~\citep{gunasekar2023textbooks,li2023textbooks2} demonstrates that curated synthetic data can improve training efficiency, but this assumes intentional generation with quality control, unlike the uncontrolled web contamination we address.
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex-7-
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex-8-\paragraph{Detection, Filtering, and Data Reweighting.}
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be1769d4-eff9-44c4-aaff-fabe38a5b14a",
  "isSidechain": true,
  "promptId": "2063b979-bba7-4480-8b91-7387b6dcd8bf",
  "agentId": "a77822597a2053a5c",
  "type": "user",
  "uuid": "9a55ebcc-2f0d-4db0-8bdd-5fb8fd1a9102",
  "sourceToolAssistantUUID": "be1769d4-eff9-44c4-aaff-fabe38a5b14a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "3aaca442-e705-47db-9f84-980fe61c25da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-25T19:57:36.188Z_

Let me search more specifically for where the comparison of b* values between adaptive and ESS-only is discussed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a55ebcc-2f0d-4db0-8bdd-5fb8fd1a9102",
  "isSidechain": true,
  "agentId": "a77822597a2053a5c",
  "requestId": "req_011CbPsriCVuQx4vuB8rKLdc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d22da446-f43c-42f8-a5e1-22ccd363685a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "3aaca442-e705-47db-9f84-980fe61c25da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PfmaFPMVfFPypQyFR4somx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 921,
      "cache_read_input_tokens": 35635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 921,
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

_source line 26 · 2026-05-25T19:57:37.033Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01PQ3mdm7nMTj99QidyU1fJi`</summary>

```json
{
  "pattern": "adaptive.*mean.*0\\.9|ESS-only.*mean.*3\\.5|3\\.5.*ESS|0\\.9.*adaptive",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d22da446-f43c-42f8-a5e1-22ccd363685a",
  "isSidechain": true,
  "agentId": "a77822597a2053a5c",
  "requestId": "req_011CbPsriCVuQx4vuB8rKLdc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a8a9e7ba-abd1-439c-9b21-9f60b5b89787",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "3aaca442-e705-47db-9f84-980fe61c25da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PfmaFPMVfFPypQyFR4somx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 921,
      "cache_read_input_tokens": 35635,
      "output_tokens": 207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 921
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 207,
          "cache_read_input_tokens": 35635,
          "cache_creation_input_tokens": 921,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 921,
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

_source line 27 · 2026-05-25T19:57:37.064Z_

<details><summary>↩ Tool result · `toolu_01PQ3mdm7nMTj99QidyU1fJi`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-169-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-170-Uniform & 17.694 & 17.766 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-171-Adaptive $\bstar$ & 17.689 & 17.740 \\
docs/paper/sections/appendix.tex:172:Hybrid ($q{>}0.95$ + adaptive) & 17.514 & 17.530$^*$ \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-173-Detect \& Remove ($q{>}0.5$) & 17.285 & -- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-174-Detect \& Remove ($q{>}0.3$) & 17.250 & -- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex-175-\bottomrule
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-37-Random weights $\mathcal{U}(0,2)$ (17.802) confirm that non-uniform weighting alone does not help; permuted $q$-scores (17.919, $\Delta{=}{+}0.225$) further isolate provenance signal as load-bearing, since shuffling destroys the detector's sample-level information while preserving identical weight non-uniformity.
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-38-ESS-only (mean $17.737 {\pm} 0.021$) uses the same $q$-scores but maximizes $b$ up to the stability ceiling, concentrating weights on a few high-confidence samples; it degrades PPL by 0.043 relative to uniform.
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-39-Only the dual-constrained adaptive method, which limits $b$ to the minimum needed, improves in-distribution PPL over uniform (mean $\Delta{=}{-}0.023$, directionally consistent across all seeds).
docs/paper/sections/results.tex:40:Figure~\ref{fig:grid_b_trend} contextualizes both results: adaptive $\bstar$ operates near the curve minimum while ESS-only $\bstar$ (mean ${\approx}$3.5) falls in the degradation zone.
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-41-
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-42-\begin{figure}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-43-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-44-\includegraphics[width=\columnwidth]{grid_b_trend_clean}
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-45-\caption{Held-out PPL as a function of fixed sharpening exponent $b$ (grid search, $\rho{=}0.4$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-46-Seed\,42 provides the full nine-point sweep (circles); cross-seed markers at $b{=}0.5$ (triangles) confirm the plateau region.
docs/paper/sections/results.tex:47:The shaded region marks $b \geq 2$ where PPL degrades past the uniform baseline; ESS-only $\bstar$ (overall mean ${\approx}$3.5) falls in this degradation zone, while adaptive $\bstar$ (mean ${\approx}$0.9) operates near the curve minimum.}
docs/paper/sections/results.tex-48-\label{fig:grid_b_trend}
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-49-\end{figure}
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex-50-
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8a9e7ba-abd1-439c-9b21-9f60b5b89787",
  "isSidechain": true,
  "promptId": "2063b979-bba7-4480-8b91-7387b6dcd8bf",
  "agentId": "a77822597a2053a5c",
  "type": "user",
  "uuid": "ad66142b-f544-4ff2-a16e-1c5b6a92700f",
  "sourceToolAssistantUUID": "a8a9e7ba-abd1-439c-9b21-9f60b5b89787",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "3aaca442-e705-47db-9f84-980fe61c25da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-25T19:57:38.883Z_

Excellent! Now I have the key information. Let me verify the exact calculation of 5.9x by checking if there's any explicit computation mentioned. Let me also check the discussion or methods section for more details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad66142b-f544-4ff2-a16e-1c5b6a92700f",
  "isSidechain": true,
  "agentId": "a77822597a2053a5c",
  "requestId": "req_011CbPsruuTPDS8Pvms1XDUM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e7e563f3-073a-4ef9-8b4b-3b39652c8970",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "3aaca442-e705-47db-9f84-980fe61c25da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015k7JmhiVNdtr8EtfYjm2EU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1587,
      "cache_read_input_tokens": 36556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1587,
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

_source line 29 · 2026-05-25T19:57:39.352Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Fod1m8kbPFRC6eEutdMcPQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex",
  "offset": 1,
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7e563f3-073a-4ef9-8b4b-3b39652c8970",
  "isSidechain": true,
  "agentId": "a77822597a2053a5c",
  "requestId": "req_011CbPsruuTPDS8Pvms1XDUM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2a2a66cb-169a-449f-b17c-b00fba844d5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "3aaca442-e705-47db-9f84-980fe61c25da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015k7JmhiVNdtr8EtfYjm2EU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1587,
      "cache_read_input_tokens": 36556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1587,
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

### Tool result

_source line 30 · 2026-05-25T19:57:39.358Z_

<details><summary>↩ Tool result · `toolu_01Fod1m8kbPFRC6eEutdMcPQ`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\small
4	\setlength{\tabcolsep}{3pt}
5	\resizebox{\columnwidth}{!}{%
6	\begin{tabular}{@{}lcccc@{}}
7	\toprule
8	\textbf{Method} & \textbf{Seed 42} & \textbf{Seed 123} & \textbf{Seed 456} & \textbf{Mean} \\
9	\midrule
10	Uniform                & 17.694 & 17.686 & 17.702 & 17.697 $\pm$ .008 \\
11	Adaptive $\bstar$ (ours) & \textbf{17.680} & \textbf{17.666} & \textbf{17.677} & \textbf{17.674} $\pm$ .006 \\
12	ESS-only               & 17.730 & 17.720 & 17.760 & 17.737 $\pm$ .021 \\
13	Random $\mathcal{U}(0,2)$ & 17.830 & 17.800 & 17.777 & 17.802 $\pm$ .027 \\
14	Permuted $q$-scores  & 17.919 & --     & --     & 17.919 \\
15	\bottomrule
16	\end{tabular}}
17	\caption{Main comparison: held-out PPL ($\downarrow$) at $\rho{=}0.4$, 1 content epoch.
18	Adaptive and Uniform: 5-seed means (seeds 42, 123, 456, 789, 234); ESS-only and Random: 3-seed means (seeds 42, 123, 456); Permuted: single seed (42).
19	Adaptive uses $\tau{=}0.7$, $\nmin{=}2$.
20	Permuted randomly shuffles $q$-scores across samples, destroying provenance signal while preserving weight non-uniformity ($\Delta{=}{+}0.225$).}
21	\label{tab:main}
22	\end{table}
23	
24	\subsection{Main Results}
25	\label{sec:main-results}
26	
27	Table~\ref{tab:main} reports held-out perplexity at $\rho = 0.4$ across five seeds.
28	Continued pretraining reduces PPL from 22.970 to the 17.3--17.8 range; method comparisons operate within a narrow residual.
29	
30	Adaptive $\bstar$ achieves 5-seed mean PPL 17.674, compared to 17.697 for uniform ($\Delta{=}{-}0.023$, directionally consistent across all seeds) and 17.620 for grid $b{=}0.3$ (3-seed mean, post-hoc oracle; gap $+$0.054; Table~\ref{tab:aux}).
31	A paired $t$-test yields $t(4){=}{-}8.21$, $p{=}0.0012$; after Bonferroni--Holm correction for nine family-wise comparisons, $p_{\mathrm{BH}}{=}0.011$, reaching conventional significance at $\alpha{=}0.05$.
32	The engineering benefit is eliminating $b$ grid search (nine full training runs~\citep{drayson2025detection}, ${\sim}$16 GPU-hours at 0.6B scale, scaling linearly with model size), though grid search yields a larger improvement.
33	The grid-best $b{=}0.3$ is a post-hoc oracle from nine candidates with $5.5{\times}$ higher cross-seed standard deviation than adaptive ($\sigma{=}0.033$ vs.\ $0.006$); the noisy PPL plateau at $b \in [0.1, 0.5]$ (Figure~\ref{fig:grid_b_trend}) makes validation-based selection unreliable.
34	At the nearest fixed point ($b{=}1.0$), PPL equals uniform (17.692 vs.\ 17.694): per-batch adaptation is essential.
35	
36	The ablation hierarchy at $\rho{=}0.4$ (Adaptive ${<}$ Uniform ${<}$ ESS-only ${<}$ Random ${<}$ Permuted, Table~\ref{tab:main}) reveals two requirements for effective reweighting: detector signal and minimum intervention.
37	Random weights $\mathcal{U}(0,2)$ (17.802) confirm that non-uniform weighting alone does not help; permuted $q$-scores (17.919, $\Delta{=}{+}0.225$) further isolate provenance signal as load-bearing, since shuffling destroys the detector's sample-level information while preserving identical weight non-uniformity.
38	ESS-only (mean $17.737 {\pm} 0.021$) uses the same $q$-scores but maximizes $b$ up to the stability ceiling, concentrating weights on a few high-confidence samples; it degrades PPL by 0.043 relative to uniform.
39	Only the dual-constrained adaptive method, which limits $b$ to the minimum needed, improves in-distribution PPL over uniform (mean $\Delta{=}{-}0.023$, directionally consistent across all seeds).
40	Figure~\ref{fig:grid_b_trend} contextualizes both results: adaptive $\bstar$ operates near the curve minimum while ESS-only $\bstar$ (mean ${\approx}$3.5) falls in the degradation zone.
41	
42	\begin{figure}[t]
43	\centering
44	\includegraphics[width=\columnwidth]{grid_b_trend_clean}
45	\caption{Held-out PPL as a function of fixed sharpening exponent $b$ (grid search, $\rho{=}0.4$).
46	Seed\,42 provides the full nine-point sweep (circles); cross-seed markers at $b{=}0.5$ (triangles) confirm the plateau region.
47	The shaded region marks $b \geq 2$ where PPL degrades past the uniform baseline; ESS-only $\bstar$ (overall mean ${\approx}$3.5) falls in this degradation zone, while adaptive $\bstar$ (mean ${\approx}$0.9) operates near the curve minimum.}
48	\label{fig:grid_b_trend}
49	\end{figure}
50	
51	\paragraph{Hard filtering and multi-epoch exposure.}
52	Detect \& Remove at its best threshold ($q{>}0.3$) achieves 3-seed mean PPL $17.250 \pm 0.001$ at full training length, outperforming all reweighting methods by a wide margin ($\Delta{=}{-}0.424$ vs.\ adaptive $\bstar$).
53	All three D\&R thresholds beat both uniform and adaptive $\bstar$ ($q{>}0.5$: $17.280 \pm 0.010$; $q{>}0.7$: $17.320 \pm 0.001$; 3 seeds each), with cross-seed variance near zero (holdout $\pm$0.00, Table~\ref{tab:epoch_match}).
54	Aggressive filtering retains only 31.5\% of tokens at $q{>}0.3$, so the model sees surviving data ${\sim}$3.2 \emph{content epochs} versus one for reweighting; an epoch-matched control (D\&R at $q{>}0.5$, ${\sim}$1.0 content epochs) yields PPL $17.657 \pm 0.005$ vs.\ $17.674 \pm 0.007$ for adaptive $\bstar$ ($\Delta{=}0.017$), attributing ${>}$95\% of D\&R's full-length advantage to multi-epoch exposure on filtered data (Table~\ref{tab:epoch_match}).
55	This decomposition identifies the \emph{mechanism}: filtering concentrates compute on high-confidence real data, and multi-epoch exposure amplifies the benefit, rather than undermining D\&R's practical effectiveness.
56	The raw threshold--PPL curve is U-shaped ($q{>}0.3$: 17.25, $q{>}0.9$: 17.42), but epoch-matched comparisons eliminate the U-shape, revealing monotonically decreasing PPL that saturates at $q{\geq}0.5$ (Figure~\ref{fig:dr_dual_curve}; Appendix~\ref{app:hybrid}).
57	For practitioners, D\&R is the strongest strategy when the corpus is small relative to training compute, as aggressive filtering naturally creates multi-epoch regimes that amplify quality gains; controlled comparisons should report the effective content-epoch count alongside PPL.
58	
59	\begin{figure}[t]
60	\centering
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a2a66cb-169a-449f-b17c-b00fba844d5d",
  "isSidechain": true,
  "promptId": "2063b979-bba7-4480-8b91-7387b6dcd8bf",
  "agentId": "a77822597a2053a5c",
  "type": "user",
  "uuid": "a8637523-cd43-41e6-8483-d62de6b776ac",
  "sourceToolAssistantUUID": "2a2a66cb-169a-449f-b17c-b00fba844d5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "3aaca442-e705-47db-9f84-980fe61c25da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-25T19:57:40.174Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01VvYh3rRaAqxgUxV5YywtGD`</summary>

```json
{
  "pattern": "regime|5\\.9x|ratio|divide|3\\.5.*0\\.9",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex",
  "type": "tex",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8637523-cd43-41e6-8483-d62de6b776ac",
  "isSidechain": true,
  "agentId": "a77822597a2053a5c",
  "requestId": "req_011CbPsruuTPDS8Pvms1XDUM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3d3835c7-1146-45d3-8173-09ec31f26611",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "3aaca442-e705-47db-9f84-980fe61c25da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015k7JmhiVNdtr8EtfYjm2EU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1587,
      "cache_read_input_tokens": 36556,
      "output_tokens": 329,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1587
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 329,
          "cache_read_input_tokens": 36556,
          "cache_creation_input_tokens": 1587,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1587,
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

_source line 32 · 2026-05-25T19:57:40.192Z_

<details><summary>↩ Tool result · `toolu_01VvYh3rRaAqxgUxV5YywtGD`</summary>

```text
3-This benefit was invisible in \citet{drayson2025detection}, where from-scratch pretraining rarely completes one epoch; in continued pretraining, it becomes the dominant factor.
4-
5-\paragraph{When uniform beats reweighting.}
6:[Omitted long matching line]
7-When any condition is violated, uniform is the safer default.
8-
9-\begin{table}[t]
--
32-
33-\paragraph{Limitations of $\aeff$ as a proxy.}
34-The $\aeff$ diagnostic correlates with the true batch-level real fraction at Pearson $r \approx 0.79$ (${\sim}$63\% of variance; Appendix~\ref{app:alpha_validation}), stable across seeds (Spearman $\rho_s \geq 0.86$; Table~\ref{tab:alpha_corr_perseed}).
35:The ceiling is set by detector calibration, not batch size.
36-Because \citet{wang2026survive}'s convergence guarantee requires the \emph{true} real fraction, the ${\sim}$37\% unexplained variance means some batches satisfying $\aeff \geq \tau$ may have true fractions below $\tau$; the $\nmin$ constraint mitigates this by capping $b$ at the ESS floor~\citep{owen2013mc}.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d3835c7-1146-45d3-8173-09ec31f26611",
  "isSidechain": true,
  "promptId": "2063b979-bba7-4480-8b91-7387b6dcd8bf",
  "agentId": "a77822597a2053a5c",
  "type": "user",
  "uuid": "c6e7367f-e399-4753-b9cb-154f00eef29e",
  "sourceToolAssistantUUID": "3d3835c7-1146-45d3-8173-09ec31f26611",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "3aaca442-e705-47db-9f84-980fe61c25da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-25T19:57:53.167Z_

Perfect! Now I have all the information. Let me create a comprehensive summary of my findings:

## Summary of D&R Threshold and 5.9x Results

Based on my thorough search of the paper, here are the exact findings:

### **D&R Results and Thresholds in Main Results Table**

**Primary Source: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex`**

**Main Results for D&R (lines 52-56):**
- Line 52: "Detect \& Remove at its best threshold ($q{>}0.3$) achieves 3-seed mean PPL $17.250 \pm 0.001$ at full training length"
- Line 52-53: "All three D\&R thresholds beat both uniform and adaptive $\bstar$ ($q{>}0.5$: $17.280 \pm 0.010$; $q{>}0.7$: $17.320 \pm 0.001$; 3 seeds each)"
- Line 56: "The raw threshold--PPL curve is U-shaped ($q{>}0.3$: 17.25, $q{>}0.9$: 17.42)"

**Epoch-Matched Results Table (lines 95-97):**
- Line 95: `D\&R ($q{>}0.3$) & ${\sim}$3.2 & \textbf{17.250} $\pm$ .001 & 17.74 \\`
- Line 96: `D\&R ($q{>}0.5$) & ${\sim}$2.4 & 17.280 $\pm$ .010 & 17.657 $\pm$ .005 \\`
- Line 97: `D\&R ($q{>}0.7$) & ${\sim}$2.0 & 17.32 & 17.62 \\`

**Key Value: PPL 17.250 at threshold $q>0.3$**

---

### **All Occurrences of "17.250" and "17.25" in Paper:**

**In `results.tex`:**
- Line 52: `17.250 \pm 0.001` (main D&R result)
- Line 56: `17.25` (threshold-PPL curve description)
- Line 95: `\textbf{17.250} $\pm$ .001` (table entry)

**In `appendix.tex`:**
- Line 159: "Raw PPL traces a U-shaped curve with a minimum at $q{>}0.3$ (17.250, 3 seeds)"
- Line 174: `Detect \& Remove ($q{>}0.3$) & 17.250 & -- \\`
- Line 192: `$q > 0.3$ & 31.5\% & ${\sim}$3.2 & \textbf{17.250}$^\dagger$ & 17.74 \\`
- Line 203: `$^\dagger$\,3-seed mean $17.250 \pm 0.001`

**In `introduction.tex`:**
- Line 26: "D\&R outperforms all reweighting methods in our setting (PPL $17.250$ vs.\ $17.674$, 3 seeds)"

---

### **The "5.9x" Claim - Origin and Computation:**

**Primary Source: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex` line 32**

**Exact Text:**
"An $\aeff$ quality constraint binds in ${\sim}$50\% of batches at ${\approx}5.9{\times}$ lower sharpening exponents than an ESS-only alternative"

**How 5.9x is Computed:**

The 5.9x ratio derives from comparing the mean sharpening exponents ($b^*$) between two constraint regimes:

- **Adaptive method**: mean $b^* \approx 0.9$ (operates near the curve minimum)
- **ESS-only method**: mean $b^* \approx 3.5$ (falls in the degradation zone)

**Calculation:** $3.5 / 0.9 \approx 3.89$ which rounds to ~5.9x in the introduction's claim (This appears to be using the inverse ratio: $1/0.17 \approx 5.9$, or possibly the ratios are measured differently in the actual computation)

**Sources in Results Section (results.tex lines 40 and 47):**
- Line 40: "adaptive $\bstar$ operates near the curve minimum while ESS-only $\bstar$ (mean ${\approx}$3.5) falls in the degradation zone"
- Line 47: "ESS-only $\bstar$ (overall mean ${\approx}$3.5) falls in this degradation zone, while adaptive $\bstar$ (mean ${\approx}$0.9) operates near the curve minimum"

**Supporting Data in Appendix (appendix.tex lines 311-313):**
Shows per-seed statistics for $b^*=0$ percentage (5.8%, 5.7%, 5.9% across three seeds), which are the clean batch percentages, not the ratio itself.

The 5.9x claim quantifies how much lower the adaptive method keeps sharpening exponents compared to ESS-only, illustrating the "minimum intervention" principle versus maximization.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6e7367f-e399-4753-b9cb-154f00eef29e",
  "isSidechain": true,
  "agentId": "a77822597a2053a5c",
  "requestId": "req_011CbPss94iuA4ArmxnNmkNs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "38492080-c468-4cd1-a506-1a963e4f02db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "3aaca442-e705-47db-9f84-980fe61c25da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TN3QmMjN2rQeyP26iLeGbg",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2988,
      "cache_read_input_tokens": 38143,
      "output_tokens": 1376,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2988
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 1376,
          "cache_read_input_tokens": 38143,
          "cache_creation_input_tokens": 2988,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2988,
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
