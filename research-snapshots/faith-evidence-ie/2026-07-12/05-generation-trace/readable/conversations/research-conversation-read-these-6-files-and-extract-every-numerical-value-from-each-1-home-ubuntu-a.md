# Research conversation: Read these 6 files and extract EVERY numerical value from each: 1. /home/ubuntu/.agent-ml-research-idea_gen_0513_6/proje

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a8128c193ad4a3e6b.jsonl`
- **Structured JSON:** [`2923dd9c75f14620ae35.json`](../../sessions/29/2923dd9c75f14620ae35.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

15 recorded events

### User

_source line 1 · 2026-05-25T19:42:14.458Z_

Read these 6 files and extract EVERY numerical value from each:
1. /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex
2. /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex
3. /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex
4. /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex
5. /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex
6. /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex

For each number, report the exact value, filename, line number, and what it represents. Be exhaustive - include all percentages, counts, correlation coefficients, p-values, model sizes, parameter counts, everything.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "00884a06-3250-4c87-b491-3b7baf3c5516",
  "agentId": "a8128c193ad4a3e6b",
  "type": "user",
  "uuid": "d538c7ee-3812-4d00-b4fd-5b5dd66d217e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "7a362cc0-08ac-4cf8-8958-672775de0ebd",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "sprightly-popping-church"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-25T19:42:16.786Z_

I'll read all 6 files and extract every numerical value with its context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d538c7ee-3812-4d00-b4fd-5b5dd66d217e",
  "isSidechain": true,
  "agentId": "a8128c193ad4a3e6b",
  "requestId": "req_011CbPrgtwWp5AUBrQAVXGQr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "45a88aa7-ed57-4899-a271-ca5a48f7c5ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "7a362cc0-08ac-4cf8-8958-672775de0ebd",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "sprightly-popping-church",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01THtxoDrfucHbMKE7TgBqod",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 726,
      "cache_read_input_tokens": 39102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 726,
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

_source line 3 · 2026-05-25T19:42:17.012Z_

<details open><summary>🔧 Tool call — Read · `toolu_019JkeXe1CadXk8DpEppmuyD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45a88aa7-ed57-4899-a271-ca5a48f7c5ee",
  "isSidechain": true,
  "agentId": "a8128c193ad4a3e6b",
  "requestId": "req_011CbPrgtwWp5AUBrQAVXGQr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "63cb88be-0565-42f4-bcfa-31195f5a56bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "7a362cc0-08ac-4cf8-8958-672775de0ebd",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "sprightly-popping-church",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01THtxoDrfucHbMKE7TgBqod",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 726,
      "cache_read_input_tokens": 39102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 726,
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

_source line 4 · 2026-05-25T19:42:17.018Z_

<details><summary>↩ Tool result · `toolu_019JkeXe1CadXk8DpEppmuyD`</summary>

```text
1	\begin{abstract}
2	Large Language Model (LLM)-based Document-level Relation Extraction (DocRE) now matches or exceeds encoder baselines in extraction accuracy, yet outputs bare relation triplets without identifying supporting sentences. Encoder-based evidence methods (SAIS, DREEAM) provide evidence but trail LLM approaches in accuracy, creating a gap between extraction performance and verifiability. We study evidence-grounded DocRE as structured generation and compare Group Relative Policy Optimization (GRPO), Direct Preference Optimization (DPO), and Rejection Sampling Fine-Tuning (RSFT) across three fully evaluated scales (1.7B, 4B, 8B) with 14B validation, two model families, and two datasets. The evidence tax (extraction cost of generating evidence) is scale-dependent: beneficial at 1.7B ($-$5.63pp dev Ign-F1) but approximately neutral at $\geq$4B (+0.25$\pm$0.47pp at 4B; positive $=$ cost). Gradient-based optimization amplifies evidence-extraction competition (GRPO catastrophic, DPO gradual), while RSFT with NLI-based scoring avoids decoupling through output filtering rather than gradient pressure. We define the Evidence-Decoupling Ratio (EDCR) to quantify extraction-evidence misalignment, validated at per-relation level ($\rho{=}{-}0.79$, $n{=}76$, $p{<}0.001$). Our 1.7B RSFT model (51.19 Ign-F1) approaches 8B Supervised Fine-Tuning (SFT) performance (50.19) at 4.7$\times$ fewer parameters. Test-set evaluation preserves model ranking across all scales (Spearman $\rho{=}1.0$)\footnote{Code and data are available at \url{https://anonymous.4open.science/r/faith-evidence-ie-18BD/}.}.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63cb88be-0565-42f4-bcfa-31195f5a56bf",
  "isSidechain": true,
  "promptId": "00884a06-3250-4c87-b491-3b7baf3c5516",
  "agentId": "a8128c193ad4a3e6b",
  "type": "user",
  "uuid": "e21e2da9-0a02-4733-ab8d-9f42385bc1f4",
  "sourceToolAssistantUUID": "63cb88be-0565-42f4-bcfa-31195f5a56bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "7a362cc0-08ac-4cf8-8958-672775de0ebd",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "sprightly-popping-church"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-25T19:42:17.214Z_

<details open><summary>🔧 Tool call — Read · `toolu_011LxqeYsyr5y7AAVUDsYiC5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e21e2da9-0a02-4733-ab8d-9f42385bc1f4",
  "isSidechain": true,
  "agentId": "a8128c193ad4a3e6b",
  "requestId": "req_011CbPrgtwWp5AUBrQAVXGQr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "557dae11-6ec5-429f-95dc-68d190232cff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "7a362cc0-08ac-4cf8-8958-672775de0ebd",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "sprightly-popping-church",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01THtxoDrfucHbMKE7TgBqod",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 726,
      "cache_read_input_tokens": 39102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 726,
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

