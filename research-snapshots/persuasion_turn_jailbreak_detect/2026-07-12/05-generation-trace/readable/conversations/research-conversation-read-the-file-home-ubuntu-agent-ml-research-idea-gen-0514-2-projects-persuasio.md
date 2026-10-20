# Research conversation: Read the file /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/concl

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 18
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-afb4a04fbc67e538a.jsonl`
- **Structured JSON:** [`90fc40869107d2982b3b.json`](../../sessions/90/90fc40869107d2982b3b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

18 recorded events

### User

_source line 1 · 2026-05-24T05:18:36.024Z_

Read the file /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex in full.

I need to find where these 4 numbers appear in the conclusion and understand their context:
- 3.7
- 9.4
- 2.5
- 57.9

For each, tell me: (1) the exact sentence it appears in, (2) what it refers to, and (3) whether this number also appears in experiments.tex or appendix.tex (check those files too).

Report concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8fdf9905-2713-48d3-8d3b-5ec87cb90759",
  "agentId": "afb4a04fbc67e538a",
  "type": "user",
  "uuid": "833c12c3-7e88-4330-90b7-023fe4ac2a61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-24T05:18:39.503Z_

I'll read the conclusion file and search for those numbers across the relevant files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "833c12c3-7e88-4330-90b7-023fe4ac2a61",
  "isSidechain": true,
  "agentId": "afb4a04fbc67e538a",
  "requestId": "req_011CbLq2DpMaCg96dW7gWM7i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d216a93-c107-41cf-834b-1a16583db151",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016Lcf3T2VUYGzkSFm7M5aVJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 60598,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 60598,
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

_source line 3 · 2026-05-24T05:18:39.720Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QRXi7oy3JRaLL3Y44HZcpp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d216a93-c107-41cf-834b-1a16583db151",
  "isSidechain": true,
  "agentId": "afb4a04fbc67e538a",
  "requestId": "req_011CbLq2DpMaCg96dW7gWM7i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70f1d8f6-070b-48d4-9df1-fd8b628ac957",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016Lcf3T2VUYGzkSFm7M5aVJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 60598,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 60598,
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

_source line 4 · 2026-05-24T05:18:39.731Z_

<details><summary>↩ Tool result · `toolu_01QRXi7oy3JRaLL3Y44HZcpp`</summary>

```text
1	% conclusion.tex
2	
3	\section{Discussion}
4	\label{sec:discussion}
5	
6	\begin{figure}[t]
7	\centering
8	\includegraphics[width=\columnwidth]{figures/paper/fig4_svd_subspace.pdf}
9	\caption{Test representations projected onto top-2 SVD directions. 9-class DAPT produces clear cluster separation absent in vanilla.}
10	\label{fig:svd_subspace}
11	\end{figure}
12	
13	\paragraph{Discriminative compression and label equivalence.}
14	Three observations argue against a topic shortcut: unstable topic OOD (F1\,=\,0.541$\pm$0.207), scrambled labels within 3.9\,pp, and label-free MLM detection (F1\,$\geq$\,0.97 at $K \leq 5$).
15	Classification DAPT compresses features into few dimensions (participation ratio 3.7--9.4 vs.\ 25--32; Figure~\ref{fig:svd_subspace}; Appendix~\ref{app:representation}), consistent with \citet{zhang2021understanding}: domain-relevant partitioning appears necessary (topic DAPT fails) and compression localizes to 3 SVD dimensions in layers 8--12. A probe confirms sufficiency; removal degrades DD by 17\,pp (Appendix~\ref{app:discriminative_probe}). The partition sufficiency finding implies that the classification objective's value lies in its structural role---forcing class-conditional feature organization---rather than in encoding persuasion-specific semantics.
16	
17	\paragraph{Cross-condition transfer and boundaries.}
18	ToxicChat (+18--42\,pp) and cross-LLM experiments (Appendix~\ref{app:cross_llm}) confirm transfer beyond single-LLM artifacts; domain exposure is universally beneficial (all jailbreak-domain DAPT variants exceed vanilla by $\geq$18\,pp on ToxicChat) but the ranking reverses across conditions (MLM leads on human data). Mixed-LLM 9-class maintains 0.818 while MLM collapses. Both data scaling (Appendix~\ref{app:scale_validation}) and mixed-LLM training involve distributional heterogeneity that appears to erode classification DAPT's concentrated feature advantage. At larger scales (355M), DAPT can be counterproductive (RoBERTa-large vanilla AA\,=\,1.000 vs.\ 9-class 0.946), and WildChat FPR rises to 68.1\%, suggesting DAPT encodes LLM-specific stylistic features that limit benign-side generalization. Mean pooling matches BiGRU ($\Delta \leq 1$\,pp), indicating detection relies on per-turn content rather than sequential patterns.
19	
20	\paragraph{Length as a potential confound.}
21	Length-matched evaluation ($N$=155) shows negligible change (DD $\Delta$\,=\,$-$2.5\,pp); the $-$57.9\,pp ActorAttack collapse under benign-turn padding (Appendix~\ref{app:length_independence}) reflects signal density dilution rather than length shortcut removal.
22	
23	\section{Conclusion}
24	
25	We decompose multi-turn jailbreak generalization into two complementary findings. On synthetic data at base scale, classification DAPT recovers OOD detection (F1\,=\,0.97--1.0 vs.\ vanilla 0.26--0.31), though template-attack robustness does not extend to strategy-diverse scenarios under mixed-LLM training (ActorAttack F1\,=\,0.504); on human-authored data, the hierarchy reverses (ToxicChat MLM 0.837 vs.\ classification 0.596)---the advantage is condition-specific and counterproductive at 355M scale. Few-shot benign adaptation reduces FPR from 58--68\% to 0--1.5\% with 10--25 conversations. The ablation framework provides a reusable template for diagnosing when domain adaptation succeeds and when it fails in this safety-critical detection setting.
26	
27	\section{Limitations}
28	\label{sec:limitations}
29	
30	\begin{itemize}[nosep,leftmargin=*]
31	\item \textbf{Synthetic data only.} All findings derive from synthetic conversations (single LLM, Qwen3-8B; 350 training, 76--118 test, 3 seeds). The evidence hierarchy reverses on human single-turn data (ToxicChat; Section~\ref{sec:discussion}), and no human-generated multi-turn jailbreak dataset exists.
32	\item \textbf{IID benign upper bound.} OOD F1 figures assume IID benign data; dual-OOD evaluation drops 13--14\,pp without adaptation (Table~\ref{tab:evidence_hierarchy}). Few-shot benign adaptation recovers performance but is validated on only two platforms ($n \leq 50$).
33	\item \textbf{Scope.} Only persuasion-mediated multi-turn attacks are addressed; single-turn token-level attacks and non-text modalities are out of scope. Cross-encoder comparisons (Section~\ref{sec:cross_encoder}) confound architecture with parameter count (184M vs.\ 355M). The 50-sample annotation verification ($\kappa$\,=\,0.78) limits evaluation of strategy characterization accuracy; however, the scrambled-label experiment demonstrates that label correctness does not affect template-attack detection. Our experiments cover base-scale encoders (125M--355M); DAPT effects may differ at larger scales, where RoBERTa-large already shows counterproductive adaptation (Section~\ref{sec:cross_encoder}).
34	\end{itemize}
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70f1d8f6-070b-48d4-9df1-fd8b628ac957",
  "isSidechain": true,
  "promptId": "8fdf9905-2713-48d3-8d3b-5ec87cb90759",
  "agentId": "afb4a04fbc67e538a",
  "type": "user",
  "uuid": "400234e3-a48e-4d87-ba5a-1ee47b977c0e",
  "sourceToolAssistantUUID": "70f1d8f6-070b-48d4-9df1-fd8b628ac957",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-24T05:18:39.930Z_

