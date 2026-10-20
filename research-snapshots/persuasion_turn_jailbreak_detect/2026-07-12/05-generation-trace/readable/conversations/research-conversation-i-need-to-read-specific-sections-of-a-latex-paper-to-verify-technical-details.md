# Research conversation: I need to read specific sections of a LaTeX paper to verify technical details for a peer review. The paper is at /home/u

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a8daa86d1003cff17.jsonl`
- **Structured JSON:** [`d6570709424a5058c378.json`](../../sessions/d6/d6570709424a5058c378.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

14 recorded events

### User

_source line 1 · 2026-05-23T11:13:50.368Z_

I need to read specific sections of a LaTeX paper to verify technical details for a peer review. The paper is at /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/

I need to find and read:
1. The experiments section - specifically where bootstrap CI and confidence intervals methodology is described (likely in the experiments.tex file, around Section 4.1 or "Metrics")
2. The part about TOST equivalence testing and delta=5pp
3. The appendix section about length stratification (Appendix U)
4. The appendix section about benign distribution shift / WildChat FPR (likely Appendix P)
5. The appendix section about padding experiments
6. The section about variance reduction claims across seeds
7. The appendix about dataset scale validation (Appendix J)

Search breadth: very thorough. Read the relevant passages in full, quoting exact text. I need exact wording for my review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "968750d3-8ea0-4a1a-a2c1-b6601657157c",
  "agentId": "a8daa86d1003cff17",
  "type": "user",
  "uuid": "154f584c-bb0a-4e69-94e8-a0ce01bb8646",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cc8c01a1-4471-49ec-97ac-eac0175f808e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-23T11:13:51.670Z_

I'll help you find and read these specific sections from the LaTeX paper. Let me start by exploring the paper structure and locating all these sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "154f584c-bb0a-4e69-94e8-a0ce01bb8646",
  "isSidechain": true,
  "agentId": "a8daa86d1003cff17",
  "requestId": "req_011CbKQJUdNh9X9tcQi1rEGu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0d367a79-7a02-4da2-99c0-0e022df0347d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cc8c01a1-4471-49ec-97ac-eac0175f808e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017rmZniiEwYSRKGkjFetzXX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18133,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18133,
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

_source line 3 · 2026-05-23T11:13:51.945Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01U2m6jXEjxhV1tVsVYD7zcZ`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper -type f -name \"*.tex\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d367a79-7a02-4da2-99c0-0e022df0347d",
  "isSidechain": true,
  "agentId": "a8daa86d1003cff17",
  "requestId": "req_011CbKQJUdNh9X9tcQi1rEGu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0fda6e9c-312a-4cf9-9eda-4abf9bcba692",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cc8c01a1-4471-49ec-97ac-eac0175f808e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017rmZniiEwYSRKGkjFetzXX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18133,
      "cache_read_input_tokens": 0,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18133
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 134,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 18133,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18133,
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

_source line 4 · 2026-05-23T11:13:52.125Z_

<details><summary>↩ Tool result · `toolu_01U2m6jXEjxhV1tVsVYD7zcZ`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0fda6e9c-312a-4cf9-9eda-4abf9bcba692",
  "isSidechain": true,
  "promptId": "968750d3-8ea0-4a1a-a2c1-b6601657157c",
  "agentId": "a8daa86d1003cff17",
  "type": "user",
  "uuid": "0805a0f7-fca5-46a0-b532-7bb72dc3ed3a",
  "sourceToolAssistantUUID": "0fda6e9c-312a-4cf9-9eda-4abf9bcba692",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cc8c01a1-4471-49ec-97ac-eac0175f808e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-23T11:13:53.832Z_

Good! Now let me search for the specific sections you need. Let me start by reading the experiments.tex file to find the bootstrap CI and confidence intervals methodology:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0805a0f7-fca5-46a0-b532-7bb72dc3ed3a",
  "isSidechain": true,
  "agentId": "a8daa86d1003cff17",
  "requestId": "req_011CbKQJc5baYvPzWXS2K6mn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e6cb8056-2ec3-48de-98b3-e77b3145f100",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cc8c01a1-4471-49ec-97ac-eac0175f808e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ELkrwTFaxdtkQ6LycpTLa2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1361,
      "cache_read_input_tokens": 18133,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1361,
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

_source line 6 · 2026-05-23T11:13:54.038Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AxzApGUD1CLd9kXMEvKFcD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6cb8056-2ec3-48de-98b3-e77b3145f100",
  "isSidechain": true,
  "agentId": "a8daa86d1003cff17",
  "requestId": "req_011CbKQJc5baYvPzWXS2K6mn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "832c25c4-698c-4af7-b43b-0b73d588c29b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cc8c01a1-4471-49ec-97ac-eac0175f808e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ELkrwTFaxdtkQ6LycpTLa2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1361,
      "cache_read_input_tokens": 18133,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1361
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 127,
          "cache_read_input_tokens": 18133,
          "cache_creation_input_tokens": 1361,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1361,
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

_source line 7 · 2026-05-23T11:13:54.050Z_

<details><summary>↩ Tool result · `toolu_01AxzApGUD1CLd9kXMEvKFcD`</summary>