_source line 6 · 2026-05-25T19:42:17.219Z_

<details><summary>↩ Tool result · `toolu_011LxqeYsyr5y7AAVUDsYiC5`</summary>

```text
1	\section{Introduction}
2	
3	Document-level relation extraction (DocRE) requires identifying semantic relations between entity pairs across multiple sentences, a task where encoder-based methods such as \citet{zhou2021atlop} long dominated.
4	Recent LLM-based approaches have closed this gap: \citet{autore2024} fine-tune LLMs with structured decomposition, \citet{xu2024lmrc} frame it as multi-choice reading comprehension, and \citet{xu2025docksrag} combine retrieval-augmented generation with structured knowledge.
5	These methods approach or surpass encoder baselines on DocRED \citep{yao2019docred} and Re-DocRED \citep{tan2022redocred} in extraction accuracy, yet every one outputs bare relation triplets $(e_h, r, e_t)$ without indicating \emph{which sentences} support each prediction.
6	Without evidence, a clinician reviewing a ten-page case report must manually locate the sentences that support each extracted drug interaction, a bottleneck that undermines trust in automated extraction.
7	
8	\begin{figure*}[!t]
9	\centering
10	\includegraphics[width=0.92\textwidth]{fig_overview.pdf}
11	\vspace{-2mm}
12	\caption{Evidence-grounded DocRE produces relation triples with supporting sentence indices, unlike standard DocRE which outputs bare triples. RSFT selects the top-$k$ of $N$ CED-scored candidates per document for fine-tuning.}
13	\label{fig:overview}
14	\end{figure*}
15	
16	Encoder-based methods have partially addressed this need: \citet{xiao2022sais} introduce sentence-level evidence supervision as an auxiliary signal, and \citet{ma2023dreeam} extend this with dynamic evidence retrieval through memory attention.
17	Both produce evidence and improve extraction, but encoder methods now trail LLM-based approaches in accuracy.
18	The community faces a gap: the most accurate extractors provide no evidence, while evidence-capable methods are no longer competitive.
19	
20	This gap reflects a structural difference.
21	In encoder methods, evidence retrieval is classification that regularizes the encoder at negligible cost; in LLM-based DocRE, evidence requires the model to \emph{generate} additional output tokens per triple, increasing output length and decoding complexity.
22	The na\"{i}ve expectation is that this generation cost always harms extraction accuracy.
23	Our experiments show this expectation is wrong.
24	The evidence tax (Ign-F1(no-evidence) minus Ign-F1(with-evidence), so positive values indicate cost and negative values indicate benefit) is not a fixed penalty but a landscape shaped by model capacity, optimization paradigm, and training data quality.
25	Within the Qwen3 family, evidence generation \emph{benefits} extraction at 1.7B ($-$5.63pp Ign-F1, partly through halving output duplication) but is approximately neutral at $\geq$4B (+0.25$\pm$0.47pp at 4B).
26	Gradient-based optimization amplifies this competition, as GRPO collapses extraction under constrained precision and DPO progressively trades extraction for evidence, while discrete sample selection (RSFT) avoids the trade-off entirely by filtering outputs rather than pushing gradients. To quantify this decoupling, we define the Evidence-Decoupling Ratio (EDCR), a diagnostic metric that measures the fraction of cited evidence not supported by gold annotations.
27	
28	We study evidence-grounded DocRE as a structured generation task and compare three post-training paradigms across three fully evaluated scales (1.7B, 4B, 8B) with 14B validation, two model families, and two datasets: Group Relative Policy Optimization (GRPO) \citep{shao2024deepseekmath}, Direct Preference Optimization (DPO) \citep{rafailov2023direct}, and Rejection Sampling Fine-Tuning (RSFT), building on Self-Taught Reasoner (STaR) \citep{zelikman2022star}. Our contributions:
29	\begin{enumerate}[itemsep=1pt,parsep=0pt,topsep=2pt,partopsep=0pt,leftmargin=*]
30	    \item \textbf{Evidence generation is not uniformly harmful.} We observe a scale-dependent evidence tax with a within-family capacity threshold: beneficial at 1.7B ($-$5.63pp) but approximately neutral at $\geq$4B (+0.25$\pm$0.47pp at 4B), challenging the assumption that evidence always costs extraction accuracy.
31	    \item \textbf{Gradient pressure causes evidence-extraction decoupling.} We characterize a decoupling spectrum (GRPO catastrophic $\rightarrow$ DPO gradual $\rightarrow$ RSFT none) and introduce the Evidence-Decoupling Ratio (EDCR) as a diagnostic, validated at per-relation level ($\rho{=}{-}0.79$, $n{=}76$, $p{<}0.001$).
32	    \item \textbf{RSFT improves extraction without decoupling.} NLI-based sample selection improves mean Ign-F1 across tested scales (+1.2 to +6.6pp) while maintaining evidence quality. We observe lower cross-seed variance under RSFT at all tested configurations, though this partly reflects shared SFT initialization and is limited by $n{=}3$ seeds (\S\ref{sec:scaling}). Our 1.7B RSFT model (51.19 Ign-F1) approaches 8B SFT performance (50.19) at 4.7$\times$ fewer parameters.
33	\end{enumerate}
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "557dae11-6ec5-429f-95dc-68d190232cff",
  "isSidechain": true,
  "promptId": "00884a06-3250-4c87-b491-3b7baf3c5516",
  "agentId": "a8128c193ad4a3e6b",
  "type": "user",
  "uuid": "58a2fe09-885a-45ca-a0b7-1c21caa5e564",
  "sourceToolAssistantUUID": "557dae11-6ec5-429f-95dc-68d190232cff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "7a362cc0-08ac-4cf8-8958-672775de0ebd",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "sprightly-popping-church"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-25T19:42:17.557Z_

<details open><summary>🔧 Tool call — Read · `toolu_015HZDShFssjHb9AMhSYwycf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58a2fe09-885a-45ca-a0b7-1c21caa5e564",
  "isSidechain": true,
  "agentId": "a8128c193ad4a3e6b",
  "requestId": "req_011CbPrgtwWp5AUBrQAVXGQr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9e021d04-8e8b-4404-a49b-fc9634c32f07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "7a362cc0-08ac-4cf8-8958-672775de0ebd",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "sprightly-popping-church",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01THtxoDrfucHbMKE7TgBqod",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 726,
      "cache_read_input_tokens": 39102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 726,
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