<details open><summary>🔧 Tool call — Read · `toolu_019XubRh91X1s8uLNp6F8eLb`</summary>

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
  "parentUuid": "400234e3-a48e-4d87-ba5a-1ee47b977c0e",
  "isSidechain": true,
  "agentId": "afb4a04fbc67e538a",
  "requestId": "req_011CbLq2DpMaCg96dW7gWM7i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42ae6e9a-65ff-4a60-af65-a9c13d442e80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016Lcf3T2VUYGzkSFm7M5aVJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 60598,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 60598,
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

_source line 6 · 2026-05-24T05:18:39.946Z_

<details><summary>↩ Tool result · `toolu_019XubRh91X1s8uLNp6F8eLb`</summary>

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
59	On OOD DD, vanilla drops to F1\,=\,0.312$\pm$0.026 and worsens with more turns (0.628$\to$0.312 at Full), consistent with attack turns occupying benign embedding regions~\citep{bullwinkel2025repeng}. MLM recovers to $\geq$0.97 at $K \leq 5$ without labels but is unstable at full length (0.914$\pm$0.115); 9-class maintains 0.997$\pm$0.005.
60	On strategy-diverse ActorAttack, TF-IDF collapses (0.261) while 9-class maintains 0.972$\pm$0.026, a 71\,pp gap confirming domain-adapted representations capture beyond-lexical features.
61	Seed-level results confirm consistent separation (Table~\ref{tab:seed_level}; bootstrap CIs non-overlapping, permutation $p < 0.0001$). FITD is non-discriminative (all F1\,$\geq$\,0.990).
62	
63	\begin{figure}[t]
64	\centering
65	\includegraphics[width=\columnwidth]{figures/paper/fig2_cross_attack_bar.pdf}
66	\caption{Cross-attack overview (F1 at full conversation length). DisPeD (9-class) maintains near-perfect detection across IID and both OOD families; vanilla collapses on OOD DD. FITD is non-discriminative for all methods.}
67	\label{fig:cross_attack_bar}
68	\end{figure}
69	
70	Prefix-length analysis (Appendix Table~\ref{tab:full_prefix}) confirms 9-class stability across all prefixes (0.972--0.997) vs.\ MLM instability at full length (0.914$\pm$0.115) and vanilla degradation (0.628$\to$0.312).
71	
72	%----------------------------------------------------------------------
73	\subsection{Decomposing the Detection Mechanism}
74	\label{sec:decomposition}
75	
76	\begin{table}[t]
77	\centering
78	\small
79	\caption{Evidence hierarchy on OOD DD and ActorAttack (AA) at full conversation length (3-seed mean$\pm$std where available). OOD F1 reflects attack-side generalization only; benign samples are IID from training distribution (benign-side shift evaluated in Section~\ref{sec:benign_shift}). Bold indicates best per column. All variants share the same Stage-2 pipeline. Full per-prefix results in Appendix Tables~\ref{tab:full_prefix} and~\ref{tab:actorattack_full}. Bottom rows: full dual-OOD evaluation with WildChat benign replacing IID benign (Appendix~\ref{app:dual_ood}).}
80	\label{tab:evidence_hierarchy}
81	\resizebox{\columnwidth}{!}{%
82	\begin{tabular}{@{}lccc@{}}
83	\toprule
84	\textbf{Variant} & DD-Full & AA-Full & DD-$K$=2 \\
85	\midrule
86	9-class (full model) & .997$\pm$.005 & .972$\pm$.026 & .981$\pm$.013 \\
87	Binary (2-class) & \textbf{1.000$\pm$.000} & \textbf{.990$\pm$.008} & .994$\pm$.009 \\
88	Scrambled labels & .997$\pm$.005 & .951$\pm$.043 & .981$\pm$.026 \\
89	MLM-only$^{\ddagger}$ (no labels) & .914$\pm$.115 & .893$\pm$.080 & .993$\pm$.009 \\
90	Mean pooling$^{*}$ & .991$\pm$.013 & .962$\pm$.015 & .994$\pm$.009 \\
91	\midrule
92	Topic classif.\ (5-class) & .541$\pm$.207 & .625$\pm$.141 & .593$\pm$.166 \\
93	Wikipedia MLM & .904$\pm$.115 & .686$\pm$.297 & .911$\pm$.073 \\
94	Vanilla DeBERTa & .312$\pm$.026 & .258$\pm$.000 & .479$\pm$.038 \\
95	TF-IDF LR$^{\dagger}$ & .961 & .261 & \textbf{1.000} \\
96	Llama Guard~3$^{\P}$ & .024 & .000 & -- \\
97	\midrule
98	\multicolumn{4}{l}{\textit{Dual-OOD (WildChat benign; Section~\ref{sec:benign_shift})}} \\[2pt]
99	9-class (no adapt) & .855 & .842 & -- \\
100	9-class (+10-shot) & .994 & .981 & -- \\
101	\bottomrule
102	\end{tabular}}
103	\vspace{-2pt}
104	{\footnotesize $^{*}$9-class encoder with mean pooling replacing BiGRU. $^{\dagger}$Deterministic (no std). $^{\ddagger}$MLM-only IID (Table~\ref{tab:main_results}) is single-seed (42); all OOD values are 3-seed. $^{\P}$Zero-shot; no domain training.}
105	\end{table}
106	
107	A clear \emph{evidence hierarchy} emerges across seven variants on synthetic multi-turn data (Table~\ref{tab:evidence_hierarchy}, Figure~\ref{fig:evidence_hierarchy}), ordered by OOD detection at full conversation length: vanilla $<$ topic $\ll$ MLM $<$ classification-supervised ($\approx$\,1.0 on DD).
108	
109	\begin{figure}[t]
110	\centering
111	\includegraphics[width=\columnwidth]{figures/paper/fig3_evidence_hierarchy.pdf}
112	\caption{Evidence hierarchy across evaluation conditions. Classification-based DAPT outperforms MLM and vanilla on synthetic OOD attacks (DD, AA), but the hierarchy reverses on human-authored single-turn data (ToxicChat), where JB-MLM leads.}
113	\label{fig:evidence_hierarchy}
114	\end{figure}
115	
116	\paragraph{Domain exposure is the primary observed factor.}
117	MLM bridges $\sim$60\,pp from vanilla (0.312$\pm$0.026 $\to$ 0.914$\pm$0.115) without labels; this supports the DAPT interpretation~\citep{gururangan2020dontstop}. TF-IDF collapse on ActorAttack (0.261 vs.\ 9-class 0.972) confirms that domain-adapted representations capture features beyond lexical overlap.
118	All three classification-supervised variants converge to equivalent detection (F1 = 0.997--1.000); McNemar's ($p > 0.13$) and paired permutation tests ($p \geq 0.40$) provide descriptive evidence suggesting equivalence. Extended to $n$\,=\,10 seeds, TOST (margin = 5\,pp) confirms equivalence on DD ($p < 10^{-8}$, $d$\,=\,$-$0.14; Table~\ref{tab:tost_sensitivity}) and FITD ($p < 10^{-8}$, $d \approx 0$). Label quality and granularity are non-factors for template-attack detection (DD/FITD: $|d| \leq 0.14$), but strategy-diverse ActorAttack retains moderate label sensitivity ($d$\,=\,0.44, TOST $p$\,=\,0.183). For template attacks, any domain-relevant classification objective suffices; the objective's structural role---partitioning the representation space---matters more than label semantics. Strategy-diverse attacks mark a difficulty boundary for this sufficiency.
119	Classification supervision is associated with 3--23$\times$ lower cross-seed variance over MLM on synthetic OOD (std 0.005 vs.\ 0.115 on DD; 3 seeds; Appendix~\ref{app:ensemble}), though this reverses on human-authored data (Section~\ref{sec:human_data}).
120	
121	\paragraph{Domain specificity is marginal at full length but meaningful for early detection.}
122	Wikipedia MLM (0.904$\pm$0.115) nearly matches jailbreak-domain MLM at full length (1\,pp gap), though jailbreak-domain text provides an 8\,pp advantage at early prefixes ($K$=2: 0.993 vs.\ 0.911).
123	Perturbation analysis (Section~\ref{sec:perturbation}) reveals a sharper domain specificity effect: Wikipedia MLM degrades by $\sim$12\,pp under adversarial paraphrasing while jailbreak-domain MLM degrades by only 2.6\,pp.
124	
125	\paragraph{Misaligned supervision destabilizes generalization.}
126	Topic classification's poor performance (0.541$\pm$0.207) is consistent with misaligned supervision; the cleaner test isolating domain exposure is Wiki-MLM vs.\ JB-MLM (Section~\ref{sec:decomposition}).
127	
128	\paragraph{Evidence hierarchy on strategy-diverse attacks.}
129	ActorAttack~\citep{ren2024actorattack} preserves the same hierarchy (Figure~\ref{fig:evidence_hierarchy}) with wider gaps: TF-IDF collapses (0.261) while classification variants converge (0.951--0.990, max gap 3.9\,pp); DAPT provides $\sim$71\,pp over vanilla (Appendix~\ref{sec:actorattack_full},~\ref{app:aa_error}).
130	
131	\paragraph{Temporal modeling.}
132	Mean pooling matches BiGRU (F1 gap $\leq$ 1\,pp; Appendix~\ref{app:temporal}) and turn-order shuffling is negligible ($|\Delta| < 1$\,pp), confirming detection relies on per-turn content rather than sequential patterns.
133	
134	%----------------------------------------------------------------------
135	\subsection{Cross-Encoder Validation}
136	\label{sec:cross_encoder}
137	
138	\begin{table}[t]
139	\centering
140	\small
141	\caption{Cross-encoder comparison on OOD Full (3-seed mean$\pm$std). DD = Deceptive Delight, AA = ActorAttack. Bold indicates best per encoder group.}
142	\label{tab:cross_encoder}
143	\resizebox{\columnwidth}{!}{%
144	\begin{tabular}{@{}lcc@{}}
145	\toprule
146	\textbf{Variant} & DD & AA \\
147	\midrule
148	\multicolumn{3}{l}{\textit{DeBERTa-v3-base (184M)}} \\[2pt]
149	Vanilla & .312$\pm$.026 & .258$\pm$.000 \\
150	MLM & .914$\pm$.115 & .893$\pm$.080 \\
151	9-class & \textbf{.997$\pm$.005} & \textbf{.972$\pm$.026} \\
152	\midrule
153	\multicolumn{3}{l}{\textit{RoBERTa-base (125M)}} \\[2pt]
154	Vanilla & .981$\pm$.026 & .466$\pm$.163 \\
155	MLM & .987$\pm$.018 & .730$\pm$.201 \\
156	9-class & \textbf{.994$\pm$.005} & \textbf{.939$\pm$.046} \\
157	\midrule
158	\multicolumn{3}{l}{\textit{RoBERTa-large (355M)}} \\[2pt]
159	Vanilla & .927$\pm$.036 & \textbf{1.000$\pm$.000} \\
160	MLM & .884$\pm$.065 & .874$\pm$.014 \\
161	9-class & \textbf{.987$\pm$.004} & .946$\pm$.057 \\
162	\bottomrule
163	\end{tabular}}
164	\end{table}
165	
166	To test whether the evidence hierarchy depends on encoder choice, we replicate vanilla, MLM, and 9-class on RoBERTa-base~\citep{liu2019roberta} (Table~\ref{tab:cross_encoder}).
167	On DD, RoBERTa-base vanilla already achieves 0.981$\pm$0.026 (vs.\ DeBERTa 0.312$\pm$0.026), so DAPT adds only 1.3\,pp. ActorAttack exposes this as DD's simplicity: RoBERTa-base vanilla collapses to 0.466$\pm$0.163, a 51.5\,pp drop, while domain-adapted variants recover (9-class: 0.939$\pm$0.046).
168	
169	RoBERTa-large (355M) reverses the DAPT advantage on ActorAttack (vanilla 1.000 vs.\ 9-class 0.946; Table~\ref{tab:roberta_large_lr}), revealing a difficulty threshold: base-scale encoders require DAPT for all attacks, while sufficient capacity renders it unnecessary. A BERT-base proxy confirms DAPT, not architecture, drives generalization (Appendix~\ref{app:bert_proxy}).
170	
171	%----------------------------------------------------------------------
172	\subsection{Mixed-LLM Training}
173	
174	All preceding experiments use single-source (Qwen3-8B) data. To test whether the evidence hierarchy transfers when training data mixes LLM sources, we train on 250 Qwen + 250 Llama-3.1-8B conversations (Table~\ref{tab:mixed_llm}).
175	Classification-based DAPT is the only variant that substantially outperforms vanilla: 9-class achieves DD OOD F1\,=\,0.818$\pm$0.096 (+53\,pp over vanilla 0.291$\pm$0.065), while MLM drops to vanilla level (0.289$\pm$0.101). On strategy-diverse ActorAttack, detection degrades to chance level (9-class F1\,=\,0.504$\pm$0.107, indistinguishable from majority baseline at $n$\,=\,3).
176	Mixed-LLM training confirms that classification supervision generalizes across LLM sources where unsupervised pretraining does not (full results in Appendix~\ref{app:mixed_llm}); per-source data reduction (250 vs.\ 350) is an alternative explanation we cannot yet disentangle.
177	
178	%----------------------------------------------------------------------
179	\subsection{Human Data Validation}
180	\label{sec:human_data}
181	
182	Since both training and OOD evaluation data are Qwen3-8B-generated, we validate on ToxicChat~\citep{lin2023toxicchat} (204 human-written jailbreak attempts + 204 benign conversations from real LMSYS interactions).
183	
184	\begin{table}[t]
185	\centering
186	\small
187	\caption{Human data validation on ToxicChat~\citep{lin2023toxicchat} (macro F1, 3-seed mean$\pm$std). Bold indicates best. Single-turn data from real LMSYS user interactions, independent of Qwen3-8B.}
188	\label{tab:human_data}
189	\begin{tabular}{@{}lc@{}}
190	\toprule
191	\textbf{Variant} & Macro F1 \\
192	\midrule
193	JB-MLM & \textbf{.837$\pm$.013} \\
194	Wiki-MLM & .791$\pm$.093 \\
195	Binary & .705$\pm$.072 \\
196	Scrambled & .616$\pm$.056 \\
197	9-class & .596$\pm$.087 \\
198	Topic & .496$\pm$.042 \\
199	\midrule
200	Vanilla & .413$\pm$.021 \\
201	\bottomrule
202	\end{tabular}
203	\end{table}
204	
205	The ordering reverses (Figure~\ref{fig:evidence_hierarchy}): JB-MLM leads (0.837$\pm$0.013) while 9-class ranks lower (0.596$\pm$0.087; $p < 0.001$). All jailbreak-domain DAPT variants exceed vanilla by 18--42\,pp, confirming transfer to human-written attacks. ToxicChat is single-turn, so the classification head provides no advantage.
206	
207	%----------------------------------------------------------------------
208	\subsection{Robustness and Strategy Analysis}
209	\label{sec:perturbation}
210	
211	Under adversarial paraphrasing (BERTScore 0.92), classification variants achieve zero degradation on OOD DD while non-adapted models degrade by $\sim$12\,pp; on ActorAttack, DAPT degrades ($\Delta$\,=\,$-$20.4\,pp) but maintains 52\,pp over vanilla (Table~\ref{tab:ood_perturbation}; Appendix~\ref{sec:perturbation_full}). We distinguish \emph{template attacks} (transition rate $<$\,0.1; e.g., Crescendo, DD) from \emph{structurally complex attacks} (rate $>$\,0.3; e.g., ActorAttack). The 9-class taxonomy characterizes known attacks ($\kappa$\,=\,0.78) but degrades on OOD ($\kappa$\,=\,0.126; Appendix~\ref{app:strategy_pred}); detection operates through \texttt{[CLS]} embeddings, not strategy accuracy.
212	
213	%----------------------------------------------------------------------
214	\subsection{Benign Distribution Shift}
215	\label{sec:benign_shift}
216	
217	On WildChat benign conversations, 9-class FPR rises to 68.1\%. Few-shot adaptation (Stage-2 BiGRU, encoder frozen, $N$ benign conversations, BCE loss, 5 epochs) resolves this: 10 WildChat conversations reduce FPR to 0\%, 25 OASST2 to 1.5\%; dual-OOD F1 drops 12--14\,pp without adaptation but recovers within 0.3\,pp (Appendix~\ref{app:dual_ood}).
218	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42ae6e9a-65ff-4a60-af65-a9c13d442e80",
  "isSidechain": true,
  "promptId": "8fdf9905-2713-48d3-8d3b-5ec87cb90759",
  "agentId": "afb4a04fbc67e538a",
  "type": "user",
  "uuid": "4faaad5c-dcb5-4075-8c07-c5cd733267b7",
  "sourceToolAssistantUUID": "42ae6e9a-65ff-4a60-af65-a9c13d442e80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-24T05:18:40.260Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0131k9YbSJK2a61e9oMB5k9k`</summary>