```text
1	% experiments.tex
2	
3	\section{Experiments}
4	
5	\paragraph{Terminology.}
6	\emph{Cross-attack OOD}: evaluation on attack families unseen during training; benign distribution remains IID throughout (OOD reflects attack-side shift only). $K$: prefix length (number of conversation turns retained). \emph{DAPT}: all Stage-1 adaptations; we extend \citet{gururangan2020dontstop} to supervised variants. \emph{Evidence hierarchy} (on synthetic data): vanilla $<$ MLM $<$ classification (Section~\ref{sec:decomposition}).
7	
8	\subsection{Setup}
9	
10	\paragraph{Data.}
11	All synthetic data is generated by Qwen3-8B~\citep{qwen3_2025}.
12	The IID dataset contains 250 Crescendo~\citep{russinovich2024crescendo} jailbreak and 250 topic-anchored benign conversations, split into training (350), validation (74), and test (76) sets with balanced class ratios (e.g., test = 38 jailbreak + 38 benign).
13	Stage~1 (DAPT) uses training + validation conversations; Stage~2 (BiGRU) trains on training, early-stops on validation, and evaluates on test.
14	OOD evaluation pairs attack-specific jailbreak conversations with the 38 IID-test benign conversations: 80 FITD~\citep{fitd2024} (non-discriminative; Section~\ref{sec:decomposition}) + 38 benign = 118 total, 80 Deceptive Delight (DD)~\citep{deceptivedelight2024} + 38 benign = 118 total, and 80 ActorAttack~\citep{ren2024actorattack} + 38 benign = 118 total.
15	No overlap exists in attack templates across families; benign is IID (same generation pipeline).
16	A paraphrased version of the IID test set (BERTScore 0.92, lexical overlap 0.20) serves as the adversarial robustness benchmark (Section~\ref{sec:perturbation}).
17	For human data validation, we use ToxicChat~\citep{lin2023toxicchat} (204 jailbreak + 204 benign from real LMSYS user interactions), entirely independent of Qwen3-8B generation.
18	
19	\paragraph{Models.}
20	Seven DeBERTa-v3 variants share the same Stage-2 pipeline and differ only in Stage-1 training (Section~\ref{sec:method}).
21	Our vanilla DeBERTa+BiGRU configuration is architecturally equivalent to DeepContext~\citep{deepcontext2026} and differs only in encoder choice (DeBERTa-v3-base vs.\ BERT); it serves as our primary baseline.
22	For cross-encoder validation, we replicate vanilla, MLM, and 9-class variants on RoBERTa-base~\citep{liu2019roberta} (Section~\ref{sec:cross_encoder}).
23	We also compare TF-IDF LR, LLM-as-judge (Appendix~\ref{sec:llm_judge}), and Llama Guard~3~8B~\citep{metallamaguard3_2024} (zero-shot; evaluates last-response safety given conversation context), which detects only 1.8\% of multi-turn jailbreaks (5/278 pooled recall; Table~\ref{tab:evidence_hierarchy}).
24	
25	\paragraph{Metrics.}
26	F1 for binary jailbreak detection at prefix $K$=2 and full conversations (full per-$K$ results in Appendix~\ref{sec:full_prefix}).
27	OOD results report 3-seed mean$\pm$std (seeds 42, 123, 456) for all variants.
28	For key pairwise comparisons, we report BCa bootstrap 95\% confidence intervals (10,000 resamples over individual predictions pooled across 3 seeds; this assumes cross-seed independence and is exploratory) and paired permutation tests (10,000 permutations). Seed-level F1 values (Table~\ref{tab:seed_level}, Appendix~\ref{app:seed_level}) confirm all pairwise conclusions hold at every seed.
29	All standard deviations are computed over 3 random seeds using the population formula ($n$ divisor); Bessel-corrected estimates ($n{-}1$ divisor) are $\approx$22\% larger but do not alter any significance conclusions.
30	
31	\paragraph{Training.}
32	Stage-1: learning rate $2 \times 10^{-5}$, batch 16, 4 epochs, MLM masking 15\%.
33	Stage-2: two-layer MLP, 20 epochs.
34	
35	%----------------------------------------------------------------------
36	\subsection{Cross-Attack Generalization}
37	
38	\begin{table}[t]
39	\centering
40	\small
41	\caption{Cross-attack generalization (F1) at $K$=2 and full conversation length. IID: Crescendo; OOD: Deceptive Delight (DD). 3-seed mean$\pm$std where noted; full per-$K$ in Appendix~\ref{sec:full_prefix}.}
42	\label{tab:main_results}
43	\begin{tabular}{@{}lcc|cc@{}}
44	\toprule
45	& \multicolumn{2}{c|}{\textit{IID (Cresc.)}} & \multicolumn{2}{c}{\textit{OOD (DD)}} \\
46	\textbf{Method} & $K$=2 & Full & $K$=2 & Full \\
47	\midrule
48	9-class & \textbf{1.000$\pm$.000} & \textbf{1.000$\pm$.000} & .981$\pm$.013 & \textbf{.997$\pm$.005} \\
49	MLM-only$^{\ddagger}$ & .974 & 1.000 & \textbf{.993$\pm$.009} & .914$\pm$.115 \\
50	Vanilla & .978$\pm$.016 & 1.000$\pm$.000 & .479$\pm$.038 & .312$\pm$.026 \\
51	TF-IDF LR$^{\S}$ & 1.000 & 1.000 & 1.000 & .961 \\
52	\bottomrule
53	\end{tabular}
54	\vspace{-2pt}
55	{\footnotesize $^{\ddagger}$MLM-only IID reports single seed (42); OOD reports 3-seed. $^{\S}$TF-IDF is deterministic (no std).}
56	\end{table}
57	
58	Vanilla encoders collapse under cross-attack transfer; domain-adapted variants recover near-perfect detection (Table~\ref{tab:main_results}, Figure~\ref{fig:cross_attack_bar}).
59	DD exhibits high lexical separability (TF-IDF F1\,=\,0.961); ActorAttack, where TF-IDF collapses to 0.261, serves as the primary stress test for beyond-lexical generalization.
60	On OOD DD, vanilla DeBERTa collapses to F1 = 0.312$\pm$0.026 and worsens with more turns (0.628 at $K$=1 to 0.312 at Full), consistent with attack turns occupying ``benign'' embedding regions~\citep{bullwinkel2025repeng}.
61	MLM achieves mean F1 $\geq$ 0.97 at all prefixes $K \leq 5$ without any classification labels; domain exposure alone is sufficient.
62	At full conversation length, MLM drops to 0.914$\pm$0.115 (seed 456 recall = 0.64), while the 9-class model maintains 0.997$\pm$0.005.
63	TF-IDF LR reaches F1 = 0.961 on full DD; DD is fully solvable by lexical features.
64	On strategy-diverse ActorAttack, TF-IDF collapses to F1 = 0.261 (precision = 1.0, recall = 0.15), while 9-class maintains 0.972$\pm$0.026: a 71\,pp gap. Lexical methods cannot capture multi-persona role-playing attack structure. This establishes a ``difficulty threshold'' for lexical methods parallel to that of vanilla encoders: both succeed on DD and fail on ActorAttack (Section~\ref{sec:limitations}).
65	Bootstrap CIs confirm non-overlapping intervals (9-class DD Full [0.943, 1.000] vs.\ vanilla [0.202, 0.341]; all permutation $p < 0.0001$). FITD is non-discriminative (all variants F1\,$\geq$\,0.990; Section~\ref{sec:limitations}).
66	
67	\begin{figure}[t]
68	\centering
69	\includegraphics[width=\columnwidth]{figures/paper/fig2_cross_attack_bar.pdf}
70	\caption{Cross-attack overview (F1 at full conversation length). DisPeD (9-class) maintains near-perfect detection across IID and both OOD families; vanilla collapses on OOD DD. FITD is non-discriminative for all methods.}
71	\label{fig:cross_attack_bar}
72	\end{figure}
73	
74	Prefix-length analysis (Appendix Table~\ref{tab:full_prefix}) shows vanilla F1 drops from 0.628 at $K$=1 to 0.312 at full length. MLM achieves strong early detection ($K$=2: 0.993) but is unstable at full length (0.914$\pm$0.115); the 9-class model maintains 0.972--0.997 across all prefixes. Classification supervision thus stabilizes against distributional drift.
75	
76	%----------------------------------------------------------------------
77	\subsection{Decomposing the Detection Mechanism}
78	\label{sec:decomposition}
79	
80	\begin{table}[t]
81	\centering
82	\small
83	\caption{Evidence hierarchy on OOD DD and ActorAttack (AA) at full conversation length (3-seed mean$\pm$std where available). OOD F1 reflects attack-side generalization only; benign samples are IID from training distribution (benign-side shift evaluated in Section~\ref{sec:benign_shift}). Bold indicates best per column. All variants share the same Stage-2 pipeline. Full per-prefix results in Appendix Tables~\ref{tab:full_prefix} and~\ref{tab:actorattack_full}.}
84	\label{tab:evidence_hierarchy}
85	\resizebox{\columnwidth}{!}{%
86	\begin{tabular}{@{}lccc@{}}
87	\toprule
88	\textbf{Variant} & DD-Full & AA-Full & DD-$K$=2 \\
89	\midrule
90	9-class (full model) & .997$\pm$.005 & .972$\pm$.026 & .981$\pm$.013 \\
91	Binary (2-class) & \textbf{1.000$\pm$.000} & \textbf{.990$\pm$.008} & .994$\pm$.009 \\
92	Scrambled labels & .997$\pm$.005 & .951$\pm$.043 & .981$\pm$.026 \\
93	MLM-only$^{\ddagger}$ (no labels) & .914$\pm$.115 & .893$\pm$.080 & .993$\pm$.009 \\
94	Mean pooling$^{*}$ & .991$\pm$.013 & .962$\pm$.015 & \textbf{1.000} \\
95	\midrule
96	Topic classif.\ (5-class) & .541$\pm$.207 & .625$\pm$.141 & .593$\pm$.166 \\
97	Wikipedia MLM & .904$\pm$.115 & .686$\pm$.297 & .911$\pm$.073 \\
98	Vanilla DeBERTa & .312$\pm$.026 & .258$\pm$.000 & .479$\pm$.038 \\
99	TF-IDF LR$^{\dagger}$ & .961 & .261 & \textbf{1.000} \\
100	Llama Guard~3$^{\P}$ & .025 & .000 & -- \\
101	\bottomrule
102	\end{tabular}}
103	\vspace{-2pt}
104	{\footnotesize $^{*}$9-class encoder with mean pooling replacing BiGRU. $^{\dagger}$Deterministic (no std). $^{\ddagger}$MLM-only IID (Table~\ref{tab:main_results}) is single-seed (42); all OOD values are 3-seed. $^{\P}$Zero-shot; no domain training.}
105	\end{table}
106	
107	A clear \emph{evidence hierarchy} emerges across seven variants (Table~\ref{tab:evidence_hierarchy}), ordered by OOD detection at full conversation length on DD:
108	
109	\noindent\hspace{0.5em}{\small vanilla (0.312$\pm$0.026) $<$ topic (0.541$\pm$0.207) $\ll$ wiki-MLM (0.904$\pm$0.115) $\approx$ jb-MLM (0.914$\pm$0.115) $<$ scrambled (0.997$\pm$0.005) $=$ 9-class (0.997$\pm$0.005) $\approx$ binary (1.000$\pm$0.000)}
110	\vspace{1pt}
111	
112	\paragraph{Domain exposure is the primary mechanism.}
113	MLM bridges $\sim$60\,pp from vanilla (0.312$\pm$0.026 $\to$ 0.914$\pm$0.115) without labels; this supports the DAPT interpretation~\citep{gururangan2020dontstop}. TF-IDF collapse on ActorAttack (0.261 vs.\ 9-class 0.972) confirms that domain-adapted representations capture features beyond lexical overlap.
114	All three classification-supervised variants converge to equivalent detection (F1 = 0.997--1.000); McNemar's ($p > 0.13$) and paired permutation tests ($p \geq 0.40$) provide descriptive evidence suggesting equivalence. Extended to $n$\,=\,10 seeds, TOST (margin = 5\,pp) confirms equivalence on DD ($p < 10^{-8}$, $d$\,=\,$-$0.14; Table~\ref{tab:tost_sensitivity}) and FITD ($p < 10^{-8}$, $d \approx 0$). An observed difficulty gradient emerges: template attacks show full equivalence ($d < 0.1$), while strategy-diverse ActorAttack retains moderate label sensitivity ($d$\,=\,0.44, $p$\,=\,0.183). Label quality and granularity are descriptively non-factors for detection.
115	Classification supervision is associated with 3--23$\times$ lower cross-seed variance over MLM on synthetic OOD (std 0.005 vs.\ 0.115 on DD; observed range across 3 seeds; formal variance ratio tests are not applicable at $n$=3; cross-seed ensemble yields marginal additional gains, Appendix~\ref{app:ensemble}). This stability benefit does not transfer to human-authored data, where classification-supervised variants exhibit the highest variance and pure MLM the lowest (Section~\ref{sec:human_data}).
116	Appendix~\ref{app:tsne} provides t-SNE visualizations confirming that domain-adapted variants produce tighter, more separable embedding clusters than the vanilla baseline.
117	
118	\paragraph{Domain specificity is marginal at full length but meaningful for early detection.}
119	Wikipedia MLM (0.904$\pm$0.115) nearly matches jailbreak-domain MLM at full length (1\,pp gap), though jailbreak-domain text provides an 8\,pp advantage at early prefixes ($K$=2: 0.993 vs.\ 0.911).
120	Perturbation analysis (Section~\ref{sec:perturbation}) reveals a sharper domain specificity effect: Wikipedia MLM degrades by $\sim$12\,pp under adversarial paraphrasing while jailbreak-domain MLM degrades by only 2.6\,pp.
121	
122	\paragraph{Misaligned supervision destabilizes generalization.}
123	Topic classification yields DD-Full F1 = 0.541$\pm$0.207; seed 123 falls \emph{below} vanilla (0.252 vs.\ 0.312). Despite using the same jailbreak-domain training data, topic classification performs worse than Wikipedia MLM (0.904$\pm$0.115), which uses out-of-domain text with no labels. A misaligned objective forces the encoder to allocate capacity to irrelevant features and actively destabilizes representations that MLM would preserve.
124	
125	\paragraph{Evidence hierarchy on strategy-diverse attacks.}
126	ActorAttack~\citep{ren2024actorattack} uses multi-persona steering across longer conversation structures and provides a more challenging OOD benchmark than DD.
127	The evidence hierarchy at full conversation length is:
128	
129	\noindent\hspace{0.5em}{\small TF-IDF (0.261) $\approx$ vanilla (0.258$\pm$0.000) $<$ topic (0.625$\pm$0.141) $<$ wiki-MLM (0.686$\pm$0.297) $<$ jb-MLM (0.893$\pm$0.080) $<$ scrambled (0.951$\pm$0.043) $\approx$ 9-class (0.972$\pm$0.026) $\approx$ binary (0.990$\pm$0.008)}
130	\vspace{1pt}
131	
132	TF-IDF collapses from 0.961 (DD) to 0.261 (ActorAttack, precision = 1.0, recall = 0.15). This gap shows that domain-adapted representations capture features beyond bag-of-words.
133	All classification-supervised variants converge to equivalent performance (0.951--0.990, max gap 3.9\,pp); this extends the DD finding. DAPT provides $\sim$71\,pp over both vanilla (0.258) and TF-IDF (0.261). Full per-prefix results and per-prefix error analysis in Appendix~\ref{sec:actorattack_full} and~\ref{app:aa_error}.
134	
135	\paragraph{Temporal modeling.}
136	Mean pooling matches BiGRU on both DD and ActorAttack (F1 gap $\leq$ 1\,pp, overlapping CIs; Appendix~\ref{app:temporal}).
137	Turn-order shuffling produces negligible change ($|\Delta| < 1$\,pp) across both DeBERTa-v3-base 9-class (DD $\Delta$\,=\,0.000, AA $\Delta$\,=\,$-$0.009, IID $\Delta$\,=\,0.000) and RoBERTa-large 9-class (DD $\Delta$\,=\,+0.001, AA $\Delta$\,=\,$-$0.007, IID $\Delta$\,=\,0.000); detection relies on per-turn representations rather than sequential patterns.
138	
139	%----------------------------------------------------------------------
140	\subsection{Cross-Encoder Validation}
141	\label{sec:cross_encoder}
142	
143	\begin{table}[t]
144	\centering
145	\small
146	\caption{Cross-encoder comparison on OOD Full (3-seed mean$\pm$std). DD = Deceptive Delight, AA = ActorAttack. Bold indicates best per encoder group.}
147	\label{tab:cross_encoder}
148	\resizebox{\columnwidth}{!}{%
149	\begin{tabular}{@{}lcc@{}}
150	\toprule
151	\textbf{Variant} & DD & AA \\
152	\midrule
153	\multicolumn{3}{l}{\textit{DeBERTa-v3-base (184M)}} \\[2pt]
154	Vanilla & .312$\pm$.026 & .258$\pm$.000 \\
155	MLM & .914$\pm$.115 & .893$\pm$.080 \\
156	9-class & \textbf{.997$\pm$.005} & \textbf{.972$\pm$.026} \\
157	\midrule
158	\multicolumn{3}{l}{\textit{RoBERTa-base (125M)}} \\[2pt]
159	Vanilla & .981$\pm$.026 & .466$\pm$.163 \\
160	MLM & .987$\pm$.018 & .730$\pm$.201 \\
161	9-class & \textbf{.994$\pm$.005} & \textbf{.939$\pm$.046} \\
162	\midrule
163	\multicolumn{3}{l}{\textit{RoBERTa-large (355M)}} \\[2pt]
164	Vanilla & .927$\pm$.036 & \textbf{1.000$\pm$.000} \\
165	MLM & .884$\pm$.065 & .874$\pm$.014 \\
166	9-class & \textbf{.987$\pm$.004} & .946$\pm$.057 \\
167	\bottomrule
168	\end{tabular}}
169	\end{table}
170	
171	To test whether the evidence hierarchy depends on encoder choice, we replicate vanilla, MLM, and 9-class on RoBERTa-base~\citep{liu2019roberta} (Table~\ref{tab:cross_encoder}).
172	On DD, RoBERTa-base vanilla already achieves 0.981$\pm$0.026 (vs.\ DeBERTa 0.312$\pm$0.026), so DAPT adds only 1.3\,pp. ActorAttack exposes this as DD's simplicity: RoBERTa-base vanilla collapses to 0.466$\pm$0.163, a 51.5\,pp drop, while domain-adapted variants recover (9-class: 0.939$\pm$0.046).
173	
174	RoBERTa-large (355M) reveals a capacity-DAPT interaction: its effect on ActorAttack reverses (vanilla 1.000 vs.\ 9-class 0.946), while smaller encoders require DAPT to bridge 47--71\,pp. All continued pretraining reduces ActorAttack performance for the largest encoder via representation drift (Table~\ref{tab:roberta_large_lr}), though classification DAPT partially compensates on DD (+6\,pp).
175	
176	Three encoder scales thus reveal a scale-dependent pattern for the \emph{difficulty threshold}: DeBERTa-v3-base requires adaptation for all attacks, RoBERTa-base only for complex ones, and RoBERTa-large for none (Section~\ref{sec:discussion}).
177	Classification supervision provides a consistent stability benefit across both base encoders (cross-seed variance: 0.005--0.046 vs.\ 0.026--0.201).
178	A BERT-base-uncased proxy (110M, matching DeepContext's encoder family) without adaptation achieves DD\,=\,0.318$\pm$0.031 and AA\,=\,0.275$\pm$0.027, comparable to vanilla DeBERTa-v3 (Appendix~\ref{app:bert_proxy}); cross-attack generalization is driven by DAPT rather than encoder architecture.
179	
180	%----------------------------------------------------------------------
181	\subsection{Mixed-LLM Training}
182	
183	All preceding experiments use single-source (Qwen3-8B) data. To test whether the evidence hierarchy transfers when training data mixes LLM sources, we train on 250 Qwen + 250 Llama-3.1-8B conversations (Table~\ref{tab:mixed_llm}).
184	Classification-based DAPT is the only variant that substantially outperforms vanilla: 9-class achieves DD OOD F1\,=\,0.818$\pm$0.096 (+53\,pp over vanilla 0.291$\pm$0.065), while MLM drops to vanilla level (0.289$\pm$0.101). On strategy-diverse ActorAttack, the advantage narrows (9-class 0.504$\pm$0.107 vs.\ vanilla 0.389$\pm$0.073, +11.5\,pp) with high seed variance; limited per-source volume (250 per LLM) likely constrains generalization to complex attacks. DD and FITD thus primarily validate the baseline rather than the method; ActorAttack, where lexical methods collapse (TF-IDF F1\,=\,0.261) and vanilla encoders fail (F1\,$\leq$\,0.389 across conditions), provides the discriminative evaluation axis.
185	Mixed-LLM training confirms that classification supervision generalizes across LLM sources where unsupervised pretraining does not; full results in Appendix~\ref{app:mixed_llm}.
186	
187	%----------------------------------------------------------------------
188	\subsection{Human Data Validation}
189	\label{sec:human_data}
190	
191	Since both training and OOD evaluation data are Qwen3-8B-generated, we validate on ToxicChat~\citep{lin2023toxicchat} (204 human-written jailbreak attempts + 204 benign conversations from real LMSYS interactions).
192	
193	\begin{table}[t]
194	\centering
195	\small
196	\caption{Human data validation on ToxicChat~\citep{lin2023toxicchat} (macro F1, 3-seed mean$\pm$std). Bold indicates best. Single-turn data from real LMSYS user interactions, independent of Qwen3-8B.}
197	\label{tab:human_data}
198	\begin{tabular}{@{}lc@{}}
199	\toprule
200	\textbf{Variant} & Macro F1 \\
201	\midrule
202	JB-MLM & \textbf{.837$\pm$.013} \\
203	Wiki-MLM & .791$\pm$.093 \\
204	Binary & .705$\pm$.072 \\
205	Scrambled & .616$\pm$.056 \\
206	9-class & .596$\pm$.087 \\
207	Topic & .496$\pm$.042 \\
208	\midrule
209	Vanilla & .413$\pm$.021 \\
210	\bottomrule
211	\end{tabular}
212	\end{table}
213	
214	All DAPT variants exceed vanilla by 18--42\,pp (Table~\ref{tab:human_data}): the adapted-vs.-vanilla gap is not a Qwen3-8B generation artifact, and domain exposure on synthetic jailbreak text transfers to human-written attacks.
215	
216	The ordering reverses: JB-MLM leads (0.837$\pm$0.013) while 9-class ranks lower (0.596$\pm$0.087; $p < 0.001$, non-overlapping CIs). ToxicChat is single-turn, so the classification head provides no advantage; validating the multi-turn hierarchy requires multi-turn human data.
217	
218	%----------------------------------------------------------------------
219	\subsection{Perturbation Analysis}
220	\label{sec:perturbation}
221	
222	Under adversarial paraphrasing (BERTScore 0.92), classification-supervised variants achieve zero degradation on IID and OOD DD (Table~\ref{tab:ood_perturbation}) while non-adapted models degrade by $\sim$12\,pp ($p < 0.001$); on ActorAttack, DAPT variants degrade ($\Delta$\,=\,$-$20.4\,pp) but maintain 52\,pp over vanilla (Appendix~\ref{sec:perturbation_full}).
223	
224	%----------------------------------------------------------------------
225	\subsection{Strategy Trajectory Analysis}
226	\label{sec:strategy}
227	
228	The 9-class taxonomy provides interpretable characterization of known attacks ($\kappa$=0.78, $n$=50; Appendix~\ref{sec:strategy_full}) but degrades to near-random on OOD ($\kappa$=0.126; Appendix~\ref{app:strategy_pred}). Its value is twofold: as ablation infrastructure (scrambled labels produce equivalent detection) and as an interpretability tool for known attacks; detection operates through domain-adapted \texttt{[CLS]} embeddings, not strategy accuracy.
229	
230	%----------------------------------------------------------------------
231	\subsection{Benign Distribution Shift}
232	\label{sec:benign_shift}
233	
234	All preceding OOD results use IID benign data. On WildChat benign conversations, 9-class FPR rises to 68.1\%; cross-LLM error decomposition confirms false positives on unfamiliar benign text drive the collapse (Appendix~\ref{app:wildchat_fpr},~\ref{app:cross_llm}).
235	Few-shot benign-only adaptation resolves this without target-domain attack data: 10 WildChat conversations reduce FPR to 0\%, and 25 OASST2 conversations reduce FPR to 1.0\% (Appendix~\ref{app:wildchat_fpr},~\ref{app:oasst2}); dual-OOD F1 drops 12--14\,pp without adaptation but recovers within 0.3\,pp (Appendix~\ref{app:dual_ood}).
236	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "832c25c4-698c-4af7-b43b-0b73d588c29b",
  "isSidechain": true,
  "promptId": "968750d3-8ea0-4a1a-a2c1-b6601657157c",
  "agentId": "a8daa86d1003cff17",
  "type": "user",
  "uuid": "e32f84fc-0f2d-4fda-825c-7d389760034b",
  "sourceToolAssistantUUID": "832c25c4-698c-4af7-b43b-0b73d588c29b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cc8c01a1-4471-49ec-97ac-eac0175f808e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-23T11:13:55.494Z_

Now let me read the appendix to find the specific sections you need:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e32f84fc-0f2d-4fda-825c-7d389760034b",
  "isSidechain": true,
  "agentId": "a8daa86d1003cff17",
  "requestId": "req_011CbKQJkQ9kBdBXdg1r2ck3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9b95c218-3ea0-46a5-9117-5a0644155ecf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cc8c01a1-4471-49ec-97ac-eac0175f808e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YECGTrPeh1KxNniaa2eTWX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 7907,
      "cache_read_input_tokens": 19494,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7907,
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

_source line 9 · 2026-05-23T11:13:56.342Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Nd5TToPQ7CfBYEooJDYui7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex",
  "limit": 3000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b95c218-3ea0-46a5-9117-5a0644155ecf",
  "isSidechain": true,
  "agentId": "a8daa86d1003cff17",
  "requestId": "req_011CbKQJkQ9kBdBXdg1r2ck3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "756e6c46-3f46-4752-925a-af987e56060b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cc8c01a1-4471-49ec-97ac-eac0175f808e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YECGTrPeh1KxNniaa2eTWX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 7907,
      "cache_read_input_tokens": 19494,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7907
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 128,
          "cache_read_input_tokens": 19494,
          "cache_creation_input_tokens": 7907,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7907,
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

_source line 10 · 2026-05-23T11:13:56.688Z_

<details><summary>↩ Tool result · `toolu_01Nd5TToPQ7CfBYEooJDYui7`</summary>

```text
1	% appendix.tex — Supplementary material
2	
3	\appendix
4	
5	\section{LLM-as-Judge Baseline}
6	\label{sec:llm_judge}
7	
8	\begin{table}[t]
9	\centering
10	\small
11	\caption{LLM-as-judge jailbreak detection. IID: binary F1 (Crescendo test set); OOD: macro F1 (DD = Deceptive Delight, AA = ActorAttack). GPT-5.5 F1 values exclude unparseable responses and represent upper bounds.}
12	\label{tab:llm_judge}
13	\begin{tabular}{@{}lcccr@{}}
14	\toprule
15	\textbf{Method} & DD & AA & IID & Unparse. \\
16	\midrule
17	\multicolumn{5}{l}{\textit{Zero-shot}} \\[2pt]
18	GPT-5.5 & -- & -- & .383 & 30--47\% \\
19	Qwen3-8B & .244 & .244 & .100 & 0\% \\
20	\midrule
21	\multicolumn{5}{l}{\textit{3-shot}} \\[2pt]
22	Qwen3-8B & .566 & .652 & -- & 0\% \\
23	\midrule
24	\multicolumn{5}{l}{\textit{Trained classifier}} \\[2pt]
25	9-class (ours) & \textbf{.994} & \textbf{.972} & \textbf{1.000} & 0\% \\
26	\bottomrule
27	\end{tabular}
28	\end{table}
29	
30	Table~\ref{tab:llm_judge} reports LLM-as-judge performance on IID and OOD data.
31	On IID Crescendo, GPT-5.5 achieves precision of 1.0 at all turn prefixes but recall ranges from only 0.105 to 0.290, resulting in F1 = 0.383 on full conversations; 30--47\% of responses are unparseable.
32	Qwen3-8B performs worse (IID F1 = 0.100).
33	On OOD data, zero-shot Qwen3-8B achieves macro F1 = 0.244 on both DD and ActorAttack by predicting nearly all conversations as benign.
34	Even with 3-shot prompting, Qwen3-8B reaches only 0.566 (DD) and 0.652 (AA), while DisPeD maintains macro F1 $\geq$ 0.972.
35	The poor performance of content-level reasoning on unseen attack families underscores the necessity of trained classifiers with domain-adapted representations.
36	
37	\section{Full Cross-Attack Results by Prefix}
38	\label{sec:full_prefix}
39	
40	\begin{table*}[t]
41	\centering
42	\small
43	\caption{Full cross-attack generalization results (F1) at all prefix lengths. 3-seed mean$\pm$std where available. ``--'' indicates insufficient conversation length for that prefix (FITD conversations contain 2--3 turns).}
44	\label{tab:full_prefix}
45	\begin{tabular}{@{}lccccc@{}}
46	\toprule
47	\textbf{Method} & $K$=1 & $K$=2 & $K$=3 & $K$=5 & Full \\
48	\midrule
49	\multicolumn{6}{l}{\textit{IID (Crescendo)}} \\[2pt]
50	9-class (ours) & 1.000$\pm$.000 & 1.000$\pm$.000 & 1.000$\pm$.000 & 1.000$\pm$.000 & 1.000$\pm$.000 \\
51	MLM-only & .960 & .974 & .987 & 1.000 & 1.000 \\
52	Vanilla DeBERTa & .968$\pm$.033 & .978$\pm$.016 & .987$\pm$.000 & .982$\pm$.014 & 1.000$\pm$.000 \\
53	TF-IDF LR & 1.000 & 1.000 & 1.000 & 1.000 & 1.000 \\
54	\midrule
55	\multicolumn{6}{l}{\textit{OOD (Deceptive Delight)}} \\[2pt]
56	9-class (ours) & .990$\pm$.013 & .981$\pm$.013 & .972$\pm$.026 & .997$\pm$.005 & .994$\pm$.005 \\
57	Binary & .994$\pm$.009 & .994$\pm$.009 & .984$\pm$.008 & 1.000$\pm$.000 & 1.000$\pm$.000 \\
58	Scrambled & .997$\pm$.005 & .981$\pm$.026 & .975$\pm$.029 & .997$\pm$.005 & .994$\pm$.005 \\
59	MLM-only & .973$\pm$.019 & .993$\pm$.009 & .997$\pm$.005 & .997$\pm$.005 & .914$\pm$.115 \\
60	Vanilla DeBERTa & .628$\pm$.038 & .479$\pm$.038 & .389$\pm$.027 & .351$\pm$.030 & .312$\pm$.026 \\
61	TF-IDF LR & 1.000 & 1.000 & .994 & 1.000 & .961 \\
62	\midrule
63	\multicolumn{6}{l}{\textit{OOD (FITD)}} \\[2pt]
64	9-class (ours) & 1.000$\pm$.000 & 1.000$\pm$.000 & -- & -- & 1.000$\pm$.000 \\
65	Vanilla DeBERTa & .954$\pm$.039 & .952$\pm$.061 & -- & -- & .994$\pm$.009 \\
66	TF-IDF LR & 1.000 & -- & -- & -- & 1.000 \\
67	\bottomrule
68	\end{tabular}
69	\end{table*}
70	
71	\section{ActorAttack Full Results}
72	\label{sec:actorattack_full}
73	
74	\begin{table*}[t]
75	\centering
76	\small
77	\caption{Full ActorAttack OOD results (F1) at all prefix lengths. 3-seed mean$\pm$std (Binary per-$K$ reports $n$=2; Full is 3-seed).}
78	\label{tab:actorattack_full}
79	\begin{tabular}{@{}lccccc@{}}
80	\toprule
81	\textbf{Method} & $K$=1 & $K$=2 & $K$=3 & $K$=5 & Full \\
82	\midrule
83	\multicolumn{6}{l}{\textit{DeBERTa-v3}} \\[2pt]
84	Binary & .788$\pm$.020 & \textbf{.935$\pm$.018} & \textbf{.976$\pm$.005} & \textbf{.995$\pm$.005} & \textbf{.990$\pm$.008} \\
85	9-class & .773$\pm$.041 & .855$\pm$.048 & .921$\pm$.046 & .966$\pm$.028 & .972$\pm$.026 \\
86	Scrambled & .652$\pm$.034 & .804$\pm$.053 & .854$\pm$.046 & .910$\pm$.052 & .951$\pm$.043 \\
87	MLM-only & .736$\pm$.150 & .909$\pm$.058 & .945$\pm$.039 & .929$\pm$.033 & .893$\pm$.080 \\
88	Wiki MLM & .656$\pm$.224 & .672$\pm$.252 & .693$\pm$.280 & .689$\pm$.285 & .686$\pm$.297 \\
89	Topic & .513$\pm$.077 & .580$\pm$.109 & .565$\pm$.100 & .615$\pm$.111 & .625$\pm$.141 \\
90	Vanilla & .337$\pm$.049 & .306$\pm$.026 & .284$\pm$.011 & .262$\pm$.006 & .258$\pm$.000 \\
91	TF-IDF LR & .633 & .730 & .571 & .242 & .261 \\
92	\midrule
93	\multicolumn{6}{l}{\textit{RoBERTa}} \\[2pt]
94	9-class & \textbf{.738$\pm$.033} & .805$\pm$.033 & .884$\pm$.066 & .925$\pm$.066 & .939$\pm$.046 \\
95	MLM & .633$\pm$.133 & .665$\pm$.150 & .713$\pm$.174 & .719$\pm$.184 & .730$\pm$.201 \\
96	Vanilla & .410$\pm$.126 & .425$\pm$.143 & .432$\pm$.144 & .466$\pm$.144 & .466$\pm$.163 \\
97	\bottomrule
98	\end{tabular}
99	\end{table*}
100	
101	Table~\ref{tab:actorattack_full} reveals three distinct prefix-length patterns. The 9-class model improves monotonically from $K$=1 to Full (+20\,pp), consistent with cumulative evidence accumulation across turns. Vanilla DeBERTa \emph{decreases} with more turns (0.337 at $K$=1 to 0.258 at Full), suggesting that additional attack turns push representations further into benign embedding regions. MLM peaks at $K$=3 (0.945) then declines to 0.893 at Full, indicating that unsupervised domain exposure captures early-turn patterns but is unstable under extended sequences.
102	
103	\subsection{Error Analysis}
104	\label{app:aa_error}
105	
106	Per-sample majority vote across 3 seeds yields 98.3\% accuracy on ActorAttack OOD (2 false negatives, 0 false positives). No sample is misclassified by all three seeds; all 7 seed-specific errors are false negatives concentrated in shorter conversations (3--6 turns). On these 7 error samples, vanilla achieves 0/3 correct votes per sample, while 9-class majority vote correctly classifies 5/7, confirming that domain adaptation provides robust per-sample coverage even where individual seeds fail.
107	
108	\section{Perturbation Robustness}
109	\label{sec:perturbation_full}
110	
111	\begin{table}[t]
112	\centering
113	\small
114	\caption{Perturbation behavior under adversarial paraphrasing on IID Crescendo ($n$=76). $\Delta$: F1 degradation (pp). Classification-supervised variants achieve zero degradation at full length; this pattern does not generalize to ActorAttack.}
115	\label{tab:perturbation}
116	\begin{tabular}{@{}lcccc@{}}
117	\toprule
118	\textbf{Method} & $\Delta$ Full & $\Delta$ $K$=1 & $\Delta$ $K$=2 & $\Delta$ $K$=3 \\
119	\midrule
120	9-class (ours) & \textbf{0.0} & \textbf{$-$2.6} & \textbf{0.0} & \textbf{0.0} \\
121	Scrambled & \textbf{0.0} & $-$5.3 & $-$2.6 & \textbf{0.0} \\
122	Binary & \textbf{0.0} & $-$9.2 & $-$2.6 & \textbf{0.0} \\
123	\midrule
124	TF-IDF LR & $-$1.3 & $-$9.6 & $-$4.1 & $-$1.3 \\
125	MLM-only & $-$2.6 & $-$9.2 & $-$4.0 & $-$4.0 \\
126	Topic (seed 42) & $-$4.0 & $-$2.7 & $-$2.7 & \textbf{0.0} \\
127	\midrule
128	Wikipedia MLM & $-$12.1 & $-$12.4 & $-$15.4 & $-$17.9 \\
129	Vanilla DeBERTa & $-$11.8 & $-$14.6 & $-$12.1 & $-$13.8 \\
130	\bottomrule
131	\end{tabular}
132	\end{table}
133	
134	Table~\ref{tab:perturbation} shows perturbation behavior on IID data.
135	Classification-supervised variants (9-class, binary, scrambled) achieve zero degradation at full conversation length regardless of label correctness.
136	Models without jailbreak-domain exposure (Wikipedia MLM, vanilla) degrade by $\sim$12\,pp.
137	McNemar's test finds no significant pairwise differences among classification-supervised variants (all $p > 0.13$), though with $\leq$7 discordant pairs, statistical power is limited.
138	
139	\begin{table}[t]
140	\centering
141	\small
142	\caption{Perturbation robustness on OOD Deceptive Delight ($n$=118). $\Delta$: F1 change (pp) from clean to paraphrased. 3-seed mean$\pm$std where available.}
143	\label{tab:ood_perturbation}
144	\begin{tabular}{@{}lcccc@{}}
145	\toprule
146	\textbf{Variant} & Clean Full & Pert.\ Full & $\Delta$ Full & $\Delta$ $K$=1 \\
147	\midrule
148	9-class & .994$\pm$.005 & 1.000$\pm$.000 & +0.6 & +0.6 \\
149	Binary & 1.000$\pm$.000 & 1.000$\pm$.000 & 0.0 & +0.6 \\
150	Scrambled & .994$\pm$.005 & 1.000$\pm$.000 & +0.6 & $-$0.3 \\
151	\midrule
152	JB MLM & .914$\pm$.115 & .941 & +2.7 & 0.0 \\
153	Wiki MLM$^{*}$ & .904$\pm$.115 & .872 & $-$3.3 & $-$3.2 \\
154	Vanilla$^{\dagger}$ & .312$\pm$.026 & .339$\pm$.055 & +2.7 & $-$6.8$\pm$1.1 \\
155	\bottomrule
156	\end{tabular}
157	\vspace{-2pt}
158	{\footnotesize $^{*}$Wiki MLM degradation is seed-driven: seed 42 accounts for $-$9.8\,pp; other seeds show 0.0\,pp change.\\$^{\dagger}$Vanilla $\Delta$ Full = +2.7\,pp reflects floor-effect noise (baseline 0.312, std 0.055), not meaningful improvement.}
159	\end{table}
160	
161	On OOD DD, the IID pattern replicates: classification-supervised variants show zero degradation while McNemar's test confirms 9-class vs.\ vanilla significance ($p < 0.001$, 49--78 discordant pairs).
162	On OOD ActorAttack, domain-adapted variants degrade substantially (9-class $\Delta$\,=\,$-$20.4$\pm$13.5\,pp, MLM $-$35.3\,pp), but perturbation narrows rather than closes the adapted vs.\ non-adapted gap: 9-class perturbed F1 = 0.768 vs.\ vanilla 0.248 (McNemar $p < 0.001$).
163	Domain specificity also manifests: Wikipedia MLM degrades by $\sim$12\,pp while jailbreak-domain MLM degrades by only 2.6\,pp.
164	
165	\section{Strategy Trajectory Analysis}
166	\label{sec:strategy_full}
167	
168	\begin{figure*}[t]
169	\centering
170	\includegraphics[width=\textwidth]{figures/paper/fig3_strategy_heatmap.pdf}
171	\caption{Persuasion strategy transition count matrices for three attack families, based on ground-truth intended strategy labels. Strategy labels validated on $n$=50 samples with a single annotator ($\kappa$=0.78); fine-grained trajectory patterns should be interpreted with this limitation. Crescendo exhibits broad coverage across all strategy categories, while FITD and DD concentrate transitions in smaller subsets. Row $i$, column $j$ counts transitions from strategy $i$ at turn $t$ to strategy $j$ at turn $t+1$.}
172	\label{fig:strategy_heatmap}
173	\end{figure*}
174	
175	Figure~\ref{fig:strategy_heatmap} shows transition count matrices for three attack families.
176	Crescendo conversations exhibit broad transition coverage across all nine strategy categories (1,818 total transitions), with the highest concentration in Role Assignment self-transitions (545); this reflects its gradual escalation design.
177	FITD conversations show a markedly sparser pattern (541 transitions), with Role$\to$Obfuscation (161) as the dominant transition, consistent with FITD's commitment-consistency exploitation~\citep{cialdini2001influence}.
178	DD conversations span 5 active source strategies (565 transitions), with Emotion$\to$Obfuscation (129) as the dominant transition, aligning with DD's design of embedding harmful content within emotionally engaging contexts~\citep{deceptivedelight2024}.
179	
180	\section{Centered CKA Heatmaps}
181	\label{sec:cka_heatmap}
182	
183	\begin{figure}[t]
184	\centering
185	\includegraphics[width=\columnwidth]{figures/paper/cka_heatmap.pdf}
186	\caption{Centered CKA similarity~\citep{kornblith2019cka} between encoder variants on IID and OOD data for DeBERTa-v3 and RoBERTa. Low off-diagonal values (vanilla vs.\ adapted variants) confirm that continued pretraining substantially reshapes representations; the MLM vs.\ 9-class block shows distinct geometries (CKA $\leq$ 0.2 on RoBERTa OOD).}
187	\label{fig:cka_heatmap}
188	\end{figure}
189	
190	\section{Embedding Space Visualization}
191	\label{app:tsne}
192	
193	Figure~\ref{fig:tsne} visualizes mean-pooled \texttt{[CLS]} embeddings via t-SNE for three representative variants (Vanilla, JB-MLM, 9-Class) on DD OOD and ActorAttack. Vanilla embeddings show dispersed jailbreak clusters with ambiguous decision boundaries, while domain-adapted variants (JB-MLM, 9-Class) produce tighter, more separable clusters. JB-MLM achieves the clearest bimodal separation on both evaluation sets, consistent with its superior detection performance.
194	
195	\begin{figure}[ht]
196	\centering
197	\includegraphics[width=\columnwidth]{figures/paper/embedding_tsne.pdf}
198	\caption{t-SNE visualization of mean-pooled \texttt{[CLS]} embeddings (perplexity=30) for Vanilla, JB-MLM, and 9-Class variants on DD OOD and ActorAttack (118 samples each; blue=benign, red=jailbreak).}
199	\label{fig:tsne}
200	\end{figure}
201	
202	\section{Cross-LLM Validation}
203	\label{app:cross_llm}
204	
205	\begin{table}[ht]
206	\centering
207	\footnotesize
208	\caption{Cross-LLM validation (F1, full conversation). All models are trained on Qwen3-8B data; conditions vary the source of jailbreak (JB) and benign (ben.) conversations at inference. Values are evaluated under a matched 50-sample subset protocol and differ from Table~\ref{tab:evidence_hierarchy}, which uses the full evaluation set.}
209	\label{tab:cross_llm}
210	\begin{tabular}{@{}lcccccc@{}}
211	\toprule
212	& \multicolumn{3}{c}{\textit{DD Full}} & \multicolumn{3}{c}{\textit{AA Full}} \\
213	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
214	\textbf{Condition} & Van. & MLM & 9-cl. & Van. & MLM & 9-cl. \\
215	\midrule
216	Qwen JB + Qwen ben. & .312 & .914 & .997 & .258 & .893 & .972 \\
217	Llama JB + Llama ben. & .261 & .282 & .433 & .261 & .368 & .321 \\
218	Llama JB + Qwen ben. & .302 & .778$^{*}$ & 1.000 & .302 & .903 & .801 \\
219	\bottomrule
220	\end{tabular}
221	\vspace{-2pt}
222	{\footnotesize $^{*}$High seed variance (std = 0.306): seed 456 outlier (F1 = 0.345); remaining two seeds achieve F1 $\geq$ 0.97.}
223	\end{table}
224	
225	Table~\ref{tab:cross_llm} shows three inference conditions. When both jailbreak and benign text come from Llama (row~2), all variants collapse (F1 = 0.26--0.43), but this conflates two sources of distribution shift: unfamiliar jailbreak patterns and unfamiliar benign text. Row~3 isolates jailbreak transferability by pairing Llama jailbreaks with the original Qwen benign distribution. Under this condition, 9-class recovers to F1 = 1.000 on DD and 0.801 on ActorAttack, and JB-MLM reaches 0.903 on ActorAttack. The contrast between rows~2 and~3 shows that the dominant failure mode in row~2 is benign distribution mismatch (false positives from unfamiliar benign text), not inability to recognize cross-LLM jailbreak patterns. Vanilla remains at 0.26--0.31 across all conditions, further confirming that encoders without DAPT lack OOD detection capability regardless of the LLM source. The residual degradation on ActorAttack (0.801 vs.\ 0.972) reflects genuine cross-LLM variation in structurally complex attack patterns.
226	
227	\begin{table}[ht]
228	\centering
229	\footnotesize
230	\caption{Error decomposition for DD Full cross-LLM conditions (matched 50-sample subsets). TP rate is identical across benign conditions; the F1 collapse in the Llama-only condition (Table~\ref{tab:cross_llm}, row~2) is driven entirely by false positives on unfamiliar benign text.}
231	\label{tab:cross_llm_error}
232	\begin{tabular}{@{}lccc@{}}
233	\toprule
234	\textbf{Metric} & Van. & MLM & 9-cl. \\
235	\midrule
236	TP rate (Llama JB) & 0.0\% & 68.0\% & 100.0\% \\
237	FP rate (Llama ben.) & 29.3\% & 88.0\% & 90.0\% \\
238	FP rate (Qwen ben.) & 0.0\% & 0.9\% & 0.0\% \\
239	\bottomrule
240	\end{tabular}
241	\end{table}
242	
243	Table~\ref{tab:cross_llm_error} decomposes DD Full F1 into true positive and false positive rates. TP rates are identical regardless of the benign source: domain-adapted models detect Llama-generated jailbreaks at the same rate whether evaluated against Qwen or Llama benign text. The F1 collapse in the full Llama condition (Table~\ref{tab:cross_llm}, row~2) is driven entirely by false positives on unfamiliar benign text (FP rate: 88--90\% on Llama vs.\ 0--0.9\% on Qwen for adapted variants). The model implicitly treats non-Qwen text style as a jailbreak indicator, a spurious correlation from single-LLM training data. This failure reflects a data diversity limitation, not a methodological one; mixed-LLM training (Table~\ref{tab:mixed_llm}) partially addresses this confound.
244	
245	\section{Mixed-LLM Training Results}
246	\label{app:mixed_llm}
247	
248	\begin{table}[ht]
249	\centering
250	\footnotesize
251	\caption{Mixed-LLM training (250 Qwen + 250 Llama conversations, 3-seed mean$\pm$std where available). ToxicChat evaluated on balanced set (408 conversations).}
252	\label{tab:mixed_llm}
253	\begin{tabular}{@{}lccccc@{}}
254	\toprule
255	\textbf{Variant} & Mixed & DD OOD & AA OOD & FITD OOD & ToxicChat \\
256	\midrule
257	9-class & \textbf{.996$\pm$.006} & \textbf{.818$\pm$.096} & \textbf{.504$\pm$.107} & \textbf{.997$\pm$.005} & \textbf{.550$\pm$.052} \\
258	MLM & .681$\pm$.226 & .289$\pm$.101 & .258$\pm$.075 & .679$\pm$.188 & .256$\pm$.053 \\
259	Vanilla & .802$\pm$.010 & .291$\pm$.065 & .389$\pm$.073 & .867$\pm$.022 & .356$\pm$.009 \\
260	\bottomrule
261	\end{tabular}
262	\end{table}
263	
264	Table~\ref{tab:mixed_llm} reports detection performance when training on a mixed corpus of Qwen3-8B and Llama-3.1-8B conversations. Classification-based DAPT (9-class) maintains the strongest DD OOD performance (0.818$\pm$0.096), outperforming both vanilla (0.291$\pm$0.065) and MLM (0.289$\pm$0.101) by 53\,pp. ActorAttack remains challenging under mixed-LLM conditions (9-class F1\,=\,0.504$\pm$0.107), suggesting structurally complex attacks require larger or more diverse training data. ToxicChat performance shows no significant improvement over single-source training (0.550$\pm$0.052 vs.\ 0.596$\pm$0.087; Section~\ref{sec:human_data}), consistent with ToxicChat being zero-shot single-turn transfer rather than a standard OOD benchmark.
265	
266	\section{Dataset Scale Validation}
267	\label{app:scale_validation}
268	
269	\begin{table}[ht]
270	\centering
271	\footnotesize
272	\caption{Dataset scale validation (1{,}000 Qwen conversations, 3-seed mean$\pm$std). IID results omitted due to train/test overlap (71\% of original test set present in expanded training data).}
273	\label{tab:scale_validation}
274	\begin{tabular}{@{}lcc@{}}
275	\toprule
276	\textbf{Variant} & DD OOD & AA OOD \\
277	\midrule
278	9-class & \textbf{.889$\pm$.041} & \textbf{.913$\pm$.041} \\
279	MLM & .338$\pm$.010 & .351$\pm$.018 \\
280	Vanilla & .326$\pm$.000 & .508$\pm$.085 \\
281	\bottomrule
282	\end{tabular}
283	\end{table}
284	
285	Table~\ref{tab:scale_validation} validates robustness to dataset scale by doubling the training corpus from 500 to 1{,}000 conversations with new topic seeds. The hierarchy 9-class $\gg$ MLM $\approx$ vanilla holds at 2$\times$ scale: classification-based DAPT maintains 40--56\,pp advantage over vanilla, while MLM provides no improvement over vanilla on either attack family (DD: 0.338 vs.\ 0.326; AA: 0.351 vs.\ 0.508).
286	
287	\section{RoBERTa-large DAPT Learning Rate Control}
288	
289	\begin{table}[ht]
290	\centering
291	\footnotesize
292	\caption{RoBERTa-large (355M) DAPT learning rate control on OOD Full (3-seed mean$\pm$std). Reducing the learning rate worsens both DD and AA, ruling out over-adaptation as the cause of the regression in Table~\ref{tab:cross_encoder}.}
293	\label{tab:roberta_large_lr}
294	\begin{tabular}{@{}lcc@{}}
295	\toprule
296	\textbf{Config} & DD Full & AA Full \\
297	\midrule
298	Vanilla (no DAPT) & .927$\pm$.036 & 1.000$\pm$.000 \\
299	9-class, LR=$2 \times 10^{-5}$ & .987$\pm$.004 & .946$\pm$.057 \\
300	9-class, LR=$1 \times 10^{-5}$ & .948$\pm$.034 & .781$\pm$.054 \\
301	\bottomrule
302	\end{tabular}
303	\end{table}
304	
305	Reducing the DAPT learning rate from $2 \times 10^{-5}$ to $1 \times 10^{-5}$ worsens both DD and AA performance, which rules out over-adaptation as the cause of the regression observed in Table~\ref{tab:cross_encoder}. An MLM-only variant (without classification) produces the same pattern (AA Full = 0.874$\pm$0.014); representation drift from continued pretraining, not classification-specific bias, is the underlying cause. Domain-adaptive fine-tuning narrows the representation space of a sufficiently large encoder and reduces its inherent OOD generalization ability.
306	
307	\section{TOST Equivalence Sensitivity Analysis}
308	
309	\begin{table}[ht]
310	\centering
311	\footnotesize
312	\caption{TOST equivalence test sensitivity to margin $\delta$ (scrambled vs.\ 9-class, 3-seed). $p$-values from two one-sided $t$-tests; $p < 0.05$ confirms equivalence within $\pm\delta$.}
313	\label{tab:tost_sensitivity}
314	\begin{tabular}{@{}lccc@{}}
315	\toprule
316	\textbf{Dataset} & $\delta$=5\,pp & $\delta$=3\,pp & $\delta$=2\,pp \\
317	\midrule
318	DD OOD & .006 \checkmark & .016 \checkmark & .035 \checkmark \\
319	ActorAttack & .290 & .428 & .507 \\
320	\bottomrule
321	\end{tabular}
322	\end{table}
323	
324	On DD, TOST confirms scrambled $\approx$ correct labels even at $\delta$=2\,pp ($p$=0.035), demonstrating that label correctness is not a detection factor; the DD equivalence conclusion is robust to margin choice. On ActorAttack, the mean gap is 2.1\,pp but TOST is underpowered (SE\,=\,0.045, $n$=3) to confirm formal equivalence at any tested margin; the variants are descriptively similar but formally inconclusive.
325	
326	\section{Partition Robustness and Topic Failure Analysis}
327	\label{app:random_partition}
328	\label{app:topic_failure}
329	
330	\subsection{Random Binary Partition Robustness}
331	
332	\begin{table}[ht]
333	\centering
334	\footnotesize
335	\caption{OOD F1 for 10 random binary partitions of the 9 strategy labels (each partition randomly assigns strategies to group A or B). All partitions use identical Stage-1 DAPT and Stage-2 GRU training; only the binary label mapping differs. Seed 42 (3 runs).}
336	\label{tab:random_partition}
337	\begin{tabular}{@{}lcccc@{}}
338	\toprule
339	\textbf{Partition} & \textbf{Group A} & \textbf{IID} & \textbf{DD OOD} & \textbf{AA OOD} \\
340	\midrule
341	0 & \{0,2,4,5,7\} & 1.000 & 1.000 & 1.000 \\
342	1 & \{1,3,5,6,8\} & 1.000 & 1.000 & 1.000 \\
343	2 & \{0,1,3,7,8\} & 1.000 & 1.000 & 1.000 \\
344	3 & \{2,4,5,6,7\} & 1.000 & 1.000 & 1.000 \\
345	4 & \{0,1,2,6,8\} & 1.000 & 1.000 & 1.000 \\
346	5 & \{0,3,4,7,8\} & 1.000 & 1.000 & 1.000 \\
347	6 & \{1,2,3,5,6\} & 1.000 & 1.000 & 1.000 \\
348	7 & \{1,4,6,7\}   & 1.000 & 1.000 & 0.636 \\
349	8 & \{0,2,3,4,8\} & 1.000 & 1.000 & 1.000 \\
350	9 & \{0,1,5,7,8\} & 1.000 & 1.000 & 1.000 \\
351	\midrule
352	Mean$\pm$Std &  & 1.000$\pm$.000 & 1.000$\pm$.000 & 0.964$\pm$.109 \\
353	\bottomrule
354	\end{tabular}
355	\end{table}
356	
357	All 10 partitions achieve perfect IID and DD OOD detection regardless of how the 9 strategy labels are split into two groups. On ActorAttack, 9/10 partitions achieve F1\,=\,1.000; the sole outlier (partition~7, AA F1\,=\,0.636) uses a 4/5 split that isolates a specific strategy cluster. The near-universal success confirms that domain-relevant binary classification---not specific label semantics---drives cross-attack generalization on template attacks. The AA outlier is consistent with the complexity-dependent boundary observed in Section~\ref{sec:decomposition}: structurally complex attacks are sensitive to specific partition choices while template attacks are not.
358	
359	\subsection{Topic Classification Failure Analysis}
360	
361	\begin{table}[ht]
362	\centering
363	\footnotesize
364	\caption{Per-turn Fisher ratio (mean across all dimensions) and silhouette score between jailbreak and benign turn embeddings (\texttt{[CLS]} representations). Higher values indicate greater per-turn separability.}
365	\label{tab:topic_failure}
366	\begin{tabular}{@{}llcc@{}}
367	\toprule
368	\textbf{Model} & \textbf{Dataset} & \textbf{Fisher (mean)} & \textbf{Silhouette} \\
369	\midrule
370	Vanilla  & IID test & 0.118 & 0.034 \\
371	Vanilla  & DD OOD  & 0.401 & 0.411 \\
372	Vanilla  & AA OOD  & 0.408 & 0.330 \\
373	\midrule
374	9-class DAPT & IID test & 0.073 & 0.048 \\
375	9-class DAPT & DD OOD  & 0.200 & 0.079 \\
376	9-class DAPT & AA OOD  & 0.832 & 0.301 \\
377	\midrule
378	Topic DAPT & IID test & 0.108 & 0.076 \\
379	Topic DAPT & DD OOD  & 0.653 & 0.274 \\
380	Topic DAPT & AA OOD  & 0.311 & 0.141 \\
381	\bottomrule
382	\end{tabular}
383	\end{table}
384	
385	Topic DAPT achieves \emph{higher} per-turn Fisher separability than 9-class DAPT on IID and DD (0.653 vs.\ 0.200 on DD) yet produces far worse conversation-level detection (F1\,=\,0.541 vs.\ 0.994). This rules out per-turn separability destruction as the failure mechanism. The 9-class model instead greatly expands the embedding space (centroid $L_2$ distance 7.5--27.6 vs.\ 0.9--1.1 for vanilla) while distributing both classes broadly, creating richer representation geometry that the downstream GRU exploits over the turn sequence. Topic classification teaches features that separate turns individually but are temporally inconsistent across a conversation---high per-turn separability does not guarantee that the GRU can learn a stable conversation-level decision boundary.
386	
387	\section{Reproducibility Details}
388	\label{sec:reproducibility}
389	
390	\paragraph{Stage-1 training.}
391	All variants use DeBERTa-v3-base (184M parameters) with learning rate $2 \times 10^{-5}$, AdamW optimizer ($\beta_1$=0.9, $\beta_2$=0.999, weight decay 0.01), linear warmup over the first 10\% of steps, batch size 16, and 4 epochs. MLM variants use 15\% random token masking. Training takes approximately 30 minutes per variant on a single NVIDIA A100 (40GB).
392	
393	\paragraph{Stage-2 training.}
394	The BiGRU has hidden dimension 256, 2 layers, and dropout 0.3 (bidirectional, so output dimension 512). The MLP classifier has layers $512 \to 256 \to 2$ with ReLU activation. Training uses learning rate $1 \times 10^{-3}$, Adam optimizer, batch size 32, and 20 epochs with early stopping (patience 5) on validation F1. Stage-2 training completes in under 5 minutes per variant.
395	
396	\paragraph{Data generation.}
397	Jailbreak conversations are generated using Qwen3-8B with attack-specific prompt templates. Crescendo conversations follow a 5--8 turn gradual escalation structure. FITD conversations use a 2--3 turn commitment-consistency structure. Deceptive Delight conversations embed harmful content within emotionally engaging 3--5 turn sequences. Benign conversations are generated with topic-anchored prompts across five domains (technology, health, finance, education, general) with matched turn counts.
398	
399	\paragraph{Strategy annotation.}
400	Each user turn is annotated by Qwen3-8B using a structured prompt that provides definitions and two examples for each of the nine strategy categories. The prompt instructs the model to output a single category label. We plan to release all generation and annotation prompts, the full dataset, and training code upon acceptance.
401	
402	\paragraph{Adversarial paraphrasing.}
403	The paraphrased test set is generated by instructing Qwen3-8B to rephrase each user turn while preserving the communicative intent. The resulting paraphrases have mean BERTScore 0.92 and mean lexical overlap 0.20 with the originals. These metrics confirm substantial surface-level variation.
404	
405	\paragraph{Cross-checkpoint variance.}
406	To disentangle Stage-1 from Stage-2 variance, we evaluate three independently trained 9-class DAPT checkpoints (seeds 42, 123, 456) with a fixed downstream BiGRU seed (42). Results: IID F1\,=\,1.000$\pm$0.000, DD OOD\,=\,0.926$\pm$0.026, AA OOD\,=\,0.935$\pm$0.013. Stage-1 training is stable (OOD std\,$\leq$\,2.6\,pp), confirming that the variance reported in the main paper is not dominated by Stage-1 initialization.
407	
408	\section{End-to-End Fine-Tuning Upper Bound}
409	\label{app:e2e}
410	
411	\begin{table}[ht]
412	\centering
413	\footnotesize
414	\caption{Frozen probing vs.\ end-to-end (E2E) fine-tuning for DeBERTa-v3-base 9-class (3-seed mean$\pm$std). E2E unfreezes the Stage-1 encoder during Stage-2 training. Frozen values use main-experiment checkpoints (matching Tables~\ref{tab:main_results}--\ref{tab:evidence_hierarchy}); Table~\ref{tab:frozen_verify} uses plan\_002 checkpoints, yielding higher frozen accuracy (DD\,=\,.997, AA\,=\,.972) and a narrower E2E gap ($\leq$2.5\,pp).}
415	\label{tab:e2e}
416	\begin{tabular}{@{}lccc@{}}
417	\toprule
418	\textbf{Config} & IID & DD OOD & AA OOD \\
419	\midrule
420	Frozen probing & 1.000$\pm$.000 & .994$\pm$.005 & .939$\pm$.047 \\
421	E2E fine-tuning & 1.000$\pm$.000 & 1.000$\pm$.000 & \textbf{.997$\pm$.005} \\
422	\midrule
423	$\Delta$ & .000 & +.006 & +.058 \\
424	\bottomrule
425	\end{tabular}
426	\end{table}
427	
428	End-to-end fine-tuning unfreezes the Stage-1 encoder during Stage-2 BiGRU training, allowing gradient flow through the full pipeline. On IID and OOD DD, the two configurations are indistinguishable; on structurally complex ActorAttack, E2E recovers +5.8\,pp. The modest gain confirms that frozen probing captures the vast majority of discriminative information encoded by Stage-1 DAPT, and that the remaining OOD gap in the frozen setting reflects downstream optimization constraints rather than missing representational capacity.
429	
430	\section{Real-World False Positive Rate}
431	\label{app:wildchat_fpr}
432	
433	\begin{table}[ht]
434	\centering
435	\footnotesize
436	\caption{False positive rate (\%) on 226 WildChat benign multi-turn conversations (GPT-3.5 users, avg 7.4 turns per conversation). All models trained on synthetic Qwen3-8B data (1{,}000-conversation scale). 3-seed mean$\pm$std.}
437	\label{tab:wildchat_fpr}
438	\begin{tabular}{@{}lcccc@{}}
439	\toprule
440	\textbf{Variant} & Seed 42 & Seed 123 & Seed 456 & Mean$\pm$Std \\
441	\midrule
442	9-class & 66.8 & 61.1 & 76.5 & 68.1$\pm$6.4 \\
443	MLM & 36.7 & 64.6 & 32.3 & 44.5$\pm$14.3 \\
444	Vanilla & 47.3 & 42.5 & 54.4 & 48.1$\pm$4.9 \\
445	\bottomrule
446	\end{tabular}
447	\end{table}
448	
449	Table~\ref{tab:wildchat_fpr} evaluates false positive rates on 226 WildChat benign multi-turn conversations from real GPT-3.5 users (avg 7.4 turns). All variants produce FPR far exceeding deployable thresholds: 9-class is worst at 68.1\%, followed by vanilla (48.1\%) and MLM (44.5\%). Domain adaptation \emph{increases} FPR relative to vanilla (+20\,pp for 9-class), indicating that continued pretraining amplifies dependence on the training benign distribution. This is consistent with the cross-LLM false positive spike (Table~\ref{tab:cross_llm_error}): models trained on synthetic Qwen3-8B benign text implicitly treat unfamiliar conversational styles as jailbreak indicators. High MLM seed variance (std\,=\,14.3\%) suggests that unsupervised pretraining is particularly unstable under benign distribution shift. Deployment requires per-domain benign calibration or mixed-source benign training data.
450	
451	\paragraph{Post-hoc calibration.}
452	ROC AUC\,=\,0.700$\pm$0.054 indicates insufficient discrimination between WildChat benign and jailbreak conversations at the representation level. At TPR$\geq$95\%, the optimal threshold still yields FPR\,=\,62.7\%, far above deployable levels. Temperature scaling cannot improve this trade-off, as ROC curves are invariant to monotonic score transforms. The AUC ceiling reflects genuine domain shift: WildChat benign and jailbreak representations overlap substantially, and no post-hoc calibration can overcome this; in-domain benign adaptation is required.
453	
454	\paragraph{Second benign source: OASST2.}
455	\label{app:oasst2}
456	
457	To test whether benign-side shift generalizes beyond WildChat, we evaluate on 200 benign multi-turn conversations from OpenAssistant OASST2~\citep{kopf2023openassistant}---a crowdsourced dataset of real human conversations, distinct from WildChat (GPT-3.5 user logs) in both authorship and topic distribution.
458	
459	\begin{table}[ht]
460	\centering
461	\footnotesize
462	\caption{OASST2 benign adaptation curve: FPR on 200 OASST2 benign conversations and OOD jailbreak detection F1 as a function of $N$ OASST2 conversations added to training. Seed 42. Compare WildChat (Table~\ref{tab:wildchat_fpr}): FPR reaches 0\% at $N$\,=\,10.}
463	\label{tab:oasst2_curve}
464	\begin{tabular}{@{}rccccc@{}}
465	\toprule
466	$N$ & FPR (\%) & IID F1 & DD F1 & AA F1 & FITD F1 \\
467	\midrule
468	0 & 57.5 & -- & -- & -- & -- \\
469	10 & 20.5 & 1.000 & 1.000 & 1.000 & 1.000 \\
470	25 & \textbf{1.5} & 1.000 & 1.000 & 0.953 & 1.000 \\
471	50 & \textbf{0.5} & 1.000 & 1.000 & 0.990 & 1.000 \\
472	\bottomrule
473	\end{tabular}
474	\end{table}
475	
476	Baseline FPR on OASST2 (57.5\%) is comparable to WildChat (68.1\%), confirming that benign-side shift is not source-specific but a general consequence of synthetic-only benign training. The adaptation curve follows the same pattern---monotonic FPR reduction with preserved OOD detection---but requires more samples: 25 conversations reduce FPR to 1.5\% (vs.\ 0\% at $N$\,=\,10 for WildChat), and 50 conversations reach 0.5\%. The slower convergence likely reflects greater distributional distance between crowdsourced OASST2 conversations and the synthetic training distribution compared to WildChat's GPT-3.5 user logs.
477	
478	\subsection{Estimated Dual-OOD Detection Performance}
479	\label{app:dual_ood}
480	
481	The OOD detection F1 reported in the main paper evaluates attack-side OOD with IID benign examples (FPR\,=\,0), providing an upper bound. To estimate performance when \emph{both} attack and benign inputs are OOD, we combine per-seed attack recall (from OOD evaluation) with per-seed benign FPR (from WildChat/OASST2 experiments), assuming independence between attack detection and benign false positives. For each seed, we compute binary detection F1 from the resulting TP, FP, FN counts on the OOD test composition (80 jailbreak + 38 benign).
482	
483	\begin{table}[ht]
484	\centering
485	\footnotesize
486	\caption{Estimated dual-OOD binary detection F1 under different benign conditions (3-seed mean$\pm$std). Attack recall held fixed from OOD evaluation; only benign FPR varies. IID row corresponds to the benign-IID upper bound (FPR\,=\,0).}
487	\label{tab:dual_ood}
488	\begin{tabular}{@{}lcc@{}}
489	\toprule
490	\textbf{Benign condition} & DD OOD F1 & AA OOD F1 \\
491	\midrule
492	IID (FPR\,=\,0) & .994$\pm$.009 & .981$\pm$.019 \\
493	WildChat, no adapt & .855$\pm$.020 & .842$\pm$.012 \\
494	OASST2, no adapt & .874$\pm$.009 & .861$\pm$.018 \\
495	WildChat + 10-shot & .994$\pm$.009 & .981$\pm$.019 \\
496	OASST2 + 25-shot & .991$\pm$.009 & .978$\pm$.018 \\
497	\bottomrule
498	\end{tabular}
499	\end{table}
500	
501	Without benign adaptation, dual-OOD F1 drops by 12--14\,pp (DD: $.994 \to .855$; AA: $.981 \to .842$), driven entirely by false positives on OOD benign inputs. After few-shot adaptation---10 WildChat or 25 OASST2 conversations---dual-OOD F1 recovers to within 0.3\,pp of the IID upper bound, confirming that the lightweight adaptation procedure (Section~\ref{sec:benign_shift}) effectively closes the benign distribution gap without compromising attack-side performance.
502	
503	\section{BERT-base Proxy Baseline}
504	\label{app:bert_proxy}
505	
506	\begin{table}[ht]
507	\centering
508	\footnotesize
509	\caption{BERT-base-uncased (110M) frozen probing without DAPT, matching DeepContext's encoder family~\citep{deepcontext2026}. 3-seed mean$\pm$std. DeBERTa-v3 results from Table~\ref{tab:cross_encoder} for comparison.}
510	\label{tab:bert_proxy}
511	\begin{tabular}{@{}lccc@{}}
512	\toprule
513	\textbf{Encoder} & IID & DD OOD & AA OOD \\
514	\midrule
515	BERT-base (110M), no DAPT & .996$\pm$.006 & .318$\pm$.031 & .275$\pm$.027 \\
516	DeBERTa-v3 (184M), no DAPT & 1.000$\pm$.000 & .312$\pm$.043 & .258$\pm$.000 \\
517	DeBERTa-v3 (184M), 9-class & 1.000$\pm$.000 & .994$\pm$.005 & .939$\pm$.047 \\
518	\bottomrule
519	\end{tabular}
520	\end{table}
521	
522	Table~\ref{tab:bert_proxy} compares BERT-base-uncased (110M parameters, matching DeepContext's encoder) against DeBERTa-v3-base (184M), both without domain-adaptive pretraining. The two vanilla encoders achieve comparable OOD performance (DD: 0.318 vs.\ 0.312; AA: 0.275 vs.\ 0.258), despite a 1.7$\times$ parameter difference and different pretraining procedures. Both collapse on OOD evaluation while 9-class DAPT recovers to 0.994 (DD) and 0.939 (AA). This confirms that cross-attack generalization is driven by domain adaptation, not encoder architecture or capacity at this scale.
523	
524	\section{Confidence Calibration}
525	\label{app:calibration}
526	
527	\begin{table}[ht]
528	\centering
529	\footnotesize
530	\caption{Expected calibration error (ECE, 10 bins) for 9-class and vanilla on IID and OOD evaluation (3-seed mean$\pm$std). Lower is better.}
531	\label{tab:calibration}
532	\begin{tabular}{@{}lccc@{}}
533	\toprule
534	\textbf{Variant} & IID & DD OOD & AA OOD \\
535	\midrule
536	9-class & $\approx$0.000 & 0.143$\pm$0.053 & 0.116$\pm$0.053 \\
537	Vanilla & 0.009$\pm$0.007 & 0.669$\pm$0.004 & 0.504$\pm$0.066 \\
538	\bottomrule
539	\end{tabular}
540	\end{table}
541	
542	The 9-class model achieves substantially lower ECE than vanilla on OOD data (0.12--0.14 vs.\ 0.50--0.67), indicating that domain adaptation improves not only discriminative performance but also confidence calibration. IID calibration is near-perfect for both variants. The residual OOD ECE (0.12--0.14) suggests that temperature scaling could further improve deployment reliability.
543	
544	\subsection{ToxicChat False Positive Confidence}
545	\label{app:confidence}
546	
547	On ToxicChat, 9-class false positives are overwhelmingly high-confidence: 70.2\% of majority-vote FPs exceed $p > 0.9$ (median 0.999), compared to 58.8\% for JB-MLM (median 0.933). Per-seed analysis is more extreme---94--98\% of single-model 9-class FPs are high-confidence (median 1.0), with the borderline fraction (25\%) in majority vote arising from cross-seed disagreement rather than individual model uncertainty. This confirms that the 9-class ToxicChat FPR reflects systematic feature misalignment---classification DAPT shifts benign text into the jailbreak region with high confidence---rather than boundary ambiguity.
548	
549	\section{Frozen Probing Verification}
550	\label{app:frozen_verify}
551	
552	\begin{table}[ht]
553	\centering
554	\footnotesize
555	\caption{Frozen probing vs.\ end-to-end (E2E) fine-tuning (3-seed mean$\pm$std). 9-class: plan\_002 checkpoints; MLM: plan\_017\_mlm\_control (matched training). Frozen probing trains only BiGRU+MLP on frozen DAPT embeddings.}
556	\label{tab:frozen_verify}
557	\begin{tabular}{@{}lcccc@{}}
558	\toprule
559	\textbf{Config} & IID & DD OOD & AA OOD & FITD OOD \\
560	\midrule
561	Frozen 9-class & 1.000$\pm$.000 & .997$\pm$.005 & .972$\pm$.026 & 1.000$\pm$.000 \\
562	Frozen MLM & .982$\pm$.016 & .993$\pm$.009 & .941$\pm$.037 & .987$\pm$.009 \\
563	E2E 9-class & 1.000$\pm$.000 & 1.000$\pm$.000 & .997$\pm$.005 & --- \\
564	\bottomrule
565	\end{tabular}
566	\end{table}
567	
568	Table~\ref{tab:frozen_verify} compares frozen probing across DAPT objectives and against end-to-end fine-tuning. On easy OOD (DD, FITD), frozen MLM and frozen 9-class representations perform comparably ($\Delta \leq 1.3$\,pp). On hard OOD (ActorAttack), 9-class retains a modest advantage (0.972 vs.\ 0.941, $\Delta$\,=\,3.1\,pp) with lower variance ($\sigma$\,=\,0.026 vs.\ 0.037). Both far exceed vanilla encoders ($\leq$0.318; Table~\ref{tab:bert_proxy}). The E2E advantage over frozen 9-class is $\leq$2.5\,pp, confirming that Stage-1 representation quality is the primary source of OOD generalization.
569	
570	A striking asymmetry emerges when comparing frozen probing to the full pipeline (Table~\ref{tab:evidence_hierarchy}): MLM frozen representations \emph{outperform} the full MLM pipeline on AA OOD (0.941 vs.\ 0.893), while 9-class frozen exactly matches its full pipeline (0.972 vs.\ 0.972). This indicates that MLM's cross-seed instability originates in Stage-2 BiGRU training rather than Stage-1 DAPT: the MLM encoder produces adequate representations that are then degraded by unstable downstream optimization. Classification DAPT, by contrast, produces representations that remain robust through Stage-2 training, explaining its consistently lower variance (Table~\ref{tab:evidence_hierarchy}).
571	
572	This two-level structure (DAPT vs.\ no-DAPT producing a representation quality leap of +70\,pp; classification vs.\ MLM DAPT producing a stability difference) is consistent with two further observations: $\lambda$=0 matches $\lambda > 0$ during E2E fine-tuning (Table~\ref{tab:lambda}), and mean pooling matches BiGRU under E2E (Table~\ref{tab:temporal}). Once DAPT representations are strong, downstream configuration details have minimal impact.
573	
574	\subsection{Single-Turn Truncation Analysis}
575	\label{app:truncated}
576	
577	To isolate whether the ToxicChat evidence-hierarchy reversal (Section~\ref{sec:discussion}) reflects multi-turn structural dependence, we truncate each synthetic test conversation to its last user turn and re-evaluate both 9-class and JB-MLM models (3-seed mean).
578	
579	\begin{table}[h]
580	\centering
581	\caption{Full-conversation vs.\ last-turn-only F1 (3-seed mean). Truncation widens the 9-class advantage, ruling out multi-turn structure as the driver of the ToxicChat reversal.}
582	\label{tab:truncated}
583	\begin{tabular}{@{}llcc@{}}
584	\toprule
585	\textbf{Dataset} & \textbf{Mode} & \textbf{9-class} & \textbf{JB-MLM} \\
586	\midrule
587	IID & Full & 1.000 & .983 \\
588	IID & Last turn & .991 & .894 \\
589	\midrule
590	DD OOD & Full & .997 & .993 \\
591	DD OOD & Last turn & .942 & .924 \\
592	\midrule
593	AA OOD & Full & .972 & .941 \\
594	AA OOD & Last turn & .978 & .927 \\
595	\midrule
596	FITD OOD & Full & 1.000 & .987 \\
597	FITD OOD & Last turn & 1.000 & .927 \\
598	\bottomrule
599	\end{tabular}
600	\vspace{-2pt}
601	{\footnotesize Mean $\Delta$ (9-class $-$ MLM): Full +1.6\,pp, Last turn +6.0\,pp. 9-class advantage widens under truncation across all families, indicating the reversal on ToxicChat is driven by distributional differences between synthetic and human text, not by multi-turn structural dependence.}
602	\end{table}
603	
604	\paragraph{Representation geometry analysis.}
605	\label{app:representation}
606	
607	To characterize the mechanism behind classification DAPT's robustness, we analyze Stage-1 representations across all seven DeBERTa-v3-base variants (seed 42). We extract \texttt{[CLS]} embeddings from 150 test conversations (50 IID + 50 DD OOD + 50 AA OOD) and compute three metrics.
608	
609	\begin{table}[ht]
610	\centering
611	\footnotesize
612	\caption{Representation geometry and class separability across Stage-1 variants. PR: participation ratio (effective dimensionality of the embedding space). Fisher ratio: inter-class distance$^2$ / sum of intra-class variances. Weight $\Delta$: L2 distance from pretrained weights (relative to pretrained norm).}
613	\label{tab:representation}
614	\begin{tabular}{@{}lccc@{}}
615	\toprule
616	\textbf{Variant} & \textbf{PR} & \textbf{Fisher} & \textbf{Wt.\ $\Delta$ (\%)} \\
617	\midrule
618	Vanilla & 31.9 & $<$0.001 & 0.000 \\
619	Wiki-MLM & 25.0 & $<$0.001 & 0.221 \\
620	JB-MLM & 24.6 & $<$0.001 & 0.256 \\
621	Topic & 14.5 & 0.012 & 0.371 \\
622	Scrambled & 7.8 & 2.60 & 0.283 \\
623	9-class & 9.4 & 4.47 & 0.303 \\
624	Binary & 3.7 & 19.7 & 0.239 \\
625	\bottomrule
626	\end{tabular}
627	\end{table}
628	
629	Classification variants compress representations into 2--9 effective dimensions (vs.\ 25--32 for MLM/vanilla) while increasing Fisher ratio by 3--5 orders of magnitude. Weight distances from pretrained are comparable across all variants ($\sim$0.2--0.4\%), indicating that the mechanism is representational restructuring rather than parameter-space regularization. Scrambled labels produce similar compression (PR\,=\,7.8, Fisher\,=\,2.6), confirming that the classification objective structure---not label semantics---drives discriminative compression.
630	
631	\paragraph{Layer-wise localization.}
632	\label{app:layerwise}
633	
634	To determine \emph{where} discriminative compression occurs, we compute PR and Fisher ratio at every DeBERTa-v3-base layer (0--12) for four variants (9-class, scrambled, JB-MLM, vanilla) using the same 236-sample evaluation set (seed 42).
635	
636	\begin{figure}[ht]
637	\centering
638	\includegraphics[width=\columnwidth]{figures/paper/fig_layerwise_representation.pdf}
639	\caption{Layer-wise representation analysis. (a)~Participation ratio: classification variants (9-class, scrambled) show sharp dimensional collapse at layers 9--10 (PR\,$\approx$\,1.5--2.9) while vanilla/JB-MLM maintain high dimensionality (PR\,$\approx$\,7--10). (b)~Fisher ratio (log scale): class separability diverges from layer 8, with 9-class peaking at 10.9 (layer 10) vs.\ vanilla 0.73 (15$\times$).}
640	\label{fig:layerwise}
641	\end{figure}
642	
643	Layers 0--7 show no systematic divergence across variants (Fisher\,$<$\,2.1 for all; PR tracks similar oscillation patterns), consistent with \citet{maennel2020random}'s finding that early layers learn label-independent features. From layer 8 onward, classification-supervised variants diverge sharply: 9-class Fisher rises from 3.2 (layer 8) to 10.9 (layer 10, peak), while vanilla remains below 1.5 throughout. Simultaneously, 9-class PR drops from 3.4 to 1.5 at layer 10---a 6.6$\times$ compression relative to vanilla (PR\,=\,9.7). JB-MLM tracks vanilla across all layers (Fisher\,$\leq$\,3.3, PR\,$\geq$\,1.4), confirming that MLM does not induce discriminative restructuring. Scrambled labels exhibit the same late-layer pattern (Fisher peaks at 7.9, layer 12; PR drops to 1.5, layer 12), reinforcing that any classification signal---regardless of label semantics---triggers late-layer compression.
644	
645	\paragraph{Discriminative subspace probe.}
646	\label{app:discriminative_probe}
647	
648	To test whether the compressed subspace is \emph{sufficient} for OOD detection, we project layer-10 \texttt{[CLS]} representations onto the top-$k$ SVD components and train a logistic regression probe (3 seeds, sklearn default). Controls: random $k$-dimensional projections (10 random bases, mean reported) and vanilla/MLM models under identical projection.
649	
650	\begin{table}[ht]
651	\centering
652	\footnotesize
653	\caption{Discriminative subspace probe: OOD F1 when projecting layer-10 representations onto top-$k$ SVD components vs.\ random $k$-dimensional projections. 9-class top-3 achieves perfect AA detection with 3/768 dimensions; MLM fails even with all 768.}
654	\label{tab:discriminative_probe}
655	\begin{tabular}{@{}llccc@{}}
656	\toprule
657	\textbf{Model} & \textbf{Projection} & DD & AA & FITD \\
658	\midrule
659	9-class & top-3 & 1.000 & \textbf{1.000} & 1.000 \\
660	9-class & top-5 & 1.000 & 1.000 & 1.000 \\
661	9-class & random-3 & 1.000 & 0.928$\pm$.129 & 1.000 \\
662	9-class & random-5 & 1.000 & 0.952 & 1.000 \\
663	9-class & full-768 & 1.000 & 1.000 & 1.000 \\
664	\midrule
665	scrambled & top-3 & 1.000 & 0.962 & 1.000 \\
666	scrambled & random-3 & 0.981 & 0.766 & 0.987 \\
667	\midrule
668	JB-MLM & top-3 & 1.000 & 0.618 & 1.000 \\
669	JB-MLM & full-768 & 1.000 & 0.636 & 1.000 \\
670	JB-MLM & random-5 & 0.685 & 0.584 & 0.744 \\
671	\bottomrule
672	\end{tabular}
673	\end{table}
674	
675	Three findings establish a link between compression and generalization (Table~\ref{tab:discriminative_probe}). First, 9-class top-3 achieves perfect ActorAttack detection (F1\,=\,1.000) using only 3 of 768 dimensions---all discriminative information resides in the compressed subspace. Second, random 3-dimensional projections degrade to 0.928 on AA, confirming that the specific SVD directions matter. Third, JB-MLM reaches only 0.636 on AA even with all 768 dimensions, demonstrating that without classification-induced compression, the representation lacks the structure needed for cross-attack generalization. DD and FITD are near-ceiling for all models, making ActorAttack the critical test.
676	SVD directions computed on IID training data only (without OOD test exposure) yield equal or higher F1 than all-data SVD (AA: 0.947 vs.\ 0.904), confirming the subspace is not an artifact of test-set leakage.
677	
678	\paragraph{SVD necessity ablation.}
679	\label{app:svd_necessity}
680	
681	The probe above establishes \emph{sufficiency}: 3 SVD dimensions carry enough information. To test \emph{necessity}, we project \emph{out} the top-3 SVD directions from full 768-dimensional 9-class \texttt{[CLS]} embeddings and re-run BiGRU classification on OOD data (3 seeds). A random-3 removal control verifies that the effect is specific to the discriminative subspace. The top-3 directions explain 89.8\% of training-set variance.
682	
683	\begin{table}[ht]
684	\centering
685	\footnotesize
686	\caption{SVD necessity ablation: OOD F1 after projecting out top-3 vs.\ random-3 SVD directions from 9-class layer-10 embeddings (3-seed mean$\pm$std).}
687	\label{tab:svd_necessity}
688	\begin{tabular}{@{}lccc@{}}
689	\toprule
690	\textbf{Condition} & DD OOD & FITD OOD & AA OOD \\
691	\midrule
692	Original 768-dim & 1.000$\pm$.000 & 1.000$\pm$.000 & .994$\pm$.005 \\
693	Remove top-3 SVD & .831$\pm$.064 & 1.000$\pm$.000 & .938$\pm$.011 \\
694	Remove random-3 & 1.000$\pm$.000 & 1.000$\pm$.000 & .994$\pm$.005 \\
695	\bottomrule
696	\end{tabular}
697	\end{table}
698	
699	Removing top-3 SVD directions degrades DD detection by 17\,pp (F1: $1.0 \to 0.831$) and AA by 5.6\,pp ($0.994 \to 0.938$), while random-3 removal has zero effect. FITD is unaffected by either ablation, indicating its discriminative information is more distributed. Combined with the sufficiency result (Table~\ref{tab:discriminative_probe}), the top-3 SVD directions are both sufficient and necessary for DD detection, sufficient but partially redundant for AA, and sufficient but not necessary for FITD.
700	
701	\section{Temporal Aggregation Comparison}
702	\label{app:temporal}
703	
704	\begin{table}[ht]
705	\centering
706	\footnotesize
707	\caption{Temporal aggregation comparison: mean pooling vs.\ BiGRU under frozen and end-to-end (E2E) settings (3-seed mean$\pm$std). Plan\_002 9-class checkpoints.}
708	\label{tab:temporal}
709	\begin{tabular}{@{}llccc@{}}
710	\toprule
711	\textbf{Setting} & \textbf{Aggregator} & DD OOD & AA OOD \\
712	\midrule
713	\multirow{2}{*}{Frozen} & BiGRU & .997$\pm$.005 & .972$\pm$.026 \\
714	& Mean pooling & .991$\pm$.013 & .962$\pm$.015 \\
715	\midrule
716	\multirow{2}{*}{E2E} & BiGRU & 1.000$\pm$.000 & .997$\pm$.005 \\
717	& Mean pooling & 1.000$\pm$.000 & 1.000$\pm$.000 \\
718	\bottomrule
719	\end{tabular}
720	\end{table}
721	
722	Table~\ref{tab:temporal} compares BiGRU and mean pooling under both frozen and E2E settings. Under frozen probing (the main paper's pipeline), BiGRU provides a marginal advantage on ActorAttack (+1.0\,pp) with overlapping confidence intervals, consistent with the main text finding that temporal order is not a core detection factor ($|\Delta| < 1$\,pp under turn shuffling; Section~\ref{sec:decomposition}). Under E2E fine-tuning, the difference vanishes entirely: mean pooling saturates all benchmarks at F1\,=\,1.000. The choice of frozen BiGRU in the main pipeline reflects a design trade-off: it enables representation-level analysis (CKA, t-SNE) that E2E would confound, while sacrificing $\leq$1\,pp on the hardest OOD set.
723	
724	\section{Length Stratification Analysis}
725	\label{app:length}
726	
727	\begin{table}[ht]
728	\centering
729	\footnotesize
730	\caption{Jailbreak recall by conversation length bin on OOD evaluation (3-seed majority vote). Benign conversations span 12--20 turns; jailbreak conversations span 3--10 turns.}
731	\label{tab:length}
732	\begin{tabular}{@{}llccc@{}}
733	\toprule
734	\textbf{Dataset} & \textbf{Variant} & 1--3 turns & 4--6 turns & 7--10 turns \\
735	\midrule
736	\multirow{2}{*}{DD OOD} & 9-class & --- & 100.0\% & 99.4\% \\
737	& Vanilla & --- & $\leq$2.6\% & $\leq$1.7\% \\
738	\midrule
739	\multirow{2}{*}{AA OOD} & 9-class & 93.3\% & 95.6\% & 100.0\% \\
740	& Vanilla & 0.0\% & $\leq$2.6\% & 0.0\% \\
741	\bottomrule
742	\end{tabular}
743	\end{table}
744	
745	Table~\ref{tab:length} stratifies jailbreak recall by conversation length. The 9-class model shows no systematic degradation: ActorAttack recall increases monotonically from 93.3\% (1--3 turns) to 100\% (7--10 turns), and DD recall is near-perfect across all bins.
746	
747	\paragraph{Length confound.}
748	Benign conversations (12--20 turns) and jailbreak conversations (3--10 turns) have zero length overlap in the OOD evaluation sets, raising the concern that the model discriminates by conversation length rather than content. Three observations argue against this interpretation:
749	(1)~Vanilla DeBERTa has access to identical length information via the BiGRU but achieves recall $\leq$2.6\% across all bins; length alone is insufficient without domain-adapted representations.
750	(2)~At prefix $K$=1, where all conversations are length-equalized, 9-class still achieves F1\,=\,0.773$\pm$0.041 on ActorAttack (Table~\ref{tab:actorattack_full}), demonstrating content-based detection independent of length.
751	(3)~The model is trained on IID data (Crescendo) and cannot learn OOD-specific length distributions; generalization to unseen length patterns must rely on content features that transfer across attack families.
752	
753	\paragraph{Direct empirical verification.}
754	\label{app:length_independence}
755	
756	\begin{table}[ht]
757	\centering
758	\footnotesize
759	\caption{Turn-count independence verification (9-class, plan\_002 checkpoints, 3 seeds). Part~A: FPR on test benign truncated to $K$ user turns (all seeds FPR\,=\,0). Part~B: WildChat FPR by turn-count bucket (mean$\pm$std). Part~C: jailbreak detection (F1) after padding with benign turns to 15+ total turns (mean$\pm$std where available).}
760	\label{tab:length_independence}
761	\begin{tabular}{@{}llcc@{}}
762	\toprule
763	& \textbf{Condition} & \textbf{FPR / F1} & $n$ \\
764	\midrule
765	\multicolumn{4}{l}{\textit{Part A: Benign truncation (test set)}} \\[2pt]
766	& Original (12--20 turns) & FPR = .000 & 38 \\
767	& Truncated $K$=3 & FPR = .000 & 38 \\
768	& Truncated $K$=5 & FPR = .000 & 38 \\
769	& Truncated $K$=8 & FPR = .000 & 38 \\
770	& Truncated $K$=10$^{*}$ & FPR = .000 & 38 \\
771	\midrule
772	\multicolumn{4}{l}{\textit{Part B: WildChat FPR by turn count}} \\[2pt]
773	& Short (3--10 turns) & FPR = .770$\pm$.105 & 196 \\
774	& Medium (11--15 turns) & FPR = .942$\pm$.054 & 23 \\
775	& Long (16+ turns) & FPR = .857$\pm$.117 & 7 \\
776	\midrule
777	\multicolumn{4}{l}{\textit{Part C: Jailbreak padding to 15+ turns}} \\[2pt]
778	& DD original & F1 = .996 & 80 \\
779	& DD padded & F1 = .971 ($\Delta$=$-$2.5\,pp) & 80 \\
780	& AA original & F1 = .963 & 80 \\
781	& AA padded & F1 = .383$\pm$.261 ($\Delta$=$-$57.9\,pp) & 80 \\
782	\bottomrule
783	\end{tabular}
784	\vspace{-2pt}
785	{\footnotesize $^{*}$$K$=10 did not truncate any conversation (test benign max $\sim$8 user turns).}
786	\end{table}
787	
788	Truncating benign conversations to match jailbreak turn counts (Part~A) produces zero false positives across all truncation levels and all 3 seeds, directly confirming that the model does not use conversation length as a detection shortcut. $K$=3 and $K$=5 are the effective control conditions where all 38 conversations were truncated; $K$=10 exceeds the maximum test benign length and serves as a no-op control.
789	
790	WildChat FPR by turn count (Part~B) provides complementary evidence: short conversations (3--10 turns, $n$=196) have \emph{lower} FPR than medium-length ones (11--15 turns, $n$=23), inconsistent with a ``short\,=\,jailbreak'' shortcut. Medium and long buckets have limited sample sizes and should be interpreted as directional evidence only.
791	
792	Padding jailbreak conversations with benign turns (Part~C) reveals an asymmetry: DD detection is resilient ($\Delta$=$-$2.5\,pp), but ActorAttack collapses ($\Delta$=$-$57.9\,pp). Padding experiments append benign turns \emph{after} the complete attack sequence; in practice, adversaries would not dilute their own successful attacks. The collapse nonetheless exposes BiGRU temporal aggregation as vulnerable to attention dilution on subtle attack signals, a limitation discussed in Section~\ref{sec:limitations}.
793	
794	\section{Inference Efficiency}
795	\label{app:efficiency}
796	
797	\begin{table}[ht]
798	\centering
799	\footnotesize
800	\caption{Inference efficiency comparison. DeBERTa+BiGRU and TF-IDF+LR measured on IID test (76 conversations, avg 8.3 turns, single A100). LLM latency from separate OOD evaluation (118 conversations; exp10); cross-condition comparison is indicative only.}
801	\label{tab:efficiency}
802	\begin{tabular}{@{}lrcr@{}}
803	\toprule
804	\textbf{Method} & Latency (ms) & Params & VRAM \\
805	\midrule
806	TF-IDF+LR & 0.43$\pm$0.05 & $\sim$10K & CPU \\
807	DeBERTa+BiGRU (ours) & 12.1$\pm$1.2 & 186.7M & 862\,MB \\
808	Qwen3-8B 3-shot$^{\dagger}$ & $\sim$5{,}200 & 8B & $\sim$16\,GB \\
809	\bottomrule
810	\end{tabular}
811	\vspace{-2pt}
812	{\footnotesize $^{\dagger}$Qwen3-8B latency from exp10 (DD/AA OOD, 118 conversations); not directly comparable to encoder latency measured on IID test.}
813	\end{table}
814	
815	Table~\ref{tab:efficiency} compares inference cost. On matched data (IID test), DeBERTa+BiGRU processes a conversation in 12.1\,ms, 28$\times$ slower than TF-IDF (0.43\,ms), but this speed gap purchases +71\,pp on ActorAttack (F1\,=\,0.972 vs.\ 0.261; Table~\ref{tab:evidence_hierarchy}). LLM-as-judge approaches are orders of magnitude slower ($\sim$5.2\,s per conversation for Qwen3-8B 3-shot) while achieving substantially lower OOD detection (DD\,=\,0.566, AA\,=\,0.652; Table~\ref{tab:llm_judge}). Zero-shot Qwen3-8B achieves F1\,=\,0.0 on DD OOD because it predicts all conversations as benign (Table~\ref{tab:llm_judge}). The full DeBERTa+BiGRU pipeline requires 862\,MB GPU memory, enabling deployment on consumer hardware. The 24.3$\times$ speedup reported in the main text derives from a matched-condition comparison (exp46: DisPeD 13.12\,ms vs.\ Qwen3-8B 318.53\,ms on the same GPU and data); the larger gap in Table~\ref{tab:efficiency} reflects different hardware conditions and evaluation sets.
816	
817	\section{Data Efficiency}
818	\label{app:data_efficiency}
819	
820	\begin{table}[ht]
821	\centering
822	\footnotesize
823	\caption{Data efficiency of 9-class DAPT (3-seed mean$\pm$std, sample std with $n{-}1$ divisor) and vanilla baseline (seed 42 only). $N$ = total training conversations (balanced jailbreak/benign).}
824	\label{tab:data_efficiency}
825	\begin{tabular}{@{}rlccc@{}}
826	\toprule
827	$N$ & \textbf{Variant} & IID & DD OOD & AA OOD \\
828	\midrule
829	50 & 9-class & 1.000$\pm$.000 & 1.000$\pm$.000 & .969$\pm$.037 \\
830	125 & 9-class & 1.000$\pm$.000 & 1.000$\pm$.000 & .975$\pm$.019 \\
831	250 & 9-class & 1.000$\pm$.000 & 1.000$\pm$.000 & .975$\pm$.035 \\
832	350 & 9-class & 1.000$\pm$.000 & .978$\pm$.030 & .972$\pm$.033 \\
833	\midrule
834	50 & Vanilla & .646 & .529 & .234 \\
835	125 & Vanilla & .532 & .244 & .244 \\
836	250 & Vanilla & .987 & .365 & .502 \\
837	350 & Vanilla & 1.000 & .360 & .489 \\
838	\bottomrule
839	\end{tabular}
840	\end{table}
841	
842	Table~\ref{tab:data_efficiency} shows that 9-class DAPT reaches near-saturation performance with as few as 50 conversations (25 jailbreak + 25 benign): AA OOD F1\,=\,0.969$\pm$0.037, already surpassing vanilla at full training size ($N$=350, AA\,=\,0.489) by 48\,pp using only 14\% of the data. DD OOD is perfectly solved at all training sizes. Vanilla performance is noisy across $N$ (single seed); the consistent pattern is that vanilla never exceeds DD\,=\,0.53 or AA\,=\,0.50 regardless of training size, while 9-class maintains AA\,$\geq$\,0.969 at all $N$. Seed 456 is systematically lower across all $N$ values, contributing most of the cross-seed variance; this is consistent with the initialization sensitivity observed in the main results.
843	
844	\section{Auxiliary Loss Weight Ablation}
845	\label{app:lambda}
846	
847	\begin{table}[ht]
848	\centering
849	\footnotesize
850	\caption{Effect of auxiliary persuasion loss weight $\lambda$ during Stage-2 E2E fine-tuning (seed 42). Stage-1 DAPT encoder is identical across all rows; only the Stage-2 loss $L = L_{\text{binary}} + \lambda \cdot L_{\text{strategy}}$ varies.}
851	\label{tab:lambda}
852	\begin{tabular}{@{}rcccc@{}}
853	\toprule
854	$\lambda$ & IID & DD OOD & FITD OOD & AA OOD \\
855	\midrule
856	0 & 1.000 & 1.000 & 1.000 & 1.000 \\
857	0.1 & 1.000 & 1.000 & 1.000 & .990 \\
858	0.5 & 1.000 & 1.000 & 1.000 & .981 \\
859	1.0 & 1.000 & 1.000 & 1.000 & .981 \\
860	2.0 & 1.000 & 1.000 & 1.000 & .944 \\
861	\bottomrule
862	\end{tabular}
863	\end{table}
864	
865	During Stage-2 E2E fine-tuning, the auxiliary persuasion loss weight $\lambda$ has limited impact on detection (Table~\ref{tab:lambda}): the maximum AA OOD gap across all $\lambda$ values is 5.6\,pp (single seed), comparable to the cross-seed variance ($\sim$6\,pp) observed in the main results. All configurations converge to perfect validation F1 within epoch 1, indicating that DAPT representations already encode sufficient discriminative features for downstream classification (Section~\ref{app:frozen_verify}). The value of persuasion strategy classification lies in Stage-1 DAPT, where it shapes encoder representations that transfer across attack families, not in the Stage-2 auxiliary loss.
866	
867	\section{OOD Strategy Prediction Analysis}
868	\label{app:strategy_pred}
869	
870	\begin{table}[ht]
871	\centering
872	\footnotesize
873	\caption{OOD strategy prediction accuracy (jailbreak turns only) and detection rate for the 9-class model (3-seed mean). $r$: Pearson correlation between per-strategy prediction accuracy and per-strategy detection rate.}
874	\label{tab:strategy_pred}
875	\begin{tabular}{@{}lcccc@{}}
876	\toprule
877	\textbf{Dataset} & Strat.\ Acc.\ & Det.\ Rate & Missed (per seed) & $r$ \\
878	\midrule
879	DD OOD & 50.1\% & 99.6\% & 0 / 0 / 1 & $\sim$0.45 \\
880	AA OOD & 50.1\% & 96.2\% & 1 / 7 / 1 & $\sim$0.24 \\
881	\bottomrule
882	\end{tabular}
883	\end{table}
884	
885	Table~\ref{tab:strategy_pred} reports OOD strategy prediction accuracy alongside detection rates. Strategy prediction accuracy is substantially above random (50.1\% vs.\ 11.1\% chance for 9 classes) and positively correlated with detection success ($r \approx 0.24$--0.45), but strategy prediction is not the detection mechanism: frozen probing with a randomly initialized strategy head (Appendix~\ref{app:frozen_verify}) achieves 97.2\% AA OOD detection, and $\lambda$=0 (no strategy loss) matches or exceeds $\lambda > 0$ during E2E fine-tuning (Table~\ref{tab:lambda}). The classification objective shapes representations during Stage-1 DAPT training; at inference, strategy predictions are a byproduct of those representations, not a driver of detection.
886	
887	\section{Cross-Seed Ensemble}
888	\label{app:ensemble}
889	
890	\begin{table}[ht]
891	\centering
892	\footnotesize
893	\caption{Majority vote ensemble (3 seeds) vs.\ single-seed mean on OOD Full. ``Fixed'' = samples corrected by ensemble; ``Broke'' = samples corrupted by ensemble.}
894	\label{tab:ensemble}
895	\begin{tabular}{@{}lcccc@{}}
896	\toprule
897	\textbf{Variant} & DD single$\to$ens. & AA single$\to$ens. & Fixed & Broke \\
898	\midrule
899	9-class & .997$\to$\textbf{1.000} & .972$\to$\textbf{.981} & 5 & 0 \\
900	MLM & .914$\to$\textbf{1.000} & .897$\to$\textbf{.953} & 26 & 0 \\
901	Vanilla & .258$\to$.258 & .258$\to$.258 & 0 & 0 \\
902	\bottomrule
903	\end{tabular}
904	\end{table}
905	
906	Table~\ref{tab:ensemble} shows that majority vote never corrupts correct predictions (Broke\,=\,0 for all variants). MLM benefits most from ensembling (+8.6\,pp DD, +6.0\,pp AA), because its per-seed errors are complementary: each seed fails on different samples, and the majority corrects these. This further exposes MLM's seed instability: its individual seeds are unreliable, but their errors are uncorrelated. By contrast, 9-class seeds are already highly consistent (std\,$\leq$\,0.026), leaving minimal room for ensemble improvement (+0.3--0.9\,pp). Vanilla errors are systematic (all seeds fail on the same OOD samples), so ensembling provides no benefit.
907	
908	\subsection{Seed-Level F1 Comparisons}
909	\label{app:seed_level}
910	
911	To verify that cross-seed pooling does not mask inconsistent pairwise orderings, Table~\ref{tab:seed_level} reports per-seed F1 for all variants on OOD DD and ActorAttack at full conversation length. The overall evidence hierarchy is maintained across seeds, with 9-class and binary consistently outperforming MLM; scrambled shows one reversal on AA (seed 42).
912	
913	\begin{table}[h]
914	\centering
915	\small
916	\caption{Per-seed F1 on OOD Full for key variants (seeds 42, 123, 456). The relative ordering is consistent across seeds.}
917	\label{tab:seed_level}
918	\begin{tabular}{@{}lcccccc@{}}
919	\toprule
920	& \multicolumn{3}{c}{DD-Full} & \multicolumn{3}{c}{AA-Full} \\
921	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
922	\textbf{Variant} & s42 & s123 & s456 & s42 & s123 & s456 \\
923	\midrule
924	9-class & 1.000 & 1.000 & .990 & .990 & .935 & .990 \\
925	Binary & 1.000 & 1.000 & 1.000 & .981 & .990 & 1.000 \\
926	Scrambled & .990 & 1.000 & 1.000 & .891 & .990 & .971 \\
927	MLM-only & 1.000 & .990 & .751 & .971 & .925 & .784 \\
928	Vanilla & .285 & .305 & .348 & .258 & .258 & .258 \\
929	\bottomrule
930	\end{tabular}
931	\end{table}
932	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "756e6c46-3f46-4752-925a-af987e56060b",
  "isSidechain": true,
  "promptId": "968750d3-8ea0-4a1a-a2c1-b6601657157c",
  "agentId": "a8daa86d1003cff17",
  "type": "user",
  "uuid": "6e3a32e2-d2b7-4989-9edc-e51bb01bfdd1",
  "sourceToolAssistantUUID": "756e6c46-3f46-4752-925a-af987e56060b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cc8c01a1-4471-49ec-97ac-eac0175f808e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-23T11:13:58.754Z_

Excellent! I've found the main content. Now let me search for the specific sections to complete the findings. Let me extract the exact sections you need:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e3a32e2-d2b7-4989-9edc-e51bb01bfdd1",
  "isSidechain": true,
  "agentId": "a8daa86d1003cff17",
  "requestId": "req_011CbKQJwaMqyuYFd8sLWKAm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3e3cb158-ff7d-4abc-9186-4577dff9bdb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cc8c01a1-4471-49ec-97ac-eac0175f808e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Bara5u8nGM3ubmqLaGcwx3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 25438,
      "cache_read_input_tokens": 27401,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25438,
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

_source line 12 · 2026-05-23T11:13:59.782Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01X64vuqTKBCwD41NULUKkmR`</summary>

```json
{
  "pattern": "TOST|equivalence.*5\\s*pp|delta.*5|margin.*5",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper",
  "output_mode": "content",
  "context": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e3cb158-ff7d-4abc-9186-4577dff9bdb6",
  "isSidechain": true,
  "agentId": "a8daa86d1003cff17",
  "requestId": "req_011CbKQJwaMqyuYFd8sLWKAm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dd88fcca-624e-4594-830f-f89ac3b02f77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cc8c01a1-4471-49ec-97ac-eac0175f808e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Bara5u8nGM3ubmqLaGcwx3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 25438,
      "cache_read_input_tokens": 27401,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 25438
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 193,
          "cache_read_input_tokens": 27401,
          "cache_creation_input_tokens": 25438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 25438,
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

_source line 13 · 2026-05-23T11:13:59.813Z_

<details><summary>↩ Tool result · `toolu_01X64vuqTKBCwD41NULUKkmR`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex-109-\noindent\hspace{0.5em}{\small vanilla (0.312$\pm$0.026) $<$ topic (0.541$\pm$0.207) $\ll$ wiki-MLM (0.904$\pm$0.115) $\approx$ jb-MLM (0.914$\pm$0.115) $<$ scrambled (0.997$\pm$0.005) $=$ 9-class (0.997$\pm$0.005) $\approx$ binary (1.000$\pm$0.000)}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex-110-\vspace{1pt}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex-111-
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex-112-\paragraph{Domain exposure is the primary mechanism.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex-113-MLM bridges $\sim$60\,pp from vanilla (0.312$\pm$0.026 $\to$ 0.914$\pm$0.115) without labels; this supports the DAPT interpretation~\citep{gururangan2020dontstop}. TF-IDF collapse on ActorAttack (0.261 vs.\ 9-class 0.972) confirms that domain-adapted representations capture features beyond lexical overlap.
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex:114:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex-115-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex-116-Appendix~\ref{app:tsne} provides t-SNE visualizations confirming that domain-adapted variants produce tighter, more separable embedding clusters than the vanilla baseline.
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex-117-
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex-118-\paragraph{Domain specificity is marginal at full length but meaningful for early detection.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex-119-Wikipedia MLM (0.904$\pm$0.115) nearly matches jailbreak-domain MLM at full length (1\,pp gap), though jailbreak-domain text provides an 8\,pp advantage at early prefixes ($K$=2: 0.993 vs.\ 0.911).
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/acl.sty-98-  \newcommand{\@LN@col}[1]{}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/acl.sty-99-  \newcommand{\@LN}[2]{}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/acl.sty-100-  \newcommand{\nolinenumbers}{}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/acl.sty-101-\fi
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/acl.sty-102-
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/acl.sty:103:\PassOptionsToPackage{a4paper,margin=2.5cm,heightrounded=true}{geometry}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/acl.sty-104-\RequirePackage{geometry}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/acl.sty-105-
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/acl.sty-106-\setlength\columnsep{0.6cm}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/acl.sty-107-\newlength\titlebox
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/acl.sty-108-\setlength\titlebox{11\baselineskip}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/acl.sty-255-\partopsep 1pt plus 0.5pt minus 0.5pt
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/acl.sty-256-\itemsep 2pt plus 1pt minus 0.5pt
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/acl.sty-257-\parsep 2pt plus 1pt minus 0.5pt
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/acl.sty-258-
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/acl.sty-259-\leftmargin 2em \leftmargini\leftmargin \leftmarginii 2em
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/acl.sty:260:\leftmarginiii 1.5em \leftmarginiv 1.0em \leftmarginv .5em \leftmarginvi .5em
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/acl.sty:261:\labelwidth\leftmargini\advance\labelwidth-\labelsep \labelsep 5pt
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/acl.sty-262-
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/acl.sty-263-\def\@listi{\leftmargin\leftmargini}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/acl.sty-264-\def\@listii{\leftmargin\leftmarginii
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/acl.sty-265-   \labelwidth\leftmarginii\advance\labelwidth-\labelsep
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/acl.sty-266-   \topsep 2pt plus 1pt minus 0.5pt
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log-114-(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log-115-Package: caption3 2023/07/31 v2.4d caption3 kernel (AR)
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log-116-\caption@tempdima=\dimen162
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log-117-\captionmargin=\dimen163
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log-118-\caption@leftmargin=\dimen164
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log:119:\caption@rightmargin=\dimen165
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log-120-\caption@width=\dimen166
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log-121-\caption@indent=\dimen167
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log-122-\caption@parindent=\dimen168
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log-123-\caption@hangindent=\dimen169
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log-124-Package caption Info: Standard document class detected.
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log-316-\Gin@req@height=\dimen175
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log-317-\Gin@req@width=\dimen176
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log-318-)
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log-319-(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log-320-Package: amsmath 2025/07/09 v2.17z AMS math features
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log:321:\@mathmargin=\skip56
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log-322-
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log-323-For additional information on amsmath, use the `?' option.
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log-324-(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log-325-Package: amstext 2024/11/17 v2.01 AMS text
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log-326-
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log-499-* \topmargin=-38.1381pt
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log-500-* \headheight=12.0pt
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log-501-* \headsep=25.0pt
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log-502-* \topskip=11.0pt
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log-503-* \footskip=30.0pt
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log:504:* \marginparwidth=59.0pt
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log-505-* \marginparsep=10.0pt
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log-506-* \columnsep=17.07182pt
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log-507-* \skip\footins=9.0pt plus 4.0pt minus 2.0pt
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log-508-* \hoffset=0.0pt
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log-509-* \voffset=0.0pt
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-302-\end{tabular}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-303-\end{table}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-304-
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-305-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-306-
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex:307:\section{TOST Equivalence Sensitivity Analysis}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-308-
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-309-\begin{table}[ht]
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-310-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-311-\footnotesize
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex:312:\caption{TOST equivalence test sensitivity to margin $\delta$ (scrambled vs.\ 9-class, 3-seed). $p$-values from two one-sided $t$-tests; $p < 0.05$ confirms equivalence within $\pm\delta$.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-313-\label{tab:tost_sensitivity}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-314-\begin{tabular}{@{}lccc@{}}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-315-\toprule
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex:316:\textbf{Dataset} & $\delta$=5\,pp & $\delta$=3\,pp & $\delta$=2\,pp \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-317-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-318-DD OOD & .006 \checkmark & .016 \checkmark & .035 \checkmark \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-319-ActorAttack & .290 & .428 & .507 \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-320-\bottomrule
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-321-\end{tabular}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-322-\end{table}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-323-
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex:324:On DD, TOST confirms scrambled $\approx$ correct labels even at $\delta$=2\,pp ($p$=0.035), demonstrating that label correctness is not a detection factor; the DD equivalence conclusion is robust to margin choice. On ActorAttack, the mean gap is 2.1\,pp but TOST is underpowered (SE\,=\,0.045, $n$=3) to confirm formal equivalence at any tested margin; the variants are descriptively similar but formally inconclusive.
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-325-
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-326-\section{Partition Robustness and Topic Failure Analysis}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-327-\label{app:random_partition}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-328-\label{app:topic_failure}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-329-
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex-21-
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex-22-Our contributions:
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex-23-\begin{itemize}[leftmargin=*, itemsep=2pt, topsep=4pt]
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex-24-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex-25-
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex:26:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex-27-
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex-28-  \item \textbf{Two-step adaptation protocol.} On the synthetic benchmark, continued pretraining achieves 24.3$\times$ inference speedup over LLM-as-judge (a deployment cost comparison; parameter counts differ by 43$\times$; Appendix~\ref{app:efficiency}); 10--25 target-domain benign conversations reduce FPR below deployment thresholds on both WildChat and OASST2 crowdsourced conversations. No target-domain attack data is required.
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex-29-\end{itemize}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.aux-1507-\@LN{1200}{15}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.aux-1508-\@LN{1201}{15}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.aux-1509-\@LN{1202}{15}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.aux-1510-\@LN{1203}{15}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.aux-1511-\@LN{1204}{15}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.aux:1512:\@writefile{toc}{\contentsline {section}{\numberline {L}TOST Equivalence Sensitivity Analysis}{16}{appendix.L}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.aux:1513:\@writefile{lot}{\contentsline {table}{\numberline {16}{\ignorespaces TOST equivalence test sensitivity to margin $\delta $ (scrambled vs.\ 9-class, 3-seed). $p$-values from two one-sided $t$-tests; $p < 0.05$ confirms equivalence within $\pm \delta $.}}{16}{table.caption.39}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.aux:1514:\newlabel{tab:tost_sensitivity}{{16}{16}{TOST equivalence test sensitivity to margin $\delta $ (scrambled vs.\ 9-class, 3-seed). $p$-values from two one-sided $t$-tests; $p < 0.05$ confirms equivalence within $\pm \delta $}{table.caption.39}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.aux-1515-\@LN{1205}{15}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.aux-1516-\@LN{1206}{15}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.aux-1517-\@LN{1207}{15}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.aux-1518-\@LN{1208}{15}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.aux-1519-\@LN{1209}{15}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd88fcca-624e-4594-830f-f89ac3b02f77",
  "isSidechain": true,
  "promptId": "968750d3-8ea0-4a1a-a2c1-b6601657157c",
  "agentId": "a8daa86d1003cff17",
  "type": "user",
  "uuid": "95365e30-19bd-4f23-adce-84a203fe9c77",
  "sourceToolAssistantUUID": "dd88fcca-624e-4594-830f-f89ac3b02f77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cc8c01a1-4471-49ec-97ac-eac0175f808e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-23T11:14:49.409Z_

Perfect! I have found all the key sections. Let me compile my comprehensive report with exact text passages for your peer review:

## PEER REVIEW FINDINGS - EXACT TEXT PASSAGES

### 1. BOOTSTRAP CI AND CONFIDENCE INTERVALS METHODOLOGY (Section 4.1 Metrics)

From **experiments.tex lines 25-29**:

"**Metrics.**
F1 for binary jailbreak detection at prefix $K$=2 and full conversations (full per-$K$ results in Appendix~\ref{sec:full_prefix}).
OOD results report 3-seed mean$\pm$std (seeds 42, 123, 456) for all variants.
**For key pairwise comparisons, we report BCa bootstrap 95\% confidence intervals (10,000 resamples over individual predictions pooled across 3 seeds; this assumes cross-seed independence and is exploratory) and paired permutation tests (10,000 permutations).** Seed-level F1 values (Table~\ref{tab:seed_level}, Appendix~\ref{app:seed_level}) confirm all pairwise conclusions hold at every seed.
All standard deviations are computed over 3 random seeds using the population formula ($n$ divisor); Bessel-corrected estimates ($n{-}1$ divisor) are $\approx$22\% larger but do not alter any significance conclusions."

**Key technical details:**
- BCa bootstrap with 10,000 resamples
- Cross-seed pooling of predictions (note: assumes cross-seed independence)
- Example CI reported in text (line 65): "Bootstrap CIs confirm non-overlapping intervals (9-class DD Full [0.943, 1.000] vs.\ vanilla [0.202, 0.341]; all permutation $p < 0.0001$)."

---

### 2. TOST EQUIVALENCE TESTING AND DELTA=5PP

From **experiments.tex lines 114-115** (main text):

"All three classification-supervised variants converge to equivalent detection (F1 = 0.997--1.000); McNemar's ($p > 0.13$) and paired permutation tests ($p \geq 0.40$) provide descriptive evidence suggesting equivalence. **Extended to $n$\,=\,10 seeds, TOST (margin = 5\,pp) confirms equivalence on DD ($p < 10^{-8}$, $d$\,=\,$-$0.14; Table~\ref{tab:tost_sensitivity}) and FITD ($p < 10^{-8}$, $d \approx 0$).** An observed difficulty gradient emerges: template attacks show full equivalence ($d < 0.1$), while strategy-diverse ActorAttack retains moderate label sensitivity ($d$\,=\,0.44, $p$\,=\,0.183)."

From **Appendix Section L (TOST Equivalence Sensitivity Analysis)** lines 307-324:

"\section{TOST Equivalence Sensitivity Analysis}

\begin{table}[ht]
\centering
\footnotesize
\caption{TOST equivalence test sensitivity to margin $\delta$ (scrambled vs.\ 9-class, 3-seed). $p$-values from two one-sided $t$-tests; $p < 0.05$ confirms equivalence within $\pm\delta$.}
\label{tab:tost_sensitivity}
\begin{tabular}{@{}lccc@{}}
\toprule
\textbf{Dataset} & $\delta$=5\,pp & $\delta$=3\,pp & $\delta$=2\,pp \\
\midrule
DD OOD & .006 \checkmark & .016 \checkmark & .035 \checkmark \\
ActorAttack & .290 & .428 & .507 \\
\bottomrule
\end{tabular}
\end{table}

**On DD, TOST confirms scrambled $\approx$ correct labels even at $\delta$=2\,pp ($p$=0.035), demonstrating that label correctness is not a detection factor; the DD equivalence conclusion is robust to margin choice. On ActorAttack, the mean gap is 2.1\,pp but TOST is underpowered (SE\,=\,0.045, $n$=3) to confirm formal equivalence at any tested margin; the variants are descriptively similar but formally inconclusive.**"

---

### 3. LENGTH STRATIFICATION (Appendix U - lines 724-792)

From **appendix.tex Section: Length Stratification Analysis** (lines 724-792):

"\section{Length Stratification Analysis}
\label{app:length}

\begin{table}[ht]
\centering
\footnotesize
\caption{Jailbreak recall by conversation length bin on OOD evaluation (3-seed majority vote). Benign conversations span 12--20 turns; jailbreak conversations span 3--10 turns.}
\label{tab:length}
\begin{tabular}{@{}llccc@{}}
\toprule
\textbf{Dataset} & \textbf{Variant} & 1--3 turns & 4--6 turns & 7--10 turns \\
\midrule
\multirow{2}{*}{DD OOD} & 9-class & --- & 100.0\% & 99.4\% \\
& Vanilla & --- & $\leq$2.6\% & $\leq$1.7\% \\
\midrule
\multirow{2}{*}{AA OOD} & 9-class & 93.3\% & 95.6\% & 100.0\% \\
& Vanilla & 0.0\% & $\leq$2.6\% & 0.0\% \\
\bottomrule
\end{tabular}
\end{table}

Table~\ref{tab:length} stratifies jailbreak recall by conversation length. The 9-class model shows no systematic degradation: ActorAttack recall increases monotonically from 93.3\% (1--3 turns) to 100\% (7--10 turns), and DD recall is near-perfect across all bins.

\paragraph{Length confound.}
Benign conversations (12--20 turns) and jailbreak conversations (3--10 turns) have zero length overlap in the OOD evaluation sets, raising the concern that the model discriminates by conversation length rather than content. **Three observations argue against this interpretation:
(1)~Vanilla DeBERTa has access to identical length information via the BiGRU but achieves recall $\leq$2.6\% across all bins; length alone is insufficient without domain-adapted representations.
(2)~At prefix $K$=1, where all conversations are length-equalized, 9-class still achieves F1\,=\,0.773$\pm$0.041 on ActorAttack (Table~\ref{tab:actorattack_full}), demonstrating content-based detection independent of length.
(3)~The model is trained on IID data (Crescendo) and cannot learn OOD-specific length distributions; generalization to unseen length patterns must rely on content features that transfer across attack families.**

\paragraph{Direct empirical verification.}
\label{app:length_independence}

\begin{table}[ht]
\centering
\footnotesize
\caption{Turn-count independence verification (9-class, plan\_002 checkpoints, 3 seeds). Part~A: FPR on test benign truncated to $K$ user turns (all seeds FPR\,=\,0). Part~B: WildChat FPR by turn-count bucket (mean$\pm$std). Part~C: jailbreak detection (F1) after padding with benign turns to 15+ total turns (mean$\pm$std where available).}
\label{tab:length_independence}
\begin{tabular}{@{}llcc@{}}
\toprule
& \textbf{Condition} & \textbf{FPR / F1} & $n$ \\
\midrule
\multicolumn{4}{l}{\textit{Part A: Benign truncation (test set)}} \\[2pt]
& Original (12--20 turns) & FPR = .000 & 38 \\
& Truncated $K$=3 & FPR = .000 & 38 \\
& Truncated $K$=5 & FPR = .000 & 38 \\
& Truncated $K$=8 & FPR = .000 & 38 \\
& Truncated $K$=10$^{*}$ & FPR = .000 & 38 \\
\midrule
\multicolumn{4}{l}{\textit{Part B: WildChat FPR by turn count}} \\[2pt]
& Short (3--10 turns) & FPR = .770$\pm$.105 & 196 \\
& Medium (11--15 turns) & FPR = .942$\pm$.054 & 23 \\
& Long (16+ turns) & FPR = .857$\pm$.117 & 7 \\
\midrule
\multicolumn{4}{l}{\textit{Part C: Jailbreak padding to 15+ turns}} \\[2pt]
& DD original & F1 = .996 & 80 \\
& DD padded & F1 = .971 ($\Delta$=$-$2.5\,pp) & 80 \\
& AA original & F1 = .963 & 80 \\
& AA padded & F1 = .383$\pm$.261 ($\Delta$=$-$57.9\,pp) & 80 \\
\bottomrule
\end{tabular}
\end{table}

Truncating benign conversations to match jailbreak turn counts (Part~A) produces zero false positives across all truncation levels and all 3 seeds, directly confirming that the model does not use conversation length as a detection shortcut."

---

### 4. BENIGN DISTRIBUTION SHIFT & WILDCHAT FPR (Appendix P - lines 430-502)

From **appendix.tex Section: Real-World False Positive Rate** (lines 430-502):

"\section{Real-World False Positive Rate}
\label{app:wildchat_fpr}

\begin{table}[ht]
\centering
\footnotesize
\caption{False positive rate (\%) on 226 WildChat benign multi-turn conversations (GPT-3.5 users, avg 7.4 turns per conversation). All models trained on synthetic Qwen3-8B data (1{,}000-conversation scale). 3-seed mean$\pm$std.}
\label{tab:wildchat_fpr}
\begin{tabular}{@{}lcccc@{}}
\toprule
\textbf{Variant} & Seed 42 & Seed 123 & Seed 456 & Mean$\pm$Std \\
\midrule
9-class & 66.8 & 61.1 & 76.5 & 68.1$\pm$6.4 \\
MLM & 36.7 & 64.6 & 32.3 & 44.5$\pm$14.3 \\
Vanilla & 47.3 & 42.5 & 54.4 & 48.1$\pm$4.9 \\
\bottomrule
\end{tabular}
\end{table}

Table~\ref{tab:wildchat_fpr} evaluates false positive rates on 226 WildChat benign multi-turn conversations from real GPT-3.5 users (avg 7.4 turns). **All variants produce FPR far exceeding deployable thresholds: 9-class is worst at 68.1\%, followed by vanilla (48.1\%) and MLM (44.5\%). Domain adaptation \emph{increases} FPR relative to vanilla (+20\,pp for 9-class), indicating that continued pretraining amplifies dependence on the training benign distribution.** This is consistent with the cross-LLM false positive spike (Table~\ref{tab:cross_llm_error}): models trained on synthetic Qwen3-8B benign text implicitly treat unfamiliar conversational styles as jailbreak indicators. High MLM seed variance (std\,=\,14.3\%) suggests that unsupervised pretraining is particularly unstable under benign distribution shift. **Deployment requires per-domain benign calibration or mixed-source benign training data.**"

From **experiments.tex Section: Benign Distribution Shift** (lines 231-236):

"\subsection{Benign Distribution Shift}
\label{sec:benign_shift}

**All preceding OOD results use IID benign data. On WildChat benign conversations, 9-class FPR rises to 68.1%; cross-LLM error decomposition confirms false positives on unfamiliar benign text drive the collapse (Appendix~\ref{app:wildchat_fpr},~\ref{app:cross_llm}). Few-shot benign-only adaptation resolves this without target-domain attack data: 10 WildChat conversations reduce FPR to 0\%, and 25 OASST2 conversations reduce FPR to 1.0\% (Appendix~\ref{app:wildchat_fpr},~\ref{app:oasst2}); dual-OOD F1 drops 12--14\,pp without adaptation but recovers within 0.3\,pp (Appendix~\ref{app:dual_ood}).**"

---

### 5. PADDING EXPERIMENTS

From **appendix.tex Section: Length Stratification - Part C** (lines 756-792):

"Part~C: Jailbreak padding to 15+ turns...
DD original & F1 = .996 & 80 \\
DD padded & F1 = .971 ($\Delta$=$-$2.5\,pp) & 80 \\
AA original & F1 = .963 & 80 \\
AA padded & F1 = .383$\pm$.261 ($\Delta$=$-$57.9\,pp) & 80 \\

**Padding jailbreak conversations with benign turns (Part~C) reveals an asymmetry: DD detection is resilient ($\Delta$=$-$2.5\,pp), but ActorAttack collapses ($\Delta$=$-$57.9\,pp). Padding experiments append benign turns \emph{after} the complete attack sequence; in practice, adversaries would not dilute their own successful attacks. The collapse nonetheless exposes BiGRU temporal aggregation as vulnerable to attention dilution on subtle attack signals, a limitation discussed in Section~\ref{sec:limitations}.**"

---

### 6. VARIANCE REDUCTION CLAIMS ACROSS SEEDS

From **experiments.tex lines 115-116**:

"**Classification supervision is associated with 3--23$\times$ lower cross-seed variance over MLM on synthetic OOD (std 0.005 vs.\ 0.115 on DD; observed range across 3 seeds; formal variance ratio tests are not applicable at $n$=3; cross-seed ensemble yields marginal additional gains, Appendix~\ref{app:ensemble}). This stability benefit does not transfer to human-authored data, where classification-supervised variants exhibit the highest variance and pure MLM the lowest (Section~\ref{sec:human_data}).**"

From **appendix.tex Section: Cross-Seed Ensemble** (lines 887-932):

"\section{Cross-Seed Ensemble}
\label{app:ensemble}

\begin{table}[ht]
\centering
\footnotesize
\caption{Majority vote ensemble (3 seeds) vs.\ single-seed mean on OOD Full. ``Fixed'' = samples corrected by ensemble; ``Broke'' = samples corrupted by ensemble.}
\label{tab:ensemble}
\begin{tabular}{@{}lcccc@{}}
\toprule
\textbf{Variant} & DD single$\to$ens. & AA single$\to$ens. & Fixed & Broke \\
\midrule
9-class & .997$\to$\textbf{1.000} & .972$\to$\textbf{.981} & 5 & 0 \\
MLM & .914$\to$\textbf{1.000} & .897$\to$\textbf{.953} & 26 & 0 \\
Vanilla & .258$\to$.258 & .258$\to$.258 & 0 & 0 \\
\bottomrule
\end{tabular}
\end{table}

Table~\ref{tab:ensemble} shows that majority vote never corrupts correct predictions (Broke\,=\,0 for all variants). **MLM benefits most from ensembling (+8.6\,pp DD, +6.0\,pp AA), because its per-seed errors are complementary: each seed fails on different samples, and the majority corrects these. This further exposes MLM's seed instability: its individual seeds are unreliable, but their errors are uncorrelated. By contrast, 9-class seeds are already highly consistent (std\,$\leq$\,0.026), leaving minimal room for ensemble improvement (+0.3--0.9\,pp).**"

---

### 7. DATASET SCALE VALIDATION (Appendix J - lines 266-285)

From **appendix.tex Section: Dataset Scale Validation** (lines 266-285):

"\section{Dataset Scale Validation}
\label{app:scale_validation}

\begin{table}[ht]
\centering
\footnotesize
\caption{Dataset scale validation (1{,}000 Qwen conversations, 3-seed mean$\pm$std). IID results omitted due to train/test overlap (71\% of original test set present in expanded training data).}
\label{tab:scale_validation}
\begin{tabular}{@{}lcc@{}}
\toprule
\textbf{Variant} & DD OOD & AA OOD \\
\midrule
9-class & \textbf{.889$\pm$.041} & \textbf{.913$\pm$.041} \\
MLM & .338$\pm$.010 & .351$\pm$.018 \\
Vanilla & .326$\pm$.000 & .508$\pm$.085 \\
\bottomrule
\end{tabular}
\end{table}

**Table~\ref{tab:scale_validation} validates robustness to dataset scale by doubling the training corpus from 500 to 1{,}000 conversations with new topic seeds. The hierarchy 9-class $\gg$ MLM $\approx$ vanilla holds at 2$\times$ scale: classification-based DAPT maintains 40--56\,pp advantage over vanilla, while MLM provides no improvement over vanilla on either attack family (DD: 0.338 vs.\ 0.326; AA: 0.351 vs.\ 0.508).**"

---

## ADDITIONAL CRITICAL NOTES FOR REVIEW:

1. **Bootstrap CI Assumptions**: The text explicitly states the cross-seed pooling "assumes cross-seed independence and is exploratory" (experiments.tex line 28) - this is an important methodological caveat.

2. **TOST Sample Size**: The TOST equivalence tests use only n=3 seeds for ActorAttack and are acknowledged as underpowered (appendix.tex line 324: "TOST is underpowered (SE=0.045, n=3)").

3. **WildChat FPR Contradiction**: The paper shows that domain adaptation (9-class) actually increases FPR relative to vanilla on WildChat (+20pp), which contradicts the claimed benefits of DAPT on real-world data (appendix.tex lines 430-450).

4. **Benign Distribution Shift**: The benign shift is substantial enough to require additional training/adaptation to reach acceptable FPR levels, suggesting a significant practical limitation for deployment.

All exact quotes and line numbers are provided above for your verification during the peer review process.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95365e30-19bd-4f23-adce-84a203fe9c77",
  "isSidechain": true,
  "agentId": "a8daa86d1003cff17",
  "requestId": "req_011CbKQKBABKKbNudTien8ML",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "82a87310-43e7-40c3-9014-1221f18813ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_1_10e47827",
  "sessionId": "cc8c01a1-4471-49ec-97ac-eac0175f808e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DZ2d1AASf2rMeaaRXA9Ew6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 7610,
      "cache_read_input_tokens": 52839,
      "output_tokens": 4998,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7610
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 4998,
          "cache_read_input_tokens": 52839,
          "cache_creation_input_tokens": 7610,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7610,
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