_source line 8 · 2026-05-25T19:42:17.563Z_

<details><summary>↩ Tool result · `toolu_015HZDShFssjHb9AMhSYwycf`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task: Evidence-Grounded Document-Level Relation Extraction}
5	\label{sec:task}
6	
7	Given a document $D = \{s_1, \ldots, s_n\}$ consisting of $n$ sentences and a set of entities $\mathcal{E}$ identified within $D$, the task of evidence-grounded document-level relation extraction (DocRE) requires predicting, for each entity pair $(e_h, e_t) \in \mathcal{E} \times \mathcal{E}$, a relation $r \in \mathcal{R} \cup \{\texttt{NA}\}$ together with a set of supporting evidence sentences $E \subseteq D$. Standard DocRE predicts only the triple $(e_h, r, e_t)$; the evidence-grounded formulation also requires $E$, which grounds each prediction in specific textual support (Figure~\ref{fig:overview}).
8	
9	\begin{figure}[t]
10	\centering
11	\includegraphics[width=\columnwidth]{fig_task_example.pdf}
12	\caption{Evidence-grounded DocRE example. Given a document with entity mentions, the model jointly predicts relation triples and supporting evidence sentences in a single structured output.}
13	\label{fig:task_example}
14	\end{figure}
15	
16	In our LLM-based approach, the model generates structured outputs that jointly encode both components. For each predicted relation, the output follows the format \texttt{(head, relation, tail) | Evidence: [S$i$][S$j$]}, requiring the model to produce complete evidence references inline with each triple rather than as a separate retrieval step. This design contrasts with encoder-based evidence methods such as SAIS~\citep{xiao2022sais} and DREEAM~\citep{ma2023dreeam}, which frame evidence identification as sentence-level binary classification. Because classification over a fixed sentence set does not increase output length, these methods incur no generation overhead. Our LLM formulation requires additional tokens for each evidence reference, creating a generation burden that scales with the number of predicted triples and their evidence sentences. This scale-dependent cost is the central phenomenon we investigate.
17	
18	
19	\subsection{Supervised Fine-Tuning Baseline}
20	\label{sec:sft}
21	
22	We fine-tune all models with Low-Rank Adaptation (LoRA) \citep{hu2022lora} at rank $r{=}64$ and scaling factor $\alpha{=}128$, applied to all linear projections (attention and feed-forward). The training data consists of DocRED~\citep{yao2019docred} training documents converted to the structured output format described above, where each example maps a document and its entity set to the complete set of relation triples with evidence annotations. We also train a \emph{no-evidence} variant under identical configuration but with evidence references removed from the output format, producing only \texttt{(head, relation, tail)}. This variant serves as an upper bound on extraction performance by eliminating the generation cost of evidence, and allows direct measurement of the evidence tax at each model scale. Detailed hyperparameters are reported in Appendix~\ref{sec:hyperparams}.
23	
24	
25	\subsection{Optimization Paradigms}
26	\label{sec:paradigms}
27	
28	We evaluate three post-SFT optimization paradigms that differ in how they incorporate quality signals from the CED scoring function (\S\ref{sec:ced}). Table~\ref{tab:paradigm_comparison} summarizes their key differences.
29	
30	\begin{table}[t]
31	\centering
32	\caption{Comparison of post-SFT optimization paradigms. All three use CED scoring but differ in how quality signals reach the model.}
33	\label{tab:paradigm_comparison}
34	\small
35	\begin{tabular}{lccc}
36	\toprule
37	& \textbf{GRPO} & \textbf{DPO} & \textbf{RSFT} \\
38	\midrule
39	Signal type & Online RL & Implicit RL & Selection \\
40	CED role & Reward & Preference & Filter \\
41	Update & Gradient & Gradient & Supervised \\
42	Decoupling & Yes & Partial & None \\
43	\bottomrule
44	\end{tabular}
45	\end{table}
46	
47	\paragraph{GRPO.}
48	Group Relative Policy Optimization~\citep{shao2024deepseekmath} is an online RL method that eliminates the need for a separate value network by computing advantages within groups of sampled outputs. For each training document, the policy generates $G$ candidate responses, which are scored by CED. The advantage of each response is computed relative to the group mean, and the policy is updated to increase the probability of above-average outputs. We test two configurations: QLoRA \citep{dettmers2023qlora} under 4-bit quantization, and bf16 full-precision LoRA, both with $G{=}8$ groups. Because GRPO applies gradient updates that directly optimize the reward signal, evidence quality and extraction accuracy compete for gradient capacity. We analyze this multi-objective tension in Section~\ref{sec:spectrum}.
49	
50	\paragraph{DPO.}
51	Direct Preference Optimization~\citep{rafailov2023direct} reformulates RLHF~\citep{ouyang2022instructgpt} as a classification problem over preference pairs, without explicit reward models. We construct preference data from the SFT model's sampled outputs: for each document, the response with the highest CED score is labeled as preferred and the lowest-scoring response as rejected. DPO then adjusts the policy to increase the log-probability ratio between preferred and rejected completions. We train for 1 and 3 epochs to observe the temporal dynamics of evidence-extraction trade-offs under implicit optimization.
52	
53	\paragraph{RSFT.}
54	Rejection Sampling Fine-Tuning is a single-round variant of iterative self-improvement methods such as STaR~\citep{zelikman2022star}. The procedure is straightforward: for each SFT checkpoint, the corresponding model generates $N{=}8$ candidate outputs per training document, each candidate is scored by CED, and only the top-$k{=}1$ response is retained as training data. In our primary experiments (4B, 8B, LLaMA-8B), all RSFT seeds share the same SFT s42 checkpoint and the same CED-scored training data; only the LoRA initialization and data shuffling seeds differ during the final fine-tuning stage. At 14B, seed-matched SFT checkpoints are used. We use $k{=}1$ (best-of-$N$) selection throughout all experiments, selecting the single highest-scoring candidate per document. This yields approximately 3,000 training examples per model (one per document; exact counts vary slightly by model due to generation failures). Unlike GRPO and DPO, RSFT does not apply gradient-based optimization pressure toward a reward signal. Instead, it improves training data quality through filtering: the model trains on its own best outputs rather than all outputs. This distinction is critical because discrete selection over complete outputs cannot exploit the extraction-evidence trade-off that gradient methods find. The contribution of RSFT in our setting is not the framework itself, which is well-established, but its application to evidence-grounded DocRE with CED as a domain-specific quality filter.
55	
56	
57	\subsection{Contrastive Evidence Discrimination}
58	\label{sec:ced}
59	
60	\begin{figure}[t]
61	\centering
62	\includegraphics[width=\columnwidth]{fig_ced_scoring.pdf}
63	\caption{CED scoring example. The positive pair (evidence $\to$ hypothesis) yields high entailment; the contrastive distractor (entity-sharing non-evidence) yields low entailment. CED measures the margin between them.}
64	\label{fig:ced_scoring}
65	\end{figure}
66	
67	CED is a scoring function that evaluates the faithfulness of predicted evidence sentences to their associated relation triples. It builds on Natural Language Inference (NLI) to measure whether evidence actually entails the predicted relation, rather than merely co-occurring with the relevant entities.
68	
69	For a predicted triple $(e_h, r, e_t)$ with evidence sentences $E$, CED constructs a positive NLI pair: the premise is the concatenation of sentences in $E$, and the hypothesis is a natural-language verbalization of the relation (e.g., ``$e_h$ has relation $r$ with $e_t$''). An NLI model based on DeBERTaV3 \citep{he2023debertav3} (\texttt{cross-encoder/nli-deberta-v3-base}) produces an entailment probability $p^+$ for this pair. The contrastive component introduces hard negatives drawn from the same document. For each triple, we collect sentences that mention $e_h$ or $e_t$ but are not in the predicted evidence set. These entity-sharing distractors serve as negative premises, and the NLI model scores each to obtain $p^-_1, \ldots, p^-_m$. The CED score for a single triple is:
70	\begin{equation}
71	\text{CED}(e_h, r, e_t, E) = p^+ - \max_j \, p^-_j
72	\label{eq:ced}
73	\end{equation}
74	This formulation forces the scoring function to distinguish sentences that genuinely support the relation from sentences that merely mention the same entities. A high CED score indicates that the evidence provides relation-specific support beyond entity co-occurrence.
75	
76	The document-level CED score aggregates over all predicted triples, weighted by extraction correctness: triples that match ground-truth relations contribute their CED scores, while incorrect triples receive zero credit. This coupling ensures that CED rewards both faithful evidence and accurate extraction jointly.
77	
78	We also evaluate a \emph{flat-NLI} baseline that uses only the positive entailment score $p^+$ without the contrastive term. CED and flat-NLI produce comparable RSFT outcomes (mean Rel-F1 difference of 0.02pp across available seeds; Section~\ref{sec:analysis}), confirming that the contrastive formulation is not essential for data selection quality. We adopt CED as the default because its per-triple discrimination scores support interpretable error analysis.
79	
80	
81	\subsection{Evidence-Decoupling Ratio}
82	\label{sec:edcr}
83	
84	For analysis, we define the Evidence-Decoupling Ratio (EDCR) as a diagnostic metric that quantifies the degree of misalignment between a model's extraction and evidence capabilities. EDCR is not a training component; it serves purely as an analytical tool for comparing optimization methods.
85	
86	EDCR is defined as the distractor citation rate across all predicted triples:
87	\begin{equation}
88	\text{EDCR} = \frac{\sum_{i} |E_i^{\text{pred}} \setminus E_i^{\text{gold}}|}{\sum_{i} |E_i^{\text{pred}}|}
89	\label{eq:edcr}
90	\end{equation}
91	where the sum ranges over all predicted triples with at least one evidence citation. $E_i^{\text{pred}}$ is the set of evidence sentences cited for predicted triple $i$, and $E_i^{\text{gold}}$ is the corresponding gold evidence (empty for false-positive predictions). EDCR thus measures the fraction of all cited evidence that does not appear in the gold evidence for the associated triple.
92	
93	A model with many false-positive triples will have high EDCR because all evidence for incorrect triples counts as distractor; even among correct triples, citing irrelevant sentences inflates the numerator. Conversely, accurate extraction with faithful evidence yields low EDCR. This dual sensitivity makes EDCR a natural diagnostic for extraction-evidence decoupling.
94	
95	EDCR operates at two diagnostic levels. At the method level, comparing EDCR across seven unique method configurations reveals a negative correlation with Rel-F1 (Spearman $\rho{=}{-}0.96$, $n{=}7$, $p{<}0.001$). Because EDCR is mechanically influenced by false-positive triples (which share determinants with Rel-F1), this correlation should be interpreted as a diagnostic pattern rather than an independent discovery; its primary value lies in per-relation analysis. We validate EDCR's diagnostic utility through per-relation analysis (\S\ref{sec:analysis}), which avoids the shared-component concern present in cross-method correlation. At the per-relation level, computing EDCR for individual relation types reveals a robust negative correlation with Rel-F1 ($\rho{=}{-}0.79$, $n{=}76$, $p{<}0.001$) that is independent of Evi-F1 ($\rho{=}{-}0.06$, $p{=}0.58$). This independence means EDCR captures relation-specific extraction-evidence misalignment that aggregate evidence metrics miss. The SFT baseline EDCR (0.6797, three-seed mean) reflects the inherent distractor rate under standard training; EDCR values substantially exceeding this level (e.g., GRPO QLoRA at 0.9876) indicate RL-induced decoupling beyond what evidence production alone explains, while values below the baseline (e.g., RSFT at 0.6487) reflect improved co-optimization.
96	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e021d04-8e8b-4404-a49b-fc9634c32f07",
  "isSidechain": true,
  "promptId": "00884a06-3250-4c87-b491-3b7baf3c5516",
  "agentId": "a8128c193ad4a3e6b",
  "type": "user",
  "uuid": "b2420f7f-7b77-4cbb-95b0-e529090e4a8d",
  "sourceToolAssistantUUID": "9e021d04-8e8b-4404-a49b-fc9634c32f07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "7a362cc0-08ac-4cf8-8958-672775de0ebd",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "sprightly-popping-church"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T19:42:17.825Z_