```json
{
  "pattern": "**/appendix.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4faaad5c-dcb5-4075-8c07-c5cd733267b7",
  "isSidechain": true,
  "agentId": "afb4a04fbc67e538a",
  "requestId": "req_011CbLq2DpMaCg96dW7gWM7i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6fa89195-cb60-4bad-bda0-00d45d18a8f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016Lcf3T2VUYGzkSFm7M5aVJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 60598,
      "cache_read_input_tokens": 0,
      "output_tokens": 279,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 60598
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 279,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 60598,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 60598,
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

_source line 8 · 2026-05-24T05:18:40.291Z_

<details><summary>↩ Tool result · `toolu_0131k9YbSJK2a61e9oMB5k9k`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6fa89195-cb60-4bad-bda0-00d45d18a8f4",
  "isSidechain": true,
  "promptId": "8fdf9905-2713-48d3-8d3b-5ec87cb90759",
  "agentId": "afb4a04fbc67e538a",
  "type": "user",
  "uuid": "e783969c-bd92-4d6a-8046-874c6d3082b4",
  "sourceToolAssistantUUID": "6fa89195-cb60-4bad-bda0-00d45d18a8f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-24T05:18:42.437Z_

Now let me search for those specific numbers in the appendix file:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e783969c-bd92-4d6a-8046-874c6d3082b4",
  "isSidechain": true,
  "agentId": "afb4a04fbc67e538a",
  "requestId": "req_011CbLq2Y5TWrRFafpBB8UR6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d6cac75b-eae9-4865-bc65-fe0bfd80a49f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RGruGp2EkDQjzd2z5sicR2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 9366,
      "cache_read_input_tokens": 60598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9366,
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

_source line 10 · 2026-05-24T05:18:42.789Z_

<details open><summary>🔧 Tool call — Read · `toolu_012Peo7AqDLwfzopY88iGJCs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6cac75b-eae9-4865-bc65-fe0bfd80a49f",
  "isSidechain": true,
  "agentId": "afb4a04fbc67e538a",
  "requestId": "req_011CbLq2Y5TWrRFafpBB8UR6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2d244864-cfe8-44ba-a791-68d2fbdd7d03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RGruGp2EkDQjzd2z5sicR2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 9366,
      "cache_read_input_tokens": 60598,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9366
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 126,
          "cache_read_input_tokens": 60598,
          "cache_creation_input_tokens": 9366,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9366,
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

