# Research conversation: Read the following files in the project at /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a6b9c6ef519ef00f3.jsonl`
- **Structured JSON:** [`561f27c2d78137ae73d3.json`](../../sessions/56/561f27c2d78137ae73d3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

22 recorded events

### User

_source line 1 · 2026-05-19T13:54:41.866Z_

Read the following files in the project at /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/:

1. Find all .tex files in docs/paper/sections/ directory
2. Read experiments.tex fully - I need to see Table 1 (SciERC AUROC columns), Table 3 (degeneracy rates, selection Δ)
3. Read appendix.tex fully - I need the cross-selection table with LP F1 and Δ values

Report the exact numbers found in these tables. Be thorough - capture all numeric values in Table 1 AUROC column for SciERC, Table 3 degeneracy and Δ values, and appendix cross-selection table values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "agentId": "a6b9c6ef519ef00f3",
  "type": "user",
  "uuid": "d329c75b-3b5c-499e-97d6-85b04b129140",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-19T13:54:43.402Z_

I'll help you find and read those files. Let me start by exploring the directory structure and locating the .tex files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d329c75b-3b5c-499e-97d6-85b04b129140",
  "isSidechain": true,
  "agentId": "a6b9c6ef519ef00f3",
  "requestId": "req_011CbC3LGbuWCkEcLx5gaewa",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cb096ff7-dc3b-40f2-a8d3-8e0b9ecc6a0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019HeMtooLNwcM9EkBMsnFER",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20325,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20325,
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

_source line 3 · 2026-05-19T13:54:43.595Z_

<details open><summary>🔧 Tool call — Glob · `toolu_011rN8tbpqWMYEevB7xk7m6E`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb096ff7-dc3b-40f2-a8d3-8e0b9ecc6a0f",
  "isSidechain": true,
  "agentId": "a6b9c6ef519ef00f3",
  "requestId": "req_011CbC3LGbuWCkEcLx5gaewa",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "728ac71e-8a4f-4440-ac65-d080b125703d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019HeMtooLNwcM9EkBMsnFER",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20325,
      "cache_read_input_tokens": 0,
      "output_tokens": 115,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 20325
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 115,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 20325,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 20325,
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

_source line 4 · 2026-05-19T13:54:43.615Z_

<details><summary>↩ Tool result · `toolu_011rN8tbpqWMYEevB7xk7m6E`</summary>

```text
docs/paper/sections/checklist.tex
docs/paper/sections/method.tex
docs/paper/sections/related_work.tex
docs/paper/sections/introduction.tex
docs/paper/sections/abstract.tex
docs/paper/sections/limitations.tex
docs/paper/sections/discussion.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/experiments.tex
docs/paper/sections/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "728ac71e-8a4f-4440-ac65-d080b125703d",
  "isSidechain": true,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "agentId": "a6b9c6ef519ef00f3",
  "type": "user",
  "uuid": "a0e5dfeb-dce4-4e15-911b-1c94be15d2af",
  "sourceToolAssistantUUID": "728ac71e-8a4f-4440-ac65-d080b125703d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-19T13:54:45.103Z_

Great! I found the files. Now let me read the experiments.tex and appendix.tex files to extract the tables you need.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0e5dfeb-dce4-4e15-911b-1c94be15d2af",
  "isSidechain": true,
  "agentId": "a6b9c6ef519ef00f3",
  "requestId": "req_011CbC3LQ9ajE8wcsWeF468t",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4f38d871-b7a5-4d36-b0f7-d7047ca9a916",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ELGxaV8is6mZD3EMqK999x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1065,
      "cache_read_input_tokens": 20325,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1065,
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

_source line 6 · 2026-05-19T13:54:46.085Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UZiY2ZUL1zrZZ6TcxeYt7o`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f38d871-b7a5-4d36-b0f7-d7047ca9a916",
  "isSidechain": true,
  "agentId": "a6b9c6ef519ef00f3",
  "requestId": "req_011CbC3LQ9ajE8wcsWeF468t",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d171c286-eff4-4065-8fcc-52d471d38650",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ELGxaV8is6mZD3EMqK999x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1065,
      "cache_read_input_tokens": 20325,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1065
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 195,
          "cache_read_input_tokens": 20325,
          "cache_creation_input_tokens": 1065,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1065,
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

_source line 7 · 2026-05-19T13:54:46.101Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JwaHhUcroAJ26Mjy5Piq7J`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d171c286-eff4-4065-8fcc-52d471d38650",
  "isSidechain": true,
  "agentId": "a6b9c6ef519ef00f3",
  "requestId": "req_011CbC3LQ9ajE8wcsWeF468t",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "92325ce4-c5aa-429f-8d1c-521d166cce09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ELGxaV8is6mZD3EMqK999x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1065,
      "cache_read_input_tokens": 20325,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1065
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 195,
          "cache_read_input_tokens": 20325,
          "cache_creation_input_tokens": 1065,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1065,
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

_source line 8 · 2026-05-19T13:54:46.140Z_

<details><summary>↩ Tool result · `toolu_01UZiY2ZUL1zrZZ6TcxeYt7o`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.
9	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\approx}$65\% F1.
10	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:fewnerd}).
11	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
12	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 51\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
13	
14	\paragraph{Models and sampling.}
15	\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (training details in Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others due to earlier convergence; Appendix~\ref{app:epoch_confound}).
16	We draw $N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}, with $N{=}16$ for scaling experiments (Appendix~\ref{app:n_scaling}).
17	
18	%% ============================================================
19	\subsection{Quality Estimation Results}
20	\label{sec:qe_results}
21	
22	\begin{table*}[t]
23	\centering
24	\small
25	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\sigma{\leq}0.026$ in Table~\ref{tab:multiseed}). Best in \textbf{bold}. RE results in Appendix~\ref{app:re_extension}. $N{=}16$ in Table~\ref{tab:robustness}.}
26	\label{tab:quality_estimation}
27	\begin{tabular}{ll cc cc cc}
28	\toprule
29	& & \multicolumn{2}{c}{\textbf{SciERC}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
30	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8}
31	Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
32	\midrule
33	VC & Structural & \textbf{.379} & \textbf{.663} & .424 & .789 & .426 & .709 \\
34	SJ  & Structural & .360 & .650 & .436 & .801 & \textbf{.431} & .704 \\
35	FK & Surface & .267 & .602 & .400 & .774 & .428 & .703 \\
36	EM  & Surface    & .295 & .614 & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
37	\midrule
38	LP     & Model      & .205 & .578 & .316 & .753 & .307 & \textbf{.761} \\
39	\bottomrule
40	\end{tabular}
41	\end{table*}
42	
43	Table~\ref{tab:quality_estimation} presents $\rho$ and AUROC for five signals across tasks and models ($\varepsilon$-free; $\varepsilon{=}0.05$ applies to selection only, stable across $[0, 0.2]$, Appendix~\ref{app:epsilon_robustness}).
44	
45	\paragraph{Signal rankings are difficulty-dependent.}
46	On SciERC (medium difficulty), structural signals lead (VC $\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\Delta\rho{=}{+}0.155$; Appendix~\ref{app:bootstrap_signal}).
47	On CoNLL (single-sample F1${\approx}$0.91), EM leads both $\rho$ and AUROC ($0.816$).
48	At the signal-collapse boundary (WNUT-17, macro F1${\approx}$42\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\rho{=}0.724$ but conditional $\rho{=}0.038$; Table~\ref{tab:wnut}); LP shows the reverse (conditional $\rho{=}0.350$; Figure~\ref{fig:signal_heatmap}).
49	This collapse illustrates a regime where model capability is insufficient to produce meaningful inter-sample variation: 51\% of instances yield zero F1 across all samples, and consistency signals merely detect this floor rather than discriminating quality among non-trivial outputs.
50	
51	%% ============================================================
52	\subsection{The Correlation-Selection Gap}
53	\label{sec:selection_gap}
54	
55	Four of five signals (SJ, FK, EM, VC) assign identical scores to all candidates from the same input by construction (\S\ref{sec:formulation}); they can estimate quality across instances but cannot rank candidates within an instance.
56	The empirical question is whether LP, the sole per-sample signal, can exploit its candidate-discriminative nature for selection.
57	LP selection effectiveness is primarily determined by LP-quality alignment rather than degeneracy level (\S\ref{sec:discussion}).
58	Cross-instance $\rho$ (Table~\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.
59	
60	\begin{table}[t]
61	\centering
62	\small
63	\caption{Best-of-$N$ NER selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\pm}\sigma$). LP is per-sample; others use consensus-proximity. Best non-oracle in \textbf{bold}. Non-tied subset in \S\ref{sec:discussion}; RE in Appendix~\ref{app:re_extension}. $^\dagger$Instance-level signals assign one score per input; per-sample ranking $p$-values are undefined.}
64	\label{tab:selection}
65	\begin{tabular}{lcc}
66	\toprule
67	Method & NER F1 & $p$ \\
68	\midrule
69	Oracle & $0.775 \pm 0.001$ & --- \\
70	Greedy ($T{=}0$) & $0.645 \pm 0.001$ & --- \\
71	\midrule
72	\multicolumn{3}{l}{\textit{Per-sample signal}} \\
73	LP           & $\mathbf{0.647} \pm 0.005$ & .29 \\
74	\midrule
75	\multicolumn{3}{l}{\textit{Instance-level signals (consensus-proximity selection)}} \\
76	SJ           & $0.646 \pm 0.002$ & .67 \\
77	FK           & $0.646 \pm 0.001$ & .79 \\
78	EM           & $0.637 \pm 0.001$ & n/a$^\dagger$ \\
79	VC           & $0.623 \pm 0.004$ & n/a$^\dagger$ \\
80	\midrule
81	Random           & $0.610 \pm 0.003$ & --- \\
82	\bottomrule
83	\end{tabular}
84	\end{table}
85	
86	\begin{figure}[t]
87	\centering
88	\includegraphics[width=\columnwidth]{fig_selection_gap}
89	\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Bars: quality estimation $\rho$ (seed 42); line with error bars: $\Delta$F1 vs.\ greedy (3-seed mean, seeds 42/123/456). Despite $\rho$ up to 0.38, no signal significantly outperforms greedy (all $p{>}0.05$; Table~\ref{tab:selection}). Dashed green: oracle upper bound ($+13.1$~pp); dotted gray: random baseline.}
90	\label{fig:selection_gap}
91	\end{figure}
92	
93	Instance-level signals assign identical QE scores to all candidates; MBR conversion does not improve over greedy on the primary test bed (Table~\ref{tab:selection}; Figure~\ref{fig:selection_gap}).
94	Instance-level signals predict \textit{which inputs} the model handles reliably, not \textit{which output} is best.
95	
96	\paragraph{LP: the sole per-sample signal also fails.}
97	On SciERC ($n{=}529$, 2-seed sign tests\footnote{MDE${\approx}$1.5~pp at 80\% power ($n{=}529$); Few-NERD ($n{=}32{,}565$; MDE${\approx}$0.22~pp) provides the definitive test.}), the oracle (0.775) reveals 13.0~pp of headroom, but LP achieves $+0.2$~pp ($p{=}0.29$), below the MDE (${\approx}$1.5~pp); selection effects below this threshold cannot be reliably detected.
98	The pattern holds across CoNLL and WNUT-17 (Table~\ref{tab:cross_selection}); under stringent TOST anchors, some configurations show significant \textit{degradation} (Appendix~\ref{app:tost}).
99	Few-NERD provides the definitive contrast: LP achieves $+1.39$~pp ($p{<}0.001$) at low degeneracy (\S\ref{sec:fewnerd}), while structural signals still degrade selection.
100	
101	\paragraph{Qualitative factors governing selection effectiveness.}
102	Three factors qualitatively shape LP selection gains: (1)~\textit{instance degeneracy} compresses the candidate space, leaving fewer instances where any signal can improve over greedy (SciERC 17.8\%, CoNLL 48.4\%; Table~\ref{tab:fewnerd}); (2)~\textit{oracle headroom} bounds the maximum achievable gain (CoNLL ${\approx}2$\,pp vs.\ SciERC 13.1\,pp); (3)~\textit{LP-quality alignment}, measured as within-instance $\rho(\text{LP}, \text{F1})$, determines whether LP can discriminate candidates in the remaining non-degenerate instances (Few-NERD $\rho{\approx}0.5$--$0.7$ vs.\ SciERC $\rho{\approx}0.26$).
103	These factors are consistent with the observed pattern (Table~\ref{tab:fewnerd}): Few-NERD (low degeneracy, strong alignment) shows the largest LP gain ($+1.39$\,pp), SciERC (weak alignment) shows unreliable gains ($+0.04{\pm}0.48$\,pp, 3-seed; Table~\ref{tab:multiseed}), CoNLL (high degeneracy, minimal headroom) shows no gain, and WNUT-17 represents the signal-collapse boundary: LP $\rho{=}{-}0.446$ (the model assigns higher log-probabilities to confidently wrong outputs), within-instance alignment absent ($\rho{=}0.043$, n.s.), and construction ineffective ($p{>}0.05$, mixed sign) because 51\% of instances yield F1${=}0$.
104	Yet QE remains effective on WNUT-17 (VC $\rho{=}0.724$; Table~\ref{tab:wnut}), confirming QE-selection decoupling at this boundary.
105	This characterization is qualitative: the three factors do not combine into a predictive model ($R^2{<}0$ across 23 configurations), but each factor's role is individually supported by controlled ablations (\S\ref{sec:fewnerd}, \S\ref{sec:discussion}).
106	
107	%% ============================================================
108	\subsection{Cross-Dataset Contrast: Few-NERD}
109	\label{sec:fewnerd}
110	
111	\begin{table}[t]
112	\centering
113	\small
114	\caption{LP selection across datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). Few-NERD/CoNLL: 3-seed means; SciERC: single-seed (3-seed in Table~\ref{tab:multiseed}). $p$: paired bootstrap.}
115	\label{tab:fewnerd}
116	\resizebox{\columnwidth}{!}{%
117	\begin{tabular}{@{}lrccccr@{}}
118	\toprule
119	Dataset & $n$ & Greedy & Degen.\% & LP $\rho$ & LP $\Delta$ & $p$ \\
120	\midrule
121	WNUT-17 & 1{,}287 & .452 & 67.9\% & $-$.446 & $-$0.45\,pp & .72 \\
122	CoNLL & 2{,}756 & .908 & 48.4\% & .302 & $-$0.85\,pp & 1.0 \\
123	SciERC & 529 & .644 & 17.8\% & .205 & $+$0.61\,pp & .193 \\
124	Few-NERD & 32{,}565 & .748 & 13.8\% & .220 & $\mathbf{+1.39}$\,pp & ${<}.001$ \\
125	\bottomrule
126	\end{tabular}}
127	\end{table}
128	
129	Few-NERD (Table~\ref{tab:fewnerd}) confirms LP selection at low degeneracy: $+1.39$~pp ($p{<}0.001$), while structural signals degrade selection (VC $-1.79$, SJ $-2.14$~pp). LP is 50$\times$ more seed-stable ($\sigma{=}0.04$ vs.\ SJ $2.02$~pp) and generalizes to LLaMA-3.1-8B (Table~\ref{tab:cross_selection}).
130	Training convergence modulates degeneracy: 5-epoch Few-NERD raises degeneracy to 31\% and halves LP gains (Appendix~\ref{app:epoch_confound}).
131	
132	\paragraph{Degeneracy alone does not predict LP selection direction.}
133	Across 23 configurations, degeneracy does not predict LP gain ($\rho{=}0.052$, $p{=}0.81$; Figure~\ref{fig:degeneracy_scatter}), though within fixed settings it causally modulates LP ($\rho{=}{-}0.881$; Appendix~\ref{app:per_type_lp}).
134	Cross-dataset prediction requires LP signal quality: Few-NERD ($\rho{\approx}0.5$--$0.7$) shows consistent gains, SciERC ($\rho{\approx}0.26$) does not (Appendix~\ref{app:conditional_decomp}).
135	
136	\begin{figure}[t]
137	\centering
138	\includegraphics[width=\columnwidth]{figures/fig_degeneracy_lp_scatter.pdf}
139	\caption{Instance degeneracy vs.\ LP selection gain across 23 configurations ($N{=}8$; $\rho{=}0.052$, $p{=}0.81$). Within Few-NERD per-entity-type analysis ($\rho{=}{-}0.881$; Appendix~\ref{app:per_type_lp}), degeneracy predicts LP gain when alignment is held constant.}
140	\label{fig:degeneracy_scatter}
141	\end{figure}
142	
143	Structural signals remain negative regardless of sample budget; $N$-scaling analyses are in Appendix~\ref{app:n_scaling}.
144	
145	%% ============================================================
146	\subsection{Robustness}
147	\label{sec:robustness_main}
148	
149	Consistency signals are robust across $T{\in}\{0.7, 1.0\}$ with sublinear $N$-scaling gains (Table~\ref{tab:robustness}); signal rankings are stable across seeds ($W{=}1.0$; Table~\ref{tab:ranking-stability}). NER calibration is reasonable (ECE 0.069--0.096; Appendix~\ref{app:calibration}).
150	
151	\begin{table}[t]
152	\centering
153	\small
154	\caption{Scale ablation: 8B vs.\ 4B QE $\rho$ ($N{=}8$, $T{=}1.0$, seed 42). RE in Appendix~\ref{app:re_extension}.}
155	\label{tab:scale_ablation}
156	\begin{tabular}{@{}ll cc r@{}}
157	\toprule
158	& & \textbf{8B} & \textbf{4B} & $\Delta$ \\
159	\midrule
160	CoNLL & SJ & .436 & .422 & $-$.014 \\
161	      & FK & .400 & .418 & $+$.018 \\
162	SciERC & SJ & .360 & .422 & $+$.062 \\
163	       & FK & .267 & .326 & $+$.059 \\
164	\bottomrule
165	\end{tabular}
166	\end{table}
167	
168	\paragraph{Scale robustness.}
169	With Qwen3-4B (Table~\ref{tab:scale_ablation}), QE is comparable (mean $|\Delta\rho|{=}0.042$), yet selection remains below greedy despite 13.0~pp headroom. Task difficulty is a stronger predictor than model scale within the 3B--8B range (Appendix~\ref{app:llama3b}).
170	Degeneracy scales with capability: 8B shows 17.8\% vs.\ 4B's 10.4\% on SciERC (Table~\ref{tab:degeneracy}).
171	
172	\paragraph{LoRA-rank ablation.}
173	LoRA rank${=}8$ (vs.\ 32) lowers degeneracy to 7.2\% but LP remains below greedy ($\rho(\text{LP}, \text{F1}){\approx}0.24$); temperature manipulation ($T{=}1.2$; \S\ref{sec:discussion}) confirms that low degeneracy and adequate alignment are independently necessary.
174	
175	\paragraph{Supervised signal combination and hidden probes.}
176	Supervised classifiers (LR, MLP, RF; 5-fold CV, $N{=}16$) and a DeBERTa-v3-base verifier all fail to close the selection gap (Appendix~\ref{app:supervised_combination}).
177	Hidden state probes improve correlation ($+37$\% on SciERC) but not selection (gap closure $-5.1$\%; Appendix~\ref{app:hidden_probe}); the bottleneck extends to model-internal representations.
178	
179	%% ============================================================
180	\subsection{Scaling Behavior}
181	\label{sec:scaling}
182	
183	We evaluate Qwen2.5-72B-Instruct in a zero-shot setting to test whether the gap persists at larger scale without fine-tuning.
184	
185	\begin{table}[t]
186	\centering
187	\small
188	\caption{Fine-tuned 8B vs.\ zero-shot 72B ($N{=}8$, $T{=}1.0$). Hdr.\ = oracle $-$ greedy (pp).}
189	\label{tab:scale_comparison}
190	\begin{tabular}{@{}llcccccc@{}}
191	\toprule
192	Dataset & Regime & Greedy & Hdr. & VC & SJ & FK & LP \\
193	\midrule
194	SciERC & 8B FT  & .645 & 13.0 & .379 & .360 & .267 & .205 \\
195	       & 72B ZS & .399 & 15.0 & .277 & .217 & .227 & .081 \\
196	\midrule
197	CoNLL  & 8B FT  & .908 & ${\approx}$2 & .424 & .436 & .400 & .302 \\
198	       & 72B ZS & .712 & 5.3  & .297 & .304 & .302 & $-$.002 \\
199	\bottomrule
200	\end{tabular}
201	\end{table}
202	
203	Zero-shot 72B produces lower greedy F1 but larger oracle headroom (Table~\ref{tab:scale_comparison}). LP $\rho$ drops from $0.205$ to $0.081$ on SciERC and from $0.302$ to near zero on CoNLL; LP selection fails in both datasets (SciERC $-0.1$~pp, CoNLL $-0.4$~pp), confirming that the gap is a structural property of the task rather than a fine-tuning artifact.
204	Structural signals remain positive but reduced (VC $\rho{=}0.277$ on SciERC, SJ $\rho{=}0.304$ on CoNLL). LP-weighted construction partially compensates on SciERC ($+1.5$\,pp, 41.4\% vs.\ 39.9\% greedy) but not on CoNLL ($-0.37$\,pp), where limited headroom (5.3~pp) leaves little room for aggregation.
205	
206	\textcolor{red}{TODO: (1) Add 72B fine-tuned results to determine whether fine-tuning at larger scale recovers signal quality. (2) Report degeneracy percentages for 72B zero-shot.}
207	
208	\begin{figure}[t]
209	\centering
210	% \includegraphics[width=\columnwidth]{figures/fig_scaling_curve.pdf}
211	\textcolor{red}{TODO: Scaling curve. X-axis: model scale (4B, 8B, 72B). Panels: (a) greedy/oracle F1 and headroom, (b) signal $\rho$. Separate lines for fine-tuned vs.\ zero-shot.}
212	\caption{\textcolor{red}{TODO: Signal quality and oracle headroom across model scales.}}
213	\label{fig:scaling_curve}
214	\end{figure}
215	
216	%% ============================================================
217	\subsection{Prescriptive Results}
218	\label{sec:prescriptive}
219	
220	The preceding sections establish that instance-level selection fails for structured IE. We now present two approaches that extract value from multi-sample generation without relying on sample ranking.
221	
222	\paragraph{Entity-level construction.}
223	Rather than selecting one of $N$ complete outputs, we aggregate entities across all samples, retaining those exceeding a confirmation threshold $\theta{=}2/N$ (${\geq}2$ of $N$ samples), with LP-weighted or uniform frequency scoring. Under fine-tuning, this default achieves the best or near-best F1 across all datasets ($\theta$ stable within $[0.15, 0.35]$; Appendix~\ref{app:theta_sweep}). In the zero-shot regime, uniform voting degrades (SciERC $-0.52$\,pp, CoNLL $-0.92$\,pp) because greater output diversity admits noise entities; LP-weighting is necessary for construction to succeed without fine-tuning (SciERC $+1.5$\,pp; \S\ref{sec:scaling}).
224	
225	\begin{table}[t]
226	\centering
227	\small
228	\caption{Entity construction vs.\ greedy ($\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\pm}\sigma$). $\theta{=}2/N$. $p$: paired bootstrap vs.\ greedy. Best in \textbf{bold}.}
229	\label{tab:entity_construction}
230	\resizebox{\columnwidth}{!}{%
231	\begin{tabular}{@{}llcccc@{}}
232	\toprule
233	Dataset & Wt. & Greedy & Constr. & $\Delta$ & $p$ \\
234	\midrule
235	SciERC & LP & $.646{\pm}.002$ & $\mathbf{.656{\pm}.003}$ & $+1.02{\pm}0.49$\,pp & .004 \\
236	       & Unif. & $.646{\pm}.002$ & $.653{\pm}.006$ & $+0.74{\pm}0.71$\,pp & .023 \\
237	\addlinespace
238	Few-NERD & LP & $.748$ & $\mathbf{.762{\pm}.005}$ & $+1.40{\pm}0.51$\,pp & ${<}.001$ \\
239	         & Unif. & $.748$ & $.756{\pm}.006$ & $+0.74{\pm}0.58$\,pp & .003 \\
240	\addlinespace
241	CoNLL & Unif. & .908 & .904 & $-0.39$\,pp & n.s. \\
242	\bottomrule
243	\end{tabular}}
244	\end{table}
245	
246	LP-weighted construction improves over greedy on Few-NERD ($+1.40{\pm}0.51$\,pp, $p{<}0.001$) and SciERC ($+1.02{\pm}0.49$\,pp, $p{=}0.004$; Table~\ref{tab:entity_construction}), positive across all 7 seed-dataset combinations, recovering ${\approx}$8\% (SciERC) and 11\% (Few-NERD) of oracle headroom. CoNLL shows no gain ($-0.39$\,pp), consistent with ceiling-regime degeneracy. The mechanism is recall-driven: aggregating low-frequency correct entities recovers mentions that no single sample captures ($N$-scaling in Appendix~\ref{app:n_scaling}).
247	
248	\paragraph{LP-alignment gating (preliminary diagnostic).}
249	Construction and LP selection are complementary: construction dominates on SciERC ($+1.02$\,pp vs.\ LP $+0.04{\pm}0.48$\,pp, n.s.; $\rho{\approx}0.2$), while on Few-NERD both yield comparable gains ($+1.40$ vs.\ $+1.39$\,pp; $\rho{\approx}0.5$--$0.7$).
250	We estimate within-instance $\rho(\text{LP}, \text{F1})$ on 50 held-out instances with bootstrap CIs (1000 resamples). Degeneracy-adjusted $\rho_{\text{adj}}$: Few-NERD $0.516$ [0.459, 0.759], SciERC $0.167$ [0.146, 0.281], CoNLL $0.065$ [$-$0.061, 0.620], WNUT-17 ${\approx}0$ (n.s.).
251	The protocol performs three-way routing: (1)~$\rho_{\text{adj}} \geq \tau{=}0.3$: apply LP selection; (2)~$\rho_{\text{adj}} < \tau$ and construction shows positive dev-set gain: apply construction; (3)~otherwise: retain greedy decoding.
252	This routes Few-NERD to LP selection ($+1.39$\,pp); SciERC, CoNLL, and WNUT-17 fall below $\tau$ and route to greedy. The conservative protocol trades SciERC's missed construction gain ($+1.02$\,pp) for protection against negative outcomes (CoNLL $-0.39$\,pp, WNUT-17 n.s.).
253	Routing is stable across $\tau{\in}[0.2, 0.4]$ and matches test-set direction for all four datasets; narrower inter-dataset margins remain untested.
254	
255	\paragraph{Selective prediction.}
256	Orthogonal to construction, QE signals support selective prediction: at 80\% coverage, filtering low-confidence instances yields $+5$--$8$\,pp F1 (AUPRC 0.70--0.92; Table~\ref{tab:cross_selection}).
257	
258	\phantomsection\label{sec:selection_results}
259	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d171c286-eff4-4065-8fcc-52d471d38650",
  "isSidechain": true,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "agentId": "a6b9c6ef519ef00f3",
  "type": "user",
  "uuid": "fa3acb3b-6f44-451e-b2bf-8b3402e049c9",
  "sourceToolAssistantUUID": "d171c286-eff4-4065-8fcc-52d471d38650",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-19T13:54:47.015Z_

<details><summary>↩ Tool result · reported error · `toolu_01JwaHhUcroAJ26Mjy5Piq7J`</summary>

```text
File content (41705 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92325ce4-c5aa-429f-8d1c-521d166cce09",
  "isSidechain": true,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "agentId": "a6b9c6ef519ef00f3",
  "type": "user",
  "uuid": "d4c34703-c883-4854-8913-6aee3e8dab87",
  "toolUseResult": "Error: File content (41705 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "92325ce4-c5aa-429f-8d1c-521d166cce09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-19T13:54:48.798Z_

Good! I found the experiments.tex file. Now let me read the appendix.tex file in sections to find the cross-selection table. Let me search for it first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4c34703-c883-4854-8913-6aee3e8dab87",
  "isSidechain": true,
  "agentId": "a6b9c6ef519ef00f3",
  "requestId": "req_011CbC3LeVXsmwxRbGN7PzD4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a6c1b80d-1a2d-44e8-920f-7309662d52dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CcYF7LqAXtBDcDVeBT7UBU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 8154,
      "cache_read_input_tokens": 21390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8154,
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

_source line 11 · 2026-05-19T13:54:50.103Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01TYtProB82tBFhmczfbTRFb`</summary>

```json
{
  "pattern": "cross.selection|cross_selection|LP.*F1.*Δ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "context": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6c1b80d-1a2d-44e8-920f-7309662d52dd",
  "isSidechain": true,
  "agentId": "a6b9c6ef519ef00f3",
  "requestId": "req_011CbC3LeVXsmwxRbGN7PzD4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fb84680f-1eb0-420e-a604-3b48c599f98c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CcYF7LqAXtBDcDVeBT7UBU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 8154,
      "cache_read_input_tokens": 21390,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8154
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 197,
          "cache_read_input_tokens": 21390,
          "cache_creation_input_tokens": 8154,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8154,
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

_source line 12 · 2026-05-19T13:54:50.120Z_

<details><summary>↩ Tool result · `toolu_01TYtProB82tBFhmczfbTRFb`</summary>

```text
219-SJ      & .089 & .517 & .288 & ${<}$1e-7 \\
220-EM      & .050 & .487 & .333 & ${<}$1e-9 \\
221-LP & $-$.410 & .219 & .350 & ${<}$1e-10 \\
222-\bottomrule
223-\end{tabular}
224-\end{table}
225-The full-set $p$-values are: VC ${<}$1e-112, FK $p{=}0.001$, SJ $p{=}0.020$, EM $p{=}0.194$, LP ${<}$1e-28.
226-VC's high full-set $\rho{=}0.724$ is entirely driven by the zero/non-zero boundary (conditional $\rho{=}0.038$, $p{=}0.49$), while LP's conditional $\rho{=}0.350$ is the highest among all signals on the non-zero subset, full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.
227-
228-\paragraph{Cross-configuration selection analysis.}
229:Table~\ref{tab:cross_selection} extends the selection analysis to five additional configurations.
230-On LLaMA SciERC, where output diversity remains substantial (18\% identical outputs, 39\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of single-sample (0.646), replicating the gap observed on Qwen SciERC (Table~\ref{tab:selection}).
231-[Omitted long context line]
232-On CoNLL, 48--87\% of instances produce identical outputs across all $N$ samples; this reflects a ceiling effect (single-sample F1 ${\approx}$0.91--0.92) rather than signal failure, and selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.
233-
234-\begin{table*}[t]
235-\centering
236-\small
237-\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$, 3-seed mean). Best non-oracle signal per row in \textbf{bold}. LP is the only signal with positive selection on both FewNERD configurations (Qwen $+1.39$~pp, Table~\ref{tab:fewnerd}; LLaMA $+0.36$~pp). At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}
238:\label{tab:cross_selection}
239-\begin{tabular}{llccccccc}
240-\toprule
241-Config & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\
242-\midrule
243-LLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \textbf{.652} & .633 \\
244-LLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \textbf{.649} & \textbf{.649} & .640 & .646 & .640 \\
245-\addlinespace
246-LLaMA/FewNERD $N{=}8$ & 32{,}565 & .784 & .884 & .779 & .779 & .774 & \textbf{.788} & .760 \\
247-\addlinespace
248-Qwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .957 & \textbf{.899} & .893 & .898 & .897 & .895 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb84680f-1eb0-420e-a604-3b48c599f98c",
  "isSidechain": true,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "agentId": "a6b9c6ef519ef00f3",
  "type": "user",
  "uuid": "927d4522-a7b2-466c-a5c1-5fb7571e0bc3",
  "sourceToolAssistantUUID": "fb84680f-1eb0-420e-a604-3b48c599f98c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-19T13:54:51.583Z_

Perfect! I found the cross-selection table. Let me continue reading that section to get the complete table and any additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "927d4522-a7b2-466c-a5c1-5fb7571e0bc3",
  "isSidechain": true,
  "agentId": "a6b9c6ef519ef00f3",
  "requestId": "req_011CbC3LshXnLHhX9EwfYNFL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ec430a27-2b6f-48a5-8445-3ee0c5876a6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SQFiuct5UjUfdmsqMRoq13",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1254,
      "cache_read_input_tokens": 29544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1254,
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

_source line 14 · 2026-05-19T13:54:52.713Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01HPgGhWapywD8RRc7zFDTNW`</summary>

```json
{
  "pattern": "Qwen/CoNLL|LLaMA/CoNLL",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "context": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec430a27-2b6f-48a5-8445-3ee0c5876a6d",
  "isSidechain": true,
  "agentId": "a6b9c6ef519ef00f3",
  "requestId": "req_011CbC3LshXnLHhX9EwfYNFL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "77e713c0-5d8c-4529-a91a-e49a6deb67e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SQFiuct5UjUfdmsqMRoq13",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1254,
      "cache_read_input_tokens": 29544,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1254
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 186,
          "cache_read_input_tokens": 29544,
          "cache_creation_input_tokens": 1254,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1254,
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

_source line 15 · 2026-05-19T13:54:52.736Z_

<details><summary>↩ Tool result · `toolu_01HPgGhWapywD8RRc7zFDTNW`</summary>

```text
243-LLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \textbf{.652} & .633 \\
244-LLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \textbf{.649} & \textbf{.649} & .640 & .646 & .640 \\
245-\addlinespace
246-LLaMA/FewNERD $N{=}8$ & 32{,}565 & .784 & .884 & .779 & .779 & .774 & \textbf{.788} & .760 \\
247-\addlinespace
248:Qwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .957 & \textbf{.899} & .893 & .898 & .897 & .895 \\
249:LLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \textbf{.925} & .924 & .924 & .923 \\
250-\bottomrule
251-\end{tabular}
252-\end{table*}
253-
254-\paragraph{Diminishing returns of $N$-scaling.}
--
329-\toprule
330-Config & Identical & Unique \\
331-\midrule
332-Qwen/SciERC & 11\% & 43\% \\
333-LLaMA/SciERC & 18\% & 39\% \\
334:Qwen/CoNLL & 57\% & --- \\
335:LLaMA/CoNLL & 88\% & --- \\
336-WNUT-17 & 55\% & --- \\
337-\bottomrule
338-\end{tabular}
339-\end{table}
340-
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77e713c0-5d8c-4529-a91a-e49a6deb67e8",
  "isSidechain": true,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "agentId": "a6b9c6ef519ef00f3",
  "type": "user",
  "uuid": "37525ccb-a77c-4fc3-b004-50d4f19f7132",
  "sourceToolAssistantUUID": "77e713c0-5d8c-4529-a91a-e49a6deb67e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-19T13:54:54.364Z_

Excellent! Now let me search for Table 1 specifically to get the SciERC AUROC values more clearly, and also look for Table 3 about degeneracy rates.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37525ccb-a77c-4fc3-b004-50d4f19f7132",
  "isSidechain": true,
  "agentId": "a6b9c6ef519ef00f3",
  "requestId": "req_011CbC3M51AzZqj8UMTyy1LY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "40faf481-0a4b-4be4-b035-6c3b0866fe4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UJW6Tse6EPpv1nvdWW9KQd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 721,
      "cache_read_input_tokens": 30798,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 721,
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

_source line 17 · 2026-05-19T13:54:55.010Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01QWF4QzGkumAiDzcZQ8wuHP`</summary>

```json
{
  "pattern": "tab:quality_estimation|SciERC.*AUROC|AUC.*\\.663|AUC.*\\.650",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "output_mode": "content",
  "context": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40faf481-0a4b-4be4-b035-6c3b0866fe4a",
  "isSidechain": true,
  "agentId": "a6b9c6ef519ef00f3",
  "requestId": "req_011CbC3M51AzZqj8UMTyy1LY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "33298ebc-33c4-4a7a-8c04-f91a3dbfbab2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UJW6Tse6EPpv1nvdWW9KQd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 721,
      "cache_read_input_tokens": 30798,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 721
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 212,
          "cache_read_input_tokens": 30798,
          "cache_creation_input_tokens": 721,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 721,
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

_source line 18 · 2026-05-19T13:54:55.033Z_

<details><summary>↩ Tool result · `toolu_01QWF4QzGkumAiDzcZQ8wuHP`</summary>

```text
11-\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
12-\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 51\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
13-
14-\paragraph{Models and sampling.}
15-\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (training details in Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others due to earlier convergence; Appendix~\ref{app:epoch_confound}).
16-We draw $N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}, with $N{=}16$ for scaling experiments (Appendix~\ref{app:n_scaling}).
17-
18-%% ============================================================
19-\subsection{Quality Estimation Results}
20-\label{sec:qe_results}
21-
22-\begin{table*}[t]
23-\centering
24-\small
25-\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\sigma{\leq}0.026$ in Table~\ref{tab:multiseed}). Best in \textbf{bold}. RE results in Appendix~\ref{app:re_extension}. $N{=}16$ in Table~\ref{tab:robustness}.}
26:\label{tab:quality_estimation}
27-\begin{tabular}{ll cc cc cc}
28-\toprule
29-& & \multicolumn{2}{c}{\textbf{SciERC}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
30-\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8}
31-Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
32-\midrule
33-VC & Structural & \textbf{.379} & \textbf{.663} & .424 & .789 & .426 & .709 \\
34-SJ  & Structural & .360 & .650 & .436 & .801 & \textbf{.431} & .704 \\
35-FK & Surface & .267 & .602 & .400 & .774 & .428 & .703 \\
36-EM  & Surface    & .295 & .614 & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
37-\midrule
38-LP     & Model      & .205 & .578 & .316 & .753 & .307 & \textbf{.761} \\
39-\bottomrule
40-\end{tabular}
41-\end{table*}
42-
43:Table~\ref{tab:quality_estimation} presents $\rho$ and AUROC for five signals across tasks and models ($\varepsilon$-free; $\varepsilon{=}0.05$ applies to selection only, stable across $[0, 0.2]$, Appendix~\ref{app:epsilon_robustness}).
44-
45-\paragraph{Signal rankings are difficulty-dependent.}
46-On SciERC (medium difficulty), structural signals lead (VC $\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\Delta\rho{=}{+}0.155$; Appendix~\ref{app:bootstrap_signal}).
47-On CoNLL (single-sample F1${\approx}$0.91), EM leads both $\rho$ and AUROC ($0.816$).
48-At the signal-collapse boundary (WNUT-17, macro F1${\approx}$42\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\rho{=}0.724$ but conditional $\rho{=}0.038$; Table~\ref{tab:wnut}); LP shows the reverse (conditional $\rho{=}0.350$; Figure~\ref{fig:signal_heatmap}).
49-This collapse illustrates a regime where model capability is insufficient to produce meaningful inter-sample variation: 51\% of instances yield zero F1 across all samples, and consistency signals merely detect this floor rather than discriminating quality among non-trivial outputs.
50-
51-%% ============================================================
52-\subsection{The Correlation-Selection Gap}
53-\label{sec:selection_gap}
54-
55-Four of five signals (SJ, FK, EM, VC) assign identical scores to all candidates from the same input by construction (\S\ref{sec:formulation}); they can estimate quality across instances but cannot rank candidates within an instance.
56-The empirical question is whether LP, the sole per-sample signal, can exploit its candidate-discriminative nature for selection.
57-LP selection effectiveness is primarily determined by LP-quality alignment rather than degeneracy level (\S\ref{sec:discussion}).
58:Cross-instance $\rho$ (Table~\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.
59-
60-\begin{table}[t]
61-\centering
62-\small
63-\caption{Best-of-$N$ NER selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\pm}\sigma$). LP is per-sample; others use consensus-proximity. Best non-oracle in \textbf{bold}. Non-tied subset in \S\ref{sec:discussion}; RE in Appendix~\ref{app:re_extension}. $^\dagger$Instance-level signals assign one score per input; per-sample ranking $p$-values are undefined.}
64-\label{tab:selection}
65-\begin{tabular}{lcc}
66-\toprule
67-Method & NER F1 & $p$ \\
68-\midrule
69-Oracle & $0.775 \pm 0.001$ & --- \\
70-Greedy ($T{=}0$) & $0.645 \pm 0.001$ & --- \\
71-\midrule
72-\multicolumn{3}{l}{\textit{Per-sample signal}} \\
73-LP           & $\mathbf{0.647} \pm 0.005$ & .29 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33298ebc-33c4-4a7a-8c04-f91a3dbfbab2",
  "isSidechain": true,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "agentId": "a6b9c6ef519ef00f3",
  "type": "user",
  "uuid": "2c4a6958-f6d6-4638-97c7-c217dc90299e",
  "sourceToolAssistantUUID": "33298ebc-33c4-4a7a-8c04-f91a3dbfbab2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-19T13:54:56.260Z_

Perfect! Now let me search for Table 3 with degeneracy and delta values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c4a6958-f6d6-4638-97c7-c217dc90299e",
  "isSidechain": true,
  "agentId": "a6b9c6ef519ef00f3",
  "requestId": "req_011CbC3MEk4mJeecTpXVqugY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "050e626c-f599-47de-bb40-f90053a87d78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RJLGS4aJtGJ9fvrcv2c5s1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 2202,
      "cache_read_input_tokens": 31519,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2202,
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

_source line 20 · 2026-05-19T13:54:57.718Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01UReKPHuPcrRePF4Ju9gbfx`</summary>

```json
{
  "pattern": "tab:fewnerd|Degen|degeneracy.*\\%|LP.*Δ|Delta",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "output_mode": "content",
  "context": 12
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "050e626c-f599-47de-bb40-f90053a87d78",
  "isSidechain": true,
  "agentId": "a6b9c6ef519ef00f3",
  "requestId": "req_011CbC3MEk4mJeecTpXVqugY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5db9322d-0527-41db-99ad-83574f782d1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RJLGS4aJtGJ9fvrcv2c5s1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 2202,
      "cache_read_input_tokens": 31519,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2202
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 186,
          "cache_read_input_tokens": 31519,
          "cache_creation_input_tokens": 2202,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2202,
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

_source line 21 · 2026-05-19T13:54:57.750Z_

<details><summary>↩ Tool result · `toolu_01UReKPHuPcrRePF4Ju9gbfx`</summary>

```text
34-SJ  & Structural & .360 & .650 & .436 & .801 & \textbf{.431} & .704 \\
35-FK & Surface & .267 & .602 & .400 & .774 & .428 & .703 \\
36-EM  & Surface    & .295 & .614 & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
37-\midrule
38-LP     & Model      & .205 & .578 & .316 & .753 & .307 & \textbf{.761} \\
39-\bottomrule
40-\end{tabular}
41-\end{table*}
42-
43-Table~\ref{tab:quality_estimation} presents $\rho$ and AUROC for five signals across tasks and models ($\varepsilon$-free; $\varepsilon{=}0.05$ applies to selection only, stable across $[0, 0.2]$, Appendix~\ref{app:epsilon_robustness}).
44-
45-\paragraph{Signal rankings are difficulty-dependent.}
46:On SciERC (medium difficulty), structural signals lead (VC $\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\Delta\rho{=}{+}0.155$; Appendix~\ref{app:bootstrap_signal}).
47-On CoNLL (single-sample F1${\approx}$0.91), EM leads both $\rho$ and AUROC ($0.816$).
48-At the signal-collapse boundary (WNUT-17, macro F1${\approx}$42\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\rho{=}0.724$ but conditional $\rho{=}0.038$; Table~\ref{tab:wnut}); LP shows the reverse (conditional $\rho{=}0.350$; Figure~\ref{fig:signal_heatmap}).
49-This collapse illustrates a regime where model capability is insufficient to produce meaningful inter-sample variation: 51\% of instances yield zero F1 across all samples, and consistency signals merely detect this floor rather than discriminating quality among non-trivial outputs.
50-
51-%% ============================================================
52-\subsection{The Correlation-Selection Gap}
53-\label{sec:selection_gap}
54-
55-Four of five signals (SJ, FK, EM, VC) assign identical scores to all candidates from the same input by construction (\S\ref{sec:formulation}); they can estimate quality across instances but cannot rank candidates within an instance.
56-The empirical question is whether LP, the sole per-sample signal, can exploit its candidate-discriminative nature for selection.
57-LP selection effectiveness is primarily determined by LP-quality alignment rather than degeneracy level (\S\ref{sec:discussion}).
58-Cross-instance $\rho$ (Table~\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.
--
77-FK           & $0.646 \pm 0.001$ & .79 \\
78-EM           & $0.637 \pm 0.001$ & n/a$^\dagger$ \\
79-VC           & $0.623 \pm 0.004$ & n/a$^\dagger$ \\
80-\midrule
81-Random           & $0.610 \pm 0.003$ & --- \\
82-\bottomrule
83-\end{tabular}
84-\end{table}
85-
86-\begin{figure}[t]
87-\centering
88-\includegraphics[width=\columnwidth]{fig_selection_gap}
89:\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Bars: quality estimation $\rho$ (seed 42); line with error bars: $\Delta$F1 vs.\ greedy (3-seed mean, seeds 42/123/456). Despite $\rho$ up to 0.38, no signal significantly outperforms greedy (all $p{>}0.05$; Table~\ref{tab:selection}). Dashed green: oracle upper bound ($+13.1$~pp); dotted gray: random baseline.}
90-\label{fig:selection_gap}
91-\end{figure}
92-
93-Instance-level signals assign identical QE scores to all candidates; MBR conversion does not improve over greedy on the primary test bed (Table~\ref{tab:selection}; Figure~\ref{fig:selection_gap}).
94-Instance-level signals predict \textit{which inputs} the model handles reliably, not \textit{which output} is best.
95-
96-\paragraph{LP: the sole per-sample signal also fails.}
97-On SciERC ($n{=}529$, 2-seed sign tests\footnote{MDE${\approx}$1.5~pp at 80\% power ($n{=}529$); Few-NERD ($n{=}32{,}565$; MDE${\approx}$0.22~pp) provides the definitive test.}), the oracle (0.775) reveals 13.0~pp of headroom, but LP achieves $+0.2$~pp ($p{=}0.29$), below the MDE (${\approx}$1.5~pp); selection effects below this threshold cannot be reliably detected.
98-The pattern holds across CoNLL and WNUT-17 (Table~\ref{tab:cross_selection}); under stringent TOST anchors, some configurations show significant \textit{degradation} (Appendix~\ref{app:tost}).
99-Few-NERD provides the definitive contrast: LP achieves $+1.39$~pp ($p{<}0.001$) at low degeneracy (\S\ref{sec:fewnerd}), while structural signals still degrade selection.
100-
101-\paragraph{Qualitative factors governing selection effectiveness.}
102:[Omitted long matching line]
103:[Omitted long matching line]
104-Yet QE remains effective on WNUT-17 (VC $\rho{=}0.724$; Table~\ref{tab:wnut}), confirming QE-selection decoupling at this boundary.
105-This characterization is qualitative: the three factors do not combine into a predictive model ($R^2{<}0$ across 23 configurations), but each factor's role is individually supported by controlled ablations (\S\ref{sec:fewnerd}, \S\ref{sec:discussion}).
106-
107-%% ============================================================
108-\subsection{Cross-Dataset Contrast: Few-NERD}
109-\label{sec:fewnerd}
110-
111-\begin{table}[t]
112-\centering
113-\small
114-\caption{LP selection across datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). Few-NERD/CoNLL: 3-seed means; SciERC: single-seed (3-seed in Table~\ref{tab:multiseed}). $p$: paired bootstrap.}
115:\label{tab:fewnerd}
116-\resizebox{\columnwidth}{!}{%
117-\begin{tabular}{@{}lrccccr@{}}
118-\toprule
119:Dataset & $n$ & Greedy & Degen.\% & LP $\rho$ & LP $\Delta$ & $p$ \\
120-\midrule
121-WNUT-17 & 1{,}287 & .452 & 67.9\% & $-$.446 & $-$0.45\,pp & .72 \\
122-CoNLL & 2{,}756 & .908 & 48.4\% & .302 & $-$0.85\,pp & 1.0 \\
123-SciERC & 529 & .644 & 17.8\% & .205 & $+$0.61\,pp & .193 \\
124-Few-NERD & 32{,}565 & .748 & 13.8\% & .220 & $\mathbf{+1.39}$\,pp & ${<}.001$ \\
125-\bottomrule
126-\end{tabular}}
127-\end{table}
128-
129:Few-NERD (Table~\ref{tab:fewnerd}) confirms LP selection at low degeneracy: $+1.39$~pp ($p{<}0.001$), while structural signals degrade selection (VC $-1.79$, SJ $-2.14$~pp). LP is 50$\times$ more seed-stable ($\sigma{=}0.04$ vs.\ SJ $2.02$~pp) and generalizes to LLaMA-3.1-8B (Table~\ref{tab:cross_selection}).
130:Training convergence modulates degeneracy: 5-epoch Few-NERD raises degeneracy to 31\% and halves LP gains (Appendix~\ref{app:epoch_confound}).
131-
132:\paragraph{Degeneracy alone does not predict LP selection direction.}
133-Across 23 configurations, degeneracy does not predict LP gain ($\rho{=}0.052$, $p{=}0.81$; Figure~\ref{fig:degeneracy_scatter}), though within fixed settings it causally modulates LP ($\rho{=}{-}0.881$; Appendix~\ref{app:per_type_lp}).
134-Cross-dataset prediction requires LP signal quality: Few-NERD ($\rho{\approx}0.5$--$0.7$) shows consistent gains, SciERC ($\rho{\approx}0.26$) does not (Appendix~\ref{app:conditional_decomp}).
135-
136-\begin{figure}[t]
137-\centering
138-\includegraphics[width=\columnwidth]{figures/fig_degeneracy_lp_scatter.pdf}
139-\caption{Instance degeneracy vs.\ LP selection gain across 23 configurations ($N{=}8$; $\rho{=}0.052$, $p{=}0.81$). Within Few-NERD per-entity-type analysis ($\rho{=}{-}0.881$; Appendix~\ref{app:per_type_lp}), degeneracy predicts LP gain when alignment is held constant.}
140-\label{fig:degeneracy_scatter}
141-\end{figure}
142-
143-Structural signals remain negative regardless of sample budget; $N$-scaling analyses are in Appendix~\ref{app:n_scaling}.
144-
--
146-\subsection{Robustness}
147-\label{sec:robustness_main}
148-
149-Consistency signals are robust across $T{\in}\{0.7, 1.0\}$ with sublinear $N$-scaling gains (Table~\ref{tab:robustness}); signal rankings are stable across seeds ($W{=}1.0$; Table~\ref{tab:ranking-stability}). NER calibration is reasonable (ECE 0.069--0.096; Appendix~\ref{app:calibration}).
150-
151-\begin{table}[t]
152-\centering
153-\small
154-\caption{Scale ablation: 8B vs.\ 4B QE $\rho$ ($N{=}8$, $T{=}1.0$, seed 42). RE in Appendix~\ref{app:re_extension}.}
155-\label{tab:scale_ablation}
156-\begin{tabular}{@{}ll cc r@{}}
157-\toprule
158:& & \textbf{8B} & \textbf{4B} & $\Delta$ \\
159-\midrule
160-CoNLL & SJ & .436 & .422 & $-$.014 \\
161-      & FK & .400 & .418 & $+$.018 \\
162-SciERC & SJ & .360 & .422 & $+$.062 \\
163-       & FK & .267 & .326 & $+$.059 \\
164-\bottomrule
165-\end{tabular}
166-\end{table}
167-
168-\paragraph{Scale robustness.}
169:With Qwen3-4B (Table~\ref{tab:scale_ablation}), QE is comparable (mean $|\Delta\rho|{=}0.042$), yet selection remains below greedy despite 13.0~pp headroom. Task difficulty is a stronger predictor than model scale within the 3B--8B range (Appendix~\ref{app:llama3b}).
170:Degeneracy scales with capability: 8B shows 17.8\% vs.\ 4B's 10.4\% on SciERC (Table~\ref{tab:degeneracy}).
171-
172-\paragraph{LoRA-rank ablation.}
173:LoRA rank${=}8$ (vs.\ 32) lowers degeneracy to 7.2\% but LP remains below greedy ($\rho(\text{LP}, \text{F1}){\approx}0.24$); temperature manipulation ($T{=}1.2$; \S\ref{sec:discussion}) confirms that low degeneracy and adequate alignment are independently necessary.
174-
175-\paragraph{Supervised signal combination and hidden probes.}
176-Supervised classifiers (LR, MLP, RF; 5-fold CV, $N{=}16$) and a DeBERTa-v3-base verifier all fail to close the selection gap (Appendix~\ref{app:supervised_combination}).
177-Hidden state probes improve correlation ($+37$\% on SciERC) but not selection (gap closure $-5.1$\%; Appendix~\ref{app:hidden_probe}); the bottleneck extends to model-internal representations.
178-
179-%% ============================================================
180-\subsection{Scaling Behavior}
181-\label{sec:scaling}
182-
183-We evaluate Qwen2.5-72B-Instruct in a zero-shot setting to test whether the gap persists at larger scale without fine-tuning.
184-
185-\begin{table}[t]
--
216-%% ============================================================
217-\subsection{Prescriptive Results}
218-\label{sec:prescriptive}
219-
220-The preceding sections establish that instance-level selection fails for structured IE. We now present two approaches that extract value from multi-sample generation without relying on sample ranking.
221-
222-\paragraph{Entity-level construction.}
223-[Omitted long context line]
224-
225-\begin{table}[t]
226-\centering
227-\small
228:\caption{Entity construction vs.\ greedy ($\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\pm}\sigma$). $\theta{=}2/N$. $p$: paired bootstrap vs.\ greedy. Best in \textbf{bold}.}
229-\label{tab:entity_construction}
230-\resizebox{\columnwidth}{!}{%
231-\begin{tabular}{@{}llcccc@{}}
232-\toprule
233:Dataset & Wt. & Greedy & Constr. & $\Delta$ & $p$ \\
234-\midrule
235-SciERC & LP & $.646{\pm}.002$ & $\mathbf{.656{\pm}.003}$ & $+1.02{\pm}0.49$\,pp & .004 \\
236-       & Unif. & $.646{\pm}.002$ & $.653{\pm}.006$ & $+0.74{\pm}0.71$\,pp & .023 \\
237-\addlinespace
238-Few-NERD & LP & $.748$ & $\mathbf{.762{\pm}.005}$ & $+1.40{\pm}0.51$\,pp & ${<}.001$ \\
239-         & Unif. & $.748$ & $.756{\pm}.006$ & $+0.74{\pm}0.58$\,pp & .003 \\
240-\addlinespace
241-CoNLL & Unif. & .908 & .904 & $-0.39$\,pp & n.s. \\
242-\bottomrule
243-\end{tabular}}
244-\end{table}
245-
246-[Omitted long context line]
247-
248-\paragraph{LP-alignment gating (preliminary diagnostic).}
249-Construction and LP selection are complementary: construction dominates on SciERC ($+1.02$\,pp vs.\ LP $+0.04{\pm}0.48$\,pp, n.s.; $\rho{\approx}0.2$), while on Few-NERD both yield comparable gains ($+1.40$ vs.\ $+1.39$\,pp; $\rho{\approx}0.5$--$0.7$).
250:We estimate within-instance $\rho(\text{LP}, \text{F1})$ on 50 held-out instances with bootstrap CIs (1000 resamples). Degeneracy-adjusted $\rho_{\text{adj}}$: Few-NERD $0.516$ [0.459, 0.759], SciERC $0.167$ [0.146, 0.281], CoNLL $0.065$ [$-$0.061, 0.620], WNUT-17 ${\approx}0$ (n.s.).
251-The protocol performs three-way routing: (1)~$\rho_{\text{adj}} \geq \tau{=}0.3$: apply LP selection; (2)~$\rho_{\text{adj}} < \tau$ and construction shows positive dev-set gain: apply construction; (3)~otherwise: retain greedy decoding.
252-This routes Few-NERD to LP selection ($+1.39$\,pp); SciERC, CoNLL, and WNUT-17 fall below $\tau$ and route to greedy. The conservative protocol trades SciERC's missed construction gain ($+1.02$\,pp) for protection against negative outcomes (CoNLL $-0.39$\,pp, WNUT-17 n.s.).
253-Routing is stable across $\tau{\in}[0.2, 0.4]$ and matches test-set direction for all four datasets; narrower inter-dataset margins remain untested.
254-
255-\paragraph{Selective prediction.}
256-Orthogonal to construction, QE signals support selective prediction: at 80\% coverage, filtering low-confidence instances yields $+5$--$8$\,pp F1 (AUPRC 0.70--0.92; Table~\ref{tab:cross_selection}).
257-
258-\phantomsection\label{sec:selection_results}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5db9322d-0527-41db-99ad-83574f782d1b",
  "isSidechain": true,
  "promptId": "0731b9be-f5e6-4a8a-9a3c-2edafe06629b",
  "agentId": "a6b9c6ef519ef00f3",
  "type": "user",
  "uuid": "c386042f-4d2b-4cad-bd8a-2c2e1de15b81",
  "sourceToolAssistantUUID": "5db9322d-0527-41db-99ad-83574f782d1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-19T13:55:05.427Z_

Perfect! I have found all the key information. Let me now compile the exact numbers from the tables you requested.

## Summary of Exact Numbers from Tables

Based on the files I've read, here are the exact numeric values you requested:

### **TABLE 1: SciERC AUROC Column (tab:quality_estimation)**
Located in experiments.tex, lines 22-41:

| Signal | Family | SciERC AUROC |
|--------|--------|--------------|
| VC | Structural | **0.663** |
| SJ | Structural | 0.650 |
| FK | Surface | 0.602 |
| EM | Surface | 0.614 |
| LP | Model | 0.578 |

### **TABLE 3: LP Selection Across Datasets (tab:fewnerd)**
Located in experiments.tex, lines 111-127:

| Dataset | n | Greedy | Degen.% | LP ρ | LP Δ | p |
|---------|-------|--------|---------|-------|-----------|-------|
| WNUT-17 | 1,287 | .452 | **67.9%** | -.446 | **-0.45 pp** | .72 |
| CoNLL | 2,756 | .908 | **48.4%** | .302 | **-0.85 pp** | 1.0 |
| SciERC | 529 | .644 | **17.8%** | .205 | **+0.61 pp** | .193 |
| Few-NERD | 32,565 | .748 | **13.8%** | .220 | **+1.39 pp** | <.001 |

### **APPENDIX CROSS-SELECTION TABLE (tab:cross_selection)**
Located in appendix.tex, lines 234-250:

| Config | n | Greedy | Oracle | SJ | FK | EM | **LP** | VC |
|--------|-------|--------|--------|--------|--------|--------|-----------|--------|
| LLaMA/SciERC N=8 | 529 | .646 | .778 | .643 | .639 | .634 | **0.652** | .633 |
| LLaMA/SciERC N=16 | 529 | .645 | .806 | .649 | .649 | .640 | **0.646** | .640 |
| LLaMA/FewNERD N=8 | 32,565 | .784 | .884 | .779 | .779 | .774 | **0.788** | .760 |
| Qwen/CoNLL N=8 | 2,756 | .908 | .957 | .899 | .893 | .898 | **0.897** | .895 |
| LLaMA/CoNLL N=8 | 2,756 | .924 | .943 | .924 | .925 | .924 | **0.924** | .923 |

The cross-selection table shows F1 scores (macro, instance-averaged) for best-of-N selection with LP marked in bold as requested. The corresponding Δ values (improvements over greedy) and other metrics can be derived from the differences shown.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c386042f-4d2b-4cad-bd8a-2c2e1de15b81",
  "isSidechain": true,
  "agentId": "a6b9c6ef519ef00f3",
  "requestId": "req_011CbC3MSUG3YLQXtn9PCVvQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dbc4bf08-13cf-4a59-b09b-78a28748ba84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a97de670-f9a7-4d30-affd-382982b8a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EALteHgQJeRbMxnfacD4AJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5092,
      "cache_read_input_tokens": 33721,
      "output_tokens": 810,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5092
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 810,
          "cache_read_input_tokens": 33721,
          "cache_creation_input_tokens": 5092,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5092,
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