<details open><summary>🔧 Tool call — Read · `toolu_016LCyfQLdr5BrfoJ6DETsQp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2420f7f-7b77-4cbb-95b0-e529090e4a8d",
  "isSidechain": true,
  "agentId": "a8128c193ad4a3e6b",
  "requestId": "req_011CbPrgtwWp5AUBrQAVXGQr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f0f97fb0-1bfb-40d3-9896-a391cd212b9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "7a362cc0-08ac-4cf8-8958-672775de0ebd",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "sprightly-popping-church",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01THtxoDrfucHbMKE7TgBqod",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 726,
      "cache_read_input_tokens": 39102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 726,
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

_source line 10 · 2026-05-25T19:42:17.831Z_

<details><summary>↩ Tool result · `toolu_016LCyfQLdr5BrfoJ6DETsQp`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\subsection{Document-Level Relation Extraction}
5	\label{sec:rw_docre}
6	
7	Encoder-based DocRE methods treat relation identification as classification over entity pair representations, with ATLOP \citep{zhou2021atlop} introducing adaptive thresholding and graph-based methods such as GAIN \citep{zeng2020gain} modeling inter-sentence reasoning. A parallel thread adds sentence-level evidence: SAIS \citep{xiao2022sais} introduced evidence supervision as an auxiliary signal, DREEAM \citep{ma2023dreeam} extended this with dynamic memory-based retrieval, and EIDER \citep{xie2022eider} fuses evidence into the relation classifier. In all three, evidence is binary sentence classification that regularizes the encoder without increasing output length.
8	
9	Recent LLM-based methods recast DocRE as generation: AutoRE \citep{autore2024} uses QLoRA with relation-head-facts decomposition, \citet{xu2024lmrc} frame extraction as reading comprehension, RelPrior \citep{wang2025relprior} leverages relation priors, and \citet{xu2025docksrag} combine retrieval with structured knowledge. These methods match or surpass encoder baselines but produce bare triplets without evidence. At 8B, our RSFT model (54.33 Ign-F1) outperforms AutoRE (52.14\footnote{AutoRE Ign-F1 from the LLaMA3-8B reproduction by \citet{wang2025relprior}; the original paper reports only F1.}) and is slightly below RelPrior ($-$1.17pp), while being the only method providing sentence-level evidence. The critical distinction is computational: in encoder methods, evidence retrieval is classification at negligible cost; in LLM-based DocRE, evidence requires generating additional tokens, imposing costs that depend on model capacity and optimization strategy.
10	
11	\subsection{Reinforcement Learning for Structured Generation}
12	\label{sec:rw_rl}
13	
14	GRPO \citep{shao2024deepseekmath} replaces PPO's \citep{schulman2017ppo} value network with group-relative advantages; DeepSeek-R1 \citep{deepseek2025r1} demonstrates its effectiveness at scale. Subsequent work addresses failure modes such as entropy collapse \citep{yu2025dapo} and length bias \citep{liu2025drgrpo}; applications to structured IE include R1-RE \citep{dai2025r1re} and REAR \citep{wang2025rear}. DPO \citep{rafailov2023direct} reformulates RLHF \citep{ouyang2022instructgpt} as implicit reward maximization. Our decoupling spectrum differs from catastrophic forgetting in RL alignment \citep{jin2025rl_panacea}: extraction and evidence compete \emph{within} a single task, resembling negative transfer in multi-task learning \citep{ruder2017overview}, amplified by QLoRA's \citep{dettmers2023qlora} constrained parameter space and capacity-dependent scaling dynamics \citep{gao2023scaling}.
15	
16	\subsection{Evidence Faithfulness and Rejection Sampling}
17	\label{sec:rw_faithfulness}
18	
19	NLI-based faithfulness evaluation \citep{laban2022summac,zhang2024infuse} and reward-based evidence grounding \citep{li2025srvf,tamo2026evidencerl} have addressed rationale quality in generation tasks. Our CED scoring targets evidence-relation entailment rather than free-form rationales. STaR \citep{zelikman2022star} introduced iterative self-improvement through rejection sampling; subsequent scaling analyses \citep{gulcehre2023rest,yuan2023rft} and theoretical connections to PPO \citep{tang2025rsftppo} have established the foundations of sample-and-select methods. RSFT extends this principle to structured IE, preserving extraction-evidence coupling through discrete selection rather than gradient pressure.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0f97fb0-1bfb-40d3-9896-a391cd212b9e",
  "isSidechain": true,
  "promptId": "00884a06-3250-4c87-b491-3b7baf3c5516",
  "agentId": "a8128c193ad4a3e6b",
  "type": "user",
  "uuid": "3c3febcd-3972-46ae-b6d6-e74db7d99425",
  "sourceToolAssistantUUID": "f0f97fb0-1bfb-40d3-9896-a391cd212b9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "7a362cc0-08ac-4cf8-8958-672775de0ebd",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "sprightly-popping-church"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-25T19:42:17.899Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FHA4YzgPDTJTLrp2pzSzoC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c3febcd-3972-46ae-b6d6-e74db7d99425",
  "isSidechain": true,
  "agentId": "a8128c193ad4a3e6b",
  "requestId": "req_011CbPrgtwWp5AUBrQAVXGQr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "03b9e554-e45c-41d1-acd4-a81494d3f68c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "7a362cc0-08ac-4cf8-8958-672775de0ebd",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "sprightly-popping-church",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01THtxoDrfucHbMKE7TgBqod",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 726,
      "cache_read_input_tokens": 39102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 726,
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

_source line 12 · 2026-05-25T19:42:17.904Z_

<details><summary>↩ Tool result · `toolu_01FHA4YzgPDTJTLrp2pzSzoC`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We study evidence-grounded document-level relation extraction as structured generation. The evidence tax is scale-dependent: gradient methods amplify extraction-evidence competition while RSFT avoids it through discrete selection, improving extraction across all tested scales; a 1.7B RSFT model approaches 8B SFT at 4.7$\times$ fewer parameters.
5	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03b9e554-e45c-41d1-acd4-a81494d3f68c",
  "isSidechain": true,
  "promptId": "00884a06-3250-4c87-b491-3b7baf3c5516",
  "agentId": "a8128c193ad4a3e6b",
  "type": "user",
  "uuid": "b4063bda-ef65-4cac-bccd-757543f2f41b",
  "sourceToolAssistantUUID": "03b9e554-e45c-41d1-acd4-a81494d3f68c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "7a362cc0-08ac-4cf8-8958-672775de0ebd",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "sprightly-popping-church"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-25T19:42:18.118Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ud7dv6tiAyrqjR39iZRoDA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4063bda-ef65-4cac-bccd-757543f2f41b",
  "isSidechain": true,
  "agentId": "a8128c193ad4a3e6b",
  "requestId": "req_011CbPrgtwWp5AUBrQAVXGQr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "27fe7ec9-1520-4f2a-a078-ea8f90c70be0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "7a362cc0-08ac-4cf8-8958-672775de0ebd",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "sprightly-popping-church",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01THtxoDrfucHbMKE7TgBqod",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 726,
      "cache_read_input_tokens": 39102,
      "output_tokens": 469,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 726
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 469,
          "cache_read_input_tokens": 39102,
          "cache_creation_input_tokens": 726,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 726,
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

_source line 14 · 2026-05-25T19:42:18.122Z_

<details><summary>↩ Tool result · `toolu_01Ud7dv6tiAyrqjR39iZRoDA`</summary>

```text
1	\section*{Limitations}
2	
3	\paragraph{Data and architecture scope.}
4	We evaluate on two datasets (DocRED, Re-DocRED), both derived from Wikipedia; cross-domain evaluation is constrained by the absence of evidence-annotated DocRE datasets beyond Wikipedia, a limitation shared by all prior evidence-aware work (SAIS, DREEAM, EIDER).
5	Evidence tax patterns span two model families (Qwen3, LLaMA) with single hyperparameter settings per RL method; other architectures, scales beyond 14B, or alternative KL coefficients may produce different decoupling behaviors. The decoupling spectrum analysis is conducted entirely at 4B scale; whether the same ordering (GRPO catastrophic $\to$ DPO gradual $\to$ RSFT none) holds at other scales remains unverified.
6	
7	\paragraph{CED scoring sensitivity.}
8	CED scoring operates at the document level using an external NLI model (DeBERTa-v3); sensitivity to other NLI model families is unexplored, and sentence-level CED filtering disrupts co-reference chains (Evi-F1 $-$7.7pp).
9	
10	\paragraph{RSFT mechanistic explanation.}
11	Our explanation for why RSFT avoids decoupling (that discrete selection cannot exploit the extraction-evidence trade-off) is structural rather than empirical. We have not isolated whether RSFT's advantage stems primarily from removing low-quality training examples, from implicit data augmentation through candidate diversity, or from both. Disentangling these factors would require controlled experiments with fixed training data quality but varied selection mechanisms.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27fe7ec9-1520-4f2a-a078-ea8f90c70be0",
  "isSidechain": true,
  "promptId": "00884a06-3250-4c87-b491-3b7baf3c5516",
  "agentId": "a8128c193ad4a3e6b",
  "type": "user",
  "uuid": "0341e4a4-0c06-4d10-a7b4-7c3dddd630f8",
  "sourceToolAssistantUUID": "27fe7ec9-1520-4f2a-a078-ea8f90c70be0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "7a362cc0-08ac-4cf8-8958-672775de0ebd",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "sprightly-popping-church"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-25T19:42:34.542Z_