_source line 11 · 2026-05-24T05:18:43.048Z_

<details><summary>↩ Tool result · `toolu_012Peo7AqDLwfzopY88iGJCs`</summary>

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
56	9-class (ours) & .990$\pm$.013 & .981$\pm$.013 & .972$\pm$.026 & .997$\pm$.005 & .997$\pm$.005 \\
57	Binary & .994$\pm$.009 & .994$\pm$.009 & .984$\pm$.008 & 1.000$\pm$.000 & 1.000$\pm$.000 \\
58	Scrambled & .997$\pm$.005 & .981$\pm$.026 & .975$\pm$.029 & .997$\pm$.005 & .997$\pm$.005 \\
59	MLM-only & .973$\pm$.019 & .993$\pm$.009 & .997$\pm$.005 & .997$\pm$.005 & .914$\pm$.115 \\
60	Vanilla DeBERTa & .628$\pm$.038 & .479$\pm$.038 & .389$\pm$.027 & .351$\pm$.030 & .312$\pm$.026 \\
61	TF-IDF LR & 1.000 & 1.000 & .994 & 1.000 & .961 \\
62	\midrule
63	\multicolumn{6}{l}{\textit{OOD (FITD)}} \\[2pt]
64	9-class (ours) & 1.000$\pm$.000 & .997$\pm$.005 & -- & -- & 1.000$\pm$.000 \\
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
287	The performance decline at 1{,}000 conversations may reflect distributional heterogeneity introduced by diverse topic seeds: the additional conversations broaden the training distribution, potentially diluting the concentrated attack-relevant features that smaller, more homogeneous datasets preserve. IID evaluation was precluded by train/test overlap in the expanded dataset (71\%), limiting analysis to OOD metrics. Human-data validation also degrades under scaled training (ToxicChat F1: 0.596 $\to$ 0.341), suggesting the expanded distribution shifts representations away from features useful for both synthetic OOD and human data.
288	
289	\section{RoBERTa-large DAPT Learning Rate Control}
290	
291	\begin{table}[ht]
292	\centering
293	\footnotesize
294	\caption{RoBERTa-large (355M) DAPT learning rate control on OOD Full (3-seed mean$\pm$std). Reducing the learning rate worsens both DD and AA, ruling out over-adaptation as the cause of the regression in Table~\ref{tab:cross_encoder}.}
295	\label{tab:roberta_large_lr}
296	\begin{tabular}{@{}lcc@{}}
297	\toprule
298	\textbf{Config} & DD Full & AA Full \\
299	\midrule
300	Vanilla (no DAPT) & .927$\pm$.036 & 1.000$\pm$.000 \\
301	9-class, LR=$2 \times 10^{-5}$ & .987$\pm$.004 & .946$\pm$.057 \\
302	9-class, LR=$1 \times 10^{-5}$ & .948$\pm$.034 & .781$\pm$.054 \\
303	\bottomrule
304	\end{tabular}
305	\end{table}
306	
307	Reducing the DAPT learning rate from $2 \times 10^{-5}$ to $1 \times 10^{-5}$ worsens both DD and AA performance, which rules out over-adaptation as the cause of the regression observed in Table~\ref{tab:cross_encoder}. An MLM-only variant (without classification) produces the same pattern (AA Full = 0.874$\pm$0.014); representation drift from continued pretraining, not classification-specific bias, is the underlying cause. Domain-adaptive fine-tuning narrows the representation space of a sufficiently large encoder and reduces its inherent OOD generalization ability.
308	
309	\section{TOST Equivalence Sensitivity Analysis}
310	
311	\begin{table}[ht]
312	\centering
313	\footnotesize
314	\caption{TOST equivalence test (scrambled vs.\ 9-class, $\delta$=5\,pp, 10 seeds). $p < 0.05$ confirms equivalence within $\pm\delta$.}
315	\label{tab:tost_sensitivity}
316	\begin{tabular}{@{}lccc@{}}
317	\toprule
318	\textbf{Dataset} & $p$ & $d$ & Equivalent? \\
319	\midrule
320	DD OOD & $2.06 \times 10^{-9}$ & $-$0.136 & \checkmark \\
321	FITD OOD & $\approx 0$ & 0.000 & \checkmark \\
322	ActorAttack & .183 & 0.440 & -- \\
323	\bottomrule
324	\end{tabular}
325	\end{table}
326	
327	We set $\delta = 5$\,pp as the equivalence margin: at performance levels above F1\,=\,0.95, a 5-point difference corresponds to roughly a 5$\times$ change in miss rate (e.g., 0.3\% vs.\ 1.5\% of jailbreaks missed), which would materially influence deployment thresholds. With 10 seeds, DD and FITD confirm formal equivalence ($p < 10^{-8}$, $|d| \leq 0.14$), demonstrating that label correctness is not a detection factor for template attacks. On ActorAttack, the mean gap is 3.0\,pp with moderate effect size ($d$\,=\,0.44); TOST does not confirm equivalence ($p$\,=\,0.183), indicating that strategy-diverse attacks retain some sensitivity to label quality. Sensitivity to margin choice was verified at $n$\,=\,3 (DD equivalent at $\delta$\,=\,2\,pp); the 10-seed analysis uses the more conservative $\delta$\,=\,5\,pp.
328	
329	\section{Partition Robustness and Topic Failure Analysis}
330	\label{app:random_partition}
331	\label{app:topic_failure}
332	
333	\subsection{Random Binary Partition Robustness}
334	
335	\begin{table}[ht]
336	\centering
337	\footnotesize
338	\caption{OOD F1 for 10 random binary partitions of the 9 strategy labels (each partition randomly assigns strategies to group A or B). All partitions use identical Stage-1 DAPT and Stage-2 GRU training; only the binary label mapping differs. Seed 42 (3 runs).}
339	\label{tab:random_partition}
340	\begin{tabular}{@{}lcccc@{}}
341	\toprule
342	\textbf{Partition} & \textbf{Group A} & \textbf{IID} & \textbf{DD OOD} & \textbf{AA OOD} \\
343	\midrule
344	0 & \{0,2,4,5,7\} & 1.000 & 1.000 & 1.000 \\
345	1 & \{1,3,5,6,8\} & 1.000 & 1.000 & 1.000 \\
346	2 & \{0,1,3,7,8\} & 1.000 & 1.000 & 1.000 \\
347	3 & \{2,4,5,6,7\} & 1.000 & 1.000 & 1.000 \\
348	4 & \{0,1,2,6,8\} & 1.000 & 1.000 & 1.000 \\
349	5 & \{0,3,4,7,8\} & 1.000 & 1.000 & 1.000 \\
350	6 & \{1,2,3,5,6\} & 1.000 & 1.000 & 1.000 \\
351	7 & \{1,4,6,7\}   & 1.000 & 1.000 & 0.636 \\
352	8 & \{0,2,3,4,8\} & 1.000 & 1.000 & 1.000 \\
353	9 & \{0,1,5,7,8\} & 1.000 & 1.000 & 1.000 \\
354	\midrule
355	Mean$\pm$Std &  & 1.000$\pm$.000 & 1.000$\pm$.000 & 0.964$\pm$.109 \\
356	\bottomrule
357	\end{tabular}
358	\end{table}
359	
360	All 10 partitions achieve perfect IID and DD OOD detection regardless of how the 9 strategy labels are split into two groups. On ActorAttack, 9/10 partitions achieve F1\,=\,1.000; the sole outlier (partition~7, AA F1\,=\,0.636) uses a 4/5 split that isolates a specific strategy cluster. The near-universal success confirms that domain-relevant binary classification---not specific label semantics---drives cross-attack generalization on template attacks. The AA outlier is consistent with the complexity-dependent boundary observed in Section~\ref{sec:decomposition}: structurally complex attacks are sensitive to specific partition choices while template attacks are not.
361	
362	\subsection{Topic Classification Failure Analysis}
363	
364	\begin{table}[ht]
365	\centering
366	\footnotesize
367	\caption{Per-turn Fisher ratio (mean across all dimensions) and silhouette score between jailbreak and benign turn embeddings (\texttt{[CLS]} representations). Higher values indicate greater per-turn separability.}
368	\label{tab:topic_failure}
369	\begin{tabular}{@{}llcc@{}}
370	\toprule
371	\textbf{Model} & \textbf{Dataset} & \textbf{Fisher (mean)} & \textbf{Silhouette} \\
372	\midrule
373	Vanilla  & IID test & 0.118 & 0.034 \\
374	Vanilla  & DD OOD  & 0.401 & 0.411 \\
375	Vanilla  & AA OOD  & 0.408 & 0.330 \\
376	\midrule
377	9-class DAPT & IID test & 0.073 & 0.048 \\
378	9-class DAPT & DD OOD  & 0.200 & 0.079 \\
379	9-class DAPT & AA OOD  & 0.832 & 0.301 \\
380	\midrule
381	Topic DAPT & IID test & 0.108 & 0.076 \\
382	Topic DAPT & DD OOD  & 0.653 & 0.274 \\
383	Topic DAPT & AA OOD  & 0.311 & 0.141 \\
384	\bottomrule
385	\end{tabular}
386	\end{table}
387	
388	Topic DAPT achieves \emph{higher} per-turn Fisher separability than 9-class DAPT on IID and DD (0.653 vs.\ 0.200 on DD) yet produces far worse conversation-level detection (F1\,=\,0.541 vs.\ 0.994). This rules out per-turn separability destruction as the failure mechanism. The 9-class model instead greatly expands the embedding space (centroid $L_2$ distance 7.5--27.6 vs.\ 0.9--1.1 for vanilla) while distributing both classes broadly, creating richer representation geometry that the downstream GRU exploits over the turn sequence. Topic classification teaches features that separate turns individually but are temporally inconsistent across a conversation---high per-turn separability does not guarantee that the GRU can learn a stable conversation-level decision boundary.
389	
390	\section{Reproducibility Details}
391	\label{sec:reproducibility}
392	
393	\paragraph{Stage-1 training.}
394	All variants use DeBERTa-v3-base (184M parameters) with learning rate $2 \times 10^{-5}$, AdamW optimizer ($\beta_1$=0.9, $\beta_2$=0.999, weight decay 0.01), linear warmup over the first 10\% of steps, batch size 16, and 4 epochs. MLM variants use 15\% random token masking. Training takes approximately 30 minutes per variant on a single NVIDIA A100 (40GB).
395	
396	\paragraph{Stage-2 training.}
397	The BiGRU has hidden dimension 256, 2 layers, and dropout 0.3 (bidirectional, so output dimension 512). The MLP classifier has layers $512 \to 256 \to 2$ with ReLU activation. Training uses learning rate $1 \times 10^{-3}$, Adam optimizer, batch size 32, and 20 epochs with early stopping (patience 5) on validation F1. Stage-2 training completes in under 5 minutes per variant.
398	
399	\paragraph{Data generation.}
400	Jailbreak conversations are generated using Qwen3-8B with attack-specific prompt templates. Crescendo conversations follow a 5--8 turn gradual escalation structure. FITD conversations use a 2--3 turn commitment-consistency structure. Deceptive Delight conversations embed harmful content within emotionally engaging 3--5 turn sequences. Benign conversations are generated with topic-anchored prompts across five domains (technology, health, finance, education, general) with matched turn counts.
401	
402	\paragraph{Strategy annotation.}
403	Each user turn is annotated by Qwen3-8B using a structured prompt that provides definitions and two examples for each of the nine strategy categories. The prompt instructs the model to output a single category label. We plan to release all generation and annotation prompts, the full dataset, and training code upon acceptance.
404	
405	\paragraph{Adversarial paraphrasing.}
406	The paraphrased test set is generated by instructing Qwen3-8B to rephrase each user turn while preserving the communicative intent. The resulting paraphrases have mean BERTScore 0.92 and mean lexical overlap 0.20 with the originals. These metrics confirm substantial surface-level variation.
407	
408	\paragraph{Cross-checkpoint variance.}
409	To disentangle Stage-1 from Stage-2 variance, we evaluate three independently trained 9-class DAPT checkpoints (seeds 42, 123, 456) with a fixed downstream BiGRU seed (42). Results: IID F1\,=\,1.000$\pm$0.000, DD OOD\,=\,0.926$\pm$0.026, AA OOD\,=\,0.935$\pm$0.013. Stage-1 training is stable (OOD std\,$\leq$\,2.6\,pp), confirming that the variance reported in the main paper is not dominated by Stage-1 initialization.
410	
411	\section{End-to-End Fine-Tuning Upper Bound}
412	\label{app:e2e}
413	
414	\begin{table}[ht]
415	\centering
416	\footnotesize
417	\caption{Frozen probing vs.\ end-to-end (E2E) fine-tuning for DeBERTa-v3-base 9-class (3-seed mean$\pm$std). E2E unfreezes the Stage-1 encoder during Stage-2 training. Frozen values use main-experiment checkpoints (matching Tables~\ref{tab:main_results}--\ref{tab:evidence_hierarchy}); Table~\ref{tab:frozen_verify} uses plan\_002 checkpoints, yielding higher frozen accuracy (DD\,=\,.997, AA\,=\,.972) and a narrower E2E gap ($\leq$2.5\,pp).}
418	\label{tab:e2e}
419	\begin{tabular}{@{}lccc@{}}
420	\toprule
421	\textbf{Config} & IID & DD OOD & AA OOD \\
422	\midrule
423	Frozen probing & 1.000$\pm$.000 & .994$\pm$.005 & .939$\pm$.047 \\
424	E2E fine-tuning & 1.000$\pm$.000 & 1.000$\pm$.000 & \textbf{.997$\pm$.005} \\
425	\midrule
426	$\Delta$ & .000 & +.006 & +.058 \\
427	\bottomrule
428	\end{tabular}
429	\end{table}
430	
431	End-to-end fine-tuning unfreezes the Stage-1 encoder during Stage-2 BiGRU training, allowing gradient flow through the full pipeline. On IID and OOD DD, the two configurations are indistinguishable; on structurally complex ActorAttack, E2E recovers +5.8\,pp. The modest gain confirms that frozen probing captures the vast majority of discriminative information encoded by Stage-1 DAPT, and that the remaining OOD gap in the frozen setting reflects downstream optimization constraints rather than missing representational capacity.
432	
433	\section{Real-World False Positive Rate}
434	\label{app:wildchat_fpr}
435	
436	\begin{table}[ht]
437	\centering
438	\footnotesize
439	\caption{False positive rate (\%) on 226 WildChat benign multi-turn conversations (GPT-3.5 users, avg 7.4 turns per conversation). All models trained on synthetic Qwen3-8B data (1{,}000-conversation scale). 3-seed mean$\pm$std.}
440	\label{tab:wildchat_fpr}
441	\begin{tabular}{@{}lcccc@{}}
442	\toprule
443	\textbf{Variant} & Seed 42 & Seed 123 & Seed 456 & Mean$\pm$Std \\
444	\midrule
445	9-class & 66.8 & 61.1 & 76.5 & 68.1$\pm$6.4 \\
446	MLM & 36.7 & 64.6 & 32.3 & 44.5$\pm$14.3 \\
447	Vanilla & 47.3 & 42.5 & 54.4 & 48.1$\pm$4.9 \\
448	\bottomrule
449	\end{tabular}
450	\end{table}
451	
452	Table~\ref{tab:wildchat_fpr} evaluates false positive rates on 226 WildChat benign multi-turn conversations from real GPT-3.5 users (avg 7.4 turns). All variants produce FPR far exceeding deployable thresholds: 9-class is worst at 68.1\%, followed by vanilla (48.1\%) and MLM (44.5\%). Domain adaptation \emph{increases} FPR relative to vanilla (+20\,pp for 9-class), indicating that continued pretraining amplifies dependence on the training benign distribution. This is consistent with the cross-LLM false positive spike (Table~\ref{tab:cross_llm_error}): models trained on synthetic Qwen3-8B benign text implicitly treat unfamiliar conversational styles as jailbreak indicators. High MLM seed variance (std\,=\,14.3\%) suggests that unsupervised pretraining is particularly unstable under benign distribution shift. Deployment requires per-domain benign calibration or mixed-source benign training data.
453	
454	\paragraph{Post-hoc calibration.}
455	ROC AUC\,=\,0.700$\pm$0.054 indicates insufficient discrimination between WildChat benign and jailbreak conversations at the representation level. At TPR$\geq$95\%, the optimal threshold still yields FPR\,=\,62.7\%, far above deployable levels. Temperature scaling cannot improve this trade-off, as ROC curves are invariant to monotonic score transforms. The AUC ceiling reflects genuine domain shift: WildChat benign and jailbreak representations overlap substantially, and no post-hoc calibration can overcome this; in-domain benign adaptation is required.
456	
457	\paragraph{Second benign source: OASST2.}
458	\label{app:oasst2}
459	
460	To test whether benign-side shift generalizes beyond WildChat, we evaluate on 200 benign multi-turn conversations from OpenAssistant OASST2~\citep{kopf2023openassistant}---a crowdsourced dataset of real human conversations, distinct from WildChat (GPT-3.5 user logs) in both authorship and topic distribution.
461	
462	\begin{table}[ht]
463	\centering
464	\footnotesize
465	\caption{OASST2 benign adaptation curve: FPR on 200 OASST2 benign conversations and OOD jailbreak detection F1 as a function of $N$ OASST2 conversations added to training. Seed 42. Compare WildChat (Table~\ref{tab:wildchat_fpr}): FPR reaches 0\% at $N$\,=\,10.}
466	\label{tab:oasst2_curve}
467	\begin{tabular}{@{}rccccc@{}}
468	\toprule
469	$N$ & FPR (\%) & IID F1 & DD F1 & AA F1 & FITD F1 \\
470	\midrule
471	0 & 57.5 & -- & -- & -- & -- \\
472	10 & 20.5 & 1.000 & 1.000 & 1.000 & 1.000 \\
473	25 & \textbf{1.5} & 1.000 & 1.000 & 0.953 & 1.000 \\
474	50 & \textbf{0.5} & 1.000 & 1.000 & 0.990 & 1.000 \\
475	\bottomrule
476	\end{tabular}
477	\end{table}
478	
479	Baseline FPR on OASST2 (57.5\%) is comparable to WildChat (68.1\%), confirming that benign-side shift is not source-specific but a general consequence of synthetic-only benign training. The adaptation curve follows the same pattern---monotonic FPR reduction with preserved OOD detection---but requires more samples: 25 conversations reduce FPR to 1.5\% (vs.\ 0\% at $N$\,=\,10 for WildChat), and 50 conversations reach 0.5\%. The slower convergence likely reflects greater distributional distance between crowdsourced OASST2 conversations and the synthetic training distribution compared to WildChat's GPT-3.5 user logs.
480	
481	\subsection{Estimated Dual-OOD Detection Performance}
482	\label{app:dual_ood}
483	
484	The OOD detection F1 reported in the main paper evaluates attack-side OOD with IID benign examples (FPR\,=\,0), providing an upper bound. To estimate performance when \emph{both} attack and benign inputs are OOD, we combine per-seed attack recall (from OOD evaluation) with per-seed benign FPR (from WildChat/OASST2 experiments), assuming independence between attack detection and benign false positives. For each seed, we compute binary detection F1 from the resulting TP, FP, FN counts on the OOD test composition (80 jailbreak + 38 benign).
485	
486	\begin{table}[ht]
487	\centering
488	\footnotesize
489	\caption{Estimated dual-OOD binary detection F1 under different benign conditions (3-seed mean$\pm$std). Attack recall held fixed from OOD evaluation; only benign FPR varies. IID row corresponds to the benign-IID upper bound (FPR\,=\,0).}
490	\label{tab:dual_ood}
491	\begin{tabular}{@{}lcc@{}}
492	\toprule
493	\textbf{Benign condition} & DD OOD F1 & AA OOD F1 \\
494	\midrule
495	IID (FPR\,=\,0) & .994$\pm$.009 & .981$\pm$.019 \\
496	WildChat, no adapt & .855$\pm$.020 & .842$\pm$.012 \\
497	OASST2, no adapt & .874$\pm$.009 & .861$\pm$.018 \\
498	WildChat + 10-shot & .994$\pm$.009 & .981$\pm$.019 \\
499	OASST2 + 25-shot & .991$\pm$.009 & .978$\pm$.018 \\
500	\bottomrule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d244864-cfe8-44ba-a791-68d2fbdd7d03",
  "isSidechain": true,
  "promptId": "8fdf9905-2713-48d3-8d3b-5ec87cb90759",
  "agentId": "afb4a04fbc67e538a",
  "type": "user",
  "uuid": "0e77714a-9598-4b22-b715-31417648aafc",
  "sourceToolAssistantUUID": "2d244864-cfe8-44ba-a791-68d2fbdd7d03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-24T05:18:44.923Z_

Now I'll search for all occurrences of the four numbers across all three files to create a complete picture:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e77714a-9598-4b22-b715-31417648aafc",
  "isSidechain": true,
  "agentId": "afb4a04fbc67e538a",
  "requestId": "req_011CbLq2jmBJs4t3H7ky9dhi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "531250a5-3543-4492-8ded-54cb98bcefe3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011Zw5hZqxvYRLwyMcJnFzWc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 14099,
      "cache_read_input_tokens": 69964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14099,
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

_source line 13 · 2026-05-24T05:18:46.018Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01WB2B96Q8nwRU8agWJLoVYV`</summary>

```json
{
  "pattern": "3\\.7|9\\.4|2\\.5|57\\.9",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "531250a5-3543-4492-8ded-54cb98bcefe3",
  "isSidechain": true,
  "agentId": "afb4a04fbc67e538a",
  "requestId": "req_011CbLq2jmBJs4t3H7ky9dhi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b3ee197e-bedd-443a-9e0b-93bc2ae7fae3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011Zw5hZqxvYRLwyMcJnFzWc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 14099,
      "cache_read_input_tokens": 69964,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14099
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 143,
          "cache_read_input_tokens": 69964,
          "cache_creation_input_tokens": 14099,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14099,
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

_source line 14 · 2026-05-24T05:18:46.045Z_

<details><summary>↩ Tool result · `toolu_01WB2B96Q8nwRU8agWJLoVYV`</summary>

```text
Found 6 files
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.fdb_latexmk
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.aux
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/acl.sty
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3ee197e-bedd-443a-9e0b-93bc2ae7fae3",
  "isSidechain": true,
  "promptId": "8fdf9905-2713-48d3-8d3b-5ec87cb90759",
  "agentId": "afb4a04fbc67e538a",
  "type": "user",
  "uuid": "fe6b1292-bb74-4a6a-8da5-f6b31732bb81",
  "sourceToolAssistantUUID": "b3ee197e-bedd-443a-9e0b-93bc2ae7fae3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-24T05:18:47.786Z_

Let me search more specifically with grep on just the tex files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe6b1292-bb74-4a6a-8da5-f6b31732bb81",
  "isSidechain": true,
  "agentId": "afb4a04fbc67e538a",
  "requestId": "req_011CbLq2xc67EmtJwdou3Bmv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4cf78ca5-71e9-40af-94f1-cd5c0d06c9fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VCGJPXHDaJgminH5e9UpAK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 421,
      "cache_read_input_tokens": 84063,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 421,
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

_source line 16 · 2026-05-24T05:18:48.232Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01LqcwaWpkpPTQR8uNAQGKfM`</summary>

```json
{
  "pattern": "3\\.7|9\\.4|2\\.5|57\\.9",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "context": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cf78ca5-71e9-40af-94f1-cd5c0d06c9fc",
  "isSidechain": true,
  "agentId": "afb4a04fbc67e538a",
  "requestId": "req_011CbLq2xc67EmtJwdou3Bmv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "450be238-9f3c-4b48-a89e-7dd2a1dab86b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VCGJPXHDaJgminH5e9UpAK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 421,
      "cache_read_input_tokens": 84063,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 421
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 187,
          "cache_read_input_tokens": 84063,
          "cache_creation_input_tokens": 421,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 421,
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

_source line 17 · 2026-05-24T05:18:48.252Z_

<details><summary>↩ Tool result · `toolu_01LqcwaWpkpPTQR8uNAQGKfM`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex-13-\paragraph{Discriminative compression and label equivalence.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex-14-Three observations argue against a topic shortcut: unstable topic OOD (F1\,=\,0.541$\pm$0.207), scrambled labels within 3.9\,pp, and label-free MLM detection (F1\,$\geq$\,0.97 at $K \leq 5$).
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex:15:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex-16-
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex-17-\paragraph{Cross-condition transfer and boundaries.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex-19-
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex-20-\paragraph{Length as a potential confound.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex:21:Length-matched evaluation ($N$=155) shows negligible change (DD $\Delta$\,=\,$-$2.5\,pp); the $-$57.9\,pp ActorAttack collapse under benign-turn padding (Appendix~\ref{app:length_independence}) reflects signal density dilution rather than length shortcut removal.
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex-22-
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex-23-\section{Conclusion}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-415-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-416-\footnotesize
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex:417:\caption{Frozen probing vs.\ end-to-end (E2E) fine-tuning for DeBERTa-v3-base 9-class (3-seed mean$\pm$std). E2E unfreezes the Stage-1 encoder during Stage-2 training. Frozen values use main-experiment checkpoints (matching Tables~\ref{tab:main_results}--\ref{tab:evidence_hierarchy}); Table~\ref{tab:frozen_verify} uses plan\_002 checkpoints, yielding higher frozen accuracy (DD\,=\,.997, AA\,=\,.972) and a narrower E2E gap ($\leq$2.5\,pp).}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-418-\label{tab:e2e}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-419-\begin{tabular}{@{}lccc@{}}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-445-9-class & 66.8 & 61.1 & 76.5 & 68.1$\pm$6.4 \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-446-MLM & 36.7 & 64.6 & 32.3 & 44.5$\pm$14.3 \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex:447:Vanilla & 47.3 & 42.5 & 54.4 & 48.1$\pm$4.9 \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-448-\bottomrule
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-449-\end{tabular}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-569-\end{table}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-570-
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex:571:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-572-
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-573-[Omitted long context line]
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-624-Topic & 14.5 & 0.012 & 0.371 \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-625-Scrambled & 7.8 & 2.60 & 0.283 \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex:626:9-class & 9.4 & 4.47 & 0.303 \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex:627:Binary & 3.7 & 19.7 & 0.239 \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-628-\bottomrule
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-629-\end{tabular}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-737-\textbf{Dataset} & \textbf{Variant} & 1--3 turns & 4--6 turns & 7--10 turns \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-738-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex:739:\multirow{2}{*}{DD OOD} & 9-class & --- & 100.0\% & 99.4\% \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-740-& Vanilla & --- & $\leq$2.6\% & $\leq$1.7\% \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-741-\midrule
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-780-\multicolumn{4}{l}{\textit{Part C: Jailbreak padding to 15+ turns}} \\[2pt]
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-781-& DD original & F1 = .996 & 80 \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex:782:& DD padded & F1 = .971 ($\Delta$=$-$2.5\,pp) & 80 \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-783-& AA original & F1 = .963 & 80 \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex:784:& AA padded & F1 = .383$\pm$.261 ($\Delta$=$-$57.9\,pp) & 80 \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-785-\bottomrule
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-786-\end{tabular}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-793-WildChat FPR by turn count (Part~B) provides complementary evidence: short conversations (3--10 turns, $n$=196) have \emph{lower} FPR than medium-length ones (11--15 turns, $n$=23), inconsistent with a ``short\,=\,jailbreak'' shortcut. Medium and long buckets have limited sample sizes and should be interpreted as directional evidence only.
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-794-
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex:795:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-796-
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex-797-\section{Inference Efficiency}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "450be238-9f3c-4b48-a89e-7dd2a1dab86b",
  "isSidechain": true,
  "promptId": "8fdf9905-2713-48d3-8d3b-5ec87cb90759",
  "agentId": "afb4a04fbc67e538a",
  "type": "user",
  "uuid": "3587a106-f3f1-4bb4-bdc0-9827045d410c",
  "sourceToolAssistantUUID": "450be238-9f3c-4b48-a89e-7dd2a1dab86b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-24T05:18:56.801Z_

Perfect. Now I have all the information. Let me compile the findings:

## Numbers Found: Location & Context

**3.7** — Appears in **appendix.tex** (line 627), NOT in conclusion.tex or experiments.tex
- **Sentence**: Table caption/row in participation ratio table for "Binary" variant
- **Refers to**: Participation ratio (dimension concentration metric) for Binary classifier variant
- **Also appears**: Mentioned in conclusion.tex line 15 as part of range "3.7--9.4" (participation ratios for classification DAPT)

**9.4** — Appears in **both conclusion.tex and appendix.tex**
- **Conclusion.tex (line 15)**: "Classification DAPT compresses features into few dimensions (participation ratio 3.7--9.4 vs.\ 25--32; Figure~\ref{fig:svd_subspace}; Appendix~\ref{app:representation})"
- **Appendix.tex (line 626)**: Table row for "9-class" variant showing participation ratio = 9.4
- **Refers to**: Maximum participation ratio (feature dimension concentration) achieved by classification DAPT methods, compared to vanilla's 25--32

**2.5** — Appears in **both conclusion.tex and appendix.tex**
- **Conclusion.tex (line 21)**: "Length-matched evaluation ($N$=155) shows negligible change (DD $\Delta$\,=\,$-$2.5\,pp)"
- **Appendix.tex (line 782)**: "DD padded & F1 = .971 ($\Delta$=$-$2.5\,pp) & 80"
- **Refers to**: F1 degradation (percentage points) when DD OOD examples are padded with benign turns; marked as negligible
- **Also appears in**: Appendix.tex line 417 as "narrower E2E gap ($\leq$2.5\,pp)" in table caption

**57.9** — Appears in **both conclusion.tex and appendix.tex**
- **Conclusion.tex (line 21)**: "the $-$57.9\,pp ActorAttack collapse under benign-turn padding (Appendix~\ref{app:length_independence})"
- **Appendix.tex (line 784)**: "AA padded & F1 = .383$\pm$.261 ($\Delta$=$-$57.9\,pp) & 80"
- **Refers to**: Massive F1 degradation when ActorAttack examples are padded to 15+ turns with benign text; reflects signal density dilution
- **NOT in experiments.tex** (experiments.tex discusses other metrics but not this length-independence ablation)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3587a106-f3f1-4bb4-bdc0-9827045d410c",
  "isSidechain": true,
  "agentId": "afb4a04fbc67e538a",
  "requestId": "req_011CbLq389KiXtWe7GEggPRc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2df97c82-1dde-413c-89b2-a9d8c422a19a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/director_32e62753",
  "sessionId": "d0343bc5-105f-48da-b75b-2236f7e1bb2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NYfLfVfVKDBd8gNcxknFZq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 3415,
      "cache_read_input_tokens": 84484,
      "output_tokens": 655,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3415
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 655,
          "cache_read_input_tokens": 84484,
          "cache_creation_input_tokens": 3415,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3415,
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