Now I'll compile a comprehensive extraction of all numerical values from these 6 files:

## COMPREHENSIVE NUMERICAL VALUE EXTRACTION

### 1. abstract.tex

| Value | Line | Context |
|-------|------|---------|
| 1.7B | 2 | Model scale: "three fully evaluated scales (1.7B, 4B, 8B)" |
| 4B | 2 | Model scale |
| 8B | 2 | Model scale |
| 14B | 2 | Validation scale: "with 14B validation" |
| 5.63 | 2 | Evidence tax (pp): "beneficial at 1.7B ($-$5.63pp dev Ign-F1)" |
| 0.25 | 2 | Evidence tax (pp): "approximately neutral at $\geq$4B (+0.25$\pm$0.47pp at 4B)" |
| 0.47 | 2 | Evidence tax uncertainty (pp): "+0.25$\pm$0.47pp at 4B" |
| 0.79 | 2 | EDCR correlation: "validated at per-relation level ($\rho{=}{-}0.79$" |
| 76 | 2 | Sample size for EDCR: "n{=}76" |
| 51.19 | 2 | Ign-F1 of 1.7B RSFT model: "(51.19 Ign-F1)" |
| 50.19 | 2 | Ign-F1 of 8B SFT: "(50.19)" |
| 4.7 | 2 | Parameter efficiency multiplier: "4.7$\times$ fewer parameters" |
| 1.0 | 2 | Spearman rho: "Spearman $\rho{=}1.0$" |

### 2. introduction.tex

| Value | Line | Context |
|-------|------|---------|
| 1.7B | 25, 30, 32 | Model scale (multiple mentions) |
| 4B | 25, 30, 32 | Model scale (multiple mentions) |
| 8B | 25, 32 | Model scale (multiple mentions) |
| 14B | 28 | Validation scale: "with 14B validation" |
| 5.63 | 25, 30 | Evidence tax (pp): "$-$5.63pp Ign-F1" (multiple mentions) |
| 0.25 | 25 | Evidence tax (pp): "+0.25$\pm$0.47pp at 4B" |
| 0.47 | 25 | Uncertainty in evidence tax |
| 0.79 | 31 | EDCR correlation: "($\rho{=}{-}0.79$" |
| 76 | 31 | Sample size: "$n{=}76$" |
| 1.2 | 32 | RSFT improvement range (pp): "+1.2 to +6.6pp" |
| 6.6 | 32 | RSFT improvement range (pp): "+1.2 to +6.6pp" |
| 51.19 | 32 | 1.7B RSFT Ign-F1: "(51.19 Ign-F1)" |
| 50.19 | 32 | 8B SFT Ign-F1: "(50.19)" |
| 4.7 | 32 | Parameter efficiency: "4.7$\times$ fewer parameters" |
| 3 | 32 | Number of seeds: "$n{=}3$ seeds" |

### 3. method.tex

| Value | Line | Context |
|-------|------|---------|
| 64 | 22 | LoRA rank: "rank $r{=}64$" |
| 128 | 22 | LoRA scaling factor: "scaling factor $\alpha{=}128$" |
| 8 | 48, 54 | Number of groups/candidates: "$G{=}8$ groups" and "$N{=}8$ candidate outputs" |
| 1 | 54 | Top-k selection: "$k{=}1$ response" and "top-$k{=}1$ response" |
| 3000 | 54 | Training examples per model: "approximately 3,000 training examples" |
| 7 | 95 | Method configurations: "seven unique method configurations" |
| 0.96 | 95 | Spearman rho correlation: "Spearman $\rho{=}{-}0.96$" |
| 0.79 | 95 | Per-relation EDCR correlation: "($\rho{=}{-}0.79$" |
| 0.06 | 95 | Independence correlation: "($\rho{=}{-}0.06$" |
| 0.6797 | 95 | SFT baseline EDCR: "(0.6797, three-seed mean)" |
| 0.9876 | 95 | GRPO QLoRA EDCR: "(e.g., GRPO QLoRA at 0.9876)" |
| 0.6487 | 95 | RSFT EDCR: "(e.g., RSFT at 0.6487)" |
| 0.02 | 78 | Mean difference in Rel-F1: "mean Rel-F1 difference of 0.02pp" |

### 4. related_work.tex

| Value | Line | Context |
|-------|------|---------|
| 8B | 9 | Model scale: "At 8B" |
| 54.33 | 9 | RSFT Ign-F1: "(54.33 Ign-F1)" |
| 52.14 | 9 | AutoRE Ign-F1: "(52.14\footnote{...})" |
| 1.17 | 9 | Performance gap: "($-$1.17pp)" |

### 5. conclusion.tex

| Value | Line | Context |
|-------|------|---------|
| 1.7B | 4 | Model scale: "1.7B RSFT model" |
| 8B | 4 | Model scale: "8B SFT" |
| 4.7 | 4 | Parameter efficiency: "4.7$\times$ fewer parameters" |

### 6. limitations.tex

| Value | Line | Context |
|-------|------|---------|
| 7.7 | 8 | Evi-F1 drop: "Evi-F1 $-$7.7pp" |
| 4B | 5 | Scale of analysis: "conducted entirely at 4B scale" |

---

## SUMMARY BY CATEGORY

**Model Scales (distinct values):** 1.7B, 4B, 8B, 14B

**Performance Metrics (Ign-F1, Rel-F1, Evi-F1):** 51.19, 50.19, 54.33, 52.14, 0.02pp

**Evidence Tax Values:** -5.63pp, +0.25±0.47pp, -7.7pp

**EDCR Correlations:** -0.96, -0.79, -0.06

**EDCR Baseline Values:** 0.6797, 0.9876, 0.6487

**Statistical Values:** Spearman ρ = 1.0, n=76, n=7, n=3 seeds

**LoRA Hyperparameters:** rank=64, α=128

**Sampling Parameters:** G=8, N=8, k=1, ~3000 training examples

**Efficiency Metrics:** 4.7× fewer parameters

**Improvement Ranges:** +1.2 to +6.6pp, +0.25±0.47pp

**Other Numerical Values:** 2 datasets, 2 model families, 52.14, 1.17pp

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0341e4a4-0c06-4d10-a7b4-7c3dddd630f8",
  "isSidechain": true,
  "agentId": "a8128c193ad4a3e6b",
  "requestId": "req_011CbPrhAfZn2o3cieWtoVfT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "16dc1e9d-99fd-49c0-88c3-b2a7df72ca06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "7a362cc0-08ac-4cf8-8958-672775de0ebd",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "sprightly-popping-church",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UZc7iwjJ5jqj7JvSwmnK9C",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 8302,
      "cache_read_input_tokens": 39828,
      "output_tokens": 2015,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8302
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 2015,
          "cache_read_input_tokens": 39828,
          "cache_creation_input_tokens": 8302,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8302,
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
